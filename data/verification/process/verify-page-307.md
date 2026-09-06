# Verification process log — verify-page-307


## [2026-09-06T23:06:38.334Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 307 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-307.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-307.json. Write /home/sfmqrb/git/rishe/data/verification/page-307.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 307` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T23:06:40.086Z] AGENT

I'll start by reading the agent instructions.


## [2026-09-06T23:06:40.791Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T23:06:40.808Z] TOOL RESULT

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
226	```json
227	{
228	  "pdf_page": 126,
229	  "book_page": 96,
230	  "verified_by": "claude-opus-5",
231	  "verified_on": "2026-09-05",
232	  "entries": [
233	    {
234	      "entry": 0,
235	      "root": "Dheigh, Dhigha",
236	      "verdict": "confirmed",
237	      "modern_form": "PIE *dʰeyǵʰ- 'to knead, form (clay)'",
238	      "note": "Pokorny 244 dheiĝh-; AHD dheigh-. Root, language label and gloss all correct.",
239	      "note_fa": "ریشهٔ هندواروپایی آغازین *dʰeyǵʰ- «خمیر کردن، شکل دادن (گِل)» … ادعای نورایی درست است.",
240	      "sources": ["https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰeyǵʰ-"],
241	      "ref_check": [{"ref": "POK:244", "status": "supports", "note": "…"}],
242	      "consulted": [{"src": "WLD", "where": "Bd. I 833", "stance": "supports", "note": "…"}],
243	      "nodes": [
244	        {
245	          "id": 6,
246	          "lang": "Avestan",
247	          "words": "pairi-daeza",
248	          "verdict": "confirmed",
249	          "derivation": "Av. pairi-daēza- 'walled enclosure' = pairi 'around' (PIE *per-) + daēza- 'wall' …",
250	          "derivation_fa": "«پردیس» … اوستایی pairi-daēza- «دیوارکشیده، باغِ محصور» از pairi «پیرامون» و daēza- «دیوار» …",
251	          "sources": ["https://en.wiktionary.org/wiki/pairidaēza"],
252	          "ref_check": [{"ref": "POK:244", "status": "supports", "note": "…"}],
253	          "consulted": [{"src": "BRT", "where": "col. 866", "stance": "supports", "note": "…"}]
254	        }
255	      ]
256	    }
257	  ]
258	}
259	```
260	
261	Rules:
262	- Include EVERY node of every non-redirect entry on the page (even empty-word pass-through
263	  nodes like `[Latin] refs=None |` — give them a one-line derivation and a verdict).
264	- `words` = the transliterations of the node joined by "; " (copy from the chart).
265	- `derivation` must be specific: forms, sound changes, dates/eras, texts or peoples,
266	  semantic shifts. 1–5 sentences. No hand-waving like "derived regularly".
267	- Keep `note` on the entry for root-level comments and for anything cross-cutting.
268	- If a node lists several words, cover each word; if they differ in verdict, use the worst
269	  verdict for the node and explain per word in `derivation`.
270	- Where the chart's own NOTE already records a dispute, evaluate it: say which side modern
271	  scholarship takes.
272	- Every node has `ref_check` (array, may contain a single `not_checked` item) AND `consulted`
273	  (array) AND `derivation_fa` (string); every entry has `note_fa`.
274	- Valid JSON only. Test it with `python3 -m json.tool` before finishing, then run
275	  `python3 /home/sfmqrb/git/rishe/tools/verify_check.py <pdf page>` — it must show 0 PROBLEM lines.
276	- When done, reply with a SHORT summary (≤ 15 lines): counts of verdicts per page, and a
277	  bullet per `disputed` / `transcription_suspect` item (root, word, one-line reason), plus
278	  any extraction errors (JSON differs from the printed page) the owner must fix.
279	  Do not paste the JSON back into your reply.
280	
```


## [2026-09-06T23:06:41.183Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-307.txt"
}
```


### [2026-09-06T23:06:41.203Z] TOOL RESULT

```
1	=== PDF page 307 (book page 277) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Leigh 2, Leikw : to leave  (refs POK:669)
4	#1 (parent #0) [Avestan] refs=POK:669; FFD:72; SOD:11 | raexnah, raix, raik, raič, raeč 2 : to leave ; rěxt, rěz, hâek 1 : to pour ; paiti-raeč : avoid, leave ☞Per 3 ; vi-raeč : leave away, run away ☞Wi
5	  #2 (parent #1) [Pahlavi] refs=BQT; HRN:141,203; FVQ:46; SNS:115 | rextan : to pour ; âp-rex : water pot, kettle ☞Ab 1 ; v-rextan : run away ; par-hěxtan, pahrězišn : to avoid
6	    #3 (parent #2) [Persian] refs=POK:669; BQT; AEF:373 | rîxtan «ریختن ( ریز ۱ ، ریزش، آبریز )» : to pour ; gorîxtan «گریختن ( گریز )» : to flee ; parhîxtan «پرهیختن ( پرهیز )» : to avoid
7	    #4 (parent #2) [Arabic] refs=FVQ:46 | 
8	      #5 (parent #4) [Persian] refs=MON:125 | ebrîq «إبریق» : a water or wine container
9	#6 (parent #0) [Latin] refs=AHD | liquěre : to be liquid
10	  #7 (parent #6) [English] refs=None | liquid, liquor
11	#8 (parent #0) [Germanic] refs=AHD | 
12	  #9 (parent #8) [English] refs=None | lend, loan
13	#10 (parent #0) [Germanic] refs=AHD | -lif : left over
14	  #11 (parent #10) [English] refs=None | eleven, twelve
15	#12 (parent #0) [Greek] refs=AHD:413 | ek-leipein : to leave out ; ek-leipsis : cessation (of light)
16	  #13 (parent #12) [Arabic] refs=TAD:63 | kosŭf, xosŭf : eclipse
17	    #14 (parent #13) [Persian] refs=MON:2975 | kosŭf «کسوف ( خسوف )» : eclipse
18	  #15 (parent #12) [Latin] refs=AHD:413 | eclîpsis
19	    #16 (parent #15) [English] refs=AHD:413 | eclipse
20	--- entry 1 ---
21	ROOT Leikw -> redirect to Leigh 2
22	
```


## [2026-09-06T23:06:44.148Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-307.json",
 "description": "Read source JSON page 307"
}
```


### [2026-09-06T23:06:44.190Z] TOOL RESULT

```
{
  "pdf_page": 307,
  "book_page": 277,
  "entries": [
    {
      "root": {
        "name": "Leigh 2, Leikw",
        "lang": "Indo-European",
        "refs": "POK:669",
        "gloss": "to leave"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:669; FFD:72; SOD:11",
          "words": [
            {"translit": "raexnah, raix, raik, raič, raeč 2", "gloss": "to leave", "script": null},
            {"translit": "rěxt, rěz, hâek 1", "gloss": "to pour", "script": null},
            {"translit": "paiti-raeč", "gloss": "avoid, leave", "script": null, "see": ["Per 3"]},
            {"translit": "vi-raeč", "gloss": "leave away, run away", "script": null, "see": ["Wi"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "BQT; HRN:141,203; FVQ:46; SNS:115",
          "words": [
            {"translit": "rextan", "gloss": "to pour", "script": null},
            {"translit": "âp-rex", "gloss": "water pot, kettle", "script": null, "see": ["Ab 1"]},
            {"translit": "v-rextan", "gloss": "run away", "script": null},
            {"translit": "par-hěxtan, pahrězišn", "gloss": "to avoid", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "POK:669; BQT; AEF:373",
          "words": [
            {"translit": "rîxtan", "gloss": "to pour", "script": "ریختن ( ریز ۱ ، ریزش، آبریز )"},
            {"translit": "gorîxtan", "gloss": "to flee", "script": "گریختن ( گریز )"},
            {"translit": "parhîxtan", "gloss": "to avoid", "script": "پرهیختن ( پرهیز )"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 2,
          "lang": "Arabic",
          "refs": "FVQ:46",
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "MON:125",
          "words": [
            {"translit": "ebrîq", "gloss": "a water or wine container", "script": "إبریق"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {"text": "گر بیافزاید می توفیق را - قوّت می بشکند ابریق را", "poet": "Molavî"}
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "liquěre", "gloss": "to be liquid", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "liquid, liquor", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "lend, loan", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "-lif", "gloss": "left over", "script": null}
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
            {"translit": "eleven, twelve", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD:413",
          "words": [
            {"translit": "ek-leipein", "gloss": "to leave out", "script": null},
            {"translit": "ek-leipsis", "gloss": "cessation (of light)", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 12,
          "lang": "Arabic",
          "refs": "TAD:63",
          "words": [
            {"translit": "kosŭf, xosŭf", "gloss": "eclipse", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 13,
          "lang": "Persian",
          "refs": "MON:2975",
          "words": [
            {"translit": "kosŭf", "gloss": "eclipse", "script": "کسوف ( خسوف )"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 12,
          "lang": "Latin",
          "refs": "AHD:413",
          "words": [
            {"translit": "eclîpsis", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 16,
          "parent": 15,
          "lang": "English",
          "refs": "AHD:413",
          "words": [
            {"translit": "eclipse", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Leikw",
        "redirect": "Leigh 2"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-06T23:06:44.876Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-06T23:06:44.917Z] TOOL RESULT

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


## [2026-09-06T23:07:05.028Z] TOOL CALL #5: Bash

```json
{
 "command": "ls data/verification/ | head -30 && python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','FFD','SOD','BQT','HRN','FVQ','SNS','AEF','MON','AHD','TAD']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:600])\n\""
}
```


## [2026-09-06T23:07:05.935Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=669 && NR<=670' POK_full.txt 2>/dev/null | head -60; echo \"=== grep leikʷ\"; grep -n \"leiku̯-\" POK_full.txt | head -20"
}
```


### [2026-09-06T23:07:06.817Z] TOOL RESULT

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
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_
FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/s
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sou
SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt
AEF {"title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence", "kind": "catalog", "url": "https://openlibrary.org/works/OL38785552W (vol. 1, 1356) ; 2015 complete ed. «فرهنگ ریشه‌شناسی فارسی» (مهرافروز) print-only: https://www.gisoom.com/book/11154690/ ; German original: https://archive.org/details/grundrissderneu00horngoog", "lookup_hint": "Not online (searched archive.org, 
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,
TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640", "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; insi
```


### [2026-09-06T23:07:08.650Z] TOOL RESULT

```
=== grep leikʷ
```


## [2026-09-06T23:07:12.015Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in POK_01.txt POK_02.txt POK_03.txt POK_full.txt; do echo \"### $f\"; grep -n \"leiku\" $f | head -10; done"
}
```


## [2026-09-06T23:07:12.676Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"leik\" AHD_watkins1985.txt | head -30"
}
```


### [2026-09-06T23:07:13.929Z] TOOL RESULT

```
### POK_01.txt
### POK_02.txt
### POK_03.txt
### POK_full.txt
56500:Material: Gothic leiku. "body, flesh, corpse ', Old Icelandic IFk^ body, corpse ', Old English
```


### [2026-09-06T23:07:13.968Z] TOOL RESULT

```
328:bheidh-. To persuade, compel, confide. 1. Probably Ger- manic *bidan, to await (< “to await trustingly, expect, trust”), in Old English bidan, to wait, stay: BIDE; ABIDE, (ABODE). 2. Latin fidere, to trust, confide, and fidus, faithful: FIANCE, FIDUCIAL, (FIDUCIARY); AFFIANCE, (AFFIANT), (AFFIDAVIT), (CONFIDANT), CONFIDE, (CONFI- DENT), (DEFIANCE), DEFY, DIFFIDENT. 3. Suffixed o-grade form *bhoidh-es- in Latin foedus (stem foeder-), treaty, league: FEDERAL, FEDERATE; CONFEDERATE. 4. Zero-grade form *bhidh- in Latin fidés, faith, trust: FAITH, FEALTY, FIDELITY; INFIDEL, PERFIDY. [Pok. bheidh- 117.] bheig-. To shine. An uncertain but plausible root. Greek phoibos, shining: PHOEBE, PHOEBUS. [Pok. bheigz- 118.] bhel-'. To shine, flash, burn; shining white and various bright colors. I. 1. Russian byelii, white: BELUGA. 2. Greek phalaros, having a white spot (> phalaris, coot): PHALAROPE. II. 1. Suffixed variant form *bhié-wo- in Germanic *bléwaz, blue, in Old French bleu: BLUE. 2. Suffixed zero-grade form *bhb-wo- in Latin flavus, golden or reddish yellow: FLAVESCENT, FLAVO-; (FLAVIN), (FLAVONE), (FLAVOPROTEIN). III. Various ex- tended Germanic forms. 1. *blaikjan, to make white, in Old English blécan, to bleach: BLEACH. 2. *blaikaz, shining, white, in: a. Old Norse bleikr, shining, white: BLEAK}; b. Old English biéc, bright: BLEAK?. 3. Ger- manic *blikkatjan in Old High German blécchazzen, to flash, lighten (> German Blitz, lightning): BLITZKRIEG. 4. *blas-, shining, white, in: a. Old English blxse, torch, bright fire: BLAZE!; b. Middle Dutch bles, white spot: BLESBOK; C. Old French ble(s)mir, to make pale: BLEM- Ish. 5. *blend-, *bland-, to shine, dazzle, blind, confuse, in: a. Old English blind, blind: BLIND; (BLINDFOLD), (PURBLIND); b. Old High German blentan, to blind, deceive: BLENDE; Gc. Old English blandan, to mingle: BLEND; d. Old French blond; blond: BLOND. 6. *blenk-, *blank-, to shine, dazzle, blind, in: a. Old English blen- can, to deceive: BLENCH!; b. Old French blanc, white: BLANCH, BLANK, BLANKET; BLANCMANGE. 7. *blisk-, to shine, burn, in Old English blyscan, to glow red: BLUSH. IV. Extended form *bhleg-, to shine, flash, burn. 1. Ger- manic *blakaz, burned, in Old English blxc, black: BLACK. 2. Zero-grade form *bhig- in: a. Latin fulgére, to flash, shine: FULGENT, FULGURATE; EFFULGENT, FOU- DROYANT, REFULGENT; b. Latin fulmen (< “fulg-men), lightning, thunderbolt: FULMINATE. 3. a. Latin flagrdre, to blaze: FLAGRANT; CONFLAGRANT, CONFLAGRATION, DEFLAGRATE; b. Latin flamma (< *flag-ma), a flame: FLAMBE, FLAMBEAU, FLAMBOYANT, FLAME, FLAMINGO, FLAMMABLE; INFLAME. 4. Greek phiegein, to burn: PHLEGM, PHLEGMATIC, PHLEGETHON. 5. Greek phlox, a flame, also a wallflower: PHLOGISTON, PHLOX; PHLOGO- PITE. [Pok. 1. bhel- 118, bheleg- 124, bhleu-(k)- 159.] bhel-2. To blow, swell; with derivatives referring to various round objects and to the notion of tumescent masculinity. 1. Zero-grade form *bhl- in Germanic *bul- in: a. Old English bolla (> Middle English boll), pot, bowl: BOLL, BOWL!; b. Old Norse bolr, tree trunk: BOLE}; c. Old Norse bulki, cargo (< “rolled-up load”): BULK}; d. Old High German bolla, ball: ROCAMBOLE; e. Middle High German bole, beam, plank: (BOULEVARD), BUL- WARK; f. Middle Dutch bolle, round object: BOLL; g. Middle Dutch bille, buttock: BILTONG; h. Swedish *buller-, “round object,” in bullersten, “rounded stone,” boulder, akin to the Scandinavian source of English BOULDER; i. possibly obsolete Swedish bulde, a swelling (see wer-1). 2. Suffixed zero-grade form *bhl-n- in: a. Germanic *bulJ6n-, bull, in Old Norse boli, bull: BULL); b. Greek phallos, phallus: PHALLUS; ITHYPHALLIC.
415:in: a. Old English twd, two (nominative feminine and neuter): Two; b. Old English fwégen, two (nominative and accusative masculine): TWAIN. 2. Germanic com- pound *twa-lif-, “two left (over from ten),” twelve (*-if-, left; see leik-), in Old English twelf, twelve, and twelfta, twelfth: TWELFTH, TWELVE. II. Adverbial form *dwis and combining form *dwi-. 1. Germanic *twi- in: a. Old English twi- (> Middle English twi-), two: TWIBIL, TWILIGHT; b. Old High German zwi- (> German zwie-), twice: ZWIEBACK, ZWITTERION. 2. Latin bis (combining form bi-), twice: BI-, BIS; BAROUCHE, BISCUIT. 3. Greek dis (combining form di-), twice: DI-!. 4. Germanic *twis in Middle English twisten, to twist: Twist. 5. Germanic *twiyes in Old English twige, twiga, twice: TWICE. 6. Ger- manic compound *twégentig, “twice ten” (*-tig, ten; see dekm), in Old English twéntig, twenty: TWENTY. 7. Ger- manic *twihna, double thread, twisted thread, in Old English twin, double thread: TWINE. 8. Germanic com- pounds “bi-twihna and *bi-twisk, “at the middle point of two” (*bi, at, by; see ambhi), in Old English betwéonum and betweohs, betwix, between: BETWEEN, BETWIXT, (TWIxT). 9. Germanic compound “twilic-, “two-threaded fabric” in Old English twilic, woven of double thread: TWILL. 10. Suffixed form *dwis-no- in: a. Germanic *twisnaz, double, in Old English twinn, getwinn, two by two, twin: TWIN; b. Latin bini, two by two, two each: BINAL, BINARY; COMBINE. 11. Suffixed form *dwi-ko- in Germanic *twig(g)a, a fork, in Old English twigge, a branch: Twic!. 12. Compound *dwi-plo-, twofold (*-plo-, -fold; see pel-3), in Greek diploos, diplous, twofold: DIPLO-, DIPLOE, DIPLOMA; ANADIPLOSIS. 13. Suffixed reduplicated form *dwi-du-mo- in Greek didumos, dou- ble, the testicles: (DIDYMIUM), DIDYMOUS; EPIDIDYMIS, TETRADYMITE. 14. Suffixed form *dwi-kha in Greek dikha, in two: DICHASIUM, DICHO-. III. Inflected form *duwo. 1. Latin duo, two: DEUCE}, DOZEN, DUAL, DUET, DUO-; DUODECIMAL, 2. Greek duo, dud, two: DUAD, DYAD; DODECAGON, HENDIADYS. IV. Variant form *du-. 1. Compound *du-plo-, twofold (*-plo-, -fold; see pel-%), in Latin duplus, double: DOUBLE, (DOUBLET), (DOU- BLOON), (DOUBLURE), DUPLE. 2. Compound *du-plek- (*-plek-, -fold; see plek-), twofold, in Latin duplex, double: DUPLEX, DUPLICATE, (DUPLICITY); CONDUPLI- CATE. 3. Suffixed form *du-bhw-io- in Latin dubius, doubtful (< “hesitating between two alternatives”), and dubitdre, to be in doubt: DOUBT, DUBIOUS; (REDOUBT- ABLE). [Pok. du6(u)- 228.]
671:extensions in: a. Old English slim, slime: sLIME; b. Old English slipor, slippery: SLIPPERY; Cc. Old English *slice, smooth (> Middle English slike, smooth): sLick; d. Old English lim, cement, birdlime: LIME; e. Old English lam, loam: LOAM; f. Old Norse s/éttr, smooth, sleek, akin to the probable Scandinavian source of Middle English slight, slender: SLIGHT; g. Middle Dutch and Middle Low German slippen, to slip, slip away, akin to the probable source of Middle English slippen, to slip: sL1P!; h. Middle Low German slépen, to drag: SCHLEP. 2. Suffixed form *lei-mo- in Latin limus, slime: LIMACINE, LIMICOLINE. 3. Suffixed form */ei-w- in Latin oblivisci (ob-, away; see epi), to forget (< “to wipe, let slip from the mind”): OBLIVION, OUBLIETTE. 4. Extended form *(sjleia- in: a. nasalized zero-grade form */i-n-a- in Latin linere, to anoint: LINIMENT; b. Suffixed zero-grade form *li- (< *lig-) in Greek litos, plain, simple: LiToTEs. [Pok. 3. lei- 662.] léi-. Also lei-. To flow. 1. Extended form “/eib- in Latin libdre, to pour out, taste: LIBATION; PRELIBATION. 2. Possibly suffixed extended form */eit-os- in Latin litus, shore: LITTORAL. [Pok. 4. lei- 664.] leid-. To play, jest. Suffixed o-grade form *loid-o- in Latin lidus, game, play, with its derivative lidere, to play (but both words may possibly be from Etruscan): LUDICROUS; ALLUDE, COLLUDE, DELUDE, ELUDE, ILLU- SION, INTERLUDE, PRELUDE, PROLUSION. [Pok. leid- 666.] leie-. To waste away. Zero-grade form “li- (< *lia-) in Greek limos, hunger, famine: BULIMIA. [In Pok. 2. lei- 661.] leig-'. To bind. 1. Germanic */ik- in Middle Low German lik, leech line: LEECH?. 2. Zero-grade form */ig-d- in Latin ligare, to bind: LEAGUE!, LEGATO, LIABLE, LIEN, LIGASE, LIGATE; ALLOY, (ALLY), COLLIGATE, COLLIGATIVE, FURL, OBLIGE, (RALLY), RELY. [Pok. 4. leig- 668.] leig-?. Poor. Perhaps Greek oligos, few, little: OLIGO-. [Pok. 1. leig- 667.] leig-5. To leap, tremble. O-grade form */oig- in Germanic *laik- in: a. Old English -lac, suffix denoting activity: WEDLOCK; b. Old Norse leika, to play: LARK?. [Pok. 3. leig- 667.] leigh-. To lick. 1. Greek leikhein, to lick: ELECTUARY. 2. Zero-grade form *lig- in Germanic *likk6n in: a. Old English liccian, to lick: Lick; b. Old French lechier, to live in debauchery: LECHER. 3. Nasalized zero-grade form *ling- in Latin lingere, to lick: ANILINGUS, CUNNI- LinGus. [Pok. leigh- 668.] leikw-, To leave. 1. Basic form *leikv- in Greek leipein, to leave: ECLIPSE, ELLIPSIS. 2. O-grade form *loikv- in: a. Germanic */aihwnjan in Old English lénan, to lend, give (< “to leave to”): LEND; b. suffixed form *loikv-nes- in Germanic */aihwniz in Old Norse Jan, loan: LOAN. 3. Zero-grade form *likv- in Germanic *-lif-, left, in: a. Germanic *ain-lif-, “one (beyond ten),” in Old English endleofan, eleven (see oi-no-); b. Germanic *twa-lif-, “two left (beyond ten),” in Old English twelf, twelve (see dwo-). 4. Nasalized zero-grade form *li-n-kv- in Latin linquere, to leave: DELINQUENT, DERELICT, RELINQUISH. [Pok. leike- 669.] leip-. To stick, adhere; fat. 1. Germanic *libam in Old English Jif, life (< “continuance”): LIFE, LIVELY. 2. Ger- manic “libén in Old English lifian, libban, to live: LIVE}. 3. Germanic */aibjan in Old English léfan, to leave, have remaining: LEAVE!. 4. Germanic “libro in Old English lifer, liver (formerly believed to be the blood-producing organ): LIVER}. 5. Zero-grade form *lip- in Greek lipos, fat: L1po-. 6. Variant form *aleibh- in Greek aleiphein, to anoint with oil (> aleiphar, unguent): ALIPHATIC; SYNA- LEPHA. [Pok. eip- 670.] leis-'. Track, furrow. 1. O-grade form *lois- in: a. Ger- manic */aist- in Old English Jast, lést, sole, footprint: Last’; b. Germanic */laistjan, “to follow a track,” in Old English /éstan, to continue: LAST?; c. suffixed form *lois-G in Germanic */aiz6 in Old English Jar, learning:
795:od-'. To smell. 1. Suffixed form *od-os- in Latin odor, smell: opor. 2. Suffixed form *od-é- in Latin olére, to smell (with J for d representing a Sabine borrowing): OLFACTORY, REDOLENT. 3. Suffixed form *od-yo- in Greek ozein, to smell: OZONE. 4. Suffixed form *od-md- in Greek osmé, smell: OSMATIC, OSMIUM; ANOSMIA. [Pok. 1. od- 72.] od-2. To hate. Latin édi, I hate, and odium, hatred: ANNOY, ENNUI, (NOISOME), ODIUM. [Pok. 2. od- 773.] 6g-. Fruit, berry. 1. Zero-grade form *ag- in Germanic *ak-ran- in Old English zcern, acorn: ACORN. 2. Latin iva (preform uncertain), grape: UVEA, UVULA; PYRUVIC ACID. [Pok. 6g- 773.] oid-. To swell. 1. Possibly Old English date, oat: oat. 2. Greek oidein, to swell: EDEMA. [Pok. oid- 774.] oi-no-. One, unique. I. Basic form *oi-no-. 1. Germanic *ainaz in: a. Old English dn, one: A1, AN!, ONCE, ONE; (ALONE), ANON, (ATONE), (LONE), (LONELY), NONE; b. compound *ain-lif-, “one left (beyond ten),” eleven (*lif-, left over; see leikw-), in Old English endleofan, eleven: ELEVEN; Cc. Old High German ein, one, in Ger- man vereinen, to unite: EINKORN, TURNVEREIN. 2. Latin anus, one: INCH}, OUNCE!, UNCIAL, UNI-, UNION, UNITE, UNITY; COADUNATE, QUINCUNX, TRIUNE, UNANIMOUS, UNICORN, UNIVERSE. 3. Latin ndn, not (< *ne-oinom, “not one thing”; ne, not; see ne). II. Suffixed form *oino-ko- in: a. Germanic *ainigaz in Old English &nig, one, anyone: ANY; b. Latin dnicus, sole, single: UNIQUE. III. Suffixed form *oino-lo- in Latin dllus, any (see ne). [In Pok. e- 281.] oito-. An oath. Probably derived from ei-1. Germanic *aithaz in: a. Old English dth, oath: OATH; b. Old High German eid, oath, in German Eidgenosse, confederate: Hucuenor. [In Pok. 1. ei- 293.] okt6(u). Eight. 1. Germanic *ahté in: a. Old English eahta, eight: EIGHT; b. Old Norse ditjan (tjan, ten; see dekm), eighteen: ATTO-. 2. Latin octé, eight: OcTANS, OCTANT, OCTAVE, OCTAVO, OCTET, OCTO-, OCTOBER, OCTONARY; OCTODECIMO, OCTOGENARIAN. 3. Greek okt6, eight: OcTAD; ocTopus. [Pok. okt6 775.]
862:flad6, flat cake, pancake: FLAN. 4. Germanic nasalized suffixed form *flu-n-th-r-j6- in Old Swedish flundra, flatfish, flounder, probably akin to the Scandinavian source of Middle English flounder, flounder: FLOUNDER?. 5. Nasalized form *pla-n-t- in Latin planta, sole of the foot, and denominative plantdre, to drive in with the sole of the foot, plant, whence planta, a plant: CLAN, PLAN, PLANT, PLANTAIN!, PLANTAR; PLANTIGRADE, SUPPLANT. 6. Suffixed form “plat-u- in Greek platus (feminine plateia), flat, broad: PIAZZA, PLACE, PLAICE, PLANE‘, (PLANE TREE), PLATE, (PLATEAU), (PLATITUDE), (PLATY?), PLATY-, (PLAZA). [Pok. plat- 833.] [plegan. To pledge for, stake, risk, exercise oneself. West Germanic verb. 1. Old English plegian, to exercise one- self, play: PLAY. 2. Late Latin plevium (> Old French plevir, to pledge), pledge, guarantee: PLEDGE; REPLEVIN. 3. Germanic derivative noun *plehti- in Old English pliht, danger, peril: PLIGHT?.] plek-. To plait. Extension of pel-*. 1. Suffixed o-grade form *plok-so- in Germanic *flahsam, flax, in Old Eng- lish fleax, flax: FLAX. 2. Full-grade form *plek- in Latin -plex, -fold (in compounds such as duplex, twofold; and supplex, “with legs folded under one,” kneeling, entreat- ing; see dwo-, upo): MULTIPLEX, QUINTUPLE, SUPPLE. 3. Latin plicdre, to fold (also in compounds used as denominatives of words in -plex, genitive -plicis): PLAIT, PLIANT, PLICA, PLICATE, PLIGHT!, PLISSE, PLY!; APPLY, COMPLICATE, COMPLICE, DEPLOY, DISPLAY, EMPLOY, EXPLICATE, IMPLICATE, REPLICATE, SUPPLICATE. 4. Suf- fixed forms “plek-to- and *plek-t-to- in Latin plectere (past participle plexus), to weave, plait, entwine: PLEACH, PLEXUS; AMPLEXICAUL, COMPLECT, (COMPLEX), PERPLEX. 5. Greek plekein, to plait, twine, and plektos, twisted: PLECOPTERAN, PLECTOGNATH. [Pok. plek- 834.] plék-. Also pleik-. To tear. 1. Zero-grade form *pbk- becoming *plak- in Germanic *flahan in Old English fléan, to strip the skin from: FLAY. 2. Suffixed o-grade form “ploik-sk- perhaps in Germanic “flaiskjan, piece of flesh torn off, in Old English flésc, flesh: FLESH. 3. Zero-grade form *plik- in Germanic *flikkja in: a. Old English flicce, side of a hog: FLITCH; b. Germanic ablaut form *flekkja in Old Norse flekkr, piece of skin or flesh, spot, stain: FLECK. [Pok. plék- 835.] pleu-. To flow. I. Basic form “pleu-. 1. Latin pluere, to rain: (PLOVER), (PLUVIAL), PLUVIOUS. 2. Greek pleusis, sailing: PLEUSTON. 3. Suffixed zero-grade form *plu-elos dissimilated into Greek puelos, trough, basin: PYELITIS. 4. Suffixed form *pl/(e)u-mon-, ‘‘floater,” lung(s), in: a. Latin pulmé (< *plumonés), lung(s): PULMONARY; b. Greek pleumén, pneumon, lung: PNEUMONIA, PNEU- MONIC. 5. Suffixed o-grade form *plou-to- in Greek plou- tos, wealth, riches (< ‘‘overflowing’’): PLUTO; PLUTOCRACY. 6. Lengthened o-grade form *pl6(u)- in: a. Germanic *fléwan, to flow, in (i) Old English flowan, to flow: FLOW (ii) perhaps Middle Dutch vluwe, fishnet: FLUE?; b. suffixed form *pld-tu- in Germanic *fléduz, flowing water, deluge, in Old English fléd, flood: FLOOD. II. Extended form *pleuk-. 1. Germanic *fleugan, to fly, in Old English fléogan, to fly: FLY!. 2. Germanic *fleu- gon-, flying insect, fly, in Old English fléoge, a fly: FLY?. 3. Probably Germanic *fleuhan, to run away, in Old English fléon, to flee: FLEE. 4. Germanic causative *flauhjan in Old English flygan, flégan, to put to flight: FLEY. 5. Germanic suffixed form *fleug-ika in Old French fleche, arrow: FLECHE, FLETCHER. 6. Zero-grade form *pluk- in: a. Germanic *flugja-, feather, in Old English -flycge, with feathers (only in unfligge, featherless): FLEDGE; b. suffixed form *flug-ti- in Old English flyht, act of flying, and *flyht, act of fleeing, escape: FLIGHT, FLIGHT?; Cc. possibly (but unlikely) suffixed form *flug- laz, dissimilated into *fuglaz, bird, in Old English fugol, bird: FowL; d. Germanic suffixed form *flug-ila in Mid- dle High German viiigel (> Germanic Fliigel), wing: FLUGELHORN, FUGLEMAN. III. Extended form *pleud-.
1172:*wer-ald., “life or age of man” (*-ald-, age; see al-3), in Old English weorold, world: woRLD; c. Frankish *wer- wulf, “man-wolf” (*wulf, wolf; see wikvo-), in French garou, werewolf: LOUP-GAROU. 2. Latin vir, man: VI- RAGO, VIRILE, VIRTUE, (VIRTUOSA), (VIRTUOSO); DECEM- VIR, DUUMVIR, TRIUMVIR. 3. Possibly Latin ciria, curia, court, if regarded as from *co-vir, “men together” (co-, together; see kom): CURIA. [Pok. uiro-s 1177.] wleik-. To flow, run. Zero-grade form *wlik-. 1. Adjective *wlik-u-, wet, in: a. suffixed form *wlik-w-d- in Latin liquare, to dissolve: LIQUATE; b. suffixed form *wlik-w-é- in Latin liquére, to be liquid: LIQUESCENT, LIQUID, LIQUOR; DELIQUESCE, LIQUEFY. 2. Suffixed form *wlik-s- in: a. Latin lixa, lye: LIXIVIATE; b. Latin prélixus, poured forth, stretched out in front, extended (pro-, forth; see per’): PROLIX. [In Pok. leiku- 669.] wlkwo-. Wolf. 1. Germanic *wulfaz in: a. Old English wulf, wolf: WOLF; b. Middle Dutch wolf, wulf, wolf: AARDWOLF; Cc. Old High German wolf, wolf, in German Wolfram, tungsten: WOLFRAM; d. Frankish *wulf, wolf (see wi-ro-). 2. Taboo variant */upo- in Latin lupus, wolf: LOBO, LUPINE!, LUPINE?; LOUP-GAROU. 3. Taboo variant *luko- in: a. Greek lukos, wolf: LYCANTHROPE, LYCOPO- piuM; b. Suffixed form */uk’-ya in Greek lussa, martial rage, madness, rabies (“wolf-ness”): LYTTA; ALYSSUM. [Pok. ulkvos 1178.] wip-6-. Fox. 1. Latin vulpés, fox: VULPINE. 2. Taboo variant *slépek- in Greek alépéx, fox: ALOPECIA. [Pok. ulp-, lup- 1179.] wogYh-ni-. Plowshare, wedge. 1. Probably Germanic *wagjaz in Old English wecg, wedge: WEDGE. 2. Prob- ably Latin vdmer, plowshare: vOMER. [Pok. wog¢hni-s 1179.] wokso-. Wax. Related to weg-!. Germanic *wahsam in Old English wex, weax, wax: WAX!. [Pok. uokso- 1180.] wopsa. Wasp. Metathesized form *wospd. 1. Germanic *wosp- in Old English wesp, weps, wasp: wAsP. 2. Latin vespa, wasp: VESPIARY. [Pok. yobhsd 1179.] wos. You (plural). Latin vds (> Old French vous), you: RENDEZVOUS. [In Pok. 1. iu- 513.] wrad-. Branch, root. I. Basic form *wrdd- in Germanic *wrét- in Old Norse rét, root: ROOT!; RUTABAGA. II. Zero-grade form *wred-. 1. Germanic *wurtiz in: a. Old English wyrt, plant, herb: wort; b. German Wurzel (< *wurzwala, rootstock; *-wala, a roll, round stem; see wel-3), root: MANGELWURZEL. 2. Latin rddix, root: RACE3, RADICAL, RADICLE, RADISH, RADIX; DERACI- NATE, ERADICATE. 3. Suffixed form *wrod-mo- in Latin rdmus, branch: RAMOSE, RAMUS; RAMIFY. 4. Suffixed reduced form *wr(e)d-ya perhaps in Greek rhiza, root: RHIZO-, RHIZOME; COLEORHIZA, LICORICE, MYCORRHIZA. [Pok. ufe)rad- 1167.] wragh-. Thorn, tip. Greek rhakhis, ridge, spine: RACHIS. [Pok. 1. uragh- 1180.] wreg-. To push, shove, drive, track down. I. Basic form *wreg- in Germanic *wrekan in: a. Old English wrecan, to drive, expel: WREAK; b. Old Norse rek (older form urek), wreckage, akin to the Scandinavian source of Anglo-Norman wrec, wreck: WRECK. II. O-grade form *wrog-. 1. Germanic *wrakjén-, “pursuer, one pursued,” in: a. Old English wrecca, exile: WRETCH; b. Frankish *wrakjo, “one pursued, an exile,” perhaps in French garce, a girl: GASKET. 2.Germanic *wrakaz in: a. Old English wrzc, exile, punishment, and Middle Dutch wrak, wreckage: WRACK}; b. Swedish rak, wreckage, akin to the source of Middle English rak, mass of driven clouds: RackK®. III. Zero-grade form “wrg-eyo-, “urg-eyo- in Latin urgére, to urge, drive: URGE. [Pok. ureg- 1181.] wrég-. To break. Suffixed form *wrég-nu- in Greek rhégnunai, to burst forth: -RRHAGIA. [Pok. urég- 1181.] [wrod-. Rose. A word (not common Indo-European) of unknown origin. 1. Suffixed form *wrod-o- in Greek rhodon, rose: RHODO-; (RHODIUM). 2. Suffixed form *wrod-ya- (perhaps via Etruscan) in Latin rosa, rose:
1418:DEEP dheub- DEER dheu-! DEFACE dhé-1 DEFAME bha-2 DEFEASANCE dhé-1 DEFEAT dhé-1 DEFECT dhé-1 DEFEND gWhen-1 DEFENSE gWhen-1 DEFER! bher-1 DEFER? bher-1 DEFERVESCENCE bhreu-2 DEFIANCE bheldh- DEFICIENT _dhé-1 DEFILE! pu-2 DEFILE? gWhi- DEFLAGRATE bhel-1 DEFLATE bhlé-2 DEFLOWER bhel-3 DEFOLIATE bhel-3 DEFORCE bhergh-? DEFORM merph- DEFUNCT bheug-2 DEFY bheidh- DEGAGE wadh-1 DEGENERATE geno- DEGLUTINATE gel-1 DEGLUTITION gWel-3 DEGRADE ghredh- DEGREE ghredh- DEGRESSION ghredh- DEGUST geus- DEHISCE ghal- DEICIDE deiw- DEICTIC deik- DEIFIC delw- DEIGN dek-1 DEISM deiw- DEITY deiw- DEJECT yé- DELAINE wele-1 DELAY slég- DELEGATE leg-1 DELIBERATE [ithra DELINQUENT leikw- DELIQUESCE wileik- DELIRIUM leis-1 DELIVER leudh-2 DELL dhel- DELPHINIUM g¥elbh- DELUDE leid- DELUGE leu(@)- DELVE dhelbh- DEMAGOGUE ag-, da- DEMAND man-2 DEMARCATION merg- DEME da- DEMEAN! men-2 DEMEAN2 mei-1
1420:DEODAR deiw-, deru DEONTOLOGY deu-1 DEPEND (s)pen- DEPICT peig-1 DEPILATE pilo- DEPLOY plek- DEPLUME pleus- DEPONE apo- DEPOPULATE populus DEPORT per-2 DEPOSIT apo- DEPRECATE prek- DEPRECIATE per-6 DEPREDATE ghend- DEPRESS per-5 DEPRIVE pert DEPTH dheub- DEPURATE peue- DEPUTE peu- DERACINATE wrad- DERANGE sker-3 DERELICT leikw- DERIVE rei-3 -DERM der-2 DERMA! der-2 DERMA? tera-1 -DERMA der-2 DERMATO- der-2 DEROGATE reg-! DERRIS der-2 DESCANT kan- DESCEND skand- DESCRIBE skribh- DESERTS = ser-3 DESERVE servus DESICCATE selkw- DESIGNATE sekw-1 DESIRE sweid-1 DESIST sta- DESMID dé- DESOLATE s(w)e- DESPAIR spé-1 DESPICABLE spek- DESPISE spek- DESPOIL spel-! DESPOND spend- DESPOT deme-! DESTINE sta- DESTITUTE sta- DESTRIER deks- DESTROY ster-2 DESUETUDE s(w)e- DESULTORY sel-4 DETAIN  ten- DETECT (s)teg- DETENT ten- DETER tres- DETERIORATE de- DETERMINE ter- DETEST trei- DETONATE (s)tene- DETOUR tera-1 DETRACT tragh- DETRIMENT tera-1 DETUMESCENCE teue- DEUCE! dwo- DEUTERAGONIST deu-? DEUTERIUM deu-!
1441:EsLis gWela-1 EBULLIENCE beu-! ECBOLIC gWele-1 ECCENTRIC kent- ECCHYMOSIS gheu- ECCLESIA kela-2 ECCRINE krei- ECEsIsS weik-1 ECHARD segh- ECHELON skand- ECHIDNA ang¥hi- ECHINO- ang¥hi- ECHINUS angVhi- ECHO (s)wagh- ECHOLALIA 1a- ECLAIR kelo-2 ECLAIRISSEMENT kelo-2 ECLAMPSIA [ap- ECLECTIC leg-! ECLIPSE leikw- ECLOSION kleu-3 ECOLOGY weik-1 ECONOMY weik-1 ECRU kreue-1 ECSTASY sta- ECTO- eghs ECTOSARC twerk- ECU skei- ECUMENICAL welk-1 ECZEMA yes- EDACIOUS ed- EDAPHIC sed-! EDDY eti EDELWEISS _athal-, kweit- EDEMA oid- EDENTATE dent- EDGE ak-
1452:ELLIPSIS leikw- ELM el-2 ELOCUTION tolkw- ELODEA sel-es- ELOIGN del-1 ELONGATE del-1 ELOPE klou-
1739:LEAGUER! legh- LEAK leg-2 LEAN! klei- LEAP klou- LEARN leis-1 LEASING leu-! LEAST leis-2 LEATHER letro- LEAVE! leip- LEAVE? §leubh- LEAVEN legWh- LECHER leigh- LECTERN leg-1 LECTION leg-1 LECTURE leg-' LEDGE legh- LEDGER legh- LEE kele-1 LEECH! feg-1 LEECH? leig-1 LEEK leug-! LEER kleu-! LEES legh- LEGACY leg-1 LEGAL leg-1 LEGATE leg-1 LEGATO leig-1 LEGEND leg-1 LEGERDEMAIN leg¥h- LEGIBLE leg-1 LEGION leg-1 LEGISLATOR leg-1, tele- LEGIST leg-1 LEGITIMATE leg-1 LEITMOTIF leit-2 LEMAN leubh- LEMMA! (s)lag¥- LEMMA? lep-t LEMURES_ lem-2 LEND leikw- LENGTH del-1 LENIENT [6-2 LENIS [6-2 LENITIVE |@-2 LENITY 16-2 LENT del-1 LENTO lento-, lep-1. LEPIDO- lep-1 LEPIDOTE lep-1 LEPRECHAUN kWrep-, legwh- -LEPSY (s)lag¥- LEPTO- lep-1 LEPTON! lep-1
1752:LIPO- leip- LIQUATE wileik- LIQUEFY wleik- LIQUESCENT wleik- LIQUID wleik- LIQUOR wileik- LIRA lithra
1758:LIVRE lithra LIXIVIATE wleik- LLANO pele-2
1759:LOAD leit-2 LOAM lei- LOAN leikw-
2136:PRO-2 per? PROBABLE per! PROBE pert PROBITY per! PROBLEM gWele-1 PROBOSCIS g¥6- PROCEED ked- PROCLAIM kele-2 PROcLITIC § klei- PROCLIVITY klei- PROCREATE ker-3 PROCTITIS prdkto- PROCTOLOGY prdkto- PROCTOR cura PROCTOSCOPE prdkto- PROCUMBENT keu-2 PROCURATOR cura PROCURE cura PROCYON kwon- PRODIGAL ag- PRODIGY ég- PRODROME der-1 PRODUCE deuk- PROFANE dhés- PROFESS bha-2 PROFESSOR reg-! PROFFER bher-1 PROFICIENT dhé-1 PROFILE gWhi- PROFIT dhé-1 PROFLIGATE bhiig- PROFOUND bhudh- PROFUSE gheu- PROGENITOR gene- PROGENY gene- PROGLOTTID glégh- PROGNOSIS gnd- PROGRAM gerbh- PROGRESS ghredh- PROHIBIT ghabh- PROJECT yée- PROLAN al-3 PROLAPSE leb-1 PROLATE tele- PROLEGOMENON leg-! PROLEPSIS (s)lag¥- PROLETARIAN al-3 PROLIFEROUS _al-3 PROLIFIC al-3 PROLIX wleik- PROLOCUTOR tolkw- PROLOGUE leg-1 PROLONG del-1 PROLUSION leid- PROMENADE men-2 PROMINENT men-2 PROMISCUOUS meik- PROMISE (s)meit(e)- PROMOTE meue- PROMPT em- PRONE per! PRONEPHROS _ negwh-ro- PRONOUN no-men- PRONOUNCE neu-! PROOF per! PROPAGATE pag- PROPEL pel-6 PROPEND (8)pen- PROPER pert PROPERTY per? PROPHET bha-2 PROPHYLACTIC phulax PROPINQUITY per? PROPIONIC ACID peie- PROPITIOUS pet- PROPOLIS pele-3 PROPORTION pere-2 PROPOSE apo- PROPRIOCEPTION per! PROPRIOCEPTOR per? PROPTOSIS pet- PROPYLAEUM pulé PROPYLON pulé PROROGUE reg-1 PROS- pert PROSCRIBE skribh- PROSE wer-3 PROSECUTE sekw-1 PROSELYTE leudh-1 PROSOMA teue- PROSOPOPEIA kWwel-2, per! PROSPECT spek- PROSPER spé-1 PROSTATE sta- PROSTHESIS dhé-1 PROSTITUTE sta- PROSTOMIUM ste-men-
2178:REIGN reg-! REIMBURSE bursa REINDEER dheu-1, ker-1 REINFORCE bhergh-2 REITERATE i- REJECT yé- REJOICE gau- REJUVENATE yeu- RELAPSE leb-! RELATE tele- RELAX slég- RELAY slég- RELEGATE leg-1 RELENT lento- RELIEVE leg¥h- RELINQUISH leikw- RELUCENT leuk- RELUCT leug-! RELY leig-1 REMAIN men-3 REMAND man-2 REMARK merg- REMEDY med- REMEMBER (s)mer-! REMEX ere-! REMINISCENT men-! REMIT (s)meit(a)- REMORA mere- REMORSE mer-2 REMOTE meue- REMOVE meue- REMUDA mei-1 REMUNERATE mei-! RENAISSANCE gene- REND rendh- RENDER do- _ RENDEZVOUS wOS RENEGADE ne RENEGE ne RENITENT kneigh- RENOUNCE neu-! RENOVATE newo- RENOWN no-men- RENT! do- REPAIR! pere-1 REPAND pete- REPARTEE pere-2 REPAST pa- REPEAT pet- REPEL pel-6 REPENT2 rép-1 REPERTORY pere-! REPINE kWei-1 REPLENISH pele-! REPLETE pele-1 REPLEVIN plegan REPLICATE plek- REPORT per-2 REPOSE! paus- REPOSIT apo- REPREHEND ghend- REPRESENT e@S- REPRESS per-5 REPRIMAND per-5 REPRISAL ghend- REPRISE ghend- REPROACH pert REPROVE per? REPTILE rép-1 REPUBLIC ré- REPUDIATE (s)peud- REPUGN peuk- REPUTE peu-
```


## [2026-09-06T23:07:36.472Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== POK_01 leaf 677 (p.669)\"; awk 'BEGIN{RS=\"\\f\"} NR==677' POK_01.txt | head -80"
}
```


## [2026-09-06T23:07:37.708Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== POK_full linqu\"; grep -n \"linqu\" POK_full.txt | head -10; echo \"=== POK_full 669\"; grep -n \"^669\\|Page 669\\|669\\b\" POK_full.txt | head -5"
}
```


### [2026-09-06T23:07:38.420Z] TOOL RESULT

```
=== POK_01 leaf 677 (p.669)
```


### [2026-09-06T23:07:38.477Z] TOOL RESULT

```
=== POK_full linqu
33138:Material: Avestan grahma- ' sinner, delinquent ' (?); 
54601:Latin linquo, -ere, ITquf to go away, leave, quit, forsake, depart from ' ( Voik^ai, compare 
54992:Material: Gr. aAEirri^ " delinquent', Aeolic aAoiTr|<; " avenger', aAoiToq " delinquent', 
54993:aAiraivEiv " commit an outrage, commit a sin', aAiTrnjojv " sinner, delinquent', aAiTp6(; "ds., 
56806:Material: Gothic lewu. "possibility, opportunity', lewjan^ relinquish, betray ' ("*abandon, 
77004:scaJlid^ lets go, unhands, relinquishes, disperses ' {*skai-l-). Old Irish erscaJliud^ breakup, 
=== POK_full 669
5766:Schuize, Kl. Schr. 669, Schwyzer Gr. Gr. I 632under), adverbal avra ' towards, opposite ', 
6517:placed after Persson Beitr. 669 an Indo Germanic "a/r*- besides *ar9- ahead (compare 
54562:Page(s): 669 
54572:Page(s): 669 
54635:Page(s): 669-670
```


## [2026-09-06T23:07:41.303Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '54540,54660p' POK_full.txt"
}
```


### [2026-09-06T23:07:41.356Z] TOOL RESULT

```
References: WP. II 400 f., WH. I 800 f., Wissmann, Norn, postverb. 183 f., Trautmann 155 

f. 

Page(s): 668 



Root / lemma: lehik-1 {* lehuK} Note: common Proto Germanic -u- > -u-, -y-, -/-. 
Meaning: to prepare for sale 

Material: Latin Heed, -ere^ to be for sale, be priced, be valued ', licet^ it is lawful, is 
allowed, is permitted', liceor, -erV to bid, make a bid ', pollicerr to hold forth, offer, 
promise ', Oscan Ifkftud, licitud^ to be for sale, be priced, be valued '; 

Latvian ITkstu, ITku, /Ikt'get, put, suggest, set, lay, place, bring, order, make, have, 
constrain, compel, possess, oblige, bid, cause, rest, tell, back ', sa/Ikt'ds., put, place, 
assemble ', nuo/Ikums ' pact, covenant'. 

References: WP. II 395, WH. I 797. 
Page(s): 669 

Root/ lemma: lehik-2{*lehuK} Note: common Proto Germanic -u- > -u-, -y-, -/-. 
Meaning: to bend 

Material: S. above S. 309 E {el-8, elehi-, lehi-), wherefore further the Celtic (?) FIN Licus ' 
Lech, River (the name is of Celtic origin), river in the west of Austria, rises south of Rote 
Wand, the highest peak in Vorarlberg ' (Bavaria), Lithuanian FIN /./e/reand Leika, 
Lithuanian //e/r/7a "marshy meadow', Latvian Iiekna6s.; compare lllyrian Ep/-//cus partus, 
FIN Pacco-//cus (Bruttium), mod. FIN Z.//^a(Kroatien). 
Page(s): 669 

Root/ lemma: /eh/k"- {* /ehcik') Note: common Proto Germanic -u- > -u-, -y-, -/-. 

Meaning: to leave 

Grammatical information: imperfect lehik^o, perfective //-/7-Ar"'d (originally athematic); Aor. 3. 

Sg. e-lik^-e, Perf. leh-lohik^-e, participle Perf. lik^o-s 

Material: Old Indie rinaktii^. PI. rincanti) ' leaves, lets go, puts away, gives, grants ', rikta- " 

blank, empty, freely of something ', rfcyate^ wird befreit von etwas, geht verlustig ', reku- 

"unproductive', atireka-m. " remnant, leftover item ', reknas-v\. " inherited possession, 

property ' = Avestan /'5eA'/7a/7- 'blessing, treasure, tribute, inheritance', -irinaxti^ clears up, 

releases ', npers. /"eA-Za/? "diffuse', gurexten 'm'\ss'; 

Armenian /k'anem' allow ', Aor. e//k'= sAins, /k'an/m' will leave, becomes weary, 
exhausted '; 



gr. Aeittu) " allow, leave ', Aoiirot; "residual, remaining', Aiijuavw " allow ', Aiaa(jO|j£v 
eaaojpev Hes. (probably with /; from *link"-id)\ AsTppa n. ' remnant, leftover item ', Asii^javov 
ds.; 

Latin linquo, -ere, ITquf to go away, leave, quit, forsake, depart from ' ( Voik^ai, compare 
Old Indie rireca, gr. AsAoina, and esp. Gothic lailv), relictus^ leave behind ', relicuos 
"residual, remaining'; 

Old Irish /e/c/b'" allows, lets go ', after Strachan (BB. 20, 31) from *link"-, with the 
vocalism of Fut. and Aor. *leik"-s-\ 

Gothic leifvan. Old Icelandic IJa, Old High German IThan, Old English lean " lend ' 
{*leik"d), participle Old Saxon Old High German farliwan^ lend ', Old Icelandic leiga^ rent ', 
Old Icelandic Ian, Old English leen. Old High German lehan^ borrowed property, fief, 
feudal estate, land held on condition of service and loyalty to the feudal lord who granted it 
' ( *laihna- = Old Indie reknas-, compare to /7-forms also Czech liknav^; 

Lithuanian lieku, old //e/r/77/ (reshaped from * link-mi), Infin. Iiktr let, allow ' and " abide, 
remain ', ///r/5S "residual, remaining', liekas^ to leave something [for somebody] ', old " 
eleventh ', palaikas ' residual, leftover, remaining ', laJkas " certain time, time, period ' 
(Latvian /a/i^s "time'), laikau, -///"keep, retain possession of, hold onto the remaining ', 
lykius " rest ', atlykis " work break '; Latvian lieks (= liekas) " supernumerary, excessive, 
spare; phoney '; Old Prussian polTnka^ he remains ', also Old Lithuanian palinkt6s.; 

Old Bulgarian of-blek-b^ remnant, leftover item ' (: Old Indie atireka-), Czech liknovati se' 
refuse, shy, hesitate, flee ', liknavy' negligent ' (see above), with s-forms Old Bulgarian 
Iichi3 " extraordinary, eminent, remarkable, wicked, evil' etc. ( *lik-ch-b, Indo Germanic 
leiq"'so-); lisitrmug, rob'; 

Maybe alb. m. lig, f. //ge" mad, evil'. 

here also Lithuanian vienuo-, dvy-likae\.c. "11, 12' etc. (bis 19), Old Lithuanian liekas^ 
eleventh '; but Gothic ain-, twa-lif. Old High German ein-, zwe-lif\ 1, 12', Old Icelandic 
ellifu. Old Norwegian 3ellugu^\X, 0llykti^Vc\e 1 1 .' etc. are to be put either to either to leip-1 
or according to Marstrander (Eriu 5, 206) borrowed from Celtic *lipi-{*lik"i-). 

References: WP. II 396 f., WH. I 808 f., Trautmann 154 f., Kuiper Nasalpras. 123 f., 179, 
Speeht KZ. 62, 89, 114. 
Page(s): 669-670 



Root / lemma: lehi-2{*lehu-) Note: common Proto Germanic -u- > -u-, -y-, -/-. 

Meaning: to eliminate, dissipate, disappear; weak, thin 

Note: (from *el-ehi^ 

Material: a. Gr. Aivapai i^tuo\xa\ Hes., Aia^opai " bend, incline, go aside, recoil, shrink, 

sink, fall, retired, drew back ', Asipoc; (handschr. Asipcbc;) oioyyoo, Koi U)xp6(; Hes. (= 

Lithuanian leTlas), K\\\bc, m. ' hunger, famine ', Aoi|j6(; ' pestilence, epidemic disease, 

plague '; Aiv6-oapK0(; " with soft, tender body '; 

Middle Irish Ifan {*lei-no-) "gentle'; leinei. "shirt' ("*soft untergarment '); 

Middle High German /v7 "lukewarm, faint, languid'. Old High German LinoPU, nid. lenig 
" ductile ', Old Icelandic Z//?/"" tender, soft, weak'; lina^ relieve, slacken '; 

Gothic af-linnan^ cease, leave, depart ', Old Icelandic linna^cease let, hamper'. Old 
English //nnan' cease', Old High German bi-linnan^ withdraw, cease', with -/7/7-from -nu-\ 
(under the influence of common Celtic -ns-, -nt- > -nn-).
```


## [2026-09-06T23:07:51.500Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== liqueo/liquere in POK_full\"; grep -n -i \"liqueo\\|liquere\\|liquidus\\|u̯leik\\|wleik\\|Meik\" POK_full.txt | head -20; echo; echo \"=== seikw / haek pour\"; grep -n \"seihik\\|Page(s): 893\" POK_full.txt | head"
}
```


### [2026-09-06T23:07:51.569Z] TOOL RESULT

```
=== liqueo/liquere in POK_full
57980:(*meiku) mjeku " doctor. 
58238:Lithuanian miesiu, miesti {*meikid) "mix', Iterat. maisau, maisyti, Latvian maisu, maisTt 
59063:Material: Avestan mairya-^ deceitful, knavish, villainous '; Armenian mei, PI. meik'^ sin '; 
78716:Root / lemma: smei-3, smeid- smeig- smeik- 
78765:with g: Lithuanian s^s/77/z^s "small, crippled '; nisi, smeikr' smooth, shy'; Old English 
78770:a clear meaning "smear, stroke' in Norwegian s/77//ra "stroke, smooth', smeikja^ caress, 

=== seikw / haek pour
72730:Page(s): 893-894 
74576:Page(s): 893
```


## [2026-09-06T23:07:52.267Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT raek\"; grep -n \"raek\\|raēk\\|raexnah\\|rae<\" BRT.txt | head -40"
}
```


### [2026-09-06T23:07:52.322Z] TOOL RESULT

```
=== BRT raek
5285:•  j.  araeka-  Adj.  -  ?  -,  Bez.  einer  Ameisen- art: maoirinqm  'kanam  kutakanqm  duzai- ninqm  V.  74. 5.
9158:—  ks  UKtmSm  (sd.)  cBrM"^  . ,  pu'^nm pure  Y.  44. 7 ;  —  kjrmaomi  "iwam  hacat.- pu^rqm  V.2^.6;  — yat  k^rmaot..  *amar- /an/a  fasu  vira  V.p.  4;  Yt5.  30,  /j.  16 [k^rmavani);  —  matdqmcä  (s,  i  c)  büiricä kjrpsvä  .  .  xrapaitl  (sd.)  Ayat  ahmat  aibi Y.  4n.  I ;  —  yi  umm  pinmm  k?rpnaoiti  . . bantjm.'a  drum  k^rmaoUi  V.  22.5;  uj.^%, Y.  10,13;  —  \hatm  parsam  hami'i''iyam akunaus  Bh.  4.2;  2%  3;  —  ya'ia  asym amasyq  (sd.)  kmnaväni  .  .  karh'qn  Yt. 5.30;  —  ts  k>rmava  mdwaire  ajyamnem V.2.z8;  36  {kirnittol);  — yat  amm  patti.- irist»m  /rä.nastirii  kjnnaaiti  V.  r/,  42;  — armadsth  atiyh  äps  k^nnaoi  Yt.5,78;— >J( Im  firasJmisA.)  *k3rjnaon'^^  ahsm  Y.30.9; Yt.iil.ii  (k^rMavqn),  89  {k»rma7,;li) ;  — yezi  iidit . .  mazdayasna  . .  kahrpsm  kvars.- dar^slm  (sd.)  k:>rmavqn  V.5,14;  13  (wo k^r»nai)t,  statt  Plur,);  —  raeko  (sd.)  mS haca  aühij  s»mat  vatihö  k^rjnaoiii  Yt. iy.2o;  10.2S;  —  ya  *a/r3.ur7'isval  (sd.) hrmavainti  irmi  Yt  13.  z6;  —  I  av<^taiy (^urJ'mazdä  ^mazänam  (sd.)  kunautiro Bh.  4.'6;   —  ava'^  adam  patipadam{%iL)
17419:Zum  V.  raek-,  —  Pü. ;  täk  3  bar  pa  3  baxHhiih (Hds.  ark£t)  pa  3  känakik;  undeutlich.  — : 1)  D.  h.  das  Grundstück  soll  so  gross  sein, ' dass  es  dnich  ÖfTnung  des  oberhalb  gezogenen  j Bewäiserongsgrabens  zweimal  im  Jahr  unter ' Wasser  gesetzt  werden  kann.  1
24726:•  j.  raek-  V.  'linquerc'.  Praes.  8  irinak-, i6  (Des.)  irlrixsa-,  30  (Iter.)  raf'aya-; j-Aor.  I  raixs:  —  PFP.  'riiya-;  Inf. »rixti,  'ri^3;  AbsoL  'irixtfm.
24736:I»  j.  raekah-  n.  'Aufgeben,  Sichzurück- [ziehen  von  — ',  mit  Äaea  und  Abi.:  'i/f ml  haia  arihh  stmal  va?ihs  kirtnaoiti  "er bewirkt,  dass  es  für  mich  besser  ist,  mich von  der  Erde  zurückzuziehen"  VL  j-j.  30". Zum  V. /-flftt-.  —  np.  murda  reg  'Erbschaft'').
25467:KompE.  —  Zum  V.  raek-.
```


## [2026-09-06T23:08:04.275Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"--- raexnah\"; grep -n \"raexn\\|rae.nah\\|raek̥n\" BRT.txt | head -10; echo \"--- pairi/paiti ric\"; grep -n \"paiti\\.ric\\|paiti\\.raek\\|pairi\\.raek\\|paitiric\" BRT.txt | head -10; echo \"--- vi raek\"; grep -n \"vT\\.raek\\|vi\\.raek\\|vT\\.rik\\|vi\\.ric\" BRT.txt | head -10; echo \"--- haek\"; grep -n \"^.\\{0,6\\}haek-\\|haek-  *V\\|hik-\\|haec\" BRT.txt | head -20"
}
```


## [2026-09-06T23:08:04.796Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== CHEUNG raik\"; grep -n \"raik\\|RAIK\\|\\*raič\" CHEUNG.txt | head -30"
}
```


### [2026-09-06T23:08:07.034Z] TOOL RESULT

```
--- raexnah
--- pairi/paiti ric
13165:—  t0it  .  .  ahurS  mazdä  .  .  ai-antanam *paitiricya{sA.)  dai>:e  (3SPM.)  V.5.  60;'— y^  va  möi  ya  gai'^a  dazdi{%%^  *aenaiihl "wer  vorhat  mir  Haus  und  Hof  zu  ver- gewaltigen" Y.46.%;  —  asting  ahmai  yS na  ffjMi"  (sd.)  daidm  (sSOM.)  Y.^ö.  18;
19034:vamaiti  Yt/o.  105;  24*,  48',  139^;  —  h- va^kS  ahmst  syaohmm  vpnzyeiti  . ,  V. 16.  17,  iS.  10,  N.  48;  —  n°  asavantm ainiitiS  (sd.)  Sstäraydti  P.  12;  N.  4,  10, 14,  75,  iS,  30,  55,  log;  —  vTsaiti  dim /rayrarayS  n'  frayrayräyeiti  (Sp.  511  u.) N.  j();  P.  15,  47',  56,  \ti4.37',  V. S.  34,  13.  40,  j(?.  16;  —  «°  ar  ahurS mazdü  ..  *paitiricya  (sA^  daihe  V.5.  60; —  »°  ma^S  gaf^yS  j/?(sd.)  bö/j  janc naoiti..\ti0.ioT,  107,  106; —  n°  ahmäi dc^ai  tat  avat  äyapt?m  Yt.5.  3^'  43'  S9> iiS;  75.21*;  —  «"  ^a«  Jj  vaoze(sA.)  .  . n°  akmät  vaSata  yS  ,  .  P.  4^;  —  «"  ocrd avUrisyät  (als  Praet)  Yt5.63;  —  «-  A? gausbvat*'*  rV  as3m  n°*..Y.4a\ —  n°  täyul n'  hasatgka  bavat*'*  N.  63;  P.  56;  —  n°  him gatvS  vindinti  pasvasca  V.  2,  9;  8  (wo  Wtn- lAfl);  —  nava.Hl  mainyava  yasata  „paiti.- drqm  n'  paitiitqm (sd.)  vjhnii  YtÖ'.3;  V,
19311:3a; —  daevanqm  anSyantqm  ahmaUa  'näi aimäiüi  °tiahe  nmans.palSe  Y.  52,  2 ;  Yt  15. t*;-~fpfvru'^wa,.aora  mainyB kaca  °nat V.  11.10;  — yaoiääta..bun  'na  V. i/.a;  1, 4,  12.2;  —  yat  aiiS  nä yS yaoldi^tyS  hala aHiiyd  'naiiiyö  xshats . .  psrayst  V.g.  39; 40,  13.22;  —  yat . .  aiiqmUt  •»anqm[ca] caratB  dva . .  V.  y.  49 ; — vTspanqm  akmya •ne  nabänasdistanqm  Y.  26'.  7 ;  —  *katämS *naAe*'>  a%auruntm  (sd.)  pärayai  N.  /;  Yt 2.11;  —  t^a.vasatfitha  avi  'tarn  airya- maim  V.  22.  7;  13;  —  tum  . .  sara%uhra *nahe  pourusaspahe'H.  g.\y,  V. /p.  4,  46, Yt  i^.  36;  —  olsmanqmHt  .  ,  vazyäi/  .  . ratsui  'tarn  fränäiayata  A. j.  5:5;  —  us3.- hista  haia  gätvs/rasasa  haca  d^mänSi'-'' Yt  16.2;  —  yavat . .  späna  dt/  hapta  'tia *pairiJ(üahi{sA.)  bavqn  V.J5.4S;  — fratara (sd.)  haca  'na  v>r3syqn  .  .  V.iö.^;  — nistara.naOnal  'nahe  V.  17.  7 ;  6. 43,  g.  33, Yt//.  60;  —  mahsmya  'naÄe  N.yX;  — parepasca  'nahe  V.  y.  45,  46;  45;  —  k»m kfmHl  aipi  'ne  gatu  *saSe  Yt5. 102;  — raocamtn  paiti  'nahe  V.  7. 14;  —  ysi  °nä hqm.6arämahi  .  .  ätnmca  .  .  3at  paslalta ahe  'nahe  spa  vä  na  vä  iriäyäj  .  .  us haca  aHbyS  'naiiby3  baraym  . .  ätnmia  . . ku%a..älr7m  aiti  barqn  ava  aitim  'rum..1 V.5-39-4i;5'33';  —  '""  '»"^^  vfti  vTsi hr3yff  kata  (sd.)  uedat^yan  aetahe  yat iristahe  V.  5.  10;  —  ahe  'nahe  upa.- %'Ui»nsqn  (sÄ)  upa^w3T»tayqn  V,  Ä  10; — yui  .  .  iristim  upaJi?r3%wSJar3m  (sd.) avajtanqn  ava  .  .  iristim  baraytn  avaha 'mm  himaym  upa  .  .  'ntm  baötayqn  . . yezi  . .  *fum  upaJ>jr3%ws.tanm  avaxanqn ava  ..  °n3m  baraytn  V.  4",  af.;  —  ratu- fris  havS  yä  'nahe  *paitiricyehe  (sd.) ^■55-  8)  bes.  im  Gegensatz  zu  Ge- meine, Gau  und  Land*);  'vsa%Pi:^..yS  hu- dänul  damanahya^  xla'hr?m  idßirahya vä  dahySu/  vä  . .  frada%äi  (sd.)  aspfrazats Y.31. 16;  —  3  eJ  'mmf'  vUsm  vä  ist^rtm vä  dahyüm  vä  ädat  dusitäcä  (sd.)  .  ,  Y. ,3/.  18;  —  im  jAw.:  mikrS  .  .  ahmäi frasanäayäti  'tamca  vfs^m^a  zantümca dahyümca  daiiihusasilmca  Yt/o.  87;  18, Y.  62. 5,  V.  Ä  1 03,  N.  6';  —  «5 ..  ahmt  'ne .. aähe  vSse  . .  ahmt  *zantvlf  . .  a^he  da^kvB ftim  vaoSata  . .  ahurpm  P./7;  Y.5.  aS,  Vr, 12.  5,  N.(?;  —  *'nyaca  (LS.)*'  vjsyaca  tarda- vaca  *da^havaca  Vr. /2.  gj  —  yujyastTm haia  *'näp'>  a^a  [. .]  vTsal  ha%r?m  {ha&i)
28177:—  in  auffälliger  Stellung"':  in  Auye/ti(sd.) kS  duiyesti  mqm  zl  mainyete  yasatim  Yt 10. 108.  6)  zl  dient  zur  Hervorhebung des  vorhergehenden  Wortes;  nur  b)  im jAw.:  nöit  zt  ahurB .  .yatikuyanqin  avars- tanqm  *paitiricya  dat^e  V.5. 60;  7. 52, FrW.  Ä  1;  —  ma  Zl  ahmt  nmane../rlm vao.'aia  mqm y'im  ahunm  mazdqm  yaka  . . P.iy;  —  a%a  zl mraoi a/iurS  »lazdä  A.4-3', Vr.  i2. 4',  V.  ;o.  19;—  aXe  zi  väcS . .  aAurd macdä  främraot  zard^uslrai  \.yi.  14;  H. J.4,  V.^49, /J.41,  Yt./4- iz;  —  alvahe zi*ai?mao-jahe ..zaiiu.dräja  asti  s/riti/(sd.) dvayä  ..  V.  JA  11;  4.47, 5.  41,  N.  ö',?;  — mliti  zi  ml  Alm  ..värvniaica  ..^1.$.  iio;
30705:duimüta-,  duiaxla-):  aibigairyä  (sd.)  dathi vispa  kumatäcä  hüxtäcä  't3cä  paitiricyä daikl  vlspä  dmmatacä  duiüxtäeä  dui- varlt3(a  Y. //.  17;  —  frastavattö  huma- taea  huxtala  °taca  niibanmnS  dusmalaca duiüxtaca  duävarstaca  H.  J.  7 ;  —  mä  hra- yqm  vaAUtanam  aiwi^yS  buyata  humata- lieca  mananhs  häxtaheca  vacaahB  'taheca fyad^nake;  "hrayqm  acUianqm  aiwt^yS buyata  dusmatake^a  matiatihs  duiüxtaheca vaianhs  duivarUah^a  syao\  nahe  V.  /A'.  1 7 ;
--- vi raek
--- haek
28650:■haek-
28658:•  j.  'haek- V.  'giessen'.  Praes.  3  hi'a-, 9  hinla-. —  PPfP.  °Aixta-;  Inf.  Aixtayai-ca, •Aincäi;  Absol.  'lalhm.  [S.  noch  "^haf- c<U.aspa-:[
28665:•  j,  'haek-  V.,  nur  mit  us  'exarescere'. Praes.  30  (Kaus.)  ha^aya-  'arefacere'.
28669:•  g.  'haecat.aspa-  m.  EN.  des  vierten Vorfahrens  Zara^uäras,  Nachkommens des  Spitama  im  fünften  Glied.
28671:•  g.  'haecataspa-  patr.  Adj.  von  Haicat.- aspa  abstammend,  dessen  Nachkomme': •pä  (VP.)  vaxsyl  vJ  spUamänAs  "ihr Haecai.asp\Ata,  ich  will  euch  Kunde  geben, ihr  Spitam'iden"  Y.46.15.
```


### [2026-09-06T23:08:07.082Z] TOOL RESULT

```
=== CHEUNG raik
```


## [2026-09-06T23:08:18.026Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls -la CHEUNG.txt && head -40 CHEUNG.txt && echo \"===\" && grep -n -i \"gurēxtan\\|guretan\\|rēxt\\|rext\" CHEUNG.txt | head -20"
}
```


### [2026-09-06T23:08:18.084Z] TOOL RESULT

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
===
12821:wareyz-/warezd ‘to melt [intr.]’ || (+ *pari-) Sh. pireX-/pirext, Rosh. pirix-/pirixt ‘to 
41054:gurextan/gurez-, 307 
41409:rextan/rez-, 187,311 
48017:pirex-/pirext, 188 
48843:rext, 322
```


## [2026-09-06T23:08:18.545Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN leaf 162 (p141)\"; awk 'BEGIN{RS=\"\\f\"} NR==163' HRN.txt | head -60"
}
```


### [2026-09-06T23:08:20.112Z] TOOL RESULT

```
=== HRN leaf 162 (p141)
— 141 —
634. rönäSj röyenäs, röyen *Krapp, Färberröte*.
wa;^. uruddn, sar. aradSn,
Wohl zu aw. raoidita- 'rötlich' (No. 635).
rönäs ist aus röyenäs (im FJ zweifach belegt)
contrahirt; andere von den Wörterbüchern überlieferte
Formen wie roden, rüdeng, röynäs sind unbelegt.
635. (i)röT, rö 'Kupfer, röyln.
aw. raoidita- 'rötlich* (vd. 1, 3); phlv. rödlk geschr.
rötik (vd. 1 (8)), rod bezw. röi (AV.), royin (AV.) ;
skr. lohä'^) 'rötlich, Roterz, Kupfer.
bei. rod 'Kupfer (325).
636. {i)röT, rö 'Gesicht'.
aw. raoSa- 'Wuchs, Ansehen'; phlv. röd"^), hu]rod(i)s7i
(AV.); got. ludja 'Antlitz'.
Allgemein entlehnt im iranischen Gebiet und über
dasselbe hinaus.
637. reht 'Diener, Sklave'.
phlv. rasik.
Wohl zu ap. \/^raS'j np. resTden (No. 016)?
638. reffen 'ausgiessen, verschütten, Praos. rez-em, rPzis,
ni^TI (Qiss. Dan.), reze, vergl. hirezen \Soiho, Durch-
schlag.
g. retmün, Praes. herlfe; Käs. V. retdti.
aw. l/'ra^d-, ra^cayat *Si\isg\essen ; phlv. re//^/w, ircPt
(päz. rezed), rec(i)sfi; lat. liquäre; ai. [/'rcc,-, rindkil
bedeutet nur überlassen, räumen' (vergl. np. gurc/ten,
No. 914); arm. vergl. IKanem 'verlassen' (H. No. 132).
kurd. 7'etin 'ausgiessen'; oss. d. lejtm, t. iJjjn
'laufen, fliehen' (167) ; bei. reöag, n. rTsay (316), vergl.
princag 'pressen, auspressen' (443); wa/. varic-am,
sar. variiz-am 'müde werden , Causat. Verweilen lassen'.
Hierher gehört auch syr. LW. pnjN, arab. LW.
ihrtq 'Wasserkanne' (de Lagarde, Ges. Abb. 7).
*J SpiegePs Erklärung, Ar. Periode 35, ist lautlich pfanz uu-
niüglich.
2j Fiilaoli oder vielmehr nur graphisch rö/, Bund.
```


## [2026-09-06T23:08:29.817Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN p.203 (leaf 224)\"; awk 'BEGIN{RS=\"\\f\"} NR==225' HRN.txt | head -50; echo; echo \"=== HRN no.914 gurextan\"; grep -n \"914\\.\" HRN.txt | head"
}
```


## [2026-09-06T23:08:30.985Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"\\*raik\\|\\*raič\\|raik-\\b\" CHEUNG.txt | head -20; echo \"---\"; grep -n \"^\\*raik\\|RAIK\\|raik \" CHEUNG.txt | head -20"
}
```


### [2026-09-06T23:08:31.404Z] TOOL RESULT

```
=== HRN p.203 (leaf 224)
— 203 —
ap. Varkäna-; aw. cehrka- 'Wolf; phlv. gurg; ai.
vfka- Wolf; arm. gaU (H. No. 62).
kurd. varg *Wolf'; afy. lüg] oss. d. beräyj t. biräy
(60, unsicher) ; bei. gvark, gurk, n. giirß (140) ; yidg.
yter;', yaj'n. aurak,
911. germ Varm*, gerniä 'Wärme', germJ, germis (AM. 54
Zeile 13; 182 Zeile 9).
ap. garma- in Garmalpada-; aw. garema- warm';
phlv. garm^ garmäk, garmth; ai. gharmd- 'Wärmen-
arm. J^rm 'warm', Jermn 'Fieber , jernum *sich erwärmen,
warm werden, erglühen' etc. (H. No. 243).
kurd. bei. (100) garm, bei. garmag (LW. ? 101); afy.
yarma\ oss. d. yarm^ t. yarm (90); siyn. gfarw, sar.
iÄrm, gürm,
912. girevtden glauben* jT^in; (Qiss. Dan., Merx' Archiv,
I, 416, 4).
ap. aw. l/'var- glauben ; phlv. varav(i)stan, mirav{i)sn
(Mün., AV.), päz. garöldan, garöisn, garavisn (AV.).
oss. t. urnjn (262) 'glauben*.
913. gire 'Hals , girebän 'Halsberge' (arab. LW. jirbän,
Jurrubän).
aw. grTva- 'Nacken (des Berges)'; phlv. (aram.) \l^))i
'Hals, Nacken' (Nöldeke, ZDMG. 46, 144), grJvak
'Bergnacken', grtvpän 'Halsberge*; ai. grlvd^ 'Hinter-
hals, Nacken .
afy. griva, greva 'Hals; Halsband'.
914. gureyten 'fliehen , Praes. gurBz-em,
Kauk.-bergjüd. viri/de (!).
skr. vi + i/^reö' (s. No. 638), allerdings nur in der
Bedeutung leer machen , laxiren vorkommend ; doch
vergl. aw. ra^cayeMti (paiti) 'sie verlassen , ai. i^rec-
'räumen, preisgeben', oss. d. lejun , t. iTjin 'laufen,
fliehen' (167); phlv. v(i)rextan.
Eine ältere Bedeutung von np. gure/ten findet sich
wohl bei AM. 237 Zeile 6: 'Also ist das Bedürfniss
nach Wasser grösser als das nach anderen Dingen,
da weder ein Gesunder noch ein Kranker es ent-

=== HRN no.914 gurextan
7915:914. gureyten 'fliehen , Praes. gurBz-em,
12436:giirexten 638, 914.
15232:+ yäi(ia09,914.
17187:v(OrB/tc(n 914.
17981:|/.a^,W»dt/i638,914.
17984:+OT 914.
18822:bgj. viriyde 914.
21195:d. ;4;Mn 638, 914.
21197:t. /f/i« B38, 914.
22757:marka 914.
```


### [2026-09-06T23:08:31.465Z] TOOL RESULT

```
---
```


## [2026-09-06T23:08:45.203Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"pahrēz\\|pahrez\\|parhēz\\|wirēxtan\\|wirextan\" CHEUNG.txt | head -20; echo \"=== index raik region\"; grep -n \"raiH\\|raik\\|rai k\\|ra i k\" CHEUNG.txt | head -20"
}
```


### [2026-09-06T23:08:45.262Z] TOOL RESULT

```
=== index raik region
510:IE meaning can be explained in terms of euphemistic usage, notably *HraiH ‘to 
2620:22 *braiH 
2652:*braiH ‘to shave, shear, cut’ 
6610:*fraiH 87 
6613:*fraiH ‘to rejoice, ? to atone, [med.] please’ 
12809:188 *HraiH 
12825:etymologically connected to *HraiH and it is tempting to regard it as an enlarged 
12826:variant of *HraiH. This enlargement must be a purely Ir. development: °¢ is perhaps 
12840:*HraiH ‘to defecate’ 
28213:*uraiH ‘to crush, push down’ 
28227:© The evidence for an Ir. root *uraiH is limited to Av. An IE provenance cannot be 
28789:446 *xraiH 
28815:*xraiH ‘to buy’ 
55114:*xraiH (s.v.), *xrap! 
55136:*baud' (s.v.), *fraiH (s.v.), 
55231:*čať , *fraiH 
55365:*bauf, *fraiH, *gaHz (s.v.), 
55773:*fraiH (s.v.), *huanH (s.v.), 
55886:*xraiH 
56178:*marH' , *pais, *uraiH,
```


## [2026-09-06T23:08:45.394Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '12800,12900p' CHEUNG.txt"
}
```


### [2026-09-06T23:08:45.440Z] TOOL RESULT

```
*NWIR: Widely attested: NP réxtan/réz- ‘to flow, pour’, Bal. rétk/réc- ‘to pour’, 
Kurd. reZ- ‘to flow, pour (out)’, Zaz. riZiyayis/riZnen- ‘to collapse, disintegrate; to 
flow’, Anar. -irit/ (impv.) iriZ ‘to spill’, Awrom. rezna ‘to pour (tears)’, Fariz. rij-/ 
-rej- ‘to pour; to be thrown on’, Gz. rëZ-/rëZa ‘to flow out, fall off’, (tr.) réZ-/ret, rit, 
Abz. reta/rej-, Abyan. retta/rej-, Ard. réte/rij-, Anar. risaye/ris-, Ham. rijayän (ret-) 
/rij-, Delij. ban. berriji, Nn. rite/rij-, Qohr. rita/rij-, Tr. rita/réj-, Varz. rite/rij- ‘to 


188 *HraiH 


pour (out)’, (caus.) Zaz. riznayis/riZnen- ‘to pour (out), shake out’, Gz. reZn-/reZna 
‘to let flow, pour, fall off, Gur. (Kand.) (ppp.) riziará/-riz- ‘to pour, strew’, Khuns. 
riZ-/rit ‘to scatter, spread’, Jow. bam-ri:t/a-ri:dz-, Meim. bem-ret/a-ri:dz-, Semn. 
ritä-, Shamerz. -rítam-/rizám-, Siv. гіё-, rëš-/ret ‘to pour, strew’, riš-/rešiā ‘to be 
poured, fall over’ (LW ?), Sorkh. dü-rát-/dá-riZ- ‘to pour’. © In many dialects the 
verb has been contaminated with *raiz?. 

*NEIR: Pash. rinjal ‘to have liquid stool’, (inch.-intr.) Yghn. rixs-, rexs- ‘to flow’, ? 
Oss. D. lixsun/lixst ‘to spit’, ? Wa. rox(n) ‘excrements; defecating' || (+ *aua-) Sariq. 
wareyz-/warezd ‘to melt [intr.]’ || (+ *pari-) Sh. pireX-/pirext, Rosh. pirix-/pirixt ‘to 
strew’ || (+ *fra-) Yi. forx-/farxi- ‘to stool’ 

© Exact IE correspondences of this root cannot be found. The root is no doubt 
etymologically connected to *HraiH and it is tempting to regard it as an enlarged 
variant of *HraiH. This enlargement must be a purely Ir. development: °¢ is perhaps 
from *ta£!. 

*PIE — > LIV: – | Pok.: 

*REFERENCES: KPF I: 140b f., 207a; Ivanow 1926: 421; KPF II: 202; Christensen, Contributions I: 164; 
Christensen, Contributions II: 57, 159; Abrahamian 1936: 120; IIFL II: 209a; Lambton 1938: 42a, 77b; 
Morgenstierne 1942: 264; Andreev — PeSéereva: 314b; Abaev, Slovar’ П: 46 Ё; EVS: 61a, 92b; WIM I: 


72; WIM ПЛ. 82; WIM Ш: 115; Safari 1373: 101; Cabolov 1997: 72; Paul 1998: 311b; 
Steblin-Kamenskij 1999: 304; Shahbakhsh: s.v. réc-; Korn 2005: 151, 199, 378 (passim) 


*HraiH ‘to defecate’ 
*AVESTAN: (+ *abi-) Y Av. auui ... irita (ppp.) ‘defecated’ (V 5.1) = Liste: 58 


*MIDDLE PERSIAN: BMP ld- /riy-/ ‘to defecate, void’ 
Pass.: IND. 3sg. BMP Iyt /rid/ 


*KHOTANESE: rrima ‘faeces’, riyai ‘anus’ 

*SOGDIAN: CSogd. rym (m.) “dirt, impurity’ 

*CHORESMIAN: rymyc (pl.) “dirty (spots)’ 

*NWIR: NP ridan/ri-, Bal. rit/ri(y)-, Kurd. ritin/rri-, Siv. rin-/rid ‘to defecate’, NP rim 
“pus, matter, humour; dregs, dross (vel sim.)’, Anar. rix ‘diarrhoea’ 

*NEIR: Oss. І. Iyjyn/lyd, D. ШипЛиа ‘to defecate’, Pash. roma, rima ‘mucus, 
dysentry’ 

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
```


## [2026-09-06T23:08:55.212Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '12750,12805p' CHEUNG.txt"
}
```


### [2026-09-06T23:08:55.256Z] TOOL RESULT

```
*REFERENCES: IIFL II: 534b, 537b; EVS: 21a; Werba 1997: 313 f.; Steblin-Kamenskij 1999: 292, 284 f. 


*(H)raHd ‘to succeed, accomplish’ 


*AVESTAN: räd- ‘to succeed, accomplish’ — Liste: 57 
Aor. athem.: INJ. 15р. ? OAv. radom (Y 29.9), SUBJ. 35р. OAv. radat (Y 51.6, 3р1. OAv. radonti (Y 
33.2); Partic.: perf. pass. Y Av. rasta-. 0 On the interpretation of OAv. radom see Kellens — Part Ш: 30. 


*PARTHIAN: ryst ‘correctly, duly, truly’ = Ghilain: 60 | DMMPP: 304a 
*KHOTANESE: (+ *ati-) tray- (t(t)ras-) ‘to rescue, deliver’ = SGS: 41 

*SANSKRIT: radh ‘to succeed, be successful’ = EWAia П: 448 

*PIE *(H)reH;d" - ‘to succeed in doing something, achieve, accomplish’. © The 
reconstruction of an initial laryngeal is based on the premise that IE roots cannot 
begin with an initial *r-. = LIV: 499 f. | Pok.: 59 f. 

*IE COGNATES: Olrish -ráidi ‘deliberates, says’, Goth. ga-redan ‘to take precautions’, 
Goth. rodjan, NHG reden ‘to talk, speak’ (« *‘to deliberate, premeditate"), ORuss. 


raditi ‘to care for’, OCS ne-raditi ‘to neglect’ 
*REFERENCES: DKS: 143b f.; Werba 1997: 396 f. 


*Hraié ‘to pour, flow’ 

*MIDDLE PERSIAN: MMP ryc- (sic), BMP lyc- /réz-/ ‘to flow; pour’ || (+ *pati-) MMP 
phryz- ‘to flow’ = DMMPP: 304a 

Pres.: IND. 3sg. BMP lycyt /rézéd/, 3pl. MMP rycynd, BMP lycynd /rézénd/; Partic.: perf. pass. MMP 
“ryxt ‘cast (of gold)’, BMP Iyht /réxt/; Inf.: BMP Iyhtn /réxtan/ || (+ *pati-) Pres.: IND. 3sg. MMP 
phryzyd, 3р1. MMP *phryzynd 

*PARTHIAN: ryz- ‘to pour’. On ryz- ‘to fall (of leaves)’ see *raiz’. > Ghilain: 94 | 


DMMPP: 304a, 274b 

Partic.: perf. pass. ryxt 

*SOGDIAN: BSogd. ryz ‘to flow’ || (+ *apa-) SSogd. p’ryc (caus.) ‘to pour (out) 
(SDGM III: 34) || (+ *ui-) CSogd. wyrxs- (inch./pass.) ‘to be poured’ 

Pres.: OPT. 3sg. BSogd. ryz’y (+ *apa-) Caus.: impf. IND. 3sg. SSogd. p’ryc (+ *ui-) Pret.: tr. IND. 3pl. 
CSogd. wry’rnt, Partic.: perf. pass. CSogd. wyrxc’ (Ё) ‘poured’ 


*NWIR: Widely attested: NP réxtan/réz- ‘to flow, pour’, Bal. rétk/réc- ‘to pour’, 
Kurd. reZ- ‘to flow, pour (out)’, Zaz. riZiyayis/riZnen- ‘to collapse, disintegrate; to 
flow’, Anar. -irit/ (impv.) iriZ ‘to spill’, Awrom. rezna ‘to pour (tears)’, Fariz. rij-/ 
-rej- ‘to pour; to be thrown on’, Gz. rëZ-/rëZa ‘to flow out, fall off’, (tr.) réZ-/ret, rit, 
Abz. reta/rej-, Abyan. retta/rej-, Ard. réte/rij-, Anar. risaye/ris-, Ham. rijayän (ret-)
```


## [2026-09-06T23:08:55.927Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"gurextan\\|guréxtan\\|gurēxtan\\|gurext\" CHEUNG.txt | head -20"
}
```


### [2026-09-06T23:08:55.978Z] TOOL RESULT

```
20233:*NWIR: NP ristan ‘to set at liberty, absolve’ || (+ *ui-) NP guréxtan/guréz-, Fariz. 
41054:gurextan/gurez-, 307
```


## [2026-09-06T23:09:02.374Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '20180,20290p' CHEUNG.txt"
}
```


### [2026-09-06T23:09:02.421Z] TOOL RESULT

```
cautiously from *ra- ‘to howl’ + z-enlargement. The z-enlargement from ysär- ‘to 
sing’ ? = SGS: 115 

*BACTRIAN: paC- ‘to call, name’, (раѕѕ.) pi- ‘to be called, be named’ = S-W, Bact.: 
220b 

*NEIR: ? M. raZdn ‘language’ (Gauthiot) 

© The Ir. root may be connected to Gr. Ado«w. The *-z of the Ir. root *raHz would 
have to be explained though: contamination with semantically similar roots ?, cf. 
SGS: l.c. 

«PIE ? *leH5K- ‘to call’ = LIV: 402 | Pok.: 650 


*IE COGNATES: Gr. А&ско “I call’, €AaKov (aor.) ‘I called’ 
*REFERENCES: JIFL II: 245a; Chantraine: 622; DKS: 361b 


*raié ‘to leave, let, abandon’ 

*AVESTAN: Y Av. raec- ‘to leave, let’ || (+ *pati-) ‘to desert’ — Liste: 58 

Pres. n-: IND. 35р. YAv. irinaxti (Yt 10.68); Aor. s-: OPT. med. 25р. YAv. paiti raexsisa (P 40); Caus.: 
pres. IND. 35р. YAv. рай raécaiieiti (V 5.8, Yt 10.41), 3pl. YAv. raecaiieinti (Yt 10.41), INJ. 3sg. ҮАУ. 
raécaiiat (Yt 5.78), SUBJ. 3sg. Y Av. “paiti. raecaiiat (ViD 2), IMPV. 25р. YAv. raécaiia (Yt 5.77); 
Intens.: pres. IND. med. 3sg. ? Y Av. iririxsaite (Y 65.7) 

*MIDDLE PERSIAN: (+ *pati-) MMP phryz- ‘to keep away from, abstain, avoid’ || (+ 
*ш-) MMP wryxt- (pret. stem), BMP wlyc- (‘LYKWN-) /wiréz-/ ‘to flee, run away’. 
© On the interpretation of MMP phryz- see Humbach — Skjarve 1983 II: 86 ff. 
c DMMPP: 346a, 274b 

(+ *pati-) Pres.: IND. 3sg. MMP phryzyd, 3pl. MMP "phryzynd || (+ *ui-) Pres.: IND. 3pl. BMP wlycynd 
/ wirezend/; Partic.: perf. pass. MMP wryxt 

*PARTHIAN: (+ *ш-) wryxs- (orig. inch.) ‘to flee? = Ghilain: 94 | DMMPP: 346a 
Pres.: IMPV. 2р1. “wryxsyd; Partic.: perf. pass. wryxt 

*KHOTANESE: (+ *pari-) OKh. pars- (pars-) ‘to escape’, OKh. parrij- (caus./tr.) ‘to 
deliver, rescue’ || (+ *fra-) hars- ‘to be left, remain’ — SGS: 76, 74, 150 

*SOGDIAN: BSogd. rxm’k, MSogd. rxmyh ‘remains’ (BBB: 34) || (+ *apa-) BSogd. 
prys-, CSogd. prxs- (intr./inch.) ‘to remain, be left || (+ *pari-) BSogd. pr’yc, 
CSogd. pryc, MSogd. pryc (caus.) ‘to leave behind, desert’ 

(+ *apa-) Pres.: IND. 3sg. BSogd. prxsty, MSogd. prxst, MSogd. prxstyy, SUBJ. 3sg. BSogd. prxs't, etc. 
|| (+ *pari-) Widely attested: Pres.: IND. 2sg. SSogd. prycy, BSogd. pr’yc’y, 3sg. BSogd. pr’yct, etc. 
*CHORESMIAN: rycy- ‘to spread out’ || (+ *apa-) pryX- ‘to leave behind’ = Samadi: 
160 

*BACTRIAN: pnyo ‘remains, what is left’ = S-W, Bact.: 221a 

*NWIR: NP ristan ‘to set at liberty, absolve’ || (+ *ui-) NP guréxtan/guréz-, Fariz. 
-wret-/-wrej-, Yar. -wret-/-wrej-, Jow. ba-urut-/a-urud3-, Meim. ba-rveft-/a-iru:ds-, 


308 *raip ? 


Nn. virite/viriss- ‘to run away from, flee’, Sang. -urít-/-uriZaen-, Sorkh. -owrut-/ 
owriZ- ‘to flee’ 

*NEIR: Oss. I. lizyn/lygd, D. lezun/ligd ‘to run away; to abandon a settlement; to 
move to another place, resettle’, Pash. raZedol ‘to cast off, shed, to fall (as leaves)’, 
Sh. (Baj.) ris-/réd, Rosh. rays-/rayd, Bart. ra(y)s-/rid, Sariq. ris-/reyd, Yzgh. raxs-/ 
rayd ‘to remain, be left’, Rosh. raysén-, Sariq. rayzon- ‘to leave behind’, Wa. rac-/ 
rayd- (caus.) ‘to leave’ || (+ *apa-) Pash. päts, paté ‘remaining, left over’ (Cheung 
2004: 129), Yghn. piraxs- (inch.) ‘to stay behind, remain’, Sariq. barézj ‘leavings’ (< 
*apa-raicaka-, EVS, l.c.) || (+ *aua- ?) ? Sariq. (Shaw) wareiz- ‘to be tired’, Wa. 
worac-/woroyn- (woroyd) ‘to remain, be left behind, leave behind’, Yzgh. woraxs- 
/worayd (inch.) ‘to pass (a place, time), outmarch, fall down [of fruit]’, worxan- 
(caus.) ‘to shake down’ || (+ *fra-) ? Sh. f()r(i)xdu ‘remaining, left over’ (LW ?) 
*SANSKRIT: гес ‘to leave, let, release, set free’ (RV+) = EWAia II: 457 f. 

*PIE *leik" “to leave, let? > LIV: 406 f. | Pok.: 669 f. 

*IE COGNATES: Gr. Aeíno, Aur vo ‘I let, leave’, Lat. linguö ‘I leave’, Arm. Ik'anel 
‘to leave’, Lith. liekmi, OPr. po-linka ‘to stay’, Goth. leilvan ‘to lend’ 

*REFERENCES: КРЕТ. 145b; EVP: 65; Christensen, Contributions I: 171 f.; Christensen, Contributions II: 


62, 118; Lambton 1938: 41a, 76b; Abaev, Slovar’ II: 44 f.; EVS: 68a f., 92b, 21a, 34a; DKS: 216b f.; 
Steblin-Kamenskij 1999: 300, 397; Lecoq 2002: 133 


*raip ? ‘to smear’ 

*NEIR: (+ *ui-) Oss. D. ilivd (old ppp.) “pitiful, wretched’ 

*SANSKRIT: rep, lep ‘to smear, attach’ (RV) = EWAia II: 460 

Except for the fossilised Oss. past participle, no certain Ir. cognate forms of Skt. 
rep, lep can be cited: even the Oss. form is semantically not evident. Several Iranian 
forms frequently cited as cognate are probably unconnected: BMP pldp- /fréb-/, NP 
fireb- (fareb-) ‘to deceive’ (< *fra-dab, *dab), Oss. I. felivyn, D. fzelevun ‘to 
deceive; to be unfaithful’ (< Oss. fiel- + I. тууп, D. evun ‘to (ex)change’ < *yaip, 
Cheung 2002: 185). The NP form rév ‘deceit, ruse’ is difficult to assess: Ir. *p can 
hardly yield NP -v in final position, cf. tab ‘fever’, tab ‘glow’ (*tap), x'ab ‘sleep’ 
(*huäp-an-, *huap/f). It cannot be excluded that the NP form is a rhyming word. In 
Persian script rev (,.,) is almost identical with dev (>) ‘devil’. 

«PIE *leip- ‘to stick, be sticky’ — LIV: 405 f. | Pok.: 670 f. 

*IE COGNATES: Gr. Aınatvo ‘I oil’, Aınapog ‘fat, oily’ Lith. тро (lipti) ‘I stick’, 
Russ. lipkij ‘sticky’ 

*REFERENCES: Abaev, Slovar’ I: 543; Werba 1997: 228
```


## [2026-09-06T23:09:32.064Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD rextan/wirextan/pahrez/abrez\"; grep -n \"rēxtan\\|rextan\\|wirēxtan\\|pahrēz\\|pahrez\\|ābrēz\\|abrēz\\|rēz-\" PHD.txt PHD_mackenzie.txt | head -30"
}
```


### [2026-09-06T23:09:32.115Z] TOOL RESULT

```
=== PHD rextan/wirextan/pahrez/abrez
PHD.txt:540:pahikēftan, pahikob- [ptkwp-tn'] strike. pahlawig [*p’hlwbyk' | (M phlwnyg), N paklaw(ān)i] Parthian; Pahlavi. pāhlom [phlwm] excellent, best, foremost. ~ih: excellence. pahlüg [p'Aok! | N pahli] side, rib. pahn [p?An! | N ~] wide, broad. сау [2d | N —à] width, breadth. lpahrextan, pahrēz- [phlyhtn', p'hlyc- | M phryz-, ] ~, N parhéxtan, parhéz-] abstain, refrain, avoid. *pahréxtan, pahrēz- [p’hlyhtn', p'hlyc- | M (phrystn), phryz-] care for, tend, protect. pahréz [Аус | N parhéz] defence, care. *pahrmāh- [ptimwh- | (N parmds-)] touch. ~арфіһ [Pkyh], ~i$n: touch, feeling. pak [DKY A < A аку; рк | = M, N ~] clean, pure, holy. ~ih: purity, holiness. pākīzaģ [p’kyck' | N ~a] pure. palang [ping | N ~] leopard. —-mušk [-mwsk' | N ~] speckled basil. pálüdag [p'Iwtk! | N ~a] starch jelly, flummery. pālūdan, pālāy- [p’lwtn', pPd- | (M p’rwdn, p’r’y-), N ~] strain, filter, purify. pambag [pmbk' | N panba] cotton. —ën [-yn'] (made of) cotton. pānāģ [p’n(’)k' | M p’ng] guard, protector; shepherd. ~th: protection. panāh [рт | = M, N ~] protector; refuge. pad ~ griftan: take refuge with. ~ih: protection. pand [pnd | = M, N ~] path; counsel, advice. panir [pnyl | N ~] cheese. panj [pnc | P рту, (M pnz), N ~] five. ~ag [-k! | N —a] pentad; hand, paw. ~аһ [h | N ~] fifty. panzdah [p’ncdh | M p’nzdh, N ~] fifteen. ірагаб [p?/k! | N para] piece, part, portion. ?párag [p?/k! | M p’rg, N para] gift, offering, bribe. paráhóm [pP?hwm = Av. para.haoma-] consecrated drink (the infusion in holy water of pounded лот and pomegranate twigs, sometimes with milk added). pardag [pitk! | N parda] veil, curtain. pardaxtan, pardaz- [pldhin', pldc- | M prdxt, N ~}, ~ az: be done with, freed of. ^ 6: set about, undertake. ~išn: freedom; undertaking. pardāxtan, pardaz- [pld’htn', pld?c- | N ~] accomplish.
PHD.txt:704:abstain pahrēxtan,
PHD.txt:906:avoid pahrēxtan, wiziristan. avoidable wizirisnig. avoidance ānābišn.
PHD.txt:1159:care (n.) nigāhdār(išn)ih, pahrēz; témár.
PHD.txt:1968:Лее wirēxtan.
PHD.txt:2374:illumination abrēzišn(īh).
PHD.txt:3169:polish abrēxtan.
PHD.txt:3947:tend pahrēxtan.
PHD.txt:4684:pardaz-, parrēz-, (frēb-)
PHD.txt:4689:pardaxtan, parrēxtan
PHD.txt:4760:1 3pahréxtan pahrez l-pahréz- pahlawig pahlüg pahlom pahlomih paygālgar pahast lpüy-
PHD.txt:4951:riyahrīh rextan
PHD.txt:5171:walg wiréxtan wars nargis wircg wircz-! wirēxtan! wircz- waranigih waranig wurróyisn waran
PHD_mackenzie.txt:3983:Ipahrextan, pahrez- [p'hlyhtn , p'hlyc- I M phryz-, J -, N parhextan,
PHD_mackenzie.txt:3986:2pahrextan, pahrez- [p'hlyhtn , p'hlyc- I M (phrystn), phryz-] care for,
PHD_mackenzie.txt:3989:pahrez [p'hlyc I N parhez] defence, care.
PHD_mackenzie.txt:4048:parrextan, parrez- [plyhtn , plyc-] remain over, be superfluous.
PHD_mackenzie.txt:4395:rextan, rez- [lyhtn , lye- I P r)lxt, M ryz-, N ,....,] flow, pour.
PHD_mackenzie.txt:5407:wirextan. wirez- [OLYKWN-tn < A ";(rq; wlyhtn', wlyc-I P wryxt,
PHD_mackenzie.txt:5409:      N gurextan, gurez-] flee, escape.
PHD_mackenzie.txt:5894:abstain pahrextan.                        advice handarz, pando
PHD_mackenzie.txt:5976:as (av.) 6won, 6yon; (cj.) ~e; - if      avoid pahrextan, wiziristan.
PHD_mackenzie.txt:6156:care (n.) nigahdar(isn)ih, pahrez;         tazenidan.
PHD_mackenzie.txt:6158:care for pahrextan.                     chatter (v.) drayidan.
PHD_mackenzie.txt:6362:defence pahrez, piisbiinih; (legal)           wisuftan.
PHD_mackenzie.txt:6497:embers xwarg.                                escape (v.) rastan, wirextan.
PHD_mackenzie.txt:6592:    nihang,oziirak.                        flee wirextan.
PHD_mackenzie.txt:6600:fig anJir.                                 flow (v.) iisixtan, rextan, taxtan,
PHD_mackenzie.txt:7301:planet abaxtar; the 7) planets             pour asixtan, rextan, taxtan, tazen-
PHD_mackenzie.txt:7347:   zot; second officiating""" raspig.          protect padan, pahrextan, srayidan;
```


## [2026-09-06T23:09:33.484Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT raexnah\"; grep -n \"xnah\\|raecnah\" BRT.txt | head -10; echo \"=== NYB\"; grep -n \"rēxtan\\|rextan\\|lyhtn\\|pahrēz\\|wirēxt\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-06T23:09:33.557Z] TOOL RESULT

```
=== BRT raexnah
6592:—  its/i"'  i?  Ad^m  jräid  aiaurune  .  . Yti'ia  ra^aistaraAe  ..\'.ij.44.  4)  mit Instr.  'zusimmea  sein  mit  — ',  sva.  'etwas zu  eigen  haben.  Jemand  zu  eigen  sein'; B)  im  Aw.:  ratUa  ..  ysi  (NDf.)  ,4?« (statt  Du.)  k}krpa  sraista  (ISf.)  *zazäite (Sil.)  Vt.5.34;  —  ujÄ"*  zl  ana  avc u.\'Mi/a  tsdO/a^a^u/..  V./ij.iO.  S)  mit a)  dem  LS,  eines  Nom.  act.'",  b)  einem Absolutiv,  c)  einem  Infinitiv  im  Sinn  von a)  ilal.  'stare  lavorando',  engl,  'to  be labouring',  ß)  (nur  bei  a)  ital.  'esser  in , lavoro'.  a)  LS.  A)  ||  im  Ap.:  «)  ^adakiy aJam  asnaiy  (sd.)  äham  abiy  ''uvajam ".,  1  wastaarching.."Bh.2. 3; — lyaxnahyä mühyS  14  raocabis  'kakatä  (sd.,  auch fdSt.)  <7-4i»*  ". .  stavano  passando"  Bh.  i. \\;  usw.  B)  im  Awr.:  ß)  aisamcTi  ä ahml  >ii>akml  .  .  vTiiiiBi  (sd.)  ai^T  Y.J2. 8.  b)  Absol.  B)  im  Aw.:  yesi  ahi g-if?  ii?r^3m  (sd.)  V.  sr.  5;  — yesi  anhat Hfiirtjin  vn  . .  aiitii.vantim  (sd.)  vä  V.  7. la;  —  ya^a  na  sat>mea  .,  *parsanqm (sd.)  *nijat3m  hyat  YtTj.yi;  —  yezicä ttasui  nar)m  *3stärayantJm  (sd.)  S»h3t'°* V.  1.4;  — yezi  *hisku  hiskväi  sralsyäntTm  i (sä)  ./«Ä<i/">  V.A'.34.  c)  Inf.  B)^im Aw.:  yims  asti  l>pri%e  (sd.)  xi'airayS  V. 1', 7;  —  iJtar/  vSi  (sd.)  masda  ahurahyS^ aAl\.^O.y,  3;  —  iäis  ä  mazda  vlävalsam  \ ^ti'i'i  (sd.)  ahlX. 34.11;  —  kasluscu'n''i\ a.\'iiu/ig  iJi^?(sd.)  auhai  isväcil  fias  paraos\ aks  är?gi'äitlY.47-A>  — y'^a  nS  ankam  1 (3PKPfA.)">    *Jafd  (sd)    manh  Y.&o.iir
24870:Nacht:  xüipJ'vtl  rauta^palwil  "seis  in  der Nacht  oder  am  Tag"  Bh.  /.  7.  b)  als  Be- zeichnung des  Zeitraums  von  Sonnenaufgang bis  Sonnenaufgang:  garmapadahyu  möAy.i I  -cc^  ->akat%  (sd.)  Skc^  Bh.^;.  i;  — viyaxnahya  mshya  14  '!abis  (^s  NP.)  ^a- knt:i  (sd.,  auch  fdSt.)  J^a"  Bh.  /.  11; usw.; —  anäiiiakahya  mähyJ  s  ''t:abis(3.ls NP.  statt  ND.)  :iaial3  (sd.)  äAa'  Bh.  /. 19.11  51  'Licht,  Lichtraum',  der  lichte
=== NYB
2895:pahrée [p’hlyc'] preservation, protection, guard 2611, 291, 12118; ~ kartan to take care of, to cherish 31%, with hac: to preserve from 852-3; rah 61... bim u ~ hac dósax" the way to fear of, and guard from, Hell 8119-11; han i vas- ~ jan well- protected animal spirit (physical life) 553, — From pahrextan.
2897:pahrčxtan [p'hlyhtn'] pahréc- to protect, to take care of^20*; imp. restrain thy- self (be indulgent)! 35°; «"e£, x%és-tan, or alone, ~ hac to be on his guard against, abstain from 6674. 717-12, 8422.26, 851. — Ps. phlysty ‘protected’; MPrs phrystn phryz- ‘to protect, to preserve; to abstain’; NP parhéxtan parhézidan par- héz- ‘to restrain oneself; to take heed’, parhéz ‘abstinence’. Bailey, BSOS VII, 1935, 762 sqq.; Verbum 214 sq. and BBB,
3307:rēcišn [lyešn'] the act of flowing, stream- ing 85??. 867. — V. rextan.
3314:réxtan [lyhtn'] réc- 1. to flow, v. récisn; Mah hac Kaivān u Vahräm rēcēt 6 Ohur- mazd the Moon is proceeding from Saturn and Mars to Jupiter 7" (astrologi- cal). — 2. to pour 108°. — Av. (1479) račk-; MPrth pt. ryxt, MPrs pres. ryz-, both ‘to flow’; Paz. pres. réz-; NP réatan rez- ‘to flow, to pour, to diffuse’. Verbum 177.
4402:xūn-rēcišnēh [-Iyešnyh] bloodshed, blood- bath 131, — V. rēxtan.
5286:raēk-: rēxtan
5288:vi + raēk-: virēxtan
```


## [2026-09-06T23:09:49.550Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FVQ p.46 (leaf 63)\"; awk 'BEGIN{RS=\"\\f\"} NR==64' FVQ_pages.txt | head -60; echo \"=== grep ibriq\"; grep -n -i \"ibriq\\|abariq\\|barîq\\|ābrēz\" FVQ.txt | head -10"
}
```


## [2026-09-06T23:09:50.609Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== TAD p63 grep kusuf\"; grep -n \"كسوف\\|خسوف\\|إبريق\\|ابريق\" TAD.txt | head -20; echo \"=== AFM\"; grep -n \"إبريق\\|ابريق\\|آبريز\" AFM.txt | head -10"
}
```


### [2026-09-06T23:09:51.804Z] TOOL RESULT

```
=== FVQ p.46 (leaf 63)
46 FOREIGN VOCABULARY OF THE QUR'AN
Grundriss, i, 256, would derive *JJ* j from DmSN as jxi from
]tDB7, by assuming a dissimilation form in Aramaic, i.e. D^mHK*.
There is no trace of such a form, however, and Brockclmann's choice
of jUttJLi as illustration is unfortunate as it appears to be a borrowed
word and not original Arabic. The safest solution is that proposed by
Rhodokanakis in WZKM, xvii, 283, and supported by Margoliouth, 1
to the effect that it has been vocalized on the analogy of Isma'll
and Isrd'll. 2 The name was doubtless well enough known in Jewish
circles in pre-Islamic Arabia, 3 and when Muhammad got the form
from Judaeo-Christian sources he formed \A\j?\ on the
same model.
IvilS.
A ewer, or water jug.
Only in the plu. form /! jb I in an early Meccan description of
Paradise. It was early recognized as a Persian loan-word (Siddiqi, 13),
and is given by al-Kindl, Risala, 85 ; ath-Tha f alibi, Fiqh, 317; as-Suy utl 4
and al-Jawaliql 5 in their lists of Persian borrowings, as well as by the
Lexicons, LA, xi, 299 ; TA, vi, 286, though some attempted to explain
it as a genuine Arabic word derived from
In modem Persian the word is j_j\ meaning urn or waterpot.
wirh Lcr.tuir*, p. \'l ; soo also Lidzbarski, JnluinHetbHcli, 7:i ; Fischer,
(Jloxtiar, 163.
2 He says : " Die Form ^j.\ durfto am ehcstcn aus ihrer Anlohiiun^ an J-**-!
und der Ausgleichung mit demselbcn zu erklaron soin, nach dcm hokatinten kur'-
anischen Prinzip, dash Personennaraen, deron Tragcr in irgeiidwoli-hc'iii Kusammen-
hange stehn, lautlich auf oine Form zu bringen wtrebt."
3 Korovitx, KU, 92; JPN. 160.
4 Itq, 318 ; Mutaw, 46 ; Muzhir, i, 136.
"' The text of the Mu'arrab (Saohau's od , p. 17) is defective here, giving the first
U], but not the second. Correcting it by the 7l(j. we read : '111 &J* 0-^ u' ^"1
'^ ^ -ill ^ Cjj.
fi Raghib, 'Mufrndut, 43 ; and see Bagh. on tho passage.
7 Vullcrx, Lex, i, 8. and for further meanings sec RQ, 4 ; Addai Sher, 6. J^jr.l
also occurs in Pers. but only as a borrowing from Arabic.
=== grep ibriq
```


### [2026-09-06T23:09:51.865Z] TOOL RESULT

```
=== TAD p63 grep kusuf
=== AFM
8290:ابريق " 
8634:ابريق ܪ
```


## [2026-09-06T23:10:01.189Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AFM ~8290\"; sed -n '8285,8295p' AFM.txt; echo \"=== AFM 8630\"; sed -n '8628,8640p' AFM.txt"
}
```


### [2026-09-06T23:10:01.241Z] TOOL RESULT

```
=== AFM ~8290


(5١ نمه‎ 


ابريق " 

اخلاد اغاحى ١١6‏ 
ܫܝ ^ 

١5١ ارمغان‎ 
=== AFM 8630

# ي + 
بأسمين ٠١١‏ 
يبان مازومى اه 


ابريق ܪ 
احور مم 
١٠٠١ 1‏ 
ا 
}1115 
ܨܘ | 
11 + ܘ |
```


## [2026-09-06T23:10:02.471Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && wc -l TAD.txt TAD_pages.txt; grep -c $'\\f' TAD_pages.txt; echo \"=== leaf tags\"; grep -n \"pdf page\" TAD_pages.txt | head -5; echo \"=== search ksf\"; grep -n \"كسف\\|كسوف\\|خسف\" TAD_pages.txt | head"
}
```


### [2026-09-06T23:10:04.055Z] TOOL RESULT

```
  3312 TAD.txt
  3117 TAD_pages.txt
  6429 total
85
=== leaf tags
=== search ksf
2430:‫تقممان النوروقدتكسف الشمس لهاولة القمربينهاويين الارض مرادفه احتجي‬
```


## [2026-09-06T23:10:08.871Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2420,2445p' TAD_pages.txt; echo \"=== leaf number\"; head -2430 TAD_pages.txt | grep -c $'\\f'"
}
```


### [2026-09-06T23:10:11.330Z] TOOL RESULT

```
‫م امول المحية غر به‬    ‫استعولبا ابن بطأوطه في رحاته التبورة فى الكلام علي يلاد الك قال‬

                                               ‫يعين مبمله وراء وياع موحدة منتوحات ‪4‬‬
‫فاتدير سموا به وحيد القرن على سبيل المشاعبة أدذمهها ‪:50‬عتاوهاء فراسوه‬
‫وعر وه كروكدحنأييد القرن الهنديويوز أنيكون الاسمفينيقي« قرنإحد»‬
                                                        ‫أي وحيد القرن‬
               ‫كستك وكشتبج فارمبي ‪ 9‬ع ‪ 6‬معناه خبط غليظ‬

‫الوا ‪:‬فاه ونيفاة‬            ‫“كتوفت لعن بوالقين الفولة حمر‬
‫تقممان النوروقدتكسف الشمس لهاولة القمربينهاويين الارض مرادفه احتجي‬
‫"ابح لاتق دءمفادن وهو شجر وف اليونانية «م«ماوةا سمي‬
                                   ‫باسممدينة فى بلاد اليونان مهدا الامبر‬

        ‫"تان حب فارسي « انكشتانه » معناه اصبعي مرادفه فمالخباط‬

  ‫رديبطهة‬
        ‫خمرا‬
           ‫معناهجامكل شيء وال‬        ‫‪ 1-‬ب أرامي‪ 8‬كر‪0‬‬
‫ل المذكور « كناش » فى قالون ان سينا‬        ‫امتكدي يجمم فها رزقه ومن‬
                           ‫وهودقتريكتب فيهالانسان ماينغي أن محنظه‬
                                   ‫تعريب «كاك ‪ 6‬القارسبى‬        ‫“كيك‬

 ‫معناه غطاء عقب الرجل ‪ .‬وجورب‬       ‫كاسات وقاشين ‪ -‬لانيني ‪3‬ع‬

       ‫‪0‬‬            ‫رلارجدلفه لفافة الرجل‬
=== leaf number
66
```


## [2026-09-06T23:10:21.658Z] TOOL CALL #32: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nprint(json.dumps(d['TAD'],ensure_ascii=False,indent=1))\nprint(json.dumps(d.get('MON'),ensure_ascii=False,indent=1)[:2000])\n\""
}
```


### [2026-09-06T23:10:24.029Z] TOOL RESULT

```
{
 "title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640",
 "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; inside.php search works.",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD.txt"
 ],
 "page_offset": "86 leaves (small book, ~80 printed pages); offset ≈ leaf − 4..6, verify against the printed numeral on the page image",
 "covers_etymology": true,
 "notes": "Arabic OCR fair. Nourai's exact edition unknown; the Beirut reprint reproduces the 1932 pagination."
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
 "notes": "covers_etymology = partial: origin-language tag visible online, Latin etyma missing. The a'lam volumes (MON5/MON6 citations, e.g. MON5:528) are NOT online: vajehyab's Mo'in has no proper-name entries (tested افراسیاب — only compounds returned); abadis shows Dehkhoda and 'فرهنگ اسم‌ها' instead, which do give Avestan forms (e.g. Frangrasyan) and can serve as a cross-check
```


## [2026-09-06T23:10:27.916Z] TOOL CALL #33: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py TAD:63 --image 2>&1 | tail -40"
}
```


## [2026-09-06T23:10:29.342Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON abriq\"; grep -n \"ابریق\\|إبریق\\|ابريق\" MON_part1.txt | head -10; echo \"=== MON kosuf\"; grep -n \"کسوف\\|خسوف\" MON_part2.txt MON_part1.txt | head -10"
}
```


### [2026-09-06T23:10:30.039Z] TOOL RESULT

```
no scan of TAD covers printed page 63 (see 'scans' in refs_online.json)
```


### [2026-09-06T23:10:30.106Z] TOOL RESULT

```
=== MON abriq
1324:بدان دست و روی شویند» ابریق؛ مطهره. 
6264:ابریق: ب:۰ [معر. آبریز] (.) ظرف سفالین 
6270:ابریق: بطم [معر . ابری. ابر بز ] (ا.) شمشیر 
20673:ابریقی که از آن در بیاله‌های کو چک شراب 
24795:کوزة شراب ابریق می» صراحی. ظرفی که 
=== MON kosuf
MON_part2.txt:2180:قمر به هنگام خسوف درون آن شود؛ 
MON_part2.txt:23134:کسوف: ۱۰۰0۲(ع.] (مصرل.) (نج.) گرفتن 
MON_part2.txt:23141:ضح.- در لغت عرب « کسوف, به معنی 
MON_part2.txt:23143:در عرف فارسی زبانان « کسوف» در آفتاب 
MON_part2.txt:23144:و ,خسوف» در ماه گوبند. کسوفت جزئی: 
MON_part2.txt:23145:(نج.) گرفتن بخشی از آفتاب؛ مق. کسوف 
MON_part2.txt:23146:کلی. کسوف کلی: (نج.) گرفتن تمام جرم 
MON_part2.txt:31411:تاوان. خسوف» کسوف. جرم» جنایت. 
MON_part2.txt:31422:انساط. کسوف» خضوف. گرفتگی آفتاب 
MON_part2.txt:31423:(خورشید» شمس): کسوف. گرفتگی ماه
```


## [2026-09-06T23:10:37.836Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '23130,23150p' MON_part2.txt; echo \"=== MON abriq ctx\"; sed -n '6260,6275p' MON_part1.txt"
}
```


### [2026-09-06T23:10:37.898Z] TOOL RESULT

```
کسور: 0۹۲ [ع.] )1( ج. کسر. باره‌های 
اعداد مانند نصف. ثلگ. ربع و غیره. 
کمی‌ها» نقصان‌ها. 

کسوف: ۱۰۰0۲(ع.] (مصرل.) (نج.) گرفتن 


کس وکار فرهنگ فارسی معیر ۱۳۹ 


آفتاب. (امص.) (نج.) آفتاب گرفتگی. 
ضح.- در لغت عرب « کسوف, به معنی 
گرفتن آفتاب و گرفتن ماه هر دو آمده ولی 
در عرف فارسی زبانان « کسوف» در آفتاب 
و ,خسوف» در ماه گوبند. کسوفت جزئی: 
(نج.) گرفتن بخشی از آفتاب؛ مق. کسوف 
کلی. کسوف کلی: (نج.) گرفتن تمام جرم 
کس وکار: :۰0-18 (امر.) (عم.) خویش و 
فوم» خویشاوند. 

کسی: ۷2۰ (کس + ی نکره| (مبهم) یک 
=== MON abriq ctx
ابریشم. ابریشم فروش. ابریشم تاب. (.) 
(مستحدث) غلافی از لاستیک و مانند آن 
که برای حفظط از سرابت امراض مقارتی 
دستمال ابر یشم: دستمال یافته از ابر بشم. 
ابریق: ب:۰ [معر. آبریز] (.) ظرف سفالین 
آب. آوند چر مین لوله‌دار که بدان وضو 
سازند» مطهره. ظرف سفالین با گوشه و 
دسته و لوله که بدان طهارت کنند» لولهین. 
آفتانه, مطهر 5 فلز ین. مشربه. وزنی معادل دو 
من. (سد.) گردن عو د؟ ۳ ابار یق. 
ابریق: بطم [معر . ابری. ابر بز ] (ا.) شمشیر 
سار تابان» سمشبر سار درحشند ه» کمان 
درخشان. زن صاحب جمال تابان بدن. 
اوزار» ادات» آلت» وسله» مایه. آنجه برای
```


## [2026-09-06T23:10:38.544Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==67' TAD_pages.txt | head -60"
}
```


### [2026-09-06T23:10:41.112Z] TOOL RESULT

```
‫فاتدير سموا به وحيد القرن على سبيل المشاعبة أدذمهها ‪:50‬عتاوهاء فراسوه‬
‫وعر وه كروكدحنأييد القرن الهنديويوز أنيكون الاسمفينيقي« قرنإحد»‬
                                                        ‫أي وحيد القرن‬
               ‫كستك وكشتبج فارمبي ‪ 9‬ع ‪ 6‬معناه خبط غليظ‬

‫الوا ‪:‬فاه ونيفاة‬            ‫“كتوفت لعن بوالقين الفولة حمر‬
‫تقممان النوروقدتكسف الشمس لهاولة القمربينهاويين الارض مرادفه احتجي‬
‫"ابح لاتق دءمفادن وهو شجر وف اليونانية «م«ماوةا سمي‬
                                   ‫باسممدينة فى بلاد اليونان مهدا الامبر‬

        ‫"تان حب فارسي « انكشتانه » معناه اصبعي مرادفه فمالخباط‬

  ‫رديبطهة‬
        ‫خمرا‬
           ‫معناهجامكل شيء وال‬        ‫‪ 1-‬ب أرامي‪ 8‬كر‪0‬‬
‫ل المذكور « كناش » فى قالون ان سينا‬        ‫امتكدي يجمم فها رزقه ومن‬
                           ‫وهودقتريكتب فيهالانسان ماينغي أن محنظه‬
                                   ‫تعريب «كاك ‪ 6‬القارسبى‬        ‫“كيك‬

 ‫معناه غطاء عقب الرجل ‪ .‬وجورب‬       ‫كاسات وقاشين ‪ -‬لانيني ‪3‬ع‬

       ‫‪0‬‬            ‫رلارجدلفه لفافة الرجل‬
                                        ‫ججوارب فارسيمعناهقبمر ا‬
‫وتالى ‪5‬ه معناه إرث ونصيب واللمراد به كبئةاليعةلان‬           ‫كليرس‬
                                                                ‫لله نصيمهم‬
 ‫كاله د ايطال مده 'مضاة ورقة مدل يتوه ‪:‬مزادفة تنك للامز‬
                                                            ‫والصك والوثيقة‬
                           ‫ونطروي معتاه بدل التقود وصرفبا‬         ‫‪00‬‬
```


## [2026-09-06T23:10:59.190Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && for n in 66 67 68; do curl -sL -o tad_n$n.jpg \"https://archive.org/download/TOB1932ARAR/page/n$n.jpg\" -w \"%{http_code} %{size_download}\\n\"; done; ls -la"
}
```


## [2026-09-06T23:11:01.813Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN eclipse\"; grep -n -i \"^eclipse\\|eclipse, n\\|ekleipsis\" KLN_1966.txt KLN_1971.txt | head -10; echo \"=== KLN liquid\"; grep -n -i \"liquére\\|liquere, to be liquid\\|^liquid\" KLN_1966.txt KLN_1971.txt | head -10; echo \"=== KLN loan/lend/eleven\"; grep -n -i \"^loan\\|^lend\\|^eleven\\|^twelve\" KLN_1966.txt KLN_1971.txt | head -20"
}
```


### [2026-09-06T23:11:10.594Z] TOOL RESULT

```
200 295896
200 304367
200 308480
total 129216
drwx------ 8 sfmqrb sfmqrb    12288 Sep  6 19:11 .
drwx------ 4 sfmqrb sfmqrb     4096 Sep  6 16:32 ..
-rw-rw-r-- 1 sfmqrb sfmqrb   774972 Sep  6 18:54 afm143.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1046357 Sep  6 18:54 afm144.png
-rw-rw-r-- 1 sfmqrb sfmqrb   533122 Sep  6 17:21 afm41_a.png
-rw-rw-r-- 1 sfmqrb sfmqrb   508509 Sep  6 17:21 afm41_b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   969829 Sep  6 17:21 afm41.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1322100 Sep  6 17:20 afm46.png
-rw-rw-r-- 1 sfmqrb sfmqrb   416305 Sep  6 17:20 afm46_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1078 Sep  6 19:10 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  5157031 Sep  6 18:05 aiw.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    26688 Sep  6 18:20 ary377_bot_p294.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71464 Sep  6 18:20 ary377_p294.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71267 Sep  6 18:19 ary378_p294.png
-rw-rw-r-- 1 sfmqrb sfmqrb    25966 Sep  6 18:19 ary378_top_p294.png
-rw-rw-r-- 1 sfmqrb sfmqrb    76489 Sep  6 17:24 bqt1237_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   127656 Sep  6 18:17 bqt1267_foot_p294.png
-rw-rw-r-- 1 sfmqrb sfmqrb   362419 Sep  6 17:50 bqt1583_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   456331 Sep  6 16:54 bqt1594_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   105420 Sep  6 18:16 bqt27.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2824 Sep  6 16:59 bqt83_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb   703015 Sep  6 17:50 bqt_fn4.png
-rw-rw-r-- 1 sfmqrb sfmqrb   299015 Sep  6 17:50 bqt_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb   325427 Sep  6 17:50 bqt_n552.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   315487 Sep  6 17:50 bqt_n553.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   330101 Sep  6 17:50 bqt_n554.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   332775 Sep  6 18:33 bqtv2_289_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   560485 Sep  6 17:53 bqtv2_650_s.png
-rw-rw-r-- 1 sfmqrb sfmqrb   541712 Sep  6 17:53 bqtv2_651_s.png
-rw-rw-r-- 1 sfmqrb sfmqrb     9689 Sep  6 18:33 bqtv2_meta.json
-rw-rw-r-- 1 sfmqrb sfmqrb   726576 Sep  6 18:33 bqtv2_n289.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   729454 Sep  6 17:53 bqtv2_n650.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   702551 Sep  6 17:53 bqtv2_n651.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   100817 Sep  6 17:36 bqt_v3_111.png
-rw-rw-r-- 1 sfmqrb sfmqrb   110820 Sep  6 17:36 bqt_v3_112.png
-rw-rw-r-- 1 sfmqrb sfmqrb    91526 Sep  6 16:59 bqt_v3_83.png
-rw-rw-r-- 1 sfmqrb sfmqrb   137595 Sep  6 18:10 buck2.txt
-rw-rw-r-- 1 sfmqrb sfmqrb      146 Sep  6 18:10 buck3.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    64531 Sep  6 16:53 build261.py
-rw-rw-r-- 1 sfmqrb sfmqrb    60498 Sep  6 17:11 build269.py
-rw-rw-r-- 1 sfmqrb sfmqrb    97300 Sep  6 17:16 build270.py
-rw-rw-r-- 1 sfmqrb sfmqrb    52615 Sep  6 17:36 build275.py
-rw-rw-r-- 1 sfmqrb sfmqrb    74145 Sep  6 17:43 build278.py
-rw-rw-r-- 1 sfmqrb sfmqrb    72342 Sep  6 17:58 build283.py
-rw-rw-r-- 1 sfmqrb sfmqrb    28249 Sep  6 18:25 build290a.py
-rw-rw-r-- 1 sfmqrb sfmqrb    63778 Sep  6 18:33 build290b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    68833 Sep  6 18:30 build291.py
-rw-rw-r-- 1 sfmqrb sfmqrb     5043 Sep  6 17:05 c1.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3501 Sep  6 17:05 c2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    56424 Sep  6 17:05 c3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78058 Sep  6 17:05 c4.png
-rw-rw-r-- 1 sfmqrb sfmqrb 60831599 Sep  6 18:01 cad_k.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb  2530822 Sep  6 18:01 cad_k.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    37980 Sep  6 17:16 c_av.png
-rw-rw-r-- 1 sfmqrb sfmqrb    29703 Sep  6 17:16 c_cros.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1174 Sep  6 17:16 c_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2612 Sep  6 18:28 c_germ.png
-rw-rw-r-- 1 sfmqrb sfmqrb    13418 Sep  6 18:28 c_greek.png
-rw-rw-r-- 1 sfmqrb sfmqrb     8430 Sep  6 18:28 c_ital.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11245 Sep  6 18:28 c_katrang.png
-rw-rw-r-- 1 sfmqrb sfmqrb     6717 Sep  6 18:28 c_katvar.png
-rw-rw-r-- 1 sfmqrb sfmqrb    28872 Sep  6 18:28 c_katvar_zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb    95615 Sep  6 16:39 coord_pg262.png
-rw-rw-r-- 1 sfmqrb sfmqrb  8373934 Sep  6 18:09 cpd.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb   378445 Sep  6 18:09 cpd.txt
-rw-rw-r-- 1 sfmqrb sfmqrb     4560 Sep  6 16:39 crop_ak2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4014 Sep  6 16:39 crop_ak.png
-rw-rw-r-- 1 sfmqrb sfmqrb    25373 Sep  6 16:42 crop_alk.png
-rw-rw-r-- 1 sfmqrb sfmqrb    24852 Sep  6 17:04 crop_fr269.png
-rw-rw-r-- 1 sfmqrb sfmqrb    43238 Sep  6 16:55 crop_germ269.png
-rw-rw-r-- 1 sfmqrb sfmqrb    51654 Sep  6 17:04 crop_gk269.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2585 Sep  6 17:05 crop_gk271.png
-rw-rw-r-- 1 sfmqrb sfmqrb    64142 Sep  6 17:02 crop_gr267.png
-rw-rw-r-- 1 sfmqrb sfmqrb     6411 Sep  6 16:39 crop_gr.png
-rw-rw-r-- 1 sfmqrb sfmqrb    23559 Sep  6 16:42 crop_kohul.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59386 Sep  6 16:39 crop_lat2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    51357 Sep  6 16:55 crop_latin269.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4761 Sep  6 16:39 crop_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4311 Sep  6 19:00 crop_loll2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3325 Sep  6 19:00 crop_loll3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3612 Sep  6 19:00 crop_loll.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3974 Sep  6 16:37 crop_me2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3300 Sep  6 16:37 crop_me.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10236 Sep  6 16:39 crop_op2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4935 Sep  6 16:37 crop_op.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5599 Sep  6 16:37 crop_pers.png
-rw-rw-r-- 1 sfmqrb sfmqrb    18514 Sep  6 18:52 crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb    22007 Sep  6 17:10 crop_sak.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5110 Sep  6 17:10 crop_sax.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4854 Sep  6 17:10 crop_shekar.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1249 Sep  6 17:05 crop_sirish.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30419 Sep  6 17:02 crop_skt267.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5359 Sep  6 19:00 crop_skt2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4064 Sep  6 19:00 crop_skt.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10043 Sep  6 16:58 crop_slav.png
-rw-rw-r-- 1 sfmqrb sfmqrb    24463 Sep  6 16:58 crop_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb  2144625 Sep  6 17:55 dmmpp.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    14732 Sep  6 18:27 e0.json
-rw-rw-r-- 1 sfmqrb sfmqrb    17126 Sep  6 17:54 e1.json
-rw-rw-r-- 1 sfmqrb sfmqrb    51742 Sep  6 18:33 e2.json
-rw-rw-r-- 1 sfmqrb sfmqrb  5301166 Sep  6 17:01 ediv.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb  1773345 Sep  6 17:01 ediv.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  1845041 Sep  6 18:04 gharib.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  3698758 Sep  6 17:50 IEC_full_djvu.txt
-rw-rw-r-- 1 sfmqrb sfmqrb      228 Sep  6 16:34 jscheck.js
-rw-rw-r-- 1 sfmqrb sfmqrb     4265 Sep  6 17:53 kapi_script.png
-rw-rw-r-- 1 sfmqrb sfmqrb   944060 Sep  6 18:06 kent_full.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   288525 Sep  6 18:07 kent_n222.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   285652 Sep  6 18:07 kent_n223.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   282304 Sep  6 18:07 kent_n224.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   268920 Sep  6 18:07 kent_n225.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb     1433 Sep  6 16:45 merge262.py
-rw-rw-r-- 1 sfmqrb sfmqrb    63035 Sep  6 16:56 mk265.py
-rw-rw-r-- 1 sfmqrb sfmqrb    73111 Sep  6 17:13 mk267.py
-rw-rw-r-- 1 sfmqrb sfmqrb    71564 Sep  6 17:08 mk268.py
-rw-rw-r-- 1 sfmqrb sfmqrb    41609 Sep  6 17:31 mk274.py
-rw-rw-r-- 1 sfmqrb sfmqrb    51778 Sep  6 17:32 mk276.py
-rw-rw-r-- 1 sfmqrb sfmqrb    46494 Sep  6 17:52 mk279.py
-rw-rw-r-- 1 sfmqrb sfmqrb    16605 Sep  6 17:54 mk280b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    17667 Sep  6 17:56 mk280c.py
-rw-rw-r-- 1 sfmqrb sfmqrb    43177 Sep  6 17:50 mk280.py
-rw-rw-r-- 1 sfmqrb sfmqrb    58322 Sep  6 17:51 mk282.py
-rw-rw-r-- 1 sfmqrb sfmqrb    63940 Sep  6 18:05 mk285.py
-rw-rw-r-- 1 sfmqrb sfmqrb    67974 Sep  6 18:09 mk286.py
-rw-rw-r-- 1 sfmqrb sfmqrb    60646 Sep  6 18:11 mk287.py
-rw-rw-r-- 1 sfmqrb sfmqrb    50446 Sep  6 18:33 mk292b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    14748 Sep  6 18:27 mk292.py
-rw-rw-r-- 1 sfmqrb sfmqrb    41011 Sep  6 18:29 mk294.py
-rw-rw-r-- 1 sfmqrb sfmqrb    45170 Sep  6 18:47 mk297.py
-rw-rw-r-- 1 sfmqrb sfmqrb    67312 Sep  6 18:51 mk298.py
-rw-rw-r-- 1 sfmqrb sfmqrb    44967 Sep  6 18:51 mk299.py
-rw-rw-r-- 1 sfmqrb sfmqrb    50897 Sep  6 18:54 mk300.py
-rw-rw-r-- 1 sfmqrb sfmqrb    49830 Sep  6 19:05 mk301.py
-rw-rw-r-- 1 sfmqrb sfmqrb    60810 Sep  6 19:07 mk303.py
-rw-rw-r-- 1 sfmqrb sfmqrb  8373934 Sep  6 17:00 mk.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb   378445 Sep  6 17:00 mk.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    11601 Sep  6 16:42 p262-g01.json
-rw-rw-r-- 1 sfmqrb sfmqrb    10625 Sep  6 16:43 p262-g02.json
-rw-rw-r-- 1 sfmqrb sfmqrb    19393 Sep  6 16:46 p262-g03.json
-rw-rw-r-- 1 sfmqrb sfmqrb    19959 Sep  6 16:44 p262-g04.json
-rw-rw-r-- 1 sfmqrb sfmqrb    12063 Sep  6 16:43 p262-g05.json
-rw-rw-r-- 1 sfmqrb sfmqrb    12051 Sep  6 16:44 p262-g06.json
-rw-rw-r-- 1 sfmqrb sfmqrb    12737 Sep  6 16:44 p262-g07.json
-rw-rw-r-- 1 sfmqrb sfmqrb    17259 Sep  6 16:46 p262-g08.json
-rw-rw-r-- 1 sfmqrb sfmqrb    17820 Sep  6 16:53 p262-g09.json
-rw-rw-r-- 1 sfmqrb sfmqrb    17855 Sep  6 16:45 p262-g10.json
-rw-rw-r-- 1 sfmqrb sfmqrb    14983 Sep  6 16:44 p262-g11.json
-rw-rw-r-- 1 sfmqrb sfmqrb    25352 Sep  6 16:46 p262-g12.json
-rw-rw-r-- 1 sfmqrb sfmqrb    17745 Sep  6 16:44 p262-g13.json
-rw-rw-r-- 1 sfmqrb sfmqrb   105748 Sep  6 16:39 p263hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5565 Sep  6 17:22 p275_krei_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb    53703 Sep  6 17:22 p275_pahlavi.png
-rw-rw-r-- 1 sfmqrb sfmqrb     7106 Sep  6 17:34 p279_greek.png
-rw-rw-r-- 1 sfmqrb sfmqrb    12970 Sep  6 17:34 p279_word.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3647 Sep  6 17:34 p279_xsaeta.png
-rw-rw-r-- 1 sfmqrb sfmqrb   130651 Sep  6 17:48 p283_arrow.png
drwxrwxr-x 2 sfmqrb sfmqrb     4096 Sep  6 18:02 p284
-rw-rw-r-- 1 sfmqrb sfmqrb    43108 Sep  6 17:51 p284_e0_fa.png
-rw-rw-r-- 1 sfmqrb sfmqrb    89734 Sep  6 17:51 p284_e0.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59639 Sep  6 17:48 p284_e2b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   106502 Sep  6 17:48 p284_e2.png
drwxrwxr-x 2 sfmqrb sfmqrb     4096 Sep  6 18:25 p289
-rw-rw-r-- 1 sfmqrb sfmqrb    54419 Sep  6 18:05 p289_labibi.png
drwxrwxr-x 2 sfmqrb sfmqrb     4096 Sep  6 18:33 p290
-rw-rw-r-- 1 sfmqrb sfmqrb     1476 Sep  6 18:11 p291_esfand.png
-rw-rw-r-- 1 sfmqrb sfmqrb    31043 Sep  6 18:11 p291_root.png
drwxrwxr-x 2 sfmqrb sfmqrb     4096 Sep  6 18:53 p295
drwxrwxr-x 2 sfmqrb sfmqrb     4096 Sep  6 18:49 p296
-rw-rw-r-- 1 sfmqrb sfmqrb     9447 Sep  6 18:41 p297_av2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     8787 Sep  6 18:41 p297_cav.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2803 Sep  6 18:41 p297_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb     8189 Sep  6 18:41 p297_op.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5216 Sep  6 18:55 p303_n18b.png
-rw-rw-r-- 1 sfmqrb sfmqrb     7082 Sep  6 18:55 p303_n18.png
-rw-rw-r-- 1 sfmqrb sfmqrb     7046 Sep  6 18:55 p303_n5.png
drwxrwxr-x 2 sfmqrb sfmqrb     4096 Sep  6 19:11 p304
-rw-rw-r-- 1 sfmqrb sfmqrb     2952 Sep  6 19:00 p305_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5794 Sep  6 19:00 p305_lat0.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4047 Sep  6 19:00 p305_lat1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66777 Sep  6 16:42 pg261.png
-rw-rw-r-- 1 sfmqrb sfmqrb    84660 Sep  6 16:39 pg262.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71156 Sep  6 16:38 pg263.png
-rw-rw-r-- 1 sfmqrb sfmqrb    92930 Sep  6 16:37 pg264hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    57862 Sep  6 16:35 pg264.png
-rw-rw-r-- 1 sfmqrb sfmqrb    13324 Sep  6 16:57 pg265_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb    86370 Sep  6 16:57 pg265.png
-rw-rw-r-- 1 sfmqrb sfmqrb    79922 Sep  6 16:42 pg266.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70622 Sep  6 16:56 pg267.png
-rw-rw-r-- 1 sfmqrb sfmqrb    69592 Sep  6 16:52 pg268.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71754 Sep  6 16:55 pg269.png
-rw-rw-r-- 1 sfmqrb sfmqrb   122626 Sep  6 16:58 pg270hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    87489 Sep  6 16:55 pg270.png
-rw-rw-r-- 1 sfmqrb sfmqrb   115300 Sep  6 17:05 pg271hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66696 Sep  6 17:04 pg271.png
-rw-rw-r-- 1 sfmqrb sfmqrb    68566 Sep  6 16:58 pg272.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66829 Sep  6 17:28 pg273_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb   157304 Sep  6 17:10 pg273hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70615 Sep  6 17:27 pg273.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65586 Sep  6 17:18 pg274.png
-rw-rw-r-- 1 sfmqrb sfmqrb    80338 Sep  6 17:21 pg275.png
-rw-rw-r-- 1 sfmqrb sfmqrb    76740 Sep  6 17:15 pg276.png
-rw-rw-r-- 1 sfmqrb sfmqrb    44171 Sep  6 17:16 pg277.png
-rw-rw-r-- 1 sfmqrb sfmqrb    89267 Sep  6 17:26 pg278.png
-rw-rw-r-- 1 sfmqrb sfmqrb   168655 Sep  6 17:34 pg279hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75777 Sep  6 17:34 pg279.png
-rw-rw-r-- 1 sfmqrb sfmqrb    82065 Sep  6 17:34 pg280.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61535 Sep  6 17:39 pg281.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70575 Sep  6 17:34 pg282.png
-rw-rw-r-- 1 sfmqrb sfmqrb    74784 Sep  6 17:47 pg283.png
-rw-rw-r-- 1 sfmqrb sfmqrb    81024 Sep  6 17:50 pg284hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    81024 Sep  6 17:51 pg284.png
-rw-rw-r-- 1 sfmqrb sfmqrb   144566 Sep  6 17:49 pg284_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    84487 Sep  6 17:53 pg285.png
-rw-rw-r-- 1 sfmqrb sfmqrb   106264 Sep  6 17:53 pg286hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    76099 Sep  6 18:10 pg286.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72442 Sep  6 17:59 pg287.png
-rw-rw-r-- 1 sfmqrb sfmqrb    53847 Sep  6 17:58 pg288.png
-rw-rw-r-- 1 sfmqrb sfmqrb    28862 Sep  6 18:27 pg289_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb    91779 Sep  6 18:26 pg289.png
-rw-rw-r-- 1 sfmqrb sfmqrb   187988 Sep  6 18:19 pg290hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    98901 Sep  6 18:18 pg290.png
-rw-rw-r-- 1 sfmqrb sfmqrb   105586 Sep  6 18:11 pg291hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70592 Sep  6 18:10 pg291.png
-rw-rw-r-- 1 sfmqrb sfmqrb   103438 Sep  6 18:12 pg292.png
-rw-rw-r-- 1 sfmqrb sfmqrb    36312 Sep  6 18:20 pg294_p294.png
-rw-rw-r-- 1 sfmqrb sfmqrb    24759 Sep  6 18:56 pg295_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb   125960 Sep  6 18:28 pg295hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    80086 Sep  6 18:56 pg295.png
-rw-rw-r-- 1 sfmqrb sfmqrb    56184 Sep  6 18:39 pg296.png
-rw-rw-r-- 1 sfmqrb sfmqrb   130247 Sep  6 18:41 pg297hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66500 Sep  6 18:33 pg297.png
-rw-rw-r-- 1 sfmqrb sfmqrb    60960 Sep  6 18:39 pg298.png
-rw-rw-r-- 1 sfmqrb sfmqrb    99543 Sep  6 18:52 pg299hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    52844 Sep  6 18:38 pg300.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61588 Sep  6 18:56 pg301.png
-rw-rw-r-- 1 sfmqrb sfmqrb   182431 Sep  6 19:00 pg302hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    91158 Sep  6 18:59 pg302.png
-rw-rw-r-- 1 sfmqrb sfmqrb   122418 Sep  6 18:55 pg303hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    89589 Sep  6 18:52 pg303.png
-rw-rw-r-- 1 sfmqrb sfmqrb    48728 Sep  6 19:00 pg304.png
-rw-rw-r-- 1 sfmqrb sfmqrb   151120 Sep  6 19:00 pg305hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    58313 Sep  6 18:59 pg305.png
-rw-rw-r-- 1 sfmqrb sfmqrb    50721 Sep  6 18:58 pg306.png
-rw-rw-r-- 1 sfmqrb sfmqrb   132637 Sep  6 18:38 sns_n155.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   129771 Sep  6 18:38 sns_n156.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   130970 Sep  6 18:38 sns_n90.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   531356 Sep  6 18:38 sns_n90_right.png
-rw-rw-r-- 1 sfmqrb sfmqrb   124445 Sep  6 18:38 sns_n92.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   522585 Sep  6 18:38 sns_n92_left.png
-rw-rw-r-- 1 sfmqrb sfmqrb   495290 Sep  6 18:38 sns_n92_right.png
-rw-rw-r-- 1 sfmqrb sfmqrb   390669 Sep  6 18:10 syn_n1548.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   390669 Sep  6 18:10 syn_n1549.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   390669 Sep  6 18:10 syn_n1550.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   351684 Sep  6 18:35 tad_n59.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   342929 Sep  6 18:35 tad_n59_mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb   242025 Sep  6 18:34 tad_n60_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   282364 Sep  6 18:34 tad_n60.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   335678 Sep  6 18:34 tad_n60_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   276093 Sep  6 18:34 tad_n61.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   332662 Sep  6 18:34 tad_n62.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   334767 Sep  6 18:35 tad_n65.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   265879 Sep  6 18:35 tad_n65_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   295896 Sep  6 19:11 tad_n66.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   304367 Sep  6 19:11 tad_n67.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   308480 Sep  6 19:11 tad_n68.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb     3698 Sep  6 18:19 zar_line.png
```


### [2026-09-06T23:11:10.699Z] TOOL RESULT

```
=== KLN eclipse
KLN_1971.txt:78770:eclipse, n. — OF. eclipse (F. eclipse), fr. L. eclip- 
=== KLN liquid
KLN_1971.txt:14777:liquid’ (which is rel. to vdceiv, ‘to flow’), and 
KLN_1971.txt:98622:liquid, C4H4O ( chem .) — Formed fr. L. furfur , 
KLN_1971.txt:98868:liquid’, fr. fusus, pp. of fundere , ‘to pour*. See 
KLN_1971.txt:112009:liquid’. Cp. -emia. 
KLN_1971.txt:134479:liquid, fluid’, prob. borrowed fr. Gk. Xaxa£, 
KLN_1971.txt:138145:liquidus, ‘flowing, fluid’. 
KLN_1971.txt:138654:liquid, to melt’, which is compounded of liquere , 
KLN_1971.txt:138670:liquid, adj. — ME., fr. OF. (— F.) liquide, fr. L. 
KLN_1971.txt:138671:liquidus, ‘flowing, fluid, liquid, clear’, fr. liquere , 
KLN_1971.txt:138681:Liquidambar, n., a genus of trees, the sweet gum 
=== KLN loan/lend/eleven
KLN_1966.txt:93:LOAN  TRANSLATIONS
KLN_1966.txt:94:Loan  translations  are  important  guideposts  on  the  road  on  which  civilization  and  culture  trav¬ eled  in  the  course  of  centuries  from  nation  to  nation.  Through  them  we  learn  e.g.  that  the chief  elements  of  the  science  of  grammar  developed  in  ancient  Greece  and  reached  Western Europe  through  the  medium  of  the  Romans.  (T  he  overwhelming  majority  of  grammatical  terms in  the  modern  languages  are  loan  translations  of,  or  derive  directly  from,  Latin  words h  which themselves  are  loan  translations  of  Greek  words.  Cp.  e.g.  the  words  subject,  verb,  adverb,  nomi¬ native,  accusative,  genitive,  dative  in  this  dictionary.)
KLN_1966.txt:10630:loan  words  cp.  costive  and  words  there  re¬ ferred  to.
KLN_1966.txt:21459:lend,  tr.  and  intr.  v.  —  ME.  lenen,  fr.  OE.  Henan, ‘to  lend,  grant’,  fr.  lien,  ‘loan’,  rel.  to  Du. lenen,  OHG.  lehanon,  MHG.  lehenen,  G.  lehnen, ‘to  lend’.  See  loan.
KLN_1966.txt:21996:loan
KLN_1966.txt:22000:loan,  n.  —  ME.  Ian,  Ion,  fr.  ON.  Ian,  which  is  rel. to  OE.  lien,  ‘lending,  thing  lent,  loan’,  henan,  ‘to lend’,  OS.,  OHG.  lehan,  OFris.  len,  ‘thing  lent, loan’,  Du.  leen,  ‘loan,  fief’,  MHG.  lehen,  G. Lehen,  Lehn,  ‘fief’,  OE.  leon,  ON.  Ija,  OFris. lla,  ‘to  lend’,  OHG.  lihan,  ‘to  borrow’,  MHG. liken,  ‘to  borrow;  to  lend’,  G.  leihen,  ‘to  lend’, rarely,  ‘to  borrow’,  Goth,  leihan,  ‘to  lend’.  The orig.  meaning  of  these  verbs  was  ‘to  let  have, leave’.  They  derive  fr.  I.-E.  base  *liqw-,  ‘to  let, leave’,  whence  also  OI.  rinakti,  ‘leaves’,  riktdl, i, ‘empty’,  reknah,  ‘possession,  property’,  a  tire - kah,  ‘remainder’,  Arm.  Ik'anem,  ‘I  leave’,  e-lik', ‘he  left’,  Gk.  Xeirmv,  ‘to  leave’,  Xotrrd?,  ‘re¬ maining,  surviving’.  L.  linquere  (perf.  ttqui),  ‘to leave',  Lith.  liekit,  likti,  ‘to  leave  behind’,  liktas, Lett,  likts,  ‘left,  left  over’,  Lith.  lekas,  ‘left  be¬ hind’,  palaikas,  ‘remainder’,  the  second  element in  OSlav.  otu-Uku,  of  s.m.,  OPruss.  polinka,  ‘he remains’,  OIr.  leicim,  ‘I  leave’,  and  the  second element  in  Lith.  vienuo-lika,  ‘eleven’,  dvy-Uka, ‘twelve’.  Cp.  lend  and  the  second  element  in eleven,  twelve.  Cp.  also  relinquish  and  delict,  de¬ linquent,  derelict,  eclipse,  ellipse,  ellipsis,  elliptic, limma,  lipo-,  ‘lacking’,  paraleipsis.
KLN_1966.txt:22002:loan  word,  —  Loan  translation  of  G.  Lehnwort, which  is  compounded  of  lehnen,  ‘to  borrow’, and  Wort,  ‘word’.  See  loan  and  word.
KLN_1966.txt:40556:twelve,  adj.  and  n.  —  ME.  twelf,  twelve,  fr.  OE. twelj,  rel.  to  OS.  twelif,  ON.  tolf,  Swed.  tolf, Dan.,  Norw.  tolv,  OFris.  twelef,  twelif,  MDu. twalef,  Du.  twaalf,  OHG.  zwelif,  MHG.  zwelif, zwelef,  zwelf,  G.  zwolf,  Goth,  twalif.  These words  are  compounds  meaning  lit.  ‘two  left  after (ten)’,  ‘two  added  (to  ten)’.  For  the  first  element see  two.  The  second  element  is  cogn.  with  L.  lin- quere,  Gk.  Aeitteiv,  ‘to  leave  behind’ ;  see  loan, relinquish  and  ep.  eleven.  Outside  Teutonic  cp. Lith.  dvy-lika,  ‘twelve’,  which  is  the  exact  equiv¬ alent  of  the  above  Teut.  words,  not  only  in meaning  but  also  in  derivation, twelvemo,  n.,  the  same  as  duodecimo.  —  A  hybrid arising  from  the  misreading  of  the  abbreviation (12  mo  (=  duodecimo)  for  twelvemo.  See  twelve and  cp.  duodecimo  and  words  there  referred  to. twentieth,  adj.  and  n.  —  ME.  twentithe,  formed fr.  twenty  on  analogy  of  fourth,  fr.  four,  etc.;  see numeral  suff.  -th.  Cp.  OE.  twentigoda,  ‘twen¬ tieth’.
KLN_1971.txt:490:LOAN TRANSLATIONS 
KLN_1971.txt:492:Loan translations are important guideposts on the road on which civilization and culture trav- 
KLN_1971.txt:12913:loan word, with the original meaning ‘as fra- 
KLN_1971.txt:18381:loan translation of 'TSpox^oq, ‘the water- 
KLN_1971.txt:22299:loan translation of Gk. fx&atva (see me- 
KLN_1971.txt:30434:loan word. See blank, adj. 
KLN_1971.txt:37200:twelve men sent by Moses to spy out the land 
KLN_1971.txt:38404:loan words fr. VL. *candus, contraction of can- 
KLN_1971.txt:45147:loan word fr. L. cicera, pi. of cicer , but was in- 
KLN_1971.txt:45622:Loanwords. Cp. the words chrysalis, cumin , se- 
KLN_1971.txt:48530:eleven , cliven, fr. OE. cleofan, rel. to OS. klio’fian. 
KLN_1971.txt:58639:loan word (possibly through the medium of an
```


## [2026-09-06T23:11:17.391Z] TOOL CALL #39: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/tad_n67.jpg"
}
```


### [2026-09-06T23:11:17.770Z] TOOL RESULT

```

```


## [2026-09-06T23:11:17.768Z] INPUT

[Image: original 1789x2838, displayed at 1261x2000. Multiply coordinates by 1.42 to map to original image.]


## [2026-09-06T23:11:41.854Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && for n in 63 64 65; do curl -sL -o tadA_n$n.jpg \"https://archive.org/download/TOB1932ARAR/page/n$n.jpg\" -w \"n$n %{http_code} %{size_download}\\n\"; done"
}
```


## [2026-09-06T23:11:42.741Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '138660,138690p' KLN_1971.txt; echo \"=== eclipse\"; sed -n '78765,78790p' KLN_1971.txt"
}
```


### [2026-09-06T23:11:48.084Z] TOOL RESULT

```
n63 200 300608
n64 200 311561
n65 200 334767
```


### [2026-09-06T23:11:48.166Z] TOOL RESULT

```
liquescens, gen. -entis, pres. part, of liquescere , 
‘to become liquid, to melt’, inchoative of liquere , 
‘to be liquid’. See liquid and -escent and cp. de- 
liquesce, deliquescent. 

liqueur, n., any of certain alcoholic liquors sweet- 
ened and flavored. — F., fr. L. liquorem, acc. of 
liquor , ‘a fluid, liquid’. See liquor. 

Derivative : liqueur, tr. v. 
liquid, adj. — ME., fr. OF. (— F.) liquide, fr. L. 
liquidus, ‘flowing, fluid, liquid, clear’, fr. liquere , 
‘to be fluid, be liquid’, which is rel. to lix, gen. 
licis, ‘ashes’, lixa, ‘water; lye’, prolixus, ‘extend- 
ed’, orig. ‘flowing forward’, and prob. cogn. 
with Oh. fliuch, ‘moist, wet’, OW .gulip, ModW. 
gwlyb , of s.m., W. glwith, ‘dew’, MBret. gloeb , 
ModBret. gleb, ‘moist, wet’. Cp. lixiviate, prolix. 
Derivatives : liquid, n., liquidate (q.v.), liquid-ly , 
adv., liquid-ness , n. 

Liquidambar, n., a genus of trees, the sweet gum 
tree (bot.) — A ModL. hybrid coined fr. L. li- 
quidus , ‘fluid’, and Arab, anbar, ‘amber’. See 

liquid and amber. 

liquidate, tr. and intr. v. — ML. liquidates, pp. of 
liquidare, ‘to liquidate’, fr. L. liquidus. See 
liquid and verbal suff. -ate. 

=== eclipse

EDENTATA 



eclipse, n. — OF. eclipse (F. eclipse), fr. L. eclip- 
sis , fr. Gk. ^cXei^k;, ‘a leaving out, forsaking, 
failure; eclipse’, fr. Ixkdn slv, ‘to leave out, 
forsake, cease; to be eclipsed’, Fr. lx (see ec-) 
and XslTOtv, ‘to leave’, which is cogn. with L. 
linquere , ‘to leave’. See relinquish and cp. ellipse. 
Derivatives: eclipse , tr. v., eclips-er , n. 
ecliptic, adj., i) pertaining to an eclipse; 2) per- 
taining to an ecliptic. — L. eclipticus , ‘pertain- 
ing to an eclipse’, fr. Gk. £xXei7TTix6?, fr. 
IxXzlneiv. See prec. word and -ic. 
ecliptic, n., apparent annual path of the sun. — 
Fr. L. linea ecliptica , ‘the ecliptic’, fr. eclipticus , 
‘pertaining to an eclipse’. The ecliptic was so 
called because it was supposed that eclipses of 
the sun and moon take place on the great circle 
forming the apparent annual path of the sun. 
eclogue, n., a short poem of pastoral character. 
— F. eclogue , eglogue , fr. L. ecloga , fr. Gk. 
txkoyii, ‘a choice, selection’, fr. £xX6yeiv, ‘to 
pick out, select’. See eclectic,
```


## [2026-09-06T23:11:55.407Z] TOOL CALL #42: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/tadA_n65.jpg"
}
```


### [2026-09-06T23:11:55.818Z] TOOL RESULT

```

```


## [2026-09-06T23:11:55.816Z] INPUT

[Image: original 1789x2838, displayed at 1261x2000. Multiply coordinates by 1.42 to map to original image.]


## [2026-09-06T23:12:07.413Z] TOOL CALL #43: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/tad_n66.jpg"
}
```


### [2026-09-06T23:12:07.945Z] TOOL RESULT

```

```


## [2026-09-06T23:12:07.943Z] INPUT

[Image: original 1789x2838, displayed at 1261x2000. Multiply coordinates by 1.42 to map to original image.]


## [2026-09-06T23:12:38.007Z] TOOL CALL #44: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/TAD && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/tad_n66.jpg /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/TAD/63.jpg && cat > /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/TAD/63.vision.txt <<'EOF'\n[TAD = Tobia al-Unaysi, Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya, printed p. ٦٣ = 63\n = archive.org/details/TOB1932ARAR leaf n66 (printed page = leaf n − 3; n65 = p.62, n67 = p.64).\n Read from the page image by vision; entries on the page, in order:]\n\nكستك وكشتيج — فارسي «كُستي» معناه خيط غليظ\n\nكسف وخسف الشمس والقمر كسوفاً — معرَّب اليوناني ekleipsis ومعناه نقصان النور، وقد تكسف\nالشمس لحيلولة القمر بينها وبين الارض. مرادفه احتجب\n\nكستنة — لاتيني castanea وهو شجر، وفي اليونانية kastanon، سُمّي باسم مدينة في بلاد اليونان بهذا الاسم\n\nكشتبان — فارسي «انگشتانه» معناه اصبعيّ، مرادفه قمع الخياط\n\nكشكول — أرامي «كُنِش كُل» معناه جامع كل شيء ...\n\nكعك — تعريب «كاك» الفارسي\n\nكلسات وقلشين — لاتيني calcea معناه غطاء عقب الرجل ...\n\nإكليرُس — يوناني kléros معناه إرث ونصيب ...\n\nكمبيالة — ايطالي cambiale ...\nكمبيو — cambio ...\nEOF\necho saved; ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/TAD/"
}
```


## [2026-09-06T23:12:39.530Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD Bd2 leikw\"; grep -n \"leiq\\^\\|leiq\\\"\\|leiqu\\|linquo\" incoming/WLD/WLD_Bd2_pages.txt | head -20; echo \"=== SYN leave\"; grep -n \"12.18\\|to leave, abandon\\|LEAVE, ABANDON\" SYN.txt | head -10"
}
```


### [2026-09-06T23:12:41.218Z] TOOL RESULT

```
saved
total 636
drwxrwxr-x  2 sfmqrb sfmqrb   4096 Sep  6 19:12 .
drwxrwxr-x 12 sfmqrb sfmqrb   4096 Sep  6 18:36 ..
-rw-rw-r--  1 sfmqrb sfmqrb 334767 Sep  6 18:36 62.png
-rw-rw-r--  1 sfmqrb sfmqrb   1272 Sep  6 18:36 62.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb 295896 Sep  6 19:12 63.jpg
-rw-rw-r--  1 sfmqrb sfmqrb   1241 Sep  6 19:12 63.vision.txt
```


### [2026-09-06T23:12:41.285Z] TOOL RESULT

```
=== WLD Bd2 leikw
26233:1. leiq^- „lassen, zuriick-, libriglassen".
26248:                                                         leiqu-
26356:sein“, nicht als „flieBen lassen, rinnen lassen^^                               = leiq^- „lassen‘‘ (Curtius 463,
=== SYN leave
7340:12.18). Walde-P. 2.403. 638, 648. Feist 330.
13678:ChSI. délo (renders épyov), ete., gen- eral Slavic for concrete ‘work’ : déti ‘put’, etc. (9.11, 12.18). Hence vb. ChSI. (st-)délati in Gospels reg. for Epya- touat, later for xovéw, Boh. délati ‘do, make’ and ‘work’ (Pol., Russ. ‘do’, 9.11).
16977:Ir. doléicim, teilcim, NIv. teilgim, epd. of léicim ‘leave’ (12.18). Pedersen 2.564.
17593:NE leave (12.18) in phrases like lefé the house is equivalent to ‘depart from’, hence now also without object, perhaps the most common popular expression, as he is leaving, he has just left.
19486:7. Skt. ha- ‘leave’ (12.18), ‘give up’, also ‘lose’. But ‘lose’ mostly expressed as ‘be lost by’, e.g. bhrasta-, pple. of bhrang- ‘fall, fall away, be lost’.
19491:Words for ‘release’ reflect such no- tions as ‘loose’ (in lit. sense ‘unbind’), ‘loosen’, ‘let go, send forth, let slip’, etc. There is frequent connection and some overlapping in use with words for ‘leave’ (12.18) and ‘let, permit? (19.47).
19500:3. Ir. léicim, also ‘let, leave’ : Grk. eixw, Lat. linquere ‘leave’, etc. (12.18).
19502:Nir. scaoilim = MIr. scailim ‘scat- ter, strew, separate’ : Lith. skelti ‘split’, ON skilja ‘divide, separate’ (cf. skilja eptir ‘leave’, 12.18), etc. Walde-P. 2.592.
19507:4. Goth. fra-létan, af-létan, ON lata laust, Dan. Igslade, OF forl@tan, Du loslaten, OHG furlazzan, NHG entlassen, loslassen, cpds. of Goth. létan, ete. ‘let, leave’ (12.18). ;
20135:3. Ir. airléicim, NIr. airleagaim, cpd, of léicim ‘leave, let? (12.18) with air. ‘pre-, pro-’. Pedersen 2.563.
```


## [2026-09-06T23:12:47.970Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '26225,26270p' incoming/WLD/WLD_Bd2_pages.txt; echo \"..... 26340-26380\"; sed -n '26335,26380p' incoming/WLD/WLD_Bd2_pages.txt; echo \"=== page tag\"; awk 'NR<=26233 && /pdf page/{p=$0} END{}' incoming/WLD/WLD_Bd2_pages.txt; grep -n \"pdf page\" incoming/WLD/WLD_Bd2_pages.txt | awk -F: '$1<26233' | tail -3"
}
```


### [2026-09-06T23:12:49.847Z] TOOL RESULT

```
wert; Xaindg Xrjydv ist ohnehin keine sichere Beziehung, und rCtkd ist ety-
                  :



mologisch nur mit A^orsicht zu gebrauchen.


1. leiq^- „lassen, zuriick-, libriglassen".

  Ai. rindkti (3. pi. rincanii) „la6t, laBt los, raumt ein‘', rikUU „leer, frei
von etwas", ricydte „wird befreit von etwas, geht verlustig", rekii- „leer",
atireka- m. „tTberbleibsel", reknas- n. ,ererbter Besitz, Eigentum" — av.
                                                            5

raexnah- „Gut, Schatz, Erbteil", irinaxti ,,verlafit"', np. rextan „ausgie8en",
gurexten „entbehren"; arm. (Hiibschmann Arm. St. I 34, Arm. Gr. I 455)
llcanem „lasse", Aor. clilc               =
                            eXme^ Ikanim „werde verlassen, werde matt,
 lasse ab": gr. Xelnco „lasse, verlasse", Xoinog „ubrig"', Xifizcdvco „lasse", Xto-
 amyxv'     edocoy,£v      Hes. (wohl mit 7, aus Hinq^-io^ Brugmann IP 3, 279);
 lat. linqno,    -ere,     liqui     {^loiq^ai,    vgl. ni. rireca^        gr.    XeXoLJia^      und bes. got,
 laih)^    relictus      „zurucklassen",          reUcuos „ubrig";         strittig       air.   leicim   „lasse.
                                                         leiqu-
                                                                                                            397

  lasse los“ (Strachan               BB. 20, 31, FicklH* 242.
                                                     Pedersen KG. I 130 152
 II 565, Meillet Msl. 15, 254;    von Thurneysen lA. 6, 195, Stokes KZ. 3?'
 258 zu kelt.-lat. lancea, frz. lancer „schlendern“,
                                                      von letzterem weiter zu
 TWTvf. flengja ds. gestellt; dock stellt
                                          do-Ieicim „-werfe“ nicht die ursprgl.
 Bed. des Verbums dar, sondern ist als „worauf
                                                                            loslassen“ zu verstehen,         ist
 terner      frz.       lancer
                         von lancea abgeleitet, und endlich norw. flengja
                                   erst
 „schleudem“ erst jiingere Bed.-Entw. aus aisl. flengja
                                                        „peitschen, gei6eln“
 s. £alk-Torp u. flmnge
                        und Wz. piaq- ,,schiagen“.
    Got. leihan,           aisl.    Ija,   ahd. llhan,    ags. Icon „leihen“,          Ptc. as. ahd. farli-
 wan „verbehen“, aisl. leiga „Tnieten“, aisl. Ian,                          ags.   Un,     ahd. UJian ,.ge-
 hehenes Gut, Lehen“ (= ai. reknas-,                         vgl.   zum J-Formans auch cech. lik-
         .feillet Msl. 15,2541f.): abg. otolck^ „Pberbleibsek‘
..... 26340-26380
                                                  (s.                              Pedersen KG. I 128)

KG I 60). Vielleicht auch                                                                    (Pedersen
                                           lit.   leknas „Morast“,     lett.Wens, lekna ds nied-
                                                                            ’>«          Abi. 361;
                    H
                                                                     ...Einbuchtung, daher feuchte
Ske^r
                                  ;




398                                         ieig', leiqr       —     (leig-), iTg-



  Die kelt. Worfce nicht wahrscheinlicher als *^lq-                                         {fliuch^   9'i^^yh      also mit
Formans -wo-) abl. zu air. folcaim „bade“, cymr. golchi „baden‘^, Wz.
uelg- „feuchf^ (Fickll^ 285 zw., Zupitza KZ. 35, 257).    leiqy^ „na6, fiiissig

sein“, nicht als „flieBen lassen, rinnen lassen^^                               = leiq^- „lassen‘‘ (Curtius 463,
Fick             121, 533; iiber 2i\ paitiraecayeiti
                                            .
                                                                         s.    yielmehr Bthl. Air. Wb. 1480).

1. leig-         und leiq- „durftig, elend, krank; Krankheit, schlechtes Ergehen^.
     Gr. ^otyog „Yerderben, Unheil, Untergang, Tod“, loiycog „verderblich,
     1.

unheilbringend, todlich“; dUyog .,klein^‘; alb. I'ih {-gu~) jjbose, mager“;
        liga „Krankheit^^, lett. liga „schwerere Krankheit, Seuche“.
     lit.

   Bezzenberger BB. 4, 332, G. Meyer Alb. Wb. 245, Alb, St. Ill 7, Pers-
sonWzerw. 15, Pedersen IP. 5, 60 f., Hoffmann BB. 26, 138 f., Lid en Arm.
St. 97 f. Persson aaO. vermutet in hig- eine Erw. von lei- „sich ducken, ein-
gehn, schwinden'" (?)                 —
                              Slav. hg^Jc^ „leicht“ bleibt trotz Lewy IP. 32, 163
bei leq^tJi- „leicht“; nicht iiberz. reiht er auch ags. llcettan, liccettan „heucheln‘^
an        (Bed. sei wie zwischen got. lints ,,heuchlerisch'‘: ahd. liiszil „klem“).
     2.    arm. aiPcat „arm, diirftig, wenig, knapp‘‘; Subst. „Armer, Bettler“,
aWat-anam „bin oder werde arm; nehme ab, werde schwach“                                                                    aus
idg.^ollqo-; demnach ist auch das d- von gr. d/Jyog wohl ait,                                                        die   Wz.
also als *(o)Z^/f/-/g- anzusetzen);                      air.    llach „elend, ungliicklich'^;                     apr. licuts
          von Bezzenberger GGIS”. 1905, 455 Anm. 3, Trautmann Apr 370
=== page tag
```


## [2026-09-06T23:13:04.235Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SOD ryz\"; grep -n \"ryz\\|rxm\\|'to flow'\\|pryc\" SOD_pages.txt | head -20; echo \"=== SOD leaf 11\"; awk 'BEGIN{RS=\"\\f\"} NR==12' SOD_pages.txt | head -25"
}
```


## [2026-09-06T23:13:06.027Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HUB\"; grep -n -i \"rextan\\|rêxtan\\|gurextan\\|ibrīq\\|ibriq\\|ābrēz\" HUB.txt | head -20; echo \"=== LEW liqueo\"; grep -n -i \"liqueo\\|liquere\" LEW_1910.txt LAT.txt | head -20"
}
```


### [2026-09-06T23:13:06.807Z] TOOL RESULT

```
=== SOD ryz
5172:    STSC p31                                                    498 >bryz-   C                         o^jJ-^^/^j
7421:      (o)poxsa ?, paysa ? =*pys(h)                                  (o)prast ©pt. st. =»pryz-, pr'st-
9404:1950 Vryz-    M                     (u-kjij)o-^r 'J^-J
9412:1951 >wryzyh M                                       jjJ^         later
11449:      Prazand ©MR bryz-, Khwar. Wz-% A v. brdz-
11620:     Par-Po5an                                                     VJ 881; Sogdica. 64, 11; *firryz "to touch" GMS
14746:       frez ©<*fra-razaya =»fryz-, fr'st-                                   negligence
14826:                                                                            fryz-, frsty
14842:3913 frmst-      M                                      J^j                frastc ©ace. -tw\ pi. -tyt =*fryz-, frst-
15006:3965 fryst =$ fr>yz-                                              3978 f ryz-    C                     jj^Tc^jj < jj^owl
16363:       xwart, xurt (ywrtk-) ©pt. st. & inf. =*ywr-\            4443 Ywry zync(h) =» ywryznych
16420:4442 Ywryznych S              (j->-V^)^f^u
20174:              n5-frast =»frst-, fryz-                                       naz =»n)sny(h)> n}z-
20599:5872 npryc S                                                          curse
21358:                                                                       nu~rez(c) ©ob. pi. -ty(y) ? =>nwryz
21363:                                                                  6149 nwryz B                                J^^- '^sJjr*
21365:                                                                       nu-rez(e) (nwryz) ©ob. pi. -y ? =^nwryjy
21371:       TSP 2.332; GMS 1096, 1331; CII 1990 B10                    6150 nwryz C => nwryz
21372:                                                                  6151 nwryzqyn C                          JiUr ojx i J^
22262:      parayz (p'rYz) ^p'ryz
=== SOD leaf 11
 ^LJ* <T-flta« .LfiT ^4-i^-y t *j> *jL» ^jU j lt7-^ tSj^* oy* J-*^*
j>^ >> *f jT ^1x^7 ^fcL^- ^ojjjo — ( j ^jAa j~J ^ilx j

                                                                                               Ui'j> ^5J*-' i5^L.J *^ ijJ^ S^ kyjj* iS^J* OU^^U 4 i,j>%a
o I ^ & <lj ^^ jl> j ^o-^jfj ^jl Xi^T ^^ <J^ U^x-                                .o-J          ^ ^-py ^UfclXii-j* J XU> 0^> ji .Xo^yi ^ Xj <Jj*>Oj> jJ

                                                                                               ^J^** ^UwUT             jl j* jl jilz-JJjjl ^ <fc# JjA ^U jU Jj jj ext-
                                                                                               L^cri^^— J J' tji*^"^ J^3 jf-ur ^ l^i^t* U ^                ^Ua.-.j 0j^
^ jlx« jl & (_o^i-> <T-IU* .<i—l *xU ^ySt U ^/^ l^O'jf \J\j* ^y?                               j' ^ Jk (J ° j'-M-1 ^ J1-^ ^ * * ^-^ <*l^v^ .Cib^. fcj^ Lfi^ ^-JL*—
                                                                                               jj! .j_^ *XU jUT^j J0>j ^jI^^- J^rr^—-? jl ^ *J-i< ljj>t* j^JLel jU

4&j <XXili tfjS^? LT*> C^r? J c£J^-^ i^W-*''' f'y' ^^ ->■> '■*.*
                   .xx*   -a ^p^^w*     j iSjA* ^aJL^tj      »^-- O'j^U^     «^*L^



jljj-i* ji <J»j   * *£■> OL*-*il   ^ ,"-*.   ■ ,.; 4-S" *— _Xi" <JJ jliL   XjU                 ^xi- ^>^* <-f jLu ^            jl <T ^<^U j>_Jfi* <0lj*oj-> j' -u*

4^ijJ tfJJi** ^jj'Ll— fj ^LrfK^O jl Xu (Jj3 Xj>- ijtejy j (<-£jl jAijjj)                       jj 4^ O-l O^jy iS**^ Jtf^f cJVi ^XU< ^bj^^i+A                    c4^i jf

O^^-lp 4j f IjJI <jL XL* 4i i_^      IoLX-1 j'^"^ ^«iJ^ j^'j* j' .XfoX*                        \^\» U \<\*Y) ^UT oU           ^a^t^     jLM OA? ^ ^ pX-. u> J-Jjl
(j(jkj_^a cot^ o-^L-- xli- u ' L^it j xjUL o^p           (jLot^L- jUj j^ j^xj                  jTl^* jl ui* j^ --Li ^^UiOl^tl oUJIUi ^ ^U vT^-U» ^^fi <(tfJ^
^UU     >a j-** ^t .c— J «j^ &%*                f>- 0^ p>> ^<-^ >> ^r^jj                      Ol^^H ^>^-           03tX_L   ^1* j i^ii^fl ^t>      ^^A>    J tf jbw jU*

                                                                                               jl ^L      -CJ j^   jU^-0 >J U^^U     v^JU* jTl^i jl ^     J >j, ^ jy»J
```


### [2026-09-06T23:13:06.873Z] TOOL RESULT

```
=== HUB
182:ruk; gurSy Tlucht' neben gurextan^ Wrzl. rik. Die
1362:Verlassen*", dem doch nur np. *pairextan entsprechen
5485:234, 235, ap. viyatarayama 'wir uberschritten' ; gurextan
5486:*fliehen' = paz. varextan Miii. Gl. 207, von vi + Wzl. ric;
8572:Tlucht' zu gurextan *fliehen', Wrzl. rik; furoy *Glanz* zu
8959:diixtar 'Tochter, zd. duydar-, skr. duhitar-; rextan aus-
9562:halten = paz. pah(a)rextan Shk. 262 , phi. pdhrextan
=== LEW liqueo
LAT.txt:34010:reposer sur *k Wm , alors cf. liquare, liquere ? Mais la vieille forne
LAT.txt:34192:dersen, 7 . G. d.k. Spr., II 565. - V. aussi liqueo.
LAT.txt:34240:du gr. t^oc, sous 1 'influence de liquor, liquere, A cause des
LAT.txt:34246:liqueo, -es, liqui (licui? cf. Cic., N.D.1,43,117; forme du reste
LAT.txt:34247:rare, et ^vitee en raison de son ambiguite), liquere: etre clair ou
LAT.txt:34260:liqueo signifie "etre clair, limpide", au sens propre et figure;
LAT.txt:34278:Cf. aussi proliqueo (transerit proliceo): prol icere: emanare, ef¬
LAT.txt:34300:laisse", il en resuite que liqueo serait un verbe d'etat appartenantala
LAT.txt:34468:V. liqueo, et colliciae. Les formes a ~s- reposent sur un ilar-
```


## [2026-09-06T23:13:18.932Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '34246,34310p' LAT.txt"
}
```


### [2026-09-06T23:13:18.981Z] TOOL RESULT

```
liqueo, -es, liqui (licui? cf. Cic., N.D.1,43,117; forme du reste
rare, et ^vitee en raison de son ambiguite), liquere: etre clair ou
liquide; etre filtre;
liqu 5 , -as, -iul, -atum, -are: i° clarifier, filtrer; 3 0 lique-
fier.
Formes verbales deriv^es d'une racine *le ik w ~/l ik w -. Liquor dont
la premifere syllabe compte toujours pour longue, s'emploie seulement
au sens de "s' 4 couler, couler"; cf.Vg.Ae.9,813 tum toto corpore sudor/
liquitur ; 9,679 liquentia flumina (toutefois d'aprfes Servius il fau¬
drait lire ici Liquetia, nom propre; cf.Havet, Man . de crit.verb.
5 174); 1,433 liquentia mella/stipant, etc.,et au sens figure dans
Pl.Tri.343 (cr 4 t.) ilico res foras labitur, liquitur. - Rare, surtout<J 45 ~
lira
poetique. Pas de derives; cf. toutefoia *liquordre, M.L.so7ya.
liqueo signifie "etre clair, limpide", au sens propre et figure;
cf. Ia formule juridique non liquet exprimee par les initiales H.L.
Se dit d'un liquide filtre ( uina liquentia , Ae.5,338; cf. 1 'emploi
figure de liquet et de defaecatum est dans Pl.Ps.760); sens auquel
s'adjoint celui de "etre liquide ou fluide" (qui semble etre d 4 rive
et plus tardif), e.g. Vg. Ae.6,734 caelum ac terras camposque liquentes
"les plaines liquides", cf. Ov.F.5.547 aequore liquidS. ~ A lique 5 se
rattachent: liquor,-oris m.: fluidite, et, au sens concret "liquide,
liqueur", liquidus: "clair, limpide, transparent, et "liquide" (la
double scansion liquor et liquor, liquidus et liquidus est dans Lucr.,
e.g. 4,1359 crassaque conueniant liquidis et liquida crassis', la
quantite longue, li^e a 1'ictus metrique, semble resulter d'une coupe
syllabique liq-uida qui a pour effet d’allonger la syllabe, non la
voyelle, cf. Havet, R.Phil .30 ,73sqq.; Vg. ne connait que liquor, liqui¬
dus); liquesco,-is: devenir liquide ou limpide; liquefacio,, liquefio:
liquefier, se liquefier; et les derives ou composes de ces formes:
liquiditas (tardif), liquidiusculus (Pl.), eliquescS (Varr.), lique¬
factis, etc.
Cf. aussi proliqueo (transerit proliceo): prol icere: emanare, ef¬
fluere. Varro: demum ubi prolicuit dulcis unda (doss. Isid.).
Liquare "filtrer" (cf. Coi.9,15,13 saccus quo uinum liquatur .) a
aussi le sens de "liquefier", cf. Plin.36,63 lapis liquatur igni. De
la liquatorium: filtre. Beaucoup de derives de liquo, attestes seu-
lement a 1 'epoque imperiale, n'ont plus que le sens de "liquide",
ainsi liquabilis: liquefiable; liquamen ( liquamentum) n.: liqueur;
en cuisine: sauce faite d'intestins de poissons liquefies, et ses
derives liquaminatus, liqudminarius, gl.'fxpanf6h\<i, liquaminosus: juteux,
liqudrius: qui concerne les liquides, liquatio: fonte, fusion. Com¬
poses: deliquo,-ds (depuis Varron); eliquo et eliquium (cf. linquo),
eliquatio; reliquo (Orib.).
A la meme famille s'apparentent elices, lixa, Wlixus, prolixus,
v. lix, lixa; et aussi les formes du type colliciae , qui dans le sen-
timent populaire se sont confondues avec les formes derivees de lacio
du type Slicius; v. lax et colliciae. - Liquare, liquidus ont subsiste
dans quelques dialectes italiens, M.L.5076,5077; liquiddre en roumain,
M.L.5076a; dSliquare, dans quelques dialectes romans, id.3543,353C.Iri.
lechdach "liquida" (scii, consonans), mot savant.
La rapprochement avec iri .fliuch, v.gall. gulip "humide" est me¬
diocre pour le sens. Celui avec persan rextan "verser" est plus sa-
tisfaisant; comme ce mot persan est inseparable de av. raeSayeiti "il
laisse", il en resuite que liqueo serait un verbe d'etat appartenantala
racine de linquS et que liquor serait a rapprocher de gr. XetTCOfiai,; la racine.
de linquo, qui a eu plusieurs developpements de sens divergents,
aurait fourni des mots signifiant "etre en 4 tat de laisser aller,
en etat liquide". Le -s- dans lixa, lixus est de meme type que dans
laxus, etc.
Cf. peut-etre limpidus.
llquis: v. obiTquus.
lira, -ae f.: billon (t. d' agri culture). Mot campagnard, cf. Coi.
3,4,0, liras rustici uocant easdem porcas, cum sic aratum est ut inter
duos latius distantes sulcos cumulus siccam sedem frumentis praebeat.
```


## [2026-09-06T23:13:19.699Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for l in 182 1362 5485 8959 9562; do echo \"--- HUB line $l\"; sed -n \"$((l-4)),$((l+6))p\" HUB.txt; done"
}
```


### [2026-09-06T23:13:21.593Z] TOOL RESULT

```
--- HUB line 182
Zukost' (eigentl. Mischung -- Ragout) ZDMG, 46, 233
* Wegeq a fiir h sjehe unter Nr, 323,— 9 -
als LW. aus dem Phi. stimmen wiirde. Zu dm^y com-
mixtio, coitus ') vgl. fur^y *GIanz* neben afroxtan^ Wrzl.
ruk; gurSy Tlucht' neben gurextan^ Wrzl. rik. Die
von Horn angefuhrten Awestaformen gehoren schwer-
lich hierher, auch nicht das von Fr. Muller, WZKM.
5, 351 angezogene np. mezldan, pr. mBzam 'harnen*.
58. Np. avdra 'verloren, verwirrt, umherirrend' etc. gehort
kaum zu den WOrtern, die *Raub* bedeuten. Doch ist
ein persisches afXJinr *Raub' verbiirgt durch die Lehn-
--- HUB line 1362
'abstinence* GI. and Ind. 88, *Vorsicht* Yatk. i. Zar.
p. 62, Anm. 48, pClhredSnd *sie hiiten, pflegen ebenda
p. 51, Anm. 16. Von dieser Pehleviform fiihrt kein
Weg zu Fr. Muller' s (WZKM. 6, 185) zd. ^paiti-ra^d-
Verlassen*", dem doch nur np. *pairextan entsprechen
wiirde. — Arm. pahrez 'Fasten' ist einmal im 14. Jhd.
belegt.
310. Zd. pairika- schlechtweg durch *Hure' zu iibersetzen,
ist falsch. Die Pairika s sind Teufelinnen, die die
Frommen zu verfuhren und vom rechten Glauben ab-
wendig zu machen suchen; phi. parlk bose Fee'
--- HUB line 5485
lautgesetzUch aus.— 156 —
^vitara-y vgl. zd. mtara- *Brett'?, nach Darmesteter =
'allee' (oben p. 91), guddstan *passiren lassen , guSastan Vor-
ubergehen', phi. v(i)tartan, v(i)tartan to pass Gl. and Ind.
234, 235, ap. viyatarayama 'wir uberschritten' ; gurextan
*fliehen' = paz. varextan Miii. Gl. 207, von vi + Wzl. ric;
giizandj gazand ^) *Schaden* = paz. vazand Shk. 272, phi.
V'zand Bdh. Gl. 262, Gl. and Ind. 242 = ap. *vij[anti'?;
guzardan auseinander setzen, vollziehen, bezahlen , piiz. gu-
zaresn 'acquittance* (of sin) Min. GL 95, vazardan *to ex-
plain , vazaresn 'distinction, release* Shk. 272, phi. v(i)dartan
--- HUB line 8959
§ 145. Ap. X — idg. k vor Konsonanten = np. x\
a) xt — idg. kt; baxt 'Schicksal, Gluck' = zd. baxta-j
skr. bhakta-; bcixtar H. 149; afroxtan *anzunden H. 94;
puxtan *kochen H. 285 ; taxtan laufen, laufen lassen H. 368 ;
diixtar 'Tochter, zd. duydar-, skr. duhitar-; rextan aus-
giessen H. 638 u. s. w. Ap. xt wird im Np. zu ft in juft
*6enosse, Paar = phi. juxt, zd. yuxta-, arm. LW. juxtak;
bediixt = hehift *die Venus* (Stern). Umgekehrt taxtan fiir
taftan H. 372.
Die armenischen Lehnworter zeigen gleichfalls xt
{baxt 'Schicksal', duxt 'Tochter u. s. w.), das aber in einigen
--- HUB line 9562
i) Dagegen wird br = ap. br {wr) und hr = ap. d^*' nicht
umgestellt: abr 'Wolke* = zd. awra-; sahr 'Stadt' =
ap. xsad^'a- u. s. w. Nur einmal ist hr in rh umgestellt
in dem etyraologisch unerklarten parhextan sich ent-
halten = paz. pah(a)rextan Shk. 262 , phi. pdhrextan
(oben p. 40), arm. pahrEz 'Fasten*, vielleicht mit An-
lehnung an die WOrter, welche mit par- anfangen.
Ueber hi aus rt und r& (= iran. rd^ und rs) s. § 89,
97, 102.
Die iibrigen Lautgruppen, bestehend aus r mit fol-
gendem Konsonanten, bleiben: marr/ *Mann ^^ ap. war%a- ;
```


## [2026-09-06T23:13:50.636Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FFD ریختن\"; grep -n \"ریختن\\|گریختن\\|پرهیختن\" incoming/FFD/FFD_pages.txt | head -20; echo \"=== SNS\"; grep -n \"rextan\\|rēxtan\\|pahrēz\\|pahrez\\|wirēxt\" SNS_pages.txt SNS.txt | head -20"
}
```


### [2026-09-06T23:13:50.701Z] TOOL RESULT

```
=== FFD ریختن
1097:معنی به کار رفته‌اند: ۱-«غربال کردن»» ۲-«افشاندن»» «ریختن». در شاهنامه آمده است:
1099:بسی زر و گوهر همی ریختند زبر مشك و عنبر همی بیختند
1194:پرهیختن
1519:باستان 182: گریختن.
1548:ریختن
1554:«گریختن» هم از ريشةٌ له آمده است > گریختن.
1957:گریختن ۱
1960:جه به معنی «ترک کردن» است. (ریختن» از ریشةٌ انة7 آمده است + «ریختن».
2501:3 (ريشه - پاییدن) ۵۰ ۷۰ (ريشه < گریختن
2740:۱ 4 (ريشه - گریختن) ۵۵ ۵۶ (ایرانی باستان
2741:(4373788200)8 : (< داریوش) ۰۲۰ ۲۱ ۲۲ گریختن) ۵۵ ۵۶ (ایراتی
=== SNS
SNS.txt:7918:.il^j-l I* ,c^i\j» I* « jef*^ ly:pahrezlha: -^fi'l' 
SNS.txt:13247:.jaio :rextan: Vflft« 
SNS_pages.txt:5122:             .il^j-l I* ,c^i\j» I*    «   jef*^ ly:pahrezlha:        -^fi'l'                           I                                                                .i/^r^
SNS_pages.txt:9244:                                               .jaio :rextan:            Vflft« *
```


## [2026-09-06T23:13:52.456Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PLA\"; grep -n \"ibrīq\\|ibriq\\|Ibriq\\|abrīz\\|äbrez\\|abrez\" incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head -20; echo \"=== LKT\"; grep -n -i \"ibriq\\|abriz\\|eclipse\" LKT.txt | head -10; echo \"=== SKT eclipse/loan\"; grep -n -i \"^eclipse\\|^lend\\|^loan\\|^eleven\\|^twelve\\|^liquid\" SKT.txt | head -20"
}
```


### [2026-09-06T23:13:52.552Z] TOOL RESULT

```
=== PLA
=== LKT
=== SKT eclipse/loan
5749:Eleven.  (£.)  }A.%,  tnleutn.  A.S.  m^> lufon.  +  Du  *//,  Icel.  elliju,  DaJi.  tllet»u Swed.  tlfva,  Goth-  ainliu  G.  tij.  p.  The best  form  is  the  Goth.  ain'tif\  where  ain» one;  and  -/i/- Litbuan.  -lika  (in  vmdiUm, eleven).     Liih.  iika  meao*  '  rcmatning,*
10150:Lend ;  see  Loan.
10547:lend.  (£.)    The  fmal  d  ik M  E,  /fM^n.     A.  S  idMkiH^  10 /.i/i,  a  loan  (abwc).  +  lccl  /^mi, Dan.  iaam,  Irotn  ^i.»«  ;  Swed. /rm,  n  lief;  G.  Uhntn^  from  /rAis,^
```


## [2026-09-06T23:14:00.983Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for l in 1097 1194 1548 1957; do echo \"--- FFD line $l page:\"; awk -v L=$l 'NR<=L && /\\[pdf page/{p=$0} NR==L{print p}' incoming/FFD/FFD_pages.txt; done; echo \"=== FFD 1548 ctx\"; sed -n '1540,1575p' incoming/FFD/FFD_pages.txt; echo \"=== FFD 1190-1200\"; sed -n '1188,1205p' incoming/FFD/FFD_pages.txt"
}
```


## [2026-09-06T23:14:02.399Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for l in 5122 9244; do echo \"--- SNS line $l page:\"; awk -v L=$l 'NR<=L && /\\[pdf page/{p=$0} NR==L{print p}' SNS_pages.txt; done; sed -n '9240,9250p' SNS_pages.txt; echo \"=== PLA arabic\"; grep -n \"ابريق\\|إبريق\\|آبريز\" incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head"
}
```


### [2026-09-06T23:14:03.834Z] TOOL RESULT

```
--- FFD line 1097 page:
[pdf page 44]
--- FFD line 1194 page:
[pdf page 47]
--- FFD line 1548 page:
[pdf page 62]
--- FFD line 1957 page:
[pdf page 77]
=== FFD 1548 ctx
[pdf page 62]
ماده‌های ماضی و مضارع فارسی دری سا ی ۵۷
اصلی 78۶ است» ۳ پیش از 1به ] بدل شده است.
رو < فارسی میانه 127۷ + ایرانی باستان ۲۵0-2*. برای 2 > آرای. ريشهٌ 780 به معنی
«حرکت کردن» است» چون 37 , 3820422 به معنی «حرکت کردن به سوی متکلم» است.
«رفتن» بط «دورشدن از متکلم» اختصاص پافته است.
روفتن
روب + فارسی میانه 30
ریختن
ریخت < فارسی میانه 7870 + ایرانی باستان 7۵۳1۵*. برای 1۵ > آراست. 7211
صورت اصلی 78 است» تا پیش از + به #بدل شده است. ريشةٌ 7 به معنی
«ترک‌کردن» است.
ریز + فارسی میانه 782 < ایرانی باستان 6-۵ز۲۵*. برای 2 > آرای. 5 به جای 3 آمده
است.
«گریختن» هم از ريشةٌ له آمده است > گریختن.
ریدن
رید + فارسی میانه 710.
ری < فارسی میانه 717
زادن
زاد < فارسی میانه 734 < ایرانی باستان 22-18*. برای 1۵ > آراست. 23 صورت
ضعیف ريشةٌ 227 است به معنی «زادن».
زای < فارسی میانه 237 < ایرانی باستان 22-72*. 8 نشانه‌ای بوده که برای ساختن
مادهٌ مجهول از ريشه به کار می‌رفته است.
[pdf page 63]
ها فعلهای فارسی دری
زدن
زد < فارسی میانه 240 + ایرانی باستان ۵-12[*. برای ۵ > آراست. 3[صورت
: ضعیف 20[ است» به معنی «زدل).
زن < فارسی میانه 227 < ایرانی باستان «۵[*. به 48[ چیزی برای ساختن مادهٌ
مضارع افزوده نشده است > اوژدن.
زدودن
زدود < ایرانی باستان ۶2-43-12 برای 1۵ -> آراست. ۳۶ پیشوند فعلی است. ريشهٌ
تا به معنی «پاک کردن» است.
زدای + ایرانی باستان 8ر12-437-2* 22 برای ساختن مادهٌ مضارع از ريشه به کار
می‌رفته است. 413۷ صورت بالانده و ۵5 صورت ضعیف ريشةٌ 4۵۷ هستند > اندودن.
زیستن
=== FFD 1190-1200
برای ساختن مادهٌ آغازی از ريشه به کار می‌رفته است.078 ريشه است, به معنی «پرسیدن».
پروردن
پرورد ج فارسی میانه 40 << ایرانی باستان 02۳-۵-[۳۵7*. برای 13 -> آراست.
1 پیشوند فعلی است. ريشهٌ 7 به معنی «حمل کردن» است. «آوردن» و «بردن» هم از
ريشهٌ ۳27 آمده‌اند.
پرور < فارسی میانه 0278۷27 < ایرانی باستان 271-027-8م۴. برای 8 > آرای.
پرهیختن
پرهیز < فار سی میانه 020762 < ایرانی باستان 812-28د027۵*, 271۳۵212-8 *. برای
2 آرای, علقبه معتی «پاییدن» است و با پیشوند فعلی 2272 به معنی «دوری گزیدن» و
با پیشوند فعلی 8351 به معنی «خدمت کردن» است. 020782 جانشین 278787 و
027172 شده است.
پرهیخت < فارسی میانه 0287871 در فارسی میانهٌ مانوي 0287181 به عنوان ماضی
برای 2 * 02713812 به کار رفته است. 027871 به قیاس با 782 و 7381و مانندهایش
به وجود آمده است.
[pdf page 48]
ماده‌های ماضی و مضارع فارسی دری ‏ ی ۴۳
پژمردن
در پهلوی اشکانی ۰2۲ از ایرانی باستان ۹-2۵7-2*ء به معنی «پژمردن» آمده
```


### [2026-09-06T23:14:05.369Z] TOOL RESULT

```
--- SNS line 5122 page:

--- SNS line 9244 page:

rv                           li; .-.-jl-t fc.U «3'>                                                                             lAi   c^b «.b«jl,
                                                                                                                                                                                   rrr


                                               .jaio :rextan:            Vflft« *
                       ^tf-^ ra?cayat- j /raSc j<                :       fc-
nakti      /r§c    :                                                                                                                                •T/T»5    (p.31 n6.
                                   M/Y^ (fiffPE. 141)
                                        •


=== PLA arabic
```


## [2026-09-06T23:14:18.356Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1950,1975p' incoming/FFD/FFD_pages.txt; echo \"=== SNS leaf for line 9244\"; head -9244 SNS_pages.txt | grep -c $'\\f'; head -5122 SNS_pages.txt | grep -c $'\\f'"
}
```


### [2026-09-06T23:14:20.128Z] TOOL RESULT

```
گیر + فارسی میانه 8۲3 < ایرانی باستان 8۲8-72*. 72 نشانه‌ای بوده که برای ساختن
ماده از ريشه به کار می‌رفته است.
گروستن, گرویدن
گروست + فارسی میانه ۷۷07۲2۷۷181. ۱۷۷۵۳۷۷/۶1 مادةٌ ماضی جعلی از مادهٌ مضارع
است. «گروید» در فارسی دری مادهٌ ماضی جعلی است. از مادهٌ مضارع.
گرو + فارسی میانه ۷۷۵۶۶۷۷ + ایرانی باستان ۴۷۶۵۷ ۷۲ صورت ضعیف ريشةٌ
57 به معنی «گُزیدن) است. 1820 برای ساختن ماده مضارع از ريشه به کار می‌رفته است.
گریختن ۱
گریخت + فارسی میانه ۷۷788 + ایرانی باستان ۷۷1-۵0-1۵*. برای 18 -> آراست. ۷:1
پیشوند فعلی است. 7211 صورت اصلی 731 است» 1 پیش از 1 به تابدل شده است. ريشةٌ
جه به معنی «ترک کردن» است. (ریختن» از ریشةٌ انة7 آمده است + «ریختن».
گریز + فارسی میانه ۷762« ایرانی باستان ۷1-۵16-2*. برای ۵ -> آرای. ابه جای ۸
آمده است.
گریست < فارسی میانه افاولاع. 81اررزتع ماده مأضی جعلی است» از مادهٌ مضارع
ساخته شده است.
گری + فارسی میانه 1تع + فارسی باستان 8۲4-78* « ایرانی باستان 8۳۵2-78 *. 2
برای ساختن مادةٌ مضارع از ريشه به کار می‌رفته است. ريشهٌ 8792 به معنی «گله کردن»
[pdf page 78]
ماده‌های ماضی و مضارع قارسی دری ۷۳
است. «گله» فارسی دری از 81188 فارسی میانه آمده است و 8128 از 874-42* فارسی
باستان. 874 صورت ضعیف ريش 8۵74 / 8720 است. 218 پسوند بوده است.
۱ گزاردن
گزارد + فارسی میانه ۷12274 < ایرانی باستان 3۳-1۵.-۷*. برای ۵ -> آراست. ۷:۱
پیشوند فعلی است. لَن صورت بالاندةٌ ريشهٌ 27 به معنی «حرکت کردن» است.
«(چریدن) از ریشهٌ 47 آمده است > چریدن.
گزار < فارسی میانه ۷1237 < ایرانی باستان 2۲-۵.-۷۷*. برای 2 > آرای.
=== SNS leaf for line 9244
133
73
```


## [2026-09-06T23:14:37.861Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -c $'\\f' SNS_pages.txt; echo \"--- leaf 134\"; awk 'BEGIN{RS=\"\\f\"} NR==134' SNS_pages.txt | head -20; echo \"--- leaf 74\"; awk 'BEGIN{RS=\"\\f\"} NR==74' SNS_pages.txt | head -8"
}
```


## [2026-09-06T23:14:39.345Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AFM abriq entries\"; grep -n \"ابريق\" AFM_pages.txt | head; echo \"=== IEC leikw\"; grep -n \"leiq\\|liqu\" IEC.txt | head -20"
}
```


### [2026-09-06T23:14:39.480Z] TOOL RESULT

```
242
--- leaf 134
rv                           li; .-.-jl-t fc.U «3'>                                                                             lAi   c^b «.b«jl,
                                                                                                                                                                                   rrr


                                               .jaio :rextan:            Vflft« *
                       ^tf-^ ra?cayat- j /raSc j<                :       fc-
nakti      /r§c    :                                                                                                                                •T/T»5    (p.31 n6.
                                   M/Y^ (fiffPE. 141)
                                        •




                                                                                         aMtaam-:^          (i^ww^^
                                                                                          WtoJto*. ii, 4fi)VMj|fc &»«.
                                                                                                                               U :amag/araah:



                                                                                                                       167 (^UcJU,
--- leaf 74
 116                                      U. ..-vL: *-L *;L



(P'erfcum.       phryz: J** {GNPE. 68) paiti+ /raec                          I


                         .(jjo-yif)          pahariz       :
```


### [2026-09-06T23:14:39.539Z] TOOL RESULT

```
=== AFM abriq entries
5433:(5١ نمه‎ابريق "
5689:ابريق ܪ
=== IEC leikw
191:nsg. nominative singular obl. oblique -
457:alm- (?) ‘rot, impurity’ MHG elm “yellow clay’; LG olm (-o- for -a-) ‘rotten wood’; Lith. alme ‘liquor from dung’
772:ati-liqutos (at-) ‘left’. Cf. leiqu-, loiqu-, liqu- tos and next Skt. áti-riktah; Li. atliktas; Latv. atlikts, beside atlika “remainder”
773:ati-loiquos (at-) “remainder, surplus'. Cf. leiqu-, loiqu-, liqu-, etc. Skt. atirekah; OCS otülékü; Li. átlaikas; Latv. atliekas (f.pl.). (The Irish form athlaoch “aged person, veteran', though isophonic, is of dif- ferent origin)
827:ausis (ousis, usis) ‘ear; pot-handle'. WP I, 18 Av. (dual) uši; Ober, u31; Arm. unkn, unkan, -amb (dual or dim. ?) beside unkunk (a plural or dual form: *pot-handle); Hitt. cf. ehuratius /(ear-stoppers'; Myc. & Gk. cpds. Owes, -oes *-eared'; Gk. os, gs. otós (oblique forms unexplained); cf. lag-oós ‘hare’, Alb. vesh, pl. veshë (fear, beside vath ‘earring’, fr. *ausoKo- (?)); Lat. auris, gp. aurium; Olr. áu, o Go. auso (n-stem); OHG ora, MHG Ore, Or beside ære “eye of needle, eyehole'; OE čare; ON eyra; OCS uši (dual) beside uxo, gs. ušese; Li. ausis, gp. ausi; Latv. auss, gp. ausu
988:brotos ‘red liquid" (?) Gk. brótos ‘gore’; Cz. broť "red sap, woad’; Srb. broé "madder" cf. Cz. brotit, Pol. broczyc *bespatter w. blood'. (The Slav evidence is ambig., cf. bhrakt- in view of OCS brosti ‘purple dye’ & Ir. bracht 'sap")
2297:diu-, diuos, om (diu-) ‘sky, day’ (oblique theme of diéus, q.v.) Skt. div, den, divám; Arm. tiv; Oss. cf. äv- diu, -deu Cdol Ger. Ab-gott); Hiero-Hitt. Tiwa-; Myc. diwe(i) (dat. sg. ‘to Zeus’; Diwo-, Diwija (names); Gk. cf. eu-día, én-dios; dia (a goddess); Alb. cf. dívet “it dawns’; Lat. dium, OLat. diu “in the daytime'; Lat. cf. also bi-duum, sub-dio, -di1ü; Ir. in-diu ‘today’; dia, gs dæ “god; day”; W dyw ‘day’; OW cf. diew “days”; cf. W he-ddiw ‘today’; Br. hé-ziu, id.; Cor. dew-, dæ-, cpds. ‘day’; OE Tīw ‘Mars’:
3455:eĝ- (2), £e (26) (sentence particle) “and, also, but, that”, etc. WP I, 542 Arm. cf. z- (acc. and oblique introductory par- ticle); zi, cj. 'that'; Alb. edhe, dhe “and, also’; Gk. (ambig.) ge, -ge; Oss. cf. äz- (intens. px.); (OCz. ež, Ze, cj. “that” indicates non-palatal *-g-)
3812:-er (alternating with oblique -n-, a collec- tive neuter extn.) Cf. Skt. vádh-ar ‘missile’; Arm. (Gear, (Sean ‘donkeys’, orear, orean ‘the nobility’; Hitt. ēdri, ēccan “eatables?; ON ætr, adj. “eatable”; átan “food; Hitt. watar, gs. wetenas ‘water’: OE wæter: ON vatn ‘water’; Gk. édar “eat- ables’; elar ‘shelter; MIr. cendar ‘heads’;
4822:ghór- ‘outflow, liquid filth, slurry, gore, pus’. Cf. ghur- Gk. cf. i-khór ('gore, pus, serum’, fr. *uis- ghor-, see uis-); Br. gor ‘abscess’; W gôr ‘pus’; G Guhr ‘slurry; manure’
5393:gurütos (2) ‘teeming, thriving’. Same as (1)? WP I, 685 Gk. brütos, on ‘fermer ted liquor’; brútea, npl. ‘lees’; cf. brüsis, f. (^welling-up'. Vbl. n. to next); W brid, pl. iau, m. ‘eruption; scab’ (?), but cf. bhrütos (1) & (2). (Isophonic: MHG krüt ‘herb’, qua *gurütóm)
5606:&eguer- (?) (an ambig. formula, cf. geger-) Skt. jagalah (adj. ‘fraudulent’; m. “a liquor’); Oss. záqgàr ‘harsh’; G cf. keck ‘downright; gay; sound, firn?
5959:Av. 2900. -áh- ‘buttocks’; Arm. dzet, o-st ‘tail’; Phryg. cf. zétna ‘gateway’; Gk. cf. s-khedón ‘nearly’; s-khédios “close; sudden’; khed-ropà (“pulse”, lit. “hanging tails"); o-gde in khódanos "seat Ir. gead ‘buttock’ beside giodar ‘liquid dung; sour milk’; n-dea-ghaid Caiter", prp.); Go. gatwo (lane, lit. *passage"); OHG gaz7a, ON gata, id.; OE geat, n. “opening, gate’; (Go in) OCS zadü ‘back’; uncertainly R-gde in Gk. kházomai *yield, flee'
6012:£hes-, variant of type ies- ‘ferment’, q. v. WP I, 601 Alb. djathë, n. (‘cheese’, fr. *&hesd-, or fr. *&heKito- by assim. from a type *&hesto-); ON gerð ‘yeast, ferment’ beside MLG gëst, Du. gist ‘yeast and OE gist, id.; Norw. gjest, id. Extns. in MHG gischen v. (‘froth’, fr. *&hes- sko); G Gischt, LG gäscht, m. (‘frotb’, fr. *Sheskito-). Simplex in OHG gësan, géron *ferment'; Sw. gása beside Norw. gjære, v. 1d.; gjær ‘barm’; Du. gier, Fris. jarre liquid manu- re
6117:9heu-, 8heumn-, £huuo, etc. Skt. havab ‘sacrifice’; Arm. cf. (e-gde) dzev, o-st. ‘shape’; Myc. -kowa (in a cpd. epithet of *oil); Gk. khóos, khoüs “liquid measure, dyke, mound’; khoé *outpour'; cf. also khóo, khónü- mi 'pile up'
6157:ehut-, radical extn. of type ghu-, see ĝhuuð, 8heuó, cf. &hütis in Skt. hutih ‘sacrifice’; Av. a-züitis "libation; Myc. cf. (queried) e(n)- kusewe ‘funnels’; Gk. khüsis ‘pouring, melt- ing, liquid’; OLat. fütis, f. ewer Li. Zütis, f. end. death’. For *&hutlo-, *&hutil-: Av. cf. u(s)zui6ya- *welling-up'; Gk. khütlon, khutla ‘fluid’; Lat. cf. fütile *sacrifical vessel; Umb. cf. ficla (equated in a parallel text w. sopa- *sacrifical liquor'; a LW in Lat. fitilla. For IE *-ü- > Umb. -i- cf pir "Drei MHG goder ‘vortex’, represents a form *$hutros
6158:$hutós ‘poured, cast, libated; liquid, liba- tion’. Cf. &hu-, $huuó, etc. Skt. hutáh "libated'; hutám ‘offering’; Arm. (?) dzu, gs dzvo, o-st. “egg? (isophonic only. Se- mantics obscure); Gk. khutós (cast; s. "mound Myc. kut-; Lat. futum ‘sprinkler’; Umb. cf. hufie ‘to a certain god'; Go. gup, OE god, ON guð ('god', and com. Gmo.); Li. fütas *perished'
6169:‘thus’ Skt. id “indeed, even’; Gk. cf. na-í (‘yes’, lit. ‘behold that’); Arm. (?) z-, zn- (an oblique px.); Lat. id; MIr. ed, Ir. eadh; OHG iz; LG cf. it-sig ‘the selfsame’; OLi. cf. id-afit “in order that’; Gk. cf. also ka-í (&and', if for *km-id). Extn. in Skt. idám: Lat. idem
6558:iüs "boiling; decoction, broth". WP I, 199 Skt. yüh, yus, yüsab; Per. jus (£-); Lat. jus, gs jüris; Ir. cf. úsc, m. (juice, fat”? contamination with uisge water: W cf. is-gell ‘soup, brine’; MHG jūs ‘snack’; G Jause ‘teatime’; Du. cf. jeu ‘gravy’; Icel. (?) yra, i-st. (drop, stew’. Am- big. cf. ür-); OCS juxa ‘soup’; Cz. jícha, Slo- vak jücha ‘brew, broth, slops'; R uxà *fish- soup’; Li. jūšē (“thick soup, fish-soup'. -$- for -s-? See las- drip) (A Slavonic origin for Jause is posited by FK: EWDS, cf. R üZin 'sup- per’, but a LW fr. SI. is also claimed for G Jau- che ‘liquid filth’)
6879:kauKos, à, io “shell, skull, bowl, cup’. Cf. kaukolos, etc. WP II, 548-551 Skt. kosah “shell, cup, pail, box, cask’; kośam, id.; cf. koSika, kausika ‘goblet; case? (dim.); Per. cf. kofče (Cladie'. LW in R kovš, id.); Oss. küsi, id.; Gk. (gloss) kaükos ‘cup’; Kaka ‘skull’; kaukíon, dim. ‘cup’; Maced. kausia ‘felt hat worn by kings’; Lat. caucum (LW? as Gk. kaükos); MIr. coach Ir. cuach “bowl, cup’; W cawg ‘dish’; ON hauss ‘skull’; Du. (?) hauw ‘siliqua, poď’; Li. kiáušas ‘skull, cup made from a skull, shell; dial. kaušas ‘ladle, Skull; kiáušē, f. *skull; kiaušis, io, m. ‘egg’;
```


## [2026-09-06T23:14:50.071Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"--- SNS leaf 73\"; awk 'BEGIN{RS=\"\\f\"} NR==73' SNS_pages.txt | head -12; echo \"=== IEC leiqu lemma\"; grep -n \"^leiquo\\|^leiqu\\| leiqu- \\|liqutos\\|loiquos ‘\" IEC.txt | head -20"
}
```


## [2026-09-06T23:14:51.353Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for l in 5433 5689; do echo \"--- AFM_pages line $l, leaf:\"; head -$l AFM_pages.txt | grep -c $'\\f'; done; echo \"--- AFM leaf around p6\"; awk 'BEGIN{RS=\"\\f\"} NR==20' AFM_pages.txt | head -20"
}
```


### [2026-09-06T23:14:51.855Z] TOOL RESULT

```
--- SNS leaf 73
                      **•   A*U 4 y>
                                                                                                    U**^U_«,1>mL
                                                                                                                                                  MT
               •&*'*•• :m5h:           ByRH            _u V|
                                              :   >»
m^h
      YJ>   ^ ^t^   Va„.        in,      57,142)




                                                                   <"-.*a».II,48)bys> Z :^                4iW        .   914)baSsaza-         _~
=== IEC leiqu lemma
772:ati-liqutos (at-) ‘left’. Cf. leiqu-, loiqu-, liqu- tos and next Skt. áti-riktah; Li. atliktas; Latv. atlikts, beside atlika “remainder”
9608:leiquo “leave, let, allow, remain”. Cf. liquos, loiquos, liqutos. WP II, 396 Skt. recàmi 'evacuate, leave’; Av. (radical) rič-, id.; Myc. leiq-, Gk. leípo, aor. élipon, id.; Arm. lkem, id.; Tokh. A cf. lek, adj. "dis, tant, apart”; Lat. cf. liqui, pf. ‘I left; MIr. lei- cim, Olr. lécim, id.; Go. leihvan ‘lend’; OE leon, MHG liben, liuhen, sv. 1. id.; ON ljá, le, wv ‘lend, grant’; OLi. liekmi, 3s li&kti, inf. likti, pf. likaü, pp liktas "leave; remain'; Li. Deko 1sg. id.; Latv. cf. lieks ‘superfluous’; Ir. cf. léic, f. ‘neglect. See next
9609:leiqusos, is "left, remaining; surplus, neglect, rejection’. Cf. liqusos, liqutós, linquo, leiquo, loiqu-. WP II, 396 Gk. leípsis, f. ‘desertion’; cf. leípsanon "re mainder’; Mir liach, adj. “sad; léic, f. ‘neglect, failing, weakness’; OCS lixü, m. ‘surplus’; 1150, lisiti, v. ‘deprive’; Cz. lichý “odd; reverse’; Srb. lih, wd R cf. liší “only”
9886:liquos ‘left’. Cf. liquno, linquó, leiquo, liqu- tos. WP II, 396 Arm. (ambig.) lik, id. (see liqutos); Gk. cf. lipo- pátor ‘deserting . . ?; Cret. cf. lissós (queried: ‘insolvent’, if for *liqusios); Lat. re-liquus, adj.; re-liquiae, fpl.; OLi. at-liküs ((remaining', beside Li. likes, f: likusi, id. Cf. also vienuo- lika, dvy-lika ‘11, 12" in relation to Go. etc. ain-lif, twa-lif, id. Long-gde in Li. lyka *odd number’; lykis, gs -io, m. (remainder?)
9887:liqutos “left, remaining’. Cf. liquos, etc. WP II, 396 Skt. riktáh “left; empty, destitute’; Arm. lik (*abandoned', but cf. liquos); Lat. cf. re-lictus “abandoned; remaining”; Gk. cf. apo-, ek-leip- téon “fit for leaving’; (the Gmc. forms OHG Iiban, bi-^; fir-leiben: OE læfan; and ON lifat (sic), pp. “left, remaining, fr. lifa, v. are am- biguous, perh. fr. *leip-, loip-, lip-, but cf. the phonol. of ‘seven, wolf); Li. liktas “left, remaining; likütis, usu. pl. liküciai ‘leavings, remains’. (Latv. likt ‘put; leave"; liktenis ‘fate’ is also ambig.)
```


### [2026-09-06T23:14:53.822Z] TOOL RESULT

```
--- AFM_pages line 5433, leaf:
178
--- AFM_pages line 5689, leaf:
181
--- AFM leaf around p6
:9 `
- من 9 3 ظاهر. والاصح انْ 45 3 13
الخمر والنمذ
(البدنوز): معرات كه بوذ وهو احتبيث ܝܘ
( البربط ) العود تعريب برت واصل معناه صدر ܐܠ( لاله يشبهة ٠‏ ومنة
اليونائي ومجمةامهة
* (البربيطاء ) الثياب معرب ܨ ܢܝܐ ومعناها الصدربة وهي ثاب يلسها
اللا ناك والنساء * على صدورهم
* ( الت ) بعنى الدليل مشتق من ب تو ومعناة الضياء
(البَرَنتَ ) السئ الخلق تعريب بَرتني ومعناه الغرور والعجب <
* 3 الإبريج ) 45 بها 5 السّمن منها < ابيز
واصل ܘܚܐܘ يصب الماء و يطآق على الدلو والسطل وغير ذلك
+ 5 سفيعة كيرة 512 ان = 7 95 عن اركاء 35
بلاط اللك والمضرب 50 وحطة الرحال اوعن بركرك اي قصر عال ٠او‏ الارجح
ܣ
05225 غرض في الهواء على رأس رمح او نوه فارسيتها برجاس ومعناما
هدف السهم ܬ اصل اللفظة يونالي 90
0 ( البرجس ( نم او هو الشتدى ويأتي يض ععنى الناقفة $
بر كيس وهو الشترى واصل معناه المتلى' سُعرا
١‏ ( اليِرْخْدَاة) المرأة التارّة الناععة معربة إما عن 'برخور ند اي الممتلى' 0
```


## [2026-09-06T23:15:07.896Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BQT ابریز/ابریق\"; grep -n \"آبریز\\|ابریق\\|آبریق\" BQT_v1_pages.txt | head -10; echo \"=== BQT گریختن/پرهیز\"; grep -n \"پرهیز\\|گریختن\" BQT_v1_pages.txt BQT_v2_pages.txt | head -10"
}
```


### [2026-09-06T23:15:07.974Z] TOOL RESULT

```
=== BQT ابریز/ابریق
6084:بیمنی ابریق و آفتابه و مطهرء ومانند آن
6090:که‌آفتابه وابریق (۳) باشد .
=== BQT گریختن/پرهیز
BQT_v1_pages.txt:7725:هست ۵ -وپرهیزکار را نی زکویند.
BQT_v1_pages.txt:10388:وشین فرشت و دال ابجد بر وزن پرهیز کار ؛
BQT_v1_pages.txt:11418:از کان است که مردم کاهل و باطل و مهمل | و زبرك و عاقل باشد - و مردم پرهیزکار را نیز
BQT_v1_pages.txt:15412:خس‌وانی : چه حابه زاعد پرهیز کار صومعگی
BQT_v1_pages.txt:18901:که کتامه از گریختن باشد
BQT_v1_pages.txt:23106:یدسا «بارابع بالف کنیده. پرهیز کار
BQT_v1_pages.txt:23743:ورفتن - و گریختن - وجان کندن باشد.
BQT_v1_pages.txt:23872:و طلاق دادنرا یز گویند - و بمعنی گریختن
BQT_v1_pages.txt:25858:ورو ردان شدن و گریختن باشد .
BQT_v1_pages.txt:30550:پرهیزنکند ومردم ازونفرت کنندلا .
```


## [2026-09-06T23:15:09.368Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== ARY ریختن\"; grep -n \"ریختن\\|گریختن\" incoming/ARY/ARY_pages.txt | head -10; echo \"=== ARY latin index\"; grep -n -i \"RIKHTAN\\|GURIKHTAN\\|LEIKW\\|RIZ\" incoming/ARY/ARY_latin_index_pages.txt | head -10"
}
```


### [2026-09-06T23:15:09.428Z] TOOL RESULT

```
=== ARY ریختن
10092:آریختن" و آنابرد کردن" شده است. ۱
12876:بازگشت به؛ ریختن.
=== ARY latin index
4015:Riz)
4113:Nos (SLOVAK) |e NARIZ, SPANISH) plays
4116:NARIZ (PORTUGUESE) gis »
4395:PARADISO (ITALIAN) gidts\ PRES, PARIZ KURDISH) (53,5
6669:(THORN) 136, (HEDGEHOG) 163 ERIZO H(SPANISH)  gliteel
7769:DALA, DALY sQWELSH) 55 DIRIZH (KURDISH) 535°
10698:DRIZEHAN THRAYADATH
13184:‘LIVRIZ :(BRETON) gis » LAM NORWEGIAN) (35 5
```


## [2026-09-06T23:15:18.881Z] TOOL CALL #62: Bash

```json
{
 "command": "head -40 tools/fetch_source.py"
}
```


### [2026-09-06T23:15:18.916Z] TOOL RESULT

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
```


## [2026-09-06T23:15:20.326Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '6078,6095p' BQT_v1_pages.txt; echo \"--- leaf\"; head -6084 BQT_v1_pages.txt | grep -c $'\\f'; echo \"=== ARY 10088\"; sed -n '10085,10098p' incoming/ARY/ARY_pages.txt"
}
```


### [2026-09-06T23:15:22.367Z] TOOL RESULT

```
۵ آپ دزد رك : فطره دژد .آب ست
آب دست ب بر وژن‌خاربست , امستجا
کردن بآب - و وضو ساختن بائد - و زاهد
پاکدامن را نیز گوبند - و کارکری را حم
گفته‌انه که دست ار درکارها با طراوت باشد ۷ .
آب دستان بر وژن آب دندان »
بیمنی ابریق و آفتابه و مطهرء ومانند آن
باشث .
ب‌دهتان شاد ه بمنی آقابدار.
وترکانآختابهچی (۱) کونند .
آب دست دذان <- با دال ابچد
بالف (۲) کشده‌وبنون‌زده ۰ بعضی آب دستادست
که‌آفتابه وابریق (۳) باشد .
آب دسد‌ان با دال اسجد . بروزن
ی هت که و ار ما
آن )4 باشد .
آ ب ث فان - بسکون ثالث بر وزن
باریندان » حریف کول‌ومفت ومغلوب را گویشد»
--- leaf
210
=== ARY 10088
۲ ا_بِپژْز (به چم *طحال")
پسگشت‌ها ۰ کی 2 (811181,0) :22 ۸/۸02۷
. 6 (82111) +7 80/1 ۷
یادداشت: ون :
۱ چم این واژه در تخاری ۸ و 8: چالش کردن» سخت کوشیدن, 1
چم این واژه در گوتبک و بونانی: لوحه با صفحه‌ای چوبی؛ سپر چوبی. :
۲- چم اصلی این واژه آشکاش " و اُشّقه کردن" بوده است که در زبان‌های ژرمنی نوین تبدیل بُه "خونریزی" و
آریختن" و آنابرد کردن" شده است. ۱
,33300 سس
اوستایی (487۸۷): ای ترا ی ان بان ایرلندی کهن (لادلقا صاه): ان
پهلوی (1/اتلهه): ,857282 گالیک (لاقهه): ۳
سانسکریت (54۸/55/77). 7۸0
ارمنی (4748149۷): ۳۸۳۸۸۷ ۰ | پسگشت‌ها پیش دا
پرنانی 0368/0): 5 زر ری ۳
```


## [2026-09-06T23:15:32.000Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BQT v3 ریختن\"; grep -n \"ریختن\\|رخنن\\|ریزیدن\" incoming/BQT/BQT_v3_pages.txt | head -10; echo \"=== BQT v4 گریختن/پرهیز\"; grep -n \"گریختن\\|پرهیز \" incoming/BQT/BQT_v4_pages.txt | head -10"
}
```


### [2026-09-06T23:15:32.064Z] TOOL RESULT

```
=== BQT v3 ریختن
763:- وفروریختنآب وتراب و امثالآن باشدهمچو
5319:کریختن و هزیمت و شکت لشکر هم آمده
16711:بمعنی ریختن_ودردنوشکافتن_ویربشان‌وی را کنده
19275:ریختن ۰ فروخواندن , فرو کوفتن [ رك : دیباچة مولفص‌لد ] و نیز براسماء درآید : فروتن .
26986:درهم شدن؟۱- و درهم کردن - و گریختن‌باشد.
31225:است - و تولك و پرریختن جانوران پرنده را
31247:که ‎de SEE‏ و خانة علفی باشد - وپرریختن
31316:‎tee .‏ است ۷ - و بععنی پر ریختن جانوران
39394:‏کویستی ’- بنم‌اول‌بروزن بگریختن»
41236:‎gusto‏ - بفتح دال , گریختن - دورشدن ۰ رگ : گال .- خروشیدن » فرباد کردن :
=== BQT v4 گریختن/پرهیز
1056:تصحیف شده . ‎٩‏ - ابویحیی مالكین دینارصری از راوبان حدیث » مردی پرهیز کار بود
7392:آژین قبیل است : خشم - نا » ترس نا4 » درد نا » شرم- ناك » پشم - ناك » پرهیز - ناك»
7394:۳+ پسوند مفتی « که» 5 -: از ۶ پرهیز » اسم معنی 2« پرهیزنا > ساخته شده » سپس از آن
21067:شته مدعیانند از بمین و سار خدای راکه بپرهیز از باری چند .>
```


## [2026-09-06T23:15:37.176Z] TOOL CALL #65: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/leyk%CA%B7-\" \\\n \"https://en.wiktionary.org/wiki/%D8%B1%DB%8C%D8%AE%D8%AA%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%DA%AF%D8%B1%DB%8C%D8%AE%D8%AA%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D8%A5%D8%A8%D8%B1%D9%8A%D9%82\" \\\n \"https://en.wiktionary.org/wiki/%D9%83%D8%B3%D9%81\" \\\n \"https://www.etymonline.com/word/eclipse\" \\\n \"https://www.etymonline.com/word/liquid\" \\\n \"https://www.etymonline.com/word/eleven\" \\\n \"https://www.etymonline.com/word/loan\" ; do\n timeout 90 python3 tools/fetch_source.py \"$u\" --note \"page 307, root Leigh 2/Leikw\" 2>&1 | tail -2\ndone"
}
```


### [2026-09-06T23:15:43.565Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/5babb21711421a72.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8f50a6d77a93ae16.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/695d455f9e4f8795.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d86ae5e966356e7e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e99538c72b61e07c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/400a9d95d1001088.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f56e7fba0e7106b6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/87e0c6febaf0521c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0c7d3a77b1f76e1f.txt
```


## [2026-09-06T23:15:46.420Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"###### PIE leykw\"; sed -n '1,120p' 5babb21711421a72.txt | grep -v \"^$\" | head -70"
}
```


### [2026-09-06T23:15:48.106Z] TOOL RESULT

```
###### PIE leykw
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/leyk%CA%B7-
FETCHED: 2026-09-06T23:15:39Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/leykʷ- - Wiktionary, the free dictionary
Reconstruction:Proto-Indo-European/leykʷ- - Wiktionary, the free dictionary 
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
 Root 
 1.1.1 
 Derived terms 
 1.2 
 References 
 Toggle the table of contents 
 Reconstruction:Proto-Indo-European/ leykʷ- 
 Add languages 
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
```


## [2026-09-06T23:15:51.569Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 5babb21711421a72 8f50a6d77a93ae16 695d455f9e4f8795; do echo \"###### $f\"; grep -n -A25 \"^ Root $\\|^ Etymology\" $f | head -60; done"
}
```


### [2026-09-06T23:15:53.315Z] TOOL RESULT

```
###### 5babb21711421a72
ugrep: warning: 5babb21711421a72: No such file or directory
###### 8f50a6d77a93ae16
ugrep: warning: 8f50a6d77a93ae16: No such file or directory
###### 695d455f9e4f8795
ugrep: warning: 695d455f9e4f8795: No such file or directory
```


## [2026-09-06T23:15:55.913Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 5babb21711421a72.txt 8f50a6d77a93ae16.txt 695d455f9e4f8795.txt; do echo \"###### $f\"; awk '/Root|Etymology/{p=1} p' $f | sed -n '1,60p'; done"
}
```


### [2026-09-06T23:15:57.717Z] TOOL RESULT

```
###### 5babb21711421a72.txt
 Root 

 1.1.1 
 Derived terms 

 1.2 
 References 

 Toggle the table of contents 

 Reconstruction:Proto-Indo-European/ leykʷ- 

 Add languages 

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
###### 8f50a6d77a93ae16.txt
 Etymology 

 1.3 
 Pronunciation 

 1.4 
 Verb 

 1.4.1 
 Conjugation 

 1.4.2 
 Derived terms 

 1.5 
 References 

 Toggle the table of contents 

 ریختن 

 7 languages 

 فارسی 
 Français 
 Bahasa Indonesia 
 Kurdî 
 Malagasy 
 Русский 
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

###### 695d455f9e4f8795.txt
 Etymology 

 1.2 
 Pronunciation 

 1.3 
 Verb 

 1.3.1 
 Usage notes 

 1.3.2 
 Synonyms 

 1.3.3 
 Derived terms 

 1.4 
 References 

 Toggle the table of contents 

 گریختن 

 3 languages 

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
```


## [2026-09-06T23:16:03.309Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 5babb21711421a72.txt 8f50a6d77a93ae16.txt 695d455f9e4f8795.txt d86ae5e966356e7e.txt e99538c72b61e07c.txt; do echo \"###### $f\"; grep -n \"Proto-Iranian\\|Proto-Indo-Iranian\\|Borrowed from\\|Inherited from\\|From Middle Persian\\|Root\\b.*leyk\\|Cheung\\|Hasandust\\|MacKenzie\\|Ultimately\\|cognate\" $f | head -20; done"
}
```


### [2026-09-06T23:16:05.068Z] TOOL RESULT

```
###### 5babb21711421a72.txt
161: Proto-Indo-Iranian: *rayčáyati 
165: Proto-Iranian: *rayčáyati 
169: Proto-Indo-Iranian: *riktás ( see there for further descendants )
177: ⇒ Proto-Indo-Iranian: *ráyknas ( < *lóykʷ-n-es- ) ( see there for further descendants )
###### 8f50a6d77a93ae16.txt
159: Inherited from Middle Persian 𐭥𐭩𐭧𐭲𐭭 ( ʿyḥtn /⁠rēxtan⁠/ ) , from Proto-Iranian *Hraič- ( “ to pour; to flow ” ) , Northern Luri رختێ ( rextı ) , an Iranian-specific suffixed form of Proto-Indo-Iranian *HriHyáti ( “ to flow ” ) . [ 1 ] 
1045: ^ Cheung, Johnny ( 2007 ), Etymological Dictionary of the Iranian Verb (Leiden Indo-European Etymological Dictionary Series; 2), Leiden, Boston: Brill, →ISBN , page 187 
1051: Persian terms inherited from Proto-Iranian 
1052: Persian terms derived from Proto-Iranian 
1053: Persian terms derived from Proto-Indo-Iranian 
###### 695d455f9e4f8795.txt
150: From Middle Persian OLYKWN-tn', wlyhtn' ( wirēxtan ) , ultimately from Proto-Indo-European *wí ( “ apart ” ) + *leykʷ- ( “ to leave ” ) ; whence also ریختن ( rixtan , “ to pour ” ) . Cognate with Avestan 𐬬𐬌𐬭𐬁𐬈𐬗 ( virāec , “ leave away, run away ” ) , Gilaki وروتن ( vörütən ) (present stem وروج ( vörüj ) ).
###### d86ae5e966356e7e.txt
195: Borrowed from Middle Persian or Parthian *ābrēk possibly via Classical Syriac ܐܒܪܝܩܐ ( ʾaḇrēqā ) , attested as Classical Persian آبریز ( ābrēz ) from آب ( āb , “ water ” ) + the present stem of the verb ریختن ( rēxtan , “ to pour ” ) . Compare Northern Kurdish avrêjk ( “ ewer ” ) .
412: Cheung, Johnny ( 2017 ), On the (Middle) Iranian borrowings in Qurʾānic (and pre-Islamic) Arabic ‎ [1] , Leiden: Leiden University, pages 2–3 
438: Inherited from Arabic إِبْرِيق ( ʔibrīq ) .
473: Inherited from Arabic إِبْرِيق ( ʔibrīq ) .
###### e99538c72b61e07c.txt
```


## [2026-09-06T23:16:16.253Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"### leykw root\"; sed -n '120,200p' 5babb21711421a72.txt; echo \"### kasafa\"; grep -n -i \"Arabic\\|root\\|Semitic\\|eclipse\" e99538c72b61e07c.txt | head -30"
}
```


### [2026-09-06T23:16:16.313Z] TOOL RESULT

```
### leykw root

 move to sidebar 
 hide 

 From Wiktionary, the free dictionary

 This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.

 Proto-Indo-European
 [ edit ] 

 Root
 [ edit ] 

 *leykʷ- ( perfective ) [ 1 ] [ 2 ] [ 3 ] [ 4 ] 

 to leave 

 Derived terms
 [ edit ] 

 Terms derived from the Proto-Indo-European root *leykʷ- (53 c, 0 e) 

 *léykʷ-t ~ *likʷ-ént ( athematic root aorist ) [ 3 ] 

 *likʷ-é-t ( thematic root aorist ) [ 5 ] [ 6 ] [ 7 ] 

 *li-né-kʷ-ti ~ *li-n-kʷ-énti ( nasal-infix present ) [ 3 ] 

 *le-lóykʷ-e ~ *le-likʷ-ḗr ( stative ) [ 3 ] 

 *loykʷ-éye-ti ( causative ) [ 8 ] 
 Proto-Balto-Slavic: 
 Latvian: làicît 

 Lithuanian: laikýti 

 Old Prussian: laikūt 

 Proto-Germanic: *laigijaną ( see there for further descendants )

 Proto-Indo-Iranian: *rayčáyati 
 Proto-Indo-Aryan: *rayćáyati 
 Sanskrit: रेचयति ( recáyati , “ to evacuate, make empty ” ) 

 Proto-Iranian: *rayčáyati 
 Avestan: 𐬭𐬀𐬉𐬗𐬀𐬌𐬌𐬈𐬌𐬙𐬌 ( raēcaiie i ti ) 

 *likʷ-tó-s 
 Proto-Indo-Iranian: *riktás ( see there for further descendants )

 Proto-Italic: *liktos 
 Latin: lictus 

 *lóykʷ-n- ( “ inheritance, property left; lent land ” ) 
 ⇒ Proto-Germanic: *laihną ( < *lóykʷ-n-o-m ) ( see there for further descendants )

 ⇒ Proto-Indo-Iranian: *ráyknas ( < *lóykʷ-n-es- ) ( see there for further descendants )

 *loykʷ-ó-s 

 Unsorted formations 

 Sanskrit: रिक्थ ( rikthá ) , Sanskrit: ऋक्थ ( ṛktha ) 

 Balto-Slavic:
 Latvian: likt ( “ to lay, put ” ) , lieks ( “ superfluous, excessive ” ) 

 Lithuanian: likti ( “ to stay ” ) 

 Slavic:
 Russian: лишать ( lišatʹ , “ to deprive, rob, divest ” ) from *leykso-

 → Proto-Finnic: *liika ( “ excess ” ) ( see there for further descendants )

 Celtic:
 Pictish: 
 → Scottish Gaelic: dìleab [ 9 ] 

 References
 [ edit ] 
### kasafa
```


## [2026-09-06T23:16:27.850Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && wc -l e99538c72b61e07c.txt && head -20 e99538c72b61e07c.txt; echo \"=== etymonline eclipse\"; grep -n -i \"eclipse\" 400a9d95d1001088.txt | head -10; echo \"=== etymonline liquid\"; grep -n -i \"liquid (adj\\|wleik\\|leikw\\|to flow\" f56e7fba0e7106b6.txt | head -10; echo \"=== eleven\"; grep -n -i \"one left\\|ainlif\\|leikw\" 87e0c6febaf0521c.txt | head; echo \"=== loan\"; grep -n -i \"leikw\\|PIE root\\|to leave\" 0c7d3a77b1f76e1f.txt | head"
}
```


### [2026-09-06T23:16:27.934Z] TOOL RESULT

```
5 e99538c72b61e07c.txt
URL: https://en.wiktionary.org/wiki/%D9%83%D8%B3%D9%81
FETCHED: 2026-09-06T23:15:41Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found=== etymonline eclipse
1:URL: https://www.etymonline.com/word/eclipse
4:TITLE: Eclipse - Etymology, Origin & Meaning
6:Eclipse - Etymology, Origin & Meaning 
21: Origin and history of eclipse 
23: eclipse (n.) 
25: "interception or obscuration of the light of the sun, moon, or other heavenly body by the intervention of another heavenly body," c. 1300, from Old French eclipse "eclipse, darkness" (12c.), from Latin eclipsis , from Greek ekleipsis "an eclipse; an abandonment," literally "a failing, forsaking," from ekleipein "to forsake a usual place, fail to appear, be eclipsed," from ek "out" (see ex- ) + leipein "to leave" (from PIE root *leikw- "to leave"). Compare ellipsis , ecliptic .
29: eclipse (v.) 
31: late 13c., "to cause an eclipse of," from Old French eclipser , from eclipse (see eclipse (n.)).Figurative use from 1570s. Also in Middle English in an intransitive sense "to suffer an eclipse," now obsolete. Related: Eclipsed ; eclipsing .
35: Entries linking to eclipse 
39: "the circle in the sky followed by the Sun," late 14c., from Medieval Latin ecliptica , from Late Latin (linea) ecliptica , from Greek ekliptikos "of an eclipse" (see eclipse (n.)). So called because eclipses happen only when the Moon is near the line. Related: Ecliptical .
=== etymonline liquid
56: liquid (adj.) 
58: late 14c., "flowing, capable of flowing; neither solid nor gaseous," from Old French liquide "liquid, running" (13c.), from Latin liquidus "fluid, liquid, moist," figuratively "flowing, continuing," also of sounds and voices, from liquere "be fluid," related to liqui "to melt, flow," from PIE *wleik- "to flow, run."
65: "a liquid substance," 1708, from liquid (adj.). Earlier it meant "sound of a liquid consonant" (1520s), following Latin liquidae , Greek hygra , applied to letters of an easy, "flowing" sound.
72: 1756, in chemistry, "melt or dissolve gradually, become liquid by absorbing moisture from the air," from Latin deliquescere "to melt away," from de- (see de- ) + liquescere "to melt," from liquere "to be liquid" (see liquid (adj.)). Transferred or figurative meaning "to melt away" is by 1858.
76: 1791, in chemistry, "liquefying in air," from Latin deliquescentem (nominative deliquescens ), present participle of deliquescere "to melt away," from de- (see de- ) + liquescere "to melt," from liquere "to be liquid" (see liquid (adj.)). Transferred or figurative sense of "apt to dissolve or melt away" is by 1837. Related: Deliquescence .
=== eleven
25: "1 more than ten; the number which is one more than ten; a symbol representing this number;" c. 1200, elleovene , from Old English enleofan , endleofan , literally "one left" (over ten), from Proto-Germanic *ainlif- (compare Old Saxon elleban , Old Frisian andlova , Dutch elf , Old High German einlif , German elf , Old Norse ellifu , Gothic ainlif ), a compound of *ain "one" (see one ) + from PIE root *leikw- "to leave."
54: "1 more than eleven, twice six; the number which is one more than eleven; a symbol representing this number;" Old English twelf "twelve," literally "two left" (over ten), from Proto-Germanic *twa-lif- , a compound of *twa- (from PIE root *dwo- "two") + *lif- (from PIE root *leikw- "to leave").
61: *leikw- 
=== loan
25: late 12c., "that which is lent or owning, a thing furnished on promise of future return," also "a gift or reward from a superior, a gift of God," from Old Norse lan "loan," from Proto-Germanic *laikhwniz (source also of Old Frisian len "thing lent," Middle Dutch lene , Dutch leen "loan, fief," Old High German lehan , German Lehn "fief, feudal tenure"), originally "to let have, to leave (to someone)," from PIE *loikw-nes- , suffixed form of root *leikw- "to leave."
54: *leikw-
```


## [2026-09-06T23:16:42.738Z] TOOL CALL #72: Bash

```json
{
 "command": "for u in \"https://en.wiktionary.org/wiki/%D9%83%D8%B3%D9%88%D9%81\" \"https://en.wiktionary.org/wiki/%D8%AE%D8%B3%D9%88%D9%81\" \"https://en.wiktionary.org/wiki/%D9%BE%D8%B1%D9%87%DB%8C%D8%B2\" \"https://en.wiktionary.org/wiki/%D9%83%D8%B3%D9%81%23Arabic\"; do timeout 90 python3 tools/fetch_source.py \"$u\" --note \"page 307, kosuf/parhiz check\" 2>&1 | tail -1; done"
}
```


## [2026-09-06T23:16:45.003Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== ARB كسوف\"; grep -n \"كسوف\\|كسف\" ARB_mo3rb.txt ARB_abdulraheem.txt | head -10; echo \"=== KFL\"; grep -n \"كسوف\" KFL.txt | head -5; echo \"=== FVQ kasafa\"; grep -n -i \"kusuf\\|kasaf\" FVQ.txt | head -5"
}
```


### [2026-09-06T23:16:47.382Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/776f85e10f6bab3f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8e9534c0ed7e4365.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/390ea53ee22aecbc.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/179ea45511ef8e37.txt
```


### [2026-09-06T23:16:47.454Z] TOOL RESULT

```
=== ARB كسوف
ARB_mo3rb.txt:14641:في يذكرأهن الاب : غلاف القمر يدخل فيه إذا كسف » ٠‏ وأنظر سان العرب ٠‏ والظاهى عتدى 
ARB_mo3rb.txt:36774:سنة 4٠م‏ ) طبعة كلية أ كسفو ورد يمطبة اليسوعبين سنة 15م 
=== KFL
=== FVQ kasafa
```


## [2026-09-06T23:16:50.626Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 776f85e10f6bab3f.txt 8e9534c0ed7e4365.txt 390ea53ee22aecbc.txt 179ea45511ef8e37.txt; do echo \"###### $f\"; head -5 $f; grep -n \"Etymology\\|From \\|Verbal noun\\|root\\|Arabic\" $f | sed -n '1,25p'; done"
}
```


### [2026-09-06T23:16:52.229Z] TOOL RESULT

```
###### 776f85e10f6bab3f.txt
URL: https://en.wiktionary.org/wiki/%D9%83%D8%B3%D9%88%D9%81
FETCHED: 2026-09-06T23:16:45Z
STATUS: 200
TITLE: كسوف - Wiktionary, the free dictionary

57: Arabic 
59: Toggle Arabic subsection 
62: Etymology 
139: From Wiktionary, the free dictionary
141: Arabic
144: Etymology
286: Categories : Arabic verbal nouns 
287: Arabic 2-syllable words 
288: Arabic terms with IPA pronunciation 
289: Arabic lemmas 
290: Arabic nouns 
291: Arabic masculine nouns 
293: Arabic nouns with basic triptote singular 
###### 8e9534c0ed7e4365.txt
URL: https://en.wiktionary.org/wiki/%D8%AE%D8%B3%D9%88%D9%81
FETCHED: 2026-09-06T23:16:46Z
STATUS: 200
TITLE: خسوف - Wiktionary, the free dictionary

57: Arabic 
59: Toggle Arabic subsection 
62: Etymology 
143: From Wiktionary, the free dictionary
145: Arabic
148: Etymology
289: Categories : Arabic verbal nouns 
290: Arabic 2-syllable words 
291: Arabic terms with IPA pronunciation 
292: Arabic lemmas 
293: Arabic nouns 
294: Arabic masculine nouns 
296: Arabic nouns with basic triptote singular 
###### 390ea53ee22aecbc.txt
URL: https://en.wiktionary.org/wiki/%D9%BE%D8%B1%D9%87%DB%8C%D8%B2
FETCHED: 2026-09-06T23:16:46Z
STATUS: 200
TITLE: پرهیز - Wiktionary, the free dictionary

65: Etymology 
85: Etymology 
166: From Wiktionary, the free dictionary
176: Etymology
232: Meninski, Franciszek à Mesgnien ( 1680 ), “ پرهیز ”, in Thesaurus linguarum orientalium, Turcicae, Arabicae, Persicae, praecipuas earum opes à Turcis peculiariter usurpatas continens, nimirum Lexicon Turkico-Arabico-Persicum ‎ [5] , Vienna, columns 799-800 
241: Etymology
244: From Middle Persian [script needed] ( pʾhlyc /⁠pahrēz⁠/ , “ defence; care ” ) . Compare Semnani پهریز ( pahriz ) . [ 1 ] 
###### 179ea45511ef8e37.txt
URL: https://en.wiktionary.org/wiki/%D9%83%D8%B3%D9%81%23Arabic
FETCHED: 2026-09-06T23:16:47Z
STATUS: -1
TITLE: 

1:URL: https://en.wiktionary.org/wiki/%D9%83%D8%B3%D9%81%23Arabic
```


## [2026-09-06T23:16:56.245Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '144,175p' 776f85e10f6bab3f.txt; echo \"-----خسوف\"; sed -n '148,175p' 8e9534c0ed7e4365.txt; echo \"-----پرهیز\"; sed -n '176,200p' 390ea53ee22aecbc.txt"
}
```


### [2026-09-06T23:16:56.311Z] TOOL RESULT

```
 Etymology
 [ edit ] 

 Derived from the verbal noun of كَسَفَ ( kasafa ) .

 Pronunciation
 [ edit ] 

 IPA ( key ) : /ku.suːf/ 

 Noun
 [ edit ] 

 كُسُوف • ( kusūf )  m 

 ( astronomy ) eclipse 

 ( astronomy ) solar eclipse 

 Declension
 [ edit ] 

 Declension of noun كُسُوف ( kusūf )

 singular

 basic singular triptote 

 indefinite

 definite

-----خسوف
 Etymology
 [ edit ] 

 Derived from the verbal noun of خَسَفَ ( ḵasafa ) .

 Pronunciation
 [ edit ] 

 IPA ( key ) : /xu.suːf/ 

 Noun
 [ edit ] 

 خُسُوف • ( ḵusūf )  m 

 ( astronomy ) lunar eclipse 

 Declension
 [ edit ] 

 Declension of noun خُسُوف ( ḵusūf )

 singular

 basic singular triptote 

 indefinite

-----پرهیز
 Etymology
 [ edit ] 

 Borrowed from Classical Persian پَرْهیزْ ( parhēz , “ abstinence, avoiding; diet, fasting ” ) , from Middle Persian [script needed] ( pʾhlyc /⁠pahrēz⁠/ , “ defence; care ” ) .

 Noun
 [ edit ] 

 پرهیز • ( perhiz ) ( definite accusative پرهیزی ( perhizi ) , plural پرهیزلر ( perhizler ) ) 

 abstinence , refrainment 
 Synonym: امساك ( imsâk ) 

 diet , dieting , regime 
 Synonyms: حمیه ( himye ) , دیه‌ت ( diyet ) 

 fasting 
 Synonyms: اوروج ( oruc ) , صوم ( savm ) 

 Derived terms
 [ edit ] 

 بیوك پرهیز ( büyük perhiz , “ Great Lent ” ) 
 پرهیز ایتمك ( perhiz etmek , “ to diet ” ) 
 پرهیز طوتمق ( perhiz tutmak , “ to fast ” )
```


## [2026-09-06T23:17:19.046Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && pdftoppm -f 307 -l 307 -r 200 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg307 && ls -la pg307.png"
}
```


### [2026-09-06T23:17:21.054Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 66772 Sep  6 19:17 pg307.png
```


## [2026-09-06T23:17:23.254Z] TOOL CALL #77: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg307.png"
}
```


### [2026-09-06T23:17:23.639Z] TOOL RESULT

```

```


## [2026-09-06T23:17:23.634Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T23:17:53.057Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT raeynah\"; grep -n \"raeynah\\|raeinah\\|raexnah\\|ra«?nah\" BRT.txt | head; echo \"=== BRT lines 24720-24745\"; sed -n '24720,24745p' BRT.txt; echo \"=== SOD entry 11\"; grep -n \"^ *11 \\|  11 [a-z]\" SOD_pages.txt | head -5"
}
```


### [2026-09-06T23:17:53.699Z] TOOL RESULT

```
=== BRT raeynah
=== BRT lines 24720-24745
KV.  10.  85,  32  und  Bthl.  IF.  10.  I.  —  Pa.: '
Buagetassen.  •
j.  vyähva:  s.  -..yam-,  |
•  j*  vy-us%'>  Inf,  'aufzuleuchten',  von  der' Morgenröte:  >rity&  xlaps  %raostavy  sa-\ layetü  (sd.)  "bei  der  Vollendung  der  dritten  I Nacht  sieht  man  die  Morgenröte  aufleuch-  \ ten"  H.  2. 7,  25.  ]
Zum  Ptaes.  14  des  V.  ^iiak-;  S  ^55.  s  e.  — Pü.:  pa  afii")  vicasisniAS)  saht),  erl.;  pa  uSiäm. —  0  Oder  auch  •sqm,  ».  lu  H.  a.  25,  — ")  Fehlt  H.  2.  7.  —  3)  'Beim  Sichtbarwerden', vgl.  lu  'vaÄ;  'had-  (V.  79.  «8:  ^äsnaoili)  und ifli-,  ai.  vicaksanä-  Adj.;  DsT.  ZA.  2.  269, 6S2.
•  j.  ..paoirjm  vatihatumca  /lata  "vranö.- ■     .  .  Vd.  20.
•  j.  raek-  V.  'linquerc'.  Praes.  8  irinak-, i6  (Des.)  irlrixsa-,  30  (Iter.)  raf'aya-; j-Aor.  I  raixs:  —  PFP.  'riiya-;  Inf. »rixti,  'ri^3;  AbsoL  'irixtfm.
1)  'freilassen,  freimachen';  a)  einen  Weg, Durchgang:  aal  ml  lam  . .  Auütm  Pisüm raiiaya  tarS  .  .  vUaauAaitSm  Yt.  5.  77; —  kuikptn  p7süm  raüayai  tarö  . .  Yt  5. 78.  b)  den  Wagen:  vas^m  . .  yat  dtm
dämSii  upamans  hu.irtxtim  (sd.) . .  trinaxH Yt/o.  68.  2)  'Jemandem  (Dat.)  etwas überlassen' :  saota  (sd.j  *anahaxtS  ■ .  dqhiStäi zao%Dm  raixiaiti  (3SK.)  N.  80.  3)  'im Stich  lassen,  dem  Verderben  preisgeben': ti  rasmanö  *ralcayeiti'''  .  .  mi^rS  Yt  10. 41.         a)  Des.  'dem  Verderben  preiszu-
geben wünschen':  yS  iiS  aiririünam  (sd.j irlrixsJiie gal'hanqm  (alsObj.)  Y.Ö5.  7;  7.
mit  ä;  s,  byärixti  Inf.
mit  paili  i)  'zuriicklassen':  äfs  uxz-a- zaiti  (sd.)  ä//  nivazaiti  äfs  paiti.raecayää ",  .  das  Wasser  lässt  (ihn)  zurück"  V.  j. 8'\  2)  'überlassen,  als  Erbgut  iiber- weisen'(?)3':  yezi  . .  pairijrihyät  cz-at  . . paUi.raicyat  (statt  "raj"")  Vd.  2.  3)  'im
Stich  lassen,  preisgeben':  ks  mthnm  aiwi.- druiaili  kS  rashäm  paiti.irinaxti  Yt  14^  4  7 ; —  mäca  tl  ihra  ,  .  astvatahe  arshSus  di- drizvö  pxsa  (sd.)  manahim  paiti  ragxfiia (»SOM.)  P.40;  —  yS  ..  manafnm  aßtäm paiti  *irinaxfi^''  P.  40.  3)  'unterlassen': s.  Inf.  'riqia.         S.  noch  PFP.
ai.  rinäili  linquit',  ririitali  (Gramm.),  tti-a- yali;  äraii : ariifi;  riiiäi;  mp.  n'x/(BTHt_  IF. /2.  im),  np,  reilan  'ausgiesaen'.  —  Pö.  (la a.So.  X.S):  Vinifxlil.  (luY.  6sy.  rii^üt, (zu  Vd.):  afii  hiilan,  |zu  P.):  afc  ränhüloji, apärenUan;  %.  noch  Inf.  Und  No.  z.  —  ')  So  - Sing.  -  mit  allen  besseren  Hd*.    NA.  yeinii.
—  ')  Näml.  auf  dem  Land,  indem  es  lOT&ck- weichl,  PüErl.;  fm  lüräi  apäc  snvU,  —  3)  Doch
]       s.  np.  murda  rig.     —    *)  Hds.  trinöisti,  d.  L nach  Dst.  "3=  pers.  sing,  futur  de  ere-nä"i
I»  j.  raekah-  n.  'Aufgeben,  Sichzurück- [ziehen  von  — ',  mit  Äaea  und  Abi.:  'i/f ml  haia  arihh  stmal  va?ihs  kirtnaoiti  "er bewirkt,  dass  es  für  mich  besser  ist,  mich von  der  Erde  zurückzuziehen"  VL  j-j.  30". Zum  V. /-flftt-.  —  np.  murda  reg  'Erbschaft'').
—  <)  Wörtl. :  decessum  meum  ex  hac  terra melius  facit  ". .  macht  er  zu  etwas  besserem"; vgl.  Dst.  ZA.  2.  604.   —    '>  S.  iBed.  raäf-
•  g.raexanah-n. 'Erbe,  Erbteil'",  in  escha- tologischem  Sinn,  von  dem  was  den  Gläu- bigen als  Lohn  bestimmt  ist'':  aauAlicä atthvascH  apayeilli^A.)  'nanks  vald>m  Y. 32. 11;  —  yBi  va^hsui  valdfnä  (sd.) manatgAS  .  .  °nä    aspSncU  .  .  caxrays{^)
Zum  V.  riui-,  —  ai.  riknas'  n.  —  Pii.:  rcxn (Transskr.),  lu  Y.J2  erl.:  ^ästak.  —  D  iBed. S.  np.  murda  reg.  —  >)  KXij/MMfüa,  Eph.  j.  5; vgl.  haahul-  Y.  J_J.  4.
•  j.  raeS^  V.  'sterben',  uzw.  von  ahun- sehen  Wesen ■',  Praes.  27  inhya-;  Per£ I   iflrih:  ~  PPfP.  irista-.
aat  aiiqm  narqm  atvS  trihyä^  h>at  , . agsa  druxiyä  nam^i^A^  fräsnaoiti'^ .^.il; —  äat . .  alte  nmänahe  spä  vH  na  vä  irüyät 'V.5.39;Ä'.i,4,Vyt44(?);  —  visptm  akSm astvanbm  .  .jumia  iristtmca  Yt  /J.  9;  —
dby  Google
1481  rae3^SchIuss  —  »rae*wa-
/ravasayü  jvanqm  . .  ao/yehl/ . .  yaka  iris-  "bii tanqm  Yt.  7^.  17;  — fravasibyS  yh  irJ-  VI** ri'^u/am  .  .  yUsca  jvantqm  Y.  24.  5;    ■ — ■ ,
mä  /is"  Öarff  (sd.)  atvS  yat  irisigm  V.J.  i«  j.  'raeOTva-  n.  i)  'Mengung'  (nur 14;  14;  — frasa  /rayöit  iristitn  uziar^J  Komp.).  2)  'Wirrnis':  kqmat  vil  *aipya- V.6.2T,  5.  41;  —  J'S  vastnm  vpavharv-'  nqm  (sd.)  hmtxm  kqmHt  vä  'wanqm  Yt. zaiti  upairi  ait»m  tristem  V.  <S'.  23;  af.',  4-5"-
=== SOD entry 11
1569:                                                                                                   11 3
18668:          11                                                                   Anc. Lett. 225, 29; GMS I375A; Hen. BAOAS 12,
```


## [2026-09-06T23:18:27.469Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -B4 -A18 \"Page(s): 893 *$\" POK_full.txt | head -60"
}
```


### [2026-09-06T23:18:29.863Z] TOOL RESULT

```
74572-"with measure of capacity measure ', Iter, saikau, -ytr, salkas, sfekas ' measure of capacity 
74573-'; sfeksnis " fathom (as measure)'; 
74574-
74575-References: WP. II 465 f., Trautmann 252. 
74576:Page(s): 893 
74577-
74578-Root / lemma: se(i)-1 {* ke(i)-kla, ske(i)-kla \y\ centum languages) 
74579-Meaning: to sift 
74580-
74581-Material: Gr. nGu), nGsw "siebe", nGpoc; m. " cheesecloth, light cotton gauze used in cheese 
74582-making, sieve '; changing through ablaut (probably h) ipiaAia to snipisrpov TwvaAsupajv 
74583-Hes., ifjaAi(;, -iboc, "Schutzgottin the MiJhlen' ; (about Latin 5//77//a "feinstes Weizenmehl' s. 
74584-but WH. II 538); Middle Irish sTthlad^6as Sieben' (//7from sTthar bucket, pail '); cymr. hidi, 
74585-Middle Breton sizi, nbret. siT sieve ' from *se-tlo-= Old Icelandic sa/dn. ' sieve ' = Gothic 
74586-*seM, assumed through karel. siekia, Finnish seula^ sieve '; Lithuanian sietas' sieve ' = 
74587-Old Church Slavic s//ods. {*sei-to-), Lithuanian sijdju, -ti^ sieve '; Slavic *sejg, *seti 
74588-{*sejati) in Old Church Slavic yOAo-seaZ/'aiviaaar serb. sTjati^ sieve ', (present-stem *seia-, 
74589-preterit-stem *s//a-); alb. shosh^s\ebe\*sia-s)\ 
74590-
74591-Maybe truncated alb. {*sethmos) shoshe' sieve ' : gr. n6p6(; m. ' sieve ', shoshit^ sieve ' 
74592-(common Celtic alb. abbreviation). 
74593-
74594-*sei- " sieve ' is probably as " through ein Geflecht fall let' eine Sonderanwendung from
```


## [2026-09-06T23:18:33.339Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"haec-\\|haek\\|hincaiti\\|to pour out, sprinkle\\|seikV\\|sei-k\" POK_full.txt | head -20"
}
```


### [2026-09-06T23:18:33.387Z] TOOL RESULT

```
70224:Meaning: to haek, noteh 
70228:Root / lemma: remb-, romb-, romb- : 'to haek, noteh' derived from a zero grade of Root / 
72684:Erguft, Besprengung', praseka-m. "Erguft, Ausguft'; Avestan haek-, hincaiti {hicaiti) "gieftt
```


## [2026-09-06T23:18:36.177Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '72670,72740p' POK_full.txt"
}
```


### [2026-09-06T23:18:36.229Z] TOOL RESULT

```
Gothic s/g/'sn. "victory'. Old High German s/g/'m. ds., german. PN Sigi-merus, Segi- 
mundus e\.c. (Indo Germanic neutr.-/5-or -es-stem). Old High German s/g/'ron'mn, 
triumph'; Old High German s/gum., Old English s/gorWctory', Old High German PN Sigur- 
mar{\v\6o Germanic neutr. -^s^stem). 

References: WP. II 481 f. 
Page(s): 888-889 

Root / lemma: seik"- 

Meaning: to spill, pour, draft 

Material: Old Indie secate, sincati {asicat) "giefttfrom, begieftt', seka-m. " downpour, 

Erguft, Besprengung', praseka-m. "Erguft, Ausguft'; Avestan haek-, hincaiti {hicaiti) "gieftt 

from', fra-saekam kbso\uWy "beimVergieften', hixra-v\. "fliJssiges Exkrement'; 

gr. T^ai 5ir|0ncfC(i Hes., Ionian iKpag " dampness ', iKpaA£0(; "humid, wet', iKpaivw " wet ', 
Tpuyoino(; "Mostsieb'; 

Latin 5/5/"oup£T'; siare\s probably from *s/(75/'e after /77e5/'e"mingere' reshaped; siccus 
"dry'; 

gall, (goidel. orVenetic-lllyrian) FIN Sequana ^Se\ne', GN Sinquatis, FIN *S/par/s^Se\/re' 
= Irish FIN Sechair, 



Old High German sJhan 'strain ', Old English seon ds., intr. "ausflieften'; Old High 
German Old Saxon Old English 5/^a/7 "tropfeind fall, sink, flow'. Old Icelandic s/galow, 
base or vorwarts glide, slide' (Modern High German vers/egen ior o\der verse/gen aiter 
dem Ptc. Middle High German versigen). Old High German ^/s/ig'palus, stagnum', 
Norwegian-Swedish sil {*sThila-) "side' (5//a" strain ', wherewith Norwegian sila 
"unaufhorlich rain' probably identical is). East Frisian 5/7'Schleuse', Middle Low German 
s/7"Schleuse, Ablaufkanal', s/7e/7"dranieren'; Old English seohtrei. {*sihtrdn-). Middle Low 
German sichter, sechter' drainage ditch '; Old Icelandic 5/5'Seihe' (schw. Verb s/5" strain 
'), Old English seohhei.. Old High German 5/77a"Seihe' {*s7h-udn-)\ 

Middle Low German se^e'triefend, blear eyed, bleareyed ', Middle Low German Middle 
High German se/ger" slowly or tenacious tropfeind, faint, languid, schal'. Old Icelandic 
se/g'/'"tough'; 

in Germanic also forms with Germanic k. Old High German Middle High German seich 
"urine' (Old High German seihhen. Middle High German seichen. Low German seken 
"urinate, to make water'). Old English 5/ice/75/7 "einsickern'. Low German sTkern, Modern 
High German sickern, Norwegian sikia, Swedish sikkla^ drool, drivel, slaver; trickle ' = Low 
German sikkelen, Norwegian dial. 5//r/5 "small stream, brook', sTka^ strain ', Old Icelandic 
sTku. "stehendes water'. Old English 5/c" watercourse ' etc.; 

nasallos serb. osye/ra "Ebbe' {*seka)\ Church Slavic sbcg, 5i.ca//" urinate, to make water 
', Iter. slov. s//ra// "hervorspritzen'; 

besides eine root seik"-^ dvj' , die probably about "abrinnen, versiegen = austrocken' 
mitse/Zr"'- "diffuse' to unite is: Avestan haecaye/t/wWh ^s "trocknet from' (trans.), haecah-u. 
" dryness, aridity ', hiku-^dxy'; 

because of seip- lies probably *sei- "drip, trickle, rinnen' the basic. 

References: WP. II 466 f., WH. II 531, Trautmann 260. 
Page(s): 893-894 

Root / lemma: seip-, seib- 

Meaning: to pour, rain, sift, *sieve, stream, trickle, dribble 

Material: Old High German sib, Dutch zeef. Middle Low German seven.. Old English sife 

n. " sieve ', in addition Old English siftan. Middle Low German siften, sichten. Modern High 

German (from dem Low German) sichten, and Old Icelandic se/n. "juncus' (because of
```


## [2026-09-06T23:18:41.888Z] TOOL CALL #82: Bash

```json
{
 "command": "sed -n '1,80p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-06T23:18:41.926Z] TOOL RESULT

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


## [2026-09-06T23:18:44.571Z] TOOL CALL #83: Bash

```json
{
 "command": "sed -n '80,140p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-06T23:18:44.611Z] TOOL RESULT

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


## [2026-09-06T23:19:31.068Z] AGENT

Now I'll write the verification file.


## [2026-09-06T23:26:10.355Z] TOOL CALL #84: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk307.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW_PIE  = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/leyk%CA%B7-\"\nW_RIX  = \"https://en.wiktionary.org/wiki/%D8%B1%DB%8C%D8%AE%D8%AA%D9%86\"\nW_GOR  = \"https://en.wiktionary.org/wiki/%DA%AF%D8%B1%DB%8C%D8%AE%D8%AA%D9%86\"\nW_IBR  = \"https://en.wiktionary.org/wiki/%D8%A5%D8%A8%D8%B1%D9%8A%D9%82\"\nW_KUS  = \"https://en.wiktionary.org/wiki/%D9%83%D8%B3%D9%88%D9%81\"\nW_XUS  = \"https://en.wiktionary.org/wiki/%D8%AE%D8%B3%D9%88%D9%81\"\nW_PRZ  = \"https://en.wiktionary.org/wiki/%D9%BE%D8%B1%D9%87%DB%8C%D8%B2\"\nE_ECL  = \"https://www.etymonline.com/word/eclipse\"\nE_LIQ  = \"https://www.etymonline.com/word/liquid\"\nE_ELE  = \"https://www.etymonline.com/word/eleven\"\nE_LOA  = \"https://www.etymonline.com/word/loan\"\n\nnodes = []\n\nnodes.append({\n \"id\": 1, \"lang\": \"Avestan\",\n \"words\": \"raexnah, raix, raik, raič, raeč 2; rěxt, rěz, hâek 1; paiti-raeč; vi-raeč\",\n \"verdict\": \"disputed\",\n \"derivation\": \"The core of the box is right. Avestan has a verb raēk- 'linquere, to leave, let go' (Bartholomae AiW 1479: \\\"j. raek- V. 'linquere'. Praes. 8 irinak-, ... j-Aor. raixs\\\"), i.e. the nasal-infix present iriṇaxti < PIE *li-né-kʷ-ti, the s-aorist raēxš- and the causative raēcaya-; Nourai's 'raix, raik, raič, raeč' are these stem alternants (raēk- / raēc- before front vowels, by the Iranian palatalisation of *k before *e/*i). The Gathic noun raēxnah-/raēxanah- n. 'inheritance, portion left' (AiW 1480, Y 32.11) = Skt. rikṇas- < PIE *lóykʷ-n-es- is likewise correct. 'paiti-raeč' is attested: paiti.raēcaiiaiti / paiti.iriṇaxti 'leaves behind, abandons' (V 5.8, Yt 10.41, Yt 14.47, P 40), and it is the source of MP pahrēz-; Cheung 2007: 307 lists it under *raič '(+*pati-) to desert'. 'vi-raeč' is NOT attested in Avestan (Bartholomae has no vi+raēk-); it is a legitimate reconstruction *wi-raik- presupposed by MP wirēxtan and by Skt. vi-ric-, and Horn no. 914 cites 'skr. vi + √rec' rather than an Avestan form. Two items are wrong: (a) 'rěxt, rěz' are Middle/New Persian stems, not Avestan; (b) 'hâek 1' is a genuine Avestan verb haēk-, hiṇcaiti 'to pour' (AiW 1730), but it belongs to a completely different PIE root, *seikʷ- 'to spill, pour' (Pokorny 893f., with Skt. siñcáti, OHG sīhan), not to *leikʷ-. Nourai has folded the 'pour' family into the 'leave' family.\",\n \"derivation_fa\": \"هستهٔ این خانه درست است: در اوستایی ستاک raēk-/raēc- به معنی «رها کردن، واگذاشتن» گواهی شده است (بارتولومه، فرهنگ ایرانی باستان، ستون ۱۴۷۹: raek- «linquere»)، با ماضی/حال iriṇaxti (از هندواروپایی *li-né-kʷ-ti) و سببی raēcaya-؛ نام raēxnah- «میراث، بهره» (ستون ۱۴۸۰) هم‌ریشه با سنسکریت rikṇas- است. صورت paiti-raēc- «فروگذاشتن» در اوستا آمده (وندیداد ۵٫۸، یشت ۱۰٫۴۱) و سرچشمهٔ pahrēz فارسی میانه است. اما vi-raēc- در اوستا گواهی ندارد و تنها بازسازی است (بر پایهٔ wirēxtan پهلوی و vi-ric- سنسکریت). دو خطا در این خانه هست: یکی آنکه rěxt و rěz صورت‌های فارسی میانه و نو هستند نه اوستایی؛ دیگر آنکه haēk- «ریختن» (ستون ۱۷۳۰) واژه‌ای اوستایی است ولی از ریشهٔ هندواروپایی دیگری یعنی *seikʷ- (پوکورنی ۸۹۳) می‌آید، نه از *leikʷ-. پس در این بخش ادعای نورایی درست نیست.\",\n \"sources\": [W_PIE, W_GOR],\n \"ref_check\": [\n   {\"ref\": \"POK:669\", \"status\": \"supports\", \"note\": \"Pokorny 669-670 s.v. leikʷ- 'to leave': 'Avestan raexnah- \\\"blessing, treasure, tribute, inheritance\\\", -irinaxti \\\"clears up, releases\\\"' (POK_full.txt, lemma leikʷ-, Page(s): 669-670). Pokorny does NOT list Av. haēk- here; haēk-, hiṇcaiti stands under seikʷ- 'to spill, pour', Page(s) 893-894.\"},\n   {\"ref\": \"FFD:72\", \"status\": \"supports\", \"note\": \"Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, printed p.72 (= FFD_pages.txt pdf page 77) s.v. گریختن: 'گریخت < فارسی میانه wirēxt < ایرانی باستان *wi-raik-ta- ... ریشهٔ ric به معنی «ترک کردن» است. «ریختن» از ریشهٔ raik آمده است' — exactly the vi-raeč → v-rextan → gorîxtan chain.\"},\n   {\"ref\": \"SOD:11\", \"status\": \"not_found\", \"note\": \"Gharib's Sogdian dictionary (SOD_pages.txt): leaf/page 11 is Persian front matter, and entry no. 11 is unrelated. The relevant Sogdian material is entry 1950 ryz- 'to flow' and BSogd. pr'yc / rxm'k; nothing at '11'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"cols. 1479-1481\", \"stance\": \"supports\", \"note\": \"'j. raek- V. \\\"linquere\\\". Praes. 8 irinak-, 16 (Des.) irīrixša-, 30 (Iter.) raēcaya-; s-Aor. raixš' and 'g. raexanah- n. \\\"Erbe, Erbteil\\\" ... Zum V. raek-. — ai. riknas-'; also 'ai. riṇākti \\\"linquit\\\" ... mp. rext, np. rextan \\\"ausgiessen\\\"' (grep 'raek-' in BRT.txt).\"},\n   {\"src\": \"CHEUNG\", \"where\": \"pp. 187-188 (*Hraič) and p. 307 (*raič)\", \"stance\": \"partial\", \"note\": \"Cheung 2007 splits the family: '*raič \\\"to leave, let, abandon\\\" ... Y Av. raec- \\\"to leave, let\\\" || (+ *pati-) \\\"to desert\\\" ... PIE *leikʷ- ... Pok.: 669 f.' but '*Hraič \\\"to pour, flow\\\" ... © Exact IE correspondences of this root cannot be found ... tempting to regard it as an enlarged variant of *HraiH'. So the 'leave' words are *leikʷ-, the 'pour' words are not.\"},\n   {\"src\": \"POK\", \"where\": \"893-894 (seikʷ-)\", \"stance\": \"contradicts\", \"note\": \"'Root/lemma: seikʷ- Meaning: to spill, pour ... Avestan haek-, hincaiti (hicaiti) \\\"gießt\\\", hixra- \\\"flüssiges Exkrement\\\"' — Av. haēk- is under a different root than leikʷ-.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. II 396\", \"stance\": \"supports\", \"note\": \"'1. leiqʷ- \\\"lassen, zurück-, übriglassen\\\". Ai. rinákti ... av. raexnah- \\\"Gut, Schatz, Erbteil\\\", irinaxti \\\"verläßt\\\", np. rextan \\\"ausgießen\\\", gurexten \\\"entbehren\\\"'.\"}\n ]\n})\n\nnodes.append({\n \"id\": 2, \"lang\": \"Pahlavi\",\n \"words\": \"rextan; âp-rex; v-rextan; par-hěxtan, pahrězišn\",\n \"verdict\": \"plausible\",\n \"derivation\": \"MacKenzie CPD confirms three of the four: 'rextan, rez- [lyhtn', lyc- | P rylxt, M ryz-, N rextan] flow, pour'; 'wirextan, wirez- [OLYKWN-tn; wlyhtn', wlyc- | P wryxt, ... N gurextan, gurez-] flee, escape'; 'pahrextan, pahrez- [p'hlyhtn', p'hlyc- | M phryz-, N parhextan, parhez-] abstain, refrain, avoid'. The past stems are the regular Iranian *-ta- participles: *raik-ta- > rēxt (OIr. -kt- > MP -xt-), *wi-raik-ta- > wirēxt, *pati-raik-ta- > pahrēxt; the present stems continue *raica-ya- > rēz-, wirēz-, pahrēz-, with Iranian *c > MP z between vowels. Two caveats: (i) Nourai's Pahlavi 'par-hěxtan' is really the NEW Persian shape; the Book-Pahlavi form is pahrēxtan (metathesis -hr- > -rh- happens only in New Persian, as Hübschmann §; Nyberg glosses 'pahrēxtan [p'hlyhtn'] pahrēc- to protect, to take care of ... to abstain from'); pahrēzišn is a normal -išn abstract. (ii) 'âp-rex \\\"water pot\\\"' is not in MacKenzie or Nyberg; the form is reconstructed (Wiktionary posits 'Middle Persian or Parthian *ābrēk', attested only as Classical Persian آبریز ābrēz 'water-pourer'), which is why it is starred by modern authors.\",\n \"derivation_fa\": \"مکنزی در «فرهنگ کوچک پهلوی» سه صورت را تأیید می‌کند: rēxtan/rēz- «ریختن، جاری شدن»، wirēxtan/wirēz- «گریختن» و pahrēxtan/pahrēz- «پرهیز کردن». ستاک ماضی همان صفت مفعولی ایرانی باستان با پسوند ‎*-ta-‎ است: ‎*raik-ta- > rēxt‎ (خوشهٔ ‎-kt-‎ ایرانی باستان در فارسی میانه به ‎-xt-‎ بدل می‌شود)، ‎*wi-raik-ta- > wirēxt‎، ‎*pati-raik-ta- > pahrēxt‎؛ ستاک حال از ‎*raica-ya-‎ می‌آید و «چ» ایرانی باستان میان دو واکه به «ز» نرم شده است. دو نکته: نخست آنکه صورت «par-hěxtan» که نورایی به پهلوی نسبت داده در حقیقت صورت فارسی نو است (پهلوی pahrēxtan است و قلبِ ‎-hr-‎ به ‎-rh-‎ در فارسی نو رخ می‌دهد؛ هوبشمان نیز آن را قلب می‌داند). دوم آنکه âp-rex در فرهنگ‌های پهلوی گواهی ندارد و صورتی بازسازی‌شده است (ویکی‌واژه ‎*ābrēk‎ می‌نویسد و تنها آبریزِ فارسی دری گواهی دارد). بنابراین ادعای نورایی با احتیاط پذیرفتنی است.\",\n \"sources\": [W_RIX, W_GOR, W_IBR, W_PRZ],\n \"ref_check\": [\n   {\"ref\": \"HRN:141,203\", \"status\": \"supports\", \"note\": \"Horn, Grundriss, no. 638 p.141: 'rextan \\\"ausgiessen, verschütten\\\" ... aw. √raēk-, raēcayat \\\"ausgiessen\\\"; phlv. rextan, rext (pāz. rēzed), rēc(i)šn ... Hierher gehört auch syr. LW. ... arab. LW. ibrīq \\\"Wasserkanne\\\" (de Lagarde, Ges. Abh. 7)'; and no. 914 p.203: 'gurexten \\\"fliehen\\\" ... aw. raēcayeinti (paiti) \\\"sie verlassen\\\" ... phlv. v(i)rextan'. Both cited pages hit exactly.\"},\n   {\"ref\": \"FVQ:46\", \"status\": \"supports\", \"note\": \"Jeffery, Foreign Vocabulary of the Qur'an p.46 s.v. إبريق: 'A ewer, or water jug ... early recognized as a Persian loan-word ... In modern Persian the word is آبريز meaning urn or waterpot' (FVQ_pages.txt leaf 64 = printed p.46).\"},\n   {\"ref\": \"SNS:115\", \"status\": \"partial\", \"note\": \"Tavoosi's Shayast ne Shayast glossary: the pahrēz entry stands on printed p.116 (SNS_pages.txt leaf 74: 'pahriz ... Vb. pres. phryz (GNPE. 68) paiti + √raēc'), one page after Nourai's citation; the rēxtan entry (leaf 134) glosses it with Av. raēcayat-/raēc- and Skt. riṇakti. Content supports, page number off by one.\"},\n   {\"ref\": \"BQT\", \"status\": \"not_found\", \"note\": \"No page given by Nourai. Borhan-e Qate' vols 1-4 (BQT_v1/v2/v3/v4_pages.txt) were grepped for ریختن، گریختن، پرهیز، ابریق: only glosses (e.g. v1 leaf 210 s.v. آب‌دستان 'بمعنی ابریق و آفتابه و مطهره') and no etymological footnote of Mo'in bearing on this chain.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"s.vv. rextan, wirextan, pahrextan\", \"stance\": \"supports\", \"note\": \"MacKenzie: 'rextan, rez- [lyhtn', lyc-] flow, pour'; 'wirextan, wirez- [OLYKWN-tn ... N gurextan, gurez-] flee, escape'; 'pahrextan, pahrez- [p'hlyhtn'] abstain, refrain, avoid'. No ābrēz entry.\"},\n   {\"src\": \"NYB\", \"where\": \"Glossary s.vv. rēxtan, pahrēxtan, pahrēc\", \"stance\": \"supports\", \"note\": \"'rēxtan [lyhtn'] rēc- 1. to flow ... 2. to pour. — Av. (1479) raēk-; MPrth pt. ryxt, MPrs pres. ryz-; NP rēxtan rēz-'; index 'raēk-: rēxtan; vi + raēk-: virēxtan'.\"},\n   {\"src\": \"HUB\", \"where\": \"Persische Studien, no. 309 and §145/§ on rh-metathesis\", \"stance\": \"partial\", \"note\": \"Hübschmann on pahrēz: 'Von dieser Pehleviform führt kein Weg zu Fr. Müller's zd. *paiti-raēc- \\\"Verlassen\\\", dem doch nur np. *pairextan entsprechen würde', and later calls parhextan 'etymologisch unerklärt' with hr > rh metathesis. His objection is now superseded by Cheung/DMMPP (MMP phryz- < *pati-raič).\"},\n   {\"src\": \"CHEUNG\", \"where\": \"p. 187 (*Hraič) and p. 307 (*raič)\", \"stance\": \"partial\", \"note\": \"'BMP lyc- /rēz-/ ... Inf.: BMP lyhtn /rēxtan/' under *Hraič 'to pour, flow'; 'MMP phryz- \\\"to keep away from, abstain, avoid\\\" || (+ *ui-) MMP wryxt-, BMP wlyc- /wirēz-/ \\\"to flee, run away\\\"' under *raič < *leikʷ-.\"}\n ]\n})\n\nnodes.append({\n \"id\": 3, \"lang\": \"Persian\",\n \"words\": \"rîxtan «ریختن ( ریز ۱ ، ریزش، آبریز )»; gorîxtan «گریختن ( گریز )»; parhîxtan «پرهیختن ( پرهیز )»\",\n \"verdict\": \"plausible\",\n \"derivation\": \"گریختن and پرهیختن are confirmed: MP wirēxtan > NP gurēxtan/gorīxtan, with the regular New Persian change of initial w- to gu-/go- (cf. wistardan > gostardan, wizārdan > gozārdan; Hübschmann p.156: 'gurextan \\\"fliehen\\\" = pāz. varextan, von vi + Wzl. ric'), and MP pahrēxtan > NP parhēxtan/parhīxtan with metathesis of -hr- to -rh-, present stem parhīz. The Middle Persian ē regularly becomes ī in the modern reading (rēxtan > rīxtan, gurēxtan > gorīxtan). رِیختن 'to pour' is the doubtful one: Pokorny 669 ('npers. rextan \\\"diffuse\\\"'), Bartholomae, Horn no. 638, Nyberg and Abolghasemi all put it under Av. raēk- / PIE *leikʷ- exactly as Nourai does, but Cheung 2007: 187 sets up a separate Iranian root *Hraič 'to pour, flow' for it, remarking that 'exact IE correspondences of this root cannot be found' and connecting it instead with *HraiH < PIE *HreiH- 'to flow'; Wiktionary follows Cheung. The derivatives in the Persian script field (ریز، ریزش، آبریز) are regular: ریز is the present stem, ریزش an -iš abstract, آبریز 'water-pourer' the compound that gave Arabic إبريق.\",\n \"derivation_fa\": \"«گریختن» و «پرهیختن» بی‌گمان درست‌اند: wirēxtan فارسی میانه در فارسی نو به «گریختن» بدل شده است، زیرا «و» آغازین در فارسی نو به «گُـ» می‌گراید (مانند گستردن از wistardan و گزاردن از wizārdan؛ هوبشمان، ص ۱۵۶)؛ و pahrēxtan با قلبِ ‎-hr-‎ به ‎-rh-‎ «پرهیختن/پرهیز» شده است. «ای» کشیدهٔ فارسی میانه در تلفظ نو به «ی» بدل شده است (rēxtan > رِیختن، gurēxtan > گریختن). اما دربارهٔ «ریختن» به معنی «فروریختن آب» اختلاف هست: پوکورنی (۶۶۹)، بارتولومه، هرن (شمارهٔ ۶۳۸)، نیبرگ و ابوالقاسمی همه آن را از ریشهٔ raik «رها کردن» می‌گیرند، درست همان‌گونه که نورایی می‌گوید؛ ولی چونگ (۲۰۰۷، ص ۱۸۷) ریشهٔ ایرانی جداگانه‌ای ‎*Hraič‎ «ریختن، روان شدن» می‌نهد و می‌گوید هم‌ارز دقیق هندواروپایی ندارد و آن را با ‎*HraiH‎ «روان شدن» می‌پیوندد؛ ویکی‌واژه نیز از او پیروی می‌کند. پس ادعای نورایی دربارهٔ «ریختن» با احتیاط پذیرفتنی است و دربارهٔ دو فعل دیگر درست است.\",\n \"sources\": [W_RIX, W_GOR, W_PRZ],\n \"ref_check\": [\n   {\"ref\": \"POK:669\", \"status\": \"supports\", \"note\": \"Pokorny leikʷ-: 'npers. rextan \\\"diffuse\\\", gurexten \\\"miss\\\"' — both Persian verbs are cited by Pokorny under this root on exactly the page Nourai gives.\"},\n   {\"ref\": \"BQT\", \"status\": \"not_found\", \"note\": \"Grepped Borhan-e Qate' vols 1-4 for ریختن/گریختن/پرهیز; only ordinary glosses, no Mo'in etymological footnote on this family (see node 2).\"},\n   {\"ref\": \"AEF:373\", \"status\": \"not_checked\", \"note\": \"Khaleqi Motlaq's Asas-e Eshteqaq-e Farsi (the Persian version of Horn+Hübschmann) is not online and not on disk (refs_online.json: kind 'catalog', 'Not online'). Its German original, Horn no. 638, was checked instead and supports.\"}\n ],\n \"consulted\": [\n   {\"src\": \"HRN\", \"where\": \"no. 638 p.141, no. 914 p.203\", \"stance\": \"supports\", \"note\": \"'rextan \\\"ausgiessen, verschütten\\\" ... aw. √raēk-'; 'gurexten \\\"fliehen\\\" ... phlv. v(i)rextan'.\"},\n   {\"src\": \"HUB\", \"where\": \"p. 9 and p. 156\", \"stance\": \"supports\", \"note\": \"'gurēx \\\"Flucht\\\" neben gurextan, Wrzl. rik'; 'gurextan \\\"fliehen\\\" = pāz. varextan, von vi + Wzl. ric'.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"p. 187 *Hraič\", \"stance\": \"contradicts\", \"note\": \"For NP rēxtan/rēz- 'to flow, pour' Cheung sets up *Hraič with '*PIE — > LIV: – | Pok.: [blank]', i.e. no PIE *leikʷ- source; only gurēxtan and pahrēz stay under *raič < *leikʷ- (p.307).\"},\n   {\"src\": \"FFD\", \"where\": \"printed pp. 57 and 72\", \"stance\": \"supports\", \"note\": \"Abolghasemi: 'ریخت < فارسی میانه rēxt < ایرانی باستان *raixta- ... ریشهٔ raik به معنی «ترک کردن» است'; 'گریخت < فارسی میانه wirēxt < ایرانی باستان *wi-raik-ta-'.\"},\n   {\"src\": \"ARY\", \"where\": \"ARY_pages.txt / ARY_latin_index_pages.txt\", \"stance\": \"silent\", \"note\": \"Aryanpur's IE-roots dictionary was grepped for ریختن/گریختن and for RIKHTAN/GURIKHTAN in the Latin index; no entry for this family was found.\"}\n ]\n})\n\nnodes.append({\n \"id\": 4, \"lang\": \"Arabic\",\n \"words\": \"(no word printed)\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"A pass-through box standing for Arabic إِبْرِيق ibrīq 'ewer, water-jug', the word spelled out in the daughter box #5. It is one of the oldest and least controversial Iranian loans in Arabic: Middle Persian/Parthian *āb-rēz (or *ābrēk) 'water-pourer' = āb 'water' + rēz, the present stem of rēxtan 'to pour', taken into Arabic in pre-Islamic times (the plural أَبَارِيق abārīq stands in an early Meccan sūra, Q 56:18, describing Paradise) and reshaped to the Arabic quadriliteral pattern ʾifʿīl; the Persian -z was rendered by Arabic -q, probably through an Aramaic/Syriac intermediary ܐܒܪܝܩܐ ʾaḇrēqā. Classical Arab lexicographers (al-Kindī, Thaʿālibī Fiqh 317, al-Jawālīqī, al-Suyūṭī, Lisān al-ʿArab XI 299) all list it among the Persian borrowings.\",\n \"derivation_fa\": \"این خانه، خانهٔ گذر است و مقصود واژهٔ عربی «إبريق» است که در خانهٔ فرزند (#۵) نوشته شده. این واژه از کهن‌ترین و بی‌مناقشه‌ترین وام‌واژه‌های ایرانی در عربی است: از فارسی میانه/پارتی ‎*āb-rēz‎ «آب‌ریز» (آب + ستاک حال ریختن) که پیش از اسلام، شاید به میانجی سریانی ʾaḇrēqā، وارد عربی شده و بر وزن «إفعيل» ساخته شده است؛ جمع آن «أباريق» در سورهٔ واقعه (۵۶:۱۸) آمده است. «ز» فارسی در عربی به «ق» بدل شده است. لغت‌نویسان کهن عرب (کندی، ثعالبی در فقه اللغة ۳۱۷، جوالیقی، سیوطی، لسان العرب) همه آن را در شمار معرّبات فارسی آورده‌اند. ادعای نورایی درست است.\",\n \"sources\": [W_IBR],\n \"ref_check\": [\n   {\"ref\": \"FVQ:46\", \"status\": \"supports\", \"note\": \"Jeffery p.46: 'إبريق A ewer, or water jug. Only in the plu. form أباريق in an early Meccan description of Paradise. It was early recognized as a Persian loan-word (Siddiqi, 13), and is given by al-Kindī, Risāla, 85; ath-Thaʿālibī, Fiqh, 317; as-Suyūṭī and al-Jawālīqī in their lists of Persian borrowings, as well as by the Lexicons, LA, xi, 299 ... In modern Persian the word is آبريز meaning urn or waterpot.'\"}\n ],\n \"consulted\": [\n   {\"src\": \"AFM\", \"where\": \"Addi Shir, s.v. الإبريق (AFM_pages.txt leaf 20, ≈ printed p.6, the page Jeffery cites as 'Addai Sher, 6')\", \"stance\": \"supports\", \"note\": \"'(الإبريق) ... تعريب آبريز، واصل معناه يصب الماء، ويطلق على الدلو والسطل وغير ذلك' — 'Arabicized from ābrīz, whose original meaning is \\\"it pours water\\\"'.\"},\n   {\"src\": \"HRN\", \"where\": \"no. 638 p.141\", \"stance\": \"supports\", \"note\": \"'Hierher gehört auch syr. LW. [ʾbryqʾ], arab. LW. ibrīq \\\"Wasserkanne\\\" (de Lagarde, Ges. Abh. 7)' — Horn derives the Arabic word from this very Persian verb.\"},\n   {\"src\": \"PLA\", \"where\": \"Asbaghi, Persische Lehnwörter im Arabischen (PLA_asbaghi_1988_ia_djvu.txt)\", \"stance\": \"silent\", \"note\": \"Grepped for ibrīq / ābrīz / إبريق in the OCR of Asbaghi; the OCR returned no hit (the transliterated headwords are badly rendered), so no statement could be extracted.\"}\n ]\n})\n\nnodes.append({\n \"id\": 5, \"lang\": \"Persian\",\n \"words\": \"ebrîq «إبریق»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"A round trip: Middle Persian āb-rēz 'water-pourer' > Arabic ibrīq > New Persian ebrīq/abrīq, re-borrowed with the Arabic spelling إبريق and the Arabic sense 'ewer, water- or wine-jug'. Mo'in's dictionary marks it explicitly as an Arabicization of the native word: 'ابریق [معر. آبریز] (اِ.) ظرف سفالین آب ... مطهره، آفتابه'. Jeffery notes the same in a footnote: 'ابریق also occurs in Pers. but only as a borrowing from Arabic'. Nourai's Rūmī couplet (گر بیافزاید می توفیق را - قوّت می بشکند ابریق را) shows the Arabicized form in classical Persian verse.\",\n \"derivation_fa\": \"این واژه نمونهٔ روشن «دوگانهٔ رفت‌وبرگشتی» است: «آب‌ریز» فارسی میانه به عربی رفت و «إبريق» شد و سپس همان صورت معرّب به فارسی بازگشت و «ابریق» شد، با املای عربی و معنی «آفتابه، ظرف آب یا شراب». معین در فرهنگ خود صریحاً می‌نویسد: «ابریق: [معر. آبریز] (اِ.) ظرف سفالین آب ... مطهره، آفتابه»؛ جفری نیز در حاشیه می‌گوید ابریق در فارسی تنها به عنوان وام‌واژه از عربی به کار می‌رود. بیت مولوی که نورایی آورده گواه کاربرد صورت معرّب در شعر فارسی است. ادعای نورایی درست است.\",\n \"sources\": [W_IBR],\n \"ref_check\": [\n   {\"ref\": \"MON:125\", \"status\": \"supports\", \"note\": \"Mo'in, Farhang-e Farsi s.v. ابریق: 'ابریق: [معر. آبریز] (اِ.) ظرف سفالین آب، آوند چرمین لوله‌دار که بدان وضو سازند، مطهره ... ج اباریق' (MON_part1.txt line 6264). The 6-vol pagination could not be checked (only the 2-vol Adena reprint is on disk), but the content is exactly what MON:125 is cited for.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"s.v. ابریق\", \"stance\": \"supports\", \"note\": \"'[معر. آبریز]' = 'Arabicized form of ābrīz' — Mo'in states the round trip himself.\"},\n   {\"src\": \"FVQ\", \"where\": \"p. 46 n. 7\", \"stance\": \"supports\", \"note\": \"'ابریق also occurs in Pers. but only as a borrowing from Arabic.'\"},\n   {\"src\": \"BQT\", \"where\": \"vol. 1, leaf 210, s.vv. آب‌دستان / آب‌دست‌دان\", \"stance\": \"partial\", \"note\": \"Borhan-e Qate' uses ابریق only as a defining synonym ('بمعنی ابریق و آفتابه و مطهره باشد'); it gives no etymology for it.\"}\n ]\n})\n\nnodes.append({\n \"id\": 6, \"lang\": \"Latin\",\n \"words\": \"liquěre : to be liquid\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Latin liquēre 'to be fluid, be clear' (whence liquidus, liquor, liquī, liquāre) is a genuine Latin word with the meaning Nourai gives, but attaching it to *leikʷ- 'to leave' is a minority position. It is defensible in two ways: Pokorny prints the material under the same page (Watkins' *wleik- is labelled '[In Pok. leikʷ- 669]'), and Ernout-Meillet argue for the connection explicitly — 'Celui avec persan rextan \\\"verser\\\" est plus satisfaisant; comme ce mot persan est inséparable de av. raēcayeiti \\\"il laisse\\\", il en résulte que liqueō serait un verbe d'état appartenant à la racine de linquō'. Against it: Walde-Pokorny II 398 says flatly that the root of liquēre is 'leikʷ- \\\"naß, flüssig sein\\\", nicht als \\\"fließen lassen, rinnen lassen\\\" = leiḱʷ- \\\"lassen\\\"'; Klein derives liquidus from liquēre 'related to lix \\\"ashes\\\", lixa \\\"lye\\\", prolixus' and cognate with OIr. fliuch, W. gwlyb 'moist'; Watkins/AHD and Etymonline set up *wleik- 'to flow, run' as a separate root. On the modern majority view the Latin branch does not belong on this chart.\",\n \"derivation_fa\": \"فعل لاتینی liquēre «آبگون بودن، زلال بودن» (از آن liquidus و liquor) واژه‌ای اصیل با همان معنایی است که نورایی می‌آورد، اما پیوند دادن آن به ریشهٔ *leikʷ- «رها کردن» رأی اقلیت است. دو پشتوانه دارد: نخست آنکه پوکورنی این ماده را در همان صفحهٔ ۶۶۹ جای داده (واتکینز ذیل *wleik- می‌نویسد «در پوکورنی زیر leikʷ- ۶۶۹»)؛ دوم آنکه ارنو و می‌یه صریحاً همین پیوند را می‌پذیرند و دلیلشان همان «ریختن» فارسی است که از raēcayeiti اوستایی جدایی‌ناپذیر است. در برابر، والده-پوکورنی (ج۲ ص۳۹۸) می‌گوید ریشهٔ liquēre همان «تر و آبگون بودن» است «نه به معنی روان کردن = leikʷ- رها کردن»؛ کلاین آن را با lix و lixa و ایرلندی کهن fliuch «تر» هم‌ریشه می‌داند و واتکینز و اتیمانلاین ریشهٔ جداگانهٔ *wleik- «روان شدن» می‌نهند. بنابراین ادعای نورایی با احتیاط پذیرفتنی است ولی پژوهش امروزی بیشتر آن را جدا می‌کند.\",\n \"sources\": [E_LIQ],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"contradicts\", \"note\": \"Watkins (AHD_watkins1985.txt): 'wleik-. To flow, run. Zero-grade form *wlik-. ... b. suffixed form *wlik-w-e- in Latin liquēre, to be liquid: LIQUESCENT, LIQUID, LIQUOR ... [In Pok. leiku- 669.]' — AHD, the reference Nourai cites here, assigns liquēre to *wleik-, not to leikw-; the index line reads 'LIQUID wleik-'. Only the bracketed Pokorny page agrees with Nourai.\"}\n ],\n \"consulted\": [\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. liqueō\", \"stance\": \"supports\", \"note\": \"'Celui avec persan rextan \\\"verser\\\" est plus satisfaisant; comme ce mot persan est inséparable de av. raēcayeiti \\\"il laisse\\\", il en résulte que liqueō serait un verbe d'état appartenant à la racine de linquō et que liquor serait à rapprocher de gr. λείπομαι.'\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. II 398\", \"stance\": \"contradicts\", \"note\": \"'leiqʷ- \\\"naß, flüssig sein\\\", nicht als \\\"fließen lassen, rinnen lassen\\\" = leiḱʷ- \\\"lassen\\\" (Curtius 463, Fick I 121, 533; über av. paitiraēcayeiti s. vielmehr Bthl. Air. Wb. 1480).'\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. liquid, adj.\", \"stance\": \"contradicts\", \"note\": \"'L. liquidus \\\"flowing, fluid, liquid, clear\\\", fr. liquere \\\"to be fluid\\\", which is rel. to lix ... lixa \\\"water; lye\\\", prolixus ... and prob. cogn. with OIr. fliuch \\\"moist, wet\\\", OW. gulip' — no link to linquere/loan.\"},\n   {\"src\": \"POK\", \"where\": \"669-670\", \"stance\": \"partial\", \"note\": \"Pokorny's leikʷ- article itself lists Latin linquō but not liquēre; the liquēre material sits in the neighbouring lemma that Watkins re-labels wleik- 'In Pok. leikʷ- 669'.\"}\n ]\n})\n\nnodes.append({\n \"id\": 7, \"lang\": \"English\",\n \"words\": \"liquid, liquor\",\n \"verdict\": \"plausible\",\n \"derivation\": \"The Latin-to-English chain itself is beyond doubt: liquid is Middle English, from Old French liquide (13th c.), from Latin liquidus 'flowing, fluid, clear' (adjective of liquēre); liquor is Middle English licour, from Old French licour/liquor, from Latin liquōrem, accusative of liquor 'a fluid', the -qu- spelling restored on the Latin model in the 16th-17th c. The only question is the ultimate root: the same doubt as node #6 — Etymonline and Watkins take it back to PIE *wleik- 'to flow, run', not to *leikʷ- 'to leave', so the words are English descendants of Latin but probably not of this chart's root.\",\n \"derivation_fa\": \"زنجیرهٔ لاتینی تا انگلیسی تردیدناپذیر است: liquid از انگلیسی میانه، از فرانسهٔ کهن liquide (سدهٔ سیزدهم)، از لاتینی liquidus «روان، زلال» (صفت از liquēre)؛ و liquor از انگلیسی میانه licour، از فرانسهٔ کهن، از لاتینی liquōrem. تنها پرسش دربارهٔ ریشهٔ نهایی است: اتیمانلاین و واتکینز آن را به ‎*wleik-‎ «روان شدن» می‌رسانند نه به ‎*leikʷ-‎ «رها کردن». پس این دو واژه بی‌گمان از لاتینی‌اند اما پیوندشان با ریشهٔ این نمودار با احتیاط پذیرفتنی است.\",\n \"sources\": [E_LIQ],\n \"ref_check\": [\n   {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference on this node; the parent box carries 'AHD', which was checked at node #6 and contradicts.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.vv. liquid, adj.; liqueur\", \"stance\": \"supports\", \"note\": \"'liquid, adj. — ME., fr. OF. (= F.) liquide, fr. L. liquidus, \\\"flowing, fluid, liquid, clear\\\", fr. liquere'; 'liqueur, n. — F., fr. L. liquorem, acc. of liquor'. The Latin→French→English route is confirmed; the root assignment is not.\"},\n   {\"src\": \"AHD\", \"where\": \"index and s.v. wleik-\", \"stance\": \"contradicts\", \"note\": \"'LIQUID wleik-', 'LIQUOR wleik-' in Watkins' index of English words.\"}\n ]\n})\n\nnodes.append({\n \"id\": 8, \"lang\": \"Germanic\",\n \"words\": \"(no word printed)\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Empty pass-through box for the Proto-Germanic verb and noun that gave English lend and loan: PGmc *laihwaną 'to lend' (< PIE *leikʷ-, o-grade *loikʷ-, Gothic leiƕan, OHG līhan, ON ljá), its causative *laihwnijaną (> OE lǣnan) and the ne/o-stem noun *laihwniz/*laihną 'thing lent, fief' (< *loikʷ-nes-, exactly matching Skt. rékṇas- and Av. raēxnah- of node #1) in ON lán, OE lǣn, OHG lēhan, German Lehen. The semantic bridge is 'to leave (with someone)' > 'to let have' > 'to lend'.\",\n \"derivation_fa\": \"این خانهٔ تهی نمایندهٔ ستاک ژرمنی آغازین است که «lend» و «loan» انگلیسی از آن آمده‌اند: ‎*laihwaną‎ «قرض دادن» (از هندواروپایی ‎*leikʷ-‎ با درجهٔ ‎o‎، یعنی ‎*loikʷ-‎؛ گوتی leiƕan، آلمانی علیای کهن līhan، نروژی کهن ljá)، سببی آن ‎*laihwnijaną‎ (> انگلیسی کهن lǣnan) و اسم ‎*laihwniz/*laihną‎ «چیز عاریتی، تیول» (از ‎*loikʷ-nes-‎) که دقیقاً هم‌ساخت raēxnah- اوستایی و rékṇas- سنسکریت است. پل معنایی چنین است: «واگذاشتن نزد کسی» ← «در اختیار نهادن» ← «وام دادن». ادعای نورایی درست است.\",\n \"sources\": [E_LOA, W_PIE],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins s.v. leikw-: '2. O-grade form *loikw- in: a. Germanic *laihwnjan in Old English lǣnan, to lend, give (< \\\"to leave to\\\"): LEND; b. suffixed form *loikw-nes- in Germanic *laihwniz in Old Norse lán, loan: LOAN.'\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"669-670\", \"stance\": \"supports\", \"note\": \"'Gothic leiƕan, Old Icelandic ljá, Old High German līhan, Old English lēon \\\"lend\\\" (*leikʷō) ... Old Icelandic lán, Old English lǣn, Old High German lēhan \\\"borrowed property, fief\\\" (*laihna- = Old Indic reknas-)'.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. II 396-397\", \"stance\": \"supports\", \"note\": \"'Got. leihan, aisl. ljá, ahd. līhan, ags. lēon \\\"leihen\\\" ... aisl. lán, ags. lǣn, ahd. lēhan \\\"geliehenes Gut, Lehen\\\" (= ai. reknas-)'.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann s.v. leiquo\", \"stance\": \"supports\", \"note\": \"'leiquo \\\"leave, let, allow, remain\\\" ... Go. leihvan \\\"lend\\\"; OE lēon, MHG līhen ... ON ljá, lé, wv \\\"lend, grant\\\". WP II, 396'.\"}\n ]\n})\n\nnodes.append({\n \"id\": 9, \"lang\": \"English\",\n \"words\": \"lend, loan\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"lend is Middle English lenen, from Old English lǣnan 'to lend, grant', a denominative of lǣn 'loan' (< PGmc *laihwniz); the final -d is a Middle English intrusion on the analogy of past tenses like sent/bent, so ME lene(n) became lend by the 15th c. loan is Middle English lan/lon, borrowed from Old Norse lán, which displaced the native OE lǣn during the Scandinavian period; the Norse word is the same *laihwniz noun. Both therefore go back to PIE *leikʷ- 'to leave' via 'to let have'.\",\n \"derivation_fa\": \"«lend» از انگلیسی میانه lenen، از انگلیسی کهن lǣnan «وام دادن» است که خود از اسم lǣn «وام» (ژرمنی ‎*laihwniz‎) ساخته شده؛ «د» پایانی در انگلیسی میانه و به قیاس با ماضی‌هایی چون sent و bent افزوده شده است. «loan» از انگلیسی میانه lan/lon و در اصل وام‌واژه‌ای از نروژی کهن lán است که جای lǣn بومی را در دورهٔ اسکاندیناوی گرفت. هر دو در نهایت به ریشهٔ هندواروپایی ‎*leikʷ-‎ «رها کردن، واگذاشتن» بازمی‌گردند. ادعای نورایی درست است.\",\n \"sources\": [E_LOA],\n \"ref_check\": [\n   {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"Nourai cites nothing on this node; the parent box's 'AHD' was checked at node #8 and supports.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.vv. lend, loan\", \"stance\": \"supports\", \"note\": \"'lend ... ME. lenen, fr. OE. lǣnan \\\"to lend, grant\\\", fr. lǣn \\\"loan\\\"'; 'loan, n. — ME. lan, lon, fr. ON. lán ... The orig. meaning of these verbs was \\\"to let have, leave\\\". They derive fr. I.-E. base *liqw-, \\\"to let, leave\\\", whence also OI. riṇakti ... Gk. λείπειν ... L. linquere.'\"},\n   {\"src\": \"SKT\", \"where\": \"s.vv. Lend; Loan\", \"stance\": \"supports\", \"note\": \"'Lend; see Loan.' and 'lend. (E.) The final d ... ME. lenen. A.S. lǣnan, to lend, fr. lǣn, a loan ... + Icel. lán, Dan. laan ... G. lehnen, from lehn.'\"},\n   {\"src\": \"AHD\", \"where\": \"index\", \"stance\": \"supports\", \"note\": \"'LEND leikw-', 'LOAN leikw-'.\"}\n ]\n})\n\nnodes.append({\n \"id\": 10, \"lang\": \"Germanic\",\n \"words\": \"-lif : left over\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Proto-Germanic *-lif- 'left (over)', the zero-grade *likʷ- of *leikʷ-, used as the second member of the two Germanic teen-formations *ain-lif- 'one left (over ten)' and *twa-lif- 'two left (over ten)'. The same idiom appears in Baltic with the cognate root: Lithuanian vienuo-lika '11', dvy-lika '12', which are the exact structural equivalents. Note that Pokorny himself hesitated here — at p.670 he adds that Gothic ain-, twa-lif 'are to be put either to leip-1 or, according to Marstrander, borrowed from Celtic *lipi- (*likʷi-)' — but Watkins, Klein, Mann and Etymonline all keep them under *leikʷ-, which is the standard view today.\",\n \"derivation_fa\": \"‎*-lif-‎ ژرمنی آغازین به معنی «باقی‌مانده» است، از درجهٔ صفر ‎*likʷ-‎ از ریشهٔ ‎*leikʷ-‎، که جزء دوم دو عدد ‎*ain-lif-‎ «یکی بر جای مانده (از ده)» و ‎*twa-lif-‎ «دو بر جای مانده» است. همین ساخت در بالتیک نیز با همان ریشه دیده می‌شود: لیتوانیایی vienuo-lika «۱۱» و dvy-lika «۱۲». پوکورنی خود در ص۶۷۰ تردید کرده و گفته صورت‌های گوتی ain-/twa-lif را یا باید به ‎leip-‎ برد یا (به پیروی مارستراندر) وام از سلتی دانست؛ ولی واتکینز، کلاین، مان و اتیمانلاین همه آن را زیر ‎*leikʷ-‎ نگاه داشته‌اند و این رأی امروزی است. ادعای نورایی درست است.\",\n \"sources\": [E_ELE, W_PIE],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins s.v. leikw-: '3. Zero-grade form *likw- in Germanic *-lif-, left, in: a. Germanic *ain-lif-, \\\"one (beyond ten)\\\", in Old English endleofan, eleven (see oi-no-); b. Germanic *twa-lif-, \\\"two left (beyond ten)\\\", in Old English twelf, twelve (see dwo-).'\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"670\", \"stance\": \"partial\", \"note\": \"'here also Lithuanian vienuo-, dvy-lika etc. \\\"11, 12\\\" ... but Gothic ain-, twa-lif, Old High German ein-, zwe-lif \\\"11, 12\\\" ... are to be put either to leip-1 or according to Marstrander (Ériu 5, 206) borrowed from Celtic *lipi- (*likʷi-)' — Pokorny doubts the Germanic forms specifically.\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. twelve\", \"stance\": \"supports\", \"note\": \"'These words are compounds meaning lit. \\\"two left after (ten)\\\" ... The second element is cogn. with L. linquere, Gk. λείπειν, \\\"to leave behind\\\"; see loan ... cp. Lith. dvy-lika.'\"},\n   {\"src\": \"IEC\", \"where\": \"Mann s.v. liquos\", \"stance\": \"supports\", \"note\": \"'Cf. also vienuo-lika, dvy-lika \\\"11, 12\\\" in relation to Go. etc. ain-lif, twa-lif, id. WP II, 396.'\"}\n ]\n})\n\nnodes.append({\n \"id\": 11, \"lang\": \"English\",\n \"words\": \"eleven, twelve\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"eleven is Middle English elleovene, from Old English endleofan/enleofan, literally 'one left (over ten)', from PGmc *ainlif- (Gothic ainlif, ON ellifu, OHG einlif, German elf); twelve is Old English twelf, literally 'two left (over ten)', from PGmc *twalif- (Gothic twalif, ON tolf, OHG zwelif, German zwölf). In both, the second element *-lif- is the zero grade of *leikʷ- (node #10), while the first is *oi-no- 'one' and *dwo- 'two'. Old English -lif- lost its final consonant and was reduced to -f/-ven in the modern forms.\",\n \"derivation_fa\": \"«eleven» از انگلیسی میانه elleovene و انگلیسی کهن endleofan/enleofan است، تحت‌اللفظ «یکی مانده (بر ده)»، از ژرمنی ‎*ainlif-‎ (گوتی ainlif، نروژی کهن ellifu، آلمانی elf)؛ و «twelve» از انگلیسی کهن twelf، تحت‌اللفظ «دو مانده (بر ده)»، از ژرمنی ‎*twalif-‎ (گوتی twalif، آلمانی zwölf). در هر دو، جزء دوم ‎*-lif-‎ همان درجهٔ صفر ریشهٔ ‎*leikʷ-‎ است (خانهٔ ۱۰) و جزء نخست ‎*oi-no-‎ «یک» و ‎*dwo-‎ «دو». ادعای نورایی درست است.\",\n \"sources\": [E_ELE],\n \"ref_check\": [\n   {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"No reference on this node; parent's 'AHD' checked at node #10 and supports.\"}\n ],\n \"consulted\": [\n   {\"src\": \"SKT\", \"where\": \"s.v. Eleven\", \"stance\": \"supports\", \"note\": \"'Eleven. (E.) M.E. enleuen. A.S. endlufon ... Goth. ainlif ... The best form is the Goth. ain-lif, where ain = one; and -lif = Lithuan. -lika (in vienolika, eleven). Lith. lika means \\\"remaining\\\".'\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. twelve\", \"stance\": \"supports\", \"note\": \"'... lit. \\\"two left after (ten)\\\" ... see loan, relinquish and cp. eleven.'\"},\n   {\"src\": \"AHD\", \"where\": \"index\", \"stance\": \"supports\", \"note\": \"'ELEVEN' is filed under oi-no- with the cross-reference '*lif-, left; see leikw-'; 'TWELVE' under dwo- with '(*-lif-, left; see leik-)'.\"}\n ]\n})\n\nnodes.append({\n \"id\": 12, \"lang\": \"Greek\",\n \"words\": \"ek-leipein : to leave out; ek-leipsis : cessation (of light)\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Greek λείπω leípō 'I leave' is the unextended thematic present of *leikʷ- (aor. ἔλιπον, perf. λέλοιπα, with the full ablaut series *leikʷ-/*loikʷ-/*likʷ-). The compound ἐκλείπω ekleípō (ἐκ 'out' + λείπω) means 'to leave out, forsake a usual place, fail to appear', and is used from Herodotus and Thucydides onwards of a heavenly body 'failing'; its verbal noun ἔκλειψις ékleipsis 'a failing, forsaking; an eclipse' is the technical Greek astronomical term. Nourai's glosses are exactly the standard ones.\",\n \"derivation_fa\": \"فعل یونانی λείπω «رها می‌کنم» صورت حالِ درون‌مایه‌ای ریشهٔ ‎*leikʷ-‎ است (ماضی ἔλιπον، ماضی نقلی λέλοιπα، با سه درجهٔ آوایی ‎*leikʷ-/*loikʷ-/*likʷ-‎). ترکیب ἐκλείπω (ἐκ «بیرون» + λείπω) به معنی «فروگذاشتن، از جای همیشگی رفتن، پدیدار نشدن» است و از هرودوت و توسیدید به بعد دربارهٔ اجرام آسمانی به کار رفته؛ اسم مصدر آن ἔκλειψις «فروگذاری، ناپدید شدن؛ گرفت» اصطلاح فنی اخترشناسی یونانی است. معنی‌هایی که نورایی داده درست‌اند و ادعای او تأیید می‌شود.\",\n \"sources\": [E_ECL, W_PIE],\n \"ref_check\": [\n   {\"ref\": \"AHD:413\", \"status\": \"supports\", \"note\": \"The 1975 New College main entry p.413 is not on disk, but Watkins' appendix (AHD_watkins1985.txt) s.v. leikw- reads: '1. Basic form *leikw- in Greek leipein, to leave: ECLIPSE, ELLIPSIS', and the index line is 'ECLIPSE leikw-'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"669-670\", \"stance\": \"supports\", \"note\": \"'gr. λείπω \\\"allow, leave\\\", λοιπός \\\"residual, remaining\\\", λιμπάνω \\\"allow\\\" ... λεῖμμα n. \\\"remnant\\\", λείψανον ds.'\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. eclipse, n.\", \"stance\": \"supports\", \"note\": \"'fr. Gk. ἔκλειψις, \\\"a leaving out, forsaking, failure; eclipse\\\", fr. ἐκλείπειν, \\\"to leave out, forsake, cease; to be eclipsed\\\", fr. ἐκ (see ec-) and λείπειν, \\\"to leave\\\", which is cogn. with L. linquere.'\"},\n   {\"src\": \"IEC\", \"where\": \"Mann s.v. leiquo, leiqusos\", \"stance\": \"supports\", \"note\": \"'Myc. leiq-, Gk. leípō, aor. élipon'; 'leiqusos ... Gk. leípsis, f. \\\"desertion\\\"'.\"}\n ]\n})\n\nnodes.append({\n \"id\": 13, \"lang\": \"Arabic\",\n \"words\": \"kosŭf, xosŭf : eclipse\",\n \"verdict\": \"disputed\",\n \"derivation\": \"Nourai's source really does say this — al-Unaysi's Tafsīr al-alfāẓ al-dākhila, printed p.63, has 'كسف وخسف الشمس والقمر كسوفاً — معرَّب اليوناني ekleipsis ومعناه نقصان النور' — but the claim cannot stand. كُسُوف kusūf and خُسُوف xusūf are ordinary Arabic maṣdars of the fuʿūl type formed on two native triliteral roots, k-s-f 'to cut off, be cut off, be gloomy' and x-s-f 'to sink in, cave in', both of which are Qur'anic in their non-astronomical senses (kisafan 'fragments' Q 17:92; xasafnā bihi l-arḍ Q 28:81, wa-xasafa l-qamar Q 75:8) and both of which have full verbal paradigms (kasafa/kusifat, xasafa/xusifa) that a loanword would not have. Two distinct roots cannot both be traced to one Greek noun, and Arabic borrowing of Greek ἔκλειψις would give something like إقليبسيس, not a sound triliteral. Wiktionary derives كسوف simply as 'the verbal noun of كَسَفَ (kasafa)' and خسوف as 'the verbal noun of خَسَفَ (ḵasafa)'; neither Jeffery's Foreign Vocabulary nor al-Jawālīqī's Muʿarrab lists either word among the borrowings. The likeness to ekleipsis is accidental, and al-Unaysi's entry is one of the loose Greek attributions that book is known for.\",\n \"derivation_fa\": \"مأخذ نورایی واقعاً همین را می‌گوید: طوبیا العنیسی در «تفسیر الألفاظ الدخیلة» ص۶۳ نوشته است «کسف وخسف الشمس والقمر کسوفاً ـ معرَّب الیونانی ekleipsis ومعناه نقصان النور»؛ اما این ادعا پذیرفتنی نیست. «کُسوف» و «خُسوف» مصدرهای عادی عربی بر وزن فُعول از دو ریشهٔ سه‌حرفی اصیل عربی‌اند: ک‌س‌ف «بریدن، تیره شدن» و خ‌س‌ف «فرو رفتن، فرو نشستن»، که هر دو در قرآن به معنی غیر اخترشناختی آمده‌اند («کِسَفاً» اسراء ۹۲؛ «فخسفنا به الأرض» قصص ۸۱؛ «وخسف القمر» قیامه ۸) و هر دو صرف کامل فعلی دارند (کسف/کُسفت، خسف/خُسف) که وام‌واژه نمی‌تواند داشته باشد. دو ریشهٔ جداگانه را نمی‌توان از یک اسم یونانی گرفت، و اگر عربی ἔκλειψις را وام می‌گرفت صورتی مانند «إقلیبسیس» می‌شد نه ریشه‌ای سالم. ویکی‌واژه «کسوف» را تنها مصدر «کَسَفَ» و «خسوف» را مصدر «خَسَفَ» می‌داند و نه جفری و نه جوالیقی هیچ‌یک را در شمار معرّبات نیاورده‌اند. پس پژوهش امروزی این ادعا را رد می‌کند؛ شباهت به ekleipsis تصادفی است.\",\n \"sources\": [W_KUS, W_XUS],\n \"ref_check\": [\n   {\"ref\": \"TAD:63\", \"status\": \"supports\", \"note\": \"Verified from the page image (archive.org/details/TOB1932ARAR leaf n66 = printed p.٦٣; saved as data/verification/sources/refs/ocr/TAD/63.jpg and 63.vision.txt): 'كسف وخسف الشمس والقمر كسوفاً — معرَّب اليوناني ekleipsis ومعناه نقصان النور، وقد تكسف الشمس لحيلولة القمر بينها وبين الارض. مرادفه احتجب'. The reference says exactly what Nourai's arrow says; it is the reference itself that is wrong.\"}\n ],\n \"consulted\": [\n   {\"src\": \"FVQ\", \"where\": \"Jeffery, Foreign Vocabulary of the Qur'an\", \"stance\": \"silent\", \"note\": \"Grepped FVQ.txt for kusuf/kasaf: no entry — Jeffery does not treat كسف/خسف as foreign, although both roots occur in the Qur'an.\"},\n   {\"src\": \"ARB\", \"where\": \"al-Jawaliqi, al-Muʿarrab (ARB_mo3rb.txt, ARB_abdulraheem.txt)\", \"stance\": \"silent\", \"note\": \"Grepped for كسوف/كسف: the only hits are incidental ('إذا كسف' in the definition of another word) — al-Jawālīqī does not list kusūf among the arabicized words.\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. eclipse\", \"stance\": \"silent\", \"note\": \"Klein traces eclipse only through Latin and French; no Arabic descendant of ekleipsis is recorded anywhere in the entry.\"}\n ]\n})\n\nnodes.append({\n \"id\": 14, \"lang\": \"Persian\",\n \"words\": \"kosŭf «کسوف ( خسوف )»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"The link drawn in this box — Arabic > Persian — is right: کسوف kosūf and خسوف xosūf are straightforward Arabic loans in Persian, taken over with the Arabic script and the Arabic technical sense, and Persian has narrowed them, as Mo'in notes, so that kosūf is used of the sun and xosūf of the moon while Arabic uses both of either. Mo'in tags the word '[ع.]' (Arabic) and adds: 'در لغت عرب «کسوف» به معنی گرفتن آفتاب و گرفتن ماه هر دو آمده ولی در عرف فارسی‌زبانان «کسوف» در آفتاب و «خسوف» در ماه گویند'. What does not hold is the box above it: the Arabic words are not from Greek (see node #13), so this Persian word is an Arabic loan with no connection to *leikʷ-.\",\n \"derivation_fa\": \"پیوندی که در این خانه کشیده شده — عربی به فارسی — درست است: «کسوف» و «خسوف» وام‌واژه‌های سرراست عربی در فارسی‌اند که با همان املا و همان معنی فنی گرفته شده‌اند، و فارسی‌زبانان آن‌ها را تخصیص داده‌اند. معین این واژه را با نشانهٔ [ع.] می‌آورد و می‌افزاید: «در لغت عرب «کسوف» به معنی گرفتن آفتاب و گرفتن ماه هر دو آمده ولی در عرف فارسی زبانان «کسوف» در آفتاب و «خسوف» در ماه گویند». آنچه درست نیست خانهٔ بالای آن است: واژه‌های عربی از یونانی نیامده‌اند (خانهٔ ۱۳)، پس این واژهٔ فارسی وام‌واژه‌ای عربی است و هیچ پیوندی با ریشهٔ ‎*leikʷ-‎ ندارد.\",\n \"sources\": [W_KUS, W_XUS],\n \"ref_check\": [\n   {\"ref\": \"MON:2975\", \"status\": \"supports\", \"note\": \"Mo'in s.v. کسوف: 'کسوف: [ع.] (مص ل.) (نج.) گرفتن آفتاب. (امص.) (نج.) آفتاب‌گرفتگی. ضح.- در لغت عرب «کسوف» به معنی گرفتن آفتاب و گرفتن ماه هر دو آمده ولی در عرف فارسی زبانان «کسوف» در آفتاب و «خسوف» در ماه گویند' (MON_part2.txt lines 23134-23146). The Arabic origin tag is there; Mo'in claims no Greek source.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"s.v. کسوف\", \"stance\": \"supports\", \"note\": \"Origin tag '[ع.]' = Arabic, plus the usage note distinguishing Persian kosūf (sun) from xosūf (moon).\"},\n   {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' (v1-v4 pages grepped)\", \"stance\": \"silent\", \"note\": \"No کسوف entry with an etymological footnote was found in the OCR of the Borhan volumes on disk.\"}\n ]\n})\n\nnodes.append({\n \"id\": 15, \"lang\": \"Latin\",\n \"words\": \"eclîpsis\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Latin eclīpsis is a straight learned borrowing of Greek ἔκλειψις, taken over by the astronomical writers (Pliny, and in the Christian period Isidore) with the Greek quantity of the diphthong -ει- rendered by Latin ī; it is declined as a Greek third-declension noun (eclīpsis, -is). Latin also formed the adjective eclīpticus < Gk. ἐκλειπτικός, whence the noun linea ecliptica > ecliptic.\",\n \"derivation_fa\": \"eclīpsis لاتینی وام‌واژه‌ای مستقیم و دانشورانه از ἔklειψις یونانی است که نویسندگان اخترشناس لاتینی (پلینیوس و در دورهٔ مسیحی ایزیدور) آن را گرفته‌اند؛ دوگانه‌واکهٔ ‎-ει-‎ یونانی در لاتینی به ‎ī‎ بدل شده و واژه چون اسم یونانی صرف سوم گردان می‌شود. از آن صفت eclīpticus (از ἐκλειπτικός) و سپس linea ecliptica «دایرةالبروج» ساخته شده است. ادعای نورایی درست است.\",\n \"sources\": [E_ECL],\n \"ref_check\": [\n   {\"ref\": \"AHD:413\", \"status\": \"supports\", \"note\": \"The Watkins appendix gives 'ECLIPSE' under leikw- via Greek leipein; Klein supplies the intermediate Latin step (see consulted). The 1975 New College page 413 itself is not on disk.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.vv. eclipse, ecliptic\", \"stance\": \"supports\", \"note\": \"'eclipse, n. — OF. eclipse (F. éclipse), fr. L. eclipsis, fr. Gk. ἔκλειψις'; 'ecliptic, adj. — L. eclipticus, \\\"pertaining to an eclipse\\\", fr. Gk. ἐκλειπτικός'.\"},\n   {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century Dictionary\", \"stance\": \"silent\", \"note\": \"The local WEB_vol1.txt covers only the first part of the alphabet in usable OCR; no eclipse entry could be read from it.\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet\", \"stance\": \"silent\", \"note\": \"Ernout-Meillet treats only inherited and old Latin vocabulary; eclīpsis, a Greek technical loan, has no entry.\"}\n ]\n})\n\nnodes.append({\n \"id\": 16, \"lang\": \"English\",\n \"words\": \"eclipse\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"English eclipse is attested c. 1300, from Old French eclipse 'eclipse, darkness' (12th c.), from Latin eclīpsis, from Greek ékleipsis; the verb 'to cause an eclipse of' follows in the late 13th c. from Old French eclipser, and the figurative sense 'to overshadow, outshine' from the 1570s. The English spelling keeps the Latin -ps-. The root sense survives in the metaphor: the sun 'forsakes' its usual place.\",\n \"derivation_fa\": \"واژهٔ انگلیسی eclipse از حدود ۱۳۰۰ میلادی گواهی شده است، از فرانسهٔ کهن eclipse «گرفت، تاریکی» (سدهٔ دوازدهم)، از لاتینی eclīpsis، از یونانی ἔκλειψις؛ فعل آن در اواخر سدهٔ سیزدهم از eclipser فرانسهٔ کهن آمده و معنی مجازی «تحت‌الشعاع قرار دادن» از دههٔ ۱۵۷۰. املای انگلیسی ‎-ps-‎ لاتینی را نگاه داشته است. معنی ریشه‌ای در همان استعاره زنده است: خورشید جای همیشگی خود را «فرو می‌گذارد». ادعای نورایی درست است.\",\n \"sources\": [E_ECL],\n \"ref_check\": [\n   {\"ref\": \"AHD:413\", \"status\": \"supports\", \"note\": \"Watkins index: 'ECLIPSE leikw-'; the appendix entry reads 'Basic form *leikw- in Greek leipein, to leave: ECLIPSE, ELLIPSIS'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. eclipse, n. and v.\", \"stance\": \"supports\", \"note\": \"'eclipse, n. — OF. eclipse ... Derivatives: eclipse, tr. v., eclips-er, n.'\"},\n   {\"src\": \"SKT\", \"where\": \"SKT.txt\", \"stance\": \"silent\", \"note\": \"Grepped for '^eclipse' in Skeat's Concise: the OCR of that column is missing/illegible, so no statement could be quoted.\"}\n ]\n})\n\nentry = {\n \"entry\": 0,\n \"root\": \"Leigh 2, Leikw\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *leykʷ- 'to leave, let' (Pokorny 669-670 leikʷ-; LIV 406f.; Watkins leikw-)\",\n \"note\": \"The root, its language label and its gloss are all correct: Pokorny 669-670 has 'Root/lemma: leikʷ- Meaning: to leave', with the perfective present *li-né-kʷ-ti (Skt. riṇákti, Lat. linquō) and the derivatives Gk. λείπω, Gothic leiƕan, Av. raēxnah-, npers. rextan/gurexten. 'Leigh 2' is not a normal transliteration of *leikʷ-; it is Nourai's own alphabetisation headword (the printed page carries 'Leigh 2, Leikw' in the root box and in the running head, and the following entry is the cross-reference 'Leikw — see root: Leigh 2'), so the extraction is faithful and nothing needs fixing. Two branches of the chart are weaker than the rest: the Latin liquēre branch (nodes 6-7) belongs to *wleik- 'to flow' for most modern authorities, though Pokorny prints it on the same page and Ernout-Meillet defend Nourai's grouping; and the Greek > Arabic 'eclipse' branch (node 13) rests on al-Unaysi, who is wrong. Nourai's own reference set on this page is unusually good: POK:669, HRN:141,203, FVQ:46, FFD:72 and TAD:63 all say exactly what he uses them for (whether or not they are right).\",\n \"note_fa\": \"ریشه، برچسب زبانی و معنی آن هر سه درست است: پوکورنی در صفحهٔ ۶۶۹ تا ۶۷۰ ریشهٔ ‎leikʷ-‎ «رها کردن، واگذاشتن» را می‌آورد، با ستاک حالِ میان‌افزودهٔ ‎*li-né-kʷ-ti‎ (سنسکریت riṇákti، لاتینی linquō) و مشتقاتی چون λείπω یونانی، leiƕan گوتی، raēxnah- اوستایی و «ریختن» و «گریختن» فارسی. «Leigh 2» آوانگاری متعارف ‎*leikʷ-‎ نیست بلکه سرواژهٔ الفبایی خود نورایی است؛ صفحهٔ چاپی نیز همین «Leigh 2, Leikw» را در جعبهٔ ریشه و سرصفحه دارد و مدخل بعدی ارجاع «Leikw ← Leigh 2» است، پس خطای خوانش اسکن در کار نیست. دو شاخه از نمودار سست‌ترند: شاخهٔ liquēre لاتینی (خانه‌های ۶ و ۷) که بیشتر مرجع‌های امروزی آن را به ریشهٔ ‎*wleik-‎ «روان شدن» می‌برند، هرچند پوکورنی آن را در همان صفحه چاپ کرده و ارنو-می‌یه از رأی نورایی پشتیبانی می‌کنند؛ و شاخهٔ یونانی ← عربی «کسوف» (خانهٔ ۱۳) که بر گفتهٔ نادرست العنیسی استوار است. در مجموع ارجاع‌های خودِ نورایی در این صفحه به‌طور غیرمعمول دقیق‌اند: POK:669 و HRN:141,203 و FVQ:46 و FFD:72 و TAD:63 همه دقیقاً همان را می‌گویند که او از آن‌ها خواسته است.\",\n \"sources\": [W_PIE, E_ECL, E_ELE, E_LOA],\n \"ref_check\": [\n   {\"ref\": \"POK:669\", \"status\": \"supports\", \"note\": \"POK_full.txt, 'Root/lemma: leikʷ- Meaning: to leave ... Material: Old Indic rinakti ... Avestan raexnah- \\\"blessing, treasure, tribute, inheritance\\\", -irinaxti ... npers. rextan \\\"diffuse\\\", gurexten \\\"miss\\\" ... gr. λείπω ... Latin linquo ... Gothic leiƕan ... Page(s): 669-670.' Exactly the page Nourai cites.\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. II 396-397\", \"stance\": \"supports\", \"note\": \"'1. leiqʷ- \\\"lassen, zurück-, übriglassen\\\"' with the same Indo-Iranian, Greek, Latin, Germanic and Baltic material; the reference line of Pokorny 669 is 'WP. II 396 f.'\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins s.v. leikw-\", \"stance\": \"supports\", \"note\": \"'leikw-. To leave. 1. Basic form *leikw- in Greek leipein ... 2. O-grade form *loikw- ... LEND, LOAN. 3. Zero-grade form *likw- in Germanic *-lif- ... 4. Nasalized zero-grade form *li-n-kw- in Latin linquere ... [Pok. leikʷ- 669.]'\"},\n   {\"src\": \"IEC\", \"where\": \"Mann s.vv. leiquo, leiqusos, liquos, liqutos\", \"stance\": \"supports\", \"note\": \"'leiquo \\\"leave, let, allow, remain\\\" ... WP II, 396. Skt. recāmi \\\"evacuate, leave\\\"; Av. (radical) rič-, id.; Myc. leiq-, Gk. leípō ... Lat. cf. liquī, pf. \\\"I left\\\" ... Go. leihvan \\\"lend\\\".'\"},\n   {\"src\": \"CHEUNG\", \"where\": \"p. 307 *raič\", \"stance\": \"supports\", \"note\": \"'*raič \\\"to leave, let, abandon\\\" ... *PIE *leikʷ- \\\"to leave, let\\\" > LIV: 406 f. | Pok.: 669 f.' — the modern Iranian handbook keeps the same root for the Avestan/Persian branch.\"}\n ],\n \"nodes\": nodes\n}\n\ndoc = {\n \"pdf_page\": 307,\n \"book_page\": 277,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-06\",\n \"entries\": [entry]\n}\n\nwith open(\"/home/sfmqrb/git/rishe/data/verification/page-307.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(doc, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk307.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-307.json > /dev/null && echo \"JSON OK\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 307"
}
```


### [2026-09-06T23:26:12.705Z] TOOL RESULT

```
ok
JSON OK
nodes verified: 16/16
node verdicts: {'disputed': 2, 'plausible': 4, 'confirmed': 10}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 14, 'not_found': 3, 'partial': 1, 'not_checked': 4, 'contradicts': 1}
books consulted: {'supports': 30, 'partial': 6, 'contradicts': 5, 'silent': 9} | by book: {'KLN': 9, 'POK': 5, 'CHEUNG': 3, 'WLD': 3, 'AHD': 3, 'IEC': 3, 'SKT': 3, 'HUB': 2, 'HRN': 2, 'MON': 2, 'FVQ': 2, 'BQT': 2, 'LAT': 2, 'BRT': 1, 'PHD': 1, 'NYB': 1, 'FFD': 1, 'ARY': 1, 'AFM': 1, 'PLA': 1, 'ARB': 1, 'WEB': 1}
```


## [2026-09-06T23:26:38.726Z] AGENT

Verification complete for PDF page 307 (book page 277). `verify_check.py 307` reports 16/16 nodes, 0 PROBLEM lines.

**Page 307 — root "Leigh 2, Leikw" (PIE \*leykʷ- "to leave"), 1 entry, 16 nodes**

Verdicts: root **confirmed**; nodes **10 confirmed, 4 plausible, 2 disputed**.
Ref checks: 14 supports, 1 contradicts, 1 partial, 3 not_found, 4 not_checked.

Disputed:
- **#1 Avestan** (`raexnah…; rěxt, rěz, hâek 1; paiti-raeč; vi-raeč`) — Av. raēk-/raēc- and raēxnah- and paiti-raēc- are all correct (Bartholomae AiW 1479-81, Cheung 307), but `hâek 1` is Av. haēk- "to pour", which Pokorny 893f. puts under a *different* root \*seikʷ-; and `rěxt, rěz` are Middle/New Persian, not Avestan. `vi-raeč` is unattested in Avestan (a legitimate reconstruction only).
- **#13 Arabic kosŭf, xosŭf < Greek ekleipsis** — al-Unaysi (TAD:63) really does say this (verified from the page image), but kusūf/xusūf are ordinary fuʿūl maṣdars of two native Arabic roots k-s-f and x-s-f, both Qur'anic; two roots cannot come from one Greek noun. Wiktionary, Jeffery and al-Jawālīqī all treat them as native.

Plausible (noted, not errors):
- **#6/#7 Latin liquēre → liquid, liquor** — AHD (the reference Nourai cites!) files LIQUID under \*wleik-, as do Walde-Pokorny II 398, Klein and Etymonline; Ernout-Meillet s.v. *liqueō* do defend Nourai's grouping, and Pokorny prints the material on p. 669.
- **#2/#3 Pahlavi/Persian** — گریختن and پرهیختن confirmed (MacKenzie, Nyberg, Cheung 307, Horn 141/203, Abolghasemi 72); ریختن "to pour" is placed here by Pokorny, Bartholomae, Horn, Nyberg and Abolghasemi, but Cheung 2007:187 (followed by Wiktionary) splits it off as \*Hraič with no IE correspondence. Also `âp-rex` is unattested Pahlavi (reconstructed \*ābrēz/\*ābrēk), and `par-hěxtan` is really the New Persian shape (MP = pahrēxtan).

**No extraction errors** — I rendered PDF p. 307 and the JSON matches the printed chart exactly, including the odd root headword "Leigh 2, Leikw" (the book's own alphabetisation label, printed in the box and running head).

Notes for the owner: the strongest confirmation on this page is the ابریق round trip (MP āb-rēz → Ar. ibrīq → NP ابریق), independently confirmed by Jeffery FVQ:46, Horn 141, Addi Shir p. 6 and Mo'in's own tag «[معر. آبریز]». SNS:115 is one page off (the pahrēz entry is on p. 116); SOD:11 could not be located in Gharib (neither page nor entry 11 is relevant); AEF:373 is not obtainable (its German original, Horn 638, was checked instead). I saved the TAD page-63 image and a verbatim vision transcript to `/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/TAD/63.jpg` and `63.vision.txt`, and archived 11 web pages via `fetch_source.py`.
