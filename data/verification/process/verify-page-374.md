# Verification process log — verify-page-374


## [2026-09-07T20:16:18.155Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 374 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-374.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-374.json. Write /home/sfmqrb/git/rishe/data/verification/page-374.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 374` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T20:16:20.183Z] AGENT

I'll start by reading the instructions.


## [2026-09-07T20:16:20.869Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T20:16:20.884Z] TOOL RESULT

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


## [2026-09-07T20:16:21.569Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-374.txt"
}
```


### [2026-09-07T20:16:21.597Z] TOOL RESULT

```
1	=== PDF page 374 (book page 344) ===
2	--- entry 0 ---
3	ROOT Ombh -> redirect to Nobh
4	--- entry 1 ---
5	ROOT Ombhro -> redirect to Nebh
6	--- entry 2 ---
7	ROOT [Indo-European] Ome : to move with energy  (refs POK:778)
8	#1 (parent #0) [Avestan] refs=POK:778; SYN:298 | ama : strength, attack (injury) force ; amâ-yavâ : injury, annoyance, grief ; arša-ama : with power of a bear ☞Rktho
9	  #2 (parent #1) [Persian] refs=BQT:31 | Aršâm «ارشام» : "strong as a bear", a male name | extra: آرشام
10	#3 (parent #0) [Sogdian] refs=SOD:6 | âm`n : power, force, strength
11	--- entry 3 ---
12	ROOT Ono -> redirect to An 2
13	--- entry 4 ---
14	ROOT Onogh -> redirect to Nogh
15	--- entry 5 ---
16	ROOT [Indo-European] Op : work, produce in abundance  (refs POK:780)
17	#1 (parent #0) [Avestan] refs=POK:780 | hu-apah, hv-apah : good work ☞Su 1 ; afnah : possessions
18	  #2 (parent #1) [Persian] refs=HRN:111 | xŭb «خوب» : good, nice
19	  #3 (parent #1) [Sogdian] refs=SOD:436 | xwp : good
20	#4 (parent #0) [Germanic] refs=AHD | oft : frequently
21	  #5 (parent #4) [English] refs=None | often
22	#6 (parent #0) [Latin] refs=AHD; KLN | opus : work ; optimus : with most production or possessions ; co-op : plenty ; optîo : choice (from abundance) ; opi-facium : work to be done, duty ☞Dhě 2
23	  #7 (parent #6) [English] refs=None | opera, operate, maneuver ; optimum ; copy ; option ; office
24	  #8 (parent #6) [French] refs=None | 
25	    #9 (parent #8) [Persian] refs=MON |  | extra: اپرا ، مانور
26	--- entry 6 ---
27	ROOT Opi -> redirect to Epi
28	
```


## [2026-09-07T20:16:25.363Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/extracted/batch/page-374.json",
 "description": "Read source JSON for page 374"
}
```


### [2026-09-07T20:16:25.401Z] TOOL RESULT

```
{
  "pdf_page": 374,
  "book_page": 344,
  "entries": [
    {
      "root": {"name": "Ombh", "redirect": "Nobh"},
      "nodes": []
    },
    {
      "root": {"name": "Ombhro", "redirect": "Nebh"},
      "nodes": []
    },
    {
      "root": {
        "name": "Ome",
        "lang": "Indo-European",
        "refs": "POK:778",
        "gloss": "to move with energy"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:778; SYN:298",
          "words": [
            {"translit": "ama", "gloss": "strength, attack (injury) force", "script": null},
            {"translit": "amâ-yavâ", "gloss": "injury, annoyance, grief", "script": null},
            {"translit": "arša-ama", "gloss": "with power of a bear", "script": null, "see": ["Rktho"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:31",
          "words": [
            {"translit": "Aršâm", "gloss": "\"strong as a bear\", a male name", "script": "ارشام"}
          ],
          "script_extra": "آرشام",
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Sogdian",
          "refs": "SOD:6",
          "words": [
            {"translit": "âm`n", "gloss": "power, force, strength", "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {"name": "Ono", "redirect": "An 2"},
      "nodes": []
    },
    {
      "root": {"name": "Onogh", "redirect": "Nogh"},
      "nodes": []
    },
    {
      "root": {
        "name": "Op",
        "lang": "Indo-European",
        "refs": "POK:780",
        "gloss": "work, produce in abundance"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:780",
          "words": [
            {"translit": "hu-apah, hv-apah", "gloss": "good work", "script": null, "see": ["Su 1"]},
            {"translit": "afnah", "gloss": "possessions", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "HRN:111",
          "words": [
            {"translit": "xŭb", "gloss": "good, nice", "script": "خوب"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Sogdian",
          "refs": "SOD:436",
          "words": [
            {"translit": "xwp", "gloss": "good", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "oft", "gloss": "frequently", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "often", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD; KLN",
          "words": [
            {"translit": "opus", "gloss": "work", "script": null},
            {"translit": "optimus", "gloss": "with most production or possessions", "script": null},
            {"translit": "co-op", "gloss": "plenty", "script": null},
            {"translit": "optîo", "gloss": "choice (from abundance)", "script": null},
            {"translit": "opi-facium", "gloss": "work to be done, duty", "script": null, "see": ["Dhě 2"]}
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
            {"translit": "opera, operate, maneuver", "gloss": null, "script": null},
            {"translit": "optimum", "gloss": null, "script": null},
            {"translit": "copy", "gloss": null, "script": null},
            {"translit": "option", "gloss": null, "script": null},
            {"translit": "office", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 6,
          "lang": "French",
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Persian",
          "refs": "MON",
          "words": [],
          "script_extra": "اپرا ، مانور",
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {"name": "Opi", "redirect": "Epi"},
      "nodes": []
    }
  ]
}
```


## [2026-09-07T20:16:25.847Z] TOOL CALL #4: Bash

```json
{
 "command": "ls data/verification/ | head -30 && echo \"---\" && cat tools/verify_check.py | head -60",
 "description": "List verification dir and check script"
}
```


### [2026-09-07T20:16:25.898Z] TOOL RESULT

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
---
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
```


## [2026-09-07T20:16:30.572Z] TOOL CALL #5: Bash

```json
{
 "command": "sed -n 1,200p data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-07T20:16:30.617Z] TOOL RESULT

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
```


## [2026-09-07T20:16:32.587Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','SYN','BQT','SOD','HRN','AHD','KLN','MON','WLD','IEC','BRT','PHD','NYB','HUB','ARY','SKT','WEB','FSD','CHEUNG','KNT']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:400])\n\"",
 "description": "Inspect refs_online entries"
}
```


### [2026-09-07T20:16:33.940Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in 
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
CHEUNG null
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
```


## [2026-09-07T20:16:40.609Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | head -80 && echo \"=== POK files ===\" && ls -la POK*",
 "description": "List refs files"
}
```


### [2026-09-07T20:16:40.662Z] TOOL RESULT

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
=== POK files ===
-rw-rw-r-- 1 sfmqrb sfmqrb  981836 Sep  4 14:06 POK_01.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1137861 Sep  4 14:06 POK_02.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1170809 Sep  4 14:06 POK_03.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 3971883 Sep  4 14:06 POK_full.txt
```


## [2026-09-07T20:16:41.912Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"778\\|omə-\\|omǝ\" POK_full.txt | head -40",
 "description": "Grep POK for root omə"
}
```


### [2026-09-07T20:16:41.972Z] TOOL RESULT

```
18929:afar', taray Aor. 'take to one's heels, made oneself scarce' (Persson Beitr. 778 a 2); 
19415:References: WP. I 778, WH. 11 11 , 324 f., 852. 
19475:References: WP. I 778 ff., WH. I 378 f., 861, Schwyzer Gr. Gr. I 348, 595, 685. 
63760:Page(s): 778 
63799:Page(s): 778 
63850:Page(s): 777-778 
63861:Page(s): 778
```


## [2026-09-07T20:16:45.770Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '63700,63920p' POK_full.txt",
 "description": "Read POK_full around page 778"
}
```


### [2026-09-07T20:16:45.818Z] TOOL RESULT

```
Lithuanian akis^eye\ ak/{= Old Bulgarian oc/) 'die beiden Augen', Latvian acs'eye', 
Old Prussian ack/s Horn. PI. ' eyes ', Old Bulgarian oko {russ. okd). Gen. ocese, Du. oci 
'eye'; Lithuanian akylas^ attentive ', poln. Oit'aczj/c (lengthened grade) 'see, pay attention, 
perceive, see ', from which through suffix misunderstanding {ob : d): baczyclook out, pay 
attention, perceive, see'; of /7-stem serb. -Church Slavic o/r/70 'window'; compare engl. (Old 
Icelandic loanword) m'nd-owds., actually ' wind-eye'; 

Affiliation from Lithuanian akas^ Wuhne, hole in the ice ', Latvian aka' of dug wells ', 
russ. river name O/ra (different above S. 23), Lithuanian ekete {akete, akyte) ' in das Eis 
gehauenes Loch zum Wasserschopfen, Wuhne ', Latvian akate^ pit in the morass full of 
water ' probably: ' water eye ', compare ' sea eyes ' as a name of the Tatra Mountain 
lakes; 



Tocharian A ak, Du. asam, B ek, Du. esanev\. "eye'; A ak-ma/lace' ("eye + nose'); 
compare W.SchuIze Kl. Schr. 248. 

Maybe Sumerian igH^i: noun, eye(s); face; front. 

verb, to see 

prep., before, in front of 

References: WP. I 169 ff., WH. II 200 ff., Benveniste Origines 1 , 48, Schwyzer Gr. Gr. 1 , 

299, Petersson Heterokl. 121. 

Page(s): 775-777 

Root / lemma: o/-{e)- {*houl-(e)-) 

Meaning: to destroy 

Material: Gr. 6AAu|ji (*6A-vu:-[ji), Fut. oAsau) "spoil', 6A£Tr|(; " Exterminator', oAeku) 

"destroy', oKooc, (*6AoF6(;) " catastrophically '; 

Latin Sit'-o/eo "destroy'; perhaps with sek. /7-Umbrian hondu, holtu^ prosternito '; 

Hittite hullai-, hulliya- "fight, struggle', etc. 

References: WH. I 4 f. (the arrangement bestreitet), Couvreur H 143. 
Page(s): 777 

Root / lemma: om(e)so-s {* houm(e)so-^ 

Meaning: shoulder 

Material: Old Indie amsa-m. "shoulder'; Armenian us. Gen. usoy ds.; lengthened grade gr. 

u)p6(; ds. from *dmsos, compare £TT-ofjfja5iO(; by Theokr.; Latin umerusirom *omesos ds., 

Umbrian uze, onse' in umero '; Gothic ams ds. (Germanic *amsa-). Old Icelandic ass" 

ridge '; Tocharian A es "shoulder' ( *omso-), B antse ( *omeso-). 

References: WP. I 178, Pedersen Tocharian 250; W. Schuize KZ. 63, 28, WH. II 815. 

Page(s): 778 

Root / lemma: oma- {*houm9-) 

Meaning: to proceed with energy; to make firm; to suffer 

Material: Old Indie a/77/7/" presses, insures urgently, swears', themat. sam-amante^ they 

promise ' (: auv-opoaai), abhy-amJti^ torments, damages ', a/77/Va "tribulation, affliction, 

disease, malady' (: gr. avin), with themat. Creation of the 2. syllable amate' pressed ', 

amatra- "tight, firm', amavan- " boisterous, strong' = 



= Avestan amavant-' strong, mighty, vast, grand'. Old Indie ama-vn. "rush, impetuousness, 
hastiness ' = Avestan ama-^ power, strength, male power, attack strength ', Adj. "strong'. 
Old Indie amayati^ damages; it is damaged, ill ', amaya-rr\. "disease, malady'; Avestan 
amayava 'aii\\ct\on, hardship '; 

gr. ofjvufji, 6|jvuu) " swear ' (6|j6aai, 6[Jcb[J0Ka; Fut. opETiai neologism), auvopoaai (: Old 
Indie sam-amant^, hom. 6|JoiiO(; " tormenting, grievously ' (probably metr. lengthening 
from 6|JoFiO(;, to *6fJ0-Fa); avia, Ionian a\7ir| " distress ' (dissimil. from *aiJiFa, Sehwyzer 
Gr. Gr. 1,259,309); 

Old leelandie a/775 "plague, bother, annoy', amask^ take offenee, feel displeasure, 
struggle with ', nisi. a/77/"plague', amstr^ indefatigable work, strain, exertion ', amin. " 
uneeasing, esp. fruitless oeeupation with a thing', Norwegian a/77/5" struggle, work, esp. 
without sueeess ', Old leelandie PN Qmlungr, 

Amali\he name of East Gothie royal family, the Amalunge, Amulingeoi German and Old 
English heroie legend. Old High German Amal-olf\ Old High German e/77/z" continuously, 
perpetually ', emizzTg, emazzTg^ continuously, pertinaciously'. Modern High German emsig 
" eager'. 

Toeharian A. amiskanne " discontent ', B omaskem "evil, bad'. 

References: WP. 11 78 f. 
Page(s): 778 

Root / lemma: om- {*houm-) 

Meaning: raw, bitter, *sweet 

Note: reduced grade oin- 

Root/ lemma: om-{*hamef}\ "raw, bitter, *sweet' : Root/ lemma: sem-1\ "to pour' : Root/ 

lemma: sem-3\ "summer'. Old Indie amia-, ambla-^sour, sorrel, Oxalis acetosella ' : gall. 

samor{ios] "summer months', samolus^ sour, sorrel, Oxalis acetosella '. 

Material: Old Indie amIa-, ambia- "sour, sorrel, Oxalis acetosella ' (= maked. appo-, 

Germanic *ampra-), zero grade amra-m. " Mango tree ', ama- "raw, unripe ' (= gr. u)|j6(;), 

amad- " eating raw flesh '; skyth. VN ApaSoKOi from Iran. *amad-aka- " raw meat eater '; 

Note: 

Phonetically the closest cognate to Old Indie amIa-, ambIa- "sour' is alb. Geg amIa, Tose 

emb(e)la "sweet' common alb. shift m > mb. Clearly the cognate of Old Indie amIa- "sour' 

derived from alb. Geg a/77a "mother', t'amle^ sour milk (of the mother), breast milk '. 



Armenian zero grade /7^/77Yaw, cruel, savage'; 

maked. appo- " astringent ', apapu opiyavov Hes.; 

gr. u)|j6c; 'raw, cruel, savage', u)[jr|aTn(; " eating raw meat ' etc. (= Old Indie amad-Wxih 
already Indo Germanic contraction from dmo-an6 ed-'eat'); 

alb. tam/e'{sour) milk', ambele, emb/e' sweet', temb/e' bile ' (article /-); 

Latin amarus' bitter'; Old Irish 0/77 >aw', cymr. of 6s., in addition Old Irish umfaje' 
copper, ore' = cymr. efydd^ copper, bronze ' ( *omiJo^\ 

Germanic *a/77/7/'a- (from *ambra-< *am-ro-) in Dutch a/TT/Oe/"' sharp, bitter, unripe ', Old 
Icelandic apr{*ampraR) 'sharp', Subst. Old English ampre. Old High German ampfaro\ 
(Sauer)ampfer '; doubtful Old English d/77m. " rust ', omei. ' Rotlauf ', Old Icelandic amai., 
amu-sotti. " Rose ' (disease, malady), amr^ reddish brown ', Modern High German Ahm, 
Ohm ' Rotlauf '; 

Latvian amuols " sorrel, Oxalis acetosella '. 

References: WP. I 179, WH. I 35, Frisk nominal formation 14. 
Page(s): 777-778 

Root / lemma: ond- pd- {* hound-) 
Meaning: stone 

Material: Old Indie adri-^ stone, esp. used to hit the Soma; cliff, mountain; rock ', Old pers. 
Ark-adhs {!); Middle Irish ond, onn. Gen. uinde {stem *ondes-) n. ' stone, rock', (common 
Celtic -ns-, -nt- > -nn-). 

Maybe lllyrian TN. {*Adhei) Ardiei 
References: WP. 11 81. 
Page(s): 778 

Root / lemma: oner- {*houner-) 

Meaning: dream 

Grammatical information: older r/n-stevn 

Material: Armenian anurj^6xeaxx\' {*ondr-io-, compare gr. t£K|J(jop : TSKpap "mark, token, 

sign'); gr. ovap Nom. Akk. n. 'dream' and Adv. 'in dream'; 6v£ipo(;, -ov, Aeolic 6voipo(;, 

Cretan avaipo(; (probably through influence of the preposition av-) 'dream'. Gen. Attic 



Ionian ovsiparot; (originally *6vaT0(;); alb. gegh. aderre, Tosc enderre' dream' (onr/'o-) 

[common alb. n- > nd-]. 

References: WP. I 180, Meillet Esquisse de l'Arm.2 150. 

Page(s): 779 

Root / lemma: ong- {better ang-) {*houng-) 

Meaning: coal 

Note: 

Root/ lemma: egnis. ognis: fire' derived from Root/ lemma: ong- [better ang-) {*heng-)\ 

coal < Root/ lemma: ok"-: "to see; eye' 

Material: Old Indie ahgara-xx\. "coal', npers. ang/stds.; gael. nir. a/ngea/l'\gbt, fire'; 

Baltic-Slavic. *angli-. Old Prussian anglis, Lithuanian anglis, Latvian uog/e'coaV 
(Latvian uogle\s neologism); Old Church Slavic ggib m. ds., but russ. ugolb, Serbo- 
Croatian ugalj, poln. wggields. etc. (./io-stem). 

Maybe alb. thengjiir {*coa\) ash' similar to alb. thua^ nail', thundra, thunder^ hoof 
(common alb. Slavic u > e). 

References: WP. I 181, Macbain Etym. Gael. Diet. 8 f., Trautmann 8, H. Wagner, Lexis 3, 

134. 

Page(s): 779 

Root / lemma: ong"- {*ong''h^ 

Meaning: to anoint, dark ointment 

Material: Old Indie anj-, anaktii^. PI. anjanti) " anoints, coats, decorates ', participle Perf. 

akta-. Pass, ajyate; anjanam^ the ointments, ointment ', anjas- n. " ointment ', anjf-^ 

anointing '; m. n. " ointment, jewellery', ajyamn. " sacrificial lard ' {a+ aJya-< *ng"io-)\ 

Armenian aucanem^ anoint, smear, rub' (compare Meillet Esquisse de I'Arm.^ 37);
```


## [2026-09-07T20:17:28.139Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Page(s): 780\\|Page(s): 779-780\\|Page(s): 780-781\" POK_full.txt",
 "description": "Find POK page 780 markers"
}
```


### [2026-09-07T20:17:28.188Z] TOOL RESULT

```
63997:Page(s): 780 
64065:Page(s): 780
```


## [2026-09-07T20:17:29.029Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"^op-\\|Root / lemma: op-\" POK_full.txt | head",
 "description": "Find op- lemma in POK"
}
```


### [2026-09-07T20:17:29.101Z] TOOL RESULT

```
64025:Root / lemma: op-1 {* hue-p-) 
64067:Root / lemma: op-2
```


## [2026-09-07T20:17:32.163Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '64020,64100p' POK_full.txt",
 "description": "Read POK op-1 entry"
}
```


### [2026-09-07T20:17:32.218Z] TOOL RESULT

```
Root / lemma: opi 
See also: see below epi. 
Page(s): 781 

Root / lemma: op-1 {* hue-p-) 

Meaning: to work, perform 

Material: Old Indie apas-u. "work' (= Latin opus), Avestan hv-apah-'goo6 work 

(verrichtend)'; apas-n. "work, religious action'; apnas-n. "yield, property, possession ', 

Avestan afnah-vant- " richly in possession '; 



gr. {* h3^\^T^\/^\) 6|jnvr| f. "nourishment, food, BromicnT ', opTTVioq " nourishing '; 

The origin of labialized Old laryngeals: 

common Armenian Celtic *hue- > gw- > g- ; Albanian gw- > v-. 

Maybe in e-grade alb. {*hueper) veper' work' : Latin opus, -e/75"work'. 

Latin opus, -er/s'work, occupation, action, work', opus est ^ it is necessary ', whereof 
opero, -a/ie'work', Oscan upsannam^ operandam ', (under the influence of common Celtic 
-ns-, -nt- > -nn-), upsatuh senti^ fact! sunt '), Perf. upsed^ fecit ', uupsens ' fecerunt ', 
(lengthened grades Perf. as in Latin odl), Umbrian osatu^ facito ', Paelignian upsaseter^ 
fieret '; Latin ops, O/O/s "fortune, richness, power; help, assistance ', by Ennius also " 
endeavor, service ', officium ' obligation ' < *opi-ficium ' working performance ', Ops " 
(Latin: "Plenty") was a fertility deity and earth-goddess in Roman mythology of Sabine 
origin ', inops, cdpia{*co-opia), opulentus^ incredibly rich in property, mighty ', probably 
also opt/mus't\r\e best' (actually "the wealthiest') ; perhaps the name the Oscl, OpscT, 
'OniKoi as ' admirers of the Ops' and Latin omnis 'all, whole, each, every ' ( *op-ni-s); 
perhaps Old Irish somme^ncW, domme^ poor' {su-, dus-op-smjo-); 

Old English efnan. Old Icelandic efna^ work, do'; lengthened grade Old High German 
uobo^ land farmer', uoben^ place at the work, exercise, revere, worship ', Modern High 
German ijben. Old High German uobam. PI. " celebration ', Middle High German uop^ 
practice, agriculture ', Old Saxon dbian^\\o\6 festivities'. Old Icelandic 0fa^ train, practice ', 
j0/^"vast, grand, violent'. Old Icelandic efna^ commit ', efni^ material, stuff for something '; 
about Old Icelandic afr power ' etc. see above S. 52; Hittite happinahh- ' make rich '. 

References: WP. I 175 f., WH. II 209, 217 f. 
Page(s): 780 

Root / lemma: op-2 

Meaning: to choose; to suggest 

Material: Gr. snioijjoijai to sni-on- " choose, pick out, sort '; Latin *opere\s covered by 

*praed-op/ont {Festus p. 205 praedotiont) ' praeoptant '; derived *opid(n)^ expectation, 

opinion', wherefore Denominativum opTnor, -ari^ assume, imagine, mean' OyO/77/b "opinion, 

expectation '; Frequentativum to *opid, -ere\s Latin opto, -a/'e'wish', wherefore option. 

"free choice ', m. ' assistant '; 

Umbrian upetu^ optato ', opeterGen. ' lectT ', Oscan ufteis^ optatT '; 



Old Church Slavic za-(j)apTD " supposition ', ne-vhz-apbnh ' unexpectedly ' (compare 
Latin in-, nec-opTnus^ unexpectedly ', which are back-formations from inopTnatus); 

Tocharian A opyac, B epyac 'reason' (Iran, loanword?). 

References: WP. 1176 f., WH. II 212 f. 
Page(s): 781 

Root / lemma: o/b^o- 

Meaning: orphan; servant; work 

Note: 

' becomes an orphan, orphan '; out of it (Armenian gr. with -ano-, Celtic Germanic \n\Vc\Jo-
```


## [2026-09-07T20:17:41.078Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD op- ===\" && grep -n -i \"op-\\b\" AHD_watkins1985.txt | head -20; echo \"=== AHD often ===\"; grep -n -i \"often\\|ufta\" AHD_watkins1985.txt | head -20",
 "description": "Grep AHD Watkins for op- and often"
}
```


### [2026-09-07T20:17:41.139Z] TOOL RESULT

```
=== AHD op- ===
446:epi. Also opi. Near, at, against. 1. Latin ob, ob-, before, to, against: OB-. 2. Greek epi, on, over, at: EPI-. 3. Greek opisthen, behind, at the back: OPISTHOBRANCH, OPIS- THOGNATHOUS. 4, Zero-grade “pi-, on, in Greek piezein, to press tight (see sed-1). 5. Old Church Slavonic ob, on, in Russian oblast’, oblast: OBLAST. 6. Prefix *op- in *op-wer-yo-, to cover over (see wer-5). [Pok. epi 323.]
805:op-'. To work, produce in abundance. 1. Suffixed form *op-es- in Latin opus (stem oper-), work, with its denomi- native verb operari, to work, and secondary noun opera, work: OPERA!, OPERATE, OPEROSE, OPUS; COOPERATE, INURE, MANEUVER, MANURE, OFFICINAL. 2. Latin offi- cium, service, duty, business (< *opi-fici-om, “perform- ance of work”; -fici-, doing; see dhé-1). 3. Suffixed form *op-en-ent- dissimilated in Latin opulentus, rich, wealthy: OPULENT. 4. Suffixed form “*op-ni- in Latin omnis, all (< “abundant’”): OMNI-, OMNIBUS; OMNIUM- GATHERUM. 5, Suffixed (superlative) form *op-tamo- in Latin optimus, best (< ‘‘wealthiest’’): OPTIMUM. 6. Prefixed Latin form *co-op- (co-, collective and inten- sive prefix; see kom) in Latin cdpia, profusion, plenty: COPIOUS, COPY; CORNUCOPIA. [Pok. 1. op- 780.]
806:op-2. To choose. 1. Latin optid, choice (from *opere, to choose): OPTION. 2. Latin optdre (frequentative of “opere), to choose: OPT, OPTATIVE; ADOPT, CO-OPT. 3. Possibly suffixed form *op-yen- in Latin opindri, to be of an opinion: OPINE, OPINION. [Pok. 2. op- 781.]
938:skep-. Also kep-. Base of words with various technical meanings such as “to cut,” “to scrape,” “to hack.” 1. Germanic *skap- in: a. Old English gesceap (ge-, collective prefix; see kom), form, creation (< “cutting”): SHAPE; b. Old English -scipe, state, condition (collective suffix): -sHIP; c. Dutch -schap, “-ship,” condition (collec- tive suffix): LANDSCAPE. 2. Germanic ablaut variant *skOpo-, “thing cut out,” container, in Middle Dutch and Middle Low German schdépe, bucket for bailing water: scoop. 3. Germanic *skaftaz in Old English sceaft, rod of a spear: SHAFT! 4, Germanic expressive form *skabb- in: a. Old English sceabb, a scab, scratch: sHaBBy; b. Old Norse skabb, a scab: scaB. 5. Variant form *skabh- in: a. Germanic *skaban in (i) Old English sceafan, to scrape, pare away: SHAVE (ii) Old High German skaban, to scrape: SAPSAGO; b. Latin scabere, to scrape: SCABIES; c. suffixed form *skabh-ro- in Latin scaber, rough (< “scratched”’): SCABROUS; d. Greek skaphé, boat (< “thing cut out”): SCAPHOID; BATHYSCAPH. 6. Variant form *skap- in Latin scapula, shoulder blade (used as a tool for scraping): SCAPULA. 7. Variant form *kap- in: a. Latin capd, castrated cock: CAPON; b. Late Latin capuldre, to cut: SCABBLE. 8. O-grade form *kop- in: a. suffixed form *kop-yd- in Germanic *hapjo, a cutting tool, ax, sickle, in (i) Old High German hdppa, happa, sickle, akin to the Germanic source of Old Provencal apcha, small ax: PIOLET (ii) Medieval Latin hapia, ax, and Old French hache, small ax: HASH!, HATCHET; NUT- HATCH, QUEBRACHO; b. suffixed form *kop-yo- in Greek koptein, to strike, cut: COMMA; APOCOPE, SARCOPTIC MANGE, SYNCOPE; C. Russian kopat’, to hack, with de- rivative kop’e, lance, in kopeika, kopeck: KOPECK. 9. Pos- sibly zero-grade variant form *skup(h)- in Greek skuphos, a cup (but more likely of obscure origin): SCYPHISTOMA, SCYPHOZOAN. [Pok. 2. (s)kep- 931.] sker-!, Also ker-. To cut. I. Basic forms *sker-, *ker-. 1. Germanic *skeran in Old English scieran, sceran, to cut: SHEAR. 2. Germanic *skeraz in: a. Old English scéar, plowshare: SHARE?; b. Old English scearu, scaru, portion, division (but recorded only in the senses of “fork of the body,” “tonsure”): SHARE!. 3. Germanic *skér- in: a. *skér-6- and *sker-ez- in Old English scéar, scissors: SHEARS; b. compound *skér-berg-, “sword protector,” scabbard (see bhergh-') in Old High German scarberc, scabbard, akin to the possible Germanic source of Anglo- Norman escaubers, scabbard: SCABBARD. 4. Germanic *skur- in Old Norse skor, notch, tally, twenty: SCORE. 5. Germanic suffixed form *skar-jam in Old Norse sker, low reef (< “something cut off’’): scaR?. 6. Suffixed o-grade extended form *skord-o- in Germanic *skardaz in Old English sceard, a cut, notch: SHARD. 7. Extended form *skerd- in suffixed zero-grade form *skrd-o- in Germanic *skurtaz in: a. Old English scort, sceort, “cut,” short: SHORT; b. Old English scyrte, undergarment (< “cut piece”): SHIRT; c. Old Norse skyrta, shirt: SKIRT. 8. Germanic extended form *skerm- in: a. Old High German skirmen, to protect, akin to the source of Old French eskermir, to fight with a sword, fence: SKIRMISH; b. Middle Dutch scherm, shield: SCREEN. 9. Variant form *kar- in Latin caré (stem carn-), flesh: CARNAGE, CARNAL, CARNASSIAL, CARNATION, CARNIVAL, CARRION, CARUNCLE, CHARNEL, CRONE; CARNIVOROUS, INCAR- NATE. 10. Suffixed o-grade form *kor-yo- in Latin co- rium, leather (originally “piece of hide”): CORIACEOUS, CORIUM, CUIRASS, CURRIER; EXCORIATE. 11. Suffixed zero-grade form *kr-to- in Latin curtus, short: CURT, CURTAL, KIRTLE. 12. Suffixed o-grade form *kor-mo- in Greek kormos, a trimmed tree trunk: cor. 13. Suffixed o-grade form *kor-i- in Greek koris, bedbug (< “cutter”): corREopsis. II. Extended roots *skert-, *kert-. 1. Zero-grade form *krt- or o-grade form *kort- in Latin cortex, bark (< “that which can be cut off”): CORTEX; DECORTICATE. 2. Suffixed form *kert-snd- in Latin céna, meal (< “portion of food”): CENACLE. III. Extended root
979:in: a. Latin sollus, whole, entire, unbroken: SOLICITOUS; b. Latin sollemnis (second element obscure), celebrated at fixed dates (said of religious rites), established, relig- ious, solemn: SOLEMN. II. Variant form *sob-. 1. Suffixed zero-grade form *sb-u- giving *sal-u- in Latin saliis, health, a whole or sound condition: SALUBRIOUS, SALU- TARY, SALUTE. 2. Suffixed zero-grade form “slo-wo- giv- ing *sala-wo- in Latin salvus, whole, safe, healthy, uninjured: SAFE, SAGE?, SALVAGE, SALVO!, SAVE!, SAVE. [Pok. solo- 979.] sp6-1. To thrive, prosper. Contracted from *spea-. 1. Suf- fixed o-grade form *sp6-ti- in Germanic *spddiz in Old English spéd, success: SPEED. 2. Suffixed form *spé-s- in Latin spés (plural spérés), hope, with denominative spérdre, to hope: DESPAIR, ESPERANCE. 3. Suffixed zero-grade form “spo-ro- in Latin prosperus, favorable, prosperous (traditionally regarded as from pro spéré, according to one’s hope; pro-, according to; see per’): PROSPER. [Pok. 3. sp(h)éi- 983.] spé-?. Long, flat piece of wood. Contracted from *speo-. I. Basic form *spé-. 1. Germanic *spé-nu- in: a. Old English spén, chip of wood, splinter: SPOON; b. Old Norse spdnn, shingle, chip: SPANNEW. 2. Possibly Greek sphén, wedge (formation unclear; earliest Greek form *sphdan): SPHENE, SPHENO-. II. Suffixed zero-grade form *spa-dh-. 1. Germanic *spadan in: a. Old English spadu, digging tool: sPADE!; b. Middle High German spat (> German Spat), spar: SPATHIC. 2. Greek spathé, broad blade: SPADE?, SPATHE, SPATULA, SPAY. [Pok. sp(hjé- 980.] spei-. Sharp point. I. Basic form *spei-. 1. Germanic *spituz in Old English spitu, stake on which meat is roasted: sPIT?. 2. Germanic *spitja- in German spitz, pointed: spitz. 3. Germanic *spi-ra- in: a. Old English spir, slender stalk: SPIRE!; ACROSPIRE; b. possibly Mid- dle Dutch spierlinc, a small, slender fish, smelt, akin to the source of Old French esperlinge, smelt: SPARLING. 4. Germanic “spik- in Old Norse spik, nail, perhaps akin to the possible source of Middle English spyk, spike: SPIKE}. 5. Germanic *spil- in Middle Low German spile, wooden peg: SPILE, SPILL?. 6. Suffixed form *spei-nd in Latin spina (> Old French espin), thorn, prickle, spine: SPINE, SPINEL, SPINNEY; PORCUPINE. 7. Suffixed form *spei-kd in Latin spica, point, ear of grain: SPICA, SPICA, SPICULUM, SPIKE?. IT. Extended o-grade form *spoig- in Germanic *spaik6én- in Old English spdca, spoke: SPOKE}. [Pok. 1. sp(hjéi- 981.] (s)peik-. Bird’s name, woodpecker, magpie. 1. Suffixed form *peik-o- in Latin picus, woodpecker: PICARO, (PICKET), (PIKE!), (PIQUE). 2. Suffixed form *peik-d- in Latin pica, magpie: PICA2, PIE2. [Pok. (s)piko- 999.] spek-. To observe. I. Basic form *spek-. 1. Germanic *spehon in: a. Old French espier, to watch: ESPY, SPY; b. Germanic derivative *speh-6n-, watcher, in Old Italian spione, spy: ESPIONAGE. 2. Suffixed form *spek-yo- in Latin specere, to look at: SPECIMEN, SPECIOUS, SPECTA- CLE, SPECTRUM, SPECULATE, SPECULUM; ASPECT, AUS- PICE, CIRCUMSPECT, CONSPICUOUS, DESPISE, EXPECT, FRONTISPIECE, INSPECT, INTROSPECT, PERSPECTIVE, PROSPECT, RESPECT, (RESPITE), RETROSPECT, SUSPECT. 3. Latin speciés, a seeing, sight, form: SPECIES; ESPE- CIAL. 4, Latin -spex (< *-spek-), “he who sees,” in: a. haruspex, diviner (see ghere-); b. auspex, augur (see awi-). 5, Suffixed form *spek-d- in Latin (denominative) déspicari, to despise, look down on (de-, down; see de-): DESPICABLE. 6. Suffixed metathetical form *skep-yo- in Greek skeptesthai, to examine, consider: SKEPTIC. IT. Ex- tended o-grade form “spoko- metathesized in Greek skopos, one who watches, also object of attention, goal, and its denominative skopein (< *skop-eyo-), to see: SCOPE, -SCOPE, -SCOPY; BISHOP, EPISCOPAL, HOROSCOPE, TELESCOPE. [Pok. spek- 984.] spel-'. To split, break off. 1. Extended form *speld- in Germanic *spilt- in Middle Dutch spelte, wheat (prob-
1096:5. Greek trias, the number three: TRIAD. 6. Greek trikha, in three parts: TRICHOTOMY. 7. Greek compound triérés, galley with three banks of oars, trireme (-érés, oar; see era-'): TRIERARCH. 8. Suffixed form “*tri-to- in Greek tritos, third: TRITIUM; TRITANOPIA. 9. Compound form *tri-pl-, “threefold” (*-pl- < combining form *-plo-; see pel-3), in Greek ¢triploos, triple: TRIPLE. 10. Compound form *tri-plek-, “threefold” (*-plek-, -fold; see plek-), in Latin triplex, triple: TRIPLEX. 11. Compound form *tri-st-i, “third person standing by” (see sta-), in Latin testis, a witness: TESTAMENT, (TESTIMONY); ATTEST, CONTEST, DETEST, OBTEST, PROTEST, TESTIFY. 12. Per- sian si, three: straR. III. Extended zero-grade form “iris, “thrice.” 1. Latin ter, thrice: TERN?; TERPOLYMER. 2. Greek tris, thrice: TRISOCTAHEDRON. 3. Suffixed form *tris-no- in Latin trini, three each: TRINE, (TRINITY). IV. Suffixed o-grade form *troy-o- in Russian troje, three: TROIKA. [Pok. trei- 1090.] trem-. To tremble. Possibly related to trep-' and tres- through a hypothetical base *ter-. Latin tremere, to shake, tremble: TREMENDOUS, TREMOR, TREMULOUS. [Pok. trem- 1092.] trep-'. To tremble. Possibly related to trem- and tres- through a hypothetical base *ter-. Latin trepidus, agi- tated, alarmed: TREPID; INTREPID. [Pok. 1. trep- 1094.] trep-2. To turn. 1. Greek trepein, to turn: -TROPOUS; APOTROPAIC, TREPONEME. 2. O-grade form *trop- in: a. suffixed form *trop-o- in Greek tropos, a turn, way, manner: TROPE, TROPO-, TROVER; CONTRIVE, (RE- TRIEVE); b. suffixed form *trop-d- in Greek tropé, a turning, change: TROPHY, TROPIC; ENTROPY. [Pok. 2. trep- 1094.] tres-. To tremble. Possibly related to trem- and trep-1 through a hypothetical base *ter-. Metathesized form *ters- in o-grade suffixed (causative) form *tors-eyo- in Latin terrére, to frighten (< “to cause to tremble”), with vowel e from terror (< *ters-os-), terror: TERRIBLE, TERROR; DETER, TERRIFIC. [Pok. tres- 1095.] treud-. To squeeze. 1. Suffixed o-grade form *troud-o- in Germanic *thrautam in Old English thréat, oppression, use of force: THREAT. 2. Variant form *trid- in Germanic “thristjan in Old Norse thrysta, to squeeze, compress: THRUST. 3. Latin tridere, to thrust, push: ABSTRUSE, EXTRUDE, INTRUDE, OBTRUDE, PROTRUDE. [Pok. tr-eu-d 1095.] trozdo-. Thrush. 1. Germanic *thrust- in Old English throstle, thrush: THROSTLE. 2. Germanic *thruskj6n- in Old English thrysce, thrush: THRUSH}. 3. Zero-grade reduced form *trzdo- in Latin turdus, thrush: STURDY. 4. Perhaps altered in Greek strouthos, sparrow, ostrich: STRUTHIOUS; (OSTRICH). [Pok. trozdos 1096.] tu-. Second person singular pronoun; you, thou. 1. Lengthened-grade form “ti (accusative “te, *tege) in Germanic *thii (accusative *theke) in Old English thi (accusative thec, thé), thou: (THEE), THOU!. 2. Suffixed extended form *éwjei-no- in Germanic *thinaz in Old English thin, thine: THINE, THY. [Pok. tu- 1097.] twei-. To agitate, shake, toss. 1. Extended form *tweid- in Germanic *thwit- in: a. Old English thwitan, to strike, whittle down: WHITTLE; b. Middle Dutch duit, a small coin (? < “piece cut or tossed off”): DorT. 2. Extended form *tweis- in Greek seiein, to shake: SEISM, SISTRUM. [Pok. 2. tuei- 1099.] twengh-. To press in on. Germanic *thwang- in: a. Old English thwong, thwang, thong, band (< “constraint”): THONG; b. by-form *twangjan in Old English twengan, to pinch: TWINGE. [Pok. twengh- 1099.] twer-', To turn, whirl. Zero-grade *tur-. I. Variant form *stur-. 1. Suffixed form *stur-mo- in Germanic *sturmaz, storm (< “whirlwind”), in Old English storm, storm: STORM. 2. Germanic *sturjan in Old English styrian, to move, agitate: STIR!. II. Suffixed form *tur-bd in Greek turbé, tumult, disorder (> Latin turba, disorder, turbé, spinning top, and turbdre, to confuse, disorder): (TROU-
1151:*op-wer-yo- (*op-, over; see epi) in Latin operire, to cover: COVER, OPERCULUM. II. O-grade form *wor-. 1. Germanic *war-nén in Old English war(e)nian, to take heed: WARN. 2. Germanic *war- in: a. (i) Old French garant, warrant, authorization: GUARANTY (ii) Old North French warant, warrant, and warantir, to guarantee: WARRANT, (WARRANTEE), WARRANTY; b. Old French garer, to guard, protect: GARAGE; c. Old French g(u)arir, to defend, protect: GARRET, GARRISON; d. Old North French warenne, enclosure, game preserve: WARREN; e. Old French g(ujarnir, to equip: GARMENT, GARNISH. [Pok. 5. uer- 1160.] wer-S, Also wera-. To speak. Variant *wré-, contracted from *wreo-. 1. Suffixed zero-grade form *wr-dho- in Germanic *wurdam in Old English word, word: worD. 2. Suffixed form *wer-dho- in Latin verbum, word: VERB, VERVE; ADVERB, PROVERB. 3. Suffixed form *wer-yo- in Greek eirein, to say, speak: IRONY. 4. Variant form *wré- in suffixed form *wré-tor- in Greek rhétér, public speaker: RHETOR. [Pok. 6. wer- 1162.] wer-7. To burn. Suffixed lengthened o-grade (causative) form *w6r-yo- in Russian varit’, to boil: saMovarR. [Pok. 12. wer- 1166.] wer-®, Squirrel. Reduplicated expressive form *wi-wer(r)- in Latin viverra, a ferret: VIVERRINE. [Pok. 13. uer- 1166.] wér-. Water. Suffixed zero-grade form *dr-ind- in Latin irina, urine: URINE. [In Pok. 9. au(e)- 78.] were-', Wide, broad. Suffixed form *wer(a)-u- metathe- sized in Greek eurus, wide: EURY-; ANEURYSM, EURYD- IcE. [Pok. 8. wer- 1165.] were-2, To find. Variant *wré-, contracted from *wrea-. Reduplicated form *we-wré- in Greek heuriskein (first person singular perfect indicative active heuréka), to find: EUREKA, HEURISTIC. [Pok. 4. ver- 1160.] werg-. To do. I. Suffixed form *werg-o-. 1. Germanic *werkam, work, in: a. Old English weorc, werc, work: work; b. Old High German werc, work: (BOULEVARD),
1217:ADDER nétr- ADDICT deik- ADDUCE deuk- -ADELPHOUS gWelbh- ADEMPTION em- ADENO- engW- ADEPT ap-1 ADHERE ghais- ADIABATIC gWa- ADIEU delw- ADIT ei-1 ADJACENT yé- ADJECTIVE yé- ADJOIN yeug- ADJOURN deiw- ADJUDICATE yewes- ADJURE yewes- ADJUST yeug- ADJUVANT ad- ADMIRE smei- ADMIT (s)meit(9)- ADMIX meik- ADMONISH men-t ADNATE gene- ADNEXA ned- ADO ad- ADOLESCENT al-3 ADOPT op-2 ADORE Or- ADORN ar- ADRENERGIC werg- ADSCITITIOUS skei- ADSORB srebh- ADULT al-3 ADULTERATE al-1 ADULTERINE al-1 ADULTERY al-1 ADUMBRATE andho- ADUST eus- ADVANCE ant- ADVECTION wegh- ADVENT gWa- ADVENTITIOUS gWa- ADVENTURE gWa- ADVERB wer-6 ADVERSE wer-3 ADVICE weid- ADVISE weid- ADVOCATE wekw- AECIUM weik-3 AEDES swad-
1394:CONVOLVE wel-3 CONVULSE wel-4 cook pekw- cOoKY kak-2 cooL gel-3 COOPER ku- COOPERATE op-1 CO-OPT op-2 COORDINATION ar- COPE! kel-1 COPEPOD kap- COPIOUS op-1 COPRO- kekw- COPULA ap-! COPULATE ap-1 COPY op-1 CORACIIFORM ker-2, merph- CORACOID ker-2 CORBEL ker-2 CORBINA ker-2 CORD ghere- CORDATE kerd-1 CORDIAL kerd-1 CORDIFORM kerd-1 CORDON ghere- COREOPSIS sker-! CORGI kwon- CORIACEOUS sker-1 CORIUM §sker-1 cOoRM sker-! CORMORANT ker-2 CORN! gre-no- CORN2 ker-1 CORNEA ker-1 CORNEL ker-6 CORNEOUS ker-1 CORNER ker-1 CORNET ker-1 CORNICULATE ker-1 CORNIFICATION ker-1 CORNU_ ker-1 CORNUCOPIA op-! CORONA sker-3 CORONOID  sker-3 CORPORAL! kWrep- CORPORAL’ kWrep- CORPORATE kWrep- CORPOREAL kWrep- CORPOSANT kWrep-, sak- CORPS kWrep- CORPSE kWrep- CORPULENCE kWrep- CORPUS krep- CORPUSCLE kWrep- CORRADE réd- CORRECT reg-! CORRIDOR kers-2 CORRIE kWer-2 CORROBORATE reudh-! CORRODE réd- CORRUGATE ruk-2 CORRUPT reup- CORSAGE kWrep- CORSAIR kers-2 CORSE kWrep- CORSET kWrep- CORTEGE gher-1 CORTEX sker-1 CORUSCATE sker-2 CORVEE reg-! CORVINE ker-2 Corvus ker-2 CORYDALIS_ ker-1 CORYMB_ ker-1 CORYNEBACTERIUM bak-, ker-1 CORYPHAEUS_ ker-1 COSMONAUT nau-2 COSMOPOLITE pele-3 cosmos kes-3 cost sta-
1812:MANEGE man-2 MANES ma-1 MANEUVER man-2, op-1 MANGE mendh-2 MANGELWURZEL_ wrad- MANGER mendh-2 MANGLE! = mai-1 MANGONEL meng- MANIA men-1
1813:MANIAC men-! MANICOTTI man-2 MANICURE cilra, man-2 MANIFEST dhers-, man-2 MANIKIN man-1 MANIPLE man-2 MANIPULATION man-2 MANNEQUIN man-! MANNER man-2 MANOMETER men-4 MANOR men-3 MANQUE man-2 MANSE men-3 MANSION men-3 MANSUETUDE man-?, s(w)e- MANTIC men-1 MANTICORE mer-2 MANTIS men-1 MANTRA men-1 MANUAL man-2 MANUBRIUM man-2 MANUFACTURE dhé-1, man-2 MANUMIT man-2 MANURE man-?, op-1 MANUS man-2 MANUSCRIPT man-2, skribh- MANY menegh-
1962:OFFEND g¥hen-! OFFENSE gWhen-1 OFFER bher-1 OFFICE dhé-1 OFFICINAL dhé-1, op-1 OFT upo
1986:OPERA! op-! OPERATE op-! OPERCULUM_ wer-5 OPEROSE op-! OPHIDIAN angwhi- OPHIOLOGY angWhi- OPHITE angWhi- OPHIUCHUS angwhi-, segh- OPHTHALMO- ok¥- OPINE op-2
1991:OPT op-2 OPTATIVE op-2 OPTIC Ook*- OPTIMUM op-! OPTION op-2 OPTOMETRY okw- OPULENT op-! Opus op-!
=== AHD often ===
105:A word of caution should be entered about the semantics of the roots. It is perhaps more hazardous to attempt to reconstruct meaning than to reconstruct linguistic form, and the meaning of a root can only be extrapolated from the meanings of its descendants. Often these diverge sharply from one another, and the scholar is reduced in practice to inferring only what seems a reasonable, or even merely possible, semantic common denominator. The result is that reconstructed words and particulary roots are often assigned hazy, vague, or unspecific meanings. This is doubt- less quite illusory; no human society from Proto-Indo-European times to the present day would be viable if conversation were limited to vague generalities. The apparent haziness in meaning of a given Indo- European root often simply reflects the fact that with the passage of several millennia the different words in divergent languages de- rived from this root have undergone semantic changes that are no longer recoverable in detail.
705:ma-. Mother. An imitative root derived from the child’s cry for the breast (a linguistic near-universal found in many of the world’s languages, often in reduplicated form). 1. Latin mamma, breast: MAMMA2, MAMMALIA, MAMMILLA. 2. Probably Greek Maia, “good mother” (respectful form of address to old women), also nurse: MaAIA, MAIEUTIC. (3. More recently formed in the same way is English MAMA.) [Pok. 3. md- 694.]
709:mag-. Also mak-. To knead, fashion, fit. 1. Germanic *mak- in: a. Germanic verb *makén, to fashion, fit, in (i) Old English macian, to make: MAKE (ii) Old French mason, mason: MASON; b. Germanic compound noun *ga-mak-(j)6n (*ga-, with, together; see kom), “he who is fitted with (another),” in Old English gemzcca, mate, spouse: MATCH}, 2. Germanic nasalized form *mangjan, to knead together, in: a. Old English mengan, to mix: MINGLE; b. Old English gemang (ge-, together; see kom), mixture, crowd: AMONG, MONGREL. 3. Suffixed form *mak-yo- in Greek massein (aorist stem mag-), to knead, hence magma, unguent: MAGMA. 4, Suffixed length- ened-grade form *mdg-ya- in Greek maza, a (kneaded) lump, barley cake: MASS; (AMASS), MAZAEDIUM. 5. Suf- fixed lengthened-grade form *mék-ero- in Latin macerdre, to tenderize, to soften (food) by steeping: MACERATE. [Pok. mag- 696, 2. madk- 698, men(a)k- 730.]
736:Latin micturire, to want to urinate (desiderative of meiere, to urinate): MICTURATE. [Pok. meigh- 713.] meik-. To mix. 1. Variant form *meig- in Greek mig- nunai, to mix: AMPHIMIXIS, APOMIXIS, PANMICTIC, PAN- MIXIS. 2. Suffixed zero-grade form *mik-sk- in Latin miscére (past participle mixtus), to mix: MEDDLE, (MED- LEY), (MELANGE), MESTIZO, MISCELLANEOUS, MISCIBLE, MIX, MIXTURE; ADMIX, COMMIX, IMMIX, MISCEGENATION, (PELL-MELL), PROMISCUOUS. 3. Possibly a Germanic form *maisk- in Old English mdsc, macs, mdx, mashed malt: MASH. [Pok. meik- 714.] mei-no-. Opinion, intention. 1. Germanic *main- in Old English *mdn, opinion, complaint (> Middle English mone, complaint): MOAN; (BEMOAN). 2. Germanic *main- Jan in Old English ménan, to signify, tell, complain of, moan: MEAN}, [Pok. mei-no- 714.] mel-1, Soft; with derivatives referring to soft or softened materials of various kinds. I. Extended form *meld-. 1. Germanic *meltan in Old English meltan, to melt: MELT. 2. Possibly Germanic *miltja- in Old English milte, spleen, and Middle Dutch milte, milt: mit. 3. Possibly Germanic *malta- in Old English mealt, malt: MALT. 4. Suffixed variant form *mled-sno- in Greek blennos, slime, also a name for the blenny: BLENNY. 5. Suffixed zero-grade form *mid-wi- in Latin mollis, soft: MOIL, MOLLIFY, MOLLUSK, MOUILLE; EMOLLIENT; 6. Possibly nasalized variant form *mlad- in Latin blandus, smooth, caressing, flattering, soft-spoken: BLAND, BLANDISH. II. Variant form *smeld-. Germanic *smelt- in: a. Middle Dutch and Middle Low German smelten, to smelt: SMELT!; b. Old High German smalz, animal fat: SCHMALTZ; C. Italian smalto, melted glass: SMALT; d. Old French esmail, enamel: ENAMEL; e. perhaps Old English smelt, smylt, a marine fish, smelt: SMELT?. III. Extended form *meldh-. 1. Germanic *mildja- in Old English milde, mild MILD. 2. Possibly Greek maltha, a mixture of wax and pitch: MALTHA. IV. Suffixed form *mel-sko- in Ger- manic *mil-sk- in Old English melfi)sc, mylsc, mild, mellow (> Middle English melsche, friable): MULCH. V. Extended form *mfk- in Greek malakos, soft: CHON- DROMALACIA, MALACOLOGY, OSTEOMALACIA. VI. Possi- bly Celtic *molto-, sheep, in Old French moton, sheep: MUTTON. VII. Suffixed zero-grade form *()ml-u- in Greek amblus, blunt, dull, dim: AMBLYGONITE, AMBLY- opiA. [Pok. 1. mel- 716.] mel-2, Of a darkish color. 1. Greek melas, black: MEL- ANO-; MELANCHOLY, PSILOMELANE. 2. Greek mullos, a marine fish: MULLET; (SURMULLET). 3. Latin mulleus, reddish purple (used only to designate a ceremonial shoe worn by Roman magistrates): MULE. 4. Perhaps Ger- manic *mal- in Middle Dutch malen, to paint: MAUL- STICK. [Pok. 6. mel- 720.] mel-3. A limb. Greek melos, limb, hence a musical member or phrase, hence music, song, melody: MELISMA; ACRO- MELIC, MELODRAMA, MELODY. [Pok. 5. mel- 720.] mel-4. Strong, great. 1. Suffixed (comparative) form *mel-yos- in Latin melior, better: (AMELIORATE), MELIO- RATE, MELIORISM. 2. Suffixed zero-grade form *m/J-to- in Latin multus (neuter multum), much, many: MOLTO, MULTI-, MULTITUDE. [Pok. 4. mel- 720.] mel-5. Bad. Latin malus, bad, and male, ill (> malignus, harmful): MAL-, MALICE, MALIGN; DISMAL, MALADY, MALEDICT, MALEFACTOR, MALEVOLENT, MALVERSATION. [Pok. mélo- 724.] mel-€, Wool. Possibly suffixed zero-grade form *ml-no- in Greek mallos, wool. [Pok. 2. mel- 719.] mel-?. To miss, deceive. Germanic *mai- in Middle Dutch mal, foolish, silly: MALLEMUCK. [Pok. 2. mel- 719.] meldh-. To pray, speak words to a deity. Germanic *meld- in Old High German meldén, to proclaim, reveal: MELD}. [Pok. 1. meldh- 722.] mele-. Also mel-. To crush, grind; with derivatives referring to various ground or crumbling substances (such as flour) and to instruments for grinding or crush-
844:fér, danger, sudden calamity: FEAR. 2. Suffixed form *peri-tlo- in Latin periclum, periculum, trial, danger: (PARLOUS), PERIL. 3. Suffixed form *per-yo- in Latin experirt, to try, learn by trying (ex-, from; see eghs): EXPERIENCE, EXPERIMENT, EXPERT. 4. Suffixed form *per-ya in Greek peira, trial, attempt (> peiran, to attempt): PIRATE; EMPIRIC. [Pok. 2. E. per 818.] per-5. To strike. Extended forms *prem-, pres- in Latin premere (past participle pressus), to press: PREGNANT?, PRESS!, PRESSURE, PRINT; APPRESSED, COMPRESS, DE- PRESS, EXPRESS, IMPRESS!, (IMPRINT), OPPRESS, RE- PRESS, (REPRIMAND), SUPPRESS. [Pok. 3. per- 818.] per-6. To traffic in, sell (< “to hand over,” “distribute”). A verbal root belonging to the group of per'. Base of two distinct extended roots. I. Root form *pret-. 1. Latin compound inter-pres (stem inter-pret-), go-between, negotiator (inter-, between; see en): INTERPRET. 2. Suf- fixed form “pret-yo- in Latin pretium, price: PRAISE, PRECIOUS, PRICE; APPRAISE, (APPRECIATE), DEPRECIATE. II. Root form *pers-. Suffixed form *p(e)r-n-o- in Greek pernanai, to sell, whence o-grade *por()-ndé in Greek porné, prostitute: PORNOGRAPHY. [In Pok. 2. C. per 817.] perd-. To fart. 1. Germanic *fertan, *fartén in Old Eng- lish *feortan (> Middle English farten), to fart: FART. 2. Greek perdix, partridge (which makes a sharp whirring sound when suddenly flushed): PARTRIDGE. See also pezd-. [Pok. perd- 819.] pere-'. To produce, procure. Perhaps an extension of per-3, a verbal root belonging to the group of per’. Possibly the same root as pere-2. Zero-grade form *pro- (becoming *par- in Latin) in: a. root form *par-d- in Latin pardre, to try to get, prepare, equip: PARADE, PARE, PARRY, (PARURE); APPARATUS, (APPAREL), COM- PRADOR, DISPARATE, EMPEROR, (IMPERATIVE), (IMPE- RIAL), (PARACHUTE), PARASOL, PREPARE, RAMPART, REPAIR}, SEPARATE, (SEVER), (SEVERAL); b. suffixed form *par-yo- in Latin parere, parire, to get, beget, give birth (> partus, accusative partum, birth): -PARA, PAR- ENT, -PAROUS, PARTURIENT, POSTPARTUM, REPERTORY; c. suffixed form *par-os, producing, in compound *pau- paros, producing little, poor (see pau-); d. suffixed form *par-ikaé in Latin Parcae, the Fates (who assign one’s destiny): Parca. [Pok. 2. D. per 818.] pere-2. To grant, allot (reciprocally, to get in return). Possibly the same root as pere-'. Zero-grade form *pro- (becoming *par- in Latin) in: a. suffixed form *par-ti- in Latin pars (stem part-), a share, part: PARCEL, (PARCE- NER), PARSE, PART; BIPARTITE, COMPART, IMPART, REP- ARTEE; b. possibly suffixed form *par-tid in Latin portid, a part (first attested in the phrase pré portiéne, in proportion, according to each part, perhaps assimilated from *pré partidne): PORTION, PROPORTION; C. perhaps Latin pdr, equal (> French pari, wager): PAIR, PAR, PARITY2, PARLAY, PEER?; COMPARE, IMPARITY, NONPA- REIL, PARI-MUTUEL. [Pok. 2. per, Section C. 817.] perg-. Pole, stem. Possibly Latin pergula, a projection, balcony, outhouse: PERGOLA. [Pok. 1. perg- 819.] perk-'. Speckled. Often used in names of spotted or pied animals. Greek perké, the perch: PERCH?. [Pok. 2. perk- 820.] perk-2. To dig out, tear out. Zero-grade form *prk- in Germanic *furh- in Old English furh, trench: FURROW. [Pok. 3. perk- 821.] perkwu-. Oak. 1. Zero-grade form *prkv- in Germanic *furhu- in Old English furh, fyrh, fir: rir. 2. Assimilated form *kverku- in Latin quercus, oak: QUERCETIN, QUER- CITRON. [Pok. perk#u-s 822.] persna. Heel. Latin perna, ham, leg, sea mussel: PEARL}. [Pok. persna 823.] pes-. Penis. Suffixed form *pes-ni- in Latin pénis (< *pesnis), penis, tail: PENCIL, (PENICILLIUM), PENIS. [Pok. 3. pes- 824.] pet- Also pete-. To rush, fly. Variant *p#é-, contracted from *ptea-. 1. Suffixed form *pet-rd in Germanic *feth-
1106:upo. Under, up from under, over. 1. Germanic *upp-, up, in: a. Old English up, uppe, up: uP; b. Old English up-, upp-, up=: UP-; C. Middle Dutch op, up: UPROAR. 2. Ger- manic *upanaz, “put or set up,” open, in Old English open, open: OPEN. 3. Germanic *ufana, “on, above,” in Old English bifan, above, over: ABOVE. 4. Possibly suffixed form *up-t- in Germanic *ufta, frequently, in Old English oft, oft: OFT, OFTEN. 5. Extended form *upes- in Germanic *ubasw6, *ubizwé6, vestibule, porch, eaves (< “that which is above or in front’), in: a. Old English efes,
1963:OFTEN upo
```


## [2026-09-07T20:17:42.344Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT ama ===\"; grep -n \"ama-\\|amavant\\|amayava\\|afnah\\|hvapah\\|hv-apah\\|huuapah\" BRT.txt | head -40",
 "description": "Grep Bartholomae"
}
```


### [2026-09-07T20:17:42.392Z] TOOL RESULT

```
=== BRT ama ===
2478:Stelle  der  kongruenten  Form  steht :  a)  das  i ;  —  iE  äbyö  frSrtt^  fr}r»m-ainti  asaonqm Neutr.  Sing.:  yüzim  .  .  aogS  data  .  .  x/a-  ..frtrvaBbyoYX.13.afi;  —  zugleich  zurück- '^nmcS  .  .  azimcll  ahyä  (statt  Du.)  ..'weisend:  asti'atjntö  ..  atihe  haxayü  frä- %wqm  mPtihi  ..vaSd>m{sA.)Y.2<).ia;  —  \yente  astvatjr?lahe  Yt.i'>.95;  —  dacnnm dva/sing  ..  qstqscä  .  .  yezT  ahyä^^  (statt'.,  atiihi  ..  kavaya  ..  daenayn  V./o.ig. Plur.) /ö/  mal  xsayehTY.44.\\i.; — duye  —  a)  mit  relativischem  Anschluss;  ama- navaiti  astanqm  (sd.)  .  .  däittm  ahmäicil  !'af6yö  acibyö  yazataHbvT'  yat  am»saeibyö harf^r?m  hrmi^ät  V.  74. 17.  b)  das  sp»^aAbyöYi.fj.^;  —  mmö  äbyö  döi'iräbyü
2483:—  para  ahtnSi  .  .  cinasti  ya%a  ^aitavS x'aitäifm  (sA)  Y.20.  i,  3)  auf  ein Relativum  als  dessen  Korrelat;  a)  adjek- tivisch: ahmili  naemäi  uzjasäitt  mtiro  .. yahtnai  naimanqm  mOiröJruxl  nai-ia  .  . paiti.päiti  Yt  /0. 1 9 ;  —  aÄ  . .  alsam  narqm yöi  kacahi  Yt/7.6;  —  mffirpm  ahyä *madahyä  (sd.)  yä  .  .  uräpayHntl  (sd.)  Y. Jt^.io;  —  Svat  A3  nü  ankuyaite  .  .  cvat ahmäi  naire  m^tm  aahat  yÖ  .  .  frama- r,UU\.4-4t;  Y.62. 1,  Yt.  10.137;  —  "^^ dussar^hahe  . .  manö  3at  ahe  .  .  mane  yö ml  dussatahö  hutaite  Y./0.12  (s.b);  — ipas  vloaSa  .  ./rS  *aAhe  vXsaiti  mt>rö ..
2578:31;  3''.  35'*. "^-85;  —  tts  haca  nassvö  °vat  •  j.  aeJa-m.,  Plur.  'Kopfhaut';  '',a  ..*kay:i apat Aaca ni:iiiraj-fnV.6.$if?); — asH.masÖ  fi^nti  masyat»hd  'r,a  *ydi  *aparaya  paiti xraoidi'aAe  bis  'rate  lar^AaAe  "..h\s^3iXtto  *)tiastrfynaya..*kaya  kasya/i/t^  *yüi  *paou- mollisligni"  V.  jj.  30;  —  'val  apayaiia  H.  ruya  paiti  *mastrr/nya  "Kopfhaut.  — iog(X).  a)  mit  dem  Korrelat  _v(K'a«/- :  Welcher TeilderKopfhautistdergrössere? ^t/ (sd.)  °vat  htT^r»m  yaval  tacantn  F. '  Der  an  der  hiotera  Schädelwand.  Wel- 27a;  a;  ■ —  yavat-  hatca  hl  sastaiibya  eher  der  kleinere?  Der  an  der  vordem hangturvayqn  'vat  apat  haca  nizbärayfn  Schädelwand."  F.jc. \.ti.2t);  —  'imt  npö  yavat ,  .  J^.ioX;  — 'foiö  zaota  (iäm\.  ratu/rii)  yajat ß-ama- raiti  "mit  so  vielem  ist  der  Z.  r.,  als  .  -^  „  . n  (selber)  .ufsagt-  N.  2,1  2,,  23,  »>',  \  )■  if^  'a.«,y<,il„t  pa,U  afa  .  .  N. j'P.  Aa)  GS.  'vatö  als  .\dv.  'quantum  ^  j-  .  j^j^j^ sat  est,  in  hinreichendem  MassM?):  hura-  "  ^^.^  ^  ^  ^^^  ^^^^^ ysscti  (sd.)  a(.a  Tato  datdyat  A.j.4;  —  .   ^i%y^_^.^^,„„  -(.^5.  y^s  ka^i^yStarlum.
2644:Zum  V.  ain-.  —  Vgl.  ^afnah-.  —  Pü.  (dRn.): pa    därün  i  ken ;    S  di  i  kin ;    ö  icn ;    kenän  i
2737:Aus  ir.  *ai:ama-,  S5J 1-  8.  —  np.  iiam.  —  langCD  sucheo,   haben  wollen,  begehren,
3580:apairi.vavastama-
3650:•  j.,  g.  apama-'',  g.  ap«ma-  Adj.  (fem. "ffiii-)  Adj.  'der  (zeitlich)  letzte',  ntir  von dem,  was  am  Ende  der  Dinge  (des  ersten Lebens)  eintreten  wird  ('jüngst')'':  'ml arihSus    unalsZ {sA.)    Y.J/.6;  43. S\    —
3863:•  j.  aiwinasE^s'tama-  Adj.  'der  am  meisten erlangt"':  hanhanultfmtm  asaAe  rdiwqm °m»m  Y.'I.$.
3973:Ableit'  —  Komp.:  ^wi\tama-,  %  268.  3. Vgl.  avLama:-^  Pü.:  fl/ar  ma/är,  erl. :  0  Jtär u  ää/ai/ä»;  e.  Ableit.
4015:•  j.  afrakavastama-  Adj.  (fem.  'mi-) 'der  am  wenigsten  von  der  Stelle  zubringen ist,  der  unerschütterlichste':  fratujsayS  . . "mit  apa^srayamnanqm  "die  Fr.  . ,  die  un- erschütterlichsten unter  den  sich  anstem- menden" Yt  y.  26.
4022:•  j.  afnah'vant-   Adj.   'reich   an   Habe,  j  •  j.  a-fra'tatkvah-"  Adj.  (fem,  •■iat.kusi-)
4614:•  j.  antama-  Adj.  i)  'der  innerste':  'ma aiwi.varma  "das  innerste  Kleidungsstück" (d.  i.  das  Hemd)  V.  7.10;  —  'ma  aiwyi- fthänS  Vd.  /2  '*.  —  2)  'der  vertrauteste, intimste':  *°m3mcit'''^  sanhs-n  "auch  das vertrauteste  Wort"  F.  j  eJ'.
4615:SuperL,  S.  'antara-.  —  ai.  anlama-  Adj.  —  Pü. : aiidarliim,  (zu  Vd.):  ha/diar.  —  ')  zSt.  Bthl. IF.  77,  115.  —  »)  Hds.  x^t>mHi\  s.  Bthl.  IF. II,  13t.  —  1>  Pü.  erl.:  ligBn  razikä.
4686:KompA.;  Ableit.  —  Vgl.  'ama-  Adj.  —  ai. äma-  m.  'impelus';  tnp.  vgl,  amävaiid  Adj.  — Pü.  i  tanäraiütVi,  Sü.  (zu  Y.  p] :  mahcisakalvam, erl. :  makämänaiahiant  yat  kaiyäpi  sahäyyam nopekialt;  (in  A):  amSvand,  Sü.:  ulsäXi.  — »  Vgl.  Ableit.  —  ')  Hds.  akmSi  (mit  der IJg&tur  für  hni);  s.  aber  Pü.
4696:•  j.  ama'vant-,  g.  Sma'vant-  Adj.  (fem. 'vaifi-)  'kräftig,  stark,  mächtig,  gewaltig, wuchtig'i  a)  vona)  Menschen  und  ß)  Göttern : o)  narf .  .  pancajiasanhö . ,  hrpzats  avi.- amahe  'vatö  Yi.S.i$;  — ya'ia  agj?  'va .  .fraxitäne  z?ma  paiti  Y.5. 20;  —  aisäta "iwa  'vantaslä  buyamä  (sd.)  Y.4J.4;  — , ^vm  yäka  ^vifrö  naväso  Vyt2;  Az,2;  — | faritJm  il  ^icJ  yähanä  tat  °vatqm  kyat ^wä  xiayqs  (sd.)  aissm  dyll  'vantim  "eine Frage  von  dir  (d.  i.  Zar^  ist  ja  wie  eine Frage  Mächtiger.."  Y.^l^.io,  zit.  A.  4. 3, wo  amavanlam  und  amavant^m ;  —  °fa (NSm.)''  äs  Vfri^rava"^  nqma  v^rp^rava] Os  'va  nqma  Yt.  i4'S9-  ß)  ralnul bjrTZö  yö  '»i  Yt,JO,ioo,  i2.6;  /7.16,  J2. ' 5;  — yö  {sraolö)  .  .  niaza  'va  firS^raja'^ , Vr./5.3;  —  °va  mt^rä  Yt  10.  loj ;  6,  25, loa;  —  airyamarigm  .  .  'vantpm  vprjhrd- ^
4724:6itTm  .  .  x/lßm  cvat  kaca  'yaätyB  "ein  •  j,  *ama-,  g.  Sma-  m.  i)  'Kraft, Loch  sollst  du  ausstechen  .  ,  Wie  weit  Stärke,  Macht":  n^ar^nö .  .  balsazim  Uta von  einander  (soll  ich  sie  ausstechen)?"  'mtmia  Yt/4.2;  —  manmn»m  (sd.)  ,. V.p,8'>.  damayai  "Tmm.  .tanuyeXX.i6.\T,   19;  —
5085:p.  ava''-parä   adv.-artige   Verb,    'dort  I  ■  J-  avauhutama-  Adj.  'der  wenigst  gute, davor':  arläda  nämST  dids  >5jr(7*«inft>j' böseste':    datVäU  .  .    Mtam    'hmais    Y.
5453:•  j.  aratö.kar^^na-  AdJ,  'wofür  die  Er- füllung der  religiösen  Pflicht  bezeichnend ist',  von  Hamaspa^maedaya  (sd.)":  ha- maspahmaSdaim  "tum  Vr.  2.  z; —  kama- spdimaldayeAe  'nahe  Vr.  1.2;  —  *'%nö F.7'>.
5548:•  jj  g-  'airyaman-,  g.  airyäman-  m. 'Genosse'  uzw.  priesterlicher,  Angehöriger des  ersten  oder  Priesteratands  (s.  unter 'pistra-),  'Sodale' ;  Sing,  auch  koU.  'Soda- lität',  nur  gAw.:  iJ  yama  kp  x^allus  {%<!.) dätäis  anhat  yp  ,  .  Y.  /fg.  7 ;  —  ahyScH x'aSus  (sd.)  yjsal  ahyä  virizsntm  mat yamnn  . .  Y.J2.1;  —  yf  '^jvaj  masdn asruinm  . .  yazli  (sd.)  apa  K^'aüSuScä  tar>- maitTm  virn^nahyiilä  . .  'yamanascä  . .  Y. 33-4  i  —  y^  asäuia  vahiils  :^aSä  (sd.) vä  al  vä  v>r>iSny3  yämiiä  (IS.  als  Subj.)  '> vil .  .  Y.  JJ.  3;  —  pairl  clausus  'yama- nascä  dadaili  ndii  .  .  i-ir>z5nä  (sd.)  Y.46. I.  A)  Name  einer  Gottheit":  vairya sar)ha  para.äi'd  upa.vasanuha  avi  nmli' mm  yamaini  imat  sanhsis  'yamanäi  J' "A^,  geh  weg,  fahr  hin  ins  Haus  zu  A., das  sollst  du  dem  A.  kund  machen"  V.
5628:araia.        •'  '  •  j,  arsama-  m,  EN.   eines  Persers,  Ar-
5632:Gebirgs.  Komp.:  arsa-^ama-  'die  Kraft  eines  Bären')
5873:•  j.  asp9r«zö.dä'tama-  Adj.  'der  am meisten  Fürsorge  anwendet,  Sorge  trägt um  — '  (Dat):  ySi  *a»Am  nprtbyS  asava- byd  ayaptö.dahmasla  °masca  (statt  NPm.) "die  den  Gläubigen  am  meisten  Almosen spenden  und  am  besten  für  sie  sorgen"
5989:•  j.  a-zarama-  Adj.  (fem,  'mä-)  'nicht
6185:')  NA.  auch  nngetrennt.  —  *)  Vgl.  'ama-'üo.
6281:—  r3laca  vaauhi  .  .  °saane  (VS.)  V.  /(?. 19,  Vytjö;  S,  1.5,  2.5;  —  raziflam  astim ..  "saonJm  Yt.16.1,  4;  o,  20;  —  airyama- mm  iitm  '^avan^m  Vr.  24-  3 ;  —  kaomS °^ava  Y.p.a';  10,14;  —  haoma  °lava (als  Vok.)"'  duraosa  Y.  j/.  10;  —  rasmiö °lilum  Yt  J2. 7;  9; —  sraohm  .  .  '/avarum Y-  57-  2i  33,  Yt.  II. T,  —  Aaurvat3t>m 'savaram''^  asahe  ratüm  Y.  71.  12;  — am^ntät^m  "savanpm'i^  asahe  ratüm  Y.7J, 13;  —  ahura  müra  .  .  •s'avana  (AD.) Y.  2. 1 1 ;  YL  70. 14s;  —  ahuraHbya  miitraei- iya  '/avanaäiya  Y,  j.  11,  a)  bes.  von Ahura Mazääh:  3  äim  tä  vaca  rämayal ahurS  masdä  'sava  alavansm  zarä^ulinm V.5.2I;  jp.15  (statt  Akk.),  Y.7/.4,  5,  57. 24,  Yt.S.i,  11.1%  12.4,  16.3,  Yt/0.89, 7J.  14,  15;  —  ahur)m  mazdqm  'iavamm aiahe  ratüm  Y.2,2,    t6.\,  ^5.1,  7/.2,  4;
6427:•  j.  asiä.hak-  Adj.  'der  Asay  anhängend, ergeben':  tDttß . .  'JiSgit  (NSn.)  Srmaili/.- hägtt  Y.  $8- 1-  a)  NSn.  'kägst  als  Adv. 'in  Ergebenheit  gegen  A':  vTspaica  alte 'hsgst  ärmaitii.hägft  (zbayemify  yazama- daEca  "und  all  diese  (rufe  ich  an)  in  Er- gebenheit gegen  A.  und  Ä.,  und  wir  beten sie  an"  Y.  -]!.  ii.
6434:•  j.  asxräx'anu'tama-  Adj.  'der  am  aller- meisten antreibende,  anregende':  amjsqs^S spitiiq  saosyantascä  .  .  aiwyämatitnq  'ittq Y./is;  "Vr.J.  s.  '
6509:.  ].  asa-*wo.zgatama-  Ad,,  'der  aUer-      ^Xr/:  d^n  ain^y-Ai.  ILm  =  j.  a>n^:  aL drängendste,  allereifrigste':  °mq  gavästrya-       äsmana).  —  jj  Vgl.  %rah-  No.  3. varlt>niq  narqm  asäunqm  Y.  13.  2.  '         j.  ainäat^a,  ainJ:  s.  unter  aiaa-.
6754:j.  aki^ta'  V.  7.  53,  54^  lies  ahqii/a'.  ^  akunin   mazdqm  .  .  mainyavanqm  dama-
6922:•  j.,  g.  ahma-,  g.  »hma-'>,  p.  ama-  Pron, I.  Pers.  Plur.  'uns'  (usw.).  Es  wird  ge- braucht i)  wenn  auf  dem  'uns'  (usw.)  be- sonderer Nachdruck  liegt:  *aia  nä  iixsta buyan  .  .  'm,li  (Dat.)  saoiäi  . .  u/n  ^fra- mainyäi  (sd.)  Yt.  if/.  3;  —  uUä  astl  usta 'mäi'^  hyat..  assm  (sd.)  Y.27.14,  a)  in Verbindung  mit  jiS:  pam  mtfsS  yatthö 'mäii'  np  sazdyäi  (sd.)  baoäaniö  pattT Y.  30.  2.  a)  bes.  bei  Gegenüber- stellung: daidi  sara'iiultrai  aojönghvat  ra- fmö  "maibyiicii  ..  Y.2,V.6*l;  —  däidi  a( nirqs  .  .  aiaHnaiihö    aidyUs    viistrying  .  .
7803:*aifma-  (%  24\  Aw,  "i^ama-  (S  296.  l).
8133:•  j.  Uj-rö-tama-''  Adj.  'der  stärkste,  kräf- tigste': ina%ranain  uyrtm  ma^ranam  °tn?m
8135:u.  ugralama-  Adj.  —   i)  Der  alte  Superl.  lu u-,ra-  ist  aajiila-,  s.  Yt.  7p.  38.
8298:•  j,  upama-  Adj.:  s.  unter  upjma-.
8392:•  j.  upa^sraotar-  m.  Bezeichnung  derer, die  beim  Gottesdienst  den  (Gaia-) Vortrag des  Zaotar,  soweit  vorgeschrieben,  nach- beten oder  respoDSorisch  ergänzen":  *'ianu,- pir3i:S  laota  dahma  "tarS  yasi  dim  tanu.- p?r?i:fm  *vT'iian  aSavatö  *ratuffyö  yaval framarfiOi  yai  aal  dim  nsit  ianu.pirJSiim *vi'jar>  vTspanam  glihanqm  *ratufryS  "Der Z.  ist  /,  die  Ü.  sind  d.  Wenn  sie  wissen,  | dass  er  (L  ist,  sind  sie  nur  für  das  r.,  was ' sie  (selber)')  aufsagen.  Wenn  sie  aber nicht  wissen,  dass  er  /.  ist,  so  sind  sie  für alle  Gahaz  r."  'S. 3g;  38,  3g''>]  —  sum- fuioiti  saota  'faranam'^  rtöit  'tärS  zaotarö xaata  ratufris  altavats  'tärSyavat  *frama- r^nti  "Es  hört  der  Z.  die  Ü.,  nicht  die  U. den  Z.;  darin  ist  der  Z.  r.,  die  U.  aber nur  filr  das,  was  sie  (selber)''  aufsagen" N.2/;  27 J.
8436:.    i.   upama-,   opama-"    Adj.    i)    'der  '^«»"«■'Tfsd.) ..  ijy?^.«  f,j«M.Ü  Vt /j.js;
8550:Superl.  aus  ar.  *M;  s.  iis.  —  ai.  üllama-  Adj. —  Pü.:  apaliim;  s.  No.  I.  — Pü.:  a^än/ralum .  .  Hin  a/alum/7.
8984:■  44-\i\  —  °rs  (statt  DP.)  pautrS  äma- yiinte  (sd.)  mazdayasnaiibyö  vä  dasvayas- naiibyS  vä  V.7.36;  —  in  Indir.  Fr^e:  asö . .  yn  .  .  varssxii  .  .  vafnaiti  'rö  ir/ravB (sd.)  Vit  ^bunai'o  va  Yt  i4.  31.  ^6". 10.  a)  ASn.  °r$m  mit  vä  ..vä  'utrum .  .  an  .  .?';  'nm  *ä^rava  diiauruiiMn  vä parayat  gaei^artqm  Vä  asp^rMif  (sd.)  avat N.  j;—  'rJm  asava  vä  dngva  va  vsrm- vaili(%A.)  mazys  'H.31.  17.  II)  als  In- liefinitum  'uterque',  mit  folg.  «/"';  pita puirasca  ..  'iaras/il  (NSm.)  Y.ff.  5;  — späoa  .  .  rast^m  (sd.)  rasma  Harascit  Yt. 14.  43;  ig.  46,  Vyt.  47; — yezica  vä gag>a "iTwJ  (sd.)  *°iarasap^  *paray3t  N.5; aaavalö  *'tarasat**  ratufris  yavai  frama- r«A'(sd.)  N.  2j; — yazäi  3xstlm..suyqmca •tarpmaiYU5.i<7).  a)  ASn.  '/arascij^' 'nach  beiden  Seiten  hin,  utroque':  p»rma
9785:•  j.  gaotama-  m.  EM.  eines  Ungläubigen:  1 yS  näiifySaAB  'tsmahe  parSyä  farit5it\ avsiti  "der,  über  den  unterliegenden  G.  ] siegreich,  aus  der  Disputation  weggeht": Yt.y.  i6'>.
9786:ai,  i;Slama-  m.  EN.  —  ar,  *gaulama;  Be<3.? Anscheinend  Superl.  —  ')  Vgl,  daiu  Yt.5.  8l. Dass  es  sich  dabei  um  die  Disputation  m"' einem  BuddhiBlen  handle  (Haiig,  Dst.;  lulel: Dakab  JRAS.  iSgS.  391,  der  naidy  für  ' corroption  of  the  Vedic  name  of  the  son  r Golama,  viz.  Nodhä^  ansieht),  ht  tinerweislich ond  mir  unwahrscheinlich;  s.  noch  Jn.  Zor. 177  nnd  lu  li^ryavanl:
```


## [2026-09-07T20:18:09.011Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== 5600-5645 ===\"; sed -n '5620,5645p' BRT.txt; echo \"=== 4720-4740 ===\"; sed -n '4718,4740p' BRT.txt",
 "description": "Read Bartholomae arsama and ama entries"
}
```


### [2026-09-07T20:18:09.083Z] TOOL RESULT

```
=== 5600-5645 ===
*)   Den   getötet   lu   haben   Mx,  2/.  Hf.  aU   asaonß  Yt  19.  132. höchstes  Verdienst  («;/)  des  GiyruVa/ii/n»  gilt; .      Vgl.    'arsari-.     S.   auch    ariaia-   und   ariäjj- vgl.  WiNDlSCHUANK  ZSt.  5-  —  *•)  Der  nach  I'ü.  j      „([  fjo   —  »j  Bd    ii    i? und    Bd.  12.  8  /o  a-iw-  /  dBi-u"   'am   Tor   der  '  ■  J  ■     3-
Hölle'  liegt;  vgl.  noch  Dd.  33.  5.  ]  •  j.  ar§avant-  m.  EN.  eines  Gläubigem
Et.  undBed.?  Vgl.  iri^ura-.  —  mp. (¥ü.) anär \  •fats aiaonS  ..vyarlavalö ..patlyarsavatd  ..
tamäl,  artür  srhiai.  1  Yt_  jy.  loq.
•  j.  arä  Adv..:  S.   unter  >ni.  Eig.  Bed.P    Ob  Ableit.  aus  arSa-l     Dann  ai. KompA.                                                                   '     r^!'»""ii-  m.  Name  von  Stadt  und  Gebirg.
•  j.  (,p.)*aräa-"  m.'Bär':  °Jii'>..  flAÄr«5:*  j-  aröadä-  f  Name  einer  Festung  in Aog.  7p.  I  Arachosien:  'da  näma"  didä  hara'uvaSiya
KompE.;  Ableit.(?).  —  Aus  ar.  ♦/■"■>.  IF-  ?-    Bh.J.  II.
261.  —  ai.  /*fa.  m.;  KDm.  ai;  vgl.  np.  xirs       Et.?')  —  ■)  VgU  lusTl  GIrPh.  2.  430  Ko.
araia.        •'  '  •  j,  arsama-  m,  EN.   eines  Persers,  Ar-
.  p.  aräa'ka-  m.  EN.  eines  Persers,  Arsac^:  """'f-  ^^raya''vJ'uS . .  vutäspakyä  pui  y" 'Aa*  näma'  *a^iyiliausnaÄya  fu^'af  S.  7.    ''""^^  ""^'^  ^\  ''^'^  vtmspahyl  pns
AbleitCmitKosesuffix)Bus*ar/«.Moder.<,»a-:..i°'w<i^    "makyä  pttä    anySramnd'  Bh./.z;
—  Vgl.   'arSan-.   —   ai.  fifoia-   Name   eines  \  —  'mar  Ao.  J.  2.
Gebirgs.  Komp.:  arsa-^ama-  'die  Kraft  eines  Bären')
,     ,  \   ,      X  \  m  »...  besiliend'.  —    »)  Oder  auch  'eines  'Henesls,
•  J.   (g-.  P)   'arSan-  m.   l)  'Mann,  Mann-        Helden';  ».  '<^io«-  und  Bgu.  Grdr.  2.  A eben'  (geschlechtlich)'»:  a)  von  Menschen:      .      ,_ .  .,.,,,
'^am  xfudrä  Y.  65.  2,  5;  -  pu^r^m  .  .  '}■  ai&o.kais.- Ad}. -7-'^ :v^r^>ray„;,m . . anyahmäi  'lanai»  varihm  YtJ7.58;  -  'to/.  m<T«J.*«w/</mj^.i«rPff,  \t/4.28. ,  -^  ..  V-.     V  ^  V  i.,T.  \        ^p^.:  ittvan  u  iahib.  —  ')  lirklaruncsv ersuch
loMi  . .  mnayml  iiimsni  •latra  (NP.)      ^,1  ^^^  3  y,  j^  (.umpflu.iiE'),  Dit.  ZA.  ,. V. /Ä  31;   — ^d^a   anyasSt   'iuris  aii      56S  {'qui  rend  viril'). xSudri  aa^riha  trm_mr,navainti  y-lS._,  .    ,      ,   „5.^8,     «raz-uxSa- ■>  Adi. K'  ^?^=^fV~  *-■*--'  """f";'  'richtig,  recht,  wahr  gesprochen';  a)  von
ntergen)  Tieren  (m  Gegens.jn  ,/<.™..»-):  ),i^„,„„  ;,,,■/„  Y.&.  5;  Yt/j.3,  75.96 -'  j,     ,  •    ,  .,.        (wo  °z°y,  —  'suxüjm  Täcim  Y,7.  26,Ij,ü.  6:
5.120;  —  ustrane ..  yö -snam  ..  mattstem  i_  «,•„_;,_   ,,7,7-,   S  "  18    Vo  z";-    ■
a,jl  sl^rMi  yyi.^'-     ■    a)  sonst  in    .,,  „^  ,,^^^  .{^  Y.5.  ."sPUZ;  -  M.^i-Ä.
Verbindung  mit  dem  Tiernamen  3>: .
cca  Y.  -f,  10;  10.  t8,  Vr.  7. 1, 20.  i,
Yt.«.3t,  39,   /«.lo:—  uHtahi-MI..  G.  2. 6,  Yt.  i<!.  8';   &j:äa*  t',7*/ Y. «  . ,
»./.»fcwV.M.,,;,,  3;j-i-a,  •Ät,l_   ^;,.„,^;„  .^,„„   ,,„^,„    .j„w,„„
vt.  17. 5s;  -  .r.""  -'«»fc«  Yt.M.  7i  -  Y.  „.  25;  27.  r,  -  -»«.«.W.i  «-/=%'
^,pmqM_-!nam  .  .  u.Inmm  •!nqm  .  •,  v,:«. ,,  Y.lS.  .,  Ny.I.  .6;  -  •.'»..«(/»&' l,r„qm  -na,  ..  anum„yamm  •*?««  V.  22. ,  ,,^^^^^_,  Yt.5.76;  -  -mmm  vui«/,„m .o;1ft.S.,.;-il.M,7.«™r««J.     .,,„„^„^;„,;i^y,    „  '_     .,„.,;^^
=== 4720-4740 ===
—  .)  VgL  Y.  29.  1.   ^.  7.   SO.  1,   wo   anyS  2.9''-  [YLJO.J17:    lies   kamahe^^ ,    —
syntaliiisch  NSm.  ist.    So  liesse  sich  das  obige  N.  4^:  lies  im^m  kaoimm;  s.  Y.  22.  i  und
onj'ö  auch  Yt.  79. 36, 38  nehmen,  aber  an  den  T.]
andern  Stellen    ist   es    sicher  Adv.;   vgl.  die  KompE.;  Ableit.  (s.  aiuyäm'^  —  VijL  ^arna-
Kote  lU/fl/-^.  I       ni.  {and  lU  ayav-).~-Vü.\  amäz-anJ.  —  0  An
•  j.  anyö-anya-  Adj.'*,  Plur.  'einander':  >  "*"»  Parallelstellen  Vl  j.  64  usw.  steh)  aJ.- paoirtm   upa   ma^im  (sd.)  ni^wtnsSiS  ,  .      '^v^-  —  ''  KZ.  jr.  265.
6itTm  .  .  x/lßm  cvat  kaca  'yaätyB  "ein  •  j,  *ama-,  g.  Sma-  m.  i)  'Kraft, Loch  sollst  du  ausstechen  .  ,  Wie  weit  Stärke,  Macht":  n^ar^nö .  .  balsazim  Uta von  einander  (soll  ich  sie  ausstechen)?"  'mtmia  Yt/4.2;  —  manmn»m  (sd.)  ,. V.p,8'>.  damayai  "Tmm.  .tanuyeXX.i6.\T,   19;  —
ai.  vgl.  anyb'nyä-  Adj.  —  Pü.:  !and  ä«  maf  paiüünlfm  'mähe. .  "krimaht . .  baaazyehi
Stellung  von   -ia^a  zeigt,  s.' an' iW,^?.a..  VgU    it.74.6i;    —    haitimq     aia/ie  .  .    °ma  .  .
V.  5i^  5>  Yt.  13.  84  unter  a?iyn-  1 1  o.  ammyl  Y.ij.z;  —  mazisttt  °mq  ämrvyZ
.  i.  anyö.tkaeäa-'>,  anya.!kaeäii-«  Adj.  ''«»«)«    mlKdayatnlil  J.' js-  i,    Vr. ,,.
(fem.  •&-)  'täer   einer'  antien.  (Gktibens)  3-     ^,  »)  von   li«  Kraft   des  Miitns  im_
Lehre  lugelao  isf:   mlMrinli  M  -läi  gescWechtlichen  Sinn :  7,ari . .  tma  ayao,
Vä  V.IS.,,  —  yal  iamSt  Vä  raoxman^m  <.f-)  f>ä  f""rlm  imm  äv,  -mö  a:,l,
färaMiy^li    ,a%,  ''myLvarma    *-Ü"  "■.•.™,""'"°  den  Mann  zum  ersten  Mal
(statt  NSm.)  31  "wenn  sonst  ans  der  Ver-  d;e  Kraft  ankommt    Yt  *.  14.         i)  bes.
wandtschafl  (einer)  stirbt,  der  einem  andern  die  beim  Angriff  entfaltete  Kraft,  'Angrilfs-
Glauben,  einer  andern  Lehre  ungetan  isf  '""•  impemu,  "e''»  t;r,irä-  nnd  vm-
V.is.ü.;   —   ■/«    Miriiä   fairi    ,!u4,S   ^rr/aa-'l    -m  aim,  ämävaMmS  v,r,i  rä
/m«har,iaili  ahmät  häcä  Lira  mäili  "'"'•  "r>>rävail,m,  Yt,4.y,- •^far.u
"er  lässt  seinen  Samen  in  eine  Frau,  die  'M, .  .rm>rä,Yt.,o.26;  A.i.i.'F.y«;
einer  andern  Lehre  mgelan  ist,  (und)  es  -•"■•'«tjim  v>r,irä}Mi,ä..^fi,.mrroi
»ird  in  Folge  dessen  ein  Kind  geboren"  V.5..7;  Vr.9.4,\ytJ7i  -  «r  «..»»,■?
```


## [2026-09-07T20:18:11.345Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== afnah ===\"; grep -n \"afnah\\|afna\" BRT.txt | head -20; echo \"=== hvapah ===\"; grep -n -i \"vapah\\|hu.apa\\|hvapa\" BRT.txt | head -20; echo \"=== amayava ===\"; grep -n -i \"amayav\\|amaya\" BRT.txt | head -20",
 "description": "Grep BRT for afnah, hvapah, amayava"
}
```


### [2026-09-07T20:18:11.430Z] TOOL RESULT

```
=== afnah ===
2644:Zum  V.  ain-.  —  Vgl.  ^afnah-.  —  Pü.  (dRn.): pa    därün  i  ken ;    S  di  i  kin ;    ö  icn ;    kenän  i
4022:•  j.  afnah'vant-   Adj.   'reich   an   Habe,  j  •  j.  a-fra'tatkvah-"  Adj.  (fem,  •■iat.kusi-)
4024:—  "ha/sne  {sA.)  *afnat»ukh  F.  2C  \aAmät  kisipnla..'kusisi^Vi.)  hamaya gätvif
6254:—  syao%ami  razistä  (sd.)  ängvataicä kyai<ä  *'iaotii  yehyäiä  ASmunylsaitl  (sd.) mi^aAyä  yucä  ksi  är»svä  Y.  _jj.  i ;  —  yS vü  xsayqs  adqs  drTtä  ayanhm  urvatsis (sd.)  Vit  huiSntul .  .  ra/nä  jvqs  yS  'savä dr3gvant)m  Y.  46.  5.  a)  Ko-i  it  von Zara^ustra  (s.  2  c  a  und  drTgvaiit- 1  2  a  a) : y!  äyal  •iavanam  divamnsm  (sd.)  hsi  . . *dusji^arä^Sm  (sd.)  . .  ISm  *vi  ahSm  dr>g- vants..dams  «a<tf«/(sd.)  Y.^7.20.  b)  im jAw.:  kat  *sava . .  vanai drvantami  'idva vanat  drußm  °sava  vanat  drvantpm  Yt. I.2S;  —  x^ayamnam  '/avanim  däyata *axsyamn^m  drvant^m  Y.  Ä  5  ;  —  vasB.- x/a'iirB  kyüi  'sava  avasS.xia'^rS  hyäf  drvä Y.S.6;  —  yqm  'lara  ..  asayqm  (sd.) va^  tarn  drva  ^ihva  Vr.  22.2;  —  mt^nm ms  janyh  mä  yim  drvatat  pimanke  mU yim  n^adafnat  'iaoiiat  uvayä  af  asti  (sd.) mskrB  drvataica  'saonai^a  Yt/o.  2;  — pdhqm  %rvB.däianqm  jasaiti  yasla  drvaile yas^a  '/aofieV.  lff.$o;  — yai  azäite^sd.) tsm  ahum  pai'iyaite  yim  "soonam  yesi  nHii azUiie  tun  aAam  pai^yäite  yim  drvatqm V.  /Ä76;  —  drvatqm  ..  urvänS ..'läunqm V.  ig.  30;  —  ga>il  nmätiam  ^mr^yS  asti '/SvaoyB  (DP.)  naSai  drvatqm  Yt,7.4;  — hiiia  para  'saonqm  pa^a  urva/ai/i  iu^a drvatqm  Yt4.4;  —  narqm  vä  'saonqm kanjamanäis  drvatqm  vä  . .  kandvaranäü YLi/,4; — yai  •i'ava  para.iriiyeiä  . . yal drvä  ava.*miryeie  H.2.1  — 19;  7,  8,  10, 15*,  16',  18  {'iaonyäi);  s.  unter  drvatif- 1 1.  2)  sonst,  a)  im  gAwr.  (ausser GHapt):  zara'^usträ  kastl  'lavä  urva^S mazsi  magäi  (sd.)  Y,  46. 14;  —  tSm  (näml. pounicistqm)  . ,  varänl  (sd.)  .  .  yä  försi vTdäl  paüyaFcä  västryaHbyo  (sd.) . .  *°iapnj 'iavabyS  Y.  5J.4;  —  hvs . .  yas^a  vadarS (sd.)  vBizdal  'iauni  Y.^a.io.        a)  spez.
6354:"  j  a-§ä-  £  'Unfreudigkeit,  Unlust,  Nicht- aufgelegtscin  (zu  — )  wegen  —  {Instr.)':_)'J  .  . nöil  aiviyäsli  (sd.)  *'saya'^  aridusa  .  .  N. 75;  —  väkmaini  (LS.  statt  IS.)  *'saya^l ifafna  vä  anaivUli  ästryeiti  "wenn  er zu  studieren  unterlässt,  weil  er  wegen  Ab- spannung oder  Schläfrigkeit  nicht  dazu aufgelegt  ist,  so  versündigt  er  sich"  N.  75.
6967:•  j.  a-x'afna-  Adj.  'schlaflos':  °w?  a/ii  . . terii  ys  ahurg  V.ifj.io;  —  mtiirstn  .  . 'mm  jai3urv3t»k?i)i  Vt.  10.7.
6970:Ableit.  aus  a^afna-;  vgl.  ^\.!nhäslya- :  stikäua: —  Pü.:  iLL''äplh.
7204:•  j.  a-x^afna-  Adj.  'schlaflos':  °tis  ahi . . tum  yS  akurö  V.  ip.  zo;  —  mtirim  .  . 'nsni  jar^iiurvaahiin  Ytio.  7.
7631:•  j.  a-W8p0Ji''afnan-  Adj.  'der  keinen voUkommenen,  d.  i.  tiefen  Schlaf  Jiat': zainauha  'na  (NS.;  DämL:  ist  der  Hund) yaia  vastryS  fsuyas  V.  y.46.
8984:■  44-\i\  —  °rs  (statt  DP.)  pautrS  äma- yiinte  (sd.)  mazdayasnaiibyö  vä  dasvayas- naiibyS  vä  V.7.36;  —  in  Indir.  Fr^e:  asö . .  yn  .  .  varssxii  .  .  vafnaiti  'rö  ir/ravB (sd.)  Vit  ^bunai'o  va  Yt  i4.  31.  ^6". 10.  a)  ASn.  °r$m  mit  vä  ..vä  'utrum .  .  an  .  .?';  'nm  *ä^rava  diiauruiiMn  vä parayat  gaei^artqm  Vä  asp^rMif  (sd.)  avat N.  j;—  'rJm  asava  vä  dngva  va  vsrm- vaili(%A.)  mazys  'H.31.  17.  II)  als  In- liefinitum  'uterque',  mit  folg.  «/"';  pita puirasca  ..  'iaras/il  (NSm.)  Y.ff.  5;  — späoa  .  .  rast^m  (sd.)  rasma  Harascit  Yt. 14.  43;  ig.  46,  Vyt.  47; — yezica  vä gag>a "iTwJ  (sd.)  *°iarasap^  *paray3t  N.5; aaavalö  *'tarasat**  ratufris  yavai  frama- r«A'(sd.)  N.  2j; — yazäi  3xstlm..suyqmca •tarpmaiYU5.i<7).  a)  ASn.  '/arascij^' 'nach  beiden  Seiten  hin,  utroque':  p»rma
11016:—  %ioähü  gathaha  tanmica  Y. 43.T;  — 3^ai^  syaö^anai^  hisvasca  Y.5J.  13;  — msr^tB  bpfstaca  damayäi  V,  2.3;  —  dasä aspa  aHnavaitlS  idtrtmcä  Y.^^iS;  — vokB  manatsha  aläls  Y.34-151 —  asoAe vahistahe  a^rasca  Y.  i.  4;  —  ahya  artlOui astvalB  manarfhasca  Y,4j.  3;  —  narqm asaonqm  dafnayasca  Yt.  7^.69;  69;  — hävöya  bäzvB  dannaca  V.?.  25;  —  afys dsikrabyS  aiwyasca  yaoxstibyB  Yt/o.  Sa;
11045:Aqscay.31.11;  32.11, !tJ.iS,45.'i;  —  ivaya ..dn-alai^a  asoonaita  Yt, /o.  2; — /.iuyan- taScä  västryäicä  Y.  2p,  6 ;  —  Aaväi  kämäica taosSua  YtJj,33;  —  yavas^a  yavaSätae'a Yt/j.So;  —  n>r»byasca  näiribyascä  Y.54. i;  —  niayal^a  upa.b»ntayal^a  N.  4S',  — tayäal^ä  Aazatghaicä  Y.  12.  2 ;  —  asnaatca xsafnaat^a  Yt  5, 1 5 ;  —  aiwtta^aca  spasi- 'ta^acaYtig.6;  —  %waAmaj  3'^riis^a mana»Aas/ä  Y.46.T, — glusca  vastraheca Yt/J.ioo; — apB  yat  snaliintylica  sras- äntySica  V, 6. 36  (s. dagegen  33 ;  Sp.564m.);
11061:masdaaai^m  baiSaz^m  Uta  am3mca  Yt  14. 2.  2)  beim  zweiten  und  den  folgen- den; A)llim  Ap.;  kSrahya  abtcarÜ  gai- ham/a  maniyamcä  ftiaibi/ca  tyädis..  Bh, 7.14.  b)  im  Aw.;  1)  die  Glieder  sind nominal;  a)  sie  folgen  sich  unmittelbar: *hub}r>itlm  *uSta.bfr9itlmca  *  vantä. b>r}i- ilmca  Y.62.']  (s.  dagegen  i;  Sp.S72  o.;  — :^'ar>n5  avasca  rafnasca  Yt.  13.  i;  — hacimnS  *mi'iira  rasnuca  armaitica  Yi.  13, 3;  —  tuda  abm  vohuca  tnanS  xsa%r>mi'a Y.  2(),  1 1 ;  —  brata  te  .  .  sraosö  aryS  ras- nulca   bsmS  amava   mi^rasca  Yt  l~.  16;
11131:•  j.  caxra'vant-  Adj.  (fem.  •vaia-)  'ein Rad  (als  Feldzeichen)  führend"':  hafnayä 'vailyh  Aog.Si.
11921:•  j.  tafnav-m. 'Fieberhitze, Fieber':  ffaiTZÄ-a
11926:•  j.  tafnah-  n.  i)  'Hitze,  Glut'  (nur  Ab- leit.).  2)  'Fieberhitze,  -glut':  yaiÖa  hi hqm  °nS  jasat  (Sp,  501  u.)  avi  tanuye  zsis- nuye  V.  7. 70.
11931:•  j.  tafnah'vant-  Adj.  'Gluthitze  enthal- tend':  mäaA^m  ..  *'natfhuntfm'1  Ytj.S-
12660:—  haca  '%ulat  mazdi  Yx. $.  7; —■  ys  °%va sf^nts  mainyus  \L  10. 143;  — '^usS  'dtisö dadOibÜ  (s.  o.)  raocibls  Y,  j&6'';  — *xi»ümaine  '%usS  N.  4j.  a)  da'äusS et)  (nämt.  mä)  heisst  der  10.  Monat  im Jahr:  aiiaiilm  maihyäiryehe  (sd.)  '"^usö v>r3%rafnafu  k.3. 11.  ß)  (nämL  ayars) heisst  der  8.,  15.  und  23,  jedes  Monats: °^us3  akurake  mazds  ratvalS  . .  S.  i.  8, >S.  23°';    vgL  2.8,  IS,  23,    Y./6.  4-6;
13550:•  j,  ■*'d»r»zäno.p«r«9a-"  Adj.  'starke, schwere  Sühne  (durch  Leibesstrafe)  er- heischend': *sfayäti . .  dafna  mazdayasml '%im  pänm  (sd.)  V,^.  41.
18613:•  j.  ^nava  indekL''  Zw.  'neun':  ya^  Ai  'va (als  Nom.)  xsafna  lacantt  Y.g.  35,  ig.  23; i/i.  10,  1 1 ;  —  'va  (als  Akk.)  ptrüwS . . i^rmuFa  V.2.  ^o;  5.  $1,  ().ii,  ii.jaPüZ., 10.18,  14-14,  17-6',  /^.aiPüZ.,  22.ao', P.g,  Yt4-ö(?>,  /9.41;  —  °^'a  «/«  may^m'^ V.5,  54;  —  -zraÄ  yatkj  navaitisca  °vaca sata  'va^a  hatattra  navasSsea  (sd.)  batvqn y.22.3;  YL/j.  59;  —  'va^a  navaÜTm^a "99"  Yt5. 8a;  —  'va  sala  upäzananqm V.  ^,  15;  15;  —  'va  (als  Instr.)  satäts harta.cnanqni  V,  4.  9;  —  *°va  *sat-lts^^ hazannmla  Ytj.  120;  —  'va  (als  Dat) druJaiH  xsa^raaiyd  V.4.10  PuZ.(?);  —  1 'vaijqm  (Gen.)  aspatiqm  ar/ham  V.  22. , 30;  —  *m?nääidyäi  (sd.) . .  'va  dasmi  Y.
=== hvapah ===
10715:gAw. :  ahya  '"kräXa  maziiiäcä  *hvapa- nhäisca  (sd.)  tsm  at  ,  .  yasamaidl  Y.^J/. a;  —  kudä  (sd.)  asim  vohuca  maus '%r)m^ä  Y.  25.  1 1 ;  —  yüism  aäbyS  .  . aogü  data  .  .  '%nmc3  .  .  yl  kuhitts  rä- mqmcS  (sd-)  däl  Y.  2p.  10;  —  isasä  (sd.) . .  maibyö  '"^nm  aojönahvat  yehy3  vfndä (sd.)  vanalmS  *drujim  Y.J/.  4;  benutzt V.ao.  8;  —  tat  mazdä  tava  '>rfm  yä  .. düAf  drigaov!\sA.)  vaiyj  Y.ß^.g;  — yJ vahyJ  varihSuS  dagdi..ahurö  '"S^rä  mazdä Y.5J.  6;  —  tici  '^rä  mazdä  dqmis  (sd.) ahurS  'V.4$.T,  9;  —  maibyS  masds  tavä rafinS  JräxStuiam  (sd.)  kyat  ^wä  °&rJ a/Jt  hacä  frqifa  Y.  4!?.  1 4 ;  34. 15;  —  y} dfmanahyä  'hnm  M^rahya  vä  daSySu:" va ../radahäi{sA.)  aspinzatä  Y.Ji,  16;  — yastJm  °ärJ/  mazäJ  mSÜai  (sd.)  jyätSul Vä  Y.  46.  4;  —  at  ratqm  zara'iuitrS  .  . dadäiij  paurvatätim  . .  mazdiU . .  ux^aHyäcß (sd.)  ifraespm  '"irimcä  "..  den  Gehorsam und  die  Herrschgewall"  \.33.i4;  benutzt Yt  IJ.  88 ;  —  vauhstts  dazd,l{%ü.)  manau/iS lyaöhananqm  a»fiSus  mazdäi  ''knmca ahuräi  a  X.2-j.iy,  —  hux^a^rSJimäi (sd.)  .  .  '"ir^m  .  .  äad)mahicä  cismahicä *hvqnmakicä  Y.^5. 5;  —  yS  dngvSUi '"^nm  hunüiiJ  {?,d.)  Y.j/,  15;  —  yais *ffrMm3{sd.)  asäivaratä..°'^r3mca  lianqm *dnfim  Y. 32.13;  —  '>rais  yujin  (sd.) karapanU  .  .  akäis  syaohanäis  .  .  Y.  46. II.  a)  mit  Gen.  'über  — '  (s.  2  a);  tarn
20155:ahyä  xlahraca  'jUnäOSyä  ^hvapanhäiS- (sd.)i'a  tSm  (näoiL  akunm)  yasamaidi  Y. 3'J.  2;  —  mihnm  .  ,  yahmi  ..  'sa  amava nilahm  Yt./o.  64(?).
30643:hvapah-
=== amayava ===
2531:y.  I ;  —  cayö  'te  raola  at»A)n  . .  yö  ava^a  '  vayrjanake  .  .  yat  °&o  kanjasante  paouru Sraoiayeite'^.2.^<j\  —  "taFsva  daxtnaih'a .gaonaAec'a  IsA.)  . .  ti.6^\  yi(7);  —  taotarf yöi  faiti  äya  z^mä  iavainti  "V.y.^^;  — ^.gstava  ..  ■""'oa'*  ..  N-tVi;  —  yetiAe  'oa "U  malsma  .  .  yaHbyö  .  .  framayattte  V. .  mazdayasnanqm  näirika  . .  *ham.raf^wa- (S'.ii;  —  'taisam  syao^nafiam  yöi  v»r>-  yeiti  "wes  von  den  M.  Frau  dort  . ."  N, sjbA'  masy.lka  V.  J5.2;  —  "tiitbyff  zao-  11;  —  ava'ia  ''QrtV.4.50;  —  taica  "'jaca >rabyö  ..  yämham  ..  N.  71;  —  ku^a  -tat  pü^nm    baraili    Y.iy^^if).  a)    mit
3568:Vgl.  apc ;  ape  :  apaya  ^  harne  :  hamaya  ?
3627:•  j.  apa-stütay-  f.  'das  Sichabgeloben, Abschwören':  yä  haca  damayat  mazda- yasnSii  'Biiis  "das  Abschwören  dei  mazd. Religion"  N.41.
4009:'nicht  hervorwachsend,  spricssend'. Pflanzen:  urvaranqm  . .  yä  para  ahmat histfitta  .  .  ^'yäntis  (NPf.)  hamaya  gätvS Yt.7J.SS-
4024:—  "ha/sne  {sA.)  *afnat»ukh  F.  2C  \aAmät  kisipnla..'kusisi^Vi.)  hamaya gätvif
4693:«  j.  amayavä-  f.  'Leid,  Drangsal':  paiti- staue  xlayasla  'vayasca  "um  zu  widerstehen dem  Jammer  und  Leid"  Y.'!.!"}.
4724:6itTm  .  .  x/lßm  cvat  kaca  'yaätyB  "ein  •  j,  *ama-,  g.  Sma-  m.  i)  'Kraft, Loch  sollst  du  ausstechen  .  ,  Wie  weit  Stärke,  Macht":  n^ar^nö .  .  balsazim  Uta von  einander  (soll  ich  sie  ausstechen)?"  'mtmia  Yt/4.2;  —  manmn»m  (sd.)  ,. V.p,8'>.  damayai  "Tmm.  .tanuyeXX.i6.\T,   19;  —
4777:ahmst  sISi  dqn  (sd.)  trvjh  utayüitl  Y.  4I5. 10;  57.7,  44.18,  47.1;  —  0,a  haurvaia "rstäta  ySi  slö  /nlzd»n  asaonqm  parSMsti jasmtqm  Yt.  1.25;  —  mazS  (sd.)  avaKyai .  .  daidl  Aaurväd  Titätä  (GD.)  V.  5Ä 7.  a)  als  Bezeichnung  fiir  die  Speise der  Seligen*;'*  at  löi  ubl  haurvassa 3^ar?%äi  3  'r^atasca  (NS.)**  "und  deine beiden  werden  zur  Nahrung  dienen,  der Wohlfahrtstrank  und  die  Unsterbltchkeits- speise"  Y.,?4.  n.  A)  als  Gottheit  {Amasa Spmtd),  der  die  Sorge  für  die  nützUchen Pflanzen  anvertraut  ist  (SüErL:  vanas- patipatiliySi  aya  damaya  fraonnta  akurd .  .  vohu  manu  .  .  a£>m  . .  xsa%rpm  .  . ärmaitil  frä  kaurvatas  fra  'r>tatils  Y.57. 24;  —  vanät  haurvasca  °rstas^a  (NS.)" •wa  sUMtttca  farsmmla  Yt  ig.  96 ;  96 ;  — armaitfm  ..  haurvaiat^m  ..  'rsiatatsm  yaza- maide  Y.16.%;  JI.12,  S,  2.6f.;  —  mazdii dadat  akurö  haurvatö  'riiatascä  .-.  sarS Y. 31.21;  —  data  vj  'rjtSscä (NS.  als VS.)i> utaySitT {%A.)  kaurvatas  draonsY.33.9,;  — iaurvatas^a  'r)tatasca\t.4.i(f)  a)bes. i  in  Dualverbindung  mit  Aaurvatät-:  aya I  damaya  fraornnta  ahurd  masdä  .  .  fra ,  sp^nta  *armaitis/ra  haurvaia  °rHäta  (ND.) Yt.  JO.92;  —  sarBi  bszdyai  (&d.)  haurräiä I  "niaia  (ND.) . .  j?.  .  Y.44.17;  —  upa.- ßm^ti  (sd.)  haurvatä  °r>talä  (AD.)  Y.  45, .  5;  —  sp)ntayai  ärmatSe  haurvalbya  -ntat- '  bya  Yt.  7. 2 ;  H.  i.  7 ;  —  yS  spsntaya  arma- töis  yä  haurvatä  'ntata  (GD.)  Y.  70. 3 ; .  —  kaurvatasca  nö  'ritats,'''^ gTusca  tasiiö.. I  Vr.  g.  5,  a)  amir>tät5  (näml.  ayar?) heisst  der  7.  Monatstag:  S.  7.7;  vgl, 2. 7, ,  V.  7tt.3,  A  1)  als  Bezeichnung  für  die
6613:iViaV.Äio?;   107; —  aisä  astt  damaya  ,imas3  tl  kaoma  gä'ia  ima  Amli  staomäyB
8844:ayä  kahmäi^^  vananqm  (sd.)  dadh  Y. 4^15.  a)  mit  Gen.  part:  kö  hg  . . ae%rapaitinq7r^cä\  *afraoxti  (sd.)  astryäü N.  75 ;  —  kahmät  mazdayasnanqm  har»- 'hrtm  barät  V./j.  17;  N.  6'/,  G2;  —  kake vS  urva  /räye^ät  "^cuius  vestnim  anima . .  ?" Yt  13. 50;  —  iat  vast  (sd.)  iaj  vä  stBlö kat  Vä  yamahya.  "quid  vis?  quid  laudis  . ." Y.J4.12;  —  kat  tBi  as'ä  xbayetai  (sd.) avanhs  .  .  kat  .  .  "quid  . .  auxilii  .  ." Y.49. 12.  A)  Nom.  in  'Ist'sätzen  (s. 'a/i-  III):  ks  ahi  yS  mqm  zbayeln  \Liy. 17;  \.g.i;~  kö  asti  iraosahe  .  .  sraosil- var>zs  W.iS-n;  2.43,  7.78,  (y.31«,  Vt. 14.  i,  F.5;  —  if  airyama  ki  x^aetus" (sd.) datäisf  aukat  \.4g.T,  —  /«/(NSm.)  aAl ka/iyS  aht  (sd.)  Y.  4J.  7 ;  —  / 1*'/*'  hau  as .  .  yS  .  .  hö  aiiO  äs  . .  a/pmaayj  .  .  yO  .  . V.  y.5if.;  —  iai  tl  asti  ahunahe  vatryehe kai'^lm  P.  27;  —  kat  asti  mq^rahe  .  . amavast^tuMit  Vt./.i;  if.*,  /2.1*;  —  kal asti  damaya  .  .  uruiiwar»  V.j.30;  — '  cit  oval  vacö  äs  .  .  yat  .  .  Y.ig.i;  — /a/(NSn.)''  laoiar/ {sd.)  kainm  anhat N.72;--/«j(NSn.)"  aiüke  asti  uzvarsz^m V,  jrf.36;  —  hat  asti  ra'iswqm  /ram»r>itis Y.  7;.  I ;  I ;  —  kal  ait'ihe  asti  paititis  (sd.) V./A68;  68;  —  kat  sT  ('quidnam')  asti . .  tistTyehe..däity^i>inö  yasnasea  vahmasia \tS.$j;  —  las(SSa.}  aiMe  asti  bassass Yti4-34.  a)Kopulafehlt:  ks  ila&aSs'qm ar.mqm  paoiryö . .  hö  bä  aütaisqm  arsnqm paoiryü  yai  ..  Y.if/.^^t.;    —    k)   asavä
10298:•  j«  g-  gätav-,  p.  gää'av-'>  m.,  n. I)  'Ort,  PlaU,  Stätte,  Stelle':  bamUta!- sva'a  paiti  'tusva  V.6.^$;  Yt  75.53; apqm..yi  para  akmät  hist?nta  ..  hamaya 'h'ö  (LS.)  Yt  13.  53;  55,  57;  —  ap5  -tav, (LS.)  rJmSiow?m  yavata  ,  .  "o  Wasser, verweilet  an  dem  Ort,  so  lange  .  .' ü'5.9;  —  nalca  .  .  *häu  nl  akmat  haca •taot  isalla  .  .  apasUtoit  (sd.)  P.  23 ;  Yt. J.17,  i6.t;   —   airime  i^A.)  °iBm  kl  nis-
10855:•  j.,  g.  xSi-  f  'Not,  Elend':  x^3  (GS.)''> dangSm  ayU  (sd.)  Umanhö  Y.31.20;  — paiiistaße  xsayasca  (GS.)''  amayavay&sla Y.7/.  17;  —  xUm^'>  F.J.
12785:j  —  mit  Numeruswechsel: %''ärayam  kärahyä  .  .  fyädÜ  gaumäi^ I  adifiiT  ".  .  des  Volks  .  .  was  ifanen  . JBh. /.  14;  —  tyJ'  imaiy  käram  aduruß- yast^  pasävc^  '//"  a'urJ'miadil  matUl dastayl  akunatd  ya%a  mam  iäma"  aAa* ava^ä  °»/'>  akunavam  Bh.  ^4;D  —  ö/n aoi  ibasSa  paityantu  i^yeja  .  .  yö  T  da%a ..yidf(AFn.)  daU  Y.65.8.  S.  noch Anhaug  a.  a)  zugleich  auf  das  gleiche Nomen  vorausweisend:  sparum  uldnm  . . yasla  dim  janal  .  .  spän>m  sTsdr^m  V. 13. 3.  3)  auf  ein  Relativ  als  dessen Korrelat:  yS . .  gai^i  aioAe  mfrrfmte  avi tu  °im  disyata  .  .  Y.  Ä  3;  —  yasca  .  . fatmmazS  gSus  da%at  nHl  'im  .  .  paiti.- pirfSimnB  bva  (sd.)  V. /<¥.  29;  Yt/.  18, II.  5;  —  s.  noch  Anhang  b  t.  II)  vor- ausweisend; i)  auf  eine  erläuternde nominale  Beifügung:  a  *'lm^''  iavaiti  aiwi.- vanyä  äagnS  yS  apaoi'S  ti^ImYt,S.if,  72, iZ  iäim),  aS  (^j^ffi)"';  —  ä  'im  ta  va^a ramayai  ahurS  mazda  ..tarahustnm  V.5. a  I ;  —  paiti  *'lm''' {ASQp^rfsat  sardhuitrs aridvlm  särqm  Yt.5. 90, 94  {dim) ;  —  ä  'im (ais ASa.) Jramraami  abm  vahiit^mHt.^.^; —  s.  nodi  1 1  a  und  Anhang  b  ß.  a)  mit lelativiscbem  Anschluss:  yaiaca  'im  janai .  .  yim  viptim  vä  V.  7.  52  PUZ.;  —  aOat 'im  vlspanqm  matistsm  dazdyäi  ahBmca ratBmca  yim  ahur?m  Y.  27.  i ;  tg.  la,  Vr. II.  i\.  2)  auf  ein  Relativ   als    dessen
12952:•  j,,  g.dflr3z-V.'stabilire;vincire'.  Praes. 1  ^r?«-'*,  i6(Des.)tfWwvi3-'>,  z^dtrnaya-, 30  (Iter.)  damaya—,  J-Aor.  1  dar»z-*^.
12961:mit  Aain  und  nl  'zusammenfesseln':  kam gava  nidamayahii3m'°'^  Yt. /.  a?.
15539:hin's';  a)  räumlich:  yat  barata  annm mainyüm  framitim  (sd.)  . ,  mva  'ri  Z3m3 karana  YL/p.  29;  —  yeähe  tat  jfar»w isat  .  .  Jraarase  vlspäU  avi  Harlan  .  .; •ri  yäii  (als  Akk.)  hapta  karlvqn . .  apatat Ytig.Si.  b)  zeitlich:  apqm..yh  para ahmät  Atslmta  . .  hamaya  gätv&  äar^yimät 'ri  zrvarum  Yt.  ;^.  53;  —  aat  d^ra  vT- car»nti  {j&nA.  frara^ayf)  dasa  "ri  xsafnö ".  .  decem  per  noctes"  Yt  13. 49.  Un- deutlich: yat  'ri  bansma  hanjasante  N. tf2*>.  2)  mit  Lok.,  nurgAw.  'in,  bei  -'»:
17259:•  j.  bi.xiapar-''  n.  'Zeit  von  zwei  Näch- ten', wobei  i)  Nacht  im  Gegensatz  zu Tag  gilt:  bi.ayarsm  •rpm'''  tanäm  framaya- yanta  "während  zweier  Tage  und  Nächte  .." Yt.  jo,  132.  2)  Nacht  als  Zeit  von Sonnenuntergang  bis  Sonnenuntergang: agta^a  .  .  tanüm  nidai^yqn  °r^m'*  vä %ri.xSapar?m  vä  ". .  auf  die  Dauer  von zwei  oder  drei  Tagen"  V.5. 12.
18697:srz.)  wer.."  Y.44.4;  3"*'; — is  urva'iä (sd.)  tpUamai  saraiuHräi  nä  mazdä  Y. 5/.  11;  —  kS  möi  paiSiii  ks  tnS  na  "i^rStä vistd . .  azää  {iA.)  Y.30.  i;  —  ataf  ahmäi .  .  üiä  (Sp.  134  o.)  ankaitl  .  .  yi . .  vandayaita  (sd.)  Y.50.3;  —  a^ yS  rna nä  trtanxlaiti  attyida  (sA)  ttvS  . .  Y.5/. 10;  —  at  yasßm  rtö'it  nä  is^mnS  äyst. (Sp.  150  Q.)  .  .  hs5  .  .  \.46.6;  —  yi  1/ ahmai  ?r?:ux'jä  {%A^  nä  däitl  '^.44.  19; —  aat  yd  na  hli  fräyazaite ..ahmäi .,  Yt 'JSi;  'S,  152;  —  Mä  tfm  urvaijm  .  . fräyavayöis  .  .  aom  nar>m  daitlm  y5  nä . .  frayatät  (sd.)  Yt  /.  24 ;  —  y3  . .  kv5 nä  */rasrBiäyäi  (sA.)  ifTf^Tvö  \ . 4ß.  i y, — /ivö  ma  n  a  sravä  tnörmdat  (sd.)  yS  ,  . Y._^2. 10;  —  a/  hv5  var^Aius  vahyä  (sd.) nä  aibJ.jamyät  yS  ..  Y.^^j.  3;  —  hvS  tat na  ahmai  dasdi(^^.  715  u.)  Y.5/.  19;  — hicä  nä  ßüma  nHaaharatü  hs  aiwyä- xsayatü  Y.5Ä4;  —  yezica  ma  hau  nä ava  snaHita  (sd.)  .  .  aJnavät  P.  2/j  — nai'a  paicaaa  *hau  *«J'^  .  .  isaäa  .  . apasütHt  (sd.)  P.  23;  —  aisS  nä  yS yaoidä'hryS  V.  g.  39,  40,  42,  ip.  31,  Vd. *?,  10,  V.  5.  41,  4.  49  (wo  naröy-,  — h'at  hS  nä  atthuyäite  (sd.)  cvat  hö na  alayäti  hat  ahmäi  naire  miidam aahatyl  .  .  A.4.^i.;  6',  V.Ä81,  p.  39', 44,  Y.Ö2. 1,  Yl/o.  i37£3;  —  yesi^  hö nä  paitiMncSit  yS  nöi}  apivatäite  damaya sva, "wenn einer.,,  der.."  V.^. 47;  —  taEca narSg3rpo5Ji3r3lasca{iA.)..'^.j.7^;  24;  — yasia  mi  aS^m  narpm  .  .paili  utiärayat sva.  "und  wer  ihn  .  ."  V.iS.  10; — paiti- tjm  ahe  nari yavaiea  ..  V.^.ai;  —  ndtt zT  ahmt  paiti  nairi  .  .  rSna  (sd.)  .  .  V. 7.  5»;  —  anätartta  a^byS  nprtbyö  . . yöi  .  .  Yt  13.  30;  —  hauca  *anayä  narä (GD.)  vohu  man3  jäg)r)bustare  arfhat yS ..  V.  4. 48.  B)  Ohne  Attribut  steht 'ein  Mann'  im  Sinn  von  'einer,  Jemand'; insbesondere  hat  der  NS.  na  in  der  Stellung der  Enklitika  häufig  die  Bedeutung  unsres 'raa.ii'-.yB  nar»m  anduIa{zA.)  sna'iajainti V.4.  »6;  18,  ai ;  —  äfs  nanm  jainti  vä V.5.  8;  8f.3;  — yB  *naire"^  aoxte  Jrä im  «Ä  (sd.)  "wer  zu  einem  sagt :  . ."  F. 4A;  —  na  tat  (Sp.  630U.)  paraJri^yeiti V.  5.  i;  a,  5;  —  mit  der  Negation  'nie- mand': nüit  spsJ>3ntS  .  .  nasui  nar?m nsil  *ästarayäti  V.  5.  3,  a)  NS.  na  in
19749:fUr  venmieinigt  gait'>:  j/ai /ü^,.mS/a  va para.irihyäti  hiai  allqm  upa.mqnayin  .  . h<at  dahmanqm  cvat  ^nu.pir^^nqm'i  ,  . 'kriiobM  dahmanqm  xlvasttm  tanu.ftn- %attqm  "wenn  der  Vater . .  oder  die  Mutter stirbt,  wie  lang  soll  man  für  sie  die  Trauer- frist aushalten,  wie  lang,  wenn  sie  d.,  wie lang,  weon  sie  t.  waren?  .  .  Dreissig (Tage)  wenn  sie  d.,  sechzig  wenn  sie  /. waren"  V.J2.I.  Wertlos:  nStt  sT  dl  yä pasu  vTra  x/ährs  ahmäi  aiaurüS  matiftya dl  latöis  manayäti*  kasiihm  uzyS^ramaya DkB.131.   *
19783:—  yS. .  upairi  hunanm  (sd.)  'tiS  baräi.. ^°nahe . .  '''naht  Y.3JI.;  — yai  iarytiaaiti driyagf  havaLmass  (sd.)  '»ff  ydisa  . .  Y. 10. 13';  —  Jahikayä  ..ye6he  ^/ra/ravatte 'nS  ya^a  awnm  Y.p.  32;  -^  iöistahecti  . . 'nS  ramayati  YL70.109;  iii;  —  para Tm  ^a  'naahe  Snasti  (Sp.  431  m.)  yt^a
```


## [2026-09-07T20:18:37.681Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD xwb ===\"; grep -n -i \"xub\\|hwp\\|xwb\\b\" PHD.txt PHD_mackenzie.txt | head -20; echo \"=== NYB ===\"; grep -n -i \"xūb\\|xub\\|hwp\" NYB_vol2_glossary.txt | head -20",
 "description": "Grep Pahlavi dictionaries for xūb"
}
```


### [2026-09-07T20:18:37.743Z] TOOL RESULT

```
=== PHD xwb ===
PHD.txt:400:huniyāģar [hwayd’kl | N xunyágar] entertainer, musician. hu-niyox$ [hwnydwhs] attentive. hunsand [hwnsnd | = P, (N xursand)] happy, contented. ~ih : happiness, content. hunušak [hwnsk' = Av. hunu§] offspring (daevic). hunušakēnīdan [hwnskynytn'] bear daevic offspring. hu-pādixšā(y) [hwp?thš”(d)) good ruler. ~th: good rule. hu-passandagih [hwpsndkyh] satisfaction. hur [ŠKL < A fkr; hwl] an alcoholic drink, *koumiss. huram [hwlm | N xurram !] happy. ««īh: happiness. hurām [л?т] blissful. hu-|-ramag [hwlmk'] having good flocks. ~-rust [-/wst'] well-grown. ---Süzagih [-s’ckyh] agreement. ~-8рӣз [-s5?s] grateful. ^ husraw [hwslwb' | (M hwsrwg), N xusraw] famous, of good керше у m ~ih: fame, good repute. Ms hušk [kwšśk! | = M, N xušk] dry. —-kün [-S TE] impotent. hu-škūh [kwškwh] dignified, splendid. ^h: dignity. hu&nüd(ag) [лото (А)! | M hwinwd, N xusniid] contented, happy. ~th: contentment, happiness. hu-tuxš [kwtwhš] artisan. huwaršt [hwwlst! = Av. hwarfta-] virtue, good deed. hu-xém [hwhym] of good character, good-natured. ^h: good character. hüxt [kwht' = Av. hüxta-] good speech.
PHD.txt:514:nihuftan, nihumb- [zhwptn', nhwmb- | = M, N <) cover, hide, conceal, clothe, nihumbidan [nhwmbytn'] = nihuftan. *nikóhidan, nikóh- [nkwh-ytn' | N ~] blame, execrate. ~išn: blame. ~išnīg : blameworthy, execrable. nil [nyl | N ~] indigo. nilópal [nylw(k)pl | N ~, nilēfar] lotus, water-lily. nimüdan, nimāy- [nmwtn', nmd- | M nmwdn, nm’y-, N ~] show, guide. nirfs- [nlps-] wane, decrease. ~išn: decrease, diminution. nirmad [nylmt'] profit, interest. ~ӧтапа [-’wmnd] profitable. P nisag [nys’k' | P nys’g] bright, splendid. niš- [nyi- | M nyyš-ydn, J ~] see, observe. nišān-, v. nišāstan. nīšān [ny$*x! | = M, N nisàn] sign, mark, banner. nišast [nsst! | N ~] association. nišastan, nišīn- [Y TY BWN-stn! < A V у; пт! | M nist, (nfyy-), N ~] sit. nišāstan, nišān- [Y TY BWN.stn!, 2n-; nP?stn!, nP?n- | M nf?st, (nP5y-), N ~] set, seat, plant, found. nišāyišn [n£ din! | M n$?y-, v. niSástan] foundation. nišēb [niyp | N ~] declivity; astr. dejection. ~ig [-yk'] declining. nišēm (nidm | M nšym, N ~an] seat, perch. ~ag [-k'] residence, abode. niSin-, v. niSastan. niwāģ [nw k! | M ng, N nawa] music, song, melody. *niwé [nwyk! | (N nuwéd)] good news. *niwéy-, -išn, v. niwistan, *niwéyénidan [nwykyn-ytn'] = niwistan. niwistan, *niwéy- [nwstn', nwyd- | nwyk-] announce, consecrate. —išn(ih): announcement. nixwār- [nswb’l- | M nyxw’r-] hasten. -išn: haste. niyübag [nyd’pk' | M ny’bg] becoming, fitting, suitable. ~th: suitability. niyāģ [nyd?k! | M nyg, N niya] grandfather, ancestor. niyāyišn [xyd?dšn! | N ~if] prayer, praise. niyāz [nyd?c | M ny’z, N ~] need, want, misery. —ómand [2wmnd | N ~mand] needy. ~6mandih: poverty. niyē(x)šidan, niyē(x)š- [n(y)duhš-ytn! | M nywi-, N niyófidan] hear. ~išn: hearing. І nizār [nz?l | (P nyz?*wr), N ~] weak, feeble.
PHD.txt:661:2xān [/?п! | P л?п] spring, source. хапар [BYTA < A рур; h'nR! | N хапа] = іхап. xandidan, xand- (*GHBHWN-yitn' < A V ghk, or У *ghqh; hnd-ytn' | (M xnyst), N —] laugh. xānīg [/?nyk! | M x?nyg, N xàni] = *xān. xar (HMRA < А hmr’; hl | N ~] donkey, ass. хаг [P1 | M ær, N ~] thorn. xar-buz [hibwe | M xrbwz] oryx. xar-g68 [higws | N ~] rabbit, hare. хаготапа [/PPwmnd] thorny. xār-pušt [/?Ipwst! | N ~] porcupine, hedgehog. xastan [hstn' | M xst, N ~] wound, injure. xašën [hsyn! | N хайл] (dark) blue. хауар [Pd(y)k! | N xdya] egg. ~-dés [-dys] oval, egg-shaped. xayüg [Ah )dwk! | N xayū] saliva, spittle. xaz [hz | N —] marten. xém [лут] nature, character. xëšm [?yfm, hfm | M xysm, N xifm] anger; the demon Wrath. --én [-ya! | M -yn) angry. xindag [hyndk' | M xyndg] ill, sick. ~th: illness, sickness. xir [C BW! < А sbw; hyl | M хут] thing, matter. xirs [hls | N ~] bear. xišt [Ast! | (P hystyg), N ~] brick. хбё [hwk' | N xwk, xóy] nature, character, disposition. x6n [DM YA < А dm’; һит! | M хоп, N хип] blood. xormā [TE A tmryn; hwlm’k' | N ~] date. xrad [hit! | M xrd, N xirad] wisdom, reason. ~ig, ~Omand [-yā!, тиа | N -mand] wise. xrafstar [hlpst] = Av. xrafstra-] reptile, noxious creature. xridan, xrin- [ZBNN-tn! < A V zbn| M xryd, xryn-, N xaridan, (xar-)] buy. xróhak [hlwhk' | N ~] coral. xrēs [DYLK A < A dkr’; hlws | P xrws, N xurós] cock. xróstan [Alwstn! | M xrwst] call, cry. xüb [hwp | M xwb, N ~] good. ~th: goodness. xuftan, xufs- [HLMWN-tn! < А У Ыт; hwptn', hwps- | М xwpt, N xuftan, xusp-] sleep. xūg [HZWL УА < А hzyr; hwk' | N ~] pig. xükar(ag) [hwkl(k') | N xūkara] hedgehog. xumb [kwmb! | M xwmb, N ~] jug, pitcher. xunak [hwnk' | M xwnk, N xunuk] happy; cool. xurdruš [kwldlwš, -dlpš = Av. xrwidruf] ‘with a bloody club’ (epithet of Xēšm, later misinterpreted as *ul-draff ‘*with raised banner’).
PHD_mackenzie.txt:390:with a hyphen. Thus lkwp-tn l denotes 'infinitive lhwptn l
PHD_mackenzie.txt:391:(= skuftan), present stem lhwp- (= skof-)', YMYTWN-tn l
PHD_mackenzie.txt:2970:hu-pidixsi(y) [hwp)thS)(d)] good ruler.
PHD_mackenzie.txt:2972:hu-passandagih [hwpsndkyh] satisfaction.
PHD_mackenzie.txt:3767:nihuftan, nihumb- [nhwptn', nhwmh- I = M, N -] cover, hide, conceal,
PHD_mackenzie.txt:5576:xiib [hwp I M xwb, N .......,] good.
PHD_mackenzie.txt:5578:xuftan. xufs- [HLMWN-tn l < A "II (llm; hwptn l , hwps- I M xwpt, N
PHD_mackenzie.txt:5623:xwarasan [hwPs'n'  '      I M xwr)s)n, N .......] sunrise, east.
PHD_mackenzie.txt:6668:    gahanig.                                     weh, xub, hu-, P naxsag; ,...., char-
=== NYB ===
2042:hu-évacéh [hw’dw’cyh] good manners in speaking, in conversation; politeness, courtesy 70%, — V. lēvāc. Paz. hūāvāži. hu-iramānēh [hwplm’nyh] the quality of exercising good command, of a com- munity: good rule 50%, with the gl. kū
2045:hu-fravart [hwplwlt'] having a good fra- vart (= fravahr, q.v.), Saint, venerable 1085, 11125,
2064:hu-pih [hwp’h] having good cattle 5076, with the gl. ki góspand veh dānēt daštan ‘that is: it knows how to breed small cattle in the best way’. — V. päh. huparyön: probably to be read *hu-parrón [hwpldwn'?] “of good re- verse side": beautiful from behind 5721, opp. hu-örön, g. v. — V. parön. The text seems to give the form hwplywn = *huparyön, but such a w. cannot be imagined here, as shown by the passage quoted s. v. hu-örön. Possibly the spell- ing should be interpreted as hwpldwn' with the spurious spelling -/d- for -rr- known now in the KZSPrth 1. 22 in fine: n. pr. prdk prdkn = Prs 1. 28 pldky ZY pldk’n, Gr. v. Dappex Dappixav; Prth 1. 21 init.: n. pr. fem. mrdwtyH, Prs 1. 26 init. unfortunately only mr ... left, but Gr. v. Mvepoč; v. also Nyberg, BSOAS XXXIII, 1970, 150. However, 57?! stands in a passage which is only known in Meherji Rana’s transcript (v. Dresden, p. 122, fol. 48, 1. 12), so the reading is not beyond doubt.
2067:hu-passandakéh [hwpsndkyh]: pat dat ~ in accordance with good equitableness in legal matters 64!’, v.s. v. passand.
2068:hu-pém [hwpym] having good milk, of cows 422.8,
2095:*hu-vaxm [hww’hm] “of good swing", epithet of the varz ‘mace’ (v. vazr) carried by Keresāspa 100%. — Renders Av. (1832) hu-nwiata- "well swung’, epithet of the vazra- of Mithra (Yt. 65. 10132) and of the vazra- in general (Yt. 10%. 1372); < m + vaeg-, v.s. v. ?vextan. Reading hypothet- ical, no Paz. reading being known to me. I take it as *hu-vexm < "hu-vataman- from *véxtan < vaig- (q. v.), which has been largely confounded with !vextan < vaik-; *huvērm > hu-vaxm (or perhaps better *hu-vahm) cf s. v. mahmän. As to véxtan as a battle term cf 254. — As Bthl (Wb 1832) has given quite misleading information about the Phl. w. I put here the notice he quotes in its correct form. It is found in the Phl Xvaršēt ntyāyišn (= Yt 6) in Zand-i Khürtak Avistäk ed. by Dhabhar, p. 21 $ 15: ké yast Ohur- mazd % amarg api-š yast Mihr 4 fragoyot . . . (l. 14) api-§ yast vazr i *hu- vazm | pat kamär apar i dévan | i Mihr frägöyöt (e: *huvaxméh € ku bāstān eton dàret: mēnēyīhā be šavet, vināskārān pã- tifrās bē kunét, u menöyihä apäc 6 kantir äyet) ‘he who has worshipped Ohurmazd the Immortal... has (at the same time) worshipped Mihr (the god) of wide (l. 14) and he has wor- shipped: the mace of good swing on the skulls of the devs, owned by Mihr of wide pasturages (its being “‘of good swing" means that it constantly behaves in the following manner: spiritually it goes off and punishes the sinners, and spiritually it returns to the quiver [sheath?])? NP v. xub nihädah, Skr. v. su-niyukta (Dhalla, The Nyaishes, 1908, p. 50). l
2716:nihuftan [nhwptn'] nihumb- [nhwmb-] to conceal, to cover: api-$ apar varr nihuft he covered himself with his garment 56?’ ; apar ~ to conceal, to keep from the knowledge of 8011 = bē ~ 8014 (read ‘L menišn 1. 13); in both places restore the reading of the MSS: nhwmbt' = nihum- bet (not -byt' = -bēt). — MPrs nhwft nhwmb- or nhwm- = nihumm- with assi- milation (A-H II, BBB); Paz. nahuftan nahumb-; NP nihuftan nihumb-. Verbum 200; Bailey, ZP 83 (82 n. 5).
2717:nihuftarčh [nhwpt?lyh] v. n. of the pre- ceding vb.: pat ~ clandestinely 6715.
4302:xuftan [hwptn'; HLMWN-tn'] x"afs-, to sleep, to fall asleep 52. 6%. 32%, — Av. (1862) x"ap-, pres. xtafsa-; MPrthPrs xwftn; Paz. x"aftan, pres. avaft-, xtafs-; NP xuftan, xuspidan, pres. xuab-.
4303:xüp [hwp ] good, excellent, agreeable 916, 3919, 5919; ~~ kartan to put in order 13°; adv. well, perfectly 7022. 817-8.2°, — MPrs xwb (S) not in MPrth., where xwž (S), xwj (A-H III) corresponds; Paz. NP xub.
7501:xirad: xrat xirämidan: äxräm- xiyär: hayyär xohal: x"ihl xösah: hösak xösidan: hošitan xub: xüp
```


## [2026-09-07T20:18:38.496Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN grep xub ===\"; grep -n -i \"xub\\|chub\\|hûb\\|hub \" HRN.txt | head -30",
 "description": "Grep Horn for xub"
}
```


### [2026-09-07T20:18:38.551Z] TOOL RESULT

```
=== HRN grep xub ===
6199:phlv. spöj (päz. spöz) 'Aufschub' (Salemann, Mel.
21567:w. hub 1098.
```


## [2026-09-07T20:18:52.308Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('HRN.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(\"npages\",len(pages))\nfor n in (130,131,132,133):\n    print(\"==== leaf\",n,\"====\")\n    print(pages[n-1][:2500])\nEOF",
 "description": "Print Horn leaves 130-133"
}
```


### [2026-09-07T20:18:53.641Z] TOOL RESULT

```
npages 412
==== leaf 130 ====
— 108
486. yi^usur 'Schwiegervater.
aw. /asitru' 'Schwiegervater ; ai. imruru-; arm.
skesr]ah\ d. i. 'Mann der Scliwiegermutter (Hübsch-
mann, Xo. 253).
kuvd. /a2ur, xozJ)\ /aur 'Schwiegervater ; afy. s^or;
bei. n. vasarik 'Schwiegervater, vasar\2ä/t *Schwager
(405); wa;K'. yjtrs, sar. (LW.) Xasur.
•Vergl. /Hsrä (No. 487).
487. xusrfi, zesä^ /jisü^ /'es etc. 'Schwiegermutter.
Käs. /asrii',
ai. <;DarrU' 'Schwiegermutter'; arm. akesnr (H. No. 253) ;
lat. socru-s; ksl. soekry.
kuvd. /ost, /esü, yasrü 'Schwiegermutter; af/. ;K''ö4fa ;
bei. V((8sö, vasl, vase (406) ; wa;^. /as, si/n. /as, sar. /,e/.
Vergl. ytisur (No. 486).
488. x^Ht 'Ziegel, Backstein'.
aw. istya- 'Ziegel, Backstein' ; phlv. /ist ; skr. isfakOr-
'Backstein'.
afy. LW. /ßta; bei. ist (168).
489. ^usk 'trocken', /ös« ') 'Ähre', yös, yöslden, yösdniden
(AM. 236 Zeile 3 v. u.), /mkUm,
Kä§. tisk (jendn, husküdSn.
ap. Msia- trocken'; aw. huskd- 'trocken*, aflluiosemnu'
'nicht vertrocknend'; phlv. /<*^Ä;, /usklh^ /ösTnUän
(Bund.)-); ;rösaA; 'Ähre' (Bund.); ai. güska-, güsyati,
skr. gösa-.
kurd. LW. hüsk; afy. vud; oss. /tisk, ba/ussin (311
und Seite 141); bei. husay 'trocknen, austrocknen (160)
(LW?); wa/. vesk,
np, /uskar {/usk ärd, Vullers, 756, vergl. dial. ör,
oben No. 13), arab. LW. x^iskar 'Mehl', phlv. /nsk[a]r
V
(vd. 6 (9) Gl., Say. näsäy. 2, 35). Vergl. de Lagarde,
Semitica 1,41, Nöldeke, ZDMG. 32, 408; de Lagarde
*J Phlv. ;(Osak (Sternbild, Bund.); kurd. t*st, vasi^ krisl; afy. vazai;
bei LW. hösay, d. hösay (100).
2) Vd. 5 (43) (44) steht zwei Mal xösinUan,
==== leaf 131 ====
-- 109 -
will auch np. /äsdk (jüd.-pers. T^^Z, Is. 7, 24) heran-
ziehen.
490. xiSm, xesm *Zorn*.
aw. aesma- 'Zorn*; phlv. /ism, x(h^fi^'
491. yi^eSTn 'bläulich, blauschwarz'; vergl. x^sisar (äähn. I,
157 Vers 510).
aw. a/saena- (Darmesteter, Et. ir. II, 53); phlv.
/asTn (Jamaspji, Pahlv. Dict. II, 421; falsch asgun,
asTu, 241), ;^ai;fm« oder axsin(?), vd. 22 (12).
kurd. stn, heslu 'blau ; afy. s7n bezw. xtn; oss. ä/sinäg
'Taube (46; vergl. Hübschmann, ZDMG. 38, 427/8);
sar. xoin, siyn. soin 'blau, yidg. ayßin (Tomaschek,
BB. VII, 204).
492. lele {jule) 'Wunde, Spitzes; Geschwätz', /ehden,
aw. hareöis; phlv. havak bezw. yarah^ vd. 2 (89).
Die Etymologie stammt von West (PPGl.s. vJialeh);
die Bedeutung der aw. und mittelp. Worte ist unsicher,
ebenso die Grundbedeutung des neupersischen. Im Men.
fasst West päzJiala als 'foolish, silly'. de Lagarde,
Beitr. z. altb. Lex. 38 wollte aw. /"ara- * Wunde' ver-
gleichen.
493. %ufn^ ;^Mw/;, yiimh Topf, Krug , /umre (HIOID, Is. 13, 12).
aw. /umba- *Topf ; phlv. yurnb*^ ai. Jcmnhhd',
kurd. LW. /um: bei. kumb, n. fftimh 'Teich, Pfuhl;
mit Wasser gefüllte Vertiefung im Felsgestein* (204);
wa/. Imbun,
494. fmkde 'Gelächter, ymdtden.
phlv. /andlta^i, yandak (PPGl.).
kurd. kenin 'lachen' ; bei. kandag, n. Uanday, yanday,
LW.') handag (186); wa/. känd-am, sar. söwrf-am (?).
oss. d. ;^odww, t. ;^wd/w (303) scheint hiervon ge-
trennt werden zu müssen und zu [/^svad- zu gehören.
Oder ist doch Urverwandtschaft vorhanden?
ffindeq 'Graben' siehe s. v. kenden (No. 869).
») Vergl. Bartholomae, ZDMG. 44, 550.
I
==== leaf 132 ====
— 110 —
495. lym 'Schlaf, /ahtdefK
Kä§. ;^öw?[es; hevoft 'schlafen*.
aw. /'a/wa- *Schlaf; phlv. /*'äÄ; ai. svdpiw-; arm.
^un (H. No. 295).
kurd. /evii, /evin; af/. LW. yöb; bei. ^?a/>, n. väir
(410).
496. x'^^^ 'leicht, gerade; niedrig, verächtlich', x^^ärT,
aw. /'ad-ra- (Geldner, KZ. 25, 478, Studien I, 17
folgg. ; Darm est eter. Et. ir. II, 189)'); phlv. /"är, nur
in der Bedeutung 'leicht', /"änha *leichtlich' (Sa le-
rn an n, Mel. asiat. IX, 234).
LW. kurd. /(^r; afy. /'är; bei. vär (290).
Die Bedeutung 'niedrig, verächtlich' ist erst neu-
persisch.
497. i^äfiten 'wünschen, wollen, Praes. /"ähem, /"äliis,
/"äste 'Besitz'.
ai. l/^soad-, svädati 'sich schmecken lassen, Gefallen
finden*, svädate; gr. rjdoftat. Vergl. np. /iväi (No. 502).
phlv. yyastan 'wollen, wünschen', /^ah(i)§ff, x^stär,
y^astak 'Besitztum' etc.; kurd. /^dsthi , ;jfMSfni; bei.
vergl. västa 'für "(413).
498. x^äW/ 'Tischdecke; Tisch (gedeckter)'.
aw. /^'^aini' 'Teppich, Überzug, Decke',
kurd. LW. /an; af/. /^än; bei. n. vän 'Platte, Teller'
(289).
Geldner, Studien I, 17/8.
499. yiyänden Vufen, lesen etc.', /emden, /unlde, /unyä
'Musik, /unyäyer,
aw. l/";^^«;/- in /^anaf.ca/ra- ('klirrend'); phlv.
X'^äntan, /untt (GF.) ; ai. [/^svan-, sodnati 'tönen'.
kurd. y^ändin^ /ündin 'lesen; oss. d. /önim, i. xöJiin
'nennen , heissen , rufen , einladen' (305) ; bei. vänag,
n. vanay, vänganay 'lesen, recitiren, studiren' (412);
wa;f. ^an-am 'reden, sagen, sprechen'.
*) Sahn. I, 170 Vers 745 steht np. j^^är direkt im Gegensfttz zu
(hfsvär, wie im Awesta '^^äSra- zu (Inzä^ra-,
==== leaf 133 ====
— 111 —
500. ^fyalTden *f?chmeckon' , /^al 'Speise', /^älger, /^älf,
X^'ältger.
aw. x^arezista-; phlv. /^list (vd. 2 (77))'); arm.
l^alcr 'süss (sehr unsicher, H. No. 287).
501. polier \Sch wester, /ö/j.
g. yohr; Käs. /üh, yöh,
SiW. /^afihar- Schwester; phlv, /^'ühar, ytlk {PPGl.);
ai. svasar-; arm. ^^oir (H. No. 294).
kurd. xöh, ;c^A^» ^^^^ (H.-Sch.), af}'. yöt' ; oss. d. /ore,
t. ;ro; bei. gvahär, n. gvähar, göhär, gvär (131) 2); wa/.
;^m/, sar. ya;^, minj. yayvd, sangl. i/vd.
502. x^**^^*» /^^^^ 'Wohlgeschmack'.
skr. sräda- * Wohlgeschmack*.
kurd. x^ *Salz ; bei. väd, n. väd, vad\ vü:: (411)
'Salz.
In diesem Worte hat sich die ursprüngliche Be-
deutung der [/"svad- im Neupersischon allein noch
erhalten; vergl. /^'dfiten (No. 497).
503. y(nb gut, schön , /hIü.
Ka§. /ßh, /öb^ /eb.
aw. hväpah' 'wohltätig; phlv. /rap bezw. /üp,
Xüpih; ai. svdpas-'^),
504. lud, ^eS (AM.) 'selbst'.
Käs. x^d.
ap. vergl. wrö- ; aw. yyatö 'selbst'; phlv. ;^^a^, j^^'a/^Ä ;
ai. svdtas,
kurd. ;^i2 ; af/. ;t'/>'<^ ; oss. d. x'^^^^^9i t. /ädäg (298) ;
bei. i?a^, n. viixt^ vas; äiyn. ^w, sar. /w, wa;^. ;frti, gen.
505. x'*^* 'Sonne', hur, hör (reimt auf .<??^^ör; Sahn. 111,1105
Vers 693), Xurasan,
*) So korrigirt D armesteter, 6t. ir. I, 136.
') Yergl. Bartholomae ZDMG. 44, 552, Hübschmann ebenda
557, Geiger, Lautlehre d. Bei. § 15, 3. Uraprachliche Dialekt-
Verschiedenheit.
«) Ebenso Fr. Müller, WZKM. 5, r>7.
```


## [2026-09-07T20:19:10.244Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SOD xwp ===\"; grep -n \"xwp\" SOD.txt | head -20; echo \"=== SOD amʾn ===\"; grep -n \"\\bʾmʾn\\|'mʾn\\|ʾm ʾn\\|ʾmʾn\" SOD.txt | head -20",
 "description": "Grep Gharib Sogdian dictionary"
}
```


### [2026-09-07T20:19:10.313Z] TOOL RESULT

```
=== SOD xwp ===
36757:xup   ©adj.  &  adv.   =>xwp 
36779:xuptar   (Ywpwtr)   =»xwptr 
43339:5350  mndxwpy(y)   M 
43340:mand-xupe  =>mntxwpy 
43681:5395  mntxwpy   C  f^J^l;  <c^jU.U 
43682:mandxupe   ^mndxwpy(y) 
46923:5835  n>xwp   M 
80536:10710  xwbn   C  =»  xwpn- 
80538:10711  xwpn-   M,  B  ^1^ 
80550:10712  xwpw   S,  B  .li 
80740:10739  xwp   M,  C  4^«i 
80741:xQp  ©<Av.  hvapak  Skt.  svapas  «»mntxwpy, 
80743:n>xwp,  Ywp 
80748:10740  xwptr  C  >Vj 
80753:10741  xwpy(y)   M,  C 
80754:xup(e)  ©in  compd.  =»xwp,  mntxwpy 
83382:11105  yxwbny'   C  =  y-,  +xwbny*  =»  xwpn- 
=== SOD amʾn ===
```


## [2026-09-07T20:19:11.497Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HUB xub ===\"; grep -n -i \"hvapah\\|svapas\\|xub\\|/tib gut\\|hüb\" HUB.txt | head -20; echo \"=== HUB pages ===\"; grep -c \"\" HUB.txt",
 "description": "Grep Hübschmann"
}
```


### [2026-09-07T20:19:11.565Z] TOOL RESULT

```
=== HUB xub ===
1972:*a;''ai oder *x^ab statt xUb erwarten. Ich setze xub
1973:(paz. xUb Shk. 254, afgh. LW. xilb 'schon) = skr.
5987:xub gut, schon = skr. suvapus-;
7639:(neben hujlr, hmlr) 'schSn' = zd. httdid^'a-; xUb *sch5n' =
7650:Shk. 251 verdaehtig ist, xub schSn*, xm Blut', xUram (xuram)
=== HUB pages ===
10983
```


## [2026-09-07T20:19:26.862Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('HUB.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages,1):\n    if 'suvapus' in p or 'xub gut' in p:\n        print(\"=== leaf\",i,\"===\")\n        print(p[:1800])\nEOF",
 "description": "Locate Hübschmann pages with xub"
}
```


### [2026-09-07T20:19:28.172Z] TOOL RESULT

```
=== leaf 68 ===
- 57 —
498. Zd. x^aini" wird von der Phi. tTbersetzung durch
xup *schon* wiedergegeben, das vollkomnien passt. Die
Zusammenstellung ist also falsch.
501. Np. x^ahar Schwester aus ^jf'ahar, vgl. skr. ace.
soctsaram, Ahnlich ware np. bahar 'Friihling' = phi.
vahar aus *vahar entstanden, wenn es zu ap. d^uravo-
hara- geh5rt.
502. Dazu np. nctnx^ah 'Ammi' u. s. w. als *Brot-wurze',
afgh. x^and 'Geschmack, Wohlgeschmack, Vergniigen
(Geiger) , kurd. xevS *Salz* ZDMG. 38, 64. Falsch ist
wohl die Aussprache x4/va, fiir die man x^a nach alien
Analogien erwarten muss. Vullers ftihrt x^ai neben
xiva an. Auch nach N 5 Id eke ist das Wort einsilbig.
503. Nach dieser Etymologic sollte man im Neup. *ipwi,
*a;''ai oder *x^ab statt xUb erwarten. Ich setze xub
(paz. xUb Shk. 254, afgh. LW. xilb 'schon) = skr.
suvapus' N. pr. (von m gut* und vapus- 'Gestalt, Schon-
heit').
505. Np. xor = x^ar 'Sonne* ist = zd. *x^'are, gen. x^mg-,
dagegen hdr 'Sonne* = zd. hvare^ gen. Awr5, skr. suaVj
gen. sfAras. Also geht xorsBd (Nr. 506) = x^arsed
*Sonne = paz. x^arsSd Shk. 255 auf zd. "^x^are-
xsaetem^ die Nebenformen von hvarexsa^tem zurtick.
507. Arm. xortik^K plur. *Speise* = zd. x^areti-, phi. x^ar-
iik^ np. x^ard% 'Speise*. Das afgh. Verbum schreibt
Geiger x^arql *essen, geniessen, trinken*. Arm.
*xortak findet sich nur im Denom. xoriakem 'schlage
in Stiicke*. Das zugehdrige np. xurda *klein, kleines
Stiick' kann mit lat. curitis (— gr. ^agxig geschoren'
nach Brugmann, Grdr. I, 238, zu ksl. hrattiku nach
Fick, Wb.'* I, p. 385), dem ein np. *A:»rrf oder *Aarrf
entsprechen wiirde, nicht vermittelt werden. Horn's
Bemerkungen tiber das anl. x aus k sind verfehlt.
Vgl. Fr. Mtiller, WZKM. 7, 373.
508. Np. x^aS gut, schon, angenehm' = zd. "^hvasi- (skr.
sval^Or-) sch5naugig? Moglich, aber nicht sicher.

=== leaf 180 ===
— 169 —
3) -dt?i- wild zu fl: askara *k\a.r ,^h\, askarak, skr. avis-
kar oflfenbar machen*, aviskara- *das
Offenbaren*.
Dazu np. basam *werde sein ? (das nicht = skr. bhavl-
syami (zd. ptc. busy ant-) sein kann).
4) em- im Anlaut wird zu ya- : yak ein = phi. ^vak
(vgl. nek *gut, schon* = phi. nevak, ap. naiba-),
aber b^var 'zehntausend' = zd. ba§vare,
5) Fro- wird zu I : ^is^an 'leben* (ziyam lebe', 5?i«da
'lebendig*) = paz. zTvastan u. s. w. Min. Gl. 225,
phi. zlvandak 'lebendig' Gl. and Ind. 152;
paz. pSy (lies ptg) = phi. pig oder plk Shk.
263, bal. p^g, nb. ^ty 'Fett* ans ^plvaka-; np.
pfA *Talg, Fett\ skr. ptvasd- *fett' (obenp. 46).
Dagegen zlva, jlva 'Quecksilber H. 683.
b) -ava- wird zu D : furod 'hinunter — skr. pravdta\
furosam Verkaufe' aus *fravaxsamij
yo2f 'Jagdleopard*= a,rm,yovaz, yavaz.
Vgl. auch sukDra (? neben sukurra, sukra u. s. w.)
patina testacea = arm. skavarak ^Schiisser; np. fordiydn
(neben fravardiyan), gr. Oovpiiyap = vtxvla (Menander,
vgl. § 135, 2, y), arm. hroUic^ hrort-ic (gen. pi.) ein Monats-
name (?); pron. di = ap. gen. avahya?
c) -wt?a- wird zu D oder i^: durod 'Segenswunsch' neben
paz. drud Min. Gl. 64, Shk. 242 und np. padrud
'Lebewohr, arm.drwo^-iSXobjPreis', ap.*rfwrw-
vatat', zd. drvatat" Gesundheit' (oben p. 61).
xub gut, schon = skr. suvapus-;
hor *Sonne* = zd. hvure d. i. huvare; skr. svar d. i.
sHvar- (oben p. 57).
Liegt uva oder u vor in ap. uvz = huvam- oder huza-'^
Vgl. syr. hUz, arm. Xuzastan, np. xuzistUn 'Susiana'.
Eine Zusammenziehung von -avay zu -m scheint vor-
zuliegen in np. kai 'Konig' = zd. Sicckava^m SLUS*kavayamy
vgl. zd. kavaya- = kavaya- 'koniglich', wahrend der nom.
zd. kava = np. *kav vertreten ist durch das arm. LW. kav
in Kav Xosrov (Sebeos p. 46) = zd. Kava Husrava, np. Kai
Xusrav.
=== leaf 226 ===
— 215 —
xusnud zufrieden' = zd. ^huxs^iiUa- (vgl. huxsnUiii-) oder
xusnUd = x^asnUd = zd. ^x^axsnuta- (siehe oben p. 58);
xUk Schwein' = phi. xUk 61. and Ind. 53 = zd. hu-; xujlr
(neben hujlr, hmlr) 'schSn' = zd. httdid^'a-; xUb *sch5n' =
skr. suvapus' (oben p. 57); xujasta gesegnet, gliicklich' =
zd. ^hujasta-; xurram^) *fr5hlich*, s. oben p. 55.
Ueber xun *Blut' siehe oben p. 58; iiber a?fm oben
p. 59 ; iiber vorgeschlagenes x Kap. 31 ; iiber xu- = a?^a-
§ 108.
Dagegen blieb u in den erwahnten huilVj hujtr sch5n'
und in Humdi (§ 105) sowie in huvaida oflfenbar , hamana
fiir humand (s. oben p. 106), also in Zusammensetzungen
mit hU' = zd. hu- *gut'. Im Paz. liegt x vor in xunar
'skiir Min. Gl. 157, das neben np. hunar und paz. hunar
Shk. 251 verdaehtig ist, xub schSn*, xm Blut', xUram (xuram)
joyfur, xurdak 'klein' = np. xurda^ xusrav well-famed'
Min. 61. 126 — 128, aber h in hubOl^ hucasm, Jmcihar^ hudln
u. s. w. (Min. 61. p. 105 — 108), in alien Kompositis, deren
Zusammensetzung mit hu- gut' noch deutlich gefiihlt wurde.
Im Phi. wird hu- und xu- durch die Schrift nicht unter-
schieden. Im Ap. wird h vor w, v nicht geschrieben^), so
dass hier w, uv sowohl fiir hu =^ skr. su wie fiir x^a- = skr.
sva- steht. Im Armenischen steht h in hnarU *Mittel und
Wege, Ranke' --^ np. hunar; hzaur machtig (aus Viti-zaur),
hlu gehorsam', hmut 'erfahren* (aus *hulu, "^humut), aber x
in Xosrov = paz. Xusrav^ np. Xusrav; Xuzastan 'Susiana
-=^ np. Xuzistdn, syr. Tin, ap. {h)uvza'. Somit ist wohl x
im Phi. anzusetzen in: xusk 'trocken, xvsrav beriihmt',
*) AuohxVnim (oder x^arraw) JRAS. 1894, p. 459; JA8B. 1868,
p. 38.
*) Darayavaus (aber gen. DarayavalMus) ^ uska- , umartiya-^
uvaspa-, uvza- u. s. w., Auramazda^ Harauvatii u. s. w. Seltiier fehlt h
vor andern Vokalen : aistata, &&tiy^ ab
```


## [2026-09-07T20:19:29.068Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"10739\\|10740\" SOD_pages.txt | head; echo \"---- pdf page tags near ----\"; awk '/10739  xwp/{found=NR} {if(found && NR<=found+3) print NR\": \"$0}' SOD_pages.txt | head -8; echo \"=== find page tag before entry ===\"; grep -n \"\\[pdf page\" SOD_pages.txt | awk -F: '$1<83000' | tail -5",
 "description": "Locate SOD entry 10739 page"
}
```


### [2026-09-07T20:19:30.404Z] TOOL RESULT

```
34806:               wysh                                             10739 xwp M, C                        4^«i
34813:          GMS 1100                                              10740 xwptr C                                    >Vj
37790:   10740                                 blind-born    8837                     bowl   1767
38376:GcOget     3483                       (to)go 4083,4174,4531,9340,                9425, 9433, 9456, 10739, 10741
39456:silver coloured    5758                   skilful 4847, 4848, 4850, 10739           socle 9182
---- pdf page tags near ----
=== find page tag before entry ===
```


## [2026-09-07T20:19:40.885Z] TOOL CALL #24: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-07T20:19:40.891Z] TOOL RESULT

```


```


## [2026-09-07T20:19:43.417Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"\\[pdf page\" SOD_pages.txt | head -3; echo ...; awk 'NR>34400 && NR<34900 && /\\[pdf page/' SOD_pages.txt | head; echo \"=== context of 10739 with page tags ===\"; sed -n '34700,34830p' SOD_pages.txt | grep -n \"pdf page\\|10739\\|10730\\|xwp\"",
 "description": "Find SOD page tags"
}
```


### [2026-09-07T20:19:44.647Z] TOOL RESULT

```
...
=== context of 10739 with page tags ===
6:10699 xw'ry*   C =* 'mprt-xw'ry*                             10712 xwpw     S, B                                    .li
58:10710 xwbn C =» xwpn-                                             King, Lord
59:10711 xwpn- M, B                                                  STii 1.2, 7, 2.17, 22; 3.22, 38, 46; GMS 131, 1221;
107:               wysh                                             10739 xwp M, C                        4^«i
108:          GMS 232, 595, 914; BBB 737                                    n>xwp, Ywp
109:                                                                      xQp ©<Av. hvapak Skt. svapas «»mntxwpy,
114:          GMS 1100                                              10740 xwptr C                                    >Vj
118:          GMS 208, 346; C2, 31V2, 12: BSTii 893.12              10741 xwpy(y)    M, C
119:    10730 xwmV w'Py S, C      (IaJ5>;cf^w. jS)*xjuj£Lj                xup(e) ©in compd. =»xwp, mntxwpy
```


## [2026-09-07T20:19:54.752Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^ *1[0-9][0-9] \\|^ *[0-9][0-9] \" SOD.txt | sed -n '1,10p'; echo \"=== search m'n forms ===\"; grep -n \"m'n\\|mʼn\\|mŋn\\|m’n\" SOD.txt | head -20",
 "description": "Look at SOD early entries"
}
```


### [2026-09-07T20:19:54.827Z] TOOL RESULT

```
1674:40 
2523:101 
2585:11 
4106:130  B.c.12  ,  that  a  Chinese  general  -  a  special  envoy 
4475:20  ax>.  The  eight  letters  on  paper  contained  writing 
4545:31       TP  28,  1931,  p.  459. 
5059:79 
5124:82 .  For  details  see  R.  N.  Frye,  HI  AS,  14, 1951,  pp.  108-118. 
5487:161  and  101.  Sims- Williams,  however,  suggests  that 
6332:161  and  101%  gimel  to  render  lYl  and  Ixl  (and 
=== search m'n forms ===
8516:151  "m'n   B  o>*S<j^j 
8889:214  "pm'nwk    M 
9208:260  "s'ym'nSy   B  o>; 
9524:315  "wm'n'k    B  Js^iJ^ 
9525:aw-manc,  omane   ©<*hdmd~mdnaka  ^'wm'n 
9530:316  "vvm'nty'kh  ksJ^^^j^ 
12491:768  'ywm'n  rwc   S     :^j^)j3jj^hJ3J^^^i^  Jjj 
13464:(o)myamande/i   (my'm'nt,  my'mnty) 
13797:'ngm'n 
14150:1006  'ngm'n   C  ^'j**** 
14163:1007  'ngm'ny'  C  ^jA^'j^ 
14164:angmanya   ^'nkm'nCy) 
14373:'nkm'nCy) 
14546:1063  'nkm'nCy)   B,  S 
14547:angaman   ^ngm'ny* 
14649:=^nw>ys-,  m'np'ys-  ? 
16761:1388  'pw  ptzm'n    B 
18026:osman   ©<*asmanam   ©ob.  -y   ^sm'n,  sm'nh 
18037:1588  'sm'n  rwc   S  -Vj^^jjjOU^T^U  ^^jc — ^  j3J 
20129:aw-man,  Oman   ^'wm'n'k
```


## [2026-09-07T20:19:59.728Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '8500,8535p' SOD.txt",
 "description": "Read SOD entry 151"
}
```


### [2026-09-07T20:19:59.774Z] TOOL RESULT

```
akuyde   (*qwytyy)  ©pp. 

suspended 

SCE  392;  GMS  858;  *kwYtu  MDii  "weight"  ? 

148  "qwytyy    M  =^  "kwyty 

149  »kwyc-    B  ^jT 
akwec  ?   ^k'wc- 

(ro)hang,  (ro)suspend 
TSP  3.200,  239  n  pl98 

150  "m'k  =»  >myk 

151  "m'n   B  o>*S<j^j 
aman  ?  ©Av.  a-ma 

power 
.     BSTBL,  Vim.  140;  VJ  n  p92.222;  Bailey.  Prolexis. 
137 

152  »m)r5   B  JUa^>»I^a 
amarO/5  ®<*ham-ar9a\  Pahl.  hamahl 
companion 

GMS  1034;  Hen.  Texts.  726;  pi.  >m}r6ty  TSP 
3.106;  ob.  pi.  >m}rd>yty,  TSP  15.27  n  pl94 

153  "mWn   B,  S  ^l 
amarGan   (^m'rS'yty,  'mrSHi)  ©gen.  pi. 
together 

GMS  1034;  TSP  2.726,  5.87,  9.15  etc.;  Vim.  12ft, 
BSTBL;  SCE  481;  Frag.  Len.  38.25,  81.8;  STii
```


## [2026-09-07T20:20:10.535Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -5 SOD_pages.txt; grep -c $'\\f' SOD_pages.txt; grep -n \"page\" SOD_pages.txt | head -5",
 "description": "Check SOD_pages markers"
}
```


### [2026-09-07T20:20:12.041Z] TOOL RESULT

```
 SOGDIAN
DICTIONARY
Sogdian - Persian - English


642
1946:grammatical identifiers to help differentiate the forms. Adding the references with page
2086:    The English Meaning comprises the next line of           the page and line or paragraph is added. For certain
2986:defective in showing Sogdian vowels in quality and                       The phonemic charts on the following pages give
3221:   See "Remarks" (page xxxv) for the differences in
3267:with an older /z/, by palatalization. Isl also merges               116. On Sogdian vocalic j% see page xxxii.
```


## [2026-09-07T20:20:12.365Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BQT ارشام ===\"; grep -n \"ارشام\\|آرشام\" BQT_v1_pages.txt BQT_v1.txt BQT_alt_v1.txt MON_part1.txt MON_part2.txt 2>/dev/null | head -20",
 "description": "Grep BQT/MON for Arsham"
}
```


### [2026-09-07T20:20:12.430Z] TOOL RESULT

```
=== BQT ارشام ===
BQT_v1_pages.txt:185:نوشته ایست نبنام‌ار بارمنه ۸۲۱۷۵۳۵۱۷۲۱۵ ودیگری نام ارشامه‌و ۳۵9 ۸
BQT_v1_pages.txt:187:نیای دار یوش‌است‌وارشامه پسراوست. داریوش درسنکتيشتة بفستان (بیستون)
BQT_v1_pages.txt:193:باریارمته وارشامه از شهریاران‌فارس بازخو انده‌شود » ایرادی نیست‌جز اینکه
BQT_v1.txt:371:نوشته ایست نبنام‌ار بارمنه ۸۲۱۷۵۳۵۱۷۲۱۵ ودیگری نام ارشامه‌و ۳۵9 ۸ 
BQT_v1.txt:373:نیای دار یوش‌است‌وارشامه پسراوست. داریوش درسنکتيشتة بفستان (بیستون) 
BQT_v1.txt:379:باریارمته وارشامه از شهریاران‌فارس بازخو انده‌شود » ایرادی نیست‌جز اینکه 
BQT_alt_v1.txt:257:نیای دار یوش است‌وارشامه پسراوست. داریوش درسنگنيشتة بفستان (یستون) 
BQT_alt_v1.txt:263:باریارمته وارشامه از شپریاران‌فارس بازخو انده‌شود » ایرادی ثیست‌جزاینکه 
BQT_alt_v1.txt:11847:۵ آرشام - ۸۵1512210 تام جد داربوش بز رکه شاهنشاه هضامنشی, مر کب از 2۳5۳2 
BQT_alt_v1.txt:12032:آریا راهت* _ ۸۳۷2۳2۳00۵ نامجد داربوش بز رکه پدر آرشام» کب از260۷9
```


## [2026-09-07T20:20:19.695Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '11835,11860p' BQT_alt_v1.txt; echo \"=== ARIARAMNE ===\"; sed -n '12028,12040p' BQT_alt_v1.txt",
 "description": "Read BQT alt Arsham entry"
}
```


### [2026-09-07T20:20:19.755Z] TOOL RESULT

```
۸ -معتی اخیر در فرهننگ دساتیی ( رك : می۲۳۰ ) آمده است 


۵ آرذف ‏ پهلوی 2۳261 < 
مراد - ممشوق » محیوب : 


یی ر ۲۸۱ » با 272016 «اونوالا ۲4۵»؛ کام» خواعش» 


۵ آرستی ‏ توانتن » بارستن » جرأت » دلیری کردن . 
۵ آرشام - ۸۵1512210 تام جد داربوش بز رکه شاهنشاه هضامنشی, مر کب از 2۳5۳2 


پبجنی‌خری و 8102 بمعنی زورء جمعاً خری نو » دارای زور خری. «بارتولمه ۲۰۶*. 


]دشی - یکی ات ورایم و سکون 
تحتانی , بمعنی معنوی باشد که در مفابل لفی 
است . چه آرش بمعتی «معئی» است ۷ . 

آدغ - بضم نالث و سکون غين نفطه 
دار » مخفف آروغ است » و آن بادی باشد که 
با صدا از کلو برمیآبد . 

=== ARIARAMNE ===
بخاطر میا ورد و غللی که ثعلق ببخش خاوری هند و اروبائبان بودند . خود را بدین تلم عفتخر 
میدانستند . « دارتالمعارف بربتانیا » امروزه غالبً این کلمه را بنژاد هند و ایرانم, اطلاق‌میکنند 
و شمب‌السنة این اقوام را آربائی گویند . #مزدینا ۲۶ ح» و ره : یستا ۳۵-۳۳ . 

آریا راهت* _ ۸۳۷2۳2۳00۵ نامجد داربوش بز رکه پدر آرشام» کب از260۷9 
آربائی و ۲۵۸۲028 یعنی رامش » جمعاً رامش‌دهنده آربایان «بارتولنه ۰۱44 


یه از صفحهٌ ۳۷ 

دز بشد هش فصل 4 بند ۴ «اروار» آمده . (رژه : باد گار زرران چاپ کابگرس 4 شمارة ۷۷) 
«یناص 2۱۷۹ » خواناری 61۷272 « سالنامة کلپببگان ۷ > حريك از دوقطعه استخوان که 
دنداهای فوفانی وئحتانی « برآن جای دارد - بشما فك « لفت‌نامه» . رد : آره.
```


## [2026-09-07T20:20:30.364Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"\\[pdf page\" BQT_v1_pages.txt | head -3; echo \"=== find arsham ===\"; grep -n \"آرشام\\|رشام\\|آرستی\\|آرذف\" BQT_v1_pages.txt | head",
 "description": "Find page tags in BQT v1"
}
```


### [2026-09-07T20:20:30.422Z] TOOL RESULT

```
=== find arsham ===
185:نوشته ایست نبنام‌ار بارمنه ۸۲۱۷۵۳۵۱۷۲۱۵ ودیگری نام ارشامه‌و ۳۵9 ۸
187:نیای دار یوش‌است‌وارشامه پسراوست. داریوش درسنکتيشتة بفستان (بیستون)
193:باریارمته وارشامه از شهریاران‌فارس بازخو انده‌شود » ایرادی نیست‌جز اینکه
```


## [2026-09-07T20:20:36.806Z] TOOL CALL #32: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/ 2>/dev/null; ls /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT 2>/dev/null | head -30",
 "description": "Check OCR cache"
}
```


### [2026-09-07T20:20:36.843Z] TOOL RESULT

```
AFM
ARY
BOOK
BQT
FFD
HRN
IRN
PLA
SNS
SOD
TAD
0001.png
0001.txt
0049.png
0049.txt
103.vision.txt
1092.jpg
1092.vision.txt
1187.png
1187.vision.txt
1219.png
1219.txt
1219.vision.txt
1223.png
1223.txt
1225.png
1225.txt
1225.vision.txt
1226.png
1226.txt
1237.png
1237.txt
1237.vision.txt
1261.png
1261.txt
1266.png
1266.txt
1266.vision.txt
1267.png
1267.txt
1267.vision.txt
```


## [2026-09-07T20:20:40.688Z] TOOL CALL #33: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT | grep -E \"^(2[0-9]|3[0-9])\\.\" ; echo \"---\"; ls /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/SOD",
 "description": "Check cached BQT pages 20-39 and SOD"
}
```


### [2026-09-07T20:20:40.734Z] TOOL RESULT

```
31.vision.txt
---
70.vision.txt
```


## [2026-09-07T20:20:44.207Z] TOOL CALL #34: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/31.vision.txt",
 "description": "Read cached BQT page 31 vision text"
}
```


### [2026-09-07T20:20:44.251Z] TOOL RESULT

```
[BQT vol.1, printed p. 31 (archive.org borhan-ghate-v1 leaf n241), read from the page image
by claude-fable-5-1 on 2026-09-04. Running head: آرش   - ۳۱ -]

Right column, top (continuation of the entry آرد, whose headword is at the foot of p. 30):
«... مخفف آورداد است که نام روز بیست و پنجم از هر ماه شمسی باشد ۱ ــ و بسکون ثالث معروف است
که غلهٔ آسیا کرده باشد ۲ ــ و بمعنی تقصیر هم آمده است .»

آردتوله ــ (۱) بضم فوقانی و سکون واو و فتح لام ، آشی باشد مانند کاچی که از آرد پزند و بیشتر
مردم درویش و فقیر خورند و آنرا بعربی «سخینه» گویند .
آرددوله ــ با دال ابجد ، بر وزن و معنی آرد توله است که آش کاچی مانند باشد .
آردم ــ بفتح رابع و سکون میم ، نام گل آذریون است که نوعی از شقایق و گل همیشه بهار باشد .
آردن ــ بفتح رابع و سکون نون ، ترشی بالا را گویند و آن ظرفی است که مانند کفگیر سوراخها دارد
و بدان چیزها صاف کنند و کفگیر را نیز گویند ــ و نام ولایتی هم هست .
آردهاله ــ بهای (۲) بالف کشیده و فتح لام ، بمعنی آرد توله است که آش کاچی مانند باشد.

Footnotes (Mo'in's etymological notes) at the foot of the page:
۱ ــ صحیح «ارد» بفتح اول است . رك : ارد .
۲ ــ پهلوی ârt «تاوادیا ۱۵۹ ، بونکر ۱۱۲» .
۳ ــ و مخفف آوردن .
۴ ــ رك : آرستن .
۵ ــ اوستا ərəxsha (درخشنده) «یوستی ۸۹» . وجه اشتقاق آن نامعلوم است «بارتولمه ۳۴۹» .
[…]
۵ آرزو ــ پهلوی ârzôk «نیبرگ ۲۸۱» یا ârzûk «اونوالا ۲۹۵»؛ کام، خواهش، مراد ــ معشوق، محبوب .
۵ آرستن ــ توانستن، یارستن، جرأت، دلیری کردن .
۵ آرشام ــ Arshâm نام جد داریوش بزرگ شاهنشاه هخامنشی، مرکب از arsha بمعنی خرس و ama
بمعنی زور، جمعاً خرس نیرو، دارای زور خرس. «بارتولمه ۲۰۴».

[Key point for verification: Mo'in's only etymological note on آرد "flour" is «پهلوی ârt»
(Pahlavi ārt), citing Tavadia p.159 and Bunker p.112. No Avestan or Indo-European form is
given on this page for آرد.]
```


## [2026-09-07T20:20:56.659Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SYN.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(\"n\",len(pages))\nimport re\n# find pages mentioning 'ama-' Avestan strength\nfor i,p in enumerate(pages,1):\n    if 'STRONG' in p.upper()[:400] and ('Av. ama' in p or 'amavant' in p):\n        print(\"=== leaf\",i,\"===\"); print(p[:1500])\nEOF\ngrep -n \"amavant\\|Av. ama\\|ama-\" SYN.txt | head -20",
 "description": "Grep Buck SYN for Avestan ama"
}
```


### [2026-09-07T20:20:58.294Z] TOOL RESULT

```
n 1545
=== leaf 338 ===
etym. dub., perh. : ON hr@fa ‘tolerate, bear’, W. craff ‘fast, secure’ (W. cryf ‘strong’? cf. above, 3). Walde-P. 1.487. Berneker 614.
SCr. jak = ChSl. jakt ‘qualis’ (Pol. jaki, Boh. jaky ‘what sort of’, etc.). Semantic development like Rum. tare fr. Lat. talis (above, 2). Leskien, Serbo- kroat. Gram. 406.
SCr. snaZan fr. snaga ‘strength’ : ChSl. snaga ‘work, zeal’, Boh. snaha ‘effort’, etc., outside connections? Mik- losich 312.
ChSl. silint, Boh. silny, Pol. silny, Russ. sil’/nyj, fr. the sbs. for ‘strength’, ChSI. sila, ete. : OPruss. seilin ‘industry, zeal’, ON seilask ‘seek for, stretch out the hand’, further root connections dub. Walde-P. 2.460 f. Briickner 490 f.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
298
Boh. mocny, Pol. mocny, Russ. most- nyj, fr. sbs. for ‘might’, Boh. moc, etc. = ChSI. mogti, fr. vbs. for ‘be able’ ChSI. mosti, mogq, ete. : Goth. magan ‘be able’, etc. (above, 4). Walde-P. 2.227.
Berneker 2.67 f., 70.
7. Skt. balin-, fr. bala- ‘strength’ : ChSl. boljiji ‘larger’, bolje ‘more’, Lat. dé-bilis ‘weak’, Grk. BeAtiwy ‘better’, ete. Walde-H. 1.327. Walde-P. 2.119 f. Berneker 72.
Skt. ¢ura-, Av. stira-, also Skt. cavas ‘strength’: Grk. axvpos ‘without au- thority’, x®pios ‘lord, ruler’, prob. fr.
SELECTED INDO-EUROPEAN SYNONYMS
the root *keu- ‘swell’ in Skt. cvayate, ete Walde-P. 1.365 f. :
Skt. ojasvant-, Av. aojah-, aojahvant- fr. Skt. ojas-, Av. aojah- ‘strength’ : Skt. vaks-, 
879:It. fango Sw. gyttja, dy, mudder SCr. _blato Fr. boue (fange) (smuts) Boh. _ bldto Sp. lodo, fango, barro, OE fen Pol. bloto cieno ME mudde, fen Russ. grjaz’ Rum. noroiu NE mud Skt. parika-, kardama- Ir. lathach Du. modder, slijk Av. osc Nir. __laitheach, draoib OHG §leimo W. Waid, mwd MHG quat, kat Br. Sank NHG = schlamm, kot, dreck
932:Skt. kardama-, etym. dub. Walde-P-
1025:NIr.  magh OHG  ebandti, feld Skt.  sama-, ajra-
1063:7. Skt. sama-, neut. sb. of adj. sama- ‘equal’ (12.91) also ‘even, level’. Also (rarely) | sama-bhiimi-, sama-sthali-, epds. with words for ‘earth, ground’ or ‘place’.
5140:3.84 WORM Gtk. oxdiAné Goth. mapa (waurms) Lith. kirmele a oKoUNARL ON ormr, madkr Lett. tarps ; 3 «vermis Dan. orm ChSl. ériivt th me Sw. mask SCr. crv Sp ead OE wyrm, wurm Boh.  éerv Rum, yf ae ME ~~ werm, wurm Pol. robak TK neg NE worm Russ. éerv’ Nir. Beat: 2 Du. worm Skt.  krmi- We bin i, » Chutmh OHG wurm Ay. (karama-), NPers. Br. tle Nee wurm _ kirm
5155:Skt. krmi-, NPers. kirm (here prob. Av. karama- used with star- of a shooting star); Ir. cruim, NIr. cruimh, cnuimh, W. pruf, Br. prenv; OLith. kirmis, now kirmélé (Lett. cerms ‘maw-worm’); here also, with different suffix, ChSl. éivt, SCr. crv, Boh. derv, Pol. czerw (mostly ‘grub, maggot’), Russ. éerv’.
6113:Lat. armus mostly ‘shoulder, fore- quarter’ of animals, rarely ‘arm’ of men; Goth. arms, etc., general Gmc.; OPruss. armo ‘arm’; ChSl. ramo, rame, SCr. rame ‘shoulder’, Boh. rdmé, rameno, mostly ‘arm’, Pol. ramie, ‘shoulder, arm’; Skt. trma- ‘forequarter’ of an animal; Av. arama- in aramd-Sita- ‘thrown by the arm’; Arm. armuka ‘elbow’.
6804:Grk.  rriw Goth. speiwan Lith. spiauti NG ss griw ON hrekja, spyta Lett. spl/aut Lat. spuere Dan. spyite ChSl.  pljtvati It. spulare Sw. spotta SCr.  pljuvati Fr. cracher OE sp@lan, hr@can, spyt- Boh. _ plivati Sp. escupir tan Pol. plué Rum.  scuipa ME spete, spite (reche) Russ. plevat’ Tr. saile (sb.) NE spit Skt. sthiv- NIr.  sailighim Du. spuwen Av. spama- (sb.) W. poert OHG = spiwan
7574:I Tite teal NE strong, powerful, Russ.  sil’nyj, mo3tnyj ie fort ‘puissant mighty Skt. balin-, ¢iira-, ojas- Sp. fuerte, potente Du. sterk, machtig, krach- vant- Tim! tare, pulernic tig . _ Av. stra-, aojahvant-, Ir. irén, laidir, adbol OHG - strengi stark, mahig, amavant- Nir. trean, laidir, nearth- kreftig, giwaltig:
7652:Av. amavant-, fr. ama- ‘strength, power’ : Skt. ama- ‘onset’, am- ‘press on, injure’, ON ama ‘vex, annoy,’ eto, Walde-P. 1.178. Barth. 141.
8131:4.94 LAME Grk. _ xwAds Goth. halts Lith. raiSas, Slubas NG xourcés ON halir (lami) Lett. _tizls, klibs, slums Lat.  claudus Dan. halt, lam ChSl. chromit It. zoppo, ranco Sw. halt, lam SCr. — hrom, Sepav Fy. botteur OE healt (lama) Boh. chromy, kulhavy yy Sp. cojo ME shalt, lame Pol. chromy, kulawy Rum.  schiop NE lame (halt) Russ. chromoj Ir. bacach, losc Du. kreupel, lam, mank Skt. grona-, srama-, pai- NIr. — bacach OHG _halz (lam) gu-, ete. W. cloff MHG lam, halz, hinlende Av. By hhe Br. kamm NHG  lahm, hinkend
8172:6. ChSI. chrom, etc., general Slavic : Skt. (Ved.) srama- ‘crippled, lame’, root connection? Walde-P. 2.706. Berneker 403.
11519:. 712 HOUSE 0 ar aaa iis Goth. gards, razn Lith. nama, butas domus ON his, rann Lett. maja, nams Dan. hus ChSl. domi, chrami, chyzt maison Sw. hus SCr.  kuéa, dom OE his, ern Boh. dtim ME hus, hous Pol. dom ae ose Russ. dom ne Wuse Skt.  grha-, dama- ven is Av. nmana- NHG haus
11527:ChSI. domi, etc., general Slavic; Skt. dama- (Vedic), Av. damana-, nmana-.
11547:Skt, dama- Skt. cala- filam ‘at; ho
12033:5. Skt. dhiimanirgama- (rare and *
12034:Russ. dymovaja truba ‘smoke-pipe’ or pyadenee of ee actual chimney) lit, R commonly iruba ‘pipe, trumpet’ used smoke-outlet’, epd. of dhiima- ‘smoke? ie alone for ‘chimney’ : ChSl. traba ‘pipe, | and nirgama- ‘outgoing’. N T 7.41 FURNITURE dl Grk. mda Goth. Lith. baldai, rakandai se NG éxtrda ON _hiisbiinadr, -biiningr Lett. istabas lietas, mebele Io Lat. _supellex Dan. mébler, husgeraad Chsk 2.52 It. mobili, supellettile Sw. mobler, husgerdd SCr. — namjeStaj, pokuésivo Fr. meubles OE idisc, inorf Boh.  nabytek h Sp. muebles ME _(houshold, mobles) Pol. mebel, sprzet Rum. mobile NE furniture Russ. mebel’, obstanovka Ir. intreb, fointreb Du. _—meubelen, huisraad Skt. (upakaranani) pr NIr. _ troscan OHG § (giziugalz, gizawi) Av. ee be W. dodrefn MHG hisrdt, hisgerate Br. annez, arrebeuri NHG miédbel, hausgérat er ‘Furniture’ is understood here in the | plurals of It. mobile, Fr. meuble, ete, pl now prevailing sense of NE furniture ‘piece of furniture’, fr. Lat. mobile i (NED s.v., 7), that is as ‘house furni- ‘movable’ (cf. mébilia ‘movable goods, ty ture’. Some of the words are connected chattels’), deriv. of movére ‘move’. mi with those for ‘house, dwelling’. But 3. Ir. intreb, fointreb, (NIr. intreabh fr the majority had originally, and some ‘property, wealth), epds. of ind- in’, fo- N still have, a wider Scope, covering all | ‘under’, and treb ‘dwelling’ (7.11). sorts of movable property, equipment, NIr. troscan ‘implements, baggage, su utensils, etc. clothes’ (Gael. trusgan ‘clothes’) and (N The words are partly plural, partly | ‘furniture’ (or more specifically troscan le Singular forms used collectively. lighe ‘furniture of the house’), loan- 1 1. Grk. émmda (also ‘utensils, fittings’, | word fr. ME trusse ‘bundle, baggage’, Gi but usually not so general as oxebn) : | with added suffix. Macbain 378. 12 erurohi surface’, érurédatos ‘on the sur- W. dodrefn, MW deodreven, cpd. of dy- th face (cf. Cret. tmmédara xphuare = tm- | ‘to’ (often intensive), go ‘sub’, and trefn fu wage émméhouat ‘come upon’, ete., IE ‘arrangement, order, system’. Keel-. Walde-P. 1.514 f. Br. annez fr. MBr. anhez ‘dwelling’, 90
13687:Skt. ¢grama- ‘fatigue, toil’ (with vb
14908:1. Grk. olxodopéw ‘build’ in general, deriv. of olxodéuos ‘builder’, or a like epd. (cf. also olxodoula ‘act of building, a building’) of ofxos ‘house, dwelling’, and the root of déuw ‘construct, build’ (not a common prose word), dédpos ‘house’ : ON timbr ‘wood for building’ (cf. below, 4), Skt. dama-, Lat. domus, etc. ‘house’, IE *dem- ‘build’, perh. ong. ‘Join, fit together’, as in Goth. gatiman, OHG zeman ‘be fitting, becoming. Walde-P. 1.786 f.
15627:GLASS Lith.  stiklas Lett.  stikls, glaze ChSl.  sitklo SCr. _ staklo Boh. _ sklo Pol. szklo Russ. _ steklo Skt.  kdca- Av. yama-
```


## [2026-09-07T20:20:59.016Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== IEC ==\"; grep -n \"omə\\|omo-\\|amā\\|Av. ama\" IEC.txt | head -20; echo \"== WLD band3 178 ==\"; grep -n \"amavant\\|amayava\" WLD_band3.txt incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt 2>/dev/null | head",
 "description": "Grep Mann and Walde-Pokorny"
}
```


### [2026-09-07T20:20:59.090Z] TOOL RESULT

```
== IEC ==
485:amāið (ammaio), denom. ‘mother, foster". WP I, 53 Lat. amo, -àre; MHG ammen ‘act as midwife’; Sw. amma 'suckle'
632:apomos “last, furthest'. Cf. apo. WP I, 49 Skt. apamáh, apama; Av. apomo; Hitt. cf. appan “after, warde": OAIb. i pér-apém “last? (*pro-apomo-)
816:auks- (auksomo-) “high; height, growth?. Cf. auk- (2) Gk. cf. aükse, aüksimos; Lat. cf. auxilium; beside Auximum (a town in S. Italy: Osimo) beside Uxama (a town in Spain: Borgo de Osma); Ir. cf. uachtar ‘top’; W uchaf ‘highest’, beside OW uch, W uwch (‘higher’. Phonology obscure, but not as JMJ § 148 (14))
1590:bhraĝtos, bhraktos (variant: bhragst-) (1). See bhrag- Lat. fractus; Mir bracht ‘breaking, reaping’; W brath “stab, bite, sting; MHG braht, breht ‘uproar’; Icel. brattur, Norw. bratt, adj. ‘steep’; OS cf. brahtom, OE breahtm ('din', fr. *bhragtomo-)
2206:desmos, à, desmn- “holder, fastener, tie, join, link'. Cf. WP I, 771 & 802 Skt. dasmáh ‘spellbinding’, Arm. (?) ávan, čvanea “string, rope’; Myc. desomo- (desmo-); Gk. desmós ‘latch, fetter; désma, id. cf. désme ‘bundle; MHG zésem, zësen “line, row, series’; ON tjasna, f. ‘peg
2386:domos, üs ‘building, house’. Cf. demo, dómn- (1) Skt. dámah, am Arm. tun, gs tan (fr. *domn-); Myc. domo-; Gk. dómos, beside domé “building, wall’; én-don “at home"; Lat. domus; Mir dom; W cf. dof ‘tame’; OHG zam; OE tam; ON tamr ‘tame’, cf. OE tama ‘tameness’; OCS domü, u-st.
3785:omo- (?) in Skt. ami ‘these’ and Ober ima “this”
6269:īsos, à “low, base, short Lat. cf. mus (lowest, fr. *isomo-); Osc. cf. ima-den "Dom below" Li. ysas, isas, jsas ‘short’; Latv. Iss, id. Of ambig. origin are MIr. isel, Ir. íseal ‘fow’, Gael. íos ‘down’; Olr. ís ‘below’; W isaf “lowest? from a type Test. or *pēds- (cf. Lat. pessimus: W isaf?
6484:ioməlos ‘holding; hold, link, junction’. See next and cf. iem-, em- Skt. (ambig.) yamalah, adj. ‘pairing, double’, m. ‘twin’; Li. jamlùs ‘capacious, receptive’. Cf. OE gilm (‘handful’, metath. for *iemol-?)
7009:kent- (2) f'endmost; before, after’. (Super- lative: kentomo-) Olr. cét-, cpds. ‘chief; Ir. céad "first, cf. céadamh *May day, the first of May': W cyn- taf ‘first’: Go. hinduma, OE hindema *'hind- most, last’; Gaul. cintu-, cpds. ‘first: MW E W cynt ('earlier'; adj. “first'); Br. kent "before": Cor. kens, kyns, kenj (kendZ) ‘former’; Bur- gundian (in Lat. context) cf. hindemos ‘chief: Go. hinduma, OE hindema *last', but W cyn- taf, Ir. céadamh (see above); MHG cf. hinder *back, behind' beside G hinten, id. (fr. *ken- tomo-)
7598:komos, us Jump, hump’. Cf. kombos, komo- los. WP I, 388 & 460 Icel. hom, gs hamar “ham, haunch'; R kom Jump’; Srb. kom ‘mash, lees’; Slovene kom “hill, peak’; Latv. kams “lump”, kama ‘clod, pease-pudding’
7605:koməros — konsos
7834:krekō, ið ‘creak, screech, grind, grate’. Cf. WP I, 463, 483 & 486 and next Skt. cf. krákşamānah, adj. ‘roaring, raging’; Gk. krëko ‘creak’; Lat. cf. crex, gs crecis “daker- hen’; MIr. crech ‘raid, foray’; W cregu ‘grow hoarse’; crec, m. ‘chirrup’; Cz. křečet, inf.
7984:krokið ‘caw, croak, squawk?. Cf. krek-, etc. Lat. crocio, ire, id.; Vedic cf. krákşamānah ‘roaring’; Big. cf. kròkon ‘raven’. Variant in W
10297:mămā (mammā) ‘mother, grandma, female, nurse’. (Onomat.) WP II, 221 Skt. māmā ‘woman friend beside måmah, m. (!) ‘bosom friend’; Per. māmā ‘mother, old woman'; Arm. mam ‘grandma’; Gk. mámma ‘breast; mother, grandma! beside mémē ‘grandma’; Lat. mamma, f. as Gk., beside mā- milla, f. “breast; Alb. mâmë, mëmë ‘mother’; Ir. mam ‘mother’; mám, f. ‘breast’; maime, beside Ir. Olr. muime (*mother, nurse', fr. *mámio); Br. mamm, OBr. -mam “mother? beside Br. mammu, f. ‘womb’; W mam, as Br; Cor. mam, pl. mammow, as Br. OHG muoma, MHG muome, wf. “maternal aunt (G Muhme, id.) beside SGer. Mahm ‘aunt; Lux. Frankish mam ‘mother’; Srb. & OCS moma (girl, fr. mamā) beside mama ‘mother’; Li. mamà, id.
12139:om- (4) (omotos, ios, omost-) ‘dead, dull, oppressive’. Cf. om- (2) Arm. amaji, adj. ((deserted, desert’, fr. *omo- tio-); s. desert; Alb. i åmtë, i àmshté, adj. *sultry; insipid; peevish; slothful; stupid"; Icel. cf. amstur, n. ‘annoyance’. Same as type (2) (?). Arm. h-amr “slow, sluggish’; b-amem, v. ‘loiter is ambig. (either from *en-omus, *en- om- or from a type iom-, q.v.)
12145:-omeno- (theme of middle-voice participle adjective or noun) Skt. vart-amānah, adj. (turning, etc.); Av. vərəz-imnəm, pl. -imna ‘deeds; Arm. ar-
13143:plid- (1) (flat, smooth? W llydd, f: Hedd, adj. (1) “flat? beside lleddf, id. (and ‘gently sloping’, fr. *plidomo-); Fris. cf. flit, n. ‘flat-bottomed boat; Du. vlet, id.; Latv. plidens, adj. ‘slippery’
13495:proeim- (form of proiomo-, priiomo- 'fore- most") OW rwyf, m. ‘ruler, leader’; Ir. riam, adv. "pre: viously’; Slovene prema, prp. ‘against’
13560:prom-, prom-, próm- (promi-) “forth, for- ward, on, forthcoming, first, beyond?” Cf. pro- and cpds. WP II, 37 Skt. prama, f. “basis, scale’; cf. param, adv. ‘afterwards; beyond; very, greatly’; Tokh. cf. parán, s. (‘dignity’, but see Supt: pro-án-); Arm. (?) orm, o-st. (^walP, but perh. fr. *por- mo-, cf. Cz. prám, R poróm, m. “ferry'); Gk. prómos, adj. ‘foremost; m. ‘leader’; Osc. pru- mu, Umb. promo- ‘first’; (for Lat. *pro- in prðmens, gs. -ntis ‘expanding’ cf. emo); Mir. rom, adj. ‘early’; Ir. roimh, roimhe, prp. Cbe- fore’, from a type *promi-); OE fram, adj. “ac- tive, virile; adv. ‘forth’; freme, adj. (“vigor- ous’, fr. *promio-); fremu, f. ‘profit’; ON Tram, adj. “forward, prominent'; fram, adv. “for- ward”; cf. framan, adv. “at the front"; fremi, prp. ‘before’; Sw. fram, adv. ‘forward’; Slovene (*-0-) pram, prama, prp. ‘against’; Cz. pramen, m. ‘source’. Cf. also Srb. pru-diti, Alb. LW pronditë, v. “benefit; produce’; Srb. prama- ljece ‘springtime’
== WLD band3 178 ==
```


## [2026-09-07T20:21:11.851Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SYN.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\ntarget=[i for i,l in enumerate(lines) if \"Av. amavant-, fr. ama-\" in l]\nprint(target)\n# find nearest preceding standalone page number\nimport re\nfor ti in target:\n    for j in range(ti,max(0,ti-200),-1):\n        m=re.match(r'^\\s*(\\d{2,4})\\s*$',lines[j])\n        if m: print(\"preceding page marker:\",m.group(1),\"at line\",j); break\n    for j in range(ti,min(len(lines),ti+200)):\n        m=re.match(r'^\\s*(\\d{2,4})\\s*$',lines[j])\n        if m: print(\"following page marker:\",m.group(1),\"at line\",j); break\n    print(lines[ti-3:ti+3])\nEOF",
 "description": "Locate SYN page for amavant"
}
```


## [2026-09-07T20:21:12.556Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"om- (1)\\|om- (2)\\|om- (3)\\|opos\\|opes-\\|opus\" IEC.txt | head -20",
 "description": "Grep Mann IEC for om- and opos"
}
```


### [2026-09-07T20:21:13.151Z] TOOL RESULT

```
[7651]
preceding page marker: 298 at line 7643
following page marker: 304 at line 7782
['SELECTED INDO-EUROPEAN SYNONYMS', 'the root *keu- ‘swell’ in Skt. cvayate, ete Walde-P. 1.365 f. :', 'Skt. ojasvant-, Av. aojah-, aojahvant- fr. Skt. ojas-, Av. aojah- ‘strength’ : Skt. vaks-, uks-, Av. vars-, uag- ‘stow make grow’, Goth. wahsjan ‘grow’, Lat, augére ‘increase’, ete. Walde-P. 199. f,', 'Av. amavant-, fr. ama- ‘strength, power’ : Skt. ama- ‘onset’, am- ‘press on, injure’, ON ama ‘vex, annoy,’ eto, Walde-P. 1.178. Barth. 141.', 'Av. zavah-, zavar- ‘strength, power’ (NPers. z6r > Turk. zor > NG tpt ‘force, violence’) : Skt. javas- ‘speed’, ju- ‘be swift’, etc. Walde-P. 1.555. Barth. 1690.', '4.82 WEAK Grk. doferis, &ppworos Goth. lasiws Lith. silpnas NG = ddbvaros ON veikr Lett. vdj8, nestiprs Lat.  débilis, invalidus, in- Dan.  svag ChSl.  slabi jirmus Sw. svag SCr. slab It. debole OE wae Boh. — slaby Fr. faible ME woke, waike Pol. slaby Sp. débil NE weak Russ.  slabyj Rum. slab Du. zwak Skt. durbala-, nirbala-, Ir. lobur, lacc, fand OHG  weich, kitmig abala- Nir. lag, fann MHG  weich, swach, kume Av. asiira- W. gwan NHG | schwach Br. gwan ‘Weak’ as the opposite of ‘strong’ is | ‘strength’ (4.81). Ernout-M. 255.']
```


### [2026-09-07T20:21:13.192Z] TOOL RESULT

```
644:spect’; Li. cf. opus ('sensitive', see apos below)
2881:dhom- (1) (dhm-, dhm-) (theme of a radical “blow, puff, swell. See dhum-). WP I, 851 Skt. dhámami, pp. dhmatah “blów?; Av. dam- ‘blow, breathe’; Per damam, "dan ‘blow’ beside dam ‘breath’, dame ‘bellows; asthma’; Oss. dimin, dumun ‘blow, smoke’; Hitt. dann- aras, -attas ‘empty’; Gk. cf. ásthma (fr. *n-Ks- . dhmn, cf. n-px. and eks); Lat. cf. fam-ex, mf. ‘tumour’ beside fam-faluca ‘pustule’; OHG cf. a-tum ‘breath’; Ger. Atem; OCS dümgo, doti ‘blow’; dümljo, dommt ‘inflate’; Cz. dma ‘throes’; roze-dma ‘emphysema’; Li. dumiü, dümti “blow, get cloudy
2882:dhom- (2) (dham-, dhóm-) (theme of a rad- ical “set, fixed’. See dhê- (2), etc.) Gk. thamüs fcompact', thamá, adv.; thámnos ‘thicket’; thaminós, adj. “close, frequent’; cf. also Hes. thaimós “family, household’; Lat. fam-ul, -ulus, -ilia; W daf, pl.-oedd “issue, output; MHG tam, gs. tammes; Du. dam ‘dam’; Go. faür-dammjan (‘dam up’. -mm- unexplained, cf. Li. domüs, j-domus “atten- tive; interesting; dome “attention? *-a- and Gk. thomós ‘pile’ *-o-)
4341:grom- (1) ‘pile, mass, chattels’ Skt. gramah ‘pile’; G (uncertain vocalism) cf. Kram (“chattels?, but MHG kram “tent, shop, goods’ of uncertain origin); OCS cf. gromada ‘pile’, grominica ‘shop’
4342:grom- (2) ‘waste, rubbish, triviality, decline’ ON krọm, gs kramar ‘wasting disease’; G cf. kramen ‘potter about; Kram ‘fuss’ (vocalism uncertain); Li. gramùs ‘finicky’; Latv. cf. gramstu-, -stīt (2) ‘twaddle’; gramšķis ‘twad- der: rubbish?
4343:grom- (3) ‘cough, cough up; sputum’ Norw. cf. kremt ‘hawking cough’; kremte ‘clear the throat’; Li. gramai ‘sputum’
7281:bustle’; kloposto, klopotati, v. id.; Ukr. Pol. klopotaty, kłopotać, tr. v. ‘bother’
7587:kolsos, om (1) ‘neck’ Gk. cf. kóll-ops, gs -opos ‘neck-skin of ani- mals’; Lat. collus, collum; Go. OHG hals; OE heals, id.; ON cf. helsi (“dog-collar”, fr. *kolsiom)
7625:kop- (kopó, ið) “hit: dig. WP II, 559. Cf. kopos (1) Gk. kópto 'hit^; Oss. cf. cäf blow’, fr. *kep-); cávín “hit”; Alb. kep ‘chip, carve’; OE cf. hafe- tian ‘clap’; (*-0- in) ON hoefa ‘hit’; OCS (and com. Sl.) kopng, -noti, kopajo, ati ‘dig’; -kopü ‘digging’; Li. kapoju, oti ‘hack’; cf. kaplys, m. ‘chopper’; Latv kapaju “chop, mince’; kaplis, s. as Li. (E hoof, G fr. LG Huf, and Du. hoef represent a form *kop-, for the sense cf. SI. kopyto "boot
7627:kopis, see kopos (1)
7631:kopos (kopis) (1) ‘blow, cut, stab, dig’. Cf. WP II, 559-561. Gk. kópos “blow; toil’; kopë “cutting, breaking, pounding’; kopís ‘dagger’; Cz. cf. vý-kop “ex- cavation'; Srb. -kop, in cpds.; OCS, Cz. (and
7642:kopos, å (2) ‘heap’. Cf. WP I, 344 & 373 and next. Cf. kop- Alb. (ambig.) kapë (in place-names: ‘peak’. Cf. koup-); R kopà, Pol. kopa ‘heap’; cf. also Pol. kopny, adj. “snowed-under?
7643:kopos, à “mass, lump’. Variant of kopos (2). Cf. kópios Gk. kópé “hilt'; ON hóf ‘feast’; Eng. hoove ‘flatulence in animals"; OCS cf. kapija Cheap’: Lat. copia ‘plenty’), Li. kúopa ‘mass; crowd’; Latv. kopa, id.
10058:lop- (lopos, a) *peel, scale, plate, flat piece, flap, scoop, shovel'. (Variants in Gk. and SI.). Cf. WP I, 10 & II, 428-430 and lepos (2) : Gk. lópos, lopós, m. ‘peel, bark, rind’; lopis, f. *fish-scale, pan’; lopás, gs -ádos ('platter, pan’. LW in Lat. lopada; Alb. lapé, f. (2) leaf; Nor. Sw. (?) lav, m. ‘lichen’; OE cf. Leier f. “metal plate’; OCS cf. lopata (tshovel'. Fr. Dal- matian-Lat. via Etrusc. fr. Gk?); Slovak cf. lop-ár, m. ‘wooden platter, trencher'; Li. lápas ‘leaf; Latv. lapa, f. id. (Alb. lopatë ‘shovel’ is fr. Sl.). OE læfer is ambig. < *laporos? A long- gde form appears in Gk. lópos, lópë “garment, skin”
12125:om- (2) *pain, sorrow, hardship Skt. cf. amatah ���disease’; amatib, f. ‘poverty’; adj. ‘poor; amiva, f. ‘suffering’; amin, adj. ‘sick’; cf. also áme, mp. ‘oppress’; Gk. (Hom.) omoiíos (fdire, horrible, epithet of old age, war, death: Skt. amivam, A 'suffering)); Av. cf. amayavo (worthless. Queried here by
12136:om- (3) ‘strength, power, ability, skill. (Cf. em- m- ‘take, hold”, etc.) Skt. ámah ‘strength’; Av. amo, m. id. (and
12139:om- (4) (omotos, ios, omost-) ‘dead, dull, oppressive’. Cf. om- (2) Arm. amaji, adj. ((deserted, desert’, fr. *omo- tio-); s. desert; Alb. i åmtë, i àmshté, adj. *sultry; insipid; peevish; slothful; stupid"; Icel. cf. amstur, n. ‘annoyance’. Same as type (2) (?). Arm. h-amr “slow, sluggish’; b-amem, v. ‘loiter is ambig. (either from *en-omus, *en- om- or from a type iom-, q.v.)
12211:op- (3) (same as (2)?) “activity, work. WP I, 175. Extn: opnos. Cf. oplos Skt. ápas, n. ‘work’; apás, adj. “active”, cf. also ápnas, n. (2) "work: Av. (?) apo, n. ‘wish’; Hitt. cf. appas ‘workman’ beside happar, gs: happaras “business, transaction”: Illyr. names Aplos, Oplos, a, mf. (See op- (2) but prob. here); It-Alb. ápull (*soft, tender? here?); Lat. Opus, gs: -eris, n. ‘work, business, deed, use"; opus, indecl. (necessary: Skt. apás); cf. also Opés, gp: opum (2) ‘power’; OE eafor, m. & n. “obligations, supplies, auxiliary force; (fr. *opeso: Lat. opera); aferian, v. “bring up rein- forcements'. Other variants: Skt. ápnas (see above) also in Hind. apna, adj. "own: OE zefnan, v. “perform, execute’; ON efna, v. id.; efni, n. ‘substance’; Norw. evne, v. “be able’; evne, s. ��ability’. Cf. further Umb. opeter, adj. "of the best; MHG (*-o-) üeben, v. (act. See õp- below); uober, adj. “active
12229:opos, see op- (2) and (3)
13665:prKsKo “ask, beg, beseech’. Cf. prKs- (1) and preK-, perK-. Variant prKsn- Skt. préchámi, v. id.; Av. porosa, lsg. id.; Per. pursam, -idan, id.; Oss. fársin, inf. id.; Tokh. B. park-, v. id.; Arm. cf. harcnem, harcanem, id.; Lat. posco, ére, pf: poposci, id.; Umb. cf. pe-purkurent (‘they shall ask’. Umb. pers- nimu, depon. imperative is prob. ‘put, not ‘pray!’); W erchi, inf. (“ask”, fr. *porKsK-); Cor. erghy, yrghy, v. ‘command’; MHG vorschen, v. “ask, seek’; Li. cf. pirsti, inf. of persü, v. ‘mediate; woo’
```


## [2026-09-07T20:21:25.894Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '12200,12235p' IEC.txt",
 "description": "Read Mann op- entries"
}
```


### [2026-09-07T20:21:25.942Z] TOOL RESULT

```
35
40
45
880
ontos (antos?) (1) “outside; field, plain, open land”. (Vowel ambig.) Skt. ántah (2) ‘outskirts’; Oss. ändä, adv. "out. side’; Tokh. ant, ante, s. "plan": Arm. and, ost & i-st. “land, field, soil
ontos (2) “lovely; beauty, charm, grace’. Cf. ondh-. (Alb. ambig.) Skt. ántah, adj. ‘lovely’; Alb. (ambig.) ândë, f. ‘desire’. Variant in Go. ansts, i-st. f. (joy, thanks, grace, favour”. But cf. on- above); OE est, mf. id. (also: *pleasure, harmony, love"); este, adj. ‘gracious’; ON ást, f. as Go. OE
onughos, onguhos, noguhos, à, om, is “nail, claw, hoof. WP I, 180 Skt. nakhah, Am. m. n. ‘nail, spur’; Oss. nix, Dig. nix (2) ‘nail, claw’; Per. nàxun, id.; Arm. cf. ey-ung, gs. -ngan ('stag's horn; nail’. In first sense cf. elonis. In second sense cf. pel-?); Gk. ónux, gs: -ukhos, Myc. onuk-, as Oss.); Lat. unguis, gpl: unguium, as Oss.; Olr. ingu, inga and ionga, pl: ingne, id.; W ewin, pl. -edd, f. id.; Br. win, pl. -u, m. 'finger-nail; Cor. ewyn as Lat.; MHG cf. nagel, m. (nail; Cz. noh, OCS nogiü, m. “griffin”? beside nogütl, Cz. nehet 'nail'; Ukr. cf. also pa-gnisty, pl. ‘nails’; Li. nagas ‘claw’; Latv. nags ‘nail, claw’. (Celtic vocalism unexplained)
op- (1), opi “back, off, out, round, at. (For Gmc. af, aba, abe, etc. see apo). Cf. opitios, od Skt. cf. apatyam, n. ‘posterity, offspring’; Hitt. apecis, adj. "Jost Lyc. epi ‘after; Myc. (am- big.) opi, opi- Cat, but cf. od, od-); Gk. cf. ópi-sthi, -the ‘late’; Lat. ob “against, towards; for, because’; cf. op-pidum ('city', fr. *op-pe- dom, see pedom, iom); opter, propter "on ac- count of, fr. *op- + *-ter-, compar. and *pro- op-ter-); cf. (?) op-inor, ari, v. ‘think’, if for *op-uoin-, cf. Skt. vénami ‘hope’, and op-erió *shut', fr. *op-uerio, WH: LEW and WP: I, 56); Osc. Umb. op “near, with, at^; Venetic op “ar; Alb. cf. afër (“near”, fr. *opter-: Lat. opter); Li. apie, api-, ap- ‘round’; Latv. ap, ap- ‘round, about, on’
op- (2) ‘yield, produce’. Cf. oplos, opətom. WP I, 175. See next Skt. cf. ápnas, n. (1) ‘wealth, property’; Alb. ap, v. ‘give’; Illyr. pers. names Aplus, m., Apla,
881
f. Aplo, mf. (-On-), Teuti-aplos, beside Oplus, Opla; Lat. opës, gp: opum, fpl. ^wealth, power, help’; opulens, -ntis ‘wealthy, influential; opulesco, v. ‘grow rich’; OE cf. æfesn, f. 'tit- bit beside frefer (“consolation', if fr. *pro- Op-); Li. cf. ápstas ‘abundance’ beside apstüs ‘abundant. Same as next? Sense of Illyrian prob. (3)
op- (3) (same as (2)?) “activity, work. WP I, 175. Extn: opnos. Cf. oplos Skt. ápas, n. ‘work’; apás, adj. “active”, cf. also ápnas, n. (2) "work: Av. (?) apo, n. ‘wish’; Hitt. cf. appas ‘workman’ beside happar, gs: happaras “business, transaction”: Illyr. names Aplos, Oplos, a, mf. (See op- (2) but prob. here); It-Alb. ápull (*soft, tender? here?); Lat. Opus, gs: -eris, n. ‘work, business, deed, use"; opus, indecl. (necessary: Skt. apás); cf. also Opés, gp: opum (2) ‘power’; OE eafor, m. & n. “obligations, supplies, auxiliary force; (fr. *opeso: Lat. opera); aferian, v. “bring up rein- forcements'. Other variants: Skt. ápnas (see above) also in Hind. apna, adj. "own: OE zefnan, v. “perform, execute’; ON efna, v. id.; efni, n. ‘substance’; Norw. evne, v. “be able’; evne, s. ��ability’. Cf. further Umb. opeter, adj. "of the best; MHG (*-o-) üeben, v. (act. See õp- below); uober, adj. “active
opákos ‘reversed, averted, everted, contrary, remote’. WP I, 122 Skt. ápākah “distant'; ápak ‘westward’; apäkä ‘distantly’; Arm. hak, cpds. haka- ‘contrary’; hakim, v. ‘lean’; Lat. opācus ‘shading, dense’; OBr. cf. acom, v. inf. ‘deny’; Ir. acc, aicc, s. ‘denial; OHG abah, aboh, abuh, adv. ‘turned back, reversed, perverse’; OS abuh, as OHG; ON ọfugr, adj. as OHG; Eng. cf. awk- in awk- ward; OCS opako, opaky, adv. ‘back, reversed’; Pol. opak, id.; Cz. opak, adv. “again, on the contrary’; Srb. opak, adj. ‘perverse, evil’; Slo- vene opak ‘inside-out beside pak, adv. ‘but, yet; Cz. pak ‘then’; cf. Slovene pačiti “de- stroy’; Cz. cf. páčit se ‘renege’
(operið ‘cover, enclose’. Prob. for op-uer-, q. v. Lat. operio, ire, v. ‘close’; OCz. opeřu, iti, v. ‘cover’, cf. Lat. cooperið, id.)
opətom ‘strength, stamina’. Cf. op- (2) & (3)
op- — oquilos (oqulos)
15
20
25
30
35
40
45
882
Skt. cf. aptas, n. ‘sacrificial ac? beside ápnas, n. id. (and ‘work’; Vedic: *property"); Umb. cf. opeter, gs. "of the best’; OE eafobp, n. “power, strength; G. dial. (?) Effte, Eff, f. (elm: semantics of Lat. robur and robustus?)
(0pin- (opIn-?). See Supt: opi, see op- (1))
opitios (opetios, opot-) “back, again’. Cf. op- (1) and opákos Skt. ápatyam, n. *descendant'; Hitt. (ambig.) apecis ('last. See apo); Gk. opíso ‘back’; OS. OE (ambig.) eft “again”
oplos (opulos) ‘power, force, abundance. Cf. op- (2) and obhel- (1). (Phonology ambig. in Gmc.) Illyr. (personal names) Aplos, Oplos, and cpd. Teuti-oplos (but Italo-Alb. ápull, adj. = “soft, tender); Lat. cf. opulens, opulentus "power. ful, rich, abundant; OE (ambig.) afol, n. *power'; ON afl, n. id.; afli, m. & aflan, oflun, f. ‘gain’; oflugr ‘strong’; OE aflian, ON afla “gain, get; Sw. cf. avlinge, n. “acquisition, pro- perty’; Norw. avl, avling ‘crop’. For the Gmc. forms cf. however obhel-
opnos, see op- (2) and (3) S kt. apnas, n. “possession; act; shape’: Hind. apna, adj. ‘own’; Norweg. evne, v. “be able’; s. ‘ability’; ON efni, n. ‘substance’
opos, see op- (2) and (3)
öpos “ceremony, celebration’. Cf. apos. Evi- dence ambig. WP I, 176 Skt. ápas, n. ‘performance’; Av. àpas, n. *cere- mony, rite’; OHG uoba, f. ‘celebration’; MHG uop, gs: uobes, sm. ‘cultivation’, cf. uober, adj. ‘active’. (If with YE *ō-, cf. op- (2) and (3))
oqu- ‘eye’. Theme of several of the follow- ing entries
(oqu-bhrüs ‘eyebrow’, cf. bhrüs, bhruues for the simplex Gk. ophrüs; OCS obrúvi, f.; Slovene obfv, f. & obrva, id. For Ir. abhra and fabhra 'eye- lid”, cf. upo-)
oquilos (oqulos) ‘eyed; eye’. Cf. oquom, oqumn-, oqus-, etc. Doric optilos, m. ‘eye’; Arm. cf. aðey, i-st. (clear-sighted', appar. fr. a type *oqusil-); Gk. cf. opállios (^opal", or a LW cf. Skt. upalah? LW in Lat. opalus); Li. akylas *keen-sighted'. (The background for Alb. syll 'squinteyed"
883
and Li. ãklas ‘blind’ is uncertain). See next
```


## [2026-09-07T20:21:28.973Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && ls; python3 - <<'EOF'\nimport re\np='WLD_Bd1_pages.txt'\nt=open(p,encoding='utf-8',errors='replace').read()\n# find page tags\ntags=re.findall(r'\\[pdf page (\\d+)\\]',t)\nprint(\"tags\",len(tags), tags[:5], tags[-3:])\n# locate text around \"hväpah\" or \"opus\" or \"amayava\"\nfor kw in ['hvapah','hväpah','amayava','opus, -eris','afnahvant','afnaAvant']:\n    idxs=[m.start() for m in re.finditer(kw,t)]\n    print(kw, len(idxs))\nEOF",
 "description": "Inspect Walde-Pokorny Band 1"
}
```


### [2026-09-07T20:21:30.383Z] TOOL RESULT

```
WLD_Bd1_1930_dli_70244_djvu.txt
WLD_Bd1_1930_dli_70244_text.pdf
WLD_Bd1_pages.txt
WLD_Bd2_1927_dli_106624_djvu.txt
WLD_Bd2_1927_dli_106624_text.pdf
WLD_Bd2_pages.txt
tags 0 [] []
hvapah 0
hväpah 0
amayava 0
opus, -eris 1
afnahvant 0
afnaAvant 0
```


## [2026-09-07T20:21:36.945Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && python3 - <<'EOF'\nimport re\nt=open('WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\ni=t.find('opus, -eris')\nprint(t[i-3000:i+2500])\nEOF",
 "description": "Read Walde-Pokorny op- entry"
}
```


### [2026-09-07T20:21:38.335Z] TOOL RESULT

```
ega „Schweif“. Liden BB. 21, 118.    Aber cech. odr „Pfahl“ (Schef-
telowitz IF. 33, 141, 144 f.) s. u. edh-. Aueh air. odb „Knoten“, eymr. oddf
„Auswuchs, Knoten“ (Bezz. bei Fick II 4 50, Johansson IF. 14, 323 z\v„
Scheftelowitz aaO.) bleibt, obwohl „Pflanzenknoten                         —
                                                            Trieb, SchoBling,
Stengel eine mogliche Begriffsentw. ware, fern, sichert also nicht g'i furs
              4
                  '



idg. Wort, odb, oddf verbindet Liden BB. 21, 111, 118 irrig als *odb(h)o- mit
lat. offa „Bissen, KIoB, Stuck Fleisch" (doch unerklart, s. Yf. LEWb.
                                                                         2
                                                                           s. v.)

und mnd. add, al in. „Geschwulst, Geschwiir", bes. „Fingergesehwiir“,
Pedersen Aspirationen i Irsk 20 (weitere Lit. bei Boisacq s. v.) lautlich
befriedigend als ozbho- mit dacpvg Ilufte (ware dann „ Ansehwellung"
                                                     ,,


                                                                2
vgl. zunachst ipoai, gioiai, ipvtai „Lendenmuskel“, Prellwitz     s. v.),  Fick
 KZ. 43, 152, so daB ein *o.ibheu- zugrunde lage, kelt. ozbh(u)o-; wenig ein-
leuchtend zerlegt Kretschmer KZ. 31, 332 oo<pvg in ost- n doTeov u -\-bhn-
unter Vergleich von ai. mayo-blui- „labend", und Persson Beitr. 415, 717
in dor- -f *o<pvg „Knochen-schwellung“, *ayvg (Z-lose Form neben lacpvdco-
juevog „vollgestopft“; ahnlich L. Meyer Ildb. I 540: unrichtig iiber oacpvc
Fick BB.           und Johansson BB. IS. 24).
                       16, 171
     Gegen Verb, von adga- als * oz-g'io - mit *ozdos. *ozghos s. Scheftelowitz
IF. 33, 141, 144 f. m. Lit,


1.     op- „arbeiten (auch. oder nach Meringcr IF. 17, 127; 18, 20Sf. ursprgl.
         vom Feldbau), zustandebringen Ertrag der Arbeit, Reichtum-'; die
                                                     ;


         Dehnstufe auch mit alter Anwendung auf religiose Handlung oder
         Feier.
               „Werk-‘ (=lat. opus'): av. hr-apah- „gutes Werk" und (wic
     Ai. a pas- n.
auch lm-apah) „gutes Werk verrichtend" upas- n. „Werk, religiose Hand-
                                                          :


lung" (: ahd uoba ,,Feier“): dpnas- n. Ertrag, Habe. Besitz", av. afnah-
vant- „reich an Besitz" (-nes wie in ai. rfknas-, ahd. Irhan und andern
auf den Besitz gebendcn Worten, daher kaum in Beziehung zum u-For-
mans von gr. o/ctju/, aisl. efnan rfni usw.. s. u.) ved. aprd- tiitig. eifrig(?)"
                                            ,                   ;                 ,.



(iiber das von Kluge KZ. 25, 312 damit verglichene got. abrs s. u. bbh-
 „stark").
       Gr. mit (aus           dem Formans stammender?) Binnennasalierung wohl da:ttvi]
 ,,Nahrung,              Getreide. Feldfriichte. Reichtum. Besitz".         ofwios ,.reiehlieh“.
 Oimv’ia              Demeter"      ;



       lat.   opus, -eris „Arbeit,      Beschaftigung, Handlung.        Werk". opus est „es
 ist    notig" („*ist MuBarbeit" nach Meringer aaO.).                 wovon opera -are „ar-
                                                                                       ,


beiten",              osk.   upsannam „operandam", apsahdi          sent   (s.   Gl. 3, 346),   perf.
upscd „fecit", uupsens „fecerunt, operati sunt" (dehnstufiges Pf. wie f ml.
bdt), umbr. osatu „facito", palign. upsasdrr ,,operaretur oder -entur": lat.
ops, opts „Yerm6gen. Reichtum, Macht; Hilfe. Beistand", bei Ennius auch
,.Bemiihung, Dienst", Ops „G6ttin des Erntesegens". inops. cdpia (* co-op in).
                                                                                                                                                 ,




                         2                                            °l'-
1
    76 _                                                                         __




opulentiis „reich an Yermogen,     machtig" (eher mit dem lat. Suffix -uutus                                                                     ,




als in altem Suffixzusammenhang mit aisl. afl: s. Prellwitz BB. 24, 215,
Brugmann II 1, 363: Jacobsolm Phil. 67, 502 Anm.). wohl auch optimus
,,der beste" (eig. „der wozu hilfreiehste" oder noch eher „der \vohlhabendste“;
s. Sommer IF. 11, 213;     von Ciardi-Dupre BB. 26, 21      und anderen nicht                                    I




besser von der Praep. ob                    —   s.   *epi. *opi abgeleitet, weitere Lit. bei Stolz

Hdb. 4 235 Anm. 6); vielleicht der Name der Oscl, Opsn, ’ Omxoi als ,,die
Reichen" oder allenfalls „die Bauern“ vielleicht air. sonime „reich“ damme   :



„arm“ (su-, dus-op-smio-, Strachan BB. 20, S).
          Ags. cefnan ,,wirken, tun“; dehnstufig ahd. uobo „Landbauer“. uoben ..ins
    Werk setzen, ausiiben, verehren", nhd. uben. ahd. noba ,.Feier“, mhd. nop ,.das
    Uben, LandbauA as. obian „feiern‘\                                  aisl. e>fa                „iiben ‘, vfr „gewaltig, heftig“,
    aisl.     efna „ausfuhren“,         cfni „Stoff,                   Zeug                 fur etwas“               (s.   Wood IA. 2<>, 24,
                                                4
    auch Falk-Torp u. evne: das von Fick II 14 verglichene cymr. an ..Stoff,
    Element 11 bleibt jedenfalls fern), ags. cefnan, efnan „ausfiihren“; ahd. afa-
    Idn       „zuwege bringen, arbeiten", aisl. afla
```


## [2026-09-07T20:21:49.575Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && python3 - <<'EOF'\nt=open('WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\ni=t.find('opus, -eris')\nprint(t[i+2500:i+8000])\nEOF",
 "description": "Read WLD further: op-2 and om-"
}
```


### [2026-09-07T20:21:50.894Z] TOOL RESULT

```
                  .,ausfiihren, ausrichten. enverben“,

    ags. afol       n.   „Kraft“,   aisl.   afl n.               ,,   Kraft,                Starke,           Hilfe“,      afli   m.   .,   Starke
    Macht, Ertrag, Yorrat, Baumfriichte",                                             afl    m. „Esse“               (eig. .,Arbeitsstatte“)’

    efla      „starken, ausfiihren,         vermogen" (s. zu diesen Z-Bildungen noch unten).
          Lit. apstas        „Uberflu8, Yorrat", upstiunas                                        ,,Fiille,      Reichlichkeit",            apstits
    ,,reichlich“.
      Ygl. Curtius 510 (aber dqevo; bleibt fern, s. Lit. dariiber u. <fihen-
    .,schwellen“: iiber air. anal ,,Reichtum“, auch bei Stokes IvZ. 36. 274. siehe
    Pedersen KG. I 441, II 5S5, aber auch 677j. Fick I 4 16, 372, II 4 14, III 4
    15, Liden Stud. 73 f., Yf. LEWb.
                                     2
                                       u. ops, optimus, opus. Der Begriff des
    ..Erntesegens,               ist nicht aus ,.saftgeschwellt“ enstanden k d.-roc
                             Ertrags"
    .,Saft“?? auch     im  Vokal   widerspricht dp- „\Vasser; Froehde BB. 21, 19,
    2 f., Johansson IF. 4. 136). sondern ist ..das erarbeitete" (: lat. opus usw.:
    L. Meyer BB. 7. 31 Iff., Fick aaO .j.
        Mit aisl. afl, ags. afol „ Kraft'* ware in der Bed. nachst vergleichbar gr.
    *<i7xekof) „Kraft“ in Av-ansXdaag dvaomoadeig lies., jon. m;."T£Aj/s „kriiftig“,
                                                             '



                                                                                              !
    dhytjTiekeibv „schwach“, bhy>)nf/Jv „Schwache‘ jon. vtjnsXe to „bin ohnmachtig"               ,


      Diintzer KZ. 13. 17 f., Prellwitz BB. 24, 214 f., Y b. 2 47, 313, Brugmann II 2 1,
                                                         T
     i




    303. Bechtel Lex. 246 f.). wozu vermutlich Arte/dwv, AttoXXcov, thess. Aa/.ovv
    (Prellwitz) als „der starke Gott und der elische MN. Tevxl-ajrXog (Prellwitz
                                                     -
                                                         ‘



    KZ. 45, 159). Doch ist das gr. d- gegentiber dem o- der andern Sprachen noch
    nicht befriedigend erkliirt, zumal im cs-St. ^utteXos auch ein d- als Reduktions-
    stufe keinen Platz htitte: entwedcr ist daher *dneXog nur zufalliger Anklang
     (*n-pclos M im-pulsus“??;, oder cs ist allenfalls mit ags. afol, aisl. afl (die dann
    mit ags. (efnan usw. erst durch sekundare Gruppenbildung zsgeschlossen
     waren) unter einem verschiedenen idg. *ap(f)lo- „Kraft“ zu vereinigen.
        Ivein Beleg fur Ablaut a (: o) in unserer Wz. ist (gegen Holthausen IF.
     35, 132) lat. apis „Biene‘‘ (sei gegentiber der Drohne, fileus, als ,,Arbeits-
     biene" benannt; unannehmbar).


         2.   op- „auswiihlen, den Yorzug geben, vermuten“.
           Die Wurzel steckt, wie Wackernagel IF. 3       258 ff. gezeigt hat. in gr.                 1   ,



         imotpopai zu em-orr- „wahlen. auslesen“: lat. *opere ist durch praed-opiont
                                                                °P-    — obh-                                                 177


iHdschr. praedotiont) ,.praeoptant“ (Fest, 244 ThdP.j belegt. Abgeleitet
*opid(n ) „Erwartung, Meinung“, wozu Denominativum opinio „Meinung,
Erwartung“, oplnor -uri „vermuten, wiihnen, meinen‘ ipopiln- *opin- wie
                                                                                                   -
                                                                                                                    :
                                   ,


lat. natione  n. natine:lat. legiOnnn  osk. leginum).
                                       ,
                                                      Frequentativum zu :



*opio,   -ere ist lat. opto,                -arc        „wiinsehen“,                wozu   optio f         „freie       Wahl“, m.
„Gehilfe,          FeldwebelA              (Gegen           die Yermutung v. Fierlingers                      KZ. 27, 477 f.,
da 6 lat. opto als *o-peto zu erklaren sei, apricht optio prnedopiont oplnor ).                ,                         ,



   U. upetu „eligito, optato“, opeter gen. ,,boni“ (v. Planta I 334), o. nftcis
„optati oder dgl.“ (v. Planta 1 425, IF. 2, 440, Skutsch BB. 23, 101) ge-
lioren nach aller Wahrscheinlichkeit hierher.
   Ab. za-(j)apz „Vermutung“, ne-m;-apbm „unvermutet“ (vgl. lat. in-, nec-
opintis „unvermutet“, welches Riickbildungen aus inoplnatus sind. vgl.
Skutsch. De nom. suff. no- ope form. 23) s. Fick KZ. 19. 259, Berneker
SEW. 29 f.
    Gr. eiamvgg „plotzlich“. welches Bezzenberger-Fick BB. 0, 236 vergleichen
(zweifelnd Fick I 4 367), gehort nicht hierher, da der Yokal nicht stimmt
und die Negation fehlt. Nicht annehmbar auch Breal Msl. 13, 3S2f. Am
                                                                  t)ber Brugmanns
                                                                                               11
 ehesten *e£-a-mvfas zu mvinog „klug, verstandig                                                       .



 Deutung lat. oplnor aus *op-isna- ..worauf verfallen“ s. unter cis- „sich
 het’tig bewegen“.
    Meillet Msl. 9, 55 f. stellt lat. opinio als *op-vrnio zu got. terns „Hoffnung“
 usw., was aber wegen des 7 von oplnor unmoglich ist.
    Uber lat. oplnor zu g
```


## [2026-09-07T20:22:00.521Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && python3 - <<'EOF'\nt=open('WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\nfor kw in ['amavant','omo-','ome-','Ungestum','ungestum','amatra','Andrang','emsig']:\n    idx=[m.start() for m in __import__('re').finditer(kw,t)]\n    print(kw,idx[:6])\nEOF",
 "description": "Locate WLD omə- entry"
}
```


### [2026-09-07T20:22:01.855Z] TOOL RESULT

```
amavant []
omo- [804786, 828582, 832885, 834188, 834599, 834615]
ome- [1263027]
Ungestum [801558, 3215628]
ungestum [831571]
amatra [925313]
Andrang [487846, 637683, 830687, 3684877, 3685591, 3685937]
emsig [192752, 916923, 1822851, 3470871, 3493050]
```


## [2026-09-07T20:22:05.207Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && python3 - <<'EOF'\nt=open('WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\nprint(t[925000:928500])\nEOF",
 "description": "Read WLD around amatra"
}
```


### [2026-09-07T20:22:07.598Z] TOOL RESULT

```
                                             iaro-    — ieu-                                                 199

-jamo).         Ostholf KZ. 23, 86 und bes. Solmsen Beitr. I 194 fF. m. Lit,. Ber-
neker 444.             —
                      Unrichtig iiber jama Wiedemann BB. 29, 317 (mit sek. j-
zu     ai.   amatra-m „GefaB“. das auf den Begriff der Hohlung gehe. doch
s.   am- „fassen“), nicht iiberzeugend auch Schulze SBprAk. 1912, 581 ts. u.
*himo- „schlammig“).


iaro- „Huhn" ? ?
     Dieser Ansatz  gilt nur, verm man annimmt. da          nir. rirln „Hiihnchen.           1.1



nsch. cireag        auf air. *ainn zuriickgehen.
                               ds.                    Andrerseits wird in gall.
JariJla EN.. acymr. icir gl. ales CPI. yeyr ), clwj-iar „Rebhuhn", acorn.
yar gl. gallina, br. iar „poule“ (Demin, iaric), clugar ,,perdrix“ kaum einUber-
                               >
gang von je ja erfolgt sein (vgl. Pedersen KG. I 65 Anm. 1). Jeden-
falls weisen lett. irbe „Rebhuhn“, lit. ('rube, jirubS „Haselhuhn“, russ.-ksl.

jarjabb , jerjabb „Rebhuhn" usw. auf eine Grundform *en.b- und konnen
mit den kelt. Wortern keinen Zusammenhang haben.                  Vgl. Trautmann
104,  Pick* II 223. Viel eher diirfte die Vermutung Pokornys (brieflich)
zutreffen, daB die kelt. Worter mit der verbreiteten si. Sippe wie bg. jiirka
jdrica ,,junges Huhn" usw. (s. oben I S. I05j zusammengehoren.


ie-,    erw. ie-k- „werfen‘\
     Gr.     Trj/a,    t)]xa.          yxa,      fjaco,   frog „werfe, sonde",           lat.       jacio   ,
                                                                                                                -ere, jcci,     jac-
tum „werfen“, jaceo                     ,
                                            -ere       „(sieh dahingestreckt,           niedergeworfen haben                     =
„liegen“.         S.           unter    si?i-    „entsenden“.


1.   ieu-      „vermengen, bei der Speisezubereitung"                                    (:        ieu-.             ;
                                                                                                                         in-,   iu-
        letzteres auf Grund der Dehnstufen, oder vor einer set-Basis *ieu ri x -)
        vermutlich eine Sonderanwendung von ieu- „vcrbinden“.
     Ai. yauti,                yuvati „vermengt“,                  ud-a-yaati „riihrt auf". pruyuuti                         „riihrt
urn", yfitt-          f.       ,AIisehung“, ayavana-      jaunv, jnviau, janti
                                                                         n. .,Ruhrl6ffel";    lit .

„heifies Wasser dariiber gieBen", lett. jdut „Teig einriihren. mischen", jaws
.,Gemengsel von Viehfutter", lit. jovulas „Schweincfutter, Treber"; air. 7th
„puls“, acymr. lot, ncymr. uivil, bret. iud, acorn, iot ., Briihe, Brei" iaus
ieu-to- ? s. Fick II 4 224, Pedersen KG. 165. Sommer Gr. Ltst. 142); gr.
  'dog, gv&og „Gerstenbier“ (agypt. Ursprung bestreitet Schrader RL. 90,
halt     fur     wahrscheinlich                    L. Meyer          Hdb. [II 271. Sommer Gr. Ltst. 153;;
alb. <jer .,Suppe" (id-no- ?                           Pedersen KG. I 65).
     s-St.     ins-,           id(n)s-      vielleicht       in     griech. jv/nj „Sauerteig“                   (* ins mil      oder
aber *ia-mG                ;
                                nicht nach Brcal Msl. 12, 314 f. mit v                        = z zu        'Cs(o)   und
„Briihe,       Su
```


## [2026-09-07T20:22:16.393Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && python3 - <<'EOF'\nt=open('WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\ni=t.find('opus, -eris')\nseg=t[i+8000:i+20000]\nprint(seg)\nEOF",
 "description": "Read WLD pages 177-179"
}
```


### [2026-09-07T20:22:17.963Z] TOOL RESULT

```
r. ahog „Rede“ (Moulton IA. I, 161; und zu *ei-
 „gehen“ (Stolz HG. 1, 26S) vgl. Yf. LEW. 2 542.
    Fick I 4 367. Muller Aldt. Wb. 302f.

 3,   op- ,,Feldahorn“?
   Lat. opulus „acer campestre ‘. Einem idg. *opolo- konnte germ. *a['ara-,
                                                            !




 *abara- zur Seite stehen, welches moglicherweise nach Falk-Torp 757 in
 norw. dan. mur ,,Feldahorn‘   iilt. dan. naver ds„ schwed. dial, narrr ds.
                                                    -

                                                        ,


 zu finden ist. Yielleicht stammen die Worter aus dem alteren Nieder-
 deutschen und haben, wie sonst oft. ein n- im Anlaut angenommen. denn
 deutsche Dialekte haben fiir den gleichen Baum die Bezeichnung B liff-
 ebern und T Veifineber,                   Wei/leper und Wei/lncper.
      Doch         ist   opulus vielleicht gar nicht                            lat.   (Varro RR.          1, S,    3:   ..Mediola-
 nenses    .   .   .   vacant opulos").
      Falk-Torp 757, 1521                    (   naur).

 5bh- „ stark heftig“??
      Pedersen KG. I 49 vergleicht            unbar ,.Ubermut". cymr. ofer
                                                                       air.   obar,
                                                        mit got. abrs ,,io/v-
 „eitel“, bret. cuvcr ,,(gout) fade; paresseux, negligent'                                             1




 Qog'\ abrabu „sehr“, biabrjan „vor Erstaunen oder Betroffenheit auBer sich
 geraten“ (Gdbed. jedenfalls nicht „furchterlich“, so daB Ficks II 4 50 Ver-
  gleich       mit         gall.   Exvbnus MN.,                       eig. „furchtlos“,      cymr. of              „Furcht“,    air.

  — mit analogischer Dehnung — onion                                       uamon „Furcht“. den Pedersen
                                                                                ,

  zw. mit obigem koinbiniert,                                   wohl zu entfallen hat). Uoch ist die Be-
  deutungsubereinstimmung nicht recht scharf zu erfassen. obar setzt einen
  ^-Diphthong, nicer Langvokal voraus, und wird abrs x on Liden St. 74 mit
                                                                                                                                              :




178                                                             obliel-   — omo-, oma-

*apo „ab, weg“, aisl. afar „sehr“ verbunden, wasfreilich aucb nicht zweifels-
frei ist (s. nach Uhlenbeck PBrB. 30, 253, auch gegen Johanssons IF. 3,
241 Verb, von abrs mit ai. ambhas- „Gewalt“, cech. obr „Riese‘' (dies mit
aruss. obrim „ Aware" zum Awarennamen), wogegen auch Yf. LEWb. 2 u.
omnis abrs auch nicht zu ai. ciprd- „tatig, eifrig (?)“, s. idg. *op- „arbeiten“).
           :




obhel- „fegen“.
  Arm. a velum „ich fege“, gr. dcpe/lm ds., bcfekim „Besen“,                                                                        ocpehgov
xdllvvTQov Hes.. dcpefaoevco „fege‘, Pedersen KZ. 39, 336.


om(e)so-s „Schulter\
     Ai. dnisa-h                   „Schulter        ‘
                                                        ;       arm. us gen. nsoy                  ds.   (Hiibschmann Arm. Gr.
1 484);
     gr. thyog                   ds.   aus *omsos und nicht *Umsos (so Solmsen KZ. 29, 62 f.),
vgl.    eTiouuddtog hei Theokr.                    lat. umerus aus *omesos ds. umbr. use, ose

,,in   umero“;
     got.          ams ds. (germ. *atnsa -), altn. ass „Bergriicken“.
     Fick I 4 168. 369, III 4 16f., Falk-Torp 9 (acts II vgl. 1429) Boisacq lOSlf.                   ;


     Moglicherweise zur Wz. em- „nehmen — tragen“.


Ohio-,     onie- ,gehobene Kraft auBe rung, energisch in etwas oder gegen
        etwas vorgehn“; daraus einerseits „fest worauf bestehn, festmachen
        = eidlich bekraftigen“, andrerseits „zusetzen, qualen, schadigen“.
     Ai.           cmtfi          „dringt   an,    bedrangt, versichert eindringlich, schwort“ (in
letzterer Bed. amlsva                           „schwore!“, Con it „er schwur“, sim-cLmirC „sie ge-
lobten“.  thennat. s un-amcmU „sie geloben“), abhy-anilti „plagt, schadigt“,
dniirci „Drangsal, Leiden, Krankheit“ mit themat. Gestaltung der 2. Silbe
('write „bedrangt“, cimatra- ,,fest“, dmatkmt- „ungestiim. kraftig“ = av. ama-
mnt- „kraftig. stark, inachtig, gewaltig                                      11
                                                                                   ,       ai.   dma- m. „Andrang, Betaubung“
= av. anin- „Kraft, miinnliche Potenz. Angriffskraft                                                     -1
                                                                                                              ,   Adj. „stark“,      ai. Clmrt-
yaU „schiidigt; ist schadhaft, krank'*, dmnya- m. „Krankheit“.
  Av. amayavd „Leid, Drangsal“ (vgl. dazu Bartholomae Stud. II 178:
vielleichtnach einem ** amayeiti fiir condyciti aus einer Form wie ai. amir a
umgebildet. aber doch wohl auch in diesem Falle einen AVzansatz *omdi-
empfehlend, welchem auch das feste          von aini-li , -ca ziemlich giinstig        t


ist,   vgl.                Brugmann II      2
                                                1,          207, II 2 3, 154, Persson Beitr. 669;                          s.   auch unten
zu     gr.         dtionog.            Venn ai. amind- „ungestum.                                   stiirmisch“ bedeutet,              diirfte
freilich nicht                    von festem                i    als ind.   Tiefstufe              gesprochen werden).                  Dazu
(Aufrecht RhMus. 40. 160), gr. duvC’iu. oyvvco ,,schwore“ ( oyooai buib/ioy.a
                                                                                                                                ,             ;


Fut. ufmrai Xeubildung fur *ofi6erat, s. Brugmann-Thumb GrGr. 4 371 m.
Anm.      einen St. due- hat Bechtel A7 okalkontr. 95 nicht erwiesen), avv-
               !       :



o about            :      hom. buoitog (Beiwort von nohuo;. rely.og, Oava-
                           ai.   scuu-amantf    ,

rog,    yijgag) „plagend,         (s. Solmsen Unt. 101 f. m. Lit.; -wolil metr.
                                                leidvoll“
Delinung eines auf *o/<o-p« ai. amt-va beruhenden du6(f)tog, kaum als
                                                                  :



-buot-. buoH-f-iog als gr. Sttitze fiir einen Wzansatz *omr,i- „auszubeuten;
hierher (Jacobsohn Phil. 57, 512. KZ. 42. 160 Anm. 1; buo-y.h) „Zuruf. Schel-
ten, Drohung“, buo-y.Xdco (:ai oma-li).                               .
                                                      omo-   :   umo-                                          179

     Obwohl opvvvat,            o/liogcu   an sich aus *apvvvat, *au6c,ai assimiliert 8ein
konnte, ist die gr. und ar. Sippe nicht nach Neisser BB. 30, 299 (wo aber
gute sachliche Bemerkungen zum Schwur unter Anfassung des Gegen-
standes, bei         dem man schwort) mit *am- „fassen“ zu verbinden.
     Aisl. ama „plagen, belastigen”, amasfc   „AnstoB nehmen, Unwillen fiihlen.
sich       womit abplagen“, nisi, ami m. „vexation, annoyance”, norw. ama „an-
dringen, antreiben”, ama seg „sich anstrengen, alle Krafte aufbieten”, nisi.
amstr „rastlose Arbeit, Anstrengung”, ami n. unaufhorliche, bes. erfolglose
Beschaftigung mit einer Sache“, norw. amla „sich abmiihen, arbeiten, bes.
ohne Erfolg”, Amali der Name des ostgotiscben Konigshauses, die Ama-
lunge. Amulinge der dt. und ags. Heldensage”, ahd. Amal-olf u. dgl.    ahd.                                ;

                                             11
cmi-j „bestandig,  fortwahrend    emiffig, ema^lg „bestandig, beharrlich”,
                                                  ,


nhd. cmsig (ags. nit „Riese“? aus *am\i\t-V> Liden Stud. 57 f.).              .




     S. FickI 4 16, 167, 368 f., Ill 4            16 (iiber lit. iimaras „Sturm, Ungestiim“ usw.
s. aber u. eum - *omo- „roh“ ist in der Bed. nicht zu vermitteln), Brug-
                        ;

                                2
mann IF.   12, 401 f., Grdr. II   1, 207 (unter moglicher Verkniipfung mit
*md- „sich miihen” nach Noreen Ltl. 85, Hirt Abl. 95), Liden Stud. 57 f-
(aber in Verb, mit idg. am-, s. auch 75 Anm. I, Falk-Torp u. amper
Nachtrag); zur Bed. aufier Brugmann (und Neisser) aaO. auch Schroder
Abl. 88.


omo-        :   omo- „roh ^bitter, scharf”?).
  Ai. amd-h „roh“: gr. tburk „roh, grob, grausam” (vgl. ib/nyon)? „rohes
Fleisch fressend usw.“ = ai. a mad- mit schon idg. Kontraktion von *omos
und *ed- „essen“, Boisacq 1082); arm. hum (mit u<o oder u nach Hiibsch-
mann Arm. Gr. I 468) ds.; air. om „roh c. of ds., hierzu air. umac „Erz.
                                                                    tl
                                                                          ,



Ivupfer” ( *omiio -). eigentlich „Roherz“ (Pedersen KZ. 36, 85; KG. I 32.
Hessen ZsfceltPhil. 9, 13j.
     Reduktionsstufe vielleicht in ai. amld-h, ambld-h „sauer, Sauerklee” (vgl.
iimriih         „Hangobaum“ [der bitter schmeckenden Samen hat]; Curtius 338 f..
Osthoff Morph. Unt. Y 75, 124,          Brugmann Grdr. II 2 I 350); arm. amoR             ,
       :

„siiB‘ ? (zum Bedeutungswandel vgl. germ. *salta- zu lit. saldiis „siiB“), alb.
emM’e „sii6“, tembl'e „GaIle“; unsicher ist maked. dfigo- „zusanimenziehend“,
afiaov dgiyavov Hes. (Hoffmann, Maked. 41): lat. amarus „bitter‘ [worin
           '




nicht etwa nach Prellwitz BB. 23, 72 die Wz. *as- „brennen“ (lat. area)
zu suchen ist. Auch die Beziehung zu amo „liebe“ (Zimmermann KZ. 3S.
503) ist abzulehnen]; ndl. amper „scharf, bitter, unreif”, apr ,.scharf‘ *am
                                                                         (
praz iiber *appr ). aschw. amper „sauer, scharf, bitter”, ags. ompre ahd.                              ,

ampfaro „Ampfer“ (*ampra aus *ambra < *amro). Johansson IF. 3, 240
sucht fiir die germ. Worter andere, unglaubhafte Verbindungen.
   Unsicher ist die Beziehung von ags. dm m. ,,Rost“, Oman f. pi. ,,Rose'                                        !

                                                                                                                     .


altn. ama f.. amu-sdtt f. „Rose“.       Dazu lit. dmaras, emerai „Meltau“?
(Fick lll 4 16, Falk-Torp 4 (name; s. 1428).     Abzulehnen der Zusammen-
hang mit idg. omi- omo- (s. d.) (Fick III 4 Falk-Torp aaO. und 21: amper:
                            :                                         .



s.   1431).
     Vgl. weiter Fick I 4 17, 167, 372.                          Vielleicht       ist   wegen amld-h, amarus
amper eine eigene Wz. am-                  „bitter,          sauer“ anzusetzen.
     Walde, Etymologifcches Worterbuch. I.                                                        13
ISO                                        oner-       — onogh-      (   :   ongh-, nogh-                     ;
                                                                                                                      ngh-)


oner- „Traum“.
  Gr. ovag nom. acc. n. „Traum“ und Adv. „im                                                                      Traum“; dveigog             ,
                                                                                                                                                  - ov ,       aol.
dvotgog,    kret. avaigog(wohl durch Ass. aus *ovaigov, -cg) „Traum“, gen.
att. jon. dvdguzog ; arm. anurj „Traum“ (a- aus anl. o- wie z. B. in atnmn

„Zahn“, ateam „hasse“; -nr- aus -or-, so daft anur-j drag = zexfuog zex-                                                      :                            :




/Liag; -rj- aus -ri-, vgl. oveigog, *ovatgog  welcher i’o-St wohl auf Grund                ,


eines /-Lokativs *oneri, on e ri neben *onr, *onur entstanden ist. Ygl. Bar-
tholomae BB. 17, 103, IF. 2, 26S, Johansson BB. 18, 34; Hiibschmann A
```


## [2026-09-07T20:22:31.945Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AE%D9%88%D8%A8",
 "prompt": "Give the full Persian etymology section for خوب (xub) verbatim: what Middle Persian, Proto-Iranian and Avestan/Sanskrit forms are cited, and which authorities (Hasandust, Horn, Hübschmann, MacKenzie, Cheung) are named."
}
```


## [2026-09-07T20:22:32.987Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/often",
 "prompt": "Quote the etymology of \"often\" and \"oft\" verbatim, including any Proto-Germanic form and any PIE root suggested (e.g. *upo)."
}
```


### [2026-09-07T20:22:36.993Z] TOOL RESULT

```
# Etymology of "Often" and "Oft"

**Often:** "repeatedly, again and again, many times, under many circumstances," mid-13c., an extended form of oft, in Middle English typically before vowels and h-.

**Oft:** Old English oft "repeatedly, again and again, many times; frequently; under many circumstances," from Proto-Germanic *ufta- "frequently", a word of unknown origin, perhaps from a suffixed form of PIE root *upo "under."
```


### [2026-09-07T20:22:37.296Z] TOOL RESULT

```
# Persian Etymology for خوب (xub)

Based on the Wiktionary content provided, the Persian etymology section cites the following forms but **does not name any of the authorities you mentioned** (Hasandust, Horn, Hübschmann, MacKenzie, or Cheung):

**Middle Persian form cited:**
"𐭧𐭥𐭡 (xūb)"

**Proto-Iranian form cited:**
"*HhuHā́pah"

**Proto-Indo-Iranian form cited:**
"*HsuHápas"

**Proto-Indo-European forms cited:**
"*h₁su- ("good") +‎ *h₃épos ("work")"

The etymology tree shows these layers of linguistic descent but provides no scholarly attributions. The References section lists dictionary sources (Steingass, Aryanpur-Kashani, Rubinčik, Hayyim, and Langenscheidt) but none of the historical linguists you specified appear in the article.
```


## [2026-09-07T20:22:43.525Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/option",
 "prompt": "Quote the etymology of \"option\" verbatim, including the Latin forms and the PIE root given (e.g. *op- \"to choose\")."
}
```


## [2026-09-07T20:22:45.088Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/%C4%81ma",
 "prompt": "Does this page exist? If so give the Proto-Iranian reconstruction, its meaning, its PIE source and the Avestan/Persian descendants."
}
```


### [2026-09-07T20:22:46.522Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-07T20:22:47.758Z] TOOL RESULT

```
# Etymology of "Option"

According to the Online Etymology Dictionary, the word "option" comes from circa 1600, meaning "action of choosing." The entry states:

"from French _option_ (Old French _opcion_), from Latin _optionem_ (nominative _optio_) 'choice, free choice, liberty to choose,' from _optare_ 'to desire, pray for, choose'"

The source traces the root further back, noting that De Vaan "derives it from Proto-Italic _\*opeje-_ 'to choose, grab,' from PIE _\*hopeie-_ 'to choose, grab.'"

The entry also mentions the PIE root in the related entry for "adoption," listing it as the "PIE root _\*op-_ (2) 'to choose.'"
```


## [2026-09-07T20:22:53.798Z] TOOL CALL #50: WebSearch

```json
{
 "query": "Aršāma Arsames etymology \"bear\" arša ama Old Persian name meaning \"having a hero's strength\""
}
```


### [2026-09-07T20:23:00.274Z] TOOL RESULT

```
Web search results for query: "Aršāma Arsames etymology "bear" arša ama Old Persian name meaning "having a hero's strength""

Links: [{"title":"Arsames - Livius","url":"https://www.livius.org/articles/person/arsames/"},{"title":"Arsames (satrap of Cilicia)","url":"https://en.wikipedia.org/wiki/Arsames_(satrap_of_Cilicia)"},{"title":"Arsames","url":"https://en.wikipedia.org/wiki/Arsames"},{"title":"Arsaces","url":"https://en.wikipedia.org/wiki/Arsaces"},{"title":"Arsamosata","url":"https://en.wikipedia.org/wiki/Arsamosata"},{"title":"Arsames I","url":"https://en.wikipedia.org/wiki/Arsames_I"},{"title":"Arsames (satrap of Egypt)","url":"https://en.wikipedia.org/wiki/Arsames_(satrap_of_Egypt)"},{"title":"Arsames (disambiguation)","url":"https://en.wikipedia.org/wiki/Arsames_(disambiguation)"},{"title":"ARŠĀMA - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/arsama-greek-arsmes-aramaic-rsm-name-of-several-achaemenid-notables/"},{"title":"Old Persian Submitted Names - Behind the Name","url":"https://www.behindthename.com/submit/names/usage/ancient-persian"}]

Based on the search results, I found detailed information about the etymology of Aršāma/Arsames:

Arsames is the Hellenized form of the Old Persian name Aršāma, meaning "having a hero's strength". The name is a compound, composed of aršan ("male, hero") and ama ("strength").

This was a common name within the Persian Achaemenid family as well as amongst the Persian elite of the Achaemenid Empire (550–330 BC). The name is attested in Aramaic as ʾršm.

Note: The search results do not contain information about the name meaning "bear" or about an "arša" element specifically referring to "bear" as suggested in your query. The etymology documented in these sources clearly indicates that the name is composed of "aršan" (male/hero) and "ama" (strength).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-07T20:23:15.593Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://www.iranicaonline.org/articles/arsama-greek-arsmes-aramaic-rsm-name-of-several-achaemenid-notables/",
 "prompt": "Quote what this article says about the etymology and meaning of the name Aršāma — the elements it is composed of, and any alternative interpretations (bear vs hero/male)."
}
```


## [2026-09-07T20:23:16.300Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://en.wikipedia.org/wiki/Arsames",
 "prompt": "Quote the etymology paragraph verbatim, including the Old Persian form, the elements and the meaning, and any cited scholar."
}
```


### [2026-09-07T20:23:17.372Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-07T20:23:20.944Z] TOOL RESULT

```
# Etymology of Arsames

According to the Wikipedia article, the etymology section states:

"His name (_Aršāma_) translates to 'having a hero's strength'."

The article identifies the Old Persian form as **Aršāma** and notes this translation meaning, though it does not break down the individual etymological elements or cite a specific scholar for this derivation in the main text. The reference is attributed to "Shahbazi" in the citations.
```


## [2026-09-07T20:23:34.514Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN opus ===\"; grep -n \"opus, work\\|L. opus\\|opera, work\\|copia\\|officium\\|manu operare\\|manoeuvre\\|maneuver\" KLN_1966.txt | head -20",
 "description": "Grep Klein for Latin op- words"
}
```


### [2026-09-07T20:23:34.588Z] TOOL RESULT

```
=== KLN opus ===
7581:as  in  cacochroia.  —  Fr.  Gk.  /poi&,  ‘color’,  which is  rel.  to  /pcopia,  ‘color’.  See  chrome  and  cp.  the second  dement  in  dischroa,  Xanthochroi. -chroic,  combining  form  meaning  ‘colored’,  as  in erythrochroic.  —  Formed  with  suff.  -ic  fr.  Gk. /poia,  ‘color’.  See  -chroia. chroma,  n.,  the  quality  or  intensity  of  a  color.  — Gk.  /p£Sp.a,  ‘color’.  See  chrome, chromaffin,  adj.,  having  affinity  for  chromium salts.  —  A  hybrid  coined  fr.  Gk.  /pcopta,  ‘color’, and  L.  off  mis,  ‘related’.  See  chrome  and  affinity and  cp.  paraffin.
7582:chromatic,  adj.,  i)  pertaining  to  color;  2)progres- sing  by  halftones  (mus)  —  L.  chromaticus,  fr. Gk.  /pcopion-on);,  ‘relating  to  color’,  fr.  /pojpa, gen.  xpcopiaxo;,  ‘color’.  See  chrome  and  -atic  and cp.  achromatic,  dichromatic,  trichromatic,  ortho- chromatic.
7585:chromatin,  n.,  protoplasm  occurring  in  the  nuclei of  cells  (biol)  —  Coined  by  the  German  ana¬ tomist  Walther  Flemming  (1843-1905)  in  1879 fr.  Gk.  /pciiaa,  gen.  /pco|j.aTo;,  ‘color’.  See chrome  and  chem.  suff.  -in. chromatism,  n.,  abnormal  coloration.  —  Gk. /pco|j.omcrp.6;,  ‘a  coloring’,  fr.  ypa>|j.cm^£iv,  ‘to color',  from  ypcojaa,  gen.  /pcopuxToc.  See  chrome and  -ism  and  cp.  chromism. chromato-,  before  a  vowel  chromat-,  combining form  denoting  color  or  chromatin.  —  Gk.  /pco- piotTo-,  /pcojAXT-,  fr.  /piopta,  gen.  /pcopiaTo;, ‘color’.  See  chrome.
9123:copious,  adj.  —  L.  copiosus ,  ‘well  supplied,  plenti¬ ful,  abounding,  copious',  fr.  copia,  ‘plenty, abundance’,  contraction  of  *co-opia,  fr.  co-  and ops,  gen.  opis,  ‘power,  might,  abundance,  wealth, riches,  treasure’.  See  opulent,  and  cp.  copy  and the  second  element  in  cornucopia.  For  the  ending see  suff.  -ous.
9146:Derivatives :  copulative,  n.,  copulative-Iy,  adv. copy,  n.  —  ME.  copie, fr.  MF.  ( =  F.)  copie.  ‘abun¬ dance;  copy’,  fr.  L.  copia,  ‘plenty,  abundance’; see  copious.  For  sense  development  see  next  word, copy,  tr.  and  intr.  v.  —  F.  copier,  fr.  ML.  copiare, ‘to  transcribe’,  orig.  ‘to  write  in  plenty’  (fr.
9147:L.  copia,  ‘plenty,  abundance’),  whence  arose  the particular  meaning  ‘to  write  the  original  text many  times’.  See  prec.  word, copyist,  n.  —  A  hybrid  coined  fr.  copy  and  -ist, a  suff.  of  Greek  origin.
9230:cornucopia,  n.,  i)  the  horn  of  the  goat  Amaltha, which  suckled  Zeus;  2)  a  horn  of  plenty;  3)  a- bundance;  4)  a  horn-shaped  receptacle  ( Greek mythol. )  —  Late  L.  cornucopia,  for  L.  cornu cdpiae,  ‘horn  of  plenty’,  fr.  cornu,  ‘horn’,  and cdpiae,  gen.  of  copia,  ‘plenty’.  See  corn,  ‘horny induration’,  and  copious, cornucopiate,  adj.,  resembling  a  cornucopia.  — Formed  fr.  prec.  word  with  adj.  suff.  -ate. Cornus,  n.,  a  genus  of  plants,  the  dogwood  and the  cornel  (hot.)  —  L..  ‘cornel  tree'.  Sec  cornel, cornute,  cornuted,  adj.  —  L.  cornutus,  ‘horned’, fr.  cornu,  ‘horn’.  See  corn,  'a  horny  induration’, cornwallite,  n.,  a  basic  copper  arsenate  {mineral.)
14055:ex  officio.  —  L.,  ‘by  virtue  of  an  office’,  formed fr.  ex,  ‘out  of’,  and  abi.  of  officium,  ‘service; office’.  See  ist  ex-  and  office, exogamy,  n.,  marriage  outside  the  tribe  or  clan ( anthropo! .)  —  Lit.  ‘outside  marriage’;  com¬ pounded  of  exo-  and  -gamy.  Cp.  endogamy. Derivatives:  exogam-ic,  exogam-ous,  adjs. Exogenae,  n.pl.,  the  Dicotyledones  (bot.)  — ModL.,  lit.  ‘growing  outside’  (see  exo-  and
22783:maneuver,  manoeuvre,  n.  —  F.  manoeuvre,  fr.  OF . manuevre,  maneuvre,  fr.  VL.  manuopera  (a  word occurring  in  Charlemagne's  Capitularies  in  the sense  of  ‘statute  labor’),  fr.  manuoperare,  cor¬ responding  to  L.  manu  operari ,  ‘to  work  by hand',  fr.  manu,  abl.  of  manus,  ‘hand’,  and  ope- rdri.  See  manual,  adj.,  and  operate  and  cp.  man¬ ure  and  mainour,  which  are  doublets  of  ma¬ neuver.
22784:maneuver,  manoeuvre,  intr.  and  tr.  v.  —  F.  ma- nctuvrer,  fr.  VL.  manuoperare.  See  prec.  word. Derivatives;  maneuver-able,  maneuvr-able,  adj., maneuver-abil-ity,  maneuvr-abil-ity,  n.  maneu- ver-er,  manoeuvr-er  n.
22833:mannitol,  n.,  a  white  crystalline  compound (C6H8(OH)6  (chem.)  —  Formed  fr.  prec.  word with  suff.  -ol  (for  alcohol), mano-,  combining  form  meaning  ‘thin,  rare  ;  of¬ ten  used  also  in  the  sense  of  ‘gas,  vapor’.  —  Gk. jj.avo-,  fr.  pav-jc,  ‘thin,  rare’.  See  manometer, manoeuvre.  —  See  maneuver, manometer,  n.,  an  instrument  for  measuring  the pressure  of  gases  and  vapors.  —  F.  manometre, lit.  ‘instrument  for  measuring  that  which  is  thin’, coined  by  Varignon  (1654-1722),  fr.  Gk.  p-avoc, Att.  pav6?  (for  ),  ‘thin,  rare’,  and  ui-
22850:‘the  sum  which  the  bridegroom  had  to  pay  for his  bride’,  OHG.,  MHG.  munt,  ‘hand,  protec¬ tion’,  OHG .foramundo,  MHG.  vormunde,  ‘pro¬ tector,  guardian’,  G.  Vormund,  ‘guardian’, OFris.  mund,  ‘guardianship;  guardian’,  Co. manal,  ‘sheaf’,  MBret.  malazn  (metathesized fr.  *manazl),  ModBret.  malan  (fr.  *manatlo),  of s.m.,  and  prob.  also  with  Gk.  pipt],  ‘hand’.  Alb. maf  (for  *  mar-no),  ‘I  take,  receive’.  All  these words  prob.  derive  from  the  heteroclitic  I.-E. base  *man/mar,  ‘hand;  to  take  into  one’s  hand’. Cp.  manus,  mainpernor,  mainprize,  maintain, manacle,  manage,  mancinism,  manciple,  man¬ date  and  words  there  referred  to,  maneuver,  man¬ icure,  manifest,  maniple,  manipulate,  manner, mansuete,  manubrium,  manufacture,  manumis¬ sion,  manumit,  manure,  mastiff,  amanuensis,  bi¬ manual,  emancipate,  legerdemain,  mortmain.  Cp. also  mound,  ‘heap  of  earth’,  mund,  Edmund, Osmond,  Raymond,  Sigismund.
22861:See  maneuver  and  cp.  inure.
24271:monochord,  n.,  an  instrument  having  only  one string  or  chord.  —  ME.  monocorde,  fr.  MF. (=  F.)  monocorde,  fr.  Late  L.  monochordon,  fr. Gk.  (zov6xop$ov,  prop.  neut.  of  the  adjective [xovoxopSo?,  ‘having  but  one  string’,  used  as  a noun;  compounded  of  p.ovop,  ‘alone,  single’, and  x°p8r],  ‘string’.  See  mono-  and  chord, monochroic,  adj.,  of  one  color.  —  Formed  with adj.  suff.  -ic  fr.  Gk.  uov6xpoop,  ‘of  one  color’,  fr. [z6voc,  ‘alone,  single’,  and  XPol“>  ‘color’, which  is  rel.  to  xP“Fa,  ‘color’.  See  mono-  and chrome  and  cp.  next  word, monochromatic,  adj.,  having  only  one  color.  — See  next  word  and  chromatic, monochrome,  n.,  a  painting  or  drawing  of  a  single color.  —  Introduced  into  English  by  the  diarist John  Evelyn  (1620-1706)  fr.  Gk.  [zovoxpwpiog, ‘of  one  color’,  fr.  p.6vog,  ‘alone,  single',  and Xpcopia,  ‘color’.  See  mono-  and  chrome  and  cp. monochroic.
26133:Derivative:  offertori-al,  adj. office,  n.  —  ME.,  fr.  OF.  (=  F.),  fr.  L.  officium, ‘service’  (in  Eccles.  L.,  ‘church  service’),  which stands  for  *opi-faciom,  lit.  ‘work-doing’,  fr.
26136:officer,  n.  —  ME.,  fr.  OF.  (=-  F.)  officier,  fr.  ML. officiarius,  fr.  L.  officium.  See  prec.  word  and agential  suff.  -er.
26137:Derivative:  officer,  tr.  v. official,  adj.  —  ME.,  fr.  OF.  official  (F.  officiel), fr.  Late  L.  officialis,  ‘pertaining  to  an  office  or service’,  fr.  L.  officium.  See  office  and  adj.  suff. -al.
26140:officiary,  adj.,  pertaining  to,  or  connected  with, the  holding  of  an  office.  —  ML.  officiarius,  fr. L.  officium.  See  office  and  adj.  suff.  -ary. officiate,  intr.  v.,  to  perform  a  duty;  esp.  to  per¬ form  the  duties  of  a  priest.  —  ML.  ojficiat-(um), pp.  stem  of  offtciare,  ‘to  perform  divine  service’, fr.  L.  officium.  See  office  and  verbal  suff.  -ate. officinal,  adj.,  kept  in  stock  by  a  druggist.  —  ML. officinalis,  ‘belonging  to  a  workshop’,  fr.  L. officina,  ‘workshop’,  which  stands  for  *opificina, it.opifex,  gen.  opificis,  ‘workman’.  Seeoffice,  suff. -ine  (representing  L.  -inus)  and  adj.  suff.  -al. officious,  adj.,  1)  friendly,  obliging  (archaic);  2) meddlesome,  interfering;  3)  unofficial,  informal (diplomacy).  —  L.  ojficiosus,  ‘dutiful,  complai¬ sant,  obliging’,  fr.  officium.  See  office  and  -ous. Derivatives:  officious-ly,  adv.,  officious-ness,  n. offing,  n.,  the  distant  part  of  the  sea,  as  far  as  it can  be  seen  from  the  shore.  —  Formed  fr.  off, adv.,  and  subst.  suff.  -ing. offish,  adj.,  inclined  to  be  aloof.  —  Formed  fr. off,  adv.,  and  adj.  suff.  -ish.
26366:fr.  open,  ‘open’.  Cp.  OS.  opandn,  oponon,  ON. opna,  MDu.,  Du.  openen,  OHG.  offanon,  MHG. offenen,  G.  ojfnen,  ‘to  open’,  and  see  open,  adj. open-eyed,  adj.  —  First  used  by  Shakespeare, opera,  n.,  a  drama  sung.  —  It.,  ‘work,  labor, composition’,  fr.  L.  opera,  ‘service,  pains,  work, labor’  (whence  also  OF.  uevre,  oevre,  F.  teuvre, ‘work’),  fr.  opus,  gen.  operis  (see  opus  and  cp. the  second  element  in  maneuver);  introduced into  English  by  the  diarist  John  Evelyn  (1620- 1706).
38001:tactics,  n.,  maneuvering  of  armed  forces.  — ModL.  tactica,  fr.  Gk.  Taxnxa,  ‘tactics’,  neut. pi.  of  TaxTix6t;,  ‘fit  for  ordering  or  ordering; pertaining  to  tactics’,  used  as  a  noun,  fr.TaxT6s, ‘ordered’,  verbal  adj.  of  tAocteiv,  ‘to  put  in order,  arrange’.  See  taxis.
```


## [2026-09-07T20:23:36.583Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON اپرا ===\"; grep -n \"اپرا\\|مانور\\|اپرا,\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head -20",
 "description": "Grep Mo'in for opera/manovr"
}
```


### [2026-09-07T20:23:36.675Z] TOOL RESULT

```
=== MON اپرا ===
MON_part2.txt:114:اپران) ذ کر کرده‌اند ولی امروزه این گیاه را ی 
MON_part2.txt:21515:کر: 0۲ (.) (مس.) آواز دسته جمعی (اپراه 
MON_part2.txt:32159:آفنته و اپران رسم بود که در قفای شخصی 
MON_part2.txt:39366:اپراطوری روم شامل ۰۰۰۰ سرباز بود.) 
MON_part2.txt:43262:مانور: ۲ (.) طر بققه تنظیم عما 
MON_part2.txt:43264:در یک منطقه. ضح. (نظ.) مانور عبارت از 
MON_part2.txt:78638:اپرام. (اتض.) شکسنت: وبرانی: قهدشکی: 
MON_part1.txt:5013:بین دو پرده 5 نماش با اپرا اجرا شود. 
MON_part1.txt:6162:اپرام: 2022 [ع. ۰[ (مص م ۰) استوار کردن» 
MON_part1.txt:6641:اپرا: 02 [- اویرا] (ا.) (نم.) ترکیبی از 
MON_part1.txt:19197:اپراه: [- عراق» معر. بست؛» بایین» ز بر ] 
MON_part1.txt:23019:کوهستان‌های اپران و ترکیه و افغانستان و 
MON_part1.txt:27933:شراب. شراب. اپرانیان: «هر مزد» بهمن» اردیبهشت» شهریور 
MON_part1.txt:91987:اکثر باغ‌های اپران کشت می‌شود. . برگک‌های 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:114:اپران) ذ کر کرده‌اند ولی امروزه این گیاه را ی 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:21515:کر: 0۲ (.) (مس.) آواز دسته جمعی (اپراه 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:32159:آفنته و اپران رسم بود که در قفای شخصی 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:39366:اپراطوری روم شامل ۰۰۰۰ سرباز بود.) 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:43262:مانور: ۲ (.) طر بققه تنظیم عما 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:43264:در یک منطقه. ضح. (نظ.) مانور عبارت از
```


## [2026-09-07T20:23:44.903Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON اپرا ===\"; sed -n '6638,6650p' MON_part1.txt; echo \"=== MON مانور ===\"; sed -n '43255,43275p' MON_part2.txt",
 "description": "Read Mo'in entries for opera and manovr"
}
```


### [2026-09-07T20:23:44.986Z] TOOL RESULT

```
=== MON اپرا ===
اپارتمان: 0 (ا.) ساختمان چند 
طبقه» هر قسمت مجزا از یکك عمارت چند 
طبقه که دارای وسایل کامل است. 
اپرا: 02 [- اویرا] (ا.) (نم.) ترکیبی از 
شعر و موسیقی و نمایش از موضوعات 
حزن آور با خنده آور. 
اپرت: 0 (.) (نسم.) نماش ایرایی 
کوچکی که ارکستر آن آهنگ‌های عامبانه و 
تا ای هیک ان سا 
شته باشد. 
اپشک : ۸05۵1 [- بشکک ] (ا.) شبنم» ژاله. 
اپیون: [- افبون]. (یو.) (.) شبرة 
مخدر و منوم که از پوست خشخاش گیر ند؛ 
=== MON مانور ===

از اسم ( (مشبه‌به) آید بدون اضافه استعمال 
شود سرو مانند؛ و اگر پیش از اسم ات 
نصورت اضافه اقعیال کدن (حر.ریط) 
نظیر» مثل (بصورت اضافه آید.) به مانند: 
مانند» نظیر» شمبه. از قبیل. 

مانور: ۲ (.) طر بققه تنظیم عما 
دستگاه. (نظط.) فن رهبری دسته‌های ت_ 
در یک منطقه. ضح. (نظ.) مانور عبارت از 


۱ ۱ 
این است که در حدود مات محو له کلبه 
وسایل خود را به روی دشمن تمرکز دهند؛ 
ی الامکان از روی غافل‌گیری دشمن و 
تأمین قوای خودی (ن ظامنامه محار ره بباده 
نظام قسمت ۱ص ۱۴۵) (نظ.) تمرین 
عملیات نظامی. 
مانه: (د)م«قد (- مان | (ا.) ائائة خانه» اثاث 
التتت:
```


## [2026-09-07T20:23:54.674Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A7%D9%BE%D8%B1%D8%A7/",
 "prompt": "What does the فرهنگ معین (Mo'in) section say for اپرا — quote the entry including any French/foreign source word given? Also any Dehkhoda note on its origin."
}
```


## [2026-09-07T20:23:55.866Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%85%D8%A7%D9%86%D9%88%D8%B1/",
 "prompt": "What does the فرهنگ معین (Mo'in) section say for مانور — quote the entry including any French source word (manœuvre)? Also any Dehkhoda note on its origin."
}
```


### [2026-09-07T20:24:00.593Z] TOOL RESULT

```
# فرهنگ معین Entry for مانور

According to the **فرهنگ معین** section, the entry states:

> "(نُ وْ ) [ فر. ] (اِ. ) اجرای عملیات جنگی به طور نمایشی و تمرینی"

This translates to: "execution of military operations in a demonstrative and training manner," with the notation "[فر.]" (French origin) and "(اِ.)" indicating it's a foreign loanword.

Regarding the **Dehkhoda dictionary note on origin**: The Dehkhoda section identifies the word as French in origin and defines it as a method for organizing device operations, with specific military applications involving troop leadership and concentration of forces against an enemy.
```


### [2026-09-07T20:24:00.839Z] TOOL RESULT

```
# اپرا (Opera) - Farhang-e Mo'in Entry

According to the **Farhang-e Mo'in** section, the entry reads:

> "(اُ پِ) [فر.] (اِ.) ۱ - نمایشی که همراه با ساز و آواز و شعر باشد. ۲ - محل اجراء این گونه نمایش ها."

This translates to: a performance accompanied by instruments, voice, and poetry; or the venue where such performances are held. The notation "[فر.]" indicates the French origin, while "(اِ.)" denotes the English source word.

**Regarding Dehkhoda origin information:** The webpage does not include a dedicated Dehkhoda dictionary section with etymological notes. The closest historical detail appears in the "دانشنامه عمومی" (General Encyclopedia) section, which notes that the word "اپرا" derives from Latin *opus* (meaning "work"), becoming the plural form used as a singular feminine noun from the 17th century onward to describe performances sung rather than spoken.
```


## [2026-09-07T20:24:12.296Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages,1):\n    if '151' in p and \"m'n\" in p and 'aman' in p:\n        print(\"=== page idx\",i,\"===\")\n        print(p[:1200]); break\nfor i,p in enumerate(pages,1):\n    if '10739' in p:\n        print(\"=== xwp page idx\",i,\"===\")\n        print(p[:400])\n        break\nEOF",
 "description": "Locate SOD pdf pages for entries 151 and 10739"
}
```


### [2026-09-07T20:24:13.624Z] TOOL RESULT

```
=== page idx 72 ===
"kVy


                                                               (fo)hang
       akafc ©f. pp. =»»k>pt>k
       crooked                                                 GMS 634
       BSTBL, Vim. 3, 17, 128                             146 »kwyt-      B                                   j^_f\
133 "k'c'y B                                 "yrtlhh           akuyd ©Parth. >gwxt ©pt. st. -^k'wc-
                                                               OcOhang
    akac(e) (»k»cyy) =»»k>c(h)
    space, void                                                GMS 858; MDii pl91
    BSTBL, Vim. 30; Padm. 25; Dhy. 124, 152, 177,         147 "kwyty      B                          O^jT^jT
      248, 356; TSP 2.585, 16.32; VJ 1233                     akuyde      (*qwytyy) ©pp.
134 »k}c(h) B                                     ^<U*         suspended
    akac (»k>cyy) ©<Skt. akasa         ^»k'c>y                SCE 392; GMS 858; *kwYtu MDii "weight" ?
    space, void                                           148 "qwytyy   M =^ "kwyty
       TSP; VJ; BSTBL, »jk>cw, Dhu. 178; Gersh. Sogd.     149 »kwyc-   B                             ^jT
         Cpds. 1945, 142 i; -yk ?, Dhy. 217
            
=== xwp page idx 504 ===
                                                                                                                     436

     xwgptyk

           BSTii 891.62; STii 5.15; C2, 60V30 -y n pl32;        10734 xwn>k     S                                      jl
             GMS 1336 n 1; MSP bl41, 143
                                                                      xone ^Ywn*^1* xwny
```


## [2026-09-07T20:24:22.024Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (71,72,73,74):\n    p=pages[i-1]\n    print(\"=== pdf idx\",i,\"first 300 ===\")\n    print(p[:300].replace('\\n','|'))\n    print(\"...has 151:\", \"151 \" in p, \"| has ʾmʾn line:\", \"m'n   B\" in p or \"m'n  B\" in p)\nEOF",
 "description": "Find printed page for SOD entry 151"
}
```


### [2026-09-07T20:24:23.261Z] TOOL RESULT

```
=== pdf idx 71 first 300 ===
                                                                                                                ?)k>ptc(h)|||||    (to)bring                                                        indigestion ?|    GMS 603; AVS 139                                                 TSP 8.126||102 "y^k1 
...has 151: False | has ʾmʾn line: False
=== pdf idx 72 first 300 ===
"kVy|||                                                               (fo)hang|       akafc ©f. pp. =»»k>pt>k|       crooked                                                 GMS 634|       BSTBL, Vim. 3, 17, 128                             146 »kwyt-      B                                   j^_f\|133
...has 151: True | has ʾmʾn line: False
=== pdf idx 73 first 300 ===
                                                                                                                 »n>y-|||||160 Mm'ty(y) M                                     <oU7   173 »mty>kh ^ fm>ty>kh|    amate ^"m't'k, »mtyc                                  174 Mmtyc B, M, S                     
...has 151: False | has ʾmʾn line: False
=== pdf idx 74 first 300 ===
                                                                                                           tt»|||||    GMS 569; EGSii 18, 58; VJ; BBB 100; AVS 94                         Aban, eighth month of the year|                                                                       Hen. JRAS 19
...has 151: False | has ʾmʾn line: False
```


## [2026-09-07T20:24:30.269Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nimport re\nfor i in (70,71,72,73):\n    p=pages[i-1]\n    nums=[l.strip() for l in p.split('\\n') if re.fullmatch(r'\\s*\\d{1,3}\\s*',l)]\n    print(\"pdf\",i,\"standalone nums:\",nums[:8])\nEOF",
 "description": "Find standalone page numbers in SOD pages 70-73"
}
```


### [2026-09-07T20:24:31.552Z] TOOL RESULT

```
pdf 70 standalone nums: []
pdf 71 standalone nums: []
pdf 72 standalone nums: ['137']
pdf 73 standalone nums: []
```


## [2026-09-07T20:24:40.412Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nimport re\nfor i in range(74,120):\n    p=pages[i-1]\n    nums=[l.strip() for l in p.split('\\n') if re.fullmatch(r'\\s*\\d{1,3}\\s*',l)]\n    if nums: print(\"pdf\",i,nums[:4])\nEOF",
 "description": "Find printed page anchors in SOD 74-120"
}
```


### [2026-09-07T20:24:41.774Z] TOOL RESULT

```
pdf 76 ['10']
pdf 77 ['11', '634', '299']
pdf 79 ['13', '617']
pdf 82 ['16']
pdf 83 ['427', '129', '433']
pdf 84 ['18']
pdf 85 ['19']
pdf 86 ['20']
pdf 87 ['721']
pdf 89 ['23']
pdf 91 ['25']
pdf 92 ['26']
pdf 93 ['27']
pdf 95 ['29']
pdf 96 ['191']
pdf 97 ['31']
pdf 98 ['32']
pdf 99 ['33']
pdf 101 ['35']
pdf 102 ['36']
pdf 103 ['36']
pdf 104 ['38']
pdf 105 ['39']
pdf 106 ['727']
pdf 108 ['42', '110']
pdf 109 ['43']
pdf 110 ['44']
pdf 111 ['45']
pdf 112 ['46']
pdf 113 ['47']
pdf 114 ['48']
pdf 115 ['49']
pdf 117 ['51', '98']
pdf 119 ['53']
```


## [2026-09-07T20:25:02.387Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT hvapah ===\"; grep -n \"gute  Werke\\|Werke  verrichtend\\|gutes  Werk\" BRT.txt | head; echo \"=== BRT line 30643 ctx ===\"; sed -n '30638,30648p' BRT.txt",
 "description": "Find Bartholomae hvapah entry"
}
```


### [2026-09-07T20:25:02.449Z] TOOL RESULT

```
=== BRT hvapah ===
29556:•  g.  havapacha-  Adj.  (fem.  °Nhä-)  'gute, schöne  Werke  verrichtend,  wohlwirkend': apö    at  yazamaidl    .    .     °par»hä     Y.  ^8.
30647:•  j'i  g-  hv-apah-  i)  (im  gAw.)  n.  'gutes Werk,  Wirken':  ahyd  xsa'i'racä  maifitUca *'pa»hauca ''  tSm  at . .  yatamaidf  "wegen seiner  Herrschgcwalt  und  Grösse  und  seiner schönen  Werke  wollen  wir  ihn  . .  verehren" Y._57.  2.  a)  (im  jAw.)  Adj.  'gute,  schöne Werke  verrichtend,  wohlwirkend',  von AhM. :  azim  . .  dämanam  nipBta  ahmt  'pg (VS,,  nämL  ahura  mazäa)  Yt  70.54;  54;
=== BRT line 30643 ctx ===
e  Formen,  die  leicht  die  Bedeutung ,  j
adam    xs'aya'kiya^    amiy   'jaty   Bh.  c;
des  'selbst;  gewinnen;  sie   stehen  l)  wenn    ^'  '^^^\^l;  ^J^J  vertritt  f;    aber  die  Lesung auf  dem  Wort  besonderer  Nachdruck  hegt,      a^j.  (oder  V.")  -  Hbm.  iFAm.  d'.  46,  Justi namentlich  bei  Gegenüberstellung;  2)  von     GIrPh.  3.  417  -  '"»■le  "cl»  f«r  umulässig;    a. einer  relativisch  angeschlossenen  nominalen!     BB-  'J-  7°,  IF-  ^o.  190,  KZ.  j/.  542. Ergäniung;  l)Dax,-Ab\.  Avavi!ya'''i  a)  als  •    p.    ''uvajiya-    Adj.   'susisch,    Susier":
dby  Google
i847
hvapah-
1  a^'int^  nStna"    •fiyJ'  Bh.4.  i; ''"5.  i'*; '
—  'ßyä  Aami^'^iyä  abava"  Bh. /.  16;  2.4. 1
Ableit.  aus  ^ujjaja-.  —  >)  NA.  bietet  ßlsch- lich  -yä,  NP.;  s.  'ava-,  Sp.  165  u.  '
•  j'i  g-  hv-apah-  i)  (im  gAw.)  n.  'gutes Werk,  Wirken':  ahyd  xsa'i'racä  maifitUca *'pa»hauca ''  tSm  at . .  yatamaidf  "wegen seiner  Herrschgcwalt  und  Grösse  und  seiner schönen  Werke  wollen  wir  ihn  . .  verehren" Y._57.  2.  a)  (im  jAw.)  Adj.  'gute,  schöne Werke  verrichtend,  wohlwirkend',  von AhM. :  azim  . .  dämanam  nipBta  ahmt  'pg (VS,,  nämL  ahura  mazäa)  Yt  70.54;  54;
—  vlspe  tl  ahurS  matdä^'^  'ps  .  .  dätnan  , Y.yi.io;  —  yahmya  ahurS  matdä  pS\ (NSm.)^'  mvai%ayai\t.S.Z$.
```


## [2026-09-07T20:25:04.863Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD ome/am ===\"; grep -n \"^ome\\|^om-\\|^am-\\|Pok. omə\\|Pok. om\" AHD_watkins1985.txt | head; echo \"=== KLN often ===\"; grep -n \"often,  adv\\|oft,  adv\\|often, adv\" KLN_1966.txt | head; echo \"=== SKT often ===\"; grep -n -i \"^often\\|OFTEN\\|oft, often\" SKT.txt | head",
 "description": "Grep AHD for om- root, Klein/Skeat for often"
}
```


### [2026-09-07T20:25:04.954Z] TOOL RESULT

```
=== AHD ome/am ===
800:om-. Raw. Possibly (but doubtful both in form and meaning) Latin amdrus, bitter-tasting (> Italian maras- ca, bitter, bitter cherry): AMARELLE, AMARETTO, MARAS- CA, (MARASCHINO), MORELLO. [Pok. om- 777.]
802:omeso-. Also omso-. Shoulder. 1. Form *omso- in Ger- manic *amsa- in Old Norse dss, a (mountain) ridge: os*. 2. Form *omeso- in Latin humerus, shoulder: HUMERUS. 3. Lengthened-grade form *dmso- in Greek 6mos, shoul- der: ACROMION. [Pok. om(e)so-s 778.]
=== KLN often ===
2329:alodial,  alodium,  n.  —  See  allodial,  allodium, aloe,  n.  —  L.  aloe,  fr.  Gk.  aX6r),  ‘aloe’,  prob. borrowed  fr.  Heb.  ahaltm,  ahaldth  (pi.),  which are  perhaps  borrowed  fr.  OI.  agaruh,  aguruh, ‘aloewood’,  these  latter  being  prob.  of  Dravid- ian  origin.  Cp.  agalloch. aloetic,  adj.  containing,  or  of  the  nature  of,  aloes ; n.,  an  aloetic  medicine.  —  Formed  with  suff. -etic  fr.  Gk.  aXot],  ‘aloe’.  See  aloe, aloft,  adv.  —  ON.  a  lopt,  ‘in  the  air’,  whence  arose the  meaning  ‘on  high’.  See  a-,  ‘on’,  and  loft, aloin,  n.,  a  bitter  crystalline  substance  (chem.)  — Formed  fr.  aloe  with  chem.  suff.  -in;  so  called because  it  is  obtained  from  the  aloe, aloisiite,  n.,  a  hydrous  subsilicate  of  calcium, ferrum,  magnesium  and  sodium  (mineral.)  , Named  after  Prince  Luigi  (Latinized  into  Aloi- sius)  Amedeo  of  Savoy,  Duke  of  the  Abruzzi. For  the  ending  see  subst.  suff.  -ite. alone,  adj.  —  ME.  al  one ,  ‘all  alone  ,  fr.  al,  all , and  one,  fr.  OE.  an,  ‘one,  alone  .  Cp.  Du.  alleen, MHG.  al-ein,  al-eine,  G.  allein,  ‘alone’,  and  see all  and  one.  Cp.  also  lone, along,  adv.  and  prep.  —  ME.  anlong,  along,  fr.  OE. andlang ,  which  is  compounded  of  and-,  ‘against’, and  lang,  ‘long’.  The  first  element  is  cogn.  with Gk.  avxt,  ‘against’,  L.  ante,  ‘before’ ;  see  ante-, anti-.  For  the  second  element  see  long,  adj. aloof,  adv.  —  Originally  a  nautical  term  formed on  the  analogy  of  Du.  te  loef,  ‘to  windward  . See  loof,  luff.
26144:oft,  adv.,  often  ( archaic  or  poet.)  —  ME.,  fr.  OE. oft,  rel.  to  OS.  oft,  ofto,  OFris.  ofra,  Dan.  ofte, Swed.  ofta,  OHG.  ofto,  MHG.  ofte,  oft,  G.  oft, ON.  opt,  Goth,  ufta,  ‘often’ ;  of  uncertain  origin, often,  adv.  —  ME.  ofte,  often,  extended  fr.  oft. See  oft.
35807:soft,  adj.  • —  ME.  so  fie,  adj.  and  adv.,  fr.  OE. softe,  orig.  an  adv.  standing  in  gradational  rela¬ tionship  to  the  adj.  sefte,  ‘easy,  mild,  comfort¬ able,  gentle’;  rel.  to  OS.  sdfti  (adj.),  safto  (adv.), OHG.  semfti  (adj.),  samfto  (adv.),  MHG. senfte  (adj.),  sanfte  (adv.),  G.  sanft  (adj.  and adv.),  MDu.  sachte,  Du.  zacht  (adj.  and  adv.), G.  sacht  (adj.  and  adv.)  and  prob.  also  to  Goth. samjan,  ‘to  please’,  ON.  semja,  ‘to  shape,  com¬ pose,  arrange;  to  settle,  make  peace’. Derivatives:  soft,  adv.,  n.  and  interj.,  soft-en,  tr. and  intr.  v.,  soft-en-er,  n,,  soft-en-ing ,  n.,  soft- ish,  adj.,  soft-ling,  n.  and  adj.,  soft-ly,  adv.,  soft¬ ness,  n.
=== SKT often ===
2:It  has  survived  long  enough  for  the  copyright  to  expire  and  the  book  to  enter  the  public  domain.  A  public  domain  book  is  one  that  was  never  subject to  copyright  or  whose  legal  copyright  term  has  expired.  Whether  a  book  is  in  the  public  domain  may  vary  country  to  country.  Public  domain  books are  our  gateways  to  the  past,  representing  a  wealth  of  history,  culture  and  knowledge  that's  often  difficult  to  discover.
59:gwd  against  becoming  obscure.  In  my  opinion,  the  habit,  frequently adopted,  of  citing  supposed  cognate  words  (often  misspelt)  wifhcmt j^wy  wla/  t/uir  meanings  art,  is  a  very  bad  one,  and  leads  to  guess- il^  and  vagueness.  It  is,  accordingly,  to  be  understood  that,  when  I do  DOC  give  the  meaning  of  cognate  words,  it  is  because  their  sense a^Teeft  «ith  that  of  die  English  word  so  nearly  as  to  prevent  ambiguity. Tbos  tmder  bik,  which  is  derived  from  the  A.  S.  bitan^  to  bite,  I  cite ihr  ri..P....  Icelandic,  Swedish,  Danish,  and  German  forms  without ci  because  ihey  all  mean  precisely  the  same  thing;  but  the
66:There  is  one  point  to  which  I  wish  to  draw  especial  attention.  Bf the  advice  of  a  friend,  I  procured  a  copy  of  a  Dictionary  of  English Etymology  by  the  Rev.  J.  Oswald,  written  on  an  unusual  but  excellent plan.  The  author  airanges  all  the  derivatives  of  the  Latin  cedtn under  the  heading  of  the  Latin  cedOy  so  that  words  such  as  acctdt^ concede^  recede^  succeed,  are  all  presented  to  the  eye  at  a  glance.  The advantage  of  such  an  arrangement  is  obvious,  and  I  at  once  de- termined to  adopt  it,  merely  substituting  the  representative  English word  cede  for  the  Latin  cedo,  and  so  in  other  cases.  At  the  same time,  I  adopted  two  very  considerable  improvements :  (i)  the  retention of  the  alphabetical  order  for  the  derived  words  accedcy  concede^  ftc^ with  a  cross-reference;  and  (a)  the  extension  of  the  principle  to words  of  English  and  Scandinavian  origin.  Mr.  Oswald  gives  the words  only  under  the  primary  form,  which  is  a  great  inconvenience, seeing  that  this  is  often  precisely  what  one  does  not  know ;  and,  yoA for  want  of  the  cross-reference,  he  omits  the  derivative  anctsler altogether.  At  the  same  time  I  have  found  his  book  very  useful,  as far  as  relates  to  that  part  of  our  language  which  is  of  classical  origin. With  respect  to  words  of  Teutonic  origin  it  is  practically  valueless; thus  the  only  word  given  under  W  is  the  word  wonder.
70:ANGLO-SAXON.  The  most  usual  vowel-change  is  that  produced by  the  occurrence  of  an  i  (which  very  often  disappears  by  a  subsequeitf contraction  of  the  word)  in  the  following  syllable.    Owing  to  thii,  we
75:Moreover,  6ubs'.antives  and  secondary  verbs  are  often  formed  from fc*wiwm  in  the  past  tense  singular,  past  tense  plural,  or  past  participle of* nrwig  verb,  rather  than  from  the  infinitive  mood.  Thus  dafidznd ^vt  from  the  base  aeen  in  the  A.  S.  imnd,  pL  L  of  bindan,  to  bind  ; ^huKhmdlt  is  derived  from  that  wliich  appears  in  the  pp.  bund-cn,
206:Notes  at  the  end  of  an  article  are  marked  off  by  beginning the  symbol  V.  XIV,  XV,  XVI,  mean  that  the  word  was  introdc* in  the  14th,  15th,  or  i6th  century,  respectively.  Hyphens  are introduced  to  shew  the  eiymological  division  of  a  word.  Thus,  im( Ccdit  the  word  concede  is  derived  from  Lat.  con-ccdcre ;  meaning concedcrt  can  be  resolved  into  con-  and  cedere.  This  etymologic division  is  often  very  different  from  that  usually  adopted  in  prinl books  when  words  have  to  be  divided;  thus,  capacious  can  only divided}  ctymologically,  as  cap-ac-i-out^  because  cap-  is  the  r< syllable.
373:Admiral.  (F.-Arab.)  M.E. more  often  amiraLm^O.  F.  amiral, also  amirt\  cf.  Low  L.  admu prince,  chief.* Arab,  amlr^  a  pri Elmir.  The  suffix  is  due  to  Arab.] amir-ai-baJir,  pnncc  of  ihc  sea.
694:Anger.  (Scand.)  M.E.  artnr^  often with  the  sense  of  vexation,  trouble,  •IceL OHgr^  grief;  Uan.  an^tr,  Swed  dw^r,  re- gret. +  L.  a"j,yr,  a  struiiglini*.  an(;uii>h. (VAGH,  A^'GH,l
1094:Atlas.  (Gk.)  Named  afler  Atlns,  the demi-god  who  was  said  to  bear  the  world on  his  shDulders ;  his  figure  used  often  lo appear  on  the  title-page  of  atlases.  — Gk. ■'AtAoj  Cficn.  'ArAo»'Tiit>,  prob.  "the  sus- tainer'  or  l»earer,  from  ^  TAL,  to  bear.
1228:Away.     (E.)       For    *«    way, now  often  used  as  if  it  meant  ojf"  (01 the  way.      A.S.  enw,^,  away.     See  Wiflr. '
```


## [2026-09-07T20:25:33.920Z] TOOL CALL #64: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%83ep-",
 "prompt": "Does this page exist? Give the reconstruction, its meaning, and the derived terms/descendants (Latin opus, Sanskrit ápas-, Avestan) it lists."
}
```


## [2026-09-07T20:25:34.652Z] TOOL CALL #65: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/H%C3%A1mas",
 "prompt": "Does this page exist? If so, give the reconstruction, meaning, PIE source and descendants (Sanskrit áma-, Avestan ama-)."
}
```


### [2026-09-07T20:25:36.567Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-07T20:25:39.495Z] TOOL RESULT

```
# Proto-Indo-European *h₃ep- Root

Yes, this page exists. Here's the information:

**Reconstruction:** *h₃ep-

**Meanings:**
1. "to work, toil, make"
2. "ability, force"

**Key Derived Terms/Descendants:**

- **Latin:** *ops* (leading to *cōpia*) and *omnis*
- **Sanskrit:** अप्‍ (áp) and अप्नस्‍ (ápnas)
- **Hittite:** ḫa-ap-pí-na-an-za and ḫā-ap-par
- **Avestan:** represented through Proto-Indo-Iranian *Háp*
- **Old Latin:** *opulentus*

The page documents approximately 56 derived terms across multiple Indo-European language families, with detailed etymological tracking through intermediate proto-languages like Proto-Italic, Proto-Germanic, and Proto-Anatolian.
```


## [2026-09-07T20:25:48.148Z] TOOL CALL #66: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E0%A4%85%E0%A4%AE",
 "prompt": "Give the Sanskrit entry for अम (áma): its meanings and its etymology, including any PIE/Proto-Indo-Iranian reconstruction and cognates (Avestan ama, Greek)."
}
```


## [2026-09-07T20:25:50.815Z] TOOL CALL #67: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%AE%D9%88%D8%A8' --note 'page 374, root Op, Persian xub: Wiktionary etymology MP xwb < PIr *HhuHapah < PIE *h1su- + *h3epos' 2>&1 | tail -3",
 "description": "Archive Wiktionary xub"
}
```


### [2026-09-07T20:25:53.972Z] TOOL RESULT

```
# Sanskrit Entry for अम (ama)

## Meanings

According to the Wiktionary entry, अम functions as both an adjective and noun:

**As an adjective:** "unripe"

**As a noun, the term denotes:**
1. Going
2. "pressure; weight; strength; power"
3. Fright; terror
4. Sickness, disease
5. A servant, follower, or attendant
6. Vital air, life-wind
7. This self
8. Unmeasured state

## Etymology & Cognates

The entry explicitly states: "(This etymology is missing or incomplete. Please add to it, or discuss it at the Etymology scriptorium.)"

The page provides **no information** regarding Proto-Indo-European or Proto-Indo-Iranian reconstructions, nor does it document cognates in Avestan or Greek as your question suggests.

## Source

The definitions derive from Vaman Shivram Apte's *The practical Sanskrit-English dictionary* (1890), though the entry notes a cleanup request regarding "the quality of Apte is disastrous here."
```


### [2026-09-07T20:25:55.665Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/1bdf23869ed832b0.txt
```


## [2026-09-07T20:26:07.574Z] TOOL CALL #68: Bash

```json
{
 "command": "for u in \\\n 'https://www.etymonline.com/word/often|page 374, root Op node 4-5: often/oft from PGmc *ufta, unknown origin, perhaps PIE *upo - not *op-' \\\n 'https://www.etymonline.com/word/option|page 374, root Op node 6-7: option from L. optio < optare, PIE *op- (2) to choose (de Vaan *h3epeie-)' \\\n 'https://en.wikipedia.org/wiki/Arsames|page 374, root Ome node 2: Old Persian Arsama \"having a hero'\"'\"'s strength\"' \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%83ep-|page 374, root Op: PIE *h3ep- to work, toil; ability, force' \\\n 'https://en.wiktionary.org/wiki/%E0%A4%85%E0%A4%AE|page 374, root Ome node 1: Sanskrit ama \"pressure, strength, power\"' \\\n 'https://abadis.ir/fatofa/%D8%A7%D9%BE%D8%B1%D8%A7/|page 374, root Op node 9: Mo'\"'\"'in marks اپرا as [فر.] French loan' \\\n 'https://abadis.ir/fatofa/%D9%85%D8%A7%D9%86%D9%88%D8%B1/|page 374, root Op node 9: Mo'\"'\"'in marks مانور as [فر.] French loan' \\\n ; do url=\"${u%%|*}\"; note=\"${u#*|}\"; python3 tools/fetch_source.py \"$url\" --note \"$note\" 2>&1 | tail -1; done",
 "description": "Archive web sources used"
}
```


### [2026-09-07T20:26:13.583Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/ec3b7eda919347ed.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/033f591bdbf8dce6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e3882bc01aaf291e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2ae141547a09dc4e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8b7dd790655ec2da.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c118eb19ce837f32.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b297a9f7c757dba0.txt
```


## [2026-09-07T20:26:17.199Z] TOOL CALL #69: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/page-316.json'));print(d['pdf_page'],d['book_page'],d['verified_by'],d['verified_on']);e=d['entries'][0];print(list(e.keys()));print(list(e['nodes'][0].keys()))\"",
 "description": "Check existing verification file shape"
}
```


### [2026-09-07T20:26:18.495Z] TOOL RESULT

```
316 286 claude-opus-5 2026-09-06
['entry', 'root', 'verdict', 'modern_form', 'note', 'note_fa', 'sources', 'ref_check', 'consulted', 'nodes']
['id', 'lang', 'words', 'verdict', 'derivation', 'derivation_fa', 'sources', 'ref_check', 'consulted']
```


## [2026-09-07T20:27:22.860Z] TOOL CALL #70: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/page-316.json'))\nfor e in d['entries']:\n  for n in e['nodes']:\n    if not n['ref_check'] or n['ref_check'][0].get('ref') in (None,'None','','-'):\n      print(json.dumps(n['ref_check'],ensure_ascii=False)); break\n\" ; python3 -c \"\nimport json;d=json.load(open('data/verification/page-316.json'))\nprint(json.dumps(d['entries'][0]['nodes'][-1],ensure_ascii=False)[:1200])\"",
 "description": "Check refs=None convention"
}
```


### [2026-09-07T20:27:24.439Z] TOOL RESULT

```
[{"ref": "None", "status": "not_checked", "note": "Nourai gives no reference for this node; checked against Etymonline, Klein and Skeat instead."}]
{"id": 11, "lang": "English", "words": "metro, metropolitan", "verdict": "confirmed", "derivation": "metropolitan (mid-14c.) < Late L. mētropolitānus < Gk. mētropolītēs, from mētrópolis 'mother city' (mḗtēr + pólis); it entered English first as an ecclesiastical title, 'a bishop having general superintendency over other bishops of his province', and only later took the secular sense. metro is a 20th-c. clipping of French (chemin de fer) métropolitain, the Paris underground railway (1900), so it reaches English through French but from the same Greek compound. The chain root → Greek → English is therefore right.", "derivation_fa": "metropolitan در سدهٔ چهاردهم میلادی از لاتین متأخر mētropolitānus و آن از یونانی mētrópolis «شهر مادر» (mḗtēr + pólis) وارد انگلیسی شده، نخست به معنای عنوان کلیسایی (متروپولیتان = اسقف اعزم) و سپس معنای غیردینی. metro کوتاه‌شدهٔ فرانسوی métropolitain (راه‌آهن زیرزمینی پاریس، ۱۹۰۰) است. پس پیکان ریشه ← یونانی ← انگلیسی درست است.", "sources": ["https://www.etymonline.com/word/metropolis"], "ref_check": [{"ref": "None", "status": "not_checked", "note": "no reference given by Nourai; checked against Etymonline and Klein."}], "consulted": [{"
```


## [2026-09-07T20:27:24.494Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KNT Arsama ===\"; grep -n -i \"arsama\\|aršāma\\|Arsames\" KNT.txt | head; echo \"=== ARY khub ===\"; grep -n \"خوب\" incoming/ARY/ARY_pages.txt | head -5",
 "description": "Grep Kent and Aryanpur"
}
```


### [2026-09-07T20:27:24.564Z] TOOL RESULT

```
=== KNT Arsama ===
305:First symbol Second Symbol Am = Ariaramnes As = Arsames B = Behistan
471:Tt is uncertain also when this Old Persian system of writing was invented. The extant in- scriptions are largely those of Darius I and of Xerxes, and it is tempting to ascribe the inven- tion to the orders of Darius when he wished to record the events of his accession, on the Rock of Behistan; but there are three inscriptions of Cyrus, as well as one each purporting to be of Ariaramnes and of Arsames. These last two may have been set up as labels to small monuments or other objects of a later period;? the orthography
472:1 For a critique of these theories, see Wb. KIA 1у-1х. 2 Ariaramnes was great-uncle of Cyrus and great-grand- father of Darius 1; Arsames was son of Áriaramnes and grandfather of Darius. Note that the two inscriptions are both on gold tablets and found at or near Ecbatana
477:(Hamadan) in Media; though the two kings are spoken of in them only as ‘king in Parsa = Persis’, which was quite distinct from Media. They may have been set up in the time of Artaxerxes П as part of an anti-Cyrus propaganda, since Cyrus the Great had dethroned Arsames, and Cyrus the Younger came very near de- feating and killing Artaxerxes II at Cunaxa (cf. JAOS 66.206-12). The gold tablet A?Hc may have been a third in the same series; all three are in Old Persian only. *Cf. especially Schaeder, SbPAW 1931.636-42. 4 They are hardly to be ascribed to Cyrus the Younger, despite Wb. ZDMG 48.653-65 (cf. also KIA lxvii-bax) on CMa, which alone was known to him; for the opposing view, cf. Hz. Klio 8.1 ff. * Though perhaps not much used by him. The other three known inscriptions of Cyrus the Great are in Akkadian; but Strabo 15.3.7-8 (page 730), on the authority of Onesicritus, states that the tomb of Cyrus at Pasargadae bore at least two inscriptions, one being bilingual, Greek and Persian. We need attach no importance to the identification of the languages by Onesicritus, but the account indicates that Cyrus had inscriptions engraved in more than one language; in which case it is unlikely that his own vernacular was omitted. Cf. JAOS 66.206-12; but also Hinz, ZDMG 96.343-9.
563:! Greek єр is not conclusive evidence for 7, despite xépoa = karía- and Zytphs = Bardiya, both with у ($80); ef. "Гутафёриує = Vitdafarnd, with -ar-, and 'Apseáum = Aršāma and 'Apratiptys = ArtaxSacd, both with r by the Elam. testimony, despite Gr. ар-. Several Greek transliterations of place-names have ap for Persian ar: Tapa = Paréava, Xayapría = Asagaria, etc.
1438:Saka-, Sug(u)da-, Nisdya-, si*kabru-, and the 3 dubious siyamam. 3 5117. рів. f from pIE s after certain sounds 1 (8115) remained unchanged in OP: у ОР тав: Ма- ‘greatest’, Av. masisla-, Gk. шікито 5 "longest". : OP fràisayam ‘I sent’, Skt. ejayat? ‘he brings’, OP uška- ‘dry’, Av. huska-, Lith. satisa-s. OP gausa- ‘ear’, Skt. ghóga- ‘noise’. 4 OP adarínaus ‘he dared’, Skt. dhysnéti ‘he dares’. 4 OP aría- ‘male’ in ArSama- ‘Arsames’, Skt. 4 rsa-bhd- ‘bull’. 4 pIE *sed-as- in ОР Лай ‘seat’, cf. СК. &os (from -$ pIE *sedos). 4 pIE *e-st-sfe-to, OP ачЧаіа ‘he stood’, cf. Gk. : israrat ‘he stands’ (from *sestatat). 4 pIE *rsti-, OP nom. arštiš, Skt. rstf-s (cf. $115). 4 OP nom. tani ‘body’, Skt. tani-s. 4 For ks and other clusters giving zš, see $102; 4 for kn and gn giving initial тп and medial im, 4 $06; for -Sc- as a sandhi product, $105; for pAr. 4 & giving OP Sy, $104; for pAr. t giving OP y 4 $80; for pAr. én giving OP $n, $82. 1 The verbal prefix ni- affects an initial s of the 4 verbal root; thus ni-$d- from ni- + stä- and 4
1914:b. Genitive: Arta-xéaga- ‘Having a kingdom of justice’; Aršāma- (from *aría-ama-) ‘Having the might of a hero’; Haxd-manis- ‘Having the mind of a friend’; Garma-pada- ‘(Month) having the place of heat’; Asa-garta- (Тапа) having caves of stone’. :
2967:$290. COORDINATION AND SUBORDINATION. Not infrequently the OP texts express by coordinate clauses ideas which are logically subordinate; the result is a series of short sentences, syntactically simple, independent of each other grammatically, but logically and semantically connected. Thus, for example, DB 446-8 vafnà Auramazdaha api- mary aniyascry vasiy astiy kartam ava ahydya diptya пазу nipistam avahyarddiy naty nipistam таша ... ‘by the favor of Ahuramazda indeed, much other (work) was done by me; that (work) is not inscribed in this inscription; for the following reason it is not inscribed, lest . . .’; this could have been expressed in one complex sentence somewhat as follows: ‘much other work was done by me, which has not been inscribed in this inscription for the following reason, lest ...’. Another excellent example is found in XPf 20-25 шій Vistáspa иа Arfüma ubā ajivatam асту Auramazdim арабӣ Ката aha Dérayavaum hya manā рий avam asdyabiyam akunaus ahydyd бата 'Hystaspes and Arsames both were living, then—unto Ahu- ramazda thus was the desire—Darius who (was) my father, him he made king in this land’; in the parallel passage DSf 13-5, yadzy ‘when’ is used . instead of асїу ‘then’, and instead of Auramazdém avatà Ката aha (found also XPf 29f, DSf 15f), we find in DNa 37f (and elsewhere) yada mim ата Gha ‘as unto me was the desire’. In dating sen- tences we regularly have expressions of the type seen in DB 1.42 Garmapadahya máhyà I X rauca- bi$ fakaia aha агава zšaçam agarbdyatd ‘of the month Garmapada, 9 days had passed—then he seized the kingship’; only in DB 1.38 the date is followed by a subordinated clause, yadiy udapa- tala ‘when he rose up in rebellion’. The same phenomenon is probably present where conjunc- tions are omitted as introductory to subordinate clauses, such as the absence of tya in РМ 20 and 50 (cf. DNa 39).
3046:$308. Тнк Position or Apposittves. Apposi- tives, whether nouns or adjectives, usually follow! that to which they are appositive; but the position is otherwise free. Appositives to a subject implied in the verbal ending may stand in any place; cf. DNb 41-5. Chiasmus sometimes is the result of stylistic considerations: XPh 47f уйа ahaniy Jiwa щй marta ariàvà ahaniy ‘happy may I be while living, and when dead blessed may I be'; DSf 12f hya mand pità Vištāspa ша Arama hya mand niydka ‘my father Hystaspes and Arsames my grandfather’, in which the appositive precedes in one instance,
3081:8312. Tue Namina Punaszs. It is a feature of OP style, that at the first mention of a person (other than of the ruling king) or of a place (other than of а governmental province) the name of that person or place should be followed by пата or nàmà; there are a few exceptions, as in DSf 12f, where the names of Arsames and Нуѕђаврез lack лата, and in DB 3.11 and 5.4, where the province- names Marguí and (ја are accompanied by nama. These phrases are always! in the nomina- tive case, whether or not that is their funetion in the sentence; they are usually followed by a re- sumptive pronoun or adverb. The form пата is used unless there is a following generic term of feminine gender (dahydus, didd), when лйт@ is
=== ARY khub ===
323:کاوشهای باستانشناسی و بررسی گنجانه‌های سفالی نیز می‌توانندگواه خوبی باشند. در اوکراین
994:(حتی انسانهای خوب) پس از مرگك جایی سرد و تاریکك است که در آن نه شادی وجود دارد نه امید.
995:تصویر دنیای پس از مرگك که در آثار هومر منعکس شده نمونه‌ی خوبی است: سرزمین مردگان در
1052:ویژگی‌های ابر انسانی ضامن خوبی محصول و زایندگی دام‌ها و پر ماهی بودن رودها و فراوانی
1067:نمونه‌ی خوبی از این مخاطرات است). لذا رسم بر این بود که مردان و پسران را بکشند و زن‌ها و
```


## [2026-09-07T20:27:37.754Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== BQT v2 khub ==\"; grep -n \"خوب ـ\\|خوب -\\|خوب:\" BQT_v2.txt BQT_v2_pages.txt 2>/dev/null | head -6; echo \"== MON khub headword ==\"; grep -n \"^خوب\\|خوب: \\[\" MON_part1.txt MON_part2.txt | head -6; echo \"== ARY headword ==\"; grep -n \"^ *خوب\" incoming/ARY/ARY_pages.txt | head -5",
 "description": "Grep BQT/MON/ARY for khub headword"
}
```


### [2026-09-07T20:27:37.861Z] TOOL RESULT

```
== BQT v2 khub ==
BQT_v2.txt:16645:حن امت که خوب - وخوبی - و خوشدلی - 
== MON khub headword ==
MON_part2.txt:7037:خوب» سند‌یده. 
MON_part2.txt:8343:خوبی برای حرارت و الکتر یسته هستند و 
MON_part2.txt:11318:خوب. مورد قبول واقع شدن (قرار گرفتن) 
MON_part2.txt:14336:خوب نویسد. قلم جعد کردن: (کد.) نوشتن؛ 
MON_part2.txt:21321:خوبی و نظطم و ترتیب اداره کند؛ خانه‌دار. 
MON_part2.txt:23203:خوب جلوه کردن. 
== ARY headword ==
1106:خوبی از اینگونه لبیدهاست. گستردگی و تداوم حرفه‌ی لبیدی در میان ملت‌های هند و اروپایی
7360:خوب ۲۵۱
```


## [2026-09-07T20:27:43.382Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '7350,7370p' incoming/ARY/ARY_pages.txt; echo \"=== ARY latin index hu ===\"; grep -n \"^HU\\|hu-apah\\|HVAPAH\\|SVAPAS\" incoming/ARY/ARY_latin_index_pages.txt | head",
 "description": "Read Aryanpur khub entry area"
}
```


### [2026-09-07T20:27:43.449Z] TOOL RESULT

```
کردی (1/821577): هلال2 ,103 رومانی (42فلان۸): 508۸
بلوچی (/6ل۵۸): 0۷28 ,0۷۸11۵8 گونبکه (0077712): ۸
افنانی (پشتر) (/4۳0۸۷): ۰ 301 ,161108 ایسلندی کهن ((10۸۵ م5 02+
تخاری ۸ (۸ ((ل70227۸): 3 اند
تخاری 2 (8 [ل703۸2): ق ان فریزی کهن (۷لفاکل۲۴ ۰:00 :5۷788788
سانسکریت (84(/8877): 5۸ آلمانی کهن (08701۵(7 210 012):
ارمنی (/۸74480014): 01 ند رید
یونانی 08650): 10 آلمانی ((14ل057): ادا اند رنه هن
[pdf page 250]
۹
خوب ۲۵۱
انگلیسی کهن (577لا8070 صاه): َ لیترانی (77704۸/4/۷): 889888 ,558170
رل اب ا اد رین پروسی کهن (9514۸ن۳# صا0): 8۷788780
انگلیسی (84ا6(/07): ان ایرلندی کهن (ل#کلقا صا0): 3 زان
دانمارکی (0۸(7/877): 0 ولزی (77ما): مان ‎٩‏ ادن
سرئدی (8(77:0]577). اد بان ان
نروژی (0۲/014(۷/): لد نان پسگشت‌ها تردن ۲
هلندی (/00767): 2 3
اسلاوی کهن (۲/۳اشا؟ #67نابل ص1): 41 (818783) :832
5878 43 دنا دار
لهستانی (0۵/374): ه50878 3 (818783) :0/28 24۸
=== ARY latin index hu ===
2887:HUWANTES HITTITE) <a ‘WIND (DUTCH) «gala
3860:HULULER, (LITHUANIAN) 32) BUHO SPANISH) gill
5074:HUN, HUNI ARMENIAN) ga} (OLD PERSIAN) gosh gs),
5111:HUPATI ASIOVAK) 1 ,L-1
7089:HUN AGAULISH) JS SOMMEIL (FRENCH) 4313
7090:HUN WELSH) 315 SUERO (SPANISH) plibyst
7091:HUN, BUNI ABRETON) 6.3. SOMNO SUTALIAN) gli!
9918:HUNSL GOTHIC) S3 SPENTA-, SPANAH, SPANYAH
10428:HUNDS GOTHIC) $3 SPA AVESTAN) .glias!
10430:HUNDR *SAKA, *SPAKA, SPAXA
```


## [2026-09-07T20:27:53.772Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '7371,7420p' incoming/ARY/ARY_pages.txt",
 "description": "Read ARY page 251 content"
}
```


### [2026-09-07T20:27:53.825Z] TOOL RESULT

```
روسی (951۸1نا): 8078 107 ناه
چکد (250(4)): ادن 0 (818783) 010/5
صربی (55۷81400): 572 5 (818733) :57
برهمی (80772(4147): ات اند نم برهان قاطع + ۷۱۸۴ ۰
اسلوا ۱ کی (51.0۵): خ5۳878
بادداشت,
چم این واژه در زبان یرنانی: دختر ۰
اوستایی (4ل۸۲87/4): 1318۸۸ +نا چکث (7ل250): 1 و708۸
پارسی باستان ((۴8/814 صان): س اسلراکی 0(/0/-5): 2
اه , پهلری (1مابقم): لیتوانی (490(فنا777/: 917-03818 تاو
او بان نایده 100 ,8 ت13 ایرلندی کهن (بلدلم/ صله): «لآو ,804
اففانی (پکس) (/0۷ ی , 28 گالی (3#لاتامه): 510۰
سانسکریت (54(7۶87): 817۷۸0108 دنا ولزی (لکلق): 1
پونانی (025): 8 ,13 برتونی (/87570): 11
لاتین (۸7ل): راد هتیت (7177775): 8تا۸9
ایسلندی کهن (7ل010۸7۵/یه صزمم: -تآو
اسلاوی کهن (ع۲1ما؟ ل#ناتق طان):
-850
[pdf page 251]
۲ | خود خویش» خویشتن
پسگشت‌ها هید ۲ 6 (0000) :2/5
کر رس برهان اطع رن ۸۴
235 نققالمانما05 9
اد
یادداشت:
۱ بازگشت به: هو :
۲ این واجريشه بیشتر بعنوان پیشوند بکار رفته است.
اوستایی (4872): فریزی کهن (۶78740 5817۸:)010 ,85817
۷۸707 ,13۸۸ آلمانی کهن (/(022214 1/04 صاه):
۱ پارسی باستان (/۶5781۸ صا0): 3 ,558 ,551230
۸1 ,2۷۸3 آلمانی (08#۵1۵4): 57 ,8812357
پهلری (۲7اتنهه): انگلیسی کهن (بلقل8(۷۵ صان): ۰
۸7 ,۷۷۸3 ,32۳۸3 . 2 ,551۵ ,ت55
کردی (08213[7): 310 انگلیسی (لل5لا6(/0): َ 557
افغانی (پشت) (4701/071):-131170 +107100 دانمارکی (0۸(/18[4): 2و
سانسکریت (54(/97007): س84 سوئدی (8۲50[54): ا۷تقزه
ارمنی (۸/8//1۵0۷): نروژی (۵فا۸/0۴0): 50
۸ 13-2 ,1118 هلندی (4ل0776): 2
برنانی (072280): + بش8 بظ اسلاوی کهن (۲70ا؟ 6 #تاتت صام):
لانین (4770): -886 رقتاتا5 ودنا5 داتا5 57017
گوتیک (0071/0: 816 ,5778 ,5118۸ لیترانی (۷لفاانهنات رم 58۷88 ,5۸88
ایسلندی کهن (42 90721۸4 صان): پروسی کهن ((851-۲# 0۱0): 8۸59
۲8۸3 آلبانی (۷لماانمقتم: ۷۳78
ساکسونی کهن (/(542:0 صا0):
0 و,قنل8 ۰ *
اا
[pdf page 252]
خورء خورشید» هور / ۲۵۳
پسگشت‌ها نخش یت دید ید
۶08۵0 48 هتم هه وهای
```


## [2026-09-07T20:34:13.908Z] TOOL CALL #75: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && cat > /home/sfmqrb/git/rishe/data/verification/page-374.json <<'JSON'\n{\n  \"pdf_page\": 374,\n  \"book_page\": 344,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-07\",\n  \"entries\": [\n    {\n      \"entry\": 2,\n      \"root\": \"Ome\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *omə- (*h₃em-) 'to advance with force, press on; make firm; harass' (Pokorny 778; Walde-Pokorny I 178 f.)\",\n      \"note\": \"Pokorny 778 carries the lemma omə- with the meaning 'to proceed with energy; to make firm; to suffer', and its material opens with Skt. ámīti 'presses on, urges insistently, swears' and includes Av. ama- 'power, strength, male power, attack strength', amavant- 'strong, mighty' and amayava- 'affliction, hardship'. Nourai's root name, the label 'Indo-European' and the gloss 'to move with energy' therefore reproduce Pokorny/Walde-Pokorny almost verbatim, so the root box is right. Two caveats: (a) Watkins/AHD has no root of this shape at all (its om- is 'raw', Pok. 777, and om(e)so- is 'shoulder', Pok. 778), and Mann (IEC) splits the same material into om- (2) 'pain, sorrow, hardship' and om- (3) 'strength, power, ability', so the double semantics ('strength' plus 'injury, grief') that Nourai packs into one root is Pokorny's analysis, not a universally shared one; (b) the third item drawn in the Avestan box, arša-ama, is not an Avestan word but Nourai's (i.e. Bartholomae's) analysis of the Old Persian royal name Aršāma-.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *omə- «با نیرو پیش رفتن، فشار آوردن، سخت گرفتن» در فرهنگ پوکورنی ص ۷۷۸ با همین معنا آمده و در ذیل آن سنسکریت ámīti «فشار می‌آورد، سخت اصرار می‌کند» و اوستایی ama- «نیرو، توان، نیروی حمله»، amavant- «نیرومند» و amayava- «رنج، سختی» فهرست شده است؛ پس نام ریشه، برچسب زبانی و معنایی که نورایی داده است درست و تقریباً نقل عین پوکورنی و والده‌ـ پوکورنی است. دو نکته: واتکینز (فرهنگ AHD) چنین ریشه‌ای ندارد و مان (IEC) همین مواد را به دو ریشهٔ جداگانه «رنج» و «نیرو» بخش کرده است؛ همچنین صورت arša-ama که در جعبهٔ اوستایی آمده واژهٔ اوستایی نیست، بلکه تجزیهٔ نام پارسی باستان Aršāma- است. ادعای نورایی در بارهٔ خودِ ریشه درست است.\",\n      \"sources\": [\"https://en.wiktionary.org/wiki/%E0%A4%85%E0%A4%AE\"],\n      \"ref_check\": [\n        {\"ref\": \"POK:778\", \"status\": \"supports\", \"note\": \"POK_full.txt, entry ending 'Page(s): 778': 'Root / lemma: omə- (*houmə-) | Meaning: to proceed with energy; to make firm; to suffer | Material: Old Indic ámīti \\\"presses, insures urgently, swears\\\" ... = Avestan amavant- \\\"strong, mighty, vast, grand\\\". Old Indic ama- \\\"rush, impetuousness\\\" = Avestan ama- \\\"power, strength, male power, attack strength\\\", Adj. \\\"strong\\\" ... Avestan amayava \\\"affliction, hardship\\\". References: WP. I 178 f.' — exactly the root Nourai draws.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. I 178 f. (WLD_Bd1_pages.txt, running head 'obhel- — omo-, omə-')\", \"stance\": \"supports\", \"note\": \"'omo-, omə- \\\"gehobene Kraftäußerung, energisch in etwas oder gegen etwas vorgehn\\\"; daraus einerseits \\\"fest worauf bestehn, festmachen = eidlich bekräftigen\\\", andrerseits \\\"zusetzen, quälen, schädigen\\\"' — with ai. áma- m. 'Andrang' = av. ama- 'Kraft, männliche Potenz, Angriffskraft' and 'Av. amayavā \\\"Leid, Drangsal\\\"'. Nourai's gloss 'to move with energy' is a translation of this.\"},\n        {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt (roots om-, om(e)so-)\", \"stance\": \"silent\", \"note\": \"Watkins lists only 'om-. Raw. [Pok. om- 777]' and 'omeso-. Shoulder. [Pok. om(e)so-s 778]'; there is no root 'to move with energy' in the appendix, so AHD neither confirms nor denies this root.\"},\n        {\"src\": \"IEC\", \"where\": \"Mann, s.v. om- (2), om- (3), om- (4)\", \"stance\": \"partial\", \"note\": \"Mann separates 'om- (2) \\\"pain, sorrow, hardship\\\"' (Skt. amīvā, 'Av. cf. amayavə') from 'om- (3) \\\"strength, power, ability, skill\\\" ... Skt. ámaḥ \\\"strength\\\"; Av. amə, m. id.' — same material, but two roots rather than Nourai's one.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"ama; amâ-yavâ; arša-ama\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Av. ama- m. is genuine and means exactly what the chart says: Bartholomae AiW s.v. '*ama-, g. āma- m. 1) \\\"Kraft, Stärke, Macht\\\"' and '3) bes. die beim Angriff entfaltete Kraft, \\\"Angriffskraft, impetus\\\"' (Yt.14.2 nərənō ... amə̄mča), with the adjective amavant- 'kräftig, stark, mächtig, gewaltig' — so 'strength, attack force' is right; it answers to Skt. áma- 'onset, pressure, strength' and descends directly from PIE *omə-. amayavā- is likewise attested: BRT s.v. 'amayavā- f. \\\"Leid, Drangsal\\\"' (Y.71.17 paitištātaēe xšayasča amayavayāsča 'to withstand misery and distress'), i.e. the 'harass, injure' branch of the same root, formed with a -yav- suffix (Bartholomae, Studien II 178, posited a verb *amayeiti beside Skt. amayati 'is ill'); Nourai's writing 'amâ-yavâ' with a hyphen and two long ā's is a normalisation, the Avestan form is amayavā-. The third item is different in kind: arša-ama is not an Avestan word but the analysis of the Old Persian dynastic name Aršāma- (Bīsutūn 1.2, XPf 20-25; Gk. Ἀρσάμης, Aram. ʾršm), grandfather of Darius I. Kent, Old Persian §1914, derives it as 'Aršāma- (from *arša-ama-) \\\"Having the might of a hero\\\"', so the segmentation arša- + ama- is standard; but the first element is taken by Kent (§1438: 'OP arša- \\\"male\\\" in Aršama-, Skt. ṛṣa-bhá- \\\"bull\\\"') and by Schmitt/Shahbazi (Enc. Iranica ARŠĀMA, whence Wikipedia 'having a hero's strength') as 'male, hero', while Nourai's 'with power of a bear' follows Bartholomae AiW 204/206, which glosses the compound 'die Kraft eines Bären besitzend' but adds in a footnote 'Oder auch \\\"eines Mannes, Helden\\\"'. Bears are indeed Av. arša- (BRT '(p.) *arša- m. \\\"Bär\\\"', Skt. ŕ̥kṣa-, NP xirs), so the reading is possible, but it is the minority one today — hence 'plausible' rather than 'confirmed' for the node.\",\n          \"derivation_fa\": \"اوستایی ama- «نیرو، توان، به‌ویژه نیرویی که در هنگام حمله آشکار می‌شود» در فرهنگ بارتولمه با همین معنا («Kraft, Stärke, Macht» و «Angriffskraft») ثبت است و صفت آن amavant- «نیرومند» است؛ هم‌ریشه با سنسکریت áma- و بازماندهٔ مستقیم ریشهٔ هندواروپایی *omə-. صورت amayavā- «رنج، سختی» نیز در اوستا (یسنا ۷۱٫۱۷) آمده و شاخهٔ «آزار رساندن» همان ریشه است؛ نگارش «amâ-yavâ» در کتاب صورتی هنجاریده است. اما arša-ama واژهٔ اوستایی نیست، بلکه تجزیهٔ نام پارسی باستان Aršāma- (نیای داریوش بزرگ، در بیستون و XPf) است: کنت در دستور پارسی باستان §۱۹۱۴ آن را از *arša-ama- «دارندهٔ نیروی پهلوان» می‌گیرد، یعنی بخش‌بندی نورایی درست است، ولی جزء نخست را نه «خرس» بلکه arša- «نر، پهلوان» می‌داند؛ خوانش «نیروی خرس» از بارتولمه است که خود در پانوشت گزینهٔ «مرد/پهلوان» را هم آورده. پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wikipedia.org/wiki/Arsames\",\n            \"https://en.wiktionary.org/wiki/%E0%A4%85%E0%A4%AE\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:778\", \"status\": \"supports\", \"note\": \"Pokorny 778 s.v. omə- lists both of the genuine Avestan words of this node: 'Avestan ama- \\\"power, strength, male power, attack strength\\\", Adj. \\\"strong\\\"' and 'Avestan amayava \\\"affliction, hardship\\\"'. It does not mention Aršāma-.\"},\n            {\"ref\": \"SYN:298\", \"status\": \"supports\", \"note\": \"Buck, Dictionary of Selected Synonyms, printed p. 298 (section 4.81 STRONG), verified by the page number standing eight lines above the entry in SYN.txt: 'Av. amavant-, fr. ama- \\\"strength, power\\\" : Skt. ama- \\\"onset\\\", am- \\\"press on, injure\\\", ON ama \\\"vex, annoy,\\\" etc. Walde-P. 1.178. Barth. 141.' — the page Nourai cites really does carry ama- 'strength' and the root connection.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"AiW col. 141 (BRT.txt line 4724) and col. 139 (line 4696), col. 138 (line 4693), col. 204/206 (lines 5628-5632)\", \"stance\": \"partial\", \"note\": \"'j. *ama-, g. āma- m. 1) \\\"Kraft, Stärke, Macht\\\" ... 3) bes. die beim Angriff entfaltete Kraft, \\\"Angriffskraft, impetus\\\"'; 'ama-vant- ... \\\"kräftig, stark, mächtig, gewaltig, wuchtig\\\"'; 'amayavā- f. \\\"Leid, Drangsal\\\"'; and for the name: 'aršāma- m. EN. eines Persers, Arsames ... Komp.: arša-*ama- \\\"die Kraft eines Bären\\\" besitzend. — Oder auch \\\"eines Mannes, Helden\\\"'. Supports ama- and amayavā- fully; on the name it gives Nourai's 'bear' gloss but flags the 'hero' alternative itself.\"},\n            {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, §1914 (and §1438)\", \"stance\": \"partial\", \"note\": \"'Aršāma- (from *arša-ama-) \\\"Having the might of a hero\\\"'; and §1438 'OP arša- \\\"male\\\" in Aršama- \\\"Arsames\\\", Skt. ṛṣa-bhá- \\\"bull\\\"'. Confirms the compound analysis arša- + ama-, contradicts the gloss 'bear'.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I 178 f.\", \"stance\": \"supports\", \"note\": \"'ai. áma- m. \\\"Andrang, Betäubung\\\" = av. ama- \\\"Kraft, männliche Potenz, Angriffskraft\\\", Adj. \\\"stark\\\" ... Av. amayavā \\\"Leid, Drangsal\\\"' — both words, same root.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"Aršâm «ارشام»\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The modern Persian male name ارشام / آرشام (Aršām / Āršām) is the Old Persian dynastic name Aršāma- (Achaemenid, grandfather of Darius I; Gk. Ἀρσάμης, Aram. ʾršm). It is not an inherited word transmitted through Middle Persian — no MP *aršām is recorded in MacKenzie or Nyberg — but a name revived in Persian in the 20th century out of the Achaemenid inscriptions and their Persian scholarly literature, which is precisely why it is a modern given name and why Mo'in treats it in the etymological footnotes of Borhan-e Qāṭeʿ rather than in the lexicon proper. On the derivation itself Mo'in's footnote (Borhan p. 31) says word-for-word what the chart says: 'آرشام — Aršām, name of the grandfather of Darius the Great, the Achaemenid king of kings, compounded of arša meaning \\\"bear\\\" and ama meaning \\\"strength\\\", altogether \\\"bear-strength\\\", \\\"having the strength of a bear\\\" (Bartholomae 204)'. So the arrow Av./OIr. ama- → Aršām is right, and the second element is secure; only the sense of the first element is uncertain, modern onomastics (Kent §1914, Schmitt's Iranisches Personennamenbuch, Shahbazi in Enc. Iranica) preferring arša(n)- 'male, hero' — 'having a hero's strength'. Hence plausible.\",\n          \"derivation_fa\": \"نام «ارشام / آرشام» در فارسی امروز همان نام پارسی باستان Aršāma- (نیای داریوش بزرگ) است و واژه‌ای موروثی نیست: در فارسی میانه (نه در فرهنگ مکنزی و نه نیبرگ) صورتی از آن ثبت نشده و این نام در سدهٔ چهاردهم خورشیدی از راه سنگ‌نوشته‌های هخامنشی و پژوهش‌های آن دوباره به نام‌گذاری فارسی راه یافته است. حاشیهٔ ریشه‌شناختی معین در برهان قاطع، ص ۳۱، درست همان چیزی را می‌گوید که در نمودار آمده است: «آرشام ــ Aršām نام جد داریوش بزرگ شاهنشاه هخامنشی، مرکب از arša بمعنی خرس و ama بمعنی زور، جمعاً خرس‌نیرو، دارای زور خرس. «بارتولمه ۲۰۴»». پس پیوند این نام با ama- «نیرو» درست است و تنها معنای جزء نخست جای گفت‌وگو دارد؛ ریشه‌شناسی امروزی آن را arša(n)- «نر، پهلوان» می‌داند، یعنی «دارای نیروی پهلوان». ادعای نورایی با احتیاط پذیرفتنی است.\",\n          \"sources\": [\"https://en.wikipedia.org/wiki/Arsames\"],\n          \"ref_check\": [\n            {\"ref\": \"BQT:31\", \"status\": \"supports\", \"note\": \"Borhan-e Qāṭeʿ vol. 1, printed p. 31 (archive.org borhan-ghate-v1 leaf n241; page read from the image and saved at data/verification/sources/refs/ocr/BQT/31.vision.txt), Mo'in's footnote no. 5: 'آرشام ــ Arshâm نام جد داریوش بزرگ شاهنشاه هخامنشی، مرکب از arsha بمعنی خرس و ama بمعنی زور، جمعاً خرس نیرو، دارای زور خرس. «بارتولمه ۲۰۴»' — Nourai's node is a translation of this footnote, and the page number is exact.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"MON_part1.txt / MON_part2.txt, grep 'ارشام' and 'آرشام'\", \"stance\": \"silent\", \"note\": \"The two OCR volumes of Farhang-e Fārsi on disk (the lexicon volumes) have no headword ارشام/آرشام; the name belongs to Mo'in's aʿlām volumes (5-6), which are not in the local library, so Mo'in's dictionary is silent here while his Borhan footnote (above) is explicit.\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, A Concise Pahlavi Dictionary (PHD.txt), grep 'arsam', 'ršm'\", \"stance\": \"silent\", \"note\": \"No Middle Persian *aršām / ʾršm is listed, which is why this is treated above as a learned revival of the Old Persian name rather than an inherited Persian word.\"},\n            {\"src\": \"KNT\", \"where\": \"Kent, Old Persian §1914\", \"stance\": \"partial\", \"note\": \"'Aršāma- (from *arša-ama-) \\\"Having the might of a hero\\\"' — same compound, different gloss for arša-.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Sogdian\",\n          \"words\": \"âm`n\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Sogdian ʾmʾn (Buddhist Sogdian) 'power, force' is entry 151 in Gharib's Sogdian Dictionary, where the etymology is given as Avestan ama-: 'ʾmʾn B | aman ? ©Av. a-ma | power' (references BSTBL, Vim. 140; Bailey, Prolexis 137). The form is the Old Iranian *ama- 'strength' extended by the common Sogdian abstract/plural suffix -ʾn (-ān), i.e. *ama-āna- > ʾmʾn, with Old Iranian a-vocalism preserved; Gharib marks the reading 'aman' with a query because the Sogdian script does not distinguish the vowel quantity. So the arrow root/Avestan ama- → Sogdian ʾmʾn is exactly what the standard Sogdian dictionary says, and Nourai's gloss 'power, force, strength' is Gharib's.\",\n          \"derivation_fa\": \"سغدی ʾmʾn «نیرو، توان» در فرهنگ سغدیِ بدرالزمان قریب مدخل ۱۵۱ است و خودِ قریب ریشهٔ آن را «اوستایی ama-» نوشته است. این صورت همان *ama- ایرانی باستان است با پسوند سغدی ‎-ʾn (ān)، یعنی *ama-āna- > ʾmʾn؛ واکهٔ a ایرانی باستان در سغدی نگه داشته شده و قریب خوانش aman را با علامت پرسش آورده، زیرا خط سغدی کشش واکه را نشان نمی‌دهد. پس ادعای نورایی (ریشه ← سغدی) و معنایی که داده است، درست و برابر با فرهنگ قریب است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"SOD:6\", \"status\": \"supports\", \"note\": \"Gharib, Sogdian Dictionary, entry 151, on printed p. 6 (SOD_pages.txt pdf leaf 72; the offset is fixed by pdf leaf 76 = printed 10): '151 ʾmʾn B | aman ? ©Av. a-ma | power | BSTBL, Vim. 140; VJ n p92.222; Bailey, Prolexis 137'. Nourai's page number is exact and the gloss and the Avestan etymology are Gharib's own.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SOD\", \"where\": \"entry 151, printed p. 6\", \"stance\": \"supports\", \"note\": \"The only Sogdian dictionary in the local matrix; quoted in full above — 'aman ? ©Av. a-ma  power'.\"},\n            {\"src\": \"BRT\", \"where\": \"AiW col. 141\", \"stance\": \"supports\", \"note\": \"Supplies the Avestan base Gharib refers to: '*ama-, g. āma- m. \\\"Kraft, Stärke, Macht\\\"'.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 5,\n      \"root\": \"Op\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *h₃ep- 'to work, produce in abundance' (Pokorny 780 op-1; Watkins AHD op-1)\",\n      \"note\": \"Pokorny 780 has '1. op- \\\"arbeiten ..., zustandebringen; Ertrag der Arbeit, Reichtum\\\"' (English database rendering: 'to work, perform'), and Watkins/AHD has 'op-1. To work, produce in abundance ... [Pok. 1. op- 780]' — Nourai's gloss is Watkins' wording verbatim, and both his cited authorities carry the material of his Avestan and Latin boxes. Wiktionary reconstructs the same root as *h₃ep- 'to work, toil, make; ability, force'. The one cross-cutting problem on this chart is that Pokorny, Walde-Pokorny and Watkins all recognise a SECOND, homophonous root op- 'to choose' (Pok. 781, WP I 176 f., AHD op-2), and it is there, not here, that Latin optiō / English option belong; Nourai has attached them to op- 'work' (see nodes 6 and 7). A second problem is Germanic oft / English often (nodes 4 and 5), which Nourai's own reference AHD files under *upo, not under op-.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *h₃ep- «کار کردن، فراوان فراهم آوردن» است؛ پوکورنی ص ۷۸۰ آن را «1. op- کار کردن، به انجام رساندن؛ دستاورد کار، ثروت» آورده و واتکینز در پیوست AHD دقیقاً «op-1. To work, produce in abundance» نوشته است، یعنی معنایی که نورایی داده نقل عین واتکینز است. ویکی‌واژه هم همین ریشه را *h₃ep- «کار کردن؛ توان» بازسازی می‌کند. دو اشکال سراسری در این نمودار هست: نخست آنکه پوکورنی، والده‌ـ پوکورنی و واتکینز همه ریشهٔ دوم و همنامِ op- «برگزیدن» (پوکورنی ۷۸۱) را جدا می‌دانند و optiō لاتین و option انگلیسی به آن ریشه تعلق دارد نه به این؛ دوم آنکه oft ژرمنی و often انگلیسی را همان مرجعِ مورد استناد نورایی (AHD) زیر ریشهٔ *upo آورده است، نه زیر op-.\",\n      \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%83ep-\"],\n      \"ref_check\": [\n        {\"ref\": \"POK:780\", \"status\": \"supports\", \"note\": \"POK_full.txt, 'Root / lemma: op-1 (*hue-p-) | Meaning: to work, perform | Material: Old Indic apas- n. \\\"work\\\" (= Latin opus), Avestan hv-apah- \\\"good work (verrichtend)\\\"; ... apnas- n. \\\"yield, property, possession\\\", Avestan afnah-vant- \\\"richly in possession\\\"; ... Latin opus, -eris \\\"work\\\" ... officium \\\"obligation\\\" < *opi-ficium ... copia (*co-opia), opulentus ... probably also optimus \\\"the best\\\" (actually \\\"the wealthiest\\\") ... Page(s): 780'. Every element of Nourai's Avestan and Latin boxes is on that page — except optiō, which Pokorny puts under 'op-2 to choose', page 781.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. I 175-176 (WLD_Bd1_pages.txt)\", \"stance\": \"supports\", \"note\": \"'1. op- \\\"arbeiten ..., zustandebringen; Ertrag der Arbeit, Reichtum\\\" ... Ai. ápas- n. \\\"Werk\\\" (= lat. opus): av. hv-apah- \\\"gutes Werk\\\" und (wie auch hu-apah) \\\"gutes Werk verrichtend\\\" ... ápnas- n. \\\"Ertrag, Habe, Besitz\\\", av. afnah-vant- \\\"reich an Besitz\\\" ... lat. opus, -eris ... inops, cōpia (*co-opia), opulentus ... wohl auch optimus'. Note that WLD prints BOTH of Nourai's Avestan variants hu-apah and hv-apah. WLD I 176 f. then has a separate '2. op- \\\"auswählen, den Vorzug geben, vermuten\\\"' with lat. optio.\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins, roots op-1 and op-2\", \"stance\": \"partial\", \"note\": \"'op-1. To work, produce in abundance. 1. ... Latin opus (stem oper-) ... OPERA, OPERATE ... MANEUVER ... OFFICINAL. 2. Latin officium ... (< *opi-fici-om) ... 5. Suffixed (superlative) form *op-tamo- in Latin optimus, best (< \\\"wealthiest\\\"): OPTIMUM. 6. Prefixed Latin form *co-op- ... in Latin cōpia, profusion, plenty: COPIOUS, COPY; CORNUCOPIA. [Pok. 1. op- 780.]' — supports the whole Latin box except: 'op-2. To choose. 1. Latin optiō, choice: OPTION ... [Pok. 2. op- 781.]', and OFT/OFTEN are indexed to 'upo', not to op-1.\"},\n        {\"src\": \"IEC\", \"where\": \"Mann, s.v. op- (2), op- (3)\", \"stance\": \"partial\", \"note\": \"'op- (3) (same as (2)?) \\\"activity, work\\\". WP I, 175 ... Skt. ápas, n. \\\"work\\\" ... Lat. opus, gs: -eris, n. \\\"work, business, deed\\\" ... Umb. opeter, adj. \\\"of the best\\\"'; and 'op- (2) \\\"yield, produce\\\" ... Skt. ápnas, n. \\\"wealth, property\\\" ... Lat. opēs ... opulentus'. Same material, but Mann hesitates between one root and two, and files Nourai's 'possessions' sense under op- (2).\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"hu-apah, hv-apah; afnah\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Both Avestan forms are real and both spellings Nourai prints are the ones the handbooks use. Bartholomae AiW (col. 1847) has 'j., g. hv-apah- 1) (im gAw.) n. \\\"gutes Werk, Wirken\\\"' (Y.37.2 ahyā xšaθrāčā mazənāčā hvāpaŋhāčā 'because of his dominion and greatness and his fine works'), '2) (im jAw.) Adj. \\\"gute, schöne Werke verrichtend, wohlwirkend\\\"', epithet of Ahura Mazdā (Yt.10.54); beside it stands the Gāthic variant hu-apaŋha- 'gute, schöne Werke verrichtend' (col. 1808). Walde-Pokorny I 175 gives exactly Nourai's pair: 'av. hv-apah- \\\"gutes Werk\\\" und (wie auch hu-apah) \\\"gutes Werk verrichtend\\\"'. The compound is hu- 'good' (PIE *h₁su-, Nourai's cross-reference ☞Su 1) + apah- < *op-es- 'work', the neuter s-stem that Latin opus and Skt. ápas- also continue, so the derivation from the root is regular. The second word, afnah- 'possessions', is the *op-nes- formation of the same root (Skt. ápnas- 'yield, property, possession'); in Avestan it is attested only in the derivative adjective — BRT 'j. afnah-vant- Adj. \\\"reich an Habe\\\"' and the fem. *afnaŋuhī- (F.2c) — and both Pokorny 780 and WP I 175 accordingly cite 'Avestan afnah-vant-'. Nourai's bare afnah is therefore a stem abstracted from afnahvant- rather than an independently attested word, which is a normalisation, not an error.\",\n          \"derivation_fa\": \"هر دو صورت اوستایی درست است و همان دوگانه‌ای است که کتاب‌های مرجع می‌آورند: بارتولمه در «واژه‌نامهٔ ایرانی باستان» ستون ۱۸۴۷ می‌نویسد hv-apah- در گاهان اسم است به معنای «کار نیک، کردار نیک» (یسنا ۳۷٫۲) و در اوستای نو صفت است «نیک‌کردار» و لقب اهوره‌مزدا (یشت ۱۰٫۵۴)، و در برابر آن صورت گاهانی hu-apaŋha- می‌آید؛ والده‌ـ پوکورنی جلد ۱ ص ۱۷۵ نیز عیناً همین دو صورت «hv-apah- و همچنین hu-apah» را ثبت کرده است. ساخت آن hu- «نیک» (هندواروپایی *h₁su-) + apah- «کار» از ستاک s‑دار *op-es- است، همان که لاتین opus و سنسکریت ápas- بازماندهٔ آن‌اند. واژهٔ دوم، afnah- «دارایی»، ساخت *op-nes- همان ریشه است (سنسکریت ápnas-) و در اوستا تنها در صفتِ afnah-vant- «توانگر، پرمال» گواهی دارد؛ پس صورت مجرد afnah در کتاب ستاکی است که از همان صفت بیرون کشیده شده، نه خطا. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"POK:780\", \"status\": \"supports\", \"note\": \"Pokorny 780 s.v. op-1: 'Old Indic apas- n. \\\"work\\\" (= Latin opus), Avestan hv-apah- \\\"good work (verrichtend)\\\" ... apnas- n. \\\"yield, property, possession\\\", Avestan afnah-vant- \\\"richly in possession\\\"'. Both of Nourai's Avestan items are on the cited page.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"AiW col. 1847 (BRT.txt line 30647), col. 1808 (line 29556), col. 106 (line 4022)\", \"stance\": \"supports\", \"note\": \"'j., g. hv-apah- 1) (im gAw.) n. \\\"gutes Werk, Wirken\\\" ... 2) (im jAw.) Adj. \\\"gute, schöne Werke verrichtend, wohlwirkend\\\", von AhM.'; 'g. hu-apaŋha- Adj. (fem. °ŋhā-) \\\"gute, schöne Werke verrichtend, wohlwirkend\\\"'; 'j. afnah-vant- Adj. \\\"reich an Habe\\\"'. Confirms the words, the meanings and (implicitly) that afnah- itself is not attested alone.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I 175\", \"stance\": \"supports\", \"note\": \"'av. hv-apah- \\\"gutes Werk\\\" und (wie auch hu-apah) \\\"gutes Werk verrichtend\\\" ... ápnas- n. \\\"Ertrag, Habe, Besitz\\\", av. afnah-vant- \\\"reich an Besitz\\\"' — the only source consulted that prints both of Nourai's variant spellings side by side.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins op-1\", \"stance\": \"silent\", \"note\": \"Watkins' entry cites no Iranian forms at all (only Latin and Germanic), so it neither supports nor contradicts the Avestan box; the suffixed form *op-es- he posits for Latin opus is however exactly the formation of Av. apah-.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"xŭb «خوب»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP خوب xūb 'good, fine' goes back to MP xūb, written hwp — MacKenzie, Concise Pahlavi Dictionary p. 95: 'xūb [hwp | M xwb, N ~] good. ~īh: goodness'; Nyberg II: 'xūp [hwp] good, excellent, agreeable ... MPrs xwb (S) ... Paz. NP xub' — and MP xūb continues Old Iranian *hu-āpah- 'doing good work', i.e. precisely the Avestan hu-apah-/hv-apah- of the parent node, with the regular loss of the Old Iranian intervocalic/final -ah- of the s-stem, hu- > MP xu- (the same hu- > x(u)- as in husrav > xusraw, hušk > xušk) and contraction of *hu-ā- to xū-. This is Horn's derivation at the very page Nourai cites and it is the modern one: Wiktionary derives Persian خوب from MP xwb, Proto-Iranian *HhuHā́pah, Proto-Indo-Iranian *HsuHápas, PIE *h₁su- 'good' + *h₃épos 'work'. The semantic shift is 'doing good work, beneficent' → 'good, fine, nice'. The one dissent on record is Hübschmann's (see consulted): he objected that hvāpah- ought to have yielded NP *xvāb / *xvai and preferred Skt. su-vapus- 'of good form' — a phonological worry not shared by the current handbooks, which is why the node is confirmed rather than plausible.\",\n          \"derivation_fa\": \"«خوب» از فارسی میانهٔ xūb (نگاشتِ hwp) است — مکنزی، فرهنگ کوچک پهلوی، ص ۹۵: «xūb [hwp | M xwb, N ~] good»؛ نیبرگ: «xūp [hwp] good, excellent» — و آن از ایرانی باستان *hu-āpah- «نیک‌کردار» است، یعنی همان hu-apah-/hv-apah- اوستایی در جعبهٔ بالا. دگرگونی آوایی هنجارین است: ستاک s‑دار ‎-ah در فارسی میانه از میان می‌رود، hu- ایرانی باستان در فارسی میانه به xu- بدل می‌شود (چنان‌که husrav > خسرو و hušk > خشک)، و *hu-ā- به xū- کشیده فروکاسته می‌شود. هرن در همان صفحه‌ای که نورایی ارجاع داده (شمارهٔ ۵۰۳، ص ۱۱۱) همین را می‌گوید و ویکی‌واژه هم امروز خوب را از فارسی میانهٔ xwb و ایرانی آغازین *HhuHā́pah و در نهایت *h₁su- «نیک» + *h₃épos «کار» می‌گیرد. تحول معنایی: «نیک‌کردار» ← «خوب، نیکو». تنها مخالف، هوبشمان است که می‌گوید از hvāpah- باید *xvāb یا *xvai به دست می‌آمد و آن را با سنسکریت su-vapus- «خوش‌اندام» می‌سنجد؛ این ایراد در پژوهش امروزی پذیرفته نشده است. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%AE%D9%88%D8%A8\"],\n          \"ref_check\": [\n            {\"ref\": \"HRN:111\", \"status\": \"supports\", \"note\": \"Horn, Grundriss der neupersischen Etymologie, printed p. 111 (= HRN.txt leaf 133, offset leaf = printed + 22), entry no. 503: 'xūb \\\"gut, schön\\\", xūbī. Kāš. xūb, xōb, xēb. — aw. hvāpah- \\\"wohltätig\\\"; phlv. xūp bezw. xūp, xūpīh; ai. svápas-.' Nourai's citation is exact: the cited page derives xūb from Av. hvāpah- and gives the Pahlavi intermediate.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie p. 95 s.v. xūb (PHD.txt line 661; PHD_mackenzie.txt line 5576)\", \"stance\": \"supports\", \"note\": \"'xūb [hwp | M xwb, N ~] good. ~īh: goodness' — supplies the Middle Persian link (and the Manichaean MP spelling xwb) that the chart's arrow Avestan → Persian passes through, though MacKenzie gives no etymology.\"},\n            {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, glossary s.v. xūp (NYB_vol2_glossary.txt line 4303)\", \"stance\": \"partial\", \"note\": \"'xūp [hwp] good, excellent, agreeable 91.6, 39.19, 59.19; ~ kartan to put in order; adv. well, perfectly. — MPrs xwb (S) not in MPrth., where xwž (S), xwj (A-H III) corresponds; Paz. NP xub.' Confirms the MP form and the NP outcome; offers no Avestan etymology, and notes that Parthian has a different word.\"},\n            {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien p. 57 (note to Horn 503), repeated pp. 169 and 215\", \"stance\": \"contradicts\", \"note\": \"'503. Nach dieser Etymologie sollte man im Neup. *xvai, *aXvai oder *xvab statt xūb erwarten. Ich setze xūb (paz. xūb, afgh. LW. xūb \\\"schön\\\") = skr. suvapus- N. pr. (von su \\\"gut\\\" und vapus- \\\"Gestalt, Schönheit\\\").' Hübschmann explicitly rejects Horn's (= Nourai's) derivation from hvāpah- on phonological grounds and proposes *hu-vapuš- 'of good form' instead; the modern handbooks (and Wiktionary's Proto-Iranian *HhuHā́pah) follow Horn, not Hübschmann.\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e Rishe-hā, printed pp. 250-251 (ARY_pages.txt, running head 'خوب ۲۵۱')\", \"stance\": \"silent\", \"note\": \"The entry exists in the scan but the OCR of its Latin cognate lists on those pages is mirrored and garbled (e.g. 'اوستایی (AVESTAN): 1318۸۸'), so no etymological statement could be read out of it; not usable either way.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Sogdian\",\n          \"words\": \"xwp\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Sogdian xwp (Manichaean and Christian Sogdian) 'good' is Gharib's entry 10739, and Gharib gives Nourai's etymology herself: 'xwp M, C | xūp ©<Av. hvapah, Skt. svapas', with the derivatives xwptr 'better' (10740), xwpy(y) 'goodness' (10741) and the compound mnt-xwpy. Sogdian xwp and MP xūb are thus parallel, independent outcomes of Old Iranian *hu-āpah-: the s-stem ending is lost, hu- becomes xw- (written xw-, i.e. /xu-/), and the p of *āpah remains unvoiced in Sogdian as in the MP spelling hwp. Since Nourai's own reference is the standard Sogdian dictionary and it states the derivation explicitly, the arrow is confirmed.\",\n          \"derivation_fa\": \"سغدی xwp «خوب» (در متون مانوی و مسیحی سغدی) مدخل ۱۰۷۳۹ فرهنگ قریب است و خودِ قریب همان ریشه‌شناسی نورایی را آورده: «xūp ©<Av. hvapah، سنسکریت svapas»، با مشتقات xwptr «بهتر»، xwpy(y) «خوبی» و ترکیب mnt-xwpy. پس سغدی xwp و فارسی میانهٔ xūb دو بازماندهٔ جداگانه از ایرانی باستان *hu-āpah-اند: پایانهٔ ستاک s‑دار می‌افتد، hu- به xw- بدل می‌شود و p در سغدی (همچون نگاشت پهلوی hwp) بی‌واک می‌ماند. ادعای نورایی درست است و عیناً گفتهٔ مرجعِ خودِ اوست.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"SOD:436\", \"status\": \"supports\", \"note\": \"Gharib, Sogdian Dictionary, entry 10739 on printed p. 436 — the page number '436' stands at the head of SOD_pages.txt pdf leaf 504, which carries the entry: '10739 xwp M, C [Persian خوب] | xūp ©<Av. hvapah Skt. svapas ⇒mntxwpy, nʾxwp, γwp'. Nourai's page reference is exact and the Avestan source is Gharib's own.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SOD\", \"where\": \"entries 10739-10741, printed p. 436\", \"stance\": \"supports\", \"note\": \"Quoted above; the only Sogdian dictionary in the matrix. Also 'xwptr C' (10740) 'better' and 'xwpy(y) M, C  xup(e)' (10741).\"},\n            {\"src\": \"BRT\", \"where\": \"AiW col. 1847\", \"stance\": \"supports\", \"note\": \"Supplies the Avestan base Gharib cites: 'hv-apah- ... \\\"gutes Werk\\\" ... Adj. \\\"gute, schöne Werke verrichtend\\\"'.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Germanic\",\n          \"words\": \"oft\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Germanic *ufta 'frequently' (Goth. ufta, OE oft, ON opt, OHG ofto) is real, but modern scholarship does not derive it from *op- 'to work'. Nourai cites AHD for this arrow, and AHD in fact files it elsewhere: Watkins s.v. 'upo. Under, up from under, over ... 4. Possibly suffixed form *up-t- in Germanic *ufta, frequently, in Old English oft: OFT, OFTEN. [Pok. upo 1106]', and his op-1 entry contains no Germanic 'oft' at all (its Germanic material is OE efnan, OHG uobo, uoben 'to practise, cultivate', ON efna). Pokorny 780 likewise has no oft under op-1. Klein calls oft 'of uncertain origin' and Etymonline says 'from Proto-Germanic *ufta- \\\"frequently\\\", a word of unknown origin, perhaps from a suffixed form of PIE root *upo \\\"under\\\"'. So the modern view is: either unknown, or from *upo — not from *op-.\",\n          \"derivation_fa\": \"صورت ژرمنی *ufta «بسیار، پیاپی» (گوتی ufta، انگلیسی کهن oft، نورس کهن opt، آلمانی علیای کهن ofto) واژهٔ واقعی است، اما پژوهش امروزی آن را از ریشهٔ op- «کار کردن» نمی‌گیرد. نورایی برای این پیکان به AHD ارجاع داده، در حالی که واتکینز خودِ این واژه را زیر ریشهٔ *upo آورده است: «*up-t- در ژرمنی *ufta \\\"frequently\\\"، انگلیسی کهن oft: OFT, OFTEN [پوکورنی upo ۱۱۰۶]»، و در مدخل op-1 هیچ اشاره‌ای به oft نیست. پوکورنی ص ۷۸۰ هم oft را ذیل op-1 نیاورده؛ کلاین آن را «با خاستگاه نامعلوم» می‌داند و اتیمانلاین می‌گوید «از ژرمنی آغازین *ufta-، با خاستگاه ناشناخته، شاید از ریشهٔ *upo». پس پژوهش امروزی این پیکان را رد می‌کند.\",\n          \"sources\": [\"https://www.etymonline.com/word/often\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"contradicts\", \"note\": \"AHD_watkins1985.txt s.v. upo: 'Possibly suffixed form *up-t- in Germanic *ufta, frequently, in Old English oft, oft: OFT, OFTEN'; and the index line 'OFT upo / OFTEN upo'. Watkins' op-1 entry (the root Nourai is on) lists no Germanic word for 'frequently'. Nourai's own cited authority puts this word under a different root.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"POK_full.txt s.v. op-1, page 780\", \"stance\": \"silent\", \"note\": \"The Germanic material of Pokorny's op-1 is 'Old English efnan, Old Icelandic efna \\\"work, do\\\"; lengthened grade Old High German uobo \\\"land farmer\\\", uoben ... Modern High German üben' — no oft/ofto anywhere.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. oft, often (KLN_1966.txt line 26144)\", \"stance\": \"contradicts\", \"note\": \"'oft, adv., often (archaic or poet.) — ME., fr. OE. oft, rel. to OS. oft, ofto, OFris. ofta, Dan. ofte, Swed. ofta, OHG. ofto, MHG. ofte, oft, G. oft, ON. opt, Goth. ufta, \\\"often\\\"; of uncertain origin.' Klein declines any connection with opus/op-.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"English\",\n          \"words\": \"often\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"English often is simply the extended form of oft — Klein: 'often, adv. — ME. ofte, often, extended fr. oft'; Etymonline dates the extension to the mid-13th c. and explains that the form in -en was used before vowels and h-, later generalised. So the arrow Germanic oft → English often is itself correct and uncontroversial. The node is marked disputed only because it inherits the problem of its parent: the chain hangs from the root Op, whereas oft/often belongs (per Watkins) under *upo or (per Klein and Etymonline) to no known PIE root.\",\n          \"derivation_fa\": \"انگلیسی often صورت گستردهٔ oft است — کلاین: «often از انگلیسی میانهٔ ofte, often، گسترش‌یافتهٔ oft»؛ اتیمانلاین این گسترش را به میانهٔ سدهٔ سیزدهم می‌رساند و می‌گوید نخست پیش از واکه و h به کار می‌رفت و سپس همه‌جایی شد. پس پیکان «ژرمنی oft ← انگلیسی often» درست و بی‌گفت‌وگوست و این گره تنها به سبب اشکال گرهِ مادر «رد‌شده» علامت خورده است: زنجیرهٔ oft/often به ریشهٔ Op بسته نمی‌شود، بلکه به گفتهٔ واتکینز به *upo می‌پیوندد و به گفتهٔ کلاین و اتیمانلاین خاستگاه هندواروپایی روشنی ندارد.\",\n          \"sources\": [\"https://www.etymonline.com/word/often\"],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this node; checked against AHD (index 'OFTEN upo'), Klein s.v. often, and Etymonline instead.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. often (KLN_1966.txt line 26144)\", \"stance\": \"partial\", \"note\": \"'often, adv. — ME. ofte, often, extended fr. oft. See oft.' Supports the oft → often step, but oft is 'of uncertain origin', so not the root drawn here.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins index, 'OFTEN upo'\", \"stance\": \"contradicts\", \"note\": \"The word is indexed to upo, not to op-1.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Latin\",\n          \"words\": \"opus; optimus; co-op; optîo; opi-facium\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Four of the five items are right and are exactly what Nourai's two references say. (1) opus, operis n. 'work' is the Latin reflex of the s-stem *op-es- (Pokorny 780 'Latin opus, -eris \\\"work, occupation, action\\\"'; AHD 'Suffixed form *op-es- in Latin opus (stem oper-)'), with the denominative operārī and the noun opera. (2) optimus 'best' is Pokorny's and Watkins' superlative *op-tamo- of the same root, 'eigentlich \\\"der wohlhabendste\\\"' (WP I 176) — i.e. Nourai's gloss 'with most production or possessions' is a translation of Walde-Pokorny. (3) 'co-op' is Nourai's shorthand for the prefixed form *co-op- that gives cōpia 'plenty' (AHD: 'Prefixed Latin form *co-op- ... in Latin cōpia, profusion, plenty'; Klein s.v. copious: 'copia, \\\"plenty, abundance\\\", contraction of *co-opia, fr. co- and ops, gen. opis'), so the entry is a formation and not a misprint. (4) 'opi-facium' is Klein's reconstruction for officium: 'office, n. — ME., fr. OF. (= F.), fr. L. officium, \\\"service\\\", which stands for *opi-faciom, lit. \\\"work-doing\\\"' (Watkins writes *opi-fici-om), the second element being facere, whence Nourai's cross-reference ☞Dhě 2. But (5) optiō 'choice' does NOT belong to this root: Pokorny puts it under '2. op- \\\"to choose; to suggest\\\" ... Latin optiō \\\"free choice\\\"', page 781; Walde-Pokorny I 176 f. the same ('2. op- \\\"auswählen, den Vorzug geben\\\" ... wozu optiō f. \\\"freie Wahl\\\"'); Watkins the same ('op-2. To choose. 1. Latin optiō, choice ... [Pok. 2. op- 781]'); and de Vaan (via Etymonline) derives optāre from Proto-Italic *opeje- 'to choose, grab', PIE *h₃epeie-. Nourai's gloss 'choice (from abundance)' is an attempt to bridge the two homophonous roots, but no standard authority — including the two he cites here — makes that bridge. Hence the node takes the worst verdict of its words.\",\n          \"derivation_fa\": \"چهار واژه از پنج واژهٔ این جعبه درست است و درست همان چیزی است که دو مرجعِ مورد استناد نورایی می‌گویند: opus «کار» بازماندهٔ ستاک s‑دار *op-es- است (پوکورنی ۷۸۰؛ واتکینز)، با فعل برساختهٔ operārī و اسم opera؛ optimus «بهترین» صورت برترینِ *op-tamo- همان ریشه است و والده‌ـ پوکورنی معنای اصلی آن را «توانگرترین» می‌داند، یعنی ترجمهٔ همان چیزی که نورایی نوشته؛ «co-op» کوتاه‌نوشتِ صورت پیشوندی *co-op- است که cōpia «فراوانی» از آن است (کلاین: cōpia از *co-opia، از co- و ops)؛ و «opi-facium» بازسازی کلاین برای officium است: «officium که به‌جای *opi-faciom است، تحت‌اللفظی \\\"کارکردن\\\"». اما optiō «گزینش» به این ریشه تعلق ندارد: پوکورنی آن را ذیل «۲. op- برگزیدن» در ص ۷۸۱ آورده، والده‌ـ پوکورنی جلد ۱ ص ۱۷۶ به بعد و واتکینز (op-2) نیز همچنین، و دِ وان صورت optāre را از ایتالیکی آغازین *opeje- «برگزیدن، گرفتن» و هندواروپایی *h₃epeie- می‌گیرد. توضیح نورایی («گزینش، از فراوانی») کوششی است برای پیوند دادن دو ریشهٔ همنام، ولی هیچ مرجع معیاری — از جمله همان دو مرجعی که خودش نام برده — این پیوند را نمی‌پذیرد. پس در بارهٔ optiō پژوهش امروزی ادعای نورایی را رد می‌کند و ریشهٔ دیگری (op- «برگزیدن») را می‌نشاند.\",\n          \"sources\": [\"https://www.etymonline.com/word/option\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"Watkins op-1 confirms opus/opera, officium '< *opi-fici-om, \\\"performance of work\\\"', optimus '*op-tamo- ... best (< \\\"wealthiest\\\")' and '*co-op- ... in Latin cōpia, profusion, plenty'. But 'op-2. To choose. 1. Latin optiō, choice (from *opere, to choose): OPTION ... [Pok. 2. op- 781]' — the same book removes optiō from this root.\"},\n            {\"ref\": \"KLN\", \"status\": \"supports\", \"note\": \"Klein supports every Latin form Nourai lists here, in his own words: s.v. copious 'L. copiosus ... fr. copia, \\\"plenty, abundance\\\", contraction of *co-opia, fr. co- and ops, gen. opis'; s.v. office 'fr. L. officium, \\\"service\\\" ... which stands for *opi-faciom, lit. \\\"work-doing\\\"'; s.v. opera 'It., \\\"work, labor, composition\\\", fr. L. opera ... fr. opus, gen. operis'. (Klein files option under optāre 'to choose', not under opus.)\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"POK_full.txt, op-1 page 780 and op-2 page 781\", \"stance\": \"partial\", \"note\": \"op-1: 'Latin opus, -eris \\\"work\\\" ... officium \\\"obligation\\\" < *opi-ficium \\\"working performance\\\" ... inops, cōpia (*co-opia), opulentus ... probably also optimus \\\"the best\\\" (actually \\\"the wealthiest\\\")'. op-2 (p. 781): 'Meaning: to choose; to suggest ... Frequentativum to *opiō, -ere is Latin optō, -āre \\\"wish\\\", wherefore optiō \\\"free choice\\\", m. \\\"assistant\\\"'.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I 175-176 (1. op-) and 176 f. (2. op-)\", \"stance\": \"partial\", \"note\": \"'lat. opus, -eris \\\"Arbeit, Beschäftigung, Handlung, Werk\\\" ... officium \\\"Obligation\\\" < *opi-ficium ... inops, cōpia (*co-opia), opulentus ... wohl auch optimus \\\"der beste\\\" (eig. ... \\\"der wohlhabendste\\\")' — then separately '2. op- \\\"auswählen, den Vorzug geben, vermuten\\\" ... Frequentativum zu *opiō, -ere ist lat. optō, -āre \\\"wünschen\\\", wozu optiō f. \\\"freie Wahl\\\"'.\"},\n            {\"src\": \"LEW\", \"where\": \"Walde, Lateinisches etymologisches Wörterbuch (LEW_1910.txt), s.v. ops, optimus, opus / optio\", \"stance\": \"partial\", \"note\": \"Walde's Latin dictionary is the source Walde-Pokorny cross-refers to for exactly this split ('Vf. LEWb.2 u. ops, optimus, opus' for the 'work' root, and optiō, opīnor under the 'choose' root); it therefore agrees with the four confirmed words and with the removal of optiō.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"English\",\n          \"words\": \"opera, operate, maneuver; optimum; copy; option; office\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Six of the seven English words are straightforward continuations of the Latin box, and Klein documents each chain: opera came in through Italian — 'opera, n., a drama sung. — It., \\\"work, labor, composition\\\", fr. L. opera ... fr. opus, gen. operis; introduced into English by the diarist John Evelyn (1620-1706)'; operate is from L. operārī (AHD: 'with its denominative verb operārī, to work': OPERATE, OPEROSE, COOPERATE); maneuver is 'F. manoeuvre, fr. OF. manuevre, maneuvre, fr. VL. manuopera (a word occurring in Charlemagne's Capitularies in the sense of \\\"statute labor\\\"), fr. manuoperāre, corresponding to L. manū operārī, \\\"to work by hand\\\"', so a compound of manus + operārī (AHD indexes MANEUVER to both man-2 and op-1); optimum is the Latin superlative neuter taken over as a learned word; copy is 'ME. copie, fr. MF. (= F.) copie, \\\"abundance; copy\\\", fr. L. copia' with the medieval sense-shift 'plenty' → 'to write in plenty' → 'transcript' (ML. copiāre); office is 'ME., fr. OF. (= F.), fr. L. officium'. Only option is misplaced: it is 'from French option (Old French opcion), from Latin optiōnem (nominative optiō) \\\"choice, free choice, liberty to choose\\\", from optāre \\\"to desire, pray for, choose\\\"' (Etymonline), i.e. from op- (2) 'to choose' (Pokorny 781, Watkins op-2, de Vaan *h₃epeie-), not from op- 'to work'. Node verdict follows the worst word.\",\n          \"derivation_fa\": \"شش واژه از هفت واژهٔ این جعبه ادامهٔ بی‌گفت‌وگوی جعبهٔ لاتین است و کلاین هر زنجیره را ثبت کرده است: opera از ایتالیایی opera «کار، اثر» و آن از لاتین opera/opus، که جان اِوِلین (۱۶۲۰–۱۷۰۶) آن را به انگلیسی آورد؛ operate از operārī لاتین؛ maneuver از فرانسوی manœuvre و آن از فرانسوی کهن manuevre و لاتین عامیانهٔ manuopera (در فرمان‌های شارلمانی به معنای «کار بیگاری») از manū operārī «با دست کار کردن»، یعنی ترکیب manus + operārī؛ optimum همان صفت برترین لاتین است که واژهٔ فرهیخته وارد انگلیسی شد؛ copy از فرانسوی copie و لاتین cōpia «فراوانی» با تحول معنایی «فراوانی» ← «فراوان نوشتن» ← «نسخه»؛ office از officium. تنها option جای نادرست دارد: از فرانسوی option و لاتین optiōnem از optāre «برگزیدن»، یعنی از ریشهٔ op- «برگزیدن» (پوکورنی ۷۸۱؛ واتکینز op-2؛ دِ وان *h₃epeie-) نه از op- «کار کردن». حکم این گره بر پایهٔ بدترین واژه است.\",\n          \"sources\": [\"https://www.etymonline.com/word/option\"],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this node; checked against Klein (KLN_1966.txt s.vv. opera, copy, copious, office, maneuver), Watkins' AHD index ('OPERA! op-1, OPTIMUM op-1, COPY op-1, OFFICE dhē-1, MANEUVER man-2, op-1, OPTION op-2') and Etymonline s.v. option.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein s.vv. opera (line 26366), copy/copious (9146/9123), office (26133), maneuver (22783)\", \"stance\": \"partial\", \"note\": \"Supports the six words as quoted in the derivation; Klein derives option from optāre 'to choose', not from opus, so he too separates it.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins index and roots op-1, op-2\", \"stance\": \"partial\", \"note\": \"'OPERA! op-1 ... OPERATE op-1 ... COPY op-1 ... OPTIMUM op-1 ... MANEUVER man-2, op-1 ... OFFICINAL dhē-1, op-1' but 'OPTION op-2' and 'OFFICE dhē-1' (Watkins indexes office to the dhē- half of the compound, though officium appears in op-1 as *opi-fici-om).\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etymological Dictionary (SKT.txt), s.vv. opera, option\", \"stance\": \"partial\", \"note\": \"Skeat's entries agree with Klein on opera/operate/office/copy (all from L. opus, opera, cōpia) and take option from L. optāre, i.e. the 'choose' root; the OCR of this file is poor for individual headwords, so it is recorded here as corroborating rather than as a primary quotation.\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"French\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"An empty pass-through box: French is the stage through which the Latin op- words reach modern Persian. The relevant French forms are œuvre (< L. opera, OF uevre, oevre — Klein s.v. opera), opéra (borrowed into French from Italian opera in the 17th c. with the new musical sense) and manœuvre (< OF manuevre < VL manuopera 'hand-work'; Klein s.v. maneuver). All three descend from Latin opus/opera exactly as the arrow from node 6 requires, so the box is correct as drawn even though the book prints no word in it.\",\n          \"derivation_fa\": \"این جعبه تهی و تنها گذرگاه است: فرانسوی حلقهٔ میانی است که واژه‌های لاتینِ ریشهٔ op- از آن راه به فارسی نو رسیده‌اند. صورت‌های فرانسویِ مربوط عبارت‌اند از œuvre (از opera لاتین، فرانسوی کهن uevre/oevre)، opéra (که فرانسوی آن را در سدهٔ هفدهم با معنای موسیقایی از ایتالیایی opera وام گرفت) و manœuvre (از فرانسوی کهن manuevre و لاتین عامیانهٔ manuopera «کارِ دستی»). هر سه، چنان‌که پیکان جعبهٔ لاتین می‌خواهد، از opus/opera لاتین‌اند؛ پس این گره درست است، هرچند کتاب واژه‌ای در آن چاپ نکرده است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference given by Nourai for this pass-through box; checked against Klein s.vv. opera and maneuver (which give the French/Old French forms) and against Mo'in's [فر.] tag on the two Persian loans below.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. maneuver (line 22783) and s.v. opera (line 26366)\", \"stance\": \"supports\", \"note\": \"'F. manoeuvre, fr. OF. manuevre, maneuvre, fr. VL. manuopera ... fr. manuoperare, corresponding to L. manu operari'; and 'fr. L. opera ... (whence also OF. uevre, oevre, F. œuvre, \\\"work\\\")'. Confirms that French inherits/borrows the op- words from Latin.\"},\n            {\"src\": \"MON\", \"where\": \"Mo'in via abadis.ir, entries اپرا and مانور\", \"stance\": \"supports\", \"note\": \"Both Persian words are tagged '[فر.]' (French) in Farhang-e Moʿin, which is what makes this French box the right intermediary rather than a direct Latin or English borrowing.\"}\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"Persian\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"The two Persian words printed only in Persian script, اپرا and مانور, are modern loans from French, as the chart's French → Persian arrow says. اپرا operā is French opéra (itself Italian opera 'work, composition' < L. opera < opus), taken into Persian with European theatre in the late Qajar/early Pahlavi period; Farhang-e Moʿin tags it '[فر.]' and defines it '(اُ پِ) [فر.] (اِ.) ۱ - نمایشی که همراه با ساز و آواز و شعر باشد. ۲ - محل اجراء این گونه نمایش‌ها'. مانور mānovr is French manœuvre (< VL manuopera 'hand-work' < manū operārī), borrowed as a military term with the modern Iranian army; Moʿin: '(نُ وْ) [فر.] (اِ.) اجرای عملیات جنگی به طور نمایشی و تمرینی', and Dehkhodā likewise marks it French. Neither is an inherited Iranian word, so their appearance at the end of a Latin → French chain (rather than under the Avestan branch) is exactly right.\",\n          \"derivation_fa\": \"دو واژه‌ای که در این جعبه تنها به خط فارسی چاپ شده‌اند، «اپرا» و «مانور»، وام‌واژه‌های نوِ فرانسوی‌اند، همان‌گونه که پیکان «فرانسوی ← فارسی» می‌گوید. «اپرا» از فرانسوی opéra است و آن خود از ایتالیایی opera «کار، اثر» و از opera/opus لاتین؛ این واژه در اواخر قاجار و آغاز دورهٔ پهلوی همراه با تئاتر اروپایی به فارسی آمد و فرهنگ معین آن را با نشانِ «[فر.]» آورده است: «(اُ پِ) [فر.] (اِ.) ۱ ــ نمایشی که همراه با ساز و آواز و شعر باشد. ۲ ــ محل اجراء این گونه نمایش‌ها». «مانور» از فرانسوی manœuvre است (از manuopera لاتین عامیانه، از manū operārī «با دست کار کردن») و به‌عنوان اصطلاح نظامی با ارتش نوین وارد شد؛ معین: «(نُ وْ) [فر.] (اِ.) اجرای عملیات جنگی به طور نمایشی و تمرینی» و دهخدا نیز آن را فرانسوی می‌داند. هیچ‌یک واژهٔ موروثی ایرانی نیست؛ پس جای‌گیری آن‌ها در پایانِ زنجیرهٔ لاتین ← فرانسوی درست است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://abadis.ir/fatofa/%D8%A7%D9%BE%D8%B1%D8%A7/\",\n            \"https://abadis.ir/fatofa/%D9%85%D8%A7%D9%86%D9%88%D8%B1/\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"MON\", \"status\": \"supports\", \"note\": \"Farhang-e Moʿin has both words as European loans. Local OCR: MON_part1.txt line 6641 'اپرا: [- اوپرا] (ا.) (نم.) ترکیبی از شعر و موسیقی و نمایش ...' and MON_part2.txt line 43262 'مانور: (ا.) طریقهٔ تنظیم عمل دستگاه. (نظ.) فن رهبری دسته‌های ... در یک منطقه'; the Latin-script source word is mangled in the OCR, but the online text of Moʿin (abadis.ir, section فرهنگ معین) shows the tag explicitly: 'اپرا (اُ پِ) [فر.] (اِ.)' and 'مانور (نُ وْ) [فر.] (اِ.)' — [فر.] = French, exactly the route Nourai draws.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"abadis.ir mirror of Farhang-e Moʿin, s.vv. اپرا, مانور\", \"stance\": \"supports\", \"note\": \"Both tagged [فر.] 'French'; Dehkhodā's entry for مانور also identifies it as French.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein s.vv. opera, maneuver\", \"stance\": \"supports\", \"note\": \"Supplies the upstream chain the Persian words hang on: It. opera < L. opera < opus; F. manoeuvre < VL manuopera < L. manū operārī.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\nJSON\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-374.json > /dev/null && echo \"JSON OK\"",
 "description": "Write verification file for page 374"
}
```


### [2026-09-07T20:34:15.440Z] TOOL RESULT

```
JSON OK
```


## [2026-09-07T20:34:19.931Z] TOOL CALL #76: Bash

```json
{
 "command": "python3 tools/verify_check.py 374",
 "description": "Run verify_check for page 374"
}
```


### [2026-09-07T20:34:21.195Z] TOOL RESULT

```
nodes verified: 12/12
node verdicts: {'plausible': 2, 'confirmed': 6, 'disputed': 4}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 9, 'contradicts': 1, 'not_checked': 3, 'partial': 1}
books consulted: {'partial': 11, 'supports': 12, 'silent': 5, 'contradicts': 3} | by book: {'KLN': 5, 'BRT': 4, 'WLD': 3, 'MON': 3, 'AHD': 3, 'KNT': 2, 'PHD': 2, 'SOD': 2, 'POK': 2, 'NYB': 1, 'HUB': 1, 'ARY': 1, 'LEW': 1, 'SKT': 1}
```


## [2026-09-07T20:34:29.404Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== SKT opera/option ==\"; grep -n -i \"Opera\\.\\|Option\\.\\|Optimism\\|Copy\\.\\|Office\\.\" SKT.txt | head -10; echo \"== LEW optio ==\"; grep -n \"optio\\|opto,\\|opus, -eris\\|optimus\" LEW_1910.txt | head -10",
 "description": "Grep Skeat and LEW for the Latin words"
}
```


### [2026-09-07T20:34:29.472Z] TOOL RESULT

```
== SKT opera/option ==
842:inopt,  foolish.  (F.-L.)  XVII  cent.- O.  V. ineptt,  —  h.iniptus^  improper,  foolish. —  L.  (>/•,  oot ;  and  aptus,  fit.  (Aliio  inapt^ from  m-.  notj  and  apt.)  And  see  Option. Aquatio.  (L.)  L.  aquaticui,  pertaiuiug to  water.— L.  otjua,  water.
6096:—  O.  F.  ex^mp/aire.m'h.  txemplarium,  late form  of  txtm/iar,  a  copy  (to  which  the mod.  E.  word  is  now  confomcd).  — L.  ex* tmptarii,  adj.,  serving  as  a  copy.  — U  tX' tmplum ;  see  enaomple  above.  Der.  tx- impiar-y  (  -  O.  F.  txtmplairt).
12796:optimism,  the  doctrine the  best.  (L.>     From  L.  oftim' best;  with  suffix   -ism  (Gk. 0P'ti-PHus  is  a  supcrl,  form  fn (i.  c.  choice) ;  cf.  optart,  to
20153:tritintvfr.    (Lt      One  of  thire  ■ os&ocialcd  in  an  office.     L.  |il.  trvim three  men,  evolved  Crooi  ibrs  (O.  pL  f
23361:ombel — nrobrell  a. unity — unit, nre— opera.
== LEW optio ==
```


## [2026-09-07T20:34:35.994Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -3 LEW_1910.txt; wc -l LEW_1910.txt; grep -n \"opus\" LEW_1910.txt | head -5",
 "description": "Inspect LEW file"
}
```


### [2026-09-07T20:34:36.064Z] TOOL RESULT

```
eae hee ne
ee
Duquesne University:
14865 LEW_1910.txt
```


## [2026-09-07T20:34:49.817Z] TOOL CALL #79: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json\np='data/verification/page-374.json'\nd=json.load(open(p,encoding='utf-8'))\ne=[x for x in d['entries'] if x['entry']==5][0]\nn6=[n for n in e['nodes'] if n['id']==6][0]\nn7=[n for n in e['nodes'] if n['id']==7][0]\nfor c in n6['consulted']:\n    if c['src']=='LEW':\n        c['where']=\"Walde, Lateinisches etymologisches Wörterbuch (LEW_1910.txt)\"\n        c['stance']=\"silent\"\n        c['note']=\"Not usable: the local OCR of Walde's Latin dictionary contains no searchable 'opus', 'optimus' or 'optio' (grep returns nothing), so the book could not be consulted directly. It is however the work Walde-Pokorny cross-refers to at this very point ('Vf. LEWb.2 u. ops, optimus, opus' under 1. op-, and optiō/opīnor under 2. op-), so its verdict is reflected indirectly in WLD above.\"\nfor c in n7['consulted']:\n    if c['src']=='SKT':\n        c['where']=\"Skeat, Concise Etymological Dictionary (SKT.txt line 12796, s.v. optimism)\"\n        c['stance']=\"contradicts\"\n        c['note']=\"The OCR is badly damaged but legible enough to show Skeat's position, which differs from both Nourai's and Watkins': 'optimism, the doctrine ... the best. (L.) From L. optim[us], best ... OP-ti-mus is a superl. form fr[om] op- (i.e. choice); cf. optare, to [choose]'. Skeat thus assigns even optimus to the 'choose' root, whereas Pokorny/Watkins/Walde-Pokorny assign optimus to op- 'work' ('the wealthiest') and only optiō to op- 'choose'. Recorded here as an older minority view; the other Skeat headwords (opera, copy, office) could not be extracted from this scan.\"\njson.dump(d,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=2)\nprint(\"written\")\nEOF\npython3 -m json.tool data/verification/page-374.json >/dev/null && python3 tools/verify_check.py 374",
 "description": "Correct LEW and SKT consulted notes"
}
```


### [2026-09-07T20:34:51.394Z] TOOL RESULT

```
written
nodes verified: 12/12
node verdicts: {'plausible': 2, 'confirmed': 6, 'disputed': 4}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 9, 'contradicts': 1, 'not_checked': 3, 'partial': 1}
books consulted: {'partial': 9, 'supports': 12, 'silent': 6, 'contradicts': 4} | by book: {'KLN': 5, 'BRT': 4, 'WLD': 3, 'MON': 3, 'AHD': 3, 'KNT': 2, 'PHD': 2, 'SOD': 2, 'POK': 2, 'NYB': 1, 'HUB': 1, 'ARY': 1, 'LEW': 1, 'SKT': 1}
```


## [2026-09-07T20:35:12.018Z] AGENT

Page 374 verified — `data/verification/page-374.json`, `verify_check.py 374` shows 0 PROBLEM lines (12/12 nodes).

**Counts** — roots: 2 confirmed (Ome, Op; the other 4 entries on the page are redirects). Nodes: 6 confirmed, 2 plausible, 4 disputed. Ref checks: 9 supports, 1 partial, 1 contradicts, 3 not_checked (nodes Nourai left unreferenced).

**Disputed**
- Op → Germanic *oft* (node 4): Nourai cites AHD, but Watkins files OFT/OFTEN under *upo* (Pok. 1106), not op-1; Pokorny 780 lists no Germanic "oft"; Klein "of uncertain origin"; Etymonline PGmc *ufta*, unknown origin.
- Op → English *often* (node 5): the oft→often step itself is fine; disputed only because it hangs from the wrong root.
- Op → Latin (node 6): *opus, optimus, co-op(ia), opi-facium* all confirmed by POK 780 / AHD / Klein — but **optiō** belongs to the homophonous root op-2 "to choose" (Pok. 781, WP I 176 f., Watkins op-2, de Vaan *h₃epeie-).
- Op → English (node 7): same issue, **option** only; opera/operate/maneuver/optimum/copy/office all confirmed from Klein.

**Plausible**
- Ome → Avestan node: *ama-* and *amayavā-* fully confirmed (Bartholomae, Buck p. 298, WP I 178); but *arša-ama* is not Avestan — it is the Old Persian name Aršāma-, and while Kent §1914 confirms the segmentation *arša-ama-*, he and Iranica/Schmitt gloss arša- as "male, hero" ("having a hero's strength"), not "bear" (Nourai follows Bartholomae's older reading, which Bartholomae himself footnotes as uncertain).
- Ome → Persian *Aršām*: Mo'in's Borhan p. 31 footnote says word-for-word what Nourai says ("مرکب از arsha بمعنی خرس و ama بمعنی زور"), so BQT:31 is exact; same "bear vs hero" caveat, plus the name is a modern revival of the OP name, not an inherited word.

**Notable ref hits**: HRN:111 is exact (Horn no. 503 derives xūb from Av. hvāpah-); SOD:6 and SOD:436 are both exactly right (Gharib entries 151 ʾmʾn "power ©Av. ama" and 10739 xwp "©<Av. hvapah"); BQT:31 confirmed from the cached page image; SYN:298 exact.

**No extraction errors found** — the JSON is faithful to the printed page; nothing for the owner to fix in `data/extracted/batch/page-374.json`. Two forms are Nourai's own normalisations rather than misreads: Avestan `amâ-yavâ` (attested form *amayavā-*) and bare `afnah` (attested only in *afnah-vant-*); `co-op` and `opi-facium` match AHD's and Klein's notation (*co-op-*, *opi-faciom*).

One dissent worth recording: Hübschmann (Pers. Stud. p. 57) rejects the xūb < hvāpah- derivation as phonologically impossible and proposes Skt. *su-vapus-*; modern sources (Wiktionary's Proto-Iranian *HhuHā́pah) side with Horn/Nourai, so the node stands confirmed. Seven web pages archived via `fetch_source.py`.
