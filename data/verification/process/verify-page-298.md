# Verification process log — verify-page-298


## [2026-09-06T22:34:19.214Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 298 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-298.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-298.json. Write /home/sfmqrb/git/rishe/data/verification/page-298.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 298` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T22:34:20.804Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T22:34:21.522Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T22:34:21.537Z] TOOL RESULT

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


## [2026-09-06T22:34:21.729Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-298.txt"
}
```


### [2026-09-06T22:34:21.741Z] TOOL RESULT

```
1	=== PDF page 298 (book page 268) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Kwon, Ka 2, Sua : dog  (refs POK:632; KLN:746; BQT:1155)
4	#1 (parent #0) [Avestan / Old Persian] refs=POK:632; KLN:746 | spâ 1, sŭnô : dog ; spakâ : dog
5	  #2 (parent #1) [Pahlavi] refs=HRN:164 | sak : dog
6	    #3 (parent #2) [Persian] refs=BQT:1155 | sag «سگ» : dog
7	  #4 (parent #1) [Avestan] refs=POK:632; FIB:207 | spâda, spâtha : army ; spatha-paiti : army protector (leader) ☞Per 3 ; Aspadâna : city of the army (Isfahan)
8	    #5 (parent #4) [Persian] refs=BQT:118,1087; HRN:155; POK:632 | sepâh «سپاه (سپه)» : army ; sepahbod «سپهبد (سپهسالار)» : Lieutenant-general ; Esfahân «اصفهان» : Name of a city in central Iran
9	    #6 (parent #4) [Sogdian] refs=SOD:94 | sp`d, `spd : army
10	  #7 (parent #1) [Old Persian] refs=KNT:210 | spâda : army
11	    #8 (parent #7) [None] refs=None | 
12	#9 (parent #0) [Old Persian] refs=KNT:209 | sakâ 2 : dog
13	  #10 (parent #9) [None] refs=None | 
14	#11 (parent #0) [Germanic] refs=AHD | hundaz : dog
15	  #12 (parent #11) [English] refs=None | hound
16	#13 (parent #0) [Latin] refs=KLN:746 | canis : dog ; insula canaria : dog island, named after its large dogs
17	  #14 (parent #13) [English] refs=None | kennel ; Canary Islands
18	  #15 (parent #13) [Spanish] refs=KLN:230 | canario : from Canary Islands < a bird >
19	    #16 (parent #15) [French] refs=None | canari : canary bird
20	      #17 (parent #16) [Persian] refs=MON:2730 | qanârî «قناری» : canary
21	      #18 (parent #16) [English] refs=AHD | canary
22	
```


## [2026-09-06T22:34:26.130Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-298.json && echo \"=== refs_online keys ===\" && python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','BQT','HRN','FIB','SOD','KNT','MON','AHD','PHD','NYB','BRT','HUB','WLD','IEC','SYN','SKT','FSD','WEB','ARY','CHEUNG','LKT']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:400])\n\""
}
```


### [2026-09-06T22:34:28.155Z] TOOL RESULT

```
{
  "pdf_page": 298,
  "book_page": 268,
  "entries": [
    {
      "root": {
        "name": "Kwon, Ka 2, Sua",
        "lang": "Indo-European",
        "refs": "POK:632; KLN:746; BQT:1155",
        "gloss": "dog"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "POK:632; KLN:746",
          "words": [
            {"translit": "spâ 1, sŭnô", "gloss": "dog", "script": null},
            {"translit": "spakâ", "gloss": "dog", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "HRN:164",
          "words": [
            {"translit": "sak", "gloss": "dog", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:1155",
          "words": [
            {"translit": "sag", "gloss": "dog", "script": "سگ"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 1,
          "lang": "Avestan",
          "refs": "POK:632; FIB:207",
          "words": [
            {"translit": "spâda, spâtha", "gloss": "army", "script": null},
            {"translit": "spatha-paiti", "gloss": "army protector (leader)", "script": null, "see": ["Per 3"]},
            {"translit": "Aspadâna", "gloss": "city of the army (Isfahan)", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "BQT:118,1087; HRN:155; POK:632",
          "words": [
            {"translit": "sepâh", "gloss": "army", "script": "سپاه (سپه)"},
            {"translit": "sepahbod", "gloss": "Lieutenant-general", "script": "سپهبد (سپهسالار)"},
            {"translit": "Esfahân", "gloss": "Name of a city in central Iran", "script": "اصفهان"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 4,
          "lang": "Sogdian",
          "refs": "SOD:94",
          "words": [
            {"translit": "sp`d, `spd", "gloss": "army", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 1,
          "lang": "Old Persian",
          "refs": "KNT:210",
          "words": [
            {"translit": "spâda", "gloss": "army", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": null,
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "KNT:209",
          "words": [
            {"translit": "sakâ 2", "gloss": "dog", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": null,
          "refs": null,
          "words": [],
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
            {"translit": "hundaz", "gloss": "dog", "script": null}
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
            {"translit": "hound", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 0,
          "lang": "Latin",
          "refs": "KLN:746",
          "words": [
            {"translit": "canis", "gloss": "dog", "script": null},
            {"translit": "insula canaria", "gloss": "dog island, named after its large dogs", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 13,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "kennel", "gloss": null, "script": null},
            {"translit": "Canary Islands", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 13,
          "lang": "Spanish",
          "refs": "KLN:230",
          "words": [
            {"translit": "canario", "gloss": "from Canary Islands < a bird >", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 16,
          "parent": 15,
          "lang": "French",
          "refs": null,
          "words": [
            {"translit": "canari", "gloss": "canary bird", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 17,
          "parent": 16,
          "lang": "Persian",
          "refs": "MON:2730",
          "words": [
            {"translit": "qanârî", "gloss": "canary", "script": "قناری"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 18,
          "parent": 16,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "canary", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
=== refs_online keys ===
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
FIB {"title": "Ebrahim Pur-Davud, Farhang-e Iran-e Bastan, vol. I, Tehran University Press 1326/1947", "kind": "website", "url": "https://noorlib.ir/book/info/104334 (viewer: https://noorlib.ir/book/view/104334?pageNumber=<N>&viewType=pdf) ; PDFs also offered at kashanketab.com / kaffeketab.ir (62 MB)", "lookup_hint": "Not on archive.org; browser needed for noorlib.", "local_file": null, "page_offset"
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in 
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
CHEUNG null
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 =
```


## [2026-09-06T22:34:33.065Z] TOOL CALL #4: Bash

```json
{
 "command": "ls data/verification/sources/refs/ && echo \"---MATRIX---\" && sed -n 1,120p data/verification/sources/SOURCE_MATRIX.md && echo \"---offsets---\" && python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','BQT','HRN','SOD','KNT','MON','AHD','PHD','NYB','BRT','HUB','WLD','IEC','SYN','SKT','FSD','WEB','ARY','LKT','FIB']:\n    v=d.get(k) or {}\n    print(k,'|',v.get('local_file'),'|',v.get('page_offset'))\n\""
}
```


### [2026-09-06T22:34:35.116Z] TOOL RESULT

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
SKT.txt
SNS_pages.txt
SNS.txt
SOD_pages.txt
SOD.txt
SPG_keilinschriften1881.txt
SYN.txt
TAD_pages.txt
TAD.txt
tessdata
TLM.txt
UNV.txt
WEB_vol1.txt
WLD_band3.txt
ZAP.txt
---MATRIX---
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
---offsets---
POK | /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt | POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
KLN | /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt | KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
BQT | ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'] | vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
HRN | /home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt | leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
SOD | ['/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD.txt'] | printed page ≈ leaf − 66 in SOD_pages.txt (0-based \f blocks; 645 leaves; English intro precedes)
KNT | /home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt | leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
MON | ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'] | None
AHD | /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt | 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.
PHD | /home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt | leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
NYB | /home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt | Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
BRT | /home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt | Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
HUB | /home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt | leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
WLD | ['/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt'] | Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696).
IEC | /home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt | TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
SYN | /home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt | leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
SKT | /home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt | leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
FSD | /home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt | vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably detected (pages ~ 700-1640) - grep the headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
WEB | /home/sfmqrb/git/rishe/data/verification/sources/refs/WEB_vol1.txt | not reliably detected (page_numbers.json sparse); grep headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
ARY | ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt'] | printed page = pdf page + 1
LKT | /home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt | leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
FIB | None | None
```


## [2026-09-06T22:34:39.994Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK leaf for p632: POK_02 leaf = 632-344 = 288 ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==289' POK_02.txt | head -60"
}
```


## [2026-09-06T22:34:41.593Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN 1966 leaf for p746: floor(746/2)+12 = 385 ===\"\nawk 'BEGIN{RS=\"\\f\"} NR>=384 && NR<=387' KLN_1966.txt | grep -n -i -A6 -B2 'kennel\\|canis\\|hound' | head -80"
}
```


### [2026-09-06T22:34:41.605Z] TOOL RESULT

```
=== POK leaf for p632: POK_02 leaf = 632-344 = 288 ===
ünire  ,stercus  facere',  ancunulenta^ ,feminae  menstruo  tempore' ;
schwed.  dial.  Iven  ,sumpfiges  Feld',  aisl.  hvein  (*kuoinä)  in  Ortsnamen, wozu  als  ,Sumpfgras'  wohl  dän.  hvene  ,agrostis,  Gattungsname  für  mehrere steife  Grasarten',  schwed.  Jiven^  norw.  dial.  hvein  ,agrostis,  dünner  Gras- halm' (mengl.  whin  , Ginster'  aus  dän.  hvine)-,
lett.  svlmt  refl.  ,sich  schmutzig  machen',  svlns  ,beschmutzt' ;
mit  andern  Formantien  vermutlich  arm.  siv  ,Bodensatz  gepreßter  Trauben, (kift-uo-)]  viel  unsicherer  ags.  hwceg^  mndl.  ivey  ,Molken'  (*kuoio-?).
WP.  I  469,  WH.  I  131  f.
2.  kuei'  in  Schallworten  für  ,zischen,  pfeifen'  u.  dgl.  (s.  ähnliches  unter  kue$-
jkeuchen').
Nisl.  hvia  ,wiehern',  schwed.  dial.  hwija  ,laut  oder  heftig  schreien', mhd.  mihe-n-  -nen,  -len,  -ren  ,wiehern',  ahd.  hwaijön,  waijön,  mhd.  weihen ^wiehern';-  dazu  als  Kausativ  ,weinen  machen' :  ags.  ä-hwöenan  ,plagen, quälen',  aschwed.  hwin  ,Belästigung' ;
aisl.  hvina  ,sausen',  hvinr  , schwirrender  Ton',  ags.  hwlnan  ,sausen*, hwinsian^  ahd.  winisön  ,jammern',  nhd.  winseln-^  aisl.  hvlskra  ,flüstem*, hvlsla  ,pfeifen,  flüstern',  ags.  hwiscettan  , pfeifen,  von  der  Maus',  hwistlian ,pfeifen',  hwisprian  ,murmeln',  ahd.  (h)wispalön  ,zischen,  wispern',  aksl. svistati  ,zischen'.
kuei-k-  in  arm.  scem  ,zische'  {*§icem  aus  *kutkio)  und  lit.  svyksti  ,pfeifend atmen'.
WP.  I  469.
5.  kuei-,  erweitert  kuei-d-,  kuei-s-,  kuei-t-  , leuchten;    hell,  weiß';   wohl Erweiterung  von  heu-,  S.  594  f. a.  kuei-d-:  ai.  svindate  ,glänzt'  (Dhätup.),  Perf.  sisvinde-,  gr.  Bergname nivöog  ,der  Weiße',  PN  J7tV(Ja^og(?);  got.  hveits,  aisl.  hvitr,  ags.  afries.  asächs.
629
7  ahd.  (h)toiz  ,weiß*,  schwundstufig-  nid.  ndd.  witt,  afries.  hivit  ds. ; r  g^  o-ot.  hveiteis,  aisl.  hweiti  n.,  ags.  hioxte^  afries.  asächs.  hwEti^  ahd. t  .^^j-'^^jid.  ,prei2;e7i';  ablautend  mengl.  lohite,  schwed.  dial.  hvitej  westfäl. ^<  .Weizen.
,     ^yg/_5-  lit.  §viesä  f.  , Licht',  svaisä  f.  , Lichtschein'.
c.  kuei-t-   (kuei-to-,   kuei-tio-,   kui-t^^^no-,   kui-t^s)ro-   ,hell,  weiß'):
lu.  5ütJ^a-  ,weiß'  (f.  s'yem  hei  Vopadeva)  ==  av.  spaeta-  ds.  (=  ahg.  sv^i^ Licht');  ai.  ivetya-  ,weiß,  licht',  fem.  -ä  (=  abg.  svSSta  , Licht'),  ai.  ivetate l-  'ist  ~^^eißS  svitna-j  svitnyä-,  svitrd-  (==  lit.  sviträs  , Glaspapier^)  ,weiß', apers.  ^jtL&ga-daxrjg,  npers.  sipihr  , Himmel';  Kompositionsform  ar.  sviti- in  ai.  ivi
```


### [2026-09-06T22:34:43.310Z] TOOL RESULT

```
=== KLN 1966 leaf for p746: floor(746/2)+12 = 385 ===
170-intr.  v.,  to  adopt  the  Greek  speech,  customs, etc.  —  Gk.  'EXXvjvl^eiv,  ‘to  speak  Greek,  make Greek,  Hellenize’,  fr.  "EXXvjvei;,  ‘Greeks’.  See Hellen  and  -ize.
171-Derivatives:  Helleniz-ation,  n.,  Hetleniz-er,  n. Helleno-,  combining  form  meaning  ‘Greek-’.  — 'EXXvjvo-,  fr.  "EXXvjve;,  ‘Greeks’.  See  Hellen. heller,  n.,  name  of  a  small  coin  formerly  current in  Germany  and  Austria.  —  G.  Heller,  fr. MHG.  halier,  heller,  short  for  Haller  pfenninc, i.e.  ‘pfennig  coined  at  Hall  (in  Swabia)’.  For sense  development  cp.  dollar.  For  the  ending see  agential  suff.  -er.
172:hellhound,  n.,  1)  a  dog  of  hell,  such  as  Cerberus; 2)  a  demon.  —  ME.  hellehund,  fr.  OE.  helle hand,  lit.  ‘hound  of  hell’.  See  hell  and  hound, hello,  interj.  —  A  var.  of  hallo, helm,  n.,  tiller;  steering  wheel  of  a  vessel.  —  ME. helme,  fr.  OE.  helma,  ‘rudder’,  rel.  to  OHG. helmo,  ‘tiller’,  MHG.  halm(e),  helm,  G.  Helm, ‘handle  of  an  ax,  helve’,  and  to  E.  helve  and halter  (qq.v.)
173-helm,  n.,  helmet  (poet.)  —  ME.,  fr.  OE.  helm.  See helmet.  Derivative:  helm-ed,  adj. helmet,  n.  —  OF.,  dimin.  of  helme  (F.  heaume), ‘helmet’,  fr.  Frankish  *helm,  which  is  rel.  to OHG.,  MHG.,  G.,  OFris.,  OS.,  OE.  helm,  ON. hjalmr,  Goth,  hilms.  These  words  prob.  meant orig.  ‘cover,  protection’,  and  derive  fr.  I.-E. base  *kel-,  ‘to  cover,  hide,  conceal’,  whence  also OE.  helan,  etc.,  ‘to  conceal’.  See  hall  and  cp. the  second  element  in  Anselm,  Kenelm,  Wil¬ liam.  Cp.  also  It.  c/mo,  OProveng.  elm,  Sp. yelmo,  ‘helmet’,  which  also  are  Teut.  loan  words. Derivative:  helmet-ed,  adj. helminth,  n.,  a  parasitic  worm.  —  Gk.
174-(later  form  £X|uvq),  gen.  eXptvllog,  for  *rirw.'jc, lit.  ‘that  which  rolls  or  twists’,  rel.  to  iXlaaetv (for  *FeX1xieiv),  ‘to  wind,  roll’,  eXi£  (for  *feXi5), ‘spiral’.  See  helix  and  cp.  the  second  element in  nemathelminth.  Derivative:  helminth-ic,  adj. helminth-,  form  of  helmintho-  before  a  vowel, helminthiasis,  n.,  a  disease  caused  by  the  pre¬ sence  of  parasitic  worms  in  the  body  (med.)  — Medical  L.,  fr.  Gk.  F/.pivfUav,  ‘to  suffer  from worms’,  fr.  eXjju?,  gen.  JXptv&o;.  See  helminth and  -iasis.
175-helmintho-,  before  a  vowel  helminth-,  combining form  meaning  ‘worm’  (med.)  —  Gk.  eXpiv&o-, eXpivit-,  fr.  eXpup,  gen.  sXp.!.v&oc,  ‘worm’.  See
176-helminth.
177-helminthology,  n.,  the  study  of  worms  (esp.  of parasitic  worms).  —  Compounded  of  hel¬ mintho-  and  Gk.  -Xoywc,  fr.  -Xoyoc,  ‘one  who speaks  (in  a  certain  manner);  one  who  deals (with  a  certain  topic)’.  See  -logy, belmless,  adj.,  having  no  helm  (said  of  a  vessel). —  See  helm,  ‘tiller’,  and  -less, helmless,  adj.,  having  no  helmet.  —  See  helmet and  -less.
178-helo-,  combining  form  meaning  ‘marsh’.  —  Gk. &X o-,  fr.  £Xoc,  ‘marsh’.  See  Helenium.
```


## [2026-09-06T22:34:50.107Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK kuon ===\"\ngrep -n \"Hund'\" POK_02.txt | head -20\necho \"--- find leaf ---\"\nawk 'BEGIN{RS=\"\\f\"} /kuon-/ && /Hund/ {print \"LEAF \" NR-1; print substr($0,1,1500)}' POK_02.txt | head -60"
}
```


## [2026-09-06T22:34:51.261Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN hound entry ===\"\ngrep -n \"hound,  n\" KLN_1966.txt | head\ngrep -n \"^hound\" KLN_1966.txt | head\ngrep -n \"hound\" KLN_1966.txt | grep -i \"OE.  hund\\|OE\\. hund\" | head"
}
```


### [2026-09-06T22:34:51.715Z] TOOL RESULT

```
=== POK kuon ===
1425:ags.  gierran  st.  V.  , tönen,  knarren,  schwatzen',  nhd.  gU-ren  (mhd.  auch garren,  gurren),  schwed.  norw.  garpa  ,lärmen,  prahlen',  aisl.  garpr  , uner- schrockener streitbarer  Mensch';  norw.  dial.  garta  , spaßen,  plaudern, grunzen';  ags.  gierman,  norw.  garma  , brüllen',  anord.  garmr  .Hund'; weiters  ags.  gryllan  ,knirschen,  wüten',  mhd.  grellen  st.  V.  , durchdringend, vor  Zorn  schreien',  grel  ,rauh,  grell,  zornig',  ndl.  grollen  , murren,  zornig sein',  mhd.  grüllen  ,höhnen',  nhd.  grollen-^
3201:ablautendes  sk-J-  vielleicht  in  gr.  crxvAaf  ^j^i^^er  Hund,  Hund;  junges Tier',  auch  y,vXla'  a-Ma^.  ""HUtoi  Hes.  (-U-  wohl  kurznamenartige  Kons.- Dehnung),  wie  von  *skel-  das  oben  genannte  lit.  skalikas,  und  von  kel- aus :  lit.  käle,  kall  ,Hündin',  alb.  kelüsh  ,Tierjunges,  bes.  junger  Hund', mir.  cuilen,  cymr.  colwyn,  acorn.  coloin,  bret.  kolen  ,junger  Hund'  (kelt. *koli-gno-) ',  diese  Namen  für  junge  Tiere,  bes.  Hunde,  wären  also  vom Kläffen  oder  Winseln  genommen.  Immerhin  aber  könnten  ov,vXa^y  xvHa als  (s)kol-,  auch  als  idg.  oder  griech.  Reduktionsformen  (Einfluß  von  xvwy?) unmittelbar  mit  kelt.  *koligno-,  lit.  käle,  alb.  kelüsh  zusammengehören.
4640:kuon-,  kun-  ,Hund';  ursprüngl.  Nom.  Sg.  küuo{n),  Gen.  kunös,
4641:Ai.  svä  und  s{u)vä  ,Hund',  Gen.  mnas,  Akk.  svänam,  Akk.  PI.  sünas] av,  spä,  spändm,  Gen.  PI.  sünam,  med.  (Herodot)  a/raxa  {*kun-ko-  ,hunde- artig'  :  ai.  svaka-  ,Wolf'),  mpers.  sak,  npers.  sag,  kurd.  sah,  wä'/i  sa6] aus  dem  Iran,  stammen  alb.  shak{;e)  ,Hündin',  gr.  anddayisg'  yivveg  Hes. (aus  *07tdAad£g)  und  russ.  sohdka  ,Hund';  vgl.  npers  salah]
4642:arm.  sww.  Gen.  san  ,Hund' Jmit  unklarem  i);  nicht  gut  vereinbar  mit skund  ,Hündchen',  falls  aus  *kuon-to-,  -tä-,  oder  zu  den  oben  S.  564  unter *ken-    ,frisch    hervorkommen'    besprochenen    Tierjungenbezeichnungen?;
4646:o-anz  unklar  lat.  canis  ,Hund',  cänes  ursprüngl.  altes  fem.  , Hündin', canlcula  (vgl.  ai.  §unl  f.)  hinsichtlich  des  a;  vielleicht  Einmischung  eines dem  mir-  cano,  cana  ,Wolfsjunges',  cymr.  cenaw  ,junger  Hund  oder  Wolf' /g.  3.  Icen-)  entsprechenden  Wortes  (so  auch  1yd.  Kav-da^ölrig'^);
4648:got.  hunds,   aisl.  hundr^   ags.  hund,  ahd.  hunt  ,Hund'  (kun-tö-),  s.  oben ;
4649:lit.  §uö  (Gen.  sufis)  ,Hund*  (zum  i-St.  geworden  in  lit.  dial.  sunis,  lett.  suns, apr.  sunis  ,Hund*) ;  ^Form  lett.  suntana  ,großer  Hund' ;  lett.  kuna  ,Hündin' wohl  mit  westidg.  Gutt.,  Trautmann  Bsl.  Wb.  310?  oder  das  Ä  von  kuca ds.  (Lockruf);  vgl.  Büga  Kalba  ir  s.  I  196;  ganz  fraglich  aber  russ. poln.  suka  , Hündin';
4934:ahd.  laffan  (luof)  ,lecken',  ahd.  leffil  ,Lö£fel',  mnd.  lepel  ds.  (:  got. *lapins,  woraus  apr.  iapinis  entlehnt) ;  ags.  lapian  , trinken,  schlürfen', aschwed.  lapa  ds.  {^lapön),  nisl.  norw.  lepja  , schlürfend  lecken  wie  ein Hund'  =  mhd.  leffen  ,lecken,  schlürfen',  shd.  gilepfen  ds.;  Intensiv,  mhd. nhd.  läppen  ds.  verhält  sich  zu  schlappen  wie  lecken  zu  schlecken-,
--- find leaf ---
LEAF 292
tvqov  ,Kleie'  trotz  des  noch  unklaren  l  nicht  zu  trennen  ist*  "^
da  aus  ,schütteln'  auch  ,ausschütteln,  streuen'  entwickelt  sein  kann,  igt mit  quatiö  möglicherweise  identisch  gr.  naaow^  att.  Tt&TTio  {Ttaoo)^  STtaaa iftda^Tjv)  ,streue,  besprenge'  (in   der  Webersprache  ,webe  bunte  Figuren  ' ein',  daher  xQmortaaiog  ,goldgestickt',  naoroQ  m. , Brautkammer,  Brautbett')  »t^ freilich  ist  ndaaco  zunächst  mit   dor.  TcfjV'  Ttfj  y,al  jtfjv  ertl  rov  ycardnaaat yial  -^axafcäaGuv  Hes.,  epidaur.  irtLTtfjv  (pdQy,av,ov  zu  verbinden;
ags.   hüdenian   , schütteln',   mhd.    hotzen   , laufen,   schaukeln*,   nisl.    hossa  " jSchütteln,  schleudern';  über  Formen  mit  s-  s.  unter  (s)küt-  ,rütteln*;        tf"
lit.  kutinetis  ,sich  zurechtzupfen'  (von  Vögeln),  kuntü,  atkutäu,  küsti  ,sich  '-- erholen'  (*aufrütteln).
WP.  I  511,  II  601,  WH.  II  399  f.
kuoi-,  kui-  ,wollen,  einladen'.
Ai.  keta-  m.  ,Wille,  Begierde,  Absicht,  Aufforderung,  Einladung',  ketana- n.  , Aufforderung,  Einladung';
gr.  'Aolxai'  yvvaLxcüv  irtLdvfxiaLi?)  Hes.,  zweifelhaft  auch  xtWa,  att.  xtTra (*xma)  ,krankhaftes  Gelüst  schwangerer  Frauen';
apr.  quäits  ,Wille',  quoi  ,er  will',  quoitU  ,wollen',  lit.  kvieciii,  kviesti ,einladen'.
WP.  I  475  f.,  WH.  I  714,  Trautmann  146  f.
kuon-,  kun-  ,Hund';  ursprüngl.  Nom.  Sg.  küuo{n),  Gen.  kunös,
Ai.  svä  und  s{u)vä  ,Hund',  Gen
```


### [2026-09-06T22:34:51.786Z] TOOL RESULT

```
=== KLN hound entry ===
16672:greyhound,  n.,  a  tall  and  slender  dog.  —  ME. grihond,  grehund,  grehounde,  fr.  OE.  grighund, rel.  to  ON.  greyhundr,  fr.  grey,  ‘dog’, and  hundre, ‘hound’  (see  hound).  The  word  is  not  related to  grey.
17510:hellhound,  n.,  1)  a  dog  of  hell,  such  as  Cerberus; 2)  a  demon.  —  ME.  hellehund,  fr.  OE.  helle hand,  lit.  ‘hound  of  hell’.  See  hell  and  hound, hello,  interj.  —  A  var.  of  hallo, helm,  n.,  tiller;  steering  wheel  of  a  vessel.  —  ME. helme,  fr.  OE.  helma,  ‘rudder’,  rel.  to  OHG. helmo,  ‘tiller’,  MHG.  halm(e),  helm,  G.  Helm, ‘handle  of  an  ax,  helve’,  and  to  E.  helve  and halter  (qq.v.)
17895:hoarhound,  n.  —  See  horehound. hoarse,  adj.  —  ME.  hors,  fr.  earlier  has,  fr.  OE. has,  rel.  to  OS.  hes,  ON.  hdss,  Dan.  hies,  Swed, hes,  Du.  hees,  OHG.  heisi,  heis,  MHG.  heise, heiser,  earlier  G.  heisch,  G.  heiser,  ‘hoarse’. These  words  prob.  meant  orig.  ‘dried  out; rough’,  and  are  rel.  to  OE.  hat ,  etc.,  ‘hot’;  see hot.  The  insertion  of  the  r  in  ME.  hors  is  prob. due  to  the  influence  of  harsh.
18072:horehound,  also  hoarhound,  n.,  name  of  a  plant.
18145:hound,  n.,  dog.  —  ME.  hound,  hund,  ‘dog’,  fr. OE.  hund,  rel.  to  OS.,  Dan.,  Swed.,  OFris.,  G. hund,  ON.  hundr,  Du.  hond,  OHG.,  MHG.  hunt. Goth,  hunds.  These  words  derive  from  a  dental enlargement  of  I.-E.  base  *kwon-,  ‘dog’,  whence OI.  svan-,  Vedic  suvan-,  Avestic  spa  (gen.  sund), Medean  spdka  (whence  Russ,  sobdka),  Toch.  A ku,  ‘dog’,  Arm.  shun  (gen.  shan),  Gk.  xutav,  L. canis,  Lith.  Sud  (gen.  Sunis),  OIr.  cii  (gen.  con), W.  ci,  Bret.,  Co.  ki,  ‘dog’,  and  perh.  also  Russ. suka,  ‘bitch’.  Cp.  Gk.  arnkSaxeq  (Hesychius),
18147:hound,  n.,  projection  at  a  masthead  serving  to support  trestletrees,  etc.  (naut.)  —  ME.  hun, prob.  fr.  ON.  hunn,  ‘knob,  knob  at  the  mast- end;  bear’s  cub’,  which  is  prob.  cogn.  with OI.  sunah,  ‘swollen’,  L.  cavus,  ‘hollow,  concave’. See  cave,  n.
22575:Mahound,  n.,  1)  Mohammed,  the  founder  of  Is¬ lam  (arch.)-,  2)  the  devil  (Scot.)  —  OF.  Mahom, Mahon,  corruption  of  Mahomet,  ‘Mohammed’. Cp.  Mohammedan.
35534:Derivative:  sleuth,  intr.  v. sleuthhound,  n.,  bloodhound.  —  ME.,  fr.  sleuth, ‘track  of  a  person  or  animal’  (fr.  ON.  sldd),  and hound.  See  sleuth  and  hound  and  cp.  slot,  ‘track of  an  animal’.
18145:hound,  n.,  dog.  —  ME.  hound,  hund,  ‘dog’,  fr. OE.  hund,  rel.  to  OS.,  Dan.,  Swed.,  OFris.,  G. hund,  ON.  hundr,  Du.  hond,  OHG.,  MHG.  hunt. Goth,  hunds.  These  words  derive  from  a  dental enlargement  of  I.-E.  base  *kwon-,  ‘dog’,  whence OI.  svan-,  Vedic  suvan-,  Avestic  spa  (gen.  sund), Medean  spdka  (whence  Russ,  sobdka),  Toch.  A ku,  ‘dog’,  Arm.  shun  (gen.  shan),  Gk.  xutav,  L. canis,  Lith.  Sud  (gen.  Sunis),  OIr.  cii  (gen.  con), W.  ci,  Bret.,  Co.  ki,  ‘dog’,  and  perh.  also  Russ. suka,  ‘bitch’.  Cp.  Gk.  arnkSaxeq  (Hesychius),
18147:hound,  n.,  projection  at  a  masthead  serving  to support  trestletrees,  etc.  (naut.)  —  ME.  hun, prob.  fr.  ON.  hunn,  ‘knob,  knob  at  the  mast- end;  bear’s  cub’,  which  is  prob.  cogn.  with OI.  sunah,  ‘swollen’,  L.  cavus,  ‘hollow,  concave’. See  cave,  n.
18148:hounds-tongue,  n.,  name  of  a  plant.  —  OE.  hundes tunge.  See  hound,  ‘dog’,  and  tongue, hour,  n.  —  ME.,  fr.  OF.  ure,  ore,  hore  (F.  heure),  . fr.  L.  hora,  ‘hour’,  fr.  Gk.  copoc,  ‘any  limited time,  the  time  of  day,  hour,  season  spring,  year’, which  is  cogn.  with  Avestic  jar1,  ‘year’,  OSlav. jaru,  ‘spring’,  L.  hornus  (fr.  *hd-ydrinos),  ‘of  this year’,  Goth,  jer,  OE.  gear,  ‘year’.  See  year  and cp.  words  there  referred  to.  Cp.  also  Horae, horal,  horary,  the  first  element  in  horography, horologe,  horoscope,  and  the  second  element  in encore.
18145:hound,  n.,  dog.  —  ME.  hound,  hund,  ‘dog’,  fr. OE.  hund,  rel.  to  OS.,  Dan.,  Swed.,  OFris.,  G. hund,  ON.  hundr,  Du.  hond,  OHG.,  MHG.  hunt. Goth,  hunds.  These  words  derive  from  a  dental enlargement  of  I.-E.  base  *kwon-,  ‘dog’,  whence OI.  svan-,  Vedic  suvan-,  Avestic  spa  (gen.  sund), Medean  spdka  (whence  Russ,  sobdka),  Toch.  A ku,  ‘dog’,  Arm.  shun  (gen.  shan),  Gk.  xutav,  L. canis,  Lith.  Sud  (gen.  Sunis),  OIr.  cii  (gen.  con), W.  ci,  Bret.,  Co.  ki,  ‘dog’,  and  perh.  also  Russ. suka,  ‘bitch’.  Cp.  Gk.  arnkSaxeq  (Hesychius),
18148:hounds-tongue,  n.,  name  of  a  plant.  —  OE.  hundes tunge.  See  hound,  ‘dog’,  and  tongue, hour,  n.  —  ME.,  fr.  OF.  ure,  ore,  hore  (F.  heure),  . fr.  L.  hora,  ‘hour’,  fr.  Gk.  copoc,  ‘any  limited time,  the  time  of  day,  hour,  season  spring,  year’, which  is  cogn.  with  Avestic  jar1,  ‘year’,  OSlav. jaru,  ‘spring’,  L.  hornus  (fr.  *hd-ydrinos),  ‘of  this year’,  Goth,  jer,  OE.  gear,  ‘year’.  See  year  and cp.  words  there  referred  to.  Cp.  also  Horae, horal,  horary,  the  first  element  in  horography, horologe,  horoscope,  and  the  second  element  in encore.
```


## [2026-09-06T22:35:07.795Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('POK_02.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in (288,289,290,291,292,293):\n    l=leaves[i]\n    nums=re.findall(r'(?m)^\\s*(6[23]\\d)\\s*$', l)\n    print(i, 'pagenums:',nums, '| first80:', l.strip()[:80].replace('\\n',' '))\nEOF\necho \"=== KLN leaf of hound ===\"\npython3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i,l in enumerate(leaves):\n    if 'hound,  n.,  dog' in l:\n        print('leaf',i); print(l[:200])\n    if 'canary,  n' in l or 'Canary  Islands' in l or 'canari' in l:\n        print('CANARY leaf',i)\nEOF"
}
```


### [2026-09-06T22:35:09.676Z] TOOL RESULT

```
288 pagenums: ['629'] | first80: ünire  ,stercus  facere',  ancunulenta^ ,feminae  menstruo  tempore' ; schwed.  
289 pagenums: [] | first80: ty-anc  ,giänzend',  av.  spiti-doid-ra-  , helläugig' ; unsicher  gr.  rlravog 
290 pagenums: ['631'] | first80: laupan ,laufen',  us-hlaupan  ,aufspringenS  anord.  hlaupa  »springen,  laufen'
291 pagenums: ['632'] | first80: »sich  drehen*,  auch  kuerb-, Gr.  %aQ7t6g  »Handwurzel*  (Drehpunkt  der  Hand
292 pagenums: ['633'] | first80: tvqov  ,Kleie'  trotz  des  noch  unklaren  l  nicht  zu  trennen  ist*  "^ da  
293 pagenums: [] | first80: *  (zum  i-St.  geworden  in  lit.  dial.  sunis,  lett.  suns, apr.  sunis  ,Hu
=== KLN leaf of hound ===
CANARY leaf 132
leaf 401
r,  gen.  horiri, ‘to  urge,  incite,  encourage,  exhort’,  fr.  I.-E.  base *gher-,  ‘to  desire’,  whence  also  OE.  geornan, giernan,  ‘to  desire’.  See  yearn  and  -ation. hortative,  adj.,  p
```


## [2026-09-06T22:35:19.031Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in (131,132,133,400,401,402):\n    l=leaves[i]\n    print('=== leaf',i,'pagenums:',re.findall(r'(?m)^\\s*(\\d{3})\\s*$', l))\nEOF\necho \"=== canary text ===\"\ngrep -n -i \"canary\\|canari\\b\\|Canaria\" KLN_1966.txt | head -20"
}
```


### [2026-09-06T22:35:20.720Z] TOOL RESULT

```
=== leaf 131 pagenums: ['228']
=== leaf 132 pagenums: ['230']
=== leaf 133 pagenums: ['232', '233']
=== leaf 400 pagenums: ['743']
=== leaf 401 pagenums: ['746']
=== leaf 402 pagenums: ['747', '748', '749']
=== canary text ===
6324:canard,  n.,  a  duck:  a  hoax.  —  F.,  ‘duck;  drake’, fr.  OF.  canari,  fr.  OF.  caner,  ‘to cackle',  which  is of  imitative  origin.  The  suff.  -art  (F  .-aril)  is  due  to the  influence  of  OF.  maslart,  'duck;  drake’,  fr. mask  (F.  male),  'male'.  See  -ard  and  cp.  cancan, canary,  n.,  —  F.  canari,  canarie,  fr.  Sp.  canario , ‘canary  bird',  lit.  ‘of  the  Canary  Islands',  fr.  L. insula  Canaria,  'one  of  the  Canary  Islands',  lit. 'Dog  Islands',  fr.  canis,  'dog'  (see  canine).  The islands  were  so  called  from  their  large  dogs, canasta,  n..  a  card  game  originating  from  Ar¬ gentina.  —  Sp.  canasta,  ‘a  basket',  fr.  canasta, a  secondary  form  of  canastro,  ‘a  large  basket’, fr.  L.  canistrum,  ‘wicker  basket',  fr.  Gk.  xxva- oepov;  see  canister.  The  game  was  so  called from  the  basketful  of  cards  used  in  it. canaster,  n.,  a  kind  of  coarse  tobacco.  —  Sp.  ca¬ nastro,  ‘a  large  basket’.  See  prec.  word.
28439:Phalaris,  n.,  a  genus  of  plants,  the  canary  grass (bot.)  —  ModL.,  fr.  Gk.  9aXapig,  ‘coot;  canary grass’.  See  next  word.
```


## [2026-09-06T22:35:32.395Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN kennel ===\"\ngrep -n \"kennel,\" KLN_1966.txt | head -3\necho \"=== HRN leaf 185 (p164) ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==186' HRN.txt | head -50\necho \"=== HRN leaf 176 (p155) ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==177' HRN.txt | head -50"
}
```


## [2026-09-06T22:35:33.356Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KNT leaf 224/225 (pp209/210) ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==225' KNT.txt | head -40\necho \"-----\"\nawk 'BEGIN{RS=\"\\f\"} NR==226' KNT.txt | head -40"
}
```


### [2026-09-06T22:35:34.036Z] TOOL RESULT

```
=== KLN kennel ===
6321:canal,  n.  —  F.,  fr.  L.  canalis,  ‘water  pipe,  chan¬ nel,  canal’,  prop,  subst.  use  of  an  adj.  formed  fr. canna ,  ‘reed,  cane ;  small  vessel,  tube’.  The  short¬ ening  of  the  double  n  is  due  to  the  phonetic  law, according  to  which  before  a  stressed  syllable, a  double  consonant  becomes  short.  Cp.  L. ciitulis,  ‘pertaining  to  a  chariot',  fr.  currus, ‘chariot’  (see  cttrule),  and  mamilla ,  ‘breast’,  di- min.  of  mamma,  ‘breast’  (whence  this  phonetic law  is  called  ‘mamilla  law’;  see  mammilla).  See cane  and  adj.  stiff,  -al  and  cp.  channel,  cannel, kennel,  'gutter',  which  are  doublets  of  canal. Derivatives:  canal,  tr.  v.,  canal{l)-er ,  n.,  canal¬ ize,  tr.  v.,  canal-ii-ation,  n. canalicular,  adj.,  pertaining  to,  or  like,  a  canali¬ culus  or  canal iculi.  —  Formed  with  adj.  suff. -ar  fr.  canaliculus  (q.v.)
6360:with  stiff,  -ic  fr.  L.  cannabis.  See  next  word. Cannabis,  n.,  a  genus  of  plants,  the  hemp  (hot.)  — L.  cannabis ,  ‘hemp’,  fr.  Gk.  xavvafkc;.  See  canvas, cannel,  n.,  a  gutter;  kennel.  —  ME.  cane!,  fr. ONF.  cane!,  fr.  L.  canalem ,  acc.  of  canalis, ‘pipe’.  See  canal  and  cp.  kennel,  ‘gutter’, cannel  coal,  a  bituminous  coal.  —  Corruption  of candle  coal.
18146:‘dogs’,  which  seems  to  be  metathesized  fr. *CT7raxa8£4,  fr.  Medean  spdka.  Cp.  the  second element  in  dachshund,  keeshond.Cp.  also  canaille, Canidae,  canine,  Canis,  chenille,  kennel,  ‘shelter for  a  dog’,  and  the  first  element  in  cynanche, Cynanchum,  quinsy,  squinancy,  scybalum. Derivatives:  hound,  tr.  v.,  hound-er,  n.,  hound- ish,  hound-y,  adjs.
=== HRN leaf 185 (p164) ===
- 164 —
743. seg *Hund'; vergl. arab. sij[ihistan d. i. np. seglpistän
'Fructus Cordiae Myxae , Sebestenen , Brustbeere*
(AM. 155).
g. saha^ sewä; Semn. eshe (vergl. Vullers ispnh,
ispehj isbähy Isbeh) ;täl. sipä'^); Käs. eshd^ espa.
niedisch^) (Snd^a (r^yr y,vva y.dkhovöi anuna M^Jb/),
Herod. I, 110; aw. span- Hund'; phlv. aak^ sag; ai.
cvdn-; arm. sun (H. No. 224).
kurd. seh (d. i. se) *Hund', Plur. sän, seiän; afy. spai.
744. »ffgtir^ sngvrne, stiyvr 'Stachelschwein'. Si/uL sJ/ttr,
g. si/ttr.
aw. sukuruna- (zu den Hundearten gezählt); phlv.
sukur (Thonnelier).
kurd. LW. st/ör; af}'. sktlnr, skön (Dar niest et er,
Ch. pop. 8 45 ; ebendaselbst baragsta (Dialekt des
Distrikts VazTrl) snkal); bei. sikun^ n. sl/un \Stachel-
schwein' (345).
745. {\)fiuniy sumh^) *Huf.
aw. vergl. safa- 'Huf; phlv. suinb, arm. LW. smhak;
ai. vergl. QapUä' 'Huf*; an. hüfr, nhd. Hüf,
kurd. LW. shn; af;. sioa gespaltener Huf, LW.
sum; oss. säffäg *Huf, Klaue' (224); wa;^. sar. LW.
süm.
Eine Urverwandtschaft ist sicher zwischen aw.
safa-, ai. (japhd-, afy. swa^ oss. säffäg einerseits und
np. surn^ snmh andererseits anzunehmen.
746. {2)sumi^ sunb 'Höhle, Loch*, smnhiden^).
kurd. so7ifin^ LW. sümb^)^ stitfib^) (H.-Sch.),
sumbtden^); bei. LW. (?) sumb Xoch', snmhag, n.
sumbay *bohren, stechen (351, 352).
Zu np. sufte^i (No. 740).
*) Vergl. hyrkän. spas bei de Lagarde, Ges. Abh. 226, 227.
*) D. i. wohl auch ap. (vergl. Hörn, Indog. Forsch. II, 137), da
die dialektischen Formen doch nicht sämmtlioh medisch sein kennen.
') Sieho vorige Seite Note 2.
=== HRN leaf 176 (p155) ===
— 155 —
Also zu aw. [/^spas'y spast/eiti *spälien'? Sehr un-
sicher, Hübschmann, Armen. Stud., S. 50, No. 257^).
699. »ipah *Heer , sipeh^ ispeh\hed (arab. isbah[hu(/), jüd.-
pers. HNDID (Is. 13, 4).
ap. Ta/ma]späda- ; aw. spaöa- *Heer ; phlv. späh,
spühpat, arm. LW. späh, aspalmhet-),
oss. d. t. afsady t. ä/sud grosse Menge, xVbteilung
von Personen, Heer, Regiment* (40).
700. sljßer, isper *Schild'.
ap. anaoa^ßdgai' oi ye()()0(p6(}0i Hesyeh ; aw. spüra-
'Schild* in sparö.\dästa' ; phlv. spar (Men.); skr. phara-,
phalaka- (Mbh.) 'SchikV, daneben LW. sphara-^spharaka-
(Nöldeke, Monatsber. BAW. 1883, 1100).
arm. LW. aspar.
701. seperden, siperden auf etwas treten*.
aw. l^spar-^ vi\spara; phlv. spurtan (Bund.); ai.
[^sphur-^ sphurdti 'schnellen, treten; plötzlich er-
scheinen* (in letzter Bedeutung spät).
Nicht durchaus einwandsfrei.
wa/. na-spar-am, §i;'n. ni-^par-am, sar. na-xitor-am
^stampfen, treten*.
702. supurz Milz', uspurz.
Käs. espül^ espol, osböl (setzen ein "^esbäl voraus)'^).
. ') Rückert'8 Erklärung des Wortes (ZDMG. 8, 240) ist, wie
immer, geistreich aber doch unmöglich.
2) Zu arm. sparapet oQx^^^Qa^nyoi vergl. Hübschmann, ZDMG.
35, 133 Note 2.
') In diesem Falle gehen die np. Dialekte mit dem Pehlevl zusammen
und setzen eine ap. Grundform ohne r- Vokal voraus. Die Einstimmig-
keit der Dialekte in der Verwerfung des r- Vokals — alle Ausnahmen
beruhen auf Übertragungen aus der Schriftsprache — haben mich —
zusammengenommen mit dem Material, welches die modernen iranischen
Sprachen liefern sowie einer Vorliebe des Neupersischen für Trübung
ursprünglicher a, 6 in u ~ veranlasst, KZ. 32, 572 folg. dem Altpersischen
den r- Vokal abzusprechen. Ich möchte jetzt jedoch an dieser Meinung
nicht mehr festhalten, zumal da auch das Beläcl noch deutliche Spuren
eines einstigen Besitzes des r- Vokals aufweist.
```


### [2026-09-06T22:35:35.913Z] TOOL RESULT

```
=== KNT leaf 224/225 (pp209/210) ===
2; 4.66. abara imf. ($40, $84, 5228.) DB 1.25, 55, 88, 94; 2.25, 34f, 40, 45, 54, 60, 68, 86, 97^; 3.6, 17, 37, 45, 62, 67 (written ar?r^, 854.11), 87; 4.61, 62; DNa 50f; DSf 19°, 32; XPh 33, 45. abara” 3d pl. imf. ($10, $40, $84, $106, 8232.1) DPe 10; DSe 18°; DSf 34. aba- raha” 3d pl. imf. ($10, $218, $282.11) DNa 19f; XPh 17 (written орт, §54.1). abara"tà 3d pl. imf. mid. ($10, $236.II) DB 1.19. abariya imf. pass. (535.1, $220, $228.IT) DSf 23°, 31f, 35, 36, 38f, 40, 48, 45. abariya" 3d pl. imf. pass. ($220, 8232.11) DSf 41, 47.  baratuv imv. (5237.П) AmH 11^; DPd 14; DSk 5. аталаш inf. ($238) DNb 41.
à + bar- ‘perform’: dbaratiy ($218, $228.1) DNb 25. Cf. also Hz. Ар] 110-1, who refers to à-bar- certain other forms listed above as augmented forms of uncompounded bar-.
pati- + à + bar- ‘bring back, restore’: райуй- baram Ist sg. imf. DB 1.68 (but -à- perhaps only by influence of pardbartam, JAOS 62.275; 558, $206c).
para + bar- ‘bear away, take-away’: pardbara imf. DB 1.71, 96. pardbartam nsn. past pte. pass. (§242.1) DB 1.62, 67f.
pari- + bar- ‘protect, preserve’ (cf. Hz. Ар 112-3): paribarümiy Ist sg. (8226.]) DNb 17. paribarühy 2d sg. subj. ($27, $136, §222.IT, 4227.1) DB 4.78; paribaráh*-di$ (827, etc.) DB 4.74. pari- barā 2d sg. imv. (5237.1) DB 4.72, 88.
fra- + bar- ‘proffer, grant’: frábara imf. AmH 7; AsH 9; DB 1.12, 25, 60; DPd 3f, 7f; DPh 8; DNa 33; DSf 11; DSm 3°; DSp 2°; D8s 6; DZc 4; DH 7; A’He 18f, 20.
bara- sb. ‘bearmg, bearer’: Av. -bara-, Skt. -bhara-, Gk. -фороѕ, pIE "bhoros ($32, $122, $1431, ҮТ), to root bar- ‘bear’, in aritibara-, takabara-, vacabara-; also bāra- ‘borne by, rider of’, with vriddhi (8122, $126, 5148.1), in asabdra-, ef, usabüri-. See Hz. Ар] 95.
bard- vb. ‘be high’: Ау, baraz- ‘high’, baraz- ant- ‘lofty’, NPers. burz ‘high’, Skt. brhánt- ‘lofty’, OHG berg ‘mountain’, pIE *bhergh-; in Bardiya-, barsan-, probably in brazman-.
Bardiya- sb. Smerdis’, brother of Cambyses ($16411): Elam. bir-h-ia, АКК. bar-zi-ia, Gk. Урёрӧ ($29.02, $30). Репу. (§144.1V) of OP bard- ‘be high’ (575.11): ‘The Exalted’. Bardiya пет. DB 1.30, 32, 39, 52f; 3.25, 35, 54; 4.9, 27, 82; DBb 4f; DBh 5. Bardiyam asm. DB 1.31 bis, 51.
barSan- sb. ‘height, depth’ (S81): Av. barazan- .
(ВМ. AiW 950); deriv. of OP bard- (575.1, $155.1; Scheil 21.26; Konig, Burgbau 51; Hz. AMI 3.57; Bv. Gr. $812; Kent, JAOS 51.204, 99.15). bar$nà ism. (806, $120) DSf 26, 26f.
bav- vb. ‘become, be’: present stem bava- (8213), Av. bavatti, Skt. bhdvati, Gk. ote ‘grows’, Lt. fut ‘I was’, Lith. butt ‘to be’, NEng. be, pIE *bheu-. See also büm:-. bavatiy (§122, §228.1) XPh 55, 56. bæa"ty 3d pl. ($232.1) DNb 14 (башайу in 2d copy, Hz. ApI 115; ef. $48). abavam Ist sg. imf. DB 1.28, 60, 72; 4.5; 5.4^; DSm 6°; XPf 35, 36f; XPh 30; XSe 4°. abava imf. ($228.IT) DB 1.32, 38, 34, 40, 48, 77, 80; 2.16f, 17, 80, 94; 3.10, 11, 20, 27, 28, 76, 82, 83; 5.5, M^, 30; DSf 25; XPf 26.  abava^ 3d pl. imf. ($112, $232.IT) DB 1.76; 2.7, 93; 3.78; 4.34. bavātiy sub). ($222.11, §228.1) DNa 43, 45f; DNb 59 (Lg. 15.74; confirmed by photograph, JNES 444). [biyjä 2d sg. opt. ($114, $218.11, $223.I, $227.11) DB 4.69. буй opt. Cbhy-net, Bv. Gr. $232, comparing Av. buyd{ from *bhu-iët; but ВЫ. Gdr. IP 1. $143 takes as *bhy-i48t, = Lt. fiet, which may be either non-thematie opt. or thematic subj.; $114, $122, 5208, $218.II, §223.1, $228. ID) DB 4.56 bis, 58, 59, 741, 75, 78f, 79°.
bigna-, in d-bigna-, see Bagabigna-.
biimi- sb. ‘earth (= world or ground)’: Av. bümi-, NPers. büm, Skt. (RV) nom. bháümi bhümis; deriv. of root bhav- (see bav-) in grade bhi-, cf. Skt. aor. ábhüt, Gk. ёфо ($11, $65, §152.1V, §179.- IIT).
LEXICON
bümim asf. DNa 2, 32; DSe 2°; DSf 1; DSt 2; DZe 1f; DE 2; XPa 1; XPb 2; XPc 1; XPd 2; XPf 2; ХР 1f; ХЕ 3; XV 2f; A!Pa 2^; A?He 2. ратат, asf. ($55.1) A3Pa 2. bümiyà sf. (8179.IT) DNa 11f; DSb 9; DSe 10; Рб 5; DSs 2°, 3°; DZb 4; DZe 6; DE 17f; XPa 9; XPb 17; XPe 7f; XPd 12; XPf 12, 25; XPh 10; ХР); XE 17; XV 13; A'Pa 18°; A?8e 4°; Wb 7; Wc 8; Wd 8.
BU nsf. ($42) DSf 24, 28. 
-----
BUyà Isf. DSd 2°; DSf 7, 15, 16, 18, 24^; DSg 2; DSi 2, 4; DS) 1°; DSy 2; D'Sb 2; A’Sa 1; А4 2; A?Ha 2; A?He 9, 17; А?Ра 11.
brdtar- sb. ‘brother’: Av. brätar-, NPers. biraddr, Skt. bhratar-, Gk. @parnp ‘clan-brother’, Lt. frater, OCS bratru, Gt. brobar, pIE *bhráter- (862, 875.111, $128, $154.П). баі nsm. ($124.5, 5186.1) DB 1.29f, 39f.
brazmaniya- adj. ‘prayerful, reverent’ (cf. Kent, Lg. 21.223-9), with braz- rather than barz- (883; cf. Elam. pir-ra-us-man-ni-ia, АКК. bi-ra- 2a-man-ni-1): deriv. (§144.IV) to pAr. antecedent of Skt. bráhman- ‘religious devotion, prayer’, ef. identical Skt. deriv. brahmanyd- ‘religious’, to pIE root *bhergh- (see OP bard-; $75.1II, §95, $120, 5155.11; Henning, TPS 1944.108-18). For other views, see Kent, Lg. 13.301; Hartmann, OLZ 40.145-60; Nyberg, Rel. 367, 478; Hz. AMI 8.69, Apl 116-8 (to Av. barag- ‘to welcome’, barag- ‘rite’, Бәтәгба- ‘beloved’; wrongly, since this would give OP *bragman-); Christensen, Essai sur la démonologie iranienne 40-1; Henning, BSOS 10.506; Abayev, Iranskie Yazyki 1.134; Scherman, JAOS 65.141-3 n.23. Cf. also О. M. Dalton, Treasure of the Oxus 94-5. On form and meaning of РЫ. brahm brahmak, see Henning, TPS 1944. 108-18. brazmaniya nsm. ХР 41, 51, 54 (hardly brazmaniy isn. modifying arid; also not -niy apn. ‘divine’ with Sen 155, nor adn. in elliptic dual with Pisani, see under aria-).
т°, of dubious meaning, Se 1; taken by Justi, IFA 17.112, to be an abbreviation for OP *méraka ‘seal’, NPers. maráh.
та-, stem of ist person pron. in obl. cases of sg.; see adam.
mà conj. ‘not’, in prohibitions ete.: Av. Skt. mà, Gk. шӯ, pIE *mé ($109, §191.1, §292b). With subj.: DNb 55 (mé-taty), 58. With opt.: DB 4.59, 69, 79°; DPd 18, 19 bis, 20; XPh 39. With
201
inj.: DB 4.54; DPe 21; DNa 58, 59, 60; DNb 52 (mà-lay). With imv.: DNb 60. With lost verbs: DNb 57, DSq 4 bis; with restored subj. A'Sa 5^ bis, A?Ha 7, 7°. See also mdtya.
mā- vb. ‘measure’: Av. Skt. ma-, Lt. métior ‘I measure’. à + må- ‘extend’: атӣій npm. past ptc. pass. (6242. П) ‘noble’ DB 1.7; DBa 11. fra- + mā- ‘command’ (‘decide, judge’, acc. to Hz. ApI 154-6; ‘plan,’ Hinz, ZDMG 95.233-5); see also framülar-, framdnd-. јтатауаіа imf. mid. ($214, 5285.11) XPg 5. framatam nsn. past pte. pass. ($242.IT) DSf 19f°, 56.
таш- vb. ‘flee’: meaning established by Мат. and АКК. versions (Hüsing, KZ 38.258); probably to Skt. munthate ‘flees’ (Jn. JAOS 38.122). атида imf. ($211) DB 2.2, 71; 3.41f, 71.
Maka- sb. ‘Maka’, a province of the Persian Empire (lit. on location given in JAOS 56.217-8): Elam. ma-ak-qa, АКК. ma-ak, cf. Gk. pl. Мака ($99, $1322, SI4LITD. See also Mactya-. Maka nsm. DB 1.17; DPe 18.
magu- sb. ‘Magian’, member of a priestly order of Media: Flam. ma-ku-i3, АКК. ma-qu-&u, Gk. Méyos ($153.1). Uncertain material on mean- ing and etymology, Kónig, Klotho 4 chap. 12, and RulD 66. magus nsm. DB 1.36, 44, 46, 64, 66, 101; 4.8; DBb 2. magum asm. DB 1.50, 54, 57, 73; 4.81.
Maciya- adj. ‘Macian’; pl., name of a prov- ince of the Persian Empire: deriv. of Maka- ($99, $113, 8132.2, $144.01). Maciya пет. A?P 29. Масту for nsm. (856.11) DN xxix. Macy npm. DNa 30; DSe 230; XPh 25.
madtar- sb. ‘mother’: Av. matar-, Skt. matdr-, Gk. Dor. ратар, Lt. mäter, pIE nom. *maté, stem *máler- ($154.П): in hamdtar-.
таша conj. ‘lest, that not, not’: mà ‘not’ + conj. tya (§133, 4292р).  matya-mam (5133) DB 1.52. тайа DB 4.43, 48, 71.
mabista- adj. ‘greatest’, equal to ‘crown prince’ in XPf (Speiser ap. Kent, Lg. 9.40-1; Hz. Apl 254-8): Av. masista-, NPers. mähist, Gk. ppxio ros ‘longest’ (radical vowel after that in anxos Jength"); superl. to pIE *mak-ros, Gk. накр, Lt. macer ‘thin’, pLE root *mak- (887) ‘be long and slender’ + superl.,suffix.<ste-) (S117, $156.11,
202 OLD PERSIAN
4190.1), Gk. -сто-, Av. -tšta-, Skt. (with aspira- tion) -gha-. таб: а пет. AsH 6; DB 2.13,
```


## [2026-09-06T22:35:45.465Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 233 234; do echo \"=== leaf $n ===\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' KNT.txt | head -c 3000; echo; done"
}
```


### [2026-09-06T22:35:47.070Z] TOOL RESULT

```
=== leaf 233 ===

=== leaf 234 ===
```


## [2026-09-06T22:35:49.727Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"spāda\\|spada-\\|Sakā\\|saka-\\|Saka-\" KNT.txt | head -20\necho \"--- leaf count ---\"; awk 'BEGIN{RS=\"\\f\"} END{print NR}' KNT.txt"
}
```


### [2026-09-06T22:35:51.328Z] TOOL RESULT

```
1438:Saka-, Sug(u)da-, Nisdya-, si*kabru-, and the 3 dubious siyamam. 3 5117. рів. f from pIE s after certain sounds 1 (8115) remained unchanged in OP: у ОР тав: Ма- ‘greatest’, Av. masisla-, Gk. шікито 5 "longest". : OP fràisayam ‘I sent’, Skt. ejayat? ‘he brings’, OP uška- ‘dry’, Av. huska-, Lith. satisa-s. OP gausa- ‘ear’, Skt. ghóga- ‘noise’. 4 OP adarínaus ‘he dared’, Skt. dhysnéti ‘he dares’. 4 OP aría- ‘male’ in ArSama- ‘Arsames’, Skt. 4 rsa-bhd- ‘bull’. 4 pIE *sed-as- in ОР Лай ‘seat’, cf. СК. &os (from -$ pIE *sedos). 4 pIE *e-st-sfe-to, OP ачЧаіа ‘he stood’, cf. Gk. : israrat ‘he stands’ (from *sestatat). 4 pIE *rsti-, OP nom. arštiš, Skt. rstf-s (cf. $115). 4 OP nom. tani ‘body’, Skt. tani-s. 4 For ks and other clusters giving zš, see $102; 4 for kn and gn giving initial тп and medial im, 4 $06; for -Sc- as a sandhi product, $105; for pAr. 4 & giving OP Sy, $104; for pAr. t giving OP y 4 $80; for pAr. én giving OP $n, $82. 1 The verbal prefix ni- affects an initial s of the 4 verbal root; thus ni-$d- from ni- + stä- and 4
1583:kasaka-, kásakaina-.
1778:IIT. With no obvious simpler nominal or verbal form: ama- in Arsdma-, asa- aspa-, u-ba-, poss. ^upa-, kaufa-, kara-, daiva-, darga-, naiba-, Parsa-, pisa-, Máda-, raba- in u-rafa-, varka- in Varkána- and Varka-zana-, Saka-, späda- in Taxma-spáda-, spára- in Vdya-spara-; the restored hana- in hana- {й-; mayüra-, of uncertain etymology; the pos- sible vāra- in ^U-vára-zmi-.
1812:ПІ. Secondary -ina-, forming adjectives: afa^- ga-ina-, küsaka-ina-, nauca-ina-.
4941:azíaina- adj, with kdsaka-, ‘turquois’ (so Bleichsteiner, WZKM 37.103-4, and Konig, Burg- bau 63-4, but considered dubious by Hinz, ZDMG 95.235-6; hardly ‘gray amber’, with Hz. AMI 3.05—7, ApI 232; not ‘hematite’, with Scheil 21.29- 30): Av. arSaéna- ‘dark-colored’, borrowed in Gk. Порто “Atevos ‘Black Sea’ (‘in-hospitable’, by Gk. popular etymology, and euphemistically changed to Еф о), from neg. a- + z&atna-, cf. Av. xSaéta- ‘shining’ (§102, 5147.1). azšaina nsm. DSf 39.
5285:kasaka- sb. ‘semi-precious stone’; Elam. ga- st-ga causes König and Wb. to write kás'ka, but this is not warranted by the OP writing. регу. of Iran. root *kas- (89.V, §87, $126, §146.II), = Skt. kaś- ‘be visible, appear, shine’ (so König, Burgbau 61; not to Skt. Ёйс@- ‘crystal, quartz’, despite Bv. BSLP 30.1.61); for meaning, cf. NEng.
--- leaf count ---
232
```


## [2026-09-06T22:35:58.194Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint(len(leaves))\nfor i in range(225,len(leaves)):\n    l=leaves[i]\n    print('leaf',i,'nums:',re.findall(r'(?m)^\\s*(2[01]\\d)\\s*$',l), '|', re.findall(r'\\b(20\\d|21\\d)\\b',l)[:6])\nEOF"
}
```


### [2026-09-06T22:35:59.710Z] TOOL RESULT

```
232
leaf 225 nums: ['201'] | ['201', '214', '211', '217', '202']
leaf 226 nums: [] | ['214', '215', '214']
leaf 227 nums: [] | ['203', '213', '213']
leaf 228 nums: ['204'] | ['204', '213']
leaf 229 nums: [] | ['205', '215', '215', '208', '213']
leaf 230 nums: ['206'] | ['208', '206']
leaf 231 nums: [] | ['210']
```


## [2026-09-06T22:36:05.240Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==232' KNT.txt | tail -c 2000\necho \"=== grep sak ===\"\ngrep -n \"sakā\\|saka nsm\\|‘Scythian\" KNT.txt | head"
}
```


### [2026-09-06T22:36:06.819Z] TOOL RESULT

```
1); -vā .. -vä ‘either... or...’: Av. và, Skt. và, pIE *ue, ef. Lt. -ve.  z$apa-ü rawca-paíi-a DB 1.20. hya-»à DB 4.68. imai-vä DB 4.71, 78, 77. yadi- vä DNb 25, 29.
vaina- present stem of vb. ‘see (mid.) seem’: Av. vaéna-, NPers. bindd, Skt. véda ‘knows’, vinddte ‘finds’, Lt. videt ‘sees’, videtur ‘seems’; pAr. *uaid- na-, plr. *yaina- ($69, 588.1, $130, $210.III; Reichelt, Aw. Ер. $157). See also Vidafarnah-. vainümiy lst sg. (4226.1) DNb 36, 36f, 39, 40. avaina imf. DB 2.76, 90; DNa 32. vainataiy mid. as pass. (8235.1) DNb 2; XPa 16. vaináhy 2d sg. subj. ($37, $222.11, $227.1) DB 4.70, 73, 77; DNb 29. vaindtiy subj. ($222.11) DS} 5°. vainātaiy subj. mid. as pass. ($222.П) DNb 35.
vau- adj. ‘good’ ($11, §153.1); nt. as sb. ‘the good, (religious) goodness’: Av. nsm. vaphus, nsn. vohu, Skt. nsm. vásuş, nsn. vdsu, pIE *yesu-; in Dérayavau-, Vaumisa-, Vahauka-, Vahyazdata-.
Va'umisa- sb. ‘Vaumisa’, a Persian officer of Darius: Elam. ma-u-mi-i8-8a, АКК. ti-mi-is-st, Gk. (Plutarch) Rutens; cpd. of vatu- and mifra- ‘friend’ (849c, $78, $148.ILD): ‘Friend of the Good’ §160.- Ib; cf. MB Gr. $51). Vaumisa nsm. DB 2.49, 51, 62. Vaumisam asm. DB 2.53, 58.
vaz$- vb. ‘grow’, see (Луах${та-.
Waj- vb. ‘be strong’: Skt. vaj-, бјаз- ‘strength’, Av. aof
=== grep sak ===
```


## [2026-09-06T22:36:13.120Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"Scyth\" KNT.txt | head; echo \"---spada---\"; grep -n \"spád\\|späd\\|spāda\\|spada\" KNT.txt | head\necho \"=== KNT online? try archive fulltext later ===\""
}
```


### [2026-09-06T22:36:13.181Z] TOOL RESULT

```
335:III. Among the less known Old Iranian lan- guages the most important was Median, known only from glosses, place and personal names, and its developments m Middle Persian, apart from borrowings in OP, which are of considerable im- portance for the understanding of OP itself. Others were the language of the Carduchi, pre- sumably the linguistic ancestor of modern Kurd- ish; Parthian, the language of a great empire which contended against Rome in the time just before and after the beginning of the Christian era; Sogdian in the northeast, the ancestor of the medieval Sogdian; Scythian, the language or languages of the various tribes known in OP аз Saká, located to the east of the Caspian and north of Parthia and Sogdiana, but also to the west of the Caspian on the steppes north of the Euxine Sea.
343:dialects, including the Arsacid and the Sasanian types, the Sogdian (known also from a trilingual inscription of Kara-Balgassün), and a dialect known as ‘Eastern Iranian’, perhaps a derivative of northeastern Scythian, in which there are texts of the Buddhists of Khotan. The notable peculiarity of these Turfan texts is that they are written in relatively pure Iranian, without the Semitic writings for the words which are to be spoken by the Тташап equivalent.
344:V. Among the earliest traces of Pahlavi, how- ever, are certain legends in Greek characters on coins of Indo-Scythic rulers of the Turuska dy- nasty in northwestern India, belonging to the first two Christian centuries.
352:VII. The Ossetic dialects, in the general re- gion of the Caucasus; derived from the Scythian of Southern Russia. |
825:Pointed-Cap Scythians’.
827:Amyrgian Scythians’.
892:IV. The following clusters of two consonants occur medially between vowels: zt z6* xn zm* zr ak, gd gn gm gr, jy, tp* tr*, üb* Om Gr*, dr du, ny то, fr, br, mn my, rk rz rg rc rj rtrd rd rn rb rm ry то r$ T$, ld*, st sp sm, Šk Sc М $d* $n. šp šm Sy &, zd 2b* zm гт, hy. In the clusters nk nz* ng nt nd mp mb hm hv, all of which actually occur, the prior sound is omitted in the writing. Of those marked with *, 00 occurs by analogical formation; 10 only in an uninterpretable word; zm, 67, and zb, only in Median words; nz only in a Scythian name; tp, tr, ld only in non-Iranian names of persons and places; Sd only in apparently cor- rupt writings.
1943:ШЇ. Names of other Iranians: the Margian (Bactrian) Frada-; the Scythian Sku*xa-; un- specified Afiyabaukna-, Arsake-.
1981:Akaufaciya ‘Men of Akaufaka’; Unarazmiy and -miš ‘Chorasmia’; Gadára ‘Gandaritis’; 8ata- gu’ Sattagydia’; Рала ‘the Daae’; Maka or ethnic Maciya; Saka or fem. бака Scythia’ or Хака ‘the Scythians’; Sug(u)da ‘Sogdiana’; Haraiva ‘Aria’; Hidus Sind’.
2717:Е. With Ласа, to denote place from which: DPh 5 (and DH 4) hacé Факат ‘from the Scythians’; but perhaps the ablative form in the plural had been lost, and its functions been taken over by the instrumental form, for there is no distinctly abla- tive plural form recorded in OP.
---spada---
379:names of the Меде T'azmaspada and of the
1084:V. There are also numerous instances of OP { @ d which are not traceable with certainty to IE origins, or are demonstrably borrowings from non-IE sources. Among these are taka- ‘shield, round hat’ in faka-bara-, tacara- ‘palace’, dipi- ‘inscription’ (see Lex. s.v.), spáda- ‘army’ (only in Iranian), imv. rax@atuv of uncertain meaning; and personal and place names such as Atamaita- (Elamite), Nadztabaira (Semitic), Ufratu- 'Eu- phrates', Katpatuka ‘Cappadocia’, Tigra- ‘Tigris’, Putaya- ‘Libyan’, Datwahya-, Daha-, Dwubála-, Mudràya-, Aburā, etc.
1313:OP tarma- ‘brave’, with Med. -rm- in the name of the Mede Tarmaspáda- and of the Sagar- tian Cicatarma-; Av. tarma- ‘brave’.
1435:the non-aspirate). sp in späda- ‘army’, in Taxmaspdda- (name of a Mede); in Vayaspdra- (name of a Persian):
1778:IIT. With no obvious simpler nominal or verbal form: ama- in Arsdma-, asa- aspa-, u-ba-, poss. ^upa-, kaufa-, kara-, daiva-, darga-, naiba-, Parsa-, pisa-, Máda-, raba- in u-rafa-, varka- in Varkána- and Varka-zana-, Saka-, späda- in Taxma-spáda-, spára- in Vdya-spara-; the restored hana- in hana- {й-; mayüra-, of uncertain etymology; the pos- sible vāra- in ^U-vára-zmi-.
3625:82 а: Madam : friisayam : Taxmaspada : nàma : Мада : mand : badaka : avam
3628:85 āva : Taxmaspáda : hada : kira : aSiyava : hamaranam : akunau’ : had )
3683:§33. 2.78-91. Saith Darius the King: One man by name Cicantakhma, a Sagartian—he became rebellious to me; thus he said to the people, “I am king in Sagartia, of the family of Cyaxares.” Thereupon І sent off a Persian and Median army; a Mede by name Takhmaspada, my subject—
3685:“Go forth; the hostile army which shall not call itself mine, that do ye smite!” Thereupon Takh- maspada with the army went off; he joined battle with Cigantakhma. Ahuramazda bore me aid; by the favor of Ahuramazda my army smote that rebellious army and took Cicantakhma prisoner, (and) led him to me. Afterwards I cut off his ears and nose and tongue, and put out one eye; he he was kept bound at my palace entrance, all the people saw him. Afterwards I impaled him at Arbela.
4890:hered to Phraortes, declared himself King in Sagartia, a distriet of northern Media; he claimed to be of the family of Cyaxares. Darius sent а force of Medes and Persians under Takhmaspada, a Median officer, who defeated and captured Cicantakhma, bringing him to Darius. Darius mu- tilated him and put him to death with torture, at Arbela ($33). Thus ended rebellion in Media (884) ; but there was still a strong rebel force in Armenia, against which Darius sent an Armenian officer named Dadarshi. Dadarshi, thrice attacked by the rebels, defeated them successively at Zuzaya on II 8 (§26), at Tigra on II 18 (§27), and at Uyama on III 9, whereafter he waited for Darius to come and make final governmental dispositions (828). This third battle by Dadarshi was only nine days after Vaumisa in а second engagement beat off the other force of Armenian rebels in the dis- trict of Autiyara, on IT 30; after which he also awaited Darius’s arrival (530). There was по fur- ther fighting in Armenia.
=== KNT online? try archive fulltext later ===
```


## [2026-09-06T22:36:15.595Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT spa- dog / spada ===\"\ngrep -n \"spā, spānəm\\|span-\\|spaka\\|spā ‚Hund\\|Hund‘\" BRT.txt | head -20\necho \"--- spada Heer ---\"\ngrep -n \"spāδa\\|spaδa\\|spāda\" BRT.txt | head -20"
}
```


### [2026-09-06T22:36:15.661Z] TOOL RESULT

```
=== BRT spa- dog / spada ===
5885:ni.  ahoilhäna-  n.,  mp.  (Pü.)  fli/flj/J«,  ann.I.W. aspastan,  —  ')  rSt.  s.  unter  usIräjlSna-. j.  aspiii':  a.  unter  aspan-, j.  BspkrtxilS  N.  pff;  lies  asprinö.
6536:Vfil.  aiakva-.  —  Pü. :  fehlt. •  j.  azay-  m.  i)  'Schlange',  ein  ^ÄiÄisches Tier:  /<fiws.tara  ya^a  'zayS  xsvoewanhs V.iS.ßs;  —  'Sinam  udarS.>rasanam  .  . °iinam  spakanqm  kahrpunanam  (sd.)  V. 14.%.  a)  Sing,  in  koll.  Sinn:  äat  ahe paityänm  .  .  'zimca  yim  raoioibtn  (sd.) zj'rtM/a..V./.2''; — yai3  '%wä  niHt  aiwi,- Jruzilnti  •iisea  arütuiisca  "damit  dir kein  Arg  antun  können  Schlangen  und  .." YL5, 90.  2)  schlangenähnlichcs  Untier 'Drache,  Ungeheuer'":  'zdis  sairitaAe simahe  vlsS.valpahe  Y.().3o;  —  'zis .  . gäuitava . .  vTraja  Aog.  ~S;  —  'leis  vJlspahe N.  48;  —  ktrasäsps  .  .  yS  jartat  °ilm (sd.)  yim  aspB.garpm  mnganm  ..
9326:•  j.  kahrpuna-  m.  Name  eines  a'aft'ischen  j  schleppten  sie  die  Weiber  den  Menschen Tiers'*:  baivan  alinam  spakanqm  •■nanqmX-^^^'  Yt. /g.  80".
12441:asahya  axäyai  (sd.)  ggnedim  Y.  37, 17;  — aiäunqm  . .  uruns  .  .  kudüJiatanqmAt  .  . yailqm  vahehl^  'na  vanainti  va  vSnghm va  vaonarS  va  H.  3g.  z;  —  karapanS kavayasca  .  .  ySng  ^S  urva  ::^a!^a  xrao- dat  (sd.)  'na  Y.46.11;  —  Ö  dngvats *tnandaHg  *9r?tael  (sd.)  haihim  yehya urvü  xraodaiti , .  Y.  ji,  13;  —  tsm  *vä ahsm  dtTgvantS  .  .  'na  nailal  (sd.)  Y.^y/. so;  zT.  verwendet  V.f.  fia;  s.  a;  —  ySi .  .  aiäm>m  vandtn  (sd.)  . .  töi  daoiStig dqn  yS  drsgvats  °na  ",.  die  —  in  AnDaiva Haus  fUr  das  Ich  des  ^rv^enossen!"  Y. 4^.  4*>.  a)  im  jAiv.:  alaonqm ..  ahümla 'nam/ai*  iaooasäi  urvänsmca  fravaiSmia yagamaide  Y.  a6.  4;  —  asni  iyazamaide\ manä  . .  °nä  [yazamaidi]  saoryantqm  yaaa- vtaide  Yt  13.  7^;  —  aisS  zT  växs . .  a  va^S ahunB  vaityS . .  uruna^a  'tiaca  (IS.)  span- vanti  (sd.)  H.  J.  4;  —  'nqm  .  .  yaoldai- är/a  dha  zl  aifihä  asH  yaosdaitis  kahmai- Ht  ..  havaya  tnsvS  'naya  yl  hvqm  'nqm yaozdaite  humataisla  ..  V.  10.  19*';  —  um vä  ahOm  drvaniö  *^a  *'na  msirtnttyJJ [a/isiäi  a/fuhe]  V.  5. 6a;  —  aiiihä  dim vütaya  fr-Jmita  (sd.)  salayeiti  ya  hava 'naT>  kaininS  k>hrpa  srlrayh  .  .  aat  Alm aoxta  ..yS  nars  asaonü  urva  alca  Karditis ahi  ..?  äat  hl paiH.aoxta  ya  hava  'na  .. az?m  ba  U  ahmt  .  .  yä  hava  'na  *:^ai- paihejanvö  {sd.Y'  H.2.9— 11; — arahvam 'nqm  V.^.ai  PüZ.s),  io.  19  PüZ.
18675:elliptisch  sva,  'ein  Mann  und  ein  Weib,  ein Menschenpaar"**:  dvaübya  haca  n)r>bya dva  nara  us^ayein/e (sd.)  t//i^wa/ia  s/ri^a nairyas^a  V.2.41.  2) '•  praegn. 'wehr- hafter Mann,  Kriegsmann;  kriegerischer Held':  narSi  ßrasaoifträi  Y.  28.  8;  — katna  (sd.)  syävarsänai  zurSjatahe  na- rahe''*  Yt*j.  18;  — pqsnus  narJ  (NS.)'^ HryS  taxmS  Aog.  84;  — y^i  narS  taxma ptntmU  Yt./J  27;  —  t! nard paiti.sanmti ySkva  v3r3%ra.l'aohl!  {sd.)  YtJ_j.  46;  — yat  mS  slärS  .  .  AacÜnte  (sd.)  n?r>byS ä^annff  *bax/3nia  Yt- 8.  1 ;  5.11,  77.6,7; das/a  narqm  *pouru.tät?m  stäkyanqm.. vanatqm  avammnanqm  Ny. J.  10;  —  hva- iai  naire  barumnäi  Y.  65.  4;  — yä  na- qm  vjg3r>pla{sd.yit . .  baoxtär^m  dahäi/i Vr.7,3;  Yt  10.12;  —  ya^a  hazannm Oim  narftn  adar.taySi^  Yt.  8.  $$; I.  19*;  —  a%ra  narqtn  mihrS.drujqtn apq/{sd.)  gavB  dar>tayeiti  Yt70. 48;  — narqm  asätanqm  frasS.car^'hrqm  saosyan- tqm  Y.  24.  5,  Yt.  13. 17.  a)  als  Bezeich- nung für  den  zweiten  Stand  (s.  'piflra-) 'Krieger,  Ritter***:  kada  .  .  mquarfi/ (sd.) rS  vis3nliY.48.  10;  — daidx atturai (AP.)  ,  .  asaunS  .  .  aidyüi  väsliyJng  ,  . ahmaibyä  ahma.rafonarahs  {^d^  Y.40.3; %wqm  ttarakl  ysi  taxma  Jathyintt äsu.aspim  .  .  %wqm  a^ravanS  .  .  mastim Yt5.  86.  3)''  ohne  Betonung  des  Ge- schlechts sva.  Mensch;  Person';  1)  im Gegensatz  zum  Tier;  uzw.  zu  a)  pasav-: ahe  nmanaßie pasvqmca  narqntla  Y.^-S; pasBm  .  .  nanm  ra?syät  V,  13.  32 b)  'span-.  . .  ahe  nmanake  spä  vä na  va  irihyat  V.5, 39;  8. 1,  4;  —  yat ahmi  spänasca  narasca  para.irüinti  V. 6.1; — y!i  pa^a  uebarmte  (^)  spänasca irista  iiarawca  (NF.)"  irisia  V.  Ä  14; 3.  32;  —  yat  ,  .  sairi  riiianie  spänasca irista  naraila  (AP.)'*  irista  V.  3.  8; 36.  c)   ^av-:  janyäi  *n>rSuI^'*  para
23868:•  j.  vohuna-nliag- :  'na-zg-  Adj.  mit ^span-  m.  'Bluthund,  Hund,  der  auf  den Mann  geht':  kva  asti  spä  'naegS^'>  däityB.- g3tusi..yS naecim  isaiti  Aunaranam  tanuye isaitt  hrahnm'^  "Bei  wem  ist  der  Blut- hund richtig  am  Platz?  .  .  (Bei  dem)  der, keine  (besondere)  Fertigkeit,  (sondern)  nur Schutz  für  seine  Person  verlangt"  V. /?, 19;  5.30;  —  späram  yim  .  .  'zg9m  V, lg.  14,  22,  a6;  —  sänqm  .  .yim  . .  'tgqmca V.  i_J.  8;  —  *us  *fäcit  spann  patinti  pams.- haurvqmca  (sd.)  .  .  'sgam^a  V,  i^.  4a,
24581:•  j.  vi-zuS-'*  m.  (auch  mit  ^span-  m.) Name  einer  Art  desHundegeschlechts;  hau 'zaui^GS-yK .  hau  vispanam . .  spaci%ra»am V.y.  16;  —  spä  -««/{NS.)  V.5.32.
25524:•  j.  umpay-  m.  (auch  mit  ^span-  m.) Name  einer  Art  des  Hundegeschlechts: hau  'pü  (statt  GS.)  HU.äatahe  . .  hau vispanam  .  .  spaci^ranqm  V.  13. 16;  — spä  •pii'V.S.ss'.
26366:•  j.  sukurana-  m.  (auch  mit  ^span-  m.) Name  einer  Art  des  'Hunde' ''geschlechts,
26439:Der  Text  ist  inkorrekt  und  inhaltlich  unklar.  — Pu. :  knrkn  maW  ('Heuschrecke')  i  gSspan- dän  dadtrii  i pur  mark;  erl.:  ma\ak  ape  äyil iiirläk  -  ku  ape  vSitr  apt  äyil  —  gäv  baslan HC  säytt  gäspandma  mariih  bavel.  AuchOrBd. (s.DST.ZA.2.8)  bietet  'Heuschrecke'  -  kmca; s.  PPGI.  ff.  3  -  für  skailJm.  —  0  So  nach der  Tradition;  s.  oben.  Anders  FkMOllek WZKM.  3.  366,  6.  183.
26785:'span-
26811:•  j.  spaka-  Adj.  'hundeartig,  Hunds*'; aHaam  •kanam  kahrpunanam  (sd.)  V. 14.  S-
26816:gehörig"':  hau  vispanam  ..  'ranqm  anya udra   upapa   "das   (ist  die  Strafe  für  die Tötung)  aller  . .  zum  Hundegeschlecht  ge- hörigen Tiere  ausgenommen   den  Otter, der  im  Wasser  lebt"  V.jj.  16. Pü,:  sak  tBxmak.  —  0  S.  "j/j«-*). j.  ". .  drujs  spaiti  di^ra  . ."  Vyt-JS. j.  'span- :  w(«-'>  m.  'Hund'*':  spänsm da%3m    .  .   az)m  yd   ahurS    maxds    hvä- vastnm     :^ä.adhr>m     Bomi.buhnm    tüi.- dqsur?m  vXrS.dra(mat»hftn  gathanqm  bar»- \a  .  .   iparum    nida%tm  ya{   dtm mazaos' (sd.)   kakrpü  tlirahe  V./;.39;   — sBnahe*>  afvahe  *asta.bifmn{^d.)  V./J.  44; \pan3m  tairittm  cd^ru.casm>m  spaOfin zairi.gaehm  ä^ritXm  t(äa  altä  pa%ä  vTVä- iayantu  aiwi.nitHsd.)cit..spatum.."wi.tn.. Hund  sollen  sie  dann  dreimal  diese  Wege auf  und  abfuhren,  und  . ."  V.Ä  16J';  17, span>tn    *nagsyeiti    FrB.3);     — .  üsi!t)m    zaurvämtn  (sd.)    upaili \yat  spänü  (NP.)  ySi  hisbnte  a:^ars  upa \3^armt?m  V,  7^.28;  —  pars  xrvis(5d.)ca .  .  baratu  (sd.)   :^ar^anqm  sänahe'''    V. 79.  28;   —  yat  . .  sps   avacä  vä  bavai ahaitys.xratuiy.13.2fj;  31,35.37.  ^5-48; —  ka%a  alte  spana  (NP.)  sl'a.Kaifam  (sd.) sfädraomm  bavqnl  .  .  yavat   aete    spana
26819:'span-  a.
--- spada Heer ---
```


## [2026-09-06T22:36:26.039Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"spaSa-\\|spa8a-\\|spa5a-\\|spaöa\\|spa&a-\\|spāδa\" BRT.txt | head -10\necho \"--- Heer with sp ---\"\ngrep -n \"'Heer'\" BRT.txt | grep -i \"sp\" | head -10\necho \"--- spadapati / spada.paiti ---\"\ngrep -n \"spä8a\\|spa9a\\|spa\\\\.\\?9a\\|spaöS\" BRT.txt | head\necho \"=== line 26819 ff context ===\"\nsed -n '26800,26830p' BRT.txt | cut -c1-400"
}
```


### [2026-09-06T22:36:26.127Z] TOOL RESULT

```
24151:vindatspaSa-  i 448
27053:•  j.  spiti",  nur  KompA, :  sva.  spaSa-. aS..  vgl.  ivilic-i.    —    Vgl.  unter  äj«:/'.   —    S. auch  jMy"  EN.
--- Heer with sp ---
26842:lusammengefallen  sein  kännen.  —  PQ. :  späh 'Heer'  -  Sü. ;  'paläkmikah  -,  wegen  des  Ad- klangs.  —  ')  S.  bav  No.'  14.  —  »)  iSt.  vgl.  Y. $3.  6  unter  fräday.  —  3)  Wie  ai.  gäyalri-, täruira;  iritidlra--a.a.;s.  nochNo.4.  —  4)  Dann vll.  mit  ai.  svälrä-  n.  {im  Nsigh.  'ähanam',  bei Olsenberg  SSE.  46.  26  'power')  lusunmen- gebörig,  das  ein  ar.  Praes.  21  'sgä-  voraus- setien  würde,  oder  -  was  das  selbe  ist  -  eine 'WurielcrwcileninB'  durcli  li;  vgl.  !irv:Ara:
28704:.  j.  'haena-,  p.  haini-  f.  'Heer,  Heer-  ■  ■  ^'^  Z'^",  h«^_^rinHi  .  .  a3aih>a schar'  uzw.  rfa?^ischer  Wesen,  'Feindes-  'i^^lsva  . .  hau  astt  äafvö. .  avat  daa,a heer,  feindliche  Heerschar':  Wabiy  imäm  ^^'"'^'"■'»^  ' . .  (sva.)  dort  ist  der  Z>. . daÄyäum  mä  5>;/.,>J*  ma  'nä  D.4.3;  V-Z-SafO;  _  s.  noch  H.1.7  (Sp.173»  o.); ^  n^it  i^ra  atryA  dai^hävS  fräs  (%A..)  "  ™  Gegensatz  zu  ÄJ  (Sp.  1718  o.):  >Sff yiyj/  •;«»  YtÄs6;  F.l-^;  -  ^«laäa  «P^-m^r^tS  i%^.  1143  m.)  ,4 5 «  ,.j-;tjr^.- «(■rr-^-b'iT  rfa/Vi^«4>.S  ■««  (NP.)')  frapatänti  '""'^  iäW  ..V.4.AS;  -  zugleich  aul  ein Yt..y.6i:  —  ya'ba  yai  hazarirS.aspam  erläuterndes  Nomen  vorausweisend:  aoa 'nam  avazeit  mäzduya'sni!  avi  vis5  Y.  hau  apa^^arS bvatzraya»ks vouru.kaiahe i8'.i^;  -  Ümäm  daAyüufn  ^ura^mazdj  ^""^  yH  haosravA  nqma  Ytip.sS;  59, patup  haia'nmD.4.6;  —  'nayä^axra-  ^'-  ")  '"  schwachdciktischer  Vcr- vai^yä  z>yazJayä  (sd.)  Aog.  A;  Yt  5.  131,  Wendung  jener,  der';  I)  zurückweisend; 4.  3.  19-  93,  ^-  II  (wo  'nayiuay-'nyhla  ^  *"/  f  ?  ^^O'uen;  a)  auf  ein  Substantiv; .  .  davai^yi  pataihyä  Y.0.18;  —  fiairi  «>  adjektivisch:  II  War««*  näm^  pärsa* ^•nyhsia  pöiynäuyS  Y.  68. 13;  -  ivi  'nayi  1  ■  ■  ''/'"'  ^'^rnaf  hada  kärä  al,yav^  Bh. (AP.)'>  xrvi^ätl!  Yt  10.  8;  />  49,  /<?.  54;  1  ^-  K^^'  '■  »?'  ^-  ?-  5-  • !  —  'Jäw«  /Jwa« —  ;*a.n<i>7'a/4yff*-«ÄS;'?"  Y.i7.asi>.  ^fi-ätfayam  . .  ya-^a  hauv  karJ'  parä- Ableit.  —  Zum  V.  ^(>>.  —  ai.  sinä-  f.  '"öJir  . .  Bh.  5. 1 ;  ü  —  »flr?m  afavarum  .. 'Heer';  mp.  (Pü.)  Äe«.  —  ')  NPn.  aUtt  NPf.  j  *hau  *n3"  .  .  P.2^;  —  zugleich  auf  ein (wie    umgekehrt,  S   ¥"■    3  d).     Vgl.    dazu  1  Rglativum    vorausweisend:    Wkärt/'    hyi^
--- spadapati / spada.paiti ---
=== line 26819 ff context ===
KompA.  —  Et.?  Nicht  la  ai,  sutc  trotz  BB. /9.197.  —  ai.  slri-  f.  —  Pü.!  ian.  —  i|  Hds. mailri.  —  J)  Hds.  ttri,  gegen  S  JOJ-  I ;  allen- falls aus  siri/a  herausgelöst.
•  j.  stri,niinan-  Adj.  '(mit  weiblichem Namen  sva.)  weiblichen  Geschlechts',  von Tieren:  hatanr.fi/  sartl/(sd.)  °manS  (NP.) . . nairyS.nämanö  V.  13. 51,  i4- 1  GL
ai.  sirinäman-  Adj.  'einen  Weibernamen  fah- rend'. —  Pü. :  mälat  »am.
•  j.  spaeta-  Adj.  (fem.  'tä-)  'weiss'; spunam  .  .  't?m  sairi.gaostm  V,  8. 16",  17, 18; — ye^he  ca%würö  vastära  'ta  vispa., Yti.  13;  —  'ta  vastri  vaahaiti  Ha  (NSf.) "weisse  Kleider  hat  die  weisse  an"  Yt. 10. 136.
KompA. i  Ableit.  —  ai  hitlä-  Adj,;  np.  sipfd. —  Pii.:  jj«.
•  j.  spaeto.ainika- Adj.  'mit  weisser  Stirn' : anid  . .  'is  Aog.  75(?)''.
PiL:  jfit/  Sali.—  »  Das  Wort  fehlt  in  Ggb.s Ausgabe,  mnss  aber,  wie  das  Glossar  zeigt, hdslich  bezeugt  sein.    Vgl,  auch /a/ro.  No.  1.
•  j.  spaeitita-  Adj.  'weiss,  weisslich':  't^m avi  vayhaiwn  VL  z^.  13;  —  upa  •tarn rasunm  YL/5. 31;  —  aurvants  'ta'' ^hamagaonärahs  Yt  10. 125.
Ableit  aMisfiaela.;  %  202.  —  Vgl.  tpaiHitt- loa. Adj.—  Npa.:  fehlt—  ')  Hier  sfiür  geichr.
•  j.  spaetini-  fem.  Adj.  'weiss,  weisslich': upa  •«(■/(AP.)  raiurä  Yt.15.ii;  —  •««" larpmil  sispimnS  Ytig.6j.
Vgl.  spaätita-  Adj.,  zu  dem  es  das  Fem.  bildet,
•  j.  spaka-  Adj.  'hundeartig,  Hunds*'; aHaam  •kanam  kahrpunanam  (sd.)  V. 14.  S-
Ableit.  aus  '^n-.  —  Vgl.  HSRODOT  i.  izo! Bnäita  T^  KiJvB  miWiMis*  Ol  M^u  —   Pü.:  sah.
•  j.  spaxStay-  f.  'Spähen':  'Hm  F. /2.
KompE.  —  Zum  V.  sfas-;  Tgl.  avajpailay-  f. Wegen   xU   (neben  H)   i.  %  86  tS-    —    Pü. :
•  j.  spa-ä^a-  Adj.  'zum  Hundegeschlecht
gehörig"':  hau  vispanam  ..  'ranqm  anya udra   upapa   "das   (ist  die  Strafe  für  die Tötung)  aller  . .  zum  Hundegeschlecht  ge- hörigen Tiere  ausgenommen   den  Otter, der  im  Wasser  lebt"  V.jj.  16. Pü,:  sak  tBxmak.  —  0  S.  "j/j«-*). j.  ". .  drujs  spaiti  di^ra  . ."  Vyt-JS. j.  'span- :  w(«-'>  m.  'Hund'*':  spänsm da%3m    .  .   az)m  yd   ahurS    maxds  
dby  Google
i6il
'span-  a.
spayaSra-
bis  hapta  nmSna  *pairi.talahi(%A.)  bavanX V./j.44f.;  43,  21,  ji;  —  xlval  man'hs\ sanB  {GS.)  %rä%nm{sA.)  kafta  sar>üa\ apTTTnäyükahe  V. /j.  45;  —  gahvam  ,.' ^rayqm  *baotdri ..  sanam  *baotdn  {sA.) V.J5.49*';  —  katärö  'xT  ayä  vthrkaya ja%wSJarS  *atghat..yak:a  spa  vfkrkahe (sd.)  ktnnaoifi  ya^a  yat  v?hrks  spa  V.  13.  \
paiti  irista  bazaiti  V.ij.g;  — spanaÄe'\ V.y.48  PüZ.;  —  Sing,  in  koUekL  SbnJ äal . .  ahe  tunanahe  . .  /rapi'iwS  (sd.)  spä  ! V.^.j;  —  taiHl  ya  bavainti  aos5.tarash .  .  yäha  anya  spa  V.  13.  42  (?).  a)  im Gegensalz  zu  Menschen  und  zu  andern Tieren :>'((/ii>4mi  spanasca  narasta  para.- irtiinti  V.5.  ij^.s,  u,  36,  8. 14;  —  yai ahmi  nmäne..spa
—  yS  s  Bne  pHtmn  jainti  yim  pasuLhmirve V.  y,  10;  11;  —  yB  spariam  jainti  yim pasui.hauruM  . .  V.  ij.  12;  14-16;  —  M'a asti  spa  pasus.haurvö  dailyff.gatuf'W.  13.1T, 18,  19;  —  yS  spamm  larspi'^w^m  *dasti yim  pasus.haurum  V.  y.  20;  21- yS  siine  yim  pasusJiaurve  vä  visMaurve va  astanqm  ahmar^tanqm  daaaitiW.i^.y,
—  dva  mii  apa.ra^ayaita  yasca  spa pasuLkaurvU  yasla  spa  vHJtaurvS,  nBit  ml nmamm  vilatö  hiä?nti  .  .  yat  mg  mit inkat  spä  pasulAaurvd  va  vis.haurvB  vä V.  13.  49.
♦)  Die  GaHung  'Hond'  umfasst  in  der  awcsti- ■chen  Zoologie  auch  den  Igel,  du  Stachel- Bchwein,   den  Otlei  D.r;    *.  die  ersten  Stellen
1612
aiiler  A  und  la  ifiac&ra..  Bd.  14-  19  kennt zehn  Arten  der  Hundegaltung.  S.  noch  Ne.  3ff. KompA.  (s,  sj>a°,  spä.',  tfiö.');  Ableit.  (i. auch  ipäiia').  —  Vgl.  lüiü-.  —  ai.  ivä, Jünai  j  afy.  ifai,  np.  vgl.  la^.  —  Pn. :  lai,  — >}  NA.  hat  immer  »;  aber  die  Hds.,  beion- ders  L4  und  K  1  bieten  oft  h,  S.  an  lunT-.  — >)  Theio.  
•  j.  'Span- :  jßH-  m.  'Spinne';  te  sBnS ma%axas{5d^)äi  aogasdastima  bavaitiii  V. 7.  a6;  —  nSi^  *mairyehe  neil  jahikaya  nsii süns  ..  P.io.
Aus  idg.  *.KA{n)ii/H;  eig.  'der  (beim  Weben oder  im  Gewebe)  hin  und  herschiesst'.  Vgl. zBed.  West  SBE.  j/.  158;  Dk.  *.  133  hat dafür  laaaHd,  in  np.  /anldan  'spinnen';  5.  Pö. —  VgL  lil.  s:äuü  'schiesten',  iiaudyili  'Weber- schiffchen' usw.  —  Pü.  (in  V.);  aJh  (in  Aw.- Buchst;i.  auchV. /.  14;  statt  in nd^/dniHi/: i.  o.),  (zu  P):  sai  'Hund'. j.
haoma   nmand.paite   . .    'tiauha   *vae(tyä.-
```


## [2026-09-06T22:36:32.440Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '26830,26850p' BRT.txt | cut -c1-700"
}
```


### [2026-09-06T22:36:32.497Z] TOOL RESULT

```
haoma   nmand.paite   . .    'tiauha   *vae(tyä.-
paite  Y.5.  27,
Ableil.  —  lEt,  s.  sfinia-.  —  Vgl,  spJnaA-.— Vä.:  aiBzürtiiTA i  s.  zu  sfinta-,
j.  spanah'vant-  Adj.  'heilig,  sanctus', on  AAura:  das?mB yat  ahmi  spanö  atvan- dasB  'naauha  Yt.  /.  8.
Pü.;  *awzi)'luUiir,  erl.:  ha^  aniiai  Hl  vas  Hc afe  a^uzäyhilm.
•  j.,  g.  spanyah-,  spainyah-"  Adj.  'der beiligere';  i)  von  Göttern:  mainyü  . . yaya  'yä  uHl  mrava^  ySm  angnm  "von den  beiden  Geistern  . .,  von  denen  der heiligere  also  sprach  zu  dem  aigen"  Y. 43.  i;  —  frä  mi  "yh  *maimva  vavaia vispqm  aiaonB  stTm  Y.  ig.  9.  2)  von Menschen:  ava^a  ^ankä  'yä  yai  mqm paiti.p)r)sar3he  "so  wirst  du  heiliger  werden, wenn  .  ."  V. /<?.  7;  —  ''poumjiartm  tBm kirMBsi  "yaalum  V. /o.  13".
Kompar.  zu  sptnta-;  sd.,  auch  zEt  —  mp. spenäk  (mit  i  aus  ar.  aiyj.  —  Pü.  {lu  V.): awiütäilum,  (sonst):  miiaünli,  fa  aaaüniiiA.  — ')  Mit  sfaiii'  nur  Y.  10.  13.
•  g.  spayaOra-  n.  'Gedeihen,  Erfolg, Glück':  ada  sl  ava  drüjö  [ai/j]"  bai-aitl skgndB  '%rahya  a^  asiitä  yaojaittl  (sd.)  . . yBi  sasmil{sü.)  vatihau  sravakS  "alsdann ja  wird  fiit  die  Welt  der  I>rug  die  Zei^ Störung  des  Glücks  erfolgen '>,  aber.." Y.^.  10.
Zu  einem  Praei.  ir.  *{^d- gebildet  3>,  in  ^m ar.  *ii/aia-  Pracs.  24  -  in  imi;  Sp.  1 56 1 0  - and   *ifiA^a;   Praes.  4  oder  37  —  id  i^fä-  -
db,Google
i6i3
spar-
lusammengefallen  sein  kännen.  —  PQ. :  späh 'Heer'  -  Sü. ;  'paläkmikah  -,  wegen  des  Ad- klangs.  —  ')  S.  bav  No.'  14.  —  »)  iSt.  vgl.  Y. $3.  6  unter  fräday.  —  3)  Wie  ai.  gäyalri-, täruira;  iritidlra--a.a.;s.  nochNo.4.  —  4)  Dann vll.  mit  ai.  svälrä-  n.  {im  Nsigh.  'ähanam',  bei Olsenberg  SSE.  46.  26  'power')  lusunmen- gebörig,  das  ein  ar.  Praes.  21  'sgä-  voraus- setien  würde,  oder  -  was  das  selbe  ist  -  eine 'WurielcrwcileninB'  durcli  li;  vgl.  !irv:Ara:
•  j.  Spar- V. 'schnellen,  treten'.  Praes.  3'»
1)  'treten,  stossen';  ma  %wä  dasna mäzdayasnii  aspake  sparSit  sparmaini  (sd.) Vyt..?5-
mit/r,j  'hervorschnellen',  intrans.: /wj (sd.)  aya»h5  frasparai  Y.p.  11.
mit  Vi  'auseinandertreten,  -stampfen'; aiAhh  z^mS  (sd.)  pasnäbya  vTspara  V, 2.31;  32  {wo  visparai).
ai.   ifharäüi     np.   lipardaa.     —     Fü.  (dRn.) :
laiigandaH,   spiirtan,   sfarlan.    —    ')  So  nach
dem  ai.  Praesens.
•  j.  sparaj-a-  m.  'Spross',  von  den  Wider- haken unterhalb  der  Pfeilspitze:  asti  yä *ayat3kama  °ya  "es  kommt  vor,  dass eiserne  Sprossen  (dran,  am  Pfeil)  sind" YLjo.  129  Gl.
```


## [2026-09-06T22:36:43.335Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '26850,26920p' BRT.txt | grep -n \"Heer\\|spä\\|spa.a-\\|spSSa\\|Kriegs\" | cut -c1-500"
}
```


### [2026-09-06T22:36:43.398Z] TOOL RESULT

```
8:Zum  V.  spar;  —  Pü. :  a:iij;aniin.  —  •)  Nach  Pü. (laagih)  gehörte  aspaht  lu  'aspä-.
12:•  j.,  g.  'spas-  V.  'spähen'.  Praes.  s hispas-,  10  '^spasu-Q)'^,  11  spaln-,  26 sparya:   —    PPfP.    'spasta-.  [S.   noch
14:1)  'hinspähen  auf—,  beobachten,  aus- spähen nach  — '  (Akk.);  spass  . .  mt^rahe *mikrS4rtijim  *hisps.s»mna''>  Yt/0.45; —  vispsng  anySng*mainy}us  spasya  dvaßa- nka  "alle  andern  beobachte  ich  mit  Feind- seligkeit des  Geistes"  Y.  44~  1 1 ;  —  tUlrJm .  .yim  ..  *uzyS.r>nt>m  *hisps.smti'^i'*  "den T.  . .,  nach  dem  sie  ausspähen,  wenn  er im  Aufgehen  ist"  Vt.  8.  36,  2)  'Acht haben  auf-'  (Akk.):  sraohm  ..ys äxsHüca urvaitiica  drujö  spasy
15:mit  aoi  und  ava  'erspähen':  nSit  dim  . . drva  .  .  ava.spa/tiäna  aoi  *ava,spasnsiti> "nicht  soll  ihn  der  Ketzer . .  durch  keinerlei Erspähen  erspähen"  Yt  11.  5.
24:SU/S;    Pü.:  päspänlh.     Zuletit   hierüber  Gdn.
33:Fl,  aber  Pü.:  päspäitrnit.     Geringe  Stelle.
35:Zum  V.  spas-.  —  ai.  späi-  m.
36:•  j.  spasan-  Adj.  Iiinspähend  (auf  — )';
54:Zum  V.  ipas:  —  lat.  'sptctor.  —  PS.;  pispän, erl.  1  hl  ääm  rat  fäsjiäyem.
55:•  j.  'spä-  V.  'iacere'',  abicere'.  Praes.  17 spaya-,  j-Aor.  i  ipak-. —  PPfP.  'spata-, PFP.  pfkwa--''>.
56:'wegwerfen  sva.  wegschaffsD,  -nehmen, beseitigen,  tilgen':  *'spayätP  zT  . .  daena mäxdayasnis  nars  ästavanahe  bandim  .  . anap3r?%;mt  Radium  ..  *dintänsp)r3^gm /Jran(sd.)..V.j.4i;  43  PüZ.*",  *N.J/J>; —  altücij  {Sp.  591  m.)  asidyS  *späf»Aaiti äslavanalibyS  . .  V.^j.  40.
64:fen': pascaSa  dls  fraspayeüi  mihrg  .  . pancataynäi  satcrfnaii'ca  .  .  Yt  JO.43. EL?  —  S,  noch  pairi.späiay:  —  Pä.:  infgati- dan,  Npü.  (in  Vt.  T^:  a/gandan,  —  <)  Gl>N. BB.  17.  99  hat  fairijpatay-  und  ufotrLtpäfa- ausser  Acht  gelassen;  s.  aach  naiuspä-.  — >)  S.  die  Bern,  data  im  Ntc.  —  3)  Ea  Uetit hiei  nur  das  Wort  ifaytiü;  offenbar  wird damit  auf  V.  j.  41  angespielt.  —  4)  Hds. •sfalä.
67:•  j.,  g.  ^spä-  V.  'proficere'.  Praes,  lob spanv-,  spsnv-.
70:•  g-  (.  3)  'spä-  n.  'Gedeihen,  Glück': t}m  .  .  ys  tis  w}n  (Sp.  405  u.)  hsr^i  ipsn- (kV.)cä  aspsncä  Y.  4$.  9.  a)  im  eschato- logischen  Sinn  (nur  Ableit).
71:KompE. ;  Ableit.  —  It.  *ipä;  worin  ar.  *ij^ -  lu  aea/;  Sp.  1561  -  und  *sphä-  -  s.  ispä-  - znsammengef allen  sein  können;  t.  zn  ipaya- %ra-.  —  iPB. !  ätäHih,  Sü.t  samädkänam.  — •>  Die  Meinung,  es  mDsse  des  Melrnins  hilbei jwf  •  statt  sf  gelesen  werden  -  Bthu  Gi^is  ' 9  -,  was  die  Herleitong  ans  ar.  *j^ilä-  aus- schlösse, ist  irrig.
```


## [2026-09-06T22:37:05.117Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v2 leaf ~612 (p1155) ===\"\npython3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint('nleaves',len(leaves))\nfor i in range(608,617):\n    l=leaves[i]\n    head=l.strip()[:300].replace('\\n',' ')\n    print('---',i,head)\nEOF"
}
```


### [2026-09-06T22:37:06.685Z] TOOL RESULT

```
=== BQT v2 leaf ~612 (p1155) ===
nleaves 684
--- 608 ‫=‪— 4‬‬                                                                                                      ‫سفته گوش‬ ‫سید ‪ 1‬ے بکراول وفتح ثالی وسکون‬                               ‫چیز که سر آنرا ایزکرده باشند هم هست ؛‬   ‫دال ابجد‪.‬بمعنی سپد است که زمین باشدوبعربی‬                   ‫و باين 
--- 609 ‫سفد کاسه‬                                                                                                ‫ع—‬                                                                                                           ‫\\‬‫ی‬   ‫تقیض میاه باشد و بعربی ابیض خوانند کونابه‬                         ‫‪۰‬‬
--- 610 ‫بیان شانز دهم‬              ‫درسین بی نقطه با قاف مشتمل بر بست و هفت لغت و ابت‬                                                                                                    ‫سقاقلوس ‪-۱‬‬                                                                                                     ‫جفتح
--- 611 ‫کسهت‌آسمان باشد‪.‬‬                                    ‫لاجورد ا‬                                          ‫ستسیی‬                                                      ‫باسین بی نقطه بروزن‌قز وین»‬ ‫است ‪-‬‬    ‫آزسمان‬               ‫سقف مینا = کنابه ا‬                                        ‫نام 
--- 612 ‫==‬                                                                           ‫سقلاطرن‬  ‫بلغت بونانی‌دواییاست کهآ درا محمودممی‌گویند»‬                                                      ‫سقلا طون ‪ ۲‬ب=روزن افلاطون‪.‬بمعنی‬  ‫وآن عصاره‌ای باشد بغایت نلخ ومهل‌صفرابود ‪.‬‬          ‫جتا‪-‬موة تخجو
--- 613 ‫‪۷۱۷ 6-‬‬  ‫و شروع بحر کنند تاآترمان کهاقطة خونی‬                ‫‪ ۰ ۲‬بفتح اول وض‌نانی‬           ‫سقوردیون‬  ‫در میان قدح آب پیدا شود و بمداز زمانی آن‬            ‫وسکون واو و رای قرشت و کسردال ابجدونعتالی‬  ‫ردد و آن شخص‬     ‫قدح پر از دل وجکر وکشش‬                                             
--- 614 ‫‪۱‬‬             ‫= هی‬                                                                                                                ‫صکاد‬ ‫بروزن خلاصه » نمعتی سکاسته است که‌خاریشت‬                                     ‫‌نهنده‬       ‫ت سخ‬‫سعنی‬                                                   
--- 615 ‫رککه‬          ‫س‬  ‫ووحه‪.‬‬      ‫کنند و هروقت که خواحند صر فکننده‬                         ‫کار صازی‬    ‫و‬       ‫‪-‬‬   ‫وخواستن‬        ‫و آندیشه مند بودن‬   ‫نسیك‌سر که وبا‬              ‫معچه‬                 ‫بست‬                   ‫تمیه‌اش سرکه با‬                                   ‫فارس
--- 616 ‫‪۷‬‬       ‫‪ ۷‬ی‬   ‫سکسکی = یم هردو سین و سکون‬ ‫ثالی و رابع بتحتانی کشیده ‪ .‬زحمتی باشد که‬                                                         ‫ارزن سازند ‪. ۱‬‬ ‫آدمی را در غات ضعف پیدا میشود‪.‬و آن طیش‬         ‫سکره ‪ = ۴‬نم اول و تخفیف کاف بر‬   ‫دلی است که باندك جنبشی وحر کتی بهم رسد‪
```


## [2026-09-06T22:37:12.541Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in range(616,624):\n    print('---',i,leaves[i].strip()[:600].replace('\\n',' '))\nEOF"
}
```


### [2026-09-06T22:37:14.296Z] TOOL RESULT

```
--- 616 ‫‪۷‬‬       ‫‪ ۷‬ی‬   ‫سکسکی = یم هردو سین و سکون‬ ‫ثالی و رابع بتحتانی کشیده ‪ .‬زحمتی باشد که‬                                                         ‫ارزن سازند ‪. ۱‬‬ ‫آدمی را در غات ضعف پیدا میشود‪.‬و آن طیش‬         ‫سکره ‪ = ۴‬نم اول و تخفیف کاف بر‬   ‫دلی است که باندك جنبشی وحر کتی بهم رسد‪.‬‬           ‫وزن سفره ‪.‬کاسه‌ای راگویندکه از سگل‬                                                  ‫اخته‬ ‫سکسنبو يه ‪ = :‬بفتح اول و سکون‬                  ‫باشند ؛ و با تشدید کاف هم گفته‌اند ؛ وضم‌اول‬ ‫ثانی وسین بی‌نقطةٌ مفتوح باون زده وبای ا‪.‬جد‬            ‫و فتح انی و ثالث مشدد هم‌آمده است
--- 617 ‫سکوا‬                                                                                                        ‫هه‬       ‫سن‬   ‫سکنگیین ‪ = ۹‬باکاف فارسی » بروزن‬                          ‫ثالی حردو آمده است ‪ ,‬مضارع سکنجدن باشد‬    ‫و معنی ‪-‬کلجبین‌است» وآن کمبری‌است کهاز‬                  ‫یعتی بتراشد ‪ -‬وبگزد ‪ -‬وسرفه کند ؛ و بکر‬  ‫سر که وعسل پزند بجهت دفع صفراوبلفم‪,‬چسك‬                                                                                           ‫‪۰‬‬        ‫اول وثالی وت‬    ‫که وانگین عل را کویند‪.‬وسکنجبین‬                                     ‫معرب‌آنت ‪.‬‬         
--- 618 ‫اه‬       ‫هی‬                                                                                                                 ‫سکوبا‬  ‫وره‌ومس‬        ‫است ‪ -‬ودرعربی لقشی که برروی طلا نف‬                                                                     ‫سکو با ‪ » ۱‬منم اول وثائی وبای ابجد‬  ‫وبند که نقش‌زر‬               ‫گز‬‫رایج باشد ‪ - ۷‬وآهنی را ی‬                            ‫بالف کشیده ‪ ,‬لام عایدی است صاری که دبری‬ ‫ننده باشند ‪ -‬وآحتیکه زمین‌را‬ ‫رابج را بکرآ‬                                                                     ‫ساخته بود و بناماو مشهور شد ‪ .‬کوبند عیسی؟‬ ‫ب
--- 619 ‫=‬        ‫ع یو‬                                      ‫باشد ‪. ۴‬‬       ‫سکیزیدن است بعنی جت و خیز کند و آلیز‬                                                                                                          ‫الدازد‬ ‫سکیز یدن‪ -‬بروژن ستیز یدن » بمعنی‬ ‫جت وخبز کردن ‪ -‬وجفته وآلیز انداختن‌ستو؟‬            ‫سکیژ فده «بروزن ستیزنده ‪ ۰‬بمعنی‬                                     ‫باشد ‪. ۵‬‬                 ‫اسب ر استر حجهند ه ولگد اندازه باشد‪.‬‬   ‫سگیله‪. ۱‬با تعتانی مجهول بر وزن‬                      ‫سگیز ‪ ۵‬؟ = پرورن‌سنیزه » بمعنی‌جست‬ ‫جمیله » بممنی جتن گلو باشد و بعربی فواق‬ 
--- 620 ‫‪—۱‬‬     ‫تن‬                                                                                                                 ‫سگال‬                                                          ‫آبی است» وآن حیوالی باشد که آش بجگان‬  ‫وه بالف‬        ‫سگان ابزک‪-‬ر نوهنمز‬ ‫»نابه ازطالبان‌ دیا‬                   ‫کشیده و بزای نقطه‌دار زده ک‬             ‫وجندبی دستر ازو بهم میرسد واورا بتازی قضاعه‬                                                                                               ‫خوالند ‪.‬‬                                       ‫راهل حرص باشد ‪.‬‬  ‫است که‬     ‫داروبی‬    ‫=‬     ‫
--- 621 ‫—‬       ‫پوي‬    ‫آنجا وافم شده است وآنرا سگزی ازآن‌جهت‬                          ‫و رفتن؛وباین معنی‌باشین لقطه‌دار هم آمده‌است‪.‬‬                                                 ‫‪7‬‬                ‫سگ جان ‪ -‬بر وزن مرجان » بمعنی‬                                                                                  ‫سخت جان وسختی کش باشد ‪.‬‬ ‫سگزن ‪ -‬بفتح اول بروزن رگے زن »‬  ‫لوعی از تکیروچك باشد وییکان آن بفابت‌باريك‬                                         ‫وتیز میباشد ‪.‬‬           ‫که سخت جان ومحنت کش باشد ‪ -‬ومردم‌غردل‬                                                                
--- 622 ‫=‬‫)وی‬‫‪-‬‬   ‫میگونند که حر کس آنرامیکند میمیرد » پس‬                    ‫=روزن سیتان »زاباتان‬                                                                               ‫سگستایت ‏‪ ٩‬ب‬  ‫بوقت کندن اطراف آنرا خالی کنند طونابی‬                       ‫باشد که سیستان امت ومعربآن سستان‌بود‪.‬‬           ‫آورند کر آبرا قن کر‬                                                             ‫وکون‬                                                                ‫‪۲‬ن‪-‬تم اول س‬                                                                          ‫سگسنبو له ب‬   ‫واد»‬      ‫دت‬‫بند‬          ‫
--- 623 ‫سلشوق‬                                                                                               ‫‪۱‬‬                                                                                                       ‫س‬ ‫اهی‬   ‫باشد بمقدار فلفل و آن سرخ و سياه رنگهدیز‬               ‫بی قضاعه گوبند و خصيةٌوی آش‬                                                                                  ‫بانعندر و‬                                                                                          ‫خو‬  ‫میباشد و بتازی‌عنب‌التعلب کوبند ‪ -‬ودرفرهنگه‬                       ‫مجگان است که جند بیدستر باشد‪.‬‬
```


## [2026-09-06T22:37:23.916Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"spaka\\|sag\\b\\|saka\\|spā\\|spah\\|sipāh\" BQT_v2_pages.txt | head -20\necho \"=== try ref_page tool ===\"\npython3 tools/ref_page.py BQT:1155 2>&1 | head -40"
}
```


### [2026-09-06T22:37:25.943Z] TOOL RESULT

```
=== try ref_page tool ===
python3: can't open file '/home/sfmqrb/git/rishe/data/verification/sources/refs/tools/ref_page.py': [Errno 2] No such file or directory
```


## [2026-09-06T22:37:27.808Z] TOOL CALL #25: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:1155 2>&1 | head -60"
}
```


### [2026-09-06T22:37:29.547Z] TOOL RESULT

```
no scan of BQT covers printed page 1155 (see 'scans' in refs_online.json)
```


## [2026-09-06T22:37:34.645Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -c \"\\[pdf page\" BQT_v2_pages.txt\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nimport re\nfor i in range(605,630):\n    l=leaves[i]\n    tag=re.findall(r'\\[pdf page \\d+\\]',l)\n    # persian digits\n    fa=re.findall(r'[۰-۹]{4}',l)\n    print(i,tag[:1],fa[:8])\nEOF"
}
```


### [2026-09-06T22:37:37.199Z] TOOL RESULT

```
0
605 [] []
606 [] ['۹۹۲۱']
607 [] []
608 [] []
609 [] []
610 [] []
611 [] []
612 [] []
613 [] []
614 [] []
615 [] ['۹۹۲۰']
616 [] ['۲۷۲۰']
617 [] []
618 [] ['۱۲۰۰', '۰۰۹۱']
619 [] ['۱۲۶۲']
620 [] []
621 [] []
622 [] ['۳۸۵۲']
623 [] []
624 [] ['۱۲۱۰']
625 [] []
626 [] ['۰۸۲۰', '۸۵۷۰']
627 [] []
628 [] ['۵۹۱۱']
629 [] ['۲۲۹۲', '۶۹۱۱']
```


## [2026-09-06T22:37:45.965Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfa='۰۱۲۳۴۵۶۷۸۹'\ndef tonum(s): return int(''.join(str(fa.index(c)) for c in s))\nfor i in range(560,640):\n    l=leaves[i]\n    cands=set()\n    for m in re.findall(r'[۰-۹]{4}',l):\n        cands.add(tonum(m)); cands.add(tonum(m[::-1]))\n    good=sorted(c for c in cands if 1000<=c<=1300)\n    if good: print(i, good)\nEOF"
}
```


### [2026-09-06T22:37:47.886Z] TOOL RESULT

```
565 [1012]
570 [1167]
571 [1110]
572 [1109]
588 [1127]
589 [1129]
592 [1220]
594 [1133]
595 [1132]
597 [1139]
602 [1139]
606 [1299]
618 [1200]
619 [1262]
624 [1210]
628 [1195]
629 [1196]
630 [1006]
635 [1253]
638 [1030]
```


## [2026-09-06T22:37:59.299Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in range(614,623):\n    l=leaves[i]\n    lat=re.findall(r'[A-Za-z]{3,}',l)\n    print(i, lat[:25])\n    if 'سگ ' in l or 'سگ' in l:\n        idx=l.find('سگ')\n        print('   ...',l[max(0,idx-100):idx+300].replace('\\n',' '))\nEOF"
}
```


### [2026-09-06T22:38:00.954Z] TOOL RESULT

```
614 ['YEY']
   ... کاسته ‪.‬‬             ‫‪۸‬‬         ‫ر دکربت‌آید‬             ‫‪۴‬‬                ‫‪.‬‬    ‫رك‪ :‬سگال‬     ‫‪- ۱‬‬               ‫سکافره ‪.‬‬     ‫رك‪ :‬شکافه »‬        ‫_‬       ‫سکالش(ه‪.‬م‪).‬اسم‌مصدراز «سگالیدن»‪.‬‬                         ‫‪“۴‬‬         ‫رکه‪:‬گالیدن‪.‬‬         ‫همحون‪ :‬ند سکال (بدسکالنده)‬ 
615 []
   ...          ‫اس ‪:‬‬         ‫نة‬                                                                     ‫سگالیده ‪ - ۴‬بر وزن خراشیده »‬ ‫سکج = بفتح اول و کر الی وسکون‬                                             ‫بمعنی فکر واندیشه و کفتگوکرده باشد ‪.‬‬ ‫باشد‬       ‫وآن انگوری‬        ‫را گونند ‪٩‬‏ _‬            ‫جنم ‪ +‬هویز‬                      ‫سازند‪.‬‬       ‫که در |فتاب یا سابه خغك‬           
616 []
   ... ف کاف بر‬   ‫دلی است که باندك جنبشی وحر کتی بهم رسد‪.‬‬           ‫وزن سفره ‪.‬کاسه‌ای راگویندکه از سگل‬                                                  ‫اخته‬ ‫سکسنبو يه ‪ = :‬بفتح اول و سکون‬                  ‫باشند ؛ و با تشدید کاف هم گفته‌اند ؛ وضم‌اول‬ ‫ثانی وسین بی‌نقطةٌ مفتوح باون زده وبای ا‪.‬جد‬            ‫و فتح انی و ثالث مشدد هم‌آمده است ‪. ۴‬‬  ‫بواو رسیده وفتح نحتالی » لفتی است رومی
617 []
   ...                              ‫« مود الفصلاء» ‏ ‪. ۱608۷0‬‬                                  ‫؟ رك‪:‬سگرنه‬       ‫و ‪۷۳۱‬‬        ‫«رشیدی» ‪ -‬خاریشت ‪ ۰‬تشی «لت فرس ‪٩‬‏‬                                           ‫سکیا (هم‪۲ ).‬‬      ‫=‬     ‫‪۹‬‬             ‫سکوی(ه‪.‬م‪).‬‬             ‫‪۸‬‬ 
618 ['TAT', 'igas', 'enyaP']
   ...                       ‫شیر را ببندد ‪.‬‬        ‫درخت و امثال آن‬            ‫دخراله و بیاغابوهای‬ ‫سگیزژ * » بکر اول بر وزن ستبز ‪۰‬‬                                                                                  ‫باشد ‪.‬‬  ‫بمعنی برجستن ‪ -‬وآلیز زدن و جفته انداختن‬                            ‫سکو بنه * ‪ -‬ختح ارل و کر الك »‬    ‫ختیوز‬  ‫ستور باشد ‏ و بمعنی جهنده و ج‬          ‫‪ -‬و امر بد
619 ['hes', 'sipl', 'esp', 'esb', 'psA']
   ...                            ‫باشد ‪. ۵‬‬                 ‫اسب ر استر حجهند ه ولگد اندازه باشد‪.‬‬   ‫سگیله‪. ۱‬با تعتانی مجهول بر وزن‬                      ‫سگیز ‪ ۵‬؟ = پرورن‌سنیزه » بمعنی‌جست‬ ‫جمیله » بممنی جتن گلو باشد و بعربی فواق‬            ‫و بمعنی‬    ‫و خیز و لکد انداختن ستور باشد ‪- ۴‬‬                                     ‫کوشدی‪.‬‬           ‫ولحاجت‬    ‫و خصومت‬   ‫که جنك‬    ‫هم آمده‌
620 ['dnaw', 'kaS']
   ...                                                                                                    ‫سگال‬                                                          ‫آبی است» وآن حیوالی باشد که آش بجگان‬  ‫وه بالف‬        ‫سگان ابزک‪-‬ر نوهنمز‬ ‫»نابه ازطالبان‌ دیا‬                   ‫کشیده و بزای نقطه‌دار زده ک‬             ‫وجندبی دستر ازو بهم میرسد واورا بتازی قضاعه‬                              
621 ['shkun']
   ...                                                         ‫—‬       ‫پوي‬    ‫آنجا وافم شده است وآنرا سگزی ازآن‌جهت‬                          ‫و رفتن؛وباین معنی‌باشین لقطه‌دار هم آمده‌است‪.‬‬                                                 ‫‪7‬‬                ‫سگ جان ‪ -‬بر وزن مرجان » بمعنی‬                                                                                  ‫سخت جان وسختی کش باشد ‪.‬
622 []
   ... روزن سیتان »زاباتان‬                                                                               ‫سگستایت ‏‪ ٩‬ب‬  ‫بوقت کندن اطراف آنرا خالی کنند طونابی‬                       ‫باشد که سیستان امت ومعربآن سستان‌بود‪.‬‬           ‫آورند کر آبرا قن کر‬                                                             ‫وکون‬                                                                ‫‪۲‬ن‪-‬تم اول س‬
```


## [2026-09-06T22:38:17.141Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nl=leaves[619]\nfor m in re.finditer(r'[A-Za-z]{2,}',l):\n    print(repr(l[max(0,m.start()-120):m.end()+60].replace('\\n',' ')))\n    print('---')\nprint(\"=== leaves 543-552 heads ===\")\nfor i in range(543,553):\n    print(i, leaves[i].strip()[:200].replace('\\n',' '))\nEOF"
}
```


### [2026-09-06T22:38:18.631Z] TOOL RESULT

```
'\u202c                \u202b\u202a۹\u202c\u202c                                                                         \u202bارعنی \u202a001S\u202c\u200f \u202a .\u202cکردی \u202ahes\u202c\u200f\u202c                                                         '
---
'         \u202bارعنی \u202a001S\u202c\u200f \u202a .\u202cکردی \u202ahes\u202c\u200f\u202c                                                                         \u202b\u200f)\u202a( (se\u202cسکد) \u202a +\u202cجمم\u202anûs\u202c\u200f «\u202c                                      '
---
'اففغانی\u202a٩12۳\u202c\u200f \u202a.\u202cکاشانی\u202c              \u202b\u202a0\u202c\u202c                                                                         \u202b\u200f\u202asipl . espê, esbé4\u202c\u202c                                            '
---
'\u202a٩12۳\u202c\u200f \u202a.\u202cکاشانی\u202c              \u202b\u202a0\u202c\u202c                                                                         \u202b\u200f\u202asipl . espê, esbé4\u202c\u202c                                                  '
---
'\u200f \u202a.\u202cکاشانی\u202c              \u202b\u202a0\u202c\u202c                                                                         \u202b\u200f\u202asipl . espê, esbé4\u202c\u202c                                                        '
---
'                       \u202b\u202a۳\u202c\u202c                                                                         \u202bص\u202a .* ۷۸۲\u202cسمنانی \u202apsA\u202c\u200f \u202a.\u202c\u202c                                                     '
---
=== leaves 543-552 heads ===
543 ‫—‬   ‫‪0‬‬   ‫سیزیوشان بهشت‬   ‫سپژ پا= با بای فارسی‌بالف کشیده»مردم‬              ‫گوبنذ سرمه کشیدن از میلی کهشبه (‪ )۱‬باشد‬                   ‫شوم فدم و دامبارك پی باشد‪.‬‬       ‫روشنامی جشم را ز
544 ‫‪ ۷‬با ‪— ۵‬‬   ‫گ بروزن نفزك‪ .‬مصفر سبز باشد‬                           ‫سپز ل =‬                            ‫یکه‬                                                                ‫ابه‬              
545 ‫ره باس‬  ‫سر کوه وقلهٌکوه باشدب وفرق‌سررا لکیفزتماند‬            ‫معروفت که منوب ببز باشد همچون سیاهی‬  ‫سیکیار » بختماول و بای ابجد بالف‬                      ‫وسقیدی کهمنوب بسیاه وسفید است ‪ -‬وسبز
546 ‫زا‬                                                                                        ‫سبك صابه‬                            ‫بدان زمین ودیوار کنند‪.‬‬             ‫اهبه از فرومایه و سفیه باشد چه
547 ‫سڀار‬                                                                                          ‫سوه =‬ ‫سبو شکستن ‪ -‬کنابه از نومید شدن‬                       ‫پبوست مزاج درسآدمی پیدا میشود دورآابمر
548 ‫رک ها‬  ‫گوبند « سپای دارم»‬                   ‫که‬‫نست‬                                          ‫ام ه‬                                             ‫نه‬‫چمنت‬                                        
549 ‫==‬                    ‫براه رو و پایمال کن ‪۰‬‬     ‫نی‬                ‫ا ف وشکوه رشان وعوکت ا‬ ‫سیر قآشیی ‏ بكر اك ‪.‬کنایه از‬                          ‫سبتاك ‪١‬‏ ۔ بکر اول و فوقائی بالف‬       
550 ‫س‪۵‬‬       ‫ایز‬                                                                                            ‫مه رده‬    ‫کاو میش سازند و آن فم سپر دو هندوسان‬                      ‫لمودن ‪ -‬و پایما
551 ‫ها‬   ‫رسیدہ باشد ‪ - ۱‬و بمعنی پایمال دولچیز حم بی‌نقطه بروزن بسباره بمعنی دلال است که‌یعریی‬                                                     ‫هت ‪ -‬وتیر تخمار را نیز کوبند ‪ ,‬وآن تیری‬ ‫سیست 
552 ‫‪¬ 40‬‬   ‫تس‬                                                                                                                    ‫سیٍکاد‬   ‫وآن‬    ‫است »‬         ‫رلوف‬                     ‫سينك
```


## [2026-09-06T22:38:28.909Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in (547,548):\n    l=leaves[i]\n    print('=== leaf',i)\n    print(l.strip()[:1500].replace('\\n',' '))\n    print('LAT:',re.findall(r'[A-Za-z]{2,}',l))\nEOF"
}
```


## [2026-09-06T22:38:30.474Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint('n',len(leaves))\nfor i in range(325,345):\n    l=leaves[i]\n    lat=re.findall(r'[A-Za-z]{3,}',l)\n    print(i, l.strip()[:150].replace('\\n',' '), '|LAT', lat[:10])\nEOF"
}
```


### [2026-09-06T22:38:30.789Z] TOOL RESULT

```
=== leaf 547
‫سڀار‬                                                                                          ‫سوه =‬ ‫سبو شکستن ‪ -‬کنابه از نومید شدن‬                       ‫پبوست مزاج درسآدمی پیدا میشود دورآابمربی‬ ‫وا امیدگردیدن ‪ -‬وشراب ریختن‪ -‬ومنع شراب‬               ‫کوبند بفتح خحای بی‌قطه (‪ )۱‬وزای شطه‬         ‫حزازه‬                                   ‫کردن باشد ‪#.‬‬                                                     ‫دار ‪ -‬وریز چوب را لی کوبند که ازدم ارمچدا‬ ‫سییوش ‪ -‬بکر اوسلکوون الى‬                            ‫شود ‪ -‬وسبوس‌آرد کندم وجو رالیز گفته‌اند ‪۱۰‬‬ ‫نقطه‌دار زده » تنم‬       ‫ن‬                          ‫یو‬‫شیده‬                               ‫بو کش‬                                   ‫توحتالی بوا‬               ‫اسبغول امت که بعربی بزرقطوها گوشد‪.‬‬       ‫‪-‬کرمی باشد که در ابار گندم وجو افند‪.‬‬  ‫و‬                                                 ‫بیان سوم‬             ‫در سین بی‌نقطه بابایفارسی مشتمل برهشتاد وهشت لفغت و کنامت‬    ‫ندووا‬        ‫آارن‬           ‫حووضیکه درآن شیر انگور بفش‬                 ‫سار = بضم اولبروزن دچار ‪,‬آهن‌جفت‬  ‫بعربی معصر خوانند ‪ - ۴‬و مطلق ظروف واوالی‬           ‫راکوبند وآن آهنی باشد سرتیز که زمین‌بآن‬  ‫راکوبند عموماً » وظرفیکه درآن الگور کرده‬                                                      ‫شیار کنند ‪ - ۴‬و بکسر اول‪,‬اسباب و مایحتاج‬ ‫ازجابی بجایی برند خصوصاً ؛ و باين ممالی تم‬ ‫ده امت خصوصاً آلات وادوات‌خانه ‪۴‬‬                                ‫اآولمهم‬               ‫وآلات وادوات خاله باشد ازهرنوعی ‪- ۴‬وچ
LAT: ['Henning', 'Sogdian', 'loan', 'words', 'BSOS']
=== leaf 548
‫رک ها‬  ‫گوبند « سپای دارم»‬                   ‫که‬‫نست‬                                          ‫ام ه‬                                             ‫نه‬‫چمنت‬                                                  ‫و‬                                                  ‫‪# .‬‬       ‫هت‬ ‫پعنی قبزل دارم و منت پذیرم ‪ -‬و بمعنی لطف‬                       ‫سبارو ‪ = ۵۱‬بفتحاولوالی‌بالف کشیده‬                       ‫است‪.‬‬     ‫نزآمده‬    ‫ومرحمت‬      ‫وشففت‬                                                                ‫وثالت بواو رسیده وبکاف زده » بمعنی کبوترباشد‬ ‫‏‪ ٣‬گرا اول‌رفتح رابع ‪:‬منت‬                    ‫سیاسه‬                                                                                        ‫وجربی حمام گوبند ‪.‬‬  ‫برکسی نهادن باشد ‪ -‬وبمعتی لطف لمودن‌وشفقت‬                      ‫آشاره‪,‬مخفف‬    ‫ولزن‬                                                                                  ‫راو‬                                                                                    ‫ببکر‬      ‫سیاره‬                                       ‫کردن هم هت ‪. ۵‬‬                                                                  ‫سی پاره است وآن بك جزو باشد اجزسزیو‬ ‫=کر اول بروزن قیاسی ؛‬                     ‫سیاسی ‪ 1‬ب‬                                         ‫و‬                                                                       ‫ک زا‬                                                                          ‫کلام خدا ‪ - ۴‬و بفتح اول کے‬                                        
LAT: []
```


### [2026-09-06T22:38:32.407Z] TOOL RESULT

```
n 777
325 << ۶+ )راد - یک اول بر وزن خبار » بن و تك آب را خوانند - و دستار را یز گویند - و هی چیز که بر پا یکشند مانند شلوار وتتبان و در عربی بممنی‌زن باشد که د |LAT []
326 از ذست ب رکرفتن یت و بود گردانیدن باشد . هوز بالف کشده , نان فطیر را گویند یمن بعنی نافی که خمیر آن نرسیده باشد . از دست دهرجستن - بستی از خر افتادن ا |LAT []
327 ما ارم » جح اول و سکون.تانی و میم » بنتی فد باشد ‏ ارمل س بر وژن جدول » بمنی بسیار وکثیرباشد. وصدا وآوازرا یز گومند - وبمعنی همه و مجبوغ هم آمده است ا |LAT []
328 اراد باشد ٩‏ - و کنابه از مردم شجاع و قهرآلود حم هت - ورایت و سرعلم را نیز گوبند ۴ - وپادشاه تال و ححاك ماراترا هم گفته‌اند ۴ . ادها « با کاف‌معنی آخر |LAT []
329 ۱ << رومی است . 1 2 بکویتد و باشیر تازه بیامیز ند وبرزیر خصه‌بمالند نموظ عجبآورد۱ اساسه بفتح نی رو اس : بمعتی نگرستن بگوشة چشم ووایس دیدن‌باشد ۴ وبکی  |LAT []
330 اسپخحول بکسر اول و سکون‌انی و بای فارسی مکور و خای نقطه دار حضموم‌بواو ولام زده » بععتی‌پیخال است که فضله وافکند گی اسیر ۱ س با بای فارسی بر وزن مهتر» |LAT []
331 فآ فا برگه زرد چوبه است - ودرخت خربزه را نیز گوبند . اسیر لو س « بالام وسین بی‌نقطه ووار مجپول بروزن کشورسوز » خانه وسرای پادشاحان و سلاطین و حکام را  |LAT []
332 قطونا باشد ۷ » و معنی ت رکیبی آن گوش اسب ۱ است ۰ چه غول بدمنی کوش هم آعده است ؛ وجط یکونند چون ب رکه آن بگوش اسب‌شبه و معنی اسفناج است » و آن سبزی باش |LAT []
333 26 ٩ ح ی 9 من - ۳۲6 وک در ۳ براء ء ‏ صعحه رر 9 اسفهان |LAT []
334 تست سس ات سس سوت سس منت سس اصنهان ترایز صقعةٌ ۱۲۳- |LAT []
335 اسیندار هف ۱ - بش میم وسکون ذال نقطه دار. بروزن ومعنی اسفندارمن است که مام دواژدهم باشد از سال شمسی - و نام روز پنبم بود از حرماه شمسی ؛ و فارسیان این |LAT []
336 ابجد و ظهور های هوز ؛ مخفف اسباه است که لشکر و سپاه باشد - و سگه را ليز کوشد که بتازی کلب خوانند» وبا پای‌فارسی هم گفته‌اندا . اسبهان » سر وزن و مصنی  |LAT []
337 ۱ ۷۲۳ ظروف می را سفید کند و اورا قلعی کر وسفید کر ی زگویند . اسپیل « بنتح‌اولبروزن‌تصیل » شخصی را گویند که پیوسته اسب دزدد و سوای اسب دزدی کار دیگر نک |LAT []
338 یعتی باز داشت و منم دفتن کرد . استای بکر اول وسکون بای‌حملی, امن استایی: است شش بایست : استیر ب با بای ابجد بر وزن استخضر » بمنی مطبر و کنده و غلیظ با |LAT []
339 علم است بی حیوانات و نباتات » بر خلاف‌استه که اسقر » بروزن متخصوص بانات لتعرتی کانه از مردم اصیل اف ۰ | کنترء از دواب‌تهود و بز رکه هم هست - ونام سلاح |LAT []
340 استرش -ایم اول و لت و قحرابم و سکون‌شین قرشت ۰ آنی راکوبند کهزمین‌را بدان شیار کنند . وسکون‌ثانی ونون وکاف فارسی» مردم کیاه باشد, وآن گیاهبت مانند مرد |LAT []
341 وت ۱ تیم استوی بش اول والث بر وزت بر کوی » مهر پشت را کویند . استه * ه ختح اول بروزن خسته , دالةٌ. خرما و شفتالو و زردآ لو ء امثال آبرا کوبند - واستضو |LAT []
342 استینه ۱ وورم وآمای کرده باشده وی سرعابی‌را گویشد که برجراحت زند ویاماساند . کوبند اکر آن سرما در شبهای ماحثاب بر جراحت بهام خورد الينه او را بکشد » و |LAT []
343 راک ِ ۰ وت ز4 ۷ داح نش تن مر دج ما وال ۱ اسطر لاب اسطرلاب برای‌سیین ارتفاع کوا کب ونشخبس‌زمان ومبل | فتاب ومقادیر ظل وتقدبرارتفاع مرتفعات و عمق چاهها  |LAT []
344 اعاء کلي اسطرلاب هفت‌عدد است : ۱ ام ۲۰ - عضاده , ۳ صفایح» نگ رن ۵ - فری » ٩‏ - فلس , ۷ - قطب .۰ ۶ التفهدم بیروئی مصحه جلال همایی ص و۲۸ - ۳۱۵ » + گاهنا |LAT []
```


## [2026-09-06T22:38:44.562Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SOD army ===\"\ngrep -n \"army\" SOD.txt | head -20\necho \"=== sp'd ===\"\ngrep -n \"sp\\`d\\|sp'd\\|spd\" SOD.txt | head -20"
}
```


### [2026-09-06T22:38:46.291Z] TOOL RESULT

```
=== SOD army ===
3988:contingents  in  the  army  of  Xerxes.  According  to 
10283:Szarmya   Opw  »zrmy>h) 
16352:assistant,  helper,  auxiliary(army) 
18076:army 
18084:weapons,  army  equipment,  equipment 
23131:azarmya   =**zrm 
23447:army 
35775:yarmyan 
35793:yarmya   ©f.  n. 
38597:way,  path(army  road) 
62766:pu-azarmya  ? 
67822:army 
67830:general  of  army 
67837:armyleader 
69941:army  commander 
79977:xarmy  ? 
87313:army     1592,  2383,  8874 
87314:army  commander    9180 
87315:army  equipment     1593 
87316:army  leader    8876 
=== sp'd ===
9215:aspon  ?   (Bsprnh)  ©Av.  aspdrdnah   ^'nspmh  ? 
18075:(o)spa5   ©<*spdda-   ©ob.  -yh   ^sp'5,  'sp'5 
18196:(o)spas-karanc   ©<*spds-kare   ©f.  n. 
23445:(a)spa5,  ispaS  ©<Av.  spdSa  ©ob.  -y 
67820:spa6  ©<Av.  spaSa  -^sp'5,  sp'dy'n 
67842:8877  sp'dy'n   C  jl^^L^ 
68031:sparze   ©Av.  spdrdza\  MP  ^pwrzyqyn 
79237:viso  pu0ra-\  Parth.  wispuhr,  <wispd$e
```


## [2026-09-06T22:38:52.956Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '18065,18090p' SOD.txt\necho \"=== find page in SOD_pages ===\"\npython3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i,l in enumerate(leaves):\n    if \"sp'5, 'sp'5\" in l or \"spa5\" in l and \"*spdda\" in l:\n        print('leaf',i,'printed~',i-66)\n        print(l[:400])\n        break\nEOF"
}
```


### [2026-09-06T22:38:54.852Z] TOOL RESULT

```
63 


1591  }sp   C  fb«L- 
asp  ?   ©pi.  >spt   =**>nsp,  *spt 

snare,  trap 
C2,  108R  4 

1592  >sp»8    B,  M,S  .L-. 
(o)spa5   ©<*spdda-   ©ob.  -yh   ^sp'5,  'sp'5 
army 

TSP  2.199,  3.29,  13ii5;  GMS  157,  1230;  Hen. 
Magi.  143.26;  MDii  pl94;  Bugut.  Insc.  B2.17 

1593  »sp*8p,ry   B  .j'>'V  <otr-  ^j&» 
(o)spa6-Pare 

weapons,  army  equipment,  equipment 

BSTBL,  Vim.  136;  GMS  1130  n  1 

1594  >sp)5y,n    B,  S  Ar-«^L- 
(o)spaSyan   ©pi.  -f 

=== find page in SOD_pages ===
leaf 128 printed~ 62
                                                                                                                        'spHvn'wy

 63
                                                                           Emmerick. SGS 135
 1591 }sp C                                               fb«L-
      asp ? ©pi. >spt =**>nsp, *spt                                 1602 »sp»rymy(y) B
```


## [2026-09-06T22:39:01.226Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '23435,23460p' SOD.txt\necho \"=== page for that ===\"\npython3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nimport re\nfor i,l in enumerate(leaves):\n    if '2383' in l and 'spa' in l:\n        print('leaf',i,'printed~',i-66)\n        j=l.find('2383')\n        print(l[max(0,j-300):j+400])\n        break\nEOF"
}
```


### [2026-09-06T22:39:03.023Z] TOOL RESULT

```
(reorder 

Hen.  Mitielir.  34;  Livsic.  HMV  259;  Frag.Len. 
82a  14,19,11.4 

2381  <NYW  -*  WW 

2382  (R  =>  'D 

2383  'sp'5   M  .u. 
(a)spa5,  ispaS  ©<Av.  spdSa  ©ob.  -y 

army 

GMS  18,  157;  BBB  519 

2384  'sprxs   M  *_f  jU  ,^4i  «Ty 
(o)sparaxs,  aspraxs  ©Av.  spardYa 

twigs 

GMS  957;  BBB  p72.573 

2385  (spty>k    M  =*  >spty>q 

2386  (spwrn   M  •x~it1J\£iJ9 
=== page for that ===
leaf 159 printed~ 93
jy-, }zt, *z>y-                                    2381 <NYW -* WW
     (to)be born
                                                                      a
     Sund. AoFviii 1981 p2l3                                    2382 (Rrm=>y 'D
                                                                2383 'sp'5 M                                           .u.
2370 'zy'm    B *± >ny>m(-)
                                                                     (a)spa5, ispaS ©<Av. spdSa ©ob. -y
2371 >zy>mnty C                                   jU>• <LrJ-
     azayamande
     birth                                                           GMS 18, 157; BBB 519
```


## [2026-09-06T22:39:08.029Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -c \"\" MON_part1.txt MON_part2.txt\ngrep -n \"قناری\" MON_part1.txt MON_part2.txt | head -10\necho \"--- adena ---\"\ngrep -n \"قناری\" incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head -10"
}
```


### [2026-09-06T22:39:08.138Z] TOOL RESULT

```
MON_part2.txt:94500
MON_part1.txt:99339
MON_part2.txt:14948:قناری: آ:08«:(.) (جان.) پرنده‌ای است از 
MON_part2.txt:14953:است. اصل این پرنده از جزایر قناری است 
MON_part2.txt:14960:می‌گردد. تربیت و نگهداری و صدور قناری 
MON_part2.txt:14970:هر سال بالغ بر ۱۰۰ هزار قناری به انگلستان 
MON_part2.txt:14976:شوند. قناری نر برای خوانندگی اگر تنها 
MON_part2.txt:14980:نمی‌خواند. قناری‌های وحشی از دانه نباتات 
MON_part2.txt:14982:می‌نمایند ولی در غذاهای قناری‌های ترییت 
--- adena ---
incoming/MON/MON_2vol_Adena_v2_djvu.txt:14948:قناری: آ:08«:(.) (جان.) پرنده‌ای است از 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:14953:است. اصل این پرنده از جزایر قناری است 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:14960:می‌گردد. تربیت و نگهداری و صدور قناری 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:14970:هر سال بالغ بر ۱۰۰ هزار قناری به انگلستان 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:14976:شوند. قناری نر برای خوانندگی اگر تنها 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:14980:نمی‌خواند. قناری‌های وحشی از دانه نباتات 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:14982:می‌نمایند ولی در غذاهای قناری‌های ترییت
```


## [2026-09-06T22:39:10.043Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '14940,14960p' MON_part2.txt"
}
```


### [2026-09-06T22:39:10.092Z] TOOL RESULT

```
قنادی: 720-1««:[ع. ف.] (حامص.) شغل 
قسسسناد» قسندسازی. شبر نی بزی» 
شیر نی فر وشی. (امر.) دکان قناد. 

قناره: (ند. ۲۵۱۱۵۲208181۲6 [ع. قناره. صعر 
کتتاره |( نتوین با اه دراز دارای 
مها بلند که قصابان در دیوار قصانی کار 
گذارند و گو شت را بدان میخ‌ها آویزند. 
قناری: آ:08«:(.) (جان.) پرنده‌ای است از 
راستة سبکبالان و از دسته کنجشکان که به 
قدو ان دازه گنجشک معمولی است. 
پرنده‌ای است زیبا و خواننده و زرد رنگ و 
گاه پرش مخلوط با پرهای قهوه‌یی و سیاه 
است. اصل این پرنده از جزایر قناری است 
(وجه تسمیه به همین مناسبت است) و از 
آنجا به دیگر نقاط جهان از جمله ایران بر ده 
شده. امر وزه این برنده در ايران نسته فراوان 
ترتبیت و نگهداری می‌شود و خواندنش 
سیار دل‌انگیز و مطبوع است و بعد از بلبل 
خسوش لحسن‌ترین پسرندگان مسحسوب 
می‌گردد. تربیت و نگهداری و صدور قناری
```


## [2026-09-06T22:39:19.874Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD watkins kwon ===\"\ngrep -n -i \"kwon\\|kwn-\\|hound.*canine\\|cynic\" AHD_watkins1985.txt | head -10\necho \"=== SYN Buck dog ===\"\ngrep -n \"3\\.61\\|DOG\" SYN.txt | head -10\necho \"=== IEC Mann ===\"\ngrep -n \"kuō\\|kwōn\\|kuon-\" IEC.txt | head -10"
}
```


### [2026-09-06T22:39:19.946Z] TOOL RESULT

```
=== AHD watkins kwon ===
166:Stockbreeding and animal husbandry were an important part of Indo-European eco- nomic life. The names for all the familiar domesticated animals are present throughout the family: gvou-, “cow and bull,” owi-, “sheep,” ag“h-no-, ‘lamb,’ aig- and ghaido-, “goat,” sd-, “swine,” and porko-, “farrow.” The domestic dog was ancient (kwon-); its name may underlie the common Indo-European word for horse, ekwo-. The expansion and migration of the Indo- European-speaking peoples in the later third and early second millennia B.c. is intimately bound up with the diffusion of the horse. The verbal root deme-?, “to force,” acquired the special sense of “‘to tame horses,” whence English TAME. Stock was a source and meas- ure of wealth; the original sense of peku- was probably “wealth, riches,” as in Latin pecu- nia, whence “wealth in cattle” and finally “cattle” proper. The same evolution from the general to the particular may be observed in the root neud-, “to make use of,” whence English NEAT?.
433:ekwo-. Horse. Possibly originally derived from kwon-. 1. Latin equus, horse: EQUESTRIAN, EQUINE, EQUITANT, (EQUITATION); EQUISETUM. 2. Greek hippos, horse: EO- HIPPUS, HIPPOCAMPUS, HIPPOGRIFF, HIPPOPOTAMUS. [Pok. ekuo-s 301.]
652:kwelek-. Bundle. Proposed by some as the root of Latin culcita, mattress, sack, which is more likely of unknown origin: QUILT. [Pok. kuelak- 630.] kwelp-. To arch. 1. Germanic *hwalbjan in Old English *hwelfan, hwylfan, with parallel form *hwelman (> Middle English whelman), to turn over: WHELM. 2. Suf- fixed o-grade form *kwolp-o- in Greek kolpos, bosom, womb, vagina: GULF; COLPITIS, COLPOSCOPE, COLPOS- copy. [Pok. 2. kuelp- 630.] kwen-. Holy. Suffixed zero-grade form *kwn-s-lo- in Germanic *hunslam in Old English hisl, hiisel, Eucha- rist: HOUSEL. [Pok. kuen- 630.] kwent(h)-. To suffer. 1. Suffixed form *kventh-es- in Greek penthos, grief: NEPENTHE. 2. Zero-grade form *kenth- in: a. Greek pathos, suffering, passion, emotion, feelings: PATHETIC, PATHO-, PATHOS, -PATHY; PATHOGNO- MONIC, SYMPATHY; b. suffixed form *k“nth-sko- in Greek paskhein, to feel, suffer: PROTOPATHIC. [Pok. kventh- 641.] kwép-. To smoke, cook, move violently, be agitated emotionally. Hypothetical base of possibly related words. 1. Suffixed variant form *kup-yo- in Latin cupere, to desire: COVET, CUPID, CUPIDITY; CONCUPISCENCE. 2. Zero-grade form *kwap-, becoming *kwap- possibly in: a. Latin vapor, steam, vapor: VAPOR; EVAPORATE; b. Latin vapidus, that has emitted steam or lost its vapor, flat, poor: VAPID; c. Greek kapnos, smoke: ACAP- niA. [Pok. kuép- 596.] kver-1, To make. 1. Sanskrit karoti, he makes: SANSKRIT. 2. Suffixed form *kver-6r with dissimilated form *kel-6r in Greek pelér, monster (perhaps “that which does harm”): PELORIA. 3. Suffixed form *ker-as- in Greek teras, monster: TERATOCARCINOMA, TERATOGEN, TERA- TOID, TERATOMA. 4, Suffixed form *ker-mn in Sanskrit karma, act, deed: KARMA. [Pok. 1. kver- 641.] kwer-2. Something shaped like a dish or shell. Suffixed variant form *k”ar-yo- in Scottish Gaelic coire, cauldron, hollow, whirlpool: corrt&. [Pok. 2. kver- 642.] kwerp-. To turn oneself. 1. Germanic *hwarb- in Old English hwearf, wharf (< “place where people move about”): WHARF. 2. Germanic *hwerban in: a. Old Norse hverfa, to turn: VARVE; b. Old Norse *hvirfa, to whirl, perhaps assimilated to Danish hvirre, to whir, akin to the Scandinavian source of Middle English whirren, to whir: WHIR; C. Old Norse hAvirfla, to whirl: WHIRL; d. Old North French werble, a warbling: WARBLE!. 3. Possibly suffixed zero-grade form *kwrp-o- in Greek karpos, wrist: CARPAL, CARPUS. [Pok. kuerp- 631.] kwes-. To pant, wheeze. 1. Germanic *hwésjan in Old Norse huzsa, to hiss: WHEEZE. 2. Latin queri, to com- plain: QUARREL!, QUERULOUS. 3. Suffixed zero-grade form *kus-ti- in Greek kustis, bladder, bag (< “bellows”): cyst, cysTo-. [Pok. kues- 631.] kwé6t-. To shake. Zero-grade form *kwet-, becoming *kwat- in Latin quatere (past participle quassus, in composition -cussus), to shake, strike: CASCARA, KVETCH, SCUTCH, SQUASH?; CONCUSS, DISCUSS, PERCUSS, RESCUE, succussIoNn. [Pok. kuét- 632.] kvetwer-. Four. I. O-grade form *ketwor-. 1. Probably Germanic *fe(d)wor- in: a. Old English féower, four: Four; b. Old English féowertig, forty: FORTY; c. Old English féowerténe, fourteen: FOURTEEN. 2. Latin quat- tuor (> Italian quattro), four: CAHIER, CARNET, QUATRAIN; CATER-CORNERED, QUATTROCENTO. IT. Mul- tiplicatives *kveturs, kvetrus, and combining forms *kvetur-, *kvetru-. 1. Latin quater, four times: (CARIL- LON), QUATERNARY, QUATERNION, QUIRE’. 2. Latin gua- drus, four-sided thing, square: CADRE, QUADRATE, QUARREL?, QUARRY?; SQUAD, SQUARE, TROCAR. 3. Latin quadri-, four: QUADRI-. 4. Latin quadra, square: QUA- DRILLE!. 5, Latin quadrdns, a fourth part: QUADRANT. 6. Latin quadrdagintd, forty (-gintd, ten times; see dekm): QUARANTINE. 7. Variant form *ket(w)r- in: a. Greek tetra-, four: TETRA-; b. Greek tessares, tettares,
655:kwo-. Also ki-. Stem of relative and interrogative pro- nouns. 1. Germanic *hwa-, hwi- in: a. personal pronouns *hwas, *hwasa, *hwam in Old English hwd, hwes, hwem, who, whose, whom: WHO, WHOSE, WHOM; b. pro- noun *hwat in Old English hwet, what: WHAT; c. adverb *hwi in Old English hwy, why: wHy; d. relative pronoun *hwa-lik- (*lik-, body, form; see lik-) in Old English hwilc, hwelc, which: WHICH; e. adverb *hwo6 in Old English hii, how: How!; f. adverb *hwan- in (i) Old English hwenne, hwanne, when: WHEN (ii) Old English hwanon, whence: WHENCE; g. adverb *hwithré in Old English hwider, whither: WHITHER; h. adverb *hwar- in Old English hwér, where: WHERE. 2. Germanic *hwatha- raz in: a. Old English hwether, hwether, which of two, whether: WHETHER; NEITHER; b. Germanic phrase *aiwo gihwatharaz, “ever each of two” (*aiwo, *aiwi, ever; see aiw-; *gi- from *ga-, collective prefix; see kom), in Old English €ghwether, &ther, either: EITHER. 3. Latin gui, who (genitive plural guérum): QUA, QUIB- BLE, QUORUM. 4. Latin quid, what, something: HIDALGO, QUIDDITY, QUIDNUNC, QuIP. 5. Latin quam, as, than, how, in quasi (quam + si, if; see swo-), as if: QUASI. 6. Latin quod, what: QUODLIBET. 7. Latin quot, how Many: QUOTE, QUOTIDIAN, QUOTIENT; ALIQUOT. 8. Latin quom, when: QUONDAM. 9. Latin quem, whom: CON- QUIAN. 10. Latin quantus, how great: QUANTITY. 11. Latin gudlis, of what kind: QuALITY. 12. Latin ut, that: (uT). 13. Latin uter, either of two: NEUTER. 14, Latin ubi, where, and ibi, there: ALIBI, UBIQUITY. 15. Persian chiz, thing: CHEESE, [Pok. k¥o- 644.] kwon-. Dog. 1. Greek kudn, dog: CYNIC; CYNOSURE, PROCYON, QUINSY. 2. Suffixed zero-grade form “kwn-to- in Germanic *hundaz in: a. Old English hund, dog: HOUND; b. Old High German Aunt (> German Hund), dog: DACHSHUND; c. Dutch hond, dog: KEESHOND. 3. Nominative form *kw6o in Welsh ci, dog: CORGI. 4. Variant *kan-i- in Latin canis, dog: CANAILLE, CA- NARY, CANICULA, CANINE, CHENILLE, KENNEL}, [Pok. Ruon- 632.]
1332:CAM gembh- CAMARILLA kamer- CAMBIST skamb- CAMBIUM skamb- CAMERA kamer- CAMPYLOTROPOUS kamp- CAN! gno- CANAILLE kwon- CANARY kwon- CANCEL carcer CANCER kar-1
1334:CANDENT kand- CANDID kand- CANDIDA kand- CANDIDATE kand- CANDLE kand- CANDOR kand- CANESCENT kas- CANICULA kwon- CANINE kwon- CANKER kar-1 CANNABIS kannabis CANOROUS_ kan- CANT? kan- CANTABILE kan- CANTEEN kanto- CANTICLE kan- CANTILLATE kan- CANTO kan- CANTON kanto- CANTOR kan- CANVAS kannabis CANZONE kan- CAPABLE kap- CAPACIOUS kap- CAPE2 kaput CAPELLA kapro- CAPIAS kap- CAPITAL! kaput CAPITAL? kaput CAPITATE kaput CAPITATION kaput CAPITELLUM kaput CAPITULATE kaput CAPITULUM kaput CAPO! kaput CAPON skep- CAPRIC ACID kapro- CAPRICE kaput CAPRICORN kapro-, ker-1 CAPRIFIG kapro- CAPRIOLE kapro- CAPROIC ACID kapro- CAPSICUM kap- CAPSID kap- CAPSTAN kap- CAPSULE kap- CAPTAIN kaput CAPTION kap- CAPTIOUS kap- CAPTIVATE kap- CAPTIVE kap- CAPTOR kap- CAPTURE kap- CAR kers-2 CARAMEL kolem- CARAT ker-1 CARAVANSARY tere-2 CARBON ker-4 CARBUNCLE ker-4 CARCINO-  kar-1 CARCINOGEN kar-1 CARCINOMA kar-1 CARD? kars- CARDIA kerd-1 CARDIAC kerd-1 CARDIO- kerd-1 CARDOON kars- CARE gar- CAREEN kar-1 CAREER kers-2 CARESS ka- CARET kes-2 CARGO kers-2 CARICATURE kers-2 CARIES ker-5 CARILLON kWetwer- CARINA kar-1 CARIOLE kers-2 CARL karlaz CARLING karlaz CARMINATIVE kars- CARNAGE sker-1 CARNAL sker-1 CARNASSIAL_ sker-1 CARNATION sker-1 CARNET kWetwer- CARNIVAL legh-, sker-1 CARNIVOROUS = sker-1 CAROCHE kers-2 CAROL aulo- CAROTID ker-1 CAROUSE ud- CARP! ger-2 “CARP kerp- CARPAL kwerp- CARPEL kerp- CARPENTER kers-2 CARPET kerp- CARPO- kerp-
1348:CHASM ghai- CHASSIS kap- CHASTE kes-2 CHAUDFROID kele-1 CHEAP caupd CHECK tké- CHECKMATE tké- CHEER ker-! CHEESE? kWo- CHEETAH kWeij-2, skai- CHEILOSIS ghel-una CHELICERA ker-1 CHELONIAN gheli- CHEMOTROPHY threph- CHENILLE kwon- CHENOPOD ghans- CHERISH ka- CHERNOZEM kers-1 CHERRY ker-6 CHERSONESE ghers-, sna- CHESS’ kap-
1394:CONVOLVE wel-3 CONVULSE wel-4 cook pekw- cOoKY kak-2 cooL gel-3 COOPER ku- COOPERATE op-1 CO-OPT op-2 COORDINATION ar- COPE! kel-1 COPEPOD kap- COPIOUS op-1 COPRO- kekw- COPULA ap-! COPULATE ap-1 COPY op-1 CORACIIFORM ker-2, merph- CORACOID ker-2 CORBEL ker-2 CORBINA ker-2 CORD ghere- CORDATE kerd-1 CORDIAL kerd-1 CORDIFORM kerd-1 CORDON ghere- COREOPSIS sker-! CORGI kwon- CORIACEOUS sker-1 CORIUM §sker-1 cOoRM sker-! CORMORANT ker-2 CORN! gre-no- CORN2 ker-1 CORNEA ker-1 CORNEL ker-6 CORNEOUS ker-1 CORNER ker-1 CORNET ker-1 CORNICULATE ker-1 CORNIFICATION ker-1 CORNU_ ker-1 CORNUCOPIA op-! CORONA sker-3 CORONOID  sker-3 CORPORAL! kWrep- CORPORAL’ kWrep- CORPORATE kWrep- CORPOREAL kWrep- CORPOSANT kWrep-, sak- CORPS kWrep- CORPSE kWrep- CORPULENCE kWrep- CORPUS krep- CORPUSCLE kWrep- CORRADE réd- CORRECT reg-! CORRIDOR kers-2 CORRIE kWer-2 CORROBORATE reudh-! CORRODE réd- CORRUGATE ruk-2 CORRUPT reup- CORSAGE kWrep- CORSAIR kers-2 CORSE kWrep- CORSET kWrep- CORTEGE gher-1 CORTEX sker-1 CORUSCATE sker-2 CORVEE reg-! CORVINE ker-2 Corvus ker-2 CORYDALIS_ ker-1 CORYMB_ ker-1 CORYNEBACTERIUM bak-, ker-1 CORYPHAEUS_ ker-1 COSMONAUT nau-2 COSMOPOLITE pele-3 cosmos kes-3 cost sta-
1406:cUsK ters- CUSPIDOR spyeu- CUSTOM s(w)e- CUTANEOUS (s)keu- CUTICLE (s)keu- CUTIN (s)keu- cuTIs (s)keu- cuTLass skel-1 CUTLET kost- CUTTLE ku- CYCLE kwel-1 CYCLO- kwel-1 CYCLOID kwel-1 CYCLONE kWel-1 CYCLOSIS kwel-1 CYGNET keuk- CYGNUS keuk- CYLINDER skel-3 CYMA keue-2 CYMBAL keu-2 CYMBIDIUM keu-2 CYNIC kwon- CYNOSURE kwon-, ors- CYPRIPEDIUM ped-1 CYPSELA keu-2 cysT kwes- CYSTO- kwes- -CYTE (s)keu- cyTo- (s)keu-
1408:DACHA d6- DACHSHUND kwon, teks- DADO d6-
=== SYN Buck dog ===
3744:CHAPTER 3 ANIMALS 3.45 Foau, Cott gal eANo 3.46 Ass, DonKEY 3.12 Mate (adj.) 3.47 Mute gia ene 3.51 Hen, Catcxen (Generic) Blan CASTE 3.52 Cock Blo ESTO 3.53 CAPON 3.16 PasTuRE (vb.) aa ee ON chaaeh Pe, 3.55 CHICKEN 3.18 HerDSMAN aA Goan 3.19 STABLE, STALL ne Duue 3.20 CATTLE (Bovine Species) et at ae se 3.612 Purry a oe 3.62 Car 3 4 CALF 3.63 Mouse eed tae AM ; eS a 3.66 FISHERMAN 3.28 Ews 3.71 Wo.ur | 3.29 Lams 3.72 Lion 3.31 Swint 3.73 BEAR 3.32 Boar 3.74 Fox | 3.33 Barrow 3.75 DEER i 3.34 Sow 8.76 MonxkEY 3.35 Pie 3.77 ELEPHANT 3.36 Goat 3.78 CAMEL | 3.37 Hu-coar 3.79 Hunt (vb.) 3.38 Kip 3.81 InsEctT 3.41 Horse (Generic) 3.82 BEE 3.42 Srantion 3.83 Fy : 3.43 GrLpine 3.84 Worm 344 Mare 3.85 SNAKE
4811:3.61 DOG Grk. — xboy Goth. hunds Lith. uo NG oxunl ON hundr Lett. suns Lat. canis Dan. hund ChSl. pisiz It. cane Sw. hund SCr. pas Fr. chien OE hund (docga) Boh. pes Sp. perro (can) ME hound, dogge Pol. pies Rum. cline NE dog Russ. sobaka (pes) Ir. ci, matad Du. hond Skt. — gvan- Nir. madra(dh), gadhar OHG hunt Av. span- W. ct MHG hunt ; Br. ki NHG hund
4828:2, NG oxvdi, fr. dim. form of late oKUA(A)os, (cKidXov* THY Kiva €youoww Hesych.) = Grk, oxbdak ‘whelp, pupp , sometimes simply ‘doe’. for whi v3 3.612. ply ‘dog’, for which see
4832:Note on ‘bitch’. Of the preceding words, Grk. xtwy, Lat. canis, and some- times others were used of the male and female dog, without distinction except as shown by the gender of the agreeing word. But for the female ‘bitch’ there are usually special terms. Some of these are simply new fem. forms of words for ‘dog’, as NG oxida, VLat. *cania (> It. cagna, MIr. caigne, Fr. chienne), Sp. perra, Br. kiez, Sw. hynda, NHG hiindin, Skt. ¢uni-, also SCr. kuéka (fr. kuéak, a less common word for ‘dog’, based on a calling cry. Berneker 636f.). Many more are quite unrelated. Rum. catea, fr. Lat. catella ‘female puppy’ (REW 1763). ON bikkja, Norw. bikje, Sw. dial. bicka, OF bicce, ME bicche, NE bitch, etym. dub., perh. : Skt. bhaga- ‘cunnus’ (Walde-P. 2.148. Falk-Torp 72). OE life, Du. teef, MLG teve (> Dan. teve) etym. dub. (Falk-Torp. 1313. Franck— v. W. 690). OHG zoha, MHG zohe, NHG dial. zope, zauche, perh. as orig. ‘bearer’ : OHG ziohan ‘draw, nourish’ (Walde-P. 1.781. Falk-Torp. 1297). Lith. kale: Ir. cuilén ‘puppy’, ete. (3.612). Among others, either of imi- tative orig. or obscure, are Fr. lice (now obs. or dial.), Br. gart, ON tik, Norw., Sw. dial. tk, Lett. kun’a, Boh. cubka, Pol., Russ. suka (see above, 1).
4835:180 SELECTED INDO-EUROPEAN SYNONYMS 3.612 PUPPY
8899:Meyer, Neugr. Stud. 2.99, 3.61, but with no mention of xéradis) is unsatisfactory, 2. Lat. coc(h)ledre, coc(h)ledrium, a small spoon with one end pointed, used for eating snails and eggs (Mart. 14,121 sum cochleis habilis, sed non minus ovis. Numquid scis potius cur cochleare vocor), deriv. of coc(h)lea ‘snail’, this fr. Grk. xoxNas. Hence It. cucchiaio, Fr. cuiller, cuilliére, Sp. cuchara, also OE cuc(e)ler. Walde-H. 1.241, TErnout-M. 201. Walde-H. 1.241. REW 2012.
10292:NG oovXi, fr. Lat. siibula (above, 2). G. Meyer, Neugr. Stud. 3.61 ff.
=== IEC Mann ===
```


## [2026-09-06T22:39:21.987Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== ARY سگ ===\"\ngrep -n \"سگ\" incoming/ARY/ARY_pages.txt | head -10\necho \"=== ARY سپاه ===\"\ngrep -n \"سپاه\" incoming/ARY/ARY_pages.txt | head -10\necho \"=== PHD sak/spah ===\"\ngrep -n \"^sag\\|sak \\|spāh\\|spah\\|spʾh\" PHD.txt | head -20"
}
```


### [2026-09-06T22:39:22.060Z] TOOL RESULT

```
=== ARY سگ ===
574:۱ طریق پیگیری پسگرایانه‌ی شکل واژه‌ها) تعبین کرده‌اند. نمونه‌ی زیر مسیر اینگونه بازسازی‌ها را در
580:نداشته تعیین دقیق آوا و معنی واژه‌های هند و اروپایی بنیادین فقط از روی پیگیری پسگرایانه و
938:همریشه‌ی مربوط به «اسب» و «گاوه و «گوسفندء و دسگ» و «خوکک؛). همریشگی واژه‌های متعدد
1199:خود را ذ کر می‌کند»کتاب او عملاً خواننده را از پسگشت به مأَذ او (که برخی امروزه نایاب هستند)
1371:دارد ولی هیچکدام از پسگشت‌های در دسترس من اشاره‌ای همریشه‌های ایرانی و سانسکریت این
1404:کردی (80/57): ۷ ,2 پسگشت‌ها ای دراد ۲
1412:پهلوی (۲هاتلهه): 17 باانتا۸7 پسگشت‌ها دای اد ادن ای
1430:پهلوی (۷هاتل۸ط): ۸1 پسگشت‌ها لامش اد ادن
1453:روسی ((5514(ا): دندید ۱۲۱۱۱ پسگشت‌ها اه دا دناد
1475:پرناتی 0888/0): .۲ 8۸ | پسگشت‌ها آشرد دا
=== ARY سپاه ===
=== PHD sak/spah ===
566:se-pay [3-p'd | N sipá] three-legged. sēr, v. Sagr. se-Sabag [3-spk!] three-night-long, trinoctial. seyom [зит | N ~] -third (in compound numerals). sëzd [s(y)zd | P syzd, (N séz/agi?)] might, tyranny; tyrannous. sézdah [sycdh | M syzdh, N ~] thirteen. sézdén [s(y)zdyn! | P syzdyn] mighty, tyrannous. si [sy] goose. sidig(ar) [styk', -kl | M sdyg, N sidigar] third. sih [30 | M syh, N si] thirty. ~om [-wm] thirtieth. sik [HLYA < А hP; sk | N ~] vinegar. sisimbar [sysymbl, -nbl | N sisambar] sisymbrium, wild-thyme. *Skandar [swkndl | N sikandar) = Aleksandar. snāh [sph] blow, strike, violence. sneh [snyh] sword. snéxr [snyhl] snow. snézag [snyck!] snow. snóy [snwd] (rain-, snow-)cloud. sófistà [swkpst’k'] sophist. 1s68 [swk'] use, profit, advantage. 25806 [swk!'] burning, combustion. 3806 [swk! | N só(y)] side, direction. sógand [swknd | M swgnd, N saugand] oath. ~ XWardan: take, swear an oath. sóhistan, sóh- [swh-stn'] touch, feel. ~iSn: feeling, sense. ~iSnig : feeling, sensitive. sēr [sz] salty. ~ag [-k!] salt (land). ѕӧзап [swsn! | N ~] lily. Só&yans [swkšydns = Av. saošyās] saviour (especially the final Saviour who will bring about the frašagird). sóxtan, sūz- [swhtn!, swe- | М swxt, swc-, N ~] burn. ~išn: burning, combustion. ~išnīg: burning, flaming. sūzāg [swo k! | М swe'gyn, N séza] burning. sózan [swen' | N ~] needle. spāh [sp’h | N sipah] army. ~bed [-pt! | N -bud] general, commander. spandān [spnd”x! | N sip~] mustard seed. Spandarmad [spndrmt'] N isfandármuó] Holy Thought, the fourth Amahraspand, earth goddess; cal. 12th month; sth day. spar [spl | M ‘spr, N sipar] shield. spar-, v. spurdan. spas [sp’s | M ?s-, “р>, N sipas] service, gratitude, thanks.
839:army gund, hén, laskar, spāh.
1290:commander framāndār, sástar, spahbed.
2087:general (n.) spāhbed.
4779:spāh ALY Q335 dēbahr, spihr, Nay LAKE spaxr spahbed VP OR 0335 spas ts” суз? spāsdār Nee es. spāsdārīh uA a soda) spāsešnās TO Put 0335 debàg VW ett spāsūmand ? v€ Pus” q335 spāš AV суз?
4814:saxtan, saxtan süg, sak say- sahigih sahig, sivag sas
5014:sagt,
```


## [2026-09-06T22:39:32.234Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD sag ===\"\ngrep -n \"sag \\[\\|sag\\b.*dog\\|dog \" PHD.txt | head -10\necho \"=== NYB ===\"\ngrep -n \"spāh\\|sag\\b\" NYB_vol2_glossary.txt | head -10\necho \"=== ARY entries for sag ===\"\ngrep -n \"سگ$\\|^سگ\\|«سگ»\" incoming/ARY/ARY_pages.txt | head\ngrep -n \"کوون\\|kuon\\|سپاه\\|اسپاه\" incoming/ARY/ARY_pages.txt | head"
}
```


### [2026-09-06T22:39:33.926Z] TOOL RESULT

```
=== PHD sag ===
217:arzómand [le wmnd | (N arjumand)] valuable, worthy. ~ih: value, worth. Arzür []zwl] a demon; a mountain at the mouth of hell. a-sag [?s?*k! | M *s?g] innumerable, countless. азап Pon! | N ~] at rest, easy, peaceful. “АП: rest, ease, peace. a-sar Dell endless. āsāy-, ~išn, v. āsūdan. a-sazāģ ["sc? k!] unfitting, unsuitable. a-sazisn|ig Dscfn-yk'] imperishable, permanent. ~ih: imperishability, permanence. a-sēj [Psyc] free from danger.
384:ёгбһ [glwh | N guroh] group, crowd. gubrág [gwpl’k'] awake, alert, vigilant. ģubrās- [gwp/”s-] = wigras-, v. wigrádan. ģuftan, $0(w)- [YMRRWN-, YMLLWN-tn! < A ymlwn, V тЇ; gwptn', gwb- | M gwptn, gw-, N ~, gā(y)-] say, speak. ~išn: speech. ģuftār [gwpt?] | N ~] speaker. ~ih: (power of) speech. gugiin- [gwk’n- | M gwg^n-] destroy. gugar(i)dan, gugar- [gwk”/-(y)tn! | N guwár-idan] digest. tuģāy [gwk*dy | M gwg'y, N guwah] witness. ~ih: testimony. ģūh [gwh | N —] dung, excrement. guhrayénidan, guhrayén- [gw AP yn-ytn!] waken, arouse. gul [gwl | N ~] flower, rose. ботап [gwnmn! | = M, N ~] doubt. ~par [-A/] casting doubt. ~ig [-yk'] doubtful. ~ih, ~igih: doubt. gumardag [gwmltk'] appointee, deputy. ģumārdan, gumār- [gwm’l-tn' | М gwm'r-dn, N gumāštan, gumar-] appoint, commission, entrust. gumbad [gwmbt' | N ~] dome, fire-temple. £umég [gwmyk! | M gwmyg] mixture. guméxtan, gumēz- [gx”myhtn!, gwmyc- | M gwmyxtn, gwmyz-] mix. ~išn: mixing, mixture; = gumézagih. gumëzag [gwmyck'] mixture. ~th: the Mixture, (the duration of) this material world. Jgund [gwnd | = P] army, troop; group, gathering. *gund [gwnd | N ~] testicle. gung [g(w)ng | N ~] dumb. ģurbaģ [gwibk! | N ~a] cat. Бита [gwlt! | P gwrd, N ~] hero. lih: heroism, bravery. gurdag [gwltk! | N ~a] kidney. *gurdih [ewityh] (some piece of) armour. gurdwār [gwltw’!] befitting a hero. ёпгр [gwlg | N ~] wolf. gurganig [gw/g”nyk! | N ~i] of (the province) Gurgan. gursag [ewlsk] | N gurusna !] hungry. «ЛЬ: hunger. Suën [gvfn! | N ~] male. gusnag [gwšnk! | J gušna] hungry. Gušnasp [gwšn(*)sf] the second major Fire of Sasanian Eran, that of warriors. £yà$ [gyw'k! | M gy'g, N jay] place.
390:hambār [kmb’l | N anbdr] store. hambārīdan, hambār- [hm-, hnb'l-ytn! | M hmb'r-, N anbürdan] fill, collect. hambasān [Anbs?n! | M *mbs*n] enemy, opponent. ~ig [-yk'] inimical, opposing. hambast [Ambst' | N anbast] compact. !hambastag [Ambstk' | N anbasta] formed, composed. shambastag [hnbstk' | М hmbst] collapsed, fallen. hambāstag [hmb’stk'] *all. īhambastan, hamband- [hmbsin', hmbnd-] form, compose; bind to- gether, intertwine, encircle. ~i8nih : binding together, intertwining. žhambastan, hambah- [%xbstn!, hnb?h- | M hmbst, hmbh-] collapse, fall down. VW "E. hambāstan, hambāh- [hnb’stn', hnb’d- | M hmb’stn, hmb’h-] cast down, demolish. ~išn: felling, demolition. ham-bašn [hmbén'] of the same stature. hambaw-, —išn, v. hambüdan. hambāy [hmb?g | (M hmb’w)] companion, partner; adversary. hambāz [hm-, hnb’c | M ?mP?z, N anbáz] partner. hambedig [%mbytyk!] = hambadig. hambēš-, —išn [hnbwi-, -£n! | N anbūšif] = hambüs-, ~išn, hambdy- (hnbwd- | M hwmbwy-, N anbóy-idan] smell (tr.). —ügih [-*kyh], —iŠn: (sense of) smell. hambüdan, hambaw- [hm-YHWWN-tn', v. büdan; hmbwtn'] be united, composed. „«išn(īh): union, composition. hambun [hmbwn'] (with a negative) not at all, not in the least. hambüsidan, hambūs- [hnbws-ytn' | N anbüsidan] come into being, be conceived. ~išn: conception. ham-dádestàn (hm-D YN A, -d'tsn! | N ham-dástán] agreeable, of the same opinion. hamdam [hmdm | N ~] intimate. ham-désag [hmdysk'] of the same form, homomorphous. hamë [hm’y | M Атуш, N ~] always. ^ ka: whenever. ham-ēdēn [m)ytwn! | N hamédün] likewise, similarly. bamé|ig (/um)yyk! | M тушур] eternal. ~iha [-yh’] eternally. hamémiil [mym] | = J] opponent, adversary. --īh: opposition. haménidan, hamén- [hmyn-ytn'] unite, compose. hamē-rawišnīh, hamē-ud-hamē-rawišnīh [(Amy W) hwy lwbsnyh) eternity.
392:hamēstār, —ih [hmyst!l, -yh] = hamēmāl, ~ih. hamésag [hmyfk! | M hmyšg, N —a] always. ^h : eternity. ~-86z [-swe] ever-burning. hamē-wahār [hmy whl | N haméfa-bahar] marigold. ham-éwénag [Am'dwynk!'] of the same kind, homogeneous. ham-góhr (hmgwhl! | M hmgwhr] of the same substance or nature, consubstantial. ham-ginag [hmgwnk! | M hmgwng] likewise, so. P hāmharz [A())mAlc | P I? mhyrz] adjutant, attendant. hāmīn [A*myn! |= M] summer. ~ig [-yk'] (of) summer. hāmist [KHDE, v. hammis ; )”mst!] all. ham-kār [hmk’l | N ~] collaborator. 7h : collaboration. hāmkišwar [mkyfwl | M. -wr] universe. hammis [KH DE < A k-hdh), ат... ~: together with. hammist [hmyst'] stagnant, peaceful. ~(ag)an [-(kYn'] limbo, the neutral station between heaven and : hell. vl hammóxtan, hammoz- [ALPWN-tn! < A У "Ip: hmwhtn', hmwc-, Ki hmsoz- | M hmwxtn, N āmēxtan, ámóz-] teach; learn. -išn: teaching. hammdxtar [Amwht?!] learner. ~th: learning. hammóz- , ~i8n, v. hammóxtan. —@йг [kmwcek?l | N āmēzgār] teacher. ham-nibardih [hmnpityh] (single) combat. hamēūģ [/tmwg] equal, like. hámón [k mwn' | N kāmūn] level, flat. hámoyén [/?mwdyn!] all. ham-pursag [hmpwrsk!] consulting, taking counsel. ^h : consultation. ham- |-ránih [Am nyh] battle, combat. ~-samiain [-s"m?n!] contiguous. ~-sardag [-sltk'] of the same kind, like. ~-sayag [-sdk! | N hamsáya) neighbour. ~-tag [-t*k! | N hamid] equal, peer. «tan [-tn'] of the same stature, build. ~=-tihmag [-twhmk'] relative, relation. hamwar [hmwl | N hamwār] level, abreast. hámwiür(ag) [%()mw?/, -k! | N hamwdara] always. ham-zamān [hm ODNA | N —] instantly, immediately. handām [And*m | = P, N andàm] member, limb. handarz [hndle | N andarz] advice, injunction, testament. handarzénidan, handarzén- [hndleyn-ytn!] advise.
398:P hd [Aw' | = P] that, he. Hóm [kwm | N ~] the sacred plant Haoma (ephedra). homānāģ [h(w)m’rk' | N hamana, J xumana], 6 .. . ~: like. ~th: likeness. hómast [hwn'st!] various series of prayers. hómyjén, -ïg [hwmyn!, -yk'] of Haoma. ~ӧтапа [-'wmnd] prepared with Haoma. Ногааа [hwrdt' | M hrwd'd, N Xurdād] Perfection, the fifth Amahra- spand, guardian of water; cal. 3rd month; 6th day. hdsag [hwsk' | М лое, N xēša] ear of corn, cluster; astr. Spica, Virgo. hēšēnīdan, hoSen- [hwsyn-ytn'] (cause to) wither. hēšīdan, hēš- [hws-ytn' | M hwi-, N x~] dry up, wither. héy(ag) [hwy, -k! | M hwy] left(-hand). Hróm [hlwm | M hrwm, N Рат] Byzantium, Rome. ~ayig [-dyk'] Greek, Byzantine, Roman. hu- [hw- | = M] good-, well-. ~ih: good, goodness. hu-bóy [hwbwd] sweet-smelling, fragrant. ~th: fragrance. hu-čašm [hwesm] unenvious, benevolent. ~ih: benevolence. hu-čihr [hweyhl | M hweyhr, (N xujir)] fair, beautiful. hudà(ha)g [hwa?(h)k' = Av. hudàáh-] good, beneficent. ~th: beneficence. hu-|-dast [hwdst'] skilful. ~-dén [-dyn'] of good (i.e. Mazdean) religion. ~-ddsSag [-dušk'] very pleasing. m-ēwāz [-"yw'c] of good speech, affable. —-ëwàzih : affability. ~-fraward [-plwit'] blessed, the late. hugar [hwgl] easy; beneficent. hu-|-&ówisn [hwgwbsn'] of good speech. ~-gugar [-gwk’l] easily digestible. ~-kunign [-kwnsn'] of good behaviour. „-mānīh [-m’nyh] good-mindedness, benevolence. humat [hwmt' = Av. humata-] good thought. humāy [hwm’y | N ~] a bird of good omen; eagle. hu-menišn [hwmynsn'] of good thought. hu-murwāģ [Awmwlw’k'] auspicious. hunar [hwal | M hwnr, N ~] virtue, ability, skill. hunarāwand [kwn wnd | M hwnr'wynd] skilled, virtuous. ~th: skill, virtue. hunarómand [kwn wmnd | N hunarmand] = hunarāwand. hunidan [kwnytn'] extract, express (juice). huniyág [/sonyd?k! | N xunyá] delightful. ~th: delight, entertainment.
505:P naxsag [nhšk! | P nxšg] good, fine.
514:nihuftan, nihumb- [zhwptn', nhwmb- | = M, N <) cover, hide, conceal, clothe, nihumbidan [nhwmbytn'] = nihuftan. *nikóhidan, nikóh- [nkwh-ytn' | N ~] blame, execrate. ~išn: blame. ~išnīg : blameworthy, execrable. nil [nyl | N ~] indigo. nilópal [nylw(k)pl | N ~, nilēfar] lotus, water-lily. nimüdan, nimāy- [nmwtn', nmd- | M nmwdn, nm’y-, N ~] show, guide. nirfs- [nlps-] wane, decrease. ~išn: decrease, diminution. nirmad [nylmt'] profit, interest. ~ӧтапа [-’wmnd] profitable. P nisag [nys’k' | P nys’g] bright, splendid. niš- [nyi- | M nyyš-ydn, J ~] see, observe. nišān-, v. nišāstan. nīšān [ny$*x! | = M, N nisàn] sign, mark, banner. nišast [nsst! | N ~] association. nišastan, nišīn- [Y TY BWN-stn! < A V у; пт! | M nist, (nfyy-), N ~] sit. nišāstan, nišān- [Y TY BWN.stn!, 2n-; nP?stn!, nP?n- | M nf?st, (nP5y-), N ~] set, seat, plant, found. nišāyišn [n£ din! | M n$?y-, v. niSástan] foundation. nišēb [niyp | N ~] declivity; astr. dejection. ~ig [-yk'] declining. nišēm (nidm | M nšym, N ~an] seat, perch. ~ag [-k'] residence, abode. niSin-, v. niSastan. niwāģ [nw k! | M ng, N nawa] music, song, melody. *niwé [nwyk! | (N nuwéd)] good news. *niwéy-, -išn, v. niwistan, *niwéyénidan [nwykyn-ytn'] = niwistan. niwistan, *niwéy- [nwstn', nwyd- | nwyk-] announce, consecrate. —išn(ih): announcement. nixwār- [nswb’l- | M nyxw’r-] hasten. -išn: haste. niyübag [nyd’pk' | M ny’bg] becoming, fitting, suitable. ~th: suitability. niyāģ [nyd?k! | M nyg, N niya] grandfather, ancestor. niyāyišn [xyd?dšn! | N ~if] prayer, praise. niyāz [nyd?c | M ny’z, N ~] need, want, misery. —ómand [2wmnd | N ~mand] needy. ~6mandih: poverty. niyē(x)šidan, niyē(x)š- [n(y)duhš-ytn! | M nywi-, N niyófidan] hear. ~išn: hearing. І nizār [nz?l | (P nyz?*wr), N ~] weak, feeble.
547:~th: visibility, appearance. paydagénidan, paydagén- [ ГОР hinin | M pyd'gynyd] reveal, explain. paydagihistan, paydagih- [py kyh-stn'] appear, be revealed, payg [pdh! | (P рар), N ~] foot-soldier, courier. *paygal [pyg'l | N payyāla, piyála] cup, goblet. -- gar [-A/] cup-maker. payģām [pgt”m! | M pyg’m, N pay(y)ām] message. ~bar LA | N -bar] messenger, apostle. paygos [p?tktvs | M p’ygws] district, province. paymān [pim”n! | M pym?n, N ~] measure, period; moderation; treaty. 6 — madan: reach maturity. ~ag [-k! | N ~a] period, measure, proportion. paymānīģ [ptm”nyk!] moderate. ~ih: moderation. *paymar [PK DWN < А pqdwn; p'tym'l] appointment, assignment. paymāy-, v. paymüdan. paymēģ [ptmwg | M pymwg] clothes, garment. paymóxtan, paymēz- [ptmwhtn!, ptmwe- | M pymwxt, bymwc-] don, wear. paymēūzan [ptmwen' | M pymwen] garment, dress. paymüdan, paymāy- [ptmwtn', ptm’d- | N ~] measure. *payram [p’tlm] the commonalty,-people. payrāstan, payrāy- [pt-, pyPstn!, pyPd- | M ругі, pyr!y-, N pērāstan) arrange, adorn. payrayag [руРак! | M pyr)yg, N pērāya] ornament, adornment. payrēģ [ptlwk'] light, brightness. paywand [ptwnd | (M руп), N ~] connection; offspring. paywand-, v. paywastan. paywasag [ptw’sk'] leather bag, wallet. paywastag [pteostk! | N ~a] continually. paywastan, paywand- [ptwstn!, ptwnd- М pywst, (pywyn-), N ~] join, connect. paywāz- [ptw’c- | M pyw’z-] answer, reply. ~ag [-k!], —i$n: response. paz-, v. poxtan. pāzand [p’cnd | N —] the Pahlavi commentaries on the scriptures (zand), transcribed in Avestan letters. pazd [pzd | — P] oppression, persecution. pazd- [pzd- | = M] blow, play (flute). pazdaģīh [pzdkyh] expulsion. pazdénidan, pazdén- [pzdyn-ytn' | P pzd-] frighten, chase. pāzen [p’c(y)n' | М pen, N pazan] ibex. pazüg [pzwk! | (N payūk, xabazdū)] guinea-worm. ~ í gühgard / gGhward: dung worm. pazzāftan [p> tn ' (M pzpt „intr.)] (cause to) ripen.
555:rabih [/pyh | M rbyh] noon, midday (heat). rad [/t! | N —] (spiritual) chief, master. АҺ: office of rad. rad [Pu | P rd, N ~] generous, liberal. ~ih: generosity, liberality. radag [itk! | M rdg, N rada] line, rank, row. radómand [/t?^wmnd] having a rad. rad-passag [/tps’k'] ceremonies of the gáhanbar festivals. radunay [/twny = Av. ratunaya-] one under the guidance of a rad. raftan, raw- [SGY TWN-tn! < А V sg’; lwb- | M rptn, rw-, N ~] go, move, proceed. ~išn, v. rawišn. raftār [/pt?] | N ~] goer. rag А! | M rg, N ~] vein. «ЛЬ: disposition, character. ray [/gy | P rg] quick, swift. ray [Pg | N —] meadow, plain. rah [/s, lh, [hy | M rh(y)] chariot, wagon. rah-, у. rastan. rah [Ps | M rh, N ~] road, way. rahag [/hk! | P rhg] = rag. rāh-dār [lsd] | N ~] brigand, highway robber. ~ih: brigandage. rahig [/syk!, Ikyk' | M rhyg, N rahi] child, page. ~ih: childhood. rāh-nimāy [Psnm?d | (M r’-hnmwd’r), № ~numa] guide. ram [Pm | М әт, N ~] peace; cal. 21st day. ram(ag) [/m(k') | P rm, N ram(a)] herd, flock. ráménidan, rāmēn- [Pmyn-ytn! | M ?myn-] give peace, pleasure. rāmišn [P min! | M rmyfn, N rāmi$] peace, ease, pleasure. ~ig [-vk! | N —z#] peaceful, at ease. ran [Рп! | N ~] thigh. P rān- [/^n-] fight. randidan, rand- [/nd-ytn! | N —] scratch, grate, abrade. rang [/ng | M rng, N —] colour, dye. ranj [Inc | P rnj, (M rnz), N ~] toil, trouble. ~ag [-k' | N —a] troubled. ranjénidan, ranjén- [/ncyn-ytn'] trouble.
562:sabuk [spwk! | N ~] light, easy. sabz [spz, sbz | N —] green, fresh. sad [roo | M sd, N ~] hundred. Sadwés [stwys | M sdwys] a star (Fomalhaut ?). ваб [KLBA < A klb | N ~] dog. Zeag [sk!] stone. sag [PR | P g] number. sagén [skyn! | M sygyn] stony. sagr [sg] | N sēr] sated, satiate. «ЛЬ: satiety. sahig [shyk' | M shyg, N sahi] worthy. ~th : worthiness. sahistan, sah- [MDMEN-stn' = A mdmh, V dmh | (M shyd, s‘y-)] seem; seem proper. ~išn: satisfaction. sahm [skm | = M, N ~] terror. ~gin [-k(y)n! | N —gin] terrible. ~genith : terribleness. sahög [shwk'] hare. sāk [s | (N sdw)] tribute. sal [SN T < A fnt | (M sr), N <] year. -sálag [SN TA, oli | N -sala] . . . -years-old. ~ih: age (of... years). salar [srd?] | M ffr, s’r’r, N ~] leader, master. ^h : authority. salwar Leikofl perennial. sāmān [?mn! | = M, N ~] limit, boundary. —Óómand [-’wmnd | M -wmnd] bounded. samór [smzl | N ~] sable (marten). sàn [?л! | N ~] kind, manner.
=== NYB ===
2320:košk [kwšk'] palace, castle 11422. — NP kušk (Turk lw. k"ošk); borrowed in Targ and Talm as qwé&q ‘tower, castle’, in Syr as gēšgā, whence Arab jausag-; Telegdi 254.
3376:ilgak [KLB"] dog 10!. 727. 9421.22, — < OP *saka- < *sn-ka- < the zero degree of *san-, the SW form of Av. (1610 sqq.) span-, OInd svan-; “the Medes call the dog oraxa'' Her. I,110 (the NW form of *saka-); NP sag.
3471:spāh-pat [sp'hpt'] army leader, general, passim; pl. cas. obl. ~-dn 28. 1113; — 72 ~ twelve leaders, of the twelve signs of the zodiac 7718, 794; 7 ~ the seven planets 7712, 7916, — Arm. lw. from Prth sparapet < *späda-pati-, v.s. v. späh; NP sipahbad.
7376:sag: !sak
=== ARY entries for sag ===
```


## [2026-09-06T22:39:50.065Z] TOOL CALL #40: Bash

```json
{
 "command": "ls site/pages/298.jpg 2>/dev/null; pdftoppm -f 298 -l 298 -r 200 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg298 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-06T22:39:52.054Z] TOOL RESULT

```
site/pages/298.jpg
total 124964
drwx------ 5 sfmqrb sfmqrb    12288 Sep  6 18:39 .
drwx------ 4 sfmqrb sfmqrb     4096 Sep  6 16:32 ..
-rw-rw-r-- 1 sfmqrb sfmqrb   533122 Sep  6 17:21 afm41_a.png
-rw-rw-r-- 1 sfmqrb sfmqrb   508509 Sep  6 17:21 afm41_b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   969829 Sep  6 17:21 afm41.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1322100 Sep  6 17:20 afm46.png
-rw-rw-r-- 1 sfmqrb sfmqrb   416305 Sep  6 17:20 afm46_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb      880 Sep  6 18:36 agents.txt
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
-rw-rw-r-- 1 sfmqrb sfmqrb     3974 Sep  6 16:37 crop_me2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3300 Sep  6 16:37 crop_me.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10236 Sep  6 16:39 crop_op2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4935 Sep  6 16:37 crop_op.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5599 Sep  6 16:37 crop_pers.png
-rw-rw-r-- 1 sfmqrb sfmqrb    22007 Sep  6 17:10 crop_sak.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5110 Sep  6 17:10 crop_sax.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4854 Sep  6 17:10 crop_shekar.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1249 Sep  6 17:05 crop_sirish.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30419 Sep  6 17:02 crop_skt267.png
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
-rw-rw-r-- 1 sfmqrb sfmqrb   125960 Sep  6 18:28 pg295hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    77133 Sep  6 18:28 pg295.png
-rw-rw-r-- 1 sfmqrb sfmqrb    56184 Sep  6 18:39 pg296.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66500 Sep  6 18:33 pg297.png
-rw-rw-r-- 1 sfmqrb sfmqrb    60960 Sep  6 18:39 pg298.png
-rw-rw-r-- 1 sfmqrb sfmqrb    52844 Sep  6 18:38 pg300.png
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
-rw-rw-r-- 1 sfmqrb sfmqrb     3698 Sep  6 18:19 zar_line.png
```


## [2026-09-06T22:39:57.384Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad\ngrep -n \"Sakā\\|Saka- sb\\|spāda- sb\\|späda- sb\\|Scythian\" kent_full.txt | head -20"
}
```


## [2026-09-06T22:39:57.421Z] TOOL CALL #42: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg298.png"
}
```


### [2026-09-06T22:39:57.442Z] TOOL RESULT

```
1575:the medieval Sogdian; Scythian, the language or 
1651:of northeastern Scythian, in which there are 
1698:gion of the Caucasus; derived from the Scythian 
3978:Pointed-Cap Scythians’. 
3984:Amyrgian Scythians’. 
4249:zb, only in Median words; nz only in a Scythian 
8421:(Bactrian) Frada-; the Scythian Sku*xa-; un- 
8601:Хака ‘the Scythians’; Sug(u)da ‘Sogdiana’; 
12126:5 (and DH 4) hacé Факат ‘from the Scythians’; 
18787:Scythians . .. (= DB 5.15-7). 
19005:DBk: This is Skunkha the Scythian. 
19200:Scythians, Maka. | 
19242:kingdom which 1 hold, from the Scythians who 
19371:Gandara, Sind, Amyrgian Scythians, Scythians 
19374:Scythians who are across the sea, Skudra, petasos- 
19710:DN XV: This is the Scythian with pointed cap. 
21281:docia, Dahae, Amyrgian Scythians, Pointed-Cap 
21282:Scythians, Skudra, men of Akaufaka, Libyans, 
21932:15 the Amyrgian Scythian. 15. This is the Pointed- 
21933:Cap Scythian. 16. This is the Babylonian. 17.
```


### [2026-09-06T22:39:57.777Z] TOOL RESULT

```

```


## [2026-09-06T22:39:57.775Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T22:40:12.344Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad\ngrep -n \"Saka\" kent_full.txt | sed -n '1,60p' | tail -40\necho \"=== spada lexicon ===\"\ngrep -n \"späda- sb\\|spada- sb\\|spāda- sb\\|spáda- sb\\|spdda\" kent_full.txt | head"
}
```


### [2026-09-06T22:40:12.405Z] TOOL RESULT

```
3986:А?Р 15 йат : Saka : tigraralud|a (as above). 
6372:Saka-, Sug(u)da-, Nisdya-, si*kabru-, and the 3 
7750:and Varka-zana-, Saka-, späda- in Taxma-spáda-, 
8600:ethnic Maciya; Saka or fem. бака Scythia’ or 
8721:Saka X Saká Saka 
8854:Suguda, Saka, Sparda, Mudréya, Uja боја, 
8938:bagaibi, vibaibiš, kamnarbis; Мааа, Sakai- 
8947:yam, aruvastam, dàtam, Sakatam, kartam, visam, 
9257:the place-names Arakadri$, KapiSakaniS, Viš- 
11728:Sakata ‘past’, to root ak- ‘pass’; and -gmata- 
16639:38 уй : XIV : тапса : Sakata : dha : yadiy : udapatatà ; hauv : kérahya : avaflü 
17120:8 tagui:Saka : абу : Dārayavauš : x8dyabiya : I martiya : Martiya : nā 
17276:98 m : aja : vasiy : Viyaxnahya : máhyà : X XII : raucabis : Sakata : dha : avatáSám : hamaranam : 
17655:47 ya : V :raucabis : Sakata : Sha : avatiaSàm : hamaranam : kartam : uta : ava 
18298:upariy | dlyalm [:] пабу : Sakaurim : naty : t[u]nuvatam, 
18299:confirming uparty[üyam] of WB, HK, Wb. KIA; Sakaurim 
18644:91 буа: араш : Saka : атка : Gha : uti :naiy : Auramazd 
18674:pasüva : hadja : Мата Kent. * (афту : Saka Kent, for 
18938:2 xa : hya : Saka 
19153:18 idus : Gadara : Saka : Maka : бабу 
19220:5 āmiy : hacd : Sakaibiá : tyaiy : para 
19672:XV iyam : Saka : tigraxaudé 
20643:4 m : dárayàmiy : һаса : Sakaibiš : tyaiy : pa 
21177:26 Katpatuka : Daha : Saka : haumavarga : Saka 
21895:: Saka : paradraiya : 
29111:Saka- adj. ‘Scythian’ ($116, $143.TIT) ; masc. 
29117:41, Saka-Studien [1939]). Elam. sa-ak-ga, АКК. 
29118:gi-mi(r)-ri, Gk. Хкобтѕ, Zeta. See also Saka-. 
29124:(1) ‘Scythian’: Saka пет. DBk 2. Saka npm. 
29135:(3) ‘Scythia’: Saka nsm. DB 1.16f; 2.8. 
29138:Saka- sb. ‘Scythia’, fem. of preceding, as sb. 
=== spada lexicon ===
5184:OP spdda- ‘army’, in the name of the Меде 
6354:sp in späda- ‘army’, in Taxmaspdda- (name of a 
8344:‘Having an upright mind’; Tarma-spdda- ‘Hav- 
25920:Taxmaspáda- sb. ‘Takhmaspada’, one of 
25922:"brave! + spdda- ‘army’ ($9.11, $108.11, $116, 
29252:späda- sb. ‘army’: GAv. spdda-, NPers. sipah,
```


## [2026-09-06T22:40:17.282Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad\nsed -n '29105,29150p' kent_full.txt\necho \"...\"\nsed -n '29245,29265p' kent_full.txt\necho \"=== page markers around ===\"\ngrep -n \"^20[5-9]$\\|^21[0-2]$\" kent_full.txt | tail -20"
}
```


### [2026-09-06T22:40:19.133Z] TOOL RESULT

```
fra- + să- ‘erect, build’: frasah|ya] s-aor. pass. 
($218.1, §220) DSf 27 (1st sg. act. }тазаһа[т| is 
possible, as proposed by Kent, JAOS 53.15, and 
approved by Schaeder, Ung. Jrb. 15.562.n2). 


Saka- adj. ‘Scythian’ ($116, $143.TIT) ; masc. 
sg. as sb., ‘Seythia’ as province or district; masc. 
pl. also as name of the province, often with modi- 
fiers (cf. JNES 2.304-5; for other discussion, cf. 
A. Hermann, AfOF, Betheft 1, Festschrift Oppen- 
heim 157-64 [1933], and J. Kluge, Klio, Веће 
41, Saka-Studien [1939]). Elam. sa-ak-ga, АКК. 
gi-mi(r)-ri, Gk. Хкобтѕ, Zeta. See also Saka-. 
Probably ‘dog’ in good sense, = ‘guardian of the 
flocks’, pIE *kyon-, Med. отака ‘dog’ (Herod. 
1.110), ef. Van Windekens, Beitr. z. Namen- 
forschung 1.98-102. | 

(1) ‘Scythian’: Saka пет. DBk 2. Saka npm. 


as пет. ($56.III) DN xv; A?P 14, 15, 24. Saká 
npm. DB 5.31. ака apm. DB 5.22", 25. Sa- 
kaibiš ipm. for abpm. (§252F) DPh 5; DH 4. 

(2) ‘Scythians’, a province of the Persian Em- 
pire: байа npm. DPe 18; DNa 25, 251, 28; DSe 
24^, 25^; XPh 26 bis. 

(3) ‘Scythia’: Saka nsm. DB 1.16f; 2.8. 


Saka- sb. ‘Scythia’, fem. of preceding, as sb. 
Saküm asf. DB 5.211. 


si"kabru- sh. ‘carnelian’: Elam. $7-/n-qa-ab-ru- 
iš, Akk. gi-in-ga-4--ru-ü (§6, §75.V, §116, §153.1; 
JAOS 54.57-8). For meaning, ef. Bleichsteiner, 
WZKM 37.101-3; Konig, Burgbau 62-3; Kent, 
JAOS 53.18, 54.37-8; ‘cinnabar’, Hz. AMI 3.64.5, 
ApI 303-5; ‘serpentine’, Gray, AJP 53.68-9. st- 
kabrus nsm. DSf 87. 


...
npf. DSf 45 (wrongly nsf. collective, Hz. AMI 
3.68-9). [stünä}] apf. DSg 3°. stünaya uncertain 
form, perhaps 18. (for -àya, $52.IIT, $176, §255; 
hardly adj. asm., with Hinz, ZDMG 95.250; 
wrongly Kent, JAOS 51.227-8) D'Sa 1, A?Hb. 


späda- sb. ‘army’: GAv. spdda-, NPers. sipah, 
Anglo-Indian spahi; in Taxmaspada-, cf. spá- 
maida- (76.V, $83.IT, $116, 5143.11). Possibly 
from pIE *kyd- ‘swell, be great’ (Gray, Lg. 25. 
377-8; cf. §90). ‘ 


spü&maida- sb. ‘camp, war’, meaning shown 
by АКК. version: cf. späda- ‘army’ (883.II), Av. 
hamaspa&maédaya- name of a diety and of his 
festival (Hz. ApI 310-5). spa@maidaya loc. sg. 
DNb 30f. 


=== page markers around ===
```


## [2026-09-06T22:40:36.060Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==293' POK_02.txt | sed -n '1,60p'\necho \"=========== next\"\nawk 'BEGIN{RS=\"\\f\"} NR==294' POK_02.txt | sed -n '1,25p'"
}
```


### [2026-09-06T22:40:38.044Z] TOOL RESULT

```
tvqov  ,Kleie'  trotz  des  noch  unklaren  l  nicht  zu  trennen  ist*  "^
da  aus  ,schütteln'  auch  ,ausschütteln,  streuen'  entwickelt  sein  kann,  igt mit  quatiö  möglicherweise  identisch  gr.  naaow^  att.  Tt&TTio  {Ttaoo)^  STtaaa iftda^Tjv)  ,streue,  besprenge'  (in   der  Webersprache  ,webe  bunte  Figuren  ' ein',  daher  xQmortaaiog  ,goldgestickt',  naoroQ  m. , Brautkammer,  Brautbett')  »t^ freilich  ist  ndaaco  zunächst  mit   dor.  TcfjV'  Ttfj  y,al  jtfjv  ertl  rov  ycardnaaat yial  -^axafcäaGuv  Hes.,  epidaur.  irtLTtfjv  (pdQy,av,ov  zu  verbinden;
ags.   hüdenian   , schütteln',   mhd.    hotzen   , laufen,   schaukeln*,   nisl.    hossa  " jSchütteln,  schleudern';  über  Formen  mit  s-  s.  unter  (s)küt-  ,rütteln*;        tf"
lit.  kutinetis  ,sich  zurechtzupfen'  (von  Vögeln),  kuntü,  atkutäu,  küsti  ,sich  '-- erholen'  (*aufrütteln).
WP.  I  511,  II  601,  WH.  II  399  f.
kuoi-,  kui-  ,wollen,  einladen'.
Ai.  keta-  m.  ,Wille,  Begierde,  Absicht,  Aufforderung,  Einladung',  ketana- n.  , Aufforderung,  Einladung';
gr.  'Aolxai'  yvvaLxcüv  irtLdvfxiaLi?)  Hes.,  zweifelhaft  auch  xtWa,  att.  xtTra (*xma)  ,krankhaftes  Gelüst  schwangerer  Frauen';
apr.  quäits  ,Wille',  quoi  ,er  will',  quoitU  ,wollen',  lit.  kvieciii,  kviesti ,einladen'.
WP.  I  475  f.,  WH.  I  714,  Trautmann  146  f.
kuon-,  kun-  ,Hund';  ursprüngl.  Nom.  Sg.  küuo{n),  Gen.  kunös,
Ai.  svä  und  s{u)vä  ,Hund',  Gen.  mnas,  Akk.  svänam,  Akk.  PI.  sünas] av,  spä,  spändm,  Gen.  PI.  sünam,  med.  (Herodot)  a/raxa  {*kun-ko-  ,hunde- artig'  :  ai.  svaka-  ,Wolf'),  mpers.  sak,  npers.  sag,  kurd.  sah,  wä'/i  sa6] aus  dem  Iran,  stammen  alb.  shak{;e)  ,Hündin',  gr.  anddayisg'  yivveg  Hes. (aus  *07tdAad£g)  und  russ.  sohdka  ,Hund';  vgl.  npers  salah]
arm.  sww.  Gen.  san  ,Hund' Jmit  unklarem  i);  nicht  gut  vereinbar  mit skund  ,Hündchen',  falls  aus  *kuon-to-,  -tä-,  oder  zu  den  oben  S.  564  unter *ken-    ,frisch    hervorkommen'    besprochenen    Tierjungenbezeichnungen?;
633
mit  fürs  Thrak.-Phryg.  auffälligem  Gutt.  1yd.  Kavöavlvig  ,x^^-^n^sS  thrak. (y^  Kccv-ödüjv  (zum  2.  Glied  s.  dhäu-  ,würgen');
o-r.  -Kvcov,  '/.wog  ,Huiid*  (xvvtsqoq  , hündischer,  d.  i.  unverschämter^  Sup. xvvratog',  zu  Kvvd(xvia  vgl.  lit.  sun-muse  ,Hundsfliege') ;
o-anz  unklar  lat.  canis  ,Hund',  cänes  ursprüngl.  altes  fem.  , Hündin', canlcula  (vgl.  ai.  §unl  f.)  hinsichtlich  des  a;  vielleicht  Einmischung  eines dem  mir-  cano,  cana  ,Wolfsjunges',  cymr.  cenaw  ,junger  Hund  oder  Wolf' /g.  3.  Icen-)  entsprechenden  Wortes  (so  auch  1yd.  Kav-da^ölrig'^);
air.  cü  (Gen.  con  ==  xwdg),  cymr.  ci  (PL  cwn  ==  -/.vveg,  lit.  sünes),  bret. corn.  ki  ,Hund*  aus  *Äwö;
got.  hunds,   aisl.  hundr^   ags.  hund,  ahd.  hunt  ,Hund'  (kun-tö-),  s.  oben ;
lit.  §uö  (Gen.  sufis)  ,Hund
=========== next
*  (zum  i-St.  geworden  in  lit.  dial.  sunis,  lett.  suns, apr.  sunis  ,Hund*) ;  ^Form  lett.  suntana  ,großer  Hund' ;  lett.  kuna  ,Hündin' wohl  mit  westidg.  Gutt.,  Trautmann  Bsl.  Wb.  310?  oder  das  Ä  von  kuca ds.  (Lockruf);  vgl.  Büga  Kalba  ir  s.  I  196;  ganz  fraglich  aber  russ. poln.  suka  , Hündin';
toch.  A  kuj  Obl.  korij  B  Nom.  ku.
Die  Bedeutung  von  lat.  canis  als  ,unglücklicher  Wurf  beim  Würfelspiel' kehrt  in  gr.  xvcov  wieder,  sowie  in  ai.  Sva-ghnin-  eigentlich  ,Hundetöter', d.  i.  ,der  die  schlechten  Würfe  vermeidende,  gewerbsmäßige,  auch  unred- liche Spieler' ;  vgl.  auch  gr.  y,ivdvvog  , Gefahr  (*Hundswurf)'  aus  *y,vv-dvvogy zu  ai.  dyütd  , Spiel'?  Schwyzer  Gr.  Gr.  1,  335  oben.
WP.  I  465 f.,  WH.  I  152 f.;  Kurylowicz  Accentuation  19;  nach  Specht Idg.  Dekl.  32,  121  f.  Ableitung  von  der  Farbwurzel  2.  keu-,  S.  594.
ktires-,  kuers-,  kurs-  , Gehölz,  Baum'??
Gr.  TtqXvog  , Steineiche',  falls  aus  *Ä;wfs-7io-s(?)  :  ^aX\.  prenne  ,arborem  gran- dem',  cymr.  corn.  bret.  prenn  ,Baum'  (*ku7'es-no-)',  ablaut.  air.  crann (*kurs-no-),  Gen.  cruinn  ds.,  cymr.  prys  (prysg)  , Gehölz'  (*kurs-to-)  ]  ags. hyrst  , Gebüsch,  Gehölz',  as.  ahd.  mnd.  hörst,  hurst  ds.,  nhd.  Horst ,Raubvogelnest'  (*ku2's-to-',  weniger  wahrscheinlich  oben  S.  548);  slav. *chvorst^,  ksl.  chvrastije,  russ.  chvörost  ,Reisig,  Strauch',  slov.  hrdst  , Eiche* (*kuors-to-?),  mit  unerklärtem  Anlaut.
WP.  I  524,  Morris- Jones  Welsh  Gr.  128,  Machek  Slavia  16  (1939),  182  f., Mikkola  ürslav.  Gr.  177.  J.  B.  Hofmann  (Etym.  Wb.  des  Gr.  284)  be- trachtet gr.  TZQLvog  wegen  des  kar.  ON  nglraaaog  als  vorgriechisch-klein- asiatisch.
Kh.'
kba  kha!  Interjektion  des  Lachens;  mit  z.  T.  einzelsprachlicher  Neu- schöpfung.
Ai.  hdkhati  (Gramm.)  ,lacht';  arm.  xaxank  , Gelächter',  gr.  xcr^d^cü (aus  *xax«?w)  flache  laut';  lat.  cachinnö,  -äre  ,hellauf  lachen',  cachinnus , Gelächter';  ahd.  kachazzen,  kichazzen,  ags.  ceahhettan  ,laut  lachen';  aksl. usw.  chochotati  ds. ;  vgl.  lit.  kikenti,  kiknoti  ,kichern'.
Ähnliche  Schallwurzel  käk-  ^auslachen'  in  gr.  xijxa^w  ,schmähe';  ahd. huohön  , spotten,  höhnen',  as.  höhi-llk  ^lächerlich';  mit  germ.  -k-:  ags. hocor  n.  , Spott'.
WP.  I  336,  WH.  I  126.  Vgl.  oben  S.  497  Jia  ha.
^  Die  bei  WP.  I  341,  348  f.,  399  angeführten  Wurzeln  khäd-  ,beißen',  khähh-  :  khöbh- jkraftlos',  kherw  ,graben'  sind  nicht  als  idg.  zu  erweisen,  ebensowenig  das  von  Specht (Idg.  Dekl.  263,  Anm.  4)  angesetzte  khä-mo-  , krumm';  die  von  ihm  (S.  256)  angeführten ai.  Beispiele  khalati-,  kharva-f  khara-.  khanda-,  khora-  sind  säm
```


## [2026-09-06T22:40:49.983Z] TOOL CALL #46: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-06T22:40:49.991Z] TOOL RESULT

```


```


## [2026-09-06T22:40:53.804Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B3%D9%BE%D8%A7%D9%87",
 "prompt": "Persian سپاه: give the full etymology section — Middle Persian form, Old Iranian/Proto-Iranian reconstruction, Avestan/Old Persian cognates, and the ultimate PIE root cited. Also any mention of سپهبد."
}
```


## [2026-09-06T22:40:56.107Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%E1%B8%B1w%E1%B9%93",
 "prompt": "Give the reconstruction, meaning, declension, and the list of descendants (especially Proto-Iranian/Avestan/Persian, Latin canis, Proto-Germanic *hundaz, Greek kuōn)."
}
```


### [2026-09-06T22:41:01.148Z] TOOL RESULT

```
# Etymology of سپاه (sipāh)

## Origin and Development

The word derives from **Middle Persian** _spʿh_ / _𐭮𐭯𐭠𐭧_ (spāh), which was "borrowed from Northwestern Iranian" languages. This traces back to Proto-Indo-Iranian *ćwáHdʰaH, ultimately from Proto-Indo-European *ḱwéh₁-dʰ-o-h₁, stemming from the root *ḱweh₁-/*ḱewh₁- meaning "to swell, be great."

## Cognates

Related words appear across ancient Iranian languages. Avestan shows _𐬯𐬏𐬌𐬛𐬌𐬌𐬁𐬌_ (sūidiiāi, "to swell, increase"), while Bactrian offers _σοδο_ (sodo/sūdo, "plenty"). Middle Persian derivatives include forms meaning "profit, advantage." Sanskrit _शवस्_ (śavas) meaning "strength, superiority" represents a possible cognate.

## Related Term: سپهبد (sepahbod)

One derived term mentioned is **سپهبد** (sepahbod), listed among words derived from the base سپاه. This compound combines the military term with additional Persian elements to denote a high-ranking military commander.
```


### [2026-09-06T22:41:02.113Z] TOOL RESULT

```
# Proto-Indo-European *ḱwṓ

**Reconstruction:** *ḱwṓ (masculine)

**Meaning:** "dog"

**Etymology:** From earlier *ḱwón-s. One theory suggests derivation from *péḱu + *-ō, possibly meaning "he of the sheep" (sheepdog), though this lacks support. The term has been compared with Old Chinese 犬 (*kʰʷeːnʔ, "dog").

**Declension:** Athematic, hysterokinetic n-stem noun with forms including nominative singular *ḱwṓ, genitive *ḱunés, and plural nominative *ḱwónes.

**Key Descendants:**
- **Proto-Iranian:** *ćwā́
- **Latin:** canēs, canis
- **Ancient Greek:** κύων (kúōn)
- **Proto-Germanic:** *hundaz
- **Armenian:** շուն (šun)
- **Hittite:** ku-wa-aš

The page notes alternative reconstructions including *ḱwōn ~ *ḱunós and *ḱúwōn.
```


## [2026-09-06T22:41:09.782Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B3%DA%AF",
 "prompt": "Persian سگ (sag) 'dog': give the full etymology — Middle Persian form, Proto-Iranian, Old Persian/Median forms, PIE root, and any note about the sg/sp alternation or Median spaka."
}
```


## [2026-09-06T22:41:10.728Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/canary",
 "prompt": "Give the full entry for canary (and any linked note on Canary Islands, Insula Canaria, canis). Also quote what it says about the French/Spanish route."
}
```


### [2026-09-06T22:41:16.317Z] TOOL RESULT

```
# Etymology of Persian سگ (sag) — "dog"

**Middle Persian**: The term derives from Middle Persian /sag/, which continued into modern Persian.

**Old Persian**: The Middle Persian form traces back to Old Persian *sakah, representing an Iranian cognate denoting canines.

**Proto-Iranian**: Old Persian *sakah developed from Proto-Iranian *cwā́, evidenced by comparisons with Avestan 𐬯𐬞𐬁 (spā) and Pashto سپی (spëy).

**Median Forms**: A related Iranian variant *spaka- appears in Old Median σπάκα (spáka), which produced Middle Median *aspak, ultimately yielding Old Armenian ասպակ (aspak).

**Proto-Indo-European Root**: All these forms descend from PIE *ḱwṓ, the ancestor for "dog" across Indo-European languages, including Sanskrit श्वन् (śvā́).

**The sg/sp Alternation**: The sg- versus sp- variation reflects phonetic shifts within Iranian languages. The Median *spaka- variant shows the "sp-" pattern, while the Persian line developed as "sg-," both deriving from the same Proto-Iranian ancestor.
```


### [2026-09-06T22:41:17.805Z] TOOL RESULT

```
# Etymology of Canary

## Full Entry

**canary (n.)** - A type of small songbird, first recorded in the 1650s (shortened from "Canary-bird," 1570s). The term also refers to a type of wine from the Canary Islands, attested from the 1580s.

## Language Route

The word traveled through Romance languages: "from French *canarie*, from Spanish *canario* 'canary bird,' literally 'of the Canary Islands.'"

## Origin of the Island Name

The Canary Islands derive from Latin *Insula Canaria*, described as the "largest of the Fortunate Isles, literally 'island of dogs'" (*canis* from the Proto-Indo-European root *kwon- meaning "dog").

## Two Theories for the Name

1. **Pliny's account**: The islands were "so called 'from its multitude of dogs of a huge size'"
2. **Competing theory**: The name may derive from the *Canarii*, a Berber people inhabiting the Moroccan coast opposite the islands who possibly settled there.

## Historical Note

Recent DNA analysis from 2019 indicates the indigenous population consisted of North African, Mediterranean, and sub-Saharan African lineages, potentially arriving around 100 C.E.
```


## [2026-09-06T22:41:20.482Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/kennel",
 "prompt": "Full entry for kennel (n.) — the Old North French / Vulgar Latin *canile chain from Latin canis."
}
```


## [2026-09-06T22:41:22.268Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://iranicaonline.org/articles/isfahan-i-general",
 "prompt": "What does Encyclopaedia Iranica say about the etymology/origin of the name Isfahan/Esfahan — Spahan, Aspadana, Old Iranian *spada- 'army'? Quote the relevant passage."
}
```


### [2026-09-06T22:41:24.557Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T22:41:27.255Z] TOOL RESULT

```
The server returned HTTP 504 Gateway Timeout.
Retry-After: 120

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-06T22:41:30.629Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Isfahan",
 "prompt": "Etymology of Isfahan / Esfahan: Middle Persian Spahān, Old Persian *spādānām, Aspadana (Ptolemy), 'armies'. Quote the etymology section."
}
```


## [2026-09-06T22:41:31.324Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/kennel",
 "prompt": "Etymology of English 'kennel' (dog house): Old Northern French / Anglo-Norman, Vulgar Latin *canile, from Latin canis."
}
```


### [2026-09-06T22:41:35.250Z] TOOL RESULT

```
# Etymology of Isfahan

According to the Wiktionary entry, Isfahan's name derives from Classical Persian through Old Persian origins. The source states: "Ultimately derived from Classical Persian _اِصْفَهَان_ (isfahān), from Old Persian _*spādānah_ ('[army](/wiki/army "army"), _adj._')" or similar forms meaning "of the armies."

The term traces back further to Proto-Iranian _*cwáHdah_, also meaning "army." This linguistic lineage reflects the city's historical significance in Persian civilization.
```


### [2026-09-06T22:41:38.044Z] TOOL RESULT

```
# Kennel: Definition and Etymology

A **kennel** primarily refers to "a house or shelter for a dog," though it has several related meanings.

## Main Definitions

The word carries multiple senses:

1. **Shelter**: A individual structure housing a dog
2. **Facility**: A place where dogs are reared or boarded
3. **Pack** (British): Dogs kept at a boarding facility collectively
4. **Animal burrow**: The hole of a fox or similar creature
5. **Obsolete usage**: A street gutter or drainage channel

## Etymology

The term has an interesting linguistic journey. It derives from Middle English through Anglo-Norman French, ultimately tracing back to Latin. The word came "from Latin canis," meaning dog, filtered through Vulgar Latin and Old French before entering English.

The modern sense developed from the Norman French word for dog shelter, which spread to other languages like Dutch and Finnish, where it was borrowed directly from English.
```


## [2026-09-06T22:41:49.568Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%B3%D9%BE%D8%A7%D9%87' --note 'page 298, root Kwon: Persian سپاه etymology (PIE *ḱweh₁- swell, NOT dog root)' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%E1%B8%B1w%E1%B9%93' --note 'page 298, root Kwon: PIE *ḱwṓ dog, descendants' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%B3%DA%AF' --note 'page 298, node 3: Persian سگ from OP *sakah / PIr *ćwā́' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/canary' --note 'page 298, nodes 13-18: canary < Fr canari < Sp canario < Insula Canaria < canis' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/kennel' --note 'page 298, node 14: kennel < Anglo-Norman < VL *canile < canis' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Isfahan' --note 'page 298, node 5: Isfahan < OP *spādānah army' 2>&1 | tail -3"
}
```


### [2026-09-06T22:41:53.547Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/405e56d870a3460b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e2ec7468377d4cbc.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ca16591994d02998.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/73980e188a31a383.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/fc7cb55afb90be3c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/067f610162bc4179.txt
```


## [2026-09-06T22:41:58.574Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HUB sag/sipah ===\"\ngrep -n \"sag\\b.*Hund\\|Hund'\\|sipäh\\|sipah\" HUB.txt | head -10\necho \"=== IEC Mann kuon ===\"\ngrep -n \"Hund\\b\\|dog\\b\" IEC.txt | grep -i \"kuon\\|kwon\\|canis\" | head -5\ngrep -n \"kuō\" IEC.txt | head -5\necho \"=== SKT hound ===\"\ngrep -n \"HOUND\\|Hound, a dog\" SKT.txt | head -5\necho \"=== LKT canari ===\"\ngrep -n -i \"kanarien\\|canari\" LKT.txt | head -5"
}
```


### [2026-09-06T22:41:58.684Z] TOOL RESULT

```
=== HUB sag/sipah ===
1675:403. Np. tola junger Hund' ist nicht = zd. tauruna^, da
1679:Hund' sein!
2667:^saka- = np. sag *Hund') angehoren.
4061:vgl. noch med. a-ndxa *Hund' (Hero dot), Dial, von Jezd: seva ZDMG.
6074:sprengen ; sipah *Heer' (jiid. pers. supdh H. 699) = zd, spada-;
6291:(Etym.?) H. 698; sipah 'Heer H. 699; sipar 'SchM H. 700;
6304:esel* = np. astar gegen skr. agvatara-] ^saka- *Hund' =
7561:tara-; sa^ Hund', medisch andau, zd. spa; — siyah *schwsirz
8588:1. Regelmassig: a) sag *Hund' = med. andxa, zd. spa
9684:p. 65, Nr. 593. Vgl. syr. LW. sagdes 'wie einen Hund', Hoff-
=== IEC Mann kuon ===
8554:kanós (“cockerel', lit. ‘carly singer); Lat. cano, Gre “sing, sound, play an instrument; canis ‘dog’; Osc. cf. af-kani, acc. sg. ((ósong', fr. *ad-^); MIr. canim beside Ir. canaim, v. ‘sing’; cana, gs canann ‘cub, whelp’; W canu, v. ‘sing’; cân, pl. canau, f. ‘song, poem’; Br. kana, v. as W; kân, m. as W; Cor. cana, v. as W; Go. hana ‘cockerel’; OHG hano, id.; ON hani, id.; Latv. sanu, ét ‘hum’; LW in Finn. kana ‘hen’
9266:Kuon-, cpds. see Eug & Kun- Skt. $van ‘dog’; Arm. San, Samb, gs. & abl. s. id.; Gk. (?) sam-, san-, in some plant-names, and perh. saíno, fut. sand (^wag; cringe, fawn’,
9366:Kuombhos *dog's lair, morass, bog; spongy, mossy, sumpy'. Cf. Kuð (Kuon-) + -bhos Arm. Samb, Lat 'reedbed'; Gk. somphós, adj. ‘boggy, hollow; ON hvammr, m. ‘grassy hol- low’; cf. Skt. $va-bhrab, -bhram “hole, pit
=== SKT hound ===
=== LKT canari ===
```


## [2026-09-06T22:42:20.886Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LEW canis ===\"\ngrep -n \"canis,\" LEW_1910.txt | head -3\necho \"=== LAT canis ===\"\ngrep -n \"canis\" LAT.txt | head -5\necho \"=== SKT hound ===\"\ngrep -n \"Hound\\|hound\" SKT.txt | head -5\necho \"=== ARY qanari/sag ===\"\ngrep -n \"قناری\\|قنار\" incoming/ARY/ARY_pages.txt | head -3\ngrep -n \"سگ (\" incoming/ARY/ARY_pages.txt | head -3\necho \"=== FSD canary ===\"\ngrep -n \"canary\" FSD_vol1.txt | head -3"
}
```


### [2026-09-06T22:42:21.005Z] TOOL RESULT

```
=== LEW canis ===
=== LAT canis ===
3427:athematique. Ponr l'-i-, cf.le role de -i- dans canis,iuuenis, etc., et
4401:en -i-, comme canis, mSnsis, etc., v. Ernout, Philologica, p.i3S et s.)
5162:de armillatus ; e.g. a. canis Prop.4,8,34. Cf.M.L.659; bret.arme} (?).
6431:L.L.7,33, dubitatur... in hoc, utrum primum una canis aut canes sit
8608:culmi pereunt, quod a rusticanis calamitas appellatur ; de m 3 me encore
=== SKT hound ===
2788:O&ninfi.  (I>.)  L.  catunur,  tietonging  (o a  Hog.  —  L.  canu,  a  dog ;  see  Hound.
7993:Grey;  the  same  as  Qrar. Greyhound.  (Scand.)  M.  E.  gniAptnu/.
7994:—  Icel  grtyhut%dr,  a  (jreyboiind.  —  Icel. gr^t  a  dog ;  kundr,  a  hound.  The  Icel. grty  is  also  used  ahru  in  the  same  sense  of prcyhoond  ;  ^.  greybaka,  a  bitch.  %  Not allietl  to  gray^  which  is  apelt  grdr  ia Icelandic
8395:Harrier  (i).  a  bare-hound ;  see  Hare.
8877:Hound,  a  dog.  (E.)  A.  S  Aund,  +  Du. hotiiif  Icel.  Auudr^  Dan.  Swed.  G.  AnnJ^ Goth,  kunds.  Allied  lo  L.  canis,  Gk. orvurr  (gen.  vwJi^,  Skt-  ^luff,  a  dog ;  al^io fo  Iri:>h  ru,  W,  ci^  a  dog,  Kuia,  stika^  a bitch.
=== ARY qanari/sag ===
=== FSD canary ===
12932:1.  One  learning  hls  alphabet;  a   novice.  2.  One  who  de-  al'nlsti  1   al'pist;  2   51'pist,  n.  Bird-seed  from  various vises  an  alphabet,  or  makes  a   special  study  of  alphabets.  crosses  [<  F.  alpiste,  <   Sp.  alpiste,  canary-seed.]
23545:The  lichen  from  which  archil  in  prepared  i* known  also  fto  the  canary  weed  or  orchilla weed.  Uhb  Did.  Arts.
42328:canary
```


## [2026-09-06T22:42:26.908Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '42326,42334p' FSD_vol1.txt | cut -c1-900\necho \"=== SKT kennel/canary ===\"\ngrep -n \"Kennel\\|Canary\" SKT.txt | head -5"
}
```


### [2026-09-06T22:42:26.984Z] TOOL RESULT

```
corncrake
eagle
canary
cotinga
egret
canvasback
coucal
eider-duck
capercaillie
=== SKT kennel/canary ===
2728:kennel  ( j),  a  gutter.  (F. »  L) tion  of  M.  E.  fa«^/.  a  channel :  i Canary,    a     bird,     a    wine,    • (Canary   Islands.)      All   named Canary  i&Iaods. Cancel;  see  Cancftr. Cancer,  (L)    L  %anfe^,  a  crib;  «h». 'eating*  tumour.  +  t'k.  xv^wdroc,  Shi. ka\ay  a  ciab ;  cf.  Skt.  hixrketn^t  hanL  N from  its  hard  shell.
9630:Kennel  (3);  «i
```


## [2026-09-06T22:42:30.996Z] TOOL CALL #59: Bash

```json
{
 "command": "sed -n '1,80p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-06T22:42:31.038Z] TOOL RESULT

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


## [2026-09-06T22:42:33.540Z] TOOL CALL #60: Bash

```json
{
 "command": "sed -n '80,140p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-06T22:42:33.584Z] TOOL RESULT

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


## [2026-09-06T22:43:00.964Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification\npython3 - <<'EOF'\nimport json,glob\nfor f in sorted(glob.glob('page-2*.json'))[-6:]:\n    d=json.load(open(f))\n    for e in d['entries']:\n        for n in e['nodes']:\n            if not n.get('words'):\n                print(f, json.dumps(n, ensure_ascii=False)[:900]); raise SystemExit\nEOF"
}
```


### [2026-09-06T22:43:03.038Z] TOOL RESULT

```
page-289.json {"id": 7, "lang": null, "words": "", "verdict": "unverified", "derivation": "An empty box, empty in the printed book too: the render of pdf p.289 (200 dpi, copied to data/verification/sources/refs/ocr/BOOK/289.png) shows a wide blank double-ruled rectangle to the right of the 'Old Persian sâ 1 / fra-sâ' box, joined to it by an arrow, with no language header, no reference and no word. Nothing to verify. Nourai's habit elsewhere is to leave such a box where he expected a Persian or English continuation and found none — here presumably a New Persian reflex of OP fra-sā-, which does not exist.", "derivation_fa": "جعبه‌ای خالی است و در خودِ کتاب هم خالی است: در تصویر صفحهٔ ۲۸۹ (که در data/verification/sources/refs/ocr/BOOK/289.png نگهداری شده) مستطیلی دوخطّه و تهی در سمت راست جعبهٔ «پارسی باستان sâ 1 / fra-sâ» دیده می‌شود که با پیکانی به آن پیوسته است، بی هیچ نام زبان، ارجاع یا واژه. چیزی برا
```


## [2026-09-06T22:43:07.948Z] TOOL CALL #62: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg298.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/298.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/298.png"
}
```


### [2026-09-06T22:43:08.080Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 60960 Sep  6 18:43 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/298.png
```


## [2026-09-06T22:51:13.562Z] TOOL CALL #63: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk298.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW = \"https://en.wiktionary.org/wiki/\"\n\nentry = {\n  \"entry\": 0,\n  \"root\": \"Kwon, Ka 2, Sua\",\n  \"verdict\": \"confirmed\",\n  \"modern_form\": \"PIE *ḱwṓ (older *ḱwón-s), gen. *ḱunés 'dog'\",\n  \"note\": \"The root box is right: Pokorny IEW 632 heads the article 'k̑uon-, k̑un- ‘Hund’; ursprüngl. Nom. Sg. k̑úuo(n), Gen. k̑unos', and Watkins/AHD has 'kwon-. Dog. [Pok. k̑uon- 632.]'. Nourai's three-part root name is his own shorthand for the three ablaut/stem shapes he collects under it: Kwon = the full grade *ḱwon- (Gk. kúōn, Gmc. *hundaz), Ka 2 = the Latin a-vocalism canis, Sua = the Indo-Iranian *ćwā- (Skt. śván-, Av. spā). All three are in Pokorny's article. The language label 'Indo-European' and the gloss 'dog' are correct. The one substantive problem on this page is not the root but a branch: the 'army' words (Av. spāδa-, OP spāda-, NP sepāh, Isfahan, Sogd. spʽδ) are hung under the dog root, and no modern authority — including Kent, whom Nourai cites for OP spāda- — accepts that; see nodes #4 and #7.\",\n  \"note_fa\": \"ریشهٔ هندواروپایی آغازین *ḱwṓ (کهن‌تر *ḱwón-s)، حالت اضافی *ḱunés، به معنی «سگ»؛ پوکورنی در فرهنگ ریشه‌شناسی هندواروپایی، ص ۶۳۲، همین ریشه را با همین معنا آورده و واتکینز (AHD) نیز آن را به همین صورت ثبت کرده است. سه‌نامی که نورایی برای ریشه آورده (Kwon، Ka 2، Sua) در واقع سه ستاکِ همان ریشه است: *ḱwon- (یونانی kúōn، ژرمنی *hundaz)، صورت لاتینی با a (canis) و ستاک هندوایرانی *ćwā- (سنسکریت śvan-، اوستایی spā). پس عنوان ریشه، برچسب زبانی و معنای آن هر سه درست است. اشکال اصلی این صفحه در خودِ ریشه نیست، بلکه در شاخه‌ای است که واژه‌های «سپاه» (اوستایی spāδa-، پارسی باستان spāda-، سغدی spʾδ، فارسی سپاه، اصفهان) را زیر ریشهٔ «سگ» نشانده است؛ هیچ منبع امروزی — حتی کِنت که خودِ نورایی به او ارجاع می‌دهد — این پیوند را نمی‌پذیرد (نگاه کنید به گره‌های ۴ و ۷).\",\n  \"sources\": [\n    W + \"Reconstruction:Proto-Indo-European/%E1%B8%B1w%E1%B9%93\"\n  ],\n  \"ref_check\": [\n    {\"ref\": \"POK:632\", \"status\": \"supports\",\n     \"note\": \"POK_02.txt \\\\f-leaf 292 (running number '633' printed inside it; leaf 288 = p.629, leaf 291 = p.632) carries the article: 'kuon-, kun- ,Hund‘; ursprüngl. Nom. Sg. küuo(n), Gen. kunos, / Ai. svä und s(u)vä ,Hund‘ ... av. spä, spänəm, Gen. Pl. sünam, med. (Herodot) σπάκα (*kun-ko- ,hundeartig‘) ... mpers. sak, npers. sag, kurd. sah ... lat. canis ,Hund‘ ... got. hunds, aisl. hundr, ags. hund, ahd. hunt ,Hund‘ (kun-tö-)'. Exactly the page Nourai cites and exactly the material of his dog branch. It says nothing at all about spāda- 'army'.\"},\n    {\"ref\": \"KLN:746\", \"status\": \"supports\",\n     \"note\": \"KLN_1966.txt \\\\f-leaf 401 (printed page number 746 on the leaf) s.v. 'hound, n., dog': 'These words derive from a dental enlargement of I.-E. base *kwon-, ‘dog’, whence OI. svan-, Vedic suvan-, Avestic spa (gen. sunō), Medean spaka (whence Russ. sobaka), Toch. A ku, Arm. shun, Gk. κύων, L. canis ... Cp. also canaille, Canidae, canine, Canis, chenille, kennel.' Confirms root, node #1, #11-#12 and #13-#14 in one place.\"},\n    {\"ref\": \"BQT:1155\", \"status\": \"partial\",\n     \"note\": \"Borhan-e Qate’ is a Persian dictionary, not an IE etymological work, so it cannot support an IE root; it supports only the Persian end of the chain. In BQT_v2_pages.txt the سگ article with Mo‘in's etymological footnote stands on \\\\f-leaf 619 (running-head arithmetic from the leaves whose numerals the OCR does recover — leaf 588 = p.1127, leaf 589 = p.1129, leaf 594 = p.1133 — puts that leaf at p.1158-1160, i.e. within a page or three of Nourai's 1155). The footnote lists the dialect cognates in Latin letters: 'کردی hes (=seh) ... سکد (se) ... nûs ... کاشانی sipl, espê, esbé ... سمنانی psA', i.e. Mo‘in reproducing Horn's list.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. kwon-\", \"stance\": \"supports\",\n     \"note\": \"AHD_watkins1985.txt: 'kwon-. Dog. 1. Greek kuōn, dog: CYNIC ... 2. Suffixed zero-grade form *kwn-to- in Germanic *hundaz in: a. Old English hund, dog: HOUND ... 3. Nominative form *kwō in Welsh ci, dog: CORGI. 4. Variant *kan-i- in Latin canis, dog: CANAILLE, CANARY, CANICULA, CANINE, CHENILLE, KENNEL. [Pok. k̑uon- 632.]' Watkins' own index lines confirm CANARY kwon- and KENNEL kwon-.\"},\n    {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 465 f. (cited by Pokorny at IEW 633)\", \"stance\": \"supports\",\n     \"note\": \"Pokorny closes the k̑uon- article 'WP. I 465 f., WH. I 152 f.' — i.e. Walde-Pokorny Bd. I 465 is the parallel treatment of the same root; Bd. I-II of WLD are not among the local OCR files (only WLD_band3.txt, the index volume), so the reference is verified only through Pokorny's own back-reference.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann col. 'Kuon-'\", \"stance\": \"supports\",\n     \"note\": \"IEC.txt line 9266: 'Kuon-, cpds. see Kuo & Kun- | Skt. śvan ‘dog’; Arm. šun, šamb, gs. & abl. s. id.; Gk. (?) sain-...' Mann sets up the same root.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 3.61 DOG, p.180\", \"stance\": \"supports\",\n     \"note\": \"SYN.txt line 4811, table '3.61 DOG': 'Grk. κύων ... Lat. canis ... OE hund ... Skt. śvan- / Av. span-'. Buck's inherited-word list for 'dog' is precisely Nourai's set.\"}\n  ],\n  \"nodes\": []\n}\n\nN = entry[\"nodes\"]\n\nN.append({\n  \"id\": 1, \"lang\": \"Avestan / Old Persian\",\n  \"words\": \"spâ 1, sŭnô; spakâ\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Avestan spā (nom. sg.) 'dog', acc. spānəm, gen. pl. sūnąm — an athematic hysterokinetic n-stem continuing PIE nom. *ḱwṓ, gen. *ḱunés; the strong stem gives spā/spān-, the weak stem sūn- (PIE *ḱun- > Ir. *śun- > Av. sūn-), so Nourai's pair 'spâ 1, sŭnô' is the correct nom./gen. couple of one paradigm. Bartholomae AiW s.v. 'j. ¹span- : spā m. ‘Hund’' documents both, with the Pahlavi gloss sak and 'ai. śvā ... np. vgl. sag'. spakā is not, strictly, Avestan-and-Old-Persian: it is the Median form σπάκα that Herodotus I.110 reports ('the Medes call the dog spaka'), a *ḱun-ko- adjective 'dog-like' substantivised; Avestan has the matching adjective spaka- 'hundeartig, Hunds-' (Vd. 14.5), and Bartholomae's entry for it explicitly cross-refers to Herodotus. The label is therefore a shade loose — Old Persian has no attested word for 'dog' at all — but the forms and the descent from the root are right.\",\n  \"derivation_fa\": \"اوستایی spā «سگ» (حالت فاعلی)، مفعولی spānəm، اضافی جمع sūnąm؛ این واژه ستاکِ n با تکیهٔ جابه‌جاشونده است و دنبالهٔ صورت هندواروپایی *ḱwṓ (اضافی *ḱunés) به‌شمار می‌رود: ستاک قوی spā/spān- و ستاک ضعیف sūn- (از *ḱun-). پس جفت «spâ / sŭnô» که نورایی آورده همان صورت فاعلی و اضافیِ یک صرف است. بارتولومه در فرهنگ ایرانی باستان ذیل span- هر دو را آورده و برابر پهلوی آن را sak و فارسی نو را sag دانسته است. اما spakā به‌دقت اوستایی یا پارسی باستان نیست؛ صورت مادی σπάκα است که هرودوت (کتاب یکم، بند ۱۱۰) گزارش کرده: «مادها سگ را spaka می‌خوانند»؛ این صفتِ *ḱun-ko- «سگ‌سان» است و اوستایی نیز صفت spaka- را دارد. بنابراین برچسب «اوستایی/پارسی باستان» کمی سهل‌انگارانه است — در پارسی باستان اصلاً واژه‌ای برای «سگ» ثبت نشده — ولی خودِ صورت‌ها و پیوندشان با ریشه درست است.\",\n  \"sources\": [W + \"Reconstruction:Proto-Indo-European/%E1%B8%B1w%E1%B9%93\", W + \"%D8%B3%DA%AF\"],\n  \"ref_check\": [\n    {\"ref\": \"POK:632\", \"status\": \"supports\",\n     \"note\": \"POK_02.txt leaf 292: 'av. spä, spänəm, Gen. Pl. sünam, med. (Herodot) σπάκα (*kun-ko- ,hundeartig‘ : ai. svaka- ,Wolf‘)'. Pokorny gives Nourai's spā, sūn- and spaka in one line, and marks spaka as Median.\"},\n    {\"ref\": \"KLN:746\", \"status\": \"supports\",\n     \"note\": \"KLN_1966.txt leaf 401 (p.746) s.v. hound: 'Avestic spa (gen. sunō), Medean spaka (whence Russ. sobaka)'.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"BRT\", \"where\": \"AiW col. 1609-1612, s.vv. spaka-, ¹span-\", \"stance\": \"supports\",\n     \"note\": \"BRT.txt: '• j. spaka- Adj. ‘hundeartig, Hunds-’ ... Ableit. aus ¹span-. — Vgl. HERODOT i.110: σπάκα τὴν κύνα καλέουσι οἱ Μῆδοι — Pü.: sak.' and '• j. ¹span- : spā m. ‘Hund’ ... ai. śvā, śūnaḥ; afγ. spai, np. vgl. sag. — Pü.: sak.' Bartholomae confirms the paradigm, the Median attribution of spaka and the Pahlavi/NP continuations.\"},\n    {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon s.v. Saka-\", \"stance\": \"partial\",\n     \"note\": \"Kent has no Old Persian common noun 'dog'; the only place he brings the word in is s.v. Saka- (Lexicon, p.209): 'Probably ‘dog’ in good sense, = ‘guardian of the flocks’, pIE *k̑uon-, Med. σπάκα ‘dog’ (Herod. 1.110)'. So the 'Old Persian' half of Nourai's language label rests on that speculation, not on an attestation.\"},\n    {\"src\": \"HUB\", \"where\": \"Persische Studien, p.~c. 8588 / 2667\", \"stance\": \"supports\",\n     \"note\": \"HUB.txt: 'a) sag ‘Hund’ = med. σπάκα, zd. spā' and '*saka- = np. sag ‘Hund’'. Hübschmann too takes the Persian word from a *saka- beside the Median spaka-.\"}\n  ]\n})\n\nN.append({\n  \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"sak\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Middle Persian sag, written with the Aramaic heterogram KLBʾ (from Aram. kalbā 'dog'), and in Book-Pahlavi transcription often given as sak because Pahlavi script does not distinguish g from k. MacKenzie's Concise Pahlavi Dictionary prints 'sag [KLBAʾ < A klb | N ~] dog'. The form is the south-western Iranian outcome of the same n-stem: the weak stem *ću(n)- with the -ka- suffix that the Median form also shows, i.e. OIr. *sa(n)ka- > MP sag; Iranian *ć- gives Persian s- (against the sp- of Avestan/Median/Pashto), so sag and spaka are the SW and NW reflexes of one word. Nourai's 'sak' is thus a legitimate transliteration of the Pahlavi spelling, not an error; Pokorny writes the same 'mpers. sak'.\",\n  \"derivation_fa\": \"فارسی میانه sag، که در دبیرهٔ پهلوی با هزوارشِ آرامی KLBʾ (از kalbā «سگ») نوشته می‌شود و چون خطّ پهلوی «ک» و «گ» را از هم جدا نمی‌کند، آن را sak هم آوانویسی کرده‌اند؛ مکنزی در فرهنگ کوچک پهلوی می‌آورد: «sag [KLBAʾ] dog». این صورت بازماندهٔ جنوب‌غربیِ همان ستاک است: ستاک ضعیف *ću(n)- به‌همراه پسوند -ka- (همان پسوندی که در صورت مادی spaka نیز هست)، یعنی ایرانی باستان *sa(n)ka- > پهلوی sag. صامت آغازینِ ایرانی *ć در فارسی به s بدل شده (در برابر sp اوستایی و مادی و پشتو)، پس sag و spaka دو بازتاب جنوب‌غربی و شمال‌غربیِ یک واژه‌اند. بنابراین «sak» نورایی آوانویسیِ درستِ املای پهلوی است، نه خطا؛ پوکورنی نیز همین «mpers. sak» را نوشته است.\",\n  \"sources\": [W + \"%D8%B3%DA%AF\"],\n  \"ref_check\": [\n    {\"ref\": \"HRN:164\", \"status\": \"supports\",\n     \"note\": \"HRN.txt \\\\f-leaf 185 (the leaf opens '— 164 —'), no. 743: 'seg ‘Hund’ ... medisch σπάκα (τὴν κύνα καλέουσι οἱ Μῆδοι), Herod. I,110; aw. span- ‘Hund’; phlv. sak, sag; ai. çvan-; arm. šun.' Horn gives exactly Nourai's Pahlavi sak/sag between the Avestan and the New Persian word.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"PHD\", \"where\": \"MacKenzie p.72 s.v. sag\", \"stance\": \"supports\",\n     \"note\": \"PHD.txt: 'sag [KLBA < A klb | N ~] dog.' — the heterogram-written MP word, with New Persian sag as its continuation.\"},\n    {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (Glossary), s.v. sag/sak\", \"stance\": \"partial\",\n     \"note\": \"NYB_vol2_glossary.txt: 'sag [KLBʾ] dog ... < OP *saka- < *sn̥-ka- < the zero degree of *san-, the SW form of Av. (1610 sqq.) span-, OInd. śvan-; ‘the Medes call the dog σπάκα’ Her. I,110 (the NW form of *saka-); NP sag.' Nyberg confirms the word and the descent from the dog root, but routes it through a South-Western *saka-, i.e. NOT directly from the Avestan/Median sp-form that Nourai's arrow draws.\"},\n    {\"src\": \"BRT\", \"where\": \"AiW s.v. ¹span-, spaka-\", \"stance\": \"supports\",\n     \"note\": \"Bartholomae's Pahlavi-gloss line for both entries is simply 'Pü.: sak'.\"}\n  ]\n})\n\nN.append({\n  \"id\": 3, \"lang\": \"Persian\", \"words\": \"sag «سگ»\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"New Persian سگ sag 'dog' continues Middle Persian sag unchanged — the commonest of all Persian animal names, in the Shahnameh and every later text. The whole chain is uncontroversial: PIE *ḱwṓ / weak stem *ḱun- > Proto-Iranian *ćwā / *ću(n)-ka- > SW Old Iranian *saka- > MP sag (KLBʾ) > NP سگ. The sp-/s- doublet survives beside it in the Iranian dialects Horn lists (Kurd. seh, Talishi sipā, Kashani espa/esbe, Semnani asp-), so Persian s- against Avestan sp- is the regular South-Western treatment of Ir. *ć and not a difficulty. The Arabic-looking سگ has nothing Semitic about it; the Pahlavi heterogram KLBʾ is a writing convention only.\",\n  \"derivation_fa\": \"فارسی نو «سگ» دنبالهٔ بی‌تغییرِ فارسی میانهٔ sag است؛ رایج‌ترین نام جانور در فارسی، از شاهنامه تا امروز. زنجیرهٔ آن بی‌مناقشه است: هندواروپایی *ḱwṓ (ستاک ضعیف *ḱun-) < ایرانی آغازین *ćwā / *ću(n)-ka- < ایرانی باستانِ جنوب‌غربی *saka- < پهلوی sag < فارسی «سگ». جفتِ sp-/s- هنوز در گویش‌های ایرانی زنده است — کردی seh، تالشی sipā، کاشانی espa/esbe، سمنانی asp- — که هرن و به‌پیروی از او معین در حاشیهٔ برهان قاطع فهرست کرده‌اند؛ پس s فارسی در برابر sp اوستایی، تحول قاعده‌مندِ *ć ایرانی در شاخهٔ جنوب‌غربی است، نه استثنا. هزوارشِ KLBʾ در پهلوی صرفاً قرارداد نگارشی است و ربطی به سامی‌بودن واژه ندارد. ادعای نورایی در این گره کاملاً درست است.\",\n  \"sources\": [W + \"%D8%B3%DA%AF\"],\n  \"ref_check\": [\n    {\"ref\": \"BQT:1155\", \"status\": \"supports\",\n     \"note\": \"BQT_v2_pages.txt \\\\f-leaf 619 (≈ printed p.1158-1160 by the recoverable running heads: leaf 588=p.1127, 589=p.1129, 594=p.1133) carries the سگ article; Mo‘in's footnote there is printed in Latin letters and the OCR still yields 'کردی hes' (= seh), '(se)', 'nûs', 'کاشانی sipl, espê, esbé', 'سمنانی' + a form beginning Asp- — i.e. Mo‘in reproducing Horn no.743. Supports the entry; the page number may be a page or two off Nourai's 1155 in this scan.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"HRN\", \"where\": \"Grundriss no. 743, p.164\", \"stance\": \"supports\",\n     \"note\": \"'743. seg ‘Hund’ ... aw. span- ‘Hund’; phlv. sak, sag; ai. çvan-; arm. šun (H. No. 224). kurd. seh (d. i. se) ‘Hund’, Plur. sān, seiān; afγ. spai.'\"},\n    {\"src\": \"HUB\", \"where\": \"Persische Studien, 'Regelmässig' list\", \"stance\": \"supports\",\n     \"note\": \"HUB.txt: 'a) sag ‘Hund’ = med. σπάκα, zd. spā' — Hübschmann lists sag among the regular SW Iranian correspondences.\"},\n    {\"src\": \"BQT\", \"where\": \"vol. 1, leaf 336 (≈ p.118), s.v. اسپه\", \"stance\": \"supports\",\n     \"note\": \"An independent Borhan witness to the same word from the other side of the alphabet: 'اسپه ... مخفف اسپاه است که لشکر و سپاه باشد - و سگ را نیز گویند که بتازی کلب خوانند، و با پای فارسی هم گفته‌اند' — Borhan itself records that اسپه means both 'army' and 'dog', i.e. it preserves the sp-form of the dog word beside the homophonous army word.\"}\n  ]\n})\n\nN.append({\n  \"id\": 4, \"lang\": \"Avestan\",\n  \"words\": \"spâda, spâtha; spatha-paiti; Aspadâna\",\n  \"verdict\": \"disputed\",\n  \"derivation\": \"The words are all genuine and Nourai's internal chain is right; what is wrong is hanging them on the dog root. Avestan spāδa- m. 'army' (Nourai's 'spâda, spâtha' is one word in two transliterations of the interdental δ), spāδa-paiti- 'army-chief' and the toponym behind Ptolemy's Aspadána are all built on spāδa-. But Avestan sp- here is not the sp- of spā 'dog': it goes back to Proto-Iranian *ćwāHda- < PIE *ḱweh₁-dʰ-o- from the root *ḱweh₁-/*ḱewh₁- 'to swell, be great' — the root of Av. sūidiiāi 'to swell, increase', Bactrian σοδο 'plenty', Skt. śávas- 'strength', MP sūd 'profit'. The semantic development is 'swelling, mass' → 'host, army'. Kent, whom Nourai himself cites for the Old Persian member (KNT:210), writes 'Possibly from pIE *k̑wō- ‘swell, be great’ (Gray, Lg. 25.377-8)'; Bartholomae likewise refers the group to an Aryan *sphā-. Pokorny p.632, Nourai's other reference, treats k̑uon- 'Hund' and says nothing whatever about spāδa-. No modern authority derives 'army' from 'dog'. The chart's own placement is therefore a false etymology; each individual form in the box is nevertheless correctly given.\",\n  \"derivation_fa\": \"خودِ واژه‌ها درست‌اند و زنجیرهٔ درونیِ نورایی هم درست است؛ آنچه نادرست است، آویختنِ این شاخه به ریشهٔ «سگ» است. اوستایی spāδa- «سپاه، لشکر» (آنچه نورایی spâda و spâtha نوشته، یک واژه است با دو آوانویسیِ همان δ میان‌دندانی)، spāδa-paiti- «سپهبد، سرلشکر» و نامِ جایی که در جغرافیای بطلمیوس Aspadána آمده، همه بر پایهٔ spāδa- ساخته شده‌اند. اما sp در این واژه همان sp در spā «سگ» نیست: به ایرانی آغازین *ćwāHda- و از آنجا به هندواروپایی *ḱweh₁-dʰ-o- از ریشهٔ *ḱweh₁- «آماسیدن، بزرگ شدن» می‌رسد — همان ریشه‌ای که اوستایی sūidiiāi «فزونی یافتن»، بلخی σοδο «فراوانی»، سنسکریت śávas- «توان» و فارسی میانهٔ sūd «سود» از آن‌اند. تحول معنایی: «آماس، انبوه» ← «انبوهِ مردان، لشکر». کِنت — همان مرجعی که نورایی برای صورت پارسی باستان به او ارجاع می‌دهد — می‌نویسد «شاید از *ḱwō- به معنی آماسیدن»؛ بارتولومه نیز این گروه را به *sphā- آریایی می‌برد. پوکورنی در ص ۶۳۲ فقط ریشهٔ «سگ» را آورده و هیچ اشاره‌ای به spāδa- ندارد. پس پژوهش امروزی این پیوند را رد می‌کند: «سپاه» از «سگ» نیامده است، هرچند تک‌تکِ صورت‌های درون این جعبه درست ثبت شده‌اند.\",\n  \"sources\": [W + \"%D8%B3%D9%BE%D8%A7%D9%87\", W + \"Isfahan\"],\n  \"ref_check\": [\n    {\"ref\": \"POK:632\", \"status\": \"not_found\",\n     \"note\": \"POK_02.txt leaf 292-293 is the complete k̑uon- 'Hund' article (WP. I 465 f., WH. I 152 f.); it lists Skt., Avestan, Median, MP, NP, Armenian, Greek, Latin, Celtic, Germanic, Baltic, Slavic and Tocharian dog-words and contains no spāδa-, no spāda-, no Aspadāna and no 'Heer'. The reference does not support the arrow.\"},\n    {\"ref\": \"FIB:207\", \"status\": \"not_checked\",\n     \"note\": \"FIB = Pur-Davud, Farhang-e Iran-e Bastan I (1326/1947). refs_online.json marks it kind=website with no local copy and no archive.org scan (only the noorlib viewer, which needs a browser session). Not accessible from here.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon s.v. späda-, p.210\", \"stance\": \"contradicts\",\n     \"note\": \"'späda- sb. ‘army’: GAv. spāda-, NPers. sipah, Anglo-Indian spahi; in Taxmaspāda-, cf. spāθmaida- ... Possibly from pIE *k̑wō- ‘swell, be great’ (Gray, Lg. 25.377-8).' Kent connects it to a 'swell' root, explicitly not to k̑uon- 'dog' — and in his phonology section he adds 'sp in späda- ‘army’, in Taxmaspāda- ... (only in Iranian)'.\"},\n    {\"src\": \"BRT\", \"where\": \"AiW, note appended to the spa-/spā- series (col. 1613)\", \"stance\": \"contradicts\",\n     \"note\": \"BRT.txt at the foot of the spayaθra-/spar- column: 'Pü.: späh ‘Heer’ ...', and the etymological note refers the group to an Aryan *sphā-/*sqā-; Bartholomae keeps ¹span- 'Hund' (col. 1610f.) and the spāδa- 'Heer' group in separate articles with separate etymologies.\"},\n    {\"src\": \"HRN\", \"where\": \"Grundriss no. 699, p.155\", \"stance\": \"partial\",\n     \"note\": \"'699. sipah ‘Heer’, sipeh, ispehbed (arab. isbahbud) ... ap. Taxma-späda-; aw. spaδa- ‘Heer’; phlv. spāh, spāhpat, arm. LW. spāh, aspahapet.' Horn confirms every form in Nourai's box and the descent NP < MP < Av./OP, but offers no link to spā 'dog' — and puts the two words 250 pages and 44 numbers apart.\"}\n  ]\n})\n\nN.append({\n  \"id\": 5, \"lang\": \"Persian\",\n  \"words\": \"sepâh «سپاه (سپه)»; sepahbod «سپهبد (سپهسالار)»; Esfahân «اصفهان»\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Taken as drawn from its own parent (the Avestan spāδa- box), this node is right in every part. (i) سپاه sepāh/sipāh 'army' < MP spāh [spʾh] < OIr. *spāda-; the intervocalic Iranian -δ- of Av. spāδa- is lost and compensated by -h in the Middle Persian form (MacKenzie 'spāh ... N sipah'), poetic سپه sepah being the shortened variant. Middle Persian actually borrowed the word from a north-western dialect, which is why it keeps sp- rather than showing the SW treatment. (ii) سپهبد sepahbod < MP spāhbed [spʾh-pt] < OIr. *spāda-pati- 'lord of the army', the Sasanian title of the four quarter-generals; Armenian borrowed it as sparapet from Parthian, and Arabic took it as iṣbahbad/isfahbad, whence it came back into Persian usage. سپهسالار is a later New Persian synonym (سپه + Ar.-Pers. سالار), not a continuation of the Old Iranian compound. (iii) اصفهان Esfahān < MP Spāhān < OIr. *spādānām '(place) of the armies', a genitive plural used as a place name; Ptolemy's Aspadána and Middle Persian Spāhān are the same name, and the Arabic-script اصفهان with ص and initial ا is the Arabised spelling of Isfahān. Only the ultimate attachment to the 'dog' root (node #4) is wrong.\",\n  \"derivation_fa\": \"اگر این گره را نسبت به پدرِ خودش (جعبهٔ اوستایی spāδa-) بسنجیم، همه‌چیزش درست است. ۱) «سپاه» از فارسی میانهٔ spāh [spʾh] و آن از ایرانی باستان *spāda-؛ δ میان‌واکه‌ایِ اوستایی افتاده و به‌جای آن h نشسته است (مکنزی: spāh … فارسی نو sipah)؛ «سپه» صورت کوتاه‌شدهٔ شعری است. نکته آنکه فارسی میانه این واژه را از گویشی شمال‌غربی وام گرفته و از همین‌رو sp آغازین را نگه داشته است. ۲) «سپهبد» از فارسی میانهٔ spāhbed [spʾh-pt] و آن از *spāda-pati- «سرورِ سپاه»، لقب چهار سپهبدِ ساسانی؛ ارمنی آن را از پارتی به‌صورت sparapet وام گرفت و عربی آن را «اصبهبذ/اسفهبد» معرّب کرد. «سپهسالار» ترکیبِ متأخرِ فارسی نو است (سپه + سالار) نه دنبالهٔ همان ترکیب ایرانی باستان. ۳) «اصفهان» از فارسی میانهٔ Spāhān و آن از *spādānām، حالت اضافیِ جمع به معنی «(جایگاهِ) سپاهیان»؛ Aspadána در جغرافیای بطلمیوس همین نام است و املای «اصفهان» با صاد، صورت معرّبِ «اسپهان/اسفهان» است. تنها ایرادِ کار، پیوندِ نهاییِ این شاخه با ریشهٔ «سگ» است (گرهٔ ۴).\",\n  \"sources\": [W + \"%D8%B3%D9%BE%D8%A7%D9%87\", W + \"Isfahan\"],\n  \"ref_check\": [\n    {\"ref\": \"BQT:118,1087\", \"status\": \"supports\",\n     \"note\": \"Two Borhan pages, one per word, and both check out. BQT_v1_pages.txt leaf 336 (≈ printed p.118, by the vol.-1 offset printed ≈ leaf − 218) s.v. اسپه: 'مخفف اسپاه است که لشکر و سپاه باشد ... اسپهان' — with the اسپهان/اصفهان article on the neighbouring leaves 333-336 ('اسفهان', 'اصنهان ... صفحهٔ ۱۲۳'). BQT_v2_pages.txt leaf 547-548 (≈ printed p.1087 by the vol.-2 offset leaf + 540) is the سپاه article — leaf 548 still shows the idiom 'گویند: سپاس دارم' immediately after it. Both of Nourai's page numbers land on the right articles.\"},\n    {\"ref\": \"HRN:155\", \"status\": \"supports\",\n     \"note\": \"HRN.txt leaf 176 (the leaf opens '— 155 —'), no. 699: 'sipah ‘Heer’, sipeh, ispehbed (arab. isbahbud), jüd.-pers. ...; ap. Taxma-späda-; aw. spaδa- ‘Heer’; phlv. spāh, spāhpat, arm. LW. spāh, aspahapet.' Exactly Nourai's sepāh and sepahbod, with the Middle Persian links.\"},\n    {\"ref\": \"POK:632\", \"status\": \"not_found\",\n     \"note\": \"Pokorny's p.632 article is k̑uon- 'Hund'; it contains no army word and no Persian sipāh. See node #4.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"PHD\", \"where\": \"MacKenzie p.76 s.v. spāh\", \"stance\": \"supports\",\n     \"note\": \"PHD.txt: 'spāh [spʾh | N sipah] army. ~bed [-pt! | N -bud] general, commander.' MacKenzie gives both of Nourai's Persian words with their Pahlavi spellings.\"},\n    {\"src\": \"NYB\", \"where\": \"Nyberg, Glossary s.v. spāh-pat\", \"stance\": \"supports\",\n     \"note\": \"NYB_vol2_glossary.txt: 'spāh-pat [spʾhpt’] army leader, general ... Arm. lw. from Prth sparapet < *spāda-pati-, v.s.v. spāh; NP sipahbad.' Confirms the Old Iranian compound behind سپهبد.\"},\n    {\"src\": \"HUB\", \"where\": \"Persische Studien (list of zd. correspondences)\", \"stance\": \"supports\",\n     \"note\": \"HUB.txt: 'sipah ‘Heer’ (jüd.-pers. spʾh, H. 699) = zd. spāda-'.\"}\n  ]\n})\n\nN.append({\n  \"id\": 6, \"lang\": \"Sogdian\", \"words\": \"sp`d, `spd\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Sogdian ʾspʾδ / spʾδ 'army' (read (o)spaδ, ispaδ), attested in the Buddhist, Manichaean and Christian corpora and in the Bugut inscription. It is the eastern-Iranian sister of Av. spāδa-, keeping the interdental δ that Middle Persian lost; the prothetic ʾ- before the sp- cluster is the ordinary Sogdian repair of initial sC-, so ʾspʾδ and spʾδ are one word in two spellings — which is exactly what Nourai's doublet 'sp`d, `spd' represents (his ` stands for aleph). Derivatives ʾspʾδβʾry 'army equipment' and ʾspʾδyʾn (pl.) are attested alongside. As with #4-#5, the word is correct; only its parentage under the dog root is not.\",\n  \"derivation_fa\": \"سغدی ʾspʾδ / spʾδ «سپاه، لشکر» (خوانده (o)spaδ و ispaδ) در متن‌های بودایی، مانوی و مسیحی و نیز در سنگ‌نبشتهٔ بوگوت گواهی شده است. این واژه خواهرِ ایرانیِ شرقیِ spāδa- اوستایی است و δ میان‌دندانی را — که فارسی میانه از دست داد — نگه داشته است. الفِ آغازینِ افزوده (پیش‌واکهٔ کمکی) شیوهٔ معمول سغدی برای شکستن خوشهٔ آغازینِ sC- است؛ پس ʾspʾδ و spʾδ یک واژه‌اند با دو املا، و همین است آنچه نورایی به‌صورت «sp`d، `spd» آورده (علامت ` همان الف است). مشتقاتی چون ʾspʾδβʾry «ساز و برگ سپاه» و جمعِ ʾspʾδyʾn نیز گواهی شده‌اند. مانند گره‌های ۴ و ۵، خودِ واژه درست است و تنها نسبت‌دادن آن به ریشهٔ «سگ» نادرست است.\",\n  \"sources\": [W + \"%D8%B3%D9%BE%D8%A7%D9%87\"],\n  \"ref_check\": [\n    {\"ref\": \"SOD:94\", \"status\": \"supports\",\n     \"note\": \"Gharib's Sogdian Dictionary, entry 2383 on printed p.93/94 (SOD_pages.txt \\\\f-leaf 159; printed ≈ leaf − 66): '2383 ʾspʾδ M | (a)spaδ, ispaδ ©<Av. spaδa ©ob. -y | army | GMS 18, 157; BBB 519.' Nourai's SOD:94 is a page number and it lands on the entry. (The Buddhist/Sogdian-script counterpart is entry 1592 ʾspʾδ on p.63: '(o)spaδ ©<*spāda- ©ob. -yh → spʾδ, ʾspʾδ | army'.)\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"SOD\", \"where\": \"Gharib entries 1592, 1593, 1594, 2383, 8874\", \"stance\": \"supports\",\n     \"note\": \"SOD.txt: '1592 ʾspʾδ B,M,S ... army'; '1593 ʾspʾδpʾry ... weapons, army equipment'; '1594 ʾspʾδyʾn ... pl.'; '8874 spaδ ©<Av. spaδa → spʾδ, spʾδyʾn'. The English index (line 87313) reads 'army 1592, 2383, 8874'.\"},\n    {\"src\": \"BRT\", \"where\": \"AiW s.v. spāδa-\", \"stance\": \"supports\",\n     \"note\": \"The Avestan etymon that Gharib cites ('<Av. spaδa') is Bartholomae's; BRT.txt line 24151 indexes the compound 'vīδat.spāδa- I 448' from that stem.\"}\n  ]\n})\n\nN.append({\n  \"id\": 7, \"lang\": \"Old Persian\", \"words\": \"spâda\",\n  \"verdict\": \"disputed\",\n  \"derivation\": \"Old Persian spāda- 'army' is real — but attested only inside the Median personal name Taxmaspāda- (DB 2.78-91, the Mede sent against Ciçantaxma) and, at one remove, in spāθmaida- 'camp' (DNb 30f); the -sp- shows it is a Median (north-western) form taken into the Old Persian of the inscriptions, since native South-Western Persian would have *sāda-. Nourai's arrow, however, is drawn from node #1 (spā 'dog'), and that is what modern scholarship rejects: Kent, the very reference cited here, writes s.v. späda- 'GAv. spāda-, NPers. sipah ... Possibly from pIE *k̑wō- ‘swell, be great’', and elsewhere lists späda- among the OP words 'only in Iranian'. Wiktionary derives the whole family from Proto-Iranian *ćwāHdah < PIE *ḱweh₁-dʰ-o-, root *ḱweh₁- 'to swell, be great'. So the form and the language label are correct, the parent is not.\",\n  \"derivation_fa\": \"پارسی باستان spāda- «سپاه» واژه‌ای واقعی است، اما تنها در دلِ نامِ خاصِ مادیِ Taxmaspāda- (بیستون ۲٫۷۸–۹۱، آن مادی که داریوش برای سرکوب چیثرتخمه فرستاد) و به‌واسطه در spāθmaida- «اردوگاه» (نقش رستم b، سطر ۳۰) گواهی شده است؛ خوشهٔ sp نشان می‌دهد که صورتی مادی (شمال‌غربی) است که به زبان کتیبه‌ها راه یافته، چراکه فارسیِ جنوب‌غربیِ اصیل باید *sāda- می‌داشت. اما پیکانِ نورایی این واژه را از گرهٔ ۱ (spā «سگ») می‌آورد و همین است که پژوهش امروزی آن را نمی‌پذیرد: کِنت — همان مرجعی که در این جعبه به او ارجاع شده — ذیل späda- می‌نویسد «شاید از *ḱwō- به معنی آماسیدن و بزرگ شدن»، و در جای دیگر آن را در شمار واژه‌هایی می‌آورد که «فقط ایرانی‌اند». ویکی‌واژه نیز سراسر این خانواده را از ایرانی آغازین *ćwāHdah و ریشهٔ هندواروپایی *ḱweh₁- «آماسیدن» می‌گیرد. پس صورت و برچسب زبانی درست است، ولی پدرِ ترسیم‌شده نادرست.\",\n  \"sources\": [W + \"%D8%B3%D9%BE%D8%A7%D9%87\"],\n  \"ref_check\": [\n    {\"ref\": \"KNT:210\", \"status\": \"partial\",\n     \"note\": \"Kent's Lexicon entry (p.210, in the s- run just after stūnā-): 'späda- sb. ‘army’: GAv. spāda-, NPers. sipah, Anglo-Indian spahi; in Taxmaspāda-, cf. spāθmaida- (§76.V, §83.II, §116, §143.II). Possibly from pIE *k̑wō- ‘swell, be great’ (Gray, Lg. 25.377-8; cf. §90).' The reference has the word with Nourai's meaning — so the box itself is supported — but proposes a different (non-dog) origin, so it does not support the arrow.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KNT\", \"where\": \"Kent §§1084, 1435, 1778 (phonology and formation lists)\", \"stance\": \"contradicts\",\n     \"note\": \"'Among these are taka- ‘shield’ ... späda- ‘army’ (only in Iranian)'; 'sp in späda- ‘army’, in Taxmaspāda- (name of a Mede); in Vayaspāra-'; and in the list of stems 'with no obvious simpler nominal or verbal form: ... Saka-, späda- in Taxma-spāda-'. Kent keeps späda- away from k̑uon- throughout.\"},\n    {\"src\": \"BRT\", \"where\": \"AiW, spāδa- group\", \"stance\": \"contradicts\",\n     \"note\": \"Bartholomae files the Avestan/Old Persian 'Heer' word separately from ¹span- 'Hund' and traces it to an Aryan *sphā- (his note under the spa-/spā- series, col. 1613: 'ar. *sphā- ... zusammengefallen sein können').\"},\n    {\"src\": \"HRN\", \"where\": \"Grundriss no. 699, p.155\", \"stance\": \"partial\",\n     \"note\": \"Horn gives 'ap. Taxma-späda-; aw. spaδa- ‘Heer’' — confirming the Old Persian form and its attestation only in the compound name — without any dog connection.\"}\n  ]\n})\n\nN.append({\n  \"id\": 8, \"lang\": None, \"words\": \"\",\n  \"verdict\": \"unverified\",\n  \"derivation\": \"An empty box, empty in the printed book as well: the 200-dpi render of pdf p.298 (copied to data/verification/sources/refs/ocr/BOOK/298.png) shows a wide blank double-ruled rectangle at the right of the 'Old Persian KNT:210 | spâda : army' box, joined to it by a plain arrow, with no language header, no reference and no word inside. There is nothing to verify and no derivation to give. It is one of Nourai's reserved slots — elsewhere on the page the same right-hand column carries the Persian or English continuation of the Old Persian box (here the New Persian سپاه it would have held is already drawn one level up, at node #5).\",\n  \"derivation_fa\": \"جعبه‌ای تهی است و در خودِ کتاب هم تهی است: تصویرِ ۲۰۰dpi از صفحهٔ ۲۹۸ (که در data/verification/sources/refs/ocr/BOOK/298.png نگهداری شده) مستطیلی پهن و دوخطّه و خالی را در سمت راستِ جعبهٔ «پارسی باستان KNT:210 | spâda : سپاه» نشان می‌دهد که با پیکانی ساده به آن پیوسته است، بی نام زبان، بی ارجاع و بی واژه. چیزی برای راست‌آزمایی و هیچ اشتقاقی در کار نیست. این یکی از خانه‌های خالیِ نمودارهای نورایی است؛ در همین صفحه ستونِ راستِ همین ردیف معمولاً دنبالهٔ فارسی یا انگلیسیِ جعبهٔ پارسی باستان را می‌گیرد (و اینجا آن دنباله، یعنی «سپاه»، پیش‌تر در گرهٔ ۵ رسم شده است). خطای خوانش اسکن نیست؛ استخراج وفادار است.\",\n  \"sources\": [],\n  \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The box carries no reference in the book.\"}],\n  \"consulted\": [{\"src\": \"BOOK\", \"where\": \"pdf p.298 render, data/verification/sources/refs/ocr/BOOK/298.png\", \"stance\": \"silent\", \"note\": \"The printed rectangle is blank; the JSON's empty node is a faithful extraction.\"}]\n})\n\nN.append({\n  \"id\": 9, \"lang\": \"Old Persian\", \"words\": \"sakâ 2\",\n  \"verdict\": \"plausible\",\n  \"derivation\": \"Old Persian Sakā is the name of the Scythians and of their province (DB 1.16f, DNa 25, DPe 18, DSe 24, XPh 26, DBk 2 'Skunkha the Scythian'); there is no Old Persian common noun sakā 'dog'. Nourai's gloss 'dog' therefore reports an etymology of the ethnonym, not a meaning. His reference does back him: Kent, Lexicon p.209 s.v. Saka-, adds 'Probably ‘dog’ in good sense, = ‘guardian of the flocks’, pIE *k̑uon-, Med. σπάκα ‘dog’ (Herod. 1.110), cf. Van Windekens, Beitr. z. Namenforschung 1.98-102.' The reconstruction is phonetically possible — an Old Iranian *saka- 'dog' is independently posited by Nyberg as the SW form standing behind Middle Persian sag, from the zero-grade *ću-n-ka- — so a homonymy between the tribal name and the dog word is not absurd. But it is a minority view and not the modern default: the ethnonym is more usually left unexplained or connected with a root *sak- 'to go, roam' (whence 'the roamers, nomads'), and Wiktionary's Persian سگ page derives the dog word from OP *sakah without identifying it with Sakā. Verdict: plausible, exactly as far as Kent takes it, and no further.\",\n  \"derivation_fa\": \"پارسی باستان Sakā نامِ سکاها و نامِ ساتراپیِ آنان است (بیستون ۱٫۱۶، نقش رستمِ a ۲۵، دیوان پرسپولیس e ۱۸، و «این سکونخهٔ سکایی» در DBk 2)؛ در پارسی باستان اسمِ عامِ sakā به معنی «سگ» وجود ندارد. پس معنایی که نورایی نوشته، در حقیقت گزارشِ یک ریشه‌شناسی برای نامِ قوم است، نه معنیِ واژه. با این‌همه مرجعِ او پشتیبانش هست: کِنت در واژه‌نامهٔ پارسی باستان، ص ۲۰۹، ذیل Saka- می‌افزاید: «احتمالاً به معنیِ نیکِ سگ، یعنی نگهبانِ گله؛ از *ḱuon- هندواروپایی، مادی σπάκα (هرودوت ۱٫۱۱۰)». این بازسازی از نظر آوایی شدنی است — نیبرگ نیز مستقلاً ایرانیِ باستانِ *saka- «سگ» را صورتِ جنوب‌غربیِ پشتِ فارسی میانهٔ sag می‌داند، از ستاکِ صفرِ *ću-n-ka- — پس هم‌آواییِ نامِ قوم با واژهٔ «سگ» بی‌راه نیست. اما این دیدگاهی اقلیّتی است و رأی رایجِ امروز نیست؛ نامِ سکا را بیشتر ناگشوده می‌گذارند یا با ریشهٔ *sak- «رفتن، کوچیدن» («کوچندگان») می‌سنجند. حکم: با احتیاط پذیرفتنی است، دقیقاً تا همان‌جا که کِنت پیش رفته است.\",\n  \"sources\": [W + \"%D8%B3%DA%AF\"],\n  \"ref_check\": [\n    {\"ref\": \"KNT:209\", \"status\": \"supports\",\n     \"note\": \"Kent, Lexicon p.209: 'Saka- adj. ‘Scythian’ (§116, §143.III); masc. sg. as sb., ‘Scythia’ as province or district ... Elam. sa-ak-ka, Akk. gi-mi(r)-ri, Gk. Σκύθης. See also Sakā-. Probably ‘dog’ in good sense, = ‘guardian of the flocks’, pIE *k̑uon-, Med. σπάκα ‘dog’ (Herod. 1.110), cf. Van Windekens, Beitr. z. Namenforschung 1.98-102.' The page and the claim are Nourai's, verbatim.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, s.v. sag\", \"stance\": \"supports\",\n     \"note\": \"'sag [KLBʾ] dog ... < OP *saka- < *sn̥-ka- < the zero degree of *san-, the SW form of Av. span-, OInd. śvan- ... NP sag.' Nyberg independently posits the Old Persian *saka- 'dog' that Kent's etymology of Sakā presupposes — though he stars it, i.e. it is unattested.\"},\n    {\"src\": \"KNT\", \"where\": \"Kent §§1778, 8601 (stem lists)\", \"stance\": \"partial\",\n     \"note\": \"Kent files Saka- among stems 'with no obvious simpler nominal or verbal form' and among the province names ('Saka or fem. Sakā ‘Scythia’ or ‘the Scythians’'), which shows how tentative his 'probably dog' remark is.\"},\n    {\"src\": \"POK\", \"where\": \"IEW 632, k̑uon-\", \"stance\": \"silent\",\n     \"note\": \"Pokorny's article lists Median σπάκα and 'mpers. sak, npers. sag' but never brings in the ethnonym Sakā.\"}\n  ]\n})\n\nN.append({\n  \"id\": 10, \"lang\": None, \"words\": \"\",\n  \"verdict\": \"unverified\",\n  \"derivation\": \"A second empty box, blank in the printed book too: the render of pdf p.298 (data/verification/sources/refs/ocr/BOOK/298.png) shows a wide double-ruled rectangle to the right of the 'Old Persian KNT:209 | sakâ 2 : dog' box, joined by an arrow, with no language header, no reference and no word. Nothing to verify. Presumably the slot Nourai left for a New Persian or English reflex of Sakā — the Persian سکا / سگزی-سیستان material — which he did not fill in.\",\n  \"derivation_fa\": \"دومین جعبهٔ تهی، که در خودِ کتاب هم سفید است: تصویرِ صفحهٔ ۲۹۸ (data/verification/sources/refs/ocr/BOOK/298.png) مستطیلی پهن و دوخطّه در سمت راستِ جعبهٔ «پارسی باستان KNT:209 | sakâ 2 : سگ» نشان می‌دهد که با پیکانی به آن وصل است و هیچ نام زبان، ارجاع یا واژه‌ای ندارد. چیزی برای راست‌آزمایی نیست. گویا نورایی این خانه را برای بازتابِ فارسی نو یا انگلیسیِ Sakā (مانند «سکا» و «سگزی/سیستان») خالی گذاشته و پرش نکرده است. استخراج وفادار است و خطای خوانش اسکن در کار نیست.\",\n  \"sources\": [],\n  \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The box carries no reference in the book.\"}],\n  \"consulted\": [{\"src\": \"BOOK\", \"where\": \"pdf p.298 render, data/verification/sources/refs/ocr/BOOK/298.png\", \"stance\": \"silent\", \"note\": \"The printed rectangle is blank; the empty node in the JSON is faithful.\"}]\n})\n\nN.append({\n  \"id\": 11, \"lang\": \"Germanic\", \"words\": \"hundaz\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Proto-Germanic *hundaz 'dog' from PIE *ḱun-tó-, i.e. the zero grade of *ḱwṓ with a dental (-to-) enlargement; the initial *ḱ- gives Germanic h- by Grimm's Law, and the *-t- of the suffix is protected from the same shift by the preceding *n... Pokorny states the formation plainly at IEW 632-633: 'got. hunds, aisl. hundr, ags. hund, ahd. hunt ‘Hund’ (k̑un-tó-)'. Watkins puts it the same way: 'Suffixed zero-grade form *kwn-to- in Germanic *hundaz'. The chart's spelling 'hundaz' with the -az of the Germanic masculine a-stem nominative is the standard reconstruction. Descent from the root as drawn is correct.\",\n  \"derivation_fa\": \"ژرمنیِ آغازین *hundaz «سگ» از هندواروپایی *ḱun-tó-، یعنی ستاکِ صفرِ *ḱwṓ با افزودهٔ دندانیِ -to-؛ *ḱ آغازین بر پایهٔ قانون گریم به h ژرمنی بدل شده و t پسوند، به‌سببِ n پیشین، از همان جابه‌جایی در امان مانده است. پوکورنی در ص ۶۳۲–۶۳۳ همین را می‌نویسد: «گوتی hunds، ایسلندیِ کهن hundr، انگلیسیِ کهن hund، آلمانیِ علیای کهن hunt «سگ» (k̑un-tó-)». واتکینز نیز همین ساخت را می‌آورد. صورتِ hundaz با پایانهٔ -az (فاعلیِ ستاکِ a مذکر) بازسازیِ متعارف است. پس انتسابِ این گره به ریشه درست است.\",\n  \"sources\": [W + \"Reconstruction:Proto-Indo-European/%E1%B8%B1w%E1%B9%93\"],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\",\n     \"note\": \"AHD_watkins1985.txt s.v. kwon-: '2. Suffixed zero-grade form *kwn-to- in Germanic *hundaz in: a. Old English hund, dog: HOUND; b. Old High German hunt (> German Hund), dog: DACHSHUND; c. Dutch hond, dog: KEESHOND.' Nourai's 'AHD' citation is the standard authority for exactly this node.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"IEW 632-633\", \"stance\": \"supports\",\n     \"note\": \"'got. hunds, aisl. hundr, ags. hund, ahd. hunt ,Hund‘ (kun-tö-), s. oben.'\"},\n    {\"src\": \"KLN\", \"where\": \"Klein p.746 s.v. hound\", \"stance\": \"supports\",\n     \"note\": \"'ME. hound, hund ... fr. OE. hund, rel. to OS., Dan., Swed., OFris., G. hund, ON. hundr, Du. hond, OHG., MHG. hunt, Goth. hunds. These words derive from a dental enlargement of I.-E. base *kwon-, ‘dog’.'\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 3.61 DOG, p.180\", \"stance\": \"supports\",\n     \"note\": \"Buck's table gives 'Goth. hunds / ON hundr / Dan. hund / Sw. hund / OE hund / Du. hond / OHG hunt / MHG hunt / NHG Hund' as the Germanic column of the inherited word.\"}\n  ]\n})\n\nN.append({\n  \"id\": 12, \"lang\": \"English\", \"words\": \"hound\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Old English hund 'dog' (the general word until Middle English) > ME hund, hound > NE hound. The Middle English spelling with -ou- represents the regular lengthening/rounding of OE ū before the nasal cluster in the orthography of the Anglo-Norman scribes; the semantic narrowing from 'dog (any)' to 'hunting dog' happened in Middle English after the borrowing of dogge/dog into the general sense. The node has no reference in the book, but Klein's 'hound' article (the very page cited for the parent, KLN:746) and Skeat both carry the chain. Descent from Proto-Germanic *hundaz as drawn is correct.\",\n  \"derivation_fa\": \"انگلیسیِ کهن hund «سگ» (تا دورهٔ انگلیسیِ میانه واژهٔ عامِ «سگ» بود) < انگلیسیِ میانه hund/hound < انگلیسیِ نو hound. املای ou در انگلیسیِ میانه بازتابِ قاعده‌مندِ ū انگلیسیِ کهن در دستگاهِ نگارشیِ کاتبانِ انگلونورمان است. تحولِ معنایی از «سگ (به‌طور کلی)» به «سگِ شکاری» پس از رواجِ dogge/dog در معنای عام رخ داده است. این جعبه در کتاب ارجاعی ندارد، اما مدخلِ hound در فرهنگ کلاین (همان صفحهٔ ۷۴۶ که برای گرهٔ پدر آمده) و نیز اسکیت همین زنجیره را می‌آورند. پس نسبتِ آن به *hundaz ژرمنی درست است.\",\n  \"sources\": [W + \"Reconstruction:Proto-Indo-European/%E1%B8%B1w%E1%B9%93\"],\n  \"ref_check\": [\n    {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The box carries no reference in the book; verified against KLN:746 (the parent's reference) and Skeat instead.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"Klein p.746 s.v. hound, n., dog\", \"stance\": \"supports\",\n     \"note\": \"'hound, n., dog. — ME. hound, hund, ‘dog’, fr. OE. hund ... Derivatives: hound, tr. v., hound-er, n., hound-ish, hound-y, adjs.'\"},\n    {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict., s.v. Hound\", \"stance\": \"supports\",\n     \"note\": \"SKT.txt: 'Hound, a dog. (E.) A.S. hund, + Du. hond, Icel. hundr, Dan. Swed. G. Hund, Goth. hunds. Allied to L. canis, Gk. κύων (gen. κυνός), Skt. śvan, a dog; also to Irish cú, W. ci, a dog, Russ. suka, a bitch.'\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. kwon-\", \"stance\": \"supports\",\n     \"note\": \"'Old English hund, dog: HOUND' — HOUND is one of the English words Watkins files under kwon-.\"}\n  ]\n})\n\nN.append({\n  \"id\": 13, \"lang\": \"Latin\", \"words\": \"canis; insula canaria\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Latin canis 'dog' belongs to the root, though with an irregularity everyone notes: the expected outcome of *ḱwon-/*ḱun- would be *cunis or the like, and the a of canis is unexplained — Pokorny writes 'ganz unklar lat. canis ‘Hund’ ... hinsichtlich des a; vielleicht Einmischung eines dem mir. cano, cana ‘Wolfsjunges’, cymr. cenaw entsprechenden Wortes'; Watkins simply files it as 'Variant *kan-i-'. So the membership is certain, the vocalism disputed. Insula Canaria is Pliny's name (Naturalis Historia VI.205) for the largest of the Fortunatae Insulae, 'so called from its multitude of dogs of a huge size' — Pliny reports that Juba II's expedition brought two of them back; hence Nourai's gloss 'dog island, named after its large dogs', which is Pliny's own explanation. (A rival modern theory takes the name from the Berber Canarii of the opposite Moroccan coast; Pliny's account is nevertheless the ancient one and the one that produced the Latin form.)\",\n  \"derivation_fa\": \"لاتینِ canis «سگ» به همین ریشه تعلق دارد، هرچند با بی‌قاعدگی‌ای که همه یادآور شده‌اند: از *ḱwon-/*ḱun- انتظار *cunis می‌رفت و a در canis ناروشن است؛ پوکورنی می‌نویسد «لاتینِ canis از حیثِ a کاملاً ناروشن است؛ شاید آمیزشی با واژه‌ای همانندِ ایرلندیِ میانه cano/cana «تولهٔ گرگ» و ولزیِ cenaw رخ داده باشد»، و واتکینز آن را صرفاً «گونهٔ *kan-i-» می‌نامد. پس عضویتِ واژه در این خانواده قطعی است و تنها واکهٔ آن محلِّ بحث. Insula Canaria نامی است که پلینیِ بزرگ (تاریخ طبیعی، ۶٫۲۰۵) به بزرگ‌ترینِ «جزایرِ سعادت» داده و آن را «به سببِ انبوهیِ سگ‌های تنومندش» چنین خوانده است؛ او می‌افزاید که هیئتِ اعزامیِ یوبای دوم دو قلاده از آن سگ‌ها را با خود آورد. پس شرحِ نورایی («جزیرهٔ سگ، نامیده به‌سببِ سگ‌های بزرگش») همان توضیحِ خودِ پلینی است. (نظریهٔ رقیبِ امروزی نام را از قومِ بربرِ Canarii در ساحلِ مقابلِ مراکش می‌گیرد، اما صورتِ لاتینی از روایتِ پلینی برخاسته است.)\",\n  \"sources\": [\"https://www.etymonline.com/word/canary\"],\n  \"ref_check\": [\n    {\"ref\": \"KLN:746\", \"status\": \"supports\",\n     \"note\": \"KLN_1966.txt leaf 401 (p.746) s.v. hound lists 'L. canis' among the reflexes of I.-E. *kwon- and cross-refers 'Cp. also canaille, Canidae, canine, Canis, chenille, kennel'. For the island half see Klein p.230 s.v. canary (node #15): 'fr. L. insula Canaria, ‘one of the Canary Islands’, lit. ‘Dog Islands’, fr. canis, ‘dog’. The islands were so called from their large dogs.'\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"IEW 633\", \"stance\": \"partial\",\n     \"note\": \"'ganz unklar lat. canis ,Hund‘, canes ursprüngl. altes fem. ,Hündin‘, canicula ... hinsichtlich des a' — Pokorny keeps canis in the root but flags its vowel.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. kwon-\", \"stance\": \"supports\",\n     \"note\": \"'4. Variant *kan-i- in Latin canis, dog: CANAILLE, CANARY, CANICULA, CANINE, CHENILLE, KENNEL.'\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 3.61, p.180\", \"stance\": \"supports\",\n     \"note\": \"Buck's Italic row: 'Lat. canis / It. cane / Fr. chien / Rum. cîine', with the note that Grk. κύων and Lat. canis were used of both sexes.\"}\n  ]\n})\n\nN.append({\n  \"id\": 14, \"lang\": \"English\", \"words\": \"kennel; Canary Islands\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Two separate English descendants of the Latin box, both correct. (i) kennel 'dog-house' came into Middle English (c.1300 kenel) from Anglo-Norman/Old Northern French kenil, chenil, from Vulgar Latin *canile 'dog-house' — a -īle formation on canis exactly parallel to Latin ovīle 'sheepfold' from ovis and bovīle from bos; the Norman k- against Central French ch- is the regular Northern French retention of Latin c- before a, and is why English has kennel, not *chenel. (Klein separates it from the homonym kennel 'gutter', which is from L. canālis — the chart means the dog word.) (ii) Canary Islands is the English rendering of Latin Insulae Canariae, taken over through Spanish Islas Canarias; the English name is thus a direct calque-plus-borrowing of the Latin name in node #13, not a derivative of the bird. Both belong under canis.\",\n  \"derivation_fa\": \"دو بازماندهٔ جداگانهٔ انگلیسی از جعبهٔ لاتین، و هر دو درست. ۱) kennel «لانهٔ سگ» حدود ۱۳۰۰ میلادی از انگلونورمان/فرانسویِ کهنِ شمالی kenil, chenil به انگلیسیِ میانه (kenel) رسیده و آن از لاتینِ عامیانهٔ *canile «سگ‌خانه» است؛ ساختی با پسوندِ -īle بر پایهٔ canis، درست همانندِ ovīle «آغل» از ovis و bovīle از bos. کافِ نورمانی در برابر ch فرانسویِ مرکزی، همان نگه‌داشتِ قاعده‌مندِ c لاتین پیش از a در شمالِ فرانسه است و از همین‌رو انگلیسی kennel دارد نه *chenel. (کلاین این واژه را از هم‌آوایش kennel «جویِ آب» — از canālis — جدا می‌کند؛ مقصودِ نمودار همان واژهٔ سگ است.) ۲) Canary Islands برگردانِ انگلیسیِ Insulae Canariae لاتینی است که از راهِ اسپانیاییِ Islas Canarias گرفته شده؛ پس نامِ انگلیسی مستقیماً از نامِ لاتینیِ گرهٔ ۱۳ می‌آید نه از نامِ پرنده. هر دو به‌درستی زیرِ canis نشسته‌اند.\",\n  \"sources\": [\"https://en.wiktionary.org/wiki/kennel\", \"https://www.etymonline.com/word/canary\"],\n  \"ref_check\": [\n    {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The box carries no reference in the book; checked against KLN (the parent's reference), Watkins and Wiktionary instead.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"Klein s.v. canal / cannel / kennel\", \"stance\": \"supports\",\n     \"note\": \"KLN_1966.txt s.v. canal: 'See cane and adj. suff. -al and cp. channel, cannel, kennel, ‘gutter’, which are doublets of canal' — Klein's explicit note that the gutter-kennel is the canal word, which by elimination leaves the dog-house kennel under canis; and at p.746 s.v. hound he lists 'kennel, ‘shelter for a dog’' among the cognates of I.-E. *kwon-.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. kwon-, index\", \"stance\": \"supports\",\n     \"note\": \"Watkins files both 'KENNEL1' and 'CANARY' under kwon- (index lines 'CANARY kwon-', and 'KENNEL1' in the kwon- article's Latin section).\"},\n    {\"src\": \"SKT\", \"where\": \"Skeat s.v. Kennel (1) / Kennel (2)\", \"stance\": \"supports\",\n     \"note\": \"SKT.txt distinguishes 'kennel (2), a gutter. (F. − L.) ... M.E. canel, a channel' from 'Kennel (1)', the dog-house, i.e. the same split Klein makes.\"}\n  ]\n})\n\nN.append({\n  \"id\": 15, \"lang\": \"Spanish\", \"words\": \"canario\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Spanish canario is first the adjective/ethnonym 'of the Canary Islands' (Islas Canarias < L. insulae Canariae), and from the 16th century the name of the small finch of those islands, Serinus canaria, exported to the Peninsula by Spanish traders after the conquest of the archipelago (Gran Canaria 1483, Tenerife 1496). The bird is thus named after the islands and the islands after the dogs, so Nourai's gloss 'from Canary Islands < a bird >' is exactly right, and so is the arrow from the Latin box. The Spanish monopoly on the trade (only cocks were sold, to keep breeding to Spain) is what carried the word into every European language.\",\n  \"derivation_fa\": \"canario در اسپانیایی نخست صفت و نسبتِ «مربوط به جزایر قناری» است (Islas Canarias از لاتینِ insulae Canariae)، و از سدهٔ شانزدهم نامِ سهرهٔ کوچکِ همان جزایر (Serinus canaria) شد؛ پرنده‌ای که پس از فتحِ مجمع‌الجزایر (گران کاناریا ۱۴۸۳، تنریفه ۱۴۹۶) بازرگانانِ اسپانیایی به شبه‌جزیره آوردند. پس پرنده به نامِ جزایر خوانده شد و جزایر به نامِ سگ‌ها؛ بنابراین توضیحِ نورایی («از جزایر قناری < یک پرنده >») دقیقاً درست است و پیکانِ آن از جعبهٔ لاتین نیز درست. انحصارِ اسپانیایی‌ها بر این تجارت (که فقط نرها را می‌فروختند تا پرورش در اسپانیا بماند) همان چیزی است که واژه را به همهٔ زبان‌های اروپایی رساند.\",\n  \"sources\": [\"https://www.etymonline.com/word/canary\"],\n  \"ref_check\": [\n    {\"ref\": \"KLN:230\", \"status\": \"supports\",\n     \"note\": \"KLN_1966.txt \\\\f-leaf 132 (printed page number 230 on the leaf) s.v. canary: 'canary, n., — F. canari, canarie, fr. Sp. canario, ‘canary bird’, lit. ‘of the Canary Islands’, fr. L. insula Canaria, ‘one of the Canary Islands’, lit. ‘Dog Islands’, fr. canis, ‘dog’ (see canine). The islands were so called from their large dogs.' Nourai's KLN:230 is precisely this entry, and it carries his whole Latin→Spanish→French→English chain in one paragraph.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"Klein p.230 s.v. canary\", \"stance\": \"supports\", \"note\": \"See the quotation above; Klein is both Nourai's reference here and the modern standard for this chain.\"},\n    {\"src\": \"SKT\", \"where\": \"Skeat s.v. Canary\", \"stance\": \"supports\",\n     \"note\": \"SKT.txt: 'Canary, a bird, a wine ... (Canary Islands.) All named ... Canary Islands.'\"}\n  ]\n})\n\nN.append({\n  \"id\": 16, \"lang\": \"French\", \"words\": \"canari\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"French canari (also canarie in the 16th c.) 'canary bird', borrowed from Spanish canario as the trade in the bird spread north from Seville; the French form drops the Spanish -o and is first recorded in the mid-16th century. Klein states the borrowing directly at p.230 ('F. canari, canarie, fr. Sp. canario'). French is then the immediate donor both for English canary (node #18) and, much later and via the francophone channels of the 19th-20th century, for Persian قناری (node #17), so Nourai's fork here is correctly placed. (The homonym canard 'duck; hoax' is a different word, from OF caner 'to cackle', and Klein keeps them apart in adjacent entries.)\",\n  \"derivation_fa\": \"فرانسویِ canari (در سدهٔ شانزدهم canarie نیز) «قناری»، وام‌گرفته از canario اسپانیایی است، آنگاه که تجارتِ این پرنده از اشبیلیه به شمال گسترش یافت؛ صورتِ فرانسوی -o اسپانیایی را انداخته و نخستین کاربردهایش از میانهٔ سدهٔ شانزدهم است. کلاین (ص ۲۳۰) همین وام‌گیری را صریح آورده است: «F. canari, canarie از اسپانیاییِ canario». سپس فرانسوی هم سرچشمهٔ مستقیمِ canary انگلیسی است (گرهٔ ۱۸) و هم — دیرتر، از راهِ مجاریِ فرانسه‌زبانِ سده‌های سیزدهم و چهاردهم خورشیدی — سرچشمهٔ «قناریِ» فارسی (گرهٔ ۱۷). پس دوشاخه‌شدنِ نمودار در اینجا درست است. (هم‌آوایش canard «مرغابی؛ خبر ساختگی» واژهٔ دیگری است از caner فرانسویِ کهن «قدقد کردن» و کلاین آن دو را در دو مدخلِ پیاپی جدا نگه داشته است.)\",\n  \"sources\": [\"https://www.etymonline.com/word/canary\"],\n  \"ref_check\": [\n    {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The box carries no reference in the book; checked against KLN:230 (the parent's reference) and Etymonline.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"Klein p.230 s.v. canary and canard\", \"stance\": \"supports\",\n     \"note\": \"'canary, n., — F. canari, canarie, fr. Sp. canario' — and the preceding entry 'canard, n., a duck: a hoax. — F., ‘duck; drake’, fr. OF. canart, fr. OF. caner, ‘to cackle’', keeping the two apart.\"},\n    {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls, s.v. canary / alpiste\", \"stance\": \"supports\",\n     \"note\": \"FSD_vol1.txt at 'alpiste': 'Bird-seed ... [< F. alpiste, < Sp. alpiste, canary-seed]' — incidental confirmation that the canary vocabulary reached English/French from Spanish.\"}\n  ]\n})\n\nN.append({\n  \"id\": 17, \"lang\": \"Persian\", \"words\": \"qanârî «قناری»\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Persian قناری qanārī 'canary' is a modern European loan, from French canari, taken in with the bird itself in the Qajar period; Mo‘in's Farhang-e Fārsī marks the entry with the French source and explains the name from the islands: 'قناری ... اصل این پرنده از جزایر قناری است (وجه تسمیه به همین مناسبت است) و از آنجا به دیگر نقاط جهان از جمله ایران برده شده'. The Arabic-looking spelling with ق and ی is orthographic dressing of the French sound shape (q- for the foreign k-/c- before ā is the normal Persian and Ottoman rendering, cf. قهوه‌خانه-type spellings and قوطی); the word has no Arabic root and is not a Semitic q-n-r formation. It is therefore not a Persian→Arabic→Persian round trip but a straight Europeanism, and Nourai's arrow French→Persian is right.\",\n  \"derivation_fa\": \"«قناری» در فارسی وام‌واژه‌ای اروپایی و نو است: از فرانسویِ canari، که همراه با خودِ پرنده در دورهٔ قاجار وارد شد. معین در فرهنگ فارسی مدخل را با نشانِ زبانِ فرانسه آورده و وجه تسمیه را از نامِ جزایر گرفته است: «قناری … اصل این پرنده از جزایر قناری است (وجه تسمیه به همین مناسبت است) و از آنجا به دیگر نقاط جهان از جمله ایران برده شده». املای عربی‌نمای آن با «ق» و «ی» صرفاً آرایشِ خطّی برای صورتِ آواییِ فرانسوی است؛ نوشتنِ q به‌جای k/c بیگانه پیش از ā در فارسی و عثمانی معمول است (مانند «قوطی»). این واژه ریشهٔ عربی ندارد و ساختِ سه‌حرفیِ سامیِ ق‌ن‌ر نیست. پس اینجا با معرّب و رفت‌وبرگشتِ فارسی←عربی←فارسی روبه‌رو نیستیم، بلکه با وام‌واژه‌ای یکسره اروپایی؛ و پیکانِ نورایی (فرانسوی ← فارسی) درست است.\",\n  \"sources\": [\"https://www.etymonline.com/word/canary\"],\n  \"ref_check\": [\n    {\"ref\": \"MON:2730\", \"status\": \"supports\",\n     \"note\": \"MON_part2.txt line 14948 (= incoming/MON/MON_2vol_Adena_v2_djvu.txt, same line) s.v. قناری: 'قناری: [OCR-garbled source tag] (جان.) پرنده‌ای است از راستهٔ سبکبالان و از دستهٔ گنجشکان ... اصل این پرنده از جزایر قناری است (وجه تسمیه به همین مناسبت است) و از آنجا به دیگر نقاط جهان از جمله ایران برده شده.' The entry is Mo‘in's and gives Nourai's meaning and the island etymology; the volume/page number 2730 could not be checked against this reflowed OCR (it has no page tags), but the article is there and it is the only قناری entry in Mo‘in.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"MON\", \"where\": \"Farhang-e Farsi, s.v. قناری\", \"stance\": \"supports\", \"note\": \"See the quotation above; Mo‘in's own headword marks it a European borrowing and derives the name from the islands.\"},\n    {\"src\": \"KLN\", \"where\": \"Klein p.230 s.v. canary\", \"stance\": \"supports\",\n     \"note\": \"Supplies the donor form Nourai's arrow needs: 'F. canari, canarie, fr. Sp. canario.' Persian قناری matches the French, not the Spanish, shape (no final -o).\"}\n  ]\n})\n\nN.append({\n  \"id\": 18, \"lang\": \"English\", \"words\": \"canary\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"English canary is attested from the 1570s as Canary-bird and from the 1650s shortened to canary, alongside canary (sack) 'the wine of the islands' from the 1580s — both from French canarie/canari, itself from Spanish canario. The English word therefore reaches the Latin insula Canaria and canis by the four-step route the chart draws, and 'canary' is one of the English words Watkins files under kwon-. The chart's arrow from the French box (rather than straight from Spanish) matches Klein and Etymonline, which both make French the immediate donor.\",\n  \"derivation_fa\": \"انگلیسیِ canary از دههٔ ۱۵۷۰ به‌صورت Canary-bird و از دههٔ ۱۶۵۰ به‌صورت کوتاه‌شدهٔ canary گواهی شده است، و در کنارِ آن canary (sack) «شرابِ آن جزایر» از دههٔ ۱۵۸۰ — هر دو از فرانسویِ canarie/canari و آن از اسپانیاییِ canario. پس واژهٔ انگلیسی از همان چهار پلهٔ نمودار به insula Canaria و canis لاتین می‌رسد، و واتکینز نیز CANARY را در فهرستِ واژه‌های انگلیسیِ برآمده از ریشهٔ kwon- آورده است. پیکانی که نورایی از جعبهٔ فرانسوی کشیده (و نه مستقیم از اسپانیایی) با کلاین و اتیمانلاین می‌خواند که هر دو فرانسوی را وام‌دهندهٔ بی‌واسطه می‌دانند.\",\n  \"sources\": [\"https://www.etymonline.com/word/canary\"],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\",\n     \"note\": \"AHD_watkins1985.txt, index of English words: 'CANARY kwon-' (line 1332), and in the root article '4. Variant *kan-i- in Latin canis, dog: CANAILLE, CANARY, CANICULA, CANINE, CHENILLE, KENNEL1.'\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"Klein p.230 s.v. canary\", \"stance\": \"supports\",\n     \"note\": \"'canary, n., — F. canari, canarie, fr. Sp. canario, ‘canary bird’, lit. ‘of the Canary Islands’, fr. L. insula Canaria ... fr. canis, ‘dog’.'\"},\n    {\"src\": \"SKT\", \"where\": \"Skeat, s.v. Canary\", \"stance\": \"supports\",\n     \"note\": \"'Canary, a bird, a wine ... (Canary Islands.) All named ... Canary Islands.'\"}\n  ]\n})\n\nout = {\n  \"pdf_page\": 298,\n  \"book_page\": 268,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-06\",\n  \"entries\": [entry]\n}\nwith open(\"/home/sfmqrb/git/rishe/data/verification/page-298.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(out, f, ensure_ascii=False, indent=2)\nprint(\"ok\", len(N))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk298.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-298.json > /dev/null && echo \"JSON OK\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 298"
}
```


### [2026-09-06T22:51:16.964Z] TOOL RESULT

```
ok 18
JSON OK
nodes verified: 18/18
node verdicts: {'confirmed': 13, 'disputed': 2, 'unverified': 2, 'plausible': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 13, 'not_found': 2, 'not_checked': 6, 'partial': 1}
books consulted: {'supports': 32, 'partial': 6, 'contradicts': 4, 'silent': 3} | by book: {'KLN': 7, 'BRT': 5, 'KNT': 4, 'SKT': 4, 'HUB': 3, 'NYB': 3, 'HRN': 3, 'POK': 3, 'AHD': 3, 'PHD': 2, 'BOOK': 2, 'SYN': 2, 'BQT': 1, 'SOD': 1, 'FSD': 1, 'MON': 1}
```


## [2026-09-06T22:51:46.499Z] AGENT

Done. `data/verification/page-298.json` written; `verify_check.py 298` reports 18/18 nodes, 0 PROBLEM lines.

**Page 298 (book p. 268), one entry — root "Kwon, Ka 2, Sua" : dog — root `confirmed`.**
Node verdicts: 13 confirmed, 2 disputed, 1 plausible, 2 unverified (the two blank boxes).
Ref checks: 13 supports, 1 partial, 2 not_found, 6 not_checked. 16 books consulted (KLN, POK, AHD, WLD-via-POK, IEC, SYN, BRT, KNT, PHD, NYB, HRN, HUB, BQT v1+v2, MON, SOD, SKT, FSD). 6 web pages archived via `fetch_source.py`; page render copied to `sources/refs/ocr/BOOK/298.png`.

Flagged items:
- **disputed — #4 Avestan `spâda, spâtha; spatha-paiti; Aspadâna` "army".** The forms are all right, but hanging them on the *dog* root is a false etymology. Av. spāδa- < PIr. *ćwāHda- < PIE *ḱweh₁-dʰ-o- "swell, be great" (Wiktionary; cf. Av. sūidiiāi, Skt. śávas-). Pokorny p.632 (Nourai's own ref) is the k̑uon- "Hund" article and contains no army word at all — `not_found`. FIB:207 not accessible.
- **disputed — #7 Old Persian `spâda` "army"** (drawn from #1 spā "dog"). Kent p.210, the very reference cited, says "**Possibly from pIE \*k̑wō- 'swell, be great'** (Gray, Lg. 25.377-8)" and elsewhere lists spāda- as "only in Iranian". Attested only in Taxmaspāda- / spāθmaida-.
- **plausible — #9 Old Persian `sakâ 2` "dog".** OP Sakā is the Scythian ethnonym; there is no OP common noun "dog". Kent p.209 *does* back Nourai ("Probably 'dog' in good sense, = 'guardian of the flocks', pIE \*k̑uon-, Med. σπάκα"), and Nyberg independently posits OP \*saka- behind MP sag — but this is a minority etymology of the tribal name, so I stopped where Kent stops.

No extraction errors: the page image confirms nodes #8 and #10 are genuinely blank double-ruled boxes in the printed book, and every word, script and reference in the JSON matches the page. Nourai's "spâda, spâtha" is his own double transliteration of the one word spāδa-, not a misprint.

Positive findings worth noting: HRN:164 (no. 743 "seg"), HRN:155 (no. 699 "sipah"), KLN:746 (hound) and KLN:230 (canary) land exactly on the cited printed pages; SOD:94 is Gharib entry 2383 ʾspʾδ on p.93/94; BQT:118 turned out to be Borhan's اسپه ("مخفف اسپاه … و سگ را نیز گویند"), BQT:1087 the سپاه article, BQT:1155 the سگ article with Mo'in's Horn-derived footnote (the vol.-2 scan puts it a page or two later than 1155).
