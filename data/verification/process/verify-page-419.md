# Verification process log — verify-page-419


## [2026-09-14T01:21:24.890Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 419 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-419.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-419.json. Write /home/sfmqrb/git/rishe/data/verification/page-419.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 419` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T01:21:25.911Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T01:21:26.759Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T01:21:26.780Z] TOOL RESULT

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


## [2026-09-14T01:21:27.276Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-419.txt"
}
```


### [2026-09-14T01:21:27.303Z] TOOL RESULT

```
1	=== PDF page 419 (book page 389) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Rei 1 : possession  (refs POK:860)
4	#1 (parent #0) [Avestan] refs=POK:860 | râ 2 : to give ; râiti, a-râiti 2 : generous ☞Apo ; raĕvant : rich
5	  #2 (parent #1) [Persian] refs=BQT:926 | râd «راد ۲» : generous
6	#3 (parent #0) [Latin] refs=AHD | rěs : thing
7	  #4 (parent #3) [English] refs=None | real, republic
8	--- entry 1 ---
9	ROOT [Indo-European] Rei 2, Reig : to scratch, tear, cut; Rekp: to pull, break  (refs POK:857; IEC:1067)
10	#1 (parent #0) [Avestan] refs=POK:858 | raesah, raeš : wound, injury
11	  #2 (parent #1) [Persian] refs=BQT:988 | rîš 1 «ریش ۱» : wound, wounded
12	#3 (parent #0) [Avestan / Old Persian] refs=FFD:56 | riš 2, rîz : to spin threads
13	  #4 (parent #3) [Persian] refs=BQT:951; HUB:12; FFD:56 | rîštan «ریشتن (رشتن ، رشته)» : to spin threads ; rîsîdan «ریسیدن (ریسمان ، ریسندگی)» : to spin threads ; abrîšam «ابریشم» : silk
14	#5 (parent #0) [Persian] refs=IEC:1067 | rîzeh «ریزه» : fragment, small piece ; rîz 2 «ریز» : small (piece)
15	#6 (parent #0) [Sanskrit] refs=POK:858; HRN:17,137 | rěš, ričate : to tear ; lěkha : to sketch, design
16	  #7 (parent #6) [Sogdian] refs=SOD:148 | dykh : letter
17	#8 (parent #0) [Germanic] refs=AHD | raigwa : row ; raipaz : rope ; rîp : ready to be reaped
18	  #9 (parent #8) [English] refs=None | row, rope, ripe
19	#10 (parent #0) [Latin] refs=AHD | rîpa : land cut by water flow
20	  #11 (parent #10) [English] refs=None | river, arrive
21	#12 (parent #0) [Greek] refs=AHD | replon : to remove seeds
22	  #13 (parent #12) [English] refs=None | ripple
23	--- entry 2 ---
24	ROOT Reig -> redirect to Rei 2
25	
```


## [2026-09-14T01:21:30.373Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-419.json",
 "description": "Read page 419 source JSON"
}
```


### [2026-09-14T01:21:30.410Z] TOOL RESULT

```
{
  "pdf_page": 419,
  "book_page": 389,
  "entries": [
    {
      "root": {
        "name": "Rei 1",
        "lang": "Indo-European",
        "refs": "POK:860",
        "gloss": "possession"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:860",
          "words": [
            {"translit": "râ 2", "gloss": "to give", "script": null},
            {"translit": "râiti, a-râiti 2", "gloss": "generous", "script": null, "see": ["Apo"]},
            {"translit": "raĕvant", "gloss": "rich", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:926",
          "words": [
            {"translit": "râd", "gloss": "generous", "script": "راد ۲"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "rěs", "gloss": "thing", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "real, republic", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Rei 2, Reig",
        "lang": "Indo-European",
        "refs": "POK:857; IEC:1067",
        "gloss": "to scratch, tear, cut; Rekp: to pull, break"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:858",
          "words": [
            {"translit": "raesah, raeš", "gloss": "wound, injury", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:988",
          "words": [
            {"translit": "rîš 1", "gloss": "wound, wounded", "script": "ریش ۱"}
          ],
          "note": null,
          "quote": {"text": "تو که مرحم نه ای زخم دلم را - نمک پاش دل ریشم چرایی", "poet": "Bâbâ Tâher"}
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "FFD:56",
          "words": [
            {"translit": "riš 2, rîz", "gloss": "to spin threads", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "BQT:951; HUB:12; FFD:56",
          "words": [
            {"translit": "rîštan", "gloss": "to spin threads", "script": "ریشتن (رشتن ، رشته)"},
            {"translit": "rîsîdan", "gloss": "to spin threads", "script": "ریسیدن (ریسمان ، ریسندگی)"},
            {"translit": "abrîšam", "gloss": "silk", "script": "ابریشم"}
          ],
          "note": null,
          "quote": {"text": "قدح مگیر چو حافظ مگر بناله چنگ - که بسته اند بر ابریشم طرب دل شاد", "poet": "Hâfez"}
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Persian",
          "refs": "IEC:1067",
          "words": [
            {"translit": "rîzeh", "gloss": "fragment, small piece", "script": "ریزه"},
            {"translit": "rîz 2", "gloss": "small (piece)", "script": "ریز"}
          ],
          "note": null,
          "quote": {"text": "سپهر برشده پرویز نیست خون افشان - که ریزه اش سرکسرئ و تاج پرویز است", "poet": "Hâfez"}
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK:858; HRN:17,137",
          "words": [
            {"translit": "rěš, ričate", "gloss": "to tear", "script": null},
            {"translit": "lěkha", "gloss": "to sketch, design", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Sogdian",
          "refs": "SOD:148",
          "words": [
            {"translit": "dykh", "gloss": "letter", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "raigwa", "gloss": "row", "script": null},
            {"translit": "raipaz", "gloss": "rope", "script": null},
            {"translit": "rîp", "gloss": "ready to be reaped", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "row, rope, ripe", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "rîpa", "gloss": "land cut by water flow", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "river, arrive", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "replon", "gloss": "to remove seeds", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 12,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "ripple", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Reig",
        "redirect": "Rei 2"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-14T01:21:30.990Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-14T01:21:31.036Z] TOOL RESULT

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


## [2026-09-14T01:21:54.518Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','BQT','IEC','SOD','HUB','HRN','FFD','AHD','MON','ARY','WLD','BRT','PHD','NYB','CHEUNG','KLN','SKT','SYN','LEW','LAT']:\n    v=d.get(k)\n    print('==',k,json.dumps(v,ensure_ascii=False)[:700])\n\""
}
```


## [2026-09-14T01:21:55.142Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo ---- && python3 tools/verify_check.py --help 2>&1 | head -20"
}
```


### [2026-09-14T01:21:55.757Z] TOOL RESULT

```
== POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index 
== BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.c
== IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstruct
== SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get s
== HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by parag
== HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the 
== FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/ref
== AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifie
== MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol 
== ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", "local_file": ["/home/sfmqrb/git/rishe/
== WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015
== BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between 
== PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<ident
== NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's 'NYB' nu
== CHEUNG null
== KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO pri
== SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i
== SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i
== LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.o
== LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for most of the book (e.g. leaf 21 = p.3); drifts in places (leaf 219 = p.301 -> -82?? probably a mis-detec
```


### [2026-09-14T01:21:56.859Z] TOOL RESULT

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
----
Traceback (most recent call last):
  File "/home/sfmqrb/git/rishe/tools/verify_check.py", line 98, in <module>
    sys.exit(main(sys.argv))
             ^^^^^^^^^^^^^^
  File "/home/sfmqrb/git/rishe/tools/verify_check.py", line 21, in main
    only = set(int(a) for a in argv[1:])
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/sfmqrb/git/rishe/tools/verify_check.py", line 21, in <genexpr>
    only = set(int(a) for a in argv[1:])
               ^^^^^^
ValueError: invalid literal for int() with base 10: '--help'
```


## [2026-09-14T01:21:59.066Z] TOOL CALL #7: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-14T01:21:59.109Z] TOOL RESULT

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


## [2026-09-14T01:22:00.242Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"rēi-\\|rēi- *:\\|Besitz, Sache\" POK_full.txt | head -20"
}
```


### [2026-09-14T01:22:00.314Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T01:22:06.469Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in POK_01.txt POK_02.txt POK_03.txt POK_full.txt; do echo \"== $f $(wc -c <$f)\"; grep -n \"Besitz, Sache\" $f | head -5; done"
}
```


## [2026-09-14T01:22:07.248Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ritzen, reißen\" POK_full.txt POK_02.txt POK_03.txt 2>/dev/null | head -10"
}
```


### [2026-09-14T01:22:07.610Z] TOOL RESULT

```
== POK_01.txt 981836
== POK_02.txt 1137861
== POK_03.txt 1170809
== POK_full.txt 3971883
```


### [2026-09-14T01:22:07.673Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T01:22:12.002Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=92 && NR<=100 {print \"----LEAF \" NR-1; print substr($0,1,1200)}' POK_03.txt"
}
```


### [2026-09-14T01:22:13.107Z] TOOL RESULT

```
----LEAF 91
 spor  ,die  Spur  verfolgen',  mnd. reke  L  (*raki)  ,Reihe,  Ordnung',  raken  ,treffen,  erreichen';  ags.  racit  f. ,Erzählung,  Bericht',  as.  raka,  ahd.  rahha  ,Rechenschaft,  Sache',  aisl.  rgk Nom.  PL  ,Ursprung,  Ursache,  Grund';  aisl.  rakr,  fries.  mnd.  rak  ,gerade," recht'  (=  lat.  rogus)]  e-stufig:  mhd.  gerech  ,wohlgeordnet',  as.  rekön  ,richteii, ordnen',  mnd.  reken  ,richtig,  unbehindert,  offen',  ahd.  rehhanön  ,ordnen, rechnen,  Rechenschaft  ablegen',  ags.  ge-recenian  ,erklären',  engl,  reckon ,wofür  halten*;  ags.  recen  ,schnell,  bereit';  aisl.  land-reki  ,König',  ahd. anet-rehho  ,Enterich';  ob  mit  der  Anschauung  der  zum  Zusammenscharren ausgereckten  Hand  die  Sippe  von  got.  rikan  ,anhäufen',  mhd.  rechen' ,zusammenscharren,  anhäufen,  sammeln',  aisl.  raka,  mnd.  raken  (*rakSn) ,(zusammen)scharren',  aisl.  reka,  ahd.  rehho  ,Rechen,  Harke',  as.  reka  f. ,Rechen',  as.  raka,  ags.  racu,  schwed.  raka  f.  ds.,  e-stufig:  norw.  dial. raak  f.  ,Spur,  Streif,  Furche,  Reihe',  isl.  räk  f.  ,Streif'  (vgl.  ai.  räji-,  rö/l , Streifen,  Reihe')  hierher  gehört,  ist  zweifelhaft;  du
----LEAF 92
 ags.  reg{e)nj  ren  m.,  ahd.  regan^ regin,  regen,  mhd.  regen  m. ;  aisl.  rigna  ,regnen',  ahd.  reganon  ds.  usw. ;  lit. (mit  westidg.  /j?)  rokia,  rökii  ,fein  regnen',  rÖke  , Staubregen'.
WP.  II  365  f.,  WH.  II  435.
reglos-  n.  ,Dunkelheit',  *erg!i- :  org!^-  ,dunkel'?
Ai.  rdjani-  ,Nacht';  gr.  SQeßog  ,Dunkel  der  Unterwelt'  (I- Vorschlag) ; arm.  erek  und  erekoy  ,Abend';  auch  Adverb  erek  , gestern';  got.  riqis, -izis  n.  , Dunkel',  nisl.  rokkr,  -rs  ,Dunkel,  Dämmerung';  hierher  vielleicht gr.  ÖQcpvog  , dunkel'  {*org'^sno-)  und  toch.  A  orkäm  (*07'g^mo-)  , Finsternis' ; anders  oben  S.  334.
WP.  II  367,  Benveniste  Hirt-Festschrift  2,  236,  Barrow  BSOAS  12,  645  f.
I.  rei-  ^ritzen,  reißen,  schneiden' ;  rei-kä  ,Riß,  Spalte^,  rei-pä  ,steiler  Rand',
rei-uä,  roi-uä  , Streifen'.
Lat.  rlma  ,Ritze'  (*rei-ma)',  mir.  reo  ,Streifen'  (*H-wo-);   ags.  räw,  rxw
f.    ,Reihe'   (*roi-ua) ;    lit.   rievä   ,Felskluft,  Fels,  Hügel'   (vgl.  lat.  rumpö :
rüpes),  raive  , Streifen',   lett..  rieii;a   ,Ritze,   Falte,  Furche';  dazu  wohl  als
,Grenzstreifen'  oder  , Hügelreihe':  mir. 
----LEAF 93
rze  um  (tr.),  stürze  nieder'  (intr.),  igeiTtia   n.  PI. ,ruinae',    iglrwr]    f.    , Absturz,    iVbhang';    lat.    rlpa    , steiler    Rand,    Ufer'; aschwed.  rlva,  aisl.  rlfa  ,zerreißen  (tr.)',  rifna  ,zerspringen,  aufspringen', rifa  f.  ,Riß,   Spalte',  mnd.  riven  ,reiben',  afries.  rlva  ,reißen',   nd.  ribhen ,pflücken,  Flachs  rupfen';  aisl.  rlfr  , erwünscht'  (vgl.  ,sich  um  etwas  reißen'), ags.  rf/  ,gewaltig,  heftig',  mnd.  rlve  ,versch wenderisch';  ablaut.  aisl.  reifr  ^..^ ,froh,   aufgeräumt',   reifa   , fördern,    beschenken';    ostfries.   riffel  ,Furehe';  %:'-' ags.    ge-riflian    ,runzeln';    mit  p    durch    Konsonantendehnung:    aisl.    rip   s-- ,Oberkante  eines  Bootes',  ostfries.   rip{e)  ,Rand,  Ufer',  mhd.  rlf  ^üfer';  ift
daneben  eine  germ.  Sippe  mit  ,Fetzen,  Streifen'  als  Grundbed.,  so  daß hier  anreihbar,  und  ,wickeln,  binden*  als  abgeleitete  Bed.:  aisl.  rif  n.  ,RefE^ mnd.  riß  ds.,  aisl.  rift  (ript)  f.  , Stück  Zeuges',  rifr  m.  {*riU-)  , Rolle, Weberbaum',  rifa  ,nähen',  ags.  rift  f.  ,Kleid,  Schleier,  Vorhang',  ahd. bein-refta  ,Hosen';  aisl.  r
----LEAF 94
',  mhd.  rist  m.  n.  ,Pflugschar, Pflugsterz';  lett.  risums,  risiens  ,Riß,  Schlitz',  aksl.  resiti  ,lösen'. WP.  II  343  ff.,  WH.  II  435  f.,  436,  438,  Trautmann  241.
2.  rei-f  roi-  in  Worten  für  , buntgestreift,  fleckig';  rei-hho-,  roi-bho-  ds.
Lit.  rai-nas  ,grau,  buntgestreift';  rm-mas  ,bunt';  air.  nahach  , gespren- kelt', lit,  raX-has  , gesprenkelt,  graubunt'  (raibti  , flimmern'),  lett.  räibs ,bunt,  fleckig',  bes.  von  Tieren,  apr.  roaban  , gestreift',  russ.  klr.  ribyj ,bunt';  *roi-ko-  scheint  die  Grundlage  von  ahd.  reh  n.,  reho  m.,  ags.  rä, räha  m.  ,Reh',  aisl.  rä  f.,  ags.  rcege  (*raigjön-),  ahd.  reia^  reia  (unklar)  und nhd.  Ricke,  ndl.  reJcke  ,Ricke',  (expressiv)  wozu  wohl  ai.  risya-  m.  , Anti- lopenbock'.
WP.  II  346,  Trautmann  235  f.,  Specht  Idg.  Dekl.  115.
3.  rei-,  re(i)-  Schallwurzel  , schreien,    brüllen,    bellen'    usw.,   s.   auch  reu-, reu-,  TU-.
Ai.  räyati  ,bellt' ;  lit.  rieju  rieti  , losschreien,  schelten',  refl.  ,sich  zanken'; lett.  reju,  reju,  riet  ,bellen';  ablaut.  räju,  rät  , schelten',  lit.  rojöju,  rojöti ,unordentlich  kr�
----LEAF 95
  f.  _,Besitz,  Reichtum'  in  räh,  räydh  (ursprüngl.  i-Stamm); das  ä  von  räh  nach  dem  Akk.  Sg.  räm,  der  ebenfalls  analogisches  ä  hat (nach  gäm,  oben  S.  482);  rayi-  ,Gabe,  Besitz,  Kleinod'  (av.  Akk.  PI.  raUy leg.  rayls),  rayi-vdnt-j  meist  re-vdnt-  ,reich';  av.  Instr.  Sg.  raya  (leg.  räya) =  ai.  räyä  (zu  rdh)^  av.  raevant  ,reich*;  ai.  av.  rä-  , geben'  (erweitert  ai. räsate  ,gibt'),  ai.  räti-  ,Gabe,  Geber*;  ai.  rata-,  av.  rätö  ,gegeben':
lat.  res,  rei  ,Sache,  Besitz'  (das  enach  dem  Akk.  rem  aus  *reHim?),  umbr. re-per  ,pro  re',  Dat.  Abi.  ri;  dazu  lat.  reus  , Prozesspartei,  der  (die)  Ange- klagte' (*rei'Os) ;  unklar  mcymr.  rei  ^Reichtum'.
WP.  II  343,  WH.  II  430 f.,  432,  Wackernagel-Debrunner  III  214  ff.; 0.  Szemerenyi  nimmt  (brieflich)  mit  Burrow  (Sanscrit  178,  245)  und  Kury- lowicz  ('Etudes  36  f.)  eine  Grundform  "^reHi-  für  das  Nomen  und  *reH- f  ür  das  Verbum  an  (?)
5.  rei-  , stützen*  s.  unter  reid-^  reih  und  rem-,
1.  rei-  :  ri-  ,zählen,  ordnen',  erweitert  rei-dh-,  s.  oben  S.  60.
2.  rei-,  röi-  ,Nuß'  (s.  Trautmann  2
----LEAF 96
elligen,  einfach,  klar';  afries.  rec^e,  ags.  gercede^  rcede ,fertig,  leicht,  klar,  einfach'  (engl,  ready)]  mnd.  gerede,  rede  ,bereit,  fertig'; mhd.  gereit j  gereite  ,fertig,  bereit,  zur  Hand' ;  als  Substantiv  in  aisl.  reidi n.  und  m.  , Ausrüstung*,  norw.  greide  n.  ,Pferdegeschirr' ;  ags.  gercede  n. ^Geschirr,  Rüstung';  mnd.  gerede  ,Gerät,  Aussteuer';  ahd.  gireiti  n.  , Fuhr- werk'; mhd.  gereite  n.  ,Wagen,  Geschirr,  Werkzeug';  aisl.  reidr,  durch- reitbar, bereit';
got.  ga-raidjan  ,anordnen,  festsetzen';  aisl.  greida  ,ordnen,  zahlen,  helfen'; ags.  {ge)röedan  ,ordnen,  helfen';  mhd.  {ge)reiten  , bereiten,  ordnen,  rechnen, zahlen'.
reidhi-  in  ir.  reid  ,planus,  facilis';  acymr.  ruid^  ncymr.  rhwydd  gleicht, frei';  abret.  roed  in  den  PN  Roed-lon,  Roidoc,  Roet-anau,  nbret.  rouez ,rare,  clair-seme';  lett.  raids  , bereit'.
reidho-  in  ir.  7'zad  ,Fahren,  Reiten';  cymr.  gorwydd  ,Pferd';  mlat.-gall. ve-reduSj  para-ve-redus  (aus  *vo-redos)  ,Beipferd';  vgl.  ahd.  ga-rit  n.  ,equi- tatus';  mhd.  In-rit  m.  , Einritt';  mnd.  rit  n.  ,Ritt';
zu  reidh-  auch  das  Abstraktsuffix  cymr.
----LEAF 97
g-),  reig-  etwa  ,recken,  ausstrecken,   mit  ausgestreckter  Hand   langea'
oder  darreichen  u.  dgl.';  bedeutungsverwandt  mit  1.  reg-.
Ahd.  reichen  ,erreichen,  (er) langen,   darreichen,  sich  erstrecken',  mnd.,
recken,  ags.  r'^c{e)an  ,ausstrecken,  reichen,   darbieten'   (engl,  reach),  aisl
reik  f.  , Scheitel  im  Haar';  lit.   reü-iuos,  -tis  ,sich  brüsten',  rdiz-aus,  -ytts
.  ,sich  wiederholt  recken' ;  als  ,Tortur  durch  Strecken  der  Glieder'  scheint
auch   verwandt   air.    riag   ,Tortur',    ringid    ,foltert,    peinigt';   mir.   reimm
,Possenreißer'    {*reig-smi-),    mcymr.    dir-rwyn    i*reig-no-)    ,Tortur,    Leid';
cyf-rwyn-ein  ds.
WP.  II  347  f.,  Trautmann  242,  Loth  RC.  42,  373.
reio-,  ri-  ,bewegen,  fließen'  s.  oben  S.  330  f.
reik-  ,sich  aufrecken'  und  ,wackeln';  , Stange,  Latte'.
Norw.  rjaa  m.  , Stange  zum  Trocknen  des  Getreides'  (*nÄan-),  schwed. dial.  ri  f.  ,Pfahl,  Stange' ;  mnd.  7'icÄ;,  reck  n.  (*rikkö-)  ,lange  dünne  Stange', mhd.  ricy  -ckes  m.  ,waagrechtes  Gestell,  Stange',  nhd.  Reck;  ahd.  rigil  m., mnd.  regel  m.  ,Riegel,  Reeling',  nnd.  auch  rlchel,  �
----LEAF 98
r  mhd.  rogel  ,nicht  fest,  schwankend',  sich  rugelen  ,sich rühren',  nhd.  dial.  rogeln  ,wackeln',  aisl.  vugla  ,in  Unordnung  bringen, stören';  geminiert  rugga  , schaukeln,  bewegen*;  rykkia  ,rücken,  eilen',  ags. roccian  , schaukeln'  (engl,  rock)^  ahd.  rucken,  nhd.  ^rücken^,  aisl.  ryJckr, ahd.  ruc  m.  ,Ruck'  i^rukki-) ;
lit.  rekles  , Stangengerüst  zum  Trocknen,  Räuchern'.
WP.  II  361  f..  Wissmann  Nom.  postverb.  176.
2.  rek-  , anordnend
Ai.  racayati  ^verfertigt,  bildet',  racana-  n.  ,Ordnen,  Betreiben';  got. rahnjan  ,rechnen';  ragin  n.  ,Rat,  Beschluß',  aisl.  regin,  PL  rggn  ,die  rat- schlagenden Mächte,  Götter',  as.  ragino  giscapu  ,  Beschlüsse  der  göttlichen Mächte',  ahd.  regin-  in  Eigennamen;  aksl.  rokh  m.  , bestimmte  Zeit,  Ziel', rekq,  restij  , sagen',  raknqti,  raSiti  ,wollen'  usw. ;  toch.  A  rake,  B  reki^ PI.  rekauna  ,Wort';
mit  e:  got.  ga-rehsns  f.  , Bestimmung,  Ratschluß';  aksl.  riöh  f.  ,accusatio';
ganz  unsicher  Zusammengehörigkeit  mit  aisl.  rän  n.  ,Raub'  (*rahna-)j r'cena  , rauben'  (^rahnjan),  ahd.  bi-rahanen  ,erbeuten';  Grundbedeutung wäre  ,Ra
----LEAF 99
-  n.  ,Ruhe,^ Friede',  npers.  räm  ,Ruhe;  fröhlich,  heiter';  ai.  rdnti  f.  ,Erquickun^ Ergötzung',  ramsu  Adv.  ,erfreulich';  rata-  , stehen  geblieben,  sich  genügen lassend,  sich  ergötzend',  rata-  n.  ,Liebeslust',  rdti-  f.  ,Rast,  Ruhe,  Lust';
mit  unklarem  rj:  gr.  '^qe^iay  -ag  , ruhig,  sanft,  leise',  '^QSj.iccLog  »ruhig', flQeixearsQog  Kompar.  (vgl.  den  es-St.  got.  rimis)]
air.  fo-rim-  ,setzen,  legen'  (ursprüngl.  *,stützen' ;  ri-  =  f-) ;  vielleicht mir.  rinde  ,Gefäß';
ahd.  rama  , Stütze,  Gestell,  Webe-  oder  Stickrahmen',  mnd.  ramty (=  mnd.  mhd.  reme),  ramen  ds.;  got.  rimis  n.  ,Ruhe';  aisl.  rgnd  f.  ,Rand, Saum,  Schild',  ags.  rand  m.  , Schildrand,  Schild',  ahd.  rant  m.  ,Rand/^ Einfassung,  Schild',  norw.  rande  und  ablaut.  rinde  , Erdrücken,  Bank', krimgot.  rintsch  ,mons',  span.  (*got.)  randa  ,Leiste';  norw.  rand  f.  ,Quer- balken,  Sims',  nhd.  bair.  ranten  , Stange'  (:  lit.  ramtiSj  ramstis  ,Stütze,  Ge- länder'); ahd.  ramft  ,Rand,  Einfassung'  kann  *rom-ti-  sein,  aber  allenfalls auch  auf  der  Erw.  rem-hh-  beruhen,  vgl.  ai.  rambhd-  m.  ,Stab,  Stütze'
```


## [2026-09-14T01:22:24.154Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=93 && NR<=96 {print \"----LEAF \" NR-1 \" (p.\" NR-1+765 \")\"; print}' POK_03.txt"
}
```


### [2026-09-14T01:22:25.321Z] TOOL RESULT

```
----LEAF 92 (p.857)
 ags.  reg{e)nj  ren  m.,  ahd.  regan^ regin,  regen,  mhd.  regen  m. ;  aisl.  rigna  ,regnen',  ahd.  reganon  ds.  usw. ;  lit. (mit  westidg.  /j?)  rokia,  rökii  ,fein  regnen',  rÖke  , Staubregen'.
WP.  II  365  f.,  WH.  II  435.
reglos-  n.  ,Dunkelheit',  *erg!i- :  org!^-  ,dunkel'?
Ai.  rdjani-  ,Nacht';  gr.  SQeßog  ,Dunkel  der  Unterwelt'  (I- Vorschlag) ; arm.  erek  und  erekoy  ,Abend';  auch  Adverb  erek  , gestern';  got.  riqis, -izis  n.  , Dunkel',  nisl.  rokkr,  -rs  ,Dunkel,  Dämmerung';  hierher  vielleicht gr.  ÖQcpvog  , dunkel'  {*org'^sno-)  und  toch.  A  orkäm  (*07'g^mo-)  , Finsternis' ; anders  oben  S.  334.
WP.  II  367,  Benveniste  Hirt-Festschrift  2,  236,  Barrow  BSOAS  12,  645  f.
I.  rei-  ^ritzen,  reißen,  schneiden' ;  rei-kä  ,Riß,  Spalte^,  rei-pä  ,steiler  Rand',
rei-uä,  roi-uä  , Streifen'.
Lat.  rlma  ,Ritze'  (*rei-ma)',  mir.  reo  ,Streifen'  (*H-wo-);   ags.  räw,  rxw
f.    ,Reihe'   (*roi-ua) ;    lit.   rievä   ,Felskluft,  Fels,  Hügel'   (vgl.  lat.  rumpö :
rüpes),  raive  , Streifen',   lett..  rieii;a   ,Ritze,   Falte,  Furche';  dazu  wohl  als
,Grenzstreifen'  oder  , Hügelreihe':  mir.  röen  ,Weg,  Bergkette'  (davon  röenaid
858
,*bahnt  sich  einen  Weg'  >  .besiegt^  roen  »Niederlage^;  bret.  run  ,HügelY aisl.  rein  f.  .Grenzstreifen',  ahd.  rein,  nhd.  Rain  ds.  (kelto-germ.  *roi-no,^
•  Erweiterungen:
reib- :  ags.  r'tpan,  riopan  ,ernten^  (engl-  reap),  rifter  ,SicbeF,  rfp  ^^ ,Ernte',  norw.  ripa  ,ritzen^,  ripa  ^abreißen,  abstreifen',  mengl.  ripeUn, nengl.  ripple  ^Flachs  brechen',  mnd.  repen,  rejpelen  ds.,  ahd.  rifila,  riffil^ ,Säge,  gezackter  Berggrat';  as.  ripi,  ags.  rlpe,  ahd.  rlfi,  nhd.  -rei/ (,zam Ernten  reif).
reig-  s.  unter  besonderem  Schlagwort.
reik(b)-  :  ai.  rikhdti,  likhdti  , ritzt',  reJchd,  lekhä  ,Riß,  Strich,  Linie*; gr.  igsiytü)  ,zerbreche,  zerreiße',  i]Qiy.s  ,bc';rst',  igeiy.igj  igiKig,  -iöoc  ,ge- schrotete  Gerste'  (-^-Schreibung  für  -sl-);  vielleicht  lat.  rixa  ,tätlicher Zank,  Streit';  cymr.  rhwygo  ,zerreißen',  rhicyg  m.  ,Bruch,  Spalte',  mbret. roegaff  ,zerreiße',  nbret.  reuga;  ablaut.  mcymr.  go-rugaw  ,zerreißen';  mhd. rihe  ,Linie',  nhd.  Eeihe^  ahd.  rlhan  ,auf  einen  Faden  ziehen',  mit  Ablaut und  gramm.  Wechsel  ahd.  riga  , Linie',  mhd.  rige  , Linie,  Reihe,  künst- licher Wassergraben',  nhd.  Biege]  norw.  reig  m.  ,Reihe,  Zeile';
lit.  riekiü,  riekti  ,(Brot) schneiden,  zum  erstenmal  pflügen',  riekl  ,Brot- schnitte',  raikaü,  -yti  ,Brot  mehrfach  in  Schnitten  schneiden';
ähnlich  reik-  in  ai.  risdtij  lisdti  ,rupft,  reißt  ab,  weidet  ab'  (npers. ristan  ,spinnen',  bal.  resag,  resay  ,spinnen,  flechten').
reip-:  gr.  egeifco)  , stü
----LEAF 93 (p.858)
rze  um  (tr.),  stürze  nieder'  (intr.),  igeiTtia   n.  PI. ,ruinae',    iglrwr]    f.    , Absturz,    iVbhang';    lat.    rlpa    , steiler    Rand,    Ufer'; aschwed.  rlva,  aisl.  rlfa  ,zerreißen  (tr.)',  rifna  ,zerspringen,  aufspringen', rifa  f.  ,Riß,   Spalte',  mnd.  riven  ,reiben',  afries.  rlva  ,reißen',   nd.  ribhen ,pflücken,  Flachs  rupfen';  aisl.  rlfr  , erwünscht'  (vgl.  ,sich  um  etwas  reißen'), ags.  rf/  ,gewaltig,  heftig',  mnd.  rlve  ,versch wenderisch';  ablaut.  aisl.  reifr  ^..^ ,froh,   aufgeräumt',   reifa   , fördern,    beschenken';    ostfries.   riffel  ,Furehe';  %:'-' ags.    ge-riflian    ,runzeln';    mit  p    durch    Konsonantendehnung:    aisl.    rip   s-- ,Oberkante  eines  Bootes',  ostfries.   rip{e)  ,Rand,  Ufer',  mhd.  rlf  ^üfer';  ift
daneben  eine  germ.  Sippe  mit  ,Fetzen,  Streifen'  als  Grundbed.,  so  daß hier  anreihbar,  und  ,wickeln,  binden*  als  abgeleitete  Bed.:  aisl.  rif  n.  ,RefE^ mnd.  riß  ds.,  aisl.  rift  (ript)  f.  , Stück  Zeuges',  rifr  m.  {*riU-)  , Rolle, Weberbaum',  rifa  ,nähen',  ags.  rift  f.  ,Kleid,  Schleier,  Vorhang',  ahd. bein-refta  ,Hosen';  aisl.  reifar  PI.  f .  ,Wickel',  reifa  ,wickeln',  ags.  ä-räfian ,loswickeln'  (ähnlich  ndl.  dial.  rijvelen  ,ausfasern');
mit  Konsonantendehnung  -p(p)-:  got.   skauda-raip  ,Schuhriemen',   aisl.   "*" reip,  ags.  räp  ,Strick,  Seil',  ahd.  reif  ,Riemen,  Faßreif,  Ring';
mit   germ.   -sp-  (aus  -ps-?):    aisl.    rispa   ,auf reißen'   und   f.  rispa   ,ein    ^^
859
leichter  Kratzer^^  aschwed.  risjpa  ,Zwist^^  nd.  ris'pe  , Flach sraufe^^,  rissen den  Flachs  durch  die  Raufe  ziehen^  (nhd.  Rispe  ,Samenbüschel^  aber ^ohl  mit  ursprüngl.  Ar-),  ahd.  risjpeln  ^zusammenraffen^,  bair.  ab-reispen abzupfen,  abbrechen^,  mhd.  be-rispeln  ^tadeln,  bestrafend
reis-:  ai.  risyati,  resati  ,wird  versehrt,  nimmt  Schaden;  beschädigt', ristd-  ,versehrt^,  resayati  ^schädigt,  straft^,  risanydti  ,geht  fehP,  risanyü- ,unzuverlässig';  av.  raes-^  irü-  ^verletzen,  verwunden;  Schaden  leiden' (Präs.  raesyeiti  tr.,  irüyeiti  tr.,  intr.,  Kaus.  raesayeiti),  Partiz.  irista-  , be- schädigt^, rae§a-  m.,  raesah-  n.  ^Schädigung',  wohl  auch  raesa-  ,Spalt  in der  Erde';  aisl.  7'lsta  (reist)  und  rista  schw.  V.  ^schneiden,  ritzen,  auf- ritzen', rista  ,Ritz,  Schlitz',  aschwed.  j-lsta  ,(Runen)  ritzen',  mnd.  risten ,einritzen',  aisl.  ristill  m.  , Pflugeisen
----LEAF 94 (p.859)
',  mhd.  rist  m.  n.  ,Pflugschar, Pflugsterz';  lett.  risums,  risiens  ,Riß,  Schlitz',  aksl.  resiti  ,lösen'. WP.  II  343  ff.,  WH.  II  435  f.,  436,  438,  Trautmann  241.
2.  rei-f  roi-  in  Worten  für  , buntgestreift,  fleckig';  rei-hho-,  roi-bho-  ds.
Lit.  rai-nas  ,grau,  buntgestreift';  rm-mas  ,bunt';  air.  nahach  , gespren- kelt', lit,  raX-has  , gesprenkelt,  graubunt'  (raibti  , flimmern'),  lett.  räibs ,bunt,  fleckig',  bes.  von  Tieren,  apr.  roaban  , gestreift',  russ.  klr.  ribyj ,bunt';  *roi-ko-  scheint  die  Grundlage  von  ahd.  reh  n.,  reho  m.,  ags.  rä, räha  m.  ,Reh',  aisl.  rä  f.,  ags.  rcege  (*raigjön-),  ahd.  reia^  reia  (unklar)  und nhd.  Ricke,  ndl.  reJcke  ,Ricke',  (expressiv)  wozu  wohl  ai.  risya-  m.  , Anti- lopenbock'.
WP.  II  346,  Trautmann  235  f.,  Specht  Idg.  Dekl.  115.
3.  rei-,  re(i)-  Schallwurzel  , schreien,    brüllen,    bellen'    usw.,   s.   auch  reu-, reu-,  TU-.
Ai.  räyati  ,bellt' ;  lit.  rieju  rieti  , losschreien,  schelten',  refl.  ,sich  zanken'; lett.  reju,  reju,  riet  ,bellen';  ablaut.  räju,  rät  , schelten',  lit.  rojöju,  rojöti ,unordentlich  krähen'  (vom  Hahn)?,  ksl.  rarb  , Schall'  (öech.  raroh  m. ,Würgfalke'),  russ.  rdjatb  ,klingen,  schallen';  aisl.  rämr  ,heiser'  (*rema-); abgeleitet  von  einem  Nomen  *rama  ist  remja  , brüllen';  möglich  hierher auch  römr  , Stimme,  Laut,  Aussprache';  vgl.  ferner  ags.  7-äria?i  , blöken, brüllen',  ahd.  reren  ds.  usw. ;
aisl.  jarma  ,blöken',  wozu  arm.  ornal  , heule'  gehört,  weist  vielleicht  auf eine  vollere  Wurzel  erd-,  re-  hin.
Erweiterungen:
reb-  , rülpsen' :  .
norw.  dial  räpa  ,den  Mund  laufen  lassen*  (*repja7i),  rapa  ,rülpsen* ;  aisl. repta  (^rapatjan)  ,rülpsen';  dän.  rcebe  ds.,  jüt.  auch  ,quaken'  s.  Falk-Torp 928 ;  vgl.  reub-  unter  1.  reu-.
860  '
rik-  jbrüllen,  schreien* :
lat.  raccäre,  rancäre  »brüllen*  (vom  Tiger);  räna  (*räcsnä)  ^Frosch»' .__ cymr.  rhegen  f.  {*rakina)  ,Wachtel' ;  mhd.  ruohen  ,brüllen,  grunzen'  (nebe^^ rohen  zu  reu-k-),  amhd.  ruohelen,  mhd.  rüehelen  ^wiehern,  brüllen,  röchet  £ (daneben  rühein,  rücheln  zu  *reu-k-)',  lit.  rekiü,  rekti  ,brüllen*,  lett.  rekt  ds.-  '-^ aksl.  rekg  ,sage';  mit  g:  lat.  ragere  ,brüllen'.
ret'  , brüllen,  lärmen* :
mhd.  rileden  ,lärmen*,  bair.  rüeden  ,brüllen,  lärmen,  in  der  Brunst  sein'« ahd.  ruod  , Gebrüll',  ir-ruota  ,rugiebam^,  agsr  re^e,   ,grausam,  schrecklich*.
WP.  II  342 f.,  WH.  II  414,  416,  421  f.,  Trautmann  242  f.
4.  rei-  :  rei-  ^Besitz,  Sache';  nach  Burrow  (Sanscrit  178,  245)  wäre  e  aus
eH  vor  i  entstanden?
Ai.  rai'  m.
----LEAF 95 (p.860)
  f.  _,Besitz,  Reichtum'  in  räh,  räydh  (ursprüngl.  i-Stamm); das  ä  von  räh  nach  dem  Akk.  Sg.  räm,  der  ebenfalls  analogisches  ä  hat (nach  gäm,  oben  S.  482);  rayi-  ,Gabe,  Besitz,  Kleinod'  (av.  Akk.  PI.  raUy leg.  rayls),  rayi-vdnt-j  meist  re-vdnt-  ,reich';  av.  Instr.  Sg.  raya  (leg.  räya) =  ai.  räyä  (zu  rdh)^  av.  raevant  ,reich*;  ai.  av.  rä-  , geben'  (erweitert  ai. räsate  ,gibt'),  ai.  räti-  ,Gabe,  Geber*;  ai.  rata-,  av.  rätö  ,gegeben':
lat.  res,  rei  ,Sache,  Besitz'  (das  enach  dem  Akk.  rem  aus  *reHim?),  umbr. re-per  ,pro  re',  Dat.  Abi.  ri;  dazu  lat.  reus  , Prozesspartei,  der  (die)  Ange- klagte' (*rei'Os) ;  unklar  mcymr.  rei  ^Reichtum'.
WP.  II  343,  WH.  II  430 f.,  432,  Wackernagel-Debrunner  III  214  ff.; 0.  Szemerenyi  nimmt  (brieflich)  mit  Burrow  (Sanscrit  178,  245)  und  Kury- lowicz  ('Etudes  36  f.)  eine  Grundform  "^reHi-  für  das  Nomen  und  *reH- f  ür  das  Verbum  an  (?)
5.  rei-  , stützen*  s.  unter  reid-^  reih  und  rem-,
1.  rei-  :  ri-  ,zählen,  ordnen',  erweitert  rei-dh-,  s.  oben  S.  60.
2.  rei-,  röi-  ,Nuß'  (s.  Trautmann  241  f.),  s.  oben  S.  61.
reibh-  ,ertönen'?
Ai.  r4hhati  ,knarren,  knistern,  murmeln ;  schreien' ;  lett.  ribet  (auch  ribet) ,dröhnen,  poltern,  tosen'.
WP.  II  349 ;  wohl  zu  3.  rei-.
reid-  ,anlehnen,  stützen'?
Gr.  igsidu)  ,lehne  an,  unterstütze,  dränge,  strenge  mich  an'  (hom.  igrjQe- Sarat  für  -qlö-),  egsia^a  ,Stütze',  ävT-rjgig  -r]Qt6og  , Strebepfeiler,   Stütze'; lat.  ridica  ,ein  durch  Spalten  größerer  Pflöcke  gewonnener  Weinpfahl'  ? WP.  II  348,  WH.  II  434;  wohl  zu  5.  rei-.
861
fcidb'  >^i'6^^  ^^  Bewegung  sein^
J^lir.  rlad(a)im  ,fahre^  (^reidh-)]  cymr.  rhioydd-hau  ^beeilen,  erleichtern^; aisl.  f'^^^  J^"^  schwankender  Bewegung  sein,  reiten^;  ags.  rldan  ^reiten^; ifries.  rlda,  mnd.  rlden,  ahd.  ritan,  mhd.  rlteriy  nhd.  reiten]
lett.  raidit  ,eilig  senden,  hetzen^,  raidities  ,zappeln^;
o-erm.  *ridjan-  steckt  in  ags.  ridda,  ahd.  ritto  ,Reiter^,  erweitert  in afries.  ridder,  mnd.  ridder  (daraus  aisl.  riddari)^  mhd.  ritter-^
o-all.  reda  , vierrädriger  Reisewagen^;  ir.  de-riad  , Zweigespann'  (idg. *reidhä)]  aisl.  reid  f.  _,Reiten_,  Reiterschar,  Wagen^,  and.  brande-reda Brandbock';  ags.  räd  f.  ,Reiten,  Zug,  Reise;  Musik^;  engl,  road  ,Weg^; ahd.  reita,  mhd.  reite  , Wagen,  Kriegszug,  kriegerischer  Anfall'  (germ. *raidö,  idg.  *roidha)j
vgl.  hierzu  gall.  redärlus  ,Lenker  einer  reda';  ON  Epo-redia,  PN  Epo- -redo-rlx]  cymr.  ehrwydd  ,schnell'  (*epo-redi-)]
germ.  *(ga)-raidia-  in  got.  ga-raijjs  , angeordnet,  bestimmt',  aisl.  greidr ,leicht  zu  bewerkst
```


## [2026-09-14T01:22:44.312Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ripple\" AHD_watkins1985.txt | head -20; echo \"=== rei- entries\"; grep -n \"^rei-\\|^ *rei-1\\|rei-1\\.\\|rei-2\" AHD_watkins1985.txt | head -30"
}
```


### [2026-09-14T01:22:44.382Z] TOOL RESULT

```
494:vine, grape: GRAPE; c. Old French grapon, grapnel: GRAPNEL; d. Old French grape, a hook: GRAPPLE; e. Ital- ian dialectal grappa, vine stem, brandy: GRAPPA. 2. Old English crump, crumb, crooked, bent, stooping: CRUM- MIE, CRUMPET, (CRUMPLE). 3. Low German krimpen, to wrinkle: CRIMP!. 4. Middle Dutch crampe, hook, and Frankish *kramp, hook: cramMpP?. 5.Old High German krampfo, a cramp, akin to the Germanic source of Old French crampe, cramp: CRAMP!. 6. Old English crypel, a cripple: CRIPPLE. 7. Germanic *kreupan in Old English créopan, to creep: CREEP. 8. Middle Low German krink, a ring: CRINGLE. 9. Germanic *krengan in Old English cringan, to yield: CRINGE. 10. Middle Dutch crinkelen, akin to Middle English crinkelen, to make kinks in: CRINKLE. 11. Old Norse kriki, a bend, nook: CREEK. 12. Old Norse krékr, a hook: cRooOK. 13. Frankish *krok- (> Old French croc), a hook: CROCHET, (CROCKET), (CROQUET), (CROUCH); ENCROACH. 14. Old English crycc, (bent) staff, crutch: CRUTCH. 15. Old French crosse, crook: CROSIER, LACROSSE. 16. Middle Dutch crulle, curly: CRULLER, CURL. 17. Old English cranc-(stzf), a weaving implement: CRANK}. 18. Norwegian krake, a sickly beast, akin to the source of Middle English crok, an old ewe: cRocK3, 19. Old Norse karpa, to boast: CaRP!, 20. Middle Dutch kroes, curled, akin to the source of Old French grosele, gooseberry: GROSSULARITE. II. Words meaning ‘“‘a rounded mass, collection; a round object, vessel, container.” 1. Old English cruma, a frag- ment: CRUMB. 2. Frankish *kruppa, rump, akin to the Germanic source of Old French croup, rump: CROUP?, (CROUPIER), CRUPPER. 3. Old English cropp, cluster, bunch, ear of corn: crop. 4. Italian gruppo, an assem- blage: Group. 5. Old English crocc, pot: CROCK}. 6, Mid- dle Dutch cruyse, pot: CRUSE. 7. Old English cribb, manger: CRIB. 8. Old English cradel, cradle: CRADLE. 9. Frankish *kripja, cradle, akin to the Germanic source of Old French cre(s)che, crib: CRECHE. 10. Old English creet and Old Norse kartr, wagon: CART. 11. Old English croft, small enclosed field: crort. [Pok. 3. ger- 385.] gerbh-. To scratch. 1. Germanic *kerban in Old English ceorfan, to cut: CARVE. 2. Zero-grade Germanic form *kurbiz in Old English cyrf, a cutting (off): KERF. 3. Variant form *grebh- in: a. Germanic *krab(b)- in Old English crabba, a crab: CRAB}; b. Germanic *krabiz- in Old French crevise, crayfish: CRAYFISH; C. perhaps Ger- manic *krab- in Old Norse krafla, to crawl: CRAWL. 4. Zero-grade form *grbh- in Greek graphein, to scratch, draw, write, and gramma (< *grbh-mn), a picture, writ- ten letter, piece of writing, and grammé, a line: GRAF- FITO, GRAM!, -GRAM, GRAMMAR, GRAPH, -GRAPH, -GRAPHER, GRAPHIC, -GRAPHY; AGRAPHA, AGRAPHIA, DIAGRAM, EPIGRAM, (EPIGRAPH), GRAPHITE, ICONOGRA- PHY, PARAGRAPH, PROGRAM, PSEUDEPIGRAPHA, TETRA- GRAMMATON, TOPOGRAPHY. [Pok. gerebh- 392.] [gerere. To carry, carry on, act, do. Latin verb of un- known origin. Oldest form ges-, past participle gestus. GERENT, GERUND, (GEST), GESTATION, (GESTICULATE), GESTURE, JEST; ARMIGER, BELLIGERENT, (CONGERIES), CONGEST, DIGEST, EGEST, INGEST, REGISTER, SUGGEST, VELIGER.] gere-'. To grow old. 1. Suffixed lengthened-grade form *géro-s- in Greek géras, old age: AGERATUM, CALOYER, GERIATRICS. 2. Suffixed form “gera-ont- in Greek geron (stem geront-), old man: GERONTO-. [Pok. ger- 390.] gere-2. To cry hoarsely; also the name of the crane. I, Words meaning “‘to cry hoarsely”; also words denoting the crow. 1, Germanic *kré- in: a. Old English crawe, a crow: CROW}; b. Old English crdwan, to crow: CROW?; c. Old English cracian, to resound: CRACK; d. Middle Dutch krdken, to crack: CRACKNEL; @. Old Norse kraka, a crow: CRAKE. f. Middle Dutch krdnen, to groan, la- ment: CROON. 2. Possibly (but more likely imitative) Germanic *kur(r)- in Old Norse kurra, to growl, akin to Middle English curre, cur: cur. II. Words denoting a
681:lem-', To break in pieces; broken, soft, with derivatives meaning “crippled.” 1. Germanic */am6n- in Old English lama, lame: LAME}. 2. Germanic *lamjan in Old Norse lemja, to flog, cripple by beating, akin to the Scandina- vian source of LAM}. 3, Perhaps Swedish dialectal loma, to move heavily, akin to the Scandinavian source of Middle English lomeren, to lumber: LUMBER?. [Pok. 1. lem- 674.]
=== rei- entries
895:ryfe, abundant: RIFE. 3. Suffixed form *reip-d- in Latin ripa, bank (< “that which is cut out by a river”): RIPARIAN, RIVAGE, RIVER; ARRIVE. IV. Extended form *reib- in Germanic *rip-. 1. Germanic *ripja- in Old English ripe, ripe, ready for reaping: RIPE. 2. Germanic *ripan in Old English ripan, to reap: REAP. 3. Middle Low German repelen, to remove seeds, akin to the source of Middle English ripelen, to remove seeds: RIPPLE? [Pok. 1. rei- 857.] rei-2. Striped in various colors, flecked. Suffixed o-grade form *roi-ko- in Germanic *raihaz in Old English rd, raha, deer: ROE*. [Pok. 2. rei- 859.] rei-3, To flow, run. 1. Suffixed zero-grade form *7i-nu- in: a. Germanic *ri-nw-an, whence *rinnan, to run, in Old English rinnan, to run, and Old Norse rinna, to run: RUN, RUNNEL; b. secondary Germanic derivative *runiz in Old English ryne, a running: EMBER DAY. 2. Suffixed zero-grade form *ri-l- in Germanic *ril- in Dutch ril and Low German rille, running stream: RILL. 3. Suffixed form *rei-wo- in Latin rivus, stream: RIVAL, RIVULET; DERIVE. [Pok. 3. er- 326.] reidh-. To ride. I. Basic form *reidh-. 1. Germanic *ridan in: a. Old English ridan, to ride: RIDE; b. Middle Dutch riden, to ride (> ridder, rider, knight): RITTER. 2. Celtic *vo-réd- in Latin verédus, post horse (*vo-, under; see upo): PALFREY. II. O-grade form *roidh-. 1. Germanic *raid- in: a. Old English rdd, a riding, road: RAID, ROAD; b. possibly Middle High German reidel, rod between upright stakes (< “wooden horse”): RADDLE!. 2. Prob- ably Germanic *raid-ja- in Old English réde, geréde, ready (< “prepared for a journey’): READY. 3. Germanic *raidjan in Vulgar Latin *arrédare, to arrange: ARRAY. [Pok. reidh- 861.] reig-'. To bind. 1. Germanic *rigg- (the -gg- is anoma- lous) in Norwegian rigga, to bind, akin to the Scandina- vian source of Middle English riggen, to rig: RIG. 2. Zero-grade form *rig- in Latin corrigia (probably borrowed from Gaulish), thong, shoelace (cor-, from com-, together; see kom): SCOURGE. [Pok. reig- 861.] reig-2. To reach, stretch out. 1. O-grade form “roig- in Germanic *raikjan in Old English récan, to stretch out, reach: REACH. 2. Possibly suffixed (stative) zero-grade form “rig-é- in Latin rigére, to be stiff (? < “be stretched out”): RIGID, RIGOR. [Pok. (reig-) 862.] rendh-. To tear up. 1. Germanic *randjan in Old English rendan, to tear: REND. 2. Germanic *rind- in Old English rinde), rind (< “thing torn off”): RIND. [Pok. rendh- 865.] rep-. To snatch. Suffixed zero-grade form *rap-yo- in Latin rapere, to seize: RAPACIOUS, RAPE!, RAPID, RAPT, RAVEN?, RAVIN, RAVISH; EREPSIN, SURREPTITIOUS. [Pok. rep- 865.] rép-'. To creep, slink. Latin répere, to creep: REPENT?, REPTILE; SUBREPTION. [Pok. 1. rép- 865.] rép-2, Stake, beam. Suffixed variant form *rap-tro- in Germanic *raf-tra- in: a. Old English refter, rafter: RAFTER; b. Old Norse raptr, beam: RAFT!. [Pok. 2. rép- 866.] ret-. To run, roll. 1. Prefixed form *to-vo-ret-, “a running up to” (to-, to; vo, under, up, up from under; see upo), in Old Irish toir, pursuit: Tory. 2. Suffixed o-grade form *rot-d- in Latin rota, wheel: RODEO, ROLL, ROTA, RO- TARY, ROTATE, ROTUND, (ROTUNDA), ROULETTE, ROUND!, ROWEL; BAROUCHE, CONTROL, PRUNE?, ROTIFORM, ROTO- GRAVURE. [Pok. ret(h)- 866.] rét-. Post. O-grade form *rdt- in Germanic *réd- in Old English réd, rod, cross: ROOD. [Pok. rét+ 866.] reu-'. To bellow. 1. Extended form *reud- in Germanic *rauton in Old Norse rauta, to roar (akin to the Scandi- navian source of ROTE?): ROUT’. 2. Suffixed extended form *reum-os- in Latin riimor, rumor, “common talk”: RUMOR. 3. Extended form *reug- in Latin rigire, to roar: RIOT, RUT’. 4. Variant *rau-ko- in Latin raucus, hoarse: RAUCOUS. [Pok. 1. reu- 867.]
2198:ROE! krek-2 ROE? rei-2 ROGATION reg-1 ROGATORY reg-1 ROLL ret- ROLLMOPS mul- ROOD rét-
```


## [2026-09-14T01:22:45.294Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"raipaz\\|raigwa\\|raiwo\\|rip-a\\|ripa .bank\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-14T01:22:45.354Z] TOOL RESULT

```
893:culdre, to rake, in Provengal rasclar (> French racler), to rake, scrape: RACLETTE. [Pok. 2. réd- 854.] reg-'. To move in a straight line, with derivatives mean- ing “to direct in a straight line, lead, rule.” I. Basic form *reg-. 1. Suffixed form *reg-to- in Germanic *rehtaz in Old English riht, right, just, correct, straight: RIGHT. 2. Latin regere, to lead straight, guide, rule (past partici- ple réctus, hence adjective réctus, right, straight): REALM, RECTITUDE, RECTO, RECTOR, RECTUM, REGENT, REGIME, REGIMENT, REGION; CORRECT, DIRECT, ERECT, RECTANGLE, RECTIFY, RECTILINEAR, RISORGIMENTO, SURGE. 3. Greek oregein (with prothetic vowel from oldest root form *sreg-), to stretch out, reach out for: ANORECTIC, ANOREXIA. II. Lengthened-grade form *rég-, Indo-European word for a tribal king. 1. Celtic suffixed form *rig-yo- in Germanic *rikja- in: a. Old English rice, realm: BISHOPRIC; b. Old Norse riki (> Norwegian rik), realm: RIKSMAL; c. Old English rice, strong, powerful: RICH. 2. Latin réx, king (royal and priestly title): REAL, REGAL, REGULUS, REIGN, ROYAL; INTERREX, REGICIDE, REGIUS PROFESSOR, VICEREINE, VICEROY. 3. Suffixed form *rég-en- in Sanskrit raja, rdjan-, king, rajah (femi- nine rdjni, queen, rani), and rdjati, he rules: RAJ, RAJAH, (RANI), (RYE2); MAHARAJAH, MAHARANTI. III. Suffixed lengthened-grade form *rég-old in Latin régula, straight piece of wood, rod: RAIL!, REGLET, REGULAR, REGULATE, RULE, IV. O-grade form *rog-. 1. Germanic *rak6 in Old English raca, racu, rake (implement with straight pieces of wood): RAKE!, 2,Germanic *rak- in Middle Dutch rakke, framework: RACK}, 3. Possibly Germanic *rankaz (with nasal infix) in Old English ranc, straight, strong, hence haughty, overbearing: RANK?. 4, Germanic *rak- inaz, ready, straightforward, in Old English gerecenian, to arrange in order, recount (ge-, collective prefix; see kom): RECKON. 5. Suffixed form *rog-d- in Latin rogdare, to ask (< “stretch out the hand”): ROGATION, ROGATORY; ABROGATE, ARROGATE, CORVEE, DEROGATE, INTERRO- GATE, PREROGATIVE, PROROGUE, SUBROGATE, SUPERER- ocaTE. 6. Suffixed form *rog-o- in a possible Latin noun *rogus, “extension, direction,” perhaps in a Latin phrase *é rogd, “from the direction of” (€ < ex, out of; see eghs), contracted into ergd, therefore, in consequence of: ARGAL, ERGO. V. Lengthened o-grade form *rég-. 1. Ger- manic *rdkjan in Old English rec(c)an, to pay attention to, take care (formally influenced by Old English reccan, to extend, stretch out, from Germanic *rakjan): RECK. 2. Germanic *rdékja- in Old English receléas, careless (-léas, lacking; see leu-1):; RECKLESS. [Pok. 1. reg- 854.] reg-2. Moist. 1. Suffixed variant form *rek-no- in Ger- manic *regnaz, rain, in Old English reg(e)n, rén, rain: RAIN; RAINBOW. 2. Possibly Latin rigdre, to wet, water: IRRIGATE. [Pok. 2. reg- 857.] reg-3. To dye. Lengthened-grade form *rég-. 1. Suffixed form *rég-és- in Greek rhégos, blanket, rug: REGOLITH. 2. Sanskrit rdgah, color, red: RAGA. 3. Perhaps Sanskrit raékshd, earlier form of lékshd, red dye: Lac}. [Pok. 1. reg- 854.] regv-es-. Darkness. Oldest root form *areg’-es-. Greek Erebos (with prothetic vowel), Erebus, a place of dark- ness under the earth: EREBUS. [Pok. regt-os- 857.] rei-1, To scratch, tear, cut. I. Extended form ‘reik-. 1. Germanic *rigon- in Italian riga, line (< “something cut out’’): RIGATONI. 2. Suffixed form *rei-md or *reig-sma in Latin rima, crack, cleft, fissure: RIMOSE. 3. Suffixed o-grade form *roik-wo- in Germanic *rai(h)-wa- in Old English raw, réw, a line, row: ROW!. II. Possible extended form *reipp-. Germanic *raipaz, rope, in: a. Old English rap, rope: ROPE; b. compound *stig-raipaz, “‘mount-rope,” in Old English stigrap, stirrup (see steigh-). III. Extended form *reip-. 1. Ger- manic *rifan, in Old Norse rifa, to tear: RIVE. 2. Zero-grade form *rip- in: a. Germanic *77fti- in Danish rift, breach, akin to the Scandinavian source of Middle English rift, rift: R1FT!; b. Germanic *rif- in Old English
1011:steigh-. To stride, step, rise. I. Basic form *steigh-. 1. Germanic *stigan in Old English stigan, to go up, rise: sty. 2. Germanic compound *stig-raipaz, “mount-rope” (*raipaz, rope; see rei-1), in Old English stigrdp, stirrup: STIRRUP. II. Zero-grade form *stigh-. 1. Germanic *sti- gila- in Old English stigel, series of steps: STILE!. 2. Suf- fixed form *stigh-to- in Germanic *stihtan, “to place on a step or base,” in Old English stiht/i)an, to settle, arrange:
```


## [2026-09-14T01:23:21.884Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD rēš/rēxt/rēs\"; grep -n \"rēš\\|rēxt\\|rēs-\\|rēsēn\\|abrēšum\\|abrēšam\" PHD.txt PHD_mackenzie.txt | head -30"
}
```


### [2026-09-14T01:23:21.977Z] TOOL RESULT

```
=== PHD rēš/rēxt/rēs
PHD.txt:170:abilag 5/4! | N ~a] blister. a-bim [bym] fearless. āb-kāmag [5A mk! | N ~a] a thick, sour soup. abnüs Pžēnws | (N ābnūs)] ebony. a-biy Pbwd] senseless. ~ih: senselessness. à abr РЫ, Séi | N ~] cloud. M bel abrang [ing | N aurang] glory, splendour. abrastan, abraz- [AP stn',SPc- | М ?br?st, N (afráttan), afrdz-] lift, raise. abraz [Pe | N afrāz] acclivity. abrēšom Pflyš(u)m | M? bryfwm, N ~} silk. ~én [-yn!] silken. abróxtan, abróz- ['piwhtn', ?phoc- | M brwxt, ?)brwc-, N afróxtan, afróz-] light, kindle, illuminate, polish. ~i$n(ih): illumination. āb-tazan Pftcn!] watercourse. a-bun [*dwx!] baseless, bottomless. a-burd-framān ['bwltplm^n'] disobedient. ~th: disobedience. aburnāy f(w)lnd, v. purnāy | N burnā] under age, child. ^h : childhood. aburnáyag [?A(w)/n’(d)yk'] child. abus [pws] (woman) having just given birth. “АҺ: childbirth. арив, -tan Pws, -tn! | M ’bwws, v. ábestan] pregnant. „il: pregnancy. abydxtan, abyóz- Phywhtn', ?bywc-] join, mix. āb-zan zn! | N ~] bath. labzar [el pel] M *6c*7, N afzār] instrument, means; spice. *abzar [6271 | M bail skill, power; powerful. „ūmand [-wmnd] skilled, able. abzāy-, —išn, у. abztidan, abzón [?pzwn! | M, J ”*bzwn, N afzün] increase, growth. ~ig [-yk!] increasing, expansive, bountiful. ~igih: bountifulness. abzüdan, abzáy- ['pzwtn!,^?pzd- | M ?bz'y-, N afzüdan, afzāy-] in- crease, grow. ~i$n: increase, growth. a-čār [cI] inevitable, Jee ~ag [-k'] compelled.
PHD.txt:193:---rēšn(ih) [-Iwsn!, -lwsnyh] Infinite Light. anāhīd р/у | N ndhid] immaculate; a goddess; astr. Venus. an-àáhóg P7 kwok!] undefiled. an-ālūd [?77/wt'] undefiled. a-nāmčištīg m mcftyk!] unspecified. an-ámurzid [?rmwlcyt! | M ?n’mwrz‘yd] merciless. an-āmurzišn [*7”mwicšn!] mercilessness. anār [71 | N ~] pomegranate. anārģēl [777/gy/ | N nārgēl) coconut. an-arzünig [?77/c”nyk!] undeserving, unworthy. an-ast [^n 4 Y T'] non-existent.
PHD.txt:316:drón yaštan: consecrate the sacrificial bread. drēš [410] mark, branding; punishment. ~ag [-k!] *desolation. drēšīdan, dro$- [d/w$-ytn'] brand. drēūšom [dlwšwm] mark. droz-, v. druxtan. drózan [dlwen! | M, J drwzn] lying, liar. ^h: falsehood. drubušt [di(w)pwst'] fortress. ~ih: defence, fortification. drüdan, *drün- (HCDLWN-tn! < A У hsd | M ача, (dwr-), N durüdan, diraw-] reap, mow. drust [drw(y)st' | (M dryst), N durust] right; well, healthy. —Ih: righteous; health. drustabed [drwystpt'] chief physician. društ [dlwšt' | N durust] harsh, rough, severe. ~ih: harshness, severity. ~-Awaz, ~-éwaz [-p'c, ~yw’c] harsh-spoken. druwand [dlwnd | M drwnd] evil, sinful, unrighteous. ~īh: sin, unrighteousness. druxtan, dróz- [dlwhtn', dlwc- | M drwxt, drwz-] lie, deceive. druz [dlwe | (P drwj)] demon. айа [dwt! | M dwd, N ~] smoke. düdag [dwtk! | N —a] family. dudigar [dtykl | M dwdygr, N digar] second. duj-, = duš-. ~-daft [dwsdpt'] ill-breathing, short of breath. ~-dānāg [dwšd”7?k!] ignorant. ~-dén [dwšdyn' | M dwjdyn-] of evil religion. «=dēys*rīh [dwsdwyslyh] the evil eye. ~-gand (dtwsgnd | P dwjgnd] stinking. ~-gandih: stench. dum(b) [dwm(b') | N ~] tail. ~dmand [-'wmnd) tailed. ааг [LH YK'! < А rhyq; dul | M dur, N ~] far, distant, remote. durgar [dwlgl | N ~] carpenter. dusraw [dwslwb!] notorious, dishonoured. ^Ah : notoriety, dishonour. duš- [dws- | = M] ill-, evil-. ~īh: evil, wickedness. ~-абаһ [dw??^ Es] foolish, stupid, ignorant. ~-абаһіһ : foolishness, stupidity. ~-arz [2 ic] worthless. 7--Ca&m [-cém] envious. —-Ca$mih: envy. ~-tihr [-cyhl | M dwfcyhr] ugly, hideous.
PHD.txt:557:ranjwar [Incwl | (M rnzwr), N ranjūr] troubled, distressed. rapihwin [/pys-, Ipyt-pyn!, -wyn' = Av. rapiüfina-] the afternoon gah; south. ~tar [-tl] southern. rasan [/sn' | N ~] rope. rasénidan, rasén- [/syn-yin'] bring. rasidan, ras- [YHMTWN-tn' < А yhmtwn, V mt^; ls-ytn! | M rs-ydn, N ~] arrive, mature. raspig [Pspyk!] second officiating priest. rast [Pst! | M rst, N ~] true, straight, direct. ~ih: truth, rastaģ [lstk! | N rasta] series, row, progression; element, газап, rah- [Istn', Ї(?)А- | N ~] escape. rastarih [/st?/y%] escape. rasüg [/swk! | (N rāsū)] weasel. Rašn [/@! | M ri, N ~] god of Justice; cal. 18th day. ra&tan, *raz- [/ftn'] colour, dye. raw-, v. raftan. rawag [/wP^k! | N rawá] current. ~ih: currency. rawügenidan, rawagén- [/zob)hyn-ytn!] set in motion, propagate. rawénidan, rawén- [SGYTWNyn-ytn', v. raftan] cause to go, extend. rawišn [lwbin', SGYTWNsn', v. raftan | N rawif] going, motion. ^h : behaviour; as a suffix, forms abstract nouns. ray [Pd | M ry, N ra] postposition, for, for the sake of. rāyēnāģ [Pdym bi | M r’yn’g] arranger. rayénidan, rāyēn- [Pdyn-ytn! | M r'yn-ydn] lead, direct, arrange, organize. ~išn: action, function; arrangement. rāyēnīdārīh [/”*dynyt?lyh | M r!ynyd?ryh] direction, organization, rāyišn [”dsn'] order, arrangement. rāyomand [Pd^wmnd] rich, majestic. raz [/c, lz | N ~] vine; vineyard. raz [Pc | M Pz, N ~] secret, mystery. ~ig [-yk'] secret. rāz-kirrēģ [Pc kylwk' | M г qrwg] architect, builder. razm [/cm | M rzm, N —] battle. —--$àh [-g's | P -g’h, (M rzm?h), N ~] battlefield. razor [lcw] | M rzwr] forest. rédak [lytk' | N ~] lad, page. тёр [/yā! | N ~] sand. rëm [lym | M rym, N —] dirt, filth, purulence. réman [lymn' | M rymn, N ~] dirty, filthy, purulent. ^b : filth. 1r€§ []yf | N ~] wound, sore. *rēš [/yf | N —] beard.
PHD.txt:559:rēšaģ [/yšk! | N rēša] root, fibre. rēšīdan, rēš- [lysyin' | N ~] wound, hurt. rëškën [/yškn'] hurtful, harmful. ~th: harmfulness. réxtan, réz- [lyhtn', lyc- | P ryxt, M ryz-, N ~] flow, pour. --išn: flow. ridan, riy- [/ytn', Id- | N ~] defecate, void. rist [lyst' | M ryst] dead. Iristag [lystk'] corpse. 'ristag [/ystk!] way, manner; sect. rist-āxēz [/yst?hyc | M ryst?hyz, N ~] resurrection of the dead, rištaģ [/(y)stk! | N ~a] rope, string, thread. riy-, v. ridan. riyahrih [/d?hlyh] scorn, mockery. rdb [/wp] robbery. rób- [/wp- | N ruftan, ~} rub, sweep. rūbāh [TALE < A tP; lwph | N ~] fox. Irēd [Iowt! | M rwd, N ~] river. *rdd [lwt' | N ~] stringed instrument. réd-bar [lwtb’] | N ~] river bank. rddig [/zvtyk! | (N róda)] intestine, gut; ~4n, (p/.) entrails, guts. тбүп [M(H)SY A < A ті; lwkn! | Р тшеп, (M rwyyn), N rauyan] oil, butter. ~-xwardig [-hwltyk'] sweetmeats. ron [lwn' | M rwn] direction. б... ~: towards. róspig [lwspyk! | N ~i] whore. ~th: whoredom. róstág [lw(t)st?k! | (P rwdyst?g), N rūstā] river-bed; district, province. rošn [lwfn! | M rwšn, N rūšan] light; bright, light. ~ih: light. röšnjag [lwsnk'] clear, obvious. ~gar [-Al | (P gr, M -ygr), N -gar] illuminator. irēy [ltd | M rwy, N ~] face. *rdy [lwd | M rwy, N ~] copper, brass. гбу-, -išn, v. rustan. гӧуап [/wdyn! | N ~] madder. róyen [/wdyn! | M r'wyn, N róyin] (made of) copper, brazen. roz [YWM < А ушт; Гос | M rwc[z, N ~) day. rózag [lwck! | M rweg, N roza] fast, fasting. rozāģ [wc k'] lightning. rózan [/wcn! | N ~] window. roz(b)ānaģ [lwe(p)’nk'] window. rózénidan, rózén- [Iwcyn-ytn! | M rweyn-] lighten, brighten. rozģār [/wck”l | N ~] daytime. r6zig [/wcyk! | N rózi] daily bread, sustenance.
PHD.txt:568:spas dāštan, ~ hangárdan: thank, give thanks. spās-dār [sp?sd?] | N sip~] grateful, thankful. ~ih: gratitude. spās|-ešnās [sp’ssn’s] grateful. —ómand [-’wmnd] grateful. spas [sp = Av. 0Bàsa-] space, atmosphere. spaxr [sp?hl | M ‘spxr, N *siparx] merrymaking, revelry. spazg [spzg | (M ‘spgj), N sipazg-] slanderous. «il: slander. spëd [spyt! | M ‘spyd, N sapéd] white. ~ag [-k! | N -a] white (of egg, etc.). —bàg [-p’k!' | N -bā] curd soup. --dàr [-?1 | N -dár] white poplar, aspen. spenag [sp(y)m?k! = Av. spanta-, cf. $annág] holy. ~ ménóg : the Good Spirit. Spig [spyk' | M ‘spyg, (N sapriy)] т. brilliance; 2. sprout, shoot. spihr [spy(y)hl | (M ‘spyr), N sipihr] sphere, sky, firmament, fate. ~ig [-yk'] heavenly. spinjanagih [spne’nkyh] hospitality. spiš [spyš | (N šipt$)) louse. Spitāmān [spyt?m?^n] of the Spitama family. spiz- [spyc- | M “рухіп, *spyz-] 1. shine; 2. sprout. —išn: 1. brilliance; 2. sprouting. spöxtan, spēz- [spwhtn', spwc- | M *spwxt, N sip~] thrust; overstep, disobey; delay, reject. ~išn: delay, rejection; disobedience. SpOz [spwe | N sipóz] disobedience; delay. ~gar LEIT N ~] disobedient; dilatory. sprahm(ag) [splhm(k') | M *sprhm(g), N siparham] flower, fragrant herb. spul [spwl] spleen. spurdan, spar- [spwiltn', spl- | N sip~] tread, trample. spurrig [spwlyk!' | (M ‘spwr), N sipari] entire, complete, perfect. ~ith: completeness, perfection. spurz [*spiz | P “spwrz, N sipurz] spleen. srat (sit! | cf. Ar. sirát] street. sraw [s/wb'] word, spell. srawénidan, srawén- [slwbyn-ytn'] report, broadcast. sraxtag [s/htk! = Av. sraxti-] side, part. sray [sd | N saray] house, hall. Igrāy-, -išn, v. srüdan. srāyīdan, ?sráy- [sPd-ytn! = Av. @rdya-] protect. ~išn: protection. srešk [sl(y)£h | (P srsk), N sirifk] drop, tear. srištan, *srēš- [s/szn! | P sryi-, N sir-~] mix, knead. sri$wadag [s/ystotk! = Av. Oriswa-] a third. sréd [s/zvt! | M srwd, N suród] song.
PHD.txt:569:Srēš 77 stūdan
PHD.txt:570:Srēš [slw$ | M sros, N surūš] the god Obedience; cal. 17th day. ~ig [-yk'] obedient. srū [slwb' | N suri(n)] horn, nail, prong. srub [s/(w)p | N usrub] lead. ~ën [-yn'] leaden. srüdan, sray- [s/wtn', sPd- | M sry-, № sur~] sing, recite, play (an in- strument). ~i$n(ih): singing, recitation. srüwar [siwbw!] horned. srūwēn [slwbyn'] horny. stabr [stpl | M stbr, N sitabr] big, coarse, strong. 7-ih : coarseness; strength, force. stabrag [stpik! | Ar. istabrag] shot silk. stadan, stán- [YNSBWN-tn' < A ynsbwn, V nsb | M ‘std, *stn-, N sit~] take. staft [stpt! | M ‘stpt] hard, firm; harsh, tyrannous; very. stahm [sthm | N sitam] power, oppression. ~ag [-k'] strong, oppressive. ~(ag)ih: oppression. stambag [sthmbk! (-h- < stahm) | M ‘stmbg, N sitamba] oppressive; obstinate. “АҺ: oppression; obstinacy. stān-, v. stadan. star [sil] = stāraģ. stárag [st?/k! | M ‘st?rg, N sitara] star. stard [st!/t!] stunned, stupefied, confounded. ~ih: stupidity, stupefaction. : star-Ošmār, -6šmur [stProfm?l, 2wfmwl] astrologer. starwan [stlwn' | N sit~] barren, childless. stáyIdan (s? dytn! | M гуд, N sit~] = stüdan. Stéy [styk! | N. sitéy] erect. sténdag [styndk!] standing, erect. stér [styl | N sitēr] stater. Stézag [styck! | M ‘styz-, N sitéza] quarrel, strife. sti [sty(y) = Av. sti-] being, existence. Std [stwh! | (P *stwb, N sutdh)] distressed, defeated. ~wih : distress. stör [stwl | P ‘stwr, N sutór] horse, mount; large cattle. «bān [-p’n' | N -bàn] (head) groom. --ģāh [-g’s] stable. *stēš [stw$] the fourth morning after death. stówénidan, stówén- [stwhyn-yin'] defeat, overcome, Stówih, v. sto. stüdan, stāy- [stwtn', st?d- | M ‘stwd, ‘st?y-~~, N sit—] praise. ~išn: praise. ~išnīg : praiseworthy.
PHD.txt:704:abstain pahrēxtan,
PHD.txt:906:avoid pahrēxtan, wiziristan. avoidable wizirisnig. avoidance ānābišn.
PHD.txt:949:beard rēš.
PHD.txt:1067:brand drēšīdan.
PHD.txt:1068:branding drēš.
PHD.txt:1092:bright rēšn, šēd, P niság.
PHD.txt:1250:clear rēšnag.
PHD.txt:1922:fibre rēšag.
PHD.txt:1968:Лее wirēxtan.
PHD.txt:2210:harmfulness rēškēnīh.
PHD.txt:2343:hurt (v.) bištan, (bēšīdan), rēšīdan.
PHD.txt:2375:illuminator rēšngar.
PHD.txt:2620:light (a.) rēšn; (weight) sabuk, xwār.
PHD.txt:2732:mark daxšag, drēš(om), nišān.
PHD.txt:3169:polish abrēxtan.
PHD.txt:3287:punishment drēš, pādifrāh, puhl.
PHD.txt:3473:root rēšag.
PHD.txt:3654:Silk abrēšom; shot — stabrag; v. damask.
PHD.txt:3947:tend pahrēxtan.
PHD.txt:4363:wound (v.) rēšīdan, xastan.
PHD.txt:4405:Srēš
PHD.txt:4689:pardaxtan, parrēxtan
```


## [2026-09-14T01:23:22.804Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== CHEUNG raiš\"; grep -n \"raiš\\|\\*raiš\\|to spin\" CHEUNG.txt | head -30"
}
```


### [2026-09-14T01:23:22.861Z] TOOL RESULT

```
=== CHEUNG raiš
7217:*gaip/b ? ‘to spin (thread) 
7226:yib-/yibt, Yi. yi(w)-, M. yrw-/yivd- ‘to spin’, ? Pash. yaibá ‘cotton (геад) (-ai- < 
12901:Sariq. rizd ‘pain’ (rather *raiš ?) || (+ *pati-) Yghn. d’ris-/drista ‘to tear, to be torn 
16280:*SANSKRIT: kart ‘to spin, twist threads’ = EWAia I: 316 
16290:‘work’ + tanidan ‘to spin’ or a connection to Skt. kart. NP kartana(k) have similar 
24589:*MIDDLE PERSIAN: BMP tn- /tan-/, (pret. stem) tt- /tad-/ ‘to spin (thread)’, BMP tnnd 
24593:tén-/ténà ‘to spread [intr.]’, tēn-/tēnā ‘to spin’, Khuns. ten-/tenä ‘to string’ 
24597:tighten, wind’, Yzgh. tant/tan- ‘to spin’ (< Pers. ?), Wa. tem-/tond- ‘to form (from 
28207:its rise is that it denotes the physical state (Kellens, l.c.), cf. *raiš. Since both 
28263:*CHORESMIAN: rYsY- ‘to spin’, гуз ‘thread’ © Samadi: 176 
28268:ris(t)a/ris-, Siv. res-/res, ris, rese, Varz. resse/res- ‘to spin’, Bal. rist, rést/rés- ‘to 
28269:twist (threads)’, (EHB) rést’, rés6/rés- ‘to spin’, NP ristah ‘fiber, filament, etc., Yzd. 
28274:*NEIR: Pash. réSal ‘to spin’, Yghn. riwes-/riwesta ‘to twine, spin’ || (+ *abi-) Oss. I. 
28275:elvisyn/elvest, D. elvesun/elvist ‘to spin’, Pash. wresol ‘to spin’, (LW) Pash. 
28278:*MISC: Orm. ras-/rasök ‘to spin’ = ris-/risók 
57872:to spin
```


## [2026-09-14T01:23:26.341Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '28180,28300p' CHEUNG.txt"
}
```


### [2026-09-14T01:23:26.397Z] TOOL RESULT

```
*uraid ? ‘to blame, condemn’ 
*AVESTAN: YAv. uruuaöö- ‘to blame, condemn ?’, “uruuaédam (Asg f.) ‘blame, 


condemnation’ (F 450) = Liste: 60 
Pass.: pres. IND. 3sg. YAv. “uruuidiieiti (P 56, F 451) 


© The Avestan forms have no known cognates. Taking his cue from Bartholomae, 
AiW: 1533, Kellens 1984: 127, fn. 12 Liste: 60) accepts the existence of an Av. root 
uruuid with the meaning ‘to perish’ ("aller à sa perte"). The evidence would be 
confined to two forms: YAv. “uruuidiieiti (P56) and YAv. "ni.uruuióiiat (У 16.7). 
Several objections can be raised though. In the first place, YAv. “uruuidiieiti (P56) 
translates Pahl. /éraxtéd/ ‘is condemned’, cf. Jamaspa — Humbach: 78 f. Similar 
forms are also attested іп the Frahang-i-Oim (already quoted by Bartholomae, s.v. 
urvaéd- ‘stürzen’), viz. Е 450 f. “uruuaédam and *uruuiöiieiti. These forms are 
glossed by Pahl. "dng /ering/ ‘condemnation’ and ’dlht /érixt/ ‘condemned’ respec- 
tively, cf. Klingenschmitt 1968: 141. All three glosses are consistent and should 
therefore not be ignored in favour of an ad hoc translation ‘to perish’. Also the Av. 
form that Kellens interprets as "serait conduite à sa perte", "ni.uruuióiiat (V 16.7), is 
probably unfounded. The translation is rather too strong-worded. Bartholomae’s 
analysis, from ^road- ‘to grow’ (1492 f.), which Kellens declined on account of its 
problematic pres. formation in -iia-, is more compelling and appears to be supported 
by an Av. past participle niiuruzdo quoted in the Herbedestan, cf. Kotwal 1 Kreyen- 
broek I: 80 Ё; Hintze 2000: 218, 333. Deriving an tia-formation from the intransive 
2road- is not necessarily an obstacle, as such iia-derivatives became productive at а 
later stage, which Kellens, Le: 125 himself points out. Alternatively, the reason for 
its rise is that it denotes the physical state (Kellens, l.c.), cf. *raiš. Since both 
"ni.uruuióiiát and niiuruzdö refer to food that ought to be given or acquired, the 
sense ‘to suffer from dystrophy, wear out, von Kräften kommen (vel sim.)’ is all the 
more likely (Almut Hintze, personal communication). LIV: —| Pok.: — 


*uraiH ‘to crush, push down’ 
*AVESTAN: YAv. uruuaii- ‘to crush, push down’, YAv. pairi.uruuaesta- (superl.) 


‘who pushes down the best” = Liste: 60 
Partic.: pres. na- YAv. uruuinant- (Yt 13.33) 


*SANSKRIT: vlay (vray’) ‘to crush, collapse’ (RV+) = EWAia II: 598 


*urais 437 


© The evidence for an Ir. root *uraiH is limited to Av. An IE provenance cannot be 
ascertained. 
*PIE — => LIV: 699 | Pok.: — 


*IE COGNATES: — 
*REFERENCES: Hoffmann 1968: 39 ff.; Werba 1997: 319 


*urais ‘to turn, spin’ 

*AVESTAN: YAv. uruuaés- ‘to twist, turn’ || (+ *abi-) ‘to turn to’ || (+ *aua-) ‘to turn 
down’ || (+ *fra-) ‘to turn to’ || (+ *ni-) ‘to turn to’ || (+ *ui-) ‘to separate’ = Liste: 
60f. 

Pres. ja-: IND. 3sg. Y Av. fraorisiieiti (Yt 10.9), ? Y Av. fraorisaiti (H 1.17), Y Av. fraoirisaite (V 9.40), 
3pl. uruuisanti (Yt 12.25), Y Av. fraoirisinti (Yt 13.46), INJ. 3du. Y Av. uruuisiiatom (Yt 19.82), SUBJ. 
lsg. YAv. ni.uruuisiiäni (Yt 17.57 Ё), 3sg. YAv. avoirisiiat (Yt 5.62), OPT. 35р. ҮАУ. fraoirisiiöit (V 
14.16), IMPV. 2sg. Y Av. ni.uruuise (Yt 17.60); Partic.: pres. med. Y Av. fraoirsimna- (Vr 12.5); Caus.: 
pres. IND. 3sg. YAv. auuaouruuaesaite (V 4.22, V 4.25), 3pl. YAv. pairi.uruuaesaiieinti (Yt 14.56), INJ. 
med. 3sg. YAv. uruuaesaiiata (Yt 13.89), SUBJ. 1sg. YAv. fraouruuaesaiieni (Yt 9.31), 35р. ҮАУ. 
auuaouruuaésaite (У 4.22, V 425) YAv. vi uruuaesaiiat (P 20) IMPV. med. 2sg. ҮАУ. 
aipi.uruuaesaiiag'ha (Yt 17.15) 

*MIDDLE PERSIAN: BMP I(y)stk /ristag/ ‘rope, string, thread’, ? MMP *rwys, BMP 
"Iwys /arwös/ ‘rope’ || (+ *abi-) MMP ’bryswm ‘silk? = DMMPP: 53b, 14b 
*PARTHIAN: (+ *4-) ’rws-, ’’rws- ‘to turn to, towards [intr.], face’. © "Despite Ghilain 
1939: 49 and 81, ’rws- and ’’rws- belong together", DMMPP: l.c. This implies that 
’rws- does not derive from *raud. = Ghilain: 49, 81 | DMMPP: 53 

Pres.: IND. 35р. "rwsyd, 3pl. ’rwsynd, SUBJ. 1р1]. ’rws’m, IMPV. 25р. ’rws; Partic.: perf. pass. "rwst, П 
"rws'd, ’rws’d; Inf.: II ’rws’d 

*SOGDIAN: ? CSogd. гуу ‘spun’ || (+ *a- ?) ? BSogd. ’rw’stk, ’rw’stkw, ’rw’st’k 
‘bound, fixed’, CSogd. ‘гух ‘bandage’ (GMS: $116, 157) 

*CHORESMIAN: rYsY- ‘to spin’, гуз ‘thread’ © Samadi: 176 

*NWIR: NP réstan, ristan/ris-, résidan/rés-, risidan/ris-, Kurd. res-/restin, Abz. 
résta/rés-, Abyan. resta/res-, Awrom. restáy/res-, (LW ?) Gz. rés-/résa, Gur. (Kand) 
-ris-, -räs-, Khuns. ris-/rist, risa, Meim. bem-reft/a-ri:s-, Nn. ressaye/ress-, Qohr. 
ris(t)a/ris-, Siv. res-/res, ris, rese, Varz. resse/res- ‘to spin’, Bal. rist, rést/rés- ‘to 
twist (threads)’, (EHB) rést’, rés6/rés- ‘to spin’, NP ristah ‘fiber, filament, etc., Yzd. 
(Zor.) résta ‘handmade noodles, macaroni; dough rolled thin then rolled up and cut 
thin into strings’, NP arvis, arvis ‘a hair rope’ (LW) || (+ *abi-) Bal. (b)resag ‘to 
spin’, NP abrésum ‘silk’ || (+ *ui-) Kurd. (Sor.) guris ‘rope, string’ 

*NEIR: Pash. réSal ‘to spin’, Yghn. riwes-/riwesta ‘to twine, spin’ || (+ *abi-) Oss. I. 
elvisyn/elvest, D. elvesun/elvist ‘to spin’, Pash. wresol ‘to spin’, (LW) Pash. 
wresam, Sh. virexum, Sariq. varaxim, Yi. forgomé ‘silk’ 

*MISC: Orm. ras-/rasök ‘to spin’ = ris-/risók 


438 *uraj 


*SANSKRIT: vrési- name of waters (VS) = EWAia II: 598 
«PIE *ureik- ‘to turn around, wind’ — LIV: 699 | Pok.: 1158 f. 
*IE COGNATES: OE wrigian ‘to tend, incline’, Engl. wry (etc.), Lith. risti ‘to bind, tie 


up’ 

*REFERENCES: КРЕТ: 141a; EVP: 64, 90; IFL I: 405b f.; КРЕП: 202; IFL II: 209a; Lambton 1938: 42a; 
Abaev, Slovar’ I: 132; Andreev — PeSéereva: 314a Ё; MacKenzie 1966: 106; EVS: 86a; WIM I: 72; WIM 
H/1: 81; WIM III: 115; Werba 1997: 238 f.; Cabolov 1997: 72; Cabolov 2001: 406; Cheung 2002: 159; 
Lecoq 2002: 121, 123, 126 (passim); Vahman — Asatrian 2002: 79; Kiefer 2003: 205; Shahbakhsh: rés-; 
Korn 2005: 134 f., 151, 313, 379 


*uraj ‘to go forth’ 

*AVESTAN: uruuaj- ‘to go forth’ — Liste: 60
```


## [2026-09-14T01:23:42.093Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FFD around p56\"; grep -n \"pdf page\" incoming/FFD/FFD_pages.txt | sed -n '50,70p'"
}
```


### [2026-09-14T01:23:42.174Z] TOOL RESULT

```
=== FFD around p56
1249:[pdf page 50]
1274:[pdf page 51]
1298:[pdf page 52]
1320:[pdf page 53]
1344:[pdf page 54]
1375:[pdf page 55]
1398:[pdf page 56]
1422:[pdf page 57]
1446:[pdf page 58]
1470:[pdf page 59]
1493:[pdf page 60]
1516:[pdf page 61]
1540:[pdf page 62]
1563:[pdf page 63]
1585:[pdf page 64]
1621:[pdf page 65]
1645:[pdf page 66]
1683:[pdf page 67]
1708:[pdf page 68]
1727:[pdf page 69]
1759:[pdf page 70]
```


## [2026-09-14T01:23:43.163Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN 17\"; grep -n \"^ *17\\. \\|^17\\. \" HRN.txt | head; echo \"=== HRN 137\"; grep -n \"^ *137\\. \\|^137\\. \" HRN.txt | head"
}
```


### [2026-09-14T01:23:43.246Z] TOOL RESULT

```
=== HRN 17
633:17. ärey 'Hass, Feindschaft*, rey,
3437:17. täj 'Krone*, täjver,
10095:17. antarmäh 'Neumond'.
=== HRN 137
1601:137. 7? 'dieser in Ider *hier, Jdrä (unbelegt), tderi (Näs.
```


## [2026-09-14T01:23:55.137Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"abrēšum\\|abresum\\|abrisum\\|abrešam\\|abrišam\\|Seide\" HRN.txt | head -20; echo \"=== HUB\"; grep -n -i \"abrēšum\\|abresum\\|abrisum\\|Seide\\|rēštan\\|ristan\" HUB.txt | head -20"
}
```


### [2026-09-14T01:23:55.289Z] TOOL RESULT

```
1021:65. ebre^stitn, ebresem *Seide*, beresem,
1033:skr. ksäuma- 'gewobene Seide* {^uparaMäuma-),
=== HUB
305:65. Np. ahreSum *Seide' ^ arm. LW. aprisum, apresum
308:flir *Seide' sind wohl sammtlich aus dem Neupersischen
854:201. Das in der Anmerkung vermuthete biristan *braten' ist
855:baristan 'zum Spinnen', wie Salemann zuerst bemerkt
856:hat. Die iranischen Verwandten') von biristan gehen
861:Ind. 79) oder triig (np. biristan) zuriick gegeniiber
1585:*drehen, wenden, spinnen ) abreSum i tavlda *seta filata'
2629:vgl. skr. gri *mengen, mischen', np. si/ristan 'mischen,
4173:abresum *Seide', aatar 'Stern', arj, arz *Werth*, arzls 'Zinn,
4379:und np. abrisum *Seido* = arm. apresiim = phi. *apresum^ alter *»/?«-
4659:Tab. 96); np. §ar *Stadt' = sahr, saristan = Sahristan.
4876:phi. apuxS(ly(i)Snlk; abr^am *Seide' = abresum, arm. apriSum;
6061:tar-; biristan *braten', iran. brij, skr. bhrjj; Jinn/ *Kupfer, =
6071:'betriigen H. 829; Jirih \iel, mehr H. 826; siristan mischen,
6124:+ rwJ. Ebenso bei abresum = baresum *Seide', arm. apri-
6173:^tistr = zd. ustra- ; vielleicht auch in abr^um *Seide* = phi.
6239:abresum 'Seide', arm. aprisum ; angubm 'Honig , phi. angpeti^
6382:H. 198; barsam (Parsenwort) H. 200; biristan *braten' H
6614:vuxt 'seiden* (AT.), eigentlich golddurchwebt* ? von zarn =
7292:sahristan 'Stadt', paz. sahrastdn, phi. s{a)trustCin Gl. and Ind.
```


## [2026-09-14T01:24:01.735Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==39 {print \"--- HRN leaf 38 (p.17)\"; print substr($0,1,1800)}' HRN.txt; awk 'BEGIN{RS=\"\\f\"} NR==159 {print \"--- HRN leaf 158 (p.137)\"; print substr($0,1,1800)}' HRN.txt"
}
```


### [2026-09-14T01:24:02.823Z] TOOL RESULT

```
--- HRN leaf 38 (p.17)
- 17 —
und Tomaschek (Pamirdialekte, 806) vergleichen
skr. ksäuma- 'gewobene Seide* {^uparaMäuma-),
ehe ohne s. he (No. 247).
66. e'iter 'Stern*.
phlv. a/tar; arm. LW. a/JarK 'Horoskop*.
Zusammenhang mit aw. apa^tara-, apa/^ra ist
unwahrscheinlich (Hübschmann, ZDMG. 38, 428,
Bartholomae, ZDMG. 42, 154).
67. erj.'Wert' (Sahn. I, 2 Vers 16), erjmend.
aw. arejah- 'Preis, Wert'; phlv. arj^ arjniand;
ai. vergl. arghd- 'Preis, Wert'.
oss. ary (31); arm. yargem 'ehren, schätzen' etc.
(Hübschmann No. 210).
gybis ^^^ 'Wert', erzan^ erzänis, erzTden,
Käs. ezü^ azün, ajiyd, ajiyd, mit Ausfall des r, wie
arm. LW. (?) azan (de Lagarde, No. 25).
aw. arejah-, arejaiti; phlv. arj, arjän, arjamk^
arJUan, päz. arzän etc., arm. LW. (?) armn 'gebührend*,
armnij armnavor; ai. drhati 'es ist wert*.
afy. yarz 'Fähigkeit, Wert*.
68. erz'Ti^ 'Blei'.
arm. arcic.
Geldner' s Gleichstellung mit aw. arezazi- (Yt. 13,
45, KZ. 25, 558) ist lautlich unmöglich; ebenso die
Ableitung von aw. erezata-, skr. rajatd-.
Die Heimat des Wortes ist noch durchaus unbekannt.
69. ers 'Thräne*.
mäz. asr; Käs. asl,
aw. asru- Thräne*; phlv. ars; ai. dgru-; lit. aszarä.
kurd. asr (Houtum-Schindler), {stir^ istir^ histir^
Jaba-Justi, sind wegen des t zweifelhaft); bei. als
(431).
Die indog. Urform war nach Bugge (BB. XIV, 72)
*ddJcru-, da auch gr. ödxpv, acymr. dacr, air. dSr, lat.
lacruma, got. tagr, ahd. zahar dazu gehören sollen.
Mindestens ist eine Dialektspaltung anzunehmen; viel-
U o r n , Qrundriss d. neup. Etymologie. 2
--- HRN leaf 158 (p.137)
- 137 —
Pärsenhandschrift 68, 10), röd(i)sn bezw. röy(i)sn; ai.
rödli' rodliati (KröA-, röltati).
bei. rtiday, n. ruday (319).
Zur i/^rödfi- vergl. Bartliolomae, ZDMG. 44, 553
No. 332.
615. resen 'Strick'.
ai. ragandr 'Strick, Riemen, Zügel, Gurt'; arm. LW.
apa\rasan zügellos*, erasan, erasanak 'Zügel' (Hübsch-
mann, No. 96).
arab. hebr. LW. rasan, bezw. JD^.
616. restden 'ankommen, erreichen', Praes. res-em^
resänTden,
g. rasadmün.
ap. i/^ras' 'kommen, gelangen', arusam^); phlv.
rasltan, ras(i)§n (AV.), rasmitan,
LW. afy. rasedal; bei. rasa(/ (313).
617. risten 'spinnen, Praes. res-efn, riste, resulen, resmän,
rismän, vergl. ebresum (No. 65).
g. risbün *Zwirn .
ai. i/^reg-, rigäte 'rupfen, abreissen.
bei. resag^ n. resay 'spinnen, flechten' (318), üresarj
'spinnen' (40) ; oss. alunjssin, d. alwiessun (bei Geiger).
resk s. eresk (No. 71).
618. risk 'Lauseei, Nisse' (AM. 141 Zeile 11, 191 Zeile 7).
ai. liksd' 'Ei einer Laus, Nisse' (Nöldeke bei
Hübschmann, Oss. Etym., S. 46).
kurd. LW. risk ; af/. riya ; bei. LW. rask, risk 'Läuse'
(217); oss. t. llsk, d. liskä 'Nisse' (170).
619. reften 'gehen, weggehen', Praes. rew-em, reftar, retvä
(arab. LW. rawäj), rewän, rewäne, retvis'^),
aw. y^rap' 'gehen' in rap<ö-.(?)3); phlv. raftafi, rapet^
rawad (3. Sing., geschr. ra/d)^ rawäk, räwäkth^
Aw. rasaintl' (y. 52, 1, 3) gehört nicht hierher nach liartho-
lomae, Indog. Forsch. II, 264.
*) BeilAufig bemerkt, ist die Aussprache rös in dem bei Vullers
aus Bh. 8. V. citirten öahnämeverse falscl^; derselbe steht I, 8 Vers 131.
') Yd. 13, 45. Aber ganz annoher.
```


## [2026-09-14T01:24:16.140Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SOD grep lykh/dykh/letter\"; grep -n \"lykh\\|δykh\\|dykh\\|ð yk\\|nwyt\" SOD.txt | head -20; echo \"=== SOD entries near 148\"; grep -n \"^ *148 \\|^148 \" SOD.txt SOD_pages.txt | head"
}
```


### [2026-09-14T01:24:16.247Z] TOOL RESULT

```
=== SOD grep lykh/dykh/letter
6271:(elephant)  from  Middle  Persian  and  Persian  pll,  dykh 
28286:C2,  48R1  n  p85;  c>nwytyt  C2,  12R5,  27R17 
48860:BSTii:  C2,  gloss.;  pi.  nwyt,  "neophyte",  C2, 
48862:57R14;  ob.  pi.  nwyty,  C2  57R5,  7 
=== SOD entries near 148
SOD.txt:8506:148  "qwytyy    M  =^  "kwyty 
SOD.txt:44799:148
```


## [2026-09-14T01:24:18.402Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"pdf page\" BQT_v2_pages.txt | head -5; echo ...; grep -n \"\\[pdf page\" BQT_v2_pages.txt | awk -F'[ ]' '{print}' | sed -n '1,3p'; echo \"=== find printed page markers\"; grep -n \"^ *926 *$\\|^ *951 *$\\|^ *988 *$\" BQT_v2_pages.txt | head"
}
```


### [2026-09-14T01:24:19.397Z] TOOL RESULT

```
...
=== find printed page markers
```


## [2026-09-14T01:24:22.241Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '6240,6300p' SOD.txt"
}
```


### [2026-09-14T01:24:22.302Z] TOOL RESULT

```
Vy- 

(A  v.  /v/)  and  */y/,  respectively. 

rose  Av.  varzSa- 

see  Av.  va#/i- 

blessing  Av.  a-frivana- 

new  Av.  nava- 

own,  self  Olr.  *griwa- 

favor  Av.  yana- 

agitate  Av.  a-yaoz~ 

to  consider  Olr.  *3-pa(y) 

IX)  The  fact  that  several  Eastern  Iranian  languages 
show  a  sound  change  of  d  >  U  and  also  the  fact  that 
in  Manichean  script  (M)  the  Semitic  sign  lamed  is 
used  to  render  Sogdian  6  and  daleth  to  render  dy 
induced  Andreas  to  assume  the  existence  of  a 
Sogdian  phoneme  /.  This  hypothesis  seems  to  be 
borne  out  by  other  evidence.  In  foreign  loanwords, 
///  is  rendered  by  S  in  the  Buddhist  script  (B) 
especially  in  the  case  of  early  borrowings  such  as 
kSp>  from  Skt.  kalpa-,  Swky  from  Skt.  loka->  pySh 
(elephant)  from  Middle  Persian  and  Persian  pll,  dykh 
(letter)  from  Skt.  lekha-,  and  Smtyr  (lamp)  from 
Greek  lamptir.  In  later  borrowings,  however,  ///  is 
rendered  by  r  (Semitic  recK  which  sometimes  has  a 
special  diacritic  sign  and  is  transliterated  by  r\  thus, 
*ndrnyr-  for  Skt.  indranlla-.  Besides,  when  Sanskrit 
words  are  transcribed  (not  borrowed)  into  the 
"Sogdian"  script,  /  is  rendered  by  r%  e.g.,  pr*n  for  Skt. 
balam. 

Some  Sogdian  loanwords  in  Persian  render  by  / 
what  is  written  6  in  B  and  M,  or  d  and  $  in  C.  For 
instance,  Pers.  mid  (wine)  from  mwS-  <  madu-\  Pers. 
pdlik  (leather  shoes)  from  p*dy\  Pers.  linj-  (to  pull 
out)  from  Sync-  <*0anjaya-%  Pers.  palindin- 
(threshold)  from  pSyund-,  Pers.  balade  (unlawful, 
corrupt)  from  p6Hy-t  Pers.  Yolin  (jug)  from  Yw6yk-. 
The  occurrence  of  double  spellings  in  place  names 
such  as  Badakhshan  and  Balakhshan,Amui(<  *Amud) 
ai*d    Amul    provides    further    evidence    for    such 


transcription. 

However,  against  the  assumption  of  Sogdian  ///  as 
a  separate  phoneme  is  the  fact  that  the  Uigurs,  who 
adapted  the  "Sogdian"  script  for  their  language, 
rendered  Uigur  Idl  by  the  Sogdian  S  and  Uigur  /// 
by  the  Sogdian  r  symbols.  Henning  suggested  that 
Olr,  1*61  and  1*01  merged  in  most  Sogdian  "dialects"
```


## [2026-09-14T01:24:29.736Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR<=6271{n+=gsub(/\\f/,\"\")} END{print \"formfeeds before line 6271:\", n}' SOD.txt; grep -n \"\\[pdf page\" SOD_pages.txt | head -3; echo ---; grep -n \"dykh\" SOD_pages.txt | head"
}
```


### [2026-09-14T01:24:30.950Z] TOOL RESULT

```
formfeeds before line 6271: 0
---
3303:(elephant) from Middle Persian and Persian pll, dykh                 noteworthy, finally, that the word         Badakhshan,
```


## [2026-09-14T01:24:34.114Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3280,3310p' SOD_pages.txt; echo \"=== nearest page tags\"; awk 'NR<=3303 && /page/ {last=NR\": \"$0} END{print last}' SOD_pages.txt; grep -n \"page\" SOD_pages.txt | awk -F: '$1<3310 && $1>3100' | tail -5"
}
```


### [2026-09-14T01:24:35.279Z] TOOL RESULT

```
  /yriw/        Yryw
                           own, self Olr. *griwa-                    Olr, 1*61 and 1*01 merged in most Sogdian "dialects"
                                                                     into one single sound which was kept as 6 in
  2) /y/:
                                                                     eastern Sogdian and became / in Western Sogdian.
  /yin/                    favor       Av. yana-
                                                                     This is, however, contradicted by the evidence of
  /ayDz/        *y>vz-
                    n      agitate Av. a-yaoz~
                  y>                                                 Yaghnabl, which ignores I One should point out that
  /apay/                   to consider Olr. *3-pa(y)
                                                                     the sound change of Idl > III is not general in
              Vy- several Eastern Iranian languages
IX) The fact that                                                    Eastern Iranian. It is only common     to some Iranian
show a sound change of d > U and also the fact that                  languages of Afghanistan such as Pasht5, Yidgha,
in Manichean script (M) the Semitic sign lamed is                    Munji and (the Kafiri dialect of) Prasun. Khotanese,
used to render Sogdian 6 and daleth to render dy                     Ossetic, Yaghnabl and most Pamir dialects ignore it .
induced Andreas to assume the existence of a                         This, probably, was also the case for common
Sogdian phoneme /. This hypothesis seems to be                       Sogdian. The sound change Idl > III might have
borne out by other evidence. In foreign loanwords,                   centered, as Morgenstierne puts it, in the area of
/// is rendered by S in the Buddhist script (B)                      Badakhshan, the north-eastern corner of Afghanistan
especially in the case of early borrowings such as                   and southern Tajikestan, in the region neighboring
kSp> from Skt. kalpa-, Swky from Skt. loka-> pySh                    on the province of NOristan (ancient KafiristanX It is
(elephant) from Middle Persian and Persian pll, dykh                 noteworthy, finally, that the word         Badakhshan,
(letter) from Skt. lekha-, and Smtyr (lamp) from                     which is used in the Islamic period to designate both
Greek lamptir. In later borrowings, however, /// is                  the area and the kind of ruby for which it was
rendered by r (Semitic recK which sometimes has a                    famous, is also spelled with / as Balakhsh (French
special diacritic sign and is transliterated by r\ thus,             Balaisy English Balas).
*ndrnyr- for Skt. indranlla-. Besides, when Sanskrit                    The last word about / is said by Livsic and Sims-
words are transcribed (not borrowed) into the                        Wiliiams. Livsic thinks that the last letter of the

=== nearest page tags
3267: with an older /z/, by palatalization. Isl also merges               116. On Sogdian vocalic j% see page xxxii.
3221:   See "Remarks" (page xxxv) for the differences in
3267:with an older /z/, by palatalization. Isl also merges               116. On Sogdian vocalic j% see page xxxii.
```


## [2026-09-14T01:24:42.804Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ykh *B\\|ykh,\" SOD.txt | head -20; echo \"=== lekha\"; grep -n \"lekha\" SOD.txt | head"
}
```


### [2026-09-14T01:24:42.878Z] TOOL RESULT

```
14451:1050  'nyyznykh    B        jfjxS3Ji><S'j~xs3MKfs  ft) 
38269:zika  ?   ©<zva   =^zykh,  zyq} 
44395:5486  mrznykh  B  ^t^itxXS^ 
49185:6162  nws'ykh   B  <s^l < jfcjk- <,^l 
51538:paslk   (p^ykh,  pJsyq,  p>syk)  ©pi.  -/   ^frsyq 
54830:7013  pr'ykh   B,  S  &r**J* 
63469:8249  pwt'ykh    B  =>  pwty'kfli) 
67898:spase  ©pi.  -/   -^sp'sykh,  ^p^kCw),  ^p's'yh 
86399:zlka   (zykh)  =^zykh,  jyk* 
86405:11535  zykh   B  j^^j 
86412:11536  zykh    B  =»  zyq> 
=== lekha
6272:(letter)  from  Skt.  lekha-,  and  Smtyr  (lamp)  from
```


## [2026-09-14T01:24:50.483Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -5 BQT_v2_pages.txt; echo \"===\"; grep -c \"\" BQT_v2_pages.txt; grep -n \"pdf page\" BQT_v2_pages.txt | head -3; grep -n \"pdf page\" BQT_v2_pages.txt | tail -3"
}
```


### [2026-09-14T01:24:50.572Z] TOOL RESULT

```
                                         ‫‪7‬‬

                          ‫رن‪۳‬‬
    ‫نات‬
      ‫ا م‬
===
41071
```


## [2026-09-14T01:24:53.953Z] TOOL CALL #29: Bash

```json
{
 "command": "sed -n '1,80p' tools/ref_page.py"
}
```


### [2026-09-14T01:24:54.001Z] TOOL RESULT

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
    else:
        print(f"no scan of {abbr} covers printed page {page} (see 'scans' in refs_online.json)"); return 1
    pdf = scan["file"] if os.path.isabs(scan["file"]) else os.path.join(REFS, scan["file"])
    if not os.path.exists(pdf):
        print("PDF not found:", pdf); return 1
    lang = scan.get("lang", "fas")
    out_dir = os.path.join(OCR, abbr + vol)
    os.makedirs(out_dir, exist_ok=True)
    base = os.path.join(out_dir, f"{page:04d}")
    png, txt = base + ".png", base + ".txt"
    if not os.path.exists(png):
        subprocess.run(["pdftoppm", "-f", str(pdf_page), "-l", str(pdf_page), "-r", "300", "-png", "-singlefile", pdf, base], check=True)
    if not os.path.exists(txt):
        # try the PDF's own text layer first; fall back to tesseract
        r = subprocess.run(["pdftotext", "-layout", "-f", str(pdf_page), "-l", str(pdf_page), pdf, "-"], capture_output=True, text=True)
        text = r.stdout if len(r.stdout.strip()) > 80 else ""
        if not text:
            env = dict(os.environ, TESSDATA_PREFIX=TESSDATA)
            r = subprocess.run(["tesseract", png, "-", "-l", lang, "--psm", "6"], capture_output=True, text=True, env=env)
            text = r.stdout
```


## [2026-09-14T01:25:01.409Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"۹۲۶\\|۹۵۱\\|۹۸۸\\|926\\|951\\|988\" BQT_v2_pages.txt | head -20; echo \"=== formfeeds total\"; tr -cd '\\f' < BQT_v2_pages.txt | wc -c"
}
```


### [2026-09-14T01:25:02.310Z] TOOL RESULT

```
118:‫‪ -۱‬شرح این لسخه درسالنامة پاری مال ‪ 4۶۲۳۱‬ص ‪ ۹۵۱-۷۵۱‬در ترجمة احوال «علامه‬
218:Heidelberg 1926 .
248:d’Egypte,        t. XXIV).     Octobre 1951 .
3828:                     ‫ی‬                           ‫‪.‬‬   ‫‪ ۵‬لفت فری ‪۹۵۱‬‬
4008:  ‫«تاوادبا‪« »۹۵۱‬اونوالامده» و ‪ ۵۷056۰‬دراوراق ءانوی‌بپارتی‬                    ‫‪1118‬‏‬
7939:  ‫چنتان» دررهلوی ( ‪ )۳8052)0۵‬ت«اوادیا ‪ )/02)560۵ ۲۰ : ۹۵۱‬م«سینا‬                             ‫‪۱‬‬
16923:  ‫‪1951; ibid, Preliminary Report‬‬                            ‫‪on an Old Dakhma of Yazd,‬‬
16924: ‫‪Reprinted.‬‬         ‫‪Sanj Vartaman‬‬                    ‫‪Pateti Annual‬‬       ‫‪1951.‬‬
17694:  ‫اسلام ‪ :‬در) ‪hãûgrid ۰‬‏ «تاواد‪:‬ا‪ » ۹۵۱‬معرب آن درقاعة « دزی ح‪۱‬صی ‪۵۳٤‬‏ » ودر گاه « ابا‬
19166:      ‫‪« - ۱‬وقاضی را دستوری است که چنین‬        ‫«تلرادیا ‪« 81۲2۷۷20521 ۰ ۹۵۱۰‬ارنوالا ‪. ۷۱۰‬‬
22290:    ‫‪۲‬ص ‪ « ۹۵۱-۹۹۱‬روز شماری ‪۵۵-۷۵۲‬‬                  ‫دین و دبان از آرامی وارد زبان عربی شده ‪ « .‬بشتپا‬
23111:                                            ‫دبتان المذاهی ص ‪.۹۵۱‬‬                 ‫و افراط شهوت داشته اند ‪۰ .‬‬
28078:   ‫‏‪W.B. Henning , Zoroaster. Oxford University Press .London 1951.‬‬
31859:   ‫سال) « بارتولمه ‪۷٩ - ۹۹۵۱‬‏ «یبرکه ‪"۰۰۷-۱۰۲‬استی ‪ 306۹‬و ‪( 0785‬نابستان)‪ ,‬کردی»‬
34348:   ‫« بارتولمه ‪« ۵۹۵۱‬تبر کت ‪ ۲۸۲‬دریهلوی ‪( 1282‬می سر * بی‌یامان)»‪ ,‬هندی باستان _ ‪5871‬‬
35056:  ‫‪ › ۹۹۵۱‬دلب رگد‬           ‫و‪2‬ل«مه‬
39048: ‫) فایده بردن ( ‪ ۵‬بارتولمه ‪۱۹۵۱٩‬‏ ور که ‪ :‬تریبکه ‪ ۹۰۲‬؛ بلوچی ‪ « 6/۹ ۰ 05‬اسشق‬                               ‫‪۷25‬‬
39198:    ‫«لن پول ‪ .‬ترجمهٌ طبقات سلاطن اسلام ترجمة اقبالص‪ »۲۹۲‬ورك‪ :‬تعلیقات چپارمقاله ص‪. ۹۵۱‬‬
=== formfeeds total
683
```


## [2026-09-14T01:25:07.624Z] TOOL CALL #31: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nprint(json.dumps(d['BQT'],ensure_ascii=False,indent=1))\n\""
}
```


### [2026-09-14T01:25:08.718Z] TOOL RESULT

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
```


## [2026-09-14T01:25:13.948Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for L in 386 411 448; do echo \"########## leaf $L (printed $((L+540)))\"; awk -v n=$((L+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v2_pages.txt; done"
}
```


### [2026-09-14T01:25:14.988Z] TOOL RESULT

```
########## leaf 386 (printed 926)
      ‫==‬                                                                                      ‫راغ‬


‫راد بوی » بابایابجد بر وزن ماه‬                    ‫‪٤‬‏ غم و الذوه‬     ‫بر ورن شان‬        ‫راح‬


                   ‫‪.‬‬   ‫ورناند‬
                            ‫عگود‬    ‫چیو»ت‬
                                        ‫رو‬                                       ‫یند ‪.‬‬
                                                                                     ‫بکاوربرا‬
‫راذهنش ‪ « ۴‬بنتحمیمو کر نون‬                       ‫بروزن شاد » کریم و جوالمرد‬          ‫راك ه‬
‫وسکون شین قرشت »کرم طبع وسخا پیشه را‬             ‫وصاحب‌همت وسخاوت‌را کویند‪٩‬‏ ‪ -‬وبمعنی‌شجاع‬
                                   ‫کونند ‪*.‬‬     ‫و حکیم و دانشمند را نز‬       ‫‪-‬‬   ‫و دلاور هم هت‬

 ‫راز = بر وزن قاز ‪ .‬بمعنی پوشیده‬                 ‫سخن کوی و سخن گزار‬        ‫و دیمهم‬    ‫‪-‬‬   ‫گفته اند‬

 ‫وپنېان‌ونېفته واسرار دل‌باشد‪ - ۴‬ورنگه ولوزرا‬                     ‫و قصه خوان حمآمده است (‪. )۱‬‬

                                                                    ‫(‪ )۱‬جك ‪ - :‬است ‪.‬‬



               ‫‪ ۰.‬قی ‪ :‬اوستا _ ‪itiûra.‬‏ هندی باستان _ ‪tûr‬‏ (خواحان دادن) اسشق ی‬                ‫‪۰‬‬

   ‫ابرست تيخ‌نيزش‪ .‬اپری که فطر او خون‪.‬‬             ‫بحریست دست رادش " بحری که موج او در‬
             ‫تش‬        ‫وراد‬
                          ‫‪۳‬‬                 ‫‪= ۴‬رد(ھم‪.).‬‬               ‫‪ ۵‬معزی لشابوری ‪٩ ۹۳۵‬‏ ‪.‬‬
  ‫)‬     ‫»ی‬‫ور‬
           ‫دابی‬
              ‫‪ 82‬ا(تزوا › ننه‬  ‫‪۲‬تا‪-2‬‬
                                   ‫‪ ۴‬پ‪-‬ھلوی ‪ « 28۲‬تاوادیا ‪٤ ۲ : ۶۹۱‬ء‏ او‬
      ‫که ‪ ۵۹۱‬ساسکریت ‪58۵۲‬‬   ‫« بارتولمه ‪ 6۱۵۱‬آرامیع ‪ ( 8287‬سربالی ‪« ) "82۵۲۵‬ریب‬
  ‫) از‬    ‫(خفیانه‬
                ‫در اوراق مالوی ( بپارتی ) ‪ 86215۷۳‬م‬          ‫ا(تروا» سر » راز) « اسشق ‪۲۰٩‬‏‬
                                                 ‫( قی ‪ :‬اوستا ‪ ,01222-۲‬فارسی ‪:‬‬                ‫چ‬
                                                                                          ‫راز ) ‪٩‬‏‬
                                                      ‫‏‪(Henning , A list of Middle‬‬
                                                 ‫‏‪Persian ..., BSOS, IX, 1,0. 87.):‬‬
                                                              ‫راز نپان خویش جپان کرد شآکار‬
                                                   ‫در ماصب وزارت دستور شپربار ‪.‬‬
                                                   ‫«معزی لیشابوری ‪۹۶۳٩‬‏ ‪.‬‬
                                                  ‫‪010۵۲‬‬    ‫رادیو ‪ -‬از فرانوی‬          ‫‪#‬‬
                                                 ‫( بی‌سيم ‪ .‬پرتو مجهول ) ؛ ابزاری برقی‬
                                                 ‫( الکتریکی) که سوت را ازفواصل دور ضبط‬
                       ‫رادیو‬                                                      ‫‪ ۳‬مشش کند ‪2‬‬

                                                                             ‫بقيه از صفحة ‪e‬‏‬
      ‫وین راح خداوند همه خلق جهانست‪.‬‬                 ‫آن روح خداوند همه خلق جهان بود‬
   ‫د منوچهری دامفانی ‪. * ۸‬‬
   ‫‪ ( 0-2‬دلل ‪ ۰‬علت » اصل ) در‬‫‪۲‬تان‬
                                ‫‪ #‬را = رای ‪ .‬پپلوی ‪ , 0۵۲‬ایرانی باس‬
  ‫‪ ( 27۳3۷۸ -‬از بن‌رو‪ .‬ازیرا) « بارتولمه ‪ ۱۲۵۱6 ۹۷۱۰‬نر که ‪ ۹۸۱‬ورك ‪:‬سو کو‬                         ‫‪7‬‬
    ‫مارسن ص ‪ » 10878012۷۸2 :۱۹۱‬طبری ‪ 8۲‬دزتر» (بکر اول و دوم) (ترا) «صاب طبری‬
   ‫‪. ۱‬کیلکی ‪ 6۲‬در‪6‬؟‪(61۳1-‬مرا)‪( 61 -6۲ ,‬نرا)؛ شهمپرزادی ‪ ۵۳‬؛ علامت مفعول صریح ‪:‬‬
     ‫‪ ۶‬مرا کت از آنجا که همت درویشان است ‪ . . .‬خاطری همراه من کنند که از دشمنی صب‬
                                                ‫‪ -‬برای» در ؛ مه ‪.‬‬    ‫ادیتنا کم ‪.٩‬‏ «کلتان ‪٩۲‬‏‬
  ‫(رهان اطع ‪) ۱۳۱‬‬
                ‫ب‬

########## leaf 411 (printed 951)
 ‫رشتاك‬                                                                                                       ‫‪-‬ي‬
                                                                                                              ‫‪ --‬ا‬


                ‫‪.‬ویند عربی است ‪.‬‬
                               ‫رزه باشد گ‬                       ‫روز رش باوتعلق دارد ‪ - ۱‬ونوعی‌ازجامة ابرشمی‬
‫ر شت = بفتح اول بر وزن طشت ‪ ۰‬نام‬                                ‫کران بها باشد ‪ -‬وبازورا (‪ )۱‬نیزگویند که‌آن‬
‫شهری است از ولایت کیلانکه آنرا «بیه پس»‬                         ‫از سردوش است نا آرنج ‪ - ۴‬ومسافت ميان دو‬
                                                                 ‫دست‌رالیز گفته‌اند چون‌ازهم‌باز کنند؟ سومخقف‬
                                                                ‫ارش هم‌هست وآن ازآرنج‌ناسرانگشتان دست ‪.۴‬‬
‫می‌بافند ‪ - ۸‬وبمعنی خاك و گردوغبارتبره ولجن‬
   ‫کرو هر امنات‪٩‬‏ کو‬
‫گفته‌اند ‪.‬که بدان خاله سقید کنند ‪ -‬وهرچیز برا‬
                                                                ‫وگز ومقدار را لیز گویند؟ ‪ -‬وزه‌ین‌پشته پشته‬
                                                                ‫راخمکفته‌اند؟ ‪ -‬و قمی ازخرماست» وآن‌سیاه‬
                                                                 ‫وبالیده میباشد‪ -‬ونام لوعی از الجیر هم هست ب‬
‫لیز کوبند که ازهمفروریزد وفروپاشد ‪ -‬ودیواری‬
‫برافتادن بود ‪ -‬و حم‬      ‫را نز کنته‌اند که مذرف‬                  ‫وسیماب و زیبق را بیزمیگوبند ‪ -‬وبائانی مشدد‬
                                                                 ‫در عربی » باران اندك و ریزه ریزه را گوبند‬
‫اول فروغ و روشتابی باشد *‪ -۷‬ونام مردی بود‬
                                                                 ‫»ردانیدن‬‫ورثان جمع آن آست‪ - ۵‬وبضم اول گ‬
   ‫یدن‬  ‫سشتن‬
           ‫رر‬ ‫ونی‬
                ‫کیمیاکر ‪ -‬و بکر اول بمع‬
                                                                 ‫چشم باشد از روی‌فهر وغضب وخشم‪ -‬ویکراول‬
    ‫ود ‪۱٩-‬‏ وسرشت وطیئت را نکیوزبند ‪.۳۱‬‬
                                                                 ‫مخففرش است که‪,‬عربی لحبهکوبندا ‪ -‬ومخذف‬
‫شتا ‪ ۴۱۰‬با فوقانی بوزن افلاکه ‪۰‬‬
                              ‫ر‬                                                         ‫‪. ۱‬‬       ‫رش حراحت حم هت‬
‫برآ هده و راست‬       ‫شاخی که تازه از بیج درخت‬
                                                                 ‫شزاشه ‪ - ۲‬بنتم‌اول وانی‌بالف کشیده‬
                                        ‫رسته باشد ‪#.‬‬             ‫و شین نقطه دار مفتوح » قطرهای کوچك باران‬

                                                                                      ‫(‪ )۷‬چك ‪ :‬ویاورا ‪۰‬‬
  ‫بر گرفت وایزد‬      ‫رش‌خود‬   ‫عسی را بردو‬    ‫_«شمعون‬                    ‫رك ‪ :‬ح ه صفحهٌ قبل‪.‬‬            ‫‪۱‬‬

                ‫مخفف «ارش» (ه‪.‬م‪:).‬‬               ‫‪۳‬‬              ‫راستاش کرد“ «الحیل فارسی ص‪“ ۰۲‬ورك‪۳ ۳ :‬‬

         ‫لزه ببست رش دگسرتای(گزای)ت وکند‪.‬‬                              ‫روز عصات‬                   ‫یگریت ا‬
   ‫«متوچپری دامغالی ‪.*۳۱‬‬
   ‫‪۴‬کنده ورش » فراز ونثیب زمین بود که پشتهپشته باشد اگر چه دشت بود ‪.‬‬
                                                                   ‫«‬
                                                                                          ‫عنجيك (ترمذی) کوید ‪:‬‬
           ‫له کنده داندو نه رش‬     ‫دنو رمده‬

   ‫«لغت فری ‪. ۱۲۲‬‬

   ‫® ‪( -‬عر) «رش بالفتح‌چکیدن آب وخون واشك وباران اندك وریزه باریدن و باران‌ریزه»‪.‬‬
  ‫خون‬     ‫« رشاش » کسحاب » چکیدهای‬           ‫‪- ۷‬‬                      ‫رش‬         ‫ول‬                 ‫«منتپی الارب؟ ‪.‬‬

                  ‫ورشاشه نا و از تازی است د«ناظم‌الاطیا» ‪.‬‬                  ‫واكاك وآب وجزآن» «منتپی‌الارب»‬
  ‫کیلو متری شمال‬         ‫اول » در ‪۹۶‬‬      ‫مر کزاستان‬        ‫حدید‬    ‫گبلان ‪ :‬در تقممات‬         ‫کرسی‬     ‫‪- ۸‬‬

   ‫‪ :‬گوهر رود وصیفقلان رودیار از آن‬         ‫ودو رود‬         ‫که‬     ‫‪۰۰۰۶۲۱‬‬    ‫و‬    ‫باختری تپران ‪ ۰‬دارای ‪ ۵‬خش‬
   ‫لش (بضم اول)؛ لوش» لوشن» لجن‬              ‫>‬       ‫‏‪٩‬‬            ‫‪۶۰۱-۷۶۱۰‬‬           ‫گذرد ‪ .‬رك‪ :‬راهنمای ابران ص‬
            ‫(ھ‪.‬م‪(.‬‬   ‫‪ ۰‬روشن‬    ‫(«‪.‬م‪).‬‬    ‫رآك‪ :‬رخش‬         ‫‪۳ ۱‬‬           ‫‪۰‬‬   ‫نامه ‪YA‬‏‬       ‫واژه‬    ‫لڙن ‪ ۰‬طبری ‪hsal‬‏‬

   ‫‪ -۴‬مبدلدرستاك» (ھ‪.‬م‪(.‬‬                ‫‪ _۴‬مخفف «سرشت» (ه‪.‬م‪.).‬‬                            ‫‪_ ۲‬رك‪ :‬رشتن‪.‬‬
   ‫* رشتن ‪ -‬بکدر اول وفتح سوم » هندی باستان ربغ ‪( 8411 - ۶۵۲ -‬چیدن پ»اره‬
   ‫کردن)؛بلوچی ‪ 8256۲‬و‪( 08256۲‬تایدن)‪( 296۳0,‬رسیدن)‪ ,‬استی ‪,nusseiwla 81981۷12‬‏‬
                 ‫تافتن » تاسدن‪.‬‬     ‫]| ؛ رسدن»‬            ‫ورك ‪ ۰‬حویشمان انا ‪ ۰‬آقی ‪ 1‬تن‬                 ‫‪YA‬‏‬    ‫شق‬

########## leaf 448 (printed 988)
 ‫‪۳‬‬                                                                                            ‫ربیای‬

‫نز گویند که از شیر کوسفند یزندبهر نحو که‬       ‫ریباس ‪ - ۲‬بائالی مجهول وبای ابجد‬
                                      ‫باشد ‏‬    ‫رستنیی باشد خودروی و عردم‬            ‫بر وزن گیلای‬

‫یرچال* ‪ -‬بروزن‌فیفال » بمعنی ربچار‬             ‫آمراخورند‪ .‬طعمآن میخوش است وبفایت از که‬
 ‫است که مربای دوشابی ‪ -‬وآنچه از شیر وماست‬                      ‫مشود وآارا ربوای هم میگویند ‪.‬‬
                       ‫گوسفند وغسره مر ند ‪۰‬‬
                                                ‫رليك = بفتح اول و بای ابجد وسکون"‬
‫زرن بیچاره ‪.‬‬   ‫ومب‬
                 ‫ریچاله ‪ - ۱‬با لا‬               ‫تانی ودال بی‌نقطه ‪ .‬نام صحرابی است کهجنکه‬
    ‫بممتی ربیمال است که مربای دوشابی باشد ‪.‬‬     ‫ره رخ که بیازده رخ مشهور است ميان‬
                                                                ‫ایرانی وتورانی در انجا وافع شد ‪.‬‬
 ‫ریحان تاتادی سبکرنون‪ .‬بمعنی‬
     ‫خوش نظر است وآ ارابترکی قلفه گویند ‪.‬‬       ‫ریتانج " ‪ -‬بااول بتانی رسیده وفوفالی‬
 ‫ربحان داود ‪ -‬رستنی باشد که‬                     ‫رباانلف کشیده و لون مفتوح بجیم زده ‪ ۰‬بمعذی‬
                                                         ‫درخت‬      ‫از صم‬     ‫که نوعی‬      ‫ینج ات‬
                                                ‫صنویس‬
 ‫آنرا مرزنگوش خوانند ‪ .‬و بعربی آذان‌القار‬                                                      ‫باشد ‪.‬‬
                                    ‫کم‬
                                                ‫رشه »‬         ‫زربت ‪ -‬بفتح موفانی بر وزن‬
‫رجان ررد کنایه از شماعآفتاب‬
                          ‫ی‬                     ‫است درهندوستان شیه بفادق لیکن‬
                                                                              ‫بار درختی‬

                                                 ‫کوچکتر ازآن باشد ‪.‬آنرا درآب کنند و دست‬
 ‫ریخ ‪ = ۲‬بکر اول بر وزن سیخ ‪۰‬‬                    ‫اهب کف کروی ولان رها‬
                          ‫له انان ح‬
‫ویوانات دیگر که روان و آبکی‬                                                 ‫ابرشمینه بدان شویند ‪.‬‬
                                      ‫باشد ‪.‬‬    ‫ر تیانج ‪ ۰ ۴‬باتستالی و جیم بروزن‬
 ‫ر یخی ‪ - ۸‬بروزن بش بن » چیزی‬                    ‫می‌متاند ‪ .‬سرطان حجری‌است‪ .‬وآن سنگی‌است‬
 ‫باشد سیاهوبیار ترش کهآنرااآرزد هیده وشیر‬       ‫است در دویم؛‬          ‫مانتد سرطان ‪ ۰‬طعت آ‬
                                                                   ‫سنرد‬
 ‫لندضم کاف وسکون‬
               ‫ابی‬
                 ‫وعر‬
                   ‫خدوب‬
                      ‫‌ل‬‫یندحساز‬
                              ‫کسف‬
                                ‫کو‬                  ‫وبعضی کوبند نوعی از سرطان دریابی باشد ‪.‬‬
                           ‫با وحای حطی ‪¥.‬‬
                                                 ‫ربجار ‪ ۴‬ه با جیم فارسی بر وزن‬
 ‫دیختنی ‏‪ - ٩‬بر وزن بیختنی ک»تابه‬              ‫» مطلق مربا راگوبند عموماً رمربایی که‬
                                                                                                 ‫دمدار‬
        ‫ازثارباشد اعم از گل وزر ومانند آن ‪.‬‬     ‫از دوشاب يخته باشند خصوصاً ‪ -‬و هر چیز را‬
   ‫رویز ‪e ۹۳‬‏ ‪(.‬‬     ‫(ه‪.‬م‪= ).‬‬   ‫روج‬    ‫ربوا ج (ه‪.‬م‪= (.‬‬       ‫(ه‪.‬م‪- ).‬‬   ‫ریوای =‬      ‫=‬    ‫‪۱‬‬

  ‫‪) ۲۱۱۷۵276‬رف( « یزد ج ‪ ۱‬ص‬           ‫كل ‏‪ e‬س ‪ = ۰ ۱۹۰‬قت‪058[16‬‬                ‫‪Rheum‬‬           ‫‏‪Ribes‬‬
   ‫)‪ ۰‬و آن توعی از ریه ‪:‬د (ه (‪.e‬‏ است که در نقاط مرطوب وشن زار روید ودم برکهه‌های‬                 ‫‪۶‬‬
   ‫‪۴‬ر‪۲‬ا=تیانج صراینج‪.‬‬       ‫‪- .»4۷۲‬‬      ‫الب‬
                                           ‫ل« ک‬
                                              ‫کند‪.‬‬
                                                 ‫آن‌سیار ضخیم گردد وباآن ‪.‬ربا وشربت ساز‬
   ‫‪ = ۴‬ربجال (ه‪.‬م‪ = ).‬ریجاله‪.‬‬         ‫‪ - ۳‬مصحف «ربيانج» ‪ .‬رك‪ :‬رییان » ارییان ‪.‬‬
   ‫معرب آن رصار ( وریصال ) جمع رواصیر ‪ .‬دزی ‪ (۲‬جح | ص ‪ ) ۵۲۷۵‬آنرا ‪ 6۷۲650100‬ترجمه‬
   ‫کرده است ‪ ۰‬دربحرااجواهر ذیل رواصیر آمده‪ :‬آلچه‌ازبقولدر آب‌طبخ کنند و روغن ونرشی‌ها‬
                  ‫رساله (هم‪. ).‬‬   ‫ربحار (هم‪= ).‬‬    ‫=‬     ‫©‬          ‫برآن افزایند ‪۱‬‬       ‫و ادويةٌ حازه‬


    ‫‪ =۷‬ریغ» وربخوك درلهجة گنابادیه گناباری» =‬            ‫‪ 1‬ر=بچال = ربچار(ه‪.‬م‪).‬‬
   ‫‏‪ - ٩‬از ‪ :‬ربختن ‪-۳‬ی (لیافت)‪.‬‬       ‫رخبن (ه‪.‬م‪ ).‬ت‬      ‫‪A‬‏ =‬           ‫‪.‬‬    ‫رین‬
                                                                               ‫عضو ‪.‬رك ‪ :‬ریغ *‬
                                                                                             ‫ر‬

   ‫فدحرهٌ ‪۷۸٩‬‏‬  ‫صیه‬
                  ‫بق‬
```


## [2026-09-14T01:25:42.314Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for L in 449 450 451; do echo \"########## leaf $L (printed $((L+540)))\"; awk -v n=$((L+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v2_pages.txt | head -60; done"
}
```


### [2026-09-14T01:25:43.404Z] TOOL RESULT

```
########## leaf 449 (printed 989)
  ‫زر‬                                                                                                       ‫‪۷‬‬

‫اول زای‬     ‫مردی هم بوده است؟ ‪ -‬ویجای حرف‬               ‫ر جر = با ثالی مجهول بروزن دمگره‬
               ‫قطه‌دار (‪ )۲‬هم بنظر‌آمده است ‪.‬‬           ‫نوعی از پازهر باشد ومعرب آن فادزهر است ‪.‬‬
‫رید کان ‪ = ۴‬بر وزن کردکان ‪ .‬غلام‬                         ‫رین ‪ - ۲‬بكر اول وثالكث و سکون‬
                                                        ‫حبوانات دنگ رکه اسهال‬        ‫» آدمی و‬            ‫ثالی ونون‬
                  ‫بچگان و پسرکالرا گوبند ‪¥.‬‬
                                                               ‫کاری کند ‪۰‬‬    ‫داشته باشد و آلوده‬          ‫وشکم رو‬

‫رار هیکر اول و سکون ثانی محجهول‬
‫وکام‬      ‫وزای قطه‌دار » جرعه وییمانه ‪ -‬ونعمت ‏‬          ‫= ریاکولوثالت‌بروزن بی‌چیزه‬                 ‫بر‬
                                                                                                      ‫ر‬
 ‫‪ -‬ورحمت باشد ‪ ۱‬و‪-‬خرده‬                ‫اد‬
                                       ‫را و‬
                                          ‫مهو‬
                                            ‫و‬            ‫را‬    ‫کنند و‬   ‫چوبی که کاوآهن را بر آن نص‬


 ‫وریزه را نکیوزیندا ‪ -‬وامر بریختن هم هست‬                        ‫برخیش بندند بجهت زمین شیار کردن ‪.‬‬
                                      ‫بعنی بریز‪. ۷‬‬       ‫ید‪ ۲‬یک راول وفتح‌دال ابجد(‪)۱‬‬      ‫ر‬
 ‫ریژ ص بکر اول وسکون انی و زای‬                           ‫مروزن زیبراه‪ .‬یران امرد بی‌رش وغلامان ترك‬
‫پشته پشته باشد ‪ - ۸‬وکامو مراد‬               ‫»ن‬
                                             ‫می‬‫زرسی‬
                                                  ‫فا‬    ‫و ام‬    ‫مقبول باشد ‪ ۴‬؛ ویفتح اول نبز کفته اند‬


                                       ‫(‪ )۲‬چك ‪ - :‬نقطه دار ‪.‬‬            ‫ایسد ‪.‬‬      ‫(‪ )۱‬چك ‪= :‬‬

  ‫پپلوی ‪katêr‬‏‬         ‫ا‬              ‫ریخ («م‪ ۳ ).‬ان (ین‌سبت) [ر که‪ :‬یمن ] ‪۰‬‬                ‫ار‬
          ‫(یسر ‪ .‬غلام جوان) «اونوالا ‪ ۰ ۰۳4‬قس ‪:‬کیلکی ‪ ۷6۲‬و مازندرانی ‪( 261۲‬یر) (ھ ‪.‬م‪ ).‬۔‬
        ‫مر کبان داغ نکارده قطار اندر قطار ‪.‬‬               ‫‪ - ۴‬ریدکان‌خواب‌نادنده مصاف اندرمساف‬
   ‫«فرخی سستالی ‪۹۷۱٩‬‏ ‪-‬‬

   ‫ظ ‪ .‬مراد « ردك خوش آرزو» قهرمان رسالهٌ پهلوی « خسروقدادان و ربدكك وی »‬                            ‫‪۴‬‬
   ‫است ‪ .‬رك ‪ :‬رسالة مزبور ترجمه وطبم اونوالا‪ .‬پارسس ص‪۷۱‬؛ و رسالة مزپور ترجمةّ نگارنده در‬
       ‫‪ - ۴‬جمم ‪ :‬ردك (ه‪.‬م‪).‬‬              ‫مجلهٌ آموزش وپرورش سال ‪ )۳۲۳۱( 8۱‬ص ‪. 64۱‬‬
          ‫رك ‪ :‬رشتن ‪..‬‬      ‫‪۷‬‬           ‫‪.‬‬     ‫‪ - ۱‬رك ‪ :‬رىزى بر‬           ‫‪.‬‬   ‫(جم)‬    ‫ریژ‬     ‫=‬       ‫®‬

                                  ‫‪.‬‬         ‫اورامالی ‪( 28۳‬رنکه درشت) دك ‪ .‬اورامان ‪۵‬‬              ‫‪-‬‬   ‫‪۵‬‬

   ‫‪«Titan‬‬     ‫دهلوی‪‎‬‬   ‫وفتح سوم ‪ ۳۳‬رستن («‪.‬م‪ »).‬اوستا ريثة _‪082۰-‬‬           ‫ور قطان ات بکراول‬        ‫‪N‬‬

       ‫حندی باستان ربشة ‪( 171۲ . 6۲-‬آزاد گذاشتن» دواندن)‪ .‬کردی ‪ 8161۲۰‬استی ‪ 01011‬رصق]ء‪‎‬‬
       ‫ورك ‪ :‬هوشمان ایشا کلکی ‪ ۳ 066۲‬تخلة شکم کردن؛ ای‪‎‬‬                          ‫بلوچی‪ 1 hgayir ‎‬اسشق‬

                                                                             ‫حاجت کردن ‪ ,‬تفوط کردن‪. ‎‬‬

                                                                                       ‫شه اصزفحه ‪٩۸٩‬‏‬
   ‫مصدری ) ‪ .‬اوستا رمشةٌ‬        ‫بکر اول وفتح چهارم ‪ ۰‬از ‪ :‬ریخ ‪ +‬تينو(ند‬                    ‫* رای‬
       ‫‪ ( 621206231 ,6681-‬بیرون ربختن) » پهلوی‪ » 0806۲ .‬لائینی ‪ .61211011‬هندی باستان‌رمشةٌ‬
       ‫ترن ] وارمنی ‪026021‬‬
                         ‫خک‬‫برسی‬
                              ‫یه کردن ) [ قس ‪ :‬پا‬
                                                ‫ترخدنل»‬
                                                      ‫‏_‪ ( rêc‬فقط بمعنی‌وا گذار ک‬
       ‫استی ‪nujêl‬‏ ‪( ,nijîl‬دوبدن ‪ ۰‬فرار‬         ‫( ترك کردن ‪ ۰‬رها کردن) ‪ ۰‬کردی ‪nitêr‬‏ (برون ریختن)‪.‬‬

        ‫کردن) ؛ بلوچی ‪20۵ 6‬کرناق ‪ 8191‬وخی ‪ 63۲۵۷۰ -0212‬سردکلی ‪(216۳2۷ - 003‬خته‌شدن)‬
       ‫«اسشق ‪۸۳۱‬؟؛ روان کردن ‪.‬جاری کردن مایم در ظرف بامحلی ‪ -‬دور انداختن_ پاشیدن_ افکندن‬
                                                                        ‫‪۰‬‬    ‫شارکردن‬       ‫پرا کنده کردن ‪-‬‬           ‫‪-‬‬
########## leaf 450 (printed 990)
    ‫اس‬                                                                                                  ‫رىژك‬
             ‫ماضی ریدن و لجاست کردن باشد ‪.‬‬                          ‫وآرزو و هوا وهوس را بیز گفته‌اند ‪٩‬‏ ‪.‬‬
‫= بروزن زستن» فرورفتن بچاه‬              ‫ی‬‫ل‬                   ‫ریژ ك ‪ -‬بکر اول وفتح زای فارسی‬
 ‫باحوض وامثال أن باشد‪-‬ویمعنی موبیدن ونوحه‬                    ‫وکناه کردن و از جای‬         ‫»ن‬
                                                                                          ‫یكا‬
                                                                                            ‫سيش‬
                                                                                              ‫عن ش‬
                                                                                                 ‫بر وز‬
‫سفتن و کربه‬
          ‫یخف‬
            ‫کردن همهت ‪٩‬ک‏‪-‬روم‬                                                    ‫فرو لغزبدن باشد ‪.‬‬
‫وجاست کردارا نیز‬
               ‫کردن بود ‪ - ۷‬وریدن ت‬                          ‫ريز هةسیهیی ک=نابه از ستارگان‬
                                        ‫کوند ‪. ۸‬‬                                                        ‫باشفد ‪.‬‬

 ‫= با اول بثانی مجهول رسیده‬             ‫سی‬
                                         ‫ر‬                   ‫دیزی راز = بعنی رحمتی بکن ‪۰‬‬
                                                                   ‫هم مده است ‪۰ ۳‬‬          ‫چه رىز بمعدی رحمت‬

                                             ‫است ‪.‬‬         ‫ریس = بکر اول وسکون‌ثانی وسین‬
 ‫ر پسیدن ‪٩‬‏ س بروزن لسیدن » رشتن‬
                                                         ‫بی‌نقطه » غضب وقهر وخشم راگویند ‪ -‬وباثالی‬
    ‫پنبه و تافتن پشم وابرشم وامثال آن باشد ‪.‬‬
                                                         ‫مجهول ‪ .‬شوربای غلیظی کهبربالای شله پولاد‬
 ‫است‬       ‫رشو»ف‬
               ‫عنکی‬
                  ‫موز‬
                    ‫دش = بر‬                                  ‫و کشکك وامثالآن ریزند ‪ - ۴‬و هربه وحلیم‬
                                                             ‫را دز گفته‌اند لیکن قبل از آدکه پخته شود ‪۰‬‬
 ‫‪—-4۹‬‬    ‫جراحت‬   ‫‪۰‬‬   ‫با ثالی محجپول‬     ‫خوانند و‬                  ‫تم‬
                                                                   ‫هن ه‬
                                                                      ‫یهعننیوزآبکی باشد ‪ -‬و امربرشت‬
 ‫وشوربای‌هربه راکویند پیش ازکفجه زدن؟‪.۱‬‬                       ‫بعنی بربس ‪ ۴‬و‪-‬بفتح اول در عربی خرامیدرا‬
‫بیدشوع‌سفید کردن ‪ -‬کنابه‬        ‫ر‬                                                                    ‫کرننده ‪.‬‬
   ‫از مردم بیمقل و کسکه کم تجربه باشد ‪.۳۱‬‬                    ‫‪« ۰‬عنی رید که‬   ‫بروزن زست‬        ‫=‬    ‫زر لست‬


                                                                                       ‫)‪ (۱‬چك‪ :‬و ‪.‬‬


                 ‫‪ = ۱‬ریز (ه‪.‬م‪).‬ریرٌ» معمولا با «کام» اید و ریژکام با ریژوکام گویند ‪:‬‬
          ‫با ریدکان مطرب بودی بفر و ژب‪.‬‬                             ‫دیدی تو ریژو کام بدو آندرون بی‬
   ‫«لفت‌فری‪.*۹۷۱‬‬        ‫کی سمرفندی‬     ‫رود‬


   ‫سپولت شناخته میشود که همان سغدی ‪( 0128۲‬میل » شهوت) است ونیز درسفدی‌مصدر‬
                                                                             ‫‪ ) hzêr‬دوست داشتن) آمده‪. ‎‬‬
             ‫‪Henning,‬‬           ‫‪Sogdian‬‬      ‫‪‎ BSOS.,X, 1,p.99.‬و ‪loan _ words...‬‬
   ‫‪-‬ب ریس پمعتی آب‌چلومعمول‬
                          ‫‪ ۴‬آ‬                        ‫‪.‬‬       ‫اسبید‬
                                                                 ‫منا‬
                                                                   ‫ت) مت‬
                                                                       ‫رعر‬
                                                                         ‫‪-‬معنی فتض (‬
                                                                                   ‫‪ ۴‬ب‬
   ‫‪( -‬عر) قرس بفتح‬          ‫‪0‬‬            ‫رشنن ‪.‬‬   ‫رك‪ :‬رسدن ‏‬           ‫‪۴‬‬          ‫نامه ‪8‬‬    ‫‪ ۱‬لت‬   ‫‪ ۴‬رکه‬    ‫است‬


  ‫رسته بمعنی مرده «بشتها‬         ‫=‬    ‫در پهلوی رستك‬      ‫‪-‬‬    ‫‪۹‬‬          ‫اول‪ ,‬خرامیدن» « منتهی الارب» ‪.‬‬
                     ‫رك‪ :‬ريدن ‪.‬‬       ‫‪۸ 7‬‬         ‫کی‬                 ‫ر‬             ‫‪۲‬ص‪ ۳۳ ۲‬رك ‪ :‬رستاخیز‪.‬‬
########## leaf 451 (printed 991)
                                                                                                    ‫‪.‬هرهس‬
 ‫چویزها بیاویز قد ‪-‬‬         ‫ا‬
                            ‫هاز‬‫اه‬
                                ‫جد ک‬
                                   ‫ابباریشم باش‬       ‫ریش خو ت‪۵2‬ه با ای مجهول ‪ ۰‬نام‬
 ‫وآ نچه ازدرخت درزیر خاکه باشد ‪ -‬ونام‌مرضی‬                ‫مرضی وعلتی است کهبعربی خنازیر گوبند ‪.‬‬
              ‫است که آبرا عرق بدلی گونند ‪.‬‬             ‫‪٩‬‏ ‪-‬‬   ‫ایت‬     ‫معروف‬     ‫قاصی‪-.‬‬         ‫رش‬

 ‫يرشیدن » بروزن پیچیدن» فروربختن‬                      ‫گزونند که برششه بکادوی شراب‬
                                                                                ‫ولته‌ای را ل‬
                        ‫‪.‬‬    ‫چیزی باشد در چبزی‬        ‫ندند تچاون شراب در بیاله ریز ندصاف رشته‬

 ‫ریشیده ‪ ۲‬ه بر وزن پیچیده » ربغ‬                       ‫شودو کوشٌآن لته کراهآوشته وشراب "رشده‬
 ‫دستار باشد ‪ -‬وبمعنی رنکگ بپشته و ریگ نهاره‬           ‫وقطره قطره‌شراب اآزن میچکیده باشد لیزریش‬
                                                                                  ‫قاضی گویند ‪.‬‬
‫بووپدر‪-‬نیان منقش را نیزگوبند ‪ -‬وام ‪,‬یکی‬
 ‫ازیادشاهان هند حم بوده است‪ -‬ویمعنی رخشنده‬            ‫ریش گاو = با ثالی معروف ؛ مردم‬
 ‫وروشن هم هست‪ -‬وبا ثائی مجپول‪ .‬رشو زخم‬                ‫ابله راحمق وطامع وصاحب آرزو باشد ‪ .‬گویند‬
                          ‫شده رگاوشد ‪.‬‬                ‫شخصی پرخود راگفت که «هرکز ریش کاو‬
 ‫ربع = بروزن قح » مخفف آريخ است‬                       ‫کشاو ؟»‬
                                                            ‫بوده ای ؟» پگرفت‪ :‬ک«دام است ر‬
‫وت و کینه باشد ® ‪ -‬وباثالی‬    ‫او‬ ‫درت‬
                                   ‫عه نف‬
                                       ‫ک‬              ‫کفت ‪« :‬آنکه هرصباح از خأنه برآبد با خود‬
 ‫‪۱‬ه دامن کوه بجالب‬‫مجپول‪ .‬بمعنی راغ‌است ک‬              ‫کوبد کنجی بيابم و چنان و چنین کنم ‪» .‬‬
                           ‫صحرا باشد ‪. ۷‬‬              ‫ب رکفت ‪ « :‬ای پدر ! من همه عمر ریش گاو‬
                                                                                                    ‫بوده‌ام‪¢ .‬‬
 ‫ريغال ب‪-‬اغین شطه دار بروزن قبقال ‪.‬‬
 ‫وشکول را گوبند ؛ و بمایعننی بازای‬
                                 ‫قدح ک‬                    ‫فازانشیوشده‬
                                                                    ‫بمب‌‬
                                                                       ‫دیش کندن = کنا‬
                      ‫نقطه دار همآمده است ‪. ۵‬‬                                              ‫کشیدن باشد ‪.‬‬
                                                      ‫ر یشمال ‪ .‬با میم بر وزن پزیرال ‪.‬‬
 ‫ریک ‪ -‬بکراول وسکون ثالی وکاف‪,‬‬
                                                                  ‫‪۱‬‬           ‫را گونند ‪۱‬‬   ‫وی‌حصت‬        ‫دیوث‬
 ‫بمعنی ای ليك بخت باشد وعدرربی وسحكث‬
 ‫کویند ‪٩‬‏ ‪ -‬وباکاف قارسی‌بروزن دیگه معروف‬                ‫ریشمالی ‪ - ۴‬بروزن‌نیك‌فالی‪.‬د‪,‬وی‬
 ‫ونایت از ذره‬
            ‫‏(‪ ۱٩)۱‬و عربان رمل خوانند ‪ -‬ک‬                                         ‫وبی‌حمیتی باشد ‪.‬‬
 ‫هم‌هست ‪ -‬و بمعنی بخت وطالم نیزگفته‌اند ‪-‬‬              ‫= بروزن‌نیشه‪ .‬تارهای ربمائی‬             ‫ربثه‬

                                                                       ‫‪.‬‬   ‫اس‬    ‫(‪ )۷‬چك ‪+ :‬‬

       ‫ی (مصدری) ‪.‬‬            ‫‪ - ۴‬از‪ :‬رشمال‬               ‫‪ - ۱‬لفة لحية فاضی (رش داور) ‪2‬‬

  ‫‪ - ۴‬پهلوی ‪( 2۵15۵۲‬مو) «اسشق ‪1۰٤٥‬ء‏ بازند ‪ 6051۲‬پ»ارسی رسکه ( بکر اول )‬
             ‫‪٩‬‏ رك ‪:‬آریغ ‪.‬‬       ‫‪ ۴‬اسم مفعول از «رشیدن» ‪.‬‬                    ‫ار‬
                                                                  ‫دنوالا ‪. ۵۲4‬‬
  ‫» رء‌فغوادمی وجالوری که‬      ‫ریخ («‪.‬م‪ ).‬است‬     ‫دیمع‬        ‫‪۲‬‬               ‫رك ‪ :‬راغ ‪.‬‬   ‫‪-‬‬    ‫‪۹‬‬

   ‫شمش روان بود و اهال داشته باشد و تواند خویشتن‌را نگهدارد ‪ -‬یلید ‪ .‬در کتابادی ربشوله‬
  ‫‪٩‬‏ ‪« -‬ازین تفسیر واضح میشودکه مؤلف ظاهراً‬                       ‫_زربكغ‪:‬ال ‪.‬‬                  ‫«کنابادی» ‪.‬‬
   ‫« ويك » (بفتح اول ) عربی را «ريك» خوانده و آبرا فارسی تصور کرده» «محمد قزوننی»‪ .‬موّلف‬
  ‫‪ -‬بعنی شن ارمی که از تفتت سنگریزه ها‬            ‫‪۶‬‬           ‫در آخر همین ماده باواو همتقل کرده ‪.‬‬

    ‫»ردی‬
       ‫حاصل شده * سنگریزه «ناظم الاطبا»‪ .‬وآن در استی ‪( 81۲‬کردوغبار) «ك ‪ .‬است ‪۲۳۱٩‬‏ ک‬
   ‫ةا و ‪ , 81۲‬افقانی ‪ * 8۵۲‬بلوچی ‪ ۵۲‬و ‪» 5۵۲‬یارسی باستان ‪ * 4612۲ -‬آمده‪ .‬رك ‪:‬اسشق‬
                              ‫و هوشمان ‪ ۲44.۰‬اشکاشمی ‪( 86۲‬رمل) «کربرسن ‪» ۲۹۰‬کیلکی ‪.811‬‬
```


## [2026-09-14T01:26:20.868Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"rāiti\\|räiti\\|arāiti\\|arāti\\|raēvant\\|raevant\" BRT.txt | head -20"
}
```


### [2026-09-14T01:26:20.922Z] TOOL RESULT

```
4153:künftige  (jenseitige)  Leben':  disyäl  aAmai naire  oval  mlzd>m  parS.asn3i  °fguhe  vazd- fary  vahistahe  omAsusV. p. 44;  ij.8,  Y.55. a,  A.3.7.  d)  s.  zu  A  1  d.  3)  mit  a) vaAista-  Adj.,  b)  acisla-  Adj.;  a)  'das  beste Sein,  Dasein,  Leben;  Ort  des  besten  Daseins, Paiadies':  vahisfym  'hüm  asaonam  raoca- wAbb  (Stverz.)  vIspB.ci^iJ^rjm'^.g.iii  usw.; S./.a?;  —  nöithl. .  bi-at. .  vaAi/tJ  '»Aus ySmanayat  ahurahe  masdä  oval  vispanqm *aastpm  (sd.)  .  .  yat  srrfoi  daoiarihum P.  40, ;  Y,  (to.  1 1 ;  —  as^m  yS  ahurS .  .  aoi urune  uri'äsma  (sd.)  dalsayeni  vakUtimca 'hüm  P.  3S;  V. /<?.  2  9 ;  —  vazdvar»  vahisiahe 'ai^is  V.  5. 44;  —  vahistajtSs>m  (sd.) TohUtahe  'riASusV.  1S.6;  —  tarS p^r^tümcit hl  urvänmt  vahisl^m  'ham  fraparaymi  .  . it  vahistät  'tihapt  Y.  if),6;  7;  —  i'lsp^m asmanpm  vahtst^m  3  °hüm  baraiti'S.24; V.7.S2,  '^f^. 3.1"^;— vahistahe  'vASu^ vahistqm  ayanqm  yazamatde  Vr.  7. 2 ;  — yatJrS  paurrd  usshistaiti  paräiti  vahistahe •w>i7»/V.;Ä26;5.6i,Y.7/.i6,YLy.i34. P. 4:9;  —  vahislai  •r^heYyi.33;  —  ia^ä 'uhSuS  vaAistahyS  paourvJm  ku%S  (sd.) Y.  44. 3.  b)  'das  schlechteste  Sein,  Da- sein, Leben;  Ort  des  schlechtesten  Seins, HöUe':  vTspa  humaia  ..  vaAistpm*°tAlim"'' *asaiti  vispa  dusmala  acisl^m  *'ijhüm"^ *asaüt  FrW.  3. 2 ;  — ya^ääl  anhat  apsniim (sd.)  '»Aus  aaslS  ärygt'atqm  at  asäum vakistim  manö  Y.30. 4 ;  —  avi  lim  spayüt. . t)mS  .  .  äca  aastpm  äla  'hüm  ä  V.J. 35;
4301:*asaya  *arpdusa  . .  nSiS  *°vis(i^  ästrydii vaHmaini  *asaya  (sd.)  x'a/na  vd  'vtsti astryeiti  N.  15.  2)  'Nichtlesen,  Nicht- vorlescn ,  Verweigerung  des  liturgischen Lesens':  yS  baoyö  (sd.)  aelahmSt  paräiti nöit pascalia  "Wistlm  ästryanti  (statt  Sing.) ". .  dann  macht  er  sich  durch  Verweige- rung des  (Liturgie-)  Lesens  nicht  sündig" N.4.
4818:—  weg':  viipim  a  ahmät  yat  ads  na  .  . haca  aHbyS  ttmUna^byS  . .  allristJ  pärayat yezica  .  .  hala  a^byS  nmanadbyd  tbists  . . paräiti  V.p. 39f;  13.  ij;  —  xsnata  para- yarüu  haca  ahmSJ  nmäiiät  Yt  l^.  1 5  7 ;  1 5  7 ;
4819:—  *%rigamim  aiwyast/lt  haca  *bamm?n paräiti  N.  Ä^.  c)  mit  avi  oder  paiti und  Akk.  oder  mit  Dat.  oder  mit  Gen.  'hin
4820:—  zu' :  xshms  asamqm  unänö  pärayeinii . .  avi  garS  nmänam  V.  75.32;  —  x3  patti apqm  paräiti  .  .  a^ra  . .  V.  jj.  51;  — xraosyS-taraca  (sd.)  .  .  hv5  urva  paräiti par3.asnäi  amihe  yaia  . .  V,  13. 8;  —  ya- tärö  paurvs  us>hiUaiti  paräiti  vahiltahe atshsus  y .  iS.^d.  2)  'aus  (dem  Haus) gehen  auf  — ,  zum  Zweck  der  Verrichtung von-'  (Akk.):  *kat!lmS  timänahe  a'iauru- fi9m{sd.)  pärayäf^''  N.  /;—  para  paoiryö äiti  (näml.  a^aururitm)  para  bityö  aiti para  "hrityS  äiti  aita  paräyaiti  ycc^a gae'^äbyS  *k)nti  "es  geht  der  erste  (auf Priesterdienst)  aus  . .  der  zweite  . .  der dritte.,;  es  gehen  die  weg,  die  (zum  Schutz) für  den  Hausstand  da'gelassen  worden) sind"  N, 2 (?)"'; — katärsm  *ä'irava  ctiauru- n>m  Vä  parayat  galiaiiqm  vä  asp^nns (sd.)  avat  N.^;  —  katärS  a'^aurun?rn ''parayat  nSirika  vä  nmätiSpaitiH  väi yezica  vä  ga^hä  vTmä  (sd.)  *katarascit ''parayat  N.  5;  *5";  —  *cvät  ''aiwtstXm parayap  'irixsapar>m  .  .  yS  haoys  (sd.)  . . paräiti  nsit  .  .  anaiwistim  (sd.)  ästryanti N.  4.  a)  mit  haca  und  Instr.:  cval  .  . äiirava  a'iaurumm  haca  ^gafi^äbis^para' yat  N,  4-  3)  'sich  an  etwas  (Akk.) machen':  yö  nar)m  ..  kasyat»he{%d.)  sanhai daoaili  vl^va  aval  hava  xraiwa  paräiti "—  wissentlich  mit  voller  Absicht  macht  er sich  daran— "V,  15- 2.  4)  'hingelangen zu  — '  sva.  'sich  verschaffen':  ffi.j(Akk.),. kaine-.tarS  äaxit^m  pärayät  tarS  ap»mca urvarqmfa  yezica  . .  tarS  (sd.)  daxst>m paräiti  . .  "nicht  soll  das  Mädchen  heim- lich sich  die  Regel  (wieder)  verschaffen, heimlich  sich  Wasser  und  Kraut  verschaf- fen .."  V.i5,9f.
5236:j.  ■''avi.nmin''  Adv.  'was  das  Mass  an- geht, an  Mass';  yavaf  also  caräitika  a' Aar^if  (sd.)  iar^/ayat  V. $.60;  61,
5338:•  j.  a-rätay-  i)  f.)  '(Nichtschenken,)  Geiz': vainit .  .  räitis  'rsiffm  Y,  60. 5.  z)  Adj. 'geizig;  Knicker':  paitUtatse  . .  'rälSisca fag^B.m»r»neyanaAe  Vty.  137.
6599:Kopula  hat  keinen  festen  Platz,  bevor- zugt aber  entschieden  die  Stelle  hinter dem  ersten  Hochton  ihres  Satzes,  und zwar  auch  im  Nebensatz.)'^':  ks  nar?  ahl yim  ..i  ..  az3m  ahmi..haomB  asava  \.g. I  f.;  12.  7  (wo  ahmt),  Yt.  7.  7  V,  11-15»', Ä15,  70.54',  74.3^  75.43-48S',  77.17, Az.  7,  Vyt  /;  —  azim  bä  is  ahmt  .  .  yä I  hava  dama  H.  2.  1 1 ;  —  srTrö  ahi  sara- .  'bus/ra  Auksntö  ahi  YL  77.  22;  10.  29', i  76',  79,  80,  72. 1,  Y.p.  25,  70.9',  6"2, 1,  V. '  iq.  6,  70,  VyL  22;  —  asU  (als  Vok.)  bfr?- zaiti  hmäta  ahi  huci^ra  YL;7. 15;  — hai^imifa  asahe  xä  ahi  Y.  70.4;  —  Hica (sd.)  caräiti}  ahi  yqm . .  H,2. 10;  —  yäha vasi  (sd.)  asäum  *ala  anhB  (sS.)  asava Y.77. 16;  —  avdha  izara>uslra)  *a»kä (iS.)'^'  spanya  V./Ä7;  —  a>a..AumäyH.- taraca  ..  atjhäma  Vr.  72.4;  —  mä  hyä>a (2p.)''>  duizaotärB  Vyt.  72;  —  aheca anhlus  yö  astvatS  yasia  asti  manahyä  Y. 57.25;  —  yatea  aAmäl  asti  mazyö  ..  tat tiB   däyala  Y.  (»5. 14;  14^;    —  yayä    asti
6796:g,  6,  2 1 ;  —  'ns  vairy3  fraoxts  H.  7. 4 ;  —  '  J-  'ahuimant-  Adj.  'der  emen  Aha  be- tam  paoiryd  zara>ustra 'npfn  vatrlm  fra-'^'^^'  stets  neben  ra/»;«^;,/.  (sd):  *"».a/'> irävayJvTb>r^>wa>,tfm{%^),lxtairJm{sA.)  ratumai  vaktnmi  vaocata  wzs  tin%n  Aha apar?tn  xraozdyehya  (sd.)  frasräiti  V.o.  "°°  ^"^"^  *""  '  "^^  "^°°'^t  das  beste" i4;V.in.2,YtiQ.8i;—panra  'na  vairya  P-'^'?)i  —  'mais  raiumatö  alaonö  asahe JrasravaySisW.n.z;    77.6,   7Ä43,  70.  zi;   '•■^^Sa-J  Vr.7.5J>;  —   'm^^m  rafummism
7920:•  j.  it,  g.  it  enkl.  Part  der  Hervorhebung; 1)  hinter  Rcl.:    eis/a    caräitis  ahi  yam  ii
8850:—  iäi/  (ab  NPn.)  he  afsman  .  .  käis pisträis  (als  NPn.)  Y.  19.  i6f.  2)  adjek- tivisch: kä  tim  ahyä  *maenis  (sd.)  anhat paouruye  Y.  44- 19;  —  i'f  ahmäi  aji/ )rmävi  I  Hl  ahmäi  jasal  äyaptim  Y.g.y, H.  f .  6 ;  —  /  Hsca  caräitis  ahi  yqm . .  "und(?) was  fiir  eine  Frau  bist  du,  die  . ."  H.  2. 10;  —  *kqm^'>  npmSi  zqm  ku^rä  n^mPi (sd.)  ayenl  V.  4''. ';  —  paiti  dim  p3r»sat zara'iuströ  .  .  kana  "iwam  yasna  yazäne kana  yasna  fräyazäne  . .  ?  äai  aoxta  andi'l ana  mqm  yasna  yazag^a  Vtj.gof.;  '5.54-', V,  ig.  1*7,  VyL  21;  —  ka  (IS.)  nä  vaca arhixha  Y.g.zs  PüZ.;  —  kake  vaca  vanäi . .  kana  zaya  .  .  ?  ana  vala  vanäni  . .  ana zaya ..  V.jp.Sf.;  —  k>m'^'^  *aem  at  ae'ira- paiiim  upayal  (sd.)  N.  12;  —  kaaham (GPf)  ">  nä  gä>:anam  .  .  ratu/ris  N. jy.  a)  im  gAw.  insbes.  NSm.  mit  dem enkl.  NS.  nä  (s.  nar-)  sva.  'wer?';  kasnä .-^Sng..  dJt  advämm  (sd.)  Y.44.3;  3.4*;
9742:—  yavanqm  .  .  västranqm  .  .  '•%anqmca  Wesen  und  Dingen  zum  (Reich  des)  Asa, ashaiiinqm  YtÄ29;  usw.;  —  s.  noch  zur  stofflichen,  sichtbaren  Welt  des  Asa Anhang  «.  2)  'Wesen'  im  Sinn  von  gehört':  'irj^räi  asake  °'^anqm  "um  zu 'Anwesen';  'Gehöft,  Haus  und  Hofs>,  schirmen  alles,  was  zum  Asa  gehört"  Vt. Hausstand  (ramilia)',  überhaupt  'Hab  und  /p.  48;  Y. 55.  3^  57.  17;  —  makrkai  alahe Gut' (im  Gegensatz  zu /<2ns-,/fl«a/-), 'weit-  '>anqm  Yt. /<).  50,  Y.(?.  8;  <?.  3,  V. /Ä  sSi lieber  Besitz*  (im  Gegensatz  zu  ankav-  —  asiby5  yli  urvätäiS  drRjS  asahyä  '^ii I  2);  Sing,  und  Plur.i  yi  .  .  varidayoSä  vTtn?r?ncaiti  (sd.)  Y.31.  1;  —  ^un  ''^ä yqm  nasdi/tqnt  '^qm  dr»^a  iax/ai ff.. (sd.)  amar/antis  ya  ahhe  Yt,  sf).  la;  — drufim ^■5'>-Z'>  — yä^a  ■  ■  v?hrkqm  azr5.dai)tTm\iti~barat  asahe  haca  ''iabyS  Yt.  ig.  93;  — fsd.)  -iaw  avi  frafiaiaiti'y.  18. 6 $'•'>■,  N.  —  s.  noch  Vt.  6'.  i  (unter  z).  a)  auch 3'Q);  —  spämm  dd^tm  ..''i^anqm  Aar»-  mA  astvanh  Adj.:  ktmat  atiAsus  astvatS ^räi  V./y.39";  — yesi  narü  ..  kafa  aoi  .  .  '''^abyö  *  astvaitibyS^^  asake  ^.13; ''iäbyS  pain.iri>:yeiii  Vd.  13;  —  cval  ns  —  gandartwim  , .  y3  apatat . .  m»r»xlam ä^rata  (sd.)  a>aurun?m  haca  *'%äbu^'>  °^J  astvaifiS  alake -Hx.  iQ.  i,\ ;  V./iV.  55, *parayät  N.  4;  —  yS  ^yujyasfim  //a.ft  .  SrB.j;  —  dar7sca(sd^  ddisat'^amfrixsyan- '"iabyd  paräiti    V.  13.  17**;    —  yas)  tat  tim  vTspqm  yqm  astvaiHm  gai'iqm  Yt.ig.
10137:ainanAaiti  nS  maus  Y.p.ap;  —  'Jus' pa/räiti(%A.)'W.4.^Z;  —  däitjm 'Sul draotUS vansS  Vd.16;  3,  fi,  N.36';  —  °Sus  mau- 1  N02;  5j;  —  %w3hin  ä  Sus  frOäsWinsB mana  (Stverz.)  V.  *.  36;  usw.;  —  gaomag-  j .  ,  haomai  äraond  Y,  //.  7;  —  yimasäi  . . z^m  (sd.)  'ava  (IS.)   dalaya   V.  ig.  32Q);\y3  masying  axsnusJ  ahmäkJtig  '3üs(GS.)
10610:4.45;  4S;  —  aslm  .  .  ya  vTspanqm  . syantqm  /rasa  °'hwa  frdhanjayeiti  Yt i-j.t*''i;  —  mit  ^äsna-  (sd.)  und  gaosS.- srBta-  (sd.):  ätmm  'tum  .  .  gaosS.srai>m 'tum  Y.  25.6;  —  äsnahe  ''hwä  .  .  gaosi\- srotahe  ''%wS  Y.  22.25;  —  "'"^  ^^  äsnim 'tum    ava.baräiti    varsma   (sd.)   Yt/7-2;
11225:•  j,  iaräiti- £ 'jungeFrau"^  uzw.  aÄwnscher Schöpfung:  'räiH  (NS.)  huraolaya  darr^a apuhra  aäti  V.J.  24;  —  %wqm  (näml. arpdvlm)  kainitiS  .  .  ja^iyhnte  .  .  nmänö.- faiilm  'hwam  'räitis  (NP.)  zhanäitis  Jail- yiinte  hutämJm  Ytj.S?;  —  äsca  'räitis (NS-)  ahi  yqm  il  yava  'räitinqm  k?hrpa sraistqm  dadar?sa  H.  2, 10.
11227:•  j.  ^aräiti'ka-  f.  'junge  Frau,  Frau' :  yavai 'ia  *avi.inatn  hariks  hancayJt  V.5.60.
12027:xraosyB.taraca  (sd.)  «?  ahitiat..  hv5  urva paräiti  parll.asnäi  anuhe  ya^a  vikrkd  va- yui  (sd.)  taile  (3SPM.)  *dramna  banzilte razBire  (sd.)  V.  y.  S.
12880:—  ')  S  411-  3  d. •  p.  darga-,  g.  daraga-,  j.  dar«}-a-  Adj. (fem.  °7J-)  'lang';  i)  räumlich:  Ufa  tarn car^am  yqm  'yqm  YtJp.  77;  5.50;  — mi^rtm  . .  yeAha  'yäat  bäeava  .  .  Yt.  10. 104.  z)  zeitlich:  M<?i«(sd.)  tat  äs  nsit 'y?m  Yt.5. 65;  —  "iimal  aipi  zrvätum Y.62.3,\tig.a6;  13.53;  —  °f^^  ^yo (sd.)  t^mattks  Y.31. 20;  —  'yayäsca  paiti danyjjltdis  YL  /y.  1 3  j ;  Y.68.11;  —  tsm (nämL  kämtm)  msi  data  'gahys  *yaos{^^^ vairyS  stSis  Y.  43.  13;  —  hyatcä  -gSm *Jr3gvö.d»dyS  rasö  {sd.)  Y.jo.ii; — ptn- fum/a  (sd.)  barjsma  starane  °y?mca  yasram ..yaaJnS'Vt.iO.iiSi—ya^a  Sicä  *aiivi- iayama  'ya  amiiayana  . .  hr^yrnya^^aSum (sd.)  Yt  70.  7  7 ;  —  °gäi  Tsyai  bfzvait!  hax- maim  (sd.)  Y.  40.  3;  —  'yai  hax^räi  Vt 10.  T),  17.6;  — fravaiayS . .  hulhaxmanS . .  'yaa'fyj  Aax^oralifyff  Vt  13.  30;  —  'y^m Aaxma  V.  60.  j;  —  dättm  tS tanuye  :^ar»nB ' urvnaläi  •y?m  havanfum  (sd.)  Yt77.  22; F.^b;  —  urunaica  'ye  havanhe  A.  i.ii; —  'yäi  AaosravaAAsi  .  .  -yai  AavafiAäi Vjtjs;  —  a  'yät  ^ä.bairyilt  (sd.)  Y. öo.  6;  —  'yqfi  upayanayä  (Stverz.)  Y, /.  13  usw.;  —  'ya  (APn.)  data  .  .  sara- >uäraAe  T.  ^6  {?);  —  iaia  tl  'yim  ävSya (sd.)  aakal  H.2. 34;  16.  a)  Adj.  an Stelle  unsres  Adv.'':  :^afsa  'yd  tna^äka "schlaf  lang,  o  Mensch"  V.  rÄ  16;  — earäiti  .  .  yä  'ya  apu%ra  aHti  V.  3.  34; 34.  b)  ASn.  als  Adv.:  H  utä,  'gam  jlvä
12944:'zu  Gesicht  bekommen,  erbUcken,  er- schauen': caräitii  .  .  yqm  it  yava  carSiti- aqm  hhrpa  sraiitqm  dädansa  ". ,  das  an Gestalt  schönste  von  den  Mädchen,  d^s ich  je  zu  Gesicht  bekommen  habe"  H. 2.10;  Y.5.  i;  —  ttla  kal  %ws  dansäni matuuca  vokü  vaidfmnS  "o  A.,  werde  ich dich  erschauen  und  den  VM.  als  ein wissender"  Y.  2Ä5";  —  a/a  vahisia  .. darjsäma  %W3  pairi  %WS  jamyama hanam  %wa  Aaxma  (sd.)  Y.  60.  la";  — kumqsdrä  (sd.)  asä  yecä  yä  raocübls  dan- jflöljSKM.)  urvasa^.30.\.-,  —  dar?sat'^ F.  i4;  —  darsstä.'.  a)  vom  visionären Erschauen:  hyaf  hufä  aipAsui  zaiiSi  dan- sjm  paourvim  "als  ich  dich  zuerst  er- schaute bei   der  Schaffung   des  Lebens"
14447:•  j.  Jhvyi-  f.  'Schrecknis,  Gefahr";  avi dli  aim  . .  aihim  baräiti  "yqmÜa  Yt  10. 37 ; —  tum  .  .  ma^anam  avi  3^alpaihy/lsf tanvS  'yam  avaiaraht  Vt  10.  sj.
```


## [2026-09-14T01:26:21.861Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"raēša\\|raesa-\\|raēšah\\|raeš\" BRT.txt | head -20"
}
```


### [2026-09-14T01:26:21.918Z] TOOL RESULT

```
5472:*)  Im  Gegensati  lu  i^ara-,  /raiäbaiitaA-  jnaXa-, sowie  tu  raesa-,  sd.  Vgl.  die  Definitionen  F.  sjb : ia  pa  vinäskärTh  sniA  afar  mnäskär  nidakel  aräitl näm  und  bei  Dsr.  ZA.  2.  .54:  .  .  tHa  iaslram yalnalayä  Sarire  evam  äadää  yatka  na  pikant  ia-
21503:•  j.  yah-  V.  'sieden'  (intrans.).  Praes.  6 jraesa-'\  2^  jyagsya-.  —  FP[P.  yaäa-i?)».
24803:"  J,  'raesa-  m.,  raesah-  n.  'Schädigung'; A)  körperliche  Schädigung  überhaupt; a)  in  Bezug  auf  den  Fötus;  yeHi^a  . .  kaine . .  3^atö  garnuim  irisyeiti  .  .  ptinbyS  (sd.) irisintqtn  ralli  Hkain  baoiiS.varltahe  ci- %aya  V.  75. 1 3.  b)  in  Bezug  auf  Hunde: yS  süne  piilrtm  jainti  ..  us  va  hl  gaohm 'hwirisaiti  apa  va  ks  pathyqm  kintUaiti . .  cikayat  sBnahe  °l5  (ASn.)  baob5.varHahe üfhaya  V.ij.io;  'Vyt.44;  —  ym..spiina ahaiiyS.at»/iar3^r>m  (sd.J  irisyqn  para  as- iqm  iriHntqm  'h  cikaen  baoZs.var^iahe Hhaya   V,  75.  22,  40.  2)  Rechtsaus-
```


## [2026-09-14T01:26:35.043Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"j\\.  *rätay\\|rätay-\\|ratay-\\|'rätay\\|raevafit\\|raēvaṇt\\|raivant\\|'rä-  *V\\|j\\.  *rä-\" BRT.txt | head -20; echo \"=== search Freigebigkeit\"; grep -n \"Freigebigkeit\\|freigebig\\|'geben'\" BRT.txt | head -20"
}
```


### [2026-09-14T01:26:35.131Z] TOOL RESULT

```
3877:•  j.  aiiwi.varatay-  i.  'Sichdarüberwälzen, Darüber  wogen':  fiasca  ä^rittm  'railt "nachdem  die  Wellen  dreimal  darüber gegangen  sind"  V.6'.4J.
4067:•  j.  a-fraratay- f. 'Gewährung'":  misäahe 'raiti  VyLjO,
4482:•  j,  a-inizbaratay-  f.  'das  Nichtweg-, forttragen':   nizhnla  (sd.)   nSit   Ua  (LS.)
5338:•  j.  a-rätay-  i)  f.)  '(Nichtschenken,)  Geiz': vainit .  .  räitis  'rsiffm  Y,  60. 5.  z)  Adj. 'geizig;  Knicker':  paitUtatse  . .  'rälSisca fag^B.m»r»neyanaAe  Vty.  137.
5654:■arätay-
5655:•  i-,  p,   'arätay-  f;  m."  'Speer,  Lanze': yaäam  zayanqm   raitöiiti  paoiryS  °iis  V. 14.^;    —    'tayasiä    karitayasca    '^.fj —  •//'/  ki-aiwyästa  Yt  13.  7 ; •tSis  huxsnutaya  Yt  10.  24;  —  'tayasat
7291:•  j.  ä-paratay-  f.  'Ausgleich,  Sühne'  einer  I Übelthat,  usw.  durch  Leibesstrafe'*:  ka  hs asti  fi>a  (sd.)  iä  he  asti  °tis  ka^  he  asti yaeidainm  V.J.38;  39,  Ä107,  /.V-ÖS.
7646:•  j.  aratay-  f.  (etwa)  "Energie':  amavata amäi  .  .  vanürayuäi  amavai'iya  gr^i^ya (GS,)  . .  a/Ä/. .  Sstöi^'  Vr.  5.4,  A)  als Gottheit:  assis  vatthuyä  ästöis  vauAuyä "ara^P  (als  Gen,)''  vanhuyh  rasastiVö vatihuyä  Y,/.i4.
7902:sehr,  tarn':    m3   tl  (nämL  kaomahe)    nJre (sd.)    .  .    '"isa    raivanto    ar»jahe    Y,  10. '7-         3)  'ebenso,  gleicher  Weise,  item', mit  Ellipse  des  Verbums^:  vasS /raxitäiteisA.)  aiwi.gäme  '^a  hama Winter;  ebenso  (kann  er  es  tun)  im  Som-
8277:•  j,  upa.9TVarätay-  f.  'Anschneiden  sva. Durchstechen  des  Grabendamms,  Damm- durchstich': yaval  ai^a  ä/s  byärixti  (sd.) 'ti  {VA.)  frabavät  ^.14.1$.
10346:•  j.  glmö.baratay-  f.  'das  Machen  eines Schrittes"': /ar.-'ffl  tüirlm  (sd.)  'nitJm  V.
12279:•  j.  tizLarätay-,  'ti2y-arätay-'>  Adj.  'mit spitzem  Speer  versehen':  mihrym  . .  °tlm Yt.10.  loa;  —  taxmpm  staotarim  . .  'Um äarTja-ärstaltn  YtJ?.  12;  —  "h"^  nqma ahmt  'lis  nama  ahmi  Yt  /J.  48.
12309:>  j    'tiiy-arätay- Adj.:  s.  unter  ft«.a».  [dem  ersten  Wort  des  Satzes»,  uzw.  i)hmter VgL  ^liiyaritay-  EN.  :  ai:  hyatcä  .  .  ai  ta  mSi  rtsil  asrusta  (sd.)
14277:•  j.  B-anvaratay-  f.  'Bogen',  als  Waffe zumSchiessen:  ^as(X/7r7M  'rfiiinqm  huktn- tanqtn  Yt /o.  128".
14413:mit  upa    und  nf  'ausstechend  graben':      KompE. paoinm   upa   maytm   Kt^w^nssi/  .  .  dva  ,   j,    ^Tvarätay-    f.    r)    'Schneiden'    (nur »risu  nUmahe  (sd.)  V.5.6.  Komp.).  2)    'Bilden,    Schaffen':   para
14536:•  j.  ^ratay-  f.   'Schirm,   Schutz':   dayi tm..ätu  'äitim . . peuru  °3itlm  Y.6'2.4'',
15840:•  j,  'parätay-  f..  Du."  'Rücken':  'ti (AD.)  he  .  .  assa  drux^  .  .  upaJvqsaiti S.S.  51;  52,  g.  18,  19.         [Yt.14.  56:  lies
16107:•  j.  'pBraÄT/arätay-  m.  EN.  emes  Gläu-
17517:•  j,  fraoratay-  f.  'Sichbekennen   zu  — '
18264:•  j.  frä-rätay-  f.  'Freigebigkeit,  Mildtätig- keit', nur  in  Verbindung  mit  vTdlsä-  (sA): tä  nS..°räiti  tä  vldlse  uzjamyqn yS  staota yesnya  Y.55. 3;  —  hSc3  tiH  fsBmh  .. aiwyäxlayatü  kadä  asä/ä  vilsträ/ä  °rä- Hca  vldlSayücä  ainiUca  ..  Y.5Ä4;  — 'räitfi'a  *vTälsasM  antar?  *3^aäalnsi^ asaonis  P.  jff ;  —  in  Dual  Verbindung:  °räili ■i'ldfh  yazamaide  yat  asli  atitar?  :^ädal- nais  asaotiTl  Vr.  21.  3  •' ;  —  °räili  *vldXs€ (?)'>  ainitii  ags's  *växsf  f.  26.
=== search Freigebigkeit
13243:yalt;  ksl.  dayelü;  ai.  adüsi;  dadkniha,  dadki; mp. .iW 3S.  1*),  ilakfl;  dal;  v^.dihad,  niAad*i), Jäd.  S.  noch  No.  33.  —  Die  einander  enl- Eprecbendeo  Formen  aus  »r.  'di-  'geben'  und *dhä-  'seilen'  sind  im  Unran.  lantgesetzlich lu  lammen  gefallen,  mit  alleiniger  Ansnabnie derer,  bei  denen  der  Warielkonslinant  vor einen  lon'oien  Geräuschlaut  zu  stehen  kam; %  53  ^-t  1^1  345^-  ~~  Wegen  des  neben  dai- auftretenden  u'aS-  s,  S  t26  No.  —  Pü.:  dälan; s,  noch  No,  4,  »4,  27,  30-39,  41  f.,  44-  — '\  Vor  dem  y  des  Opt.,  mit  a  au^  uridg.  /, %  6g.  2  No.  3.  —  ')  Y.  6fi.  1,  vgl.  No.  23.  - 1»  Y,  j/.  I,  vgl.  No.  41.  —   4)  Vorher  geht
18264:•  j.  frä-rätay-  f.  'Freigebigkeit,  Mildtätig- keit', nur  in  Verbindung  mit  vTdlsä-  (sA): tä  nS..°räiti  tä  vldlse  uzjamyqn yS  staota yesnya  Y.55. 3;  —  hSc3  tiH  fsBmh  .. aiwyäxlayatü  kadä  asä/ä  vilsträ/ä  °rä- Hca  vldlSayücä  ainiUca  ..  Y.5Ä4;  — 'räitfi'a  *vTälsasM  antar?  *3^aäalnsi^ asaonis  P.  jff ;  —  in  Dual  Verbindung:  °räili ■i'ldfh  yazamaide  yat  asli  atitar?  :^ädal- nais  asaotiTl  Vr.  21.  3  •' ;  —  °räili  *vldXs€ (?)'>  ainitii  ags's  *växsf  f.  26.
18265:*)  Freigebigkeit  gegenüber  Religionsgenossen wird  oft  genug  eingeschärft;  vgl.  iB.  unter 'dS%ra-,  dagegen  halte  man  F.  50  unter  itaod-.
24089:•  j.  vi-di5ä-  f  'Freigebigkeit,  Mildtätig- keit', nur  in  Verbindung  TD\i/raraiay-{sA.)i ta  nS  .  .  fräraiti  ta  °ie  (IS.) ''  usjamyan ya  staoia  yesnya  Y.55. 3;  —  hScS  na f^ma  ni/ai^haratB  ..hada  asala  vasträcä frarätua  'sayli{l%.)ca  ainiHca^.^S.«,;  — fraraülsca  *'sasca  antar»  *^adalnais  asa&- nl^  P.36;  • —  in  Dual  Verbindung  damit: frarSiti  °se  (AD.)  yasamaide  yat  asti  an- tars  :^adamai?  asaonsi  Vr.  21.  y,  —  frä- raiti *°se''>  ainitis  agl'o  *vaxsT.26.
25301:•  i^  g.  'rätay- :  raiti-  i)  Adj.  'dienstwillig;  \ Diener,  Gehilfe' :  mßiryin .  .yaihe  aita  *tayB  l ..  spass  ätfhsire  Yt  10.  45.  i)  f.  'Dienst, Dienstwilligkeitj  Pflichterfüllung':  aAurit  na na  avarS  (sd.)  shmä  (3p.  270  o.)  °töis. yüsmävalqm  ".  .:  so  wollen  wir  bereit sein  euresgleichen  zu  dienen"  Y.  2g. ' 11".  a)  bes.  in  religiöser  Hinsicht:  avis\ nä  antan  hSntü  mmaifaitji  ctärä  '/ayS' "oflfenkundig  sollen  unter  uns  werden  die deutlichen  ehrerbietigen  Pflichterfüllungen" ^•33-  7")  *'*•  P- J^  ™''  der  Ausführung:  [ tä  ävifj'ä  °tayg^^  antar?  *afm^sca  sp?nts iaoiyantas^a  fräräUllca  *vldlsäs(sd.)ca arttan  *^3dainäif  asaonis  "die  sollen offenkundig  werden  die  Pflichterfdllungen zwischen  den  ASp.  und  den  Sao^y.  und , die  Freigebigkeit  und  Mildtätigkeit  zwischen  I den  rechtgläubigen  Retigionsgenossen"  P. ^■,  — yäti  catica  . .  dahmS  aiava  *kaurvh *'itl^''''  dähaj  a0i  dim  aiwyäiH  yä dahma  vatshi  äfritis  "so  oft  ein  recht- gläubiger Gemeinder  seine  religiösen  Pflich- ten völlig  erfüllt,  .  ."  P.ja.
25303:•  j.,  g.  ^rätay-  :  rSiti-  £  1)  'Gabe,  Ge- wälming':  'itf  ..kyat(%'^.  1315  m.)  mlidim *mavai^fm  (sd.)  /radadaha  daZnäbyd  Y. 40. 1 ;  —  tim  haiai  oHi  'ifi  . .  mafyäi yi.  18.  ^{7);  —  Aumrum  'ifi  bartila  FrW. g.  2  (?);  —  ku%ra  tä/ryS  Äawa«(näml,  aot.- büta)  .  .  iä  iütdä  .  .  tä  'tayB  *yam  ahurs mazdä  tara%usträi  /rävavaca  "werden  die Gebete  erfüllt  werden  . .  die  Schuldforde- rungen ■ .  ihre  Gewährungen,  die  . ."  V. 65. 9-  a)  insbes.  'Opfergabe,  -spende': avä  (näml,  vao^amä)  vS  vatmhls  •tsil dangsMasäu!  (sd.)  näla  . .  paitijJndä  Y. 38,$.  a)  'Freigebigkeif:  vainlt  ahmi nmäne  . .  °itii  araiffm  "überwinden  soll  in diesem  Haus  die  Freigebigkeit  die  Karg- heit" Y,  60.  5.         IS.  räitf  als  Inf.  sbes.
25321:Freigebigkeit  (Vj/(J>-)  geschieht"  (?):  aBai^a va^  mazdaoxtim  %ri.afsmfm  cä^rv.pistnm panca.ratu  '"him  Y.  ip.'iö,
```


## [2026-09-14T01:26:47.688Z] TOOL CALL #37: Bash

```json
{
 "command": "ls site/pages/419.jpg 2>/dev/null; pdftoppm -f 419 -l 419 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg419 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg419.png"
}
```


## [2026-09-14T01:26:48.972Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=546 && NR<=552 {print \"----LEAF \" NR-1; print substr($0,1,600)}' IEC.txt"
}
```


### [2026-09-14T01:26:49.549Z] TOOL RESULT

```
site/pages/419.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 79366 Sep 13 21:26 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg419.png
```


### [2026-09-14T01:26:50.623Z] TOOL RESULT

```
----LEAF 545
adj. ‘the same"; cf. ten-pàt ‘right there’; Latv. pats, pati, prn. ‘self; pat, adv. ‘even’ |
pot-, (2) o-gde radical of type pet- (1) “fly, fall Gk. cf. potáomai, v. “fly, hover’; poté, f. (1) flight’ beside pótema, n. id.; potaánós, adj. ‘winged’; Li. pátinas, m. ‘winged creature"
poteio (potiio) “possess; dominate’. Cf. potis Skt. patye, m. & patiyami, v. “be lord”; Av. cf. háàm-paiOy(eimi), v. ‘possess’; cf. also pai- 0imnó ‘being in possession’; Arm. unim, v. ‘have’; Alb. pata, aor. Leg beside patshé ʻI had”; me pasé, inf. ‘to 
----LEAF 546
g, cover’. WP IT, 72 Skt. patram, n. (1) “holder”; radical in Gk. pó- ma, n. ‘lik’; Go. fodr, n. ‘sheath’; OHG fuotar, n. ‘sheath, lining; OE foóor, foóer, n. (1) ‘case, cover’; ON fóór-, in a cpd. “lining”; Sw. foder, n. (2), id. (Isophonic: MHG vuoder, sn. ‘load’: E fother (of hay))
pot-siét Alb. -fté in opt. 3s constructions, also in ndo- fta, ndo-shta “perhaps”, fr. *an-dei-pot-siet, reduced to *-siot; Lat. possit; W osyd “if it be
pous- (phous-) ‘down, fluff, hair’. Cf. paus-, pauslos, pau-uid-, etc. Lat. cf. pü-bes, gs: -beris, adj. ‘adoles
----LEAF 547
t, former; W rhwys, m. ‘vigour, excess; MHG vrist, sm. f. n. “delay, time-limit, interval; cf. vristen, v. *postpone, delay, reserve, protract, preserve, protect
préio “fire, heat. WP II, 27 Gk. cf. pímprémi, fut: préso, inf. pimpránai, v. ‘kindle’; R pr&ju, prét, po-, v. ‘stew, sweat’; so-prěť & -prévat, v. "Tester": Ukr. prity, inf. *sweat
985
prek- “offer, sale, goods’ Lat. cf. precius, adj. *well-advanced, thriving’; Olr. recc, Ir. reic, m. “selling; sale’; reccaim, reacaim, v. ‘sel; W rheg, pl. Jon f. ‘gift’; Li. préke, f. “goods? (archaic: *price
----LEAF 548
losami, v. (2) ‘sprinkle, anoint; (z-gde in) prusnómi, id.; (long z-gde in) Cz. prys- kati, inf. ‘spray, squirt’; (o-gde in) Li. prausiü, ti, v. ‘wash, bathe’
preuto (preutso, phreut-) ‘snort, blow, spray”. WP II, 28 Skt. prothami, v. id.; Av. frao0-, v. id.; OE à- fréopan, v. ‘foam at mouth"; (z-gde in) E froth, s. & v.; ON cf. (o-gde) frauó, n. beside (z- gde) froóa, f. id.
proi, see pri and cf. pri-
proidos, is (prid-) “offer, addition, subven- tion’. Cf. pri, do- i Lat. praes, gs: praedis, m. ‘security, bail’; Srb. prid, m. ‘use, benefit’; priden, adj. “
----LEAF 549
 prí-, q.v.) Lat. cf. pri-die ‘the day before’; pri-dem *re- cently' beside OLat. pri (Lat. prae); Li. pri- (verbal prefix) beside OCS (and com. S1.) pri-, id.
priia- (priia-, priio-) *dear-. Element of the following cpds. WP II, 86 Skt. cf. priyáh, f: priya, adj. “beloved'; mf. friend" (f. also: ‘mistress, wife"); OHG Fria, v. ‘goddess Fria’; ON Frigg, sf. id.; OS fri, f. ja- st. woman’; OLE frige, fpl. “love?
priiã-ĝen-, -gent-, -$n- ‘kinsman; beloved’. Cf. (variant) prəi-ĝen-, pri-2ən- W rhian, pl. -edd, -ed & rhiain, also rhiant, pi. rhiaint ‘parent’; rhieni,
----LEAF 550
, cf. pro-, ago Per. far-àz, adj. *exalted"; far-azam, v. ‘erect’; Oss. (Graz, s. ‘means, facility’; fárazun, inf. ‘be able’; Arm. ar-ac, i-st. s. “proverb, precept’; Gk. prágos, n. “deed, act; Alb. prodh, m. ‘boon’; prodhë, f. ‘produce, product"; OHG fruohhan, adj. ‘bold’; OS cf. frokno *boldly'; ON froekn, adj. ‘bold’; OCS prazü, m. "breed. ing male animal” beside prozü, prp. ‘through’. Verbal types (pro-ag0, pro0, etc.) cf. Skt. pra- ajakah, m. ‘carter’; Av. paraze(imi), v. “bring along”; Per. farazam ‘erect’; Arm. ar-acem, v. ‘tend 
----LEAF 551
í, proj, adv. “early'; próios, adj. id.; EMAIb. prej, prp. ‘towards’; MIr. ré, prp. id.; MHG vrüe, vruo, vrüeje, adv. *early'. Variant in Greek próén, Doric próàn, adv. “formerly, of late’; Latv. projām “forth, away’. Cf. also Gk. proimos, adj. of early morning” and Latv. prom “forth?
prok- “forth, forward; later, late; advance. Celtic variant: prok-, Skt. prók- Skt. prak, prak-, id.; Av. fraca, id.; Gk. próka ‘forthwith, suddenly’; Lat. cf. re-ci-procus, adj. back-and-forth’, if for *re-que-proc-); (R- gde in) Ir. rag-, px. “late-?; W rhag, prp. *be- fo
```


## [2026-09-14T01:27:03.155Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"rēza\\|reza, \\|riza\\b\\|rēzah\\|rizeh\" IEC.txt | head -20; echo \"=== reik/reig entries\"; grep -n \"^reik-\\|^reiĝ-\\|^reig-\\|^reiso\\|^reik\" IEC.txt | head -20"
}
```


### [2026-09-14T01:27:03.223Z] TOOL RESULT

```
1703:bhrüg- (2) ‘tremble’ Illyr. in Lat. briza *quaking-grass'; OE broc- cian ‘tremble’; Pol. bryze *yellowrattle'
14463:reig- (roig-) “break, (Gar breach, téar, cut; piece, fragment Per. (e- or o-grade) rize ‘fragment’; Ir. ria- ghaim, v. 'téar; crucify’; Go. cf. (?) bi-reikei, f. ‘danger’; OCS riza, f. ‘garment, cloak’; R riza ‘chasuble’; Latv. riezis “baulk, boundary, ploughing-strip’; rieze, f. (time, occasion’. Se- mantics of OCS razü ‘time’, cf. Gk. rhōx and rhogás ‘cut, têar’, see urõĝ-); o-gde in Li. rai- žau, -yti, v. ‘cut, score”
15891:skridh- (zero-gde of type skreidh-, q. v.) Br. cf. skriza, Cor. scryja, v. ‘tremble’; OE scrid, adj. (swift. But cf. skritós and the pa- rallel type skreit- above); ON skriór, m. ‘glide, slip’; skriða, f. landslip'; skrióna, v. ‘slip’; Li. cf. skrydis, gs: -dZio, m. flight; skristi, pf. skridau, v. “fly?
=== reik/reig entries
14463:reig- (roig-) “break, (Gar breach, téar, cut; piece, fragment Per. (e- or o-grade) rize ‘fragment’; Ir. ria- ghaim, v. 'téar; crucify’; Go. cf. (?) bi-reikei, f. ‘danger’; OCS riza, f. ‘garment, cloak’; R riza ‘chasuble’; Latv. riezis “baulk, boundary, ploughing-strip’; rieze, f. (time, occasion’. Se- mantics of OCS razü ‘time’, cf. Gk. rhōx and rhogás ‘cut, têar’, see urõĝ-); o-gde in Li. rai- žau, -yti, v. ‘cut, score”
14464:reiko, ið ‘têar, break, cut’. WP II, 344. See next Av. cf. iriC-, v. ‘break out; — paiti “attack, destroy’; Gk. ereíko, v. “break, téar, slit, shat- ter; OW (denom.) rwygaw, W rhwygo, id.; MHG rihen, sv. 1. ‘stab’; Li. riekiù, ^ti, v. ‘slice’; ON cf. rista, rísta, f. ‘cut; ristill, m. *plowshare'
14465:reikos, à, io 'téar, cut, rupture’. WP II, 344. See reikó
14476:reiksó, ið (reiksKo) "lay, spread, extend, reach’ Alb. rresh, v. ‘superimpose; fall — of snow or rain; W rhwych, f. “extent, extension’; Li. riešu, “ti, v. (2) ‘spread; stretch (yarn) on loom’. (Isophone: Li. reiškiu, reikšti, “explain, express, publish’)
14478:reiso, ið ‘snatch; ravish; burst, split’. WP I, 140. Av. raeš- ‘wound’; Skt. resámi, risyami, v. (2) "injure; OE risan, sv. 1. (3) ‘seize, ravish’; Latv. riešu, riesti, intr. "burst, split; spread”. (Isophone: Go. ur-reisan)
```


## [2026-09-14T01:27:23.147Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR<=14463{n+=gsub(/\\f/,\"\")} END{print \"leaf index (0-based) of line 14463:\", n}' IEC.txt; awk -v n=14463 'BEGIN{RS=\"\\f\"} {c++; if (NR==587) print}' /dev/null 2>/dev/null; echo \"---- print surrounding leaf\"; awk 'BEGIN{RS=\"\\f\"} NR==588' IEC.txt | head -60"
}
```


### [2026-09-14T01:27:24.246Z] TOOL RESULT

```
leaf index (0-based) of line 14463: 591
---- print surrounding leaf
 *dapple, speckled’; Oss. áxsid, Dig. àxsed (cred Of sky)
qusoitos (2) ‘rollicking, raving, mad (?) Per. Saida ‘maď’; Oss. cf. áxsidán, v. ‘boil, seethe’; (Gk. phoitos, adj. ‘raving, roving’ is tentatively derived fr. *guhoit- by Bois. & others)
(qusoio? qusuiə? See Supt:Qu)
qusoio (grate, abrade, gnaw, destroy’. Cf. qusëið (1). (Per. ambig.) Per. xàyam, v. ‘chew, gnaw’; Gk. psóo, v. ‘wear down, crush’; cf. psomós, m. ‘crumb, morse?’; ON sóa, v. (pp: sóó E sóinn), v. ‘destroy’; Raat, inf. “blame, criticise’; (OCS cf. xa-ba,
qusoidhos — qusür-
10
20
25
30
35
40
45
1060
f. “harm, offence’; xa-biti, inf. ‘corrupt’; xa- ben, adj. ‘wretched’, Srb. cf. há-biti, inf. de: stroy’ but cf. qusàbh- for an alternative read- ing)
qusolos (?) ‘rogue, lad” Skt. khálah, m. ‘rogue’; Cz. pa-cholek, dim. *farm-boy'; pa-chole, n. dim. ‘lad’; Ukr. pa- xolok, m. id.
qusõros ‘rough, gritty; gravel, scab, mange’. (Indo-Iran. ambig. cf. ksēr-) Skt. khárah “rough; Per. xāriš, xware "ich, mange’; xaram, v. ‘itch, scratch’; Oss. cf. (z- gde) xür, Dig. xurä ‘gravel, rubble’; Gk. pso- rós, adj. “rough, uneven; scabby’; psóra, f. ‘scab, itch’; Cz. charý ‘shabby, dingy’; Big. cf. xáro ‘rascal; ill-luck’; Li. šuoras, m. ‘scratch, line, groove, stripe; outburst, rage’; Ukr. cf. xaryty, inf. ‘clean’
qusoud-, cf. quseud-. Only in Hes. psoudía, f. ( ‘deceit’. Hes. Cretan); (iso- phonic) OCS xuzdo, xuditi, v. “blame, ac- cuse'
qusoudhos ‘puny’. Cf. qusudros & ksud-. (Phonology indeterminate in some instances) Skt. cf. ksódhukah, adj. dim. type “hungry”; Av. šud-, v. ‘hunger’ beside Suðo, m. id. (both z-gde); cf. Gk. (?) psüthos, n. (ffalsehood". Infl. of type quseud-, q. v.); ON sauór, pl. sau- ðir, s. sheep’, lit. small animal"); OCS xudŭ, adj. ‘little’; Blg. xud, Srb. hud, adj. ‘bad’; OCz. & Cz. chudý, adj. ‘poor’; Moravian ‘slim, thin’; Ukr. cf. xudoba “cattle?
qusudros ‘worn, granular’. Cf. ksudh- (sic) and qusoudhos. (Phonol. ambig. in some in- stances). WP I, 502 (Various reflexes in Iran.) Skt. ksudráh, adj. ‘crushed; small; humble; mean’; Av. xšudrəm, n. geed Per. cf. (from various dialects) xurd ‘minute, tiny’; sūdan, pp: süde, v. (rub, wear down’, fr. *Ksud- ?); sul ‘feeble, weak-willed'; Romani: cf. culo, adv. "little; Gk. cf. psüdrakes, fpl., & psudrá- kia, npl. ‘pimples, rash’. Radical in Av. x3ud-, v. “pound, crush?
(qusudh-, cf. qusoudh-)
qusül- a possible variant for items listed under ksül-, q.v. Cf. further ON syla, tr. & intr. ‘stiffen (with ice)
(qusür-, a possible variant for types listed
1061
under qusór-, q. v. Oss. cf. xür, Dig. xurä ‘gravel, rubble’; Icel’
rab- (rabəl-) Lat. (ambig.) rabio, ére, v. ‘rave, rage’; rabies, f. id.; MHG (ambiguous) reffen, v. ‘snatch; bully, reprimand’; cf. G raffen, v. ‘snatch’; Du. rap, adj. ‘agile’; Sw rapp, adj. ‘dashing’; LG cf. rappeln, v. ‘clatter’; Rappel, m. ‘fit, whim, freakishness'; G Raffel, f. ‘chatterbox’. (For Du. rapen, v. ‘gather’; Sw. rappa, v. ‘snatch’; G raffen, id. a prototype *krab-, q.v. is possible)
(rād- see rod-, and cf. WP II, 369)
rād- (rðd-?) ‘glad’. (Vowel ambig. in Gmc. & Sl. Cons. ambig. in Sl.) OE rot, adj. “glad; noble; excellent'; cf. rëtan, v. ‘cheer; OCS radü, adj. ('glad; willing’, and com. S1.); radi “for the sake of”; Cz. rád, adv. ‘gladly’
radh- (or rodh-?) “seek, find, get OE redian, v. ‘reach, find, effect; OCz. roditi, inf. ‘seek, want Li. cf. randü, ràsti, v. “find”; pf: radaü; cf. also radejas, m. 'finder'; Latv. rodu, rast, pf: radu, v. as Li. (Note: EME to redd ‘to save’; MHG retten, v. id. is held to derive from *krat- OT. Romani rodav “seek? equates with Hindi dhündhna, inf. id. Icel. rata, ratast ‘find the way, succeed' derives from a type *rad- or *rod-, *urad-, *urod-)
rādh- ‘show, tell, declare, speak’. WP I, 429 Olr. ro-radid, 3s. (speaks': Li. pra-ródyti
```


## [2026-09-14T01:27:29.369Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==592' IEC.txt | grep -n \"^10[0-9][0-9]$\\|10[0-9][0-9]\" | head; echo \"=== full leaf 591 head\"; awk 'BEGIN{RS=\"\\f\"} NR==592' IEC.txt | sed -n '1,40p'"
}
```


### [2026-09-14T01:27:30.463Z] TOOL RESULT

```
14:1068
23:1069
=== full leaf 591 head
 m. (number, if for *sm-ridhmo-); Gallo-Lat. ve- rédus, gs: -1, m. 'post-horse, hunting horse": W go-rwydd, m. ('steed', fr. *epi-reidh-, cf. the W. LW gosper, fr. Lat. vesper 'evening); It. cf. réidh, adj. ‘smooth, clear, free’ (fr. *rei- dhio-; Mir réimm, n. ((course', fr. *rei- dhimn-); Ir. réim ‘troop, host’ (cf. sense of E gang); Li. riedmenos, pl. “motion”
reidhos, ios 'going, moving; easy-going, coursing’. See reidh- above. OL. réid, Ir. réidh, adj. ‘smooth, easy’; ad. réid, m. “course, ride, race’; Gaul. cf. -redus (in ve-redus, para-ve-redus); OBr. ruid "Tree, empty’; Br. ruéz, rués (sparse; OW & W rhwydd “free, easy, tolerable’; (o-gde in) MHG be-reit, -reite, adj. “ready”
reig- (roig-) “break, (Gar breach, téar, cut; piece, fragment Per. (e- or o-grade) rize ‘fragment’; Ir. ria- ghaim, v. 'téar; crucify’; Go. cf. (?) bi-reikei, f. ‘danger’; OCS riza, f. ‘garment, cloak’; R riza ‘chasuble’; Latv. riezis “baulk, boundary, ploughing-strip’; rieze, f. (time, occasion’. Se- mantics of OCS razü ‘time’, cf. Gk. rhōx and rhogás ‘cut, têar’, see urõĝ-); o-gde in Li. rai- žau, -yti, v. ‘cut, score”
reiko, ið ‘têar, break, cut’. WP II, 344. See next Av. cf. iriC-, v. ‘break out; — paiti “attack, destroy’; Gk. ereíko, v. “break, téar, slit, shat- ter; OW (denom.) rwygaw, W rhwygo, id.; MHG rihen, sv. 1. ‘stab’; Li. riekiù, ^ti, v. ‘slice’; ON cf. rista, rísta, f. ‘cut; ristill, m. *plowshare'
reikos, à, io 'téar, cut, rupture’. WP II, 344. See reikó
reidh- — reio
10
20
25
30
35
40
45
1068
Av. cf. irixta- 'outbreak'; Gk. cf. ereikion, n. *'crumbly pastry’; W rhwyg, pl. -au, f. “break, tear; Li. rieke, f. ‘slice’; Latv. rieks, m. id.; (uncertainly) MHG rihe, sf. “back lane, gutter, ditch, groove, groin, row, line’; wm. ‘instep’. Cf. rik-
reiksó, ið (reiksKo) "lay, spread, extend, reach’ Alb. rresh, v. ‘superimpose; fall — of snow or rain; W rhwych, f. “extent, extension’; Li. riešu, “ti, v. (2) ‘spread; stretch (yarn) on loom’. (Isophone: Li. reiškiu, reikšti, “explain, express, publish’)
reipo, ið ‘snatch, têar, fling’. WP II, 345. Cf. rīp- (urīp-) Gk. ereípo, v. ‘dash, destroy’; cf. ereípion, n. ‘ruin, shambles’; OFris. riva, sv. 1. ‘snatch’; ON rifa, sv. 1. id. (and 'téar); Sw. af-riva, id.; ME riven, sv. 1. ‘split, têar’; cf. OE rif, adj. ‘violent, fierce’; s. 'garment.. (Isophone: Bis. ripam, v. “hop, jump")
reiso, ið ‘snatch; ravish; burst, split’. WP I, 140. Av. raeš- ‘wound’; Skt. resámi, risyami, v. (2) "injure; OE risan, sv. 1. (3) ‘seize, ravish’; Latv. riešu, riesti, intr. "burst, split; spread”. (Isophone: Go. ur-reisan)
reit- (rit-) ‘go’. Cf. rit-. (Gmc. -ei- or -1-) Skt. cf. ritíh, f. (1) ‘course, stream, current’; OFris. cf. rith ‘stream’; OSax. rith, d Li. rie- tà, Eti, v. «roll
reitis, os ‘buttock, haunch’ Arm. eri, gs: ervo, ab. s. ereav “back, spine — of animals’; OCS riti, f. 'arse'; Li. ríetas, m. ‘haunch’
reiuos, à ‘channel’. Cf. WP I, 140 Lat. rivus, gs: -i, m. ‘brook, dike’; Ir. riabh, f. 'streak; welt; groove; W rhiw, pl. -iau, f. “drift; slope’; Li. rievà, f. “hill; ford, shallow; bank, sandbar’; rievé, f. ‘seam, vein, grain, stripe’; Latv. rieva, f. ‘chink; fold; rut; wrink- le^; cf. Li. rieveju, eti, tr. & intr. 'striate, be striated; grain, line, quilt
reið (1) ‘be mindful, think, ponder, observe, watch, regard’. Cf. retos and WP I, 73 Gk. cf. areménos, pt. as adj. ‘contemplating, expectant'; Alb. ruej, ruaj, v. “mind, guard’; rojë, f. ‘guard’; cf. ré, oroe, f. ‘attention’; Lat.
1069
reor, reri, v. ‘think’; MHG cf. ram, sm. & rame, sf. "am: OCS rájo, ati, v. (2) ‘discuss’. (NB: for Gk. oráo, óremi, see uor-, uer-)
reið (2) ‘constrain’. Cf. WP I, 141 Av. rà-, v. ‘restrain’, OCS rájo, ati, v. (D ‘push, force’; sü-r&jo, ati, v. (t
```


## [2026-09-14T01:27:38.954Z] TOOL CALL #42: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg419.png"
}
```


### [2026-09-14T01:27:39.489Z] TOOL RESULT

```

```


## [2026-09-14T01:27:39.482Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-14T01:28:06.453Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==23' HUB.txt | head -50"
}
```


### [2026-09-14T01:28:07.645Z] TOOL RESULT

```
~ 12 --
(Shk. 228), das auch advtnak u. s. w. gelesen werden
kann, vor. Also auch hier adTnak = adenak zu corri-
giren? Fr. Miiller's Gleichung: ayma = phl. aivmak
(wie gleichfalls gelesen werden kann) = ap. "^abi-vaina-
ist lautlich unmoglich. Nordbal. Ciz%na = *5jfwa sieht
ans wie ein dem Persischen entlehntes *(ldina, das
sonst nicht vorliegt. Osset. aiddnd ist lautlich nicht
klar, noch weniger kurd. nainih Afgh. dhina, ahTna^
Glina ist LW.
65. Np. ahreSum *Seide' ^ arm. LW. aprisum, apresum
setzt ein phi. apresum (aus *apare§um^ *uparesum u.s. w.)
voraus. Auch die iibrigen hier angefiihrten Worter
flir *Seide' sind wohl sammtlich aus dem Neupersischen
entlehnt, ebenso das syr. Wort, vgl. de Lagarde, G. A.
p. 7.
68. Np. a/i^Tz heisst auch 'Zinn\ vgl. Gazophyl. s. v. stagno,
Rosen, Neup. Sprachfuhrer p. 35 u. s. w., der eigent-
liche Name fiir *Blei' ist surb, Urspriinglich gilt arzzz
fiir beide Metalle, indem man zwischen weissem arztz
= 'Zinn' und schwarzem arziz — 'Blei' unterschied.^)
Auch die Armenier nennen Blei schwarzes ardic, Im
Pehlevi musste das Wort *arctc lauten. Geldner's
arezazi' (nach Darmesteter = *bataille*) habe ich
schon KZ. 27, 101 abgelehnt.
69. Vor dieser Nummer konnte arts *Wachholder mit
seinen Nebenformen {avirs u. s. w.) erwahnt werden,
mit denen Geiger bal. apurs 'Wachholder* zusammen-
gestellt hat. Leider steht nicht fest, welche der ver-
schiedenen persischen Formen richtig ist.
70. Die neupers. Formen ars, aras, ras = *Elle' sind an
sich auflfallig (aus altem ars hatteias, aus altem aras:
raS werden miissen) und stimmen nicht zu zd. cLrstya- 2),
das im Neupersischen zu *ast' geworden ware. Auch
die Bedeutung von drstya- fDaumen* oder *Klafter etc. ?)
Vgl. F r e i t a g , arab. Wb. a. v. rasas.
^) Die Var. dristya- hat G e 1 d n e r nicht in den Text auf-
genommen. Ihr wiirde np. *drist entsprechen.
```


## [2026-09-14T01:28:07.691Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^ *rēi-\\|rē-i-\\|^rē-\\|res, thing\\|REPUBLIC\\|REAL, \" AHD_watkins1985.txt | head -10"
}
```


### [2026-09-14T01:28:07.783Z] TOOL RESULT

```
621:hréc, rook: RooK!. 4. Germanic *hraban, *hrabnaz, raven, in Old English hrefn, raven: RAVEN}. 5. Extended form *krep- in Latin crepdre, to crack, burst, creak: CREPITATE, CREVICE; DECREPIT, DECREPITATE, QUEBRA- cHo. 6. Extended form *kri- in Germanic *krik- in Old French criquer, to creak, click: CRICKET!. II. Variant form *skr-. 1.Germanic *skrik- in Old English scric, thrush: SHRIKE. 2. Germanic *skrékjan- in Old Norse skrekja, to shriek: SCREAK, SCREECH. 3. Germanic *skrainjan, to shout, shriek, in Old Norse screma, to scream, perhaps akin to the possible Scandinavian source of Middle English scremen, to scream: SCREAM. III. O-grade form *kor-. 1. Latin corvus, raven: CORBEL, CORBINA, CORMORANT, CORVINE, Corvus. 2. Greek ko- rax, raven (> korakias, chough): CORACIIFORM, CORA- com. [Pok. 1. ker- 567.] ker-3. To grow. 1. Suffixed form *ker-es- in Latin Cerés, goddess of agriculture, especially the growth of grain: CEREAL, CERES. 2. Extended form *kré- (< *krea-) in: a. suffixed form *kré-yd- in Latin credre, to bring forth, create, produce (< “to cause to grow”): CREATE, CREOLE; PROCREATE; b. suffixed form *kré-sko- in Latin créscere, to grow, increase: CRESCENDO, CRESCENT, CREW!; AC- CRUE, CONCRESCENCE, CONCRETE, DECREASE, EXCRES- CENCE, INCREASE, RECRUIT. 3. Suffixed o-grade form *kor-wo-, “growing,” adolescent, in Greek kouros, koros, boy, son: DIOSCURI, HYPOCORISM. 4. Compound *sm-kéro-, “of one growth” (*sm-, same, one; see sem-'), in Latin sincérus, pure, clean: SINCERE. [Pok. 2. ker- 577.) ker-4, Heat, fire. 1. Suffixed form *ker-té in Germanic *herthé in Old English heorth, hearth: HEARTH. 2. Zero-grade form *kr- in: a. Latin carbé, charcoal, ember: CARBON, CARBUNCLE; b. extended form *krem- in Latin cremdre, to burn: CREMATE. 3. Possibly suffixed and extended form *kera-mo- in Greek keramos, potter’s clay, earthenware: CERAMIC. 4. Possibly variant ex- tended form *krds- in Russian krasa, beauty (< “bril- liance of fire”): CRASH?. [Pok. 3. ker(a)- 571.] ker-5. Also kere-. To injure. Suffixed zero-grade form *kro-yé- in Latin cariés, decay, caries: CARIES. [Pok. 4. her- 578.] ker-8. A kind of cherry. 1. Suffixed zero-grade form *kr-no- in Latin cornus, cornel tree: CORNEL. 2. Full- grade form *ker- probably in Greek kerasos, cherry: CHERRY. [Pok. 4. ker- 572.] kerd-', Heart. 1. Suffixed form *kerd-en- in Germanic *hertén- in Old English heorte, heart: HEART. 2. Zero-grade form *krd- in: a. Latin cor (stem cord-), heart: CORDATE, CORDIAL, COURAGE, QUARRY!; ACCORD, CONCORD, CORDIFORM, DISCORD, MISERICORD, RECORD; b. suffixed form *krd-yd- in Greek kardia, heart, stom- ach, orifice: CARDIA, CARDIAC, CARDIO-; DIPLOCARDIAC, ENDOCARDIUM, EPICARDIUM, MEGALOCARDIA, MYOCAR- DIUM, PERICARDIUM. 3. Possibly *kred-dha-, “‘to place trust” (an old religious term; *dho-, to do, place; see dhé-'), in Latin crédere, to believe: CREDENCE, CREDI- BLE, CREDIT, CREDO, CREDULOUS, GRANT; MISCREANT, RECREANT. [Pok. kered- 579.] kerd-2. Craft. Suffixed form *kerd-d in Old Irish cerd, art, artist: CAIRD. [Pok. 2. kerd- 579.] kerdh-. Row, herd. Suffixed form *kerdh-d@ in Germanic *herdo in Old English heord, herd: HERD. [Pok. kerdho- 579.] kere-. To mix, confuse, cook. 1. Variant form *kra- (< *kraa-) in Germanic *hrdr- in: a. possibly Old English hrér, lightly boiled, half-cooked: RARE?; b. Middle Dutch roer, motion: UPROAR. 2. Zero-grade form “krp- in: a. suffixed form *kro-ti- in Greek krasis, a mixing: IDIOSYNCRACY; b. suffixed form *kro-ter- in Greek kra- ter, mixing vessel: CRATER. [Pok. hero- 582.] kerp-. To gather, pluck, harvest. Variant karp-. 1. Ger- manic *harbistaz in Old English herfest, harvest: HAR- VEST. 2. Latin carpere, to pluck: CARPET; EXCERPT,
656:kerep-. Body. 1. Suffixed form *krep-es- in Germanic *hrifiz in Old English Arif, belly: MipRIFF. 2. Suffixed zero-grade form *krp-es- in Latin corpus, body, sub- stance: CORPORAL, CORPORAL’, CORPORATE, CORPOREAL, CORPOSANT, CORPS, CORPSE, CORPULENCE, CORPUS, COR- PUSCLE, CORSAGE, CORSE, CORSET; LEPRECHAUN. [Pok. 1. krep- 620.]
887:ré-. To bestow, endow. Contracted from *rea-. Suffixed form *rea-i- goods, wealth, property, in Latin rés, thing: RE?, REAL!, REBUS, REIFY, REPUBLIC. [Pok. 4 rei- 850.]
893:culdre, to rake, in Provengal rasclar (> French racler), to rake, scrape: RACLETTE. [Pok. 2. réd- 854.] reg-'. To move in a straight line, with derivatives mean- ing “to direct in a straight line, lead, rule.” I. Basic form *reg-. 1. Suffixed form *reg-to- in Germanic *rehtaz in Old English riht, right, just, correct, straight: RIGHT. 2. Latin regere, to lead straight, guide, rule (past partici- ple réctus, hence adjective réctus, right, straight): REALM, RECTITUDE, RECTO, RECTOR, RECTUM, REGENT, REGIME, REGIMENT, REGION; CORRECT, DIRECT, ERECT, RECTANGLE, RECTIFY, RECTILINEAR, RISORGIMENTO, SURGE. 3. Greek oregein (with prothetic vowel from oldest root form *sreg-), to stretch out, reach out for: ANORECTIC, ANOREXIA. II. Lengthened-grade form *rég-, Indo-European word for a tribal king. 1. Celtic suffixed form *rig-yo- in Germanic *rikja- in: a. Old English rice, realm: BISHOPRIC; b. Old Norse riki (> Norwegian rik), realm: RIKSMAL; c. Old English rice, strong, powerful: RICH. 2. Latin réx, king (royal and priestly title): REAL, REGAL, REGULUS, REIGN, ROYAL; INTERREX, REGICIDE, REGIUS PROFESSOR, VICEREINE, VICEROY. 3. Suffixed form *rég-en- in Sanskrit raja, rdjan-, king, rajah (femi- nine rdjni, queen, rani), and rdjati, he rules: RAJ, RAJAH, (RANI), (RYE2); MAHARAJAH, MAHARANTI. III. Suffixed lengthened-grade form *rég-old in Latin régula, straight piece of wood, rod: RAIL!, REGLET, REGULAR, REGULATE, RULE, IV. O-grade form *rog-. 1. Germanic *rak6 in Old English raca, racu, rake (implement with straight pieces of wood): RAKE!, 2,Germanic *rak- in Middle Dutch rakke, framework: RACK}, 3. Possibly Germanic *rankaz (with nasal infix) in Old English ranc, straight, strong, hence haughty, overbearing: RANK?. 4, Germanic *rak- inaz, ready, straightforward, in Old English gerecenian, to arrange in order, recount (ge-, collective prefix; see kom): RECKON. 5. Suffixed form *rog-d- in Latin rogdare, to ask (< “stretch out the hand”): ROGATION, ROGATORY; ABROGATE, ARROGATE, CORVEE, DEROGATE, INTERRO- GATE, PREROGATIVE, PROROGUE, SUBROGATE, SUPERER- ocaTE. 6. Suffixed form *rog-o- in a possible Latin noun *rogus, “extension, direction,” perhaps in a Latin phrase *é rogd, “from the direction of” (€ < ex, out of; see eghs), contracted into ergd, therefore, in consequence of: ARGAL, ERGO. V. Lengthened o-grade form *rég-. 1. Ger- manic *rdkjan in Old English rec(c)an, to pay attention to, take care (formally influenced by Old English reccan, to extend, stretch out, from Germanic *rakjan): RECK. 2. Germanic *rdékja- in Old English receléas, careless (-léas, lacking; see leu-1):; RECKLESS. [Pok. 1. reg- 854.] reg-2. Moist. 1. Suffixed variant form *rek-no- in Ger- manic *regnaz, rain, in Old English reg(e)n, rén, rain: RAIN; RAINBOW. 2. Possibly Latin rigdre, to wet, water: IRRIGATE. [Pok. 2. reg- 857.] reg-3. To dye. Lengthened-grade form *rég-. 1. Suffixed form *rég-és- in Greek rhégos, blanket, rug: REGOLITH. 2. Sanskrit rdgah, color, red: RAGA. 3. Perhaps Sanskrit raékshd, earlier form of lékshd, red dye: Lac}. [Pok. 1. reg- 854.] regv-es-. Darkness. Oldest root form *areg’-es-. Greek Erebos (with prothetic vowel), Erebus, a place of dark- ness under the earth: EREBUS. [Pok. regt-os- 857.] rei-1, To scratch, tear, cut. I. Extended form ‘reik-. 1. Germanic *rigon- in Italian riga, line (< “something cut out’’): RIGATONI. 2. Suffixed form *rei-md or *reig-sma in Latin rima, crack, cleft, fissure: RIMOSE. 3. Suffixed o-grade form *roik-wo- in Germanic *rai(h)-wa- in Old English raw, réw, a line, row: ROW!. II. Possible extended form *reipp-. Germanic *raipaz, rope, in: a. Old English rap, rope: ROPE; b. compound *stig-raipaz, “‘mount-rope,” in Old English stigrap, stirrup (see steigh-). III. Extended form *reip-. 1. Ger- manic *rifan, in Old Norse rifa, to tear: RIVE. 2. Zero-grade form *rip- in: a. Germanic *77fti- in Danish rift, breach, akin to the Scandinavian source of Middle English rift, rift: R1FT!; b. Germanic *rif- in Old English
1142:HELMINTH; ANTHELMINTIC, PLATYHELMINTH. [Pok. 7. uel- 1140.] wel-‘, To tear, pull. 1. Suffixed form *wel-do- in Latin vellere, to tear, pull: AVULSE, CONVULSE, DIVULSION, EVULSION, REVULSION, SVELTE. 2. Suffixed form *wel-no- in Latin vullis, shaggy hair, wool: VELOURS, VELVET, VILLUS [Pok. 8. wel- 1144.] wele-'. Wool. Probably related to wel-‘. 1. Suffixed extended zero-grade form “*wi-nd- in: a. Germanic *wullé in Old English wul(l), wool: woot; b. Italic *wland in Latin lana (> French laine), wool, and its derivative laénig6, down: LANATE; DELAINE, LANIFER- OUS, LANOLIN, LANUGO; ¢. Celtic *wland in Welsh gwlan, wool (> Middle English flannel, woolen cloth): FLANNEL. 2. Possible suffixed o-grade form *wol(o)-no- in Greek oulos, wooly, curly: ULoTRICHOUs. [Pok. 4. uel- 1139.] wela-2. To strike, wound. 1. Suffixed o-grade form *wol()-o- in Germanic *walaz in Old Norse valr, the slain in battle in: a. Old Norse Valhdéll, Valhalla: VAL- HALLA; b. Old Norse Valkyrja, “chooser of the slain,” name of one of the twelve war goddesses (-kyrja, chooser; see geus-): VALKYRIE. 2. Suffixed basic form *welo-nes- in Latin vudnus (stem vulner-), a wound: VULNERABLE. [In Pok. 8. wel- 1144.] welg-. Wet. Germanic *welk- in: a. Old English wolc(e)n, cloud, sky: WELKIN; b. Middle English welken, to wilt: wILT!. [Pok. 2. welk-, uelg-, 1145.] welt-. Woods; wild. 1. Suffixed form *wolt-u- in Germanic *walthuz in: a. Old English weald, wald, a forest: WEALD, WOLD!; b. Old Norse vdllr, field: VOLE!. 2. Ger- manic *walthdn- in Middle English welde, a plant yield- ing a yellow dye, weld: WELD2. 3. Germanic *wilthigaz in: a. Old English wilde, wild: wip; b. Old English wildéor, wilddéor, wild beast (déor, animal; see dheu-'): WILDERNESS; C. Dutch wild, wild: WILDEBEEST. [In Pok. 4. uel- 1139.] weme-. To vomit. 1. Germanic *wam- in Old Norse vamla, qualm, and Danish vamle, to become sick, prob- ably akin to the Scandinavian source of Middle English wam(ejlen, to feel nausea, stagger: WAMBLE. 2. Latin vomere, to vomit: NUX VOMICA, VOMIT. 3. Greek emein, to vomit: EMESIS, EMETIC. [Pok. wem- 1146.] wen-', To desire, strive for. 1. Suffixed form *wen-w- in Germanic *winn(w)an, to seek to gain, in Old English winnan, to win: WIN}. 2. Suffixed zero-grade form *wn-ydé in Germanic *wunjé in Old English wynn, wen, pleasure, joy: WEN2, WINSOME. 3. Suffixed (stative) zero-grade form *wn-é-, to be contented, in Germanic *wunén in Old English wunian, to become accustomed to, dwell: won!, (wont). 4. Suffixed (causative) o-grade form *won-eyo- in Germanic *wanjan in Old English wenian, to accustom, train, wean: WEAN}. 5. Germanic *wéniz, hope, with denominative *wénjan, to hope, in Old English wénan, to expect, imagine, think: WEEN. 6. Suffixed zero-grade form *wn-sko- in Germanic *wunsk- in Old English wyscan, to desire, wish: WISH. 7. O-grade *won- perhaps in Germanic *wani- in: a. Old Norse Vanir, the Vanir: VANIR; b. Old Norse vana- in Vanadis, name of the goddess Freya: VANADIUM 8. Suf- fixed form *wen-es- in: a. Latin venus, love (> venerari, to worship): VENERATE, VENEREAL, VENERY!, VENUS; b. suffixed form *wen-es-no- in Latin venénum, love potion, poison: VENOM. 9. Suffixed form *wen-eto-, “be- loved,” possibly in Germanic *Weneda-, a Slavic people, in Old High German Winida, the Wends: WEND. 10, Suffixed form “wen-yd@ in Latin venia, favor, forgive- ness: VENIAL. 11. Lengthened-grade form *wén-d- in Latin véndri, to hunt: VENATIC, VENERY2, VENISON. 12. Suffixed basic form *wen-o- in Sanskrit vanam, forest: WANDEROO. 13. Possibly zero-grade suffixed form *wn-ig- in Sanskrit vanik, vdnijah, merchant (? < “seek- ing to gain”): BANIAN. [Pok. 1. ven- 1146.] wen-2. To beat, wound. 1. Suffixed zero-grade form
2178:REIGN reg-! REIMBURSE bursa REINDEER dheu-1, ker-1 REINFORCE bhergh-2 REITERATE i- REJECT yé- REJOICE gau- REJUVENATE yeu- RELAPSE leb-! RELATE tele- RELAX slég- RELAY slég- RELEGATE leg-1 RELENT lento- RELIEVE leg¥h- RELINQUISH leikw- RELUCENT leuk- RELUCT leug-! RELY leig-1 REMAIN men-3 REMAND man-2 REMARK merg- REMEDY med- REMEMBER (s)mer-! REMEX ere-! REMINISCENT men-! REMIT (s)meit(a)- REMORA mere- REMORSE mer-2 REMOTE meue- REMOVE meue- REMUDA mei-1 REMUNERATE mei-! RENAISSANCE gene- REND rendh- RENDER do- _ RENDEZVOUS wOS RENEGADE ne RENEGE ne RENITENT kneigh- RENOUNCE neu-! RENOVATE newo- RENOWN no-men- RENT! do- REPAIR! pere-1 REPAND pete- REPARTEE pere-2 REPAST pa- REPEAT pet- REPEL pel-6 REPENT2 rép-1 REPERTORY pere-! REPINE kWei-1 REPLENISH pele-! REPLETE pele-1 REPLEVIN plegan REPLICATE plek- REPORT per-2 REPOSE! paus- REPOSIT apo- REPREHEND ghend- REPRESENT e@S- REPRESS per-5 REPRIMAND per-5 REPRISAL ghend- REPRISE ghend- REPROACH pert REPROVE per? REPTILE rép-1 REPUBLIC ré- REPUDIATE (s)peud- REPUGN peuk- REPUTE peu-
```


## [2026-09-14T01:28:17.761Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1398,1450p' incoming/FFD/FFD_pages.txt"
}
```


### [2026-09-14T01:28:17.823Z] TOOL RESULT

```
[pdf page 56]
ماده‌های ماضی و مضارع فارسی دری --___شش ۵۱
صورت اصلی 3 است.» 0 پیش از ۲ به ۶ بدل شده است.
خواب < فارسی میانه 330: اسم است» در فارسی دری «خواب» به عنوان مادهٌ
مضارع «خفتن» به کار رفته است. ماده مضارع در فارسی میانه کته است.
بازماندهٌ ۹۷۵۵۵* ایرانی باستان. ۵۸:* ساخته شده است از ۸82 با بدل‌شدن 0 به ؟
پیش از 8 و 82 8 برای ساختن مادةٌ آغازی از ريشه به کار می‌رفته است. برای 2 آرای.
در فارسی دری از «خفس» که به صورتهای «خسپ» و «خسب» هم به کار رفته. مادهٌ
ماضی جعلی ساخته شده است: خفسید., خسپید, خسبید.
خندیدن
خندید < فارسی میانه ۰۵414 مادهٌ ماضی جعلی است. از ماده مضارع ساخته
شده است. َ
خند < فارسی میانه 75384 < ایرانی باستان ۰*۵4 380 در فارسی میانه و ایراتی
باستان» «خندیدن» معنی می‌دهد.
خواستن
خواست < فارسی میانه 7۳391« ایرانی باستان 9-1۵:*. برای اه آراست. 7۷36
صورت اصلی ۷38 است. 4 پیش از ۲ به 5 بدل شده است. ۷30 به معتی «خواستن»
است.
خواه + فارسی میانه ۳:5 < ایرانی باستان -۷۷24:*. برای ۵ -> آرای.
خواندن
خواند + فارسی میانه ۷384 < ایرانی باستان 1:۵۵-1۵*. برای 18 > آراست. ريشةٌ :
31 به معنی «بانگ کردن» است.
خوان < فارسی میانه ۷۸37 < ایرانی باستان -۳۷3:*. برای ۵ > آرای. 1۷۷3۵
صورت بالاندةٌ ۷۵2 است.
[pdf page 57]
فعلهای فارسی دری
خوردن
خورد + فارسی میانه ۷۵7۵4 + ایرانی باستان ۷۷۵۲-1۵*. برای 2 آراست.
: خور + فارسی میانه 5۷۵7 < ایرانی باستان ۴*3۵۲-۵. برای 8 -> آرای.
و 3۷/8۲ به معنی (خوردن» و «نوشیدن» هر دو به کار رفته‌اند.
خوشیدن
«خوشید» مادةٌ ماضی جعلی است. از مادهٌ مضارع ساخته شده است.
خوش « فارسی میانه 355 < ایرانی باستان 8۸۵05-8*. برای ۵ -> آرای. ريشةٌ 1205 به
معنی «خشک شدن» است.
واژةٌ «خشک» از ريشهٌ ۳203 گرفته شده است. صورت فارسی ميانةٌ آن 1031 است. از
ایرانی باستان 8۵5-2*. 1805 صورت ضعیف ريشه و 1۵ پسوند است.
دادن
داد < فارسی میانه 434 < ایرانی باستان 43-12*. برای "18 > آراست. ريشهٌ 45
به‌معنی «دادن» است. در ایرانی باستان دو ريشةٌ 48 وجود داشته است: ۱-به معنی
«دادن»» ۲- به معنی «نهادن». «نهادن» از 13 به معنی «نهادن)» آمده است. >
نهادن.
ده < فارسی میانه 42 < ایرانی باستان ۵4۵۵5". 4202 ماد مضاعف است از 43.
داشتن
داشت + فارسی میانه 4381. به جای 4381 باید 417۵ می آمد از 4۲-12* ایرانی باستان.
7 صورت ضعیف ريشةٌ 447 است. برای 1۵ -> آراست. 4351 به قیاس با 137 1351
به‌وجود آمده است.
دار < فارسی میانه 437 < ایرانی باستان 437-۵*. برای 2 -> آرای. 437 صورت بالانده
ريشهٌ 487 است. 447 به معنی «داشتن» است.
[pdf page 58]
ماده‌های ماضی و مضارع فارسی دری ۳ تا ۵۳
دانستن
دانست < فارسی میانه 420191. 432181 در فارسی میانه مادهٌ ماضی جعلی است.
دان + فارسی میانه 438 + فارسی باستان 4202* < ایرانی باستان 2288*: دانستن.
```


## [2026-09-14T01:28:26.273Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"رشتن\\|ریسیدن\\|ریس\\b\\|رشت \" incoming/FFD/FFD_pages.txt | head -20"
}
```


### [2026-09-14T01:28:26.327Z] TOOL RESULT

```
130:رشت رز
1027:برشتن
1028:برشت < فارسی میانه 07151 < ایرانی باستان ۳۳18-1*. برای 18 -> آراست. 0۲2 که
1532:رشتن
1533:«ریس) ماده مضارع «رشتن» است. ظاهراً «رشتن»» «ریس» از ربشةٌ 5۵12" به معنی
1535:رشت < ایرانی باستان 718-1۵*. برای 1۸ -> آراست. ۲2 صورت اصلی قلة است» 7
1537:ریس < ایرانی باستان 112-2*.برای 2 > آرای.در اینجا 2ب بدل شده است. > لشتن.
1636:سرشتن
1637:سرشت < فارسی میانه 85151 + ایرانی باستان ۶713-1۵*. برای ۵ > آراست. کزرّه
1963:گریست < فارسی میانه افاولاع. 81اررزتع ماده مأضی جعلی است» از مادهٌ مضارع
2134:نگرستن. نگریستن. نگریدن
2135:نگرست» نگریست» نگرید. هر سه مادةٌ ماضی جعلی هستند. در فارسی میانه
2480:۰ ۵2 : (ريشه - بافتن + رشتن) ۵۶
2481:: داقسنادم: ۳۴۵ (ريشه < بافتن -ه رشتن
2507:8 ۰ 8 : ۶ + رشتن
```


## [2026-09-14T01:28:29.981Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1525,1545p' incoming/FFD/FFD_pages.txt; echo \"=== nearest pdf page tag\"; awk 'NR<=1532 && /\\[pdf page/ {p=$0} END{print p}' incoming/FFD/FFD_pages.txt; echo \"=== header line of that page\"; awk 'NR<=1540 && NR>=1500' incoming/FFD/FFD_pages.txt | grep -n \"pdf page\" "
}
```


### [2026-09-14T01:28:31.044Z] TOOL RESULT

```
رسیدن
رسید < فارسی میانه 72914. مادةٌ ماضی جعلی است. از ماده مضارع ساخته شده
است.
رس < فارسی میانه 7۵8 + ایرانی باستان ۲۵-۹-۵*. برای ۵ -> آرای. 8نشانه‌ای بوده که
برای ساختن‌مادء آغازی‌از ريشه‌به کار می‌رفته‌است.ريشةٌ ۲3به‌معنی «حرکت‌کردن» است.
«پذیره» بازماندةٌ 0207788 فارسی میانه است و ربطی به «پذیرفتن» ندارد. ۳02477۸8
بازماندةٌ 0211-78-6۵* ایرانی باستان است. 081 پیشوند و 1۵ پسوند و 73 ريشه است.
رشتن
«ریس) ماده مضارع «رشتن» است. ظاهراً «رشتن»» «ریس» از ربشةٌ 5۵12" به معنی
«بافتن» آمده است» به شرح زیر:
رشت < ایرانی باستان 718-1۵*. برای 1۸ -> آراست. ۲2 صورت اصلی قلة است» 7
پیش از 1 به 5 بدل شده است. 717 صورت ضعیف ريشه است.
ریس < ایرانی باستان 112-2*.برای 2 > آرای.در اینجا 2ب بدل شده است. > لشتن.
۱ رقتن
رقت < فارسی میانه 71 « ایرانی باستان ۴۲۵۳4۵. برای 12 -> آراست. 720 صورت
[pdf page 62]
ماده‌های ماضی و مضارع فارسی دری سا ی ۵۷
اصلی 78۶ است» ۳ پیش از 1به ] بدل شده است.
رو < فارسی میانه 127۷ + ایرانی باستان ۲۵0-2*. برای 2 > آرای. ريشهٌ 780 به معنی
«حرکت کردن» است» چون 37 , 3820422 به معنی «حرکت کردن به سوی متکلم» است.
«رفتن» بط «دورشدن از متکلم» اختصاص پافته است.
=== nearest pdf page tag
[pdf page 61]
=== header line of that page
17:[pdf page 61]
41:[pdf page 62]
```


## [2026-09-14T01:28:45.895Z] TOOL CALL #48: Bash

```json
{
 "command": "S=/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && pdftoppm -f 419 -l 419 -r 400 -png -singlefile EtymologicalDictionary-persian-english.pdf $S/pg419_hi && python3 -c \"\nfrom PIL import Image\nim=Image.open('$S/pg419_hi.png'); print(im.size)\n# crop the Avestan/OP box region: approx x 0.20-0.45, y 0.33-0.40 of page\nw,h=im.size\nim.crop((int(0.19*w),int(0.325*h),int(0.45*w),int(0.385*h))).save('$S/crop419_a.png')\nim.crop((int(0.19*w),int(0.63*h),int(0.55*w),int(0.70*h))).save('$S/crop419_b.png')\nim.crop((int(0.19*w),int(0.77*h),int(0.45*w),int(0.83*h))).save('$S/crop419_c.png')\n\""
}
```


### [2026-09-14T01:28:49.058Z] TOOL RESULT

```
(3400, 4400)
```


## [2026-09-14T01:28:51.210Z] TOOL CALL #49: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/crop419_a.png"
}
```


### [2026-09-14T01:28:51.237Z] TOOL RESULT

```

```


## [2026-09-14T01:28:54.145Z] TOOL CALL #50: Bash

```json
{
 "command": "S=/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('$S/pg419_hi.png'); w,h=im.size\nim.crop((int(0.19*w),int(0.375*h),int(0.42*w),int(0.425*h))).save('$S/crop419_d.png')\n\""
}
```


### [2026-09-14T01:28:55.531Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T01:28:57.660Z] TOOL CALL #51: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/crop419_d.png"
}
```


### [2026-09-14T01:28:57.679Z] TOOL RESULT

```

```


## [2026-09-14T01:29:19.641Z] TOOL CALL #52: Bash

```json
{
 "command": "S=/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('$S/pg419_hi.png'); w,h=im.size\nim.crop((int(0.19*w),int(0.555*h),int(0.45*w),int(0.605*h))).save('$S/crop419_skt.png')\nim.crop((int(0.19*w),int(0.695*h),int(0.45*w),int(0.745*h))).save('$S/crop419_grk.png')\n\""
}
```


### [2026-09-14T01:29:21.006Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T01:29:23.263Z] TOOL CALL #53: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/crop419_grk.png"
}
```


### [2026-09-14T01:29:23.282Z] TOOL RESULT

```

```


## [2026-09-14T01:29:33.345Z] TOOL CALL #54: Bash

```json
{
 "command": "sed -n '1,40p' tools/fetch_source.py; mkdir -p data/verification/sources/refs/ocr/BOOK; cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg419.png data/verification/sources/refs/ocr/BOOK/419.png; ls -la data/verification/sources/refs/ocr/BOOK/ | head"
}
```


### [2026-09-14T01:29:33.492Z] TOOL RESULT

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
total 19776
drwxrwxr-x  2 sfmqrb sfmqrb  12288 Sep 13 21:29 .
drwxrwxr-x 13 sfmqrb sfmqrb   4096 Sep  7 13:51 ..
-rw-rw-r--  1 sfmqrb sfmqrb  71589 Sep  5 10:46 100.png
-rw-rw-r--  1 sfmqrb sfmqrb 104864 Sep  4 19:03 101.png
-rw-rw-r--  1 sfmqrb sfmqrb  68145 Sep  5 10:49 102.png
-rw-rw-r--  1 sfmqrb sfmqrb  79623 Sep  5 10:55 103.png
-rw-rw-r--  1 sfmqrb sfmqrb  78826 Sep  5 10:59 104.png
-rw-rw-r--  1 sfmqrb sfmqrb  82500 Sep  5 11:05 105.png
-rw-rw-r--  1 sfmqrb sfmqrb  55270 Sep  5 11:03 106.png
```


## [2026-09-14T01:29:39.181Z] TOOL CALL #55: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/res#Latin\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/reh₁ís\" \\\n \"https://en.wiktionary.org/wiki/%D8%B1%DB%8C%D8%B4\" \\\n \"https://en.wiktionary.org/wiki/%D8%B1%D8%B4%D8%AA%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D8%A7%D8%A8%D8%B1%DB%8C%D8%B4%D9%85\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 419 (Rei 1 / Rei 2, Reig): root and node checks\" 2>&1 | tail -2; done"
}
```


### [2026-09-14T01:29:42.921Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/ce2f94113524ca2d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2fbe30a48f2cc0a7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e17421429166fa74.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/034cda863459f668.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c03254e07af3549e.txt
```


## [2026-09-14T01:29:45.599Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 034cda863459f668 c03254e07af3549e e17421429166fa74; do echo \"########## $f\"; grep -n -i \"etymology\" -A 12 $f.txt | head -60; done"
}
```


### [2026-09-14T01:29:46.655Z] TOOL RESULT

```
########## 034cda863459f668
62: Etymology 1 
63-
64- 1.1.1 
65- Pronunciation 
66-
67- 1.1.2 
68- Verb 
69-
70- 1.1.2.1 
71- Alternative forms 
72-
73- 1.1.2.2 
74- Derived terms 
--
80: Etymology 2 
81-
82- 1.2.1 
83- Pronunciation 
84-
85- 1.2.2 
86- Verb 
87-
88- 1.2.2.1 
89- Derived terms 
90-
91- 1.3 
92- References 
--
161: Etymology 1
162- [ edit ] 
163-
164- From Proto-Iranian *wrais- ( “ to turn, to spin ” ) , from Proto-Indo-Iranian , from Proto-Indo-European *wriḱ-yé-ti ( “ to twist, to bend ” ) , [ 1 ] whence also Avestan 𐬎𐬭𐬎𐬎𐬌𐬯𐬌𐬀 ( uruuisia , “ to turn ” ) , German reihen ( “ to sew loosely ” ) , English wry , Latin rīca ( “ veil ” ) . Doublet of رشته ( rešte , “ thread, string ” ) .
165-
166- Pronunciation
167- [ edit ] 
168-
169- IPA ( key ) : [reʃˈtæn] 
170-
171- Verb
172- [ edit ] 
173-
--
193: Etymology 2
194- [ edit ] 
195-
196- From Proto-Iranian *ra(n)ǰ- ( “ to colour, dye ” ) , from Proto-Indo-Iranian [Term?] . Cognate with Sanskrit रञ्ज् ( rañj , “ to be dyed or coloured, to redden, grow red, glow ” ) . [ 2 ] Related to رنگ ( rang , “ color ” ) .
197-
198- Pronunciation
199- [ edit ] 
200-
201- IPA ( key ) : [ræʃˈtæn] 
202-
203- Verb
204- [ edit ] 
205-
########## c03254e07af3549e
65: Etymology 
66-
67- 1.3 
68- Pronunciation 
69-
70- 1.4 
71- Noun 
72-
73- 1.4.1 
74- Derived terms 
75-
76- 1.4.2 
77- Descendants 
--
172: Etymology
173- [ edit ] 
174-
175- Inherited from Middle Persian [Book Pahlavi needed] ( ʾp̄lyšwm, ʾp̄lyšm /⁠abrēšōm, abrēšom⁠/ , “ silk ” ) , from Proto-Iranian *upawraišamah . Compare Luri ڢریشم ( wrişem ) and Old Armenian loanword ապրիշում ( aprišum , “ silk ” ) .
176-
177- Pronunciation
178- [ edit ] 
179-
180- ( Classical Persian ) IPA ( key ) : /ʔab.reː.ˈʃam/ , /ʔab.reː.ˈʃum/ 
181-
182- ( Dari, formal ) IPA ( key ) : [ʔäb.ɾeː.ʃám] , [ʔäb.ɾeː.ʃʊ́m] 
183-
184- ( Dari, formal ) IPA ( key ) : [ʔäb.ɾeː.ʃám] , [ʔäb.ɾeː.ʃʊ́m] 
########## e17421429166fa74
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
69-
70- 1.3.1 
71- Derived terms 
72-
73- 1.4 
74- References 
--
82: Etymology 1 
83-
84- 2.1.1 
85- Noun 
86-
87- 2.2 
88: Etymology 2 
89-
90- 2.2.1 
91- Noun 
92-
93- 2.3 
94: Etymology 3 
95-
96- 2.3.1 
97- Noun 
98-
99- 2.4 
100- Further reading 
101-
102- 3 
103- Persian 
104-
105- Toggle Persian subsection 
106-
--
108: Etymology 1 
109-
110- 3.1.1 
111- Pronunciation 
112-
113- 3.1.2 
114- Noun 
115-
116- 3.1.2.1 
117- Inflection 
118-
119- 3.1.2.2 
120- Related terms 
--
123: Etymology 2 
124-
125- 3.2.1 
126- Pronunciation 
127-
128- 3.2.2
```


## [2026-09-14T01:29:53.402Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '/^ Persian$/,$p' e17421429166fa74.txt | sed -n '1,120p' | grep -n \"From\\|Middle Persian\\|Proto-Iranian\\|wound\\|beard\" | head -30"
}
```


### [2026-09-14T01:29:54.461Z] TOOL RESULT

```
4: یک مرد با ریش کوتاه ― A man with a short beard 
9: Derived from Middle Persian [script needed] ( lyš /⁠rēš⁠/ , “ beard ” ) , probably from Proto-Iranian *xraiša- , from Proto-Indo-European *kreyso- , itself from Proto-Indo-European *(s)kre-i-s- , an extension of *(s)ker- ( “ to turn, bend ” ) . [ 1 ] 
52: beard 
55:šāna tawān kard ba angušt-i xwēš If there is no ivory comb for one's beard ,
```


## [2026-09-14T01:29:56.567Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '/^ Persian$/,$p' e17421429166fa74.txt | grep -n \"Etymology 2\" -A 20 | head -40"
}
```


### [2026-09-14T01:29:57.571Z] TOOL RESULT

```
151: Etymology 2
152- [ edit ] 
153-
154- Inherited from Middle Persian lyš ( rēš ) , from Proto-Indo-Iranian *rayšás ( “ injury, wound ” ) from the root *rayš- ( “ to be wounded, hurt; to suffer injury ” ) . [ 2 ] [ 3 ] 
155-
156- Pronunciation
157- [ edit ] 
158-
159- ( Classical Persian ) IPA ( key ) : /ˈreːʃ/ 
160-
161- ( Dari, formal ) IPA ( key ) : [reːʃ] 
162-
163- ( Dari, formal ) IPA ( key ) : [reːʃ] 
164- ( Kabuli ) IPA ( key ) : [reːʃ] 
165-
166- ( Hazaragi ) IPA ( key ) : [reːʃ] 
167-
168- ( Iran, formal ) IPA ( key ) : [ɹiːʃ] 
169-
170- ( Tajik, formal ) IPA ( key ) : [ɾeʃ] 
171-
--
238: Etymology 2
239- [ edit ] 
240-
241- Derived from Classical Persian ریش ( rēš , “ wound, injury ” ) .
242-
243- Pronunciation
244- [ edit ] 
245-
246- ( Standard Urdu ) IPA ( key ) : /ɾeːʃ/ 
247-
248- Noun
249- [ edit ] 
250-
251- ریش • ( rēš )  m ( Hindi spelling रेश ) 
252-
253- wound 
254-
255- scar
```


## [2026-09-14T01:30:03.704Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n \"Proto-Italic\\|reh₁\\|Sanskrit रा\\|rayí\\|Etymology\" ce2f94113524ca2d.txt | head -20; echo \"=== PIE page\"; head -40 2fbe30a48f2cc0a7.txt"
}
```


### [2026-09-14T01:30:03.780Z] TOOL RESULT

```
62: Etymology 1 
71: Etymology 2 
85: Etymology 1 
94: Etymology 2 
120: Etymology 
148: Etymology 1 
169: Etymology 2 
181: Etymology 3 
190: Etymology 4 
210: Etymology 1 
228: Etymology 2 
240: Etymology 3 
254: Etymology 1 
269: Etymology 2 
287: Etymology 3 
304: Etymology 
333: Etymology 
353: Etymology 
373: Etymology 1 
382: Etymology 2 
=== PIE page
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/reh₁ís
FETCHED: 2026-09-14T01:29:41Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/(H)reh₁ís - Wiktionary, the free dictionary

Reconstruction:Proto-Indo-European/(H)reh₁ís - Wiktionary, the free dictionary 

 Jump to content 

 Main menu 

 Main menu

 move to sidebar 
 hide 

 Navigation

 Main page 
 Community portal 
 Requested entries 
 Recent changes 
 Random entry 
 Help 
 Glossary 
 Contact us 
 Special pages 

 Search 

 Search 

 Appearance 

 Donations 

 Create account 

 Log in
```


## [2026-09-14T01:30:06.602Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '/Proto-Indo-European$/,$p' 2fbe30a48f2cc0a7.txt | grep -n \"Noun\\|Descendants\\|Sanskrit\\|Avestan\\|Latin\\|wealth\\|possession\\|Iranian\\|rā\" | head -40"
}
```


### [2026-09-14T01:30:07.605Z] TOOL RESULT

```
9: Noun
14: wealth , goods 
106: Descendants
109: Proto-Indo-Iranian: *raHíš ( see there for further descendants )
118: ↑ 2.0 2.1 De Vaan, Michiel ( 2008 ), “ rēs, reī ”, in Etymological Dictionary of Latin and the other Italic Languages (Leiden Indo-European Etymological Dictionary Series; 7), Leiden, Boston: Brill, →ISBN , pages 520-521 : “ *Hreh₁-i- 'wealth, goods' ” 
122: ^ Sihler, Andrew L. ( 1995 ), New Comparative Grammar of Greek and Latin , Oxford, New York: Oxford University Press, →ISBN , page 341 : “ *reH₁is ”
```


## [2026-09-14T01:30:15.867Z] TOOL CALL #61: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%D8%B1%D8%A7%D8%AF\" \\\n \"https://www.etymonline.com/word/ripple\" \\\n \"https://www.etymonline.com/word/river\" \\\n \"https://en.wiktionary.org/wiki/%D8%B1%DB%8C%D8%AE%D8%AA%D9%86\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 419 (Rei 1 / Rei 2, Reig): node checks rad, ripple, river, rixtan\" 2>&1 | tail -1; done"
}
```


### [2026-09-14T01:30:18.616Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/bcd404de5727dc7d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1bfa73e198d10af3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/164b893d49ce5460.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8f50a6d77a93ae16.txt
```


## [2026-09-14T01:30:22.823Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"### راد\"; sed -n '/^ Persian$/,$p' bcd404de5727dc7d.txt | grep -n \"Middle Persian\\|Proto-Iranian\\|Avestan\\|generous\\|From \" | head -12; echo \"### ripple\"; grep -n -i \"ripple\" 1bfa73e198d10af3.txt | head -12; echo \"### river\"; grep -n -i \"ripa\\|river (n\" 164b893d49ce5460.txt | head -8; echo \"### ریختن\"; sed -n '/^ Persian$/,$p' 8f50a6d77a93ae16.txt | grep -n \"Proto-Iranian\\|Middle Persian\\|Proto-Indo-European\" | head -8"
}
```


### [2026-09-14T01:30:23.977Z] TOOL RESULT

```
### راد
7: Inherited from Middle Persian [Book Pahlavi needed] ( lʾt' /⁠rād⁠/ ) , from Old Persian [script needed] ( *rā́daʰ ) , from Proto-Iranian *HráHdah , from Proto-Indo-Iranian *HráHdʰas , from Proto-Indo-European *h₂réh₁dʰ-o-s , from *h₂reh₁dʰ- ( “ to care ” ) +‎ *-os .
9: Cognate with Old Avestan 𐬭𐬁𐬛𐬀𐬵 ( rādah , “ generosity, care; generous ” ) , Vedic Sanskrit राधस् ( rā́dhas , “ favour, generosity, gift ” ) , Proto-Slavic *raditi ( “ to care about, to heed ” ) , Proto-Germanic *rēdaną ( “ to decide, advise ” ) .
52: generous , bounteous , liberal 
80: Persian terms inherited from Middle Persian 
81: Persian terms derived from Middle Persian 
84: Persian terms inherited from Proto-Iranian 
85: Persian terms derived from Proto-Iranian 
103: Requests for Book Pahlavi script for Middle Persian terms 
### ripple
1:URL: https://www.etymonline.com/word/ripple
4:TITLE: Ripple - Etymology, Origin & Meaning
6:Ripple - Etymology, Origin & Meaning 
21: Origin and history of ripple 
23: ripple (v.) 
25: early 15c., riplen , "to crease, wrinkle;" 1660s, "to present a ruffled surface," of obscure origin, perhaps a frequentative of rip (v.), and compare rip (n.2) and rumple . Transitive sense, in reference to the surface of water, "cause to ripple, agitate lightly," is from 1786. Related: Rippled ; rippling .
28: ripple (n.) 
30: "very small wave," 1798, from earlier meaning "stretch of shallow, rippling water" (1755), from ripple (v.). The meaning "light ruffling of the surface suggestive of a ripple" is from 1843.
32: The meaning "ice cream streaked with colored syrup" is attested by 1939, so called from its appearance. In reference to the ripple-rings in water from a cast stone, by 1884. (Chaucer, late 14c., used roundel "a little circle" for that.) As the name of a brand of inexpensive wine sold by E&J Gallo Winery, from 1960 to 1984. In geology, ripple-mark "wavy surface on sand formed by wind or water" is by 1833. Ripple effect "continuous spreading results of an event or action" is from 1950.
35: Entries linking to ripple 
109: Share ripple 
113: https://www.etymonline.com/word/ripple Copy 
### river
23: river (n.) 
25: early 13c. (late 12c. in surnames), "a considerable body of water flowing with perceptible current in a definite course or channel," from Anglo-French rivere , Old French riviere "river, riverside, river bank" (12c.), from Vulgar Latin *riparia "riverbank, seashore, river" (source also of Spanish ribera , Italian riviera ), noun use of fem. of Latin riparius "of a riverbank" (see riparian ).
34: riparian (adj.) 
36: "of or pertaining to river banks, situated on or near a river bank," 1849, with -an + Latin riparius "of a river bank," from riparia "shore," later used in reference to the stream flowing between the banks, from ripa "(steep) bank of a river, shore."
40: Riparious , of animals, "living on or in river banks," is from 1650s.
### ریختن
12: Inherited from Middle Persian 𐭥𐭩𐭧𐭲𐭭 ( ʿyḥtn /⁠rēxtan⁠/ ) , from Proto-Iranian *Hraič- ( “ to pour; to flow ” ) , Northern Luri رختێ ( rextı ) , an Iranian-specific suffixed form of Proto-Indo-Iranian *HriHyáti ( “ to flow ” ) . [ 1 ] 
902: Categories : Persian terms inherited from Middle Persian 
903: Persian terms derived from Middle Persian 
904: Persian terms inherited from Proto-Iranian 
905: Persian terms derived from Proto-Iranian
```


## [2026-09-14T01:30:47.380Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN rad\"; grep -n \"räd 'freigebig\\|rad 'freigebig\\|freigebig\" HRN.txt | head -10; echo \"=== PHD rad\"; grep -n \"rād \\[\" PHD.txt | head -5; grep -n \"generous\" PHD.txt | head -5; echo \"=== NYB\"; grep -n \"rād\\b\" NYB_vol2_glossary.txt | head -10"
}
```


### [2026-09-14T01:30:47.496Z] TOOL RESULT

```
=== HRN rad
5391:601. räd 'freigebig.
=== PHD rad
555:rabih [/pyh | M rbyh] noon, midday (heat). rad [/t! | N —] (spiritual) chief, master. АҺ: office of rad. rad [Pu | P rd, N ~] generous, liberal. ~ih: generosity, liberality. radag [itk! | M rdg, N rada] line, rank, row. radómand [/t?^wmnd] having a rad. rad-passag [/tps’k'] ceremonies of the gáhanbar festivals. radunay [/twny = Av. ratunaya-] one under the guidance of a rad. raftan, raw- [SGY TWN-tn! < А V sg’; lwb- | M rptn, rw-, N ~] go, move, proceed. ~išn, v. rawišn. raftār [/pt?] | N ~] goer. rag А! | M rg, N ~] vein. «ЛЬ: disposition, character. ray [/gy | P rg] quick, swift. ray [Pg | N —] meadow, plain. rah [/s, lh, [hy | M rh(y)] chariot, wagon. rah-, у. rastan. rah [Ps | M rh, N ~] road, way. rahag [/hk! | P rhg] = rag. rāh-dār [lsd] | N ~] brigand, highway robber. ~ih: brigandage. rahig [/syk!, Ikyk' | M rhyg, N rahi] child, page. ~ih: childhood. rāh-nimāy [Psnm?d | (M r’-hnmwd’r), № ~numa] guide. ram [Pm | М әт, N ~] peace; cal. 21st day. ram(ag) [/m(k') | P rm, N ram(a)] herd, flock. ráménidan, rāmēn- [Pmyn-ytn! | M ?myn-] give peace, pleasure. rāmišn [P min! | M rmyfn, N rāmi$] peace, ease, pleasure. ~ig [-vk! | N —z#] peaceful, at ease. ran [Рп! | N ~] thigh. P rān- [/^n-] fight. randidan, rand- [/nd-ytn! | N —] scratch, grate, abrade. rang [/ng | M rng, N —] colour, dye. ranj [Inc | P rnj, (M rnz), N ~] toil, trouble. ~ag [-k' | N —a] troubled. ranjénidan, ranjén- [/ncyn-ytn'] trouble.
2092:generous rad.
=== NYB
507:(cf 41?" and 89%); ~ fravartak in the letter 1822; — combined with another prep.: ~ 6 pad estat 28%. 1189. 11917 (cf above 1871); ~ 6 ax“ i astomand 401; m andar äyiyänak 409; ~ tdi sdxdn 401; ~ pat óstak 48% (ete.). — b) temporal: ~ sal 2 mazdesn bag’ Šāhpuhr” in the year 2 of the Mazdayasnian Divine Sh. Pl:l; ~ sal "68 in the year 68 P2:1; ~ pat han jamān ka at the time when 41%, adak ~ pat jamän at that time 619; 4214; 3 sap td three nights ago 512-3, — c) figurative: on, about (esp. in headings and book titles), concerning; (reigning) over, (merciful) to, (hostile) to- wards; (means) for; ete.; — with an inf. or a v.n.: in order to 3714-15, 4515; 1185 (continued by inf. + rād, l. 6). - ~ does not govern encl. pronouns; single excep- tion apar-aš 54° (late passage). — Av. (394 sq.) upati, OP upariy; MPrthPrs br; Paz. awar; NP bar. Cf aper. — On MDM 43" v. hàreftan.
509:apar-āstišnēh [’pl’stSnyh] the act of ac- cepting and taking care of: ~ % én den rād 589, with the gl. kū tà? pat én den bē éstat (subju. 3d p. sg., v. estátan) ; 5919. — < apar + ēstātan; as to the alternation é-: à- cf ästenisn.
534:apa-sistan ['psstn'] apčsistan [’pysstn'] apa-sih- ['psh-, *psyh-] or apésih- ['py- syh-], to be destroyed, annihilated: bē apasihet will be annihilated, of Ahriman 644, of the wicked 103! (in both passages ’pshyt' in the printed editions); — bē apäyet apesihät (subju. 3d p. sg.) vis ? Pourusäsp the manor of P. (must be =) is evidently going to be destroyed 441°; nē be apesistan <i> vis 1 Pourušāsp rād not in order that the manor of P. might be destroyed 4421. My spellings apasihät, apasistan in Dk are to be corrected; the scribe of the Dk MS (now available in re- production) constantly writes all forms of this vb. and its derivatives ’pys-, keeping the two letters y and s distinct with a care not very common in Phl. writing (in 441° he wrote by a slight slip of pen ’p’s- instead of ’pys-). The form apēsīhāt 441° is directly confirmed by MPrs ’bysyh’d (S). — < apa- + Av. (1547) saéd-, pres. pass. "apa-sidyati > Milr *apa-siy-é > apa-sihet or apa-styy-ēt > apa-siyét > apasthét; Paz. awasihed, awasthend; M Prth ?bsyst ‘dried’, Ghilain 83. The form with -ē-: apésihét etc. goes back to *apa- hisidyatt with pres. reduplication (cf Av. ava-hisióyat which is, however, perf. opt.). The active pres. ‘to destroy’ was *apa- sind- > apa-sinn- (always spelt ’psyn-): apa-sinnčt, apa-sinnisn (Paz. awa-sinasn) ; from this are formed the secondary infini- tives apa-sinnitan (BdJ 15%, apésinni- tan (Mx 2771), apasinnistan (KnA 79). Bal sinday ‘to break’, Skr chid- (< Id.- = europ. aci pres. chinad-, chind- (Lat.
554:apäyistan ['p'dstn'], apāyītan [’p’dytn'] apäy-, 3d p. sg. apāyēt [’p’dt', ^p'dyt'], 3d p. pl. apäyend ['p'dynd], pret. 3d p. sg. apāyist 1. to please a p. (pat) 83%; cigon mēnēyān apäyist as it had pleased (was predestinated by) the heavenly gods 405, v. below. — 2. impers. it is desirable: -m apāyēt 6 han ciš I desire, try to obtain, this 562%, — 3. to be needed 1211-2 also pat. kär. apāyet 14%. 375, andar apāyēnd 105%. — 4. to be proper, seemly 4015 (bē ~). — 5. impers. apäyet auxiliary vb.: must, ought to, shall, should, has to, is bound to, ete. with the p. as indir. obj. (virtual dat.), a) governing an inf., which is as a rule placed after: u api-t xvatāyēh i Ērān šahr vas sal apäyet kartan and thou shalt exercise dominion over Iran for many years 629-31; 918-19, ]014 ete.; in this case preverbs to the inf. are drawn to apäyet; bé — pursitan 1319; ba ~ hištan 1313; kār-ē i apar nē ~ kartan 104%; apārīk 6 [KN] ~ xtartan 94??; less often the inf. is placed before: ēzatan nē ~ 1017-19; pit u mat frazand i xueš rād En and kär u kirpak ... bē üámóxtan ~ the parents shall teach 6522-23; 6519-20; 9113; the inf. sometimes has to be supplied: -
557:urvar har cé ne ~ (se. hösitan) à nē hošet 9612-13, 9810-11; — apāyet būtan it is bound to happen, of predestination, explains jäyisn 271, brihenisn 16°; used itself as a nominal expression of Predestination: apäyet-bütan rād 16!!; — b) taking a v. n. as its complement: -šān ... gošt z"arisneh ne — it is not allowed for them to eat meat 10420-21; — e) governing a subordinate clause introduced by kū 8!. 1181-14 by ka 56?? (gl); without an introductory particle, with the governed vb. in ind. or in Subju.: ~ stdyé thou shalt profess 596; bē ~ apesihät 4419-19, v.s. v. apa- sistan. — MPrs ’b’yd with inf. (A-H II); Paz. āwāyastan āwāyad; āwāyastaa ‘re- quisite, desire’ (SGV); NP bäyistan, bā- yad; andar-vdi ‘desire, need (cf above no. 3; to be distinguished from andarvāt ‘atmosphere’, g. v.). Den. of OIr *updya- < *upa-aya- ‘that which comes upon, is imposed upon, affects a p.' = 1. need, 2. duty, cf Av. (150) upa-ay-, v. HP II, 17 sg.; Verbum 168; Ghilain 48. apāyišnīk ['p'dányk] proper, fit, fitting, handsome, nice, exquisite, comp. ~-tar, 33-5. 422, etc. passim; pl. cas. obl. ~-dn the qualified ones 1052,
835:reluctancy: atün hàn i kart (v. ?kartan) ~ dahét he will create unwillingness with regard to what you have instituted 45), with the following gl. explaining ~: kū šmāh xvēš rād ne tuvān zuästan, kas šmāh rād ne xvāhēt ‘~ means that you are incapable of an act of will for your own sake and nobody will be willing (to act) for your benefit’ (you will be diffident and inefficient, and nobody will work for you) 45*3; the gist of Yam's speech is expressed in the gl. 452, v. acārēnītam.
909:band [bnd] tie, band, bond; fetters 919. 34! (81? probably mistaken for bry<n> = brin, cf Mx ch. 279; Paz. is wanting); ~ + zēndān imprisonment, captivity 9°; ~ the snare of Death 6514-18; ca rād ka menčyan u gētīkān dänisn u kār-ākāhēh har 2 band 6 tč [i.e. xrat] patvast why are knowledge and skill of both the heavenly and the earthly beings (so) closely tied up with (dependent on) thee [the Wisdom]? 8811-12; the Skr. v. joins band with the preceding har 2: dvdvapi bandhau, but this is contradicted by 12017-18; cigön martömäan i andar gété band 6 mēnēyān patvast estet as men in this world are closely tied up with the heavenly beings. — Av. (926 sq.) banda- ; MPrth. bnd; bndys?n ‘prison’ (MHC); MPrs bnd (A-H II), bn = bann (S, A-H I), bnyst’n = bannistän < band- (A-H I); Paz. NP band. V. bastan.
1075:xueseh api-š han and hir rād 4544-4; u... Wo... u -c: Mar u gazdum u apārīk-ic arafstr 76°; only -c with the last w.: andar hindükän hrom apdrik-ic damikihä 109 (apärik ‘etc.’ often asyndetically added); with negation: ké-§ ciš-ic pat pēc nēst man-ic [LY-c!] nest 1022; nē... u nē-c 1220.21. nE... U NĒ... u ne-c „2119-29. — 2. emphasizing particle: nün-ic K Bi: ‘etei, iu 'ahanün- -ic, hambun-ic, dit-ic,
1117:cê [MH; cyh 12111] 1. interrog. pron. what? 59. 726. 89? ete.; how? 1513, 51?!; with prep. 6 cé, pat cé, hac cē; cé rād? why? 351! ete.; combined with a subst.: ce zaman? 715, cē gah? 722; pat ce āivēnak? how? 76%; cé vinäs? 121, cē vat? 7322, etc. ; apar cē ātvēnak margēnītan i Zartuxst pursit how to kill Z. 4912-25-26, 4813-14 (apar governs the whole clause). — 2. rel. pron. what: či ndmakY ce ... nipištv estet, ce Šahpuhr" . . . framätY nipigstany P 2:3-4; kart" ... ce ... sahät P2:8-9; har ce 61.3218, 86%. 9618; ēt ce ... apāc āvurt 11214715; 361; pat hàn cim rād ce 121". — 3. conj. a) subordinating: because 105); ce ka id. 991. — b) coordination: for 2$. 619.22. etc., passim. — MH 305 wrong ideogr. for encl. -c(%). — < cahya, gen. sg. of Av. OP (422 sq.) ka-.
1128:cihčnitan [cyhynytn'] to make known, to teach, to announce; ētšān O$-c rād cihenit ku . they announced about him that ... 37’, with the gl. kū-šān guft; pres. pass. nč be cihiyom [cyhywm]: I am not informed 51°, with the gl. ku né dānēt, cf s. v. apasthistan, — Paz. cthini- dan Skr. v. jūā- (Aog.); from Av. (428) kač0- ‘to teach’.
```


## [2026-09-14T01:30:52.303Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5391,5405p' HRN.txt; echo \"=== leaf/page\"; awk 'NR<=5391{n+=gsub(/\\f/,\"\")} END{print \"leaf\",n,\"printed page\",n-21}' HRN.txt"
}
```


### [2026-09-14T01:30:53.427Z] TOOL RESULT

```
601. räd 'freigebig.
aw. vergl. aräiti-^); ai. rati- Villig zu geben'; phlv.
rat (auch Titel, vergl. Hörn, Mitteilungen, Heft IV,
27), ratth.
602. räz geheim, verborgen'.
aw. razah' (vd. 8, 97); phlv. raz^ vergl. Qaovav^
Chron. Pasch. I, 730, 14, 15 (de Lagard e, Ges. Abh.
192) ; skr. rdhas- 'Einsamkeit, Geheimniss'.
603. rast recht, wahr, rechts*, 7'äste^ rastl, rästln (Sahn. I,
123 Vers 1070).
ap. rasta- recht, richtig'; aw. rasta--, phlv. rast,
rastlh\ ai. raddhd-,
oss. d. t. rast^ rasf (212).
LW. kurd. af/. bei. (222) rast; wa./. rast, ssiv, rüst.
604. räm *Ruhe; fröhlich, heiter, ramis, ramist (Lex.).
=== leaf/page
leaf 155 printed page 134
```


## [2026-09-14T01:31:14.853Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### SKT ripple\"; grep -n \"^ripple\\|ripple, \" SKT.txt | head -5; echo \"### SKT rope\"; grep -n \"^rope\\|rope, a cord\\|Rope\" SKT.txt | head -5; echo \"### SKT row\"; grep -n \"^row (1)\\|row, a line\\|Row\" SKT.txt | head -5; echo \"### SKT ripe\"; grep -n \"^ripe\\|Ripe\" SKT.txt | head -5"
}
```


### [2026-09-14T01:31:14.965Z] TOOL RESULT

```
### SKT ripple
16136:ripple  (I),  to  pluck  the  seeds  from flax-stalks.  (Sciind.)  ME.  ripplen,  ripeUn^ to  ripple  :  from  the  sb.  ripple,  a  llax- comb  (Jainieson).  Formed,  with  suffix  •//, of  the  agent,  from  Swed.  repa,  lo  ripple flax,  orig.  to  scratch,  rip  :  see  rip  (above). •4-Du.  repelen,  to  ripple,  from  rtp^l,  a ripple,  from  repen,  to  beat  flnx ;  G.  riffeln, to  ripple,  from  riffel,  a  ripple.
16137:ripple  (3),  10  graze  slightly.  (Scind.) ' Kipp!e,  rtsciuderc;*  Levins  (1570).  Fic- quenlative  of  rip  (above).
### SKT rope
16208:Rope.  (E.)  M.  E.  roop.  A.  S.  rdp.  + Du.  rtep,  Icel.  reip,  Swed.  «/,  Dan.  reb\ G.  rtif,  circle,  hoop,  ring,  sometimes  a rope.     Der.  rop-y,  stringy,  glutinous.
### SKT row
548:adoleseont.  Rowing  op.  (L.)  L.  aJo- iacmf;  stem  of  pre?,  pt,  of  adoleseert,  to STOW  op.  —  L  a.if  to ;  oleseert,  inceptive lonn  01  ttiin^  to  grow,  from  atertt  to nourish.
2694:oampestral,  Rowing  in  fields.  (L.) L.  camficitr-is^  growing  in  fields. —  L.  cam- pus,  a  field.
12537:tf.E.  M«:  A.S  .Jr  ^Du. ;  n^.  «f.  Swcd.  ^i.  G.  tirA^ ; If.  ^Kot  allied  to  a^ffm. Comb. £.  rrr:  A.S.  tfr.'f-Icel. ilfix,  Furthnr  altinl n.  (p-fT/uif«L.  r^ irl/as,  au  o»r,  />-/i, tr'ttro,  a  paddle,  nidder. Row.
16163:Koaa-tree,  Rowan-tree,  the  roouo- tftin  ash.  (Scand.)  Spelt  rQun-trtt,  roan- trtt,  rotvart-treein  Jami«on.  — Swcd.  ronn, O.  Swcd.  rutin,  ronn,  roas'trec ;  Dan.  ron, Iccl.  rtynir,  the  some.  Cf.  L.  emm,  the same.
16250:Row  (j),  to  propel  with  oars,  (E.) M.  £.  ytWCTt.^A.  S.  r^wan,  to  row.  4- I^u. rocijfn,  Iccl.  rda,  Swcd.  ro,  Dan.  r$€, M.  H.  G.  rucjen.  Allied  to  Skt.  an'/ra,  a paddle,  rudcfer,  Lithuan.  irfi,  to  row;  Gk. ip^Tti6t,  a  paddle,  oar.     (^  AR.)
### SKT ripe
15705:ripe.  (E.)  M.  E.  rip*.  A.  S.  W/V,  fit for  reaping;  cf.  rip,  har\est.  — A.  S.  ripan» to  rcap.+  Du.  ny/,  G.  reif,  ripe.
16119:Ripe ;  see  Beap.
```


## [2026-09-14T01:31:16.920Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### KLN ripple\"; grep -n -o \"ripple[^.]\\{0,220\\}\" KLN_1966.txt | head -6; echo \"### KLN ripa/river\"; grep -n -o \"rīpa[^.]\\{0,160\\}\" KLN_1966.txt | head -4; echo \"### KLN res\"; grep -n -o \"L\\. rēs[^.]\\{0,160\\}\" KLN_1966.txt | head -4"
}
```


### [2026-09-14T01:31:18.095Z] TOOL RESULT

```
### KLN ripple
3139:rippled’, fr
3139:ripple  by  a  stroke’
6289:rippled’  (lit
9621:ripple,  croft,  crop,  crumple
9698:ripple,  n
9698:ripple’,  MHG
### KLN ripa/river
### KLN res
```


## [2026-09-14T01:31:27.969Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '9698p' KLN_1966.txt | cut -c1-700; echo; echo \"=== KLN river\"; grep -n -o \"river,  n[^§]\\{0,300\\}\" KLN_1966.txt | head -2; echo \"=== KLN res/real\"; grep -n -o \"L\\.  res[^§]\\{0,200\\}\" KLN_1966.txt | head -3"
}
```


### [2026-09-14T01:31:29.113Z] TOOL RESULT

```
Crinum,  n.,  a  genus  of  plants  of  the  amaryllis family  ( bot .)  —  ModL.,  fr.  Gk.  xptvov,  ‘lily’, which  is  a  foreign  word  of  unknown  origin.  Cp. the  first  element  in  crinoid. crio-,  combining  form  meaning  ‘ram-headed’.  — Gk.  xpto-,  fr.  xptoc,  ‘ram,  battering  ram’,  which prob.  stands  for  *xplf6?  and  is  rel.  to  xepa6?, ‘homed’,  fr.  xspai;,  ‘horn’,  and  cogn.  with  ON. hreinn,  ‘reindeer’.  See  horn  and  cp.  cerato-,  cer¬ vine.  Cp.  also  the  first  element  in  reindeer, criosphinx,  n.,  a  sphinx  with  the  head  of  a  ram.  — Compounded  of  Gk.  xpf6<;,  ‘ram’,  and  aeptyi;, ‘sphinx’.  See  pr

=== KLN river
32980:river,  n.  —  ME.  rive  re,  fr.  OF.  rivere,  riviere, ‘land  lying  along  a  river;  river’  (whence  F. riviere,  ‘river’),  fr.  Late  L.  riparia  (scil.  terra), ‘land  lying  along  a  riverbank’,  fem.  of  riparius, ‘of  a  riverbank’,  fr.  ripa,  ‘riverbank,  seashore’. See  riparian  and  cp.
=== KLN res/real
3499:L.  res¬ tore,  ‘to  stop’,  fr.  re-  and  stare,  ‘to  stand’.  See slate  and  cp.  rest,  ‘to  remain’, arrest,  n.  —  ME.  arest,  fr.  OF.  arest  (F.  arret), back  formation  fr.  arester  (F.  arre
9275:L.  responded,  ‘to answer’.  See  respond.
23150:L.  resfacti. Cp.  G.  Tatsache,  which  is  the  loan  translation of  E.  matter  of  fact.
```


## [2026-09-14T01:31:33.698Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -o \"riparian,  adj[^§]\\{0,330\\}\" KLN_1966.txt | head -2; echo \"=== republic\"; grep -n -o \"republic,  n[^§]\\{0,300\\}\" KLN_1966.txt | head -2; echo \"=== real\"; grep -n -o \"real,  adj[^§]\\{0,300\\}\" KLN_1966.txt | head -2"
}
```


### [2026-09-14T01:31:34.862Z] TOOL RESULT

```
32959:riparian,  adj.,  pertaining  to  the  bank  of  a  river.  — Formed  with  suff.  -an  fr.  L.  riparius,  ‘that  which frequents  riverbanks’,  fr.  ripa,  ‘riverbank,  sea¬ shore’,  which  is  prob.  cogn.  with  Gk.  ipelneiv, ‘to  tear  down’,  epiTrvr,,  ‘a  broken  cliff  or  crag’, ON.  rifa,  ‘to  tear,  break',  MHG.  rif,  ‘river- 
=== republic
32432:republic,  n.  —  F.  republique,  fr.  MF.,  fr.  L.  res publica,  respublica,  ‘state,  commonwealth’,  lit. ‘a  public  thing’,  fr.  res,  ‘thing’,  and  fem.  of  pu- blicus,  ‘public’.  See  real,  adj.,  and  public. Derivatives:  republic-an,  adj.  and  n.,  republic¬ an-ism,  n.,  republic-an-ize,  t
=== real
3301:real,  adj.,  1)  of  a  tree  or  trees;  2)  living  in trees.  —  Formed  with  adj.  suff.  -al  fr.  L.  ar- boreus,  ‘pertaining  to  a  tree  or  trees’,  fr.  arbor. See  arbor,  ‘tree’.
5372:real,  adj.,  pertaining  to  Boreas;  northern.  — L.  borealis,  fr.  boreas.  See  next  word  and  adj. suff.  -al.
```


## [2026-09-14T01:31:46.227Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -o \"real,  adj\\.,  actual[^§]\\{0,260\\}\\|realis[^§]\\{0,160\\}\" KLN_1966.txt | head -3; echo \"=== LAT res\"; grep -n -o \"rēs, *rĕī[^§]\\{0,300\\}\\|res, rei[^§]\\{0,300\\}\" LAT.txt | head -3; grep -n \"^res\\b\\|^rēs\\b\" LAT.txt | head -5"
}
```


### [2026-09-14T01:31:47.427Z] TOOL RESULT

```
4001:realis,  the  Northern  Lights.  —  L.,  lit. ‘northern  dawn’.  The  term  was  introd'AAby Gassendi  in  1621.  See  aurora  and  bort aurum,  n.,  gold  (term  of 
5372:realis,  fr.  boreas.  See  next  word  and  adj. suff.  -al.
7020:realis,  dissimil.  fr. *Cereralis,  ‘pertaining  to  Ceres',  fr.  Ceres,  gen. Cereris,  ‘Ceres’,  name  of  the  Italian  goddess  of agriculture,  prop,  ‘goddess
=== LAT res
10793:res ); b. lat. accessibilis.
17027:res, sic in oratione qui facit, disertus ; de nene Cic., De Or. 1,340;
20522:res familiaris, patrimonium - , familia englobe les res mancipi, l'en-
20530:res familiaris-, puis par extension "familier"; subst. fami l iaris m.:
22024:res ne facit festinem. La forne poarrait etre toutefois le subj. de
```


## [2026-09-14T01:31:47.657Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Besitz, Sache\\|rēi-\\|rei- .ritzen\\|ritzen, reissen\" incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt | head -10"
}
```


### [2026-09-14T01:31:47.755Z] TOOL RESULT

```
22337:1. rei- „ritzen, reiSen". Zsfassung der Erweiterungen bei Persson Beitr. 334 f., 
22861:„locker, undicht'' und '"rei- „ritzen, reiBen'^ s. unter letzterem. Zu-
```


## [2026-09-14T01:31:51.008Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '22337,22380p' incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt; echo \"=== search rei- Besitz in Bd2\"; grep -n \"Besitz, Sache\\|ai. räh\\|räyah\" incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt | head -5"
}
```


### [2026-09-14T01:31:51.127Z] TOOL RESULT

```
1. rei- „ritzen, reiSen". Zsfassung der Erweiterungen bei Persson Beitr. 334 f., 
773, 839, 840, 842; daS aber *rei- eine Erweiterung von er(e)- „locker, 
undicht" sei (s. d, : aksl. oidti „lvaiv, xa'datgaTv^' sei noch zweisilbiges 
*erei-), ist mindestens ganz nebelhaft und wird nicht durch genauere 
Bedeutungsiibereinstimmung naher geriickt. 

Lett, rhoa „Schlitze, Ritze im Holz, Falte, Runzel, Furche", lit. reici 
„Felskluft, Fels, Riff" (vgl. rnpes : riimpo), auch „Hugel" (wohl sekundar), 
rem „Geader im Stein oder Holz, Streifen, Gang durchs Getreide", raiv'e 
„Streifen" (s. auch Persson Beitr. 773 Anm. 2; die Bed.-Entw. ,, Ritze, 
geritzter Strich, Streifen, Reihe" auch in der Erw. rei-k-, s. u.) ; ob ags. 
rdiv, row ,,Reihe" als "^roi-ua hieher (Trautmann ZfdtWtf. 7, 268) oder als 
"^roik-iid zur Erw. reik- geh5rt (Zupitza Gutt. 67 f.), ist unentschieden. 

Als (Grenz)streifen oder Hugelreihe" allenfalls hieher anord. rein .jgras- 
bewachsener Grenzstreifen zwischen Ackern", ahd. rein ds., Hain „Boden- 
erhebung als Grenze", air. roen „Weg: Bergkette", bret. run ,,Hugel" 
(Persson Beitr. 773; Fick 11^234, Pedersen KG. I 58). — Lat. rlma ,, Ritze", 
an sich auf '^rei-ma (Persson Beitr. 773) oder "^reid-ma (: aschw. rlta 
„ritzen", s. u. rei-d-) zuruckfiihrbar (auch auf "^ureid-ma ; ags. writan „ritzen, 

23 " 



344 rei- 


schreiben" Sommer Hdb.^ 231, Boisacq 274 Anm. 5), ist am ehesten ^reik- 
sma (:ndl. reesem „Liiiie, Eeihe*' aus "^roiTc-smo-; Froehde KZ. 22, 264, 
Yf. LEWb.2 S.V.). 

Erweiterungen: 

~:ai. rikhdti, likJidti „ritzt“, rekhd, lekhd „Ei6, geritzter Strich, 
Linie, Streifen, Eeihe“. Gr. igelxco „zerbreche, zerrei6e“, ijgixe „barst“, 
igsixlg, sQixig^, -tdog „geschrotete Gerste“ (-t-SchreibuDg fiir wie in 
igixdg'd igey/Lcog Hes.; das -e- von egeyjLia, egey/uog neben egiyjLia n. „ge- 
schrotete Hiilsenfriichte" ist wohl verderbt). Yielleicht lat. riooa „tatlicher 
Zank, Streit“ (Persson Wzerw. 103 Anm. 2; kaum nach Holthausen IP. 25, 
151 zu *uer-, "^ureik- „drehen“; noch anders Trautmann Apr. 415). Cymr. 
rhwygo „zerreifien“, rhwyg m. „Bruch, Spalte“, mbret. roegaff „zerrei6e'', 
nbret. reuga (Pick II* 228). 

=== search rei- Besitz in Bd2
```


## [2026-09-14T01:31:59.497Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"raevant\\|räti- „Gabe\\|rati- „Gabe\\|rayi-\\|rdyi-\" incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt | head -10; echo \"=== rei- geben\"; grep -n \"rei- „Besitz\\|„Besitz\\\"\" incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt | head -10"
}
```


### [2026-09-14T01:31:59.583Z] TOOL RESULT

```
22327:rayidi „Gabe, Besitz, Kleinod“, revant- „reich'*, av. raevant ds., av. ra- 
=== rei- geben
29686:son IF, 2, 7 f., Liden Stud. 55 Anm. 1 m. Lit.; air. selb, cymr. hclw „Besitz"
```


## [2026-09-14T01:32:02.313Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '22315,22337p' incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt"
}
```


### [2026-09-14T01:32:02.377Z] TOOL RESULT

```
grimm“ (nicht aus "^rout-^ wie Holthausen IF. 20, 328 f,). Ygl. Fick III^ 
347 {rop), s. auch unten S. 351. 
reb- „rulpsen“; 

norw. dial, rcepa „den Mund laufen lassen“ (^repjan), rapa „rulpsen‘^; 
altn. repta {^rapatjan) „rulpsen^^ (daneben rypta aus ^rupatjany s. retig^p 
Fick lU^ 337 {rap), Falk-Torp 928 {rcebe), 

2* re(i)- „geben; Sache'^ 

Ai. ratif rasate „gibt, verleiht, gewahrf' {rir'Jii, raridhvam), rah „Gut, 
Schatz, Eeichtum‘‘, rati-h „Yerleihung, Gunst'" (oder auch zu idg. le(i)l), 
rayidi „Gabe, Besitz, Kleinod“, revant- „reich'*, av. raevant ds., av. ra- 
„gewahren, spenden“; ai. rata-h, av. rato „dargebracht“. Lat. res (= ai. 
rah), rei „Sache‘‘; umbr. re-per „pro re'', ri abl. dat. Hierher lat. reus „der 
Angeklagte", alter Gen. auf -os (^rews)', reios est bedeutete „er ist am ProzeB 
beteiligt" (Thurneysen IF. 14, 131). 

Die kelt. Anreihungen bei Fick II ^ 225 sind unrichtig, vgl. Yf. LEWb.^ 
650. Ebenso abzulehnen die Yerbindung von lat. rUs mit gr. yorj oder lat. 
horior (Frohde KZ. 22, 251, Fick I ^ 436). 

1. rei- „ritzen, reiSen". Zsfassung der Erweiterungen bei Persson Beitr. 334 f.,
```


## [2026-09-14T01:32:14.639Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==592' IEC.txt | grep -n -o \"rīp-[^\\n]\\{0,300\\}\\|roipos[^\\n]\\{0,200\\}\" | head -5; echo \"===\"; grep -n -o \"raipaz\\|reipos[^,]\\{0,120\\}\\|roiua[^,]\\{0,120\\}\" IEC.txt | head -8"
}
```


### [2026-09-14T01:32:15.768Z] TOOL RESULT

```
17:rīp- (urīp-) Gk. ereípo, v. ‘dash, destroy’; cf. ereípion, n. ‘ruin, shambles’; OFris. riva, sv. 1. ‘snatch’; ON rifa, sv. 1. id. (and 'téar); Sw. af-riva, id.; ME riven, sv. 1. ‘split, têar’; cf. OE rif, adj. ‘violent, fierce’; s. 'garment.. (Isophone: Bis. ripam, v. “hop, jump")
===
```


## [2026-09-14T01:32:19.902Z] TOOL CALL #75: Bash

```json
{
 "command": "grep -rl \"Rekp\" data/extracted/batch/ | head; echo \"---\"; grep -ro \"\\\"name\\\": \\\"Rekp[^\\\"]*\\\"\" data/extracted/batch/ | head; echo \"--- index\"; grep -rn \"Rekp\" data/extracted/batch/ | head -5"
}
```


### [2026-09-14T01:32:20.015Z] TOOL RESULT

```
data/extracted/batch/page-420.json
data/extracted/batch/page-419.json
---
data/extracted/batch/page-420.json:"name": "Rekp"
--- index
data/extracted/batch/page-420.json:66:        "name": "Rekp",
data/extracted/batch/page-419.json:66:        "gloss": "to scratch, tear, cut; Rekp: to pull, break"
```


## [2026-09-14T01:32:22.429Z] TOOL CALL #76: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/extracted/batch/page-420.json'))\nfor e in d['entries']:\n    print(json.dumps(e['root'],ensure_ascii=False))\n\""
}
```


### [2026-09-14T01:32:23.518Z] TOOL RESULT

```
{"name": "Rek, Reg 2", "lang": "Indo-European", "refs": "POK:863; WLD2:362", "gloss": "to tie"}
{"name": "Rekp", "redirect": "Rei 2"}
{"name": "Rěkto", "redirect": "Reg 1"}
{"name": "Rem", "lang": "Indo-European", "refs": "POK:864", "gloss": "to rest"}
```


## [2026-09-14T01:32:51.459Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"letter\" SOD.txt | head -20"
}
```


### [2026-09-14T01:32:51.521Z] TOOL RESULT

```
3674:transliteration  in  bold  letters  and  in  Sogdian 
3687:Capital  letters  in  the  transliteration  denote 
3689:with  or  without  the  letter(s)  in  the  parentheses  are 
4274:souls".  These  letters,  which  could  not  have  been 
4464:These  letters,  which  are  probably  the  oldest 
4472:towers,  Stein  found  a  bundle  of  letters  together  with 
4475:20  ax>.  The  eight  letters  on  paper  contained  writing 
4478:palaeographical  evidence,  Stein  dated  the  letters  as 
4485:the  letters  in  the  second  volume  of  his  work  on  the 
4491:the  letter,  its  date  as  190  ad.  In  1948,  Henning, 
4922:letters,  "Problem  der  Interpretation  Manichaisch- 
5384:secular  materials  such  as  letters,  legends  on  coins, 
5428:non-religious  letters,  documents  and  inscriptions,  as 
5481:Livsicl04.  The  alphabet  consists  of  the  22  letters  in 
5482:the  traditional  Aramaic  order  (although  four  letters 
5486:fact  that  this  letter  represents  two  distinct  phonemes, 
5551:special  letters  fi  and  6  (borrowed  from  Sogdian 
5584:characters  /,  x,  z  to  the  22  letters  of  the  Syriac 
5601:are  written.  Beside  secular  materials,  such  as  letters, 
5848:letters  provide  evidence  for  the  existence  of  two
```


## [2026-09-14T01:32:58.797Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>5800 && NR<6600 && /^[ ]*[0-9ivxl]+[ ]*$/ {print NR\": \"$0}' SOD.txt | head -20"
}
```


### [2026-09-14T01:32:59.914Z] TOOL RESULT

```
5857: xxxi 
6204: xxxiv
```


## [2026-09-14T01:33:44.383Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^\\*raiš\\|\\*raiš ‘\" CHEUNG.txt | head; echo \"---\"; grep -n \"raiš\" CHEUNG.txt | sed -n '1,12p'"
}
```


### [2026-09-14T01:33:44.460Z] TOOL RESULT

```
---
12901:Sariq. rizd ‘pain’ (rather *raiš ?) || (+ *pati-) Yghn. d’ris-/drista ‘to tear, to be torn 
28207:its rise is that it denotes the physical state (Kellens, l.c.), cf. *raiš. Since both
```


## [2026-09-14T01:33:46.624Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '12860,12920p' CHEUNG.txt"
}
```


### [2026-09-14T01:33:46.687Z] TOOL RESULT

```
*SANSKRIT: ray ‘to flow, drip, run, bubble up’ (RV+) > EWAia II: 437 

© The Ir. cognate root of Skt. ray has become an euphemism for ‘to defecate’, 
replacing forms of a root that was no doubt considered uncouth, possibly *zad 
(Y Av. zadanha (pl.) ‘backside, anus’, cf. Skt. had, EWAia Ш: 532). 

PIE *HoreiH- ‘to flow, stream’ > LIV: 305 | Pok.: 330 f. 

*IE COGNATES: Gr. ópívo ‘I bring in commotion, confuse’ (influenced by ópvuju ?), 
Lat. rivus (m.) ‘brook’, Olrish rian ‘river, sea’, Russ. réjat’ ‘to stream fast, flow’, 
rinut’ ‘to stream, to flow’, Cz. finouti se ‘to stream, to flow’ 


*Hraiz 189 


«REFERENCES: EVP: 63; Abaev, Slovar’ П: 54; DKS: 363b f., 364a; WIM 1988: 115; Werba 1997: 371; 
Lecoq 2002: 611a; Shahbakhsh: s.v. ri(h/y)-; Korn 2005: 233, 316, 378 


*Hrais ‘to be torn, tear, cut, split’ 

*KHOTANESE: (+ *fra-) harät’- (hars-) ‘to burst || (+ *ui-) birät’ ‘to split, burst’ 
= SGS: 149, 98 

*SOGDIAN: (+ *uz-) BSogd. zr’ys- (intr./pass.) ‘to be severed, interrupted’, BSogd. 
zr’ys- (tr/caus.) ‘to sever, interrupt, destroy’, MSogd. zrys- ‘to hurt’, CSogd. 
zrys-’sy ‘coming to an end, about to perish’ (Sims-Williams 1985: 99, fn. 28) || (+ 
*pati-) MSogd. ptrys ‘to tear away’, BSogd. ptr’ySky ‘tearing away’ 

(+ *uz-) Pres.: OPT. 3sg. BSogd. zr’ys’y; Impf.: IND. 1sg. MSogd. zrysw (ВВВ: 33); Partic.: perf. pass. 
MSogd. zrystyy (BBB: 33); Inf.: *zryš (BBB: 33); Caus.: pres. IND. 3sg. BSogd. zr’yst || (+ *pati-) Impf.: 


IND. 3sg. MSogd. ptyrys (BBB: 45); Partic.: perf. pass. MSogd. ptrystyy (BBB: 33); Inf.: MSogd. ptrys 
(BBB: 33) 


*CHORESMIAN: rYs- ‘to scold аб = Samadi: 176 

*NEIR: Oss. I. lyst(zeg), D. list(ag) ‘fine, in pieces’, I. lystaen, D listen ‘litter’, ? 
Sariq. rizd ‘pain’ (rather *raiš ?) || (+ *pati-) Yghn. d’ris-/drista ‘to tear, to be torn 
(off || (+ *ui-) Sh. wirdx-t, Rosh. wirix-t, Bart. wiriX-t ‘to cut a piece’, Yzgh. wrix-t 
‘to slit up, slaughter’ 

*SANSKRIT: res/les ‘to tear off, pluck’ (RV+) = EWAia II: 461 

«PIE *Hirei-K- ‘to cut, split, tear’ ? = LIV: 504 | Pok.: 858 

*IE COGNATES: Gr. ёрєїкө ‘I break, tear off’, MWelsh rwyg-, MBret. roeg- ‘to tear’ 
*REFERENCES: Andreev — PeSéereva: 247a Ё; EVS: 71b, 92b; Abaev, Slovar’ П: 57 Ё; Werba 1997: 228 


*Hraiz ‘to shake’ 

*PARTHIAN: 0 On ryzynd see *raiz?. 

*KHOTANESE: rriys- ‘to tremble’ || (+ *abi-/*ui-) bär(r)iys- (biriys-) ‘to shake’ || (+ 
*fra-) OKh. hariys- ‘to tremble’ = SGS: 116, 99, 149 f. 

*NEIR: Oss. I. rizyn/ryzt, D. rezun/rizt ‘to shake’, Pash. reZdedol ‘to shake, tremble’ ||
```


## [2026-09-14T01:33:57.023Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"raes\\|raēš\\|irista\\|iriO\" CHEUNG.txt | head -15"
}
```


### [2026-09-14T01:33:57.105Z] TOOL RESULT

```
2733:*NWIR: NP biristan ‘to roast’, biryan ‘roasted’, Bal. brétk/brej- ‘to roast, fry, parch’, 
8137:*NWIR: NP giristan/giriy- ‘to weep’, NP gilah ‘complaint; lamentation’, Kurd. 
8735:(BKYWN-) /griy-/ ‘to weep’, NP giristan/giriy- ‘to weep’, deriving both from a root 
11006:fraesiiamahi (Vr 22.1, P 3(34)); Partic.: pres. {1} YAv. paitisant- (P 12 (13), Vyt 52), med. (ad hoc?) 
11032:*NWIR: (+ *fra-) Zaz. ristis/risen- ‘to send’, (old caus. ppp.) NP firistah/firestah 
20292:*AVESTAN: Y Av. raes- ‘to get hurt, suffer damage’ = Liste: 59 
20300:15.22, V 15.40, Vyt 44); Caus.: pres. IND. 3sg. Y Av. "raesaiieiti (V 5.12), SUBJ. 3sg. YAv. raesaiiat (V 
20331:59.21 f£, Vr 11.7), med. YAv. iririüana- (Р 23, P 34), perf. pass. YAv. irista- (Yt 13.9, Yt 19.11, Yt 
21275:keep, protect’, Yzgh. saj-/saxt ‘to prepare (a bed, etc.) || (+ *fra-) Oss. D. raesazun/ 
23199:sraiian'ha (Yt 17.21); Fut.: IND. 3sg. YAv. sraesiieiti (V 8.34); Aor. athem.: INJ. med. 3sg. YAv. nisrita 
23260:*NWIR: NP siristan/sirés- ‘to mix, mingle; knead’, Gz. siris-/sirist ‘to knead the 
23530:*fra-) NP firistadan/firist-, Bal. Sastit, Sastit, Sasta0-/Sast-, Sast- ‘to send’, Ard. 
33614:pairiOna-, 154 
33660:raes-, 308 
40831:biristan, 23
```


## [2026-09-14T01:33:59.279Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '20285,20330p' CHEUNG.txt"
}
```


### [2026-09-14T01:33:59.360Z] TOOL RESULT

```
*IE COGNATES: Gr. Aınatvo ‘I oil’, Aınapog ‘fat, oily’ Lith. тро (lipti) ‘I stick’, 
Russ. lipkij ‘sticky’ 

*REFERENCES: Abaev, Slovar’ I: 543; Werba 1997: 228 


*rai§ ‘to suffer (damage, illness)’ 
*AVESTAN: Y Av. raes- ‘to get hurt, suffer damage’ = Liste: 59 


*га102 309 


Pres. ja-: IND. 350. YAv. irisiieiti (V 13.38, V 15.4, V 15.6, V 15.8, etc.), SUBJ. 3sg. YAv. irisiiat (V 
7.38, V 13.37, V 15.4, etc.), 3pl. YAv. irisiian (V 15.22, V 15.40); Partic.: pres. YAv. irisint- (V 15.12, V 
15.22, V 15.40, Vyt 44); Caus.: pres. IND. 3sg. Y Av. "raesaiieiti (V 5.12), SUBJ. 3sg. YAv. raesaiiat (V 
15.11, Vyt 44) 

*MIDDLE PERSIAN: BMP lys- /rés-/ ‘to wound, hurt’ 

*NWIR: NP res ‘wound’, also borrowed into Kurd. ris, Bal. res ‘id.’ 

*NEIR: Oss. I. rissyn/ryst, D. resun/rist, Wa. riZ/rizd- ‘to be ill’, (caus.) 
riZ(bI)v-/riZovd- ‘to cause illness’ (pres. -Z- from pret.), Oss. I. ris ‘illness’, Wa. rizg 
‘illness, disease’, ? Sariq. rizd ‘pain’ (rather *rais ?) || (+ *upa-) Pash. bréx (m.) 
‘twitch of pain, cramp, spasm’, ? Sh. biréj ‘a worm dangerous for sheep’ (< 
*upa-raisa-Ci- ?) 

*SANSKRIT: res ‘to get harmed, hurt’ (RV+) = EWAia II: 462 

9 The root appears to be exclusively Ш. 


*REFERENCES: Horn 1893: 142; EVP: 15; MacKenzie, Pahlavi: 72; Abaev, Slovar’ II: 411 f.; EVS: 20b, 
71b; Nyberg II: 169b; Werba 1997: 229; Steblin-Kamenskij 1999: 296 f.; NEVP: 15 


*rai0! ‘to lead, go forth; [euphem.] die, pass away’ 

*AVESTAN: Y Av. IrI0- ‘to die, pass away’ || (+ *para-) ‘id.’. Ф Kellens 1984: 320 also 
assigns iridontom (Yt 5.130) to this root, but the passage is rather obscure. = Liste: 
58 

Pres. ja-: IND. 35р. ҮАУ. iridiieiti (V 6.10, V 6.12, V 6.14, etc.), 3р1. YAv. para.iriinti (V 6.1 ЁЁ), INJ. 
25р. Y Av. para.iri0iiö (H 2.16), SUBJ. 3sg. YAv. iriiiat (V 5.27, V 5.39, V 8.1, eet Perf.: OPT. 35р. 
irraidiiät (ViD 17); Partic.: pres. YAv. para.iridiiant- (H 2.16), perf. YAv. iririüus- (Y 24.5, Y 26.6, Y
```


## [2026-09-14T01:34:15.583Z] AGENT

Now I have enough to write the verification file.


## [2026-09-14T01:45:07.679Z] TOOL CALL #83: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-419.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\n\ndoc = {\n \"pdf_page\": 419,\n \"book_page\": 389,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-13\",\n \"entries\": []\n}\n\n# ---------------- entry 0 : Rei 1 ----------------\ne0 = {\n \"entry\": 0,\n \"root\": \"Rei 1\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *(H)reh₁i- / *reh₁-i- 'wealth, goods, property' (Pokorny 860 '4. rēi- : rē- ‚Besitz, Sache’)\",\n \"note\": \"Pokorny IEW p.860 heads the entry '4. rēi- : rē- ‚Besitz, Sache’' and gathers under it exactly the material Nourai charts: Skt. rāḥ/rāyáḥ 'Besitz, Reichtum', rayi- 'Gabe, Besitz', re-vánt- / Av. raēvant- 'reich', ai.+av. rā- 'geben', ai. rāti- 'Gabe', Lat. rēs, rei 'Sache, Besitz'. Walde-Pokorny II 343 has the same lemma under the shape '2. rē(i)- ‚geben; Sache’'. Watkins/AHD lists it as 'rē-. To bestow, endow ... suffixed form *reə-i- goods, wealth, property, in Latin rēs: RE², REAL¹, REBUS, REIFY, REPUBLIC [Pok. 4 rei- 860]'. The modern laryngealist shape (de Vaan 2008 s.v. rēs; Wiktionary) is *(H)reh₁is 'wealth, goods'. Language label ('Indo-European'), gloss ('possession') and the page citation are all right. Note that the root is *rē(i)-, not the homophonous *rei- 'to scratch' of the next entry — Nourai's numbering Rei 1 / Rei 2 reproduces Pokorny's own separation correctly.\",\n \"note_fa\": \"ریشهٔ هندواروپایی آغازین *(H)reh₁i- «دارایی، مال، چیز» است که پوکورنی در صفحهٔ ۸۶۰ زیر عنوان «۴. rēi- : rē- Besitz, Sache» آورده و همان موادی را گرد آورده که نورایی رسم کرده است؛ والده‐پوکورنی (جلد ۲ ص ۳۴۳) هم آن را *rē(i)- «دادن؛ چیز» خوانده است. تفاوت این ریشه با *rei- «خراشیدن، دریدن» (مدخل بعدی) در خود پوکورنی هم رعایت شده و نورایی آن را درست نگاه داشته است. ادعای نورایی در مورد ریشه درست است.\",\n \"sources\": [W + \"Reconstruction:Proto-Indo-European/reh₁ís\", W + \"res#Latin\"],\n \"ref_check\": [\n   {\"ref\": \"POK:860\", \"status\": \"supports\",\n    \"note\": \"POK_03.txt leaf 94-95 (= IEW pp. 859-860): '4. rei- : rē- ‚Besitz, Sache’ ... Ai. rai- m. f. ‚Besitz, Reichtum’ in rāḥ, rāyáḥ ... rayi- ‚Gabe, Besitz, Kleinod’ ... av. raēvant ‚reich’; ai. av. rā- ‚geben’ ... ai. rāti- ‚Gabe, Geber’ ... lat. res, rei ‚Sache, Besitz’'. Exactly the chart.\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. II p. 343\", \"stance\": \"supports\",\n    \"note\": \"WLD_Bd2 djvu line 22322 ff.: '2. rē(i)- ‚geben; Sache’. Ai. rāti, rāsate ‚gibt, verleiht’ ... rāti-ḥ ‚Verleihung, Gunst’, rayiḥ ‚Gabe, Besitz, Kleinod’, revant- ‚reich’, av. raēvant ds., av. rā- ‚gewähren, spenden’ ... Lat. res (= ai. rāḥ), rei ‚Sache’'.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. rē-\", \"stance\": \"supports\",\n    \"note\": \"AHD_watkins1985.txt line 887: 'rē-. To bestow, endow. Contracted from *reə-. Suffixed form *reə-i- goods, wealth, property, in Latin rēs, thing: RE², REAL¹, REBUS, REIFY, REPUBLIC. [Pok. 4 rei- 860.]'\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, r- section (pp. 1061 ff.)\", \"stance\": \"silent\",\n    \"note\": \"Mann's r- lemmas on pp.1061-1069 (leaves 588-591 of IEC.txt) cover rād-, rādh-, reidh-, reig-, reiko, reiso etc.; no separate lemma for the 'possession' root was found by grep ('Besitz'/'wealth, goods' hits nothing here).\"}\n ],\n \"nodes\": []\n}\n\ne0[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Avestan\", \"words\": \"râ 2; râiti, a-râiti 2; raĕvant\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Av. rā- 'to give, grant' (Pokorny 860 'ai. av. rā- ‚geben’'; WP II 343 'av. rā- ‚gewähren, spenden’') is the verbal root; its ti-abstract is Av. rāiti- / rātay- f. 'gift, granting; generosity' (Bartholomae AiW col. ~1521 '²rātay- : rāiti- f. 1) ‚Gabe, Gewährung’ ... 3) ‚Freigebigkeit’'), and the vant-adjective of the noun rayi- 'wealth' is Av. raēvant- 'rich' (= Skt. re-vánt-, from *rayi-vant-, with the regular contraction ayi > aē). All three are correctly formed and correctly glossed — EXCEPT a-rāiti-: with the Indo-Iranian privative *a- (Nourai's own cross-reference ☞ Apo points at the prefix entry) it means the OPPOSITE, 'ungenerosity, niggardliness'. Bartholomae, AiW s.v. 'a-rātay- 1) f. ‚(Nichtschenken,) Geiz’; 2) Adj. ‚geizig; Knicker’', citing Y.60.5 vainīt ... rāitiš arāitīm 'may generosity overcome niggardliness in this house'. So the box's single gloss 'generous' is right for rāiti- but wrong for a-rāiti-.\",\n \"derivation_fa\": \"اوستایی rā- «دادن، بخشیدن» ستاک فعلی است؛ از آن اسم معنای مختوم به -ti ساخته شده است: rāiti-/rātay- «بخشش، دهش، جوانمردی» (بارتولومه، فرهنگ ایرانی باستان). raēvant- «توانگر» صفت مختوم به -vant از rayi- «دارایی» است (*rayi-vant- > raēvant-، با ادغام ayi به aē)، هم‌ریشه با سنسکریت re-vánt-. اما a-rāiti- با پیشوند نفی *a- معنای واژه را واژگونه می‌کند و «نابخشندگی، بخل» معنی می‌دهد (یسنا ۶۰ بند ۵: rāitiš arāitīm). پس معنای «بخشنده» در جعبهٔ کتاب فقط برای rāiti- درست است و برای a-rāiti- نادرست؛ با این یادآوری، ادعای نورایی با احتیاط پذیرفتنی است.\",\n \"sources\": [W + \"Reconstruction:Proto-Indo-European/reh₁ís\"],\n \"ref_check\": [\n   {\"ref\": \"POK:860\", \"status\": \"supports\",\n    \"note\": \"IEW 860 (POK_03.txt leaf 95): 'av. raēvant ‚reich’; ai. av. rā- ‚geben’ (erweitert ai. rāsate ‚gibt’), ai. rāti- ‚Gabe, Geber’'. The page carries rā-, rāti- and raēvant- but not a-rāiti-.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"AiW s.vv. a-rātay- and ²rātay- : rāiti-\", \"stance\": \"partial\",\n    \"note\": \"BRT.txt line 5338: 'j. a-rātay- 1) f. ‚(Nichtschenken,) Geiz’: vainīt .. rāitiš ‘rātīm Y.60.5. 2) Adj. ‚geizig; Knicker’'; line 25303: 'j., g. ²rātay- : rāiti- f. 1) ‚Gabe, Gewährung’ ... 3) ‚Freigebigkeit’'. Confirms rāiti- but contradicts the gloss given to a-rāiti-.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. II p. 343\", \"stance\": \"supports\",\n    \"note\": \"'av. rā- ‚gewähren, spenden’ ... revant- ‚reich’, av. raēvant ds. ... ai. rāta-ḥ, av. rātō ‚dargebracht’'.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Persian\", \"words\": \"râd\",\n \"verdict\": \"plausible\",\n \"derivation\": \"NP راد rād 'generous, liberal' continues MP rād [lʾT'] 'generous, liberal' (MacKenzie, CPD p.70). Two Old Iranian preforms compete, and both give MP rād regularly (OIr. -āt-, -ād- > MP -ād, NP -ād): (a) Nourai's route, from the rā- 'give' family, i.e. *rāta- 'given, giving' / Av. rāiti- 'generosity' — this is what Horn, Grundriss no.601 (p.134) proposes ('rād ‚freigebig’. aw. vergl. a-rāiti-; ai. rāti- ‚willig zu geben’; phlv. rāt') and what Moʼin's footnote in Borhan-e Qateʼ p.926 repeats; (b) the route now standard in Wiktionary (following the Vedic equation), from Av. rādah- n. 'generosity, care' = Ved. rā́dhas- 'favour, gift', i.e. OP *rādaʰ < PIr. *HrāHdah- < PIE *h₂reh₁dʰ-o-s 'care, provision' — a different root from Rei 1. Nourai's arrow is therefore a defensible, traditional (Horn/Moʼin) derivation rather than a settled one; the competing rādah- etymology is not mentioned in the chart.\",\n \"derivation_fa\": \"«راد» در فارسی نو از فارسی میانه rād «بخشنده، جوانمرد» (مکنزی ص ۷۰) بازمانده است. دو ریشهٔ ایرانی باستان برای آن پیشنهاد شده و هر دو از نظر آوایی به rād می‌رسند: یکی همان که نورایی آورده، یعنی از ستاک rā- «دادن» (اوستایی rāiti-، سنسکریت rāti-) که هرن در مادهٔ ۶۰۱ و معین در حاشیهٔ برهان قاطع (ص ۹۲۶) همان را آورده‌اند؛ دیگری از اوستایی rādah- «دهش، پرستاری» (= ودایی rā́dhas-) از ریشهٔ هندواروپایی *h₂reh₁dʰ- «تیمار کردن» که ویکی‌واژه و پژوهش امروزی آن را ترجیح می‌دهد. پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n \"sources\": [W + \"%D8%B1%D8%A7%D8%AF\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:926\", \"status\": \"supports\",\n    \"note\": \"BQT_v2_pages.txt leaf 386 (= printed p.926, the راد page: 'راد بروزن شاد، کریم و جوانمرد و صاحب‌همت و سخاوت را گویند'). Moʼin's footnote at the foot of the page reads (OCR) 'قس: اوستا — rāiti هندی باستان — rāti (خواهان دادن) استشق ...', i.e. Moʼin compares Av. rāiti- / OInd. rāti- 'willing to give' — Nourai's arrow.\"}\n ],\n \"consulted\": [\n   {\"src\": \"HRN\", \"where\": \"no. 601, p. 134\", \"stance\": \"supports\",\n    \"note\": \"HRN.txt line 5391 (leaf 155 = printed p.134): '601. rād ‚freigebig’. aw. vergl. a-rāiti-; ai. rāti- ‚willig zu geben’; phlv. rāt (auch Titel...), rātīh.' — Horn is evidently Nourai's (and Moʼin's) source, including the odd a-rāiti- citation.\"},\n   {\"src\": \"PHD\", \"where\": \"p. 70 s.v. rād\", \"stance\": \"supports\",\n    \"note\": \"PHD.txt line 555: 'rād [lʾT | P rd, N ~] generous, liberal. ~īh: generosity, liberality.' — confirms the Middle Persian link form.\"},\n   {\"src\": \"Wiktionary\", \"where\": \"راد (Persian)\", \"stance\": \"contradicts\",\n    \"note\": \"'Inherited from Middle Persian lʾṭʹ /rād/, from Old Persian *rā́daʰ, from Proto-Iranian *HráHdah, ... from Proto-Indo-European *h₂réh₁dʰ-o-s, from *h₂reh₁dʰ- (“to care”) ... Cognate with Old Avestan rādah “generosity”, Vedic rā́dhas-' — a different root from Rei 1.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Latin\", \"words\": \"rěs\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Lat. rēs, gen. reī f. 'thing, matter, property' is the western reflex of the same i-stem noun: PIE *(H)reh₁is, acc. *(H)reh₁im (whence the Latin acc. rem, after which the nominative was remade), = Skt. rāḥ / acc. rā́m 'wealth'. Pokorny 860 sets 'lat. res, rei ‚Sache, Besitz’ (das e nach dem Akk. rem aus *reHim?)' beside Umbrian re-per 'pro re' and Lat. reus '(litigant) party' (*rei-os); de Vaan 2008 (s.v. rēs, pp. 520-521) reconstructs *Hreh₁-i- 'wealth, goods'. Gloss 'thing' and language label are right.\",\n \"derivation_fa\": \"لاتینی rēs «چیز، مال، امر» بازماندهٔ همان نام مختوم به i در هندواروپایی آغازین است: *(H)reh₁is، رایی آن *(H)reh₁im که لاتینی rem از آن آمده و سپس فاعلی rēs بر قیاس آن ساخته شده است؛ هم‌ریشه با سنسکریت rāḥ «دارایی». پوکورنی (ص ۸۶۰) و دووان (۲۰۰۸) هر دو همین را می‌گویند؛ ادعای نورایی درست است.\",\n \"sources\": [W + \"res#Latin\", W + \"Reconstruction:Proto-Indo-European/reh₁ís\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"AHD_watkins1985.txt line 887 s.v. rē-: 'Suffixed form *reə-i- goods, wealth, property, in Latin rēs, thing: RE², REAL¹, REBUS, REIFY, REPUBLIC. [Pok. 4 rei- 860.]'\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW 860\", \"stance\": \"supports\",\n    \"note\": \"'lat. res, rei ‚Sache, Besitz’ (das e nach dem Akk. rem aus *reHim?), umbr. re-per ‚pro re’, Dat. Abl. ri; dazu lat. reus ‚Prozesspartei’ (*rei-os)'.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. II p. 343\", \"stance\": \"supports\",\n    \"note\": \"'Lat. res (= ai. rāḥ), rei ‚Sache’; umbr. re-per ‚pro re’, ri abl. dat. Hierher lat. reus ‚der Angeklagte’.'\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. republic\", \"stance\": \"supports\",\n    \"note\": \"KLN_1966.txt line 32432: 'republic, n. — F. république, fr. MF., fr. L. res publica, respublica, ‚state, commonwealth’, lit. ‚a public thing’, fr. res, ‚thing’.'\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 4, \"lang\": \"English\", \"words\": \"real, republic\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Both English words go back to Lat. rēs through learned Latin/French channels. real (adj.) 'actual' < Late Latin reālis 'relating to things' (a juristic coinage from rēs), via Old French/Anglo-French real, first in 15th-c. English legal language ('real property' = property in things); republic < Middle French république < Lat. rēs pūblica 'the public thing, the commonwealth', in English from the 1590s. AHD lists REAL¹ and REPUBLIC among the derivatives of the root, so the arrow Latin → English is exactly what Nourai's cited reference says.\",\n \"derivation_fa\": \"هر دو واژهٔ انگلیسی از راه لاتینی عالمانه و فرانسه به rēs می‌رسند: real از لاتینی متأخر reālis «وابسته به شیء» (اصطلاحی حقوقی) و republic از لاتینی rēs pūblica «کار همگانی، ملک عمومی» که از راه فرانسهٔ میانه république در سدهٔ ۱۶م وارد انگلیسی شد. کلاین و واتکینز همین را می‌گویند؛ ادعای نورایی درست است.\",\n \"sources\": [W + \"res#Latin\"],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\",\n    \"note\": \"The node carries no reference of its own in the book; it inherits AHD from its Latin parent, which does list REAL¹ and REPUBLIC under rē-.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. republic\", \"stance\": \"supports\",\n    \"note\": \"KLN_1966.txt line 32432: 'republic ... fr. L. res publica ... lit. ‚a public thing’, fr. res, ‚thing’, and fem. of publicus ... See real, adj., and public.'\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. rē- and index\", \"stance\": \"supports\",\n    \"note\": \"Root entry lists 'REAL¹ ... REPUBLIC'; the reverse index line 2178 has 'REPUBLIC rē-'.\"}\n ]\n})\n\ndoc[\"entries\"].append(e0)\n\n# ---------------- entry 1 : Rei 2, Reig ----------------\ne1 = {\n \"entry\": 1,\n \"root\": \"Rei 2, Reig\",\n \"verdict\": \"plausible\",\n \"modern_form\": \"PIE *rei- 'to scratch, tear, cut', with the extensions *reik-/*reig-, *reip-, *reib-, *reis- (Pokorny 857-859; AHD rei-¹)\",\n \"note\": \"The main root is right: Pokorny IEW 857 '1. rei- ‚ritzen, reißen, schneiden’; rei-kā ‚Riß, Spalte’, rei-pā ‚steiler Rand’, rei-uā, roi-uā ‚Streifen’', with the extensions reib-, reig-, reik(b)-, reip-, reis- on pp.858-859; Watkins/AHD 'rei-¹. To scratch, tear, cut. [Pok. 1. rei- 857.]'; WP II 343 ff. The second label 'Reig' is supported by Nourai's other reference: Mann, IEC p.1067 has a lemma 'reig- (roig-) “break, breach, téar, cut; piece, fragment”' (Pokorny's own reig- on pp.861-862 means 'to bind' and 'to reach, stretch', not 'to tear', so the label depends on Mann). The third label, 'Rekp: to pull, break', is NOT a reconstructible root in any of the handbooks on disk (no *rekp- in Pokorny, Walde-Pokorny or Watkins; grep finds nothing), and the book's own index makes 'Rekp' a redirect to 'Rei 2' (page 420). The printed page (420 dpi render of pdf p.419, kept as data/verification/sources/refs/ocr/BOOK/419.png) really does read 'Rekp', so the extraction is faithful; the likeliest intent is Pokorny's extension *reip- 'reißen' (the source of rope and L. rīpa charted below) or *rep- 'reißen, raffen' (IEW 865).\",\n \"note_fa\": \"ریشهٔ اصلی درست است: هندواروپایی آغازین *rei- «خراشیدن، دریدن، بریدن» (پوکورنی ص ۸۵۷) با گسترش‌های *reik-، *reip-، *reib-، *reis-. برچسب دوم یعنی Reig را فقط فرهنگ تطبیقی من (IEC ص ۱۰۶۷) به معنای «شکستن، دریدن» می‌آورد؛ در پوکورنی reig- معنای دیگری دارد. برچسب سوم یعنی Rekp به معنای «کشیدن، شکستن» در هیچ یک از مرجع‌های معتبر (پوکورنی، والده‐پوکورنی، واتکینز) نیست؛ تصویر صفحهٔ چاپی نشان می‌دهد که همین صورت در کتاب چاپ شده، پس خطای استخراج نیست و احتمالاً خطای چاپی/نام‌گذاری خود نورایی به جای *reip- است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"POK:857\", \"status\": \"supports\",\n    \"note\": \"POK_03.txt leaf 92 (= IEW 857): 'I. rei- ‚ritzen, reißen, schneiden’; rei-kā ‚Riß, Spalte’, rei-pā ‚steiler Rand’, rei-uā, roi-uā ‚Streifen’. Lat. rīma ‚Ritze’ (*rei-ma) ... ags. rāw, rǣw f. ‚Reihe’ (*roi-ua) ...'\"},\n   {\"ref\": \"IEC:1067\", \"status\": \"supports\",\n    \"note\": \"IEC.txt leaf 591 (printed p.1067, running head 'reidh- — reio', page number 1068 printed further down the leaf): 'reig- (roig-) “break, breach, téar, cut; piece, fragment” Per. (e- or o-grade) rize “fragment”; Ir. riaghaim “téar; crucify”; ... OCS riza “garment” ...'\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. II pp. 343-344\", \"stance\": \"supports\",\n    \"note\": \"'1. rei- ‚ritzen, reißen’. Zsfassung der Erweiterungen bei Persson Beitr. 334 f. ... Erweiterungen: [reik-]: ai. rikháti, likháti ‚ritzt’, rekhā, lekhā ‚Riß, geritzter Strich, Linie, Streifen, Reihe’. Gr. ἐρείκω ‚zerbreche, zerreiße’ ...'\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. rei-¹\", \"stance\": \"supports\",\n    \"note\": \"'rei-¹. To scratch, tear, cut. I. Extended form *reik- ... II. Possible extended form *reip(p)-. Germanic *raipaz, rope ... III. Extended form *reip- ... Latin ripa, bank ... IV. Extended form *reib- ... [Pok. 1. rei- 857.]'\"},\n   {\"src\": \"CHEUNG\", \"where\": \"EDIV p. 189 s.v. *Hrais\", \"stance\": \"partial\",\n    \"note\": \"Cheung lemmatises the Iranian side as '*Hrais “to be torn, tear, cut, split” ... *SANSKRIT: res/les “to tear off, pluck” ... PIE *Hirei-K- “to cut, split, tear” ? = LIV: 504 | Pok.: 858' — same root, laryngeal-initial shape.\"}\n ],\n \"nodes\": []\n}\n\ne1[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Avestan\", \"words\": \"raesah, raeš\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Younger Avestan raēš- / iriθ- 'to wound, injure, suffer damage' (pres. raēšiieiti tr., irisiieiti intr., caus. raēšaiieiti) with the nouns raēša- m. and raēšah- n. 'injury, damage' — Nourai's 'raesah, raeš'. Pokorny puts this s-extension of *rei- on p.858 exactly as charted ('reis-: ai. riṣyati, reṣati ... av. raēš-, iriθ- ‚verletzen, verwunden’ ... raēša- m., raēšah- n. ‚Schädigung’'), so the language, the forms and the gloss are all right. One caveat worth recording: Cheung (EDIV p.308) lemmatises the verb as PIr. *raiš 'to suffer (damage, illness)' and remarks 'the root appears to be exclusively II [Indo-Iranian]', i.e. he does not commit to the PIE tie to *rei-; Mann (IEC 1068 'reiso') and Pokorny do make it.\",\n \"derivation_fa\": \"اوستایی متأخر raēš- / iriθ- «زخم زدن، آسیب رساندن، آسیب دیدن» و نام‌های raēša- و raēšah- «آسیب، زخم» دقیقاً همان است که پوکورنی در صفحهٔ ۸۵۸ زیر گسترش reis- از ریشهٔ *rei- آورده است و بارتولومه نیز همان معنا را ثبت کرده است. تنها نکته آنکه چونگ (۲۰۰۷) این ستاک را *raiš می‌خواند و آن را ویژهٔ هندوایرانی می‌شمارد. ادعای نورایی درست است.\",\n \"sources\": [W + \"%D8%B1%DB%8C%D8%B4\"],\n \"ref_check\": [\n   {\"ref\": \"POK:858\", \"status\": \"supports\",\n    \"note\": \"POK_03.txt leaf 93 (= IEW 858, 'reis-' paragraph): 'av. raēš-, iriθ- ‚verletzen, verwunden; Schaden leiden’ (Präs. raēšyeiti tr., iriθyeiti tr., intr., Kaus. raēšayeiti), Partiz. irista- ‚beschädigt’, raēša- m., raēšah- n. ‚Schädigung’.'\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"AiW s.v. ¹raēša-\", \"stance\": \"supports\",\n    \"note\": \"BRT.txt line 24803: 'j. ¹raēša- m., raēšah- n. ‚Schädigung’; A) körperliche Schädigung überhaupt ...' with V.15.13 / V.13.10 citations.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann p. 1068 s.v. reiso\", \"stance\": \"supports\",\n    \"note\": \"'reiso, ið “snatch; ravish; burst, split”. WP I, 140. Av. raeš- “wound”; Skt. resámi, risyami “injure”; OE risan “seize, ravish” ...'\"},\n   {\"src\": \"CHEUNG\", \"where\": \"EDIV p. 308 s.v. *raiš\", \"stance\": \"partial\",\n    \"note\": \"'*raiš “to suffer (damage, illness)”. *AVESTAN: YAv. raeš- “to get hurt, suffer damage” ... *SANSKRIT: res “to get harmed, hurt” ... ⊙ The root appears to be exclusively II.' — same form and sense, no PIE tie asserted.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Persian\", \"words\": \"rîš 1\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"NP ریش rīš (classical rēš) 'wound, sore; wounded' continues MP rēš [lys] 'wound, sore' (MacKenzie, CPD p.72), itself the regular outcome of the Old Iranian s-stem noun of the verb charted above (*raiša- / Av. raēša-): OIr. ai > MP ē > NP ī in the Iranian pronunciation, so raēša- > rēš > rīš. The denominal MP verb rēšīdan 'to wound, hurt' and NP ریش‌دل in Bābā Tāher's quoted couplet belong with it. It must be kept apart from the homograph ریش 'beard' (MP rēš 'beard', probably PIr. *xraiša-), which is why Nourai's numbering rīš 1 is right.\",\n \"derivation_fa\": \"«ریش ۱» به معنای زخم از فارسی میانه rēš «زخم، ریش» (مکنزی ص ۷۲) و آن از ایرانی باستان *raiša- (اوستایی raēša-) است؛ دوگانهٔ ai ایرانی باستان در فارسی میانه به ـــēـ و در تلفظ ایرانی فارسی نو به ـــیـ بدل شده است. ویکی‌واژه و چونگ نیز همین را می‌گویند. این واژه را باید از هم‌نگاشتش «ریش» (موی صورت، از *xraiša-) جدا دانست و شماره‌گذاری نورایی درست است. ادعای نورایی درست است.\",\n \"sources\": [W + \"%D8%B1%DB%8C%D8%B4\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:988\", \"status\": \"partial\",\n    \"note\": \"Printed p.988 of Moʼin's Borhan (BQT_v2_pages.txt leaf 448, confirmed by the catch-line 'بقیه از صفحهٔ ۹۸۷' at its foot) carries ریباس ... ریچار ... ریخ ۲ ... ریختنی — not ریش. The ریش 'جراحت' entry stands two pages later, on p.990 (leaf 450: 'ریش = بروزن ... با ثانی مجهول ، جراحت'), so the citation is off by two pages; the content Nourai needs is there.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"p. 72 s.v. ¹rēš\", \"stance\": \"supports\",\n    \"note\": \"PHD.txt line 557: '¹rēš [lys | N ~] wound, sore. *rēš [lys | N ~] beard.' and line 559 'rēšīdan, rēš- [lysytn' | N ~] wound, hurt.'\"},\n   {\"src\": \"Wiktionary\", \"where\": \"ریش (Persian), Etymology 2\", \"stance\": \"supports\",\n    \"note\": \"'Inherited from Middle Persian lyš (rēš), from Proto-Indo-Iranian *rayšás (“injury, wound”) from the root *rayš- (“to be wounded, hurt”).'\"},\n   {\"src\": \"CHEUNG\", \"where\": \"EDIV p. 308 s.v. *raiš\", \"stance\": \"supports\",\n    \"note\": \"'*MIDDLE PERSIAN: BMP lys- /rēs-/ “to wound, hurt”. *NWIR: NP res “wound”, also borrowed into Kurd. ris, Bal. res.'\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Avestan / Old Persian\", \"words\": \"riš 2, rîz\",\n \"verdict\": \"disputed\",\n \"derivation\": \"This box is Nourai's Old Iranian preform for the 'spin' verb of node #4, taken straight from Abolqasemi (FFD p.56), who writes: '«ریس» مادهٔ مضارع «رشتن» است. ظاهراً «رشتن»، «ریس» از ریشهٔ *raiš به معنای «بافتن» آمده است: رشت < ایرانی باستان *rišta-; ریس < ایرانی باستان *rais-a-'. Two problems. (i) Form: the present stem Abolqasemi gives is *rais-/*rēs- with s; the book prints 'rīz' with z, which is not a form any source knows (nor is the verb actually attested in Avestan or Old Persian — both preforms are reconstructions). (ii) Descent: modern Iranian etymology does not derive this verb from *rei- 'to scratch, tear' at all. Cheung, EDIV pp.437-438 files the whole family under PIr. *uraiš 'to turn, spin' (YAv. uruuaēs- 'to twist, turn'), from PIE *u̯reik̑- 'to turn around, wind' (LIV 699, Pokorny 1158 f.) — a root with initial *u̯- that has nothing to do with *rei-. Wiktionary follows him ('from Proto-Iranian *wrais- “to turn, to spin”, from Proto-Indo-European *wriḱ-yé-ti “to twist, to bend”'). Nourai's own authorities (Pokorny 858 'npers. ristan ‚spinnen’' under reik-, Horn no.617, Hübschmann, Moʼin) all represent the older, pre-Cheung view.\",\n \"derivation_fa\": \"این جعبه صورت ایرانی باستانی فعل «رشتن» است و مستقیماً از ابوالقاسمی (ماده‌های فعل‌های فارسی دری، ص ۵۶) گرفته شده که ستاک ماضی *rišta- و ستاک مضارع *rais-a- را می‌آورد. دو اشکال هست: یکی آنکه کتاب به جای rīs صورت rīz را چاپ کرده که در هیچ منبعی نیست (و این ستاک‌ها در اوستا و پارسی باستان گواهی نشده‌اند و بازسازی‌اند)؛ دیگر آنکه ریشهٔ این فعل در پژوهش امروزی *uraiš «تابیدن، چرخاندن» (اوستایی uruuaēs-) از هندواروپایی *u̯reik̑- است (چونگ ۲۰۰۷ ص ۴۳۷–۴۳۸) نه *rei- «خراشیدن». پژوهش امروزی ادعای نورایی را رد می‌کند.\",\n \"sources\": [W + \"%D8%B1%D8%B4%D8%AA%D9%86\"],\n \"ref_check\": [\n   {\"ref\": \"FFD:56\", \"status\": \"supports\",\n    \"note\": \"FFD_pages.txt [pdf page 61] = printed p.56 (pdf 62 carries the printed number ۵۷): 'رشتن — «ریس» ماده مضارع «رشتن» است. ظاهراً «رشتن»، «ریس» از ریشهٔ *raiš به معنای «بافتن» آمده است ... رشت < ایرانی باستان *rišta- ... ریس < ایرانی باستان *rais-a-'. Supports the box's content (but with s, not z, and without any Avestan/Old Persian attestation).\"}\n ],\n \"consulted\": [\n   {\"src\": \"CHEUNG\", \"where\": \"EDIV pp. 437-438 s.v. *urais\", \"stance\": \"contradicts\",\n    \"note\": \"'*urais “to turn, spin”. *AVESTAN: YAv. uruuaēs- “to twist, turn” ... *NWIR: NP rēstan, ristan/ris-, rēsidan/rēs- ... “to spin” ... ‹PIE *ureik- “to turn around, wind” → LIV: 699 | Pok.: 1158 f.'\"},\n   {\"src\": \"POK\", \"where\": \"IEW 858, reik(b)- paragraph\", \"stance\": \"partial\",\n    \"note\": \"'ähnlich reik- in ai. risáti, lisáti ‚rupft, reißt ab, weidet ab’ (npers. ristan ‚spinnen’, bal. resag, resay ‚spinnen, flechten’)' — Pokorny does attach the Persian verb to *rei-, which is Nourai's warrant, but only in a parenthesis.\"},\n   {\"src\": \"Wiktionary\", \"where\": \"رشتن (Persian), Etymology 1\", \"stance\": \"contradicts\",\n    \"note\": \"'From Proto-Iranian *wrais- (“to turn, to spin”), from Proto-Indo-Iranian, from Proto-Indo-European *wriḱ-yé-ti (“to twist, to bend”), whence also Avestan uruuisia “to turn”, German reihen, English wry, Latin rīca “veil”.'\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 4, \"lang\": \"Persian\", \"words\": \"rîštan; rîsîdan; abrîšam\",\n \"verdict\": \"disputed\",\n \"derivation\": \"The three Persian words belong together and are correctly grouped: رشتن/ریشتن rištan (past stem rišt-), ریسیدن rīsīdan (a secondary infinitive built on the present stem rēs-), with the nominal derivatives رشته rišta 'thread' (MP rištag 'rope, string, thread'), ریسمان rīsmān and ریسندگی; and ابریشم abrīšam 'silk' < MP abrēšom/abrēšum, a prefixed formation on the same stem (Hübschmann, Persische Studien p.12 no.65, reconstructs MP *aparēšum / *uparēšum from the Armenian loan aprišum, aprešum; Wiktionary and Cheung read it as PIr. *(upa-)abi-uraišamah). What is disputed is the root: Nourai hangs the group on *rei-/*reik- 'to scratch, tear', following Pokorny 858, Horn no.617 (p.137) and Moʼin's Borhan footnote; Cheung, EDIV pp.437-438, and after him Wiktionary, derive the whole family from PIr. *uraiš 'to turn, spin' (YAv. uruuaēs-) < PIE *u̯reik̑- 'to turn, wind', with cognates Oss. ælvisįn, Pashto wresal, Khwar. rγsy- 'to spin' and Kurd. (Sor.) guriš 'rope' (< *ui-raiš-) that presuppose the *u̯-. On that view the semantic bridge is 'twist' → 'spin', not 'pluck, tear off' → 'spin'.\",\n \"derivation_fa\": \"هر سه واژه به درستی یکجا آمده‌اند: «رشتن» (ستاک ماضی rišt-)، «ریسیدن» که مصدری جعلی از ستاک مضارع rēs- است، با مشتقات «رشته» (فارسی میانه rištag «ریسمان، نخ»)، «ریسمان» و «ریسندگی»؛ و «ابریشم» از فارسی میانه abrēšom که ساختهٔ پیشونددار همین ستاک است (هوبشمان، ص ۱۲ شمارهٔ ۶۵، از روی وام‌واژهٔ ارمنی aprišum صورت *aparēšum را بازسازی کرده است). آنچه مورد اختلاف است ریشه است: نورایی به پیروی از پوکورنی و هرن و حاشیهٔ معین آن را به *rei- «دریدن» می‌بندد، اما چونگ (۲۰۰۷) و ویکی‌واژه آن را از *uraiš «تابیدن» (اوستایی uruuaēs-) می‌دانند؛ گواه ایشان صورت‌های ایرانی دیگر مانند آسی ælvisįn، پشتو wresal و کردی guriš است که وجود *u̯- آغازین را لازم می‌کند. پژوهش امروزی ادعای نورایی را رد می‌کند.\",\n \"sources\": [W + \"%D8%B1%D8%B4%D8%AA%D9%86\", W + \"%D8%A7%D8%A8%D8%B1%DB%8C%D8%B4%D9%85\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:951\", \"status\": \"supports\",\n    \"note\": \"BQT_v2_pages.txt leaf 411 = printed p.951 (رشت/رشتاک page). Moʼin's footnote at the foot: '* رشتن – بکسر اول وفتح سوم ، هندی باستان ریشهٔ ... (چیدن، پاره کردن)؛ بلوچی rēsag ... (تابیدن)، آسی alwisyn/alwesun ... ورک: هوبشمان ...' — i.e. exactly Nourai's 'tear/pluck' root, with a cross-reference to Hübschmann.\"},\n   {\"ref\": \"HUB:12\", \"status\": \"supports\",\n    \"note\": \"HUB.txt leaf 22 = printed p.12, no. 65: 'Np. abrešum ‚Seide’ = arm. LW. aprišum, apresum setzt ein phl. aprešum (aus *aparešum, *uparešum u.s.w.) voraus. Auch die übrigen hier angeführten Wörter für ‚Seide’ sind wohl sämmtlich aus dem Neupersischen entlehnt.'\"},\n   {\"ref\": \"FFD:56\", \"status\": \"supports\",\n    \"note\": \"Abolqasemi p.56 (pdf p.61) gives رشتن/ریس from *raiš 'to weave', as quoted at node 3.\"}\n ],\n \"consulted\": [\n   {\"src\": \"CHEUNG\", \"where\": \"EDIV pp. 437-438 s.v. *urais\", \"stance\": \"contradicts\",\n    \"note\": \"'*MIDDLE PERSIAN: BMP l(y)stk /ristag/ “rope, string, thread” ... || (+ *abi-) MMP ’brysŵm “silk” ... *NWIR: NP rēstan, ristan/ris-, rēsidan/rēs- ... “to spin” ... NP abrēsum “silk” || (+ *ui-) Kurd. (Sor.) guris “rope, string”. ‹PIE *ureik- “to turn around, wind”.'\"},\n   {\"src\": \"HRN\", \"where\": \"no. 617, p. 137\", \"stance\": \"supports\",\n    \"note\": \"HRN.txt leaf 158 = p.137: '617. risten ‚spinnen’, Praes. res-em, riste, resulen, resmān, rismān, vergl. ebresum (No. 65). ai. √reś-, riśāte ‚rupfen, abreissen’. bal. resag, n. resay ‚spinnen, flechten’ ...' — the old view, and clearly Nourai's model.\"},\n   {\"src\": \"PHD\", \"where\": \"pp. 4, 72 s.vv. abrēšom, rištag\", \"stance\": \"supports\",\n    \"note\": \"PHD.txt line 170 'abrēšom [ʾplys(w)m | M ʾbʳyšwm, N ~] silk'; line 559 'rištag [l(y)stkʹ | N ~a] rope, string, thread' — confirms the Middle Persian link forms.\"},\n   {\"src\": \"Wiktionary\", \"where\": \"ابریشم (Persian)\", \"stance\": \"contradicts\",\n    \"note\": \"'Inherited from Middle Persian (ʾp̄lyšwm, ʾp̄lyšm /abrēšōm, abrēšom/, “silk”), from Proto-Iranian *upawraišamah. Compare ... Old Armenian loanword ապրիշում (aprišum).' — same prefix analysis as Hübschmann, but with the *wraiš root.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 5, \"lang\": \"Persian\", \"words\": \"rîzeh; rîz 2\",\n \"verdict\": \"plausible\",\n \"derivation\": \"ریزه rīza 'fragment, small piece' and ریز rīz 'small (piece)'. Nourai's reference is verbatim: Mann, IEC p.1067, s.v. 'reig- (roig-) “break, breach, téar, cut; piece, fragment”' opens its list with 'Per. (e- or o-grade) rize “fragment”', so the cited authority does derive the word from the *rei-/*reig- 'tear, cut' family. Persian lexicography, however, takes rīz/rīza as the present stem rēz- of ریختن rēxtan 'to pour, shed, scatter' plus -a, i.e. 'what is poured out, crumbs': Moʼin's footnote in Borhan p.989 s.v. ریختن derives it from 'Av. raēk-, raēč- (بیرون ریختن), MP rēxtan, Lat. linquō, OInd. ric-', i.e. PIE *leikʷ- 'to leave', and Wiktionary has rīxtan < MP rēxtan < PIr. *Hraič- 'to pour, flow'. Both roots begin *rei-, but they are different roots, and the majority Persian view attaches rīza to the 'pour' one. Hence: the arrow is what Nourai's source says, but it is not the standard account.\",\n \"derivation_fa\": \"«ریزه» و «ریز» را من (فرهنگ تطبیقی هندواروپایی، ص ۱۰۶۷) عیناً زیر ریشهٔ reig- «شکستن، دریدن، پاره» آورده است؛ پس ماخذی که نورایی نشان داده دقیقاً همین را می‌گوید. اما ریشه‌شناسی فارسی معمولاً «ریزه» را از ستاک مضارع «ریختن» (فارسی میانه rēxtan، rēz-) می‌داند؛ معین در حاشیهٔ برهان ص ۹۸۹ ذیل «ریختن» آن را به اوستایی raēk-/raēč- و لاتینی linquō می‌بندد، یعنی ریشهٔ *leikʷ- «وانهادن» که با *rei- «خراشیدن» یکی نیست. پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n \"sources\": [W + \"%D8%B1%DB%8C%D8%AE%D8%AA%D9%86\"],\n \"ref_check\": [\n   {\"ref\": \"IEC:1067\", \"status\": \"supports\",\n    \"note\": \"IEC.txt leaf 591 (printed p.1067): 'reig- (roig-) “break, breach, téar, cut; piece, fragment” Per. (e- or o-grade) rize “fragment”; Ir. riaghaim, v. “téar; crucify” ...' — the exact claim of the node.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BQT\", \"where\": \"p. 989, Moʼin's footnote s.v. ریختن\", \"stance\": \"contradicts\",\n    \"note\": \"BQT_v2_pages.txt leaf 449: '* ریختن بکسر اول وفتح چهارم ، از: ریخ + تن ... اوستا ریشهٔ raēk-, raēč- (بیرون ریختن)، پهلوی rēxtan، لاتینی linquo، هندی باستان ریشهٔ ric- ... کردی rētin (بیرون ریختن) ... هوبشمان ۱۳۸'.\"},\n   {\"src\": \"PHD\", \"where\": \"p. 72 s.v. rēxtan\", \"stance\": \"partial\",\n    \"note\": \"PHD.txt line 559: 'rēxtan, rēz- [lyhtnʹ, lyc- | P ryxt, M ryz-, N ~] flow, pour' — the Middle Persian verb whose present stem rēz- underlies NP ریز/ریزه on the majority view.\"},\n   {\"src\": \"Wiktionary\", \"where\": \"ریختن (Persian)\", \"stance\": \"partial\",\n    \"note\": \"'Inherited from Middle Persian 𐬥𐬩𐬧𐬲𐬭 (/rēxtan/), from Proto-Iranian *Hraič- (“to pour; to flow”) ... an Iranian-specific suffixed form of Proto-Indo-Iranian *HriHyáti (“to flow”).'\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 6, \"lang\": \"Sanskrit\", \"words\": \"rěš, ričate; lěkha\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Two separate Sanskrit items, both genuinely under *rei- but both slightly mis-transliterated. (a) Skt. riś- / riśáti, liśáti 'plucks, tears off, grazes off' (Pokorny 858 under reik-; Cheung EDIV 189 'res/les “to tear off, pluck”'); Horn no.617 writes it 'ai. √reś-, riśāte ‚rupfen, abreissen’' — Nourai's 'rēš, ričate' reproduces Horn with ś read as č in the second form, so read riśáte. (b) Skt. lekhā (~ rekhā) is the NOUN 'scratch, line, stroke, drawing' from likháti / rikháti 'scratches, draws, writes' (Pokorny 858, WP II 344 'ai. rikháti, likháti ‚ritzt’, rekhā, lekhā ‚Riß, geritzter Strich, Linie’'); the chart glosses it as a verb, 'to sketch, design', which fits likh- but not lekhā. The r-/l- doublet (rikh-/likh-, reṣ-/leṣ-) is the regular Vedic-to-Classical l for r. Derivation and root assignment are right; only the citation forms are loose.\",\n \"derivation_fa\": \"دو مادهٔ جداگانهٔ سنسکریت است که هر دو واقعاً از *rei- می‌آیند ولی آوانگاری آنها دقیق نیست: یکی riś-/riśáti «کندن، برکندن» که هرن آن را riśāte نوشته و در کتاب به صورت ričate آمده (خوانش نادرست ś به č)؛ دیگری lekhā (و گونهٔ rekhā) که اسم است به معنای «خط، خراش، نقش» و فعل آن likháti «خراشیدن، نوشتن» است؛ کتاب معنای فعلی به آن داده است. ابدال r/l در سنسکریت متأخر قاعده‌مند است. ادعای نورایی با احتیاط پذیرفتنی است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"POK:858\", \"status\": \"supports\",\n    \"note\": \"IEW 858 (POK_03.txt leaf 92-93): 'reik(b)-: ai. rikháti, likháti ‚ritzt’, rekhā, lekhā ‚Riß, Strich, Linie’ ... ähnlich reik- in ai. risáti, lisáti ‚rupft, reißt ab, weidet ab’.'\"},\n   {\"ref\": \"HRN:17,137\", \"status\": \"supports\",\n    \"note\": \"HRN p.137 (leaf 158) no.617: 'ai. √reś-, riśāte ‚rupfen, abreissen’' — the source of Nourai's 'rēš, ričate'. HRN p.17 (leaf 38) carries the tail of no.65 ebrešum 'Seide' ('skr. kṣauma- ‚gewobene Seide’'), i.e. the silk word of node 4.\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. II p. 344\", \"stance\": \"supports\",\n    \"note\": \"'ai. rikháti, likháti ‚ritzt’, rekhā, lekhā ‚Riß, geritzter Strich, Linie, Streifen, Reihe’. Gr. ἐρείκω ‚zerbreche, zerreiße’ ...'\"},\n   {\"src\": \"CHEUNG\", \"where\": \"EDIV p. 189 s.v. *Hrais\", \"stance\": \"supports\",\n    \"note\": \"'*SANSKRIT: res/les “to tear off, pluck” (RV+) = EWAia II: 461. ‹PIE *Hirei-K- “to cut, split, tear” ? = LIV: 504 | Pok.: 858.'\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 7, \"lang\": \"Sogdian\", \"words\": \"dykh\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Buddhist Sogdian δykh 'letter, written character' is a loanword from Sanskrit lekhā / lekha- 'writing, letter' — so the arrow Sanskrit → Sogdian is a borrowing, not an inheritance, and is correct as drawn. Gharib, Sogdian Dictionary, Introduction §IX (on the Sogdian /l/ problem) states it explicitly: in early Buddhist-script borrowings foreign /l/ is rendered by δ, 'kδpʹ from Skt. kalpa-, δwky from Skt. loka-, pyδh (elephant) from Middle Persian and Persian pll, δykh (letter) from Skt. lekha-, and δmtyr (lamp) from Greek lamptṛr'. The Buddhist Sogdian texts in which such Indic loans occur are 6th-9th c. translations made in the Turfan and Dunhuang area.\",\n \"derivation_fa\": \"سغدی بودایی δykh «نامه، حرف» وام‌واژه‌ای است از سنسکریت lekha- «نوشته، خط»؛ پس پیکان کتاب از سنسکریت به سغدی رابطهٔ وام‌گیری است نه وراثت. بدرالزمان قریب در دیباچهٔ فرهنگ سغدی خود (بخش نهم، دربارهٔ واج لام) می‌نویسد که در وام‌واژه‌های کهن خط بودایی، لام بیگانه با δ نوشته می‌شده است: kδpʹ از kalpa-، δwky از loka-، δykh از lekha-. ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"SOD:148\", \"status\": \"partial\",\n    \"note\": \"The statement is in Gharib's book verbatim (SOD.txt lines 6268-6273 = SOD_pages.txt line 3303): '... δykh (letter) from Skt. lekha-, and δmtyr (lamp) from Greek lamptir'. But it stands in the Introduction, whose pages are numbered in Roman numerals (the nearest page marks in the OCR are 'xxxi' and 'xxxiv'), so the citation '148' does not match the page; entry no. 148 of the dictionary (ʾqwytyy) is unrelated. Content supported, page reference unverified.\"}\n ],\n \"consulted\": [\n   {\"src\": \"SOD\", \"where\": \"Introduction §IX (pp. ~xxxiv-xxxv)\", \"stance\": \"supports\",\n    \"note\": \"'In foreign loanwords, /l/ is rendered by δ in the Buddhist script (B) especially in the case of early borrowings such as kδpʹ from Skt. kalpa-, δwky from Skt. loka-, pyδh (elephant) from Middle Persian and Persian pll, δykh (letter) from Skt. lekha-.'\"},\n   {\"src\": \"POK\", \"where\": \"IEW 858\", \"stance\": \"supports\",\n    \"note\": \"Supplies the Sanskrit etymon of the loan: 'ai. rikháti, likháti ‚ritzt’, rekhā, lekhā ‚Riß, Strich, Linie’'.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 8, \"lang\": \"Germanic\", \"words\": \"raigwa; raipaz; rîp\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Three Proto-Germanic preforms, all from Watkins/AHD s.v. rei-¹, but the first is mis-copied. (a) 'row': AHD has 'Suffixed o-grade form *roik-wo- in Germanic *rai(h)-wa- in Old English rāw, rǣw, a line, row: ROW¹' — the reconstruction is *rai(h)wa-, not 'raigwa'; Pokorny 857 files OE rāw under *roi-uā, and WP II 343 leaves it open whether it is *roi-uā or *roik-uā. (b) 'rope': AHD 'Possible extended form *reip(p)-. Germanic *raipaz, rope, in Old English rāp, rope: ROPE' — exactly as charted (Pokorny 858 'got. skauda-raip, aisl. reip, ags. rāp ‚Strick, Seil’'). (c) 'ripe': AHD 'Extended form *reib- in Germanic *rip-. 1. Germanic *ripja- in Old English rīpe, ripe, ready for reaping: RIPE', i.e. the gloss 'ready to be reaped' is AHD's own wording; Pokorny 858 has 'as. ripi, ags. rīpe, ahd. rīfi, nhd. reif (‚zum Ernten reif’)'.\",\n \"derivation_fa\": \"سه صورت ژرمنی آغازین که هر سه از فرهنگ واتکینز (AHD) گرفته شده‌اند، ولی اولی درست نقل نشده است: برای row صورت بازسازی‌شده *rai(h)wa- (از *roik-wo-) است نه raigwa؛ پوکورنی نیز انگلیسی کهن rāw را زیر *roi-uā آورده است. *raipaz «طناب» و *rīpa- «رسیده، آمادهٔ درو» درست‌اند و دقیقاً همان‌اند که واتکینز و پوکورنی می‌گویند. ادعای نورایی با احتیاط (با تصحیح صورت نخست) پذیرفتنی است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"partial\",\n    \"note\": \"AHD_watkins1985.txt s.v. rei-¹ has '*roik-wo- in Germanic *rai(h)-wa- in Old English raw, rew, a line, row: ROW¹', '*reip(p)-. Germanic *raipaz, rope ... ROPE', '*reib- in Germanic *rip-. 1. Germanic *ripja- in Old English ripe, ripe, ready for reaping: RIPE'. Two of the three forms match; 'raigwa' does not correspond to Watkins's *rai(h)-wa-.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW 857-858\", \"stance\": \"supports\",\n    \"note\": \"857: 'ags. rāw, rǣw f. ‚Reihe’ (*roi-ua)'; 858 (reib-): 'as. ripi, ags. rīpe, ahd. rīfi, nhd. reif (‚zum Ernten reif’)'; 858 (reip- with -p(p)-): 'got. skauda-raip ‚Schuhriemen’, aisl. reip, ags. rāp ‚Strick, Seil’, ahd. reif'.\"},\n   {\"src\": \"SKT\", \"where\": \"s.vv. Rope, ripe\", \"stance\": \"supports\",\n    \"note\": \"SKT.txt line 16208 'Rope. (E.) M.E. roop. A.S. rāp. + Du. reep, Icel. reip, Swed. rep, Dan. reb; G. reif'; line 15705 'ripe. (E.) M.E. ripe. A.S. rīpe, fit for reaping; cf. rip, harvest. — A.S. rīpan, to reap.'\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 9, \"lang\": \"English\", \"words\": \"row, rope, ripe\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Direct native continuations of the Germanic forms above: OE rāw/rǣw 'line, row' > ME rawe > row; OE rāp 'rope, cord' > rope (still in stirrup < OE stīgrāp 'mount-rope'); OE rīpe 'ready for reaping' > ripe, beside OE rīpan 'to reap' > reap. All three are listed as the English outcomes of rei-¹ by Watkins and are given the same pedigree by Skeat. Note that row 'to propel with oars' is a different word (PIE *h₁erə-), and only row 'a line' belongs here.\",\n \"derivation_fa\": \"هر سه واژه بازماندهٔ مستقیم صورت‌های ژرمنی بالا در انگلیسی کهن‌اند: rāw «ردیف» > row، rāp «طناب» > rope، rīpe «آمادهٔ درو» > ripe. باید توجه داشت که row به معنای «پارو زدن» واژهٔ دیگری است و به این ریشه ربطی ندارد. ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\",\n    \"note\": \"No reference in the book on this node; it inherits AHD from the Germanic parent, which names ROW¹, ROPE and RIPE.\"}\n ],\n \"consulted\": [\n   {\"src\": \"SKT\", \"where\": \"s.vv. Rope, ripe, Row\", \"stance\": \"supports\",\n    \"note\": \"Skeat gives Rope < A.S. rāp and ripe < A.S. rīpe 'fit for reaping'; his 'Row (2), to propel with oars' is kept separate ('A.S. rōwan ... allied to Skt. aritra, Gk. ἐρετμός'), confirming the homonymy caveat.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. rei-¹\", \"stance\": \"supports\",\n    \"note\": \"Lists ROW¹, ROPE, RIPE (and REAP) as the English derivatives of the root.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 10, \"lang\": \"Latin\", \"words\": \"rîpa\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Lat. rīpa f. 'steep bank of a river, shore' from the *reip- extension of *rei-, the sense being 'the cut (edge)' — Watkins glosses it in so many words: 'Suffixed form *reip-ā- in Latin ripa, bank (< “that which is cut out by a river”)', which is precisely Nourai's gloss 'land cut by water flow'. Pokorny 858 puts it in the same paragraph as Gk. ἐρείπω 'I throw down, tear down' and ἐρείπια 'ruins' ('lat. rīpa ‚steiler Rand, Ufer’'), and Klein s.v. riparian says rīpa 'is prob. cogn. with Gk. ἐρείπειν ‚to tear down”, ἐρείπνη ‚a broken cliff’, ON. rífa ‚to tear, break’'.\",\n \"derivation_fa\": \"لاتینی rīpa «کنارهٔ پرشیب رود، ساحل» از گسترش *reip- از ریشهٔ *rei- است و معنای اصلی آن «آنچه بریده/کنده شده» است؛ واتکینز هم دقیقاً همین معنا را می‌دهد. پوکورنی (ص ۸۵۸) آن را در کنار یونانی ἐρείπω «فروافکندن» قرار داده و کلاین نیز همین را تکرار می‌کند. ادعای نورایی درست است.\",\n \"sources\": [\"https://www.etymonline.com/word/river\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"AHD_watkins1985.txt s.v. rei-¹ III.3: 'Suffixed form *reip-ā- in Latin ripa, bank (< “that which is cut out by a river”): RIPARIAN, RIVAGE, RIVER; ARRIVE.'\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW 858 (reip-)\", \"stance\": \"supports\",\n    \"note\": \"'reip-: gr. ἐρείπω ‚stürze um (tr.), stürze nieder’ (intr.), ἐρείπια n. Pl. ‚ruinae’, ἐρείπνη f. ‚Absturz, Abhang’; lat. rīpa ‚steiler Rand, Ufer’.'\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. riparian\", \"stance\": \"supports\",\n    \"note\": \"KLN_1966.txt line 32959: 'riparian ... fr. L. riparius ... fr. ripa, ‚riverbank, seashore’, which is prob. cogn. with Gk. ἐρείπειν, ‚to tear down”, ἐρείπνη ‚a broken cliff or crag’, ON. rífa, ‚to tear, break’.'\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 11, \"lang\": \"English\", \"words\": \"river, arrive\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Both are French-mediated reflexes of Lat. rīpa. river: Vulgar Latin *rīpāria (terra) 'land along a bank' > Old French rivière 'riverbank; river' > Anglo-French rivere, in English from the late 12th c. (first in surnames) — note the semantic shift from the bank to the stream itself, which happened in Gallo-Romance. arrive: Vulgar Latin *arrīpāre 'to come to shore' (ad + rīpa) > Old French ariver 'to come to land, land a boat' > ME ariven (c. 1200), generalised to 'reach any destination' by the 14th c. Watkins lists RIVER and ARRIVE under the root; Klein and Etymonline give the same chain.\",\n \"derivation_fa\": \"هر دو از راه فرانسه به لاتینی rīpa می‌رسند: river از لاتینی عامیانه *rīpāria «زمین کنار رود» و فرانسهٔ کهن rivière، که در خود گالورومانس از «کناره» به «خود رودخانه» تحول معنایی یافته؛ و arrive از *arrīpāre «به ساحل رسیدن» (ad + rīpa) و فرانسهٔ کهن ariver. کلاین و اتیمانلاین همین زنجیره را می‌دهند؛ ادعای نورایی درست است.\",\n \"sources\": [\"https://www.etymonline.com/word/river\"],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\",\n    \"note\": \"No reference on this node; the Latin parent's AHD entry names RIVER and ARRIVE.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. river\", \"stance\": \"supports\",\n    \"note\": \"KLN_1966.txt line 32980: 'river, n. — ME. rivere, fr. OF. rivere, riviere, ‚land lying along a river; river’ ... fr. Late L. riparia (scil. terra), ‚land lying along a riverbank’, fem. of riparius ... fr. ripa.'\"},\n   {\"src\": \"Etymonline\", \"where\": \"s.v. river, riparian\", \"stance\": \"supports\",\n    \"note\": \"'river (n.) early 13c. ... from Anglo-French rivere, Old French riviere ... from Vulgar Latin *riparia “riverbank, seashore, river” ... from Latin riparius ... from ripa “(steep) bank of a river, shore”.'\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 12, \"lang\": \"Greek\", \"words\": \"replon\",\n \"verdict\": \"transcription_suspect\",\n \"error_in\": \"book\",\n \"book_prints\": \"replon\",\n \"correct_form\": \"repelen (Middle Low German), beside Middle English ripelen — not Greek\",\n \"derivation\": \"There is no Greek word 'replon', and no Greek link in the ancestry of English ripple. The source Nourai cites says something else: Watkins/AHD s.v. rei-¹, IV ('Extended form *reib- in Germanic *rip-') ends '3. Middle Low German repelen, to remove seeds, akin to the source of Middle English ripelen, to remove seeds: RIPPLE²'. Nourai has evidently taken 'repelen, to remove seeds' from that line, dropped a syllable, and then filed it under the previous language heading, producing a phantom Greek word. The printed page (rendered at 400 dpi, kept as data/verification/sources/refs/ocr/BOOK/419.png) clearly reads 'Greek ... replon : to remove seeds', so the JSON is faithful and the error is the author's. Corrected, the box should read: Middle Low German / Middle English repelen, ripelen 'to strip the seeds from flax' — a Germanic node, not a Greek one. Pokorny 858 gives the same material under the reib- extension: 'mengl. ripeln, nengl. ripple ‚Flachs brechen’, mnd. repen, repelen ds., ahd. rifila ‚Säge’'.\",\n \"derivation_fa\": \"واژه‌ای یونانی به صورت replon وجود ندارد و در تبار واژهٔ انگلیسی ripple هیچ حلقهٔ یونانی نیست. ماخذی که نورایی نشان داده (فرهنگ واتکینز) می‌گوید: «آلمانی سفلای میانه repelen «دانه‌گیری کردن»، هم‌ریشه با انگلیسی میانه ripelen». پیداست که مؤلف همین واژه را با حذف یک هجا به صورت replon آورده و آن را زیر عنوان «یونانی» نشانده است. تصویر صفحهٔ چاپی نشان می‌دهد همین صورت در کتاب چاپ شده، پس خطا از خود کتاب است نه از خوانش اسکن.\",\n \"sources\": [\"https://www.etymonline.com/word/ripple\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"contradicts\",\n    \"note\": \"AHD_watkins1985.txt s.v. rei-¹ IV.3: 'Middle Low German repelen, to remove seeds, akin to the source of Middle English ripelen, to remove seeds: RIPPLE².' No Greek form anywhere in the entry (the only Greek in the rei-¹ family, ἐρείκω/ἐρείπω, is not in Watkins's entry at all).\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW 858 (reib-)\", \"stance\": \"supports\",\n    \"note\": \"'reib-: ags. rīpan, riopan ‚ernten’ (engl. reap) ... mengl. ripeln, nengl. ripple ‚Flachs brechen’, mnd. repen, repelen ds., ahd. rifila, riffil ‚Säge, gezackter Berggrat’.' The word is Germanic.\"},\n   {\"src\": \"SKT\", \"where\": \"s.v. ripple (1)\", \"stance\": \"supports\",\n    \"note\": \"SKT.txt line 16136: 'ripple (1), to pluck the seeds from flax-stalks. (Scand.) ME. ripplen, ripelen ... from the sb. ripple, a flax-comb ... from Swed. repa, to ripple flax, orig. to scratch, rip ... + Du. repelen ...; G. riffeln.'\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 13, \"lang\": \"English\", \"words\": \"ripple\",\n \"verdict\": \"plausible\",\n \"derivation\": \"English has two 'ripple's. RIPPLE², the flax-comb and the verb 'to strip the seeds from flax' (ME ripelen, 15th c.), is the one AHD attaches to this root through Middle Low German repelen / Swedish repa 'to scratch, rip' — Skeat says the same. RIPPLE¹, the common modern word 'small wave; to ruffle a surface' (v. early 15c. 'to crease, wrinkle'; n. 1798), is treated by Etymonline as 'of obscure origin, perhaps a frequentative of rip (v.)'. The chart gives only the bare word 'ripple' with no gloss, so the arrow is right for the flax sense and unproven for the sense a reader will assume; and its immediate parent (node #12) is in any case a phantom Greek form. Verdict therefore plausible rather than confirmed.\",\n \"derivation_fa\": \"در انگلیسی دو ripple هست: یکی شانهٔ کتان و فعل «دانه از ساقهٔ کتان جدا کردن» که واتکینز و اسکیت آن را از آلمانی سفلای میانه repelen و سوئدی repa «خراشیدن» می‌دانند و به همین ریشه می‌بندد؛ دیگری ripple معمول به معنای «موج ریز» که اتیمانلاین خاستگاهش را ناروشن می‌خواند. چون جعبهٔ کتاب هیچ معنایی نداده و پدر آن (جعبهٔ یونانی) ساختگی است، ادعا فقط با احتیاط پذیرفتنی است.\",\n \"sources\": [\"https://www.etymonline.com/word/ripple\"],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\",\n    \"note\": \"No reference in the book on this node; it depends on the AHD citation of its (mislabelled) parent.\"}\n ],\n \"consulted\": [\n   {\"src\": \"SKT\", \"where\": \"s.vv. ripple (1), ripple (2)\", \"stance\": \"supports\",\n    \"note\": \"'ripple (1), to pluck the seeds from flax-stalks ... from Swed. repa, to ripple flax, orig. to scratch, rip'; 'ripple (2), to graze slightly ... Frequentative of rip.'\"},\n   {\"src\": \"Etymonline\", \"where\": \"s.v. ripple\", \"stance\": \"partial\",\n    \"note\": \"'ripple (v.) early 15c., riplen, “to crease, wrinkle”; 1660s, “to present a ruffled surface”, of obscure origin, perhaps a frequentative of rip (v.)' — i.e. the everyday word is not securely attached to this root.\"}\n ]\n})\n\ndoc[\"entries\"].append(e1)\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-419.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(doc, f, ensure_ascii=False, indent=1)\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-419.py && python3 -m json.tool data/verification/page-419.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 419"
}
```


### [2026-09-14T01:45:09.083Z] TOOL RESULT

```
written
JSON OK
nodes verified: 17/17
node verdicts: {'plausible': 6, 'confirmed': 8, 'disputed': 2, 'transcription_suspect': 1}
root verdicts: {'confirmed': 1, 'plausible': 1}
ref checks: {'supports': 12, 'not_checked': 4, 'partial': 3, 'contradicts': 1}
books consulted: {'partial': 6, 'supports': 30, 'contradicts': 6} | by book: {'POK': 6, 'Wiktionary': 5, 'CHEUNG': 5, 'PHD': 4, 'KLN': 4, 'SKT': 4, 'WLD': 3, 'BRT': 2, 'HRN': 2, 'AHD': 2, 'Etymonline': 2, 'IEC': 1, 'BQT': 1, 'SOD': 1}
```


## [2026-09-14T01:45:32.922Z] AGENT

Done — `data/verification/page-419.json` written, `verify_check.py 419` reports 17/17 nodes and **0 PROBLEM lines**.

**Page 419 (book p. 389) — 2 entries (+1 redirect skipped), 17 nodes**

Verdicts: roots confirmed 1 / plausible 1; nodes confirmed 8, plausible 6, disputed 2, transcription_suspect 1.
Ref checks: supports 12, partial 3, contradicts 1, not_checked 4 (bare English leaf nodes with no refs).

Flagged items:
- **disputed — Rei 2 #3 `riš 2, rîz` (Av./OP) and #4 `rîštan, rîsîdan, abrîšam`**: Cheung EDIV 437-8 and Wiktionary put the whole "spin" family under PIr. \*uraiš / PIE \*u̯reik̑- (Av. uruuaēs- "to twist"; cf. Oss. ælvisyn, Kurd. guriš), not \*rei- "to scratch, tear". Nourai's own refs (POK 858 parenthesis, Horn 617, Hübschmann 12, Moʼin BQT 951, Abolqasemi FFD 56) all back the older view, so the arrow is traditional but superseded.
- **transcription_suspect — Rei 2 #12 `[Greek] replon : to remove seeds`**: no such Greek word. AHD s.v. rei-¹ IV.3 reads "Middle Low German **repelen**, to remove seeds … RIPPLE²". `error_in: book` — the printed page (verified at 400 dpi, copied to `data/verification/sources/refs/ocr/BOOK/419.png`) really prints "Greek … replon", so the extraction is faithful; the language label is wrong too (Germanic, not Greek).

Other findings worth the owner's eye (no extraction errors found — JSON matches the printed page throughout):
- Root box "Rei 2, Reig" also prints **"Rekp : to pull, break"**, which is not a root in Pokorny, Walde-Pokorny or Watkins; page 420 makes "Rekp" a redirect to Rei 2. Likely the author's label for Pokorny's \*reip-.
- Rei 1 #1: `a-râiti` is glossed "generous" but Bartholomae s.v. a-rātay- gives "(Nichtschenken,) Geiz" — the privative means the opposite (Y.60.5 rāitiš arāitīm).
- Rei 1 #2 `râd`: Nourai/Horn 601/Moʼin derive it from Av. rāiti-; Wiktionary (Ved. rā́dhas- equation) prefers Av. rādah- < PIE \*h₂reh₁dʰ- — marked plausible.
- Rei 2 #5 `rîzeh/rîz`: Mann IEC 1067 supports Nourai verbatim ("Per. rize 'fragment'"), but Moʼin (BQT 989) and Wiktionary attach it to ریختن < \*Hraič- — marked plausible.
- Citation slips: **BQT:988** should be ~990 (p. 988 has ریباس–ریختنی; ریش "جراحت" is on p. 990); **SOD:148** — the δykh < Skt. lekha- statement is in Gharib's Introduction §IX (roman-numbered, ~p. xxxv), not p. 148; **AHD** prints \*rai(h)-wa-, not the chart's "raigwa"; Sanskrit "ričate" is Horn's riśāte with ś misread.
