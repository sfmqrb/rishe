# Verification process log — verify-page-129


## [2026-09-05T20:02:37.901Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 129 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-129.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-129.json. Write /home/sfmqrb/git/rishe/data/verification/page-129.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 129` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T20:02:39.426Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T20:02:40.269Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T20:02:40.289Z] TOOL RESULT

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


## [2026-09-05T20:02:40.813Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-129.txt"
}
```


### [2026-09-05T20:02:40.834Z] TOOL RESULT

```
1	=== PDF page 129 (book page 99) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Dher 2, Dherabh, Dhrâbh; Dhragh 2 : to make muddy, unclear, dark; to confuse, disturb  (refs POK:251)
4	#1 (parent #0) [Avestan] refs=POK:252 | driwi 1 : dark birth mark
5	#2 (parent #0) [Germanic] refs=AHD | derk : dark
6	  #3 (parent #2) [English] refs=None | dark
7	#4 (parent #0) [Greek] refs=AHD | traxus : disturbing, rough
8	  #5 (parent #4) [Latin] refs=None | 
9	    #6 (parent #5) [French] refs=None | 
10	      #7 (parent #6) [Persian] refs=MON:1058 | tarâxom «تراخم» : trachoma
11	    #8 (parent #5) [English] refs=None | trachoma
12	--- entry 1 ---
13	ROOT Dherabh -> redirect to Dher 2
14	--- entry 2 ---
15	ROOT Dhers -> redirect to Dhars
16	--- entry 3 ---
17	ROOT [Indo-European] Dheu 1 : to flow  (refs POK:259)
18	#1 (parent #0) [Avestan / Old Persian] refs=FFD:54 | daw : to run
19	  #2 (parent #1) [Pahlavi] refs=POK:259; FFD:54 | davîtan : to run
20	    #3 (parent #2) [Persian] refs=BQT:902; HRN:130 | davîdan «دویدن» : to run | extra: دو ۲ ، دونده ، پادو
21	#4 (parent #0) [Sanskrit] refs=POK:259 | dhav : to run
22	#5 (parent #0) [Germanic] refs=AHD | dauwaz : dew
23	  #6 (parent #5) [English] refs=None | dew
24	
```


## [2026-09-05T20:02:46.074Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-129.json && echo \"=== refs_online keys ===\" && python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','AHD','MON','BQT','HRN','FFD','WLD','IEC','SYN','BRT','KNT','PHD','NYB','HUB','CHEUNG','ARY','KLN','SKT','FSD','WEB']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:400])\n\""
}
```


## [2026-09-05T20:02:46.134Z] TOOL CALL #4: Bash

```json
{
 "command": "sed -n '1,200p' data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-05T20:02:47.930Z] TOOL RESULT

```
{
  "pdf_page": 129,
  "book_page": 99,
  "entries": [
    {
      "root": {
        "name": "Dher 2, Dherabh, Dhrâbh; Dhragh 2",
        "lang": "Indo-European",
        "refs": "POK:251",
        "gloss": "to make muddy, unclear, dark; to confuse, disturb"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:252",
          "words": [
            {"translit": "driwi 1", "gloss": "dark birth mark", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "derk", "gloss": "dark", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "dark", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "traxus", "gloss": "disturbing, rough", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Latin",
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "French",
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Persian",
          "refs": "MON:1058",
          "words": [
            {"translit": "tarâxom", "gloss": "trachoma", "script": "تراخم"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 5,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "trachoma", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Dherabh",
        "redirect": "Dher 2"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Dhers",
        "redirect": "Dhars"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Dheu 1",
        "lang": "Indo-European",
        "refs": "POK:259",
        "gloss": "to flow"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "FFD:54",
          "words": [
            {"translit": "daw", "gloss": "to run", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "POK:259; FFD:54",
          "words": [
            {"translit": "davîtan", "gloss": "to run", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:902; HRN:130",
          "words": [
            {"translit": "davîdan", "gloss": "to run", "script": "دویدن"}
          ],
          "script_extra": "دو ۲ ، دونده ، پادو",
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK:259",
          "words": [
            {"translit": "dhav", "gloss": "to run", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "dauwaz", "gloss": "dew", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "dew", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
=== refs_online keys ===
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/downloa
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
CHEUNG null
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
```


### [2026-09-05T20:02:47.979Z] TOOL RESULT

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


## [2026-09-05T20:03:21.961Z] TOOL CALL #5: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py"
}
```


### [2026-09-05T20:03:22.005Z] TOOL RESULT

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


## [2026-09-05T20:03:22.397Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/page-127.json'))\nprint(json.dumps(d['entries'][0], ensure_ascii=False, indent=1)[:3000])\n\""
}
```


### [2026-09-05T20:03:24.140Z] TOOL RESULT

```
{
 "entry": 0,
 "root": "Dhem",
 "verdict": "confirmed",
 "modern_form": "PIE *dʰemH- (LIV² *dʰmeh₁-) 'to blow, breathe; to smoke, raise dust'",
 "note": "Pokorny IEW 247-248 heads the entry 'dhem-, dhemə- \"stieben, rauchen (Rauch, Dunst, Nebel; nebelgrau, rauchfarben = düster, dunkel), wehen, blasen (hauchen = riechen)\"', so Nourai's language label (Indo-European) and his gloss 'to make vapor, raise dust' are an accurate short rendering of the German. Cheung (Etym. Dict. of the Iranian Verb, *damH³) writes the same root «PIE *dʰmeH- 'to blow' = LIV: 153 | Pok.: 247 f.»; Wiktionary reconstructs *dʰemH-. Watkins/AHD carries no dhem- root (its list goes dhembh- → dhen-¹), simply because no English word reaches it through Latin or Greek, so its silence is not a disagreement. Two weak spots in the chart: the Avestan node's gloss (node 1) and the name Damāvand (node 2), which Nourai's own source BQT:878 derives from a different root.",
 "note_fa": "ریشهٔ نمودار همان ریشهٔ هندواروپاییِ آغازینِ *dʰemH- «دمیدن، فوت کردن؛ دود و بخار برخاستن» است. پوکورنی در صفحهٔ ۲۴۷ کتاب خود آن را با معنای آلمانیِ «stieben, rauchen … wehen, blasen» آورده و برگردانِ کوتاهِ نورایی («بخار ساختن، گرد برانگیختن») با آن می‌خواند؛ چونگ نیز همین ریشه را *dʰmeH- «دمیدن» (LIV ۱۵۳) می‌نویسد. پس جعبهٔ ریشه، برچسبِ زبان و معنای آن درست است و ادعای نورایی در این حد پذیرفتنی است. تنها دو نقطهٔ سست در نمودار هست: معنایی که برای صورتِ اوستایی داده شده (گرهٔ ۱) و نامِ «دماوند» (گرهٔ ۲) که خودِ مأخذِ نورایی، یعنی حاشیهٔ معین بر برهان قاطع ص ۸۷۸، آن را از ریشهٔ دیگری می‌گیرد.",
 "sources": [
  "https://en.wiktionary.org/wiki/%D8%AF%D9%85%DB%8C%D8%AF%D9%86",
  "https://en.wiktionary.org/wiki/%D8%AF%D9%85"
 ],
 "ref_check": [
  {
   "ref": "POK:247",
   "status": "supports",
   "note": "POK_01.txt (grep -n 'dbem-' → line 3513), IEW p.247: 'dbem-, dhemo- ,stieben, rauchen (Rauch, Dunst, Nebel; nebelgrau, rauchfarben == düster, dunkel), wehen, blasen (hauchen = riechen)'; the page continues 'Ai. dhámati ,bläst', av. daδmainya- …, npers. damīdan ,blasen, wehen', dam ,Atem, Atemzug''. Exactly the root box as drawn."
  }
 ],
 "consulted": [
  {
   "src": "WLD",
   "where": "Bd. I 851 f. (WLD_Bd1 djvu line 53642)",
   "stance": "supports",
   "note": "'dhem-, dhemə- „stieben, rauchen (Rauch, Dunst, Nebel; nebelgrau, rauchfarben = düster, dunkel), wehen, blasen (hauchen = riechen)“. Bedeutungsumfang wie bei Wz. *dheu- „stieben“.' — the source Pokorny 247 abridges."
  },
  {
   "src": "CHEUNG",
   "where": "s.v. *damH³ (CHEUNG.txt line 4670 ff.)",
   "stance": "supports",
   "note": "'*damH³ \"to blow, breathe; to swell\" … «PIE *dʰmeH- \"to blow\" > LIV: 153 | Pok.: 247 f.»'"
  },
  {
   "src": "AHD",
   "where": "Watkins 1985, d-list (AHD_watkins1985.txt line 377)",
   "stance": "silent",
   "note": "the appendix runs 'dhembh-. To bury. … [Pok. (dhembh-), dhmbh- 248.] dhen-¹. To run, flow.' — no dhem- entry at all, since no English word descends from it via Latin/Greek."
  },
  {
   "src": "IEC",
```


## [2026-09-05T20:03:30.231Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"dher-2\\|dherobh\\|dhera-bh\\|dhrabh\\|dhragh\\|dhr9bh\" POK_01.txt | head -40; echo \"---- dheu1 ----\"; grep -n \"dheu-1\\|dheu-, dheu\\|dhau-\" POK_01.txt | head -40"
}
```


### [2026-09-05T20:03:30.299Z] TOOL RESULT

```
3586:d.  dherobh-  :  dhräbh-  :  dhrobb-.
3679:Lat.  trahö  .ziehe',  traha  , Schleife',  trägum  ,Schleppnetz',  trägula  ,ds., kleine  Schleife'  können  durch  Spirantendissimilation  {^*dragö  zu  *dragö) auf  dhragh-  zurückgehen,  aber  auch  idg.  t-  haben  (:  air.  traig  ,Fuß'  usw., 8.  trUgh-).
3681:dbcrbh'  (dherobh-?)  ,arbeiten'.
---- dheu1 ----
```


## [2026-09-05T20:03:31.243Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"driwi\\|driwi-\" BRT.txt | head -20; echo \"=== POK driwi ===\"; grep -rn \"driwi\" POK_01.txt POK_02.txt POK_03.txt POK_full.txt 2>/dev/null | head -20"
}
```


### [2026-09-05T20:03:31.331Z] TOOL RESULT

```
14147:Et.?').  —  Pü.  (luV.  2):  drdpk  {Tranistr.), erl. :  ii  darl  ätaaret,  (zu  V.  /.  l) :  atanärai darimil,  erl.;  darim  5  darin  patioail  islel.  — >)  Wegen  JusTis  driwi-  EN.  (NB.  86)  s.  West SBE.  j.  132  No.  6.  —  ')  Cto.s  Hinwei*  auf ai.  dfmbhh-  (GGA.  iSgj.  400)  hilft  nicht  weiter. —  3)  zBed.  vgl.  At.  /?.  12,  wo  aianärai darim  lut  Schilderung  eines  häsilichen  Weibes verwendet  wird;  etwa  'voller  Mutter-  oder Pockenmale'.    S.  noch  'raeia-  No.  2.
14148:•  j,  driwika-  n.  'Stöhnen,  Heulen':  pait- yar^nt  (näml.  fiaraivahe)  fräkinntat  aurS mainyul. . ^sraskpmia  'käca (AP.) "..Weinen und  Stöhnen"'>  V.;.8.
=== POK driwi ===
```


## [2026-09-05T20:03:35.976Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '14130,14150p' BRT.txt"
}
```


### [2026-09-05T20:03:36.030Z] TOOL RESULT

```
y ■  7 1 ;  —  dagva  'vaniö  duzdh»M  V,  ig.  3, »8,33,  44  t*,  47;  —  daivanqm  ..  'va/amW. fi.So.  a)  ««T  K.  von  AraraMainyav^: vahistö  ahurS  matäs  .  .  antamca  'vanipm ämrßta  aya  antari.uxii  (sd.)  Y.  /p.  15;  — hamiitse  .  .  vupaya  'vatB  sisU  Y.  61.  $ (s.  Ol).  «)    im    Gegensatz    zu    asavan-
(Sp.  251  u.):  asaonS  ahmi  'vatö  nöit  ahmt Y. /O.  16;  —  fradahäi  vTspayä  alaonS stöis  hamistSe  vupayh  'vatö  j/Si'/ Y.52.4; Ä  8.  10)  von  ajidem  Schöpfungen  der dafiAschta  Welt  'glaubensfeindlich,  ruch- los'; pairi  'valal  mahrkäl  pairi  °vatai a^mät  pairi  drvafhyö^''  ''kaltabys\.$-].ti, YtJO.  93  (wo  'vataiibyü')''''.
Abteil,  «u  ''drug-,  S  268. 10,  2/j,  IF.  13.  130. —  Vgl.  drujaHl-,  —  mp.  dn-and.  —  Pö. :  drvand. Sq.:  durgaii,  durgalimän.  —  0  Mit  ähn- lichem Gegcnlatz  wie  lu  i.  —  >)  VgL  doli- yhil  yäi  läilärö  drtgTiantö  Y,  46.  1,  femer  zu 'ioDay-,  bhtdva-,  *Ft>hma:  —  3)  Vgl.  Y.  45.  I , 45,  3  ijiacid  drigvt)  und  in  iarafan-,  iiiig-.  — *)  S  a68.  57.  Gani  wertlos  iit  die  Var.  dn/qAyä/, die  NA.  lu  Yt.  r.  iq  aufgenommen  hat.  — S)  Pü.  hat  den  Plural  drvnndän,  ausier  Y.  /o. 16,  wo/o  ÄiJi/reanrf.  —  6)Diemask.  (neutr.) Form  statt  der  fem.,  S  ?Z9.  I,  ^/J.  S.  noch Nu  7,  —  7>  Mask.  (neutr.)  Fonn  -  s.  N0.6  - nach  der  d-Dekl.    Nicht  recht  sicher,  5.  Var.
•  j.  drajä-  f.  Name  eines  Flusses*':  'jya (IS.)  paiti  zbarahi  nmänakt  pourusoipahe "an  der  Z>r.,  auf  dem  Hügel  des  Hauses ^.s"  V.  /p-  4 ;  —  '}ya  paiti  zbarahe  "auf dem  Hügel  an  der  Dr."  V.if).  ii.
•>  über  seine  Lage  s.  Bd.  20.  32:  diraja  (in Aw.-Bochst.) ')  rät  pa  frän  ijii  kls  man  ifaruSasp i  fätar  i  laratiäl  pa  bar  bil.  Weiteres  bei  J«. Zor.   193.
Statt   dir»}-    geschr.,   J  ^6S.  39.    —    »)   Das
Mp.  transskribirt  verschiedentlich,  meist  d  rp.
j.  drrwdaea  Yt.  I3.    11:  lies  drrnnia'a.
•  j.  dranjayant-  Adj.,  PPA.:  s.  'drang-. KompE.
•  j.  drazra-  Adj.:  s.  unter  dirtzra-.
•  j.  drij-av-,  g.  drigav-  :  g.  *dr^u-'^  Adj. (fem.  j.  rfrJrr-)" 'arm,  bedürftig,  schwach': yat  iprsnaoiti  'yaos  havat.masS (sA.)  manS ya^a  ..Y.lO.  13:13;  —yim  *'yBsat  (HS.) *a^.tial^  xbayäti  Yt/o.  84;  —  *'yaos asl>.tkaisaAe  P.  44;  —  ^rJySidyai  (sd.) •gäm  yüwt/lkfm  H.34-1;  —  sraoiB  'yäm 'krijß.t?ms  isA.)  \i..it.y,  —  *'yüm^n  °rT- vTmca  P.  26;  —  ys  -fagim  **rlvayasla " amaval  nmän>m  harnJästi  \.5~.io;  - tat  mäsdä  tavä  x/t^rtm  ya  .'r^hjyöi  däfij 'gaove*^  vahyg  "dein,  o  M.,  ist  die  Herrsch-
gewalt, durch  die  du  dem  rechtlebenden Aimen  das  bessere  Los  verschaffen  wirst" V.5_j,  9;  —  yim  'guiyö  dadat  v3stär?m "er  (Zar.),  den  sie  den  Armen  als  Hirten bestellt  haben"  Y.  27. 13S';  benützt  ip.  14.
KompA.,  E.  —  El  ?  VgL  BEZZENBEKGEit  GGN.
18/S.  267  (5.  aber  Leskieh  Ablaut  324),  Hau.
PSt  6s,  Bloomfield  AJPh.  //.  429.  —  Vgl.
draijiitS.Oma-.  —  mp.  (Pü.)  vgl.  driföi,  (Pjz. darySs),  np.  vgl.  daroii;  s.  IlBM,  aO.  —  Pü. : I.  o.,  Sü. :  dmdri,  durbalak.  —  0  So  gegen NA.  (drig')  fast  alle  guten  Hds.;  Saö^J.gf. — •)  S  268.  1  a,  2/J.  —  J)  S  268.  13,  —K)% 268. 35;  s.  aber  Var.  —  5>  S.  noch  zu  väslar: g.  drTtä  \.  46.  ft:  s.  Idar-.
•  j.  driwray-  f.  'Flecken,  Mal'  (nur Komp.).  a)  bes. 'Muttermal' :  mä  dhra .  .  °wil  . .  mSia.am  anyqm  daxstanqm  ,  . atarahe  mainySuiV.2.3^.  a)  aXsGasva: 'wii'  daevB  V.  ig.  43  '*.  [V.  7. 2 :  lies  aka- ran^mJriwya^
Et.?').  —  Pü.  (luV.  2):  drdpk  {Tranistr.), erl. :  ii  darl  ätaaret,  (zu  V.  /.  l) :  atanärai darimil,  erl.;  darim  5  darin  patioail  islel.  — >)  Wegen  JusTis  driwi-  EN.  (NB.  86)  s.  West SBE.  j.  132  No.  6.  —  ')  Cto.s  Hinwei*  auf ai.  dfmbhh-  (GGA.  iSgj.  400)  hilft  nicht  weiter. —  3)  zBed.  vgl.  At.  /?.  12,  wo  aianärai darim  lut  Schilderung  eines  häsilichen  Weibes verwendet  wird;  etwa  'voller  Mutter-  oder Pockenmale'.    S.  noch  'raeia-  No.  2.
•  j,  driwika-  n.  'Stöhnen,  Heulen':  pait- yar^nt  (näml.  fiaraivahe)  fräkinntat  aurS mainyul. . ^sraskpmia  'käca (AP.) "..Weinen und  Stöhnen"'>  V.;.8.
Fü.:  d  dr  ddpii.irii  (s.  o.),  erl.;  vä'ok  e  an mn  a  dd  an  k  an  mn  m ;  asi  ke  fßn  giwSl  iu  pa tabürak  iunwirf "(ihr) Sprechen  ist  das:  hiimüh lakük  Aümüm;  andre  sagen,  sie  machten  es mit  dem  Tamburin".  Ist  grislatth')  lu  korri- giren? —  ')  GrB.  versteht  darunter  ie{va)n  u mSi  'Klagen  und  Weinen'  um  Verstorbene, was  nach  Sd.  p5.  i  ff.,  Av.  16.  J  ff.  eine  schwere Sünde  ist  Vgl.  DsT.  ZA.  3.  10.  —  »)  Vgl. No.   I   und  Av.  r6.  7.
•  j.  drü  Adv.  'seiüich,  nach  den  Seiten hin':  vTitäspahe  .  .  yd  druca  paurvatUa aiai  ravS  ya^a  (sd.)  ".  .  der  seitlich  und vom  .  ."  Yt/J.  99;  99-
```


## [2026-09-05T20:03:36.526Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3575,3600p' POK_01.txt"
}
```


### [2026-09-05T20:03:36.576Z] TOOL RESULT

```
anord.  dregg  f.,  PI.  dreggiar  ,PIefe'  (daraus  engl,  dregs)-^
alit.  drages  {^dhrdghiäs)  PL,  apr.  dragios  PI.  ,Hefe',  lett.  (Endzelin  KZ. 44,  65)  dradzi  ,Überbleibsel  von  gekochtem  Fett';  slav.  *drosJca  aus *dhr9gli-skä  in  mbulg.  drostija  PL  n.  ,Hefe',  klr.  drUci  ds.,  sonst  assimiliert zu  Hroska  (sloven.  troska  .Bodensatz,  Hefe')  und  meist  *drozga  (aksl. drozdbje  PL  f.  ,TQvyiay  Hefe'  usw.;  s.  Berneker  228);
hierher  auch  gallorom.  "^drasica  ,Darrmalz'  (M.-L.  2767),  das  irgendwie aus  älterem  ^drascä  (=  slav.  *droska)  oder  *drazgä  (==  slav.  *drozga) umgestaltet  sein  wird;
mit  «^Formans:  ahd.  {^trast,  PL:)  trestir  .was  von  ausgepreßten  Früchten übrigbleibt.  Bodensatz.  Trestern'.  ags.  dcerst(e),  di'sest  f.  .Bodensatz.  Hefe' (germ.  *äraysta-,  Sverdrup  IF.  35.  154).  drös  ds.;
mit  sn-Formans :  ags.  drösne  f..  drösna  m.  .Hefe.  Schmutz',  ahd.  druosana, truosana  .Hefe.  Bodensatz';
hierher  wohl  lit.  dergia  (dergti)  .es  ist  schlechtes  Wetter',  ddrganaj ddrga  .quatschiges,  schlechtes  Wetter'  (Stoßton,  vgl.  die  gr.  Wurzelformen und  lit.  dregnas,  dregnüs  .feucht');  dazu  aruss.  padoroga  wohl  .Unwetter', sloven.  sy-dragaj  -drag,  -drga  .kleinkörniger  Hagel;  gefrorene  Schnee- klümpchen.  Graupeln';  lit.  dargüs  .garstig,  schmutzig';  alit.  dergesis .unflätiger  Mensch',  alit.  dergeti  .hassen',  lett.  derdzeties  .zanken,  streiten' (Mühlenbach-Endzelin  I  456  m.  Lit.),  apr.  de^-gt  ,sie  hassen';  lit.  dergti .schmutzig  werden,  beschmutzen',  dargti  ,beschimpfen',  ddrga  f.  , regne- risches Wetter,  Besudelung,  Beschimpfung';
b.  dherg-  in:  mir.  derg  ,rot';  rahd.  terken  .besudeln',  ahd.  tarchannen, terchlnen   ,(verdunkeln)    verbergen,   verstecken',    mnd.    dork    , Kielwasser-
252
räum',  ags.  deorc  , dunkelfarbig',   engl,  dark-^    ags.  peorcung  ,Dämmerunj wohl  mit  d  nach  deostor  ^dunkel',  geduxod  ,dunkel'.
c.  dherk-  in:   lit.  derkti  ,garstig  machen,  besudeln',  darkyti  ^schmähej schimpfen,  entstellen',  darkus  ,garstig',  apr.  erder kts  ,vergiftet',  lett.  därl därci   (*darkis)    ,Schecke''  Mühlenbach-Endzelin   I  448    (s.  die    Sippe Leskien  Abi.  361);    oder  zu  mhd.  zurch  ,Kot',  zürchen  ,cacare'?   Zupitz^ Gutt.  170  unter  Betonung  des  Intonationsunterschiedes  von  derkti  gegen» über   dergesis  usw.;
hierher  wohl  toch.  AB  tärkär  ,Wolke'  (Frisk  Indog.  24); WP.  I  854  ff.
d.  dherobh-  :  dhräbh-  :  dhrobb-.
Unsicher  av.  driici-  {*dhrdhhi-)  ,Flecken,  Muttermal';
mir.  drah  ,Treber,  Hefe'  (*dhrdbho'),  drahar-slüag  ,gemeines  Volk';
aisl.  draf,  engl,  draff  ,Berme,  Hefe',  mnd.  draf,  ahd.  trebir  PI.  ,Treber', anord.  drafli  m.  , frischer  Käse',  drafna  ,sich  auflösen',  norw.  drevja  ,weiche Masse';  geminiert  nl.  drabbe  ^Berme,  Bodensatz',  ndd.  drabbe  ,Schlamm'; schwed.  dröv  n.  ,Bodensatz'  {*dhräbho-),  ags.  dröf,  ahd.  truobi  ,trübe', got.  dröbjan,  ahd.  truoben  ,trüben,  verwirren',  ags.  drefan  ,auf rühren, trüben'  (dasselbe  Bed.-Verh.  wie  zwischen  gr.  ragdaacj  und  anord.  dreggiar).
Eine  nasalierte  Form  mit  halt,  u  als  Tiefstufenvokal  einer  zweisilbigen Basis  (mitbedingt  durch  den  Nasal  m?)  scheint  lit.  *drumb-  in  lit.  druinstas (kann  für  *drumpstas  stehen)  ,Bodensatz',  drumstüs  ,trübe',  drumsciü^ druihsti  ,trüben'   (Schleifton    durch    die   schwere    Gruppe  mpst  bedingt?).
WP.  I  854 f.,  WH.  I  538 f.,  Schwyzer  Gr.  Gr.  I  715.
2.  dher-,  dhero-  ,halten,  festhalten,  stützen'.
Ai.  dhar-  ,halten,  tragen,  stützen,  erhalten,  aufrecht  halten'  (Präs.  meist dhärdyati]  Perf.  dadhära,  dadhri]  dhj-td-:  dhdrtum)  Pass.  ,zurückgehalten werden,  fest  sein,  sich  ruhig  verhalten',  av.  dar-  ,halten,  festhalten,  zu- rückhalten; woran  festhalten,  es  beobachten  (ein  Gesetz);  fest  im  Ge- dächtnis halten;  mit  den  Sinnen  auffassen,  vernehmen;  sich  aufhalten, weilen'  (därayeiti  usw.,  Partiz.  dardta-),  ap.  därayämiy  ,halte',  npers.  Inf. dästan^  osset.  Inf.  dai-iin,  daryWj
ai.  dhdrana-  ,tragend,  erhaltend',  dliarüna-  , haltend,  stützend;  n.  Grund- lage, Stütze',  dhärana-  ,haltend;  n.  das  Halten,  Zurückhalten' =  av.  därana- n.  ,Mittel  zum  Zurückhalten',  ai.  dhartdr-  und  dhdntar-  m.  ,Halter', dharitrl  ,Trägerin',  dhartrd-  n.  ,Halt,  Stütze'  .=  av.  darddra-  n.  ,das Festhalten,  Begreifen',  ai.  dhdrma-  (=  Isit.  firmus)  m.  , Satzung,  Sitte,  Recht, Gesetz',  dharmän-  m.  ,Halter',  dhdrman-  n.  ,Halt,  Stütze,  Gesetz,  Brauch', dhdrlmani  Lok.  ,nach  der  Satzung,  nach  Brauch',  dhäraka-  ^haltend;  m. Behälter',  dhrti-  f.  ,das  Festhalten,  Entschlossenheit',  dx-dhr-d-  ,festhaltend',
253
Ahrl  (oder  sadhrlm)    Adv.    ;,auf    eia    Ziel   hinhaltend,   einem    Ziele   zu%
ji^^'m-anc-  ;nach  einem  Ziele  hin  gerichtet,  vereint,  zusammen';  didhlHä ^*     Vbsicht  zu  stützen",  av.  dldardsatä  ,er  schickt  sich  an^;
über  ai.  cZÄiVa-  ,fest^  s.  Wackernagel  Ai.  Gr.  I  25;
arm.  vielleicht  c^ac^ar  (redupl.)  , Aufenthalt,  Ruhe^  (,*Einhalten^,  vgl.  die Bed.  ,weilen,  sich  ruhig  verhalten^,  dadarem  ,nehme  ab  (vom  Wind)^,
1  ^^  ags.  darian  ,latere^,  ndl.  bedaren  ,ruhig  werden  (vom  Wind,  Wetter)^;
```


## [2026-09-05T20:03:53.163Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3550,3576p' POK_01.txt"
}
```


### [2026-09-05T20:03:53.213Z] TOOL RESULT

```
Nur  in  Erweiterungen  (fast  ausschließlich  germ.):
c?-Erw.:  anord.  detta  st.  V.  ,schwer  und  hart  niederfallen,  aufschlagen' {*dintan.  vgl.   norw.   dial.  datta  [*dantö7i]  ,klopfen':   denta  ,kleine    Stöße
250
geben'),  ufries.  dintje  gleicht  schüttern^  norw.  deise  ^taumelnd  fallen,  gl^Jf (aus:)  ndd.  dei(n)sen  (*dantisöri)  ^zurücktaumeln,  auskneif en^;  ostfries. ,Fall^  (s  aus  -dt-  oder  -c?s-),  anord.  dyntr,  ags.  dynt  m.  (=  anord.  dyi engl,  dint  ,Schlag,  Stoß^;
alb.  g-dhent  ,behaue  Holz,  hoble,  prügle^,  ge^^.  dliend,  dhenn   ,baue schneide'.
Gutt.-Erw.:  anord.  danga  (*dangön)  ,prügeln':  aschwed.  diunga  st.  Y^ ,schlagen^,    mengl.    dingen    ,sclilagen,    stoßen^,    nengl.    ding    (skand.  L^^ mhd.  tingelen   ,klopfen,  hämmernv  norw.   dingle   (und    dangle)   ,bauinela« Kaus.  anord.  dengja,  ags.  dengan,  mhd.  tengen  {tengelen)  ,schlagen,  klopfea' hämmern  (nhd.  dengelnj]  ahd.  tangal  m.  ,Hammer^
Labial-Erw.:  schwed.  dimpa  {damjp)  ,schnell  und  schwer  fallen',  nj dumpen  ,schlagen,  stoßen',  engl.  dial.  dump  ,schwer  schlagen'.
WP.  I  853  f.
1.  dhengh'  ,d rücken,  krümmen,  bedecken,  ^vorauf  liegen'.
Air.  dingid,  for-ding  ,unterdrückt'  (s.  auch  dheigh-)'^  vgl.  Pedersen II  506;
lit.  dengiü,  dengti  ,decken',  dangä  , Decke',  dangia  ,Himrael',  dazu  difu ,versch winden'  (aus  ,*bedeckt  werden'),  slav.  '^d(^ga  ,Bogen'  (:  Yii.  danql in  russ.  dugd  , Bogen',  alt  ,Regenbogen',  bulg.  d^gdy  serb.  düga,  pol dial.  dega  ds.,  wohl  zu:
aisl.  dyiigia  ,Misthaufen,  Haus  in  der  Erde,  wo  die  Frauen  Handarbeiten verrichteten',  ags.  dynge,  ahd.  tunga  , Düngung',  as.  düng,  ahd.  tung,  mhd. tunc  ,unterirdisches  Geraach,  wo  die  Frauen  webten'  (ursprüngl.  zum  Schutz gegen  die  Kälte  mit  Dünger  eingedeckte  Winterhäuser),  ags.  dimg  ,Ge-  . fängnis',  ahd.  tungen  ,bedrUcken,  düngen',  ags.  engl,  dimg  ,Dünger',  nhd. Dung,  Dünger.
WP.  I  791  f.,  854,  Trautmann  44  f.
2.  dhengh'  ,ei-reichen,  fest  zugreifen,  fest,  kräftig,  schnell'.
Ai.  daglinöti  (Aor.  dhak,  daghyäh  usw.)  ,reicht  bis  an,  erreicht',  -dagkna- ,bis  an  etwas  reichend'  (^dhngh-)'^
gr.  raxvg  ,schnell',  Kompar.   d^daaiuv  {^dhngh-)]
air.  daingen  ,fest,  stark'  ==  cymr.  dengyn  ds.  (*dangino-  oder  *dengino-)]
slav.  degz :  dgg^  ,Stärke,  Kraft,  Gelingen'  in  russ.-ksl.  djag^  , Zugriemen', russ.  djdga  , Ledergurt',  djdglyj  ,kräftig,  gesund',  djdgnuh  ,wachseu,  stark    ;, ; werden';    ablaut.    abulg.    ne-dogh    ,Krankheit'     (aber    russ.    düzij   ,stark,  ^ kräftig'   gehört  vielmehr  zu  dheugh-,  unten  S.  271);  der  Bedeutung  nach hat  wohl  eine  Vermischung  mit  slav.  teg-  ,ziehen,  spannen'  stattgefunden (Brückner  KZ.  42,  342  f.).
WP.  I  791f.,  Berneker  190,  217f.
251
..  dber-,  dherg-  in  kons.  Erweiterungen  .trüber  Bodensatz  einer  Flüssig- keit, auch  allgemeiner  von  Schmutz,  Widerlichkeit,  von  quatschigem Wetter,  von  trüben  Farbentünen  usw.;  verbal:  Bodensatz  und  Schlamm aufrühren,  trübend  Ursprüngl.  eins  mit  dher-  ,Unrat,  cacare^
a.  dherg-gh-:
Gr.  ^gdadw,  att.  ^q6ttw  (Perf.  hom.  t€zq7]xcc  intr.)  ,verwirre,  beun- ruliig:^';  rccQCcyy]  .Verwirrung^,  laodooa),  att.  -ttw  ,verwirre'  (*dh,r9gh-iö :  Vit. inrgti  s.  unten);  TQäyvg,  ion.  TQiqxvg  ,rauh,  uneben'  (wohl  ursprüngl.  von Schmutzkrusten;  -^ä-  hier  aus  sog.  r,  d.i.  *dh^vdghü-s)]  idoy^rj-  Tccga^ig lies.  (Vokalstufe  wie  OTtagyi^  :  Vit.  sprögti);
lat.  fraces  L  ,Ölhefe',  fracere  ,ranzig  sein'  aus  *dh^gh-'^  das  c  ist  wohl von  faBces,  floccBs   bezogen,  da    *dherk-   sonst   nur   baltisch   bezeugt   ist;
in  der  Bed.  .Bodensatz,  Hefe':  alb.  drä  f.,  geg.  drd-ni  ,Bodensatz  des  Öls, von  ausgelassener  Butter;  Weinstein'  (Grundform  *draii  aus  *dragä, *dhrdgha) ;
anord.  dregg  f.,  PI.  dreggiar  ,PIefe'  (daraus  engl,  dregs)-^
alit.  drages  {^dhrdghiäs)  PL,  apr.  dragios  PI.  ,Hefe',  lett.  (Endzelin  KZ. 44,  65)  dradzi  ,Überbleibsel  von  gekochtem  Fett';  slav.  *drosJca  aus *dhr9gli-skä  in  mbulg.  drostija  PL  n.  ,Hefe',  klr.  drUci  ds.,  sonst  assimiliert zu  Hroska  (sloven.  troska  .Bodensatz,  Hefe')  und  meist  *drozga  (aksl. drozdbje  PL  f.  ,TQvyiay  Hefe'  usw.;  s.  Berneker  228);
```


## [2026-09-05T20:04:08.607Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD dherg / dher ===\"; grep -n \"dherə*gh\\|dhergh\\|dherg-\\|dher-1\\|dher-2\\|dher-¹\" AHD_watkins1985.txt | head -20; echo \"=== AHD dheu ===\"; grep -n \"dheu-1\\|dheu-¹\\|^dheu\\|dheu-\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-05T20:04:08.679Z] TOOL RESULT

```
<persisted-output>
Output too large (35.6KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/buf3eiw2r.txt

Preview (first 2KB):
=== AHD dherg / dher ===
377:dapper, heavy, strong; later quick, nimble: DAPPER. [Pok. dheb- 239.] dhegvh-. To burn, warm. Suffixed o-grade form *dhogvh- eye- in Latin fovére, to warm, cherish, foment (> fomen- tare, to foment, and fomes, tinder): FOMENT, FOMITE. [Pok. dhegth- 240.] dh@(i)-. To suck. Contracted from *dheoa(i)-. 1. Suffixed reduced form *dhé-mnd- in Latin fémina, woman (< “she who suckles”): FEMALE, FEMININE; EFFEMINATE. 2. Suf- fixed reduced form *dhé-to- in Latin fétus, pregnancy, childbearing, offspring: FAWN, (FETAL), FETUS; EFFETE, (FETICIDE), SUPERFETATE. 3. Suffixed reduced form *dhé-kundo- in Latin fécundus, fruitful: FECUND. 4. Suf- fixed reduced form *dhé-no- in Latin fénum, faenum, hay ( < “produce”): FENNEL, FINOCHIO; (FENUGREEK), SAIN- FOIN. 5. Perhaps suffixed zero-grade form *dhi-lyo- (< *dhia-lyo-) in Latin filius, son, and filia, daughter (but these are equally possibly from the root bheue-): FILIAL, FILIATE; AFFILIATE, HIDALGO. 6. Suffixed reduced form *dhé-lo- in Latin fél(are, to suck: FELLATIO. 7. Suffixed reduced form *dhé-l-ik- in Latin félix, fruitful, fertile, lucky, happy: FELICITATE, FELICITY; FELICIFIC, INFELIC- Ty. 8. Suffixed reduced form *dhé-ld- in Greek thélé, nipple: ENDOTHELIUM, EPITHELIUM, (MESOTHELIUM). 9. Suffixed reduced form *dhé-l-u- in Greek thélus, female: THEELIN. [Pok. dhéi)- 241.] dheia-. To see, look. Variant form *dhyd- (< *dhyag-) in: a. suffixed form *dhyd-mn in Greek sémeion and séma (stem sémat-), sign: SEMANTIC, SEMATIC; SEMAPHORE, SEMASIOLOGY, SEMEME, SEMIOLOGY, SEMIOTIC; b, San- skrit dhydti, he meditates (< “he observes mentally”): ZEN BUDDHISM. [Pok. dheis- 243.] dheigh-. To form, build. 1. Germanic *daigjén in Old English d%ge, bread kneader: DAIRY. 2. Germanic *-dig- in Old English compound Aléfdige, mistress of a house- hold (< “bread kneader”; Al#f, bread, loaf): LADY. 3. Ex- tended o-grade form *dhoigho- in Germanic *daigaz in: a. Old English dag, dough: pouGH; b. Old High German teic, do
...
</persisted-output>
```


## [2026-09-05T20:04:09.867Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN dark ===\"; grep -n \"^dark\\|dark, adj\" KLN_1966.txt | head -10; echo \"=== KLN trachoma ===\"; grep -n \"trachoma\\|trachom\" KLN_1966.txt SKT.txt | head -10; echo \"=== KLN dew ===\"; grep -n \"^dew,\\|dew, n\\.\" KLN_1966.txt SKT.txt | head -10"
}
```


### [2026-09-05T20:04:09.988Z] TOOL RESULT

```
=== KLN dark ===
=== KLN trachoma ===
KLN_1966.txt:39743:Derivative :  trace,  tr. v. ,  to  fasten(a  horse)  by  trace, trache,  form  of  tracheo-  before  a  vowel, trachea,  n.,  windpipe  (anat.)  —  Medical  L.  tra¬ chea,  fr.  L.  trachia,  fr.  Gk.  (dpxr,pia)  tc ayi'.y., ‘windpipe’.  Tpa/eta  is  the  fern,  of  xpax'i?, ‘rough’,  which  is  prob.  rel.  to  •SpdcuTEi.v,  ‘to trouble,  disquiet’,  and  cogn.  with  ON.  dregg, ‘dregs’;  see  dreg  and  cp.  trachoma,  trachyte.
KLN_1966.txt:39755:‘a  cutting  of',  fr.  to pf,,  ‘a  cutting’.  See  -tomy. trachoma,  n.,  a  contagious  disease  of  the  eyes {med.)  —  Medical  L.  trachoma,  fr.  Gk.  xpa- y otpa,  ‘roughness’,  fr.  xpa/ue,  ‘rough’;  see trachea  and  -oma.  The  disease  is  so  called  be¬ cause  it  is  characterized  by  the  roughness  of  the inner  surface  of  the  eyelids, trachy-,  combining  form  meaning  ‘rough’.  —  Gk. xpa y\>-,  fr.  Tp  axils,  ‘rough’.  See  trachea, trachyte,  n.,  a  light-colored  volcanic  rock  (pe- trogr.)  —  Formed  fr.  Gk.  xpa/iSs,  ‘rough’  (see trachea),  with  subst.  sulf.  -ite;  so  called  because of  the  roughness  of  its  fractured  surface. Derivative:  trachyt-ic,  adj. track,  n.  —  ME.  trak,  fr.  MF.  trac,  ‘track  of horses,  trace’,  fr.  OF.,  prob.  of  Teut.  origin;  cp. MDu.  treck,  Du.  trek,  ‘a  drawing’,  MDu. trecken,  Du.  trekken,  ‘to  draw,  puli’,  OHG. trehhart,  ‘to  draw,  shove’,  MHG.  trecken,  ‘to draw’.  Cp.  trek,  trigger.
=== KLN dew ===
```


## [2026-09-05T20:04:17.879Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('AHD_watkins1985.txt',errors='ignore').read()\nfor pat in ['dherag','dhera-g','dherg','dhreg','dheu-','dheua','dhau']:\n    for m in re.finditer(re.escape(pat), t):\n        s=t[max(0,m.start()-200):m.start()+500].replace('\\n',' ')\n        print('###',pat,'|',s[:700]);print()\n        break\nEOF"
}
```


### [2026-09-05T20:04:19.389Z] TOOL RESULT

```
### dherag | exge, dragnet: DRAY; d. Old Norse *drahtr, drdttr, act of drawing, akin to the source of Middle English draught, a pull: DRAFT. 2. Russian drogi, a wagon: DROSHKY. See also variant form dhreg-. [Pok. dheragh- 257.] dhreg-. To draw, glide. Variant form of dhragh-. 1. Na- salized Germanic form *drinkan, to draw into the mouth, drink, in Old English drincan, to drink: DRINK. 2. Nasal- ized Germanic form *drankjan, “to cause to drink,” in: a. Old English drencan, to soak: DRENCH; b. Scandina- vian *drunkna, drugna, to drown, akin to the Scandina- vian source of Middle English drounen, to drown: DROWN. [Pok. dhreg- 273.] dhregh-. To run. 1. Greek trekhein (< *threkhein), to run (> trokhos, wheel)

### dherg | ok. 1. dher- 251.] dher-2, To hold firmly, support. 1. Suffixed form *dher-mo- in Latin firmus, firm, strong: FARM, FERMATA, FIRM, FIRMAMENT; AFFIRM, CONFIRM, INFIRM, (INFIR- MARY). 2. Extended form *dhergh- possibly in Latin fortis, strong (but this is also possibly from bhergh-?). 3. Suffixed zero-grade form *dhr-ono- in Greek thronos, seat, throne (< “support”): THRONE. 4. Suffixed form *dher-mn in Sanskrit dharma, statute, law (< “that which is established firmly”): DHARMA. 5. Old Persian dar-, to hold (whence Persian -ddr, ‘“-holder’’): SIRDAR, TAHSILDAR, ZAMINDAR. [Pok. 2. dher- 252.] dher-3, To drone, murmur, buzz. Extended zero-grade form *dhrén- in: a. Germanic *drén- in Old English

### dhreg | e; wickerwork, fence. pele-2. Flat; to spread. mu-', Imitative of inarticulate sounds. After the basic meaning there may appear further information about the phonological shape or nature of the root: dhreg-. To draw, glide. Variant form of dhrag-. temp-. To stretch. Extension of ten-. tauro-. Bull. Derivative of sta-, but an in- dependent word in Indo-European. dail-. To divide. Northern Indo-European root. pipp-. To peep. Imitative root. pa-. To protect, feed. Contracted from *pao-. kak-2. A round object, disk. Germanic root. mas. Male, Latin adjective of unknown ori- gin. Most, but not all, of the additional informa- tion is self-explanatory. In the first three examples, the boldface forms

### dheu- | le: FANATIC; PROFANE. 4. Possibly suffixed zero-grade form *dhas-o- becoming *dhes-o- in Greek theos (< *thes-os), god: THEO-; APOTHEOSIS, ATHEISM, ENTHUSIASM, PANTHEON, POLYTHEISM. [Pok. dhés- 259.] dheu-'. Also dheue-. The base of a wide variety of derivatives meaning “to rise in a cloud,” as dust, vapor, or smoke, and related to semantic notions of breath, various color adjectives, and forms denoting defective perception or wits. 1. Suffixed extended zero-grade form *dhii-mo- (<*dhua-mo-), smoke, in: a. Latin fimus, smoke: FUMAROLE, FUMATORIUM, FUMATORY, FUME; FUMARIC ACID, FUMIGATE, FUMITORY, PERFUME; b. Greek thumos, soul, spirit: -THYMIA; ENTHYMEME; c. Greek thumon, thumos, thyme (< “p
```


## [2026-09-05T20:04:29.300Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk '/^259$/{found=NR} END{}' POK_01.txt; grep -n \"^259$\\|^ *259 *$\" POK_01.txt | head; echo \"--- dheu entries ---\"; grep -n \"dheu-\\|dhau-\\|dheue\" POK_01.txt | sed -n '1,40p'"
}
```


### [2026-09-05T20:04:31.026Z] TOOL RESULT

```
3708:259
--- dheu entries ---
2961:Im   Germ,  außerdem    mit    i-Vokalismus    mnd.    trlseln,   westfäl.    trids^ly^      i ,rollen,  taumeln^,  holl.  trillen  ,zittern^  (woraus  ital.  trillare  ^beben,  Trillep schlagen')  usw.  Gegen  Verbindung  von  ai.  drdvati  mit  av.  dvaraiti  ,geht* s.  unter  *dheu-y  *dheuer-  ^stieben^
3395:In  allen  Gliedern  etwas  zweifelhafte  Verbindung.  Über  air.  de'd(a). vgl.  Pedersen  KG.  II  504  f.  (von  einem  Perf.  *dhe-doue  aus  zu  got.  diwans , sterblich'?  s.  dheu-  , hinschwinden',  wo  auch  über  air.  dlth,  arm.  di).  Die germ.  Sippe  endlich  erinnert  z.  T.  an  die  unter  "^dheues-  ,stieben'  bespro- chene von  ndd.  dösig  und  könnte  nicht  bloß  in  der  5-Erw.,  sondern  auch in  der  Bed.  sich  z.  T.  nach  dieser  gerichtet  haben;  immerhin  ist  mit  einer alten  Verwandtschaft  von  anord.  dcesask  usw.  und  ir.  -deda  zu  rechnen.
3528:inwieweit  die  s-Formen  schwed.  mdartl.  stimma,  stimha  , dampfen^,  norw. mdartl.  stamma,  stamha  ,stinken^  einen  idg.  Hintergrund  haben  oder  nur nach  dem  Nebeneinander  von  ahd.  toum :  ags.  stEam,  dt.  toben :  stieben (s.  unter  dheu-,  dkeu-bh-  ,stieben^)  neugeschaffen  sind,  ist  fraglich;
3718:Arm.  di'Jt  , Götter*  (PI.  *dheses)',  lat./eWae  (alat. /esiae)  ,Tage,  an  denen keine  Geschäfte  vorgenommen  wurden,  Feiertage*,  festus  ,f estlich,  feier- lich, ursprüngl.  von  den  der  religiösen  Feier  gewidmeten  Tagen',  osk. fiisnam  Akk.  ,templum',  umbr.  fesnaf-e  ,in  fanum'*,  tiefstufig  lat.  fänum {*fas-no-m)  , heiliger,  den  Göttern  geweihter  Ort'  und  ai.  dhisnya-  , an- dächtig, fromm,  heilig'  (unsicherer  dhisanyant-  u.  dgl.,  s.  unter  dheid- , sehen');  über  gr.  d-eog  ,Gott'  s.  unter  dheues-,  über  lat.  fäs,  fästus  oben S.  105f.
3731:Got.  diwans  (*dheu-ono-) , sterblich*,  ablaut.  ahd.  touiven,  as.  döian  , sterben*, anord.  deyja,  dö  (*döw),  däinn  ,sterben';  got.  daups  ,tot*,  auch  af-dauipt ,geplagt',  ahd.  töt^  ags.  dead,  anord.  daudr  ,tot*,  got.  dau^us  ,Tod',  ahd. töd,  ags.  deaj)^  anord.  daud-r,  -ar  und  daude  ,Tod*;
3732:air.  duine  (*dliu-n-io-),  PI.  döini  (*dheuen-{o-),  cymr.  dyn,  corn.  bret. den  , Mensch*  (.Sterblicher*,  Brugmann  ZfceltPh.  3,  595 ff.);  s.  auch  unter ghdem-]
3733:vielleicht  lat. /wnws  (fönus?)  n.  , Leichenbegängnis,  Bestattung',  fallsaus *dheu{e)-nos  ,auf  den  Tod  bezügliche  Erweisung';  formell  jedoch  genau =  air.  n.  5-Stamm  dün  , Festung',  wohl  ursprüngl.  ,Burghügel'  (s.  unter 4.  dheu-  S.  263);
3745:4.  dheu-,  dheuO'  (vermutlich:  dhue-,  vgl.  dio  Erw.  dhue-k-,  dhä-s-)  ,stieben, wirbeln,  bes.  von  Staub,  Rauch,  Dampf;  wehen,  blasen,  Hauch,  Atem; daher  dampfen,  ausdünsten,  riechen,  stinken;  stürmen,  in  heftiger, wallender  Bewegung  sein,  auch  seelisch;  in  heftige,  wirbelnde  Bewe- gung versetzen,  schütteln';  Nominalbildungen:  dhü-li-,  dhü-mo-.
3768:gr.  d-icü  (ßdvaa),  lesb.  d^vio) , stürme  einher,  brause,  tobe,  rauche'  {*dhu-iö, V  aus    d^awj   edvaa,   wie   auch   ü   im   ai.  Pass.  dhüydte   und   anord.  dyja    g ,schütteln'   Neubildung   ist;    in   der   Bed.   ,rase'   vielleicht   aus  *dhusiö,  s.  /^ dheues-),  ^vduj,  dvd^w  ds.,  MeXka  ,Sturm'  (s.  S.  269  unter  dheues-),  ep.  divot  j% ,fahre  einher,  stürme  daher^  {^d-vvJ^w),  d^Vvew  ds.  {^-^viifu)),  ^vvog'  ndh- fiOQy    ÖQ^irj,    ÖQÖLiog   Hes.    Mit   der   Bed.    , rauchen    (Rauchopfer),   riechen': -d^Vü)    (^ö-w),    Ts&vyta    ,opfere',    -d-vaia  , Opfer',    ^i(j,cc    ,Opfertier^,  ^vog  n. , Raucher  werk  (daher  lat.  tüs),  Opfergabe,   Opfer'  (davon  ^veia  ,Mörser'?
3777:got.  dauns  f.  , Geruch,  Dunst'  (*dhou-ni),  anord.  daunn  m.  , Gestank' (vgl.  alb.  dej]  über  ahd.  nhd.  dunst  s.  unter  der  Wurzelform  *dheues-); anord.  dünn  m.  , Daune  (daraus  mnd.  düne^  wovon  wieder  nhd.  Daune] vgl.  mndl.  donst  ,Daunen,  Staubmehl'  =  dt.  Dunst]  s.  Falk-Torp  u.  dum,)] as.  dununga  ,deliramentum'  (u  oder  «?);  aisl.  düni  ,Feuer';
3781:Vgl.  noch  das  vielleicht  ursprungsgleiche  *dheu-  ,laufen,  rinnen'.
3819:6.  r-Erw. :  dheuer-  (dhuer-,  dheur-)   ,wirbeln,  stürmen,  eilen;  Wirbel    ^
3846:Ob  hierher  als  *dheu-g-:   germ.  *du-k-j  *du-kk-  ^tauchen,  sich  ducken"',
3852:dheues-,  dhues-,  dheus-,  dhas-  ,stieben,  stäuben,  wirbeln  (nebeln,  regnen, Dunst,  Staub;  aufs  seelische  Gebiet  angewendet:  gestehen,  verwirrt sein,  betäubt, .  dösig,  albern),  stürmen  (vom  Wind  und  aufgeregtem Wesen),  blasen,  wehen,  hauchen,  keuchen  (Hauch,  Atem,  Geist,  Ge- spenst, animal;  riechen,  Geruch)'.  Erweiterung  von  4.  dheu-',  auch Ausdrücke  für  , dunkle  Farben'  scheinen  als  ,nebelgrau,  staubfarben' angereiht  werden  zu  sollen. Ai.  dhvamsati  , zerstiebt,  zerfällt,  geht  zugrunde',  Partiz.  dhvastd-j Kaus.  dhvamsdyati,  dhvasdyati  ,bestäubt,  vernichtet',  dhvasmdn-   m.  ,Ver-
3854:dunkelung^;  dhvasird'  ,hestii\iht,  besprengt^,  dhvasrd-  ^bestaubt,  unkenntlich^, dhüdsti-  f.  ;das  Zerstäuben^  (=  ahd.  tunist,  dun{i)st  ,Wind,  Sturm,  Hauch, punst';  ags.  afries.  düst  ,Staub^),  dhüsara-  , staub  farbig^;  zur  Bilduno- (*dhi-es-mi,  Konj.  dheu-s-5  neben  "^dhu-n-es-mi,  Konj.  *dhu-m-s-o)  vgl. Kuiper  Nasalpräs.  41;
```


## [2026-09-05T20:04:37.055Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"laufen,  rinnen\\|laufen, rinnen\" POK_01.txt | head; echo ---; sed -n '3708,3748p' POK_01.txt | cut -c1-300"
}
```


### [2026-09-05T20:04:37.117Z] TOOL RESULT

```
3720:X.  dbeu-  ,laufen,  rinnen*.
---
259
dbers'  , wagen,  kühn  sein',  älter  ,angreifen,  losgehen*  (auch  mit  -i-,  -u- erweitert).
Ai.  dhrs-nö-ti,  dhdrs-ati  ,ist  dreist,  mutig,  wagt',  ährsü-  (Gramm.),  dhrsat Jierzhaft'  (=  av.  dard^at),  dhrsnii-  ,kühn,  tapfer,  mutig,  dreist,  frech', dhfstd-  ,keck,  frech',  dhfsüa-  ,kühn,  mutig',  dädhrsi-  ,beherzt,  kühn',  mit Objekt  dharsayati  ,wagt  sich  an, 
gr.  lesb.  -d-sgaog  n.  ,Mut,  Kühnheit'  (hom.  QsgalTrjg  ,Frechling'),  mit aus  dem  Adj.  verschleppter  Tief  stufe  ion.  altatt.  d^ccQOog  (att.  ^agoog)  ds., att.  d-gdaog  n.  ,Mut,  Kühnheit;  Verwegenheit,  Frechheit',  d-aqüeu),  d^aggeo) ,bin  mutig',  S-agavg  (rhod.  QaQGvßio
lat.  infestus  , feindlich*,  infestäre  , feindlich  behandeln,  angreifen'  und manifestus   , handgreiflich,   auf  der  Tat  ertappt;    offenkundig'   (*dhers-to-)]
got.  ga-dars  ( :  ai.  Ferf .  dadhdrsa  ,hat  sich  erkühnt'),  Inf.  gadaürsan,  ,ich wage',  as.  gidurran,  ags.  dear^  durran,  ahd.  {gi)tar,  (gi)turran  ,wagen',  ahd. giturst,  ags.  gedyrst  f.  , Kühnheit,  Verwegenheit'  (=  ai.  drsti-h  ,Kühnheit');
lit.  nasaliert  lit.  dresü  ,wage*  (*dhrensö),  dristü,  dristi  {dhrns-)  , wagen', drqsä  (*dkrons-)  , Dreistigkeit',  di-qsüs  =  lett.  drüoss  ,mutig'  (*dhrons-j alit.  noch  drisüs  und  draiisniaus)]  ohne  Nasalierung  apr.  dirstlan  , stattlich* und  dyrsos  ,tüchtig'  (*dirsu
hierher  vielleicht  toch.  A  ^sär  ,rauh',  tsrasi  , stark',  B  tsirauüe  , Stärke*.
WP.  I  864,  WH.  I  698  f.,  Trautmann  60,  Van  Windekens  Lexique  147.
dbes-,  dhos-  in  religiösen  Begriffen.
Arm.  di'Jt  , Götter*  (PI.  *dheses)',  lat./eWae  (alat. /esiae)  ,Tage,  an  denen keine  Geschäfte  vorgenommen  wurden,  Feiertage*,  festus  ,f estlich,  feier- lich, ursprüngl.  von  den  der  religiösen  Feier  gewidmeten  Tagen',  osk. fiisnam  Akk.  ,templum',  umbr.  fesnaf-e  ,in  
WP.  I  867,  WH.  I  453,  3 f.;  EjVP  333,  347 f.
X.  dbeu-  ,laufen,  rinnen*.
Ai.  dhdvate  , rennt,  rinnt',  dehnstufig  dhdvati  ds.,  dhäuti-h  f.  , Quelle, Bach*;  mpers.  davfidan  ,laufen,  eilen*,  päm.  dav-  ,laufen,  rennen';
17*
260
gi\   ^€w,   ep.   auch   x^siu),  Fut.   d^£vaoy,ai  , laufen*;   lak.    af]'  rqixe   Hes; ^oög  , schnell',  ßorj-^öog  ,auf  einen  Anruf  schnell  zur  Hand,  helfend*,  daznl ßotjd-iü)   (statt   *ßorjdo€Cü)  , helfe',    ^oaCu)   ,versetze  in  schnelle  Bewegun, bewege  mich  sc
gr.-illjr.  dvdv'  ytgrjvrjv  Hes.;
anord.  dgggy  Gen.  dggguar  {*dawwo),  ags.  deatü,  as.  dau^  ahd.  to\i^  n} Tau  (*dawioa-)',
unsicher  mir.  döe  ,Meer'  (*dheuiä)  als  ,das  heftig  Bewegte';
hierher  wohl  *dhu-rO'  im  thrak.  FIN  ^A-d^vqag  (^n-dhu-r-)  und  in reichen  ven.-illyr.  FIN,  so  illyr.  Duria  (Ungarn),  nhd.  Tyra,  Thur,  äh Dura   (Elsaß,  Schweiz),    oberital.  Dora,  Doria,    frz.   Dore,    Doire,   Don iber.  Durius,    Turia  usw.   (Fokorny  Urill.  2,  10,
nach  Rozwadowski  (Rev.  Slav.  6,  58  ff.)  hierher  der  FIN  Düna,  wes slav.  Dvina  (*dhueinä),  als  finn.  väinä  ,breiter  Fluß*,  estn.  väin(a)  ,Sund* syrj.  'dyn  »Mündung*  entlehnt. .   WP.  I  834.
2,  dbeu-,  dbu-ei-  , hinschwinden,  bewußtlos  werden,  sterben*.
Got.  diwans  (*dheu-ono-) , sterblich*,  ablaut.  ahd.  touiven,  as.  döian  , sterben*, anord.  deyja,  dö  (*döw),  däinn  ,sterben';  got.  daups  ,tot*,  auch  af-dauipt ,geplagt',  ahd.  töt^  ags.  dead,  anord.  daudr  ,tot*,  got.  dau^us  ,Tod',  ahd. töd,  ags.  deaj)^  anord.  dau
air.  duine  (*dliu-n-io-),  PI.  döini  (*dheuen-{o-),  cymr.  dyn,  corn.  bret. den  , Mensch*  (.Sterblicher*,  Brugmann  ZfceltPh.  3,  595 ff.);  s.  auch  unter ghdem-]
vielleicht  lat. /wnws  (fönus?)  n.  , Leichenbegängnis,  Bestattung',  fallsaus *dheu{e)-nos  ,auf  den  Tod  bezügliche  Erweisung';  formell  jedoch  genau =  air.  n.  5-Stamm  dün  , Festung',  wohl  ursprüngl.  ,Burghügel'  (s.  unter 4.  dheu-  S.  263);
nach  Marstrander  Pres,  a  nasale  inf.  15^  hierher  air.  -deda  , seh  windet dahin'  aus  *dhe-dhu-ä-t]  vgl.  auch  oben  unter  3.  dhe-]
im  Germ,  auch  die  Bed.  , fühllos,  ohnmächtig  werden*,  awnord.  da {*dawa)  , Bewußtlosigkeit,  Ohnmacht*,  Prät.  dö  auch  , wurde  gefühllos' (von  Gliedern),  aschwed.  däna  ,in  Ohnmacht  fallen*,  norw.  daana  , steif, lahm  werden  (von  Gliedern),  in  Ohnmacht  fallen'  (Abl
3'
261
Erweiterung-  dhu-ei-  :  dhu-i-  in:
arm.  di^  Gen.  dioy  , Leiche,  Leichnam',  air.  dlth  {*dhuUu-)  ,Ende, Tod';  ag-s.  dwlnan  (st.  V.)  ,abnehmen;  schwinden',  neben  dem  7iöM-Verb anord.  duma  und  duena  ds.;  ags.  dwcescan  , auslöschen'  (*dwaiskjan),  lit. (/i?i5<i  ,erlöschen'  (Büga  bei  Endzelin  KZ.  52,  12
WP.  I  835,  WH.  I  451,  568.
dbeu-  , blank,  glänzen'.
Ai.  dhavald-  ,glänzend  weiß',  dJiävatl  ,macht  blank,  reinigt,  spült',  av. fraöavata  ,rieb  sich  (reinigend)  ab';
gr.  ^oög' . . .  Xa^TtQÖg^  d^owaau  •  . . .  XaiinQvvai  Hes.,  ddoVreg  X«t;xci:  -^iovreg Ps.-Hsd.,  S^alsiov  xad-agöv.   xal  d-coUov  Hes.  (Kontr.  aus  *^oJ^aUog).
WP.  I  835,  Schulze  KZ.  29,  260  f.  =  Kl.  Sehr.  369.
4.  dheu-,  dheuO'  (vermutlich:  dhue-,  vgl.  dio  Erw.  dhue-k-,  dhä-s-)  ,stieben, wirbeln,  bes.  von  Staub,  Rauch,  Dampf;  wehen,  blasen,  Hauch,  Atem; daher  dampfen,  ausdünsten,  riechen,  stinken;  stürmen,  in  heftiger, wallender  Bewegung  sein,  auch  seelisch;  in  heftige,  
Mit  lü-Formantien:
Ai.  dhUmd-h  m.  ,Rauch,  Dampf,  dhümäyati  , raucht,  dampft'  =  lat. fümäre,  formell  auch  =  ahd.  tümön  ,sich  im  Kreise  drehen*;
gr.  d^vixog  ,  Gemüts  Wallung,  Leidenschaft,  Mut*  (dvi^iao)  noch  rein  sinn- lich , rauche,  räuchere';  ■d-Vf.idX-ajip  , Kohlenmeiler',  d-^i.av.ög  , leidenschaftlich*, d^v^aivo)  , zürne*  usw.);
```


## [2026-09-05T20:04:54.855Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== CHEUNG dau ===\"; grep -n \"davīdan\\|davidan\\|dawīdan\\|\\*dau\\b\\|dav-\" CHEUNG.txt | head -30"
}
```


### [2026-09-05T20:04:54.908Z] TOOL RESULT

```
=== CHEUNG dau ===
5253:*dau! *to speak, chat' 
5286:*dau? ‘to run’ 
5294:*NWIR: NP davidan/dav-, Kurd. dawin/daw-, Gil. (Rsht.) dovastoen/dov-, Siv. 
5323:*dau? ? ‘to be skilful’ 
5329:© The existence of *dau ‘to be skilful’ is doubtful, the Avestan evidence is question- 
5358:*dauč! (*dauj ?) ‘to milk, traire (< **to draw’ ?)’ 
5383:© Both *daué and *dauxš are problematic: they may have either a different origin or 
6376:*duar: these "roots" are perhaps extended formations of *dau? (Skt. dhàv) ‘to run’, 
40896:davidan/dav-, 65 
55510:*dau’, *Hnar 
55999:*dau, *zrad 
57661:*dau', *dram, *drau’, *duar, 
57951:*dau, *far’, *HaH(a)d, 
58127:*dau, *zrad
```


## [2026-09-05T20:04:56.631Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN ===\"; grep -n \"dav\\(i\\|î\\|ī\\)dan\\|dawîdan\\|davîdan\\|davîden\\|davîdan\" HRN.txt | head -20; echo \"=== HRN grep dav ===\"; grep -n \"davîden\\|dav\\b\" HRN.txt | head -20"
}
```


### [2026-09-05T20:04:56.700Z] TOOL RESULT

```
=== HRN ===
=== HRN grep dav ===
5017:LW. kurd, durüy; af/. daröy; bei. davöy^ drög,
5254:"WSL/, vidäv-am 'laufen, rennen', sar. davän-am
10333:64. daväk (geschrieben dübak) 'Bote.
10336:65. davärastan 'laufen, dararUan (Phlv.-Vend., AV.),
10341:66. davnstan 'sprechen*, dav(i)sn (vd. 19 (141)) (>), nur
10384:Hörn, Gruudri88 d. iioiip. Eiymolog-ie. ]8verdrängt. Desshalb scheint mir arm. dav *Nach-
10385:stellung, Hinterlist, Verrat', davem nachstellen', dav-
14835:l^dav-, darata 66.
21487:8. davänam 585.
```


## [2026-09-05T20:05:02.449Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5286,5330p' CHEUNG.txt"
}
```


### [2026-09-05T20:05:02.504Z] TOOL RESULT

```
*dau? ‘to run’ 
MIDDLE PERSIAN: MMP dw-, BMP dw(b)- (LHTWN-) /daw-/ ‘to run’ = DMMPP: 


143b 
Pres.: IND. 3pl. MMP dwyynd, MMP dwynd; Partic.: pres. MMP dww’n, BMP dwb’n /dawan/ 


*NWIR: NP davidan/dav-, Kurd. dawin/daw-, Gil. (Rsht.) dovastoen/dov-, Siv. 
doui-/douiya “to run’, (sec. caus.) Gil. (Rsht.) davancen/davan- ‘to cause to run’, 
Kurd. (Sor.) daw ‘run’ (LW ?), NP dok, Khuns. dek, dik ‘spindle’ || (+ *ham-) Anar. 
hendefte/hendewn-, Nn. endefte/endewn- (sec. caus.) ‘to send’ 

*NEIR: Oss. I. dawyn/dawd, D. dawun/dawd ‘to spawn’, Yghn. dau-/dáuta ‘to run’, 
(caus.) ? Yi. lou-/lowai ‘to graze’ || (+ *abi-) Wa. vidaw- ‘to ride’ || (+ *upa- ?) Wa. 
pióówg (in pióowg woc- ‘to become apparent, noticeable, to appear’) || (+ *ni-) Wa. 
nióó(w)g ‘branch of a river? 


66 *dau3 ? 


*MISC: Par. daw- (?), dhaw-/dah- ‘to run’ (LW ?), ? Par. daw- ‘to be straight’ 
*SANSKRIT: dhav ‘to walk, to hurry, to flow’ (RV+) = EWAia I: 789 

© This Пг. root has a cognate in Gr. only ? 

«PIE *d'eu- ‘to move, go’ > LIV: 147 f. | Pok.: 260, 262 


*IE COGNATES: Gr. 8€ ‘I walk’, 8005 ‘quick’ 

*REFERENCES: KPF I: 143a; IIFL I: 249a, 251b; Christensen, Contributions I: 65; IIFL II: 547, 222a; 
Andreev — PeSéereva: 245a Ё; Abaev, Slovar’ I: 349; WIM I: 349; WIM Ш: 104; Werba 1997: 200; 
Steblin-Kamenskij 1999: 244, 459; Cabolov 2001: 284; Lecoq 2002: 131, 133; ESIJa II: 384 ff. 


*dau? ? ‘to be skilful’ 

*AVESTAN: OAv. dauu- ‘to be skilful’ — Liste: 31 

Partic.: pres. OAv. dauuant- (Y 31.10) 

© The existence of *dau ‘to be skilful’ is doubtful, the Avestan evidence is question- 
able, on which see further Kellens — Pirart 1991: 67; Humbach 1992 (2): 67.
```


## [2026-09-05T20:05:03.457Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5240,5270p' HRN.txt; echo \"=== page markers ===\"; grep -c $'\\f' HRN.txt; grep -n \"585\\.\" HRN.txt | head"
}
```


### [2026-09-05T20:05:05.242Z] TOOL RESULT

```
583. {i)dös 'die letzte, vergangene Nacht'.
aw. daosatara- 'abendlich, westlich'; phlv. dös,
dösastar, vergl. s(i)dös (geschrieben s(i)t") ') ; ai. dösä-,
kurd. duc; afy. LW. dös; oss. disson 'gestern Abend'
(116); bei. dost (95).
Bartholomae, BB. XV, 209 möchte auch in
aw. daozanhahe, duzanha-, daozavat u. a. m. die ur-
sprüngliche Bedeutung 'finster, nächtlich' finden.
584. (^)dös 'Schulter .
aw. daösa- 'Schulter (ZPGL); phlv. dös; ai. dos-,
dösdn- 'Vorderarm, Arm'.
585. dev>lden 'laufen, eilen , devän, devämden,
ai. l/^dhaV'j dhdvati 'rennen, rinnen, strömen; phlv.
davTtan (auch "2M geschrieben); gr. dsu).
"WSL/, vidäv-am 'laufen, rennen', sar. davän-am
'galoppiren'.
586. duvlst {*duvest) 'zweihundert' {du sed).
aw. dv^ säte ; päz. dvest (Aogem.) ; ai. dve gate 'zwei-
hundert'.
Der ehemalige Majhülvokal hat sich in der Aus-
sprache, die ursprünglich duvest gewesen sein muss,
*) Dar m steter, Et. ir. I, 319.— 131 —
nicht mehr erhalten ^). duvlst ist die einzige im Np.
bewahrte Dualform.
587. deh zehn, dehum, )^Dinn (Is. 37, 30)2).
aw. dasa zehn', dasema-; phlv. dahuw; ai. r/ara,
dafamci-; arm. ^as« *zehn' (H. No. 270).
kurd. bei. LW. deh, dah; afj'. las; oss. d. t. das,
däsäm (106); wa/. das^ las, sar. dh, sij'n. J7s, te,
ya;ai. sangl. das, minj. LW. daÄ.
588. dih *Dorf*, vergl. dihgän (arab. LW. dihqän, arm.
=== page markers ===
396
5251:585. dev>lden 'laufen, eilen , devän, devämden,
12078:devatiiden 585.
12087:./eMrfe« 585.
14849:(lä)iö.karsn' 585.
15760:darllan 585.
20255:i r/ä// 585.
21487:8. davänam 585.
21986:viSavam 585.
23164:I surääiq 727.salidäiiaj 585.
```


## [2026-09-05T20:05:21.781Z] TOOL CALL #21: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['FFD','BQT','MON','HRN','BRT','KNT','PHD','NYB','POK','ARY']:\n    e=d[k]; print(k, '|', e.get('page_offset'), '|', str(e.get('lookup_hint'))[:300]); print()\n\""
}
```


### [2026-09-05T20:05:23.613Z] TOOL RESULT

```
FFD | 115 leaves (PDF pages); printed page = PDF page − 5 (PDF 40 = p.35). 2nd printing 1385 of the same Qoqnus setting (ISBN 964-311-015-X). | Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).

BQT | vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). | grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --d

MON | None | Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbe

HRN | leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.

BRT | Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops.

KNT | leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; section refs like '$147'. Nourai's page numbers should fall in 164-215 for lexicon citations.

PHD | leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB).

NYB | Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.

POK | POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' giv

ARY | printed page = pdf page + 1 | Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY
```


## [2026-09-05T20:05:31.052Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FFD page 54 (pdf 59) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==59' incoming/FFD/FFD_pages.txt | head -60"
}
```


## [2026-09-05T20:05:31.765Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD daw ===\"; grep -n \"^daw\\|dawistan\\|dwtn\\|to run\" PHD.txt | head -20; echo \"=== NYB ===\"; grep -n \"^daw\\|dawistan\\|dw-\\b\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-05T20:05:32.899Z] TOOL RESULT

```
=== FFD page 54 (pdf 59) ===
[pdf page 59]
چا انا نا فعلهای فارسی دری
دوختن (۱)
دوخت + فارسی میانه 4071 < ایرانی باستان 4203-1۵*. برای 2 > آراست. 42
: صورت اصلی 42 است. 3 پیش از 1 به #بدل شده است.
دوز + فارسی میانه 432 + ایرانی باستان 4۵-۸*. برای 2 > آرای. 6 به جای ۴ آمده
است. ريشةٌ 1421 به معنی «دوختن» است.
دوخمن(۲)
دوخت + فارسی میانه 457 « ایرانی باستان 4۵-1*. برای 1۵ > آراست. ۵28
صورت اصلی 4205 است. 8 پیش از ۲ به #بدل شده است.
دوش + فارسی میانه 435+ ایرانی باستان 5.۶42۵ برای ساختن ريشةٌ جدید به ريشه
افزوده شده است. 8 پیش از دبه #بدل شده است. ريشهٌ 4208 به معنی «دوشیدن» است.
دوشیدن
دوشید + فارسی میانه 45810. 0 مادهٌ ماضی جعلی است از 465. مادهٌ مضارع
به معنی «دوشیدن» است.
دویدن
دوید < فارسی میانه 48۷۲۵. ماد ماضی جعلی است از 7 و ۲۵. 489 مادةٌ مضارع
است.
دو < فارسی میانه هل + ایرانی باستان *-42۷۷*. برای 2 > آرای. ريشهٌ 40۷ به
معنی (دویدن» است. ۱
دیدن
دید <ج فارسی میانه 474 « ایرانی باستان ۵۲-1۵*. برای 48 > آراست. ريشة 7
به‌معنی «دیدن» است.
```


### [2026-09-05T20:05:32.959Z] TOOL RESULT

```
=== PHD daw ===
310:das [d’s | N ~] sickle. dàs?r [d’sl = Av. dātra-) gift, reward. dast [Y DE < A yd-h; dst! | = M, N ~] hand. dastag [dstk! | N —a] bunch, bundle, group. dast(a)gird [Y DE., dst-krt! | M dstygyrd, N dastgird] estate. dast- gir [dst OH DWN, (v. griftan) | N ~] 1. helper; 2. captive. dast-graw [dstglwb!] captivity. dast-kàrih [ҮЛЕ ГУА | N ~7] handiwork. dast-šūy [dstšwd] = ģūmēz. dastwar [dstwbl | М dstwr, N dastür] authority, priest, minister. ~th: custom; authority. dastyar [dstyd?l | (P dstd’r), N ~] helper. ~th: help, assistance. dašn [dšn! | = M] right hand. dāšn [d”$n' | M d’s(y)n] gift. dašnaģ [dsnk' | N ~a] 1. right hand; 2. dagger. dašt [dst! | = M, N —] plain, open ground. daštān [dft?n! | N ~] menstruation; menstruous. „estān [-st?n'] secluded place for menstruous women. -—--màh [-m?h] menstrual cycle. -ūmand [-’wmnd] menstruous. dāštan, dar- [YHSNN-tn! < А V ben: d^ftn', Pl- | M d'An, ar-, N ~] have, hold, keep, preserve. pad . . . dāštan: hold by, to; take for. pad éd dāštan [cf. N pindāštan] consider. --išn: preservation, maintenance. dāštār [4° #1 keeper, preserver. daw-, v. dawidan, dawistan. idawāl [dwb’l | N ~] leather, skin. ždawāl [dwbl | N ~] deceit, trickery. idawīdan, daw- [LH TWN-tn! < A Vrht; dwytn', dwb- | M dw-, N ~] run. *dawidan, daw- [dw-ytn'] speak (daevic). 1, 2 dawistan [LH TWN-stn!, dwstn'] = 1 * dawidan. daxmag [dhmk' | P dxmg, N ~a] tomb, dakhma (a building where corpses are exposed for destruction). „estān [-si?n!] cemetery. dax$ag [dhšk! | M dxsg] mark, sign, characteristic; memory. pad ~ dàštan : remember. az — hištan: forget. ~6mand [-’wmnd] marked. Day [ddw' | M dyy, N ~] Creator; cal. roth month; 8th, 15th, 23rd days. dayag [d^yk! | M d?yg-, N ~aj (wet-)nurse. „ānīh [nyh] | (N dāyagī)] nursing, nurture. dazidan, daz- [dc-ytn'] burn, scorch. --išn : burning.
394:handāxtan, handāz- [hnd@htn', hnd?c- | M hnd?c-, № an~] plan, allot, reckon, judge. ~išn: judgement. handāxtār [%nd”%t”[] planner. handāz-, ~išn, v. handaxtan. ~ag [hnd?ck! | N andáza] measure, manner; ~ 1: like. handēmān [hndym’n' | = M] before, in the presence of. ~th: audience, presence. handēmānģar [kndym’ nkl] introducer (into the presence). „lt: introduction. handéSidan, handēš- [Ahndyti-ytn! | M hndy§-, N an~] think, consider, reflect. išn: thought, reflection. handēšīdār [hndyfyt?I] thoughtful. handēxtan, handēz- [hndwhtn', hndwc- | N an~] gain, acquire, amass. „-išn(īh): acquisition. handraxtag [hndl htk! | P ?ndrxt] oppressed. ~ih: oppression, suffering. handüdan, *handāy- [hndwtn' | (M ?nwd), N an~] smear, plaster, anoint. hangad [hngt! | P ?ngd] fortunate, rich. ~ih: fortune, wealth. hangām [hng’m | N ~] time, occasion. ~ig [-yk!] timely. hangarag [hng’lk' | N angara] reckoning. hangardan, hangàr- [hng’l-tn' | M hng^r-, N an~] consider, reckon. ~išn: consideration. hang��xtan, hangéz- [hngyhtn', hngyc- | (M hgjyn-), N an~] arouse, stimulate, stir up. ~išn: arousing. hangirdénidan, hangirdén- [hngityn-ytn'] complete, summarize. hangirdig [kngltyk'] complete, perfect; summary. ~ih: completion, summary. hangdSidag [hngw£ytk! | M ”ngwšydg] way, manner, likeness. ~ 1: like. hanģrāyīdan [hngl’dytn'] lament. hangrüdag [hnglwtk'] lamenting. hanj-, v. hixtan. hanjaftan [hncptn' | P hnjft, (M hnzpt)] be finished. hanjāftan, hanjām- [hnc’tn', hnm- | P hnj ft, hnjm-, (M hnzpt, N anjāmīdan)] finish, complete, carry out. hanjām [kne m | N anjám] end, completion, outcome. hanjaman [hncmn! | (P ?njmn, M hnzmn), N anjuman] gathering, assembly, congregation, community. ~ig [-yk'] (notable) member of the community. hanjīdan [hnc-ytn' | N ~] = hixtan.
595:~ih: bitterness. taxt [2А | N ~] throne. ~ag [-#! | N ~a] tablet, plank, (chess) board. taxtan, taz- [Phtn', tc- | M rem, tz-] run, flow. išnīh : flow. tāxtan, taz- [?Аїп!, Pc- | M Рс-, N ~] cause to run, flow; chase; pour. taxt-gàh [?hig’h | N <] couch. taz-, —išnih, v. taxtan. táz-, v. tāxtan, tazāģ [tc’k'] flowing, running. tāzānaģ [P enh | N tāz(y)āna] whip. tazënidan, tazën- [tcyn-ytn'] = tāxtan. tazidan, taz- [tc-ytn'] = taxtan. Itázig [Pcyk! | N tázi] swift, fast. "Táüzig [Pcyk! | N tāzi] Arab. tēmār [tym] | M tym’r, N ~] sorrow, grief, care. ltërag [tylk' | N tēra] dark, turbid. *térag [tylk'] (mountain) peak, summit. téx [tyh | N téy] sharp edge, ridge; ray. Mēz [tye | M tyz, N ~] quick. ~ih: speed. *téz [tye | (P tyj), N ~] sharp. ~ih: sharpness. *tidag [tytk' | (N dida)] pupil (of eye). tigr [HTY A < А Шу; tgl | M tygr, N tir] arrow. *tihóg [tyh:wk! | N tihi] small grey partridge. tir, v. tigr. Tir [tyl | M tyr, N ~] a god (confused with Tištar); astr. Mercury; cal. 4th month; 13th day. tis [MNDOM < А mnd‘m; ts | M, J tys] thing, affair. «iz [-c | M -yc] (with a negative) по... at all. tišn [tyšn!] thirst. tišnag [tyfnk! | M tyšng, N ~a] thirsty. ~th: thirst. Tištar [гуй | № ~] astr. Sirius. të [LK < A l-k | M tw, N tu] thou, thee. *tóf [twp | N to] layer. tóhmag [twhmk' | M twhmg, N tuxma] seed; stock, family. tom [t(w)m | M tm, N tam] darkness. -tom [-twm | (M. -dwm)] suffix forming superlative adjectives. tóm [twm | (M twhm, N tuxm)] seed, family. tórag [twlk' | N tora] jackal. tūšag [twšk! | N tófa] provisions. tóxtan, töz- [twhtn', twc- | M twz-, N ~] atone, expiate. ~išn: atonement, expiation. tóz [twe | N ~] bark, skin.
1495:dawn bamdad, ēš, ós(e)bàm.
1496:dawning wizīhišn(ih).
3490:run dawīdan, (dawistan), póy-, tax- tan, (tazidan); (daevic) dwāridan, (dwaristan); cause to ~ tàxtan, tazénidan.
4944:daw-! Jdawistan! Jdawidan! (215) wuzurg!
5417:dostih dëst l*?dawistan dūpāy gubrāg gubrās- guftār guftārīh guftan
=== NYB ===
5126:dawrā-maēšī: davr
```


## [2026-09-05T20:05:53.527Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON traxom ===\"; grep -n \"تراخم\" MON_part1.txt MON_part2.txt incoming/MON/*djvu.txt 2>/dev/null | head -10; echo \"=== ARY dovidan ===\"; grep -n \"دویدن\" incoming/ARY/ARY_pages.txt | head -10"
}
```


### [2026-09-05T20:05:53.626Z] TOOL RESULT

```
=== MON traxom ===
MON_part1.txt:39489:تراخم: همق:د) (.) (بز.) مرضی است که 
MON_part1.txt:44712:جوش پلکث؛ تراخم. 
MON_part1.txt:44720:جوش‌های تراخمی بصورت گرد (پودر) 
MON_part1.txt:78474:تراخم» ریزش مژه‌ها. 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:36547:زاید جفن: (پز.) تراخم. گوشت شت گاو و 
MON_part2.txt:36547:زاید جفن: (پز.) تراخم. گوشت شت گاو و 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:39489:تراخم: همق:د) (.) (بز.) مرضی است که 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:44712:جوش پلکث؛ تراخم. 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:44720:جوش‌های تراخمی بصورت گرد (پودر) 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:78474:تراخم» ریزش مژه‌ها. 
=== ARY dovidan ===
5889:چم این واژه در اوستایی و لیترانی و افغانی؛ دویدن» جاری شدن.
6588:چم این واژه در زبان پهلوی: دویدن؛ شتابیدن,
8537:دویدن, دو / ۲۹۱
8561:چم این واژه در زبان‌مالهنر و اروپایی کهن: دویدن» جاری شدن. :
```


## [2026-09-05T20:05:54.239Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT dav ===\"; grep -n \"^• *[jg]\\.* *dav-\\|dav-  \\|1dav-\\|'dav-\" BRT.txt | head -20"
}
```


### [2026-09-05T20:05:54.293Z] TOOL RESULT

```
=== BRT dav ===
3240:•  j,  adav-  (,  p.  adav-)  f.  'Wasserlauf; Bach,  Kanal':  us  . .  apqm  °oavd  apaiti.- »nti  Jasanti  Yt  Ä  29.
7594:11  hindav-  No.  1 ;  doch  vgl.
8580:AbleiL  iMui-Yhiniitni-;  vgL  iBed.  ai.  udanlya- Adj,  —  «)  NA.  getrennt  und  mit  i  stall  j; s.  F  I  usv-,  IQ  Aiadav-  and  No.  3.  —  'J  In mp.  Schriften  usind,  usindam  genannt;  vgl. SBE.  47.   160.
12556:'dav-.
12797:•  j.  'dav-  V.  'sprechen',  von  rftfaischen Wesen''.     Praes.  2  dava-.
12801:*dav-  688
12806:•  j.  *dav-  V.  'entfernen'.  Praes.  3  dava-, 4  dva-.
12810:•  j.  Jdav-  V.,  nur  mit  /ra  'reinigend  ab- reiben'.    Praes.  i  dava-.
12813:•  g.  <dav-  V.  '(sich)  diHngen'.     Praes.
13674:Ableit  —  Znin  V.  'dav-.  —  ai.  dül6.  m.  — Fü. :  daväi  (zu  np.  danidan  *laufen']  oder gäiuäk  (in  ap.gußan);  s.  10  düfya-.  Dazu  die Erl.:  räyhütär.
15932:•  j.  pazdav-  m,  Name  schädlicher  Klein- tiere, etwa  'Käfer,  Made' :  baevan  'dunam gäks.varttanqm  (sd.)  ava.JanySl  V.  14.  6,
21505:a\.ydsyaH,  yf^ati;  yas/äi;  np. jasian  (?,  GlrPh. /b.  139),  PDw.  yaiin  {?,  GlrPh.  /  b.  Z98).  — PQ.!  »da«  ßaa,  •eitUait,  Sä.  {lu  Y.p):  mala- vatT  'schmutzig'  (,  weil  man  hixr°  Im)*}.  — ')  Nicht  ganz  sicher,  da  'l>ni°  fiir  'siitf  ge- schrieben sein  kann;  s.  hindav-  No.  I.  — ">  /  müEste  vom  redupl.  Praeseos  stammen. Statt  yaihliiyS  im  Text  schreibt  DST,  in  der Note  yokiH'.  VII.  ist  beide»  falsch.  Ob yaihnübyöt  —  J)  Vgl,  No.  i.  —  4)  M  hat aestnüm,  K  yaisinlim;  s.  noch  No.  I.  — S)  Und  deshalb  überwallenden.  —  «)  Vgl.  Dst. ZA,  3.  II.  Jamaspji  Gloss,  475-  476  bat aySrRjn^d  'surpasses', j.  yahi  Yt.  10.  64:  lies  yalimi;  5.  ya-  mit No.  17.
22913:Ableil.  aus  'var>du-iam-  "was  aus  weicher Erde  besteht'.  *var>dav-  Adj.  sva.  vatidva-; vgl.  ai.  fbhiv-  und  j-bhvä-  Adj.,  yakäs-  und yaki/ä-  Adj.  —  Pü. :  mim  tamtk.
23031:—  4)  Hdi.  vtrixanOm.  —  S)  Sollte  vmänüm «ein.  Geringe  Stelle.  —  *)  Vgl.  iBed.  np. varz,  iari  'Feldarbeit,  Ackerbau'.  —  7)  So  T; s.  hindav-  No.  I.  —  *)  Hds.  virnant'.  — 9)  So  K  7  ■.  NA.  yä/qm,  Pü. :  varsisnak.  — «•)  S,  »Bed,  Gdh.  BB.  12.  98.  —  »')  Pü. :  an i  aoiäi  ape  vartÜn,  —  ")  PO.:  an  släyUn M  nyäyäti  an  i  amäi  ape  ■Borvsn.  —  'J)  Ptt.  1 uniariitan,  erL  (zu  V.  7^):  apäl  karlati,  (zu V.  4,  13)  i  api  vicärlBH.
23196:ai.  vihati,  ukyäte  (Praet.  37,  Fass.]^  uhl,  vaksai; ; udhäh,  vähadhyai;  mp.  voiSlan  'dahin fahren', , rp.  i'.ijrH'fl« 'wehen',  afj.  po/ii/ 'fliegen' (Praes.  I vuzt],  sbal,  gvcaag,  ZDg.  vailmün  'laufen'.  — Pü. !  vaätan,  vazemlan;  s.  noch  No.  6  ff-  —  ' I)  Nur  im  Abiol.  —  '>  S  W  H;  »■  dagegen  • ai.  üijh^.  —  »  S  /a/  g.  Wertlos  Wilhelm  | Mus.  3.  600.  —  4)  Stall  vaänii,  lu  S  325  No.  ■ S.  hindav-  No.  I.  —  s)  Them.  —  &)  Pü. : vastnit;  s.  zu  vaou  Inf.  —  7)  Es  handelt  sich  | Dm  einen  Kamof,  bei  dem  die  Entscheidung nicht  fallen  will.  Anders  Gdn.  sYI.Si,  Dst. ZA.  3.  572.  Npü.  (fOc  vailiakS):  ml gardadA —  S)  Pü.:  nap  an  (Mills  iivawfn),  Sü.:  svämi-^ iämitü.  —  9>  Unsicher;  vlL  haplol,  für *avcaa>:  —  ")  Fehlt  in  Pü.  —  ")  Pü.  erL; buland  e  sar  .  .  fröt  ö  bun.
24802:ai.  risyixii  'ei  tut,  nimmt  Schaden',  refäyali 'er  tut  Schaden',  ri}/iiA;  mp.  resilan.  —  Pü. : reiitan,  zu  3  a  erl. :  api  murtan.  —  ■>  Pü. : ku  ne  an  i  pas  Ö  i  pis  etön  relet.  —  ')  S.  zu hindav-  Nu.  I.  —  J)  Hds.  'hntanqm.  —  4)  Hd». airiyq.
25567:Vgl.  BgE.  wrig^an  USW.l  HBIL  IF.  //.  lOa  — Pü. :  variVan.  — ')  )  «att  i  für  y^,  vgl.  No.  8. S.  hindav-  No.  I.  —  •)  In  aA%5iriSta:  — J)  Hd».  urvityeiU;  Fü. :  fehlt.  —  «  NA.  'saiU; j.Vat.  —  S)  S  363.  44.  —  *)  NA,  'urvaiiaiU;  l. Var.  —  7)  S  368.  31.  —  ")  So  Fl  uiw.j  NA. 'tirtti;  t.  No.  I.  —  9)  NA.  'saiH',  ■.  Var.
29945:•  j.  hsndav-  m.:  s.  unter  Aindav-,
30065:•  p.  hi^dav-  m.:  s.  unter  kindav-.
30076:•  j.  bindav-,  h«ndav-",  p.  hi°dav-  m. Name  eines  Lands,  Indien:  II  imä  dahyava^ tyä  adam  agarbäyam  . ,  'du/  D.  5.  3 ;  5.  2 ; —  Aaca  us'as/ara  'dva  avi  daolastanm 'dum  V.J.  r8  PiiZ.;  —  yH^i  ulastaire •dvS  *ägiurvayeiii  yatSt  daoiataire  niytu "auch  wenn  er  im  Östlichen  Indien  ist, er  packt  (ihn);  auch  wenn  er  im  west- lichen ist,  er  schlägt  (ihn)  nieder"  Y. 57.  2g.  a)  mit  Aapla  'sieben'  dn.: paniadasfm  asunhamca  . .  frä'^wirtsfm  . , yS  Aapta  'du  (AP.)'»  V.  /.  i8.
```


## [2026-09-05T20:06:01.889Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '12790,12816p' BRT.txt; echo \"===== 13665-13676\"; sed -n '13665,13676p' BRT.txt"
}
```


### [2026-09-05T20:06:01.960Z] TOOL RESULT

```
daya-
". .  der  . .  Reinigimgeo  vonümmt,  (aber) mit  der  .  .  Religion  nicht  vertraut  ist" V.p.  53,         äim,  dit  als  Pait.  sbes.
Aus  dem  Zusammenhaug  gerissene  oder sonst  undeutlich:  Stellen:  ahmt  'im  paiti franhfn%at  V.  2.  j  PiiZ.;  —  yai,cit  'im dava  . .  T.^4'}  —  yaica  *'im  .  ,  Vyt.47i
—  «äV  zI  dj  yä  pastt  vJra  maästya  di iatSis..manayJl{&A.)  DkB.  131.
Sonat  idcht  nichweisbar;  ar.  d'  oder  dh'.  — Das  Fron,  ichliesst  sich  in  das  ersle  Wort des  Satzes  an,  von  dem  es  ntu  doich  ein andres  Enklitikam  -  wozu  aach  äal  N,  jSf. nnd  Aa  Vt.  ir.  zi  gerechnet  werden  dürfen  - getrennt  werden  kuin ;  t.  noch  No.  a,  5 ;  TgL W«.  IF.  r.  30s,  0,0.  Fron,  55,  —  Pn,:  ä, an;  (Flor.)  äJän;  aach  we^elassen.  —  ')  So Fi;  na.  hat  überall  din.  —  >)  Wo  an  zweiter Stelle  die  NA.  falsch  intetjningirt;  1.  Bthl. IF.  13.  143.  — J)  So  Fa.  NA.  hu  dwi,  was aach  lonat  oft  als  Variante  bezeugt  ist,  zB. Y.  Ä  a  (Pt  4\  5.  I,  ig.  11,  Yu  la  1  nsw.  — 4)  Die  Verbindung  aa/  du  ävati^  wird  viel- fach formelhaft  gebraucht  —  S>  Gegenüber WM.  IF.  /.  405  TgL  FoT  KZ.  57.  7  No,  3. Erklärt  sich  die  Stelinng  TOn  äi  durch  die Tonlosigkeit  des  Verbamsim  Hauptsatz?  — ^)  Konstruktion  nach  dem  Sinn.  —  7)  Wie Eü.  zeigt,  aaf  käram  zu  beziehen,  nicht  auf imaiy.  —  ")  Mir  scheint,  es  habe  im  Iran.  za> : nächst  überhaupt  nur  *dim  gegeben,  das  den Akk.  aller  Zahlen  und  Geschlechter  zu  *kai, ' *sai  (j.  ke,  st,  p.  iaiy)  bildete,  —  «  VgL  hin und  das  Umgekehrte  bei  It  (zu  i^ou-),  Ae.  —  | '•)  VgL  dazu  Y.//.  15,  via  pairi  ti  tatiava  aam  , .  .  KrDäium  hau  oHStäl  aiikaa^.  \
•  j.  daya-  m.  —  ?— :  paityänm  ake  frä-\ lünniat  atirS  mainyus  skaillm  (sd.)  yqm gavaca  'yaca  pouru.mahrkfm  V.  7.  4''.
Pü.  da  dt.  —  >)  S.  tu  statay-.
•  j.  'dav-  V.  'sprechen',  von  rftfaischen Wesen''.     Praes.  2  dava-.
Nur  Med.  'sprechen,  sagen,  reden'; i)  mit  Aklc  des  Gesagten:  dalva  drvants .,    ayqm    äaci%rfm    däunta'^    V, /(j.  45;
—  uspatat  Jranroie  .  .  ayqm  daoihrim daomns'*  Yt. 75,57;  —  aHs  daksk5  .  . saxsä^nm  daomnö*'' \t.ig.\T.  3)  das Gesagte  folgt  in  direkter  Rede:  adavtita (Augm.)  avrS  mainyuf:  mä  .  .  H.  2.  35; Yt^.  14;  —  ktnsanJm  ..yS  davata:  nsit «?  .  .  Y.  5.  34;  —  advännta  adäunta (Augm.)  dafva  V.  ig.  45;  45,  47.  a)  mit uiti:  uiti  davata  Äi  y}  .  .  ai?rö  mainyus; drvxf  upa.dvilra  V.  ig.  i ;  44,  Yt.  77.  1 9, Vyt^;  —  büiyqsta  .  .  uiti  aoj?mna  uiti daomna:  yfafsata  .  .  FrW.  10.  43.
mit  paiti  'antworten',  mit  Dat.  der  Fers.
*dav-  688
und  folg.  dir.  Rede:  paHi  a&mai  adavata (Augm.)  .  .  aarB  mainyui:  mä  ml .  .  V. ig.6;  —  druxi  hl  paiti jd<tvata:skiäara .. v.ig.y,  JA  31.
mit  /r3  nnd  vi  'hin  und  her  reden': fradavata  vtdavata  fi-amof^fota  vlmaigiata ar»HJ  mainyu/  "es  redete  hin,  es  redete her,  es  überlegte  hin,  es  Überlegte  her AM.''  V.jp.43.
mit  vT:  s.  bei  JrS.
mp.  (Pü.)  dm/istan  i),  PDi.  war-^aam  "ich  rede an»  dem  Schlafp).  —  ')  Im  Gegens.  zu  mrav und  vai-,  t,  H.  2.  \^,  35  twd  V.  ig.  6,  7.  — •)  Statt  davi',  %  36S.  22,  33,  3^.  —  S>  Hos.1 NpEt.  17  a.
•  j.  *dav-  V.  'entfernen'.  Praes.  3  dava-, 4  dva-.
'forttreiben,  for^agen':  *apala  vh  samar? ana  dttyc**^  (iSPM.)  "fort  ja^e  ich  euch damit  (zurück)  in  die  Erde"  Yti.  39.
mit  avi  und  frä  Med.  'mit  sich  fort- führen, fortreissen',  vom  Wasser:  yäha masyaya  äß  kasyanhqm  apqm  *avi./rä- '  iavaite'^  "wie  ein  grösseres  Wasser  kleinere Wasser  mit  sich  fortreisst"  V,  5.  34.
Vgl.  «i.  doj'i/äm,  dmiasänaioA  (usw.),  gr.  Jm- !  luu  (usw.);  IF.  13.  137.  —  S.  noch  dita-, düta-,  äittiaalam,  daibitä.  —  Pü.  (zu  Yt.):  fa lamii  daMil,  (zu  V.) :  apar  fräl  boret.  —  ')  So nach  J  10,  F  1  nsw.;  s.  BXHU  IF.  It.  136.  — *)  Jpl,  Mfa;  NA.  -ti.
•  j.  Jdav-  V.,  nur  mit  /ra  'reinigend  ab- reiben'.    Praes.  i  dava-.
Med.  'sich  abreiben  mit  — '  (Gen.): aOaesamca  t>mS  p3riiu.ß'avaii{si.)  /rata- vata  {3S,)  V.ß.  29.
ai.  dhävalt ;  np.  aiutüdan,  tidüdan  (HOKK  GliPh. /  b.  130).  —  PiL ;  fräe  e  tanSiid,  erL ;  xäfi  afie i  ianäiid.
•  g.  <dav-  V.  '(sich)  diHngen'.     Praes.
I  daV'  :  du:
i)  'drangen,  bedrängen':  mS  urva gSuscä
atyä  (sd.)  Ayat  maiäqm  dvaidi  (iDftM.)"
===== 13665-13676
•  j.  kaia  suraya  ayaca   tl  diiänaya"'    .  baxsätii  Yl/o.iio.
Vyt  5'-  I      Behrort  Ton  aaiiiiay;  etwa  'drückend,  qnilend'.
dby  Google
749
düta-
duraedarSt^ma-
7SO
dahfAt-  -  vgl.  Yt.  J-p.  94  f.  und  K5  {(ür  dul- xra^iiiä  zu  Y.  4g.  4)  -  passt  nicht.  —  •)  So  F 1.
•  g.  düta-  m.  'Abgesandter,  Bote':  äioffi "täwkS  hakamä  mg  iiärayB{sd.)  ..y.32.  i.
Ableit  —  Znin  V.  'dav-.  —  ai.  dül6.  m.  — Fü. :  daväi  (zu  np.  danidan  *laufen']  oder gäiuäk  (in  ap.gußan);  s.  10  düfya-.  Dazu  die Erl.:  räyhütär.
•  g.  dütya-  n.  'Botschaft":  maraxtärS jigirsiai  (sd.)  kämt  %wahyä   mq>:rSne  Y.
Ableit.  au»  däla:  —  ai.  dSlyä-  n.  —  Pü.: davH^I  oitt  göiuSk  {s.  IM  düta-),  mit  der  Erl,; pesfSi;  Sil-;  puraksarafi.  —  •)  Wegen  Sü.  die wahrscheinlichere  I-esung,  sva.  "Läufer';  NpQ. allerdings  güyi.
```


## [2026-09-05T20:06:19.380Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KNT dav ===\"; grep -n \"^dav\\|to run\" KNT.txt | head -10; echo \"=== MON 39489 context ===\"; sed -n '39485,39495p' MON_part1.txt"
}
```


### [2026-09-05T20:06:19.443Z] TOOL RESULT

```
=== KNT dav ===
=== MON 39489 context ===
تراجیح. حلقها [ع.] (مص‌م.) ج. . ترجیح. 
نزونی‌ها. تعادل و تراجیح: منک 3 
فرونی» برابری و پیشی. 

تراخم: همق:د) (.) (بز.) مرضی است که 
چشم را عارض می‌شود و موجب پیدایش 
جوش‌های عفونی در مخاط یلک بالا شد ه 
و پبلک را از حالت معمول ضخیم‌تر 
شیف قزی اس معالحه شود موجب 
ناراحتی‌های شدید می‌گردد و عاقبت منجر 
به کوری می‌شود.
```


## [2026-09-05T20:06:20.144Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==360' BQT_v2_pages.txt | head -40"
}
```


### [2026-09-05T20:06:21.848Z] TOOL RESULT

```
 ‫دوکار ‪:‬‬                                                                                                        ‫تس‬


‫پبازرا گوبند‬      ‫انی وساد بی قطه‪ .‬بلغت ادلمغرب‬              ‫بمعنی دشوینه است که ظرف شیر دوشیدن‬
                                                                                                                ‫باشد ‪¥.‬‬
                              ‫وبعربی صل خوانند *‬
                                                             ‫‪۰‬‬        ‫‪۰‬‬    ‫‪۰‬‬     ‫‪"°‬‬              ‫‪۴‬اه‬   ‫ه‬   ‫‪۵‬‬

‫تخم‬     ‫کو کو »‬   ‫بروزن‬   ‫باقاف‬    ‫‪-‬‬   ‫قوه‬   ‫دو‬
                                                                                                           ‫باشد ‪۰‬‬    ‫‪“a‬‬   ‫‪۱‬‏‬
‫زردك صحرابی است‌وییخ آن شقاقل است ‪.‬و گیاه‬
‫آنرا خرس گیاه خوانند » چه خری آنرا بسیار‬                         ‫دشویز ‪ - ۱ ۵‬بازای«وزبروزن‌یوشد‪.‬‬
                                                                                                 ‫دختر بکر را گونند ‪۰‬‬
                                        ‫دوست مسدارد ‪۰‬‬
                                                             ‫دو طفل بسند یف ه ‪-‬کنابه ازمردمان‬
‫بسکون سین بی نقطه ‪,‬‬                    ‫دو فوس‬
‫لغتی است بونانی ‪ ۱‬بمعنی دوقو که تخم زردك‬                                                    ‫چشم باشد ‪.‬‬
 ‫صحرایی‌باشد‪ .‬وبعضی کویندنوعی ازآست ودآرا‬                        ‫دو طقل نود ‪ -‬بمعنیدوطفل‌بندیده‬
‫بشیرازی بدران خواشد ‪ ,‬وبعضی دبگ رکفته اند‬                                        ‫است که مردمان چشم باشد ‪.‬‬

              ‫فمس صحرایی است‬     ‫رتخ‬‫کوس‬
                                      ‫دوق‬                        ‫از دو لب مهوت‬   ‫کنابه‬       ‫=‬    ‫طوطی‬         ‫دو‬



                                  ‫دولك ‪۷۰‬‬                                                              ‫ومعشوق باشد ‪.‬‬
‫‏‪aa‬‬
                                                                 ‫دوعلوی ‪ - ۲‬کنابه اکزوکب زحل‬
             ‫دوك‬                  ‫رسمانرسند‪.‬‬        ‫يدان‬                                            ‫ومشتری باشد ‪*# ۰‬‬
                                                                 ‫دوغبا ‪ = ۴‬باغین‌نقطه‌دار بروزن شورباء‬                         ‫‪:‬‬
 ‫مقراض راکوبند مطلقاً وبعربی جلمان بر وزن‬                                        ‫ای هاش وعاستانه رگاونشد‪.‬‬
‫وبمعتی‬     ‫سلمان خوانند وهربكث را جلم گویند ‪-‬‬
                                                                 ‫دو عو ‪-‬بروزن کو کوء باقیماندة چیزی‬
‫حلقی هم‌آمده است » وآن ضربتی ومشتی باشد‬                      ‫ودرته دیگ وباتل‬          ‫ماد‬         ‫که روغن | فراگرفته‬


 ‫که برزیر گلو زند وآنرا دوکاردی یز گویند‬                                                                            ‫بماثك ‪.‬‬
                                         ‫ماضافةٌ تستالی ‪.‬‬        ‫دو فص ‪٣‬‏ م اول وقاف و سکون‬

  ‫‪ ۱‬از ‪ :‬دوش ( دوشیدن ؟) ‪ +‬ایزه ( ایو ‪ .‬يولد صفیر ) ؛ لغة دختر دوشنده‬
```


## [2026-09-05T20:06:29.060Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==359' BQT_v2_pages.txt | head -50"
}
```


### [2026-09-05T20:06:31.116Z] TOOL RESULT

```
     ‫—~‪—~AAA‬‬                                                                                                               ‫دوسرألی‬

 ‫ژولیده» بمعنی چبیده(‪)٤‬‏ وخودرا چسبایده(ه)‬                      ‫دو سرالی ‪ = 1‬بفتح اول بر وزن لن‬
                                   ‫باشد ‪.‬‬                              ‫ده وسطبر وبزر که باشد‪.‬‬
                                                                                            ‫کعننی‬
                                                                                                ‫ترالی » بم‬
     ‫نش ‪ ۰‬بمکعنتیف‬
                 ‫دوش م بر وگزو‬                                   ‫دو سر د هلیز ‪ -‬کنابه از عناصرارعه‬

‫و امر‬           ‫باشد ا ‪ -‬وش گذشته را نز گونند ‪۷‬‬                        ‫‪-‬ای خمه را نگیوزبند ‪.‬‬
                                                                                           ‫حو‬‫اوست‬
                   ‫از دوشیدن هم هت نی بدوش ‪.‬‬                    ‫«ابه‌ازهفت کوکب‬
                                                                              ‫دو سر قندیل کن‬
                                                                ‫است ‪ -‬وهرستار روشن را نز گفته اندو کنابه‬

‫که انرا مسد‌وشند همجو گوسفند وگاو و امثال‬
                                                                                                         ‫‪.‬‬     ‫از فلك هم هت‬

         ‫تهه‬
           ‫اهشهرچ‬
                ‫دت ک‬
                   ‫آن ‪ -‬وکنابه ازشخصی اس‬                        ‫دو سر ی = بفتح اول بروزن کوثری '‬
                           ‫باشد ازو بتدریج بگیرند ‪.‬‬             ‫بمعنی‌دوسرالی است که‌بزر کههوسطبرو گنده‌باشد‪.‬‬
                                                                ‫دوسنك ‪ ۴‬ب باانی جهول بر وزن‬
‫داشته باشد وآنرا بگرردن مجرمانو کناهکاران‬                              ‫موبند » بعنی بچسبند(‪ )۱‬وملاصق شوند ‪.‬‬
     ‫‪.‬‬     ‫گذارند ‪ -‬ولوعی از پنکان دوشاخ هم هت‬                  ‫دو سنكه ‪ = ۴‬بروزن دوزنده * بمعنی‬
                                                                ‫چبنده (‪ )۲‬باشد ‪ -‬و زمین لغزنده ‪ -‬وگل‬
‫ان کنابه‌ازشادی کردن‬            ‫بر‬    ‫دوش‬
                                                                ‫چسبنده(‪ )۲‬را نگیوزنند ؛ ویکسرثالث هبمنظر‬
                                                   ‫باشد ‪.‬‬
                                                                                                                      ‫آمده است ‪.‬‬
 ‫دوشنه ‏‪ - ٩‬م اول و ثانی مجهول‬
                                                                ‫دو سین = بر وزن بوسیدن » بمعنی‬
‫وفتح ثالث و نون » ظرفی باشد که درآن شیر‬                         ‫چسبیدن(‪ )۳‬وملصق شدن ‪ -‬ورسدن‪ -‬ولغزندن‬
                                               ‫‪.‬‬   ‫دوشمد‬
                                                                                                                           ‫باشد ‪. ۴‬‬
 ‫اهس بائانی مجهول بوزن خوشه؛‬
                           ‫د"وش‬                                  ‫دوسیده * ‪ -‬با ثالی مجهول بورزن‬

                                           ‫‪۰‬‬       ‫چپنده‬    ‫)<( چك‪:‬‬                ‫‪.‬‬       ‫‪ :‬بجسپند‬      ‫چك‬         ‫(‪)۱‬‬


                                           ‫چش ‪ :‬چپانید ‪.‬‬               ‫()‬              ‫‪.‬‬       ‫چیید»‬    ‫چك‪:‬‬         ‫‏(‪)٤‬‬



          ‫؟ ‪.‬‬   ‫جمم ممارع از « دوسیدن‬    ‫‪ -‬سوم شحص‬                                     ‫رك ‪ :‬دوصری ‪.‬‬                   ‫‏‪١‬‬


                ‫‪ _ ۴‬متعدیآن «دوسانیدن ‪( ¢‬ح‪.‬م‪).‬‬                     ‫ة‬       ‫اسم فاعل از (دوسدن»‬                  ‫=‬     ‫‪۳‬‬
```


## [2026-09-05T20:06:40.269Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='ignore').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    for w in ['دویدن','دونده','پادو']:\n        if w in p:\n            print('leaf',i,'≈p',i+543,'|',w, p.count(w))\nEOF"
}
```


### [2026-09-05T20:06:41.959Z] TOOL RESULT

```
leaf 348 ≈p 891 | دویدن 3
leaf 350 ≈p 893 | دونده 1
```


## [2026-09-05T20:06:44.663Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==349' BQT_v2_pages.txt | grep -n \"دویدن\" ; echo \"=== full leaf 348 head ===\"; awk 'BEGIN{RS=\"\\f\"} NR==349' BQT_v2_pages.txt | head -60"
}
```


### [2026-09-05T20:06:46.368Z] TOOL RESULT

```
19: ‫‪ ¥‬دو ] تش ‪-‬کنابه از دوب معشوق | وزن روارو » دویدن بهرطرف باشد از پی‌هم ‪-‬‬
33:                                                                  ‫(دویدن) د اسشق ‪ 6۷۵‬دوم “ ‪.‬‬
43:                       ‫‏‪ - ٩‬از ‪ :‬دو (دویدن) ‪( ۱ +‬واسطه) ‪ +‬دو (ایسا) ‪.‬‬
=== full leaf 348 head ===
    ‫یات‬                                                                                     ‫دله گرقه‬

‫دلین ‪ = ۴‬بر وزن رسیدن ‪ .‬بمعئی‬
 ‫دوبدن بنشاط و بخوشحالی براه رفتن باشد ® ‪-‬‬           ‫نعمت الهی باشد ‪ -‬و بمعنی خوشحال و شادمان‬

 ‫وبمعنی ازجای دآر‪.‬دن ‪ -‬وازخشم وقپرجوشیدن‬            ‫را لىز‬   ‫و تند براه رونده و دوفده‬        ‫هم همست‬

                                   ‫همگفته‌اند ‪:‬‬                                              ‫کفهداند ‪.‬‬


         ‫راه رفته ناشد ‪۳‬‬   ‫بخوشحالی‬    ‫خرام ده و‬
                                                     ‫وخوشحالی‌بخرامی‪ -‬وبعریی‪ ۴‬مردم دون وخیی‬
                                                                                            ‫رکاویند ‪.‬‬


                                         ‫بان نورد هم‬


 ‫‪ ¥‬دو ] تش ‪-‬کنابه از دوب معشوق | وزن روارو » دویدن بهرطرف باشد از پی‌هم ‪-‬‬
‫شوخصی را نکیوزبند که خدمات جزئی باو‬                                                               ‫باشد‬
     ‫رجوع باشد وهرساعت اورا بکاری فرستند ‪.‬‬
                                                    ‫دواج ‪ = ۲‬بفتح اول بر وزن رواج »‬
‫دوادی ت بفتح اول بر وزن نهاری »‬                                             ‫یمعنی لحان باشد ‪. ۸‬‬
‫از آن به‌ینج‬   ‫رایج ازطلا که هرك‬   ‫زری‌بوده‌است‬


 ‫وال ابجد بد | شیالی خرح میشده " وشیانی زری بوده الزای‬
                                                     ‫دوادو ‏‪ = ٩‬بفتح اول د‬

       ‫(عر) بتشدید اخرآمده ‪.‬‬
                           ‫‪۴‬‬                   ‫؟ ‪۴‬‏ رك‪ :‬دیدن ‪.‬‬          ‫رك ‪ :‬دنه ‪.‬‬      ‫‪۱‬‬
   ‫از ‪ :‬دن ‪٣‬‏ بدن(یسوند مصدری) ‪.‬هندی باستان » ره ‪_131d‬‏ ‪62040020 ,‬‬                      ‫‪۴‬‬
                                                                  ‫(دویدن) د اسشق ‪ 6۷۵‬دوم “ ‪.‬‬

  ‫بر خم همی خرامی و بردن همی‌دلی ‪.‬‬                 ‫‌بهرمی‌شینی و ب رگل همی خوری‬
                                                                              ‫®ل‪-‬‬
                                                                                ‫گ‬
  ‫«‪+‬ءنوچهری دامفانی ‪۹۰۱٩‬‏ ‪.‬‬
   ‫‪ - ۷‬طبری [‪ .2۷04‬ز‪( 4۷40‬لحاف)‪ .‬مدارزانی‬                    ‫‪ - ۷‬اسم‌مقمول از«دنیدن» ‪.‬‬
                                      ‫کنوی [‪ . ۵۷61‬ز‪ . 24‬زا ‪2[ .‬ظ‪ 0‬دواژه نامه ‪. 4۹۳۰‬‬
           ‫همی غلطم اندرمیان دواح ‪.‬‬                     ‫یمآگه از اسل وفرع خراج‬                ‫‪۸‬‬
  ‫فردوسی‌طوسی‪« .‬چهارمقاله‪.>۸4‬‬
                       ‫‏‪ - ٩‬از ‪ :‬دو (دویدن) ‪( ۱ +‬واسطه) ‪ +‬دو (ایسا) ‪.‬‬
 ‫که ‪« ۷۵-۸۵‬منای‬
              ‫‪ #‬دو ‪ -‬م اول (‪ , )00‬پهلوی ‪ , 80‬از ره ل‪« © 13۷‬ریی‬
 ‫‪.‬ردی لال ‪.‬‬‫‪ > ۲۷‬بارسی باستان ‪( 3103۷0۱ -‬دومن) ‪ .‬اوستا ‪( 2۷‬دو) » پازند ‪ ۵4‬ک‬
  ‫‪ . 0‬افمای ‪ . 2۷1‬استی ‪8۷‬ا‪ .1‬وخی ‪ ۰ 099‬سریکلی لوطل ‪ .‬شفنی ‪ » 624‬یفنوبی‬
     ‫ف‬
     ‫صد »‬
        ‫و متکلیجی لا " منجی ‪ « 0‬اسشق ‪ » ۵۷۵‬؛ عدد اصلی بين يك و سه » ضمف واح‬
                                                                ‫چهار ‪ .‬انان ‪.‬‬
```


## [2026-09-05T20:07:10.368Z] TOOL CALL #32: Bash

```json
{
 "command": "sed -n '1,60p' tools/ref_page.py; ls data/verification/sources/refs/incoming/BQT/"
}
```


### [2026-09-05T20:07:10.453Z] TOOL RESULT

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
BQT_v3_pagemap.json
BQT_v3_pages.txt
BQT_v3_picofile.pdf
BQT_v4_pages.txt
BQT_v4_pages.txt.pages
BQT_v4_picofile.pdf
BQT_v5_pages.txt
BQT_v5_pages.txt.pages
BQT_v5_picofile.pdf
```


## [2026-09-05T20:07:30.277Z] TOOL CALL #33: Bash

```json
{
 "command": "grep -ho '\"ref\": \"BQT[0-9]*:[0-9]*\"' data/verification/page-*.json | sort -u | head -30; echo ---; python3 - <<'EOF'\nimport json,glob,re\nfor f in sorted(glob.glob('data/verification/page-1*.json')):\n    d=json.load(open(f))\n    for e in d['entries']:\n        for n in e.get('nodes',[]):\n            for rc in n.get('ref_check') or []:\n                if rc.get('ref','').startswith('BQT') and 'leaf' in (rc.get('note') or ''):\n                    print(f, rc['ref'], rc['status'], rc['note'][:300]); print()\nEOF"
}
```


### [2026-09-05T20:07:32.328Z] TOOL RESULT

```
"ref": "BQT:102"
"ref": "BQT:103"
"ref": "BQT:1063"
"ref": "BQT:1077"
"ref": "BQT:1086"
"ref": "BQT:111"
"ref": "BQT:1175"
"ref": "BQT:1203"
"ref": "BQT:1225"
"ref": "BQT:1254"
"ref": "BQT:1275"
"ref": "BQT:13"
"ref": "BQT:1309"
"ref": "BQT:137"
"ref": "BQT:1382"
"ref": "BQT:1385"
"ref": "BQT:142"
"ref": "BQT:1437"
"ref": "BQT:1445"
"ref": "BQT:145"
"ref": "BQT:1452"
"ref": "BQT:1455"
"ref": "BQT:1485"
"ref": "BQT:1488"
"ref": "BQT:1494"
"ref": "BQT:159"
"ref": "BQT:164"
"ref": "BQT:169"
"ref": "BQT:173"
"ref": "BQT:1748"
---
data/verification/page-105.json BQT:626 supports Found at BQT_v2_pages.txt leaf 84 (printed ≈ 627 on the leaf+543 offset, i.e. Nourai's 626 within the ±3 drift of that volume): headword «چراغ ـ بروزن فراغ؛ فتیله‌ای باشد که آنرا با چربی و روغن و امثال آن روشن کرده باشند», footnote 9 «کلمهٔ فارسی است که در آرامی و سریانی و نیز عربی (سراج) وارد شده (

data/verification/page-106.json BQT:676 supports On the same Borhan page (BQT_v2_pages.txt leaf 134 = printed 677) the footnote to چیری reads «... بهلوی čēr ... čīrīh ... ؛ غالب شدن، ظفر یافتن. رک: چیره» — Mo'in gives precisely the Pahlavi forms Nourai puts in this box, though he writes the abstract čīrīh (Nourai čĕrîh).

data/verification/page-106.json BQT:676 partial The entry is at printed p. 677 (BQT_v2_pages.txt leaf 134), one page later than the citation: «چیر - بر وزن میر بمعنی غالب شدن و ظفر یافتن و مستولی گردیدن بر دشمنی باشد - و شجاع و دلاور را نیز گویند»; footnote «اوستا čira (زرنگ، شجاع) «بارتولمه ۵۹۸»». Content supports; page number off by one.

data/verification/page-106.json BQT:1203 partial The Borhan headword سیخ with Mo'in's etymological footnote is in BQT_v2_pages.txt at leaf 667, i.e. printed p. ~1210 by the running offset (leaf+543) — about seven pages after Nourai's citation, so the page number cannot be confirmed. The entry itself is there: «سیخ ... معرب «سیخ» ... ترکی «شیش» ...

data/verification/page-106.json BQT:1203 partial The Borhan footnote to سیخ (leaf 667, printed ≈1210) does mention «ترکی «شیش»» beside the Kurdish/Baluchi/Gilaki forms, but Mo'in only juxtaposes the Turkish word; he does not derive it from Persian.

data/verification/page-108.json BQT:904 partial Borhān-e Qāte‘ vol.2 leaf 364 = printed p.904 (fixed by its own catchline 'بقیه در صفحهٔ ۹۰۵'); the headword there is «دهره» and Mo‘in's footnote 9 reads 'سانسکرت dhārā'. So BQT:904 does give Skt. dhārā, but as the etymon of Persian dahre, not as a member of the *dā- 'divide' family.

data/verification/page-108.json BQT:813 supports Borhān-e Qāte‘ vol.2 leaf 273 (= printed p.813 on the offset fixed by the دهره page): headword «داس» ‘بر وزن طاس، افزاری است که بدان غله درو کنند و بعربی منجل خوانند’, and Mo‘in's footnote 4 to it reads (through the OCR) 'پهلوی dās، هندی باستان dātra-, ... کردی ...' — i.e. exactly Nourai's Sanskrit 

data/verification/page-108.json BQT:333 partial Borhān-e Qāte‘ vol.1 leaf 553 = printed p.333 (fixed by its catchline 'بقیه از صفحهٔ ۳۳۲'): headword «بیدستر» ‘بر وزن بی مسطر، نام حیوانی است بحری ...’ with a footnote carrying Latin-script forms (OCR unreadable). The page has the word, but the analysis attached to it in Mo‘in's Farhang-e Fārsī (rep

data/verification/page-108.json BQT:813 supports vol.2 leaf 273 = p.813, headword «داس» with Mo‘in's footnote giving Pahlavi dās and Old Indian dātra-.

data/verification/page-108.json BQT:904 supports Borhān-e Qāte‘ vol.2 leaf 364 = printed p.904 (its own catchline reads 'بقیه در صفحهٔ ۹۰۵'): «دهره ۹ - بر وزن هره، حربه است دسته‌دار و دسته‌اش از آهن و سرش مانند داس باشد و در غایت تیزی بوده و بیشتر مردم گیلان دارند ... و بعضی گویند افزاری است که بدان غله درو کنند»; footnote 9 at the foot of the sam

data/verification/page-110.json BQT:817 supports Borhan-e Qate' vol. 2, leaf 277 of BQT_v2_pages.txt (printed page ≈ leaf+543, i.e. 817-820; the headword block دام runs from Nourai's cited page). The entry's sense 4 is 'هرچیز که جانوران در آن بفریب گرفتار شوند' = snare, and Mo'in's footnote 4 at the bottom of the page reads: 'هندی باستان dāman- (ب

data/verification/page-110.json BQT:921 supports Borhan-e Qate' vol. 2, BQT_v2_pages.txt leaf 381 (printed ≈ leaf+543 = 921-924, the last page of the د section, next leaf starting ذ): 'دیهیم ۱ ـ بکسر ها بروزن تعظیم، تاجی که مخصوص پادشاهان است … و بمعنی تخت'; the footnote at the foot of the leaf glosses it as the band 'که بر (افسر) پادشاه ایران بست

data/verification/page-111.json BQT:917 supports BQT_v2_pages.txt leaf 377 (= printed p.917; the leaf/page offset is fixed by the 'بقیه در صفحهٔ ۹۰۸' catch-lines), footnote 1 to the headword دیو: 'پهلوی dēv … اوستا daēva (دیو). هندی باستان devá (خدا) «اشتقاق ۵۹۸». این کلمه در قدیم به گروهی از پروردگاران آریایی اطلاق می‌شده ولی پس از ظهور زرتشت و م

data/verification/page-111.json BQT:908 supports BQT_v2_pages.txt leaf 368 = printed p.908 (fixed by the catch-lines 'بقیه در صفحهٔ ۹۰۸' on leaf 367 and 'بقیه از صفحهٔ ۹۰۷' on leaf 368), footnote to دیبا: 'پهلوی dēpāk «تاوادیا ۹۱۰»، از هندی باستان dīp-, dīpayati (زبانه کشیدن، پرتو افکندن، درخشیدن) … «اشتقاق ۵۹۱» … اگرچه اشتقاق آن قطعی نیست' and, i

data/verification/page-111.json BQT:908 supports BQT_v2_pages.txt leaf 368 = printed p.908: headword 'دیبا * = بروزن زیبا، قماشی باشد از حریر الوان' with Mo'in's footnote 'پهلوی dēpāk … در فارسی = دیباه، دیبه؛ و دیباچه و دیوان نیز از همین ریشه است، معرب آن دیباج است' — the headword, the gloss 'a colorful cloth', and the extras دیبه/دیباج are all o

data/verification/page-112.json BQT:912 supports BQT_v2_pages.txt leaf 370 (printed ≈ p.912; running offset printed ≈ leaf + 543). The page carries both headwords: 'دیز … رنگ و لون را گویند عموماً چنانکه اسب سیاه خسرو پرویز را شبدیز گویند … و رنگ سیاه را نیز گویند' and 'دیس … همتا و مانند و شبیه و نظیر باشد'. Moʿin's footnote: 'آقای پورداود نوشته‌

data/verification/page-113.json BQT:827 supports Borhan-e Qate' vol. 2, BQT_v2_pages.txt leaf 287 (printed ≈830, i.e. within the ±3 uncertainty of the leaf→page mapping): headword 'دخش = بفتح اول بروزن رخش' with Mo'in's footnote 'پهلوی daxšak (شغل، تکلیف) قیاس: اوستا daxšta … «بارتولمه ۶۷۷» و ممکن است از اوستا daxša (نشان، علامت) «بارتولمه ۶۷۹» مش

data/verification/page-113.json BQT:866 supports Borhan-e Qate' vol. 2: the دشت / دشتان / دشن / دشوار block sits at BQT_v2_pages.txt leaves 325-327 (printed ≈868-870, i.e. Nourai's 866 within the ±3 leaf→page uncertainty). Borhan's دشن is quoted by Dehkhoda as 'دستلاف، که سودای اول اصناف باشد. (برهان)' — precisely Nourai's 'first (daily) sales'.

data/verification/page-114.json BQT:916 supports Borhān-e Qāṭeʿ vol. 2, the دینار leaf (BQT_v2_pages.txt leaf 376, printed ≈916–919), footnote 1: '۱ ـ پهلوی dēnār، تاوادیا ۹۱ ... از لاتینی dēnārius بتقدیر dēnārium بمعنی «نقدی برابر ده آسی» چه در اول وضع آن از نقره و مساوی ده آسِ as بود و آس از نقود مسین بود' — Moʿin asserts exactly Nourai's Latin 

data/verification/page-114.json BQT:916 supports Same leaf (BQT_v2_pages.txt leaf 376): headword 'دینار = بر وزن بیمار، زر سرخ را گویند ...' with the etymological footnote quoted at node 15, plus Moʿin's cross-reference 'برای ارزش دینار، رک: دائرة المعارف اسلام؛ و ارزش دینار و تومان در قرون مختلفه، مقالات کسروی ج۱ ص۱۰۹'.

data/verification/page-116.json BQT:829 partial In the scan (BQT_v2_pages.txt, leaf 289 ≈ printed p.831; the running head two leaves earlier reads ۲۲۴ = continuous 829) Mo'in's footnote 7 to دراز reads 'اوستا drājah- (طول). پهلوی drāj ... بلوچی drāj و drāz ... نیز در پهلوی drang «معین ۲:۱۷۲»'. It gives Avestan drājah- and Pahlavi (not Avestan) dr

data/verification/page-116.json BQT:829 supports Mo'in's footnote to دراز (BQT_v2_pages.txt leaf 289, printed ≈829-831): 'اوستا drājah- (طول). پهلوی drāj ... بلوچی drāj و drāz'.

data/verification/page-116.json BQT:841 supports Mo'in's footnote 1 to درنگ (BQT_v2_pages.txt leaf 301, printed ≈843): 'پهلوی drang (دراز، آهسته) «معین ۱۷۲:۲» ... اوستا darəγahe ... «بارتولمه ۱۹۱۶» ... zrvan-darəγō.xᵛaδāta- (زروان (زمان) پایدار). رك: Henning, Sogdian/Central Asian Words'.

data/verification/page-116.json BQT:894 partial the دودمان entry stands in the scan at BQT_v2_pages.txt leaf 354 ≈ printed p.896 (the cited 894 is within the ±2 drift of this scan). Mo'in's footnote 3 there analyses 'از: دود + مان' and glosses دوده as 'دودمان، دودخانه' with 'پهلوی dūtak' - it supports the compound but treats -mān as a suffix rath

data/verification/page-117.json BQT:817 partial BQT_v2_pages.txt leaf 277 (printed p.817 — the offset printed = leaf + 540 is confirmed by the دند entry on leaf 344 = Nourai's BQT:884). The headword is 'دام = بروزن رام، نقیض دد باشد که آن وحشی غیر درنده است عموماً' and footnote 1 runs '۱ - هندی باستان damá- ... یونانی δαμάλης (گاو نر)، لاتینی dom

data/verification/page-117.json BQT:817 supports BQT_v2_pages.txt leaf 277 (printed p.817): headword 'دام = بروزن رام، نقیض دد باشد که آن وحشی غیر درنده است عموماً و آهو و غزال و ... را گویند خصوصاً'; footnote 1 lists 'هندی باستان damá-, یونانی δαμάλης, لاتینی domāre, اُستی domun'. Borhān/Moʿin support both the sense and the Indo-European affiliat

data/verification/page-117.json BQT:159 supports BQT_v1_pages.txt leaf 377 (printed p.159): headword 'الماس؟ - بروزن کربای، گوهریست مشهور - و کنایه از تیغ و شمشیر و کارد و تیر - و آبگینه و مردم جلد و چابک باشد - و بمعنی قلم‌تراش هم هست - و دندان را نیز گویند'; Moʿin's footnote on the same leaf begins '۴ - از یونانی ...' ('from Greek ...'), the Lat

data/verification/page-117.json BQT:884 supports BQT_v2_pages.txt leaf 344 (printed p.884, the دند entry), footnote 5: 'در اوستا و پارسی باستان *dantan-، حالت مفرد فاعلی اوستا dantā، پارسی باستان *dantā، فارسی دند (دندان، دنده). حالت مفرد مفعولی dantānam ‹ فارسی دندان (سن). در اوستا حالت جمع فاعلی dantānō. «هوبشمان»'. Moʿin's page carries the Aves

data/verification/page-117.json BQT:884 supports BQT_v2_pages.txt leaf 344 (printed p.884; offset confirmed by the دام entry at leaf 277 = Nourai's BQT:817). Headword 'دند = بفتح اول بروزن چند، استخوان پهلو باشد'; footnote 5: 'در اوستا و پارسی باستان *dantan-، حالت مفرد فاعلی اوستا dantā، پارسی باستان *dantā، فارسی دند (دندان، دنده). حالت مفرد مفع

data/verification/page-118.json BQT:870 supports The NOTE's own citation. BQT_v2_pages.txt leaf 329 (printed 869), Moʿin's footnote 7: «دوب dub در زبان سومری بمعنی لوحه و خط است. از این زبان وارد اکدی شده ṭuppu … و از این زبانها وارد آرامی شده … نقل از «لغات بیگانهٔ اکدی» تألیف Zimmern»; the continuation on leaf 330 (printed 870) adds «برخی دیگر ه

data/verification/page-118.json BQT:869 supports Borhan-e Qateʿ ed. Moʿin, printed p. 869 = BQT_v2_pages.txt leaf 329 (the leaf carries the دفتر article and its footnotes; the estimated +543 offset in refs_online.json is ~3 leaves too high here — for this stretch printed ≈ leaf + 540). Moʿin's footnote there: «دفتر … را از یونانی diphthéra (پوست ح

data/verification/page-119.json BQT:848 supports BQT_v2_pages.txt leaf 308 = printed p.848 (offset +540, fixed by the 'بقیه از صفحهٔ ۸۳۸' note on leaf 299 = p.839). Mo'in's fn. 8: 'از: در (ه.م.) + یدن (پسوند مصدری) از ریشهٔ اوستایی dar- (شکافتن)، پهلوی darītan، هندی باستانی dar-, dr̥ṇāti ... در اوراق مانوی پهلوی dryd (دریدن). Henning, A list of Mi

data/verification/page-119.json BQT:845 supports BQT_v2_pages.txt leaf 305 = printed p.845 (offset +540). Headword 'دره = بفتح اول و تشدید ثانی ... گشادگی میان دو کوه را گویند'; Mo'in's fn. 9: 'اوستا daranū- (دره، گردنه) ... و رک: هوبشمان ایضاً ... در فارسی بمعنی وادی عربی آید. رک: دائرةالمعارف اسلام: دره؛ گیلکی darreh'.

data/verification/page-119.json BQT:838 supports BQT_v2_pages.txt leaf 298 = printed p.838 (offset +540, confirmed by the 'بقیه از صفحهٔ ۸۳۸' catch-line on leaf 299). Headword 'درفش' ('همان درفش کاویان است که علم فریدون ...'); Mo'in's fn. 4: 'رایت، بیرق، اوستا drafša- (بیرق)، پهلوی drafš ... ارمنی drawš ... و درفشی، ترکی: درفس'.

data/verification/page-120.json BQT:844 ? supports Borhan-e Qate', vol. 2, archive leaf 304 (printed page ~846/847 by the running-head offset, so Nourai's own '844 ?' is within the scan-offset uncertainty of two or three pages): headword 'درون = بفتح اول، بمعنی اندرون' and, in the same entry, '... و دعایی باشد که مغان در ستایش خدای تعالی و ذر آن خوا

data/verification/page-121.json BQT:809,843 supports BQT_v2_pages.txt leaf 269 (≈ printed 809, start of the دار entries): Mo'in's footnote 9 'پهلوی dār «تاوادیا ۹۱۲»، اوستا dāuru- (چوب)، قس: ارمنی ... هندی باستان dāru- (چوب)، کردی و بلوچی dār ... و رک: هوبشمان ۲۲۵'. Leaf 300 (≈ 843): 'درگر = باکاف فارسی بروزن دختر، درودگر را گویند' + footnote 'مخفف «د

data/verification/page-121.json BQT:869 partial BQT_v2_pages.txt leaf 329 (its foot carries 'بقیه در صفحهٔ ۸۷۰', so this is printed p.869) opens the بیان دهم 'در دال بی نقطه با فا' and has دف with 'دف زدن', 'دفتین'. The page does have the word Nourai wants, but its footnote derives Arabic دف from Hebrew/Sumerian, not from Persian داریه.

data/verification/page-121.json BQT:840,842,843 supports BQT_v2_pages.txt leaf 302 (≈ printed 842) 'درو ۳ = بروزن سرود، بمعنی صلوات است' with Mo'in's footnote 'پهلوی drūt (صحت، آرامش) ... drōd (آرزوی خیر و برکت) از ریشهٔ *drvatāt (ارمنی drut) و از اوستا drvatāt- «بارتولمه ۷۸۹»'; leaf 296 (≈ 836–840) carries درست with the Pahlavi/Old-Persian forms; leaf 30

data/verification/page-121.json BQT:854 partial the درونه entry with Mo'in's footnote 'drūna (کمان، قوس) بلوچی drīn' is at BQT_v2_pages.txt leaf 305, i.e. printed p.845±3 (its foot reads 'بقیه در صفحهٔ ۸۴۸'), not p.854; p.854 falls in the دژ section. The content Nourai wants is in Borhan, but the page number is off by about nine.

data/verification/page-123.json BQT:837 partial BQT_v2_pages.txt leaf 297 (printed 837), Mo'in's footnote to درشت: '... (جرأت، جسارت، کوشش) و اوستا darši ... و هوبشمان از ریشهٔ ایرانی *družt- می‌داند'; i.e. Mo'in cites Skt dhṛṣṇu- next to Hübschmann's competing *družta-, so the page supports Nourai's family but records the rival derivation as wel

data/verification/page-123.json BQT:822 partial BQT_v2_pages.txt leaf 282 (printed 822), Mo'in's footnote: 'دایه — ... اوستا daēnu (مادّه [از جانوران])، پهلوی dāyag (دایه)، هندی باستان ریشهٔ dhā- (شیر دادن)، ارمنی dayeak (دایه، مربّی)، کردی dāyik و dāyā (مادر) ... معرّب آن دایة (ماماه، قابله)'. Supports دایه fully; the page has no entry for دایی 

data/verification/page-123.json BQT:820 supports BQT_v2_pages.txt leaf 280 (printed 820), Mo'in's two footnotes: 'دانگ — ... پهلوی dāng، پارسی باستان (بنقل یونانی) δανάκη ... ارمنی dang، عربی معرّب دانق ... اصلاً همریشهٔ دانه (ه.م) است' and 'دانه — ... پهلوی dān(ag)، اوستا dānō-karša- (دانه‌کش)، هندی باستان dhānā- (دانهٔ گندم)، بلوچی dān(ag)، گیلک

data/verification/page-124.json BQT:169 supports Borhān-e Qāte‘ vol.1, leaf 387 of BQT_v1_pages.txt (running head '۱۶۹') carries the headword «اندام - بروزن انجام، معروف است که بدن و عضو آدمی باشد»; Mo'in's etymological footnote on that page is not legible in this OCR.

data/verification/page-124.json BQT:418 supports vol.1 leaf 644 = p.418, the «پنام» entry; Mo'in's long footnote there reads «در اوستا paiti-dāna ... در وندیداد بند ۹ پنام جزو اسلحه و لوازم یک مرد جنگی بشمار آمده ... دو قطعه پارچهٔ سفید که بروی دهان آویخته», and it prints the Avestan with -n-, contradicting Nourai's 'paiti-dâma'. Same page carries

data/verification/page-124.json BQT:818 supports Borhān vol.2, leaf 278 of BQT_v2_pages.txt = printed p.818 (running-head calibration leaf+540, checked against داد=807 and داور=821): headword «دان بر وزن نان، مطلق دانه را گویند ... و چون در آخر کلمه آید معنی ظرفیت بخشد، همچو قلمدان و کیفدان و قهوه‌دان», with footnote 7 'اوستا dāna-، هندی باستان dh

data/verification/page-124.json BQT:807 supports vol.2 leaf 267 = p.807 (running head داد): the داد entry 'وبمعنی راستی و عدل و عدالت', footnote 8 'پهلوی dāt (قانون) ... پارسی باستان dāta- ... قس: هندی باستان dhāta- ... بارتولمه', and the neighbouring headword 'داتوبر ... بمعنی داور و دادری' with the note 'پهلوی است، رک: داور'.

data/verification/page-124.json BQT:814 not_found vol.2 leaf 274 = p.814 by the same calibration is the داس‌/داستان page (داسار، داستاره، داستان، داسخاله); it contains nothing on داد or داور. Its Mo'in footnote (deriving داستان from Pahlavi dātastān 'حق، قانون') belongs to node #14, not here.

data/verification/page-124.json BQT:821 supports vol.2 leaf 281 = p.821 (running head داوردان): 'داور - بر وزن خاور، نام خدای عزوجل است - و پادشاه عادل ... و دراصل دادور بروزن دادگر بوده', with the Latin-script footnote giving Pahl. dātōbar/dātbar/dātwar, Av. dātō-bara, Arm. datavor.

data/verification/page-124.json BQT:862 supports vol.2 leaf 322 = printed p.862 by the leaf+540 calibration (verified against داد=807, دان=818, داور=821): the page carries the دست‌/دستوار block ('دستوار ... دستوانه') immediately preceding the دستور headword; دستان stands a few pages earlier in the same دست‐ run.

data/verification/page-126.json BQT:918 partial RE-CHECKED. BQT_v2_pages.txt leaf 378 = printed p. 918 (leaf 379 carries the header 'دیو دولت' and the page numeral ۹۱۹). The page has 'دیوار گر = دیوارساز و گلکار و بنّا را گویند' and 'دیوال، با لام، بر وزن و معنی دیوار است، چه در فارسی را و لام بهم تبدیل می‌یابند'; Mo'in's footnote reads '#دیوار ب

data/verification/page-126.json BQT:851 supports RE-CHECKED. BQT_v2_pages.txt leaf 311 = printed p. 851 (leaf 310 = p. 850 ends 'بقیه در صفحهٔ ۸۵۱'). The headword reads 'دژ = بکسر اول و سکون ثانی، قلعه و حصار باشد ۱، و بمعنی زشت و بدخوی و خشم ... نیز هست ۲', and Mo'in's footnote on the facing page (p. 850, s.v. دز) reads 'دز و دژ (ه.م.) ممکن است ش

data/verification/page-126.json BQT:359 partial RE-CHECKED. BQT_v1_pages.txt leaf 581 = printed p. 359 (the next leaf opens 'بقیه از صفحهٔ ۳۵۹'), s.v. پالیز: 'پالیز ۱ - بر وزن کاریز، بمعنی باغ و بوستان و کشتزار باشد عموماً و خربزه‌زار و خیارزار و هندوانه‌زار را گویند خصوصاً'; also 'پالیزبان - باغبان و بستان‌بان ... و نگاهدارندهٔ پالیز'. Nourai's 

data/verification/page-126.json BQT:912,914 supports RE-CHECKED. BQT_v2_pages.txt leaf 374 = printed p. 914 (leaf 372 = p. 912, the دیز/دیزه and دیگدان entries; leaf 378 = p. 918 fixes the offset). The headword on p. 914 reads 'دیگ، بکسر اول و سکون ثانی ... و کاف فارسی ... ظرفی که در آن چیزی پزند ۳', and Mo'in's footnote 3 reads 'به قول هوبشمان دیگ فا

data/verification/page-127.json BQT:876,877 supports BQT_v2_pages.txt leaf 336 = printed p.876 (offset printed = leaf+540, confirmed by the دماوند entry falling on leaf 338 = p.878, the page Nourai's own NOTE cites): headword «دم» with Moʿin's footnote 5 «هندی باستان dhamati (نفس کردن > دمیدن)؛ پهلوی dam نفس؛ اُستی dimin, dumun (دمیدن، وزیدن)؛ کردی de

data/verification/page-127.json BQT:888 supports BQT_v2_pages.txt leaf 348 = printed p.888 (printed = leaf + 540): «دنیدن ‑ بر وزن رسیدن. بمعنی دویدن بنشاط و بخوشحالی براه رفتن باشد …» with Moʿin's footnote ۴ «از: دن + یدن (پسوند مصدری). هندی باستان √dhan-, dadhanat (دویدن)». Exactly the derivation and the gloss of the chart.
```


## [2026-09-05T20:07:40.370Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==363' BQT_v2_pages.txt | head -60"
}
```


### [2026-09-05T20:07:42.115Z] TOOL RESULT

```
    ‫هت‬                                                                                             ‫دوبره‬
                                                                  ‫‪۷.‬‬   ‫بدان دوات مر کب را برهم زد‬

‫تحتانی مجهول ولام» بمعنی مکر وحیله باشد‪.‬‬           ‫دو بر‪ = ۵‬بروزن کبیره؛ دوالونسمه‌ای‬
‫و ابررشم گنده را نیزگوبند که از پیله‌ای (‪)۱‬‬                                   ‫باشد که مدان قماربازاد‪4 .‬‬
          ‫‪۰‬‬
    ‫آن باشد ‪.‬‬       ‫ورن‬
                      ‫ر د‬
                        ‫دکرم‬
                           ‫حاصل شودکه دو‬           ‫بضم اول وفتح ثالث وسکون‬                ‫يوك‬
                                                                                            ‫د‬
                                                                  ‫کاف » کنانه از دم آخرمردن باشد ‪۱‬‬




                                            ‫بیان بیستم‬
              ‫ددرال بی‌نقطه بهاای هوز مشتمل بر بنجاه لفت و کنات‬
‫وفر باد رایز گفته‌اند؛ ومعنی اول با زای نقطه‌دار‬     ‫علری‬   ‫‪.‬‬    ‫بقتح اول و سکون الى‬       ‫‌‬   ‫‪3‬‬


                         ‫است معین که ‪,‬عربی‌عشره گوبند ‪ -‬وامرمعروف | هم پنظرآمده است ‪. ۴‬‬
‫دهار ‪ -‬و وهاژ با زای هوز و زای‬                       ‫ونهی منکر را نیز گفته‌الد ‪ -‬ویکسراول معروف‬
‫است که درمقابل شهرباشد ‪ - ۴‬وامر بدادن هم | فارسی هر دو آمده است بر وزن نماز * بانگ‬
 ‫وفریاد ونعره راکوبند ‪ -‬وبک‌راول دره وشکاف‬                                             ‫رای بل ‪2‬‬
 ‫‪۵‬هار = بروزن بهار ‪,‬غار ودره وشکاف | کوه را ‪۵‬؛ وبمعنی اول بکسراول » وبمعنی‌ثالی‬


                                                   ‫(‪ )۱‬چك ‪ :‬پیله» خم ‪ :‬بكپیله ‪.‬‬
  ‫‪- ۱‬یپلوی(‪*121‬اونوالا ‪ ¥‬اوستا ‪, 2531‬هندی باستان ‪» 266‬ارمنی‪ .]52‬کردی وبلوچیع‬
  ‫‪ .021 8‬افتانی ‪ 92۱‬استی‪ . 581‬وخی‪ 821. 5201‬شربکلی ‪ .5601‬شغنی‪521 . 501‬‬
  ‫ختنی ‪« 2521‬بیلی‪ .‬روز کارنوج؛ شمارة‬          ‫نوم وسنگل جى ‪ " 5314‬منجیع ‪ « 021‬اسذق‪۷۸‬‬
  ‫‪ ۰‬بارسی باستان‬    ‫دبه ‪ .‬یپلوی ‪hêd‬‏ »‪ 2‬تاوادها ‪۶۴‬‬     ‫=‬    ‫‪۳‬‬             ‫‪.‬‬    ‫گیلکی ‪2‬‬     ‫‪* ۲6‬‬    ‫‪ ۳‬ص‬

   ‫‪.‬ردی ‪. 112‬اففانی ع تال‬‫‪1‬ا‪ . 73‬هندی‌باستان‪ 11158 -‬ک‬‫‪( 00‬سرزمین) » اوستا ق‬
      ‫بلوچی ع ‪ 01‬و تا « اسشق ‪۸‬ه» ورك ‪ :‬هوبشمان ابا ک›یلکی ‪ . 6‬رك‪ :‬ده‌بوید‪.‬‬
                               ‫‪« - ۴‬دهار ‪ ,‬غار وشکاف کوه بود » اسدی (طوسی) گوید ‪:‬‬

     ‫زبان چون درخت ودهان چون دهار»‪.‬‬                             ‫بکابك پراکنده بر دشت وغار‬
  ‫د لفت فری ‪. ۸۵۱‬‬
                                 ‫© _ مصحف « دهار > (هدم‪. ).‬‬               ‫رك ‪ :‬دهاز ‪.‬‬      ‫‪۴‬‬
  ‫هندی باستان‬      ‫)‪.‬‬   ‫ددن ( پسوند مصدری‬    ‫‪ -‬بفتح اول و چهارم » از ‪ :‬دو‬          ‫‪ #‬وولكان‬
   ‫»اری شدن ) › بهلوی ‪ . 8212۷24‬وخی ‪۷60۱۷ _ 002‬‬
                                              ‫( دوبدن ج‬                            ‫‪12۷40 ,‬‬           ‫‪۷‬‬
   ‫(دوبدن) » سریکلی ‪ ( 02۷21 - 0۳8‬چارنمل رفتن ) « اسشق ‪ » ۵۸۵‬نیز یهلوی ‪0251۷20‬‬
          ‫»یلکی ‪82/523۷0‬؛ شتابان رفتن » رفتن با ته‌جیل بسار » تاختن ‪.‬‬
                                                                    ‫که ‪ 4۵‬گ‬
                                                                          ‫ریب‬
                                                                            ‫«ن‬
‫‪ #‬دویت ‪ -‬بکر اول و دوم » ( لفة بضم اول وکر دوم) ‪ .‬اوستا ‪.6۷14 6125‬پاز ند‬
  ‫هذدی باهتان ‪ ( 6۷1 6126‬دوعد) « امشق ‪٩۸۵‬‏ » ؛ دو بارصد ‪ .‬چهار بار بنجاه ‪.‬‬                     ‫‪, ۱‬‬
‫( بهران قاطع ‪) ۸۱۱‬‬
```


## [2026-09-05T20:08:03.046Z] TOOL CALL #35: Bash

```json
{
 "command": "sed -n '1,40p' /home/sfmqrb/git/rishe/tools/fetch_source.py"
}
```


### [2026-09-05T20:08:03.087Z] TOOL RESULT

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


## [2026-09-05T20:08:07.099Z] TOOL CALL #36: Bash

```json
{
 "command": "for u in \"https://en.wiktionary.org/wiki/%D8%AF%D9%88%DB%8C%D8%AF%D9%86\" \"https://en.wiktionary.org/wiki/%CF%84%CF%81%CE%B1%CF%87%CF%8D%CF%82\" \"https://www.etymonline.com/word/trachoma\" \"https://www.etymonline.com/word/dark\" \"https://www.etymonline.com/word/dew\"; do echo \"### $u\"; python3 tools/fetch_source.py \"$u\" --note \"page 129: Dher2/Dheu1 verification\" 2>&1 | tail -2; done"
}
```


### [2026-09-05T20:08:11.818Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/%D8%AF%D9%88%DB%8C%D8%AF%D9%86
/home/sfmqrb/git/rishe/data/verification/sources/web/84cf5f14e4889280.txt
### https://en.wiktionary.org/wiki/%CF%84%CF%81%CE%B1%CF%87%CF%8D%CF%82
/home/sfmqrb/git/rishe/data/verification/sources/web/77f5b0244bda3c08.txt
### https://www.etymonline.com/word/trachoma
/home/sfmqrb/git/rishe/data/verification/sources/web/53119d0c045b0daa.txt
### https://www.etymonline.com/word/dark
/home/sfmqrb/git/rishe/data/verification/sources/web/cc339dcdd6f5273c.txt
### https://www.etymonline.com/word/dew
/home/sfmqrb/git/rishe/data/verification/sources/web/2b166f36b91cafa4.txt
```


## [2026-09-05T20:08:14.041Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 84cf5f14e4889280 77f5b0244bda3c08; do echo \"######## $f\"; grep -n -A20 -i \"etymology\" $f.txt | head -60; done"
}
```


### [2026-09-05T20:08:15.771Z] TOOL RESULT

```
######## 84cf5f14e4889280
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Verb 
69-
70- 1.3.1 
71- Conjugation 
72-
73- 1.3.2 
74- References 
75-
76- 1.3.3 
77- Further reading 
78-
79- Toggle the table of contents 
80-
81- دویدن 
82-
--
154: Etymology
155- [ edit ] 
156-
157- Inherited from Middle Persian [script needed] ( LHTWN-tn /⁠dawīdan⁠/ ) , [ 1 ] from Proto-Indo-European *dʰew- ( “ to run ” ) . 
158-
159- Pronunciation
160- [ edit ] 
161-
162- ( Classical Persian ) IPA ( key ) : /da.wiː.ˈdan/ 
163-
164- ( Dari, formal ) IPA ( key ) : [d̪ä.wiː.d̪án] 
165-
166- ( Dari, formal ) IPA ( key ) : [d̪ä.wiː.d̪án] 
167- ( Kabuli ) IPA ( key ) : [d̪ä.wiː.d̪án] 
168-
169- ( Hazaragi ) IPA ( key ) : [d̪ä.wi.d̪án] 
170-
171- ( Iran, formal ) IPA ( key ) : [d̪æ.viː.d̪ǽn] 
172-
173- ( Tajik, formal ) IPA ( key ) : [d̪ä.vi.d̪án] 
174-
######## 77f5b0244bda3c08
65: Etymology 
66-
67- 1.3 
68- Pronunciation 
69-
70- 1.4 
71- Adjective 
72-
73- 1.4.1 
74- Declension 
75-
76- 1.4.2 
77- Derived terms 
78-
79- 1.4.3 
80- Related terms 
81-
82- 1.4.4 
83- Descendants 
84-
85- 1.5 
--
97: Etymology 
98-
99- 2.2 
100- Pronunciation 
101-
102- 2.3 
103- Adjective 
104-
105- 2.3.1 
106- Declension 
107-
108- 2.3.2 
109- Derived terms 
110-
111- 2.4 
112- Further reading 
113-
114- Toggle the table of contents 
115-
116- τραχύς 
117-
--
188: Etymology
189- [ edit ] 
190-
191- From Proto-Hellenic *tʰrākʰús (whence Mycenaean Greek 𐀲𐀨𐀐𐀹(𐀊) ( ta-ra-ke-wi(ja) ) ), from Proto-Indo-European *dʰréh₂gʰ-us ~ *dʰr̥h₂gʰ-éws ( “ rough ” ) , from *dʰreh₂gʰ- ( “ to irritate ” ) . [ 1 ] Compare θρᾱ́σσω ( thrā́ssō ) . [ 2 ] 
192-
193- Pronunciation
194- [ edit ] 
195-
196- IPA ( key ) : /traː.kʰýs/ → /traˈçys/ → /traˈçis/ 
197-
198- ( 5 th BCE Attic ) IPA ( key ) : /traː.kʰýs/ 
199-
200- ( 1 st CE Egyptian ) IPA ( key ) : /traˈkʰys/ 
201-
202- ( 4 th CE Koine ) IPA ( key ) : /traˈçys/ 
203-
```


## [2026-09-05T20:08:22.871Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 53119d0c045b0daa cc339dcdd6f5273c 2b166f36b91cafa4; do echo \"######## $f\"; sed -n '1,120p' $f.txt | grep -v \"^\\s*$\" | sed -n '10,60p'; done"
}
```


### [2026-09-05T20:08:24.531Z] TOOL RESULT

```
######## 53119d0c045b0daa
 Apps 
 Premium 
 Log in 
 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
 Origin and history of trachoma 
 trachoma (n.) 
 disease of the eyes characterized by granulation on the eyelid, 1690s, from Modern Latin trachoma , from Greek trakhoma "roughness," from trakhys "rough" (see tracheo- + -oma ). Related: Trachomatous .
 also from 1690s 
 Entries linking to trachoma 
 -oma 
 word-forming element, from Greek -oma , with -o- , lengthened stem vowel + -ma , suffix forming neuter nouns and nouns that indicate result of verbal action (equivalent of Latin -men ); especially taken in medical use as "morbid growth, tumor," based on sarcoma , carcinoma .
 tracheo- 
 before vowels trach- , word-forming element used from early 19c. in anatomy, biology, etc., "of or pertaining to the trachea, having the form of a trachea, of the trachea and," from Latinized form of Greek trakheia , as used in anatomy in reference to the windpipe (see trachea ). Greek trakheia is from trakhys "rough, uneven, stony," figuratively "severe, harsh," also used of rough voices, anger, etc., which according to Watkins is connected to the root of dark and dreg , but Beekes discounts this and says it is related to thrassein "to trouble, disturb."
 English also uses trachy- in a few words to indicate "rough."
 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
 More to explore
 hoedown 
 "noisy dance," 1841, Southern U.S., apparently originally the name of a specific dance, perhaps from perceived similarity of dance motions to those of farm chores, hence from hoe (n.). The step of every negro dance that was ever known, was called into requisition and admirably e
 speed 
 Middle English spede, from Old English sped "success, a successful course; prosperity, riches, wealth; luck, good fortune; opportunity, advancement," from Proto-Germanic *spodiz (source also of Old Saxon spod "success," Dutch spoed "haste, speed," Old High German spuot "success,"
 ambition 
 mid-14c., ambicioun, "eager or inordinate desire for honor or preferment," from Old French ambicion (13c.), or directly from Latin ambitionem (nominative ambitio) "a going around," especially to solicit votes, hence "a striving for favor, courting, flattery; a desire for honor, t
 sanction 
 1560s, "a law or decree," from Latin sanctionem (nominative sanctio) "act of decreeing or ordaining," also "a decree, an ordinance, a law," noun of action from past-participle stem of sancire "to decree, confirm, ratify, make sacred" (see saint (n.)). Originally especially of ecc
 algebra 
 "formal mathematics; the analysis of equations; the art of reasoning about quantitative relations by the aid of a compact and highly systematized notation," 1550s, from Medieval Latin algebra, from Arabic "al-mukhtasar fi hisab al-jabr wa al-muqabala" ("the compendium on calculat
 romanticism 
 1803, "a romantic idea," from romantic + -ism. In literature, 1823, in a French context, in reference to a movement toward medieval forms (especially in reaction to classical ones), an association now more often confined to Romanesque. The movement began in German and spread to E
 poignant 
 late 14c., poinaunt, "painful to physical or mental feeling" (of sauce, spice, wine as well as things that affect the feelings), from Old French poignant "sharp, pointed" (13c.), present participle of poindre "to prick, sting," from Latin pungere "to prick, pierce, sting," figura
 patriotism 
 "love of one's country; the passion which moves a person to serve his country, either in defending it or in protecting its rights and maintaining its laws and institutions," 1726, from patriot + -ism. The patriotic quip My country, right or wrong traces to a toast given by U.S. W
 groom 
 c. 1200 (late 12c. in surnames), grome "male child, boy;" c. 1300, "a youth, young man," also "male servant, attendant, minor officer in a royal or noble household ranking higher than a page; a knight's squire." A word of unknown origin with no certain cognates in other Germanic 
 Semite 
 1847, "a Jew, Arab, Assyrian, or Aramaean" (an apparently isolated use from 1797 refers to the Semitic language group), back-formation from Semitic or else from French Sémite (1845), from Modern Latin Semita, from Late Latin Sem, Greek Sēm "Shem," one of the three sons of Noah (G
 Share trachoma 
 ‘ cite ’ 
 Page URL :
 https://www.etymonline.com/word/trachoma Copy 
 HTML Link :
 <a href="https://www.etymonline.com/word/trachoma">Etymology of trachoma by etymonline</a> Copy 
 APA Style :
 Harper, D. (n.d.). Etymology of trachoma. Online Etymology Dictionary. Retrieved September 5, 2026, from https://www.etymonline.com/word/trachoma Copy 
 Chicago Style :
 Harper Douglas, "Etymology of trachoma," Online Etymology Dictionary, accessed September 5, 2026, https://www.etymonline.com/word/trachoma. Copy 
 MLA Style :
 Harper, Douglas. "Etymology of trachoma." Online Etymology Dictionary, https://www.etymonline.com/word/trachoma. Accessed 5 September, 2026. Copy 
 IEEE Style :
 D. Harper. "Etymology of trachoma." Online Etymology Dictionary. https://www.etymonline.com/word/trachoma (accessed September 5, 2026). Copy 
######## cc339dcdd6f5273c
 Apps 
 Premium 
 Log in 
 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
 Origin and history of dark 
 dark (adj.) 
 Middle English derk , later dark , from Old English deorc "without light, lacking light or brightness (especially at night), obscure, gloomy;" figuratively "sad, cheerless; sinister, wicked," from Proto-Germanic *derkaz (source also of Old High German tarchanjan "to hide, conceal"), which is of uncertain etymology. For vowel change, see marsh .
 Application to colors, "not radiating or reflecting much light," is from late 14c. Of complexion, "not fair," from early 14c. Figurative sense of "obscure, not easily understood" is from early 13c.; that of "sullen, sad" is from 1590s. Meaning "concealed, secret" is from late 14c. Dark Continent "Africa" (1828) combines several figurative senses (earliest references are in missionary publications). Theater slang for "closed" is from 1916.
 Dark Ages "benighted time in history, period of ignorance" is attested by 1739; the specific focus on the centuries of the early Middle Ages in Europe, from the fall of Rome to the revival of secular literature, is from 1830s, from dark in a sense of "characterized by ignorance, backward in learning, void of intellectual light" (late 14c.). 
 Dark horse "competitor for honors or office about whom nothing certain is known, or whose identity is at first concealed," especially, in U.S., politics, "one who is unexpectedly brought forward as a candidate in a convention," 1842, is an image from horse racing, of horses whose performances or capabilities are not generally known, in which dark is used in its figurative sense of "unknown."
 Moonraker is called a "dark horse"; that is neither his sire nor dam is known. ["Pierce Egan's Book of Sports," London, 1832] 
 dark (n.) 
 early 13c., derk , "absence of light, night-time," from dark (adj.). Figurative in the dark "in a state of ignorance" is from 1670s; earlier it meant "in secrecy, in concealment" (late 14c.).
 also from early 13c. 
 Entries linking to dark 
 marsh (n.) 
 "tract of water-soaked or partially flooded land; wet, swampy ground; piece of low ground, usually more or less wet but often nearly dry at certain seasons," Middle English mersh , from Old English mersc , merisc "marsh, swamp," from Proto-Germanic *marisko (source also of Old Frisian and Old Saxon marsk "marsh," Middle Dutch mersch , Dutch mars , German Marsch , Danish marsk ), probably from Proto-Germanic *mari- "sea" (from PIE root *mori- "body of water").
 The vowel shift from -e- to -a- began in 15c. and is usual for -er- followed by a consonant: Compare darling (Middle English dereling , Old English deorling ), far (Middle English fer , Old English feorr ), mar (Middle English merren ), hart (Middle English hert , Old English heorot ). Marsh gas "methane generated by decaying matter in marshes" is attested by 1819.
 darken (v.) 
 c. 1300, derken , "to make dark or darker, deprive of light;" early 14c. (intransitive), "to grow or become dark," from dark (adj.) + -en (1). The more usual verb in Middle English in both senses was simply dark , as it is in Chaucer and Shakespeare, and darken did not predominate until 17c. The Anglo-Saxons also had a verb sweorcan meaning "to grow dark."
 Meanings "grow less white or clear, turn a darker color" and "render less white or clear" are from late 14c. Figurative sense of "render gloomy, sadden" is from 1742. To darken (one's) door (usually with a negative) "enter one's house as a visitor," usually with an implication of unwelcomeness, is attested from 1729.
 darkling 
 darkly 
 darkness 
 dark-room 
 darksome 
 darky 
 dern 
 far 
 See All Related Words (10) 
 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
 More to explore
 darkling 
 "in the dark," mid-15c., from dark (n.) + now-obsolete adverbial ending -ling (compare headlong). The verb darkle is a back-formation from 1810 (Moore, who rhymed it with sparkle), assuming the -ing as a present-participle adjective ending. But having nothing to do with the part
 darky 
 also darkey, darkie, colloquial for "a black person, a Negro" (now offensive), 1775, from dark (adj.) + -y (3). Related: Darkies. Jake thought how strange it was to hear the Englishman say “darky” without being offended. Back home he would have been spoiling for a fight. There h
 dern 
 "secret, hidden," from Old English derne (West Saxon dierne) "concealed, secret, dark," from West Germanic *darnjaz (source also of Old Saxon derni, Old Frisian dern "concealed, dark," Old High German tarni "secret, concealed, veiled"), related to dark (adj.). Archaic or poetic o
 temerity 
 "by chance, at random; indiscreetly, rashly, recklessly;" probably, etymologically, "blindly," from PIE root *temsro- "dark..." (adj.), source also of Sanskrit tamisra- "dark night," tamsrah "dark;" Avestan temah "darkness;" Middle Persian tar "darkness...," tarig "dark;" Lithuanian tamsa "darkness," tamsus "dark;" Old Church Slavonic tima "darkness;" Old High German dinstar..."dark," demar "twilight;" Old Irish temel "darkness."...
 dun 
 Old English dunn "dingy brown; dark-colored," perhaps from Celtic (compare Old Irish donn "dark;" Gaelic donn "dull; dark...brown; dark;" Welsh dwnn "brownish"), from PIE *donnos, *dusnos "dark."...
 brunette 
 of a woman, "dark in complexion, having a brownish tone to the skin and hair," 1660s, from French brunette, fem. of brunet..., from Old French brunet "brownish, brown-haired, dark-complexioned," fem. diminutive of brun "brown" (12c.), of West Germanic...As a noun, "woman with dark hair and eyes and of a dark complexion," from 1710....Burnete also was used of a wool-dyed cloth of superior quality, originally dark brown....
 dusk 
 Middle English also had it as a verb, dusken "to become dark."...Perhaps it is from a Northumbrian variant of Old English dox "dark-haired, dark from the absence of light," with transposition...Old English dox is from PIE *dus-ko- "dark-colored" (source also of Swedish duska "be misty," Latin fuscus "dark," Sanskrit...
 obscure 
 c. 1400, "dark," figuratively "morally unenlightened; gloomy," from Old French obscur, oscur "dark, clouded, gloomy; dim, not clear" (12c.) and directly from Latin obscurus "dark, dusky, shady," figuratively "unknown; unintelligible; hard to discern; from insignificant ancestors,
 evening 
 from Old English æfnung "the coming of evening, sunset, time around sunset," verbal noun from æfnian "become evening, grow toward evening," from æfen "evening" (see eve). As a synonym of even (n.) in the sense "time from sunset to bedtime," it dates from mid-15c. and now entirely
######## 2b166f36b91cafa4
 Apps 
 Premium 
 Log in 
 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
 Origin and history of dew 
 dew (n.) 
 "water vapor deposited from the atmosphere by condensation, especially during the night," Middle English deaw, deu , from Old English deaw , from Proto-Germanic *dawwaz (source also of Old Saxon dau , Old Frisian daw , Middle Dutch dau , Old High German tau , German Tau , Old Norse dögg "dew"), perhaps from PIE root *dheu- "to flow" (source also of Sanskrit dhavate "flows, runs").
 Used figuratively of something refreshing (late Old English), or suggestive of morning and youthful freshness (1530s). As a verb, "to wet with or as with dew," Old English deawian .
 The formation of dew is explained by the loss of heat by bodies on the earth's surface through radiation at night, by which means they and the air immediately about them are cooled below the dew-point ....Dew is thus deposited chiefly on bodies which are good radiators and poor conductors of heat, like grass; hence also it appears chiefly on calm and clear nights--that is, when the conditions are most favorable for radiation. It never appears on nights both cloudy and windy. In winter dew becomes hoar frost. [Century Dictionary]
 Entries linking to dew 
 dag (n.) 
 several words, probably unrelated, including: 1. "pendant point of cloth on a garment," late 14c., of uncertain origin; 2. "thin rain, drizzle, wet fog," Scottish, late 17c., from a Scandinavian source such as Old Norse dögg , plural daggir "dew," from Proto-Germanic *daowo- (source of Old English deaw ; see dew ); 3. "kind of heavy pistol," 1560s, of uncertain origin; 4. "clot of dirty wool about the rear end of a sheep," 1731; 5. "tough but amusing person," Australian and New Zealand slang, 1916.
 dewberry (n.) 
 popular name of a woodland bramble or its fruit, which is black with a bluish dewy bloom, 1570s, from dew + berry . a name variously applied in England and North America.
 dewdrop 
 dewfall 
 dewpoint 
 dewy 
 honeydew 
 mildew 
 See All Related Words (8) 
 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
 More to explore
 mildew 
 "minute parasitic fungus that appears on plants or decaying organic matter," mid-14c., a transferred sense of a word that meant originally "nectar, honeydew" (the sugar-rich sticky stuff secreted by aphids feeding on plant sap); this is from mid-13c. as mildeu, from Old English m
 rosemary 
 widely cultivated for its fragrance, late 14c., rose-marie, earlier rosmarine (c. 1300), from Latin rosmarinus, literally "dew...of the sea" (compare French romarin), from ros "dew" + marinus "of the sea, maritime," from mare "sea, the sea, seawater...Latin ros is from a PIE noun probably from *ers- "to be wet" (source also of Lithuanian rasa, Old Church Slavonic rosa "dew...
 drizzle 
 Perhaps it is an alteration of drysning "a falling of dew" (c. 1400), from Old English -drysnian, which is related to dreosan...
 micturition 
 As during the final 20 minutes of a 4-hour film after drinking a 32-ounce Mountain Dew from the snack bar and the movie ends...
 frost 
 A black frost (late 14c.) is one which kills plants (turns them black) but is not accompanied by visible frozen dew....
 dreary 
 blood-stained," from dreor "gore, blood," from (ge)dreosan (past participle droren) "fall, decline, fail," used of rain, snow, dew...
 precipitation 
 The meteorological sense of "rain, snow, dew, frost, hail, etc.; moisture from the atmosphere deposited on the earth's surface...
 mess 
 c. 1300, "a supply or provision of food for one meal," from Old French mes "portion of food, course at dinner," from Late Latin missus "course at dinner," literally "a placing, a putting (on a table, etc.)," from past participle of mittere "to put, place," in classical Latin "to 
 calendar 
 c. 1200, calender, "the year as divided systematically into days and months;" mid-14c. as "table showing divisions of the year;" from Old French calendier "list, register," from Latin calendarium "account book," from calendae/kalendae "the calends" the first day of the Roman mont
 empathy 
 1908, modeled on German Einfühlung (from ein "in" + Fühlung "feeling"), which was coined 1858 by German philosopher Rudolf Lotze (1817-1881) as a translation of Greek empatheia "passion, state of emotion," from assimilated form of en "in" (see en- (2)) + pathos "feeling" (from PI
 Share dew 
 ‘ cite ’ 
 Page URL :
 https://www.etymonline.com/word/dew Copy 
 HTML Link :
 <a href="https://www.etymonline.com/word/dew">Etymology of dew by etymonline</a> Copy 
 APA Style :
```


## [2026-09-05T20:08:38.480Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('AHD_watkins1985.txt',errors='ignore').read()\ni=t.find('dher-2, To hold firmly')\nprint(t[i-1600:i+60].replace('\\n',' '))\nprint('\\n=========DEW=========')\nfor m in re.finditer(r'DEW', t):\n    print(t[max(0,m.start()-800):m.start()+120].replace('\\n',' ')); print('---')\nEOF"
}
```


### [2026-09-05T20:08:40.610Z] TOOL RESULT

```
ginally made of clay or mud bricks): PARADISE. [Pok. dheigh- 244.] dhel-. A hollow. 1. Germanic *daljé in Old English dell, valley: DELL. 2. Germanic *dalam in Old English del, valley: DALE. 3. Germanic *del- in Old Norse dzla, wooden gutter on a ship: DALLES. [Pok. 1. dhel- 245.] dhelbh-. To dig, excavate. Germanic *de/ban in Old English de/fan, to dig: DELVE. [Pok. dhelbh- 246.] dhembh-. To bury. Suffixed zero-grade form *dhmbh-o- in Greek taphos (< *thaphos), tomb: CENOTAPH, EPI- TAPH. [Pok. (dhembh-), dhmbh- 248.] dhen-'. To run, flow. Suffixed o-grade form *dhon-ti- in Latin fons (stem font-), spring, fountain: FONT!, FOUN- TaIN. [Pok. 1. dhen- 249.] dhen-2. Palm of the hand. Suffixed form *dhen-r in Greek thenar, palm of the hand: THENAR. [Pok. 2. dhen- 249.] dher-1. To make muddy; darkness. 1. Suffixed form *dher-g- in Germanic *derk- in Old English deorc, dark: DARK. 2. Suffixed zero-grade form *dhr-egh- in: a. Ger- manic ‘suffixed form *drah-sta- in Old English drés, dregs: pross; b. Germanic *dragj6 in Old Norse dregg, dregs: DREGS. 3. Suffixed extended zero-grade form *dhro-bh- in Germanic *drab- in: a. Old English dreflian, to drivel: DRIVEL; b. probably Low German drabbelen, to paddle in water or mire, draggle, akin to the Low German source of Middle English drabelen, to draggle: DRABBLE; C. Middle Irish drab, dregs, probably akin to the Celtic source of DRAB2. 4. Suffixed extended dher-2 zero-grade form *dhra-gh- in: a. Greek tarassein (Attic tarattein), to confuse, disturb: ATARACTIC; b. Greek trakhus, rough: TRACHEA, TRACHOMA, TRACHYTE. [Pok. 1. dher- 251.] dher-2, To hold firmly, support. 1. Suffixed form *dher-mo- 

=========DEW=========
-m-bho- in Germanic *dumbaz in Old English dumb, dumb: pumps; c. Germanic *diibén- in Old English *dife, dove (< “dark-colored bird”): DOVE!. 12. Extended zero-grade form *dhwel- in: a. Germanic *dwelan, to go or lead astray, in Old English dwellan, to deceive (but influenced in sense by cognate Old Norse dvelja, to tarry): DWELL; b. Germanic *dulaz in (i) Old English dol, dull: DoL- DRUMS (ii) Middle Low German dul, dull: (DOLT), DULL. 13. Extended zero-grade form *dhwes- in Greek suffixed form *th(wjes-es-, smoke, whence Greek *th(w)es-es-yon, becoming theion, brimstone, sulfur: THIO-, THION-. 14. Perhaps Old English docce, dock (< “dark-colored plant”): Dock‘. 15. Perhaps Irish did, pipe: DUDEEN. [Pok. 4. dheu- 261.] dheu-2. To flow. Germanic *dauwaz, dew, in: a. Old English déaw, dew: DEW; b. compound *melith-dauwaz, “honeydew” (see melit-). [Pok. 1. dheu- 259.] dheu-’. To become exhausted, die. 1. Suff
---
nexplained fact that no common Indo-European noun for milk can be reconstructed is another root *g(ajlag-, *g(a)lakt-, milk, found only in: a. Greek gala (stem galakt-), milk: (GA- LACTIC), GALACTO-, GALAXY; AGALACTIA, POLYGALA; b. Latin lac (stem lact-), milk: (LACTATE), LACTEAL, LACTESCENT, LACTO-, LETTUCE; C. the blended Germanic form cited in I. 2. above. [Pok. melg- 722, glag- 400.] melit-. Honey. 1. Greek meli, honey: HYDROMEL, MARMA- LADE, MELILOT, OENOMEL. 2. Latin mel (stem meil-), honey: MELLIFEROUS, MELLIFLUOUS, MOLASSES. 3. Ger- manic *melith- in compound *melith-dauwaz (*dauwaz, dew; see dheu-?), honeydew (a substance secreted by aphids on leaves; it was formerly imagined to be distilled from the air like dew), in Old English mildéaw, honey- dew, nectar, later also mildew: MILDEW. [Pok. melit- 723.] mélo-. Also smé@lo-. Small animal. Zero-grade form *smalo- in Germanic *smal-, small animal, hen
---
kan- DESCEND skand- DESCRIBE skribh- DESERTS = ser-3 DESERVE servus DESICCATE selkw- DESIGNATE sekw-1 DESIRE sweid-1 DESIST sta- DESMID dé- DESOLATE s(w)e- DESPAIR spé-1 DESPICABLE spek- DESPISE spek- DESPOIL spel-! DESPOND spend- DESPOT deme-! DESTINE sta- DESTITUTE sta- DESTRIER deks- DESTROY ster-2 DESUETUDE s(w)e- DESULTORY sel-4 DETAIN  ten- DETECT (s)teg- DETENT ten- DETER tres- DETERIORATE de- DETERMINE ter- DETEST trei- DETONATE (s)tene- DETOUR tera-1 DETRACT tragh- DETRIMENT tera-1 DETUMESCENCE teue- DEUCE! dwo- DEUTERAGONIST deu-? DEUTERIUM deu-! 88 DEUTERO- deu-! DEUTERONOMY deu-!, nem- DEVANAGARI deiw- DEVASTATE eu-2 DEVEST wes-4 DEvi deiw- DEVIATE wegh- DEVIL gWele-! DEVIOUS wegh- DEVISE weidh- DEVOID eu-2 DEVOIR ghabh- DEVOLVE wel-3 DEVOTE weg¥h- DEVOUR gWera-4 DEVOUT weg*h- DEW dheu-2 DEXTER deks- DEXTERITY deks- DEXTRO- deks- DEXTRORSE_ wer-3 DHARMA dher-2 DI-!_ dwo- DIABASE gWa- DIABETES gW
---
PHROS negWh-ro- METAPHOR bher-1 METAPHRASE gWhren- METAPLASM pele-2 METASTASIS sta- METATHESIS dhé-1 METE! med- METE2 mei-3 METEMPSYCHOSIS bhes-? METER! mé-2 METER? mé-2 METER? mé-2 -METER mé-2 METHEGLIN med- METHINKS tong- METHOD sed-2 METHYLENE hule, medhu- METONYMY no-men- METOPE okw- METOPIC okw- METRICAL mé-2 METRO- miater- METROLOGY mé-2 METRONOME mé-2, nem- METRONYMIC n0-men- METROPOLIS miéater-, pele-3 -METRY mé-2 MEW! mei-1 MEZZO-RELIEVO legh- MI smei- MIASMA mai-2 MICA smé- MICKLE meg- MICRO- smé- MICROBE gWei- MICROCOSM kes-3 MICROFICHE dhig®- MICRON smé- 97 MICROPYLE pulé MICTURATE meigh- MID! medhyo- MIDDLE medhyo- MipcaRD medhyo- MIDGE mu-2 MIDRIFF krep- MIDWIFE me-2 MIGHT! magh-! MIGRAINE ker-1 MIGRATE mei-1 MIL! gheslo- MIL? gheslo- MILCH melg- MILCHIG melg- MILD mel-? MILDEW melit- MILE gheslo- MILFOIL bhel-3, gheslo- MILIEU medhyo- MILIUM mele- MILK melg- MILL! mele- MILLENARY gheslo- MIL
---
```


## [2026-09-05T20:10:16.581Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD Bd1 dher trüb ===\"; grep -n \"trüber  Bodensatz\\|trüber Bodensatz\\|dherag\\|dherəgh\\|dhera-gh\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -10; echo \"=== WLD Bd1 dheu laufen ===\"; grep -n \"laufen, rinnen\\|laufen,  rinnen\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -10"
}
```


### [2026-09-05T20:10:16.646Z] TOOL RESULT

```
=== WLD Bd1 dher trüb ===
47505:dheragh -, ilhrty- (vgl. auch Anklange unter tier- „schinden“, Wzf. deryh-, 
50504:„Krampf" (eher zu anord. druga „ziehen", idg. dherag- gehort dagegen 
50956:*dheragh- „ziehen u gestellt werden. 
51839:Oder als „hinziehen“ zu idg. dheragh-1). 
54120:Wz. dheragh- „ziehen"? s. Berneker 226; fur ersteres spricht einigermaBen 
54157:Sippe bekommen zu haben, sondern ist von *dheragJi- „ziehen“ aus ver* 
54219:*dheragh- „ziehen, schleifen"; wenigstens ist dafiir eine Urbed. „festhaltend 
54320:dheragh dheregh- 
55158:mindestens ebensogut als eine Yariante auf Palatal neben dheragh- „ziehen“ 
55180:trigo „Trauer“ (s. *drrgh -), lat. t radio (doch s. u. *dheragli-), mndl. trecken 
=== WLD Bd1 dheu laufen ===
52566:1. dheu- „laufen, rinnen“. 
52821:„laufen, rinnen“.
```


## [2026-09-05T20:10:19.171Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SKT dark/dew ===\"; grep -n \"^Dark\\|^Dew\\|Dark, obscure\\|Dew, moisture\" SKT.txt | head -10; echo \"=== IEC dhraghus ===\"; grep -n \"dhraghu\\|dhrāghu\\|dhauo\\|dhawo\" IEC.txt | head -10; echo \"=== NYB dawistan ===\"; grep -n \"dawistan\\|dawītan\\|davītan\\|LHTWN\" NYB_vol2_glossary.txt | head -10"
}
```


### [2026-09-05T20:10:19.251Z] TOOL RESULT

```
=== SKT dark/dew ===
4987:Dew  (E.^  U.E.deu.Jew.  KS^dedw, dcw.  +  Du.  danxif,  Iccl  »/oi;y  {Rcn.  dffggvar), I*)aii.  (/«^,  Swcd.  i/Jiy,  G.  t/iait.  Perhaps allied  to  Ski.  J/tdv,  to  run,  or  dAtSv,  to  wa&n. bedew,  to  cover  with  dew.  (E.)  From dejv,  with  prefix  dc-.
=== IEC dhraghus ===
=== NYB dawistan ===
145:LHTWN-: RAT to run
1243:davistan [LHTWN-stn'], davitan [dwytn', LHTWN-tn'] to run, pt. = pret. 3d p. sg. davist [LHTWN-st'] 71%; pass. constr.: devän hanjaman davit [dwyt'] (by the devs an assembly was run at =) the devs hurriedly arranged an assembly 424, .. MPrs dw-, Verbum 173; NP davidan.
```


## [2026-09-05T20:10:27.475Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '52566,52590p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt"
}
```


### [2026-09-05T20:10:27.521Z] TOOL RESULT

```
1. dheu- „laufen, rinnen“. 

Ai. dhavate „rennt, rinnt u , dehnstufig dhavati ds., dhauti - „Quelle, Bach“, 
ilhdra „Strom, GuBstrahl“ (wenn aus *dho[u]ra; von Fick I 3 115, Schulze 
KZ. 29 261, Bugge BB. 14,78 zu gr . dogog, ■frogw/uai, 'dgmaxco gestellt, 
was Uhlenbeck Ai. Wb. 136 zu bestimmt ablehnt; mit dhara will Jokl 
SBAkWien 168, I 1 3 f., alb. der& „gieBe aus“ verbinden, mit praesens- 
bildendem d oder dh, was aber nur unter einer Wz. dher- erwagenswert 
ist, da ein o-stufiges und dazu denominatives d(A)-Praesens *dho-r-d(h)d 
unglaublich ware); mp. davidan „laufen, eilen u , pam. dav- „laufen, rennen“. 
Gr. deco (= ai. dhdvati) und dgco (= ai. dhavati-. in del?] Z 507, Schulze 
Qu. ep. 278), Fut. devaojuai ,.laufen“, do<k „schnell“, flog-doog „auf einen 
Zuruf hin schnell zur Hand, zu Hilfe eilend ‘, doatco „versetze in schnelle 
heftige Bewegung; bewege mich schnell, tummle mich ‘: anord. dqgg, gen. 
dqgguar ( *dawu o ), ags. deem, as. dau, ahd. tou, nhd. Tau ( *damva- ). Unsicher 
mir. doe „Meer“ ( *dheuia , dhmiia „das rinnende oderheftig bewegte“? Stokes 
BB. 21, 127) Fick I 4 75, 244f., Persson Beitr. 677. — Fern bleiben gr. 
drjg, d?jTog ,.Lohnarbeiter, Knecht“ (von Brugmann IF. 19, 388 als *§fa- x- 
angereiht; abgelehnt von Frankel Nom. agentis I 87 Anm. 2) und ayadog 
,.gut“ (sei *dya-i)y-6g „*sehr schnell" nach dems.). — Uber lat. favonms 
(angeblich „Tau-, Regenwind"; Froehde BB. 17, 311) s. Vf. LEWb. 2 s. v. 

Urspriingliche Gleichheit mit dheu- „stieben, heftige Bewegung" (z. B. 
Fick, Brugmann, Persson aaO.) ist moglich. — Yerschieden ist ai. dhd- 
vati „reinigt, macht blank" usw. (gegen Fick I 4 244 f. Uhlenbeck AiWb.
```


## [2026-09-05T20:10:27.937Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Bodensatz einer Fl\\|Widerlichkeit\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -5"
}
```


### [2026-09-05T20:10:27.983Z] TOOL RESULT

```
53858:der Bodensatz einer Flussigkeit, auch allgemeiner von Schmutz, Wider-
```


## [2026-09-05T20:10:38.976Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '53853,53875p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt; echo \"=== driwi in WLD ===\"; grep -n \"driwi\\|drdbhi\\|dhrabhi\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head"
}
```


### [2026-09-05T20:10:39.036Z] TOOL RESULT

```
die teilweise Gleichheit der hier begegnenden Bedeutungen nicht aus ursprgl. 
gleichen Grundbedeutungen der versch. Wurzeln erklart zu werden. 

1. dher-, dhera- in kons. Erweiterungen (zusammengefaBt bei Hirt Abl. 82 
und bes. Reichelt KZ. 46, 321 f.) „truber, schmieriger, ranziger, stinken- 
der Bodensatz einer Flussigkeit, auch allgemeiner von Schmutz, Wider- 
lichkeit (Abneigung gegen Stinkendes) von quatschigem Wetter, von 
triiben, schmutzigen Farbentonen usw.; verbal: Bodensatz und Schlamm 
aufriihren. triiben". Ob ursprgl. eins mit dher- „Unrat, cacare“? 

1. dhereyh- (vgl. bes. Bezz. BB. 4,320f.): 

Gr. dgdoaai. att. flodrrco (Pf. hom. xhgyya intr.) ,.verwirren, beunruhigen" 
(ursprgl. wohl vom Aufriihren des Schlammbodens in einem Gewasser) ; 
raoayy „Yerwirrung", ragdoaco, att. -ttcd „verwirre“; rgayvg, jon. rgy/og 
,.rauh, uneben" (wohl ursprgl. von Schmutzkrusten; nicht nach Pedersen 
IvZ. 39, 344 zu arm. erag ..schnell". -ga- hier aus sog. f, d. i. *dh e rdghu-s); 
rdo'/Jj ' raon^ic und draoyov' ayeiuaoTOv Hes. (\ okalstufe wie onaoyr} : lit. 



dher-, dhera- 

=== driwi in WLD ===
53986:rinnen bringen“ beruhen. — Ob zu dt. triibe auch av. driwi- „Flecken, 
55188:Muttermal“ aus *dhrabhi- stellt sich in Ablaut und Bed. besser zu *dherabh- 
55305:und driwi- f. „Flecken, Mal“ nach Sch. „Pockennarben“) idg. dhl- voraus,
```


## [2026-09-05T20:10:43.917Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '53980,53995p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt; echo \"=== 55300 ===\"; sed -n '55298,55312p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt"
}
```


### [2026-09-05T20:10:43.978Z] TOOL RESULT

```
Thumb KZ. 36, 1 8 2 f . , Falk-Torp u. drav (Lit.), Hirt Abl. 82, Reichelt 
KZ. 46, 321 f. Fiir anord. drafli ist wegen des gibed, gr. roorpaUg ,,ge- 
ronnene Milch, frischer Kase“ Zugehorigkeit zu letzterer Sippe zwar ver- 
fiihrerisch, doch ware drafli der einzige germ. Reflex dieser andern Wz. 
und ist die formale Ahnlichkeit (urn. *drafelan-') doch nur sehr vage; es 
kann auf einem Verbum *drabaldn „durch Hefe oder Trebern zum Ge- 
rinnen bringen“ beruhen. — Ob zu dt. triibe auch av. driwi- „Flecken, 
Muttermal“? (ware dhrdbhi--, Charpentier KZ. 40, 460 f., der besondere enge 
Verwandtschaft mit anord. blbp-drefjar „Bluttropfen“ annimmt, das aber 
zu draf „Abfall“, Wz. dhrebh- „zerbrechen“ gehort). 

2. dher- ( dhere -) „halten, festhalten, stiitzen“. 

Ai. dhar- „halten, tragen, stutzen, erhalten, aufrecht halten“, vratam 

„ein Gesetz beobachten“ (Praes. meist dhardyati ; Pf. dadhdra , dadhre; 
=== 55300 ===
u. *g*er- „Berg“). Scheftelowitz IF. 33, 165 f. 

rp/.do) v dkdm u ist Kreuzung von dXdco mit cpkiftw , wie andrerseits cpMfiw 
durch Kreuzung mit dkaco auch zu dkfpco umgestaltet ist (s. Yf. IF. 19, 
105, LEWb. 2 u. fligo ; Scheftelowitz aaO., auch schon ZdMG. 59, 697, setzt 
freilich auch fiir dktfim unter Yerkniipfung mit av. driivilca- n. „ Angst, 
Schaudern“ (Bartholomae Airan. Wb. 778 iibersetzt hingegen „St6hnen“) 
und driwi- f. „Flecken, Mal“ nach Sch. „Pockennarben“) idg. dhl- voraus, 
doch sind die av. Worter keine verlaBliche Stiitze fiir ein solches idg. 
*dkleib- „driickend reiben“ und ist die Annahme eines dialektischen Wan- 
dels von gr. ■&).- zu cpk- (bzw. pi zu /?-) nicht begrundet.
```


## [2026-09-05T20:10:57.610Z] TOOL CALL #46: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://abadis.ir/fatofa/%D8%AA%D8%B1%D8%A7%D8%AE%D9%85/' --note \"page 129 node 7: Mo'in/Dehkhoda entry for تراخم (trachoma)\" 2>&1 | tail -2"
}
```


### [2026-09-05T20:11:01.381Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/ac3081cf49e6c1bf.txt
```


## [2026-09-05T20:11:03.366Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n \"تراخم\" ac3081cf49e6c1bf.txt | head -30"
}
```


### [2026-09-05T20:11:03.418Z] TOOL RESULT

```
4:TITLE: تراخم - معنی در دیکشنری آبادیس
6:تراخم - معنی در دیکشنری آبادیس 
10: تراخم
13: مترادف تراخم : چشم درد، تورم پرده چشم
18: تراخم. [ تْرا / ت َ خ ُ ] ( از فرانسوی ، اِ ) مرضی است مسری و مزمن که در همجو، مخصوصاً در قسمت لاپلکی آن دانه هایی تولیدمی کند که کم کم به قسمت همجوی بن کیسی و حتی روی یامه ( قرنیه ) رسیده و بالاخره منجر به پژمردگی همجو میگردد که بشکل نوارهای التیامی در پشت پلک دیده میشود.
19:نشانه ها: مانند اغلب امراض مزمن شروع تراخم نیز بی سروصدا و مخفی است ، بطوری که غالباً ممکن است شخص ماهها و سالها مبتلا به تراخم باشد بدون این که مختصر توجهی به کسالت خود نموده باشد. به این ترتیب ابتدای این کسالت را غالباً هنگام معاینه بچه ها قبل از ورود به کودکستان یا دبستان و یا معاینه سربازان میشود دید. گاهی نیز برحسب اتفاق در موقعی که شخص برای چیز دیگر مثلاً ضربه چشم یا همجوئید حاد مراجعه می کند، پزشک به تراخم او پی میبرد،و اگر از این بیماران که در روی همجوی پلکی آنان پراز دانه های تراخمی است تحقیقاتی از سابقه چشم آنهابعمل آید معمولاً اظهار میدارند که تاکنون چشم درد نکشیده اند. فقط گاهی برخی از اشخاص خیلی حساس برای سنگینی پلکها و تاب ترسی ( خوف النور ) رجوع کرده و اظهار میدارند که صبحها خیلی بزحمت چشمها را باز می کنند، یادر موقع کار چشمهایشان آب ریزش دارد بنابراین نشانه های نهشتی در ابتداء همان آبریزش و تاب ترسی و سنگینی و خستگی چشمهاست. علایمی که چشم پزشک می تواند ببیند، در دوره سیر تراخم متفاوت است و بهمین جهت دانشمندان تراخم را به حالتهای مختلف تقسیم کرده و دوره دوم را که دوره تراخم کامل است برحسب اینکه با همجوئید فصلی یا همجوئید سوزاکی توأم باشد بدسته های فرعی منقسم نموده اند. در اینجا برای سهولت امر از دسته های فرعی صرفنظر میشود و برای اینکه علائم تراخم را در حالات و دوره های مختلف آن شرح دهیم آنرا بشرح زیر تقسیم می کنیم : 1- تراخم اولیه یا مشکوک. 2- تراخم عمومی یا قطعی. 3- تراخم التیامی.
20:تراخم اولیه : این دوره از تراخم را چون هیچ نوع نشانه خارجی ندارد بیشتر در هنگام معاینه دانش آموزان دبستانها می توان دید، در این حال اگر پلکهای کودک مبتلا را برگردانده دقت کنیم دانه هایی بقطر چهار تا هشت دهم میلیمتر در روی همجوی لاپلکی ( ملتحمه ظفره ) مخصوصاً در کنار بالایی آن خواهیم دید و چون در کودکان لنفاوی مزاج نیز دانه هایی شبیه بدانه های نامبرده منتها قدری کوچکتر دیده میشود و این خود باعث اشتباه در تشخیص است ، به این مناسبت این حالت از تراخم را برخی از دانشمندان تراخم مشکوک نامیده اند. فرق میان دانه های تراخمی و دانه های طبیعی در این است که دانه های تراخمی را همیشه رگهای کوچک احاطه کرده اند و مختصری هم از دانه های طبیعی بزرگتر میباشند و از طرف دیگر عده دانه های طبیعی شش تا هشت عددبیشتر نبوده و معمولاً در ثلث داخلی و خارجی کنار بالائی لاپلک ( غضروف ظفره ای ) جا دارند، در صورتی که عده ٔدانه های تراخمی بزودی زیاد شده و تمام کنار بالایی لاپلک را میگیرد. دانه های داخلی غالباً بهم چسبیده و توده بزرگی را درست می کنند، در صورتی که دانه های خارجی مدتها از یکدیگر جدا هستند. این حالت از تراخم ممکن است ماهها و سالها بدون تغییر مانده و بیمار از وجود آن آگاه نشود، فقط اشخاص حساس مختصر سنگینی در چشم خود احساس خواهند کرد. بیشتر بخوانید ... 
37:نوعی عفونت چشمی مزمن، شبیه التهاب ملتحمۀ شدید. در این بیماری، ملتحمه ملتهب شده، چرک و جوشگاه تشکیل می شود، و گاه به آسیب قرنیه می انجامد. علت آن عفونت سازواره ای شبه ویروسی، با نام کلامیدیا، است. بیماری در مناطق گرم و خشک شایع است و به درمان با آنتی بیوتیک ها پاسخ می دهد. با این حال، این بیماری شایع ترین علت منفرد کوری در جهان است. در ۱۹۹۹، ۱۴۶میلیون نفر در دنیا به تراخم مبتلا بودند. اکثر مبتلایان در کشورهای در حال توسعه زندگی می کنند. wikijoo: تراخم 
42: تراخم
50: تراخم ؛ تِرِخ ، تِرِخت ، تِرِختی ، تِرِخت شدن ، سفت و سیخ بودن ، از رِخوَت در آمدن و ریخت یافتن
59:اصطلاح محلی نیز از کلمه ی ترخ و تراخم در حالتی که کسی راست و استوار بخواهد راه برود می گویند تِرخ تِرِخ راه رفتن. 
61:در مجموع مفهوم کلمه ی تراخم در چشم پزشکی و علم طب به دانه های سفتی که در پشت پلک های چشم ایجاد می شود گفته می شود.
69: تراخم یک بیماری چشم است، به معنای چشم درد.
```


## [2026-09-05T20:11:24.432Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '8530,8575p' incoming/ARY/ARY_pages.txt; echo \"=== which pdf page ===\"; awk 'NR<8575 && /\\[pdf page/ {p=$0} END{}' incoming/ARY/ARY_pages.txt; grep -n \"\\[pdf page\" incoming/ARY/ARY_pages.txt | awk -F: '$1<8575' | tail -3"
}
```


### [2026-09-05T20:11:26.175Z] TOOL RESULT

```
خی (707۸7252): 57۸ پسگشت‌ها رای ان ل ۳
سانسکریت (54۸/8/8/7): 0۷17197۸ ,001۸7 8 موه
رومانی ((۸14ل(#): 1 (886030) ایرد ها ۱
۸ ۵ ,ش2015 بقه +5 07 تلهلط
آلمانی (08701۸(7): لاد نما 58 ,0177-108
[pdf page 290]
۹
دویدن, دو / ۲۹۱
بادداشت:
چم اين واژه در زبان آلبانی: دوما"
چم اين واژه در زبان هتیت؛ ستوان دوم
ِ
:
اوستایی (4۳:874(۷): 0889 2۸ انگلیسی کهن (ب7ولا2۸/0 012)(شاید)
را ت0۸ ,05۸1۷
پپلوی (۲ماللم): انگلیسی (2۸0/574)(شاید) اند اد
,3۸1187۸ ,0۸۷۸7۸ دانمارکی (0۸۸//824)(شاید) 206
,09۷8830۸3 ,0۸۷70۸8 سوئدی (537722/573)(شاید) 2۸6
سانسکریت (54(785777): هلندی (01767)(شاید) 127
1 013۸ ,082۷۸75
آرمنی (434/8(/42): 0/۸ پسگشت‌ها شک تیا
بونانی 07280): 0 ۶000
0 ,7351 ,730 3 (0) 7
ایسلندی کهن (/(52270104/4 010)(شاید) 253 موم
6 131 (8۲۱) 0/275
نررس کهن (۸0788 012)(شاید) 694 دی
00606 3 (08) :0(0(5
آلمانی کهن ((087244 777077 010)(شاید) 7 (05) 547
۹ ت70 010 :043 ۸ 07لا
.ار آلمانی (0880/40)(شاید) 7۸7 برهان قاطع + .۹
است بادداشت.
چم این واژه در زبان‌مالهنر و اروپایی کهن: دویدن» جاری شدن. :
چم اين واژه در زبان‌های ژرمنی نوین: ژاله,
اوستایی (/4(8974): ۰ 0۸3181 ,0۸301 پارسی باستان (۶37807 0ا0):
[pdf page 291]
۸11۸ ,نت0۸ انگلیسی (تکلاه/۵: 10۷۳ ,00۷۲۷
پهلری (1/لالمه): 0 هلندی (070ان 71
کردی (4ل03). 0۸ اسلاوی کهن (ع4ذل5 نان صامم:
بلرچی (ات‌ناستمه: 5 ,ت05 متططاضی
افغانی (پشتو) (۸۳0[7۸21). 13 روسی (/42ا5کتا): 03
تخاری ۸ (۸ ۸(۷ل70727۸7). اد رنه با لیتوانی (۸2(هناب 7 رم).
تخاری 8(8 #۸ 7027۸). اد ادن ره با 56 ما0
سغدی ((56007014): روهار ایرلندی کهن (للكل#ا ضان):
سانسکریت ‎ :)64۸/587/7(‏ 0۸ ,اق0 7 010۸1۸ ,0
برنانی (08881): ۰ 2018108 ,0051۵09 سلتی (کلتی) (ع2/71): 00
لاتین (/712ا): زان ولزی (۴8ل): ,010۸8
=== which pdf page ===
8505:[pdf page 289]
8535:[pdf page 290]
8564:[pdf page 291]
```


## [2026-09-05T20:11:38.124Z] TOOL CALL #49: Bash

```json
{
 "command": "timeout 300 python3 tools/ref_page.py ARY:291 2>&1 | head -60"
}
```


### [2026-09-05T20:11:43.371Z] TOOL RESULT

```
(no exact page map; using offset -1 -> pdf page 290; check the printed number and re-run with --pdf-page if off)
REF: ARY:291  PDF: data/verification/sources/refs/incoming/ARY/ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf page 290  OCR-lang: fas+eng

له
یادداشت؛
چم اين واژه در زبان آلبانی: دوما"
چم اين واژه در زبان هتیت: ستوان دوم
ٍ
ْ
ٍ
اوستایی (۸۲-9747): 085179 ,2۸ انگلیسی کهن (8ل8۸01 012)(شاید)
071 ت0۸ ,05۸۷
پهلوی (1ها۳۸(7): انگلیسی (6۸/01/57)(شاید) 12
,3۸۷187۸ ,0۸۷۸7۸ دانمارکی (0۸۸//5)(شاید) 206
,0۷۷۸810۸ رل0۸۷10۸3 سوئدی (57750/527)(شاید) 2۸:6
سانسکربت (54/5707077): هلندی (017627)(شاید) 124
71 ,077۸ ,071۸۷۸7۳
ارمنی (4/07144): 0۸ پسگشت‌ها رده رات دنت
بونانی 07880): 0 ۶002/0
0 ,77781 ,17780 3 (03۷) 7
ایسلندی کهن (54(/010۸/4۸ ۲)010(شاید) 253 ههام 05
06 ۰ |131۱ (8۲۱) :۸0727
نررس کهن (۸0۶5 010)(شاید) 694 8
00606 3 (05۷0) :0110275
آلمانی کهن (/(052/۸ 27704 2ا0)(شاید) 7 (05۷) 57
: ت70 071 :۸0۸/3 ۸ 07 نت۱4۸
ی آلمانی (/020/۸)(شاید) 71۸7 برهان قاطع : ۹.۲
7 بادداشت:
چم این واژه در زبان مافل‌اهند و اروپایی کهن: دویدن» جاری شدن. ۱
چم این واژه در زبان‌های ژرمنی نوین: ژاله.
اوستایی (/(4۲857۸): ۰ 2۸177۷1 ,ت0۸01 پارسی باستان (۷/ف۶88۶ 0ا0):
```


## [2026-09-05T20:12:03.650Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HUB davidan ===\"; grep -n \"davîden\\|davîdan\\|dawîdan\\|davidan\" HUB.txt | head -10; echo \"=== SYN dew/run ===\"; grep -n \"^10\\.46\\|Dew\\b\" SYN.txt | head -10; echo \"=== IEC dhawo ===\"; grep -n \"dhāwō\\|dhawō\\|dhāw-\\|dhaw-\" IEC.txt | head -10"
}
```


### [2026-09-05T20:12:03.742Z] TOOL RESULT

```
=== HUB davidan ===
=== SYN dew/run ===
17472:10.46 RUN (vb.)
=== IEC dhawo ===
```


## [2026-09-05T20:12:42.647Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '17472,17530p' SYN.txt | grep -n -i \"pers\\|dhav\\|dāv\\|Skt\" | head -20"
}
```


### [2026-09-05T20:12:42.709Z] TOOL RESULT

```
2:Be: Aor, eépapovr, Goth. rinnan, pragjan Lith. bégti, lekéli tpé : ON renna, hlaupa Lett. — skriet Bot cirra x) Dan. fbe ChSl. testi ‘ carrer Sw. springa, rénna (lépa) SCr. tréali *  couriy OE irnan, rinnan, Boh. _ bézeli ‘ correr pr@gan Pol. —_biedz tm, dlerga ME © renne Russ. bezat’ + rethim NE run Skt.  dhdv-, dru-, dra- yw Thim Du. loopen Av. taé-, dru- thedeg OHG  loufan, rinnan redek, MHG loufen, rinnen NHG  laufen, rennen
9:(poet.), cf. dpduos ‘course’; Skt. dram- ‘run about, wander’. *dra-. Skt. dra- (8sg. drati); Grk. azo- bt6pacxw ‘run away’, aor. arédpav. " *dreu-. Skt. dru- (8sg. dravati), Av. dru- (caus. dravaya-, pple. drita-, but only of Daevic beings); Goth. trudan ‘tread, step’, etc.
12:Grk. #éw, with éods ‘swift? : Skt. dhav-
19:4. Ir. rethim, NIr. rithim, W. Br. redek :*Ir. roth, W. rhod, OHG rad Lat. rota ‘wheel’, Skt. ratha- ‘chariot’, Walde-P. 2.368, Pedersen 2.600 f. :
20:5. Goth. rinnan, ON renna, OF irnan rinnan, ME rinne, renne, NE run, OHG rinnan, MHG rinnen (NHG rinnen): hence NHG rennen, Sw. rdnna, orig. caus. = OHG rennan, ON renna (pret, rende) ‘cause to run’, Goth. ur-rannjan ‘cause (the sun) to rise’ : Skt, r- (8sg. roti, rnvati) ‘move, stir’ (10.11), Grk. épvune ‘rouse, move’, ete, Walde-P. 1.138. Falk-Torp 890, 901. Feist 398 f.
26:Lett. dial. vert, prob. fr. *wer- under- lying words for ‘turn’ (10.12). Walde-P. 1.271. Persson, Beitrige 956.
27:7. ChSl. testz, tekq ‘run, flow’, whence the Slavie words for ‘flow’ (cf. 10.32) : Lith. tekéti ‘flow, run’, Lett. tecét ‘flow’, Ir. techim ‘flee’ (10.51), Av. taé- (88g. taéaiti) ‘run, flow’, Skt. tak- (3sg. taklt) ‘rush’. Walde-P. 1.715.
30:8. Skt. and Ay. words, above, 1, 2, 7.
32:Go’ is understood here as covering the most generic verbs denoting locomo- tion, without necessary implication of direction or goal. In so far as they are used for ‘go away, BO from’, it is only by contrast to those for ‘come’, as in NE come and go, etc. In NE come and the other European words listed under ‘come’ (10.48) there is the implication of approach toward or arrival at a goal (which is often felt as the real or imagined position of the speaker or another; but any such defini- tion is too narrow). Itis probable that this situation fairly reflects the difference in value between the two important IE roots *ei- and *g’em-, as essentially one of aspect. The eae expressed the action of going ae a the latter involved the im- telation is aia aoe ER AH their oe y partially maintained in oth used Sas Skt. i and gam- are ot ‘come? ere we must translate ‘go’ { according to the situation or 1 Prefix employed ( j di Come’, sam- for popenally. sd: for ihe Cl Tare, gam- eine only that Av. <- is Prefix mostly tequent and without
36:OCOMOTION, TRANSPORTATION, NAVIGATION 693 10.47 GO Goth. gaggan, -leipan, -stei- Lith. ili tpt, gee gan ; Lett.  zel, pret. gaju Ci TT ate wd- ON — ganga, fara, lida ChSl. iti, choditi Me He (Oe are) Dan. gaa (fare) SCr. iti, hoditi [a dere, ea) ead Sw. 4 (fara) Boh. ili, choditi __andare he lab OE gangan, gan, faran, Pol. —_i8¢, chodzié ie aller, vat, *7 wadan Russ. idli, chodit’ op. tr, voy nbla ME go, gonge, fare Skt. t-, y¢-, gam-, ga- jum. “ne -rega, aul) NE = go, went Av. jam-, i-, ya-, dvar- Ir ei (chuaidh, rag- Du. gaan, vane Nir. eT dh) OHG oariget gan, faran, h, el, idan Y. myned (a, aelh MHG gén, gan, varn, liden unt, (a, eas, yelo,  NHG gehen (fahren) Br. 2 etc.)
41:*ei-. Grk. due (but mostly fut. in sense); Lat. ire (> Sp. ir, Fr. fut. iraz, It. inf. ire, imperat. tte, etc.); Lith. eztz, Lett. iet, ChSl. it, SCr. 767, Boh. jiti, Pol. is¢, Russ. idti, Skt. 2- (38g. ett), Av. i- (88g. aeiti, OPers. aitiy); Hitt. im- perat. 2sg. it, 2pl. ten (Sturtevant, Hitt. Gram. 95).
42:*yG-. Skt., Av. ya- : Lith. joti, Lett. jat, ChSl. jachati ‘ride’, etc.; uncertain Goth. iddja, OE éode ‘went’, which, moreover, do not coincide (Feist 288 f.) ; Toch. A yd- ‘go’ (SSS 423, 458); Hitt. ya- ‘go, march’ (Sturtevant, Hitt. Gloss. 184).
48:venire ‘come’ (> the Romance words) ; Goth. giman, OE cuman, etc., general Gme. for ‘come’; Skt., Av., OPers. gam- ‘go, come’ (Skt. gacchati, Av. fasaiti, sko- presents like Grk. Bacxw; Av. Jam- without prefix mostly ‘come’; also Av., OPers. a-jam- ‘come’, whence NPers. amadan ‘come’); Toch. kém-, kum-, etc. ‘come’ (SSS 428 f.).
49:*gra-. Grk. aor. &8nv, Dor. é8av; Skt. aor. agam, pres. jigali; Av. aor. gat; Lett. gaju ‘went’ (pret. to zet).
```


## [2026-09-05T20:12:44.749Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC dheu ===\"; grep -n \"^dheuō\\|dheu-\\|dhevō\\|dhewō\" IEC.txt | head -10; echo \"=== IEC dhregh/dhragh ===\"; grep -n \"dhrāghus\\|dhraghu\\|dhrogh\\|dherəgh\\|dheragh\" IEC.txt | head -10"
}
```


### [2026-09-05T20:12:44.806Z] TOOL RESULT

```
=== IEC dheu ===
2872:dheu- (1) “flow. Cf. dhouos, dheunt. WP I, 834 Skt. dhávate, 3s.; Gk. théo, théwo ‘run, scud'; Gallo-Brit. Deva (n. of River Dee); Lat. cf. fons: fontis (fr. *dheunts fountain); Gaul. cf. divona ‘fountain’. (Isophonic w. Go. diwan 'to die")
2873:dheu- (2) “bright; shine, daytime’ Skt. cf. dhavalah ‘glistening’; Gk. cf. theion 'sulphur, theo (2) ‘shine’. Perh. also in theiló-pedon 'sunny spot'; cf. also leuka-théa (ambig.) beside théā ‘view, sight; OS cf. (?) -digu, -du in hiu-digu, -du ‘today’: OHG hiu-tu, -to; uncertainly Arm. -Éean in tunfean ‘of the daytime’
2875:dheuelos, dheuolos, see dheu- (2)
2876:dheunt- (dheuont-) ‘flowing; flow’. Cf. dheu- (1) & dhouos Skt. -dhavat, dhavat ‘running’; Gk. théon, -óntos, id.; Lat. fons, fontis ‘fountain’ (vo-
2879:dheuos, ios ‘kinsman, affinis’. Skt. dhaváh “husband, lord"; Arm. cf. ur-£u, gs or-Éui, if for type *putro-dheu- 'son-in- law’; Gk. theios ‘uncle’; theía ‘aunt
3045:dhouos (dhouuo-) (running, flowing; run, flow, course’. WP I, 834 Vedic cf. dhavate, 3s. ‘flows’; dhavati, id.; dhàvin, adj. ‘running’; Per. dav ‘running, race’; davad, 3s. ‘runs’; Gk. thoós ‘rapid’; Hitt. cf. (?) tawal a sacrificial drink’; Alb. cf. déjet, 3s. mp. ‘thaws; OHG tou; Du. dauw; LG dau; OE dēaw ‘dew’; Du. cf. also dooi, m. ‘thaw’; G auf-tauen, v. id.; ON dọgg ‘dew’. Cf. also Lat. fóns, gs fontis ‘fountain’; Per. davende ‘running’ and see dheu-
3245:dhüið (1) “shake, stir, dash, rouse’. Cf. dhunio Skt. (redup. *dheu-dhu-) do-dhüye ‘shudder’; dhuvámi “shake; struggle’; dhünomi, id.; Gk. thúo, Lesb. thuið ((1) ‘storm, rage"); ON dýja ‘shake, brandish’; Icel. dúa ‘thud, echo,
=== IEC dhregh/dhragh ===
```


## [2026-09-05T20:12:58.480Z] TOOL CALL #53: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://www.cnrtl.fr/etymologie/trachome' --note \"page 129 node 6: French trachome, date and origin\" 2>&1 | tail -1; echo ---; f=$(python3 - <<'EOF'\nimport hashlib;print(hashlib.sha1('https://www.cnrtl.fr/etymologie/trachome'.encode()).hexdigest()[:16])\nEOF\n); grep -n -i \"trachome\\|1808\\|grec\" /home/sfmqrb/git/rishe/data/verification/sources/web/$f.txt | head -20"
}
```


### [2026-09-05T20:13:01.555Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/00df87111104727a.txt
---
1:URL: https://www.cnrtl.fr/etymologie/trachome
```


## [2026-09-05T20:13:03.968Z] TOOL CALL #54: Bash

```json
{
 "command": "sed -n '1,40p' /home/sfmqrb/git/rishe/data/verification/sources/web/00df87111104727a.txt"
}
```


### [2026-09-05T20:13:04.019Z] TOOL RESULT

```
URL: https://www.cnrtl.fr/etymologie/trachome
FETCHED: 2026-09-05T20:13:01Z
STATUS: 200
TITLE: Portail lexical

Portail lexical
```


## [2026-09-05T20:13:07.948Z] TOOL CALL #55: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://fr.wiktionary.org/wiki/trachome' --note \"page 129 node 6: French trachome etymology\" 2>&1 | tail -1; grep -n -A6 -i \"Étymologie\" /home/sfmqrb/git/rishe/data/verification/sources/web/$(python3 -c \"import hashlib;print(hashlib.sha1('https://fr.wiktionary.org/wiki/trachome'.encode()).hexdigest()[:16])\").txt | head -30"
}
```


### [2026-09-05T20:13:10.556Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/fb441df6e47e6334.txt
76: Étymologie 
77-
78- 1.2 
79- Nom commun 
80-
81- 1.2.1 
82- Vocabulaire apparenté par le sens 
--
165: Étymologie 
166- [ modifier le wikicode ] 
167-
168- ( 1752 ) Du latin trachoma , emprunté au grec ancien τράχωμα , trákhôma , lui-même de  τραχύς ,  trákhus («   rugueux   »). 
169-
170- Nom commun 
171- [ modifier le wikicode ]
```


## [2026-09-05T20:14:02.711Z] AGENT

Now I have all the evidence. Let me write the verification file.


## [2026-09-05T20:20:41.048Z] TOOL CALL #56: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk129.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW_FA = \"https://en.wiktionary.org/wiki/%D8%AF%D9%88%DB%8C%D8%AF%D9%86\"\nW_GR = \"https://en.wiktionary.org/wiki/%CF%84%CF%81%CE%B1%CF%87%CF%8D%CF%82\"\nE_TRA = \"https://www.etymonline.com/word/trachoma\"\nE_DARK = \"https://www.etymonline.com/word/dark\"\nE_DEW = \"https://www.etymonline.com/word/dew\"\nAB_TRA = \"https://abadis.ir/fatofa/%D8%AA%D8%B1%D8%A7%D8%AE%D9%85/\"\nFR_TRA = \"https://fr.wiktionary.org/wiki/trachome\"\n\ndoc = {\n \"pdf_page\": 129,\n \"book_page\": 99,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Dher 2, Dherabh, Dhrâbh; Dhragh 2\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *dʰer- / *dʰerə- 'sediment, dirt; to stir up the mud, make turbid, darken', with the consonantal extensions *dʰerəgʰ-/*dʰrəgʰ- and *dʰerəbʰ- : *dʰrābʰ- : *dʰrəbʰ- (Pokorny IEW 251-252; Watkins dher-1)\",\n   \"note\": \"Pokorny IEW p.251 heads the entry '1. dher-, dherə- in kons. Erweiterungen „trüber Bodensatz einer Flüssigkeit, auch allgemeiner von Schmutz, Widerlichkeit, von quatschigem Wetter, von trüben Farbentönen usw.; verbal: Bodensatz und Schlamm aufrühren, trüben“', and its sub-sections are exactly the secondary names of Nourai's root box: a. dherəgh- (= his 'Dhragh 2', to be kept apart from dherāgh- 'to draw', IEW 257, his 'Dhragh 1') and d. dherəbh- : dhrābh- : dhrəbh- (= his 'Dherabh, Dhrâbh', IEW 252). Watkins/AHD prints the same root as 'dher-1. To make muddy; darkness … [Pok. 1. dher- 251.]' and hangs on it precisely the two branches Nourai draws: '*dher-g- in Germanic *derk- in Old English deorc, dark: DARK' and 'suffixed extended zero-grade form *dhrə-gh- in … Greek trakhus, rough: TRACHEA, TRACHOMA, TRACHYTE'. So root, language label and gloss are right. Two caveats, both recorded on the nodes: Nourai's numbering is his own (Pokorny's 1. dher- is 'muddy', his 2. dher- is 'to hold' — Nourai reverses them), and Beekes rejects the Greek branch (see node 4).\",\n   \"note_fa\": \"جعبهٔ ریشه همان ریشهٔ هندواروپایی آغازینِ *dʰer-/*dʰerə- است که پوکورنی در صفحهٔ ۲۵۱ فرهنگ خود با معنای آلمانی «تهْ‌نشستِ تیرهٔ مایع، چرک و لجن؛ و در معنای فعلی: لجن را برهم زدن، تیره کردن» آورده است؛ نام‌های فرعی نمودار (Dherabh، Dhrâbh، Dhragh ۲) نیز همان گسترش‌های همخوانیِ dherəgh- و dherəbh- : dhrābh- : dhrəbh- در صفحه‌های ۲۵۱–۲۵۲ همان کتاب‌اند. واتکینز (پیوست ریشه‌های هندواروپایی فرهنگ American Heritage) نیز همین ریشه را dher-¹ «گِل‌آلود کردن؛ تاریکی» می‌نویسد و درست همان دو شاخه‌ای را از آن می‌گیرد که نورایی کشیده است: ژرمنی *derk- > انگلیسی dark، و یونانی trakhús > trachoma. پس ریشه، برچسب زبان و معنا درست است. دو نکته: شماره‌گذاری «Dher ۲» از خودِ نورایی است (نزد پوکورنی dher-¹ همین ریشه و dher-² «نگه داشتن» است)، و بیکس پیوند واژهٔ یونانی را با این ریشه نمی‌پذیرد (نگاه کنید به گرهٔ ۴).\",\n   \"sources\": [E_DARK, E_TRA, W_GR],\n   \"ref_check\": [\n    {\"ref\": \"POK:251\", \"status\": \"supports\",\n     \"note\": \"POK_01.txt line 3574 f. (IEW p.251, the page number stands on line 3573): '1. dher-, dherə- in kons. Erweiterungen „trüber Bodensatz einer Flüssigkeit, auch allgemeiner von Schmutz, Widerlichkeit, von quatschigem Wetter, von trüben Farbentönen usw.; verbal: Bodensatz und Schlamm aufrühren, trüben“ Ursprüngl. eins mit dher- „Unrat, cacare“'; the same page's section 'a. dherəgh-' carries 'gr. θράσσω, att. θράττω „verwirre, beunruhige“ … τρᾱχύς, ion. τρηχύς „rauh, uneben“'. Nourai's English gloss is an accurate condensation of the German.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. I 854 f. (WLD_Bd1_1930 djvu line 53856 ff.)\", \"stance\": \"supports\",\n     \"note\": \"'1. dher-, dherə- in kons. Erweiterungen … „trüber, schmieriger, ranziger, stinkender Bodensatz einer Flüssigkeit, auch allgemeiner von Schmutz, Widerlichkeit … verbal: Bodensatz und Schlamm aufrühren, trüben“. Ob ursprgl. eins mit dher- „Unrat, cacare“?' — the entry Pokorny 251 abridges, with the same sub-section '1. dherəgh-' (Gk. θράσσω, ταράσσω, τραχύς).\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, d-list (AHD_watkins1985.txt, s.v. dher-1)\", \"stance\": \"supports\",\n     \"note\": \"'dher-1. To make muddy; darkness. 1. Suffixed form *dher-g- in Germanic *derk- in Old English deorc, dark: DARK. … 4. Suffixed extended zero-grade form *dhrə-gh- in: a. Greek tarassein … to confuse, disturb: ATARACTIC; b. Greek trakhus, rough: TRACHEA, TRACHOMA, TRACHYTE. [Pok. 1. dher- 251.]'\"},\n    {\"src\": \"KLN\", \"where\": \"s.v. trachea (KLN_1966.txt line 39743)\", \"stance\": \"supports\",\n     \"note\": \"'Τραχεῖα is the fem. of τραχύς, „rough“, which is prob. rel. to θράσσειν, „to trouble, disquiet“, and cogn. with ON. dregg, „dregs“; see dreg' — Klein joins exactly the Greek 'rough/disturb' words and the Germanic 'dregs' words that make up this root.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Avestan\", \"words\": \"driwi 1\", \"verdict\": \"plausible\",\n     \"derivation\": \"Avestan driwi- (Bartholomae's headword driwi̯a-/driwi- f. 'Flecken, Mal', especially 'Muttermal', attested only in compounds: mā-driwya- in Vd. 2.29 beside the other daxšta- 'marks', and driwyō in Vd. 19.43) would go back to *dʰrəbʰi- , the zero grade of the dherəbʰ- : dhrābʰ- : dhrəbʰ- extension whose other members are ON draf, OE dræf 'dregs, refuse', OHG truobi 'turbid', Goth. drōbjan 'to trouble' — i.e. 'sediment, dirty deposit' → 'blemish, spot on the skin'. The equation is possible but expressly uncertain: Pokorny p.252 prints 'Unsicher av. driwi- (*dhrəbhi-) „Flecken, Muttermal“'; Walde-Pokorny I 855 puts it as a question ('Ob zu dt. trübe auch av. driwi- „Flecken, Muttermal“? (wäre *dhrəbhi-, Charpentier KZ. 40, 460 f.)'), and Bartholomae himself writes only 'Et.?' under the entry. Nourai's gloss adds a colour the sources do not have: Bartholomae and Pokorny say 'spot, mark, birthmark', never 'dark' birthmark — the 'dark' comes from the root's own semantics, not from the Avestan word.\",\n     \"derivation_fa\": \"واژهٔ اوستایی driwi- (نزد بارتولومه ذیل driwi-/driwya-، مادّه‌ای مؤنث به معنای «لکه، نشان» و به‌ویژه «خالِ مادرزاد»، که تنها در ترکیب‌های وندیداد ۲٫۲۹ و ۱۹٫۴۳ آمده) را می‌توان بازساختِ *dʰrəbʰi- دانست، یعنی درجهٔ صفرِ همان گسترشِ dherəbʰ- که نمایندگانِ دیگرش نورس کهن draf «تفاله» و آلمانی بالای کهن truobi «تیره، گل‌آلود» است؛ تحول معنایی از «تهْ‌نشست و چرک» به «لکه و خالِ پوست» است. با این همه، این پیوند در خودِ مأخذها قطعی نیست: پوکورنی در صفحهٔ ۲۵۲ آن را با قید «Unsicher» (نامطمئن) می‌آورد، والده-پوکورنی آن را به‌صورت پرسش و به نقل از شارپانتیه ثبت کرده و بارتولومه ذیل همین مدخل تنها می‌نویسد «؟Et». افزون بر این، «تیره» بودنِ خال افزودهٔ نورایی است؛ مأخذها تنها «لکه، خال» می‌گویند. پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\"ref\": \"POK:252\", \"status\": \"supports\",\n       \"note\": \"POK_01.txt line 3586 ff. (IEW p.252, section 'd. dherəbh- : dhrābh- : dhrəbh-'): 'Unsicher av. driwi- (*dhrəbhi-) „Flecken, Muttermal“; mir. drab „Treber, Hefe“ … aisl. draf, engl. draff „Berme, Hefe“ …'. The page carries exactly the arrow Nourai draws, but marks it 'uncertain'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"AiW s.v. driwi̯a- (BRT.txt line 14146 f.; the entry stands just before driwika- 'Stöhnen, Heulen', AiW col. 771-772)\", \"stance\": \"partial\",\n       \"note\": \"'j. driwi̯a- f. „Flecken, Mal“ (nur Komp.). a) bes. „Muttermal“: mā driwya … mai�iyanąm anyąm daxštanąm …' V.2.29; 'b) … driwyō daēvō V.19.43'. Then: 'Et.?' — Bartholomae confirms the word and the sense 'birthmark' but offers NO etymology, and does not call it dark.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. I 855 (WLD_Bd1_1930 djvu line 53986)\", \"stance\": \"partial\",\n       \"note\": \"'— Ob zu dt. trübe auch av. driwi- „Flecken, Muttermal“? (wäre *dhrəbhi-; Charpentier KZ. 40, 460 f. …)'. Walde-Pokorny states the connection as an open question credited to Charpentier, which is the source of Pokorny's 'Unsicher'.\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. dher-1\", \"stance\": \"silent\",\n       \"note\": \"Watkins lists only the Germanic, Greek and Celtic reflexes of dher-1 (dark, dregs, drivel, ataractic, trachea); no Iranian word at all, so the appendix neither supports nor denies the Avestan item.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Germanic\", \"words\": \"derk\", \"verdict\": \"plausible\",\n     \"derivation\": \"Proto-Germanic *derkaz 'dark' (OE deorc, whence ME derk; OHG tarchanjan 'to hide, conceal', MHG terken 'to besmirch', MLG dork 'bilge') is derived by Pokorny and Watkins from the g-extension *dʰer-g- of this root, semantically 'muddy, turbid' → 'murky, dark' — the same shift seen in Lith. dergti 'to become filthy; to be bad weather' and MIr. derg 'red'. Pokorny p.252 section 'b. dherg-' lists 'mir. derg „rot“; mhd. terken „besudeln“, ahd. tarchannen … ags. deorc „dunkelfarbig“, engl. dark', and Watkins repeats it verbatim. The reservation: Etymonline (following the Germanicists) calls PGmc *derkaz 'of uncertain etymology', so the arrow is the standard handbook view rather than a settled one.\",\n     \"derivation_fa\": \"ژرمنی آغازین *derkaz «تاریک» (انگلیسی کهن deorc، آلمانی بالای کهن tarchannen «پنهان کردن»، آلمانی میانه terken «آلودن») را پوکورنی و واتکینز از گسترشِ کامیِ همین ریشه، یعنی *dʰer-g-، می‌گیرند؛ تحول معنایی از «گل‌آلود و تیره» به «تاریک» است، همان‌گونه که در لیتوانیایی dergti «چرکین شدن؛ هوای بد بودن» و ایرلندی میانه derg «سرخ» دیده می‌شود. پوکورنی در صفحهٔ ۲۵۲، بخش «b. dherg-»، عیناً می‌نویسد: «ags. deorc „dunkelfarbig“, engl. dark». تنها احتیاط این است که ریشه‌شناسی *derkaz نزد ژرمن‌شناسان امروز قطعی شمرده نمی‌شود (اتیمولاین: «of uncertain etymology»)؛ پس ادعای نورایی دیدگاهِ رایجِ کتاب‌های مرجع است، نه حکمی بی‌چون‌وچرا.\",\n     \"sources\": [E_DARK],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"Watkins 1985 s.v. dher-1: 'dher-1. To make muddy; darkness. 1. Suffixed form *dher-g- in Germanic *derk- in Old English deorc, dark: DARK.' Nourai's node reproduces Watkins' *derk- exactly, including the spelling without a case ending.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"IEW 252, section b. dherg- (POK_01.txt line 3580 f.)\", \"stance\": \"supports\",\n       \"note\": \"'b. dherg- in: mir. derg „rot“; mhd. terken „besudeln“, ahd. tarchannen, terchinen „(verdunkeln) verbergen, verstecken“, mnd. dork „Kielwasserraum“, ags. deorc „dunkelfarbig“, engl. dark.'\"},\n      {\"src\": \"KLN\", \"where\": \"s.v. trachea (KLN_1966.txt line 39743) and dreg\", \"stance\": \"supports\",\n       \"note\": \"Klein places the 'dark/dregs' Germanic group and the Greek 'rough' group in one family ('τραχύς … cogn. with ON. dregg, „dregs“; see dreg'), i.e. the same root box.\"},\n      {\"src\": \"WEB\", \"where\": \"Etymonline s.v. dark (archived)\", \"stance\": \"partial\",\n       \"note\": \"'from Old English deorc … from Proto-Germanic *derkaz (source also of Old High German tarchanjan „to hide, conceal“), which is of uncertain etymology' — the Germanic form is exactly as drawn, but its attachment to the IE root is not treated as established. (Consulted online in place of Webster's vol. 2, which is not in the local library.)\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"English\", \"words\": \"dark\", \"verdict\": \"confirmed\",\n     \"derivation\": \"OE deorc 'without light, gloomy' > ME derk > NE dark; the -er- > -ar- vowel change is the regular 15th-c. English development before a consonant (cf. ME dereling > darling, ME fer > far, ME hert > hart). Attested figuratively 'sad, sinister' already in Old English, of colours from late 14c., 'secret' from late 14c.\",\n     \"derivation_fa\": \"انگلیسی کهن deorc «بی‌روشنایی، تیره و غم‌انگیز» > انگلیسی میانه derk > انگلیسی نو dark. تبدیل er- به ar- در سدهٔ پانزدهم میلادی قاعده‌مند است (همان‌گونه که dereling به darling و fer به far بدل شده). این حلقه از زنجیره هیچ اختلافی ندارد و ادعای نورایی درست است.\",\n     \"sources\": [E_DARK],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\",\n       \"note\": \"The node carries no reference of its own; it inherits AHD from its parent, which spells out 'Old English deorc, dark: DARK'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein s.v. dark\", \"stance\": \"supports\",\n       \"note\": \"The OCR of the 1966 edition does not carry a line-initial 'dark' entry that grep can reach ('grep -n \\\"^dark\\\" KLN_1966.txt' is silent — the two-column scan runs entries together), but Klein's trachea entry (line 39743) cites the same family; recorded as a confirming but not directly quotable lookup.\"},\n      {\"src\": \"WEB\", \"where\": \"Etymonline s.v. dark (archived)\", \"stance\": \"supports\",\n       \"note\": \"'Middle English derk, later dark, from Old English deorc … For vowel change, see marsh' — exactly the OE > ME > NE chain of this arrow.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"Greek\", \"words\": \"traxus\", \"verdict\": \"plausible\",\n     \"derivation\": \"Greek τραχύς (Ionic τρηχύς) 'rough, uneven; harsh', beside θράσσω/ταράσσω 'I stir up, trouble'. Pokorny p.251 derives it from *dʰr̥əgʰú-s, the zero grade of the dherəgʰ- extension ('wohl ursprüngl. von Schmutzkrusten' — originally of crusts of dirt), and Watkins repeats this ('*dhrə-gh- … Greek trakhus, rough: TRACHEA, TRACHOMA, TRACHYTE'), which is exactly what the chart draws. Modern Greek etymology is split: Wiktionary reconstructs *dʰréh₂gʰ-us ~ *dʰr̥h₂gʰ-éws 'rough' from a root *dʰreh₂gʰ- 'to irritate' and links only θρᾱ́σσω, while Beekes explicitly 'discounts' the connection with dark/dregs and keeps only the tie to thrassein. So the word and the intra-Greek family are certain; the attachment to Nourai's root box is Pokorny's and Watkins' view, not the current consensus. Nourai's transliteration 'traxus' is his usual x for χ, and his gloss 'disturbing, rough' merges the senses of θράσσω and τραχύς.\",\n     \"derivation_fa\": \"یونانی τραχύς (در ایونی τρηχύς) «زبر، ناهموار، درشت»، هم‌خانوادهٔ θράσσω/ταράσσω «برهم زدن، آشفتن». پوکورنی (ص ۲۵۱) آن را از *dʰr̥əgʰú-s، درجهٔ صفرِ گسترشِ dherəgʰ-، می‌گیرد و می‌افزاید که معنای نخستین آن احتمالاً «پوستهٔ چرک و لجنِ خشکیده» بوده؛ واتکینز نیز همین را می‌گوید و trachoma و trachea را ذیل همان ریشه می‌آورد — یعنی درست همان چیزی که نمودار کشیده است. اما ریشه‌شناسی امروزیِ یونانی دودسته است: ویکی‌واژه ریشهٔ جداگانهٔ *dʰreh₂gʰ- «آزردن، خراشیدن» را بازمی‌سازد و بیکس پیوند این واژه را با dark و dregs رد می‌کند و تنها هم‌ریشگی با θράσσω را می‌پذیرد. پس واژه و معنایش درست است، ولی وصل کردنِ آن به این جعبهٔ ریشه دیدگاهِ پوکورنی–واتکینز است، نه اجماع امروز. نویسهٔ «traxus» هم شیوهٔ خودِ نورایی برای نگارشِ χ است.\",\n     \"sources\": [W_GR, E_TRA],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"Watkins 1985 s.v. dher-1, §4: 'Suffixed extended zero-grade form *dhrə-gh- in: a. Greek tarassein (Attic tarattein), to confuse, disturb: ATARACTIC; b. Greek trakhus, rough: TRACHEA, TRACHOMA, TRACHYTE.' — the node's form, gloss and its two English continuations all come from this line.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"IEW 251, section a. dherəgh- (POK_01.txt line 3576 ff.)\", \"stance\": \"supports\",\n       \"note\": \"'Gr. θράσσω, att. θράττω … „verwirre, beunruhige“; ταραχή „Verwirrung“, ταράσσω … „verwirre“ (*dhr̥əgh-i̯ō); τρᾱχύς, ion. τρηχύς „rauh, uneben“ (wohl ursprüngl. von Schmutzkrusten; -ᾱ- hier aus sog. r̥, d.i. *dhr̥əghú-s).'\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. I 854 (WLD_Bd1_1930 djvu line 53864 ff.)\", \"stance\": \"supports\",\n       \"note\": \"'1. dherəgh-: Gr. θράσσω, att. θράττω … „verwirren, beunruhigen“ (ursprgl. wohl vom Aufrühren des Schlammbodens in einem Gewässer); … τραχύς, jon. τρηχύς „rauh, uneben“ … -ρᾱ- hier aus sog. r̥, d. i. *dhr̥əghu-s.'\"},\n      {\"src\": \"KLN\", \"where\": \"s.v. trachea (KLN_1966.txt line 39743)\", \"stance\": \"supports\",\n       \"note\": \"'…τραχύς, „rough“, which is prob. rel. to θράσσειν, „to trouble, disquiet“, and cogn. with ON. dregg, „dregs“; see dreg and cp. trachoma, trachyte.'\"},\n      {\"src\": \"WEB\", \"where\": \"Etymonline s.v. tracheo- (archived with 'trachoma')\", \"stance\": \"partial\",\n       \"note\": \"'Greek trakheia is from trakhys „rough, uneven, stony“ … which according to Watkins is connected to the root of dark and dreg, but Beekes discounts this and says it is related to thrassein „to trouble, disturb“.' — the dispute in one sentence.\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"Latin\", \"words\": \"\", \"verdict\": \"plausible\",\n     \"derivation\": \"Empty pass-through node: the Latin link is Modern (Medical) Latin trachōma, not a Classical Latin word. Greek τράχωμα 'roughness' (τραχύς + the noun suffix -ωμα, the ordinary medical formant of sarcōma, carcinōma) was taken over by 17th-century medical Latin as trachoma, the name for the granular roughening of the inner eyelid; from that neo-Latin term both the English and (through French) the Persian word come. Klein and Etymonline both label it 'Medical L.' / 'Modern Latin', so the chart's bare '[Latin]' box is right in substance but hides the fact that this is scientific New Latin of c. 1690, not a word of the Roman language.\",\n     \"derivation_fa\": \"این گره تهی و تنها حلقهٔ واسطه است. پیوندِ «لاتینی» در اینجا لاتینِ کلاسیک نیست، بلکه لاتینِ نوِ پزشکی است: یونانی τράχωμα «زبری» (از τραχύς با پسوندِ اسم‌سازِ -ωμα، همان که در sarcōma و carcinōma هست) در سدهٔ هفدهم میلادی به‌صورت trachoma وارد اصطلاح‌نامهٔ پزشکیِ لاتین شد و نامِ زبرشدنِ دانه‌دارِ پشتِ پلک گردید؛ واژهٔ انگلیسی و — از راه فرانسه — واژهٔ فارسی هر دو از همین صورتِ لاتینِ نو آمده‌اند. کلاین «Medical L.» و اتیمولاین «Modern Latin» می‌نویسند. پس جعبهٔ «لاتینی» در ماهیت درست است، اما این نکته را پنهان می‌کند که سخن از لاتینِ علمیِ حدود ۱۶۹۰ است نه زبان رومیان.\",\n     \"sources\": [E_TRA, FR_TRA],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Empty box with no reference of its own in the book; checked against Klein and Etymonline instead.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"s.v. trachoma (KLN_1966.txt line 39755)\", \"stance\": \"supports\",\n       \"note\": \"'trachoma, n., a contagious disease of the eyes (med.) — Medical L. trachoma, fr. Gk. τράχωμα, „roughness“, fr. τραχύς, „rough“; see trachea and -oma.'\"},\n      {\"src\": \"WEB\", \"where\": \"Etymonline s.v. trachoma (archived)\", \"stance\": \"supports\",\n       \"note\": \"'1690s, from Modern Latin trachoma, from Greek trakhoma „roughness“, from trakhys „rough“.'\"}\n     ]\n    },\n    {\n     \"id\": 6, \"lang\": \"French\", \"words\": \"\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Empty pass-through node: French trachome, first attested 1752 (fr.wiktionary; the term spreads in French ophthalmology after the Egyptian campaign of 1798-1801, when 'ophtalmie d'Égypte' became a European epidemic), borrowed from the medical Latin trachoma and thence from Greek τράχωμα. French is the correct intermediary for the Persian word, because 19th- and early-20th-century Persian medicine took its whole terminology from French.\",\n     \"derivation_fa\": \"این گره نیز تهی و واسطه است: فرانسویِ trachome، نخستین کاربردِ ثبت‌شده ۱۷۵۲ میلادی، وام‌گرفته از لاتینِ پزشکیِ trachoma و از آن‌جا از یونانیِ τράχωμα. رواجِ این اصطلاح در پزشکیِ فرانسه پس از لشکرکشی ناپلئون به مصر (۱۷۹۸–۱۸۰۱) و همه‌گیریِ «چشم‌دردِ مصری» در اروپا است. فرانسه به‌درستی حلقهٔ میانیِ واژهٔ فارسی است، زیرا پزشکیِ ایران در سدهٔ سیزدهم و چهاردهم خورشیدی اصطلاحاتش را یکسره از فرانسه گرفت.\",\n     \"sources\": [FR_TRA],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Empty box with no reference of its own; checked against fr.wiktionary and Dehkhoda's 'از فرانسوی' tag on the Persian word.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"WEB\", \"where\": \"fr.wiktionary.org s.v. trachome (archived)\", \"stance\": \"supports\",\n       \"note\": \"'(1752) Du latin trachoma, emprunté au grec ancien τράχωμα, trákhôma, lui-même de τραχύς, trákhus (« rugueux »).'\"},\n      {\"src\": \"MON\", \"where\": \"Dehkhoda/Mo'in via abadis.ir s.v. تراخم (archived)\", \"stance\": \"supports\",\n       \"note\": \"'تراخم. [تْرا / تَ خُ] (از فرانسوی، اِ) مرضی است مسری و مزمن که در همجو (ملتحمه) … دانه‌هایی تولید می‌کند' — the Persian lexicographic tradition itself names French as the source, confirming this link of the chain.\"}\n     ]\n    },\n    {\n     \"id\": 7, \"lang\": \"Persian\", \"words\": \"tarâxom «تراخم»\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Persian تراخم tarāxom 'trachoma' is a 20th-century medical loan from French trachome (Gk τράχωμα → Med.Lat. trachoma → Fr. trachome → Pers. تراخم), the French -ome being rendered -om/-am and written with خ for the Greek/French kh sound. Dehkhoda's article marks it '(از فرانسوی، اِ)' = 'from French, noun', and Mo'in (the page Nourai cites) gives the same word with the ophthalmological definition. The Arabic-looking shape (t-r-ā-x-u-m, as if a faʿālul pattern) is accidental: the word has no Arabic root and did not travel through Arabic; it is a straight phonetic spelling of the French term, adopted with the rest of Persian clinical vocabulary in the Dār al-Funūn/Pahlavi era, when trachoma was the commonest cause of blindness in Iran.\",\n     \"derivation_fa\": \"«تراخم» وام‌واژه‌ای پزشکی از فرانسویِ trachome است که در سدهٔ چهاردهم خورشیدی وارد فارسی شده: یونانی τράχωμα ← لاتینِ پزشکی trachoma ← فرانسوی trachome ← فارسی «تراخم»؛ خوشهٔ آغازینِ tr در فارسی با کسرهٔ کوتاه شکسته شده و صدای kh فرانسوی/یونانی با «خ» نوشته شده است. دهخدا در ذیل همین واژه می‌نویسد «(از فرانسوی، اِ)» و معین (همان صفحه‌ای که نورایی یاد کرده) واژه را با همان تعریفِ چشم‌پزشکی آورده است. شکلِ ظاهراً عربیِ واژه (بر وزن «تفاعل/فعالُل») تصادفی است: این واژه ریشهٔ عربی ندارد و از راه عربی هم نیامده، بلکه نویسه‌گردانیِ مستقیمِ اصطلاحِ فرانسوی است. پس ادعای نورایی — یونانی › لاتینی › فرانسوی › فارسی — درست است.\",\n     \"sources\": [AB_TRA, E_TRA, FR_TRA],\n     \"ref_check\": [\n      {\"ref\": \"MON:1058\", \"status\": \"supports\",\n       \"note\": \"Mo'in, Farhang-e Fārsi, the تراخم entry (MON_part1.txt line 39489, in the ت section of vol. 1, consistent with the cited p.1058): 'تراخم … (پز.) مرضی است که چشم را عارض می‌شود و موجب پیدایش جوش‌های عفونی در مخاط پلک بالا شده و پلک را از حالت معمول ضخیم‌تر … اگر معالجه نشود موجب ناراحتی‌های شدید می‌گردد و عاقبت منجر به کوری می‌شود.' The bracketed origin tag is mangled in this OCR ('همق:د)'), but Dehkhoda's parallel article states '(از فرانسوی)', i.e. exactly Nourai's French → Persian arrow.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"abadis.ir, Dehkhoda + Mo'in articles on تراخم (archived)\", \"stance\": \"supports\",\n       \"note\": \"'تراخم. [تْرا / تَ خُ] (از فرانسوی، اِ) مرضی است مسری و مزمن …' — explicit French origin.\"},\n      {\"src\": \"BQT\", \"where\": \"Borhān-e Qāteʿ (ed. Moʿin), ت section\", \"stance\": \"silent\",\n       \"note\": \"A 17th-century Persian dictionary cannot contain a 20th-century medical Europeanism; grep of BQT_v1_pages.txt for تراخم returns nothing, as expected. Recorded so the silence is not mistaken for a failed lookup.\"},\n      {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e rishe-hā-ye hend-o-orupāyi\", \"stance\": \"silent\",\n       \"note\": \"grep of incoming/ARY/ARY_pages.txt for تراخم finds nothing; Aryanpur treats inherited Persian vocabulary, not modern European loans.\"}\n     ]\n    },\n    {\n     \"id\": 8, \"lang\": \"English\", \"words\": \"trachoma\", \"verdict\": \"confirmed\",\n     \"derivation\": \"English trachoma, first recorded in the 1690s, taken directly from the Modern/Medical Latin trachōma (Greek τράχωμα 'roughness'), so called because the disease roughens the inner surface of the eyelids; the same Greek adjective gives English trachea (via Med.Lat. trachia, Gk (ἀρτηρία) τραχεῖα 'the rough windpipe') and trachyte. Watkins lists TRACHEA, TRACHOMA, TRACHYTE together under dher-1, exactly the chart's branch.\",\n     \"derivation_fa\": \"انگلیسیِ trachoma، نخستین کاربردِ ثبت‌شده در دههٔ ۱۶۹۰ میلادی، مستقیماً از لاتینِ نو/پزشکیِ trachōma (از یونانیِ τράχωμα «زبری») گرفته شده؛ نام‌گذاری از آن روست که این بیماری سطحِ درونیِ پلک را دانه‌دار و زبر می‌کند. همان صفتِ یونانی، واژه‌های trachea (نای، از «شریانِ زبر») و trachyte را نیز ساخته است. واتکینز هر سه را با هم ذیل ریشهٔ dher-¹ می‌آورد — همان شاخه‌ای که نورایی کشیده است. ادعای نورایی درست است.\",\n     \"sources\": [E_TRA],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\",\n       \"note\": \"No reference on the node; it inherits the parent's AHD, whose dher-1 entry ends '…Greek trakhus, rough: TRACHEA, TRACHOMA, TRACHYTE.'\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"s.v. trachoma (KLN_1966.txt line 39755)\", \"stance\": \"supports\",\n       \"note\": \"'trachoma … — Medical L. trachoma, fr. Gk. τράχωμα, „roughness“, fr. τραχύς, „rough“ … The disease is so called because it is characterized by the roughness of the inner surface of the eyelids.'\"},\n      {\"src\": \"WEB\", \"where\": \"Etymonline s.v. trachoma (archived)\", \"stance\": \"supports\",\n       \"note\": \"'disease of the eyes characterized by granulation on the eyelid, 1690s, from Modern Latin trachoma, from Greek trakhoma „roughness“, from trakhys „rough“.'\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 3,\n   \"root\": \"Dheu 1\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *dʰeu- 'to run, flow' (Pokorny IEW 259 '1. dheu- „laufen, rinnen“'; Watkins dheu-2 'to flow')\",\n   \"note\": \"Pokorny p.259 gives '1. dheu- „laufen, rinnen“' with precisely the material of this chart: 'Ai. dhávate „rennt, rinnt“, dehnstufig dhāvati ds., dhāutí- „Quelle, Bach“; mpers. davīdan „laufen, eilen“, pām. dav- „laufen, rennen“ … anord. dǫgg, Gen. dǫggvar (*dawwō), ags. dēaw, as. dau, ahd. tou n. „Tau“ (*dawwa-)'. Watkins numbers it dheu-2 and glosses it, like Nourai, simply 'To flow', citing '[Pok. 1. dheu- 259.]'. So the root, its language label, its gloss and Nourai's own POK:259 citation are all correct — indeed Pokorny's entry itself names the Middle Persian verb, which is unusual and makes this one of the better-sourced charts in the book. The single weak point is the topmost Iranian node: no Avestan or Old Persian verb dav- 'to run' is attested (see node 1); the Iranian branch of this root begins, in the record, with Middle Persian.\",\n   \"note_fa\": \"ریشهٔ نمودار همان ریشهٔ هندواروپاییِ آغازینِ *dʰeu- «دویدن، روان شدن» است. پوکورنی در صفحهٔ ۲۵۹ ذیل «1. dheu- „laufen, rinnen“» درست همین مواد را می‌آورد: سنسکریت dhávate «می‌دود، روان می‌شود»، فارسی میانه davīdan «دویدن، شتافتن»، و در آلمانیِ کهن tou و انگلیسی کهن dēaw «شبنم» از *dawwa-. واتکینز نیز آن را dheu-² با معنای «to flow» می‌نویسد و به همان صفحهٔ ۲۵۹ پوکورنی ارجاع می‌دهد. پس ریشه، برچسب زبان، معنا و ارجاعِ خودِ نورایی (POK:259) همه درست است؛ نکتهٔ درخورِ توجه آن‌که خودِ پوکورنی فعلِ فارسیِ میانه را در متنِ ریشه آورده و این نمودار را از مستندترین نمودارهای کتاب کرده است. تنها نقطهٔ سستِ آن، بالاترین گرهِ ایرانی است: هیچ فعلِ اوستایی یا پارسی باستانِ dav- به معنای «دویدن» گواهی نشده و شاخهٔ ایرانیِ این ریشه، در اسناد، از فارسی میانه آغاز می‌شود (نگاه کنید به گرهٔ ۱).\",\n   \"sources\": [W_FA, E_DEW],\n   \"ref_check\": [\n    {\"ref\": \"POK:259\", \"status\": \"supports\",\n     \"note\": \"POK_01.txt line 3720 (the page numeral 259 stands on line 3708): '1. dheu- „laufen, rinnen“. Ai. dhávate „rennt, rinnt“, dehnstufig dhāvati ds., dhāuti-ḥ f. „Quelle, Bach“; mpers. davīdan „laufen, eilen“, pām. dav- „laufen, rennen“'; the entry continues on p.260 with 'gr. θέω … θοός „schnell“' and 'anord. dǫgg … ags. dēaw, as. dau, ahd. tou n. „Tau“ (*dawwa-)'. WP. I 834.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. I 834 (WLD_Bd1_1930 djvu line 52566 ff.)\", \"stance\": \"supports\",\n     \"note\": \"'1. dheu- „laufen, rinnen“. Ai. dhavate „rennt, rinnt“ … mp. davidan „laufen, eilen“, pam. dav- „laufen, rennen“. Gr. θέω … : anord. dǫgg, gen. dǫggvar (*dawwō), ags. deaw, as. dau, ahd. tou, nhd. Tau (*dawwa-).' It adds the warning that Skt. dhāvati „reinigt, macht blank“ (to wash) is a DIFFERENT root — relevant to node 4.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. dheu-2\", \"stance\": \"supports\",\n     \"note\": \"'dheu-2. To flow. Germanic *dauwaz, dew, in: a. Old English dēaw, dew: DEW; b. compound *melith-dauwaz, „honeydew“ (see melit-). [Pok. 1. dheu- 259.]' — Nourai's gloss 'to flow' is Watkins' wording verbatim.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann, IEC s.v. dheu- (1) and dhouos (IEC.txt lines 2872, 3045)\", \"stance\": \"supports\",\n     \"note\": \"'dheu- (1) „flow“. Cf. dhouos, dheunt. WP I, 834. Skt. dhávate, 3s.; Gk. théo, théwo „run, scud“ …'; and 'dhouos (dhouuo-) „running, flowing; run, flow, course“ … Per. dav „running, race“; davad, 3s. „runs“ … OE dēaw „dew“ … ON dǫgg „dew“ … Per. davende „running“' — Mann puts the Persian verb, the Persian agent noun davande and the Germanic 'dew' words under one root, i.e. the whole chart.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Avestan / Old Persian\", \"words\": \"daw\", \"verdict\": \"plausible\",\n     \"derivation\": \"The Old Iranian verbal root *dau- 'to run' is real and is the necessary ancestor of MP dawīdan/NP davīdan, but it is NOT attested in either Avestan or Old Persian, so the box's language label is wrong. Cheung, Etymological Dictionary of the Iranian Verb, s.v. *dau2 'to run', lists only 'MIDDLE PERSIAN: MMP dw-, BMP dw(b)- /daw-/', '*NWIR: NP davīdan/dav-, Kurd. dawin/daw-, Gil. dovastən', '*NEIR: Oss. dawyn, Yaghn. daw-/dáuta' and Skt. dhav — no Old Iranian attestation at all. Bartholomae's AiW knows four Avestan roots dav-, none of them 'run' (1dav- 'to speak', of daevic beings; 2dav- 'to drive away'; 3/4dav- with frā- 'to rub clean' = Skt. dhāv- 'wash'; 5dav- 'to press'); Kent's Old Persian lexicon has no dav- at all; and Buck's synonym list gives Av. taē- and dru- as the Avestan words for 'run'. Nourai's own source is milder than his box: Abolghasemi, Feʿl-hā-ye Fārsi-ye Dari p.54, writes 'ایرانی باستان *dav-', i.e. reconstructed Old Iranian, not attested Avestan/Old Persian. The derivation is therefore right in substance (PIE *dʰeu- > Old Iranian *dau-, with the regular Iranian loss of the aspirate: PIE *dʰ > Ir. d) and wrong only in the language label.\",\n     \"derivation_fa\": \"ستاکِ ایرانیِ باستانِ *dav- «دویدن» واقعی است و نیای ضروریِ فارسی میانهٔ dawīdan و فارسی نوِ «دویدن» به شمار می‌رود؛ اما در هیچ متنِ اوستایی یا پارسی باستان گواهی نشده است، و از این رو برچسبِ زبانِ این جعبه نادرست است. چونگ در فرهنگ ریشه‌شناختیِ فعل‌های ایرانی، ذیل *dau² «دویدن»، تنها صورت‌های فارسی میانهٔ مانوی و کتابی (dw-/daw-)، فارسی نو (davīdan/dav-)، کردی (dawin)، گیلکی، آسی و یغنابی را می‌آورد و هیچ صورتِ ایرانیِ باستانِ گواهی‌شده‌ای ندارد. بارتولومه چهار ریشهٔ اوستاییِ dav- می‌شناسد که هیچ‌کدام «دویدن» نیست («سخن گفتن» از موجوداتِ دیوی، «راندن»، «سترون و پاک ساییدن» = سنسکریت dhāv «شستن»، و «فشردن»)؛ در واژه‌نامهٔ پارسی باستانِ کنت نیز چنین فعلی نیست؛ باک هم واژه‌های اوستاییِ «دویدن» را taē- و dru- می‌داند. مأخذِ خودِ نورایی نیز محتاط‌تر از جعبهٔ اوست: ابوالقاسمی در «فعل‌های فارسی دری» ص ۵۴ می‌نویسد «ایرانی باستان *dav-»، یعنی صورتِ بازسازی‌شده، نه گواهی‌شده. بنابراین اصلِ اشتقاق درست است (dʰ هندواروپایی در ایرانی به d بدل شده) و تنها برچسبِ «اوستایی/پارسی باستان» نادرست است؛ ادعای نورایی با این تصحیح پذیرفتنی است.\",\n     \"sources\": [W_FA],\n     \"ref_check\": [\n      {\"ref\": \"FFD:54\", \"status\": \"partial\",\n       \"note\": \"Abolghasemi, Feʿl-hā-ye Fārsi-ye Dari p.54 = incoming/FFD/FFD_pages.txt pdf page 59 (printed = pdf − 5), s.v. دویدن: 'دوید < فارسی میانه … مادهٔ ماضی جعلی است از … / دو < فارسی میانه daw + ایرانی باستان *dav-… ریشهٔ dav به معنی «دویدن» است' (the Latin forms are largely destroyed by the Persian OCR, but the words «ایرانی باستان» = Old Iranian and the root dav are legible). The page supports the root and the Middle Persian link, but calls the form Old IRANIAN (reconstructed), not Avestan or Old Persian.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"CHEUNG\", \"where\": \"EDIV s.v. *dau2 'to run' (CHEUNG.txt lines 5286-5300)\", \"stance\": \"contradicts\",\n       \"note\": \"'*dau2 „to run“. MIDDLE PERSIAN: MMP dw-, BMP dw(b)- (LHTWN-) /daw-/ „to run“ … *NWIR: NP davidan/dav-, Kurd. dawin/daw- … *NEIR: Oss. dawyn/dawd … Yghn. dau-/dáuta „to run“ … *SANSKRIT: dhav … «PIE *dʰeu- „to move, go“ > LIV: 147 f. | Pok.: 260, 262»'. Cheung's Avestan section is EMPTY for this root — the standard modern treatment of the Iranian verb records no Avestan/OP form.\"},\n      {\"src\": \"BRT\", \"where\": \"AiW s.v. 1dav- … 5dav- (BRT.txt lines 12797, 12806, 12810, 12813)\", \"stance\": \"contradicts\",\n       \"note\": \"'j. 1dav- V. „sprechen“, von daēvischen Wesen'; 'j. 2dav- V. „entfernen“ … „forttreiben, fortjagen“'; 'j. 3dav- V., nur mit frā „reinigend abreiben“ … ai. dhāvati'; 'g. 4dav- V. „(sich) drängen“'. None of Bartholomae's Avestan dav- roots means 'to run'.\"},\n      {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon\", \"stance\": \"silent\",\n       \"note\": \"grep -n '^dav' KNT.txt returns nothing: the Old Persian lexicon has no verb dav-, so the 'Old Persian' half of the label is unsupported as well.\"},\n      {\"src\": \"SYN\", \"where\": \"Buck 10.46 RUN (SYN.txt line 17472 ff.)\", \"stance\": \"contradicts\",\n       \"note\": \"Buck's table gives 'Skt. dhāv-, dru-, drā-' but 'Av. taē-, dru-' for 'run', and his commentary adds '*dreu-. Skt. dru-, Av. dru- (… but only of Daevic beings)'. The Avestan words for 'run' are taē- and dru-, not dav-.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. I 834\", \"stance\": \"partial\",\n       \"note\": \"Walde-Pokorny's Iranian evidence for this root is 'mp. davidan „laufen, eilen“, pam. dav- „laufen, rennen“' — Middle Persian and Pamir, no Avestan or Old Persian.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"davîtan\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Middle Persian dawīdan / dawistan 'to run' (Book Pahlavi written with the Aramaic ideogram LHTWN-tn' from Aram. √rht 'run', phonetically dwytn' / dwstn'; Manichaean MP dw- /daw-/, 3pl. dwyynd, participle dwwʾn /dawān/). The older transcription of dwytn' is davītan — exactly the form Nourai prints, taken over from Horn and Nyberg. Formation: Old Iranian present stem *dau- + the MP infinitive suffix -tan on a secondary past stem daw-īd-, i.e. the 'weak' inchoative-denominative type that spreads in Middle Persian (dawīd- beside the older sigmatic dawist-). The same verb continues unbroken into New Persian.\",\n     \"derivation_fa\": \"فارسی میانهٔ dawīdan/dawistan «دویدن»؛ در پهلویِ کتابی با هُزوارشِ آرامیِ LHTWN-tn' (از ریشهٔ آرامیِ rht «دویدن») و به‌صورتِ آوایی dwytn'/dwstn' نوشته می‌شود، و در فارسی میانهٔ مانوی dw- /daw-/ آمده است. خوانشِ کهن‌ترِ dwytn' همان davītan است — دقیقاً صورتی که نورایی آورده و آن را از هرن و نیبرگ گرفته است. ساخت: ستاکِ حالِ ایرانیِ باستان *dav- به‌علاوهٔ ماده ماضیِ جعلیِ -īd- و پسوندِ مصدریِ -tan، همان الگوی «مصدرِ جعلی» که در فارسی میانه رواج می‌یابد (dawīd- در کنارِ صورتِ کهن‌ترِ dawist-). این فعل بی‌گسست به فارسی نو رسیده است. ادعای نورایی درست است.\",\n     \"sources\": [W_FA],\n     \"ref_check\": [\n      {\"ref\": \"POK:259\", \"status\": \"supports\",\n       \"note\": \"Pokorny's own text on the cited page names the Middle Persian verb: 'mpers. davīdan „laufen, eilen“' (POK_01.txt line 3721) — the arrow Old Iranian → Pahlavi davītan is in the cited page itself.\"},\n      {\"ref\": \"FFD:54\", \"status\": \"supports\",\n       \"note\": \"incoming/FFD/FFD_pages.txt pdf page 59 (= printed 54), s.v. دویدن: 'دوید < فارسی میانه … / دو < فارسی میانه daw …' — Abolghasemi derives both the NP past stem and the NP present stem from the Middle Persian forms.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD p.25 s.v. dawīdan (PHD.txt line 310)\", \"stance\": \"supports\",\n       \"note\": \"'daw-, v. dawīdan, dawistan. … 1dawīdan, daw- [LHTWN-tn! < A √rht; dwytn', dwb- | M dw-, N ~] run. 2dawīdan, daw- [dw-ytn'] speak (daevic). 1,2 dawistan [LHTWN-stn!, dwstn'] = 1dawīdan.' MacKenzie normalises dawīdan; the ideogram and the phonetic spelling dwytn' are both given.\"},\n      {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (Glossary) s.v. davistan (NYB_vol2_glossary.txt line 1243)\", \"stance\": \"supports\",\n       \"note\": \"'davistan [LHTWN-stn'], davītan [dwytn', LHTWN-tn'] to run, pt. = pret. 3d p. sg. davist [LHTWN-st'] … MPrs dw-, Verbum 173; NP davīdan.' Nyberg spells the infinitive davītan — letter for letter Nourai's form — and himself draws the arrow to NP davīdan.\"},\n      {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 585, p.130 (HRN.txt line 5251 ff.)\", \"stance\": \"supports\",\n       \"note\": \"'585. dev(î)den „laufen, eilen“ … phlv. davītan (auch … geschrieben)'.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Persian\", \"words\": \"davîdan «دویدن»\", \"verdict\": \"confirmed\",\n     \"derivation\": \"New Persian دویدن davīdan (colloquial dowīdan), present stem دو dow-, continues MP dawīdan without change: MP -aw- is written و and read ow/av, and MP final -tan > NP -dan after a vowel (dawītan > davīdan), the same voicing seen in dīdan, šenīdan. The chart's extra words are all transparent members of the same family: (a) دو ۲ dow = the bare present stem used as a noun 'a run, running' (Mann: 'Per. dav „running, race“; davad, 3s. „runs“'); (b) دونده davande = dow- + the present-participle/agent suffix -ande, 'runner' (Mann lists 'Per. davende „running“'); (c) پادو pā-dow = پا 'foot' + دو 'run', literally 'foot-runner', an errand-boy — Borhān-e Qāteʿ defines it 'شخصی را گویند که خدمات جزئی به او رجوع باشد و هر ساعت او را به کاری فرستند'. Wiktionary states the same chain: 'Inherited from Middle Persian LHTWN-tn /dawīdan/, from Proto-Indo-European *dʰew- „to run“'.\",\n     \"derivation_fa\": \"«دویدن» (davīdan؛ در گفتار dowīdan) با ستاکِ حالِ «دو» دنبالهٔ بی‌واسطهٔ فارسی میانهٔ dawīdan است: -aw- فارسی میانه در خط فارسی با «و» نوشته می‌شود و -tan پایانیِ مصدر پس از واکه در فارسی نو به -dan نرم شده است (dawītan > دویدن)، همان تحولی که در «دیدن» و «شنیدن» هم دیده می‌شود. واژه‌های افزودهٔ نمودار همه از همین خانواده‌اند: «دو ۲» همان ستاکِ حال است که اسم شده («دویدن، مسابقهٔ دو»؛ مان در فرهنگ تطبیقیِ هندواروپایی «Per. dav „running, race“» می‌آورد)؛ «دونده» از «دو» + پسوندِ فاعلیِ «-نده» (مان: «Per. davende»)؛ و «پادو» از «پا» + «دو»، تحت‌اللفظ «پا-دو»، که برهان قاطع آن را چنین تعریف می‌کند: «شخصی را گویند که خدمات جزئی به او رجوع باشد و هر ساعت او را به کاری فرستند». ویکی‌واژه نیز همین زنجیره را می‌دهد: «برگرفته از فارسی میانهٔ dawīdan، از هندواروپایی آغازینِ *dʰew-». ادعای نورایی درست است.\",\n     \"sources\": [W_FA],\n     \"ref_check\": [\n      {\"ref\": \"BQT:902\", \"status\": \"supports\",\n       \"note\": \"Borhān-e Qāteʿ ed. Moʿin, BQT_v2_pages.txt leaf 362 = printed p.902 (offset printed = leaf + 540, fixed in the page-127 check by دنیدن on leaf 348 = p.888). Moʿin's footnote at the foot of the page: '# دویدن ـ بفتح اول و چهارم، از: دو + یدن (پسوند مصدری). هندی باستان dhāv-… (جاری شدن)، پهلوی davīt…، وخی … (دویدن)، سریکلی … (چارنعل رفتن) «اشتقاق ۵۸۵»؛ … شتابان رفتن، رفتن با تعجیل بسیار، تاختن' — the analysis دو + یدن, the Sanskrit dhāv-, the Pahlavi form, and even a cross-reference to Horn's entry no. 585, which is Nourai's other citation here.\"},\n      {\"ref\": \"HRN:130\", \"status\": \"supports\",\n       \"note\": \"Horn, Grundriss der neupersischen Etymologie no. 585, printed p.130 (HRN.txt line 5251, the running number '— 131 —' follows two entries later): '585. dev(î)den „laufen, eilen“, devān, devāmden, ai. √dhav, dhávati „rennen, rinnen, strömen“; phlv. davītan (auch … geschrieben); gr. θέω. Wax. vidāv-am „laufen, rennen“, sar. davān-am „galoppiren“.' Exactly the chart's Sanskrit-Pahlavi-Persian chain.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"Moʿin's etymological footnote in Borhān, p.902 (as quoted above)\", \"stance\": \"supports\",\n       \"note\": \"'از: دو + یدن (پسوند مصدری) … «اشتقاق ۵۸۵»' — Moʿin analyses the infinitive as present stem دو + the infinitive suffix, precisely Nourai's دو ۲ / دویدن pair.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"EDIV s.v. *dau2 (CHEUNG.txt line 5294)\", \"stance\": \"supports\",\n       \"note\": \"'*NWIR: NP davidan/dav-, Kurd. dawin/daw-, Gil. (Rsht.) dovastən/dov-, Siv. doui-/douiya „to run“ … (sec. caus.) Gil. davanənen/davan- „to cause to run“.'\"},\n      {\"src\": \"IEC\", \"where\": \"Mann, IEC s.v. dhouos (IEC.txt line 3045)\", \"stance\": \"supports\",\n       \"note\": \"'Per. dav „running, race“; davad, 3s. „runs“ … Per. davende „running“' — Mann independently records both extras دو and دونده under this root.\"},\n      {\"src\": \"BQT\", \"where\": \"Borhān-e Qāteʿ, BQT_v2_pages.txt leaf 348 = printed p.888 (the دو / دوادو / پادو block)\", \"stance\": \"supports\",\n       \"note\": \"The پادو entry: 'شخصی را گویند که خدمات جزئی باو رجوع باشد و هر ساعت او را بکاری فرستند'; on the same leaf Moʿin's footnote to دوادو reads 'از: دو (دویدن) + ا (واسطه) + دو (ایسا)', i.e. he analyses these compounds through the verb 'to run', which is Nourai's extras list.\"},\n      {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e rishe-hā, printed p.291-292 (incoming/ARY/ARY_pages.txt, pdf pages 290-291)\", \"stance\": \"partial\",\n       \"note\": \"The headword 'دویدن, دو' is there with an Avestan/Pahlavi/Sanskrit/Greek cognate table and a citation to Borhān-e Qāteʿ, and the note 'چم این واژه در زبان … هند و اروپایی کهن: دویدن، جاری شدن' ('the sense of this word in Proto-Indo-European: to run, to flow') — which matches the root gloss; but the Latin-script forms are destroyed in both the bulk OCR and a fresh tesseract pass (ref_page.py ARY:291), so nothing can be quoted from the cognate columns.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"Sanskrit\", \"words\": \"dhav\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Sanskrit √dhāv-/dhav- 'to run, flow' (3sg. dhávate 'runs, streams', lengthened-grade dhāvati; derivative dhāutí- f. 'spring, brook'), attested from the Rigveda; it preserves the PIE aspirate that Iranian loses (*dʰeu- > Skt. dhav-, Ir. dav-), which is what makes the Sanskrit form the control for the whole Iranian branch. One caution the chart does not mention: Sanskrit has a homonymous √dhāv- 'to wash, cleanse' (the source of Avestan frā-dav- 'to rub clean'), which Walde-Pokorny expressly keeps apart from this root ('Verschieden ist ai. dhāvati „reinigt, macht blank“'); Nourai's box, glossed 'to run', takes the right one.\",\n     \"derivation_fa\": \"سنسکریت √dhāv-/dhav- «دویدن، روان شدن» (سومْ‌شخصِ مفردِ dhávate «می‌دود، روان می‌شود»، با درجهٔ کشیده dhāvati؛ مشتقِ dhāutí- «چشمه، جویبار»)، گواهی‌شده از ریگ‌ودا. این صورت واکِ دمیدهٔ هندواروپایی را نگاه داشته است، حال آن‌که در شاخهٔ ایرانی dʰ به d بدل شده — و همین سنسکریت است که مِحَکِ درستیِ کلِ شاخهٔ ایرانی به شمار می‌رود. یک هشدار که در نمودار نیامده: در سنسکریت ریشهٔ هم‌آوایِ دیگری هست، √dhāv- «شستن، پاک کردن» (که همتای اوستایی‌اش frā-dav- «سترون ساییدن» است) و والده-پوکورنی صریحاً آن را از این ریشه جدا می‌کند؛ نورایی با معنای «دویدن» ریشهٔ درست را برگزیده است.\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\"ref\": \"POK:259\", \"status\": \"supports\",\n       \"note\": \"POK_01.txt line 3721: 'Ai. dhávate „rennt, rinnt“, dehnstufig dhāvati ds., dhāuti-ḥ f. „Quelle, Bach“' — the first witness Pokorny cites for the root.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"WLD\", \"where\": \"Bd. I 834 (WLD_Bd1_1930 djvu lines 52568, 52588)\", \"stance\": \"supports\",\n       \"note\": \"'Ai. dhavate „rennt, rinnt“, dehnstufig dhavati ds., dhauti- „Quelle, Bach“ …' and, at the end of the entry, 'Verschieden ist ai. dhāvati „reinigt, macht blank“ usw.' — the homonym warning.\"},\n      {\"src\": \"SYN\", \"where\": \"Buck 10.46 RUN (SYN.txt line 17472 ff.)\", \"stance\": \"supports\",\n       \"note\": \"Buck's row for 'run' reads 'Skt. dhāv-, dru-, drā-', and his commentary equates 'Grk. θέω, with θοός „swift“ : Skt. dhāv-'.\"},\n      {\"src\": \"IEC\", \"where\": \"Mann, IEC s.v. dheu- (1) (IEC.txt line 2872)\", \"stance\": \"supports\",\n       \"note\": \"'dheu- (1) „flow“ … Skt. dhávate, 3s.; Gk. théo, théwo „run, scud“; Gallo-Brit. Deva (n. of River Dee) …'\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"Germanic\", \"words\": \"dauwaz\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Proto-Germanic *dawwaz 'dew' (OE dēaw, OS dau, OFris. daw, MDu. dau, OHG tou, German Tau, ON dǫgg gen. dǫggvar) is the o-grade noun *dʰow-o- of this root, 'that which runs/flows (down)' — semantically the same nominalisation as Skt. dhāutí- 'spring, brook' beside dhávate. The Germanic geminate -ww- reflects the sequence *-w-w- of *dawwa- (Verschärfung is absent here; ON dǫggvar preserves the -w- of the stem). Watkins puts it under dheu-2 with exactly Nourai's reconstruction, *dauwaz.\",\n     \"derivation_fa\": \"ژرمنی آغازین *dawwaz «شبنم» (انگلیسی کهن dēaw، ساکسونی کهن dau، آلمانی بالای کهن tou و آلمانی Tau، نورس کهن dǫgg با حالتِ اضافیِ dǫggvar) اسمی است با درجهٔ o از همین ریشه، *dʰow-o-، به معنای «آنچه فرو می‌ریزد و روان می‌شود» — همان‌گونه که در سنسکریت dhāutí- «چشمه، جویبار» در کنارِ dhávate ساخته شده است. جفتیِ -ww- بازتابِ ساختِ *dawwa- است که در نورس کهن dǫggvar هنوز پیدا است. واتکینز نیز آن را ذیل dheu-² و با همان بازساختِ *dauwaz می‌آورد که نورایی نوشته است. ادعای نورایی درست است.\",\n     \"sources\": [E_DEW],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"Watkins 1985: 'dheu-2. To flow. Germanic *dauwaz, dew, in: a. Old English dēaw, dew: DEW; b. compound *melith-dauwaz, „honeydew“ (see melit-). [Pok. 1. dheu- 259.]' — the node copies Watkins' *dauwaz letter for letter.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"IEW 259-260 (POK_01.txt line 3726)\", \"stance\": \"supports\",\n       \"note\": \"'anord. dǫgg, Gen. dǫgguar (*dawwō), ags. dēaw, as. dau, ahd. tou n. „Tau“ (*dawwa-)' — listed inside the dheu-1 entry, i.e. exactly the root→Germanic arrow.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. I 834\", \"stance\": \"supports\",\n       \"note\": \"'anord. dǫgg, gen. dǫgguar (*dawwō), ags. deaw, as. dau, ahd. tou, nhd. Tau (*dawwa-)'.\"},\n      {\"src\": \"IEC\", \"where\": \"Mann, IEC s.v. dhouos (IEC.txt line 3045)\", \"stance\": \"supports\",\n       \"note\": \"'dhouos (dhouuo-) „running, flowing; run, flow, course“ … OHG tou; Du. dauw; LG dau; OE dēaw „dew“ … ON dǫgg „dew“' — Mann reconstructs the same o-grade noun that underlies *dawwaz.\"}\n     ]\n    },\n    {\n     \"id\": 6, \"lang\": \"English\", \"words\": \"dew\", \"verdict\": \"confirmed\",\n     \"derivation\": \"OE dēaw > ME deaw/deu > NE dew, with the regular monophthongisation of OE ēa and the loss of final -w in spelling; the OE verb dēawian 'to bedew' is attested beside it, and the compound mildēaw 'honeydew' (later mildew) shows the same noun. Etymonline gives the whole chain and attaches it, 'perhaps', to 'PIE root *dheu- „to flow“ (source also of Sanskrit dhavate „flows, runs“)'; Skeat likewise: 'Perhaps allied to Skt. dhāv, to run'. The English word itself is beyond doubt; the hedges concern the PIE attachment, which is node 5's business.\",\n     \"derivation_fa\": \"انگلیسی کهن dēaw > انگلیسی میانه deaw/deu > انگلیسی نو dew؛ دوواکهٔ ēa در انگلیسی کهن به واکهٔ ساده بدل شده و -w پایانی در املا افتاده است. در انگلیسی کهن فعلِ dēawian «شبنم‌زدن» و ترکیبِ mildēaw «شهدِ گیاهی» (بعدها mildew) نیز از همین اسم ساخته شده‌اند. اتیمولاین همین زنجیره را می‌دهد و آن را «شاید» به ریشهٔ هندواروپاییِ *dʰeu- «روان شدن، هم‌ریشه با سنسکریت dhavate» می‌بندد؛ اسکیت هم می‌نویسد «شاید هم‌ریشه با √dhāv سنسکریت به معنی دویدن». خودِ واژهٔ انگلیسی هیچ تردیدی ندارد و احتیاطِ مأخذها به پیوندِ هندواروپایی مربوط است که کارِ گرهِ پیشین است. ادعای نورایی درست است.\",\n     \"sources\": [E_DEW],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\",\n       \"note\": \"No reference on the node; it inherits the parent's AHD, whose dheu-2 entry ends 'Old English dēaw, dew: DEW'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict. s.v. Dew (SKT.txt line 4987)\", \"stance\": \"supports\",\n       \"note\": \"'Dew (E.) ME. deu, dew. AS. dēdw, dew. + Du. dauw, Icel. dögg (gen. döggvar), Dan. dug, Swed. dagg, G. thau. Perhaps allied to Skt. dhāv, to run, or dhāv, to wash.'\"},\n      {\"src\": \"WEB\", \"where\": \"Etymonline s.v. dew (archived)\", \"stance\": \"supports\",\n       \"note\": \"'Middle English deaw, deu, from Old English deaw, from Proto-Germanic *dawwaz (source also of Old Saxon dau … Old Norse dögg „dew“), perhaps from PIE root *dheu- „to flow“ (source also of Sanskrit dhavate „flows, runs“).'\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-129.json','w',encoding='utf-8') as f:\n    json.dump(doc, f, ensure_ascii=False, indent=1)\n    f.write('\\n')\nprint('written')\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk129.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-129.json > /dev/null && echo \"JSON OK\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 129"
}
```


### [2026-09-05T20:20:43.363Z] TOOL RESULT

```
written
JSON OK
nodes verified: 14/14
node verdicts: {'plausible': 5, 'confirmed': 9}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 10, 'not_checked': 5, 'partial': 1}
books consulted: {'partial': 6, 'silent': 4, 'supports': 29, 'contradicts': 3} | by book: {'WEB': 7, 'WLD': 5, 'KLN': 5, 'POK': 3, 'MON': 3, 'IEC': 3, 'BRT': 2, 'BQT': 2, 'ARY': 2, 'CHEUNG': 2, 'SYN': 2, 'AHD': 1, 'KNT': 1, 'PHD': 1, 'NYB': 1, 'HRN': 1, 'SKT': 1}
```


## [2026-09-05T20:21:08.160Z] AGENT

Done. `verify_check.py 129` reports **0 PROBLEM lines** (14/14 nodes, 2 roots).

**Page 129 (book p. 99) — verdicts**
- Roots: 2 confirmed (Dher 2 = Pokorny IEW 251 `1. dher-`; Dheu 1 = IEW 259 `1. dheu- "laufen, rinnen"`). The two redirect entries (Dherabh, Dhers) were skipped as instructed.
- Nodes: 9 confirmed, 5 plausible, 0 disputed, 0 transcription_suspect, 0 unverified.
- Ref checks: 10 supports, 1 partial, 5 not_checked (all of them empty/reference-less boxes that inherit the parent's AHD citation).

**Plausible (not confirmed), one line each**
- Dher 2 #1 Av. *driwi* "dark birth mark": the word is real (Bartholomae, AiW: 'Flecken, Mal', esp. 'Muttermal'), but Pokorny 252 prints it "Unsicher", Walde-Pokorny I 855 poses it as a question after Charpentier, Bartholomae writes only "Et.?" — and no source calls the mark *dark*.
- Dher 2 #2 Gmc *derk* "dark": Pokorny 252 (b. dherg-) and Watkins support it verbatim, but PGmc *derkaz is "of uncertain etymology" for modern Germanicists.
- Dher 2 #4 Gk *traxus*: Pokorny/Watkins put τραχύς under this root (Watkins even lists TRACHEA, TRACHOMA, TRACHYTE there), but Beekes discounts the link to dark/dregs and Wiktionary reconstructs a separate *dʰreh₂gʰ- "to irritate".
- Dher 2 #5 "[Latin]": the link is Modern/Medical Latin *trachōma* (c. 1690), not a Classical Latin word — the bare "Latin" box hides that.
- Dheu 1 #1 "Avestan / Old Persian daw": **the one substantive error on the page.** Old Iranian *dau- is real, but it is attested in neither Avestan nor Old Persian — Cheung's *dau² has an empty Avestan section, Bartholomae's four Avestan dav- roots mean 'speak (daevic) / drive away / rub clean / press', Kent has no dav-, Buck gives Av. taē-, dru- for 'run', and Nourai's own source (Abolghasemi FFD:54) says only «ایرانی باستان *dav-». Wrong language label, right derivation.

**Notable positives:** Pokorny 259 itself prints "mpers. davīdan", and Moʿin's footnote at Borhān p.902 (leaf 362, offset printed = leaf + 540) cites «اشتقاق ۵۸۵» = Horn no. 585, Nourai's other citation on that node — both of his refs check out exactly; Dehkhoda confirms تراخم «از فرانسوی», and fr.wiktionary dates French *trachome* to 1752.

**Extraction errors for the owner: none.** The JSON matches the chart faithfully; no printed-page image was needed since nothing was flagged transcription_suspect.

Archived web sources (via `fetch_source.py`): Wiktionary دویدن and τραχύς, Etymonline trachoma/dark/dew, fr.wiktionary trachome, abadis.ir تراخم. (cnrtl.fr/etymologie/trachome returned an empty JS shell and is not cited.)
