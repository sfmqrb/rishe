# Verification process log — verify-page-383


## [2026-09-07T20:40:18.348Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 383 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-383.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-383.json. Write /home/sfmqrb/git/rishe/data/verification/page-383.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 383` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T20:40:20.328Z] AGENT

I'll start by reading the instructions.


## [2026-09-07T20:40:21.048Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T20:40:21.061Z] TOOL RESULT

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


## [2026-09-07T20:40:21.451Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-383.txt"
}
```


### [2026-09-07T20:40:21.464Z] TOOL RESULT

```
1	=== PDF page 383 (book page 353) ===
2	--- entry 0 ---
3	ROOT [Sanskrit] Parvan, Parvata : knot; knotty, rugged  (refs SYN:26)
4	#1 (parent #0) [Avestan] refs=SYN:26; BQT:401 | paurvatâ : mountain range ; paurvatâ-vac : sound of mountains, echo ☞Wekw
5	  #2 (parent #1) [Persian] refs=BQT:345,399,401 | paž «پژ ۱» : rough terrain, mountain ; pâpaž «پاپژ» : mountain range, rough terrain ; pažvâk, pežvâk «پژواک» : echo
6	--- entry 1 ---
7	ROOT Parvata -> redirect to Parvan
8	--- entry 2 ---
9	ROOT Pa-ter -> redirect to Pa
10	--- entry 3 ---
11	ROOT [Indo-European] Ped, Pod : foot  (refs POK:790)  PART 1
12	#1 (parent #0) [Avestan / Old Persian] refs=KLN:1112 | pâd, pâdha, pad, pada : foot, step
13	  #2 (parent #1) [Persian] refs=BQT:344,367; HRN:63 | pâ «پا» : foot, base ; pây-în «پایین» : towards the feet, down ; pâ-jâmeh «پاجامه» : pants, pajamas ☞Yôs | extra: پای ۱ ، پی ، پاچه ، پایه
14	  #3 (parent #1) [Hindustani] refs=HJB:748 | paě-jâma
15	    #4 (parent #3) [English] refs=AHD:943; KLN:1112; AID:234 | pajamas
16	      #5 (parent #4) [Persian] refs=MON:868,902 | pîjâmeh «پی جامه» | extra: پیژامه
17	  #6 (parent #1) [Avestan] refs=POK:790 | padika : walker ; padâtaka : pedestrian
18	    #7 (parent #6) [Persian] refs=BQT:434; NYB:147 | payk «پیک» : messenger ; piyâdeh «پیاده» : pedestrian
19	#8 (parent #0) [Sogdian] refs=SOD:270,273 | pd : foot ; pdny : heel
20	  #9 (parent #8) [Persian] refs=SOD:270; FRS:173; SLW:98 | pal «پَل» : heel
21	#10 (parent #0) [Latin] refs=AHD; KLN:1166 | ped : foot ; ped-yôs : lowest, worst
22	  #11 (parent #10) [English] refs=None | dispatch, impede, pedestrian, pessimism, pedicure
23	
```


## [2026-09-07T20:40:32.104Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-383.json",
 "description": "Read source JSON page 383"
}
```


### [2026-09-07T20:40:32.150Z] TOOL RESULT

```
{
  "pdf_page": 383,
  "book_page": 353,
  "entries": [
    {
      "root": {
        "name": "Parvan, Parvata",
        "lang": "Sanskrit",
        "refs": "SYN:26",
        "gloss": "knot; knotty, rugged"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "SYN:26; BQT:401",
          "words": [
            {
              "translit": "paurvatâ",
              "gloss": "mountain range",
              "script": null
            },
            {
              "translit": "paurvatâ-vac",
              "gloss": "sound of mountains, echo",
              "script": null,
              "see": [
                "Wekw"
              ]
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
          "refs": "BQT:345,399,401",
          "words": [
            {
              "translit": "paž",
              "gloss": "rough terrain, mountain",
              "script": "پژ ۱"
            },
            {
              "translit": "pâpaž",
              "gloss": "mountain range, rough terrain",
              "script": "پاپژ"
            },
            {
              "translit": "pažvâk, pežvâk",
              "gloss": "echo",
              "script": "پژواک"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "سفر خوش است کسی را که بامراد بود - اگر سراسر کوه و پژ آیدش در پیش",
            "poet": "Khosravânî"
          }
        }
      ]
    },
    {
      "root": {
        "name": "Parvata",
        "redirect": "Parvan"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Pa-ter",
        "redirect": "Pa"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Ped, Pod",
        "lang": "Indo-European",
        "refs": "POK:790",
        "gloss": "foot"
      },
      "part": 1,
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "KLN:1112",
          "words": [
            {
              "translit": "pâd, pâdha, pad, pada",
              "gloss": "foot, step",
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
          "refs": "BQT:344,367; HRN:63",
          "words": [
            {
              "translit": "pâ",
              "gloss": "foot, base",
              "script": "پا"
            },
            {
              "translit": "pây-în",
              "gloss": "towards the feet, down",
              "script": "پایین"
            },
            {
              "translit": "pâ-jâmeh",
              "gloss": "pants, pajamas",
              "script": "پاجامه",
              "see": [
                "Yôs"
              ]
            }
          ],
          "script_extra": "پای ۱ ، پی ، پاچه ، پایه",
          "note": null,
          "quote": {
            "text": "بشهر اندر آمد سراسر سپاه - پی را نبد بر زمین نیز راه",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Hindustani",
          "refs": "HJB:748",
          "words": [
            {
              "translit": "paě-jâma",
              "gloss": null,
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
          "lang": "English",
          "refs": "AHD:943; KLN:1112; AID:234",
          "words": [
            {
              "translit": "pajamas",
              "gloss": null,
              "script": null
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
          "refs": "MON:868,902",
          "words": [
            {
              "translit": "pîjâmeh",
              "gloss": null,
              "script": "پی جامه"
            }
          ],
          "script_extra": "پیژامه",
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 1,
          "lang": "Avestan",
          "refs": "POK:790",
          "words": [
            {
              "translit": "padika",
              "gloss": "walker",
              "script": null
            },
            {
              "translit": "padâtaka",
              "gloss": "pedestrian",
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
          "refs": "BQT:434; NYB:147",
          "words": [
            {
              "translit": "payk",
              "gloss": "messenger",
              "script": "پیک"
            },
            {
              "translit": "piyâdeh",
              "gloss": "pedestrian",
              "script": "پیاده"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "مرحبا ای پیک مشتاقان بگو پیغام دوست - تا کنم جان از سر رغبت فدای نام دوست",
            "poet": "Hâfez"
          }
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Sogdian",
          "refs": "SOD:270,273",
          "words": [
            {
              "translit": "pd",
              "gloss": "foot",
              "script": null
            },
            {
              "translit": "pdny",
              "gloss": "heel",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Persian",
          "refs": "SOD:270; FRS:173; SLW:98",
          "words": [
            {
              "translit": "pal",
              "gloss": "heel",
              "script": "پَل"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "همیشه کفش و پلش را کفیده بینم من - بجای کفش و پلش دل کفیده بایستی",
            "poet": "Ma'rûfî"
          }
        },
        {
          "id": 10,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD; KLN:1166",
          "words": [
            {
              "translit": "ped",
              "gloss": "foot",
              "script": null
            },
            {
              "translit": "ped-yôs",
              "gloss": "lowest, worst",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "English",
          "refs": null,
          "words": [
            {
              "translit": "dispatch, impede, pedestrian, pessimism, pedicure",
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


## [2026-09-07T20:40:32.407Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-07T20:40:32.445Z] TOOL RESULT

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


## [2026-09-07T20:40:40.766Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['SYN','BQT','POK','KLN','HRN','HJB','AHD','AID','MON','NYB','SOD','FRS','SLW','IEC','WLD','BRT','KNT','PHD','HUB','ARY','SKT','LKT','FSD','WEB','LEW','LAT']:\n    v=d.get(k)\n    print(k, json.dumps(v,ensure_ascii=False)[:600] if v else 'MISSING')\n    print()\n\""
}
```


### [2026-09-07T20:40:42.053Z] TOOL RESULT

```
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

HJB {"title": "H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)", "edition_found": "1903 Crooke edition (pagination identical to the 1968 reprint)", "kind": "archive_djvu", "url": "https://archive.org/details/hobsonjobsonagl02croogoog", "identifier": "hobsonjobsonagl02croogoog (others: bub_gb_6Z5iAAAAMAAJ, hobsonjobsonglos00yulerich, india.history.resource.89053)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt", "page_offset": "leaf = printed + 35..51 (plates inserted; e.g. leaf 83 = p.32, leaf 319 = p.270, leaf 535 = p.4

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

AID {"title": "G. C. Whitworth, An Anglo-Indian Dictionary, London 1885", "edition_found": "1885 (DLI scan); also 1981 reprint scan", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.45332", "identifier": "in.ernet.dli.2015.45332 (also anglo-indiandictionary, 1981 reprint)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AID.txt", "page_offset": "leaf = printed + 18 (e.g. leaf 20 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lo

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=

FRS {"title": "Asadi Tusi, Loghat-e Fors, ed. Mojtaba'i & Sadeqi, Kharazmi 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/LughatEFurs-AbuMansurAliBinAhmadAsadiTusiFarsi (Abbas Eqbal's 1319/1940 Tehran edition); also dli.ernet.439493 / dli.ernet.437743 (Horn's 1897 Göttingen edition, 'Lughat Faras')", "lookup_hint": "Look up the headword (entries grouped by final letter); FRS_pages.txt has \\f page breaks (567 leaves). Pagination differs from the 1365 Kharazmi edition Nourai cites — verify the entry, not the page.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/s

SLW {"title": "W. B. Henning, 'Sogdian Loan-Words in New Persian', BSOAS 10.1 (1939) pp. 93-106", "edition_found": "reprint in W. B. Henning Selected Papers I (Acta Iranica 14, 1977) - different pagination; original in JSTOR", "kind": "archive_djvu", "url": "https://archive.org/details/w.-b.-henning-selected-papers", "identifier": "w.-b.-henning-selected-papers (also w.-b.-henning-selected-papers_202108)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HENNING_selected_papers.txt", "page_offset": "Selected Papers scan: leaf = p + 12 for the front matter; reprinted articles ke

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 

FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt

WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W

LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f b

LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for mos
```


## [2026-09-07T20:40:47.141Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==50 || NR==51' SYN.txt | head -120",
 "description": "Buck p.26 (leaf 50/51)"
}
```


## [2026-09-07T20:40:47.819Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"parvata\\|párvata\\|parvan\\|párvan\" SYN.txt | head -40",
 "description": "grep parvata in Buck"
}
```


### [2026-09-07T20:40:48.401Z] TOOL RESULT

```
acq 128 f.
2. Lat. mons, montis (> It. monte, etc.), W. mynydd, Corn. meneth, Br. menez ‘mountain’, Av. mati- ‘mountain top’, fr. the root seen in Lat. é-, pré- mineére ‘stand out, project’ (cf. NE eminence, prominence in physical sense), minae ‘projecting points, threats’. Walde-P. 2.263. Ernout-M. 628 f.
Lat. adj. monténus, VLat. *mon- taneus (cf. subterrdneus, etc.), neut. pl. *montanea ‘mountainous regions, moun- tain chain’, whence It. montagna, OFr. montai(g)ne (> ME mountain), Fr. montagne, Sp. montafia, which have en- croached on the shorter form or even displaced it. Sp. monte now ‘woods’. REW 5664, 5666.
Lat. collis, : Grk. xodwvés, ete., above, 2. Hence It. colle, collina, Fr. colline, Sp. colina, collado, Rum. colina (neolog.).
Lat. clivus ‘slope, hill’ : Goth. Alains ‘hill’, Grk. Airs ‘slope, hillside’, fr. IE *klet- ‘bend, incline’, in Lat. clinare, Grk. KXtvea, Skt. cri-, NE lean, ete. Walde-P. 1.490 ff. Ernout-M. 197f. Walde-H. 1. 236.
Sp. cerro ‘hill’, also ‘back of the neck, spine’, fr. Lat. cirrus ‘tuft of feathers, crest (of birds)’, REW 1949. Other Sp. words for ‘hill’ are otero fr. Lat.
altarium ‘high altar’, poyo (cf. It. poggio ‘hill’, Fr. pui in place names) fr. Lat. podium ‘balcony’. Cf. Menéndez-Pidal, Orig. del espafiol 425 ff.
Rum. deal ‘hill’, loanword fr. Bulg., SCr.-ChSl. délit ‘part’, through ‘bound- ary’. Tiktin 515. Berneker 195.
3. Ir. sliab, NIr. sliabh ‘mountain’ : W. llyfr ‘heel of a drag’, OHG slitfan ‘slip, glide’, etc. (*sleib- beside *sleidh- and *sleub-, Walde-P. 2.391, 707, 710), the development being through ‘slope’ (cf. NE slope fr. pple. of OF slitpan ‘slip’), hence ‘hill’ (cf. Lat. clivus, Goth. hlains, above), ‘mountain’. Thurneysen, Gram. 117. Stokes 319. Pedersen 1.84.
W. mynydd, Br. menez ‘mountain’ : Lat. mons, etc., above, 2.
Ir. telach, tulach ‘hill’ (also NIr. in phrases) : Grk. ridy ‘swelling’, Lat. tu- mulus ‘mound’, etc. Walde-P. 1.71@.
Tr. cnoc ‘hill’, Br. krec’h, OBr. knoch (W. cnwceh ‘boss, knuckle’) : ON hnakki ‘nape of the neck’, NE neck, etc. Walde-P. 1.390 ff. Pedersen 1.160.
Ir. bri, W., Br., Corn. bre ‘hill’ : OF beorg, etc. below, 4.
W. bryn ‘hill’ : Ir. bruinne, W. bronn ‘breast’, Ir, bri, W. bru ‘belly, womb’, NE breast, etc. Walde-P. 2.197. Peder- sen 1.86, 376.
4, Goth. fairguni ‘mountain’ : OF firgen in epds., as firgen-gat ‘mountain goat’, and prob. a loanword fr. Celtic *perkunia, represented by Hercynia silva (with regular Celtic loss of initial p), this further connected with Lat. quercus ‘oak’, Relation between ‘woods’ and ‘(wooded) mountain’, as elsewhere. Walde-P. 2.48. Feist 137 ff.
Goth. hlains ‘hill’ : Lat. clivus, etc., above, 2.
ON fjall (fell), Dan. fjeld ‘mountain’, Sw. fjall ‘high mountain’ (ME, NE fell fr. ON) : OHG felis, NHG fels ‘rock’, Skt. pasana- ‘stone’, etc. (1.44). AL
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
cr ee ra SS NR
|
Digitized by Arya Samaj Foundation Chennai and eGangotri
THE PHYSICAL WORLD IN ITS LARGER ASPECTS 25
though the root connection is uncertain, the sense ‘rock, stone’ is more widely dis- tributed and prob. earlier. Walde-P. 9.66. Falk-Torp 223.
Dan. bjerg, Sw. berg, OE beorg (‘moun- tain, hill’ and ‘burial mound’, in former sense replaced by the Fr. forms, in the latter sense NE barrow), OHG
, NHG berg, etc., the most widespread Gmce. word for ‘mountain’ (but ON bjarg ‘rock, precipice’; in Goth. only bazrga- het = dpewh ‘hill country’) : Skt. brhant- ‘high, great’, Av. barazant- ‘high’, bara- zah- ‘height, mountain’, Arm. berj ‘height’, Ir. bri, ace. brig, W., Br. bre ‘hill’. Walde-P. 2.172 ff. Falk-Torp 77.
OE din ‘mountain, hill’ (NE down), ODu. dina (> Du. duin ‘sandhill’, Fr., NE dune), formerly believed to be a loanword fr. Celtic (Ir. din ‘fortified place’), but this is now generally doubt- ed; perh. fr. the root seen in Skt. dhu- ‘shake’, etc., with development similar to that in Grk. 6ts, @tvds ‘sandbank’ (*Of-tv-). Walde-P.:1.837. Falk-Torp 171. Franck-v. W.141. NED sv. down, sb.
OE munt fr. Lat. méns, montis; ME mount, mountain fr. OFr. mont, mon- tat(g)ne (above, 2).
OK hyll, ME, NE hill : Grk. xodwvés, Lat. collis, etc. (above, 1).
Dan. bakke, Sw. backe ‘hill’ : ON bakki bank’, NE bank, etc. (1.33). Walde-P. 2.148,
Du. heuvel, MAG hiibel ‘hill’ : OHG hovar, OE hofer ‘hump’, Lith. kupra ‘hump’. Here also Av. kaofa- ‘mountain peak, camel’s hump’, OPers. kaufa Mountain’ (NPers. kwh ‘mountain’) : Lith. kaupas, ChSl. kupt, NE heap, NHG haufe ‘heap’, Grk. xidés ‘bent’, all fr. TE *keup-, *keub-, *keubh- in words for ‘bend, curve’. Walde-P. 1.372 ff. oh ha a Gor, pe mound’, fr, the adj. seen in
- hauhs, OHG hoh, ete. ‘high’
(12.31), ultimately connected with the preceding group *keubh-, etc., above. Walde-P. 1.371. Hence also NHG hiigel ‘hill’, by blend with MHG hibel. In the same group Dan. hoj ‘hill’ : hoj ‘high’, like NHG héhe, NE height fr. the respec- tive adj. forms.
OHG buhil, MHG bdihel ‘hill’ : ON bola ‘blister, boss’, prob. fr. an exten- sion of IK *bhu- beside *bu- in words for ‘swell’ (cf. Grk. Bouvds, above, 1). Walde-P. 2.114, 146.
5. Lith. kalnas, etc. : Lat. collis, etc., above, 1.
6. ChSl. gora, etc., general Slavic for ‘mountain’ (in some regions ‘forest’, as always Lith. gire, 1.41) : Skt. giri-, Av. gairi- ‘mountain’, and prob. Alb. gur ‘stone’. Walde-P. 1.682. Berneker 329. Further connection with Skt. guru-, Grk. Bapis ‘heavy’, through the notion of ‘heavy, solid mass’ (Thumb, IF 9.299) is plausible. Cf. Skt. acala- ‘mountain’ fr. adj. acala- ‘immovable’.
ChSl. chliimu, SCr. hum, Boh. chlum, Russ. cholm, the most widespread Slavic word for ‘hill’, is prob. a Gme. loanword (LG holm ‘hill’, etc., above, 2). So Berneker 410f., Stender-Petersen 263 ff.; otherwise Brickner, KZ 48.194.
The usual Boh. and Pol. words for ‘hill’ are dims. of gora, as Boh. pahorek, Pol. pagérek, wzgérek.
SCr. brdo ‘height’ (‘mountain’ or ‘hill’), late ChSI. brido, etc., either cog- nate with or loanword fr. the Gmc. group OHG bort ‘edge’, etc. Walde-P. 2.163. Berneker 118 f. Stender-Petersen 267 f.
SCr. brijeg ‘height, hill’ (dim. brezul- jak), also ‘shor
```


### [2026-09-07T20:40:48.450Z] TOOL RESULT

```
955:line hill Pol. gora; pagérek, Sp. montajia; colina, cerro Du. berg; heuvel wzg6rek Rum. munte; deal, colina OHG _ berg; buhil, houc Russ. gora; cholm Ir. sliab; telach, cnoc, bri MHG berg; biihel, hiibel, Skt. giri-, parvata-, acala-, NIr. — sliabh; cnoc (tulach) houc etc. W. mynydd; bryn (bre) NHG berg; hiigel Av. gairi-, paurvata, bara- Br. menez; Icrec’h, bre zah-, OPers. kaufa.
1016:Skt. parvata- ‘mountain, mountain range, rock’, Av. paurvata- ‘mountain range’, fr. adj. Skt. parvata- ‘knotty, rugged’, fr. parvan- ‘knot’.
```


## [2026-09-07T20:40:53.500Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('SYN.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor ln in (955,1016):\n    off=sum(len(l)+1 for l in lines[:ln-1])\n    leaf=t[:off].count('\\f')\n    print(ln,'leaf',leaf,'printed p.',leaf-24)\nprint('---context 1016---')\nprint('\\n'.join(lines[1010:1022]))\nEOF"
}
```


### [2026-09-07T20:40:54.817Z] TOOL RESULT

```
955 leaf 48 printed p. 24
1016 leaf 51 printed p. 27
---context 1016---
Boh. vrch ‘top, summit’ (as ChSl. vrichit, etc. 12.33), used also for ‘moun- tain’.
Boh. kopec ‘hill’, fr. kopa ‘heap’. Ber- neker 562.
7. Skt. giri-, Av. gairt- : ChSl. gora, etc., above, 5.
Av. barazah- : OE beorg, etc., above, 4.
OPers. kaufa-: Du. heuvel, etc., above, 4.
Skt. parvata- ‘mountain, mountain range, rock’, Av. paurvata- ‘mountain range’, fr. adj. Skt. parvata- ‘knotty, rugged’, fr. parvan- ‘knot’.
Skt. acala- ‘mountain’ fr. adj. acala- “Smmovable’.
Skt. ¢azla- ‘mountain’, fr. ¢ila- ‘stone, rock’.
1.28 PLAIN, FIELD
Grk. zedlov Goth. stabs ibns Lith.
NG medlov, wedtada, Kauros ON slétta
lyguma, laukas Lett. lidzenums, lauks
```


## [2026-09-07T20:41:08.804Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"پژواک\\|پاپژ\" BQT_v1_pages.txt | head -20\necho \"=== pdf page tags near ===\"\ngrep -c \"\" BQT_v1_pages.txt"
}
```


### [2026-09-07T20:41:08.879Z] TOOL RESULT

```
=== pdf page tags near ===
32486
```


## [2026-09-07T20:41:08.991Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"paurvata\\|pauruuata\\|paurvatā\" BRT.txt | head -20"
}
```


### [2026-09-07T20:41:09.046Z] TOOL RESULT

```
11080:yä^a*  ..  YLÄ48;  — fravasayS  ..yqmca J^rS  , .  yqmca  sraolahe  yqmca^  . .  Yt  13. 85  f.;  —  yaica  aahat  %wyqst)mailu  asa- nhqm  yatca  anAai  iar^snufpaiti  gatrinam yatca  jqfnusha  raonam  V.2.a3;  —  drjgva- tal'ä  hyailä  *alaom  yehyä^ä  ASmimyä- saiti , ,  Y,  ji^.  I ;  —  paurvatatim  mana- T»hascS  vaahsm  .  .  iyaohanahyä  .  .  ySeä ux%aAyäiä  '^.33.  14.  2)  die  Glieder sind  verbal;  sie  folgen  sich  unmittelbar: Ayat  T  mainimadicä  vaocöimäcä  vir>zimäca Y.J5.3;  —  ya^ä  ta  l  .  .  mSngkacS  vao- casca  äascs  vanlcä  . .  \.3g.ä,;  —  mistt ,  ,  väntUafca  snaÜiniaBca  srascintalca *Jyai3kttnla^a  Yt. 5.120;  —  yat  ähnmca akoi.vaxiayat  ahrasca  tisrS  ^raxti^ yaoi- daiaf  sao&ralca  vScim  paiH.^<rf3t  N. 7J.  a)  mitTmesis;_yfrJöflftVa  var^atica saosyantica  aiwica  asäi(e(sd.)  jämayäiti  A. 4,6;  —  äca  nS  jamyät  avaiiihe  äca'i  70 jamyap  Yt /o.  5.  4)  in  abweichender
19779:vahiita—,  yaT  tat/  a%a  hatä.maräta  (sd.) vahista  vdiitä  •naaha  Y.J2.6>';  —  *df nS  maiJa  . .  vatthtul/radaxüa  (sd.)  °tuwhs Y.  J/.  17*';  —  king  a  vanA^ii/ ßmaj •naaAS  ^istü  {sA.)  Y.^.ii«;  44- 16*'; —  ya%a  ns  a  vohü  jimai  (sd.)  •naaha (als  Subj.)«  Y.  44.1«;  —  axsß  {n^) vanhJui  alä  ÜtTm  'navhB  Y.  46.  3^>; 32.  9*);  —  vatafOus  °nai»Jü5  syao%ana vaolai  ginhqm  (sd.)  huxratui  Y.34.  io*>; ^o.  io^>;  —  t^g  zhayä  (sd.)  vanhSus uxlaii  •nanhs  Y.46. 14**;  —  mat  vä  . . pairi/asai  .  .  vaiakfui  •nat)AS  ktmantäta (sd.)  Y.50.8'';  —  vanhSus..  kaotq%wat (sd.)  ä  'nanhsY.45.'i^''>  —  ahurim  aia- vafom  vanhTui  ßiT^hfm  (sd.)  'naaks  Y. J/.  lO^J;  —  'naahö  VawAj«/*'  i/ft/J  (sd.) Y.57. 18*';  —  yBi . .  ärmaitim  . .  duL^ao- %anä  avatazat  va»Afui  2vistT  (sd.)  •naahs Y.^4.9«;  —  yöi  ziahiitäi  *aiaonö  .  . rar7^an(s±)  'na»h6Y.32.  ii»;  —  doTvö.- tu/tä  (sd.)  vaisAfuI  sfSdyamna  (sd.)  °naahs matdä  .  .  xraiJus  nasyanio  (sd.)  aSaatca Y.^2.4*>; —  kuda  (sd.)  a/»m  vohuia  'n3 x/a^fvmia  Y,  2().  II*';  —  ySHg  a/aat^ä vSistä  vanfOufcit  . .  'naiaAff  »n%w9ng  (sd.) Y.  28. 10»;  —  y!  aii  as>m  nipätihl  (sd) 'nas^a  vohü  Y.aÄiis);  —  tat^a  %wahmt *a  *dqm  (Sp.  684  o.)  nipätshl  'nS  vohü urunasca  asäunqm  Y.^p.  10*';  verwendet 42.4;  —  inYHapL:  vohü  ^ma  •nat3ha voha  "kwa  asa  .  .  pairijas3maidl  Y.  36. 4'°*-  «)  im  Gegensatz  zu  Sprechen und  Handeln:  vahÜtaca  'naaha  aiä£(Sp. 231  m.)  ha/a  fyao%anäSt  vatanhai'a  Y. 47.1"*;  —  paurvatatim  (sd.)   'nanhasiä
20658:mit  paitt  'antworten''*:  paiti.mrüiai paurvatan  Y.  yi.i;  —  bays.baxtB  paiti.- mruyä  Vyt.  25  (?).  a)  Jemandem  (Dat) :
20846:pairijasai  .  .  maiiyJ  dävBi  Y,  2Ä2;  — y7  va  . .  ufyanj  ä  mSi . .  jasata  Y.  28. 3 ; J'J.  1 1 ;  ~  ys  nipänkE  ..  JrS  ma  sn'ä  Y. 28.11;  —  die  Beziehung  ist  ungenau,  in- sofern die  Person  wechselt  und  statt  des Gen.  des  Pron.  pers.  das  Pron  poss. steht  (s.  Sp.  4  m.):  y!  mq%ra  (sd.)  vaHm . .  baraitl  zara^uströ  data  .  .  AisvS  rai- %Im  (sd.)  stöi  mahya  rassng  .  .  sahit  Y. ^o.  6.  B)  eine  Bezugsmasse  ist  (äusser- hch)  nicht  vorhanden,  sondern  —  in  irgend einem  durch  den  Zusammenhang  gebotenen Kasus  — zu  ergänzen;  a)  im  gAw.''*;  das Relativ  ist  a)  substantivisch;  zu  1):  mazda dadat . .  vazdvarS  (sd.)  .  .yS  hSi  . .  urvdhö (sd.)  "^,  dabit ..  pcrpetuitatem..(ei)qui.. amicus"  '^.31. 2 1 ;  jj.  11;  —  y}  ahUm  (sd.) iiasqs  aibl . .  mraol  "qui  .  .  Studiosus  .  . (ei) '. ."  Y.  51. 19;  —  sardi  bsidyät  (sd.) . .  yy  rä^imö  .  .  "coniungi  .  .  (cum  eo) qui.,"  Y.44. 17;  —  ay^  *mainivä  varata yS  dngvh  "eorum  spirituum  . .  (is)  qui fallax"  Y.^JO.  5 ;  —  ;'^  (zu  3) . .  drlta  ayant^m urvatJis  (sd.)  .  .  yj  ahvä  dr>gvant3m  vi- arS hqs  la^  frö ..mruyat  ",.qui,.(is)  ,."  Y. 4('-Z',  —  paurvatabm  {&d^)  manatthasca vanhlul  .  .  syaohanahya  .  .  j;yä{'aS{.ya uxQaüyaai  "prioratum   et  bene  cogitandi
20847:I  et  (eum)  qui  (est)  faciendi  et  dicendi" I  Y.  33. 14;  —  *grSkms . .  atikSus  maraxtärB I  (sd.)  ahya  \yai(a  ^'Grlhmas  . .  et  (ii)  qui (sunt) ..  destructores"  Y.J2. 13; —  ku%ra töi  andrS  (sd.)  .  .  yöi  .  ,  caxrays  "num tibi  (sunt)  fidi  (ü)  qui  . ,"  Y.^4.7;  — kada  .  .  yOi  uxiäiiS  ainqm  .  .  frärmtl "quando  . .  (ii)  qui  (sunt)  tauri  .  ."  Y.  4G. 3;  —  naldä  dahySus  \ydi  iastSrS  drjsvatas "neque  (ii)  qui  (sunt)  . .  imperatores"  Y. 4O.  I ;  —  tat  ..  uitanai  data  . .  ySi  sl gSus  v^nzinl  (sd.)  azyi  ".  .  vitae  (eorum) qui  .  ."  Y.  34.  14;  —  tim  at  yasna- nqm  paurvataia  yazamaidl  ySi  ..  iyeintJ ".  .  imprecationum  .  .  (eorum)  qui  .  ." ^•37-  2;  —  yi  varpsaiil  (sd.)  kyat vasnä  firasöJ^mim  "qui  . .  fecerit  . .  (id) quod  (est)  .  ."  "^.46.  19;  —  hyatcS dar>gSm  dr)gvll.d»byS  rasB  savai'a  alavabyö "et  (id)  quod  (est)  . .  damnum  et  lucra  . ." Y._jo.  11;  —  Aaihyavanitqm  {%A.)  hyat vasna  f?rasS.t}m}m  "verificationem  (eius) quod.."  Y. 50.11;  —  ai  zt  töi  vaxsya .. hyai  aksyä  (NSf.;  sd.)  dngvaiii  wörtlich ",.  von  dem,  was  die  Androhung  ist,,"  Y, 51.  8;  —  hyat  "qsasutä  (sd.)  yä  (NPn.) daiiiiana  (sd.)  fraoxta  "..  (ea)  quae  (sunt) . .  enuntiata"  Y.  48.  1 ;  —  das  Relativ  kon- gruirt  mit  dem  Praedikat:  vldvä  yalclt güzra  (sd.)  singhanhS  (wörtlich)  "kennend auch  (das),  was  die  geheimen  Lehren  (sind)" Y.4<V,3;  —  anais  a  vT.nSnasa  ya  (NSt) iarapsjis{ad.}cä  kjvltäscä  Y._J2.  15;  — *m>ndäiäyai  (sd.)  ya  (NSf)  toi  adisHi Y.44.8;  5,^.13;  —  nipatihw . .  tumas^a ya  armaitiH&d.)  Tiilcä  Y.4g.  10;  —  yS va  mSi  \yh  (NPf)  gasha  dasdi  (Sp. 7 1 S  u.)  *asnatihe  wörtlich  ". .  (das),  was meine  Besitztümer  (sind)  .  ."  Y,  46. 8;  — vtayUta  yä  (NPn.)  mrqi  sädra  drtgvats (wörtlich)  "immer  (wird  sein)  was  die Qualen  (sind)  .  ."   Y.45.  7;  43-5,  49-6;
21429:paurvatatä  yazamaidi  Y.^7.  a;^p,  4;  —
23267:•  J.  vaäan-  m.  —  ?  -,  Plur.  mit  asta Name  eines  Gebirgs:  ahmai  haca  garayS fraoxfyqn  . .  aita  *sanu  paurvata  ". ,  <ks Gebirg  'die  acht  V.'"  Yt/5.3.
27788:•  j.,  g.  zaraO'uätra-  m.  EN.  des  Stifters der  mosi/ischen  Religion,  aus  der  Spitatna- (sd.)familie,  Sohns  des  Poumfaspa  und der  iJwySii.wa*);  a)  im  gAw.:  aim  möi idä  visiJ  (Sp.  1315  u.)  yf  n}  afvS  säsnä (sd.)  gäiatä  'rS  spitämö  hvS  ta  . .  vaHl . . iankirg^ra  {sA.)  iravayetihl  Y.2t>.  8;  — yS  mq%rä  (sd.)  *vaam  .  .  baraitT  urva%ö as'd  tumar?hs  'r3  Y.J0.6;  —  a^  ahurS hv5  mainyäm  'rS  V3rmtlmazda  yasß  Hlca spSnisiS  Y. 4?- 16;  —  at  höi  aoji{zA.)  'rS paourvim  ^hai^ys.dvaisa  .  .  Y.  4j,  8;  — at  ratqm  (sd.)  °r5  lanvascl£  ifaAyä  ustartsm dadäitl  paurvatatjm  (sd.)  ^.33.  14;  — hyal    mlidim    °rS    magavabyB  (sd.)    iBist
28733:%ai  . .  haraihyS  paiti  bamayä;  äat  ^wä . .  spmta  , .  mtnya  vlivama  vlbann  . .  Sat ttkva  paurvatahva  pouru.sar3hs  viraehahe 'mS  gaoma  zairi^aoiiB;  H  tl  ba^ata  irJ- ra'iar»  (sd)  .  .  Y.IO.  lofF.;  —  vlipe  'ma ufasiaomi  yoteit  barlnusva  gairinqm yaieii  jafnuSva  raonqm  yaiäi  atahu  thn- tanko. .  V.10.1 7; — yi>  barfsman  */rasl?r>nte 'mqsca  var^sisd.)ca  ..  ti.gj;  —  •m^m täirim  binzantifn  ..'m?m  fra^mim  frädat.- gafi-»>n  'mim  düraosim  yatamaide  Y.  lO. 3i;  7f.i,  Vr.  //.  a',  V.J9.19;  —  pasi^a fra»uharHÜ  'inahe  huiahe  H.  1. 9;  — vai>hus  *mö  huiätö  °mS  .  .  zairi^aons namyqsul  yaia  :^arinte  vahiitS  urunaica ps'^mainyB.hmö  Y.t).i6;  —  äriiyj  . .  ä/ri- Z'acaahs  zavainti  gäul^a  aspasc'a  'masca . .  'mS  ^älär»m  (sd.)  tavaiti  . .  Y.  //. 1—3;  — yasf  ti  bäla  °ma  zlire  gava iristoAe  baxsatte  'S..  10.  13;  —  hd yS  'mähe maid  (sd.)  asa  hacaite  urvilsmana  Y.  10.  8 ; YL  /7.  S  ;  —  nnjaiti  'mähe  mmö  Y.  lo.  8 ; —  als  Amulet;  'mim  batre  (Sp.  933  u.) *slliriJ)aoy»m  .  .  'imin  yim  nivizaili  (sd.) uivandät  apayettt  Vt  /4-  5  7 ;  S  7 ;  —  'm Kult;  'ma  .  .  asaya  kuitvana  asaya  hag- syanta  Vr,  g.  3  ;  12.  x,  3,  Y.g.  3,  4,  V.  18. 1 2 ;  — /rab?rita  *zaoi:ra  frabarStl. .  hävana 'man  hunyät  N.  61?;  —  hävananS  (näml. kairim  aahat)yal'mimca  ahunavat  anha- vammia  *vlmanitt  (Sp.  1135  u.)  ,.  *äsna- iars  yat  'mfmca  äsnayät  °m>mca  pairi.- hanzM . .  ^raehwiskarake  (sd.)  yat  'm^m^a gtiva  *rai'iaiay>Jt  baxsayäatla  N.j2-y6;  — 'manqmca  har.'iyamnanqm  ySi  hansyente ra^we  bimaiie  Vr. /2.  i;  Y.  2y.f>;  —  °m)m aiaya  usdutun  (Stverz.  Sp.  719  o.)  Y.  22. I  i  usw. ;  —  ahuräi  mazdäi  'ma  Sva^ia- yamoAl  Yi.ii.i;  i',  Yt.io.120;  —  imq 'mqsla  myazdqsia  zao%räsca  barasmala  . . gqmca  huiiänk)m  ..*m3mca paraMaomimca aismqsca  baothlmla  . .  pairica  dad»mahl . . Y.4'1;  3Z,7-i(>,  ''''■h  "3;  Vr.p.3, //.  3;  —  hSvanaca  tastaca  °maca  V. /fj.  9; 5.  39;  —  kal  in  'ma  yaozdayan  aahtn  . . yä  nasäum  avaJiirtta  .  .1  V.6.43;  —  neil 'mB  hutB  axtU , .  nSit  *nasus.ava.b3r>tS  (sd.) ava  alte  ahuta . .Y . 6. 4y,  — yö..aiiaiaons 'mähe  kutake  dalaiti  Y.iS.ia;  —  *jarsi/ *'r/wn''>  zarähusira  .  .  yaka  *%risar>m nitim^m  P.2p,  A) alsGottheit**>'*:  wni5 'mai  Y.p.3,  16,  /o.  13,  17,  Yt/7.  S;  — 'ntü   upail  tard>!uitr»m  .  .  ä  dtm  pmsat
29419:•  j.  hamankuna-  m,  —  ?  — ,  Du,  mit  äva- Name  eines  Gebirgs:  ahmal  hala  garayS fraexfyqn  .  .  dva  'na  paurvata  ".  .  das Gebirg  'die  zwei  H'"  Ytjp. 3.
```


## [2026-09-07T20:41:16.197Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"paurvata-\\|paurvatä-\\|pauruuata-\" BRT.txt | head\necho \"=== also gairi/parvan ===\"\ngrep -n \"^.\\{0,40\\}parvan\" BRT.txt | head"
}
```


### [2026-09-07T20:41:17.668Z] TOOL RESULT

```
15735:•  j.  paurvatä-  f.  'Bergzug,  -kette,  Gebirg":
=== also gairi/parvan ===
```


## [2026-09-07T20:41:17.724Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor f in BQT_v1_pages.txt BQT_v2_pages.txt incoming/BQT/BQT_v3_pages.txt; do echo \"## $f\"; grep -c \"پژواک\" $f 2>/dev/null; grep -n \"پژ\" $f 2>/dev/null | head -3; done"
}
```


### [2026-09-07T20:41:19.043Z] TOOL RESULT

```
## BQT_v1_pages.txt
0
1901:داشته - دیگر رسالةً موسوم به « زور باستانی » که حکیم آند پژوه پارسی زردشتی دد تحقیق
7513:کاهی تازماند و گاهی پژمرده و سرو از این ها
17812:و پژمرده شد - وفراهم آمد - ویین‌چین کردید.
## BQT_v2_pages.txt
0
7292:                ‫گزبد ‪ :‬ای‌فوك چنگلوك چو پژمرده‌ب رکه كوك خواهی که چون چکوك ببری سوی هوا‪.‬‬
16391:‫د بکر بای فارسی‬         ‫دانش پژوه‬                            ‫بفتح‌ثالك وواو وبای‬                  ‫دانج و بر ‪1‬‬
16394: ‫وفضل جوینده وطالب علم‌باشد چه پژوه جوننده‬                  ‫تخمی است زردرنگه وطعم آن نلخ میباشد و از‬
## incoming/BQT/BQT_v3_pages.txt
0
2473:« بپژاد » است ء ‎only‏ اشتباء ازین بیتهای فردوسی طوسی ناشی شده :
3597:‏صفیی زدن باشد - وپژمرده شدن را ‎jh‏ گویند.
3668:- و ‎gine‏ پژمردکی هم کفته‌الد ؛ و بکراول
```


## [2026-09-07T20:41:23.775Z] TOOL CALL #13: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nprint(json.dumps(d['BQT'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['MON'],ensure_ascii=False,indent=1))\n\""
}
```


### [2026-09-07T20:41:25.138Z] TOOL RESULT

```
{
 "title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)",
 "kind": "archive_djvu+local_scan_ocr",
 "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.com/file/8230741184/borhane_ghatee_jelde_4.pdf.html (م–ی, 553 pp), vol 5 https://s3.picofile.com/file/8230741300/borhane_ghatee_jelde_5.pdf.html (تعلیقات, Amir Kabir 5th pr. 1376, 293 pp). Same set behind login on ketabnak.com/book/55304-55307 and /58249.",
 "lookup_hint": "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt"
 ],
 "page_offset": "vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').",
 "covers_etymology": true,
 "notes": "Persian OCR is mediocre: headwords and Mo'in's footnotes (e.g. '۱ - رك: ابر کوه', Pahlavi/Avestan Latin forms) are mostly readable but with many character errors; search with short substrings and tolerate errors. BQT_v1_pages.txt was built from the djvu.xml; BQT_v2_pages.txt from pdftotext -layout of the _text.pdf. Volumes 3–5 (roughly ح/خ–ی and the تعلیقات volume) are not online in full text; for those use Dehkhoda quotations of Borhan/Mo'in via vajehyab/abadis/parsi.wiki, or page images on noorlib (different edition). | Vols 3-5 scans (image only) in incoming/BQT; vols 1-2 have OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt. Offsets verified by eye at several pages (v3 drifts by ~4 pages; page_map gives exact positions once built). || UPDATE: vols 3-5 now downloaded (image-only PDFs, verified as Mo'in's edition from title pages and the Latin footnotes) and OCRed locally. Image-only scan OCRed locally with tesseract 5 (fas.traineddata from github.com/tesseract-ocr/tessdata_fast, stored in incoming/_tessdata). *_pages.txt = 'fas' model (best for Persian); *_pages_faseng.txt = 'fas+eng' model (better for the Latin-script Pahlavi/Avestan etyma, worse for Persian). Pages separated by \\f; leaf N = N-th \\f-block 0-based = PDF page N+1. Search with short substrings and tolerate OCR errors. Provenance caveat: picofile is a general file host, the uploads are not from a library; treat as a grey copy (the book is in copyright in Iran). | vol 4 (م–ی) OCR text, tesseract fas+eng, pages tagged [pdf page N], printed = pdf+1917 | vol 5 (ta'liqat) OCR text, printed = pdf-5 | vol 3 (ش–ل) OCR text (689/721 pages), printed ≈ pdf+1203..1209 | BQT_v2_pages.txt: printed page = leaf + 540 (verified by catch-lines at pp. 838-855, 869, 904); earlier estimate +543 was 3 pages off.",
 "scans": [
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
 ],
 "cites": "page number, continuous across the five volumes of Mo'in's edition (1342/1963 = Amir Kabir 1362 reprint); Mo'in's etymological footnotes are the cited material"
}
{
 "title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)",
 "kind": "website+archive_djvu",
 "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)",
 "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt"
 ],
 "page_offset": null,
 "covers_etymology": true,
 "notes": "covers_etymology = partial: origin-language tag visible online, Latin etyma missing. The a'lam volumes (MON5/MON6 citations, e.g. MON5:528) are NOT online: vajehyab's Mo'in has no proper-name entries (tested افراسیاب — only compounds returned); abadis shows Dehkhoda and 'فرهنگ اسم‌ها' instead, which do give Avestan forms (e.g. Frangrasyan) and can serve as a cross-check. noorlib has no Mo'in 6-vol entry found. The 6-vol edition itself was not found on archive.org, Google Books or HathiTrust full view. || RE-SEARCH 2026-09: still no scan of the 6-vol Amir Kabir edition (incl. vols 5-6 اعلام) on archive.org, Google Books (API quota-limited; WebSearch found no record with preview), HathiTrust (no record surfaced), noorlib, ketabnak (author page persons/6040 lists 34 Mo'in titles, none the 6-vol فرهنگ), tarikhema, picofile, scribd, Commons/Wikisource. Only the 2-vol Adena condensation exists (archive.org, mirrored on ketabnak 65980/65981, picofile, persianpdf, scribd); its image PDFs were downloaded to incoming/MON/ (the _text.pdf variants with OCR layer are at the same archive.org identifiers). The 6-vol set is purchase-only (in print: iketab.com, bookroom.ir/book/97022, 30book.com/Book/32100).",
 "cites": "page number of Mo'in's six-volume Farhang-e Farsi; MON5:… / MON6:… = volume 5 / 6 (proper names)"
}
```


## [2026-09-07T20:41:30.766Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -o \"\\[pdf page [0-9]*\\]\" BQT_v1_pages.txt | head -3\necho \"---\"\nawk 'BEGIN{RS=\"\\f\"} NR==565' BQT_v1_pages.txt | head -40"
}
```


### [2026-09-07T20:41:32.167Z] TOOL RESULT

```
---
گفتار 3
از کاب برهان قاطم درحرف بای فارسی با حروف نبجی
مبتتی بربیست و يك بیان و محئوی بریکیزار و پنجاه و يك
لشت و کنات
تیان اول
در بای فارسی بالف (۱) مشتمل بردومست و سی وشش لغت و کنایت
* هاه روف ات بمریی رل | افزار » دو تختة کوجك باشد بمقدلر لین که
بافند کان و جولاهگان چون بك پای بر آن
افشارند نصفی از رشتهابی که مببافشد یاین رود
و چون پای دیگر بیفثارند صف دیگر.
خوانند ٩‏ - و تاب
وطاقت وقدرت وقوترا
نیز گویند .
با افز اد - بااور لجن - با همزه مفتوح و واو
با فا و زای نفطه دار ساکن و رای قرشت و سکون نون جوم
بروزن تاهموار », کفش 5
مج 3 مفتوح بئون دبگر زده: به‌عنی خلشال باشد وآن
و پاپوش را گونند . ۱ حلقه است از طلا و نقره و مانندآن که زنان‌در
پا افشاد » با شین قرشت بروزن یا | پا یکنند .
(۱) خم۳ : باالف .
۱ - ابرانی باستان ۳۵4 بارتولمه ۸4۲ », اوستا ۳30192 , حندی باستان 0848 ,
بهلوی 880 «یب رکه ۱۱۷ «اونوالا ۷+ه» ء کردی ۳83 , استی 30] «امشق ۲۸۱»؛ در فارسی
پاوبای ۰ کیلکی ۳2 , فریزنی + برندی و نطنزی 02 « ۵.. ٩‏ ص ۲۸۹ *. سمنالی:» سرخ
ولاسکردی۳2 ۰ ۳ ۶ « . ۲ س ۱۸ , اورامانی (02. 3 «2. اورامان 4۱۲۵.
۵ پ - بکر اول (باه فارسی» باه معقوده؛ پی*؛ نام‌حرف سوم از القبای قارسی. راجع‌به
تبدیل پ به ی ر: ص: بح‌از دساچهةٌ مولف. ونیز رك: لفت نامه.
( بر های فاطع ۴۸)
```


## [2026-09-07T20:41:40.369Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in range(560,575):\n    p=t[i].strip().split('\\n')\n    print(i, '|FIRST:', p[0][:60] if p else '', '|LAST:', p[-1][:60] if p else '')\nEOF"
}
```


### [2026-09-07T20:41:41.698Z] TOOL RESULT

```
560 |FIRST: بنم ثانث مر وزث میگفت اه |LAST: معرب آن یمارستان و مارستان «شی». "
561 |FIRST: ۳:۱ |LAST: ی مشاتی و دهان فرار دارد و قو شامه در جوف آنت .
562 |FIRST: نبویرد |LAST: ۴ مخفف ابیون » رك : افیون .
563 |FIRST: ۳۳ |LAST: ۴ رله ؛
564 |FIRST: گفتار 3 |LAST: ( بر های فاطع ۴۸)
565 |FIRST: با آ هو - بالف بسدکشيده و های |LAST: وی
566 |FIRST: باتو ك‌ ثالت بواو رسده: خانه ومنزل |LAST: ٩‏ - را : باژنامه و بای نامه .
567 |FIRST: او |LAST: رك :آي و خرده اوستا ۰.۹۹
568 |FIRST: بممنی سیه (۱) باشد , و آن خربنن چیزیست |LAST: امروز نیز
569 |FIRST: 4و۳ |LAST: رك : پهلوی ورد : مقدمهٌ آقای پورداود برهمین کتاب .
570 |FIRST: ۳9 |LAST: ایران اطلاق میکردد . ركه : قارس. ۱
571 |FIRST:  |LAST: 
572 |FIRST: ۲۶ ۵ |LAST: «(۲۲ 4۵
573 |FIRST: - وس |LAST: حضاننشی نوشته شده‌است. رك : مقدمه کتاب حاضر .
574 |FIRST: داریلب ْ ۱ 4 ۲و |LAST: (برهای فاطع۳۹ )
```


## [2026-09-07T20:41:49.651Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (565,618,619,620,621,622):\n    print('='*20,'leaf',i,'~p.',i-220)\n    print(t[i][:2500])\nEOF"
}
```


### [2026-09-07T20:41:50.936Z] TOOL RESULT

```
==================== leaf 565 ~p. 345
با آ هو - بالف بسدکشيده و های
بواو رسیده » باصطلاح بنایان خانةٌ شش بهلو
باشد وآنرا بعریی عسدس‌خوانند - وخالةٌ مقرنس
کچ‌بربرا یز گوبند. ودرعربی نیز حقرتس‌بمعنی
خانة کج بری‌باشد - و کنابه از دنیا هم هست
پا ح بسکون بای ابجد ؛ خلیقةٌ وین
عسی علیدالسلام را گوبند - و با بای فادسی هم
,یاپ س بابای فارسي بروزن کا6ا» پاپ‌را
کویند که خلیفة دین عبسی عله اللام
باشد ۴ .
پا بر جا - بتح بای ابجد وسکون رای
فرشت و جیم بالف کشیده ؛ بمعنی دایم وهمیشه
و ثابت قدم باشد .
با بر نی -با نون حاکن وجیم عفتوح
بنون دیگی زده» بمعنی‌یا اورنجن استکه‌بعر دی
خلخال گویند .
۱ - قب آحوپا (ه .م) :
زین‌دیو وفا چرا طمع‌داری
رك: یاپ (حاشیه).
شطرنج ازفبیل لات ومات. «لفت نامه».
لاور * بفتح بای فارسی و کون زای
وگل کهنه و رم را نیز گفته‌اند و حربی طبن
خواشد؟ . ۱
پاپسی]وددن » کنابه از رد
دادن و قطح نظر کردن‌ووا گذاشتن - وبازماندن
از طلب بعجز - و منپزم شدن در رزم باشد .
پا بلند کردن - کنایه از دوبدن
باشد . ٩8‏ ۱
بات . بسکون تلی فرشت » اورتگه
و سرهر و تخت را گویند۴ ج
پاثیر اس - بکر فوقانی و سکون
فارسی و رای قرشت بالف کشیده و بسین بی‌نقطة
گوشد .
باتبله است و آن مطلق دبک باشدعموها ودنگ
دهن فراخ حلوا پزی را کوبند خصوصلل" .
۴ - نیزنوعی از زبان وبلختن در
۲ رك : باتبله .
>
ادوخ
وی
==================== leaf 618 ~p. 398
پروش :
روش < بر وزن خموش » جوششی
است که از اعضای‌آدمی بر می‌آید و آنرا بعربی
بثر گویند .
روت بر وزن آرزن . مخفف پروان
است وآن شهری‌باشد تزديك بقزنین ٩‏ - وچرخ
ابرشم را نیز گوبندکه آنرا بپای کردانند .٩‏
پر و ند ۲ بروزن فرزند ؛ نام مزرعه
ایست‌از مضافات قزوین؟ -و بمنی امر دهم آمده
ان که پسر مساده باشد . و ی یممنی امرود
نوشته اند که آن میوه ابست مشهور و هیچ بك
خاهدندار ند افه اعل؟ ۱
فر و ۵ ه بسکون تانی بر وزن‌ارژنده,
بته قماش واسباب را گویندوبعرمی رزمه‌خوانشد.
وبسنی لْفافةٌ ماش و اسباب را کفته الد نی
۱ ره : پروان .
۳
پارچه‌ای که قمای را بدان پیچند - وبسنی‌جوان
مانندی‌را کون دکه «هن آن از بهلوی آن باشد-
واستادان بزاز اسباب د کان خود را در آن هند
و با دبسمالها بندند - وبضم ثانی وسکون ثالث
ورابع جم آمفه است* .
بر وه « بفتح اول وثالث بر وزن‌مروه .
هر چیز که در ناخت وتاراج » وجنگ‌وشییشون
از دشمن بدست آیدا" - و بممنی چادر شب عم
آمده است - و پروین را نیز گویند, وآن چند
سناره است در کوهان ثور۷ .
پروهان > باهای‌هوزبروزن‌خ رکمان,
بمعتی ظاحر وآشکرا باشدش .
پرو یز ٩‏ با بای مجهول بر وزن
شبدیز ۰ بمعتی مظفر و عتصور و سعیدب و عزیز
اشکنان.« لت نامه ».
گل بروند دسته بمته مود
۴ - بده فرسنگه شرقی -
معنی امرود و هم
ت. کل امرود 23 میگوید
* ماهروژ
۹ -آن چگ کوشهة باقوت که ازکان خیزد
۷ - رگ پرو و پرون.
۸ زویشت روز کار قوی کشت و این سخن
ابن لفط ظاحر ۱ پزدهان ( ,
دربیت ذبل :
0 تقو بملء فیپا
ي ۰ «لفت نامد» .
جر روی روز گلر بکوم پروحان .
۷۳ 22
( تراع » متاجره ) « تب رکه ۱۵ * .
==================== leaf 619 ~p. 399
همت و مضاوت وخوش رفتاری و جلوه کردن‌هم
اه اطع
پر و یز قلاك «کنایه از خورشیداست.
رو لزان ه
بروزن گردبدن » آلتی
باشد که‌بدان! ردوشکر
و ادوبة حارة کوفته پرومزن
و امثارآن بیژ ند .
روش - با بای مجپول بر وزن
| دروش ؛ تقصیر وکاهلی درکارها کردن باشد .
رو لین ؟ ‏ بروزن ضمین ۰ چندستارء
کوچك باشد یکجا جمم شده در کوهان تور .
و آنرا بعربی ربا خوانند - و نام مئزلست از
جملهٌ بیست و هشت منزل غمرء و بضی کوند
اين ستاره ها دئبة حمل است‌نه کوهان نور. واول
اسح است .
ره ٩‏ بفتح اول و ثانی مشدد .حلقه
زدن لشکر باشد از سوار و پیاده بجهت شکار
وفیره - وخطی را نیز کویند که از سوار و پیاده
کشیده شود وآنرا بمربی صف خوانند؟" سودامن
وطرف و کنار؛ هرچیز را بیز گوند حمچو پرة
بیابان و پر بینی و پر کوه - و جزوی از ففل
که بدان محکم شود - وب رگکاه راهم کقده‌اند.
ر گرامی باشد - ویزبان پهلوی ماهی را گوشد.
و لقب پسر انوشیروان‌هم هست او چون‌اوماهی
خسرو دوم(یرویز) درشکار ( جلم نقره )
( زاره : صنایع امران ماستان)
بمپار دوست میداشت بدین سیب او دا پرویز
میگفنند. و مضمه پرویزن است؟ .وآن آلتی
باشد که بدان آرد + شکر و امتال آن بز ند »
و بستی کویند آلتی است مخصوص شکر بیختن
سو بیختن را نیز گوبند- وپروین را هم گفته‌اند
وآن سناره‌ای چنداست‌در کوحان ور - وبمعنی
۱ . نام نواده انوشیروان بر هرمزد چهارم ( ۵4۰ - ٩۷۷‏ مُ 3
۴ راك : پرویزن ۰ ۴ رگ : پروین . ناوت
0201۳5 صیغ جمم آمده (نیربشت بند۱۷). برخی‌از خاور شناسان آنرا به‌پروین ترجمه
کرده‌اند (رك : بعتها اس ۳4۵ ؛ ۲ ص ۳۵۵)» افنانی ۳6۲۵196 . بلوچی 020۷2۲ « اسشق
۳۰۸ » درسفدی : بروی» خوارزمی: بروی» عربی: ثرباء فرانمه ۳۱6۱206 ونیز مثزل اول از
منازل قمرترد ابرانیان « گاه شماری می۲۰4 (بنقل‌از بندهش بوستی) و ص ۳۳۵ *.
 *‏ پهلوی۳۵۸۲۳2 (حاشیه - لبه ‏ کناره) «ناوادیا ۱۹۶ نیز بمعنی بال‌ویر « اونوالا
۰4 3 َ #
۷ آنکه آرندکته (انگور) رابکواره مت باارغان مینک لح
نه بتصاصتی کنند خلق اشاره نه‌یدیت یادشه مخواهد ازومال:
«منوچهری داعغانی ۱۳۶*.
==================== leaf 620 ~p. 400
پرهازه .
و پر؛ آسیا (۱) و دولاب و امثال آن باشد -
وبسمنی‌پهلو نیز بنظر آمدم‌است که‌بعربی جنب
خوانند .
پر هازه - بر وزن دروازه . چوب
پومیده و رکوی سوخنه باشد که بربالای‌سنکه
چشاق گذاشته چشماق (۲) بدان زنند نا آتشل
درآن افتد .
پرهام - بر وزن فرجام » نامی است
پارسی باستانی و معرب آن براهیم است٩‏ .
پر هتن - بفتح الك و سکون خای
غطه دار بر وزن برجستن » بمعنی ادب کردن
عاشف 6 فبکن تالث هم‌آمده است؟ ۲
سهوده را گوبند - و جامه ای که از تاش
۱ - ركگ : ایرهام .
و حرارت آتش رنگه کردانیده شوختن ترديك
رسمه باشد ۰
. فر هون - بروزن مجنون. دایرم وهر
چیز میان‌خالی را گوبشد مانندچنبر وطوقوحالة
ماه و امتاز آن۴ ۰
ثر هیلقن - بر وزن‌انگیختن» بمعنی
ادب کردن باشد.
پر هیز * ه بر وزن پرویز » آست
که بعریی حذر و احتراز میکویند؟ - و ترد
محققیناجتناب از ماسویاه تمودن باشدوبمعنی
تری و بیم و نگاهداشت‌خود ازمضرت. و بمعنی
تفاوت هم بنظر آمده ات
ری ۲ بننع اول وکر ثانی وسکون
نحتانی , همروف است که قیض دیو باشد -
جهل کشبده بگردجان تو پرهون.
تاصرخسرو بلخی. «لفت نامه».
۱ - چهل روز با لشکر اویز بود
۵ پپلوی 0۸۲۳۵6
کهی رزم ر که روی برهیز بود .
فردوسی‌طوسی. «لفت‌نامه».
باهمال خود انسائرا می‌فر سمف. دراومتا بری جنس موّث «حادو» مصوب شده که ازطرف اهریمن
گماشته شده تاییروان مزدیسنا رااز داه راست مثحرف سازد. همجن پربان درزمرة میاه اهردمن
خدزمین وآب وگیاه وستوران و آنش درکارند . همانها بشکل ستار کان دباله دار بانشثر فرعتة.
باران در ستیزماند ناوی راز بارس گی بازدارند وزمین رااز خشکی وبران سازه. ( از بادداتهای
استاد پورداود ورك: بشنها ۱ص ۳۰-۲۹) . درپهلوی ۳2116 ارمنی ۳2۲3» اففانی [۳8۲«اسشق
۳۰( «بی رکه ۱ , خوانساری ۳6۲6 ۶ سالنامةٌ فررهنکه کلپابگان ۷» گیلکی 03 در
ادییات پارسی بنوعی‌از زنان ج نکه نبایت خوبرو باشند» اطلاق‌شده «غیاث‌اللغات» :
پری هفته رخ ودیو در کرشمة حسن بسوخت دیده ژ حیرت که امن چه بو لسجی است.
«حافظ شیر ازی ص 66۵.
==================== leaf 621 ~p. 401
ومشفف پربر هم هست که پربروز باشد که روز
پیش‌دیروز است؟ سومضارع مخاطی‌پربدن باشد
وبشم اول بمعنی پر ومملو بودن .
پری‌افسای افونگی باشد یمنی
صاحب تسخیر و شخصی که از برای تسخیر جن
افسون خواند .
فر 43۳۵ - بروزن ددیجه , لیف خرعا را
کون وازآن رسمان تابند .
ممدوله بروزن برشان » انونگر و شخ یکه
تخیر جن کرده باشد .
بر بدا بفتح اول بروزن خریدار »
کسی را گویند که جن‌داشته باشد ودختر یکه
اف ون گران چیزها بخوانند و بدو بدمند نا او
برقص دراید . و از ماضی و متقبل چیز ها
بگوید - ودیوانه و مجنون‌را هم کفته‌اند- و جا
ومقام دیورا لیز گوبند .
بر یف حت » بروزن همیگفت: نام دختر
۰سام نریمان عاشق او شد
وزال ازو بهم رسید. ۵
بر ثر 9
دیروز باشد که روز حال روز سیم است .
لِز ه بانحتانی مجهول بر وزن عویز .
فرباد و فتان را کویند ۴ و سیزه که در کنار
جوی و رودخانه و تالاب و جایی‌که آب بیار
باشد برویف و پرویزن را نیز گفته‌اند که ۳۳
پر یز ن «بروزن کشیدن» مخفف پرویزن
ات 15 آردیز باشد ۲ ۴
پر سای باسین بی‌نقطه. مخذف پری
افنا: ات که پر مقوان و وگن و دتقی .مه
بر سود ه با سین بی نقطه بر وزن
پربروزه نام دبری ومعدی بوده در زمان خسرو
چرویز » وبعضی گویند نام مقامیست که شیرین از
دشت آبخوك با نجا رفت.
پر وی بانحتالی‌مجپول بروزن کشیش»
پرشان ۴ - وپرشانکننده را کوبند ۵ - وامر
بدین معنی هم هست معتی پربشان کن و از
هم بپاشی- و پربشان کردن واز هم جدا نمودن‌را
نیز کفته اند - ویمعنی پربشانی و آشفنگی حم
اهلد ات #2
۴ - ازپریزت چنان بلرزدکوه
۷
مانند : خالك برش :
باد برسده نوهم نرسد
که زمين بومپن بلرزاند . علی فرقدی.
« لفت نامه *.
5 - در کلمات من کت
طیران کردن:
آن زاغ را نگه کن چون پرد
شه درصفحً ۳۹۸
==================== leaf 622 ~p. 402
ح‌ِ ۰ 4 بت .
سازد ٩‏ ,
فر لصو ع اب وزن کئبدن مشتف
برمشان باشد ۴ - و بمعی افشاندن و برشان
کردن هم‌آمده است .
۱ پر یشیك ه مانی پربشیدن است یعنی
پرشان کرد و براکنده ساخت ٩‏ .
بر شین « بر وزن پری دسن .
سمنی بدحاوپریشان کردایدن و بیخود گشتن
بائد ؟ .
پریشیده ۴
ممعنی بر شان شده و برباد داده و عتفرق ساخته
بر وزن پری دنله ۰
باشد .
فری گر فت - کسی راگونن که جن
باو ار شده باشد و او از مفیبات خبر دهد و از
ماضی و مستقبل گوید » و دزد برده بیدا کند»
و هر چیز که در خاطر " بگنرانی و ازو بیرسی
بگوبد. واکی خوابی دیده باشی وآنرا فراموش
کرده باشی ازو بپرسی جواب کوبد و تعبیر
نمابد. وازاحوال غایب لیزخبردهد» وبعربی آورا
کاهن خواشد .
فر لون» بر وزن آفیون » علتی باشد
باخارشی که آن را کسر گویند. و بعریی جرب
خواند ۵ .
ز اخقی ه بفتح اول بر وزن نباختن ,
بععنی گداختن باشد» و بکسر اول هم آعده
است ۰
۱ پز اوه بر وزن کساوه . داشی
و کوره‌ای را کوب که در آن ظروف سفالن
۱ رك: ‏ یشیدن . ۴ - رل : فرنفان.
زچندین ال وچندین زر که برپاشی وپرشی
۴ - اسم مفعول از پریشیدن (ه .م.)
شقل لغت ناهد؟.
وخشت وگچ وآهاث بز ند.
پز ی فقن ۱ « بابای فارسی ونون وتای
فرشت بروزن پهلو شکن, بز بان ژند و بازند(۱)
بممنی دادن باشدکه در مقابل گرفتن است .
و پزپونمی یعنی میدهم ويزپونید یعلی بدهید.
عجب باشد که‌باشد درجهان‌تنگی ودروشی!
فرخی میستانی. «لفتِ نامه».
شه ازسفحهٌ ۳۹۷
«لفت نامه * .
```


## [2026-09-07T20:42:06.650Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(t):\n    if 'پژ' in p and 600<i<700:\n        print(i, i-220, p.count('پژ'))\nEOF"
}
```


### [2026-09-07T20:42:07.892Z] TOOL RESULT

```
623 403 2
624 404 6
625 405 7
626 406 7
```


## [2026-09-07T20:42:13.818Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (623,624,625,626):\n    print('='*20,'leaf',i)\n    print(t[i][:3000])\nEOF"
}
```


### [2026-09-07T20:42:15.096Z] TOOL RESULT

```
==================== leaf 623
۵ بفتح اول وسکون‌ثانی ودالابجد,
بمعنی خون باشد که بعرچی دم گویند , و بعضی
بمملی جان کفته‌اند که بعربی روح خوانند .
پز ۱2۵ بفتح اود و دال ابجد بروزن
نفزكك » کرمکی باشد که کندمرا خورد و خراب
سرشك ؛ طب و جراح را گوبند ۴ - و بفتح
اول و ثانی بممنی جغد باخد, و آن پرنده ایست
حمروف و حنسوی . #۶
۱ فز عیّك » نم اولوغین قطمدار وسکون
ثانی ونون ودال بی‌نقطه. بممنی بزغنج است‌وان
پته مانندی باشد بی مفز که بدان پوست را
دبای کنند 3
وی - ختح اور و سکون ثانی و واو
بتحثانی کشیده ۰ فرومابه تربن مردمان را گومند
و بعربی ارذل خوانند ۰ بفنح اول و شانی «م
آمده است . #
لِر - بفتح اول وسکون ثانی» زمین پست
و بلند و کوه و کتل را گویند» و ؛عربی عضه
خوانند ۴ - وبسسنی کهنه و مندری هم هست -
و کل کهثه و نرم را نیز گویند - و بمعنی چرل
وریم هم آمده است ۴ - و جنم اور برف ریزها
که از شدت هوای سرد مانند ز,ك از آسمان
بریزد - و چوبی باشد زهد که بدان مداوا کنند
و آن‌را بعربی وج خوانند .
| گن» باعاف فارسی بروزن مساکن .
زشت ویلید وچ رکن را کوند ۵
او ند ‌ بروزن دهاو ند ۰ چودی باشد
کهدریس درانداز ند نادر کشوده نگروو؟ وجوب
کازران را نیز گویند ۰
له نم هردو بای فارسی و سکون
۷۲۰۰ «مشت‌ها ۲۷ صس4۳۵۷.
پارسی لیز: مجشلك» بژشك .
۳ ‌- رژد: پژاگن.
لطیف و جوانم چو کل در بهار
اکر سراسرکوه وپژ آبدش هزپیش.
خسروانی «لفت فرس ۱۷۸
در خانه فروبند بقلج و یژاوند .
رود کی سمرفندی. «لت نامد».
بغیه درصفحٌ 4۰۰
==================== leaf 624
ی کاله: ۱ 2 ۱ سب هه سس
هردو زای عجمی, کلمهای باشد که شبانان بز را
بدان نوازتی کنند وبوی خود خوانند و آن را
پزیژی هم کوبند ٩‏ .
بز کاله بفثح اول بروزن ی رکاله ؛
بععنی حصه وبهرء ولخت وپاره باشداز هرچیز -
وپاره و وسلهرا تیز گوبند که برجامه دوزند ودر
عربی رقعه خوانتد ؟ .
فر ۵ - بفتح اول و سکون ثانی و هیم .
ببعنی کوه باشد که بعربی جبل خوانند. وبکسر
اول حم آخفة 0
۳ مان ۴ « بکسراول بروزن کرمان»
بممنی افسرده و بی رونق و غمن‌الث و مخمور
واندوهگن باشد ۵ , وباینمعئی بفتح اول وضم
اول هردو آمده است - ویضم اول بمعنی‌خواهض
واوژه هم کفثداند ۰
لژ ما4 متح اود بر وزن عمسایه .
کاوی که فربدون راشیر میداد وبکسر اول هم
آنفد است ۹ 4
بر هر ده مکش اول وضم میم بروزن
دل برده » بمعنی بژمان و افرده و غمنالك
3 اندوهگین و بی رونق باشد - و بمعنی روی
بخشکی آورده و نرنجیده ودرهم کشیده شده هم
فست ۷
بر مر بده ۲ بکسراول و رای فرشت
بتحتالی رسیده و فتح دال , بمعنی برزمرده باشد
کهغمناك واندوهگین وافرده گردیده و بی‌رواق
شده است 5
فزن - بر وزن و معنی زغن است که
غلیواج باشد.
۱ - شود دل بحرف فرآن به نشود بز به جزیژی فربه. سنابی غزنوی. «لفت نامه» .
۳۳ بر کاله, وظاهراً همین صورت صحیح است. «لخغت نامه». ‏ و
۴ - پارسی باستان_ 00202 ۵ + تافقا2 ؛ پپلوی 25۳15020 ( بازند 0ناعدم) ,
هندی باستانی ۳20 ۲+ 0224 (مخالت کردن » اعتراض کردن ) «اسشق ۳۱۷». رك: بشیمان.
ه‌ بت آندرین خانه بوده‌ام عپمان کرده ام شاد اژو دل بزعان ِ
عتصری بلخی. «لفت ناهه؟.
۱ - مصحف‌پرمابه؛ رك : پرمابه و پرمابون . ۲ - اسم مفعول از پژمردن, رك : پژمردن .
پزمرالدن و پزمرالیدی - بکسس اول و ضم سوم و فتح هشتم , متمدی پژمردن ‏
پژُمرده کردن ۰ اذبال :
همی پژمرانه رخ ارغوان کند نیره دبدار روشن روان .
فردوسی طوسی. «لغت نامد» , رك: بزمردن.
* پزمر دن و پزمریدن - بکسر اول و ضم سوم و فتح پنجم » پارسی باستان أکقا08 ( اوستا
0 )+--8031. پز ظاهرا اشتبا‌فدمی ا-ت بجای‌یژ 0120 . ویزدر پژوهیدن ویژمان هم
دیده میشود «اسشق ۰۳۱۳ درهندی باستان ۵۵۷۱ ( سفت #دن » سحی شدن) » ارمنی
۲ - 2 با 10[۲ - 2 5 ۲۱۴1۲0 -2 (یحی شدن) «یب رکه ۲۳۸ :۰ ۷۵۲۵8۵۶).  .‏
بقبه اسف ۳۵٩‏
کنندچنانك نن‌مردم مر پزشکی‌را وچنانك اندازه مرهندسد را...» «دانشنامه ی۵۷*.
۵ پزیدن - بفتح اول وچهارم. پختن («.م) - پخته‌شدن:
هرمیوم که ذرباغ جبان‌بد همه پخته‌است ای غورة چون سنگه تخواهی‌توزبدن.
مولوی بلخی رومی . ذلفت نامه * .
(برهان قاطع‌هه)
==================== leaf 625
ات
برخست باشد ۰ و آن کیاهی است خود روی
و خوشبوی مانند اسفناج که داخل آش کنند
چون در کوه و کنبذ باواز بلند چیزی بگویند
در جوا ب‌همانرا نو ند » وآن‌را بمرمی‌صد اخو انند.
یر ول - بروزن‌قبول, کمب پا واسشخوان
۱ شتالنگه را کوش وستان زنان راهم گفتهاند-
و گلوله‌ا ی که طفلان بدان بازی کنند - وبمعنی
فندق هم هست و آن را هفزی باشد که بخورند
پژولش ۲ ۰ بکر اول بر وزن
نکوهش , بمعنی پژهرده و پربشان و درهم
شده باشد .
پژ و لیف ۴ - بر وزن نکوهید » یعنی
عزمرده شد وآب وئاب در وی نماند .
بر و لیدن بکراول‌بروزن‌نکوهیدن:
پرمرده شدن- و پژمرده کردن- ودرهم آمیختن
ویرثان کردیدن بود ۵ - و بمعنی تداخل هم
آمده‌است که درهم‌شدن‌باشد. وباین‌معنی بفتح‌اول
هم گفته‌اند وصیحت کردن - وجم‌تجو وبازیری
(۱) خم۳ : گزند .
و تفحص نمودن را نیز گویند .
لیدم ۴
و له " - بر وزن تکوهیده »
یز مرده شده ونرم گردیده شدت و بی‌اب و تاب
شدم و ابترشده- وصیحت کرده شدموبازیری
کرده شده باشد .
بزوم هتح اول بر وزث سموم ه
فقبر و دروش و کدا و خوار و ی اعشبار را
ند
پژو مان - بايم بر رزن خموشان ؛
جمعم پژوم ات نی فقیران و درویشان
و کدابان! .
فر و لاس ح بروزن دربند » چوبی باشد
که درپس در گذارند تادر کشوده نگردد- وچوب
کازران را نیز گویند ۷ - و کنابه از مردم
پس درنشین ودیوت باشد, و باین معنی بفتح اود
وئالی همآمده است ِ
بزوه ۸ بکسر اول وضم‌ثانی وسکون
هاء بممتی تفحص_ و تجسی و بازجمتن - و باز
خواست باشد- و جوندم و طالب و خواعنده را
نیز گوبند ٩‏ - و اهر باین معنی هم‌هست معنی
لفحص وتجسی بکن وبطلب وبخوام ويتتَهة بلند
وآمتر قبا ومانند آندا لیز کویند *۱.
یزرو شم 1 بروژن نکوهش,: تفحص
ص؟ ۲۷۷ اف نامد» .
۴ - انم مصتر از : پژولیدن .
٩‏ وه : برّمان () .
۵ رك : مدولیدن .
بزوه. «لفت نامه».
وفتح واو باشد. «لفت ناعه».
گرددان من بدولاند زود
صد ور محنت برایشان بر گشود .
مولوی بلخی‌رومی. «لفت‌نامه*.
==================== leaf 626
وتجسی وجستجوی را کوبندب وبمعنی مصدر نیز
آمده است که جستجوکی زن باشد.
۰ 4 9 فروشند کی
پژوهنده ۴ بر وژن فروشنده »
بمعنی بازیرس کننده و قحص نماننده باشد
وحکیم و عاقل و خردمند و زبرك را لیز
گویند .
پژوهیك ۴ ه_ بر وزن نکوهید »
ماضی پژوهیدن است یعنی تفحص و تجسس کرد
وجسجو نمود .
پر و هیكان؟ » بروزن‌دکوهیدن,به‌منی
تفحص وتجسی کردن و بازخت وجستجونمودن ۵
وخواستن ن باشد.
پژوهیده ۷ » بروزن نکوهیده ۷:
خردمند وعافل وزبرك ودانا را کویند۸ .
بر وی » بفتح اول وئانی وثالث سحتانی
کشیده» مردم فرومابه و اراذل را گویند. و بضم
اولرنان‌هم باین معنی آمده است ٩‏
ت- رك: بزوهدن .
<< چنین کات فر سنده را راهجوی
بازجسته: کاویده است :
سخن شد پژوهیده از هر دری
اه مت
رف لین بروزن.قزوین * بنعنی _ کثیف
وچ رکن باشد*٩-‏ و کثیف‌شدن وچر کن‌داشتن‌را
له ه بفنتح اول و انی و اخفای هاء
زمین پشته پشته باشد - وکتل و کربوه را نیز
کویندکه بمربی عقبه خوانند - وآستر جامه را
ئیز گفته‌اند وبکسر اول و ضم ثانی واظهار ها
مخفف بژوه است ت ۷۱ که بمعنی شحص و تجسی
وبازخواست باشد.
. بر هان بنم او بر ون سلطان »
بمعنی آرذو و خواهش دل و غبطه باشد ٩۴‏ .
وّطه صفتی است در آدمی که چون چیز خوب
پیش کسی بیندخواهد که آنچیز با مثلآن چیز
او حم داشته باشد می آنکه صاحب آنسیز
تقصانی برسد ومحروم شود وآدمی را اين صفت
محبود است » برخلاف حسد که بر عکس این
بود چهحسود خواهد که آن‌چیز رااو داشته باشد
وبغیر ازو کسی نداشته باشد و صاحب آن چیز
محروم بماند .
؟ ‏ اسم فاعلاز پژوهیدن (ه .م).
.
_ بیژوه نا دارد این ماه شوی؟
فردوسی طوسی. «لفت نامه» .
۲ - معنی نضت آن پژوهش کرده ؛
ز شاهی و تاج و ز هی کشوری .
فردوسی‌طوسی. «لفت نامد».
بروهیده سودابه را شاه گفت
که اين رازت از من نب‌اید نپفت .
ی هیشم آرد دوات بن سوراخ
‌ -- ر4: بروه ۰
امست. رك:بروهان. «لیت‌نامه؟ .
```


## [2026-09-07T20:42:40.817Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(\"### leaf 625 full\")\nprint(t[625][3000:])\nprint(\"### search پاپژ / پا پژ\")\nfor i,p in enumerate(t):\n    if 'پاپژ' in p or 'پا پژ' in p:\n        print('HIT leaf',i)\nEOF"
}
```


### [2026-09-07T20:42:42.180Z] TOOL RESULT

```
### leaf 625 full

### search پاپژ / پا پژ
```


## [2026-09-07T20:42:49.607Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in range(560,580):\n    if 'پژ' in t[i] or 'اپژ' in t[i]:\n        print('HIT',i, [l for l in t[i].split('\\n') if 'پژ' in l][:5])\nprint('--- leaf 569 head')\nprint(t[569][:1800])\nEOF"
}
```


### [2026-09-07T20:42:50.870Z] TOOL RESULT

```
--- leaf 569 head
4و۳
بادم۱ بروزن ساده ,که خرو کاورا
کوبند - و چراگاه اسبان و شتران و کاوان را
بز کته اند - و پمعنی چوب دستی نیز آمده
ٍِ.
باده‌بان ۴ بروزن صابه‌بان کله‌بان
وچوپان وپاسبان ونگاهبانرا گویند.
پادیاب - بایای حطی بروزن ماعتاب,
پیمنی شدتن وپاکیزه ساختن چیز ها باشد
با دعا خواندن ۴ .
پا۵یاو» بروزن آب‌ساو. بععای پادیاب
است که شتن و باکیزه ساختن چیزها بادعا
خواندن باشد بلغت زند وبازند (۱) 6 .
پادبر بر وزن جاگیر , چوبی باشد
تانیفتده و باذال نقطه دار هم کنته‌اند و اين اسح
است بنا بر فاعد کلیه که هرگاه ما قبل دال
حرف علت باشد وآن حرف علت ساکن باشد
است
(۱) چك ء ژند و پلزند  .‏
اسنت ۸ .
اف بر وزن خار ۰ بمعنی سال گذشته
و پیش ازین باشد ۷ - و «خفف پاره هم هسنت -
و چرم دبافت کرده دا نیز کویند - و بمعنی
پرواز و پرش هم‌آمده است؛ چه پاریدن بمعای
بر بدن باشد 3
پار او - بارای بالف کشیده وبواو زده .
زت بر و مرژال را گونند - و نام بلو کیت از
پار د۸- بضم دال وسکون‌هيم» رانگی‌را
چاروا دوزند وبریس ران چارو! اندازند » وی
کوبند چرمی باشد که بریس زین اسب بندند
وبرزیر دم‌اسب اندازند. واين اسح است .
پار س - بسکون الث بروزن و حعنی
۳ هس یابه ۹ ۳ ۰
۴ رك : یادیاو .
۶ با 2202۷ . وآن مثل وضوست تزد مسلمانان. زرتفتب ی که میخواهد پادباب کند نضت
بك «خشنوتره اهورهه مزداو» (بخشنودی اهور مزدا) م‌خواند ویس از آن یکبار « اشم وهو...»
میسراید . آنگاه روی.ودستها وپاهای خودرا میشومد» از آن پسکشتی نو مبکند و بترئیب عقرد
کمربند خود می کتاید ودعای مخصوصآرا میخواند وباردیگر پدورکمر می‌بندد. «خرده اوسنا
۹ مح ۱*. ۱ رك : لت‌نامه ویازیر. .  .‏ ۷ 2 در: پارسال» پارینء قس مانسکربت
۸ ( در سال گذشته ) ؛ ارمتی 0۵ ( سال گذشته ) , کردی ۵ . افنانی ۳۵۲۵5 ,
استی 18۲8 ۰ 18808 ( در مال پیش ) » وخی ۳8۳0 ۰ سریکلی 2۳۷۷15 ( قس بونانی
61 ) بارسی باستان2 ۳8۲۷۷ (سابقا), اوستا 8211۲۷2 « اسشق ۲۷۰ *. ۸ - در
پارسی باستان (کتیبه‌های هضامنشی) 2752 : ام مکی از اقوام ابرانی مقیم جذوب ایران که نام
بقبه درصفحةً ۳۰
۵ پارت - پارسی‌باستان ۳۵۲4118۷2 مقر قوم پارت (
```


## [2026-09-07T20:42:59.274Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (566,567):\n    print('='*15,i)\n    print(t[i])\nEOF"
}
```


### [2026-09-07T20:43:00.614Z] TOOL RESULT

```
=============== 566
باتو ك‌ ثالت بواو رسده: خانه ومنزل
و عفرب باشدا - و ظرفی را نیز کوبند که از
گنل سازند و گندم و جو درآ ن‌کنند .
پاقیله « بکر فوفانی وسکون‌حتالی
و فتح لام ۰ مطلق دمکهرا کونند عموماً ودنک
دهن فراخ حلوا پزی را خسوصاً .
بانیمار ع_ با میم بروزن‌شالیکار» بمعنی
تعجیل و شتاب باشد ویزبان زند و پازند(۱) نیز
همن معنی دارد؟ :
پاقینی - با فوقنی بتحتانی رسیده ولون
بدان بفشانشد و باك سازند .
پاچال ع با جیم فارسی بر وزن پامال»
کوی باشد که جولاهگان در وفت بافندگی
پاهای خودرا درآن آویز ند ۳ استادان بقال و قانبا
و ات درآن اسناده چیزی فروشند ۴ ۲
پاجاهه - با جیم بالف کنیده و تج
میم , شلوار و تتباتراگوند؟ .
پاشان باشد - و بمعنی پاشیدن هم هست6
است وآن کوی باشد که استادان جولاعه بای در
(۱) چك: ژند ویاژند.
طسی «لفت نامه».
0 ح
س بفلح تحتانییلیدی و لجاست:
هر دوراه را گوشن که بول و عابط باشد۷ .
پاچك » بر وزن اوك . سرکین
کاو را گوبند که شفك شده باشد » با
بدست پهن کرده بجهت سوختن خشكك کرده
باشمف .
باحجله » بررزن قافله.
چیزی‌باشدماتند فربال کوچکی
۲هجهت کوفتن‌برف بریای‌بندند . #۵(
تا مردم قافله و لشکر وغیره‌از
بالای آن بفرات بگنرند۸ . باچله ۰
پاچ نامه - بر وزن شاهنامه, لقبرا
گوبند و بمعتی همال و فرین هم آمده
یت ۵ .
باچنگ - بر ون آهنکه : دربحة
کوچکی را گوند در خانه و کوشك و غبره
از پنجرء و امنال آن که بيك چشم از آن نگاه
توان کرد*٩-‏ وکفش وبا وافزار را نز گفته‌اید»
و با باتک و پاهنگسترادف است
9 ۰ ی هه
پاچیدن - بر وزن: وممنی پافدناشه
که باشانیدن است۵ - ونرم وآهته برامرفتو را
ب ی آب شود خنجر بهرام ات . خن
رك: بونکره همان صفحه .
- ۷181185 انگلیسی ( جامة کشاد که
۶ مال فراز آری و بکار نداری
۱-- پا چه ( نان ضنبی ).
۳
۸ - ظیراسکی
٩‏ - را : باژنامه و بای نامه .
=============== 567
او
نیز گویند . ۱
پاچیله » بر وزن پانیله . کنش و پا
افزار باشد .
پاخره ‏ بفتح خای نقطه دار و رای
بی نفطه : صفه و نشیدتی را گویند که در پیش
در خانه باژند» ویکسرخای نفطه‌دار نیز گفته‌اند
و بسکون آن هم آحده است .
پاخیره - بر وزن کاجیره , بنای دیوار
و خانه و امثا آن باشد و آنرا بعربی رهص
خواند . ۱
پاخیره دن ‏ بنتح زای هوزوسکون
تون, بنا و گل کار و دبوار کر را گوبند. وسربی
رحاص خوانند .
پاث ۱ بر وزن شاد.بمعنی‌ای ویاسبان
و نگهبان و پاییدن باشد که از دوام و بات ودد
تظر داشتن است - و مامان و دارندگی دا لیز
وید - و بمعنی بز رک و عمده هم هست »
و پادشاه مر کب ازین است- و تخت واورنگث را
نز کفه‌انده چون در اصل این لفت بات بوده
و تابدال بدل شد بسب قاعدم کلی یابسبب تفییر
السنه وازمان.
باداد بر وزن دادار سعنی بلفی
از ماههای ملکی- و اسب جلد ونند وتیز را نیز
کویند - امر برپای داشتن هم‌هست . *
‌
و بسنی کوبند پاداش بمعنی مکافات است مطلفا
خواه جزا و معافات لیکی باشد و خراه بدی۷ ۰
هاد‌اشت؟ - بسکون تلی فرشت ۰
بمعنی ۳ ست که جزا و مکافاث یکی
باشد . ۱
باداشی * ‌ شتح شین نقطه‌داروسکون
نون» بمعتی پاداشت باشد که جزای نیکی است
چ هکفتاند ,
یت ؛
بگانه‌ای که دودستش کهعطا بدهد
حزار فابده با صد هزار پاداشن ۷ .
پادام ‏ بر وزن آرام , حلقةٌ موی را
کویند. وآن دامیست که ازدم اسب ساند و در
راه جانوران برنده گذارند - و پرنده‌ای‌دا نیز
کفته‌اند که ترديك بدام بندند تا جانوران دیگر
بهوای اوآیند ودردام افتند, واو را بعربی ملواح
خوانند .
پادرر کایه بننتی_موار و مواری :
سفر باشد و کنابه از مهیا بودن و مستمد شدن .
اسباب سفر است - ودم تزع را نیز کفته‌اند که
ابتدای سفر آخرت است- و هرچیز یکه تزديك
بضایم‌شدن باشد عموماً و شراب ی که مادل بشرشی
شده باشد خصوصا . 4
پادسکه -بنتح اك بر وزن پات »
شغنی 8202 (شبان) «اسشق۲1۵».
۴ - بهلوی 02۳15۳0 224
۴ - نگر نيك‌وبد تاچه کردی ز پیش
رد پاداشن ۳
۹ ی ره ": پادای
رك :آي و خرده اوستا ۰.۹۹
```


## [2026-09-07T20:43:35.751Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK: find ped- entry page 790 ===\"\ngrep -n \"pedqm\\|ped-, pedi\\|pēd-, pōd-\\|ped-, pod-\" POK_full.txt | head -20"
}
```


### [2026-09-07T20:43:35.801Z] TOOL RESULT

```
=== POK: find ped- entry page 790 ===
```


## [2026-09-07T20:43:36.983Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD watkins ped ===\"\ngrep -n -A25 \"^ped-\\|^ped\\. To go\" AHD_watkins1985.txt | head -60"
}
```


### [2026-09-07T20:43:37.033Z] TOOL RESULT

```
=== AHD watkins ped ===
819:ped-2. Container. 1. Suffixed o-grade form *pod-om in Germanic “fatam in Old English fzt, cask: vat. 2. Suf- fixed o-grade form *pod-ilo- in Germanic *fatilaz in Old English fetel, girdle: FETTLE. 3. Probably full-grade form *ped- in Germanic *fet- in Middle High German vetze, “clothes,” rags, probably akin to the source of obsolete English fritter, fragment: FRITTER}. [Pok. 1. péd- 790.]
820-peg-. Breast. 1. Suffixed variant form *pek-tos- in Latin pectus, breast: PECTORAL; EXPECTORATE, PARAPET. 2. Possibly suffixed variant form *pek-so- in Sanskrit
821-paksah, wing: PUNKA. [Pok. (peg-), pdg- 792.]
822-p@(i)-. Also pé-, pi-. To hurt. Possible root; contracted from *pea(i)-. 1. Suffixed (participial) form *pi-ont- (< *pia-ont-) in Germanic *fiand-, hating, hostile, in Old English féond, fiond, enemy, devil: FIEND. 2. Possibly *pé- in suffixed zero-grade form *po-to- in Latin pati, to suffer: PASSIBLE, PASSION, PASSIVE, PATIENT; COMPAS- SION. [Pok. pé(i)- 792.]
823-peie-. Also pei-. To be fat, swell. 1. Extended o-grade form *poid- in Germanic *faitaz, plump, fat, in derivative Germanic verb *faitjan, to fatten, whence Germanic past participle *faitidaz, fattened, in Old English f#t/t), fat: FAT. 2. Possibly suffixed zero-grade form *pi-tu- in Latin pituita, moisture exuded from trees, gum, phlegm: PIP 5, PITUITARY, PITUITOUS. 3. Possibly suffixed zero-grade form “pi-nu- in Latin pinus, pine tree (yielding a resin): PINE!, PINEAL, PINON, PINNACE; PINA CLOTH. 4. Suffixed zero-grade form *pi-won- in Greek pidn, fat: PROPIONIC ACID. 5. Suffixed zero-grade form *pi-wer-, “fat, fertile,” in: a. *Iwer-ii, the prehistoric Celtic name for Ireland, in Old English Jras, the Irish: (ERSE), IRISH; b. * Piwer-id in Greek Pieria, a region of Macedonia: PIERIAN SPRING. [Pok. pei()- 793.]
824-peig-'. Also peik-. To cut, mark (by incision). 1. Alter- nate form *peik- in Germanic *fihala, cutting tool, in Old English fil, file: FILE. 2. Nasalized zero-grade form *pi-n-g- in Latin pingere, to embroider, tattoo, paint, picture: PAINT, PICTOR, PICTURE, PICTURESQUE, PIG- MENT, PIMENTO, PINTO; DEPICT, PICTOGRAPH. 3. Suffixed zero-grade form *pik-ro- in Greek pikros, sharp, bitter: PICRO-. 4. O-grade form *poik- in Greek poikilos, spotted, pied, various: POIKILOTHERM. [Pok. 1. peig- 794.]
825-peig-?. Also peik-. Evil-minded, hostile. 1. Suffixed zero-grade form *pig-olo- in Germanic *fikala- in Old
826-English ficol, treacherous, false: FICKLE. 2. Suffixed o-grade form *poik-os in Germanic *gafaihaz (*ga-, collective prefix; see kom), in Old English gefah, enemy: FOE. 3. Suffixed o-grade form *poik-yos in Germanic *faigjaz in Old English fege, fated to die: FEY. 4. Suf-
827-peis-'
828-fixed o-grade form *pozk-itd in Germanic *faihithé in Old French faida, hostility, feud: FEUD!. [Pok. 2. peig-795.] peis-'. To crush. 1. Suffixed zero-grade form *pis-to- in Latin pistillum, pestle: PESTLE, PISTIL. 2. Nasalized zero-grade form *pi-n-s- in Latin pinsdre, to pound: PISTON. 3. Possibly suffixed form *pis-lo- in Latin pilum, javelin, pestle: PILE?. 4. Perhaps Greek ptissein (pt- for p-), to crush, peel: PTISAN, (TISANE). [Pok. 1. (peis-2), pis- 796. peis-2. To blow. Germanic “fis- in Old Norse fisa, to fart, akin to the Scandinavian source of Middle English fise, fart: F1zGIG. [Pok. 2. peis- 796.] peisk-. Fish. Zero-grade form *pisk-. 1. Suffixed Ger- manic form “fisk-a- in: a. Old English fisc, fish: FISH; b. Middle Dutch vische, vis, fish: WEAKFISH. 2. Suffixed form “pisk-i- in Latin piscis, fish: PISCARY, PISCATORIAL, PISCES, PISCI-, PISCINA, PISCINE; GRAMPUS, PORPOISE. [Pok. peisk- 796.] pek-'. To make pretty. 1. Possibly Germanic “fagra- in Old English feger, beautiful: FAIR}. 2. Possibly Germanic *fagin-, *fagan-, to enjoy, in Old English fegen, joyful, glad (> fagnian, to rejoice): FAIN, FAWN}. [Pok. 1. pek- 796.] pek-?. To pluck the hair, fleece, comb. 1. Extended form *pekt- in Germanic *fehtan, to fight, in Old English feohtan, to fight: FIGHT. 2. Suffixed extended form *pekt-en- in: a. Latin pecten, a comb: PECTEN; b. zero-grade. form *pkt-en- in Greek kteis (genitive ktenos < *pktenos), a comb: CTENIDIUM; CTENOID, CTENOPHORE. [Pok. 2. pek- 797.] peku-. Wealth, movable property. 1. Germanic *fehu- in: a. Old Norse fé, property, cattle: FELLOW; b. Old French fie, fief: FEE; c. Medieval Latin feudum, feudal estate: FEUD?; INFEUDATION. 2. Suffixed form “peku-n- in Latin peciinia, property, wealth: PECUNIARY; IMPECUNIOUS. 3. Suffixed form *peku-l- in Latin peciilium, riches in cattle, private property: PECULATE, PECULIAR. [In Pok. 2. pek- 797.] pekv-. To cook, ripen. 1. Assimilated form (in Italic and Celtic) *kvekw- in Latin coquere, to cook: COOK, CUISINE, (CULINARY), KILN, KITCHEN, QUITTOR; APRICOT, BISCUIT, CONCOCT, DECOCT, PRECOCIOUS, RICOTTA. 2. Greek pe- pon, ripe: PEPO. 3. Greek peptein, to cook, ripen, digest (> peptos, cooked): PEPTIC; DRUPE, EUPEPTIC, PEPSIN, PEPTONE, PUMPKIN. 4. Greek -pepsia, digestion: DYSPEP- sia. 5. Sanskrit pakva-, ripe: PUKKA. [Pok. peky- 798.] pel-1. Dust, flour. 1. Latin pollen, fine flour, dust: PoL- LEN. 2. Latin pulvis, dust: POWDER, PULVERIZE. 3. Latin palea, chaff: PAILLASSE, PALEA. 4. Greek palunein, to sprinkle flour: PALYNOLOGY. 5. Greek poltos, porridge (made from flour), probably borrowed via Etruscan into Latin as puls, pottage: POULTICE, PULSE?. [Pok. 2 b. pel- 802.] pel-2. Pale. 1. Suffixed variant form *pal-wo- in: a. Ger- manic *falwaz in Old English fealu, fealo, reddish yellow: FALLOW DEER; b. Latin pallére, to be pale: PALE, PAL- LID, PALLOR; APPALL; C. Latin palumbés (influenced in form by Latin columbus, dove), ringdove, “gray bird”: PALOMINO. 2. Suffixed form “pel-ko- probably in Ger- manic *falkén-, falcon (< “gray bird”), in: a. Old French girfaut, gyrfalcon: GYRFALCON; b. Late Latin falcé, falcon (but Germanic *falkén- is also possibly from the Late Latin): FALCON. 3. Suffixed extended form *peli- wo- in: a. Greek pelios, dark: PELOPS; b. o-grade form *poli-wo- in Greek polios, gray: POLIOMYELITIS. 4. Per- haps Greek pelargos (< *pelawo-argos), stork (< “black- white bird”; argos, white; see arg-); PELARGONIUM. [Pok. 6. pel- 804.] pel-3. To fold. 1. Extended o-grade form *polt- in Ger- manic *falthan, *faldan in: a. Old English fealdan, faldan, to fold: FoLD!; b. Old High German faldan, to fold: FALTBOAT; Cc. Germanic compound “*faldistélaz, “folding stool” (*stdlaz, stool; see sta-), in Medieval Latin compound faldistolium, folding chair: FALDSTOOL;
829-pela-2
830-d. Germanic combining form *-falthaz, *-faldaz in Old English -feald, -fald, -fold: -roLD. 2. Combining form *.plo- in: a. Latin -plus, -fold (as in triplus, threefold): DECUPLE, MULTIPLE, OCTUPLE, QUADRUPLE, SEPTUPLE, (SEXTUPLE), TRIPLE; TRIPLOBLASTIC; b. Greek -plos, -ploos, -fold (as in haploos, haplous, single): -PLOID; (DIPLOID), HAPLOID. [Pok. 3. a. pel- 802.]
831-pel-4. Skin, hide. 1. Suffixed form *pel-no- in Germanic *felnam in Old English fell, skin, hide: FELL, 2. Ger- manic suffixed form *fel-men- in Old English filmen, membrane: FILM. 3. Suffixed form *pel-ni- in Latin pellis, skin: PELISSE, PELLICLE, (PELT!), PELTRY, PIL- LION; PELLAGRA, SURPLICE. 4. Greek -pelas, skin: ERY- SIPELAS. 5. Suffixed form *pel-to- in Greek pelté, a shield (made of hide): PELTATE. [Pok. 3 b. pel- 803.]
832-pel-5. To sell. Lengthened o-grade form *pdl- in Greek p6lein, to sell: BIBLIOPOLE, MONOPOLY. [Pok. 5. pel- 804.] pel-6. To thrust, strike, drive. I. Suffixed form *pel-de-. 1. Germanic “*felt-, *falt-, to beat, in: a. Old English anfilt(e), anfealt, anvil (“something beaten on”): ANVIL; b. Germanic “*feltaz, *filtiz, compressed wool, in (i) Old English felt, felt: FELT! (ii) Medieval Latin filtrum, filter, piece of felt: FILTER. 2. Latin pellere (past participle pulsus), to push, drive, strike: POUSETTE, PULSATE, PULSE!, PUSH; COMPEL, DISPEL, EXPEL, IMPEL, PROPEL, REPEL. 3. Suffixed o-grade form *pol-o-, fuller of cloth, in Latin polire, to make smooth, polish (< “to full cloth”): POLISH. II. Extended form *peb-. 1. Present stem *pelna- in: a. Latin appelldre, “to drive to,” address, entreat, appeal, call (ad-, to; see ad-): APPEAL; b. Latin compellare, to accost, address (com-, intensive prefix; see kom): COMPELLATION; Cc. Latin interpellare, “to thrust between,” interrupt (inter-, between; see en): INTERPEL- LATE. 2. Suffixed zero-grade extended adverbial form *pla-ti, in pre-Greek *pldti in Greek plésios, near (< “pushed toward”): PLESIOSAURUS. [Pok. 2. a. pel- 801.] pel-7. Dish. Suffixed lengthened-grade form *pél-owi- in Latin pélvis, basin: PELVIS. [Pok. 4. pel- 804.] pele-1. 1. To fill; with derivatives referring to abundance and multitude. Variant “*p/é-, contracted from “pleo-. I. Suffixed zero-grade form “pls-no-. 1.Germanic *ful- naz, *fullaz, full, in Old English full, full: FULL’. 2. De- rivative Germanic verb *fulljan, to fill, in Old English fylian, to fill: FILL. 3. Latin root *pldno-, replaced by *pléno- (influenced by Latin verb plére, to fill; see III. 1. below) in Latin plénus, full: PLENARY, PLENITUDE, PLENTY, PLENUM; PLENIPOTENTIARY, REPLENISH, TERREPLEIN. II. Suffixed form *p(e)la-u-. 1. Possibly Latin paliis, marsh (? < “inundated”; but possibly rather from pel-?): PALUDAL, PALUDISM. 2. Obscure compara- tive form (Old Latin p/ous) in Latin plis, more: PIU, PLURAL, PLUS; NONPLUS, PLUPERFECT, SURPLUS. 3. O-grade form *pol()-u- in Greek polus, much, many: POLY-; HOI POLLOI. III. Variant form “p/é-. 1. Latin plére, to fill: (ACCOMPLISH), COMPLETE, COMPLIMENT, COMPLY, EXPLETIVE, IMPLEMENT, REPLETE, SUPPLY. 2. Possibly suffixed form *plé-dhw- in Latin p/lébs, plébés, the people, multitude: PLEBE, PLEBEIAN, PLEBS; PLEBISCITE. 3. Suffixed form *plé-dhwo- in: a. Greek pléthos (Ionic pléthus), great number: ISOPLETH; b. Greek derivative verb pléthein, to be full: PLETHORA; PLETHYSMOGRAPH. 4. Suffixed (comparative) form *plé-i(sjon- in Greek pledn, pleién, more: PLEO-, PLEO- NASM; PLEIOTAXY, PLEIOTROPISM, PLIOCENE. 5. Suffixed (superlative) form *p/é-isto- in Greek pleistos, most: PLEISTOCENE. IV. Possibly Sanskrit piirah, cake (< “that which fills or satisfies”): POORI. [Pok. 1. pel- 798.] pela-2, Flat; to spread. Variant *pld-, contracted from *plaa-. 1. Suffixed form *pel{a)-tu- in Germanic “felthuz, flat land, in Old English feld, open field: FIELD. 2. Suf- fixed form *pel{a)-t-es- (by-form of *pel)-tu-) in Ger- manic *feltha-, flat land, in: a. Old High German feild, field: FELDSPAR; b. Middle Dutch veld, velt, field: VELDT. 3. Variant form “pld- in: a. suffixed form
833-pela-*
834-*pld-ru- in Germanic *fléruz, floor, in Old English flor, floor: FLOOR; b. suffixed form *p/d-no- in Latin planus, flat, level, even, plain, clear: LLANO, PIANO?, PLAIN, PLANARIAN, PLANE!, PLANE2, PLANE, PLANISH, PLANO-, PLANULA; AIRPLANE, EXPLAIN. 4. Suffixed zero-grade form *pb-ma in Latin palma (< *palama), palm of the hand: PALM!, PALM2. 5. Possibly extended variant form *plan- in: a. Greek planasthai, to wander (< “to spread out”): PLANET; APLANATIC; b. possibly Germanic *flan- in Old Norse flana, to wander aimlessly, akin to the Germanic source of French fléner, to walk the streets idly: FLANEUR. 6. Suffixed zero-grade form *pl-dh- in Greek plassein (< *plath-yein), to mold, “spread out”: -PLASIA, PLASMA, -PLAST, PLASTER, PLASTIC, PLASTID, -PLASTY; DYSPLASIA, METAPLASM, (TOXOPLASMA). 7. O-grade form *pols- in: a. Russian polyi, open: POLYN- Ya; b. Slavic polje, broad flat land, field, in Polish Polak, Pole: PoLACK, POLKA. See also extensions plak-' and plat-. [Pok. pels- 805.] pele-%, Citadel, fortified high place. Greek polis, city: POLICE, (POLICY!), POLIS, POLITIC, (POLITY); ACROPOLIS, COSMOPOLITE, MEGALOPOLIS, METROPOLIS, NECROPOLIS, POLICLINIC, PROPOLIS. [In Pok. 1. pel- 798.] pelis-. Also pels-. Rock, cliff. Germanic *felzam, rock, in Old Norse fjall, fell, rock, barren plateau: FJELD. [Pok. peli-s- 807.] pen-. Swamp. Suffixed o-grade form *pon-yo- in Ger- manic *fanjam, swamp, marsh, in Old English fenn, marsh: FEN. [Pok. 2. pen- 807.] penkve. Five. I. Basic form *penke. 1. Assimilated form *pempe in Germanic *fimf in: a. Old English fif, five: FIVE; b. Old High German finf, funf, five: FIN2. 2. Ger- manic compound “*fimftehun, fifteen (*tehun, ten; see dekm), in: a. Old English fifténe, fifteen: FIFTEEN; b. Old Norse fimmtdn, fifteen: FEMTO-. 3. Assimilated form *kvenke in: a. Latin quinque, five: CINQUAIN, CINQUE, QUINQUE-; CINQUEFOIL, QUINCUNX; b. Latin distributive quini, five each: KENO, QUINATE; C. Latin compound quindecim, fifteen (decem, ten; see dekm): QUINDECENNIAL. 4. Greek pente, five: PENTA-, PENTAD; PENTACLE, PENTADACTYL, PENTAGON, PENTAMETER, PENTARCHY, PENTASTICH, PENTATEUCH, PENTATHLON. 5. Sanskrit pavica, five: PUNCH’; PACHISI. II. Compound *penke-(d)konta, “five tens,” fifty (*-(d)konta, group of ten; see dekm). 1. Latin quinqudginta, fifty: QUINQUA- GENARIAN, QUINQUAGESIMA. 2. Greek pentékonta, fifty: Pentecost. III. Ordinal adjective *penk-to-. 1. Ger- manic “fimftdn- in Old English fifta, fifth: FIFTH. 2. Latin quintus (< *quinc-tos), feminine quinta, fifth: QUINT!, QUINTAIN, QUINTET, QUINTILE; QUINTESSENCE, QUINTILLION, QUINTUPLE. IV. Suffixed form *penkv-ro- in Germanic *fingwraz, finger (< “one of five”), in Old English finger, finger: FINGER. V. Suffixed reduced zero-grade form *pnk-sti- in Germanic *fii(nh)stiz in: a. Old English fyst, fist: Fist; b. Dutch vuist, fist: FOIST. [Pok. penkve 808, pnksti- 839.] pent-. To tread, go. 1. Germanic *finthan, to come upon, discover, in Old English findan, to find: FIND. 2. Suffixed o-grade form *pont-i- in: a. Latin pdns (stem pont-), bridge (earliest meaning, “way, passage,” preserved in the priestly title pontifex, “he who prepares the way”; -fex, maker; see dhé-1): PONS, PONTIFEX, PONTIFF, PON- TINE, PONTOON, PUNT}; (TRANSPONTINE); b. Russian put’, path, way, in sputnik, fellow traveler: SPUTNIK. 3. Zero-grade form *pnt- in Greek patein, to tread, walk: PERIPATETIC. 4. Suffixed zero-grade form *pnt-o- in Iranian *path-, probably borrowed (? via Scythian) into Germanic as *patha-, way, path, in: a. Old English peth, path: paTH; b. Middle Dutch pad, way, path: FOOTPAD. [Pok. pent- 808.] per’. Base of prepositions and preverbs with the basic meanings of “forward,” “through,” and a wide range of extended senses such as “in front of,” “before,” “early,” “first,” “chief,” “toward,” “against,” “near,” “at,”
835-49
836-per’
837-“around.” I. Basic form *per and extended form *peri. 1. Germanic *fer-, *far-, used chiefly as an intensive prefix denoting destruction, reversal, or completion, in: a. Old High German far-, in German vereinen, to unite: TURNVEREIN; b. Middle Dutch vieren, to let out, slacken: VEER; C. compound “*fer-getan, “‘to lose one’s hold,” forget (see ghend-). 2. Suffixed (comparative) form *per-ero-, farther away, in Germanic *fer(e)ra’in Old English feor(r), far: FAR. 3. Compound “per-n-yo-, of last year (*-n-, year; see en-), in Germanic *fernja- in Old High German firni, old: FmRN. 4. Latin per, through, for, by: PER, PER-; PARAMOUNT, PARAMOUR, PARGET, PAR- VENU. 5. Greek peri, around, near, beyond: PERI-; PERIS- SODACTYL. 6. Sanskrit pari, through, around: PALANQUIN. 7. Avestan pairi, around: PARADISE. II. Zero-grade form *pr-. 1.Germanic *fur, before, in: a. Old English for, before, instead of, on account of: FOR; b. Old English for-, prefix denoting destruction, pejora- tion, exclusion, or completion: For-. 2. Extended form *prt- in Germanic *furth-, forward, in Old English forth, forth: FORTH; AFFORD. 3. Suffixed (comparative) form *pr-tero- in Germanic *furthera- in Old English furthra, furthor, farther away: FURTHER. 4. Compound *pr-st-i- (or *por-st-i-, with o-grade form *por-), “that which stands before,” stake, post (see sta-). III. Extended zero-grade form “pro-. 1. Suffixed (superlative) form *pro-mo- in: a. Germanic *fruma-, *furma- in Old Eng- lish forma, first, foremost: FOREMOST, FORMER?; b. Latin compound prandium, “first meal,” late breakfast, lunch (probably < *pram-d-ium < *pram-(e)d-yo-; second ele- ment *-(e)d-, to eat; see ed-). 2. Suffixed (superlative) form *pro-isto- in Germanic *furista-, foremost, in Old English fyrst, fyrest, first: FIRST. 3. Suffixed form *pre-wo- in Greek *prowo-, first, foremost, in: a. analogi- cally suffixed Greek form *préw-arya in Greek prdira, forward part of a ship: PROw; b. suffixed (superlative) Greek form *préw-ato- in Greek prétos, first, foremost: PROTEIN, PROTIST, PROTO-, PROTON. 4. Suffixed form *pro-i in Celtic *(p)ari, *are in Gaulish ari (combining form are-), before, in Latin arepennis, half-acre (second element obscure): ARPENT. IV. Extended form “prod. 1. Germanic *fura, before, in: a. Old English fore, for (> Middle English fore-), before: FORE, FORE-; FOREFA- THER; b. Old High German fora (> German vor), before: VORLAGE; Cc. Germanic prefixed and suffixed form *bi-fora-na, in the front (*bi-, at, by; see ambhi), in Old English beforan, before: BEFORE. 2. Greek para, beside, alongside of, beyond: PARA-); PALFREY. V. Extended form *pré. 1. a. Germanic *fra, forward, away from, in Old Norse *frd (> Middle English fro), from: FRO; FROWARD; b. Germanic *fra-, completely (see ed-, éik-). 2. Suffixed form *pro-mo- in: a. Germanic *fram, from, in Old English from, from: FROM; b. Germanic *frum, forward, hence derivative verb *frumjan, to further, in Old French f(ojurnir, to supply, provide: FURNISH, VE- NEER; C. Czech pram, raft: PRAAM. 3. Suffixed form *pr6é-wo- in Germanic *frdw6-, lady, in: a. Old High German frouwa, lady: FRAU, (FRAULEIN); b. Middle Dutch vrouwe, woman: vRouw. 4. Latin pré, pro-, be- fore, for, instead of: PRO!, PRO-!; PURCHASE. 5. Suffixed form *pr6-no- in Latin prénus, leaning forward: PRONE. 6. Possible suffixed form *pro-ko- in Latin compound reciprocus, alternating, ‘‘backward and forward” (*re-ko-, backward; see re-): RECIPROCAL. 7. Suffixed adverb *pro-kve in: a. Latin prope, near: APPROACH, RAPPROCHEMENT, REPROACH; b. suffixed form *prok- ink“o- in Latin propinquus, near: PROPINQUITY; Cc. suf- fixed (superlative) form *prok’-samo- in Latin proximus, nearest: PROXIMATE; APPROXIMATE. 8. Compound *pro-bhw-o-, growing well or straightforward (*bhw-o-, to grow; see bheue-), in Latin probus, upright, good, virtuous: (PROBABLE), PROBE, PROBITY, (PROOF), PROVE; APPROVE, IMPROBITY, (IMPROVE), (REPROVE). 9. Greek pro, before, in front, forward: PRO-2. 10. Suffixed (com-
838-per-?
839-parative) form *pro-tero- in Greek proteros, before, former: HYSTERON PROTERON, PROTEROZOIC. VI. Exten- ded forms *prai-, *prei-. 1. Latin prae, before: PRE-; PRETERIT. 2. Suffixed (comparative) form *prei-yos- in Latin prior, former, higher, superior: PRIOR2. 3. Suffixed form *prei-wo- in: a. Latin privus, single, alone (< “standing in front,” “isolated from others”): PRIVATE, PRIVILEGE, PRIVITY, PRIVY; DEPRIVE; b. Latin proprius, one’s own, particular (< pré priv6, in particular, from the ablative of privus, single): PROPER, PROPERTY; APPRO- PRIATE, PROPRIOCEPTION, PROPRIOCEPTOR. 4. Extended form *preis- in: a. suffixed (superlative) form *preis-mo in (i) Latin primus (< *prismus; ablative plural primis), first, foremost: PREMIER, PRIMAL, PRIMARY, PRIMATE, PRIME, PRIMITIVE, PRIMO, PRIMUS; IMPRIMIS, PRIMA FACIE, PRIMAVERA, PRIMEVAL, PRIMIPARA, PRIMOGENI- TOR, PRIMOGENITURE, PRIMORDIAL (ii) Latin compound princeps, “he who takes first place” (-ceps, “-taker”; see kap-), leader, chief, emperor: PRINCE, PRINCIPAL, PRIN- CIPLE; b. suffixed form *preis-tano- in Latin pristinus, former, earlier, original: PRISTINE. VII. Extended form *pres- in compound “*pres-g“u-, “going before” (*gvu-, to go; see gWa-), in Greek presbus, old, old man, elder: PRESBYTER, (PRIEST); PRESBYOPIA. VIII. Extended form *proti in Greek pros, against, toward, near, at: PROS-; PROSOPOPEIA. Other possibly related forms are grouped under per-2, per-3, per-4, per-5, and per-’. [Pok. 2. A. per 810.] per-?. To lead, pass over. A verbal root belonging to the group of per’. I. Full-grade form *per-. 1. Suffixed form *per-tu-s in Germanic “*ferthuz, place for crossing over, ford, in Old Norse fjérdhr, an inlet, estuary: FIRTH, FJORD. 2. Suffixed form *per-ond in Greek peroné, pin of a brooch, buckle (< “that which pierces through”): PERONEAL. II. O-grade form *por-. 1. Germanic *faran, to go, in: a. Old English faran (> Middle English faren), to go on a journey, get along: FARE; WAYFARER, WAY- FARING, (WELFARE); b. Old High German faran, to go, travel: GABERDINE. 2. Suffixed form *por-o-, passage, journey, in Greek poros, journey, passage: PORE”; EMPO- RIUM, POROMERIC. 3. Suffixed (causative) form *por- eyo-, to cause to go, lead, conduct, in Germanic *farjan, to ferry, in Old English ferian, to transport: FERRY. 4. Lengthened-grade form *pdér- in: a. Germanic suffixed form *f6r-ja- in Old English (ge)féra, “fellow-traveler,” companion (ge-, together, with; see kom): FERE; b. Ger- manic suffixed (causative) form *fér-jan in Old High German fuoren, to lead: FUHRER. 5. Possibly suffixed form *por-no-, feather, wing (< “that which carries a bird in flight”), in: a. Germanic *farnd, feather, leaf, in Old English fearn, fern (having feathery fronds): FERN; b. Sanskrit parnam, leaf, feather: PAN2. III. Zero-grade form pr-. 1. Suffixed form *pr-tu-, passage, in: a. Ger- manic *furdu- in Old English ford, shallow place where one may cross a river: FORD; b. Latin portus, harbor (< “passage”): PORT!; IMPORTUNE, OPPORTUNE. 2. Suffixed form *pr-té in Latin porta, gate (> Old French porte, door): PORCH, PORT’, PORTAL, PORTCULLIS, PORTE-CO- CHERE, PORTER®, PORTICO, PORTIERE, PORTULACA. 3. Suffixed (denominative) form *pr-to- in Latin portdre, to carry: PORTS, PORTABLE, PORTAGE, PORTAMENTO, PORTATIVE, PORTER}; COMPORT, DEPORT, EXPORT, IM- PORT, (IMPORTANT), PORTFOLIO, PURPORT, RAPPORT, REPORT, (SPORT), SUPPORT, TRANSPORT. [Pok. 2. B. per 816.]
840-per-3. The young of an animal (< “a bringing forth,” “offspring”), Derivative root belonging to the group of per'. Suffixed o-grade form *por-si- in Germanic *farzi-, young cow, in Old English fearr, calf, and compound heahfore, calf (first element obscure): HEIFER. [In Pok. 2. D. per 818.]
841-per-‘. To try, risk (< “to lead over,” “press forward”). A verbal root belonging to the group of per’. 1. Lengthened grade *pér- in Germanic *féraz, danger, in Old English
842-50
843-pet-
844-fér, danger, sudden calamity: FEAR. 2. Suffixed form *peri-tlo- in Latin periclum, periculum, trial, danger: (PARLOUS), PERIL. 3. Suffixed form *per-yo- in Latin experirt, to try, learn by trying (ex-, from; see eghs): EXPERIENCE, EXPERIMENT, EXPERT. 4. Suffixed form *per-ya in Greek peira, trial, attempt (> peiran, to attempt): PIRATE; EMPIRIC. [Pok. 2. E. per 818.] per-5. To strike. Extended forms *prem-, pres- in Latin premere (past participle pressus), to press: PREGNANT?, PRESS!, PRESSURE, PRINT; APPRESSED, COMPRESS, DE- PRESS, EXPRESS, IMPRESS!, (IMPRINT), OPPRESS, RE- PRESS, (REPRIMAND), SUPPRESS. [Pok. 3. per- 818.] per-6. To traffic in, sell (< “to hand over,” “distribute”). A verbal root belonging to the group of per'. Base of two distinct extended roots. I. Root form *pret-. 1. Latin compound inter-pres (stem inter-pret-), go-between, negotiator (inter-, between; see en): INTERPRET. 2. Suf- fixed form “pret-yo- in Latin pretium, price: PRAISE, PRECIOUS, PRICE; APPRAISE, (APPRECIATE), DEPRECIATE. II. Root form *pers-. Suffixed form *p(e)r-n-o- in Greek pernanai, to sell, whence o-grade *por()-ndé in Greek porné, prostitute: PORNOGRAPHY. [In Pok. 2. C. per 817.] perd-. To fart. 1. Germanic *fertan, *fartén in Old Eng- lish *feortan (> Middle English farten), to fart: FART. 2. Greek perdix, partridge (which makes a sharp whirring sound when suddenly flushed): PARTRIDGE. See also pezd-. [Pok. perd- 819.] pere-'. To produce, procure. Perhaps an extension of per-3, a verbal root belonging to the group of per’. Possibly the same root as pere-2. Zero-grade form *pro- (becoming *par- in Latin) in: a. root form *par-d- in Latin pardre, to try to get, prepare, equip: PARADE, PARE, PARRY, (PARURE); APPARATUS, (APPAREL), COM- PRADOR, DISPARATE, EMPEROR, (IMPERATIVE), (IMPE- RIAL), (PARACHUTE), PARASOL, PREPARE, RAMPART, REPAIR}, SEPARATE, (SEVER), (SEVERAL); b. suffixed form *par-yo- in Latin parere, parire, to get, beget, give birth (> partus, accusative partum, birth): -PARA, PAR- ENT, -PAROUS, PARTURIENT, POSTPARTUM, REPERTORY; c. suffixed form *par-os, producing, in compound *pau- paros, producing little, poor (see pau-); d. suffixed form *par-ikaé in Latin Parcae, the Fates (who assign one’s destiny): Parca. [Pok. 2. D. per 818.] pere-2. To grant, allot (reciprocally, to get in return). Possibly the same root as pere-'. Zero-grade form *pro- (becoming *par- in Latin) in: a. suffixed form *par-ti- in Latin pars (stem part-), a share, part: PARCEL, (PARCE- NER), PARSE, PART; BIPARTITE, COMPART, IMPART, REP- ARTEE; b. possibly suffixed form *par-tid in Latin portid, a part (first attested in the phrase pré portiéne, in proportion, according to each part, perhaps assimilated from *pré partidne): PORTION, PROPORTION; C. perhaps Latin pdr, equal (> French pari, wager): PAIR, PAR, PARITY2, PARLAY, PEER?; COMPARE, IMPARITY, NONPA- REIL, PARI-MUTUEL. [Pok. 2. per, Section C. 817.] perg-. Pole, stem. Possibly Latin pergula, a projection, balcony, outhouse: PERGOLA. [Pok. 1. perg- 819.] perk-'. Speckled. Often used in names of spotted or pied animals. Greek perké, the perch: PERCH?. [Pok. 2. perk- 820.] perk-2. To dig out, tear out. Zero-grade form *prk- in Germanic *furh- in Old English furh, trench: FURROW. [Pok. 3. perk- 821.] perkwu-. Oak. 1. Zero-grade form *prkv- in Germanic *furhu- in Old English furh, fyrh, fir: rir. 2. Assimilated form *kverku- in Latin quercus, oak: QUERCETIN, QUER- CITRON. [Pok. perk#u-s 822.] persna. Heel. Latin perna, ham, leg, sea mussel: PEARL}. [Pok. persna 823.] pes-. Penis. Suffixed form *pes-ni- in Latin pénis (< *pesnis), penis, tail: PENCIL, (PENICILLIUM), PENIS. [Pok. 3. pes- 824.] pet- Also pete-. To rush, fly. Variant *p#é-, contracted from *ptea-. 1. Suffixed form *pet-rd in Germanic *feth-
```


## [2026-09-07T20:43:42.843Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '815,819p' AHD_watkins1985.txt"
}
```


### [2026-09-07T20:43:42.881Z] TOOL RESULT

```
peig-
shackle,” entangle, hinder (in-, in; see en): IMPEDE. 6. Suffixed form *ped-ikd- in Latin pedica, fetter, snare: DISPATCH, IMPEACH. 7. O-grade form *pod- in: a. Greek
* pous (stem pod-), foot: PEW, -POD, PODITE, PODIUM;
ANTIPODES, APODAL, APPOGGIATURA, APUS, CALIBER, LYCOPODIUM, MONOPODIUM, OCTOPUS, PELECYPOD, PHALAROPE, PLATYPUS, PODAGRA, PODIATRY, PODOPHYL- LIN, POLYP, POLYPOD, SYMPODIUM; b. Russian pod, un- der: PODZOL. 8. Suffixed form *ped-ya in Greek peza, foot: TRAPEZIUM. 9. Suffixed form *ped-o- in: a. Greek pedon, ground, soil: PEDO-!; PARALLELEPIPED; b. San- skrit padam, footstep, foot, and pat (> Hindi paisd), foot: PAISA, PICE, PIE’, PUG3; c. Middle Persian pdi, leg, foot: PAJAMAS, TEAPOY; d. lengthened-grade form *pédo- in (i) Greek pédon, rudder, steering oar: PILOT (ii) Greek pédan, to leap: DIAPEDEsIs. 10. Suffixed form *ped-i- in Greek pedilon, sandal: CYPRIPEDIUM. II. Verbal root *ped-, to stumble, fall. 1. Germanic *fetén in Old English fetian, feccean, to bring back: FETCH!. 2. Latin *ped- in: a. suffixed (comparative) form *ped-yos in Latin péor, worse (< “stumbling”): PEJORATION; IMPAIR; b. suffixed (superlative) form *ped-samo- in Latin pessimus, worst: PESSIMISM; C. suffixed form *ped-ko- in Latin peccdre, to stumble, sin: PECCABLE, PECCADILLO, PECCANT; IMPEC- CABLE. [Pok. 2. péd- 790.]
ped-2. Container. 1. Suffixed o-grade form *pod-om in Germanic “fatam in Old English fzt, cask: vat. 2. Suf- fixed o-grade form *pod-ilo- in Germanic *fatilaz in Old English fetel, girdle: FETTLE. 3. Probably full-grade form *ped- in Germanic *fet- in Middle High German vetze, “clothes,” rags, probably akin to the source of obsolete English fritter, fragment: FRITTER}. [Pok. 1. péd- 790.]
```


## [2026-09-07T20:43:48.899Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '810,815p' AHD_watkins1985.txt"
}
```


### [2026-09-07T20:43:48.938Z] TOOL RESULT

```
ors-. Buttocks, backside. 1. Suffixed form *ors-o- in Germanic *arsaz in Old English zrs, ears, backside: ass?. 2. Suffixed form ‘*ors-d- in: a. Greek oura, tail: URO-2, -UROUS; ANTHURIUM, ANURAN, CYNOSURE, EREMURUS, OXYURIASIS, SQUIRREL, TRICHURIASIS; b. probably Greek silouros, sheatfish (< obscure first element + oura): SILURID. [Pok. ers- 340.]
pan-
os-. Ash tree. Germanic “aski- in Old English zsc, ash: ASH?2. [Pok. 6s- 782.] 6s-. Mouth. 1. Latin ds (stem 6r-), mouth, face, orifice, and derivative dstium (< suffixed form *6s-to-), door: ORAL, OS!, OSCULATE, OSCULUM, OSTIARY, OSTIUM, USHER; INOSCULATE, ORIFICE, ORINASAL, OROTUND, OSCITANCY, PERORAL. 2. Possibly Latin auriga, chari- oteer (< *6r-ig-, “he who manages the (horse’s) bit”; -ig-, driving, from *ag-; see ag-): AURIGA. [Pok. 1. 6us- 784.] ost-. Bone. 1. Latin os (stem oss-), bone: 082, OSSEOUS, OSSICLE, OSSUARY; OSSIFRAGE, OSSIFY. 2. Greek osteon, bone: OSTEO-; ENDOSTEUM, EXOSTOSIS, PERIOSTEM, SYN- OSTOSIS, TELEOST. 3. Suffixed form *ost-r- in: a. Greek ostrakon, shell, potsherd: OSTRACIZE, OSTRACOD; b. Greek ostreon, oyster: OYSTER; C. variant form in Greek astragalos, vertebra, ball of the ankle joint, knuck- lebone, Ionic molding: ASTRAGAL, ASTRAGALUS. [Pok. ost(h)- 783.] ous-. Also aus-. Ear. 1. Suffixed form *ous-en- in Ger- manic *auzan- in Old English éare, ear: EAR}. 2. Suffixed form *aus-i- in Latin auris, ear: AURAL!, AURICLE; AURIFORM, ORMER. 3. Latin auscultdre, to listen to (*aus- + *kli-to-, inclined; see klei-): AUSCULTATION, scouT!. 4. Suffixed basic form *ous-os- in: a. Greek ous (stem 6t-), ear: OTIC, OTO-; MYOSOTIS, PAROTID GLAND; b. Greek Jagés, hare (< */ag-ous-, “with drooping ears”; *lag-, to droop; see slég-). [Pok. dus- 785.] owi-. Sheep. 1. Germanic *awi- in Old English ewe, eowu, ewe: EWE. 2. Latin ovis, sheep: OVINE; OVIBOS. [Pok. oui-s 784.] pa-. To protect, feed. Contracted from *pas-. 1. Suffixed form *pé-trom in Germanic *fodram in: a. Old English fédor, fodder: FODDER; b. Old French feurre, fodder: FORAGE; C. Old French forreure, trimming made from animal skin, fur (< “sheath, case, lining”): FuR. 2. Suf- fixed form *pd-dhlom (doublet of *pd-trom) in Latin padbulum, food, fodder: PABULUM. 3. Extended form *pat- in: a. Germanic *féd-, food, in Old English foda, food: Froop; b. Germanic denominative *fédjan, to give food to, in Old English fédan, to feed: FEED; Cc. suffixed form *pdt-tro- in Germanic *fdstra- in Old English fostor, food, nourishment: FOSTER. 4. Extended form *pds- in: a. suffixed form *pds-sko- in Latin pdscere, to feed: PASTURE; ANTIPASTO, PESTER, REPAST; b. Latin pdstor, shepherd: PASTOR; C. suffixed form *pds-t-ni- in Latin pGnis, bread (diminutive pastillus, medicine tablet): PANADA, PANATELA, PANNIER, PANOCHA, PANTRY, PAS- TILLE, (PENUCHE); APPANAGE, COMPANION, (COMPANY). 5. Suffixed form *pd-ti- in Iranian *pdti- in Persian pdd, protecting against: BEZOAR. 6. Suffixed form *pd-won-, protector, in Old Persian khshathra-pdvd, protector of the province: SATRAP. [Pok. pd- 787, 1. pd(i)- 839.] pag-. Also pak-. To fasten. 1. Lengthened-grade form *“pak- in Germanic *fogjan, to join, fit, in Old English fégan, to fit closely: FAY}. 2. Nasalized form *pa-n-g- in: a. Germanic *fangiz, seizure, in (i) Old English fang, feng, plunder, booty: FANG (ii) Dutch vangen, to catch: VANG; b. Latin pangere, to fasten: COMPACT!, IMPINGE. 3. Root form *pak- in: a. Latin pdx, peace (< “a binding together by treaty or agreement”): PACE?, PAY!, PEACE; APPEASE, PACIFIC, PACIFY; b. Latin pacisci, to agree: PACT. 4. Suf- fixed form *pak-sio- in: a. Latin pdlus, stake (fixed in the ground): PALE!, PALISADE, PEEL’, POLE?; IMPALE, TRA- VAIL, (TRAVEL); b. probably Latin pdla, spade: PALETTE, PEEL*. 5. Lengthened-grade form *pdg- in: a. Latin pdagus, “boundary staked out on the ground,” district, village, country: PAGAN, PEASANT; b. Latin pdgina, “trellis to which a row of vines is fixed,” hence (by metaphor) column of writing, page: PAGE?, PAGEANT; c. Latin prépdgés (pré-, before, in front; see per'), layer of vine, offspring (< “a fixing before”): PROPAGATE; d. Greek pégnunai, to fasten, coagulate: PECTIN, PEGMA- TITE. [Pok. pak- 787.] pan-. Fabric. 1. Germanic *fandn- in: a. Old English
pandoura
fana, flag, banner, weathercock: VANE; b. compound *gund-fanon-, “battle-flag” (see ghen-'). 2. Extended form *panno- in Latin pannus, piece of cloth, rag: PANE, PANEL. 3. Possibly Greek pénos, web (> Latin pdnus, a swelling): PANICLE. [Pok. pan- 788.] [pandoura. Three-stringed lute. Greek noun of obscure origin. BANDORE, MANDOLIN, PANDORE.] pant-. All. Attested only in Tocharian and Greek. Greek pas (neuter pan, stem pant-), all: PAN-, PAN; DIAPASON, PANCRATIUM, PANCREAS. [In Pok. 1. keu- 592.] pap-'. Teat (sound symbolism). Probably the same word as pap-2. 1. Middle English pap(pje, nipple: Pap}. 2. Latin diminutive papula, pimple (diminutive papilla, nipple): PAPILLA, PAPULE. 3. Variant form *pup(p)- in Latin piipus, boy, and pupa, girl: puPA, PUPIL. [In Pok. barb- 91.] pap-?. Food (baby-talk root). Reduplication of pa-. 1. Germanic nasalized form *pamp- in Flemish frequen- tative pamperen, to cram with food, akin to the source of Middle English pamperen, to pamper: PAMPER. 2. Latin pappa, food (> Middle English pap, soft food): PAP?, POPPYCOCK. [Pok. pap(p)a 789, ba*mb- 94.] papa. A child’s word for “father,” a linguistic near-uni- versal found in many languages. 1. French papa, father: PAPA. 2. Greek pappas, father, and pappos, grandfather: PAPPUS, POPE. [Pok. pap(p)a 789.] paso-. Kinsman by marriage. Latin parri- (for pari-) in compound parri-cida (oldest form paricidas), murderer of a near relation: PARRICIDE. [Pok. pdso-s 787.] past-. Solid, firm. 1. Germanic *fastuz, firm, fast, in: a. Old English fest, fixed, firm: FAST!; STEADFAST; b. Middle Dutch vast, firm, fast: AvAST. 2. Germanic *fastinon, to make firm or fast, in Old English festnian, to fasten, establish: FASTEN. 3. Germanic *fastén, to hold fast, observe abstinence, in: a. Old English festan, to abstain from food: rasT?; b. Old Norse fasta, to abstain from food: BREAKFAST. [Pok. pasto- 789.] pau-. Few, little. I. Adjectival form *pau-, few, little. 1. Germanic *fawaz in Old English féawe, few: FEW. 2. Suffixed form *pau-ko- in Latin paucus, little, few: PAUCITY, POCO. 3. Suffixed form *pau-ro- in metathetical form *par-wo- in Latin parvus, little, small, neuter parvum, becoming parum, little, rarely: PARAFFIN, PAR- vovirus. 4. Compound “pau-paros, producing little, poor (*par-os, producing; see pere-'), in Latin pauper, poor: PAUPER, POOR, POVERTY. II. Suffixed reduced variant form “pu-lo-, young of an animal. 1. Germanic *fulén- in Old English fola, young horse, colt: FOAL. 2. Germanic derivative *fuljé in Old Norse fylja, female colt: FILLY. 3. Latin pullus (probably with expressive gemination), young of an animal, chicken: POLTROON, PONY, POOL?, POULARD, PULLET; CATCHPOLE. III. Basic form *pau- and variant form *pi-, boy, child. 1. Suffixed form *pu-ero- in Latin puer, child: PUERILE, PUERPERAL. 2. Suffixed form “pi-sso- in Latin piisus, boy: PUSIL- LANIMOUS. 3. Suffixed form *paw-id- in Greek pais (stem paid-), child (> paideia, education): PEDO-?; ENCY- CLOPEDIA, ORTHOPEDICS. [Pok. pdu- 842.] paus-. To leave, desert, cease, stop. Greek pauein, to stop (> Latin pausa, a stopping): PAUSE, (PESADE), (POSE!); COMPOSE, DIAPAUSE, (REPOSE!). [Pok. paus- 79.] ped-'. Foot. I. Nominal root. 1. Lengthened o-grade form *pod- in Germanic *fot- in Old English fot, foot: Foor. 2. Suffixed form *ped-ero- in Germanic *feteré in Old English fetor, feter, leg iron, fetter: FETTER. 3. Suffixed form *ped-el- in Germanic *fetel- in Old High German vizzelach, fetlock, akin to the Germanic source of Middle English fitlock, fetlock, fetlock: FETLOCK. 4. Basic form *ped- in Latin pés (stem ped-), foot: PAWN2, -PED, PEDAL, PEDATE, PEDESTRIAN, PEDI-, PEDICEL, PEDUNCLE, (PEON), PES, PIONEER; MILLIPEDE, SESQUIPEDALIAN, TRIPEDAL, TRIVET, VAMP!. 5, Form *ped-yo- in: a. Latin expedire, to free from a snare (ex-, out of; see eghs): EXPEDITE; b. Latin impedire, “to put in fetters, hobble,
peig-
```


## [2026-09-07T20:43:49.994Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK 790 in POK_02 (leaf = p - 344) ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==446' POK_02.txt | head -60"
}
```


### [2026-09-07T20:43:51.456Z] TOOL RESULT

```
=== POK 790 in POK_02 (leaf = p - 344) ===
```


## [2026-09-07T20:43:57.825Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"pē̆d-\\|ped-, pō̆d-\\|pēd-, pŏd-\" POK_full.txt | head -20\necho \"---\"\ngrep -n \"790\" POK_full.txt | grep -i \"ped\\|fuss\\|fuß\" | head"
}
```


### [2026-09-07T20:43:57.906Z] TOOL RESULT

```
---
```


## [2026-09-07T20:44:01.541Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nls -la POK_*.txt\ngrep -c \"\" POK_full.txt POK_02.txt\necho \"--- sample\"\nhead -c 800 POK_full.txt\necho; echo \"--- search 'Fuß' near ped\"\ngrep -n \"pōd-\" POK_full.txt | head"
}
```


### [2026-09-07T20:44:01.629Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb  981836 Sep  4 14:06 POK_01.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1137861 Sep  4 14:06 POK_02.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1170809 Sep  4 14:06 POK_03.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 3971883 Sep  4 14:06 POK_full.txt
POK_02.txt:6716
POK_full.txt:93771
--- sample
List of language abbreviations in tlie lED 



Abbreviation Language name 


Aeq. 




Aequian 


Akk. 




Akkadian 


Alan. 




Alanian (=Old Ossetic) 


Alb. 




Albanian 


Anat. 




Anatolian 


Ang. 




Anglian 


AngN 




Anglo-Norman 


Aram.- 


■Iran 


Aramaeo-lranian 


Ash. 




Ashkun 


Ass. 




Assyrian 


Auk. 




Aukshtaitian 


Bactr. 




Bactrian 


Bel. 




Belorussian 


Br. 




British 


Bret. 




Breton 


BVan. 




Bas-Vannetais 


CCI. 




Continental Celtic 


Chak. 




Chakavian 


Chor. 




Chorasmian 


Clb. 




Celtiberian 


Class. 


Skt. 


Classical Sanskrit 


Co. 




Cornish 


Corn. 




Cornouillais 


Dae. 




Dacian 


Dan. 




Danish 


Dard. 




Dardic 


Dzuk. 




Dzukian 


EBI. 




East Baltic 


EGm. 




East Germanic
--- search 'Fuß' near ped
```


## [2026-09-07T20:44:05.147Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"Page 790\\|Seite 790\\|^790$\" POK_full.txt | head\necho \"--- try pod- fuss ---\"\ngrep -n -i \"ped-, pod-\\|1\\. ped-\\|2\\. ped-\" POK_full.txt | head -20"
}
```


### [2026-09-07T20:44:06.349Z] TOOL RESULT

```
--- try pod- fuss ---
```


## [2026-09-07T20:44:11.154Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"ped\" POK_full.txt | grep -i \"790\" | head -10\necho \"=== POK_02 leaves check ===\"\npython3 - <<'EOF'\nt=open('POK_02.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(t))\nfor i in range(440,452):\n    print(i, repr(t[i][:100]))\nEOF"
}
```


### [2026-09-07T20:44:12.460Z] TOOL RESULT

```
Exit code 1
=== POK_02 leaves check ===
434
Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
IndexError: list index out of range
```


## [2026-09-07T20:44:16.335Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nfor f in ('POK_01.txt','POK_02.txt','POK_03.txt'):\n    t=open(f,encoding='utf-8',errors='replace').read().split('\\f')\n    print(f,len(t))\n    # find leaf mentioning 'pessimus' or 'Fuss'\n    for i,p in enumerate(t):\n        if 'pessimus' in p or 'pessimum' in p:\n            print('  pessimus leaf',i)\nEOF"
}
```


### [2026-09-07T20:44:17.579Z] TOOL RESULT

```
POK_01.txt 364
POK_02.txt 434
POK_03.txt 430
  pessimus leaf 24
```


## [2026-09-07T20:44:26.034Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('POK_03.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (22,23,24):\n    print('='*15,'leaf',i)\n    print(t[i][:2600])\nEOF"
}
```


### [2026-09-07T20:44:28.220Z] TOOL RESULT

```
=============== leaf 22
wickelter  Faden, Gewebe,  Gewand',  7trjVi^oi.iaL  ,webe'  (dor.  TtäviadsTai  Theokr.);  ablaut. lat.  pannus  ,Tuch,  Lappen'  (expressives  nn);  got.  fana  m.  ,Lappen, Schweißtuch',  ahd.  fano  ,Zeug,  Tuch',  nhd.  Fahne,  ags.  fana  m.  ,Fahne, Tuch;  Iris', /ane, /anw  f.  ,Fahne,  Schwertlilie';  unklar,  mir.  an-art  ,lei- nernes  Tuch';  dürfte  man  das  gr.  und  lat.  ä  als  expressiv  auffassen  (vgl. oben  S.  211  zu  gall.  drappus),  könnte  Beziehung  zu  {s)pen-  ,spannen, spinnen^  angenommen  werden.
WP.  II  6,  WH.  II  247  f.
pando-s  , gekrümmt'.
Lat.   pandus    .gekrümmt,    gebogen,    geschweift'    (pandö,    -äre    , biegen, krümmen')  =  aisl.  fattr  {*fanta-)  ,zurückgebeugt,  zurück^ebo-en'. WP.II  6;  s.  unter  1.  pet-.
789
aak',  P^^S~  »schwellen',  bedeutungs-  und  ursprungsverwandt  mit  ba^mb- pa^mp-,  bu-,  pu-  usw.  (oben  S.  94  f.)  , aufblasen,  schwellen'.
Lat.  pänus  (*pank-no-)  , entzündliche  Geschwulst,  Büschel  der  Hirse', rom.  p^'^'^  j  davon  pänlcum  , Pflanze  mit  einem  Büschel' ;  panceps  „e'Axog xtrjyovg  irti  rgaxrjUov"^  Gloss.  (aus  *päno-caps),  pantex  , Wanst,  Gedärme' fauf  Grund  eines  Partiz.  *panc-to-s  , geschwollen,  aufgeblasen');
aksl.  pgciti  se  ,infläri',  pgcina  ,mare',  poln.  pqh  .Knospe',  pek  ,Bündel', russ.  puk  , Bündel,  Büschel,  Strauß',  püca  , Blähung'  usw.;  mit  Media aksl.  pggy  ,corjmbus',  pggvica  ,globulus'.
WP.  II  6,  WH.  II  248.
pap(p)^  Kinderlallwort  für  , Vater;  Speise'.
Gr.  Ttdnrca  Vok.,  -ov  Gen.  ,Papa',  TCctTtaq'  Ttargög  vno'AOQio^a,  TcartTtog Großvater'   (daraus  lat.  pappus),   TtaTcrciag  , Väterchen',   nanTcaCeiv   .Papa sagen';   skyth.  Zevq  JJaTtalog'^   \a.t.  päpa,  pappa  Kinderlallwort  für  , Speise; Vater',  pappö  -äre  , essen';   nhd.  pappen   , essen'  (mit  stockender  Lautver- schiebung durch  nebenhergehende  Neuschöpfung). WP.  II  4,  WH.  II  249,  250;  vgl.  appa  oben  S.  52.
pär-  , zeigen;  sichtbar  sein'.
Gr.  fcsTtocQstv  ,vorzeigen',  Ttsfcagsvat^ov  e'öq)QaGTOv,  aacpig  Hes. ;  lat. päreö,  -ere  ,erscheinen,  sichtbar  sein,  sich  zeigen;  Folge  leisten,  gehorchen', appäreö,  compär
=============== leaf 23
eö  , erscheine'  (parret,  nach  Festus  für  päret,  wie  baca  : bacca  usw.).
WP.  II  6,  WH.  II  252  f.
parikä  ,Buhlerin,  Konkubine';  nur  iran.  und  irisch.
Av.  pairikä    , dämonische   Buhlerin',    mp.  parlk,    np.  patn    ,Peri'    (iran. *parlka)]  mir.  a{i)rech  , Konkubine'. Thurneysen  IF.  42,  146  f.,  WP.  II  7.
päsö-s  , Verwandter'?
Gr.  TCTjög,  dor.  rtadg  , Verschwägerter',  naatTai'  ovyysveig  lies.;  lat.  päri- clda  (*päso-kaidä)  jünger  parri-czda  .Mörder  an  nahen  Verwandten';  nach Wackernagel  Gnomon  6,  458  aus  *parso-clda  zu  ind.  purum-  ,Mensch' aus  ai.  '^pursa-.
WP.  II  7,  WH.  II  253  f.
pasto-  ,fest'.
Ai.  pastyd-m  ,Wohnsitz' ;   arm.    hast   (i-St.)   ,fest';   aisl. /as^r,  3i^s.  fcest, as.  fast,  ahd.  festi,  nhd.  fest. WP.  II  7  f.
790  •
paus-  ,los-,  ablassen'.
Gr.  Tiavo)  ,mache  aufhören',  Med.  ,höre  auf,  lasse  ab',  navXa  ,Ruhe', 7iavGu)Xri  ,Rast' ;
apr.  pausto  ,wild',  aksl.  pusU  ,öde,  wüst';  pustüi,  russ.  pustüh,  puskäh ,(los)lassen',  sloven.  delo-pust  ,Feierabend'  usw.
WP.  II  1,  Trautmann  208  f.
päuson-  :  püson-  , Göttername'.
Ai.  Püsdn-  m.  ,vedischer  Gott^  Hüter  und  Mehrer  der  Herden  und  des menschlichen  Besitzes  überhaupt',  gr.  U&v,  ark.  Jj&ixjv  (^TIgvgwv)]  iWyv. (messap.)  PN  Pausö,  -onos,  gall.  (venet.)  PN  Fusa  m. ;  unsicher,  ob  zu  ai. pusyati,  pumäti,  pösati  ,gedeiht,  wächst  zu,  macht  gedeihen,  ernährt', pösa-  m.  , Gedeihen,  Wachstum' ;  s.  unter  1.  pu-.
WP.  II  2;  vgl.  Charpentier  Idg.  Jb.  19,  90.
1.  p^d-,  pBd-  , fassen;  Gefäß';  pedo-  , Gefäß,  Einfassung'.
Ai.  vielleicht  palla-  m.  , Kornbehälter',  palll  .Getreidemaß'  (falls  -II-  aus -dl-)]  ahd.  fazzön,  mhd.  vazzen  ,in  ein  Gefäß  tun,  fassen,  rüsten,  sich bekleiden',  ahd.  fezzil,  mhd.  vezzel  ,Band,  Fessel',  ags.  fetel{s)  m.  , Gürtel', aisl.  fetill  m.  , Schulterband'  (germ.  *fatila-),  ahd.  vazz  , Behälter,  Kasten', as.  fat  n.  , Gefäß',  ags.  faet  n.  , Gefäß,  Faß',  aisl.  fat  n.  , Gefäß,  Kleid'; 3Lgs.  ßetels  ,Gefäß',  ahd.  givazzi  , Bagage',  mhd.  gevxzze,  nhd.  , Gefäß';  got. fetjan,  ags.  fäetan  , schmücken',  aisl.  fseta  ,es  mit  jemandem  zu  tun  haben (,schmücken'  aus  , schön  tun  mit?');  lit.  pMas  , Getreidegarbe',  lett.  peda ,Bund,  Armvoll',  ablaut.  lit.  püodas,  lett.  puods  m.  ,Topf'.
WP.   II  22,  Trautmann  227.
2.  ped-,  päd-  m.  ,Fuß' ;  Nom.  Sg.  p^ts.  Gen.  ped-es/-ös,  Nom.  PI.  ped-es]
verbal    .gehen,    fallen';  pedo-m    ,(Fu
=============== leaf 24
treffend';  aus  , Fußfessel'  ist  z.  T. schon  grundsprachlich  ,Fessel  überhaupt'  geworden. 1.  Ai.  päd-  ,Fuß'   {pdt,  pädam,  paddh),   av.  päd-  ds. ;   apers.   pädaibiyä ,mit    den   Füßen';    arm.  ot-k'    „Ttödsg'',    ot-n   ,,7tovg,    noda'']    gr.  jtwg,  att. Tiovg,   Gen.  nodög  ,Fuß'   {kyLaTÖiiTradog  ,100  Fuß  lang');  lat.  pes,  p^dis  ds., umbr.  peri,  persi   ,pede'    (dupursus   ,bipedibus',  -u-  wohl   aus   -ö-);    air.  is , unterhalb'    (wovon    ise      ,niedrig')   m.   Dativ,   aus   dem   Lok.    PL   *ped-su ,zu  Füßen'  deutbar  =  alb.  posh  in  perposh  ,unten',  posh-te  ,herab,  unter- irdisch; unten,  hinunter';   got.  fötus,    aisl.   fötr,  ags.  föt  (Nom.   PI.   aisl. fetr,  ags.  fet  aus  *föt-iz)  ahd.  fuoz   ,Fuß' ;   hitt.   luv.  pata-^   Hierogl.-bitt. pat  ds.;  toch.  A  pe,  B  pai,  Dual  A  pem,  B  paine-
791
zu  ped-  ,Fuß'  gehört  gv.  dial.  rceda  „^«t«",  ursprüngl.  ,(jemandem) auf  dem  Fuße',  vg-1.  lat.  pedisequus,  -a  , Diener,  -in*  eig.  ,auf  dem  Fuße folgend'  und  unten  die  arm.  von  het  , Fußspur'   gebildeten  Präpositionen;
mit  -i-ös,  -i-t-  , gehend'  sind  gebildet:  gr.  rtet^ög  ,pedestris',  lat.  _pec?-es, -i't-is  , Fußgänger,  Fußsoldat' ;  von  lat.  jpes  stammt  pedäre  ,mit  einem  Fuß versehen,  stützen',   und  davon  wieder  pedum  , Hirtenstab,  Stütze';
pedio-  in  ai.  pddya-  .den  Fuß  betreffend',  pddyä  , Fußtritt,  Huf,  av. paiöyä  ,Fuß',  gr.  neCa  f.  ,Fuß,  unterer  Rand,  Kante,  Saum,  kleines Fischernetz',  lat.  acu-pedius  , schnellfüßig',  ahd.  ßzza  , Gewinde,  Garn' (=  gr.  7t6^a),  nhd.  , Fitze',  (wozu  germ.  *fetl  f.  in  aisl.j^^  , Schwimmhaut, Rand^,  ags.  ßtt  , Abschnitt,  Gedicht',  norw.  dial.  ßor-ßt  , Eidechse',  „tstqü- /Tfi^og"),  lit.  lengva-pldis  ,leisefüßig' ;  pedi-  in  gr.  nsdllov  n.  , Sandale' und  germ.  *fetl]  podio-m  :  mir .  u{i)de  n.  , Reise'.
2.  Verbal:  ai.  pddyate  ,geht,  fällt'  (ä-patti-  , Unfall';  padäti-,  pat-ti-  m. ,Fußknecht'),  av.  paiöyeiti  ,bewegt  sich  nach  abwärts,  legt  sich  nieder': 2iVs[.  pad<^,  pasti  , fallen'  auch  _po-pasfi  , fassen'  eig.  , auf  jemanden  fallen,  an- fallen' (oder  zu  1.  pgc?-?);  napasth  , casus' ;  lit.  pedinu,  -inti  , langsam  gehen, leise  treten',  peduoti  , Fußtritte  machen',  gr.  Tcrjödcü  , springe,  hüpfe';  vgl.  zur e-Stufe  noch  lit.  pedä  , Fußspur',  pescias  ,zii  Fuß'  aus  *ped-tios,  lett.  p^da  , Fuß- sohle, Fußstapfe,  Fuß  als  Maß',  pec  (aus  pedis,  Instr.  Fl.  von  p^ds  ,
```


## [2026-09-07T20:44:43.676Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN leaf 84 (p.63) ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==85' HRN.txt | head -50"
}
```


## [2026-09-07T20:44:44.384Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD pāy/payg/payādag ===\"\ngrep -n \"pāy\\|payg\\|payādag\\|pādag\\|pay \" PHD.txt | head -30"
}
```


### [2026-09-07T20:44:44.921Z] TOOL RESULT

```
=== HRN leaf 84 (p.63) ===
— 63 —
279. pälez 'Garten (Sahn. I, 73 Vers 207) ^), palezhan, arab.
LW. faliz,
ap. nagdÖHöog; aw. pairida^za-,
LW. kurd. päres, arm. partez, syr. Dn*)5?, JDD'^'TlEi.
280. panzde 'fünfzehn , vergl. pänsed 'fünfhundert'.
aw. paücadasa 'fünfzehn; skr. pdflcada^a; phlv.
pancdahion,
kurd. [daupe/ij etc.]; paiizde (LW.); afy. pinjalas;
oss. d. findtäs^ t. findfäs (292) ; bei. panzda (LW.).
281. päl^ pä Tuss ; vergl. paye 'Stufe', päym.
aw. päda- 'Puss* ; phlv. pCLT *Fuss', päyah *Stufe' ; ai.
päda-; arm. otn (H. No. 280).
kurd. pai (LW.) 'Fuss'; bei. päd, n. /xlJ, ^^ö^ (291);
oss. *fad aus bäymmoad-äi 'barfuss*, bäyömbad-äi 'bar-
fuss erschlossen? (267).
282. päyisten 'fest stellen , dauern ; erwarten ; vergl.
päylden 'schützen', päyende.
ap. l/^pä-, pö^wi; schützen; aw. l/^pÄ-, pcf«7e, vergl.
paiti.pait^ (yt. 10, 19) erwartet, versieht sich';
ai. [/'pä-, pdti.
Bei AM. ist päyTden als schützen, conserviren sehr
häufig, z. B. 'schützt vor Zersetzung (191 Zeile 2,
248 Zeile 6), erhält das Haar' (122 Zeile 7), *die
Gesundheit' (237 Zeile 4); auch 'sich halten', z. B.
seine Kraft hält sich nicht länger als ein Jahr (187
Zeile 3 v. u.).
Vullers (Lexicon) nimmt mit Unrecht zwei ver-
schiedene np. päyiden an.
Da für p&yiden (phlv. pöyitan) die Aussprache mit ö
durch den Reim gesichert ist (z. B. Sahn. I, 143, V.
251 — pöt^ röT — II, 962, V. 34 — pöyende^ jöyende
— III, 1096, V. 528 — pöi, jm, Vis und Rämin, S. 48,
^) Palez soll nach den persischen Original Wörterbüchern mehr
*Fruchtgarten' bedeuten; die obige Stelle, sowie Sahn. II, 765, Vers 5,
sprechen nicht dafür. Sahn. II, 626, Vers 1846, III, 1377, Vers 2047
sind zu allgemein.
```


### [2026-09-07T20:44:44.968Z] TOOL RESULT

```
=== PHD pāy/payg/payādag ===
312:débag [dyp’k! | N dēbā] brocade. débahr [dyp?hl | P dybhr] anger. pad — dāštan: banish. dég [dyk' | N ~] cauldron. LU) deh [M TA < A m? | M dyh, N ~] country, land; village. 0" гу -ģān [МТА-, dh? »'] = dahigàn. dën [dyn' | = M, N din] religion; cal. 24th day. dēnār [4ут/ | N dindr] (gold) dinar. dēn-āstawān [dyn’stwh’n'], dēn-burdār [dynbwit^l] believing, faithful. dénig [dyny&! | N dini] religious. dénódag [dynwtk'] female, milch. dér, dérand, v. dagr, dagrand. d��s(ag) [dys(k') | M dys] form, appearance. désidan, dēs- (dys-ytn! | M dys-yd] build. déw [SD Y.A < A #02, pl. šydy? | N ~] demon, devil. dēwān [d(p)ywn! | N <] archive, collected writings. déwanag [dyw”nk! | N ~a] demonic, mad. dēwār [dyw?l | M dyw’r, N ~] wall. déw|-ésnih [Š D Y Aysnyh | (M dyw?snyh)] idolatry, devil-worship. ~-ézagih [ŠD Y Ayckyh] = ~-ésnih. dēwēk [dywwk! | № déwuk] leech. dibir [dpy(w)r' | M dbyr, N ~] scribe. ~ih: writing, scribeship. „estān [-st?n! LN ~] school. did [TWB < A twb; dt'] again, then, further. didan, wén- [HZ Y TWN-tn! < A У hzy; dytn', wyn- | M dydn, wyn-, N —, bin-] see. ~išn: sight, seeing. ~i8nig : visible. didar [dyť] | N ~] sight; visible. pad ~ [N padidár] visible. didom [dtwm] second. dil [LB(B)ME < A lb(b)-h; dyl | = M, N ~] heart. dilér [dylywl, dlyl | N ~] brave. diz [KLYTA < A дур; dc | M dyz, N ~] fortress. dē [2, TLYN' < A tryn | M dw, N du] two. ~-ахмапіб [2 !hw)nyk!] relating to both worlds. ~ganag [dwk”nk! | M dwg'ng, N dugāna] double; twin. dok [dwk! | N ~] spindle. dol [del | N —] bucket; astr. Aquarius. dó|-pahikar [dwptkl | N du-paikar] astr. Gemini. ~-pay [2 LGLE, дора | N du-pà] biped, human being. dos [dws | N —] gum; plaster. dē-saxwan [2 shwn'] two-tongued, deceitful. dēsēn [dwsyn'] gummy; plastery; *glazed (pottery). dóst [dwst' | = M, N ~] friend.
494:nab [np | N nawa] grandson. nabānazdišt [nb”nzdšt! = Av. nabünazdista-] next of kin. паї [w | M mp] family. ~ag [-R! | N náf(a)] navel. !naft [npt! | = M, N ~] moist, damp; naphtha. *naft [npt'] descendant. nahang [жле] province. *nakkira [nkyl’y] denying, repudiating. ~yih: repudiation. nāl- [wl- | P (n’r-), N ~] groan, complain. nam [nm | N ~] moisture. nám [SM < A £m; m | = M, N ~] name, fame. namad [nmt' | N <) felt. námag [MGLTA < A melt: ттк! | M пто, N пата] book, letter. namak [nmk! | M nmyhk, N ~] salt. namāz [OSGDE < A sgdh; nm’c | = M, N ~] reverence, prostration, prayer. ~ burdan: pay homage. nām-burdār [л?т bwlt?l | N ~] heir, preserving the father's name. nāmčišt [?жт-, ŠMcst'], (pad) ~: in particular, especially. ~ig [-yk'] famous, well known.
536:pa(č)čēn [pcgn!] copy. *pa(č)čībāg [pcyp k', PWNe- | N *pajiw] *deceptive. ^h : deceit, hypocrisy. *pa(č)čībāy- [pcyp'd-, PWNc-] deceive. pad [PWN, for *pty | M pd, N pa] to, at, in, on. pad- [pt- | M *pd-) fall. padam [pd”m | (IN pandm)] mask for the mouth, worn by a celebrating priest. !Ipádan, pày- (UIN TLWN-tn! < А V ntr; Ptn, pd- | M pd, p’y-, N páyidan] protect, watch, defend. *pádan, pāy- [N TLWN-tn!, etc.] stand, wait. pādāšn [p?td?fn! | M p’d’syn, N pàdàs] reward, retribution. padēx [ptyhw'] flourishing, prosperous. ~ih: prosperity. padéxénidan, padéxén- [ptyhwyn-ytn'] make flourish, prosper. pādēz [p'tyc | M p'dyz, N pāyēz] autumn. pad-góhr [PW Ngwhl] т. jewelled; 2. of good stock, well-born. padifrah [p’tpl’s | M p'dypr?h, N *pādafrāh] punishment, retribution. padir-, ~išn, v. padiriftan. padirag [ptylk' | M pdyrg, N paóira] towards, against, counter-. (6) — madan: come to mect. ~ih: meeting, opposition.
545:pas-dānišnīh [4HLd’nsnyh] anti-knowledge. pasēmāl [psym’l, v. hamemal] defendant, accused. ~ih: (legal) defence. pasen [psyn! | N pasin] final, last. pasox [p’shw' | № ~] = passox. passand [psnd | N pasand] pleasure, liking. passandidan, passand- [psnd-ytn' | M psynd-, N pasandidan] like, approve. ~išn: liking, approval. ~isnig : likeable. passáxt [ps’ht'] test. passaxtan, passàz- [ps’hin', ps’c- | M ps?xt, ps’c-] fashion, prepare; insert; test. ~išn: preparation, constitution. passazag [psck! | M pscg] suitable, fitting. ~ih: suitability. passox [pshw! | M pswx, № pāsux) answer. past [pst' | N ~] low; astr. dejection. pašēmān [pšm?n! | = M, N ~] penitent, repentant. ~ih: penitence, repentance. pašm [psm | N ~] wool. ~ёп [-yn! | N ~in] woollen. pašn [psn'] bond, agreement. pāšnag [p’snk! | N ~a] heel. pāšom [p(”)$zvm) excellent. passing [pšng | N pišing] drop, exudation. paššinjag [pfnck! | N pišanja] drop. paššinjīdan, paššinj- [psnc-ytn' | N pišanjīdan) sprinkle. ~išn: sprinkling. pa&t(ag) [pšt(k)! | J pst] pact, bond, agreement. *pattān [pt’n'] noise, resonance. ~6mand [отта] resonant. pattāyistan [pi?dstn'] = pattüdan. pattüdan, pattày- [ptwtn', ptd- | P ptwdn, M pt’y-] stay, remain, last, endure. pattüg [ptwk'] enduring, patient, persevering. ^АҺһ: endurance, patience, perseverance. paxSag [phšk! | N pasa] mosquito, gnat. 1рау [pdy | N ~] foot; footstep, track. ~ 1: after. *pay [pdy | M pyy, N ~] sinew, tendon. pay [LGLE < А rglh; p'dy | M p'y, N —] foot, leg; foot (12 in.). 1,2 páy-, у, bL? pādan. payādaģ [pd’tk! | М py’dg, N piyada] on foot, foot-soldier, (chess) pawn. payag [p'd(y)k! | N paya] base, station. paydag [pyt?k! | M pyd'g, N payda] visible, obvious, revealed.
547:~th: visibility, appearance. paydagénidan, paydagén- [ ГОР hinin | M pyd'gynyd] reveal, explain. paydagihistan, paydagih- [py kyh-stn'] appear, be revealed, payg [pdh! | (P рар), N ~] foot-soldier, courier. *paygal [pyg'l | N payyāla, piyála] cup, goblet. -- gar [-A/] cup-maker. payģām [pgt”m! | M pyg’m, N pay(y)ām] message. ~bar LA | N -bar] messenger, apostle. paygos [p?tktvs | M p’ygws] district, province. paymān [pim”n! | M pym?n, N ~] measure, period; moderation; treaty. 6 — madan: reach maturity. ~ag [-k! | N ~a] period, measure, proportion. paymānīģ [ptm”nyk!] moderate. ~ih: moderation. *paymar [PK DWN < А pqdwn; p'tym'l] appointment, assignment. paymāy-, v. paymüdan. paymēģ [ptmwg | M pymwg] clothes, garment. paymóxtan, paymēz- [ptmwhtn!, ptmwe- | M pymwxt, bymwc-] don, wear. paymēūzan [ptmwen' | M pymwen] garment, dress. paymüdan, paymāy- [ptmwtn', ptm’d- | N ~] measure. *payram [p’tlm] the commonalty,-people. payrāstan, payrāy- [pt-, pyPstn!, pyPd- | M ругі, pyr!y-, N pērāstan) arrange, adorn. payrayag [руРак! | M pyr)yg, N pērāya] ornament, adornment. payrēģ [ptlwk'] light, brightness. paywand [ptwnd | (M руп), N ~] connection; offspring. paywand-, v. paywastan. paywasag [ptw’sk'] leather bag, wallet. paywastag [pteostk! | N ~a] continually. paywastan, paywand- [ptwstn!, ptwnd- М pywst, (pywyn-), N ~] join, connect. paywāz- [ptw’c- | M pyw’z-] answer, reply. ~ag [-k!], —i$n: response. paz-, v. poxtan. pāzand [p’cnd | N —] the Pahlavi commentaries on the scriptures (zand), transcribed in Avestan letters. pazd [pzd | — P] oppression, persecution. pazd- [pzd- | = M] blow, play (flute). pazdaģīh [pzdkyh] expulsion. pazdénidan, pazdén- [pzdyn-ytn' | P pzd-] frighten, chase. pāzen [p’c(y)n' | М pen, N pazan] ibex. pazüg [pzwk! | (N payūk, xabazdū)] guinea-worm. ~ í gühgard / gGhward: dung worm. pazzāftan [p> tn ' (M pzpt „intr.)] (cause to) ripen.
565:se-pay 75 spas
566:se-pay [3-p'd | N sipá] three-legged. sēr, v. Sagr. se-Sabag [3-spk!] three-night-long, trinoctial. seyom [зит | N ~] -third (in compound numerals). sëzd [s(y)zd | P syzd, (N séz/agi?)] might, tyranny; tyrannous. sézdah [sycdh | M syzdh, N ~] thirteen. sézdén [s(y)zdyn! | P syzdyn] mighty, tyrannous. si [sy] goose. sidig(ar) [styk', -kl | M sdyg, N sidigar] third. sih [30 | M syh, N si] thirty. ~om [-wm] thirtieth. sik [HLYA < А hP; sk | N ~] vinegar. sisimbar [sysymbl, -nbl | N sisambar] sisymbrium, wild-thyme. *Skandar [swkndl | N sikandar) = Aleksandar. snāh [sph] blow, strike, violence. sneh [snyh] sword. snéxr [snyhl] snow. snézag [snyck!] snow. snóy [snwd] (rain-, snow-)cloud. sófistà [swkpst’k'] sophist. 1s68 [swk'] use, profit, advantage. 25806 [swk!'] burning, combustion. 3806 [swk! | N só(y)] side, direction. sógand [swknd | M swgnd, N saugand] oath. ~ XWardan: take, swear an oath. sóhistan, sóh- [swh-stn'] touch, feel. ~iSn: feeling, sense. ~iSnig : feeling, sensitive. sēr [sz] salty. ~ag [-k!] salt (land). ѕӧзап [swsn! | N ~] lily. Só&yans [swkšydns = Av. saošyās] saviour (especially the final Saviour who will bring about the frašagird). sóxtan, sūz- [swhtn!, swe- | М swxt, swc-, N ~] burn. ~išn: burning, combustion. ~išnīg: burning, flaming. sūzāg [swo k! | М swe'gyn, N séza] burning. sózan [swen' | N ~] needle. spāh [sp’h | N sipah] army. ~bed [-pt! | N -bud] general, commander. spandān [spnd”x! | N sip~] mustard seed. Spandarmad [spndrmt'] N isfandármuó] Holy Thought, the fourth Amahraspand, earth goddess; cal. 12th month; sth day. spar [spl | M ‘spr, N sipar] shield. spar-, v. spurdan. spas [sp’s | M ?s-, “р>, N sipas] service, gratitude, thanks.
746:after fraz az, pas az, pay i.
811:apostle fréstag, paygambar; v. pro- phet. .
818:appointment pāymār.
998:biped dēpāy.
1215:chess Catrang; (pieces) K šah, Q frazén, B pil, Kt asp, R mādayār, P payādag.
1295:commonalty amaragān, pāyram.
1421:courier payg.
1461:cup paygal.
1462:cup-maker paygālgar.
1659:district awestàm, kust(ag), pāygēs, réstag, zand.
1993:foot pay, pay; on — payādag.
1994:foot-soldier payadag, payg.
2116:goblet jām(ag), paygal.
2297:homage, pay — namaz burdan.
2333:human being dēpāy, mardómzàdag.
2791:message paygām.
2792:vidi aštag, bayaspān, paygām-
3062:pay mizd.
3278:province awestám, nahang, pāygēs, réstag, šahrestān.
3301:quadruped čahārpāy.
4428:I pay (16 a.) — 12 in. ‘foot’
4431:1 gam i dē pay (80 a.) = s ft. ‘pace’
4606:. čahārpāy
```


## [2026-09-07T20:44:57.034Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== NYB p.147 (leaf 155) ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==156' NYB_vol2_glossary.txt | head -60"
}
```


## [2026-09-07T20:44:57.896Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SOD grep foot/heel ===\"\ngrep -n \"pδ\\|pδny\\|pdny\" SOD_pages.txt | head -20\necho \"=== SOD 'heel' ===\"\ngrep -n \"heel\" SOD_pages.txt | head -20"
}
```


### [2026-09-07T20:44:58.252Z] TOOL RESULT

```
=== NYB p.147 (leaf 155) ===
 Hell] 5324-26, cf s. v. aržan- tkénitan. — Paz. nigerīdan, nigaridan ; NP ntgarīdan, -istan. The spelling nkdl is attested by FrP 10. As the spelling -dl- regularly denotes -ér- we have to establish
140
nipart
the pronunciation nikér- < *ni-karyati (of the same type as the syn. spas-: spasyeiti ‘he espies, finds out’, cf also Skr pasyati), which also accounts for Paz. NP nigar-, niger-, ci men(itan) < *manyati: Paz. manidan, minidan. Hübschmann, PSt. 102, no. 1038, nikir- < *nikriya- (better *nikrya-), accepted by Bthl; I disagree. - Arm. lw. *nkirt- (< *ni-kirt-) in nkrt-em ‘to strive for, to care for’ in the N. T., Ep. ad Philipp. 31%. — To be combined with 2kartan; cf also Skr kal- ‘to observe, to mean, to consider’.
nikéxtan [nkyhtn'] nikéc- [nkyc-] to dis- close, to expose, to expound Religion and religious matters 60%. — V. also nikecišn. — Paz. nagežidan. Inf. nikéxtan DkM 821}.
niküneh [nkwnyh] downwards: pat ~ emphasizing the prev. frot 5123. 5245. — NP nigün, nigü(n)sür; MPrth ngws’r (S, MHC), cf Arm. Iw. nkun ‘defeated, con- temptible’. Cf pasčh, pēšē (v.s. v. peš), uléh.
nimāyišnihā [nm’dänyh’] adv. of the v. n. nimäyisn (from the next w.): gētē handācak ~-c ... spurrik perfect as far as measured by earthly measure 110°; v. handäcak.
nimütan [nmwtn'] nimay- [nm?d-], pres. 3d p. sg. nm'dt', inser. nm?dty, both = nimáyét, 3d. p. pl. nm’dynd = nimdyénd, to show, to denote, to signify, to indicate 512, 810 etc.; to teach 81!!; — a syn. of kartan : patifras ~ 10112; handácak ~, v. the preceding w.; bahrak ~ to allot a share 1152-35, — < ni + Av. OP (1165) mäy-, cf framütan; MPrth nm?dn nm’y-; MPrs nmwdn nm?y; Paz. NP namudan; Verbum 203.
nimūtārēh abstr. v. n. of the preceding vb.: indication, act of establishing 45%; manifestation 71°; teaching 11220,
nipart [nplt'] quarrel, combat 703. 1075. — MPrth pt. nbrd’d ‘to combat’, Ghilain 53; Paz. naward; NP nabard.
www.parsianjoman.org | ool wok
nipartak
nipartak [npltk'] brave, excellent 316, 16", — NP nabardah ‘warlike, brave’, navard ‘worthy, excellent’.
nipast [npst'] place where a thing is deposited, depository, gl. of KLYT’ = gellāitā (v. Ideograms) 107%, — I reject the interpretation of the passage given by Bailey, ZP 152. There is no evidence what- ever of an ideogr. KLYT = QRYT’ being used for diz ‘fortress’. This Aram. w. always signifies ‘village’; in the FrP, ch. 2, it is hidden behind the somewaht be- wildering disguise MRDYN! (-DYN- common. error for -YT-) for MRYT" for QRYT* (cf MDM for QDM) = rētastak (g. v.) A form *ntptst for nipist is no- where attested, so the diz i nipist has to disappear from our context. KLYT? = Aram gellāitā (ultimately from lat. cella) refers obviously in KnS VI, 11 to the sanctuary of the Dragon of Kirman, most probably a cavern. — I deeply deplore the Ahrimanic slip of pen which made me write ntpāst, instead of nipast, as the equivalent of KLYT’ in the Index, I, 160a, 14. A benevolent critic will find the correct reading nipast in I, 157a, 30. - From nipastan; nipast is to nipas
```


### [2026-09-07T20:44:58.330Z] TOOL RESULT

```
=== SOD grep foot/heel ===
=== SOD 'heel' ===
3768:                                                                   121-123. Sir Mortimer Wheeler". JRAS, 1970, pp.
12761: 3168 cpt- B                                              jjbi>           wheel, circle
12821:3179 cynrVk ? B =» cyzr'w'k                                              wheel
13225:     wheel                                                            synagogue
23290:                                                                     heel, kick
25302:                                                                   heel
28938:                                                                     wheel
31910:     chariot, wheel(Mahayana)
38527:heel 6820, 7509                       Hindu priest         8505               house     3540, 4063, 4935, 4943,
39845:Vishparkar      10515                   water-buffalo      204                  wheel   3180, 3192, 3313, 8752,
39847:   10409, 10411, 10413, 10525           waterfalls    284                       wheel of the law    3595
```


## [2026-09-07T20:45:04.719Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== NYB leaf 163 ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==164' NYB_vol2_glossary.txt | head -40"
}
```


### [2026-09-07T20:45:05.960Z] TOOL RESULT

```
=== NYB leaf 163 ===
pa0ana-; NP pahn "wide, large’ ; v. also pahnāt.
päh-ast [p'hst'] sheepfold 9411-14, — < päh + ast < Av. (212) asta- ‘home, abode’, cf Av. (881) pasus.hasta- ‘sheep- fold’ for *pasu-Sasta- from had- ‘to sit’ (v. nisastan).
Pahlécak [phlyck'] n. pr. of a man of the Tūrs 114". — Thus Cat. 53; it may also be read Pālēcak, Pārēcak.
pahlom [p’hlwm, inser. p'lswmy], pāšom [p’swm] 1. noble, elevated, exalted, fore- most: Sühpuhr ... martan ~ foremost among man 15!? = P2:5 (p’lswmy). — 2. sublime, blessed, paradisiae, of Garod- màn and the heavenly world 3115. 325 [p'šwm]. 8916; of those bringing about the fraškart 105%. 1067! [p’swm]; ~ dēstēh i 6 yazdčin blessed friendship with the gods 5511; of ahläyeh 598; sup. ~-tom apazär i crat the most sublime power of Wisdom 89?" (~-tar Mx 151), — Not to be combined with fratom (g. v.) From *pardama-, orig. ‘Parthian’, an adj. derived from Par0a(va)- (Gr IIdp0ot) in the same way as Av. (710) dahyuma- from dahyu- and (1661) zantuma- from zantu-, cf also (1566) the name of the people Sairima-. In Achaemenian time there are proper names such as (in Bab. cuneiform) Par-ta- a- ma, Pa-ar-ta-am-mu (Holma, NKt 35 n. 1, after Tallqvist) Hence in the Bible, with the Hebr. pl. ending, partemim ‘the nobles’ at the Babylonian and Per- sian (historically: the Parthian) court: Esth. 13. 6%. Dan. 13. Parthians constitu- ting the highest social class in Parthian-
dominated Iran, *pardama- assumed the
148
pahrčxtan
sense of ‘the highest, the most elevated’ in general, still surviving in pahlavān ‘heroes’, pahlavānī ‘heroic’ in the epic. — Paz. pahalim, pahlum etc., Skr. v. atah- para, atyuttama. FrP, Cod.P fol. 11° p’hlwm: Paz. phälum with the gl. (NP) pšm: yani bihišt. Cf. s. v. Mahlah.
pahlomčh sublimity, heavenly nature: yazdàn = 5514,
pahlük [p'hlwk'] rib, ribs = the chest 5421, — OP "par0u-, Av. (877) parasu-, porosu-; NP pahlu.
pahnäi [p’hn’y] breadth, width 381°. 925.9 ete. passim. — Abstr. of pahan; SM l. 42 phn’y; NP pahna; Bal pahnäd ‘side, di- réction’.
pahr [p’hl] guard, frontier guard 11412. — Cf Av. (887) padra-vant-; MPrth p’hr; p'hr-byr ‘commander of the guard’ (A- H I; phrbd ‘guardian’ A-H III); NP pahr, pahrah ‘night watch’ — all NW
forms, as against SW pds (g.v.). — V.
Virči-pahr.
pahrée [p’hlyc'] preservation, protection, guard 2611, 291, 12118; ~ kartan to take care of, to cherish 31%, with hac: to preserve from 852-3; rah 61... bim u ~ hac dósax" the way to fear of, and guard from, Hell 8119-11; han i vas- ~ jan well- protected animal spirit (physical life) 553, — From pahrextan.
pahréc-karéh [—-k'lyh] power to give protection 5223,
pahrčxtan [p'hlyhtn'] pahréc- to protect, to take care of^20*; imp. restrain thy- self (be indulgent)! 35°; «"e£, x%és-tan, or alone, ~ hac to be on his guard against, abstain from 6674. 717-12, 8422.26, 851. — Ps. phlysty ‘protected’; MPrs phrystn phryz- ‘to protect, to preserve; to abstain’; NP parhéxtan parhézidan par- héz- ‘to restrain oneself; to take heed’, parhéz ‘abstinence’. Bailey, BSOS VII, 1935, 762 sqq.; Verbum 214 sq. and BBB,
www.parsianjoman.org | oe zl wb
pahréxtan
Gl. s.v. pahristan; Schaeder, UJ XV, 1936, 579 sqq. — Paz. paharčatan paharēž-.
pahréxtar n. actoris of the preceding vb.: hac... ~ bäs! keep away from! 6976.
pairästak [pdl'stk'] ready-made 6°. — Arm lw. patrast; NP vb. patrāstan patrāy-; <
```


## [2026-09-07T20:45:06.016Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '23285,23295p;25296,25308p' SOD_pages.txt\necho \"=== entries 6820 / 7509 ===\"\ngrep -n \"^ *6820\\|^ *7509\\| 6820 \\| 7509 \" SOD_pages.txt | head"
}
```


### [2026-09-07T20:45:06.556Z] TOOL RESULT

```
6806 pdfnq     C                           (J^ai^-ux-u^
                                                                6819 p6ny *» pSn'y
      pa8fang ? ©<*pad-*0anga ?
      jointG?/ ankle or wrist)                                  6820 pdn(y) C                                     j&m^U
      C2, 17R1 n p58                                                 pa8n, pa8an ©<pad-         ©ace. pdnw
                                                                     heel, kick
6807 p5k} M                         tsjlza <cl* <djfc                S W, C2, 94V14 pl76-7; Benv. pznw
     paSka ©f. n. =»pdq\ p5kh, p^k2
     law, tradition, judgement                                  6821 pSnyh =» p8nh

      BBB b3 d5 f59, 746-, GMS 1635; Hen. Tales.                6822 -p6r =* -py8r>k
       GMS 600; perf. psYt&r-, BBB 531                             pasan    ©loc. psny\ ace. psnw   =^psyn-, }psn
7497 psrty C                                         <sj&
                                                                   S W apud. Mack. AI 25, 428 n 16; C2 p51 n 5
     pasayde ©pp.
       spilled                                                7509 psn' M, C                                         -uil
       STi 81.14; BSTi 346                                         pasna ©<Av. pasna ©f. ace.
                                                                   heel
7498 psqV C                             <*^i<>rj-
                                                                   BSTii: C2, 51V13 n p98; Bailey. Prolexis. 183;
     paskar =#pskr-
                                                                                                                       302


=== entries 6820 / 7509 ===
23288:      jointG?/ ankle or wrist)                                  6820 pdn(y) C                                     j&m^U
25300:       spilled                                                7509 psn' M, C                                         -uil
38527:heel 6820, 7509                       Hindu priest         8505               house     3540, 4063, 4935, 4943,
38676:John  11050                             kick 6820                              knowing conflicts       2078
```


## [2026-09-07T20:45:21.030Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"payk\\|patyātak\\|payātak\\|patātak\\|piyāda\\|pēk \" NYB_vol2_glossary.txt | head -20\necho \"=== leaf 162 ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==163' NYB_vol2_glossary.txt | head -30"
}
```


### [2026-09-07T20:45:22.230Z] TOOL RESULT

```
2225:karp [klp'], cas. obl. karpēk [klpyh] 95**, the external, visible form of living be- ings: der-pattäi ... ~ dārēnd they will have their external form everlasting (= an everlasting bodily form) 10515; — as the second element of a compound: mdtak ~ having female shape 5717; pat kanik ~ in the shape of a maiden 731; 6 martom karpéh into human shape 9526; mart ~~, martë [GBR? 4-1] ~ 104%; 9621, 9819; 6 hàn 4 uštur ~ 9915, — Av. (467 sq.) kahrp-; Arm. lw. kerp; MPrs kyrb (A-H I), but Paz. karf.
2749:nipēk [npyk'] document, codex, book, pl. ~-ihā 108°. 1097. 1112-917. 1128. — < *ni-paya-ka- ‘that which is kept, or is to be kept, in safe custody’, ‘record’, originally an administrative term; MPrth Prs nbyg; Paz. nevé, nivé. From Av. (886) ni-pãy- (pres. also pay-). — Bthl’s ety- mology: nipčk < "nipčhak < *ni-paida- ka- from a SW form of nipištan (MirM IV, 30, n. 2) is untenable.
7332:piyādah: padātak
=== leaf 162 ===
hunuskan ozatak gurg a bitch wolf whose cubs had been killed 4927; hunuskän özatak dit saw the cubs killed 50!; — v. n. dzanisn 1. pred. : be ozanišn is to be killed 108; 2. as a subst. : kārēcār u ozanišn 134; pat ozanišn āivēnak 1032, v. divénak. — Av. (491) ava-gan-, pres. -jan-, pt. -jata-; MPrth
www.parsianjoman.org ool ws 2
Ozatan
147 pad
^wjdn "wjn- (MHC); MPrs 'wzdn "wzn-; Paz. awazadan awazan-. V. also janišn, ganäk and apa-Zand.
özmütan [’wzmwtn'] to try, to test 1185. — Pres. özmäy-; özmäyisn [”wzm'dšn'] Vd. 5% comm. From Av. (1165) mäy- ‘to measure’ = OP; < *aviš-māy-, whence *aviž-māy- > *aviz-mäy- with ž > z according to the general phonetic rule in SW. Hence with different contractions l. ēzmāy = BP, 2. či(v)zmdiy- = Ps.
’cmwty = dzmut, NP āzmūdan āzmāy-; |
-p, -pi [-py] (Prth) emphasizing part.: LHw-p = hē-p to him HajA:14; "MT- S-p = kaš-ip, v. "kaš; apar-p-im ravišn I must climb up 40%; (ZK-p =) an-ip tē armēšt daxšak-ip früc venend 5113-14 (v.s. v. an and tē); ZK-py 51: as -p(?) is purely Prth we have to assume the Prth. equivalent of ZK: et-- p? (Henning,
Iranistik 78 n. 3); niin-ip 539; be-p 5374.
— 'The enclitie form of api, v. ap-; the NW equivalent of SW -c(2) < -cit: MPrth ’wh-wb < *öh-up ‘just so’ (A-H III); ’gwb < *hak-up, the equivalent of SW hakar-ic; mrdwb mrd'n ?frdwm Sh yy ‘thou art the Man, the most exalted of men, the King’, Sogd. 297°. 30.
pacén [pcyn'] copy 108:6. 10912. 11022. 1111122, 1121. — Arm. lw. pacén, pačean, pačik ; Hebr. lw. patšægæn Esth. 34 etc. < *patšagn < *pati-cagn- < Olr *paticag- niya- (Syr, J.-Ar. paršagnā with inorganic -r- < -t-), v. Benveniste, JA 225, 1934, 180-185.
pid (pa) [pd; LGLH; Prth NGRYN] foot, with the indef. art. —-ē [LGLH +1) 18", 241° ete. passim; HajA:6.11 (Prth); HajB:6.12 (LGLH). - Av. (842) päd-; MPrth p'd; MPrs p’y; Paz. pdé, pah; NP pā(y).
padak [pdk'] step, tread, (a horse’s) run: nev [IB] —-än animals of valiant run,
BP äzmäyisn (g.v.). The inf. and pt. have followed the analogy of nimütan framütan for *nimätan framätan.
Ož [’wc'] force, power 55%. 9415; vas-~ mighty 96%. — Av. (39 sq.) aojah-; Paz. aoj.
ožčh in mas-~ the quality of having great power 89’, abstr. of the compound mas-ož having great power, Paz. meh- aoja, Skr. v. mahabala (ŠGV).
özömand [’we’wmnd] mighty 974,
P
pl. cas. obl, app. of aspän 19°. — Av. (842) Ipaöda-; MPrth pdg = MPrs pyg; NP paik ‘walking runner, messenger’ ; Arm. lw. payik ‘footman, guardian’; Syr. lw. paigā id.; Sogd. 2527.26. V. also pada- tak and pade.
pidak [p'dk'] station, sphere of the celestial bodies 522. 932-9. 104°. — Also p’hk' = pähak. — Av. (887) páóa-; Paz. päya (Mx); NP päyah.
paditak [pd’tk'] footsoldier; pawn in chess 11912. — MPrs py’dg Sogd 2574. 26; NP piyädah; Skr. lw. padäti(ka)-.
padé [pd+1] adv.; ~ i prep. on the tracks of, on the heels of 71%. — An ad- verbial formation, on the pattern of fräceh, pasēh, pēšēh, ulēh etc., from pad-, the weak st. of pdd- (v.s. v. pad), cf OP Loc. ni-padiy adv. ‘in pursuit’, prep. with acc. ‘in pursuit of’; Bal p'adā ‘after, behind’ (Gilbertson and Longworth Da- mes; pada Mockler); NP pai id. (pa? also ‘footstep, track’ < the same päd-, or < pada-, v. s.v. padak). [The normal Ir. equivalent of Aram ’KBY’ ‘heel’, FrP 10, was doubtlessly identical with NP pai, but there are variants pointing to the ws. signifying ‘grease, fat’: paé (cf SGV V, 58. VI, 14). pč, pih; in fact, ‘heel’ is in Bal pô, not to be separated
from pih].
www .parsianjoman.org | ool ak,
10"
Paétrip
Paétrip [Paz.] one of Zartuxst’s fore- fathers 4626,
pah [p’h] cattle in general, but particu- larly small cattle: asp sardärän u ~ sardaran 4418; ~ 4 gdspanddn flock of sheep 9724; sheep's wool 47%. — < OP *pa0u-, SW form of Av. (879) pasu-.
pahan [p'hn'] broad, sup. ~-tom 96°. — Av. (843)
```


## [2026-09-07T20:45:22.465Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor i,p in enumerate(t):\n    if '6820' in p or ' p6 ' in p:\n        print('leaf',i, 'tail:', p.strip()[-80:].replace('\\n',' | '))\nEOF"
}
```


### [2026-09-07T20:45:23.779Z] TOOL RESULT

```
leaf 339 tail:    yazd   ©ob. -yh |                                                           L^U
leaf 558 tail:                     hireling      5418                      housemate    310,311
leaf 561 tail:                  king of splendour   2105                lain down    6027, 6039
```


## [2026-09-07T20:45:37.385Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (335,336,337):\n    print('='*10,'leaf',i,'p.',i-66)\n    print(t[i][:1800])\nEOF"
}
```


### [2026-09-07T20:45:38.700Z] TOOL RESULT

```
========== leaf 335 p. 269
                                                                                                                            1
26?
                                                                                                                 pcxyz-
      GMS 412; BSTii 893.10, 849.13; C2, 31V10,                      MSP; inf. pcxsyy, GMS 910
        12R13, 104V16                                        6712 pcxt-       C                             j&J \tf*j>$*t

6702 pcwqyrny     C                                   y*j          pacayd (ptcxt-) ©pt. st. =#pcxs-, pcyd'r-,
                                                                     pcyt>r-, ptcyt-, pcyt-
      pacukerne   ©ob. pi. -ty ^pckwym'y                           (to)receive, 0<?)take
      fearful
                                                                   GMS 56, 509, 551
      BSTii: C2, 12V15

6703 pcwst- B                        0>jf~j> <0>J> >jj^^>    6713 pcxtY- =* pcyd'r-
     pacwast ©pt. st. =»pcwz-                 *s>            6714 pcxw'k M                                            ^U
     (fo)meet                                                      pacxwak ^pcwyw'k, pcyw*k
                                                                   obstacle
     Frag. 2a.25
6704 pcwstk B                                                      BBB 505.2, 726; GMS 98a, pcxw'kK KG 496
                                           * (5J^ * ^~*
     pacwaste ©pp.                                           6715 pcxw'q =* pcxw'k
      caught by illness ?                                    6716 pcxw'kCk) =* pcxw'k
      TSP105.110
                                                             6717 pcxw'y-     M, C             CfAkJk'&J'iSjfj'r
6705 pcwstw       B                    u^Iw^La      <,yU7l        p
========== leaf 336 p. 270
                                                                                                                  270



pcxyz^nty

      GMS 623; Gersh. BSOAS 14.490
                                                              6738 pcykwyr =» pc'ykwyr-
6727 pcxyz'mnty C              0^ j>f j <0-> j >' j J*- j*    6739 pcynyq C                                       ^j^
     pacxezamande ^pcy'yz-, pcyst-, pcyst'ny                       pacaynik, pacenik
     kneeling                                                      suitable
      C2, 56V26                                                    BSTii 892.20; Benv. JA 1955, 301; C2, 31R20
6728 pcy C                                              *^    6740 pcyp'qc C                         jte*\<J>fj~
      pacay ? ^pcy'y-, pc>y                                        pacyapakc ? ©*pati+ydfi-
                                                                   confusion
      profit
      C2, 27R8, pc>y, 55V28                                        STii 3.53; GMS 1002, y>fr Gersh. Sogd. Cpds.
                                                                     1945, 141
6729 pcy^y B, S                     ^SiS a^ ^^Ay
     pacyay ? ^pcy'y                                          6741 pcysty     C                                  *^T
     success, profit, help                                         paciste ©<pati-cista
     BSTBL, Vim. 125; Dhy. 230; TSP 3, 103; KG 546,                learned
       568                                                         STii 1.2

6730 pcy*y- B, M                    0\#w^» <u->_*c~* >>       6742 pcywfs- S                   o^o££*io>J'j~z
     pacyay (pcyy'y-) ©<*pati-ay ^pc'y-, pcy                       pacyufs ©intrans. v. =#pcywfs-
     0o)be right, (rc)fit                              
========== leaf 337 p. 271
271
                                                                                                                    pd>ty
      foot, step                                                   Benv. TSP 2.1163, 3sg. pres. pd}rfit
      BBB 489; paddw, Hen. BSOAS 11, 68.22; GMS              6761 pd'rnqy' C                    (*jjJj^ <&[*-) ^Sclu
        506
                                                                   ^pyS'rnqy*
6750 p8»k B                                   ?u^<?:*              providence
     pa8ak ?, pa5ak? =>p5kw(w)                                     STii 3.20; S W, C2 p86.21; Sund. AoFiii 1975,
                                                                     18V3
     large, wide
      TSP 8.107; "banner", Hen. Cosm. p3l6, pala =           6762 pdVny        C                     juu-l taxjj^ ^l^-
                                                                   pa8arne ©pi. -t ^pSS'rny
                                                                   keeper, sustaining, bishop
         pr>kpS-1
6751 p5> -♦
                                                                   Benv. JA 1955, 331.26; C2 14R21, 55V18, 48R21,
6752 pS'yt- M                                d-^
                                                                     54R24 p86.21
     paOayd ©<*pati-&axta ©pt. sL; pres. pdync-
       ->p58*Yty                                             6763 pd'rty C                            lay** <*xi. ^ jU$&
                                                                  paSarte ©pp.
      (fo)pull
      GMS 600, 8J0                                                 sustained
                                                                   BSTii 903.13: C2, 57R13 p86.21
6753 p6'k B                                   ^j^<^
     paSe ^
```


## [2026-09-07T20:45:46.128Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(t[336][-1200:])\nprint(\"@@@@@@@@ 337 head\")\nprint(t[337][:900])\nEOF"
}
```


### [2026-09-07T20:45:47.552Z] TOOL RESULT

```
ciyarP ©impf. =»pcyrP-                                      GMS 623
     (to)accept, OcOperceive
     TSP 5.71, 87                                             6747 pcyy'y- M =$ pcy'y-
                                                              6748 p5- S                              •jjoly*
6736 pcyyyz- B                                   u^jylj
     pacixez ©impf. =^pcyxyz-, pcy*yz-                             pa5 (p8\ -p5w, -p5y) ©nom. gen. -y; ace. >\Je-
                                                                                                            -w
     OcOkneel                                                       =*-p5>k
     VJ 97 etc.; TSP 6.83, 7.21; GMS 623; Frag. Len.               family, race, kin
                                                                   MSP p49 bll2; Sund. IMTT 1992, 79. 12n 54,
6737 pcyqs- C                             *     ^bjlioxjl            STSC 49; MDii p41.5; Frag. Len. 81.5, 77R6
     pacikas ©impf. =#pcks-
     (/<?)expect                                              6749 pS-1 M,S                       (^dk-f^'k
     STi 39.3; Sund. AoFiii 78                                     pa8 (p85) ©ace. -w; ob. -y =*p5-y, p>8

@@@@@@@@ 337 head
271
                                                                                                                    pd>ty
      foot, step                                                   Benv. TSP 2.1163, 3sg. pres. pd}rfit
      BBB 489; paddw, Hen. BSOAS 11, 68.22; GMS              6761 pd'rnqy' C                    (*jjJj^ <&[*-) ^Sclu
        506
                                                                   ^pyS'rnqy*
6750 p8»k B                                   ?u^<?:*              providence
     pa8ak ?, pa5ak? =>p5kw(w)                                     STii 3.20; S W, C2 p86.21; Sund. AoFiii 1975,
                                                                     18V3
     large, wide
      TSP 8.107; "banner", Hen. Cosm. p3l6, pala =           6762 pdVny        C                     juu-l taxjj^ ^l^-
```


## [2026-09-07T20:45:48.156Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== Henning SLW: Sogdian loan-words in New Persian ===\"\ngrep -n \"pal\\b\\|'heel'\\|paðnē\\|paSne\" HENNING_selected_papers.txt | head -20\necho \"=== grep Sogdian Loan-Words title ===\"\ngrep -n \"Sogdian Loan-Words\" HENNING_selected_papers.txt | head"
}
```


### [2026-09-07T20:45:48.227Z] TOOL RESULT

```
=== Henning SLW: Sogdian loan-words in New Persian ===
1553:# Normally d°ykn- is " pal favourite with Manichesane, ef. eg. Hom. Poalm-hook, register 4.x. wapepBok4. Tuck. or 2 npl'ynty = Bed pl. opt. (parabolic optative 5 “al(0) above, 1?
4652:fa fitting description. The literal meaning of » presumably “ the principal battalion"). médiyn “essential, basic, core, capital” (frequent in the Dinkard ; Zachner, BSOS., ix, 305, 306%, 309%, otc., rightly translates “‘ chiefly") should be kept distinot from madiyin ** book” (of. Nyberg, Mazi. Kal., 58), originally “ com- ‘memorabilia, memoriae’” as Bartholomae, Mir. Mund., ¥, 16 8q.,
5376:(Brg. b, first page) (134) Jm ‘yf (135){gwnlg gwng (en)g [.]-cyd 00 ky pal (136) Jb ‘wa wy 00 ‘gr i 88)[oo e]'wn o'r kw ny myryb 00 xw'r(199)('wd] b'r pwr kwnynd oo 'wi"'n (140){ . . . Je pymweyd oo ‘yn nab (141) 00 "wd ny hwstyg'n oo (143) "w)é bwn ny hwstyg’n (143) Payhyd oo ef"wn] (144)]e "st (Fry. 5, second page) (145)].yn we (146) {as'Jh bat 00 (pd) ‘stg ply](147)[pyt re) o0 “wd erm oo wd “nfdr}(148) ‘wyrd 00 "(y}g dr'yd 00 "br y(2\[d)(149) r'stygr oo hwrxiyd ‘wd m'{b] (180) dw ty 'w dst dd oo "be mbr{'spnd151) dixt'n "wa d’m'n 0 "y(g) [zew'n #) (182) by oo pd "w'm "{w'm|(153) prystyd oo dyt{yl ardrwit] (14) [b]wt oo méyfh’ (155) peya{tl(a)('n
5394:(Fry. f, frat page) (ITA)jny{(17)}wst{(178) Js swd 00 (c)wn wraygte] (ITA) ky t|(x)m q'ryd 00 pad wal... 178) Jd 00 nywi'g ky d'nyyén(179) Jeynd oo e'wn myrd ky prwig (180))(yiyr "bgnd oo hwstyg'n bwd(I81)] ny ‘0 bhr ‘y wnywayy (182)) (a}xwst gr'n oo o'wn(183)]([.}t'n oo nxwst (184) tw pdlyxir r{yd)(185))t’byy (Fry. J, second page) (186)]yp{ (187) Jwys{p(188)] wh (c)w(c) 00 nywi’g [ky(189)(rw'n]g’n dyyd oo wn ‘s(kwh] (190) myrd key dwxt 'w 3°h hn(A){ym’n|(191) qwnyd oo 'w wzrg pdyxir r(s)[yd](192)00 rw'ng’n pal taw'r ‘y 'r{d'w] (198)00 "wn p'k by oo o'fwn (194) ky pd 'dwr wd wd o0f(198) j'mg “y hwelyhe “yg?)(196) [p]d tn 'y yw(jdhr (197) wrdyl
6071:Srge'dg g'wa'dg pal mrg 00 ‘wd (34) rwb's ‘yw pd byd ‘ng’? (85) (wed ‘pyd Thynd 00] 00 "w'gwn (36) (hw 'dwr warg 'w] hrw dw (){d(w}e 00
14216:Arm. post 42 Georg, pantunfi €2-3 Sen: papal Dai
14955:(water, air, in we earth. Aceonling tothe Manichasans thy their pn our earth, a mpass the universe and 30 have their roof of the worll. ‘They had to be protected against the Po and therefore were enveloped in the five d=Agnara, These bviously accompanied the Garments from their emplacement in the “third earth ” to the top of the world ; it is thas ate that they should be mentioned as the first thing created in the Mixed World. With the dwsjuara we would identify also the maikbe “ mattresses” or “beds ", named by ‘Theodor bar Qonai in ¢ Garments, in a troublesome passage (Pognon, 129, 6; of. Cumont, i, 31 45; Jackson, 240), At any rate, Sogdian fasp Hence, froin Av. fraspal Yt. 15, 2, betwee throne, couch” and upastrona- “ spread, rug", of, Pers. farasp *
15022:P 8, 107, of a pB"k = palé, else wheel ” is mentioned in the Paalo-b Splenditenens (cf. ibid., 198, 98, " the Rez h of Light”); it is doubtful whether ’skyeyg ezr- ‘superior wheel " (Lit, “hi lying whe tet (the parallel passage qu against it). Now, if it is o
15366:(22) "YMTW MN cnt(ey «'r 1 pal (23) Bew'n 't kmay(n) ® priaaw) pet'hi
16284:ently chosen at random from the middle of a sentence may strike 1s as ‘The procedure commonly adopted for Papal Bulls would have been unsuitable for Asoka’s Edicts ; their opening words are far too
16880:1845, Vol. i, 351 5qq. De Bode’s report attracted little attention. It is true, the reliefs were briefly mentioned in handbooks; thus by Spiegel in his Evdnische Alter- Vol, iti (1878), p. 820 (the name misspelt as Teng-i-Salek); in an annotation in the Grundrits der Iranischen Philologie, Vol. ii (1896-1904), p. 486, m. §, where the astonishing assertion® is made that Tenk-i Saulek (sic) is ohne Zeeifel identical with the Seleucia /Soloke ‘of Strabo, xvi, 1, 18, p. 744; but the inscriptions fell altogether into oblivion. Although the reliefs obviously belong to Parthian times, indeed constitute the principal series of Parthian rock-sculptures, even so well-informed a scholar as E, Herafeld could write “there are no other Arsacid sculptures [than those at Mount Bisutiin] of any importance known in Iran" (Archaeo- logical History of Iran, 1935, p. $7); similarly K. Erdmann, Die Kunst Irons ur Zeit der Sasaniden, Berlin 1943, p. 46. R. Ghirshman, in his discussion
17061:AWa. Court assembly in the throne room. Stein, Fig. 33. Our plate xii All nine figures (except possibly No. 9, counting from the observer's left) are bare-headed; their hairdress resembles that of the satrap on the stele of Khwisak (except for No. 8 whose hair falls down to the shoulders). ‘The two principal figures, Nos. 1 and 8, are seated on elaborate throne-chairs, with steps, foot-stools, arm-rests, and high backs with elliptic projections (which may be responsible for Stein's suggestion that No. 1 was diademed); they wear long, transparent (silken?) robes. Figures Nos. 1,8, and g hold staves in their right hands,
18055:‘The principal difference is that Herafeld read K in two places where I read D, tnd on these letters hangs tho fate of both the Khagan and the Aq-Agatardn Now, the letters K and D resemble each other in a general way ; both consist of two crescents (open to the left), a smaller one on top of a larger, but XX has in addition a short horizontal stroke at the bottom. Whenever there is doubt about the presence or absence of the horizontal stroke (as is apt to happen particularly often in the Inst lines of blocks where the letters reach down to the edge of the stone), it becomes dificult to distinguish them ; there are other points of difference (e.g. the lower crescent of D is more rounded and ita lower horn is continued further to the left; the axis of K is vertical with w slight inclination to the left, while that of D is inclined to the right), but the reliance on them.
18430:Jong sentence, in which all the principal supporters of Narseh were enumerated ; the critical passage comes near its end
18502:‘ Suchas, Die Chonit tom Arta, pl, dented Bé@ Nightde with Qu fnadmimible, He rolled cn 0. Hofimunn's etymology F (Mariyrratien, 41, se of Hoffman's etymology (which ital is Altrnetive en00gh) a je Sachau' entiation; for Ifthe Crook name [ersisted up to Muslim times, coe woul expect to fied it being ued in earlier centri, and not 1 Syrie tranlation of i, The principal ejection, however, la that BA@ Nightle ly in BA¢ ‘Carma, while Qutrabbul (the ditt Snmediataly tothe NW of Baghdad, cn the western bank
18526:1 J, Reval and 8, Kiya, Ovsirid-i nawiteha wt peibarhayi Kali angi ( Kade No, 14). Tehran, Isfandirmadh-mih 1320 Yeed, (= Feb-March, 1152) Here quoted as Report "Year § No.4, Tir, 1811 [= June-July, 195: Only the principal ‘drawing and inscription had attracted Dr, Frye's notice * Year 8, No. 6, Subrivar, 1331 [= Avg.-Sopt, 1952), p. 38. No. 9, Adar, 1831 [= Nor.-Dee, 1952), pp. 538 rn and, with the meaning of darre valley "CE, Ivaniow," Rustic Pootry inthe Dis horasan (U.and Proc. Aa. Soe, Bengal, NS. x1), 1025 bal a riverbed, wid rllah  ; sce Vullers a. bil 6—As the brief wowels of place-namos are not given in the Report, the correct pronunciation of Jenga is neceamrily uncertain. Useful information on the grography and history of this region ix contained in W. Ivanow’s article,“ Persian at spoken in Birjand " (J. end Pree, Ax. Soe. Renal, N&. xxiv, 1028, No. 4), pp. 236-246 On the origin of this mame (Xsif/d from Xwnyp) see Markwart, Welrof und rang, p. 20, 0.2 ‘The forms with fnal st are doe to disimilation, ef. the reverne ‘ange from -t to 1p (se Trans. Phil. 8 1, m.2).
19066:'D yad’n bays'l, which is idiomatic Pahlavi, means “until/so long as God (is) the helper”. The principal “‘act of iniquity and falsehood” apprehended by Mihr-Narsch is presumably the unlawful levying of a toll. The whole concluding sentence, although formally a statement, is nevertheless a wish or hope in meaning,
19616:Our! knowledge of the Khwarezmian language depends largely on two classes of material, which are dissimilar in character but supplement each other. On the one hand, we have the sentences in legal books, chief among them the Qunyatu *IMunyah; on the other, the Khwarezmian glosses in the Mugaddimatu *1Adab, the principal MS. of which was published in facsimile by Zeki Velidi Togan three years ago.*
20446:Tt is not possible to discuss here all the problems connected with the verb of this dialect. The following table contains the principal forms of the preterite and the perfect
20916:After studying Freyman’s latest article (here quoted as SV. vi) one realizes, not without surprise, that there has been no advance over the inevitably incomplete and in many points faulty statements in my part of the Report. It is clear that no proper analysis has ever been attempted. In consequence, not even the principal poi phonology or morphology have been grasped (apart, of course, from those that had already been dealt with in the Report). The explanations given by Freyman unsystematically, sentence by sentence, are marked by poverty of invention, lack of coherence, and irritating repetitiveness. There is an abundance of blunders; a few examples may be he
=== grep Sogdian Loan-Words title ===
```


## [2026-09-07T20:45:54.569Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"loan-words in new persian\\|Loan-words in New\\|Sogdian loan\" HENNING_selected_papers.txt | head"
}
```


### [2026-09-07T20:45:54.639Z] TOOL RESULT

```
11763:we may take this opportunity of mentioning a hitherto unrecognized Sogdian loan-word in Turkish, viz. Turk. gly ni, i, 430; ili, 134 ‘andalib; Ton Muhanni, 176—Aaxir) from Sogdian
11770:milar Sogdian loan-words in Pe nd-wif, ete,
```


## [2026-09-07T20:45:55.125Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FRS پل ===\"\ngrep -n \"کفیده\\|پلش\\|معروفی\" FRS_pages.txt | head -10"
}
```


### [2026-09-07T20:45:55.179Z] TOOL RESULT

```
=== FRS پل ===
1010: ‫چون‌نو ای‌خنبا کر ان باشد کهزناد چنانکه ازرقی| درف هنک سروری ‪ :‬معروفی | گفت‪:‬‬
2414:              ‫آهنی باشد‪ ۲‬کهبدان ماهیکیرند » [معروفی کوید ‪:‬‬
3383:            ‫کره دوتا باشدکه آسان ‪:‬نگشایند »| معروفی گوید ‪:‬‬
5539:                          ‫رکفته ‪:‬‬     ‫کفیده‬      ‫کفید‬
5545:   ‫کفیده شود سنکک تیمار خوار ]‬
8106:                            ‫کليك بود بعنی بتازی حول [معروفی گوید ‪:‬‬
13219:                                    ‫یبای استمعروفی‌در راه خوارزم!‬
13449:                                           ‫پاشنة پابود[معروفی کوید ‪۱ :‬‬
13450:                                  ‫هميشه کفش و پلش راکفیده بینممن‬
13452:‫بجایکفش و پلش دل کفیده بایستی ]‬
```


## [2026-09-07T20:46:01.006Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '13440,13455p' FRS_pages.txt\npython3 - <<'EOF'\nt=open('FRS_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\noff=sum(len(l)+1 for l in lines[:13448])\nprint('leaf', t[:off].count('\\f'))\nEOF"
}
```


### [2026-09-07T20:46:02.347Z] TOOL RESULT

```
                                                ‫» ‪ -‬درحاشبهٌ لناینبت چنین آمده ‪:‬‬
  ‫اینسالخوردمز ال برابنای‌زرومال[ کذ!]‬               ‫تارب چر ا نیردس گث ازه‌بان ما‬
                                                                 ‫‪ -1‬چ ‪:‬و ین انبان ‪۰‬‬
                                      ‫‪۳۳‬‬

                           ‫ای آن که جز از شعر غزل هیچ ‪ ۱‬تخوانی‬
‫هرکز نکنی سیردل از قتببل و ترفند ]‬
                            ‫‪۷‬‬

                                           ‫پاشنة پابود[معروفی کوید ‪۱ :‬‬
                                  ‫هميشه کفش و پلش راکفیده بینممن‬

‫بجایکفش و پلش دل کفیده بایستی ]‬
                                  ‫خوهل‬
                                  ‫کر بود ضد راست؟ [بوشکور گوید ‪:‬‬
                                 ‫بس ار زاژ و خوهل آوری دش من‬
leaf 332
```


## [2026-09-07T20:46:09.735Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HJB PYJAMMAS ===\"\ngrep -n -i \"pyjamma\\|pyjama\\|paejama\\|pae-jama\" HJB.txt | head"
}
```


### [2026-09-07T20:46:09.780Z] TOOL RESULT

```
=== HJB PYJAMMAS ===
1750:1885.— "The  cloth  from  which  these pyjamas  aro  made  (in  Swat)  is  known  as Alacha,  and  is  as  a  rule  manufactured  in their  own  houses,  from  2  to  20  threads  of silk  being  let  in  with  the  cotton  ;  the  silk  aH well  as  the  cotton  is  brousrht  from  Peshawur and  spun  at  home"— M'Nair's  Report  on Explorations,  p.  5.
13285:L0NG-DBAWEB8,  s.  This  is  axt old-fashioned  equivalent  for  pyjamas^ (a. v.).  Of  late  it  is  confined  to  the Madras  Presidency,  and  to  outfitters* lists.  [Mosquito  drawers  were  probably like  these.]
13293:(See  PYJAMAS,  HOaUL  BBEEGHS8.. SHULWAUB8,  SIB0RAB8.)
14424:MOGUL  BBEE0HE8,  s.  Ap- parently an  early  name  for  what  we call  long-drawers  or  pyjamas  (qq.v.).
14426:In  a  picture  by  Vandyke  of  William l8t  £arl  oi  Denbigh,  belonging  to  the Duke  of  Hamilton,  and  exhibited  at Edinburgh  in  July  1883,  the  subject is  represented  as  out  shooting,  in  a  red striped  shirt  and  pyjamas^  no  doubt  the *'  Mogul  breeches  "  of  the  period.
17404:S laces  it  is  peculiar  to  men,  the  women's rawers  being  Tnrwar.  Herklots  {Qanoon-e- lalam,  App.  xiv.)  gives  eezar  as  equivalent to  Bhulwaur,  like  the  pyjamma,  but  not so  wide.
18368:PYJAMAfAS.
18373:PYJAMMAS,  8.  Hind,  pdi-jdma (see  JAMMA),  lit.  'leg-clothing.'^  A pair  of  loose  drawers  or  trowsers,  tied round  the  waist.  Such  a  garment  is used  by  various  persons  in  India,  e.g. by  women  of  various  classes,  by  Sikh men,  and  by  most  Mahommedans  of both  sexas.  It  was  adopted  from  the Mahommedans  by  Europeans  as  an article  of  dishabille  and  of  night attire,  and  is  synonymous  with  Long Drawers,  Shulw^urs,  and  Mogul- breecliefl.  [For  some  distinctions between  these  various  articles  of  dress see  Forbes-Watson,  {Textile  Manu- factures, 57).]  It  is  probable  that  we English  took  the  habit  like  a  good many  others  from  the  Portuguese. Thus  Pyrard  (c.  1610)  says,  in  speak- ing of  Goa  Hospital:  "lis  ont  force calsons  sans  quoy  ne  couchent  iamais les  Portugais  des  Indes"  (ii.  p.  11; [Hak.  Soc.  ii.  9]).  The  word  is  now  used in  London  shops.  A  friend  furnishes the  following  reminiscence  :  "  The  late
18375:some  40  years  ago,  in  reply  to  a question  why  pyjammas  had  feet sewn  on  to  them  (as  was  sometimes the  case  with  those  furnished  by London  outfitters)  answered :  *  I believe,  Sir,  it  is  because  of  the White  Ants!'"
20111:SHULWAUBS,  s.  Trooseis,  or drawers  rather,  of  the  Oriental  kind, the  same  as  pyjammas,  long-drawen, or  mogiil- breeches  (qq.vX  The Persian  is  shalwdr,  whicA  according to  Prof.  Max  Miiller  is  more  correcUr shulvdr^  from  shul,  'the  thigh,'  re- lated to  Latin  cruc,  cruris^  and  to  Ski. kskura  or  hhtira^  'hoof  (see  Putey  on Danielj  570).  Be  this  as  it  may,  the Ar.  form  is  sirwdl  (vulg.  duiruxil\,  pL sardtoUy  [which  Burton  (Arah.  NtghtSy i.  206)  translates  'bag-trousers'  and 'petticoat- trousers,'  "the  latter  being the  divided  skirt  of  the  future!^ This  appears  in  the  ordinary  editions of  the  ^ook  of  Daniel  in  Qreek,  as ffopdfiapa,  and  also  in  the  Yul^te,  as follows :  "  £t  capillus  capitis  eorum non  esset  adustus,  et  saianla  eorum non  fuissent  immutata,  et  odor  ignis
```


## [2026-09-07T20:46:10.451Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AID pyjamas ===\"\ngrep -n -i \"pyjama\\|paijama\" AID.txt | head\necho \"=== KLN pajamas ===\"\ngrep -n -i \"pajama\\|pyjama\" KLN_1966.txt KLN_1971.txt | head"
}
```


### [2026-09-07T20:46:10.512Z] TOOL RESULT

```
=== AID pyjamas ===
5161:PAijAmA.  [Persian.]  Drawers,  trou- sers, such  as  are  worn  by  MusalmAn men  and  women.  Among  Euro- peans, sleeping-drawers.
=== KLN pajamas ===
KLN_1971.txt:44264:and foot and cp. the first element in pajama and 
KLN_1971.txt:95528:ped, pawn (in chess), parallelepiped, pajama, 
KLN_1971.txt:171327:pajamas, pyjamas, n. pi., loose trousers or draw- 
KLN_1971.txt:171328:ers. — Hind, pajama, paijama, lit. ‘leg-garment’, 
KLN_1971.txt:196714:pyjamas, n. pi. — See pajamas, 
KLN_1971.txt:216938:‘foot’ ; see foot and cp. the first element in pajama, 
KLN_1971.txt:242190:poy and pajama. The spelling teapoy is due to 
KLN_1966.txt:7237:charpoy,  n.,  the  common  Indian  bedstead.  — Hind.  charpai,  lit.  ‘four-footed’,  fr.  Pers.  cdhar- pdi,  ‘four-footed’,  fr.  (ahar,  ‘four’  (which  is  rel. to  Avestic  ca&ward,  ‘four’),  and  pal,  ‘foot’ (which  is  rel.  to  Avestic  pad-,  ‘foot’).  See  four and  foot  and  cp.  the  first  element  in  pajama  and the  second  element  in  teapoy.  Cp.  Gk.  TerpaKOU? and  L.  quadrupes,  ‘four-footed’,  which  are  the exact  etymological  equivalents  of  Pers.  cahar-pdi. charqui,  n.,  dried  meat.  —  Sp.,  fr.  Peruv.  charqui, ‘dried  meat’.  Cp.  jerk,  ‘to  dry  meat’, chart,  n.,  a  sea  map.  —  F.  carte,  fr.  Late  L.  carta, fr.  L.  charta.  See  card,  ‘a  piece  of  pasteboard’, and  cp.  next  word.
KLN_1966.txt:15110:foot,  n.  —  ME.  fat,  fr.  OE.  fat,  rel.  to  OS.  fat, ON.  fa tr,  Swed.  fat,  Dan.  fad,  Du.  voet,  OHG. fuo3,  MHG.  VU03,  G.  Fuji,  Goth./o/u.s,  ‘foot’,  and cogn.  with  Ol.  pit,  acc.  pidam,  ‘foot’,  Avestic pad-,  ‘foot’,  Toch.  A  pe,  B  pai,  ‘foot’,  A  pent,  B paine,  ‘both  feet’.  Arm.  ot-n,  ‘foot’,  ot-k\  ‘feet’. Dor.  Gk.  7rtii ;,  Att.  7101)9  (formed  on  analogy  of 009,  ‘ear’),  gen.  770809,  L.  pes,  gen.  pedis,  ‘foot’, Ol.  paddm,  ‘step,  track’.  Arm.  het,  gen.  he  toy, ‘track,  footmark’,  Gk.  rtiSt),  ‘fetter’,  TreSav,  ‘to bind  with  fetters’,  7t£Sov,  ‘ground,  earth’,  h.peda, ‘footstep \pedica,  ‘shackle,  fetter’,  impedire,  ‘en¬ tangle,  ensnare’,  expedire,  ‘to  extricate,  disen¬ gage’,  Lith.  peda,  ‘footstep,  trace’,  OSlav.  podii, ‘loft’,  Russ,  pod-oshva,  ‘sole  of  foot’.  All  these words  derive  fr.  I.-E.  base  *pdd-,  *pid-,  ‘foot’. Cp.  fetch,  fetlock,  fetter,  fit,  ‘part  of  a  song’.  Cp. also  antipodes,  apod,  babouche,  biped,  breviped, caliber,  cap-a-pie,  charpoy,  expedient,  expedite, impeach,  impede,  impedimenta.  Lycopodium, millepede,  multiped(e),  octopus,  oppidan,  palmi¬ ped,  pawn  (in  chess),  parallelepiped,  pajama, pedal,  pedate,  -pede,  pedesis,  pedestal,  Pedetes, pedicel,  pedicle,  pedigree,  pedology,  ‘the  study  of soils’,  peduncle,  peon,  pes,  petiole,  pew,  Peziza, pie,  ‘a  small  coin’,  piepoudre,  pilot,  podagra, podal,  podium,  podo-,  pug,  ‘footprint’,  puy,  seer- paw,  Taliped,  Tarsipes,  teapoy,  trapezium,  triped, tripos,  vamp,  ‘front  part  of  the  foot’,  velocipede. Cp.  also  pejorative,  pessimism.
KLN_1966.txt:26951:pajamas,  pyjamas,  n.  pi.,  loose  trousers  or  draw¬ ers.  —  Hind,  pajama,  paijama,  lit.  ‘leg-garment’, fr.  Pers.  pa,  pat,  ‘foot,  leg’,  and  jama,  ‘clothing, garment’.  Pers.  pal,  ‘foot,  leg’,  is  rel.  to  Avestic pad-,  ‘foot’,  and  cogn.  with  Gk.  tcou;,  gen.  tto- 86q,  L.  pes,  gen.  pedis,  ‘foot’,  Goth,  fotus,  OE. fot,  ‘foot’.  See  foot  and  cp.  the  second  element in  charpoy,  teapoy,  seerpaw. pal,  n.,  an  intimate  friend.  —  English  Gypsy  pal, phal,  ‘brother’,  fr.  Gypsy  phral,  fr.  OI.  bhratar , ‘brother’.  See  brother.
```


## [2026-09-07T20:46:19.424Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ndef leafof(fn, lineno):\n    t=open(fn,encoding='utf-8',errors='replace').read()\n    lines=t.split('\\n')\n    off=sum(len(l)+1 for l in lines[:lineno-1])\n    return t[:off].count('\\f')\nprint('KLN_1966 26951 leaf', leafof('KLN_1966.txt',26951))\nprint('KLN_1966 15110 leaf', leafof('KLN_1966.txt',15110))\nprint('HJB 18373 leaf', leafof('HJB.txt',18373))\nprint('AID 5161 leaf', leafof('AID.txt',5161))\nEOF"
}
```


### [2026-09-07T20:46:20.892Z] TOOL RESULT

```
KLN_1966 26951 leaf 594
KLN_1966 15110 leaf 330
HJB 18373 leaf 794
AID 5161 leaf 252
```


## [2026-09-07T20:46:43.441Z] TOOL CALL #50: Bash

```json
{
 "command": "sed -n '1,60p' tools/ref_page.py"
}
```


### [2026-09-07T20:46:43.496Z] TOOL RESULT

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


## [2026-09-07T20:46:45.687Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT leaf 658 (p.434?) پیک ===\"\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (657,658,659):\n    if 'پیک' in t[i] or 'پیاده' in t[i]:\n        print('HIT',i)\nfor i,p in enumerate(t):\n    if 'پیک ' in p and 640<i<690:\n        print('cand',i, i-224)\nEOF"
}
```


### [2026-09-07T20:46:46.988Z] TOOL RESULT

```
=== BQT leaf 658 (p.434?) پیک ===
HIT 659
```


## [2026-09-07T20:46:50.866Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(t[659])\nEOF"
}
```


### [2026-09-07T20:46:52.169Z] TOOL RESULT

```
ی
بهنا 4 بروزن مستانه , نوعی‌از میمون
باشد- وکلیچةٌ روغنی را لبز گود .
هنال بروزن کمند. دامی باشدکه‌بدان
آهو گیر ند.
(م ی و - بروزن فدفور » چیزیست مانند
دستنبوی که بزبان عرب آن را حنظل خوانند
وقنامالنمام(۱) همان‌است- ویمعنی بهی‌نیز هست
که خرزحره باشد .
44 س ختح ارل وثانی و تالث . بمعتی
بهن‌است» و آن شیری باشد که سیب مهربانی
بیار دریستان مادر طفیان کند - وبسکون ثانی
چوکان بازی و کوی بازی باشد - و نوعی از
سازند و گوی را در آن نهاده بر خوا اندازند
وچون تزديك بزمین رسد باز بهمان پهنه‌میز نند
[۴ نگذارد که برزهن آید ی تمفصل رسانند ۰
وآن‌را جربی طبطا بکوبند- و پهنی ران آذمی
و حیوانات دیگر باشد از جاب درون و آن را
بربی قطن خوانند - و بمعنی میدان هم آمده
خوانند وچوبی باشد مخروطی تراشیده که‌اطفال
رسمانی برآن پیچند و نوعی برزمین اندازند که
تادیرباز بگردد ۱ .
ی « بنتح اول بر وزن سهی ۰ حنظل
باشد و آنراخریز؛ تلخ‌هم هت و خرزهرمرا
چوکان را نیز گوشد که سر آنرا مانشدکفه یز پهی خوانند ؟ .
بیان بیست ویکم
ی ه بنثح اول و سکون الی » ممروف
است» و آن چیزی‌باشد که بر کمان وزین اسپ
وب تیرجایی که پیکان درآ نکنندیبند. وجربی
عصب کویند. و مضفف پای است که بمربی رجل
خوانشد ۴ - و نشان بای باشد که نقش‌فدم‌است ۴
ودئبال و پس وعقب. و تعافب. و قصد و اراده -
ونشان - و پی‌بردن بعنی نشان یافتن - و بمعنی
برای و بهر بیز حست چنانکه گوبند * از پی
فلان کار» بعنی از برای فلان کار واز بهر فلان
چیز - و بمعتی بار و مرنبه هم آمده است مثل
آنکه گونند فچند پی» مراد آن باشد که چند
مرتبه وچند پار- وتلب و طافت را نیز کفته‌اند -
؟ - باين معتی در اسطلاح علمی
۴ . رك: ا.
بقیه از صفحة 4۳۲
مشق ۰۳۶۹
۴ - پهلوی 09220 2 اونوالا 6 ۸
```


## [2026-09-07T20:47:02.374Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in range(659,666):\n    hits=[l for l in t[i].split('\\n') if 'پیک' in l or 'پیاده' in l]\n    if hits: print('leaf',i,'p~',i-225, hits[:4])\nEOF"
}
```


### [2026-09-07T20:47:03.690Z] TOOL RESULT

```
leaf 659 p~ 434 ['وب تیرجایی که پیکان درآ نکنندیبند. وجربی']
```


## [2026-09-07T20:47:11.669Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON پیژامه ===\"\ngrep -n \"پیژامه\\|پی جامه\\|پیجامه\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt 2>/dev/null | head\necho \"=== ARY پژواک / پا / پیک ===\"\ngrep -n \"پژواک\\|پژ \" incoming/ARY/ARY_pages.txt | head\necho \"=== ARY پا foot ===\"\ngrep -n \"PED\\|Ped\\b\" incoming/ARY/ARY_latin_index_pages.txt | head"
}
```


### [2026-09-07T20:47:11.755Z] TOOL RESULT

```
=== MON پیژامه ===
incoming/MON/MON_2vol_Adena_v1_djvu.txt:25474:که به زیرشلوار یا شلوار پیژامه و یا امثالش 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:34030:پی جامه: (م-922 01-12 (امر.) نوعی شلوار 
MON_part1.txt:25474:که به زیرشلوار یا شلوار پیژامه و یا امثالش 
MON_part1.txt:34030:پی جامه: (م-922 01-12 (امر.) نوعی شلوار 
=== ARY پژواک / پا / پیک ===
=== ARY پا foot ===
340:(ENCYCLOPEDIA OF INDO-EUROPEAN CULTURE, PP. 290-299)
2570:rie type Sas EPEDANOS GREER) gly
4192:HOLD CHURCH $PAVIC) 345 539-1 PES, PEDIS LATIN) 3
4194:PEDA LITHUANIAN) gly} PIE SPANISH) glityel
4195:PEDA LATVIAN) (3) 5) PIEDE ITALIAN) gist!
5234:PEDA LITHUANIAN) gi 3 HOLD PERSIAN) jel go
5235:PEDA LATVIAN) (93) gi 3 PATI. PADAM.
5236:PEDAN HITTITE) sx PEY PAHLAVI) (5 shay
5241:AMINDAROV: (AFTER) 131 PEDON, PEDION (GREEK) sy
5242:PEDA (LATIN) 3
```


## [2026-09-07T20:47:16.872Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '34025,34036p' MON_part1.txt\necho \"=== ARY around 5234 ===\"\nsed -n '5225,5250p' incoming/ARY/ARY_pages.txt\necho \"=== ARY 4188-4200 ===\"\nsed -n '4185,4200p' incoming/ARY/ARY_pages.txt"
}
```


### [2026-09-07T20:47:16.950Z] TOOL RESULT

```
پیت: ؛آم (۱.) چلیک فلزی (آهنی با حلبی) 
برای نفت و روغن و مانند آن» تنکة آهنی با 
حلبی مکعب مستطیل شکل برای حفظ و 
حمل نفت و روغن و غیره. 

پی جامه: (م-922 01-12 (امر.) نوعی شلوار 
کشاد که زنان هند بوشند. جامه‌ای کشاد و 
صحتا بر ها از سم له و سلوان وان چاو 
خانه و هنگام خواب بوشند؛ ببژاما. 

پیچ: * (امص.) خمیدگی» کجی, گردش» 
گشت. هر یکث از خم‌های چیزی (مانند 
=== ARY around 5234 ===
واژه از آراه" به "رهنمود" در زبان‌های فارسی و کردی و بلوچی منطقی بنظر می‌رسد.
فارسی (/(۳87۶]4): پوپو, پک (به چم ایّریُر"یا اشانه سر) ۸4 ,8177
چم آنگلیسی سرواژه‌ی فارسی: 10000
هند و آروپایی (۰)/۸00-210720۷ ,۹5807
کردی (78.015): زتولاها لتونی (لتی) (/7۷1با): نی اد ابا
ارمنی (048۸//4/): 7007
بونانی (07886): 205 پسگشت‌ها مینست
لاتین (7100ل): 10۸ 1
فرانسه (۳52/2): 10 0 (31۳۳8) :امد
آلمانی کهن (/(05824۸ هط صاه): 6 (1100708) +7
10۸ 35 (10400)) انم
لهستانی (34ل]۳0): و در برهان قاطم + ۳۳۵
اسلا کی (5107430): 11
[pdf page 178]
۹ ها و
یادداشت:
این واژه نوعی "نام آوا" (031034۸70۳011۸) است.
چم انگلیسی سرواژی ارس 1868
اوستایی (45874/0): ۳7۸ ب3ظ7 بقا78 (711۸/201
پهلری (1ه]۳۸): ان انگلیسی (8لا6۸0): ۴1 ماآر۲87
کردی (07018): 7 ,۴181 نروژی (/(07/501۸/): 01۸
افغانی (پشتو) (/۸70]۸۸). 07 هلندی (7(ع007): ۷۲
یونانی (066524): ها ۶۸ ,۲۸۲۸۹ اسلاوی کهن (ع۲1بها5 ۱267 صا0):
لاتین (/712ضا): ۲۴۲8 اد 8 ان |
فرانسه (لح/۳882۸): 2۸7 روسی ((551۸نا#): ۳
اسپانیایی (62۸0/180): باقاط ,8817870 چکه (2507): ۸ ۴0۸
=== ARY 4188-4200 ===
لاتین (14710)(شاید) را دی
ایسلندی کهن ((010۸۷24نف5 طا): پسگشت‌ها گرد رن
۸ ب818۸ 1 ۶002
۱ آلمانی کهن (/(0570/۸ ۱/017 صا0): 7 (8۸1(08۵)) :تا (ماط0
7 ,)8186 8 (8130) 2
انگلیسی کهن (37ا8۸۷0 012): 85077۸0 1153 8
اسلاوی کهن (۷72ما5 بل#تابن صال): برهان قاطع + ۱ ۳۴۰
0 8۸7۸7 807۸1 ,85055 :
یادداشت:
بازگشت به: باک
[pdf page 144]
نج
بینی / ۱۴۵
یکره دض
اوستایی (/4887۸4۸): ۷۸۲۰ ,۷۸5۸ نروژی (/۸/07775014): 5(
پارسی باستان (۲8۴۶۶4۸۷ ۰)010 ۰ ۲۸7۸۵۲ هلدی (017۳[4): ناد لا
```


## [2026-09-07T20:47:26.234Z] TOOL CALL #56: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-07T20:47:26.240Z] TOOL RESULT

```


```


## [2026-09-07T20:47:30.809Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%BE%DA%98%D9%88%D8%A7%DA%A9",
 "prompt": "What does this page say about Persian پژواک — meaning and etymology (any components پژ + واک, Avestan, Middle Persian)?"
}
```


## [2026-09-07T20:47:32.011Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%BE%DB%8C%DA%A9",
 "prompt": "Persian پیک: meaning and etymology — Middle Persian form, Avestan, any relation to pāy 'foot'?"
}
```


### [2026-09-07T20:47:36.043Z] TOOL RESULT

```
# پژواک (Pažwāk) - Wiktionary Entry Analysis

Based on the Wiktionary page provided, here's what it conveys:

## Meaning
The page defines پژواک simply as **"echo"** — that is its sole stated definition in the noun entry.

## Etymology
The page contains **no etymological information**. There is no discussion of:
- Component breakdown (پژ + واک)
- Avestan origins
- Middle Persian ancestry
- Historical linguistic development

The entry focuses exclusively on pronunciation variants across different Persian dialects (Classical, Dari, Iranian, Tajik, and Hazaragi) and lists one derived term: پژواک‌نگاری (pežvâk-negâri), but provides no etymological analysis or historical linguistic context.

**In summary:** While the page delivers the word's modern meaning and phonetic data, it deliberately omits any etymological commentary that might address your specific questions about component structure or historical language origins.
```


### [2026-09-07T20:47:38.669Z] TOOL RESULT

```
# پیک (Peyk) - Persian Word Etymology

Based on the Wiktionary entry, **پیک** has two distinct etymologies:

## Etymology 1: Messenger/Courier

The primary meaning derives from Middle Persian, ultimately tracing to Proto-Iranian **\*pā́dah** ("foot"). The entry notes this is "cognate with Sanskrit _padika_" (pedestrian).

The word carries Iranian borrowings across multiple languages: Old Armenian, Georgian, Classical Syriac, and Arabic all adopted related forms. Interestingly, it's a "doublet of _فوج_" (fowj) in Persian, meaning both share the same ancestral root but diverged during linguistic evolution.

**Primary definition:** "messenger, courier"

## Etymology 2: Alcohol Measure

A separate entry indicates this word was "borrowed from English _peg_," referring to a "shot (measure of alcohol)."

The etymological research cites classical philologists like Paul Horn (1893) and Heinrich Hübschmann (1897), demonstrating the word's well-documented linguistic heritage across Indo-European and Semitic language families.
```


## [2026-09-07T20:47:44.256Z] TOOL CALL #59: WebSearch

```json
{
 "query": "پژواک ریشه‌شناسی پژ واک حسن‌دوست اوستایی"
}
```


## [2026-09-07T20:47:45.967Z] TOOL CALL #60: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%BE%D8%A7%DB%8C",
 "prompt": "Persian پای/پا: etymology — Middle Persian, Old Persian, Avestan, Proto-Iranian, Proto-Indo-European forms. Also mention پایین if present."
}
```


### [2026-09-07T20:47:51.716Z] TOOL RESULT

```
# پای (pây) - Etymology Summary

Based on the Wiktionary entry, here's the linguistic heritage of this Persian word:

## Primary Etymology (Foot)

The word پای originates from an ancient lineage:

- **Middle Persian**: pāy
- **Old Persian**: 𐎱𐎠𐎭 (pād(a))
- **Proto-Iranian**: *pā́dah
- **Proto-Indo-Iranian**: *pā́ts
- **Proto-Indo-European**: *pṓds ("foot")

This demonstrates how the term evolved across multiple language families over millennia, ultimately tracing back to the Indo-European root meaning "foot."

## Secondary Etymology (Pie)

The entry also documents a modern borrowing: "پای was borrowed from English _pie_" to denote the baked dessert in Persian.

## Language Variants

The word appears across multiple Persian dialects with consistent pronunciation patterns, though the Iranian Persian form is noted as archaic compared to the standard پا (pâ).
```


### [2026-09-07T20:47:53.816Z] TOOL RESULT

```
Web search results for query: "پژواک ریشه‌شناسی پژ واک حسن‌دوست اوستایی"

Links: [{"title":"محمد حسن‌دوست - ویکی‌پدیا، دانشنامهٔ آزاد","url":"https://fa.wikipedia.org/wiki/%D9%85%D8%AD%D9%85%D8%AF_%D8%AD%D8%B3%D9%86%E2%80%8C%D8%AF%D9%88%D8%B3%D8%AA"},{"title":"فرهنگ ریشه‌شناختی زبان فارسی - ویکی‌پدیا، دانشنامهٔ آزاد","url":"https://fa.wikipedia.org/wiki/%D9%81%D8%B1%D9%87%D9%86%DA%AF_%D8%B1%DB%8C%D8%B4%D9%87%E2%80%8C%D8%B4%D9%86%D8%A7%D8%AE%D8%AA%DB%8C_%D8%B2%D8%A8%D8%A7%D9%86_%D9%81%D8%A7%D8%B1%D8%B3%DB%8C"},{"title":"فرهنگ ریشه‌شناختی فارسی، محمد حسن‌دوست، 1393 تهران، فرهنگستان زبان و ادب فارسی، دورۀ پنج جلدی","url":"https://lsi-linguistics.ihcs.ac.ir/article_1976.html"},{"title":"پژواک - معنی در دیکشنری آبادیس","url":"https://abadis.ir/fatofa/%D9%BE%DA%98%D9%88%D8%A7%DA%A9/"},{"title":"محمد حسن دوست","url":"https://ensani.ir/fa/article/author/73236"},{"title":"کتاب فرهنگ ریشه شناختی زبان فارسی(5جلدی) اثر محمد حسن دوست | ایران کتاب","url":"https://www.iranketab.ir/book/40213-farsi-language"},{"title":"فرهنگ ریشه‌شناختی زبان فارسی | راهک","url":"https://raahak.com/?p=942"},{"title":"محمد حسن دوست نویسنده کتاب فرهنگ ریشه شناختی زبان فارسی(5جلدی) | ایران کتاب","url":"https://www.iranketab.ir/profile/23034-mohammad-hasandust"}]

بر اساس نتایج جستجو، اطلاعات زیر را می‌تواند برای شما ارائه دهم:

## درباره "پژواک" از نظر ریشه‌شناسی

پَژ در پَژواک همان واژ در واژگون است و یک پیشوند وارونگی‌رسان است، و واک با آواز و واژه و واج هم ریشه دارد و ریشه آن واختن در پهلوی است به معنی گفتن، خواندن. پَژواک: از پَژ (پیشوند) به همراه واژه یِ واک به چمِ بازتابِ یا انعکاسِ صدا ساخته شده است.

## درباره محمد حسن‌دوست اوستایی

محمّد حسن‌دوست متخصص زبان‌های ایرانی باستان و استاد وابستهٔ دانشگاه شهید بهشتی است. فرهنگ ریشه‌شناختی زبان فارسی یک فرهنگ لغت اختصاصی برای ریشه‌شناسی زبان فارسی تألیف محمد حسن‌دوست است که در سال ۱۳۹۳ در پنج جلد منتشر شده است. این کتاب در سی‌وسومین دورهٔ جایزهٔ کتاب سال جمهوری اسلامی ایران، در گروه «زبان‌های باستانی»، به‌عنوان اثر برگزیده شناخته شد.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-07T20:48:11.178Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\ni=15735-1\nprint('\\n'.join(lines[i-3:i+6]))\noff=sum(len(l)+1 for l in lines[:i])\nprint('LEAF', t[:off].count('\\f'))\nEOF"
}
```


### [2026-09-07T20:48:13.035Z] TOOL RESULT

```
—  ")  H.  3.  19  ff.  ist  jünger  als  H.  3.  t  ff. und  diesem  Sliick  nachgebildet.  —  ■])  Pü. : paarunt  (in  Aw.-Buchst.)  j  s.  zu  *aivS.gava' No.  4.
•  j,  paurva'tar« ')  Adv.  'zuvor,  vorerst,  vor »!Atm':  pprfsal  frahoitrd . .  zara%ustr>m: paifi.mrüihi  p'  Y.  71.  i.
Pü. ! ////iw- ').  —  ')  Lesung  nicht  sicher.  — 3)  Mit  undeutlicher  Kil.,   s.  Dst.  ZA.  /.  430.
•  j.  paurvatä-  f.  'Bergzug,  -kette,  Gebirg":
dva  hamankunai^^  Ha  (NS.)  YtJ(j.3;  3;
—  äat  ähva  'tähva  pguru.iari\s  VTra^ahe haamS  Y.  jo.  la.
ai.  Tgl.  pärvcUa-  xa.  —  Pü.:  anäar  an  jiäi  i pnr  täk,  aber  Sfi.:  pavilraniiaresu.
•  j.,  g.  paiirva'^t-  f.  'prioratus'  uzw. i)  'Voransein,  Anderspitzestehen,  princi-
patus' :  amavai^yä  'tätS  amavai^yS  upara- tätB'Vi.ff.4.  3)  'das  Höchste  (einer Sache),  Inbegriff,  Auslese':  mastfm  yqm pouru,äsaintJm  mq^raheäi  "Wöm  Y. 57.20;
LEAF 493
```


## [2026-09-07T20:48:13.358Z] TOOL CALL #62: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%BE%DA%98%D9%88%D9%87%DB%8C%D8%AF%D9%86",
 "prompt": "Persian پژوهیدن: etymology — what is the prefix پژ- derived from (Old Iranian *pati-?), and what does the entry say about Middle Persian forms?"
}
```


### [2026-09-07T20:48:19.539Z] TOOL RESULT

```
# Etymology of پژوهیدن (pežuhidan)

Based on the Wiktionary entry, the word is **inherited from Middle Persian** with the form **wcwstn** (pronounced /⁠wizōstan, wizōhīdan⁠/), meaning "to investigate, to examine."

## Sound Changes from Middle Persian to New Persian

The entry explains the phonetic evolution: "The initial 'w' phoneme most likely first turned into 'b', which is a very common sound change from Middle Persian to New Persian (change of initial w- to either b- or gw- → g-). Afterwards, the 'b' turned into a 'p' phoneme."

**Regarding the prefix پژ- (pežh):** The entry does not explicitly discuss whether this derives from Old Iranian *pati- or provide detailed etymological analysis of the individual morphological components. It focuses on the overall word's development from Middle Persian rather than breaking down the prefix's ultimate Indo-European origins.
```


## [2026-09-07T20:48:30.112Z] TOOL CALL #63: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%BE%DA%98%D9%88%D8%A7%DA%A9/",
 "prompt": "What do Dehkhoda and Mo'in (فرهنگ معین) say about پژواک — definition and any etymology or origin tag? Quote the Persian text."
}
```


## [2026-09-07T20:48:31.118Z] TOOL CALL #64: WebSearch

```json
{
 "query": "\"پژواک\" etymology \"pati-vāka\" OR \"*pati-vāk\" Persian echo prefix paž-"
}
```


### [2026-09-07T20:48:36.649Z] TOOL RESULT

```
# Dehkhoda and Mo'in Definitions of پژواک

**Dehkhoda (لغت نامه دهخدا):**
The dictionary entry states: "پژواک. [ پ َژْ / پ ِژْ ] ( اِ ) آوازی که در کوه و گرمابه و دره و گنبد و مانند آن پیچد. صدا. آواز منعکس. عکس الصوت."

This describes it as the sound that reverberates in mountains, bathhouses, valleys, and domes—identifying it as an echo or reflected sound.

**Mo'in (فرهنگ معین):**
The entry provides: "(پِ ) (اِ. ) بازتاب صدا در کوه ، طنین ."

Mo'in's definition is more concise, describing it simply as the reverberation of sound in mountains and as resonance (طنین).

Neither source explicitly provides etymological or origin information for the word's derivation.
```


### [2026-09-07T20:48:39.323Z] TOOL RESULT

```
Web search results for query: ""پژواک" etymology "pati-vāka" OR "*pati-vāk" Persian echo prefix paž-"

Links: [{"title":"Hidden in Plain Sight: Illuminating Indo-European Cognates in Persian – borderlessblogger","url":"https://borderlessblogger.com/2023/05/19/hidden-in-plain-sight-illuminating-indo-european-words-in-persian/"},{"title":"پژواک - معنی در دیکشنری آبادیس","url":"https://abadis.ir/fatofa/%D9%BE%DA%98%D9%88%D8%A7%DA%A9/"},{"title":"Dialectal Layers in West Iranian: a Hierarchical Dirichlet Process Approach to Linguistic Relationships","url":"https://arxiv.org/pdf/2001.05297"},{"title":"Persian-Etymology-Charts.pdf","url":"https://parsianjoman.org/wp-content/uploads/2022/12/Persian-Etymology-Charts.pdf"},{"title":"List of English words of Persian origin - Wikipedia","url":"https://en.wikipedia.org/wiki/List_of_English_words_of_Persian_origin"},{"title":"Pe (Persian letter)","url":"https://en.wikipedia.org/wiki/Pe_(Persian_letter)"},{"title":"HPS: a hierarchical Persian stemming method","url":"https://arxiv.org/pdf/1403.2837"},{"title":"Connecting the Persian-speaking World through Transliteration","url":"https://arxiv.org/pdf/2502.20047"},{"title":"Echo subject","url":"https://en.wikipedia.org/wiki/Echo_subject"}]

Based on the search results, I found relevant information about the Persian word "پژواک" (Pezhvāk/pezhvāk).

The word "Pezhvāk" meaning "echo" comes from Middle Persian ʾwʾz (āwāč, āwāz, "voice, sound, tune"), with the second element from wāč/wāz ("word, speech"), which derives from Proto-Iranian *wā́xš, from Proto-Indo-Iranian *wā́kš, ultimately from Proto-Indo-European *h₂éd ("to, toward") + *wōkʷs.

The etymological structure appears to break down as:
- **پ** (pe/pa) - corresponds to the prefix meaning "back, again" or "re-" (similar to how English "re-" works)
- **ژ** (zh) - represents the Middle Persian development
- **واک** (vāk) - derives from the root meaning "voice, sound, word"

So "پژواک" essentially means "re-voice" or "re-sound," which semantically aligns with the concept of an echo—a repeated sound that returns. In modern Persian, پژواک (pezhvāk/echo) refers to the repetition of a sound wave or the repetition of a radar or sonar signal through surface reflection.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-07T20:48:50.632Z] TOOL CALL #65: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%BE%DB%8C%D8%A7%D8%AF%D9%87",
 "prompt": "Persian پیاده: etymology — Middle Persian form, Proto-Iranian, relation to pāy 'foot'. Quote the etymology."
}
```


## [2026-09-07T20:48:51.927Z] TOOL CALL #66: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/pajamas",
 "prompt": "Etymology of pajamas/pyjamas: Hindi/Urdu paejama, Persian pai jamah, dates, route into English. Quote it."
}
```


### [2026-09-07T20:48:56.416Z] TOOL RESULT

```
# Etymology of Persian پیاده (piyāda)

The word derives from **Middle Persian** *pdʾtk'* (payādag), which came from **Proto-Iranian** *\*padātaka-* or *\*padātika-*, meaning "on foot."

The etymology involves two possible formations:

1. **Compound origin**: From Proto-Iranian *\*pada-* (foot) + *\*taka-* (to walk, flow). The first component traces to *\*pā́dah* (foot), while the second derives from *\*tač-* and ultimately Proto-Indo-European *\*tekʷ-* (to run, flow).

2. **Alternative formation**: From *\*padāti-* (a secondary derivation from "foot") + *\*-kah* (a deadjectival suffix, -ic).

As the source notes: "the former component from [Proto-Iranian] *\*pā́dah* ('foot')" shows the semantic foundation in the word for foot, with later morphological development producing the modern Persian term meaning both "pedestrian" and "on foot."
```


### [2026-09-07T20:48:56.943Z] TOOL RESULT

```
# Etymology of Pajamas

**Origin:** The word "pajamas" comes from Hindi *pajama*, which likely derived from Persian *paejamah*, meaning "leg clothing."

**Component breakdown:** The Persian term combines *pae* ("leg," from the Indo-European root *ped-* meaning "foot") and *jamah* ("clothing, garment").

**Entry into English:** The garment itself—loose trousers tied at the waist—was worn by Muslims in India and adopted by Europeans there around 1800, particularly for sleepwear. The modern American spelling became established by 1845, while British English favors the spelling "pyjamas."

**Key quote:** The word originated as "loose trousers tied at the waist," worn by Muslims in India and embraced by Europeans there, particularly for nightwear.
```


## [2026-09-07T20:49:13.228Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D9%BE%DA%98%D9%88%D8%A7%DA%A9' --note 'page 383, root Parvan, Persian pažvâk: Wiktionary entry (echo; no etymology given)' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D9%BE%DB%8C%DA%A9' --note 'page 383, root Ped/Pod node 7: Persian payk < MP, Proto-Iranian *padah, cognate Skt padika' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D9%BE%D8%A7%DB%8C' --note 'page 383, root Ped/Pod node 2: Persian pay/pa < MP pay < OP pada < PIE *pods' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D9%BE%DB%8C%D8%A7%D8%AF%D9%87' --note 'page 383, node 7: Persian piyada < MP payadag < PIr *padataka-' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/pajamas' --note 'page 383, nodes 3-4: pajamas < Hindi pajama < Persian pae-jamah' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://abadis.ir/fatofa/%D9%BE%DA%98%D9%88%D8%A7%DA%A9/' --note 'page 383, node 2: Dehkhoda + Moin on pazvak (echo), no etymology tag' 2>&1 | tail -2"
}
```


### [2026-09-07T20:49:17.684Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/b4708a391490f32c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3978347b3fe1bcc8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cd8f15cdf4b429c4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/368005c46dd2afaa.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ba31b0c49580744c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/03f6a25d7d996b2e.txt
```


## [2026-09-07T20:49:24.530Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KNT pada ===\"\ngrep -n \"pāda\\|pada-\\|padiy\" KNT.txt | head -8\necho \"=== IEC ped foot ===\"\ngrep -n \"pēd-\\|pedes.*foot\\|pod-.*foot\" IEC.txt | head -8\necho \"=== LAT peior pessimus ===\"\ngrep -n \"peior\\|pessimus\" LAT.txt | head -6\necho \"=== SKT dispatch ===\"\ngrep -n -i \"^dispatch\\|Dispatch, Despatch\\|despatch\" SKT.txt | head -5"
}
```


### [2026-09-07T20:49:24.616Z] TOOL RESULT

```
=== KNT pada ===
545:$29. Тнк Persistence OF VoweL y into ОР! makes difficulties in the normalization. The nor- malized form of some words containing т is certain: thus дт in the month-name Garma- pada- might theoretically be grama- or garama- or grma-, but is actually garma-, a form assured by etymological cognates. The name атат is Тата, though the characters might equally well stand for Атёйта; and those who would normal- ize with r as à vowel write ’rSdéma, using the sign for the glottal stop to represent the character which elsewhere has the vowel value a. But in £r^m*i3^ we have no clue to the vowel of the first syllable; it may be &arm:$ ог багата or 0pmió (though hardly 6rami$, since ør became с). То avoid the necessity of making decisions in cases where there is no evidence, the normalization here employed is ar alike for phonetic ar and for phonetic 7, and for those instances where we do not have proof of the value, which may also be ara or та.
1061:daéva-, Skt. devd-, Lt. divos deus. pIE *ped- ‘foot’, loc. in ОР ni-padiy, Skt. padi,
1280:name Garma-pada-, c£. Lt. formus ‘hot’. pIE root *g*hen- ‘strike’, OP ja"tiy, Skt. Айли;
1515:*ped- or pod- Чоо? in ni-padiy pati-padum Gurma-pada-, (Ar.) *pàd- in pddaibiya ‘with the two feet’.
1654:nai-mà, nai-maty, nai-$im, nat-pati-mà, pali-maty, iyat-Saty, imat-vd, yadi-patiy, yadi-và, [us}i-ca; similarly in phrasal compounds, pati-padem, ni-padiy. By analogy, naty-di§ DB 4.73, 78.
1678:Prep. patiy, but pati-padam; party, but pari- barümiy; prefix ni- (not found separately in OP) in ni-padiy, ni-rasdtiy.
1774:йр- ‘water’, zíap- ‘night’, xfnau- in u-zfnau- ‘well satisfied’, gau- ‘cow’ in compounds, bard- ‘year’, dwar- ‘door’ in duvara-, nar- ‘man’ in üv-nara-, nàv- ‘ship’, паћ- ‘nose’, pad- ‘foot’ in nipadiy etc., vas- ‘wish’ in adv. vasiy, vib- ‘house’, séd- in upa-stá- ‘aid’, zam- ‘earth’ in u- zma- etc.; perhaps napdl- ‘grandson’, an old pIE word, probably a compound; possibly dà- in ‘wada- as element of Paisiyà-uvüdà-, and vaj- in gen. daha-vaja. $143. Noun AND ApjectivE STEMS WITH THE-
1777:II. Extending a non-verbal stem: üv-nara- to nar-, *wwăi-pašiya- to pati-, pada- páda- to pad-, Márgava- to Margu-, duS-iydra- to yàr-, vazra- in vazra-ka- to *vazy-, eühara- in Gira-vahara- to *yasr-, u-zma- to гат-, hama- to ham-; perhaps Gau-baruva- to baru-, müha- о mah-, viða- to vid-.
=== IEC ped foot ===
6622:kàios, à “base, pedestal, trunk, stem, stand, leg’. WP I, 362 & 509 Skt. kayah ‘trunk, stem, body’; Arm. kaj, kajk, i-st. ‘seat, position’; kajan, Let lodge"; kajun, adj. ‘stable, firm’; MHG hei, heie, f. (ram- mer, beetle’; G Heie 'paving-ram'; Du. hei, id.; Sw. cf. hajare 'pile-driver'; Li. kója “leg, foot’; Latv. kāja, id. (& “base, stand")
10715:met-pod- at the foot, near’. Cf. me-ghri Arm. mawt ‘near, by, at; Thess. mespódi, cj. ‘til’; (Lat. cf. a-pud, fr. *ad-pod-, and pro-pe fr. *pro-ped-)
12562:ped-, péd- “foot in several cpds. See below. WP II, 23 Type *pé&ds, cons. stem. beside *pods, id., obli- que: *ped-, pod- ‘foot’. Type *pedos, om, ios, iə (footing, ground, foundation, place, home- stead" with other semantic extensions)
12570:Vedic pad, pàd, m. id. beside pada, padbhis “on foot: Skt. padáh, ám, mn. ‘step, pace’, cf. pade pade ‘at every step’; pádyah, adj. “foot-?; padyà, f. ‘track’; Av. paiðya, f. ‘foot’; paiðyð, adj. “foot-?; páda, s. ‘land’; Ober pada-, s. ‘footing, step, station’; pada, s. ‘foot; Per. pay, s. ‘foot; paye, s. ‘ground, basis’; pà-, cpds.; Oss. fád ‘footstep’; fad ‘foot; fäz, adj. Cat, plain’, fr. *pedio-); fäzä ‘plain’; Tokh. A pe, B pai, s. ‘foot; Arm. het, hetk, g: hetoç, ab. -ovk ‘footstep’; het, adj. ‘last’; heti, he- tisn, adv. *on foot; heto ‘after’; Hitt. pedan, s. ‘place’; pedesi, adv. “on the spot’; (o-gde in) pata-, for *pada- ‘foot’; Gk. pezis, gs: pezidos, f. “foot, sole, edge’; pédé, péza, f. “foot, sole, base, edge, parapet'; pezós, adj. ‘pedestrian’; Myc. Gk. pédon ‘land’; pédoi, adv. *on the ground’; Aeol. Lesb. peda, Sapph. Dor. ped-, Arc. pe, prp. (after: Arm. het, heto); pesdàj, pezé, adv. “on foot; cf. hexá-pedos, adj. ‘six- footed’; (o-gde in) poús, gs: podós, m. ‘foot; Lat. pēs, gp: pedum, m. id.; peda f. ‘pace’, cf. also la-pes, -pidis (? “catch-fooP hence 'stone"); pedes, adv. “on foot; prope ‘near’; cf. also pro-pere, adv. (*quickly', if for *pro- pedi); peior, adj. ‘worse’; cf. op-pidum, n. ‘walled town’; LLat. acu-pedius 'swift-footed"; centi-pedium 'centipede'; Umb. peti, adv. “by the foot? beside perum, adv. (‘to the ground”, cf. Lat. pessum); Gallo-Lat. cand-etum, if for *cant-edom (*100-foot measure’. Thus R. Gar- nett 1843); Olr. ed, m. (a measure of distance’; cf. also éiss, f. (track, trace, fr. *pedsi-); ON fet, n. *pace, foot-measure'; fit, pl: fitjar, f. ‘webbed foot; ley’; Sw. fját, n. ‘footstep’; (o- gde in) OHG fuoss, OE fót, Du. voet, ON fótr, m. *foot'; Li. pedà, f. ‘sole, pace, foot- measure’; péde, pédZià, f. (stand, base’; pl. *stilts); -pedis, adj. (“*-fooP in cpds.); (o-gde in) pádas, m. “sole; threshing-floor; oven floor’; Latv. pēda, f. ‘sole, footstep, track’; pec, prp. (for *pēds 'after); (o-gde in) pads, m. ‘floor. Verbal extns. in Av. paióye(imi), v. *go'; Hitt. pedahi, v. ‘fetch’; Gk. pedáo, v. ffet- ter beside o-pédéo, v. (false ‘Doric’: opadéo) (follow, attend’, if for *soqu-ped-); ON feta, sv. 3 ‘step’ beside fzeta (here?) “have dealings with’; OHG cf. gi-fezzan, v. “collapse, decay’;
12573:pedes, pedesi, pedos(i), pedoi, etc. adv. see ped-, pēd- for variants Hitt. pedesi “on the spot’; Lat. pedes ‘on foot’
12575:pedol-, pedul- ‘fetter, bond, thong’. Cf. ped-, péd- and pod-. (Var. pedil-) Hitt. petulas, petuliyas ‘noose, loop’; Gk. (variant) pedilon ‘shoe, sandal, fetter, fetlock'; Lat. cf. pedülis, adj. 'foot-; MIr. íall, Ir. iall, gs: éille, f. (thong, fr. *pedla); OHG fezzil, m. (G Fessel, f. ‘fetter, shackle’); OE fetel, m. ‘belt; ME fetel, s. ‘strap’; ON fetill, pl: fetlar, m. ‘strap, thong’ (all Gmc. forms from *podil-); cf. also EME to fettle, v. ‘tackle — a job’; Li. pëdulas, adj. ‘flat-footed, broad- footed'
12605:pékstis, ios (form of *pedsqui-? cf. pedese- qu-) Ober, pasti$, m. ‘infantryman’; OCz. pěš, adj. ‘pedestrian’; R pé&3ij, id.; Cz. pěší, adj. 'infan- try-; cf. R péS$kóm, Cz. pěšky “on foot: Li. pekscias, adj. *foot-, infantry- beside pēsčias, id.; pesciom(is), adv. “on foot
13288:pod-, pód- radical: “foot: ground, base’. See ped-, pods and the following
=== LAT peior pessimus ===
31366:y est phonetiquement altere. L'explication de peierdre par peior
35942:paratif et le superlatif sont empruntes a une autrer acine; -r. peior.
46224:pessimus
46255:peior ( c.-A-d. piiior), -oris, n.pelus ad j . comp .: pire, plusmauvais.
46256:pessimus (pessu-),- a, -um superi.: le pire, le plus ou trbs mau-
46258:6367,6440 pessimus. L' e de peior est bref de nature, et c'est la
=== SKT dispatch ===
5176:Dispatch :  see  Pedal.
13599:despatch,  dispatch.  (F.-Ll  1^ orig.  sense  was  *to  remove  a  hbdrans. Better  speUiiig,  despatch ^Q.  F.  dupKhA (F.  dJp^cher\  to  hasten,  despatch. -0.^ des'  (L.  dis-\  apart,  away;  -pe. hinder.  This  O.  F.  -pescher despesckir  Coldest  form  despci.k impescher,  answering  to  l^w  L. care*  and  impediraref  of  whicti occurs  with  the  sense  *  to  put  liini the  way;*  both  from  L.  peJict^  • clog,  which  is  from  L„ped;  stem  offK foot.     See  impeach  (below).
```


## [2026-09-07T20:49:36.890Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== WLD Bd2 parvata/parvan ===\"\ngrep -n \"parvata\\|parvan\" incoming/WLD/WLD_Bd2_pages.txt incoming/WLD/WLD_Bd1_pages.txt WLD_band3.txt 2>/dev/null | head -10\necho \"=== POK parvata ===\"\ngrep -rn \"parvata\\|parvan-\" POK_01.txt POK_02.txt POK_03.txt | head -6\necho \"=== IEC parvan ===\"\ngrep -n \"parvan\\|parvata\" IEC.txt | head -6"
}
```


### [2026-09-07T20:49:36.971Z] TOOL RESULT

```
=== WLD Bd2 parvata/parvan ===
incoming/WLD/WLD_Bd2_pages.txt:2118:Hymne auf Apollo 129 „Knoten“:        parvan- n. „Knoten, Gelenk, Ab-
incoming/WLD/WLD_Bd2_pages.txt:2121:pants- n. „Knoten, Gelenk, Glied-^ (dazu scheint auch ai. parvata- m.
=== POK parvata ===
=== IEC parvan ===
```


## [2026-09-07T20:49:40.871Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nprint('\\n'.join(lines[2105:2135]))\noff=sum(len(l)+1 for l in lines[:2117])\nprint('LEAF', t[:off].count('\\f'))\nimport re\nm=re.findall(r'\\[pdf page (\\d+)\\]', t[:off])\nprint('last pdf page tag', m[-1] if m else None)\nEOF"
}
```


### [2026-09-07T20:49:42.366Z] TOOL RESULT

```
„priscu8‘^, neben der jo*Abl. as. anfnrndagnn (einmal freilich forndagitn),
ags. fyrn, firn ^priscus^' (s. Schulze KZ. 42, 93 ff.). Vgl. ai. piirand- „vor-
malig^^ zu pnrd, ap. paranam „vormals^ zu para,           Ob mit Verwendung
auf die zukiinftige Zeit ein *per-no oder per-mo- in lat. perendle „uber~
morgen^* als Loc. einer Zs. *per{i)nO’dies vorliege (Brugmann MU. VI 351 ff.
mit Lit. iiber friihere Deutungen) ist mir fraglich.
  Auf per-        in     anderer Verwendung                      weist   *per-u-)Jn-    in   horn,    jieigag
(Pind. jieigag), Ttetgarog,          att.       Tieoag, -azog        „Ausgang, Ende“, horn.          aTzeigcov
„unendlich“    =       (att.)   djiigova    *       Tiegag    jni]   eypvra Hes.,   horn. Tietgaivco,     att,
Tiegaivco   „vollende^. — Daneben eine gleichlautende, aber nach Schulze
Qu. ep.l09f., 116ff. sonderzustellende Sippe der Bed. „Knoten^; jzsigijvavre
X 175, 192      ^knotend,           kniipfend befestigende“,                 Ttetgara   fx   51,   162,   179,
Hymne auf Apollo 129 „Knoten“:        parvan- n. „Knoten, Gelenk, Ab-
                                                         ai.
schnitt, Zeitpunkt^, pdru- m. „Knoten, Gelenk, Glied (Ozean, Himmel)^^,
pants- n. „Knoten, Gelenk, Glied-^ (dazu scheint auch ai. parvata- m.
                                                                                        ,




32                                                          per-



„Berg^ zu gehoren; der Yersuch Reichelts IF, 32, 28f die Bed. durch
Yergl. m. gr. nigarog       s. u. 2    ~                   —
                                        aufzuhellen, scheitert freilich daran,
daB horn. Tiegarog uicht "^Tzegfarog^ ^perunto- sein kann, sondern Ableitung
von Tiega ist). Eine Uberbriickung der schon ursprachlichen Bedeutungs-
LEAF 35
last pdf page tag None
```


## [2026-09-07T20:49:52.948Z] TOOL CALL #71: Bash

```json
{
 "command": "ls site/pages/383.jpg 2>/dev/null || pdftoppm -f 383 -l 383 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg383 && echo done && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg383.png"
}
```


### [2026-09-07T20:49:54.300Z] TOOL RESULT

```
Exit code 2
site/pages/383.jpg
done
ls: cannot access '/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg383.png': No such file or directory
```


## [2026-09-07T20:49:56.841Z] TOOL CALL #72: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/site/pages/383.jpg"
}
```


### [2026-09-07T20:49:56.872Z] TOOL RESULT

```

```


## [2026-09-07T20:50:12.394Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"pessimism,  n\\|pejorative,  adj\\|pessimism\" KLN_1966.txt | head -5\npython3 - <<'EOF'\ndef leafof(fn, lineno):\n    t=open(fn,encoding='utf-8',errors='replace').read()\n    lines=t.split('\\n')\n    off=sum(len(l)+1 for l in lines[:lineno-1])\n    return t[:off].count('\\f')\nEOF"
}
```


### [2026-09-07T20:50:14.275Z] TOOL RESULT

```
15110:foot,  n.  —  ME.  fat,  fr.  OE.  fat,  rel.  to  OS.  fat, ON.  fa tr,  Swed.  fat,  Dan.  fad,  Du.  voet,  OHG. fuo3,  MHG.  VU03,  G.  Fuji,  Goth./o/u.s,  ‘foot’,  and cogn.  with  Ol.  pit,  acc.  pidam,  ‘foot’,  Avestic pad-,  ‘foot’,  Toch.  A  pe,  B  pai,  ‘foot’,  A  pent,  B paine,  ‘both  feet’.  Arm.  ot-n,  ‘foot’,  ot-k\  ‘feet’. Dor.  Gk.  7rtii ;,  Att.  7101)9  (formed  on  analogy  of 009,  ‘ear’),  gen.  770809,  L.  pes,  gen.  pedis,  ‘foot’, Ol.  paddm,  ‘step,  track’.  Arm.  het,  gen.  he  toy, ‘track,  footmark’,  Gk.  rtiSt),  ‘fetter’,  TreSav,  ‘to bind  with  fetters’,  7t£Sov,  ‘ground,  earth’,  h.peda, ‘footstep \pedica,  ‘shackle,  fetter’,  impedire,  ‘en¬ tangle,  ensnare’,  expedire,  ‘to  extricate,  disen¬ gage’,  Lith.  peda,  ‘footstep,  trace’,  OSlav.  podii, ‘loft’,  Russ,  pod-oshva,  ‘sole  of  foot’.  All  these words  derive  fr.  I.-E.  base  *pdd-,  *pid-,  ‘foot’. Cp.  fetch,  fetlock,  fetter,  fit,  ‘part  of  a  song’.  Cp. also  antipodes,  apod,  babouche,  biped,  breviped, caliber,  cap-a-pie,  charpoy,  expedient,  expedite, impeach,  impede,  impedimenta.  Lycopodium, millepede,  multiped(e),  octopus,  oppidan,  palmi¬ ped,  pawn  (in  chess),  parallelepiped,  pajama, pedal,  pedate,  -pede,  pedesis,  pedestal,  Pedetes, pedicel,  pedicle,  pedigree,  pedology,  ‘the  study  of soils’,  peduncle,  peon,  pes,  petiole,  pew,  Peziza, pie,  ‘a  small  coin’,  piepoudre,  pilot,  podagra, podal,  podium,  podo-,  pug,  ‘footprint’,  puy,  seer- paw,  Taliped,  Tarsipes,  teapoy,  trapezium,  triped, tripos,  vamp,  ‘front  part  of  the  foot’,  velocipede. Cp.  also  pejorative,  pessimism.
27887:spring’,  is  folk  etymology, pegmatite,  n.,  a  coarse  granite  rock  ( geol .)  —  F., coined  by  the  French  mineralogist  Rene-Just Haiiy  (1743-1822),  fr.  Gk.  7trjYp.a,  gen.  nipf- [xaTop,  ‘something  fastened  together’,  from  the stem  of  7TY]YvuvaL,  ‘to  make  firm’,  fr.  I.-E.  base * pag -,  *pdk-,  ‘to  join  together’.  See  pact  and words  there  referred  to  and  cp.  esp.  parapegm. For  the  ending  see  subst.  suff.  -ite. pegomancy,  n.,  divination  by  fountains.  —  Com¬ pounded  of  Gk.  7nr]Y7),  ‘fountain,  spring’,  which is  of  uncertain  origin,  and  fxavTEioi,  ponma, ‘oracle,  divination’,  for  which  see  -mancy. peignoir,  n.,  lady's  loose  robe.  —  F.,  fr.  peigner, ‘to  comb  the  hair',  fr.  peigne,  ‘comb’,  fr.  L.  pec- linem,  acc.  of  pecten,  ‘comb’.  See  pecten. pejorate,  tr.  v.,  to  depreciate.  —  Late  L.  pejordtus, pp.  of  pejordre,  ‘to  make  worse’.  See  pejorative. Derivative:  pejorat-ion,  n. pejoration,  n.,  depreciation.  —  Formed  with  suff. -ation  fr.  L.  pejor,  ‘worse’.  See  next  word. Derivative:  pejoration-ist,  n. pejorative,  adj.',  depreciative,  disparaging.  — Formed  with  suff.  -ive  fr.  L.  pejordtus,  pp.  of
27888:pejordre,  ‘to  make  worse’,  fr.  pejor,  ‘worse’, which  stands  for  *ped-yos  and  is  rel.  to  L.  pessi- mus,  ‘worst’  (for  *ped-semos ;  see  pessimism), and  to  pessum,  ‘downward,  to  the  ground’,  and cogn.  with  OI.  padyate,  ‘falls’;  from  the  same base  as  L.  pes,  gen.  pedis,  ‘foot’  (see  Walde- Hofmann,  LEW.,  II,  p.  275  s.v.  peior,  p.  296  s.v. pessum,  and  p.  295  s.v.  pes).  See  foot  and  cp. impair.  For  the  ending  see  suff.  -ive.
28346:pessimism,  n.,  1)  in  philosophy,  a)  the  doctrine that  this  world  is  the  worst  possible  world;  b) the  belief  that  the  evil  in  life  outweighs  the good;  2)  the  tendency  to  take  the  worst  view  of things.  —  Fr.  L .  pessimus,  ‘worst’,  which  stands for  *ped-ss mos,  and  is  rel.  to  pejor  (for  *ped- yds),  ‘worse’.  See  pejorative  and  cp.  words  there referred  to.  The  word  pessimism  was  first  used by  Coleridge.
```


## [2026-09-07T20:50:20.883Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor ln in (15110,26951,27887,28346):\n    off=sum(len(l)+1 for l in lines[:ln-1])\n    print(ln,'leaf',t[:off].count('\\f'))\nEOF"
}
```


### [2026-09-07T20:50:23.185Z] TOOL RESULT

```
15110 leaf 330
26951 leaf 594
27887 leaf 613
28346 leaf 622
```


## [2026-09-07T20:50:33.869Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HUB ===\"\ngrep -n \"paik\\|piyade\\|pijade\\|pä, päi\\|päd-\" HUB.txt | head -10\necho \"=== HRN paik/pijade ===\"\ngrep -n \"paik\\|pijade\\|pijäde\" HRN.txt | head -10"
}
```


### [2026-09-07T20:50:33.931Z] TOOL RESULT

```
=== HUB ===
1550:Alexanderroman p. 14, arab. /ai/, phi. paik West,
1551:Pahl. Texts II, 280, plur. paikan Yatk. i. Zar. p. 50,
1554:prakr. paikka-. Fiir das Altpersische ist mit Horn
4335:patkar = np. paikar; phi. pacen = arm. patcen;
4552:'Schimmel*; patker *Bild' = np. paikar; -ker 'machend' (2. Glied
6777:phi. patrahan oder perahan? (siehe oben p. 45); paikar^
6779:Ind. 93; paikar *Bild', phi. patkar, syr. N^IDPS, arm. patker
6780:(5. Jhd.), ap. patikara-] paikan 'Pfeil', arm. patkandaran
7084:syr. W^B, phi. paik, arm. payik, skr. padika- (s. oben p. 45
8494:paikar 'Kampf* = phi. patkar, arm. paiKar (5. Jhd.); pai-
=== HRN paik/pijade ===
255:(Monatsber. BAW. 1879, 463), paikka- Tussoldat' zu np.
3402:aw. paiti -\- [/kan- (?); arm. LW. paikan\daran
```


## [2026-09-07T20:50:39.161Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '1540,1560p' HUB.txt\necho \"---- 7080-7090\"\nsed -n '7080,7090p' HUB.txt\necho \"---- HRN 250-260\"\nsed -n '248,262p' HRN.txt\npython3 - <<'EOF'\nt=open('HUB.txt',encoding='utf-8',errors='replace').read(); lines=t.split('\\n')\nfor ln in (1550,7084):\n    off=sum(len(l)+1 for l in lines[:ln-1]); print('HUB',ln,'leaf',t[:off].count('\\f'),'-> p.',t[:off].count('\\f')-10)\nt=open('HRN.txt',encoding='utf-8',errors='replace').read(); lines=t.split('\\n')\nfor ln in (255,):\n    off=sum(len(l)+1 for l in lines[:ln-1]); print('HRN',ln,'leaf',t[:off].count('\\f'),'-> p.',t[:off].count('\\f')-21)\nEOF"
}
```


### [2026-09-07T20:50:40.451Z] TOOL RESULT

```
356. Np. pes Vor' = paz. phi. pSs (61. and Ind. 113—114)
^= bal. pSs = arm. pBS- (in Lehnwortern) ist jeden-
falls nicht = ap. pati§, Dass auch kein Grund vor-
handen ist, np. piS- auf ap. patis zuriickzufuhren, ist
oben Nr. 312—314 gezeigt. Nach np. paskam = arm.
patskamh = zd. ^paiti'skemba- (oben Nr. 314) soUte
man np. pas- fiir ap. patis- (in Comp.) erwarten. —
Np. pi^x^ar hat seiner Bedeutung nach nichts mit
dem angefiihrten phi. pati§x^ar zu thun.
359. Np. paig Tussganger = syr. N3^£> Noldeke,
Alexanderroman p. 14, arab. /ai/, phi. paik West,
Pahl. Texts II, 280, plur. paikan Yatk. i. Zar. p. 50,
*) *A long robe, a shirt or shift*.— 46 —
Anm. 14, arm. LW. payilc, skr. padika- Tussganger ,
prakr. paikka-. Fiir das Altpersische ist mit Horn
^padika- anzusetzen.
360. Phi. patMrUan „K5cher" ? Soil heissen *kampfen'.
365. Wenn Horn paz. pey (lies ply oder pig) = phi. pig
Oder pik (Shk. 263) = bal. pig^ nb. ply mit Recht auf
*plvaka- zuriickfiihrt, kann doch np. pth = paz. pih
= phi. pih (Shk. 264) auf zd. pfvah-^ skr. ptvas- Tett*
---- 7080-7090
mU Min. Gl. 140, g. frnd, bal. mUd^ mid, nb. mldy also ap.
*muda' ? ; sSi 'Gatte = ap. *xSauSa- ? ; maig *Heuschrecke
(neben malax) = phi. maig (und malak Bdh. 47, 10), bal.
maday, madax, arm. marax, zd. mataxd-; patg *Bote* =
syr. W^B, phi. paik, arm. payik, skr. padika- (s. oben p. 45
— 46)Vjp»y^rfa *Pussganger' = skr. paddti-y padatika-; miyan
'Mitte' = paz. phi. miyan, zd. maiSyqna^ ; bayd, bayog 'Braut'
= skr. vadhu^; beva 'Wittwe == phi. vevak, zd. Mava,
skr. vidhavd-; zBr unten* = paz. ai-er, phi. Sr- in Srtany
Ertkan PPGl. p. 9 aus "^ayar = zd. adairi (s. § 58, b)';
drdstan *in Ordnung bringen, schmticken', pr. arayam, pai-
---- HRN 250-260
lands vollständig unzugängliche Schriften und Aufsätze anführt —
stammen teils aus eigenen Aufzeichnungen des Herausgebers, teils von
einem Mitgliede dieses Judenstammes. Das beigefügte Glossar enthält
ca. 2000 Worte; da Prof. Miller selbst eine sprachliche Untersuchung
über den Dialekt ankündigt, so verzichte ich darauf, hier einige Be-
obachtungen über denselben mitzuteilen.— XII —
hier noch nach: handi- 'Gefangener zu np. hende, No. 230
(Monatsber. BAW. 1879, 463), paikka- Tussoldat' zu np.
pelf/, No. 359 (Goldschmid t ib. 922), und divira-
'Schreiber zu np. dehir, No. 540 (ib. 463). Die meisten
indischen Lehnworte in den PärasTprakä9as erscheinen in
sehr jungen Formen, so dass sich ihre Erwähnung nicht
verlohnt hätte; ganz dasselbe gilt auch von den Formen
neupersischer Worte in den portugiesischen Reiseberichten
(Lendas da India, herausgegeben von Gaspar Correa, Lisboa
HUB 1550 leaf 55 -> p. 45
HUB 7084 leaf 210 -> p. 200
HRN 255 leaf 17 -> p. -4
```


## [2026-09-07T20:50:59.596Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"heel\" HENNING_selected_papers.txt | head -20"
}
```


### [2026-09-07T20:50:59.659Z] TOOL RESULT

```
4244:« spinning-wheel, s0 tha
4334:rolling wheel the small ones like the head of the domesticated ‘ox? The moon is the size of a mccoourss of two hddras, each geographical Ad0ra being about as much as a parasang of average length.* The sun is the size of Bran-vé,
6518:sin = weapons, P7, 152; P13, 16; Man. ayy M133 V ii,1; M 6000 Lo, Hardly hero = saddle (as Pers. eis) which in Sogd. ie pyrbn., P 13, 6, from parid{hyina- = Persian pilin“ packsadale", ef. Pers. pllad’ (sho, wrongly, blldd) "'n (packhorse " from *parid(hja.. "The reduction of -Bin to -Ban in normal in Sogdian ; ef also Wakhi paden, pidn " endl", Morgenatiore, 117. i, 538 (from *pdrden 1}. Note that ayrh VJ. 770, Dhuta 18, P 6, 138, i“ wheel", not " (the remark on yeh is atruck out in th copy of his paper in J. 1996, | (p. 228), M. E. Benveniste very kindly sent me)
10792:» putpenp'y ‘ese, Sb, 771, mast mean abe pred the wheel, ‘This reveals « rot of five consonants, (fret) syop, of at ast four, ayes, if -ap- = bs developed from aa orgial ms Hence compare Pablsalm, dahm(jah, and’ Vida
14642:many puzzling points; nevertheless one cannot help wishing Mani had n himself a little wax model of the world and kept it by his side and looked ralling subjects-as the Right ree Wheels, the Seven Great Columns, the
14777:and king over all the ten Firmamen Then, below the ten Firmaments, they fashioned rolling wheel and (sid)
14798:Tn the low it, Two Sons of G the Superior Wheel cont
14914:raps) of the five wheel of the sp
14915:ments or Wheels of wind, mined the elemental spheres
14969:honoris, to which a whole chapter devoted, wheel" mw phere” (as was done by A. Bdhli
14993:wheel that lies in front of the R Kephalaia (xxxvi, yp. 87 8q.) is confused with the “wheel of the tents, Keph f the
15014:nro (cf. Keph, 8, 31, ° the wheel is like
15022:P 8, 107, of a pB"k = palé, else wheel ” is mentioned in the Paalo-b Splenditenens (cf. ibid., 198, 98, " the Rez h of Light”); it is doubtful whether ’skyeyg ezr- ‘superior wheel " (Lit, “hi lying whe tet (the parallel passage qu against it). Now, if it is o
15036:word. I had considered “ wheel ", mi
18675:2 Fr, Mller thecry that the at an invontion of the authors of the Frabang’ (ef. Geiger, WZKAM, 9 Auld be coneMdered sericaaly. A comoposnd form "E “‘ne fs not know to Pala: {hat it should stand for @ (from Ze) i hardly pooibe. yt, of course, might be rl ‘dhorny ch eg. Wakhi verin-+ wordt. “to shear” (Morgeostierse, Indorran, Frost Lang. ti. 0), B burridan,theelore “coceshorn”, “iwice- shorn, ee
21146:che rubbed» (Bal. muiag etc.), Pk'ry- «to paint» (ef, Pers. nigar); Sw'ewvoice » (cf. AV. fravaka-), Snsyd whe went astray », Sntyk «astra n'syd (franas-, franasta-), Sw2d «he jumped», caus. impf. Sw'Ey- «throw» (fra-waz-) sbw'k «pure» (fracpawaka-), cf. also #8 «nine» if from frdd- «increase» (the only aberrant numeral of Khwar.; 90» is mwyc, «19» mw’dys). In addition, there are a few cases where one suspects that fr- has become r-, €.g. rand «insult» rxy’ occur», cf. ‘rs'wyk «pumice» (fra-siw-?) and p'er'wydh «he recalled it» (Sogd. pyBr'w-); that this change existed in a Khw. di by Beruni’s ren (rawacina) = Av. fravasingm. — xr remains in the middle of a word, txryk «bitter», cxyr «wheel, but loses -r- at the beginning of roots, xn- «buy», sxm- «ransom» (Sogd. syr'yn-), p'cx'wd- «he scratched» (BSOS., X, 509); doubtful is the occurrence of -rx in p'rxw0d whe became lost, giddy, dazzled», possibly from apa + Av. xraoda- (ef, the met
21479:audience by Shapur, was accompanied by two of his disciples, which pre~ supposes that he had begun his mission before and had acquired followers, Further, Ibn anNadim, quoting Manichacan sources, states* that before his meeting with Shapur Mani had travelled about in various countries; that he had converted Shapur’s brother Pérdz to his creed, evidently in the course of his journeys, perhaps in Khorasan und Kishin where he was governor; and that Pérd “caused him to come to Shapur"’. On the heels of that report,* under the heading ‘'the Manichaeans say’"—the very heading that had introduced also the report of Mani’s ‘coming out” on the day of Shapur's coronation (plainly both are derived from one and the sume
24874:volume of the Trudi Xoresmkoy Arxeologo-Etnografideshoy Ehspedici (1958) two of the leather documents and a single specimen of the wooden tablets ( = Toprag-g. No. 10) were published (pp. 208 sqq.), accompanied by unsatisfactory reproductions (fig. 97) ‘They were re-published, with improved readings and reproductions, in S. P. Tolatov, Po drevnim del'tam Oksa i Yaksarta, 1962, 217 sqq., where a second wooden tablet (= Toprag- @. No. 8) is added; it isa misfortune that in the illustration this important document has been so strongly reduced that some of the letters can no longer be distinguished with assurance. In the same book there is a reference toa fresh find of documents at a fort called Yakke-Parzan, p. 257, and one of them, containing the beginnings of seven lines, is reproduced, fig. 165; those documents are attributed, on unknown grounds, to the 8th century. (3) The ossuary inscriptions of Tog-gal'a, One notes with gratification that, thanks to the infusion of fresh blood into Soviet Choresmian studies, their publication has been tackled on the heels of their discovery; they were found as recently as 1962. In an article by S. P. Tolstov and V. A. Livshite that appeared in Sovetskaya Etnografiya 1964, 2, 50-69, nine of those scriptions are edited; an English version, printed in the Acta Antiqua Ac, Sc. Hung., xii, 1964, 231-251, is provided with a plate that is wholly satisfactory.4 At the same time the excavator of the site, A. V. Gudkova, published a report (Tok-kala, Tashkent 1964) which on seventeen plates brings an additional mass of material It is a great pity that Mme Gud- kova's noble effort at thus making the material readily usable has been partly spoiled in the printing, by selection of too wide a “screen”, which blurs the delicate distinctions of letters, severs connected letters, and even causes them to disappear without trace on occasion. Many of the ossuary
```


## [2026-09-07T20:51:01.130Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^ *S W \\|S W = \\|SW =\\|Sogdian Loanwords\\|Loanwords\" SOD_pages.txt | head -10\ngrep -n \"BSOAS 10\\|BSOS 10\\|SLW\" SOD_pages.txt | head -10"
}
```


### [2026-09-07T20:51:01.657Z] TOOL RESULT

```
25298:                                                                   S W apud. Mack. AI 25, 428 n 16; C2 p51 n 5
35210:          S W R 207; GMS 232; KG 550, 572, 3sg. impf.
20829:           Hen. BSOAS 10, 102; BBB 59                                        nmW, VJ 470
20854:           GMS 1063; Hen. BSOAS 10, 102 n 4, 11, 74.14;
```


## [2026-09-07T20:51:13.052Z] TOOL CALL #79: WebSearch

```json
{
 "query": "Henning \"Sogdian loan-words in New Persian\" 1939 list \"pal\" heel Persian پل"
}
```


### [2026-09-07T20:51:22.031Z] TOOL RESULT

```
Web search results for query: "Henning "Sogdian loan-words in New Persian" 1939 list "pal" heel Persian پل"

Links: [{"title":"SOGDIAN LANGUAGE ii. Loanwords in Persian - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/sodgian-language-i-loanwords/"},{"title":"Sogdian Loan-words in New Persian | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Sogdian-Loan-words-in-New-Persian-Henning/96f750fcd406f9dc986286dcda90e927701ea0ef"},{"title":"Sogdian Loan-words in New Persian - Walter Beresford Henning - كتب Google","url":"https://books.google.com.sa/books/about/Sogdian_Loan_words_in_New_Persian.html?id=L2ufPgAACAAJ&redir_esc=y"},{"title":"Bactrian Loanwords in New-Persian","url":"https://languagestudy.ihcs.ac.ir/article_451.html?lang=en"},{"title":"(PDF) The Myth of Sogdian Lambdacism","url":"https://www.academia.edu/35344474/The_Myth_of_Sogdian_Lambdacism"},{"title":"Sogdian Loan-words in New Persian | Bulletin of SOAS | Cambridge Core","url":"https://www.cambridge.org/core/services/aop-cambridge-core/content/view/2CE640EC43EF3DF612D3B344626E0FE6/S0041977X00068245a.pdf/sogdian-loan-words-in-new-persian.pdf"},{"title":"Bulletin of SOAS: Volume 10 - Issue 1 | Cambridge Core","url":"https://www.cambridge.org/core/journals/bulletin-of-the-school-of-oriental-and-african-studies/issue/155ADC7707C4BB820BC41D6770CA0D27"}]

Based on the search results, I found relevant information about Henning's work on Sogdian loanwords in Persian. Most examples in the lists about Sogdian loanwords are first mentioned in Henning, 1939. The work was published in the Bulletin of the School of Oriental and African Studies in 1940, volume 10, pages 93-106.

Regarding the specific word "pal" (پل - "bridge" or "heel"), the search results show that pālik meaning "shoes" is mentioned in Henning, 1939, page 99, and there are also references to other l-containing words that represent Sogdian loans where Persian words containing an /l/ can be considered as Sogdian loans, if this l represents Sogdian /δ/.

The search results also reference Henning's postulation that in most Sogdian dialects, Old Iranian d (δ) and θ had merged into one sound which was very near to l in West Iranian.

However, the search results do not contain the complete list or specific details about "pal" (پل) with the meaning you're asking about. To access the full article with all the examples from Henning's 1939 work, you would need to consult the original publication directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-07T20:51:28.950Z] TOOL CALL #80: WebFetch

```json
{
 "url": "https://www.cambridge.org/core/services/aop-cambridge-core/content/view/2CE640EC43EF3DF612D3B344626E0FE6/S0041977X00068245a.pdf/sogdian-loan-words-in-new-persian.pdf",
 "prompt": "Does this article (Henning, Sogdian Loan-words in New Persian, BSOAS 10, 1939) list Persian pal 'heel' from Sogdian pδny/paδn? Quote the passage and note the page number (around p.98)."
}
```


### [2026-09-07T20:51:30.868Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-07T20:51:34.705Z] TOOL CALL #81: WebFetch

```json
{
 "url": "https://www.iranicaonline.org/articles/sodgian-language-i-loanwords/",
 "prompt": "Does this Encyclopaedia Iranica article on Sogdian loanwords in Persian mention Persian pal 'heel' (from Sogdian paδn/pδny)? What does it say about the l ~ δ criterion and cite Henning 1939?"
}
```


### [2026-09-07T20:51:36.164Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-07T20:51:46.073Z] TOOL CALL #82: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/p%E1%B9%93ds",
 "prompt": "PIE *pṓds 'foot': what descendants and derived terms are listed (Latin pēs, Greek pous, Sanskrit pad-, Avestan/Old Persian, Proto-Iranian *pā́dah)? Any mention of *ped-yos/pessimus?"
}
```


## [2026-09-07T20:51:47.194Z] TOOL CALL #83: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/dispatch",
 "prompt": "Etymology of dispatch: is it traced to Latin pedica / ped- 'foot', or to something else? Quote."
}
```


### [2026-09-07T20:51:52.161Z] TOOL RESULT

```
# PIE *pṓds Descendants and Derived Terms

Based on the Wiktionary article, the following descendants are listed:

**Direct descendants include:**
- Proto-Albanian, Armenian, Anatolian languages (Hittite, Lycian, Luwian)
- Proto-Celtic, Proto-Germanic, Hellenic (Ancient Greek πούς)
- Proto-Indo-Iranian, Proto-Italic, Proto-Tocharian

**Specific modern language examples:**
- Greek: πόδι (pódi)
- Albanian: përposh, poshtë
- Tocharian A: pe; Tocharian B: paiyye

**Derived terms listed:**
The article mentions "*h₁pōs-pṓds" as a derived compound, with descendants in Proto-Balto-Slavic (Latvian papēdis, Latgalian papīds).

**Regarding your specific question:** The article does not mention "*ped-yos" or "pessimus" (the Latin superlative form). The Latin descendant is listed under "Proto-Italic: *pets" but no further details about Latin derivatives appear in this reconstruction entry.
```


### [2026-09-07T20:51:52.359Z] TOOL RESULT

```
# Etymology of "Dispatch" and the Latin "Ped-" Connection

According to the Online Etymology Dictionary, the exact origin of "dispatch" is uncertain. The word comes from Spanish *despachar* or Italian *dispacciare*, but scholars disagree about the second element's source.

One proposal connects it to Latin *-pedicare* meaning "to entrap," which derives from Latin *pedica* ("shackle"), ultimately linked to *ped-* meaning "foot." As the source states: "Another says it is Latin *-pedicare* 'to entrap' (from Latin *pedica* 'shackle'..."

However, this remains speculative. The entry notes that "its exact source and meaning is uncertain" and references the OED for a fuller discussion. So while a connection to the Latin foot-related root *ped-* has been proposed, it represents one theory among several rather than a confirmed etymology.
```


## [2026-09-07T20:51:57.680Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/p%E1%B9%93ds' --note 'page 383, root Ped/Pod: PIE *pods foot, descendants' 2>&1 | tail -1\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/dispatch' --note 'page 383, node 11: dispatch < Sp/It, second element possibly L. pedica < ped-; uncertain' 2>&1 | tail -1"
}
```


### [2026-09-07T20:51:59.712Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/4a56fc6c970348e1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c0b74b44c0ff55ce.txt
```


## [2026-09-07T20:52:02.559Z] TOOL CALL #85: Bash

```json
{
 "command": "sed -n '1,120p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-07T20:52:02.598Z] TOOL RESULT

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


## [2026-09-07T20:59:13.501Z] TOOL CALL #86: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-383.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW_PZ = \"https://en.wiktionary.org/wiki/%D9%BE%DA%98%D9%88%D8%A7%DA%A9\"\nW_PAYK = \"https://en.wiktionary.org/wiki/%D9%BE%DB%8C%DA%A9\"\nW_PAY = \"https://en.wiktionary.org/wiki/%D9%BE%D8%A7%DB%8C\"\nW_PIY = \"https://en.wiktionary.org/wiki/%D9%BE%DB%8C%D8%A7%D8%AF%D9%87\"\nE_PAJ = \"https://www.etymonline.com/word/pajamas\"\nE_DIS = \"https://www.etymonline.com/word/dispatch\"\nAB_PZ = \"https://abadis.ir/fatofa/%D9%BE%DA%98%D9%88%D8%A7%DA%A9/\"\nW_PODS = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/p%E1%B9%93ds\"\n\ndoc = {\n \"pdf_page\": 383,\n \"book_page\": 353,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-07\",\n \"entries\": [\n\n # ---------------- entry 0 : Parvan / Parvata ----------------\n {\n  \"entry\": 0,\n  \"root\": \"Parvan, Parvata\",\n  \"verdict\": \"confirmed\",\n  \"modern_form\": \"Sanskrit parvan- n. 'knot, joint, section' → adj./n. parvata- 'knotty, rugged; mountain'\",\n  \"note\": \"The root box is exactly right. Buck (SYN) p.26, §1.22 'mountain': \\\"Skt. parvata- 'mountain, mountain range, rock', Av. paurvata- 'mountain range', fr. adj. Skt. parvata- 'knotty, rugged', fr. parvan- 'knot'\\\" — the language label (Sanskrit), both forms and both glosses are Nourai's source verbatim. Walde-Pokorny II 31 f. (under *per-) has the same: \\\"ai. parvan- n. 'Knoten, Gelenk, Abschnitt, Zeitpunkt', páru- m. 'Knoten, Gelenk, Glied', parus- n. ... (dazu scheint auch ai. parvata- m. 'Berg' zu gehören)\\\". Pokorny has no separate parvan- headword, so SYN/WLD are the standard here. What is NOT confirmed is the use Nourai makes of the root on this page: the Persian branch (paž, pâpaž, pažvâk) does not follow from it — see the node comments.\",\n  \"note_fa\": \"ریشهٔ سنسکریت parvan- «گره، بند، مفصل» و صفت/اسم parvata- «گره‌دار، ناهموار؛ کوه» درست است. باک (فرهنگ مترادف‌های هندواروپایی، ص ۲۶) دقیقاً همین را می‌گوید: parvata- سنسکریت «کوه، رشته‌کوه» از صفت parvata- «گره‌دار، ناهموار» از parvan- «گره»، و اوستایی paurvata- «رشته‌کوه» هم‌ریشهٔ آن است. والده-پوکورنی (جلد ۲، ص ۳۱–۳۲) نیز parvata- را ذیل *per- به parvan- می‌بندد. پس عنوان ریشه، نام زبان و معنی، هر سه درست است؛ اما شاخهٔ فارسیِ این نمودار (پژ، پاپژ، پژواک) از آن برنمی‌آید (نگاه کنید به یادداشت گره‌ها).\",\n  \"sources\": [],\n  \"ref_check\": [\n   {\"ref\": \"SYN:26\", \"status\": \"supports\", \"note\": \"Buck, A Dictionary of Selected Synonyms, p.26 (SYN.txt \\\\f-leaf 51, §1.22 MOUNTAIN, HILL): 'Skt. parvata- \\\"mountain, mountain range, rock\\\", Av. paurvata- \\\"mountain range\\\", fr. adj. Skt. parvata- \\\"knotty, rugged\\\", fr. parvan- \\\"knot\\\"'. Nourai's root box is a direct transcript of this sentence.\"}\n  ],\n  \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. II pp. 31-32, s.v. per- (WLD_Bd2_pages.txt leaf 35)\", \"stance\": \"supports\", \"note\": \"'ai. parvan- n. \\\"Knoten, Gelenk, Abschnitt, Zeitpunkt\\\", pdru- m. \\\"Knoten, Gelenk, Glied\\\", parus- n. \\\"Knoten, Gelenk, Glied\\\" (dazu scheint auch ai. parvata- m. \\\"Berg\\\" zu gehören)' — knot > mountain, exactly Nourai's root.\"},\n   {\"src\": \"POK\", \"where\": \"grep 'parvata|parvan-' over POK_01/02/03\", \"stance\": \"silent\", \"note\": \"Pokorny's IEW has no parvan-/parvata- headword; the material is only in Walde-Pokorny II 31 f. So Nourai's choice of SYN as the reference is the right one.\"},\n   {\"src\": \"SYN\", \"where\": \"p.24 word-table of §1.22\", \"stance\": \"supports\", \"note\": \"The synoptic table on p.24 lists 'Skt. giri-, parvata-, acala-, etc.' and 'Av. gairi-, paurvata, barazah-, OPers. kaufa' — paurvata is a recognised Avestan word for a mountain range.\"}\n  ],\n  \"nodes\": [\n   {\n    \"id\": 1,\n    \"lang\": \"Avestan\",\n    \"words\": \"paurvatâ; paurvatâ-vac\",\n    \"verdict\": \"plausible\",\n    \"derivation\": \"paurvatā- is real: Bartholomae, Altiranisches Wörterbuch, s.v. 'paurvatā- f. \\\"Bergzug, -kette, Gebirg\\\"', attested Yt.19.3 (dva hamankuna aēte, 'the two H. mountains') and Y.10.11 (āat āhva paurvatāhva pouru.sarǝδǝs vīraδahe), with the express comparison 'ai. vgl. parvata- m.' It is the regular Avestan cognate of Skt. parvata-: Indo-Iranian *parvatā- keeps -rv- in Avestan, where Old Iranian a before r + consonant is frequently written au (paurva- 'first'), hence paurvatā- beside Skt. parvata-. So the arrow Skt. parvan-/parvata- → Av. paurvatā- is a cognate/parallel-formation relation, correctly drawn, and Buck states it in the very page Nourai cites. The second word, paurvatā-vac 'sound of mountains, echo', is NOT an Avestan word: it does not appear in Bartholomae (the only compounds of paurvatā- are the mountain names), nor in Buck. It is Nourai's own back-formation, built to serve the Persian pažvāk below; the second element vāc- 'voice' is of course genuine Avestan (his ☞Wekw pointer is right, PIE *wekʷ- 'speak'), but the compound is unattested.\",\n    \"derivation_fa\": \"واژهٔ اوستایی paurvatā- «رشته‌کوه، کوهستان» واقعی است: بارتولومه در فرهنگ ایرانی باستان ذیل paurvatā- آن را «Bergzug, -kette, Gebirg» معنی می‌کند و شاهدهای یشت ۱۹٫۳ و یسنا ۱۰٫۱۱ را می‌آورد و خود به «قس سنسکریت parvata-» ارجاع می‌دهد؛ پس این واژه هم‌ریشهٔ parvata- سنسکریت است (در اوستایی a پیش از r + همخوان بارها au نوشته می‌شود، مانند paurva- «نخستین»). اما ترکیب paurvatā-vac «آوای کوه‌ها، پژواک» در هیچ متن اوستایی و در فرهنگ بارتولومه نیامده؛ این ساختِ خودِ نورایی است تا «پژواک» فارسی را از آن بگیرد. جزء دوم یعنی vāc- «آوا» البته اوستایی راستین و از ریشهٔ هندواروپایی *wekʷ- است (ارجاع ☞Wekw او درست است)، ولی خودِ ترکیب گواهی ندارد.\",\n    \"sources\": [],\n    \"ref_check\": [\n     {\"ref\": \"SYN:26\", \"status\": \"supports\", \"note\": \"Buck p.26: 'Av. paurvata- \\\"mountain range\\\"' listed beside Skt. parvata-; supports the Avestan word but says nothing about a compound with vāc-.\"},\n     {\"ref\": \"BQT:401\", \"status\": \"partial\", \"note\": \"Borhan-e Qate' vol.1 printed p.401 (BQT_v1_pages.txt \\\\f-leaf 625, offset leaf-224 fixed by the 'بقیهٔ در صفحهٔ ۴۰۰' catch-line on leaf 623) is the پژواک entry: 'چون در کوه و گنبد باواز بلند چیزی بگویند در جواب همان را شنوند و آن را بعربی صدا خوانند' — it defines the echo but the OCR of Mo'in's footnotes on that page shows only cross-references (رك: پژولیدن etc.), no Avestan paurvatā-vāc.\"}\n    ],\n    \"consulted\": [\n     {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch s.v. paurvatā- (BRT.txt line 15735, \\\\f-leaf 493)\", \"stance\": \"partial\", \"note\": \"'paurvatā- f. \\\"Bergzug, -kette, Gebirg\\\": dva hamankuna aēte (NS.) Yt.19.3; āat āhva paurvatāhva pouru.sarǝδǝs vīraδahe ... Y.10.11. ai. vgl. parvata- m.' — the noun is confirmed; no compound *paurvatā-vac- exists in the dictionary.\"},\n     {\"src\": \"WLD\", \"where\": \"Bd. II 31-32\", \"stance\": \"supports\", \"note\": \"Groups ai. parvata- 'Berg' with parvan- 'Knoten'; the Iranian cognate is the same formation.\"},\n     {\"src\": \"SYN\", \"where\": \"p.24 table, §1.22\", \"stance\": \"supports\", \"note\": \"'Av. gairi-, paurvata, barazah-' among the Avestan words for 'mountain'.\"}\n    ]\n   },\n   {\n    \"id\": 2,\n    \"lang\": \"Persian\",\n    \"words\": \"paž «پژ ۱»; pâpaž «پاپژ»; pažvâk, pežvâk «پژواک»\",\n    \"verdict\": \"disputed\",\n    \"derivation\": \"All three words exist, but the derivation from Avestan paurvatā- is rejected. (a) پژ paž: Borhan-e Qate' p.399 (BQT_v1_pages.txt leaf 623) has the entry 'بفتح اول و سکون ثانی، زمین پست و بلند و کوه و کتل را گویند و بعربی عقبه خوانند' with exactly Nourai's Khosravānī verse ('اگر سراسر کوه و پژ آیدش در پیش', quoted from Loghat-e Fors 178), so the word and gloss are right. Phonetically, however, Av. paurvatā- cannot give paž: Old Iranian -rv- gives NP -rv-/-hl- (paurva- > MP pahlom, NP پهلو), and -t- between vowels gives -d-/-y-, never -ž-; a regular reflex would be something like *purvad/*pahlavad, not paž. (b) پاپژ pāpaž is a Persian compound پا 'foot' + پژ 'rough ground', i.e. 'foot-hills', not a continuation of the Avestan word. (c) پژواک pažvāk/pežvāk 'echo' (Dehkhoda: 'آوازی که در کوه و گرمابه و دره و گنبد و مانند آن پیچد. صدا. آواز منعکس'; Mo'in: 'بازتاب صدا در کوه، طنین'): the second element واک 'voice' is undisputed (< Old Iranian *vāxš, PIE *wekʷ-, Nourai's ☞Wekw), but the first element is the Persian prefix پژ-/پچ-/پت- < Old Iranian *pati- 'back, in return' — the same prefix as in پژوهیدن, پاسخ, پژمردن — so پژواک = *pati-vāka- 'answering voice, sound sent back', which is both phonetically regular and semantically exact for 'echo'. Nourai's 'mountain-voice' analysis is a folk etymology encouraged by the coincidence that the standard Persian gloss mentions کوه. Wiktionary's پژواک entry gives no etymology and Mo'in/Dehkhoda give none, so nothing independent supports the paurvatā- link.\",\n    \"derivation_fa\": \"هر سه واژه در فارسی هست، اما گرفتنشان از اوستایی paurvatā- پذیرفتنی نیست. «پژ» در برهان قاطع ص ۳۹۹ آمده: «زمین پست و بلند و کوه و کتل را گویند و بعربی عقبه خوانند»، با همان بیت خسروانی که نورایی نقل کرده (از لغت فرس ۱۷۸)؛ پس واژه و معنی درست است. ولی از نظر آوایی paurvatā- اوستایی هرگز «پژ» نمی‌دهد: خوشهٔ -rv- ایرانی باستان در فارسی به -هل-/-رو- می‌رسد (paurva- < پهلو) و -t- میان‌واکه‌ای به d/y بدل می‌شود، نه به ژ؛ صورت مورد انتظار چیزی مانند *پهلود می‌بود. «پاپژ» هم ترکیب فارسی «پا + پژ» است، نه بازماندهٔ مستقیم واژهٔ اوستایی. دربارهٔ «پژواک»: جزء دوم «واک» بی‌گمان از *vāxš ایرانی باستان و ریشهٔ هندواروپایی *wekʷ- است (ارجاع ☞Wekw نورایی درست است)، ولی جزء نخست پیشوندِ پژ-/پچ-/پت- از *pati- ایرانی باستان به معنی «باز، در پاسخ» است — همان پیشوندی که در «پژوهیدن»، «پاسخ» و «پژمردن» دیده می‌شود. پس پژواک = *pati-vāka- «آوای بازگردانده»، که هم از نظر آوایی قاعده‌مند است و هم معنایش دقیقاً «انعکاس صدا». معین «بازتاب صدا در کوه، طنین» و دهخدا «آواز منعکس، عکس‌الصوت» می‌نویسند و هیچ‌یک ریشه‌ای به دست نمی‌دهند. کوتاه سخن: ادعای نورایی را پژوهش امروزی رد می‌کند و به‌جای «آوای کوه» پیشوند *pati- را می‌نشاند.\",\n    \"sources\": [W_PZ, AB_PZ],\n    \"ref_check\": [\n     {\"ref\": \"BQT:399\", \"status\": \"supports\", \"note\": \"Borhan vol.1 p.399 (leaf 623): 'پژ - بفتح اول وسکون ثانی، زمین پست و بلند و کوه و کتل را گویند، و بعربی عقبه خوانند ... اگر سراسر کوه و پژ آیدش در پیش. خسروانی «لغت فرس ۱۷۸»' — the word, the gloss and Nourai's verse, but no etymology.\"},\n     {\"ref\": \"BQT:401\", \"status\": \"partial\", \"note\": \"Borhan vol.1 p.401 (leaf 625) is the پژواک entry ('چون در کوه و گنبد باواز بلند چیزی بگویند در جواب همان را شنوند و آنرا بعربی صدا خوانند'); the surviving OCR of the footnotes on that page carries no Avestan etymon.\"},\n     {\"ref\": \"BQT:345\", \"status\": \"not_found\", \"note\": \"Printed p.345 = BQT_v1_pages.txt leaf 565 (the پا/پاپ block). The OCR of that leaf is fragmentary and no پاپژ headword survives in it; the entry is presumably there in the print but could not be read from the local text.\"}\n    ],\n    \"consulted\": [\n     {\"src\": \"MON\", \"where\": \"vajehyab/abadis, فرهنگ معین s.v. پژواک\", \"stance\": \"partial\", \"note\": \"'(پِ) (اِ.) بازتاب صدا در کوه، طنین' — meaning only; Mo'in gives no origin tag, so no support for an Avestan source.\"},\n     {\"src\": \"BQT\", \"where\": \"Dehkhoda quoting Borhan, abadis s.v. پژواک\", \"stance\": \"partial\", \"note\": \"'پژواک. [پ َژْ / پ ِژْ] (اِ) آوازی که در کوه و گرمابه و دره و گنبد و مانند آن پیچد. صدا. آواز منعکس. عکس الصوت.' — definition only, no etymology.\"},\n     {\"src\": \"HRN\", \"where\": \"grep 'pazvak|pezvak|paz ' over HRN.txt\", \"stance\": \"silent\", \"note\": \"Horn's Grundriss has no entry for پژ or پژواک.\"},\n     {\"src\": \"HUB\", \"where\": \"grep over HUB.txt\", \"stance\": \"silent\", \"note\": \"Hübschmann, Persische Studien, has no پژ/پژواک entry either.\"},\n     {\"src\": \"FRS\", \"where\": \"Loghat-e Fors, the Khosravānī verse cited by Borhan (لغت فرس ۱۷۸)\", \"stance\": \"supports\", \"note\": \"Borhan's own source for پژ is Asadi's Loghat-e Fors, i.e. the word is an old Dari one — but that says nothing about an Avestan mountain-word.\"}\n    ]\n   }\n  ]\n },\n\n # ---------------- entry 3 : Ped, Pod ----------------\n {\n  \"entry\": 3,\n  \"root\": \"Ped, Pod\",\n  \"verdict\": \"confirmed\",\n  \"modern_form\": \"PIE *ped-/*pod- (nom. *pṓds) 'foot'; also verbal 'to tread, fall'\",\n  \"note\": \"Pokorny p.790 has exactly '2. ped-, pōd- m. \\\"Fuß\\\"; Nom. Sg. pōts, Gen. ped-es/-ōs, Nom. Pl. ped-es; verbal \\\"gehen, fallen\\\"; pedo-m \\\"(Fuß)boden\\\"' — Nourai's headword, language label, gloss and page citation are all right. Watkins/AHD 'ped-1. Foot ... [Pok. 2. pēd- 790]' agrees, and adds the two branches that matter on this page: the *ped-yos/*ped-samo- comparative-superlative behind Latin peior/pessimus, and 'Middle Persian pāδ, leg, foot: PAJAMAS, TEAPOY'. Note that Pokorny's p.790 also holds '1. pēd- \\\"fassen; Gefäß\\\"' (Watkins' ped-2), an unrelated homonym; Nourai correctly takes only the 'foot' entry. This is PART 1 of the root; the Germanic (foot), Greek (pous) and further Latin branches are on the continuation page.\",\n  \"note_fa\": \"ریشهٔ هندواروپایی آغازین *ped-/*pod- «پا» درست است. پوکورنی در ص ۷۹۰ عیناً می‌نویسد: «2. ped-, pōd- m. \\\"Fuß\\\"؛ حالت فاعلی مفرد pōts، اضافی ped-es/-ōs ...؛ فعلی: رفتن، افتادن». واتکینز در پیوست ریشه‌های هندواروپایی فرهنگ American Heritage نیز ذیل ped-1 «Foot» همین ارجاع [Pok. 2. pēd- 790] را می‌آورد و دو شاخه‌ای را که در این صفحه به کار می‌آید نام می‌برد: *ped-yos / *ped-samo- که به peior و pessimus لاتینی می‌رسد، و «فارسی میانه pāy، که pajamas و teapoy انگلیسی از آن است». باید توجه داشت که در همان ص ۷۹۰ پوکورنی ریشهٔ همنامِ دیگری هم هست («1. pēd- گرفتن؛ ظرف») که ربطی به پا ندارد و نورایی درست تنها ریشهٔ «پا» را برداشته است.\",\n  \"sources\": [W_PODS],\n  \"ref_check\": [\n   {\"ref\": \"POK:790\", \"status\": \"supports\", \"note\": \"Pokorny IEW p.790 (POK_03.txt \\\\f-leaf 23, the page carrying the printed '790' marker): '2. ped-, pōd- m. \\\"Fuß\\\"; Nom. Sg. pōts, Gen. ped-es/-ōs, Nom. Pl. ped-es; verbal \\\"gehen, fallen\\\"; pedo-m \\\"(Fuß)boden\\\"'. Continues p.791 with 'ai. pād- \\\"Fuß\\\" (pāt, pādam, padáh), av. pād- ds.; apers. pādaibiyā \\\"mit den Füßen\\\" ... lat. pes, pedis'.\"}\n  ],\n  \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. ped-1 'Foot' (AHD_watkins1985.txt lines 814-819)\", \"stance\": \"supports\", \"note\": \"'ped-1. Foot. I. Nominal root ... 4. Basic form *ped- in Latin pēs (stem ped-), foot ... 9.c. Middle Persian pāδ, leg, foot: PAJAMAS, TEAPOY. II. Verbal root *ped-, to stumble, fall ... a. suffixed (comparative) form *ped-yos in Latin peior ... b. suffixed (superlative) form *ped-samo- in Latin pessimus: PESSIMISM. [Pok. 2. pēd- 790.]'\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 23 (cited by Mann as 'WP II, 23' for ped-)\", \"stance\": \"supports\", \"note\": \"Mann's IEC entry for ped- refers to WP II 23 for the same root; the Bd.2 scan is the source Pokorny 1959 reprints on p.790.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, An Indo-European Comparative Dictionary, s.v. ped-, pēd- (IEC.txt line 12562)\", \"stance\": \"supports\", \"note\": \"'ped-, pēd- \\\"foot\\\" ... Type *pēds, cons. stem, beside *pods, id., oblique: *ped-, pod- \\\"foot\\\"' with Skt. pad-, Av. paiδya-, 'Per. pay, s. \\\"foot\\\"; paye, s. \\\"ground, basis\\\"', Lat. pēs, peior.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck §4.37 'foot'\", \"stance\": \"supports\", \"note\": \"Buck treats *ped-/*pod- as the common IE word for foot across the family, the same reconstruction.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. foot (KLN_1966.txt leaf 330)\", \"stance\": \"supports\", \"note\": \"'All these words derive fr. I.-E. base *pōd-, *pēd-, \\\"foot\\\". ... Cp. also pejorative, pessimism.'\"}\n  ],\n  \"nodes\": [\n   {\n    \"id\": 1,\n    \"lang\": \"Avestan / Old Persian\",\n    \"words\": \"pâd, pâdha, pad, pada\",\n    \"verdict\": \"confirmed\",\n    \"derivation\": \"Avestan pād- 'foot' (acc. pāδǝm, gen. paδō) and its derived stem paδa- / paiδya- 'foot, footstep' continue PIE *pōd-/*ped- with the regular Iranian voicing of intervocalic -d- to -δ- (Nourai's 'pâdha' is the usual Latin-letter rendering of paδa-). Old Persian has the same pair: the strong stem in pādaibiyā 'with the two feet' (DB) and the weak stem pad- in the adverb ni-padiy 'in pursuit, on the track of' and in pati-padam 'in its place', plus the derived pāda- in the month-name Garma-pada-. Kent's lexicon lists them under '*ped- or pod- \\\"foot\\\" in ni-padiy, pati-padam, Garma-pada-, (Ar.) *pād- in pādaibiya'. So all four forms of the node are real and correctly attributed to Avestan/Old Persian.\",\n    \"derivation_fa\": \"اوستایی pād- «پا» (رایی pāδǝm، اضافی paδō) و ستاک مشتق paδa-/paiδya- «پا، گام» بازماندهٔ *pōd-/*ped- هندواروپایی‌اند؛ d ایرانی باستان میان دو واکه به δ نرم شده است و «pâdha»ی نورایی همان نگارش لاتین paδa- است. در پارسی باستان نیز همین دوگانگی ستاک دیده می‌شود: ستاک قوی در pādaibiyā «با دو پا» (بیستون) و ستاک ضعیف pad- در قید ni-padiy «در پی، بر ردّ» و در pati-padam «در جای خود»، و صورت مشتق pāda- در نام ماه Garma-pada-. کنت در واژه‌نامهٔ پارسی باستان همین‌ها را ذیل «*ped- یا pod- \\\"پا\\\"» می‌آورد. پس هر چهار صورتِ این گره درست و به‌جا نام‌گذاری شده است.\",\n    \"sources\": [W_PAY],\n    \"ref_check\": [\n     {\"ref\": \"KLN:1112\", \"status\": \"supports\", \"note\": \"Klein s.v. pajamas (KLN_1966.txt leaf 594 ≈ printed p.1112): 'Pers. pāi, \\\"foot, leg\\\", is rel. to Avestic pad-, \\\"foot\\\", and cogn. with Gk. πούς, gen. ποδός, L. pēs, gen. pedis, \\\"foot\\\", Goth. fōtus, OE. fōt, \\\"foot\\\".' — the Avestan/Old Persian starting point Nourai draws.\"}\n    ],\n    \"consulted\": [\n     {\"src\": \"BRT\", \"where\": \"Bartholomae AiW col. 885 ff. s.v. pad-/pāδ- (also quoted by Nyberg as 'Av. (842) pāδ-')\", \"stance\": \"supports\", \"note\": \"Nyberg's glossary cites 'Av. (842) pāδ-' for the foot-word and 'Av. (842) 1paiδa-' for the derivative behind payg — i.e. Bartholomae has both stems.\"},\n     {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, lexicon/root index (KNT.txt line 1515)\", \"stance\": \"supports\", \"note\": \"'*ped- or pod- \\\"foot\\\" in ni-padiy, pati-padam, Garma-pada-, (Ar.) *pād- in pādaibiya \\\"with the two feet\\\".' Also line 1061: 'pIE *ped- \\\"foot\\\", loc. in OP ni-padiy, Skt. padi'.\"},\n     {\"src\": \"POK\", \"where\": \"IEW p.791\", \"stance\": \"supports\", \"note\": \"'ai. pād- \\\"Fuß\\\" (pāt, pādam, padáh), av. pād- ds.; apers. pādaibiyā \\\"mit den Füßen\\\"'; and 'pedio- in ai. pādya-, av. paiδyā \\\"Fuß\\\"'.\"}\n    ]\n   },\n   {\n    \"id\": 2,\n    \"lang\": \"Persian\",\n    \"words\": \"pâ «پا»; pây-în «پایین»; pâ-jâmeh «پاجامه»\",\n    \"verdict\": \"confirmed\",\n    \"derivation\": \"Old Iranian pāda- > Middle Persian pāy [p'dy] 'foot, leg' > New Persian پای pāy, with the everyday short form پا pā by loss of the final -y (the doublet پای/پا is still alive; Borhan's cross-references پای ۱، پی، پاچه، پایه on this page are all of the same stem). Horn, Grundriss der neupersischen Etymologie, no. 281, p.63: 'pā, pā \\\"Fuss\\\"; vergl. pāye \\\"Stufe\\\", pāyīn. — aw. pāda- \\\"Fuss\\\"; phlv. pāī \\\"Fuss\\\", pāyah \\\"Stufe\\\"; ai. pāda-; arm. otn.' پایین pāyīn is that same pāy plus the locative/adjectival -īn 'at the feet' > 'below, down' (Horn puts it in the same entry). پاجامه pā-jāmeh is a transparent Persian compound pā 'leg' + jāmeh 'garment' (< MP jāmag), i.e. 'leg-garment', the word that travelled to India and back (nodes 3-5).\",\n    \"derivation_fa\": \"از ایرانی باستان pāda- به فارسی میانهٔ pāy (نوشتهٔ p'dy) «پا، ساق» و از آن فارسی نو «پای»، و صورت کوتاه روزمرهٔ «پا» با افتادن ی پایانی؛ این دوگانه هنوز زنده است (ارجاع‌های برهان در همین صفحه — پای ۱، پی، پاچه، پایه — همه از همین ستاک‌اند). هرن در دستور ریشه‌شناسی فارسی نو، شمارهٔ ۲۸۱، ص ۶۳ می‌نویسد: «pā, pā \\\"پا\\\"؛ قس pāye \\\"پله\\\"، pāyīn. — اوستایی pāda- \\\"پا\\\"؛ پهلوی pāī \\\"پا\\\"، pāyah \\\"پله\\\"؛ سنسکریت pāda-؛ ارمنی otn». «پایین» همان pāy + پسوند -īn است، نخست «در سوی پاها» و سپس «زیر، پایین». «پاجامه» نیز ترکیب روشن فارسی «پا + جامه» (جامه از jāmag پهلوی) یعنی «جامهٔ پا» است — همان واژه‌ای که به هند رفت و از راه انگلیسی بازگشت. ادعای نورایی درست است.\",\n    \"sources\": [W_PAY],\n    \"ref_check\": [\n     {\"ref\": \"HRN:63\", \"status\": \"supports\", \"note\": \"Horn no.281 on printed p.63 (HRN.txt \\\\f-leaf 84): 'pā, pā \\\"Fuss\\\"; vergl. pāye \\\"Stufe\\\", pāyīn. — aw. pāda- \\\"Fuss\\\"; phlv. pāī \\\"Fuss\\\", pāyah \\\"Stufe\\\"; ai. pāda-; arm. otn (H. No. 280).' Exactly the arrow Nourai draws, and it covers pāyīn too.\"},\n     {\"ref\": \"BQT:344\", \"status\": \"supports\", \"note\": \"Borhan vol.1 printed p.344 (BQT_v1_pages.txt leaf 564, the first page of the پ section) is the پا entry, and its footnote 1 is Mo'in's etymological note giving 'ایرانی باستان … بارتولمه … اوستا … هندی باستان … پهلوی … کردی … استی …' for the word — the standard Old-Iranian-to-Persian chain.\"},\n     {\"ref\": \"BQT:367\", \"status\": \"not_checked\", \"note\": \"p.367 = leaf ~588 of BQT_v1_pages.txt; the OCR of that leaf is too degraded to identify the headword (presumably پاجامه/پاچه). Not read.\"}\n    ],\n    \"consulted\": [\n     {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary, p.66 s.v. pāy (PHD.txt line 545)\", \"stance\": \"supports\", \"note\": \"'pāy [LGLE < A rglh; p'dy | M p'y, N —] foot, leg; foot (12 in.)' and 'payag [p'd(y)k! | N pāya] base, station' — MP pāy is the direct ancestor of NP پا/پای, and pāya of پایه.\"},\n     {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, p.147 s.v. pād (pā)\", \"stance\": \"supports\", \"note\": \"'pād (pā) [pd; LGLH; Prth NGRYN] foot ... — Av. (842) pād-; MPrth p'd; MPrs p'y; Paz. pāδ, pāh; NP pā(y).'\"},\n     {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien\", \"stance\": \"supports\", \"note\": \"Hübschmann treats the pā-/pāy- family throughout (e.g. p.200 payg, piyāda) on the same Old Iranian pād- base.\"},\n     {\"src\": \"IEC\", \"where\": \"Mann s.v. ped-, pēd-\", \"stance\": \"supports\", \"note\": \"'Per. pay, s. \\\"foot\\\"; paye, s. \\\"ground, basis\\\"' listed among the direct descendants.\"}\n    ]\n   },\n   {\n    \"id\": 3,\n    \"lang\": \"Hindustani\",\n    \"words\": \"paě-jâma\",\n    \"verdict\": \"confirmed\",\n    \"derivation\": \"The Persian compound pā(y)-jāmeh was carried into India with Persian as the court and administrative language of the Delhi Sultanate and the Mughals, and became Hindi/Urdu पाजामा pāy-jāmā / paijāmā 'leg-garment', the loose drawstring trousers worn by Muslim men and women, Sikhs and others. Hobson-Jobson p.748: 'PYJAMMAS, s. Hind. pāi-jāma (see JAMMA), lit. \\\"leg-clothing.\\\" A pair of loose drawers or trowsers, tied round the waist. Such a garment is used by various persons in India ... It was adopted from the Mahommedans by Europeans as an article of dishabille and of night attire.' Nourai's 'paě-jâma' is Yule's pāi-jāma with the Hindi diphthong written ě.\",\n    \"derivation_fa\": \"ترکیب فارسی «پای‌جامه» همراه با زبان فارسی — که زبان دیوان و دربار سلطنت دهلی و گورکانیان هند بود — به هند رفت و در هندی/اردو به صورت پاجاما/پای‌جاما «جامهٔ پا» درآمد، یعنی همان شلوار گشادِ بندی که مردان و زنان مسلمان و سیک‌های هند می‌پوشیدند. یول و برنل در هابسون-جابسون، ص ۷۴۸ می‌نویسند: «PYJAMMAS: هندی pāi-jāma (نگاه کنید به JAMMA)، تحت‌اللفظ \\\"جامهٔ پا\\\"؛ شلوار گشادی که با بند به کمر می‌بندند … اروپاییان آن را از مسلمانان هند گرفتند و جامهٔ خانه و خواب کردند». صورتِ paě-jâma در کتاب نورایی همان pāi-jāma یول است. ادعای او درست است.\",\n    \"sources\": [E_PAJ],\n    \"ref_check\": [\n     {\"ref\": \"HJB:748\", \"status\": \"supports\", \"note\": \"Hobson-Jobson printed p.748 (HJB.txt \\\\f-leaf 794; leaf = printed + 46 here): 'PYJAMMAS, s. Hind. pāi-jāma (see JAMMA), lit. \\\"leg-clothing.\\\" A pair of loose drawers or trowsers, tied round the waist ... It is probable that we English took the habit like a good many others from the Portuguese.'\"}\n    ],\n    \"consulted\": [\n     {\"src\": \"AID\", \"where\": \"Whitworth, An Anglo-Indian Dictionary, p.234 (AID.txt leaf 252)\", \"stance\": \"supports\", \"note\": \"'PAIJĀMĀ. [Persian.] Drawers, trousers, such as are worn by Musalmān men and women. Among Europeans, sleeping-drawers.' — Whitworth calls the word Persian, i.e. a Persian loan in Indian usage.\"},\n     {\"src\": \"KLN\", \"where\": \"Klein s.v. pajamas (leaf 594 ≈ p.1112)\", \"stance\": \"supports\", \"note\": \"'Hind. pajama, paijama, lit. \\\"leg-garment\\\", fr. Pers. pā, pāi, \\\"foot, leg\\\", and jāma, \\\"clothing, garment\\\".'\"}\n    ]\n   },\n   {\n    \"id\": 4,\n    \"lang\": \"English\",\n    \"words\": \"pajamas\",\n    \"verdict\": \"confirmed\",\n    \"derivation\": \"British residents in India adopted the Indian garment as informal and night wear from about 1800; the word is first recorded in English in that sense in the early 19th century (Yule cites Anglo-Indian usage throughout the 1800s), the American spelling pajamas being settled by about 1845 and the British pyjamas remaining the norm. Etymonline: 'pajamas ... from Hindi pajama, probably from Persian paejamah, literally \\\"leg clothing\\\", from pae \\\"leg\\\" (from PIE root *ped- \\\"foot\\\") + jamah \\\"clothing, garment\\\"'; Klein and Watkins (AHD, s.v. ped-1: 'Middle Persian pāδ, leg, foot: PAJAMAS, TEAPOY') say the same. The chain Persian → Hindustani → English is thus exactly as Nourai draws it.\",\n    \"derivation_fa\": \"انگلیسی‌های مقیم هند از حدود ۱۸۰۰ میلادی این جامهٔ هندی را جامهٔ خانه و خواب کردند و واژه در همان معنی به انگلیسی راه یافت؛ املای آمریکایی pajamas از حدود ۱۸۴۵ تثبیت شد و املای بریتانیایی pyjamas ماند. اتیمانلاین می‌نویسد: «pajamas از هندی pajama، احتمالاً از فارسی paejamah به معنی تحت‌اللفظی \\\"جامهٔ پا\\\"، از pae \\\"پا\\\" (از ریشهٔ هندواروپایی *ped-) و jamah \\\"جامه\\\"». کلاین و واتکینز (پیوست ریشه‌های AHD ذیل ped-1: «فارسی میانه pāy: PAJAMAS، TEAPOY») نیز همین را می‌گویند. پس زنجیرهٔ فارسی ← هندی ← انگلیسی که نورایی رسم کرده درست است.\",\n    \"sources\": [E_PAJ],\n    \"ref_check\": [\n     {\"ref\": \"KLN:1112\", \"status\": \"supports\", \"note\": \"Klein (KLN_1966.txt leaf 594 ≈ printed p.1112): 'pajamas, pyjamas, n. pl., loose trousers or drawers. — Hind. pajama, paijama, lit. \\\"leg-garment\\\", fr. Pers. pā, pāi, \\\"foot, leg\\\", and jāma, \\\"clothing, garment\\\".'\"},\n     {\"ref\": \"AID:234\", \"status\": \"supports\", \"note\": \"Whitworth p.234 (AID.txt leaf 252, leaf = printed + 18): 'PAIJĀMĀ. [Persian.] Drawers, trousers ... Among Europeans, sleeping-drawers.'\"},\n     {\"ref\": \"AHD:943\", \"status\": \"not_checked\", \"note\": \"AHD:943 is a page of the main word-list of the 1975 New College Edition (the entry 'pajamas'), which is not in the local library; the Watkins IE-roots appendix that is on disk confirms the etymology under ped-1 ('Middle Persian pāδ, leg, foot: PAJAMAS, TEAPOY') but has its own pagination.\"}\n    ],\n    \"consulted\": [\n     {\"src\": \"HJB\", \"where\": \"Hobson-Jobson p.748\", \"stance\": \"supports\", \"note\": \"Documents the Anglo-Indian adoption: 'It was adopted from the Mahommedans by Europeans as an article of dishabille and of night attire ... The word is now used in London shops.'\"},\n     {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. ped-1, section I.9.c\", \"stance\": \"supports\", \"note\": \"'Middle Persian pāδ, leg, foot: PAJAMAS, TEAPOY.'\"},\n     {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etymological Dictionary\", \"stance\": \"silent\", \"note\": \"No pyjamas entry in the concise edition.\"}\n    ]\n   },\n   {\n    \"id\": 5,\n    \"lang\": \"Persian\",\n    \"words\": \"pîjâmeh «پی جامه» (also پیژامه)\",\n    \"verdict\": \"plausible\",\n    \"derivation\": \"This is the round trip: the Persian compound went to India, from India to English/French, and came back to Persian in the 20th century as a name for Western-style sleeping trousers. Mo'in's Farhang-e Farsi has the headword پی‌جامه glossed 'نوعی شلوار گشاد که زنان هند پوشند؛ جامه‌ای گشاد … در خانه و هنگام خواب پوشند؛ پیژاما' — i.e. he registers both the Indian garment and the modern re-borrowing, with the variant پیژاما. The one qualification is the route: the everyday Iranian form پیژامه with -ž- points to French pyjama (French j = /ʒ/), not to English pajamas with /dʒ/; Nourai's own alternative spelling پیژامه is precisely the French-mediated form, while پی‌جامه is the older, directly Indo-Persian spelling. So the arrow English → Persian should read 'European (chiefly French) → Persian'.\",\n    \"derivation_fa\": \"این گره همان «سفر رفت و برگشت» واژه است: ترکیب فارسی «پای‌جامه» به هند رفت، از هند به انگلیسی و فرانسه، و در سدهٔ چهاردهم خورشیدی دوباره به فارسی بازگشت، این بار به معنی شلوار خوابِ اروپایی. معین در فرهنگ فارسی سرواژهٔ «پی‌جامه» را چنین معنی می‌کند: «نوعی شلوار گشاد که زنان هند پوشند؛ جامه‌ای گشاد … در خانه و هنگام خواب پوشند؛ پیژاما» — یعنی هم جامهٔ هندی و هم وام‌گیری تازه را ثبت کرده است. تنها نکته دربارهٔ راه وام‌گیری است: صورت رایج «پیژامه» با «ژ» نشان می‌دهد که میانجی، فرانسهٔ pyjama بوده (j فرانسوی = ژ)، نه انگلیسیِ pajamas که در آن /dʒ/ است؛ صورت «پی‌جامه» همان املای کهن‌ترِ هندی-فارسی است. پس ادعای نورایی با این احتیاط پذیرفتنی است که پیکان باید «از زبان‌های اروپایی (بیشتر فرانسه)» خوانده شود نه صرفاً «از انگلیسی».\",\n    \"sources\": [E_PAJ],\n    \"ref_check\": [\n     {\"ref\": \"MON:868,902\", \"status\": \"partial\", \"note\": \"The 6-volume Amir Kabir edition is not online, so the exact pages could not be opened; the 2-volume Adena condensation of Mo'in (MON_part1.txt line 34030) has the headword: 'پی جامه: … نوعی شلوار گشاد که زنان هند پوشند. جامه‌ای گشاد … در خانه و هنگام خواب پوشند؛ پیژاما.' The entry Nourai cites exists and carries both forms; only the page numbers are unverifiable.\"}\n    ],\n    \"consulted\": [\n     {\"src\": \"MON\", \"where\": \"MON_part1.txt line 34030 s.v. پی جامه\", \"stance\": \"supports\", \"note\": \"Gives the Indian garment sense and the variant پیژاما, i.e. the re-borrowed European form.\"},\n     {\"src\": \"KLN\", \"where\": \"Klein s.v. pajamas\", \"stance\": \"partial\", \"note\": \"Klein documents the outward journey (Pers. > Hind. > Eng.) but says nothing about the return loan into Persian.\"},\n     {\"src\": \"BQT\", \"where\": \"grep 'پیژامه' over BQT_v1/v2_pages.txt\", \"stance\": \"silent\", \"note\": \"No پیژامه/پی‌جامه headword in Borhan-e Qate' — as expected for a 20th-century loan, since Borhan is a 17th-century dictionary.\"}\n    ]\n   },\n   {\n    \"id\": 6,\n    \"lang\": \"Avestan\",\n    \"words\": \"padika; padâtaka\",\n    \"verdict\": \"plausible\",\n    \"derivation\": \"Both forms are exactly what Iranists reconstruct, but neither is attested in Avestan — the language label is Nourai's (or the book's) mistake. (a) *padika- 'one who goes on foot' is the Old Iranian preform posited for NP payk: Hübschmann, Persische Studien no.359, pp.45-46: 'Np. paig \\\"Fussgänger\\\" = syr. paigā, arab. faij, phl. paik ... arm. Lw. payik, skr. padika- \\\"Fussgänger\\\", prakr. paikka-. Für das Altpersische ist mit Horn *padika- anzusetzen.' So padika- is attested in Sanskrit and reconstructed for Old Persian, not read off an Avestan text. (b) padātaka- likewise: Wiktionary derives NP piyāda from MP payādag < Proto-Iranian *padātaka-/*padātika- 'on foot' (*pada- 'foot' + *taka- 'going', or *padāti- + *-ka-), and Hübschmann p.200 equates 'payāda \\\"Fussgänger\\\" = skr. padāti-, padātika-'. Pokorny p.791, the page Nourai cites, has the Sanskrit forms — 'ai. padyate \\\"geht, fällt\\\" (ā-patti- \\\"Unfall\\\"; padāti-, pat-ti- m. \\\"Fußknecht\\\")' — as Sanskrit, not Avestan. Verdict: the forms and the derivational step Old Iranian *pad- → *padika-/*padātaka- are right; the label 'Avestan' should read 'Sanskrit / reconstructed Old Iranian'.\",\n    \"derivation_fa\": \"هر دو صورت درست‌اند، اما هیچ‌کدام در متون اوستایی گواهی ندارند؛ برچسب «اوستایی» خطای کتاب است. یکم، *padika- «پیاده‌رو» صورتی است که ایران‌شناسان برای نیای «پیک» بازسازی کرده‌اند: هوبشمان در Persische Studien، شمارهٔ ۳۵۹، ص ۴۵–۴۶ می‌نویسد: «فارسی نو paig \\\"پیاده\\\" = سریانی paigā، عربی فیج، پهلوی paik … ارمنی وام‌گرفتهٔ payik، سنسکریت padika- \\\"پیاده\\\"، پراکریت paikka-. برای پارسی باستان باید همراه هرن *padika- نهاد.» دوم، padātaka- نیز چنین است: ویکی‌واژه «پیاده» را از payādag فارسی میانه و آن را از *padātaka-/*padātika- ایرانی باستان می‌گیرد (*pada- «پا» + *taka- «رونده»)، و هوبشمان در ص ۲۰۰ می‌نویسد «payāda \\\"پیاده\\\" = سنسکریت padāti-، padātika-». پوکورنی هم در همان ص ۷۹۱ که نورایی ارجاع داده این صورت‌ها را سنسکریت می‌داند: «ai. padāti-, pat-ti- m. \\\"Fußknecht\\\"». پس گام اشتقاقی از *pad- ایرانی باستان به *padika-/*padātaka- درست است و تنها نام زبان باید «سنسکریت / ایرانی باستانِ بازسازی‌شده» می‌بود.\",\n    \"sources\": [W_PAYK, W_PIY],\n    \"ref_check\": [\n     {\"ref\": \"POK:790\", \"status\": \"partial\", \"note\": \"Pokorny p.790-791 has the root and, on p.791, 'ai. padyate \\\"geht, fällt\\\" (ā-patti- \\\"Unfall\\\"; padāti-, pat-ti- m. \\\"Fußknecht\\\")' — the padāti- material, but explicitly as Sanskrit (ai. = altindisch); Pokorny lists no Avestan padika-/padātaka-, only 'av. paiδyeiti \\\"bewegt sich nach abwärts\\\"' and 'av. paiδyā \\\"Fuß\\\"'.\"}\n    ],\n    \"consulted\": [\n     {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien no.359, pp.45-46 (HUB.txt leaf 55) and p.200 (leaf 210)\", \"stance\": \"supports\", \"note\": \"p.45-46: '... skr. padika- \\\"Fussgänger\\\", prakr. paikka-. Für das Altpersische ist mit Horn *padika- anzusetzen.' p.200: 'payg \\\"Bote\\\" = syr., phl. paik, arm. payik, skr. padika-; payāda \\\"Fussgänger\\\" = skr. padāti-, padātika-.'\"},\n     {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, p.147\", \"stance\": \"supports\", \"note\": \"'padātak [pd'tk'] footsoldier; pawn in chess ... MPrs py'dg, Sogd 2574.26; NP piyādah; Skr. lw. padāti(ka)-.' — again Sanskrit, not Avestan.\"},\n     {\"src\": \"BRT\", \"where\": \"grep 'padika|padataka' over BRT.txt\", \"stance\": \"contradicts\", \"note\": \"Bartholomae's Altiranisches Wörterbuch has no paδika- or paδātaka- headword; the labels 'Avestan' on this node cannot be sustained from the Avestan lexicon.\"},\n     {\"src\": \"IEC\", \"where\": \"Mann s.v. ped-, pēd-\", \"stance\": \"partial\", \"note\": \"Lists 'Skt. padáh ... pádyah, adj.; padyā, f. \\\"track\\\"; Av. paiδya, f. \\\"foot\\\"' — the Avestan derivative is paiδya-, not padika-.\"}\n    ]\n   },\n   {\n    \"id\": 7,\n    \"lang\": \"Persian\",\n    \"words\": \"payk «پیک»; piyâdeh «پیاده»\",\n    \"verdict\": \"confirmed\",\n    \"derivation\": \"پیک payk 'foot-messenger, courier' continues Middle Persian payg [pdh'] 'foot-soldier, courier' (MacKenzie, Concise Pahlavi Dictionary p.65), from Old Iranian *padika- 'one who goes on foot'; Nyberg (Manual of Pahlavi II, p.147) sets it out: 'Av. paiδa-; MPrth pdg = MPrs pyg; NP paik \\\"walking runner, messenger\\\"; Arm. lw. payik \\\"footman, guardian\\\"; Syr. lw. paigā'. The word was borrowed onward into Syriac paigā, Armenian payik and Arabic فيج fayj. Old Iranian intervocalic -d- > MP -y- and the -ka- suffix > -g/-k give payg/payk regularly; the semantic line is 'goer on foot' > 'runner' > 'courier' (Hafez's line quoted by Nourai, 'مرحبا ای پیک مشتاقان', is the classical use). پیاده piyādeh 'on foot, pedestrian, chess pawn' continues MP payādag [pd'tk'] 'on foot, foot-soldier, (chess) pawn' (MacKenzie p.65; Nyberg p.147 'padātak ... NP piyādah'), from Old Iranian *padātaka-; MP -ādag > NP -āda regularly, with the prothetic i- of piyāda from the glide. Both Persian words and both meanings in the chart are right.\",\n    \"derivation_fa\": \"«پیک» به معنی «قاصدِ پیاده، چاپار» دنبالهٔ payg فارسی میانه (نوشتهٔ pdh) است، به معنی «سرباز پیاده، پیک»، و آن از *padika- ایرانی باستان «آنکه پیاده می‌رود». نیبرگ در دستور پهلوی، بخش دوم، ص ۱۴۷ زنجیره را چنین می‌آورد: «اوستایی paiδa-؛ پارتی pdg = فارسی میانه pyg؛ فارسی نو paik \\\"دوندهٔ پیاده، پیام‌رسان\\\"؛ ارمنی وام‌گرفتهٔ payik؛ سریانی وام‌گرفتهٔ paigā». همین واژه به سریانی و ارمنی و عربی («فیج») هم وام داده شده است. دگرگونی‌های آوایی قاعده‌مندند: d میان‌واکه‌ای ایرانی باستان در فارسی میانه y می‌شود و پسوند -ka- به g/k می‌رسد؛ تحول معنایی هم «پیاده‌رو ← دونده ← قاصد» است (بیت حافظِ نقل‌شده در نمودار، «مرحبا ای پیک مشتاقان»، همین کاربرد کلاسیک است). «پیاده» نیز دنبالهٔ payādag فارسی میانه است («پیاده، سرباز پیاده، سربازِ شطرنج» در فرهنگ مکنزی و نیبرگ)، از *padātaka- ایرانی باستان؛ -ādag پهلوی به -اده در فارسی نو بدل می‌شود. ادعای نورایی دربارهٔ هر دو واژه درست است.\",\n    \"sources\": [W_PAYK, W_PIY],\n    \"ref_check\": [\n     {\"ref\": \"NYB:147\", \"status\": \"supports\", \"note\": \"Nyberg, A Manual of Pahlavi II (glossary) printed p.147 (NYB_vol2_glossary.txt \\\\f-leaf 162, the leaf carrying the running head '147 pad'): '... Av. (842) 1paiδa-; MPrth pdg = MPrs pyg; NP paik \\\"walking runner, messenger\\\"; Arm. lw. payik \\\"footman, guardian\\\"; Syr. lw. paigā id.; Sogd. 2527.26. V. also padātak and padē.' and on the same page 'padātak [pd'tk'] footsoldier; pawn in chess ... NP piyādah'.\"},\n     {\"ref\": \"BQT:434\", \"status\": \"partial\", \"note\": \"Borhan vol.1 printed p.434 (BQT_v1_pages.txt leaf 659, fixed by the 'بقیه از صفحهٔ ۴۳۲' catch-line) is the پی entry: 'مخفف پای است که بعربی رجل خوانند، و نشان پای باشد که نقش قدم است ... و دنبال و پس و عقب' with a Pahlavi footnote. The پیک and پیاده headwords fall a page or two later and did not survive in the OCR of vol.1, so only the immediate context could be read.\"}\n    ],\n    \"consulted\": [\n     {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary p.65 (PHD.txt line 547 and 545)\", \"stance\": \"supports\", \"note\": \"'payg [pdh! | (P pap), N ~] foot-soldier, courier' and 'payādag [pd'tk' | M py'dg, N piyāda] on foot, foot-soldier, (chess) pawn' — both New Persian outcomes given explicitly.\"},\n     {\"src\": \"HUB\", \"where\": \"Persische Studien no.359 p.45-46 and p.200\", \"stance\": \"supports\", \"note\": \"'Np. paig \\\"Fussgänger\\\" = syr. paigā, arab. faij, phl. paik ... skr. padika-'; 'payāda \\\"Fussgänger\\\" = skr. padāti-, padātika-'.\"},\n     {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no.359 (index note, HRN.txt line 255)\", \"stance\": \"supports\", \"note\": \"Horn's no.359 is the paig entry Hübschmann is correcting; the introduction notes 'paikka- \\\"Fussoldat\\\" zu np. paig, No. 359'.\"},\n     {\"src\": \"MON\", \"where\": \"Wiktionary پیک, citing Horn 1893 and Hübschmann 1897\", \"stance\": \"supports\", \"note\": \"'From Middle Persian, ultimately from Proto-Iranian *pā́dah (\\\"foot\\\"); cognate with Sanskrit padika (\\\"pedestrian\\\"); borrowed into Old Armenian, Georgian, Classical Syriac and Arabic.'\"}\n    ]\n   },\n   {\n    \"id\": 8,\n    \"lang\": \"Sogdian\",\n    \"words\": \"pd; pdny\",\n    \"verdict\": \"confirmed\",\n    \"derivation\": \"Sogdian pδ (written pd, also pδ') 'foot, step' and pδn(y) 'heel' are both in Gharib's Sogdian Dictionary: entry 6749 'pδ- M,S — paδ (paδδ) © acc. -w; ob. -y ... foot, step' (printed p.271) and entry 6820 'pδn(y) C — paδn, paδan © < pad- © acc. pδnw ... heel, kick' (printed p.273). The forms continue Old Iranian *pad-/*pāda- with the East Iranian development of *d to δ; pδny is *padna- 'heel' (cf. Av. pāšna-, MP pāšnag, NP پاشنه, from *pāršni-, and the parallel *padna- type). So Nourai's Sogdian node, both words and both glosses, is right; his page numbers land on the correct pages of Gharib.\",\n    \"derivation_fa\": \"دو واژهٔ سغدی pδ (نوشتهٔ pd، نیز pδ') «پا، گام» و pδn(y) «پاشنه» هر دو در فرهنگ سغدی بدرالزمان قریب هست: مدخل ۶۷۴۹ «pδ- ... foot, step» در ص ۲۷۱ و مدخل ۶۸۲۰ «pδn(y) — paδn، paδan، از pad- ... heel, kick» در ص ۲۷۳. این صورت‌ها دنبالهٔ *pad-/*pāda- ایرانی باستان‌اند با تحول ویژهٔ ایرانی شرقی که d را به δ بدل می‌کند؛ pδny از *padna- «پاشنه» است (قس pāšna- اوستایی، pāšnag پهلوی و «پاشنه»ی فارسی). پس گره سغدیِ نورایی — هر دو واژه و هر دو معنی — درست است و شماره‌های صفحه‌ای که داده دقیقاً بر صفحه‌های قریب می‌افتد.\",\n    \"sources\": [],\n    \"ref_check\": [\n     {\"ref\": \"SOD:270\", \"status\": \"supports\", \"note\": \"Gharib entry 6749 'pδ-1 M,S | paδ (paδδ) © acc. -w; ob. -y ... foot, step | BBB 489; paδδw, Hen. BSOAS 11, 68.22; GMS 506' — the entry opens at the foot of SOD_pages.txt leaf 336 (printed p.270) and the gloss 'foot, step' is printed at the top of leaf 337 (p.271); Nourai's 270 is the page where the entry begins.\"},\n     {\"ref\": \"SOD:273\", \"status\": \"supports\", \"note\": \"Gharib entry 6820 'pδn(y) C | paδn, paδan © < pad- © acc. pδnw | heel, kick | S W, C2, 94V14 p176-7; Benv. pznw' on SOD_pages.txt leaf 339 = printed p.273 (printed = leaf − 66). English index of the dictionary: 'heel 6820, 7509'.\"}\n    ],\n    \"consulted\": [\n     {\"src\": \"SOD\", \"where\": \"Gharib, Sogdian Dictionary, entries 6749 (p.270-271) and 6820 (p.273); English index s.v. heel\", \"stance\": \"supports\", \"note\": \"Both words, both glosses, exactly as charted.\"},\n     {\"src\": \"PHD\", \"where\": \"MacKenzie p.66 s.v. pāšnag\", \"stance\": \"partial\", \"note\": \"'pāšnag [p'šnk! | N ~a] heel' — the South-West Iranian word for 'heel' is pāšnag/پاشنه, a different formation from Sogdian pδny; useful contrast for node 9.\"},\n     {\"src\": \"BRT\", \"where\": \"Bartholomae s.v. pāšna- (AiW)\", \"stance\": \"partial\", \"note\": \"Avestan pāšna- 'heel' (< *pāršni-) is the Avestan word; the Sogdian pδn- type is a separate, East Iranian formation on pad-.\"}\n    ]\n   },\n   {\n    \"id\": 9,\n    \"lang\": \"Persian\",\n    \"words\": \"pal «پَل»\",\n    \"verdict\": \"plausible\",\n    \"derivation\": \"پَل pal 'heel' is a genuine early Dari word: Asadi Tusi's Loghat-e Fors glosses it 'پاشنهٔ پا بود' and quotes exactly Nourai's Maʿrufi verse ('همیشه کفش و پلش را کفیده بینم من / بجای کفش و پلش دل کفیده بایستی'). The Sogdian source is Henning's classic criterion (Sogdian Loan-words in New Persian, BSOAS 10, 1939, 93-106): in most Sogdian dialects Old Iranian d/δ and θ had merged into a sound close to West Iranian l, so a New Persian word with -l- where South-West Iranian has -d-/-y- is a Sogdian loan. NP pal 'heel' beside native پاشنه pāšna is exactly that pattern: Sogd. pδn- 'heel' (< *padna-, Gharib 6820) with δ > l, the -n- lost as in other short Persian reflexes. The step is therefore very likely right, but I could not read Henning's page 98 itself — the Cambridge PDF of the article returns HTTP 403 and the local OCR of Henning's Selected Papers does not contain the article in readable form — so the specific attribution to SLW:98 stays unverified.\",\n    \"derivation_fa\": \"«پَل» به معنی «پاشنه» واژه‌ای راستین از دریِ کهن است: اسدی طوسی در لغت فرس آن را «پاشنهٔ پا بود» معنی می‌کند و همان بیت معروفی را می‌آورد که نورایی نقل کرده است («همیشه کفش و پلش را کفیده بینم من / بجای کفش و پلش دل کفیده بایستی»). سغدی‌بودن آن بر پایهٔ معیار مشهور هنینگ است (مقالهٔ «وام‌واژه‌های سغدی در فارسی نو»، BSOAS ۱۰، ۱۹۳۹، ص ۹۳–۱۰۶): در بیشتر گویش‌های سغدی d/δ و θ ایرانی باستان به آوایی نزدیک به «ل» فارسیِ غربی بدل شده‌اند؛ پس هر واژهٔ فارسی که در آن «ل» در جای d/y جنوب‌غربی نشسته باشد، وام‌واژهٔ سغدی است. «پل» در برابر «پاشنه»ی بومی دقیقاً همین الگوست: سغدی pδn- «پاشنه» (از *padna-، قریب ۶۸۲۰) با تبدیل δ به ل و افتادن n. بنابراین این گام به‌احتیاط پذیرفتنی است؛ ولی خودِ صفحهٔ ۹۸ مقالهٔ هنینگ را نتوانستم ببینم (نسخهٔ کمبریج خطای ۴۰۳ می‌دهد و متن OCR مجموعه‌مقالات هنینگ این مقاله را خوانا ندارد)، پس استناد به SLW:98 وارسی‌نشده می‌ماند.\",\n    \"sources\": [],\n    \"ref_check\": [\n     {\"ref\": \"FRS:173\", \"status\": \"supports\", \"note\": \"Asadi Tusi, Loghat-e Fors (FRS_pages.txt \\\\f-leaf 332, in the final-ل section): headword glossed 'پاشنهٔ پا بود [معروفی گوید: همیشه کفش و پلش را کفیده بینم من / بجای کفش و پلش دل کفیده بایستی]' — the word, the gloss and Nourai's shāhed. (The local scan is the Eqbal 1319 edition, whose pagination differs from the Kharazmi 1365 edition Nourai cites, so the number 173 could not be matched.)\"},\n     {\"ref\": \"SOD:270\", \"status\": \"supports\", \"note\": \"Gharib entry 6749 pδ 'foot, step' / 6820 pδn(y) 'heel' — the Sogdian side of the loan is confirmed (see node 8).\"},\n     {\"ref\": \"SLW:98\", \"status\": \"not_checked\", \"note\": \"Henning, 'Sogdian Loan-words in New Persian', BSOAS 10.1 (1939) 93-106: the Cambridge Core PDF returns HTTP 403 and the local HENNING_selected_papers.txt OCR does not contain a readable text of the article (grep for 'Sogdian loan-words'/'heel' produced only unrelated hits). Could not confirm that p.98 lists pal.\"}\n    ],\n    \"consulted\": [\n     {\"src\": \"SOD\", \"where\": \"Gharib 6820 (p.273)\", \"stance\": \"supports\", \"note\": \"'pδn(y) ... paδn, paδan © < pad- ... heel' — the Sogdian etymon exists with the right meaning.\"},\n     {\"src\": \"FRS\", \"where\": \"Loghat-e Fors, leaf 332\", \"stance\": \"supports\", \"note\": \"Attests پل 'heel' in 10th-11th-century Dari poetry (Maʿrufi of Balkh).\"},\n     {\"src\": \"HRN\", \"where\": \"grep 'pal' over HRN.txt\", \"stance\": \"silent\", \"note\": \"Horn's Grundriss has no entry for پل 'heel'.\"},\n     {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. pāšnag\", \"stance\": \"partial\", \"note\": \"The inherited South-West Iranian word for 'heel' is pāšnag > پاشنه; پل with -l- cannot be a South-West form, which is what makes the Sogdian (or generally North-East Iranian) source likely.\"},\n     {\"src\": \"HENNING\", \"where\": \"HENNING_selected_papers.txt, grep 'Sogdian loan-word' / 'heel'\", \"stance\": \"silent\", \"note\": \"The Selected Papers OCR yields only passing mentions of 'a hitherto unrecognized Sogdian loan-word in Turkish' etc.; the 1939 article itself is not usable in this scan.\"}\n    ]\n   },\n   {\n    \"id\": 10,\n    \"lang\": \"Latin\",\n    \"words\": \"ped; ped-yôs\",\n    \"verdict\": \"confirmed\",\n    \"derivation\": \"Latin pēs, gen. pedis 'foot' is the direct continuation of PIE *pṓds / *ped- (Pokorny 790-791: 'lat. pēs, pedis ds.'). 'ped-yôs' is not a Latin word but the pre-Latin comparative *ped-yōs that yields Latin peior 'worse' (with -dy- > -i-, i.e. *pedyōs > *peiiōs > peior), matched by the superlative *ped-samos > pessimus 'worst'; the semantics run from the verbal side of the root, 'stumbling, falling' > 'coming off worse'. Klein s.v. pejorative: 'peior, \\\"worse\\\", which stands for *ped-yos and is rel. to L. pessimus, \\\"worst\\\" (for *ped-semos), and to pessum, \\\"downward, to the ground\\\", and cogn. with OI. padyate, \\\"falls\\\"; from the same base as L. pes, gen. pedis, \\\"foot\\\"'; Watkins says the same under ped-1, II.2. So Nourai's gloss 'lowest, worst' for ped-yôs is right; only the language label is loose (it is a reconstruction, not attested Latin).\",\n    \"derivation_fa\": \"لاتینی pēs (اضافی pedis) «پا» بازماندهٔ مستقیم *pṓds/*ped- هندواروپایی است (پوکورنی ۷۹۰–۷۹۱: «lat. pēs, pedis ds.»). اما ped-yôs واژهٔ لاتینی نیست، بلکه صورت تفضیلیِ پیشالاتینی *ped-yōs است که به peior «بدتر» می‌رسد (با تحول -dy- به -i-: *pedyōs > *peiiōs > peior)، و در برابرش صیغهٔ عالی *ped-samos > pessimus «بدترین» می‌ایستد؛ معنا از سویهٔ فعلیِ ریشه می‌آید: «لغزیدن، افتادن» ← «بدتر درآمدن». کلاین ذیل pejorative می‌نویسد: «peior \\\"بدتر\\\" که به‌جای *ped-yos است و با pessimus \\\"بدترین\\\" (از *ped-semos) و pessum \\\"رو به پایین\\\" خویشاوند است و با padyate سنسکریت \\\"می‌افتد\\\" هم‌ریشه؛ از همان پایهٔ pes, pedis \\\"پا\\\"». واتکینز نیز همین را ذیل ped-1 بند دوم می‌گوید. پس معنی «پست‌ترین، بدترین» که نورایی برای ped-yôs آورده درست است؛ تنها برچسب زبان کمی سهل‌انگارانه است، چون این صورتی بازسازی‌شده است نه لاتینیِ گواهی‌شده.\",\n    \"sources\": [],\n    \"ref_check\": [\n     {\"ref\": \"KLN:1166\", \"status\": \"supports\", \"note\": \"Klein, s.v. pejorative (KLN_1966.txt leaf 613) and pessimism (leaf 622 ≈ printed pp.1150 and 1168, i.e. the 1160s block Nourai cites): 'peior ... stands for *ped-yos and is rel. to L. pessimus, \\\"worst\\\" (for *ped-semos ...) ... from the same base as L. pes, gen. pedis, \\\"foot\\\" (see Walde-Hofmann, LEW., II, p.275 s.v. peior, p.296 s.v. pessum, and p.295 s.v. pes)'; 'pessimism ... fr. L. pessimus, \\\"worst\\\", which stands for *ped-ssmos, and is rel. to pejor (for *ped-yōs)'.\"},\n     {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. ped-1, II.2: 'Latin *ped- in: a. suffixed (comparative) form *ped-yos in Latin peior, worse (< \\\"stumbling\\\"): PEJORATION; IMPAIR; b. suffixed (superlative) form *ped-samo- in Latin pessimus, worst: PESSIMISM.' (Nourai cites AHD without a page, i.e. the IE-roots appendix.)\"}\n    ],\n    \"consulted\": [\n     {\"src\": \"LAT\", \"where\": \"Ernout-Meillet, Dictionnaire étymologique de la langue latine, s.v. peior / pessimus (LAT.txt lines 46255-46258)\", \"stance\": \"supports\", \"note\": \"'peior (c.-à-d. peiior), -oris, n. peius adj. comp.: pire, plus mauvais. pessimus (pessu-), -a, -um superl.: le pire ... L'e de peior est bref de nature'.\"},\n     {\"src\": \"IEC\", \"where\": \"Mann s.v. ped-, pēd- (IEC.txt 12562)\", \"stance\": \"supports\", \"note\": \"'Lat. pēs, gp: pedum, m. id.; peda f. \\\"pace\\\" ... pedes, adv. \\\"on foot\\\"; prope \\\"near\\\"; ... peior, adj. \\\"worse\\\"; cf. op-pidum, n. \\\"walled town\\\"' — peior listed under the foot root.\"},\n     {\"src\": \"POK\", \"where\": \"IEW p.790-791\", \"stance\": \"supports\", \"note\": \"'lat. pēs, pedis ds.' and, in the verbal section, the 'gehen, fallen' semantics that underlie peior/pessimus.\"},\n     {\"src\": \"LEW\", \"where\": \"Walde-Hofmann LEW II 275 (peior), 295 (pes), 296 (pessum), as cited by Klein\", \"stance\": \"supports\", \"note\": \"Klein's cross-reference is to exactly these pages of the standard Latin etymological dictionary.\"}\n    ]\n   },\n   {\n    \"id\": 11,\n    \"lang\": \"English\",\n    \"words\": \"dispatch, impede, pedestrian, pessimism, pedicure\",\n    \"verdict\": \"plausible\",\n    \"derivation\": \"Four of the five are straightforward and are listed under Watkins' ped-1: impede < Latin impedīre 'to shackle the feet, hinder' (in- + pes/pedis); pedestrian < Latin pedester, -tris 'going on foot' (17th-c. Latinism); pedicure < French pédicure, coined from Latin pes/pedis + cūrāre 'to care for' (19th c.); pessimism < Latin pessimus 'worst' (< *ped-samos), a word first used in English by Coleridge (Klein s.v. pessimism). The fifth, dispatch, is the weak link: Skeat derives it from Old French despeechier / Spanish despachar, from a Late Latin *dis-pedicāre 'to unfetter', beside impedicāre, 'from L. pedica, a clog, which is from L. ped-, stem of pes, foot' (Skeat s.v. despatch, and 'Dispatch: see Pedal'), and Watkins likewise puts DISPATCH under *ped-ikā- in Latin pedica. Etymonline, however, records that 'its exact source and meaning is uncertain' and that the pedica derivation is only one of the competing proposals for the second element of Spanish despachar / Italian dispacciare. Hence 'plausible' for the node as a whole.\",\n    \"derivation_fa\": \"چهار واژه از پنج واژهٔ این گره روشن است و واتکینز همه را ذیل ped-1 آورده است: impede از impedīre لاتین «به پا بند نهادن، بازداشتن» (in- + pes/pedis)؛ pedestrian از pedester لاتین «پیاده‌رو» (وام‌گیری کتابی سدهٔ هفدهم)؛ pedicure از pédicure فرانسه، ساخته از pes/pedis و cūrāre «پرستاری کردن» (سدهٔ نوزدهم)؛ و pessimism از pessimus لاتین «بدترین» (از *ped-samos) که نخستین‌بار کالریج در انگلیسی به کار برد (کلاین ذیل pessimism). حلقهٔ سست، dispatch است: اسکیت آن را از despeechier فرانسهٔ کهن و despachar اسپانیایی می‌گیرد و آن را به *dis-pedicāre لاتین متأخر «از بند رها کردن» می‌رساند، از pedica «پای‌بند» که خود از ped- «پا» است؛ واتکینز هم DISPATCH را ذیل *ped-ikā- می‌گذارد. ولی اتیمانلاین می‌نویسد «خاستگاه و معنی دقیق آن نامعلوم است» و ریشهٔ pedica تنها یکی از چند پیشنهاد برای جزء دوم است. از این رو داوری این گره «با احتیاط پذیرفتنی» است.\",\n    \"sources\": [E_DIS],\n    \"ref_check\": [\n     {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this node (refs=None); the checks below are the independent ones.\"}\n    ],\n    \"consulted\": [\n     {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etymological Dictionary, s.v. despatch/dispatch (SKT.txt line 13599) and the cross-reference 'Dispatch: see Pedal' (line 5176)\", \"stance\": \"supports\", \"note\": \"'O.F. despeechier ... answering to Low L. *dispedicare and impedicare ... both from L. pedica, a clog, which is from L. ped-, stem of pes, foot. See impeach.'\"},\n     {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. ped-1, I.5-6 and II.2\", \"stance\": \"supports\", \"note\": \"'5. Form *ped-yo- in ... b. Latin impedire, \\\"to put in fetters,\\\" entangle, hinder: IMPEDE. 6. Suffixed form *ped-ikā- in Latin pedica, fetter, snare: DISPATCH, IMPEACH' and '*ped-samo- in Latin pessimus, worst: PESSIMISM'; PEDESTRIAN, PEDI- also listed under I.4.\"},\n     {\"src\": \"KLN\", \"where\": \"Klein s.v. foot and s.v. pessimism (leaves 330, 622)\", \"stance\": \"supports\", \"note\": \"Klein's list at 'foot' includes 'expedient, expedite, impeach, impede, impedimenta ... pedal, pedate, -pede ... Cp. also pejorative, pessimism' — all the node's words except dispatch, which he treats s.v. despatch.\"},\n     {\"src\": \"PEI\", \"where\": \"Etymonline, s.v. dispatch (archived)\", \"stance\": \"partial\", \"note\": \"'its exact source and meaning is uncertain ... Another says it is Latin -pedicare \\\"to entrap\\\" (from Latin pedica \\\"shackle\\\")' — the ped- derivation is one proposal among several.\"}\n    ]\n   }\n  ]\n }\n ]\n}\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-383.json\",\"w\",encoding=\"utf-8\") as f:\n    json.dump(doc, f, ensure_ascii=False, indent=1)\n    f.write(\"\\n\")\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-383.py"
}
```


### [2026-09-07T20:59:15.015Z] TOOL RESULT

```
ok
```


## [2026-09-07T20:59:18.736Z] TOOL CALL #87: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-383.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 383"
}
```


### [2026-09-07T20:59:20.112Z] TOOL RESULT

```
JSON OK
nodes verified: 13/13
node verdicts: {'plausible': 5, 'disputed': 1, 'confirmed': 7}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 15, 'partial': 5, 'not_found': 1, 'not_checked': 4}
books consulted: {'partial': 9, 'supports': 31, 'silent': 6, 'contradicts': 1} | by book: {'BRT': 4, 'HUB': 4, 'PHD': 4, 'MON': 3, 'HRN': 3, 'IEC': 3, 'KLN': 3, 'BQT': 2, 'FRS': 2, 'POK': 2, 'NYB': 2, 'AHD': 2, 'SKT': 2, 'SOD': 2, 'WLD': 1, 'SYN': 1, 'KNT': 1, 'AID': 1, 'HJB': 1, 'HENNING': 1, 'LAT': 1, 'LEW': 1, 'PEI': 1}
```


## [2026-09-07T20:59:27.141Z] TOOL CALL #88: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json,io\np='data/verification/page-383.json'\nd=json.load(open(p,encoding='utf-8'))\nfor e in d['entries']:\n    for n in e['nodes']:\n        for c in n.get('consulted',[]):\n            if c['src']=='PEI':\n                c['src']='ETYMONLINE'\njson.dump(d, io.open(p,'w',encoding='utf-8'), ensure_ascii=False, indent=1)\nopen(p,'a',encoding='utf-8').write(\"\\n\")\nprint('done')\nEOF\npython3 tools/verify_check.py 383"
}
```


### [2026-09-07T20:59:28.468Z] TOOL RESULT

```
done
nodes verified: 13/13
node verdicts: {'plausible': 5, 'disputed': 1, 'confirmed': 7}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 15, 'partial': 5, 'not_found': 1, 'not_checked': 4}
books consulted: {'partial': 9, 'supports': 31, 'silent': 6, 'contradicts': 1} | by book: {'BRT': 4, 'HUB': 4, 'PHD': 4, 'MON': 3, 'HRN': 3, 'IEC': 3, 'KLN': 3, 'BQT': 2, 'FRS': 2, 'POK': 2, 'NYB': 2, 'AHD': 2, 'SKT': 2, 'SOD': 2, 'WLD': 1, 'SYN': 1, 'KNT': 1, 'AID': 1, 'HJB': 1, 'HENNING': 1, 'LAT': 1, 'LEW': 1, 'ETYMONLINE': 1}
```


## [2026-09-07T20:59:48.907Z] AGENT

Page 383 (book p. 353) verified: `data/verification/page-383.json`, `verify_check.py 383` shows 0 PROBLEM lines.

**Counts** — 2 non-redirect entries, 13 nodes. Roots: 2 confirmed. Nodes: 7 confirmed, 5 plausible, 1 disputed. Ref checks: 15 supports, 5 partial, 1 not_found, 4 not_checked. 23 distinct books consulted.

**Disputed**
- Parvan → #2 Persian `پژ / پاپژ / پژواک`: all three words exist (Borhan p.399 has پژ "زمین پست و بلند و کوه و کتل" with Nourai's Khosravānī verse; p.401 has پژواک), but the Avestan source is wrong. `paurvatā-` cannot give `paž` phonetically (OIr. -rv- → NP -hl-/-rv-, -t- → -d-/-y-, never -ž-), and پژواک is *pati-vāka- "answering voice": the prefix پژ-/پچ- < OIr. *pati- (as in پژوهیدن، پاسخ), not پژ "mountain". Only the second element واک (Nourai's ☞Wekw) is right.

**Notable book errors (not extraction errors — the print matches the JSON)**
- Parvan #1: `paurvatâ-vac` "sound of mountains, echo" is labelled Avestan but is unattested — not in Bartholomae (who has only `paurvatā-` f. "Bergzug, -kette, Gebirg") nor Buck. Nourai's own back-formation, built to feed پژواک. Node marked plausible.
- Ped/Pod #6: `padika, padâtaka` labelled **Avestan**, but neither is Avestan. `*padika-` is Hübschmann/Horn's reconstructed Old Persian (Skt. *padika-*, PSt. no. 359 pp. 45-46); `padātaka-` is Proto-Iranian/Sanskrit (`padāti-, padātika-`). Pokorny 791, the page cited, gives them as `ai.` (Sanskrit). Should read "Sanskrit / reconstructed Old Iranian". Node marked plausible.
- Ped/Pod #10: `ped-yôs` labelled Latin; it is the pre-Latin *ped-yōs behind `peior` (Klein, Watkins). Gloss "lowest, worst" is right; node still confirmed.
- Ped/Pod #5: پی‌جامه/پیژامه is a re-borrowing, but the -ž- points to French *pyjama*, not English *pajamas*. Marked plausible.

**No extraction errors** — the page image (`site/pages/383.jpg`) matches the JSON node-for-node, including refs, Persian script and the `script_extra` fields.

**Unreachable references**: `SLW:98` (Henning, BSOAS 10 — Cambridge PDF 403, article not readable in the local Selected Papers OCR), `AHD:943` (1975 New College main word-list, not on disk), `BQT:345` (پاپژ; printed p.345 exists but the vol.-1 OCR of that leaf is fragmentary → not_found), `BQT:367`, `MON:868,902` (6-vol Mo'in not online; the 2-vol condensation has the پی‌جامه entry).
