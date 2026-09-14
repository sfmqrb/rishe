# Verification process log — verify-page-451


## [2026-09-14T01:56:13.263Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 451 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-451.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-451.json. Write /home/sfmqrb/git/rishe/data/verification/page-451.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 451` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T01:56:14.269Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T01:56:15.006Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T01:56:15.026Z] TOOL RESULT

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


## [2026-09-14T01:56:15.681Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-451.txt"
}
```


### [2026-09-14T01:56:15.697Z] TOOL RESULT

```
1	=== PDF page 451 (book page 421) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Skai : shining, bright  (refs POK:917)
4	#1 (parent #0) [Avestan] refs=POK:700,916; BQT:2047,674; KNT:184 | čitra : clarity, face, also race and origin ; hu-čitra : with nice face ☞Su 1 ; manuš-čitra : with a manly face, or from the race of "Manush" ☞Men 1
5	  #2 (parent #1) [Persian] refs=BQT:674, 2047, 2336; MON:5140 | čehreh «چهره» : face ; hožîr «هژیر» : beautiful ; Manǔčehr «منوچهر» : "from Manush family"
6	#3 (parent #0) [Avestan] refs=POK:917; SOD:367 | čâyâ, asaya : shade
7	  #4 (parent #3) [Sogdian] refs=SOD:367 | sy`k : shade
8	  #5 (parent #3) [Persian] refs=HRN:154 | sâyeh «سایه» : shade
9	#6 (parent #0) [Greek] refs=POK:917; AHD | skena : tent
10	  #7 (parent #6) [Latin] refs=AHD | scaena : stage
11	    #8 (parent #7) [French] refs=None | 
12	      #9 (parent #8) [Persian] refs=MON | senârîo «سناریو» : scenario
13	      #10 (parent #8) [English] refs=None | scene, scenario
14	#11 (parent #0) [Germanic] refs=AHD | skînan : to shine
15	  #12 (parent #11) [English] refs=None | shine
16	--- entry 1 ---
17	ROOT [Old Iranian] Skaif, Skaip : to wait  (refs FFD:63)
18	#1 (parent #0) [Pahlavi] refs=FFD:63 | škěb : patient
19	  #2 (parent #1) [Persian] refs=FFD:64; MON | šakîb «شکیب» : patient ; šakîbîdan «شکیبیدن» : to be patient | extra: شکیبا ، شکیبایی
20	شکیفتن
21	--- entry 2 ---
22	ROOT Skaip -> redirect to Skaif
23	--- entry 3 ---
24	ROOT [Indo-European] Skaivos : sinister, odd, strange  (refs WLD2:537; IEC:1146)
25	#1 (parent #0) [Greek] refs=IEC:1146 | skaios : awkward
26	#2 (parent #0) [Latin] refs=IEC:1146 | scaevus : sinister
27	#3 (parent #0) [Persian] refs=IEC:1146; MON:2085 | šǔx «شوخ» : vulgar, rude, a joker, also beautiful | extra: شوخی
28	
```


## [2026-09-14T01:56:18.413Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-451.json",
 "description": "Read page 451 source JSON"
}
```


### [2026-09-14T01:56:18.505Z] TOOL RESULT

```
{
  "pdf_page": 451,
  "book_page": 421,
  "entries": [
    {
      "root": {
        "name": "Skai",
        "lang": "Indo-European",
        "refs": "POK:917",
        "gloss": "shining, bright"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:700,916; BQT:2047,674; KNT:184",
          "words": [
            {"translit": "čitra", "gloss": "clarity, face, also race and origin", "script": null},
            {"translit": "hu-čitra", "gloss": "with nice face", "script": null, "see": ["Su 1"]},
            {"translit": "manuš-čitra", "gloss": "with a manly face, or from the race of \"Manush\"", "script": null, "see": ["Men 1"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:674, 2047, 2336; MON:5140",
          "words": [
            {"translit": "čehreh", "gloss": "face", "script": "چهره"},
            {"translit": "hožîr", "gloss": "beautiful", "script": "هژیر"},
            {"translit": "Manǔčehr", "gloss": "\"from Manush family\"", "script": "منوچهر"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "ای فخر آل اردشیر ای مملکت را ناگزیر - ای همچنان چون جان وتن آثاروافعالت هژیر",
            "poet": "Daqîqî"
          }
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:917; SOD:367",
          "words": [
            {"translit": "čâyâ, asaya", "gloss": "shade", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Sogdian",
          "refs": "SOD:367",
          "words": [
            {"translit": "sy`k", "gloss": "shade", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 3,
          "lang": "Persian",
          "refs": "HRN:154",
          "words": [
            {"translit": "sâyeh", "gloss": "shade", "script": "سایه"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Greek",
          "refs": "POK:917; AHD",
          "words": [
            {"translit": "skena", "gloss": "tent", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "scaena", "gloss": "stage", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "French",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Persian",
          "refs": "MON",
          "words": [
            {"translit": "senârîo", "gloss": "scenario", "script": "سناریو"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 8,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "scene, scenario", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "skînan", "gloss": "to shine", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 11,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "shine", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Skaif, Skaip",
        "lang": "Old Iranian",
        "refs": "FFD:63",
        "gloss": "to wait"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Pahlavi",
          "refs": "FFD:63",
          "words": [
            {"translit": "škěb", "gloss": "patient", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "FFD:64; MON",
          "words": [
            {"translit": "šakîb", "gloss": "patient", "script": "شکیب"},
            {"translit": "šakîbîdan", "gloss": "to be patient", "script": "شکیبیدن"}
          ],
          "script_extra": "شکیبا ، شکیبایی\nشکیفتن",
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Skaip",
        "redirect": "Skaif"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Skaivos",
        "lang": "Indo-European",
        "refs": "WLD2:537; IEC:1146",
        "gloss": "sinister, odd, strange"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Greek",
          "refs": "IEC:1146",
          "words": [
            {"translit": "skaios", "gloss": "awkward", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Latin",
          "refs": "IEC:1146",
          "words": [
            {"translit": "scaevus", "gloss": "sinister", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Persian",
          "refs": "IEC:1146; MON:2085",
          "words": [
            {"translit": "šǔx", "gloss": "vulgar, rude, a joker, also beautiful", "script": "شوخ"}
          ],
          "script_extra": "شوخی",
          "note": null,
          "quote": {
            "text": "خمی که ابروی شوخ تو در کمان انداخت - بقصد جان من زار ناتوان انداخت",
            "poet": "Hâfez"
          }
        }
      ]
    }
  ]
}
```


## [2026-09-14T01:56:19.158Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-14T01:56:19.223Z] TOOL RESULT

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


## [2026-09-14T01:57:04.498Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','BQT','MON','KNT','SOD','HRN','FFD','WLD','WLD2','IEC','AHD','PHD','NYB','BRT','CHEUNG','ARY','HUB']:\n    if k in d: print(k, json.dumps(d[k],ensure_ascii=False)[:700]); print('---')\n    else: print(k,'MISSING')\n\""
}
```


## [2026-09-14T01:57:05.208Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"skāi-\\|skǝi-\\|skī-\" POK_full.txt | head -30"
}
```


### [2026-09-14T01:57:05.727Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index 
---
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.c
---
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol 
---
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archiv
---
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get s
---
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the 
---
FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/ref
---
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015
---
WLD2 MISSING
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstruct
---
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifie
---
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<ident
---
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's 'NYB' nu
---
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between 
---
CHEUNG MISSING
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", "local_file": ["/home/sfmqrb/git/rishe/
---
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by parag
---
```


### [2026-09-14T01:57:05.804Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T01:57:08.516Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls -la POK* && head -c 600 POK_full.txt && echo \"=== grep skai\" && grep -n \"skai\" POK_full.txt | head -20"
}
```


### [2026-09-14T01:57:08.590Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb  981836 Sep  4 14:06 POK_01.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1137861 Sep  4 14:06 POK_02.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1170809 Sep  4 14:06 POK_03.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 3971883 Sep  4 14:06 POK_full.txt
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


=== grep skai
44165:See also: see below under skai-t- 
52546:Latvian skaittV count, recite prayers ', Lithuanian skait-au, -///"count, read '. 
75040:compare Lithuanian skaistas) and caelum^sky, heaven' {*kaid-lo-or*kaid-, *kait-slo-, 
75041:compare with -/'-forms German heiter' bright, clear ', Lithuanian skaid-rus, skaidrus); 
75050:Lithuanian skaidrus, s/ra/io'/'i/s "bright, clear, bright'; Latvian skafdrs6s., "clean'; 
75051:Lithuanian skaistas, 5/r5/s/i>5 "bright'; different (to s/re/ic/- under S. 921) Trautmann 263. 
75153:alb. /75/e" scale, husk, fishbone, splinter, beard the Ahren ' {*skolia= Gothic skaija); 
75201:Norwegian Swedish skaiie; ablaut. Swedish skulle 'skull, cranium', older Swedish skolla 
76958:Indo Germanic skei-p-, -b^- extended from skei-, compare *skai-uo-s {*skai-uo-s) "slant, 
77004:scaJlid^ lets go, unhands, relinquishes, disperses ' {*skai-l-). Old Irish erscaJliud^ breakup, 
77069:Lithuanian skfedziu, sk/est/" separate, divide'. Iter. skaidyti{: Gothic skaidan. Old Indie 
77084:with it identical Lithuanian skfedziu, s/r/'es//" dilute', sAys/as'thin fluid', Latvian skaidTV 
77716:bright' ( *skairi-i). Old Frisian skeria "clean';
```


## [2026-09-14T01:57:14.802Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"917\" POK_full.txt | head -20; echo \"=== pagemark\"; grep -n \"Page(s)\" POK_full.txt | head -5"
}
```


### [2026-09-14T01:57:14.872Z] TOOL RESULT

```
72562:References: WP. II 483 ff., WH. II 507 ff., 511, EM2 917 ff., Trautmann 248, 258 ff., 273. 
75059:Page(s): 916-917 
77090:strain '; russ. sd/r;^' "veritable, genuine'; compare also above S. 917; 
77490:Page(s):917 
77727:Page(s): 917-918 
87802:griesgramig', /At/c/o'5/'e"niedermetzeln' (from *truci-caidos\.o Latin caedo above S. 917), to 
=== pagemark
1549:Page(s): 2 
1574:Page(s): 2 
1607:Page(s): 2-3 
1637:Page(s): 1 
1679:Page(s): 3
```


## [2026-09-14T01:57:15.631Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==(917-344)' POK_02.txt | head -60"
}
```


### [2026-09-14T01:57:16.696Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T01:57:18.461Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '77440,77500p' POK_full.txt"
}
```


### [2026-09-14T01:57:18.523Z] TOOL RESULT

```
schuren 'scour, rub, clean, clean, sweep, wash away ' = Danish skure, Swedish skura6s.; 

with formants -/o-. Middle High German schiel {*skeulo-) "splinter, abgesprungenes or 
ragged piece'; 



Latvian skurinat lausen, ruffle; tousle ', refl. "sich kratzen, krauen'; 

with ^extension: Middle Irish scofha/d 'cWps, cuts' {*skutati), scofht "cutting edge, cusp, 
peak', also " hair lock '; Middle High German hudele rag'; Lithuanian skutu, skust/" scrape, 
peel ', skutas ^scrap, shred, rag', skutenos' scrapings ', Old Lithuanian skutna^ bald head, 
worn out place'; Latvian skuot/t/es ' s\c\r\ schuppen', skaute^ sharp edge'; Lithuanian 
sk/aut/s ^p'\ece Zeug', skiautere^ cockscomb, crest on head of cock, rooster's comb '; 
perhaps Latin scutilus^iWiu' and gr. OKUTaAn "club, mace, joint, stick', qkutqAov ds., 
aKUTaAi(; "staff, cudgel, club, Waize' (*"cleaved Aststiick' or likewise); here OKUTri KscpaAr) 
Hes., GKUTQ Tov TpaxH^ov. IiKsAoi Hes.; 

about East Lithuanian s/ri/e'/5s"rag' compare Specht Indo Germanic Dekl. 56; thereafter 
probably skvernas 6s. from *skernas. 

References: WP. II 552 f. 
Page(s): 954 

Root / lemma: (s)k(h)ai-, (s)k(h)ai-d-, (s)k(h)ai-t- 

Meaning: to hit, kick 

Material: Latin caedo, -ere {occTdo eic.) "hew, hit, strike, slay', cae'o'es"Schlachten, 

Morden', caementum {*caid-smento-) "Bruchstein', caeA//?? "chisel' {*caid-slo-), caia 

{*caidja) f. "cudgel ', caid, -are'hew, hit, strike', ancaesa\asa caelata', ana/en. "small 

shield' ( *ambi-caid-sli-)\ 

alb. qieirsky, heaven' from Italian cielo "sky' < Latin caelum (1) -/n. "the burin or 
engraving tool', caelum (2) -/n. "the heavens, sky, air, climate. Esp. heaven as the home 
of the gods; fig., heaven as the height of joy, renown, etc..'. 

k(h)ai-\v\ mnl. /7e/e"Rammblock', Middle High German Modern High German heie 
"beetle, hammer, wooden hammer, Ramme', mnl. heien^hW, bump, poke, rammen'. 
Modern High German Swiss Z?©/©/? "stomp, hemp break, rupture'; 

khai-t-\v\ Armenian xaif "prick, prick, sting', xait'em^ prick ', xlt'am'be anxious ', xlt" 
grieving heit, heftiger pain'; against it xlrt's\.u\z\g, anxious, argwohnisch' from *khid-ro-\ 

References: WP. II 538, WH. I 44, 45, 129, 130, 131; about Old Indie khidatrre\U, 
presses' [a), secondary khedai. "Druck, load' s. J. Wackernagel Stud. A. Grierson, 826- 
28. 
Page(s):917 



Root / lemma: (s)k(h)ed-, (s)k(h)e-n-d- 

Meaning: to crush, scatter 

Note: (extension from sek- "cut, clip') 

Material: Old Indie s/r^ao'a/e (uncovered) 'splits' {*skhnd-l)\ Avestan scandayeiti^ breaks,
```


## [2026-09-14T01:57:22.409Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '77660,77740p' POK_full.txt"
}
```


### [2026-09-14T01:57:22.491Z] TOOL RESULT

```
Root / lemma: sRai-, sRai- : sRT- 



Meaning: to glimmer (of wet things); sliadow 

Note: 

Root / lemma: sRai-, sRai-. sRT-\ to glimmer (of wet things); shadow, derived from 

truncated Root /lemma: aisk- {* avisk-): bright, shining. 

Material: Old Indie chaya^ radiance, shimmer, shadow', Avestan a-saya- "wer keinen 

shadow wirft', np. saya 'shadow, protection'; 

gr. GKia f. {sRn-a) "shadow', GKispoq, hom. gkiosic; 'shady, dark', OKipov "sunshade ' 
(formal = alb. hir, with length Gothic skeirs); with the grade sR^i\-: OKrivn, Doric OKava 
"tent, stage, scene ', GYS\yoc„ Doric OKavoq, n. "tent; body (as wrapping of the soul)'; gkhv " 
butterfly, moth ' Hes.; OKivap n. "body'; 

Note: 

From gr. OKia "shadow' + gr. oupa "tail' derived gr. OKioupoi;, Latin sciurus -i, pi. sciuridae 
m. "squirrel', alb. from a reshuffled Latin cognate derived alb. {*sciuridae) ceter, keter 
"squirrel' from alb. derived Bulgarian katerica "squirrel'. Typical of alb. is the drop of initial 
S-: sc- > c- also the shift c > k 

alb. he, /7/e "shadow' {*sk//a), /?/>■" grace ' (= gr. oKipov), (hjona ^ shadow' {*skei-n-?), 
Geg /7i/y"god'; 

Typical alb. s/r->/7- initials. 

Old Icelandic skTu. " hypocrisy ' (: gr. OKid), Gothic s/re/>75/7 "shine, appear, seem, 
gleam, shine, gleam'. Old Icelandic sklha ds., Old High German Old English sc/han ds., 
Modern High German sche/nen {n-present, compare Old Church Slavic s/'ngtr, if also in 
Latin scintilla "spark' a formation from a similar originator from is present, is doubtful 
(derivative eines *s/^/-/7/c»- "gleaming'?); 

Maybe Venetian sciantizo : Napulitano scentella : Portuguese centeiha : Romanian 
scanteie> alb. shkendija: "spark'. 

Old Icelandic skihn., Old Saxon skin, Old High German scTnxw. "shine, radiance '; Old 
English Old Saxon scima. Middle High German sc/7e/77e "shadow'. Modern High German 
Schemen^ shadowy shape'. Old Icelandic skim/m. " radiance ', Modern High German 
schimmern, Schimmel eic; Gothic 5/re//775 "shiner, torch'. Old High German Old Saxon 
scTmo, Old English sdmam. "light, radiance '; Middle High German scheim ds.; without s- 
probably Norwegian hTm, hJma, as s/r/777"thin cover, Hautchen' (as "durchscheinend', 
compare:) Old Icelandic skjarm. " transparent skin, sash '; Gothic s/re/AS "clear, bright'. Old 



Icelandic skTrr, Old English sc/?"durchsichtig, bright, clean', Middle High German (md.) 
schTr^ pure, candid ', Modern High German schier. Old Icelandic 5/r^/r"clean, clear, 
bright' ( *skairi-i). Old Frisian skeria "clean'; 

Latvian seja{*keia) "shadow, reflection, face'; 

Old Church Slavic sijati, singti^ become gleam, illuminated ', 5e/76 "shadow' (besides 
stenbior *scenb)\ Czech ciry^ pure, candid ', russ. 5C//3y' "veritable, genuine' (Gothic 
loanword?). Church Slavic *s//i>" open open ', Adv. s//y etc.; 

Tocharian B skiyo "shadow' (= gr. gkiq). 

References: WP. II 535 f., WH. I 131, Jokl L.-U. 60 ff., Trautmann 304. 
Page(s): 917-918 

Root / lemma: sRed- 

Meaning: to cover 

Material: Old Indie chadati {uncovered), chadayat/" bedeck, verbirgt', chattra-m' shelter', 

chad/s-n. "cover, roof; Avestan sadayantf-^a garment' (skyth. trouser?), afghan. pso/s/'to 

put on, wear' {*pati-u pa-sad-); Old High German hazrw.. Middle High German haezen. 

"Rock, clothing'. Old English hseteru Hom. PI. n. "dress'.
```


## [2026-09-14T01:57:42.649Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Page(s): *700\\|Page(s): *69[89]-700\\|Page(s): *700-\" POK_full.txt | head; echo \"=== 916\"; grep -n \"Page(s): *91[56]\" POK_full.txt | head"
}
```


### [2026-09-14T01:57:42.724Z] TOOL RESULT

```
57405:Page(s): 700 
57443:Page(s): 700 
57457:Page(s): 700 
57472:Page(s): 700 
57701:Page(s): 699-700 
57756:Page(s): 700-701 
=== 916
74185:Page(s):915 
74381:Page(s):915 
74397:Page(s):915 
74902:Page(s):915 
74946:Page(s): 915-916 
74971:Page(s):916 
75059:Page(s): 916-917
```


## [2026-09-14T01:57:44.778Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '57370,57475p' POK_full.txt"
}
```


### [2026-09-14T01:57:44.847Z] TOOL RESULT

```
Note: 



Root / lemma: rnand-: hurdle, plaited twigs, horse fence, stable, derived from Root/ 
lemma: mend- mond-{mQd-l)\ to suck (breast), to feed; breast. 
Material: Old Indie mandura^ stable ', mandiramu. 'house, chamber'; gr. (Illyrian?) 
pav5pa f. 'corral, pen, fold, stall, hurdle ', \\bNbaKoQ, 'bar, bolt'; thrak. [jav5aKr|<; ' 
Garbenband '; Illyrian PN Mandurium or Mandur/a {Ca\abnen); whether primary meaning ' 
stable, horse fence ', perhaps to mendo-' the young of an animal ', S. 729 (mend-). 

Note: 

The inanimate suffix -ur- . Old Indie mandura^ stable ' : UAupioi , oi, lllyrians, UAupia , n, 
lllyria, also'lAAupi? , n. Adj. 'lAAupiKO^ , n, 6v, Illyrian: -kx\, the region or province of lllyria, 
'lAAupi^io , speak the Illyrian language, 'IAAupia:--hence Adv. 'lAAupiaii. 
References: WP. II 234, Krahe Festgabe Bulle 205 f. 
Page(s): 699 

Root / lemma: mahnu-sor mohnu-s 
Meaning: man 

Material: Old Indie manu-, manus-' person, man, husband' (also ' male ancestor of the 
people'), Avestan in PN Manus-ci&ra-, proto Germanic *manuaz\n PN A^5/7/7i/s (Tacitus), 
ancestor of the Germans, Gothic manna {Ger\. mans), Old Icelandic madr, mannr. Old 
English Old Frisian Old High German mann^rr\ar\, husband', Gothic mannisks. Old 
Icelandic mennskr. Old English Old High German mennisc^ human, of human beings, of 
people; humane'; Old High German mann/sko etc. 'person'; Old Church Slavic mozb, russ. 
muz'mar\, husband' {*mang/a-, suffix similarly as in Lithuanian 27770-^-^5 'person'). 
Maybe the root word is related to the name of the moon in PIE; Mene/aus 'rr\oor\ god?'; 
also egypt. Menes?'\'\or\ of revenge' (the chariot of the moon was pulled by lions in Egypt). 
Lion was the beast that fell from the moon. 

References: WP. II 266, Trautmann 169; perhaps to 3. men- '\.h\r\k'. 
Page(s): 700 

In Sanskrit, the name Manu appropriately came to mean "man" or "mankind" (since Manu, 
or Noah, was the father of all post-flood mankind). The word is related to the Germanic 
Mannus, the founder of the West Germanic peoples. Mannus was mentioned by the 
Roman historian Tacitus in his book Germania. Mannus is also the name of the Lithuanian 
Noah. Another Sanskrit form, manusa is closely related to the Swedish manniska, both 
words meaning "human being." 



The same name may even be reflected in the Egyptian Menes (founder of the first dynasty 
of Egypt) and Minos (founder and first king of Crete). Minos was also said in Greek 
mythology to be the son of Zeus and ruler of the sea. 

The English word "man" is thus also related to the Sanskrit manu, as well as its 
equivalents in other Germanic languages. Gothic, the oldest known Germanic language, 
used the form Manna, and also gaman ("fellow man"). 

The name Anu appears in Sumerian as the god of the firmament, and the rainbow was 
called "the great bow of Anu," which seems a clear reference to Noah (note Genesis 9:13). 
In Egyptian mythology Nu was the god of waters who sent an inundation to destroy 
mankind. Nu and his consort Nut were deities of the firmament and the rain. Nu was 
identified with the primeval watery mass of heaven, his name also meaning "sky." 

Root / lemma: mahrtio- 

Meaning: horse 

Note: only Celtic and Germanic 

Material: Irish marc, cymr. etc. /775/r/7 "horse', gall. papKOv Akk. Sg., MarcodurumPH; 

Old High German marah. Old English mearh. Old Icelandic marr^horse' (Modern High 
German in Mar-schall, -stall), fem. Old High German meriha. Old English mJere, Old 
Icelandic merr. Modern High German Mahre. 

References: WP. II 235. 
Page(s): 700 

Root / lemma: mahth-1ox mohth- 

Meaning: a kind of harmful insect 

Material: Armenian /77a///"louse'; Gothic mat^a, m. Old High German mado. Old English 

mada^worm, maggot ', Old Icelandic maMr6s., Old Swedish matk, Finnish loanword 

matlkka " little worm'. 

References: WP. II 228, H. Petersson z. Kenntnis the Heterokl. 32 f. 

Page(s): 700 

Root / lemma: maht-2 

Meaning: hack, flapper 

Material: Old Indie matya- n. "harrow or stump ', matJkrta-^ harrowed or rolled '; Latin 

mateola^ a kind of mallet '; Old High German (gl.) /t?©^^/^ "plough' (Lehmann Afneuere 



Spr. 119, 188); from Vulgar Latin mattiuca:0\6 English mattoc, engl. mattock' hack, 
mattock, hoe'. Old Bulgarian motyka'hack, mattock, hoe'; 
References: WP. II 229, WH. II 49. 
Page(s): 700 

Root / lemma: mahu-ro-
```


## [2026-09-14T01:57:45.316Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '74950,75060p' POK_full.txt"
}
```


### [2026-09-14T01:57:45.407Z] TOOL RESULT

```
Material: Old Indie skabhnati, skabhnotr propped ', Perf. caskambha, skabhayatF 
fastened, ligated, strengthened, reinforced, made fast; fortified '; skambha-rc\., 
skambhana-m^ prop, pillar', Avestan i/y055/r5/77i6'a/77 'under fastening, strengthening ', 
fraskamba-, frascimbana- " girders, pillars '; npers. paskam " a covered walk between 
columns, colonnade, piazza, arcade, gallery, porch, portico ', sogd. sk'np- {*skamb) " base 
of the universe '; 

Maybe alb. Geg shkamb, Tosc sbkemb'seat, bench, rock, stone, *pillar' related to Latin 
scamnum {*sksb'"nom). 

Latin scamnum {* skdb^nom) " bench, footstool ', Demin. scabillum, scabe/fum ' n\e6r\ges 
Bankchen, footstool '; 

die Aryan within nasalization, as well as the e-vocalism from Avestan frascimbana- 
(compared with Old Indie skambhana-m) reshuffling through Aryan from skabh- after 
*stent)^- (see steb-' jamb, upright section of a doorframe or window frame; stanchion, 
roof support ') in Old Indie stabhnat/" plinth, base, base of a pedestal t', stambha- ' posts, 
pillars, columns ' etc. 

References: WP. II 539, WH. II 487 f. 
Page(s):916 

Root /lemma: (sjkamb- and (s)kemb- 

Meaning: to curve, bend 

Note: 

Root/ lemma: {sjkamb- and (s)kemb-\ "to curve, bend' derived from Root/ lemma: kam-p- 

: "to bend'. 

Material: Gr. aKapp6(; "crooked, bowlegged'; Old Irish ca/77,6' "crooked', cymr. corn, cam, 
bret. kamm ds., gall, in Camb/o-dunum 'Kempten', bret. camhetan rot' rim of the wheel ' 
{*cambita); zero grades *kmb-'\.\}'cn = swap, vary, exchange ' and "zusammendrehen. 



fessein' in gall.-Latin cambiare^s\Na'Q, vary, exchange ' and Middle Irish cimb^ tribute, 
silver'. Old Irish c/'mb/d 'captwe', c/mbe' captivity, imprisonment, confinement'; 
Maybe alb. /re/r7/?ey 'exchange' a Latin loanword. 

With e-vocalism: gr. Koppoc; m. "band, strap, loop', K0|jp6u) " bind, knot '; Norwegian 
hempa 'Kleiderstrippe, loop, noose, snare, handle, part of an object designed to be 
gripped by the hand ' (also ' stuff of hemp ', in which meaning certainly influenced by hamp 
" hemp '); 

from a basic meaning " go crookedly ' from reiht man an: gr. *OK£|jpu) " limp ' 
erschlossen from dem names lK6iJpO(;, Swedish skumpa " limp ', skimpa " jump, dance ', 
Old High German scimpfan^ joke drive, push, play, deride ', Modern High German 
schimpfen, Schimpf, Modern High German (Low German) humpen, humpeln^ hobble, limp 
'(or to keub-? above S. 590 f.); 

*(s)kamb- rexrnuAs an kam-, kamp- 'bend' (above S. 525); sein relationship to (s)kemb- 
is still unclear; also das zur nasalized root for 'bend' (?) or 'haken' (compare Lithuanian 
kimbCi, kibti^ hang bleiben'): kabli, -eti^ hang ', kabinti^ hang ', kablysm. 'hook', kabei. ' 
Heftel, hook ' (but also e-forms as kebeklis 'hook'); Old Church Slavic skobai. ' fibula ', 
russ. skoba^ agrafe, hook, clasp ', wherefore Old Icelandic hopu. 'small bay'. Old English 
/7o/?'ring'; against it Old Icelandic hespa^ iron staples ' = Old English haepse, haesp. 
Middle High German haspe, hespe. Modern High German Haspe, Haspe, holl. hespe 
'Hijftgelenk', Middle Dutch also 'hack, mattock, hoe' to kap-, above S. 527 f. 

References: WP. 1346, 350 f., ll539f.,WH. I 148f., Trautmann 112, 116. 

Page(s):918 

Root / lemma: (s)kand- (s)kend- 

Meaning: shine 

See also: see above S. 526 {ka-). 

Page(s):918 

Root / lemma: (s)kai- (d-), (t-) 

Meaning: shining, bright 

Material: Old Indie ket'u- m. 'Lichterscheinung, brightness, Bild' (= Gothic haidus), keta- m. 

'mark, token, sign', kefana-m' body, mark ', c/tra- 'augenia\\\g, lovely, superb, pretty, 

splendid, bright', n. 'apparition' = Avestan c/^ra- ' augenia\\\g, clear, bright' (ablaut, with Old 

High German heitar); 



Latin probably caes/us'\/KauK6q, from den Augen' (from *ka/t-or *kaid-to- iroxw, 
compare Lithuanian skaistas) and caelum^sky, heaven' {*kaid-lo-or*kaid-, *kait-slo-, 
compare with -/'-forms German heiter' bright, clear ', Lithuanian skaid-rus, skaidrus); 

Gothic haidus^V\v\6 of way' (originally *'lichte apparition'), Old Icelandic heidrxw. 
"honour, earnings'. Old English had, haed. Old High German /7e//'Stand, rank, kind of 
(Modern High German suffix -heit}\ Old Icelandic heidu. "clear, bright sky, heaven' (: Old 
Indie keta-vn.), heid-rM]. "cheerful, uncloudy'; Old High German /7e//a/'"cheerful, 
gleaming (originally from the cloudless sky, heaven)'. Old Saxon /7eo''5/'"cheerfur, Old 
English hador6s., n. "cheeriness of sky'; 

Lithuanian skaidrus, s/ra/io'/'i/s "bright, clear, bright'; Latvian skafdrs6s., "clean'; 
Lithuanian skaistas, 5/r5/s/i>5 "bright'; different (to s/re/ic/- under S. 921) Trautmann 263. 

Maybe alb. s/ray"edge, end' 

References: WP. II 537 f., WH. I 130f., 133; 

See also: compare kai-3{above S. 519) and 5^^/- (under). 

Page(s): 916-917
```


## [2026-09-14T01:58:26.243Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT ciθra\"; grep -n \"ci&ra\\|ciÖra\\|ci9ra\\|ciGra\\|čiθra\\|ci0ra\" BRT.txt | head -30"
}
```


### [2026-09-14T01:58:26.303Z] TOOL RESULT

```
=== BRT ciθra
```


## [2026-09-14T01:58:27.663Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT saya\"; grep -n \"a-saya\\|asaya\\|a\\.saya\\|saya-\" BRT.txt | head -20; echo \"=== KNT citra\"; grep -n -i \"citra\\|ci.ra\" KNT.txt | head -20"
}
```


### [2026-09-14T01:58:27.740Z] TOOL RESULT

```
=== BRT saya
2731:Zum  V.  äs-;  s.  unter  ana-,  —  aL  ihm-  n.  — )  VgL  iKoDstT.  Dbr.  AiS.  185. j-,  g.  'aeä-  V.  'suchen'.  Praes.  3  isa-, a  isa-,  *»Ja-'',  14  b  tfasa-,  aisasa-", 17  (Fut)  aifya-,  30  (Iter.)  aSsaya-;  Perf. iyals-^,  yals-i\  —  PPfP.  isla-,  PFP.  k><7-;
2732:(AD.)  baom  Y.7.2; —  Aa  »i?  bara  'm (AP.)  bansmaca  U.io^;  —  'masca  bam- maca  N.  7/T.;  —  *kava  °ma  (IS.)  Aava bansmana  N.  108-,  — ■  °m>m  aSaya  b^nlsm Y.62.^;   —  yü  °md  (AP.)''  asaya   barat  * V.Ä79;    —    *kva    a/Sqm  (AP.)  ^'mim^    ' paiti.barat    N. /oj;    — ■    cvat    nä    nit?ma 'mähe  patti.barS  ratufri^  "wie  viel  Brenn-    _  .  .
2777:(Kaus.)  aisaya-,  adaya-.  —  Inf.  'istS;  Absol.  |  np.  xn,  KSs.  ii;  vgl.  tfi-  f.  'Deichsel'.  —  Pü. : 'ihmnitn.  \      "i  so  nach  Ga.  (und  Dst.),
3508:•  j.  apa-j-zära-  m.  'Abfluss,  {Wasser)ab- zwejgung'  a)  des  VouruAasa:  srayä  vouru.- kasaya  .  .  yeäke  . .  Aazannm  -ranam  . . kasal  aSsqm  °ranqm  c(&war>.sat»m  ayan.- baranqm..*arihas(a  me  *afi:aAka  Spö 'rö *vt)asaiti  vispJis  aoi  karsvqn  Y.  65.  4  £; —  aija  käu  'rö  bvat  zrayanAs  vouru.- kaiahe  vairil  yH  Aaosravä  nqma  Yt  ig. 56;  —  zrayauhs  vouru.kasahe  ,  .  vTspJ rairi/  a^araiti  vlsp}sca..nimraoi!  vlspSsca srlr!  'äire (AP.)'> \i.8.i,f>;~ katiht kaüht •,lire(XS.)  Ytj.ioi.  b)  der  Ratfka:\ tipa  guoim  'r>m  ra»hayh  Yt/5. 27,  j
3775:•  g-  C  j-)  aibi,  j.  aiwi  (aivi)''*,  p.  abiy 1)  Praen.  II  a)  mit  Akk.  bei  Veiben  der Bewegung;  a)  'ad,  zu  -  hin,  zu,  gegen  - hin':  Aauv  ksrJ' parärasJ'  'biy  vistaspam Bh.  j.  1;  D.  5.3;  —  nadPlabaira"  ..  'biy b-litrum  a/iyavt^  Bh.2.1;  J.14,  5.4;  — iJra*  . ,  hacUmi^  hamtii''iy(^  abavJ'  'biy avatn..astyavt^{sA.)  Bh.y.s;  13,  /.ii,i6% 5.  s;  —  'biy  bubirum  yd^ä  naiy  upilyatn (sd.)  Bh.  j.  19;  —  *adakiy  aham  asnaiy (sd.)  aham  "biy  *uva/am  Bh.  2.4;  —  _fra- vartil  agarbayata  utä  anayatä  "biy  mäm Bh.  2. 13;  J4,  /,  17,  5. 1,  4;  —  pasävc^ adam  käram  . .  fräisayant  'biy  viHäspam Bh.j.  i;  —  yuviyam  (sd)  ii^tanaiy  kacä . .  °biy  drayJ'  /)-«*  . .  D,  i'].y,  3,  Bh.j. 4.  ß)  'adversus,  contra,  gegen' :  pasäva'' kUra^  .,  'biy  avam  ..  aHyazia"  Bh.  1. 18;  — Aauv  karam  fraisaya'^  kari^uvatim . .  'biy avam  Bh.^.9 ;  3, 9, 1 1.||  b) mitLok. 'über, inBetreff  von  -';  /:>rasayai{%^)  'bl  ^Tu.lÄa
3867:•  j.aiwri.vaeSayanta-  Adj.  'der  zugewiesen werden  soll,  wird,  dedicandus':  haoma  . . asiiya  aiwi.vaioayamna  asaya  'la  ". .  qui dedicantur  .  .  dedicabuntur"  Y\.f).$.
4301:*asaya  *arpdusa  . .  nSiS  *°vis(i^  ästrydii vaHmaini  *asaya  (sd.)  x'a/na  vd  'vtsti astryeiti  N.  15.  2)  'Nichtlesen,  Nicht- vorlescn ,  Verweigerung  des  liturgischen Lesens':  yS  baoyö  (sd.)  aelahmSt  paräiti nöit pascalia  "Wistlm  ästryanti  (statt  Sing.) ". .  dann  macht  er  sich  durch  Verweige- rung des  (Liturgie-)  Lesens  nicht  sündig" N.4.
4305:•  j.  an-a'bdäta-  Adj.  'nicht  (mit  dem Hemd)  bekleidet':  bansma  asaya  frastar)- t^m  asaya  aiwyJst^fn  'few"  Vyt.  23.
4881:j,  ayayTi  N.  15%  lies  asaya;  %.  asä-,
5450:Zum  V.  'ar-.  —  VgL  aUy  und  S  ^Sg.  4  C mit  No.  —  Pü.:  larsäiäsJh.  ~~  0  Hds.  ä  rii-' lim;  5.  aber  Pii,  und  iSt.  Y.  60.  3,  wo  oioö- w^  xsnülasla  asayasra  . ,  paili.uiiilayasfa.
5693:asaya-
5729:•  j.  a-saya-  i)  Adj.  'der  keinen  Schalten
6071:'sa  (ab  Subj.)^  naptyoisä  . .  türaAya  uxjSn  a  a:  aevö  panlä  yS  'sähe  Y,  72.  1 1 ;  — (sd.)  Y.  4Ö.  1 3 ;  —  y7  xidknm  .  .  'iä .  ratus  . .  'sähe  *dasayat  paniqta  Vyt  42 ; /radähai  (sd.)  aspp/fsata  Y.ji.  161  — 1 — 'sähe  faiti  pantqm  ti/ahi  päi/i  mq^rynt %wahmät  äkras^a  manaahascä  yayä  syao- !  V.  ^  43  (s.  ob.) ;  —  sva.  'Stätte,  wo  das %anaU  °hm  %raosiä  (sd)  \.46.J;  — ,  j^sa  heittüxh  ist' :  haoa  nJ  ß-aounauayät/i vanh^us  :^aasus  i^aaatä  (sd.)  vaahius  'sähe  paiti  panlqm  drujg  vaiim^la  asmi- •/fli/J..  Y.J5.  5.  a)  GS.  mit /«ä- 'der  nqm  (sd.)  "waim  wird  uns  (die  Rinder) Pfad  des  ASa,  der  Wahrheit,  des  beUigen  !  zurUckführcn  zum  Pfad  des  Asa  . ."  Yt Rechts'   (s.  I  3  b  a):    dr^gvafö  .  .    *"Ji/j  70. 86.  ß)  GS.  mit  bir^  (sd.):  hnja
6206:i)  'dem  heiligen  Recht  gemäss  handeln': asayata  (aP.)  vastryäüa  (sd.)  pu'^ra  fra- /ae/tra  \yi.  !!''>.        a)  mit  einer  Massbe- stimmung 'Werke  des  v4sa  (heiligen  Rechts) verrichten':  tauu.mats  (sd.)  asayäiti  yS .  . __  _  P.18.         a)  'sich  das  Recht,  den  recht- (/a)  aArätTA9ti  —  4) "lü  \'.  43.  i  12  2. St. ::  massigen  Anspruch,  erwerben  (auf  — )"': '  ■—   S.  noch No.  3,5,7.— ')S.iBed.BTHL.L>i.a/  fyf  „s  anhuyäifUsd.)  ä-at  hs  na  asa~ 39,  KZ.  ,S.  32,  GDN.  BB.  /j.  259.  -  I  ^^^  ci'af  ahmäi  nair,  mizd  m  a»hat  yö  . .
6219:taM    tva    itsit    .  ,    tt/rqm    'yqm    n3it    .  . fästryqm    HSit  pu%reistlm     "keiner    von denen,   die  nicht  essen,  ist  tüchtig  die  .  . Werke  des  Aia  zu  verrichten  noch  . .  Land- b2u  zu  treiben  .  .  noch  in  den  Besitz  von Söhnen  zu  gelangen"  V._j, 33').        a)  mit einer    (akkus.)     Massbestimmung:     tatui.- masd  (sd.)  xl  *altqmat  'yam  *pafre  yö  . . P.  18.         3)  'Erwerb  des  (höchsten)  An- rechts, Anspruch  auf  das  Paradies':  imqm aifkvyqmca  (sd.)  *°j'fl«('a*' Y._J.4; — yqm aiai'a    vaauhlm    °yqm    vaioa    tarn    drvA K'i'jvä  "welchen  guten  Anspruch  der  A^a- gläubige    kennt   (sva.  besitzt),   damit  ist der  2?n^läubige  unbekannt"  Vr.  22.3. Zum  Praes.  3 1  asaya-,  —  Pü. :  ahräiih  (Sü. :  puri- jralä],  erl.  (zu  Y.  3):    iär  u  karpai  .  .  hamäi kvaim.    —    ')  Vgl.  Vyt.  //    unler    asaya-.  — '\  NA.  aiyqtn ;  s.  aber  Nir.
6300:—  N.  75:  lies  asaya  st  °saom;  —  Y.  //. V.7.52PliZ.:  lies  hati:mt.al':^
6693:—  yj  (nämL  zao^ra)  *naire  aSaone  *dasie ahüi'a  *haite  *casanäica  paitica  ^p^rts- mattJi  xratem  aiavamm  "welche  (Z.)  für einen  Gläubigen  gespendet  wird,  der  die fromme  Weisheit  studirt  und  lehrt  und erforscht"  N.  84.  a)  absol.  'shidlren, dem  Studium  (^c%.  der  heiligen  Texte)  ob- li^en':  y5  avaoa  »Sil  aiwylsti*"^  *asaya . . "wer  dort  dem  Studium  nicht  obliegt  aus
6801:yät K.4.%;  ■''N.  (iS;  —  'nahe  vairyehe  asaya frasrütahe  Y.27.7,  Vr.72.2;  7,4,  2.6,  Y. 7p.  2 1 ;  —  'nahe  vairyehe  arsuxoahe  växs y.^.i;  Vr.  70.2;  —  'nanqm  vairyanqm N.  702;  —  'n^m  vairlm  yazamaide  Y.  13. 8;  7.26,  61,1,  Vr.74.3;  —  'nJ  vairyS vacqm  j'irUrajqst^mäYl.  il.y,  —  sraohm .  .  yeAlie  'ns  vairyg  snatiis  vuata  Y.  57. 22;  — jainti   mqm   'na    vairy.
6973:•  j,  a-x^arant-  Adj.  'nichtessend' :  nazcis 'r^iitam  tva  ns'it . .  asayam  (sd.)  . .  V.  j.33,
7098:•  j.  äxä-''  V.,  niur  mit  ami  'i<f>opäv\ I  Praes.  30  (Iter.)  amyJxsaya-.  Inf. I  aiwyäxstriii.
=== KNT citra
385:1 Note that Ciça- in this name has the OP form and not the Median *Cióra-. * ViMüspa, Aspacand, and Vidafarnd, despite the Median phonetics, are specifi- cally Persians; but personal names often belong to other dialects or languages than that of the locality to which the owner of the name belongs. Cf. also note 1.
1002:But äi in gen. Cišpãiš and Cicizrai§ is only graphic, cf. $179.IV; aniyéued, maškāuvā are for -@uvd, = Skt. -dsu + enclitic -à; Pai&iyduadaya is probably for Patsiya-wadaya.
1092:Av. cibra- ‘seed, lineage’, OP cica-.
2126:Gen. Sg. skautais, Fravartatš, Cišpaiš, Gáigarcait, Bägayädaiš; also Cišpäiš, Cicixrais.
3586:Техт or DB, Сошмх П: 1 :98ty : Dárayavaus : xSayafiya : paeüva : Naditabaira : ha 2 dà : kamnaibis : asabaraibis : amufa : Bübirum : ašiya 3 va: pasàva : adam : Babirum : ašiyavam : vasnd : Auramazdiha : uta : Ba 4 birum : agarbiyam : uta : avam : Naditabairam : agarbüyam : pasáva : ava 5 m : Naditabairam : adam : Babirauv : avüjanam —— :0ütüy : Dārayavauš : x 6 Sdyabiya : yātā : adam : Bübirauv : àham : ima : dahydva : tyà : hacàma : ha 7 migiyà : abava : Рагва : Üvja : Mada : Aðurā : Mudráya : Parfava : Margus : Өз 8 tagui:Saka : абу : Dārayavauš : x8dyabiya : I martiya : Martiya : nā Q ma : Cicixrais : puca : Kuganakà : пата : vardanam : Pársaty : avada : adaraya : 10 hauv : udapatatà : Uvjaiy : Кагаһуй : avaðā : afaha : adam : Imanis : amiy : 0 11 vjeiy :xSdyafiya —— : @atiy : Darayavaus : zsayattya : adakaiy : adam : asna 12 iy : àham : abiy : Üvjam : pasáva : hac&ma : alarsa : Üvjiy& : avam : Marti 13 yam :agarbaya : hyašām : mafista : dha : шат : avàjana — : 00у: D 14 árayavaus : xSiyafiya : І martiya : Fravartiá : пата : Мада : hauv : udapatat 15 à : Madaiy : Катаһуй : ауаба : абала : adam : XSa6rita : amìy : Uvaxdtrah 16 уй : taumàyá : pasáva : kāra : Mada : hya : v'àpaliy : haw : hacáma : hamiciya : a 17 bava : abiy : avam : Fravartim : aSiyava : hauv : тёйуайтуа : abava : Madaiy 18 9àtry : Dárayavaus : xšāyaðiya : kara : Parsa : ша : Мада : bya : ира : mim : 4 19 ha : hauv : kamnam : aha : раѕауа : adam : kdram : fraiSayam : Vidarna : пата : Pársa : man 7 20 à : badaka : avam&àm : mafistam : akunavam : avataSaám : afaham : parait : avam : К 2] dram : tyam : Madam : jatà : hya : mand : пау : gaubataiy : pasiva : hauv : Vidarna : ha 22 dà : kara : айуауа : yafà : Madam : parárasa : Māruš : пата : vardanam : Ma 23 дау : ауада : hamaranam : akunaus : hada : Мада : һуа : Màdaisuvà 24 :ma(iSta : dha : hauv : adakaiy : пау : avadà : аһа : Auramazdimary : u 25 раѕійт : арага : vasnà : Auramazdáha : kāra : hya : тара : avam : kàram : t 26 yam : hamiciyam : aja : vasiy : Animakahya : mähyä : XXVII : raueabis : fakat 27 à : аһа : avatüsám : hamaranam : kartam : pasáva : hauv : Ката : һуа : manā : Карада : пат 28 à : dahydus : Mádaiy : avadà : mam : amánaiya : y8tà : adam : arasam : Mada ' 20m : 08у : Dàrayavaus : xšāyaðiya : адаг х : nàma : Arminiya : man 30 à : badaka : avam : adam : frāišayam : Árminam : avafasazy : aaham : paraidiy : ka 31 ra : һуа : hamigiya : mană : naiy : gaubataiy : avam : jadiy : pasiva : Dadarsi 32 š : aSiyava : yafà : Arminam : parárasa : pasáva : hamigiya : hagmatà : paral 33 tà : patiš : Dādaršim : hamaranam : cartanaiy : Züzahya : пата : àvahanam : А 34 rmíniyaiy : avadà : hamaranam : akunava : Auramazdimaiy : upastàm : a 35 bara : vasnà : Auramazdàha : kāra : һуа : manā : avam : küram : {уаш : hamigiyam : 36 aja : vasiy : Oüravaharahya : máhya : VIII : raucabis : 09akatà : dha : ava 87 à$üm : hamaranam :kartam : бабу : Dárayavaus : z3àyaffya : patiy : duv 38 itiyam : hamigiyà : hagmatà : paraitd : patiš : Dàdar&im : hamaranam : carta 3€ nay : Tigra : пата : didà : Arm‘niyavy : avadà : hamaranam : akunava : А 40 uramazdàmaiy : upastàm : арага : vašnā : Ашатагдаћа : kāra : һуа : тапа :a 41 vam : káram : tyam : hamigiyam : aja : vasiy : G9üravüharahya : mihya : ХҮШ 42 :raueabiá : бакаќа : аһа : ауабадат : hamaranam : kartam —— : 00у : Daraya 43 vaus : xšāyaðiya : patiy : citiyam : hamictyd : hagmatà : paraita : pat 44 iš : Dádar&im : hamaranam : cartanaiy : Uyama : nama : didi : Arm'myaty :a 45 vadā : hamaranam : akunava : Auramazdimaiy : upastam : арага : vaSnà : Aurama 46 zdàha : kāra : һуа : manā : avam : küram : tyam : ham?giyam : aja : vasiy : Oàigarea 7 d :mábyà : IX : raucabis : Nakata : dha : ауада ат : hamaranam : kartam : pasava 48 : Dadarsis : citā : mim : amánaya : Arm/niyaiy : yiti : adam : arasam : Ма
5385:Citcizri- sb. ‘Cincikhri’, father of Martiya (§163.V): Elam. st-in-sa-ak-ri-1§, Akk. #-in-Sa- ah-ri-i& Cicizrais gsm. (§179.1V) DB 2.9.
```


## [2026-09-14T01:58:35.140Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==199' KNT.txt | head -40"
}
```


### [2026-09-14T01:58:36.422Z] TOOL RESULT

```
DB 1.34f, 41, 461; 2.74, 88f; 5.19f, 35; DNb 30, 37, 40f, 43, 45; XPf 19f; XPh BAL.
щй AsH 13; DB 1.34 bis, 34f, 41 ter, 46 bis, 47, 57, 67, 77, 85; 2.3, 4, 18, 74 ter, 77, 81f, 87, 88, 89, 92; 3.30, 47, 48, 50, 58, 74, 77 (written ud, §52. VI), 88, 90, 91; 4.7, 56, 61, 62, 75 bis, 79, 89, 91 bis; 5.11, 12, 19, 20°, 28°, 31, 35 bis; DPd 15; DPe 18, 14; DNa 53; DNb 3f, 26, 27, 28, 30 bis, 37 bis, 40f, 41, 43 bis, 45 ter; DSe 28°, 51f; DSf 13, 28 bis, 29, 33, 35, 36, 37, 40, 44 bis, 48, 50, 52, 55, 57; Обр 2°; DSs 7°; DSt 9; "рле 11; XPa 19 bis; XPb 24, 30; ХРе 13 bis; XPd 19; XPf 19f, 20, 39, 46, 47; XPg 5, 11; XPh 24, 35, 38, 41, 48, 53, 54, 55, 58; Хе 5°; XV 20, 27°; A'Pa 24°: A%Sa 4, 5, 5°; ASe 5; A’Sd 4; A’Ha 5°, 6, 6f; A?He 19; A*Pa 25 bis, 26.
utü-maiy АЗН 12; DB 4.46 (visible to Cameron; ef. note ad loe.); DPh 10; DNa 52f; DH 8; XPb 29; XV 26f°; А?Не 20. utà-taiy DB 4.56, 58, 73f, 75, TH, 79. utā-šaiy DB 2.74f, 89. ша-&т DB 2.13°; 5.18, 26. иій-4ат DB 3.57; 5.15. ulá-di$ DNb 46f.
ula-maiy (§135) DSe 51°; DSf 58; DSj 6°; DSt 9°; XPa 15, 18f; XPd 18f; XPf 41, 45f; XPg 14; XPh 58 (space for w left blank; Lg. 13.303); XSc 5^; A'Pa 23°; Аа 4. uta-Sem (8135) XPh 34, (In restorations there is almost always un- certainty between utà- and uld-.)
Utüna- sb. ‘Otanes’, ally of Darius against Gaumata: Elam, fu-ud-da-na, Akb &»mi-it-la-na-" ,
176
Gk. 'Ürávgs; perhaps u- ‘good’ + tāna- to root tan- ‘stretch, extend’ (§164.II), Av. Skt. tan-, Gk. telve, Lt. tendit, cf. Skt. tdna-m ‘offspring’: ‘Hav- ing good posterity’. [апа] nsm. DB 4.83.
utava- adj. ‘strong, in health’: u- ‘good’ + deriv. of tav- ‘be strong’ (§122). utava nsm. DB 4.71f (emendation of HK, ApKT 1.63, 2.29, for KT’s detse, with first and third characters very faint; $541).
ubanuvaniya- sb. ‘good bowman’: u- ‘good’ + Sanwaniya- ‘bowman’. wudanwaniya nsm. DNb 42.
ud prep. and prefix ‘up’, becoming Iran. us- uz- before dentals ($85): Av. us- uz-, Skt. ud, pIE *ud (and *üd in NEng. out, NHG aus): ud with verbal root раф, us- in ustaxand-, u(z)- in uzma- (S84).
ира (i.e. upd, cf. 5140.1) prep. and prefix ‘to- ward’: Av. ира, Skt. úpa, Gk. iad, Lt. s-ub ‘under’, pIE “иро.
(1) Prep. with acc., ‘under, with, m the time of (hardly ‘belonging to’, as taken by Hz. ApI 353): DB 2.18, 3.30; A’Sa 4; А?Ра 23; Sf.
(2) Prefix, ‘under’, in Upadarma-; ‘toward’, with verb ay-; ‘beside’, in upasia-.
Upadarma- sb. ‘Upadarma’, father of Agina: Elam. uk-ba-[lar|-ra-an-ma. From ира + darma- (root dar-), Skt. dhérma- ‘right conduct’ (§163.V): “Не who is under (= behaves himself according to) right conduct’ (so Bthi. AiW 390, with lit.; hardly Upadara"ma-, after the Elam.; hardly as taken b Hz. ApI 190). Upadarmahyá gsm. DB 1.74.
upariy adv., prep., prefix, ‘above’: Av. upairi, Skt. upd, Gk. тёр, Lt. s-uper, Gt. ufar, pIE *uperi (5191.1). (1) Adv. ‘above’, XPh 31. (2) Prep. with ace., ‘over, over and above, upon, according to’: DB 4.64; DNb 4, 32, 46, 49; DSf 27. (3) Prefix, ‘over’, with verb ay-.
upasté- sb. ‘help, aid’: upa- + verbal root slà- (6140.1, $142), ef. Gm. Bei-stand for meaning. upastém asf. AmH 10; DB 1.25, 55, 87, 94; 2.24f, 34, 40, 45, 54, 60, 68, 86, 97°; 3.6, 17, 37, 45, 62, 67, 87; 4.60f, 62; DPd 13; DNa 50; DSf 19°; DSk 5; XPh 32, 45.
Ufrütu- sb. ‘Euphrates’, river of Babylonia:
OLD PERSIAN
Elam. t-ip-ra-tu-i8, Akk. purattu, Gk. Еўфрат
(§75.V, §76.V, §166, $166.II). Etymology un. |
certain, probably a popular etymologizing in OP of a local non-Iranian name, cf. Bthl. AiW 1830; Fick, ВВ 24.310; Justi, ТЕА 17.116; Tm. Lex. 77, Ufrätwā ism. DB 1.92 (not gen., as taken
```


## [2026-09-14T01:58:36.444Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5720,5740p' BRT.txt; echo \"=== manus\"; grep -n \"Manui\\|Manus\\.\\|manui\\.\\|Manui\\.ci\" BRT.txt | head -10"
}
```


### [2026-09-14T01:58:36.518Z] TOOL RESULT

```
Yt.5-  73-
Eiß.  Bed.?  Wohl  Komp.  mit  asan-i\.  —  Vgl.  l asa-iaiia-.  —  O  Gaui  Unsicheres  bei  Jusxl . NB.  42,  HoRN  NpEt   165.  '
•  j.  asabanä-  C  £N.  einer  gläubigen  Frau: -rtaya  nairyä  pouru'jäxstöis  asaenya  "der  ; A.,  Frau  des  /*.  . ."  Ytij.140.  1
Eig.  fem.  lu  tuabana-  (sd.)  "die   aus   der  A.- Familie"».     Vgl.  Yt.  5.  73  und  DST.  ZA.  3. 552.  —  ')  S.  Avdf!-. p.  asaöäriiis:  lies  asbär".
•  j-t  E-  (.  P-)  asan-iaj«-,  j.,  p.  asman-  m." i)  'Stein':  *ja«s(alsAP.)  äi/i{sd.)  maya  äiti darSii"V.g.  11;  —  'sSnaShia'^ ..  vtHiaeh-a' . .  tBiuxha  (sd.)  V,  6. 5 1,  a)  als  Amulet: °samm  *siyaire.ci^rim  (sd.)  abars  *aAurö.- puirS  (sd.)  Yl;4.59-  b)  als  Waffe, 'Schleuderstein,  Steingeschoss':  Uavasca  . . •sanas(a  . .  (NP.)  fraäaxlaitya  V.  Z7.9;  — karjtS  .  .  vazrö .  .  'sänS  atymSJütä  Yt.  JJ. 72;  /.18;  —  jainti  mqm  ahuna  vairya avavata  snai^isa  ya'^a  'sma  iatS.masa (sd.)  Yt/7.20;  —  'sanS  (als  AP.)  tasia drazimnS  katä-masatiks  Aynti  V,  117.43); —  yahmai  .  .  aurvan/a  *yuxta  vJsa %an/asante  (sd.)  .  .  asUnas/a  (als  AP.) vispeMvia  "dem  .  .  die  Renner  am  ge- schirrten Wagen   ziehen  -  .  und  die  all-
s-  noch   A,  2  a)   auch   Plur.*':
maitiyul  spfnisiö  y}  xraoldisting  'sSnö (AP.)5i   vasti  {%&)   Y.^0. 5.  A)   als
Gottheit  (i'asa/o):  'smaium  yazamaide  zqm hu'iatfhiin  yazatim ..  Y.  16.  6;  —  'smaugm :^anvaiil3m  yazamaide  S.  2.17;  —  tqm'ä 'smamm^ä  yazamaidi\.42.y,  —  s.  noch Y.  7. 16   und  A  a.  A  a)    avig  (näml.
ayar?)  heisst  der  27.  Monatstag:  'sna binzats  sürahe%.i.2T,  vergl  2. 27,  Y.  7Ö'. 6-  [Yt.7j.96:  lies  asns.:^anrats">.'\ KompA. ;  Ableit.—  Vgl.  aimd^amani-ZÜ.  — tü.äiniaii'  m.  'Stein;  Himmel',  6ian-:aia-  m. 'Stein;  Himmel';  np,  äsmäit,  samän,  —  S. auch  lU  asi,i^-a..  —  Pü.:  10«^-,  (lu  V.  6): sanken;  äsmän.  S.  noch  Xo.  3,  5.  —  ')  Ober die  gegenseitigen  Beiiehungen  der  Stamm- formen (S  /SSaa  2  mit  No.)  s.  JScnumT Ktit.  88.  --  ')  Them.  —  3)  Pü. :  soHg  i  sani;;ii mil  der  Bemerk.:  ail  kc  mcnSk  yauihinhyök -5:i:iti,i;  s.  daiu  Y.  57.  12,  Vt.  7?,  20.  — 4)  Aus  dem  vorher^.  Verbum  ist  ein  solches von  ähnlicher  Bed.  lu  ergänzen.  —  5)  Pü. : cn  äsmän  1  fraliim  dCim.  Wegen  asma  als  AP. 5.  JScitsimTKriLSgundV.^as.  Ich  halte  die Stelle  für  geslött.  —  6)  S.  auch  V,  5. 25,  wo das  Wort  für  Himmel  ausgefallen  ist.  — 7)  Nach  der  n-Dekl.,  S^ojBem.  — «1  S.  auch Vr.  tl.  2  mit  No.  5.  —  9)  BtHL  IF.  /.  63 Ko.  _   .0,  S.  unter  a!mS.i.^amaHt:
•  j.  a-saya-  i)  Adj.  'der  keinen  Schalten
dby  Google
109
hat,  wiiW:  yim  . .  aurvants  . .  viivSahS •ya  i'UEwiA' Y.  57- 27,  2)n.  (oder  f.  'yiJ-7) im  Du.  Name  eines  Bergs  oder  Gebirgs; ahmat   haca  garayö  /raox^yan  . .   'yaica
VtJ9-4-
Vgl  »i.  ckiya-  f.  'Schallen',  rp.  säya.  —  PO. : *näsäyat,  Npü.:  li  läya.  —  '>  S.  dam  Jn. JAOS,  jS.  XL,  DST.  ZA.  /.  366.
•  j.  a-sarsta'  Adj.  'nicht  gebrochen'  sva. "nicht  gebeugt,  nicht  mutlos  gemacht': taräiuitrlf  'tS  aka  mananha  xruzdya tbaisi.parsiannm  (sd.)  W.ig.\.
PPfP.  lum  ai,  V.fyTiäti,  Ürynd 'fiangit,  frang'- Inr';  vgl  lu  vf.gusiiim  bei  Hörn  NpEt.  205, S.  noch  laray-,  säray:  —  m.  asirla'.  —  Pü.; kit!  afsatüfük  "vom  Gefrieren";  vlL  alter FeMerfürAof'ii/fjiuuniÄ.  (Unrichtig  FrMüller WZKM.  3.  23.)
•  j.  asah-  n.  'Ort,  Stätte,  Platz,  Raum': y8  anyeAe  *'saAya  (LS.)  bansma  */ra- stff^ie^.ioi; — äaire  "saAi  razaaiam(sd.) V.Ä97;  —  atfffi  daoam  °s/f  rämsMäitTm (sd.)  ndil  kuäalJäiim'V.i.i;  iPUZ.,  Vyt. 2'j(?);  —  xrüma  'sl6rs{3is  Subj.)  frasinia danunam  YL  13.  ^S;  —yatca  aakat  %wyqs- brnalrva  'sauham  V.2.23;  —  yäi^a  °sS mai^animca  atmisilSe  äaiära  (sd.)  Yt.  13. 67.  a)  sonst  neben  sSihra-.  paoirlm •sanham^a  Sstiranamca  vakishm  frii' "iwtnspm  .  .  airyatDtn  vaSjB  "als  die  erst- beste der  Stätten  undWohnplätze.."  V.  I.a; Y.  /.  lÖ;  —  hpnti  atiyäscii  °s3sca  sSi^rSsca irirasla..  V.J.  20;  Y.  3.16,  S.  7.28,  2.28; —  äat . .  vazaite  väiS . .  avi  'sä  avi  /gi'irS ai-i  karh'ä  yäis  hapta  Yt  Ä  3  3 ;  —  para  nU ahntät  h<üa  'sarihal^a  ^t^räatca  axslat .,  iia/a  äzätliscaY.g.^y,  —  Adoa..  aktnai •saaAalia  sUrbraläi  paiti.jasata  iii V.  ß.  5  4 ;  55,  57;  —  tä  yai'.yeinti  p>sanahu kavc  'tahi  säi^rafai  Yt.  IJ.  27.
KompA-,  E.   —  Vgl.  ai.  äsä-  f.i);  af7.  dst-Js! ■lieh  aoftalten'.  —  Pü.:  ySi,  Sü.:  sikänam "  S.  daxD  /Schmidt  Plur.  149.
•  j.  a-sä£ayant-  Adj.  'nicht  lehrend';  ys saite  haurvqm  iarasca  xsapanim  ayaztmnö ..  asixsJ  asJäzyS  . .  "..  nicht  lernend,  nicht lehrend  . ."  V.  iS.  5.
Fü.:  ondeullicb.
=== manus
```


## [2026-09-14T01:58:49.707Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ci9ra\\|cÍ9ra\\|ci\\&ra\\|cibra\\|cifira\\|ciftra\\|ci\\^ra\\|ci0ra\\|cithra\" BRT.txt | head -20; echo \"---hu.ci\"; grep -n \"hu\\.ci\\|hnci\\|hu-ci\" BRT.txt | head -10"
}
```


### [2026-09-14T01:58:49.784Z] TOOL RESULT

```
6599:Kopula  hat  keinen  festen  Platz,  bevor- zugt aber  entschieden  die  Stelle  hinter dem  ersten  Hochton  ihres  Satzes,  und zwar  auch  im  Nebensatz.)'^':  ks  nar?  ahl yim  ..i  ..  az3m  ahmi..haomB  asava  \.g. I  f.;  12.  7  (wo  ahmt),  Yt.  7.  7  V,  11-15»', Ä15,  70.54',  74.3^  75.43-48S',  77.17, Az.  7,  Vyt  /;  —  azim  bä  is  ahmt  .  .  yä I  hava  dama  H.  2.  1 1 ;  —  srTrö  ahi  sara- .  'bus/ra  Auksntö  ahi  YL  77.  22;  10.  29', i  76',  79,  80,  72. 1,  Y.p.  25,  70.9',  6"2, 1,  V. '  iq.  6,  70,  VyL  22;  —  asU  (als  Vok.)  bfr?- zaiti  hmäta  ahi  huci^ra  YL;7. 15;  — hai^imifa  asahe  xä  ahi  Y.  70.4;  —  Hica (sd.)  caräiti}  ahi  yqm . .  H,2. 10;  —  yäha vasi  (sd.)  asäum  *ala  anhB  (sS.)  asava Y.77. 16;  —  avdha  izara>uslra)  *a»kä (iS.)'^'  spanya  V./Ä7;  —  a>a..AumäyH.- taraca  ..  atjhäma  Vr.  72.4;  —  mä  hyä>a (2p.)''>  duizaotärB  Vyt.  72;  —  aheca anhlus  yö  astvatS  yasia  asti  manahyä  Y. 57.25;  —  yatea  aAmäl  asti  mazyö  ..  tat tiB   däyala  Y.  (»5. 14;  14^;    —  yayä    asti
7255:aoxta  aAurö  mazdä  N.  2. 3ti.; —  äat(s.Z) frasüsat  andvl  . .  ä°  aoxta  arsdvl  Yt5. V.  22,i  iSt.;  —  aat  (s.  8)  mi paoiry3i T/äi  xSqfne  ätari  .  .  nmänS.paitim yäsaiti  .  .  ä'  mE  Htyäi  . .  v3strjm  ßuyan- t3m  yiJsaiti  .  .  ä-  ml  ^n'tyäi  .  .  sraoi3m yäsaiti  V.  7<S',  18— 22;  —  ci^ra  mürahe frayana  (sd.)  .  .  ä°  Ava  pasu  vira  vase.- xsa'hrö  fracaraüe  (sd.)  Yt.  10.  112;  — mi^nm  ..yaiAe../rada'ial  ahurö  mazdä ban-ar}  düikranqm  . .  ,r  äbyö  di'i^rabyS ..  spasyäti ..  ä'  ..  Yt./o.82;  28,  101  (vor yat),  JJ.68,  H.2.10, 14  iSt,  P.  j^'aSt.  (vor
7536:•  j.  'i-zäta-  Adj.  (fem.  Ha-)  'adeHg,  edel, vornehm':  °ta  F.  7;  —  kainins  . .  "tayi raevasci^raya  H.  2.9;  —  kainlnö  . .  rafvat ai^r^m  (sd.)  °taya  Yt5.64;  —  'tarn  hutao- sam  Yt9.i6.
17191:•  '].  barazavant-  m.  EN.  eines''  Gläu- bigen, BapCasynjg:'  uxsänS  vfhtsravaahB dQralsrüia/ie  {sA.)  'vatd  YtJj.  119;  -— fräci^rahe  °vatB  Yt /_;.  184.
25524:•  j.  umpay-  m.  (auch  mit  ^span-  m.) Name  einer  Art  des  Hundegeschlechts: hau  'pü  (statt  GS.)  HU.äatahe  . .  hau vispanam  .  .  spaci^ranqm  V.  13. 16;  — spä  •pii'V.S.ss'.
26500:—  'ia  yesnya  . ,  ya  äai3  arahSid  paouru- yehya  Y.55.6;  3;  —  vahi^la  ci^ra  .  .  yä *ta  yesnya  Vr.  2_J.  1;  Y.  7;.  7,  Ny.4.  8;  — haurvqm  kandaitlm  'tanqm  yesnyanqm  Y. 35.  Si'Yt.  JO.  ijj,  N.  J2,  Vyt.2c?;  —  Üanam yesnyanqm  handätanqm  kufr3yastanqm  Vr. '■3;  3-T,  5-7>  J2-3.  Y.55.7;  —  'bayam (sd.)  'tanqm  yesnyanqm  Y.  55.  7;  5s Überschr.
26645:a/sH^ra ..Slam  zjmasa^ra  ..  slärB  urvarS.-  •  j.  Starstaeii- f.,  Plur.  Bezeichnung  eines a^ra  S.2.13;  ¥1/2.28—31;  —  stäram\zara  Lager  fiir  Tiere  geeigneten  weichen aßci^ranqm  YtÄ  39;  S.1. 13.  a)  von  und  wannen  Stoffs:  upjia  hl  (nämL  der bestimmten  Sternen  uod  Sternbildern:  >  säugenden  Hündin)  gJtam  iaray»i  {stL) lisirlm  (sd.)  Uänm  razvantgm  *3fanna-  •  tumS.vantshva  (sd.)  kamcit  vä  'Üttam  V. nhuntim   YLÄ  a;  i,  3,  50,  12,27,  18.  5,  7, '  ij.  43.
27830:•  j.,  g.  zaraOoiätray-  patr.  Adj.  (auch fem.)  'von  Zaräku^ra  stammend,  dessen Nachkomme':  isat.västrahe  'rsii..urvaiat.' narahe  °rSit  .  .  hvar3.ci^rahe  'röis  YL y-  98;  —  *isai.vasirahe  °rdis  rumS  ti.ji; Y.2J.  2,  26.  s-  a)    Kar'  il   von  /j«/.-
28479:syaoianail  sarvnß  (sd.)  .  .  *hiBva  uxZäis  ys  nairikaya  ci^ravaityä  ..  paurvö.vasfut
28714:—  insbesondere  zur  Wiederaufnahme  des Subjekts,  das  sammt  Zubeliör  unmittel- bar vorausgeht^:  /  marliyt^  i^i^Vtaxma" näma"  asagartiyc^  hauvmaiy  hamii^iya'' abav^  Bh.  2.  14;  —  /  martiya''  araxa'' nama!'  arminiya''  haldüahya  pu^'a*  hauv udapatatä  Bh.,;.  13;  —  vistäspf^  tnatiä pita  hauv  paT^avaiy  ah<^  Bh,  2.  lö;  — dSrayJ'vt^us  xiäya%iya''  hyc^  manä  pitil hauv  .  .  vasiy  ty<^  naibam  akunaus  X. 7.  3;  D.  4-  ';  —  margui  näma"  dahyäus hauv(fem.)maiy  haHtiyä  abava^  Bh.j.3; 5, 1 ;  —  hya^  du7'aistam  nyäii/  axiatä  (sd.) Äau[fem.}ay  J'urä  nirasätiy  D.5.3J  — hauv  vahyazdätJ'  hyi^  bardiyJ'  agaubatä hauv  käram  fräisayi^  Bh.^.  9;  11;  — käri^  pänJ^  utä  mäda''  Afn*  upä  niilm äh<^  hauv  kamnam  äha^  Bh.  2.  6;l(  — ar^aia  vJptS  arsala  vaipayB  .  .  hau  asti daSi-B  hau*"  .  .  V,  <?.  33.  b)  auf  ein Relativum  als  dessen  Korrelat:  \hy(^ madaisuvä  mäkilt<^  äha*  hauv  *adakly naiy  adäraya''  Bh.  2.6;  —  hyä  J'ura''- mazdähc^  Jramiinä  hauv(ieai.)taiy  gas/ä mä  ^adaya^  D.  6. 6.  II  »)  auf  den  Inhalt eines  Satzes;  in  Kongruenz  mit  dem  (ge dachten)  Praedikat:  kä  hl  asti  n^a?  .  . panca  sota  upäxananam  upäisit  hau  (fem.) Jaiäus  hau  vTsäus  häu^ . .  hau  vispanqm . .  spaci^ranqm  anya  udra  upapa  ". .  das  (ist auch   die  Strafe  für  die  Verletzung)  des
---hu.ci
30193:•  j.  hu-ci3ra-  Adj.  (fem.  'rä-)  i)  'von guter  Abstammung,  Herkunft':  nfm!  *nm .  .  yeAhl  n/maahs  ciinm  Aumahmcä AoxDmcä  hvarsUmcä  Y.^S.i.  t)  'des Anblick  gut  ist,  schön*:  äuiäia  aki  'ra (NSf.)  Yt. /-.  15.
30197:•  g.  hu-cistay-  f.  'die  gute  Lehre':  AvS' tsng  frd^h  pa%m}/tg  (sd.)  'tdis  *carat  Y. 46. 4.  a)  'Inhalt  der  guten  Lehre,  was sie  enthält,  insbes.  was  sie  in  Aussicht stellt,  verheisst':  tai  .  .  vairJm  (näml. mXid^m)  astvaiti  ustänäi  (sd.)  data  .  . xsmäkqm  'tim  ahurä  xrafSui  asä  fraäS v>nz7nä  "diesen  köstlichen  (Lohn) . .  werdet ihr  . .  verschaffen  . .:  was  eure  gute  Lehre verheisst,  o  Ah.,  die  der  Weisheit,  die durch  Äsa  die  Gemeinden  fördert"  Y. 34.\it.
```


## [2026-09-14T01:58:51.280Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD cihr\"; grep -n -i \"cihr\\|čihr\" PHD.txt PHD_mackenzie.txt | head -20; echo \"=== PHD sayag\"; grep -n -i \"sāyag\\|sayag\\|sayak\" PHD.txt PHD_mackenzie.txt | head"
}
```


### [2026-09-14T01:58:51.462Z] TOOL RESULT

```
=== PHD cihr
PHD.txt:125:did ... add other. add dig |YTMAL < А *?{т?1 | N di] yesterday. delete *drém ... (read balgam) drubušt ... add protective. drust [drw(d)st' ... duš-čihr ... add ill-natured. duš-nām [-n^m | (M dwjn'm), N ~] add ill-famed. dušwār [dwáw?l | (M dwjw'r), ... ékanag ... for obedient read loyal, faithful. ~th : for obedience read loyalty, faithfulness. for Farrēbāg... read KFarrēbāy [pinb(^)g] ... frayad |pl(y)d^t' | N faryad] ... delete M pry'd. frazand |prz/znd | ... frusag ... add M prwšg. garódman ... read | P grdm'n. gazdum |gcd(w)m, gzd(w)m |... guftàr ..., ~th : add eloquence. hambar |hm-, hnb] |... add  hamest |hmyst'] whose good and bad deeds weigh equal. ~(ag)an |-(k)^n'] limbo, the neutral station between heaven and hell. delete hammist ..., ~(ag)an ... handarz ... add M °’ndrz. hammoxtan, hammoz-, ~i8n : add learning. hast |TWMNYA < A tmny ; ... add hūg [HZWLYA < A hzyr’; hwk' | M hwg, N xiig] pig. add hūkar(ag) |hwkl(k') | N xükara] porcupine. (not hedgehog) add *huzārag [hwc’lk | N хијага) little, small, few. !jadag ... add fortune. jüdan ... | M jwwdn, jwy- ... add karawuš [kl wš| N ^] wine-press. delete karbunag ... read karbūg |klpwk', klbwk'| lizard. kardagān ... add service (ofthe gods). delete karxēš vds
PHD.txt:164:abarmān [5/mn'] in charge. abarmānd ['pín?nd] inheritance, privilege. abarmānīģ [%n?nyk!] noble. abar-menišn Pf/myn$n'!] proud, haughty. abarón Pf*/xwn! | N wárün] contrary, wrong, sinful. ~ih: sin. abar-6z PóPeoc] stronger. ~ih: mastery. abar-tan [Pltn'] arrogant. ~th: arrogance. abarwēz Pfltvyc | (M *bruyj, N parwéz)] triumphant, victorious. ~ih: triumph, victory. abarzén, v. zmašk, abaxs [hš] repentant; regret. ~ЛЬ : repentance. abaxšāwand [5hP^wnd] regretful. abaxšāyīdan, abaxšāy- [5APd-ytn! | М ?bxPy-, N baxšūdan, baxšāy-) forgive, have mercy on. ~išn: mercy, forgiveness. ~i&nig : forgiving, merciful. labāxtar [*5?*4tl | M 7b’xtr] planet. žabāxtar [PP’htl | (N bāxtar ‘west’)] north. abaydag Pyrťk', v. paydag | M ?byd?g] invisible. ~th: invisibility. abày- : abayéd ['yt' | M Maud, N bāyad] it is necessary, fitting; must (+ infinitive). ~ist Pf?dst' | N bāyist] it was necessary. ~istan [?P?dstn!] be necessary, fitting; desire, want. ~išn: necessity. ~išnīg : necessary, fitting, seemly. abāz [L AWHL < A lI2(w)hr;?Pc | М Рс, N baz, wa] back, again, re-. ~ айдап б: attribute, ascribe to. 7 appoint t= ~ dāštan: withhold, restrain, prevent. ~ ēstādan az: abandon, desist from. — kardan: open. — kardan az: disengage from, wean. ~ mándan: remain behind. ~ pádan: remain, stay. — raftan : issue, go forth. ~ waštan O: turn into, become. ~ wirāstan: rearrange. abāzsār [LAWHLs'I] rebellious. ~ih: rebellion. āb-čihrag [$ cyhlk'] holding the seed, essence of water. abd [>24 | М "Gd J ?bd-] wonderful. ~ sahistan: seem wonderful (to) > marvel.
PHD.txt:298:čāšt [ой | N ~] lunch, meal. 1~ag [-k'] food. &а$їар [c'štk'] doctrine. čāštan, čāš- [c?s-tn'] teach. ~išn: teaching. čatrang [cting | (Ar. šatranj)] chess. *taw(la)gan [cwpk'n!! | Ar. sawlajan, N čaugān] (curved) polo-stick ; polo. CaxSágih [ch kyh] (sense of) taste. čaxšišn [chsfn! | M, J схі, N ¿aš-] taste, flavour. 148 [ME < A mh | M cy, N či] what, which. ~ ray: for what, why. ~ih: quiddity, essence. tčē [ME, v. 166] for, because, since, as, that. &ë-ëwënag [ME ^ dwynk!] how. ~ith : circumstances. čegām-iz [су?т-с | M cyg^myc], —-6(w): a little; whatever. Cegámag [cyk”mk! | N &(ag)áma] song, snatch. €éh- , —išn, v. idan. *téhag [cyhk'] grief. čehel [40 | N chil] forty. Céh-widarag [cyhwtlg] = činwad puhl. čēlān [cy”x! | = M, N ~] dagger. ~gar [-kl, -gl | N ~] swordsmith. Cér [cyl | M cyr, N —] victorious, triumphant, brave. —Ih: bravery. Cérihistan, Cérih- [cylyh-stn'] triumph, be victorious. īčīdan, čīn- [cytn', cyn- | M cyydn, cyn-, N ~] gather, pile up. ~išn: gathering. *čīdan, čēh- [cytn', cyh- | M cy-] mourn, lament, grieve. ~i8n : lamentation. ~i$nig¢ : mournful. ihr [cyhl | M cyhr, № ~] form, shape, appearance, face. žčihr(aģ) [cyhl(k') | M сулу, P -g, № ~] seed, origin; nature, essence. Cihrénidan, čihrēn- (cyhlyn-ytn'] form. Cihrig [cyhlyk'] natural. čihr-šnāsīh [суйру] physics. čim [c(y)m | M сут, N ~] reason, cause, purpose, meaning. ~ (ray): why? Cim-gó6wáàgih [сут gwh’kyh] logic. čimīģ [cymyk!] purposeful. čīn-, ~i8n, v. idan. čīnag [cynk! | P cyng, N ~a] grain, bait. Cinàr [су | N ~] oriental plane tree. činwad [cynw(p)t'], ~ puhl: the ‘divider bridge’ which separates the souls of the righteous dead, who cross, from those of the wicked, who fall off.
PHD.txt:315:drón yastan 28 duš-čihr
PHD.txt:398:P hd [Aw' | = P] that, he. Hóm [kwm | N ~] the sacred plant Haoma (ephedra). homānāģ [h(w)m’rk' | N hamana, J xumana], 6 .. . ~: like. ~th: likeness. hómast [hwn'st!] various series of prayers. hómyjén, -ïg [hwmyn!, -yk'] of Haoma. ~ӧтапа [-'wmnd] prepared with Haoma. Ногааа [hwrdt' | M hrwd'd, N Xurdād] Perfection, the fifth Amahra- spand, guardian of water; cal. 3rd month; 6th day. hdsag [hwsk' | М лое, N xēša] ear of corn, cluster; astr. Spica, Virgo. hēšēnīdan, hoSen- [hwsyn-ytn'] (cause to) wither. hēšīdan, hēš- [hws-ytn' | M hwi-, N x~] dry up, wither. héy(ag) [hwy, -k! | M hwy] left(-hand). Hróm [hlwm | M hrwm, N Рат] Byzantium, Rome. ~ayig [-dyk'] Greek, Byzantine, Roman. hu- [hw- | = M] good-, well-. ~ih: good, goodness. hu-bóy [hwbwd] sweet-smelling, fragrant. ~th: fragrance. hu-čašm [hwesm] unenvious, benevolent. ~ih: benevolence. hu-čihr [hweyhl | M hweyhr, (N xujir)] fair, beautiful. hudà(ha)g [hwa?(h)k' = Av. hudàáh-] good, beneficent. ~th: beneficence. hu-|-dast [hwdst'] skilful. ~-dén [-dyn'] of good (i.e. Mazdean) religion. ~-ddsSag [-dušk'] very pleasing. m-ēwāz [-"yw'c] of good speech, affable. —-ëwàzih : affability. ~-fraward [-plwit'] blessed, the late. hugar [hwgl] easy; beneficent. hu-|-&ówisn [hwgwbsn'] of good speech. ~-gugar [-gwk’l] easily digestible. ~-kunign [-kwnsn'] of good behaviour. „-mānīh [-m’nyh] good-mindedness, benevolence. humat [hwmt' = Av. humata-] good thought. humāy [hwm’y | N ~] a bird of good omen; eagle. hu-menišn [hwmynsn'] of good thought. hu-murwāģ [Awmwlw’k'] auspicious. hunar [hwal | M hwnr, N ~] virtue, ability, skill. hunarāwand [kwn wnd | M hwnr'wynd] skilled, virtuous. ~th: skill, virtue. hunarómand [kwn wmnd | N hunarmand] = hunarāwand. hunidan [kwnytn'] extract, express (juice). huniyág [/sonyd?k! | N xunyá] delightful. ~th: delight, entertainment.
PHD.txt:813:appearance čihr, dés(ag), paydagih.
PHD.txt:953:beautiful hucihr, nëk(óg).
PHD.txt:1801:essence ¢éih, čihr(ag), gēhr(ag), mādag, mādayān, xwadih, uruspar.
PHD.txt:1865:face čihr, róy.
PHD.txt:2010:form (n.) brahm(ag), čihr, dēs(ag), éwén(ag), gēn(ag), jadag, kālbod, kirb; of the same — hamdēsag.
PHD.txt:2279:hideous duščihr.
PHD.txt:2891:natural čihrīg, góhrig.
PHD.txt:2892:nature čihr(ag), góhr(ag); Ciyonih; xem, хор.
PHD.txt:3002:origin čihr(ag), fragàn.
PHD.txt:3118:physics čihr-šnāsīh.
PHD.txt:3560:seed čihr(ag), dan(ag), tóhmag, tóm; having many ~s was-tóhmag.
PHD.txt:3616:shape čihr, kālbod.
PHD.txt:4107:ugly duščihr, zist.
PHD.txt:4592:беһ- čēh-widarag čēhag 1-2čihr čihrēn- čihrēnīdan čihrīg cihrag čihr-šnāsīh čēhišnīg čēhišn ет! &yónih
PHD.txt:5392:duSfarrag dušfarragīh duščihr duščašm duščašmīh Чома gost düd jüdan düdag gawdar gaz- vau yaštant nay-! nidant gazidan gazīdag nay-! nidant
=== PHD sayag
PHD.txt:392:hamēstār, —ih [hmyst!l, -yh] = hamēmāl, ~ih. hamésag [hmyfk! | M hmyšg, N —a] always. ^h : eternity. ~-86z [-swe] ever-burning. hamē-wahār [hmy whl | N haméfa-bahar] marigold. ham-éwénag [Am'dwynk!'] of the same kind, homogeneous. ham-góhr (hmgwhl! | M hmgwhr] of the same substance or nature, consubstantial. ham-ginag [hmgwnk! | M hmgwng] likewise, so. P hāmharz [A())mAlc | P I? mhyrz] adjutant, attendant. hāmīn [A*myn! |= M] summer. ~ig [-yk'] (of) summer. hāmist [KHDE, v. hammis ; )”mst!] all. ham-kār [hmk’l | N ~] collaborator. 7h : collaboration. hāmkišwar [mkyfwl | M. -wr] universe. hammis [KH DE < A k-hdh), ат... ~: together with. hammist [hmyst'] stagnant, peaceful. ~(ag)an [-(kYn'] limbo, the neutral station between heaven and : hell. vl hammóxtan, hammoz- [ALPWN-tn! < A У "Ip: hmwhtn', hmwc-, Ki hmsoz- | M hmwxtn, N āmēxtan, ámóz-] teach; learn. -išn: teaching. hammdxtar [Amwht?!] learner. ~th: learning. hammóz- , ~i8n, v. hammóxtan. —@йг [kmwcek?l | N āmēzgār] teacher. ham-nibardih [hmnpityh] (single) combat. hamēūģ [/tmwg] equal, like. hámón [k mwn' | N kāmūn] level, flat. hámoyén [/?mwdyn!] all. ham-pursag [hmpwrsk!] consulting, taking counsel. ^h : consultation. ham- |-ránih [Am nyh] battle, combat. ~-samiain [-s"m?n!] contiguous. ~-sardag [-sltk'] of the same kind, like. ~-sayag [-sdk! | N hamsáya) neighbour. ~-tag [-t*k! | N hamid] equal, peer. «tan [-tn'] of the same stature, build. ~=-tihmag [-twhmk'] relative, relation. hamwar [hmwl | N hamwār] level, abreast. hámwiür(ag) [%()mw?/, -k! | N hamwdara] always. ham-zamān [hm ODNA | N —] instantly, immediately. handām [And*m | = P, N andàm] member, limb. handarz [hndle | N andarz] advice, injunction, testament. handarzénidan, handarzén- [hndleyn-ytn!] advise.
PHD.txt:564:sang [KYPA < A kyp’; CCA (in error); sng | (P?sng), N ~] stone, rock. -~sar [-s?1] stony place. sanj-, v. saxtan. sanwar [snwl = Av. 0anwar-] bow. sar [LOYŠE < A r'šh; sl | M sr, N ~] head; top, summit; end, begin- ning. | sarāsar [s?s] | N ~] from end to end. sard [s/t! | M srd, N ~] cold. ^Àh: coldness. sardag [sltk' = Av. sarada- | (M s’rg), J srdg] sort, kind. sardsér [s/tsyl | N ~] cold region, uplands. sārēnīdan, sárén- [s’/yn-ytn'] provoke. sargen [slgyn' | N sargin] dung, manure. sarmāģ [s/m?k! | N затта] coldness. sarw [slw(b)' | M srw, N ~] cypress. sas [ss | N ~] bug. sāstār [s”st”7 | P s?s?r] commander; tyrant. ~ih: tyranny. Sawah [sw’h = Av. sawahi-] the western continent of the earth. saxt [sQ)At! | N ~] strong, hard, severe(ly); very. “Аһ: strength, severity. saxtag [shtk! | (N saxtiyán)] morocco leather. saxtan, ѕапј- [s’htn', snc- | N ~] weigh. sāxtan, sáz- [s*htm!, ?c- | (P s?*c-), N ~] make, prepare; tolerate. sāxtārīh [Pht yh] toleration, forbearance. saxwan [МРУА < А mly’; shwn' | М sxwn, N suxan] word, speech. say-, v. südan. sayag [sg dk! | M ғур, N sáya] shade, shadow. lsaz- [sc- | M sz-, N ~] be fitting, proper, worthy. --i$n(ih): fitness, worthiness. 26а2-, —išn, v. sazistan, saz-, v, sáxtan. sazāģ [sk | N sazá] fitting, worthy. ~th: fitness, worthiness. ~ ~war [-w/ | N sazāwār] = затар. sazistan, *saz- [sc-stn'] pass. ~išn: passing, transience. ~iSnig : transient, perishable, mortal. sé [3; TLTA < А tl? | M sh, N si] three. sëb [syf | N ~] apple. sēj [sye = Av. 'Gyejah- | N ~) danger, trouble. --ómand [-”zvmnd | N —mand] dangerous. sel [si | N —] spear, javelin. sém [sym | N —] — asém. !sén(ag) [syn(k)! | N sina] breast, chest. *sén murw [synmzlw | (N simury)] a fabulous bird.
PHD.txt:2907:neighbour hamsayag.
PHD.txt:3610:shade, shadow sāyag.
PHD_mackenzie.txt:2780: --sAyag [-s)dk l I N hamsiiya] neighbour.
PHD_mackenzie.txt:4523:sayag [s'dk 1 M s'yg, N saya] shade, shadow.
PHD_mackenzie.txt:7149:neighbour hamsayag.                    observation nigerisn.
PHD_mackenzie.txt:9042:raftanl            \\~ \\ tV\).)        sahig, sayag                \~
PHD_mackenzie.txt:11582:bastan[            \,~,~          hamsayag             ,~
```


## [2026-09-14T01:59:06.114Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"•.*ci\\^ra\\|•.*manui\\|• *j\\..*manu\" BRT.txt | head -20; echo \"=== manus.ci\"; grep -n \"manui\\.ci\\^ra\\|Manus\\^\\|manus\\^ci\" BRT.txt | head"
}
```


### [2026-09-14T01:59:06.226Z] TOOL RESULT

```
5458:•  j.  arsSa-,  p.  arda-  i)  Adj.  'halb' (nur  Komp.).  2)  m.  'Seite':  *atitar?m (sd.)  'tijm  mayaAe  V.p.29;  —  antar?m 'fam  nmanaheV.6.i,y,  — dasinim  (vair- yastärtm)  hl  upa  "htm  Yt.  10. 100';  — visps  he  upa  'wun  (lies  -o!)  \tio.ioo; —  äasimm  hl  'Öe..  Aävöya  hl  "%€  "rechts (links)  ihm  zur  Seite", Yt. /o.  ia6;  —  ww- %asö  (sd.)  gairis  parmtarim  °c,5  (AD.) manuiahe  YL/p.i.  [V.  5.19,  5.33,  Yl j".6o:  lies  antar».am>m^
5570:•  j.  airyava-  m.  EN.  Name  eines  Gläu-  des  Viitäspa-.  pu>ri>m  yat  'fa/ie  taxm>m bigen:    manuS.airahe  (sd.)    'vahe   asaonS  kai-alm  züstJspfm  Vtj.  105.
7536:•  j.  'i-zäta-  Adj.  (fem.  Ha-)  'adeHg,  edel, vornehm':  °ta  F.  7;  —  kainins  . .  "tayi raevasci^raya  H.  2.9;  —  kainlnö  . .  rafvat ai^r^m  (sd.)  °taya  Yt5.64;  —  'tarn  hutao- sam  Yt9.i6.
10495:•  j.  gram-  V.  'erglimmen,  Grimm  hegen'. ;     "  I"»  Gegens.  lu  manueSfi-,
17191:•  '].  barazavant-  m.  EN.  eines''  Gläu- bigen, BapCasynjg:'  uxsänS  vfhtsravaahB dQralsrüia/ie  {sA.)  'vatd  YtJj.  119;  -— fräci^rahe  °vatB  Yt /_;.  184.
19842:•  j.  manu/-  m.  ES.  eines  alten,  vorsag- lidien  Helden.
19844:•  j.  manuSa-  m.  Name  eines  Bergs '>: afr^atB{sA^  gairi/ pärmtar^m  ar^d  °lahe Ytiff.i.
19847:•  j.  manuä.£i3-ra-  in.  EN.  eines  Gläubigen: *%raie  airyävafu  asoönö  "des  M.,  Sohns des  A.  .:•  Yty.  131.
25524:•  j.  umpay-  m.  (auch  mit  ^span-  m.) Name  einer  Art  des  Hundegeschlechts: hau  'pü  (statt  GS.)  HU.äatahe  . .  hau vispanam  .  .  spaci^ranqm  V.  13. 16;  — spä  •pii'V.S.ss'.
26645:a/sH^ra ..Slam  zjmasa^ra  ..  slärB  urvarS.-  •  j.  Starstaeii- f.,  Plur.  Bezeichnung  eines a^ra  S.2.13;  ¥1/2.28—31;  —  stäram\zara  Lager  fiir  Tiere  geeigneten  weichen aßci^ranqm  YtÄ  39;  S.1. 13.  a)  von  und  wannen  Stoffs:  upjia  hl  (nämL  der bestimmten  Sternen  uod  Sternbildern:  >  säugenden  Hündin)  gJtam  iaray»i  {stL) lisirlm  (sd.)  Uänm  razvantgm  *3fanna-  •  tumS.vantshva  (sd.)  kamcit  vä  'Üttam  V. nhuntim   YLÄ  a;  i,  3,  50,  12,27,  18.  5,  7, '  ij.  43.
27830:•  j.,  g.  zaraOoiätray-  patr.  Adj.  (auch fem.)  'von  Zaräku^ra  stammend,  dessen Nachkomme':  isat.västrahe  'rsii..urvaiat.' narahe  °rSit  .  .  hvar3.ci^rahe  'röis  YL y-  98;  —  *isai.vasirahe  °rdis  rumS  ti.ji; Y.2J.  2,  26.  s-  a)    Kar'  il   von  /j«/.-
30190:•  j.  hu'xsnütay-  f.  'gute  Befriedigung': tbiltahecii  ax^nuHake  müra  manu  räma- yeiti    'üittm  paiti    mihrahe    ".  .  bei  (Sp.
=== manus.ci
```


## [2026-09-14T01:59:13.140Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^• *j\\.\\, *g\\. *ci\\|• *j\\., *g\\.  *ci\\|Same.*Geschlecht\\|'Same'\" BRT.txt | head -20; echo \"--- try\"; grep -n \"ci\\^ra-\" BRT.txt | head -20"
}
```


### [2026-09-14T01:59:13.218Z] TOOL RESULT

```
11326:•  j.,  g.  'äiSra-  (,  p.eßi''a-)  n.  i)  'Same', im  eig.  Sinn  (nur  Komp.).  2)  'Urspmng, Herkunft,  Abstammung':  *JhiaJi^ra  .  . Ajiiii  iristanqm  un'qitH?  .  .  spmtäl  haca mainyaot . .  aisqm  'rsm  FrW,  10.  39  f.;  Yt. 8.  4;  —  kainlnS  . .  pritiiaikyS  ratvat  "/vm  '* äzätayh  "eines  Mädchens,  . .  eines  gerad- gewachsenen —  reich  die  Herkunft  —  eines adeligen"  YL5,  64;  —  mmS  huci^r>m  .  . yetihl  n>manhg  °r>m  kumatimcä  . .  Y.  5Ä  ]
21999:Eig-  Bed.?  Die  Übersetzung 'germe  de»  Wiy"*'. 'the  Iranian  secd'  fusst  auf  der  falschen  Ver- bindung von  vaijah-  mit  np.  blj  'Same''); vgL  nba!.  hij,  ai.  bijam,  die  ar.  Ä*  erweisen, S  14.  ~  i)  Them.  —  »)  Nach  HoRK  NpEt. XIX  exislirt  das  Wort  überhaupt  nicht.
--- try
```


## [2026-09-14T01:59:18.949Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '11300,11340p' BRT.txt"
}
```


### [2026-09-14T01:59:19.001Z] TOOL RESULT

```
•  g.  *cäätav-"  :  'aiw-  Adj.  'bedachtsam, sorglich':  «"J^rJj'J (sd.)  ns  :^'a^rmt  dai- dU3  %wä  'ciiwS'^  [iB-y  sfisnis/a  mainys masda  ", .  soll  er  das  Paradies  empfangen durch  deinen  sorglichen  heiligsten  Geist, o  M."  Y.4?-2-
Znm  V.  ka^l-.  —  «.  vgl.  cikitäu.  Adj.  —  Tu. : lö  failäkea  (iSImp.,  Sü.:  ^oiä/oya),  erl. ;  tö galt!  ku  ^arrikötnand  mart  ii,  ces  pa  tS  /aJ- läkih.  —•  ■)  So  mit  jünger«!!  Hds.;  die  älteren leireissen  das  Wort  NA,  nn%wä,  aber  KZ. _jo.  317  H!i%'.  —  ")  So  nach  KZ.  30.  323, wozn  ZDMG.  46.  394.  Nach  Mills  G.  510 "chuhllkmä  . .  is  a  pert  imperat. . .  miswritten for  elüehU.H/pä" ;    das  ist  mir  nicht  fasslich.
•  j.  ädiawah-  Adj.  (fem.  '%u^-),  PPfA.:
s.  ktm-.
KompE.  —  S.  fiiüiviah-.
•  p.  citä  ■'  Adv.  'so  lange',  mit  folg.  yätä 'bis  dass':  dädarHi  c'  mäm  amänaya''  .. yäta  adam  arasam  msa'aOT  Bh.2,  9;  6,  11.
Eig.  tU.  'D.  wartete  auf  michi  wie  lange?  Bis dass  . .' ');  dann  Ableit.  aus  'kay-,  %  2J2.  4-  — >)  Oder  cUä,  mit  der  Länge  wiej'i/fl.  —  »)  In Aü.  und  Eü.  fehlt  das  Wort.
•  j,  äS-ay-  f.  'Sühne'  durch  Geld,  Ver- mögen': lanar»  vazyanam  aismanqm  .  . ahre. .  urune  °%Xm  nisiririuyät  "..  für  seine Seele  als  Sühne  . ."  V.  14. 2.  DS.  '^a- yaica  als  Inf.  sbes.
Znin  V.  käy-;  %  iSg  mit  No.  3.  —  VgL  ä^ä-, —  Pö.:  tSHsH.
•  j.  ci9«yae-«!  Inf.  '(und)  durch  Geld-, Vemjögensstrafe  zu  sühnen':  *i?arS  nött hl  afihat  «ä*  upaMntayaica  (sd.)  N.  45-
Zum   V.  käy-.  —  VgL  c&ay-,  —  Pü.:  töäin.
•  j.  äÄS-  £  'Busse,  Sühne'  einer  Übeltat, uzw.  durch  Geld-,  Vermögensstrafe:  ks Al  asti  '>a  ia  Äi  asti  äptritis  (sd.)  kat hx  asti  yaoidshntn  (sd.)  "wie  kann  man ; das  durch  Vermögens.,  wie  durch  Leibes- 1 strafe  sühnen,  wie  kann  man  sich  davon  j entsündigen?" V.J. 38;  39,^107.  a)über- haupt  'Strafe"':  ka  kl  asti  °%a  "was  ist die  Strafe  dafür?"  V.J.  36,  4.",  «8,  20,! ai,  55.  5-2.  S.  43.  6^-4.8.  10,47,  7-72,, 8,  33,  26,  104,  p.49,  7J.4,  12,  24,  14.  I, 15-50,  iÄ-13.  14,  16;  F.jp;  —  paitita (sd.)  fü!  •ä«  V.J.  21;  —  vaauhi  dalna  . .
'"harn  %w>r3saiti  V.j.  42;  7.71*;  —  ä/s °^qm  ^fraoirisyäti  V.  H,  104;  106;  — .  .  Hkayat  .  .  baots.varstahe  (sd.,  auch fdSt)  ''^aya  V.  7, 38  usw.;  —  xlaydte hl.,%risum  aUahe  'äi  (GS.)  apanharstse "er  kann  ihm  ein  Drittel  von  der  Strafe dafür  erlassen"  V.5.  26.
KoropA.,  E.  (vgl.  acAeirilla-).  — Zum  V.  iSy-. —  Pü.:  täiisn,  zn  V.  3.  38 f.,  S.  107  mit  der ErL:>o  i^äslai.—  O  WeU,  wenn  nicht  alle, so  doch  die  meisten  andern  Strafen  in  solche am  Vermögen  umgesetzt  weiden  konnten; vgl.  IF.  10.  Sf- •  j.  ttütt  sX  äl  asrao^yanqm  tanunqm  alahe urva  "ä^iäi  ^vfoaiti  P.  15.
VgL  V.  14.  2.   —   Pü. ;  B?  .  .  airäüh  ö  ruvän löHin  *1nndtt.
•  g.  £i9^nä  Part  zur  Einleitung  der  Frage
'num?':    c°  mazda    huxsahra  (sd.)    daSoä
ätakafS  t.44-  20.
Verbindung  von  Ht,  ASn.  aus  'iaj'-,4'''ö,  Frage- pait.,  ar.  **Jti(Pausaform)-B3;  lat.  juid-ne.  — Pü.!  Xsön  hakirL
•  j.,  g.  'äöra-  i)  Adj,  (fem.  °ra-)  'mani- festus,  offenbar,  klar,  sichtbar,  augenfällig': ttü  Im  vTspa''>  °r7(NSm.)  zi''>  mazdanhs.- düm(sd.)  Y.43-i;  —  "nm  ahurim  mazdam Yt.j.  4;  —  ävil  nh  atUar?  hSntü  ..  °rS raiays  (■&&.)  Y.  JJ.  7 ;  —  -ri  (NPn.)  mi'irahe /rayans(sd.)Yt.  10.112;  —  'ra  vS  buyärss masänä  'ra  vö  zatan^.savS  (sd.)  'nm  bsit yäifmÜt  :^ar3n3  .  .  dayata  Ny.j.  n;  in ungeschickter  Verwendung  Vyt.  7f.;  —  "nl (NPn.)  J  kudiiahs  .  .  valdymnai  (sd.)  ■  . Y.J/.  32;  —  °/vm'>  dasvan  bassaz?m  Y. 10.  7.  2)  n.  'Gesicht';  a)  sva.  'Anblick': taica  .  .  awÄÄ/  vahistahe  're  paityanie "und  die  Werden  des  Anblicks  des  Para- dieses teilhaftig  werden"  P.  4g.  b)  sva. 'Anthtz':  yB  paoirys  'nm  urvaäayaia  (sd.) .  .  haolat  Yt.  13.  89;  —  mßinm  ..  *yahmi paiti  'rim  vlhatsm  vJspais  avi  karsvqn Yt  10. 64.  c)  sva.'  Vision,  Erscheinung' : 'ra  (IS.)  msi  dam  *ahUmMLratüm  (sd) ciidi  '^.44-i(>.'  d)  sva.  'äussere  Er- scheinung, Gesammtheit  der  äusseren  Merk- male', spez.  von  der  Menstruation:  ya} kl  'ra  daxst>m  havaiti  yat  kl  daxsta 'r?m  bavaiH  V.  16.  i4[?)^'I  —  s.  Ab- leit*' 3)  'Kundgebung';  vJ  daSväis  .  . sarpm  mruyi .  .  vi  manSbTs  vi  valsbxl  vT syao^anais  vi  'rai/  Y.  12,  4.  a)   sva
dby  Google
S87
»ä*ra-
'Offenbaiung* :  vahista  'ra  (AP.)  yatamaide y3  itaota  yesnya  Vr.aj.  i.  Undeutlich: :fahmi  dam  :^ahmi  're  Vr.  i4-'i;  —  tat 'nmca  N,  65*';  —  'nmctt  N.  67*';  —  äat haca  'nm  FrW.^.  2;  —  wertlos:  'nm buya  tämäi  ..  Vyt^.         [Yt/o.  67:  lies
KompA. ;  Ableil.  —  ai.  rilrä-  l)  Adj.  'augen- lallig',  2)  □.  'Erscheinung';  np.  ri^r 'Gesicht'.
—  PiL:  failät  (SQ.:  fraialaA),  pallikih;  %. noch  No.  3-4.  —  VgL  auch  >n%ra-.  — ■)  Die  Worte  li%ri  (näml.  ahuri)  xT  bilden einen  Zwischen  salz.  —  >>  Vä.:  faiiäiinii.  Sä.: pratäiaj/ali.  —  J)  Pü.;  täi  ta  an  i  di  Hktab (s.  No.  4)  daxiai  Sovel .  ,  cääv  an  i  öi  daxsak hhr  bavel.  —  1)  Pü.:  hhrak'.  S.  No.  3.  — ;]  AbgCTissene  Zitate  ohne  Fü.
•  j.,  g.  'äiSra-  (,  p.eßi''a-)  n.  i)  'Same', im  eig.  Sinn  (nur  Komp.).  2)  'Urspmng, Herkunft,  Abstammung':  *JhiaJi^ra  .  . Ajiiii  iristanqm  un'qitH?  .  .  spmtäl  haca mainyaot . .  aisqm  'rsm  FrW,  10.  39  f.;  Yt. 8.  4;  —  kainlnS  . .  pritiiaikyS  ratvat  "/vm  '* äzätayh  "eines  Mädchens,  . .  eines  gerad- gewachsenen —  reich  die  Herkunft  —  eines adeligen"  YL5,  64;  —  mmS  huci^r>m  .  . yetihl  n>manhg  °r>m  kumatimcä  . .  Y.  5Ä  ]
I.  3)  'Geschlecht,  Stamm,  Nachkom-, menschaft':  gayeie{sA.)  inarti^nS .  .yakmal haca  /räiw^nsat  (näml.  ahurö)  najö  .  , 'nm  airyanqm  dahyunam  Yt.  i_j.  87;  — 'r>m  buyät  ahmya  nmilne  "Nachkommen- menschaft  soll  in  diesem  Haus  , ."  FrD. /;  —  °ra  F. ig.  a)  mit  Abi.:  at yss dasvä  . .  akät  (sd.)  manauhs  siä  °r?m  Y. 32.  z.  [!'D.6.2:  lies  ariyt^.cfii''a^.] KorapA-,  E.;    Ableit.  —  np.  fihr  'Ursprunß'.
—  Et.?  Die  angenommene  Gleichheit  mit 'ci%ta-  (sd.)  gilt  mir  für  unwahrscheinlich.  — Pü.:  löxmaii  (lU  FrW.  und  FrD.):  pal/äm, s.  'h%ra:  —  ')  H.  2.  9  steht  statt  dessen rar^'asä^rayi.  Ist  M/Ta/  ä^rjm  richtig  be- zeugt, so  kann  es  nur  als  Zwischensati  ge- fasst  werden.
•  j.  *äOTa.avah-  Adj.:   s.  unter  /liJ/-,!.-
avah:
•  p,  tSi&'a°'taxma-  m.  EN.  eines  Sagar- tiers,  der  sich  gegen  Darius  I.  empörte,
Tpnix,Tnai-fji.-^i:  'm<^'  mliiia"  asagariiya" hauvmaiy  hamd'^iya''  abavJ'  Bh.  2. 14; 4.  2,  g;  —  laxmaspada''  .  .  Aamaranam akunam  hadä  °mä..utä  °main  m^arbäya'' Bh.  2. 14.
Komp.  mit  AS.  im  1.  Glied?  Vgl.  Richter IF.  p.  203,  FüY  KZ.  3^.  504,  wo  auch  iLes. and  Litt.
•ät  I  I  I  588
j.  c&rttvaohqm:  lies  cAra-av'.
•  j.  äÖxa'vant-  Adj.,  nur  fem.  °vaiti- 'an  der  die  Zeichen  des  Geschlechts  sicht- bar sind,  die  die  Regel  hat':  yat  ahmt ttmüne . .  nairiia  °vaiH  daxstavaiti  vohuna- vaili''*  nishioäi  Y.iO.  i;  —  yS  näiriiqm 'vaitlm  daxstavaitim  vohunavaitXm  xsudri avi  */rai?Äansaiti  V .  15.  T ;  /Ä  67;  — yS näiriiayä  'vai'tyä  daxstavaityh  vohuna- vaityä  ^ari^^tm  frabarat  V.  26,5;  13,  14.
Pü.:  ährSmand,  erL:  lar/'gelb'.  —  i)  Ich  halte die  drei  Ausdrücke  €',  d',  v'  (ür  synonym  ;  an. ders  Ggr.  OK.  260.  Sie  sind  überall  verbun- den ausser  V.  /.  59,  wo  doistaraili-  allein vorkommt
•  g.  CiSriLavah-,  j,  ^Äiftra.avah- "  Adj. 'deutliches,  augenfälliges  Ergötzen,  Behagen schaffend':  at  tsi  atrSm  ahurä  usSmakJ.. ^aslstjm  imavaithm  f/ö((sd.)  raparUE  'vav- h)m  ai  .  .  "von  deinem  Feuer  {Ätar),  o Ah.,  . .,  dem  verheissenen ,  machtvollen, wünschen  wir,  dass  es  dem  Getreuen  augen- fälliges Behagen  (schaffe),  aber.,"  ^.34. 4*>;  —    narqm  ..  *°Z'anhqm  Ny.j.  10'*.
*)  Die  Stelle  bezieht  sich  auf  den  feurigen MetallBtrom  beim  jüngsten  Gericht,  vgl.  Bd.  jo. so  und  unter  hulay-.
PS.:  S  ayä^oär  as  fa\läkrn?l  (3S.)  rämiin;  die
```


## [2026-09-14T01:59:42.924Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} {for(i=1;i<=1;i++) if ($0 ~ /Ciça|Cica-|cica-|Cicantaxma|Cicixri/) print NR\": \"substr($0,1,300)\"\\n----\"}' KNT.txt | head -40"
}
```


### [2026-09-14T01:59:43.962Z] TOOL RESULT

```
21: gs and uses; fuller discussion will be found in the phonology and in the Lexicon, s.vv.:
I. Place-Names:
Asagarla ‘Sagartia’, a district of Media, with
s in asa- from Ё if it means ‘stone’. Sikayawati$, a Median fortress, with s- from
Ё if, as is probable, the first part is identical
with 
----
46:  sahá, from pIE *sm-dhe; same suffix in avadà, idä, ada-kary.
With Skt. d from pIE dh by Grassmann's Law (§73.IV): pIE *dhrugh-je- in OP adurujiya ‘he lied’, Skt.
drihyati ‘he deceives’, Gm. friigen; pIE
*dhrougho- in OP drauga- ‘Lie’, Skt. dróha-
drógha- ‘injury’. pIE *dhighé
----
69: ed on -vand- (pIE -џепі-) or on zero grade $
ES OM = AM epu ein bo Ny SNS БАМЫ
paps PEE Rs
pro Se yok
also in A'ura- d
-vat- (pIE -021-); more probably they are made -
upon vat-: ar-uwant- in aruvas-ta-, sikaya "-want- in `
Sikaga^uval-i-, hara^-uvant- in Hara*uvat-i-. )
NOUN STEMS 58
$168. 
----
71: 61.1.Ь.), ‘Having a - 4
shield of weaving, = wicker shield’.
$163. Names or Persons in the OP inscrip- tions must be divided according to nationalities, which in the main show the linguistic nature.
I. Names of Persians are far the most nu- merous; but some show Median phonetics, indi- cated by
----
155: ha : a
10 vjaiy :
DBE 1 :iyam : Fra 2 vartiš : 3 aduru 4 руа : ava
5 08 :авћа: айат; > |
6 Xšaðrita : amiy
7 : Uvaxštrahya
8 :taumáyà : adam 9 : xSdyaéiya : amiy 10 : Mà
П дау:
4 dam : Imanis : am 5 iy : Uvjaiy : x
6 Sàyai
Т ya:
```


## [2026-09-14T01:59:46.735Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 206 207 208; do echo \"=== leaf $n ===\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' KNT.txt | head -c 1500; echo; done"
}
```


### [2026-09-14T01:59:47.665Z] TOOL RESULT

```
=== leaf 206 ===
 sg. subj. (8212, $227.1) DNa 42. xindsdtiy subj. ($02, $97, 5110, $122) DB 1.52.
azinav- vb. ‘hear, satisfy’ ($96): cf. Av. zšnav- ‘Genüge haben an’, adj. zínav- ‘Genüge leistend’, ріс. zšnůta-, sb. zínütay- ‘Zufriedenstellung’ (Bthl. AiW 557-60); apparently an extension of root zinà- ‘learn’ (cf. pIE *40- and *doy- ‘give’), with semantic development ‘learn, hear of, hear’, and ‘hear, hearken to, satisfy’ (Lg. 15.171; ef. also Bv. TPS 1945.47-50). Hz. ApI 238-40 gives an impossible equation with Skt. éru- ‘hear’ (pIE
OLD PERSIAN
*flu-); Sen 247, 251, has wrong meanings. Р}.
sani, Acme 1.319-20, gives another etymology, -
See also uzsnav-.
z5nula- past pte. pass. ($71, 3242.1), cf. uzšnav-: zSnuta nsm. ‘satisfied’ DNb 26. |xsnutam) nsn. ‘heard’ DNb 53.
à + zínav-: dxSnautiy (§71, $122, $208) ‘satisfy’ DNb 24. āzšnavāhy 2d sg. subj. (§227.1) ‘satisfy’ DNb 29f. äzšnudiy 2d sg. ішу. ($208, §237.1) ‘hear’ DNb 54.
gaifa- sb. ‘(living) personal property, cattle’: Av. gaébü- ‘individual living being, pl. world; household, property’, РЫ. géhdn ‘world’ (from gen, pl.), to root pIE *g*ei- seen in OP jiv- (869, $101, $151). For varying interpretations, see Tm. Lex, 85, with lit. — ga26àm-cà (S89) asf. DB 1.65.
gaud- vb. ‘conceal’: Av. gaoz-, Skt. githati (§88). apa- + gaud- ‘conceal, hide away’: apagau- dayahy 2d sg. subj. (§227.1) DB 4.55, 51. apagaudaya 2d sg. inj. (5215,
=== leaf 207 ===
n, fall down’: [avagmat]a nsf. past pte. ($244) DSe 46f (conj. of Kent, cf. JAOS 54.46).
рата + gam- ‘go forth’: paragmata nsf. past pte. ($101, $103.IV, §122, 8132.2, §244) DNa 44f.
ham- + gam- ‘come together, assemble’: ha"- gmaté npm. past pte. ($101, $1081У, $1322, $140.V, $244) DB 2.32, 38, 43, 52, 58; 3.65. See also Надтаійла-.
gay- vb., see Jiv-. gara- ‘devouring’, see bdtugara-.
garta- sb., either ‘cave’ or ‘wagon’, see Asa- garla-.
Garmapada- adj. ‘Garmapada’, the fourth month, June-July: Elam. kormabadas, АКК. du-
183
'"üzu. From garma- ‘heat’, Av. garama-, Skt. gharmá-, Lt. formus ‘hot’, NEng. warm, pIE *gthormo-, cf. Gk. bepuos (with analogical -e-), + pada- ‘step, station’ ($29, §31, $149.1, $161.Ib, $165): ‘Heat-Station Month’. — Garmapadahya gsm, DB 1.42; 3.71, 46.
gav- sb. ‘cow, cattle’ ($101): Av. gau£, Skt. gaus, Gk. fois, NEng. cow, pIE nom. *g*dus: in Gaubaruva-, Gaumäla-, perhaps in Gatagu-.
gasta- adj. ‘repugnant, evil’; пі, as sb., ‘evil, harm’: past pte. ($85, $242.I) of vb. *gant- *gandh- ‘smell’, Av. ganti- ‘evil odor’ (AIW 493), duZ-gantt- ‘evil-smelling’ (AiW 757), Skt. gandhá- ‘odor’ (Bv. Gr. $179); for meaning, ef. Lt. odor ‘smell’, бй ‘(I have smelled), I hate’, odium ‘dislike, hatred’. Not abstract to same root, *gant-tdi-, nom. gasta', abl. shortened by haplology, as taken by Hz. AMI 8.68, ApL 173-7. gastá nsf. DNa 57f. дазій
=== leaf 208 ===
3f, 57; XPa 20; XPc 14; XPf 48, alva}m-c* ($521) DB 5.9. Ка&-сїу nsm. DB 149, 53; DSe 37. @& ciy asn. DB 1.58. paruvam-ciy DB 1.63, 67, 69. yaciy (q.v.) DNb 35, 36, 57. haw-cty DPe 23f. hakaram-ciy DNb 34f. [haca-cily DSf 23: vakna-|cily XPg 7f, less likely than vaknalptly, see under apiy. |
Citcizri- sb. ‘Cincikhri’, father of Martiya (§163.V): Elam. st-in-sa-ak-ri-1§, Akk. #-in-Sa- ah-ri-i& Cicizrais gsm. (§179.1V) DB 2.9.
сій adv. ‘so long’, correlative with уйій ‘un- til’: from ci- + suffix seen in Gk. ёте-та ‘then’ (8191.11; wrongly König, RuID 72, and Sen 40). DB 248, 63.
cica- sb. ‘seed, lineage’: Av. &6ra-, NPers. &hr ‘origin’ ($78, $148.IIT). In Ariyaciqa-, Ciça- іахта-.
Ciga"lazma- sb. ‘Cicantakhma’, а Sagartian
OLD PERSIAN
rebel: Elam. şi-iš-ša-an-tak-ma, Akk. -it-ra-an. — | lah-ma, Gk. Tpravraixuns. From ciga-(§9.n1) + | lazma- ‘brave’ ($9.11): ‘Brave-by-Lineage’ (§160,- Ie); the -zm- is Median ($163.II; Jacobsohn, KZ 54.261; Bv. BSLP 31.2.79). For the nasal end-
ing the prior element, see $159.n1. Cicatazma
пет. DB 2.79; 4.20; DBg 1f. Ciçatarmam asm, DB 2.871. Cicalaxmà ism. DB 2.86.
сіла] emphasizing adv. after neg., ‘at all’: , :
Av. cină ‘also, likewise’; perhaps isn. of ci-, cf.. 4 JAOS 58.116-7, 324, and Harl, KZ 63.2 (not ! eità], with Sen 134). DSe 36.
ciyăkara- (§53) adj. ‘how great’; nt. аз sb., ‘how great a thing’: *ciya(n)t-, cf. Skt. kiyat nsn. ‘how
```


## [2026-09-14T01:59:53.607Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN 154\"; grep -n \"^ *154\\.\\|  154\\. \" HRN.txt | head; echo \"=== sāja\"; grep -n \"säja\\|sâja\\|saja \" HRN.txt | head -20"
}
```


### [2026-09-14T01:59:53.684Z] TOOL RESULT

```
=== HRN 154
1746:154. bädefräh 'Vergeltung, Strafe'.
10844:154. pahlutn Vortreflflich, ausgezeichnet', pahlumih bozw.
11699:154.
=== sāja
```


## [2026-09-14T01:59:56.601Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==175' HRN.txt | head -c 2000"
}
```


### [2026-09-14T01:59:57.661Z] TOOL RESULT

```
— 153 —
bei. LW. sazag (237). Np. nüxte, säz sind vielfach
entlehnt, vergl. auch np. sä^t lieitzeug in arm. sa/teal
gesattelt*, ansa/t *ungesattelt' (Noldeke bei Hübsch -
mann, ZDMG. 35, 132 No. 37).
np. sd/ten ist eine Causativbildung zum Stamme sac-
(np. seztden).
689. {i)8är ^Schmerz, Leid*.
aw. sddra- 'Wehe, Leid*.
690. (2)-ÄÄr 'Kopf in nigün]sar^ sebuk]sar etc.
aw. sära-, särah- *Kopf*; phlv. vergl. sar[var 'Helm\
Vergl. No. 726.
691. 8äl 'Jahr*.
aw. sare^a- 'Jahr*; phlv. sal, sälak *alt\ arm. LW.
nava]8ard, graecisirt (nicht lydisch, vergl. G. Meyer,
Indog. Forsch. I, 326) i'for adodiv (Job. Lydus), chald.
LW. "»TlDli (de Lagarde, Öemitica I, 65), ;K''ärezm.
nau^arjT (Nöldeke, Pers. Stud. I, 34); skr. gardd-
'Herbst, Jahr (mit Zahlen)'.
oss. d. särdä, t. särd 'Sommer* (223).
Allg. entlehnt: kurd. af/. bei. (235) säl; wa/. sdl,
sar. säL
692. sälär 'Anführer'.
aw. *särö,dära' ; phlv. sälar, \idQa(jTaöa()av\öaXdvrji^
(Procop. Pers. I, 7, 11 u. ö.), arm. LW. s(dar, spajsalar,
np. serdär (phlv. sardär) ist eine junge Bildung, da
man sonst seryär erwarten müsste.
Vergl. No. 726.
693. sämän 'Ordnung, Grenze; Hausgerät etc.'.
phlv. sämän, bezw. sahmän (z. B. AV. 'boundary-
mark'), arm. LW. sahman o()ocj oQ^o/ndc^ -nQoacayua (de
Lagarde, No. 1934).
Zu ai. [/'gad' etc. (Fr. Müller, WZKM. 5, 262).
(\)8än 'Wetzstein.
Siehe efsan (No. 98) 0.
*) Nachträglich sei hier noch np. sumhäde (goschr. sunb"), Käs.
K. sunbötä, arab. LW. sunbäSaj^ sunhäSat (Bibl.' geogr. arab. IV, 277)
'"Wetzstein* erwähnt
■}\*m^t!/*m.^i
```


## [2026-09-14T02:00:00.911Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==176' HRN.txt | head -c 2500"
}
```


### [2026-09-14T02:00:01.849Z] TOOL RESULT

```
— 154 -
694. (2)säii 'Teil, Stück; Art und Weise'; -$an gleich,
ähnlich, -sä.
Die Deutung von aw. sü^ia- (yt. 19, 44) als *Stück'
(Studien, I, 148) hat Geldner BB. XV, 254 wider-
rufon.
LW. kuid. säriy z. B. kH\sän *öü; wie?', va]suna auf
diese Weise'; afy. San; bei. sang (236).
Np. -sä^) hat das auslautende n verloren, wie äsuid,
a (No. 52), senrjso (Käs. Z. zu 1. süh) u. a. ni. Gehört
np. 'äsan 'äsä gleich, ähnlich* auch hierher?
695. säf/e 'Schatten, Schutz'.
ai. chayd' 'Schatten'; plilv. sayak,
kurd. se^ si\ bei. säig, n. saJ (340); wa;^. LW. sayd,
sar. suyä,
696. supär Tflug .
ai. phdla- Tflugscliar*, zu l^phal-, splial- *aufreissen'.
sar. spur 'Pflug .
697. Hiipävden anvertrauen, übergeben*, jüd.-pers. p1N?10,
supiirden, sipäris (sifärls).
g. vaspartmün.
aw. tis-\- 2. l/'par-; phlv. avspärtan, avspurtan. (vd. 5
(77)), spiirtltan (AV.); ai. iid -{- "lA^par- 'hinüber-
führen', utpdrana- 'Übersetzen*; vergl. lat. portäre.
af/. späral übergeben'; kurd. sipärtin.
Die Etymologie stammt von de Lagarde, ist aber
sehr unsicher. Bei siperl (No. 703) passt die An-
knüpfung an l^par- ausfüllen* besser.
698. »Ipäs 'Dank*.
phlv. späs, späsdär; arm. spas-em aufwarten, dienen',
spas 'Dienst'.
^) Np. sä *Tribut* ist dagegen au8 *sävaka- entstanden, vergl. die
Form säv (Nöldeko, Pers. Stud. II, 20 Anm. 4). In der Bedeutung
'kostbare Art Stoff* (Vis und Rämln 52 Vers 7 v. u.) wird es ebenfalls
hierher gehören.
```


## [2026-09-14T02:00:06.884Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"sy'k\\|sy\\`k\\|sy’k\\|s'yk\\|sāyā\\|shade\\|shadow\" SOD_pages.txt | head -20"
}
```


### [2026-09-14T02:00:07.925Z] TOOL RESULT

```
5892:743 ^sy'k- B                        oj^j^tjxyr                                                                                   o*u
10931:                                                                                pasik ©<Parth. by?h ^p'sy'k
15504:                                                                4140 ynsy'kh S                              ^/^J<fl£*i-I
15533:                                                                4145 ynsy'kh    B                                    4*&>
15534:       xansyak     ^yrsy'k                                               4157 ynt'q qry C                            juli <jl$*jb
15896: 4266 yrsy'k B                                   j^f '<j±f         self, body, soul
15897:      xarsyak -^ynsy'kh
17445:     Gersh. TPS 1945, 147                                    4825 kr'ysy'kh M                      LJT 4, «^lj ^.LJT
21452:6162 nws'ykh     B                         <s^l < jfcjk- <,^l
22437:6515 p'sy'k M.                           sJcaToj^.
22442:6516 p'syk => p'sy'k                                                    211; Frag. Len. 98a2
28424:                                                if 11 'iJtJ?         8582 rwpsy'kh S
29973:   - fun                                                          sayak (sy'k, sy*q) ®<*syaka-, A v. asaya\ Skt.
29976:                                                                   shadow,  ©ob. -y; pi. -t(h)
30227:9180 s'ykn S                                    oL^j^x^J           VJ gloss, p 119
30232:9181 s'ykn'yk B                                J>& <*&*       9192 -sc B, S                                jT jl^i j|
32258:      (<?/)wind, windy                                        9897 w'xs'yk' S, M
39369:  3862                                 serious    4180                          shadow  9104
```


## [2026-09-14T02:00:10.925Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '29960,29990p' SOD_pages.txt; echo \"=== find page tag\"; awk 'NR>=29900 && NR<=29990 && /pdf page/' SOD_pages.txt; awk 'NR<=29975 && /\\[pdf page/' SOD_pages.txt | tail -3"
}
```


### [2026-09-14T02:00:12.033Z] TOOL RESULT

```
         <?2, 65V 5, 8, 68V5; f. pp. swxsc\ BSTii 909.17:
         C2, 61R17; Sund. AoFviii 1981, 22R4                 9102 sy-1        (u>> ^r,tu: jj)j*^ y>\te 4oJ+\JaJ4> <o>b jUj
                                                                    say/si ©trans. & intrans. v. =^syt-, sy't-, z>ryy
9089 sxnd- M                              o>J*j*-+
     sxand (sxnt-) ©Parth. 'sxnd-                                     sy-, }sy-\(to)appear,
                                                                    (fo)show,     }sy-2     (r^)show oneself
     (ro)make fun of                                                GMS 494, 550; TSP p271; VJ pi 19; BSTBL pl46;
     BBB p84.716; BSTi 90, 299; S W, BSOAS 1983,                      MDii 21 1; SCE 80, 332; C2 p226; AVS 82
       42

9090 sxndy M                               .>^«^>s.          9103 sy-1 ^ >sy-3
                                                             9104 sywk(h) B                                jL-U^U
     sxande ©pi. -tt =»SY}ntcyk, k*tSY}ntyt }SY}nt
   - fun                                                          sayak (sy'k, sy*q) ®<*syaka-, A v. asaya\ Skt.
       Gersh. Sogd. Cpds. 1945, 145                                  chaya% Yaghn. siyoka-, Khwar. sy*k\ Pahl.
                                                                     sayag canopy
                                                                   shadow,  ©ob. -y; pi. -t(h)
9091 sxnt-     C ^ sxnd-
9092 sxnw =» swxn(w)                                               VJ pi 19; TSP 2.1005, 6.124, 7.10; BSTBL, Dhy.
9093 sxth     S(AL) -» syt-(h)                                       260; ob. -y, SCE 530; TSP 7.10; Tales. 483.23;
                                                                     pi. -t(hh STi 31.13; Dhy. 219; GMS 124, 979;
9094 sxw'y- M, C                      frfj&t^j*                      STii 8.4
     (o)sxway (sxwy-, 'sxw'y) ©<*us-xwahaya
       ©impf. syxwyy =^sxwst-, swx*y-, SYw*y-                9105 sy>k B, M -» sy»k(h)
     0<?)take up, (to)lift                                   9106 sy'q C => sy»k(h)
     GMS 417; GMS 627; C2 glossy MSP b36, 116;
                                                             9107 sy'mnty C                                      >1*«uUj
        3sg. pres. sxw'yu Sund. AI 28, 1988, 184; AVS             sayamande
        95                                                        mark, sign =*z*ry sy'mnty

9095 sxwn- S, M                                                    STi 31.11; GMS 550n 2
=== find page tag
```


## [2026-09-14T02:00:17.861Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"pdf page\" SOD_pages.txt | head -3; awk 'NR<=29975' SOD_pages.txt | grep -n \"pdf page\" | tail -3"
}
```


### [2026-09-14T02:00:19.014Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T02:00:22.784Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} {n++} END{print \"leaves:\",n}' SOD_pages.txt; python3 - <<'EOF'\np='/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt'\nt=open(p,encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nidx=sum(len(l)+1 for l in lines[:29970])\nprint('leaf index of line 29970 =', t[:idx].count('\\f'))\nEOF"
}
```


### [2026-09-14T02:00:23.930Z] TOOL RESULT

```
leaves: 644
leaf index of line 29970 = 434
```


## [2026-09-14T02:00:38.842Z] TOOL CALL #33: Bash

```json
{
 "command": "sed -n '1,40p' tools/fetch_source.py; echo \"=== ref_page\"; sed -n '1,40p' tools/ref_page.py"
}
```


### [2026-09-14T02:00:38.901Z] TOOL RESULT

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
=== ref_page
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
```


## [2026-09-14T02:00:45.808Z] TOOL CALL #34: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%DA%86%D9%87%D8%B1%D9%87\" \\\n \"https://en.wiktionary.org/wiki/%D8%B3%D8%A7%DB%8C%D9%87\" \\\n \"https://en.wiktionary.org/wiki/%D8%B4%DA%A9%DB%8C%D8%A8\" \\\n \"https://en.wiktionary.org/wiki/%D8%B4%D9%88%D8%AE\" \\\n \"https://en.wiktionary.org/wiki/%D9%85%D9%86%D9%88%DA%86%D9%87%D8%B1\" \\\n ; do echo \"### $u\"; python3 tools/fetch_source.py \"$u\" --note \"page 451 Skai/Skaivos verification\" 2>&1 | tail -2; done"
}
```


## [2026-09-14T02:00:48.237Z] TOOL CALL #35: Bash

```json
{
 "command": "for u in \\\n \"https://www.etymonline.com/word/scene\" \\\n \"https://www.etymonline.com/word/scenario\" \\\n \"https://www.etymonline.com/word/shine\" \\\n \"https://en.wiktionary.org/wiki/%CF%83%CE%BA%CE%B7%CE%BD%CE%AE\" \\\n \"https://en.wiktionary.org/wiki/scaevus\" \\\n ; do echo \"### $u\"; python3 tools/fetch_source.py \"$u\" --note \"page 451 Skai/Skaivos verification\" 2>&1 | tail -2; done"
}
```


### [2026-09-14T02:00:49.846Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/%DA%86%D9%87%D8%B1%D9%87
/home/sfmqrb/git/rishe/data/verification/sources/web/deff477016be655e.txt
### https://en.wiktionary.org/wiki/%D8%B3%D8%A7%DB%8C%D9%87
/home/sfmqrb/git/rishe/data/verification/sources/web/dd9a784112c954d4.txt
### https://en.wiktionary.org/wiki/%D8%B4%DA%A9%DB%8C%D8%A8
/home/sfmqrb/git/rishe/data/verification/sources/web/f3c283c80e058002.txt
### https://en.wiktionary.org/wiki/%D8%B4%D9%88%D8%AE
/home/sfmqrb/git/rishe/data/verification/sources/web/a2cd66389cabd6f3.txt
### https://en.wiktionary.org/wiki/%D9%85%D9%86%D9%88%DA%86%D9%87%D8%B1
/home/sfmqrb/git/rishe/data/verification/sources/web/857503e14c7dc05f.txt
```


### [2026-09-14T02:00:53.764Z] TOOL RESULT

```
### https://www.etymonline.com/word/scene
/home/sfmqrb/git/rishe/data/verification/sources/web/bd2729d0ce832973.txt
### https://www.etymonline.com/word/scenario
/home/sfmqrb/git/rishe/data/verification/sources/web/8f7012a03136ce62.txt
### https://www.etymonline.com/word/shine
/home/sfmqrb/git/rishe/data/verification/sources/web/aef4d75fc281c662.txt
### https://en.wiktionary.org/wiki/%CF%83%CE%BA%CE%B7%CE%BD%CE%AE
/home/sfmqrb/git/rishe/data/verification/sources/web/e2e6514385ae01ef.txt
### https://en.wiktionary.org/wiki/scaevus
/home/sfmqrb/git/rishe/data/verification/sources/web/45e793d08b03435f.txt
```


## [2026-09-14T02:00:56.043Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in deff477016be655e dd9a784112c954d4; do echo \"######## $f\"; grep -n -A12 \"Etymology\" $f.txt | head -60; done"
}
```


### [2026-09-14T02:00:57.227Z] TOOL RESULT

```
######## deff477016be655e
62: Etymology 
63-
64- 1.2 
65- Noun 
66-
67- 1.2.1 
68- Descendants 
69-
70- 2 
71- Persian 
72-
73- Toggle Persian subsection 
74-
--
76: Etymology 
77-
78- 2.2 
79- Pronunciation 
80-
81- 2.3 
82- Noun 
83-
84- 2.3.1 
85- Descendants 
86-
87- 2.4 
88- References 
--
166: Etymology
167- [ edit ] 
168-
169- Borrowed from Classical Persian چهره ( čihra ) 
170-
171- Noun
172- [ edit ] 
173-
174- چهره • ( čhrh / čihrä, čehrä /) ( plural چهره‌ها ( /⁠čihrä-hā, čehrä-hā⁠/ ) ) 
175-
176- face , visage 
177- Synonyms: یوز ( ywz /⁠yüz⁠/ ) , پیکر ( pykr /⁠päykär⁠/ ) , جبین ( jbyn /⁠jäbīn⁠/ ) , روی ( rwy /⁠rūy⁠/ ) , چیرای ( čyrʾy /⁠čıray⁠/ ) 
178- 1484 , Ali-Shir Nava'i , فرهاد و شیرین [ Farhad and Shirin ], page 260b , line 29 : قیو صورت که مانی قیلدی تمثال
--
195: Etymology
196- [ edit ] 
197-
198- Inherited from Middle Persian 𐭰𐭧𐭫𐭪𐭩 ( čihrag ) , from Old Persian *čiθrakah , from Proto-Iranian *čiθrákah , from Proto-Indo-Iranian *čitrám , from Proto-Indo-European *kʷi-tróm , from *kʷey- ( “ bright, burning ” ) . [ 1 ] Cognate with Sanskrit चित्र ( citra ) and Baluchi چِهرَگ ( čihrag , “ countenance, face ” ) 
199-
200- Pronunciation
201- [ edit ] 
202-
203- ( Classical Persian ) IPA ( key ) : /t͡ʃih.ˈra/ 
204-
205- ( Dari, formal ) IPA ( key ) : [t͡ʃʰe̞ɦ.ɾä] 
206-
207- ( Dari, formal ) IPA ( key ) : [t͡ʃʰe̞ɦ.ɾä] 
######## dd9a784112c954d4
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
73- 1.3.2 
74- Descendants 
--
156: Etymology
157- [ edit ] 
158-
159- From Middle Persian [Book Pahlavi needed] ( sʾdk' ) , 𐫘𐫀𐫏𐫃 ( sʾyg /⁠sāyag⁠/ ) , from Old Persian *θāyakā , from Proto-Iranian *caHyā́kaH .
160-
161- Pronunciation
162- [ edit ] 
163-
164- ( Classical Persian ) IPA ( key ) : /saː.ˈja/ 
165-
166- ( Dari, formal ) IPA ( key ) : [sɑː.jä] 
167-
168- ( Dari, formal ) IPA ( key ) : [sɑː.jä]
```


## [2026-09-14T02:01:16.501Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in f3c283c80e058002 a2cd66389cabd6f3 857503e14c7dc05f; do echo \"######## $f\"; sed -n '100,260p' $f.txt | grep -n -B2 -A10 \"Etymology$\" | head -70; done"
}
```


### [2026-09-14T02:01:17.596Z] TOOL RESULT

```
######## f3c283c80e058002
######## a2cd66389cabd6f3
53- [ edit ] 
54-
55: Etymology
56- [ edit ] 
57-
58- (This etymology is missing or incomplete. Please add to it, or discuss it at the Etymology scriptorium .) 
59-
60- Pronunciation
61- [ edit ] 
62-
63- ( Classical Persian ) IPA ( key ) : /ˈʃoːx/ 
64-
65- ( Dari, formal ) IPA ( key ) : [ʃoːx] 
######## 857503e14c7dc05f
42- [ edit ] 
43-
44: Etymology
45- [ edit ] 
46-
47- From Avestan 𐬨𐬀𐬥𐬎𐬱𐬗𐬌𐬚𐬭𐬀 ( manušciθra ) . Akin to Old Armenian Մանաճիհր ( Manačihr ) , an Iranian borrowing.
48-
49- Pronunciation
50- [ edit ] 
51-
52- ( Classical Persian ) IPA ( key ) : /ma.nuː.ˈt͡ʃihr/ 
53-
54- ( Dari, formal ) IPA ( key ) : [mä.nuː.t͡ʃʰe̞ɦɾ]
```


## [2026-09-14T02:01:21.623Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && wc -l f3c283c80e058002.txt && sed -n '1,200p' f3c283c80e058002.txt | tail -120"
}
```


### [2026-09-14T02:01:21.682Z] TOOL RESULT

```
255 f3c283c80e058002.txt

 فارسی 
 Kurdî 
 Malagasy 

 Entry 

 Discussion 

 English 

 Read 

 Edit 

 View history 

 Tools 

 Tools

 move to sidebar 
 hide 

 Actions

 Read 

 Edit 

 View history 

 General

 What links here 
 Related changes 
 Upload file 
 Permanent link 
 Page information 
 Cite this page 
 Get shortened URL 

 Print/export

 Create a book 
 Download as PDF 
 Printable version 

 In other projects

 Appearance

 move to sidebar 
 hide 

 From Wiktionary, the free dictionary

 See also: شكيت 

 Persian
 [ edit ] 

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ʃa.ˈkeːb/ , /ʃi.ˈkeːb/ 

 ( Dari, formal ) IPA ( key ) : [ʃä.kʰéːb] , [ʃɪ.kʰéːb] 

 ( Dari, formal ) IPA ( key ) : [ʃä.kʰéːb] , [ʃɪ.kʰéːb] 
 ( Kabuli ) IPA ( key ) : [ʃä.kʰéːb] , [ʃɪ.kʰéːb] 

 ( Hazaragi ) IPA ( key ) : [ʃä.kʰéːb̥] , [ʃi.kʰéːb̥] 

 ( Iran, formal ) IPA ( key ) : [ʃæ.kʰʲíːb̥] , [ʃe.kʰʲíːb̥] 

 ( Tajik, formal ) IPA ( key ) : [ʃä.kʰéb] , [ʃi.kʰéb] 

 Rhymes: -eːb 

 Readings

 Classical reading ? 

 šakēb, šikēb

 Dari reading ? 

 šakēb, šikēb

 Iranian reading ? 

 šakib, šekib

 Tajik reading ? 

 šakeb, šikeb

 Verb
 [ edit ] 

 شکیب • ( šakēb or šikēb ) 

 present stem form of شکیفتن ( šikēftan ) 

 Noun
 [ edit ] 

 شکیب • ( šakēb or šikēb ) 

 patience 
 Synonyms: صبر ( sabr ) , تحمل ( tahammul ) , شکیبایی ( šikēbāyī ) 
 c. 1520 , Selim I of the Ottoman Empire , edited by Benedek Péri, The Persian Dīvān of Yavuz Sulṭān Selīm , Budapest, Hungary: Research Centre for the Humanities, Eötvös Loránd Research Network, →ISBN , page 78 : برداشته بظلم فراقت ز جان شکیب 
وصل تو کرده بر سر جانها نثار عدل bardāšta ba-zulm-i firāqat zi jān šakēb 
wasl-i tu karda bar sar-i jānhā nisār adl You have removed patience from the soul by the tyranny of parting from you;
Reunion with you strews justice upon the head of [your lovers'] souls. (Classical Persian transliteration) 

 Descendants
 [ edit ]
```


## [2026-09-14T02:01:29.041Z] TOOL CALL #39: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%D8%B4%DA%A9%DB%8C%D9%81%D8%AA%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D9%87%DA%98%DB%8C%D8%B1\" \\\n \"https://en.wiktionary.org/wiki/%D8%AE%D8%AC%DB%8C%D8%B1\" \\\n \"https://en.wiktionary.org/wiki/%CF%83%CE%BA%CE%B1%CE%B9%CF%8C%CF%82\" \\\n ; do echo \"### $u\"; python3 tools/fetch_source.py \"$u\" --note \"page 451 Skaif/Skai verification\" 2>&1 | tail -1; done"
}
```


## [2026-09-14T02:01:31.437Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== CHEUNG skaif/kaif\"; grep -n -i \"skaif\\|\\*kaif\\|skaib\\|škēb\\|shakib\\|sakeb\\|kEb\" CHEUNG.txt | head -20; echo \"=== CHEUNG shadow\"; grep -n -i \"sāya\\|saya-\" CHEUNG.txt | head -5"
}
```


### [2026-09-14T02:01:32.875Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/%D8%B4%DA%A9%DB%8C%D9%81%D8%AA%D9%86
/home/sfmqrb/git/rishe/data/verification/sources/web/94a2bfb38c3bc7c9.txt
### https://en.wiktionary.org/wiki/%D9%87%DA%98%DB%8C%D8%B1
/home/sfmqrb/git/rishe/data/verification/sources/web/cc972195b129aed2.txt
### https://en.wiktionary.org/wiki/%D8%AE%D8%AC%DB%8C%D8%B1
/home/sfmqrb/git/rishe/data/verification/sources/web/410aa7ae29fdb71d.txt
### https://en.wiktionary.org/wiki/%CF%83%CE%BA%CE%B1%CE%B9%CF%8C%CF%82
/home/sfmqrb/git/rishe/data/verification/sources/web/8403d216eac4f87c.txt
```


### [2026-09-14T02:01:32.995Z] TOOL RESULT

```
=== CHEUNG skaif/kaif
=== CHEUNG shadow
```


## [2026-09-14T02:01:36.069Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls -la CHEUNG.txt && head -c 400 CHEUNG.txt; echo; echo \"=== grep kaip\"; grep -n -i \"kaip\\|xšnav\\|šikēftan\\|sikeftan\" CHEUNG.txt | head"
}
```


### [2026-09-14T02:01:36.161Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 1769485 Sep  4 14:06 CHEUNG.txt
Etymological 
Dictionary 


of the Iranian Verb 


Johnny Cheung 


Etymological Dictionary of the Iranian Verb 


Leiden Indo-European 
Etymological Dictionary Series 


Edited by 
Alexander Lubotsky 


VOLUME 2 


Etymological Dictionary 
of the 


Iranian Verb 


By 


ohnny Cheun 
y g 


LEIDEN : BOSTON 
2007 


This publication has been made possible by the financial support of the 
Netherlan
=== grep kaip
55468:*CiaH', *xšnav (s.v.)
```


## [2026-09-14T02:01:37.429Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 94a2bfb38c3bc7c9 cc972195b129aed2 410aa7ae29fdb71d 8403d216eac4f87c; do echo \"######## $f\"; grep -n -A8 \"^ Etymology$\" $f.txt | head -40; done"
}
```


### [2026-09-14T02:01:38.554Z] TOOL RESULT

```
######## 94a2bfb38c3bc7c9
######## cc972195b129aed2
140: Etymology
141- [ edit ] 
142-
143- From Parthian 𐫍𐫇𐫝𐫏𐫍𐫡 ( hwcyhr /⁠hužihr⁠⁠/ ) . Doublet of خجیر ( xujīr  / xojir ) .
144-
145- Pronunciation
146- [ edit ] 
147-
148- ( Classical Persian ) IPA ( key ) : /hu.ˈʒiːr/ 
######## 410aa7ae29fdb71d
155: Etymology
156- [ edit ] 
157-
158- Inherited from Proto-Iranian *Hhučiθráh (composed of *Hhu- ( “ good ” ) and *čiθráh ( “ appearance, likeness; face ” ) ), from Proto-Indo-Iranian *Hsučitrás .
159-
160- Pronunciation
161- [ edit ] 
162-
163- ( Classical Persian ) IPA ( key ) : /xu.ˈd͡ʒiːr/ 
--
213: Etymology
214- [ edit ] 
215-
216- From Classical Persian خُجیر ( xujīr , “ beautiful; pleasant, agreeable ” ) . 
217-
218- Pronunciation
219- [ edit ] 
220-
221- ( Standard Urdu ) IPA ( key ) : /xə.d͡ʒiːɾ/ , /xʊ.d͡ʒiːɾ/ 
######## 8403d216eac4f87c
165: Etymology
166- [ edit ] 
167-
168- From earlier *σκαιϝός ( *skaiwós ) . Formally and semantically identical to Latin scaevus ( “ left ” ) , both from Proto-Indo-European *skeh₂iwos .
169-
170- Pronunciation
171- [ edit ] 
172-
173- IPA ( key ) : /skai̯.ós/ → /scɛˈos/ → /sceˈos/ 
--
435: Etymology
436- [ edit ] 
437-
438- From Ancient Greek , ultimately from Proto-Indo-European *skeh₂iwo- . Cognate with Latin scaevus .
439-
440- Adjective
441- [ edit ] 
442-
443- σκαιός • ( skaiós )  m ( feminine σκαιά or σκαιή , neuter σκαιό )
```


## [2026-09-14T02:01:49.231Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"kaif\\|kaib\\|kēb\\|keb\\b\" CHEUNG.txt | head -20; echo \"=== index of roots starting sk\"; grep -n \"^\\*sk\\|^ \\*sk\" CHEUNG.txt | head -30"
}
```


### [2026-09-14T02:01:49.313Z] TOOL RESULT

```
=== index of roots starting sk
15701:*skob"- ‘to pick clean, get rid of leaves; to split, shave’). These stages appear to be 
22506:*skamb ‘to support, use as support’ 
22547:*skap/f ‘to split, make a crack, crack’ 
22567:*skar 345 
22594:*skar ‘to pursue, drive, look for (the cattle)’ 
22650:*skard ‘to pierce (through)’ 
22681:*skarf ‘to stumble’ 
22686:*skauH 347 
22712:*skauH ‘to poke, touch; to earmark, ? to cover’ 
33068:*skeid-, 327 
33070:*skek-, 325 
33071:*skem-, 371 
33072:*skend-, 37 
33074:*skep-, 345 
33075:*skerd"-, 346 
33079:*skeu(H;)-, 348 
33080:*skob'-, 235 
37706:*skav- (skü-/skv-), 347 
55907:*skap/f (S.v.), 
56165:*skauH 
56167:*skap/f 
56452:*skauH 
57084:*skar 
57098:*skap/f 
57365:*skard, *su(m)p/b! , *tard 
57379:*skauH 
57494:*skar 
58084:*skarf 
58269:*skamb
```


## [2026-09-14T02:01:49.984Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '120,230p' 94a2bfb38c3bc7c9.txt"
}
```


### [2026-09-14T02:01:50.065Z] TOOL RESULT

```
 Get shortened URL 

 Print/export

 Create a book 
 Download as PDF 
 Printable version 

 In other projects

 Appearance

 move to sidebar 
 hide 

 From Wiktionary, the free dictionary

 Persian
 [ edit ] 

 Alternative forms
 [ edit ] 

 شکیبیدن ( šakibidan ) 

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ʃi.keːf.ˈtan/ 

 ( Dari, formal ) IPA ( key ) : [ʃɪ.kʰeːf.t̪ʰán] 

 ( Dari, formal ) IPA ( key ) : [ʃɪ.kʰeːf.t̪ʰán] 
 ( Kabuli ) IPA ( key ) : [ʃɪ.kʰeːf.t̪ʰán] 

 ( Hazaragi ) IPA ( key ) : [ʃi.kʰeːf.t̪ʰán] 

 ( Iran, formal ) IPA ( key ) : [ʃe.kʰʲiːf.t̪ʰǽn] 

 ( Tajik, formal ) IPA ( key ) : [ʃi.kʰef.t̪ʰán] 

 Rhymes: -an 

 Readings

 Classical reading ? 

 šikēftan

 Dari reading ? 

 šikēftan

 Iranian reading ? 

 šekiftan

 Tajik reading ? 

 šikeftan

 Verb
 [ edit ] 

 Dari

 شکیفتن 

 Iranian Persian

 Tajik

 шикефтан 

 شکیفتن • ( šekiftan ) ( present stem شکیب ( šekib ) ) 

 to be patient , wait 
 c. 1260s , Jalāl ad-Dīn Mohammad Rūmī , translated by Reynold A. Nicholson , مثنوی معنوی [ Masnavi-ye-Ma'navi ], volume II, verse 76: خاک درگاهت دلم را میفریفت
خاک بر وی کاو ز خاکت می شکیفت xāk-i dargāh-at dil-am rā mē-farēft
xāk bar way k-ō za xāk-at mē- šikēft The dust of thy threshold was bewitching my heart:
dust (woe) on him that was patient without thy dust! 

 to tolerate 

 Conjugation
 [ edit ] 

 Conjugation of شکیفتن ( literary Iranian Persian )

 infinitive

 شکیفتن ( šakēftán ) 

 stem

 present

 شکیب ( šakēb ) 

 past

 شکیفت ( šakēft ) 

 participle

 present

 شکیبنده ( šakēbandé ) 

 past
```


## [2026-09-14T02:01:59.653Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD && grep -n \"pdf page\" FFD_pages.txt | head -5; echo \"=== search shakib\"; grep -n \"شکیب\\|شکیف\" FFD_pages.txt | head -20"
}
```


### [2026-09-14T02:01:59.756Z] TOOL RESULT

```
1:[pdf page 1]
24:[pdf page 2]
59:[pdf page 3]
70:[pdf page 4]
75:[pdf page 5]
=== search shakib
1726:شکیفت < ایرانی باستان ۴۶1۵1۲1۵. برای 18 - آراست. ‎٩1۸10‏ صورت اصلی ‎٩۳۵۲‏
1731:شکیب < فارسی میانه 51650 < ایرانی باستان 8-م۶۵1*. برای ۵ > آرای.
1767:شکیب آور از درد و بر من مشیب که از مهر بسیار بهتر شکیب
```


## [2026-09-14T02:02:02.534Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD && sed -n '1700,1790p' FFD_pages.txt; echo \"=== which pdf page\"; awk 'NR<=1731 && /\\[pdf page/' FFD_pages.txt | tail -2"
}
```


### [2026-09-14T02:02:03.633Z] TOOL RESULT

```
برای 18 -> آراست. 201 پیشوند فعلی است. ۰8130 صورت بالاندةٌ ريشهٌ ۰۶127 صورت
اصلی 131 است. 0 پیش از 1به ؟بدل شده است. ريشهٌ به معنی «فشار آوردن» است.
در فارسی میانه 55131127 به معنی «فشارآوردن» و «اشتافتن» است.
شتاب + فارسی میانه 053180» صورت کهنتر 2۳8130 + ایرانی باستان 201-8130-8*.
برای ۵ سه آرای.
شدن
شد < فارسی میانه 504 + ایرانی باستان 50-1۵*. برای 1۵ > آراست. 80 صورت
ضعیف ريشةٌ 5۵7و آن به معنی «رفتن» است.
[pdf page 68]
ماده‌های ماضی و مضارع فارسی دری سا ۳و۶
شو < فارسی میانه 32 + ایرانی باستان 32-۵*. برای 2 > آرای.
شست.
شست < فارسی میانه 5081 ج ایرانی باستان 3508-1۵*. برای 1۵ -> آراست. 7504
صورت اصلی 3۷8 است. 4 پیش از 1 به 5 بدل شده است. 7504 صورت ضعیف ريشةٌ
40 و آَن به معنی «تحریک کردن» است.
شوی < فارسی میانه 50 < ایرانی باستان 35200-8*. برای 2 آرای. «شور) به جای
اشوی» جدید است > جستن.
شکافت < فارسی میانه 531 < ایرانی باستان ۴2-31-1۵ برای 12 -> آراست. 2
پیشوند فعلی است. 831 صورت بالاندهٌ ریشهٌ قاا است و ۴۵۲ به معنی «شکافتن» است.
شکاف < فارسی میانه 5۶ + ایرانی باستان 2-3۶-۵*. برای 2 -> آرای.
شکست < فارسی میانه 5۵91 < ایرانی باستان ۹16۵۶-12*. برای 18 -> آراست. ‎٩1۵0‏
‏صورت اصلی ۶۵8 است. 4 پیش از ۲ به 8 بدل شده است. ۹24 صورت ضعیف ريشةٌ
4 است.برای‌ضعیف کردن ريشه #حذف شده‌است. 5۵74 به‌معنی «شکستن»است.
شکن < فارسی میانه 5۵7 < ایرانی باستان ۶1۸2-۵*. برای 2 -> آرای.
شکفت < فارسی میانه 5/1
شکف جشکوف ج فارسی میانه 501
شکیفت < ایرانی باستان ۴۶1۵1۲1۵. برای 18 - آراست. ‎٩1۸10‏ صورت اصلی ‎٩۳۵۲‏
[pdf page 69]
جوا را فعلهای فارسی دری
است. این ريشه به معنی «صبر کردنْ» است.

شکیب < فارسی میانه 51650 < ایرانی باستان 8-م۶۵1*. برای ۵ > آرای.

شمردن

شمرد + فارسی میانه 530076 < ایرانی باستان 1-37:۳4۵ط۵*. برای 18 -> آراست.
201 پیشوند فعلی است. ۳7337 صورت اصلی 55 است. ۵ بعد از آبه 5بدل شده است و
#به جای 27 در صورت ضعیف ريشه آمده است. ريشهٌ ۰1337 که صورت دیگرش 11۵7
است و از آن «آمار» آمده» به معنی «شمردن» است.

شمر, شمار < فارسی میانه 0570۱۶ 0337 < ایرانی باستان 1-57037-8ط۵*. برای 2
< آرای. 3۳37 صورت بالاندةٌ ريشةٌ ۸۸۲ است. 580۲ با حذف 4 از ۰5307۵
به‌قیاس با ۷8۵7 و ۷۷270 به‌وجود آمده است.

شناخت + فارسی میانه 5031. به جای 50371 باید 5034 می آمد» از 3۸3-18* ایرانی
باستان. ظاهراً به قیاس با فعلهایی چون ۹32و ‎٩381‏ بوده که 5371 به وجود آمده است.

شناس < فارسی میانه 5039 < ایرانی باستان 3503-6۵*. 58 برای ساختن ماد آغازی
به کار می‌رفته است. ريشهٌ 583*به معنی «شناختن» است.

شنودن :

شنود < فارسی میانه 25084 < ایرانی باستان ۴۹58-12 برای 1۵ > آراست. 7608
صورت ضعیف ريشهةٌ 7573۷ است» به معنی «شنودن».

«(شنید» و «شنفت» صورتهای دیگر «شتود» هستندء هر دو در فارسی دری به وجود
آمده‌اند.

شنو + فارسی میانه 252۷ ه ایرانی باستان 5۵۷-۵*. برای ۸ > آرای.
[pdf page 70]
ماده‌های ماضی و مضارع قارسی دری سس ۶۵
ی یف ۰
شیفت + ایرانی باستان 33۳۵-۲1۵*. برای 1۵ -> آراست. 0ه7537 صورت اصلی
آنه5۷* است. 0 پیش از 1 بدل به آ شده است. ريشهٌ 8۷۵10*به معنی «جنبیدن) است.
شیب < فارسی میانه 580 + ایرانی باستان 35۷/۵10-۵*. برای 2 > آرای.
«شیفته» صفت فاعلی گذشته از «شیفتن» است و در بیت زیر از گرشاسبنامةٌ اسدی
«(مشیب) به معنی («ناراحت مشو) به کار رفته است:
شکیب آور از درد و بر من مشیب که از مهر بسیار بهتر شکیب
فراموشیدن, فرموشیدن
فراموشید. فرموشید + فارسی میانه 1 ماد ماضی جعلی است. از ماده
مضارع ساخته شده است. در فارسی دری «فرامشت» بازماندة 11371۵31 فارسی میانه
است. 1۳30۵1 بازمانده 112-3-7108-1۵* ایرانی باستان است. برای 2 > آراست. 3و 5۵
هر دو پیشوند فعلی هستند. ريشةٌ کار" ظاهراً به معنی «فراموش‌کردن» است.
فراموش, فرموش < فارسی میانه 137۵5 < ایرانی باستان 172۵-3-۳۵5-۵*. برای 2
> آرای. 13۵05 صورت افزودةٌ ریشهٌ 05 است.
فرجامیدن
«فرجامید» مادهٌ ماضی جعلی است. از مادهٌ مضارع ساخته شده است.
فرجام + فارسی میانه 17[300 < ایرانی باستان 370-2[-17۵*. برای ۵ -> آرای. 370[/ظ
صورت بالاندهٌ ريشةٌ 8/[278 است. 8/1270 به معنی «حرکت کردن» است. صورت بالاندةٌ
آن با پیشوند فعلی ۵ به معنی «به پایان‌رساندن» است. در فارسی میانه ماد ماضی :
به صورت 178[31۲ آمده است» از ایرانی باستان 17[348*, با آمدن 31[ به‌جای
«آمدن) و «انجامیدن» هم از 8/۵7 آمده‌اند -> «آمدن) و «انجامیدن).
فرستادن
فرستاد + فارسی میانه 1۲68130 1138110 هر دو ماده ماضی جعلی هستند. از 11
[pdf page 71]
و فعلهای فارسی دری
ماده مضارع.
فرست س فارسی میانه 1۳681 ج ایرانی باستان - ها5زه ۳ *: فرستاده. قاقنه۲؟ صفت
[ مفعولی گذشته است از پیشوند فعلی 8 و هاگٌذ: صفت مفعولی گذشته از فا صورت
ضعیف ريشهٌ قَة: «روانه‌شدن ‏ وکردن» و برای پسوند 2 > آراست.
قرشته از 121512-1۵ آمده است.
=== which pdf page
[pdf page 68]
[pdf page 69]
```


## [2026-09-14T02:02:21.072Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"be patient\\|patience\" CHEUNG.txt | head -20; echo \"=== HRN shakib\"; grep -n -i \"sakeb\\|sikeb\\|sakîb\\|sakib\\|schakib\\|sikef\\|sakef\" HRN.txt HUB.txt | head -20"
}
```


### [2026-09-14T02:02:21.151Z] TOOL RESULT

```
29281:*SANSKRIT: Кѕат ‘to tolerate, be patient, gracious’ (RV+) > EWAia I: 426 
=== HRN shakib
```


## [2026-09-14T02:02:25.509Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD\"; grep -n -i \"škēb\\|skeb\\|škyb\\|skyb\\|šagēb\\|patience\\|patient\" PHD.txt | head -20; echo \"=== NYB\"; grep -n -i \"skyb\\|škēb\\|skeb\" NYB_vol2_glossary.txt | head -10"
}
```


### [2026-09-14T02:02:25.590Z] TOOL RESULT

```
=== PHD
212:anērān [?7°3?n'] non-Eran, the world beyond Eran. an-érang [?n’ylng] blameless. an-espās [’nsp’s] ungrateful. ~ih: ingratitude. 2 AY angubén [DW BS Y.A < A dbf ; ?ngpyn! | N angubin] honey. By? Wat), angür [AN BE < A ‘nb’; ?ngwl | N ~] grape. А AC k angust Pngwst! | (N angust)] finger, toe; unit of length (š in.). Va м ~arig [-lyk'] finger ring. „bān [-p’n'] finger-guard, -stall. anidan, ānay- [HY TYWN-tn! < А hyty, ^? th; ?nytn!] bring, lead. anig Payk! | (N pēšānī)] front, forehead. anī-z [AH RN(y)e, v. any | N niz] other also. anjir Pncyl | N ~] fig. anódag [nwtk! | M ?nwdg] strange, alien. ~ig [-yk'] foreign. ünóh, *ànóy [TME < A tmh | M ?nwh, ?wy] there. an-dst Pwwst'] infirm, unreliable. anos [nws] lit. immortal, i.e. the next life; elixir, antidote. — xwardan : risk death, fight to the death. anošag Pxwšk! | M ?nwsg, N ~a] immortal. «ii: immortality. ~-ruwan [-lwb’n'] the late, deceased. an-Ošmār [?7wsm’l] countless, innumerable. anó$-xwar [поў] mortal. *апбу, v. ānēh. anSahrig [nstr'yk'] slave. an-umméd P7wmyt! | J *nwmyd, N nauméd] hopeless, despairing. an-uspurrig [^r wspwlyk') imperfect. any [AH RN < A *hrn; (corruptly, 2К?у = *dn-i) | M ?n()] other. a-pattüg [ptwk!] impatient. a-paymān (?ptm?n!] immoderate. ~ih : immoderation. *apédag [ругА! | P?pyd(g)] lost, stray. ~dar [-d?/] custodian of stray animals. a-petitig žtytyk!] unrepentant, unconfessed. 7h : unrepentance. a-petyürag Pf(y)tyd'lk'] without misfortune, unassailed. a-pohisn Pwhšn'] incorruptible. appar [?5/ | М ’pr] robbery, theft. appar ['P?/] taken away, removed. ~ih : removal, loss, deprivation. apparag [25/6] robber. appurdan, appar- [YHNCLWN-tn' < A yhnslwn, V asi: >pl- | M эрит, *p(w)r-] steal. ~išn: stealing, theft. a-pursišnīg Ppwrsinyk'] irresponsible.
252:bāmdād [6’md’t' | М bmd?d, N ~] dawn, morning. bāmīģ [P myk!] brilliant, glorious. -bān [-??s! | M Aa, N ~] suffix, -keeper, -guard. band [bnd | = Р, N ~] bond, link. band-, v. bastan. bandag [bndk! | P bndg, N ~a] servant. bang [bng | N ~] henbane. bānūg [Pnwk! | N Бапи) lady. bar [b] | N ~] fruit, produce, profit. bar-, —išn, v. burdan. ībār [Pl | N ~] time, occasion. *bār [P1 | N ~] bank, shore. заг [D] | M P?r, N ~] fruit. ‘bar [b] | M br, N ~] load, burden; duty. bāraģ [5/А! | N ~a] mount, horse. barbut [blbwt! | N ~] lyre. bārestān [b/st?n'] patient, resigned. ~ih: patience, resignation. barig/k [b’lyk' | N bārīk (cf. tārīg)) thin, fine, subtle. bar-jamag [bly mk! | N ~a] saddle-bag. barómand [b wmnd | N ~] fruitful, prolific. barsom [blswm | M brswm] the bunch of twigs used in the Yasna cere- mony. baršnūm [b/s2wm] the major purification ritual. bastan, band- [ASLWN-tn! < A Vier bstn', bnd- | M bstn, (bn-), P bnd-, N ~] tie, bind. bāstān [b’st?n' | M PysPn, N ~] always, often. bas [YHWWNS | M P, N ~] be! (imperative of büdan, q.v.) baSkué [bskwe] gryphon. bašn [bén' | = P] top, peak; stature; mane (v. buš). baw-, —i$n, v. büdan. baxš-, —išn, v. baxtan. baxt [b()At! | N ~] fortune, fate. baxtan, baxš- [HLKWN-tn! < А У hig; bC)htn', bhf- | M bxt, bx$-, N baxsidan] apportion, distribute. ~išn: bestowal, distribution. bay [ORHY A < A */h; bk', bg | M by] god, lord. im ~: his Majesty. бу ~: his late Majesty. bayaspān [by’sp’n'] messenger, envoy.
292:*brinj [binc | (M bryng), N birinj] bronze, brass. ~én [-yx!] bronze, brazen. brinómand [blyn’wmnd] delimited. brištan, bréz- [blystn', blyc- | M bryz-, N biristan] roast. brüg [blwk' | M brwg, N abrü] (eye)brow. büdan, b(aw)- [YHWWN-tn! < A yhwwn, У hwh; bwtn', b- | M bwdn, bw-, N büdan] be, become. bawišn: becoming, genesis. büf [bwp | N <), *büg [bwk'] owl. buland [bwind | = M, N ~] high. būm [bwm | N ~] land, earth, country. ~-€andag [-cndk'] earthquake. Ibun [bwn' | = M, N ~] base, foundation, bottom. *bun [bwn! | N ~] = wan. bunag [bznk! | N ~a] baggage; abode, camp. — daštan: dwell, settle. bun-dahišn(īh) [bzundhšn!, -yh] primal creation. bunih [bwnyh] beginning. buništ [bwnyst! | = M] foundation. ~ag [-k'] principle. bun-kadaģ [bwnktk'] original house, home. bun-xān [bwnh?n'] source. bur-, —išn, v. buridan. burāģ [bzoP RU] cutting, sharp. burām-, v. bram-. burd [bwit! | M bwrd] patient. ~ih: patience. burdan, bar- [Y BLWN-tn! < А У ybl; bwltn', bl- | M Бата, br-, N <] carry, bear, take, endure. ~išn: bearing, behaviour. burdār [bwit!]] bearer; womb. ~ih: patience. burd-ešnēhr [bwit! fnwhl | P bwrdyfnwhr] grateful, thankful. burg [bwig | (Ar. burj)] tower. buridan, bur- [bwl-ytn! | M bwr-, N ~] = bridan. —j$n: cutting. Burz [bwic] the god of agriculture. Burzénmihr [bwlcynmtr!] the third major Fire of Sasanian Eran, that of husbandmen. burzidan, burz- [bwlc-ytn'] praise, honour. ~i$n: praise, honour. —iŠnié : praiseworthy. buš [ро | N ~] mane. būšāsp [bwPsp | M bwsy'sp, N ~] sleep, sloth; dream. * but [bwt! | = M, N ~] Buddha; idol. buz [AZ < A ‘z; Бос | N ~] goat.
545:pas-dānišnīh [4HLd’nsnyh] anti-knowledge. pasēmāl [psym’l, v. hamemal] defendant, accused. ~ih: (legal) defence. pasen [psyn! | N pasin] final, last. pasox [p’shw' | № ~] = passox. passand [psnd | N pasand] pleasure, liking. passandidan, passand- [psnd-ytn' | M psynd-, N pasandidan] like, approve. ~išn: liking, approval. ~isnig : likeable. passáxt [ps’ht'] test. passaxtan, passàz- [ps’hin', ps’c- | M ps?xt, ps’c-] fashion, prepare; insert; test. ~išn: preparation, constitution. passazag [psck! | M pscg] suitable, fitting. ~ih: suitability. passox [pshw! | M pswx, № pāsux) answer. past [pst' | N ~] low; astr. dejection. pašēmān [pšm?n! | = M, N ~] penitent, repentant. ~ih: penitence, repentance. pašm [psm | N ~] wool. ~ёп [-yn! | N ~in] woollen. pašn [psn'] bond, agreement. pāšnag [p’snk! | N ~a] heel. pāšom [p(”)$zvm) excellent. passing [pšng | N pišing] drop, exudation. paššinjag [pfnck! | N pišanja] drop. paššinjīdan, paššinj- [psnc-ytn' | N pišanjīdan) sprinkle. ~išn: sprinkling. pa&t(ag) [pšt(k)! | J pst] pact, bond, agreement. *pattān [pt’n'] noise, resonance. ~6mand [отта] resonant. pattāyistan [pi?dstn'] = pattüdan. pattüdan, pattày- [ptwtn', ptd- | P ptwdn, M pt’y-] stay, remain, last, endure. pattüg [ptwk'] enduring, patient, persevering. ^АҺһ: endurance, patience, perseverance. paxSag [phšk! | N pasa] mosquito, gnat. 1рау [pdy | N ~] foot; footstep, track. ~ 1: after. *pay [pdy | M pyy, N ~] sinew, tendon. pay [LGLE < А rglh; p'dy | M p'y, N —] foot, leg; foot (12 in.). 1,2 páy-, у, bL? pādan. payādaģ [pd’tk! | М py’dg, N piyada] on foot, foot-soldier, (chess) pawn. payag [p'd(y)k! | N paya] base, station. paydag [pyt?k! | M pyd'g, N payda] visible, obvious, revealed.
585:šimšār Lë"! | N ~] box tree. Sir [HLBA < A hlb’; $1 | M šyyr, N ~] milk. šīrēn [5/yn! | M syryn, N ~in] sweet. ~ih: sweetness. SiSag [$y$k! | N fifa) bottle, flask. škaft [Ар] = Skeft. škāftan, škāf- [sk’p-tn' | M ‘kk’ pt, N fikáftan] split, burst. Skarag [skik! | P *škr-] (bird) of prey. škarwīdan, škarw- [fklw-ytn' | M ‘fkrw-st, N fikarfidan] stumble, stagger. škastan, Sken(n)- [TBLWN-tn' < A N tbr; škstn!, škyn- | M ‘tkn-, N stkastan, fikan-] break. ^ i$n: breaking. škēbāģ [fkyp?k! | P kyb-, N #hëba] patient. ~ih: patience. Skeft [škypt! | P “#kyft, N šigift] hard; extraordinary, astonishing; very. ~ih: hardness; hardship, distress; astonishment. šken(n)-, ~išn, v. škastan. ških- [fkyh- | N šikth-] be broken. Skóf-, у. Skuftan. Skdfag [fRwpk! | N šukēfa] flower, blossom. Skoft [škwpt'] = škeft. 1$kóh [ол | M Ай] poor. --īh: poverty. *§k6h [kwh | N sukdh] dignity, majesty; fear. škuftan, &ЕбЇ- [škwp-tn! | N fukuftan] flower, blossom. Énàs-, v. Snaxtan. šnàsag [fn'sk! | P *$n*sg] knowing, knower; sense. ~ih: knowledge. šnāxtan, $nàs- [fm htn!, fie | M хіп, Чи s-, N fin-] know, recog- nize. šnāyēnīdan, šnāyēn- [sz dyn-ytn'] please, propitiate. ~išn: happiness. šnāyīdan, šnāy- [fr'd-ytn!] praise, propitiate. --i$n : praise, gratitude. šnāz [frc | (N šinā(w))] swimming. šnāzīdan, šnāz- [fr'c-ytn! | M $2? 2-, (IN šināw-)] swim. $nóhr [snwhl | М *fnwhr] gratitude, contentment. šnūmaģ [fnwmk! | M *fnwm-] satisfaction, contentment. &nó&ag [šnwšk! | N šunoša] sneeze. $nüg [šnwk' | M *fnwg] knee. šnūman [fnwmn! = Av. xsniimaine] propitiation. 86n [swn'] kind, manner. ~ig [-yk!] customary, ordinary. šūy-, v. Sustan. Sdy [std | N ~] husband.
2389:impatient apattüg.
3057:patience bārestānīb, burdīh, bur- dārīh, pattūgīh, škēbāgīh.
3058:patient bārestān, burd, škēbāg.
4540:salag! škaf- škāftan nibay-! nibastant ških- šken(n)- šken(n)išn škēbāgīh škēbāg škeftīh škeft 1*$kķēh &kohih škūf- škūfag škoft škuftan hur!, šakar škarw- škarwīdan škarag škastan škaft
=== NYB
```


## [2026-09-14T02:02:35.033Z] TOOL CALL #49: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:674 2>&1 | head -40"
}
```


### [2026-09-14T02:02:36.155Z] TOOL RESULT

```
no scan of BQT covers printed page 674 (see 'scans' in refs_online.json)
```


## [2026-09-14T02:02:36.815Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC leaf 588\"; awk 'BEGIN{RS=\"\\f\"} NR==588' IEC.txt | grep -n -i \"skaiw\\|skaios\\|scaevus\\|sux\\|šux\" ; echo \"--- raw head\"; awk 'BEGIN{RS=\"\\f\"} NR==588' IEC.txt | head -c 800"
}
```


### [2026-09-14T02:02:37.971Z] TOOL RESULT

```
=== IEC leaf 588
--- raw head
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
qu
```


## [2026-09-14T02:02:42.555Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 630 631 632; do echo \"=== leaf $n\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' IEC.txt | grep -n -i \"skaiw\\|skaio\\|scaev\\|sux\\|10[0-9][0-9]\\|11[0-9][0-9]\" | head -8; done"
}
```


### [2026-09-14T02:02:43.883Z] TOOL RESULT

```
=== leaf 630
2:1137
22:1138
=== leaf 631
5:1139
20:1140
=== leaf 632
4:1141
22:1142
```


## [2026-09-14T02:02:46.026Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==634' IEC.txt | head -c 3000"
}
```


### [2026-09-14T02:02:47.144Z] TOOL RESULT

```
, that, who") Skt. syah, f: sya beside sah, sa & tyah, tyā;
siāið (siasio) — siütós
10
20
25
30
35
40
45
1144
OPer. hya, hyā, rel.; Arm. cf. hi- in him ‘why’; hi-bar “how, as’; Tokh. B se ‘this’; Hiero-Hitt. syas, id.; Olr. sé, seo, so, m.; sí, f.; se, n. ‘he, she, it^; Ir. id.; cf. MIr. postpositive -so, -sa, id.; Br. hé- in hé-vlené ‘this year’; hé-ziu: W he-ddyw ‘today’; Br. hi ‘she; they’; W hi ‘she’; hwy ‘they’; Cor. cf. hemma, m., ho- mma, f. ‘this’; OE sē, m., sēo, seō ‘he, she; which’; ON sjá, mf. ‘this, he, she’. (NB. For Slavonic types in sěj, si-, etc. see Kis) : Siü-dhlom, -trom ‘sewing device, needle, bodkin’. Cf. siūið and next Skt. cf. sütram, n. ‘thread’; Lat. sūbula f. ‘awl’; OHG siula, süla, f. id.; MHG siuwele, siule, wf. id.; LG sügel, m. id.; Sw. syl pl. -ar, m. id.; OCS šilo, Cz. šídlo, id.; Li. siūlas, m. “thread”; siule, f. ‘seam’.
siüio, (silluos, siüs) ‘suture, seam? WP II, 515. Cf. siü-dhlom, siüio Skt. cf. syüh, f. ‘string’; ON syja, f. “line of boards in a ship’; OCS (and com. Sl.) Sívá, m. ‘suture’; Slovak šev, gs: švu, id.; Li. cf. siüvis, gs. siüvio, m. ‘stitch’; Latv. Suve, f. id.
siüið (siüuo) ‘sew’. WP II, 515. Cf. siü-dhlom, siüio, siütós and next Skt. sivyàmi, pp: syutáb, id.; Oss. xwin, Dig. xujun, pp: xud, id.; Gk. cf. kas-süo, v. (‘sew together, « *Kmt-. Here Ainsworth 1736: suo: *kassüo for katasuó?); cf. pisuggos (/shoe- maker’, fr. *ped-suuo-, with pi- for *pe- before *su-, cf. písures); Lat. suo, ére, id.; Go. siujan; OHG siuwen; OS siuwian; OE seowan & séo- wian; Sw. sy, id.; OCS (and com. Sl.) So, Siti, id.; Li. siüvu, siūti, id.; Latv. Sum, šūt, id.
siümn- ‘suture’. Cf. sitið, etc. Skt. syüman, n. “band, thong, stitch’; Hitt. (?) sumanc (queried: *thread"); Gk. humén, gs: -ménos, m. ‘membrane’ beside kás-süma, n. ‘thing stitched, sole, leather patch’; Lat. cf. fer- rumen, n. ‘solder, glue’ (?) (cf. dher-); MIr. süainem, s. (error for *süaimen "hong: OPr. Sumeno fcobbler's sewing thread"
siütós ‘sewn’; siütis ‘sewing, suture’. See siüió, etc. Skt. syütáh, id. beside syütih, f. sewing; bag’; Oss. xud, pp. ‘sewn’; Lat. sütus, adj. id.; MHG
1145
siut, sm. ‘stitch’; ON súð, f. “tongue of board’; OCS au (and com. SL), pp. as Skt.; Li. siütas, Latv. Süts, id. Cf. *sieut- in Skt. syotah (beside syütah *bag"); OE sēod, m. ‘purse’; Icel. sjóður, id.
sküb- ‘gouge, dig out; gouger, trowel, scoop’. . (Short vowel in) MHG schepfe, scheffe, f. ‘trawling-net’; Du. schep, m. ‘scoop, trowel’; E skep ‘trough for builders rubble’; Du. scheppen, v. ‘shovel up’; G schöpfen, v. ((2) ‘bale out, ladle out, w. vowel-rounding); (long vowel in); MHG schuofe, wf. ‘ladle, scoop’; Swiss schüefe f. id., Du. schoep, f. ‘paddle, shovel, scoop’; E (fr. Norse) scoop; MLG schōpe(n),
```


## [2026-09-14T02:02:51.210Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==635' IEC.txt | head -c 3500"
}
```


### [2026-09-14T02:02:52.121Z] TOOL RESULT

```
 (-əlos) Hes. skáphalos ‘ladle, baler’; Ir. scabhal, mf. ‘cauldron’
skabhos, à (skobh-?) (1) ‘cłasp, catch; prop, stay, support. Cf. skobh- (2) Skt. cf. skabhnómi, -nümi, v. “fix; prop’; Arm. cf. xab, xabK, s. ‘ambush; trick, fraud"; xabem, v. ‘trick’; OCS skobü, skoba, mf. ‘brooch’; Big. Cz. skoba, f. ‘clamp, cramp’; Oss. cf. käbäl ‘linchpin, peg, bobbin’
skăb- — skal-
15
20
25
30
35
40
45
1146
skabhos (2) ‘cutting, sharp; cut’. Cf. skobh- (1). (Gmc. & S1. ambig.) Gk. skáphos, m. ‘digging’; n., gs: -eos, & ska- phé, f. (*trench'. Fem. also ‘trough, boat’); MHG schabe, wf. ‘rasp; shaving; ringworm; moth’; OE scafa, wm. ‘plane (tool); Du.
. schaaf, f. id.; cf. E spoke-shave; Sw. skav, n.
*offcut, cutting, shaving’; Big. skoba, f. (2) ‘spokeshave’; R cf. skobeP, m. id.; Li. skabùs, adj. ‘cutting, sharp’
skabhros ‘rough, sharp’. Cf. skab- and WP II, 563 Lat. scaber, f: scabra, adj. ‘rough, rugged, dirty, scaly’; LG cf. schabberig, adj. ‘severe, auste- re: Latv. skabrs, adj. ‘fissile, sharp, shrill, penetrating’. (Isophonic: Oss. kåbår ‘hunk of bread": käbur, kåbíla ‘pup’; Li. skabrüs ‘nim- ble, lively’. Here?)
skabhtos (assimilated to skaptos. Cf. skăbh-, and skap- as a separate entry) Gk. skaptós, adj. (dug, diggable'. Here, in view of skápto, pf. éskapha, v. 'dig); OE (ambig.) sceafóa, sceafoóa, wm. (“chip, shav- ing’. Cf. skap-); Li. skábtas, m. ‘gouge’
skadro- (skhadro-?), cf. skhad- Du. schateren, Fris. skatterje, v. ‘burst out laughing’; Du. schater-lach, m. ‘outburst of laughter’; E to shatter; Latv. skadrs, adj. ‘split- ting; gay, lively, fresh; shrill, dazzling’
(skag-, see skhag-)
(skaiuo, ið (skauið) ‘divert, bend, twist’. See next)
skaiuos ‘left-hand, sinister, odd, strange’. Cf. skauios (skauios), skeuios, ksauios, kseuios. WP II, 537 Per. cf. šūx, adj. ‘lewd, impudent'; Oss. xiw, adj. ‘straddle-legged’; Gk. skaiós, adj. “left- handed, awkward, stupid, unlucky, crooked’; Alb. (variant) i huej, Tosk i huaj, adj. ‘strange, foreign’; Lat. scaevus ‘lefthand, sinister, un- lucky’; W ysgoew, adj. ‘wry; fickle’; cf. ysgoe- wan, m. ‘fickle one’; Li. dial. cf. (variant) Seivas (*crooked', fr. *ksaiuos); ON cf. (vari- ant) skeifr, adj. ('skew”, fr. *skaip- or *skaibh-. Ambig.)
(skaió ‘split, divide’, see sKhaio)
skal- ‘point, spike, splinter, flake’. Cf. skel-, skol-, skl-. (Hitt., Gmc. and Balto-Slav ambig.
1147
Alb. ambig.) Hitt. cf. skallai(mi), v. (queried: “split'); Gk. cf. skállo, v. “hoe, harrow, rake’; skaleús, m. ‘hoe’; Alb. halë, f. *pine-needle; scale; awn; prickle; splinter; flake of chaff; W ysgall, pl. ‘thistles’; Cor. ascal, id.; Br. cf. askol, m. Cthistle', perh. fr. *aK-skol-); Go. skalja, f. ‘stile’: MHG schal(e), s & wf. “shell, cup’; OE scealu, sciell, f. *shell, husk; scale; scale-pan'; WG Schall, f. “bolt, bar; Du. schel, f. ‘scale, glaucoma’; G. dial. Schelle (beside Schale), f. ‘dish’; ON skel, plur. -jar, f. ‘shell’ beside skál, pl. -ir, f. “bowl, scale-pan'; OCS skoli- ka ‘shell’; R cf. o-skólok, m. ‘splinter, chip’; Li. skalà, f. id.; skalüs ‘fissile’; Latv. skals (1log: Li. skàálas, id.)
skalið, see skal-
skalmos, à (1) “peg, thole-pin, linchpin, row- lock, haft, board'. Cf. skal-. WP II, 591 Gk. skalmós, m. ‘peg; tiller; (LW in) Lat. scalmus, 1, m. "rowlock thong o
```


## [2026-09-14T02:03:05.921Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"pdf page\" incoming/WLD/WLD_Bd2_pages.txt | head -3; python3 - <<'EOF'\nimport re\np='/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt'\nt=open(p,encoding='utf-8',errors='replace').read()\n# find skai-u̯o- mention\nfor m in re.finditer(r'skai', t):\n    print(m.start(), repr(t[m.start()-120:m.start()+300]).replace('\\\\n',' | ')[:420])\n    print('---')\nEOF"
}
```


### [2026-09-14T02:03:07.102Z] TOOL RESULT

```
349525 ' *plakszsakd, nicht nach | Fick^BB. 3, 162 zu gr. Tiakaoig, s. pela, oder nach Prellwitz^ 349 aus einem | *plak-), lett. plaskains „glatt, flach und breit zugleich‘*, aksl. plosk |                                                                          7 „flach^‘; es      > |  |  | kann ^pldt-sqo- (s. MeiUet Et. 332, Brugmann II^ l 480), aber auch ^plaq-sqo-, |                                                       
---
804873 " biyszJcau, blyJcs^i „erbleichen“, | blaiksztaus, -pis ,,sich aufklaren, Tom Hiramek^; lett. blaiskums „Fleck“, | meln’-blaiskai'tis „dunkelgrau‘‘- |   Kuss.-ksl. bleshb „Glanz“ (ablautend aksl. blisk^ „Glanz'‘ und *bhsk^ in | eech, blesk (gen. alt blsku) „Bbtz“; aksl. bhStq, bhsfati „glanzen‘‘, Iter. | bliscajq,    bliscati s§ (usw. ;      s.   Berneker 60 f., 63 f., Trautmann Bsl. Wb. 34; | Yf. KZ. 34, 51 5 f.;   
---
2040553 "pen „auf- und niedergehn, von schwammigem Boden^*, ablautend mhd« | \x0c                                         suordos   — skai-                                                  535 |  | sumpf jjSumpf = aisl. soppr „BairS norw. auch „Pilz^*; die germ. Form en- |                   ' |  |  |  |  | dreiheit berechtigt nicht zu Feists Got. Wb. 256, Annahme von Entlehnung | irgendwoher, etwa  dem Finnischen. |   Kuhn K
---
2043072 'lel vom „schwingenden Fluge“ zu einer Wz. suel- „drehen“, | 8.   iiber   deren ungeniigende Gewahr unter uel- „drehen“. |  |  | skai- jjgedampft schimmern          ; |                                          Schatten (Abglanz)“         :   ^di-    :   ski-. |  |      Ai. chayd „Glanz, Schimmer, Schatten”, av. a-saya-                    „wer keinen Schatten | wirft”, np.    saya „Schatten, Schutz”. |      Gr. oyAa (
---
2045950 'll, rein\'\', mhd. (md.) scMr planter", nhd. schier; | aisl. skmrr „rein, klar", afries. skeria „reinigen" (aber nicht ahd. skai |  | jjSagax" s. u. sqd- „schneiden“). |   DaS die germ. Worte in der Anwendung auf hellen Glanz etwa z. T. | auch der Wz. sqai(t\\^ -d) „heir\' entstammen, ware erst zu erwagen, wenn | diese ohne erweiternden Dental nachgewiesen wiirde. |      Abg.   sijati^ sinqti „glanzen, scheinen, hel
---
2047907 ' | auf “       „echt, .rein, unverfalscht" mit Eecht anreiht, ist hochst fraglich. | \x0c                                      skaiuos   —    (s)qai(-t-, -d-)                                         537 |  | skaiaos „liak \'‘5 reimt auf Haiuos. |   Gr. ocaiog = \\dit, scaevus                    oTiaiorrjg         ^ scaevitcls.          Curtius 166.      Viel- | leicht ursprgL „schief“ (wenngleich norw. dial, skaa „s
---
2047984 "ch. | \x0c                                      skaiuos   —    (s)qai(-t-, -d-)                                         537 |  | skaiaos „liak '‘5 reimt auf Haiuos. |   Gr. ocaiog = \\dit, scaevus                    oTiaiorrjg         ^ scaevitcls.          Curtius 166.      Viel- | leicht ursprgL „schief“ (wenngleich norw. dial, skaa „schi€f“ niclit als | ^shxiuos zu vergleichen, sondern zu mlid. schcehe „scliief“ 
---
2048896 " (cymr. esgud | „flink, rege“) aus kelt. ski-tos^ nir. sets „Ermudung'‘ (-^^Suffix), mit welchen | Prellwitz^ 413 auch idg, skaims vereinigen will (B. bei Fick II ^ 310 ver- | bindet seitk mit russ. Mi-ryj ,jklein, diirftig^ hochst fragwiirdig); sollte | freilich setth usw. zu skUh- „beschadigen“ gehoren (s. d.), wiirde nir. do- | tach^ wenn altes i dafiir sicher steht, Yon scith zu trennen sein; oder es | ist dotac
---
2050077 '. skdistas^ Fick KZ. 21, 8f.) und caelum „Himmel“ | {*qaid4o- oder quid-, qait-slo-^ vgl. mit -r-Formans dt. heiter, lit. skaid-riis^ | skdidrus; Solmsen Stud. 184, s. auch Vf. LEWb.^ s. v. nicht wahrschein-               ; |  |  | licher nach Thurneysen GGA. 1907, 803 synkopiertes ^caerlum als sub- | stantiviertes n. des Adj. *caerulus^ s. u.        „Farbbezeichnung“)‘ |    Got. haidus „Art und Weise“ (ursprgl. *„l
---
2051081 'tt“ [^hai-ma-^ | KogellF. 4, 312ff.). |    Lit.                 „hell, klar (von    der Luft,           vom Wetter}‘\\ lett. skaidrs „hell, | klar, deutlich, durchsichtig, reiu^‘,           lit.       skdistas, skaisfns ,heH“, apr. skistan |                                                                                           5 |  |  |  | acc. „rein‘‘ (: abg. cistz ds.), ferner mit den Bed. „Flussigkeit durch Mi
---
2051165 'Luft,           vom Wetter}‘\\ lett. skaidrs „hell, | klar, deutlich, durchsichtig, reiu^‘,           lit.       skdistas, skaisfns ,heH“, apr. skistan |                                                                                           5 |  |  |  | acc. „rein‘‘ (: abg. cistz ds.), ferner mit den Bed. „Flussigkeit durch Mischung | mit Wasser klarer, durchsichtig machen (s. Lit. u. sqei- „scheiden‘‘, auch | fu
---
2051592 'te), lit. skiedziu, skiesti ^verdiinnen (z. B. Milch | mit Wasser)‘\',          skystas    „dunnfiussig‘\',         lett.   skaidlt „Getranke               verdiinnen", | skists „dunnflussig“ (und „rein, klar,                    keusch”;      sklstit „reinigen,           saubern‘% | \x0c538                                    (s)q(h)ai(d)-   — sqat- | Bfitdinat „dunn, fliissig maclien‘‘, sMidrs „dunnflussig‘‘) ; abg.
---
2075008 'gemachter Sack“ | (Pick III^ 89, Palk-Torp u. hit). |    Lit. sMedziu, skiesti „trennen, scheiden\'", Iter, skdidyti (: got. skaidan^ | 8. Brgm. IP. 32, 193, ai. chedayati)^ skiedrd „Span“, skiemenys pi. „der beim |  | Weben durch die Trennung der oberen und unteren Faden vermittelst der | Hevelten entstandene Raum, durch welche das Schifflein geworfen wird“, | skaidulios (?) „Plachsfasern‘‘ (wie spdliai „Plachsscha
---
2075237 "ung der oberen und unteren Faden vermittelst der | Hevelten entstandene Raum, durch welche das Schifflein geworfen wird“, | skaidulios (?) „Plachsfasern‘‘ (wie spdliai „Plachsschaben“ von ^spel- „8palten‘'), | pask^sti „sich zerstreuen“, ganljklos aspkydiisios „zerstreute Weiden‘‘; ohne | anl. s- (durch diss. Schwund?) w^ohl auch sukidq^s „zerlumpt, zerfasert^‘ | (Persson Beitr. 148); |   lett.     skiedu,   skied „
---
2075759 '„die iiber den Weberhefteln sich kreuzen- | den Paden“, skidu, skisi auseinander fallen, zergehn“, skidrs „undicht, dunn% | skaida „Span“. |    Aber      eine urspriinglich        versch.       Gruppe           sind       lit.   skiedziu^   skiesti „ver- | diinnen, z. B. Milch mit Wasser“,                        „dunnflussig“, \\eii. skaidit „Getranke | verdunnen‘% skists „dunnflussig“ (und „rein, klar, keusch“, was
---
2075966 'nd       lit.   skiedziu^   skiesti „ver- | diinnen, z. B. Milch mit Wasser“,                        „dunnflussig“, \\eii. skaidit „Getranke | verdunnen‘% skists „dunnflussig“ (und „rein, klar, keusch“, was aber | nicht nach v. d. Osten-Sacken IF. 33, 193 auf EinfiuB des mss. Hstyj be- | ruht), sklstit „reinigen, saubern“, skldinat „dunn, fliissig machen^‘, skidrs | „diinnflus8ig“, die zu lit. skdistas, sknistus „he
---
2076392 ' strahlend‘‘, | apr. skistan Acc, „rein“, lett. skaldrs „hell, klar, deutlich, durchsichtig, | rein“ gehoren (s. sqai- oder skai~ „glanzen, strahlen^), wie auch abg. | (usw.) cisH „rein‘‘, cistiti „reinigen‘‘                            cestiti „reinigen‘^, cediti         „seihen" | \x0c                                                           sqei-                                           545 |  | (s.   Pedersen I
---
2105492 'Bruch“, schor en „zerrei6en trans. und intr,“ auf *sqti-ro- oder          zu- | riickgeht, ist fraglich) sicher gehn got. skaiiro „Schaufeh‘ (in winpi-skmlro |                               ; |  |  | „Wurfschaufel“), ahd. scora, mhd. schor 5,Schaufel, Haue, Spitzhaue“, | schorn „zsscharren, kehren, fortstoBen“, schilrn „einen AnstoB geben, reizen, | dasFeuer durchstoren, anfachen, schuren“, Aisl. skora „scheuern, sc
---
2108533 '- ,,schneiden“ gehorigen "^skernas (vgl. skara „Fetzen, Lumpen^) | umgebildet? |    Mit c?-Erw. lit. skudrus „scharP, lett. skaiidrs ds., skaudre ,.scharfe |                            : |  |  |  | Kante“ (anders Leskien Abl. 308: zu lit. skaiidiis „schmerzhaft“ usw. s. Wz. | sqeiid- „unwil]ig‘‘). |    S. Johansson IF. 19, 125ff. (mit vielem fernzuhaltenden), Persson Beitr. | 374 if., 952, 883.              — |     
---
2108638 "„scharP, lett. skaiidrs ds., skaudre ,.scharfe |                            : |  |  |  | Kante“ (anders Leskien Abl. 308: zu lit. skaiidiis „schmerzhaft“ usw. s. Wz. | sqeiid- „unwil]ig‘‘). |    S. Johansson IF. 19, 125ff. (mit vielem fernzuhaltenden), Persson Beitr. | 374 if., 952, 883.              — |                     Ganz fragwiirdig reiht Petersson IF, 24, 257 f. lit. kunas | „Fleisch, Leib‘' an (vgl. zur Be
---
2111903 'tig, neidisch | sein,        schmollen, zurnen\'^,      lit.    skaudiis „schmerzhaft,           verdrieBlich,    heftig", | skaiista (skandcti) „es schmerzt^,                 lett. skdithi,     skdudti^ skdnst „miBgunstig, | neidisch sein   und schadigen“, skaiidU ds., lit. skaiididtfs „Geschwur‘^ |      Bezzenberger-Fick BB. 6, 240, Pick Wb.       566. Zur bait. Sippe s. Les- | kien Abl. 308 (aber lit. skiidrhs „s
---
2112034 "kandcti) „es schmerzt^,                 lett. skdithi,     skdudti^ skdnst „miBgunstig, | neidisch sein   und schadigen“, skaiidU ds., lit. skaiididtfs „Geschwur‘^ |      Bezzenberger-Fick BB. 6, 240, Pick Wb.       566. Zur bait. Sippe s. Les- | kien Abl. 308 (aber lit. skiidrhs „scharf‘^, von der Axt, lett. skaiidrs „scharf**', | skaudre „8charfe Kante“ wohl kaum als „woran man sich weh tut“ hierher, | sondern wie
---
2112052 "rzt^,                 lett. skdithi,     skdudti^ skdnst „miBgunstig, | neidisch sein   und schadigen“, skaiidU ds., lit. skaiididtfs „Geschwur‘^ |      Bezzenberger-Fick BB. 6, 240, Pick Wb.       566. Zur bait. Sippe s. Les- | kien Abl. 308 (aber lit. skiidrhs „scharf‘^, von der Axt, lett. skaiidrs „scharf**', | skaudre „8charfe Kante“ wohl kaum als „woran man sich weh tut“ hierher, | sondern wie lett. skaute „sch
---
2112219 "BB. 6, 240, Pick Wb.       566. Zur bait. Sippe s. Les- | kien Abl. 308 (aber lit. skiidrhs „scharf‘^, von der Axt, lett. skaiidrs „scharf**', | skaudre „8charfe Kante“ wohl kaum als „woran man sich weh tut“ hierher, | sondern wie lett. skaute „scharfe Kante‘‘ zu sqeti- „schneiden, kratzen“); | skaudeti usw. nicht zu qeud- „schreien‘', s. d. |  |  |  | 3. (s)qeud- „^yerfeD,          schieBen, hetzen** ;         intr
---
2113867 "e ahd. sco^ „GeschoB, Sch66Iing“ scu^ ^SchuB, ^Yurf, Schnellig- | keit'^,      aisl.   skjotr^ ags. sceot „schnell“, got. skaiita d. sg. „(hervorschieBen- | der) Zipfel oder           Saum eines Kleides''', aisl. skaiit n. „Zipfel, Ecke, SchoB, | Vorsprung“, ahd. sco^ „Zipfel,     KleiderschoB, RockschoB^^ (s. auch Falk- | Torp u. skjed^ skjede)^ mnd. schot{-tt-) „(Yorgeschobener) Riegel, Yerschlu6‘S | wo von schiit
---
2113956 "tr^ ags. sceot „schnell“, got. skaiita d. sg. „(hervorschieBen- | der) Zipfel oder           Saum eines Kleides''', aisl. skaiit n. „Zipfel, Ecke, SchoB, | Vorsprung“, ahd. sco^ „Zipfel,     KleiderschoB, RockschoB^^ (s. auch Falk- | Torp u. skjed^ skjede)^ mnd. schot{-tt-) „(Yorgeschobener) Riegel, Yerschlu6‘S | wo von schiitten „abdammen, hindern, schutzen‘‘, mhd. nhd. schiltzen, Ohne | anl. S’ mhd. hossen^ koUen 
---
2119846 'gl. zum |     Bed.-Umfang die wohl verwandten (Persson Wzerw. 90, Wood Min. |     21, 228) Wzln. sqeud- „werfen, schieBen", skai- ds.; dagegen liegt |     qseiibk- .jSchwanken" in der Bed. weiter ab, als daB Yereinigung der |     Anlaute durch Umstellung zu befiirworten ware. |    Lit. skiibti „eilen", skuhinti „beeilen“, skiihus, skubnis ..flink, eilig"    (aber | abg. skubq^ skubati „zupfen,                reiBen"
---
2537939 '. i, so da6 lett. spiidrs, | spuschs durch Ablautneubildung; Kiedermanns Yereinigung von amvdgg | mit lat. scintilla- s. u. skai- „sehimmern"                   — |                                             als Dissimilationen eines mittel- | meerlandischen ^stinth- ziehe ich nicht mehr vor). Ygl. noch das ahn- | liche "^speng- „glanzen“. |    Zupitza KZ. 36, 61 vermutet mit Unrecht alten r- und ?*Schwund in | span
---
```


## [2026-09-14T02:03:16.887Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"skai\\|ski-\\b\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-14T02:03:16.945Z] TOOL RESULT

```
934:*sua-yo-, contracted to *si-yo- in Greek huein, to rain, and huetos, rain: ISOHYET. II. Possible extended zero-grade form *sib-. 1.Germanic *sip- in: a. Old English sipan, sipian, to drink, sip: suP!; b. Old French soup(e), soup: SOUP, (SUP2). 2. Germanic “supp- in: a. Old English sopp, bread dipped in liquid: sop; b. possibly Low German sippen, to sip, probably akin to the source of Middle English sippen, to sip: stp. III. Possible ex- tended zero-grade form “sig-. 1. Germanic *sik- in Old English sican, to suck: sucK. 2. Germanic shortened form *sukdn in Old English socian, to steep: SOAK. 3. Latin siigere, to suck: SUCTION, SUCTORIAL. 4, Variant form *sik- in Latin siicus, succus, juice: SUCCULENT. [Pok. 1. seu- 912.] seut-. To seethe, boil. 1. Germanic *seuthan in Old English séothan, to boil: SEETHE, (SODDEN). 2. Germanic *suth- in: a. Middle Dutch sudde, sudse, marsh, swamp: sups; b. suffixed form *suth-l- in Middle High German sudelen, to soil, do sloppy work, akin to Middle Dutch soetler, sutler: SUTLER. [Pok. 4. seu- 914.] si-lo-. Silent. Suffixed (stative) form *si/-é- in Latin silére, to be silent: SILENT. [In Pok. 2. sé(i)- 889.] skabh-. To prop up, support. Suffixed form *skabh-no- in Latin scamnum, a bench (> Old English sceamel, table, stool): SHAMBLES. [Pok. skabh- 916.] skai-. Also kai-. Bright, shining. 1. Extended form *kaid- in Germanic *haiduz, “bright appearance,” manner, quality, in Old English -hdd, quality, condition: -Hoop. 2. Suffixed form *ki-t-ro- in Sanskrit citra-, variegated, many-colored: CHEETAH, CHINTZ. [Pok. (s)kdi- 916.] [skalkaz. Servant, slave. Germanic noun of unknown origin. 1. Old High German compound marahscalc, “horse-servant” (see marko-). 2. Germanic compound *sini-skalkaz, “old servant” (see sen-'). [In Pok. (s)kel- 929.]] skamb-. Also kamb-. To curve, bend. Suffixed form *kamb-o- in Celtic *kambo-, crooked, and denominative verb *k(a)mb-yo-, to turn, exchange, whence Gallo-Latin cambidre, to exchange: CAMBIST, CAMBIUM, CHANGE. [Pok. (s)kamb- 918.] skand-. Also skend-. To leap, climb. 1. Latin scandere, to climb: SCAN, SCANDENT, SCANSION, SCANSORIAL; AS- CEND, (CONDESCEND), DESCEND, TRANSCEND. 2. Suffixed form *skand-alo- in Greek skandalon, a snare, trap, stumbling block: SCANDAL. 3. Suffixed form *skand-sld- in Latin scdlae, steps, ladder: ECHELON, ESCALADE, SCALE?. sked-. To split, scatter. Extension of sek-. 1. O-grade form *skod- in Germanic *skaé- in Old English *sc(e)ater- ian, to scatter: SHATTER. 2. Variant nasalized form *ska-n-d- in Latin scandula, a shingle for roofing (< “split piece”): SHINGLE}. [Pok. (s)k(hjed- 918.] skeei-. To gleam. 1. Suffixed form “ske(ji-no- in Ger- manic *skinan, to gleam, shine, in: a. Old English scinan, to shine: SHINE; b. Old High German scinan, to shine: GEGENSCHEIN. 2. Germanic extended form *ski-m- in Old English scimerian, scymrian, to shine brightly: SHIM- MER. 3. Possibly suffixed form *ski-nto-, shining, in Latin scintilla, a spark: SCINTILLA, SCINTILLATE, STEN- CIL, (TINSEL). 4. Suffixed zero-grade form *skia-G-, *skiy-d- in Greek skia, shadow: SKIAGRAM, SKIASCOPE, SQUIRREL. [Pok. skai- 917.] skei-. To cut, split. Extension of sek-. 1. Germanic suffixed form *ski-nd- in: a. Old English scinu, shin, shinbone (< “piece cut off’): SHIN!-; b. Old French eschine, backbone, piece of meat with part of the back- bone: CHINE, 2, Latin scire, to know (< “to separate one thing from another,” “discern”): SCIENCE, SCILICET, SCIOLISM, SCIRE FACIAS; ADSCITITIOUS, CONSCIENCE, CONSCIOUS, NESCIENCE, (NICE), OMNISCIENT, PLEBI- SCITE, PRESCIENT. 3. Suffixed zero-grade form *skiy-end in Old Irish scian, knife: SKEAN. 4. Extended root *skeid- in: a. Germanic *skitan, to separate, defecate, in Old English *scitan, to defecate: SHIT; b. suffixed zero-grade
936:form *sk(hjid-yo- in Greek skhizein, to split: SCHISM, SCHIST, SCHIZO-; C. nasalized zero-grade form *ski-n-d- in Latin scindere, to split: SCISSION; EXSCIND, PRESCIND, RESCIND. 5. Extended root *skeit- in: a. Germanic *skaith-, *skaidan in (i) Old English scéadan, to sepa- rate: SHED! (ii) perhaps Old English scéath, sheath (< “split stick”): SHEATH; b. Germanic *skidam in Old Norse skidh, log, stick, snowshoe: SKI; C. o-grade form *skoit- in Latin scittum, shield (< “board”): ECU, ES- CUDO, ESCUTCHEON, ESQUIRE, SCUDO, SCUTUM, (SQUIRE). 6. Extended root *skeip- in Germanic *skif- in: a. Middle English sheve, pulley (< “piece of wood with grooves”): SHEAVE?; b. Old Norse skifa, to slice, split, akin to the Scandinavian source of SKIVE; c. Middle Low German schever, splinter, akin to the possible Low German source of Middle English schivere, scivre, splinter: SHIVER?. [Pok. skei- 919.] skel-'. Also kel-. To cut. 1. Germanic *skalj6, piece cut off, shell, scale, in: a. Old English scell, sciel, shell: SHELL; b. Italian scaglia, chip: SCAGLIOLA. 2. Germanic *skalé in: a. Old English sc(e)alu, husk, shell: SHALE; b. Old French escale, husk, shell: scALE!. 3. Germanic *skal- in: a. Old Norse skalli, bald head (< “closely shaved skull”): SCALL; b. Old Norse skalpr, sheath, shell, akin to the source of Middle English scalp, scalp: SCALP. 4. Germanic *skél6é in Old Norse skal, bowl, drinking vessel (made from a shell): SCALE’, SKOAL. 5. Germanic *skelduz in Old English scield, shield (< “board’’): SHIELD. 6. Germanic *skeli- in: a. Old Norse skil, reason, discernment, knowledge (< “‘incisiveness”): SKILL; b. Middle Dutch schillen, to diversify, with past partici- ple schillede, separated, variegated, akin to the Low German source of Middle English scheld, variegated: SHELDRAKE. 7. Germanic skulé, a division, in Middle Low German schdle, troop: SCHOOL?, SHOAL’. 8. Suffixed variant form *kel-tro- in Latin culter, knife: COLTER, CULTRATE, CUTLASS. 9. Suffixed zero-grade form “skl-yo- in Greek skaillein, to stir up, hoe (> skalenos, uneven): SCALENE. 10. Extended root *skelp- in: a. Germanic *skelf- in Middle Low German schelf, shelf (< “split piece of wood”): SHELF; b. possibly Germanic *halbaz (< variant root *kelp-), divided, in Old English healf, half: HALF; C. perhaps variant *skalp- in Latin scalpere, to cut, scrape, with derivative sculpere (originally as the combining form of scalpere), to carve: SCALPEL, SCULP- TURE. [Pok. 1. (s)kel- 923.] skel-2. To be under an obligation. O-grade (perfect) form *skol- in Germanic *skal-, I owe, hence I ought, in Old English sceal (used with the first and third person singular pronouns), shall: SHALL. [Pok. 2. (s)kel- 927.] skel-3. Also kel-. Crooked. With derivatives referring to a bent or curved part of the body, such as a leg, heel, knee, or hip. 1. Suffixed form *skel-ko- in Germanic *skelha- in Old High German scilihen, to wink, blink (> German Schiller, iridescence): SCHILLER. 2. Suffixed form *skel-es- in Greek skelos, leg: ISOSCELES, TRISKELION. 3. Suffixed o-grade form “skol-yo- in Greek skolios, crooked: sco.iosis. 4. Lengthened o-grade form *skol- in Greek skéléx, earthworm, grub (< “that which twists and turns”): SCOLEX. 5. Suffixed lengthened-grade form *k6l-o- in Greek kélon, limb, member: COLON}. 6. Attrib- uted (quite doubtfully) by some to this root is Greek kulindein, to roll: CALENDER, CYLINDER. [Pok. 4. skel- 928.] skele-. To parch, wither. Variant *sk/é-, contracted from *skleo-. 1. Greek skellesthai, to dry, whence skeletos (< suffixed form *skeb-to-), dried up (body), mummy: SKELETON. 2. Suffixed variant form *sk/é-ro- in Greek skléros, hard: SCLERA, SCLERO-, SCLEROMA, (SCLEROSIS), (SCLEROTIC), SCLEROTIUM, SCLEROUS; SCLEROTIZATION. [Pok. 3. (s)kel- 927.] skeng-. Crooked. Germanic *skank6n-, “that which bends,” leg, in Old English sc(e)anca, shinbone: SHANK. [Pok. (s)keng- 930.]
943:(s)keu-. To cover, conceal. Zero-grade form *(s)ku-. Variant *(s)keua-, zero-grade form *(s)kua-, contracted to *(s)kii-. 1. Suffixed basic form in Germanic *skeu-jam, cloud (“cloud cover’), in Old Norse sky, cloud: sky. 2. Zero-grade form *skd- in: a. suffixed form *ski-mo- in Germanic *skiimaz, foam, scum (< “that which covers the water’), in (i) Old High German sciim, scum (> German Schaum, foam): MEERSCHAUM (ii) Middle Dutch schiim, scum: SCUM; Db. suffixed form *ski-ro- in Latin obsciirus, “covered,” dark (ob-, away from; see epi): OBSCURE; CHIAROSCURO. 3. Zero-grade form *ku- in: a. suffixed form “ki-ti- in Germanic *hidiz in Old Eng- lish Ayd, skin, hide: HIDE?; b. suffixed form *ku-ti- in Latin cutis, skin: CUTANEOUS, CUTICLE, CUTIS; CUTIN; c. possibly suffixed form *kd-lo- in Latin cilus (> French cul), the rump, backside: CULET, CULOTTES; BASCULE, RECOIL; d. suffixed form *ku-to- in Greek kutos, a hollow, vessel: -cyTE, cyTo-. 4. Extended zero-grade form *kus- in: a. Germanic *huson- in Old English hosa, hose, covering for the leg: HOSE; b. suf- fixed form *kus-dho- (or suffixed extended form *kudh- to-) in Germanic *huzdam in Old English hord, stock, store, treasure (< “thing hidden away”): HOARD; c. Rus- sian kishka, gut (< “sheath”), akin to the Slavic source of Yiddish kishke, kishke: KISHKE. 5. Suffixed extended zero-grade form *kut-no- in Latin cunnus, vulva (< “sheath”): CUNNILINGUS. 6. Extended root *keudh- in: a. Germanic suffixed lengthened zero-grade form *hiid- Jan in Old English hydan, to hide, cover up: HIDE}; b. Germanic suffixed zero-grade form *hid-jdn- in French hutte, hut: HuT. [Pok. 2. (s)keu- 951.] skeubh-. To shove. 1. Germanic *skeuban and derivative lengthened zero-grade form *skdban in: a. Old English sciifan, to shove: SHOVE; b. Old Norse skifa, to push, perhaps akin to the probable Scandinavian scource of SCUFF, SCUFFLE!, 2. Germanic suffixed form *skub-ilé- in: a. Old English scofl, a shovel: SHOVEL; b. Middle Dutch schoffel, schuffel, a shovel, hoe: SCUFFLE?. 3. Ger- manic *skub-, *skuf-, *skup- in: a. Danish skof, jest, teasing, probably akin to the Scandinavian source of Middle English scof, mocking: scoFF; b. possibly (but quite doubtfully) Old English scop, poet (< “jester’): scoP; c. Low German schiiffeln, to walk clumsily, shuffle cards, probably akin to the source of SHUFFLE. [Pok. skeub- 955.] skeud-. To shoot, chase, throw. 1. Germanic *skeutan, to shoot, in: a. Old English scéotan, to shoot: SHOOT; b. Old Norse skj6ta, to shoot: SKEET. 2. Germanic *skutaz, shooting, shot, in: a. Old English sceot, scot, shooting, a shot: sHOT!; b. Old High German scuz, shooting, a shot: scHuss; C. Old Norse skot and Old French escot, contri- bution, tax (< “money thrown down”): SCOT, (SCOT AND Lot). 3. Germanic *skutjan probably in Old English scyttan, to shut (by pushing a crossbar): sHUT. 4. Ger- manic *skutilaz in Old English scytel, a dart, missile: SHUTTLE. 5. Germanic *skautj6n- in: a. Old English scéata, corner of a sail: SHEET?; b. Old English scéte, piece of cloth: SHEET!. 6. Germanic *skut- in Old Norse skita, mockery (< “shooting of words”), akin to the Scandinavian source of scouT*. 7. Germanic “skaut-, perhaps in Old French escoutille, hatchway: SCUTTLE}, [Pok. 2. (s)keud- 956.] skeup-. Cluster, tuft, hair of the head. 1. Germanic *skauf- in Old English scéaf, bundle, sheaf: SHEAF. 2. Possibly Germanic *hupp- in Middle Dutch hoppe, the hop plant (having tuftlike inflorescence): HoP?. [Pok. (s)keup- 956.]
1348:CHASM ghai- CHASSIS kap- CHASTE kes-2 CHAUDFROID kele-1 CHEAP caupd CHECK tké- CHECKMATE tké- CHEER ker-! CHEESE? kWo- CHEETAH kWeij-2, skai- CHEILOSIS ghel-una CHELICERA ker-1 CHELONIAN gheli- CHEMOTROPHY threph- CHENILLE kwon- CHENOPOD ghans- CHERISH ka- CHERNOZEM kers-1 CHERRY ker-6 CHERSONESE ghers-, sna- CHESS’ kap-
1355:CHINTZ skai-
1641:-HOOD §skai-
```


## [2026-09-14T02:03:29.111Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -on \"SCENE [a-z()ə-]*\\|SCENARIO [a-z()ə-]*\\|SKIAGRAM [a-z-]*\" AHD_watkins1985.txt | head -10; echo \"=== KLN scene\"; grep -n \"scene, n\\.\\|scene,n\\|skene\\|σκηνή\" KLN_1966.txt KLN_1971.txt | head -10"
}
```


### [2026-09-14T02:03:29.194Z] TOOL RESULT

```
2268:SKIAGRAM skeei-
=== KLN scene
KLN_1971.txt:63800:damascene, n., damson plum. — Lit. ‘plum of 
KLN_1971.txt:63946:see damascene, n. 
KLN_1971.txt:152518:mise-en-scene, n., 1) setting on the stage; 2) 
KLN_1971.txt:214307:scene, n. — MF. scene (F. scene), fr. L. scaena , 
KLN_1971.txt:220210:OHG. skbni, OFris. skene , MDu. scone , MHG. 
KLN_1971.txt:223232:skene, n. — A var. of skean. 
KLN_1966.txt:34928:sheen,  adj.,  beautiful,  bright.  —  ME.  schene, shene,  fr.  OE.  sciene,  scene,  scyne,  rel.  to  OS., OHG.  skbni,  OFris.  skene,  MDu.  scone,  MHG. scheme,  Du.  schoon,  G.  schon,  Goth,  skaunjai, nom.  pi.,  ‘beautiful’,  fr.  Teut.  base  *skauni-, orig.  meaning  ‘conspicuous,  considerable’,  fr. I.-E.  base  *(s)qeu-,  *(s)qeu-,  ‘to  look  at,  observe, perceive’.  See  show  and  cp.  scone.
KLN_1966.txt:35415:skene,  n.  —  A  var.  of  skean. skep,  n.,  1)  a  kind  of  basket;  2)  a  beehive.  —  ME. skeppe,  ‘skep,  skepful’,  fr.  OE.  sceppe,  ‘skepful’, fr.  ON.  skeppa,  ‘basket,  bushel’,  which  is  rel.  to OS.  skepil,  MDu.  scepel,  Du.  schepel,  OHG. sceffil,  MHG.,  G.  scheffel,  ‘bushel’,  and  to  OS. skap,  MDu.  scap,  OHG.  scaf,  MHG.  schaf,  G. Schaff,  ‘cask,  barrel’;  fr.  I.-E.  base  *skab-,  ‘to work  with  a  stone  scraper,  to  scrape,  scratch’. See  shape,  n.,  and  cp.  skipple. skeptic,  sceptic,  adj.  —  F.  sceptique,  fr.  L.  scepti- cus,  fr.  Gk.  crxETtrixbq,  ‘inquiring,  thoughtful, doubting’,  which  is  rel.  to  aximsa&oit,  ‘to  look carefully,  consider',  oxi^iS,  ‘inquiry,  doubt’, and — with  vowel  gradation — to  oy.oTretv,  ‘to
```


## [2026-09-14T02:03:32.231Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '214300,214325p' KLN_1971.txt; echo \"=== scenario\"; grep -n \"scenario\" KLN_1971.txt | head -3"
}
```


### [2026-09-14T02:03:32.328Z] TOOL RESULT

```
referred to. 

scenario, n., outline of the plot of a play. — It., 
fr. Late L. see nan us, ‘of stage scenes’, fr. L. 
scaena , scena. See scene. 

Derivative: scenar-ist , n. 
scene, n. — MF. scene (F. scene), fr. L. scaena , 
scena, ‘stage, scene’, fr. Gk. axTjvY), ‘tent, booth, 
stage’, which is rel. to mad, ‘shade’, fr. I.-E. 
base *ska(i), *sk & i~, *ski-, ‘to shine, flicker, 
glimmer’, whence also OI. chdya, ‘brilliance, 
luster; shadow’, Toch. B. skiyo. Alb. he, ‘shad- 
ow’, Goth, skeinan , OE. scinan, ‘to shine’. See 
shine and cp. words there referred to. Cp. also 
proscenium, mise-en-scene. 
scenery, n. — Fr. earlier scenary , fr. L. scendrius, 
‘pertaining to the stage’, fr. scaena , scena. See 
scene and -ery and cp. scenario, 
scenic, adj. — F. scenique, fr. L. scaenuus, sceni- 
cus , fr. Gk. oxt)vix 6<;, fr. majvV). See scene and 
-ic. 

Derivatives: scenic-al , adj., scenic -al-ly, adv. 
scenograph, n., a perspective picture. — Back 
formation fr. scenography. 
=== scenario
214302:scenario, n., outline of the plot of a play. — It., 
214318:scene and -ery and cp. scenario,
```


## [2026-09-14T02:03:41.835Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in bd2729d0ce832973 8f7012a03136ce62 aef4d75fc281c662; do echo \"##### $f\"; grep -n -m1 -A6 \"1530s\\|1717\\|Old English scinan\\|scenario (n.)\\|scene (n.)\\|shine (v.)\" $f.txt | head -20; done"
}
```


### [2026-09-14T02:03:42.971Z] TOOL RESULT

```
##### bd2729d0ce832973
23: scene (n.) 
24-
##### 8f7012a03136ce62
23: scenario (n.) 
24-
25- 1868, "sketch of the plot of a dramatic work," from Italian scenario , from Late Latin scenarius "of stage scenes," from Latin scena "scene" (see scene ); earlier in nativized form scenary (1690s). The meaning "imagined situation" is recorded by 1960, in reference to hypothetical nuclear wars.
26- also from 1868 
27-
28- Entries linking to scenario 
29-
##### aef4d75fc281c662
23: shine (v.) 
24-
```


## [2026-09-14T02:03:45.324Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '23,35p' bd2729d0ce832973.txt; echo \"#### shine\"; sed -n '23,35p' aef4d75fc281c662.txt"
}
```


### [2026-09-14T02:03:45.399Z] TOOL RESULT

```
 scene (n.) 

 1530s, "subdivision of an act of a play," also "stage-setting," from French scène (14c.), from Latin scaena , scena "scene, stage of a theater," from Greek skēnē "wooden stage for actors," also "that which is represented on stage," originally "tent or booth," which is related to skia "shadow, shade," via the notion of "something that gives shade" (see Ascians ).

 According to Beekes' sources, the Greek word "originally denoted any light construction of cloth hung between tree branches in order to provide shadow, under which one could shelter, sleep, celebrate festivities, etc."

 A theatrical word; the wider senses come from the notion of the painted drops and hangings on stage as the "setting" for the action. From "stage setting" the sense extended to "material apparatus of a theatrical stage, part of a theater in which the acting is done" (1540s), which led to "setting of any artistic work, place in which the action of a literary work is supposed to occur" and the general (non-literary) sense of "place where anything is done or takes place" (both by 1590s).

 Hence the sense in reference to a (specified) activity and its realm or sphere (1931, as in the poetry scene ) and U.S. slang sense of "setting or milieu or situation for a specific group or activity," attested from 1951 in Beat jargon.

 Meaning "any exhibition, display, or demonstration of strong feeling," especially "stormy encounter between two or more persons," is attested by 1761. By 1650s as "a view presented to the mind or eye." 

 Behind the scenes "having knowledge of affairs not apparent to the public" (1748) is an image from the theater, "amid actors and stage machinery" (back of the visible stage and out of sight of the audience), which is attested from 1660s. Scene of the crime is attested by 1843. To make a scene "make a noisy or otherwise unpleasant demonstration" is by 1831.
#### shine
 shine (v.) 

 Middle English shinen , from Old English scinan "shed, send forth, or give out light; be radiant, be resplendent, illuminate," of persons, "be conspicuous" (class I strong verb; past tense scan , past participle scinen ). This is reconstructed to be from Proto-Germanic *skeinanan (source also of Old Saxon and Old High German skinan , Old Norse and Old Frisian skina , Dutch schijnen , German scheinen , Gothic skeinan "to shine, appear"), which perhaps is from a PIE root *skai- "to shine, to gleam" (source also of Old Church Slavonic sinati "to flash up, shine").

 Of smoothed or polished surfaces, "gleam, give off reflected light," late Old English. Of a person, a face, "be fair-skinned, be beautiful," c. 1200. Also used in Middle English of night when cloudless and starlit. The transitive sense of "cause to shine" is from 1580s; the meaning "to black (boots)" is from 1610s. Related: Shined (in the shoe polish sense), otherwise shone ; shining .

 shine (n.) 

 1520s, "brightness, radiance," from shine (v.). Indicating "sunshine," and paired with rain (n.), from 1620s. Meaning "polish given to a pair of boots" is from 1871.

 For the American English slang meaning "a prank, a trick," see monkey-shines . Often also "a fancy, a liking," as in phrases such as take a shine to , "fancy," attested by 1830 in representations of Yankee dialect; shine up to "attempt to please as a suitor by making a brilliant impression" (1882).

 The derogatory meaning "black person" is attested by 1908, perhaps from glossiness of skin or, on another guess, from frequent employment as shoeshines.
```


## [2026-09-14T02:03:51.538Z] TOOL CALL #60: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nprint(json.dumps(d['BQT'].get('scans'),ensure_ascii=False,indent=1))\nprint('MON scans:',json.dumps(d['MON'].get('scans'),ensure_ascii=False)[:500])\nprint('MON local:',d['MON'].get('local_file'))\n\""
}
```


### [2026-09-14T02:03:52.642Z] TOOL RESULT

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
MON scans: null
MON local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt']
```


## [2026-09-14T02:03:57.111Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -3 BQT_v2_pages.txt; grep -c \"pdf page\" BQT_v2_pages.txt; echo \"=== v4\"; grep -n \"pdf page\" incoming/BQT/BQT_v4_pages.txt | head -3; grep -c \"pdf page\" incoming/BQT/BQT_v4_pages.txt"
}
```


### [2026-09-14T02:03:57.199Z] TOOL RESULT

```
                                         ‫‪7‬‬

                          ‫رن‪۳‬‬
0
=== v4
1:[pdf page 1]
2:[pdf page 2]
23:[pdf page 3]
553
```


## [2026-09-14T02:04:01.220Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} /pdf page 130\\]/{print NR}' incoming/BQT/BQT_v4_pages.txt; python3 - <<'EOF'\nimport re\np='/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt'\nt=open(p,encoding='utf-8',errors='replace').read()\npages=re.split(r'\\[pdf page (\\d+)\\]',t)\nd={}\nfor i in range(1,len(pages),2):\n    d[int(pages[i])]=pages[i+1]\nfor printed in (2047,2336):\n    pdf=printed-1917\n    s=d.get(pdf,'')\n    print('=== printed',printed,'pdf',pdf,'len',len(s))\n    print(s[:1200])\nEOF"
}
```


### [2026-09-14T02:04:02.443Z] TOOL RESULT

```
130
=== printed 2047 pdf 130 len 2553

ند ها ملیوش
و بممتی علوی هم‌آمده است که در برایر سقلی منوشان - بروزن خموشان, ام حاکم
است ۱ ؛ وباین معنی بفتح اول هم کفته‌اند. فاری‌است که ازجانب کیخروحکومت و پادشاهی
منوچهر ؟ - بکر جیم فارسی . فاری میکرد9 - وعنع ازنوشانیدن هم‌هست؟۹ .
یی بهشت روی » چه مئو مخغف مینواست که مه - بفتح اول و ثالی وظهور ها » فك
بهشت باشد وچهره بمعنی روی » و بمعنی علوی | اسفل‌را کوبند که چانه ومرتبهٌ پایین دهان باس
ذأات هم‌هت چه متو بمعنی علوی وچهر بمعنی | و بکسراول و اضم آخر » در عربی بمعتی از او
ذات باشد - و نام پرابرج است وبعتی کفته‌اند | باشد -
نبیرة ابرج است ازجالب دختر » اسّاعلم. کوبند منهیان ۷ ر بع مسکون - کنایه
چون سلم وتور ابرج را کشتند تیغ بر اولاد او از هفت ک و کب است که زحل و مشتری و مرخ
نپادند وا کثرمخدرات اورا هلاكساختند, یکی‌از | وآفتاب و زهره وعطارد و ماه باشد +
سنورات خر کیرجر سابل کرت | منهیان سبع طباق ۶۸- بسنی
کی کل وا مانوی هر کرد ۴ منهیان ربم مسکون است که سبعهٌ سیاره باشد.
کوه متولد شده بود اورا مانوش چهر‌فام کرد
وبمرور ایام وتغییر السته منوچهر شد » و بعتی منیژه ‎٩‏ - با تحتانی مجهول و زای
کوبند که مادر اورا نام نکرد تا بز رکه شد واو | فارسی » بروزن ومعنی منیجه است که نام دختر
بفایت خوش‌سورت بوداورا منوچهرخواندند بمنی | افراسیاب باشد و بیژن پسرکیو یاو عاشق بود.
بپشت صورت چه‌هرچیزخوب ر
=== printed 2336 pdf 419 len 1672

هزیر ۳۳۹
باشد مراسب راکه تاآنرا نشکنند با نکننداسب | بمعنی ستوده و پسندیده وخوب ونيك وخاسگی
علف بغراغت نمیتواند خورد وفربه نمیشود ۱ ۰ | باشد ۴ - و بمعنی جلدی و چابکی و هوشیاری

هیر ۲ - بنتح اور ۴۳ بروزن فقیر » هم‌آمده است 8 ؛ و چم اول نیز گفته‌اند .

بیان نهم
در های هوز با سین بی نقطه مشتمل بر هشت لئفت

هستره « بفتح اولوتای قرشت بروزن | دانه‌واستخوان میوه‌هاراگوبند مانند دانهٌ زردآلو
مسخره , جوال مانندیرا گوبند که ازچوب وبی | وشفتالو وغیره ۷ - و بمعنی‌حق وراستی ودرستی
باقته پاشند و بر پشت الاغ گذارید و بدان‌خعت | و حقایق اشیا هم ()آمده است ۸ - و شخسیرا
وآجر و خاك وامثال آ ن کنند ‎٩‏ . یز کوبند که اقرار و اعتراف بچیزی کند ‎٩‏ .

هستو - با تای قرشت بر وزن بدخو , هستودان *۱- بنتح اول ودال بالف

62 چش: ۳ بنظن .

۱ رشیدی بهمین هعنی آورده است . ۲ «عجیر (ه.م.) * خجیر (۸م.) »
اوستا -136111878 » پپلوی 30018۳ « اسشق 019۱۳۹۳ > بمعنی‌خوب چهر » خوش‌نما . اوستا
-6112 ( نيك ناد ) « بارتولمه ۱۸۲۱ > رك : نیب رک ص ۱۶۹ ؛ شعمیرزادی وطالقانی
۲آزه3 ( خوب ) ۰ ۴ - بضم اول اسح است . ۴ -« عژیر لیکو باشد . دقیفی
(طوسی) گوید :

ای فغر آل اردشیر » ای مملکت را لاکزیر

ای همچنان چون جان و تن » آثار وافعالت هرب .>
« لغت فری ص *۱۶ ۴ .
و رك : صحاح‌الفری لسغهٌ طاعتی . 8 - بمعنی جلد و چايك ( صفت ) است :
کاهگاعی که ا
```


## [2026-09-14T02:04:16.148Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"چهره\" BQT_v2_pages.txt | head -20"
}
```


### [2026-09-14T02:04:16.207Z] TOOL RESULT

```
3518:                         ‫ص‪« »۳‬اسشق ‪ « ۷۳:6‬هوبشمان ‪ ۷۳4‬رك‪ :‬چهره » چرخ‪.‬‬
7791:‫چهیدن ‪ ۰‬بر وزن و معنی چکیدن‬                                  ‫چهره پدرار ‪ -‬سور و مورتگر را‬
21907:‫ک وکباست کهزحل‌ومشتری‌ومرشو فتاب‌وزهره‬                     ‫روت است ‪ -‬وبمعنی رخ وروی وچهره باشد ‪-‬‬
26372:           ‫بپرهیزی از درد سر وزگرالی»‬                  ‫اگرچهرهی را ت کومتر لوازی‬
27215: ‫باشد‪ ,‬وان کرمی است که چون بربدن چسبانند‬                          ‫گوبند باعتبار سرخی چهره ‪ ۰‬چه رنه اوسر خ‬
31501:                                       ‫«فس» و بمعتی جوان ساده‌چهره وبی موی وجمم آن سادکان ‪:‬‬
```


## [2026-09-14T02:04:18.100Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '7760,7800p' BQT_v2_pages.txt"
}
```


### [2026-09-14T02:04:18.157Z] TOOL RESULT

```
 ‫‪ - ۱‬پهلوی ‪( ۲1116‬تخم) «یبر گے ‪« »64‬مسینا ‪ 7116 ۷: ۲۳۱:۲۰‬ط(بیمت‪,‬نژاد‪.‬منظر )‬
  ‫«مناس ‪ )۰۷۲:۲‬ازاوستا ‪( 2۳1101‬تخمه؛نژاد)«بارتولمه ‪)۷۸۵‬پارسی باستان ‪( 871101-‬نوع‪.‬اصل)‬
  ‫‪« _ ۲‬خمانی ‪ ...‬ملقب بشهر آزاد»‬                       ‫اسشق و هوبدمان ‪۳‬‬             ‫ور که‬        ‫ص‪۰۷۱‬‬       ‫«اسفا ‪۱:۲‬‬

  ‫«طبری حص‪٠٤۲‬‏ دریپلوی )‪)011]- 262‬دیوستی‪.‬بندهش ‪»۲۲۱‬شاهنامه«چهرزاد» «فهرست ولف»‪:‬‬
           ‫و‪۲٩‬؟‪.‬‏‬    ‫التواریخ والقصص ‪» 6‬ور ‪۳ :‬‬             ‫«یادشاهی همای چهر آزاد سی سال بود“ «محمل‬

  ‫[ك ‪:‬گاه ]‪ .‬توایی از موسیقی ابرانی » معرب آن‬
                                            ‫چ‪#‬هارگاه _ بفتح اول و دوم ر‬
                                                                           ‫‪.‬‬        ‫«حهار گاء» «دزی ج ص‪۲۲‬‬
  ‫کن هفتم ( لپجهٌ مر کزی )‪ .‬بهلوی‬                     ‫چهار شنبه ‪ -‬بفتح اول و دوم و پنجم‬
  ‫‪« ۲2018۰‬منای ‪ , ۰۷۲۰‬کیلکر ‪7286 200۳۲8115‬؛ روز پنجم از ابام‌هفتةٌ ملمانان‪.‬‬                                       ‫‪۸‬‬

  ‫* چهارم ‪ -‬بفتح اول وضم راء از ‪ :‬چپار ‪ +‬ام ( سوند عدد )‪ .‬پهلوی ‪011۲0۵20‬‬
     ‫ما ‪۲٩ : ۱۳۱‬‏ با ‪« 00۵6۲20120‬مدای ‪ ۰۷۲‬؛ عدد ترتیبی برای چهار ‪ ,‬درمرئبةٌ چهار ‪.‬‬
  ‫‪ #‬چهل ‪ -‬بکراول‪ ,‬دوم بهلوی ‪« 100‬مسینا ‪ ۰ ۲۳۱‬دارسی‌باستان‪ ,‬ازلا‪820 )70‬‬
  ‫پارسی بامتان_ ‪ , 1۵00۳۷5۳0120‬اوستا ‪.259۳2۷۷0126,]-‬هندی‌باستانی ]‪ « 891۲2۷020‬اسفا ‪: ۱‬‬
                                 ‫‪۲‬ص ‪۷۵,۳٩۲‬‏ مضفف آن‌چل ؛ عدد اصلی چپار برابر ده ؛سی‌بعلاوه ده ‪.‬‬
                                                                                                     ‫‪7-۷‬‬


  ‫چهر ه شدن ‪ -‬کناءه ابزرخاستن‬                                  ‫ووی‬
                                                                 ‫چهر ه ‪ -‬یکسر اول » صورت ر‬
                       ‫بمنازعت باشد ‪3.‬‬                          ‫ضم اول ير سادة امرد‬    ‫و‬   ‫‪-‬‬   ‫‪۱‬‬     ‫باشد‬   ‫اده‌ی‬


                                                             ‫؛ویند باين معنی‬
                                                                           ‫ونو کر وملازم راتیز گفته‌اند گ‬
 ‫جهیل ‪ = ۴‬بروزن‌شهید‪ .‬ماضی‌چکیدن‬
                                                                                               ‫«ندی است ؟‪.‬‬
                                ‫چکید ‪.‬‬         ‫باشد «عنی‬
‫چهیدن ‪ ۰‬بر وزن و معنی چکیدن‬                                  ‫چهره پدرار ‪ -‬سور و مورتگر را‬
                                                   ‫باشد ‪.‬‬                                              ‫‪.‬‬    ‫فل‬




                                              ‫لبان ليست و دو یم (‪)۱‬‬


              ‫لغت و کنات‬            ‫دده‬           ‫در‬   ‫درجم فارسی با بای حطی فطل‬
```


## [2026-09-14T02:04:35.306Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\np='/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt'\nt=open(p,encoding='utf-8',errors='replace').read()\nprint('formfeeds',t.count('\\f'))\nlines=t.split('\\n')\nidx=sum(len(l)+1 for l in lines[:7760])\nprint('leaf at line 7760 =', t[:idx].count('\\f'))\nEOF"
}
```


### [2026-09-14T02:04:36.486Z] TOOL RESULT

```
formfeeds 683
leaf at line 7760 = 132
```


## [2026-09-14T02:04:44.803Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"شوخ\" MON_part1.txt MON_part2.txt | head -20"
}
```


### [2026-09-14T02:04:44.872Z] TOOL RESULT

```
MON_part2.txt:3999:وت شوخ 
MON_part2.txt:5554:| نگ سار شوخی کند و بو سته لطمفه 
MON_part2.txt:8160:شوخ بودن» خوش طبع بودن. (امص.) 
MON_part2.txt:18823:ظالم, شوخ. زنبور کافر: نوعی زنبور سرخ. 
MON_part2.txt:20145:شوخ و بازیگر. کبک کر: (جان.) دراج. 
MON_part2.txt:21933:چرکث» ریم اندام» شوخ. 
MON_part2.txt:37976:لا غ: (.) هزل» ظرافت» شوخی. خوش 
MON_part2.txt:39503:باریک و نیکو نکته. بذله. شوخی. نکتة 
MON_part2.txt:40884:لور: ۱۲ (۱.) شوخی» بی‌حیایی. 
MON_part2.txt:41502:لیم: ((ص.) شوخ و ظریف و بذله گو. 
MON_part2.txt:51461:(امص.) مزاح» شوخی. 
MON_part2.txt:54825:مراح: ۱۳۱ ۳06 (مص‌ل.) شوخی کردن؛ 
MON_part2.txt:54826:خوش طبعی کردن. (امص.) شوخی؛ خوش 
MON_part2.txt:54842:شوخی کردن. (امسص.) شوخی؛ خوش 
MON_part2.txt:56606:دهند. کسی که بسیار شوخی و هزل گوید و 
MON_part2.txt:59461:لطیفه گوی. (ص.) شوخ. 
MON_part2.txt:59463:(مص‌ل.) شوخی کردن با کسی مزاح کر دن. 
MON_part2.txt:61895:(معریل.) شوخی کردن با کنی؛ مزاح کردن. 
MON_part2.txt:61896:خوش صحبتی کردن. (امص.) شوخی» 
MON_part2.txt:64340:(مصل.) بازی کردن با هم. شوخی کردن
```


## [2026-09-14T02:04:45.866Z] TOOL CALL #67: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://abadis.ir/fatofa/%D8%B4%D9%88%D8%AE/\" --note \"page 451, Mo'in on شوخ\" 2>&1 | tail -1"
}
```


### [2026-09-14T02:04:48.632Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/25f4f2996606e600.txt
```


## [2026-09-14T02:04:51.431Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '8140,8175p' MON_part2.txt; echo \"=== abadis\"; grep -n -m3 -A20 \"فرهنگ معین\" /home/sfmqrb/git/rishe/data/verification/sources/web/25f4f2996606e600.txt | head -40"
}
```


### [2026-09-14T02:04:51.524Z] TOOL RESULT

```
در بين پرده کاملاً نمایان است و به چنگال 
ختم می‌شود. انگشتان و پاهایش نیز به وسیله 
پرده‌ای بهم مربوطند ولی هیچ وقت برای 
حرکت حیوان بکار نمی‌روند و فقط در 
امتداد بدن قرار گرفته و تشکیل باه عصبی 
سنا را می‌دهند. این جانور در تمام مناطق 
قطبی دریاها فراوان است. فکك فاقد گوش 
خارجی است و بدین جهت تمیز آن از 
دیکر شستانداران در بای شها آثبت::شکار 
زیاد و بی‌تناسب این حیوان به منظور استفاده 
از گوشت و پوست و چربی آن امروزه به 
مقدار زیادی نسل وی را رو به انقراض برده 
اشتته: کته بای ار ایت»: نو و در درسای 
مازندران وجود دارد و بنام فك خزر 
موسوم است. سگك دریایی؛ گربةٌ دریایی؛ 
شیر دریایی. 

فی: :۵) (۱.) (گیا.) در آمل و مازندران به 
گونه‌های مختلف ید اطلاق می‌شود. 
فکاهت: :۱۵۲7۲ (ع. فکاهة] (مصل.) 
شوخ بودن» خوش طبع بودن. (امص.) 
خوش طبعی» مزاح. 

فکر: ۲*] (ع.] (.) اندیشه+ ج. افکار. به فکر 
رفتن: متفکر شدن, انديشه کردن. 

۹ )2۳۹ [ع. . فکر 5 (.) اندیشه؛ ج. 


تم تاد (۱.) ی کار دودکش 


فررهنک فارسی معین 


فک 
=== abadis
42: فرهنگ معین
43-
44- (اِ ) چرک ، ریم .
45- (ص . ) ۱ - گستاخ ، بی حیا. ۲ - زنده دل ، خوشحال . ۳ - دزد. ۴ - خوشگل . 
46-
47- فرهنگ عمید
48-
49- ۱. شاد، خوشحال، زنده دل.
50-۲. بذله گو، اهل مزاح.
51-۳. [قدیمی] خوشگل.
52-۴. [قدیمی] گستاخ.
53-* شوخ وشنگ: [قدیمی] خوشگل و ظریف.
54-۱. چرک بدن.
55-۲. چرک لباس: اگر شوخ بر جامهٴ من بُوَد / چه باشد دلم از طمع هست پاک (خسروی: شاعران بی دیوان: ۱۷۸ ). 
56-
57- واژه نامه بختیاریکا
58-
59- از گونه ی گیاهان ییلاقی با دانه های قرمز رنگ
60-
61- مترادف ها
62-
--
154: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
155-
156- لینک ها 
157-
158- حقوق این سامانه وابسته به دیکشنری آبادیس می باشد. 
159-
160- استفاده از نوشتارهای این دیکشنری، با ذکر منبع، آزاد است. 
161-
162- © 2006-2026 abadis.ir
```


## [2026-09-14T02:05:02.541Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Schmutz'\" HRN.txt | head -20; echo \"=== HUB\"; grep -n -i \"sux\\|šūx\\|suh 'Schmutz\" HUB.txt | head -10"
}
```


### [2026-09-14T02:05:02.607Z] TOOL RESULT

```
794:lat. Inf um; air. loth 'Schmutz'; lit. lutyna-Sy lutgn^
=== HUB
1206:p. 103) ist nach np. und paz. pasux (Shk. 263, Min.
4398:zd. nava^); ausl. -ux aus -axv: pasux 'Antwort* = phi.
4400:= phi. fairaxv; suxtin ^= suxan *Wort', paz. saxun aus
4670:gift*, paz. pad(a)zah(a)r Shk. 261 ; np. paz. pasux *Antwort*,
6767:paz. pasux 'Antwbrt' aus ^pdtsaxv (neben phi. pasaxo aus
6845:II, 297 und -pan schiitzend'; np. paz. pasux 'Antwort' aus
7465:sal Mahr = zd. sareda-; surx Voth* = zd. suxra-,
7466:ap. &uxra'; suxun^ suxan *Wort* aus iran. "^saxvan- = ap.
7471:afsan *Wetzstein , afsar 'Krone', pdsux *Antwort\ pasand
7770:d. i. dozaxv, zd. daoSanuha-, arm. dzoxK (oben p. 64); suxun,
```


## [2026-09-14T02:05:13.844Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && grep -n \"شوخ\" ARY_pages.txt | head -10; echo \"=== chehre/saye\"; grep -n \"^.*چهره\\|سایه\" ARY_pages.txt | head -10"
}
```


### [2026-09-14T02:05:13.952Z] TOOL RESULT

```
=== chehre/saye
10039:سانسکریت: نور کم سایه,
```


## [2026-09-14T02:05:19.536Z] TOOL CALL #71: Bash

```json
{
 "command": "pdftoppm -f 451 -l 451 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg451 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg451.png"
}
```


### [2026-09-14T02:05:21.324Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 82815 Sep 13 22:05 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg451.png
```


## [2026-09-14T02:05:23.374Z] TOOL CALL #72: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg451.png"
}
```


### [2026-09-14T02:05:23.963Z] TOOL RESULT

```

```


## [2026-09-14T02:05:23.956Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-14T02:05:44.623Z] TOOL CALL #73: Bash

```json
{
 "command": "sed -n '1,200p' tools/verify_check.py"
}
```


### [2026-09-14T02:05:44.665Z] TOOL RESULT

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


## [2026-09-14T02:05:51.596Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LEW scaena\"; grep -n \"scaena\\|scena,\" LEW_1910.txt | head -5; echo \"=== LEW scaevus\"; grep -n \"scaevus\" LEW_1910.txt LAT.txt | head -5; echo \"=== SKT\"; grep -n \"^scene\\|scene (1)\\|scene, a stage\" SKT.txt | head -5; grep -n \"shine, to\" SKT.txt | head -3"
}
```


### [2026-09-14T02:05:51.705Z] TOOL RESULT

```
=== LEW scaena
=== LEW scaevus
LAT.txt:40230:scaevus, etc.
=== SKT
```


## [2026-09-14T02:05:53.979Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '40200,40245p' LAT.txt; echo \"=== LAT scaena\"; grep -n \"scaena\" LAT.txt | head -5"
}
```


### [2026-09-14T02:05:54.088Z] TOOL RESULT

```
(XUTI C , IXUTTOC. - V. «U.
mQtuus; v. nuto.
myrtus: v. murtus.
myxa, -ae f.: 1* sorte de prunier (Plin. 13, 5 t), nixa-,-a* bec de
lanpe, lunignon. Enprunt (Martia!) au gr. \ivtp., i at ini se, et pass 4
aous des fomes alt^r^es dans lea 1 . ronanes (fr , niche, ete. ). V. M.L.
5B04, et O. Bloch, Dict. 4 tym., s.u.nablium, -I (nablum, naulium) a.: sorte de harpe, d'origine phd-
nicienne; hebr. nSbel, passe <?galenent en gr. vaj3Aa(c). Emprunt atteste
a partir d’Ovide. *
Derives: nabli 5 ,-Snis n.: ya\Tr\Z } nablizd: yaAAw (Gloss.).
nacca, -ae n.: -ae appellantur uulgo fullones... quidam aiunt
quod omnia fere opera ex lana voutr) dicuntur a Graecis, P.F.,i 66 , 7 .
Atteste dans Apulae, comme le d 4 riv 4 naccinus.
Cf. vaxo{ "toison", vacrato "fouler", v<xxt;i|S. Mot ynlgaire, avec
g^min^e expressive; peut-etre osco-grec, ou enpmnte par 1'interme-
diaire de 1’etrusque, comme un certain nombre de substantifs en -a.
Le mot courant de la 1 . ferite est fullS. Senble sans rapport avec
Matta, cognomen des Pinarii, et qu’on trouve dans Hor., 5 « 1 , 6 ,i «4 (ou
Porphyrion note Matta pro uulgari et sordido homine posuit) et Perse,
3,31. A moins que tous deux ne soient des d^formations, dlorigine
differente, de vaxTqC (~ta.z).
naenia: v. nSnia.
naeuus, -I m.: tache sur le corps> envie, verrue. Une forme rd-
duite neus est attest^e CGL IV 134,6; les formes romanes remontent
a naeuus et neus, cf.M.L.50o7.
Derives: naeuius : qni a des taches; naeuolus, naeuulus (epoq.imp.).
Maeuus represente un ancien gnaiuos , conserve encore comme praenomen
(abrege en Gn.), Gnaiuos, Gnaeus, tandis que Maeuius a fourni le nom
d»une gSns, d*oii Maeuidnus ; cf.osq .Gnaivs, Cnaivlles.
Etymologie inconnue; cf., pour la diphtongue et la structure, laeuus,
scaevus, etc.
nam: conjonction explicative, correspondant pour le sens'comme
pour 1'emploi au gr.yapi toutefois, A 1'encontre de ce dernier, se
place le premier mot de la phrase. Les exemples de nam place le second
mot sont poetiques (Catulle 64,301; Hor., Vg., e.g. Ae.3,379, prohibent
nam cetera Parcae | scire), et suspects d^influence grecque.
i° Mam est, comme enim, une particule de sens affirmatif: "en ve¬
rite", cf. Pl., Men.S37, ubi illae armillae sunt quas una dedi'? - Mumquam
dedisti. - Mam pol hoc unum dedi j ,et Mi.1335. Ce sens est ancien mais
rare. Le plus souvent nam sert A introduire un nouveau developpement
dans un. raisonnement, une confirmation speciale d^une affirmation
generale: Cic.Diu.3,1,3, Magnus locus philosophiaeque proprius a Platone,
Aristotele, Theophrasto, totaque Peripateticorum familia tractatus
uberrime. Mam quid ego de Consolatione dicam?, oA nam correspond A
peu prfes A notre "A ce propos". En particulier, nam introduit une
explication, un compiement, une justification, des exemples A 1 'appui
=== LAT scaena
14315:un intera^diaire etrusque, cf. SSturnus, Saeturnus, et scaena, paelex),
21043:gustam adhibeant | fauentiam, ore obscaena dicta segregent , ob le pobte
23399:actum scaenarum composita, pifece de th^atre on fable; 3° fabula coaae
38822:proprement le "souffleur": -es dicuntur et qui in scaena monent histriones,
42843:obscaenus rappelle celle de scSna, scaena qui semble supposer un
```


## [2026-09-14T02:05:57.011Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '42835,42860p' LAT.txt; echo \"=== scaeuus entry\"; grep -n \"scaeuus\" LAT.txt | head -5"
}
```


### [2026-09-14T02:05:57.103Z] TOOL RESULT

```
augure" ( obscgnae auSs, canSs; obscenum ostentum, etc.)j par suite
dans la 1. courante "d^aapect laid ou affreux; qu 1 on doit Aviter ou
cacher; obscone"; obscSna n.pl. = to. cuSokou Ancien, uauel, classique.
DArivA: obscSnitas (class.).
Le sena technique semble le pli^s ancien, cf. Fest.318,16 , t, cum
apud antiquos omnis fere obscena dicta sint quae mali ominis habe¬
bantur, Mais 1 'Atymologie du mot est inconnue; il n*y a rien k tirer
de la glose de Festus 304,34. Peut-fctre empruntA: la variation obscSnus,
obscaenus rappelle celle de scSna, scaena qui semble supposer un
intermAdiaire Atrusque entre le modble grec et 1 'emprunt latin. Le
rapport avec caenum ne se laisse. pas justifier.
obscurus, -a, -um: obscur (sens physique et moral). Correspond k
gr. OXOT8I.VOC1 s'o]>pose k clSrus, UsitA de tout temps; p an roman (sauf
roumain). M.L.C030.
DArivAs et composAs: obscGrit&s, M.L.Coiya; obscuro,-as; -atio;
obscurefacio (Non. ), inobscurabilis (Tert., cf .ocxotiotoC Greg.Nyss.);
obscuri-dicus,-loquium, tous deux rares et poAtiques; obscuroluna
(= OXOTOJAT^VT]), Ital.
La graphie par b montre que la langue coupait ob-scurus , bien
que le mot ne se laisse pas dhalyser en latin; cf. le 6, de obsSnium.obturo
- Ooy -
De 1 'AlAment - scUrus , on rapproche skr. skauti "il couvre", skutdh
"couvert" et v.isl .skuggi, v.h.a .scvwo "ombre", v.h.a.scur et scura
"grange". Rapprochements plus lolntains: lit. skura, "peau, Acorce"
et gr. oxuxoC "peau travaillAe, cuir", et scutum? La racine n'est
paa dissyllabique; l'C de obscurus est de ces u qui existaient pres
=== scaeuus entry
1649:exprimant nne infirmit6, caecus, scaeuus, taeter, nn nalaiae, taedet,
31983:suffixe et mSme diphtongue a vocalisme "populaire" a que dans scaeuus.
54873:designant un dEfaut: aeger, laeuus, scaeuus, caecus, claudus, ualgus,
54878:ont un correspondant, ce qui est le cas de laeuus, scaeuus, caecus,
55705:scaeuus, -a, -um: gauche, qui est k gauche ou qui vient degau-
```


## [2026-09-14T02:06:00.611Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '55705,55740p' LAT.txt; echo \"=== scaena entry\"; grep -n \"^sc[ae]na, -ae\\|scSna, -ae\\|scaena, -ae\" LAT.txt | head"
}
```


### [2026-09-14T02:06:00.696Z] TOOL RESULT

```
scaeuus, -a, -um: gauche, qui est k gauche ou qui vient degau-
che. Usite surtout dans la langue augurale ou avec des sens figures:
subst.s caeua,-ae f."presage qui vient a gauche"; Scaeua , cognomen,
"gaucher". Comme laeuus , a le sens de "d'heureux augure, favorable",
cf. 1 'emploi de bona scaeua "bon presage" et obscaeudre dans Plaute
St.461,673 {y. strena), Ps. 1138, et le tdmoignage de Varr., L.L.7,97, pue-
ris turpicula res in collo quaedam suspenditur, ne quid obsit, bonae
scaeuae causa scaeuola appellatur. Ea dicta ab scaeua, i.e. sinistra,
quod quae sinistra sunt bona auspicia existimantur. D'autre part,
comme sinister , 1'adj. scaeuus, peut-etre d’aprbs le grec cr>coii»6c, a
pris (du reste rarement) le sens de "gauche, maladroit" et aussi
de "defavorable, sinistre" (surtout dans Apulee), cf. P.F.443,8: scaeua
res dicitur mala, quasi sinistra: axcuov enim Graece sinistrum dicitur-,
mais scaeua avait conservi? le sens de "presage" (indiff4rent, cf.
Fest.433,36, scaeuam uolgus quidem et in bona et in mala re uocat,
cum aiunt bonam et malam).- Ancien et repris par les archalsants.
Non roman. Outre scaeuola, explique par Varron, loc.cit., et usite1055
sc&lpS
comme cognomen, et Scaeuinus, on rencontre 1 1 'epoque imperiale
scaeuitds ( Geli., Amm., Apul. ) fait sur le module de gr. oxai, ott]£ .
Les noms pour "gauche" sont divers (par contraste avec celui de
"droite"; v. aussi sinister oppose a dexter). Le latin, qui a laeuus
en face de XauoC, a de m§me scaeuus en face de OXOUOS; formation
parallele, avec a radical. De scaeuus, cotaioC, on rapproche lit.
kaire "main gauche". Iri. ciotan "la gauche" et gall. chuith "gauche"
ne concordent pas; a en juger par scando et les cas analogues, le
vocalisme o est une variante expressive et populaire (-v.saeuus) .
Du cote oriental, il y a des mots analogues: skr. savydh et v.sl.sif/t
"gauche"; sl. suji indique un ancien *seuyo~, avec vocalisme e.
scala, —ae f.?: calices et calathi et scalae poculorum genera,
ante ex ligno facta, inde et uocata: Graeci enim lignum xaXa uocauerunt,
Isid.20,5,5.
Mot germanique: all .Schale, etc. V. Sofer, p.154 et s.
■ scala: v. scand5.
scalmus, -I m.: dane ou tolet, cheville pour 1 'aviron. Empr.
au gr. 05 cccXp,oC (d 4 ja dans Cic.), pass 4 dans les 1 . romanes, M.L.7C40.
=== scaena entry
```


## [2026-09-14T02:06:06.692Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"scSna\\|sc&na\" LAT.txt | head -10"
}
```


### [2026-09-14T02:06:06.754Z] TOOL RESULT

```
42837:cacher; obscone"; obscSna n.pl. = to. cuSokou Ancien, uauel, classique.
42843:obscaenus rappelle celle de scSna, scaena qui semble supposer un
57962:sescSnarius. Pris quelquefois pour designer an grand noabre indA-
```


## [2026-09-14T02:06:13.607Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"chāyā\\|chayd\\|chāyā́\\|skia.*shadow\\|Skt. chāyā\" SYN.txt | head -8; echo \"=== SYN face\"; grep -n \"15\\.4[0-9]\\|'FACE'\" SYN.txt | head -5"
}
```


### [2026-09-14T02:06:13.694Z] TOOL RESULT

```
=== SYN face
5893:Most of the words for ‘ear’ belong to an inherited group. ‘These and the others, so far as their origin is clear, are related to words for ‘perceive, hear’ (15.11, 15.41),
5902:Br. skouarn, Corn. scovarn, W. ysgy- farn (obs.), etym. dub., but perh., fr. a *skeu- beside IE *keu- in Grk. xotw ‘per- ceive, hear’, Lat. cavére ‘beware’, Goth. hausjan ‘hear’, OF scéawian ‘look at’, etc. (15.41, 15.52). Henry 243. Win- disch ap. Ernault, Dict. étym. 377. Less probably Pedersen 2.53.
17557:2. Grk. épxouat, etym. dub. Boisacq 287 with refs. Perh. fr. an extension of IE *er- in Grk. dpvine ‘rouse’, Skt. rnoti ‘moves’ (10.11); or more closely : dpxéo- pac ‘jump, dance’. Persson (cf. Boi- sacq). McKenzie, Cl. Q. 15.44.
17664:Ir. do-sennim (e.g. 3pl. du-m-sennat, etc.), etym. dub., perh. as orig. ‘start, frighten (game, etc.) by a noise’ : Skt. svan- ‘sound’, Lat. sondre, etc. (15.44). Pedersen 2.625.
18816:Grk, aipéw ‘seize, take, catch, etc.’ (much less common than AauBavw for take’), etym. dub. Walde-P. 2.498. McKenzie, Cl. Quart. 15.46f. Aeol. typ: aypa ‘the hunt’, etc. Walde-P. I36f, Aor. ety prob. : caus. Goth. saljan ‘offer, OF sellan ‘give, sell’, etc.
```


## [2026-09-14T02:06:17.138Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"shadow\" SYN.txt | head -10"
}
```


### [2026-09-14T02:06:17.189Z] TOOL RESULT

```
1859:1.63 SHADE Grk.  oxed Goth. skadus Lith.  Se3élis, pavesis, NG oKtd, HoKLos ON skuggt paunksne Lat. umbra Dan. skygge Lett. pavénis, ena, patna It. ombra Sw. skugga ChSl.  sént, Stént Fr. ombre OE scead, sceadu, scii(w)a SCr. — sjena, hladovina Sp. sombra ME shade, shadow Boh. — stin Rum. umbré NE shade (shadow) Pol. cient Ir. scath, foscad Du. schaduw Russ. ten’ (sen’) Nir. scath OHG - scato, sciiwo, sct Skt. chaya- W. cysgod MHG §schate Av. ‘*saya- Br. skeud NHG - schatten
1860:Most of the words for ‘shade’ are used also, without differentiation, for the image cast, the ‘shadow’. The figura- tive use for ‘disembodied spirit’ is also widespread from Homer on.
1861:1. Grk. xa, ChSl. séni, SCr. sjena, Russ. sen’ (Boh. siti, Pol. sien, Russ. seni ‘entrance room’, etc., as room without light), Skt. chaya-, Av. *saya- (a-saya- ‘without shadow’), NPers. saya-, Alb. hé, fr. IE *skai-, *ski-, prob. the same root as in Goth. skeinan, OF scinan, Ch§l. sijatt ‘shine’ (15.56). Connection through a notion of ‘faint light’ (as in NE shimmer, NHG schimmer) or ‘re- flection’. Cf. OF scima ‘shadow, gloom’ beside scima ‘light, brightness’. Walde-
1864:3. Ir., NIr. scath (also fo-scad, but NI. foscadh chiefly ‘shelter’), W. cysgod (i.e. cy-sgod), Br. skeud, Goth. skadus, OE scead, sceadu, ME, NE shade, shadow (latter now mostly for the image cast), Du. schaduw, OHG scato, MAG schate,
11441:Words for ‘mirror’ are mostly from verbs for ‘look’, with a few from words for ‘shadow’ or other sources. The common use of the word for the mate- rial ‘glass’ in the sense of ‘mirror’ seems to be peculiar to English.
11446:3. Ir. scdthan : scath ‘shade, shadow’ (1.63). Cf. Goth. skuggwa, etc. (be- low, 4).
11450:4. Goth. skuggwa, ON skuggsja, OHG scticar : ON skuggi, OE scia, ete. ‘shade, shadow�� (1.63). Falk-Torp 1045. Feist 435.
15821:Br. skeudenn ‘image, statue’ (Er- nault), deriv. of skeud ‘shadow’ (1.63).
25526:Tn early Greece there was no general term to designate the different devices for timekeeping. The earliest was, of course, the sundial, the zédos and yve- pov, the concave dial and the pointer, also called later cxwoPipas, oKtOBnpov ‘shadow-catcher’. The usual name
25565:chaya- ‘shadow’ and ambu- ‘water’ with
```


## [2026-09-14T02:06:29.715Z] TOOL CALL #81: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://abadis.ir/fatofa/%D8%B3%D9%86%D8%A7%D8%B1%DB%8C%D9%88/\" --note \"page 451, Mo'in on سناریو (French tag)\" >/dev/null 2>&1; grep -n -m1 -A6 \"فرهنگ معین\" /home/sfmqrb/git/rishe/data/verification/sources/web/*.txt 2>/dev/null | grep -A6 \"سناریو\" | head -5; python3 -c \"\nimport hashlib;print(hashlib.sha1('https://abadis.ir/fatofa/%D8%B3%D9%86%D8%A7%D8%B1%DB%8C%D9%88/'.encode()).hexdigest()[:16])\""
}
```


## [2026-09-14T02:06:30.777Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"cihr\\|sayak\\|s'yk\" NYB_vol2_glossary.txt | head -10"
}
```


### [2026-09-14T02:06:32.657Z] TOOL RESULT

```
44a7302c7a89e625
```


### [2026-09-14T02:06:32.703Z] TOOL RESULT

```
570:äp-eihrak [’p'-cyhlk'] containing the seed of the waters 87°; àp- u damik- u urvar- u gospand-cihrak containing the seed of the waters, the earth, the plants and the cattle 8711. — Av. (103 sq.) af$-cidra-; v. cihr and -cihrak.
1129:eihr [cyhl; inscr. ctly] seed, origin HajB 2-4. SPrs: 5.7.13. P1:2.4; essence, innate quality 55°. — Av. (587) ?c?0ra-, OP *cica- in n. pr. Cicantaxma (Trosapéevng < * Cica-farnah-) ; MPrs cyhr essence, shape, origin, face = MPrth cyhrg; cyhr’wynd ‘beautiful’, Sogd. 35.37, cf hu-cihr; Paz. cihar, Skr. v. rüpa, rüpävayava (SGV); NP cihr; v. also Shr.
1130:-cihrak [cyhlk'] = cihr used as the last element of an adj. compound, v. dp-~, damik-~, gospand-—, mart6m-~,urvar-~. Cihrāzātān [cyhl’c’t’n'] patron. 116". — From n. pr. C?hrāzāt, ci āzāt.
1172:dahyupat [dhywpt'] ruler, king: Fran ~ of Vistasp-sah 1917. 6017-2. 1118; of Manušcihr 47°; of the Great King killed by Alexander 107’; Vadagān (g. v.) ~ of Dahäk 902; — pl. cas. obl. ~-dn in a general sense 110?!. 1192”; — subordinated to the Great King: xtatäi u ~ 1274, 7223; xvatčiydn u an [ZK] ~-dn 727); zuatai u ~u sardar u dastavar % den 1081-?, — Av. (681 sq.) datyhu-pati- < *dahyu-pati- ‘lord of the country’; MPrs dhybyd (A-H I); Paz. dahevad, Skr. v. rājan (Mx), dehavad, Skr. v. grāmapati, svamin (SGV). al-Biru- ni, Chronologie 22077, transliterates dahü- fadiya = dahyupatčh.
1177:damik-cihrak [dmyk cyhlk'] containing the seed (the constituent element) of the Earth 879. — V. cihr- and cihrak and cf äp-cihrak.
1699:gospand-cihrak [~-cyhlk'] containing the seed of cattle 879, — V. cihr, cihrak: cf ap-cihrak, gö-cihr.
1754:expressed (nominal sentence as in the Semitic languages): man Sähpuhr hom 154; tē ke he? 737; to rād ke Dugdav he 4721. en rētak ke hast? who is this boy? 1617; Artaxsér ... nē pat giyāk hast 6?" sq.; kë zan-& hac õi hucihrtar nest ‘qua pulchrior non est mulier', who is the most beautiful of all women 259-19; ēzšān amüh hem ke ... we are of those who 5723-24, šmāh ke xtēn het 6111; sagr hend 86%, — 3. in the 3d p., together with a subst. virtually in dat., or with a pron. in cas. obl., it expresses ‘to possess’ xdnak i-t hast the house that belongs to thee 5325-26; fradandan i-5 hast the chil- dren he has 142; with ràd as in NP: Papak rüd pus-é hast 3?. — 4. Together with verbal or other nouns it forms periphrastic verbal expressions, e. g. han- dešitar vicītār hom 125; frēftār hah 3419; matür hom 46’; kartar hom 101?’; brihenäk hend 7777; ke (cas. obl.) vitīrišn nest which is incorruptible 66°; tö hän-ic äkäh he this thou knowest 399; hayyär hend they help 106%; -š hayyaréh hénd they help him 1001-12; pat kamēstārēh + spihr hénd they offer resistance to the. Sphere 8721; ké (cas. obl.) Mihr u Mah pat pust hah which M. and M. protect 317-8, ete. — 5. auxiliary vb. forming compound tenses: būt hom, būt hend I was, they were, eto., v. Grammar; notice: HWH-nd, regularly hend, must stand for the subju. händ 14? (fut.). 335 (cond.). — 6. Wrong use of the ideogr. HWH-: a) HWH-wm for the encl. pron. lst p. sg., added to the pret. pass. in order to emphasize the agent-
1758:hae [MN ; hc 619] prep., with -c: MN-c = hac-ic; not with an encl. pron. (as to haciš, hacisan v.s. v. hactš); the original sense ‘accompanying, with’ (Skr sacā) is still transparent in ~ ... hämisi (g. v.) ‘together with’, but the meaning ‘from, of’ prevails since the OIr period. 1. Local: hàn yam ... hac dast i Artaxser 6 damik opast 92°; api-š hecak hac cah ul hixt 155; hakar hac asp bē nisinam 27?; hac star püdak tai mah pädak 93"; hac dar ētšān bagän namäc burt from the gate-way (i.e., halting at the entrance, from this place) I rendered adoration to His Majesty. P1:4; — figurative, with a great many vbs. and idioms, the sense of ‘from, of’ being more or less transparent. akahé- nitan, āšnūtan, pursitan, x"āstan, dast šustan hac ete., v. the individual ws.; — origin: ke cihr (Prth Shr) hac yazatān (Prth y’ztn) whose origin is from the gods, of divine origin HajB: 2.4 (HajA: 2.4). SPrs: 5-6 (yazdān) (SPrth: 5). P1: 2.4 (yazdàn) ; "Apasči... à hac Haran ŠPrs: 9; hac tohmak + Dārāt būt 18, etc. — 2. tem- poral: hac im róc from today onwards, henceforth 9"; hac im réc tdi 3 roc within three days 51%; hac rahikehv [lsykyhy] ever since my youth 1282-5; ete. — 3. after a v. n. it expresses the subj. of the act: patirak zanišn + hac ganäk menoi on the point of being slain by the Evil Spirit 46°-§; zanisn i devàn hac han i 0$ xvarrah the demons being slain by his divine splendour 461?; freftakeh + hac dēvān de- ception by-the demons 461; 4513-14; ete. —
1760:4. partitive: hac fradandan + han mart kasé anyone of the children of that man 25; hac šmāh xiönän ke hast ke ...? 25” ete.; fratom hac ax" i astomand 53%; xuastom hac z"arisnàn the most delicious of dishes 7413; ete. — 5. in comparison ‘than’: hac apārīk kanicakän āžarmīktar 422; Zarristan ke... zan-ē hac či hucihr- tar nest 259-19; hac tē veh 411; kū-š suk mas būt hac apdrik gāv 492°; more emphatically yuvattar (g. v.) hac hàn + huhömikän homtar 40°’. — 6. causative: hac hàn dušxvār sahist by this he was very much shocked 4?-?; hac hàn 1 devan sārēnišn 3774-25 : causal conj. : hac hàn cigon because 4511; hac han i with a nominal clause 48!. — 7. forming adverbs: hac pas, hac pes, hac be, hac apar (hacapar), hacadar; prepositions: pas hac, peš hac (= patiš hac 368), yuvat hac, bé hac; frame prepositions: hac. . . rād owing to 1525-26; hac .. . bérén 20%; hac . . . yuvatāk 76°. — Av. (1746 sqq.) hacé; OP haca; MPrth ^c, "Z; MPrs 'c, "z; Paz. ez (eži-ca); NP az.
2039:hu-cihr [hweyhl] beautiful, lovely, comp. —-tar 1815. 2510, 262, 289. 731.3, — MPrth Prs hweyhr ; Paz. hücihar; NP hujir, hužir ; v. cihr. Bailey, BSOS XI, 1943, 774 n. 1. hucihrčh beauty 558.
```


## [2026-09-14T02:07:20.661Z] TOOL CALL #83: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg451.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/451.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/451.png"
}
```


### [2026-09-14T02:07:20.743Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 82815 Sep 13 22:07 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/451.png
```


## [2026-09-14T02:07:30.167Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"### skene\"; grep -n -A4 \"^ Etymology$\" e2e6514385ae01ef.txt | head -20; echo \"### scaevus\"; grep -n -A4 \"^ Etymology$\" 45e793d08b03435f.txt | head -20; echo \"### senario\"; grep -n -m1 -A6 \"فرهنگ معین\" 44a7302c7a89e625.txt"
}
```


### [2026-09-14T02:07:31.331Z] TOOL RESULT

```
### skene
181: Etymology
182- [ edit ] 
183-
184- Usually said to be a derivative of Proto-Indo-European *(s)ḱeh₃- ( “ shade, shadow ” ) , originally referring to a light construction of cloth hung between tree branches to provide 
185-a shadow which could be used for shelter and other activities, [ 1 ] though the vocalism is difficult to explain as full grade *sḱeh₃- gives σκω- ( skō- ) and zero grade *sḱh₃- gives σκο- ( sko- ) .
--
349: Etymology
350- [ edit ] 
351-
352- From Ancient Greek σκηνή ( skēnḗ , “ theatre stage ” ) .
353-
### scaevus
149: Etymology
150- [ edit ] 
151-
152- From Proto-Italic *skaiwos , from Proto-Indo-European *skeh₂iwos . Cognates include Ancient Greek σκαιός ( skaiós , “ rude; brusque ” ) .
153-
### senario
23: فرهنگ معین
24-
25- (س ) [ ایتا. ] (اِ. ) فیلم نامه ، داستان مخصوص فیلم سینما. 
26-
27- فرهنگ عمید
28-
29- داستان یا شرح صحنه های یک فیلم که در آن بیشتر به طرح ریزی صحنه ها و مناظری که باید فیلم برداری شود و چگونگی حرکت دوربین ها و گرفتن تصویر از هنرپیشگان توجه می شود و کارگردان از روی آن فیلم را تهیّه می کند.
```


## [2026-09-14T02:15:15.140Z] TOOL CALL #85: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/page-451.json",
 "content": "{\n  \"pdf_page\": 451,\n  \"book_page\": 421,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-13\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Skai\",\n      \"verdict\": \"plausible\",\n      \"modern_form\": \"two distinct PIE roots: (a) *ḱey-/*kʷey-t- 'bright, conspicuous' (Pokorny (s)kai-(d-),(t-) 916-917) and (b) *sḱeh₂(i)- / *sḱeh₃- 'to glimmer faintly; shadow' (Pokorny sḱāi-, sḱəi-, sḱī- 917-918)\",\n      \"note\": \"Nourai's headword and gloss are copied verbatim from Pokorny p. 916-917, where the lemma '(s)kai-(d-), (t-)' is glossed exactly 'shining, bright' and whose material includes Skt. citrá- = Av. čiθra-. But the rest of the chart (čāyā/a-saya-/sāya, Gk. σκιά-σκηνή, Gmc. *skīnan) belongs to the NEXT Pokorny lemma, sḱāi- : sḱəi- : sḱī- 'gedämpft schimmern; Schatten' (pp. 917-918), which is why Nourai's single page reference POK:917 lands between the two. Pokorny himself cross-refers them ('compare kai-3 and sḱāi-'), and Watkins/AHD likewise keeps them apart ('skai-. Also kai-. Bright, shining. [Pok. (s)kāi- 916]' vs 'skeəi-. To gleam. [Pok. skāi- 917]'). Modern reconstruction separates them completely: the čiθra- family is *kʷi-tró- to *kʷey- 'bright, burning' (no s-mobile, plain/labiovelar), the shadow family is *sḱeh₂- (palatal, giving Skt. ch-, Av./OP s-/θ-). So the root box as printed is real and correctly glossed, but the tree under it conflates two roots — hence 'plausible' rather than 'confirmed'.\",\n      \"note_fa\": \"سرواژهٔ «Skai» با معنی «درخشان، روشن» دقیقاً همان مدخل (s)kai-(d-),(t-) در پوکورنی صص ۹۱۶–۹۱۷ است که در آن سنسکریت citrá- و اوستایی čiθra- آمده‌اند؛ اما شاخه‌های «سایه» و «خیمه/صحنه» و «درخشیدن» به مدخل بعدی پوکورنی، یعنی *sḱāi- : sḱəi- : sḱī- «کم‌سو درخشیدن؛ سایه» (صص ۹۱۷–۹۱۸) تعلق دارند. نورایی این دو ریشه را که در کتاب پوکورنی پهلوی هم افتاده‌اند یکی گرفته است، حال آنکه ریشه‌شناسی امروزی آنها را جدا می‌داند: خانوادهٔ «چهر» از *kʷey- «روشن، تابان» و خانوادهٔ «سایه» از *sḱeh₂- (با کام‌شدگی که در سنسکریت ch- و در ایرانی s-/θ- می‌دهد). پس جعبهٔ ریشه درست است ولی درخت زیر آن دو ریشه را در هم آمیخته؛ ادعای نورایی «با احتیاط پذیرفتنی» است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%DA%86%D9%87%D8%B1%D9%87\",\n        \"https://en.wiktionary.org/wiki/%D8%B3%D8%A7%DB%8C%D9%87\",\n        \"https://en.wiktionary.org/wiki/%CF%83%CE%BA%CE%B7%CE%BD%CE%AE\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:917\", \"status\": \"partial\", \"note\": \"POK_full.txt: p.916-917 carries 'Root/lemma: (s)k(h)ai-(d-),(t-) | Meaning: shining, bright | Material: Old Indic ketú-..., citrá- 'augenfällig, ... bright' = Avestan čiθra-' (Nourai's gloss verbatim); pp.917-918 carry a SEPARATE lemma 'sḱai-, sḱəi- : sḱī- | Meaning: to glimmer (of wet things); shadow | Material: Old Indic chāyā, Avestan a-saya-, np. sāya; gr. σκιά ... σκηνή, Doric σκανά 'tent, stage'; Gothic skeinan, OHG scīnan'. Page 917 itself also holds a third, unrelated lemma '(s)k(h)ai- to hit'. So POK:917 supports the material but not the merger of the two lemmas into one root.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. II 535 and 537\", \"stance\": \"supports\", \"note\": \"WLD_Bd2_pages.txt: 'skai- „gedämpft schimmern; Schatten (Abglanz)“ : sḱəi- : sḱī-. Ai. chāyā „Glanz, Schimmer, Schatten”, av. a-saya- „wer keinen Schatten wirft”, np. sāya „Schatten, Schutz”' (p.535) — Pokorny's source for the 917-918 lemma; the 'hell/bright' lemma sits separately at (s)qai(-t-,-d-) p.537ff.\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.vv. skai- and skeəi-\", \"stance\": \"partial\", \"note\": \"AHD_watkins1985.txt: 'skai-. Also kai-. Bright, shining. ... Suffixed form *ki-t-ro- in Sanskrit citra- ... [Pok. (s)kāi- 916.]' AND 'skeəi-. To gleam. 1. Suffixed form *ske(ə)i-no- in Germanic *skīnan ... 4. Suffixed zero-grade form *skiə-ā- in Greek skia, shadow. [Pok. skai- 917.]' — Watkins keeps the two roots apart, as Nourai does not.\"},\n        {\"src\": \"SYN\", \"where\": \"§1.63 SHADE\", \"stance\": \"supports\", \"note\": \"SYN.txt: 'Grk. σκιά, ... Skt. chāyā-, Av. *saya- (a-saya- \\\"without shadow\\\"), NPers. sāya-, Alb. hē, fr. IE *skāi-, *skī-, prob. the same root as in Goth. skeinan, OE scīnan, ChSl. sijati \\\"shine\\\". Connection through a notion of \\\"faint light\\\" ... or \\\"reflection\\\".'\"},\n        {\"src\": \"IEC\", \"where\": \"Mann, p.1146 region (leaf 635)\", \"stance\": \"silent\", \"note\": \"Mann's alphabetical run skabh- / skadro- / skaiuos / skal- has no 'skai- shine/shadow' lemma at this point; he treats the shadow root elsewhere under skiā-. No contribution to this root box.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"čitra; hu-čitra; manuš-čitra\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The three words are real Avestan lexemes, but the book prints them in a simplified Sanskrit-style transliteration: Avestan actually has čiθra- (with the interdental θ from Proto-Iranian *tr), hu-čiθra- and the personal name Manuš.čiθra-. Bartholomae AiW cols 587-588 in fact carries TWO homographs: ¹čiθra- adj. 'manifestus, offenbar, klar, sichtbar' / n. 'Gesicht, Anblick, Antlitz' (cognate 'ai. citrá-, np. čihr \\\"Gesicht\\\"') and ²čiθra- n. 'Same; Ursprung, Herkunft, Abstammung; Geschlecht, Stamm' (cognate 'np. čihr \\\"Ursprung\\\"'), with the explicit warning 'Die angenommene Gleichheit mit ¹čiθra- gilt mir für unwahrscheinlich'. Nourai's single gloss 'clarity, face, also race and origin' therefore fuses two words Bartholomae deliberately separates. hu-čiθra- (AiW 30193) is 'von guter Abstammung' and 'des Anblick gut ist, schön'; Manuš.čiθra- (AiW) is the name of a believer, Manuš- being a legendary hero, so 'of the seed/lineage of Manuš'. As to the root: Pokorny 916 does put Skt. citrá- = Av. čiθra- under (s)kai- 'bright, shining', and Watkins derives citra- from *ki-t-ro- under the same lemma, so the arrow is exactly what Nourai's sources say; but modern reconstruction (Wiktionary, following Mayrhofer/Cheung) has Proto-Indo-Iranian *čitrám < PIE *kʷi-tróm to *kʷey- 'bright, burning' — a plain/labiovelar root that cannot be the same as the s-mobile palatal *sḱeh₂(i)- of 'shadow' under which the rest of this chart hangs.\",\n          \"derivation_fa\": \"هر سه واژه اوستایی‌اند، اما کتاب آنها را به شیوهٔ سنسکریت نویسی ساده کرده است: صورت درست اوستایی čiθra-، hu-čiθra- و نام خاص Manuš.čiθra- است (θ اوستایی از *tr ایرانی باستان). بارتولمه در ستون‌های ۵۸۷–۵۸۸ فرهنگ ایرانی باستان دو واژهٔ هم‌نگاشت آورده است: ¹čiθra- «آشکار، روشن، دیدنی» و «چهره، رخ»، و ²čiθra- «تخم، اصل، نژاد، تبار»، و صریحاً می‌گوید یکی‌دانستن این دو را باورکردنی نمی‌داند؛ پس معنیِ یکجای نورایی («روشنی، چهره و نیز نژاد و اصل») دو واژه را در هم آمیخته است. دربارهٔ ریشه: پوکورنی (ص ۹۱۶) و واتکینز به‌راستی citrá-/čiθra- را زیر همین ریشهٔ «درخشان» آورده‌اند، ولی ریشه‌شناسی امروزی آن را از هندوایرانی آغازین *čitrám و هندواروپایی *kʷi-tróm از *kʷey- «تابان» می‌داند که با ریشهٔ «سایه» یکی نیست. خطای نگارشی چیترا/چیثرا از آنِ کتاب است، نه خوانش اسکن.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%DA%86%D9%87%D8%B1%D9%87\",\n            \"https://en.wiktionary.org/wiki/%D8%AE%D8%AC%DB%8C%D8%B1\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:916\", \"status\": \"supports\", \"note\": \"POK_full.txt, lemma '(s)k(h)ai-(d-),(t-)', Page(s): 916-917: 'Old Indic ... citra- \\\"augenfällig, lovely, superb, pretty, splendid, bright\\\", n. \\\"apparition\\\" = Avestan čiθra- \\\"augenfällig, clear, bright\\\"' — exactly Nourai's arrow.\"},\n            {\"ref\": \"POK:700\", \"status\": \"supports\", \"note\": \"POK_full.txt, lemma 'manu-s / monu-s | Meaning: man', Page(s): 700: 'Old Indic manu-, manuṣ- \\\"person, man\\\" ... Avestan in PN Manuš-čiθra-' — supports the manuš- element of manuš-čiθra-.\"},\n            {\"ref\": \"KNT:184\", \"status\": \"supports\", \"note\": \"KNT.txt leaf 208 (printed p.184, leaf 207 = p.183): 'çiça- sb. \\\"seed, lineage\\\": Av. čiθra-, NPers. čihr \\\"origin\\\" (§78, §148.III). In Ariyaçiça-, Çiça-taxma-.' Kent thus gives the Avestan form, its gloss and the New Persian outcome.\"},\n            {\"ref\": \"BQT:2047\", \"status\": \"supports\", \"note\": \"BQT_v4_pages.txt pdf page 130 (= printed 2047): entry منوچهر, '... او را مانوش چهر نام کرد و بمرور ایام و تغییر السنه منوچهر شد' — Borhan derives Manūčehr from Mānuš-čehr.\"},\n            {\"ref\": \"BQT:674\", \"status\": \"supports\", \"note\": \"BQT_v2_pages.txt (چهر/چهره run, scan leaf 132 ≈ printed 674): Mo'in's footnote reads 'پهلوی čihr (تخم) «نیبرگ ۶۴» ... از اوستا čiθra- (تخمه، نژاد) «بارتولمه ۵۸۷»، پارسی باستان çiça- (نوع، اصل)' — the Avestan etymon, spelled čiθra-.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"AiW cols 587-588, s.vv. ¹čiθra-, ²čiθra-, hu-čiθra-, manuš.čiθra-\", \"stance\": \"partial\", \"note\": \"BRT.txt: '¹čiθra- 1) Adj. \\\"manifestus, offenbar, klar, sichtbar, augenfällig\\\"; 2) n. \\\"Gesicht\\\" ... ai. citrá-, np. čihr \\\"Gesicht\\\"' and '²čiθra- (p. çiça-) n. 1) \\\"Same\\\" ... 2) \\\"Ursprung, Herkunft, Abstammung\\\" ... np. čihr \\\"Ursprung\\\". — Et.? Die angenommene Gleichheit mit ¹čiθra- gilt mir für unwahrscheinlich.'; 'hu-čiθra- Adj. 1) \\\"von guter Abstammung, Herkunft\\\" 2) \\\"des Anblick gut ist, schön\\\"'; 'manuš.čiθra- m. EN. eines Gläubigen ... Yt.13.131' beside 'manuš- m. EN. eines alten, vorsagenhaften Helden'. Supports the words but splits the meaning into two lexemes.\"},\n            {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II, glossary s.v. čihr and hu-čihr\", \"stance\": \"supports\", \"note\": \"NYB_vol2_glossary.txt: 'čihr [cyhl] seed, origin ...; essence, innate quality. — Av. (587) čiθra-, OP *çiça- in n.pr. Çiçantaxma ...; MPrs cyhr essence, shape, origin, face = MPrth cyhrg ... NP čihr' and 'hu-čihr [hwcyhl] beautiful, lovely ... MPrth Prs hwcyhr; Paz. hūčihar; NP hujīr, hužīr'.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. skai-\", \"stance\": \"supports\", \"note\": \"'skai-. Also kai-. Bright, shining. ... 2. Suffixed form *ki-t-ro- in Sanskrit citra-, variegated, many-colored: CHEETAH, CHINTZ. [Pok. (s)kāi- 916.]'\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"čehreh «چهره»; hožîr «هژیر»; Manǔčehr «منوچهر»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All three are the regular New Persian continuants of the Avestan/Old Iranian forms in node #1. (1) چهره čehre < Middle Persian čihr(ag) [cyhl(k')] 'form, shape, appearance, face; seed, origin, nature' (MacKenzie), from Old Persian *čiθraka- / Proto-Iranian *čiθráka-; Avestan θ regularly becomes MP h before r (čiθra > čihr), and the MP -ag suffix gives NP -a (čihrag > čehre); Wiktionary's chain is MP čihrag < OP *čiθrakah < PIr *čiθrákah < PII *čitrám. (2) هژیر hažīr/hužīr is NOT the direct Persian (south-western) reflex but the PARTHIAN one: Parthian hwcyhr /hužihr/ < *hu-čiθra- 'of good appearance, beautiful', with Parthian č > ž between vowels and loss of the second h; the south-western doublet is خجیر xujīr (MacKenzie explicitly glosses MP hu-čihr 'fair, beautiful (N xujīr)', Nyberg 'NP hujīr, hužīr'). Borhan-e Qate' p.2336 s.v. هژیر and Daqiqi's verse 'ای فخر آل اردشیر ... آثار و افعالت هژیر' (the very couplet the chart quotes) are the classical attestation. (3) منوچهر Manūčehr < MP Manūčihr < Av. Manuš.čiθra- 'of the seed/lineage of Manuš', with u from the unstressed š-cluster and popular reinterpretation as minu-čehr 'of paradisal face' already in Borhan.\",\n          \"derivation_fa\": \"هر سه واژه بازماندهٔ منظم صورت‌های ایرانی باستان‌اند. «چهره» از فارسی میانهٔ čihrag (نوشتهٔ cyhl(k')، در مکنزی «شکل، رخ، چهره؛ تخم، اصل، گوهر») و آن از ایرانی باستان *čiθraka-؛ θ اوستایی پیش از r در فارسی میانه به h بدل شده (čiθra > čihr) و پسوند -ag فارسی میانه در فارسی نو -ه شده است. «هژیر» بازماندهٔ پارتی است نه پارسی میانهٔ جنوب‌غربی: پارتی hwcyhr /hužihr/ از *hu-čiθra- «خوب‌چهر، زیبا»، با تبدیل č میان‌واکه‌ای به ž در پارتی؛ دوگانهٔ جنوب‌غربی آن «خجیر» است (مکنزی: hu-čihr «زیبا» = خجیر؛ نیبرگ: NP hujīr, hužīr). حاشیهٔ معین بر برهان قاطع (ص ۲۳۳۶) و بیت دقیقی «ای فخر آل اردشیر… آثار و افعالت هژیر» همین را تأیید می‌کند. «منوچهر» از اوستایی Manuš.čiθra- «از تخمهٔ منوش» است و ریشه‌شناسی عامیانهٔ «مینو‌چهر = بهشت‌روی» که در برهان آمده، ثانوی است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%DA%86%D9%87%D8%B1%D9%87\",\n            \"https://en.wiktionary.org/wiki/%D9%87%DA%98%DB%8C%D8%B1\",\n            \"https://en.wiktionary.org/wiki/%D8%AE%D8%AC%DB%8C%D8%B1\",\n            \"https://en.wiktionary.org/wiki/%D9%85%D9%86%D9%88%DA%86%D9%87%D8%B1\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:2336\", \"status\": \"supports\", \"note\": \"BQT_v4_pages.txt pdf page 419 (= printed 2336), entry هژیر with Mo'in's footnote 2: '«هجیر (ه.م.) = خجیر (ه.م.)» اوستا -hučiθra، پهلوی hučihr ... بمعنی خوب چهر، خوش‌نما. اوستا -čiθra (نیک نژاد)، بارتولمه ۵۸۷ ...؛ رک: نیبرگ ص ۱۶۹' — plus the Daqiqi couplet 'ای فخر آل اردشیر ... آثار و افعالت هژیر' that the chart quotes.\"},\n            {\"ref\": \"BQT:2047\", \"status\": \"supports\", \"note\": \"Same file, pdf page 130 (= printed 2047), s.v. منوچهر: '... اورا مانوش چهر نام کرد و بمرور ایام و تغییر السنه منوچهر شد'.\"},\n            {\"ref\": \"BQT:674\", \"status\": \"supports\", \"note\": \"BQT_v2_pages.txt, چهر/چهره run (leaf 132 ≈ printed 674), Mo'in's footnote: 'پهلوی čihr (تخم) «نیبرگ ۶۴» ... از اوستا čiθra- «بارتولمه ۵۸۷»، پارسی باستان çiça-'.\"},\n            {\"ref\": \"MON:5140\", \"status\": \"not_checked\", \"note\": \"Mo'in vol. 5 (اعلام) is not online and not in the local library (only the 2-vol Adena lexicon reprint); the same claim is covered by BQT:2047.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie 1971, s.vv. čihr, čihr(ag), hu-čihr\", \"stance\": \"supports\", \"note\": \"PHD.txt: 'čihr [cyhl | M cyhr, N ~] form, shape, appearance, face. čihr(ag) [cyhl(k') | M cyhrg, P -g, N ~] seed, origin; nature, essence'; 'hu-čihr [hwcyhl | M hwcyhr, (N xujīr)] fair, beautiful'.\"},\n            {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II, s.vv. čihr, hu-čihr, dahyupat (Manuščihr)\", \"stance\": \"supports\", \"note\": \"'čihr ... Av. (587) čiθra-, OP *çiça- ... NP čihr'; 'hu-čihr ... NP hujīr, hužīr'; Manuščihr cited as a Pahlavi personal name.\"},\n            {\"src\": \"HRN\", \"where\": \"Grundriss, no entry\", \"stance\": \"silent\", \"note\": \"grep of HRN.txt for čihr/hažīr/Manūčihr returns nothing in the numbered entries consulted; Horn does not treat these.\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur, headword list\", \"stance\": \"silent\", \"note\": \"grep of ARY_pages.txt for چهره / هژیر returns no entry.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Avestan\",\n          \"words\": \"čâyâ, asaya\",\n          \"verdict\": \"transcription_suspect\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"čâyâ, asaya : shade\",\n          \"correct_form\": \"Sanskrit chāyā́- 'shade' (not Avestan) beside Avestan a-saya- 'casting no shadow' (implying *saya- 'shadow')\",\n          \"derivation\": \"The second word is genuine: Avestan a-saya- is an adjective 'der keinen Schatten hat, wirft' (Bartholomae, s.v.), attested of swift steeds in Y.57.27 and as a mountain name in Yt.19.4; it presupposes an unattested *saya- 'shadow' < Proto-Iranian *čaHyā́- < PIE *sḱeh₂-yeh₂-. The first word, čâyâ, is NOT Avestan: it is Sanskrit chāyā́- 'radiance, shimmer, shadow', which Pokorny lists two lines above the Avestan form in exactly this order ('Old Indic chāyā ..., Avestan a-saya- ..., np. sāya'), and which Nourai has taken over into the Avestan box, additionally re-spelling the Sanskrit ch- as č-. Avestan would require sāya-/saya- (Buck writes it starred, 'Av. *saya-'); a form *čāyā is phonologically impossible in Iranian, where PIE palatal *sḱ gives s-/θ-, not č-. The derivation drawn (root 'shadow' > Iranian shadow-word) is right; the language label on the first word is wrong, and the printed page (pdf 451, image saved as sources/refs/ocr/BOOK/451.png) shows the error is the book's, not the extraction's — the JSON reproduces the box exactly.\",\n          \"derivation_fa\": \"واژهٔ دوم درست است: اوستایی a-saya- صفت است به معنی «آن که سایه ندارد/نمی‌افکند» (بارتولمه، ذیل همین مدخل) و بر وجود *saya- «سایه» در اوستایی دلالت می‌کند که از ایرانی آغازین *čaHyā́- و هندواروپایی *sḱeh₂-yeh₂- می‌آید. اما واژهٔ نخست، čâyâ، اوستایی نیست؛ صورت سنسکریت chāyā́- «فروغ، سایه» است که پوکورنی درست دو سطر پیش از صورت اوستایی و به همین ترتیب آورده و نورایی آن را در جعبهٔ «اوستایی» جا داده و ch- سنسکریت را هم č- نوشته است. در زبان‌های ایرانی *sḱ هندواروپایی به s/θ بدل می‌شود نه č، پس *čāyā در اوستایی ناممکن است (باک آن را با ستاره و به‌صورت Av. *saya- می‌آورد). جهت گزاره (ریشهٔ «سایه» ← واژهٔ ایرانی «سایه») درست است؛ خطا در برچسب زبانی و از آنِ کتاب چاپی است، نه خطای خوانش اسکن — تصویر صفحه در sources/refs/ocr/BOOK/451.png ذخیره شده است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B3%D8%A7%DB%8C%D9%87\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:917\", \"status\": \"supports\", \"note\": \"POK_full.txt, lemma 'sḱai-, sḱəi- : sḱī- | Meaning: to glimmer (of wet things); shadow', Page(s): 917-918: 'Old Indic chāyā \\\"radiance, shimmer, shadow\\\", Avestan a-saya- \\\"wer keinen Schatten wirft\\\", np. sāya \\\"shadow, protection\\\"' — note Pokorny labels chāyā Old Indic, Nourai labels it Avestan.\"},\n            {\"ref\": \"SOD:367\", \"status\": \"supports\", \"note\": \"SOD_pages.txt entry 9104 (scan leaf 434 ≈ printed p.368, i.e. the cited page-range): 'sy'k(h) B — sāyak (sy'k, sy'q) < *sāyaka-, Av. a-saya-, Skt. chāyā-, Yaghn. siyoka-, Khwar. sy'k, Pahl. sāyag; shadow, canopy' — Gharib explicitly gives Av. a-saya- and Skt. chāyā- as the comparanda.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"AiW s.v. a-saya- (scan leaf 109)\", \"stance\": \"supports\", \"note\": \"BRT.txt: 'j. a-saya- 1) Adj. \\\"der keinen Schatten hat, wirft\\\": yim .. aurvanta .. vīspaŋhō °ya Y.57.27, 2) n. (oder f.) im Du. Name eines Bergs Yt.19.4. — Vgl. ai. chāyā- f. \\\"Schatten\\\", np. sāya. — Pü.: *nāsāyat, Npü.: sāya.' Bartholomae has no Avestan čāyā.\"},\n            {\"src\": \"SYN\", \"where\": \"Buck §1.63 SHADE\", \"stance\": \"supports\", \"note\": \"SYN.txt: 'Skt. chāyā-, Av. *saya- (a-saya- \\\"without shadow\\\"), NPers. sāya-, Alb. hē, fr. IE *skāi-, *skī-' — Buck marks the Avestan simplex with an asterisk, i.e. unattested.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II 535\", \"stance\": \"supports\", \"note\": \"'Ai. chāyā „Glanz, Schimmer, Schatten”, av. a-saya- „wer keinen Schatten wirft”, np. sāya „Schatten, Schutz”' — same distribution of language labels as Pokorny.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Sogdian\",\n          \"words\": \"sy`k\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Sogdian sy'k / sy'q (Buddhist and Christian Sogdian), read sāyak, 'shadow, canopy', from Proto-Iranian *sāyaka- — i.e. the same *sḱeh₂-yeh₂- + the productive Iranian -ka- suffix that also yields Middle Persian sāyag and hence New Persian sāya. Gharib's entry lines it up with Av. a-saya-, Skt. chāyā-, Yaghnobi siyoka-, Khwarezmian sy'k and Pahlavi sāyag, so the chart's arrow Avestan (shadow-word) > Sogdian is exactly what the cited dictionary says. Sogdian y here is the glide of *āya, and the -k spells the suffix -ak; the oblique/plural forms -y, -t(h) are given by Gharib.\",\n          \"derivation_fa\": \"سغدی sy'k/sy'q که sāyak خوانده می‌شود، به معنی «سایه، سایبان» است و از ایرانی آغازین *sāyaka- می‌آید؛ یعنی همان ستاک *sāya- به‌علاوهٔ پسوند زایای -ka- ایرانی که فارسی میانهٔ sāyag و فارسی نوِ «سایه» را هم پدید آورده است. غریب در فرهنگ سغدی (مدخل ۹۱۰۴، حوالی ص ۳۶۷–۳۶۸) آن را با اوستایی a-saya-، سنسکریت chāyā-، یغنابی siyoka-، خوارزمی sy'k و پهلوی sāyag برابر نهاده است. پس پیوند نمودار (اوستایی ← سغدی) درست و «تأییدشده» است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"SOD:367\", \"status\": \"supports\", \"note\": \"SOD_pages.txt entry 9104 (computed scan leaf 434, printed ≈ 368): 'sy'k(h) B ... sāyak (sy'k, sy'q) ®<*sāyaka-, Av. a-saya-, Skt. chāyā-, Yaghn. siyoka-, Khwar. sy'k, Pahl. sāyag | shadow, canopy'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. sayag\", \"stance\": \"supports\", \"note\": \"PHD.txt: 'sayag [s'dk' | M s'yg, N sāya] shade, shadow' — the Middle Persian member of the same *sāyaka- set; also 'ham-sayag [-s'dk' | N hamsāya] neighbour'.\"},\n            {\"src\": \"ISS\", \"where\": \"Bailey, Khotanese\", \"stance\": \"silent\", \"note\": \"no Khotanese form was needed or found for this node; Gharib's own comparanda (Yaghnobi, Khwarezmian) already cover the eastern Iranian side.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Persian\",\n          \"words\": \"sâyeh «سایه»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"New Persian سایه sāya 'shade, shadow, protection' < Middle Persian sāyag [s'dk' / Manichaean s'yg] < Proto-Iranian *sāyaka- (Wiktionary's chain: MP sāyag < OP *θāyakā < PIr *caHyā́kaH), ultimately PIE *sḱeh₂-yeh₂- 'shadow', whose Indic cognate is chāyā́ and whose Greek cognate is σκιά. The MP -ag > NP -a change is the ordinary one (cf. bandag > banda); the long ā is retained. Horn's numbered entry 695 on the very page Nourai cites gives exactly this, together with the Kurdish, Balochi and Wakhi/Sarikoli cognates. The extended sense 'protection, patronage' (سایهٔ کسی) is already Middle Persian.\",\n          \"derivation_fa\": \"«سایه» از فارسی میانهٔ sāyag (نوشتهٔ s'dk'، مانوی s'yg) و آن از ایرانی آغازین *sāyaka- می‌آید؛ ویکی‌واژه زنجیره را چنین می‌دهد: فارسی میانه sāyag < پارسی باستان *θāyakā < ایرانی آغازین *caHyā́kaH، و سرانجام هندواروپایی *sḱeh₂-yeh₂- «سایه» که هم‌ریشهٔ سنسکریت chāyā́ و یونانی σκιά است. پسوند -ag فارسی میانه طبق قاعده در فارسی نو -ه شده (مانند bandag > بنده) و ā کشیده برجا مانده است. هرن در «بنیاد ریشه‌شناسی فارسی نو»، مدخل ۶۹۵، در همان صفحهٔ ۱۵۴ که نورایی یاد کرده، همین را آورده است. معنی گستردهٔ «پناه و حمایت» نیز از دورهٔ میانه پیداست. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B3%D8%A7%DB%8C%D9%87\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"HRN:154\", \"status\": \"supports\", \"note\": \"HRN.txt scan leaf 176 = printed p.154, entry '695. sāye \\\"Schatten, Schutz\\\". ai. chāyā \\\"Schatten\\\"; phlv. sāyak, kurd. sē, sī; bel. sāig, n. sāī; wax. LW. sāyā, sar. suyā.' — page and entry match exactly.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 s.v. sayag\", \"stance\": \"supports\", \"note\": \"'sayag [s'dk' | M s'yg, N sāya] shade, shadow'.\"},\n            {\"src\": \"HUB\", \"where\": \"Persische Studien\", \"stance\": \"silent\", \"note\": \"grep of HUB.txt for sāya/sāye returns no entry; Hübschmann's part I follows Horn's numbering but does not comment on no. 695.\"},\n            {\"src\": \"SYN\", \"where\": \"Buck §1.63\", \"stance\": \"supports\", \"note\": \"'NPers. sāya-, ... fr. IE *skāi-, *skī-, prob. the same root as in Goth. skeinan, OE scīnan'.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Greek\",\n          \"words\": \"skena\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Greek σκηνή skēnḗ (Doric σκᾱνά skānā) 'tent, booth; stage building of a theatre', printed by Nourai without the length mark as 'skena'. Pokorny puts it under the shadow root with the lengthened grade sḱē-: 'with the grade sḱēi-: σκηνή, Doric σκᾱνά \\\"tent, stage, scene\\\", σκῆνος, Doric σκᾶνος n. \\\"tent; body (as wrapping of the soul)\\\"', beside σκιά 'shadow'. Klein s.v. 'scene' says the same ('Gk. σκηνή, \\\"tent, booth, stage\\\", which is rel. to σκιά, \\\"shade\\\"'), and Etymonline, citing Beekes' sources, explains the semantics: the word 'originally denoted any light construction of cloth hung between tree branches in order to provide shadow'. Wiktionary agrees that it is 'usually said to be a derivative of PIE *(s)ḱeh₃- \\\"shade, shadow\\\"', while noting that the ē-vocalism is not trivially derivable from the standard full/zero grades — a caveat about ablaut, not about the connection.\",\n          \"derivation_fa\": \"یونانی σκηνή (skēnḗ)، در گویش دوری σκᾱνά، به معنی «خیمه، سایبان؛ ساختمان پشت صحنهٔ تئاتر» است؛ کتاب آن را بی‌نشانهٔ کشش «skena» نوشته است. پوکورنی آن را زیر همان ریشهٔ «سایه» با درجهٔ کشیدهٔ sḱē- می‌آورد و در کنار σκιά «سایه» می‌نشاند، و کلاین نیز در مدخل scene همین را می‌گوید. از نظر معنایی، چنان‌که بیکس (به نقل اتیمولوژی‌آنلاین) توضیح می‌دهد، σκηνή نخست به هر سرپناه سبکِ پارچه‌ای گفته می‌شد که میان شاخه‌ها می‌آویختند تا سایه بیفکند. ویکی‌واژه این اشتقاق را می‌پذیرد و تنها در توجیه واکهٔ ē تردید می‌کند. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%CF%83%CE%BA%CE%B7%CE%BD%CE%AE\",\n            \"https://www.etymonline.com/word/scene\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:917\", \"status\": \"supports\", \"note\": \"POK_full.txt, lemma 'sḱai-, sḱəi- : sḱī-', Page(s): 917-918: 'gr. σκιά f. \\\"shadow\\\" ... with the grade sḱēi-: σκηνή, Doric σκανά \\\"tent, stage, scene\\\", σκῆνος, Doric σκᾶνος n. \\\"tent; body\\\"'.\"},\n            {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"AHD_watkins1985.txt s.v. 'skeəi-. To gleam' lists Greek skia (SKIAGRAM, SKIASCOPE, SQUIRREL) under Pok. skai- 917 but does not carry skēnē/SCENE in its word list (index has SKIAGRAM skeəi- only), so Watkins supports the root but not this particular Greek word.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein 1966-67 s.v. scene\", \"stance\": \"supports\", \"note\": \"KLN_1971.txt line 214307: 'scene, n. — MF. scene (F. scène), fr. L. scaena, scena, \\\"stage, scene\\\", fr. Gk. σκηνή, \\\"tent, booth, stage\\\", which is rel. to σκιά, \\\"shade\\\", fr. I.-E. base *skā(i), *skəi-, *skī-, \\\"to shine, flicker, glimmer\\\", whence also OI. chāyā ... Goth. skeinan, OE. scīnan, \\\"to shine\\\".'\"},\n            {\"src\": \"SYN\", \"where\": \"Buck §1.63\", \"stance\": \"supports\", \"note\": \"Buck lists Grk. σκιά under IE *skāi-, *skī-, the same root; σκηνή is its lengthened-grade derivative in Pokorny.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Latin\",\n          \"words\": \"scaena\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin scaena (also spelled scēna) 'stage of a theatre, scene' is a borrowing of Greek σκηνή, taken over in the Doric/South-Italian form σκᾱνά, which is why Latin has -ae-/-ē- rather than -ē- alone; the loan belongs to the earliest layer of Roman theatrical vocabulary (Plautus, Terence). Ernout–Meillet note that the doublet scēna ~ scaena 'semble supposer un intermédiaire étrusque entre le modèle grec et l'emprunt latin', i.e. the word probably reached Rome through Etruscan mediation along with much other stage vocabulary — a refinement of, not an objection to, the chart's Greek > Latin arrow. Klein gives the same descent.\",\n          \"derivation_fa\": \"لاتین scaena (به نگارش دیگر scēna) «صحنهٔ نمایش» وام‌واژه‌ای است از یونانی σκηνή، و چون از صورت دوری σκᾱνά گرفته شده، در لاتین -ae-/-ē- دارد؛ این وام‌گیری به کهن‌ترین لایهٔ واژگان نمایشی رومی (پلاؤتوس و ترنتیوس) بازمی‌گردد. ارنو و مِیه یادآور می‌شوند که دوگانگی scēna ~ scaena احتمالاً نشان می‌دهد واژه از راه اتروسکی به لاتین رسیده است؛ این نکته اشتقاق یونانی ← لاتین را رد نمی‌کند بلکه دقیق‌تر می‌کند. کلاین نیز همین زنجیره را می‌دهد. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/scene\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"not_found\", \"note\": \"AHD_watkins1985.txt has no SCENE/SCAENA entry in the Indo-European roots appendix or its English index (grep for 'SCENE' returns only SKIAGRAM under skeəi-); Nourai's bare 'AHD' citation for this node cannot be verified in the 1985 Watkins text.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LAT\", \"where\": \"Ernout–Meillet, s.v. obscaenus (LAT.txt line 42843)\", \"stance\": \"supports\", \"note\": \"'la variation obscēnus, obscaenus rappelle celle de scēna, scaena qui semble supposer un intermédiaire étrusque entre le modèle grec et l'emprunt latin'.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. scene\", \"stance\": \"supports\", \"note\": \"'fr. L. scaena, scena, \\\"stage, scene\\\", fr. Gk. σκηνή'.\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"French\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"An empty pass-through box in the book (printed as a bare 'French' label with no word): the implied word is Old/Middle French scène (attested 14th c.), a learned borrowing of Latin scaena/scēna, which then gives English scene (1530s) and, later, Persian سناریو through the francophone cinema vocabulary. Etymonline: 'scene (n.) 1530s ... from French scène (14c.), from Latin scaena, scena'.\",\n          \"derivation_fa\": \"این جعبه در کتاب تهی است و فقط برچسب «فرانسوی» دارد؛ واژهٔ مقصود فرانسوی scène است که در سدهٔ چهاردهم میلادی به‌صورت وام‌واژه‌ای عالمانه از لاتین scaena/scēna وارد فرانسوی شده و سپس انگلیسی scene (۱۵۳۰م) و از راه واژگان سینمایی فرانسوی، «سناریو»ی فارسی از آن سرچشمه گرفته‌اند. اتیمولوژی‌آنلاین: «scene، ۱۵۳۰م، از فرانسوی scène (سدهٔ ۱۴)، از لاتین scaena». حلقهٔ واسطه درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/scene\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the book gives no reference for this pass-through box.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. scene\", \"stance\": \"supports\", \"note\": \"'MF. scene (F. scène), fr. L. scaena, scena'.\"},\n            {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century\", \"stance\": \"silent\", \"note\": \"not consulted separately; Klein and Etymonline already cover this uncontroversial Latin > French link.\"}\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"Persian\",\n          \"words\": \"senârîo «سناریو»\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Persian سناریو senāriyo 'film script, scenario' is indeed a 20th-century European loan in the chain scaena > scēnārius > scenario, but the immediate donor is disputed between the chart and Nourai's own cited source. Mo'in, whom the node cites, tags the word [ایتا.] — Italian — in his lexicon ('(س) [ایتا.] (اِ.) فیلم‌نامه، داستان مخصوص فیلم سینما'), and that matches the international history of the word: Italian scenario (from Late Latin scēnārius 'of stage scenes') was borrowed into French as scénario in the 18th c. and into English in 1868. The chart's direct French > Persian arrow is nevertheless well motivated for Persian: the Persian form has s- (not Italian š-) and final -o exactly as French /senaʁjo/, and Persian cinema terminology of the 1930s-40s came through French. So the word does descend from Latin scaena as drawn, but the missing Italian link makes the chart's route only approximately right.\",\n          \"derivation_fa\": \"«سناریو» وام‌واژه‌ای اروپایی از سدهٔ بیستم است و در نهایت به لاتین scaena و مشتق آن scēnārius بازمی‌گردد؛ اما دربارهٔ زبان واسط میان نمودار و مأخذ خودِ نورایی اختلاف هست. معین که در همین گره به او ارجاع داده شده، واژه را [ایتا.] یعنی ایتالیایی برچسب زده است («(س) [ایتا.] (اِ.) فیلم‌نامه، داستان مخصوص فیلم سینما»)، و تاریخ واژه هم همین را نشان می‌دهد: ایتالیایی scenario از لاتین متأخر scēnārius، سپس فرانسوی scénario و انگلیسی scenario (۱۸۶۸م). با این همه، پیکان مستقیم «فرانسوی ← فارسی» در نمودار بی‌وجه نیست، چون صورت فارسی s- دارد نه š- ایتالیایی و پایانهٔ -و آن دقیقاً مطابق تلفظ فرانسوی است و واژگان سینمایی فارسی در دههٔ ۱۳۱۰–۱۳۲۰ بیشتر از فرانسوی گرفته شده‌اند. پس اصل اشتقاق درست است ولی حلقهٔ ایتالیایی افتاده است؛ «با احتیاط پذیرفتنی».\",\n          \"sources\": [\n            \"https://abadis.ir/fatofa/%D8%B3%D9%86%D8%A7%D8%B1%DB%8C%D9%88/\",\n            \"https://www.etymonline.com/word/scenario\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"MON\", \"status\": \"partial\", \"note\": \"Mo'in's lexicon entry for سناریو, read through abadis.ir (section فرهنگ معین): '(س ) [ ایتا. ] (اِ. ) فیلم نامه ، داستان مخصوص فیلم سینما' — Mo'in has the word but tags it Italian, not French as the chart draws.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. scenario\", \"stance\": \"partial\", \"note\": \"KLN_1971.txt line 214302: 'scenario, n., outline of the plot of a play. — It., fr. Late L. scēnārius, \\\"of stage scenes\\\", fr. L. scaena, scena. See scene.' — Italian, not French.\"},\n            {\"src\": \"DEV\", \"where\": \"Devic, Dictionnaire des mots français d'origine orientale\", \"stance\": \"silent\", \"note\": \"not applicable: scénario is not an orientalism; grep returns nothing.\"}\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"English\",\n          \"words\": \"scene, scenario\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"English scene is exactly as drawn: 1530s 'subdivision of an act of a play', from French scène (14c.) < Latin scaena/scēna < Greek σκηνή. English scenario, however, did not come through French: it was borrowed in 1868 directly from Italian scenario (Late Latin scēnārius), an earlier nativized form scenary being attested from the 1690s; Klein likewise marks it 'It., fr. Late L. scēnārius'. So of the two words in the box, one confirms the French route and one needs an Italian node, which the chart does not draw.\",\n          \"derivation_fa\": \"انگلیسی scene دقیقاً همان‌گونه است که نمودار می‌کشد: از ۱۵۳۰م به معنی «بخشی از یک پرده» از فرانسوی scène (سدهٔ ۱۴) و آن از لاتین scaena و یونانی σκηνή. اما scenario از راه فرانسوی نیامده است: در ۱۸۶۸م مستقیماً از ایتالیایی scenario (از لاتین متأخر scēnārius) وام گرفته شده و صورت بومی‌شدهٔ پیشین آن، scenary، از دههٔ ۱۶۹۰ گواهی دارد؛ کلاین هم آن را «It., fr. Late L. scēnārius» می‌داند. پس از دو واژهٔ این جعبه یکی راه فرانسوی را تأیید می‌کند و دیگری به حلقهٔ ایتالیایی نیاز دارد که در نمودار نیست.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/scene\",\n            \"https://www.etymonline.com/word/scenario\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the book gives no reference for this box.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein s.vv. scene, scenario\", \"stance\": \"partial\", \"note\": \"'scene, n. — MF. scene (F. scène), fr. L. scaena' (supports) but 'scenario, n. — It., fr. Late L. scēnārius' (Italian, not French).\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etymological Dictionary\", \"stance\": \"silent\", \"note\": \"grep of SKT.txt for 'scene'/'shine, to' returns no matching headword line in this OCR; Skeat could not be used for this node.\"}\n          ]\n        },\n        {\n          \"id\": 11,\n          \"lang\": \"Germanic\",\n          \"words\": \"skînan\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Proto-Germanic *skīnaną 'to shine, appear' (Gothic skeinan, Old Norse skína, Old High German/Old English scīnan, Dutch schijnen, German scheinen), from the same *sḱeh₂(i)- 'glimmer, cast a shadow' with the zero-grade *skī- plus the n-present suffix. Watkins states it formally: 'skeəi-. To gleam. 1. Suffixed form *ske(ə)i-no- in Germanic *skīnan, to gleam, shine, in: a. Old English scīnan, to shine: SHINE', referred to Pokorny 917 — precisely Nourai's 'AHD' citation. Pokorny p.917-918 lists 'Gothic skeinan, Old Icelandic skína, Old High German Old English scīnan, Modern High German scheinen (n-present)'. The semantic bridge between 'shadow' and 'shine' is the notion of faint light or reflection (Buck).\",\n          \"derivation_fa\": \"ژرمنی آغازین *skīnaną «درخشیدن، پدیدار شدن» (گوتی skeinan، نورس کهن skína، آلمانی علیای باستان و انگلیسی باستان scīnan، هلندی schijnen، آلمانی scheinen) از همان ریشهٔ *sḱeh₂(i)- «کم‌سو درخشیدن؛ سایه» با درجهٔ صفر *skī- و پسوند حال n ساخته شده است. واتکینز در پیوست ریشه‌های هندواروپایی می‌نویسد: «skeəi- درخشیدن... صورت پسونددار *ske(ə)i-no- در ژرمنی *skīnan ... انگلیسی باستان scīnan: SHINE» و به پوکورنی ۹۱۷ ارجاع می‌دهد؛ یعنی همان ارجاع AHD نورایی. پیوند معنایی «سایه» و «درخشش» از راه مفهوم «فروغ کم‌رنگ/بازتاب» است (باک). ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/shine\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt: 'skeəi-. To gleam. 1. Suffixed form *ske(ə)i-no- in Germanic *skīnan, to gleam, shine, in: a. Old English scīnan, to shine: SHINE; b. Old High German scīnan, to shine: GEGENSCHEIN. ... [Pok. skai- 917.]'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"IEW 917-918, lemma sḱai-\", \"stance\": \"supports\", \"note\": \"'Gothic skeinan \\\"shine, appear, seem, gleam\\\", Old Icelandic skína, Old High German Old English scīnan, Modern High German scheinen (n-present)'.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. scene (cross-reference to shine)\", \"stance\": \"supports\", \"note\": \"'... whence also OI. chāyā ... Goth. skeinan, OE. scīnan, \\\"to shine\\\". See shine.'\"},\n            {\"src\": \"SYN\", \"where\": \"Buck §1.63\", \"stance\": \"supports\", \"note\": \"'prob. the same root as in Goth. skeinan, OE scīnan, ChSl. sijati \\\"shine\\\". Connection through a notion of \\\"faint light\\\" ... or \\\"reflection\\\".'\"}\n          ]\n        },\n        {\n          \"id\": 12,\n          \"lang\": \"English\",\n          \"words\": \"shine\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English shine < Middle English shinen < Old English scīnan 'shed or give out light, be radiant' (class I strong verb, past scān, pp. scinen) < Proto-Germanic *skeinanan/*skīnaną (cf. Old Saxon/Old High German skīnan, Old Norse skína, Gothic skeinan), from the PIE root Etymonline cites as *skai- 'to shine, to gleam' (Old Church Slavonic sinati 'to flash up, shine' belongs here too). The chart's Germanic > English step is the standard one and needs no further comment.\",\n          \"derivation_fa\": \"انگلیسی shine از انگلیسی میانهٔ shinen و آن از انگلیسی باستان scīnan «تابیدن، درخشیدن» (فعل قوی طبقهٔ یکم: گذشتهٔ scān، اسم مفعول scinen) می‌آید و آن از ژرمنی آغازین *skīnaną (ساکسونی باستان و آلمانی علیای باستان skīnan، نورس کهن skína، گوتی skeinan). اتیمولوژی‌آنلاین ریشهٔ هندواروپایی را *skai- «درخشیدن» می‌گذارد و اسلاوی کلیسایی کهن sinati «تابیدن» را هم‌ریشه می‌شمارد. گام «ژرمنی ← انگلیسی» در نمودار همان زنجیرهٔ استاندارد است و ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/shine\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the book gives no reference for this box; the parent node carries AHD, which does list SHINE under skeəi-.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. skeəi-\", \"stance\": \"supports\", \"note\": \"'Old English scīnan, to shine: SHINE'.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. scene\", \"stance\": \"supports\", \"note\": \"'Goth. skeinan, OE. scīnan, \\\"to shine\\\". See shine and cp. words there referred to.'\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 1,\n      \"root\": \"Skaif, Skaip\",\n      \"verdict\": \"plausible\",\n      \"modern_form\": \"Old Iranian *skaif-/*skaip- 'to be patient, endure' (Abolqasemi); no independent reconstruction in Cheung's Etymological Dictionary of the Iranian Verb\",\n      \"note\": \"The root box is a faithful rendering of Abolqasemi, Fe'l-hā-ye Fārsi-ye Dari p.63-64, whose Persian text reads 'شکیفت < ایرانی باستان *skaif-ta ... این ریشه به معنی صبر کردن است' and 'شکیب < فارسی میانه škēb < ایرانی باستان *skaip-a'. Two caveats: (a) Abolqasemi's gloss is «صبر کردن» 'to be patient / to endure', which the chart renders 'to wait' — close but not identical; (b) the root is a back-projection from the Persian verb pair šikēftan / šakēb and is not in Cheung 2007 (no *skaif or *skaip entry; his nearest lemma is *skap/f 'to split, crack', which is a different root), nor in Horn or Hübschmann, and Wiktionary's entries for شکیب and شکیفتن carry no etymology at all. So the root is plausible but rests on a single modern Iranian authority.\",\n      \"note_fa\": \"جعبهٔ ریشه دقیقاً برگرفته از «فعل‌های فارسی دری» ابوالقاسمی صص ۶۳–۶۴ است که می‌نویسد: «شکیفت < ایرانی باستان *skaif-ta … این ریشه به معنی صبر کردن است» و «شکیب < فارسی میانه škēb < ایرانی باستان *skaip-a». دو نکته: نخست آنکه معنی نزد ابوالقاسمی «صبر کردن» است و نورایی آن را «to wait / انتظار کشیدن» آورده که نزدیک است ولی یکسان نیست؛ دوم آنکه این ریشه بازسازیِ واپس‌نگرانه از جفت «شکیفتن/شکیب» است و در فرهنگ ریشه‌شناختی فعل ایرانی چونگ (۲۰۰۷) مدخلی به نام *skaif یا *skaip وجود ندارد (نزدیک‌ترین مدخل او *skap/f «شکافتن» است که ریشه‌ای دیگر است)، و هرن و هوبشمان و ویکی‌واژه هم دربارهٔ آن خاموش‌اند. پس ریشه «با احتیاط پذیرفتنی» است و تنها بر یک مرجع امروزی ایرانی تکیه دارد.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%D8%B4%DA%A9%DB%8C%D8%A8\",\n        \"https://en.wiktionary.org/wiki/%D8%B4%DA%A9%DB%8C%D9%81%D8%AA%D9%86\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"FFD:63\", \"status\": \"supports\", \"note\": \"FFD_pages.txt, pdf page 68 = printed 63 (header 'ماده‌های ماضی و مضارع فارسی دری ۶۳'), last entry: 'شکیفت < ایرانی باستان *skaif-ta. برای -ta → آراست. skaif صورت اصلی *skif ...' continuing on printed 64 with 'است. این ريشه به معنی «صبر کردن» است.'\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"CHEUNG\", \"where\": \"EDIV, root index\", \"stance\": \"silent\", \"note\": \"grep of CHEUNG.txt for skaif / skaip / škēb / 'be patient' finds no such lemma; the only nearby root is '*skap/f \\\"to split, make a crack, crack\\\"' (p.345), semantically unrelated.\"},\n        {\"src\": \"HRN\", \"where\": \"Grundriss\", \"stance\": \"silent\", \"note\": \"grep of HRN.txt for šakīb / šikēftan returns nothing.\"},\n        {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. škēbāg\", \"stance\": \"supports\", \"note\": \"'škēbāg [škyp'k | P škyb-, N šikēbā] patient. ~īh: patience.' — confirms a Middle Persian stem škēb- with exactly this meaning, which is the evidence the reconstruction rests on.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"škěb\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Middle Persian škēb 'patience; patient', attested in MacKenzie's dictionary as the adjective škēbāg [Book Pahlavi škyp'k, Psalter stem škyb-] 'patient', with abstract škēbāgīh 'patience' (MacKenzie's English index: 'patience ... škēbāgīh; patient ... škēbāg'). The chart's škēb is the bare stem behind that -āg derivative and behind New Persian šakēb. Abolqasemi derives it from Old Iranian *skaip-a-, i.e. the p-variant of the root with the thematic vowel that regularly yields a Middle Persian present stem; MP -ē- reflects Old Iranian *-ai-, and *p between the diphthong and the vowel is spirantised, which is why the Book Pahlavi spelling is škyp' but the Psalter has škyb-.\",\n          \"derivation_fa\": \"فارسی میانه škēb «شکیبایی؛ شکیبا»، که در فرهنگ مکنزی به‌صورت صفت škēbāg (پهلوی کتابی škyp'k، ستاک مزامیر škyb-) «شکیبا» و اسم معنای škēbāgīh «شکیبایی» آمده است. صورت škēb در نمودار همان ستاک برهنه‌ای است که هم -āg بر آن افزوده شده و هم فارسی نوِ «شکیب» از آن است. ابوالقاسمی آن را از ایرانی باستان *skaip-a- می‌گیرد: ai ایرانی باستان در فارسی میانه به ē کشیده بدل شده و p میان‌واکه‌ای سوده (spirant) شده است؛ از همین‌روست که املای پهلوی کتابی škyp' ولی صورت مزامیر škyb- است. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"FFD:63\", \"status\": \"partial\", \"note\": \"FFD_pages.txt printed p.63 gives the root *skaif-ta for the past stem شکیفت; the Middle Persian škēb itself is given one page later (printed 64): 'شکیب < فارسی میانه škēb < ایرانی باستان *skaip-a'. So the content is right but Nourai's page number for the Pahlavi box is one page early.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 s.v. škēbāg\", \"stance\": \"supports\", \"note\": \"'škēbāg [škyp'k | P škyb-, N šikēbā] patient. ~īh: patience.' Also in the English-Pahlavi index: 'patient bārestān, burd, škēbāg'.\"},\n            {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II glossary\", \"stance\": \"silent\", \"note\": \"grep of NYB_vol2_glossary.txt for škēb / skyb returns nothing; the word does not occur in Nyberg's text corpus.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"šakîb «شکیب»; šakîbîdan «شکیبیدن»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"New Persian شکیب šakēb/šikēb 'patience' is the inherited continuant of Middle Persian škēb, with the usual prothetic/anaptyctic vowel breaking the initial cluster šk- (škēb > šakēb/šikēb), and it is at the same time the present stem of the verb شکیفتن šikēftan 'to be patient, endure, wait' (Wiktionary: 'شکیب ... present stem form of شکیفتن'; 'شکیفتن ... to be patient, wait; to tolerate', Rumi, Masnavi II.76). شکیبیدن šakēbīdan is the secondary, denominative infinitive built on that present stem beside the older šikēftan — exactly the pair the book prints (شکیب / شکیفتن in the added Persian script, with شکیبا and شکیبایی). The -f- of šikēftan and the -b- of šakēb continue the *skaif- / *skaip- alternation Abolqasemi posits: *skaif-ta gives the past stem šikēft, *skaip-a the present stem šakēb.\",\n          \"derivation_fa\": \"«شکیب» بازماندهٔ منظم škēb فارسی میانه است؛ خوشهٔ آغازین šk- با واکهٔ میانجی شکسته شده و šakēb/šikēb به دست آمده است. همین واژه در عین حال ستاک حال فعل «شکیفتن» است (ویکی‌واژه: «شکیب … صورت ستاک حال شکیفتن»؛ «شکیفتن … صبور بودن، منتظر ماندن، تحمل کردن»، با شاهدی از مثنوی مولوی، دفتر دوم). «شکیبیدن» مصدر جعلیِ ثانوی است که از همان ستاک حال ساخته شده و در کنار «شکیفتن» کهن‌تر به کار رفته است — درست همان جفتی که کتاب در جعبهٔ فارسی آورده (شکیب/شکیبا/شکیبایی و شکیفتن). تفاوت f و b در «شکیفتن» و «شکیب» همان گردش *skaif-/*skaip- است که ابوالقاسمی فرض کرده: *skaif-ta ستاک گذشته و *skaip-a ستاک حال. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B4%DA%A9%DB%8C%D8%A8\",\n            \"https://en.wiktionary.org/wiki/%D8%B4%DA%A9%DB%8C%D9%81%D8%AA%D9%86\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"FFD:64\", \"status\": \"supports\", \"note\": \"FFD_pages.txt pdf page 69 = printed 64: 'شکیب < فارسی میانه škēb < ایرانی باستان *skaip-a. برای -a → آرای.' — exactly the chart's Pahlavi > Persian arrow and page.\"},\n            {\"ref\": \"MON\", \"status\": \"not_checked\", \"note\": \"no page number is given for Mo'in here and vol. 2 of the 6-vol print is not online; the abadis/vajehyab lexicon text for شکیب was not consulted for this node because FFD already carries the etymology.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. škēbāg\", \"stance\": \"supports\", \"note\": \"MacKenzie explicitly gives the New Persian outcome: 'škēbāg ... N šikēbā' — i.e. شکیبا, one of the forms in the book's added Persian script.\"},\n            {\"src\": \"HUB\", \"where\": \"Persische Studien\", \"stance\": \"silent\", \"note\": \"grep of HUB.txt for šakīb/šikēftan returns nothing.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"EDIV\", \"stance\": \"silent\", \"note\": \"no entry for the verb šikēftan / šakēb in Cheung 2007 (grep for 'be patient' finds only the Sanskrit kṣam- comparandum under an unrelated root).\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 3,\n      \"root\": \"Skaivos\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *skeh₂iwós 'left, left-handed' (> Proto-Italic *skaiwos)\",\n      \"note\": \"Nourai's headword and gloss are taken verbatim from Mann, IEC col./p. 1146: 'skaiuos \\\"left-hand, sinister, odd, strange\\\"', and Mann's own reference there is 'WP II, 537', which is Nourai's second citation. Walde-Pokorny II 537 has 'skaiuos \\\"link\\\", reimt auf *laiuos. Gr. σκαιός = lat. scaevus, σκαιότης = scaevitas. Curtius 166. Vielleicht ursprgl. \\\"schief\\\"'. Modern scholarship agrees: Wiktionary reconstructs PIE *skeh₂iwos for both Greek σκαιός and Latin scaevus. The root box is therefore correct, though 'sinister, odd, strange' is the English-side spread of the meaning; the core sense is 'left'.\",\n      \"note_fa\": \"سرواژه و معنیِ «Skaivos: شوم، عجیب، ناهنجار» عیناً از فرهنگ تطبیقی هندواروپاییِ مان، ص ۱۱۴۶ گرفته شده است: «skaiuos \\\"چپ، شوم، عجیب، بیگانه\\\"»، و خود مان آنجا به والده–پوکورنی جلد دوم ص ۵۳۷ ارجاع می‌دهد که همان ارجاع دوم نورایی است. در والده–پوکورنی آمده: «skaiuos \\\"چپ\\\"، هم‌وزن *laiuos؛ یونانی σκαιός = لاتین scaevus». پژوهش امروزی نیز همین را می‌گوید و ویکی‌واژه برای هر دو واژهٔ یونانی و لاتین ریشهٔ هندواروپایی *skeh₂iwos را بازسازی می‌کند. پس جعبهٔ ریشه درست است، هرچند معنی بنیادی «چپ» است و «شوم و ناهنجار» گسترش معنایی آن.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/scaevus\",\n        \"https://en.wiktionary.org/wiki/%CF%83%CE%BA%CE%B1%CE%B9%CF%8C%CF%82\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"IEC:1146\", \"status\": \"supports\", \"note\": \"IEC.txt scan leaf 635 (printed 1146-1147): 'skaiuos \\\"left-hand, sinister, odd, strange\\\". Cf. skauios, skeuios, ksauios, kseuios. WP II, 537 | Per. cf. šūx, adj. \\\"lewd, impudent\\\"; Oss. xiw, adj. \\\"straddle-legged\\\"; Gk. skaiós, adj. \\\"left-handed, awkward, stupid, unlucky, crooked\\\"; Alb. i huej ...; Lat. scaevus \\\"lefthand, sinister, unlucky\\\"; W ysgoew ...' — Nourai's gloss is Mann's, word for word.\"},\n        {\"ref\": \"WLD2:537\", \"status\": \"partial\", \"note\": \"WLD_Bd2_pages.txt, running head 'skaiuos — (s)q(h)ai(-t-, -d-) 537': 'skaiuos \\\"link\\\", reimt auf *laiuos. Gr. σκαιός = lat. scaevus, σκαιότης = scaevitas. Curtius 166. Vielleicht ursprgl. \\\"schief\\\"' — supports the root and the Greek/Latin equation, but Walde-Pokorny lists no Iranian member at all, so it does not support the Persian branch.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"POK\", \"where\": \"IEW, lemma (s)kai- 917 / skei-p- 922\", \"stance\": \"partial\", \"note\": \"POK_full.txt line 76958: 'Indo-Germanic skei-p-, -b- extended from skei-, compare *skai-uo-s (*sḱai-uo-s) \\\"slant, crooked\\\"' — Pokorny knows the form skai-u̯o- but treats it as a side-note, not a lemma with Iranian material.\"},\n        {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. scaeuus\", \"stance\": \"supports\", \"note\": \"LAT.txt line 55705: 'scaeuus, -a, -um: gauche ... Le latin, qui a laeuus en face de λαιός, a de même scaeuus en face de σκαιός; formation parallèle, avec a radical.'\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985\", \"stance\": \"silent\", \"note\": \"grep of AHD_watkins1985.txt for skai-u̯o-/scaevus/skaios returns nothing; the root is not in Watkins's appendix (no English descendant).\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Greek\",\n          \"words\": \"skaios\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Ancient Greek σκαιός skaiós 'left, left-handed' and hence 'clumsy, awkward, boorish, ill-omened', from earlier *σκαιϝός *skaiwós < PIE *skeh₂iwós; the digamma is preserved in the Mycenaean-era form and lost in classical Greek, giving the diphthong -αι- + -ός. The derivative σκαιότης 'awkwardness' answers Latin scaevitas. Nourai's gloss 'awkward' is the secondary sense; the primary sense is 'left(-hand)', from which 'awkward, unlucky' develops through the usual Indo-European valuation of the left side (cf. Latin sinister, Greek ἀριστερός euphemism).\",\n          \"derivation_fa\": \"یونانی باستان σκαιός «چپ، چپ‌دست» و از همین‌رو «ناشی، بی‌دست‌وپا، بدشگون»، از صورت کهن‌تر *σκαιϝός و آن از هندواروپایی *skeh₂iwós؛ واکِ ϝ (دیگاما) در یونانی کلاسیک افتاده و دوگانه‌واکهٔ -αι- برجا مانده است. مشتق σκαιότης «ناشی‌گری» برابر scaevitas لاتین است. معنی «awkward» که نورایی آورده معنای ثانوی است؛ معنی اصلی «چپ» است و از آن، مانند sinister لاتین، معنای «شوم و ناشی» پدید آمده است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%CF%83%CE%BA%CE%B1%CE%B9%CF%8C%CF%82\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"IEC:1146\", \"status\": \"supports\", \"note\": \"Mann p.1146 s.v. skaiuos: 'Gk. skaiós, adj. \\\"left-handed, awkward, stupid, unlucky, crooked\\\"'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"WLD\", \"where\": \"Bd. II 537\", \"stance\": \"supports\", \"note\": \"'Gr. σκαιός = lat. scaevus, σκαιότης = scaevitas.'\"},\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. scaeuus\", \"stance\": \"supports\", \"note\": \"'scaeuus en face de σκαιός; formation parallèle'.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Latin\",\n          \"words\": \"scaevus\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin scaevus 'left, on the left' < Proto-Italic *skaiwos < PIE *skeh₂iwós, formed exactly like laevus : Greek λαιός. In Latin it is mainly augural: scaeva f. 'omen coming from the left', bona scaeva 'good omen', the cognomen Scaeva 'left-handed' and the amulet scaevola explained by Varro (L.L. 7,97) — and because Roman augury counted the left as favourable, scaevus could mean 'auspicious' as well as, under Greek influence from σκαιός, 'clumsy' and 'sinister, unlucky' (P.F. 443,8 'scaeua res dicitur mala, quasi sinistra'). Nourai's gloss 'sinister' is thus the later, Grecising sense.\",\n          \"derivation_fa\": \"لاتین scaevus «چپ» از ایتالیایی آغازین *skaiwos و آن از هندواروپایی *skeh₂iwós، درست به همان ساخت laevus در برابر λαιός یونانی. در لاتین بیشتر کاربرد فال‌بینانه دارد: scaeva «فالی که از سمت چپ می‌آید»، bona scaeva «فال نیک»، لقب Scaeva «چپ‌دست» و طلسم scaevola که وارّو (زبان لاتین ۷٬۹۷) شرح داده است؛ و چون در فال‌گیری رومی سمت چپ را خجسته می‌شمردند، scaevus هم معنی «خجسته» داشت و هم، زیر تأثیر σκαιός یونانی، معنی «ناشی» و «شوم» (فستوس ۴۴۳٬۸: «scaeua res dicitur mala, quasi sinistra»). پس معنی «sinister» که نورایی آورده معنای متأخر و یونانی‌مآبانه است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/scaevus\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"IEC:1146\", \"status\": \"supports\", \"note\": \"Mann p.1146 s.v. skaiuos: 'Lat. scaevus \\\"lefthand, sinister, unlucky\\\"'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet, s.v. scaeuus (LAT.txt 55705ff.)\", \"stance\": \"supports\", \"note\": \"'scaeuus, -a, -um: gauche, qui est à gauche ... Comme laeuus, a le sens de \\\"d'heureux augure, favorable\\\" ... D'autre part, comme sinister, l'adj. scaeuus, peut-être d'après le grec σκαιός, a pris ... le sens de \\\"gauche, maladroit\\\" et aussi de \\\"défavorable, sinistre\\\".'\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II 537\", \"stance\": \"supports\", \"note\": \"'Gr. σκαιός = lat. scaevus'.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"šǔx «شوخ»\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The Persian branch is the weak link of this chart. Nourai's own source says only 'Per. cf. šūx, adj. \\\"lewd, impudent\\\"' — Mann marks it 'cf.', a tentative comparison, and the reference Mann himself gives for the root, Walde-Pokorny II 537, contains no Iranian word at all. Phonologically the equation does not work: PIE *skeh₂iwós would yield a New Persian form in *šēw/*šīw (cf. the treatment of *ai and of final *-wa-), never a form ending in -x; nothing in the root accounts for the Persian خ. Semantically the Persian evidence points elsewhere: Mo'in's own entry, which Nourai cites (MON:2085), gives as the NOUN sense 'چرک، ریم' (dirt, filth, pus) and only then the adjective senses 'گستاخ، بی‌حیا؛ زنده‌دل، خوشحال؛ دزد؛ خوشگل', and Amid likewise lists 'چرک بدن، چرک لباس' with a classical verse (Khosravi); i.e. the oldest attested sense of شوخ is 'grime', from which 'brazen, impudent' develops ('shameless' as 'unwashed'), not 'left/awkward'. Neither Horn nor Hübschmann nor Aryanpur has the word, and Wiktionary's entry for شوخ carries no etymology at all, so no positive alternative is established — but the derivation as drawn is not supported by anything except Mann's own hesitant 'cf.' and should be treated as rejected rather than accepted.\",\n          \"derivation_fa\": \"شاخهٔ فارسی این نمودار سست‌ترین حلقهٔ آن است. مأخذ خود نورایی، یعنی مان (ص ۱۱۴۶)، تنها می‌نویسد «Per. cf. šūx» و همین «cf.» نشان می‌دهد که سنجشی احتیاطی است؛ افزون بر آن، مرجعی که مان به آن ارجاع می‌دهد (والده–پوکورنی ج۲ ص۵۳۷) هیچ واژهٔ ایرانی ندارد. از نظر آوایی این برابرنهاد درست درنمی‌آید: *skeh₂iwós هندواروپایی در فارسی نو باید چیزی مانند *شیو/*شیب بدهد، نه واژه‌ای با خِ پایانی؛ هیچ‌چیز در ریشه توضیح‌دهندهٔ «خ» نیست. از نظر معنایی هم گواهی فارسی به سوی دیگری اشاره دارد: در فرهنگ معین (همان MON:2085) نخستین معنی اسمی «چرک، ریم» است و سپس صفت‌ها («گستاخ، بی‌حیا؛ زنده‌دل؛ دزد؛ خوشگل»)، و عمید نیز «چرک بدن، چرک لباس» را با شاهدی از خسروی می‌آورد؛ یعنی کهن‌ترین معنی «شوخ» آلودگی و چرک است و «بی‌شرم و گستاخ» از همان‌جا آمده، نه از «چپ و ناشی». هرن، هوبشمان و آریان‌پور این واژه را ندارند و ویکی‌واژه هم ریشه‌شناسی‌اش را خالی گذاشته است؛ پس ریشه‌شناسی جایگزینِ استواری در دست نیست، ولی پژوهش امروزی این اشتقاق را نمی‌پذیرد و باید آن را رد شده دانست.\",\n          \"sources\": [\n            \"https://abadis.ir/fatofa/%D8%B4%D9%88%D8%AE/\",\n            \"https://en.wiktionary.org/wiki/%D8%B4%D9%88%D8%AE\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"IEC:1146\", \"status\": \"partial\", \"note\": \"IEC.txt leaf 635 (printed 1146): under 'skaiuos' Mann writes 'Per. cf. šūx, adj. \\\"lewd, impudent\\\"' — the word is there, but flagged as a mere comparison ('cf.') and placed before the securely cognate Greek and Latin forms.\"},\n            {\"ref\": \"MON:2085\", \"status\": \"partial\", \"note\": \"Mo'in's entry for شوخ, read via abadis.ir (section فرهنگ معین): '(اِ ) چرک ، ریم . (ص . ) ۱ - گستاخ ، بی حیا. ۲ - زنده دل ، خوشحال . ۳ - دزد. ۴ - خوشگل .' — Mo'in gives the word and Nourai's glosses but attaches NO origin tag (unlike his [ایتا.], [ع.], [په.] tags elsewhere), so he offers no support for an Indo-European derivation.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"WLD\", \"where\": \"Bd. II 537\", \"stance\": \"contradicts\", \"note\": \"The lemma Mann cites for this root, 'skaiuos \\\"link\\\"', lists only Gk. σκαιός and Lat. scaevus (plus a Norwegian dialect form it rejects); no Iranian cognate is given, so Walde-Pokorny does not know a Persian member of this family.\"},\n            {\"src\": \"HRN\", \"where\": \"Grundriss der neupersischen Etymologie\", \"stance\": \"silent\", \"note\": \"grep of HRN.txt for šūx / 'Schmutz' finds no entry for شوخ.\"},\n            {\"src\": \"HUB\", \"where\": \"Persische Studien\", \"stance\": \"silent\", \"note\": \"grep of HUB.txt for sux/šūx returns only pasux, surx, suxan — no شوخ.\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e Riše-hā-ye Hend-o-Orupāyi\", \"stance\": \"silent\", \"note\": \"grep of ARY_pages.txt for شوخ returns nothing; this independent modern Persian IE-roots dictionary does not claim an Indo-European origin for the word.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-09-14T02:15:15.190Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe/data/verification/page-451.json (file state is current in your context — no need to Read it back)
```


## [2026-09-14T02:15:17.768Z] TOOL CALL #86: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-451.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 451"
}
```


### [2026-09-14T02:15:19.132Z] TOOL RESULT

```
JSON OK
nodes verified: 17/17
node verdicts: {'plausible': 3, 'confirmed': 12, 'transcription_suspect': 1, 'disputed': 1}
root verdicts: {'plausible': 2, 'confirmed': 1}
ref checks: {'supports': 17, 'not_checked': 5, 'partial': 5, 'not_found': 1}
books consulted: {'partial': 3, 'supports': 26, 'silent': 13, 'contradicts': 1} | by book: {'KLN': 7, 'PHD': 5, 'SYN': 4, 'WLD': 4, 'NYB': 3, 'HUB': 3, 'LAT': 3, 'BRT': 2, 'AHD': 2, 'HRN': 2, 'ARY': 2, 'ISS': 1, 'WEB': 1, 'DEV': 1, 'SKT': 1, 'POK': 1, 'CHEUNG': 1}
```


## [2026-09-14T02:15:41.712Z] AGENT

Done — `/home/sfmqrb/git/rishe/data/verification/page-451.json` written; `verify_check.py 451` reports 17/17 nodes, 0 PROBLEM lines.

**PDF page 451 (book 421) — 3 entries (1 redirect skipped), 17 nodes**
- Node verdicts: 12 confirmed, 3 plausible, 1 transcription_suspect, 1 disputed
- Root verdicts: 1 confirmed (Skaivos), 2 plausible (Skai, Skaif/Skaip)

Flagged items:
- **transcription_suspect — Skai #3 `čâyâ, asaya` [Avestan]**: `čâyâ` is not Avestan but Sanskrit chāyā́-, copied straight out of Pokorny 917 where it stands two lines above Av. a-saya-; Iranian *sḱ gives s-/θ-, never č-, and Buck writes the simplex starred (`Av. *saya-`). `error_in: book` — the printed page shows exactly what the JSON has (image saved to `data/verification/sources/refs/ocr/BOOK/451.png`).
- **disputed — Skaivos #3 `šǔx «شوخ»`**: Mann (IEC 1146) only writes "Per. cf. šūx", and his own reference WP II 537 has no Iranian member at all; *skeh₂iwós cannot give NP -x; Mo'in (the cited MON:2085) gives no origin tag and makes the primary sense «چرک، ریم» 'filth', from which 'brazen' develops. Horn, Hübschmann, Aryanpur and Wiktionary are silent — no alternative etymology is established, but the drawn one fails.
- **plausible — root Skai**: Nourai merges two adjacent Pokorny lemmas, `(s)kai-(d-),(t-)` "shining, bright" (916-917, whence Av. čiθra-) and `sḱāi-/sḱəi-/sḱī-` "glimmer; shadow" (917-918, whence sāya, σκιά/σκηνή, *skīnan); modern reconstruction keeps *kʷey- and *sḱeh₂(i)- apart. Watkins does too.
- **plausible — Skai #1**: the book prints Avestan as `čitra` (Sanskrit-style); the real form is čiθra-. Also Bartholomae (AiW 587-588) splits ¹čiθra- 'visible, face' from ²čiθra- 'seed, lineage' and calls their identity "unwahrscheinlich", whereas Nourai glosses them as one word.
- **plausible — Skai #9/#10 (senâriyo / scene, scenario)**: scenario comes from Italian, not French — Mo'in himself tags سناریو `[ایتا.]` and Klein/Etymonline give It. scenario < Late L. scēnārius (Eng. 1868). The chart's French node is right for *scene* only.

Reference notes for the owner (not extraction errors): `FFD:63` on the Pahlavi box should be `FFD:64` (that is where Abolqasemi puts `شکیب < MP škēb < OIr *skaip-a`); `AHD` on the Latin `scaena` node is not verifiable — Watkins 1985 has no SCENE entry. Everything else checked out page-exact: POK 916/700, KNT 184 (`çiça- 'seed, lineage': Av. čiθra-, NPers. čihr`), HRN 154 no. 695 (`sāye`), SOD ~367 entry 9104 (`sāyak < *sāyaka-`), BQT 674/2047/2336 (incl. the Daqiqi couplet the chart quotes), IEC 1146, WLD2 537.

**No extraction errors found** — the JSON reproduces the printed page faithfully, including the empty French pass-through box and both poetry quotes.
