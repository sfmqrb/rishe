# Verification process log — verify-page-445


## [2026-09-14T01:55:56.718Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 445 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-445.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-445.json. Write /home/sfmqrb/git/rishe/data/verification/page-445.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 445` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T01:55:57.788Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T01:55:58.526Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T01:55:58.586Z] TOOL RESULT

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


## [2026-09-14T01:55:59.026Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-445.txt"
}
```


### [2026-09-14T01:55:59.048Z] TOOL RESULT

```
1	=== PDF page 445 (book page 415) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Ser 1 : to flow  (refs POK:909)  PART 2
4	#1 (parent #0) [Indo-European] refs=POK:1003; KNT:205; IEC:1276 | Sreu, Sru : to flow ; Srěm : flow, running
5	  #2 (parent #1) [Avestan / Old Persian] refs=POK:1003; HRN:139 | rautah, raodah : river, flow ; raodaiti : flows
6	    #3 (parent #2) [Pahlavi] refs=MON | rôt 2 : river
7	      #4 (parent #3) [Persian] refs=BQT:969 | rŭd «رود ( رودخانه )» : river ; rŭd-bâr «رودبار» : riverside ☞Per 2
8	      #5 (parent #3) [Arabic] refs=VDQ:226 | rauza : land of rivers, garden | NOTE: PLA:138 derives it from Persian "raz: garden". See "Leudh".
9	        #6 (parent #5) [Persian] refs=MON | rowzeh «روضه» : garden
10	  #7 (parent #1) [Sogdian] refs=SOD:346 | rwt : river
11	  #8 (parent #1) [Avestan] refs=POK:1003 | ravan : river ; raonami : the rivers ; urvant, sru-vant : fluently
12	  #9 (parent #1) [Germanic] refs=AHD | strau-maz : stream
13	    #10 (parent #9) [English] refs=None | stream
14	  #11 (parent #1) [Greek] refs=AHD | rhein : to flow ; rheuma : stream ; rhutmos : rhyme
15	    #12 (parent #11) [French] refs=None | 
16	      #13 (parent #12) [Persian] refs=MON:1693,1701 | româtîsm «روماتیسم» : rheumatism ; rîtm «ریتم» : rhythm, rhyme
17	      #14 (parent #12) [English] refs=AHD | rheumatism, rhythm
18	    #15 (parent #11) [Latin] refs=None | 
19	      #16 (parent #15) [English] refs=AHD | diarrhea, hemorrhoid, rhyme
20	  #17 (parent #1) [Persian] refs=IEC:1276 | ram «رَم» : flight ; ramîdan «رمیدن» : to shy, to be scared | extra: رماندن ، رمانیدن ، رمیده ، رموک
21	
```


## [2026-09-14T01:56:01.813Z] TOOL CALL #3: Bash

```json
{
 "command": "python3 -m json.tool data/extracted/batch/page-445.json | head -200",
 "description": "Read source JSON for page 445"
}
```


## [2026-09-14T01:56:02.532Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-14T01:56:03.069Z] TOOL RESULT

```
{
    "pdf_page": 445,
    "book_page": 415,
    "entries": [
        {
            "root": {
                "name": "Ser 1",
                "lang": "Indo-European",
                "refs": "POK:909",
                "gloss": "to flow"
            },
            "part": 2,
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Indo-European",
                    "refs": "POK:1003; KNT:205; IEC:1276",
                    "words": [
                        {
                            "translit": "Sreu, Sru",
                            "gloss": "to flow",
                            "script": null
                        },
                        {
                            "translit": "Sr\u011bm",
                            "gloss": "flow, running",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 2,
                    "parent": 1,
                    "lang": "Avestan / Old Persian",
                    "refs": "POK:1003; HRN:139",
                    "words": [
                        {
                            "translit": "rautah, raodah",
                            "gloss": "river, flow",
                            "script": null
                        },
                        {
                            "translit": "raodaiti",
                            "gloss": "flows",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 3,
                    "parent": 2,
                    "lang": "Pahlavi",
                    "refs": "MON",
                    "words": [
                        {
                            "translit": "r\u00f4t 2",
                            "gloss": "river",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 4,
                    "parent": 3,
                    "lang": "Persian",
                    "refs": "BQT:969",
                    "words": [
                        {
                            "translit": "r\u016dd",
                            "gloss": "river",
                            "script": "\u0631\u0648\u062f ( \u0631\u0648\u062f\u062e\u0627\u0646\u0647 )"
                        },
                        {
                            "translit": "r\u016dd-b\u00e2r",
                            "gloss": "riverside",
                            "script": "\u0631\u0648\u062f\u0628\u0627\u0631",
                            "see": [
                                "Per 2"
                            ]
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 5,
                    "parent": 3,
                    "lang": "Arabic",
                    "refs": "VDQ:226",
                    "words": [
                        {
                            "translit": "rauza",
                            "gloss": "land of rivers, garden",
                            "script": null
                        }
                    ],
                    "note": "PLA:138 derives it from Persian \"raz: garden\". See \"Leudh\".",
                    "quote": null
                },
                {
                    "id": 6,
                    "parent": 5,
                    "lang": "Persian",
                    "refs": "MON",
                    "words": [
                        {
                            "translit": "rowzeh",
                            "gloss": "garden",
                            "script": "\u0631\u0648\u0636\u0647"
                        }
                    ],
                    "note": null,
                    "quote": {
                        "text": "\u0631\u0648\u0636\u0647\u0654 \u062e\u0644\u062f \u0628\u0631\u06cc\u0646 \u062e\u0644\u0648\u062a \u062f\u0631\u0648\u06cc\u0634\u0627\u0646\u0633\u062a - \u0645\u0627\u06cc\u0647\u0654 \u0645\u062d\u062a\u0634\u0645\u06cc \u062e\u062f\u0645\u062a \u062f\u0631\u0648\u06cc\u0634\u0627\u0646\u0633\u062a",
                        "poet": "H\u00e2fez"
                    }
                },
                {
                    "id": 7,
                    "parent": 1,
                    "lang": "Sogdian",
                    "refs": "SOD:346",
                    "words": [
                        {
                            "translit": "rwt",
                            "gloss": "river",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 8,
                    "parent": 1,
                    "lang": "Avestan",
                    "refs": "POK:1003",
                    "words": [
                        {
                            "translit": "ravan",
                            "gloss": "river",
                            "script": null
                        },
                        {
                            "translit": "raonami",
                            "gloss": "the rivers",
                            "script": null
                        },
                        {
                            "translit": "urvant, sru-vant",
                            "gloss": "fluently",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 9,
                    "parent": 1,
                    "lang": "Germanic",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "strau-maz",
                            "gloss": "stream",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 10,
                    "parent": 9,
                    "lang": "English",
                    "refs": null,
                    "words": [
                        {
                            "translit": "stream",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 11,
                    "parent": 1,
                    "lang": "Greek",
                    "refs": "AHD",
                    "words": [
```


### [2026-09-14T01:56:03.114Z] TOOL RESULT

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


## [2026-09-14T01:56:07.750Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -m json.tool data/extracted/batch/page-445.json | sed -n '200,400p'",
 "description": "Rest of source JSON"
}
```


### [2026-09-14T01:56:08.892Z] TOOL RESULT

```
                    "words": [
                        {
                            "translit": "rhein",
                            "gloss": "to flow",
                            "script": null
                        },
                        {
                            "translit": "rheuma",
                            "gloss": "stream",
                            "script": null
                        },
                        {
                            "translit": "rhutmos",
                            "gloss": "rhyme",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 12,
                    "parent": 11,
                    "lang": "French",
                    "refs": null,
                    "words": [],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 13,
                    "parent": 12,
                    "lang": "Persian",
                    "refs": "MON:1693,1701",
                    "words": [
                        {
                            "translit": "rom\u00e2t\u00eesm",
                            "gloss": "rheumatism",
                            "script": "\u0631\u0648\u0645\u0627\u062a\u06cc\u0633\u0645"
                        },
                        {
                            "translit": "r\u00eetm",
                            "gloss": "rhythm, rhyme",
                            "script": "\u0631\u06cc\u062a\u0645"
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 14,
                    "parent": 12,
                    "lang": "English",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "rheumatism, rhythm",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 15,
                    "parent": 11,
                    "lang": "Latin",
                    "refs": null,
                    "words": [],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 16,
                    "parent": 15,
                    "lang": "English",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "diarrhea, hemorrhoid, rhyme",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 17,
                    "parent": 1,
                    "lang": "Persian",
                    "refs": "IEC:1276",
                    "words": [
                        {
                            "translit": "ram",
                            "gloss": "flight",
                            "script": "\u0631\u064e\u0645"
                        },
                        {
                            "translit": "ram\u00eedan",
                            "gloss": "to shy, to be scared",
                            "script": "\u0631\u0645\u06cc\u062f\u0646"
                        }
                    ],
                    "script_extra": "\u0631\u0645\u0627\u0646\u062f\u0646 \u060c \u0631\u0645\u0627\u0646\u06cc\u062f\u0646 \u060c \u0631\u0645\u06cc\u062f\u0647 \u060c \u0631\u0645\u0648\u06a9",
                    "note": null,
                    "quote": {
                        "text": "\u062a\u0648 \u0622\u0646 \u0648\u062d\u0634\u06cc \u063a\u0632\u0627\u0644 \u0648 \u0647\u0631 \u0642\u062f\u0645 \u0627\u0632 \u0645\u0646 \u0631\u0645\u06cc\u062f\u0646\u0647\u0627 - \u0645\u0646 \u0648\u0627\u06cc\u0646 \u062f\u0634\u062a \u0628\u06cc \u067e\u0627\u06cc\u0627\u0646 \u0648\u0628\u06cc\u062d\u0627\u0635\u0644 \u062f\u0648\u06cc\u062f\u0646\u0647\u0627",
                        "poet": "H\u00e2tef Esfah\u00e2n\u00ee"
                    }
                }
            ]
        }
    ]
}
```


## [2026-09-14T01:56:09.815Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['POK','KNT','IEC','HRN','MON','BQT','VDQ','SOD','AHD','PLA','SYN','WLD','PHD','NYB','BRT','CHEUNG','ARY']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:600])\n    print()\n\"",
 "description": "Inspect refs_online entries"
}
```


### [2026-09-14T01:56:11.012Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

VDQ {"title": "Fereydun Badreh'i (tr.), Vazheha-ye Dakhil dar Qor'an-e Majid (Persian translation of Jeffery FVQ with notes), Toos 1372/1993", "kind": "website", "url": "https://noorlib.ir/book/view/12868?pageNumber=<N>&viewType=pdf (page images; viewType=html also exists) ; info: https://noorlib.ir/book/info/12868 ; ketabnak.com/book/51136 (download blocked)", "lookup_hint": "noorlib viewer is JavaScript-rendered (WebFetch/curl get only the site chrome); needs a browser. Since it is a translation of FVQ, verify the substance via FVQ (same entry order); page numbers differ.", "local_file": null, "

SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 lea

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

CHEUNG null

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it
```


## [2026-09-14T01:56:15.274Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['POK','KNT','IEC','SOD','HRN','BQT','MON']:\n    e=d[k]; print(k,'OFFSET:',e.get('page_offset')); print(' HINT:',e.get('lookup_hint')); print(' LOCAL:',e.get('local_file')); print()\n\"",
 "description": "Page offsets for key refs"
}
```


### [2026-09-14T01:56:16.996Z] TOOL RESULT

```
POK OFFSET: POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
 HINT: Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\data\ie\pokorny&root=config
 LOCAL: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt

KNT OFFSET: leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
 HINT: Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; section refs like '$147'. Nourai's page numbers should fall in 164-215 for lexicon citations.
 LOCAL: /home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt

IEC OFFSET: TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
 HINT: Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.
 LOCAL: /home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt

SOD OFFSET: printed page ≈ leaf − 66 in SOD_pages.txt (0-based \f blocks; 645 leaves; English intro precedes)
 HINT: Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/SogdianDictionary for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}
 LOCAL: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD.txt']

HRN OFFSET: leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
 HINT: Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.
 LOCAL: /home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt

BQT OFFSET: vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
 HINT: grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)
 LOCAL: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt']

MON OFFSET: None
 HINT: Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).
 LOCAL: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt']
```


## [2026-09-14T01:56:20.627Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n 'lemma: sreu' POK_full.txt; echo ---; grep -n 'lemma: ser-' POK_full.txt; echo ---; grep -n 'Page(s): 909\\|Page(s): 1003' POK_full.txt | head -20",
 "description": "Grep Pokorny full for sreu and ser"
}
```


### [2026-09-14T01:56:20.747Z] TOOL RESULT

```
80847:Root / lemma: sreup- 
80867:Root / lemma: sreu- 
---
73956:Root / lemma: ser-1 ( *ker- < *kel-) 
73996:Root / lemma: ser-2 
74030:Root / lemma: ser-3, sor- 
74054:Root / lemma: ser-4 
74093:Root / lemma: ser-5, extended serp- 
---
73919:Page(s): 909 
73937:Page(s): 909 
73994:Page(s): 909-910
```


## [2026-09-14T01:56:23.093Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '73900,74000p' POK_full.txt; echo ===SREU===; sed -n '80840,80920p' POK_full.txt",
 "description": "Print Pokorny ser- and sreu- entries"
}
```


### [2026-09-14T01:56:23.243Z] TOOL RESULT

```
Exit code 1
: Tulu e:l, Koraga eli, Kannada eeLu, Badaga iyyu, Kodagu ye:|u, Kurumba -o.lu, Tcxla ow, 
Kota ye:ye, Tamil aezhu, Malayalam e:lu, Irula elu 

Nahali 

Nahali sato 

Basque 

Basque zazpi 

Etruscan 

Etruscan+ semph 

Human 

Hurrian+ shindia 
References: WP. II 487. 
Page(s): 909 

Root / lemma: sep- 

Meaning: to care of smth.; to honour 

Material: Old Indie s4o5//"liebkost, umwirbt, pflegt, betreibt', Avestan hap- (2. 3. Sg. hafsT, 

haptl) "(in the Hand)halten, stijtzen'; gr. -snoj (with apcpi-, 5i-, £cp-, [jeG-, nspi-), Aor. sir-e- 

GTTOv, -ansTv " provide, supply, bereite, bearbeite'; ottAov n. "tool, appliance, weapon', 

ottAeoo "harness', onAopai "bereite mirto' etc.; 

in addition Indo Germanic *sepeljd\x\ Old Indie saparyat/ \enera\.ur', Latin sepe//d -Ire, 
sepu/tum^ bury' i.e. "venerari sepulcro'. 

References: WP. II 487, WH. II 517, Benveniste Origines 1, 47. 
Page(s): 909 



Root / lemma: serk- 

Meaning: hedge, to fence 

Material: Gr. I^koq, n. " paddock, corral, pen, fold, fence. Wall; loop, noose, snare, 

Fangnetz', opKavr) 'Umzaunung', opKoq m., opKiov 'oath'; 

Latin sarcio, -Tre' patch, mend, wiederherstellen', sarctus tectusiroxw a house "twisted 
and gedeckt, i.e. complete ', 5a/r//7a "bundle. Pack, tragbares baggage ', sartor 
"Flickschneider', Umbrian sars/fe "*sarcTte'; Hittite sar-n/n-k- 'ersetzen, compensate '. 

References: WP. II 502, WH. 478 f. 
Page(s):912 

Root / lemma: ser-1 ( *ker- < *kel-) 
Meaning: to flow 

Material: Old Indie sfsarti, sarati^ flows, hurries, jagt wornach, verfolgt'; fut. sarisyati, 
subjunctive s/sFrsat/irom a heavy basis *sera-, compare hom. pcbopai "budge me quick, 
fast, strong, stijrme an, hurry ' from *srd-/d; ein root nouns *srd, in addition Old Indie *sTr, 
*sfrah, is die base of a-stem Old Indie siraav\6 sTra^ Rinnsal, stream'; Old Indie sarfti. 
"stream, brook, river', sarana-' running ', sa-5/'-^-"stromend', sa-sr-'h " running, hurrying '; 
sarayu; sarayu-m. "name eines river', ap. Haraiva-, Avestan (Akk.) Haroyum, np. Hare^ 
river and region from Ugml '; 

Old Indie sarma-m. " das Flieften ', gr. oppn "Aniauf, attack, Drang after etwas', whereof 
oppau) "treibe an, rege an', intr. "stiJrme hence, worauf los'; in addition oppsvov " Salbei ' 
as "die Anreizende', s. Stromberg, Gr. Pflanzennamen 93; aipsoj " gripe, seize' instead of 
*aTpu) ( *Ser/d) through influence of aypsu) ds.; 

Old Indie sara- "fluid', sara "river, stream, brook', gr. 6p6(;, Latin serum^ the wasserige 
Teil the geronnenen milk, whey '; perhaps alb. gjize {*ser-dja) "gelabte milk, cheese'; 

thrak. PN Germ/sera "\Narmwasser', FIN litp[i\oq; French la Sermane{*Sermanna), 
northern Italy Sermenza ( *Sermentia), (under the influence of common Celtic -ns-, -nt- > - 
nrh), Venetic PN Sirmid{*Sermid), Pannonian PN Sirmium, poln. (Venetic) PN Srem 
{*Sermo-)\ lllyrian FIN Sa/77^s (Kampanien); gall. (Venetic-lllyrian) FIN Sara{*Sera), 
Saravus'd\e Saar'; Sar-b\\6et many FIN in the Lombardei, Switzerland and Frankreich, 
also appellative (Mantua sa/7ic>7" stream, brook' etc.); cymr. FIN Sdr{*Sora)\ sor- a\so in den 
FIN Old Prussian Sar-ape, Lithuanian-poln. Szar-upa, Latvian Sarija; 



Middle Irish sirid {* serTtI) "durchwandert, sucht heim, loots, verlangt', verbal noun siriud, 
cymr. herw {*ser-uo-) 'Landstreicherei', Middle Irish serb^ theft '; 

Lithuanian a/7S//Y/"unnzingeln', Latvian sirt^ umherschwarmen, Raubziige make ', sira 
(compare Old Indie sira) "Umherstreifer, beggar'. 

References: WP. II 497 f., WH. II 525, Schwyzer Gr. Gr. 1, 727^; in addition sreu-'i\o\N\ 
after E. Fraenkel Gl. 32, 33 here gr. psGsa 'nostril, nose', p60O(; "Wogenschwall', as well 
as pi(;, pTv6(; "nose' as "die Triefende'. 
Page(s): 909-910 

Root / lemma: ser-2 

Meaning: to guard, watch over, support 

Material: Avestan hara/t/"\r\as acht, schijtzt'; haurva/t/ds., /75^n/5-"beschutzend, hijtend' in 
(eval):1: ==SREU=== not found
```


## [2026-09-14T01:56:26.719Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '80845,80940p' POK_full.txt",
 "description": "Print Pokorny sreu entry"
}
```


### [2026-09-14T01:56:26.795Z] TOOL RESULT

```
Page(s): 1 002 

Root / lemma: sreup- 

Meaning: scabby, dirt 

Material: Gr. purroc; m. "smut, Unreinlichkeit', purrou), punaivw "sully', punapoq "dirty, 

filthy', punau) "bin dirty, filthy', puno(; n. "wheys', punraj "clean', Med. "wash myself, 

schneuze myself; proto Slavic. *strup-b (from *sreupos or *sroupos) "wound' (Old Church 

Slavic; actually "*scurf, scab auf the wound'), " poison, pus' (slov.), "scurf, scab' (New 

Bulgarian russ.), "skin rash by children' (Serbo-Croatian), " crust, scab, eschar ' (poln. 

Czech); ablaut. Church Slavic strbp-bth "roughness, hardness '. 

References: WP. II 703, Vasmer 3, 32. 

Page(s): 1 004 

Root / lemma: sreu- 

Meaning: to flow 

Material: Old Indie sravati^ flows ' (= gr. psw), srava-m. "das Flieften' (= gr. pooc;. Old 

Church Slavic o-sfrovb), g/r/srava ^Bergstrom' (= gr. por), Lithuanian srava), sm/^- flowing, 



geflossen' (= gr. puT6(; = fern. Lithuanian srutsr, zero grade Latvian strauts), srutf-i. "way, 
das Flieften' (= gr. puai(;, perhaps Armenianan/), sravat- f. 'river' (= gr. -pEFsT-nO. O'd 
Indie srotahu.. Old pers. rautah-v\., npers. rdd^nvef; causative s/'si/aya//" makes flow', 
srava-vn. " effluence '; 

Avestan (ravan-), Gen. PI. raon^m'the FliJsse', urvant- {sru-vant-) " flowing '; from 
einemo(/7)-present from (: gr. pu9-pi6(;?): Avestan raodaiti^ flows ', rao5ah-v\. "river', urud\. 
" river flow, bed' (Old Indie visruh-i. "stream' or likewise?); 

Armenian aroganem, oroganem^ wet ' {*srou-), compare Old Lithuanian srav/nu^make 
bluten'), probably also an/ "canal' {*srut/s or *sruios)\ 

gr. p£U) "flow' (Put. p£uoo|jai, Aor. Epidaur. s^sppua, Kalymna £[Y]-pug Konj. from 
*sruua-\ compare Lithuanian pasruvo "floft' from -at, usually *sreue- in sppunv, Lithuanian 
sravetr, to this beiden heavy base Old Indie Inf. sravitav§)\ p6o(; (Cypriot p6Fo(;), Attic pou(; 
m. "current, flood', nspi-ppooc; "rings umflossen' (also aijjo-pooq for expressed aijjoppoc;), 
pon (korkyr. Dat. PI. p/7oFaTaiv) "das Stromen, stream' (= Lithuanian srava), puT6(; " 
flowing, stromend', nspippuTOc; "rings umflossen' (= Old \r\d'\c par/sruta-), puaic;f. "das 
Stromen', pua(;, -a5o(; "rinnend', pu5r|v, hom. pu56vAdv. "in Uberfluft'; psupa n. "Stromen, 
river; surge '; aKaAa-ppEirri^ "gentle flowing ', pa9u-pp£iTr|c; "deep flowing ', Eu-ppeirri^ "rich 
flowing ', (*-pp£F£Tr|c;, compare Old Indie sravat-), as Ionian pssGpov, Attic psTGpov n. " 
river flow, riverbed ' from themat. *sreue- derive ; pu0fj6(;, Ionian pua|j6(; ("the wash of the 
waves of Meeres compared) regelmaftige Bewegung, rhythm '; thrak. iTpuiJOov river name, 
iTpupn town name; 

Old Irish sruaimmu. "river', abret. strum^ copia (lactis) ' (= gr. psuija, if not ablaut 
equally with Germanic *strauma-)\ but Old Irish sruth "river', cymr. ffrwde\.c., from *spru-tu- 
; compare Pokorny Celtica 3, 308 f.; 

Old High German stroum. Old English stream. Old Icelandic s//'5^/r7/'"stream' (: Latvian 
straume, poln. strumien); 

Lithuanian sraviu, sravet/{o\6 sravu) " mild flow, seep, drip', sraujas ^rasch flowing ', 
srava^6as Flieften, Menstruieren', srove, Latvian strave, straume 'stream', strauts 
"Regenbach, Stromschnelle', Lithuanian sruta 'Jauche'; Old Church Slavic struja 'currer\t', 
ostrovb "\s\ar\6' ("das Umflossene'), poln. 5/At//77/e/7 "stream, brook'; 

Indo Germanic sreu- is extension from ser- "flow'. 

References: WP. II 702 f., Trautmann 279 f.; Vasmer 2, 287; 3, 32. 



Page(s): 1 003 



Root / lemma: sreno- -a 

Meaning: body part (hip?) 

Material: Avestan rana- m. "the outer Teil of Oberschenkels, thigh', mp. np. ran^ thigh '; 

Lithuanian strenos^6\e loins, the cross'. 

References: WP. II 705. 

Page(s): 1 002 

Root / lemma: sng-, sngos- 

Meaning: cold, frost 

Material: Gr. pTyoc; n. "frost', pTvEU), Perf. m. present-meaning sppTva " freeze, shudder,
```


## [2026-09-14T01:56:51.399Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KNT p205 area: grep rautah ===\"; grep -n 'rautah\\|rauta-' KNT.txt | head -20; echo \"=== IEC srem/sreu ===\"; grep -n '^srem\\|^sreu\\|^srēm\\|srem-\\|sreumi\\|srevo' IEC.txt | head -30",
 "description": "Grep Kent and Mann"
}
```


### [2026-09-14T01:56:51.485Z] TOOL RESULT

```
=== KNT p205 area: grep rautah ===
=== IEC srem/sreu ===
17083:sreum- ‘flowing; flow, stream; pour’. Cf. sroum-, sru-, etc. WP II, 703 Gk. rheüima, n. ‘flood, current’; Alb. rrymë, f. ‘current’; Olr. sráaim, id. (*-eu- or *-ou-); Li. cf. (o-gde) sraumu0ó, gs: eps, m. id.; Gk. cf. rhéa, adv. ('easily', fr. *sreum). (W rhuf, m. 'gush' suggests a type *reum-, roum-)
17084:sreut- ‘flow’, etc. See srout-, sru-, etc. and next. Cf. also srüuó ' Skt. (e- or o-gde) srótas, n. “current, stream, artery’; Li. sraütas, m. id.
17085:sreuó, io ‘run, flow’; sreuos, à, io ‘stream, flow, current’. WP H, 703 Skt. srávami, v. id.; Av. (radical) Oru-, id.; Gk. rhéo, rhéwo, id.; Ir. sreabhaim, v. id.; W ffreuo, inf. ‘gush, spout’; OCS strujo, struiti, id.; Li. cf. sraviu, ēti, v. and sroviu, ēti, v. id. Nominal types in Skt. sravab, adj. ‘running, flowing’; m. ‘flow’; Arm. (ambig.) aru, gs: ařvi, ab. s. -vav, s. ‘stream, channel’; Gk. rhéos, n. id.; Alb. cf. rrua, gs: rroi, m. (“water- course’, perh. a LW); Olr. sreb, srib, Ir. sreabh, f. stream": W ffrau, pl. ffreuon, f. ‘gush’;
```


## [2026-09-14T01:56:53.161Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD sreu ===\"; grep -n -i 'sreu' AHD_watkins1985.txt | head -30; echo \"=== AHD ser flow ===\"; grep -n -i '^ser-\\|straumaz' AHD_watkins1985.txt | head -20",
 "description": "Grep AHD Watkins"
}
```


### [2026-09-14T01:56:53.239Z] TOOL RESULT

```
=== AHD sreu ===
897:reu-2, Also reue-. To smash, knock down, tear out, dig up, uproot. 1. Suffixed o-grade form *rous-o- in Ger- manic *rawwa- in: a. Old Norse régg, réggr, woven tuft of wool: RAG}; b. Norwegian rugga, rogga, coarse cover- let, akin to the Scandinavian source of RUG. 2. Basic form *reu- in Latin ruere, to collapse, cause to collapse: RABBLE, RUIN. [Pok. 2. reu- 868.] reudh-', Red, ruddy. I. O-grade form *roudh-. 1. Ger- manic “raudaz in: a. Old English réad, red: RED; b. Old Norse rauthr, red (> reythr, rorqual): RORQUAL. 2. Ger- manic *raudnia- in Old Norse reynir, mountain ash, rowan (from its red berries), akin to the source of ROWAN. 3. Latin rijfus (of dialectal Italic origin), reddish: RUFES- CENT, RUFOUS. 4. Latin rdbus, red, in robigd, ribigo, rust: RUBIGINOUS. 5. Latin rdbur, rdbus, red oak, hard- ness, and rdbustus, strong: ROBLE, ROBORANT, ROBUST; CORROBORATE, RAMBUNCTIOUS. II. Zero-grade form *rudh-. 1. Form *rudh-d- in Germanic *rud6 in: a. Old English rudu, red color: RUDDLE, RUDDY; b. Old English rudduc, robin: RUDDOCK. 2. Suffixed form *rudh-sto- in Germanic *riist- in Old English rdst, rust: RusT. 3. Latin rubeus, red: ROUGE, RUBEOLA, RUBY; RUBEFACIENT 4. Latin rubicundus, red, ruddy: RUBICUND. 5. Latin rubidus, red: RUBIDIUM. 6. Suffixed (stative) form *rudh-é- in Latin rubére, to be red: RUBESCENT; ERUBES- CENCE. 7. Suffixed form *rudh-ro- in: a. Latin ruber, red: RUBELLA, RUBRIC; BILIRUBIN; b. Latin rutilus, reddish: RUTILANT; Cc. Greek eruthros, red (with pro- thetic vowel, from oldest root form *sreudh-): ERY- THEMA, ERYTHRO-; d. possibly remade Greek erusi-, red, reddening: ERYSIPELAS. 8. Suffixed form *rudh-to- in Latin russus, red: RISSOLE, ROUX, RUSSET. [Pok. reudh- 872.] reudh-2, To clear land. 1. Suffixed zero-grade form *rudh-yo- in Germanic *rudjan in Old Norse rydhja, to clear land: RID. 2. Possibly Germanic expressive variant *rudd- stick, club, in Old English rodd, stick: Rop. [In Pok. 2. reu- 868.] reue-. To open; space. 1. Suffixed variant form *ri-mo- (< *rua-mo-) in Germanic *riimaz in: a. Old English rim, space: ROOM; b. Old French run, ship’s hold, space: RUMMAGE. 2. Suffixed form *reu(g)-es- in Latin ris, “open land,” the country: RURAL, RUSTIC. [Pok. reuo-, ri- 874.] reug-. To vomit, belch, smoke, cloud. 1. Germanic *reu- kan in Old English réocan, to smoke, reek: REEK. 2. Suf- fixed zero-grade form *rug-to- in Latin ructdre, to belch: ERUCT. [Pok. 4. reu- 871.] reugh-men-. Cream. O-grade form *roughmen- in Ger- manic *rau(g)ma- in Middle Low German rém(e), cream: RAMEKIN. [Pok. reugh-m(e)n- 873.] reup-. Also reub-. To snatch. I. Basic form *reub- in Germanic *rupja in Flemish rippen, to rip: RIP!. II. O-grade form *roup-. 1. Germanic *raufjan in: a. Old English réafian, to plunder: REAVE!; b. Old English beréafian, to take away (be-, bi-, intensive prefix; see ambhi): BEREAVE. 2. Germanic *raubén, to rob, in: a. Middle Dutch and Middle Low German réven, to rob: ROVER; b. Old French rober, to rob: ROB; c. Italian rubare, to rob: RUBATO. 3. Germanic *raubd, booty, in Old French robe, robe (> “clothes taken as booty”): ROBE. 4. Suffixed form *roup-tro- in Sanskrit loptram, booty, from lumpati, he breaks, removes: LOOT. III. Zero-grade form *rup-. 1. Latin dsirpdre (< *isu- rup-; isus, use, usage, from iti, to use), originally “to interrupt the orderly aquisition of something by the act of using,” whence to take into use, usurp: USURP. 2. Na- salized form *ru-m-p- in Latin rumpere, to break (> riipés, rock): ROUT!, RUPTURE; ABRUPT, BANKRUPT, CORRUPT, DISRUPT, ERUPT, INTERRUPT, IRRUPT, RUPICO- Lous. [Pok. 2. reu- 868.] rezg-. To plait, weave, wind. Germanic *ruski- in Old English risc, rysc, rush: RUSH?. [Pok. rezg- 874.] [risan. To rise. Germanic word. 1. Germanic *risan in:
995:spit!. 2. Germanic *speiw- in Old English spiwan, spio- wan, to spew: SPEW. 3. Germanic *spait- in Old English spatl, spittle: sPITTLE. 4. Germanic *spiit- in: a. Middle English spouten, to spout forth: spout; b. Dutch sputte- ren, to sputter, akin to the probable Low German source of SPUTTER. 5. Zero-grade form *spu- in Latin spuere, to spit: SPUTUM; CUSPIDOR. 6. Zero-grade form *(s)pyu- in Greek ptuein, to spit: HEMOPTYSIS, PTYALIN. [Pok. (s)p(hjieu- 999.] srebh-. To suck, absorb. Zero-grade form *srbh- in: a. Germanic *surp- in altered form in Dutch slurpen, to slurp, lap: SLURP; b. suffixed form *srbh-é- in Latin sorbére, to suck: ABSORB, ADSORB, RESORB. [Pok. srebh- 1001.] srenk-. To snore. O-grade form *sronk- in: a. Greek rhonkos, rhonkhos, a snoring: RHONCHUS; b. Greek rhunkhos, snout, bill, beak: RHYNCHOCEPHALIAN. [Pok. srenk- 1002.] sreu-. To flow. 1. Suffixed o-grade form *srou-mo- in Germanic *straumaz, stream, in: a. Old English stréam, stream: STREAM; b. Dutch stroom, stream: MAELSTROM. 2. Basic form *sreu- in: a. Greek rhein, to flow: RHEO-, -RRHEA; CATARRH, DIARRHEA, HEMORRHOID, RHYOLITE; b. suffixed form *sreu-mn in Greek rheuma, stream, humor of the body: RHEUM. 3. Suffixed zero-grade form *sru-dhmo- in Greek rhuthmos, measure, recurring mo- tion, rhythm: RHYME, RHYTHM. [Pok. sreu- 1003.]
1336:CASE2 kap- CASHIER kes-2 CASTE kes-? CASTIGATE kes-2 CASTLE kes-2 CASTRATE kes-2 CATA- kat-1 CATABOLISM gWele-1 CATACHRESIS gher-5 CATACLYSM kleu-2 CATALECTIC slég- CATALEPSY (s)lag¥- CATALOGUE leg-1 CATALYSIS leu-1 CATAMENIA mé-2 CATAPLEXY plak-2 CATAPULT pél- CATARRH sreu- CATASTASIS sta- CATASTROPHE streb(h)- CATCH kap- CATCHPOLE pau- CATECHIZE (s)wagh- CATEGORY ger-1 CATER-CORNERED kWetwer- CATERPILLAR pilo- CATHEDRA sed-1 CATHEPSIN kat-1 CATHETER yé- CATHODE sed-2 CATHOLIC sol- CATION ei-1 CATOPTRIC okw- CATTLE kaput CAUDILLO kaput CAUDLE kele-1 CAULESCENT kaul- CAULICLE kaul- CAULIFLOWER _bhel-3, kaul- CAULINE kaul- CAUSTIC kéu- CAUTERY kéu- CAUTION keue-1 CAVE keue-2 CAVEAT keue-1 CAVERN keue-2 CAVETTO keue-2 CAVIL  kel-8
1424:DEVANAGARI deiw- DEVASTATE eu-2 DEVEST wes-4 DEvi deiw- DEVIATE wegh- DEVIL gWele-! DEVIOUS wegh- DEVISE weidh- DEVOID eu-2 DEVOIR ghabh- DEVOLVE wel-3 DEVOTE weg¥h- DEVOUR gWera-4 DEVOUT weg*h- DEW dheu-2 DEXTER deks- DEXTERITY deks- DEXTRO- deks- DEXTRORSE_ wer-3 DHARMA dher-2 DI-!_ dwo- DIABASE gWa- DIABETES gWa- DIABOLIC gWela-1 DIACRITICAL krel- DIADEM dé- DIAGNOSIS gnd- DIAGONAL genu-! DIAGRAM gerbh- DIAL deiw- DIALECT leg-1 DIALOGUE leg-1 DIALYsIs_leu-1 DIAMETER mé-2 DIAMOND deme-2 Diana deiw- DIANTHUS andh- DIAPASON pant- DIAPAUSE paus- DIAPEDESIS ped-1 DIAPHANOUS bha-1 DIAPHORESIS bher-1 DIAPHRAGM bhrekw- DIAPHYsIS bheue- DIARRHEA sreu- DIARTHROSIS ar- DIARY deiw- Diaspora sper-4 DIASTASIS sta- DIASTOLE stel- DIASTROPHISM_streb(h)- DIATESSARON kWetwer- DIATHESIS dhé-1 DIATOM tem- DIATRIBE tere-1 DIAZO = gWei- DICAST deik- DICENTRA kent- DICHASIUM dwo- DICHO- dwo- DICHOTOMY tem- DICKER dekm DICLINOUS  klei- DICROTISM kret-2 DICTATE deik- DICTION deik- DICTUM deik- DIDACTIC dens-! DIDAPPER dub- DIDYMIUM dwo- DIDYMOUS dwo- DIE! dheu-3 DIE? dé-
1595:HEM! kem-2 HEMATOCRIT krei- HEMERALOPIA amer- HEMI- sémi- HEMISTICH  steigh- HEMOPTYSIS spyeuU- HEMORRHOID sreu- HEMP kannabis
1791:MADAM deme-! MADAME deme-1 MADDER! modhro- MADEMOISELLE deme-1 MADONNA deme-1 MADREPORE miater- MADURO ma-1 MAELSTROM mele-, sreu- MAENAD men-! MAESTOSO meg- MAESTRO meg-
2181:RETE era-2 RETIARY era-2 RETICENT tak-1 RETICLE era-2 RETICULE ere-2 RETIFORM ere-2 RETINA era-2 RETINACULUM  ten- RETORT! terkw- RETRACT tragh- RETRAL re- RETRIEVE trep-2 RETRO- re- RETROACTIVE ag- RETROCEDE ked- RETROGRADE ghredh- RETROGRESS ghredh- RETRORSE wer-3 RETROSPECT spek- RETURN tera-1 RETUSE (s)teu- REVEAL weg-1 REVEILLE weg-2 REVEL duellum REVENANT gWa- REVENGE deik- REVENUE gWa- REVERBERATE wer-3 REVERE! wer-4 REVERT wer-3 REVEST wes-4 REVIEW weid- REVIVE gWei- REVOKE wekw- REVOLVE wel-3 REVULSION wel-4 REWARD wer-4 RHABDOMANCY wer-3 RHABDOVIRUS wer-3 RHAPSODY wed-2, wer-3 RHEO- sreu- RHETOR wer-6 RHEUM sreu- RHINOCEROS ker-1 RHIZO- wrad- RHIZOBIUM gWei- RHIZOME wrad- RHODIUM wrod- RHODO- wrod- RHODOCHROSITE ghréu- RHODODENDRON deru RHODOPSIN OkW- RHOMBUS_ wer-3 RHONCHUS  srenk- RHYME sreu- RHYNCHOCEPHALIAN srenk- RHYOLITE sreu- RHYTHM = sreu-
2200:ROW? era-1 ROWAN reudh-! ROWEL ret- ROWEN wel-2 ROYAL reg-! -RRHAGIA wrég- -RRHEA sreu- RUBATO reup- RUBEFACIENT dhé-1, reudh-1
2319:STOVE! staup- sTow sta- STRABISMUS streb(h)- STRABOTOMY streb(h)- STRAIN! | streig- STRAIN?  ster-2 STRAIT  streig- STRANGE eghs STRANGLE strenk- STRANGLEs  strenk- STRANGULATE _ strenk- STRANGURY strenk- STRATAGEM ag-, ster-2 STRATH ster-2 STRATOCRACY  ster-2 STRATUS  ster-2 STRAW ster-2 STREAK streig- STREAM sreu- STREET  ster-2 STRENGTH  strenk- STREPTO-  streb(h)- STREPTOMYCES meug-2 STREPTOMYCIN meug-2 STREPTOTHRICIN  thrix STREUSEL ster-2 STREW ster-2
=== AHD ser flow ===
924:ser-1, To protect. 1. Extended form *serw- in Latin serudre, to keep, preserve: CONSERVE, OBSERVE, PRE- SERVE, RESERVE, (RESERVOIR). 2. Suffixed length- ened-grade form *sér-6s- perhaps in Greek hérés, “protector,” hero: HERO. [Pok. 2. ser- 910.]
925:ser-?, To flow. 1. Suffixed form *ser-o- in Latin serum, whey: SERAC, SERUM. 2. Basic form *ser- in Sanskrit sarati, sasarti, it flows, it runs: SAMSARA. 3. Extended roots *sr-edh-, *sr-et-, to whirl, bubble, in Germanic *stred- in Old High German stredan, to whirl, swirl, whence ablaut formation in Middle High German séru- del, whirlpool: STRUDEL. [Pok. 1. ser- 909; sr-edh- 1001.]
926:ser-3, To line up. 1. Latin serere, to arrange, attach, join (in speech), discuss: SERIES, SERTULARIAN; ASSERT, DESERT’, DISSERTATE, EXERT, INSERT. 2. Suffixed form *ser-mon- in Latin sermé (stem sermé6n-), speech, dis- course: SERMON. 3. Suffixed form *ser-d- perhaps in Latin sera, a lock, bolt, bar (? < “that which aligns”): SEAR?, (SERRIED). 4. Suffixed zero-grade form *sr-t- in Latin sors (stem sort-), lot, fortune (probably from the lining up of lots before drawing): SORCERER, SORT; ASSORT, CONSORT, SORTILEGE. [Pok. 4. ser- 911.]
995:spit!. 2. Germanic *speiw- in Old English spiwan, spio- wan, to spew: SPEW. 3. Germanic *spait- in Old English spatl, spittle: sPITTLE. 4. Germanic *spiit- in: a. Middle English spouten, to spout forth: spout; b. Dutch sputte- ren, to sputter, akin to the probable Low German source of SPUTTER. 5. Zero-grade form *spu- in Latin spuere, to spit: SPUTUM; CUSPIDOR. 6. Zero-grade form *(s)pyu- in Greek ptuein, to spit: HEMOPTYSIS, PTYALIN. [Pok. (s)p(hjieu- 999.] srebh-. To suck, absorb. Zero-grade form *srbh- in: a. Germanic *surp- in altered form in Dutch slurpen, to slurp, lap: SLURP; b. suffixed form *srbh-é- in Latin sorbére, to suck: ABSORB, ADSORB, RESORB. [Pok. srebh- 1001.] srenk-. To snore. O-grade form *sronk- in: a. Greek rhonkos, rhonkhos, a snoring: RHONCHUS; b. Greek rhunkhos, snout, bill, beak: RHYNCHOCEPHALIAN. [Pok. srenk- 1002.] sreu-. To flow. 1. Suffixed o-grade form *srou-mo- in Germanic *straumaz, stream, in: a. Old English stréam, stream: STREAM; b. Dutch stroom, stream: MAELSTROM. 2. Basic form *sreu- in: a. Greek rhein, to flow: RHEO-, -RRHEA; CATARRH, DIARRHEA, HEMORRHOID, RHYOLITE; b. suffixed form *sreu-mn in Greek rheuma, stream, humor of the body: RHEUM. 3. Suffixed zero-grade form *sru-dhmo- in Greek rhuthmos, measure, recurring mo- tion, rhythm: RHYME, RHYTHM. [Pok. sreu- 1003.]
```


## [2026-09-14T01:57:05.689Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==221' KNT.txt | head -60",
 "description": "Print Kent leaf 220 (printed 205)"
}
```


### [2026-09-14T01:57:07.210Z] TOOL RESULT

```
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
```


## [2026-09-14T01:57:07.625Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\n# find leaf containing 'sreum-'\nfor i,p in enumerate(pages):\n    if 'sreum-' in p or 'sreuō' in p:\n        print('LEAF',i)\n        print(p[:3000])\n        break\nEOF",
 "description": "Find Mann sreum leaf"
}
```


### [2026-09-14T01:57:09.384Z] TOOL RESULT

```
LEAF 704
cipice’; cf. stremit'sa, v. ‘rush, gush’; stremglàv ‘headfirst’
sren- ‘loin, kidney’. Cf. rénos, is Lat. rén, gs: rénis, m. ‘kidney’; Li. dial. srénos, usu. strenos, fpi. ‘loins, waist'. (NB. The initial str- is characteristic of Latv., where the wd. does not occur).
(srep-, improbable reconstruction for (1) strep-, (2) urep-, q. v.)
sret- “spread, expand, spill, flood”. (variant: stret- ? for OCor. and OHG). Ir. sreathaim, v. *spread; shed'; (OCor. stret, Cor. streth, pl. ow, f. ‘stream, flow? conflicts w. phonol., since sr- normally Cor. & W fr-, ffr-); OHG str&dan, sv. ‘well up, spurt’; (uncertainly Gk. rheità, npl. ‘streams’, preferably fr. *sreuito)
sreum- ‘flowing; flow, stream; pour’. Cf. sroum-, sru-, etc. WP II, 703 Gk. rheüima, n. ‘flood, current’; Alb. rrymë, f. ‘current’; Olr. sráaim, id. (*-eu- or *-ou-); Li. cf. (o-gde) sraumu0ó, gs: eps, m. id.; Gk. cf. rhéa, adv. ('easily', fr. *sreum). (W rhuf, m. 'gush' suggests a type *reum-, roum-)
sreut- ‘flow’, etc. See srout-, sru-, etc. and next. Cf. also srüuó ' Skt. (e- or o-gde) srótas, n. “current, stream, artery’; Li. sraütas, m. id.
sreuó, io ‘run, flow’; sreuos, à, io ‘stream, flow, current’. WP H, 703 Skt. srávami, v. id.; Av. (radical) Oru-, id.; Gk. rhéo, rhéwo, id.; Ir. sreabhaim, v. id.; W ffreuo, inf. ‘gush, spout’; OCS strujo, struiti, id.; Li. cf. sraviu, ēti, v. and sroviu, ēti, v. id. Nominal types in Skt. sravab, adj. ‘running, flowing’; m. ‘flow’; Arm. (ambig.) aru, gs: ařvi, ab. s. -vav, s. ‘stream, channel’; Gk. rhéos, n. id.; Alb. cf. rrua, gs: rroi, m. (“water- course’, perh. a LW); Olr. sreb, srib, Ir. sreabh, f. stream": W ffrau, pl. ffreuon, f. ‘gush’;
1277
adj. (flowing! (but W rhewin ‘drain, gutter’ is from a type *reu-); Li. (o-gde) sraujà beside (e-gde) sriaujà, f. ‘stream’; sravà, f. id.; sraujùs, adj. ‘flowing’; Latv. (o-gde) strauja, f. ‘current’
srig- ‘flow’ Lat. cf. riguus, adj. ‘watery’; rigo, are, v. ‘water’; Ir. dial. striog, f. ('driblet, for *sriog) (?); R streZà, f. “current, rapid, water- way’; Ukr. cf. stryhavka, f. ‘swamp’. (Potential isophone in Latv. strigt, inf. rank)
srīĝ- “feel cold, shiver’. WP II, 705. (Variant: ri-) Oss. rizin, Dig. rezun, inf. id.; Per. cf. ariz, s. *hoarfrost; Gk. rhigéo, v. ‘shiver’; Lat. (in- tensive fr- for initial r-) frigeo, ere, v. id. (cf. Supt: srág- “berry? for analogy) beside rígeo, ere, v. id. (and 'stiffen); OW, W cf. rhynn, rh?$n, adj. ‘shivering’; m. ‘shiver’ (for expected *ffrynn, fr. *rigno- beside *srigno-); Cor. rynny, inf. ‘shiver’; Cz. stříž(e), f. “newly formed ice; Slovene srež, m. 'hoarfrost. Nominal types include Gk. rhigos, n. “cold; shudder’; Lat. frigus, gs: ons, n. id. beside rígor, oris, m. ‘stiff cold"; Br. frimm, m. (“hoar- frost', fr. *srigmo-. Fr. frimas is of ambig, origin); cf. also Cz. stříž-aha ‘dry frost; Pol. $rezoga “haze?
(srik- ‘rub’, see Supt: S)
srin- (sris-) “nose; headland”; Cf. WP I, 140 Gk. hus gs: rhinós, f. ‘nose’; cf. rhíon, n. “headland”; Br. fri, pl. friu, m. ‘nose’;
```


## [2026-09-14T01:57:18.196Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(pages[704][3000:9000])\nEOF\necho \"=== grep srem in IEC ===\"; grep -n 'srem' IEC.txt | head",
 "description": "Full IEC leaf 704 + grep srem"
}
```


### [2026-09-14T01:57:19.481Z] TOOL RESULT

```
Cor. ryn, pl. -yow, and rün, pl. -yow, m. “head- land”; rynen and rünen, f. ‘hillock’
srisà, srisnà “file, saw’. (onomat.) Per. arrah, id.; Oss. xirx, Dig. xirxá, s. ‘saw’; Kurd. ere, id.; Gk. hung f. ‘file’; Lat. serra, f. ‘saw’. (Phonol. of cerrus & Plautine terr ‘3 times', cf. terni, cerno, etc.)
srübh- (one of several variants in sense of ‘sup, slurp’. Cf. srebh-, srubh-, srb-, sorb-, surb-, etc.). (Onomat.) Gk. rhopháo, rhophéo, v. id.; Li. sruobiù & sriuobiü, ^ti, id.; cf. sr(ijuobalas, m. ‘soup’
(srodh-, o-gde of type sredh- ‘run, flow
=== grep srem in IEC ===
```


## [2026-09-14T01:57:28.262Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN leaf 160 (p.139) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==161' HRN.txt | head -70",
 "description": "Horn p.139"
}
```


### [2026-09-14T01:57:29.232Z] TOOL RESULT

```
=== HRN leaf 160 (p.139) ===
- 139 -
624. {2)renff *Bergschaaf* (Vis und RäniTn, S. 144 Vers 13,
245 Vers 2 v. u.; Scliefer, Chrest. pers. 11, 249,
17 «.).
skr. ranku- *eine Art Antilope' (Nöldeke, münd-
liche Mitteilung).
625. revän 'Seele'.
aw. urvan- (d. i. tiruvan') *Seele*; phlv. riivän (ge-
schrieben )X2n), ruvdmk.
626. robäh *Fuchs'.
g. rüwüs *Fuchs (Semn. rüwä *Katze').
aw. raopis (?) ; plilv. röpäs, röbas ; ai. löpa^d- (skr.
lopäka- 'Art Schakal') *Fuchs'; arm. a)Me8 *Fuchs'
(Hübschmann No. 9).
Verg]. Bartholomae, Bß. 10, 294, der gr. dhimfj^
für ein Lehnwort hält; ebenso G. Meyer, Indog.
Forsch. I, 328 Anm.
kurd. rüwi 'Fuchs'; oss. d. robas, t. rübas (215);
bei. ropask (323; röba LW.); sar. rapc.
627. röd *Fluss', rödbar^ röd/ßne.
Kas. K.Z. röxönd^ rö/önS.
ap. rautah' Tluss'; phlv. röt, rötbar (Bund.); ai.
sr6tas- 'Strömung, Strombett, Strom, Fluss'.
kurd. rö; bei. röt (330).
628. rüde {*röde) 'Eingeweide'.
Käs. rävd, rüvS.
phlv. rötlk 'Eingeweide* (AV.).
kurd. rum; bei. rö^, rös (331); sar. raud.
Das neupersische Wort muss dem Bai. und Sar. zu
Folge auch ursprünglich einen Majhülvokal gehabt
haben ^).
629. rö^ (röj) 'Tag', rdzäne, rözgär (lX:i^Tn, Is. 1, 1), rö^e,
rözT (arab. LW. rizq-),
g. rüj.
^) von Staokelberg, Fünf ossetische Erzählungen, 83 ver-
gleicht 088. (t.) rüd 'Wurst'.
2) Wohl zuerst erkannt von Rückert, ZDMO. 10, 279.
```


## [2026-09-14T01:57:29.603Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== CHEUNG ram ===\"; grep -n 'ramīdan\\|ramidan\\|rēm\\|\\*ram' CHEUNG.txt | head -40",
 "description": "Cheung on ram"
}
```


### [2026-09-14T01:57:29.761Z] TOOL RESULT

```
=== CHEUNG ram ===
7843:*NWIR: NP giramidan/giram- (denomin.) ‘to honour, respect’, NP girami ‘treasured, 
12619:*Har'), similar to *ram, whose IE credentials cannot be established either. 
13018:*NWIR: NP ramis ‘rest, tranquillity’ || (+ *a-) NP aramidan/aram- ‘to become calm, 
20489:312 *ram 
20499:*ram ‘to go, move’ 
20523:*NWIR: NP ramidan/ram- ‘to be afraid, terrified; to flee in terror’ (or Pth. LW *hram- 
29027:*NWIR: NP xiramidan ‘to stride’ 
40757:aramidan/aram-, 191 
41030:giramidan/giram-, 107 
41359:ramidan/ram-, 312 
41650:xiramidan, 449 
55622:*baiH, *pau, *ram (s.v.), 
55903:*dais’ (s.v.), *harc, *ram 
56587:*baiH, *pau, *ram (s.v.), 
56742:*iat, *ram, *uraj, *xar, 
57227:*miHu, *nau, *ram, *suaH, 
58257:*man (s.v.), *ram (S.V.),
```


## [2026-09-14T01:57:34.850Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '20489,20570p' CHEUNG.txt",
 "description": "Cheung *ram entry"
}
```


### [2026-09-14T01:57:34.902Z] TOOL RESULT

```
312 *ram 


*PIE— > LIV: — | Pok.: 


*IE COGNATES: — 
*REFERENCES: EVP: 65; Henning, Cosmog.: 309, ad 32; NEVP: 71; Shahbakhsh: s.v. réz- 


*ram ‘to go, move’ 

*MIDDLE PERSIAN: (+ *ati- or *fra-) MMP ’hr’m-, BMP ’hl’m- /ahram-/ (orig. caus.) 
‘to lift up, raise’ || (+ *ni-) MMP nyr’m- ‘to cast, throw down’. ç MMP "hr'm-, BMP 
*hl’m- /ahram-/ are from Pth. or just from an unspecified Wir. dialect ? On the initial 
"h- cf. Sundermann, CLI: 106 f. Differently Ghilain: < *ati-°. However the form 
BMP ’hl’mydyt /ahramiyéd/, connected by Nyberg 1974: 11b to MMP ’hr’m-, can 
also be interpreted differently: /axramed/ ‘he strides’, s.v. *xrämH. > DMMPP: 34b 
f., 253a 

(+ *ati- or *fra-) Pres.: IND. 3sg. MMP "hr'myd, ’hr’m<y>d, MMP (in Sogd.) ’xr’myd, SUBJ. 3sg. MMP 
*hr’m’d, 3р1. MMP ’hr’m’nd, IMPV. 25р. MMP ’hr’m; Partic.: perf. pass. supplet. MMP рі ’hr’pt, 
*hr’ ft, Inf.: MMP ’hr’ptn, ’hr’ptn || (+ *ni-) Pres.: IND. 3sg. MMP nyr’myy, SUBJ. 3sg. MMP nyr’m’d, 
IMPV. 2sg. MMP nyr’m; Partic.: pres. MMP nyr’m’g, perf. pass. MMP nyr’pt, nyr’pt 

*PARTHIAN: (+ *fra-) 'hr'm- (orig. caus.) ‘to lift up, raise’ || (+ *ni-) n(y)r’m- ‘to 
hold back, restrain, suppress’ = Ghilain: 73 | DMMPP: 35a, 253a 

(+ *fra-) Partic.: perf. pass. П "hr'm'd || (+ *ni-) Pres.: IND. 35р. nyr’myd, 3р1. “nr’mynd, SUBJ. 2sg. 
nyr’m’, IMPV. 2pl. nyr’myd 

*KHOTANESE: (+ *ati-) t(t)ram- ‘to cross over; enter’ || (+ *ni-) naram- ‘to go out’ || 
(+ *pati-) LKh. param- ‘to grasp, understand’ — SGS: 40, 49, 73 

*NWIR: NP ramidan/ram- ‘to be afraid, terrified; to flee in terror’ (or Pth. LW *hram- 
< *@ram ?), Bal. ranbit/ranb-, ram(b)it/ram(b)- ‘to shy, become startled, run, rush, 
uproot’ (-b- < *Hrab/f'), Kurd. (Kurm.) rav-/ravin, (Sor.) faw- ‘to run away, flee; 
[Sul.] to be scared’, Gur. (Kand.) rämä-/-räm- ‘to run (away), flee’, Abz. ram kar- 
‘to flee, save oneself? (< *Oram ?) 

*NEIR: (+ *ati-) ? Pash. drümedol ‘to go’ (alternatively from *dram) || (+ *upa-) M. 
varém-/varemd ‘to stand’ (Zarubin) 

*MISC: Par. ram-/rami ‘to go round’, (caus.) Par. rém- (supplet.?) rhant ‘to turn’ 

No IE etymology can be suggested, it may be a blend of similar roots of motion, 
e.g. *Har! or *Hran and *gam. 

“PIE LIV: — | Pok.: 

*REFERENCES: EVP: 22; IIFL I: 284b; IIFL II: 259b; KPF II: 201 f.; Cabolov 1997: 71; Lecoq 2002: 
601a; Shahbakhsh: s.v. ram(b)- 


*rand ‘to scrape, smoothen’ 
*MIDDLE PERSIAN: ВМР Ind- /rand-/ ‘to scratch, grate, abrade, rake’ 
Pass.: IND. 3sg. BMP Indyt /randid/ 


*ra(n)j 313 


*KHOTANESE: LKh. ran- ‘to scrape’ || (+ *aua-) OKh. varras- (varri-) ‘to scratch’ || (+ 
*fra-) haran- ‘to throw’ — SGS: 115, 119, 149 

*NWIR: NP randidan ‘to scrape’, NP razdah ‘tired, exhausted, hindered’ (= Skt. 
raddhá-), Bal. rast, randit/rand- ‘to comb; to draw (a sword)’, ? Bashk. (North.) ron-/ 
rönd- ‘to cover (an ewe), mate’ (Gershevitch 1977: 64 f.), Bashk. (North.) aran-/ 
ärand, агаг-, (South.) yiran-/irant-, yiranst ‘to comb’ || (+ *?) ? Sh. (Baj.) piriü-/ 
pirüst, Rosh. par&0-/paröst, Orosh. pará6-/parüst, Sariq. para0-/pariist ‘to burst, tear 
[intr.]’, (caus.) Sh. pirénd-/pirént, Rosh. parénd-/parént, Sariq. parin-/parind ‘to tear, 
burst [tr.]’ 

*NEIR: Oss. D. randun ‘to smooth, iron’, Yghn. rant-/ränta- ‘to wipe (out)’ (-t- < *-0- 
< Ir. *-d- ?) || (+ *uz-) Wa. zrand-/z(a)rast-, z(o)rond- ‘to scratch, scrape’ 

*SANSKRIT: randh ‘unterliegen’ (RV+), randháya- (caus.) ‘unterwerfen = EWAia 
II: 431 

9 The semantic range of meanings displayed by the Ir. forms is difficult to reconcile: 
the meanings may go back to originally ‘to depress (soil, hair, clothes, etc.)’
```


## [2026-09-14T01:57:44.937Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FVQ rawda ===\"; grep -n -i 'rauda\\|rawda\\|rauḍa\\|روضة\\|rauḍ' FVQ.txt | head -20; echo \"=== FVQ_pages grep ===\"; grep -n -i 'rauda\\|rawda\\|روض' FVQ_pages.txt | head -20",
 "description": "Grep Jeffery for rawda"
}
```


### [2026-09-14T01:57:45.014Z] TOOL RESULT

```
=== FVQ rawda ===
9075:O.Pers. rauda, day 2 ; Skt. ^t^ shining, radiant. The Phlv. JDgy 
9214:(Rauda). 
=== FVQ_pages grep ===
5331:O.Pers. rauda, day 2 ; Skt. ^t^ shining, radiant. The Phlv. JDgy
5408:(Rauda).
```


## [2026-09-14T01:57:47.477Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA && python3 - <<'EOF'\nt=open('PLA_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('NPAGES',len(pages))\nimport re\nfor i,p in enumerate(pages):\n    if 'rauza' in p or 'rauḍa' in p or 'روضة' in p or 'rauḍ' in p:\n        print('--- leaf',i,'---')\n        print(p[:1500])\nEOF",
 "description": "Grep Asbaghi PLA for rauza"
}
```


### [2026-09-14T01:57:48.583Z] TOOL RESULT

```
NPAGES 302
--- leaf 151 ---
zufüf                                                                 197                                               rawägir

2% - rufüf:              Pl. v. raff g. v.

Olk,- rimäg:             Pl. v. ramaq g. v.

or       _    ramgan       = armagäan            q.    v.


GO» - ramag:            "Herde"            aus dem pers.              Au rame '          mp.s?        °,

                                                                                                              3
ar       -    ranfis:       "Narzisse"                eine    Metathese          v.=-    nargis     g.     vV..


Sy) - rand:            "eine         wohlriechende             Pflanze"          <pers.o           nardin,        syr.    1, ,
         hebr.173          3,


Er       -    randaf:       "schwarzes                Leder"        aus    dem   pers.   o,», rande      4        mp.    »p rand
         v.    Verb     randidan             5 "Nabschleifen,               abreiben"     „


u    -       ranf:     "wilde          Weiden"         pers.    6,


OL», - rahbän               s. rahib.

ale,           -     rahbäniyya:             "Mönchstum,             Klosterleben,       Askese"      s.    rähib.


Fi            - rahnamaf = rahnämaf a. v.

0,2,- rahwa = rahwäß q. v.

gi» -         rawag:       "fließend,                beweglich"           pers, << mp.        ZI» rawag     "fließend"       v.
         Verb        raftan          "gehen".


sb           - rawädig:          Pl.
--- leaf 152 ---
raudag                                                                      138                                                                 rüt_



Ob» - raudaqg:                   "abgezogenes                  Fell;       zum Braten           abgehäutetes               Zicklein"        aus
       dem          pers.        0),        rüude      Im.                 IPP     rüdan       "pluck,         pull       out"    2,


Ss, - raudak:                    "schöner              Junge"        aus    dem pers. 3%, ridak                      ®    — mp.» redak             a
       Ve       nw»           rodiSn             >> rüyiS            "wachsen,           ein    junger         Mann       werden",

 .                                                                                   -          5
Cs, - rauzan:                    "Fenster"               aus    pers.       &,      rozan            m.              ep    rocan       <a.
       raocana              6,


Eli             -    rüznämaf:               "Kalender"                    pers.     _,    rüz       <mp.9pP             ro® am.           raocah,
       ap.          raucah         + a-ı          näme        mp.          „Pl     nämak       7,


abs); - rauzana                    = rauzan              q.    V.


ol,         -       rüstäg         =    rustäg           q.    v.


Erz         - rusahtag                  = rusahtaf              a. v.

ol, - rußan:                     "Fenster"               aus
```


## [2026-09-14T01:57:57.456Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA && python3 - <<'EOF'\nt=open('PLA_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(pages[152])\nEOF",
 "description": "Print PLA printed page 138"
}
```


### [2026-09-14T01:57:58.611Z] TOOL RESULT

```
raudag                                                                      138                                                                 rüt_



Ob» - raudaqg:                   "abgezogenes                  Fell;       zum Braten           abgehäutetes               Zicklein"        aus
       dem          pers.        0),        rüude      Im.                 IPP     rüdan       "pluck,         pull       out"    2,


Ss, - raudak:                    "schöner              Junge"        aus    dem pers. 3%, ridak                      ®    — mp.» redak             a
       Ve       nw»           rodiSn             >> rüyiS            "wachsen,           ein    junger         Mann       werden",

 .                                                                                   -          5
Cs, - rauzan:                    "Fenster"               aus    pers.       &,      rozan            m.              ep    rocan       <a.
       raocana              6,


Eli             -    rüznämaf:               "Kalender"                    pers.     _,    rüz       <mp.9pP             ro® am.           raocah,
       ap.          raucah         + a-ı          näme        mp.          „Pl     nämak       7,


abs); - rauzana                    = rauzan              q.    V.


ol,         -       rüstäg         =    rustäg           q.    v.


Erz         - rusahtag                  = rusahtaf              a. v.

ol, - rußan:                     "Fenster"               aus    dem      pers.      &s,     röäan        "Licht,          hell"           mp.    op
       rosan au.                        raox$ana              8, mand.           rufanaiia          °.

ou-     raud:          Pl.         v.asy            rauda       q. v.

Ay -        rauda:            "Garten"              aus       pers,„ raz            v.    Verb (u,             rostan      mp.»            rod
                                                                                                11
       << aw.               raod.           10    / ap.        raza      "Weinstock"


b»-     rüt:          "Fluß"            aus       pers.)» rüud             12        mp.>»           rod       <a.         rautah.




 1.    Gähiz, al-bayän                       n.     Fück       Arabiya,           Tafalıpi          figh       al-luga      S.     198.
 2.    Mackenzie                 Ss.    v.
 3.    Addai          Scher            s.    v.
 4.    Mackenzie                 Ss.    v.
 5.    Wahrmund               s.       v.,       Fraenkel           s.   v.,      al-Mu’arrab            Ss.    Ve
 6.    Mackenzie                 S.     v.
 7.    Nyberg          Bd.         II       s.    v.
 8.    ebda.
 9.    Macuch           Ss.      v.
 10.    Bartholomae                     AIW,        S.    1495,
 11.    Mayrhofer                      S.    14l.
 12.    Muhit           s.       v.,        Nyberg        s.    v.
```


## [2026-09-14T01:58:11.614Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '9195,9235p' FVQ.txt; echo \"=== page context ===\"; python3 - <<'EOF'\nt=open('FVQ_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if '(Rauda)' in p or 'Rauda' in p:\n        print('LEAF',i)\n        print(p[:2500])\nEOF",
 "description": "Jeffery Rauda context"
}
```


### [2026-09-14T01:58:12.774Z] TOOL RESULT

```
FOREICrN VOCABULARY OF THE QUR*AN 145 

Eth. C? 71 and the Phlv. ideogram **v&y roramnd or jjjy rovnand, 1 

arc of Aram, origin we may assume the same for Ar, ^Lltj, 

but the ultimate origin of the word is still uncertain. 2 It occurs in 
Heb. as "pQ""), in Aram. WWH and X3QT"), as well as Mandaoan 
MiWn, 3 but appears to be non-Semitic. 4 Horovitz, Parodies, 9, 
thinks that if it is true that the pomegranate is a native of Socotra 
we may have to look in that direction for the origin of the word. It is, 
of course, possible that it is a pre-Semitic word taken over by the 
Semites. (See Laufer, Sino-Iranica, 285.) 



(Rauda). 
xxx, 14 ; xlii, 21. 

A rich, well watered meadow ; thence a luxurious garden. (LA, 
ix, 23.) 

Both passages are- late Meccan and refer to the blissful abode of 
the redeemed. 

There can be little doubt that the word was borrowed as a noun 

.* , * -- 
into Arabic, and from it were then formed <^J "to resort to a 



garden", (j^J'j " to render a land verdant ", (j^jjl 4 * to abound 

in gardens ", etc. As some of these forms occur in the early literature 
the borrowing must have been an early one. 

Vollors, ZDMG, 1, 641, 642, noted that the word is originally 
=== page context ===
LEAF 162
FOREICrN VOCABULARY OF THE QUR*AN 145
Eth. C? 71 and the Phlv. ideogram **v&y roramnd or jjjy rovnand, 1
arc of Aram, origin we may assume the same for Ar, ^Lltj,
but the ultimate origin of the word is still uncertain. 2 It occurs in
Heb. as "pQ""), in Aram. WWH and X3QT"), as well as Mandaoan
MiWn, 3 but appears to be non-Semitic. 4 Horovitz, Parodies, 9,
thinks that if it is true that the pomegranate is a native of Socotra
we may have to look in that direction for the origin of the word. It is,
of course, possible that it is a pre-Semitic word taken over by the
Semites. (See Laufer, Sino-Iranica, 285.)
(Rauda).
xxx, 14 ; xlii, 21.
A rich, well watered meadow ; thence a luxurious garden. (LA,
ix, 23.)
Both passages are- late Meccan and refer to the blissful abode of
the redeemed.
There can be little doubt that the word was borrowed as a noun
.* , * --
into Arabic, and from it were then formed <^J "to resort to a
garden", (j^J'j " to render a land verdant ", (j^jjl 4 * to abound
in gardens ", etc. As some of these forms occur in the early literature
the borrowing must have been an early one.
Vollors, ZDMG, 1, 641, 642, noted that the word is originally
Iranian, and he suggested that it was from the Iranian V rud, meaning
to yrow. 5 The Av. ^i-ui fojod means to flow* from which cornea
1 PPG1, 198 ; Frdhang, Glossar, p. 105 ; and Noldeko, Neue Beitrar/fi, 42.
3 Low, Aram&Mche Pfltinzfiiwiainen, 310, says : " Etymologic dunkol," and soo
Ziinincrn, Akkad. Fremdw, 54.
3 Nt>ldekc, Aland. Gramm, 123 ; Lidxbarski, Mandaisc.hfi Lituryien, p. 218.
4 Hommel, Anfsdtze, 97 ff. ; RDB, 941, "a foreign word of doubtful origin"
5 " ^JJ ^ * ine Wtymulogio : zur Bcdeutung ist hier nur daran zu orirmorn,
dass cs in der Nomadensprache jeden grunen Fleck in odor Umgebung bczeiehnet.
Mit dem alten Spraehgcbrauch deckt sich nooh jctzt nach meiner Krfahrung gonau
dio Sprachc z.B. der Sinaibeduinen. . . . Toh glaubo nicht fehl z\i gehen, wenn ich,
j, aus p. \/ rud c waohscn ', erklfiro."
Bartholomae, AIW, 1495; Reichelt, Awestisc.hes Elementarbuch, 493.
```


## [2026-09-14T01:58:22.052Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('FVQ_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(pages[163][:2500])\nEOF",
 "description": "Jeffery p.146"
}
```


### [2026-09-14T01:58:23.343Z] TOOL RESULT

```
146 FOREIGN VOCABULARY OF THE QUR^AN
raoSah a river* and JJ^D^JJ) rao8a, growth (cf.
Skt. "O^, rising, height), also meaning stature,* From the same root
comes Phlv. 5y a lake or riverbed* and the Pers. ^Jj commonly
used for river, e.g. C*J ^Jj the Euphrates. The Phlv. word is
important, for the Lexicons tell us (cf. Tha'lab in LA, ix, 23) that
water was an indispensable mark of a <^Jj. Thus the conclusion
would seem to be that the Arabs learned the Phlv. Sy 4 in the
Mesopotamian area and used it for any well watered or irrigated land.
(Ar-Knm).
XXX, 1.
The Byzantine Empire.
It is the common name for the Byzantine Greeks, though also used
in a wider sense for all the peoples connected or thought to be con-
nected with the Eastern Roman Empire (e-f. TA, viii, 320).
A considerable number of the early authorities took it as an
Arabic word derived from *lj to desire eagerly, the people being so
called because of their eagerness to capture Constantinople (Yaqut,
Mu'jam, ii, 862). Some even gave them a Semitic genealogy L/l, xv,
150, and Yaqut ii, 861. Others, however, recognized the word as
foreign, as e.g. al-Jawallqi, Mu'arrab, 73, who is the authority followed
by as-Suyutl, Itq, 32 1. 5
The ultimate origin, of course, is Lat. Roma, which in Gk. is 'Pto/zr;,
which came into common use when ?} Nea 'PoJ^u; as distinguished
from 7} Trpeo-fivTepa 'Pco/zi; became the name of Constantinople
1 Horn, (friindrift*, 139 ; Bartholomae, A I \V, 1495. Cf. th< O.IVrs. rautn = river
which is related to Gk. pvais, ptrro?.
PPUl, 198.
3 PPG1, 198, cf. Av. AdJ) urud, riverbed, from the root mod (Reichelt, Avestan
Reader, 266). and Pazend r^7, Phlv. qoy a river (flhikantl, Glossary, 265).
1 Addai Sher, 75, wants to derive ^j from Pers. jij, which seoms to be wide
of the mark.
6 So Mutaw, 47, which elasses it among the borrowings from Persian.
```


## [2026-09-14T01:58:44.490Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AFM p75 area / روضة ===\"; grep -n 'روضة\\|الروضة' AFM.txt | head -20; echo; echo \"=== PHD rod ===\"; grep -n -E \"^r[oō]d|rōd |rwtk|'lwt\" PHD.txt | head -20; echo; echo \"=== NYB rot ===\"; grep -n -i 'rōt\\|rōd .*river\\|rwt' NYB_vol2_glossary.txt | head -20",
 "description": "Addai Shir, MacKenzie, Nyberg greps"
}
```


### [2026-09-14T01:58:44.587Z] TOOL RESULT

```
=== AFM p75 area / روضة ===
3105:+ (الروضة ) من الرمل والعشب مستتقع الا تكو النضنت مز القز به 11 
3106:وفي الكلمات الروضة ® 1 ٠‏ في !ܐܕܩ ܐܨ 03 عن ديز وهي ܬ الاء في 

=== PHD rod ===
4479:rod

=== NYB rot ===
```


## [2026-09-14T01:58:46.556Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT raodah/ravan ===\"; grep -n 'raoδah\\|raoδa\\|raonąm\\|raodah\\|sruuant\\|urvant' BRT.txt | head -30; echo \"=== SOD rwt ===\"; grep -n \"rwt\" SOD_pages.txt | head -20",
 "description": "Bartholomae and Gharib greps"
}
```


### [2026-09-14T01:58:46.633Z] TOOL RESULT

```
=== BRT raodah/ravan ===
2497:b)  substantivisch:  *ydhä  *i}is'^^ iiä  varsiaiis  yä  dälä  atihius  paouruyehyä ralüs  ^■ao^anä  razUtä  (sd.)  "velut  (est) secundum  eas  (leges)  . .  quae  (sunt)  leges vitae  prioris"  Y.  33. 1 ;  —  Aaemö  aiibis (ab  Dat)  yöi  aurvantö  Atta  taxüsti
2686:*zamarigusa    avazat   vXspe   daifa    Yt /<?.       AbleiV  aus  ■arr'OB.u'ajflZw. 'elf;  vgl.  tF,  S  ?/o 81 ;  —  yahmai  . .  aurvantö  . .  v3sa  '^an-  ■     aK  und  IF.  p.  245.  —  Pü. :  yHdahum. }aianie   °va   caxra  (sd.)    Yt  10.136;    —  •  j-    aeväkam    Adv.    'zugleich' (?):    aiv aim  .  .  yß  t0  °ve  säsnä   (sd.)  gäsatä    Y.   narqm  asaonqm  ahunvitim  ga^qm  frasrä- ^9.8;  YtJ7.i9,2i;    —  yö  nö  °v6  at  U  vay'nti  Vd. /2.
4241:•  j.  an-aoäa-  Adj.  'dem  kein  Verderben droht,  unsterblich':  aurvantö .  .  mainyus.- ii^ar?^a  'shihs  Yt  70.125.
4653:vorausg.  nagclm  und  la-  'nicht  irgend  ein anderer';  naSclm  tsm  'nySm  yOsmat  vasdä asa  "ich  kenne  nicht  irgend  einen  andern als  euch,  0  Asä"  Y.  j^7">.  II  a)  mit AbL  des  Verglichenen:  ttsit  mSi  vaiiä(sd.) x/mai  *nyS  Y.  2g.  1 ;  ^0. 1 ;  —  h3m  tta mavaitl  payBm  dadat  'nyJm  %wahmat a^rasciJ  ..Y.46.J;  34.7.  ni)  'alienus', a)  im  Gegensatz  zu  'eigen':  nsii  hl  'iiys ttrva  kaom  urvantm  paiti  irista  bqzaiti V.  y,  9'";  — jahikayai  ya  aom  pu>^r»m baraiti  'nyahmai  arsänai  varit»m  pai'^e apa.baraiti(sd.)Ytij.s8.  b), lim  Gegen- satz zu  'heimisch',  sva.  'hostis':  yadiy  ava'ia *maniyähay  hacä  'niyaria  (iS.)  ma  tarsam ".  ,  vor  keinem  Feind  will  ich  mich  zu fürchten  haben"  D.5,3;  D.4.2;  —  karam tyam  ..ajanam  vasiy  'iiiyJ'  apiy3*ahyaiä (sd)  Bh.  j.  19.  IV)  In  ungenauer  Aus- drucksweise; das  mit  a'  Bezeichnete  ist dem  Vorausgehenden,  dem  es  gegenüber- gestellt wird,  nicht  gleichartig'J':  daat {taeta)  -nyatsam  rähwqm  paiti.maydi^i^d^
4977:Yt.  10.  46.  a)  mit  relativischeni.  An- schluss:  °vä  (APn.)  j>ä  näiryi-  yä  fu'irahe "das  der  Frau  .  ."  N.  5^;  —  'v3.  (APf.) ^1  anyä  srävaydij  "die  andern  (näml. Gä'^Ss)  .  ."  N.46;  —  naicis  "vat  y3  spsn- iahe  Yt.i5.3t?).  3)  auf  ein  Relativum als  dessen  Korrelat,  a)  adjektivisch:  dva aurvanta  . .  aom  .  .  aurvanhm  yS  anhat äsus. .  aom  ,  .  aurvanhm  yö  , .  urvaisayat YL5.131;  /.24,  14-^9',  —  i^y  '^"J  ^'"^^ 3s  .  .  yat  mS  fravaocö  .  .  Y.ig.i;  Yt  5. 41,  Vr.  20.  i  f.*,  G.  2.8;  —  xfä^r^meä  'val .  .  yä  .  .  rämqmcä  (sd.)  dät  Y.2p.  10; °va  (IS.)  daxita  daxstavanta  yä  nditpom ßra{sA.)/raäaxsta\t.5.')^;  —  'vä(lS.)i^ wanarthii  yä  .  .  manta  .  .  Y.  33.  6 ; 'vaiiiha  drüjB  .  .  yä  .  .  upa.dvqsaiti  V, 17;  17;  —  Aaca  'vai/ihai  Jahikayäi  .  . yä  .  .  upa.baraiti  (sd.)  Yt.  17. 58;  —  nsU 'va  (APf.)  zaoira  ..  yä  ..  framthar>nii Yt5.93;  I4.\i\  —  *'va}ika  (APf.)  > va^ays  .  .  yä  .  .  anhan  Y.  2j.  1 ;  —  •; (APn.)  dämqn  . .  yi  A^nti  . .  Vr.  7.4;  — •w7(/  uroaikis  (sd.)  ya  ta  . .  didirszd  Y. 44--ii;—''*'vä  (NPf.)  dakyäve^  tyä  dura- yt^v<^uS  adärayj'  \i.6.ä,;  —  mat  'vaby5 (DP.)  daxstäbyö  ydäsa  aHrai'a  "mit  den Zeichen,  wie  ein  Priester  (sie  hat)"  V.  /j. 22.  a)  das  Substantiv  ist  aus  dem Relativsatz  heraus  zu  ergänzen:  yä  tu haßi  (sd.)  'vi  (APf'>,  näml.  asll)  yä  da alis..\.43.\.  b)  substantivisch:  'tat yäsqs  hyal  vS  istä  (sd.)  vakishm  Y.  4g. 12;  —  've  (als  AP.)  aifi  (sd.)  dat^ants . .  ysi  . .  dniihiti  Yt.  10.4s ;  45;  "*  °z'J»V aibt  ySng  dainll  nSit  Jyatius  (sÄ). .  Y.  J2. 15;  —  'valsqmca  päi^B  paniö  yim  (statt AP.)  isMiH  mhmJrufdYK.  /O.45,  4)  auf den  Inhalt  eines  Konjunktions-  oder  Re- lativsatzes, a)  adjektivisch:  'va^  ayapl>m dazdi  mi  .  .  ydha  azgm  häcayene  . .  Yt.5. 18;  130,  p.i7f.,  75.3,  77.25;—  'vaÄeca paiti  yqiiahe  ya^  he  da%ai  .  .  Yt  16. 6 f.  b)    substantivisch:    'val   h!   as/t
5386:•  j.  auruäa-  Adj.  'weiss',  1)  von  Tieren: pttsüm  .  .  'hm  vH  vohu.gaon^m  vä  "ein weisses  oder  schwarzes  Schaf  Yt.ÄsS; —  aspa/ie  ktkrpa  'iahe .  .  aspahe  kihrpa sämahe  "in  Gestalt  eines  weissen  Rosses . .  in  Gestalt  eines  schwarzen  Rosses"  Vt. Ä  18-21";  —  aurvants  'la  raoxsna  fnl- ä)r»sra  Y. 57, 37;  YL  JO.  136.  z)  sonst: srlra  i-a  auhtn  blzava  'h  (ND.)  Yt.5.7;
5551:1 99  'airyaman-  —  aurvant-  aoo
5583:•  j.  airyö.sayana-  n. 'arischer  Wohnsitz,  .j^g. aurvant-, aourvant-" Adj. 'schnell; W.  der  Arier':  vJspjm  .  .  'fvm  Yt  10.  13.  tapfer,  Held':  '7-at"  F.  7;  —  /laomo  aeibis
5732:hat,  wiiW:  yim  . .  aurvants  . .  viivSahS •ya  i'UEwiA' Y.  57- 27,  2)n.  (oder  f.  'yiJ-7) im  Du.  Name  eines  Bergs  oder  Gebirgs; ahmat   haca  garayö  /raox^yan  . .   'yaica
6440:i6i  aäta-aurvant-
6455:•  j.  *asta.aurvant-''  m.  EN.  eines  Gegners des  Viitäspa:  tarn  yazata  i'TsiOspS  .  . yaisa azäni  pplana  (sd.)    'vantö  (GS.)  Vt.fJ.jo.
10045:solut 'heimkommen,  -kehren':  sraohm  ., yS  vXspaHbyö  haca  ansaHbyS  . .  vavanv^ paiti.Jasaiti  Y.  57.  13;  —  yä^a  tl  vispe aurvanta  zaw^aba  paiti.Jasqn  Yt.  5. IJ2.         3)  "hinkommen,  -gehen,  sich  hin-
11056:spmts  mainyui  yasca  a^rö  Y.  57.  17;  — dva  yaska  .  ,  yasca  suis  yasca  tarsnS  V. 7.70;  —  äva  aurvanta  .  .  yimca  bipaiti- stätum  aurvanUm  yimca  cahwarypaiiiit3- mm  Ytj.  131; — yaiaca  hukmpta  fstäna yaha'a  atalan  niväzäna  Yt  5. 1 2 7 ;  — ya'iraca  mazistA  Jrfr»tä  ya^raca  atbislö as'ava  Yt.  13.  25;  —  ähnlich,  aber  mit  ab- weichender Stellung  des  ca :  yaihä  pourüica hr^ijayqn  naiäica  aiäha  (Sp.  80.)  yasaiü «jfJnJi  (sd.)  .,  Y.  65.  II.  fi)  'ii  Ver- bindung mit  ä  (s.  Sp.  300  m.):  yaHbyascä  töi 3  ya^ä  aiibyS  ä  a»h}n  Y.3p.  i.  An- hang zu  I.  Beim  ersten  Glied  steht  ci^ statt  lä:  tJctJ  maxdä  vasimJ  anyäcil  vXäuyl Y.44.  3.  3)  die  Glieder  sind  verbal; a)  sie  folgen  sich  unmittelbar:  yavat  . . tavalü  isäiia  Y.JO.  11;  —  ySi  iahara'a hmicä  Y.  5/.  aa;  — ydä^a  Tm  mSiiäica raoca^ä  Y.  45. 3;  —  hanalmacS  zaimscn y.41.^; —  daitihul  nihatai'^a  haosätai'a Yt  13.  66 ;  — ya'isa  m . .  *bairyetica  *x'air' yetica  V.  5.  40 ;  —  asBis  .  .  yä  ns  äraicä frtnavataicä  Y.  56^.  3;  —  yat  haonumca ahunavat  aNhavatwmca  *vTma$täi  (sd.)  N, 72;  —  yat  haomimca  äsnayät  haonDmSa pairi.kamat  N.  75.  a)  mit  unregel- mässiger Stellung  des  ersten  la:  yat  hao- miMca   gava  *rag^JoayäJ  baxsayäa/äi  N.
11761:surunvata  yasna  tarn  yjzäi  . .  arfdvJm YL5, 9;  /7.  3;  —  la  hasHt  upa.sbayeiU tqra.-fravalayS  Yt.ij.ög;  —  .Ja  nipa- yemi  vispa  vokü  Yt  5. 89;  —  harn  taät (NDm.)  bJeus  baratö ..  tistryasi'a ..  daFvasca .  .  la  (Sp.  615  m.)  yaitya^S  Yt.  S artikelhaft:  //{AD£)  aifam  paili  sruye(sä.) aZsa  druxs  upa.dvqsaiti'S ."j.  24'"';  — ya^a te  vTspe  aurvanta  zasvauha  (sd.)  paili. jasqnXX.  ^.\%t\  ;o.i2S;  —  ta  nS  data  tä (Sp.  6 1 5  u.)  fravaocäma  Y.  70.  2 ;  —  ava  Al baraytn  läshm  dauru{'si.)  upa  tqm  manao- ürTm  "sie  sollen  ihm  . .  am  Hals  anbringt V.  ij.  30;  —  minutn  barat  andvl  .,  upa tqm  srirqm  manao^rim'Vt. 5.  i2T. titn  urva^fm  /rayavaySiJ'(sä.)  sna^äi  Yt. 7.  24;  —  i^m  valmcit  yazamaide  "(ihn) den  f. , ."  Yl  75. 1 ;  i;  —  äal  t>m  varpm kfrsnava  V.  2.  25;  —  avavanOm  asa- vaynyäi  (sd.)  tqm  ä^qm  dagtayJ  V.  5. 14;  —  ä  tai  :^ami5  yasamaide  Vr.  ig.  a ; Ytö.iä;  —  nöit  kl  tä  vlsB  tilyul . . apaili.- buili  haca  vTiibyS  para.baraiti  (sd.)  V.  13. 40(?);  —  nava  äfs. .  navata  baiiacajipsa V.  21.  3  (?);  —  s.  noch  Yt.  10.  6,  i§.  49, V.p,  29;  s.  Sp.  616  o.  bb)  mit  rela- tivischem  Anschlüsse' ;  a)  im  gAiv.:  at  tSng dngva  ySng  asalefl  vazdrJng p,lt  gä fror»' f^{s6..)  Y.4Ö.4;  —  t3is  . .  yäis  daiäis  . . ^,46.  15.  B)imjAvr.:  tat  drvais..ta! . .  pairi.urvalstsm  yat  tamS  voku  Yt. //.  a; Y-jÄ  I';  —  ta  (NPn.)  ns  ama  ta"  . . uxjamyqn  yä  staota  yestiya  Y.  55.  3;  — ta  vanukJ?  tä  vahisth  yazamaide  ya  .  . fravasayö  Yt. y.  27;  —  tä  .  .  upastqm k^Ttti  dahiita  ya  fravasayS  Yt  13. 17;  76;
13236:—  asdibü ..  rao^a.aiwi.varma  (sd.)  ..  t?/ne faiti  mdai^iiaV.6.  sijÄ 76;  —  iva's.h) . .  tanüm  . .  nida'hamal . .  dar^is'tagA'aläi] fiaiti  gntuh'a  V.6.^i,{.  g)  paiti  mit Gen.:  aurvant^m  "iawä  ,  .  bayB  nida^al
13444:•  j.  dämLdäta-'),  dami-däta-  Adj.  (fem. VJ-)  'vom  Schöpfer  (AhM^  geschaffen'" von  Gottheiten:  aurvant»m  ^ws  (näml. Aaom^m)  °Um  Y.  io.  10';  —  mikrtm  .  . 't^/n  YLJO.61;  —  a/i"  srTi-e  'oatte  (VSf.) Yt./7.6o,  61;  —  gsusca  una  -/jYt  74.54.
13920:•  g.  damSna-  n.:  s.  unter  nmäna-.  *dvaäbya^^  sr?subya'iü.Osi—dva  aurvanta
14260:i)  '(den  Wagen,  Akk.)  ziehen',  von Rossen  usw.;  Med.:  yahmäi  .  .  aurvanta *yuxta  väia  (als  AP.)  ^anjasante  Yt  10. 13Ö;  —  te  mt  vai>m  "kanjayänte  \l.  ig, 44.  2)  '(den  Strang,  Akk.)  anziehen', von  Rossen,  Med. ;  sva. ',  am  Strang)  ziehen' : aspaahs  .  .  mrätim  canma  (sd.)  %anja- ymfe  \X.i'j.i2.  3)  '(den Wagen, Akk.) lenken',  vom  Fahrer,  Akt:  yat  vTspanqm yuxtanqm  ..fratsrngm  ^aii/ayeni  "dass  ich
14328:/«%««»  Y.p,  19;  i9ffiS;  —  ana  äwal yasna  yaxäm  YLJ7.61';  —  kasp  %wam\ paoiryS  haotna  . .  hunuta  Y.  p.  3 ;  —  kana  , %wqm  yasna  yassane  Yt.5,  90,  15.  54;  —  ' kana  hwä  yaitia  ..  Yt./j.  54;  Vyt.21;  —  j az)m  'hwä  yasna  yasäfu  Vyt.20;  20;  — toi  äyapt^m, yas)  ^wä yäsämaAiYt  10. 33; 30,  5.90,  17.61,  Y.  Ö2. 1;  —  _>'öi  äioÄ vaffun  . .  Yl  io.  9a;  —  _)'o/  äai  J  dtdvllma Y,  öl?.  I ;  Yl  75. 30;  —  _>wji  %w3  didvalSa Y.J.  ai; — ^aäo  %wqi»  mit  taurvayät . . Yt./5.s6;  —  t^a  %wa  haxsöit  gjul vakwa  Y.63. 10;  10,  Vyty,  22,  45,  Any. 2^;  —  afii  %wä  3l>ayai  avairiAeYt.  lo.jy, 78;  — _/rJ  äwam  xadaraAa paiti  uzuxiäne Yt/9.  50;  48;- —  a/a  .  ,,  dansäma  haiS, pairi  %wa  Jamyama,  kamtm  hwä  haxma (sd.)  Y.  60.  la;  —  aoxtSJtamana  %wä yasna  ..yassi  Yt  /o.  31 ;  56,  Y.p.  27;  — aurvantsm  %tffS  ..iayS  tatasatY. 10.10;  10; —  yaskgm  %wqm  paiHsanhämi  V.20.7; 7";  — yaaamaiäe  %wa  aAuräne  Y .  68.  ^ (vgl.  6,  Sp.  787  o.);  Y.li.  10;  — yatayania %wqni  matdayasna  Yt.  10. 1  ig;  12.1';  — _fra  ff  kfhrpgmla  .  .yaoidäiäni;  ktnnaomi hwqm^^  hacaLpuhram  V, 2/.  6;  ■ —  b^a\ &a  histahe..,  iä^a  %wqm  tarasla  äahsns\ .  .  j^anha  bairydnte  V,^,  29;  verwendet Yyt.41';  —  /?  als  Akk.'"»:  . .  kuha  ti assm  biiazüni  V,  22.  6"*;  —  SU  aitike fraca  stuyl  . .  yezi  tl  aidhe  avil.urSrao%a (sd.)  Y./.ai'".  2)  Abi;  nur  b  i)   im
14885:—  paoiryS  gairiS  AqtnJtisiat  .  .  'ti  äya z^mä  YX.ig.i;  /O.  98,  /J.97,  Y.9.IS.  V, 7,  54;  —  nasunqm  yä  'ti  aya  zimä  irJri- ^ar»  V.5. 4;  — '11  karJ*  pärst^  hyJ'  vtha- (id.)patiy3'^  . .  Bh.  J.  4;  2.  5  (ergänzt);  — tiyri/  ,  ,  afanvaia  'ti  niral  (Sp.  184  o.) Yt^.  38;  —  dasina  'ti  ahoanha  "auf  der rechten  Seile"  N.  65.  4)  mit  Abi.,  nur räumlich;  a)  auf  die  Frage  woher?:  mihr>m .  .  yS  vlspfm  aAsm  . ,  ädiiäiti  haraihyat 'ti  bar3tanhai  Ytio.  51.  b)  auf  die Frage  wo?:  dunmqn  hqmJiiitinli  *iisMndvat °ti  garsit  YtS.32;  —  yim  yazata  ahurS mazda  raoxinat  'ti  gara  nmana£  Yt /0. 1 2  3 ; 5.25,45.  s)  mit  Gen.,  nur  raumlich; a)  auf  die  Frage  woher?:  naKa  dunmqn (sd.)  uzjasaiti  Aaraihyd  'ti  iamayä  Yt 10.  50.  b)  auf  die  Frage  wo?r  ^dasimm J  va  gaonavatö  (sd.)  ^banstrvS  va  'ti vayhanaAe  N.  65;  —  zqm  .  .  yetiAa  'ti  . . apa  taünti  Yt  jj.  9  f. ;  i  o ;  — y^iihe  nmämm ..vüätfm  banzi'te  paiti  bar^aAi (Sp.Ba^ u.)  AaraiiyS  'tt  banxayä  Y. 57.21;  19;  — ys .  .  Aaomq  utdasta  .  .  kara^yS  'ti  bar»- '  xayä  Ytio.  90.  c)  auf  die  Frage  wo- hin?: aurvantim  %wä  .  .  bcrjS  nida'iat .  . Aarai^yS  'ti  banzaya  Y.SO.  10.  6)  mit Dat(?)"'',  räumlich  auf  die  Frage  wo?: tarn  yazata  auf  .  .  daAakS  bawrsii  'ti daiiihaove  Yt.  5.  29.  3)  zum  Ausdruck des  Gleichkoromens,  Aufwiegens;  mit  Akk. 'gleichwertig  mit  — ',  bei  Ellipse  des  Verbums {'ah-):  ha  ml  baya  .  .  satam  'ti  anyaisqm ra^wqm  gä^anqm  "dieses  Stück  .  .  wiegt hundert  andre,,  auf  Y./^.S"';  15.  A)bes. zur  Angabe  dessen,  was  als  Preis  oder  Lohn geboten  oder  verlangt  wird,  'gegen,  um, für';  i)  mit  Akk.:  uzbasaui  'ti  ammxtttn (sd.) /rarazaite  miirS  Yt  10. 1 24.  a)  mit Lok.:  yehyS  .  .  vaAistptn  yesng  'ti  vaidä (sd.)   mazda  Y,  57.  2a;   27.15,  Vr.  16I3;
18443:—  iW  nö  aurvantB  .  .  Ytio.  4a;  42,  V, J2.  2(?);  —  yö  nB  data  Y.j.  1;  Yt  y.  51, /f.  40,  Vyt.jO;  —  yS  nö  .  .  irjrlxsätte gal%anqm  Y.  öj.  7;  7;  —  yö  nB  aivB  Y. II.  9'';  —  yh  nö  hsnii  gJ^ä  harihra- vaitlSca  .  .  Y.  55.  2 ;  2 ;  —  fravasibyö  yh nB  isla  urvöibyS  Y.56'.  2;  —  yaBsqm  nB akurB  . .  vanhB  vaiaa  (sd.)  Vr.  16.  y,  — kö  nB  slavät  Yti^.  50;  —  hake  nö  i(,a nqma  ayairy3t . .  kahmai  nö  tat  da%r>m dayajYt.l3.$o;  —  asaya  nö  *paiil.jamyai Y.  7.  24;  —  humaya  nö  buyata  Vr. /2.  5; Y.  6<y.  21;  —  uvaUbya  nB  ahubya  nipaya Y.57.  25,  Yt  10.  93;  —  uäa  nB  tatB a%rava  Yti_j.94;  F.2d".  zu  i  a):  a^a nö  jamyai  ^avariheY-S'-ii  Vt  to.  5*,  77, 78;  —  upa  ta  nB  iha  ..  *i^miB  fravasayö Yt/J.  146;  —  a^atla  nB  va^B /ravaoce Y.ig.it.  zu  2);  maia  ya}  nö  uyra.- bäiauS nivanai  Yt  i0.7Si — yB agnanhaiti nB  manBY.g.iq;  29; — avai  ayaptim  datdi nö  Y1.5.  58;  73,  15.  40;  —  ma  eis  paurvö boilyalta  nö  Y.g.21;  —  wertlos:  Yt 2.  II'.  V)  j.  ni,  ns  Akk.-Gen.-Dat Plur."';  zu  i)  spraoiS  .  .  y!  na  (Dat.)  isiB (sd.)  Y.  56.1;   —    a^is  .  .  y.i  nS  (Dat)
19836:•  j.  tnaimv-asah-'>,inainyav-*Adj.(auch fem.)  'im,  durch  den  Raum  der  Geister (d.  L  die  Luft)  sich  bewegend,  schwebend, fliegend';  a)  von  Rossen:  sraoltm .  .yim . . aurvantö..sp>nta  vi^änhs  asaya  'ivasanAs (NPm.)  vaxaaii  Y.57,  a?.  b)  von  Ge- schossen: ^aäiz  tiyris  'ytmasä  (ÜSia.)  yim anÄai  .  .  YtS.6;  —  hazaarjm  ifunam (arltinqm,  lakuianqm,  kantanqm,  gMa- nqm,  fem.!) ..  'j/avasä  (NPm.,  {.)'*  vas^nti •yavasä  patanti  kam?r^  paiti  äalvanam YLJO.i39(fi:).
19900:—  miäir»m  .  .  yim  aurvants  'vättkö  .  . vatftiÜ  Yt  10,  68;  —  akunm  masdqm 'yaom  'yavanqm  dämanqrn  °yaoyä  siöU aiamät  rir/SmÄ*  Vr.2.4;  Vd.20;  —  ratavB •yavanqm  (näml.  dämanqm) . .  *gaeihyanqm Vr.  7.  I ;  —  ratavB  'yava  ayese  yeiti  .  . ga^ya  Vr.  2.  i.  A)  bes.  von  a)  Göttern, b)  Dämonen;  zu  a):  ahur?m  masdqm  'yaom Vr.  2.  4;  —  lait  masyS  gathyd  ^^(sd.).. yi&a  mi^rasat  'y«vS  Yt/o.io6;  io6f.*,
19910:•  j.  mainyuä.x'ar«&a-  Adj.  (fem.  •%a^ i)  'die  Nahnmg  des  Geistes  bildend':  yh nS  htnti  gdhä  Aarfhravaitls^a . .  '^äsca  yä nö  hsnti  urune  tvaim  i^an'äfmld  vastr^mSi Y.55.  a;  2.  2)  'die  Nahrung  der  Geister geniessend':   aurvants  .  .  *&a  anaa^ahs
20797:—  avaf  yät  (statt  NSn.)  hvarS  aväcl  Y. ^6.  6.  zu  3) :  viävA  avqm  (nämL  •« jf nftw)  yä  (NSf.)  Jm  anhat' apima  (sd.)  Y. 44- 19;  —  avat  xlääir>m  hyat  .  .  vokü vaxsat{%d^  manaiahä  Y.^i.6;  —  x/a- %nmäJ  avat  ya  (IS.)  huitUU .  .  dst  Y. 2g.  10;  —  av3is  urvatais  i&A.)  ya  (APn.) ia..dJd>riiS  H.44~\%-  ß)  adjektivisch wie  bei  e  (Sp.  1204  m.):  avä  yä  da  asts (Sp.  241  u.)  dngväit^ . .  Y.  43-  4-  B)  im jAw.;  das  Relativ  ist  a)  substantivisch aom  asmatum  yS  usca  raoxlnS  .  .  y3 imqm  zqm  äca  patrica  bväva  ..yö  histaite ..yim  vasle..yaAmäi  tiSii-.  Ytl^.sL; aom  ,.  *aurvantim  y3  ha^/tayä  ..urvalsayat karana  Ytj.131;  131,14.58;  —  *avaiti hat  jahikayäi  yä  . .  pu^nm  . .  patke  upa. baraitiisd.)  Yt  17.  58;  Ä  51,  V.io.  17';  - aomca  süksm  yim  baraiti  karö  Ytr4'29;
20919:unter  a.  2)  in  andern  Kasus^**;  a)  ASm. : yai  upatihacat  yim  yimim  xsalt>m  kvq- 'iwpm  Yt.  r(>.  31;  —  vazimna  yim  vohSm sraohm  Y.57.  29;  —  dva  aurvanta yasatni yimla  bipaitislän>m  ,  .  yimta  ca'^wartpai- tiliärmn  Yt5. 131.  b)  ASf:  aoi  yam gagäqm  astvaUim  Y.  (j.  8;  57.  24;  — ymqnqm  ratüm  amruyl  dainqm  *mäzda- yasnlm  afim  vatfuhim  *p3rmdim  yqmca bipaitistanqm  aiaonlm  imqmcä  tarn  Y. y.  i;  —  yam  bityqm  kva  agtqm  xsa- param  urva  *vanhaiH  "die  zweite  (Nacht) wo  weilt  diese  Nacht  .  ."  H,  2. 3,  11;  5, nsit  tl  .  .   *drajys  *{yeinm  fra'
20952:aurvanta  *yux/a*i  vai'a  %imjasiaU  Yt j  to.  1 36.  2)  'zusammenfügen;  verbünden'; ia)  absolut:  upa  tair^m  Aarayä  yuxtayi
22011:—  ya%a  ratsm  ahurs  vastä  (3SPfA,)  . .  |  seinem  Verstand  bewusst  ist:  'wenn  .  .'" ayi  asaya{'i&^  Y.J7.  2;  3^.6;  —  aam  _yj;P.  3/;  —  sp^m  viiu/avaitfm  .  .  äraagpm saota  . .  vlli'ä  alsqm  yasmmca  vahm?mca  (sd)  »iÄK/(NSm.)  apäihisi^A.)  V.-/.  55; ".  .  der  ich  mich  verstehe  auf  .  ."  Vr. ,  54.  a)  ohne  Objekt:  yS  näirikqtn II.  19;  19*.  a)  Kaus.  'erkennen  —,,ctiravaitim,,vl''ovä..vl'iuilm..xiuärä ms&ta  lassen' -.va^.ayatna  F.  S.  a)'etwas,\am  JraaAamaiti  V.iS.6j;  — yS  narvm.. Jemanden  (Akk.)  erkennen  als—'  {Akk.};'  iasyaahe  {sd.)  sarWiäi  daoaiti  vilvä  avat Perf.  auch 'etwas,  Jemanden  (Akk.)  kennen  '  ^«nia  xra%itia  paräiti  (Sp.  153  u.)  V", als-  (Akk.),  wissen  (von -),  dass  -  ist':  ,15.  2.  b)  insbes.  Part.  PerC  a)  Akt "t  yStg ■•  vdista  ..  »rpiailftg  {sd.)  Y.2Ä10;:  'kundig':  sraos>m  . .  yim  aurvants . .  spmta
22692:vaim  aurvantqm  aurvöJ^m^m  yazamaide Vt/j.57;  57";  —  i-jj^ (Nom.) '' . . «»ft- maisva  (sd.)  gatusva  . .  hqm  isimnfm  (Sp, 29  m.)  pailyaiti  Yt  15.  53.
23166:1)  'fahren';  i)  Irans.;  a)  von  Zugtieren sva.  'ziehen*:  srao&m  ..yim  ..  aurvanlS .. vatmti  Y.57.  37;  Yt.  ;o.  68,  47,  77. 12;  — aurvants  . .  vazimna  yim  vohüm  sraohm Y. 57.29;  —  s.  noch  'vazäna-,  b)  vom Wind;  a'hra  pascaUa  vazaite  vätB  .  . varymca  maiy>mca  fyanhumta  avi  ('hin zu  . .')  asä  . .  YL<y,  33.  c)  vom  Fahrer, sva.  'lenken':  y&  *paourvS  väsim  vataite VL5.  11;  —  s.  noch  Absol.  2)  intrans.; a)  von  Zugtieren:  ahmya  väse  vatänte ("a^warS  aunian/s"a.ndtmW^enz\eheTi,," YtJO.iag.  b)  vom  Fahrer;  Akt  und Med:  dahmS..  banmnS  vä  vazimnS  vS ". .  reitend  oder  fahrend"  N.  J7 ;  —  talints . . barmtB  .  .  vaz?nts  nSit  framanyenU  (sd.) "laufend  . .  reitend  , .  fahrend  . ."  Yt  10.  ao; —  fravaiayB  . . ya  aojislä  vaz>ntqm  Yt 13.  a6;  —  ahmya  *vasa  (sd.)  vazsmna (NSf.)  Yt  5.  n ;  —  dasimm  hl  upa  ar^m vazaite  .  .  sraess  Ytro.  100;  100,  laö', 70;  —  vTspS  hl  ypa  *ar^j  vastnti yä  apB  Yt  10.  100;  —  mi^r)m  ,  .  ys vUpähu  harsvShu  .  ,  vataite  ^ar»nS.dä YtJO.i6;  107;  — yat  d^ra  para.jasaiti vaztmnB  (näml.  mihrB)  Yt.70.  loi;  86, 74. 2 ;  —  nixiata  ahmät  vazata  atarl YtJO.  127.  c)    von    Heer  und   Volk
=== SOD rwt ===
8018:      arsanx Orsx, >rsy) ©*arsah-, Skt. arsas                         arta-waspc Ortwsp'y, Yt'wspy, 'rwt'wspy)  (^'
8159:1521 'rwt'wspy       S =* 'rt'wsp'y                                    1534 'spVck' B                         &£*t_yi>*<j*?
11445: 2680 prwt =» prH                                                        fra-ke5 ©adv. ^Pr'k1
14072:3614 8rwt>t S                                              ^^U               133; TSP 16.44-, GMS 1097, 1255; Gersh. Sogd.
14079:3615 5rwth      S                                       P^u^j^j            heart
14084:3616 Srwtpt S                                   (j/^ xU)^Ci>7
14291:     from this word to another                                     5urt(a), Surta ©ob. -y\ f. n. =»8rwth
16484:                                                C.lUl^ i^U*<J&             Ywtty, VJ 836; rwt>())yt SCE 532; TSP 6.109;
17789:       C2 gloss.                                                         Vaj. 2.4, Dhy. 20; Anc. Lett. 2.57; Wrwt, TSP
17804:         kt'rwt
17808:        4958 kt»rwt B -+ kt>r                                                destruction
22075:                                                             6406 p>p>rwty
22214:     SCE 451                                                par =^p}rwty, p*
22302:6466 p'rc- C                                      o^J'^j            par-ti -»p\ p>t\ p>rwty, p'rZY
22306:                                                              6481 p>rwty B, C, S        (o>> ^t* j*)^ & <^ Ajj
22346:      par(u)ti    =»p>rwty                                                6501 p>s>y(y)- B, M, C                                ^ui
23813:     paruti (prwty, pr'wHy) =*prw >P£Y
24603:      paruti =*p>rwty, pr*w>PZY
24684:                                                            7304 prwty =» pr>w>PZY
28358:                                                                             rocik (rwtcyk) ©Pahl. rozig
```


## [2026-09-14T01:58:58.020Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SOD leaf 412 (printed ~346) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==413' SOD_pages.txt | head -60",
 "description": "SOD printed page 346"
}
```


### [2026-09-14T01:58:59.132Z] TOOL RESULT

```
=== SOD leaf 412 (printed ~346) ===
                                                                                                                     rwstm(y)

 345


      (/<9)make grow                                                       TSP 2.1193, 7.26, 8.39, 29; BSTBL, Padm. 52, 61
      Sogdica. 47.4; GMS 547
 8567 rw8ny(y) M                          ^ij^j^Jm                    8577 rwke'tCh) =» rwk
      ro8ne (rwdny) ©ace. -nw-, nom. -ny; pi. -/iyf
                                                                      8578 rwkSyspr* =* rwk
      (a/Obrass, (o/)copper, brazen                                            pl30
      GMS 1058, 1246; BBB pl34; Hen. BSOAS 8,                         8579 rwkp'r =* rwk
        1936, 584; C2 gloss. 23R4, rwdny, 91R8,                       8580 rwp— B, C                   o^,jj <c*3j i o^>- <o-^^
        rwdnw; pi. rwdnyt, Hen. Tales. 473, 51                             rop ©fraup\ Pahl. rob
                                                                           0<?)pick up
8568 rw8yn>k B                                    ijj <J=iJJ
                                                                           VJ 695; STi 47.17, 48.21
     roSene =*rw8ynch
                                                                      8581 rwps(h)   B, M                                   a\>3j
       (<?/)brass
       TSP 2.527                                                           rup(a)s ©Parth. robas\ Khot. ruvasa-, Khwar.
                                                                             ob.
                                                                             rwbs;-y(h)
                                                                                     Oss. robds; Skt. lopasd; *raupasa ©f. n.;
 8569 rwSynch B
y     roSenc ©f. adj. ^rwSy^k
                                                       J5UJ                fox
       (o/)brass, brazen
                                                                           GMS 121; TSP 2.772, 13.18; Frag. Len. 68, 18, 19;
       SCE 229; GMS 1058
                                                                             SCE 149; Hen. Tales. 475.15
8570 rwyn
                                                if 11 'iJtJ?         8582 rwpsy'kh S
       royn   ©Av. raoYna*, Pahl. roYn\ Khwar. rYn%                                                       *bj(<f ^js) <u*bj
                                                                          rupasyak
          Yaghn. ruYin ©ob. -y(y) =»Y>W rwyn                              (related to)fox
       fat, oil
                                                                           MDii B-3, 13, 14-5 p71, 73nl2-3; MDiii p63
       TSP 2.897; BSTBL, Padm. 40, 54, Dhy. 279; STi
          36.1, 43.9; BSTii 827.50: C2, 94V20, 21; KG                8583 rwr* =* rwrh
         550, 552, 572, 580; MDii A-5, 13; CII 1990 p85;             8584 rwrh B, M                              <jLjJ**\f<jJ>
         Gersh. Sogd. Cpds. 1945, 147                                     yriira (rwr>) ©Av. urvard-      ©f. n.«, ob. -yh\ pi.
8571 rwysn B, S                                                             -t(t), -th =»>rwr(h)
                                         ^jj^jj
     roxsn- ©Av. raoxsna-, Parth. MP rosn ©nom.                           drug, medical plant
       ob. -y                                                             TSP 3.215, 272, 275, 279, 174, 6.186, 1881;
       bright, light                                                        BSTBL, Padm. 5, 32, Dhu. 261; GMS 99, 221,
                                                                            492, 1175; BBB p62, 517
       TSP 25ii, 4, 14.33; O1 16; W~Li; Frag. Len. 93.16
                                                                     8585 rwrt M                                      f^
8572 rwYsn}Yr6mn(h) B, S(M)                           ,:.,^,              shameless
     ru/oxsna-yar8man ©ob. -yh, ~wh
                                                                           BBB p92 b93
       =»rwxsn)Yr8mn, rywsn^rSmn
       paradise                                                      8586 rwrty'mync M                   c/j>> «u^A* 'fA*
       Hen. Tales. 476.13.21; S W, HJ 1976, 46, 49, Frag.                 shameless, insolent
         4.5, 6.8                                                          BBB p92bia, GMS 1103; S W, Xwast. 1991,
8573 rwysntr        S                                          "jj          327c8
                                                                     8587 rwrtyh B                             ^i^^^
       roxsntar ©-y =*rwxsndr                       ^j^Jj
```


## [2026-09-14T01:58:59.203Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n 'rwt ' SOD_pages.txt | head -30; echo \"--- river in SOD ---\"; grep -n 'river' SOD_pages.txt | head -40",
 "description": "SOD grep rwt/river"
}
```


### [2026-09-14T01:58:59.269Z] TOOL RESULT

```
11445: 2680 prwt =» prH                                                        fra-ke5 ©adv. ^Pr'k1
17808:        4958 kt»rwt B -+ kt>r                                                destruction
28528:8600 rwt M, C                                        <;U-^j i*3J            STi 3.72; GMS 1111; STii 3.72
31242:     GMS 1014                                                         11; Sund. AoFviii, 1981, 23V7; inf. 0brwt C2,
35843:11060 ywn'yq      C                                     ^         11072 ywrdnn rwt                                  o>j'->jj
--- river in SOD ---
2185:      the designation of "Sogdiana" (7r.l0.15). H. W. Bailey           IL Its size as given by the traveller, from the river
2283:rivers" as Hayatilah. In the second half of the fifth         element played is shown, for instance, by the Sogdian
2290:recognized as a ruler in Transoxiana. The Oxus river          Iran may have accelerated the process of
2397:        Yaghnab, a tributary of the Zarafshan river in                       "Uigur" respectively. See A. von Gabain, Altturkische
2713:Muller published "Soghische Texte I" (abbreviated                  river.80 Over 76 documents were found, written on
4420:     river ?                                                                {name of an)illncss, glow
19406:        Marv river
20408:                                                                         river
28530:     river                                                                  ruxst ? ^ryw^nt
35846:       C2, 1R9                                                          Jordan  river
36647:        shore, river bank                                                    zinak   =4zyn}kh, znw
38683:Jordan river      11072                killer of man  5472                     koumiss    3284
38869:Marv river     5477                        7649, 7799, 9386                         3067,3282, 11175
39295: river   217, 5824, 8600                  Rust 8591
39297: river bank     11325                     Rustam   8589
```


## [2026-09-14T01:59:05.754Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if '8600 rwt' in p:\n        print('LEAF',i)\n        import re\n        idx=p.find('8600 rwt')\n        print(p[:200])\n        print('...')\n        print(p[max(0,idx-600):idx+700])\n        break\nEOF",
 "description": "Locate SOD entry 8600 rwt page"
}
```


### [2026-09-14T01:59:06.916Z] TOOL RESULT

```
LEAF 413
 rwsty(h)                                                                                                                     346

         TSP 13.2, 5, 24, 25, 26, 28 ii 4, 1 1, 12                   
...
98                                                             W-Lii 546, 547.25, 548.19, 564, -A, MSP b28
8599 rwsnyr'yw S(M)                       <S~*3J u~*> iCT'3J j*41
                                                                              b97; CII 1990 p67 G4-5
     rosn-yriw                                                         8610 rwxsny^y* C                           jll^jh^3j
                                                                            roxsnyakya
     light souliviva anima)
        Sund. KG 607-8 pl89; AoF, 1979, 120 n49                             brightness
8600 rwt M, C                                        <;U-^j i*3J            STi 3.72; GMS 1111; STii 3.72
     rot (rwwt) ©<OP rautah-            ©ob. -y                        8611 rwxst- C                            j* j^y iqx*z±~^
     river                                                                  ruxst ? ^ryw^nt
        GMS 39, 530; STii 1.20; BSTii 860.35, 879.11: C2
                                                                            (/a)shine
          gloss. 22V7, 12, 23R11, 12, 23V5, 53R6, 87V11;                    BSTi 31; Benv. JA 1943-5; S W, IIJ 1976, 57n 60
```


## [2026-09-14T01:59:14.065Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD around 4479 ===\"; sed -n '4465,4495p' PHD.txt; echo \"=== PHD_mackenzie rōd ===\"; grep -n \"rōd\\|rōt\\|'lwt\" PHD_mackenzie.txt | head -20",
 "description": "MacKenzie rod"
}
```


### [2026-09-14T01:59:14.133Z] TOOL RESULT

```
=== PHD around 4479 ===
Musu» 0530
13710 eo eD ae vu vot 145 000 Mor -Qr (9с -rar ute» rar
tagīg
tag
takēk tagarg
-tar
tar, tarr tarazén- tarāzēnīdan tarāzūg piht
targ
tars
dat targumān tarwēn- tarwēnīdan trufš truftag truš
talag, tarrag talagčīn tarmānīh tarmenišnīh tarmenišn
tars-
[181]
ves v p үө шее
rod
ўе
tanómandih tanbahr tund tundih tanīhā tandrustīh tandrust tandrust tanīg tanuk tanūr tantūhmag Tür Tiran tórag, Turk -tom
tom, tom tumbag tof
toz
töz- tõzišn töšag
tušt
tagigih
PAHLAVI KEY
[180] MY G t^ tt?
Say jue we
^07 ug
NJU tw? A132? qt up We»? үр HIP МС qt ue
\ 25110
nr
Sur
ISS iy? ur
=== PHD_mackenzie rōd ===
981: IUldag ['lwth l ] defiled, polluted.
1054:an-aUld ['n'lwt l] undefiled.
3999:paliidag [p'lwtk l I N -a] starch jelly, flummery.
4000:piUiidan, palay- [p'lwtn', p'l'd- I (M p'rwdn, p'r'y-), N --] strain, filter,
```


## [2026-09-14T01:59:15.982Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('N',len(pages))\nfor i in (424,425,426,427,428):\n    p=pages[i]\n    print('=== LEAF',i,'===')\n    print(p[:900])\nEOF",
 "description": "BQT vol2 leaves near p.969"
}
```


### [2026-09-14T01:59:17.104Z] TOOL RESULT

```
N 684
=== LEAF 424 ===
    ‫سوه‬                                                                                                ‫ردان خاك بیز‬
‫و دام‬       ‫وباین‌معتی با زای قطمرار هم مده است ‪-‬‬                   ‫وعلم پادشاهی هم هست ‪ .‬کوبند در جزیره‌ای از‬
 ‫کیاهی است بهاری که اکثر چرندکان خصوصاً‬                              ‫جزابر اودرختی است که بارآن درخت‌مرغ است‬
            ‫کوسفند بچریدن‌آن فربه وگرد‬
 ‫نهو‪-‬عی ازچرم‬                                                                             ‫‪.‬‬     ‫ودیگر عجایبات هم هت‬
                                         ‫باشد سیاه رنگه ‪.‬‬            ‫نردان خا پکیزنابه از باريك‬
 ‫گ" بروزن خندیدن» ‪:‬هنی‬                    ‫دن‬
                                           ‫بلد‬
                                             ‫ر‬                       ‫بینان ودفیق نظران کوالکه دقیقه‌ای ازدقایق‬
 ‫تراشیدن باشد ‪ -‬و بسمنیوستنهمعست‪(٩)-‬‏‬                   
=== LEAF 425 ===
‫رنگه رییع‬                                                                                    ‫‪-0‬‬
                                                                                              ‫‪‎‬ی ‪٩‬‬


                                      ‫‪.‬‬     ‫ویات‬
                                               ‫خ‬       ‫‪ ۱-7‬طرزوروش‬         ‫بوشند ‪۰‬‬    ‫ژنده‌ای که دروشان‬

                                                        ‫‪-‬ثل‬
                                                          ‫‪ ۲۱‬م‬        ‫و سرت وقاعده و فالون باشد ‪۰‬‬
                                                          ‫یر‬
                                                           ‫ش‪-‬‬‫‪.‬‏ ‪۳۱‬‬            ‫ناند‬
                                                                                 ‫ور‬‫گبه‬
                                                                                     ‫ومانشد ونظر وش
=== LEAF 426 ===
   ‫نت‬                                                                                          ‫رنگه رزگلگون‬


                                                           ‫نگ رر گلگون ‪-‬کنابه از راب‬
                                                                                   ‫ر‬
                    ‫تاریکی وتیر گی هوا باشد ‪.‬‬                              ‫فروش است و بعربی خمار گویند ‪.‬‬
 ‫رنگیدن = بر وزن لنگیدن ‪ ,‬روسدن‬                        ‫ر نگر و تا د بکر اول وسکون ثالی‬
                               ‫ورستن گیاء باشد ‪.‬‬
                                                       ‫فوفانی‬      ‫و‬   ‫بواو رصیده‬    ‫بی ناه‬    ‫رای‬       ‫‪1‬‬    ‫» فتح ثالی‬




‫ر نگینا = بانون بالف کشیده‪ .‬شفترنگه‬                    ‫در‬      ‫معروف‬       ‫است‬      ‫جاتوری‬    ‫آن‬     ‫و‬       ‫»‬   ‫گوند‬   ‫را‬

          ‫بادد » وآن میوهء‌ایست شبیه بشفتالو ‪.‬‬             ‫
=== LEAF 427 ===
 ‫روادان‬                                                                                                                     ‫=‪“۷‬‬

 ‫ویآنشتر دآربهای‬
               ‫پلای ‪ ۰‬رستنیی باشد ب‬                                 ‫= بروزن هوا؛ بمعنی‌جایزوجاری‬                            ‫روا‬
‫استاده روید و بمربی جرجیرالماء و کرفس‌الماء‬                         ‫ورواح وروان باشد ‪ -‬ویمعتی حصول‌کار هم‌هست‬
                                                ‫خوانند ‪. ۷‬‬          ‫همچون‌کام روا وبضم اول درعربی دیدار وخویی‬
‫رواق ‪ -‬بکسر اول بر وزن عراق ‪۰‬‬                                       ‫بی سيراب‬  ‫عمردر‬‫منظر باشد ‪ - ۴‬وبکسر اول ه‬
‫وابوایکه درمر تة‬            ‫پیشگاه خانه را گو‪.‬ند ‪9 ۲‬‬                ‫شدن را کوبند ‪ - ۴‬ر ریسماییکه بدان باربر‬
                                   ‫‪۰‬‬    ‫ساخته باشند‬      ‫دوم‬                                                           ‫شتربندن
=== LEAF 428 ===
  ‫سره‬                                                                                    ‫روان آورد‬

                     ‫داشن را فيز گویند ‪٩‬‏‬        ‫سیفتح واو وسکون را‬         ‫روان ورد‬
‫رو با د بض اول و بای ابجد بالف‬                   ‫بخرد و دانا و صاعب‬      ‫حکیم و‬     ‫و دال بی‌شطه ‪,‬‬


           ‫کشیده ‪ ,‬بمعنی روباه تربك است‬
                                                                                    ‫و‬   ‫را گونند‬   ‫عقل‬



           ‫عنبالملب خوانند در اختبارات ‪۰#‬‬        ‫روان بخش ‪ ۰ ۱‬فدرمخته‌ایت که‬
‫رو باه تر بك ‪ -‬نم تای فرشت (‪)4‬‬                    ‫علم وداش با اوست وبعربی اورا (‪ )۱‬روح‌القدس‬
                                                                                             ‫خوالند ‪.‬‬
‫و فتح بای ابجد(ه) وسکون کاف؛ سگه انکور‬
‫باشد )‪(٩‬‏ چه تربك بمعنی انگور باشد‪.‬و بعربی‬        ‫روان بد ‪ - ۲‬ینم بای ابجد ()‬
        ‫علتع
```


## [2026-09-14T01:59:24.622Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(425,445):\n    p=pages[i]\n    if 'رودبار' in p or 'رودخانه' in p or 'رود ' in p:\n        print('=== LEAF',i,'=== has rud markers')\n        print(p[:1200])\n        print()\nEOF",
 "description": "Find BQT rud page"
}
```


### [2026-09-14T01:59:25.736Z] TOOL RESULT

```
=== LEAF 427 === has rud markers
 ‫روادان‬                                                                                                                     ‫=‪“۷‬‬

 ‫ویآنشتر دآربهای‬
               ‫پلای ‪ ۰‬رستنیی باشد ب‬                                 ‫= بروزن هوا؛ بمعنی‌جایزوجاری‬                            ‫روا‬
‫استاده روید و بمربی جرجیرالماء و کرفس‌الماء‬                         ‫ورواح وروان باشد ‪ -‬ویمعتی حصول‌کار هم‌هست‬
                                                ‫خوانند ‪. ۷‬‬          ‫همچون‌کام روا وبضم اول درعربی دیدار وخویی‬
‫رواق ‪ -‬بکسر اول بر وزن عراق ‪۰‬‬                                       ‫بی سيراب‬  ‫عمردر‬‫منظر باشد ‪ - ۴‬وبکسر اول ه‬
‫وابوایکه درمر تة‬            ‫پیشگاه خانه را گو‪.‬ند ‪9 ۲‬‬                ‫شدن را کوبند ‪ - ۴‬ر ریسماییکه بدان باربر‬
                                   ‫‪۰‬‬    ‫ساخته باشند‬      ‫دوم‬                                                           ‫شتربندند ‪. ۴‬‬
                                                                    ‫رواد ‪ -‬بفتح اول بروزن سواد » زمین‬
‫رواق لی‌ستون ‪ -‬کنابه ازآسان‬
                                                                    ‫پت و بلند وپشتهپعتةٌپرآب و علف باشد ‪-‬‬
                                           

=== LEAF 429 === has rud markers
  ‫رود بار‬                                                                                            ‫‪4‬‬
‫لخت پپلوی است ومر کب است از روخ و چاو ‪--‬‬                      ‫بویان ‪ = ۱‬بکراك بروزن‌رومیان‪.‬‬
                                                                                          ‫ر‬
  ‫کویخاه بلند سادة‬
                 ‫بممتی تارك سر ساده » چه ر‬                    ‫بمعنی اربیان است که ملخ آبی باشد و بعریی‬
  ‫بی‌برگے وباراست وچکاد بالای پیشانی که ترديك‬                ‫جرادالیحر خوانند ‪ .‬چون آنرا با نخود سياه‬
                              ‫بتارك سر باشد ‪.‬‬                 ‫بکوبند و برلاف ضماد کنند حب‌القرع رابیرون‬
  ‫رود سم اول و سکون ثالی مجپول‬                                                                        ‫‪¥.‬‬   ‫آورد‬




 ‫و دال ابجد (‪ ۰ )۳‬حر رودخانةٌ عظیم و سیال را‬                 ‫روج = با جيم » بروزن و معنی روز‬
       ‫گویذد نوا ‪ , ۱‬و رودخانۀآ مو را ‪۷‬‬                      ‫است که بعربی‪ :‬نخهاورانند ‪ - ۴‬و بهندی یله‬
 ‫و فرزند را نیز گوبند‪ - ۷‬و نام سازی است که‬                                 ‫که کاو کوهی باشف ‪۰‬‬    ‫کاو را گونن‬


  ‫فند و غیره باشد ‪-‬‬ ‫سود‬
                      ‫ور‬‫کعنی‬
                           ‫

=== LEAF 430 === has rud markers
    ‫سه‬                                                                                                   ‫رودزم‬

                         ‫مفرد روده همگفته‌اند ‪:‬‬         ‫کوحار » نامبلوکی است و شهری است مابین‬
‫رودلاخ ‪ - ۴‬بلام بالفکید وبخای‬                            ‫گیلان وقزوین‪ -‬وبمعنی جداول آب ورودخانهای‬
 ‫یطه دار زده ‪ ۰‬جابیکه دران رودخانه و جشمه‬
                                          ‫نق‬             ‫بز رکے وجابیکه درآن رودخاله (‪ )۱‬بیارجاری‬
                                                                                          ‫باشد ‪#.‬‬
                           ‫‪ 3‬زهاب مار باشد ‪۰‬‬

‫باشد»‬   ‫رونای‬   ‫بروزن سوزن»‬          ‫رودن‬
                                                         ‫رودزم ‪ -‬بكر () ثالك و تم‬
‫وآن کاهی است که چیزها بدان رنگه کنند ‪1‬‬                    ‫زای‌فارسی وسکون میم نامرودخاله است‌مشهور‪.‬‬

 ‫‌ بادال ابجد بروزن‌هوشنگه‪,‬‬       ‫رودن‬
                                                         ‫رودساد ‪ -‬با سین بی‌قطه (‪ )۳‬بالف‬
                                                         ‫وسازنده‬   ‫مطرب‬      ‫نقطه‌دار(‪ )4‬رده‬    ‫ویزای‬     ‫که‬
             ‫باشد‬   ‫است که رونای‬        ‫یمه‌نی رودن‬
          

=== LEAF 431 === has rud markers
     ‫روز خوش‬                                                                                           ‫‪-4۷۱-‬‬
      ‫لش مد و او را در‬   ‫و غراشان‬         ‫ویادشاهان(‪)۳‬‬
                                                           ‫رو ر ‪ -‬ممروفت و بعربی نهار وبوم‬
      ‫زمان دربان خوانند و روزبانان جمع ِ‬                  ‫فنتیاب همهت چنانکه گوبند‬     ‫آمع‬
                                                                                         ‫گوبند ‪ -‬وی‬
     ‫گا‪-‬هبان‪-‬‬
            ‫دربانان باشد‪ .‬وسر هنگه‪ -‬ووچانوش‬                ‫دروز برآهد» مرادآن باشدکه آفتاب برآهد ‪-‬‬
 ‫و شقیم را گوبند ‪ -‬و بمعتی جلاد هآمده‬                      ‫کونایه از ظاهر وآشکارا وروشن باشد ‪ -‬وبمعنی‬
                                             ‫است ‪. ۴‬‬       ‫روز کارهم هت ت که کنابه ازفرصتباشد چنانکه‬

‫دون وک خت ارم ین‬                                          ‫کونند « امروز روز فلالی استت» بعثی روز گار‬
                                                                            ‫‪.:‬‬   ‫ازو ات‬      ‫وفرصست‬        ‫قلالی است‬
‫بی غل‬       ‫ست‬
             ‫رو‬‫دست‬
                 ‫را‬             ‫د‬
                                ‫که‬‫متر‬
                         

=== LEAF 432 === has rud markers
 ‫‪“AYY‬‬                                                                                                     ‫روز خون‬

‫معروف‌است کهزمانة نایدارباشد؟ ‪-‬ومدت‌وفرصترا‬                 ‫وور خون ‪ -‬بسکون الك ‪ .‬تاخت‬
                                                           ‫بردن در روز باشد بر سر غچنينمانکه ابشان‬
‫که‌آن چیز و آن کی در ان بوده باشد همحجو‬                    ‫بی‌خبر وغافل باشند ‪ -‬و عاخت بردن در شب را‬
‫تسغمیر و امثال آن ‪-‬‬          ‫روز کار جوالی و ِ‬                                                    ‫شبخون گوبند ‪.‬‬
            ‫ِ‪.‬‬     ‫وباکاف تازی روز جنکه راا‬                 ‫رورذاد = بدااد ابجد (‪ )۱‬بر وزن‬
                                                                    ‫هوشیار » خدمتکار وبند گانرا گویند ‪.‬‬
                         ‫واوقات ضایم کردن باشد ‪.‬‬            ‫رور در نگ بكر ات ک‪۰‬نابه‬
                  ‫رفتگان‬        ‫رور ګار‬                                                        ‫از روز قیامت باشد ‪.‬‬
                   ‫باشد ج‬   ‫ما حصلان‬     ‫بی‌دولتان وی‬       ‫ررورح = بسکون‌الت‪ .‬روشنیوشفافی‬
‫رور گرد = بسکون‌تالك وکاف فارسی‬                             ‫ونابه از سرخروی(‪)۲‬‬
                                          

=== LEAF 433 === has rud markers
 ‫روز مریم‬                                                                           ‫‪avr‬‬
                                   ‫باشد ‪.#‬‬       ‫رور ننگ و نام ‪ - ۱‬بکراك‪‎.‬‬
                                                 ‫بمعنی روز کوشش است ککنهابه از ررز جنگ‬
‫وعم وسکون را وزا ودال ابجد‪ ,‬نام روزیتجشنیه‬     ‫وجدال وقتال و کینه خواستن باشد ‪ -‬و روز غنا‬
                                                   ‫ند‪.‬‬
                                                     ‫یام‬
                                                       ‫گهوون‬
                                                           ‫مزیشگ‬
                                                               ‫وساز وصحبت را یز رو‬
                                   ‫است ؟ ‪.‬‬
                                                  ‫نی‬
                                                   ‫نګ و فيرف»نش‬                    ‫رور‬
‫رود هریم ‪ -‬کنایه از خناموشی‬                              ‫وکوشش‬    ‫بر جنگ‬

‫وسکوت باشد؟ ‪ -‬کونابه از مرکهوموت حم‬             ‫رو ر نه ؟ د بفتح اول و تال و لون‬
                                   ‫‪4‬‬   ‫هت‬        ‫وسکون تانی ‪ ۰‬معروفت که مطلق‌سوراخ ومنقثة‬


  ‫‪۲‬شمار ‪۷‬‬
        ‫‪:‬وزن ‪»( ۳

=== LEAF 441 === has rud markers
                                                                                               ‫‪۷‬‬


                                 ‫جشم امتت‪ .‬ء‬      ‫همچو باطنش‬           ‫رآن‬
                                                                         ‫ایهکه‬
                                                                             ‫ظر چ‬
                                                                                ‫و نم اول ه‬
 ‫رومی خوی کی رګاوندکه‬                                                                              ‫لباشد ‪.‬‬

‫دورنگه ومتلون مزاج‌باشد وبهر کهرسد برنگه‬          ‫روم = نم اول وئالی مجهول بر وزن‬
                              ‫وخوی اوشود ‪.‬‬        ‫موم » موی زهار باشد ‪ - ۱‬و با ثانی معروف‬
‫رومی رن رعنا د کنابه ازآفتاب‬                      ‫ملکی است مشهور بحدود شام‪ - ۴‬ومخفف رویم‬
                             ‫عالم تاب است ‪.‬‬       ‫هم هت یمنی روی هن ‪ -‬وبفتح اول نام درختی‬
‫روهینا ‪ -‬بروزن بوسیناه بمعنی زدوده‬               ‫نت » و بعضی گویند‬         ‫آکی‬‫رل م‬
                                                                                 ‫م مق‬
                                                                                    

=== LEAF 442 === has rud markers
 ‫‪AA‬‬                                                                                                  ‫رواس‪‎‬‬

 ‫فته اند که‬
          ‫ګم‬‫کوبند «رون‌آن» بمنی سبب آن وباعث آن ‪١‬‏ | عسیب خوانند؟ ؛ و بکر اول ه‬
                                    ‫بروزن شکنج‬       ‫و با ثالی مجهول‪ .‬نام قصه‌ایست درهندوستان که‬

                         ‫ر‬
‫توجو ‪ - ۴‬بفتح اول وضمجیمبر‬                                                        ‫مولد ابوالفرح ب(ود‪. )۱‬‬
‫وزن سمن بو » کرمی باشد چوب خوار و بعربی‬                            ‫‪۱‬‬                ‫‪.‬‬          ‫ر‬
                                                                                           ‫نواس؟‬
                                   ‫ارضه گویتدش ‪.‬‬                                        ‫بضم اول وئالی مجهول‬


‫سیاره باشد که زحل و مشتری ومریخ و آفتاب‬                   ‫رز‬                         ‫ورسین بی لقطةٌ زده ‪.‬‬
                 ‫وزهره وعطارد وماه است ‪.‬‬                   ‫دج ‪(€7‬‬                   ‫کیاهی‌است‌معروف که‬
 ‫رو نما ‪ -‬و روی‌لها ک‪.‬نابه از (‪)۳‬‬                                                       ‫بدان جامه و ابریشم‬
 ‫هد به وتحفه‌است که در وقت دیدن روی عروی‬                     ‫رولای‬

=== LEAF 443 === has rud markers
  ‫رورشنه‬                                                                                            ‫”‪~A‬‬

                                                                ‫جو بنده‪ .‬کشت وزراعت پزرور و بالیده را‬
 ‫روا ‪ ۳‬وعزهبنر‌بوبا(‪ .)4‬بمعني‌روینده‬
 ‫باشد بعنی هرچیز که آززمین بروبد (‪ - )0‬ودر‬
                      ‫‪۳‬‬   ‫دبدترا گویند ‪۸‬‬       ‫عر هی خواب‬        ‫وکر ثالث ونون بتحتالی رسیده ‪ ۰‬آهن وپولاد‬
‫بنك = یمعای رو بنداست کهآ نرا‬                  ‫دوی‬

                                                                 ‫روهینا = بائالی‌مجهول بروزن موستنا»‬
 ‫روی پوش ‪ -‬بمعنی روپوش است‬                                       ‫بمعنی روهنی است که‌آهن وفولاد جوهردار باشد‬


 ‫کونایه اکزی چویزی که ظاهر وباطنش یکی‬                            ‫روهینابی(‪ - )۷‬وشمشر جرا قیمتی را نیز‬
                                                     ‫نباشد ‪.‬‬    ‫کفتماند‪ .‬وروهینیا بدو بای حطی هم بنظرآمده‬
 ‫روی خاندان د یکرنات ‪,‬کنابه‬                                                                             ‫است‪. .‬‬
 ‫از بپترین و اشرف ودودمان و خالدان باشد ‪.‬‬
                                                                 ‫رو هینی نز = عم اول وسکون انی‬
 ‫روی دل نمودن
```


## [2026-09-14T01:59:38.109Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\np=pages[429]\nprint(p[1000:4000])\nEOF",
 "description": "BQT leaf 429 rest"
}
```


### [2026-09-14T01:59:39.208Z] TOOL RESULT

```
 نیز گوبند‪ - ۷‬و نام سازی است که‬                                 ‫که کاو کوهی باشف ‪۰‬‬    ‫کاو را گونن‬


  ‫فند و غیره باشد ‪-‬‬ ‫سود‬
                      ‫ور‬‫کعنی‬
                           ‫نوازند ‪ -‬و بم‬                     ‫الی و حای‬    ‫و سکون‬    ‫سم اول‬   ‫=‬   ‫روح‬

 ‫واری که برروی ساز ها‬
                    ‫و زه کومان حلاجی ت‬                       ‫حطی» نام پرده‌ای باشد از برده‌های موسیقی رد‪5‬‬
 ‫پرو موی او را‬           ‫‪ -‬وفمرنغدویکه‬
                                     ‫وس‬‫کند‬
                                         ‫کش‬                                  ‫عربی تفس ناطقه را گویند ‪.‬‬     ‫ودر‬

  ‫تمام کنده باشند و بروغن بربان کرده باشندھ ‪.‬‬
                                                              ‫روح هکرم ‪ -‬بکر حایحطی(‪:)۱‬‬
  ‫رودا به = بر وزن دوشابه ‪ ۰‬نام دختر‬                                      ‫کنابه از جبرئیل عایه‌اللام است ‪.‬‬
  ‫وستم‬‫مپراب کابلی است که زال او را خواست ر‬
                                                              ‫روخ ‪ = ۴‬بضم اول وسکون‌نانی وخای‬
 ‫ازو تولد یافت ‪ -‬و نام قلعه ایست که رودابه در‬                ‫قطه دار ک‪,‬یاهی است بلند واز بر گے وبارخالی‬
                                   ‫آن توطن داشته ‪.‬‬
                                                             ‫ودرمیان آب میروید و از آن حصیر میبافند ‪.‬‬
 ‫رود]ورد‪ .‬پفتح واو و کون را‬                                  ‫در خراسان الگور و خریزه بدان آونگه‬
 ‫ودال‌هردوبی نقطه" نام‌رودخاله‌ایست ودرمو بدالفضلا‬
                    ‫بحذف دال آخر نوشته الد ‪.‬‬
                                                             ‫روخ چکاد * = باجیم فارسی وکاف‬
‫رود] هو = بضم هاوسکون واو » نام‬                              ‫بروزن کور سواد ‪ ۰‬کسی راکوبند که ميان سراو‬
                                     ‫‪۰‬‬   ‫رودخاله‌ابست‬
                                                             ‫اسلم‬    ‫ری‬
                                                                      ‫نداشته باشد و او راآدم سر و‬          ‫موی‬

 ‫رود بار ‪٩‬‏ ه بباای ابجد بر وزن‬                              ‫خوانند با صاد و عین بی نقطه (‪ .)۲‬گویند این‬
            ‫(‪ )۳‬چك ‪ - :‬ابجد ‪.‬‬              ‫(‪ )۲‬جك ‪ - :‬بی‌نقعاه ‪۰‬‬               ‫(‪ )۱‬چك‪ :‬بگر حا‪.‬‬

                   ‫ورك‪ :‬اریبان در کتاب حاضر ولغت نامه‪.‬‬          ‫‪Jd homard‬صس‏ ‪۷۱۰‬‬             ‫=‬   ‫‏‪٩‬‬

      ‫لوخ‪ .‬و رك‪ :‬دوخ‪.‬‬    ‫رخ‬     ‫‪ ۳‬ےت رك‪:‬‬         ‫رك راه روح ‪.‬‬         ‫‪۴‬‬           ‫رك ‪ :‬روز‪.‬‬
                                                                                          ‫‪- ۴‬‬
   ‫‪ - ۱‬پپلوی‬              ‫‪ :‬روخ جکاد ‪.‬‬      ‫‪ ۲ :۱‬ص‪۸۹۱‬‬         ‫‪:‬ا‬
                                                               ‫اكسف‬
                                                                  ‫© _رك‪ :‬دوخ جکاد )‪ (۱‬ور‬
   ‫‏‪( ٤‬رود) “ پارسی باستان ‪« 12]218۲-‬بارتولمه ‪ ۰۹4۱2۰‬هندی باستان_‪( 58]679‬جربان آب»‬
        ‫‪.‬‬     ‫ارحنی غ ‪tor‬‏ (رود)«هوشمان ‪۷‬‬               ‫مسر روده رود)‪ .‬کردی ‪ ۵41‬بلوچی‪« ۵۲‬اسشق ‪۷۲‬
```


## [2026-09-14T01:59:39.896Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON روضه ===\"; grep -n 'روضه' MON_part1.txt | head -10; echo \"=== MON رمیدن ===\"; grep -n 'رمیدن' MON_part1.txt | head -10; echo \"=== MON رود ===\"; grep -n '^رود\\|رود (' MON_part1.txt | head -10",
 "description": "Mo'in greps"
}
```


### [2026-09-14T01:59:40.001Z] TOOL RESULT

```
=== MON روضه ===
28815:(حامص.) روضه‌خوانی و خوانندگی کردن 
34974:(روضه‌خوانی) پامنبری اطفالی که پیش از 
34975:اقامهٌ روضه يا تعزیه به جماعت می‌خوانند. 
43046:که در آن مراسم عزا و روضه‌خوانی برپا 
51202:منبر و روضه‌خوانی است به نیت براورده 
62979:و تکرار کردن (در روضه‌خوانی» عزاداری يا 
63756:مجالس عمومی (مانند روضه‌خوانی) بکار 
64999:روضه‌خوان. 
69105:روصه: (۲۵۳2۵)۲۵۷۵ [ع. . روضه] (.) باغ» 
69106:گلزار؟ج. رباضء روضات. روضه 4 باغ رفیع: 
=== MON رمیدن ===
3275:شدن با...» آرمیدن با... اسودن دل: خوش 
7029:(مص م.) آرمیدن با زن. آوردن. کردن کاری 
11756:خواستن» آرمیدن. (امسص.) آسایش؛ 
12655:شدن؛ رمیدن. (امص.) وحشت 
13598:اشمئراز: عقعصه ۰] (مص‌ل.) رمیدن» 
43843:تنافر: 290۲( [ع. ۰] (مص‌ل.) از هم رمیدن» 
44210:رمیدن» بیزار بودن؛ کراهت داشتن. (امص.) 
51271:شدن» رفتن. جنبیدن. رمیدن. لایق بودن» 
68401:رم «ه (اسص.) رمیدن» گریز. نفرت» 
68462:رمیدن: 7- ۲۵۱0 (مص‌ل.) فرو ربختن 
=== MON رود ===
1402:رودخانه (فره.) 
1483:روده تالاب و امثال آن زهد یعنی تراود؛ 
3839:رود ولی اجازة باز گشت نمی دهد. 
4096:رود و نیز برای آهار دادن بارچه‌ها استعمال 
4253:رود (غعفص.): آهن آلات؛ بلورالات؛ 
4685:رود. بیمارستان سیار. 
5187:رود آهمنگ. (مست.) هر یک از 
6231:روده» آورده؛ مق , آستر» بطانه. 
6796:روده). نضصرت» نضارت. کثرت مال؛ ملکك. 
10968:رود.
```


## [2026-09-14T01:59:53.235Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON rowze ctx ===\"; sed -n '69100,69112p' MON_part1.txt; echo \"=== MON ram ctx ===\"; sed -n '68395,68410p' MON_part1.txt; sed -n '68458,68470p' MON_part1.txt; echo \"=== روماتیسم / ریتم ===\"; grep -n 'روماتیسم\\|ریتم\\|رتم' MON_part1.txt | head -10",
 "description": "Mo'in entries for rowze, ram, rheumatism"
}
```


### [2026-09-14T01:59:53.359Z] TOOL RESULT

```
=== MON rowze ctx ===
روصه ۱ فر هنک فارسی معین ۱۷۲۱ 


آنکه دارای اند شه‌ای روشن است. کسی که 
در امور با نظر باز و متجددانه نگرد. 
روصه: (۲۵۳2۵)۲۵۷۵ [ع. . روضه] (.) باغ» 
گلزار؟ج. رباضء روضات. روضه 4 باغ رفیع: 
(کد.) بهشت. (کد.) قبر» گور. روضة ترکیب: 
غالب مردم» جسد آدمی. روضه حور: (کد.) 
بهشت. روضه دوزخ‌بار: (کد.) شمشیر آبدار. 
روضه رضوان: (کد.) بهشت. روضة فیروزه 
رنگ: (کد.) آسمان. خطبه‌ای که در مراسم 
عزاداری بالای منبر خوانند و آن شامل حمد 
=== MON ram ctx ===
به عهده دارد. وظیفه» عمل. (مک.) آلتی که 


راننده به وسیلةً آن ماشین را به هر طرف که 
بخواهد حرکت دهد) فرمان. 

رم «ه (اسص.) رمیدن» گریز. نفرت» 
اکراه. 

رم: س«: (.) گسله چارپایان؛ رمه. گروه؛ 
دسته. 

رم: 2-0 (- ریم] () چرکک زخم» ریم. 

رم ۵۵ (.) نوشابه‌ای الکلی که از تقطیر 
تشگ ساخته شود. 

رمایه: (0-)«رقسه: [ع. رماية] (مصل.) تیر 
انداختن. (امص.) تبراندازی. 

رمیدن: 7- ۲۵۱0 (مص‌ل.) فرو ربختن 
سقف و دیوار. 

رمح: جاسم۲ [ع.] )۱( نیز ۵) ج. آرماح. رماح. 
رمك: ۲2۵۵4 (ع.] (.) (یز.) درد چشم. (بز.) 
ورمی که در طبقه ملتحمه پدید آید. 

رمز: ۰۳2 [ع.) (مصل.) پوشیده گفتن) 
پوشیده نمودن؛ به وسبله لب» چشم ابرو» 
=== روماتیسم / ریتم ===
1941:آپارتمان: 0 (.) (معم.) قسمتی 
6638:اپارتمان: 0 (ا.) ساختمان چند 
9608:ارتماس: سوت [ع. ۰[ (مسصم.) به آب 
9611:ارتماسی: وت [غ. ف.] (ص‌نسه.) 
9612:منسوب به ارتماس. سل ارتماسی: (فق.) 
9659:ارتماطیقی: ۵۳27 (معر.) علم 
29123:پایزه: (ه)مع رتم ,(یمتردر (- پاچه - 
40512:نستر غیده: (0-)02]-رتمادها (امف.) درهم 
42534:کردن» نزدیک گردانیدن. یورتمه بردن 
43473:آنکه رتمام) مصدر است» چون در فارسی
```


## [2026-09-14T02:00:02.986Z] TOOL CALL #35: Bash

```json
{
 "command": "sed -n '1,60p' tools/fetch_source.py",
 "description": "Inspect fetch_source.py"
}
```


### [2026-09-14T02:00:03.057Z] TOOL RESULT

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
    fetch_url = urllib.parse.urlunsplit((parts.scheme, parts.netloc.encode("idna").decode(),
                                         urllib.parse.quote(parts.path, safe="/%:@!$&'()*+,;="),
                                         urllib.parse.quote(parts.query, safe="=&%:/?+"), parts.fragment))
    os.makedirs(WEB, exist_ok=True)
    path = os.path.join(WEB, h + ".txt")
    if os.path.exists(path) and time.time() - os.path.getmtime(path) < 86400:
        print(path); return 0
    status, title, text = 0, "", ""
    try:
        req = urllib.request.Request(fetch_url, headers={"User-Agent": UA, "Accept-Language": "en"})
        with urllib.request.urlopen(req, timeout=60) as r:
            status = r.status
            raw = r.read(4_000_000)
            ctype = r.headers.get("Content-Type", "")
            enc = "utf-8"
            m = re.search(r"charset=([\w-]+)", ctype)
            if m: enc = m.group(1)
            body = raw.decode(enc, errors="replace")
            if "html" in ctype or body.lstrip().lower().startswith("<!doctype html") or "<html" in body[:2000].lower():
                mt = re.search(r"(?is)<title>(.*?)</title>", body)
```


## [2026-09-14T02:00:08.665Z] TOOL CALL #36: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/srew-\" \\\n \"https://en.wiktionary.org/wiki/%D8%B1%D9%88%D8%AF\" \\\n \"https://en.wiktionary.org/wiki/%D8%B1%D9%85%DB%8C%D8%AF%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D8%B1%D9%88%D8%B6%D8%A9\" \\\n \"https://www.etymonline.com/word/rhythm\" \\\n \"https://www.etymonline.com/word/rheumatism\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 445, root Ser 1 / sreu-, nodes 1-17\" ; done",
 "description": "Archive web sources"
}
```


### [2026-09-14T02:00:11.981Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/583487ebcf6f48d3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4b3ffb8efb102073.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9af4871f2b20d347.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7833ffe91c163cca.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9fe127a480490d44.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/fd64323d9ab8bfe5.txt
```


## [2026-09-14T02:00:14.789Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 583487ebcf6f48d3 4b3ffb8efb102073 9af4871f2b20d347 7833ffe91c163cca; do echo \"######## $f\"; head -c 3500 $f.txt; echo; done",
 "description": "Read fetched wiktionary pages"
}
```


### [2026-09-14T02:00:15.887Z] TOOL RESULT

```
######## 583487ebcf6f48d3
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/srew-
FETCHED: 2026-09-14T02:00:10Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/srew- - Wiktionary, the free dictionary

Reconstruction:Proto-Indo-European/srew- - Wiktionary, the free dictionary 

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

 Personal tools 

 Donations 

 Create account 

 Log in 

 Contents

 move to sidebar 
 hide 

 Beginning

 1 
 Proto-Indo-European 

 Toggle Proto-Indo-European subsection 

 1.1 
 Etymology 

 1.2 
 Root 

 1.2.1 
 Derived terms 

 1.2.2 
 Descendants 

 1.3 
 References 

 1.4 
 Further reading 

 Toggle the table of contents 

 Reconstruction:Proto-Indo-European/ srew- 

 1 language 

 Türkçe 

 Reconstruction 

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
 Get shortened URL 

 Print/export

 Download as PDF 
 Printable version 

 In other projects

 Appearance

 move to sidebar 
 hide 

 From Wiktionary, the free dictionary

 This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.

 Proto-Indo-European
 [ edit ] 

 Etymology
 [ edit ] 

 According to one theory, derived from Proto-Indo-European *ser- , whence also Latin serum . [ 1 ] [ 2 ] 

 Root
 [ edit ] 

 *srew- [ 3 ] [ 4 ] 

 to flow , stream 

 Derived terms
 [ edit ] 

 Terms derived from the Proto-Indo-European root *srew- (49 c, 0 e) 

 *sréw-e-ti ( thematic root present ) 

 *sréw-mn̥   n ( “ stream ” , proterokinetic men-stem ) [ 4 ] [ 5 ] [ 6 ] [ 7 ] 
 Proto-Hellenic: *hréumə 
 Ancient Greek: ῥεῦμα ( rheûma ) ( see there for further descendants )

 Proto-Celtic: *srouman [ 8 ] ( see there for further descendants )

 *sre/ow-t(-)es- [ 4 ] 
 Proto-Indo-Iranian: *sráwtas ( see there for further descendants )

 *sréw-ti-s ~ *sru-téy-s [ 4 ] 
 Proto-Balto-Slavic: *srū́ˀtei ( with irregular acute ) ( see there for further descendants )

 Proto-Hellenic: *hréutis , *hrútis 
 Ancient Greek: ῥεῦσις ( rheûsis ) , ῥύσις ( rhúsis ) 
 Greek: ρύση ( rýsi ) 

 Proto-Indo-Iranian: *srutíš 
 Proto-Indo-Aryan: *srutíṣ 
 Sanskrit: स्रु॒ति ( srutí , “ stream, (out)flow, discharge; course, path; drain ” ) 

 *srow-m-eh₂ 
 Proto-Albanian: *srūmā 
 Albanian: rrymë , rrym 

 Proto-Balto-Slavic: *sraumā́ˀ 
 Latvian: stràuma [ 4 ] 

 *srow-mo-s 
 Proto-Germanic: *straumaz [ 4 ] ( see there for further descendants )

 *srow-men- 
 Proto-Balto-Slavic: *sraumen 
 Proto-Slavic: *strumy ( see there for further descendants )

 Thracian: 
 → Ancient Greek: Στρυμών ( Strumṓn ) 

 *srow-éh₂ [ 4 ] 
 Proto-Balto-Slavic: *srawā́ˀ 
 Latvian: strava , stràvа , strāva 

 Lithuanian: sravà 
 ⇒ Lithuanian: prasrava 

 Proto-Hellenic: *hrowā́ 
 Ancient Greek: ῥοή ( rhoḗ ) Greek: ροή ( roḯ ) 

 Proto-Indo-Iranian: *srawáH 
 Proto-Indo-Aryan: *srawáH 
 ⇒ Sanskrit: गिरिस्रवा ( girisrav�
######## 4b3ffb8efb102073
URL: https://en.wiktionary.org/wiki/%D8%B1%D9%88%D8%AF
FETCHED: 2026-09-14T01:30:30Z
STATUS: 200
TITLE: رود - Wiktionary, the free dictionary

رود - Wiktionary, the free dictionary 

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

 Personal tools 

 Donations 

 Create account 

 Log in 

 Contents

 move to sidebar 
 hide 

 Beginning

 1 
 Old Tati 

 Toggle Old Tati subsection 

 1.1 
 Etymology 

 1.2 
 Noun 

 2 
 Persian 

 Toggle Persian subsection 

 2.1 
 Etymology 

 2.2 
 Pronunciation 

 2.3 
 Noun 

 2.3.1 
 Synonyms 

 2.3.2 
 Derived terms 

 2.3.3 
 Descendants 

 2.4 
 Noun 

 3 
 Urdu 

 Toggle Urdu subsection 

 3.1 
 Etymology 

 3.2 
 Pronunciation 

 3.3 
 Noun 

 3.3.1 
 Declension 

 3.3.2 
 Derived terms 

 3.4 
 References 

 Toggle the table of contents 

 رود 

 16 languages 

 Azərbaycanca 
 فارسی 
 Français 
 Magyar 
 Bahasa Indonesia 
 한국어 
 Kurdî 
 Limburgs 
 ລາວ 
 Lietuvių 
 Malagasy 
 Polski 
 پښتو 
 Русский 
 Türkçe 
 中文 

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

 See also: زود 

 Old Tati
 [ edit ] 

 Etymology
 [ edit ] 

 Cognate with Larestani رود ( rud , “ son ” ) and Southern Luri رود ( rūd , “ child, offspring ” ) 

 Noun
 [ edit ] 

 رود ( rud ) 

 ( Old Azari ) son 

 ( Old Azari ) child 
 15th century , Pir Zehtab Tabrizi
 ای اسکندر 
 رودم کشتی 
 رودت کشاد ay Iskandar, rud-am kuštī, rud-at kušâd! Oh Iskandar , you killed my son; may your son perish as well! 

 Persian
 [ edit ] 

 Persian Wikipedia has an article on: رود 

 Wikipedia fa 

 Etymology
 [ edit ] 

 Inherited from Middle Persian lwd ( /⁠rōd⁠/ , “ river ” ) , from Old Persian 𐎼𐎢𐎫 ( r-u-t /⁠rautaʰ⁠⁠/ , “ river, torrent ” ) , from Proto-Iranian *hráwtah , from Proto-Indo-Iranian *sráwtas , from Proto-Indo-European *srew- , possibly from *ser- .. Cognate with Yaghnobi рута ( ruta ) , Roshani рӯд ( rūd ) , Yazghulami рәд ( rəd ) , Ishkashimi ру̊чик ( růčik ) .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ˈroːd/ , /ˈruːd/ 

 ( Dari, formal ) IPA ( key ) : [roːd̪] , [ruːd̪] 

 ( Dari, formal ) IPA ( key ) : [roːd̪] , [ruːd̪] 
 ( Kabuli ) IPA ( key ) : [roːd̪] , [ruːd̪] 

 ( Hazaragi ) IPA ( key ) : [rʊːd̪̥] , [rud̪̥] 

 ( Iran, formal ) IPA ( key ) : [ɹuːd̪̥] 

 ( Tajik, formal ) IPA ( key ) : [ɾɵd̪] , [ɾud̪] 

 Rhymes: -oːd , -uːd 

 Readings

 Classical reading ? 

 rōd, rūd

 Dari reading ? 

 rōd, rūd

 Iranian reading ? 

 rud

 Tajik reading ? 

 rüd, rud

 Noun
 [ edit ] 

 Dari

 رود 

 Iranian Persian

 Tajik

 рӯд 

 رود • ( rōd, rūd / rud ) ( plural رودها ( rōd-hā, rūd-hā / rud-hâ ) , Tajik spelling рӯд , or руд ) 

 river 

 torrent 

 Synonyms
 [ edi
######## 9af4871f2b20d347
URL: https://en.wiktionary.org/wiki/%D8%B1%D9%85%DB%8C%D8%AF%D9%86
FETCHED: 2026-09-14T02:00:10Z
STATUS: 200
TITLE: رمیدن - Wiktionary, the free dictionary

رمیدن - Wiktionary, the free dictionary 

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

 Personal tools 

 Donations 

 Create account 

 Log in 

 Contents

 move to sidebar 
 hide 

 Beginning

 1 
 Persian 

 Toggle Persian subsection 

 1.1 
 Pronunciation 

 1.2 
 Verb 

 Toggle the table of contents 

 رمیدن 

 4 languages 

 فارسی 
 Kurdî 
 Malagasy 
 Русский 

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

 Persian
 [ edit ] 

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ra.miː.ˈdan/ 

 ( Dari, formal ) IPA ( key ) : [rä.miː.d̪án] 

 ( Dari, formal ) IPA ( key ) : [rä.miː.d̪án] 
 ( Kabuli ) IPA ( key ) : [rä.miː.d̪án] 

 ( Hazaragi ) IPA ( key ) : [rä.mi.d̪án] 

 ( Iran, formal ) IPA ( key ) : [ɹæ.miː.d̪ǽn] 

 ( Tajik, formal ) IPA ( key ) : [ɾä.mi.d̪án] 

 Rhymes: -an 

 Readings

 Classical reading ? 

 ramīdan

 Dari reading ? 

 ramīdan

 Iranian reading ? 

 ramidan

 Tajik reading ? 

 ramidan

 Verb
 [ edit ] 

 Dari

 رمیدن 

 Iranian Persian

 Tajik

 рамидан 

 رمیدن • ( ramidan ) ( present stem رم ( ram ) ) 

 to run away 

 to run wild 

 to buck 

 Retrieved from " https://en.wiktionary.org/w/index.php?title=رمیدن&oldid=72331171 "

 Categories : Persian terms with IPA pronunciation 
 Rhymes:Persian/an 
 Rhymes:Persian/an/3 syllables 
 Persian lemmas 
 Persian verbs 

 Hidden categories: Pages with entries 
 Pages with 1 entry 

 This page was last edited on 26 March 2023, at 15:04.

 Definitions and other text are available under the Creative Commons Attribution-ShareAlike License ; additional terms may apply. By using this site, you agree to the Terms of Use and Privacy Policy. 

 Privacy policy 

 About Wiktionary 

 Disclaimers 

 Legal & safety contacts 

 Code of Conduct 

 Developers 

 Statistics 

 Cookie statement 

 Mobile view 

 Search 

 Search 

 Toggle the table of contents 

 رمیدن 

 4 languages 

 Add topic
######## 7833ffe91c163cca
URL: https://en.wiktionary.org/wiki/%D8%B1%D9%88%D8%B6%D8%A9
FETCHED: 2026-09-14T02:00:11Z
STATUS: 200
TITLE: روضة - Wiktionary, the free dictionary

روضة - Wiktionary, the free dictionary 

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

 Personal tools 

 Donations 

 Create account 

 Log in 

 Contents

 move to sidebar 
 hide 

 Beginning

 1 
 Arabic 

 Toggle Arabic subsection 

 1.1 
 Pronunciation 

 1.2 
 Noun 

 1.2.1 
 Declension 

 1.2.2 
 Descendants 

 2 
 Gulf Arabic 

 Toggle Gulf Arabic subsection 

 2.1 
 Etymology 

 2.2 
 Pronunciation 

 2.3 
 Noun 

 3 
 Moroccan Arabic 

 Toggle Moroccan Arabic subsection 

 3.1 
 Etymology 

 3.2 
 Pronunciation 

 3.3 
 Noun 

 Toggle the table of contents 

 روضة 

 8 languages 

 Français 
 Magyar 
 Bahasa Indonesia 
 Kurdî 
 Malagasy 
 Русский 
 Тоҷикӣ 
 Türkçe 

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

 See also: روضه 

 Arabic
 [ edit ] 

 Root 

 ر و ض ( r w ḍ ) 

 7 terms 

 Pronunciation
 [ edit ] 

 IPA ( key ) : /raw.dˤa/ 

 Noun
 [ edit ] 

 رَوْضَة • ( rawḍa )  f ( plural رَوْضَات ( rawḍāt ) or رِيَاض ( riyāḍ ) ) 

 garden , meadow 
 609–632 CE , Qur'an , 30:15 : فَأَمَّا الَّذِينَ آمَنُوا وَعَمِلُوا الصَّالِحَاتِ فَهُمْ فِي رَوْضَةٍ يُحْبَرُونَ faʔammā llaḏīna ʔāmanū waʕamilū ṣ-ṣāliḥāti fahum fī rawḍatin yuḥbarūna And as for those who had believed and done righteous deeds, they will be in a garden [of Paradise], delighted. 

 kindergarten 

 Declension
 [ edit ] 

 Declension of noun رَوْضَة ( rawḍa )

 singular

 singular triptote in ـَة ( -a ) 

 indefinite

 definite

 construct

 informal

 رَوْضَة 
 rawḍa 

 الرَّوْضَة 
 ar-rawḍa 

 رَوْضَة 
 rawḍat 

 nominative

 رَوْضَةٌ 
 rawḍatun 

 الرَّوْضَةُ 
 ar-rawḍatu 

 رَوْضَةُ 
 rawḍatu 

 accusative

 رَوْضَةً 
 rawḍatan 

 الرَّوْضَةَ 
 ar-rawḍata 

 رَوْضَةَ 
 rawḍata 

 genitive

 رَوْضَةٍ 
 rawḍatin 

 الرَّوْضَةِ 
 ar-rawḍati 

 رَوْضَةِ 
 rawḍati 

 dual

 indefinite

 definite

 construct

 informal

 رَوْضَتَيْن 
 rawḍatayn 

 الرَّوْضَتَيْن 
 ar-rawḍatayn 

 رَوْضَتَيْ 
 rawḍatay 

 nominative

 رَوْضَتَانِ 
 rawḍatāni 

 الرَّوْضَتَانِ 
 ar-rawḍatāni 

 رَوْضَتَا 
 rawḍatā 

 accusative

 رَوْضَتَيْنِ 
 rawḍatayni 

 الرَّوْضَتَيْنِ 
 ar-rawḍatayni 

 رَوْضَتَيْ 
 rawḍatay 

 genitive

 رَوْضَتَيْنِ 
 rawḍatayni 

 الرَّوْضَتَيْنِ 
 ar-rawḍatayni 

 رَوْضَتَيْ 
 rawḍatay 

 plural

 sound
```


## [2026-09-14T02:00:27.882Z] TOOL CALL #38: Bash

```json
{
 "command": "pdftoppm -f 445 -l 445 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg445 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg445.png",
 "description": "Render PDF page 445"
}
```


### [2026-09-14T02:00:29.631Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 74593 Sep 13 22:00 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg445.png
```


## [2026-09-14T02:00:31.803Z] TOOL CALL #39: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg445.png"
}
```


### [2026-09-14T02:00:32.372Z] TOOL RESULT

```

```


## [2026-09-14T02:00:32.370Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-14T02:00:49.002Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && python3 - <<'EOF'\nfrom PIL import Image\nim=Image.open('pg445.png')\nprint(im.size)\n# empty box approx x 830-1190 of 1545 display -> scale to actual width\nW,H=im.size\nbox=(int(0.52*W),int(0.38*H),int(0.80*W),int(0.46*H))\nim.crop(box).resize((int((box[2]-box[0])*2.2),int((box[3]-box[1])*2.2))).save('pg445-crop.png')\nEOF\nls",
 "description": "Crop empty box region"
}
```


### [2026-09-14T02:00:50.276Z] TOOL RESULT

```
(1700, 2200)
391-top.png
394hi.png
394-zoom.png
400-bot.png
400-top.png
404-top.png
411-top.png
412-zoom.png
414-bot.png
417hi.png
417-top.png
417-zoom.png
421-top.png
428hi.png
428-zoom2.png
428-zoom.png
429hi.png
429-zoom.png
431-top.png
432-bot.png
436-full.png
afm74-420.png
afm76-421.png
agents.txt
ahd430.txt
beekes410.txt
bqt1328-ftr-437.png
bqt1328-hdr-437.png
bqt1328-top-437.png
bqt1330-top-437.png
bqt1-440.txt
bqt2123-fn-435.png
bqt390_436_foot.jpg
bqt390_436_top.jpg
bqt390_662_foot.jpg
bqt390_662_top.jpg
bqt390_n436.jpg
bqt390_n662.jpg
build2-434.py
build3-434.py
build-389.py
build-390.py
build-391.py
build393.py
build-394.py
build-395.py
build-396.py
build-398.py
build-400.py
build-401.py
build-405.py
build-406.py
build-407.py
build-412.py
build-414.py
build-415.py
build-417.py
build-418.py
build-419.py
build-422.py
build-425.py
build-426.py
build-428.py
build-429.py
build-430.py
build-431.py
build-434.py
build-435.py
build-438.py
c404-empty.png
c404-greek.png
c404-patil.png
c404-pest.png
c404-symp2.png
c404-symp.png
c412_cedar.png
c412_makrome.png
c412_makrome_zoom.png
c412_meqrameh.png
c412_meq_zoom.png
c412_sedr_zoom2.png
c412_sedr_zoom.png
crop14-394.png
crop18-394.png
crop411_a.png
crop411_b.png
crop411_c.png
crop419_a.png
crop419_b.png
crop419_c.png
crop419_d.png
crop419_grk.png
crop419_skt.png
crop428a.png
crop428b.png
crop428c.png
crop428d.png
crop-437.png
e0-434.json
edit_about.py
edit_research.py
ffprof
gen-420.py
irn-425.pdf
irn-425.txt
knt-440.txt
knt443.txt
meta-443-knt.json
pg390b.jpg
pg390b.png
pg390.png
pg391big.png
pg391crop.png
pg391.png
pg391root.png
pg391sog.png
pg392.png
pg393.png
pg394hi.png
pg394.png
pg397.png
pg398.png
pg399-crop1.png
pg399-greek.png
pg399.png
pg399-sog.png
pg400big.png
pg400_fa_heli.png
pg400_fr2.png
pg400_french.png
pg400_kasak2.png
pg400_kasak3.png
pg400_kasak.png
pg400.png
pg402.png
pg404hi.png
pg404.png
pg405.png
pg406.png
pg407.png
pg408-ampus.png
pg408-germ.png
pg408.png
pg409.png
pg410hi.png
pg410-k2.png
pg410-kadm2.png
pg410-kadm.png
pg410-persian.png
pg410.png
pg410-q2.png
pg410-qedam.png
pg411_300.png
pg411.png
pg412_hi.png
pg412.png
pg412_uhi.png
pg413.png
pg414-greek.png
pg414.png
pg415-emptybox.png
pg415hi.png
pg415.png
pg416-v.png
pg417.png
pg418hi.png
pg418.png
pg418-raj2.png
pg418-raj3.png
pg418-rajidan.png
pg419_hi.png
pg419.png
pg420b.png
pg420.png
pg421.png
pg422.png
pg423.png
pg424.png
pg426.png
pg428hi.png
pg428.png
pg429-crop1.png
pg429-crop2.png
pg429-crop3.png
pg429hi.png
pg429.png
pg431.png
pg432.png
pg433.png
pg435-n1.png
pg435-n4.png
pg435.png
pg436.png
pg437-437.png
pg437hi-437.png
pg438.png
pg443.png
pg444.png
pg444-serom.png
pg444-sibum.png
pg445-crop.png
pg445.png
pg452.png
pg453.png
pg456-germ.png
pg456hi.png
pg456.png
pg458.png
queue.txt
sem410.html
u_mak.png
u_meq.png
u_sedr.png
write397.py
write-402.py
write409.py
write410.py
write436.py
```


## [2026-09-14T02:00:53.298Z] TOOL CALL #41: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg445-crop.png"
}
```


### [2026-09-14T02:00:53.320Z] TOOL RESULT

```

```


## [2026-09-14T02:01:03.833Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KNT rauta ===\"; grep -n -i 'rauta\\|rauta-\\|ruta' KNT.txt | head -20; echo; echo \"=== KNT leaf for p205 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==221' KNT.txt | grep -n -i 'rau\\|root' | head",
 "description": "Kent rauta"
}
```


### [2026-09-14T02:01:04.969Z] TOOL RESULT

```
=== KNT rauta ===
1968:‘mountain’; rauta ‘river’, At the first introduction
2194:J. The neuter formation with suffix -os in nom.- acc. sg., -es- in other forms: type Lt. gen-us gen- ет-18, Gk. *y&-os yév-e-os, Skt. ján-as 3án-as-as. OP has nom. rauta? ‘river’, Skt. srólas; nom.-aec. rauca? ‘day’, Av. raoco ‘light’, Skt. rócas ‘light’; асе. draya* ‘sea’ (and draiya*, §48), Av. zrayd, Skt. jráyas; асе. manaX-cà (§105), Av. mand, Skt. mdnas; acc. züra^ ‘evil’, Ау. 2070; асе. mita? ‘evil’. Inst. manahá, Skt. mánasà. Loc. drayahy-à (with added -2; also written drayahiyà, but whether the ~i- is syllabic cannot be determined), Skt. jrdyasz, ef. Av. manahi-cà. Inst. pl. raucabi$, probably for *raucatbiš, cf. Av. mandbis, Skt. mánobhzs: the -h from -s in certain sandhi positions here trans- ferred to the medial position before the consonant of the case-suffix, and then voiced before the voiced consonant and lost with the same products as when final in the respective languages.
3120:‘fortress, stronghold’, vardanam ‘town’, dvahanam ‘village’, kaufa ‘mountain’, rauta ‘river’, The re- sumptive adverbs are avadà ‘there’, hacá avadaSa
4405:rauta : tya : Mudràyaly : danuvatiy : ab
5847:ташіаћ- sb. ‘river’ ($166): NPers. ra8, Skt. srólas- ‘current, river’, pIE *sreutos (5118.1, $156.П) to root *sreu- ‘flow’; perhaps same as Av. 6raotah-, with sandhi initial (Bthl. Саг. IP 1.§87.- n2, AW 800). rauta nsn. anacoluthic in naming phrase (wrongly gen.-abl. to stem таш-, Mt. MSLP 19.56-7, MB Gr. $167, $316) DZc 9.

=== KNT leaf for p205 ===
1:tem (530, $148.I, 6154.1), ef. Av. posana- ‘battle’, Skt. pfiana- ‘battle, army’, to root in Av. poral-onie ‘they fight’? (Bv. TPS 1945.69-4; not agency noun
12:pasü prep. ‘after’, temporal with асе. and local with gen. (Bv. BSLP 33.2.153): Av. paséa, NPers. pds, Skt. paácá, isn. to stem in Lith. (dat.) adv. and prep. різки ‘behind, later, after’ (Foy, KZ 35.26); pIE *po as in Lt. po-lið, positus, Gk. &-vó, + *sg*é, inst. to root noun from *seq*- ‘fol- low’, Av... hacatte, Skt) Gdeate, Gk. trerai, Lt.
```


## [2026-09-14T02:01:06.665Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HUB rod ===\"; grep -n -i 'rôd\\|röd\\|rautah\\|rōd' HUB.txt | head -20; echo \"=== NYB rot ===\"; grep -n -i \"rōt\\|rot 'river'\\|lwt\" NYB_vol2_glossary.txt | head -20; echo \"=== KLN rhythm/stream ===\"; grep -n -i 'rhythm,\\|rheum,\\|stream, n' KLN_1966.txt | head -10",
 "description": "Hubschmann, Nyberg, Klein"
}
```


### [2026-09-14T02:01:06.795Z] TOOL RESULT

```
=== HUB rod ===
7784:'Fluss', arm. rot = ap. rautah-, skr. srofas; hazdr 'tausend',
=== NYB rot ===
112:HSD(1)WN-: (-/- inserted through the influence of the Prs d dlwtn' = drütan): HSD to reap
156:LWTH: L'WATEH together with him
491:?apak [LWTH] 1. a) adv. together: (ka- nicak virtual dat.) andar ham Sap ~ bit in that same night he was together with the girl 16!-?; referring back to an encl. pron.: sih (restore the reading “30”, v. 28th) 4-$ ~ pat asp which was with him on the horse 8? (v.s.v. i and ef andar); Sih-& ... —-aš pat asp nišast estat 89: as prepositions do not govern an encl. pron. ~ must be the adv., and -aš refer to the following pat asp or to the whole sentence. — b) prep. together with, with, in all its senses, passim; in spite of 118; ~ man 5?*; ~ amäh 19, ~ smäh 1918, ~ disin 82; ēvak ~ dit with each other 7818. 799. 1071, — 2. adj. prostrate, knocked down, lying on one’s back: čvak apar, ~ dit, apar ēstūt hend o en kar they set about this act (making coition), the one above, the other lying on her back 4314-4; ka Ahriman ~ A. being knocked down (lying senseless) 914 (the enel. -4 after ~ belongs to the following, taking up the preceding subj. Ohurmazd which begins the period), a wordplay — not understood by the Pazandist — with — hämöden yazdan u amahraspandän |. 5—6, the first
495:3a-pàk unclean, soiled, turbid: LWTH dp be *šēpēnd (q. v) 2016-17: LWTH wrongly substituted for ’p’k = a-päk?
503:apäk-puhr [LWTH pwhl] he who has a son 22%. - Cf the NP compounds with bà: bā-āb ‘having water’ and the like.
1351:drot [dlwt'; SRM] benediction (in salu- tations, etc.), welfare, prosperity 14°. 1710, 1918, 12129; ~ 6 ruvän dätan to say farewell to one's life, to die 293-1. — < Olr *druvatüs, nom. of Av. (782 sq.) drvatčit-; MPrthPrs drwd; Paz. drüd; NP durud.
1603:friyät [plyd’t'] help: 6 ~ rasitan 71%. 752. — Paz. friäd, fryäd; NP faryad. friyät- [plyd’t-] pres. 3d p. sg. ~-é to help 721, Paz. friäded. — Cf MPrs pry’d’g ‘helper’, pry?dysn ‘help’ (A-H II, BBB). frt [plwt' down, downwards, with ämatan and many other vbs., v. each separately; — haciš — nest "is not below this (level) 109%, — OP fravata^, Benve- niste, BSL 30, 1930, 59; Ps. plwty; MPrs prwd; Paz. fröd, NP furo(d). Cf yuvat. trēt-barišnēh [—-blšnyh, YDLWN-&nyh] the act of descending, descent 392-11; cf apar-barisneh.
1638:Garödmän [glwtm’n'] Paradise 3115 ete. passim. — Av. (512sg.) garö.demäna- ‘House of Praise’, v. gardmik.
1896:*handrütak [hndlwtk'] *discouraged: dil ~ kart it made his heart *discouraged 73; [adv. -ihā : ēišān vas ~-tha 6 Artaxšēr guft very discouraged they said to A. KnS VIL3]. - Reading uncertain; no Paz. known to me. Henning, followed by M. Schwartz (JRAS 1966, 121), reads hangrü- tak, connecting it with MPrs grwdg ‘lamen- tation’, grwdgyn ‘lamenting’ (List 83, with another reading of our passage 79). How- ever, the idea of ‘lamentation’ is scarcely to the point in the quoted passages (it would be important to know more about the use and purport of grwdg). Until further elucidation I maintain my old reading *handrütak, now connecting it with drütan drav-, commonly ‘to mow, to reap’, but originally ‘to cut’, thus han-drütak ‘cut up, afflicted’. Bailey, BSOAS XXIV, 1961, 478, discusses a root drav-, dru- ‘to treat violently’, which is perhaps identical.
2475:Marv-rót [mlw lwt'] a town 1144. — "Marv on the river’ (i.e. Muryab), situated five days’ journey from Marv šāhijān (v. above), Yaqut 4, 506 sg.; Arab Marvarud or Marv al-rud.
3311:rēš-galūtak [lyšglwtk'] the head of the exiles, the exilarch, title of the head of all Jews in the Sassanian empire, ac- credited at the Sassanian court, and responsible to the Great King. for the Jewry of the empire 116°. — Borrowed from Aram res gälütä.
3348:rot [lwt'; YM?] river P1:3. 56214-16, — OP rautah-; MPrthPrs rud; Paz. NP rod.
3349:Rötastahm [lwtsthm] n. pr. 1162. — NP Rustam; Old Sogd rwstmy, Reichelt, Sogd. Handschr.- R. II, 63.
3353:rötastäk [lwtst’k], rostak [lwst’k] district, province 377. 8618. — In FrP 2 it is the first subdivision under šahr ‘dominion, kingdom’, and placed above déh ‘village’ and zänak ‘house’, cf Nyberg, Byzantion XXXVILI, 1968, 114-115. — MPrth rwdyst’g (A-H III); Paz. röstä, pl. rostčiga ; NP rēstā(i) ‘any inhabited place; a market-town, a village’; Arab. lw. rustäg, ruzdäg ‘arable land’.
3519:srot [slwt'] hearsay, rumor 45%, — Av. (1633) sraota- ‘the hearing (of a prayer)’; MPrs srwd ‘song’; v. srütan.
3521:srütan [slwtn'] sräy- [sl’d]- to sing: tambür zat u srut väcik played the lute and sang vocally (sang a chant to the music) 4°; to recite by chanting 59. — Av. (1639 sqq.) srav- ‘to hear’, caus. ‘to recite (the -holy texts, singing them)’; MPrth sr’w-, MPrs sr’y- ‘to sing’; NP surüdan siräy-; v. srot.
4291:Xösröi [hwslwd; hwslwd' 110!5 M, but hwslwd Cod. K 43b] n. pr. A. the 3d king of the Kayanian dynasty, mostly known as Kai-Xösröi [kdhwslwd, -Iwd'] 7133. 1138-17; with the patron. Siydvaxsan 116’; eschatological hero 887°. 99—100 passim. 1065; — ~ i Kavätän, founder of five cities 114? sqq., is probably the old Kayanian king of the heroic saga. — B. the Sassanid kings from Bahram I (273— 276) onwards assumed the title ka? (g.v.) and regarded themselves as Kayanians: Kai-Kavät (488—531), his son im bag Xösröi šāhān šah i Kavätän (531-579) 10921, known as anösak-ruvän 118%; on Baxt-— v. this w. — Gr Xoopöns, NP Xusrav; Av. (1738) žhaosravah-. The spell- ings are: 1. on coins: hwslwd, hwslwdy (already Prth); hwslwy (predominant un- der Khosroes II 590-628); once hwslw? and once hwslwty (!) v. Paruck 380- 384. 386-390; Hansen, Catrang 18-19; — 2. in the inseriptions: KZSPrth hwsrw, Gr. v. Xootew, Prs hwslwb, which is also the spelling in three of the cities mention- ed 1141? sqq., certainly to be pronounced Xūsrūv = Arm Xosrov (but Syr Kösrö). In my opinion the BP form hwslwb' re- presents in reality hwslwdy, -b- being, as often at the end of the w., the cursive form of the letter d as written in the Ps.
=== KLN rhythm/stream ===
24124:model,  n.  —  MF.  modelle  (F.  modele),  fr.  It.  mo- dello,  fr.  VL.  *modellus,  fr.  L.  modulus,  ‘  small measure;  rhythmical  measure,  rhythm,  time, melody,  mode’,  dimin.  of  modus.  See  mode  and cp.  mold,  ‘model’.
32759:ponticum,  fr.  MedL.  rha  Ponticum,  lit.  ‘Pontic rhubarb’.  The  first  element  stands  for  orig. rheum,  ‘rhubarb’,  fr.  Gk.  pijov,  fr.  Pers.  rewend, of  s.m. ;  the  alteration  of  rheum  into  rha  is  due to  a  confusion  with  Rha,  the  ancient  name  of the  river  Volga.  See  Rheum,  rhubarb.  For  the second  element  see  Pontic.
32779:rheum,  n.,  discharge  from  the  mucous  membranes (archaic).  —  ME.  reume,  fr.  OF.  reume  (F. rhume),  ‘a  cold’,  fr.  L.  rheuma,  fr.  Gk.  psupia, ‘that  which  flows;  discharge,  flux,  rheum’,  from the  stem  of  pcEiv,  peiv,  ‘to  flow’.  See  rheo-. Derivatives:  rheum-ic,  adj.,  rheum-y,  adj., rheum-i-ly,  adv.,  rheum-i-ness,  n.
32780:Rheum,  n.,  a  genus  of  herbs  (bot.)  —  L.,  ‘rhubarb’, fr.  Gk.  prjov,  fr.  Pers.  rewend,  of  s.m.  See  rhu¬ barb  and  cp.  rhapontic.
32781:rheumatic,  adj.  —  ME.  rewmatik,  fr.  MF.  reuma- tique  (F.  rhumatique),  fr.  L.  rheumaticus,  ‘troubl¬ ed  with  rheum’,  fr.  Gk.  pEuixaxtxo;,  fr.  peOpia, gen.  pedptaxo;.  See  rheum  and  1st  -atic. Derivatives:  rheumatic,  n.,  rheumatic-al,  adj. rheumatism,  n.  —  L.  rheumatismus,  ‘rheum,  ca¬ tarrh’,  fr.  Gk.  p£U[i.aTi(T|i.6;,  fr.  p£upiaxt£E<j&ai, ‘to  suffer  from  a  flux’,  fr.  pEujxa,  gen.  peuiiaxo;. See  rheum  and  -ism.
32823:rhombus,  n.,  an  oblique-angled  equilateral  paral¬ lelogram.  —  L.  See  rhomb, rhoncial,  also  rhonchal,  adj.,  pertaining  to  arhon- chus.  See  next  word  and  adj.  suff.  -al. rhonchus,  n.,  a  whistling  sound  heard  on  the auscultation  of  the  chest.  —  L.,  ‘a  snoring’,  fr. Gk.  poy-/_o;,  which  is  rel.  to  (56yxo;,  friyyoq, ply xo;,  of  s.m.  plyysiv,  peyxEtv,  ‘to  snore’; prob.  of  imitative  origin, rhotacism,  n.,  mispronunciation  of  the  letter  r.  — ModL.  rhotacismus,  fr.  Gk.  ptoTaxiopoc,  fr. pwraxlqEiv.  See  next  word  and  -ism. rhotacize,  intr.  v.,  to  mispronounce  the  letter  r. — Gk.  ptoTaxi^Eiv,  ‘to  use  the  letter  r  excessive¬ ly’,  fr.  p<7>,  name  of  the  letter  r.  See  rho  and  -ize. rhubarb,  n.,  a  garden  plant  with  large  leaves  and edible  leaf  stalks.  —  ME.  rubarbe,  fr.  MF.  reu- barbe,  rubarbe  (F.  rhubarbe),  fr.  ML.  rheubar- barum.  The  first  element  in  ML.  rheubarbarum derives  fr.  L.  rheum,  fr.  Gk.  ptjov,  ultimately  fr. Pers.  rewend,  ‘rhubarb’  (whence  also  Russ. reven).  Cp.  the  ML.  form  rhabarbarum,  which comes  fr.  Gk.  pec  fSxppapov,  lit. ‘foreign  rhubarb’ ; px,  ‘rhubarb’,  is  a  blend  of  pvjov,  ‘rhubarb’,  with 'Pa,  the  Scythian  name  of  the  Volga;  see  roric. The  second  word  in  pa  |3xp!3xpov  refers  to  the foreign  origin  of  the  plant.  It.  rabarbaro  (whence G.  Rhabarber)  derives  fr.  Gk.  pa  |3dpj3xpov.  Cp. rhapontic,  rheum.
32834:Derivative:  rhyparograph-ic,  adj. rhythm, n.  -  MF.  rhythme (F. rhytme),  fr.  L.rhyth- mus,  fr.  Gk.  puff|z6;,  ‘measured  motion,  time, proportion,  symmetry,  rhythm’,  formed  from the  stem  of  pelv  ‘to  flow',  with  suff.  -ffja.6;,  a var.  of  (cp.  -ism).  See  rheo-  and  cp.  next word.
36992:Derivatives:  streak,  tr.  v.,  streak-y,  adj.,  streak- i-Iy,  adv.,  streak-i-ness,  n. stream,  n.  —  ME.  strem,  streme,  fr.  OE.  stream, ‘flowing,  current;  running  water,  river’,  rel.  to OS.  strom,  ON.  straumr,  Dan.  stram,  Swed. Strom,  Norw.  straum,  OFris.  stram,  Du.  stroom, OHG.,  MHG.  stroum,  strom,  G.  Strom,  ‘cur¬ rent,  river’,  fr.  I.-E.  base  *sreu-,  ‘to  flow’,  whence also  OI.  sravati,  ‘flows’,  srotafi,  ‘stream’, Arm.  aroganem,  ‘I  moisten,  wet’,  Gk.  p£eiv  (for •apefetv),  ‘to  flow’,  p6o ;  (for  »ap6Foi;), ‘stream’,  Lett,  strauma,  ‘stream,  river’,  Pol. strumieh,  ‘brook’,  Lith.  sraveti,  ‘to  trickle,  ooze’, OSlav.  struja,  ‘river’,  o-strovu,  ‘island’,  lit.  ‘that which  is  surrounded  by  a  river’,  OIr.  sruaim,  Ir. sruth  (gen.  srotha),  Co.  streth,  ‘river’.  Cp.  the river  name  Expujxtov,  lit.  ‘River’.  Cp.  rheo-, rheumatic,  rheumatism,  rhythm,  the  first  element in  rhyolite  and  the  second  element  in  Calirrhoe, catarrh,  hemorrhoids,  diarrhea,  pyorrhea,  se¬ borrhea.  Cp.  also  strudel  and  the  second  element in  maelstrom.  Base  *sreu-  is  an  enlargement  of base  *ser-,  whence  Gk.  opp.f)  (for  *aoppr) ),  ‘on¬ set’,  opo;  (for  *acip6 ?),  ‘whey’,  L.  serum, ‘whey’.  See  hormone  and  serum.
```


## [2026-09-14T02:01:20.421Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if \"rautah- sb.\" in p:\n        print('LEAF',i)\n        print(p[:300])\n        break\nEOF",
 "description": "Kent leaf for rautah-"
}
```


### [2026-09-14T02:01:21.658Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T02:01:22.785Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD Bd2 sreu ===\"; grep -n 'sreu-\\|srev-\\|straumaz\\|sreu' incoming/WLD/WLD_Bd2_pages.txt | head -20; echo \"=== SYN river ===\"; grep -n 'NPers. rūd\\|NPers. rud\\|1.36 RIVER\\|RIVER' SYN.txt | head -10",
 "description": "Walde-Pokorny and Buck"
}
```


### [2026-09-14T02:01:22.909Z] TOOL RESULT

```
=== WLD Bd2 sreu ===
33099:704 f.       —   S.   auch sreu-      „flie6en‘\
42141:wohl vielmehr zu "^sreup-^ s. d.    eher hieher vielleicht lit. sirubas, lett.
42490:u.    str^m zu '^sreu- „flie6en");
46584:702                                    sraq^-to-,   -ti-   — sreu-
46634:sreu- „flie6en“.
46652:                                                sreup                                         703
46662:sreue- in iggvfjv, lit. sraveti; zu einer dieser beiden set-Basen ai. Inf. srd-
46671:att. geT^gov „FluBlauf, FluBbett" von them at. sreue- ausgegangen (s. Pers-
46692:u. str0m^ Persson Beitr. 654, 662.    Idg. sreu- ist Erw. von ser- „flie6en",
46697:sreup- „schorfiger Schmutz am Korper".
46701: femen", vgl.     B. dt. kdpfeii Kopf ) slav. strujr/b (aus *sreupos oder *srou-
46712: aon Beitr. 445 zu ster-^ streup- „starren"). Beziehung zu sreu- „flieBen"
=== SYN river ===
1374:1.36 RIVER; STREAM; BROOK
```


## [2026-09-14T02:01:29.145Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if \"sb. ‘river’ ($166)\" in p or \"sb. ‘river’ (§166)\" in p:\n        print('LEAF',i); print(p[:400]); break\nEOF\necho \"=== SYN 1.36 ===\"; sed -n '1374,1420p' SYN.txt",
 "description": "Kent leaf + Buck river"
}
```


### [2026-09-14T02:01:30.676Z] TOOL RESULT

```
LEAF 229
d sg. opt. mid. ($223.II, $284.1I) XPh 50. yadiyaiša” (8220, 5228.11, 4282.101; written 11924, $5.1; cf. Hz. AMI 8.67, ApI 357-8) 3d pl. opt. pass. (Ogden ap. JAOS 58.325; not yadiyatš 2d sg. opt. mid. with Wb. Symbolae Koschaker 196, nor fut. pass. with Hz. AMI 8.67, ApI 357-8) XPh 39.
lwadé- conj. ‘where’: GAv yada, Skt. yada; probably rel. nt. pAr. #00 + postpos. 4. уайд- tya XPh 35f ($133, $29
=== SYN 1.36 ===
1.36 RIVER; STREAM; BROOK
Grk. orapés; pedua; xel- Goth. ahwa, flddus; rinnd Lith.  upé; sriovée; upelis pappos ON a; lekr (bekkr) Lett.  upe; strdva; upele NG qoTapos, TOTAML; pea; Dan.  flod; sirém; bek ChSl.  réka; tokii; potoku puaxe Sw. flod; strém; back SCr. rijeka; tok, struja; Lat.  jfluvius, flimen (am- OE éa; stream; rip, broc potok nis); rivus ME river; stream; broke Boh. eka; potok
Rum. fluviu, rt; pirtt Tr. ab(a); sruth; glais NIr.  abha; sruth; sruthan afon; ffrwd; nant, afonig Br. «ster (aven); gouer Between the large ‘river’ emptying into the sea and the tiny ‘brook’ there are infinite gradations, and often a wealth of words for these, which must be mostly ignored here. But generally Oe are distinctive words for ‘river’ and ‘brook’, and also one for ‘stream’, a generally for all forms of running te ee Mainly for those intermediate a : one the extremes of ‘river’ and : te for ‘brook’ may be diminutives Ose for ‘river’ river’. Conversely, a word
It. fiume; rivo; ruscello, NE river; stream; brook Pol. rzeka; potok; ruczaj, etc. Du. rivier; stroom; beek strumyk Fr. fleuve; riviére; ruis- OHG fluz, aha; strom; bah Russ. eka; potok; rutej : seau MHG _  vluz; strom; bach Skt. nadi-; sarit-, srotas-; Sp. rio; arroyo NHG  fluss; strom; bach kulya-
Ay. Graotah-, ravan-, etc., OPers. rauta-
for ‘brook’ may be displaced by a dimin- utive form of it (or otherwise) and itself serve for ‘river’.
Most of the words are derived from roots meaning ‘flow, run’. Some are cognate with words for ‘water’, perhaps originally ‘flowing water’ (cf. 1.31). Some are from verbs for ‘rush, plunge’, or ‘roar’, applied first to a rushing, roar- ing stream.
1. Derivs. of IE *sreu- ‘flow’ in Grk. pew, Skt. sru-, ete. Walde-P. 2.702 f.
Grk. pedpa, poos, pon ‘stream, current’,
i CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri aa
a2 SELECTED INDO-EUROPEAN SYNONYMS
pvat, ‘swollen brook’ (Thuc. 4.96), NG dim. puax ‘brook’, also peyarid ‘water-
tourse’ (with or without water); Ir. sruaim, sruth ‘stream, river’ (NIr. ‘river’ in river names), NIr. srutén ‘brook’, W. ffrwd ‘stream’, Br. froud ‘torrent’ (so Pedersen 1.35; fr. *spru-tu- : OE spritan ‘sprout’, etc. Walde-P. l.c.); ON straumr, OE stréam, OHG strdm, etc. ‘stream’; Lith. sr(z)ové, Lett. strava, etc., ‘stream’, Pol. strumier, strumyk ‘brook’; Skt. srotas-, sravat-, Av. @raotah- (in cpds.), ravan-, raodah-, ‘stream, river’, OPers. rauta ‘river’ (used of the Nile), NPers. rid ‘river’.
2. Derivs. of IE *rei- in Skt. ri- ‘et go’, mid. ‘flow’, Goth. rinnan ‘run, flow’, ete. Walde-P. 1.139 ff., Ernout- M. 866 f. -
Lat. rivus ‘brook’; OE rip ‘brook’ (gl. Lat. rivus), MLG ride ‘brook’; Goth. rinnd ‘brook’; ChSl. réka, etc., general Slavic for ‘river’.
From Lat. rivus (through rius) come Sp. rfo ‘river’ (Olt. rio ‘brook’ and ‘riy- er’, OF r. ri ‘brook’), Rum. rité ‘river’ (now fluviu for large rivers like the Danube). Dim. forms for ‘rivulet, brook’, Lat. rivolus, It. rivolo, Rum. rviilet, It. ruscello, Fr. ruisseau, REW 7341, 7338a. Gamillscheg 777.
3. From IE *ap (and ab-) ‘water’, Skt. pas, etc. (1.31). Walde-P. 1.46, Ernout-M. 45. Walde-H. 1.40.
Lat. amnis ‘river’ (poet.); Ir. ab (aba, oub, etc.), NIr. abha ‘river’, W. afon ‘river’, afonig ‘brook’, Br. aven ‘river’ (mostly obs.), Lith. upé, Lett. upe, OPruss. ape ‘river’, Lith. upelis, Lett. upele ‘brook’ (but Lett. upe also ‘brook’).
4. Grk. rorapss (NG POp. wordt), fr. root of rimrw ‘fall’, réropat ‘fly’, Skt. pat- ‘fly, fall’, etc. That is, Torayés was at first the ‘falling, plunging, rushing’ stream. Walde-P. 2.19. Persson, Bei- trige 654. Kretschmer, Glotta 27,248 f.
‘Brook’ would be covered by fedua, etc. (above, 1), otherwise by words that commonly denote ‘mountain-torrent’. So xapddpa : xapdcow ‘cut into’; xeluappos (but once ‘river’ in LXX, and ‘brook’ in NT), Hom. xepéppovs, Xetudppoos, cpd. of xetya ‘cold, winter’ and péw ‘flow’.
5. Lat. fluwius (> Fr. flewe; Rum.
fluviu neolog.), and fliimen (> It. jiume),
both common words for ‘river’ (fluvius preferred in earlier writers, flamen in Caesar; Arch. lat. Lex. 7.588), fr. Sluere ‘flow’. Walde-P. 2.213. Ernout-M. 371. Walde-H. 1.519.
OF. river, riviere, fr. Lat. riparia, deriv. of ripa ‘riverbank’ (1.27), was used for ‘shore’ (like It. riviera, etc.), then also for the stream flowing between the banks. Hence ME, NE river, Du. rivier ‘river’, while Fr. riviére is used of the smaller river tributary to the fleuve. REW 605.
Sp. arroyo, Port. arroio ‘brook’, fr. a pre-I word attested by arrugia ‘mine gallery’ in Spain (Pliny HN 33.70), Basque arroila ‘canal’, etc., appropriate to the deep-gullied arroyo of the dry season. REW 678. Bertoldi, BSL 32.122. Wartburg, Entstehung d. rom. Volker 22 f. .
Rum. piriti ‘brook’, prob. : rit ‘river’, influenced by Alb. pérrue ‘brook’. G. Meyer, Alb. Etym. Wtb. 335. Spitzer, Mitt. d. rum. Inst. 1.296. Jokl, IF 37.91.
6. Ir. ab, W. afon, etc., above, 3.
Ir. sruth, etc., above, 1.
Br. ster ‘river’, MBr. staer, fr. *stagro- : Grk. crdtw ‘drip’, orayayv ‘drop’, Lat. stagnum ‘pool’. Walde-P. 2.612. Peder- sen 1.103,
Ir. glais ‘brook’, perh. : Ir. glass ‘green’. Macbain 196 s.v. glaiseach.
Br. gouer, Corn. gover (OCorn. guuer, gl. rivus) ‘brook’, W. gofer ‘overflow, rill’, Ir. fobar in place names, epd. of
— so Ln public Domain. Gurukul Kangri Collection, Haridwar
—_— Bigitized by Arya Samaj Foundation Chennai and eGangotri
| | | |
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
THB PHYSICAL WORLD IN ITS LARGER ASPECTS 43
go- (= Ir. fo, Grk. i7é, etc.) eT
‘bher- ‘bear’ (so Henry s.v.), OF :
IE *bher- ‘gush’ in Ir. topur ‘spring , ete. “Pp. 2.157 ff., but without men-
(Walde-P. ;
tion of Br. gouer, etc.). Vendryes, RC
37.306 f.
W. nant ‘brook’ also ‘valley, gorge, OBr. nant ‘gorge, brook’, Gall. nanto ‘valley’, fr. IE *nem- ‘bend’, Skt. nam-, ete. Walde-P. 2.302. Stokes 192. Otherwise (: Grk. voun ‘pasturage’, etc.) Benveniste, BSL 32.85. In either case, ‘brook’ fr. ‘valley’.
7. Goth. ahwa, ON a, OE éa, OHG aha : Lat. aqua ‘water’ (1.31).
Goth. flddus (once for rorapés) = OF fld, OHG fluot ‘flood’ (sometimes also ‘river’) fr. root of OE flowan ‘flow’, etc. (10.32). The use of the corresponding Dan., Sw. flod as ‘river’ is after that of MLG vlét (Falk-Torp 239). OHG fluz, MHG vluz, NHG fluss, fr. (extension of the same root in) OHG fliozan ‘flow’.
Norw. elf (usual word for ‘river’), Sw. alf = ON elfr ‘Elbe’, prob. : Lat. albus ‘white’, etc. (cf. Grk. a4\¢és and the river "A\deés). Falk-Torp 188f. Hellquist 1434.
```


## [2026-09-14T02:01:41.454Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\n# locate the line index 5847 (1-based)\ntarget=lines[5846]\nprint('LINE:',target[:200])\npos=sum(len(l)+1 for l in lines[:5846])\nleaf=t[:pos].count('\\f')\nprint('LEAF',leaf)\npages=t.split('\\f')\nprint(pages[leaf][:200])\nprint('...TAIL...')\nprint(pages[leaf][-300:])\nEOF",
 "description": "Find Kent leaf/page for rautah"
}
```


### [2026-09-14T02:01:42.554Z] TOOL RESULT

```
LINE: ташіаћ- sb. ‘river’ ($166): NPers. ra8, Skt. srólas- ‘current, river’, pIE *sreutos (5118.1, $156.П) to root *sreu- ‘flow’; perhaps same as Av. 6raotah-, with sandhi initial (Bthl. Саг. IP 1.§87.- n2,
LEAF 229
d sg. opt. mid. ($223.II, $284.1I) XPh 50. yadiyaiša” (8220, 5228.11, 4282.101; written 11924, $5.1; cf. Hz. AMI 8.67, ApI 357-8) 3d pl. opt. pass. (Ogden ap. JAOS 58.325; not yadiyatš 2d sg. opt. mid
...TAIL...
1), Skt. rdhale ‘has- tens, speeds’, rahas- nt. ‘speed, quickness’ (for fur- ther connections, see Uhlenbeck, Wrtb. d. altind. Sprache 241). ragam asn. (or asm.?) as adv. (§143.1, $191.IIT) DB 4.44, perhaps with develop- ment to ‘eagerly’ or ‘confidently’.
Raga- sb. ‘Rhages’, a district in Media: El
```


## [2026-09-14T02:01:50.752Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && grep -n 'رود' ARY_pages.txt | head -20; echo \"=== latin index ===\"; grep -n -i 'RUD\\|ROD' ARY_latin_index_pages.txt | head -20",
 "description": "Aryanpur rud"
}
```


### [2026-09-14T02:01:50.821Z] TOOL RESULT

```
79:ترکیپب (هند و آریایی (13100-۸837۸3) بکار می‌رود.
103:03۷00-۸3۷۸3 بگار می‌رود.
342:قدیمی که در زبان‌های هند و اروپایی باستانی دیده شده نشان می‌دهد که قبل از ورود هند و
351:آورده بودند که آثار هنری آن در بسْیاری از موزه‌ها دیده می‌شود. ورود هند و اروپائیان از شمال.
358:اروپایی تا حدود ۲۵۰۰ سال قبل از میلاد رواج داشته‌اند وی ورود اقرام هند و اروپایی از شمال
655:(5۸۸/۸71۸07) نه تنها در کرانه‌های رود دانوب کوج نشین شدند پلکه در قرن دوم میلادی برای
738:هنوز بطور قطعی خوانده و تفسیر نشده‌اند و احتمال مي‌رود که اصلاً هند و اروپایی نباشند. تعداد .|
771:مرکز آسیای صغیر پیش رفتند. در اثر ورود اقوام هند و اروپایی دیگر؛ کم کم گستره‌ی مردم سلت :
794:مردم آلمانی نژاد را خاور رود «راین؛ (8۳7107) و باختر رود «ادر؛(0358) تعیین کرده است.
812:باستانی ترین اشاره به زبان ارمنی د رکتاب هرودوت (مورخ یونانی) آمده که می‌گوید ارتش
850:نیز از ریشه‌ی ایرانی هستند. مثلاً نام رودهای «دن» (00/1) و «دونتز» (0027875) و «دونپر)
851:(0۸(118758) و شاید «دانرب» (0۸/17288) از واژه‌ی ایرانی کهن - []2۸81 به معنی رودخانه
1052:ویژگی‌های ابر انسانی ضامن خوبی محصول و زایندگی دام‌ها و پر ماهی بودن رودها و فراوانی
1115:(110178۸0078) شعر عشقی يا رزمی می‌سرودند و در بزم‌ها با صدای آهنگین می‌خواندند..
1147:حاوی سرودهای نیایشآمیز بنام «پشت‌هاء (۷۸81778) و وردهایی برای طرد دیوها پنام «ویدیوداده ...۰
1313:اروپایی به عقب برود (فارسی نوین * پهلوی * پارسی باستان + اوستایی +هند واروپایی). ضماً
2182:۲ در زبان‌های آلمانی و انگلیسی و سلتی وگانی و ولزی این واجريشه به صورت نام رودخانه (اسم خاص) بافی
2264:چم این واژه در زبان ارمثی: سرود. ۰
2336:: واژه‌ی "اروند رود" نیز از همین ريشه است و در برهان قاط : برابر با "دجله " شناخته شده است ولی امروز هم چم
2788:برخی از روستاهای مازندران و گیلان به کار می‌رود. شاید علت از مان رفتن این واژه در دیگر نواحی فلات ایران
=== latin index ===
2167:POKORNY. ——=S*~*~*~S~« RT RODA PORTUGUESE) ii
2170:‘MACKENZIE: (WAGON) 139 ROD, RAT
2173:e rebloby| — RODOR
3327:BRATI (OLD PRUSSIAN) S53. BRODHIR
3335:‘REFERENCES chan BRUDER (GERMAN) galt
3338:DELAMARRE (FRERE) 38 BRODER DANISH) Sjlail>
3339:MACKENZIE: (BROTHER) 105 BRODER SWEDISH) Sy
3341:ONIONS: (BROTHER) 121 BRODER, BROEDER (DUTCH) sala
6692:(CRUDE) 109, (RAW) 129 AMARUS LATIN) 3
7898:LITHUANIAN) 33 DRUDAN © (PAHLAVI) 5 shay
8651:RADOR, RODOR RAH PAHLAVI) 5.3444
8660:-RET, ROD (BRETON) 3.3. ROTA (LATIN) pa
8665:MACKENZIE: (RAH) 70 RODA (PORTUGUESE) Ji x
8667:SKEAT: (RET) 757 RODULL
8717:-RITUM GAELIC) SIE RODOND SPANISH) glshe\
8739:LID, LJUDING 4(CZECK) See, RAOTHAITI, RUD-, RAOTHENTI
8741:LAUDIS LATVIAN) (3) 3.93 RUDAG, RUDHAGH .(BALUCHI) yz sb
8742:Luss OLD IRISH) gS 543 2) RODHATI, SANSKRIT) 4 Suse
8743:LLYSIAU :QVELSH) 55 ROHATI, ROHA-, RUDH-, RODHANTI
8927:STRUMIEN HPOLISH)  gl-ng) ROT, ROD s(PAHLAVI) (5 shay
```


## [2026-09-14T02:01:54.277Z] TOOL CALL #49: Bash

```json
{
 "command": "for u in \"https://abadis.ir/fatofa/%D8%B1%D9%88%D9%85%D8%A7%D8%AA%DB%8C%D8%B3%D9%85/\" \"https://abadis.ir/fatofa/%D8%B1%DB%8C%D8%AA%D9%85/\" \"https://www.etymonline.com/word/stream\" ; do python3 tools/fetch_source.py \"$u\" --note \"page 445, nodes 13/14/10: Mo'in tags for روماتیسم/ریتم, stream\"; done",
 "description": "Fetch abadis + etymonline"
}
```


### [2026-09-14T02:01:58.239Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/4fb414b5b270993d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/72e1a21aebd58fd4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/648673ea8897e303.txt
```


## [2026-09-14T02:02:08.562Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && python3 - <<'EOF'\nt=open('ARY_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'STREAM' in p and ('رود' in p):\n        print('=== LEAF',i,'===')\n        print(p[:2500]); print()\nEOF",
 "description": "Find ARY entry for rud"
}
```


### [2026-09-14T02:02:09.695Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T02:02:12.639Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && grep -n 'SREU\\|STRAUMAZ\\|STROTAS\\|RAUTAH\\|SROTAS' ARY_pages.txt ARY_latin_index_pages.txt | head -20",
 "description": "ARY grep for sreu"
}
```


### [2026-09-14T02:02:12.709Z] TOOL RESULT

```
ARY_latin_index_pages.txt:8932:STRAVA, LATVIAN) (3) 9 SROTAS
```


## [2026-09-14T02:02:15.365Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && sed -n '8915,8945p' ARY_latin_index_pages.txt",
 "description": "ARY index context"
}
```


### [2026-09-14T02:02:15.413Z] TOOL RESULT

```
ALUES + JARMENIAN) 5!
‘REFERENCES beth ALOPEKS GREEK) gli,
POKORNY = SSSOS*~«*CTS VOLPES MATIN) ga 4
DELAMARRE: (RENARD) 135 RAPOSA (horatisny elslel
MACKENZIE: (FOX) 115 RAPOSA s(PORTUGUESE) J 5,
4A i gbG dy RAV DANISH) Sails
RAV (SWEDISH) 5-8 yo
[pdf page 309]
alersyay) | Ve
leg: STROOM (DUTCH) sala RAODHAITI, AVESTAN) gles!
OLD CHURCH SLAVIC) pS 53%! RAVAN
STRUJA : RAUTA (OLD PERSIAN) gl go
STRUMIEN HPOLISH)  gl-ng) ROT, ROD s(PAHLAVI) (5 shay
STRUIA (RUSSIAN) 9 RO, RUBAR (KURDISH) 53,5
REKA (CZECH) Sex ROT HBALUCHI) 3
RIEKA SLOVAK) Su -RUD (AFGHAN) (3-4) gl
SRAVETI, SRUTHL(LITHUANIAN) | jl} SRAVATI, SRU, (SANSKRIT) < Site
STRAVA, LATVIAN) (3) 9 SROTAS
STRAUME ROT ARMENIAN)
SRUAIMM — (OLD IRISH) oS 54 p! RHEIN, REUM AGREEK) gly
SSRWD A(WELSH) ($3) :(OLD SCANDINAVIAN) -745,5-thay!
STRAUMR
‘REFERENCES beh STROM — (OLD SAXON) pS i yp-Se
POKORNY, = SOS*~*~*~*~*~*~*«d STRAM (OLD FRISIAN) cS 623
BARNHART: (STREAM) 1075 | (OLD HIGH GERMAN) oS glT
MACKENZIE: (RIVER) 131 STROUM
BUCK: 41-42 STROM (GERMAN) glaJT
ONIONS: (STREAM) 874 STREAM (OLD ENGLISH) oS gt!
SKEAT: * (STREAM) 706 STREAM ENGLISH) gJS\
+ | RAMAT: 130 STROM DANISH) Sails
AMINDAROV: 29 STROM :(SWEDISH) 45 ye
```


## [2026-09-14T02:02:27.011Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 4fb414b5b270993d 72e1a21aebd58fd4; do echo \"#### $f\"; grep -o 'فرهنگ معین.\\{0,300\\}' $f.txt | head -3; grep -o '\\[فر\\..\\{0,120\\}' $f.txt | head -3; done",
 "description": "Check abadis Mo'in tags"
}
```


### [2026-09-14T02:02:28.073Z] TOOL RESULT

```
#### 4fb414b5b270993d
فرهنگ معین
فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راه
#### 72e1a21aebd58fd4
فرهنگ معین
فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راه
```


## [2026-09-14T02:02:31.121Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -o 'روماتیسم.\\{0,200\\}' 4fb414b5b270993d.txt | head -5; echo ---; grep -o 'ریتم.\\{0,200\\}' 72e1a21aebd58fd4.txt | head -5",
 "description": "Extract abadis entries"
}
```


### [2026-09-14T02:02:32.078Z] TOOL RESULT

```
روماتیسم - معنی در دیکشنری آبادیس
روماتیسم - معنی در دیکشنری آبادیس 
روماتیسم
روماتیسم. ( فرانسوی ، اِ ) بیماری درد مفاصل. ( ناظم الاطباء ). رثیه. ریاح طیاری. ( یادداشت مؤلف ). مرضی که به سبب دردهای عارض در مفاصل مشخص است. عامل این مرض می تواند یک ویروس و یا استرپتوکوک در نوع رماتیسم 
روماتیسم اقسام مختلف دارد. ( از فرهنگ فارسی معین ). 
---
ریتم - معنی در دیکشنری آبادیس
ریتم - معنی در دیکشنری آبادیس 
ریتم
ریتم : ایقاع، ضرب، وزن
ریتم. ( فرانسوی ، اِ ) توالی ضربات آهنگ که برای موزون کردن نوای موسیقی به کار می رود. ضرب. ( فرهنگ فارسی معین ).
```


## [2026-09-14T02:02:37.938Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 9fe127a480490d44 fd64323d9ab8bfe5 648673ea8897e303; do echo \"#### $f\"; sed -n '1,6p' $f.txt; grep -o 'from PIE root \\*sreu.\\{0,200\\}\\|1550s.\\{0,250\\}\\|late 14c\\..\\{0,250\\}' $f.txt | head -4; done",
 "description": "Etymonline content"
}
```


### [2026-09-14T02:02:39.044Z] TOOL RESULT

```
#### 9fe127a480490d44
URL: https://www.etymonline.com/word/rhythm
FETCHED: 2026-09-14T02:00:11Z
STATUS: 200
TITLE: Rhythm - Etymology, Origin & Meaning

Rhythm - Etymology, Origin & Meaning 
from PIE root *sreu- "to flow"). Compare rhyme .
1550s as "metrical movement, movement in time characterized by equality of measures and alteration of stress and relaxation." By 1776 as "regular succession of beats or accents in music."
from PIE root *sreu- "to flow").
late 14c., cicle, "perpetual circulating period of time, on the completion of which certain phenomena return in the same order," especially and originally in reference to astronomical phenomena, from Old French cicle and directly from Late Latin cyclus, from 
#### fd64323d9ab8bfe5
URL: https://www.etymonline.com/word/rheumatism
FETCHED: 2026-09-14T02:00:11Z
STATUS: 200
TITLE: Rheumatism - Etymology, Origin & Meaning

Rheumatism - Etymology, Origin & Meaning 
late 14c., reume , "watery fluid or humid matter in the eyes, nose, or mouth" (including tears, saliva, mucous discharge from the nostrils), from Old French reume "a head-cold" (13c., Modern French rhume ) and directly from Latin rheuma , reuma , from Greek r
from PIE root *sreu- "to flow").
late 14c. as "a head-cold, catarrh." The -h- was restored in early Modern English.
late 14c., "cogent, convincing, compelling" (of evidence, an argument, etc.); c. 1400 as "full of meaning;" from Old French preignant "pregnant, pithy, ready capable," which is probably from Latin praegnans "with child, pregnant, fu
#### 648673ea8897e303
URL: https://www.etymonline.com/word/stream
FETCHED: 2026-09-14T02:01:58Z
STATUS: 200
TITLE: Stream - Etymology, Origin & Meaning

Stream - Etymology, Origin & Meaning 
from PIE root *sreu- "to flow."
late 14c., as is the sense of "steady current in a river."
late 14c. Related: Streamed ; streaming . Compare German strömen , Dutch stroomen , Danish strömme , all verbs from nouns. Of air, c. 1300; of light from late 14c.; of flags, 1550s, of hair, 1731.
late 14c., mocioun, "process of moving; change of place, continuous variation of position;" also "suggestion, proposal or proposition formally made," from Old French mocion "movement, motion; change, alteration" (13c., Modern French motion) and directly from
```


## [2026-09-14T02:03:09.491Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i 'srem\\|srēm\\|srĕm\\|srěm' IEC.txt POK_full.txt | head -20",
 "description": "Search Srem forms"
}
```


### [2026-09-14T02:03:09.568Z] TOOL RESULT

```
POK_full.txt:45847:Prunus padus', kir. cerem-cha, -ucha6s., sloven, crem-ha, -5a(and with palatal) srem-sa, 
POK_full.txt:50106:A s-form sRem- one seeks incredible in Gothic skaman' be ashamed'. Old English 
POK_full.txt:51898:srayah-, Superl. Old Indie srestha- {srai'stha-), Avestan sraesta-. Old Indie sreman-m. " 
POK_full.txt:73977:nrh), Venetic PN Sirmid{*Sermid), Pannonian PN Sirmium, poln. (Venetic) PN Srem
```


## [2026-09-14T02:03:19.436Z] TOOL CALL #57: Bash

```json
{
 "command": "sed -n '1,80p' tools/verify_check.py",
 "description": "Inspect verify_check.py"
}
```


### [2026-09-14T02:03:19.495Z] TOOL RESULT

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
```


## [2026-09-14T02:03:21.620Z] TOOL CALL #58: Bash

```json
{
 "command": "sed -n '80,140p' tools/verify_check.py",
 "description": "Rest of verify_check"
}
```


### [2026-09-14T02:03:21.670Z] TOOL RESULT

```
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


## [2026-09-14T02:03:36.638Z] TOOL CALL #59: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg445.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/445.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | tail -5",
 "description": "Copy page image for audit"
}
```


### [2026-09-14T02:03:36.761Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb  90918 Sep  5 10:16 92.png
-rw-rw-r--  1 sfmqrb sfmqrb  93420 Sep  5 10:18 94.png
-rw-rw-r--  1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r--  1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r--  1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
```


## [2026-09-14T02:10:01.172Z] TOOL CALL #60: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-445.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\nSREW = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/srew-\"\nRUD = \"https://en.wiktionary.org/wiki/%D8%B1%D9%88%D8%AF\"\nRAMIDAN = \"https://en.wiktionary.org/wiki/%D8%B1%D9%85%DB%8C%D8%AF%D9%86\"\nRAWDA = \"https://en.wiktionary.org/wiki/%D8%B1%D9%88%D8%B6%D8%A9\"\nET_RHY = \"https://www.etymonline.com/word/rhythm\"\nET_RHE = \"https://www.etymonline.com/word/rheumatism\"\nET_STR = \"https://www.etymonline.com/word/stream\"\nAB_ROM = \"https://abadis.ir/fatofa/%D8%B1%D9%88%D9%85%D8%A7%D8%AA%DB%8C%D8%B3%D9%85/\"\nAB_RIT = \"https://abadis.ir/fatofa/%D8%B1%DB%8C%D8%AA%D9%85/\"\n\nnodes = []\n\ndef N(**kw):\n    nodes.append(kw)\n\nN(\n id=1, lang=\"Indo-European\", words=\"Sreu, Sru; Srěm\", verdict=\"plausible\",\n derivation=(\n  \"PIE *srew- 'to flow' is a real root and is indeed an extension of *ser- 'to flow': Pokorny \"\n  \"closes the sreu- article (IEW 1003) with 'Idg. sreu- ist Erw. von ser- \\\"fließen\\\"', so Nourai's \"\n  \"root→node arrow is exactly what his cited page says. The zero grade *sru- appears in Gk. rhutos, \"\n  \"Skt. sruta-, and the suffixed forms *sréw-mn̥ (Gk. rheuma), *srow-mo- (Gmc. *straumaz) and \"\n  \"*srew-tos (Skt. srotas-, OP rautah-) generate everything below. The second form on the card, \"\n  \"'Srěm : flow, running', is not a reconstruction any handbook prints: the page Nourai cites, \"\n  \"Mann IEC 1276, has 'sreum- \\\"flowing; flow, stream; pour\\\"' (with Gk. rheuma, Alb. rrymë, OIr. \"\n  \"sruaim), which is almost certainly what 'Srěm' is meant to be — a garbled *sreum-. (The only \"\n  \"'Srem' in Pokorny is the Polish/Venetic place-name Śrem *Sermo- under ser-1, p. 910, not a root.) \"\n  \"Hence plausible rather than confirmed: the first two forms are right, the third is a misprint of \"\n  \"Mann's headword.\"),\n derivation_fa=(\n  \"ریشهٔ هندواروپایی آغازین *srew- «جاری شدن» گسترش‌یافتهٔ *ser- با همان معناست؛ پوکورنی خود در پایان \"\n  \"مدخل sreu- (ص ۱۰۰۳) می‌نویسد که sreu- صورت گسترده‌ٔ ser- است، پس پیوند ریشه به این گره درست است. \"\n  \"ستاک تهی‌درجهٔ *sru- و صورت‌های پسوندی *sréw-mn̥ (یونانی rheuma)، *srow-mo- (ژرمنی *straumaz) و \"\n  \"*srew-tos (سنسکریت srotas-، پارسی باستان rautah-) سرچشمهٔ همهٔ شاخه‌های این نمودارند. اما صورت دوم \"\n  \"«Srěm» در هیچ فرهنگ معتبری چنین بازسازی نشده است؛ در همان صفحهٔ مأخذ نورایی (مان، ص ۱۲۷۶) مدخل \"\n  \"sreum- «جاری، جریان» آمده و پیداست که «Srěm» خطای چاپی کتاب برای *sreum- است. بنابراین ادعای نورایی \"\n  \"با احتیاط پذیرفتنی است.\"),\n sources=[SREW],\n ref_check=[\n  {\"ref\": \"POK:1003\", \"status\": \"supports\",\n   \"note\": \"Pokorny IEW 1003 'Root/lemma: sreu-, Meaning: to flow' … closing line 'Indo Germanic sreu- is extension from ser- \\\"flow\\\"' (POK_full.txt line 80867 ff.; Page(s): 1003).\"},\n  {\"ref\": \"KNT:205\", \"status\": \"supports\",\n   \"note\": \"Kent, Old Persian, Lexicon s.v. rautah-: 'sb. \\\"river\\\" (§166): NPers. rōd, Skt. srótas- \\\"current, river\\\", pIE *sreutos … to root *sreu- \\\"flow\\\"' (KNT.txt line 5847; r- pages of the lexicon, pp. 204-205).\"},\n  {\"ref\": \"IEC:1276\", \"status\": \"partial\",\n   \"note\": \"Mann IEC p.1276 (leaf 704) has 'sreum- \\\"flowing; flow, stream; pour\\\"', 'sreut- \\\"flow\\\"' and 'sreuō, io \\\"run, flow\\\"' — so 'Sreu, Sru' is supported, but the page has no headword spelled 'Srěm'.\"}],\n consulted=[\n  {\"src\": \"WLD\", \"where\": \"Bd. II 702-703\", \"stance\": \"supports\",\n   \"note\": \"'sreu- \\\"fließen\\\"' with the same material; 'Idg. sreu- ist Erw. von ser- \\\"fließen\\\"' (WLD_Bd2_pages.txt lines 46634, 46692).\"},\n  {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. sreu-\", \"stance\": \"supports\",\n   \"note\": \"'sreu-. To flow. 1. Suffixed o-grade form *srou-mo- in Germanic *straumaz … 2. Basic form *sreu- in Greek rhein … [Pok. sreu- 1003.]'\"},\n  {\"src\": \"IEC\", \"where\": \"p. 1276\", \"stance\": \"partial\",\n   \"note\": \"'sreum- \\\"flowing; flow, stream; pour\\\". Cf. sroum-, sru-, etc. WP II, 703' — the likely original of the card's 'Srěm'.\"},\n  {\"src\": \"KLN\", \"where\": \"1966 s.v. stream\", \"stance\": \"supports\",\n   \"note\": \"'fr. I.-E. base *sreu-, \\\"to flow\\\" … Base *sreu- is an enlargement of base *ser-' (KLN_1966.txt line 36992).\"}],\n)\n\nN(\n id=2, lang=\"Avestan / Old Persian\", words=\"rautah, raodah; raodaiti\", verdict=\"confirmed\",\n derivation=(\n  \"OP rautah- 'river' (neuter s-stem, attested in DZc 9 of the Nile: 'rauta tya Mudrāyaiy danuvatiy') \"\n  \"continues PIE *srew-tos; the Iranian loss of initial s- before r (*sr- > *hr- > r-) is regular, \"\n  \"and Skt. srótas- is the exact cognate. Avestan has the same stem with the sandhi-variant θraotah- \"\n  \"in compounds, beside raoδah- n. 'river' and the thematic present raoδaiti 'flows' (a dh-present to \"\n  \"the same root, with intervocalic *d > δ). Kent's lexicon, Bartholomae and Buck all put these three \"\n  \"forms under *sreu-, exactly as the chart draws it. Nourai's single box labelled 'Avestan / Old \"\n  \"Persian' mixes the two languages: rautah- is Old Persian, raoδah-/raoδaiti are Avestan.\"),\n derivation_fa=(\n  \"پارسی باستان rautah- «رود» (ستاک خنثیِ ـs، در کتیبهٔ DZc دربارهٔ نیل: rauta tya Mudrāyaiy danuvatiy) \"\n  \"دنبالهٔ *srew-tos هندواروپایی است؛ افتادن s آغازین پیش از r در ایرانی (sr- > hr- > r-) قاعده‌مند است و \"\n  \"srótas- سنسکریت همتای دقیق آن است. در اوستایی همین ستاک به صورت θraotah- (در ترکیب‌ها) و raoδah- \"\n  \"«رود» دیده می‌شود و فعل raoδaiti «می‌رود، جاری است» نیز از همین ریشه است (d ایرانی باستان میان دو واکه \"\n  \"در اوستایی به δ بدل شده). کنت، بارتولومه و باک هر سه این صورت‌ها را زیر *sreu- آورده‌اند؛ پس ادعای نورایی \"\n  \"درست است. تنها یادداشت این‌که در یک جعبه دو زبان درآمیخته: rautah- پارسی باستان و raoδah-/raoδaiti اوستایی است.\"),\n sources=[SREW, RUD],\n ref_check=[\n  {\"ref\": \"POK:1003\", \"status\": \"supports\",\n   \"note\": \"IEW 1003: 'Old Indie srotah- …, Old pers. rautah-, npers. rōd \\\"river\\\"'; 'Avestan raodaiti \\\"flows\\\", raoδah- n. \\\"river\\\", urud- \\\"river flow, bed\\\"'.\"},\n  {\"ref\": \"HRN:139\", \"status\": \"supports\",\n   \"note\": \"Horn, Grundriss §627 (p.139): 'röd \\\"Fluss\\\", rödbar … ap. rautah- \\\"Fluss\\\"; phlv. röt, rötbar (Bund.); ai. srótas- \\\"Strömung, Strombett, Strom, Fluss\\\"' (HRN.txt leaf 160).\"}],\n consulted=[\n  {\"src\": \"KNT\", \"where\": \"Lexicon s.v. rautah- (pp.204-205)\", \"stance\": \"supports\",\n   \"note\": \"'rautah- sb. \\\"river\\\" (§166): NPers. rōd, Skt. srótas- …, pIE *sreutos … to root *sreu- \\\"flow\\\"; perhaps same as Av. θraotah-, with sandhi initial (Bthl. AiW 800).'\"},\n  {\"src\": \"SYN\", \"where\": \"Buck 1.36 RIVER (pp.41-42)\", \"stance\": \"supports\",\n   \"note\": \"'Skt. srotas-, sravat-, Av. θraotah- (in cpds.), ravan-, raoδah-, \\\"stream, river\\\", OPers. rauta \\\"river\\\" (used of the Nile), NPers. rūd \\\"river\\\"' — all under '1. Derivs. of IE *sreu- \\\"flow\\\"'.\"},\n  {\"src\": \"ARY\", \"where\": \"s.v. رود (Latin index, pdf p.309)\", \"stance\": \"supports\",\n   \"note\": \"Aryanpur's cognate list for رود: 'RAODHAITI (AVESTAN), RAVAN, RAUTA (OLD PERSIAN), ROT, ROD (PAHLAVI) …' with references 'POKORNY 1003; MACKENZIE (RIVER) 131; BUCK 41-42'.\"}],\n)\n\nN(\n id=3, lang=\"Pahlavi\", words=\"rôt 2\", verdict=\"confirmed\",\n derivation=(\n  \"Middle Persian rōd (written ⟨lwt'⟩, ideogram YM' ) 'river' is the regular continuation of OP \"\n  \"rautah-: the Old Iranian s-stem loses its ending, the diphthong au monophthongises to ō, and the \"\n  \"final -t stays voiceless in the Book-Pahlavi spelling while it is voiced -d in the spoken form. \"\n  \"Nyberg glosses the word and derives it in one line from Old Persian; Horn already had 'phlv. röt, \"\n  \"rötbar (Bund.)'. Nourai's '2' distinguishes this rōd from the homonym rōd 'gut, string (of an \"\n  \"instrument)' (MP rōdīg), a different word. His reference is only the bare 'MON', but the derivation \"\n  \"is the standard one.\"),\n derivation_fa=(\n  \"فارسی میانهٔ rōd (به خط پهلوی ⟨lwt'⟩، هُزوارش YM') «رود» دنبالهٔ قاعده‌مند rautah- پارسی باستان است: \"\n  \"پایانهٔ ستاک ـah از میان رفته، مصوت مرکب au به ō تک‌آوا شده و -t پایانی در املای پهلوی نگاه داشته شده \"\n  \"است. نیبرگ در واژه‌نامهٔ خود rōt را یکراست از پارسی باستان rautah- می‌گیرد و هرن نیز «phlv. röt, rötbar» \"\n  \"آورده است. شمارهٔ «۲» در کتاب برای جدا کردن این واژه از هم‌آوای آن rōd «روده، زهِ ساز» است. ادعای نورایی درست است.\"),\n sources=[RUD],\n ref_check=[\n  {\"ref\": \"MON\", \"status\": \"not_checked\",\n   \"note\": \"Nourai gives only the bare abbreviation MON (Mo'in) with no volume/page; the 6-vol. print edition is not online and the 2-vol. abridgement (MON_part1/2.txt) has no Pahlavi transliterations. The claim is however covered by Nyberg and MacKenzie below.\"}],\n consulted=[\n  {\"src\": \"NYB\", \"where\": \"Glossary p. (s.v. rōt)\", \"stance\": \"supports\",\n   \"note\": \"'rot [lwt'; YM'] river P1:3. 562(14-16). — OP rautah-; MPrthPrs rud; Paz. NP rōd' (NYB_vol2_glossary.txt line 3348).\"},\n  {\"src\": \"PHD\", \"where\": \"Pahlavi key, 'rōd'\", \"stance\": \"partial\",\n   \"note\": \"MacKenzie's index page lists the headword 'rod' (PHD.txt line 4479 in the Pahlavi key); the OCR of the main entry is unusable, but Aryanpur cites 'MACKENZIE: (RIVER) 131' for MP rōd.\"},\n  {\"src\": \"HRN\", \"where\": \"no. 627, p.139\", \"stance\": \"supports\",\n   \"note\": \"'phlv. röt, rötbar (Bund.)' beside 'ap. rautah- \\\"Fluss\\\"'.\"}],\n)\n\nN(\n id=4, lang=\"Persian\", words=\"rŭd «رود ( رودخانه )»; rŭd-bâr «رودبار»\", verdict=\"confirmed\",\n derivation=(\n  \"NP رود rūd/rōd 'river' is inherited straight from MP rōd; the Classical majhūl vowel ō (rōd) became \"\n  \"ū in modern Iranian Persian while Dari keeps rōd, exactly as with شیر/گور. رودبار rūd-bār 'riverside, \"\n  \"a land of many streams' is the same noun plus the old suffix -bār 'place bearing/holding' (cf. جویبار \"\n  \"jūy-bār, مرغزار-type formations); Horn already cites 'rödbar' from the Bundahišn, so the compound is \"\n  \"pre-Islamic. The book's parenthetical gloss «رودخانه» is the modern Persian synonym (rūd + xāne). The \"\n  \"cited page, Borhan-e Qāṭeʿ 969, is precisely the page on which رود and رودبار stand.\"),\n derivation_fa=(\n  \"«رود» در فارسی نو میراث مستقیم rōd فارسی میانه است؛ واکهٔ مجهول ō در فارسی ایرانِ امروز به ū بدل شده \"\n  \"(rūd) حال آن‌که در دری همچنان rōd گفته می‌شود، درست مانند «شیر» و «گور». «رودبار» همان اسم است با \"\n  \"پسوند کهنِ -بار «دارنده، جای» (سنجید­ه با «جویبار»)؛ هرن صورت پهلوی rōtbār را از بندهش نقل کرده، پس \"\n  \"ترکیب پیش از اسلام ساخته شده است. حاشیهٔ معین بر برهان قاطع (ص ۹۶۹) ذیل «رود» همین را می‌گوید: «پارسی \"\n  \"باستان rauta-، بارتولمه؛ هندی باستان srotas- (جریان آب)؛ کردی ro، بلوچی rōt؛ ارمنی rot (وام از ایرانی)، \"\n  \"هوبشمان». ادعای نورایی درست است.\"),\n sources=[RUD],\n ref_check=[\n  {\"ref\": \"BQT:969\", \"status\": \"supports\",\n   \"note\": \"Borhan-e Qāṭeʿ ed. Moʿin, p.969 (BQT_v2_pages.txt leaf 429; running heads of leaves 431/432/433 read ۹۷۱/۹۷۲/۹۷۳, so leaf 429 = p.969) has the headwords «رود … رودخانهٔ عظیم و سیال را گویند» and «رودبار», and Moʿin's footnote 4 at the foot of that page: «(رود) پارسی باستان rauta- «بارتولمه»، هندی باستان srotas- «جریان آب» … کردی ro، بلوچی rōt … ارمنی rot (رود) «هوبشمان»».\"}],\n consulted=[\n  {\"src\": \"HRN\", \"where\": \"no. 627, p.139\", \"stance\": \"supports\",\n   \"note\": \"'röd \\\"Fluss\\\", rödbar, rödxāne' — Horn lists exactly the two words of this box plus رودخانه.\"},\n  {\"src\": \"HUB\", \"where\": \"Persische Studien (Armenian loans)\", \"stance\": \"supports\",\n   \"note\": \"'\\\"Fluss\\\", arm. rot = ap. rautah-, skr. srotas' (HUB.txt line 7784) — Hübschmann derives Arm. rot from the same Old Persian word that gives NP rūd.\"},\n  {\"src\": \"ARY\", \"where\": \"s.v. رود\", \"stance\": \"supports\",\n   \"note\": \"Aryanpur puts NP رود under PIE *sreu- with Kurdish ro/rubar, Baluchi rot, Afghan -rud, citing Pokorny 1003 and Buck 41-42.\"},\n  {\"src\": \"SYN\", \"where\": \"Buck 1.36\", \"stance\": \"supports\",\n   \"note\": \"'NPers. rūd \\\"river\\\"' listed under derivatives of IE *sreu-.\"}],\n)\n\nN(\n id=5, lang=\"Arabic\", words=\"rauza\", verdict=\"disputed\",\n derivation=(\n  \"Arabic رَوْضة rawḍa 'well-watered meadow, garden' (Qur'ān 30:15, 42:22) is what Nourai derives from \"\n  \"Pahlavi rōd. He is faithfully following his source: Jeffery, Foreign Vocabulary of the Qur'ān 145-146 \"\n  \"(= VDQ 226) reports Vollers's view that the word is Iranian and concludes 'the Arabs learned the Phlv. \"\n  \"rōd in the Mesopotamian area and used it for any well watered or irrigated land', citing Horn 139 and \"\n  \"Bartholomae AiW 1495. Modern scholarship does not follow this. (a) Phonologically the loan is bad: \"\n  \"Persian d is normally rendered by Arabic د, not by the emphatic ض, and the -ah of rawḍa is a native \"\n  \"feminine ending on a triliteral pattern faʿla. (b) The word sits in a productive native root ر و ض \"\n  \"with rāḍa 'to break in, train', riyāḍ 'meadows', riyāḍa 'exercise', which Wiktionary and the Arabic \"\n  \"lexica treat as Semitic. (c) Asbaghi, Persische Lehnwörter im Arabischen 138 — the reference Nourai's \"\n  \"own NOTE cites — does call it a Persian loan but from a completely different word: 'rauda: \\\"Garten\\\" \"\n  \"aus pers. raz, v. Verb rostan, mp. rōd << aw. raod / ap. raza \\\"Weinstock\\\"', i.e. from the root *(H)raud- \"\n  \"'to grow' (Nourai's 'Leudh'), not from rōd 'river'; and Jeffery himself dismisses that route ('Addai \"\n  \"Sher, 75, wants to derive رَوْضة from Pers. رز, which seems to be wide of the mark'). Note also that on \"\n  \"the same page Asbaghi does record the genuine loan of this word-family: 'rūt: \\\"Fluß\\\" aus pers. rūd, mp. \"\n  \"rōd < a. rautah' — Arabic borrowed rūd as رُوت, not as رَوْضة. Nourai's NOTE is therefore accurate about \"\n  \"what PLA:138 says; the arrow itself is the disputed part.\"),\n derivation_fa=(\n  \"«رَوْضة» عربی «مرغزارِ پرآب، باغ» (قرآن، روم ۱۵ و شوری ۲۲) را نورایی از rōd فارسی میانه می‌گیرد و در این کار \"\n  \"وفادارانه از مأخذ خود پیروی کرده است: جفری در «واژه‌های دخیل در قرآن» صص ۱۴۵-۱۴۶ رأی فولرس را می‌آورد که \"\n  \"واژه ایرانی است و نتیجه می‌گیرد عرب‌ها rōd پهلوی را در بین‌النهرین شنیدند و آن را بر هر زمین آبیاری‌شده \"\n  \"اطلاق کردند. اما پژوهش امروزی این را نمی‌پذیرد: نخست از نظر آوایی، دالِ فارسی در معرّب‌ها معمولاً به «د» بدل \"\n  \"می‌شود نه به «ض» تفخیمی؛ دوم، «روضة» در دلِ ریشهٔ زایای سه‌حرفی ر و ض (راضَ «رام کردن»، ریاض، ریاضة) نشسته \"\n  \"است و ویکی‌واژه و فرهنگ‌های عربی آن را واژه‌ای سامی می‌دانند؛ سوم، اصباغی در «وام‌واژه‌های فارسی در عربی» ص ۱۳۸ \"\n  \"— همان مأخذی که یادداشت خودِ نورایی به آن ارجاع می‌دهد — آن را وام‌واژه می‌داند اما از «رز» (اوستایی raod- \"\n  \"«روییدن»، پارسی باستان raza «تاک»)، نه از «رود». افزون بر این، اصباغی در همان صفحه وام‌گیری واقعی این \"\n  \"خانواده را ثبت کرده است: «rūt: رود، از فارسی rūd، فارسی میانه rōd، از ایرانی باستان rautah». پس یادداشت \"\n  \"نورایی دربارهٔ PLA درست نقل شده، ولی خودِ این پیکان پذیرفتنی نیست.\"),\n sources=[RAWDA],\n ref_check=[\n  {\"ref\": \"VDQ:226\", \"status\": \"supports\",\n   \"note\": \"VDQ is Badreh'i's Persian translation of Jeffery; checked in the original, FVQ pp.145-146 s.v. (Rauda): 'Vollers … noted that the word is originally Iranian … The Av. raoδah- \\\"a river\\\" … From the same root comes Phlv. rōd \\\"a lake or riverbed\\\" and the Pers. rūd … Thus the conclusion would seem to be that the Arabs learned the Phlv. rōd in the Mesopotamian area and used it for any well watered or irrigated land' (FVQ_pages.txt leaves 162-163; footnote: 'Horn, Grundriss 139; Bartholomae AiW 1495').\"},\n  {\"ref\": \"PLA:138\", \"status\": \"partial\",\n   \"note\": \"Nourai's NOTE is quoted correctly: Asbaghi p.138 (PLA_pages.txt leaf 152) prints 'rauda: \\\"Garten\\\" aus pers. raz, v. Verb rostan, mp. rōd << aw. raod / ap. raza \\\"Weinstock\\\"' — a Persian origin, but from *raud- 'grow', not from rōd 'river'.\"}],\n consulted=[\n  {\"src\": \"FVQ\", \"where\": \"pp.145-146 s.v. Rauḍa\", \"stance\": \"supports\",\n   \"note\": \"Jeffery accepts the Pahlavi rōd route and explicitly rejects the raz route in n.4: 'Addai Sher, 75, wants to derive رَوْضة from Pers. رز, which seems to be wide of the mark.'\"},\n  {\"src\": \"PLA\", \"where\": \"p.138\", \"stance\": \"contradicts\",\n   \"note\": \"Asbaghi derives rawḍa from Persian raz, and on the same page gives the true reflex of rōd in Arabic: 'rūt: \\\"Fluß\\\" aus pers. rūd, mp. rōd < a. rautah'.\"},\n  {\"src\": \"AFM\", \"where\": \"p.75 (cited by Jeffery)\", \"stance\": \"partial\",\n   \"note\": \"Addai Shir's Kitāb al-alfāẓ al-fārisiyya al-muʿarraba treats الروضة as a Persianism (the entry appears in AFM.txt lines 3105-3106, OCR badly damaged); he derives it from رز, not from رود.\"},\n  {\"src\": \"KLN\", \"where\": \"1966, no entry\", \"stance\": \"silent\",\n   \"note\": \"Klein has no 'rauda/rawda' headword (grepped rauda/rawda/rouda in KLN_1966.txt): the word never entered European languages, so he is silent.\"}],\n error_in=None,\n)\n\nN(\n id=6, lang=\"Persian\", words=\"rowzeh «روضه»\", verdict=\"confirmed\",\n derivation=(\n  \"NP روضه rowże 'garden, meadow' is an unremarkable Arabic loanword, taken over with its Arabic \"\n  \"spelling and its ض (pronounced /z/ in Persian), from Arabic رَوْضة rawḍa; the Arabic diphthong aw \"\n  \"is kept as ow in Persian, and the tāʾ marbūṭa is read as -e. Mo'in tags the headword exactly so: \"\n  \"«روضه [ع. روضه] (اِ.) باغ، گلزار؛ ج. ریاض، روضات». The word is productive in Persian in senses the \"\n  \"Arabic does not have (روضه‌خوانی 'the recitation of the Karbala lament', from روضة الشهداء, Kāšefi's \"\n  \"book of 908/1502), and the Hafez line quoted on the card («روضهٔ خلد برین خلوت درویشان است») uses it \"\n  \"in the Qur'anic sense 'the garden of Paradise'. This node is correct whatever the ultimate origin of \"\n  \"the Arabic word: if node #5 is right the word is a Persian→Arabic→Persian round trip, if not it is a \"\n  \"plain Arabic loan.\"),\n derivation_fa=(\n  \"«روضه» در فارسی وام‌واژه‌ای عربی است که با املا و «ض» خود به فارسی آمده (در فارسی /ز/ تلفظ می‌شود)؛ \"\n  \"مصوت مرکب aw عربی در فارسی ow مانده و تای گرد به -ه خوانده شده است. معین در فرهنگ فارسی همین را \"\n  \"می‌گوید: «روضه [ع. روضه] (اِ.) باغ، گلزار؛ ج. ریاض، روضات». این واژه در فارسی زایا شده و معناهایی یافته \"\n  \"که در عربی ندارد (روضه‌خوانی، از «روضة الشهداء» کاشفی، ۹۰۸ ق) و بیت حافظِ نقل‌شده در نمودار آن را به \"\n  \"معنای قرآنی «باغ بهشت» به کار برده است. این پیکان در هر حال درست است: اگر گرهٔ ۵ پذیرفته شود، «روضه» \"\n  \"وام‌واژه‌ای دوسویه (فارسی ← عربی ← فارسی) است و اگر نه، وام‌واژه‌ای سادهٔ عربی.\"),\n sources=[RAWDA],\n ref_check=[\n  {\"ref\": \"MON\", \"status\": \"supports\",\n   \"note\": \"Mo'in, Farhang-e Fārsi s.v. روضه (MON_part1.txt line 69105): «روضه: rowza [ع. روضه] (اِ.) باغ، گلزار؛ ج. ریاض، روضات» — the tag [ع.] is Mo'in's marker for an Arabic loan.\"}],\n consulted=[\n  {\"src\": \"MON\", \"where\": \"s.v. روضه\", \"stance\": \"supports\",\n   \"note\": \"[ع.] 'Arabic'; no Persian etymon is claimed for the Persian word itself.\"},\n  {\"src\": \"FVQ\", \"where\": \"pp.145-146\", \"stance\": \"partial\",\n   \"note\": \"Jeffery documents the Arabic word and its Qur'anic use, which is what Persian borrowed; he says nothing about the re-borrowing into Persian.\"},\n  {\"src\": \"PLA\", \"where\": \"p.138\", \"stance\": \"partial\",\n   \"note\": \"Asbaghi lists rauda among Persian loans in Arabic, which would make روضه a round-trip; but from raz, not rōd.\"}],\n)\n\nN(\n id=7, lang=\"Sogdian\", words=\"rwt\", verdict=\"confirmed\",\n derivation=(\n  \"Sogdian rwt /rōt/ 'river' (Manichaean and Christian texts; also spelt rwwt) is the East Iranian \"\n  \"cognate of MP rōd, from the same Old Iranian *rautah- with the regular Iranian loss of *s- before \"\n  \"*r-. Gharib's dictionary, the very reference cited, derives it explicitly from Old Persian rautah-. \"\n  \"Nourai hangs the node on the Indo-European box #1 rather than on the Old Iranian box #2; \"\n  \"historically it should descend through Old Iranian, as Gharib's own note shows.\"),\n derivation_fa=(\n  \"سغدی rwt /rōt/ «رود» (در متون مانوی و مسیحی، به املای rwwt نیز) همتای ایرانی شرقیِ rōd فارسی میانه \"\n  \"است و هر دو از *rautah- ایرانی باستان می‌آیند، با همان افتادن قاعده‌مند s پیش از r. غریب در «فرهنگ \"\n  \"سغدی» — همان مأخذی که نورایی آورده — آن را صریحاً از rautah- پارسی باستان می‌گیرد. تنها نکته این‌که \"\n  \"نورایی این گره را یکراست به جعبهٔ هندواروپایی وصل کرده، حال آن‌که از نظر تاریخی باید از گرهٔ ایرانی باستان \"\n  \"(#۲) بگذرد. ادعای نورایی درست است.\"),\n sources=[SREW],\n ref_check=[\n  {\"ref\": \"SOD:346\", \"status\": \"supports\",\n   \"note\": \"Gharib, Sogdian Dictionary, printed p.346 (SOD_pages.txt leaf 413), entry 8600: 'rwt M, C — rot (rwwt) © <OP rautah- © ob. -y — river — GMS 39, 530; STii 1.20; BSTii 860.35, 879.11; C2 gloss. 22V7 …'. Nourai's 346 is the printed page, and the entry is on it.\"}],\n consulted=[\n  {\"src\": \"SOD\", \"where\": \"entry 8600, p.346\", \"stance\": \"supports\",\n   \"note\": \"'rot (rwwt) <OP rautah-, river'.\"},\n  {\"src\": \"NYB\", \"where\": \"s.v. Rōtastāk / rōt\", \"stance\": \"supports\",\n   \"note\": \"Nyberg's Pahlavi glossary compares 'MPrth rwdyst'g' and 'Old Sogd rwstmy', confirming the same rōd/rwt stem across the Middle Iranian dialects (NYB_vol2_glossary.txt lines 3348-3353).\"}],\n)\n\nN(\n id=8, lang=\"Avestan\", words=\"ravan; raonami; urvant, sru-vant\", verdict=\"transcription_suspect\",\n derivation=(\n  \"The three items come straight out of Pokorny's sreu- article, which reads: 'Avestan (ravan-), Gen. \"\n  \"Pl. raonąm \\\"die Flüsse\\\", urvant- (sru-vant-) \\\"flowing\\\"'. So ravan- 'river' is right and urvant-/\"\n  \"sru-vant- 'flowing' is right (a -uant- adjective to the zero grade *sru-, with the Avestan \"\n  \"development *sru- > uru-). But 'raonami' is not an Avestan form: Pokorny prints the genitive plural \"\n  \"raonąm, and Nourai has read the nasal hook of ⟨ą⟩ plus the ⟨m⟩ as ⟨ami⟩. The printed page 415 of the \"\n  \"book itself shows 'raonami : the rivers', so the extraction is faithful and the error is the author's \"\n  \"(a misread of his own source, not a scan artefact). Nourai's gloss 'the rivers' in fact preserves \"\n  \"Pokorny's 'die Flüsse' — i.e. he knew it was the genitive plural. The gloss 'fluently' for \"\n  \"urvant-/sru-vant- should be 'flowing' (an adjective, not an adverb). Node otherwise confirmed; \"\n  \"Buck 1.36 independently lists Av. ravan- and raoδah- under *sreu-.\"),\n derivation_fa=(\n  \"هر سه صورت این جعبه مستقیماً از مدخل sreu- پوکورنی (ص ۱۰۰۳) گرفته شده است: «اوستایی (ravan-)، جمع \"\n  \"اضافیِ raonąm «رودها»، urvant- (sru-vant-) «روان، جاری»». پس ravan- «رود» و urvant-/sru-vant- درست‌اند \"\n  \"(صفت با پسوند -uant- از درجهٔ تهیِ *sru-، که در اوستایی به uru- بدل می‌شود). اما «raonami» صورتی اوستایی \"\n  \"نیست: پوکورنی raonąm نوشته و نورایی قلّاب خیشومیِ ⟨ą⟩ را با ⟨m⟩ به‌صورت ⟨ami⟩ خوانده است. تصویر صفحهٔ ۴۱۵ \"\n  \"چاپی نشان می‌دهد که خودِ کتاب «raonami» دارد، پس خطا از نویسنده است نه از خوانش اسکن. برگردان «fluently» \"\n  \"نیز باید «flowing/روان» باشد. جز این، محتوای گره درست است و باک نیز ravan- و raoδah- اوستایی را زیر \"\n  \"*sreu- آورده است.\"),\n error_in=\"book\",\n book_prints=\"raonami : the rivers\",\n correct_form=\"raonąm (Av. gen. pl. of ravan- 'river')\",\n sources=[SREW],\n ref_check=[\n  {\"ref\": \"POK:1003\", \"status\": \"partial\",\n   \"note\": \"IEW 1003: 'Avestan (ravan-), Gen. Pl. raonąm \\\"die Flüsse\\\", urvant- (sru-vant-) \\\"flowing\\\"' — supports ravan- and urvant-/sru-vant-, but the page reads raonąm, not 'raonami'.\"}],\n consulted=[\n  {\"src\": \"SYN\", \"where\": \"Buck 1.36 RIVER\", \"stance\": \"supports\",\n   \"note\": \"'Av. θraotah- (in cpds.), ravan-, raoδah- \\\"stream, river\\\"' listed under IE *sreu-.\"},\n  {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch\", \"stance\": \"silent\",\n   \"note\": \"The local OCR of Bartholomae is too corrupt to locate cols. 1490-1500 reliably (grep for raoδah/raonąm returns only unrelated aurvant- lines); Kent and Jeffery both cite AiW 800 / 1495 for these stems.\"},\n  {\"src\": \"WLD\", \"where\": \"Bd. II 702-703\", \"stance\": \"supports\",\n   \"note\": \"Walde-Pokorny's sreu- article, the source of Pokorny's text, carries the same Avestan material.\"}],\n)\n\nN(\n id=9, lang=\"Germanic\", words=\"strau-maz\", verdict=\"confirmed\",\n derivation=(\n  \"Proto-Germanic *straumaz 'stream' < PIE *srow-mo-, the o-grade of *srew- with the -mo- suffix. The \"\n  \"-t- is the regular Germanic epenthesis in the cluster *sr- (*sr- > *str-, as in *streumaz beside Lith. \"\n  \"sraumuõ, Latv. straume, Pol. strumień, which have no -t-). Pokorny lists 'Old High German stroum, \"\n  \"Old English stream, Old Icelandic straumr'; Watkins reconstructs precisely 'Germanic *straumaz', \"\n  \"which is what the AHD reference Nourai cites prints.\"),\n derivation_fa=(\n  \"ژرمنی آغازین *straumaz «جویبار، جریان» از *srow-mo- هندواروپایی است، یعنی درجهٔ o ریشهٔ *srew- با \"\n  \"پسوند -mo-. حرف t در آن افزودهٔ قاعده‌مند ژرمنی در خوشهٔ *sr- است (*sr- > *str-)، چنان‌که همتایان بالتی و \"\n  \"اسلاوی بدون t هستند: لیتوانیایی sraumuõ، لتونیایی straume، لهستانی strumień. پوکورنی صورت‌های \"\n  \"stroum آلمانی علیای باستان، stream انگلیسی باستان و straumr نورس باستان را می‌آورد و واتکینز در پیوست \"\n  \"AHD دقیقاً *straumaz را بازسازی کرده است. ادعای نورایی درست است.\"),\n sources=[ET_STR, SREW],\n ref_check=[\n  {\"ref\": \"AHD\", \"status\": \"supports\",\n   \"note\": \"Watkins 1985 s.v. sreu-: '1. Suffixed o-grade form *srou-mo- in Germanic *straumaz, stream, in: a. Old English stréam, stream: STREAM; b. Dutch stroom, stream: MAELSTROM.'\"}],\n consulted=[\n  {\"src\": \"POK\", \"where\": \"IEW 1003\", \"stance\": \"supports\",\n   \"note\": \"'Old High German stroum. Old English stream. Old Icelandic straumr \\\"stream\\\" (: Latvian straume, poln. strumien).'\"},\n  {\"src\": \"KLN\", \"where\": \"1966 s.v. stream\", \"stance\": \"supports\",\n   \"note\": \"'rel. to OS. strom, ON. straumr … fr. I.-E. base *sreu-, \\\"to flow\\\"'.\"},\n  {\"src\": \"SYN\", \"where\": \"Buck 1.36\", \"stance\": \"supports\",\n   \"note\": \"'ON straumr, OE stréam, OHG strōm, etc. \\\"stream\\\"' under derivatives of IE *sreu-.\"}],\n)\n\nN(\n id=10, lang=\"English\", words=\"stream\", verdict=\"confirmed\",\n derivation=(\n  \"OE strēam 'flowing, current; running water, river' > ME strem, streme > NE stream, with the regular \"\n  \"Great Vowel Shift raising of ME ē to /iː/. The verb 'to stream' is a late-14c. denominative. This is \"\n  \"the direct native reflex of Germanic *straumaz, not a borrowing; Etymonline and Klein agree.\"),\n derivation_fa=(\n  \"انگلیسی باستان strēam «جریان، آب روان، رود» ← انگلیسی میانه strem ← انگلیسی نو stream؛ واکهٔ بلند ē \"\n  \"انگلیسی میانه در «جابه‌جایی بزرگ واکه‌ها» به /iː/ بدل شده است. فعل to stream در اواخر سدهٔ چهاردهم از \"\n  \"همین اسم ساخته شده. این واژه بازماندهٔ مستقیم و بومی *straumaz ژرمنی است، نه وام‌واژه. ادعای نورایی درست است.\"),\n sources=[ET_STR],\n ref_check=[\n  {\"ref\": \"None\", \"status\": \"not_checked\",\n   \"note\": \"The node carries no reference of its own; it inherits the AHD citation of its parent #9, which supports it ('Old English stréam, stream: STREAM').\"}],\n consulted=[\n  {\"src\": \"KLN\", \"where\": \"1966 s.v. stream\", \"stance\": \"supports\",\n   \"note\": \"'stream, n. — ME. strem, streme, fr. OE. stream, \\\"flowing, current; running water, river\\\" … fr. I.-E. base *sreu-.'\"},\n  {\"src\": \"AHD\", \"where\": \"Watkins s.v. sreu-\", \"stance\": \"supports\",\n   \"note\": \"'Old English stréam, stream: STREAM'.\"},\n  {\"src\": \"SKT\", \"where\": \"Concise Etym. Dict. s.v. stream\", \"stance\": \"supports\",\n   \"note\": \"Cited by Aryanpur ('SKEAT: (STREAM) 706') in his cognate list for رود, alongside Onions 874 and Barnhart 1075.\"}],\n)\n\nN(\n id=11, lang=\"Greek\", words=\"rhein; rheuma; rhutmos\", verdict=\"confirmed\",\n derivation=(\n  \"Greek ῥέω/ῥεῖν rheîn 'to flow' < *sréw-e-ti, with the regular Greek loss of initial *s- and the \"\n  \"resulting aspirated rho (ῥ- = hr-); ῥεῦμα rheûma 'stream, flux, humour of the body' < *sréw-mn̥ \"\n  \"(a men-stem, gen. rheúmatos); ῥυθμός rhuthmós 'measured motion, proportion, rhythm' < zero grade \"\n  \"*sru-dhmo-. The card's gloss 'rhyme' for rhutmos is a shortcut: the Greek word means 'rhythm', and \"\n  \"'rhyme' is only the later English descendant of it (through Latin rhythmus and Old French rime). \"\n  \"Watkins puts all three under sreu- exactly as drawn.\"),\n derivation_fa=(\n  \"یونانی ῥεῖν rheîn «جاری شدن» از *sréw-e-ti است؛ s آغازین در یونانی افتاده و بازماندهٔ آن دمِش روی ρ \"\n  \"است (ῥ- = hr-). ῥεῦμα rheûma «جریان، سیلان، خِلط بدن» از ستاک men‌دارِ *sréw-mn̥ و ῥυθμός rhuthmós \"\n  \"«حرکت موزون، تناسب، وزن» از درجهٔ تهیِ *sru-dhmo- می‌آید. برگردان «rhyme» برای rhutmos در کتاب \"\n  \"کوتاه‌نویسی است: معنای واژهٔ یونانی «ریتم» است و «قافیه» تنها بازماندهٔ متأخر انگلیسی آن (از راه لاتینی \"\n  \"rhythmus و فرانسهٔ کهن rime) است. واتکینز هر سه را زیر sreu- آورده، پس ادعای نورایی درست است.\"),\n sources=[ET_RHY, SREW],\n ref_check=[\n  {\"ref\": \"AHD\", \"status\": \"supports\",\n   \"note\": \"Watkins 1985 s.v. sreu-: '2. Basic form *sreu- in: a. Greek rhein, to flow: RHEO-, -RRHEA; CATARRH, DIARRHEA, HEMORRHOID, RHYOLITE; b. suffixed form *sreu-mn in Greek rheuma, stream, humor of the body: RHEUM. 3. Suffixed zero-grade form *sru-dhmo- in Greek rhuthmos, measure, recurring motion, rhythm: RHYME, RHYTHM.'\"}],\n consulted=[\n  {\"src\": \"POK\", \"where\": \"IEW 1003\", \"stance\": \"supports\",\n   \"note\": \"'gr. ῥέω \\\"flow\\\" … ῥεῦμα n. \\\"Strömen, river; surge\\\" … ῥυθμός, Ionian ῥυσμός … regelmäßige Bewegung, rhythm'.\"},\n  {\"src\": \"KLN\", \"where\": \"1966 s.vv. rheum, rhythm\", \"stance\": \"supports\",\n   \"note\": \"'rheum … fr. Gk. ῥεῦμα, \\\"that which flows; discharge, flux\\\", from the stem of ῥέειν, ῥεῖν, \\\"to flow\\\"'; 'rhythm … fr. Gk. ῥυθμός … formed from the stem of ῥεῖν \\\"to flow\\\"'.\"},\n  {\"src\": \"IEC\", \"where\": \"p.1276 s.v. sreum-\", \"stance\": \"supports\",\n   \"note\": \"'Gk. rheûma, n. \\\"flood, current\\\"' under sreum-.\"}],\n)\n\nN(\n id=12, lang=\"French\", words=\"\", verdict=\"confirmed\",\n derivation=(\n  \"An empty pass-through box: the Greek words reach Persian and (for rhythm) English through French, \"\n  \"the implied forms being rhumatisme (16th c., from Latin rheumatismus < Gk. rheumatismos) and rythme/\"\n  \"rhythme (14th-16th c., from Latin rhythmus < Gk. rhuthmos). French is the correct intermediary for \"\n  \"the Persian words of node #13, which are 19th-20th-century francisms.\"),\n derivation_fa=(\n  \"جعبه‌ای گذرا و بی‌واژه است: واژه‌های یونانی از راه فرانسه به فارسی (و در مورد rhythm به انگلیسی) رسیده‌اند؛ \"\n  \"صورت‌های ضمنی فرانسه rhumatisme (سدهٔ شانزدهم، از لاتینی rheumatismus) و rythme/rhythme (از لاتینی \"\n  \"rhythmus) است. برای واژه‌های فارسی گرهٔ ۱۳ که وام‌واژه‌های فرانسوی سدهٔ سیزدهم و چهاردهم خورشیدی‌اند، \"\n  \"فرانسه واسطهٔ درستی است.\"),\n sources=[ET_RHY, ET_RHE],\n ref_check=[{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Empty pass-through node with no reference of its own.\"}],\n consulted=[\n  {\"src\": \"KLN\", \"where\": \"1966 s.v. rhythm\", \"stance\": \"supports\",\n   \"note\": \"'rhythm, n. — MF. rhythme (F. rythme), fr. L. rhythmus, fr. Gk. ῥυθμός' — Klein routes rhythm through French.\"},\n  {\"src\": \"PHN\", \"where\": \"Pihan, Dict. étym. des mots français…\", \"stance\": \"silent\",\n   \"note\": \"Pihan covers only French words of Arabic/Persian/Turkish origin; rhumatisme and rythme are Graeco-Latin and are absent (grepped rhumatisme/rythme in PHN.txt).\"}],\n)\n\nN(\n id=13, lang=\"Persian\", words=\"româtîsm «روماتیسم»; rîtm «ریتم»\", verdict=\"confirmed\",\n derivation=(\n  \"روماتیسم rumātism and ریتم ritm are modern Persian loans from French rhumatisme and rythme, taken \"\n  \"over during the Qajar/Pahlavi period along with the rest of the medical and musical vocabulary that \"\n  \"came through French-language schooling; the French nasal-free -isme is rendered ـیسم and French /y/ \"\n  \"in rythme is simplified to Persian i. Dehkhoda and Mo'in both tag them 'فرانسوی': «روماتیسم. (فرانسوی، \"\n  \"اِ) بیماری درد مفاصل … (از فرهنگ فارسی معین)» and «ریتم. (فرانسوی، اِ) توالی ضربات آهنگ … (فرهنگ فارسی \"\n  \"معین)». These are the endpoints of the same *srew- chain, re-entering Persian some 2500 years after \"\n  \"رود did — a genuine doublet pair with رود.\"),\n derivation_fa=(\n  \"«روماتیسم» و «ریتم» وام‌واژه‌های نوِ فارسی از فرانسهٔ rhumatisme و rythme‌اند که در دورهٔ قاجار و پهلوی همراه \"\n  \"دیگر واژگان پزشکی و موسیقی از راه آموزش فرانسوی به فارسی درآمدند؛ پسوند -isme فرانسوی «ـیسم» نوشته \"\n  \"شده و واکهٔ /y/ فرانسوی در rythme در فارسی به i ساده شده است. دهخدا و معین هر دو را «(فرانسوی، اِ)» \"\n  \"برچسب زده‌اند: «روماتیسم. (فرانسوی، اِ) بیماری درد مفاصل… (از فرهنگ فارسی معین)» و «ریتم. (فرانسوی، اِ) \"\n  \"توالی ضربات آهنگ… (فرهنگ فارسی معین)». نکتهٔ زیبای این نمودار آن است که این دو واژه و «رود» دوگانه‌اند: \"\n  \"هر دو از یک ریشهٔ هندواروپایی‌اند، یکی میراثی و دیگری وام‌گرفته پس از دو هزار و پانصد سال. ادعای نورایی درست است.\"),\n sources=[AB_ROM, AB_RIT, ET_RHY],\n ref_check=[\n  {\"ref\": \"MON:1693,1701\", \"status\": \"not_checked\",\n   \"note\": \"The 6-vol. print Mo'in (vol. 2, pp.1693 and 1701) is not online and the 2-vol. Adena abridgement on disk lacks both headwords (grepped روماتیسم/ریتم in MON_part1/2.txt). Mo'in's text is however quoted verbatim by abadis.ir, which attributes 'فرانسوی' to فرهنگ فارسی معین for both words — see sources.\"}],\n consulted=[\n  {\"src\": \"MON\", \"where\": \"via abadis.ir s.vv. روماتیسم، ریتم\", \"stance\": \"supports\",\n   \"note\": \"«روماتیسم. (فرانسوی، اِ) … (از فرهنگ فارسی معین)»؛ «ریتم. (فرانسوی، اِ) توالی ضربات آهنگ … (فرهنگ فارسی معین)».\"},\n  {\"src\": \"ARY\", \"where\": \"not applicable\", \"stance\": \"silent\",\n   \"note\": \"Aryanpur's dictionary treats only inherited Indo-European vocabulary of Persian; modern French loans such as روماتیسم/ریتم are not entered.\"}],\n)\n\nN(\n id=14, lang=\"English\", words=\"rheumatism, rhythm\", verdict=\"plausible\",\n derivation=(\n  \"Both words are in AHD under sreu-, and rhythm does come through French: ME/early ModE from MF \"\n  \"rhythme (mod. rythme), from Latin rhythmus, from Gk. rhuthmos (Klein s.v. rhythm). Rheumatism, \"\n  \"however, is not normally routed through French: it is 1601 in English from Latin rheumatismus, \"\n  \"itself from Gk. rheumatismos, the base noun rheum having come via Old French reume in the late 14th \"\n  \"c. Klein prints simply 'rheumatism, n. — L. rheumatismus … fr. Gk. ῥευματισμός', with no French step. \"\n  \"So the node's content is right and the root connection is certain; only the placement of rheumatism \"\n  \"under the French box is loose — hence plausible rather than confirmed.\"),\n derivation_fa=(\n  \"هر دو واژه در پیوست AHD زیر sreu- آمده‌اند و rhythm واقعاً از راه فرانسه به انگلیسی رسیده است: از \"\n  \"فرانسهٔ میانه rhythme، از لاتینی rhythmus، از یونانی rhuthmos (کلاین، ذیل rhythm). اما rheumatism \"\n  \"معمولاً از راه فرانسه نمی‌آید: در سال ۱۶۰۱ میلادی مستقیماً از لاتینی rheumatismus (از یونانی \"\n  \"rheumatismos) وارد انگلیسی شده و تنها واژهٔ پایهٔ rheum در اواخر سدهٔ چهاردهم از فرانسهٔ کهن reume گرفته \"\n  \"شده است؛ کلاین نیز می‌نویسد «rheumatism — L. rheumatismus … fr. Gk. ῥευματισμός» بی هیچ میانجی \"\n  \"فرانسوی. پس محتوای گره درست است و پیوند آن با ریشه قطعی، ولی جای دادن rheumatism زیر جعبهٔ فرانسه \"\n  \"دقیق نیست؛ از این رو «با احتیاط پذیرفتنی».\"),\n sources=[ET_RHE, ET_RHY],\n ref_check=[\n  {\"ref\": \"AHD\", \"status\": \"supports\",\n   \"note\": \"Watkins 1985 s.v. sreu-: 'b. suffixed form *sreu-mn in Greek rheuma, stream, humor of the body: RHEUM'; '3. … Greek rhuthmos …: RHYME, RHYTHM'; the AHD index lists RHEUM and RHYTHM under sreu-.\"}],\n consulted=[\n  {\"src\": \"KLN\", \"where\": \"1966 s.vv. rheum, rheumatic, rheumatism, rhythm\", \"stance\": \"partial\",\n   \"note\": \"'rheum, n. — ME. reume, fr. OF. reume (F. rhume) … fr. L. rheuma, fr. Gk. ῥεῦμα'; 'rheumatism, n. — L. rheumatismus … fr. Gk. ῥευματισμός' (no French step); 'rhythm, n. — MF. rhythme (F. rytme), fr. L. rhythmus' (French step present).\"},\n  {\"src\": \"SKT\", \"where\": \"Skeat s.v. rheum/rhythm\", \"stance\": \"supports\",\n   \"note\": \"Skeat likewise takes both back to Gk. rheîn 'to flow'; cited by Aryanpur ('SKEAT (STREAM) 706') in the same cognate family.\"}],\n)\n\nN(\n id=15, lang=\"Latin\", words=\"\", verdict=\"confirmed\",\n derivation=(\n  \"An empty pass-through box standing for the Latin transmission of the Greek compounds: Late Latin \"\n  \"diarrhoea (< Gk. diarrhoia), Latin haemorrhoidae (< Gk. haimorrhoides), Latin rhythmus (< Gk. \"\n  \"rhuthmos). Latin is the correct intermediary for all three words of node #16, which reached English \"\n  \"in medical and metrical Latin (and, for rhyme, through Old French rime).\"),\n derivation_fa=(\n  \"جعبه‌ای گذرا و بی‌واژه که نمایندهٔ انتقال لاتینی ترکیب‌های یونانی است: لاتینی متأخر diarrhoea (از یونانی \"\n  \"diarrhoia)، لاتینی haemorrhoidae (از یونانی haimorrhoides) و لاتینی rhythmus (از یونانی rhuthmos). \"\n  \"برای هر سه واژهٔ گرهٔ ۱۶ لاتینی میانجی درستی است؛ «rhyme» نیز از همین rhythmus لاتینی از راه فرانسهٔ \"\n  \"کهن rime به انگلیسی رسیده است.\"),\n sources=[ET_RHY],\n ref_check=[{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Empty pass-through node with no reference of its own; covered by the AHD citation on its child #16.\"}],\n consulted=[\n  {\"src\": \"KLN\", \"where\": \"1966 s.v. rhythm\", \"stance\": \"supports\",\n   \"note\": \"'fr. L. rhythmus, fr. Gk. ῥυθμός' — the Latin link Nourai's empty box stands for.\"},\n  {\"src\": \"AHD\", \"where\": \"Watkins s.v. sreu-\", \"stance\": \"supports\",\n   \"note\": \"DIARRHEA and HEMORRHOID are listed under sreu- via Greek rhein, and both reached English through Latin.\"}],\n)\n\nN(\n id=16, lang=\"English\", words=\"diarrhea, hemorrhoid, rhyme\", verdict=\"confirmed\",\n derivation=(\n  \"diarrhea: Gk. diárrhoia 'a flowing through' (dia- + rheîn) > Late Latin diarrhoea > OF diarrie/\"\n  \"diarrhee > ME diaria, 14th c. hemorrhoid: Gk. haimorrhoḯdes (phlébes) 'bleeding (veins)' (haima \"\n  \"'blood' + rhein) > L. haemorrhoidae > OF emorroides > ME emeroudis, 14th c., respelled on the Greek \"\n  \"in the 16th c. rhyme: ME rime, from OF rime 'verse', from Latin rhythmus, from Gk. rhuthmos; the \"\n  \"Germanic word rīm 'number' reinforced it, and the spelling with rh- was imposed c.1600 after the \"\n  \"Latin. All three are listed under sreu- by Watkins, and all three pass through Latin as the chart \"\n  \"shows.\"),\n derivation_fa=(\n  \"diarrhea: یونانی diárrhoia «جاری‌شدن از میان» (dia- + rheîn) ← لاتینی متأخر diarrhoea ← فرانسهٔ کهن \"\n  \"diarrhee ← انگلیسی میانه، سدهٔ چهاردهم. hemorrhoid: یونانی haimorrhoḯdes «رگ‌های خون‌ریز» (haima \"\n  \"«خون» + rhein) ← لاتینی haemorrhoidae ← فرانسهٔ کهن emorroides ← انگلیسی میانه emeroudis، که در \"\n  \"سدهٔ شانزدهم املای یونانی‌اش بازسازی شد. rhyme: انگلیسی میانه rime از فرانسهٔ کهن rime «شعر»، از \"\n  \"لاتینی rhythmus، از یونانی rhuthmos؛ واژهٔ ژرمنی rīm «شمار» آن را تقویت کرده و املای rh- در حدود سال \"\n  \"۱۶۰۰ به تقلید از لاتینی بر آن نشسته است. واتکینز هر سه را زیر sreu- آورده و هر سه از لاتینی گذشته‌اند، \"\n  \"درست همان‌گونه که نمودار نشان می‌دهد. ادعای نورایی درست است.\"),\n sources=[ET_RHY],\n ref_check=[\n  {\"ref\": \"AHD\", \"status\": \"supports\",\n   \"note\": \"Watkins 1985 s.v. sreu-: 'Greek rhein, to flow: RHEO-, -RRHEA; CATARRH, DIARRHEA, HEMORRHOID, RHYOLITE'; '… Greek rhuthmos …: RHYME, RHYTHM'. The AHD index confirms 'DIARRHEA sreu-', 'HEMORRHOID sreu-', 'RHYME sreu-'.\"}],\n consulted=[\n  {\"src\": \"KLN\", \"where\": \"1966 s.v. stream (cross-refs)\", \"stance\": \"supports\",\n   \"note\": \"'Cp. rheo-, rheumatic, rheumatism, rhythm, the first element in rhyolite and the second element in Calirrhoe, catarrh, hemorrhoids, diarrhea, pyorrhea, seborrhea' — Klein's own list of the English words of this family.\"},\n  {\"src\": \"SKT\", \"where\": \"Skeat s.vv. rhyme, diarrhoea\", \"stance\": \"supports\",\n   \"note\": \"Skeat likewise derives rhyme from L. rhythmus < Gk. ῥυθμός and diarrhoea from Gk. διάρροια, both to ῥέω 'flow'.\"}],\n)\n\nN(\n id=17, lang=\"Persian\", words=\"ram «رَم»; ramîdan «رمیدن»\", verdict=\"disputed\",\n derivation=(\n  \"رم ram 'a bolting, taking fright' and رمیدن ramīdan 'to shy, bolt, flee in terror' (present stem رم-) \"\n  \"cannot be derived from *srew- 'to flow'. The modern standard treatment is Cheung, Etymological \"\n  \"Dictionary of the Iranian Verb 312, who sets up a Proto-Iranian root *ram 'to go, move' — MMP/BMP \"\n  \"ahram- 'to lift up, raise', Parthian 'hr'm-, Khotanese t(t)ram-/naram-, NP ramīdan/ram- 'to be \"\n  \"afraid, terrified; to flee in terror', Bal. ram(b)it/ram(b)-, Kurd. rav-/ravin, Gur. rāmā- — and \"\n  \"states flatly: 'No IE etymology can be suggested, it may be a blend of similar roots of motion, e.g. \"\n  \"*Har or *Hran and *gam' (and elsewhere, p.—, 'similar to *ram, whose IE credentials cannot be \"\n  \"established either'). Phonologically the chart's route is impossible anyway: *srew- gives Iranian \"\n  \"*raw-/rau-, which yields rōd, rav-, ravān — never a stem in -m-. The cited page, Mann IEC 1276, \"\n  \"contains sreum-, sreut-, sreuō, srig-, srīǵ-, srin-, srisā, srūbh- and no Persian ram at all. Nourai \"\n  \"has probably been misled by the *sreum-/*Srěm form he put in node #1: a PIE 'sreum-' would indeed \"\n  \"look like a source for ram, but the m there is a suffix, not part of the root. Note also that ram- \"\n  \"must be kept apart from آرمیدن ārāmīdan / رامش rāmiš 'rest, calm' (Cheung's separate root), a \"\n  \"distinction Nourai does not draw.\"),\n derivation_fa=(\n  \"«رَم» و «رمیدن» (ستاک حال: رم-) را نمی‌توان از ریشهٔ *srew- «جاری شدن» گرفت. دیدگاه معیار امروزی از آنِ \"\n  \"چونگ در «فرهنگ ریشه‌شناختی فعل ایرانی» (ص ۳۱۲) است که ریشهٔ ایرانی آغازین *ram «رفتن، حرکت کردن» را \"\n  \"بازسازی می‌کند: فارسی میانهٔ مانوی و کتابی ahram- «برداشتن، بلند کردن»، پارتی ’hr’m-، ختنی t(t)ram-، \"\n  \"فارسی نو رمیدن/رم-، بلوچی ram(b)-، کردی rav-/ravin، گورانی rāmā-؛ و صریح می‌نویسد که «هیچ ریشه‌شناسی \"\n  \"هندواروپایی برای آن نمی‌توان پیشنهاد کرد». از نظر آوایی نیز این مسیر ناممکن است: *srew- در ایرانی به \"\n  \"*raw-/rau- بدل می‌شود و صورت‌هایی چون rōd، رو-، روان می‌دهد، نه ستاکی با m. افزون بر این، صفحه‌ای که \"\n  \"نورایی ارجاع می‌دهد (مان، ص ۱۲۷۶) هیچ مدخل فارسی «رم» ندارد و تنها sreum-، sreut-، sreuō و مانند آن \"\n  \"در آن است. گویا نورایی به سببِ همان صورت ساختگی «Srěm» در گرهٔ نخست به این پیوند رسیده است. باید \"\n  \"«رمیدن» را از «آرمیدن/رامش» (ریشه‌ای جداگانه نزد چونگ) نیز جدا داشت. پژوهش امروزی ادعای نورایی را رد \"\n  \"می‌کند.\"),\n sources=[RAMIDAN],\n ref_check=[\n  {\"ref\": \"IEC:1276\", \"status\": \"not_found\",\n   \"note\": \"Mann IEC p.1276 (IEC.txt leaf 704, printed pp.1276-1277) contains sreum-, sreut-, sreuō, srig-, srīǵ-, srin-, srisā, srūbh- — no Persian ram/ramīdan and no headword that would license this arrow (grepped 'ram' and read the whole leaf).\"}],\n consulted=[\n  {\"src\": \"CHEUNG\", \"where\": \"EDIV p.312 s.v. *ram\", \"stance\": \"contradicts\",\n   \"note\": \"'*ram \\\"to go, move\\\" … *NWIR: NP ramidan/ram- \\\"to be afraid, terrified; to flee in terror\\\" (or Pth. LW *hram- < *θram ?) … No IE etymology can be suggested, it may be a blend of similar roots of motion, e.g. *Har or *Hran and *gam.' PIE/LIV/Pokorny fields are all empty.\"},\n  {\"src\": \"POK\", \"where\": \"IEW 1003 s.v. sreu-\", \"stance\": \"silent\",\n   \"note\": \"Pokorny's sreu- article lists no Iranian m-stem and no Persian ram; the Iranian material is confined to rautah-, raoδah-, raoδaiti, ravan-, urvant-.\"},\n  {\"src\": \"MON\", \"where\": \"s.v. رم\", \"stance\": \"partial\",\n   \"note\": \"«رم (امص.) رمیدن، گریز، نفرت، اکراه» (MON_part1.txt line 68401) — Mo'in gives the meaning but no etymology, i.e. he does not support the *sreu- connection.\"},\n  {\"src\": \"ARY\", \"where\": \"no entry for رمیدن under *sreu-\", \"stance\": \"silent\",\n   \"note\": \"Aryanpur's cognate list for رود (Latin index pdf p.309) contains no Persian رم/رمیدن.\"}],\n)\n\nentry = {\n \"entry\": 0,\n \"root\": \"Ser 1\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *ser- 'to flow' (Pokorny 1. ser- 909; Watkins ser-2), extended as *srew- 'to flow, stream' (Pokorny 1003)\",\n \"note\": (\n  \"Part 2 of the 'Ser 1' chart. The root box is right in every respect: Pokorny's first ser- (IEW \"\n  \"909-910) is glossed 'to flow' and gathers Skt. sisarti/sarati 'flows', sarit- 'river', Gk. hormē, \"\n  \"Lat. serum, and a long list of European river names; Watkins's AHD entry 'ser-2, To flow … [Pok. 1. \"\n  \"ser- 909]' is the same root. The link from *ser- to the *srew- of node #1 is not Nourai's invention \"\n  \"but Pokorny's own closing sentence at 1003, 'Idg. sreu- ist Erw. von ser- \\\"fließen\\\"', repeated by \"\n  \"Klein s.v. stream. Everything in the Iranian column (nodes 2-4, 7) and the European column (9-11, \"\n  \"14-16) checks out against Pokorny, Kent, Horn, Nyberg, Gharib, Buck, Klein and Watkins. The two \"\n  \"weak arrows are #5 (Arabic rawḍa) and #17 (Persian ramīdan); one book misprint (#8 raonami for \"\n  \"raonąm) and one non-existent reconstruction (#1 'Srěm', a garbling of Mann's sreum-) are the \"\n  \"transcription issues. A nice structural point the chart brings out without saying so: رود and \"\n  \"ریتم/روماتیسم are doublets — the same PIE root reaching Persian twice, once by inheritance and once \"\n  \"by a 20th-century loan from French.\"),\n \"note_fa\": (\n  \"بخش دوم نمودار «Ser 1». جعبهٔ ریشه از هر نظر درست است: ریشهٔ نخستِ ser- نزد پوکورنی (ص ۹۰۹-۹۱۰) با \"\n  \"معنای «جاری شدن» آمده و صورت‌هایی چون sisarti/sarati سنسکریت، sarit- «رود»، hormē یونانی و serum \"\n  \"لاتینی و انبوهی از نام رودهای اروپایی را گرد آورده است؛ واتکینز نیز در پیوست AHD همین ریشه را با \"\n  \"ارجاع «[Pok. 1. ser- 909]» آورده. پیوند *ser- به *srew- ساختهٔ نورایی نیست، بلکه جملهٔ پایانی خودِ \"\n  \"پوکورنی در ص ۱۰۰۳ است: «sreu- گسترش‌یافتهٔ ser- است»، و کلاین نیز ذیل stream همین را می‌گوید. همهٔ \"\n  \"ستون ایرانی (گره‌های ۲-۴ و ۷) و ستون اروپایی (۹-۱۱ و ۱۴-۱۶) با پوکورنی، کنت، هرن، نیبرگ، غریب، باک، \"\n  \"کلاین و واتکینز سازگار است. دو پیکان سست نمودار «رَوضه» (گرهٔ ۵) و «رمیدن» (گرهٔ ۱۷) است؛ یک خطای چاپی \"\n  \"کتاب (raonami به جای raonąm در گرهٔ ۸) و یک بازسازی ناموجود («Srěm» در گرهٔ ۱، گشتهٔ sreum- مان) نیز در \"\n  \"کار است. نکتهٔ ساختاری زیبای این صفحه آن است که «رود» و «ریتم/روماتیسم» دوگانه‌اند: یک ریشهٔ هندواروپایی \"\n  \"که دوبار به فارسی رسیده، یک‌بار به میراث و یک‌بار به وام از فرانسه.\"),\n \"sources\": [SREW, RUD],\n \"ref_check\": [\n  {\"ref\": \"POK:909\", \"status\": \"supports\",\n   \"note\": \"Pokorny IEW 909-910: 'Root/lemma: ser-1 (*ker- < *kel-), Meaning: to flow. Material: Old Indic sisarti, sarati \\\"flows, hurries\\\" … Old Indic sarit- \\\"stream, brook, river\\\" … gr. ὁρμή … Lat. serum … References: WP. II 497 f. … in addition sreu- \\\"flow\\\". Page(s): 909-910' (POK_full.txt line 73956 ff.).\"}],\n \"consulted\": [\n  {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. ser-2\", \"stance\": \"supports\",\n   \"note\": \"'ser-2, To flow. 1. Suffixed form *ser-o- in Latin serum, whey: SERAC, SERUM. 2. Basic form *ser- in Sanskrit sarati, sasarti, it flows, it runs: SAMSARA … [Pok. 1. ser- 909; sr-edh- 1001.]'\"},\n  {\"src\": \"WLD\", \"where\": \"Bd. II 497 f., 702 f.\", \"stance\": \"supports\",\n   \"note\": \"Walde-Pokorny II 497 f. is Pokorny's own reference for ser- 'fließen'; II 702 f. gives sreu- with the note 'Idg. sreu- ist Erw. von ser- \\\"fließen\\\"' (WLD_Bd2_pages.txt line 46692).\"},\n  {\"src\": \"KLN\", \"where\": \"1966 s.v. stream\", \"stance\": \"supports\",\n   \"note\": \"'Base *sreu- is an enlargement of base *ser-, whence Gk. ὁρμή \\\"onset\\\", ὀρός \\\"whey\\\", L. serum, \\\"whey\\\". See hormone and serum.'\"},\n  {\"src\": \"IEC\", \"where\": \"Mann, sreuō / sreum- (p.1276)\", \"stance\": \"supports\",\n   \"note\": \"Mann's headwords 'sreuō, io \\\"run, flow\\\"' and 'sreum- \\\"flowing; flow, stream; pour\\\"' with 'WP II, 703'.\"}],\n \"nodes\": nodes,\n}\n\nout = {\n \"pdf_page\": 445,\n \"book_page\": 415,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-13\",\n \"entries\": [entry],\n}\n\n# drop None values\ndef clean(o):\n    if isinstance(o, dict):\n        return {k: clean(v) for k, v in o.items() if v is not None}\n    if isinstance(o, list):\n        return [clean(x) for x in o]\n    return o\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-445.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(clean(out), f, ensure_ascii=False, indent=1)\n    f.write(\"\\n\")\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-445.py",
 "description": "Build page-445.json"
}
```


### [2026-09-14T02:10:02.447Z] TOOL RESULT

```
ok
```


## [2026-09-14T02:10:05.164Z] TOOL CALL #61: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-445.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 445",
 "description": "Validate and run verify_check"
}
```


### [2026-09-14T02:10:06.472Z] TOOL RESULT

```
JSON OK
nodes verified: 17/17
node verdicts: {'plausible': 2, 'confirmed': 12, 'disputed': 2, 'transcription_suspect': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 12, 'partial': 3, 'not_checked': 5, 'not_found': 1}
books consulted: {'supports': 34, 'partial': 7, 'contradicts': 2, 'silent': 6} | by book: {'KLN': 9, 'SYN': 4, 'ARY': 4, 'AHD': 3, 'MON': 3, 'POK': 3, 'SKT': 3, 'WLD': 2, 'IEC': 2, 'NYB': 2, 'HRN': 2, 'FVQ': 2, 'PLA': 2, 'KNT': 1, 'PHD': 1, 'HUB': 1, 'AFM': 1, 'SOD': 1, 'BRT': 1, 'PHN': 1, 'CHEUNG': 1}
```


## [2026-09-14T02:10:26.015Z] AGENT

Page 445 (book p. 415) verified — `data/verification/page-445.json`, `verify_check.py 445` shows 0 PROBLEM lines.

**Counts** — 1 entry, root `confirmed`; nodes 17/17: 12 confirmed, 2 plausible, 2 disputed, 1 transcription_suspect. Ref checks: 12 supports / 3 partial / 1 not_found / 5 not_checked.

**Disputed**
- #5 Arabic `rauza` (رَوْضة) ← Pahlavi rōd: Nourai follows Jeffery FVQ 145-146 (=VDQ:226) faithfully, but Persian *d* would give Arabic د not emphatic ض, the word sits in the productive native root ر و ض (rāḍa, riyāḍ), and Asbaghi PLA:138 — the page Nourai's own NOTE cites — derives it from Persian *raz* (< *raud- "grow"), while recording the *real* loan of rōd as Arabic **rūt** "Fluß" on that same page.
- #17 Persian `ram` / `ramîdan` ← *sreu-: Cheung EDIV 312 sets up Proto-Iranian *ram "to go, move" and says "No IE etymology can be suggested"; *srew- gives Iranian *raw- (rōd, ravān), never an -m- stem. The cited IEC:1276 has no Persian ram at all (`not_found`).

**Transcription_suspect**
- #8 Avestan `raonami`: Pokorny 1003 prints gen. pl. **raonąm** "die Flüsse". `error_in: "book"` — the printed p.415 shows "raonami", so the extraction is faithful; Nourai misread the ą-hook. Page PNG saved to `data/verification/sources/refs/ocr/BOOK/445.png`.

**Other book-side oddity (not flagged as a verdict)**: #1's second form "Srěm : flow, running" is no known reconstruction; the cited IEC:1276 has `sreum-` "flowing; flow, stream; pour", of which "Srěm" is almost certainly a garbling. Node kept at `plausible` (Sreu/Sru confirmed; root→*srew- edge is Pokorny's own words, "Idg. sreu- ist Erw. von ser-").

**Extraction notes for the owner**: none material. One cosmetic gap — the printed chart has a completely **blank** double-ruled box as the child of #8 (right of the Avestan box); it carries no language label and no words, and the JSON omits it. Nothing to fix unless empty boxes are meant to be captured.

**Best confirmations found**: BQT:969 is exactly the رود/رودبار page, and Mo'in's footnote there reads «(رود) پارسی باستان rauta- «بارتولمه»، هندی باستان srotas-… ارمنی rot «هوبشمان»». SOD:346 entry 8600 gives "rwt … <OP rautah-, river" verbatim. Kent's lexicon, Horn §627, Nyberg s.v. rōt, Buck 1.36 and Aryanpur s.v. رود all line up with nodes 2-4/7-11.
