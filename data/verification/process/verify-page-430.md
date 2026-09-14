# Verification process log — verify-page-430


## [2026-09-14T01:21:55.042Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 430 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-430.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-430.json. Write /home/sfmqrb/git/rishe/data/verification/page-430.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 430` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T01:21:56.244Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T01:21:57.073Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T01:21:57.097Z] TOOL RESULT

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


## [2026-09-14T01:21:57.576Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-430.txt"
}
```


### [2026-09-14T01:21:57.639Z] TOOL RESULT

```
1	=== PDF page 430 (book page 400) ===
2	--- entry 0 ---
3	ROOT [Aramaic] Salîbâ : cross  (refs BQT:656; MON:1310)
4	#1 (parent #0) [Persian] refs=MON:1310; BQT:656 | čalîpâ «چلیپا» : cross | extra: چلیپایی
5	#2 (parent #0) [Arabic] refs=MON:1310,2161 | salîb : cross
6	  #3 (parent #2) [Persian] refs=MON:2161 | salîb «صلیب» : cross | extra: مصلوب
7	#4 (parent #0) [Sogdian] refs=SOD:126 | clyb` : cross
8	--- entry 1 ---
9	ROOT [Arabic] Šalla : to paralyze (hand)  (refs SAP:818)
10	#1 (parent #0) [Persian] refs=BQT:1287 | šal 2 «شَل ۲» : lame, crippled ; šalîdan «شلیدن» : to lame
11	--- entry 2 ---
12	ROOT Sam -> redirect to Sem 2
13	--- entry 3 ---
14	ROOT Šamšěr -> redirect to Šfšyr
15	--- entry 4 ---
16	ROOT [Akkadian] Sarâpu, Sarpu : Sarâpu: to melt, refine. Sarpu: refined silver.  (refs AHD:1206; KLN:1445)
17	#1 (parent #0) [Arabic] refs=KLN:1445 | s.r.f : to purify silver ; sarrâf : coin and money exchanger
18	  #2 (parent #1) [Persian] refs=MON:2144 | sarrâf «صرّاف» : money exchanger
19	#3 (parent #0) [Old English] refs=AHD:1206 | seolfor : silver coin
20	  #4 (parent #3) [English] refs=None | silver
21	--- entry 5 ---
22	ROOT Sarpu -> redirect to Sarâpu
23	
```


## [2026-09-14T01:22:00.502Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-430.json",
 "description": "Read source JSON for page 430"
}
```


### [2026-09-14T01:22:00.541Z] TOOL RESULT

```
{
  "pdf_page": 430,
  "book_page": 400,
  "entries": [
    {
      "root": {
        "name": "Salîbâ",
        "lang": "Aramaic",
        "refs": "BQT:656; MON:1310",
        "gloss": "cross"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "MON:1310; BQT:656",
          "words": [
            {"translit": "čalîpâ", "gloss": "cross", "script": "چلیپا"}
          ],
          "script_extra": "چلیپایی",
          "note": null,
          "quote": {"text": "تا مایۀ ایمان بود شهادت - تا قبلۀ ترسا بود چلیپا", "poet": "Farrokhî"}
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Arabic",
          "refs": "MON:1310,2161",
          "words": [
            {"translit": "salîb", "gloss": "cross", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "MON:2161",
          "words": [
            {"translit": "salîb", "gloss": "cross", "script": "صلیب"}
          ],
          "script_extra": "مصلوب",
          "note": null,
          "quote": {"text": "آنجا که کار صومعه را جلوه میدهند - ناقوس دیر راهب و نام صلیب هست", "poet": "Hâfez"}
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Sogdian",
          "refs": "SOD:126",
          "words": [
            {"translit": "clyb`", "gloss": "cross", "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Šalla",
        "lang": "Arabic",
        "refs": "SAP:818",
        "gloss": "to paralyze (hand)"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "BQT:1287",
          "words": [
            {"translit": "šal 2", "gloss": "lame, crippled", "script": "شَل ۲"},
            {"translit": "šalîdan", "gloss": "to lame", "script": "شلیدن"}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {"name": "Sam", "redirect": "Sem 2"},
      "nodes": []
    },
    {
      "root": {"name": "Šamšěr", "redirect": "Šfšyr"},
      "nodes": []
    },
    {
      "root": {
        "name": "Sarâpu, Sarpu",
        "lang": "Akkadian",
        "refs": "AHD:1206; KLN:1445",
        "gloss": "Sarâpu: to melt, refine. Sarpu: refined silver."
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Arabic",
          "refs": "KLN:1445",
          "words": [
            {"translit": "s.r.f", "gloss": "to purify silver", "script": null},
            {"translit": "sarrâf", "gloss": "coin and money exchanger", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "MON:2144",
          "words": [
            {"translit": "sarrâf", "gloss": "money exchanger", "script": "صرّاف"}
          ],
          "note": null,
          "quote": {"text": "خموش حافظ و این نکته های زر سرخ - نگاهدار که قلاب شهر صرّافست", "poet": "Hâfez"}
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Old English",
          "refs": "AHD:1206",
          "words": [
            {"translit": "seolfor", "gloss": "silver coin", "script": null}
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
            {"translit": "silver", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {"name": "Sarpu", "redirect": "Sarâpu"},
      "nodes": []
    }
  ]
}
```


## [2026-09-14T01:22:02.611Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['BQT','MON','SOD','SAP','AHD','KLN','PLA','AFM','FVQ','ARY','HRN','HUB']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:600])\n    print()\n\"",
 "description": "Inspect refs_online entries"
}
```


### [2026-09-14T01:22:03.514Z] TOOL RESULT

```
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=

SAP {"title": "Ahmad Sayyah, Farhang-e Sayyah / Farhang-e Bozorg-e Jame'-e Novin (Persian translation of al-Munjid), 3 vols, Eslam 1368/1989", "kind": "purchase", "url": "https://fidibo.com/book/142427 (vol.1, 1152 pp) ; https://fidibo.com/book/142430 (vol.2, 1206 pp) — PDF ebook, ~300,000 toman each, free sample", "lookup_hint": "Not found (archive.org has Bandar-Rigi's منجد الطلاب translation, abo_abdrahman_kordi_barid_20150501_1718, and the Arabic al-Munjid on noorlib.ir/book/info/32878 — usable to check the Arabic-side content, not Sayyah's pages).", "local_file": null, "page_offset": null, "c

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 lea

AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/

FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sou

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol
```


## [2026-09-14T01:22:09.322Z] TOOL CALL #5: Bash

```json
{
 "command": "sed -n '1,200p' data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-14T01:22:09.396Z] TOOL RESULT

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


## [2026-09-14T01:22:20.404Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"seolfor\\|silubr\\|sarpu\\|ṣarpu\\|sarapu\" KLN_1966.txt | head -40\necho \"=== KLN 1971 ===\"\ngrep -n -i \"seolfor\\|silubr\\|sarpu\" KLN_1971.txt | head -30",
 "description": "grep Klein for silver/sarpu"
}
```


### [2026-09-14T01:22:20.489Z] TOOL RESULT

```
35228:silver,  n.  —  ME.  silver,  fr.  OE.  seolfor,  siolofr, silofr,  rel.  to  OS.  silutar,  ON.  silfr,  Dan.  solv, Swed.  silver,  MDu.  silver,  Du.  silver,  OHG. sillabar ,  silabar,  MHG.,  G.  silber,  Goth,  silubr. Cp.  OSlav.  sirebro,  OPruss.  siraplis,  Lith.  sida- bras,  ‘silver’.  All  these  words  are  prob.  borrow¬ ed  ult.  fr.  Akkad,  farpu,  ‘silver’,  lit.  ‘refined
35232:silvern,  adj.  —  ME.  silveren,  fr.  OE.  seolfren, silfren,  fr.  seolfor,  siolofr,  silofr,  ‘silver’.  See silver.
=== KLN 1971 ===
222088:silver, n. — ME. silver, fr. OE. seolfor, siolofr, 
222091:siUabar, silabar, MHG., G. silber, Goth, silubr. 
222094:ed ult. fr. Akkad, sarpu . ‘silver’, fit. ‘refined 
222120:silfren , fr. seolfor , siolofr, silofr, ‘silver’. See
```


## [2026-09-14T01:22:21.760Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SOD clyb ===\"\ngrep -n \"clyb\\|clyp\\|crosses\\|cross\\b\" SOD_pages.txt | head -40",
 "description": "grep Gharib Sogdian for clyb"
}
```


### [2026-09-14T01:22:21.838Z] TOOL RESULT

```
=== SOD clyb ===
2010:notes, cross-references, Persian meaning, English          the Buddist corpus and non-Buddhist excerpts within
2023:those by different researchers. The aim has been to           "full" entry in the dictionary but as one cross-
2063:sometimes marked with the overstrike v denoting               entries, sometimes cross-referenced to each other
2076:entries are mutually cross-referenced. It may also be        Sogdian term. A question mark following a meaning
2079:synonymous terms. Most cross-referencing, however,           the source(s) of the entry, generally using biblio-
2080:is on grammatical basis, as with the cross-                           graphic abbreviations in common use for Sogdian
2252:in their homeland organized themselves in a small            northward across the Oxus. One might assume that
2858:the Nestorian Christian cross.95 The longest                     readings in a number of cases; also Henning,
10394:         azate-t        (»z>tk) ©pi.                                             (r<9)cross over
10945:                                                                               0o)pass, (fo)cross
11901:2839 pst'y =» Pst»k                                                 =»ftr-, 0c)cross
12879:3202 clyb> C                                      i_aJL^ <uJL*-        cananste ? (ensty)
12881:     cross
14623:       (to)cross over, 0o)remove
16686:     OeOgo, 0<?)pass, GcOcross, (ro)transfer                           706 b22; MSP b3; Yysypw, Hen. Tales. 480-30
22905:       cross, torture instrument                               6691 pcw>Ytk B
24018:     cross-legged                                                       7073 prbyrc    M                               Ji*ftj£cJjj
26567:     torture instrument, cross ^
26622:         cross, torture instrument                                    pattan ©Skt. pattana =»ptn
26628:         cross                                                        lamp, light
26632:      cross                                                           abuse
31098:     tap/fnak                                                            xypOpr clyb; Weber. IF 80, 1975, 90; AVS 106
37967:cross    3202, 6681, 7638, 7921, 7945,   (to)cut     1032, 3892, 5906, 7732,     deacon   9280
37973:cross-legged     7062                      6864, 8279, 8281, 8293, 8294          dear   218, 3622, 3973, 5850, 7337,
37974:(Across over 2300, 3839                  (to)cut out 2754, 10960                   7368
```


## [2026-09-14T01:22:28.252Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '12860,12900p' SOD_pages.txt\necho \"--- pdf page tag near ---\"\nawk 'NR<=12890 && /\\[pdf page/ {p=$0; n=NR} END{}' SOD_pages.txt\ngrep -n \"\\[pdf page\" SOD_pages.txt | awk -F: '$1<12890' | tail -3",
 "description": "Context for SOD entry 3202 clyb"
}
```


### [2026-09-14T01:22:29.331Z] TOOL RESULT

```
                                                                       cana ©abl. =>csn(,), cn'wq
3198 ckst»k    B                             v^Hjju^j
                                                                        GMS 386, 1205; C2, 69R25
      cokoste (c'k'st'y, cksty, ckst'k) ©*dus-ka(r)sa-
        =»ck}st}y
      ugly
                                                                  3210 cn'yty B, S     (<*-jgs* <, :iS^> ^ <i^>- j-O^uiT /^l
                                                                       canay(a)tc (cnyty) ©<can+dTate ? =»cn}nyty
      GMS 286, 1089; SCE 16, 69                                        completely, absolutely
3199 ckst'k => ckst'k                                                   GMS 475, 1611; TSP 2.43, 340, 574, 69, 467
3200 ckstwny M                                                           n pl69; MDii 1.1, 20; MSP b88
     c(o)kostu/one/i                                              3211 cn'nyty B
                                                                                                                    Sur<k^
      ugliness                                                          cananyate ©<can+anYate
                                                                        completely                    ^cn'yty
      GMS 1089
                                                                        TSP 2.492
3201 cksty     M =» ckst»k
                                                                  3212 cn'nstty B
3202 clyb> C                                      i_aJL^ <uJL*-        cananste ? (ensty)
     caliba ©<Syr.                                                     completely
     cross
                                                                        SCE 124; GMS 475, 1611
     BSTii 880.13; C2, 77R13                                                                                            }Ui
                                                                  3213 cn?wq C
3203 cm-      M, S                                                     thirsty
     cam      (DKhot. tcePma-, Khwar. tsam; Orm. cimi                  canauk, canuq ? =»csn()), csnwq, cn}
       ©nom. ace. -y(yh pi. cmt\ ob. cmf        =*csm,
                                                                       STi 24.7, 25.16, 27.10; GMS   1076
     eye m-                                                       3214 cnNvxy    M
        cy
     GMS 385; STii 1:26, 2.16, 21; BSTi 151                            canuxe/i ? ©Av. anhuyat haca         ^cnm'ny,
                                                                         cnywy,                                        j^jf
3204 cm>n(y)     B                                       j, j          from  heartcnywcm'ny
                                                                                                                                      ii   " 1

      127
                                                                                                                              cntrpVyck
             BBB 730-, GMS         lln 1, 337; Benv. JA 1959, 123              3227 ensty => ennsty, cn'nstty
      3215 cn5>n       S =» cndn
                                                                               3228 cnt'mny B                      jj^jjjl ^*^f <J^jjj'i'
--- pdf page tag near ---
```


## [2026-09-14T01:22:37.634Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor f in MON_part1.txt MON_part2.txt; do echo \"=== $f ===\"; grep -n \"چلیپا\" $f | head -20; done",
 "description": "grep Mo'in for čalipā"
}
```


### [2026-09-14T01:22:38.742Z] TOOL RESULT

```
=== MON_part1.txt ===
13596:چلیپائیان. 
39691:چلیپاییان که یک ساله و بعضی انواعش دو 
54702:خاج: 7 (.) صلیب» چلیپا. خاج اعظم: 
55959:از تیرةٌ چلیپاییان (صلیبیان) که دو نوع سفید 
90101:صلیب: امه [معر. آرا. صلیبا - چلیپا] (ا.) 
=== MON_part2.txt ===
28866:علفی از تیرة چلیپاییان که ار تفاعش بین ۳۰
```


## [2026-09-14T01:22:38.952Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor f in MON_part1.txt MON_part2.txt; do echo \"=== $f ===\"; grep -n \"صلیب\\|صرّاف\\|صراف\" $f | head -20; done",
 "description": "grep Mo'in for salib and sarraf"
}
```


### [2026-09-14T01:22:40.018Z] TOOL RESULT

```
=== MON_part1.txt ===
13744:اصراف: 4 [ع. 8 (مص م 0( بگر دانیدن» 
17960:انصراف: ۲ [ع.] (مص‌ل.) با زگشتن» 
17964:انصرافات. 
30019:عصر جنگ‌های صلیبی از آسیا به مغرب 
30355:گاهی به شکل صلیب در ابتدای مهبل قرار 
35896:انصراف. وصول» رسیدن واصل شدن. 
38058:قبود مادی و حجاب‌های ظلمانی و انصراف 
44239:سره از ناسره» صرافی کردن. تمیز دادن 
44240:عیب‌ها و نیکویی‌های کلام. (امص.) صرافی. 
51255:چلییا: 12 [آرا. صلیبا - معر. صلیت ] 
51257:کردند؛ صلیب. چوب چهار پره که مسیحیان 
54702:خاج: 7 (.) صلیب» چلیپا. خاج اعظم: 
55077:صلیبیان که بطور خودرو در باغ‌ها و صحراها 
55959:از تیرةٌ چلیپاییان (صلیبیان) که دو نوع سفید 
60633:درم کز یننده] (ص فا 0( صراف. 
64689:دینارشمر: ۲ (ص‌فا.) صراف. 
71602:متصل به صلیب که مسیحیان به گردن خود 
79334:علفی از تیرهٌ صلیببان که ۴ گونه از آن 
89341:صراف: له [ع.] (ص.) آنکه پول نیکك 
89345:صرافت: :«۰56: (ع. صرافة] (امص.) شغل 
=== MON_part2.txt ===
17460:صراف. 
18620:کاشی‌های صلیبی شکل که غالبا سنگث‌های 
18622:غیر از اینها اشکال ستاره‌یی صلیبی را که با 
37149:معر .] خزانه‌دار. نقاد» صراف» صیر فی. ها 
38761:را صلیب‌وار بریده باشند - ریزند و نیز در 
66095:صرافی کننده. (اد.) آنکه نیکث و بد قطعه‌ای 
72608:صراف. آنکه سخن درست را از نادرست 
76093:که آن را کیفیت صلیب سیاه گویند (این 
77417:ضح.- نفاخ به تشدید فاء مانند صراف که به 
88049:صلیبی به اروپا رفته است. ویولون را به این 
93215:جام چهار قسمتی به شکل صلیب است که به
```


## [2026-09-14T01:22:46.446Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"--- چلیپا 51250-51262 ---\"; sed -n '51248,51262p' MON_part1.txt\necho \"--- صلیب 90095-90112 ---\"; sed -n '90094,90112p' MON_part1.txt\necho \"--- صراف 89335-89350 ---\"; sed -n '89333,89352p' MON_part1.txt",
 "description": "Print Mo'in contexts"
}
```


### [2026-09-14T01:22:46.551Z] TOOL RESULT

```
--- چلیپا 51250-51262 ---
چله‌نشین: «آ3ه:(۱:)۰۵ا* [- چله نشیننده] 
(ص‌فا.) کسی که در چله خانه نشیند و 
رباضت کشد. گوشه گر منز وی» معتکف. 
(اصطلاح لوطیان) آلت تناسل مرده نره. 
چجلی: 5۱ (حامص.) احمقی؛ بیعقلی. 
دیوانگی» سفاهت.. 

چلییا: 12 [آرا. صلیبا - معر. صلیت ] 
(اخ.) داری که عیسی را بر آن مصلوب 
کردند؛ صلیب. چوب چهار پره که مسیحیان 
نشانادار عیسی (ع) بر گردن آویزند ی با 


خود دارند و يا در کلیساها و نقاط دیگر برپا 

--- صلیب 90095-90112 ---

صله دادن: «د120-.: [ع. ف.) (مسصم.) 
عطا دادن جایزه دادن. 

صله گرفتن: محاع6۲ع- [ع. ف.] (مص‌ل.) 
جایزه گرفتن» انعام گرفتن. 

صلیب: امه [معر. آرا. صلیبا - چلیپا] (ا.) 
شکل صلیب از چوب يا فلز که ترسایان به 
گردن خود آویزند و در کلیسا و خانه و نقاط 
دیگر جای دهند؛ چلیا. صلیب اکبر: ( کذ.) 
تقاطم خط استوا با خط محور (فلکث) که 
خط شمالی جنوبی باشد. صلیب شکسته: 
شعار حزب ناز یسم (دورة هبتلر) در آلمان. 
ولی این شکل در ايران باستان (آثار تخت 
جمشید) و هند قدیم سابقهٌ ممتد دارد. 
صمات؛ 0۳21 [ع.] (اسص.) سگوت» 
صمت؛ خاموشی. 

--- صراف 89335-89350 ---
صراحیه: ()0:5: [ع. صراحیه] (ا.) 
شراب خالص و پاکیزه. سخن خالص و 


بی آمیغ. 

صراط: 3۱ [ع.] (.) راه» طریق. صراط 
مستقیم: : راه راست. 
صراف: له [ع.] (ص.) آنکه پول نیکك 
را از بد جدا کند؛ سره گرء نقاد ناقد. (ف.) 
کسی که به داد و ستد انواع پول پردازد. 
صیرفی. 
صرافت: :«۰56: (ع. صرافة] (امص.) شغل 
و پیشة صراف؛ صرافی. 
صرامت: ادصقمه [ع. و یز 
قطع کردن؛ بریدن. (امص.) دلیری» جرأت» 
مردانگی. 
صرح: : ۶2:6 [ع.] (.) کوشکك» قصر بلند» 
کاخ. صرح ممرد: قصر رخشان و ساده و 
هموار. ( کد.) فلکك.
```


## [2026-09-14T01:22:59.184Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -c \"\" MON_part1.txt; grep -n \"\\[pdf page\" MON_part1.txt | head -3\necho \"--- form feeds ---\"; python3 -c \"\nd=open('MON_part1.txt',encoding='utf-8',errors='replace').read()\nprint('FF count', d.count('\\f'))\n\"\npython3 -c \"\nimport io\nlines=open('MON_part1.txt',encoding='utf-8',errors='replace').read().split('\\n')\n# find page-number-only lines near our targets\nimport re\nfor t in (51255,90101,89341):\n    print('target',t)\n    # search backwards for a short numeric line\n    for i in range(t-1,max(0,t-200),-1):\n        s=lines[i].strip()\n        if re.fullmatch(r'[0-9۰-۹]{2,4}',s):\n            print('  prev numeric line',i+1,repr(s)); break\n    for i in range(t,min(len(lines),t+200)):\n        s=lines[i].strip()\n        if re.fullmatch(r'[0-9۰-۹]{2,4}',s):\n            print('  next numeric line',i+1,repr(s)); break\n\"",
 "description": "Look for MON page markers"
}
```


### [2026-09-14T01:23:00.432Z] TOOL RESULT

```
99339
--- form feeds ---
FF count 0
target 51255
target 90101
target 89341
```


## [2026-09-14T01:23:07.436Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== v2 چلیپا ===\"; grep -n \"چلیپا\\|جلیپا\\|چلییا\" BQT_v2_pages.txt | head -20\necho \"=== v1 ===\"; grep -n \"چلیپا\" BQT_v1_pages.txt | head -5",
 "description": "grep Borhan v2 for čalipā"
}
```


### [2026-09-14T01:23:07.507Z] TOOL RESULT

```
=== v2 چلیپا ===
6651: ‫چلیپا‪- ٩‬‏ بابای فارسی پروزن مسیسا‪,‬‬                     ‫فارسی بروزن خروح ‪ ۰‬افزاری بساشیداکبهآانان‬
6662:      ‫چلیپا‬              ‫کونند سه کوشه ای بداشکه‬        ‫چلو ك ‪ » ۳‬بفتح اول وثانی وواووکاف»‬
6697:                   ‫وصلیب معرب چلییاست ‪#.‬‬          ‫و هر خط منحنی را لیز‬          ‫و برشتةٌ زنار کشند ‪-‬‬
8874:‫خاج " = بر وزن تاج » بمعتی چلیپا‬                                 ‫وژن صابون » بزر که‬          ‫=ر‬
9382:  ‫‪ .‬دانه‌های آن‌فرمز‬                 ‫‪ _ ۴‬خاکےی ص=داااصریا؟ ازتیر‪ :‬چلیپابان ‪8٥‬‬
11000:  ‫=‪ 512801‬از تبرچلیپائبان ‪ )/56۲6]16۵۳‬که‬ ‫‪8 ۴‬‬                                     ‫‪.‬‬   ‫خرجته‬ ‫؟ ‏ رك‬
=== v1 ===
```


## [2026-09-14T01:23:08.781Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\nls\necho \"=== v3 شل ===\"; grep -n \"شلیدن\\|شَل\\b\" BQT_v3_pages.txt | head -20",
 "description": "grep Borhan v3 for šal"
}
```


### [2026-09-14T01:23:08.904Z] TOOL RESULT

```
BQT_v3_pagemap.json
BQT_v3_pages.txt
BQT_v3_picofile.pdf
BQT_v4_pages.txt
BQT_v4_pages.txt.pages
BQT_v4_picofile.pdf
BQT_v5_pages.txt
BQT_v5_pages.txt.pages
BQT_v5_picofile.pdf
=== v3 شل ===
```


## [2026-09-14T01:23:14.487Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"\\[pdf page\" BQT_v2_pages.txt | awk -F: '$1<6710' | tail -4\necho \"=== ===\"\nsed -n '6640,6710p' BQT_v2_pages.txt",
 "description": "Find page tag and print Borhan čalipā context"
}
```


### [2026-09-14T01:23:15.415Z] TOOL RESULT

```
=== ===
                   ‫جله = بکر اول و ف‬                             ‫ساخته بوده‌الد بکصد وشصت گر ؟ ‪.‬‬
‫رسمانی باشد که ازیهنای‌کار جولاهگان زیوآ بد‬
‫وآلرا نبافند و بانگشت ببحیثه در جابی گذار ند‬           ‫جلمچی ‪ -‬باجی‌فارسی بروزن سمنبو »‬
‫زبند ‪ - ۷‬و چهل روزی که‬
                     ‫یو‬‫زمهانرا ک‬
                               ‫‪-‬و ک‬                    ‫خود را زود‬   ‫که لبای و رخوت‬    ‫وا کوند‬   ‫کسی‬


  ‫درویشان در کوشه‌ای شینند وروزمدارند وصادت‬                                    ‫چر کن وه لوث گرداند‬
                                        ‫کنند ‪. ۸‬‬
                                                       ‫چلوج ‪ - ۴‬بضم اول وسکون جيم‬
 ‫چلیپا‪- ٩‬‏ بابای فارسی پروزن مسیسا‪,‬‬                     ‫فارسی بروزن خروح ‪ ۰‬افزاری بساشیداکبهآانان‬
 ‫صلیب تصاری باشد و آن داری است که باعتقاد‬

 ‫ابشان عیسی علیه‌اللام را بر آن کشید» صلیب‬                                                       ‫است‬


                     ‫کرده‌اند و آن‌باین شکل‌است ‪۳‬‬      ‫ونی بواو‬‫چلو چوب ‪ .‬بفتح اول ا‬
                     ‫و آبرا تر‪-‬ابان اطزلا و نقره‬          ‫بواوی‬
                                                              ‫کشیده و ضم جیم فارسی و سکون وا‬
                     ‫سازند و بجهت تیمن و تبرك‬         ‫ابجد ‪ ,‬سیخ کباب راکوبند ‪ » ۴‬و نم اول هم‬
                     ‫بر گردن آویزند ؛ و بعضی‬                                                ‫گنتهاند ‪.‬‬
      ‫چلیپا‬              ‫کونند سه کوشه ای بداشکه‬        ‫چلو ك ‪ » ۳‬بفتح اول وثانی وواووکاف»‬
                                                                        ‫!‬    ‫فت‬
                                                                              ‫‪):‬سچش‬
                                                                                  ‫(‪۱‬‬

      ‫‪ «۱‬در میان خراییهای (ظ ‪ .‬خرابه های) عمارت جمشیدی توتیای هندی بابند‪...‬‬
     ‫‪ ۳‬طم‬       ‫اکنون‌مردم ستونهایی که در آن‌عمارت مانده جهل منار می‌خوالند‪« ¢ .‬نز هه القلوب مقالهٌ‬

                     ‫‪:‬‬    ‫‪ :‬تخت حمشف‬   ‫رک‬   ‫‪- ۴‬‬          ‫لیسترانج ‪ ۱۳۳۱‬ص‪ ۱۲۱‬در ذ کر اصطخر ‪.‬‬
                    ‫کام خوبش از دهان او ب رگیر‬               ‫هرویی چو لعبت سیمن‬
                    ‫میلی ازچل‌مناره درب رگیر‪.‬‬                ‫ور بلندی درشت میشواهی‬
             ‫سعدی شامزی«کلعات چاپ‪ ۹۵۲۱‬قمری‪ :‬مقطعات (شمارء صفحه ندارد) »‪.‬‬
                      ‫جولو چوب ‪.‬‬
                               ‫ك ‪:‬وجل‬
                                    ‫ر‪-‬‬‫‪۴‬‬       ‫مصحف چکوج («‪.‬م‪۰ ).‬‬     ‫‪۳‬‬

     ‫‪ - ۷‬باین معنی درتر کی‬   ‫حل‪-‬وركن‪:‬ك‌وجلنگ ‪.‬‬
                                             ‫‪۱‬‬         ‫= جلو («‪.‬م‪.).‬‬ ‫‪۵‬‬

      ‫آلار هن «را؛رهةالمعارف‬    ‫صوم‬    ‫‏‪A‬‬
                                                    ‫فچلی» بکسر اول و «چلیه» آمده «چنتابی ‪. ۷۸۲۰‬‬
      ‫اسلام» باين معنی از ‪ :‬چل (چهل) ‪ +‬ه (نبت) « چله چپل روزباشد که زن‌بنشیند ازبهرزادن‬
       ‫ی مدانگ که ياك شود وبدان چهل‌روز نگره‌ابه شود و نماز نکند گویند بجله‌دراست ‪ ۰‬عسجدی‬
                                                                                     ‫(مروزی) کوبد ‪:‬‬
                                                                    ‫برافشاندم خدوا لودچله درشکاف او‬
                             ‫‪ ۲‬ص ‪٩‬‏ صلیبا (عربی صلیب) ‪:‬‬     ‫ماخوذ از آرامی «اسقا ‪9‬‬      ‫‪۹‬‬

                ‫مانند یکی فکیرون چلیا ‪.‬‬                       ‫آن زاغ‌رانگه کن چون می‌پرد‬
      ‫‪٩.‬‏‬    ‫ممارء مروزی‪« .‬لت فرس*‪۱‬‬
                                                                                              ‫‪۳‬ی‬
                                                                                               ‫—~ ‪۷‬‬


‫کفته‌اند ‪ -‬و کنایه ار زلف ممشوق حم هت ‪.‬‬            ‫براهمه و نود ازطلاا و نقره و امثال آن سازد‬

                   ‫وصلیب معرب چلییاست ‪#.‬‬          ‫و هر خط منحنی را لیز‬          ‫و برشتةٌ زنار کشند ‪-‬‬




                                     ‫بیان هیحد هم‬
            ‫درجیم فارسی بامیم مشتمل بوش و دوقتو کات‬

 ‫که معني‌ندارد‪ -‬ویمعنی‌جرم وکناه نگیفزته‌انس‬       ‫چم = بفتح اول و سکون الی » بمعنی‬
 ‫وخوردن آوشامیدن راهمکویند‪ .‬ومرومدارالمرز‬         ‫وسر بر‬
                                                       ‫‪-‬م‬
                                                        ‫خرام روفتاری (‪ )۲‬بناز باشد ‪٩‬‏ ا‬
‫و مردم مروشاهجان چشم را چم میگوبند که‬             ‫‪-‬تواری را‬
                                                          ‫‪۷‬ف‬‫خرامیدن همهت بعنی بخرام ر‬
```


## [2026-09-14T01:23:21.573Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -c \"\\[pdf page\" BQT_v2_pages.txt; grep -n \"\\[pdf page\" BQT_v2_pages.txt | head -3\npython3 -c \"\nd=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nprint('FF',d.count('\\f'))\n\"",
 "description": "Check BQT v2 page tags"
}
```


### [2026-09-14T01:23:22.674Z] TOOL RESULT

```
0
FF 683
```


## [2026-09-14T01:23:25.771Z] TOOL CALL #17: Bash

```json
{
 "command": "sed -n '1,60p' tools/ref_page.py",
 "description": "Inspect ref_page tool"
}
```


### [2026-09-14T01:23:25.819Z] TOOL RESULT

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


## [2026-09-14T01:23:28.212Z] TOOL CALL #18: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:1287 2>&1 | head -60",
 "description": "Fetch Borhan page 1287"
}
```


### [2026-09-14T01:23:36.343Z] TOOL RESULT

```
REF: BQT:1287  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 78  OCR-lang: fas

۱ هل

ش لفت ۱ < بکر اول وئانی بر وزن | مخفف‌شگون‌است ۴ که فاليك و بفال پرداشتن
گرفت » بمعئی عجب و تءجب باشد ۳ . و میمنت داستن چیز ها باشد مثل پرواز وآواز

شگل ؟ - بکر اول وانی و سکون مرغان و حرکات و سکنات آدمیان و وحوش
لام 0 چداری باشد كوچك که هر دو دست اسب وامثال آبشان
و استر را بدان محکم بنداد - و ریسمالیرا نیز شگون ۱ - بنم اول بر وزن سکون »
کوبند که برپای کنجشك بندند. بمعنی شگن است که فال ليك - و بفال‌برداغتن

شگن - بطم اول و ثالی وسکون نون . | ومبارك داستن چیزها باشد .

بیان هیجدهم
در شن نقطه دار 0 لام مشتمل در بیست وشش لغت

شل - بفتح اول و سکون نالی » پوست چیق نرم و است را کوبند ‎٩‏ - و بکر اول
باز اه رلگ: را گونند که در مبان درز کفش نیزه کوچکی است که آبراکاهی دویره و سه‌یره
و موزه و براق زین اسب نهاده بدوزند بجهت سازند و پنج و ده آلرا بردست کبرند و يك يك
خوشآبند کی و بعطی از براق اسب را نیز بآن را بجالب دشمن اندازند*۱ - ومیوه‌ای باشد کرو
دوزند - و رانآدمی راکوبند خصوصاً وران‌سایر | و مدور مانند بهی وطعم آن یز باتلخی آميخته
خحیوانات را ءموما ۷ - و بعربی دست و-پای را | باشد وآلرابهندی بیل کویند واز آن مر‌بامازند؟
گوبند که از کار بازمانده باشد ۸ - و بضم اول | و باین مهنی بضم اول هم آمده است.

۹ * شکیفت (ه.م.) پهلوی 510۱]1 (عجیب » حیرت انگیز) ر4:شکفتن. 5018160
از 5818۷11 #* با 51310]1 مستقیماً همریشه است . قس‌ريشهٌ اوستابی - 8162012 «بارتولمه
۹ ایرالی میاله 55۹1 (عمجیب) رز ۹ ۳ - ویمعئی ممجزه :
« عیسی بدوگفت تا آبتها و شگفتها نمی بینید ایمان نمی آورید ...» «انجیل قارسی ص۰۸۸

۴ اه شگال » شکال » شکیل . ۴ - رك4 : شگون .

- مامر زهره خیره‌بین ازحسنشان ‏ مشتری از روبعان کیرد شگن .

مولوی بلخی. «فرهنگه‌نظام».

۹ - سانسکر,ت 516176 ( پرنده» مخصوصاً پرنده‌ای که خوش بمن با شوم باشد)
۶« وبلیامز ۰۹۲:۱*۸۹ ۷ -قفس: شننگه , شلوار . «اسشق - هوبشمان ۸۹

۸ - عل (بفتح‌اول‌وتشدید دوم) مصدراست بمعنی تباه شدن دست‌وخدك کردیدن ,واغل
بفتح اول ودوم ونددید سوم » مردتباه دست (منتهی الارب ) وشل بمعنی آاخیر تصرفنی است از
ابرایان دركلمة اشل عربی وشلیدن هم مصدر جعلی آنت. .

. ‏چون‌بدیدآن روی هه‌چون‌بر ک هکل مططرب کردید و شد پاهاش شل‎ - ٩
‏مولوی پلخی «مثنوی».‎

*۶ - درهند سیل کویند بسین مپمله ویای «*جپول «بپارعجم» :

بگوندٌ غل اففالیان دوپرء وتیز چودسته بسته بهم‌تپرهای بی‌سوفار ‏ ۶ فرخی-رستانی ۶۹۳ ۰
```


## [2026-09-14T01:23:55.174Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN 1966 around 35228 ===\"; sed -n '35224,35232p' KLN_1966.txt\necho; echo \"=== KLN sarraf/sarf ===\"; grep -n -i \"sarraf\\|sarrāf\\|Arab. sarafa\\|sarafa\\|sayrafi\" KLN_1966.txt | head -20",
 "description": "Klein silver entry + sarraf"
}
```


### [2026-09-14T01:23:55.313Z] TOOL RESULT

```
=== KLN 1966 around 35228 ===
Silurian,  adj.,  pertaining  to  the  geological  period that  preceded  the  Devonian.  —  Prop,  ‘pertain¬ ing  to  the  rocks  of  Wales,  once  inhabited  by  the Silures'  (see  prec.  word).  The  name  Silurian  was given  to  this  period  by  the  geologist  Sir  Roderick Impey  Murchison  (1792-1871),  because  the rocks  characteristic  of  this  period  are  especially frequent  in  Wales.
Derivative:  Silurian,  n.
silvan,  sylvan,  adj.,  1)  living  in  the  woods;  2) wooded.  —  Formed  with  suff.  -an  fr.  L.  silva, ‘wood,  forest’,  which  is  of  uncertain  origin.  The spelling  sylvan  (with  y  for  i)  is  due  to  the  in¬ fluence  of  Gk.  5X7),  ‘forest’,  from  which  silva was  supposed  to  derive.  Cp.  savage,  Silas, Silvester,  Silvia.
Derivatives:  silvan,  sylvan,  n.,  silvan-ity,  n., silvan-ry,  n.
silver,  n.  —  ME.  silver,  fr.  OE.  seolfor,  siolofr, silofr,  rel.  to  OS.  silutar,  ON.  silfr,  Dan.  solv, Swed.  silver,  MDu.  silver,  Du.  silver,  OHG. sillabar ,  silabar,  MHG.,  G.  silber,  Goth,  silubr. Cp.  OSlav.  sirebro,  OPruss.  siraplis,  Lith.  sida- bras,  ‘silver’.  All  these  words  are  prob.  borrow¬ ed  ult.  fr.  Akkad,  farpu,  ‘silver’,  lit.  ‘refined
silver’,  which  is  rel.  to  $arapu,  ‘to  refine,  smelt’, farrapu,  ‘goldsmith’,  Heb.  tzardph,  ‘he  refined, smelted’,  tzoreph,  ‘goldsmith,  silversmith’, Aram. -Syr.  tzeraph,  ‘he  refined,  smelted’,  Arab. sarf,  ‘pure  (wine)’.
Derivatives:  silver,  tr.  v.  and  adj.,  silver-ed,  adj., silver-er,  n.,  silvern  (q.v.),  silver-y,  adj.,  silver-i- ness,  n.
silverize,  tr.  v.,  to  cover  with  silver.  —  A  hybrid coined  fr.  silver  and  -ize,  a  suff.  of  Greek  origin.
silvern,  adj.  —  ME.  silveren,  fr.  OE.  seolfren, silfren,  fr.  seolfor,  siolofr,  silofr,  ‘silver’.  See silver.

=== KLN sarraf/sarf ===
35077:shroff,  n.,  name  of  a  money  changer  in  the  Far East.  —  Hind,  sarraf,  fr.  Arab,  sarrdj,  ‘money changer’,  fr.  sarrafa,  ‘he  changed  money’, second  conjugation  of  sarafa,  'he  turned’, shroud,  n.  —  ME.  schrud,  shrud,  shroud,  fr.  OE. scrud,  ‘dress,  garment’,  rel.  to  ON.  skrud,  ’the shrouds  of  a  ship,  ornament,  furniture  of  a church’,  Dan.,  Swed.  skrud,  ‘dress,  attire’,  and in  gradational  relationship  to  OE.  screade, scread,  ‘shred,  paring’.  See  shred,  n. Derivatives:  shroud,  tr.  v.,  shroud-ed,  adj., shroud-ing,  n.,  shroud-less,  adj.,  shroud-y,  adj. Shrovetide,  n.,  the  time  for  confession  before Lent.  —  ME.  shroftide,  schroftide-,  compounded
```


## [2026-09-14T01:23:57.752Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD watkins silver ===\"; grep -n -i \"seolfor\\|silver\" AHD_watkins1985.txt | head -20\necho; echo \"=== SKT silver ===\"; grep -n -i \"SILVER\" SKT.txt | head -10\necho; echo \"=== AKD sarpu ===\"; grep -n -i \"sarpu\\|sarapu\\|ṣarpu\" AKD.txt | head -20",
 "description": "AHD/Skeat/Zimmern for silver"
}
```


### [2026-09-14T01:23:57.845Z] TOOL RESULT

```
=== AHD watkins silver ===
172:The Indo-Europeans knew metal and met- allurgy, to judge from the presence of the word ayes- in Sanskrit, Germanic, and Latin. The term designated copper and perhaps bronze. Iron is a latecomer, technologically, and the terms for it vary from dialect to dialect. Latin has ferrum, while the Ger- manic and Celtic term was *isarno-, properly “holy (metal),” doubtless so called because the first iron was derived from small meteor- ites. Gold was known from ancient times, though the names for it vary; ghel-2, prob- ably “yellow (metal),” and aurum (*aus-, Latin aurum), are widespread. Silver was arg-, with various suffixes, doubtless mean- ing “white (metal).”
290:arg-. To shine; white; the shining or white metal, silver. 1. Suffixed form *arg-ent- in Latin argentum, silver: ARGENT, ARGENTINE. 2. Suffixed form “arg-i-U/l)- in Greek argillos, white clay: ARGIL. 3. Suffixed form *arg- u-ro- in Greek arguros, silver: LITHARGE, PYRARGYRITE. 4. Suffixed form *arg-i-n- in Greek arginoeis, brilliant, bright-shining: ARGININE. 5. Extended form “argu-, brilliance, clarity, in Latin denominative arguere, to make clear, demonstrate: ARGUE. 6. Suffixed form *arg- ro- in Greek argos (< *argros), white (see pel-2). [Pok. ar(e)g- 64.]
540:(COVEN), (COVENANT), EVENT, INTERVENE, INVENT, MIS- ADVENTURE, PARVENU, PREVENIENT, PREVENT, PROV- ENANCE, (PROVENIENCE), REVENANT, REVENUE, SOUVENIR, SUBVENTION, SUPERVENE. 3. Suffixed zero-grade form *gvm-yo- in Greek bainein, to go, walk, step, with basis (< *gm-ti-), a stepping, tread, base, and -batés (< *gwa-to-, zero-grade of gd-, contraction of *gaa-), agential suffix, “one that goes or treads, one that is based”: BASE!, BASIS; ABASIA, ACROBAT, ADIABATIC, AMPHISBAENA, ANABAENA, DIABASE, DIABETES, STEREO- BATE, STYLOBATE. 4, Suffixed zero-grade form “g“(g)-u- in compound form “pres-gu-, “going before” (see per’). 5. Basic form *gvd- in Greek béma, step, seat, raised platform: BEMA. 6. Sanskrit jigdti, he goes: JUGGER- NAUT. [Pok. g¥d- 463.] gvadh-. To sink. Possible root. 1. Suffixed form *guadh-u- in Greek bathus, deep (> bathos, depth): BATHOS, BATHY-. 2. Greek benthos, depth, may be formed on bathus by analogy with penthos, grief, and pathos, passion, suffering (or it may be from an unrelated root *g¥(e)ndh-): BENTHOS. 3. Suffixed variant form *gudh-yo- in Greek bussos, bottom of the sea: ABYSS. [Pok. gddh- 465.] g’ébh-'. To dip, sink. Suffixed zero-grade form *gvabh-yo- in Greek baptein, to dip: (BAPTIST), BAPTIZE; ANABAPTIST. [Pok. g¥ébh- 465.] g”ébh-2. Hypothetical base of some Germanic words associated with the notion of sliminess. 1. Middle Dutch quac-, unguent, liquid, in obsolete Dutch quacksalver, quacksalver: QUACKSALVER. 2. Low German quabbeln, to shake like jelly, tremble, akin to Middle English quaven, to tremble: QUAVER. [Pok. 2. g¥ébh- 466.] grei-. Also gveia-. To live. I. Suffixed zero-grade form *gwi-wo-, *gi-wo- (< *gi9-wo-), living. 1. Germanic *kwi(k)waz in: a. Old English cwic, cwicu, living, alive: QUICK, QUICKSILVER; b. as a name for couch grass (from its rapid growth), in Old English cwice, couch grass: (COUCH GRASS), QUITCH GRASS. 2. a. Latin vivus, living, alive: VIVIFY, VIVIPAROUS; b. Latin denominative vivere, to live: VIAND, VICTUAL, VIVA, VIVACIOUS, VIVID; CON- VIVIAL, REVIVE, SURVIVE. 3. Further suffixed form *gvi- wo-td in Latin vita, life: VIABLE, VITAL; LIGNUM VITAE, VITAMIN. II. Suffixed zero-grade form *gia-o- in Greek bios, life (> bioté, way of life): BIO-, BIOTA, BIOTIC; AEROBE, AMPHIBIOUS, ANABIOSIS, CENOBITE, MICROBE, RHIZOBIUM, SAPROBE, SYMBIOSIS. III. Variant form *gwyd- (< *gvyoo-). 1. Greek z0é, life: AzO-, (DIAZO). 2. Suffixed form *gvy6-yo- in Greek zdon, zdion, living being, animal: (-Z0A), -ZOIC, ZOO-, ZOON, -ZOON. IV. Pre- fixed and suffixed form *su-g~ia-es- (*su-, well; see su-), “living in good condition,” in Greek hugiés, healthy: HYGEIA, HYGIENE. [Pok. 3. gei- 467.] g”eia-. To press down, conquer. Sanskrit jayati, he con- quers: JAIN. [Pok. gveio- 469.] gvel-'. To pierce. 1. Suffixed o-grade form “gvol-eyo- in Germanic *kwaljan in Old English cwellan, to kill, destroy: QUELL. 2. Suffixed zero-grade form *g“/-yo- in Germanic *ku/jan in Old English *cyllan, to kill, perhaps the source of Middle English killen, to kill: KILL}. 3. Full-grade form *gvel- in Greek beloné, needle: BEL- ONEPHOBIA. [Pok. 1. g¥el- 470.] gel-2. To fly; a wing. Possibly in Latin voldre, to fly: VOLANT, VOLATILE, VOLE2, VOLITANT, VOLLEY. gvel-3, To swallow. Dissimilated to *gel-. 1. Germanic *kel- in Old English ceolu, throat, dewlap, perhaps akin to Middle English cholle, throat: JowL?. 2. Germanic *keluz in Old Norse Aj6ir, keel: KEEL}. 3. Suffixed zero-grade form “gul-d in Latin gula, gullet, throat, palate: GOLIARD, GULAR, GULES, GULLET. 4, Extended (expressive) form *glutt- in: a. Latin gluttire, gliitire, to swallow: GLUT; DEGLUTITION; b. Latin glutté, a glutton: GLuTTon. [In Pok. 2. gel- 365.] gvelbh-. Womb. 1. Suffixed form *gvelbh-u- in Greek delphus, womb, whence delphis, dolphin (referring to its
1078:a. Latin téla, web, net, warp of a fabric, also weaver’s beam (to which the warp threads are tied): TILLER?, ToiL2; b. Latin subtilis, thin, fine, precise, subtle (< *sub-téla, “thread passing under the warp,” the finest thread; sub, under; see upo): SUBTLE. 3. Suffixed form *teks-On, weaver, maker of wattle for house walls, builder (possibly contaminated with *teks-tdr, builder), in Greek tekton, carpenter, builder: TECTONIC; ARCHITECT. 4. Suf- fixed form *teks-nd-, craft (of weaving or fabricating), in Greek tekhné, art, craft, skill: TECHNICAL, POLYTECHNIC, TECHNOLOGY. 5. Possibly Germanic *thahsu-, badger (“the animal that builds,” referring to its burrowing skill), in Old High German dahs (> German Dachs), badger but more likely borrowed from the same pre- Indo-European source as the Celtic totemic name Tazgo-, Gaelic Tadhg, “‘badger’”): DACHSHUND. [Pok. tekth- 1058.] tekv-. To run, flee. Suffixed o-grade form *tokv-so- in Iranian *taxsa-, bow, borrowed into Greek toxon, bow, also (in the plural) bow and arrow (< “that which flies’): Toxic. [Pok. tekz- 1059.] tel-. Ground, floor, board. 1. Germanic *thil-j6- in Middle Low German and Middle Dutch dele, plank: DEAL?. 2. Suffixed form *tel-n- in Latin telliis (stem telliir-), earth, the earth: (TELLURIAN), (TELLURIC), (TELLURION), (TELLURIUM), TELLURO-. 3. Possibly reduplicated form *ti-tel- in Latin titulus, placard, label, superscription, title: TITLE. [Pok. 2. tel- 1061.] tela-. To lift, support, weigh; with derivatives referring to measured weights and thence to money and payment. 1. Suffixed form *telo-mon- in Greek telamén, supporter, bearer: TELAMON. 2. Suffixed form *tel/a)-es- in: a. Greek telos, tax, charge: TOLL!; PHILATELY; b. Latin tolerdre, to bear, endure: TOLERATE. 3. Suffixed zero-grade form *th-i-, becoming *tali- (influenced by ¢dlis, such), in Latin ¢alid, reciprocal punishment in kind, “something paid out”: TALION; RETALIATE. 4. Suffixed variant zero-grade form *tala-nt- in Greek talanton, balance, weight, any of several specific weights of gold or silver, hence the sum of money represented by such a weight: TALENT. 5. Perhaps intensive reduplicated form *tantal- in Greek Tantalos, name of a legendary king, “the sufferer’: (TANTALIZE), TANTALUS. 6. Perhaps zero-grade form *tla- in Greek Atlas (stem Atlant-), name of the Titan supporting the world: ATLANTIC, ATLAS. 7. Suffixed zero-grade form *tl-é- in Germanic *thulén in Old English tholian, to suffer, endure: THOLE. 8. Suf- fixed zero-grade form *tl-to- in Latin ldtus, “carried, borne,” used as the suppletive past participle of ferre, to bear (see bher-'), with its compounds: ABLATION, COL- LATE, DILATORY, ELATE, ILLATION, LEGISLATOR, OB- LATE], PRELATE, PROLATE, RELATE, SUPERLATIVE, TRANSLATE. 9. Suffixed zero-grade form *tl-d- in San- skrit tuld, scales, balance, weight: TAEL, TOLA. 10. Nasal- ized zero-grade form *tl-n-a- in Latin tollere, to lift: EXTOL. [Pok. 1. éel- 1060.] tem-. Also teme-. To cut. I. Form *tema-. Nasalized form *t(e)m-n-a- in Greek temnein, to cut: TMESIS, TOME, -TOME, -TOMY; ANATOMY, ATOM, DIATOM, DICHOTOMY, ENTOMO-, EPITOME. II. Form *tem-. 1. Suffixed form *tem-lo- in Latin templum, temple, shrine, open place for observation (augury term < “place reserved or cut out”), small piece of timber: TEMPLE!, TEMPLE’; CONTEMPLATE. 2. Extended root *tem-d- becoming *tend- in o-grade suffixed (iterative) form *tond-eyo- in Latin tondére, to shear, shave: TONSURE. [Pok. 1. tem-, tend- 1062.] teme-. Dark. Suffixed form *tema-s-. 1. Latin temere, blindly, rashly: TEMERARIOUS, TEMERITY. 2. Suffixed form *temas-rd- in Latin tenebrae (plural), darkness: TENEBRAE, TENEBRIONID. [Pok. tem()- 1063.] temp-. To stretch. Extension of ten-. 1. Possibly Latin tempus, temple of the head (? where the skin is stretched from behind the eye to the ear): TEMPLE?. 2. Zero-grade form *tmp- perhaps in: a. Persian taftan, to weave (the
2151:QUICK gWei- QUICKSILVER gWel- Quip! gwet-1

=== SKT silver ===
928:F.  ar^m'.^L.  arymtum.  silver:   from  iU    V brigbtncas.  (•^AKG,  to  tfainc.>  Sec  below. Argillaoeous,  clayey.  (L.)     U  argii/a- eettJt  adj.  from  argiHaf  day,  csp.  while  clny.
4655:dollar.  (Du.  —  G,>  Do.  JaalJtr,  a dollar.  Adapted  and  borrowed  from  G. thaler^  a  dollar.  The  G.  rhaitr  U  short {qt  j0achim.ftkaUr,  a  coiti  m.iile  from  silver fuim  1  in  Joachirruthal  ^Joachim's  dale)  in Uohvniia,  ab.  a.o.  1518.
6580:ftligrree.  Span.  -  U)  Formerly //«'- grvnt;  XVII  cent.  —  Span./Zi^rana,  fili- gree-work, fine  wrought  work.  — Span. ^/d, a  thread  or  tow,  JiJar,  to  spin ;  gutno,  grain or  texture ;  so  called  because  the  chief texture  of  it  was  wrought  in  silver  wiie. From  X^filnm,  thread;  ^ranum^  grain.
11128:mark  (i),  a  coin.  (E.)  M.  £,  mart, A.  S.  marc,  a  mark,  coin  ;  a  particular  use of  A.  S.  meartt  a  mark,  stomp,  &C'4-G. mark,  a  weight  of  silver,  a  coin :  Icel.  m&rk. marquo,  letters  of.  (F.*G.)  A Utter  of  marque  was  a  v<Tm\&^Qtv  \r)  % ntlcr  to  ooake  tvpiisaU  4iu  v\ui  gouBXri  ^
11445:mercury.  q»ick«ilver.  (F.  — O  ME. mtrcurie,  quicksilver, narard  after  the  planet Mercury.  —  O.  F.  Me*xurit  U  Norman foim^;  F.  mtrcure.  —  L.  Mtrcunnm,  ace, of  Mircurius,  Mercnr)*,  god  of  tiaftic.  •■  L. mer<;  item  of  merx,  merchandise.
11505:•ks  off;  also,  a  glimmer,  or  cat-silver,
11506:hctalUcIc  boHr  like  silver,  which  shines
14142:Plate,  a  thin  piece  of  metil.  fl'i  <lol (F.-Gk.)  M.E.//a/^-OI  ": ivrly  the  fem.  oX  plat,  flat. plata,  a  lamina*  plate  of  ru:  .-  . Plafa,  plate,  silver;  but  the  Span was  borrowed  from  French.  —  Gk.  rkuA flat,  broad;  whence  also  Do  Van  plat. ( Svted.plaft,  flat.  +  Lilhuan.  platus,  broiJ Skt.  pxithtu,  large.     (V  PRAT  >
14163:See  alfove ;  and  t»ee  Form. metal.   (Span   —  F   —  Gk.) named  from  in  silvery  ap- i.  ft'o/a,  silver.  —  O.  F.  fi/tUi,
14164:xte,    also   silver   plate ;   aec

=== AKD sarpu ===
360:alvk.  Mtrapu  Goldschmied  (sarpu  Silber,  siirrujnt  (MetsiYle)  schmel- zen) :  >  wohl  durchweg  der  St.  srp  in  der  Bed.  des  MetaUschmelzens, -läuterns  im  Hebr.  (auch  Phon.)  und  Aram.  (>>  im  Arab.).  akk.  Jcu-
```


## [2026-09-14T01:24:25.779Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN calipa/salib/sal ===\"; grep -n -i \"čalīpā\\|calipa\\|tschalīpā\\|schal\\b\\|Kreuz\" HRN.txt | head -20\necho; echo \"=== HUB ===\"; grep -n -i \"calipa\\|Kreuz\\|salīb\" HUB.txt | head -20\necho; echo \"=== AFA (Fraenkel aram. Fremdw.) salib ===\"; grep -n -i \"Kreuz\\|salīb\\|salib\\|sarraf\\|sairafi\" AFA.txt | head -30",
 "description": "grep Horn, Hübschmann, Fraenkel"
}
```


### [2026-09-14T01:24:26.409Z] TOOL RESULT

```
=== HRN calipa/salib/sal ===
4999:Nii^£»NT1 bedeutet *Kreuz* (Nöldeke, Mand. Gramm. 309 Nore i).

=== HUB ===
2452:patiy kar *kreuzigen (Bang: pfahlen') gehOrt schwerlich
7893:in uzmaydpatiy *an das Kreuz' und in paruzana- Von vielen StUmmen^
8092:s. oben, raja^ raza oben p. 66 ^). Np. ocaj *Kreuz' aus alterem
8093:"^xac = arm. xac *Kreuz* ist arm. LW.

=== AFA (Fraenkel aram. Fremdw.) salib ===
9341:arabien war Ton Abessynien aus das Kreuz gepredigt wor-
9665:109 sind noch zu erklären. Das Kreuz ._*-J-i Nibiga 2, 10
```


## [2026-09-14T01:24:28.264Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FVQ salib ===\"; grep -n -i \"salīb\\|salib\\|crucif\\|cross\" FVQ_pages.txt | head -20\necho; echo \"=== AFM ===\"; grep -n \"صليب\\|چليپا\\|صراف\" AFM_pages.txt | head -20\necho; echo \"=== TAD ===\"; grep -n \"صليب\\|صلیب\\|چليپا\" TAD_pages.txt | head -20",
 "description": "grep Jeffery, Addi Shir, Unaysi"
}
```


### [2026-09-14T01:24:28.363Z] TOOL RESULT

```
=== FVQ salib ===
1288:or by traders who had crossed from Egypt or Abyssinia, 8 it is impossible,
2102:that this was the form that crossed over into Arabia, his further
2256:him " to a place on high " may refer to the saint's crucifixion. R. Hartmann, in
2512:across a pO^K *12 "HO (Baba Mezi'a, 39 b ), showing a form with
4111:1 Strcck, EI t i, 1059 ; ZA, xv, "2T2 IT. Bcrossus says it landed jrpo; r<Z opcL run-
6791:with which we may compare Heb. T"}B? to lay cross wise, to interweave,
7171:To crucify.
7172:The passages are all relatively late. Once it refers to the crucifixion
7173:of our Lord (iv, 156), once to the crucifixion of Joseph's prison com-
8805:were in favour of its being Greek (ath-ThaSalibl, Fiqh, 318 ; as-
9142:board, e.g. the rtrAo? affixed to the Cross, and for the tablets of the

=== AFM ===
3119:* ( فأوَانيا) اصول بيض غليظة كلا صابع يقال لها عود الصليب يتداوى بها

=== TAD ===
230:                                               ‫بلادنا إبان الهروب الصليبية‬
```


## [2026-09-14T01:24:34.176Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '7160,7200p' FVQ_pages.txt\necho \"=== page tag ===\"; grep -n \"\\[pdf page\" FVQ_pages.txt | awk -F: '$1<7200' | tail -2",
 "description": "Print Jeffery salaba entry"
}
```


### [2026-09-14T01:24:35.252Z] TOOL RESULT

```
Aramaic into Pahlavi as )^)j srdt. Cf. Bailey in JRAS, 1934, p. 505.
3 Fraenkel, Vocab, 25 ; von Kremer, Ideen, 226, n. ; Dvorak, Fremdw, 26, 31, 76 ;
Vollers, ZDMO, 1, 614 ; Ii, 314.
4 Hoffmann, ZA, xi, 322. What Fraenkel, Fremdw, 237, means by JimST I know
not.FOREIGN VOCABULARY OF THE QUR ? AN 197
occurs in the genuine old poetry, but it is found in the S. Arabian
inscriptions, where X40&> X40& = aedificium elatum (Rossini,
Glossarium, 225).
(Salaba).

iv, 156 ; v, 37 ; vii, 121 ; xii, 41 ; xx, 74 ; xxvi, 49.
To crucify.
The passages are all relatively late. Once it refers to the crucifixion
of our Lord (iv, 156), once to the crucifixion of Joseph's prison com-
panion (xii, 41), and in all the other passages to a form of punishment
which Muhammad seems to have considered was a favourite pas-
time of Pharaoh, but which in v, 37, he holds out as a threat against
those who reject his mission.
The word cannot be explained from Arabic, as the verb is denomina-
tive from <^Ju?. This c^*Ju* occurs in the old poetry, e.g. an-Nabigha,
ii, 10 (Ahlwardt, Divans, p. 4), and 'Adi b, Zaid (Aghanl, ii, 24), etc.,
and is doubtless derived from Aram. NIT /JS ; Syr. )cu.^, as
Fracnkel, Freutdw, 276, claims. The word is not original in Aram., how-
ever, and perhaps came originally from some Iranian source from a root
represented by the Pers. Ui>- (Vollers, ZDMG, 1, 614). Mingana,
y * V
Syriac Influence, 86, claims that it was from Syr. rather than from
Jewish Aram, that the word came to Arabic, and as the Eth.
seems to be of this origin, 1 it may be so. 2
(Salawdt).
xxii, 41.
Places of worship.
Though the Commentators are not unanimous as to its meaning
they are in general agreed that it means the synagogue of the Jews,
and as such many of them admit that it is a borrowing from Heb.
(Baid. and Zam. on the passage 3 : al-Jawaliql, Mu'arrab, 95 ; as-Suyuti,
1 The form fl ft/fl is later and derived from the Arabic (Noldeke, Neue Beitrdge, 35).
2 So Ahrens, Christlichefi, 40.
3 That it was a borrowing is evident from the large crop of variant readings of
the word noted by al-'Ukbari, Imla\ ii, 89.198 FOREIGN VOCABULARY OF THE QUR*AN
Itq, 322 ; al-Khafaji, 123 ; as-Sijistam, 201). This idea that it is Hebrew
=== page tag ===
```


## [2026-09-14T01:24:46.836Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '9650,9680p' AFA.txt",
 "description": "Print Fraenkel context for salib"
}
```


### [2026-09-14T01:24:46.933Z] TOOL RESULT

```
Mu^arr. 62); ^jjül^ aus M^tAixoV IniSoAo (über die
.1 «'^ '-'-^ >- -"--^
LlU
l'T \\'\ Ulllii
rf^MMl^h
»4 . -« • Kdurcli Tgl. Hamüsa 244; Nüldeke 3/iinr^. -
Cnimm.p.38. Anm. 2 ; Hoffmaon Z D M G. XXXII. 748);
Ton .'1 » U» aus rxrpiipxi^ (sehr wohl voa ■^jiTpixio: iZjJbJ
unterschiedeD). Deutlich ist ferner .j^Ll »Inspector", ent-
Icbot aua U&^^'O'i atJioQ durch dia Form und das Heraus-
treten aus der Lautverschiebung als unarabisch gesichert.
,j- 1 ,i4 iDiacoQua" (schon als Name in alter Zeit bekannt)
Ibn Dor. Kit-al-iStik. 2GS , 12; Plur. ^j«xL-i Jäk. H. 830,
5 ist entlehnt aus Ul=l ; ^_^l-k«. aus ^=^,1-^ PSm.
2086. Aber jjtj und Nebenformen Mu^arr. 151 ; Gl. BelLi(j.
109 sind noch zu erklären. Das Kreuz ._*-J-i Nibiga 2, 10
ist bekanntlich durch Vennitteluug des aramüischen L ?^ * S ,
N3'7V aus pera. [ .^ ^ \ y entlehnt. Darnach ist Gesenius
Hwb. IX. 710. Sp. -i. Z. 15 a. f. zu berichtigen. Die Wur-
Bel .„wLö ist aber auch echt Amrk. 55, 11.
Deutlicli ist die Entlehnung des ^«Su des Holzes, mit
dem die Christen im Oriente auch noch heute zum Gottes-
dienste rufen, (vgl. de Vogue in der Revue des deui mon-
des 1876 I. 307) und welches Muhammed eiue Zeitlang für
seine Gläubigen adoptiert hatte (Ibn Doreid Kit-at-i£tiJf.
p. 268 unten) '^Äntara App. 5, 1; A^ääbei Gauh. s. t. (\»;
derselbe ZDMG. XXXIII. 215; Div. Leb. 137,12; A^i
XIX. 92, 23; Bekri 215, 4; 300, 5 (u-ajI^j Name einer
Melodie Ägäni III. 97, 15) ans 1-*.=j=J »der Klopfer".
[Hier verdient bemerkt zu werden , dass der Name ^jSJi
schon vorislamisch ist. 'Adi Ibn Zeid bei Bekri 233, 13].
```


## [2026-09-14T01:24:47.394Z] TOOL CALL #25: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-14T01:24:47.400Z] TOOL RESULT

```


```


## [2026-09-14T01:24:58.099Z] TOOL CALL #26: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%86%D9%84%DB%8C%D9%BE%D8%A7",
 "prompt": "Give the full Persian entry for چلیپا: etymology, meaning, and any cited sources (Hasandust, Mo'in, Syriac/Aramaic origin)."
}
```


## [2026-09-14T01:24:59.639Z] TOOL CALL #27: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B5%D9%84%D9%8A%D8%A8",
 "prompt": "Give the Arabic entry for صليب: etymology (Aramaic/Syriac ṣlībā?), root ص ل ب, meaning. Also list any Persian section."
}
```


### [2026-09-14T01:25:04.048Z] TOOL RESULT

```
# Persian Entry: چلیپا

## Etymology
The word is "borrowed from Classical Syriac ܨܠܝܒܐ (ṣəlīḇā) or some other Aramaic form, perhaps via Sogdian." The Aramaic /ṣ/ sound typically becomes /č/ in Middle Iranian. It functions as a doublet of صلیب (salib).

## Meanings

**As a Noun:**
1. Cross or crucifix
2. Cruciform or crooked shapes, including:
   - Hair curls
   - Chalipa (a calligraphic panel)
   - Swastika
   - Chiasma (genetics term)

**As an Adjective:**
1. Cruciform or cross-like in appearance
2. Crooked or curly

## Cited Source
A 1520 poetic quotation from Selim I of the Ottoman Empire demonstrates usage: "Whoever has chosen to love curly locks of hair / Has abandoned piety and chosen the road of idolatry."

The entry notes no modern Persian lexicographers (like Hasandust or Mo'in) in its citations, relying instead on classical literary sources and the etymological connection to Semitic languages.
```


### [2026-09-14T01:25:06.323Z] TOOL RESULT

```
# صليب (Salīb) - Wiktionary Entry

## Etymology
The word صليب is **borrowed from Aramaic צְלִיבָא (ṣəlīḇā)**, which itself was borrowed from Akkadian ṣalāpum, meaning "to cross out, to pervert; to give difficulty or be crooked."

## Root
**ص ل ب** (ṣ l b) - Contains 10 related terms

## Primary Meanings (Arabic)

**Etymology 1 - Noun:**
1. "cross" (geometrical figure) - Example: Southern Cross
2. "cross/crucifix" (in Christian context) - the post for crucifixion

**Etymology 2 - Adjective & Noun:**
- Adjective: "hard, solid"
- Noun: "marrow, grease of bones"

## Derived Terms
- الصَّلِيب الأَحْمَر (Red Crescent/Red Cross)
- صَلِيبِيّ (crusader)
- صَلِيبِيَّة (crusade)

## Persian Section
The document contains **no dedicated Persian section**, though it notes Classical Persian صَلِیب (salīb) appears in the "Descendants" section, showing the word spread to Persian and subsequently to related languages like Tajik, Urdu, and Hindi.
```


## [2026-09-14T01:25:14.113Z] TOOL CALL #28: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B4%D9%84",
 "prompt": "Give the Persian entry for شل: etymologies (there may be several: شل \"lame/paralyzed\", شل \"loose\"), and their stated origins (Arabic شلل? Middle Persian? Hasandust?)."
}
```


## [2026-09-14T01:25:15.605Z] TOOL CALL #29: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/silver",
 "prompt": "Full etymology of \"silver\": Old English seolfor, Proto-Germanic *silubr-, and any mention of Akkadian sarpu / Assyrian / non-IE substrate origin."
}
```


### [2026-09-14T01:25:19.447Z] TOOL RESULT

```
# Persian شل Etymologies

The Persian entry presents four distinct etymologies:

**Etymology 1** (Adjective: "soft, limp; loose, lax")
- Origin: Incomplete/Missing. The entry notes: "This etymology is missing or incomplete" and suggests a possible Proto-Indo-European root *(s)kelh₁-* ("to dry up, wither"), but explicitly states this is uncertain.

**Etymology 2** (Noun: "thigh; thin colored leather")
- Origin: "Cognate with Mazanderani eškel" from Proto-Indo-European *skelo-*

**Etymology 3** (Noun: "spear, javelin; trident, harpoon")
- Origin: Listed as incomplete with no stated etymology provided.

**Etymology 4** (Adjective: "lame")
- Origin: "Borrowed from Arabic أشل" (cited as from Arabic أشل)

The entry does not mention Middle Persian or Hasandust as sources for any Persian شل entry.
```


### [2026-09-14T01:25:20.711Z] TOOL RESULT

```
# Etymology of "Silver"

Based on the Online Etymology Dictionary, the word "silver" has Germanic roots with uncertain ultimate origins.

## Etymology Chain

The term traces back through **Old English _seolfor_** to **Proto-Germanic _*silabur-_**, which spread across Germanic languages (Old Saxon, Old Norse, Dutch, German, etc.). 

The dictionary notes this appears to be a **Wanderwort** (loan-word) that displaced the typical Indo-European term for the metal, represented by Latin _argentum_.

## Origin Debate

The source identifies "uncertain origin" as the ultimate etymology. The entry suggests Germanic/Balto-Slavic connections and proposes possible links to old Celtic words used in Spain, though the exact donor language remains unclear. Some scholars have theorized potential Iberian substrate influence rather than simple Germanic invention.

**Notably, the provided source makes no mention of Akkadian _sarpu_ or Assyrian origins**—only Germanic, Balto-Slavic, and possibly Hispano-Celtic connections are discussed.
```


## [2026-09-14T01:25:29.111Z] TOOL CALL #30: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/silubr%C4%85",
 "prompt": "Give the full etymology discussion of Proto-Germanic *silubrą: proposed origins, mention of Akkadian ṣarpu / Assyrian ṣarpu 'refined silver', Basque, Anatolian/Hittite, substrate, and which scholars (Boutkan, Kroonen, Beekes) say what."
}
```


## [2026-09-14T01:25:31.398Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B5%D8%B1%D9%81",
 "prompt": "Give the Arabic entry for صرف: the verb صَرَفَ (ṣarafa) meaning and etymology, the noun صَرْف, and the adjective صِرْف 'pure, unmixed'. Note any Proto-Semitic root reconstruction and any mention of Akkadian ṣarāpu or refining silver."
}
```


### [2026-09-14T01:25:35.461Z] TOOL RESULT

```
# Etymology of Proto-Germanic *silubrą

## Proposed Origins

The etymology of this word for "silver" remains uncertain. The entry identifies it as "likely a Wanderwort of non-Indo-European substrate origin."

## Comparative Evidence

Multiple language families show related forms:
- **Proto-Balto-Slavic** *sirabras ("silver")
- **Basque** zilar ("silver")
- **Celtiberian** silabur ("money")
- **Ancient Greek** σίδηρος (sidēros, "iron")

## Semitic Hypothesis

A Semitic origin has been proposed, comparing:
- **Proto-Berber** *a-ẓrəf ("silver")
- **Akkadian** ṣur-pu-um and ṣa-ra-pu-um (the latter meaning "to smelt, refine")

However, the entry notes this derivation "has been rejected by some scholars as phonologically and geographically implausible."

## Displacement Theory

The word apparently replaced an earlier Proto-Germanic term (*urkundą from Proto-Indo-European *h₂ŕ̥ǵn̥tom), a displacement "connected with the adoption of more advanced metallurgical techniques and terminology."

## Scholar Attribution

The entry cites Orel, Kroonen, Mallory, Adams, and Ringe but doesn't specify individual scholar positions on particular hypotheses beyond the general rejection note.
```


### [2026-09-14T01:25:37.183Z] TOOL RESULT

```
# Arabic Entry for صرف

## Verb صَرَفَ (ṣarafa)

The entry presents this as a Form I verb with meanings including "to turn," "to divert," and "to change (money)." Additional senses include "to dismiss," "to spend," and "to embellish." In grammatical contexts, it means "to inflect (a noun) with tanween."

The article includes extensive conjugation tables for active and passive voices across multiple tenses but does not provide Proto-Semitic root reconstruction or references to Akkadian cognates.

## Noun صَرْف (ṣarf)

The noun form functions as a verbal noun from the verb above. Definitions include "diverting, averting," "expenditure," and "delivery, distribution." Notably, the entry states it refers to "the breaking down and manipulating of roots" in grammatical morphology contexts.

## Adjective صِرْف

The web page does not contain an entry for an adjective صِرْف meaning "pure, unmixed." This sense appears only in Persian and Urdu sections as borrowed from Arabic, but no standalone Arabic adjective entry is provided in the material shown.
```


## [2026-09-14T01:25:58.823Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '352,372p' AKD.txt",
 "description": "Print Zimmern context for sarpu"
}
```


### [2026-09-14T01:25:58.877Z] TOOL RESULT

```
akk.  pahani  Töpfer  :  >  aram.  pahhara  (>-  arab.  fahhär). akk.  qarasti  pta  Ton  abkneifen,   von   der  Tätigkeit  des  Töpfers  (mytho- logisch :  Menschenbildners)  :  davon  wohl  beeinflußt  hebr.  qöra.s  mlt-tit  vom Ton    abgekniffen    (geschaffen)    sein  Hi.  33,  6.  Während   akk.  eseru
(St.  jsr)  zeichnen,   usurtu  Zeichnung,    Bild,  liebi*.  jasar  bilden  (pun.  j.p- Töpfer)   wohl    urverwandt    sein    werden,    stammt    dagegen    wahrsch.    erst
1)  Wegen   des  Vorhandenseins   der  Wurzel   als   III   in  der  nicht  entlehnten  Bed. Schatten  usw.
      27      
von  dem  genannten  akk.  usurtu  :  späthebr.  si'ir  bilden,  süra  Gestalt  (un- sicher), aram.  mir  formen,  bilden,  silrta  Bild,  südarab.  mr  bilden,  Bild (und  aus  dem  Aram.  oder  Südarab.  erst  arab.  surat  Bild,  sawwara  bilden).
akk.  nappalm  Schmied  :  ^  wohl  jüd.-avam.  napprihii.  —  Viell.  be- ruht np/j  im  spez.  Sinne  des  Feueranlilasous  im  übrigen  Semit,  überhaupt erst  auf  Beeinflussung  durch  akk.  napnJju.  Zu  arab.  tilmid  Gehülfe
des  Schmieds  s.  unten  S.  29  unter  lamddu.
[Falls  aram.  qainäjd,  qrmfd,  arab.  qain  Schmied,  helu'.  wohl  im  N. pr.  Qajin  (vgl.  äth.  Jccnajil  Kunstfertiger)  mit  den  wohl  auf  akk.  qani't  Rohr, zurückgehenden  "Wörtern  für  „Lanze"  zusammenhängt  (hebr.  qajin,  arab. qancit),  würde  mittelbar  auch  qainfijd,  qain  Schmied,  erst  aus  dem  Akk. stammen.  Dagegen  ist  ein  akk.  qinai  Schmied,  das  viell.  im  Neubabyl. vorliegt,  <;;  aram.  qaindjd.]
alvk.  Mtrapu  Goldschmied  (sarpu  Silber,  siirrujnt  (MetsiYle)  schmel- zen) :  >  wohl  durchweg  der  St.  srp  in  der  Bed.  des  MetaUschmelzens, -läuterns  im  Hebr.  (auch  Phon.)  und  Aram.  (>>  im  Arab.).  akk.  Jcu-
timniu,  huüimmu  Goldschmied  (<<;  sum.  htdiiii)  :  Ob  dazu  wohl  hebr. kätem  Gold  (^  ägypt.  ktm),  auch  südarab.  Jdm,  gehört,  oder  nur  ein  zu- fälliger Gleichklang  vorliegt?
Zu  Schmelzofen  s.  unten  S.  32  unter  kdru.
akk.  Pael  nmUtl  (eig.  füllen)  einlegen,  einfassen  (von  Edelsteinen), tamlitii  Füllung,  Fassung  :  davon  wohl  beeinflußt  hebr.  millc  einfassen (mit    Edelsteinen),    milliVd,   millaim   Einfassung.  akk.  patdlm  ein-
bohren, durchbohren;  allerdings  bisher  nicht  im  techn.  Sinne  des  Ein- schneidens  zu  belegen  :  trotzdem  viell.  doch  >  hobv.  pittah  einschneiden, ■pitti'iäh  eingeschnittene  Arbeit,  jüd.-aram.  pittulid  dass.  O  viell.  arab. fatljat  Ring),  auch  phön.  und  südarab.  ^itlt.
akk.  nasdliu,  niisiikiu  wahrsch.   auch   spez.   vom  Metallgießen  ge- braucht, dann  :  >  wohl  hebr.  7insak,  phön.  iisk  in  diesem  spez.  Sinne, akk.  ;:i'pti,  sipu  Form  zum  Metallguß,  später  auch  Prägung,  Währang  : >  wohl  jüd.-aram.  zTpä,  syr.  z'ibä  Futteral.  ~  Ob  dazu  viell.  auch  aram. zepä  falsch  1  O  arab.  2^7/' falsche  Münze)  gehört?
akk.  isparu  Weber  (wahrsch.  <[  sum.  ushar,  eSbar)  :  >  'iipr  in aram.  Beischrift  zu  assyr.  Geschäftsurkunde,  syr.  'espdrd,  jüd.-aram. 'aspdrd  Flickschneider  od.  ä.  akk.  mdhisu  Weber,  maljdm  weben
1)  Urspr.  viell.  die  (negative)  Matrize  des  Prägstempels  bedeutend?
      28      
(spez.  Bed.-Bntw.  von  mahäsu  schlagen)  :  davon  beeinflußt  jüd.-aram.  mähjä "Weber,  mahä  weben  (sonst :  schlagen  =  akk.  mahrisu).
akk.  satü  weben  :  >>  wohl  hebr.  mtü  weben  (vieU.  Jes.  19,  10  vor- liegend), sati  Gewebe,  aram.  sdtä.,  'asti  weben,  sitja  Gewebeaufzug  (> wahrsch.  arab.  satä  und  sadfi).  Wie  weit  damit  etwa  auch  ägypt.  sf spinnen,  zusammenhängt,  vermag  icli  nicht  zu  beurteilen.  Zu  hebr.
mänör,  aram.  nirä  Webschaft,  sowie  natdä  Gewebe,  Webstuhl,  nawwälä Weber,  s.  unten  S.  42  unter  mru  Joch.
Zu  akk.  barämti  bunt  weben  s.   unten  S.  37.  akk.  sabsinnu
```


## [2026-09-14T01:26:00.597Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B5%D8%B1%D8%A7%D9%81",
 "prompt": "Give the Arabic entry صَرَّاف (ṣarrāf): meaning, etymology (from which verb/root), and the Persian entry صراف if present."
}
```


### [2026-09-14T01:26:05.686Z] TOOL RESULT

```
# صَرَّاف (ṣarrāf) - Arabic Entry

**Meanings:**
1. Moneychanger
2. Cashier (including "صَرَّاف آلِيّ" - ATM)
3. Banker
4. Grammarian

**Etymology:**
Derived from the Arabic verb صَرَفَ (ṣarafa), meaning "to pay out, spend, or change money." It functions as an occupational noun from this root.

**Root:** ص ر ف (ṣ r f)

---

# صراف - Persian Entry

**Meanings:**
1. Money changer
2. Banker/money dealer (historical usage)

**Etymology:**
The Persian term was borrowed from Arabic صَرَّاف (ṣarrāf), following the same occupational derivation pattern from the verb root related to currency exchange and financial transactions.
```


## [2026-09-14T01:26:19.002Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nlines=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\n')\nfor t in (35228,35077):\n    print('line',t+1)\n    for i in range(t,max(0,t-60),-1):\n        s=lines[i].strip()\n        if re.fullmatch(r'\\d{3,4}',s) or re.match(r'^\\[(pdf )?page',s):\n            print('  back marker',i+1,repr(s)); break\n    for i in range(t,min(len(lines),t+60)):\n        s=lines[i].strip()\n        if re.fullmatch(r'\\d{3,4}',s):\n            print('  fwd marker',i+1,repr(s)); break\nEOF\ngrep -n \"\\[pdf page\\|^1445$\\|^1444$\\|^1446$\" KLN_1966.txt | head",
 "description": "Find Klein page markers"
}
```


### [2026-09-14T01:26:20.349Z] TOOL RESULT

```
line 35229
  back marker 35205 '1444'
  fwd marker 35251 '1446'
line 35078
  back marker 35054 '1439'
  fwd marker 35080 '1440'
35193:1445
35205:1444
35251:1446
```


## [2026-09-14T01:26:28.113Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://www.ahdictionary.com/word/search.html?q=silver",
 "prompt": "Give the etymology line of the noun \"silver\" as printed in the American Heritage Dictionary (e.g. \"[Middle English silver, from Old English seolfor...]\"), plus any note about Akkadian."
}
```


## [2026-09-14T01:26:30.932Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://lexicon.quranic-research.net/data/14_9/018_Sd.html",
 "prompt": "From Lane's Lexicon entry for صرف (ṣ-r-f): does it list a sense 'to purify/refine silver' or 'pure, unmixed' (صِرْف), and how does it define صَرَّاف / صَيْرَفِيّ (money changer)?"
}
```


### [2026-09-14T01:26:31.778Z] TOOL RESULT

```
# Etymology of "Silver"

According to the American Heritage Dictionary, the etymology line states:

"[Middle English, from Old English _siolfor, seolfor_, probably ultimately from Akkadian _ṣarpu_, refined silver, verbal adj. of _ṣarāpu_, to smelt, refine; see **ṣrp**]"

The entry notes that the word traces back through Old English forms to an Akkadian origin meaning "refined silver," derived from a verb meaning to smelt or refine metal.
```


### [2026-09-14T01:26:34.055Z] TOOL RESULT

```
error:10000438:SSL routines:OPENSSL_internal:TLSV1_ALERT_INTERNAL_ERROR
```


## [2026-09-14T01:26:39.900Z] TOOL CALL #37: WebSearch

```json
{
 "query": "American Heritage Dictionary Semitic roots appendix \"ṣrp\" \"to smelt, refine\" Akkadian ṣarpu silver Arabic"
}
```


## [2026-09-14T01:26:40.894Z] TOOL CALL #38: WebSearch

```json
{
 "query": "Lane Lexicon صرف ṣarrāf ṣayrafī money changer \"pure, unmixed\" ṣirf"
}
```


### [2026-09-14T01:26:46.143Z] TOOL RESULT

```
Web search results for query: "American Heritage Dictionary Semitic roots appendix "ṣrp" "to smelt, refine" Akkadian ṣarpu silver Arabic"

Links: [{"title":"Proto-Semitic language - Wikipedia","url":"https://en.wikipedia.org/wiki/Proto-Semitic_language"},{"title":"roots | ahdictionary","url":"https://www.tumblr.com/ahdictionary/tagged/roots"},{"title":"Guide to the Semitic Roots Appendix","url":"https://www.ahdictionary.com/word/semguide.html"},{"title":"The American Heritage Dictionary entry: silver","url":"https://www.ahdictionary.com/word/search.html?q=silver"},{"title":"The American Heritage® Dictionary Blog — The Semitic heritage of common English words","url":"https://ahdictionary.tumblr.com/post/146364000478/the-semitic-heritage-of-common-english-words"},{"title":"Akkadian language","url":"https://en.wikipedia.org/wiki/Akkadian_language"}]

Based on the search results, I found relevant information about the Semitic roots in question:

The Proto-Semitic root *ṣrp means 'to smelt', which is part of technological terminology in Semitic languages. The American Heritage Dictionary includes an Appendix of Semitic Roots, which documents Semitic words that have influenced English vocabulary.

The search results confirm that silver probably comes ultimately from Akkadian (a language of ancient Mesopotamia, spoken in the powerful Assyrian and Babylonian empires), which aligns with the connection you're asking about between the smelting root and the concept of silver refining in Akkadian and Arabic.

The Wikipedia article on Proto-Semitic language lists *ṣrp 'to smelt' among technological terms in the Semitic language family, though the specific full entry from the American Heritage Dictionary Semitic roots appendix with all the linguistic details you mentioned wasn't directly accessible in these search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-14T01:26:48.455Z] TOOL RESULT

```
Web search results for query: "Lane Lexicon صرف ṣarrāf ṣayrafī money changer "pure, unmixed" ṣirf"

Links: [{"title":"کی تشریح | ریختہ sarf","url":"https://www.rekhta.org/urdudictionary?keyword=sarf"},{"title":"Edward William Lane, An Arabic-English Lexicon, ص, صرف","url":"http://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:2002.02.0028:root=Srf"},{"title":"صرف - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D8%B5%D8%B1%D9%81"},{"title":"صرف — 2 Meanings & Definitions in Arabic | Lane's Lexicon","url":"https://www.laneslexicon.com/word/%D8%B5%D8%B1%D9%81"},{"title":"صرف according to Arabic-English Lexicon by Edward William Lane (d. 1876)","url":"https://quranx.com/Dictionary/Lane/%D8%B5%D8%B1%D9%81"},{"title":"صرف - The Arabic Lexicon - Hawramani.com","url":"https://arabiclexicon.hawramani.com/%D8%B5%D8%B1%D9%81/"},{"title":"All dialects/MSA: change (money) | WordReference Forums","url":"https://forum.wordreference.com/threads/all-dialects-msa-change-money.2064072/"},{"title":"Language Matters | Where the word ‘shroff’ came from, and its many meanings | South China Morning Post","url":"https://www.scmp.com/magazines/post-magazine/short-reads/article/2079497/where-word-shroff-came-and-its-many-meanings"}]

Based on the search results, I found relevant information from Lane's Lexicon and related Arabic lexicographic sources:

## صِرْف (ṣirf) - "Pure, unmixed"

صِرْف means "pure, unmixed, or free from admixture; applied to wine, or beverage, as meaning unmixed". The term applies to wine, beverage, and other things like blood and phlegm, as meaning free from turbid foulnesses.

## صَرَّاف (ṣarrāf) - "Money-changer"

The Arabic صَرَّاف (ṣarrāf) means "money-changer," and this word entered Persian as ṣarrāf and Gujarati as šaraf during the period of Perso-Arabic influence in the Indian subcontinent. The English word "shroff" has been used since the early 1600s, documented in colonial writings on India, referring to local Asian bankers or money changers.

## صَرَفَ (ṣarafa) - Related verb

The verb صَرَفَ الشَّرَابَ (he did not mix the beverage or wine) relates to the concept of something being pure or unmixed.

The etymological connection between "pure/unmixed" (ṣirf) and "money-changer" (ṣarrāf) appears to relate to the practice of exchanging money and assessing the purity of coins.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-14T01:26:59.102Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN 4985-5010 ===\"; sed -n '4985,5012p' HRN.txt\necho; echo \"=== PHD cross ===\"; grep -n -i \"cross\\b\\|crucif\" PHD.txt PHD_mackenzie.txt | head -15\necho; echo \"=== NYB ===\"; grep -n -i \"cross\\b\\|crucif\" NYB_vol2_glossary.txt | head -10",
 "description": "Horn context and Pahlavi dictionaries"
}
```


### [2026-09-14T01:26:59.190Z] TOOL RESULT

```
=== HRN 4985-5010 ===
die Formen in den Varianten durcheinander gehen
(z. B. I, 107 Vers 839). Duriiyß etc. halte ich für
Composita, wohl mit Praep. ati, deren zweites Glied
ruys (No. 610) ist.
551. derniän *Arzenei', vergl. darß (No. 523), dermene'^)
^Absinth'.
i^dhar- 'halten', vergl. aw. drva- gesund'; phlv.
darwan 'Arzenei'.
LW. kurd. af/. bei. (48) darmän,
555. durüd, duröd (8ähn. I, 50 Vers 301, 170 Vers 751),
'Segenswunsch, Gebet'.
*j Vergl. auch SFgnirt^? *Frecliling*.
'-) *Banner', nicht Waife, wie Darmes t et ci-, Et. ir. II, 273 über-
Hetzt. Auch im Sähnäme heisst direfs niemals Lanze'. Mand. LW.
Nii^£»NT1 bedeutet *Kreuz* (Nöldeke, Mand. Gramm. 309 Nore i).
Greldner^s Übersetzung von aw. (jaos drafsö (y. 10, 14J durch
*ein Tropfen Milch* (Metrik, S. 153) ist schwerlich richtig (s. Ausgabe).
^) dramna (Bund), syr. LW. ^^O")*!-— 124 —
aw. droatäl- 'Geisundlieit' ') ; plilv. drüt (Men. ; AV.),
drütik courtoous' (West II, 280).
556. durüclen 'crndtcn\ Praes. diretv-em diretvldeiij durüd
'Erndto', JN^ni ^Erndte' (Is. 9, 2).
aw. vergl. dereta-, adereta- {t/ava-) ^geschnittenes,
gemähtes (sc. Korn)'; päz. drüdan erndten (PPGl.,
Men.).
kurd. dirün, dirütin erndten', dirün 'Erndte*; wa/.
drdw-am.
Das 3 in jüd.-pers. )x5l*n zwingt direivem zu lesen

=== PHD cross ===
PHD.txt:77:Verbs are quoted in the infinitive form, followed by the present stem, except when either of these is not certainly attested. Cross references are made where necessary.
PHD.txt:298:čāšt [ой | N ~] lunch, meal. 1~ag [-k'] food. &а$їар [c'štk'] doctrine. čāštan, čāš- [c?s-tn'] teach. ~išn: teaching. čatrang [cting | (Ar. šatranj)] chess. *taw(la)gan [cwpk'n!! | Ar. sawlajan, N čaugān] (curved) polo-stick ; polo. CaxSágih [ch kyh] (sense of) taste. čaxšišn [chsfn! | M, J схі, N ¿aš-] taste, flavour. 148 [ME < A mh | M cy, N či] what, which. ~ ray: for what, why. ~ih: quiddity, essence. tčē [ME, v. 166] for, because, since, as, that. &ë-ëwënag [ME ^ dwynk!] how. ~ith : circumstances. čegām-iz [су?т-с | M cyg^myc], —-6(w): a little; whatever. Cegámag [cyk”mk! | N &(ag)áma] song, snatch. €éh- , —išn, v. idan. *téhag [cyhk'] grief. čehel [40 | N chil] forty. Céh-widarag [cyhwtlg] = činwad puhl. čēlān [cy”x! | = M, N ~] dagger. ~gar [-kl, -gl | N ~] swordsmith. Cér [cyl | M cyr, N —] victorious, triumphant, brave. —Ih: bravery. Cérihistan, Cérih- [cylyh-stn'] triumph, be victorious. īčīdan, čīn- [cytn', cyn- | M cyydn, cyn-, N ~] gather, pile up. ~išn: gathering. *čīdan, čēh- [cytn', cyh- | M cy-] mourn, lament, grieve. ~i8n : lamentation. ~i$nig¢ : mournful. ihr [cyhl | M cyhr, № ~] form, shape, appearance, face. žčihr(aģ) [cyhl(k') | M сулу, P -g, № ~] seed, origin; nature, essence. Cihrénidan, čihrēn- (cyhlyn-ytn'] form. Cihrig [cyhlyk'] natural. čihr-šnāsīh [суйру] physics. čim [c(y)m | M сут, N ~] reason, cause, purpose, meaning. ~ (ray): why? Cim-gó6wáàgih [сут gwh’kyh] logic. čimīģ [cymyk!] purposeful. čīn-, ~i8n, v. idan. čīnag [cynk! | P cyng, N ~a] grain, bait. Cinàr [су | N ~] oriental plane tree. činwad [cynw(p)t'], ~ puhl: the ‘divider bridge’ which separates the souls of the righteous dead, who cross, from those of the wicked, who fall off.
PHD.txt:308:dahigān [dhywk’n' | N dihgān] countryman, farmer. dahliz [d^hlyc | (M dhryz), N ~] portico. dahm [d?hm] virtuous, pious; a full member of the Mazdean community, initiate. dahom [hwm | M dhwm, N ~] tenth. dalman [d”/mn' | N dál(man)] lammergeyer, eagle. dam- , ~išn, v. daftan. īdām [d”m | = M] creature, creation. здат [Pm | = M, N ~] tame animal. здат [d’m | P d’mg, N ~] net, snare, trap. dāmād [d?r?t! | M 424, N ~] bridegroom, son-in-law. ~ih: condition of a bridegroom, son-in-law. daménag [dmynk'] fan. damidan [dmytn'] = daftan. dān-, —išn, v. dānistan. -dàn [-d’n' | = M, N ~] suffix, -holder, -container. dàn(ag) [d”x(k)! | N ~a] seed, grain. Н dānāg [4>рА! | М dwg, N dana] knowing, wise. ША zn kh ~ih: knowledge, wisdom. ar dandàn [KK A < А kk’; dnd’n' | = M, N ~] tooth. dānistan, dān- [YDOYTWN-stn' < A У yd‘; d’n-stn' | M d^n-ystn, N ~] know. ~ign: knowledge. ~i8ndmand [- отпа) knowing. dar [BBA < A bb’; dl | M dr, N =] door; palace; chapter, subject. dar [d?] | M d@’r-, N ~] tree, gallows; wood. dar-, -išn, v. dāštan. -dār [-d'/| M -d’r, N ~] suffix, -holder, -keeper. Р darāy [dPg | J ~, N darāy] bell. *darak [dlk'] section, paragraph. darband [B B Abnd | N ~] gate. darbās [dips] palace. dard [dit! | M drd, N ~] pain. ~отапа [отла | M -wmnd, N ~mand] ill, suffering. dārēn [d'/yn! | М drwyn] wooden. darģāh [dig’s | N ~] doorway. dargardih [d*/krtyh | M d’rgyrdyh] crucifixion. dar-handarzbed [BB A-, dl-hndlcpt'] chamberlain. darigbed [dlykpt'] palace superintendent. *darmag [d?/mk!'] fine, delicate. darmān [dim?n! | M drmn, N ~] remedy, medicine. darridan, darr- [SDKWN-tn! < A V sdg; dl-ytn! | N <] split, tear. dàrüg [d"Iwk! | М drwg, N dari] drug, medicament. dār-wāzīg [Tlw cyk! | N dár-bàz] (pole-)acrobat. darz [dlc | N ~] seam. ~ig [-уА! | N darzi] tailor.
PHD.txt:593:tan-bahr [żn'Þ’ hl] physique. tand [tnd | = P] faint, languishing. ~ih: faintness, langour. | tan-drust [tn'drw(y)st! | N ~] healthy, whole. ~ih: health. tang [ing | = M, N ~] narrow, tight. ~ih: narrowness; distress. tanig [tn'yk! | N tani] bodily, corporal. tanigard(ig) [tnykrt(yk)! | M inygyrd] corporeal. ` tanīhā [tn'y/? | M tnyP?, N tanha] alone. tanómand [tn wmnd | N ~] corporeal. “АҺ: corporeality. tan-tdhmag [tn'twhmk'] (sap) of plants. tanuk [tnwk! | N ~] thin, shallow, tanür [tnw] | M tnwr, N ~] oven. tar [LCDr! < A l-sd; tl | M tr] over, through, across. ~ kardan, ~ menidan: abuse, despise. -tar [-z# | (M -dr), N ~] suffix forming comparative adjectives. tar [2] | M гу] darkness. tarāzēnīdan, tarāzēn- [tcyn-ytn!] weigh. tarázüg [tPcwk! | (P tPzwg), N tarazü] balance, scales; astr. Libra. targ [tlg | N ~] helmet. tarģumān [tigm?n! | M trgwmn] interpreter. tarig/k [PIyk! | M гуур, N tárik!] dark. ~th: darkness. tarist [¢/st'] = tar. tar-mānīh [t/m’nyh] perversity. tar-menišn [tImynin! | N tarmanist] perverse; contemptuous. 7h : perversity; contempt. tarr [t/, LC Dr (in error, v. tar) | N —] moist, fresh. ~ag [tik! | N ~a] vegetable. tars [2/5 | M trs, N ~] fear, respect. tarság [ts k! | M trs’g, N tarsā] Christian. tarsāģāh [15(?)/?5] respectful, reverent. ~ih: respect, reverence. tarsidan, tars- [tls-ytn' | (M tyrs??dn), N ~] fear, be afraid. tarwénidan, tarwēn- [t/zvyn-ytn! | M trw-] overcome, conquer. tas [25 | N ~] die (for gaming). tasum [tswm | = M] fourth. tāšīdan, tāš- [O i-ytn!'] cut, cleave; create. taSkanag [tšknk!] under-shirt. tašt [tšt' | N ~] bowl. tāšt [021] *certainty. ~ig [-yk'] certain. tāwān [1?(d)w’n' | N ~] compensation, obligation. taxl [t?% | (M thr), P txl, N talx] bitter.
PHD.txt:651:wénig [wynyk! | M wynyg, N bini] nose. wénO£ [wynwk' | N bunü] lentil. wēš [zoy£ | = M, N béf] more. wé&ag [wysR! | N beta] thicket, wood. --estün [-st?n'] woodland. ~ig [-yk'] silvan. wēwag [wdpk! | N béwa] widow. 1wéxtan, wez- [NSSHWN-tn! < А V nsh; wyhtn', wyc- | P wyxt-, N bextan, béz-] sift, select, choose, separate, cleanse, purify, winnow. ~išn: selection. *wēxtan, wēz- [wyhtn!, wyc-] swing, brandish, throw, pour out. Wīdadafš [wydtpš = Av. wīdašafšū-| the south-western continent of the earth. widang [wtng | P wdng] trouble, distress, constraint. widār [xt' | N gudár] passage, entrance. widarag [wtlg | M wdr, N guàar] path, passage. widardan, wider- [wtitn!, wt(y)l- | M wd(y)r-, N guóar-] pass (by, away), cross, die. : ~išn(īh): passage, crossing, death. ~i$nig : transient. widārdan, widār- [xwt?/-tn! | M wyd’r-, N guóárdan] let pass, transport; endure, suffer. widārīdan [w?lytn'] = widardan. widaštan [wtstn' | N gušaštan] = widardan. widāxtan, widāz- [wt’hin', wtc- | (P wd’c-), N gudaxtan, gudāz-| melt, dissolve. widāzīhistan, widazih- [wt’cyh-stn'] be melted, dissolved. wider- , -išn(-īģ, -ih), v. widardan. widerān [wt(y)?n! | N guóarán) transient, dying. widest [zot(y)st! | N bidast] (hand) span (9 in.). ~ig [-yk'] span-sized, midget. widimās [wtym’s | (M wyd’m’s)] wonder, miracle. ~ig [-уА!] wonderful. ~ih: miracle. widimušt [wtymust | M wd(y)mwšt] astonished. ~ih: astonishment. *widwar [wytwl] contented, resigned, consoled. ~ih: contentment, resignation, consolation. wiftag [wyptk'] passive sodomite. wigrad [zogPt! | N bīdār] awake, alert. wigradan, wigras- [zog tn, wgl’s- | M wygr'd, wygr’s-] awaken, rouse. ~i$n(ih): awakening. wih-, v. wistan. wihan(ag) [zh?n(k)', (b-) | M wl?ng, N bahāna] cause, reason. wihēz- [wyhyc- | M twhyz-] move, progress. wihéz(ag) [wyhyc(k')] movement, progression.
PHD.txt:723:across tar, tarist,
PHD.txt:1444:cross widardan, (widaštan).
PHD.txt:1449:crucifixion dārgardīh.
PHD_mackenzie.txt:363:stem, except when either of these is not certainly attested. Cross
PHD_mackenzie.txt:1795:       souls of the righteous dead, who cross, from those of the wicked, who
PHD_mackenzie.txt:1891:dargardih [d'lkrtyh I M d'rgyrdyh] crucifixion.
PHD_mackenzie.txt:4922:tar [LCDr l < A l-~d; tll M tr] over, through, across.
PHD_mackenzie.txt:5345:   cross, die.
PHD_mackenzie.txt:5916:across tar, tarist.                       agitati01I ayardenisn.
PHD_mackenzie.txt:6312:cross widardan. (widastan).                dare ayaridan.

=== NYB ===
1192:dar [d?l] tree 3319. 42?! ; pat ~ apar kartan to crucify 208. — Av. (738) dāru-, dru-; MPrs adj. d’rwyn; d’r-gyrdyyh ‘crucifix- ion’ (S); MPrth d’lwg (v. dari), @rwbdg ‘crucified’ (S; a much discussed w., v. Verbum 223 sq.; JA 228, 1936, 197). NP ddr "wood, gibbet'; v. also dari.
2237:ikartan [krtn'; klty; ‘BYDWN-t'] kun- [ BYDWN-;forms v. I, 179; pres. 3d p.sg. kwnd: read kund] to make, to do, to per- form, to exercise, to commit, to cause, to bring about; to manufacture, to construct (hac ‘of’ a material); — forms active deriva- tive vbs. a) from v.ns. in -išn, e.g. āsāyišn ^ to repose, azbäyisn ~ to invoke; gar- zišn, īzišn, koxšišn, nikērišn, pursišn, za- nisn ete.ete. ~ ; b) from other nouns: čfrin, amoxtareh, appar, hampursakeh, tak, varz ete. ete. —, v. the resp. ws.; — with a pred. adj., e.g. 73. 34" etc.; girt kart = girt kartak (g. v.); vat-kart v. vat; or a pred. subst., e.g. api-$ ... bitaxš kunom 2510-11; . with kart as its cognate obj. P2:6-7. 8 [read (TB =) nev kart" kunän that I may do good deeds]. — With prev.: andar 6 kar ~, v. kar; api-§ Mānušcihr andar 6 Patisz"argar kart he brought M. (as a captive) to P. 1164-5, cf Bd A p. 2315-5; — apüc ~ to repel 42*3 gl.; to reflect 1125; — pat ddr apar ~ to crucify a p. 208; — bé ~ to remove 65; — berön asmän kunst he wil turn them out of heaven 10318; — frāc ~ to send forth 161!5; to bring forth, to produce 48?9; to attempt 81?!. — NB: man kart HWH-wm 374-5 for man kart-om by me it was done, v.s. v. h- and -m. — *BYDWN.x,ot' = kunät 5314, cf BY- DWN-x,-yd = 2nd p.sg.kunēKnS VII, 11. — Av. (444 sqq.) tkar-, pres.ko ranu-; OP kar- kunav-; MPrth kyrdn kr-; MPrs kyrdn kwn-; Paz. NP kardan kun-; cf s.v. hangirtikeh.
3410:sat-0š [stwš] the state of one just deceased ; theological term expressing the state of the deceased from the moment his life (jan) expires, the soul (ruvän) remaining at the head of the corpse, until the morning of the fourth day when the ruvän leaves this world and, after having been exam- ined, passes across the Cinvat bridge to the other world, “the three-nights-inter- val” (between the existence in this world and the entrance into the beyond) 6411, described 726-7615. — The literal mean- ing of this term was lost early, as shown by the very varying Paz. trans- literations: saduš, sadiš, sadis(a), sediš, sadaš etc. (Mx; Tavadia, Šnš 12). An- klesaria gives in his ed. of Mx (not yet published) sēdēš, which Tavadia (himself reading the Phl form satus) seems to reject. At all events sēdēš is an attempt to harmonize the Paz. reading with the Skr. v. trirdtra, -rin, rendering the termino-
3651:škuft [Skwpt'] strange, surprising 724; stupefied 11%, - MPrth ‘sky/t ‘wonderful, amazing, immense(ly), very’; NP šikijt ‘anything wonderful’, šikuft ‘a prodigy, magnificence’, šigift, Sıguft ‘wonder, aston- ishment’. The etymological relation be- tween skapta- and *skupta-, *skipta- is not clear, but their meanings cross.
4240:vitartan [wtltn'], viturtan [wtwltn'], vi- taštan [wtštn'], vitir- [wtyl-] to pass: andar dašt bē vitart passed over the plain 318; pat kustak + deh vitart passed outside the village 619-17; to pass by 7!1.15.22; bē vitast drove ahead 71’; to cross a bridge 7225.27; to go through a stream 101%. 10323; kë vitīrēndv the passers-by 12815; — pt. vitart, viturt deceased: vitart coll. the deceased 837. 8413; viturtān martūmān 10517. — Av. (640) vi-tar- = OP; MPrth w(y)drdn w(y)dr- (S, MHC); MPrs pres. wdyr- (S); Ps. pt. wilty, pres. wtyl-, wtl-; Paz. vadardan vadirdan, pres. vadar-, va- der-, vadir-; NP guöastan guóar-. Verbum 206, Ghilain 57.
4245:to Z. through the line of his maternal grandmother 3619-11, cf 3817-18, — 2. intens. of vitartan: vitartan % Cinvat puhl to cross the Ch. bridge 64!?; the arrow ditikar sok bé vitärt pierced through to the other side 371, pat pušt be vitārēt (pres. hist.) pierced through and came out through the back 292-3, pat dil be vitārēt penetrated into the heart 2521-22, — MPrthPrs wyd’rdn w(y)d’r-; MPrs also pt. wd’$, Verbum 192; NP guöärdan or guöästan, guóür-.
```


## [2026-09-14T01:27:11.437Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY\necho \"=== ARY چلیپا/صلیب ===\"; grep -n \"چلیپا\\|صلیب\\|صراف\\|شلیدن\" ARY_pages.txt | head -20\necho \"=== ARY latin index ===\"; grep -n -i \"CALIPA\\|SALIB\\|SARRAF\\|SHAL\\b\\|ŠAL\" ARY_latin_index_pages.txt | head -20",
 "description": "grep Aryanpur"
}
```


### [2026-09-14T01:27:11.515Z] TOOL RESULT

```
=== ARY چلیپا/صلیب ===
=== ARY latin index ===
305:Sa sean Beda ist IS Be Sle 3m slo shal ( Gdle) whadar Gejly col dale
652:: col 8 lle shew lal shal eels
5352:TeKO LITHUANIAN) «i p) TAGHT, TASHAL, Ossett) pis)"
5566:TRAP, TRPKY SLOVAK) 51 shal TRIV, TRIW — -{AFGHANI) (7-4) gli!
6227:ZHUVAT (SLOVAK) 5 shal TYGGVA OLD NORSE) oS 393
8335:poié POLISH) gle DAVASHAL —«(AFGHANT) (3-4) gui!
11773:KASH, KASHAL, KASHALE (oy
13578:“shal (MAT, MATER) "31" at aly j} aoa Golhaat ta sdb Sar yp old glasjly ») badly
```


## [2026-09-14T01:27:13.414Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nd=open('SOD_pages.txt',encoding='utf-8',errors='replace').read().split('\\n')\nimport re\n# find standalone page numbers near line 12879\nfor i in range(12700,12960):\n    s=d[i].strip()\n    if re.fullmatch(r'1[0-9]{2}',s):\n        print(i+1, repr(s))\nEOF",
 "description": "Find SOD printed page numbers near entry 3202"
}
```


### [2026-09-14T01:27:14.472Z] TOOL RESULT

```
12823 '126'
12896 '127'
```


## [2026-09-14T01:27:21.811Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LKT sarraf/shroff/silber ===\"; grep -n -i \"sarraf\\|sarrāf\\|schroff\\|sarpu\\|Silber\" LKT.txt | head -20\necho; echo \"=== HJB shroff ===\"; grep -n -i \"SHROFF\" HJB.txt | head -10\necho; echo \"=== TAD صراف ===\"; grep -n \"صراف\\|صرف\" TAD_pages.txt | head -10",
 "description": "Lokotsch, Hobson-Jobson, Unaysi"
}
```


### [2026-09-14T01:27:21.904Z] TOOL RESULT

```
=== LKT sarraf/shroff/silber ===
244:[Wörtlich  „Vater  der  Zecken",  die  ar. kiräd,  plr.  kirdän  heißen].  Der  rein weifae  'Kuhreiher',  Ardea  bubuleus  Sa- vigny,  ein  afrikanischer  Vogel  [die Schreibung  aboogerdan  bei  ML  36  wie schon  vorher  bei  Körting,  Lateinisch- romanisches Wörterbuch.  3.  Aufl.  Pader- born 1907,  s.  V.  ist  englisch].  Durch volksetymologische  Neugestaltung  hier- aus vielleicht  frz.  bwuf-garde,  garde- bcfuf  'eine  Art  Silberreiher'.  [FASS in  RomForsch  III,  488.  KURYLOWICZ in  Rocznik  Orientalistyczny.  Tom  II. Lwöw  1925.    S.  252.
369:'Strick'.  Davon  it.  alamari  plr.  'Rock- verschnürungen',  sp.  alamar  'mit  Schnü- ren verzierte  Knöpfe  zum  Schmucke od.  zum  Gebrauch'  [Dicc  Gast  101a], pg.  alnmar  'Schnüre  od.  Spangen  aus Seiden-,  Gold-  od.  Silberfäden  zur  Zierde am  Anzüge'  [Gonstancio  Dicc  42  b].  — Die  Etymologie  ist  m.  E.  zweifelhaft; vielleicht  ist  besser  liamäla  als  Grdwt. zu  nehmen ;  das  vulg.  ar.  Wort  'amära selbst  aus  herber,  amrär  'Schnur'.  [ML 397.  DE  54/6.  Caix,  Studi  di  etimologia italiana  e  romanza.  Firenze  1878. S.  145.
1187:'Gruppe;  Paket  Gold-  oder  Silbergeld' [Kelekian  Kämüs  488  a];  hieraus  rum. ciochinä  'Sattelknopf.  —  Löbel  EITAP 32  fragt  nachdem  Bedeutuugszusammen- hang  zwischen  rum.  ciochinä  und  tk. cykyn.  Dieses  letztere  war  das  Geld, das  die  Großen  der  Hohen  Pforte  ver- teilten, wenn  bei  einer  Feuersbrunst die  Feuerwehrleute  angespornt  werden sollten;  es  war  also  weggeworfenes  Geld, das  man  ebenso  gut  unnütz  an  den Haken  oder  wie  wir  im  Deutschen  zu sagen  pflegen  ,an  den  Nagel  hängen" konnte.  Im  Rumänischen  sagt  man nun  genau  so  a  pnne  la  ciochinä  im Sinne  von  'beiseite  werfen'.  Der  Zu- sammenhang mit  der  Bedeutung  'Schnal- le, Haken,  Sattelknopf  wird  so  ziemlich einleuchtend.
1251:'Stempel,  Siegel'  [vom  Stamme  tarn, dam  'Tropfen,  tröpfeln'  Vämbery  Tkt EtWb  S.  167,  Nr.  180;  aus  'Tropfen', nämlich  'zur  Bekräftigung  oder  Unter- schrift eines  gegenseitigen  Vertrages  auf das  Schriftstück  fallen  gelassener  Tropfen' wurde  'Siegel';  der  Sinn  des  tk.  Wortes 'Stammesabzeichen,  Brandzeichen  auf dem  Arme  eines  Verurteilten,  Kontroll- zeichen  auf  Gold,  Silber,  Wagen'  ent- spricht genau  dem  ar.  wasm,  d.  h. 'Zeichen,  das  von  den  Beduinen  den Kamelen  eingebrannt  wird  und  durch welches  sich  die  einzelnen  Stämme  und Unterabteilungen  voneinander  untei- scheiden'l;  rum.  danga  'Brandzeichen, Stempel';  rliss.  tamga  'Stempel,  Waren- zoir,  tamoznja  'Zollamt',  bulg.  damga 'Stempel,  Zeichen',  serb.  danga,  dagma 'Zeichen'.  Wahrscheinlicli  gehört  hier- hin auch  russ.  den'gi  'Geld'  [vgl.  C.  M. Fraehn,  De  origine  vocahuli  Rossici den'gi.  Gasani  s.  a.  (1815)].  [Gorjajew 88  und  360.  Mikl  SlEtWb  39  b.  Bern SlEtWb  178.
1348:'Eine  Silbermünze  von  wechselndem Werte'  [vgl.  dazu  MORITZ  in  AbhPr- AW  Berlin  1918,  Nr.  4,  S.  30,  Anm.  2, wo  das  Abwärtsgleiten  des  Dirhams  für die  ersten  tausend  Jahre  der  Hedschra bis  auf  den  50.  Teil  seines  ursprünglichen Wertes  nachgewiesen  wird],  vulgär  aus- gesprochen dirhem  [das  ar.  Wort  kommt selbst  aus  gr.  bpaxMn  ZDMG  LI,  297, das  auf  bpdTTU),  bpäTTOiuai  zurückgeführt wird  u.  soviel  wie  'eine  Handvoll',  sc. von  Spießen,  bedeutet];  hieraus  frz. dirhem,  sp.  adereme,  adarme,  pg.  adarme 'Gewicht  od.  Münze',  pg.  auch  figürlich 'geringfügige  Sache'  [Gonstancio  Dice 21b];  über  das  tk.  drem  wurde  rum. dram  'ein  Quentchen,  V^oo  einer  Okka [s.  hier  Nr.  1.590]',  also  in  der  Walachei 3,370  g,  in  der  Moldau  3,229  g.  [DE 41.    Devic  DEt  103.
1465:Plrl.  fulüs  [aus  gr.  (pöUi;  ZDMG  XXI, 672/674]  'kleine Silber-  od.  Kupfermünze' ; hieraus  sp.  foluz,  pg.  fuluz  [Constancio
1536:'Franke'  [aus  diesem  oder  einem  an- deren europäischen  Worte  entlehnt]; hierzu  frenk  ileti  [aus  ar.  Hlla  'Krank- heit'] eigentlich  'fränkische  Krankheit', d.  h.  Syphilis;  hieraus  rum.  franpa, sfranjia  'dass.'.  —  Tk.  frengi  seraser ■'Brokat,  Seide  mit  Gold  und  Silber  durch- wirkt' ergibt  rum.  fretighie  'Brokat'. E.  LlTTiVIANN  in  Festschrift  für  Kuhn. München  1916.  S.  241/242.
2166:'Eichmaß,  Feingehalt  des  Goldes  oder Silbers,  Pendel  zum  Regulieren  einer LTir',  ebenso  tk.  ajar ;  hieraus  rum.  aiar 'Eichmaß,  Regulator'.
2294:'Zwanzig',  mit  dem  Suffix  -Hk  zur  Be- zeichnung eines  Geldstücks  jirnii-lik 'Münze  von  20  Para  oder  20  tk.  Pfund'; hieraus  rum.  irmilic  'alte  Silbermünze von  20  Piastern'.
2606:Ein  Silber-  oder  Goldgewicht  von  '/400 Tulä;  über  tamul.  oder  konkani  käsu wurde  zunächst  pg.  caixa  'Münze  von 3  Reis'  [Constancio  Dicc  204  c]  und hieraus  engl,  cash,  Bezeichnung  für  jede kleine  Münze  in  verschiedenen  Teilen Ostasiens;  in  China  ist  seit  mehr  als zwei  Jahrtausenden  der  runde,  mit  einer zentralen  viereckigen  Durchbohrung  ver- sehene Käsch  typisch.  Über  seine  Ge- schichte vgl.  MÜLLER  in  MSOS  XXH, ostasiat.  Abtlg.  S.  10  ff.  Hobson-Jobson 167/168.
2978:1275.  Tk.  kyl.abdan: 'Flittergold'  [Kelekian  Kämüs  967 :  Metall- faden aus  Silber  und  Kupfer  als  Nach- ahmung eines  Goldfadens];  hieraus  bulg. kalahadan,  serb.  klobodan  'dass.'.
3473:'Wachs',  ebenso  tk.  niiim  'dass.,  Kerze', hieraus  serb.  nium  'Kerze',  [über  tk. tnumgi/]  rum.  mungiü,  munger  'Kerzen- fabrikaiit',  m!<H.9?/7f 'Keizenfabrik',  kat. sp.  nioniia  'Pech  und  Asphalt',  apg. muminha  'Mischung  vou  Pech  und Quecksilber',  bes.  die  harzige  Masse,  die aus  den  der  Sonne  ausgesetzten  Mumien floß  und  als  heilkräftig  galt.  —  Ar.
3943:1730.  Sskr.  rüpya: 'Verarbeitetes  Silber',  ebenso  rüpiya; hieraus  engl,  rupee,  frz.  roiipie,  dtsch. Rupie,  die  Grundmünze  des  angloind. Münzsystems,  schon  während  der  mu- liammedanischen  Herrschaft  gebräuch- lich. Von  demselben  Grundwoit  kommt russ.  ruhl' ,  engl,  roidtle,  dtsch.  Hubel. [Hobson-Jobson  774/776.  Gorjajew  303.
4215:[Letzten  Endes  von  ass.  sarpii  'Silber', eigentlich  'das  Geläuterte'  vom  Vb' surrupu  'läutern,  schmelzen',  hieraus  syr. sarräpä,  ar.  sairaf  'Geldwechsler',  vgl. ZAkkFW  59]  'Wechsler',  tk.  ebenso; hieraus  rum.  zaraf  'Geldwechsler',  za- raflic,  zäräße  'Wechselstube';  serb. saraf,  bulg.  sarafin  'Wechsler'.
4257:Ein  Gewicht,  ungefähr  19,37  g  [vom  Vb. säkal  'wägen';  vgl.  assyr.  siklu,  hier  Nr. 1456  a],  und  später  ein  Geldstück  im Gewichte  von  14,55  g  Silber  und  im Werte  von  2,50  M;  hieraus  in  gleicher Bedeutung  engl  shekel.  dtsch.  Sekel  und unter  Einfluß  von  gr.  oikXoc,  lat.  sicltis, auch  ndl.  sikhel.
4384:'Gemisch  von  arseniger  Säure  und  Queck- silber, Arsenik'  [SANGUINETTI  in  JAs 1866,  I;  Adj.  zu  Sulaiman,  N.  pr.,  =
4429:'Filigran,  Gold- oder  Silberdraht' ;  hier- aus rum.  s:\rma  'Drnht,  bes.  aus  Gold oder  Silber'.
4607:2Ü.Ö0.  Ar.  taiisija: Subst.  Infin.  des  Vbs.  wasä  II  'färben, schönmachen',  also  'Färbung';  hieraus sp.  ataujia,  pg.  atauxia,  fnuxia.  mfrz. tauchie,  it.  tausia  'Damaszierung  mit Gold  oder  Silber',  dtsch.  Vb.  tauschieren. [DE  214/215.  Eguilaz  .306.  ML  8602  a.
4727:schon  bei  Avicenna  aufgeführt  wird [wahrscheinlich  selbst  aus  dem  Pers.J, vulg.-ar.  turhid;  liieraus  zur  Bezeichnung eines  Purgiermittels  mlat.  turpethum, kat.  sp.  pg.  turbit,  sp.  tiirbiche,  frz.  tur- bith]  ndl.  turbith,  engl,  furbüh,  turpeth. Frz.  turbith  rnineral  ist  ein  Präparat aus  Quecksilbersulfat  mit  gleicher  Wir- kung. [DE  351.  Pevic  DEt  2^22.  Eguilaz .509.  Dozy  Oost  9(i.  Lammens  Rem 241/24-^.
4800:2143.  Ar.  'utärid: 'Quecksilber',  ebenso  tk.  ntaryd  ;  hieraus russ.  rtut',  klruss.  ortut',  rtut',  poln.  rt^6, trt^c,  cech.  rtut  'dass.'.    [Gorjajew  302. Mikl  SlEtWb  285a.

=== HJB shroff ===
14318:1567.—"  .  .  .  furthermore  that  no  infidel shall  serve  as  scrivener,  shroff  {xarrafo) moeadam  {vioead(U>\  naique  (see  NAIK), peon  (pido)  parpatrim  (see  PABBUTTT), collector  of  dues,  ewTeffidor,  interpreter, procurator  or  solicitor  in  court,  nor  in  any other  office  or  charge  in  which  he  can  in any  way  hold  authority  over  Christians." — Decree  ofOit  Sacred  Council  of  Qoa^  Dec.  27. In  Arch.  Port.  OrinU.  fascic.  4.
15596:1799. — "  I  have  written  to  Campbell  a  long letter  about  the  nerxick  of  exchange,  in which  I  have  endeavoured  to  explain  the principles  of  the  whole  system  of  shroffing (see  SnSOFF).  .  .    "—Wellitigton,  i.  56.
20065:SHROFF.
20089:SHROFF,
20096:1585. — *^This  present  year,  because  only two  ships  came  to  Goa,  (the  reals)  have  sold at  12  per  cent,  of  Xarafaggio  (shroffage), as  this  commission  is  called,  from  the  word Zaraifo,  which  is  the  title  of  the  banker." —Saasetti,  in  De  GubenuUis,  Storia,  p.  203.
20102:1750. — " .  .  .  the  Irruption  of  the  Mo- rattoes  into  Camatica,  was  another  event that  brought  several  eminent  Shroffli  and wealthy  Merchants  into  our  Town ;  inso- much, that  I  may  say,  there  was  hardly  a Shroff  of  any  Note^  in  the  Moaul  empire but  had  a  House  in  it ;  in  a  word,  Maarass was  become  the  Admiration  of  all  the  Coun- try People,  and  the  Envy  of  all  our  European
20104:1809.—"  I  had  the  satisfaction  off  beaziw the  Court  order  them  (t.e.  Qcno.  MAitin^ executors)  to  pa/  two  lacs  and  a  half  to the  plaintiff,  a  shroff  of  Lncknow."— Zd. VaUnlia,  i.  243.

=== TAD صراف ===
587:      ‫حشب مرأدفه مصرف‬       ‫معئاه ‪ 5‬الااصل مول من‬   ‫‪ 5-5‬سمدم ايطالى ‪125‬‬
1081:             ‫ية مأخوذة مندق أي لوح وعريبها المصراع والصرفق‬
1878:       ‫اللغة وقراثها وهو مشتق من‪ +012‬كدب مرادكفهتاب الصرف واانحو‬
2451:                           ‫ونطروي معتاه بدل التقود وصرفبا‬         ‫‪00‬‬
```


## [2026-09-14T01:27:24.423Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B4%D9%84%D9%84",
 "prompt": "Arabic شلل / شَلَّ (šalla): verb meaning 'to be paralyzed / wither (of the hand)', the adjective أَشَلّ (ašall), root ش ل ل, and any etymology or Proto-Semitic reconstruction. Also list descendants (Persian شل?)."
}
```


### [2026-09-14T01:27:25.489Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-14T01:27:36.718Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LKT 4205-4220 ===\"; sed -n '4203,4220p' LKT.txt\necho; echo \"=== HJB 20085-20100 ===\"; sed -n '20085,20100p' HJB.txt",
 "description": "Lokotsch sarraf entry and Hobson-Jobson shroff"
}
```


### [2026-09-14T01:27:36.799Z] TOOL RESULT

```
=== LKT 4205-4220 ===
(b)  Bezeichnung  eines  Windes,  heut- zutage 'Südwind'  Mrklje;  hieraus  it. scirocco,  siz.  sciloccu,  sp.  siroco,  jaloque, pg.  xaroco,  frz.  siroc;  engl.  ndl.  sirocco, dtscb.  Sirokko  'heißer  Südwestwind'. [Aus  den  europäischen  Formen  mit  l haben  die  Araber  ihr  saJük,  saläk  zurück- genommen).
(c)  Auf  das  ar.  Grundwort  sarki  geht auch  sicherlich  der  aus  byzantinischen Quellen  bekannte  Name  eines  zwischen Ägypten  und  Syrien  zeltenden  Beduinen- stammes lapaKfivoi  zurück;  hieraus  zur Bezeichnung  aller  islamischen  Völker des  Orients  lat.  Saraceni,  Adj.  saracenus 'sarazenisch',  it.  saracino  'Stechpuppe oder  hölzerner  Mann,  nach  dem  die Reiter  mit  der  Lanze  stießen',  saracenüo 'sarazenisch',  saracwiffre 'seil  warz  werden (Weintraube)',  hz.  sarrasin  'Buchweizen' [nach  de  Candolle  im  XV.  Jahrhundert aus  der  Tartarei  und  Rufsland  nach Mittel-  und  Westeuropa  eingeführt:  Poly- gonum  fagopyrum],  sarassine  'Gatter', Sarrazin  im  Argot  der  Pariser  Setzer 'Streikbrecher',  sp.  sarraccino  'Buch- weizen', überall  in  der  Bedeutung  'Sa-
10*
Tk.  sarma]^.]
148
razene,  sarazenisch';  engl,  saroccn,  sa- racenie,  dtsch.  Sarazene,  sarazenisch. [Andere  Ableitungen  von  ar.  sarräg, das  aber  nicht  'Reiter',  sondern  'Sattler' heißt,  oder  von  särikln  'Diebe'  sind nicht  annehmbar,  vgl.  Lettre  de  M.  Silv. de  Sacy  au  rödacteur  du  Moniteur  sur l'etymologie  du  nom  des  Assassins.  Im Moniteur,'  an  1809,  no.  359,  pg.  5/6,] [DE  241/243.  Devic  DEt  72.  Lammens Rem.  57/58.    Eguilaz  348.    ML  7595.
1857.  Tk.  sarmak; 'Einwickeln',  subst.  Infin.  sarma  'das Eingewickelte' ;  hieraus  rum.  sarma  'mit Reis   und   Hackfleisch    gefüllte  Kraut- klöße'.
1858.  Pers.  särpänäk:
[Zu  sär  'Kopf,  s.  liier  Nr.  1841J  'Weib- licher Kopfschmuck';  hieraus  russ.  eer- pjanka  'undichte  Leinwand,  Fliegen- tuch, dünnes  Gewebe',  poln.  s(i)erpianka dass.'.    [Gorjajew  318.    Karlowicz  424.
1859.  Ar.  sarra:
'Krieg,  Schlacht ;  Streit,  Schlägerei'  [aus Sarr  'böse,  schlimm'] ;  hieraus  siz.  sciar- ra  'Prügelei,  Rauferei'.  [GrSVociSic  245.
1860.  Ar.  sarräf:
[Letzten  Endes  von  ass.  sarpii  'Silber', eigentlich  'das  Geläuterte'  vom  Vb' surrupu  'läutern,  schmelzen',  hieraus  syr. sarräpä,  ar.  sairaf  'Geldwechsler',  vgl. ZAkkFW  59]  'Wechsler',  tk.  ebenso; hieraus  rum.  zaraf  'Geldwechsler',  za- raflic,  zäräße  'Wechselstube';  serb. saraf,  bulg.  sarafin  'Wechsler'.
1861.  Ar.  sart:
'Bedingung',  ebenso  tk.;  hieraus  rum. §art  'Gehörigkeit,  Passendes'.
1862.  MaL  särnng:
'Behälter,  bes.  Scheide  für  den  Kris; Art  Rock'  [Pijn  127  ;  vielleicht  aus  sskr. särana];  hieraus  engl,  sarong,  dtsch. Sarong  'ein  langer  Rock,  gewöhnlich von  buntem  Seidenstoff  oder  Baumwolle', das  Hauptbekleidungsstück  der  Malayen und  Javanesen,  ndl.  saroeng.  [Hobson- Jobson  796.
1863.  Tk.  sary:

=== HJB 20085-20100 ===
[1869.—".  .  .  the  men  in  their  tnldaiis, or  small  single-roofed  tents,  had  a  bad  time of  it.  .  .  ."—Ball,  JungULife,  156.]
8HBAUB,  8HB0BB,  s.    Ar.
shardb;    Hind,   shardb,  sh/rdb,   'wine.' See  under  8HEBBET.
SHBOFF,  s.  A  money-changer,  a banker.  Ar.  sarrdf  sairafi^  sairaf. The  word  is  used  by  Europeans  in China  as  well  as  in  India,  and  is there  applied  to  the  experts  who  are employea  by  banks  and  mercantile firms  to  check  the  quality  of  the dollars  that  pass  into  the  houses  (see Giles  under  next  word).  Also  flhroff- age,  for  money-dealer's  commission. From  th^  same  root  comes  the  Heb. afirifj  'a  soldsmith.'  Compare  the figure  in  malachi,  iii.  3 :  '*  He  shall sit  as  a  refiner  and  purifier  of  silver ;
SHROFF,
832
SHULWAURS.
and  he  shall  purify  the  sons  of  Levi/' Only  in  Hebrew  the  goldsmith  tests metal,  while  the  sairaf  tests  coins. The  Arab  poet  says  of  his  mare : "  Her  forefeet  scatter  the  gravel  every midday,  as  the  dirhams  are  scattered at  their  testing  by  the  sairaf  (W.  R.  S.)
1564.— "iSWarw*  of  the  officers  qf  the  Cus- tom Houses,  and  other  charges  for  these  which the  Treasurert  have  to  pay.  .  .  .  Also  to  the Xairafo,  whose  charge  it  is  to  see  to the  money,  two  pardaos  a  month,  which make  for  a  year  seven  thousand  and  two hundred  reis." -- BoUlho,  Tomboy  in  Sub- Miosy  238.
1560. — "  There  are  in  the  city  many  and very  wealthy  ^arafOf  who  change  money." — fenreirOf  ch.  i.
1584.— *' 5  tangma  make  a  teraphin  (see XERAFINE)  of  gold;  hut  if  one  would change  them  into  hoMruchies  (see  BUD- GBOOE)  he  may  have  5  tangas  and  16 hasarHckieg^  which  ouerplus  they  call cerafBgio.  .  .  ."—Barret,  in  Hail.  ii.  410.
1585. — *^This  present  year,  because  only two  ships  came  to  Goa,  (the  reals)  have  sold at  12  per  cent,  of  Xarafaggio  (shroffage), as  this  commission  is  called,  from  the  word Zaraifo,  which  is  the  title  of  the  banker." —Saasetti,  in  De  GubenuUis,  Storia,  p.  203.
1698.— "There  is  in  every  place  of  the street  exchangers  of  money,  by  them  called XaraffOB,  which  are  all  christian  Jewes." — Linschoten,  66 ;  [Hak.  Soc.  i.  281,  and  see  244.]
c.  1610. — "Dans  ce  March^  .  .  .  aussi sont  les  changeurs  qu'ils  nomment  Cherafes, dont  il  y  en  a  en  plusieurs  autres  endroits  ; leurs  boutiques  sont  aux  bouts  des  ruSs  et carrefours,  toutes  couuertes  de  monnoye, dont  ils  payent  tribut  au  Roy."— Pymrrf  cU Laval,  ii.  39  ;  [Hak.  Soc.  ii.  67].
[1614. — "  .  .  .  having  been  borne  in  hand by  our  SaxafM  to  pay  money  there." — Foster^ Lettert,  iii.  282.  The  "  BherifT  of  Bantam  " {ibid.  iv.  7)  may  perhaps  be  a  shro£F,  but compare  Bhereef.]
1678.— "It  could  not  be  improved  till the  Governor  had  released  the  Bhroffa  or Bankers."- i^«-,  413.
```


## [2026-09-14T01:27:38.880Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B4%D9%84#Arabic",
 "prompt": "Is there an Arabic section for شل (šall/šalla)? Give its meaning ('paralysis, withering of the hand'), the verb شَلَّ, the adjective أَشَلّ, and any descendants into Persian."
}
```


### [2026-09-14T01:27:44.550Z] TOOL RESULT

```
# Arabic Section for شل

Yes, there is an Arabic section covering this word with multiple etymologies.

**Meaning of شَلّ (šall):** The noun form serves as a verbal noun, though the document indicates related concepts through the verbs. The first verb meaning describes "to be lame, to limp," while a second verb form means "to drive, to goad, to prod (livestock)" or "to lame, to paralyze."

**The verb شَلَّ (šalla):** The document presents three verb forms:
1. First form (Form I): "to be lame, to limp"
2. Second form (Form I): "to drive, to goad, to prod livestock" and "to lame, to paralyze"
3. Third form (passive-only): "to be paralyzed"

**The adjective أَشَلّ:** While not explicitly detailed as a standalone entry, the passive participle **مَشْلُول** (mašlūl) meaning "paralyzed" appears in the conjugation tables.

**Descendants into Persian:** The document lists one descendant: **شلیدن** (šalidan) in Persian, derived from the Arabic root.
```


## [2026-09-14T01:28:11.245Z] TOOL CALL #46: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:656 2>&1 | head -50",
 "description": "Fetch Borhan page 656"
}
```


### [2026-09-14T01:28:12.315Z] TOOL RESULT

```
no scan of BQT covers printed page 656 (see 'scans' in refs_online.json)
```


## [2026-09-14T01:28:20.728Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\ntxt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nlines=txt.split('\\n')\n# ff index for line 6651\npre='\\n'.join(lines[:6651])\nprint('ff before line 6651:', pre.count('\\f'))\npages=txt.split('\\f')\n# print first line of a few pages around\nn=pre.count('\\f')\nfor i in (n-2,n-1,n,n+1):\n    p=pages[i]\n    nums=re.findall(r'(?m)^\\s*([۰-۹\\d]{3,4})\\s*$',p)\n    print(i, 'nums:',nums[:6], '| head:', p.strip().split('\\n')[0][:60])\nEOF",
 "description": "Locate Borhan v2 page index for čalipā"
}
```


### [2026-09-14T01:28:21.916Z] TOOL RESULT

```
ff before line 6651: 114
112 nums: [] | head: ‫اس‬    ‫)ی‬
113 nums: [] | head: ‫‪0‬ی‬
114 nums: [] | head: ‫ربسمانی است که برگردن اسبان بندند ‪.‬‬        ‫جلمله = بفتح
115 nums: [] | head: ‫‪۳‬ی‬
```


## [2026-09-14T01:28:25.285Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'));print(json.dumps(d['BQT'],ensure_ascii=False,indent=1))\n\"",
 "description": "Full BQT ref record"
}
```


### [2026-09-14T01:28:26.384Z] TOOL RESULT

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


## [2026-09-14T01:28:49.292Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /tmp && timeout 120 curl -s \"https://archive.org/metadata/americanheritag00morr\" | python3 -c \"\nimport json,sys\nd=json.load(sys.stdin)\nprint(d.get('server'), d.get('dir'))\nfor f in d.get('files',[]):\n    if f['name'].endswith(('_djvu.txt','.pdf','_djvu.xml','_chocr.html.gz')): print(f['name'], f.get('size'))\n\" 2>&1 | head -20",
 "description": "Check AHD archive item"
}
```


### [2026-09-14T01:28:50.805Z] TOOL RESULT

```
ia600806.us.archive.org /29/items/americanheritag00morr
americanheritag00morr.pdf 178433537
americanheritag00morr_bw.pdf 171657742
americanheritag00morr_chocr.html.gz 226566018
americanheritag00morr_djvu.txt 20939236
americanheritag00morr_djvu.xml 222321049
americanheritag00morr_encrypted.pdf 178154443
```


## [2026-09-14T01:28:54.765Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /tmp && timeout 180 curl -sG 'https://ia600806.us.archive.org/fulltext/inside.php' --data-urlencode item_id=americanheritag00morr --data-urlencode doc=americanheritag00morr --data-urlencode path=/29/items/americanheritag00morr --data-urlencode q='seolfor' | python3 -c \"\nimport json,sys\nd=json.load(sys.stdin)\nm=d.get('matches',[])\nprint('matches',len(m))\nfor x in m[:8]:\n    print(x.get('par',[{}])[0].get('page'), x.get('text','')[:160].replace('\\n',' '))\n\" 2>&1 | head -20",
 "description": "Full-text search AHD for seolfor"
}
```


### [2026-09-14T01:28:56.260Z] TOOL RESULT

```
Traceback (most recent call last):
  File "<string>", line 3, in <module>
  File "/usr/lib/python3.12/json/__init__.py", line 293, in load
    return loads(fp.read(),
           ^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/json/__init__.py", line 346, in loads
    return _default_decoder.decode(s)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/json/decoder.py", line 337, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/json/decoder.py", line 355, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
```


## [2026-09-14T01:29:04.118Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && timeout 300 curl -s -o ahd430.txt \"https://ia600806.us.archive.org/29/items/americanheritag00morr/americanheritag00morr_djvu.txt\" && ls -la ahd430.txt && grep -n \"seolfor\" ahd430.txt | head -10",
 "description": "Download AHD djvu text and grep seolfor"
}
```


### [2026-09-14T01:29:05.577Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 4868 Sep 13 21:29 ahd430.txt
```


## [2026-09-14T01:29:15.057Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n 'https://en.wiktionary.org/wiki/%DA%86%D9%84%DB%8C%D9%BE%D8%A7' \\\n 'https://en.wiktionary.org/wiki/%D8%B5%D9%84%D9%8A%D8%A8' \\\n 'https://en.wiktionary.org/wiki/%D8%B4%D9%84' \\\n 'https://en.wiktionary.org/wiki/%D8%B5%D8%B1%D9%81' \\\n 'https://en.wiktionary.org/wiki/%D8%B5%D8%B1%D8%A7%D9%81' \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/silubr%C4%85' \\\n 'https://www.etymonline.com/word/silver' \\\n 'https://www.ahdictionary.com/word/search.html?q=silver' ; do\n timeout 120 python3 tools/fetch_source.py \"$u\" --note 'page 430 verification (Salîbâ / Šalla / Sarâpu entries)' 2>&1 | tail -2\ndone",
 "description": "Archive web sources"
}
```


### [2026-09-14T01:29:19.160Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/6ec8a771433e645d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1e3398f2a1951828.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/800888b2697f0e21.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4ca7051d962c0063.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/003c54de90be5271.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/dc8842da73f4796a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/140db01994c05028.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2e26786a197a478d.txt
```


## [2026-09-14T01:29:21.750Z] TOOL CALL #53: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py",
 "description": "Read verify_check tool"
}
```


### [2026-09-14T01:29:21.811Z] TOOL RESULT

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


## [2026-09-14T01:30:22.692Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON شل ===\"; grep -n \"^شل:\\|شل: \\|شلیدن\" MON_part1.txt MON_part2.txt | head -10\necho; echo \"=== HRN schal/lahm ===\"; grep -n -i \"lahm'\\|'lahm\\|gelähmt\" HRN.txt | head -10\necho; echo \"=== PHD/NYB asem silver ===\"; grep -n -i \"asēm\\|asem \\[\" PHD.txt | head -5",
 "description": "Extra greps for šal and Pahlavi silver"
}
```


### [2026-09-14T01:30:22.808Z] TOOL RESULT

```
=== MON شل ===
MON_part2.txt:7482:فشل: ا25] [ع.] (.) مرد بد دل و ترسنده و 
MON_part2.txt:7485:فشل: اه [ع.] (مصل.) کاهلی کردن؛ 
MON_part2.txt:7488:فشل: (ع25] [ع.] یت و سست و 
MON_part2.txt:7491:فشل: ۳ پرده هودج. فرشی که 
MON_part2.txt:30627:تعان اسب 9 مانشل: ان کب کرفبت رون وا 
MON_part2.txt:40574:نقص پا یا خستگیء شلیدن. لنگیدن کاری: 
MON_part2.txt:81424:نهشل: ۳۵۷5 (ع.] (.) گ رگد ذئب. چرغ. 
MON_part2.txt:85607:ورمیشل: [۹۵] ۷۰۳ (.) نوعی رشته فرنگی 
MON_part1.txt:13578:اشل: 8 (.) واحدی است برای طول 
MON_part1.txt:13581:اشل: (28210 [ع.] (ص.) مردی که دست او 

=== HRN schal/lahm ===

=== PHD/NYB asem silver ===
545:pas-dānišnīh [4HLd’nsnyh] anti-knowledge. pasēmāl [psym’l, v. hamemal] defendant, accused. ~ih: (legal) defence. pasen [psyn! | N pasin] final, last. pasox [p’shw' | № ~] = passox. passand [psnd | N pasand] pleasure, liking. passandidan, passand- [psnd-ytn' | M psynd-, N pasandidan] like, approve. ~išn: liking, approval. ~isnig : likeable. passáxt [ps’ht'] test. passaxtan, passàz- [ps’hin', ps’c- | M ps?xt, ps’c-] fashion, prepare; insert; test. ~išn: preparation, constitution. passazag [psck! | M pscg] suitable, fitting. ~ih: suitability. passox [pshw! | M pswx, № pāsux) answer. past [pst' | N ~] low; astr. dejection. pašēmān [pšm?n! | = M, N ~] penitent, repentant. ~ih: penitence, repentance. pašm [psm | N ~] wool. ~ёп [-yn! | N ~in] woollen. pašn [psn'] bond, agreement. pāšnag [p’snk! | N ~a] heel. pāšom [p(”)$zvm) excellent. passing [pšng | N pišing] drop, exudation. paššinjag [pfnck! | N pišanja] drop. paššinjīdan, paššinj- [psnc-ytn' | N pišanjīdan) sprinkle. ~išn: sprinkling. pa&t(ag) [pšt(k)! | J pst] pact, bond, agreement. *pattān [pt’n'] noise, resonance. ~6mand [отта] resonant. pattāyistan [pi?dstn'] = pattüdan. pattüdan, pattày- [ptwtn', ptd- | P ptwdn, M pt’y-] stay, remain, last, endure. pattüg [ptwk'] enduring, patient, persevering. ^АҺһ: endurance, patience, perseverance. paxSag [phšk! | N pasa] mosquito, gnat. 1рау [pdy | N ~] foot; footstep, track. ~ 1: after. *pay [pdy | M pyy, N ~] sinew, tendon. pay [LGLE < А rglh; p'dy | M p'y, N —] foot, leg; foot (12 in.). 1,2 páy-, у, bL? pādan. payādaģ [pd’tk! | М py’dg, N piyada] on foot, foot-soldier, (chess) pawn. payag [p'd(y)k! | N paya] base, station. paydag [pyt?k! | M pyd'g, N payda] visible, obvious, revealed.
1534:defence  pahréz, pasēmālīh.
1536:defendant pasēmāl.
4644:frašn frašagirdīg frašagird frašamurw fradāg fradom fradomīh pardag pambagén pambag passaxt passáxtan passox passáz- passāzišn pasen pasēmāl pasēmālīh brin-t bridan™ passazagih passazag past, pist pistag
```


## [2026-09-14T01:30:29.482Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '13578,13586p' MON_part1.txt\necho \"---\"\nsed -n '40568,40578p' MON_part2.txt",
 "description": "Print Mo'in ašall and šalidan contexts"
}
```


### [2026-09-14T01:30:29.568Z] TOOL RESULT

```
اشل: 8 (.) واحدی است برای طول 
معادل ۰۰ ذراع یا ٩۰‏ گز. 

اشل: (28210 [ع.] (ص.) مردی که دست او 


افتاده باشد. 

اشل: اه [نردبان مقیاس» پایه] (.) رتب؟ 
---


فر هنگ فارسی معین لو 


به يکك جانب بلند و کوتاه شدن به سبب 
نقص پا یا خستگیء شلیدن. لنگیدن کاری: 
نقصی در آن بودن که موجب تعویق و 
تعطیل گر دد (لخ.) 

لو: (1:۷0(.) نوعی از حلوا است.
```


## [2026-09-14T01:32:06.276Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SKT ===\"; grep -n -i \"silver\\.\" SKT.txt | head -5; grep -n \"A\\.  S\\.  seolfor\\|seolfor\" SKT.txt | head -5\necho; echo \"=== FSD vols ===\"; grep -n \"seolfor\" FSD_vol1.txt FSD_vol2.txt FSD_vol3.txt FSD_vol4.txt | head -5\necho; echo \"=== WEB ===\"; grep -n \"seolfor\" WEB_vol1.txt | head -5\necho; echo \"=== IEC/SYN silver ===\"; grep -n -i \"silver\" SYN.txt | head -8",
 "description": "Skeat/FSD/Webster/Buck for silver"
}
```


### [2026-09-14T01:32:06.428Z] TOOL RESULT

```
=== SKT ===
14163:See  alfove ;  and  t»ee  Form. metal.   (Span   —  F   —  Gk.) named  from  in  silvery  ap- i.  ft'o/a,  silver.  —  O.  F.  fi/tUi,
16300:Rupee,  nn  Indian  coin.  (Hind. -Skt.^ Hindustani  nlpiyah^  .1  rupee.  — Skt.  nipya, haiid^ume.  also  (as  sb.)  silver.  — Skt.  riipa^ l>cauly.
17274:Silver.   (E.)    A.  S.  t.-^  " like    meole  for  miU*)'^ sUfr ;  Dan.  sSh ;  Sv.  - ' Gotb.  silubr;   Kus- Perhaps  named  fro< sidus,  a  star,  I.ith.  jwta-
17990:speole,  money  in  gold  or  silver.  (L.) Evolved  as  a  sb.  from  the  old  word  species, 'money  paid  by  tfllV  Phillips;  prob.  by confusion  with  L  abl.  specie,  as  if  paid  in specie  ^  mid  iu  visible  coin.

=== FSD vols ===
FSD_vol3.txt:209844:of looklng-»das8cs f< AS cwlcseolfor, < ewir, living. 4-
FSD_vol2.txt:6440:L.  rubidus,  red  (its  spectrum) Anglo-.Sa.xon  seolfor  Igray

=== WEB ===

=== IEC/SYN silver ===
8925:Schrader, Reallex. s.v. Gabel and NED s.v. fork, sb. 2. Roman forks used in cooking are mentioned by Petronius, passim. But small bronze and silver forks like our modern table forks have also been found (so my colleague Ullman informs me), though there seems to be no literary reference to the use of forks for eating.
11134:A ‘jewel’ (mostly ‘precious stone’, now esp. with its setting, but in part includ- ing gold and silver ornaments) may be expressed simply as ‘(precious) stone’, but more commonly by specialization of something ‘valuable, costly’, ‘beauti- ful’, ‘giving pleasure’, an ‘ornament’ or a ‘plaything’. In a few cases the name of a specific ornament or gem has been gen- eralized (cf. Fr. bijou, NG dtapavrixd, below).
11145:3. NIr. seod fr. Ir. sét ‘a valuable’ covering a wide range of objects (cf. Laws, Gloss. s.v.), but including ‘pin, brooch’, its earliest attested sense (cf. sét argait ‘silver brooch’ Thes. 2.345) a Lat. (orig. Gall.?) sentis ‘thornbush’, MLat. ‘brooch’, etym.? Schrader, Real- lex. 2.335. Walde-P. 1.450.
13526:SILVER
15402:9.65 SILVER Grk. — &pyupos Goth.  silubr Lith. sidabras NG done ON silfr Lett. sidrabs Lat. argentum Dan. sfif ChSl.  s(it)rebro It. argento Sw. silver SCr.  srebro Fr. argent OE siolfor, seolfor Boh. _ sifebro Sp. plata ME - sylver Pol. __srebro Rum. argint NE silver Russ. serebro Tr. argat, airged Du. —_zilver Skt. —_ rajata- Nir. airgead OHG - sil(a)bar Av. grazata-, OPers. W. arian MHG ssilber ardata- Br. arc’hant NHG silber
15424:aonuos ‘without mark, uncoined’, used freq. with xpvaés or a&pyupos for gold or silver bullion, and aonuoy finally special- ized to ‘silver’ (LXX and freq. in pap.).
15425:Sp. plata, Port. prata, through ‘silver plate’, fr. Prov. plata ‘plate’ : Fr. plat, It. piatto, etc., all fr. Grk. rAarts ‘flat’. REW 6586.
19618:ERCE 773 PROPERTY, COMM pOSSESSION, 11.43 MONEY atts, fathu Lith. pinigat ; a Gor fe, peningar (baugr) ea ite ort ee, aphbess Dan. penge SCr. aoe vet x0 rd Byes 2eenee Boh. abe } pals ges, arger OE feoh, sceatt oh. penize a pean 1 ME mone(ye), fe Pol. pieniqdze rel NE money Russ. den'gi It ce Du. geld Skt. (dhana-) Be nea OHG  scaz, gelt Avs hi) % soni, porale MHG  gelt, schaz i NHG geld vi igen od Cae j,  orchan ord of value in the IE ; names of particular coins, the latter in he chief oa history of the IE- | part derived from the name of the metal riod ae Jes before the introduc- | used, especially ‘silver’. In one group a a money’ based on coinage | ‘money’ is from ‘payment’. 10)
```


## [2026-09-14T01:32:10.317Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '15402,15423p' SYN.txt",
 "description": "Buck on SILVER"
}
```


### [2026-09-14T01:32:10.369Z] TOOL RESULT

```
9.65 SILVER Grk. — &pyupos Goth.  silubr Lith. sidabras NG done ON silfr Lett. sidrabs Lat. argentum Dan. sfif ChSl.  s(it)rebro It. argento Sw. silver SCr.  srebro Fr. argent OE siolfor, seolfor Boh. _ sifebro Sp. plata ME - sylver Pol. __srebro Rum. argint NE silver Russ. serebro Tr. argat, airged Du. —_zilver Skt. —_ rajata- Nir. airgead OHG - sil(a)bar Av. grazata-, OPers. W. arian MHG ssilber ardata- Br. arc’hant NHG silber
1. Derivs. of IE *arg- in words for ‘bright, white’ like Grk. dpyés, Skt. arjuna-, ete. Some variation in form of root and of suffix. Walde-P. 1,82f. Ernout-M. 71. Walde-H. 1.66, 848,
Grk. apyupos; Lat. argentum (> It.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
argento, Fr. argent, Rum. argint), Ose. abl. sg. aragetud; Gall. arganto- in Ar- ganto-marus, etc., Ir. argat, airged, NI. airgead, W. arian, Br. arc’hant; Skt. rajata-, Av. arazata-, OPers. ardata- (Dar. Sus. f. 40), all neuter; Arm. arcat’.
a en —
Pe ee <2, ee 2 ee T
— «1
NS 1 ee) Se _
MISCELL
m some common t in Asia Minor.
ee 3 siolfor, OHG sil(a)- Ha C.; OPruss. sirablan, : Lett. sidrabs; ChSl. sure- general Slavic.
bro, of Grk. &onuov fr.
3, NG dtu, dim.
copr, efydd, pres kouevr, arem
Grk, xadxés and Lat. aes covered both ‘copper’ and its alloy with tin, ‘bronze’. Their actual reference in the majority of cases would be to bronze, since this was somuch more extensively employed than pure copper. So Goth. azz (which ren- ders xadxés as the ‘copper’, really bronze coin, also in aiza-smipa for xadxebs ‘cop- persmith’), ON eir, OF ar, OHG @r, all cognate with Lat. aes and orig. words for epee were applied mainly to what a bronze. A new, specific name if Ca : nia spread over nearly all nished b 7 he Europe, was fur- eae a a a Lat. derivative of the The old “aii eae one ‘bronze’, but for thi ee somestt ton which spread a another new word, furnished aah oy all Europe, was Which is disputed ronzo, the source of
Tass, the allo ‘own in clase
es, NE b Pres) origin
with zinc, was un- antiquity. Of its "ass (whence Ir. pras, W. Y applied to bronze and
ANEOUS PHYSICAL ACTS, ETC.
Digitized by Arya Samaj Foundation Chennai and eGangotri
611
```


## [2026-09-14T01:32:33.504Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v3 صراف ===\"; grep -n \"صراف\" incoming/BQT/BQT_v3_pages.txt | head -5\necho \"=== BQT v3 صلیب ===\"; grep -n \"صلیب\" incoming/BQT/BQT_v3_pages.txt | head -5\necho \"=== FSD vol4 silver ===\"; grep -n \"sil'ver\\|silver, n\" FSD_vol4.txt | head -5",
 "description": "Borhan v3 and FSD checks"
}
```


### [2026-09-14T01:32:33.606Z] TOOL RESULT

```
=== BQT v3 صراف ===
4854:مه وخور است ‎Bly Ulan‏ درصراف.
39557:وخزانه دار ۱ و صراف هم هست و عربان افد ویفتح اول هم آمده است ۰
39559:‎lan,‏ آخ رکه خزینه دار وصراف وتحصیل‌دار فیل وا قوی ‎Je‏ باشد .
=== BQT v3 صلیب ===
9891:‏صلیب روزن این بلم خضرا .
13083:عود الصلیب ‎wo‏ دوايی است که ‎TT PAST‏ ۷
13103:‏1 -یوآن‌مود السلیب ‎putt‏ پرطفل صلیب آوبزم اندر حلق عمداء
13776:‏همه چون غول بیابان , همه چون مار صلیب‎
19206:صلیب بشکنی و دارها زنی چو صلیب تن فرنگان از دار ها کنی ‎GT‏
=== FSD vol4 silver ===
11208:omlold  bivalve- s.  side,  tho  upper  portion  of  a   round  of  Sierra  Nevada  mountains,  10,934  ft  high beef  —   s.  skin,  an  outer  membrane  or  thin  envelop  having  sll  vern,  2   sil'vern.a  [Poet  or  Archaic!  Maae
11241:sU'ver-bc^'ry,  1   silvar-ben,  2   sIFv er-bCr  y,  n   A   sll'vcr-ware",  1   sil'ver-wur',  2   sirxcr-wflr',  n   Articles shriib  (Elragnus  argentea),  of  the  northwestern  United  made  of  silver,  silver  plate,  especially,  silver  tableware. State^WTthsihery  foliage,  flowers,  and  edible  fruit  as  dishes,  v   ases,  ornaments,  etc  ^   .
11242:sll  ver-blU  ,   1   sil  v’er-bil  ,   2   sll  ver-bll  , n   A   seed-eating  sU'ver-Wced",  1   sil'ver-wid',  2   sTl'vcr-wCd*,  n   4 spermestinc  bird  (genus  Jliwnio),  as  the  nutmeg-bird  species  of  potentilla  (Argentina  ansertna)  growing
```


## [2026-09-14T01:38:30.999Z] TOOL CALL #59: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-430.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\n\ndata = {\n \"pdf_page\": 430,\n \"book_page\": 400,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-13\",\n \"entries\": []\n}\n\n# ------------------------------------------------------------------ entry 0\ne0 = {\n \"entry\": 0,\n \"root\": \"Salîbâ\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"Aramaic / Classical Syriac ṣlībā (ܨܠܝܒܐ, Jewish-Aram. צְלִיבָא) 'cross, crucifix', a qatīl-type noun from the Semitic root ṣ-l-b 'to crucify, fix, fasten'\",\n \"note\": \"The root box is right in language, form and gloss: ṣlībā is the ordinary Aramaic/Syriac word for the cross (Peshitta, 2nd c. CE onwards), built on the verb ṣəlab 'to crucify'; en.wiktionary derives the Aramaic noun in turn from Akkadian ṣalāpu 'to cross out, make crooked'. Nourai's three-way fan-out from this one etymon is correct: Persian čalīpā and Christian Sogdian clyb' are direct Iranian borrowings from Syriac, while Arabic ṣalīb is the Arabicisation, which then re-entered Persian as ṣalīb — so čalīpā and ṣalīb are doublets of the same Aramaic word. The one thing to weigh is the opposite direction printed in Nourai's own source: the text of Borhān-e Qāṭeʿ itself says «و صلیب معرّب چلیپاست» ('ṣalīb is the Arabicised čalīpā'), and Fraenkel (Aram. Fremdwörter, p. 272) and Vollers (ZDMG 50, 614, cited by Jeffery) made Aramaic ṣlībā itself a loan from Persian čalīpā. Moʿin rejects this in his own footnote to that very page, and modern scholarship agrees: ṣ-l-b is an inherited Semitic root (Heb. צלב, Syr. ṣlab, S-Arabian) attested long before any Iranian contact, and Persian has no pre-Islamic form of the word.\",\n \"note_fa\": \"«صلیبا» واژه‌ای آرامی/سریانی (ܨܠܝܒܐ) به معنی «چلیپا» است که از ریشهٔ سامی ص‑ل‑ب «بر دار کشیدن، به چلیپا آویختن» ساخته شده و از سدهٔ دوم میلادی در متون سریانی (پشیتا) به کار رفته؛ ویکی‌واژه خودِ این اسم آرامی را نیز وام‌گرفته از اکدی ṣalāpu می‌داند. نورایی به‌درستی هر سه شاخه را از همین یک واژه گرفته است: فارسی «چلیپا» و سغدیِ مسیحی clyb’ وام‌گیری مستقیم از سریانی‌اند و عربی «صلیب» معرّبِ همان است که دوباره به فارسی بازگشته؛ پس «چلیپا» و «صلیب» دوگانهٔ (doublet) یک واژه‌اند. تنها نکتهٔ درخورِ سنجش، دیدگاه وارونه‌ای است که در متن خودِ برهان قاطع آمده («و صلیب معرّب چلیپاست») و فرانکل و ولرس نیز آرامی را وام‌گرفته از فارسی شمرده‌اند؛ معین در حاشیهٔ همان صفحه این را رد می‌کند و پژوهش امروزی نیز اصالت سامی ریشهٔ ص‑ل‑ب را مسلّم می‌داند. حکم: ادعای نورایی درست است.\",\n \"sources\": [W+\"%DA%86%D9%84%DB%8C%D9%BE%D8%A7\", W+\"%D8%B5%D9%84%D9%8A%D8%A8\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:656\", \"status\": \"supports\",\n    \"note\": \"Borhān-e Qāṭeʿ ed. Moʿin, s.v. چلیپا — BQT_v2_pages.txt leaf 114 (printed ≈ leaf+540 = p. 654, i.e. within the ±3 uncertainty of the stated offset for Nourai's p. 656). The Borhān text reads «چلیپا … صلیب نصارا باشد و آن داری است که باعتقاد ایشان عیسی … را بر آن کشیدند» and «و صلیب معرب چلیپاست»; Moʿin's footnote 9 to the headword corrects this: «مأخوذ از آرامی [صلیبا] … صلیبا (عربی صلیب)» — i.e. Persian čalīpā from Aramaic ṣalībā, exactly Nourai's arrow.\"},\n   {\"ref\": \"MON:1310\", \"status\": \"supports\",\n    \"note\": \"Moʿin, Farhang-e Fārsi, s.v. چلیپا (MON_part1.txt line 51255): «چلیپا [آرا. صلیبا = معر. صلیب] (اِخ.) داری که عیسی را بر آن مصلوب کردند؛ صلیب». The bracketed tag [آرا.] = Aramaic is precisely the root Nourai draws. (The OCR text of Moʿin on disk carries no page markers, so p. 1310 itself could not be checked, only the entry.)\"}\n ],\n \"consulted\": [\n   {\"src\": \"FVQ\", \"where\": \"p. 197 s.v. صلب (ṣalaba)\", \"stance\": \"partial\",\n    \"note\": \"Jeffery: 'The word cannot be explained from Arabic, as the verb is denominative from ṣalīb … and is doubtless derived from Aram. ṣlībā; Syr. ṣlīḇā, as Fraenkel, Fremdw. 276, claims.' Supports an Aramaic ṣlībā, but adds 'The word is not original in Aram., however, and perhaps came originally from some Iranian source from a root represented by the Pers. چلیپا (Vollers)' — the reverse of Nourai's chart.\"},\n   {\"src\": \"AFA\", \"where\": \"p. ~272 (AFA.txt line 9665)\", \"stance\": \"contradicts\",\n    \"note\": \"Fraenkel: 'Das Kreuz صليب Nābiga 2,10 ist bekanntlich durch Vermittelung des aramäischen ܨܠܝܒܐ, צליבא aus pers. چلیپا entlehnt.' — Arabic ṣalīb via Aramaic from PERSIAN čalīpā, i.e. the 1886 view that reverses Nourai's root. Not followed today.\"},\n   {\"src\": \"MON\", \"where\": \"s.v. چلیپا and s.v. صلیب\", \"stance\": \"supports\",\n    \"note\": \"«صلیب [معر. آرا. صلیبا = چلیپا]» (MON_part1.txt line 90101) — Moʿin makes Arabic ṣalīb the Arabicisation of Aramaic ṣalībā and equates it with چلیپا.\"},\n   {\"src\": \"BQT\", \"where\": \"vol. 2 leaf 114, s.v. چلیپا (text + Moʿin fn. 9)\", \"stance\": \"partial\",\n    \"note\": \"The 17th-c. text derives Arabic from Persian; Moʿin's editorial footnote reverses it to Aramaic → Persian. Nourai follows Moʿin, correctly.\"}\n ],\n \"nodes\": []\n}\n\ne0[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Persian\", \"words\": \"čalîpâ\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"NP چلیپا čalīpā 'cross' is a borrowing of Classical Syriac ṣlībā, taken over in the Middle Iranian period: Semitic ṣ- is regularly rendered by Iranian č- (the same substitution is visible in the Christian Sogdian form clyb' = čalībā of node #4), intervocalic -b- was heard/written as -p- in New Persian, and the Aramaic determinate ending -ā was kept, giving čalīpā. en.wiktionary states it exactly so: 'borrowed from Classical Syriac ܨܠܝܒܐ (ṣəlīḇā) or some other Aramaic form, perhaps via Sogdian … Aramaic /ṣ/ typically becomes /č/ in Middle Iranian', and calls it a doublet of صلیب. There is no Zoroastrian-Pahlavi antecedent — MacKenzie's Concise Pahlavi Dictionary has no word for 'cross', only dār-gardīh 'crucifixion' and dār 'gallows, wood' — which fits a loan taken in the Christian milieu of eastern Iran and first attested in early New Persian verse (the chart's own Farroḵi Sistāni line, 11th c.). The derived adjective چلیپایی 'cruciform' is a regular NP -ī formation. Moʿin's footnote to Borhān («مأخوذ از آرامی صلیبا») and his Farhang entry ([آرا. صلیبا]) both give Nourai's arrow.\",\n \"derivation_fa\": \"«چلیپا» وام‌واژه‌ای است از سریانیِ کلاسیک ṣlībā که در دورهٔ ایرانی میانه وارد شده است: صادِ سامی در ایرانی میانه به‌قاعده به «چ» بدل می‌شود (همان ابدالی که در سغدیِ مسیحی clyb’ /čalībā/ دیده می‌شود)، «ب» میان‌واکه‌ای در فارسی نو «پ» نوشته و گفته شده و پایانهٔ معرفهٔ آرامیِ ‑ā نیز مانده است؛ پس ṣlībā ← čalīpā. در فارسی میانهٔ زردشتی برابری برای آن نیست — مکنزی تنها dār-gardīh «به دار کشیدن» را می‌آورد — و این با وام‌گیری در محیط مسیحیِ ایرانِ شرقی سازگار است؛ کهن‌ترین گواه‌ها از شعر فارسی دری (فرخی سیستانی، سدهٔ پنجم) است. «چلیپایی» نیز صفت نسبیِ فارسی از همان واژه است. معین در حاشیهٔ برهان قاطع «مأخوذ از آرامی صلیبا» و در فرهنگ فارسی «[آرا. صلیبا]» می‌نویسد. حکم: ادعای نورایی درست است.\",\n \"sources\": [W+\"%DA%86%D9%84%DB%8C%D9%BE%D8%A7\"],\n \"ref_check\": [\n   {\"ref\": \"MON:1310\", \"status\": \"supports\", \"note\": \"«چلیپا [آرا. صلیبا = معر. صلیب]» — Moʿin tags the word Aramaic (MON_part1.txt line 51255).\"},\n   {\"ref\": \"BQT:656\", \"status\": \"supports\", \"note\": \"Moʿin's footnote 9 s.v. چلیپا, BQT_v2_pages.txt leaf 114: «مأخوذ از آرامی … صلیبا (عربی صلیب)»; the Borhān's own text «و صلیب معرب چلیپاست» is the older, rejected direction.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"s.v. چلیپا\", \"stance\": \"supports\", \"note\": \"«[آرا. صلیبا = معر. صلیب]».\"},\n   {\"src\": \"BQT\", \"where\": \"vol. 2, s.v. چلیپا + Moʿin fn. 9\", \"stance\": \"supports\", \"note\": \"footnote «مأخوذ از آرامی صلیبا (عربی صلیب)».\"},\n   {\"src\": \"PHD\", \"where\": \"grep 'cross', 'crucif' in PHD.txt\", \"stance\": \"silent\", \"note\": \"MacKenzie has no Pahlavi word for 'cross': only 'dargardīh [d'lkrtyh | M d'rgyrdyh] crucifixion' and dār 'tree, gallows; wood'. No Middle Persian antecedent of čalīpā — consistent with an Islamic-era / Christian-Sogdian route.\"},\n   {\"src\": \"HRN\", \"where\": \"grep 'calipa', 'Kreuz' in HRN.txt\", \"stance\": \"silent\", \"note\": \"Horn's Grundriss has no entry for چلیپا (the only 'Kreuz' hit, at leaf ~124, is a footnote on drafš/Mandaic). Horn lemmatises inherited Iranian words, so the silence is itself evidence the word is a loan.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Arabic\", \"words\": \"salîb\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Arabic صليب ṣalīb 'cross' is a loan from Aramaic/Syriac ṣlībā, taken over into pre-Islamic Arabic through the Christian Arabs of Ḥīra and Najrān: it is already in the old poetry (an-Nābigha ii,10; ʿAdī b. Zayd) and the Qurʾān uses the denominative verb ṣalaba 'to crucify' (iv,156; v,37; vii,121; xii,41; xx,74; xxvi,49). Jeffery (FVQ 197) is explicit that the direction is noun → verb and that the noun is Aramaic: 'the verb is denominative from ṣalīb … doubtless derived from Aram. ṣlībā; Syr. ṣlīḇā'. The Arabic form drops the Aramaic determinate -ā and fits the native faʿīl pattern, which is why the word was felt to belong to a genuine Arabic root ṣ-l-b (whence ṣalaba, maṣlūb, ṣulbān). en.wiktionary gives the same chain, tracing the Aramaic in turn to Akkadian ṣalāpu. The only dissent concerns the far end: Fraenkel (p. 272) and Vollers made the Aramaic itself a borrowing from Persian čalīpā — not accepted today, since the Semitic root is old and the Iranian word has no pre-Islamic attestation.\",\n \"derivation_fa\": \"عربیِ «صلیب» وام‌واژه‌ای است از آرامی/سریانی ṣlībā که از راه عرب‌های مسیحی حیره و نجران پیش از اسلام به عربی راه یافته است؛ در شعر جاهلی (نابغه ۲/۱۰ و عدی بن زید) و سپس در قرآن (نساء ۱۵۶، مائده ۳۷، اعراف ۱۲۱، یوسف ۴۱، طه ۷۴، شعراء ۴۹) دیده می‌شود. جفری (ص ۱۹۷) تصریح می‌کند که فعل «صَلَبَ» در عربی اشتقاقی از همین اسم است، نه برعکس. پایانهٔ معرفهٔ آرامی ‑ā افتاده و واژه به قالب «فَعیل» عربی درآمده و از همین رو ریشهٔ ص‑ل‑ب در عربی زایا شده است (صَلَبَ، مصلوب، صُلبان). ویکی‌واژه نیز همین زنجیره را می‌آورد و آرامی را از اکدی ṣalāpu می‌گیرد. تنها اختلاف بر سر سرچشمهٔ خودِ آرامی است که فرانکل و ولرس آن را فارسی «چلیپا» می‌دانستند؛ این دیدگاه امروز پذیرفته نیست. حکم: ادعای نورایی درست است.\",\n \"sources\": [W+\"%D8%B5%D9%84%D9%8A%D8%A8\"],\n \"ref_check\": [\n   {\"ref\": \"MON:1310,2161\", \"status\": \"supports\", \"note\": \"Moʿin s.v. صلیب: «صلیب [معر. آرا. صلیبا = چلیپا]» (MON_part1.txt line 90101) and s.v. چلیپا «[آرا. صلیبا = معر. صلیب]» (line 51255) — both pages make Arabic ṣalīb the Arabicised Aramaic ṣalībā, as the chart draws it. Page numbers themselves unverifiable (the Moʿin OCR on disk has no page markers).\"}\n ],\n \"consulted\": [\n   {\"src\": \"FVQ\", \"where\": \"p. 197 s.v. صلب\", \"stance\": \"partial\", \"note\": \"'the verb is denominative from ṣalīb … doubtless derived from Aram. ṣlībā; Syr. ṣlīḇā' — supports the arrow, but reports Vollers's contrary idea that the Aramaic came from Persian čalīpā.\"},\n   {\"src\": \"AFA\", \"where\": \"p. ~272\", \"stance\": \"contradicts\", \"note\": \"Fraenkel: Arabic ṣalīb 'durch Vermittelung des aramäischen … aus pers. چلیپا entlehnt' — Aramaic only as intermediary, with Persian as the ultimate source.\"},\n   {\"src\": \"TAD\", \"where\": \"grep صليب in TAD_pages.txt\", \"stance\": \"silent\", \"note\": \"al-ʿUnaysī's list of foreign words in Arabic has no ṣalīb entry (only الحروب الصليبية 'the Crusades' in passing, line 230).\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Persian\", \"words\": \"salîb\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"NP صلیب ṣalīb is the Arabic word re-borrowed into Persian after the conquest, and is the learned doublet of the older, directly-borrowed چلیپا: the same Aramaic etymon reached Persian twice, once through Middle Iranian (čalīpā) and once through Arabic (ṣalīb), which is why Moʿin defines each by the other («صلیب [معر. آرا. صلیبا = چلیپا]»). Because it came with Arabic morphology it brought its derivatives along — مصلوب maṣlūb is the Arabic passive participle of ṣalaba 'to crucify', and صلیبی 'crusader'. The chart's Ḥāfeẓ line («ناقوس دیر راهب و نام صلیب هست») shows it current in 14th-c. Persian. en.wiktionary lists Classical Persian صَلِیب among the descendants of the Arabic noun.\",\n \"derivation_fa\": \"«صلیب» در فارسی نو وام‌واژه‌ای عربی است که پس از اسلام وارد شده و دوگانهٔ ادبیِ «چلیپا» به شمار می‌رود: یک اتیمونِ آرامی دو بار به فارسی رسیده — یک بار از راه ایرانی میانه (چلیپا) و یک بار به میانجی عربی (صلیب) — و از همین رو معین هر یک را با دیگری تعریف می‌کند: «صلیب [معر. آرا. صلیبا = چلیپا]». چون واژه با صرفِ عربی آمده، مشتقات عربی‌اش نیز با آن آمده است: «مصلوب» اسم مفعولِ «صَلَبَ» و «صلیبی» منسوب به آن. شاهد حافظ («ناقوس دیر راهب و نام صلیب هست») رواج آن را در فارسی سدهٔ هشتم نشان می‌دهد. ویکی‌واژه نیز فارسیِ کلاسیک «صَلِیب» را در فهرست بازماندگانِ واژهٔ عربی آورده است. حکم: ادعای نورایی درست است.\",\n \"sources\": [W+\"%D8%B5%D9%84%D9%8A%D8%A8\"],\n \"ref_check\": [\n   {\"ref\": \"MON:2161\", \"status\": \"supports\", \"note\": \"Moʿin s.v. صلیب (MON_part1.txt line 90101): «صلیب: [معر. آرا. صلیبا = چلیپا] (ا.) شکل صلیب از چوب یا فلز که ترسایان به گردن خود آویزند …» — tagged معرَّب (Arabicised), i.e. entering Persian through Arabic.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"s.v. صلیب\", \"stance\": \"supports\", \"note\": \"«[معر. آرا. صلیبا = چلیپا]»; Moʿin equates it with چلیپا, i.e. treats the two as the same word by two routes.\"},\n   {\"src\": \"BQT\", \"where\": \"vol. 3 (ش–ل), grep صلیب\", \"stance\": \"silent\", \"note\": \"The Borhān lemmatises صلیب nowhere (hits in BQT_v3_pages.txt are only verse quotations, e.g. line 19206 «صلیب بشکنی و دارها زنی»); as a Persian-word dictionary it leaves Arabic loans out, so it has nothing to say for or against.\"},\n   {\"src\": \"ARY\", \"where\": \"grep صلیب/چلیپا in ARY_pages.txt\", \"stance\": \"silent\", \"note\": \"Aryanpur's dictionary of Indo-European roots of Persian has no entry for either word — expected, since both are Semitic loans.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 4, \"lang\": \"Sogdian\", \"words\": \"clyb`\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Christian Sogdian clyb' (Syriac script, read čalībā) 'cross' is attested in the Turfan Christian Sogdian texts (Gharib cites BSTii 880.13 and C2, 77R13 — the latter a Christian Sogdian manuscript from Bulayïq). It is a straight borrowing from Syriac ṣlībā made by the Nestorian mission in Central Asia, with the same Semitic ṣ → Iranian č substitution that produced Persian čalīpā; Gharib's entry marks the source herself with '©<Syr.'. The Sogdian form is the strongest evidence against the old Fraenkel/Vollers direction, because it shows the word arriving in Iranian from Syriac in a documented Christian milieu, not leaving Iranian for Aramaic; en.wiktionary even suggests Persian čalīpā may have come 'perhaps via Sogdian', which would make node #4 the intermediary of node #1 rather than its sibling — a nuance Nourai's chart does not draw, but not an error in the arrow itself.\",\n \"derivation_fa\": \"سغدیِ مسیحی clyb’ (به خط سریانی، خوانش čalībā) «چلیپا» در متون مسیحیِ سغدیِ تورفان گواه دارد (غریب به BSTii 880.13 و C2, 77R13 از بولایق ارجاع می‌دهد) و وام‌گیریِ مستقیم از سریانی ṣlībā به دست مبلغان نسطوری در آسیای میانه است؛ همان ابدالِ صادِ سامی به «چ» که در «چلیپا»ی فارسی هم دیده می‌شود. غریب خودْ منبع را «©<Syr.» نشانه‌گذاری کرده است. این صورتِ سغدی قوی‌ترین گواه در ردّ دیدگاه فرانکل/ولرس است، زیرا نشان می‌دهد واژه در محیطی مستند از سریانی به ایرانی رفته، نه برعکس. ویکی‌واژه حتی احتمال می‌دهد «چلیپا»ی فارسی «شاید به میانجی سغدی» آمده باشد — نکته‌ای که نورایی سغدی را هم‌تراز فارسی گذاشته و این میانجی‌گری را ننموده است، هرچند خودِ پیکان نادرست نیست. حکم: ادعای نورایی درست است.\",\n \"sources\": [W+\"%DA%86%D9%84%DB%8C%D9%BE%D8%A7\"],\n \"ref_check\": [\n   {\"ref\": \"SOD:126\", \"status\": \"supports\", \"note\": \"Gharib, Sogdian Dictionary, entry no. 3202 on printed p. 126 (SOD_pages.txt line 12879, inside the page block 126 that runs lines 12823–12895): '3202 clyb' C — čalība ©<Syr. — cross — BSTii 880.13; C2, 77R13'. Nourai's SOD:126 is the printed page, and it says exactly what the arrow says: Sogdian from Syriac (= the Aramaic root box).\"}\n ],\n \"consulted\": [\n   {\"src\": \"SOD\", \"where\": \"no. 3202, p. 126\", \"stance\": \"supports\", \"note\": \"'clyb' C … ©<Syr. … cross' — Gharib tags the word a Syriac loan.\"},\n   {\"src\": \"PHD\", \"where\": \"grep 'cross'/'crucif'\", \"stance\": \"silent\", \"note\": \"no Middle Persian counterpart; MacKenzie has only dārgardīh 'crucifixion'. The cross-word is confined to the Christian (Sogdian/Syriac) side of Middle Iranian.\"}\n ]\n})\n\ndata[\"entries\"].append(e0)\n\n# ------------------------------------------------------------------ entry 1\ne1 = {\n \"entry\": 1,\n \"root\": \"Šalla\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"Arabic شَلَّ šalla (root ش ل ل) 'to wither, be paralysed (of the hand)'; maṣdar شَلَل šalal; adj. أَشَلّ ašall 'having a withered/palsied hand'\",\n \"note\": \"The root box is correct in language, form and gloss. en.wiktionary's Arabic entry gives šalla both intransitive 'to be lame, to limp' / 'to be paralysed' and causative 'to lame, to paralyze', with the participle مَشْلُول 'paralysed'; Lane s.v. ش ل ل gives the same, with ašall of a man whose hand is withered. Moʿin's footnote in Borhān-e Qāṭeʿ states the Arabic side in the same words: «شَلّ … مصدر است بمعنی تباه شدن دست و خشک گردیدن، و اَشَلّ … مرد تباه‌دست (منتهی‌الارب)». Nourai's cited source (SAP = Sayyāḥ's Persian rendering of al-Munjid, p. 818) is not available in any digital form, so the reference itself could not be inspected, but its content is corroborated by the Arabic lexica.\",\n \"note_fa\": \"ریشهٔ عربیِ «شَلَّ» (ش‑ل‑ل) به معنی «خشک و تباه شدن دست، فلج شدن» درست ثبت شده است؛ مصدر آن «شَلَل» و صفتش «أَشَلّ» یعنی «مردی که دستش از کار افتاده». ویکی‌واژه هر دو کاربرد لازم («لنگ شدن، فلج شدن») و متعدی («فلج کردن») را می‌آورد و اسم مفعول «مشلول» را نیز ثبت کرده است. معین در حاشیهٔ برهان قاطع همین را می‌نویسد: «شَلّ … مصدر است بمعنی تباه شدن دست و خشک گردیدن، و اَشَلّ … مرد تباه‌دست (منتهی‌الارب)». مأخذی که نورایی آورده (فرهنگ سیاح، ص ۸۱۸) در هیچ نسخهٔ رقمی در دسترس نبود، اما محتوای آن با فرهنگ‌های عربی تأیید می‌شود. حکم: ادعای نورایی درست است.\",\n \"sources\": [W+\"%D8%B4%D9%84\"],\n \"ref_check\": [\n   {\"ref\": \"SAP:818\", \"status\": \"not_checked\", \"note\": \"Sayyāḥ, Farhang-e Sayyāḥ (Persian al-Munjid) — no online or local copy exists (refs_online.json: 'kind': 'purchase', fidibo ebook only). The Arabic content of the entry was instead checked against en.wiktionary's ش ل ل material and Moʿin's footnote in BQT.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"s.v. أشل\", \"stance\": \"supports\", \"note\": \"«اشل: [ع.] (ص.) مردی که دست او افتاده باشد» (MON_part1.txt line 13581) — Moʿin's Arabic adjective, the base of the Persian word.\"},\n   {\"src\": \"BQT\", \"where\": \"vol. 3 p. 1287, Moʿin's fn. 8 to شل\", \"stance\": \"supports\", \"note\": \"«شَلّ (بفتح اول و تشدید دوم) مصدر است بمعنی تباه شدن دست و خشک گردیدن، و اَشَلّ … مرد تباه دست (منتهی الارب)» — the Arabic root as Nourai states it.\"},\n   {\"src\": \"FVQ\", \"where\": \"grep šalla / paralyse in FVQ_pages.txt\", \"stance\": \"silent\", \"note\": \"Jeffery has no entry for the root (it is not a Qurʾānic foreign word) — expected for a native Arabic root.\"}\n ],\n \"nodes\": []\n}\n\ne1[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Persian\", \"words\": \"šal 2; šalîdan\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"NP شَل šal 'lame, crippled, with a useless limb' is taken from Arabic, and specifically — as Moʿin says in his footnote to Borhān-e Qāṭeʿ p. 1287 — from the adjective أَشَلّ ašall: «و شل بمعنی اخیر تصرفی است از ایرانیان در کلمهٔ اشلّ عربی و شلیدن هم مصدر جعلی آنست» ('šal in the last sense is an Iranian adaptation of the Arabic word ašall, and šalīdan too is a denominative infinitive built on it'). The initial ʾa- of ašall was taken for the Arabic elative/colour-and-defect prefix and dropped, and the geminate -ll simplified, giving Persian šal; on that stem Persian then built the maṣdar-e jaʿlī شلیدن šalīdan 'to be/become lame' with the native infinitive suffix -īdan — the same pattern as فهمیدن, رقصیدن. en.wiktionary agrees on both points: its Persian شل 'Etymology 4 (adj. lame)' is 'Borrowed from Arabic أشل', and شلیدن is listed as the Persian descendant of Arabic شل. The Borhān's own entry already notes the Arabic sense: «و بعربی دست و پای را گویند که از کار بازمانده باشد». Nourai's index '2' on šal is well judged: the homonymous شل 'loose, limp; soft', شل 'thigh' and شل 'spear, harpoon' are separate, non-Arabic etyma (Wiktionary's Etymologies 1–3), and only the 'lame' one belongs here.\",\n \"derivation_fa\": \"«شَل» در فارسی وام‌واژه‌ای عربی است و چنان‌که معین در حاشیهٔ برهان قاطع (ص ۱۲۸۷) می‌نویسد از صفتِ «أَشَلّ» گرفته شده است: «و شل بمعنی اخیر تصرفی است از ایرانیان در کلمهٔ اشلّ عربی و شلیدن هم مصدر جعلی آنست». همزهٔ آغازینِ «أشلّ» را نشانهٔ وزنِ أفعلِ عربی (صفتِ عیب و رنگ) پنداشته و انداخته‌اند و تشدیدِ لام نیز ساده شده، پس «شل» به دست آمده؛ سپس از همین ستاک، مصدر جعلیِ «شلیدن» با پسوندِ مصدریِ فارسی ‑یدن ساخته شده است (همان الگوی «فهمیدن» و «رقصیدن»). ویکی‌واژه نیز «شل» به معنی «لنگ» را وام‌گرفته از عربیِ «أشل» می‌داند و «شلیدن» را در فهرست بازماندگانِ «شلّ» عربی می‌آورد. متن خودِ برهان هم می‌گوید «و بعربی دست و پای را گویند که از کار بازمانده باشد». شمارهٔ ۲ که نورایی به «شل» داده درست است، زیرا «شل» به معنی «سست/نرم»، «شل» به معنی «ران» و «شل» به معنی «نیزه» ریشه‌های جداگانه و غیرعربی دارند. حکم: ادعای نورایی درست است.\",\n \"sources\": [W+\"%D8%B4%D9%84\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:1287\", \"status\": \"supports\", \"note\": \"Page fetched with tools/ref_page.py BQT:1287 (vol. 3, pdf p. 78; cached at data/verification/sources/refs/ocr/BQT/1287.*). The headword شل is there, and Moʿin's footnote 8 reads: «شَلّ (بفتح اول و تشدید دوم) مصدر است بمعنی تباه شدن دست و خشک گردیدن، و اَشَلّ … مرد تباه دست (منتهی الارب) و شل بمعنی اخیر تصرفی است از ایرانیان در کلمهٔ اشلّ عربی و شلیدن هم مصدر جعلی آنست.» — both of Nourai's Persian words derived from the Arabic root, exactly as charted.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BQT\", \"where\": \"p. 1287, entry شل + Moʿin fn. 8\", \"stance\": \"supports\", \"note\": \"«و شل بمعنی اخیر تصرفی است از ایرانیان در کلمهٔ اشلّ عربی و شلیدن هم مصدر جعلی آنست».\"},\n   {\"src\": \"MON\", \"where\": \"s.v. أشل; s.v. لنگیدن\", \"stance\": \"supports\", \"note\": \"«اشل [ع.] (ص.) مردی که دست او افتاده باشد»; and لنگیدن is glossed with شلیدن («… نقص پا یا خستگی، شلیدن، لنگیدن», MON_part2.txt line 40574), confirming the Persian verb's currency and sense.\"},\n   {\"src\": \"HRN\", \"where\": \"grep 'lahm', 'gelähmt' in HRN.txt\", \"stance\": \"silent\", \"note\": \"Horn has no entry for شل/شلیدن — he lemmatises inherited Iranian words, so a loan from Arabic is simply absent.\"},\n   {\"src\": \"PHD\", \"where\": \"grep in PHD.txt\", \"stance\": \"silent\", \"note\": \"no Middle Persian *šal 'lame'; MacKenzie has no such lemma, which fits an Arabic loan of the Islamic period.\"}\n ]\n})\n\ndata[\"entries\"].append(e1)\n\n# ------------------------------------------------------------------ entry 4\ne4 = {\n \"entry\": 4,\n \"root\": \"Sarâpu, Sarpu\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"Akkadian ṣarāpu 'to refine, smelt (metal); to fire (bricks), to dye red', verbal adjective ṣarpu 'refined (silver)', agent noun ṣarrāpu 'refiner, silversmith'\",\n \"note\": \"Both Akkadian forms and both glosses are right, and the derivational relation Nourai draws inside the root box (ṣarpu = verbal adjective of ṣarāpu) is the standard one; the current American Heritage Dictionary prints it in those very words s.v. silver ('Akkadian ṣarpu, refined silver, verbal adj. of ṣarāpu, to smelt, refine; see ṣrp'), and Proto-Semitic *ṣrp 'to smelt' is a recognised technological root. What the chart then does with the root is of two different qualities: the Semitic branch (→ Arabic ṣ-r-f → Persian ṣarrāf) is supported by the whole older loanword literature (Zimmern, Lokotsch, Klein, Hobson-Jobson), while the Germanic branch (→ OE seolfor → English silver) is a hypothesis that AHD and Klein print but that Kroonen, Wiktionary and Etymonline set aside in favour of an unidentified non-Indo-European Wanderwort — see node #3.\",\n \"note_fa\": \"هر دو صورتِ اکدی و هر دو معنی درست ثبت شده‌اند و نسبتی که نورایی میان آن دو می‌گذارد (ṣarpu صفتِ فعلیِ ṣarāpu) همان است که فرهنگ‌های معتبر می‌آورند؛ فرهنگ American Heritage در مدخل silver عیناً می‌نویسد «Akkadian ṣarpu, refined silver, verbal adj. of ṣarāpu, to smelt, refine» و ریشهٔ سامیِ آغازین *ṣrp «گداختن، پالودن» شناخته‌شده است. اما دو شاخه‌ای که از این ریشه کشیده شده هم‌ارزش نیستند: شاخهٔ سامی (← ص‑ر‑ف عربی ← «صرّاف» فارسی) را زیمرن، لوکوچ، کلاین و هابسن‌جابسن پشتیبانی می‌کنند، حال آنکه شاخهٔ ژرمنی (← seolfor انگلیسی کهن ← silver) فرضیه‌ای است که کلاین و AHD می‌پذیرند ولی کرونن و ویکی‌واژه و اتیمآنلاین آن را کنار می‌گذارند و واژه را «واژهٔ سرگردان» (Wanderwort) با خاستگاهِ ناشناختهٔ غیرهندواروپایی می‌دانند (نگاه کنید به گرهٔ ۳).\",\n \"sources\": [W+\"Reconstruction:Proto-Germanic/silubr%C4%85\", \"https://www.ahdictionary.com/word/search.html?q=silver\"],\n \"ref_check\": [\n   {\"ref\": \"AHD:1206\", \"status\": \"supports\", \"note\": \"The AHD main-entry etymology is verbatim Nourai's root box: 'silver … [Middle English, from Old English siolfor, seolfor, probably ultimately from Akkadian ṣarpu, refined silver, verbal adj. of ṣarāpu, to smelt, refine; see ṣrp]' (ahdictionary.com, the current online edition of the same dictionary). The 1975 New College printed page 1206 could not itself be opened — archive.org's americanheritag00morr is access-restricted (its _djvu.txt download returns an error page) and the local AHD file is only Watkins's Indo-European appendix, which has no 'silver' because the word is not IE; but the etymology text is unchanged across editions, so the citation stands.\"},\n   {\"ref\": \"KLN:1445\", \"status\": \"supports\", \"note\": \"Klein 1966 p. 1445 (KLN_1966.txt line 35228; the page numerals 1444 and 1446 bracket it at lines 35205/35251), s.v. silver: 'ME. silver, fr. OE. seolfor, siolofr, silofr, rel. to OS. silutar, ON. silfr … Goth. silubr … All these words are prob. borrowed ult. fr. Akkad. ṣarpu, \"silver\", lit. \"refined silver\", which is rel. to ṣarāpu, \"to refine, smelt\", ṣarrāpu, \"goldsmith\", Heb. tzāraph, \"he refined, smelted\", tzoreph, \"goldsmith, silversmith\", Aram.-Syr. tzeraph, \"he refined, smelted\", Arab. ṣarf, \"pure (wine)\".' — the exact page, and it covers BOTH branches of Nourai's chart.\"}\n ],\n \"consulted\": [\n   {\"src\": \"AKD\", \"where\": \"Zimmern, Akkadische Fremdwörter, p. 27\", \"stance\": \"supports\", \"note\": \"'akk. ṣarrāpu Goldschmied (ṣarpu Silber, ṣurrupu (Metalle) schmelzen) : > wohl durchweg der St. srp in der Bed. des Metallschmelzens, -läuterns im Hebr. (auch Phön.) und Aram. (>> im Arab.).' — the Akkadian words exist as glossed, and Zimmern makes them the source of the West-Semitic (and, indirectly, Arabic) ṣrp/ṣrf root.\"},\n   {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1860 s.v. Ar. ṣarrāf\", \"stance\": \"supports\", \"note\": \"'[Letzten Endes von ass. ṣarpu \"Silber\", eigentlich \"das Geläuterte\" vom Vb. ṣurrupu \"läutern, schmelzen\", hieraus syr. ṣarrāpā, ar. ṣairaf \"Geldwechsler\", vgl. ZAkkFW 59]' — the Akkadian → Syriac → Arabic route of the money-changer word, i.e. Nourai's Semitic branch.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck §9.65 SILVER, p. 611\", \"stance\": \"partial\", \"note\": \"Buck lists OE siolfor/seolfor with OHG sil(a)bar, OPruss. sirablan, Lith. sidabras, ChSl. sŭrebro and (OCR damaged) traces them to 'some common [source] in Asia Minor' — a common non-IE source, but he does not name Akkadian.\"},\n   {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt, IE-roots appendix\", \"stance\": \"silent\", \"note\": \"grep 'seolfor'/'silver' returns only the essay remark 'Silver was arg-, with various suffixes' and the root arg- 'the shining or white metal, silver' (Pok. 64) — i.e. Watkins's appendix has no IE root for the Germanic silver-word at all, which is why the AHD main entry must reach outside IE for it.\"}\n ],\n \"nodes\": []\n}\n\ne4[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Arabic\", \"words\": \"s.r.f; sarrâf\",\n \"verdict\": \"plausible\",\n \"derivation\": \"The Semitic root ṣ-r-p 'to smelt, refine (metal)' — Akkadian ṣarāpu/ṣarpu, Hebrew ṣārap 'he refined', ṣōrēp 'goldsmith', Aram.-Syr. ṣəraf, Syr. agent-noun ṣarrāpā — appears in Arabic with the regular Proto-Semitic *p > Arabic f as ṣ-r-f, and Arabic ṣarrāf is formally its faʿʿāl intensive/occupational noun, 'one who assays and exchanges coin'. Three of the standard loanword handbooks state Nourai's arrow outright: Zimmern (p. 27) has the ṣrp root spreading from Akkadian into Hebrew, Phoenician and Aramaic 'and (indirectly) into Arabic'; Lokotsch (no. 1860) says of Arabic ṣarrāf 'ultimately from Assyrian ṣarpu \"silver\", properly \"the refined\", from the verb ṣurrupu \"to refine, smelt\", whence Syriac ṣarrāpā, Arabic ṣayraf \"money changer\"'; and Hobson-Jobson s.v. SHROFF supplies the semantic bridge — 'From the same root comes the Heb. ṣōrēp, \"a goldsmith\". Compare … Malachi iii.3: \"He shall sit as a refiner and purifier of silver\" … Only in Hebrew the goldsmith tests metal, while the ṣairaf tests coins.' Two things keep this at 'plausible' rather than 'confirmed'. First, Nourai's gloss of the root as 'to purify silver' compresses two Arabic families: the refining sense survives clearly only in ṣirf 'pure, unmixed (wine)' — which is exactly the item Klein p. 1445 cites as the Arabic reflex of Akkadian ṣarpu — whereas the everyday Arabic ṣarafa means 'to turn, divert, dismiss, exchange (money)'. Second, Arabic lexicography and en.wiktionary derive ṣarrāf simply as the agent noun of that native ṣarafa, with no Akkadian involved; Klein himself, s.v. shroff (p. 1439), writes 'Arab. ṣarrāf, \"money changer\", fr. ṣarrafa, \"he changed money\", second conjugation of ṣarafa, \"he turned\"'. So the Akkadian ancestry of the Arabic root is a respectable and repeatedly published claim, but it is a claim about a possible inherited/borrowed Semitic root, not a documented borrowing event.\",\n \"derivation_fa\": \"ریشهٔ سامیِ ص‑ر‑پ «گداختن و پالودنِ فلز» — اکدی ṣarāpu/ṣarpu، عبری ṣārap «پالود» و ṣōrēp «زرگر»، آرامی/سریانی ṣəraf و اسم فاعلِ سریانیِ ṣarrāpā — با تبدیلِ قاعده‌مندِ «پ»ِ سامیِ آغازین به «ف» در عربی به صورت ص‑ر‑ف درآمده و «صرّاف» صیغهٔ فَعّالِ همان است، یعنی «آن‌که سکه را می‌سنجد و مبادله می‌کند». سه کتابِ مرجعِ وام‌واژه‌ها همین را می‌گویند: زیمرن (ص ۲۷) گسترشِ ریشهٔ srp را از اکدی به عبری و فنیقی و آرامی و «سپس (با واسطه) به عربی» می‌داند؛ لوکوچ (شمارهٔ ۱۸۶۰) «صرّاف» عربی را «سرانجام از آشوریِ ṣarpu «نقره»، در اصل «پالوده»» و از راه سریانیِ ṣarrāpā می‌گیرد؛ و هابسن‌جابسن پلِ معناییِ آن را می‌سازد: در عبری زرگر فلز را می‌آزماید و در عربی صیرفی سکه را. اما دو نکته آن را از «تأیید کامل» بازمی‌دارد: نخست آنکه معنیِ «پالودنِ نقره» که نورایی به ریشه داده، در عربی روشن‌تر در «صِرْف» (ناب و ناآمیخته) مانده است — همان واژه‌ای که کلاین در ص ۱۴۴۵ بازتابِ عربیِ ṣarpu می‌شمارد — حال آنکه «صَرَفَ»ِ رایج یعنی «گرداندن، بازگرداندن، مبادله کردن». دوم آنکه فرهنگ‌نویسیِ عربی و ویکی‌واژه «صرّاف» را بی‌هیچ پیوندِ اکدی، صرفاً اسم فاعلِ همان «صَرَفَ»ِ بومی می‌دانند و خودِ کلاین در مدخل shroff می‌نویسد «از صَرَّفَ، بابِ دومِ صَرَفَ «گرداند»». پس: با احتیاط پذیرفتنی است.\",\n \"sources\": [W+\"%D8%B5%D8%B1%D9%81\", W+\"%D8%B5%D8%B1%D8%A7%D9%81\"],\n \"ref_check\": [\n   {\"ref\": \"KLN:1445\", \"status\": \"partial\", \"note\": \"Klein p. 1445 s.v. silver does name an Arabic member of the family — 'Arab. ṣarf, \"pure (wine)\"' — alongside Heb. ṣārap and Aram.-Syr. ṣəraf, all 'rel. to' Akkad. ṣarāpu; so the page supports an Arabic ṣ-r-f belonging to the refining root. It does not, however, say on that page that ṣarrāf 'money changer' comes from it; at p. 1439 s.v. shroff Klein derives ṣarrāf from ṣarafa 'he turned'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"AKD\", \"where\": \"Zimmern p. 27\", \"stance\": \"supports\", \"note\": \"'der St. srp in der Bed. des Metallschmelzens, -läuterns im Hebr. (auch Phön.) und Aram. (>> im Arab.)' — the refining root reaching Arabic from the Akkadian/Aramaic side.\"},\n   {\"src\": \"LKT\", \"where\": \"no. 1860, s.v. Ar. ṣarrāf\", \"stance\": \"supports\", \"note\": \"'Letzten Endes von ass. ṣarpu \"Silber\" … hieraus syr. ṣarrāpā, ar. ṣairaf \"Geldwechsler\"' — exactly Nourai's arrow, including the money-changer sense.\"},\n   {\"src\": \"HJB\", \"where\": \"s.v. SHROFF, pp. 831–832\", \"stance\": \"supports\", \"note\": \"'Ar. ṣarrāf, ṣairafī, ṣairaf … From the same root comes the Heb. ṣōrēf, \"a goldsmith\" … Only in Hebrew the goldsmith tests metal, while the ṣairaf tests coins.'\"},\n   {\"src\": \"KLN\", \"where\": \"p. 1439 s.v. shroff\", \"stance\": \"partial\", \"note\": \"'Hind. sarraf, fr. Arab. ṣarrāf, \"money changer\", fr. ṣarrafa, \"he changed money\", second conjugation of ṣarafa, \"he turned\"' — the competing, purely Arabic-internal derivation.\"},\n   {\"src\": \"FVQ\", \"where\": \"grep ṣarrāf / ṣarf in FVQ_pages.txt\", \"stance\": \"silent\", \"note\": \"not a Qurʾānic foreign word; Jeffery has no entry.\"}\n ]\n})\n\ne4[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Persian\", \"words\": \"sarrâf\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"NP صرّاف ṣarrāf is an unassimilated Arabic loan (the faʿʿāl occupational noun of ṣarafa), current in Persian from the ʿAbbasid bazaar onward as the title of the money-changer and, later, the private banker; it keeps the Arabic šadda in Persian spelling and takes native derivatives صرّافی 'money-changing, banking' and صرّافخانه. Moʿin's definition preserves precisely the assaying sense that ties the word to the 'refine/test metal' side of the root: «صرّاف [ع.] (ص.) آنکه پول نیک را از بد جدا کند؛ سره‌گر، نقّاد، ناقد. (ف.) کسی که به داد و ستد انواع پول پردازد؛ صیرفی» — 'one who separates good coin from bad; assayer … one who deals in currencies'. From Persian the word travelled on: Hindustani sarrāf, whence Anglo-Indian shroff (Hobson-Jobson pp. 831–2, with Portuguese xarafo already in 1564), and Ottoman Turkish sarraf, whence Romanian zaraf, Serbian saraf, Bulgarian sarafin (Lokotsch no. 1860). The chart's Ḥāfeẓ line («نگاهدار که قلاب شهر صرّافست») shows it fully naturalised by the 14th century. This node is independent of the uncertainty at node #1: whatever the Arabic root's own ancestry, Persian took the word from Arabic.\",\n \"derivation_fa\": \"«صرّاف» در فارسی وام‌واژه‌ای عربی است (صیغهٔ فَعّالِ «صَرَفَ») که از روزگار عباسی در بازارِ ایران به معنی «سکه‌سنج و مبادله‌گرِ پول» و سپس «بانکدارِ خصوصی» به کار رفته و تشدیدِ عربی را در املای فارسی نگاه داشته و مشتقاتِ فارسیِ «صرّافی» و «صرّافخانه» از آن ساخته شده است. تعریفِ معین دقیقاً همان معنای «سنجشِ عیار» را نگاه داشته که واژه را به سویهٔ «پالودن/آزمودنِ فلز»ِ ریشه پیوند می‌دهد: «آنکه پول نیک را از بد جدا کند؛ سره‌گر، نقّاد، ناقد … کسی که به داد و ستد انواع پول پردازد؛ صیرفی». واژه از فارسی به اردو (sarrāf) و از آنجا به انگلیسیِ هند (shroff) رفته است — هابسن‌جابسن، ص ۸۳۱ — و از راه ترکی عثمانی به رومانیایی zaraf و صربی saraf و بلغاری sarafin (لوکوچ، ش ۱۸۶۰). شاهد حافظ («نگاهدار که قلاب شهر صرّافست») نشان می‌دهد که واژه در سدهٔ هشتم کاملاً فارسی شده بود. این گره به تردیدِ گرهٔ ۱ وابسته نیست: هر چه پیشینهٔ خودِ ریشهٔ عربی باشد، فارسی این واژه را از عربی گرفته است. حکم: ادعای نورایی درست است.\",\n \"sources\": [W+\"%D8%B5%D8%B1%D8%A7%D9%81\"],\n \"ref_check\": [\n   {\"ref\": \"MON:2144\", \"status\": \"supports\", \"note\": \"Moʿin s.v. صرّاف (MON_part1.txt line 89341): «صراف: [ع.] (ص.) آنکه پول نیکـ را از بد جدا کند؛ سره‌گر، نقاد ناقد. (ف.) کسی که به داد و ستد انواع پول پردازد. صیرفی.» The tag [ع.] = Arabic is Nourai's arrow #1 → #2. (Position is right too: the entry sits ~17 columns before صلیب at Nourai's MON:2161, matching the 2144/2161 gap; the OCR carries no page numerals, so the page itself is unverified.)\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"s.v. صرّاف\", \"stance\": \"supports\", \"note\": \"«[ع.] … آنکه پول نیک را از بد جدا کند؛ سره‌گر، نقاد» — Arabic loan, and the assayer sense.\"},\n   {\"src\": \"HJB\", \"where\": \"s.v. SHROFF, p. 831\", \"stance\": \"supports\", \"note\": \"'A money-changer, a banker. Ar. ṣarrāf, ṣairafī, ṣairaf' — with the Indo-Persian chain that carried the Persian word to English.\"},\n   {\"src\": \"LKT\", \"where\": \"no. 1860\", \"stance\": \"supports\", \"note\": \"'\"Wechsler\", tk. ebenso; hieraus rum. zaraf … serb. saraf, bulg. sarafin' — the word's spread out of Persian/Arabic.\"},\n   {\"src\": \"BQT\", \"where\": \"vol. 3, grep صراف\", \"stance\": \"silent\", \"note\": \"the Borhān does not lemmatise صرّاف (hits in BQT_v3_pages.txt are inside definitions/verse only) — an Arabic loan, outside its scope.\"}\n ]\n})\n\ne4[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Old English\", \"words\": \"seolfor\",\n \"verdict\": \"plausible\",\n \"derivation\": \"OE seolfor (also siolofr, silofr) continues Proto-Germanic *silubra- — OS silubar, ON silfr, Goth. silubr, OHG sil(a)bar — which is matched outside Germanic by Balto-Slavic *sirabras (OCS sŭrebro, OPruss. sirablan, Lith. sidãbras), Celtiberian silabur 'money' and Basque zilar, and which has displaced the inherited IE word for the metal (*h₂r̥ǵn̥tom, Lat. argentum). Nourai's arrow — the whole group borrowed from Akkadian ṣarpu 'refined silver' — is exactly what his two cited sources say: AHD s.v. silver, 'probably ultimately from Akkadian ṣarpu, refined silver, verbal adj. of ṣarāpu, to smelt, refine', and Klein p. 1445, 'All these words are prob. borrowed ult. fr. Akkad. ṣarpu'. But current handbooks do not follow them: en.wiktionary's Proto-Germanic *silubrą calls the word 'likely a Wanderwort of non-Indo-European substrate origin' and reports the Semitic comparison (with Proto-Berber *a-ẓrəf, Akkadian ṣurpum/ṣarāpum) as 'rejected by some scholars as phonologically and geographically implausible'; Kroonen and Etymonline give simply 'uncertain origin', Etymonline not mentioning Akkadian at all, and Buck (§9.65) posits only 'some common source in Asia Minor'. Two further reservations about the chart as drawn: it runs Akkadian straight to Old English, skipping Proto-Germanic *silubra- and the Balto-Slavic/Iberian members through which any such loan would have had to pass; and the gloss 'silver coin' is too narrow — OE seolfor is 'silver, the metal', with 'money, coin' only a derived sense.\",\n \"derivation_fa\": \"seolfor (و گونه‌های siolofr، silofr) در انگلیسیِ کهن دنبالهٔ ژرمنیِ آغازینِ *silubra- است — ساکسونیِ کهن silubar، نورسِ کهن silfr، گوتی silubr، آلمانیِ علیای کهن sil(a)bar — که بیرون از ژرمنی با بالتواسلاویِ *sirabras (اسلاویِ کلیسایی sŭrebro، لیتوانیایی sidãbras)، کِلتی‌ایبریِ silabur و باسکیِ zilar همسان است و جای واژهٔ اصیلِ هندواروپاییِ این فلز (*h₂r̥ǵn̥tom، لاتینی argentum) را گرفته است. پیکانِ نورایی — وام‌گیریِ همهٔ این گروه از اکدیِ ṣarpu «نقرهٔ پالوده» — همان است که هر دو مأخذِ خودِ او می‌گویند: AHD «احتمالاً سرانجام از اکدیِ ṣarpu» و کلاین ص ۱۴۴۵ «همهٔ این واژه‌ها احتمالاً سرانجام از اکدیِ ṣarpu وام گرفته شده‌اند». اما مرجع‌های امروزی این را نمی‌پذیرند: ویکی‌واژه در مدخلِ *silubrą آن را «به احتمال زیاد واژه‌ای سرگردان با خاستگاهِ زیرلایه‌ایِ غیرهندواروپایی» می‌خواند و مقایسهٔ سامی را «از نظر آوایی و جغرافیایی ناپذیرفتنی» نزد شماری از پژوهشگران گزارش می‌کند؛ کرونن و اتیمآنلاین تنها «خاستگاهِ نامعلوم» می‌نویسند و باک (§۹.۶۵) فقط «سرچشمه‌ای مشترک در آسیای صغیر» را احتمال می‌دهد. دو ایرادِ دیگر بر نمودار: نورایی اکدی را یکراست به انگلیسیِ کهن می‌رساند و *silubra-ی ژرمنیِ آغازین و اعضای بالتواسلاوی/ایبری را که هر وام‌گیری ناچار از میان آن‌ها گذشته است نادیده می‌گیرد؛ و معنیِ «سکهٔ نقره» تنگ‌تر از واقع است، زیرا seolfor یعنی «نقره (فلز)» و معنیِ «پول/سکه» در آن ثانوی است. حکم: با احتیاط پذیرفتنی است؛ پژوهشِ امروزی آن را قطعی نمی‌داند.\",\n \"sources\": [W+\"Reconstruction:Proto-Germanic/silubr%C4%85\", \"https://www.etymonline.com/word/silver\", \"https://www.ahdictionary.com/word/search.html?q=silver\"],\n \"ref_check\": [\n   {\"ref\": \"AHD:1206\", \"status\": \"supports\", \"note\": \"AHD s.v. silver: '[Middle English, from Old English siolfor, seolfor, probably ultimately from Akkadian ṣarpu, refined silver, verbal adj. of ṣarāpu, to smelt, refine; see ṣrp]' — the arrow as drawn, with AHD's own hedge 'probably'. (Printed page 1206 not inspectable: archive.org's New College scan is access-restricted.)\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"p. 1445 s.v. silver\", \"stance\": \"supports\", \"note\": \"'All these words are prob. borrowed ult. fr. Akkad. ṣarpu, \"silver\", lit. \"refined silver\", which is rel. to ṣarāpu, \"to refine, smelt\"'.\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat, s.v. Silver (SKT.txt line 17274)\", \"stance\": \"partial\", \"note\": \"OCR-damaged, but Skeat gives 'Silver. (E.) A.S. [seolfor] … Goth. silubr; Rus[s. serebro] … Lith. sida[bras]' and only a tentative 'Perhaps named fro[m] … sidus, a star' — no Semitic source; an older guess now abandoned.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck §9.65, p. 611\", \"stance\": \"partial\", \"note\": \"groups OE siolfor/seolfor with OHG sil(a)bar, OPruss. sirablan, Lith. sidabras, ChSl. sŭrebro as from a common source '…in Asia Minor' — a shared non-IE origin, but Akkadian is not named.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 IE-roots appendix\", \"stance\": \"silent\", \"note\": \"no root for the Germanic silver-word; the appendix's only 'silver' root is arg- 'the shining or white metal' (Pok. 64), which gives argentum, not seolfor.\"}\n ]\n})\n\ne4[\"nodes\"].append({\n \"id\": 4, \"lang\": \"English\", \"words\": \"silver\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Modern English silver is the regular continuation of OE seolfor through ME silver/selver/sylver: the OE trisyllabic siolofr/seolfor was reduced to two syllables with syncope of the medial vowel, the OE intervocalic voiced allophone of /f/ came to be written v from Middle English on, and the final -or weakened to -er. Klein p. 1445 gives 'ME. silver, fr. OE. seolfor'; AHD gives 'Middle English, from Old English siolfor, seolfor'; Skeat and Buck (ME sylver > NE silver) agree. The node is uncontroversial; the empty refs field costs nothing, since the parent's KLN:1445 covers this step too.\",\n \"derivation_fa\": \"«silver» در انگلیسیِ امروز دنبالهٔ قاعده‌مندِ seolfor انگلیسیِ کهن است که از راهِ انگلیسیِ میانه (silver/selver/sylver) رسیده: صورتِ سه‌هجاییِ siolofr/seolfor با افتادنِ واکهٔ میانی دوهجایی شده، گونهٔ واک‌دارِ /f/ میان‌واکه‌ای از انگلیسیِ میانه به بعد v نوشته شده و پایانهٔ ‑or به ‑er سست شده است. کلاین (ص ۱۴۴۵) «ME. silver, fr. OE. seolfor» و AHD «Middle English, from Old English siolfor, seolfor» می‌نویسند و اسکیت و باک نیز همین را می‌آورند. این گره بی‌مناقشه است و نبودِ ارجاع در نمودار زیانی ندارد، زیرا ارجاعِ گرهٔ مادر (KLN:1445) همین گام را نیز پوشش می‌دهد. حکم: ادعای نورایی درست است.\",\n \"sources\": [\"https://www.etymonline.com/word/silver\", \"https://www.ahdictionary.com/word/search.html?q=silver\"],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the chart gives no reference for this node; the step is covered by the parent's KLN:1445 ('ME. silver, fr. OE. seolfor') and by AHD's 'Middle English, from Old English siolfor, seolfor'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"p. 1445 s.v. silver\", \"stance\": \"supports\", \"note\": \"'silver, n. — ME. silver, fr. OE. seolfor, siolofr, silofr'.\"},\n   {\"src\": \"SKT\", \"where\": \"s.v. Silver\", \"stance\": \"supports\", \"note\": \"Skeat marks the word '(E.)' = native English and starts from 'A.S. [seolfor]'.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck §9.65\", \"stance\": \"supports\", \"note\": \"the column prints the chain 'OE siolfor, seolfor / ME sylver / NE silver'.\"}\n ]\n})\n\ndata[\"entries\"].append(e4)\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-430.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(data, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-430.py && python3 -m json.tool data/verification/page-430.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 430",
 "description": "Write and validate page-430.json"
}
```


### [2026-09-14T01:38:32.241Z] TOOL RESULT

```
Exit code 1
  File "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-430.py", line 159
    {"ref": "KLN:1445", "status": "supports", "note": "Klein 1966 p. 1445 (KLN_1966.txt line 35228; the page numerals 1444 and 1446 bracket it at lines 35205/35251), s.v. silver: 'ME. silver, fr. OE. seolfor, siolofr, silofr, rel. to OS. silutar, ON. silfr … Goth. silubr … All these words are prob. borrowed ult. fr. Akkad. ṣarpu, "silver", lit. "refined silver", which is rel. to ṣarāpu, "to refine, smelt", ṣarrāpu, "goldsmith", Heb. tzāraph, "he refined, smelted", tzoreph, "goldsmith, silversmith", Aram.-Syr. tzeraph, "he refined, smelted", Arab. ṣarf, "pure (wine)".' — the exact page, and it covers BOTH branches of Nourai's chart."}
                                                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
```


## [2026-09-14T01:38:40.678Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && python3 - <<'PY'\np='build-430.py'\ns=open(p,encoding='utf-8').read()\nold='''ON. silfr … Goth. silubr … All these words are prob. borrowed ult. fr. Akkad. ṣarpu, \"silver\", lit. \"refined silver\", which is rel. to ṣarāpu, \"to refine, smelt\", ṣarrāpu, \"goldsmith\", Heb. tzāraph, \"he refined, smelted\", tzoreph, \"goldsmith, silversmith\", Aram.-Syr. tzeraph, \"he refined, smelted\", Arab. ṣarf, \"pure (wine)\".\\''''\nnew='''ON. silfr … Goth. silubr … All these words are prob. borrowed ult. fr. Akkad. ṣarpu, “silver”, lit. “refined silver”, which is rel. to ṣarāpu, “to refine, smelt”, ṣarrāpu, “goldsmith”, Heb. tzāraph, “he refined, smelted”, tzoreph, “goldsmith, silversmith”, Aram.-Syr. tzeraph, “he refined, smelted”, Arab. ṣarf, “pure (wine)”.\\''''\nassert old in s, 'not found'\ns=s.replace(old,new)\nopen(p,'w',encoding='utf-8').write(s)\nprint('patched')\nPY\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-430.py && python3 -m json.tool data/verification/page-430.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 430",
 "description": "Patch script, rebuild and validate"
}
```


### [2026-09-14T01:38:41.991Z] TOOL RESULT

```
Exit code 1
patched
  File "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-430.py", line 163
    {"src": "LKT", "where": "Lokotsch no. 1860 s.v. Ar. ṣarrāf", "stance": "supports", "note": "'[Letzten Endes von ass. ṣarpu "Silber", eigentlich "das Geläuterte" vom Vb. ṣurrupu "läutern, schmelzen", hieraus syr. ṣarrāpā, ar. ṣairaf "Geldwechsler", vgl. ZAkkFW 59]' — the Akkadian → Syriac → Arabic route of the money-changer word, i.e. Nourai's Semitic branch."},
                                                                                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
```


## [2026-09-14T01:39:19.472Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && python3 - <<'PY'\np='build-430.py'\ns=open(p,encoding='utf-8').read()\nterms=['silver','refined silver','to refine, smelt','goldsmith','he refined, smelted',\n 'goldsmith, silversmith','pure (wine)','Silber','das Geläuterte','läutern, schmelzen',\n 'Geldwechsler','Wechsler','a goldsmith','He shall sit as a refiner and purifier of silver',\n 'money changer','he changed money','he turned','the refined']\nn=0\nfor t in terms:\n    a='\"%s\"'%t; b='“%s”'%t\n    n+=s.count(a)\n    s=s.replace(a,b)\nopen(p,'w',encoding='utf-8').write(s)\nprint('replaced',n)\nPY\npython3 build-430.py 2>&1 | tail -5",
 "description": "Replace inner quotes and rerun"
}
```


### [2026-09-14T01:39:20.765Z] TOOL RESULT

```
replaced 25
  File "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-430.py", line 223
    "id": 4, "lang": "English", "words": “silver”,
                                         ^
SyntaxError: invalid character '“' (U+201C)
```


## [2026-09-14T01:39:25.779Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && python3 - <<'PY'\np='build-430.py'\ns=open(p,encoding='utf-8').read()\ns=s.replace(': “silver”,', ': \"silver\",')\ns=s.replace(': “silver”\\n', ': \"silver\"\\n')\nopen(p,'w',encoding='utf-8').write(s)\nPY\npython3 build-430.py 2>&1 | tail -5",
 "description": "Fix delimiter and rerun"
}
```


### [2026-09-14T01:39:26.885Z] TOOL RESULT

```
written
```


## [2026-09-14T01:39:29.417Z] TOOL CALL #63: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-430.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 430",
 "description": "Validate JSON and run verify_check"
}
```


### [2026-09-14T01:39:30.629Z] TOOL RESULT

```
JSON OK
nodes verified: 9/9
node verdicts: {'confirmed': 7, 'plausible': 2}
root verdicts: {'confirmed': 3}
ref checks: {'supports': 8, 'partial': 1, 'not_checked': 1}
books consulted: {'supports': 16, 'silent': 11, 'partial': 4, 'contradicts': 1} | by book: {'MON': 4, 'BQT': 4, 'PHD': 3, 'KLN': 3, 'HRN': 2, 'FVQ': 2, 'LKT': 2, 'HJB': 2, 'SKT': 2, 'SYN': 2, 'AFA': 1, 'TAD': 1, 'ARY': 1, 'SOD': 1, 'AKD': 1, 'AHD': 1}
```


## [2026-09-14T01:39:37.105Z] TOOL CALL #64: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/page-430.json'))\nfor e in d['entries']:\n    print(e['entry'], e['root'], e['verdict'], '| nodes:', [(n['id'],n['words'],n['verdict']) for n in e['nodes']])\n    assert e.get('note_fa')\n    for n in e['nodes']:\n        assert n.get('derivation_fa') and n.get('ref_check') and n.get('consulted'), n['id']\nprint('all fields present')\n\" && ls -la data/verification/sources/refs/ocr/BQT/1287.* 2>/dev/null",
 "description": "Sanity-check output fields"
}
```


### [2026-09-14T01:39:38.188Z] TOOL RESULT

```
0 Salîbâ confirmed | nodes: [(1, 'čalîpâ', 'confirmed'), (2, 'salîb', 'confirmed'), (3, 'salîb', 'confirmed'), (4, 'clyb`', 'confirmed')]
1 Šalla confirmed | nodes: [(1, 'šal 2; šalîdan', 'confirmed')]
4 Sarâpu, Sarpu confirmed | nodes: [(1, 's.r.f; sarrâf', 'plausible'), (2, 'sarrâf', 'confirmed'), (3, 'seolfor', 'plausible'), (4, 'silver', 'confirmed')]
all fields present
-rw-rw-r-- 1 sfmqrb sfmqrb 389026 Sep 13 21:23 data/verification/sources/refs/ocr/BQT/1287.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3756 Sep 13 21:23 data/verification/sources/refs/ocr/BQT/1287.txt
```


## [2026-09-14T01:39:58.281Z] AGENT

Page 430 verified. `data/verification/page-430.json` written; `verify_check.py 430` reports 9/9 nodes, 0 PROBLEM lines.

**Counts** — roots: 3 confirmed (2 redirect entries, `Sam`→`Sem 2`, `Šamšěr`→`Šfšyr`, and `Sarpu`→`Sarâpu`, skipped). Nodes: 7 confirmed, 2 plausible. Ref checks: 8 supports, 1 partial, 1 not_checked. 16 supports / 4 partial / 1 contradicts / 11 silent across 16 books.

**No `disputed` or `transcription_suspect` items, and no extraction errors** — the JSON matches the chart text throughout.

Notable findings:
- **Salîbâ (Aramaic "cross")** — fully confirmed on all four arrows. Moʿin's footnote in Borhān (BQT_v2 leaf 114 ≈ p. 654) says «مأخوذ از آرامی صلیبا (عربی صلیب)», Moʿin's Farhang tags چلیپا «[آرا. صلیبا]», and Gharib no. 3202 p. 126 gives Sogdian `clyb' ©<Syr.` — SOD:126 is exact. Worth flagging for the owner: the *printed Borhān text itself* says the reverse («و صلیب معرب چلیپاست»), and Fraenkel (AFA p. 272) and Vollers (via Jeffery FVQ p. 197) derive Aramaic ṣlībā from Persian چلیپا. Nourai follows Moʿin, which is the modern view; I recorded the dissent as `contradicts`/`partial` consults rather than downgrading the verdict.
- **Two `plausible` nodes, both under Akkadian Sarâpu/Sarpu:**
  - #1 Arabic `s.r.f / sarrâf` — Zimmern (AKD p. 27), Lokotsch no. 1860 and Hobson-Jobson s.v. SHROFF all support the Akkadian→Syriac→Arabic route, but Nourai's gloss "to purify silver" conflates ṣirf "pure, unmixed" (Klein's actual Arabic reflex) with everyday ṣarafa "to turn, exchange"; Klein himself (p. 1439) derives ṣarrāf from ṣarafa "he turned".
  - #3 Old English `seolfor` — AHD (verbatim: "probably ultimately from Akkadian ṣarpu … verbal adj. of ṣarāpu") and Klein p. 1445 print exactly Nourai's claim, but Wiktionary/Kroonen call *silubrą a non-IE Wanderwort and report the Semitic comparison "rejected by some scholars as phonologically and geographically implausible"; Etymonline omits Akkadian entirely. Also the chart jumps Akkadian → OE, skipping Proto-Germanic, and glosses seolfor "silver coin" (too narrow).
- **SAP:818** (Sayyāḥ) is the page's only unreachable reference — no digital copy exists; the Arabic šalla/ašall content was corroborated from Wiktionary and Moʿin's footnote at BQT:1287 instead.
- Minor: the Moʿin OCR on disk has no page markers, so MON:1310 / 2144 / 2161 were verified by entry content, not by page number (the 2144→2161 gap does match the صراف→صلیب distance).

8 web sources archived via `fetch_source.py`; BQT p. 1287 cached under `data/verification/sources/refs/ocr/BQT/`.
