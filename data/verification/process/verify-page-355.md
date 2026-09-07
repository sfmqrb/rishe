# Verification process log — verify-page-355


## [2026-09-07T18:17:57.739Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 355 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-355.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-355.json. Write /home/sfmqrb/git/rishe/data/verification/page-355.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 355` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T18:17:59.858Z] AGENT

I'll start by reading the instructions.


## [2026-09-07T18:18:00.564Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T18:18:00.577Z] TOOL RESULT

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


## [2026-09-07T18:18:01.158Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-355.txt"
}
```


### [2026-09-07T18:18:01.176Z] TOOL RESULT

```
1	=== PDF page 355 (book page 325) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Nei 1, Ni 2 : to shine, to be excited  (refs POK:760)  PART 1
4	#1 (parent #0) [Old Persian] refs=POK:760; KNT:192; AIN:59; SPG:227 | ni 3, naiba : beautiful, brave, good
5	  #2 (parent #1) [Pahlavi] refs=SNS:291; BQT:2237; AIN:60 | něv : brave ; něv-ak : good
6	    #3 (parent #2) [Persian] refs=KLN:1033; BQT:2127; TZF:20 | Nîv «نیو ( نیوان )» : brave ; nard 1 «نرد ۱» : backgammon, distorted form of "Nîv Ardeshîr" ☞Ar ; nîk «نیک ( نیکو )» : good, pure
7	      #4 (parent #3) [Persian] refs=PLA:27 | âbnîk «آب نیک» : good (distilled) water? ☞Ab 1
8	        #5 (parent #4) [Greek] refs=WEB:44 | ambix : a cup used in distilling water
9	        #6 (parent #4) [Arabic] refs=WEB:44; PLA:27 | al-anbîq, al-ambîq : distilling apparatus | NOTE: May have been derived from Greek "ambix" which is related to the Persian word (WEB:44 & TAD:4).
10	          #7 (parent #6) [Persian] refs=MON:362 | anbîq «انبیق» : distilling apparatus
11	          #8 (parent #6) [Spanish] refs=KLN:47 | alambique : distilling apparatus
12	            #9 (parent #8) [French] refs=KLN:47 | alambic | NOTE: May be through Latin "alambicum"
13	              #10 (parent #9) [English] refs=None | alembic
14	          #11 (parent #6) [Persian] refs=None | rŭnîk «رونیک ( نیکرو )» : beautiful ☞Leudh
15	            #12 (parent #11) [Arabic] refs=AFM:74; FVF:297 | raonaq : beauty, splendor
16	              #13 (parent #12) [Persian] refs=MON:1694 | rownaq «رونق» : splendor, success
17	#14 (parent #0) [Latin] refs=KLN:1033 | ni-těre : to shine
18	  #15 (parent #14) [English] refs=None | neat ; net 1 : pure
19	
```


## [2026-09-07T18:18:04.698Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/extracted/batch/page-355.json",
 "description": "Read source JSON for page 355"
}
```


### [2026-09-07T18:18:04.741Z] TOOL RESULT

```
{
  "pdf_page": 355,
  "book_page": 325,
  "entries": [
    {
      "root": {
        "name": "Nei 1, Ni 2",
        "lang": "Indo-European",
        "refs": "POK:760",
        "gloss": "to shine, to be excited"
      },
      "part": 1,
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "POK:760; KNT:192; AIN:59; SPG:227",
          "words": [
            {"translit": "ni 3, naiba", "gloss": "beautiful, brave, good", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "SNS:291; BQT:2237; AIN:60",
          "words": [
            {"translit": "něv", "gloss": "brave", "script": null},
            {"translit": "něv-ak", "gloss": "good", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "KLN:1033; BQT:2127; TZF:20",
          "words": [
            {"translit": "Nîv", "gloss": "brave", "script": "نیو ( نیوان )"},
            {"translit": "nard 1", "gloss": "backgammon, distorted form of \"Nîv Ardeshîr\"", "script": "نرد ۱", "see": ["Ar"]},
            {"translit": "nîk", "gloss": "good, pure", "script": "نیک ( نیکو )"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "چو طوس و چو گودرز گشواد و گیو - چو گرگین و فرهاد و بهرام نیو",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "PLA:27",
          "words": [
            {"translit": "âbnîk", "gloss": "good (distilled) water?", "script": "آب نیک", "see": ["Ab 1"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Greek",
          "refs": "WEB:44",
          "words": [
            {"translit": "ambix", "gloss": "a cup used in distilling water", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 4,
          "lang": "Arabic",
          "refs": "WEB:44; PLA:27",
          "words": [
            {"translit": "al-anbîq, al-ambîq", "gloss": "distilling apparatus", "script": null}
          ],
          "script_extra": null,
          "note": "May have been derived from Greek \"ambix\" which is related to the Persian word (WEB:44 & TAD:4).",
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Persian",
          "refs": "MON:362",
          "words": [
            {"translit": "anbîq", "gloss": "distilling apparatus", "script": "انبیق"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 6,
          "lang": "Spanish",
          "refs": "KLN:47",
          "words": [
            {"translit": "alambique", "gloss": "distilling apparatus", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "French",
          "refs": "KLN:47",
          "words": [
            {"translit": "alambic", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": "May be through Latin \"alambicum\"",
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "alembic", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 6,
          "lang": "Persian",
          "refs": null,
          "words": [
            {"translit": "rŭnîk", "gloss": "beautiful", "script": "رونیک ( نیکرو )", "see": ["Leudh"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 11,
          "lang": "Arabic",
          "refs": "AFM:74; FVF:297",
          "words": [
            {"translit": "raonaq", "gloss": "beauty, splendor", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 12,
          "lang": "Persian",
          "refs": "MON:1694",
          "words": [
            {"translit": "rownaq", "gloss": "splendor, success", "script": "رونق"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 0,
          "lang": "Latin",
          "refs": "KLN:1033",
          "words": [
            {"translit": "ni-těre", "gloss": "to shine", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 14,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "neat", "gloss": null, "script": null},
            {"translit": "net 1", "gloss": "pure", "script": null}
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


## [2026-09-07T18:18:07.565Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KNT','AIN','SPG','SNS','BQT','TZF','KLN','PLA','WEB','MON','AFM','FVF','TAD','WLD','AHD','HRN','HUB','PHD','NYB','IEC','SYN','SKT','FSD','LKT','DEV','PHN','FVQ','ARY','BRT','CHEUNG','DOZ','LAM','AFA','HJB','AID','TTS','SOD']:\n    v=d.get(k)\n    print(k, json.dumps(v, ensure_ascii=False)[:400] if v else 'MISSING')\n\"",
 "description": "Check reference metadata"
}
```


### [2026-09-07T18:18:08.856Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
AIN {"title": "E. Lidén, Studien zur altindischen und vergleichenden Sprachgeschichte, Uppsala 1897", "edition_found": "1897", "kind": "archive_djvu", "url": "https://archive.org/details/studienzuraltin00lidgoog", "identifier": "studienzuraltin00lidgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AIN.txt", "page_offset": "leaf = printed + 5 (e.g. leaf 9 = p.4). local file ha
SPG {"title": "F. Spiegel - title lost in the bibliography OCR (Table IV no. 93 is missing); Table III lists Spiegel with SPG and ARP. Best guesses: Die altpersischen Keilinschriften (2nd ed. 1881) or Eranische Alterthumskunde (1871-78)", "edition_found": "Die altpersischen Keilinschriften, 2. Aufl. 1881 (downloaded as a guess)", "kind": "archive_djvu", "url": "https://archive.org/details/diealtpersis
SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
TZF {"title": "Mohsen Abolghasemi, Tarikh-e Mokhtasar-e Zaban-e Farsi, Bonyad-e Andisheh-ye Eslami 1373/1994", "kind": "website", "url": "https://ketabnak.com/book/81646 (142 pp. PDF; login) ; https://farhangoadabeirani.blogsky.com/1395/07/20/post-1048/ (download post)", "lookup_hint": "Not on archive.org (only his دستور تاریخی زبان فارسی: archive.org/details/20220417_20220417_2237, and تاریخ زبان فار
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_page
FVF {"title": "S.M.A. Emam Shushtari, Farhang-e Vazheha-ye Farsi dar Zaban-e Arabi, Anjoman-e Asar-e Melli 58, Tehran 1347/1968", "kind": "website", "url": "https://noorlib.ir/book/info/105056 (page viewer: https://noorlib.ir/book/view/105056?pageNumber=<N>&viewType=pdf) ; https://ketabnak.com/book/48613 (818 pp. PDF, login) ; http://parsianjoman.org/?p=1265 (download post)", "lookup_hint": "Alphabeti
TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://a
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 =
DEV {"title": "L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876", "edition_found": "1876", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairety00devi", "identifier": "dictionnairety00devi (also dictionnairetym02devigoog, fr105comparative41)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt", "page_offset": "leaf
PHN {"title": "A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, Paris 1866", "edition_found": "1866", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairetym01pihagoog", "identifier": "dictionnairetym01pihagoog (others: bub_gb_QnsSAAAAIAAJ, dictionnairetym00pihagoog)", "local_file": "/home/sfmqrb/git/rishe/data/verific
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.t
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
CHEUNG MISSING
DOZ {"title": "R. Dozy, Oosterlingen: Verklarende lijst der Nederlandsche woorden die uit het Arabisch, Hebreeuwsch, Chaldeeuwsch, Perzisch en Turksch afkomstig zijn, Leiden 1867", "edition_found": "1867", "kind": "archive_djvu", "url": "https://archive.org/details/oosterlingenver00dozygoog", "identifier": "oosterlingenver00dozygoog (also ...01dozygoog, ...02dozygoog)", "local_file": "/home/sfmqrb/git
LAM {"title": "H. Lammens, Remarques sur les mots français dérivés de l'arabe, Beyrouth 1890", "edition_found": "1890", "kind": "archive_djvu", "url": "https://archive.org/details/remarquessurles00lammgoog", "identifier": "remarquessurles00lammgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAM.txt", "page_offset": "leaf = printed + 57 (e.g. leaf 59 = p.2). local file has \
AFA {"title": "S. Fraenkel, Die aramäischen Fremdwörter im Arabischen, Leiden 1886 (repr. Hildesheim 1962, same pagination)", "edition_found": "1886", "kind": "archive_djvu", "url": "https://archive.org/details/diearamischenfr00fraegoog", "identifier": "diearamischenfr00fraegoog (also bub_gb_SzdbAAAAQAAJ)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFA.txt", "page_offset": "
HJB {"title": "H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)", "edition_found": "1903 Crooke edition (pagination identical to the 1968 reprint)", "kind": "archive_djvu", "url": "https://archive.org/details/hobsonjobsonagl02croogoog", "identifier": "hobsonjobsonagl02croogoog (others: bub_gb_6Z5iAAAAMAAJ, hobsonjobsonglos00yulerich, india.history.resource
AID {"title": "G. C. Whitworth, An Anglo-Indian Dictionary, London 1885", "edition_found": "1885 (DLI scan); also 1981 reprint scan", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.45332", "identifier": "in.ernet.dli.2015.45332 (also anglo-indiandictionary, 1981 reprint)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AID.txt", "page_offset": "leaf
TTS {"title": "H. Vámbéry, Etymologisches Wörterbuch der turko-tatarischen Sprachen, Leipzig 1878 (repr. Osnabrück 1972)", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/etymologischesw00vmuoft (Toronto scan; also Google/bub_gb copies)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft.pdf", 
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in
```


## [2026-09-07T18:18:32.134Z] TOOL CALL #5: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo --- && cat data/verification/sources/SOURCE_MATRIX.md | head -80",
 "description": "List verification dir and source matrix"
}
```


### [2026-09-07T18:18:32.181Z] TOOL RESULT

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
```


## [2026-09-07T18:18:34.292Z] TOOL CALL #6: Bash

```json
{
 "command": "pdftoppm -f 355 -l 355 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg355 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/",
 "description": "Render page 355 to PNG"
}
```


### [2026-09-07T18:18:36.241Z] TOOL RESULT

```
total 20060
drwx------ 2 sfmqrb sfmqrb     4096 Sep  7 14:18 .
drwx------ 4 sfmqrb sfmqrb     4096 Sep  7 11:48 ..
-rw-rw-r-- 1 sfmqrb sfmqrb     8635 Sep  7 12:07 318-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   101267 Sep  7 12:07 318-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61586 Sep  7 12:18 320-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   115970 Sep  7 12:18 320hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    86272 Sep  7 12:18 320-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    13284 Sep  7 12:18 320-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   107524 Sep  7 12:27 328-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    43713 Sep  7 12:35 331-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   135301 Sep  7 12:35 331-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    52382 Sep  7 12:41 333-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    88345 Sep  7 12:41 333-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    68568 Sep  7 12:43 335-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   105946 Sep  7 12:43 335-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   111897 Sep  7 13:57 340hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    24993 Sep  7 13:57 340-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    92337 Sep  7 13:59 342-mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb    92697 Sep  7 13:56 343hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30778 Sep  7 13:56 343-mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61503 Sep  7 13:52 346-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1011 Sep  7 14:18 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    14937 Sep  7 11:56 arrows.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1413 Sep  7 12:27 box1b.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1385 Sep  7 12:27 box1.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1132 Sep  7 12:27 box2b.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1988 Sep  7 12:27 box2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    85949 Sep  7 11:57 bqt2002_a.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72256 Sep  7 11:58 bqt2002_f1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   161214 Sep  7 11:57 bqt2002_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   153966 Sep  7 13:44 bqt2014_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63319 Sep  7 12:40 build333.py
-rw-rw-r-- 1 sfmqrb sfmqrb    83643 Sep  7 12:12 build.py
-rw-rw-r-- 1 sfmqrb sfmqrb     7075 Sep  7 12:13 c331_av1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10759 Sep  7 12:13 c331_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3537 Sep  7 11:53 c_migare2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1829 Sep  7 11:53 c_migare3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2261 Sep  7 11:53 c_migare4.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3958 Sep  7 11:53 c_migare.png
-rw-rw-r-- 1 sfmqrb sfmqrb    46690 Sep  7 13:44 crop_av3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    40759 Sep  7 13:44 crop_heb.png
-rw-rw-r-- 1 sfmqrb sfmqrb    94819 Sep  7 13:44 crop_pers0.png
-rw-rw-r-- 1 sfmqrb sfmqrb    19652 Sep  7 11:53 c_semita2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2639 Sep  7 11:53 c_semita.png
-rw-rw-r-- 1 sfmqrb sfmqrb    40259 Sep  7 11:50 ferdowsi2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30950 Sep  7 11:51 ferdowsi3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    28946 Sep  7 11:51 ferdowsi4.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4298 Sep  7 11:50 ferdowsi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78732 Sep  7 13:40 ffd32.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61328 Sep  7 13:44 ffd82.png
-rw-rw-r-- 1 sfmqrb sfmqrb     9383 Sep  7 11:55 masjid.wiki
-rw-rw-r-- 1 sfmqrb sfmqrb    33701 Sep  7 12:04 mk319a.py
-rw-rw-r-- 1 sfmqrb sfmqrb    46151 Sep  7 12:09 mk319b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    51516 Sep  7 12:09 mk322.py
-rw-rw-r-- 1 sfmqrb sfmqrb    61981 Sep  7 12:06 mk323.py
-rw-rw-r-- 1 sfmqrb sfmqrb    63978 Sep  7 12:35 mk330.py
-rw-rw-r-- 1 sfmqrb sfmqrb    64100 Sep  7 12:34 mk331.py
-rw-rw-r-- 1 sfmqrb sfmqrb    90456 Sep  7 12:42 mk332.py
-rw-rw-r-- 1 sfmqrb sfmqrb    99976 Sep  7 12:34 mk334.py
-rw-rw-r-- 1 sfmqrb sfmqrb    57252 Sep  7 12:38 mk337.py
-rw-rw-r-- 1 sfmqrb sfmqrb    83271 Sep  7 13:58 mk338.py
-rw-rw-r-- 1 sfmqrb sfmqrb    74349 Sep  7 13:57 mk340.py
-rw-rw-r-- 1 sfmqrb sfmqrb    59512 Sep  7 13:57 mk341.py
-rw-rw-r-- 1 sfmqrb sfmqrb    82502 Sep  7 13:57 mk342.py
-rw-rw-r-- 1 sfmqrb sfmqrb    66284 Sep  7 13:55 mk343.py
-rw-rw-r-- 1 sfmqrb sfmqrb    58811 Sep  7 13:57 mk344.py
-rw-rw-r-- 1 sfmqrb sfmqrb    36436 Sep  7 13:51 mk348b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    20510 Sep  7 13:47 mk348.py
-rw-rw-r-- 1 sfmqrb sfmqrb    61503 Sep  7 13:42 navak2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3021 Sep  7 13:42 navak.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1525 Sep  7 13:41 p342_box2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1759 Sep  7 13:41 p342_box3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1703 Sep  7 13:41 p342_box.png
-rw-rw-r-- 1 sfmqrb sfmqrb   108903 Sep  7 13:41 p342hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10531 Sep  7 13:39 p343_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30408 Sep  7 13:39 p343_mus.png
-rw-rw-r-- 1 sfmqrb sfmqrb    21223 Sep  7 13:47 part1.json
-rw-rw-r-- 1 sfmqrb sfmqrb    37635 Sep  7 12:04 part_a.json
-rw-rw-r-- 1 sfmqrb sfmqrb    58545 Sep  7 12:09 part_b.json
-rw-rw-r-- 1 sfmqrb sfmqrb    97817 Sep  7 11:50 pg318hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    62558 Sep  7 11:50 pg318.png
-rw-rw-r-- 1 sfmqrb sfmqrb    67293 Sep  7 11:54 pg319.png
-rw-rw-r-- 1 sfmqrb sfmqrb   146848 Sep  7 12:01 pg320hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    80891 Sep  7 12:00 pg320.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71522 Sep  7 12:00 pg321.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72193 Sep  7 11:57 pg323.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65279 Sep  7 11:49 pg324.png
-rw-rw-r-- 1 sfmqrb sfmqrb    55902 Sep  7 11:58 pg326.png
-rw-rw-r-- 1 sfmqrb sfmqrb   163982 Sep  7 11:53 pg327hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    73619 Sep  7 11:52 pg327.png
-rw-rw-r-- 1 sfmqrb sfmqrb    69765 Sep  7 12:12 pg329.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72757 Sep  7 12:13 pg330.png
-rw-rw-r-- 1 sfmqrb sfmqrb   128240 Sep  7 12:13 pg331hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    94945 Sep  7 12:12 pg331.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75312 Sep  7 12:17 pg332.png
-rw-rw-r-- 1 sfmqrb sfmqrb   104609 Sep  7 12:27 pg333hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70886 Sep  7 12:26 pg333.png
-rw-rw-r-- 1 sfmqrb sfmqrb    41782 Sep  7 12:18 pg334_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    97297 Sep  7 12:18 pg334.png
-rw-rw-r-- 1 sfmqrb sfmqrb    58407 Sep  7 12:18 pg334_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    88659 Sep  7 12:22 pg335.png
-rw-rw-r-- 1 sfmqrb sfmqrb    57846 Sep  7 12:31 pg336.png
-rw-rw-r-- 1 sfmqrb sfmqrb    60414 Sep  7 12:19 pg337.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65267 Sep  7 13:37 pg338.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63922 Sep  7 13:44 pg339.png
-rw-rw-r-- 1 sfmqrb sfmqrb   111897 Sep  7 13:44 pg340hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    64116 Sep  7 13:39 pg341.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75149 Sep  7 13:40 pg342.png
-rw-rw-r-- 1 sfmqrb sfmqrb    64151 Sep  7 13:39 pg343.png
-rw-rw-r-- 1 sfmqrb sfmqrb    60735 Sep  7 13:42 pg344.png
-rw-rw-r-- 1 sfmqrb sfmqrb   168870 Sep  7 13:42 pg346hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    76794 Sep  7 13:39 pg346.png
-rw-rw-r-- 1 sfmqrb sfmqrb    69045 Sep  7 14:18 pg355.png
-rw-rw-r-- 1 sfmqrb sfmqrb        0 Sep  7 13:36 queue.txt
-rw-rw-r-- 1 sfmqrb sfmqrb       49 Sep  7 12:17 sns53.png
-rw-rw-r-- 1 sfmqrb sfmqrb    35039 Sep  7 12:17 sns_n53.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    35039 Sep  7 12:17 sns_n54.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  1021826 Sep  7 12:18 sns_p54.png
-rw-rw-r-- 1 sfmqrb sfmqrb 12288786 Sep  7 12:18 sns_text.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb      341 Sep  7 13:46 s.py
-rw-rw-r-- 1 sfmqrb sfmqrb     1308 Sep  7 11:54 v2001.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    27253 Sep  7 12:02 z_maqd2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63140 Sep  7 12:02 z_maqd3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4293 Sep  7 12:01 z_maqd.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2895 Sep  7 12:01 z_meh.png
-rw-rw-r-- 1 sfmqrb sfmqrb    25378 Sep  7 12:01 z_mezna2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    33685 Sep  7 12:01 z_mezna.png
```


## [2026-09-07T18:18:40.149Z] TOOL CALL #7: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg355.png"
}
```


### [2026-09-07T18:18:40.501Z] TOOL RESULT

```

```


## [2026-09-07T18:18:40.499Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-07T18:18:58.767Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && pdftoppm -f 355 -l 355 -r 400 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf p355hi && python3 -c \"\nfrom PIL import Image\nim=Image.open('p355hi.png'); print(im.size)\n# crop left connector region: x 400-700 (at 200dpi) -> double for 400dpi\nim.crop((850,1250,1300,2200)).save('c355_conn.png')\nim.crop((950,2000,2100,2400)).save('c355_runik.png')\n\"",
 "description": "Crop connector region at high res"
}
```


### [2026-09-07T18:19:01.605Z] TOOL RESULT

```
(3400, 4400)
```


## [2026-09-07T18:19:04.653Z] TOOL CALL #9: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/c355_conn.png"
}
```


### [2026-09-07T18:19:04.669Z] TOOL RESULT

```

```


## [2026-09-07T18:19:11.247Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('p355hi.png')\nim.crop((850,2100,2200,2600)).save('c355_runik2.png')\nim.crop((700,2400,2700,2900)).save('c355_arab2.png')\n\"",
 "description": "Crop runik region"
}
```


### [2026-09-07T18:19:13.026Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-07T18:19:15.812Z] TOOL CALL #11: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/c355_runik2.png"
}
```


### [2026-09-07T18:19:15.833Z] TOOL RESULT

```

```


## [2026-09-07T18:19:29.685Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nf=open('POK_full.txt',encoding='utf-8',errors='replace').read()\npages=f.split('\\f')\nprint('npages',len(pages))\n# find page markers\nfor i,p in enumerate(pages[:5]):\n    print('---',i,repr(p[:200]))\nEOF",
 "description": "Inspect POK_full structure"
}
```


### [2026-09-07T18:19:30.885Z] TOOL RESULT

```
npages 1
--- 0 'List of language abbreviations in tlie lED \n\n\n\nAbbreviation Language name \n\n\nAeq. \n\n\n\n\nAequian \n\n\nAkk. \n\n\n\n\nAkkadian \n\n\nAlan. \n\n\n\n\nAlanian (=Old Ossetic) \n\n\nAlb. \n\n\n\n\nAlbanian \n\n\nAnat. \n\n\n\n\nAnatolian '
```


## [2026-09-07T18:19:30.986Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"naiba\" KNT.txt | head -20; echo \"=== BRT naiba\"; grep -n -i \"naiba\" BRT.txt | head -20",
 "description": "Grep naiba in Kent and Bartholomae"
}
```


### [2026-09-07T18:19:31.047Z] TOOL RESULT

```
982:Also vaindhy, Skt. ind. vénati; haind, Skt. sénd; айа, duvaislam, gaibam, naibam, -tary, -$au, tyaty.
1042:V. OP p bf are in some instances not traceable to pIE forebears or are definitely borrowings from outside sources; such are piru- ‘ivory’, si"kabru- ‘carnelian’, naiba- ‘good’ (only in Iranian), and many place and personal names, such as Pirdva ‘Nile’, Putdya- ‘Libyan’, Babirus ‘Babylon’, Arabdéya ‘Arabia’, Arbatrü- ‘Arbela’, Ufrütu- ‘Euphrates’, Nadifaba?ra ‘Nidintu-Bel’, Nabukudracara ‘Nebuchadrezzar’.
1778:IIT. With no obvious simpler nominal or verbal form: ama- in Arsdma-, asa- aspa-, u-ba-, poss. ^upa-, kaufa-, kara-, daiva-, darga-, naiba-, Parsa-, pisa-, Máda-, raba- in u-rafa-, varka- in Varkána- and Varka-zana-, Saka-, späda- in Taxma-spáda-, spára- in Vdya-spara-; the restored hana- in hana- {й-; mayüra-, of uncertain etymology; the pos- sible vāra- in ^U-vára-zmi-.
2716:Е. With or without prepositions, to denote place where or within which: DB 1.92 vardanam amu» Ufrātwã ‘a town beside the Euphrates’; DB 3.26 kära Parsa hya vapatüj ‘the Persian army which (was) in the palace’; XPa 13f vasiy aniyaSciy naibam kartam ana Parsé ‘much other good (construction) was built within this (city) Persepolis’.
4214:DSe = Darius, Susa Е. 1 baga : vazraka : Auramazdà : hya : ima 2 т: bimim : adadé ; һуа : avam : as 3 татат : adadà : hya : martiyam : ad 4 ada : hya : &iyàülim : adad& : mart 5 iyahyü : hya : Darayavaum : XŠm : ak 6 unauš : айбат : parūvnām : XSm : a 7 шат : parüvnüm : framálàram : a 8 dam : Darayavaus : XS : vazraka : XS : XSy 9 anim : XS : dahyünám : vispazanü 10 nam : XS : ahyaya : bümiyà : vaz 11 rakàyà : düraiy : apiy : Vistas 12 pahyà : puça : HazamaniSya : Рат 13 sa : Pārsahyā : рисо : Ariya : Ari 14 ya : ciga : 08tiy : Dàrayavaus : XS : 15 уа&па : Auramazdaha : imá : dahy 16 āva : {уй : adam : agarbayam : apaia 17 ram : hacd : Parsa : adamsdm : pat 18 iyaxíayaty : manā : bajim : abara : 19 tyasam : hacéma : afahya : ava : aku 20 nava : datam : tya : mand : avadis : a 21 dáraya : Майа: Uja : Parðava : Haraiva : 22 Baatris : Suguda : Uvarazmis 23 : Zrdka : Наташайх : Bataguš : Maci 24 уй : Gadàra : Hidus : Зака : haumava 25 rgà : Saká : tigrazaudà : Babir 26 u$ : Авита : Arabéya : Мийгаа : 27 Armina : Katpatuka : Sparda : Yaun 28 à : аву : drayahya : ula : уа 29 y : paradraya : Skudra : Putayà : 30 Kuxiyd : Karka ; 6àtiy : Рата 31 yavau& : XS : vasiy : tya : duskarta 32 m : Gha : ava : naibam : akunavam : da 33 hyáva : ayauda : aniya : aniyam : 34 aja : ava : adam : akunavam : vašnā 39 : Auramazdaha : уаба : aniya : a 36 шуат : пау : jatiy : cind : gà 37 fava : kaSciy : astiy : дат : 38 tya : maná : haeá : avana : tarsat 39 y : улда : hya : tauviyd : tyam :s 40 kauéim : naiy : jatiy : naiy : vi 41 mardatiy : байу : Dérayavaus :
4307:2 hyayd BUyā : Vistáspahyd : риса : Haxümanisiya : 0 3 atiy : Dárayavaus XS : yaķā : АМ : тт: XSyam : akunaus : 4 ahyayé BUyà : vaina : AMha: visam : naibam : akunavam
4308:Norte to DSi: * For restoration, ef. XPg 4, XV 20; but the Akk. does not warrant Brd.'s visam tya naibam, WZKM 39.43; cf. XPh 43.
4447:3 ada : hya : Syátim : ada : martiyahyà : һуа 4 : XSavarSim : xSiyafiyam : akunaué : aivam : 5 parünàm : xSayatiyam : aivam : parünàm : fram 6 àtàram : adam : XSayarsa : xSayafiya : vazraka : 7 xšāyaðiya : хёйуайїуйпаш : x&ayafiya : dahy _ 8 ünàm : paruv : zanànàm : хёйуадіуа : ahyay 9 & : bümlyà : vazrakáyà : düraiy : apiy : Da 10 rayavahaus : x&ayafiyahyà : риса : Haxémanis П iya : 0atiy : Xšayāršā : xšāyaðiya : vasna : 12 Auramazdáhà : imam : duvarfim : visadahyum 13 : adam : akunavam : vasiy : aniyascly : naibam 14 : kartam : апа : Parsi : tya : adam : akunavam : 15 utamaiy : tya : рія : akunaus : tyapatiy : ka 16 riam : vainataly : парага : ava : visam : vaSnà : А 17 uramazdaha : akumà : Qatiy : Xšayāršā : 18 xSayafiya : mam : Auramazda : pātuv : utamai 19 y : xSacam : ut& : tya : manā : kartam : uta : tyamai 20 y : pica : kartam : avaseiy : Auramazda : patuv
4532:XPg = XERXES, PERSEPOLIS G. 1 байу: XSayarsa : 2 x&àyafya : vazraka : vaš 3 ni : Auramazdiha : vasi 4 y : tya : naibam : akunau 5 $:utà : fràmáyatà : 6 Darayavaus : xSayabiya 7 :hya: mana : pita : vas 8 парту : Auramazdiha 9 : adam : abiyajivayam 10 :abiy : ava : kartam : 11 uta : frataram : akuna 12 vam : mim : Auramazdà 18 : pátuv : hada : bagai 14 bi$ : utamaiy : xSacam
4597:42 œ : àha : tya : duskartam : akariya : ava : ada 43 m :naibam :akunavam : aita : tya : adam :ak 44 unavam : visam : vasnà : Auramazdaha : aku 45 navam : Auramazdaimaiy : upastám :abara : у 46 ata : kartam : akunavam : tuva : kā : hya : 47 apara : yadimaniyaiy : йуй{а : ahanty
4656:9 framàátàram : adam : Xšayāršā : 10 x&àyafiya : vazraka : хёдуабуа : 11 xšāyaðiyānām : xšāyaðiya : da 12 hyünàm : paruv : zanànàm : x$ 13 àya8iya : ahy&yà : bümiyà : va 14 zrakày& : düraiy : apiy : Daraya 15 vahaus : xšāyaðiyahyā : риса : Ha 16 x&manisiya :0ütiy : XSayársá 17 : xSayabiya : Dārayavauš : xSiya 18 буа : һуа : manā : pitä : hauv : va 19 502 : Auramazdaha : vasiy : tya : 20 naibam : akunauég : uta : ima : st 21 änam : hauv : niyastdya : katanaiy 22 : yaniy : dipim : naiy : nipist 23 ām : akunaus : pasáva : adam : ni 24 yastéyam : та : dipim : піра 25 iStanaiy : màm : Auramazda : pa 26 tuv : hada : бадафт : utämai 27 y : zSaqam : Ша : атану : kartam
4910:The alphabetic orderisáf dk zgejt6 edn pfo тутіоѕ §zh, while final y and v are disregarded (thus пату has the alphabetic place of nai, and pre- cedes naiba-). Raised letters inserted to show sounds omitted in the OP system of writing also have no effect on the alphabetic order.
5574:| du$karia- ad). ‘ill-done’, opposite of naiba- (Hz. ApI 1434): duš- + karta- ‘done, made’, past pte. pass. tokar-. duskartam nsn. DSe 31f; XPh 42. draug- vb., see duruj- and draujiya-.
5583:naiba- adj. ‘beautiful, (religiously) good’, re- .
5584:placing GAv. vahu- ‘good’, and opposite of duš- karta- (Hz. AMI 8.68, ApI 266-7): NPers. nē ‘brave, good’ ($11, §75.V, $148.11). пафа nsf. DPd 8. naibam nsn. XPa 13, 16; XPg 4; XV 20. naibam asn. DSe 32°; DSi 4^; DSp 2f°; XPh 43.
=== BRT naiba
4210:'über  (einen  Raum)  hin' :  Xvasiy  aniyasHy naibam  (sd.)  kartam  'il  pursä  tyJ'  adam akunavam  Uta ..  ". .  in  Persien  .."  X.1.3.
4652:26; — yeti^a  hl  °«va(NPn.)  aya  fyaoUna /raz'arsia  Y.J.21;  21;  —  MAj  ..  vas»ml\ (sd)    'nyacä  (APn.)   viduyS  Y.44.3;    — | paitica  (sd.)    hl  °nya  (NDm.)    dva atshtn  patüa  v3  V.5.27;  —  ha  mg  baya , .  sai»m  paiti  'nyaHqm  räi:Wqfn  . .  dasa paiti  °nye  ratavaY.ig.$;  —  ka  aPva  alö.- stüitis  ya  dasa  'nyaisqm  (als  GPf.)  asö.- stäitinqm  artjaiii  lLi,6; — alt a  ..*' inim  ^°> a^rapaitim    upBisdil   a%a    %ritTm  .  .    N. II.         a)  Siog.  und  Plur.  mit  folg.  eiy,  eii'> 'auch  ein  anderer':  *uta»iaiy  'niya/äy  (SSu.) vasiy  astiy  kartam  Bk^S;  —  \vasiy yasiiy  naibam (sd.)  hartem  X.i. 3;  —  h^nii 'fiyäscit  asasca  /m^ras/a  srTrh^a gibt  auch  noch  andre  schöne  .  .  Stätten und  Wohoplätze"  V. /,  28.         b)  mit  folg. ia-    und    /ii    'irgend    ein    anderer' iasat   aafiSus    asti-ats   N.  6^.  c)    mit
8188:•  j.  Uta,  g.'',  p.  Uta  (,  uta'Y^  Part  'und', an  der  Spitze  des  Satz(teil)es  stehend,  doch s.  II  2  A  und  No.  6;  I)  zur  Verbindung syntaktisch  gleichstehender  Satzteile  bei gleichem Verbum:  Ipar^ara*  'tiJ  varhln^ hatni'^'iyä  abava'  Bh.2.16;  6,  Am./,  4i A0.J.4;  —  ^urJ'masdi!  upastäm  abar^ '13  aniyil  bag!lh<^  tyaiy  ha'iiy  Bh,  4- 1 2, 13,  D.  5. 2 ;  —  vasiy  anivasi'iy  naibam (sd.)    kartam    .  .    tya*    adam    akunavam
9142:—  Uta  ty<^  manu  kartam  utä  tya"  maiy pi^'ii*  kartam  X.  /.  4;  y.  3;  —  fy.i'' manu  kartam  id-i  utä  tya^maiy  kartam apataram  ava''  Hsam  7'ahiä  a''ura''mas- d,thJ'  akimavam  X.2.3;  3,^.3;  —  avaisäm iiaiy  astiy  kartam  ya>ä  manä  .,  kartam Bh. .,'.  9;  —  Uta  tye^  "mäm  kart,l'"" Ao,  /.  4;  —  Aai(7' .  .  vasiv  tya^  naibam akimau;'"  X.  7.  3;  —  'tyJ'  kunavaky ava''taiy  a"urtrmazd,i  mkwtm'  (sd.)  Rh. 4.  17;  16;  —  a''uri^mazd<lmaiy  upastäm abitra    yätä  kartam  akunavam  D.  6.  5;
9143:—  imam  duTariim  ,  .  adam  akunai-am, \vasiy  aniytiiay   naibam  kartam..  tya''
11355:nicht  minder;  dazu  noch,  ferner  noch'; a)  II  im  Ap. :  maia  <^urt^masda  patuv  .  . Uta  tyt^  man3  kartam  utä  ty^maiy  pt- ä'«*  kartam  avasciy  .  .  patuv  "mich  soll ^ÄjV.schQuenundwas  von  mir  geschaffen worden  ist;  und  was  von  meinem  Vater geschaffen  worden  ist,  das  soll  (AiM.) auch  (gleichfalls)  schützen"  X,  /.  4;  j.  3; — ■  imam  duvari^im  . .  adam  akunavam vasiy  aniyalHy'^  naibam  (sd.)  kartam  X. l.  3;  —  hinter  utä^h'  *utamaiy  aniyasciy (Sp.  137  m.)  vasiy  astiy  kartam  Bh.  4- 8.  b)  im  Aw.:    m^r>m  ..ytm  . .  vfs-
12376:*  p.  tya-  Pron.  rel.  (fem.  'yä-")  'welcher, wer,  der';  I)  als  eigentliches  Relativum; 1)  mit  einem  demonstrativen  Korrelat,  das i)  folgt,  uzw,  a)  aita-  (Sp.  13  u.):'  datam 'yJ'  mana  aitJ'  ^adariy  D.6'.3".  b)  ^ava- (Sp,  166  o.):  ya^säm  Aa/ama*  ahahyJ' . .  avi^  *akunavayi^t3  Eh.  7.  7 ;  D.  6.  3,  4; —  •_)'«*  kunavahy  avt^iaiy  .  .  Bh.  ^.  16, 17;  —  Uta  'yJ'maiy  p^'^e^  kartam  ava^- ay  . .  X. z.  i;  3.  $;  —  '>'«*  maiia  iariam idä  Uta  'yJ'maiy  apaiaram  iartam  av(^ visam  X.  2.  3;  —  'y^patiy  (sd.)  kartam vainataiy  naibam  (sd.)  ovo'  visam  .  .  X. 7.  3 ;  —  'yaiy  paruvä  xiaya%iya  yata  aAä" avaijilm  .  .  'Bh.4-  9;  —  xsa'S!''am  'yo'' . . parabartam  aAa*  ava*  .  ,  Eh.  7.  14;  — martiya  'yatsäty  Jraiamä  anusiya  akd'ia flufl/)'.- Bh, 2. 13.  a)  vorausgeht,  uzw. a)  ima-  (Sp.  371  ni.):  («a*  /v«*  adam akunavam ..  vasna  (^ur^mazdaki^  akuna- vam  Bh.-^i2;6,  2,  Am.4(?);  —  dahyavt/' ima  "yä  Aami^'iyä  abavd^  draugf^dU hamtk^iya  akunauf?,\i..4.a,; — imam  dipim ..'yam  adam  myapisam^.4-'^  <,.  b)  ^ava- (Sp.  165  m.,  167  m.)t  ^ava  dahyavJ"  'yä darayJ'vJ'us . .  adaraya*  'D.6.4;  —  ovaAya kärahya . .  yam  vahyazdatt^  fraisayt^  ßh. _^. II.  c)  sonstige:  iyam  dakyaus . .'yam manä  J'urJ'mazda  frabari^Yi.4.3\ — hauti karJ'  asiyavt^  'yam  vaAyazdatt^ /rai/ayJ' Bh.  J.9,  3)  eines  geht  voraus  und  eines folgt:  aiti/'  x^a%'am  'ya^  gaumatJ*  .  . adfna*  kt^hnfyam  atta^  x^dÜ'am  . .  Bh. 7,  la;  —  aita'  'ye^  kartam  avi/'  visam  .. D.  6. 5.  2)  ohne  demonstratives  Korre- lat; i)  das  Relativum  bezieht  sich  auf  ein
12380:vorausgehendes  Substaadvum:  uts  aniya bagäha'  'yaiy  Ai^Hy  Bb..^.  12,  13;  — S  mana  taumayä  'yaiy  paruvam  xsäya- ^iyä  ähi^  Bh./.  4;  —  martiyä  'yaisaiy fratama  anusiya  äAa'tä  Bh.  j.  7,  8,  11; ^.18;  —  imä  dahyäv<^  'yä  adam  *aäarsiy ..  °ya  ka'ämt^  atars^  D. 5.  3;  6'. 3,  Bh. j.  6,  7,  2.  a;  — -  ayaäanä  'ya  (APa)  gau- mättr  , .  vyai^  aäam  niyah^ärayaM  Bh. 1. 14;  —  adi^ari/ ..*vi^aiMscä  °yädis  gau- mStJ*  adfn/^  Bh.  /.  14;  —  *drayi^  'yJ' hacä  pärst^  aitiy  D.  z/.  3;  3;  —  vasiy aniyasciy  naibam  kariam  .  .  'ya^  adam akunavam  utamaiy  'yJ'  pttä  akunaui  X. I.  3.  2)    das    Relativum    hat    keine
12385:knüpfung einer  nominalen  Ergänzung  an dn  vorausgehendes  Substantiv;  l)*J  im Nominativ  (oder  dem  ihm  gleichen  Akku- sativ): yaunä  (sd.)  'yaiy  ''uikakyä  uta 'yaiy  *drayahyä  D.  5.  2 ;  —  sakä  (sd.) 'yaiy  ^tara'drayt^  D.  6.  3;  —  dahyäv<r 'yä  *paruvaiy  ü.ß.z;  —  xsa%''am  'ya* babirauv  Bh.  i.  16;  —  x/a'^'am  .  .  ya^ *vaiariam  'y<^  ''uvaspam  D.  77. vasiy    'ya^    naibam    X.  7.  3.  l)    in
14905:•  p.  "patiy  enkl  Part  der  Verallge- meinening,  nur  hinter  Relativen;  i)  tya'p- kariam  vainalaiy  naibam{s.ä.)  av^  visa/n.. "quodcumque  factum.."  X.J.3.  2)*yaäip''^'' ^maniyühay  tyt^  ''Sye^karam  (sd.) . .  "wenn etwa  , ."  I).  6. 4.
18484:•  p.  nalba-  Adj.  (fem.  °bä-)  'schön,  gut, tüchtig' :  dahyäu^  . .  hyä  °bä  D,  4.  a ;  — vasiy  amyaiay  'dam  kartam  . .  tycr  adam akunavam  .  ,  iyJ^paiiy  kartam  vainataiy •tarn  ava^  visam  vasnä  a*ura*mazääi^ akum3  "auch  noch  viel  andres  Schöne  ist geschaffen  . .,  das  ich  geschaffen  habe  . .; welch  Werk  schön  anzusehen  ist,  all  das haben  wir  nach  dem  Willen  des  AhM. geschaffen"  X.  /.  3;  —  Aaiw . .  vasiy  tyJ' naibam  akunau^  "der  hat  viel  Schönes geschaffen"  X.  7, 3.
22105:(sd.)  vainantS  (AP.)  braianta  . .  »mabm zaranim  Yt.5. 129.  a)  mit  ergänzendem Partizip '':_yff/i'tfOT  ainim  avaSiai/(2SPiA.; Augm.)  saocayaca  kirmavanttm  "wenn  du leben  andern  .  .  treiben  sahst"  H. 2. 13; —  \ya'h3  avaina'  imäm  bümim  *yauda'tim (sd.)  D.ö'.4.  2)  AkL  'es  einer  Sache (Akk.)  ansehen  (können)':  vansim  . .  vae- naiti  kalarS  ayravU  (sd.)  vi!  *bunavs  vä Yt.  14-  31,  iG.  10.  3)  Akt  'ansehen für  — '  (Akk.):  ySi  %wS  vam»n  .  .  aham rff/Bwc'fl"diedidi  für  denj4.und^.  ansehen" YL  10.  92;  — yim  dim  vaEnät  *rvistaäva (sd.)  *vindatum  N.  16.  4)  Med.  'videri, gesehen  werden,  scheinen':  a6da(sd,ya i  (sd.)  ioa  . .  sadayät  yat  iha  pasSuS .  .paa?m vaSnäite  V.  2.  24;  —  haksrit  ir  irixtahe I  (sd.)  .  .  valnaite  (statt  Plur.)  itarasca  . . V,  2. 40;  —  \tya'paüy  iariam  vainataiy naibam  (sd,)  X.i.  ^;—~  tanOm  yä  mi  val- naite Auraeoa  ".  .  quae  mihi  vtdetur  for- mosa"  Y.io.14.
28714:—  insbesondere  zur  Wiederaufnahme  des Subjekts,  das  sammt  Zubeliör  unmittel- bar vorausgeht^:  /  marliyt^  i^i^Vtaxma" näma"  asagartiyc^  hauvmaiy  hamii^iya'' abav^  Bh.  2.  14;  —  /  martiya''  araxa'' nama!'  arminiya''  haldüahya  pu^'a*  hauv udapatatä  Bh.,;.  13;  —  vistäspf^  tnatiä pita  hauv  paT^avaiy  ah<^  Bh,  2.  lö;  — dSrayJ'vt^us  xiäya%iya''  hyc^  manä  pitil hauv  .  .  vasiy  ty<^  naibam  akunaus  X. 7.  3;  D.  4-  ';  —  margui  näma"  dahyäus hauv(fem.)maiy  haHtiyä  abava^  Bh.j.3; 5, 1 ;  —  hya^  du7'aistam  nyäii/  axiatä  (sd.) Äau[fem.}ay  J'urä  nirasätiy  D.5.3J  — hauv  vahyazdätJ'  hyi^  bardiyJ'  agaubatä hauv  käram  fräisayi^  Bh.^.  9;  11;  — käri^  pänJ^  utä  mäda''  Afn*  upä  niilm äh<^  hauv  kamnam  äha^  Bh.  2.  6;l(  — ar^aia  vJptS  arsala  vaipayB  .  .  hau  asti daSi-B  hau*"  .  .  V,  <?.  33.  b)  auf  ein Relativum  als  dessen  Korrelat:  \hy(^ madaisuvä  mäkilt<^  äha*  hauv  *adakly naiy  adäraya''  Bh.  2.6;  —  hyä  J'ura''- mazdähc^  Jramiinä  hauv(ieai.)taiy  gas/ä mä  ^adaya^  D.  6. 6.  II  »)  auf  den  Inhalt eines  Satzes;  in  Kongruenz  mit  dem  (ge dachten)  Praedikat:  kä  hl  asti  n^a?  .  . panca  sota  upäxananam  upäisit  hau  (fem.) Jaiäus  hau  vTsäus  häu^ . .  hau  vispanqm . .  spaci^ranqm  anya  udra  upapa  ". .  das  (ist auch   die  Strafe  für  die  Verletzung)  des
```


## [2026-09-07T18:19:41.635Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | head -80 && echo \"=== POK sizes\" && wc -c POK_01.txt POK_02.txt POK_03.txt POK_full.txt",
 "description": "List refs dir"
}
```


### [2026-09-07T18:19:41.675Z] TOOL RESULT

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
=== POK sizes
 981836 POK_01.txt
1137861 POK_02.txt
1170809 POK_03.txt
3971883 POK_full.txt
7262389 total
```


## [2026-09-07T18:19:43.184Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"nei-t\\|neit-\\|nītere\\|niteo\\|nitēre\\|nitere\" POK_full.txt | head -30",
 "description": "Grep Pokorny for nei-t"
}
```


### [2026-09-07T18:19:43.250Z] TOOL RESULT

```
26783:blame, esp. by word ', neit-^ to be hostile towards, attack ' neiq-{see there), in ne/-, n/-. 
62247:netar-, netar-m. 6s., netra-n. " direction, eye'; Middle Irish ne, /7/a "warrior, hero ' {*neit-s). 
62249:Gen. Sg. Proto Irish netas. Old Irish math {*nei-t-os, s. also nei-2)\ Hittite /75/- "steer, guide, 
78933:Root / lemma: sneit-
```


## [2026-09-07T18:19:47.996Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Root / lemma: nei\" POK_full.txt | head -20 && echo === && grep -n \"Page(s): 760\\|Page(s): 759\\|Page(s): 761\" POK_full.txt | head",
 "description": "Find nei root lemma in Pokorny"
}
```


### [2026-09-07T18:19:48.055Z] TOOL RESULT

```
Exit code 1
62133:Root / lemma: neid-1{*he- neid-f) 
62154:Root / lemma: neid-2: nid- {*he- neid-2) 
62176:Root / lemma: neig"- {^hoing"^ 
62207:Root / lemma: neik- {*hoink-) 
62239:Root / lemma: nei-1, neie-. nT-{*hoin^ 
62257:Root / lemma: nei-2, neie- : m- {*hoin-) 
62988:Root / lemma: neik- : nlk- : nik- {*he- neik-) 
(eval):1: == not found
```


## [2026-09-07T18:19:51.147Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '62230,62290p' POK_full.txt",
 "description": "Print Pokorny nei-1 and nei-2 entries"
}
```


### [2026-09-07T18:19:51.199Z] TOOL RESULT

```
through dissimilation. 

Note: (common Baltic Hittite n- > /-) 

References: WP. II 321, Trautmann 195 f.; J. Loth RC. 40, 352 f.; 41, 193 ff. 

Page(s): 761 

Root / lemma: nei-1, neie-. nT-{*hoin^ 

Meaning: to lead 

Material: Old Indie /7ay5// (participle mta-), Avestan /75ye/// "leads'. Middle Persian mtan 

"guide, lead, drive, push'. Old Indie mthai. " direction, way', mtho, /7e/a "guide, leader', 

netar-, netar-m. 6s., netra-n. " direction, eye'; Middle Irish ne, /7/a "warrior, hero ' {*neit-s). 

Gen. Sg. Proto Irish netas. Old Irish math {*nei-t-os, s. also nei-2)\ Hittite /75/- "steer, guide, 

lead'. 

References: WP. II 321, Pedersen Hittite p. 77 f., 81, Frisk Suffixales -th- 5 f. 

Page(s): 760 

Root / lemma: nei-2, neie- : m- {*hoin-) 
Meaning: to move vividly, be excited; to shine 

Material: Latin nited, -ere^ shine| glitter| look bright; be sleek/in good condition; bloom| 
thrive ', nitidus^ shining! bright ', nitor^ press/lean upon; struggle; ADVance; depend on 
(with abl.); strive] labor, radiance ' (from a participle *ni-t6-); perhaps re-mdeo^ shine 
(back)l gleam; smile back (at) ' (with present formation -d(h)-)\ *nei-b^o-\x\ Middle Irish 
mab^ vitality ', cymr. nwyf6s.\ noi-b^o-\v\ Old pers. naiba-, npers. /7eM/ "beautiful, good', 
Old Irish /7c»Z&"holy'; *ne/-ma\n Middle Irish n/am 'radiance, beauty'; *ne/-ko-\n Middle 
Irish nlacbm. " hero ', n/achusm. " braveness'; *ne/-to-\n cymr. /7tvyo'"ferventness, passion', 
hispan. war god Neto; Old Irish PN Ma// {Gen. Ne///) from *ne/t-s-/o-s, placed perhaps also 
in Old Irish /7/a" hero ' (see ne/-1)\ Germanic *n/Pa-\n Gothic ne/f^n. " envy ', Old English 
nTdm. "fight, struggle, hate, enmity'. Old Saxon Old Frisian /7/?/7" eagerness, hate, envy ', 
Old Icelandic nfd' derision, ridicule, disgrace, shame'; could also belong to Old Irish mtbn. 
(Indo Germanic *n/lu-) "fight, struggle'; dubious Old Indie /7/7a- "bluish black', nayana-n. f. 
"eye', netra-n. ds. 

References: WP. II 321, 336, WH. II 168, 171, Vendryes RC. 46, 265 ff. 
Page(s): 760 

Root / lemma: ne/-3, ni- {*houn-) 



See also: see above S. 312 f. {en-). 
Page(s): 760 



Root / lemma: neR- {*hounR-) 

Meaning: death, dying; dead person 

Material: Old Indie nasyati, nasati^ gets lost, disappears, passes away ', nasayat/" makes
```


## [2026-09-07T18:20:07.489Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD nei/noibho\"; grep -n -i \"noibho\\|nei-\\b\\|nitere\\|niteo\" AHD_watkins1985.txt | head -20; echo \"=== AHD neat\"; grep -n -i \"^neat\\|neat,\" AHD_watkins1985.txt | head",
 "description": "Grep Watkins AHD"
}
```


### [2026-09-07T18:20:07.556Z] TOOL RESULT

```
=== AHD nei/noibho
642:h. Anglo-Norman aloper, to run away from one’s hus- band with a lover: ELOPE. kneigwh-. To lean on. 1. Latin cdnivére (< *con-niguére; com-, together; see kom), “to lean together” (said of eyelids), to close the eyes, be indulgent: CONNIVE. 2. Suf- fixed zero-grade form *knigvh-to- in Latin nictdre, to move the eyelids, wink: NICTITATE. 3. Uncertain preform in Latin niti, to lean forward, strive: NISUS; RENITENT. [Pok. knei-geh- 608.] knid-. Egg of a louse. Suffixed form *knid-d in Germanic *hnito in Old English hnitu, egg of a louse: NIT. [Pok. knid- 608.] ko-. Stem of demonstrative pronoun meaning “this.” I. Variant form *ki-. 1. Germanic *hi- in: a. Old English he, he: HE!; b. Old English him, him: HIM; c. Old English his, his: 1s; d. Old English hire, her: HER; e. Old English Ait, it: 1r. f. Old English hér, here: HERE; g. Old English heonane, heonon, from here: HENCE. 2. Suffixed form “ki-tro- in Germanic *hi-thra- in Old English hider, hither: HITHER. 3. Suffixed form *ki-s in Latin cis, on this side of: cis-. II. Variant form *ke-. 1. Preposed in *ke-etero- (*e-tero-, a second time, again; see i-) in Latin céterus (neuter plural cétera), the other part, that which remains: ET CETERA. 2. Latin -ce (see nu-). III. Attrib- uted by some to this root (but more likely of obscure origin) is Germanic root *hind-, behind. 1. Old English bihindan, in the rear, behind (bi, at; see ambhi): BE- HIND, HIND!. 2. Old High German hintar (> German hinter-), behind: HINTERLAND. 3. Germanic derivative verb *hindron, to keep back, in Old English hindrian, to check, hinder: HINDER}. [Pok. ko- 609.] k6-. To sharpen, whet. Contracted from *koo-. 1. Suffixed extended form “kooi-no- in Germanic *haind in Old English hdn, stone: HONE!. 2. Perhaps Greek kénos, cone, conical object (< “a sharp-pointed object”): CONE. [Pok. Aéi- 541.] kob-. To suit, fit, succeed. Germanic *hap- in Old Norse happ, chance, good luck: HAP, (HAPPEN), (HAPPY); (HAP- LEss), (MISHAP). [Pok. kob- 610.] [kokkos. Kermes berry, pit, grain. Greek noun of un- known origin: COCCID, COCCUS, COCHINEAL; MONO- COQUE.] koksa. Body part. Latin coxa, hip: Coxa, CUISSE, CUSH- ION. [Pok. koksd 611.] kolem-. Grass, reed. Suffixed form *kolsm-o-. 1. Ger- manic “*halmaz in Old English healm, halm, straw: HAULM. 2. Latin cudmus, stalk: CULM!. 3. Zero-grade form “kibpm-o- in Greek kalamos, a reed, straw: CALA- MITE, CALAMUS, CALUMET, CARAMEL, SHAWM. [Pok. kolomo-s 612.] koli-. Glue. Suffixed variant form *koly-a in Greek kolla, glue: COLLAGE, COLLO-, COLLODION; PROTOCOL. [Pok. Rolfeji- 612.] kom. Beside, near, by, with. 1. Germanic *ga-, together, with (collective and intensive prefix and marker of the past participle), in Old English ge-, with, also participial, collective, and intensive prefix: ENOUGH, HANDIWORK, YCLEPT. 2. Latin cum, co-, with: CUM; CONQUIAN. 3. Old Latin com, with (collective and intensive prefix): co-, com-. 4, Suffixed form *kom-trd in Latin contra, against, opposite: (CON!), CONTRA-, CONTRARY, (COUNTER!), COUNTER-, COUNTRY; ENCOUNTER. 5. Suffixed form *kom-yo- in Greek koinos, common, shared: COENO-; CENOBITE, EPICENE, KOINE. 6. Reduced form *ko- (see gher-', mei-', smei-). [Pok. kom 612.] konemo-. Shinbone, bone, Reduced form *kemmo- per- haps in Germanic *hamma in Old English hamm, ham, thigh: HAM. [Pok. konamo- 613.] konk-. To hang. 1. Germanic *hanhan in: a. Old English hon, to hang: HANG; b. Dutch (dialectal) hankeren, to long for; HANKER; ¢C. possibly Middle English he(e)ng, hinge, hinge (ultimately from the base of Old English hangian, to hang): HINGE. 2. Suffixed form *konk-t-d- in
776:sively, very (< *ne-mi-s, “not little”; *mi-, little; see mei-2): NIMIETY. 4. Latin nihilum, nothing (< *nehilum, “not a whit, nothing at all”; hilum, a thing, trifle; origin unknown), contracted to nihil, nil, nothing: NIHILISM, (NIHILITY), NIL; ANNIHILATE. 5. Latin non, not (< *ne-oinom, “not one thing”; *oino-, one; see oi-no-): Non-. 6. Italic *nek, not, in: a. Latin prefix neg-, not: NEGLECT, (NEGLIGEE), NEGOTIATE; b. Latin negdre, to deny: NEGATE; ABNEGATE, DENY, RENEGADE, (RENEGE). 7. Greek né-, not: NEPENTHE. 8. Zero-grade combining form *n- in: a. Germanic *un- in Old English wn-, not: uN-!; b,. Latin in-, not: IN-1; c. Greek a-, an-, not: A-}, (AN-); d. Sanskrit a-, an-, not: AHIMSA, AMRITA. [Pok. ne 756.] nebh-. Cloud. 1. Suffixed form *nebh-lo- in Germanic *nibla- probably in Old Norse nifl-, “mist” or “dark”: NIFLHEIM. 2. Suffixed form *nebh-eld- in: a. Latin nebula, cloud: NEBULA, NEBULOUS; b. Greek nephelé, cloud: NEPHELINE; NEPHELOMETER. 3. Suffixed form *nebh-es- in Greek nephos, cloud: NEPHOLOGY. 4. Nasal- ized form *ne-m-bh- in Latin nimbus, rain, cloud, aura: NIMBUS. See ombhro-. [Pok. (enebh-) 315.] ned-. To bind, tie. 1. O-grade form *nod- in: a. Germanic *nati- in Old English ne¢(t), a net: NET!; b. Germanic *nat-ilo, a nettle (nettles or plants of closely related genera such as hemp were used as a source of fiber), in Old English netel(e), netle, nettle: NETTLE; c. Germanic *nat-sk- in Anglo-Norman nouch, brooch: OUCH?. 2. Lengthened o-grade form *nédo- in Latin nédus, a knot: NODE, NODULE, NODUS; DENOUEMENT. 3. Re-for- mation of the root in Latin nectere (past participle nexus), to tie, bind, connect: NEXUS; (ADNEXA), ANNEX, CONNECT [Pok. 1. ned- 758.] negwh-ro-. Kidney. Greek nephros, kidney: NEPHRO-; MESONEPHROS, METANEPHROS, PERINEPHRIUM, PRO- NEPHROS. [In Pok. eng¥- 319.] negw-ro-. Adjective denoting various colors; with deriva- tives like Greek nebros, “fawn.” Latin niger, black: NEGRO, NIELLO, NIGRESCENCE, NIGRITUDE; DENIGRATE, NECROMANCY, NIGROSINE, [néhw-iz. Near. Germanic root. Old English néah, near: NEAR, NEIGHBOR, NEXT, NIGH.] nei-. To be excited, shine. 1. Suffixed form “nei-to- in Germanic *nitha-, animosity, in Old Norse nidh, scorn (> nidhingr, villain): NIDDERING. 2. Suffixed zero-grade form *ni-to- in Latin nitére, to shine: NEAT!, (NET?). 3. Possibly Persian nil, indigo: ANIL, LILAC. [Pok. 2. nei- 760.) neie-. To lead. Sanskrit nayati, he leads: NAINSOOK. [Pok. 1. nei- 760.] neig’-. To wash. Germanic *nikwiz, *nikuz in Old High German nihhus, river monster, water spirit: NIx!. [Pok. neigt- 761.] nek-', Death. 1. Latin nex (stem nec-), death: PERNI- cious. 2. Latin necdre, to kill: INTERNECINE. 3. Suffixed (causative) o-grade form *nok-eyo- in Latin nocére, to injure, harm: NOCENT, NOCUOUS, NUISANCE; INNOCENT, INNOCUOUS. 4. Suffixed o-grade form *nok-s- in Latin noxa, injury, hurt, damage: NOXIOUS; OBNOXIOUS. 5. Suffixed full-grade form *nek-ro- in Greek nekros, corpse: NECRO-, NECROSIS; NECROMANCY. 6. Greek nek- tar, the drink of the gods, “overcoming death” (*tar-, overcoming; see ter@-2): NECTAR, (NECTARINE). [Pok. nek- 762.] nek-?. To reach, attain. I. O-grade form *nok- in Ger- manic *ga-nah- (*ga-, intensive prefix; see kom), “satis- fies,” forming *gandga-, sufficient, in Old English gendg, enough: ENOUGH. II. Variant form “enk-. 1. Redupli- cated in Greek enenkein, to carry, whence onkos, a burden, mass, hence a tumor: ONCOGENESIS, ONCOLOGY. 2. Compound root *bhrenk- (see bher-'). [Pok. enek- 316.] nekw-t-. Night. O-grade form *nokv-t-. 1. Germanic *naht- in Old English niht, neaht, night: NIGHT. 2. Latin
=== AHD neat
1905:NEAT! nei-
1906:NEAT2 neud-
```


## [2026-09-07T18:20:08.956Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD\"; grep -n -i \"\\bnew\\b\\|newag\\|nēw\" PHD.txt | head -20; echo \"=== PHD_mackenzie\"; grep -n -i \"nēw\\|new \" PHD_mackenzie.txt | head -20",
 "description": "Grep MacKenzie for new/newag"
}
```


### [2026-09-07T18:20:09.028Z] TOOL RESULT

```
=== PHD
5:NEW YORK TORONTO
6:Oxford University Press, Walton Street, Oxford OX2 6DP Oxford New York Toronto Delhi Bombay Calcutta Madras Karachi Petaling Jaya Singapore Hong Kong Tokyo Nairobi Dar es Salaam Cape Town Melbourne Auckland
26:By its nature the dictionary cannot claim to contain the entire vocabulary of any particular text. Nor is there any express inten- tion of presenting new solutions to the many problems remaining in the Pahlavi texts. Rather the readings of many scholars have
60:Since the discovery of the Iranian material written in the near- phonetic Manichaean script it has become possible to establish a hypothetical phonemic system for Middle Persian and Parthian of the third century A.D. far more accurate than before, when only the remoter evidence of Old Iranian, New Persian, and loanwords in other languages (particularly Armenian) was available. A description of this phonemic system has been given in my article cited above. Within its terms all the entries in this dictionary are transcribed.
92:Later forms of the word are quoted from Judaeo-Persian (J—from whatever source) and the earliest New Persian (N— rarely in their Arabic guise, when this has displaced the Persian, Ar.).
103:In Manichaean Middle Persian the corresponding forms are spelt dydn, wyn- respectively, indicating the same pronunciation. In New Persian the infinitive is still didan, but the present stem has become, regularly, bin-.
113:M Manichaean Middle Persian N (early) New Persian P Parthian
207:~ widardan: outstrip. andarag [adig] in, between, among. andarmāh [?ndim’h] new moon. andarón [?ndlwn! | M ?ndrwn, N —rün] inside, within, andarway [ndlw?d | (P ?ndrw'z)] air, atmosphere.
516:—jh: weakness. nizārīh- [nz?lyh-] become weak. nē [ТА < A t£? | М пол, N nuh] nine. nóg [nek! | М mwg, N naw] new, recent. ~erz [-hvc | N nawróz] New Year's day. ---zád(ag) [-z't(k)! | N nawzàád] new-born. nohom [nhwm | = M, N ~] ninth. nózdah [nwzdh | № ~] nineteen. nin [KON < A k‘n | M, J поп] now.
912:backgammon nēwardaxšīr.
1072:brave čēr, dilēr, marčābuk, mardān- ag, nēw.
2126:good (a.) huda(ha)g, nēk(ēg), new, weh, xūb, hu-, P naxšag; ~ char- acter huxémih; — deed huwatršt, kirbag; — repute husrawih; — rule hupādixšāyīh; ~ ruler hupádix- šā(y); ~ speech hüxt; ~ spirit spenag mēnēg; ~ thought humat; of ~ behaviour hukunišn; of ~ character huxém; of — religion hudén; of — repute husraw; of — speech hu-éwaz, hu-gówisn; of ~ stock pad-góhr(ag); of ~ thought humenišn.
2843:moon āyišm, mah; full ~ purrmah; new ~ andarmāh,
2911:new nog.
2912:new-born nūgzād(ag).
2913:New Year's day пӧвгӧг.
4714:= 39110 Wes) nuo VAS 4599 110) VA nes 15v" 0) New g GNU O 3° ос uo
5232:wasnid nixwiür- nixwārišn nahang, nihang wiyūz- wayūdagān wēn- (v. dīdan) жатап! wēnāgīh wēnāg winnār- winnārišn nēwardaxšīr winnārdan wēnāb wēnābdīg wēnābdāg niyūxš- niyoxsidan niyoxsián wénig
5233:new, wen
=== PHD_mackenzie
14:     NEW YORK         TORONTO
16:                       Oxford New York Toronto
122:tion of presenting new solutions to the many problems remaining
303:the remoter evidence of Old Iranian, New Persian, and loanwords
413:(J-from whatever source) and the earliest New Persian (N-
460:In New Persian the infinitive is still didan, but the present stem
476:N         (early) New Persian
1089:andarmah ['ndlm'h] new moon.
3715:new [T!1 < A tb; nyw l I = M, N -] good, brave.
3823: --roz [-lwe I N nawroz] New Year's day.
7126:  new -- andarmah.                             naphtha naft.
7153:new HOg.                               obstinate starnbag, wastar.
7155:New Year's day nogroz.                 obvious iiskadg, casmagah, casmdid,
7594:sinew pay.                                    smite zadan; v. hit, beat.
```


## [2026-09-07T18:20:21.123Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD_mackenzie nard/newardaxsir/newag/nek\"; grep -n \"nard\\|newardax\\|newag\\|nekih\\|^nek\\| nek \" PHD_mackenzie.txt | head -20; echo; sed -n '3710,3725p' PHD_mackenzie.txt; echo \"=== NYB\"; grep -n \"nēw\\|nyw\\|nēwak\\|newak\" NYB_vol2_glossary.txt | head -20",
 "description": "Grep MacKenzie and Nyberg"
}
```


### [2026-09-07T18:20:21.212Z] TOOL RESULT

```
=== PHD_mackenzie nard/newardaxsir/newag/nek
3698:nek [nywk I M nyk, N --] good, beautiful.
3701:nek-gohr [nywl~ gwhl] good-natured, virtuous.
3703:nekog [nywkwk ' I M nyyqww!, N neluJ] = nck.
3716: --ardax~ir [nyw'lthfyll N nard !] backgammon.
5988:assist ayaridan, frayadidan.             backgammon newardaxsir.
6682:generatio1l awadag.                           goodness huih, nekih, nekgohrih,
10206:nekgohr                     \.... 1" St"\    ,,'is
10233:                             "to~,           ,....innardan

nerog [nylwk ' I M nyrwg, N nero] strength, power.
 ......,omand [-)wmnd] strong, powerful.
nest                             59                          nihanll
nest [LOYTI < A e 'yty I M nyst, N -] is not.
 -ih: non-existence.
new [T!1 < A tb; nyw l I = M, N -] good, brave.
 --ardax~ir [nyw'lthfyll N nard !] backgammon.
nezag [nyck I N neza] lance.
                '
neziiman, -ig [nycwm'n l , -yk l I M nyzwm'n] dextrous, skilful.
 --ih: skill, artistry.
nibard [nplt l I N nabard] fight, struggle, battle.
 --ag [-k l I N --a] tried, experienced.
nibardidan, nibard- [nplt-ytn' I P nbrd'd] fight, do battle.
nibastan, nibay- [SKBHWN-tn I < A v Ikb; npstn l , npd- I M nbst] lie
     down, sleep.
=== NYB
2595:murvik [mwlw'k] an augury, an omen 181. - MPrth mwrgw’g (S); MPrs mwrw’; nyw-murwh ‘of good augury’ (A-H II); Paz. murväi; NP murvà.
2682:névák [ndwk'] good in a general sense; beautiful, nice; favorable, comp. ~-tar 604; adv. well 220, 713. 7619; as an attr. commonly placed after its headw., but m jäyisn 1214 as against jāytšn + ~ 181, yatak i ~ 1133; — placed before its head w., with the ending -é or -en : —-ē āvām the favorable time 55%; ~-én kunišn good deeds 7227, v.s. v. ménói. — Ps. nywk- ; Paz. nek, nyak; NP nék.
2774:niyandar [nyw’ndl; ny-BYN] inside, within 4216, 934, — Ps. nywndly, v. Barr s. V.; as to the spelling -yw- for -yy- before a vowel v.s. v. apyuxt (add Ps. dlyu”w = driyāv = drayāp, v. Barr s. v.).
2779:niyöSitan [ndwkšytn'] to listen 90%. — Ps. pres. nydwhšyt = niyöxset; MPrth pres. ngwš-, MPrs nywš-; Paz. nyoxšidan, NP myēšīdan; < mi + Av. (485 sg.) gaoš-.
```


## [2026-09-07T18:20:36.478Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN1966 neat\"; grep -n \"neat, adj\\|neat,\" KLN_1966.txt | head -10; echo \"=== KLN1966 alembic\"; grep -n \"alembic\" KLN_1966.txt KLN_1971.txt | head -10; echo \"=== KLN net\"; grep -n \"net, adj\" KLN_1966.txt KLN_1971.txt | head",
 "description": "Grep Klein for neat, net, alembic"
}
```


### [2026-09-07T18:20:36.577Z] TOOL RESULT

```
=== KLN1966 neat
7869:-cle,  dimin.  subst.  suff".  « —  Fr.  L.  -cuius  (masc.), -cula  (fem.),  or  -culum  (neut.),  either  directly or  through  the  medium  of  F.  -de.  See  -cule. clean,  adj.  —  ME.  cleric,  fr.  OE.  cline,  ‘clear, clean,  pure’,  rel.  to  OS.  kleni,  ‘dainty,  graceful’, OHG.  kle  ini,  ‘shining,  neat,  elegant"  (whence MHG.  kleine,  ‘nice,  graceful,  small’,  G.  Mein, ‘small’;  in  G.  Kleinod,  ‘jewel,  gem’,  prop, ‘something  neat  or  fine’,  the  orig.  meaning  of klein  survives),  and  prob.  cogn.  with  Gk.  yXxivov (Hesychius),  ‘star-shaped  ornaments’,  -(zhxv, ‘to  laugh’.  See  geloto-  and  cp.  the  first  clement in  kleeneboc.  Derivatives :  dean,  adv.  (c\.v.), clean¬ er,  n.,  clean-ing,  n.,  clean-ly,  adv. clean,  adv.  —  OE.  dine,  "entirely’,  fr.  dine ‘clear,  clean,  pure’.  See  clean,  adj. cleanly,  adj.  —  ME.  clenly,  fr.  OE.  clinlic,  fr. cline.  See  clean,  adj.,  and  adj.  suff.  -ly. Derivatives:  clean-li-ly,  adv.,  clean-li-ness,  n. cleanness,  n.  —  ME.  clennesse,  fr.  OE.  dinnes, fr.  dine.  See  dean,  adj.,  and  -ness, cleanse,  tr.  v.  —  ME.  clensien,  clensen,  fr.  OE. dinsian,  fr.  dine.  See  dean,  adj.
14486:feat,  adj.,  neat,  dexterous  (archaic).  —  ME.  fete.
18203:Huguenot,  n.,  French  protestant  of  the  16th  and 17th  centuries.  —  F.,  fr.  earlier  eiguenot,  fr. MHG.  eit genome  (G.  Eidgenosse),  ‘confederate’, which  is  compounded  of  eit  (G.  Eid),  ‘oath’,  and genome  (G.  Genosse),  ‘comrade’.  For  the  first element  sec  oath.  The  second  element  derives fr.  OHG.  gind$o,  ‘comrade’,  which  is  rel.  to OS.  ginot,  OE.  geneat,  OFris.  nat,  ON.  nautr, ‘companion,  comrade’,  Goth,  niutan,  ‘to  reach, attain’,  OE.  neotan,  ‘to  enjoy’,  neat,  ‘ox,  cow’. See  neat,  ‘an  animal  of  the  ox  family’.  F.  Hugue¬ not  was  influenced  in  form  by  the  name  of  Hugues Besan?on,  a  Genevan  party  leader.
21742:base  *ni-,  ‘to  shine’.  See  neat,  adj.,  and  cp.  anil and  the  first  element  in  nilgai  and  in  nainsook. Derivative:  lilac ,  adj.
23112:matelote,  n.,  a  dish  of  fish.  —  F.,  fr.  matelot. ‘sailor’,  fr.  MF.  matenot,  a  loan  word  fr.  MDu, mattenoot,  which  is  rel.  to  ON.  motunautr, MHG.  masgenoje,  lit.  ‘messmate’.  For  the  first element  in  these  words  see  mate,  ‘companion’. The  second  element  is  rel.  to  ON.  nautr,  OE. geneat,  OS.  ginot,  OFris.  nat,  OHG.  gino3, gind30,  MHG.  gend3,  G.  Genosse,  ‘mate,  com¬ panion’.  These  words  orig.  meant  ‘one  who shares  cattle  with  others’.  They  are  rel.  to  ON.
23113:/ mm,  OE.  neat,  ‘ox,  cattle’;  see  neat,  n.  Cp. matross.
25029:natterjack,  n.,  a  toad  having  a  yellowish  stripe  on the  back  (Bufo  calamita).  —  Of  uncertain  origin, natty,  adj.,  neatly  smart.  —  Perhaps  rel.  to  F.  net, ‘neat’ ;  see  neat,  adj.
25079:Nearctic,  adj.,  pertaining  to,  or  designating,  the arctic  and  temperate  regions  of  North  America ; used  esp.  in  botanical  and  zoological  classi¬ fication.  —  Compounded  of  ne-  and  arctic, neat,  n.,  an  animal  of  the  ox  family;  cattle.  — ME.  net,  neet,  fr.  OE.  neat,  rel.  to  OS.  not,  ON. naut,  Swed.  not,  Dan.  nod,  OFris.  ndt,  OHG. nog,  ‘ox,  cattle’,  and  to  OE.  neotan,  ‘to  use, enjoy’,  OS.  niotan,  ON.  njota,  OFris.  niata, OHG.  (gi)niogan,  MHG.  geniegen,  G.  genieften, ‘to  enjoy’,  Goth,  niutan,  ‘to  reach,  attain’,  ga- niutan,  ‘to  catch’,  OE.  nytt,  ON.  nyt,  OHG., MHG.  nuz,  G.  Nutzen,  ‘use,  profit,  advantage’, and  cogn.  with  Lith.  nauda,  ‘use,  possession’, Lett,  nauda,  ‘money’.  All  these  words  derive  fr. I.-E.  *neud-,  ‘to  possess,  use,  enjoy’.  Accord¬ ingly  OE.  neat,  ON.  naut,  etc.,  lit.  denote  'a  use¬ ful  animal'.  Cp.  the  second  element  in  Huguenot and  in  matelote.
25080:neat,  adj.,  pure,  undiluted;  cleanly,  tidy;  elegant.
25303:net,  adj.,  free  from  all  deductions.  —  ME.,  fr. MF.  (=  F.),  ‘neat,  clean’.  See  neat,  pure’. Deriva'tive:  net,  tr.  v.,  to  gain  as  net  profit, nether,  adj.,  lower.  —  ME.  nethere,  nithere,  fr. OE.  neodera,  nidera,  ‘lower  ,  from  the  adverb neodor,  nider ,  ‘downward  ;  rel.  to  the  adverbs OS.  nithar,  ON.  nidr,  OFris.  milter,  Du.  neder, neer,  OHG.  nidar,  MHG.  nider,  G.  nieder (whence  the  adjectives  OS.  nithiri,  ON.  ned(ar)ri, Dan.,  Swed.  nedre,  OFris.  nithera,  Du.  neder , OHG.  nidari,  nidaro,  MHG.  nider(e),  G.  nieder ) ; prop,  comparatives  formed  fr.  I.-E.  *nl-,  down.
=== KLN1966 alembic
KLN_1971.txt:10785:alembic, n. — ME., fr. OF. (=F.) alambic, fr. 
KLN_1971.txt:10789:‘cup, cap of a still, alembic’, which is of uncer- 
KLN_1971.txt:137882:limbec, n., alembic {archaic). — Aphetic for alem- 
KLN_1966.txt:2149:man.  Cp.  F.  allemand,  ‘German’,  which  also derives  fr.  Teut.  Alamann-  (see  allemande). alembic,  n.  —  ME.,  fr.  OF.  (=F.)  alambic,  fr. OSp.  (=  Sp.)  alambique  fr.  Arab,  al-anbtq,  ‘the still’,  which  is  formed  fr.  al-, ‘the’,  and  Gk.  4p.(3tl;, ‘cup,  cap  of  a  still,  alembic’,  which  is  of  uncer¬ tain,  possibly  Semitic  origin.  Cp.  It.  lambicco, which  is  of  the  same  origin  as  Sp.  alambique. Alenu,  n.,  concluding  prayer  ( Jewish  liturgy).  — Heb.  ‘dlimi,  lit.  ‘upon  us’,  formed  fr.  'al,  ‘on, upon’,  with  -dnu,  the  pronom.  suff.  of  the  1st person  in  the  plural.  The  prayer  is  so  called from  the  first  words  ‘alenu  leshabbiah,  ‘it  is  (in¬ cumbent)  upon  us  to  praise’.  Heb.  ‘al  is  rel.  to ‘aid11,  ‘he  went  up’.  See  aliyah.
KLN_1966.txt:21755:limbec,  n.,  alembic  (archaic).  —  Aphetic  for  alem¬ bic.
=== KLN net
KLN_1971.txt:159456:new, ‘beautiful’. Cp. natty, net, adj., nitid, niton. 
KLN_1971.txt:160784:net, adj., free from all deductions. — ME., fr.
```


## [2026-09-07T18:20:44.336Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '159440,159470p' KLN_1971.txt; echo \"=== 1966 neat adj\"; sed -n '25080,25086p' KLN_1966.txt",
 "description": "Print Klein neat entry"
}
```


### [2026-09-07T18:20:44.438Z] TOOL RESULT

```
Lett, ttduda, ‘money’. All these words derive fr. 
L-E. *neud-, ‘to possess, use, enjoy’. Accord- 
ingly OE. neat, ON. naut, etc., lit. denote ‘a use- 
ful animal \ Cp. the second element in Huguenot 
and in matelote. 

neat, adj., pure, undiluted; cleanly, tidy; elegant. 

— MF. (= F.) net, ‘clean, pure, neat’, fr. OF., 
fr. L. nitidus, ‘shining, bright, clear, well-favor- 
ed, elegant, smart, trim’, fr. nitere, ‘to shine’, fr. 
I.-E. base *nei-, *m~, ‘to shine’, whence also 
Mir. niam, ‘gleam, splendor’, niamda, ‘shining’, 
OIr. noib, ‘holy’, niab , ‘strength’, W. nwyfiant , 
‘gleam, splendor’, possibly also OI. ni-lah, 
‘swarthy, black, dark’, OPers. naiba-, ModPers. 
new, ‘beautiful’. Cp. natty, net, adj., nitid, niton. 
Cp. also lilac. 

Derivatives: neat-ly, adv., neat-ness, n. 

’neath, neath, prep., beneath. — Short for be- 
neath. 

neb, n. 1) the beak or bill of a bird; 2) nose; 3) 
point, tip. — ME. nebbe, fr. OE. nebb, ‘beak, 
nose, face’, rel. to MLG., MDu, nebbe, ‘beak’, 
ON. nef ‘beak, nose’, Du. sneb, snavel, OHG. 
snabul, MHG. snabel, G. Schnabel, ‘beak’, 
OFris, snavel , ‘mouth’. Cp. nib, nipple, snaffle, 
snap, snipe, snow, ‘a kind of vessel’. 
=== 1966 neat adj
neat,  adj.,  pure,  undiluted;  cleanly,  tidy;  elegant.
—  MF.  (=  F.)  net,  ‘clean,  pure,  neat’,  fr.  OF., fr.  L.  nitidus,  ‘shining,  bright,  clear,  well-favor¬ ed,  elegant,  smart,  trim’,  fr.  nitere,  ‘to  shine’,  fr. I.-E.  base  *nei~,  *nl-,  ‘to  shine",  whence  also Mir.  niam,  ‘gleam,  splendor’,  niamda,  ‘shining’, OIr.  noib,  ‘holy’,  niab,  ‘strength’,  W.  nwyfiant, ‘gleam,  splendor’,  possibly  also  OI.  nf-lah, ‘swarthy,  black,  dark’,  OPers.  naiba-,  ModPers. new,  ‘beautiful’.  Cp.  natty,  net,  adj.,  nitid,  niton. Cp.  also  lilac.
Derivatives:  neat-ly,  adv.,  neat-ness,  n.
’neath,  neath,  prep.,  beneath.  —  Short  for  be¬ neath.
neb,  n.  1)  the  beak  or  bill  of  a  bird;  2)  nose;  3) point,  tip.  —  ME.  nebbe,  fr.  OE.  nebb,  ‘beak, nose,  face’,  rel.  to  MLG.,  MDu,  nebbe,  ‘beak’, ON.  nef,  ‘beak,  nose’,  Du.  sneb,  snavel,  OHG. snabul,  MHG.  snabel,  G.  Schnabel ,  ‘beak’, OFris,  snavel,  ‘mouth’.  Cp.  nib,  nipple,  snaffle, snap,  snipe,  snow,  ‘a  kind  of  vessel’.
Derivative:  nebb-ed,  adj.
Nebalia,  n.,  a  genus  of  marine  crustaceans  (zool.)
```


## [2026-09-07T18:20:52.695Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=25060 && NR<=25085' KLN_1966.txt | grep -o \"10[0-9][0-9]\" | head; echo \"--- markers\"; grep -n \"^\\s*10[23][0-9]\\s*$\" KLN_1966.txt | sed -n '1,5p'; echo \"=== PLA files\"; ls incoming/PLA/ 2>/dev/null; ls /home/sfmqrb/git/rishe/data/verification/sources/refs/ | grep -i pla",
 "description": "Check Klein page markers and PLA files"
}
```


### [2026-09-07T18:20:54.048Z] TOOL RESULT

```
--- markers
24786:1021
24831:1022
24960:1028
25059:1033
25092:1035
=== PLA files
PLA_asbaghi_1988_ia_djvu.txt
PLA_asbaghi_1988_ia.pdf
PLA_pages.txt
```


## [2026-09-07T18:21:00.932Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^\\s*4[5-9]\\s*$\" KLN_1966.txt | head -5; echo \"=== alembic line\"; grep -n \"alembic\" KLN_1966.txt | head -3; echo \"=== PLA anbiq\"; grep -n -i \"anbīq\\|anbiq\\|ambiq\\|inbīq\\|inbiq\" PLA_pages.txt PLA_asbaghi_1988_ia_djvu.txt | head -20",
 "description": "Klein p47 marker and Asbaghi anbiq"
}
```


### [2026-09-07T18:21:02.336Z] TOOL RESULT

```
2114:45
2142:46
2186:49
=== alembic line
2149:man.  Cp.  F.  allemand,  ‘German’,  which  also derives  fr.  Teut.  Alamann-  (see  allemande). alembic,  n.  —  ME.,  fr.  OF.  (=F.)  alambic,  fr. OSp.  (=  Sp.)  alambique  fr.  Arab,  al-anbtq,  ‘the still’,  which  is  formed  fr.  al-, ‘the’,  and  Gk.  4p.(3tl;, ‘cup,  cap  of  a  still,  alembic’,  which  is  of  uncer¬ tain,  possibly  Semitic  origin.  Cp.  It.  lambicco, which  is  of  the  same  origin  as  Sp.  alambique. Alenu,  n.,  concluding  prayer  ( Jewish  liturgy).  — Heb.  ‘dlimi,  lit.  ‘upon  us’,  formed  fr.  'al,  ‘on, upon’,  with  -dnu,  the  pronom.  suff.  of  the  1st person  in  the  plural.  The  prayer  is  so  called from  the  first  words  ‘alenu  leshabbiah,  ‘it  is  (in¬ cumbent)  upon  us  to  praise’.  Heb.  ‘al  is  rel.  to ‘aid11,  ‘he  went  up’.  See  aliyah.
21755:limbec,  n.,  alembic  (archaic).  —  Aphetic  for  alem¬ bic.
=== PLA anbiq
ugrep: warning: PLA_pages.txt: No such file or directory
ugrep: warning: PLA_asbaghi_1988_ia_djvu.txt: No such file or directory
```


## [2026-09-07T18:21:06.728Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA && grep -n -i \"anbīq\\|anbiq\\|ambiq\\|inbiq\\|Alembik\\|Destillier\" PLA_pages.txt | head -20",
 "description": "Grep Asbaghi for anbiq"
}
```


### [2026-09-07T18:21:06.774Z] TOOL RESULT

```
1888: amirabür                                                                                      27                                                             ambiq
1928:=>! - ”ambig:                                  "Alembik"              pers.          ®, mand.              anpaga        (iranian,           talm. xmyıx ) 9,
1929:              syr.             anı            10,       sp.       alambique,              engl.        alembic,           frz.       alambic,         dtsch.
1930:              Alembik                   "Destillierkolben"                           11, wahrscheinlich                     aus       dem     pers.    ‘«_7T äbnik.
6509:ae            - bambiq:                  "Keller           aus       Holz    mit       gewölbtem        Dach"   aus        dem     pers.     £ ham
```


## [2026-09-07T18:21:13.189Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA && sed -n '1885,1945p' PLA_pages.txt",
 "description": "Print Asbaghi p27 context"
}
```


### [2026-09-07T18:21:13.233Z] TOOL RESULT

```
12.           Mackenzie         Ss.       v.
13.           Frahang         Pahlavik               s.     v.
14.           Wahrmund         s.       v.
 amirabür                                                                                      27                                                             ambiq

     7.                                  _                                                                                            -
Pi                         _ ”amiräbür:                        "Stallmeister"                   aus dem ar. „-ı ’amir + pers.                            _.>'
              ähör             s.       äbör,           syr.         ı91lyel.

                       j                ._                                  __                             u
ob!                            - ’amirbäris                       = ’ambarbäris                 s. ’ambarbäris               .
 r
ol-           An:          "Zeit",                 offensichtlich                    handelt           es     sich    um    einen         Singular,       der
              analog                    zum        Plural,           nachgebildet                   wurde.      s.d\,i ’awan u.uL; ’ibban .

              .5           >        -ı7                               >          -              >      -
 o»ab1-                        "anabir:              Pl.       v._1 ambär                 s.        'ambar.

  „3                             -
21                         "anafir: Pl. v._si’angar s. ”’ankar.
              s                           -                                                                                                               -
„ob                -       ”anähid:                  "Venus"          (astrolog.)                    pers.     ı aus       dem       pers.    „si     nahid
               << mp.                   up           anähit          am.             anähitä           2, ap.        anähita          "fleckenlos;            Göttin
              Anahita" -

      3,

Löl _ ”ambär:                                  "Magazin,              Kornspeicher"                    pers.        9 aus    dem pers.           21       ambar
                                                                                                                     ’
                  —mp.>r                           hanbar          ap.           hambara              4      syr.    fyaatlao 5,

     .$
ol - ”anbar = “anbar s.                                               “anbar .
   „5             -                                                            _                                   _
ob 21 - ”anbarbäris                                                = ’ambarbäris                     s. ”’anbarbäris             .

au) -
          s
                   ’anba:                 "Mango"              aus    dem     pers,            as] anbe        m.           2         ambag     6, syr.Nest
                                                                                                                                                                       7


 ..3                                -
=>! - ”ambig:                                  "Alembik"              pers.          ®, mand.              anpaga        (iranian,           talm. xmyıx ) 9,
              syr.             anı            10,       sp.       alambique,              engl.        alembic,           frz.       alambic,         dtsch.
              Alembik                   "Destillierkolben"                           11, wahrscheinlich                     aus       dem     pers.    ‘«_7T äbnik.




1. al-Marfa®                              s.       v.,       Addai     Scher          s.       v.
2.        Nyberg                Bd.           II     s.      v.
3.        Wahrmund                      Ss.    v.,        al-MuCarrab                s.    v.
4.        Bartholomae                          s.       v.,       Mayrhofer           s.       v.
5.        Brockelmann                          s.       v.
6. Hosrow                       Qobädän                 n.     Chista       9.       S.    1072
7.        Brockelmann                          Ss.      v.
8. al-Mundid                              s. v.
9.        Macuch                Ss.      v.
10.           Brockelmann                          s.     v.
11.           Wildhagen                       s.     v.
```


## [2026-09-07T18:21:28.716Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in SKT.txt FSD_vol1.txt LKT.txt DEV.txt PHN.txt DOZ.txt LAM.txt AFA.txt FVQ_pages.txt; do echo \"=== $f\"; grep -n -i \"alembic\\|alambic\\|anbiq\\|anbīq\\|ambix\\|Destillier\" $f | head -6; done",
 "description": "Grep multiple books for alembic"
}
```


### [2026-09-07T18:21:30.083Z] TOOL RESULT

```
=== SKT.txt
527:Alembic,  0  vessel  for  distilling.  (F  — Span.-Arab.-Gk.)  M.  E.  aUpthk."?. altxmhique  (Cot.)  •  Span,  alambiqut.  — Arab.  tU,  the;  and  antik  (pronouncctl  am' ink's,  a  still.  —  Gk.  li/i^i^.  a  cup,  goblet; can  of  a  GtjU.-Gk.  &^^,  4l/i^<vr,  foot  of  a goulct ;  allied  to  L,  nntbo^  %  bow.
=== FSD_vol1.txt
10898:Al'a-math,  1   al'a-mafh;  2   al'a-mSth,  n.  Bib.  (DouaO. a-Iam'bict,  n.  An  alembic.
11540:[Hare.]  To  distil,  as  by  the  alembics.  a-Iem'bi- cate}.
11552:The  world  cares  little  for...  any  thing  J a   man  has  to  utter  that  has  not  previously  been  dis- tilled  in  tho  alembicol  hia  life.
11559:[   <   F.  alambic,  <   LL.  alambiscus,  <   Ar.  abanblq,  <   al,  AI"e-the'a,  I   al'i-fhl'a  or  o-irou-s;  2   J£e_t,h6'a  or CUP  ‘   a-lam'b,c^
55957:Cam"pan',  1   koA'pon';  2   cab 'pan',  Jeanne  L.  H.,  Madame de  (nee  Genest)  (»°/«I752-Vi«I622).  A   French  teacher  and writer:  confidante  of  Marie  Antoinette;  Memoirs  of  the  Pri~ rate  Life  of  Marie  Antoinette.  LS22. cam-pa'na1, 1   kam-pe'na;  2   cam-pa'na,  n.  1.  A   bell* shaped  vessel  forming  the  upper  portion  of  an  alembic. See  illu3.  under  alembic.  2.  The  pasqueflower  ( Anem- one pulsatilla).  3.  Arch.  Any  bell-shaped  member.
83895:boobook. —   c.splnt,  n.  An  English  plant,  the  wake-robin.  CU-cur  bit,  1   Juu-kurbit;  2   cu-cGr'bit,  n.  1,  The  body c.» pintle X.  °f  an  alembic,  originally  gourde -shaped hence,  any
=== LKT.txt
233:[Aus  pers.  äb  s.  hier  Nr.  5  und  kär 'Werk,  Tat'  Horn  NpEt  S.  185,  Nr.  831; dazu  das  T  des  AbstraktumsJ,  ebenso bind.  'Wasserarbeit'.  Hieraus  angloind. abcaree,  abkary  ursprünglich  'die  Arbeit, Wasser  zu  destillieren  und  zu  verkau- fen', heutzutage  'die  Steuer  auf  diesas Geschäft'.  Abkary-System  ist  also das  System  der  Besteuerung  geistiger Getränke  in  Britisch-Indien.  [Hobson- Jobson  2.
399:[Das  selbst  aus  gr.  äußiE;  in  der  Aus- sprache amblk]  'Destilliergefäß'.  Hieraus z.  T.  mit,  z.  T.  ohne  ar.  Art.  lat.  alam- bicum  und  die  romanischen  Formen: it.  lambicco,  lambiccio,  limbiccio  'Destil- lierkolben', Vb.  lambicare  'durch  das Reagenzglas  gehen,  genau  prüfen',  lam- biccarsi  od.  beccarsi  il  cervello  'sich  den
402:Kopf  zerbrechen';  prov.  elamhic,  frz. tiliimbic,  runi.  alanibic,  .sp.  alambiqnc, pg.  lamhiqnc;  en^'l.  aleinhic.  Vb.  frz. alamhiquer  'destillieren',  auch  figür- licli.  [DE  r)(i.  Devic  DEl  5.  ML  ii± Warlbg  FEWb  57.  GIBBS  in  American Journal  of  Science  and  Arts  XXXIII,  325.
2662:1130.  Ar.  kattära: 'Destillierkolben'  [vom  Vb.  kattara 'destillieren',  II.  Form  von  katara  s.  hier Nr.  1128];  hieraus  mit  ar.  Art.  sp.  alqui- tara  'Destilliergefäß'  [=  alatnbiqne,  s.  hier Nr.  79.    Dicc  Gast  137  a.    DE  186].
6207:alambic  79
7423:Aegidius  951 aegyptus  1222 alambicum  79 alchanna  867 algorismus  890 algorithmus  890 alleluia  793 ahnageshim  1348 almutium  1520 amaracum  1411 amen  68
=== DEV.txt
270:Alambic  Esp.  alamhique,  port,  lamhique,  itai.  lambico, de  l'arabe  (^^^^j^î  al-anhiq,  venant  du  grec  a^^i^^  vase  à distiller,  précédé  de  l'article  arabe  al.
2403:Alambic.
2404:Alambique,  esp.  voy.  Alambic.
2698:Afxé'/^,  voy.  Alambic.
3773:Lambico,  ital.  voy.  Alambic.
3774:Lambique,  pg.  voy.  Alambic.
=== PHN.txt
1052:différence qui existe entre : alambic et vase à distillation; —
1095:ALAMBIC, s. m. (a.-gr.)
1098:cordent à regarder alambic comme la transcription du grer
1791:distillation à l'alambic; précédé de ^^j \rotW]esprit, <S^I ^jjARH 43
=== DOZ.txt
=== LAM.txt
1610:feit poui» almageste, alchimie, alambic, c'est-à-dire qu'ils ont accolé leur
6982:rencontre plusieurs termes d'alchimie, les éîixirs obj-TV» » les alambics
=== AFA.txt
=== FVQ_pages.txt
```


## [2026-09-07T18:21:43.292Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | grep -i \"WEB\\|SPG\\|AIN\\|TAD\\|SNS\\|MON\\|ARY\"; echo \"=== PHN alambic\"; sed -n '1090,1115p' PHN.txt; echo \"=== LKT 79\"; sed -n '390,410p' LKT.txt",
 "description": "Check WEB local and read PHN/LKT"
}
```


### [2026-09-07T18:21:43.352Z] TOOL RESULT

```
AIN.txt
MON_part1.txt
MON_part2.txt
NYB_vol2_glossary.txt
SNS_pages.txt
SNS.txt
SPG_keilinschriften1881.txt
TAD_pages.txt
TAD.txt
WEB_vol1.txt
=== PHN alambic
gypte, il s'empara de l'atabékiat de Syrie après la
mort de Nour eddîn. Signalé, dès sa jeunesse, par
ses exploits contre les chrétiens, il parvint à leur
reprendre Jérusalem, et mourut en i iq«3, laissant un
frère nommé Malek Adel , et dix-sept fils.
ALAMBIC, s. m. (a.-gr.)
(^Afj^lt [aUn^] Nom d'un appareil de chimie qui sert à la
distillation de certains liquides. — Les étymologistes s'ac-
cordent à regarder alambic comme la transcription du grer
i(x€t^y vase- à bords relevés, précédé de l'article arabe al. Cepen-
dant il est probable que les chimistes ont emprunté directe-
ment ce terme aux Arabes, qui sans doute l'avaient tiré de la
langue grecque. — Les Espagnols et les Portugais écrivent
alnmbique.
ALBUFÉRA, n. pr. (a.)
5;.A^I [aU>ouh'aîrat] le lac, ou la petite mer, forme diminutive
de^^ [iaAV] mer. Nom d'un lac d'Espagne , au sud de Valence ,
et tout près de la Méditerranée avec laquelle il' communique ;ALC 17
il a quarante-quatre kilomètres de tour. Près de ce lac, en
181 a, le général français Suchel remporta une victoire qui
lui valut le titre de duc d'Albuféra. — On trouve encore en
espagnol albuhera, et en portugais albufeira, avec le sens de
lac ou lagune, ce qui confirme l'origine arabe de ces mots.
ALCAÇAR et ALCAZAR, n. pr. (a.)
jjaJk}\ [alqas'r] le château, dénomination commune à divers
châteaux forts ou palais élevés par les Maures, et par suite
=== LKT 79
75.  Ar.  'aiiäk:
'Ziege',  aber  'anäk  al-ard  wörtlich 'Erdziege'  heißt  der  'Dachs'  od,  ein anderes  ähnliches  Tier.  Hieraus  [mit Vertauschung  der  Nasalen]  Alamac, Amak  ein  Sternname:  y  Andromedae. [Devic  DEt  40.  Ideler  Sternn  126 bis  127.
76.  Tk.  Anadolu:
'Kleinasien'  [vom  gr.  dvaxujXri  'Aufgang sc.  der  Sonne',  'Osten'  vom  Vb.  dvareWo)]. Zur  Bezeichnung  Kleinasiens  in  allen europäischen  Sprachen  gebraucht,  z.  B. dtsch.  Anatolien.  —  Hieraus  rum.  ana- dol  'eine  Art  tk.  Pelzmantels'.
77.  Pers.  änbär:
'Schuppen',  gesprochen  ämbär  [von ämbästän  'anfüllen,  anhäufen'  Horn NpEt  S.  26,  Nr.  III],  ebenso  tk.  ambar. Hieraus  rum.  ambar,  hambar  'Speicher, Schuppen,  Kornboden',  Ableitung  ham- bara^;  russ.  bulg.  serb.  ambar  'Scheune, Schuppen,  Speicher',  poln.  ambar,  im- bar,  kl  russ.  ambar  'Niederlage'.  — VÖLLERS  in  ZDMG  LI,  299  Nr.  94 will  jedoch  anbär  aus  gr.  ^lunöpiov  ab- leiten.   [Gorjajew,4.  Bern  SlEtWb  28.
78.  Ar.  'anbar:
Mit  Assimilation  'ambar  gesprochen; hieraus  it.  ambra,  frz.  ambre,  sp.  pg. ambar,  [mit  ar.  Art.]  alambar,  alambre, rum.  ambrä,  ambru;  engl,  ambre,  ndl. amber,  dtsch.  Amber;  russ.  ambra.  — Aniber  ist  eine  ihrer  Herkunft  nach zweifelhafte,  ilirer  Zusammensetzung nach  unvollständig  bekannte,  sehr  teure, dunkelgraue  Masse,  die  in  früheren Zeiten  in  der  Medizin  hochgeschätzt war,  während  sie  heute  fast  nur  noch zur  Herstellung  von  Parfümen  benutzt wird.  In  rundlichen  oder  kantigen Stücken  auf  dem  Meere  schwimmend oder  am  Strande  angespült,  wird  die Ambra  im  Indischen  Ozean  gefunden und  für  feine  Sorten  je  kg  5000  Mark und  mehr  gezahlt.  Vermutlich  ist  der Amber  die  verhärtete  Kotmasse  des Pottwals  Catodon  macrocephalus  Lac. —  Dazu  engl,  yellow  amber  'Bernstein'. [DE  188/9.  Eguilaz  258.  ML  441. Gorjajew  4.
79.  Ar.  anbik:
[Das  selbst  aus  gr.  äußiE;  in  der  Aus- sprache amblk]  'Destilliergefäß'.  Hieraus z.  T.  mit,  z.  T.  ohne  ar.  Art.  lat.  alam- bicum  und  die  romanischen  Formen: it.  lambicco,  lambiccio,  limbiccio  'Destil- lierkolben', Vb.  lambicare  'durch  das Reagenzglas  gehen,  genau  prüfen',  lam- biccarsi  od.  beccarsi  il  cervello  'sich  den
Ar.  aiiilnl  ]
8
Kopf  zerbrechen';  prov.  elamhic,  frz. tiliimbic,  runi.  alanibic,  .sp.  alambiqnc, pg.  lamhiqnc;  en^'l.  aleinhic.  Vb.  frz. alamhiquer  'destillieren',  auch  figür- licli.  [DE  r)(i.  Devic  DEl  5.  ML  ii± Warlbg  FEWb  57.  GIBBS  in  American Journal  of  Science  and  Arts  XXXIII,  325.
80.  Ar.  audul :
(Auch  haudrd;  selbst  aus  dem  pers. und  letzten  Endes  aus  sanskr.  himlöla, andöla  'chinesische  Sänfte',  vgl.  ZDMG LI,  «58;  LH,  i282;  auch  syrisch  andül BrLexSyr  28  a]  'Sänfte'.  Hieraus  viel- leicht mit  ar.  Art.  sp.  lando  'leichter mit  Maultieren  bespannter  Wagen  mit 4  Sitzen'  [Dicc  Gast  1240c,  freilich  mit unrichtiger  Etymologie],  frz.  londau, engl,  landau,  dtsch.  Landau,  volksety- mologisch umgestaltet  zu  Landauer.  — Der  Vers  in  GOETHES  'Hermann  und Dorothea'  I,  56:  ,Im  geöffneten  Wagen (er  war  in  Landau  verfertigt)"  kann natürlich  nicht  als  Beweis  für  die*Ety- mologie  gelten,  wonach  die  Wagen  nach ihrem  Ursprungs-  und  Herstellungsorte, der  bayrischen  Stadt  Landau,  benannt sein  sollen.  Ebensowenig  bewiesen ist  die  Existenz  eines  angeblichen  eng- lischen Erfinders  namens  LANDOW. [Kluge  273.  [Dagegen  wohl  doch  mit Recht  Jacob  EMA  97.]
81.  Ar.  anf:
'Nase'.  Anf  al-faras  [s.  hier  Nr.  586] 'die  Nase  des  Pferdes'  ist  der  ar.  Name eines  im  Maule  des  Sternbildes  Pegasus stehenden  Sternes;  hieraus  Enif  'e Pegasi'.  [Devic  DEt  109/110.  Ideler Sternn  117,
82.  Mal.  ang'grek:
[Pijn  7:  standelkruit]  'eine  Orchideenart' in  den  Tropen,  besonders  Angrecum fragrans  Thou.,  deren  Cumarin  enthal- tende Blätter  den  Bourbon-  od.  Faham- tee  liefern,  und  Angrecum  sesquipedale Thou.,  bei  uns  in  Treibhäusern  gehalten. Aus  dem  mal.  entstand  zuerst  frz.  an- grec,  hieraus  der  botanische  Name  lat. angraecim  od.  angrecum.  [Rom Forsch  III,  492.    Devic  DEt  32.
83.  Ar.  'ankabüt:
'Spinne'.  Wegen  der  Ähnlichkeit  der sich  kreuzenden  Meridiane  und  Parallel- kreise am  Astrolabium  hiefa  ein  Teil desselben  sp.  alhancahit,  frz.  alancabuth. [Devic  DEt  5.    Laramens  Rem  4.
```


## [2026-09-07T18:21:54.178Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WEB alembic\"; grep -n -i \"alembic\" WEB_vol1.txt | head -8; echo \"=== WEB ambix\"; grep -n -i \"ambix\\|anbiq\\|al-anbiq\" WEB_vol1.txt | head -8",
 "description": "Grep Webster for alembic/ambix"
}
```


### [2026-09-07T18:21:54.245Z] TOOL RESULT

```
=== WEB alembic
5131:al-, in Arabic, a prefix, corresponding to the Italian il, and the Spanish el and la. equiva- lent to the English definite article, the; as, Alkoran, the Koran, or the book; alcove, al- chemy, alembic, almanac.
5379:ALEMBIC
5386:T urifies, or works a change; as, the alembic of a vivid imagina-
108115:lim’bec, lim’beck, n. an alembic; a still. [Obs.] 3
=== WEB ambix
5377:a-lem/bic, n. [L. alambicus; Ar. alanbiq; al, the, and anbiq, Per. ambiq, a still; Gr. ambix, a cup of a still.]
```


## [2026-09-07T18:21:55.621Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== TAD anbiq\"; grep -n \"انبیق\\|أنبيق\\|الأنبيق\\|انبيق\" TAD_pages.txt TAD.txt | head -8; echo \"=== AFM rownaq\"; grep -n \"رونق\\|الرونق\" AFM_pages.txt | head -10",
 "description": "Grep TAD and AFM"
}
```


### [2026-09-07T18:21:55.686Z] TOOL RESULT

```
=== TAD anbiq
=== AFM rownaq
2956:ܡ ܐܠ والترونق وايرئاق ܐ ܢ‎ 1
3877:( النرْق) اليد ( شفاء الغذيل ) ٠‏ معرب نزخ وهعناه السعد والرونق
```


## [2026-09-07T18:22:08.452Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^\\s*4[3-5]\\s*$\" WEB_vol1.txt | head; echo \"=== ctx\"; sed -n '5370,5395p' WEB_vol1.txt; echo \"=== AFM pages markers\"; grep -n \"\\[pdf page\" AFM_pages.txt | head -5; python3 -c \"\nimport re\nt=open('AFM_pages.txt',encoding='utf-8',errors='replace').read()\nprint(len(t.split('\\f')))\"",
 "description": "Webster page check and AFM page structure"
}
```


### [2026-09-07T18:22:09.867Z] TOOL RESULT

```
=== ctx
āle’house, 7. a house where ale is sold; tav- ern; saloon.
ale knight, a drinking companion. [Obs.]
alem, n. [Turk. alem, a flag, banner.] the standard of the Ottoman empire.
Al/e-man-ni, n.pl. the Alamanni.
Al-e-man’nic, a. [L. Alemannicus, pertaining io the Alamanni, from Goth: alamans, all
men.] relating to the Alamanni.
Al-e-man/nic, n. the German dialect of the Alamanni.
a-lem/bic, n. [L. alambicus; Ar. alanbiq; al, the, and anbiq, Per. ambiq, a still; Gr. ambix, a cup of a still.]
1. a chemical apparatus formerly used in distilla- tion, and usually made of glass or metal. The bot- tom part, containing the substance to be distilled, was called the cucurbit; the upper part which re- ceived and condensed the steam was called the head, the beak of which was fitted to the neck of a re- ceiver. 2. anything that refines,
ALEMBIC
need
be detected. at full length; lengthwise.
its sound.
a-lep’i-d6te, a. having no scales, house as a sign. [Obs.]
Gr. larix, the larch.} a chilean tree of the pine family.
all’ for alla, for L. ad and illam, on the, an
T urifies, or works a change; as, the alembic of a vivid imagina-
tion. å-Jem’broth, n. a double chloride of mercury 3 and ammonium, formerly used by alchemists. A leniçon lāce, a delicate but durable lace of
I e-point, originating in Alencon, France, in the seventeenth century. It has a solid floral pattern made in small sections and is pieced together so that the seams cannot
a-length/’, adv. at full length; along; stretched
a/leph (-lif), n. [Heb., lit., ox, leader.] the first letter of the Hebrew alphabet, a neutral vowel: various diacritical marks determine
ale; dote n. [Gr. a priv., and lepis (lepido- a t a oe A RR £6 tis), scale.| any fish whose skin is not scaly.
rom aleator, a gamester; alea, a —),- : Gi Ale’pole, n. a pole set up in front of an ale- Aj.ex.an/dri-in, a. 1.
a-lérce’, n. [Sp. alerce, the larch tree; L. larix;
= Digitized by Arya Samaj Foundation Chennai and eGangotri _
Alexandrine
=== AFM pages markers
198
```


## [2026-09-07T18:22:16.297Z] TOOL CALL #32: Bash

```json
{
 "command": "python3 tools/ref_page.py AFM:74 2>&1 | head -60",
 "description": "Fetch AFM page 74"
}
```


### [2026-09-07T18:22:17.707Z] TOOL RESULT

```
no scan of AFM covers printed page 74 (see 'scans' in refs_online.json)
```


## [2026-09-07T18:22:22.146Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('AFM_pages.txt',encoding='utf-8',errors='replace').read()\npg=t.split('\\f')\n# find which chunk contains 'رونق' or the ر section\nfor i,p in enumerate(pg):\n    if 'رونق' in p or 'روزنامج' in p or 'رونا' in p:\n        print('chunk',i, repr(p[:120]))\nEOF",
 "description": "Locate rownaq in AFM"
}
```


### [2026-09-07T18:22:23.379Z] TOOL RESULT

```
chunk 91 'ܚܝ ܀ ¶ ܚܚ\n#\n١ل\u200f ܝܢ ورم في حسجاب الدماغ تحدث عنه 3 مركب من 919\n50 وم :ܨ اي ورم ومنة ܨܥ ` ܣܪܣܤܣܡܐ ܨ 11 22\nال سي £ 0:09393 '
chunk 117 "3 1 ܇ «\nܝܟ 1 ܪ .2 ܢ\n1\nܨ\n- (١١5\n` 5 (التَرقد) شجر عظام اوهي ܡܦ\u200e *\nبالفارسبة بهذا المعنى الاخير\u200e\n07 0 0 ' 5 2 2 #\nܐܠ ܨ( 0 "
chunk 153 'هه 00 ܐܓ\nأن طاف اقطار المسكونة اتتهى الى اذور 9 وأعر 43" 0.33\nحل عالتفى اعلهة الشرقية منة عرش مرضع .2 لس نا به الملوكة و'
chunk 172 'سيهبد ١١5\u200f\n1 20\nܡ\nستازه ¥ ^\nستاك ܟ\nستاو ^\nܚܐܘ ܙ ܟ\n2 هم ,9\nستو 6م\nܗܘ 6م\nحت $¢ ^\nܙܝ ܘ ^\nتيان وم\nؤس ܘ ^\nسدا ¥܀ ܙ\nسداب 8م\nܚܬ'
```


## [2026-09-07T18:22:28.639Z] TOOL CALL #34: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['AFM','WEB','SPG','AIN','SNS','TAD','FVF','TZF','MON','BQT']:\n    print('#####',k); print(json.dumps(d[k],ensure_ascii=False,indent=1))\n\"",
 "description": "Print full ref metadata"
}
```


### [2026-09-07T18:22:29.891Z] TOOL RESULT

```
##### AFM
{
 "title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)",
 "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt"
 ],
 "page_offset": "198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image",
 "covers_etymology": true,
 "notes": "Arabic OCR fair; Syriac/Latin etyma partially garbled.",
 "cites": "page number of Addi Shir, al-Alfāẓ al-fārisiyya al-muʿarraba (1908)"
}
##### WEB
{
 "title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)",
 "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w",
 "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/WEB_vol1.txt",
 "page_offset": "not reliably detected (page_numbers.json sparse); grep headword. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Headword bold at line start; etymology in brackets. 2nd-edition pagination is the same across 1958-1983 printings, so a 1978 page number can be checked in the 1962 vol. 1 scan for words A-(mid alphabet); vol. 2 only via lending copies.",
 "notes": "",
 "cites": "page number of Webster's New Twentieth Century Dictionary, 2nd ed."
}
##### SPG
{
 "title": "F. Spiegel - title lost in the bibliography OCR (Table IV no. 93 is missing); Table III lists Spiegel with SPG and ARP. Best guesses: Die altpersischen Keilinschriften (2nd ed. 1881) or Eranische Alterthumskunde (1871-78)",
 "edition_found": "Die altpersischen Keilinschriften, 2. Aufl. 1881 (downloaded as a guess)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/diealtpersische00spiegoog",
 "identifier": "diealtpersische00spiegoog (Eranische Alterthumskunde: in.gov.ignca.11987 vol.1, in.ernet.dli.2015.529286 vol.2, in.ernet.dli.2015.103474 vol.3)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SPG_keilinschriften1881.txt",
 "page_offset": "Keilinschriften 1881: leaf = printed + 11 for the texts, leaf = printed - 29 for the Glossar (e.g. leaf 182 = p.211). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "IDENTIFICATION UNCERTAIN. Check whether Nourai's SPG page numbers fit the Keilinschriften glossary (pp. ~200-250) or the Alterthumskunde; grep the OP word.",
 "notes": "If ARP = 'Die arische Periode' (1887) per Table IV no. 14, SPG is Spiegel's other work."
}
##### AIN
{
 "title": "E. Lidén, Studien zur altindischen und vergleichenden Sprachgeschichte, Uppsala 1897",
 "edition_found": "1897",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/studienzuraltin00lidgoog",
 "identifier": "studienzuraltin00lidgoog",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AIN.txt",
 "page_offset": "leaf = printed + 5 (e.g. leaf 9 = p.4). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Numbered word studies; grep the Sanskrit word.",
 "notes": "Built from djvu.xml."
}
##### SNS
{
 "title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/VajnameShayest",
 "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt"
 ],
 "page_offset": "242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image",
 "covers_etymology": true,
 "notes": "OCR quality is POOR: Persian text mostly garbage, Latin transliterations partially readable. Verification will usually need the page image."
}
##### TAD
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
##### FVF
{
 "title": "S.M.A. Emam Shushtari, Farhang-e Vazheha-ye Farsi dar Zaban-e Arabi, Anjoman-e Asar-e Melli 58, Tehran 1347/1968",
 "kind": "website",
 "url": "https://noorlib.ir/book/info/105056 (page viewer: https://noorlib.ir/book/view/105056?pageNumber=<N>&viewType=pdf) ; https://ketabnak.com/book/48613 (818 pp. PDF, login) ; http://parsianjoman.org/?p=1265 (download post)",
 "lookup_hint": "Alphabetical by Persian headword; noorlib page number N is the scan page — browser needed to read. Not on archive.org.",
 "local_file": null,
 "page_offset": null,
 "covers_etymology": true,
 "notes": "PDF exists on several Iranian sites (ketabnak/parsianjoman) but could not be fetched here (login/JS)."
}
##### TZF
{
 "title": "Mohsen Abolghasemi, Tarikh-e Mokhtasar-e Zaban-e Farsi, Bonyad-e Andisheh-ye Eslami 1373/1994",
 "kind": "website",
 "url": "https://ketabnak.com/book/81646 (142 pp. PDF; login) ; https://farhangoadabeirani.blogsky.com/1395/07/20/post-1048/ (download post)",
 "lookup_hint": "Not on archive.org (only his دستور تاریخی زبان فارسی: archive.org/details/20220417_20220417_2237, and تاریخ زبان فارسی on samta.samt.ac.ir / library.tebyan.net/f/Viewer/Pdf/168187 which overlap in content).",
 "local_file": null,
 "page_offset": null,
 "covers_etymology": false,
 "notes": "PDF exists but not downloadable without login."
}
##### MON
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
##### BQT
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


## [2026-09-07T18:22:38.297Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 - <<'EOF'\nimport re\nt=open('BQT_v4_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('n',len(pages))\ndef show(printed):\n    pdf=printed-1917\n    for p in pages:\n        m=re.search(r'\\[pdf page (\\d+)\\]',p)\n        if m and int(m.group(1))==pdf:\n            print('#### printed',printed,'pdf',pdf)\n            print(p[:2500])\n            return\n    print('not found pdf',pdf)\nshow(2127); show(2237)\nEOF",
 "description": "Print BQT vol4 pages 2127 and 2237"
}
```


### [2026-09-07T18:22:39.492Z] TOOL RESULT

```
n 553
#### printed 2127 pdf 210
[pdf page 210]
۲۱۷۷ رجل
ترجل - بفتح اول و ثالی و ض جیم معروف از مخترعات بوزرجمهر که در براین
وسکون لام » لوعی از جامة ابربشمی باشد که در | شطرنج ساخته و بعی کوبند لرد قدییم است اما
حبشه بافند . دوکعیتین داشته, دوی دیگررا بوزرجمهر اضافه.
فرخ - بکر اول و سکون ای و بای کرده است؟۴ - وتندساقة درخت را دی زکوبند ۴
قطهدار » بمعنی قیمت و بپزی اجنای باشد ۱ | - وترکیبی‌هم هست مرکب ازستدل وکل‌لرمتی
و بمعنی رواج و رولق هم آمده است. و فوفل و اقاقیا وحنض و سفیداب و مرداسنگه .
نرد ۲ بن وزن فرد » بازبی است ‏ | که بر ورمها ی کرم طلاکنند نافع باشد 8 -
۱ - نود که این کلمه را ازه خریدن » میداند « امشق ۱۰۲۷ کردی 8[[7 (یها »
احتکار ) » 875 « ژابا س 4۱۸ » ورك : اسشق ایضاً ۰
لاجرم از جود و از سخاوت اوست نرخ گرفته‌مدیح وصامتی ( صامت ) ارزان.
رود کی سمرقندی « تاریخ سیستان ص۳۲۱
۲ - کلمةٌ « بیو اردشین » که بازیی بوده که کوبا اردشیر آنرا اختراع نموده بترخیم
درعربی وفارسی «* نرد > شده است. * تمی‌زاده . با دگاری واه یگ و اه رت .اف دح
تاهمونه با - دریهلوی 88۷۷2۲13801۳ « خسرو کوانان اجک 5 اس
ارتك‌وی. چاپ اونوالا س۱۹ بند ۱۵ > اي ن کلمه رادر ‏ ال روما اس
قرامت سنتی۷10)۷188(۸۲۸81(501۳خوانده‌اند . ر :4‏ اج خ زیر سر
وط ,0قا2م۶3 ۱ ۸۲۵1۲ ] ۸#صف ۴2۳ سس را سس #
-29 2۲ :۱896,0.7 وفط 89 عمدزمدگ :۶ و هک
۰ .5 روط ,۳202830 ۲نطعطالها ۸ ز- 2
موز 2زن۷ :8 .م ,۱900 ودط 30 . فااده رد (تخته)
و 13 .0 ,1932 ووط 809 7127200۲6۰ 0۰ .7 اط ,8 ۵1۲2۵2ط)۲ 3 فردوسی
در شاهنامه در عنوان * اندر فرستادن رای هند شطرنج را نزد نوشین روان > ( شاهنامة بخ ج ۸
ی ۲4۹۱ ببعد ) که ظاهراً مع‌الواسطه ترجمه و اقتبای است از رساله پهلوی کزارش شترنگه ۰
بجای نیو اردشین كلم «نرد» را بکار برده :
بدین‌سان که گفتم بیاراست نرد برشاه شد سربسس با د کرد...
نپادیم برجای شطرلج ۰ لرد کنون تا بیازی که آرد نبرد؟
انا س ۰۹۷-۲۹۹۹
معر ب کلمه پیز ۶ برد » است و « نردشین > درعربی بمعتی مهره (طاس ) بازی است « دزی چ ۲
س ۹۵۵ :۲ *. ۴ - در قدیم دربازی ترد «سه مهره» بکار می بردند. موّلف قایی‌الفنون
در ( احوال نرد ) کوید : « عدد کمبتین را سه بنابرین نهادند که حرکات اکش سیارات به قلك
تمام شود ...> « امیر ( طفانشاء ) سه مهره درشش گاه داشت واحمد بدیهی سه مغره در يك گاه»
و ضرب امین را بود . احتیاطها کرد و بینداخت تا سه شش زند , سه يك پرآمد .> ( چهار مقالٌ
عروضی مصحح نگارنده طبع دوم و رك تس ۷
۴ - ای خداوندی که فطل وفخر وجاه وعز نو آن چو بیخ است » این چو درد است
آن چو غاخت این چو بار . مختاری غزئلوی « رشیدی > و رك : لغت قری‌س۹۲.
8 - رك : محیطاعظم » فرهنگه نظام +

#### printed 2237 pdf 320
[pdf page 320]
دنه نیو
خروار باشد ۱ - و بمعنی خوب و خوش و زیبا | شد۸ - و بنمن یکره ومسکه هم‌ه ت که بجریی
هم‌هت ۲ . زبده خوانند ؛ و بحذف تحتانی هم بنظر آمدم
نیمور « بر وزن طیفور : آلت تناسل | است که بر وزن لیمو باشد .
راگویند ۴ - نی نهاو ندی - نم دارویی است که
یمه ۴ - بر وزن هیمه . صف هرچیز | عربان قسب‌الزربره خوانند وآن نی باریکی‌است
راکوبند - و برقع را نیز کفته‌اند وآن‌چیزیست | است مانند فلم وباریکتر ازفلم » وآن‌تیرم رنگه
که برروی پوشند 9 . وتلخ میباشد. معده وجچگر را نافع است-
نیم هلال - یک ها , کنایه از لب نیا - بکسر هردو نون بروز ن کیمیا +
ممشوق است. بلفت سربانی نانخواء راکوبند وآن تغمی است
نیناد ۱ - با اور بثانی رسیده ونون‌بالف که بر روی خمیر نان پاشند و اجواین همان
کشیده وبدال زده, بمعنی سبر باشدو آن‌مقاومت است ‎٩‏ .
شی است باهوا۷ ۰ لیق - بکر اول و ثانی مجهول پروزن
نینوک « بنم‌نون دویم بروزن بی‌موی» | دبوء بمعتی پهلوان وتجاع ودلیر ومر‌دانه ودلاور
بفری قدریم نام قسبةٌ موصل باشد . و نام شهری ‏ وبهادر باشد *۱-. و بممنی‌ناودان هم‌آمدهء‌است ۱۱
که بونی علیه‌اللام به‌آنجا بجهت دعوت کردن | - و بکر اول و ضم ثانی بمعنی راست باش د که
مردم‌آن شهر رفته بود و وقوع بطن ماهی‌درآآنجا | نقیض کج است.
۱ يم لنکه ( صف مدل) . ۴ -ر4 : جهپانگیری » رشیدی »۰
فرهنکه نظام .
۴ - من این لیمور خود را وق ف کردم علی مبیانکم با آبها آلای.
سوزنی سمرقندی « سروری» و رك : فرهتگه نظام -
۴ - پهلوی 60286 ( بخش » سهم . جهت ) . بلوچی: 2817088 (جهت و سمت ۰
طرف ) قی : افغانی 61381 ( صف ) « هوبشمان ۱۰۹۹ » شهمیرزادی 81702 «که . ۷ص
۷ رك : اسشق ۱۹۹ و ر4 : یم پهلوی 818021 ( پیراهن مقدس ) « تاواد‌پا
4۹ وقی: لیم نن ۰ لیم‌تنه . - دراسطلاح بنایی « نیمه » پیمتی نيمه (صف)آجر بکار رود
۹-ظ . بر ساخته فرقةٌ آذرکیوان . ۷ < هوی (عر). ۸ ینوا
06() شهری درآسیای قدرم » پایتخت مملکت‌آشور واقع در کنار دجله . ر4 : قاموی
مقس ص ۲-۹۲۱ ‎٩‏ همان «زیان» است : ۹
پدرم بسکه لینیا خور شد شکم او ز نیا پر شد .
پسرسید هلی رازی « جهانگیری ».
*- پهلوی 88۷ ( شجاع . فهرمان ) [ هز. 188 ] * پونکن رس ۴۱۱۸ : * نیوه مد
دلیر و مر‌دانه بود. فردوسی (طوسی) گفت :
چوطوی و چوگودر زکشواد وکیر چو کر کین و فرهاد وبهرام نیو .>
« لغت قری ی 4۱۲ *.
۱ ممال « باو» (ه.م.) :
بر دو سوی سرآن: دوکوش چو نیو چه کنی در هی خروش وغیربو -
و۱ - رد : ینوی . سنالی خردوی « فرهنکه نظام ».
```


## [2026-09-07T18:23:07.748Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON anbiq\"; grep -n \"انبیق\" MON_part1.txt MON_part2.txt | head -6; echo \"=== MON rownaq\"; grep -n \"رونق\" MON_part1.txt MON_part2.txt | head -8; echo \"=== MON nik/niv\"; grep -n \"نیو\\b\" MON_part2.txt | head -4",
 "description": "Grep Mo'in for anbiq and rownaq"
}
```


### [2026-09-07T18:23:07.834Z] TOOL RESULT

```
=== MON anbiq
MON_part1.txt:17169:انبیق: مارا [غ. معر.] (ا.) ظرفی است برای 
=== MON rownaq
MON_part2.txt:17331:گرفتن کار: رونق و نظام یافتن کار» گرم 
MON_part2.txt:17379:نیک سامان دادن آن را؛ رونق و جلوه دادن 
MON_part2.txt:17381:رونق و نظام یافتن آن. خوابیدن کار: (کذ.) 
MON_part2.txt:18202:بی‌رونق؛ مق. رواء رواج. کالای (متاع) 
MON_part2.txt:18626:مزین بوده و مین کاری بر رونق و 
MON_part2.txt:18636:نیمه قرن هشتم ه. (چهاردهم م.) رونق 
MON_part2.txt:22945:رونق افتادن ( کالا). (اسص.) بی‌رونقی» 
MON_part2.txt:22947:بی‌خر یدار؛ بی‌مشتری. بی‌رونق» بی‌رواج. 
=== MON nik/niv
5613:دنیا و بهره‌های مادی دنیوی باشد و گریز از 
9397:آلومینیوم طبیعی است و فرمولش را می‌توان 
16786:آلومنیوم است. ک‌ائولن بسطوری که از 
19135:انجیر اسپانیولی؛ انجیر عربی؛ انجیر مغربی؛
```


## [2026-09-07T18:23:08.960Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('AFM_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(78,90):\n    print('#### chunk',i)\n    print(pages[i][:600])\nEOF",
 "description": "Print AFM chunks around p74"
}
```


### [2026-09-07T18:23:10.199Z] TOOL RESULT

```
#### chunk 78
ܚ ܝ =
( "5 5 وهو 973 6 المشتري ܥ 9
فأخوذة ܟ عن ܟ ياف ܙܒܘܢܐ (فرتكل :^ ܙ )
ܨ 501 00000 والانس والشرطي وجمعة 4( 60( في الصحاح:
67 عند العرب 15 ܢܨ بذلك بعض ܠܐ لدفعهم اهل 3 © :
55 القرآن 6 الزبانية 9 الغلاظ الشداد. وقال الاخفش :5 07
بعضهم واحدهم زبالي وقال بعضهم ارين وقال مضي ريه شيل ع ا
والقول الاول اي واحدهم زبافي ܝܟ لان ܐܚܬ ܐܠ ومعناه ܨ وهو
ܘ )3 2950 ܐ <
+ (ازج) تعريب زج وهو نصا ل السهم والخديدة 5 £ ܐܢܐ الرمح ومئة
السريالي ايحم
01 الذهب ال سه 3 تعريب )+ اي زيئة.٠وقالوا‏ فبه
ܥܝ
0 ܗ 21 اللنين واإضارمة ع خم ومعناه |ܐܨ| ܐ
( الزدياب او 9 الذهب او ماه وهو أصح < * من َرْ اي
ذهب ومن 0 اي ماء ٠٠‏ والدّر ب
#### chunk 79
ܓ
( ;3 ) 3 با لعصفر تعر يبب 1ك وهو ماء العصفر
(الرَردَمَة ورَرَدَمَهُ ) اذا عصر حلقة معرب )© ثحت 0 شفاء
الغليل ) 9 لغة فيه . وامل زَرَدَ (خنق ) 5 زَرْدَم او هو وفاق بين
اللغات فان السر يالى- 351 معناه : 65
+ |( © ما اتحدر من السيول ١‏ التابج ) معرب 95( واصل '
5191
+ (الرردى ) نوع ܝܨ !ܐ ܙܒ ;ܐ‫ 05 3:3 والعسل تعر يب زرده
* (الزرير» نبات ضمغ به فارستتة £ ويتال له بالتركيّة « الا جهره»
وقيل هو ورف ,£ وفيل نوع من الزهور ܢ̈ܝ في جبال جرجان ܝ به ( البرهان
القاطع ) ْ 0 ` 3 يف ¥ £ ومعناه ذهي
* (انّافة ) :نشوان قصير الرجلن طويل اليدين زامة كأ س البعيد وقرنة ܝ
32 ل 6 ܨ وعنقة كعنق الفرس ܣܨ ܝ زرا نه وه ن الف
#### chunk 80
⁄ܤ _- 4 =
03 ܝ وام الاب ܝܐ فقول 14 ارال 16 ١‏ الاي ( 0 55 )|
3710 3 ܘ( § الدين والعينة معرب 9 ذهب 5
# ( ال راوندك) فارسى ܝ وهو 0 = 3 2 9
+¥ (ازّري) من الناس الدع الذى لا بعد ايا 3 رارك وهو تناه
وقالوا 7 ܝ @ 9 £ 1 عليه
ܟ ) 7 890 وهنا تمن
٠ 7‏ الغليل ٠الزلابية‏ قيل هي 3 عر
أورودها £ رجز قدي ٠‏ ܐܝܝ وهر 0 قا عن أ( لها وهو عحين يقل بالشمن ثم د
بالدس ومنة ܙܠܘܒܝܐ بالسر 0 الدارجة وزاميه 22
+ )10 ) ماء زلال ܒ ‫ ا مرور £ الحلق يارد عدب 32 زلال وهو
دودة تتكون في الثلج المركزم لك ܝ دقيقة سضاء اذا 3 ܐܬ ܀ .ܟܝܐ 4
باردًا عذب فيال لذلك الماء بالفارسمّة « آب زلال» اي ماء زلال ( البيهان القاطع)
ܕܘܚ 4 09:0 بالكرد
#### chunk 81
ܣܐ ), °^
( | ; 90 ܚܐ تورك وهى آلة من )4411
ܛ )7 + £ له زهر 2 (21) 1
(|? ثيل ܬ وهو معروف 01:20 ¿ الفارسي ذَ نيل ٠وزنماير‏ لعة فيه بالفارسة
2 0:33237 السريالي. ܐܕܗ ܡ ` مشتق من الادائي (راجع
فرنكل ص :^«
+ .6 وا 0 المنطقة تمرك واي
)عدن ري لض د فيها عقّد حريفة الطعم تعريب
ܓ 0 ` بالروميّة
11111 و 211010011 3( ® 00 0 ® :9 2:00
ܪ 7611765610 وباطرمائتة 111 وبالتركة والكردنة وميا الدارجة
زحفيل وبالروسة د[ ]2 77116
>
9 1 ܣܣ ܙܢܓܪܐ
( الزنجير) السلسةة فارسة ومنة زنير ® ` والتركّة 4 3
003 <$ ا ܚ ار
وقال عنة في البرهان القاطع | معدني. ܟܐܢ ܐܢܢ يحصل في معادن ܟ
ܐܬܝܬܝ ܕ" وهو ادر 7 أوجود ٠‏ والصناعي ܘܚܝ 47 ܕܐܕ ܚܝ 
#### chunk 82
1 ܡܡ اله -
ورد ذ ره في كتاب ܐܨ ܟܐܝܐ )ܐܨ الفارسي الذي عاش في الميل الرابع المسيح ْ
وورد ايضاً ܪ † الزنادقة 010 الرنذ” 50 :في كتات الأ بستا ܩܘ حيث قبل :2 اننا
ܣܠ الصلاة٠ ٠0‏ تكى ارب الزنده ܀ وخر .هما جميعاً 0 ` 8 في
التاريخ القديم ساحر 10 المذهب ٠وقد‏ 5 الكلمة الفرس المحدثون فتافظر |
عا عل ضورة 3 زلنايك8 587 اتوت لفظة زنديق ( ܟܠܐ ܕ المشرق 141:١‏
ܠܚ `
,ܡ8‬«ܤ«_ܐܥ_ - 13307 3:03 6ܝ60 شيل با كان قات
والصحيح ان اازندبيجي معرب عن ذّ ند بيجى وهر كل قاش متين منسوج من غزر
غليظ خشن لتبطين الثياب
( ال تقِيكجّة » وعاء ادوات الراعي معرب دن بيله 5 والرَ تقليجَة انتان
كه
+1110 )© رين زنك وهو الشاطر
و كردة ) الر
#### chunk 83
ܐܬ ܒܚܕ |
5 تعريب زاك اي 9:5 ومنة السرياني الدارج ܣ والكردي
زاج
( الز .يج ) معرب زيك وهو خيط البناء
ال ܗ عند المنحجمين كتاب تعرف به احوال حركات ܆
زيك
00700 ܨ القوة ܐܪܪ 64 زور ( سُفاء الغليل ) ومنه ® والكردي
زود
0 0 العيد 2 مأخوذ من اك الغضوب ` ܐ الاخلاق
` ( 566 الزشق في :ܨ اهل المديئة ( حرط :)058 3 وهو
تصحيف < ܐ العرب 210 ٠‏ اكلام والكتاب اي زينة ونقشة واصلة ܘܟ
05000 ( مع الذهب فيطلى هنم يلتى الطبي ܝ 8 الزاووق
وى ܐܬܬܢ ٠‏ .وقد تورسعوا فيه حتى فيل ككل عزن 90 وان : يحكن فيه
الزاووف
+ 1 القصير وزوتكل ® القصير ا-لقير النّة 399 وزو نلك
ܕ
بالعر بر
+ 7 ܝܫܡ ܢܢܐ واجتمع مولد ܘܨܒ 4 الال والتزويق
( الز يربا
#### chunk 84
كا )ܐ =
( الزي ) ܐܬܝܬ مأخوذ من زي ومعناه اميوة والهيئة وهو مشتق م. زنشان أى
عاس 003 زيب ومعناه !]ܨ ܘ ܀ 449 4 الاراعي ` ܙܝܘܐ 9م41 4 اككردي ربو او زيف
ܝ الفضة
الس
(السالار» فارسي بحت وهو الزعيم والمولى
((40) وهى )> بالفارسية ومثاها الل ܕܬ
لمانا الوطن والطبّة معرب سو ومعناها 0 والناحية
دالا ارس جود اسم 13 أتتداوى بها ٠‏ واشت لغة فيه
( ܐܚܝ ) الخرز الاسود معرب شه قال في ܐܡܝܢ :شه يفت الباء
حجر ܐܚ ܕܦ بارق يشمه يا 50742 ٠وهو‏ نوعان ٠‏ نوع ܚܝ موجود في دست
قبجاق (في تركستان) وهو في الأصل ماء 2 ܧܥ . والنوع الشالي معدني يرك به
من بلاد جيلان٠‏ وقال صاحب المفردات: ان هذا اعلجر هو روح 5 27 1 له
2 مارصيتى » 6
#### chunk 85
6
١‏ السََذة ) وعاء 51 سبد ١‏ والسفط لغة فيه ٠ومنة‏ سد بالتركئة
ܥ
# 9 0 0 اللهر 5 اظنة تصحيف :ܗܒ وهو
مدمن الفسق والفجور
ܢ( 5 ثوب رقيق جيٍد .وهو ايضأ مر 3 ودرع دقيقة النسج في
إحكام ٠كل‏ ذلك نسبة الى سابور على غير القياس وهي كورة في بلاد فارس ( محيط
6:1
395 ܕ 5( الا لأعراض © 39:35 مكل اصله
ܨ يسان وهو تخفيف سك يستان اي ܕ ܠ ٠‏ قامة
0:30404[ 8000 10000 ܡܘ يشبه الذراق في ܕܚܘ عصير ازج
يدل في الأدوية ( البرهان القاطع ) ٠‏ وقال $¢ :” ومن الشجر المخاطة وهي
الى تسميها الفرس السسستان لما عرة ازجة §@ >
= + (السبرَة) طائر ܕܬ يزيدوا عليه ٠‏ فلعلة معرب سباروك وهو الام
55 سقيفة بين دارين نحتها طر دق مأخوذة من 
#### chunk 86
دم @ ܛ بد
ܕܐܠܚܟܐܟ ܢ ܨ ( 2 $ ܐܐ ܝ ܝ الغدير والبحيرة
ع مياه ٠‏ و بمعنى وسط القوم وا شرافهم معربان إها :1( ܐܚ ومعناة الثللم 8
0 على ܝ 1 عن استآم ويا ܐܡܬܝ عليه د يطلق 09 على
1 4 ܨܐ }ܝ ܢ والفضة من ܗܘ واللجام ܨ | ܕ عن ܝ 0
الدعامة
7( 3 9 تلق في 4:0 قال فرنتكل 5 ` ان
اللفظة :® ܐ معبحه ذ ܥܙ وهي _ من ܣܓܪ اي . ومنع وححز٠‏ وورد
ܣܘܓܪܐ بمنى الساجور في كتاب كايلة ودمئة طبعة يكل ٠‏ وعندي ان الكلمة
فارسنة عراقة ون سلت إى كلت ومن كير اي ماسك
(السَحِيّة) الخأق والطبيعة .قال ابو عمّيدة:هي فارسيّة .وم يأت بدليل على
ذلك 51 ܐ ® > ومعناها القاعدة والسارة
(الددس) الك فرت سحت والشخيت'والسحددت لغتان شه
+ 6 :ܠ 22 من بطون
#### chunk 87
ܣܘܠ ܛܬܐ حلفت
يشد عينَّيهِ بنديل ويتكئ على صدر واحد من 540 5 ان سار الصيان
: ܝ ويذهب كل واحد منهم الى (! ܕ % فيلتحف بساط او حاف بأو مسح
فيئام ٠‏ وحينئدك الصى ܨ : ` ܝ الات من ܧ 4.4 كان من
رفةا نه الصديان 9 : وبدعوه بأسمه ٠قاذا‏ اصاب بك ون قد سلم فيده ذلك
5 0 ,11 فمحمله على ظهره ذاهاً ره 4 حى بوصلة الى مكانه ه ولام
5 0 00 اللك 6 0 0 القس بن أوس | احد ܐܝ آل
3 ` 0390
6 303 تركرا منازلهم وبعد اباد
اهل 5 5 _ والقصر ذى الشرفات من سثداد
9959 تلاق ايعان 50 00000
الذي يناه السِنِمّار. وقيل له سددير لانه كان في داخله ثلاث قبب فان ܕܨ باللفة
المهاوة معناها القيّة 9 في مادة ` ± على وزن ܕܫܐ اسم 5 ردي
بفى 304 
#### chunk 88
00
الس ملك 0 كن ها قصران ܠܐܫܐ السداعة أحدههما كان 2 689
وفيه كانت 0 ܣ 572 من خورن اي 1[ كل ومن < 3
ل 01 وكان يحوي ثلاث قرس متداخلة بعضها ببعض كان النعان بترم
فيها فرائض دينه >
١السيدارة)‏ 2:7 المقئعة والعصابة معرب ستاره ومعناها 5.058
6 95 ان 0( ابكلية 9 0 ܣܬܪܐ
( امدق والسلرة2) تعر وب 3 ܨ 00 الوقود المشهورة عند الفرس 201
0 ين ين كان ܫܝ ÷ ܒܝ تسحون وان نا
من العليود واميوانات فيد بطون على أرجل كل منها حزمة من حشيش ثم يطلقومسا
بعد ان ܥ | قد وضعوا على احلزمة صوفانة او حي 0 ܢ معأ ܒܝ
6 0555( باضظرات عق وجة 35 799[ أن
الداعى الى تسمية تلك الليلة بالسدّق ( 359 7 صد ومعناه الماثة ` للندسة )
001 كان له م
#### chunk 89
لكر ).لد
(السدِلّ) هو كثلثة بيوت في 7 45 » من سه اي ثلاثة
ومن دل اي وسط اومن دير اي القبّة ٠‏ او هو ` 3 0
السداي والسد اف 6 لنت شارف عت رمات ل 11
ورانحته ججملته مكروهة تعريس © ومنة التريى سدّاف
(السادّج) معرب 5 وهو ما لا نقش فيه ٠‏ وهنة السذّج عند الولّدين للسيط
اسن الاق لسهله والسذاجة : 0 والسهولة
(السَودَنيق) فسره البعض - 53 0 5 لغات منها 095
والسودّق 4 6 £ ` 15: والسدنوق والسوذ يق 532
والسذقان والسودارئق لوول اوالشوذائق .قال الموهري ديع ذلك فارسي
معرب٠‏ 0 8 ]1 فشر بير الع الاو يتقف الشحر عنقاره ويقال
4 0 = ( | ܬܐ( اله اطع ) ٠‏ والظاهر 3 اصل 27 لس فارسا واعلّها
200 عن اليونالي ܙ ܙ ,23ج و ܝܫܝ
```


## [2026-09-07T18:23:21.684Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('AFM_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'رونق' in p or 'روناق' in p or 'رونك' in p:\n        print('### chunk',i)\n        for ln in p.split('\\n'):\n            if 'رونق' in ln or 'روناق' in ln or 'رونك' in ln: print('   >>',ln)\nEOF\necho \"=== chunk 72-78 heads\"\npython3 - <<'EOF'\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(70,79):\n    print('#### chunk',i); print(pages[i][:500])\nEOF",
 "description": "Search AFM for rownaq variants"
}
```


### [2026-09-07T18:23:23.019Z] TOOL RESULT

```
### chunk 117
   >> ܡ ܐܠ والترونق وايرئاق ܐ ܢ‎ 1
### chunk 153
   >> ( النرْق) اليد ( شفاء الغذيل ) ٠‏ معرب نزخ وهعناه السعد والرونق
### chunk 169
   >> درونك ܟ
### chunk 174
   >> فدرونك لا وو ܕ ܙ ܙ ܙ
=== chunk 72-78 heads
#### chunk 70
ܚܐ 4 ܝܝ
اد بعون 3505 ± الثالي
* (الدوكة ) الشر والخصومة 10205 عدن الخطر الأر 0 ا
ومما ܨ
* (الدولة ) الداهية وهي لغة في 15 عن اطوهري بال جاء | الدهر ¥ ته
وتولاته اي بدواهيه تعر بب دوله ومعناهما لكر وان ܐܨ الذي تتنشاءم به
العامة قائلة انه عبارة عن الداهية والموت فأطلق `
(الداماً ) 0 قبل ® والاصح 5 5
+ (الديك) 3 بالاثافي ܙ ܐܝܐ ععنى ديك افاسي وهو القدر
عد (الد رين والديانة » المعتقد والمذهم خرن 3 ن الفارسي 50 المعتقد
ويطلق ايضاً على ملاك كان موكلا على حافظظة العالم: وعلى اليوم الرابع والعشر.ين من
كل
#### chunk 71
اه
ܐ ® صمغ الصنو بر 5 لغة فيه ٠‏ وهو داتبانج الفارسية ٠‏ قال في
البرهان 0 اطع : « راتيانج على وزن ܝ ع8 الصنو بر وهو مثل سائر الصموغ 50
9 وهر م ذلك 0 10 © زفت برطت ٠واما‏ يكون صلم
فنسكى حبائل «رحته» ܝ يعمد بالطبخ فية شال له 0 20030 ) باليونانة وحام
1 في شيراز 3 والظاهر 5 اصل الكلمة يونالي
83 ܐܐܝ مطلقاً وهو مشتق من :0 سال :
( ܙ( ] نج ) الأنسون وقيل هو الشمرة وهو الأصح لان الاطاء في كتب
الفردات يذحكرون الأ نيسون في حرف الهمزة ثم يذكون الرازيانج في حرف اراء
ويد ون لكل ]ܐ اع ري ܐ ܒ
راز يأ نه وقال في 
#### chunk 72
سند لو ”ا ܵܣ
علاوة 2 رماس ومنه السريالى. ܪܝܒܣܐ والكردي رياس
0 ( ܕ ܝܡܝ ) الرجل التافه اي اللقير ينطق في امر العامة وهو غير اهل
3[ ` 7 وتكن الأرجم اله تغريت 9 ܣ اأزحه
المقاوب
* (الإرريآن) فير ات 6 1530 ܐܢܐ ܚܨ اربيان وهو جراد
اللعراقيل لات راك 5 صدفي ܐܬ الى النصف وفي كلا طرفيه عشر ارجل
ܚܬ بارجل ܐܝܢܝ £ راسه قرنان ̄ أن 1 ܝ ܚܝ 09 ܐܚܨ
60 دو الي اناعم (10:0111611± 7201561 : عتم قط )
0 فارسي حض وهو !ܟ
# ` بعنى قطعة من ن قطع ع الطائر ا معروف 5 وك
% ]) ܝܨ ٠‏ ترك والاسم متشا 0 هخ رض وغ
٠ . 1‏ ܕܨ اش
99 9
+ (
#### chunk 73
لالط 77 ܓ
¥ (الرِزق) تعر يبب روزي وما يمعنى واصل. روزى نسبة الى روز وهو النهار.
وقالت فيه العرب رزق وارتزق الى غير ذلك
(الرازق ) السب املاحي 390 6 ( والخمر:
ܝܚܪ من رازى وهو لتو 0( ܒ ( راجع ܫܝܐ 1 >( ٠ورازقي‏
بالفارسيّة يطاق ايضاً على العنب الملاحي ܕܟ وقال في البرهان القاطع :« زتموا ان
ܣܨ ܝ سم احده 09 00 الاننو راز 930 هذه المدئة (اى ܘܙ 4 الري ٠)»‏ ولا
مت اراد كل” منها 0 ܓ ܨ بأسمه 3 من جراء ذلك 2 ܚܠ ܙܠ ܝ ٠فاشّار‏
اليهها احد |( ْ ܣܨ 11 ܐܝ ܐܢ )| ܙܠ ܧ 3 ܐ الاخر. ند
ܣܣ 93 ثما رازيين >
( الروزنة ) تعري
#### chunk 74
3 ܣ
* (الرشك» اكبيد اللحية معرب من ريشكاو: اي بليسة الثور 9 علل
الرجل الاحمى
(الشغك) فادسق ححض وقو العقرب
04:02 39
( § القام الاول ٠‏ هن الانفام تعريب رانست ومعناه المستقي الموافق
+ د 0 معرب عن 7 الذي ܝ
ܟ ܨ ) ¥ 3 مغرت ܐܘܐ عن رت اي العريان ام عن رت أي الفقير
١الرطل‏ ) ® عشرة 5 اوقة ܘܐܒ ܡ وهو نصف المن النبريزى واللن التبديزي
1 109 ارخا ® على وعاء يوضع فيه الشراب :ونحوه فهر ܫܐ
باليونائّة ܚܝܫ 7 2 ® ٠‏ لست ادري هل اصله يوناني ام فاسي ܨ
(اأطل)» 12 0 ܟ واتكبير 0 0:30 تهون عن لاز
وهو ْيطلق على ما عتق من
#### chunk 75
و شرب ܛ النردين وهو ܝܐ الرومى. اليه عن ܐܐܐܠ 002200 او )280 ومنه
)ܛ 1 وهو بالارامسة ܢܪܕܐ وبا ® دب وناردا )` ® القدعة
والظاهر ان اصل الكلمة سانسكريتىق 221202 ومعناه « 50035 (القاموس
ܐܚܐܢ تاليف جيسيديوس)
* (الرانف ° 3 5 رَ نف . قال في 1 القاطع :
« ر نف على وزن انف كاه البهرامج وهو « مدمشك »> ويقال له بالتركة « سلطالى
٠ 4 0 /‏ ܘ 3( ܀܀ .‫ . ܀ ܨ 7
سكوت » زهره يظهر قبل ورقه وهو قدر البلوط اصفر احمر اسود ابيض 2" الرانحة
كثيرًا ويقال 4 بالتركة « ووقار كو ܣ 6 ولس هو « سورقون » 4| توم
النعض ¢
( الرَام ) ال
#### chunk 76
بق اي
ذر را 0 ١‏ ريس ليوا موت ونم وهو منسرب الى بر `
(1710153) الذي كان اسم القديم :#م؛ فانة من سواحله كان يستخربج الراوند ومن
8" اليو في ومن >00:00م:34] مركت ب < الراوند في اللغات !ܕܙ ܢ ܕ % وهو - 111
1811110 بالرومسة و 1001316310 بالايطا ® 0 بالفرنسة
0 00:07 ( ܠܐ س الاين وهو فارسي ܥܨ ܕܘܫܐܘ ه !ܐܐܐܝ
(الروزنامة » 6 من روز اي يوم ومن نامه اي كتاب
, 7 ( قير بالرجل يقال انه « رَوْس سو » اي رجل سو وهو معرب عن
9( 30900
+ (الروضة ) من الرمل والعشب مستتقع الا تكو النضنت مز القز به 11
وفي الكلمات الروضة ®
#### chunk 77
21
1
(الزنيق) سيال معدني معروف معرب ܨܘ ومنة السريائي ܙܢܒܓ
+ م000 كار مأخوذ من با تر ومعناه أجل ܐ
+ (الزبرجح) الزينة من سي او ܨܚ ܕܐܝܬܝ والسحاب الرقيق فبه ¬
00 من سأ اى ع تين وي للد اي 1 أى اصلة عنعن ود 2
عنْ 7 7 1 ܒ الوجه
3:3 جنوال زوج 99 975 135
* 5 ܝ او صفرةٍ مأخوذ من زراب ومعثاه ماء الذهب او
101
2 زتموا انها اسم شيطان او رئيس ان قل ومنة سد سميت الاإعصار
زو بعة 1 ܒ 0 ام زو بعة ة وأ بو زوبعة زعموا ان فيها 1 81 مستا
( > ܝܐ المحيط  )‏ قا 0401 و #نعودية عن .ارا وشا الشرير وقاطع الطريق او ܨ
زُوباغ و
#### chunk 78
ܚ ܝ =
( "5 5 وهو 973 6 المشتري ܥ 9
فأخوذة ܟ عن ܟ ياف ܙܒܘܢܐ (فرتكل :^ ܙ )
ܨ 501 00000 والانس والشرطي وجمعة 4( 60( في الصحاح:
67 عند العرب 15 ܢܨ بذلك بعض ܠܐ لدفعهم اهل 3 © :
55 القرآن 6 الزبانية 9 الغلاظ الشداد. وقال الاخفش :5 07
بعضهم واحدهم زبالي وقال بعضهم ارين وقال مضي ريه شيل ع ا
والقول الاول اي واحدهم زبافي ܝܟ لان ܐܚܬ ܐܠ ومعناه ܨ وهو
ܘ )3 2950 ܐ <
+ (ازج) تعريب زج وهو نصا ل السهم والخديدة 5 £ ܐܢܐ الرمح ومئة
السريالي ايحم
01 الذهب ال سه 3 تعريب )+ اي زيئة.٠وقالوا‏ فبه
ܥܝ
0 ܗ 21 اللنين واإضارم
```


## [2026-09-07T18:23:37.760Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && pdftoppm -f 77 -l 77 -r 300 -png -singlefile /home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.pdf afm77 && python3 -c \"\nfrom PIL import Image\nim=Image.open('afm77.png'); print(im.size)\n\" ",
 "description": "Render AFM pdf page 77"
}
```


### [2026-09-07T18:23:44.488Z] TOOL RESULT

```
(2913, 4900)
```


## [2026-09-07T18:23:47.282Z] TOOL CALL #40: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/afm77.png"
}
```


### [2026-09-07T18:23:48.158Z] TOOL RESULT

```

```


## [2026-09-07T18:23:48.156Z] INPUT

[Image: original 2913x4900, displayed at 1189x2000. Multiply coordinates by 2.45 to map to original image.]


## [2026-09-07T18:23:57.689Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && pdftoppm -f 76 -l 76 -r 300 -png -singlefile /home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.pdf afm76",
 "description": "Render AFM printed p74"
}
```


### [2026-09-07T18:24:06.609Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-07T18:24:09.794Z] TOOL CALL #42: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/afm76.png"
}
```


### [2026-09-07T18:24:10.746Z] TOOL RESULT

```

```


## [2026-09-07T18:24:10.744Z] INPUT

[Image: original 2913x4900, displayed at 1189x2000. Multiply coordinates by 2.45 to map to original image.]


## [2026-09-07T18:24:31.564Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON anbiq ctx\"; sed -n '17165,17175p' MON_part1.txt; echo; echo \"=== PLA rawnaq\"; grep -n -i \"rawnaq\\|raunaq\\|rönaq\\|ronaq\" incoming/PLA/PLA_pages.txt | head; echo \"=== HRN nik/new\"; grep -n \"nêk\\|nîk\\|nēk\\|nêv\\|naiba\" HRN.txt | head -20",
 "description": "MON anbiq, PLA rawnaq, Horn nik"
}
```


### [2026-09-07T18:24:31.689Z] TOOL RESULT

```
=== MON anbiq ctx
پیغمبران و خشوران. 
انبیره: (م-)معآطاود ( .) خلاشه و خاشاکی که 
پس از پوشش خانه بر بام اندازند تا بر بای 
آن خاک و گل ریزند و بندایند. 
انبیق: مارا [غ. معر.] (ا.) ظرفی است برای 
تقطیر مایعات و گرفتن عصاره و عرق. 
انتا< : 60۸8 [ع.] (مصل.) فرا رسیدن 
هسنکام زایش چارپایان. نتیجه گرفتن از 
چیزی. (منط.) نتیجه گرفتن از مقدمات 
منطقی؛ - ج. انتاجات. 
انتشاه: ِِ [ع. ۰ (مصل.) آگاه شدن» 

=== PLA rawnaq
=== HRN nik/new
```


## [2026-09-07T18:24:47.478Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN\"; grep -n \"nêk\\|nêv\\|nêkû\\|naib\\|nêkô\" HRN.txt | head -10; echo \"=== HRN nik alt\"; grep -n -i \"nik\\b\" HRN.txt | head -10; echo \"=== HUB\"; grep -n -i \"naiba\\|nêk\\|nêv\\|nēk\" HUB.txt | head -10; echo \"=== IEC\"; grep -n -i \"niteo\\|nitere\\|nei-\\|noibho\" IEC.txt | head -10",
 "description": "Horn, Hübschmann, Mann"
}
```


### [2026-09-07T18:24:47.557Z] TOOL RESULT

```
=== HRN
14233:naibtt' 1068.
=== HRN nik alt
1002:bei. ädenk, n. adm, üzma ^Spiegel' (10); kurd. nainik;
1172:stT' in stinik (vd. 5 (38), aw. ereöwa-) ^b^%stm 'aufrecht
1181:490). Die Lesung stenik, sten scheint Bartholomae nach brieflicher
1491:bücher: änikj enik) vermag ich im Neupersischen nicht
1623:ermänik^ ermämh (Aw.-Komm.); ai. aryamän- 'Busen-
2045:phlv. apuxscLt/(i)snik (Men.).
2642:ir. I 57); phlv. venik (Bund., AV.), bEmk (AV.).
3727:kurd. tenik; oss. f(wäg (248); bei. tanak, n. fana/,
5798:zarmxj syr. talm. yy)*) 'Arsenik'; zerJr, zifir 'gelbes
7573:aw. kanyä-^ kaini7i-, kainikä- 'Jungfrau, Mädchen';
=== HUB
5966:(vgl. nek *gut, schon* = phi. nevak, ap. naiba-),
6006:-ewa- zu 5 in nek gut, seh5n* = phi. nevak, ap. naiba-
6406:nBk)j ap. naiwa-, geschrieben naiba- *sch5n ; girav, girau
6440:NSvsahpuhr, np. NesapUr (Stadt), zu ap. naiba- (Tab. 59).
8781:schOn = phi. nSvak, ap. naiba- ; bak Turcht' = *bhayaka- ?
=== IEC
11581:nei- "down Cf. ni-, neiu- Gk. neí-atos ‘lowest’; neíara, adv. "lower; nei-óthen ‘from below’; nei-óthi “down below’; formant in OCS niže (‘below’, and com. Sl.); nici ‘face downward’; and in Slo- vene ni-Cati, inf. ‘crouch’; ni-hati, inf. ‘dangle’; z-gde in Skt. Av. ni- ‘down’; Oss. ní, ni, id.
11593:neido (1), (ninid-) “put down, belittle’. Cf. nei-, ni- Skt. cf. nindami, 3pl. pf. ninidüs “blame, mock’; Gk. (uncertainly) cf. ón-eidos, n. (re- proach’, if not for *uon-ueid-); Li. cf. niedu, eti, v. ‘despise, hate?
11596:nei-quis, -quid “nobody, nothing; trifle, tri- vial person, scamp'. Var: -quos. Cf. quis, quid, quos, quod & ne-, nei-, ne-quis, etc. Oss. cf. (for the formation) níkw “never; no- where’; OCS nikyj ‘no, none’ ničí ‘nothing’; Li. niðkas ‘nobody; bad, wretched; scamp’; niekis, gs: -io, m. ‘trifle’; Latv. nieks ‘nothing; scamp’
11597:neiu- ‘down; low, base; lowland, lowness’. Cf. nei- Gk. ambig. Gk. (ambig.) neí-atos ‘lowest; nei-óthen, -óthi ‘from below; below’; cf. nei-; Go. (am- big.) *neiwan, sv. 1. (resent, perh. fr. *nei- quo); OE cf. (z-gde) neowol (“headlong; down, deep’, fr. *niuol-); Hom. neiós, f. (field, fallow’. Ambig. cf. nei-); OCS niva ‘field’; Cz. cf. nivec, Slovak nivoč ‘nothingness’; Latv. nieva ‘contempt’
11606:nekstos (nektos), variants of type neksos (1) above. Cf. neKs- Lat. cf. necto, Ere, pf. nexi, sup. nexum “join; knit; spin; frame’; W nais, pl. neisiau, m. (band, De fr. *nektios) beside naith, pl. nei- thion m. ((2) *betrothal, fr. *nektis); OE cf. nestan, v. (^spin'. Phonol. uncertain); ON nist, nisti, n. "brooch, pin’; cf. G Nistel, f. "band. age, belt, shoestring'. (For the variant Nestel, Du. nestel, see nast-. W ambig.)
11651:néquis (néquoios); néquid (anybody, no- body; anything, nothing. Cf. nequos & quis, quid, quod Skt. (Vedic) nákis ‘nobody; not, never’; Av. cf. naecis ‘nobody’; Oss. cf. nići, Dig. neke ‘nobody’; nici, Dig. neci ‘nothing’ (fr. nei-?); Lat. (ut) nequis; Umb. ne. . .phim (sic: acc. sg.); OCS cf. nékyj ‘somebody’; adj. "a cer- tain. . ?; něčij, prn. (someone's, and com. SI.)
11747:nl ‘down’, see nei-. With short vowel in Skt. ni, Av. ni-; Oss. ní, ni; with long vowel cf. OCS niz-, cpds. ‘down’; and Li. ny-rinti, inf. *cast down the eyes'
11808:noit- (nit-) (1) “inflame, kindle; be inflamed, burn brightly”. Lat. niteo, ere, v. ‘shine’; cf. nitidus, adj. ‘bright’; o-gde in OCz. nietiti, Pol. niecic, Slovene netiti, inf. (inflame, kindle’. Not re- lated to the OCS type gnétiti ‘inflame, arouse’)
15035:saul-, sáuel- ‘sun’. WP II, 446. (Indo-Iran. variant: sül-) Skt. cf. (z-gde) sürab, m. id.; Av. cf. hüro, gs. of hvaro, id.; Oss. cf. xur, Dig. xor, id.; Kurd. awer id. (and 'east); Scyth. (king's name) Saulius; Gk. helios, heélios, aélios (sic), id.; Lat. sol, cons. decl. m. id.; MIr. sól, id.; Gaul. sul- (in a name); W haul, pl. heu- liau, m., Br. héol, m. id.; Vannic dial. hiaol, m. id.; Cor. howl, m. id.; Go. sauil, n., OE Sol, n., Sw. sol, m. id.; ON sól, f. ‘sun, day”; Li. saulē, Latv. saule, f. id. (OCS slüníce n. ‘sun’ appears to be a cpd., cf. the Skt. variant sül- (*sul-) and (root of) Lat. nitere, nitidus?). Verbal types: Gk. héliázo, hélióo; Lat. solo, are, in-^; Icel. sóla, v. (a-stem); Sw. sola, v.; W heulo, inf.; Latv. saulot, inf.
```


## [2026-09-07T18:24:49.452Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LEW niteo\"; grep -n -i \"niteo\\|niteō\\|nitidus\" LEW_1910.txt | head -8; echo \"=== LAT\"; grep -n -i \"niteo\\|nitidus\" LAT.txt | head -8; echo \"=== SNS nev\"; grep -n -i \"nēv\\|new\\b\\|nyw\" SNS_pages.txt | head -10; echo \"=== SPG naiba\"; grep -n -i \"naiba\\|naiba-\" SPG_keilinschriften1881.txt | head -10",
 "description": "Latin dicts, SNS, Spiegel"
}
```


### [2026-09-07T18:24:49.553Z] TOOL RESULT

```
=== LEW niteo
=== LAT
36918:l'indique, sana preuve, M.L. s.u. nitidus, 5y3y.
41542:niteO, -es, -ul, -ere: briller, etre luisant, ^elatant. Se dit
41548:nitidus (fr. net), M.L.5999; nitiditas (Acc.); nitidiusculus (Pl.),
41552:(deja dans Enn.), Sni tSscd, d'ou eniteo', inter-, per-, prae-, re-
41556:dh); niteo serait bati sur un adjectif *nitos, comme fateor-, sur le
53238:*nldeo. Le sens fait penser a niteo (avec 1), q.u.
=== SNS nev
505:                    Etymologie. Strassburg 1893 new ed.,         Nt
512:                                                                                        Strassburg. 1904 new ed., Berlin 1961.
549:                                                                                        Heidelberg 1912. new ed., Leipzig, 1955.
785:        1964                                                                                                      burg 1904 new ed.., Berlin 1961.
821:                      BSOS. XII, 1948.                                                                            1892-93 new ed., 1960.
860: Modi, j.j.:   The Religi OUB Ceremonies                                       Strassburg 1893. new ed., 1974 (GNPE)
870:                                                                                     1897    new ed., Germany 1962. (Arm. Gram).
871:         East. V new ed., India 1965.
887:Pagliaro, A.:   Prof Jackson Memorial Volume,                                  berg 1912 new ed., Leipzig 1955.
11516:Ctfir.tfan.       nyk,     nyW^*                AiW>.1035)naiba-             :**
=== SPG naiba
2183:13. adam. ak'unavam. vasiy. aniyasbciy. naibam.
2186:16. rtam. vainataiy. naibam. ava. visam. vasbnä. A
2468:20. naibam. ak'unaush. utä. ima. st
4051:treten. — Sehr schwierig ist l. 15 tyapatiy kartam vainataiy naibam.
4815:gaubatiy « J^y ; naibaka «= neup. ^ju.
7061:acc. sg. naibam D, 13. 16. K, 20, Oppert vergleicht passend neup. ^ju
```


## [2026-09-07T18:25:10.605Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ndef leafof(fn, lineno):\n    t=open(fn,encoding='utf-8',errors='replace').read().split('\\n')\n    txt='\\n'.join(t[:lineno])\n    return txt.count('\\f')\nprint('SNS line 11516 leaf', leafof('SNS_pages.txt',11516))\nprint('SPG line 7061 leaf', leafof('SPG_keilinschriften1881.txt',7061))\nprint('SPG line 4815 leaf', leafof('SPG_keilinschriften1881.txt',4815))\nprint('HRN line 14233 leaf', leafof('HRN.txt',14233))\nEOF\necho \"=== SNS ctx\"; sed -n '11500,11530p' SNS_pages.txt",
 "description": "Find leaf numbers"
}
```


### [2026-09-07T18:25:11.966Z] TOOL RESULT

```
SNS line 11516 leaf 163
SPG line 7061 leaf 198
SPG line 4815 leaf 140
HRN line 14233 leaf 344
=== SNS ctx
                                                                     ifjsl^tfc^l              jc^»:MP5t*«JMj*j                               ^b^b^ f w-SjI
                                                                                                                                      r'lA*    •—«*li o.L *jl3
                                Lc^Uhbo'j                                                                                                                                                       Tlo
u
                                                       .L(W :venag:          ***X\                                                                                ro/iv^ .y-^i/TJ

ryn      :jjH (GNPE. 59)       vainShiy:^ vaSnami                  :   fa.
                                                                             ^         , U.i     "U^l, (^ ^tfU^T.^4 v bT) x^ mirang:
    (Mir. Man.   Ill, 64) wyn               :   A    tttf*.*».IXf 52)
                                                                 If/**5
                                                                                                                                                                                               ^*l


                                                                                       :         a«j<3m            :       T c-j j jbi^ , ^Sw^tp
                                                                                                                                                              :Neryosang:                a*?o^s|

Ctfir.tfan.       nyk,     nyW^*                AiW>.1035)naiba-             :**
                                                                                           .   l^-I **#
                                                                                                           iftaj   ^             ij^ } J, .^u b
                                                                                                                                      \

                                                                                                                                             f                .   ^1 Neryosang:

't .J    ^V ^.6/^-^^>tf^^ nJk                              :
                                                               ^   "'        61)                                                                                                   •\X/A^


                                                                                                                                                        —J- «^x*i f*i:nem:
                                                                                                                                                                         .                       *»
                                                                                           nym         :   A{AiWb.               1036')       nfena-wSj^na&na-                       :    t-
                                                                                                   •   A-M*^^ lAjt/tH* -6/lf*5                          LMiff.Man,!!!, 59)
```


## [2026-09-07T18:25:29.408Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"naiba\" POK_01.txt POK_02.txt POK_03.txt | head -10; echo \"=== search nei- german\"; grep -n \"bewegt sein, erregt sein\" POK_0*.txt | head",
 "description": "Find Pokorny German original nei-2"
}
```


### [2026-09-07T18:25:29.461Z] TOOL RESULT

```
POK_02.txt:6665:Lat.  niteö,  -ere  ,glänze,  strahle',  nitidus  , glänzend',  nitor  ,  Glanz'  (von einem  Partiz.  *ni-tö-) ;  vielleicht  re-nldeö  , erglänzen'  (mit  präsensbildendem -d(hy)]  *nei-bhO'  in  mir.  nlab  , Lebenskraft',  cymr.  nwyf  ds. ;  noi-bho- in  apers.  naiba-,  npers.  new  , schön,  gut',  air.  nolh  , heilig';  *nei-mä  in mir.  nlam  , Glanz,  Schönheit';  *nei-Jco-  in  mir.  mach  m.  ,Held',  nlachus m., Tapferkeit';  *nei-to-  in  cjmr.  nwyd  , Leidenschaft',  hispan.  Kriegs- gott Netö]  air.  PN  Nlall  (Gen.  NeiU)  aus  *neit-s-lo-s]  steckt  vielleicht auch  in  air.  ma  ,Held'  (s.  1.  nei-)]  germ.  ^nipa-  in  got.  neip  n.  ,Neid', ags.  m(J  m.  , Kampf,  Haß,  Feindschaft',  as.  afries.  nith  , Eifer,  Haß,  Neid\ aisl.  nid  ,Hohn,  Schmach';  könnten  auch  zu  air.  nlth.  n.  (idg.  *i2ifu-) ,Kampf  gehören;  zweifelhaft  ai.  nila-  , schwarzblau',  nayanä-  r\.  f.  ,Auge', netra-  n.  ds.
=== search nei- german
```


## [2026-09-07T18:25:33.365Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '6650,6680p' POK_02.txt",
 "description": "Print Pokorny p760 context"
}
```


### [2026-09-07T18:25:33.400Z] TOOL RESULT

```
Gr.  didiyL7]  {*nd-ikä) ;  ahd.  nazza,  aisl.  nqtr,  ahd.  nezzila  (germ.  *natilön), ags.  netele]  daneben  mit  idg.  -t-  (also  *n9-t-,  nö-t-  als  ^Erw.  zur  vermut- lichen Wurzel  (s)ne-)  apr.  noatis,  lit.  notere,  notre  , Nessel',  nötryne  ,Taub- nesseP,  lett.  ndtrCj  nätra  ,Nessel',  slav.  *nat'b  , Krautblätter'  in  slov.  nät (Gen.  nati),  poln.  nac  ds.  und  allenfalls  (als  redupl.  urkelt.  *ni-nati-?) mir.  nenaid,  nir.  neantög  ,Nessel',  dissimil.  bret.  linad  ds. '  WP.II  328  f.,  WH.n  144  f.,  155  f.,  172  f.,  Trautmann  194,  H.  Jacobsohn Arier  u.  Ugrofinnen  90 f.;  s.  unter  (s)we-.
2.  ned-  ,tönen,  brüllen,  rauschen'.
Ai.  nddati  ,tönt,  brüllt,  rauscht',  nada-  m.  ,Brüller,  Stier,  Fluß*,  nadi- f.  ,Fluß,  Flut',  nadl-na- m.,  nadl-sa-  m.  ,Meer',  usw.;  av.  wacZ- , schmähen'; gr.  (illyr.)  FIN  Neda  (Arkad.),  Nedwv  (Messen.);  thrak.  FIN  NeOTog] illjr.  FIN  Nearog  (Dalm.)  aus  *ned-to-.
A.  Mayer  Mel.  Boisacq  II  132  f.,  Krabe  IF.  58,  209  ff.
nedo-  ,Schilf'?
Ai.  nada-  m.  vermutlich  , Schilfrohr',  npers.  nai,  dial.  nad  , Schilf;  arm. net    ,Pfeil';   lit.    nendre   (und    Undre)   ,Schilfrohr'   (mit  Nasal   nach    lenkti ,biegen'?);    lett.  nasli  , Schilf  aus  *nadslis? WP.  II  329 ;  vgl.  Kuiper,  Proto-Munda  82.
760  •
negh-  , durchbohren,  stechen'.
Mir.  ness  , Wunde'  {*negh-8-)]  reduktionsstufig  aksl.  v^-nhzq  , steck hinein',  Infin.  v^-nhzngt^,  Kaus.  russ.-ksl.  v^-noziti  , hineinstechen'-  aksl nozh  , Messer';  ob  hierher  ai.  dhsu-  , Stange'  (*ngh-su-)?
WP,  II  326  f.,  Trautmann  200.
1.  nei-,  neio-ini-  , führen'.
Ai.  ndyati  (Partiz.  nltd-),  av.  nayeiti  , führt',  mpers.  nltan  , führen treiben',  ai.  nlthä  f.  , Führung,  Weg',  nltho,  netä^  ,Führer',  nitar-,  netdr- m.  ds.,  netrd-  n.  , Führung,  Auge';  mir.  ns,  nla  ,Krieger,  Held'  {*neit-i\ Gen.  Sg.  urir.  netas,  air.  niatJi  {*nei-t-os\  s.  auch  2.  nei-)]  hitt.  näi-,  lenken führen'.
WP.  II  321,  Pedersen  Hitt.  §  77  f.,  81,  Frisk  Suffixales  -th-  öf.
2.  nei-,  neis-  :  ni-  , lebhaft   bewegt   sein,    erregt   sein,   glänzen';    noi-bho-^
,gut,  heilig';  kelto-germ.  nei-to-,  ni-tu-  , Leidenschaft'.
Lat.  niteö,  -ere  ,glänze,  strahle',  nitidus  , glänzend',  nitor  ,  Glanz'  (von einem  Partiz.  *ni-tö-) ;  vielleicht  re-nldeö  , erglänzen'  (mit  präsensbildendem -d(hy)]  *nei-bhO'  in  mir.  nlab  , Lebenskraft',  cymr.  nwyf  ds. ;  noi-bho- in  apers.  naiba-,  npers.  new  , schön,  gut',  air.  nolh  , heilig';  *nei-mä  in mir.  nlam  , Glanz,  Schönheit';  *nei-Jco-  in  mir.  mach  m.  ,Held',  nlachus m., Tapferkeit';  *nei-to-  in  cjmr.  nwyd  , Leidenschaft',  hispan.  Kriegs- gott Netö]  air.  PN  Nlall  (Gen.  NeiU)  aus  *neit-s-lo-s]  steckt  vielleicht auch  in  air.  ma  ,Held'  (s.  1.  nei-)]  germ.  ^nipa-  in  got.  neip  n.  ,Neid', ags.  m(J  m.  , Kampf,  Haß,  Feindschaft',  as.  afries.  nith  , Eifer,  Haß,  Neid\ aisl.  nid  ,Hohn,  Schmach';  könnten  auch  zu  air.  nlth.  n.  (idg.  *i2ifu-) ,Kampf  gehören;  zweifelhaft  ai.  nila-  , schwarzblau',  nayanä-  r\.  f.  ,Auge', netra-  n.  ds.
WP.  II  321,  336,  WH.  II  168,  171,  Vendryes  RC.  46,  265  ff.
3.  nei-,  ni-  s.  oben  S.  312  f.
I.  neid-  ,heruntermachen,  schmähen'.
Ai.  nindati,  Pass.  nidyd-te  , schmähen,  tadeln,  verachten',  dnedya-  ,nicht zu  schmähen',  nid-,  nidä,  nidä,  nindä  , Schmähung,  Tadel,  Verachtung'; av.  naed-  (näisml)  ,schmähen';  arm.  anicanem,  Aor.  3.  Sg.  anec  ,fluche' (*oneid-s-et) ;
gr.  ^vsLÖog  , Vorwurf,  Schmach',  dvsiöi^a)  , schmähe'  (o-Präfix  ,be-schimpfe', wie  auch  arm.  anicanem) ;  got.  ga-naitjan  , schmähen',  naiteins  , Lästerung', ■  ahd.  neizzen  , quälen,  plagen',  ags.  ncetan  ds.;  lit.  niedeti,  lett.  nist  ,ver- achten',  naids,  naidus  ,Haß,  Feindschaft'.
WP.  II  322  f.,  Kuiper  Nasalpräs.  130,  Trautmann  193;  wohl  zu  nei- S.  312f.
r
761
ueid-  '  n^d-  ^fließen,  strömen',  FIN  Neidä,  Nidä.
^i.    nedati  ,  flließt,    strömt';    gall.    FIN   Nida   ,Nidda'    und   ,Nied',    brit. pi^  Nida,  cymr.  Nedd  ,Neatli' ;  vollstufig  poln.  FIN  Nida,  lit.  FIN  Niedä, apr.  FIN  Nyda  ,Neide'. J.  Löwenthal  ZONF.  6,  81,  Krähe  BzNF.   1,  248ff.
aeig^-  ^waschen';  Pass.  Partiz.  nig'A-to-.
Ai.  nBnekti  , wäscht,  reinigt',  Aor.  anäiksU,  Pass.  nijyate,  Partiz.  niktd-, ninikta  Imper.  , waschet',  Kaus.  nejdyati-,  Aor.  naBnizaiti  Intens.  , wäscht ab,  spült  weg';  gr.  vit,o}  (*nig'^iö  =  ir.  nigim)  ,wasche',  Fut.  vlipw,  Aor. l^/ii//«,  viTtTQOv  ,Waschwasser',  x^Q-^'^yj  ds.,  ä-viTizog  ,ungewaschen'  (=  ai. niUd-,  ir.  necht)]  gr.  äviyqög  .^äy-ad-aq-coc,^^  ]  lat.  noegeum  (^noigV:-io-)  ,Schweiß- tuch^;
air.  nigid  , wäscht'  {'^nig^ieti,  Verlust  der  Labialisierung  vor  x),  Fut. -ninus  =  ai.  (Gramm.)  niniksati-,  necht  ,rein';  mcymr.  enneint  ,Bad' (*an-nig-antio-]  das  g  aus  dem  Präs.  übertragen);
germ.  *nikwe8^  -us-  in  aisl.  nykr  (Gen.  nyks)  , Wassergeist,  Flußpferd', ags.  nicor  ,Wasseruntier,  Krokodil',  ahd.  nihhus,  nichus  , Flußuntier, I  Wassergeist',  nhd.  Nix,  ahd.  nichussa  , weiblicher  Wassergeist,  Nixe', mndl.  nicker,  mnd.  necker  , Wassergeist'.
WP.  II  322,  Thurneysen  Gr.  115;  anders  Vendryes  RC.  47,  442  ff.
```


## [2026-09-07T18:25:43.918Z] TOOL CALL #49: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-07T18:25:43.925Z] TOOL RESULT

```


```


## [2026-09-07T18:25:46.088Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"naiba\\|noibho\\|noi-bho\" incoming/WLD/WLD_Bd2_pages.txt | head -10; echo \"=== WLD niteo\"; grep -n \"nite\" incoming/WLD/WLD_Bd2_pages.txt | head -10",
 "description": "Grep Walde-Pokorny Bd2"
}
```


### [2026-09-07T18:25:46.143Z] TOOL RESULT

```
21225:*noi-hho- in ap. naiba-, np. new „schon, gut“, air. noib „heilig“ (Liden
=== WLD niteo
501:Keutrum eines Adj. "^pE-ni-s „beschMigt, mangelhaft"), paenitet „es rent,
7746:mengl. pniten „schlagen,                stofien,      'wegstecken“ (engl. ptif) usw., yrozu                        aisl.
12981:   Mit der Bed. von as. brustian (s. o.) und lat. fnitex,, mhd. brie’^en (s. u.
15246:(z B. Yanitek 200) mit mdnus .jgut‘* zusammengebracht werden, immCmis
16282:vereinbar,        vgl.   lett.   rnitel   ,,verandern, unterlassen",       refl.   „aufhoren, nach-
21215:    Lat. niteo, -rre ,,glanzen“, yiitidiis „glanzend, fettglanzend, fett; von wohl-
21216:gepflegtem Aussehen^', nitor „Glanz, Glatte“ {niteo auf Grund eines Ptc.
25697:   Ahd, Uso Adv. „sensim, pedetentim, leniter“, mhd. Adj. und Adv. llse^ nhd.
30259:Samnium      osls., Safinim; lat. Samnites (der von Schulze Eigenn. 478f.,
43055:steam „See8chwalbe“, apr. starnite ^Mowe^^ (gebessert aus iiberliefertem
```


## [2026-09-07T18:25:51.041Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '21205,21235p' incoming/WLD/WLD_Bd2_pages.txt; echo \"=== page tags near\"; awk 'NR>=21150 && NR<=21240 && /\\[pdf page|^ *3[23][0-9] *$/' incoming/WLD/WLD_Bd2_pages.txt | head",
 "description": "Print WLD nei entry"
}
```


### [2026-09-07T18:25:52.256Z] TOOL RESULT

```
       Ai. ndyati (Ptc. nitd-),                  av. nayeiti „fuhrt‘',         mp. nitan „fuhren, treiben'%
ai.     nttar-,        nUctr-     m.     ^Piihrer', neird-            n.   ,,Pubrung,      Auge“       ;
                                                                                                           ein ^nei-t-{s)
„Puhrer,        Heerfuhrer^^ vermutet Pokorny ZfcPh. 10, 405                                        wohl        ricbtig   als
Grundlage von mir. ne, nae^ gen. ogom nHas,                                       air.    math       (archaisch       nHK)
„Held“.
  Gr. dvivy]fii (Hirt IF.                  12,    219 f.)   &,   vielmehr u. na- „helfen'\


2. nei“ ,,gianzen'\
    Lat. niteo, -rre ,,glanzen“, yiitidiis „glanzend, fettglanzend, fett; von wohl-
gepflegtem Aussehen^', nitor „Glanz, Glatte“ {niteo auf Grund eines Ptc.
‘"'ni-to-, wie fateor           remdeo, -ere „erglanzen*^ (eig. ,,herniederglanzen“)
rait praesensbildendem -dih)-:, dazu '^nei-ma in mir. niam „Glanz, glanzen-
der Schmuck“, cymr. mvyf „Lebhaftigkeit'', mir. niamde „glanzend“, cymr.
mvyfiant „Glanz, Ge\valt“ nivyfo „lebendig werden^' (ansfiibrlich Osthoff
IF. 5, 299) mit Formans -hho- (vgl. z. B. doyv-q)og, lit. ral-has „gesprenkelt“)
                   ;


*noi-hho- in ap. naiba-, np. new „schon, gut“, air. noib „heilig“ (Liden
Stud. 59 m.Lit.).
    Hochst fraglich ist hingegen Zugehorigkeit von got. nidva f. „Rosk’
              und ai. nila- ,,dunkelfarbig, schvrarzblau‘^ (Liden aaO.). Uber
letzteres und andere mit ni-. net- anlautende Worte fiir „dunkeb' s. u.
neig- „unreinlich“.


neiq- „herunterraachen, zanken“.
      Gr. veTxog         n.    ..Zank, Streit”,         vsiyJoj ,,zanke, streite, fahre an,                       schelte'*':

=== page tags near
```


## [2026-09-07T18:25:59.867Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('AIN.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('nleaves',len(t))\nfor leaf in (64,65,66):\n    print('#### leaf',leaf)\n    print(t[leaf][:2200])\nEOF",
 "description": "Print Liden pages 59-61"
}
```


### [2026-09-07T18:26:01.067Z] TOOL RESULT

```
nleaves 114
#### leaf 64
STUD. Z. ALTIND. U. VERGL. SPRACHGESCH. 59
thet ämatra-, ebenso amind- VI: 19, i, X: 116, 4; dma-^^N VIII:
12, 24 bezeichnet den Andrang des gewaltigen vajra-Trägers:
nä yäm vivikto rödasT nantäriksäni vajrinam,
ämäd id asya titvise säm öjasah.
Zu dieser Herleitung stimmt auch die älteste Bedeutung von
indriyä-y das von der mächtigen Kraft sowohl des Indra als der
Marut's, der Rbhu's, des Soma gebraucht wird.
Weder die Ableitung des Namens Indra- von der Wz. in-
'eindringen auf ^, noch die Zusammenstellung mit ai. nr- gr.
dv^Q^ kann als besonders glaubhaft gelten.
Ai. nila-. — Apers. naiba-,
Ai. nila- RV etc. 'dunkelfarbig, namentlich schwarzblau,
dunkelblau, blau', nill F. kl. 'Indigopflanze, Indigo', steht inner-
halb des Altind. vereinzelt. Benfev Griech. Wurzellex. II: 57
und BOPP Gloss. comp. 222 verbinden es mit lat. niger, Benfey
aaO. 53 alternativ mit ai. nlra- 'Wasser', gr. vcogoifj. Keine neuere
Deutung ist mir bekannt.
Vorausgesetzt, dass die ursprüngliche Bedeutung '(dunkel)
glänzend' ist, verbindet es sich mit lat. re-ni-d-eo 'strahle zu-
rück, erglänze, schimmere; lächele freundlich oder höhnisch';
7il-t-eo 'blinke, gleisse, glänze; prange, strotze', nitela 'Glanz,
Schimmer', nitidus 'glänzend; üppig; feist'. Dass hierin -öf- und -A
als suffixale Bestandtheile zu fassen sind, lässt sich schon aus
dem Lateinischen selbst schliessen und wird als nothwendig er-
wiesen durch air. niam (aus ^nei-mä-) F. 'Glanz', niamda 'glän-
zend', cymr. nwyf 'pervading dement; vivacity, energy, vigour;
Geilheit', nwyfiaftt 'brightness; vigour'. Die Verwandtschaft der
lat. und kelt. Wörter ist von OSTHOFF IF V: 299 ff. erkannt
und in morphologischer und sonstiger Hinsicht eingehend und
überzeugend begründet.
* BRWb. ; s. die Bemerkungen dagegen von Jacobi KZ, XXXI: 316.
* Jacobi aaO., s. dagegen Johansson aaO. ; vgl. Wackernagel aaO. §§ 16,
157, Bartholom^e IF VII: 54.
Anders Benfey Orient u. Occident I: 49, N., Grassmann Wb. z. Rigv. s. v.
#### leaf 65
6o E. LlDltN
Durch das Lat. und Kelt. ergiebt sich als Wurzel nei-. nt-
glänzen'. Ai. ?n/a- aus idg. *ni-/o- zeigt lange Tiefstufe, die
auch im lat. -nl-d-ere vorliegen kann.
Im Germ, dürfte sich unserer Wurzel das bisher völlig dunkle
got. nidwa Y. 'Rost', wozu nach Falk Arkiv f. nord. filol. V: 1 1 1
vielleicht an. nidfqlr in der V^luspä Str. 50, anzuschliessen ^
Idg. Grundform *m-tuä-; zum Suffixe vgl. got. wahtwö 'Wache',
waurstw 'Werk'; piwadw 'Knechschaft*, /'/'{/Vrf zc/ä 'Liebe' u.a."
Endlich möchte ich hier unterbringen apers. iiaiba- 'schön,
gut*, pehl., npers. nezv, pehl. new-ak npers. nek 'schön, gut* ^,
womit air. noib noeb 'heilig* identisch ist^. Grundbedeutung
wäre etwa 'glänzend, strahlend', wovon sich einerseits die Bed.
'schön, gut', andrerseits die Bed. 'rein, heilig' abzweigte. Die
Grundform idg. "^noi-bko- ist hinsichtlich des Suffixes zu vergleichen
mit lat. albus gr. dX-ifo-c zu ahd. elo 'lohbraun, gelb' ai. arunä-
'röthlich, goldgelb' asl. olovo 'Blei'; — lat. gal-bu-s 'blassgelb'
zu gil-vii-s 'gelb', lit. gel-t-as asl. zlütü 'gelblich', vgl. ae. culufre
'Taube' apreuss. golimban 'blau'^; — lit. rai-ba-s 'gesprenkelt,
graubunt', vgl. rat-na-s 'graubunt gestreift'; — acer-bu-s (: acer)\ —
gr. ägyr-tfio-g 'glänzend' (: ai. ärjuna- 'weiss', gr. äg^vgog); —
ai. sthüla-bhä- ^^- sthülä- u. dgl. m.
Ai. isa und Verwandtes.
Ai. isa F. bezeichnet i. Deichsel, Du. die doppelte, gabel-
förmige Deichsel (RV, AV, Brähm., ep.); nach den Lexicographen
'Deichsel am Pfluge'; isä-danda- 'Deichselstange' (Visnupur.);
^ Nur DiEFENBACH Vcrgl. Wb. d. goth. Spr. II: no giebt ein Paar Deu-
lungsvorschläge, an die er aber selbst nicht glaubt.
'^ Vgl. Kluge Nom. Stammbildungslehre 63, 104, Brugmann Vergl. Gr. II: 1 1 1.
^ HoRN Grundriss d. neupers. Etymol. n:o 1068, Fr. Müller Wiener Zeitschr,
f. d. Kunde d. Morgenl. V: 265.
4 Zimmer KZ XXIV: 210, Fick Wb.* II: 194.
5 Prellwitz Bß XXII: 104.
#### leaf 66
STUD. Z. ALTIND. U. VERGL. SPRACHGESCH. 6l
2. Brett an der Bettstelle (Varäham. Brh.); 3. ein best. Längen-
mass = 88 angula (Qulbasütra) ^.
Man hat es mit av. »//a;//-/^^ dieselbe Deichsel» verglichen'^,
das aber nicht existiert, s. BARTHOLOMiE ZddmGes. XLVIU: 512.
Die verschiedenen Verwendungen von tsd lassen uns ver-
muthen, dass der ursprüngliche Sinn des Wortes etwa »Stange»
war. Jedoch muss auch die speciellere Bedeutung 'Deichsel' in
eine ferne Zeit hinaufgehen; ich vermuthe nämlich Urverwand-
schaft mit nslov., kroat., serb., öech. oje, sorb. vojo, kleinruss.
voje, voje, vyje, vtje, bulg. ojiste (daraus rum. oÜte, alb. oste) 'De-
ichsel, Deichselstange', kroat. oje u pluga 'Pflugstöckchen'; im
Kroat. und Serb, gilt die specielle Bedeutung 'Deichsel am
Ochsenwagen' ^.
Die slavischen Formen gehen auf einen neutralen i-Stamm
(asl. ^'oje für "^ojoy Gen. '^ojese) zurück; vgl. besonders nslov. oje,
Gen. ojesa, wie slovo. Gen. slovesa. Betreffs der Gestaltung des
Stammes besteht zwischen dem ai. is-a und der Grundform des
slav. Wortes, idg. *oies-, wesentlich dieselbe Relation wie z. B.
zwischen ai. äyas- 'Erz' und agall. (und germ.) is-arno- 'Eisen'.
Hier möge an ein gleichbedeutendes finn.-ugr. Wort erinnert
werden: finn., wot. aisa, ehstn. ais, weps. ais ; auch im Mordw.:
ersamordw. azeja, azia, mokschamordw. azia *, überall = 'Stange
der Gabeldeichsel, Femerstange'. Aus dem Finn. hat das Wort
in später Zeit weiter ins Lappische^ und ein Paar seh wed. Mund-
arten in Finnland ^ gedrungen. — Ahlquist De vestfinska sprä-
kens kulturord 115 hält das Wort für genuin finnisch. Dies ist
aber in Anbetracht der Lautähnlichkeit mit dem slav. ojes- (das
* FiCK Wbch* I: 177 zieht auffölliger Weise die Schreibung ifä vor, wel-
che bei einigen Lexicographen vorkommt.
2 S. z. B. Zimmer Altind. Leben 248, Fick aaO.
V
^ MiKLOsiCH EW 220, Zelechovski Ruth. -deutsches Wbch. — Im Russ. und
Pohl, herrscht dafür das deutsche Lehnwort dyslo, bez. dyszel.
* WiEDEMANN Gramm, d. Ersa-mordw. Spr. 1 16, Ahlquist Mokscha-mordw.
Gramm. 150.
^ Norweg.-lapp. aissa 'temo vehicuH', Friis Ordbog over det läpp. Sprog.
^ Pyttis ojsor^ Houtskär eisor PI., Korpo eisel-stang, s. Vendell Saml. af
o
```


## [2026-09-07T18:26:12.010Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"1068\" HRN.txt | head -10",
 "description": "Find Horn no. 1068"
}
```


### [2026-09-07T18:26:12.053Z] TOOL RESULT

```
9221:1068. nek 'schön, gut', nekö, nekt, new 'wacker, Held'
13125:>/eÄ* 1068.
13126:^/^H 1068.
13127:;eÄ:ö 1068.
13133:new 1068.
13339:/7e//äot 348, 1068.
14233:naibtt' 1068.
16467:1068 Anm.
16499:Art' 1068 Anm.
16503:"?«■ 1068.
```


## [2026-09-07T18:26:15.692Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '9215,9240p' HRN.txt; echo \"=== leaf\"; python3 -c \"\nt=open('HRN.txt',encoding='utf-8',errors='replace').read().split('\\n')\nprint('leaf', '\\n'.join(t[:9221]).count('\\f'))\"",
 "description": "Print Horn no 1068"
}
```


### [2026-09-07T18:26:16.999Z] TOOL RESULT

```
päz. nestj nesU,
ap. naiy + asti,
1067. neS 'Spitze, Stachel; Gift (AM. S. 10 Zeile 5 v. u.)',
nester 'Lanzette'.
ai. vergl. neksana- spitzer Stab, Spiess', zu [/'neks-,
niksati 'durchbohren' (Hörn).
1068. nek 'schön, gut', nekö, nekt, new 'wacker, Held'
(Sahn, I, 416 Vers 555, HI, 1106 Vers 707, von einer
Frau).
*) Wenn phlv. n{i)käm^ vd. 7 f 192) Gl , wirklich 'matrice' bedeutet
— was ich bezweifle - so müsstc es nCOgüm gelesen werden, um mit
np. niyäm vereinigt werden zu können (Darm est eter, Et. ir. I, 61,
Note 4).
*) Lies *amyadäciih
«J Reimt auf yekesi (Öähn. I, 42 Vers 144; 170 Vors 750). Auch
in Indien spricht man heute nlst.- 239 —
ap. fiaiha- \schön, gut* ; phlv. neicah, nSwakih, new
(PPÖl.) 0.
1069. nem 'Hälfte, halb*.
aw. naema- *halb* in naemo asm, na^me /saf^ti,
vd. 4, 45, Geld n er, Studien I, 100 [na^mqm im
ZPGl. bedeutet nicht *halb*); skr. nvma- halb*; phlv.
mm, nSmak.
kurd. nTw *Hälfte, vergl. nlwrfiz 'Mittag*; afy. mmai;
bei. vergl. nl^röt^, nSnnöc, n. nermös 'Mittag', mmsap,
n. nSmSaf 'Mitternacht* (269) ; sar. L W. naim.
=== leaf
leaf 259
```


## [2026-09-07T18:26:28.950Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A3%D9%86%D8%A8%D9%8A%D9%82",
 "prompt": "What does this page say about the Arabic word أنبيق (anbīq) — its etymology, source language, meaning? Quote the etymology section verbatim."
}
```


## [2026-09-07T18:26:29.292Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/alembic",
 "prompt": "Quote verbatim the full etymology given for \"alembic\"."
}
```


### [2026-09-07T18:26:32.667Z] TOOL RESULT

```
# Analysis of أنبيق (anbīq)

Based on the Wiktionary page provided, there is **no etymology section** for this word. 

The page only contains:
- **Pronunciation**: /ʔan.biːq/
- **Part of speech**: Masculine noun
- **Definition**: "alternative form of إِنْبِيق (ʔinbīq)"
- **Declension tables** showing various grammatical forms

The entry indicates this is an alternative spelling of another form rather than providing etymological information about the word's origin or source language.
```


### [2026-09-07T18:26:37.703Z] TOOL RESULT

```
# Etymology of Alembic

According to the Online Etymology Dictionary, here is the full etymology:

"distillation vessel used in old chemistry," late 14c., earlier _limbeck_ (mid-14c.), from Old French _alambic_ (13c.), via Old Spanish, from Arabic _al-anbiq_ "distilling flask," via Persian, from Greek _ambix_ "cup," a word of unknown, possibly Semitic, origin. Often spelled _limbeck_ 15c.-17c. The _al-_ is the Arabic definite article, "the."
```


## [2026-09-07T18:26:43.269Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A5%D9%86%D8%A8%D9%8A%D9%82",
 "prompt": "Quote verbatim the etymology given for the Arabic word إنبيق (inbīq)."
}
```


## [2026-09-07T18:26:45.001Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%AC%CE%BC%CE%B2%CE%B9%CE%BE",
 "prompt": "Quote verbatim the etymology, meanings, and any descendants listed for Ancient Greek ἄμβιξ."
}
```


### [2026-09-07T18:26:46.461Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-07T18:26:46.710Z] TOOL RESULT

```
# Etymology of إنبيق (inbīq)

According to the Wiktionary entry, the etymology is:

"Borrowed from Ancient Greek _ἄμβιξ_ (ámbix), allegedly via Classical Syriac."
```


## [2026-09-07T18:26:53.680Z] TOOL CALL #59: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%B1%CC%94%CC%81%CE%BC%CE%B2%CE%B9%CE%BE",
 "prompt": "Etymology and meaning of Ancient Greek ambix"
}
```


## [2026-09-07T18:26:53.922Z] TOOL CALL #60: WebSearch

```json
{
 "query": "Greek ἄμβιξ ambix etymology Pre-Greek Beekes cup cap of still"
}
```


### [2026-09-07T18:26:55.658Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-07T18:27:02.885Z] TOOL RESULT

```
Web search results for query: "Greek ἄμβιξ ambix etymology Pre-Greek Beekes cup cap of still"

Links: [{"title":"ἄμβιξ - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%E1%BC%84%CE%BC%CE%B2%CE%B9%CE%BE"},{"title":"ἄμβιξ - Ancient Greek (LSJ)","url":"https://lsj.gr/wiki/%E1%BC%84%CE%BC%CE%B2%CE%B9%CE%BE"},{"title":"ἄμπυξ - Ancient Greek (LSJ)","url":"https://lsj.gr/wiki/%E1%BC%84%CE%BC%CF%80%CF%85%CE%BE"},{"title":"ambix - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/ambix"},{"title":"ambix in English","url":"https://kaikki.org/dictionary/English/meaning/a/am/ambix.html"},{"title":"Ambulia","url":"https://en.wikipedia.org/wiki/Ambulia"},{"title":"Robert S. P. Beekes","url":"https://en.wikipedia.org/wiki/Robert_S._P._Beekes"},{"title":"alembic - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/alembic"},{"title":"Deep Dive: Why Ambix? - Ambix Spirits","url":"https://ambixspirits.com/deep-dive-why-ambix/"}]

Based on the search results, here's what I found about the Greek term ἄμβιξ (ambix):

## Definition and Meaning

ἄμβιξ (ambix) means 'cup, beaker', and more specifically, it refers to the "head" or "cap" which fits over the mouth of the cucurbit in a distilling apparatus to receive the vapors.

## Etymology

The etymological status of this word is uncertain. According to Wiktionary's classification, ἄμβιξ is listed among "Ancient Greek terms with unknown etymologies". 

Regarding Pre-Greek origin and Beekes: While the search results mention that Robert S. P. Beekes worked on Pre-Greek, the non-Indo-European language spoken in Greece before Greek, obtaining information from words in Classical Greek that show non-Greek structure, and that Beekes authored the Etymological Dictionary of Greek, the search results do not provide specific details about Beekes' analysis of ambix or whether he classified it as Pre-Greek.

## Related Etymology Notes

The search results include some German etymological notes suggesting the ending is similar to κύλιξ (kylix), though the exact Pre-Greek origins remain unclear.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-07T18:27:06.150Z] TOOL CALL #61: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E1%BC%84%CE%BC%CE%B2%CE%B9%CE%BE",
 "prompt": "Quote verbatim the etymology, definitions and descendants of Ancient Greek ἄμβιξ."
}
```


## [2026-09-07T18:27:07.676Z] TOOL CALL #62: WebFetch

```json
{
 "url": "https://lsj.gr/wiki/%E1%BC%84%CE%BC%CE%B2%CE%B9%CE%BE",
 "prompt": "Quote the LSJ entry for ἄμβιξ verbatim, including citations (authors/works) and any etymological note (Frisk/Beekes)."
}
```


### [2026-09-07T18:27:09.297Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-07T18:27:11.496Z] TOOL RESULT

```
# Etymology, Definitions, and Descendants of ἄμβιξ

## Etymology

"The suffix is no doubt a substrate element, as it is in κύλιξ (kúlix)." The word is "often connected with ἄμβη (ámbē, 'raised edge') and ἄμβων (ámbōn, 'crest of a hill'), but this remains uncertain." Ultimately, the source remains undetermined.

## Definitions

This Ancient Greek noun has two meanings:

1. "spouted cup"
2. "alembic, still"

## Descendants

The term produced several linguistic offspring across different languages:

- Modern Greek: άμβικας (ámvikas)
- Arabic: إِنْبِيق (ʔinbīq), with further descendants noted
- Classical Syriac: Multiple forms including ܐܡܒܝܩܐ (ʾambīqā)
- English: ambix
```


## [2026-09-07T18:27:18.416Z] TOOL CALL #63: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%86%D8%B1%D8%AF",
 "prompt": "Quote verbatim the etymology given for Persian نرد (nard, backgammon) and for the Arabic نرد if present. Mention any Middle Persian nēw-ardaxšīr."
}
```


## [2026-09-07T18:27:19.611Z] TOOL CALL #64: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%86%DB%8C%DA%A9",
 "prompt": "Quote verbatim the etymology given for Persian نیک (nīk) — Middle Persian, Old Persian, Proto-Iranian and PIE forms and cognates."
}
```


### [2026-09-07T18:27:24.716Z] TOOL RESULT

```
# Etymology of نرد (nard)

## Persian نرد
The etymology states: "From earlier _[نردشیر](/wiki/%D9%86%D8%B1%D8%AF%D8%B4%DB%8C%D8%B1#Persian "نردشیر")_ (nardašir), from [Middle Persian](https://en.wikipedia.org/wiki/Middle_Persian "w:Middle Persian") _[nywʾlthšyl](/wiki/nyw%CA%BElth%C5%A1yl#Middle_Persian "nywʾlthšyl")_ (nēw-ardaxšīr, "backgammon")."

## Arabic نرد
The Arabic entry provides: "Clipping of _[نَرْدَشِير](/w/index.php?title=%D9%86%D8%B1%D8%AF%D8%B4%D9%8A%D8%B1&action=edit&redlink=1 "نردشير (page does not exist)")_ (nardašīr) or from [Persian](https://en.wikipedia.org/wiki/Persian_language "w:Persian language")."

The Middle Persian origin (nēw-ardaxšīr) ultimately traces the word back to ancient roots referring to the backgammon game.
```


### [2026-09-07T18:27:26.051Z] TOOL RESULT

```
# Etymology of Persian نیک (nīk)

According to the Wiktionary entry, the word's origin traces through multiple language stages:

**Middle Persian:** "nēk" (derived from the diminutive form of a word meaning "brave, valiant")

**Old Persian:** "*naibakah" (from the cuneiform 𐎴𐎡𐎲, n-i-b /naibaʰ/)

**Proto-Iranian:** "*naybah"

The entry notes that the Persian term is "Equivalent to نیو (niv, 'brave, valiant') +‎ ـک (-ak, diminutive suffix)."

The source cites Oklor Skjærvø's 2009 work on Middle West Iranian, which explains: "the suffix -ak (-k) makes diminutives" and provides "nēw 'good': nēk 'good'" as a specific example.

No Proto-Indo-European forms or cognates are explicitly provided in this entry.
```


## [2026-09-07T18:27:33.010Z] TOOL CALL #65: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B1%D9%88%D9%86%D9%82",
 "prompt": "Quote verbatim the etymology and meanings for Arabic رونق (rawnaq) and Persian رونق if present."
}
```


## [2026-09-07T18:27:33.905Z] TOOL CALL #66: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/niteo",
 "prompt": "Quote verbatim the etymology of Latin niteō, including any PIE reconstruction, cognates, and reference to de Vaan."
}
```


### [2026-09-07T18:27:38.532Z] TOOL RESULT

```
# Etymology of Latin niteō

According to the Wiktionary entry, the etymology is as follows:

"Probably from a past participle Proto-Italic *nitos ('made bright'), from a root Proto-Indo-European *ney- ('to shine')."

The entry notes potential cognates including Middle Irish níam ("splendor, gleam") and níamda ("shining"), as well as Sanskrit नील (nī́la, "dark-colored, dark blue").

This etymological information is sourced from de Vaan's *Etymological Dictionary of Latin and the other Italic Languages* (2008), page 410.
```


### [2026-09-07T18:27:38.945Z] TOOL RESULT

```
# Etymology and Meanings: رونق (rawnaq)

## Arabic رونق (rawnaq)

**Etymology:** No etymology section provided for Arabic (as the root word).

**Meanings:**
- "beauty, glamour"
- "splendour"
- "radiance, glow, luster"

## Persian رونق (rawnaq)

**Etymology:** "Borrowed from Arabic رَوْنَق (rawnaq)."

**Meanings:**
- "boom, heyday, flourishing"
- (poetic) "beauty, glamour, splendor"
- (poetic) "radiance, glow, luster"
```


## [2026-09-07T18:28:00.953Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BQT runik\"; grep -n \"رونیک\\|رونيك\" BQT_v1_pages.txt BQT_v2_pages.txt incoming/BQT/BQT_v3_pages.txt incoming/BQT/BQT_v4_pages.txt 2>/dev/null | head; echo \"=== MON runik\"; grep -n \"رونیک\" MON_part1.txt MON_part2.txt | head; echo \"=== PLA rawnaq arabic\"; grep -n \"رونق\\|روناق\" incoming/PLA/PLA_pages.txt | head; echo \"=== PLA nik\"; grep -n -i \"nik\\b\\|äbnik\" incoming/PLA/PLA_pages.txt | head",
 "description": "Search for runik and rawnaq in Persian/Arabic loanword books"
}
```


### [2026-09-07T18:28:01.053Z] TOOL RESULT

```
=== BQT runik
=== MON runik
MON_part2.txt:20921:اورونیک متصل به چند مولکول آرابینوز 
MON_part2.txt:20924:گالاکتورونیک متصل به قندهای گالا کتوز 
MON_part1.txt:6964:میکا که دور آن سیم فرونیکل پیچیده شده 
MON_part1.txt:39638:الکترونیکی در جسم نیم هادی کر یستالین 
=== PLA rawnaq arabic
=== PLA nik
283:Botanik:           amlüg       "Birne",          azädraht         "persischer           Flieder",       asfaräg     "Spargel"
1930:              Alembik                   "Destillierkolben"                           11, wahrscheinlich                     aus       dem     pers.    ‘«_7T äbnik.
2951: -          barni:        "feine              Dattelart"             aus    dem       pers,    Js.      bar-nik           "gute    Frucht"       8
3583:u - banik:                  "Gips"        pers.        4,,
4990:           davänik,                ar..yi, dänig                    stammt       aus     dem mir,        dänak     2, syr. tert,
8227:Me] - zarnih:                         "Arsenik,              Sandarak"          pers.       11 < ap.             daraniyä         "Gold"
8241:Arsenik                                                                                   145                                                      za°faräni
8244:         daher                Arsenik             u.     Arsen     aus          dem        ar.        sernik             pers.      g         zarnih      g.    v.    1
9486:ori»         - sandrüs:;                  "Sandarak;            roter          Arsenik,            Lack"        14        mand.   sandlus,      syr.
14087:                                                                                                                Ce nik
```


## [2026-09-07T18:28:11.690Z] TOOL CALL #68: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%B1%D9%88%D9%86%D9%82/",
 "prompt": "What do Dehkhoda and Mo'in (فرهنگ معین) say about رونق — its origin tag (e.g. [ع.] Arabic) and meanings? Quote the origin bracket and first definition verbatim in Persian."
}
```


## [2026-09-07T18:28:12.614Z] TOOL CALL #69: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%B1%D9%88%D9%86%DB%8C%DA%A9/",
 "prompt": "Is there any entry for رونیک in Dehkhoda or Mo'in or any Persian dictionary on this page? Quote whatever is given."
}
```


### [2026-09-07T18:28:17.678Z] TOOL RESULT

```
# رونق - Dehkhoda and Mo'in Definitions

**Dehkhoda (لغت نامه دهخدا):**
- Origin tag: (ع اِ) — Arabic origin
- First definition: "آب کار" (prosperity/flourishing)

**Mo'in (فرهنگ معین):**
- Origin tag: [ع.] — Arabic origin  
- First definition: "فروغ ، روشنایی" (radiance, brightness)
```


### [2026-09-07T18:28:17.951Z] TOOL RESULT

```
Based on the content provided, there is **no dictionary entry definition** for رونیک (Rounik) from Dehkhoda, Mo'in, or other Persian dictionaries shown on this page.

The page only contains:
- User-submitted etymological information about Turkish language influences on Persian
- Historical references and bibliographic sources
- Images related to the word
- General information about the Abadis dictionary platform itself

The actual dictionary definitions from Dehkhoda, Mo'in, or other reference works are not included in the text provided.
```


## [2026-09-07T18:28:29.361Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SPG_keilinschriften1881.txt',encoding='utf-8',errors='replace').read().split('\\f')\np=t[198]\nimport re\ni=p.find('naibam')\nprint(p[max(0,i-800):i+500])\nEOF",
 "description": "Print Spiegel glossary p227"
}
```


### [2026-09-07T18:28:30.703Z] TOOL RESULT

```
Misswachs nom. D'ushiyäram H, 19.
abl. D'ushiyärä H, 17, (Von dush = SijQ und yära = aw. yäre Jahr.
Cf. oben die Bern, zu d. St. und Grammatik § 26 Anm.)
Drauga (7? ^T <7f <Ty^) Lüge. nom. Bh. l, 34. IV, 34. H,
20. abl. draugd Bh. IV, 37. H, 17. Aw. draogho, neup. g^^*> ^ durig;
die Schreibart 7? fcY i^ K^*" Bh. I, 34. beruht wol nur auf einem
Missverständnisse.
Draujana (7? ^f KTl "^K ^^) Lügner nom. Bh. IV, 38. 63.
68. Von duruj, lügen.
Dranga (7f ^T K^T*") lange Zeit acc. adverbial lange Zeit
hindurch Bh. IV, 56. 75. So übersetze ich, .indem ich mit Oppert
(Inscript des Achömenides p. 175) das neup. J^s^^ vergleiche. Doch
würde auch dargam = aw. deregha, neup. ot> einen guten Sina geben.
Wurzel ist drenj oder draj.
Naiha (r:^ y'j' r:f schön, gut Fem. nom. sg. naxM H, 8. Neutr.
acc. sg. naibam D, 13. 16. K, 20, Oppert vergleicht passend neup. ^ju
und huzv. ^rj i. e. neup. viLu.
Naiy (r:< ff y<-) nicht Bh. I, 48. 49. 52. 53. 71. II, 21. 24.
31. 51. 84. III, 15. 85. IV, 44. 47. 51. 55. 58. 63. 73. 78. V, 32 H, 11. K,
22. naishim Bh. IV, 49. Cf. Aw. noic und naedha.
Nactitabira ( ^^ ^TT "ff" ^TfT ^T IT ^Y ) N. pr. Name eines
Empörers in Babylon, nom. Bh. I, 77. 92. II, 1. IV, 12. d, 1. acc.
NadHtäbiram Bh. I, 80. 84. II, 4. 5. gen. Nad'itabirahyä Bh. I, 85. 89.
95. Der zweite Thei
```


## [2026-09-07T18:28:31.070Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== ARY nik\"; grep -n \"نیک\" incoming/ARY/ARY_pages.txt | head -8; echo \"=== ARY latin\"; grep -n -i \"NIK\\|NIV\\|NEI\" incoming/ARY/ARY_latin_index_pages.txt | head -8",
 "description": "Aryanpur for nik"
}
```


### [2026-09-07T18:28:31.136Z] TOOL RESULT

```
=== ARY nik
136:باستانشناسی و ویژگی‌های زبان شناختی زبان‌های ژرمنیکه؛ دیدمان گهواره بودن آلمان را نی ی
205:هندی» اسلاوی» بالتیکه) و زبانهای سنتم 4 (ژرمنی» لاتین» یونانی» سلنیک). در زبانهای
561:5 لاتین: ۸0153 گونیکه: 638آه شلایکر چنین استدلال کرد؛: این فهرست و فهرست‌های .+
749:آثار فلسفی و تاریخ ی گوناگون. زبان یونانیکلاسیکه به ندریج تبدیل به یونانی نوین شد. سخنگویان
789:سنگ نوشته‌هایی به الفبای رونیکك (۹17210) از آنها در شمال اروپاکشف شده است. این زبان در,
874:بانیکه؛ آلبانی
975:۲-قربانی کردن انسان وحیوان: قربانیکردن حیوان در میان هند و اروپائیا نکهن رواج داشت
1097:تروا ادامه داد تاکشته شد. او هم مانند دیگر قهرمانان هند و اروپایی در پی نام نیک بود نه سرای
=== ARY latin
596:Set 9 (2A ST Ay ND CY eee ague) ogSegem slaglj & y (CUNEIFORM) ho
3502:BFS ilall (SNOW : pL S) SNAW 5545 Sil NIVIS, NIK ig) IPH sp, SSNEZA !
3506:.SNTHL 5 joa y (NEVE : gy! (NIEVE : Lily NEIGE :4.31 SNIEG
5788:TORDEN (SWEDISH) «538 y+ STENEIN, STENO = (GREEK) gli,
5811:TENU FRENCH) Wi! 3 TENIK :(KURDISH) 53,5
6177:JAUNAS, JAUNIKIS JUVENCUS, JUVENIS (LATIN) 53
7018:‘REFERENCES bethy *OISMA, ORINEIN — «(GREEK) gli»
8833:*ARSANA, ARSANIVA (HITTITE) <2» ARSAL s(TOKHARIAN A) A 5 5%
```


## [2026-09-07T18:28:42.017Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SYN good\"; grep -n \"naiba\\|nitidus\\|niteo\" SYN.txt | head -6; echo \"=== FSD neat\"; grep -n \"neat.*nitidus\\|nitidus\" FSD_vol3.txt FSD_vol2.txt FSD_vol4.txt 2>/dev/null | head -6; echo \"=== SKT neat\"; grep -n -i \"^Neat\\|Neat, \" SKT.txt | head -6",
 "description": "Buck, Funk&Wagnalls, Skeat for neat"
}
```


### [2026-09-07T18:28:42.106Z] TOOL RESULT

```
=== SYN good
22488:Du., MHG, NHG klein, in MHG mostly ‘pure, neat, fine, pretty’ (cf. NHG kleinod ‘jewel, gem’), OHG kleinz ‘shining, slender, fine’, etc., OE cline ‘pure, clean’ (NE clean), prob. : Grk. yawol* apmrptopara Hesych., yAnvea ‘bright things, trinkets, stars’, yAnv7n ‘pupil of the eye’, yeAetv’ Aapumerv, avOetv Hesych., and other words with common notion of ‘bright, shining’. ‘Bright’ > ‘clean, neat’, as in Lat. nitidus > Fr. net, etc. (15.87), hence through ‘fine, delicate’ to ‘small’. Walde-P. 1.623.
26544:; Lat. nitidus (of
27043:Rum. neted, fr. Lat. nitidus ‘bright, shining’ (15.57). REW 5929.
27334:It. netto, Fr. net (OF r. neit, net > ME neate, nete ‘clean, pure, bright’, NE neat), fr. Lat. nitidus ‘bright, shining, polished’ (15.57). REW 5929.
29622:™ ‘mat NHG gut naiba-
29656:OPers. naiba (clearly ‘g00
=== FSD neat
FSD_vol3.txt:76466:( < L. nitidus (see nitid) + tela, web.] Nlt'^e-la'rl-set.—
=== SKT neat
3806:encomium,  coaunendation.  (L.  — Gk.) latinised  ftom  Gk.  iynuititov,  neat,  of iyiiiMJiuof,  laudatory,  full  of  revelry.  — Gk. iv,  in  ;  icwftof,  revelry.
12202:Neat  (I),  black  cattle,  an  ox.  fE.)  V met,  both  line,  and  pi.  AS.  mat nf<S/,  cattle.  -^  Toel  nau/,  pi.  naui,  cat M.H.G.Hf^,  fWJi^,  catllc.  p.  So  named  fi (beir  usefulness  and  eniploymeiU  ;  from t  of  A.  S.  Mtiian,  m'Stan,  to  use.  empl cf.  Icel.  njdta,  G.grm£ssen,  Goth,  niutan enjoy,  get  benefit  from.  Cf.  Litbi nauiid^  usefulneis,  Skt.  Hand,  to  be  pica (V  NUD.)     Der.  mat-herd.
12203:Noat  (a),  tidy.  (.F.-L.)  F.  «(,  ni netU,  fern.,  neat,  pure.  — L.  rutiduj,  shuk neat.  —  L,  mUrt,  to  shirtc.
12395:quaint,  neat.  odd.  (F«*L.)  M.  E. ifMeint,  also  iji40»Ht,  £omt,  commonly  with the  sense  of  'famous.'  »  O.  F.  £oint, 'quaint,  compt,  neat,  boe;*  Cot.  —  L. io^iitus,  well-known,  pp.  of  ccgHoatre,  to know;  ^cc  coKniaauoo  (above).  Confused with  L.  eemftuSf  neat,  pp.  of  iemurt^  to , Oflorn  {=co-imert  =  som-imere)\  esp.  in  F., but  the  M.  v..  word  keeps  lo  the  L. fOgnituj.    Der.  at-quaint  (above).
13050:subpoena,  a  writ  commanding  attend* ance  under  a  penalty.  (L.)     L.  nA,  under ; pvnd^  abl.  ofpctna,  a  peoUty. Faint;  see  Pioturo. Fainter,  a   rope   for   mooring  a  boat (F.  —  L  »  Gk.)     Assimilated  to  painUr, one  whu  paints :  orig.  M.  Y^panttr,  a  noose, esp.  for  catching  birds. —  O.  V.  pantitrt,  a snare  for  birds,    a   large  net  for  catching many  at  once.  —  \^  patUhtr,  a  hunting -net for    catching  wild  beasts.  —  Gk.  ■dj'Pi/^oi, adj..  catching  all  sorts.- Gk.  «ar,  neat,  of war,  every  ;  &^p,  a  wild  beast.     See  Fatt- and  Seer.     (And  xepoft/Aer,) Paiir :  see  Par.
16796:residue.  (F.-L.)  O. F.  rufim.* residuum^  a  remainder,  neat,  oi*  roaAi rem.iining.~L  rtsidtre  (above).
```


## [2026-09-07T18:28:49.619Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '29650,29662p' SYN.txt",
 "description": "Print Buck OPers naiba context"
}
```


### [2026-09-07T18:28:49.663Z] TOOL RESULT

```
ChSl. blagt (reg. for dyaGss and xpn- orés ‘good’ in moral sense, cf. Jagié, Ent- stehungsgesch. 326), in modern Slavic mostly ‘gentle, blessed, noble’, etc., never general for ‘good’, etym. dub. Walde-P. 2.182. Berneker 69.
Russ. chorosij (has displaced dobry; as the common word for ‘good’), orig. ‘or- derly, neat’, hypocoristic formation fr. ORuss. choronent, pple. of choroniti ‘put in order’: ChSl. chraniti ‘guard, keep’. Berneker 397. Jagié, Arch. sl. Ph. 6.282 ff.
8. Skt. sddhu-, orig. ‘straight, right, ready’, fr. sadh- ‘reach one’s goal, ac- complish, guide aright, etc.’. Walde-P. 2.450.
Skt. bhadra-, also ‘blessed, auspicious, fair’, prob. : Goth. batiza ‘better’, ba- tists ‘best?. Walde-P. 2.151f. Falk- Torp 67.
Skt. vasu- (Vedic in this sense; later mostly as neut. sb. ‘goods, wealth’), AY. vanhu-, vohu- (OPers. only in prop c names, as Dadraya-vaus, Vau-misa) : Gall. -vesus (in Bello-, Sigo-vesus, ete), Gme. Wisu-rth, -mar, Wisi-Gothae, ett,
Ir. feib ‘excellence’ (dat. sg.), W- a ‘fine, splendid, gay’, etc. Wa. 1.310. site
OPers. naiba (clearly ‘g00
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
igitized by Arya Samaj Foundation Chennai and eGangotri
. TEMPERAMENTAL, MORAL, AESTHETIC NOTIONS 1177 3 and so, rather than For the numerous other Indo-Iranian 7 jnscr- 4 5) = ¢ ’ ¢ J Dsiva y, elsewhere) : Ir. noib ‘holy’, | words that may be used for ‘good’ (and ipeautifu ’- bho-) fr, the root seen in Ir. | ‘bad’), cf. Schwyzer, Die altindischen und b. ( tia ce’, Lat. nitére ‘shine, glit- | altiranischen Worter fiir gut und bése, niam Pade. 9.321. Festgabe Kaegi 12 ff. ter’: 16.72 BAD 4s (8v0-) Goth. ubils Lith. blogas, negeras, piktas Grk. og ON vandr, illr, daligr Lett. sltkts, nelabs, l’auns NG Bae i Dan. ond, slet, slem, daarlig Chsl.  zitlit Lat. a tivo, malo Sw. ond, elak, ddlig SCr.  nevaljan, zao It. Eats OE yfel (earg) Boh. &patny, zly Fr. mal(o) ME _ wvel, ill, badde Pol. aly Be wil NE bad (ill, evil) Russ. plochoj, chudoj, dur- He Pie (Grach-, do-) Du. slecht, kwaad, erg noj Nir. ole (droch-, do-) OHG ubil Skt.  pdpa-, asddhu-, abha- WV * drwg (dy-) MHG tibel, bese dra- (dus-) Br. fall, gwall, drouk NHG schlecht, schlimm Ay. aka-, aya-, avawhu- : ; (bése, tibel, arg) (dus-)
For ‘bad’ as the opposite of ‘good’ there are equally generic words in some of the IE languages, but in others a vari- ety of terms partly differentiated in feel- ing and according to the object qualified, so that it may be difficult to say which is the more nearly generic. Some are mainly ‘evil, wicked’ in the moral sense.
An adj. denoting any undesirable quality, physical or mental, any oppro- brious epithet, may easily be generalized to ‘bad’. Thus, either in earlier attested meanings or in cognates, ‘disgusting, Ugly, defective, faulty, weak, timid, eee ete. In some languages neg. Pas. of words for ‘good’ are in fairly Common use, banca egteement between different tts’, maoge : is in a prefix for ‘ill-,
PAnian, eee in Greek and Indo- iit €n in the same branch there
```


## [2026-09-07T18:29:00.481Z] TOOL CALL #74: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/neat",
 "prompt": "Quote verbatim the etymology for \"neat\" (adj.) and any mention of net (adj.) and Latin nitere/nitidus and PIE root."
}
```


## [2026-09-07T18:29:01.600Z] TOOL CALL #75: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%86%DB%8C%D9%88",
 "prompt": "Quote verbatim the etymology and meanings for Persian نیو (nīv/nēw)."
}
```


### [2026-09-07T18:29:05.797Z] TOOL RESULT

```
# Persian نیو (nīv/nēw)

**Etymology:**
"From Middle Persian nyw /⁠nēw⁠/, 'good, brave, valiant', from Old Persian n-i-b /⁠naibaʰ⁠/, 'blessed', from Proto-Iranian *naybah ('fortunate, blessed')."

**Meaning:**
The entry defines this archaic adjective as "brave, valiant."
```


### [2026-09-07T18:29:06.123Z] TOOL RESULT

```
# Etymology of "Neat" (adj.)

**Main Etymology:**
"1540s, 'clean, free from dirt,' from Anglo-French neit, French net 'clear, pure' (12c.), from Latin nitidus 'well-favored, elegant, trim,' literally 'gleaming,' from nitere 'to shine,' from PIE root *nei- 'to shine'"

**Key Components:**

The adjective traces back through French to Latin *nitidus* (meaning gleaming or elegant) and the verb *nitere* (to shine). The ultimate Indo-European foundation is the root *\*nei-*, which also appears in related words meaning "gleam" and "splendor" across Celtic languages.

**Sense Development:**
The word expanded from its original cleanliness sense to mean "well-shaped" (1540s), then "tidy in habit" (1570s), "orderly" (1590s), and "undiluted" for liquor (circa 1800).

**Note on "Net":**
While the entry discusses both a noun and adjective form of "neat," the document does not provide a separate entry linking "net" (the noun, meaning mesh fabric) to this same etymology, though related words like "natty" derive from the same root.
```


## [2026-09-07T18:29:21.805Z] TOOL CALL #76: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%D8%A5%D9%86%D8%A8%D9%8A%D9%82|p355 Arabic inbiq: Wiktionary derives it from Ancient Greek ambix via Syriac, not from Persian ab-nik (nodes 6,7)\" \\\n \"https://www.etymonline.com/word/alembic|p355 alembic: Etymonline chain Gk ambix > Ar al-anbiq (via Persian) > OSp > OFr > ME (nodes 5,6,8,9,10)\" \\\n \"https://en.wiktionary.org/wiki/%E1%BC%84%CE%BC%CE%B2%CE%B9%CE%BE|p355 Greek ambix: substrate/unknown etymology, descendants Arabic inbiq and Syriac ambiqa (node 5)\" \\\n \"https://en.wiktionary.org/wiki/%D9%86%D8%B1%D8%AF|p355 Persian nard < nardashir < MP new-ardaxsir (node 3)\" \\\n \"https://en.wiktionary.org/wiki/%D9%86%DB%8C%DA%A9|p355 Persian nik < MP nek, dim. of new; OP *naibakah, PIr *naybah (nodes 2,3)\" \\\n \"https://en.wiktionary.org/wiki/%D9%86%DB%8C%D9%88|p355 Persian niv < MP new < OP naiba- < PIr *naybah (nodes 1,2,3)\" \\\n \"https://en.wiktionary.org/wiki/%D8%B1%D9%88%D9%86%D9%82|p355 Arabic rawnaq (no etymology given, treated as Arabic); Persian rownaq borrowed from Arabic (nodes 12,13)\" \\\n \"https://en.wiktionary.org/wiki/niteo|p355 Latin niteo < PIt *nitos < PIE *ney- 'to shine' (de Vaan 410) (node 14)\" \\\n \"https://www.etymonline.com/word/neat|p355 English neat < Fr net < L nitidus < nitere < PIE *nei- 'to shine' (nodes 14,15)\" \\\n \"https://abadis.ir/fatofa/%D8%B1%D9%88%D9%86%D9%82/|p355 Dehkhoda (ع ا) and Mo'in [ع.] both tag Persian رونق as an Arabic loan (node 13)\" \\\n ; do url=\"${u%%|*}\"; note=\"${u##*|}\"; python3 tools/fetch_source.py \"$url\" --note \"$note\" 2>&1 | tail -2; done",
 "description": "Archive web sources"
}
```


### [2026-09-07T18:29:27.135Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/36598f374e4f7bb0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/36b71d3f79e008e4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c22c9ab5afedfa27.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0a9557299970eee3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/185cb6668a0c0b48.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/faea9ff3b00e9489.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/25be4fc0b8cf9295.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3991ee7fbe77cb15.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f122b9b7c7e75415.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6bd0c49dda6ecbad.txt
```


## [2026-09-07T18:29:52.532Z] TOOL CALL #77: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/AFM && cat > /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/AFM/74.vision.txt <<'EOF'\n# Addi Shir, Kitab al-Alfaz al-Farisiyya al-Mu'arraba (Beirut 1908), printed page ٧٤ = 74\n# read from the page image (AFM.pdf pdf page 76; printed = pdf page − 2, verified against ٧٥ on pdf 77)\n# the local OCR (AFM_pages.txt) renders this page as Syriac/Latin garbage, hence read by eye.\n\n٭ (الرَوْنَق) حُسْنُ كلِّ شيء. مركّب من رُو اي وجه ومن نَیک اي صبیح حسن\n\n# neighbouring entries on the same page (context):\n٭ (الرَنْف والرَنَف) بهرامج البرّ فارسیّتهُ رَنْف. قال في البرهان القاطع: «رِنف على وزن انف ...»\n(الرَام) اليوم الحادي والعشرون من كلّ شهر من شهور الفرس ... واصل معنى رام بالفارسیّة الراحة والفرح\n٭ (الراهب) وجمعهُ رُهبان وهو معروف. قال فرنكل (ص:٢٦٨) انّهُ مأخوذ من السریانيّ ... لكن اصل الكلمة فارسيّ وهو مركّب من رُه اي الصلاح ومن بان اي صاحب ...\n(الرَهنامَج) كتاب الطريق مركّب من راه اي طريق ومن نامَه اي كتاب\n٭ (الرَوَاج) ضدّ الكساد تعريب رَوايى الذي بمعناهُ وهو مشتقّ من رفتن ...\n٭ (الرَهْوان) معرّب رَهْوار وهو البِرذون اذا كان لیّن الظهر في السَیر ...\n٭ (الرَوَند والرِیوَند والراوند) ...\nEOF\ncat > /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/AFM/75.vision.txt <<'EOF'\n# Addi Shir, al-Alfaz al-Farisiyya al-Mu'arraba (1908), printed page ٧٥ = 75 (AFM.pdf pdf page 77)\n# read by eye; used only to fix the pdf→printed offset (printed = pdf − 2). No رونق entry here.\n٭ (الرَاز) رئيس البنّائين وهو فارسيّ محض ومعناهُ الطیّان\n(الرُوزنامة) مركّبة من رُوز اي يوم ومن نامه اي كتاب\n٭ (الرَوس) ... معرّب عن روش\n٭ (الرَوْضة) ... معرّبة عن ریز ...\n(الرُوط) معرّب رُود وهو النهر ... \n(الرَاوُوق) المصفاة تعريب راوك وهو ما صَفا من الخمر والماء وغيرهما (فرنكل ص:١٦٥)\n(الرُون) فارسيّ محض وهو الشدّة\n٭ (الریغ) تعريب ریك وهو الغبار\nEOF\ncp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/afm76.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/AFM/74.png\ncp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/afm77.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/AFM/75.png\nls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/AFM/",
 "description": "Save AFM vision notes and page images"
}
```


### [2026-09-07T18:29:53.926Z] TOOL RESULT

```
total 6944
drwxrwxr-x  2 sfmqrb sfmqrb    4096 Sep  7 14:29 .
drwxrwxr-x 13 sfmqrb sfmqrb    4096 Sep  7 13:51 ..
-rw-rw-r--  1 sfmqrb sfmqrb 1512597 Sep  5 16:42 0120.png
-rw-rw-r--  1 sfmqrb sfmqrb     598 Sep  5 16:43 0120.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb 1090365 Sep  5 16:42 0123.png
-rw-rw-r--  1 sfmqrb sfmqrb    1396 Sep  5 16:42 0123.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  774972 Sep  6 18:55 0141.png
-rw-rw-r--  1 sfmqrb sfmqrb     903 Sep  6 18:54 0141.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb 1046357 Sep  6 18:55 0142.png
-rw-rw-r--  1 sfmqrb sfmqrb    2100 Sep  6 18:55 0142.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb    2726 Sep  6 17:24 39.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb 1579505 Sep  7 14:29 74.png
-rw-rw-r--  1 sfmqrb sfmqrb    1517 Sep  7 14:29 74.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb 1055262 Sep  7 14:29 75.png
-rw-rw-r--  1 sfmqrb sfmqrb     811 Sep  7 14:29 75.vision.txt
```


## [2026-09-07T18:30:01.949Z] TOOL CALL #78: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/c355_conn.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/355-connector.png && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/c355_runik2.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/355-runik.png && sed -n '1,120p' /home/sfmqrb/git/rishe/tools/verify_check.py",
 "description": "Copy audit crops and read verify_check.py"
}
```


### [2026-09-07T18:30:02.026Z] TOOL RESULT

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


## [2026-09-07T18:30:49.956Z] AGENT

Now let me write the verification file.


## [2026-09-07T18:42:57.554Z] TOOL CALL #79: Bash

```json
{
 "command": "python3 - <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW = \"https://en.wiktionary.org/wiki/\"\n\nroot = {\n \"entry\": 0,\n \"root\": \"Nei 1, Ni 2\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *nei- / *neiə- : *nī- 'to be vividly moved, be excited; to shine' (Pokorny 2. nei-, IEW 760); adjective derivative *noi-bʰo- 'good, holy'\",\n \"note\": \"Pokorny IEW 760 has '2. nei-, neiə- : nī- ‚lebhaft bewegt sein, erregt sein, glänzen‘; noi-bho- ‚gut, heilig‘; kelto-germ. nei-to-, ni-tu- ‚Leidenschaft‘', and Watkins/AHD has 'nei-. To be excited, shine. [Pok. 2. nei- 760]'. Nourai's gloss 'to shine, to be excited' is a literal rendering of Pokorny's, the language label 'Indo-European' is right, and the page number 760 is exact. The only caveat is the label: Pokorny's *1.* nei- (p. 760 as well) is 'führen, to lead' and his *2.* nei- is the 'shine' root, so Nourai's 'Nei 1' is his own numbering, not Pokorny's. The two branches drawn on this page (Old Persian naiba- via *noi-bʰo-, and Latin niteō via *ni-to-) are precisely the two branches Pokorny lists under 2. nei-, so the root box is sound. The root is not in Watkins as 'noibho-' but the OP/NP words are placed under it by Lidén 1897, Walde-Pokorny II 321/336, Pokorny 760, Klein 1033, Buck 16.71 and Hübschmann.\",\n \"note_fa\": \"ریشهٔ هندواروپایی آغازین *nei- / *nī- «جنبش و تابش داشتن، درخشیدن» در واقع همان ریشهٔ «2. nei-» پوکورنی (صفحهٔ ۷۶۰) است که معنای آن را «lebhaft bewegt sein, erregt sein, glänzen» آورده‌اند؛ واتکینز (پیوست ریشه‌های فرهنگ امریکن هریتیج) نیز همین را با ارجاع به پوکورنی ۷۶۰ می‌آورد. هر دو شاخهٔ این نمودار — پارسی باستان naiba- از *noi-bʰo- و لاتین nitēre از *ni-to- — در همان مادهٔ پوکورنی أمده است. تنها نکتهٔ قابل ذکر این که شماره‌گذاری «۱» از خود نورایی است و در پوکورنی این ریشه شمارهٔ ۲ است (ریشهٔ شمارهٔ ۱ به معنای «راهبری کردن» است). ادعای نورایی در بارهٔ خود ریشه درست است.\",\n \"sources\": [W+\"niteo\", W+\"%D9%86%DB%8C%D9%88\"],\n \"ref_check\": [\n   {\"ref\": \"POK:760\", \"status\": \"supports\",\n    \"note\": \"Pokorny IEW p. 760 (page marker '760' at POK_02.txt line ~6663, entry at line 6665): '2. nei-, neiə- : ni- ‚lebhaft bewegt sein, erregt sein, glänzen‘; noi-bho- ‚gut, heilig‘ ... Lat. niteö, -ere ‚glänze, strahle‘ ... *noi-bho- in apers. naiba-, npers. new ‚schön, gut‘, air. noib ‚heilig‘'. Both the gloss and both branches of Nourai's chart are there. grep: grep -n 'naiba' POK_02.txt\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. II, s.v. '2. nei- ‚glänzen‘' (WLD_Bd2_pages.txt lines 21213-21226; = WP. II 321/336 cited by Pokorny)\", \"stance\": \"supports\",\n    \"note\": \"'2. nei- ‚glänzen‘. Lat. niteo, -ere ‚glänzen‘, nitidus ... *noi-bho- in ap. naiba-, np. new ‚schön, gut‘, air. noib ‚heilig‘ (Lidén Stud. 59 m.Lit.)' — note that Walde-Pokorny's own authority for the Iranian branch is Lidén p. 59, i.e. Nourai's AIN:59.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. nei- (AHD_watkins1985.txt line 776)\", \"stance\": \"supports\",\n    \"note\": \"'nei-. To be excited, shine. 1. Suffixed form *nei-to- in Germanic *nitha- ... 2. Suffixed zero-grade form *ni-to- in Latin nitere, to shine: NEAT1, (NET2). 3. Possibly Persian nil, indigo: ANIL, LILAC. [Pok. 2. nei- 760.]' — identical gloss and page; Watkins does not carry the Old Persian naiba- branch.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, s.v. noit- (nit-) (1) (IEC.txt line 11808)\", \"stance\": \"partial\",\n    \"note\": \"'noit- (nit-) (1) “inflame, kindle; be inflamed, burn brightly”. Lat. niteo, ere, v. “shine”; cf. nitidus, adj. “bright”' — Mann sets Latin niteō up under a separate root *noit-/nit- ‘kindle’ rather than under nei-, so the Latin branch is compatible in substance but differently labelled; Mann's own 'nei-' (line 11581) is the preverb 'down'.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 16.71 'good', pp. 1176-77 (SYN.txt lines 29656 ff.)\", \"stance\": \"supports\",\n    \"note\": \"'OPers. naiba (clearly “good” [in the inscriptions] and so, rather than “beautiful”) : Ir. noib “holy”, (*noi-bho-) fr. the root seen in Ir. niam “radiance”, Lat. nitere “shine, glitter”: Walde-P. 2.321.'\"}\n ],\n \"nodes\": []\n}\n\nN = root[\"nodes\"]\n\nN.append({\n \"id\": 1, \"lang\": \"Old Persian\", \"words\": \"ni 3, naiba\", \"verdict\": \"confirmed\",\n \"derivation\": \"Old Persian naiba- (cuneiform n-i-b) 'beautiful, good' is well attested in the Achaemenid inscriptions — fem. nom. naibā (DPd 8 'a land ... which is beautiful'), neut. acc. naibam (XPa 13/16, XPg 4, DSe 32, DSi 4, DSp 2, XPh 43, always of Xerxes' and Darius' building work, 'much other good/beautiful (construction) was built'), and it is the standing antonym of duš-karta- 'ill-made'. Formally it goes back to PIE *noi-bʰo- (o-grade of *nei- 'to shine' + the adjectival suffix -bʰo- as in Latin albus, lit. rai-ba-s), whence also Old Irish nōib 'holy'; the original sense will have been 'shining, radiant', which split into Iranian 'good, beautiful' and Irish 'pure, holy' (Lidén 1897: 59-60, Walde-Pokorny II 321/336, Pokorny 760, Buck 16.71). Proto-Iranian is reconstructed *naybah 'fortunate, blessed'. Nourai's second headword 'ni 3' is not an attested Old Persian lexeme: it is his cross-reference label for the bare root variant nī- (his root entry 'Ni'), and only naiba- belongs in the box. Kent's Old Persian lexicon dissents from the whole IE connection ('naiba- “good” (only in Iranian)', p. 43), but he stands alone against Lidén, Walde-Pokorny, Pokorny, Hübschmann, Klein and Buck.\",\n \"derivation_fa\": \"پارسی باستان naiba- (میخی n-i-b) «زیبا، نیک» در سنگ‌نوشته‌های هخامنشی فراوان به کار رفته است (naibā در DPd ۸؛ naibam در XPa ۱۳ و ۱۶، XPg ۴، DSe ۳۲) و همواره متقابل duš-karta- «بدساخته» است. این واژه از صورت هندواروپایی *noi-bʰo- (پایهٔ o از ریشهٔ *nei- «درخشیدن» به افزودن پسوند صفتساز -bʰo-) می‌آید؛ هم‌ریشهٔ ایرلندی باستان nōib «مقدّس» است و معنای نخستین آن «درخشان» بوده که از یک سو به «نیک، زیبا» و از سوی دیگر به «پاک، مقدّس» دگرگون شده است (لیدن ۱۸۹۷، والده‐پوکورنی، پوکورنی ۷۶۰، باک). ایرانی باستان را *naybah «خوش‌بخت، فرّه‌مند» بازسازی کرده‌اند. اما «ni 3» واژهٔ پارسی باستان نیست؛ ارجاع درونی نورایی به ریشهٔ «Ni» است. کنت در واژه‌نامهٔ پارسی باستان این ریشه‌شناسی را نمی‌پذیرد، ولی بیشتر پژوهشگران دیدگاه لیدن را پذیرفته‌اند. ادعای نورایی درست است.\",\n \"sources\": [W+\"%D9%86%DB%8C%D9%88\", W+\"%D9%86%DB%8C%DA%A9\"],\n \"ref_check\": [\n   {\"ref\": \"POK:760\", \"status\": \"supports\", \"note\": \"'*noi-bho- in apers. naiba-, npers. new ‚schön, gut‘, air. noib ‚heilig‘' (POK_02.txt line 6665, on printed p. 760).\"},\n   {\"ref\": \"KNT:192\", \"status\": \"contradicts\", \"note\": \"Kent's lexicon (KNT.txt lines 5583-84, s.v. naiba-) gives 'naiba- adj. “beautiful, (religiously) good”, replacing GAv. vahu- “good”, and opposite of duš-karta- ... NPers. nē(w) “brave, good”' — so the word, gloss and New Persian continuation are confirmed, but Kent expressly denies the IE root: 'OP p b f are in some instances not traceable to pIE forebears ... such are piru- “ivory”, sikabru- “carnelian”, naiba- “good” (only in Iranian)' (line 1042, § on b). Page 192 is in the grammar/lexicon range; the lexicon entry itself is at p. 193 in the 1953 printing.\"},\n   {\"ref\": \"AIN:59\", \"status\": \"supports\", \"note\": \"Lidén, Studien (1897) p. 59 is headed exactly 'Ai. nila-. — Apers. naiba-' and argues the root 'nei-, ni- ‚glänzen‘' from Latin nit-eo/re-nid-eo and Irish niam (AIN.txt leaf 64, printed p. 59). This is the study Walde-Pokorny cites for the Iranian branch.\"},\n   {\"ref\": \"SPG:227\", \"status\": \"supports\", \"note\": \"Spiegel, Die altpersischen Keilinschriften (2. Aufl. 1881), Glossar p. 227 (SPG_keilinschriften1881.txt leaf 198): 'Naiba (cuneiform) schön, gut. Fem. nom. sg. naibā H,8. Neutr. acc. sg. naibam D,13.16. K,20. Oppert vergleicht passend neup. نیک und huzv. ... i.e. neup. نیکو.' The identification of SPG with the Keilinschriften is thereby confirmed, since the Glossar offset (leaf = printed − 29) lands exactly on the naiba- entry.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW, s.v. p. naiba- (BRT.txt line 18484)\", \"stance\": \"supports\",\n    \"note\": \"'p. naiba- Adj. (fem. °bā-) ‚schön, gut, tüchtig‘: dahyāuš .. hyā °bā D,4.2; vasiy aniyašciy naibam kartam ... ‚auch noch viel andres Schöne ist geschaffen‘ X.1.3' — form, gender and glosses as in the chart; Bartholomae gives no PIE root here.\"},\n   {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien, pp. ~90/98/109 (HUB.txt lines 5966, 6006, 6406, 6440)\", \"stance\": \"supports\",\n    \"note\": \"'(vgl. nek ‚gut, schön‘ = phl. nevak, ap. naiba-)'; '-eva- zu ... in nek ‚gut, schön‘ = phl. nevak, ap. naiba-'; 'ap. naiwa-, geschrieben naiba- ‚schön‘'; 'Nēvšahpuhr, np. Nēšāpūr (Stadt), zu ap. naiba-'.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 16.71 'good', p. 1177 (SYN.txt line 29656)\", \"stance\": \"supports\",\n    \"note\": \"'OPers. naiba (clearly “good” ... rather than “beautiful”) : Ir. noib “holy”, (*noi-bho-) fr. the root seen in Ir. niam “radiance”, Lat. nitere “shine, glitter”.'\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. II s.v. 2. nei- (WLD_Bd2_pages.txt line 21225)\", \"stance\": \"supports\",\n    \"note\": \"'*noi-hho- [= *noi-bho-] in ap. naiba-, np. new ‚schön, gut‘, air. noib ‚heilig‘ (Lidén Stud. 59 m.Lit.).'\"}\n ]\n})\n\nN.append({\n \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"něv; něv-ak\", \"verdict\": \"confirmed\",\n \"derivation\": \"Old Persian naiba- gave Middle Persian nēw (Pahlavi book spelling nyw, Manichaean nyw) 'good, brave' by the regular loss of Old Iranian final -a and the monophthongisation ai > ē (the same change as in OP daiva- > MP dēw); MacKenzie p. 59 prints 'nēw [nyw | = M, N ~] good, brave', and Horn's no. 1068 gives 'phlv. nēwak, nēwakīh, nēw (PP Gl.)'. The extended form nēw-ak (spelt nywk) is nēw plus the productive Middle Persian suffix -ak (Old Iranian -aka-, in origin a diminutive/relational suffix); it contracted to nēk already inside Middle Persian, which is why MacKenzie reads the very same spelling nywk as nēk 'good, beautiful' with a by-form nēkōg, while Nyberg's glossary reads it nēvak. Nourai's two forms therefore correspond exactly to Lidén's 'pehl. nēw, pehl. nēw-ak' (Studien p. 60), which is where he took them from; the glosses 'brave' for nēw and 'good' for nēw-ak are a legitimate simplification (both words carry both senses).\",\n \"derivation_fa\": \"پارسی باستان naiba- در فارسی میانه به nēw (نوشتار پهلوی nyw) «نیک، دلیر» بدل شده است؛ واکهٔ مرکّب ai ایرانی باستان به ٔe کشیده تبدیل شده و «a» پایانی افتاده است (همان دگرگونی که daiva- را به dēw رساند). مکنزی در صفحهٔ ۵۹ می‌نویسد: «nēw [nyw] good, brave» و هرن در مادهٔ ۱۰۶۸ صورت‌های nēwak و nēwakīh را می‌آورد. صورت nēw-ak از افزودن پسوند -ak (از ایرانی باستان -aka-) ساخته شده و همان در فارسی میانه به nēk تبدیل شده است؛ از این‌رو مکنزی همان نوشتار nywk را nēk می‌خواند و نیبرگ nēvak. صورت‌های نورایی دقیقاً همان است که لیدن در صفحهٔ ۶۰ آورده است. ادعای نورایی درست است.\",\n \"sources\": [W+\"%D9%86%DB%8C%D9%88\", W+\"%D9%86%DB%8C%DA%A9\"],\n \"ref_check\": [\n   {\"ref\": \"AIN:60\", \"status\": \"supports\", \"note\": \"Lidén, Studien p. 60 (AIN.txt leaf 65): 'Endlich möchte ich hier unterbringen apers. naiba- ‚schön, gut‘, pehl., npers. nēw, pehl. nēw-ak npers. nēk ‚schön, gut‘, womit air. nōib nōeb ‚heilig‘ identisch ist ... Die Grundform idg. *noi-bho- ...' with footnote 3 'HORN Grundriss d. neupers. Etymol. n:o 1068'. This is verbatim Nourai's Pahlavi box.\"},\n   {\"ref\": \"BQT:2237\", \"status\": \"supports\", \"note\": \"Borhan-e Qate' ed. Mo'in, p. 2237 (vol. 4, pdf p. 320 of BQT_v4_picofile.pdf, s.v. نیو), Mo'in's footnote 10: 'پهلوی nēv (شجاع، قهرمان) [هز. ...] «نیبرگ ص ۲۱۸»: «نیو ... دلیر و مردانه بود. فردوسی (طوسی) گفت: چو طوس و چو گودرز گشواد و گیو / چو گرگین و فرهاد و بهرام نیو» «لغت فرس ص ۴۱۲».' The Pahlavi form nēv with the gloss 'brave' is exactly Nourai's, and this is also the source of the Ferdowsi verse printed in his Persian box.\"},\n   {\"ref\": \"SNS:291\", \"status\": \"not_found\", \"note\": \"Tavoosi's Shayast-ne-Shayast glossary does contain the entry ('nyk, nyw ... (AiWb. 1035) naiba-', SNS_pages.txt leaf 163), which is the right lemma with a cross-reference to Bartholomae's AiW col. 1035 s.v. naiba-, but the printed page number could not be mapped: the archive.org scan has 242 leaves and refs_online.json records the page offset as undetermined, so p. 291 cannot be confirmed.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD p. 59 (PHD_mackenzie.txt lines 3698-3716)\", \"stance\": \"supports\",\n    \"note\": \"'nēw [nyw | = M, N ~] good, brave.' and just above 'nēk [nywk | M nyk, N ~] good, beautiful', 'nēkōg [nywkwk | M nyyqww, N nēkū] = nēk' — i.e. MacKenzie reads Nourai's nēv-ak as nēk, the same spelling nywk.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (Glossary), s.v. nēvāk (NYB_vol2_glossary.txt line 2682)\", \"stance\": \"supports\",\n    \"note\": \"'nēvák [nywkʼ] good in a general sense; beautiful, nice; favorable, comp. ~-tar 604; adv. well 220, 713 ... Ps. nywk-; Paz. nēk, nyāk; NP nēk.' — Nyberg's reading nēvak is the one Nourai (after Lidén and Horn) uses, and Nyberg himself gives NP nēk as the outcome.\"},\n   {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 1068, pp. 238-39 (HRN.txt line 9221, leaf 259-60)\", \"stance\": \"supports\",\n    \"note\": \"'1068. nēk ‚schön, gut‘, nēkō, nēkī, nēw ‚wacker, Held‘ (Šāhn. I, 416 Vers 555 ...) ... ap. naiba- ‚schön, gut‘; phlv. nēwak, nēwakīh, nēw (PPGl.).'\"}\n ]\n})\n\nN.append({\n \"id\": 3, \"lang\": \"Persian\", \"words\": \"Nîv «نیو ( نیوان )»; nard 1 «نرد ۱»; nîk «نیک ( نیکو )»\", \"verdict\": \"confirmed\",\n \"derivation\": \"All three New Persian words go back to the Middle Persian pair of the previous box. (a) نیو nīv/nēv 'brave, valiant' (pl./collective نیوان) continues MP nēw unchanged but for the New Persian raising of ē to ī in the classical-to-modern pronunciation; it is a Shahname word, and Mo'in quotes for it the very verse Nourai prints, Ferdowsi's 'چو طوس و چو گودرز گشواد و گیو / چو گرگین و فرهاد و بهرام نیو'. (b) نیک nīk 'good' (with the extended نیکو nīkū < MP nēkōg) continues MP nēk < nēw-ak, i.e. nīk is literally the -ak derivative of nīv; Wiktionary states this explicitly ('equivalent to نیو (niv) + ـک (-ak)', from MP nēk, OP *naibakah, Proto-Iranian *naybah). (c) نرد nard 'backgammon' is the clipped form of Middle Persian nēw-ardaxšīr, the name of the game 'the good/heroic Ardaxšīr' invented, in legend, by Ardashir I: MacKenzie's dictionary prints 'nēw-ardaxšīr [nywʼltḥšyr | N nard!] backgammon' and the Pahlavi treatise Wīzārišn ī čatrang ud nihšīn ī nēw-ardaxšīr is named after it; Persian نرد and Arabic نرد are shortenings of the intermediate نردشیر nardaxšīr/nardashīr, which itself survives in Arabic نردشیر 'dice'. Nourai's phrase 'distorted form of Niv Ardeshir' is precisely Mo'in's ترخیم (clipping). Ferdowsi already uses نرد where the Pahlavi source has nēw-ardaxšīr.\",\n \"derivation_fa\": \"هر سه واژه بازماندهٔ همان دو صورت فارسی میانه اند. «نیو» (جمع: نیوان) از nēw پهلوی و واژه‌ای شاهنامه‌ای است؛ معین در حاشیهٔ برهان قاطع (ص ۲۲۳۷) همان بیتی را که نورایی نقل کرده گواه می‌آورد. «نیک» (و نیکو از nēkōg) از nēk پهلوی و آن خود از nēw-ak است؛ پس «نیک» در اصل مشتقّ پسوندی «نیو» است. «نرد» نیز صورت مرخّم «نیو‐اردشیر» (پهلوی nēw-ardaxšīr) است؛ مکنزی می‌نویسد «nēw-ardaxšīr ... backgammon» و رسالهٔ پهلوی «ویزارشن چترنگ و نششین نیو‐اردشیر» به همین نام است. میانجی این دو، «نردشیر» است که در عربی به معنای مهره/طاس مانده است. فردوسی خود در جای «نیو اردشیر» پهلوی، «نرد» را به کار برده است. ادعای نورایی درست است.\",\n \"sources\": [W+\"%D9%86%D8%B1%D8%AF\", W+\"%D9%86%DB%8C%DA%A9\", W+\"%D9%86%DB%8C%D9%88\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:2127\", \"status\": \"supports\", \"note\": \"Borhan-e Qate' ed. Mo'in p. 2127 (vol. 4, pdf p. 210), s.v. نرد ۲, footnote 2: 'کلمهٔ «نیو اردشیر» که بازیی بوده که گویا اردشیر آنرا اختراع نموده بترخیم درعربی وفارسی «نرد» شده است ... در پهلوی nēw-Artaxšīr «خسرو کوادان ...» ... فردوسی در شاهنامه ... بجای نیو اردشیر کلمهٔ «نرد» را بکار برده ... معرّب کلمهٔ ... «نرد» است و «نردشیر» درعربی بمعنی مهره (طاس) بازی است «دزی ج ۲ ص ۹۵۵»'. Nourai's 'distorted form of Niv Ardeshir' is this footnote almost word for word. (نیو and نیک themselves stand on later pages of the same volume — نیو on p. 2237, cited in the box above.)\"},\n   {\"ref\": \"KLN:1033\", \"status\": \"supports\", \"note\": \"Klein s.v. 'neat, adj.' (KLN_1966.txt line 25080; the page marker '1033' stands at line 25059, so the entry is on p. 1033): '... fr. I.-E. base *nei-, *ni-, “to shine”, whence also Mir. niam ... OPers. naiba-, ModPers. new, “beautiful”.' Klein's 'ModPers. new' is Nourai's Nîv.\"},\n   {\"ref\": \"TZF:20\", \"status\": \"not_checked\", \"note\": \"Abolghasemi, Tarikh-e Mokhtasar-e Zaban-e Farsi (1373) is not available online in a form that can be read here (refs_online.json: PDF behind a ketabnak login, not on archive.org).\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD p. 59 and English-Pahlavi index (PHD_mackenzie.txt line 3716; PHD.txt line 912)\", \"stance\": \"supports\",\n    \"note\": \"'nēw-ardaxšīr [nywʼltḥšyr | N nard!] backgammon' — MacKenzie himself equates the Middle Persian compound with New Persian nard; the index likewise has 'backgammon nēwardaxšīr'.\"},\n   {\"src\": \"MON\", \"where\": \"Mo'in, s.v. نیک / نیو (checked in the 2-vol Adena condensation, MON_part2.txt, and via abadis.ir)\", \"stance\": \"partial\",\n    \"note\": \"The lexicon has the words with the expected senses, but the 2-vol condensation available here strips the Latin-script Pahlavi etyma of the 6-vol print edition, so it can only corroborate the meanings, not the etymology.\"},\n   {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 1068 (HRN.txt line 9221)\", \"stance\": \"supports\",\n    \"note\": \"'nēk ‚schön, gut‘, nēkō, nēkī, nēw ‚wacker, Held‘ (Šāhn. I, 416 Vers 555; III, 1106 Vers 707, von einer Frau)' — Horn's nēkō is Nourai's نیکو and his nēw 'wacker, Held' is نیو.\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e Rishe-ha-ye Hend-o-Orupayi (grep نیک / نیو in ARY_pages.txt and the Latin index)\", \"stance\": \"silent\",\n    \"note\": \"No headword for نیک or نیو was found; the hits are unrelated (رونیک 'runic', نام نیک in running text).\"}\n ]\n})\n\nN.append({\n \"id\": 4, \"lang\": \"Persian\", \"words\": \"âbnîk «آب نیک»\", \"verdict\": \"disputed\",\n \"derivation\": \"Nourai's source here is Asbaghi's Persische Lehnwörter im Arabischen (1988) p. 27, which ends its entry on Arabic ʾanbīq with 'wahrscheinlich aus dem pers. آبنیک ābnīk' — i.e. a supposed compound آب آb 'water' + نیک nīk 'good' = 'good water', hence 'distillate'. The word, however, is not attested: it is in neither Borhan-e Qate' (checked vols 1-4), nor Mo'in, nor Dehkhoda, and Asbaghi offers no citation for it. Nourai's own question mark ('good (distilled) water?') registers the doubt. Against this stands a solid tradition — Klein p. 47, Skeat s.v. Alembic, Funk & Wagnalls, Lokotsch no. 79, Devic p. 5, Pihan p. 16, Etymonline and Wiktionary — which derives Arabic al-anbīq from Greek ἄμβιξ (via Classical Syriac ܐܡܒܝܩܐ ʾambīqā), a word already used of distilling gear by Greek alchemists (Dioscorides, Zosimus) centuries before New Persian existed. Even Nourai's other reference for the box below (WEB:44) makes the Greek word the source, not the descendant. The chart's arrows out of this node (to Greek and to Arabic) are therefore drawn the wrong way round, and the node itself rests on a single, unsupported conjecture. Note also that formations of this shape do exist in Persian and were borrowed into Arabic — Asbaghi p. 145 has Arabic barnī 'a fine kind of date' from Persian bar-nīk 'good fruit' — so āb-nīk is possible in principle, but there is no evidence it was ever said.\",\n \"derivation_fa\": \"تکیه‌گاه نورایی در اینجا اصباغی در وام‌واژه‌های فارسی در عربی (۱۹۸۸، ص ۲۷) است که می‌نویسد «احتمالاً از فارسی آبنیک». امّا واژهٔ «آبنیک» در هیچ منبع فارسی — نه برهان قاطع، نه معین، نه دهخدا — شاهد ندارد و خود نورایی هم پس از معنا علامت سوال گذاشته است. در برابر، کلاین (ص ۴۷)، اسکیت، لوکوتش (مادهٔ ۷۹)، دویک، پیان، اتیمولاین و ویکی‌واژه همه «الأنبیق» را وام‌گرفته از یونانی ἄμβιξ (به‌واسطهٔ سریانی ʾambīqā) می‌دانند؛ واژهٔ یونانی قرن‌ها پیش از پیدایش فارسی نو در متون کیمیاگری به کار رفته بود. پس جهت پیکان‌ها در نمودار وارونه است: پژوهش امروزی این ادعا را رد می‌کند. (البته ساخت‌هایی از این گونه در فارسی ممکن است؛ مانند عربی «برنی» از فارسی bar-nīk «میوهٔ نیک»، اصباغی ص ۱۴۵.)\",\n \"sources\": [\"https://www.etymonline.com/word/alembic\", W+\"%D8%A5%D9%86%D8%A8%D9%8A%D9%82\"],\n \"ref_check\": [\n   {\"ref\": \"PLA:27\", \"status\": \"supports\", \"note\": \"Asbaghi 1988 p. 27 (PLA_pages.txt lines 1888-1930), s.v. ʾanbīq: 'ʾambīq: ‚Alembik‘ pers.⁸, mand. anpaga (iranian, talm. אמביק)⁹, syr. ...¹⁰, sp. alambique, engl. alembic, frz. alambic, dtsch. Alembik ‚Destillierkolben‘¹¹, wahrscheinlich aus dem pers. آبنیک ābnīk.' The page says what Nourai's arrow says (with 'wahrscheinlich'), and gives no supporting attestation.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein p. 47 s.v. alembic (KLN_1966.txt line 2149)\", \"stance\": \"contradicts\",\n    \"note\": \"'alembic, n. — ME., fr. OF. (=F.) alambic, fr. OSp. (=Sp.) alambique fr. Arab. al-anbīq, “the still”, which is formed fr. al-, “the”, and Gk. ἄμβιξ, “cup, cap of a still, alembic”, which is of uncertain, possibly Semitic origin.' No Persian source at all.\"},\n   {\"src\": \"LKT\", \"where\": \"Lokotsch no. 79, p. 8 (LKT.txt lines 399-402)\", \"stance\": \"contradicts\",\n    \"note\": \"'79. Ar. anbīk: [Das selbst aus gr. ἄμβιξ in der Aussprache ambīk] ‚Destilliergeräß‘. Hieraus z. T. mit, z. T. ohne ar. Art. lat. alambicum und die romanischen Formen ...' — Greek is the source of the Arabic word.\"},\n   {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' ed. Mo'in, grep آبنیک / آب نیک in BQT_v1_pages.txt, BQT_v2_pages.txt, BQT_v3_pages.txt, BQT_v4_pages.txt\", \"stance\": \"silent\",\n    \"note\": \"No such headword; the compound is not lexicalised in the Persian dictionary tradition.\"},\n   {\"src\": \"MON\", \"where\": \"Mo'in, grep آبنیک in MON_part1.txt / MON_part2.txt\", \"stance\": \"silent\", \"note\": \"No entry for آبنیک.\"}\n ]\n})\n\nN.append({\n \"id\": 5, \"lang\": \"Greek\", \"words\": \"ambix\", \"verdict\": \"disputed\",\n \"derivation\": \"The word itself is real and Nourai's gloss is accurate: Ancient Greek ἄμβιξ (ámbix), gen. ἄμβικος, means 'spouted cup' and then 'the head/cap of a still, alembic', the part fitted over the cucurbit to catch the vapour. What is wrong is the arrow: ἄμβιξ is not a loan from Persian. Wiktionary (following Frisk/Chantraine) says 'the suffix is no doubt a substrate element, as it is in κύλιξ', that it is 'often connected with ἄμβη (“raised edge”) and ἄμβων (“crest of a hill”), but this remains uncertain', and lists it among Greek words of unknown etymology; the descendants it names are Modern Greek άμβικας, Classical Syriac ʾambīqā, Arabic إنبیق and English ambix — no Iranian anywhere. Klein calls it 'of uncertain, possibly Semitic origin', Skeat compares Greek ἄμβη/ἄμβων 'foot of a goblet' and Latin umbo. Nourai's own reference, Webster's, states 'Gr. ambix, a cup of a still' as the ultimate source of the Arabic word, not as a borrowing from Persian.\",\n \"derivation_fa\": \"خود واژه درست است: یونانی باستان ἄμβιξ (جمع مضافی ἄμβικος) به معنای «جامی لوله‌دار» و سپس «سرپوش دستگاه تقطیر» است. امّا جهت پیکان نادرست است؛ این واژه وام‌واژهٔ فارسی نیست. ویکی‌واژه (به پیروی فریسک و شانترین) پسوند آن را عنصری از زبان زیرلایهٔ پیش‐یونانی می‌داند (مانند κύλιξ) و پیوند آن را با ἄμβη و ἄμβων نامطمئن می‌شمارد؛ بازمانده‌های آن را یونانی نو، سریانی، عربی و انگلیسی می‌شمارد و هیچ زبان ایرانی در میان نیست. کلاین آن را «نامعلوم، احتمالاً سامی» می‌داند. نکتهٔ گویا این‌که مرجع خود نورایی (وبستر، ص ۴۴) هم یونانی را سرچشمه می‌داند، نه وام‌گیرنده. پژوهش امروزی این ارتباط را رد می‌کند.\",\n \"sources\": [W+\"%E1%BC%84%CE%BC%CE%B2%CE%B9%CE%BE\", \"https://www.etymonline.com/word/alembic\"],\n \"ref_check\": [\n   {\"ref\": \"WEB:44\", \"status\": \"contradicts\", \"note\": \"Webster's New Twentieth Century Dictionary, 2nd ed., s.v. a-lem'bic (WEB_vol1.txt line 5377): '[L. alambicus; Ar. alanbiq; al, the, and anbiq, Per. ambiq, a still; Gr. ambix, a cup of a still.]' The gloss Nourai prints ('a cup used in distilling water') is Webster's, but Webster puts Greek at the END of the chain as the source, with Persian ambiq (not ābnīk) merely as a link between Greek and Arabic — the reverse of Nourai's arrow. (The 1962 vol. 1 OCR carries no page markers, so p. 44 could not be confirmed directly, but the entry text is verbatim what Nourai cites.)\"}\n ],\n \"consulted\": [\n   {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict., s.v. Alembic (SKT.txt line 527)\", \"stance\": \"contradicts\",\n    \"note\": \"'Alembic, a vessel for distilling. (F. – Span. – Arab. – Gk.) M.E. alembik ... Span. alambique. – Arab. al, the; and anbīq (pronounced ambīq), a still. – Gk. ἄμβιξ, a cup, goblet; cap of a still. – Gk. ἄμβη, ἄμβων, foot of a goblet; allied to L. umbo, a boss.' Skeat even offers a Greek-internal etymology for ambix.\"},\n   {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls, s.v. alembic (FSD_vol1.txt line 11559)\", \"stance\": \"contradicts\",\n    \"note\": \"'[< F. alambic, < LL. alambiscus, < Ar. al-anbīq, < al, the, + Gk. ἄμβιξ, cup]'.\"},\n   {\"src\": \"PHN\", \"where\": \"Pihan p. 16 s.v. ALAMBIC (PHN.txt lines 1095-1104)\", \"stance\": \"contradicts\",\n    \"note\": \"'Les étymologistes s'accordent à regarder alambic comme la transcription du grec ἄμβιξ, vase à bords relevés, précédé de l'article arabe al. Cependant il est probable que les chimistes ont emprunté directement ce terme aux Arabes, qui sans doute l'avaient tiré de la langue grecque.'\"}\n ]\n})\n\nN.append({\n \"id\": 6, \"lang\": \"Arabic\", \"words\": \"al-anbîq, al-ambîq\", \"verdict\": \"disputed\",\n \"derivation\": \"Arabic الأنبیق al-anbīq (also إنبیق inbīq, and with the assimilation n > m before b the pronunciation al-ambīq) 'still, alembic' is genuine and correctly glossed, and it is the word that spread through Europe. Its origin, though, is Greek, not Persian āb-nīk: Wiktionary (s.v. إنبیق) says flatly 'Borrowed from Ancient Greek ἄμβιξ (ámbix), allegedly via Classical Syriac', and the Syriac intermediary ʾambīqā is attested (as is Mandaic anpaga and Talmudic אמביק, which Asbaghi himself lists). Etymonline: 'from Arabic al-anbiq “distilling flask”, via Persian, from Greek ambix “cup”' — note that even where a Persian link is admitted, Persian is the transmitter of the Greek word, not its origin. The Arabic form has no Arabic root and the shape ʾanbīq matches a Greek ámbik- with prothetic ʾ + the regular Arabic rendering of Greek -ιξ as -īq. Nourai's own NOTE ('May have been derived from Greek \\\"ambix\\\" which is related to the Persian word') half-concedes this; modern scholarship takes the Greek side of that note and drops the Persian half.\",\n \"derivation_fa\": \"عربی الأنبیق / إنبیق (و با همگونی ن>م پیش از ب: الأمبیق) واژه‌ای است واقعی و معنای آن درست است؛ همین واژه بود که به اروپا راه یافت. ولی خاستگاه آن یونانی است نه «آب‐نیک» فارسی: ویکی‌واژه می‌نویسد «وام‌گرفته از یونانی باستان ἄμβιξ، به گفتهٔ برخی به‌واسطهٔ سریانی»، و صورت سریانی ʾambīqā و مندایی anpaga و تلمودی אמביק (که خود اصباغی نیز می‌آورد) گواه آن است. اتیمولاین می‌نویسد «از عربی al-anbiq، به‌واسطهٔ فارسی، از یونانی ambix» — یعنی فارسی نقش واسطه دارد نه خاستگاه. ریشهٔ عربی برای أنبیق در کار نیست و وزن آن دقیقاً برابر گرداندن یونانی ámbik- است. یادداشت خود نورایی نیمی از این را پذیرفته است؛ پژوهش امروزی همان نیمهٔ یونانی را می‌پذیرد و نیمهٔ فارسی را کنار می‌گذارد.\",\n \"sources\": [W+\"%D8%A5%D9%86%D8%A8%D9%8A%D9%82\", W+\"%D8%A3%D9%86%D8%A8%D9%8A%D9%82\", \"https://www.etymonline.com/word/alembic\"],\n \"ref_check\": [\n   {\"ref\": \"WEB:44\", \"status\": \"partial\", \"note\": \"Webster's s.v. alembic (WEB_vol1.txt line 5377) gives 'Ar. alanbiq; al, the, and anbiq, Per. ambiq, a still; Gr. ambix, a cup of a still' — it does put a Persian form in the chain (ambīq, not ābnīk) but as an intermediary between Greek and Arabic, so it supports the existence of a Persian link while contradicting the direction of Nourai's derivation.\"},\n   {\"ref\": \"PLA:27\", \"status\": \"supports\", \"note\": \"Asbaghi p. 27 s.v. ʾanbīq: '... wahrscheinlich aus dem pers. آبنیک ābnīk' — the one reference that does say what Nourai's arrow says. The same entry, however, lists mand. anpaga, talm. אמביק and syr. ʾambīqā, which are the Aramaic reflexes of the Greek word.\"},\n   {\"ref\": \"TAD:4\", \"status\": \"not_found\", \"note\": \"cited only in the box's NOTE. Tobia al-Unaysi, Tafsir al-alfaz al-dakhila (1932) is on disk as TAD_pages.txt/TAD.txt, but grep for انبیق / أنبيق / الأنبيق returns nothing (the Arabic OCR of this 86-leaf scan is patchy); the entry could not be located.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein p. 47 s.v. alembic (KLN_1966.txt line 2149)\", \"stance\": \"contradicts\",\n    \"note\": \"'fr. Arab. al-anbīq, “the still”, which is formed fr. al-, “the”, and Gk. ἄμβιξ ... of uncertain, possibly Semitic origin.'\"},\n   {\"src\": \"DEV\", \"where\": \"Devic p. 5 s.v. Alambic (DEV.txt line 270)\", \"stance\": \"contradicts\",\n    \"note\": \"'Alambic. Esp. alambique, port. lambique, ital. lambico, de l'arabe al-anbīq, venant du grec ἄμβιξ vase à distiller, précédé de l'article arabe al.'\"},\n   {\"src\": \"LKT\", \"where\": \"Lokotsch no. 79, p. 8 (LKT.txt line 399)\", \"stance\": \"contradicts\",\n    \"note\": \"'Ar. anbīk: [Das selbst aus gr. ἄμβιξ in der Aussprache ambīk] ‚Destilliergeräß‘.'\"},\n   {\"src\": \"FVQ\", \"where\": \"Jeffery, Foreign Vocabulary of the Qur'an (grep anbīq/ambīq in FVQ_pages.txt)\", \"stance\": \"silent\",\n    \"note\": \"Not a Qur'anic word, so absent — as expected.\"},\n   {\"src\": \"AFA\", \"where\": \"Fraenkel, Die aramäischen Fremdwörter im Arabischen (grep anbiq/ambiq/Destillier in AFA.txt)\", \"stance\": \"silent\",\n    \"note\": \"No hit in the OCR; Fraenkel's book covers pre-Islamic Aramaisms and does not treat this alchemical term.\"}\n ]\n})\n\nN.append({\n \"id\": 7, \"lang\": \"Persian\", \"words\": \"anbîq «انبیق»\", \"verdict\": \"confirmed\",\n \"derivation\": \"New Persian انبیق anbīq 'still, retort' is the Arabic أنبیق taken over with the article dropped, as regularly happens with Arabic technical vocabulary entering Persian through the scientific literature (compare اکسیر < al-iksīr, کیمیا < al-kīmiyā). Mo'in's dictionary marks it '[ع. معر.]' — Arabic, and itself an Arabicised (foreign) word — and defines it 'ظرفی است برای تقطیر مایعات و گرفتن عصاره و عرق', exactly Nourai's 'distilling apparatus'. So the arrow Arabic → Persian is right; on Nourai's overall scheme it would be a round trip (Persian ābnīk → Arabic → Persian), but since the ābnīk step fails, انبیق is simply an Arabic loan of ultimately Greek origin. The Persian form ambīq that Webster's cites is the same word with n > m assimilation.\",\n \"derivation_fa\": \"«انبیق» فارسی وام‌واژهٔ عربی أنبیق است که بدون حرف تعریف وارد فارسی شده است؛ همان‌گونه که «اکسیر» و «کیمیا» از راه متون علمی و کیمیاگری به فارسی راه یافتند. معین این واژه را با نشانهٔ «[ع. معر.]» می‌آورد و معنای آن را «ظرفی است برای تقطیر مایعات و گرفتن عصاره و عرق» داده است. پس پیکان عربی ← فارسی درست است؛ منتها در طرح نورایی این باید بازگشت واژه‌ای فارسی از راه عربی باشد، درحالی که چون حلقهٔ «آبنیک» مردود است، این تنها یک معرّب از اصل یونانی است.\",\n \"sources\": [W+\"%D8%A5%D9%86%D8%A8%D9%8A%D9%82\"],\n \"ref_check\": [\n   {\"ref\": \"MON:362\", \"status\": \"partial\", \"note\": \"The entry is there: 'انبیق: [ع. معر.] (اِ.) ظرفی است برای تقطیر مایعات و گرفتن عصاره و عرق.' (MON_part1.txt line 17169, the 2-vol Adena condensation of Mo'in). It confirms the word and its gloss and tags it as Arabic/Arabicised, but Mo'in gives no source language, and the 6-vol pagination (p. 362) cannot be checked because no scan of the 6-vol Amir Kabir edition is available (see refs_online.json).\"}\n ],\n \"consulted\": [\n   {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' ed. Mo'in, grep انبیق in BQT_v1_pages.txt (آ–ت)\", \"stance\": \"silent\",\n    \"note\": \"The 17th-c. Borhan does not lemmatise this technical Arabism.\"},\n   {\"src\": \"MON\", \"where\": \"Mo'in s.v. انبیق (MON_part1.txt line 17169)\", \"stance\": \"supports\",\n    \"note\": \"'[ع. معر.]' = Arabic, muʿarrab — i.e. an Arabic word which is itself a borrowing; the Persian word is therefore a loan from Arabic, as the chart draws it.\"},\n   {\"src\": \"PLA\", \"where\": \"Asbaghi p. 27 (PLA_pages.txt line 1928)\", \"stance\": \"partial\",\n    \"note\": \"Asbaghi lists 'pers.' among the forms of the word, i.e. he knows a Persian anbīq; his claim is only about the ultimate source.\"}\n ]\n})\n\nN.append({\n \"id\": 8, \"lang\": \"Spanish\", \"words\": \"alambique\", \"verdict\": \"confirmed\",\n \"derivation\": \"Spanish alambique 'still' was taken over from Andalusi Arabic al-ʾanbīq with the article agglutinated, the standard pattern for Arabisms in Ibero-Romance (al-gebra > álgebra, al-quṭun > algodón); Old Spanish alambique is first at home in the alchemical and pharmaceutical vocabulary of the 13th-14th centuries, and Portuguese lost the al- (lambique), as did Italian (lambicco). Klein p. 47 gives the chain 'ME., fr. OF. (=F.) alambic, fr. OSp. (=Sp.) alambique fr. Arab. al-anbīq'; Lokotsch no. 79 lists 'sp. alambique' among the Romance reflexes of Arabic anbīk. So the Arabic-to-Spanish arrow of the chart is exactly right; only the pedigree of the Arabic word (see node 6) is at issue.\",\n \"derivation_fa\": \"اسپانیایی alambique از عربی اندلسی al-ʾanbīq گرفته شده، با همان الگوی رایج که حرف تعریف «al-» به واژه می‌چسبد (الجبر > álgebra، القطن > algodón). این واژه در متون کیمیاگری و داروسازی سدهٔ هفتم و هشتم هجری جا گرفته است؛ در پرتگالی و ایتالیایی بدون al- (lambique، lambicco) مانده است. کلاین (ص ۴۷) و لوکوتش (مادهٔ ۷۹) هر دو همین زنجیره را می‌آورند. ادعای نورایی در این حلقه درست است.\",\n \"sources\": [\"https://www.etymonline.com/word/alembic\"],\n \"ref_check\": [\n   {\"ref\": \"KLN:47\", \"status\": \"supports\", \"note\": \"Klein s.v. alembic, p. 47 (KLN_1966.txt line 2149, between the page markers 46 at line 2142 and 49 at line 2186): 'ME., fr. OF. (=F.) alambic, fr. OSp. (=Sp.) alambique fr. Arab. al-anbīq, “the still” ... Cp. It. lambicco, which is of the same origin as Sp. alambique.'\"}\n ],\n \"consulted\": [\n   {\"src\": \"LKT\", \"where\": \"Lokotsch no. 79, p. 8 (LKT.txt lines 399-402)\", \"stance\": \"supports\",\n    \"note\": \"'... die romanischen Formen: it. lambicco, lambiccio, limbiccio ‚Destillierkolben‘ ... prov. alambic, frz. alambic, rum. alambic, sp. alambique, pg. lambique; engl. alembic.'\"},\n   {\"src\": \"DEV\", \"where\": \"Devic p. 5 s.v. Alambic (DEV.txt line 270)\", \"stance\": \"supports\",\n    \"note\": \"'Esp. alambique, port. lambique, ital. lambico, de l'arabe al-anbīq ...'\"},\n   {\"src\": \"PHN\", \"where\": \"Pihan p. 16 (PHN.txt line 1104)\", \"stance\": \"supports\",\n    \"note\": \"'Les Espagnols et les Portugais écrivent alambique.'\"}\n ]\n})\n\nN.append({\n \"id\": 9, \"lang\": \"French\", \"words\": \"alambic\", \"verdict\": \"confirmed\",\n \"derivation\": \"French alambic is attested from the 13th century (Old French alambic, alembic) and comes, as Klein p. 47 and Etymonline both say, from Old Spanish alambique — the route by which most Arabic alchemical terms reached France. The box's NOTE 'May be through Latin \\\"alambicum\\\"' is well founded: Medieval Latin alambicum/alembicum (also alambiscus in the Funk & Wagnalls chain) is the form used in the Latin alchemical corpus translated from Arabic in 12th-13th c. Spain, and Lokotsch no. 79 explicitly derives the Romance forms from 'lat. alambicum'. So Spanish, Medieval Latin and French are essentially one transmission event in the Toledo translation milieu rather than a strict sequence, and both the arrow and the note are acceptable.\",\n \"derivation_fa\": \"فرانسوی alambic از سدهٔ ۱۳م میلادی گواهی دارد و بر پایهٔ کلاین (ص ۴۷) و اتیمولاین از اسپانیایی باستان alambique گرفته شده است — همان راهی که بیشتر اصطلاحات کیمیاگری عربی به فرانسه رسیدند. یادداشت نورایی دربارهٔ لاتین alambicum پذیرفتنی است: لاتین میانه alambicum/alembicum در ترجمه‌های لاتینی متون عربی در اسپانیای سدهٔ ۱۲–۱۳ م، به‌کار می‌رفت و لوکوتش نیز صورت‌های رومانس را از همین می‌گیرد. پس این حلقه درست است.\",\n \"sources\": [\"https://www.etymonline.com/word/alembic\"],\n \"ref_check\": [\n   {\"ref\": \"KLN:47\", \"status\": \"supports\", \"note\": \"Klein p. 47 s.v. alembic: 'ME., fr. OF. (=F.) alambic, fr. OSp. (=Sp.) alambique fr. Arab. al-anbīq' — exactly Spanish > French.\"}\n ],\n \"consulted\": [\n   {\"src\": \"LKT\", \"where\": \"Lokotsch no. 79, p. 8 (LKT.txt lines 399-402)\", \"stance\": \"supports\",\n    \"note\": \"'Hieraus z. T. mit, z. T. ohne ar. Art. lat. alambicum und die romanischen Formen ... prov. alambic, frz. alambic ... Vb. frz. alambiquer ‚destillieren‘' — confirms the Medieval Latin alambicum of Nourai's note.\"},\n   {\"src\": \"DEV\", \"where\": \"Devic p. 5 (DEV.txt line 270)\", \"stance\": \"supports\", \"note\": \"French Alambic derived from the Arabic through Spanish/Italian.\"},\n   {\"src\": \"LAM\", \"where\": \"Lammens, Remarques sur les mots français dérivés de l'arabe (LAM.txt lines 1610, 6982)\", \"stance\": \"partial\",\n    \"note\": \"Lammens lists alambic among the French words with the agglutinated Arabic article ('ils ont accolé leur [article] ... pour almageste, alchimie, alambic') and among alchemical borrowings ('les élixirs ... les alambics'), without discussing the Greek/Persian question.\"}\n ]\n})\n\nN.append({\n \"id\": 10, \"lang\": \"English\", \"words\": \"alembic\", \"verdict\": \"confirmed\",\n \"derivation\": \"English alembic is a Middle English borrowing of Old French alambic, first recorded late 14c. (Chaucer's Canon's Yeoman's Tale has 'alambikes'), with the aphetic variant limbec/limbeck current from the mid-14c. to the 17c. The -a- of the French form was raised to -e- in the English spelling under the influence of the Medieval Latin alembicum. Klein and Etymonline give the same chain; the box carries no reference of its own, which is unproblematic for such a well-known Romance-to-English link.\",\n \"derivation_fa\": \"انگلیسی alembic در انگلیسی میانه از فرانسوی باستان alambic وام گرفته شده و نخستین گواهی آن پایان سدهٔ ۱۴م است (چاوسر: alambikes)؛ صورت کوتاه‌شدهٔ limbec نیز از میانهٔ سدهٔ ۱۴م تا سدهٔ ۱۷م رواج داشت. تبدیل a به e در نوشتار انگلیسی به تأثیر لاتین میانهٔ alembicum است. کلاین و اتیمولاین همین زنجیره را می‌دهند. ادعای نورایی درست است.\",\n \"sources\": [\"https://www.etymonline.com/word/alembic\"],\n \"ref_check\": [\n   {\"ref\": \"None (box prints no reference)\", \"status\": \"not_checked\", \"note\": \"The English box carries no refs=; the link is covered by KLN:47 in the two boxes above.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein p. 47 s.v. alembic; p. 891 s.v. limbec (KLN_1966.txt lines 2149, 21755)\", \"stance\": \"supports\",\n    \"note\": \"'alembic, n. — ME., fr. OF. (=F.) alambic ...' and 'limbec, n., alembic (archaic). — Aphetic for alembic.'\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. Alembic (SKT.txt line 527)\", \"stance\": \"supports\",\n    \"note\": \"'Alembic, a vessel for distilling. (F. – Span. – Arab. – Gk.) M.E. alembik ... F. alembique (Cot.)'.\"},\n   {\"src\": \"WEB\", \"where\": \"Webster's 2nd ed. s.v. a-lem'bic (WEB_vol1.txt lines 5377-5386)\", \"stance\": \"supports\",\n    \"note\": \"'a chemical apparatus formerly used in distillation ... The bottom part, containing the substance to be distilled, was called the cucurbit; the upper part which received and condensed the steam was called the head' — the English word and its referent.\"}\n ]\n})\n\nN.append({\n \"id\": 11, \"lang\": \"Persian\", \"words\": \"rŭnîk «رونیک ( نیکرو )»\", \"verdict\": \"disputed\",\n \"derivation\": \"This node reproduces Addi Shir's explanation of Arabic rawnaq: 'al-rawnaq, the beauty of everything; compounded of rū, i.e. face, and nīk, i.e. fair, handsome' (al-Alfāẓ al-fārisiyya al-muʿarraba, 1908, p. 74). The second element is indeed نیک nīk of the box above, and the compound with the elements reversed — نیکرو nīk-rū 'fair-faced', which Nourai prints as the variant — is a perfectly ordinary and well attested Persian word. But رونیک rū-nīk in that order is not a Persian word at all: there is no such headword in Borhan-e Qate' (checked vols 1-4), in Mo'in, or in Dehkhoda, and Addi Shir cites no text for it. It is a back-formation invented to explain the Arabic word, and modern Arabists do not follow him: Asbaghi's 1988 monograph on Persian loanwords in Arabic, which is the current standard and which Nourai uses elsewhere on this very page, has no entry for rawnaq at all. The node is therefore rejected as an unattested reconstruction. EXTRACTION ERROR: the JSON gives this node parent #6 (Arabic al-anbīq); on the printed page the arrow into the rŭnîk box comes from the long vertical connector that descends from the Persian nîk box (#3), which is also the only reading that makes sense (see the crops saved as data/verification/sources/refs/ocr/BOOK/355-connector.png and 355-runik.png).\",\n \"derivation_fa\": \"این خانه همان سخن أدّی شیر است که در صفحهٔ ۷۴ می‌نویسد: «(الرَونَق) حُسنُ کلّ شیء. مرکّب من رُو ای وجه ومن نَیک ای صبیح حسن». جزء دوم همان «نیک» است و صورت وارونهٔ آن، یعنی «نیکرو»، در فارسی کاملاً معمول و مستند است؛ امّا «رونیک» با این ترتیب در هیچ فرهنگ فارسی — برهان قاطع، معین، دهخدا — مدخل ندارد و خود أدّی شیر نیز شاهدی نمی‌آورد؛ ساخته‌ای است برای توجیه واژهٔ عربی (ریشه‌شناسی عامیانه). اصباغی در وام‌واژه‌های فارسی در عربی (۱۹۸۸) هیچ مدخلی برای «رونق» ندارد. پژوهش امروزی این مدخل را رد می‌کند. نکتهٔ دیگر: در دادهٔ استخراج‌شده پدر این خانه را خانهٔ شمارهٔ ۶ (عربی الأنبیق) نوشته‌اند، درحالی که در صفحهٔ چاپی پیکان از خط عمودی بلندی می‌آید که از خانهٔ «نیک» (شمارهٔ ۳) فرود می‌آید — خطای خوانش اسکن.\",\n \"sources\": [\"https://abadis.ir/fatofa/%D8%B1%D9%88%D9%86%DB%8C%DA%A9/\", W+\"%D8%B1%D9%88%D9%86%D9%82\"],\n \"ref_check\": [\n   {\"ref\": \"None (box prints no reference)\", \"status\": \"not_checked\", \"note\": \"The rŭnîk box carries no refs=; its substance comes from AFM:74, cited in the Arabic box below (and verified there).\"}\n ],\n \"consulted\": [\n   {\"src\": \"AFM\", \"where\": \"Addi Shir 1908, p. 74 s.v. الرَونَق (read from the page image; transcript saved at data/verification/sources/refs/ocr/AFM/74.vision.txt)\", \"stance\": \"supports\",\n    \"note\": \"'ـ (الرَونَق) حُسنُ کلّ شیء। مرکّب من رُو ای وجه ومن نَیک ای صبیح حسن' — the only source for the reconstruction, and the source of Nourai's node.\"},\n   {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' ed. Mo'in, grep رونیک in BQT_v1/v2/v3/v4_pages.txt\", \"stance\": \"silent\",\n    \"note\": \"No headword رونیک anywhere in the five volumes' OCR.\"},\n   {\"src\": \"MON\", \"where\": \"Mo'in, grep رونیک in MON_part1/part2.txt; Dehkhoda and Mo'in via abadis.ir/fatofa/رونیک/\", \"stance\": \"silent\",\n    \"note\": \"No dictionary entry for رونیک in Dehkhoda or Mo'in (the abadis page returns only user-submitted notes and no lexicon article).\"},\n   {\"src\": \"PLA\", \"where\": \"Asbaghi 1988, grep رونق / rawnaq / raunaq in PLA_pages.txt\", \"stance\": \"contradicts\",\n    \"note\": \"The standard modern monograph on Persian loanwords in Arabic has no entry for rawnaq — i.e. Asbaghi does not accept it as a Persian word, although he does accept comparable compounds with nīk (p. 145: 'barnī: ‚feine Dattelart‘ aus dem pers. bar-nīk ‚gute Frucht‘').\"}\n ]\n})\n\nN.append({\n \"id\": 12, \"lang\": \"Arabic\", \"words\": \"raonaq\", \"verdict\": \"disputed\",\n \"derivation\": \"Arabic رَونَق rawnaq 'beauty, lustre, splendour' is a real and old Arabic word (rawnaq al-ḍuḥā 'the brightness of the forenoon', rawnaq al-sayf 'the sheen of the sword'), so the box's form and gloss are right. The derivation from a Persian rū-nīk is what fails. Addi Shir (p. 74) proposed it in 1908 and Emam Shushtari repeated it, but no modern authority follows: Wiktionary's entry gives the Arabic word no foreign etymology at all and treats the Persian رونق as a borrowing from it; Asbaghi's Persische Lehnwörter im Arabischen (1988) omits it; and phonologically the Arabic form belongs with the native family of the root r-w-q 'to be clear, limpid' (rāqa 'was clear', rawwaqa 'to clarify, decant', rāʾiq 'limpid'), the -n- being the familiar quadriliteral infix (cf. the doublet rāwūq 'strainer', which Addi Shir on the very next page derives from Persian rāwūk following Fraenkel p. 165). A Persian etymology for rawnaq is therefore a minority nineteenth/early-twentieth-century opinion that modern scholarship rejects.\",\n \"derivation_fa\": \"عربی رَونَق به معنای «زیبایی، جلوه، فروغ» واژه‌ای کهن و اصیل عربی است (رونق الضّحی، رونق السیف)؛ پس صورت و معنای خانه درست است، امّا گرفتن آن از «رونیک» فارسی پذیرفتنی نیست. أدّی شیر (۱۹۰۸) و امام شوشتری این را گفته‌اند، ولی مرجع امروزی‌ای آن را نپذیرفته است: ویکی‌واژه برای رونق عربی ریشهٔ بیگانه نمی‌آورد و «رونق» فارسی را وام از عربی می‌داند؛ اصباغی نیز آن را نیاورده است. از نطر ساخت، رونق به خانوادهٔ ریشهٔ ر‐و‐ق (راق، روّق، رائق «زلال، صاف») تعلق دارد و «ن» میانی همان افزودهٔ رباعی‌ساز است. پس پژوهش امروزی ادعای نورایی را رد می‌کند.\",\n \"sources\": [W+\"%D8%B1%D9%88%D9%86%D9%82\", \"https://abadis.ir/fatofa/%D8%B1%D9%88%D9%86%D9%82/\"],\n \"ref_check\": [\n   {\"ref\": \"AFM:74\", \"status\": \"supports\", \"note\": \"Addi Shir, al-Alfāẓ al-fārisiyya al-muʿarraba (1908) p. 74 — the printed numeral ٤٧ [۷۴] is on AFM.pdf pdf page 76 (printed = pdf − 2, fixed against ۷۵ on pdf 77) — reads: 'ـ (الرَونَق) حُسنُ کلّ شیء। مرکّب من رُو ای وجه ومن نَیک ای صبیح حسن'. This is exactly Nourai's arrow, and the reference page number is correct. The book's local OCR is unusable (Syriac glyph substitution), so the page image was read and transcribed to data/verification/sources/refs/ocr/AFM/74.vision.txt with the image at .../74.png.\"},\n   {\"ref\": \"FVF:297\", \"status\": \"not_checked\", \"note\": \"Emam Shushtari, Farhang-e Vazheha-ye Farsi dar Zaban-e Arabi (1347) has no local copy and no readable online text (refs_online.json: noorlib page viewer needs a browser; ketabnak needs a login).\"}\n ],\n \"consulted\": [\n   {\"src\": \"PLA\", \"where\": \"Asbaghi 1988 (grep رونق / rawnaq in PLA_pages.txt)\", \"stance\": \"contradicts\",\n    \"note\": \"No entry: the modern standard list of Persian loanwords in Arabic does not include rawnaq.\"},\n   {\"src\": \"MON\", \"where\": \"Mo'in and Dehkhoda via abadis.ir/fatofa/رونق/\", \"stance\": \"contradicts\",\n    \"note\": \"Dehkhoda tags رونق '(ع اِ)' and Mo'in '[ع.]' — both classify it as an Arabic word borrowed into Persian, with no Persian origin claimed.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein (grep rawnaq/raunaq in KLN_1966.txt / KLN_1971.txt)\", \"stance\": \"silent\",\n    \"note\": \"The word has no English derivative, so Klein does not treat it.\"},\n   {\"src\": \"AFA\", \"where\": \"Fraenkel, Die aramäischen Fremdwörter im Arabischen (grep rawnaq in AFA.txt)\", \"stance\": \"silent\",\n    \"note\": \"No hit; Fraenkel does not class rawnaq as a foreign word either.\"}\n ]\n})\n\nN.append({\n \"id\": 13, \"lang\": \"Persian\", \"words\": \"rownaq «رونق»\", \"verdict\": \"confirmed\",\n \"derivation\": \"New Persian رونق rownaq 'splendour, lustre; briskness of trade, prosperity' is a straightforward Arabic loan of rawnaq, adopted with the usual Persian pronunciation of the Arabic diphthong aw as ow. Wiktionary states 'Borrowed from Arabic رَونَق (rawnaq)'; Dehkhoda marks it '(ع اِ)' and Mo'in '[ع.]' — both meaning 'Arabic noun'. The commercial sense Nourai gives ('success'), i.e. رونق گرفتن 'to boom', is a Persian semantic development from 'lustre' to 'brisk trade'. The arrow Arabic → Persian is thus correct; what does not hold is the round trip Nourai builds it into, since the Arabic word is not itself Persian (see node 12).\",\n \"derivation_fa\": \"«رونق» فارسی به معنای «فروغ، جلوه؛ رواج و گرمی بازار» وام‌واژهٔ عربی رَونَق است؛ مصوّت مرکّب aw عربی در تلفّظ فارسی به ow بدل شده است. ویکی‌واژه می‌نویسد «وام‌گرفته از عربی رَونَق»، دهخدا نیز آن را «(ع اِ)» و معین «[ع.]» می‌نشاند. معنای «کامیابی/رواج» که نورایی می‌آورد تحوّل معنایی درون‌فارسی است (از «درخشش» به «گرمی بازار»). پس این پیکان درست است؛ ولی دورهٔ رفت و برگشت فارسی‐عربی‐فارسی که نورایی ترسیم کرده پذیرفتنی نیست، زیرا خود واژهٔ عربی فارسی نیست.\",\n \"sources\": [W+\"%D8%B1%D9%88%D9%86%D9%82\", \"https://abadis.ir/fatofa/%D8%B1%D9%88%D9%86%D9%82/\"],\n \"ref_check\": [\n   {\"ref\": \"MON:1694\", \"status\": \"supports\", \"note\": \"Mo'in s.v. رونق tags the word '[ع.]' (Arabic) and glosses it 'فروغ، روشنایی' (read via abadis.ir/fatofa/رونق/, which reproduces the فرهنگ معین article), so it supports the Arabic → Persian arrow. The 6-vol page number 1694 cannot be verified because no scan of that edition is available; the 2-vol condensation on disk carries رونق only inside compounds.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"Mo'in via abadis.ir/fatofa/رونق/ ; compounds in MON_part2.txt (lines 17331, 18202, 22945)\", \"stance\": \"supports\",\n    \"note\": \"'[ع.] فروغ، روشنایی'; the condensation shows the live Persian idioms رونق و نطام یافتن کار, بی‌رونق، بی‌رواج — i.e. Nourai's 'success' sense.\"},\n   {\"src\": \"BQT\", \"where\": \"Dehkhoda's article on رونق (abadis), which quotes the Persian lexicographic tradition\", \"stance\": \"supports\",\n    \"note\": \"Dehkhoda's headword is marked '(ع اِ)' with the first gloss 'آب کار' — an Arabic noun in Persian use.\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur (grep رونق in ARY_pages.txt)\", \"stance\": \"silent\",\n    \"note\": \"Aryanpur's dictionary of Indo-European roots of Persian has no entry, consistent with the word being an Arabic loan.\"}\n ]\n})\n\nN.append({\n \"id\": 14, \"lang\": \"Latin\", \"words\": \"ni-těre\", \"verdict\": \"confirmed\",\n \"derivation\": \"Latin niteō, nitēre 'to shine, glitter, be sleek' (with nitidus 'shining, sleek, elegant' and nitor 'brightness') is the Italic branch of the same root: Pokorny p. 760, in the same entry that yields Old Persian naiba-, has 'Lat. niteō, -ēre ‚glänze, strahle‘, nitidus ‚glänzend‘, nitor ‚Glanz‘ (von einem Partiz. *ni-tō-)', i.e. the verb is a denominative built on a zero-grade verbal adjective *ni-to- 'made bright'; Watkins/AHD says the same ('Suffixed zero-grade form *ni-to- in Latin nitēre, to shine') and so does de Vaan (2008: 410), 'probably from a past participle Proto-Italic *nitos “made bright”, from PIE *ney- “to shine”', with cognates Middle Irish níam 'splendour, gleam' and Sanskrit nīla- 'dark blue'. Nourai's spelling 'ni-těre' uses the hyphen to isolate the root and his ě for the long ē of the second-conjugation infinitive, the same convention he uses for Pahlavi něv = nēw in this chart, so it is not a misprint; the citation form in the dictionaries is niteō / nitēre. The one caveat is that the root connection, while the standard view, is not certain: Mann files niteō under a separate *noit-/nit- 'kindle, burn brightly', and de Vaan hedges with 'probably'.\",\n \"derivation_fa\": \"لاتین niteō / nitēre «درخشیدن، تابیدن» (با nitidus «درخشان» و nitor «درخشش») شاخهٔ ایتالیکی همان ریشه است. پوکورنی در همان مادهٔ صفحهٔ ۷۶۰ می‌نویسد: «Lat. niteō, -ēre ‚glänze, strahle‘ ... (von einem Partiz. *ni-tō-)»؛ واتکینز نیز «صورت پسونددار صفر‐پایه *ni-to- در لاتین nitēre» و دووان (۲۰۰۸، ص ۴۱۰) «احتمالاً از اسم مفعول ایتالیکی آغازین *nitos «درخشان‌شده»، از هندواروپایی *ney-». نوشتار «ni-těre» در کتاب، خط فاصله را برای جداکردن ریشه و نشانهٔ ٔe را برای ٔe کشیده به کار برده است (همان روشی که در něv = nēw دارد)، پس غلط چاپی نیست. تنها احتیاط: مان (IEC) این فعل را زیر ریشهٔ جداگانهٔ *noit- «افروختن» می‌نشاند. ادعای نورایی درست است.\",\n \"sources\": [W+\"niteo\", \"https://www.etymonline.com/word/neat\"],\n \"ref_check\": [\n   {\"ref\": \"KLN:1033\", \"status\": \"supports\", \"note\": \"Klein s.v. 'neat, adj.', p. 1033 (KLN_1966.txt line 25080; page marker 1033 at line 25059): 'fr. L. nitidus, “shining, bright, clear, well-favored, elegant, smart, trim”, fr. nitere, “to shine”, fr. I.-E. base *nei-, *ni-, “to shine”' — both the Latin verb, its gloss and its attachment to the root, exactly as the chart draws it.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"Pokorny p. 760 s.v. 2. nei- (POK_02.txt line 6665)\", \"stance\": \"supports\",\n    \"note\": \"'Lat. niteö, -ere ‚glänze, strahle‘, nitidus ‚glänzend‘, nitor ‚Glanz‘ (von einem Partiz. *ni-tö-); vielleicht re-nideo ‚erglänzen‘ (mit präsensbildendem -d(h)-)'.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. nei- (AHD_watkins1985.txt line 776)\", \"stance\": \"supports\",\n    \"note\": \"'2. Suffixed zero-grade form *ni-to- in Latin nitere, to shine: NEAT1, (NET2).'\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. niteō (LAT.txt lines 41542-41556)\", \"stance\": \"partial\",\n    \"note\": \"'niteō, -ēs, -uī, -ēre: briller, être luisant, éclatant ... nitidus (fr. net) ... niteō serait bâti sur un adjectif *nitos, comme fateor sur ...' — the *nito- analysis is there, but Ernout-Meillet do not commit to the IE root.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann s.v. noit- (nit-) (1) (IEC.txt line 11808)\", \"stance\": \"partial\",\n    \"note\": \"'noit- (nit-) (1) “inflame, kindle; be inflamed, burn brightly”. Lat. niteo, ere, v. “shine”; cf. nitidus, adj. “bright”' — same forms, different root label.\"}\n ]\n})\n\nN.append({\n \"id\": 15, \"lang\": \"English\", \"words\": \"neat; net 1\", \"verdict\": \"confirmed\",\n \"derivation\": \"Both English words come from Latin nitidus, the adjective of nitēre, by way of Old and Middle French net, nette 'clean, clear, pure' (12c.). Middle English took over net/nete, whence with lengthening the modern spelling neat, first recorded in the sense 'clean, free from dirt' in the 1540s and developing 'well-shaped' (1540s), 'tidy' (1570s), 'orderly' (1590s) and, of spirits, 'undiluted' (c. 1800) — Nourai's gloss 'pure' for net is the earlier of the two senses. The commercial net 'free from all deductions' is the same French word re-borrowed in the mercantile sense ('clear of charges'), which is why Klein and Watkins keep the two as neat¹ and net² under one root. Buck 15.87/17.24 notes the same semantic path for the whole Romance family: 'Bright > clean, neat, as in Lat. nitidus > Fr. net'. This is an uncontroversial Latin > French > English chain.\",\n \"derivation_fa\": \"هر دو واژهٔ انگلیسی از لاتین nitidus — صفت فعل nitēre — و از راه فرانسوی باستان و میانه net, nette «پاک، زلال، خالص» (سدهٔ ۱۲م) آمده‌اند. انگلیسی میانه net/nete را گرفت و سپس به نوشتار neat رسید؛ معنای «پاک، بی‌آلایش» از دههٔ ۱۵۴۰ م و معنای «مرتّب» از دههٔ ۱۵۷۰ گواهی دارد؛ «خالص، رقیق‌نشده» دربارهٔ مشروب از حدود ۱۸۰۰ م. واژهٔ بازارگانی net «خالص، بی کسورات» همان واژهٔ فرانسوی است که دوباره در معنای تجاری وام گرفته شده است؛ از این‌رو کلاین و واتکینز neat¹ و net² را کنار هم زیر یک ریشه می‌آورند. این زنجیره مورد اختلاف نیست و ادعای نورایی درست است. (نباید با neat دیگر، به معنای «گاو، دام» از ریشهٔ جرمنی *neud-، اشتباه شود.)\",\n \"sources\": [\"https://www.etymonline.com/word/neat\", W+\"niteo\"],\n \"ref_check\": [\n   {\"ref\": \"None (box prints no reference)\", \"status\": \"not_checked\", \"note\": \"The English box carries no refs=; the Latin box above cites KLN:1033, which is precisely Klein's entry for 'neat, adj.' and cross-refers to 'net, adj.'\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein p. 1033 s.v. 'neat, adj.' and p. 1035 s.v. 'net, adj.' (KLN_1966.txt lines 25080, 25303)\", \"stance\": \"supports\",\n    \"note\": \"'neat, adj., pure, undiluted; cleanly, tidy; elegant. — MF. (=F.) net, “clean, pure, neat”, fr. OF., fr. L. nitidus ... fr. nitere, “to shine” ... Cp. natty, net, adj., nitid, niton.' and 'net, adj., free from all deductions. — ME., fr. MF. (=F.), “neat, clean”. See neat, “pure”.' Klein also distinguishes the homonym 'neat, n., an animal of the ox family' from I.-E. *neud-.\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. Neat (2) (SKT.txt line 12203)\", \"stance\": \"supports\",\n    \"note\": \"'Neat (2), tidy. (F. – L.) F. net, nette, fem., neat, pure. – L. nitidus, shining, neat. – L. nitere, to shine.'\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 15.87 / 17 (SYN.txt lines 22488, 27334)\", \"stance\": \"supports\",\n    \"note\": \"'It. netto, Fr. net (OFr. neit, net > ME neate, nete “clean, pure, bright”, NE neat), fr. Lat. nitidus “bright, shining, polished” (15.57). REW 5929'; and '“Bright” > “clean, neat”, as in Lat. nitidus > Fr. net, etc.'\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, index and s.v. nei- (AHD_watkins1985.txt lines 776, 1905-06)\", \"stance\": \"supports\",\n    \"note\": \"'NEAT¹ nei-' / 'NEAT² neud-' in the index, and under nei-: '*ni-to- in Latin nitere, to shine: NEAT¹, (NET²)' — exactly Nourai's pair neat / net 1.\"}\n ]\n})\n\nout = {\"pdf_page\": 355, \"book_page\": 325, \"verified_by\": \"claude-opus-5\",\n       \"verified_on\": \"2026-09-07\", \"entries\": [root]}\np = \"/home/sfmqrb/git/rishe/data/verification/page-355.json\"\nwith open(p, \"w\", encoding=\"utf-8\") as f:\n    json.dump(out, f, ensure_ascii=False, indent=2)\nprint(\"wrote\", p, len(json.dumps(out)))\nPYEOF",
 "description": "Write page-355.json"
}
```


### [2026-09-07T18:42:59.023Z] TOOL RESULT

```
wrote /home/sfmqrb/git/rishe/data/verification/page-355.json 97388
```


## [2026-09-07T18:43:02.889Z] TOOL CALL #80: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-355.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 355",
 "description": "Validate JSON and run verify_check"
}
```


### [2026-09-07T18:43:04.327Z] TOOL RESULT

```
JSON OK
nodes verified: 15/15
node verdicts: {'confirmed': 10, 'disputed': 5}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 14, 'contradicts': 2, 'not_found': 2, 'not_checked': 5, 'partial': 2}
books consulted: {'supports': 27, 'partial': 5, 'silent': 11, 'contradicts': 11} | by book: {'MON': 6, 'KLN': 5, 'LKT': 4, 'BQT': 4, 'SKT': 3, 'DEV': 3, 'PLA': 3, 'SYN': 2, 'PHD': 2, 'HRN': 2, 'ARY': 2, 'PHN': 2, 'AFA': 2, 'AHD': 2, 'BRT': 1, 'HUB': 1, 'WLD': 1, 'NYB': 1, 'FSD': 1, 'FVQ': 1, 'LAM': 1, 'WEB': 1, 'AFM': 1, 'POK': 1, 'LAT': 1, 'IEC': 1}
```


## [2026-09-07T18:43:24.636Z] AGENT

Page 355 verified — `data/verification/page-355.json` written, `verify_check.py 355` reports 0 PROBLEM lines (15/15 nodes).

**Verdicts** — root: 1 confirmed. Nodes: 10 confirmed, 5 disputed.

Root `Nei 1, Ni 2` "to shine, to be excited" = Pokorny's **2. nei-** on p. 760 verbatim ("lebhaft bewegt sein, erregt sein, glänzen"; *noi-bʰo- "gut, heilig"), with both drawn branches (OP naiba-, Lat. niteō) in that one entry. Watkins, Walde-Pokorny II, Lidén 59-60, Buck 16.71, Hübschmann, Spiegel 227 and Horn 1068 all confirm the Iranian chain OP naiba- → MP nēw / nēw-ak → NP nīv / nīk; MacKenzie p. 59 and Mo'in's footnote in Borhan 2127 confirm nard < MP nēw-ardaxšīr.

**disputed (5)** — all in the alembic/rawnaq sub-tree:
- #4 Persian `âbnîk` "good water" — unattested (absent from Borhan, Mo'in, Dehkhoda); rests solely on Asbaghi 1988 p. 27 "wahrscheinlich aus dem pers. ābnīk".
- #5 Greek `ambix` — real word, wrong arrow: substrate/unknown etymology (Wiktionary, Klein, Skeat), never a Persian loan; Nourai's own WEB:44 makes Greek the source.
- #6 Arabic `al-anbîq` — from Greek ἄμβιξ via Syriac ʾambīqā (Wiktionary, Etymonline, Klein 47, Lokotsch 79, Devic, Pihan, Skeat, F&W), not from āb-nīk.
- #11 Persian `rŭnîk` «رونیک» — not a Persian word; Addi Shir's 1908 back-formation (the attested compound is نیکرو nīk-rū).
- #12 Arabic `raonaq` — native Arabic (root r-w-q); Wiktionary gives no foreign source, Asbaghi omits it entirely; only Addi Shir 74 and Emam Shushtari claim Persian.

**Extraction error for the owner to fix:** node #11 (`rŭnîk`) has `"parent": 6` in `data/extracted/batch/page-355.json`; on the printed page its arrow comes off the long vertical connector descending from the Persian `nîk` box, i.e. **parent should be 3**. Audit crops saved to `data/verification/sources/refs/ocr/BOOK/355-connector.png` and `355-runik.png`.

**Notes on Nourai's own refs:** KNT:192 *contradicts* him (Kent lists naiba- among OP words "not traceable to pIE forebears"); SNS:291 not_found (entry located at leaf 163 but the scan's page offset is undetermined); TZF:20 and FVF:297 inaccessible; TAD:4 not locatable in the OCR. AFM:74 verified from the page image (local OCR is Syriac garbage) — transcript saved to `data/verification/sources/refs/ocr/AFM/74.vision.txt` + `74.png`/`75.png`. 10 web pages archived via `fetch_source.py`.
