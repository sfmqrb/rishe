# Verification process log — verify-page-140


## [2026-09-05T20:08:11.725Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 140 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-140.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-140.json. Write /home/sfmqrb/git/rishe/data/verification/page-140.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 140` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T20:08:13.684Z] AGENT

I'll start by reading the agent instructions.


## [2026-09-05T20:08:14.414Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T20:08:14.428Z] TOOL RESULT

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


## [2026-09-05T20:08:14.604Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-140.txt"
}
```


### [2026-09-05T20:08:14.623Z] TOOL RESULT

```
1	=== PDF page 140 (book page 110) ===
2	--- entry 0 ---
3	ROOT Domu -> redirect to Dem
4	--- entry 1 ---
5	ROOT [Indo-European] Dous : arm  (refs POK:226)
6	#1 (parent #0) [Avestan] refs=POK:226 | daoš : shoulder
7	  #2 (parent #1) [Persian] refs=BQT:898; HRN:130; POK:226 | dŭš «دوش ۲» : shoulder
8	--- entry 2 ---
9	ROOT Drap -> redirect to Der 1
10	--- entry 3 ---
11	ROOT Drapses -> redirect to Der 1
12	--- entry 4 ---
13	ROOT [Greek] Drassoman : as much as one can hold in the hand, later it was used as a unit of weight and finally a coin  (refs FVQ:129)
14	#1 (parent #0) [Greek] refs=FVQ:129 | draxmon, draxmě : a coin, also a unit of weight | NOTE: This may be from a Semitic root
15	  #2 (parent #1) [Arabic] refs=TAD:27 | derham : a coin and also a unit of weight. | NOTE: This is possibly from Pahlavi (FVQ:130).
16	  #3 (parent #1) [Pahlavi] refs=FVQ:130; MON:1513 | dram, diram : a silver coin, also a unit of weight
17	    #4 (parent #3) [Persian] refs=BQT:840 | deram «دِرَم» : a coin | extra: دِرهَم
18	--- entry 5 ---
19	ROOT [Indo-European] Dregh : unwilling  (refs WLD:821)
20	#1 (parent #0) [Avestan] refs=WLD:821 | drigu, dregu, driwi 2 : poor
21	  #2 (parent #1) [Pahlavi] refs=BRT:849 | driyôš : poor
22	    #3 (parent #2) [Persian] refs=BQT:846; HRN:124; KLN:431 | darvîš «درویش» : poor | extra: درویش ، دریوز ، دریوزگی | NOTE: TAD:27 suggests "darvîsh" is a distorted form of Persian "dar pîsh : at the door, beggar". BQT:846 does not agree with this derivation.
23	--- entry 6 ---
24	ROOT Drep -> redirect to Der 1
25	--- entry 7 ---
26	ROOT Drop -> redirect to Der 1
27	--- entry 8 ---
28	ROOT Drtis -> redirect to Der 1
29	--- entry 9 ---
30	ROOT Drtos -> redirect to Der 1
31	
```


## [2026-09-05T20:08:17.760Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/extracted/batch/page-140.json",
 "description": "Read source JSON for page 140"
}
```


### [2026-09-05T20:08:17.802Z] TOOL RESULT

```
{
  "pdf_page": 140,
  "book_page": 110,
  "entries": [
    {
      "root": {
        "name": "Domu",
        "redirect": "Dem"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Dous",
        "lang": "Indo-European",
        "refs": "POK:226",
        "gloss": "arm"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:226",
          "words": [
            {
              "translit": "daoš",
              "gloss": "shoulder",
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
          "refs": "BQT:898; HRN:130; POK:226",
          "words": [
            {
              "translit": "dŭš",
              "gloss": "shoulder",
              "script": "دوش ۲"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Drap",
        "redirect": "Der 1"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Drapses",
        "redirect": "Der 1"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Drassoman",
        "lang": "Greek",
        "refs": "FVQ:129",
        "gloss": "as much as one can hold in the hand, later it was used as a unit of weight and finally a coin"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Greek",
          "refs": "FVQ:129",
          "words": [
            {
              "translit": "draxmon, draxmě",
              "gloss": "a coin, also a unit of weight",
              "script": null
            }
          ],
          "script_extra": null,
          "note": "This may be from a Semitic root",
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Arabic",
          "refs": "TAD:27",
          "words": [
            {
              "translit": "derham",
              "gloss": "a coin and also a unit of weight.",
              "script": null
            }
          ],
          "script_extra": null,
          "note": "This is possibly from Pahlavi (FVQ:130).",
          "quote": null
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "FVQ:130; MON:1513",
          "words": [
            {
              "translit": "dram, diram",
              "gloss": "a silver coin, also a unit of weight",
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
          "lang": "Persian",
          "refs": "BQT:840",
          "words": [
            {
              "translit": "deram",
              "gloss": "a coin",
              "script": "دِرَم"
            }
          ],
          "script_extra": "دِرهَم",
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Dregh",
        "lang": "Indo-European",
        "refs": "WLD:821",
        "gloss": "unwilling"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "WLD:821",
          "words": [
            {
              "translit": "drigu, dregu, driwi 2",
              "gloss": "poor",
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
          "lang": "Pahlavi",
          "refs": "BRT:849",
          "words": [
            {
              "translit": "driyôš",
              "gloss": "poor",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:846; HRN:124; KLN:431",
          "words": [
            {
              "translit": "darvîš",
              "gloss": "poor",
              "script": "درویش"
            }
          ],
          "script_extra": "درویش ، دریوز ، دریوزگی",
          "note": "TAD:27 suggests \"darvîsh\" is a distorted form of Persian \"dar pîsh : at the door, beggar\". BQT:846 does not agree with this derivation.",
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Drep",
        "redirect": "Der 1"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Drop",
        "redirect": "Der 1"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Drtis",
        "redirect": "Der 1"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Drtos",
        "redirect": "Der 1"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-05T20:08:18.406Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T20:08:18.446Z] TOOL RESULT

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


## [2026-09-05T20:08:30.239Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re,io,os\ndef page(f,n):\n    d=open(f,encoding='utf-8',errors='replace').read()\n    ps=d.split('\\f')\n    print(f, \"pages:\",len(ps))\n    print(ps[n-1][:3000])\nEOF\ngrep -n \"dous\" POK_full.txt | head -40",
 "description": "grep POK for dous"
}
```


## [2026-09-05T20:08:31.772Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources; python3 -c \"\nimport json;d=json.load(open('refs_online.json'))\nfor k in ['POK','WLD','BRT','HRN','KLN','BQT','FVQ','MON','TAD','HUB','PHD','ARY']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:600]);print()\n\"",
 "description": "Read refs_online entries"
}
```


### [2026-09-05T20:08:33.028Z] TOOL RESULT

```
1227:Greek odous, Armenian atamn, cf. English tooth, Latin dens, Sanskrit dantah. 
2857:master ', maybe also Tti-h\. 'plague, need'; gr. aiv6(; 'tremendous'; 
23339:Root / lemma: dous- 
23344:Root/ lemma: dous-\ "arm' derived from an archaic root *^^e:/5'hand, arm' (see below). 
23352:{*dous-nt-s). Gen. o'oa/'arm'; Latvian pa-duse {zero grade) ' Achselhohle; Busen des 
23362:Root / lemma: dous-\ "arm' derived from an archaic root *^/;ef/5"hand, arm' (see below). 
23374:The key link between Root/ lemma: dous- {* gheus-): "arm' derived from an archaic root 
41440:acymr. Jud-gual, abret. lud-uuar tremendous fight '; this Jud-{= iud^ became later in 
41665:tremendous fight ') 
64979:A common satem Root/ lemma: dous-\ 'arm' (see above) derived from an archaic root
```


### [2026-09-05T20:08:34.710Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sou

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640", "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; insi

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it
```


## [2026-09-05T20:08:37.604Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '23335,23400p' POK_full.txt",
 "description": "Print Pokorny dous- entry"
}
```


### [2026-09-05T20:08:37.657Z] TOOL RESULT

```
Page(s): 223 



Root / lemma: dous- 
Meaning: arm 

Note: 

Root/ lemma: dous-\ "arm' derived from an archaic root *^^e:/5'hand, arm' (see below). 

But she shift gh- > £/- is a unique Old pers., Baltic, celt., Illyrian-alb.. 

Material: Old Indie dos-n. (m.). Gen. dosnah^ forearm, arm, lower part of the forefoot with 

animals', Avestan daos- m. ' upper arm, shoulder', npers. f/ds "shoulder'; Old Irish doe 

{*dous-nt-s). Gen. o'oa/'arm'; Latvian pa-duse {zero grade) ' Achselhohle; Busen des 

Kleides '; sloven, pazduha, pazdiha besides pazuha, paziha 'armpit', and with the same d- 

loss (ein Erklarungsversuch by Berneker233 f.) Old Bulgarian etc pazucha'Koknoc;'. 



Note: 

Root / lemma: dous-\ "arm' derived from an archaic root *^/;ef/5"hand, arm' (see below). 

But she shift gh- > d-\sa unique Old pers., Baltic, celt., Illyrian-alb.. 

Two other roots, respectively Root/ lemma: ghesor-1, ghesr-: "hand' and Root/ lemma: 

ghesto-2\ "hand, arm' derived from an extended archaic root gheus+ reduced form of the 

common PIE suffix variants -tar, -ter, -tra, -tre. : Old Indie hasta-hm. "hand', Avestan 

zasta-. Old pers. dasta- ds.; 

The key link between Root/ lemma: dous- {* gheus-): "arm' derived from an archaic root 

*gheus'[^ar\d, arm' and Root /lemma: ghesor-1, ghesr- {* gheus-): hand' and Root/ 

lemma: ghesto-2 {* gheus-): "hand, arm' are Baltic : Latvian pa-duse {zero grade) " armpit ' 

: Lithuanian pa-zaste, pa-zastisi. " place under the arm, armpit '. 

Note: common Baltic-lllyrian gh- > z: Old pers., Avestan, lllyrian- alb. - celt, gh- > z, d. 

References: WP. I 782, Trautmann 64. 
Page(s): 226 

Root / lemma: do- : da-, also do-u- : deu- : du- 
Meaning: to give 

Grammatical information: (perfective) Aoristwurzel with secondary present di-do-mi. 
Material: Old Indie da-da-ti {kox . a-da-m. Opt. deyam. Put. dasyati, Aor. Med. adita= gr. 
£5oTO, Inf. damane :<^x. 56p£vai, compare Latin daminr\\3x\d over, deliver, give up, 
render, furnish, pay, surrender', whether originally infinitive) "gives' (pali. dinnaio a present 
*di-da-ti), (under the influence of common Celtic -ns-, -nt- > -nn-), Avestan dadaitids.. Old 
pers. Imp. dadatuv^ he should give '; root nouns Old Indie da[s] astu^ be a giver '; Infin. 
datum {: Latin Supin. datum); participle oV/a-/? (uncovered), secondary datta-h, zero grade 
in a-t-ta-h, pra-t-ta-h ' devoted' , ablaut, in tva-data-h' you gave from ', Avestan data-; to 
Put. Old Indie dasyam/{: Lithuanian duosiu) s. Schwyzer Gr. Gr. I 788''''; 

Armenian ta-m^do', ta-m/( "we hand over, deliver, give up, render, furnish, pay,
```


## [2026-09-05T20:08:38.892Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"drigu\\|driyo\\|driyu\\|dryw\" BRT.txt | head -30; echo ---; grep -n -i \"dregh\\|dhregh\" POK_full.txt | head -20",
 "description": "grep BRT for drigu and POK for dregh"
}
```


### [2026-09-05T20:08:38.958Z] TOOL RESULT

```
20111:•  j.  marzdikavas't«ma-  Adj.  'der  am meisten  Erbarmen,  Mitleid  haf ;  'i»ma  (als AP.)  ^räyd.driyut^ma  A.J.  4.
---
22764:"carve, hit, gehen' etc, Latvian drazt6s.\ see below dregh-1, 
23555:Root / lemma: dregh- 
23577:Root/ lemma: tr-eu-d-\ "to press, push, * displeasure' derived from Root/ lemma: dregh-: 
87449:Root/ lemma: tr-eu-d-\ 'to press, push, * displeasure' derived from Root/ lemma: dregh-:
```


## [2026-09-05T20:08:43.406Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '23550,23600p' POK_full.txt",
 "description": "Print Pokorny dregh- entry"
}
```


### [2026-09-05T20:08:43.484Z] TOOL RESULT

```
References: WP. I 814 ff., WH. I 266, 360 ff., 371 f., 861, Schwyzer Gr. Gr. I 6868, 722, 
741 , 794, 806 ff., Trautmann 56 ff. 
Page(s): 223-226 

Root / lemma: dregh- 
Meaning: unwilling, displeased 
Note: or perhaps originally "be slack, tough'? 

Material: Gothic //-/go "mourning, grief, repulsion'. Old Norse tregim. "mourning, grief, 
hindrance ', tregr^ unwilling, averse ', treginn^ grieving ', Old English tregam. "mourning, 
grief, affliction '; Old Saxon tregom. "pain', fregan {on\y Inf.) with Dat. "be afflicted ', Middle 
Dutch tregen' lose the courage ', Old Norse trega= Old English //"e^/a/? "afflict, sadden'; 
compare with a probably old concrete meaning " zahe, zahe haftend ' Norwegian Dialectal 
treg a\so " persistent, firm ', /Ae^e "tough fibre, filament, sinew, hard skin', Swedish tragen^ 
fatigueless '; lengthened grade Old High German tragi^\6\e, slow, querulous ', Old Saxon 
trag^es/W, bad'. Old English fragf. " affliction, wickedness ', Old Saxon Old High German 
tragrf. " sluggishness, displeasure '; 

Lithuanian dryz-tu, drizau, o'/vz// "faint, languid, slack become' (Buga Kalba ir. s. 219), 
drizinti ^s\ack make'; to Lithuanian /vcompare Hirt Indo Germanic Gr. II 83. [common 
lllyrian-Baltic -gh- > -0'- shift] 

Maybe alb. //le//? "castrate, clip' [common alb. -g > -//? shift] (see below) 

Note: 

Root/ lemma: tr-eu-d-\ "to press, push, * displeasure' derived from Root/ lemma: dregh-: 

"unwilling, displeased' [common lllyrian-Baltic -gh- > -d-, lllyrian alb. -g > -th. 

References: WP. I 821 f., Persson Beitr. 46 f. 

Page(s): 226-227 



Root / lemma: dre- : dra-, extended dr-em- 

Meaning: to sleep 

Material: Old Indie drati, draya-ti, -/e "asleep", n/'-dra 's\eep'] in addition zero grade ni-drita- 

/7 'sleeping, dozed off; 

Armenian tartam^s\o\N, sleepy ' {*der-d-, Pedersen KZ. 39, 416); 

gr. horn. Aor. sSpaGov ( *e-dr-6^-om), new sSapGov " slept ', secondary KaraSapGavu) " 
dozed off '; 

Latin dorm/d's\eep, drowse ' {*drm-Tid)\
```


## [2026-09-05T20:08:44.283Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"driju\\|drigu\\|driyu\\|drigav\\|dr6gu\\|dregu\" BRT.txt | head -30",
 "description": "grep Bartholomae for drigu"
}
```


### [2026-09-05T20:08:44.335Z] TOOL RESULT

```
14140:•  j.  drij-av-,  g.  drigav-  :  g.  *dr^u-'^  Adj. (fem.  j.  rfrJrr-)" 'arm,  bedürftig,  schwach': yat  iprsnaoiti  'yaos  havat.masS (sA.)  manS ya^a  ..Y.lO.  13:13;  —yim  *'yBsat  (HS.) *a^.tial^  xbayäti  Yt/o.  84;  —  *'yaos asl>.tkaisaAe  P.  44;  —  ^rJySidyai  (sd.) •gäm  yüwt/lkfm  H.34-1;  —  sraoiB  'yäm 'krijß.t?ms  isA.)  \i..it.y,  —  *'yüm^n  °rT- vTmca  P.  26;  —  ys  -fagim  **rlvayasla " amaval  nmän>m  harnJästi  \.5~.io;  - tat  mäsdä  tavä  x/t^rtm  ya  .'r^hjyöi  däfij 'gaove*^  vahyg  "dein,  o  M.,  ist  die  Herrsch-
20111:•  j.  marzdikavas't«ma-  Adj.  'der  am meisten  Erbarmen,  Mitleid  haf ;  'i»ma  (als AP.)  ^räyd.driyut^ma  A.J.  4.
```


## [2026-09-05T20:08:54.708Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR>=14100 && NR<=14160' BRT.txt | head -80",
 "description": "Print Bartholomae context around drigav"
}
```


### [2026-09-05T20:08:56.611Z] TOOL RESULT

```
j.  dräjöyeidm  F.JJ:  lies  dräjyö  iyeillm.
•  j.  dräjiätsm  Adv.  'am  längsten,  so lang  als  möglich' :  yahmi  zT  käcit  tanunqm dr°  häme  mal~i:aifie  miisnai  "auf  dass nämlich  in  dieser  selben  Wohnung  jede Person  so  lang  als  möglich  verweile"  Y. 16.  10.
ASn.  aus  'lA-^/uiW- Adj.,  Superl.  im/awyii-. — Vgl,  *dräJyS.  —  ai.  vgl.  draghiflha-  Adj.  — Pfi. :  dräilar.
•  j.  *dräjyö'*  Adv.  'weiter,  auf  grössere Entfernung':  nBtl  tl  ahmäi  dr"  *iyeitJm'^ framraomi  (sd.)  .  ,  yqm  .  .  äfrltlm  yünat haca  .  .  yaha  .  .  P.33.
ASn.  aus  'dräjyah-  Adj..  Kompar,  zu  dar^ya-. —  Vg].  dräjüta'.  —  mp.dräi'\  np.  dirät*). — Pü.!  drnidndtk  (ar-i).  —  ')  Hda.  dräj& yeüim.  —  ä)  Eig.  Kompar.,  wie  mp.  veh,  np. bih  uara.  —  3}  Vgl  lu  draljistB.lima..
•  j.  drSd-a-  m.  EN.  emes  Gläubigen: '^ahe  alaota . . paiti.drä^ahe . .  Yt,y,i09.
Wohl  Kuriname;  eig.  Bed.?
•  g.  *dragu-däyah- '>  Adj.  (auch  fem,) 'für  den,  die  Armen  sorgend':  apasca  va .  .  ag»nyä  (sd.)  'yaahB  (APf.)  vlspB.paitXs Y.38.  5.
Pü. !  drriai  dayai,  erl.:  ä/  i  aadar  fius  däii, Sü.:  äpo  yäh  anlar^aibAasthänt;  vgl.  zu  mae- taru-.    —    0  Mfa  usw.;  NA.  drig-;   t.  unter
•  g.  dragvant-,  j.  drvant-  Adj.  (fem. 'vaiti-)  'der  zur  Drug  hält  und  gehört'; I)  von  Menschen  'Genosse  der  Drug, .öri^fgläubig,  götzendienerisch,  aftergläubig,
j  glaubensfeindlich';   i)  bes.  im  Gegensatz I  zu  asavan-  (sd,,  Sp.  346  m.,  auch  filr  den »5*
dby  Google
775
dr«gvant-  I  i  a
dngvant-  n  a
776
Wortlaut  dSt);  a)  int  gAw.:  katlltSm\bStidvahyä  (sd.)  .  .  tka^B  -gva  .  .  aiäi asava  vä  'gvä  vä  virtnvaitl  (sd.)  mazyö  ränsB  \.4ff.3;  —  t/u/.sasti/ (sd.)  .  .  akä Y.ji.iy;  44-a,  46.6  (zit  7/.13.  P-50,  varanS  -gvä  *ftizvä  av^r»tS  (sd.)  Y.  45. wo   drvs),  4j.  5;    —    'gvani^tit  Y,  46.  5,;  r-  «)    i^'^t'  ^£.    von    bestimmten  dem
48.  2,  51.  9;  —  'gvSitl  Y.33. 3,  43. 4,  8, 1  Zarahustra  feindlichen  Persönlichkeiten, 4<i-^  (zit  7/.  13,  P.  50,  wo  drvaite),  47.4;  .uzw.  aa)  von  einem  Fürsten"':  y!  'gväitl —  °gvata£a  Y-JJ,  i;  —  'gvants  (NP.)  x/ahr^m  Aunaitl  (sd.)  Y.  jj.  ig;  —  ai \.4'j.^,   *j2.ii;  31.20    (s^  Volt.;    ire\  tfng    'gvh  ySng   asahyä   vaidrStig  päi  ga
verwendet  V.5. 62,  wo  drvantll);  —  al<A- xsä^rSng  dus^^adkatong  dusvalanM  dui- daHiitig  *duzmanargks  'gvots  (AP.)  Y.  4g. ii\  43- ^Si  45- T,  —  *°g^sj3Öyö  V. 30.11, 31.  14.  b)  im  jAwr.:  yat  aiava  para.- irüiyaH  .  .  tüirlm  gäma  frabarat  yB  nars alaonS  urva  anayragsna  raocBhva  nidmäl .  .  yai  'vä  ava.^mirytie  .  .  tairim  gäma frabarat  yS  nari  "vatö  urva  anayralt'va timBhva  nidalat  H.  2.  1,  15  und  19,  33; 25,  26;  —  a  dim  aoxia  p)r?sö  pourvB aiava  para.irt^yl!  iä^a  asäum  para.- irtiyS  kaka  asäum  apa.jasS  .  .  ä  dim aoxta  ptnsö  pourvB  °vS  (statt  NS.)  ava.- m^rpts  ia%a  'v5  (ys.)ava.*miryarjÄa  iaha <frM/ö(Sp.  781  m.)  apc/assU.  2.  16  und  34; —  :^ar3hanqm  hl  ^baratqm  sarpmayehi tat  näiriiayäi  .  .  asaonyai  :^ar3k>in  .  . 3?ar»kanqm  hl  ^bantqm  (sd.)  viSayäatla . .  tat  Jahikayai  . .  'vattyäi  ^ariinn  H. 2.18  und  36;  —  'vä  V.Ä6,  Vr.22.z;  — 'vaniim  Y.Ä  5,  YL/.28';  —  'vaiU  V.ig. 29;  —  'vataica  Yt.ro.  a;  —  'vatat  \t. 10.2;  —  'vatq»i'V.iS.'j6,  ig.30,'Vt3.4, 4.4,  II. 4.  2)  sonst;  a)  im  gAw.:  hyat akSyä  (sd.)  'guaitl  uitä  yS  ai'^m  dädre Y.5/.8''; — yascä  dS^Png 'gvatS  dadät"
frBntöis  (sd.)  . .  yastSnt  xidhrat . .  mBthat ".)  jyStyuS  v3  Y.  46.  4;  —  hyat  mä  'gva dldaniata  (sd.)  *ama^hg  Yjt6. 7 ;  — y3  fra- 'gvantfm  xsayB{sA.)Y.32.^; — yqm natdislam  gaihqm  'gva  baxsaiit(sd.)Y.^o. von  einem  Lehrer^':  ma  ai  at vS  'gvaiö  mq^rqscä  güsiä  säsnäscä  (sd.)  . . gaitä  y!  m'anlä  assm  *ahämMs  (sd.)  Y. 8  f.;  —  yS  mä  °gv,'i  '^wä  savä  (sd.) paitLtnti  Y.  44.  12;  —  hyat  vTsSnIä  (sd.) 'gvantsm  avB  Y._j2. 14.  b)  im  jAw.:
hB  dmB  ahm  upa.ra4}iayeiU  {sA)  yS '^vattt *'dahäiti  P.50;  —  mä  mqm  'vB  (VS.) paiti  *di^i/ Vyt.  50;  50,  ^i ;  —  iahyacü "vatqm    ara^wyö.manarthqm  .  .    Y,  6^4;
—  vUpe  *vantO  tanu.drujB  yB  ad>r)tB.tiaisB (sd.)  V. /(/.  18;  —  mairyS  'vä  bhangrB ^-  5-  3S;  Aog.  ti2i;  —  masyehe  'vats sästarsiiA.)  Y.p.  31;  Ö5.  8,  V.4.49,  2/.1, Yt.  7_J.  137;  —  masyäi  "'vaifyai  Yt.4r3;
—  *yat  nBit  viitfm  (sd.)  'vatB  tJ.54;  YL 5.38;  —  mß,rö.drujB  .  .  Aaihlm.a/ava.' janasca  'vaniB Yt  10. 38,  45;  V.J. 26,  Aog. 56';  —  'vatqm  dafvayasnanqm  V.  jp.  26, 41,  Yt.5.68,  11.6;  5.94;  —  oUmB.varioa- nqmca  °vatqm  Yl/J.  138;  —  äai  narqm •vatqm  ba7'ainti}iik.3;   —    vlspä  *janayB
j2.io"; —  nsil  >r>s.vacä  sarSm{sA.)didqs\yi  'vaitls  V.  20.10  i  —  ailm  dahäA^m  . 'gvätä  hyal..aiä  yuxta{,&A.)  Y.4i?.9";  — 'vantim  Y.().  8;  Yt.5. 109;  —  'vä  saini- antarS  vXspTng  °gvatB  haxm}ng\..\  mruyl\gäui  Yt/p.93;  —  tat  'vatö  'vatam  .  . (Sp.  134111.)  Y.49.3;  —  mit  tnzfjysi.tat  'vats  -vatyäsca  .  .Yt.11.2;  Vyt^7(?); frajylitii  (sd.)  nBit  fiuymtl  'gfasü  pairl  —  tarn  ahüm  .  .  yim  'vatqm  V.5.62;  — Y.  2(). 5;  —  yS  "'guB-dbls  a^am^m  (sd.) .  in  gAw.  Form:  vi  zl  anä  (sd.)  sarsm vädäyBitY.2g.2;  —  ksi^'gvB.dibts  xraräÜ\mruyl ya^anä  'gvätä  (IS.)  *rqxfyania  Y. rämqm  (sd.)  dantl  Y.  ^ä*.  11;  ^  kyat  12. 4.  U)  von  den  Göttern  des  Drug- *ainatih£  'gvaiff  3:>äri/2  i^jtig  ar?hayälsd.)'\g\&abens;  i)  im  gAw.:  aya  *mainiva Y.^2. 16;  —  ka'hä  asäi  drujim  dyqm\varata  yS  'gvä  aastä  virizyB  ahm  main- zastayd  (sd)  .  .  imavaiilm  sinam  dirvBi^yus  spfriistü  ".  .der  zur  JJrug  habende.,  der (sd.)  'gvasB  V.4/.14;  —  ya>rä  ««(»ywj-';  heiligste  Geist"  Y.jo.j.  2}  im  jAw.,
'gvatö  anqsat(sil.)  parä  Y.5J.7;  —  vaya.-'sv^  'ruchlos,  verrucht':  snaiäi  aiirahe bindubyS  (sd.)  did.^art^Sm  nqsa^  ^ä%r}m  '  matnySui  'vatö  .  .  vJspanqm  datvanqm *'gvB.d?byS  dSjtt.arita^byS  Y.  ^3.  6 ;  —  lä  varmyanqm^a  'vätqm  Y.  27.  i ;  Yt,  5.  2  2, 'gvatö  *mandaitg  dalnl  *fr>zaos  {sd.)  i0.i)i,  118,  13.78,  137;  —  pairi  main- haihTm  Y-ßi-  13;  4Q.  4;  —  naidä  dahySus  yaoyät  dnijat  ^varmyayäalca  *°vB.i^yJi''^ yni    säslärö    (sd.)     'gvanlB    \.  4O.  1 ;    —    .  .  pairi    'ratat  yat   anrät   mainyaoi  Yt
dby  Google
777
dr9gvant-  IH
■drug-  A
778
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
Vgl.  ai.  hirui,  Aurüi  (mit  ar.  di).     Unsicher.
•  j,  druka-"  m.  Name  einer  Krankheit, eines  Gebrechens  od.  dgl.:  paitiltätse  yas- kake  . .  mahrkahe  .  .  'kahe  V.  20.  3.
Pü. :  fehlt.  —  n  1. 4,  K  I  durtii:
•  }.,  g.  'drug-  C,  nur  Sing.  'Lüge,  Trug": at  yas  daivä  . .  akäi  (Sp.  45  m.)  mana»hB sta  a'imm  .  .  'üjasca  fiairimirt/iis'H  Y. 72.  3.        A)  insbes.  als  dogmalischer  Term.
dby  Google
779
drug-  A  I
'dnig-  Noten
780
techn.  '^Dn^,  d.  i.  'Inbegriff  dessen,  was dem  Wahren  und  Rechten  (^/a)  en^gen- gesetzt  ist,  die  rfaftische  Welt  der  Lüge und  ihre  Ordnung";  i)  bes,  im  Gegensatz zu  'a/o-  (sd.,  Sp.  230  o.,  auch  für  den Wortlaut  dSt);  a)  im  gAw.:  atca  ahmäi va/ynäi . .  mdättm  ahm  (sd.) .  .ikaisäi  (sd.) ..  'uxi  \.49-3;  —  ysi  urvamii  °ajs aiahyä  gathä  vlm»r7ncaitt  (sd.)  V.j;.  i;
```


## [2026-09-05T20:09:08.216Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"^8[45][0-9]$\\|^ *849 *$\\|^ *850 *$\" BRT.txt | head -20",
 "description": "find column 849 header in BRT"
}
```


### [2026-09-05T20:09:09.746Z] TOOL RESULT

```
15146:841
15182:843
15185:844
15225:846
15264:847
15267:848
15287:849
```


## [2026-09-05T20:09:11.472Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '15280,15330p' BRT.txt",
 "description": "Print BRT column 849 area"
}
```


### [2026-09-05T20:09:11.526Z] TOOL RESULT

```
'schwellen  (intrans.),  strotzen',  von  Milch: pipyaitm  (sbes.,  unter /yttVu^-).
mit  fra  i)  intrans,;  mit  avi  und  Akk, 'hinschwellen,  -fli essen  zu  — ',  Med:  aaat :!fannS  frapinvata  avi  zrayS  vount.kai>m Yt.  ig.  5 1 '',  3)  traps,  'schwellen  machen, zum  Gedeihen  bringen',  Akt.:  yB  yaom kärayeiti..  hB  imam  daSnam . .  frapinaoiti V.J.  31-
ai.  firniäle,  fiimrati,  pipyufl.  —  Fü.  {in  V,  3): ftäl  pänenet,  erl. ;  kus  parvart  bavtt;  s.  noch unter  pifäiah-,  —  ')  Anders  Gdn.  3Yt  29,  39 'enlkam',  VSL  2. 179  'gewann  den  Vorsprang*, DsT.  ZA.  3.  630  Wa  sc  nourrir'.
•  j.  payaohar-  m.  EN.  eines  Gläubigen: 'aharB  maxitBil  aiäotiB  des  /*.,  Sohns  des M.  .  :•  Yty.  116.
Komp.:  'payaA-+*Aar-  f.  'Flass,  Strom'  (ai.vgL lirA-  f.),  also  eig.  'der  Ströme  von  Milch  hat'{?).
•  j.  'payah-  n.  'Milch',  auch  Plur.:  *'yB F.  10  i  —  nsit  *yB  fsuta  (sd.) , .  toit  gstd . . ^■7-  77;  —  aipi.yiaurvatqm  aspayanqm^a °yar3hqm  gävayanamcä  malsinatiqmca  buz- yanqmla  hqm.vaoirinqm  la.vaoirinqm  V. 5.  5a;  —  rafu/ris  *°ySbls'^^  sfastiisca a:^ästäisca  N.57.  a)  mit  'tütrya-  Adj. 'Molke':  taitya  (sd.)  paya  bavat  aspa- yüaiea  *'xaraySaJ/a  "die  Molke  kann  von
dby  Google
849
*payah-
ipar-
«so
einer     Ross-     oder    Eselstute     stammen'
N.  67,  A)    Plur,    mit    xsaudray-   (sd.)
Name  eines  aus  Milch  hergestellten  alko- holischen Getränks,  wohl  'Kumis':  x^au- drinqm  °yat)Aam  N.  67;  66.  Undeut- lich: rafu/ris  *nairiAayS  kihrpa  nöii 'yatshs  nsit  suns  k?hrpa  'yatfho  ratufril v?hrkayä  kshrpala  'yanhaca  N.  5p; mananhs  nSit  'yar?hs  N,  6y  *'.
KompE.  —  Zum  V.  /a/-.  —  Vgl.  'payak- ai.  päyas-  n.  —  Pü. :  pem;  s.  noch  No.  3. >)  Hds. /fljv'.  —  ')  Pü.t/a,
•  j.  'payah-  Adj.  '(milchend,  Milch  sva.) Saft  gebend,  schaffend"':  maiaydizarf- ma^tt  {sd.)  'yanhim  Vr.  2.  2;  —  mailySi- zanmayehe  'yatths  Vr.  /.  2.
Vgl  'fayak-.  —  Pü.;  flmenU.  —  ')  Bed.  nach Roth  ZDMG.  34.  703.
•  j.  pav-  V.  'faulig  werden,  verwesen' Praes.  27  puya-.
yezica  alle  nasävO  friäsyatila  (sd.)  fi^e tica  Y.6.28;  —  'puyant;
a\.  puyaü,  wose.  ämiiiyun,  mp.  kaniiüiltan'i^ np.  fiüsü/an');  t.  noch  Pü.  zu  afiuyan/'  und GltPh.  1  b,  321.  —  Fä.-.fiälai.  —  D  Inkob.; vgl.  GIrPh.  /.  320,  /  b.  129.
•  j.  pavant-  Adj.  'hütend,  schirmend, schützend':  avä  °va  (NS.)  pasca  'vii  pars •vä  spa/  vT^aSa  ,  .  frä  *aähe  vJsaiti nivirS  .  .  yakmäi  .  .  Yt  10. 46.
Ableit  (mit  vanl^  aus  '"^pS^y)-  n.  Das  auf- fällige a  setzt  die  Existens  von  Fonnen  wie *kupi,  *kup3Bi  usw.,  nach  der  i-Dekt.,  voraus.
•  j.  *pavitajr-  f.  'Fäulnis,  Venvesung": cvat  antar>  *n)r3ui  aSsa  druxl  y3  nasus axtica  'ti^a  ahitica  fräsnaoiti  "wie  viel . , trifft  die  Drug  . .  mit  Krankheit,  Fäulnis und  Befleckung?"  V.5. 27,
Zum  V.  pav:  —  Vgl.  pülay;  zu  dem  sich *paviüiy'  verhalt  wie  im  Aind.  sämlay-  I.  zu sätäy-  i,  —  Pü.!  paiinjisn  'Bespiengung',  erl. : remanih.  —  i)  So  L  4,  K  1 ;  NA.  pivaf.
•  j.  'par-  V.  'gleich  machen'.  Praes.  4 psra-,  3$  (Pass.)  pairya-.
'vergleichen':  kva  iä  (föä/'j(sd.)  *pair- yeU'^  V.  ig.aj.
mit  aipi  'begleichen  (eine  Schtild)',  ohne Obj.  'Busse  tun':  Aa  hi  asti  B'ha  hä  hl asH  aptnHl  aipi.pänmnäi  ida  alaone nSil  anaipi.panmnäi  drujO  nmaw..  "..das ist  daiiir  die  Sühne  für  den  Gläubigen, der  hier  Busse  tut;  für  den  (aber),  der nicht  Busse  tut  (,  gilt  der  Spruch):  draß\ d^mämmw.  (Y.^i).  iidj"  V.  Ä  107.^
VgL  Sp>T}lay-,  anäp>ri%a-.  —  lat  vgl.^ar  Adj.  I
'gleich'.  —  Pü.  (in  V.  yp);  ku  Hält  däir  api raruiend,  erl. :  \kii)  iSn  äyiin  u  iavHit  tu  yäi, s,  No.;  (tu  V.  S):  ka  apar  pukrik  att,  erl.! ka  apta-  vicärel.  —  >)  So  nach  Jp  I,  Mr2. NA.  hat  pärayänii  (».  auch  Pü.);  doch  beachte man,  dass  kurz  lavOT  zweimal  nipätayania steht,  das  leicht /äi-iij''  vnanlasst  haben  kann. pairy'  ist  jedenfalls  die  lectio  diS".
•  j.,  g.  'par-  V.  'füllen'.  Praes.  3  'fra-^'', 1  pa/r-,  II  p)rm-;  Perf.  *pa/r-.  —  PPfP.
p?r3na'  (sbes.).
'Julien,  voll  machen' :*/r(2n/-".     a)'(einen
Wunsch)  erfüllen':  aiibyS  ptrina  i,i^lKY>
äpanäii{^A.)  käm?m  Y.  2tV.  10.        b)  '(ein
Werk)    vollständig    machen,    vollenden';
/anu.matsisd.)  sf  *aliamai  asayam  *pafre^
*yat  ..  T.iS.
mit  iam  'füllen  mit  -'  (Gen.):  yS  gTus
unihwan  Aqmpä/räiti*'>  "wer  den  Bauch
mit  Fleisch  füllt"  V.^48.
ttL  pptali,  pptiti  i  np.  anb^rad  'er  füllt  ein'.  — Pü.(iuV.3^:  ampa  diänpurr  kambärel kämak, (zu  P.):  ka  . .  kambärel,  erl.:  kuS  .  .  kart,  (lu V.  v)!  ke  pa  göit  unAwar  ö  kam  kambitit istel,  erl.!  jfr.  —  >)  la/raJ.äp-.  fra-  ist  Koinp- Form  zu  einem  al,  *purä-li.  —  »)  Them.;  ai, pfna.  —  i)  Hds.  p/rf.  —  4)  Them.
•  j.  3par-  V.  'verurteilen'.  Praes.  10 pmnav-,  27  (Pass,)  pirya-'\  —  PPfP. parita',  'pfnta',  p>Ia'.
'Jemanden  (Akk.)  zum  Verlust  von  - (Akk.)  verurteilen';  Pass.  'etwas  (Akk.) rechtskräftig  verlieren,  etwas  verwirken': puxtfmcit  (sd.)  ««  andusqm  tanUm  pir- yeHe''>  "..verwirkt  man  den  Leib"  V.4. 17; —  yö  gä'hä  asrävayS  *qsta{sA.)  va  tarS.- maiti  va  lanüm  *piryeiH  N.  .^'"'*;  42'', 45''. 7''j  —  pt^Janus  ianUm  *piryde*^^1 F.  25b;  —  ''piryäe^'i  F.  10.
mit  apa  dnwS.:  yn  ga%ä  asrsvayö  afa tansm  *piTynti^'^''*  N.42.
mit/iwV(dnwS.:/iMÄ  *Äa^ra  *q/rasruiti sl  paiti  tanüm  ^piryäte^  N.  7.
xlfrä  dnwS. :  myasdavh  ratui amyazda- vatt?m  ratunalm  yäUm  (sd.)  gaihanam frapirinaoiti  A.3.  ii^*;  10;  —  myazdava .  .  amyasdavamm  . .  ähsirim  tka^pm  /ra- pirmaoiH  ",  .  verurteilt  . .  den  I^en  zum Verlust  des  ah.  Richters"  .^._j.  12*';  — Pass.:  aaf  i^armö  frapiryäd^^ "^  V.  5.  9 PüZ.
Vgl.  MIO.  LW.  fariavorel  'vernrleilen'  (BB.7. 187)  usw.  (bei  Hbu.  AGt.  t.  22S).  —  Pü. (für  tanüm  firyiili  zu  V.,  N,,  F.);  tanäpuhr tttvit,  (für  piryiti  F.  lo):  apärf-');  Sü.  (für /rap»r>ncuiili):  viikinnayitum,    Npü.!  fari,  i/ür.
ob,Google
851  ^ar-  —  'para  II 2  c  852
/»flu  iatdoH.  —    ')  $  :68.  40.    A'"  steht  V. ' ,  g.  jpgr-  V.  'obstaie'.     Perf.  i  pa/r-.
N, /<.  —  II  Zu  J  jjj  Ko.  —  ii    Die  Worte    "ej^oa:  at  ml yaiä  bjtiävö pafrlmaiistö^'
```


## [2026-09-05T20:09:20.700Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification; grep -h -o '\"ref\": \"BRT:[0-9]*\"[^}]*' page-*.json | head -20",
 "description": "check prior BRT ref usage"
}
```


### [2026-09-05T20:09:20.752Z] TOOL RESULT

```
"ref": "BRT:598",
"ref": "BRT:598",
"ref": "BRT:667",
"ref": "BRT:653",
"ref": "BRT:345", "status": "supports", "note": "Bartholomae, AiW: the āhita- entry stands in the column block headed '345 āh- … āhūirya- 346' (archive.org altiranischeswr00bartgoog, form-feed leaf 219 of BRT.txt; the next running head on that leaf is '347 āhūirya-'). Text: '• j. āhita- Adj. \"befleckt, verunreinigt\" … KompE. — PPfP. … — Vgl. [Pü.] āhōk, np. āhū \"Sünde\".' Bartholomae therefore states in so many words that New Persian āhū 'sin, fault' and Pahlavi āhōk belong to Avestan āhita- — which is precisely the arrow Nourai draws (his cited column 345 is right, or at most one column early)."
"ref": "BRT:1862",
"ref": "BRT:755",
"ref": "BRT:755",
"ref": "BRT:208",
"ref": "BRT:862",
"ref": "BRT:862",
"ref": "BRT:968",
```


## [2026-09-05T20:09:30.912Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== HRN dos/darves ===\"; grep -n -i \"dôš\\|dôs\\|doš\\|darvēš\\|darvês\\|derwîsch\\|dervisch\\|darvîš\" HRN.txt | head -30",
 "description": "grep Horn"
}
```


### [2026-09-05T20:09:30.961Z] TOOL RESULT

```
=== HRN dos/darves ===
```


## [2026-09-05T20:09:32.164Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== PHD ===\"; grep -n -i \"driyo\\|drahm\\|dram\\|dwš\\|dōš\" PHD.txt | head -30; echo \"=== PHD_mackenzie ===\"; grep -n -i \"driyo\\|drahm\" PHD_mackenzie.txt | head -20",
 "description": "grep MacKenzie"
}
```


### [2026-09-05T20:09:32.220Z] TOOL RESULT

```
=== PHD ===
214:a-pus [' BRE] without a son, childless. ár-, v. árdan. 5 āranj "Inc | N ~] elbow.. 9-43. "Ant *a-rāst Prst'] untruth. ārāstan, ārāy- [Pstn!,^Pd- | N ~] prepare, arrange, adorn. ~ién: arrangement, adornment. a-rawüg [”/wbk!] immobile. Ard р | M?yrd, N ~] a goddess; cal. 25th day. ard [KHM A < А gm; п | N ~] flour. агаа [py | (M rd?w)] righteous, truthful. ardan, ār- [THNN-tn' < А V thn; ?l-tn'] grind, mill. ardāyīh ['i?dyh | M?rd?yyh] righteousness, rectitude. ardig [/tyk! | M ?rdyg] battle. ardikkar рук], -kl | M?rdyqr] warlike, warrior. ~ith: doing battle. arduš [”ldwš = Av. aroduš-] a degree of sin. Ardwahišt Prtwhst' | M ?rdywhyst, (N urdībihist)] Right, the second Amahraspand, guardian of fire; cal. 2nd month; 3rd day. arešk [lysk' | M ()rysk, N rašk] envy, jealousy. ~én [-yn'] envious, jealous. ārešn Pim! | M ”7ysn-, N (a)rif] cubit. aryand [?/епа | N ~] horrible. arģawān [*/gwk'*n! | N aryawān] purple. armēšt ["/myst'] inactive, infirm. ~ih: infirmity. armēšt-ģāh [-g’s] secluded place for the infirm. агбуї&п [/wdšn'] growth. ~ig [-y&!] growing, vegetable. ars Dis | M?rs, N ~] tear (drop). artēštār УЯ? | N artēšdār!] warrior. „īh: warriorhood. arus [2/00] white. arwand [wnd] swift, valiant; river Orontes. ~ih: swiftness, valour. arwés [lwys | M ?rwys, N ~] rope. arz [KSP! < А Ар; с | N ~] worth, value. Arzah [Iz h == Av. arazahi-] the eastern continent of the earth. arzan [PE < А prg’; len! | N <) millet. arzàn Plen | M *rz'n, N ~] valuable, worthy. ~ig [-yk'] worthy. ~igih: value, worth, worthiness. arzidan, arz- [?/с-уїп! | N ~] be worth. ~išn: value, worth. arziz (сус | M ?rzyz, N ~] tin, lead. —ën [-yn'] tin, leaden. ārzōg Picwk! | M'wrzwg, N àrzó] desire, lust,
314:~th: friendship, love. 140$ [dws | N ~] shoulder. 2108 [duš | N ~] last night, previous evening. dēš-, —išn, v. Ł 2 dēšīdan, !doxtan. dēšag [dwsk'] dear, loving. —ih: love. došaram [dwi?m | M dw%’rm] love. dēšastar [dušstl] west. īdēšīdan, 458- [dws-ytn!] like, love. ~ign: liking, pleasure. *došidan [dwsytn'] = *dóxtan. dēšīzap [dwsyck' | (M дох, ] dwskyzh), N —a] maiden, virgin. “АҺ: maidenhood, virginity. dówom [2wm | N ~] -second (in compound numerals). 1dóxtan, dēš- [dwhtn', dws | N ~] milk. *dóxtan, döz- [dwhtn', dwc- | N ~] sew. dóys?r [dwysl = Av. dõiðra-} eye. dēz-, v. ?dóxtan. drafš [dips | P drfš, N ~] banner. drafšīdan, drafš- [dipi-ytn! | P drfi-, N ~] 1. shine; 2. tremble. drahm [ZWZN! < А zwza | M drhm, N dir(h)am] drachm. dra(h)nāy [di(k)rd) length. dramanag [dimnk! | N dirmana] wormwood. dranģ [ding | N dirang] period, duration. dranjidan, dranj- [dInc-ytn!] speak. ~išn: speech. draxt [4/0)А | M drxt, N diraxt] tree. drày-, ~išn, v. drāyīdan. drayā(b) [dlyd?(p) | M dry?b, N darya(b)] sea. ~-bār LI | N -bàr] sea-shore. агауӣп-јбуіёп [did?n ywdsn'] one who speaks while eating. ~ih: (the sin of) speaking while eating. drayidan / drayistan, drāy- [dPd-ytn!, -stn! | M dryst, dPy-, N daráyidan] speak (daevic), chatter. —išn: chatter. drāz [dlc | N diráz] long. *drém [dlym] phlegm. driyó$ [41220 | N daryūš, darwé§] poor, needy. ~th: poverty. dró [KDBA < А kdb’; dlwb! | M drw, (N daróy)] lie, deceit. drd [SRM < A šim; dlwt! | M атта, N daród] health, well-being, prosperity, peace. dró-dadwarih [KDB A d'twblyh] false judgement. īdron [dlwn' | N dariina] bow. *drón [dlwn' | N darūn] consecrated bread, ceremony in which c.b. is used.
316:drón yaštan: consecrate the sacrificial bread. drēš [410] mark, branding; punishment. ~ag [-k!] *desolation. drēšīdan, dro$- [d/w$-ytn'] brand. drēūšom [dlwšwm] mark. droz-, v. druxtan. drózan [dlwen! | M, J drwzn] lying, liar. ^h: falsehood. drubušt [di(w)pwst'] fortress. ~ih: defence, fortification. drüdan, *drün- (HCDLWN-tn! < A У hsd | M ача, (dwr-), N durüdan, diraw-] reap, mow. drust [drw(y)st' | (M dryst), N durust] right; well, healthy. —Ih: righteous; health. drustabed [drwystpt'] chief physician. društ [dlwšt' | N durust] harsh, rough, severe. ~ih: harshness, severity. ~-Awaz, ~-éwaz [-p'c, ~yw’c] harsh-spoken. druwand [dlwnd | M drwnd] evil, sinful, unrighteous. ~īh: sin, unrighteousness. druxtan, dróz- [dlwhtn', dlwc- | M drwxt, drwz-] lie, deceive. druz [dlwe | (P drwj)] demon. айа [dwt! | M dwd, N ~] smoke. düdag [dwtk! | N —a] family. dudigar [dtykl | M dwdygr, N digar] second. duj-, = duš-. ~-daft [dwsdpt'] ill-breathing, short of breath. ~-dānāg [dwšd”7?k!] ignorant. ~-dén [dwšdyn' | M dwjdyn-] of evil religion. «=dēys*rīh [dwsdwyslyh] the evil eye. ~-gand (dtwsgnd | P dwjgnd] stinking. ~-gandih: stench. dum(b) [dwm(b') | N ~] tail. ~dmand [-'wmnd) tailed. ааг [LH YK'! < А rhyq; dul | M dur, N ~] far, distant, remote. durgar [dwlgl | N ~] carpenter. dusraw [dwslwb!] notorious, dishonoured. ^Ah : notoriety, dishonour. duš- [dws- | = M] ill-, evil-. ~īh: evil, wickedness. ~-абаһ [dw??^ Es] foolish, stupid, ignorant. ~-абаһіһ : foolishness, stupidity. ~-arz [2 ic] worthless. 7--Ca&m [-cém] envious. —-Ca$mih: envy. ~-tihr [-cyhl | M dwfcyhr] ugly, hideous.
318:^-éwüzih [-yxw'cyk | (M dwšw'cyh)) evil speech, calumny. ~+farrag [-plg | P dwéfr] unfortunate. ~-farragih : misfortune. ~-gowisn [-gwbsn'] of evil speech, ill-spoken. ~-humat [-hwmt'] evil thought. ~-hixt [-Awht' | M dwfxwptyy!] evil speech. ~-kām [-2’m] ill-will, malevolence. ~-kanig [-knyk'] hag. — kar LAT difficult. ~-kuni&n [-kwngn'] of evil behaviour, ill-doing. dušmat [dwfmt! = Av. dufmata- | M dw$mtyy!)] evil thought. dušmen [dwsm(y)n' | = M, N dušman] enemy. ~ih: enmity. „ādīh [dušmntyh | M dwkmny’dyh, J dwfmn'dy] enmity, hostility. duš-|-menišn [dwf-myntn!] of evil thought, ill-thinking. --nàm [->”m | N ~] abuse, insult. dušox [dwshw! | M dtws(w)x] hell. ~ig [-yk'] hellish. duš-pādixšā(y) [dušp*thš*(d)) evil ruler. ~th: evil rule, misrule. dušrām [dwsl())m] unhappy. ~ih: unhappiness. dušwār [2001 | M dwšw”r, № ~] difficult, disagreeable. ~ih: difficulty, trouble, misfortune. du&-|-wir [dws-wyl] evil-minded. ~-wurréyisnih [-wlwdsnyh] heresy. c-.xém [-hym] evil-natured. ~-xwadiayih [-hwt'yh] misrule. ~-xwar Lea! | N ~] = dušwār. dušxwaršt [до оной! | M dwkxw styh!] evil deed. duxt [BRTE < A brt-h; dwht' | M dwxt, N ~] daughter. ~ar [dwhtl | N ~] daughter. duz(d) [GN BA < A gnb’; dwc(t) | M dwz, N duzd] thief. ~th [dwe(d)yh] theft. duzidag [dwcytk'] stolen; intercalary (days). duzidan, duz- [dwe-yin' | N duzdidan] steal. dwārīdan / dwāristan, dwür- [dwP?l-ytn!, -stn! | M dwr-] run, move (daevic). ~išn: abode (of demons), hell. dwāzdah [dw'cdh | M dw'zdh, N duwazdah] twelve. ~ап [-’n'] the zodiac.
1689:drachm drahm.
4350:wormwood dramanag.
5360:dramanag, garmēg
5361:garmowar garmowarih *dramanag garmscr darbās drubustih drubust drafš
5376:garānīh darhandarzbed yarranidan garan yarranisn gramigih gramig grāmag drāyīdan, grāyīdan drāz, grāb draxt griy- grih dargūh garasman 1 3uriw griwag grīwbān driyos driyöšīh darigbed dilér drëm griyistan
5450:gandanag drahm! gandagih
=== PHD_mackenzie ===
2043:drahm [ZWZN' < A zwzn I M drhm, N dir(h)am] drachm.
2063:driyos [d1gwf I N dary6f, darwef] poor, needy.
6429:disobedient aburdframan, spozgar.       drachm drahm.
7144:needy astanag<>mand, driyos, niyaz.    obedience ekanagih.
7288:Pisces Mahig.                              poor driyos, skoh.
7304:poverty driyosih, niyazomandih,                privilege abarmand.
10761:drahmI                                    , ... t'      gohrag                             ,}-t'
```


## [2026-09-05T20:09:39.772Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== HRN Schulter ===\"; grep -n \"Schulter\" HRN.txt | head; echo \"=== HRN Derwisch/arm ===\"; grep -n -i \"derwisch\\|drigu\\|driyo\" HRN.txt | head",
 "description": "grep Horn German glosses"
}
```


### [2026-09-05T20:09:39.833Z] TOOL RESULT

```
=== HRN Schulter ===
4207:460. {2)%ä 'Schulter .
4208:aw. /äo, yt. 10, 71 ; 14, 29 'Schultern'.
4211:setzung von aw. /äo durch 'Schultern (man erwartet
5248:584. (^)dös 'Schulter .
5249:aw. daösa- 'Schulter (ZPGL); phlv. dös; ai. dos-,
6438:789. suft, sift 'Schulter .
6439:aw. supfi' 'Schulter ; phlv. suft; ai. rüpti- 'Schulter ;
6440:ndd. schuft (fichucht) 'Schulter (Bezzenberger, BB.
7612:'Schulter*, kurd. kuwi 'wild*.
=== HRN Derwisch/arm ===
21479:y. ddriyow 561.
```


## [2026-09-05T20:09:46.874Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'PY'\nd=open('HRN.txt',encoding='utf-8',errors='replace').read()\nlines=d.split('\\n')\nimport bisect\n# compute leaf index per line\nleaf=0\nleafof=[]\nfor l in lines:\n    leafof.append(leaf)\n    leaf+=l.count('\\f')\n    # form feeds may be inside lines\nfor n in (4207,5248):\n    print('line',n,'leaf',leafof[n-1],'printed page',leafof[n-1]-21)\nPY\nsed -n '5240,5262p' HRN.txt; echo \"---- 561 ----\"; grep -n \"^561\\.\\|561\\. \" HRN.txt | head",
 "description": "locate Horn pages and entry 561"
}
```


### [2026-09-05T20:09:48.623Z] TOOL RESULT

```
line 4207 leaf 123 printed page 102
line 5248 leaf 151 printed page 130
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
---- 561 ----
5041:561. (lerj/ä *Meer; grosser Fluss', jüd.-pors. nxni (Is. 8,
```


## [2026-09-05T20:09:52.402Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'PY'\nd=open('HRN.txt',encoding='utf-8',errors='replace').read()\npages=d.split('\\f')\nfor p in (145,146):\n    print('=== leaf',p,'printed',p-21,'===')\n    print(pages[p][:2500])\nPY",
 "description": "print Horn printed page 124"
}
```


### [2026-09-05T20:09:54.142Z] TOOL RESULT

```
=== leaf 145 printed 124 ===
— 124 —
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
und mit Spiegel, Arische Periode, 70 gr. Ooftko
'pflücken* zu vergleichen.
557. iliiröy, deröy 'Lüge; unwahr.
ap. drauga- *Lüge*; i\\^\ draoya'\ phlv. dröy, dröy,
LW. kurd, durüy; af/. daröy; bei. davöy^ drög,
n. dröy (49).
558. dnrüne 'Regenbogen'.
skr. drum- 'Bogen' (spät und selten).
bei. drm, drmuk 'Regenbogen* (85); yidg. LW.
drün,
bei. drin beweist, dass die ebenfalls überlieferte
np. Aussprache dnrüne falsch ist, vergl. Hübsch-
mann, ZDMG. 44, 555.
559. derves 'Bettler; arm', deryös (Vis und RämTn, S. 395,
Vers 8), deryös, deryöz, deryöze.
aw. vergl. driyu- 'arm*, fem. driwt- {*driyvJ-),
driwika- {?); phlv. daryöä, daryösih.
Die neupersisehen Formen sind im Einzelnen schwer
zu erklären. Auch derey 'Jammer, Elend', Grund-
bedeutung 'Mangel, Beraubtsein*, dereyä gehören nach
Nöldeke (mündliche Mitteilung) hierher.
560. derre 'Thal, Schlucht'.
aw. darenä- 'Thal, Schlucht'; Adovu, Ptolem. 6, 1
(Spiegel, ZDMG. 32, 721).
») Vergl. Fr. Müllor, WZKM. 5, 352.
=== leaf 146 printed 125 ===
- 125 —
wa/. i5ör, sar. öer.
Dazu got. dal 'Thal'; ksl. dolu 'Thar (ITorn, KZ.
32, 589 No. 26).
561. (lerj/ä *Meer; grosser Fluss', jüd.-pors. nxni (Is. 8,
23). '
ap. drayah'^) 'Meer*; aw. zrayah- 'Meer; plilv.
daryapj daryäk (Bund.), ^re; ai. jräyan-,
bei. zirih *Qnell\ zira *Meer (425).
LW. kurd. deryä; af/. daryäh; bei. darya (50);
yidg. däriyow Tluss*.
Die Form deryäb verdankt nur einer Anlehnung an
ah * Wasser ihre Entstehung. Phlv. zful ist entweder
dialektisch oder nur als ursprüngliche und dann weiter
gedrungene Umschreibung von aw. zrayah- anzu-
sehen; np. zeräh ist sicher Dialektforni.
5H2. derriden, deriden 'zerreissen*.
aw. {/'daV'^ dereta- 'spalten'; phlv. darltan bozw.
darritan ; ai. V^dar-^ ddrsi {dpuiti).
kurd. deriyän; af>'. dural; bei. dirag, dirray, n. diray,
dinay (78); sar. z-dard-änam (Caus.).
563. dix, diz, dez-) 'Burg, vergl. dizhäii-^), dlzdär (syr. LW.
n^nn).
ap. didä' Testung', vergl. ncwciduooi^' (No. 279);
aw. daf^za-; phlv. d(i)z (AV. ; Bund.); arm. vergl. dcz
•Jlaufe' (Hübschmann No. 82).
Die neupersischon Formen diz und dcz sind beide
gleich ursprünglich. Ap. dida- steht für dlöä- und
zwar entspricht das ap. d hier einem ar. fA ; in diesem
Falle wird es im Nenpersischen nicht zu y, Ascoli's
Erklärung von np. dwar 'Mauer aus ap. '^didavara-
\Stadtwair ist daher nicht wahrscheinlich, zumal die
ältere Form devar gewesen zu sein scheint, vergl.
No. 599.
») Bartholomae, ZDMa. 46, 29S No. XV.
2) Dez findet sich in einer ganzen Reilie trän soxanisch er
Ortsnamen, die Herr Prof. Nöldeke gesammelt liat und demnächst
anderswo mitteilen wird.
^) Ma\i^rr nl-Umerä.
```


## [2026-09-05T20:10:09.113Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; ls; python3 - <<'PY'\nimport re\nf='WLD_Bd1_pages.txt'\nd=open(f,encoding='utf-8',errors='replace').read()\nprint(len(d))\nidx=[m.start() for m in re.finditer(r'drigu|drīgu|dregh', d)]\nprint(len(idx))\nfor i in idx[:20]:\n    print('...', d[i-200:i+300].replace('\\n',' '))\nPY",
 "description": "grep Walde-Pokorny Bd1"
}
```


### [2026-09-05T20:10:10.838Z] TOOL RESULT

```
WLD_Bd1_1930_dli_70244_djvu.txt
WLD_Bd1_1930_dli_70244_text.pdf
WLD_Bd1_pages.txt
WLD_Bd2_1927_dli_106624_djvu.txt
WLD_Bd2_1927_dli_106624_text.pdf
WLD_Bd2_pages.txt
4216315
5
... auf ein (7/(-Praes. -dr-dh-o von einer ein-                                                     ;   fachsten Wzf. *der- ist dalier wohl nicht zuruckzugreifen.         Curtius 5 233.                 — dregh- (-gh-T) .,unwillig, verdrossen", oder vielleicht ursprunglicher „schlaff,          zahe sein“?       Got. trig!} „Trauer, Widerwille", anord. tregi m. „Trauer, Hindernis", tregr „unwillig,  ungeneigt", trcginn „betriibt", ags. trega m. ,,Trauer, Leiden", as.        m. „Schmerz", tregan (nur I
... can „reizen, quiilen, plagen", aksl. raz-drahdi „reizen“ gehorigen draghate „qualt, plagt, miiht sich" zu scheiden sein sollte; Zupitza Gutt. 181. Falk-Torp              u. Ircey   m. Lit.);      av. drigu-,               drdgu- „arm, bediirftig, schwach"? (Zup. aaO.; andere Lit. bei Bartholomae Airan. \Yb. 777 f.)                                                                                                             53 * 822                                dregh-     cech. z-drdhati se ,,si
... .; andere Lit. bei Bartholomae Airan. \Yb. 777 f.)                                                                                                             53 * 822                                dregh-     cech. z-drdhati se ,,sieh weigern, sprode tun, sich zieren", poln. wzdragac siq„sich weigern, nicht daran wollen, sich strauben" (Zupitza Gutt. 181; nach Berneker 219 Iterativ zu einem verlorengegangenen Grundverbum. Oder als „hinziehen“ zu idg. dheragh-1).   Aus dem Lit. stellt man hierh
...                 1                                          '     vielleicht auch cech. z-drahati se „sich weigern", poln. wz-dragac siq „sich  strauben, nicht daran wollen“ (als „hinziehen“; oder zu *dregh- „unwillig“?)  und aksl. pcdragz „Saum, Rand eines Kleides“ u. dgl. (anders u. *deryh-  „fassen ‘); etwas weniger wahrscheinlich russ. droga, „Wagenbaum“ (s. u.  dhcr-, dhereyh- „halten“).       Lat. tralio „ziehe“, traha „Schleife“, tragum „Schleppnetz“, tragula „ds.,  kleine Schleife“       
...     dhrigh- „Haar, Borste“.                                                                                                                 £      Gr. dn(g, xgiyog „Haar; Borste", ir. gairb-driuch ( *drigu -) „Borste‘ .                                                              L     Fick II 4 156.           verbindet Prellwitz 2 187 abweichend mit lit. dr ilea „eine Partie   Faden, die wie eine Locke gewiekelt herabhaDgen“, drykstu dryhii von                        ,     faden- oder halmartig
```


## [2026-09-05T20:10:27.075Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'PY'\nimport re\nd=open('FVQ_pages.txt',encoding='utf-8',errors='replace').read()\npages=d.split('\\f')\nprint('pages',len(pages))\nfor i,p in enumerate(pages):\n    if re.search(r'[Dd]irham|Dirham', p):\n        print('--- leaf',i,'---')\n        print(p[:100].replace('\\n',' '))\nPY",
 "description": "find dirham in Jeffery"
}
```


### [2026-09-05T20:10:28.752Z] TOOL RESULT

```
pages 335
--- leaf 146 ---
FOREIGN VOCABULARY OF THE QUR'AN 129 we have a technical word for the study of Scripture borrowed fr
```


## [2026-09-05T20:10:31.149Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'PY'\nd=open('FVQ_pages.txt',encoding='utf-8',errors='replace').read()\npages=d.split('\\f')\nfor i in (146,147):\n    print('=== leaf',i,'===')\n    print(pages[i])\nPY",
 "description": "print Jeffery pp.129-130"
}
```


### [2026-09-05T20:10:32.957Z] TOOL RESULT

```
=== leaf 146 ===
FOREIGN VOCABULARY OF THE QUR'AN 129
we have a technical word for the study of Scripture borrowed from the
root ttn*! so widely used in this connection by the Jews.
Geiger's suggestion lias had wide acceptance among Western
scholars, 1 and it is curious that some of the Muslim philologers felt the
difficulty, for as-Suyiitl, Itq, 320, and in the Mukadkdhab, tells us that
some considered it to be Heb., and in Mutaw, 56, he quotes others as
holding it to be Syriac. Syr. **) does mean to train, to instruct, and
Eth. f*A to interpret, comment upon, whence JtCft'Th and ffCffl
commentary, but neither of these is so likely an origin as the Jewish
$"")*V which, as Buxtorf, Lex, 297, shows, is the commonest word
in the Rabbinic writings in connection with the exposition of Scripture,
and which must have been commonly used among the Jewish com-
munities of Arabia. 3
)5 (Dirham).
xii, 20.
A dirham.
Only the plu. form ^IjS is found in the Qur'an, and only in
the Joseph story.
It was commonly recognized by the philologers as a borrowed word.
al-Jawaliql, Mu'arrab, 66, notes it, 4 and ath-Tha 'alibi, Fiqh, 317,
includes it in his list of words common to Persian and Arabic. There was
some doubt as to the vowelling of the word, however, the authorities
varying between ,%Jfc*p ; t-^J^ ail d (t^J^ or f^J-^ ( c ^ -^ xv > ^)'
The ultimate origin is the Gk. fyja^/z??, 5 which passed into Syr.
as UOD>>. Some, however, would derive Spa^r] from a Semitic
source. Boissacq suggests this, and Levy, Fremdw, 118, connects it
1 Fracnkel, Vocab, 23; Fleischer, Kleinere Schriflen, ii, 122; Sprenger, Leben, ii,
289 ; Hirschfeld, Betirage, 51 ; New Researches, 28.
2 Eth. f*ft and 9R > / f *t\ are themselves derived from the Heb. Nolde-k^, iAV?/e
Jleitrdtje, 38; Horovitz, JPN, 109.
3 Rhodokanakis, WZKM, xvii, 285, thinks that in ^j^here we have a combina-
tion of ttf*n and D"n. " Zur Radix ^^ ist naohzutragen, dass in ihr VEF^\ und
Oil (v. Levy) zusammenfielen. Daher einerseits die Bedeutung stwlieren anderseits
arbeiten abnutzen." ,
4 So al-Khafaji, 83 ; LA, xv, 89.
5 Fraenkel, Vocab, 1^; Fremdw, 191.
K
=== leaf 147 ===
130 FOREIGN VOCABULARY OF THE QUR*AN
with Heb. 718311 (Phon. D38311) * beside TOTTK, which is
the Persian gold Daric, the Gk. SapeiKO?, and the Cuneiform da-ri-ku,
which appears in Syr. as )jQ3j>>. Liddell and Scott, however, are
doubtless right in deriving it from 8pa.(T(TOnai and meaning originally
" as much as one can hold in the hand ", then a measure of weight
and lastly a coin. This Spa-^/j.^ passed into Iranian first as a measure of
weight and then as a coin. In Phlv. we find the ideograms p.i dram
and J**o draxm meaning a silver coin, 2 or sometimes tnoney in general, 3
which is the origin of the Mod. Pers. *j$ and p and the Arm.
^L/iwi/^ 4 and may be assumed as the source of the Ar. j$ also. 5
It was doubtless an early borrowing from the Mesopotamian area,
for it occurs in the old poetry, e.g. 'Antara xxi, 21 (Ahlwardt, Divans 9
p. 45).
(Dihaq).
Ixxviii, 34.
Full.
It occurs only in an early Meccan passage descriptive of the delights
of Paradise, where, besides an enclosed garden and full-bosomed
virgins, the blessed are promised IsLjo L*.lj .
The Commentators are agreed that it means fall and there is con-
siderable agreement that it is to be derived from ^*po to press.
1 Lidzbarski, Handbuch, 257 ; Harris, Glossary, 96 ; cf. also Aram. D1D11 in
Cook, Glossary, 41.
2 PPGl, 105 and 110; Nyberg, Glossar, 58; Sayast, Glossary, 160; Frahang,
Glossary, 78. Haug thinks this of Babylonian origin, but Hubschmann rightly derives
it from a form *drahm from Spaxw, and then compares Av. JJ(^yjJOO taxma,
cf. Arm. Gramm, i, 145 ; Pers. Stud, 251.
8 e.g. in the Dadistan-i-Dmlk, cf. West, Pahlavi Texts, ii, 242.
4 Hubschmann, Arm. Gramm, i, 145.
6 Vullers, Lex, i, 832, 840 ; Vollers, ZDMG, li, 297, and Addai Sher, 62, though
some statements of the latter need correction.
```


## [2026-09-05T20:10:49.691Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; pdftoppm -f 140 -l 140 -r 300 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg140 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render PDF page 140"
}
```


## [2026-09-05T20:10:51.689Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'PY'\nd=open('TAD_pages.txt',encoding='utf-8',errors='replace').read()\npages=d.split('\\f')\nprint('leaves',len(pages))\nfor i,p in enumerate(pages):\n    if 'درهم' in p or 'درويش' in p or 'درویش' in p:\n        print('--- leaf',i,'---', p[:80].replace('\\n',' '))\nPY",
 "description": "find dirham/darvish in TAD"
}
```


### [2026-09-05T20:10:52.104Z] TOOL RESULT

```
total 1976
drwx------ 2 sfmqrb sfmqrb   4096 Sep  5 16:10 .
drwx------ 4 sfmqrb sfmqrb   4096 Sep  5 16:02 ..
-rw-rw-r-- 1 sfmqrb sfmqrb 154316 Sep  5 16:07 bqt_bot389.png
-rw-rw-r-- 1 sfmqrb sfmqrb 168738 Sep  5 16:07 bqt_bot390.png
-rw-rw-r-- 1 sfmqrb sfmqrb 520653 Sep  5 16:07 bqt_n389.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 527392 Sep  5 16:07 bqt_n390.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    395 Sep  5 16:10 leaf.py
-rw-rw-r-- 1 sfmqrb sfmqrb  53212 Sep  5 16:08 pg130_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  74748 Sep  5 16:08 pg130.png
-rw-rw-r-- 1 sfmqrb sfmqrb 107108 Sep  5 16:08 pg130_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb  87739 Sep  5 16:10 pg134.png
-rw-rw-r-- 1 sfmqrb sfmqrb  68320 Sep  5 16:08 pg136_300.png
-rw-rw-r-- 1 sfmqrb sfmqrb  63248 Sep  5 16:08 pg136.png
-rw-rw-r-- 1 sfmqrb sfmqrb  70436 Sep  5 16:10 pg140.png
-rw-rw-r-- 1 sfmqrb sfmqrb  89133 Sep  5 16:09 pg145.png
```


### [2026-09-05T20:10:54.024Z] TOOL RESULT

```
leaves 87
--- leaf 30 ---                                             ‫الإ‬
```


## [2026-09-05T20:10:58.963Z] TOOL CALL #25: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg140.png"
}
```


### [2026-09-05T20:10:59.454Z] TOOL RESULT

```

```


## [2026-09-05T20:10:59.450Z] INPUT

[Image: original 2550x3300, displayed at 1546x2000. Multiply coordinates by 1.65 to map to original image.]


## [2026-09-05T20:12:00.081Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources; python3 -c \"\nimport json;d=json.load(open('refs_online.json'));print(json.dumps(d['BQT'],ensure_ascii=False,indent=1));print(json.dumps(d['TAD'],ensure_ascii=False,indent=1));print(json.dumps(d['KLN'],ensure_ascii=False,indent=1))\"",
 "description": "Read BQT/TAD/KLN ref details"
}
```


### [2026-09-05T20:12:01.695Z] TOOL RESULT

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
 "title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67",
 "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein",
 "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt",
 "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.",
 "notes": "Other 1966 IA copies (comprehensiveety01klei/02klei etc.) are lending-only (401/403). local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt (paginated by leaf); /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt (plain djvu.txt, no page marks)",
 "local_files": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt"
 ],
 "cites": "page number, continuous across the two volumes (1966–67)"
}
```


## [2026-09-05T20:12:42.316Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'PY'\nd=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=d.split('\\f')\nprint('leaves',len(pages))\nfor leaf in (300,306,358):\n    print('='*20,'leaf',leaf,'printed',leaf+540,'='*20)\n    print(pages[leaf][:2600])\nPY",
 "description": "print BQT vol2 leaves 300, 306, 358"
}
```


### [2026-09-05T20:12:44.189Z] TOOL RESULT

```
leaves 684
==================== leaf 300 printed 840 ====================
        ‫رح‬

 ‫ولام وسکون‌الی‬      ‫در لك ‪ = ۳‬تکراول‬                         ‫در لك = بقتح اول بروزن قدك‪,‬دستارجه‬
‫وکاف ‪ .‬جام کوناه قد آستن کوناه پیش واز را‬                 ‫رگاونند که رومال ورویاك باشد ؛ و باين معثی‬
                                               ‫وتف‬        ‫بجای حرف انی زای نقطه‌دار همأ مده‌است‪ -‬ودر‬

 ‫در لورینه سیر خوردن ‪- ۴‬‬                                                               ‫عربی مممنی مال باشد ‪.‬‬

‫کنابه از فرب خوردن ‪ -‬و کردن‌کاری باشد" که‬
‫عمش کنن را منخص سازند ‪ -‬ویمعئی درشادی‌غم‬                  ‫‪ ۰‬و عصی یخی را گوند که درزیر‌ناودان‬           ‫گوند‬

                                                                                                     ‫به ود‬
‫کنابه‬              ‫در لور بنه سیر دآدن‬                        ‫‪3‬ممنی‌ابن ات‬
                                                                         ‫در کحامی خو ر ۔ب‬
 ‫کاازری‌باشد که عش کے رابرهم زنند ‪ -‬وفریب‬                 ‫‪٩‬‏ عدی‬     ‫است‬   ‫و کی درخور‬       ‫هی زد‬     ‫که کسا‬

 ‫خوردن ازکی ‪ -‬ودرعین شادی غم‌پیش آمدن‌را‬                                                             ‫می زسد ‪.‬‬
                                         ‫نز گوند ‪۰‬‬
                                                              ‫از نتوشدن‬          ‫در کشیدن ه کنابه‬
 ‫در ليك ‪ = 3‬یکراول ولام وسکون‬                             ‫محو کردن ‪ -‬و رد نمودن‬               ‫‪-‬‬   ‫و سر کدن‬
 ‫ثالی و تحتالی و کاف» به‌عنی‌در (اكاست کدقبای پیش‬                                                      ‫باشد‪¥ .‬‬
                           ‫واز آستن کوناه باشد ‪۶#.‬‬
                                                          ‫‪ -‬باکاف فارسی بروزن دختر »‬           ‫در گر‬
‫در ها ۔ بروزن سرما » خ رکوش را‬                                                             ‫درود کررگاویند ‪.‬‬
                                           ‫گومنت ‪:‬‬        ‫در لاله = بفح اول و صکون ثالی‬
 ‫»ج دووا‬
       ‫لا‬‫عمان‬
            ‫دروزن فر‬
                   ‫درهان ب‬                                 ‫وضم کاف فارسی ولام الف ولام مفتوح » بمعنی‬
‫ودار‌باشد ‪ - ۷‬ویمعتی درمالده ‪ -‬واهر باینمعنی‬               ‫کدارله است که بخ زبرناردان‌باشد وآن درهوای‬
                                ‫همت ‪. ۸‬‬   ‫ه‬                                ‫سرد ث کل مخروطی بسته مشود ‪.‬‬

   ‫‪3‬‬    ‫رك‪:‬دراہك‬     ‫‪۴‬‬         ‫مخفف «در و کر » = درو دگر‪.‬‬       ‫‪۴‬‬            ‫‪ ۱‬رك ‪ :‬در کلاله ‪.‬‬
              ‫در لك ‪۰‬‬    ‫رك‪:‬‬    ‫‪1‬‬          ‫‪.‬‬   ‫رل‪ :‬مادةٌ قل‬    ‫‪_ ۵‬‬           ‫‪.‬‬    ‫‪ - ۴‬رك‪ :‬هاده نمف‬
   ‫« بارتولمه ‪٩ ۴۹۹‬‏ ‪ ۰‬قس‬           ‫‪ - ۲‬ب
==================== leaf 306 printed 846 ====================
   ‫نت‬                                                                            ‫درة آسمان‬
‫همآمده است ‪ -‬و بکراول درفربی آلت ضرب | باشد وآن زرست‌رايج ووزنیاست معروف ‪.۷‬‬
‫بررزن سررشته» بمعنی‌جود‬     ‫رشت‬
                              ‫ه‬ ‫د‬                                              ‫وزدارا گوبند ‪.‬‬
                          ‫در آسمان ‏کنابهازکهکنانانت‪ | .‬وعطا وکرم باشد ‪#.‬‬
‫در هم بقلی ‪ = ۲‬مشهور أست ‪٠‬‏ وآن‬                                    ‫وآارا بعریی مجره خواند ‪.‬‬
‫زری بوده‌منتوب برای ‪,‬هودی کهآ را رای‌الیفل‬        ‫هرام » بروزن فرجام ؛ یمعنی درهم‬
                                                                                ‫د‬
                                     ‫رك‪ :‬بشلی ‪.‬‬    ‫‪۴‬‬         ‫‪ - ۱‬رك ‪ :‬درهم » درم ‪.‬‬

                                                                           ‫شه از صفسه ‪۵6۸‬‬

  ‫‪ #‬درهم ‪ -‬بفتح اول وسوم » از‪ :‬در (حرف اضافه) هم ؛ شوش ‪ .‬مختلط‪ .‬شوریده؛‬
      ‫دلتان ‪. ۳:۰‬‬
                ‫را) ونفی کنند تاچندین دزهم چرا گنت ک‬            ‫اد‬
                                                                 ‫شزیندش‬
                                                                      ‫(ودی‬
                                                                         ‫آشفته‪* :‬ملك فرم‬
          ‫(ك‪ :‬درم) ‪.‬‬
                   ‫وفتح (رکسر) سوم » معرب» واحد كوك نقره و واحد وزن ر‬                  ‫وکل‬
                                                                                         ‫رای‬
                                                                                           ‫م‬
  ‫‪ #‬ورویش ‪ .-‬شنح اول » پپلوی ‪hsöyird‬‏ ( فقیر؛ تھی دست ) « ای ‪> ۲: ۲۷۲‬‬
 ‫رتا‪00‬ع‪ . 120‬بازید ‪ . 05۵67780‬هردواز اوسا ‪« 11081۳-‬بارتولمه ‪ . ۷۷۷‬شک کلمه[ شکر‬
  ‫و رك‪ :‬اسشق وهوبشمان ‪ 4۵۵‬؛ دولف «تفس» اصلآ نرا ”در بیش بمعتی‬             ‫ست‪ .‬رك‪ :‬لبر که‬
   ‫قتام الیاب دانته‪ .‬وغالباآترا بممنی ( گدای درخاله ها) گرفته‌الد ف«ولری ‪ . ۱.‬ص ‪٩۳۸: 2‬‏‬
  ‫‪ 04۸ ۳‬ولی ابن اشتقاق عامیانه است ‪ .‬رف‪ :‬مقالة ‪ ۴۲۴‬درباب تاربخ عرب در‪۵‬ا‪1‬ا‪٩06۳‬‏ ج‬
   ‫‪ ,‬شمارء *س‪۹۸‬ه‪ .‬در چپار مقالة نظامی عروضی (ص‪)٩۸‬‏ نام شاهری «پسردرغوش ‪٩‬م‏ده‬             ‫‪۷‬‬
                                                  ‫ومرحوم قزوینی در تعلیقات (س‪ )۲۵۱‬بوشته ‪:‬‬
                                                  ‫« در میزان الافکار فی شرح معیار الاشعار که‬
                                                  ‫رساله امت در عروط تالف خواجه سیرآلدین‬
                                                  ‫طوسی مطوراست که دربسنی ازبلاد ابران‌کمة‬
                                                  ‫درویش
==================== leaf 358 printed 898 ====================
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
‫وفتح ثالث و نون » ظرفی باشد که درآن شیر‬
```


## [2026-09-05T20:13:19.043Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'PY'\nimport re\nd=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=d.split('\\f')\nfor i,p in enumerate(pages):\n    if i<290 or i>320: continue\n    if re.search(r'درم|دِرَم|درهم', p):\n        # show lines containing\n        hits=[l.strip() for l in p.split('\\n') if re.search(r'درم|درهم',l)]\n        print('leaf',i,'printed',i+540, ' | '.join(hits)[:400])\nPY",
 "description": "locate deram entry in BQT vol2"
}
```


### [2026-09-05T20:13:20.761Z] TOOL RESULT

```
leaf 290 printed 830 ‫درمتن کتاب مصذف بنعنی شفتالوکه بعربی خوخ‬                 ‫رقدکوهلفت‬ | ‫‪.‬‬   ‫غلم تکار تدم ‪ .‬درمحله ایندوابرانیکا‪ .‬کلکته صال ‪ 4‬شمارء ‪۷-۳‬‬         ‫رو لد دست‪.‬‬
leaf 293 printed 833 ‫‪ .‬كر ‪‎‬هبنمرا‪. :‬‬     ‫فحصم « »زش‬      ‫_‬    ‫‪۴‬‬        ‫‪.‬‬   ‫رك ‪ :‬درهم شلی‬   ‫‪-‬‬   ‫‪۱‬‬
leaf 296 printed 836 ‫ونندرمتی هم هت ‪. ۴‬‬                      ‫روزن کهواره ‪ .‬بہمنی درسار‬ | ‫باشد وآن‌درمی جلف است که دعك ازاجرت استاد‬                            ‫است »چه ساره‬           ‫ومعنی تکریبی آن لپزرددره‬ | ‫در سمی ‪ = ۸‬بذم اول و فتح الث بر‬                   ‫صحیح‌خوانند؟ ‪-‬وبمعنی درهم ودینار وزری‌باشد‬ | ‫‪- ۸‬پپلوی‬               ‫‪.‬‬   ‫» درشته‬    ‫درصه‬     ‫رك‪:‬‬     ‫‪۷‬‬                 ‫‪-
leaf 298 printed 838 ‫‪« _ ٦‬بدانکه درین کتاب دولغه مدالاست ‪ .‬امادرمتنشسکی‪‎‬‬                ‫® _ رك ‪ :‬درخشدن‪. ‎‬‬
leaf 299 printed 839 ‫ازیوست خرس بود‪ .‬وبقول دبگرازپوست شیر» و بزرو گوهرآراسته بود ‪ .‬خوارزمی درمفانیح‌الملوم‬
leaf 300 printed 840 ‫ودار‌باشد ‪ - ۷‬ویمعتی درمالده ‪ -‬واهر باینمعنی‬               ‫کدارله است که بخ زبرناردان‌باشد وآن درهوای‬ | ‫‪ - ۸‬از درماندن؟‪.‬‬        ‫بر منیع ‪ 027۲721‬نیب ک‪ »:۹‬ورك‪ :‬اسثق مهوبشمان‪4۵‬ه ‪.‬‬                          ‫‪1‬‬ | ‫‪ #‬درم ‪ -‬بکراول وفتح دوم پهلوی ‪ « 772۳1‬منای ‪ ۱۷۲:۲۰‬و ‪ < 0۳5201‬تاوادیا‬ | ‫ازیونانی ‪« 8×۵۲‬نبرک ‪۸‬ه“ معرب آن درهم (بک راول وفتح سوم )؛‬       ‫‪ ۰۶‬و ‪.‬
leaf 301 printed 841 ‫درمل = بورزن بلبل » غله رکاویند‬ | ‫و واو ک»نابه ازدرهم پیچیدن ‪ -‬و ینهان کردن‪-‬‬ | ‫‏‪ - ١‬لفة بمعنی‌جابکه درم باشد‪.‬‬
leaf 303 printed 843 ‫که برای امتبازچهاریابان وستوران دربهارهر سالگرء هابی راکه درهمان سالزاده میشدند بادرفشی‬
leaf 305 printed 845 ‫معنی آخر است کقهوس قزح (‬                                ‫کوش اکر فدری از آن درمان‌خانه‬                         ‫افع است‬ | ‫کنند ودرمیان هردوران زن حانملدهفآوریززند‬
leaf 306 printed 846 ‫زری بوده‌منتوب برای ‪,‬هودی کهآ را رای‌الیفل‬        ‫هرام » بروزن فرجام ؛ یمعنی درهم‬ | ‫رك‪ :‬بشلی ‪.‬‬    ‫‪۴‬‬         ‫‪ - ۱‬رك ‪ :‬درهم » درم ‪.‬‬ | ‫‪ #‬درهم ‪ -‬بفتح اول وسوم » از‪ :‬در (حرف اضافه) هم ؛ شوش ‪ .‬مختلط‪ .‬شوریده؛‬ | ‫(ك‪ :‬درم) ‪.‬‬
leaf 308 printed 848 ‫ککهسی درمقام خرابی و استیصال کسی شود ‪.‬‬              ‫رود مت‬      ‫اعت که‬      ‫کنابه از شراب خواری‬
leaf 309 printed 849 ‫لگردد ؛ ویکراول هم مده است `‬                    ‫درمقام تأسف و حسرت کویند ‪ -‬وبمعنی افوس‬
leaf 310 printed 850 ‫درمار = طم اول بروزن گلزار ‪ .‬دام‬ | ‫ت‬   ‫دوم) قلمها‬   ‫و تشد نف‬   ‫(یکراول‬    ‫کے درمار‬   ‫‪۵‬‬            ‫افثار ‪.‬‬   ‫افثره و دزد‬    ‫رك‪:‬‬         ‫‪۴‬‬
leaf 312 printed 852 ‫باشد ؛ وبفتح انوفلزدرست است ؛ وبابای فارسی‬                      ‫حیف ودریغ وافوی باشد ودرمۇ‪,‬دالفضلا بهمین‬
leaf 318 printed 858 ‫ومندی را نگیوزبند که درآن رفعتیبا هضر ئی‬                         ‫دهند ‪ -‬ومسندی را لگیوزنند که درمرتبه ورتبه‬
leaf 320 printed 860 ‫دت بممتی صدرمجلس ومسند باشده ‪ -‬ویفتح‬ | ‫پبوسته خواهد درمند وصدر مجلس بنشیند ‪.۷‬‬                                                           ‫مثتر كك باشد ‪. #‬‬
```


## [2026-09-05T20:13:33.483Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'PY'\nd=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=d.split('\\f')\nprint('====== leaf 300 (p.840) full ======')\nprint(pages[300][2500:])\nprint('====== leaf 358 (p.898) full ======')\nprint(pages[358][2200:])\nPY",
 "description": "print footnotes on BQT 840 and 898"
}
```


### [2026-09-05T20:13:35.479Z] TOOL RESULT

```
====== leaf 300 (p.840) full ======
‫‪_ ۵‬‬           ‫‪.‬‬    ‫‪ - ۴‬رك‪ :‬هاده نمف‬
   ‫« بارتولمه ‪٩ ۴۹۹‬‏ ‪ ۰‬قس‬           ‫‪ - ۲‬بهلوی ‪ « 03۳۳۳1‬منای ‪۱۷۲٩‬‏ از ربت ‪۲2 -‬‬
       ‫‪ - ۸‬از درماندن؟‪.‬‬        ‫بر منیع ‪ 027۲721‬نیب ک‪ »:۹‬ورك‪ :‬اسثق مهوبشمان‪4۵‬ه ‪.‬‬                          ‫‪1‬‬
       ‫‪ #‬درگاه ‪ -‬بفتح اول » از ‪ :‬در ‪ -‬گاه (پوند مکان ) » پهلوی ‪( 8487310‬دائرة لمعارف‬
  ‫اسلام ‪ :‬در) ‪hãûgrid ۰‬‏ «تاواد‪:‬ا‪ » ۹۵۱‬معرب آن درقاعة « دزی ح‪۱‬صی ‪۵۳٤‬‏ » ودر گاه « ابا‬
  ‫ص ‪۲۹: ۷۳4‬؛ بار گاه ‪ .‬در‪,‬ار» سرای وادشاهی » دبوان ملطاتی ‪ « :‬یکی ازملوك عجم شنیدم که‬
   ‫مته‌لقان را همی کفت که مرسوم‌فلان راچندانکه هست مضاعف کد که ملازم دگراه است ومترصد‬
                             ‫د‪-‬ر » درواژه ‪-‬آستانهٌ در» حشرت ‪.‬‬
                                                            ‫*تان ‪* ۷4‬‬   ‫فرمان ‪.‬‏ گل‬
  ‫‪ #‬درم ‪ -‬بکراول وفتح دوم پهلوی ‪ « 772۳1‬منای ‪ ۱۷۲:۲۰‬و ‪ < 0۳5201‬تاوادیا‬
  ‫ازیونانی ‪« 8×۵۲‬نبرک ‪۸‬ه“ معرب آن درهم (بک راول وفتح سوم )؛‬       ‫‪ ۰۶‬و ‪.‬‬
   ‫واحد سک قره (وزن و ‪:‬بای آن درعصرهای مختلف» متفاوت بوده است) ‪ .‬رك ‪ :‬دار المعارف‬
  ‫اسلام ‪ :‬درهم ‪١‬‏ ورك‪ :‬دزیح اص ‪ ۸۳‬واحدوزن ‪ :‬معادل شش‌دانگه(هر دانگ معادل درفراط)‬
                                          ‫«ناطم الاطبا» ورك‪ :‬دائرة لمعارف اسللام‪ :‬درهم ‪. ۲‬‬

====== leaf 358 (p.898) full ======
ند ؛ ویکسرثالث هبمنظر‬
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

     ‫‪ - ۱‬اوتا ‪( 20۳5621 .‬شانه‪ ,‬کتف) »بهلوی‬                                 ‫از «دوسدن»‬           ‫اسم مفعول‬      ‫‪۳‬‬
                                                                                                                      ‫‏‪e‬‬

         ‫‪- ۷‬بهلوی ‪60‬‬           ‫‪ 096‬هندی باستان ‪( 04115۵4-, 056-‬بازو‪ :‬ساعد) «اسشق ‪6۸۵‬؟‪.‬‬
     ‫(شب یش) «ناوادیا‪« )۰۹۱‬اسشق ‪ ۳۸۵‬اوستا‪( 2۲21205020 -‬عصری» غربی )ک‪۰‬ردی ‪. 6‬‬
              ‫افغانی ع ‪ . 01501‬استی ‪( ۳0551‬عصر دیروز) “ بلوچی ‪« 1564‬اسشق ایضا» ‪.‬‬
                 ‫از ‪ :‬دوش ‪( ۳۱‬لیاقت بمعنی دوشیدتی » نظیر خوانا بمعنی خواندنی) ‪.‬‬                                      ‫‪۵‬‬
         ‫‪ - ۶‬رك‪ :‬دوشند ‪ ,‬دراراك (‪-‬لطان آناد) ‪8915۱-۷28‬‬                                     ‫‪.‬‬    ‫دوشه‬   ‫رك‪:‬‬           ‫‪۹‬‬


                                                                            ‫«مکی نژاد › ‪.‬‬              ‫یردن)‬
                                                                                                           ‫وفششی‬
                                                                                                               ‫دظر‬
                                                                                                                 ‫(‬
                                                                                                        ‫‪۷٩۸‬‏‬        ‫حزهٌ‬
                                                                                                                       ‫فا‬‫صبه‬
                                                                                                                           ‫بق‬
                                                                       ‫‪.‬‬     ‫د کل کلاب ‪۵‬‬                 ‫مرو‬             ‫و سردسر‬

 ‫‪۳‬‬       ‫‪» ۷۲‬‬   ‫«مناس‪۲‬‬   ‫‪60‬‬    ‫‪ ۲‬بهلوی‬   ‫(مصدری)‬        ‫دی‬      ‫بت سم اول ‪ 4‬ار ‪ ۳‬دوست‬                  ‫ستی‬   ‫دو‬      ‫‪#‬‬


                                                     ‫عدق‬    ‫ت‬   ‫خبرخواهی‬       ‫‪-‬‬   ‫مودت‬         ‫‪ 6‬باری ‪.‬‬       ‫› رفاقت‬       ‫معت‬
```


## [2026-09-05T20:13:51.797Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== KLN dervish ===\"; grep -n \"^dervish\\|^dervish,\\|dervish, n\" KLN_1966.txt | head; echo; grep -n \"dervish\" KLN_1971.txt | head",
 "description": "grep Klein for dervish"
}
```


### [2026-09-05T20:13:51.856Z] TOOL RESULT

```
=== KLN dervish ===
10994:dervish,  n.,  a  Mohammedan  mendicant  monk.  — Turk,  derwish,  fr.  Pers.  ddrwesh,  ‘beggar;  poor’. Cp.  Avestic  driyu-,  fern,  driwi-,  ‘poor’.

37227:calender, n., a mendicant dervish. — Pers. 
68729:dervish, n., a Mohammedan mendicant monk. — 
240380:taj, n., cap worn by Moslem dervishes. — Arab.
```


## [2026-09-05T20:13:53.340Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== KLN drachma ===\"; grep -n \"^drachma\\|drachma,\" KLN_1966.txt | head; echo \"=== SKT drachm ===\"; grep -n -i \"drachm\" SKT.txt | head",
 "description": "grep Klein/Skeat for drachma"
}
```


### [2026-09-05T20:13:53.424Z] TOOL RESULT

```
=== KLN drachma ===
11353:didrachma,  didrachm,  n.,  an  ancient  Greek  silver coin,  a  two-drachma  piece’.  —  Late  L.  didrach¬ ma,  fr.  Gk.  8i8pa/jj.ov,  ‘a  two-drachma  piece’, fr.  81-  (see  di-,  ‘two’)  and  Spa/pir),  ‘drachm’.  See
11354:drachma.
11556:Derivative :  dirge,  tr.  and  intr.  v. dirhem,  n.,  a  weight  and  a  silver  coin  used  in various  Mohammedan  countries.  —  Arab,  dir¬ ham,  fr.  Gk.  Spcf/jj.-/].  See  drachma, dirigible,  adj.  and  n.  —  Formed  with  suff.  -ible fr.  L.  dirigere,  ‘to  direct,  guide’.  See  direct,  v. diriment,  adj.,  rendering  null  and  void  (law).  — L.  dirimens,  gen.  -entis,  pres.  part,  of  dirimere, ‘to  separate,  divide,  interrupt,  destroy’,  fr.  di-, ‘apart’,  and  emere,  ‘to  buy’,  orig.  meaning  ‘to take,  receive’.  Accordingly  dirimere  lit.  means ‘to  take  away’.  The  form  of  the  verb  should properly  be  *disimere  (fr.  dis-  and  emere);  the change  of  s  to  r  is  due  to  rhotacism.  See  exempt and  -ent.
12194:Dracaena,  n.,  a  genus  of  plants  of  the  lily  family (bot.)  —  ModL.,  fr.  Gk.  Spaxmva,  ‘she-dragon’, fern,  of  8paxo>v.  See  dragon, drachm,  n.,  a  drachma.  —  See  dram, drachma,  n.,  1)  an  ancient  Greek  coin;  2)  an ancient  Greek  weight.  —  L.,  fr.  Gk.  Spayjry;. See  dram  and  cp.  didrachma.
12221:dram,  n.,  a  weight.  —  OF.  drame  (F.  drachme), fr.  L.  drachma,  ‘drachma’,  fr.  Gk.  Spaxpcq,  ‘an Attic  weight;  a  silver  coin’,  lit.  ‘a  handful’,  rel. to  Spaypcq,  ‘handful’,  Spaypa,  "a  sheaf’,  lit.  ‘as much  as  one  can  grasp,  a  handful’,  from  the stem  of  SpaaacaHai  (for  *8pa/-ae:<i9at),  ‘to clutch,  grasp,  seize’;  cogn.  with  Arm.  trpak, ‘faggot’,  perh.  also  with  OSlav.  po-dragu, ‘border’,  OHG.  zarga,  ‘border,  edge,  frame’, ON.  targa,  OE.  targe,  ‘shield,  buckler’.  Cp. drachma,  Drassidae.  Cp.  also  targe,  ‘shield’.
=== SKT drachm ===
5377:Drachm;  sec  Dram.
5387:Dram,  Drachm.  (F.-^.-Gk.^ drame,  drtichme^  '  a  dram,  eighth  p< an  onnc;e;'Cot.  —  L.t/rwr/ww.  — Gk.Jip a  handful,  a  drachm.i,  o-scd  both  as  V{ and  coin :  cf.  ipay^a,  as  mach  at  on grasp. —  Gk.  Upaaaofim,  I  grasp.
```


## [2026-09-05T20:14:25.952Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== HUB dos/darves ===\"; grep -n -i \"Schulter\\|derwîs\\|derves\\|darvēš\\|driyu\" HUB.txt | head -20; echo \"=== NYB drahm/driyos ===\"; grep -n -i \"drahm\\|driyō\\|driyos\\|dram\" NYB_vol2_glossary.txt | head -20; echo \"=== AHD dous ===\"; grep -n -i \"^deu\\|dous\" AHD_watkins1985.txt | head -10",
 "description": "grep HUB, NYB, AHD"
}
```


### [2026-09-05T20:14:26.019Z] TOOL RESULT

```
=== HUB dos/darves ===
2149:hierher, das fem. von driyu- arm' lautete drlm-
6500:kdfak *Satter, West PT. 4, 48, bal. kdpak, nb. kl^fay *Schulter ,
8292:tara- ; dds *Schulter H. 584 ; dusman *Feind' H. 565 ; mm
=== NYB drahm/driyos ===
1242:davanik [dw?nyk] transliteration of the broken pl. dawānīg of Arab dānag, -iq, a small coin: Abu (Arab) ~ “‘the father of the small coins" = he who is greedy for money, the nickname of the caliph Abu Ja‘far Mansur, the founder of Bagdad 11771. — Arab dānag is borrowed from Milr dáng (BP d?ng), Arm. lw. dang, NP dank, dän(u)g; according to FrP 29 it was 1/, of a denar, but in Islamic times 1/, of a drahm; late Greek authors Šuvaxn = 0B0X6c.
1325:döSäram [dwš'lm]. love, affection 51. 826 etc. — MPrs dws’rm, -myh, -myy love, dws’rmgr ‘loving’; Paz. dusär(a)m. < dos + dram: doš SW form of Av. (1656) zaoša-, MPrth zwš ‘willingness’ (MHC); dram cf s. v. rämisn.
1330:drahm [ZWZN] a silver coin, the drachm 68. 119%, — From Gr špaxun. In Sassanian time its weight was 4.25 gr. silver. drahnai [dlhn?y], dranäi [dln’y] length 6514, 9616, etc. — From draž; the form is influenced by pahnäi (q. v.). Paz. dranäe (SGV).
=== AHD dous ===
105:A word of caution should be entered about the semantics of the roots. It is perhaps more hazardous to attempt to reconstruct meaning than to reconstruct linguistic form, and the meaning of a root can only be extrapolated from the meanings of its descendants. Often these diverge sharply from one another, and the scholar is reduced in practice to inferring only what seems a reasonable, or even merely possible, semantic common denominator. The result is that reconstructed words and particulary roots are often assigned hazy, vague, or unspecific meanings. This is doubt- less quite illusory; no human society from Proto-Indo-European times to the present day would be viable if conversation were limited to vague generalities. The apparent haziness in meaning of a given Indo- European root often simply reflects the fact that with the passage of several millennia the different words in divergent languages de- rived from this root have undergone semantic changes that are no longer recoverable in detail.
364:LOIN. 4. Possibly suffixed variant *dlo-gho- in Greek dolikhos, long: DOLICHOCEPHALIC, DOLICHOCRANIAL. [Pok. 5. del- 196.] del-2. To recount, count. 1. Germanic *taljan in Old English tellan, to count, recount: TELL. 2. Germanic *tal6é in: a. Old English talu, story: TALE; b. Middle Dutch dle, speech, language: TAAL. 3. Old English denominative talian, to tell, relate, probably akin to the source of Middle English talken, to talk: TALK. 4. Per- haps Greek dolos, ruse, snare: DOLERITE. [Pok. 1. del- 193.] del-3. To split, carve, cut. 1. Suffixed form *del-to- in Germanic *teldam, “thing spread out,” in Old English teld, awning, tent: TILT?. 2. Germanic extended form *telg- in Old English telgor, telgra, twig, branch: TILLER’. 3. Perhaps o-grade form *dol-é- in Latin dolére, to suffer (? < “to be beaten”): DOLE?, DOLOR; CONDOLE, INDO- LENT. 4. Suffixed o-grade form *dold-dhraé in Latin dolabra, a heavy chopping tool (< doldre, to chisel, hew): DOLABRIFORM. [Pok. 3. del- 194.] del-*. To drip. Perhaps suffixed (stative) o-grade form *dol- in Germanic *talgaz in Middle Low German falg, talch, tallow (< “dripping fat”), perhaps akin to the source of Middle English talow, tallow: TALLOw. [Pok. 4. del- 196.] deme-'. Also dem-. House, household. 1. Suffixed re- duced o-grade form *dom-o-, dom-u-, house, in: a. Latin domus, house: DOME, DOMESTIC, DOMICILE; MAJOR- DOMO; b. suffixed form *dom-o-no- in Latin dominus, master of a household (feminine domina > Old French dame, lady): DAME, DAN?, DANGER, DoM, DOMAIN, DOMI- NATE, DOMINICAL, DOMINIE, DOMINION, DOMINO}, (DOM- INO2), DUENNA, DUNGEON; (MADAM), MADAME, MADEMOISELLE, MADONNA, PREDOMINATE. 2. Com- pound *dems-pot-, “house-master” (*-pot-, powerful; see poti-), in Greek despotés, master, lord: DESPOT. 3. Root form *dem()-, to build (possibly a separate root), in: a. Germanic *timram in Old English timber, building material, lumber: TIMBER; b. Germanic *tumfté in Old Norse topt, homestead: Torr. [Pok. dem- 198.] deme-2. To constrain, force, especially to break in (horses). 1. Suffixed o-grade form *dom-o- in Germanic *tamaz in Old English tam, domesticated: TAME. 2. O-grade form *doma- in Latin domdre, to tame, sub- due: DAUNT; INDOMITABLE. 3. Zero-grade form *dmo- in Greek daman, to tame (> adamas, unconquerable): ADAMANT, DIAMOND. [Pok. (dema-), doma- 199.] denk-. To bite. 1. Germanic *tanhuz in Old English toh, tenacious, sticky (< “holding fast”): TOUGH. 2. Germanic *tanguz in Old English tang(e), tong(e), pincers, tongs: TONGS. 3. Germanic *tang- in Old Norse tangi, a point, sting, akin to the Scandinavian source of Middle English tonge, tange, point, tang: TANG!. 4, Germanic *teng- in Old High German zinko, spike, prong: z1Nc. [Pok. denk- 201.) dens-'. To use mental force. Reduplicated and suffixed zero-grade form *di-dns-sko- in Greek didaskein, to teach: pipactic. [Pok. 1. dens- 201.] dens-2. Dense, thick. 1. Suffixed form *dens-o- or *dns-o- in Latin dénsus, thick: DENSE; CONDENSE. 2. Suffixed zero-grade form *dns-u- in Greek dasus, hairy, shaggy: DASYURE. [Pok. 2. dens- 202.] dent-. Tooth. (Originally participle of ed- in the earlier meaning “to bite.”) 1. O-grade form *dont- in Germanic *tanthuz in Old English toth, tooth: TOOTH. 2. Zero-grade form *dné- perhaps in Germanic *tunth-sk- in Old English tisc, tix, canine tooth: TUSK. 3. Full-grade form *dent- in Latin déns (stem dent-), tooth: DENTAL, DENTATE, DENTI-, DENTICLE; (BIDEN- TATE), DANDELION, EDENTATE, INDENT!, (INDENTURE), TRIDENT. 4. O-grade variant form *(o)dont- in Greek odén, odous, tooth: -ODON, -ODONT, ODONTO-; CERATO- Dus. [In Pok. ed- 287.] deph-. To stamp. 1. Suffixed form *deph-s-ter- in Greek
370:deu-'. To lack, be wanting. 1. Possibly suffixed form *deu-s- in: a. Germanic *teuzdn in Old English téorian, tyrian, to fail, tire (< “to fall behind”): TIRE}; b. Greek dein, to lack, want: DEONTOLOGY. 2. Suffixed form *deu-tero- in Greek deuteros, “missing,” next, second: DEUTERO-; DEUTERAGONIST, (DEUTERIUM), DEUTERON- omy. (For suffixed zero-grade form *du-s-, combining form of *dew-es-, a lack, see dus-.) [Pok. 3. deu- 219.] deu-2. To do, perform, show favor, revere. 1. Suffixed form *dw-enos in Latin bonus (> Old French bon, femi- nine bonne), good (< “useful, efficient, working”): Bo- NANZA, BONBON, BONITO, BONNE, BONUS, BOON?, BOUNTY; BONHOMIE, DEBONAIR. 2. Adverbial form *dw-ené in Latin bene, well: BENEFACTION, (BENEFAC- TOR), BENEFIC, (BENEFICENCE), BENEFIT, BENEVOLENT, BENIGN, (HERB BENNET). 3. Diminutive *dw-ene-lo- in Latin bellus (> Italian bello, feminine bella), handsome, pretty, fine: BEAU, BEAUTY, BELLE; BELDAM, BELLA- DONNA, BELVEDERE, EMBELLISH. 4. Possibly suffixed zero-grade form *dw-eye- in Latin bedre, to make blessed: BEATITUDE; BEATIFIC, BEATIFY. 5. Possible (but unlikely for formal and semantic reasons) suffixed zero-grade form *du-na- in Greek dunasthai, to be able: DYNAMIC, DYNAMITE, DYNAST, (DYNASTY); AERODYNE. [Pok. 2. deu- 218.]
371:deu-’. To burn, hurt. Germanic suffixed form *teu-n6 in Old English téona, injury: TEEN?. [Pok. ddu- 179.] deue-. Also dwae-. Long (in duration). Suffixed zero-grade form *dii-ro- (< *dua-ro-) in Latin dirdre, to last: DURABLE, DURANCE, DURATION, DURING; PERDU- RABLE, THERMODURIC. [In Pok. 3. deu- 219.]
372:deuk-. To lead. 1. Germanic *teuhan in Old English téon (> Middle English tuggen), to pull, draw, lead: TUG; WANTON. 2. Suffixed zero-grade form *duk-d- in Ger- manic *tugdn in Old English togian, to draw, drag: TOW}. 3. Suffixed o-grade form *douk-eyo- in Old English *tiegan, tigan, to bind: TIE. 4. Suffixed o-grade form *douk-mo- in Germanic *tau(h)maz in Old English téam, descendant, family, race, brood: TEAM. 5. Germanic denominative *tau(h)mjan in Old English téman, tieman, to beget: TEEM!. 6. Basic form *deuk- in Latin diicere, to lead: DOCK!, DOGE, DOUCHE, (DUCAL), (DUCAT), (DUCH- ESS), (DUCHY), DUCT, DUCTILE, DUKE; (ABDUCENS), AB- DUCT, ADDUCE, CIRCUMDUCTION, CON3, (CONDOTTIERE), CONDUCE, CONDUCT, DEDUCE, (DEDUCT), EDUCE, (EN- DUE), INDUCE, INTRODUCE, PRODUCE, REDOUBT, RE- DUCE, SEDUCE, SUBDUCTION, SUBDUE, TRADUCE, TRANSDUCER. 7. Suffixed zero-grade form *duk-d- in Latin éducdre, to lead out, bring up (é- < ex-, out; see eghs): EDUCATE. [Pok. deuk- 220.]
411:deu-'. Greek dus-, bad: pys-. [Pok. dus- 227.]
1026:Middle Dutch stuyver, stiver: STIVER. II. Extended form *steud-. 1. Nasalized form *stu-n-t- in Germanic *stunt- jan in Old English styntan, to dull: stinT!. 2. Germanic *staut- in: a. Old High German stézan, to push: sTOss; b. Middle Low German and Middle Dutch stéten, to force, akin to the source of Middle English stutten, to stutter: sTUTTER. III. Extended form *steug-. 1. Ger- manic *stukkaz in: a. Old English stocc, tree trunk: stock; b. Old High German stoc (> German Stock), staff: ALPENSTOCK; Cc. Old French estoc, rapier, sword point: TUCK’, 2. Germanic *stukkjam in: a. Old High German stukki, crust, fragment, covering: SHTICK; b. Italian stucco, stucco: stucco. 3. Germanic *stok- in Dutch stoken, to poke, thrust: sTOKER. IV. Suffixed (stative) zero-grade extended form *stup-é- in Latin stupére, to be stunned: STUPENDOUS, STUPID; STUPEFY. V. Suffixed (stative) extended zero-grade form *stud-é- in Latin *studére, to be diligent (< “to be pressing for- ward”): STUDENT, STUDY. VI. Extended zero-grade form *stug- in Greek Stux, the river Styx (< “hatred”): Styx. VII. Variant zero-grade form *tud-. 1. Latin tudes, ham- mer: TOIL!. 2. Suffixed form *tud-ti- in Latin tussis, cough: TussIs. 3. Nasalized form *tu-n-d- in Latin tun- dere, to beat: CONTUSE, OBTUND, PIERCE, RETUSE. VIII. Variant zero-grade form *tup-. 1. Suffixed form *tup-o- in Greek tupos, a blow, mold, die: TYPE; ANTI- TYPE, ARCHETYPE. 2. Nasalized form *tu-m-p- in Greek tumpanon, drum: TYMPANUM. [Pok. 1. (s)teu- 1032.] steu(e)-. To condense, cluster. Possible root. 1. Extended form *stip- in: a. Greek stuppé, tuft, tow: STOP, STUPE; b. Sanskrit stipah, tuft of hair, crown of the head: STUPA. 2. Extended form *stibh- in Greek stuphein, to contract: sTYPTIC. [Pok. steua- 1035.]
1096:5. Greek trias, the number three: TRIAD. 6. Greek trikha, in three parts: TRICHOTOMY. 7. Greek compound triérés, galley with three banks of oars, trireme (-érés, oar; see era-'): TRIERARCH. 8. Suffixed form “*tri-to- in Greek tritos, third: TRITIUM; TRITANOPIA. 9. Compound form *tri-pl-, “threefold” (*-pl- < combining form *-plo-; see pel-3), in Greek ¢triploos, triple: TRIPLE. 10. Compound form *tri-plek-, “threefold” (*-plek-, -fold; see plek-), in Latin triplex, triple: TRIPLEX. 11. Compound form *tri-st-i, “third person standing by” (see sta-), in Latin testis, a witness: TESTAMENT, (TESTIMONY); ATTEST, CONTEST, DETEST, OBTEST, PROTEST, TESTIFY. 12. Per- sian si, three: straR. III. Extended zero-grade form “iris, “thrice.” 1. Latin ter, thrice: TERN?; TERPOLYMER. 2. Greek tris, thrice: TRISOCTAHEDRON. 3. Suffixed form *tris-no- in Latin trini, three each: TRINE, (TRINITY). IV. Suffixed o-grade form *troy-o- in Russian troje, three: TROIKA. [Pok. trei- 1090.] trem-. To tremble. Possibly related to trep-' and tres- through a hypothetical base *ter-. Latin tremere, to shake, tremble: TREMENDOUS, TREMOR, TREMULOUS. [Pok. trem- 1092.] trep-'. To tremble. Possibly related to trem- and tres- through a hypothetical base *ter-. Latin trepidus, agi- tated, alarmed: TREPID; INTREPID. [Pok. 1. trep- 1094.] trep-2. To turn. 1. Greek trepein, to turn: -TROPOUS; APOTROPAIC, TREPONEME. 2. O-grade form *trop- in: a. suffixed form *trop-o- in Greek tropos, a turn, way, manner: TROPE, TROPO-, TROVER; CONTRIVE, (RE- TRIEVE); b. suffixed form *trop-d- in Greek tropé, a turning, change: TROPHY, TROPIC; ENTROPY. [Pok. 2. trep- 1094.] tres-. To tremble. Possibly related to trem- and trep-1 through a hypothetical base *ter-. Metathesized form *ters- in o-grade suffixed (causative) form *tors-eyo- in Latin terrére, to frighten (< “to cause to tremble”), with vowel e from terror (< *ters-os-), terror: TERRIBLE, TERROR; DETER, TERRIFIC. [Pok. tres- 1095.] treud-. To squeeze. 1. Suffixed o-grade form *troud-o- in Germanic *thrautam in Old English thréat, oppression, use of force: THREAT. 2. Variant form *trid- in Germanic “thristjan in Old Norse thrysta, to squeeze, compress: THRUST. 3. Latin tridere, to thrust, push: ABSTRUSE, EXTRUDE, INTRUDE, OBTRUDE, PROTRUDE. [Pok. tr-eu-d 1095.] trozdo-. Thrush. 1. Germanic *thrust- in Old English throstle, thrush: THROSTLE. 2. Germanic *thruskj6n- in Old English thrysce, thrush: THRUSH}. 3. Zero-grade reduced form *trzdo- in Latin turdus, thrush: STURDY. 4. Perhaps altered in Greek strouthos, sparrow, ostrich: STRUTHIOUS; (OSTRICH). [Pok. trozdos 1096.] tu-. Second person singular pronoun; you, thou. 1. Lengthened-grade form “ti (accusative “te, *tege) in Germanic *thii (accusative *theke) in Old English thi (accusative thec, thé), thou: (THEE), THOU!. 2. Suffixed extended form *éwjei-no- in Germanic *thinaz in Old English thin, thine: THINE, THY. [Pok. tu- 1097.] twei-. To agitate, shake, toss. 1. Extended form *tweid- in Germanic *thwit- in: a. Old English thwitan, to strike, whittle down: WHITTLE; b. Middle Dutch duit, a small coin (? < “piece cut or tossed off”): DorT. 2. Extended form *tweis- in Greek seiein, to shake: SEISM, SISTRUM. [Pok. 2. tuei- 1099.] twengh-. To press in on. Germanic *thwang- in: a. Old English thwong, thwang, thong, band (< “constraint”): THONG; b. by-form *twangjan in Old English twengan, to pinch: TWINGE. [Pok. twengh- 1099.] twer-', To turn, whirl. Zero-grade *tur-. I. Variant form *stur-. 1. Suffixed form *stur-mo- in Germanic *sturmaz, storm (< “whirlwind”), in Old English storm, storm: STORM. 2. Germanic *sturjan in Old English styrian, to move, agitate: STIR!. II. Suffixed form *tur-bd in Greek turbé, tumult, disorder (> Latin turba, disorder, turbé, spinning top, and turbdre, to confuse, disorder): (TROU-
1422:DEUTERO- deu-!
1423:DEUTERONOMY deu-!, nem-
```


## [2026-09-05T20:14:27.542Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== LKT ===\"; grep -n -i \"dirhem\\|drachme\\|derwisch\" LKT.txt | head -20; echo \"=== AFM ===\"; grep -n \"درهم\\|درویش\\|درم\" AFM.txt | head -20",
 "description": "grep Lokotsch and Addi Shir"
}
```


### [2026-09-05T20:14:27.603Z] TOOL RESULT

```
=== LKT ===
1292:'Bettler ;  arm'  [Horn  NpEt  S.  124,  Nr.  559], ebenso  tk.  derwis  'arm,  Bettelmönch'; hieraus  rum.  dervi§,  it.  dervis  [mit  Be- tonung der  Pänultima],  frz.  derviche,  sp. derviche,  pg.  dervis,  derviche;  dtsch. Derwisch,  ndl.  dervis,  engl,  dervish ;  russ. bulg.  serb.  derwis,  cech.  dervis,  poln. dervisz.
1348:'Eine  Silbermünze  von  wechselndem Werte'  [vgl.  dazu  MORITZ  in  AbhPr- AW  Berlin  1918,  Nr.  4,  S.  30,  Anm.  2, wo  das  Abwärtsgleiten  des  Dirhams  für die  ersten  tausend  Jahre  der  Hedschra bis  auf  den  50.  Teil  seines  ursprünglichen Wertes  nachgewiesen  wird],  vulgär  aus- gesprochen dirhem  [das  ar.  Wort  kommt selbst  aus  gr.  bpaxMn  ZDMG  LI,  297, das  auf  bpdTTU),  bpäTTOiuai  zurückgeführt wird  u.  soviel  wie  'eine  Handvoll',  sc. von  Spießen,  bedeutet];  hieraus  frz. dirhem,  sp.  adereme,  adarme,  pg.  adarme 'Gewicht  od.  Münze',  pg.  auch  figürlich 'geringfügige  Sache'  [Gonstancio  Dice 21b];  über  das  tk.  drem  wurde  rum. dram  'ein  Quentchen,  V^oo  einer  Okka [s.  hier  Nr.  1.590]',  also  in  der  Walachei 3,370  g,  in  der  Moldau  3,229  g.  [DE 41.    Devic  DEt  103.
1447:'Arm';  in  alle  europäischen  Sprachen zur  Bezeichnung  des  Bettelmönches  über- gegangen und  mit  Derwisch  [s.  liier Nr.  496]  und  Jogi  [s.  hier  Nr,  2169]  ver- wechselt. Dtsch.  Fakir,  frz.  fakir,  fa- quir,  it.  fachiro,  engl,  fakir,  fakeer  usw. —  Vielleicht  ist  hieraus  mit  W^echsel von  r  zu  n  auch  geworden :  it.  facchinu,
2399:—  Die  afrikanischen  Stämme  essen  die gerösteten  Bohnen  [ar.  bunn,  wodurch unser  dtsch.  Wort  beeinflußt  ist]  mit Bulter;  erst  spät,  etwa  im  15.  Jahr- hundert wurde  der  Trank  erfunden,  um die  Derwische  wachzuhalten,  damit  sie
2893:'Mütze'  [Horn  NpEt  S.  192,  Nr.  863  und KZ  XXXII,  582],  tk.  kälah  'Derwisch- mütze'; hieraus  rum.  chiulaf  'Mütze'; bulg.  gugla(7).
3553:'Schilf,  näi  'Flöte'  [Horn  NpEt  S.  237, Nr.  1060],  ebenso  tk.  nej  'Flöte',  ins- besondere diejenige,  deren  sich  die Mewlewi- Derwische  ['heulende  oder drehendeDerwische',derftcÄfs/oMrneMrs] bei  ihrem  religiösen  Tanze,  dem  dikr [vulgäre  Aussprache  zikr]  bedienen; hieraus  rum.  naiü,  neiü  'Panflöte', naingiü  'Flötenbläser'.
4368:Ekstase  erblickt  und  besonders  von  den Derwischorden  gepflegt  wird :  frz.  soufi, was  wir  heutzutage  etwa  'Theosoph' nennen  [Einwirkung  von  gr.aoqpöq 'weise' braucht  nicht  ausgeschlossen  zu  sein, wenn  es  auch  nicht  Grundwort  ist]; engl.  sofi.
5769:Dalai-Lama  1302 DriZ/e*-  j.  468 Da//os  j.  468 Damast  476 damaszieren  476 Damesinel  1871 Da?«  504 dawnen  j.  505 St.  482 Denebola  St.  482 Derwisch  496 Dey  460 dibbern  j.  514 D//f<eZ  j.  2068 D/f/(27«/  521 Diwan  526 Doc/j^s  j.  1984 Doto  j.  1984 Dollinger  j.  2002 Dolman  530 Dolmetsch(er)  2078 I>oM/"es  j.  1978
6465:dirhem  523
=== AFM ===
1202:( ܠܨ ܨ ) الباطل < والدرهم الذي فْضْتَهُ رديّة معرب ܨܘ بالفارسيّة عن 
1410:( التآجة ) الصماحة .2 الفضّة واصلة تازه بالفارسة الدرهم المضروب حديثا 
2574:( الدرمك) دقيق الموارى 0 الذي ܫܐ ܀ ومثة ܝܝ ° ܓܪܡܟܐ 
2683:. من الدرهم 11-7 ردي دعل 
3507:( ܐܠܚܢ = ق) ل ) درهم زيف معرب سه تا اي ثلاث 300 (شفاء الغليل) 
6091:( التبهرج ) الدرهم ازيف الردي تعر يبب ܘ واصل ܫܐ د 
7248:درم +¡ 
7249:درما ܟܕ
```


## [2026-09-05T20:15:53.794Z] TOOL CALL #34: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-05T20:15:53.800Z] TOOL RESULT

```


```


## [2026-09-05T20:15:55.371Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'PY'\nd=open('TAD_pages.txt',encoding='utf-8',errors='replace').read()\npages=d.split('\\f')\nfor i in (30,31,32,33):\n    print('=== leaf',i,'===')\n    print(pages[i][:1800])\nPY",
 "description": "print TAD leaves 30-33"
}
```


### [2026-09-05T20:15:57.540Z] TOOL RESULT

```
=== leaf 30 ===
                                            ‫الإ‬                                                  ‫آ‬

‫وونابى ‪ 8021:81‬وهو الراسب مانلزيت والراسب والسعيظ‬                                       ‫دردي‬


                                             ‫ل‬                                 ‫‪.‬‬

                                             ‫» معناه خ!‬      ‫ترى « درزي‬             ‫‪-‬‬   ‫درزي‬


‫فش >‬
   ‫ريةّ«‬
       ‫ِترك‬
          ‫ديال‬
             ‫ار‪-‬سي « د رفش » معناهتلالؤ وع‪1‬م وف‬
                                              ‫رففس‬
‫ناه عام ولواء وفي يه همم ‪ 220‬معتاه نسيج وفي الافر نسية م‪ 33‬معناه‬
                                       ‫معئأه عام وأواء وراية‬           ‫السيج ومئه ‪1190‬م‪2710‬‬

             ‫ية مأخوذة مندق أي لوح وعريبها المصراع والصرفق‬
                                                         ‫ام‪--‬‬
                                                            ‫عفة‬
                                                              ‫در‬
‫درثم ‪ -‬نوناني ‪6‬تصطعة‪ 0‬وهو نقد قضه وورزن ايضًا ‪ 5‬درم الفارسي وهو‬




    ‫درويش ‪ --‬فارمي « دربيش ‪ 6‬معناهقدام الباب وهو كناية عن الفقير‬

‫اةم‪-‬ية افرنسية ‪6‬تذدعناهك معناه اثنا عشر من نوع واحد مرادقه‬
                                                         ‫عيئ‬
                                                           ‫دز‬
                                                                                        ‫اننا عشربة‬
‫فارسي‪ 2‬دست»معناه بدولدمعان كثيرةمحوالثوب والجلس والميلة‬                            ‫لامالا‬


                                 ‫دستحة ‪--‬فارمي « دسته » معناه حزمة وقبضة‬

  ‫فارسي « دوسر » معناه ذو رأسين وبراد بهمسمارمحدد العلرفين‬                               ‫دار‬

                 ‫‪0‬‬                      ‫‪2‬‬                                  ‫‪1‬‬         
=== leaf 31 ===
 ‫ب قهاعدةأساسيةيرجعاليهاكدقترأسما اءلجند ومموع قوانين الدولة ويقطدلق‬
                                        ‫عالىوزير الكبير أيضا مرادفه سانة‬
                                           ‫دف ‪ -‬ارامي « ذفا» معناه توح‬
             ‫مه الت ف اراي د دّفا © أيلوح مرادفه كاز السفينة‬
‫دف" س منآلات الطرب ‪ -‬عبراني « ‪# 0‬امقدق ين « ددنت »أي‬
                                                                  ‫ضرب وثقر وقرع‬
 ‫دففيرنيقية ذ كرهاهرودط المتوفيسنة ‪ 8-4‬قبل الميجقال انالفينيقيين‬
 ‫الذبنأدخلوا حروف الحجاء الى بلادنا أدخلوا معها بأعضلانمانظهم نحو«زفري»‬
‫ون«تارا »‬
        ‫أي كتبة(منسفروزيرأي كتب ) ون«مطم » أي قضاة دي‬
                        ‫«‪ 6‬از أكيتاب صغيروهو الدقتر المذكور الخ ‪...‬‬
‫اليوناني الذي معناه‬     ‫‪5‬سأمعنداء‪00‬‬
                                  ‫ات انار دذكان ‪ 4‬و‪5‬أي‬                        ‫‪5‬‬

                                               ‫كاسميناء حاوت‬      ‫اتادؤوعاء اغا ‪5‬‬
                                             ‫دلغان (© ‪ -‬عامية فصيحها غضار‬
                                    ‫دلفين ‏ بوناني ‪ 811164‬مرادفه اللاخس‬
‫دلو العفجيرانية «دلي» وهو ا_سممبمدعنلىاة مشتق من دلايداوالعربى‬
‫دمغة ‏ عامي ‪ -‬ترك ( دامغهوطمفه ومنًا» معناهالسمة والوسموالعلامة‬
                 ‫ظ‬                                       ‫والائروالطابعوالروشم ‪...‬‬
 ‫دمقس سس تعربب وماق ة قة اليونانيأي دمشقي” ويراد به نسيج حرو‬
‫أيْضيخاباكل سح ددياى دنقىوينديالبآوعنل ليلذ البزنان انا‬
‫اهودبة للنجارة ‪ 8‬وبديشيق عرش » أي على حربر الفراش الدمشقي (ّ‬
  ‫‪ 6‬وهو التراب الأتلن او تام العلين اليابس اوأنطينامنك الذيلانها لطّدرمل واحدتدمةنة‬

=== leaf 32 ===
‫وك‪2‬ن‪0‬ا‪ 6531‬اللاتيني يراد بسك ك‪ 3‬مفنولاذ كانت صلم ‪7‬‬
                                                 ‫‪0‬‬                             ‫‪0‬‬
                                  ‫ى ‪ .‬دمقس مذكورفيمعلقةامرىء القيس‬
       ‫‏‪ ١‬دامية ‏ عبراني « دموت » معناه مشامبةثمصورةلانهانشبهالاصل‬
                       ‫ارامي ( دنح ‪6‬ا معناهظبوروهوعيدالغطاس‬               ‫دنم‬
                              ‫دهقان ‪--‬فارمي ‪ 2‬دهكان » معناهزعم القرية‬
   ‫يهض‬
     ‫بون‬
       ‫أدا‬
         ‫ضةالة وهو ناتلهزهركير وحمي ج‬
                                    ‫اعام‬
                                       ‫تليقّةوسلوال‬
                                                  ‫ده‬
 ‫لزهرة من‬
        ‫ع الاسوجي انباني الذي نقلهاذه‬                        ‫وأخغر وأصثر اسيةمّء‬
                                                 ‫المكسيك الى اسبانيا سئة ‪44/902‬‬
 ‫نوزة نت م ‪3 533‬ورك © وهو لامزبطك قرو النارنيةوعورةة‬
                                          ‫هو جرة صغيرة لها عروتان‬
‫دوزن القاون © ‪ -‬نري «دوزن» معناه تريب ونظام وعربيه بض ويظا‬
       ‫دوش ‪ -‬عامي افرنسي ‪636‬نا‪0‬ف معناه مزراب وميزاب مرادفه _منضخة‬
                                   ‫دوشك ‪ -‬نري « دأوشك » معناه فراش‬
                     ‫دوطة ‏”" ايطالي ‪ 6100‬معناه جهاز مرادفه مر وصداق‬
 ‫دوق ‪ -‬ايطالي هدس فيالاصل اللاتيني ناك معنا قائد وهو الآن لقب‬
                                                                ‫دون الامير‬         ‫'إرف‬
                      ‫دردبان ‪ -‬الطليعة ‪ -‬فارسي « ديدبان ‪ 6‬معناه ذو نظر‬

 ‫اوثاره لبجحرى عسلية اللحن‬   ‫‪ 0‬قولون دوزت الغنى القانون ونخوءط شد * ماارنخى من‬

                ‫‪0‬اككت أوتاره فاصطفق قال الشاعر‬
                                             ‫‏‪ ٠‬آل المرهرى ومبفقت ‪-0‬اذا‬

             ‫دم الزق عنا واعطفاق امزاهر‬          ‫قمر" ط‬    ‫كظل ال‬   ‫ووم‬

=== leaf 33 ===
                                          ‫ل لك‬




                 ‫ذعا ‏ فارسي « دييا© معناهنسيج من حرير ويطلق علىكل منسوج‬


‫‪-‬تيني ‪#‬انالئة‪ 061‬معناه عشري وهو نقد روماني قددىم يشتمل على‬
                                                         ‫دنار لا‬
                                    ‫عشر وحدات وكان الدينار عشرة درأهم عند العرب‬
         ‫©ناه يجنون أي الشيطان‬
                             ‫سي معناه شياطين وجان و « دبوانه مع‬
                                                              ‫انر‪--‬‬
                                                                  ‫فوا‬
                                                                    ‫دد‬
‫لتفقلامرنسية الىالارامية « دنوا » ومعناه شيطان ثنمقل على‬
                                                       ‫حالفيهفاقد‬
   ‫(قد‬
     ‫سبل المجاز ليدل علىكتاب القوانين والحسايات ومجلس المال الخ ‪ .‬م‬
 ‫|‬                                                                    ‫اخنلندون )‬
                                         ‫‪40‬‬   ‫‪- 2‬‬



‫معناه صم أي‬                ‫تارايربعاءنيالعتتويروأصله إوناني فصاع‬
                                                               ‫والكم ح ف‬

     ‫ظ‬                                 ‫مايسيل من الشجرة فينعقد مشتق هن ‪ 967‬سال‬
             ‫ريسية والتركية معناه دواء مُسهل وقيل انهاألصرلماز‬
                                                             ‫لدف‏ا ف‬
                                                                   ‫اون‬
                                                                     ‫را‬
         ‫ظ‬                                              ‫الهندي أونبات يطلق البطن‬
                                ‫رخت ‪ -‬فارسي ارت ‪#‬امماء الشترج والماسن‬
                        ‫رزداق ورستاق ‪ -‬فارسي ‪ 2‬روستا ‪ 4‬معناه القرى والسواد‬

 ‫رق وار ‪ -‬في اليونانية
```


## [2026-09-05T20:16:07.222Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%D9%88%D8%B4",
 "prompt": "Give the Persian entries: the etymology of دوش meaning \"shoulder\" and of دوش meaning \"last night\". Quote the Middle Persian, Old Iranian / Proto-Iranian and Proto-Indo-European reconstructions and cognates given."
}
```


## [2026-09-05T20:16:09.083Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%D8%B1%D9%88%DB%8C%D8%B4",
 "prompt": "Give the Persian etymology of درویش (darvīš): Middle Persian form, Avestan form, Proto-Iranian reconstruction, and any noted difficulties or alternative explanations. Quote exactly."
}
```


### [2026-09-05T20:16:13.966Z] TOOL RESULT

```
# Persian Etymology for دوش

## "Shoulder" (Etymology 2)

**Middle Persian origin:** Inherited from Middle Persian *dwš* (/dōš/)

**Older sources:** From Old Persian *dauš*, continuing from Proto-Iranian *\*dáwš*, and Proto-Indo-Iranian *\*dáwš*, ultimately from Proto-Indo-European *\*dóws* ("forearm")

**Cognates:** Avestan *daoš* ("forearm") and Sanskrit *doṣan* ("forearm")

## "Last Night" (Etymology 3)

**Middle Persian origin:** Inherited from Middle Persian *dwš* (/dōš/)

**Reconstruction chain:** From Proto-Indo-Iranian *\*dawšáH*, tracing back to Proto-Indo-European *\*dowséh₂*

**Cognates:** Younger Avestan *daošatara* ("located towards the evening, westerly") and Sanskrit *doṣā́* ("dusk; evening")

Both meanings descend from ancient Indo-European roots, with the "shoulder" sense preserving the body-part meaning while "last night" derives from temporal associations with evening.
```


### [2026-09-05T20:16:20.711Z] TOOL RESULT

```
# Persian Etymology of درویش (darvīš)

Based on the Wiktionary entry, here is the etymological breakdown:

**Middle Persian form:** The entry states the word comes "from [Middle Persian](https://en.wikipedia.org/wiki/Middle_Persian "w:Middle Persian") _[dlgwš](/wiki/dlgw%C5%A1#Middle_Persian "dlgwš")_ (/⁠driyōš⁠/)"

**Avestan forms:** Two related terms appear: "_[𐬛𐬭𐬌𐬔𐬎](/w/index.php?title=%F0%90%AC%9B%F0%90%AC%AD%F0%90%AC%8C%F0%90%AC%94%F0%90%AC%8E&action=edit&redlink=1 "𐬛𐬭𐬌𐬔𐬎 (page does not exist)")_ (drigu), _[𐬛𐬭𐬌𐬖𐬎](/w/index.php?title=%F0%90%AC%9B%F0%90%AC%AD%F0%90%AC%8C%F0%90%AC%96%F0%90%AC%8E&action=edit&redlink=1 "𐬛𐬭𐬌𐬖𐬎 (page does not exist)")_ (driγu, 'poor, needy')"

**Proto-Iranian reconstruction:** The entry references "a [Proto-Indo-Iranian](https://en.wikipedia.org/wiki/Proto-Indo-Iranian_language "w:Proto-Indo-Iranian language") root" and notes "[Old Iranian](https://en.wikipedia.org/wiki/Old_Iranian_languages "w:Old Iranian languages") _[\*drigu-](/w/index.php?title=Reconstruction:Proto-Iranian/drigu-&action=edit&redlink=1 "Reconstruction:Proto-Iranian/drigu- (page does not exist)")_"

**Cognates:** The entry mentions Sanskrit _[ध्रिगु](/w/index.php?title=%E0%A4%A7%E0%A5%8D%E0%A4%B0%E0%A4%BF%E0%A4%97%E0%A5%81&action=edit&redlink=1 "ध्रिगु (page does not exist)")_ (dhrigu, "needy") as a related term sharing this root.
```


## [2026-09-05T20:16:33.554Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%B4%CF%81%CE%B1%CF%87%CE%BC%CE%AE",
 "prompt": "Give the Ancient Greek etymology of δραχμή: which verb it derives from (δράσσομαι?), the literal meaning, and any related forms (δράγμα, δραγμή). Also list descendants in Arabic, Persian, Middle Persian, Armenian, Latin."
}
```


## [2026-09-05T20:16:35.411Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%D8%B1%D9%87%D9%85",
 "prompt": "Give the Arabic etymology of درهم (dirham): what language it is borrowed from and via what intermediary (Middle Persian? Greek? Aramaic?). Also give the Persian entry درهم / درم if present."
}
```


### [2026-09-05T20:16:40.312Z] TOOL RESULT

```
# Ancient Greek Etymology of δραχμή

## Derivation and Meaning

The word derives from the verb **δράσσομαι** (drássomai, "to hold, to seize"). According to the source, it functions as a "verbal noun ('holding')" of this verb.

However, scholar Beekes argues that variants like δαρχμά suggest a **Pre-Greek substrate origin** rather than standard Proto-Hellenic derivation.

## Descendants Listed

The document provides these descendants:

**In Persian languages:**
- Middle Persian: drahm

**In Indic languages:**
- Sanskrit: द्रम्म (drámma)

**In other languages:**
- Latin: drachma
- Old Armenian: դրաքմայ (drakʻmay), դրաքմէ (drakʻmē), դրագմէ (dragmē)

**Note:** The source does not list Arabic descendants or mention related forms like δράγμα or δραγμή. It does reference Bactrian, Khotanese, and Sogdian descendants but notes these lack native script representations in the available text.
```


### [2026-09-05T20:16:40.662Z] TOOL RESULT

```
# Etymology of درهم (Dirham)

## Borrowing Path

The Arabic word درهم is "Borrowed from Middle Persian 𐭦𐭥𐭦𐭭 (drahm), borrowed from Ancient Greek δραχμή (drakhmḗ)."

In summary: **Ancient Greek → Middle Persian → Arabic**

## Persian Entry

The Wiktionary page confirms a Persian descendant exists. Under the descendants section, it notes: "Persian: درهم (derham)," indicating the word also appears in Persian with a similar form.

The etymological chain demonstrates how this currency term traveled westward through major historical empires and trade networks, beginning with the Greek drachma and eventually becoming widely adopted across Islamic and Mediterranean regions.
```


## [2026-09-05T20:17:00.578Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/dram",
 "prompt": "Give the full etymology text for \"dram\" and, if shown, \"drachma\" and \"dirham\"/\"dirhem\"."
}
```


## [2026-09-05T20:17:00.998Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/dervish",
 "prompt": "Give the full etymology text for \"dervish\"."
}
```


### [2026-09-05T20:17:06.436Z] TOOL RESULT

```
# Etymology of Dram, Drachma, and Dirham

## Dram
"Mid-15c., 'small weight of apothecary's measure,' a phonetic spelling, from Anglo-Latin _dragma_, Old French _drame_" ultimately tracing to Greek _drakhma_, meaning "handful" and related to the verb "to grasp." The fluid dram (one-eighth fluid ounce) later developed the meaning "a small drink of liquor" by 1713, leading to the term "dram shop" for establishments selling liquor.

## Drachma
Originating in the late 14c., this term referred to an ancient Athenian coin and Greek unit of weight. The word derives from Greek _drakhme_, likely meaning "a handful" (specifically of six obols, the least valuable coins in ancient Athens), connected to the concept of grasping.

## Dirham
The page briefly mentions that Arabic _dirham_ derives from the Greek source, though it provides no additional etymological details beyond this connection to the drachma lineage.
```


### [2026-09-05T20:17:07.388Z] TOOL RESULT

```
# Etymology of Dervish

The word "dervish" originates from the 1580s, derived from Turkish *dervish*, which comes from Persian *darvesh* or *darvish* meaning "beggar" or "poor." This Persian term connects to Arabic *faqir* (see fakir entry).

The definition refers to an "Islamic monk or friar who has taken a vow of poverty and austerity." The term essentially describes a religious mendicant committed to austere living. The famous "whirling dervishes" represent just one order among many such Islamic groups.

The original English spelling was *dervis*, with the modern spelling becoming standard by the mid-19th century. The word entered English vocabulary during a period of increased contact with Islamic cultures, reflecting how English adopted terminology for religious practitioners from Muslim societies.
```


## [2026-09-05T20:17:15.165Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for f in MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt; do echo \"### $f\"; grep -c \"\" $f 2>/dev/null; grep -n \"درم\\b\" $f 2>/dev/null | head -3; done; echo \"=== search drahm in MON ===\"; grep -n \"drahm\\|dram\" MON_part1.txt MON_part2.txt 2>/dev/null | head -10",
 "description": "grep Mo'in files"
}
```


## [2026-09-05T20:17:15.629Z] TOOL CALL #43: WebSearch

```json
{
 "query": "Avestan drigu- \"poor\" etymology Proto-Iranian *drigu- Hasandust darvīš origin"
}
```


### [2026-09-05T20:17:17.275Z] TOOL RESULT

```
### MON_part1.txt
99339
1574:شدن» شرمگین گشتن. درم (,خحالت) 
2348:آدرم: 2027 [ « آذرم - آدرمه - آترمه ِ 
4080:ارتعاش درمی‌ آیند و آن رابه وسیلةً سر 
### MON_part2.txt
94500
775:این نوع غده‌ها دارای اصل مزودرمی 
832:رنگی درمی آید که در وسط قسمت محیطی 
1254:ظرفج: : لهاتم [- - گر فج] (ا.) درمنه که آتش 
### incoming/MON/MON_2vol_Adena_v1_djvu.txt
99339
1574:شدن» شرمگین گشتن. درم (,خحالت) 
2348:آدرم: 2027 [ « آذرم - آدرمه - آترمه ِ 
4080:ارتعاش درمی‌ آیند و آن رابه وسیلةً سر 
### incoming/MON/MON_2vol_Adena_v2_djvu.txt
94500
775:این نوع غده‌ها دارای اصل مزودرمی 
832:رنگی درمی آید که در وسط قسمت محیطی 
1254:ظرفج: : لهاتم [- - گر فج] (ا.) درمنه که آتش 
=== search drahm in MON ===
```


### [2026-09-05T20:17:26.014Z] TOOL RESULT

```
Web search results for query: "Avestan drigu- "poor" etymology Proto-Iranian *drigu- Hasandust darvīš origin"

Links: [{"title":"درویش - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D8%AF%D8%B1%D9%88%DB%8C%D8%B4"},{"title":"dlgwš - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/dlgw%C5%A1"},{"title":"dervish - Wiktionary, the free dictionary","url":"https://en.m.wiktionary.org/wiki/dervish"},{"title":"Are the words Dervish and Druid Cognates? | WordReference Forums","url":"https://forum.wordreference.com/threads/are-the-words-dervish-and-druid-cognates.2653397/"},{"title":"DARVĪŠ - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/darvis/"},{"title":"Avestan","url":"https://en.wikipedia.org/wiki/Avestan"},{"title":"♡ Dervish","url":"https://justsimplyinlove.wordpress.com/me/comment-page-1/"},{"title":"Dervish","url":"https://en-academic.com/dic.nsf/enwiki/222001"},{"title":"Darwish — Grokipedia","url":"https://grokipedia.com/page/Darwish"},{"title":"Dervish — Grokipedia","url":"https://grokipedia.com/page/Dervish"}]

Based on the search results, I found relevant information about the etymology you're asking about:

The Persian word darvīš derives from earlier daryōš, from Middle Persian dlgwš (/driyōš/), which comes from Old Iranian *drigu-, from a Proto-Indo-Iranian root shared with Sanskrit dhrigu ("needy") and Avestan drigu, driγu ("poor, needy").

More specifically, darvīš is a poor, indigent, ascetic person, derived from Avestan drəgu-, driγu- meaning "the needy one, dependent". The etymological chain shows Middle Persian driyōš "worthy poor, needy; one who lives in holy indigence"; Pāzand daryōš; and New Persian darγōš > daryōš > darvīš.

The Persian darvīš traces etymologically to Middle Persian driyōš, signifying "needy one" or "one who lives in holy mendicancy," with roots in Old Iranian and Avestan drigu-, an ancient term for "dependent" or "mendicant," with the Avestan corpus dating to approximately 1000–600 BCE.

The search results confirm the Proto-Iranian *drigu- origin and its connection to related Indo-Iranian terms, though I did not find specific information about "Hasandust" in these results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-05T20:17:34.139Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://www.iranicaonline.org/articles/darvis/",
 "prompt": "Quote the etymological paragraph on darvīš: the Middle Persian, Pāzand, Avestan forms and the phonetic development given (darγōš > daryōš > darvīš), and any comment on rival etymologies such as \"dar-pīš\"."
}
```


## [2026-09-05T20:17:35.555Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%AF%D8%B1%D9%85/",
 "prompt": "Show the فرهنگ معین (Mo'in) entry for درم and for درهم: the bracketed origin tag (e.g. [په.] Pahlavi, [ع.] Arabic) and the definition."
}
```


### [2026-09-05T20:17:36.081Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-05T20:17:41.231Z] TOOL RESULT

```
# فرهنگ معین Entries

## درم
**Origin tag:** (اِ.) [Islamic/Arabic origin]
**Definition:** "۱ - مسکوک نقره . ۲ - واحد وزن معادل شش دانگ"
(A silver coin; a unit of weight equal to six dangs)

## درهم
The page does not contain a separate فرهنگ معین entry specifically labeled for درهم. However, under "فرهنگ فارسی" (Persian lexicon), درهم is defined as: a silver currency unit (whose weight and value varied across different historical periods) and a weight measurement equivalent to six dangs.
```


## [2026-09-05T20:17:54.038Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== SYN shoulder ===\"; grep -n -i \"doṣ\\|dos-\\|Skt. dos\\|dōš\" SYN.txt | head -10; echo \"--- SYN 4.30 shoulder ---\"; grep -n \"SHOULDER\" SYN.txt | head -5; echo \"=== IEC dous ===\"; grep -n -i \"dousos\\|dous-\\|dōus\" IEC.txt | head -10",
 "description": "grep Buck and Mann"
}
```


### [2026-09-05T20:17:54.112Z] TOOL RESULT

```
=== SYN shoulder ===
5543:minus hunchback’)—whence It. dos- 8 (beside dorso), Br.,. Rum, dos i fr, deorswm fimedid . prob. as ‘sloping, steep’ (cf. abrup- 1 down’) ‘mountain ee later of men.
6108:Av. daog- ‘upper arm, shoulder’ (NPers. dog ‘shoulder’) : Skt. dos- ‘fore- arm’, Ir. doe ‘arm’, ete. Walde-P. 1.782. Pedersen 2.104.
6125:Ir. doe : Skt. dos- ‘forearm’, Av. daog-
8042:ME tyred, NE tired, pple. of ME tyre, OF teorian ‘fail, give out, become weak, exhausted’, perh. as Gme. *teuz-, IE *deus- : Skt. dosa- ‘fault, lack’, Grk. dé, Hom. dew ‘lack’, etc. Holthausen, IF 20.324. Walde-P. 1.782.
22305:Av. daogatara-, daogastara-, adj. (-3- fr. usastara- ‘eastern’), fr. *daogq- ‘eve. ning, west’ = Skt. dosa- ‘evening, dark- ness’ (prob. : dicis, etc., above, 1), Barth. 674. Walde-P. 1.777 f.
25427:6. Skt. dosa- (RV ete, AV also
29843:Skt. dosa- ‘fault, harm, guilt, sin’, fr. dus- ‘ill’ (16.72).
--- SYN 4.30 shoulder ---
6080:yprs OF TH ‘ Ilel forms with | nal throat. Walde-P. 2.634. NED s.v. 1, etc., beside par HG | throat na ‘swvel ALG. strotte, Du. strot, M pees : 3 init, 8, 28 } ¥, ME strouten ‘bulge, 6. Lith. gerklé, ChSl. griilo, etc., “hroa - s(ro22e oe aati an once, meaning dub., | above, 1. a: ell’ (OE 8 wut), ete., Temoter root Lett. rtkle (Lith. ryklé dial. or vulgar), of, NED 5. ee but immediate | fr. the root of Lett. ri, Lith. ryt ‘swal- . 3 | connections ee of ‘throat’ doubtless | low’. Mihl.-Endz. 3.537. semantic SoU ied first to the exter- 7. Skt. and Av. words, above, 1. ‘hulge, swell’, app41e 4.330 SHOULDER 2 Goth. amsans (acc. pl.) Lith. petys Crk. dyos ON herdr, oxl Lett.  plecs, kamiésis NG  dpos a Dan.  skulder ChSi. amo, pleste Lat. aa ate Sw. azel, skuldra SCr.  rame, pleéa It. Litite OE eal, sculdor Boh. _rameno, plece aa ME _ schulder Pol. — ramie, plecy (pl.) Ep. ee NE shoulder Russ. pleéo aoe ial formnt Du. schouder Skt.  skandha-, ansa- Sitios pala OHG - scultira, ahsala (cupli-) V ‘ ysgwydd MHG | schulter, ahsel Ay. supti- (daos-) Br. skoaz NHG | schulter, achsel
=== IEC dous ===
```


## [2026-09-05T20:17:55.088Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY; grep -n \"دوش\\|درویش\\|درم \" ARY_pages.txt | head -20; echo \"=== latin index ===\"; grep -n -i \"^DOUS\\|DOUS\\|DREGH\\|DRACHM\" ARY_latin_index_pages.txt | head -10",
 "description": "grep Aryanpur"
}
```


### [2026-09-05T20:17:55.142Z] TOOL RESULT

```
3058:۱ در برخی از زبان‌های هند و اروپائی این واژه به چم آشانه" و "دوش " هم به کار می‌رود.
3823:انا اد 8 (111611) درم ده من
8480:ٍ دوش (به چم "کتف") ۸۹1
13620:چم واژه‌های این فهرست (به جز اوستایی و پهلوی و فارسی و کردی و بلوچی و سانسکریت): شیر» شیر دوشیدن
13621:(شاید بدین علت که شبر دوشیدن ستلزم "مالش " با "مالیدن" است.)
=== latin index ===
4901:mndous, BLUSA ee PULGA SPANISH) gel
8173:DANT (WELSH) 59 ODON, ODOUS, ODONTOS
8205:TA, TAN | HITTITE) cca DoUS PORTUGUESE) gi
```


## [2026-09-05T20:18:17.494Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'PY'\nd=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nlines=d.split('\\n')\nleaf=0; leafof=[]\nfor l in lines:\n    leafof.append(leaf); leaf+=l.count('\\f')\nprint('dervish line 10994 leaf',leafof[10993])\nPY\necho \"=== BRT daos ===\"; grep -n \"daoš-\\|daosa-\\|daoš\\b\\|daos-\" BRT.txt | head -10",
 "description": "Klein leaf and Bartholomae daoš"
}
```


### [2026-09-05T20:18:19.216Z] TOOL RESULT

```
dervish line 10994 leaf 237
=== BRT daos ===
8700:•  j,  u^as'tara-  Adj.  'gegen  Morgen  ge- legen, östlich':  °taire  kinävd  (sd.)  , .  daosa- taire  V.57.29;  —  haca  °lara  hindva  (sd.) avi  daosaslanm  hindum  V.J.  18  PüZ.;  — -taräl  haca.  nalmitt  °taraalyi>  haca  nai- maiibyS  V.  ig.  5,
```


## [2026-09-05T20:18:30.254Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'PY'\nd=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=d.split('\\f')\nprint('leaves',len(pages))\np=pages[237]\nprint(repr(p[:300]))\nprint('...')\nprint(repr(p[-300:]))\nPY",
 "description": "inspect KLN leaf 237"
}
```


### [2026-09-05T20:18:33.058Z] TOOL RESULT

```
leaves 903
'nus  of  turtles  (zool.)  — ModL.,  compounded  of  dermo-  and  Gk.  /eX6p, ‘tortoise’.  See  Chelonia.\ndeni,  adj.,  hidden,  secret  (archaic).  —  ME.  derne, fr.  OE.  derne,  dierne,  ‘concealed,  secret,  dark’, rel.  to  OS.  derni,  OFris.  dern.  OHG.  tarni,  of s.m.,  OHG.  tarnjan,  MH'
...
'ated  base  of  stare, ‘to  stand’.  See  assist  and  cp.  words  there  re¬ ferred  to.\ndesistance,  n.,  the  state  of  desisting.  —  Formed fr.  prec.  word  with  suff.  -ance. desition,  n.,  cessation  of  being,  ending  — Formed  with  suff  -ion  fr.  L.  desitus,  ‘a  ceasing’, fr.  des'
```


## [2026-09-05T20:18:43.378Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'PY'\nd=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=d.split('\\f')\nfor i in (227,228):\n    print('=== leaf',i,'===',repr(pages[i][:150]),'...',repr(pages[i][-150:]))\nPY",
 "description": "inspect KLN leaf 227"
}
```


### [2026-09-05T20:18:44.976Z] TOOL RESULT

```
=== leaf 227 === 'ce’,  prop.  neut.  of  decretus,  pp.  of  de- cernere,  ‘to  pronounce  a  decision,  decide,  deter¬ mine’,  fr.  de-  and  cernere,  ‘to  separate' ... ',  defalcat-or,  n. defalcation,  n.,  embezzlement.  —  ML.  defal¬ cate,  gen.  -onis,  fr.  defalcatus.  See  prec.  word and  -ion.\ndefamation,  n'
=== leaf 228 === '.,  calumny,  aspersion.  —  ME.  dif- famacioun,  fr.  OF.  dijfamation,  fr.  L.  diffamd- tionem,  acc.  of  diffamatid,  fr.  diffamatus,  pp.  of' ... 'us,  pp.  of  definire.  See  de¬ fine.  L.  definitio  is  prop,  a  loan  translation  of Gk.  ijpia\\j.bc,,  which  derives  fr.  opi^eiv,  ‘to boun'
```


## [2026-09-05T20:19:00.626Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'PY'\nd=open('KLN_1971.txt',encoding='utf-8',errors='replace').read()\nn=len(d)\ni=d.find('dervish, n., a Mohammedan')\nprint('frac',i/n, 'est page of 844:', round(i/n*844))\nj=d.find('drachma, n.')\nprint('drachma frac',j/n,'est page:',round(j/n*844))\nPY",
 "description": "estimate 1971 Klein page"
}
```


### [2026-09-05T20:19:02.415Z] TOOL RESULT

```
frac 0.24707577557242683 est page of 844: 209
drachma frac 0.27447438641702054 est page: 232
```


## [2026-09-05T20:19:17.360Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY; sed -n '8465,8490p' ARY_pages.txt; echo \"--- page tag ---\"; awk 'NR<=8480 && /\\[pdf page/ {p=$0} END{}' ARY_pages.txt; grep -n \"\\[pdf page\" ARY_pages.txt | awk -F: '$1<8480' | tail -2",
 "description": "context of ARY dush mention"
}
```


### [2026-09-05T20:19:18.880Z] TOOL RESULT

```
فرانسه (07ظ۳): لاش 9 0و2
اسپانیایی (8۳۸۸/1873): 70 68 (030055) :7
ایتالیایی (۵(۷ه): ان ان 8 (001771) دنا ار
گرتبک (00777/0): 08۸0۲ ,ا87۸8ن۸1[ تام دی هی
ایسلندی کهن (01۸۸۵(۷آیت5 صان): 24 (0۷8ت) بکنة (318(0) اقا لبم
05۸ 2 (030088) :0102/5
ساکسونی کهن ((54200 010): 1108۸3 برهان قاطع : ۱ ۸۹۷
فریزی کهن (۸ها5ل7۴ صاه): :
یادداشت:
چم این واژه در زبان‌های هند و اروپایی کهن: خوشایند بودن» مزه دادن؛ لذات بردن» مزه.
چم این واژه در زبان‌های رمانس: مزه» میل,
چم این واژه در زبان‌های ژرمنی نوین: پسندیدن» گزیدن,
چم این واژه در زبان‌های یونانی: مورد پسند» ارزشمند. 1
[pdf page 288]
اک ی
ٍ دوش (به چم "کتف") ۸۹1
اوستایی (48874/۷): 2۸087۸ ,0۸05 4 ,30۸ بش00
پهلری (۲1اشاتلهه): 10 ولزی (7لل78): 71 ۱
افغانی (پشتو) (/470/۸۷): 0213۸ ,0573۸ ۱
سانسکریت (84۸/9777): پسگشت‌ها رده انا
8 ,)2350 +268 ,05375 6 ۸00000
لانین (7100 )+ رنه ۱ 8 (005) نظ ههام ات0
فرانسه (2/(3ق۳): 205 2 (1057آ81301) +5ل2 ۸/۸527
ایتالیایی (/مقاله7): 200 236 8
لیتوانی (۸[142تا777/): 03 0 (ت0038۸) +7
ایرندی کهن (بلدنقا صرا0): برهان قاطع + ۸۹۸
--- page tag ---
8449:[pdf page 287]
8478:[pdf page 288]
```


## [2026-09-05T20:19:31.824Z] TOOL CALL #53: Bash

```json
{
 "command": "mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg140.png data/verification/sources/refs/ocr/BOOK/140.png && ls -la data/verification/sources/refs/ocr/BOOK/140.png",
 "description": "copy page image for audit"
}
```


### [2026-09-05T20:19:31.889Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 70436 Sep  5 16:19 data/verification/sources/refs/ocr/BOOK/140.png
```


## [2026-09-05T20:19:38.452Z] TOOL CALL #54: Bash

```json
{
 "command": "for u in \\\n 'https://en.wiktionary.org/wiki/%D8%AF%D9%88%D8%B4' \\\n 'https://en.wiktionary.org/wiki/%D8%AF%D8%B1%D9%88%DB%8C%D8%B4' \\\n 'https://en.wiktionary.org/wiki/%CE%B4%CF%81%CE%B1%CF%87%CE%BC%CE%AE' \\\n 'https://en.wiktionary.org/wiki/%D8%AF%D8%B1%D9%87%D9%85' \\\n 'https://www.etymonline.com/word/dram' \\\n 'https://www.etymonline.com/word/dervish' \\\n 'https://abadis.ir/fatofa/%D8%AF%D8%B1%D9%85/' ; do\n python3 tools/fetch_source.py \"$u\" --note 'pdf page 140 (book p.110): roots Dous, Drassoman, Dregh — verification of dus/dos shoulder, darvis, drachme/dirham/deram' 2>&1 | tail -3\ndone",
 "description": "archive web sources"
}
```


### [2026-09-05T20:19:44.470Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/00af144fca24970c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/313c79c995d5d311.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c434670d4306d99a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2d72d82f2426ae03.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/93becea6c26d1ccf.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a1e8825b52d8f0bb.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/88fbfa042b2f6fdd.txt
```


## [2026-09-05T20:19:47.515Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '1,80p' tools/verify_check.py",
 "description": "read verify_check.py"
}
```


### [2026-09-05T20:19:47.556Z] TOOL RESULT

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


## [2026-09-05T20:19:50.545Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '80,140p' tools/verify_check.py",
 "description": "rest of verify_check.py"
}
```


### [2026-09-05T20:19:50.588Z] TOOL RESULT

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


## [2026-09-05T20:20:01.896Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; python3 - <<'PY'\nimport re\nd=open('WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\nfor m in re.finditer(r'daus-|dous-|daoš|daos-|dos-n|Vorderarm', d):\n    i=m.start()\n    print('>>>', d[i-350:i+350].replace('\\n',' '))\n    print()\nPY",
 "description": "grep WLD Bd1 for dous"
}
```


### [2026-09-05T20:20:03.674Z] TOOL RESULT

```
>>> iickbleiben" (nach Sievers zur germ. Wz. *terh-).     Aber anord. tjon „Schaden, Yerderben", ags. teona teone „Schaden, Un-            ,   recht,  Yerhohnung" (Wood Min. 22, 121) nicht zu einer (eben auch durch  ai. dura-, ddviyas- nicht gestiitzten) kiirzern Wzf. *deu sondern vielleicht  zu dciu- ,.brennen",           s.   d.    2.    deus- (oder dous-)             „Arm\        Ai. dos- n. (m.), gen. dosmh                                  „Yorderarm, Arm, unterer Teil des Vorder-  fuBes bei Tieren“, av. davs- m. ,Oberarm, Schulter", npers. dos „Schulter‘‘';  air. doe, gen. doat „ Arm"   lett. pa-duse (tiefstufig) „Achselhohle                                              ;
```


## [2026-09-05T20:21:25.812Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"AHD dregh:\"; grep -c \"dregh\" AHD_watkins1985.txt; echo \"AHD dous:\"; grep -c \"dous-\\.\" AHD_watkins1985.txt; echo \"=== BRT daos- around col 674 ===\"; grep -n \"^67[3-6]$\" BRT.txt | head; ",
 "description": "check AHD and BRT columns"
}
```


### [2026-09-05T20:21:28.191Z] TOOL RESULT

```
AHD dregh:
0
AHD dous:
0
=== BRT daos- around col 674 ===
12530:673
12533:674
12580:676
```


## [2026-09-05T20:21:30.629Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '12525,12580p' BRT.txt",
 "description": "print BRT col 673-676"
}
```


### [2026-09-05T20:21:30.717Z] TOOL RESULT

```
')  Hds.  daiiS.där'.  vgl.  za. ftcUimatil-  No.  \.\*dalst^!U  pantqm    Vyt  42\  *F.  /4'*;    —
•  j.  daevö.tama-  Adj.  'der  am  ta.i\^QTi\fravasayS ..yhitrvaraHqm..srlräurukmts Dafva  ist,  YAzdaliiä':  dacvanqm  'vum  YX.'' dalsayeinii  YtJ_j.  55;  —  at  tu  mUi  daü J.14';  —  daevü  paitiss  daluS  daei'anqm  (i^s-hatK^^  astm  kyatmä  zaozaomx'^\AS& °tnö  V.  75. 43.  |mich  das  A.  sehen,  nach  dem  ich  rufe'*
ai.  vgL  dc.aiama-  Adj.  —  Pü.:  fehlt  ,  Y.  43. 10  {Zar.  Spricht).         3)  'jemandem
•  j.  daevö.däta-  Adj.  (fem.  HH-')  'von  (Dat)  etwas  zuweisen,  zusprechen,  zu- den /^d^'d  geschaffen': /•in.i/vt  i/^mu  °/^m  sichern':    Msä  (3Sf-AorM.)^   mSi   istoif
dby  Google
673
dae»-  mit  avi
dauStar-
674
(sd.)  xiii'^fvm  Y.  51.  a;  —  6>rtx&am  mSi forasaeitrS  kvB.gvl!  däedöii't'i*  kihrpsm  .  . yam  . .  i^am  (sd.)  "den  geschätzten  Leib'' der  lieben  (Jui^;frau)  hat  mir  FrMv.  zuge- sprochen, welcher  . ."  Y.5J.  17;  —  <^^st (Pass.)*'  he a^Ae  avai  miiäfm{^) ..ya%a .. ^3-Tt  ^-5-44;  —  srTra  p^nsS  disyata yaha  mOvaya  ..Vyi.ß^i'i);  — jimama  tl dalsayama  U  .  .  Vyt_j2(?)  a)  '(Strafe) zuweisen  sva.  festsetzen':  avavantfm  asa- vaynyai  (sd.)  tqm  S^qm  daisayS  V.  5. 14.  3)  'Jemanden  (Dat-)  unterweisen in  — ,  belehren  über  — '  (Akk.):  ahmai  dal- nam  dalsayat  ahurd  Yt.  II.  14.  4)  'kund machen';  iä^a(ßd.)  ayärS ..firasayai dlsS (sSj-AorM.)  \.43-l.  5)  '(Jemandem) durch  —  (Instr.)  darauf  hinfuhren,  dazu verleiten,  dass  er—'  (KeUtivum):  «7a  dalna disyät  . .  yS  %riummaim  ratBm  aiwyän- kam  (sd.)  «Ji^  ahvyästi  V.  18.  9.
mit  ain,  aoi  1)  dnwS.  z  :  pasätSa  at>m yS  aAwö  .  .  aoi  urune  urväsma  (sd.)  dal- sayeni  P.J<¥.  t)  dnwS.  4:  yi' .  .y3^wa ..m^rrffnte  avi  tu  dim  disyatayh  apasca.. ". ,  den  macht  uns  kund,  ihr  Wasser und  .."  Y.Ä3.
mit  frä  dnwS.  3 :  koAmäi  fradasayö dalnam  V.  2.  i ;  —  ahmäi  fradalsaim  dag- nam  V.  2. 2;  —  aet?m  mq%nm  ma  fra- daesaysi^  ainyal  pihre  va  .  .  Yt.  14.  4Ö*'. mit  harn  Med.  'sich  weisen  lassen  in  — (Akk.),  sich  etwas  gesagt  sein  lassen': inja  avat  AandalsayaauÄa  .  .  yai  . .  "zu- rück !  lass  dir  das  gesagt  sein,  . . :  wenn . .'' Yt.ig.^8;  50.
ai,  äiiäti,  dldiiai,  diiyaii,  äeiayaä,  adii^i; woss.  äwdttu«.  —  PQ.  (lu  \.43,  Vi.  //,  V.  2, tS,  F.  14) :  nimütan ;  {in  V.  5,  p,  P.  38,  Y.  S) : nikeaian,  (tu  Y.  S)  erl. :  ftäiä*  ape  kartan  %  s. «och  No.  »f.  —  '>  Hds.  daev'.  —  »)  PB.: doMe,  Sa.:  diHL~il  Pfl.:  daAäl,  Sä.:  d^hi. 4)  NäinL  seinei  Tochler  znr  Ehe.  Pü.i niiebin  HÜeiil,  etl. :  iuia  dtal  ianih  afie  dahil. S.  anch  Dk.  g.  44.  17.  —  5)  Zu  S  S^S- ')  Vgl.  Yt.  4.  9,  wo  fradaxscQiö.
•  j.  daesa-  m.  'Zeichen,  Otnea':  pattiHatSe ayanqmca    :^a/nanqm    ayanqmca
VL/J.  104-
Zum  V.  dais-,  —  ai.  deli-  m.  'Gegend';  nip. uidfs  'Gätzenbild',  np.  'des  'ähnlich';  s.  dazu HOKN  GIrPb.  /  b.  35.
•  '}.  daez-  V.  'häufen,  schichten'  (Erde, Steine);  nur  mit  Praev,  Praes.  i  du-, 30  (Iter.)  da&aya-.  —  PPfP.  'dis'ta-'-\
mit  US  -aufhäufen,  -schichten,  -dämmen,
■mauern':  yS  latitn  utäalum  utdiäa'^ (3SPrM.)  "wer  diesen  Damm  (Mauer)  er- richtet haf  V. /5,  36;  —  affaXiva  dax- W  . .  ysi  bavairiti  (sd)  usdagia  us- dista'^  (NPm.)  V.7.S4.
mit  pairi  'rings-,  rundum  aufdämmen, mauern':  altera  he  alte  masdayasna  ai^ha e^rnH  pairi.dalxan  (sd)  pairi.datzayan  V. 3.  18.
Ar.  "dhailh-  {ygl.  oA. /eiAkss);  ai.  dlgdhi*^: diAänIi;  digdAäk').  —  Pii.:  umschreibt  mit däian  oder  kattan.  —  ')  S  5J  n.  —  »)  Mit inalogischem  gdh,  Sp.  413  n.
j.  daiza-  m.   "Häufen,   Schichten'  von Erde,  Steinen. KompE.  —  Zum  V.  dan-,  —  np,  dcz  "Burg', gr.  «rxoe  'Mauer',   osk.  /eihius  (AP.)   'WafP; ü.  deka-  m.  'Körper'.
j.  daoi^ri-  'Spruch,  Rede'uzw.  i/nji/ischer
Wesen,    nur  mit  aya-  Adj.:   frattrase  .  .
ayqm  °rTm  daomnl  Yt  jp.  57;  —    arfqm
■rfm  daunta  daiva  V,  ig.  45.
Zum  V.  Uav;  auffällige  BildangO.    —    Pü.:
Tehlt.  —  ')  Die  Stämme  auf  Vi-  bilden  sonst
die  Fem.  zn  den  Nom.  ag.  auf  l(0':    VgL  zu
j.  daanijailii  N.  6^:  \w%  tat^.J'.
i  j.  daonrna-  Adj,  (fem.  °na-),  PPM.:  s.
'dav-.
•  p.  dauä-  V,:  s.  unter  zao^-.
•  j.  daoä-  m.  'Oberarm,   Schulter":    "Ä
(ND,)F.  _3g;  —  cvat  na  *mt?>na  alsmahe (sd.)  paitiiarS  ratufriii  yaha  vansnahe kihrpahe  äSus  (NS,)  ".  •  (so  gross)  als  der Oberarm  eines  Mannesleibes"  N.  S06;  F. 14"-
ai.    ddf-   in.,   n.  'Vorderarm';    mp.  (Fa.),   np.
dsi   ■Schulter'.  —   t)  Wo  pü.  auigefttllen   ist
Unrichtig  WZKM.  y.  143.
■  j.daoäa'tara-,  dao^s'tara-  Adj.'^  'gegen
Abend  gelegen,  westlich' :  usastaire  hindvö.
(sd.)  . .  -iataire  Y.  57,  39;  —  hala  usastara
hifidva    avi  'iastanm    hgndüm  (sd)  V.  t.
18  PüZ.
Ableit,   aus   ^dao'sä-  f.  'Abend,    Westen';    ai.
deiä-  f.  'Dunkel,    Abend',    np.  dös  'die  letit-
vergangene    Nacht'   (s.  dazu   BtHU   BB.  IS-
208).  —  mp,  (Pü.)  dösastar;  s.  No.  I.  —  •»  Das
s  stammt  von  dem  gegensätzlichen  ahulara-;
Tgl.  ai.    HfisB   difäiaJea   AV.  i6.  4-  &   (wozu
Lanman  JAOS.  io.  468).
•  p.  dauiltar-  m.  'Freund,  zugetan':  hyt^ 'ta  ahJ'  .  .  hy<^  arike^  äkJ'  Bh.  /. 8.       i)  'Gönner,  gewogen',  mit  Akk.  der
dby  Google
67S
""daozavät
'daxäta-
676
```


## [2026-09-05T20:29:42.705Z] TOOL CALL #60: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk140.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\ndata = {\n \"pdf_page\": 140,\n \"book_page\": 110,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [\n\n  # ------------------------------------------------------------------ Dous\n  {\n   \"entry\": 1,\n   \"root\": \"Dous\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *dóws / *dews- ~ *dous- 'forearm, arm' (Pokorny 226; Walde-Pokorny I 782)\",\n   \"note\": \"The root, the language label and the gloss are all right. Pokorny p.226 has 'Root/lemma: dous- Meaning: arm', and Walde-Pokorny I 782 heads it '2. deus- (oder dous-) „Arm“'. Its witnesses are Skt. doṣ- 'forearm', Av. daoš- 'upper arm, shoulder', NPers. dōš 'shoulder', OIr. dōe (gen. doat) 'arm', Latvian pa-duse 'armpit', OCS pazucha. Because the root is confined to Indo-Iranian, Celtic and Balto-Slavic, Watkins/AHD does not list it at all (grep of AHD_watkins1985.txt for 'dous' = 0 hits), so Nourai's 'Indo-European' label is correct but the root is a restricted, not a pan-IE, one. Wiktionary reconstructs it as PIE *dóws 'forearm'. Pokorny's own note that the root is a d-variant of an archaic *gheus- 'hand, arm' is speculative and is not needed for the two arrows on this page.\",\n   \"note_fa\": \"ریشهٔ هندواروپایی آغازین *dóws (صورت‌های دیگر: *deus-/*dous-) به معنای «بازو، ساعد» ریشه‌ای واقعی است و پوکورنی (ص ۲۲۶) و والدهٔ‌پوکورنی (ج۱ ص ۷۸۲) همان معنا را می‌دهند. گواهان آن سنسکریت doṣ-، اوستایی daoš-، فارسی «دوش»، ایرلندی کهن dōe و لتونیایی pa-duse است. چون این ریشه فقط در شاخه‌های هندوایرانی، سلتی و بالتیک‌اسلاوی مانده است، واتکینز (پیوست ریشه‌های AHD) آن را نیاورده است. ادعای نورایی درست است.\",\n   \"sources\": [\"https://en.wiktionary.org/wiki/%D8%AF%D9%88%D8%B4\"],\n   \"ref_check\": [\n    {\"ref\": \"POK:226\", \"status\": \"supports\",\n     \"note\": \"POK_full.txt (lines 23339-23356), 'Page(s): 226': 'Root / lemma: dous- | Meaning: arm ... Material: Old Indic dos- n. (m.), Gen. dosnah ‘forearm, arm ...’, Avestan daos- m. ‘upper arm, shoulder’, npers. dos ‘shoulder’; Old Irish doe (*dous-nt-s), Gen. doat ‘arm’ ... References: WP. I 782'. Exactly the root, gloss and both arrows Nourai draws.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. I 782 (WLD_Bd1_pages.txt)\", \"stance\": \"supports\",\n     \"note\": \"'2. deus- (oder dous-) „Arm“. Ai. dos- n. (m.), gen. dosnah „Vorderarm, Arm, unterer Teil des Vorderfußes bei Tieren“, av. daos- m. „Oberarm, Schulter“, npers. dos „Schulter“; air. doe, gen. doat „Arm“; lett. pa-duse (tiefstufig) „Achselhöhle“'.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 4.30 SHOULDER (SYN.txt line 6108)\", \"stance\": \"supports\",\n     \"note\": \"'Av. daos- ‘upper arm, shoulder’ (NPers. dos ‘shoulder’) : Skt. dos- ‘forearm’, Ir. doe ‘arm’, etc. Walde-P. 1.782. Pedersen 2.104.'\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 appendix\", \"stance\": \"silent\",\n     \"note\": \"grep of AHD_watkins1985.txt for 'dous' / a 'dous-' lemma returns 0 hits; Watkins omits this restricted root, so Nourai's chart has no AHD counterpart here.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Avestan\",\n     \"words\": \"daoš\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Avestan daoš- m. is a real s-stem meaning 'upper arm, shoulder' (Bartholomae, AiW col. 674: '• j. daos- m. ‘Oberarm, Schulter’', attested F.39 and N.106). It is the o-grade *dous- of the root: PIE *ou > Proto-Iranian/Avestan ao, and the root-final *s becomes š after the u-diphthong by the ruki rule, giving daoš-. Its exact Indic match is Skt. doṣ-/doṣán- 'forearm' (RV), and outside Indo-Iranian OIr. dōe 'arm' (< *dous-nt-s). Nourai's arrow root → Avestan is therefore correct; the only quibble is that the chart gives the bare stem 'daoš' without the stem marker.\",\n     \"derivation_fa\": \"اوستایی daoš- (ستاک s‌دار) به معنای «بازوی بالا، کتف» واقعاً در متن اوستا آمده است و بارتولومه (ستون ۶۷۴) آن را به همین معنا ثبت کرده است. این صورت مرتبهٔ آوایی o ریشه است: دوگانه‌واکهٔ هندواروپایی *ou در ایرانی باستان به ao بدل شده و s پایانی برپایهٔ قاعدهٔ روکی (ruki) پس از u به ش بدل گشته است. هم‌ریشهٔ دقیق آن در سنسکریت doṣ-/doṣán- «ساعد» است. ادعای نورایی درست است.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/%D8%AF%D9%88%D8%B4\"],\n     \"ref_check\": [\n      {\"ref\": \"POK:226\", \"status\": \"supports\",\n       \"note\": \"Pokorny p.226 s.v. dous-: 'Avestan daos- m. ‘upper arm, shoulder’' stands directly under the root, i.e. the arrow root → Avestan is Pokorny's own.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"AiW col. 674 (BRT.txt lines 12533-12570)\", \"stance\": \"supports\",\n       \"note\": \"'• j. daos- m. ‘Oberarm, Schulter’: ... ai. dos- m., n. ‘Vorderarm’; mp. (Pü.), np. dos ‘Schulter’.' Bartholomae gives the Avestan word, its Sanskrit match and the Middle/New Persian continuation in one line.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. I 782\", \"stance\": \"supports\",\n       \"note\": \"'av. daos- m. „Oberarm, Schulter“' listed as the Iranian witness of *deus-/*dous-.\"},\n      {\"src\": \"SYN\", \"where\": \"Buck 4.30\", \"stance\": \"supports\",\n       \"note\": \"Buck's Avestan slot for SHOULDER reads 'Av. supti- (daos-)', with the note quoted above.\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Persian\",\n     \"words\": \"dŭš\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"NP دوش dōš 'shoulder' is the regular continuation of Old Iranian *dauš- through Middle Persian dōš (MacKenzie, CPD: 'dōš [dws | N ~] shoulder'): the Old Iranian diphthong *au monophthongised to Middle Persian ō, which New Persian keeps as the wāw-e majhūl, hence the spelling دوش. Strictly the word is not a descendant of the Avestan form but of its Old Persian sister, so the chart's Avestan → Persian arrow is a shorthand for 'Old Iranian'. The '۲' in the script field is Nourai's homonym index: دوش 1 is 'last night' (< MP dōš < *daušā-, Av. daošatara- 'westerly'), an unrelated word that happens to fall together. Nourai's transliteration 'dŭš' with a breve is non-standard; the sources write dōš. Mo'in's footnote at Borhan p.898 states the chain expressly.\",\n     \"derivation_fa\": \"«دوش» به معنای کتف از فارسی میانه dōš می‌آید (مکنزی: dōš «کتف») و آن از ایرانی باستان *dauš- است؛ دوگانه‌واکهٔ au ایرانی باستان در فارسی میانه به واو مجهول (ō) بدل شده و همین املای «دوش» را پدید آورده است. دقیق‌تر آن که فارسی نو فرزند اوستایی نیست بلکه دنبالهٔ صورت هم‌زاد پارسی باستان است و پیکان کتاب کوتاه‌نوشتی است برای «ایرانی باستان». عدد ۲ در کتاب برای جداکردن این واژه از «دوش» به معنای شب گذشته است که ریشهٔ دیگری دارد (اوستایی daošatara- «باختری»). حاشیهٔ معین بر برهان قاطع (ص ۸۹۸) همین زنجیره را می‌آورد. ترجیحاً باید dōš نوشت، نه dŭš.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/%D8%AF%D9%88%D8%B4\"],\n     \"ref_check\": [\n      {\"ref\": \"BQT:898\", \"status\": \"supports\",\n       \"note\": \"Borhan-e Qate' ed. Mo'in p.898 (BQT_v2_pages.txt leaf 358), headword 'دوش ... بمعنی کتف باشد' with Mo'in's footnote 1: 'اوستا daoša- (شانه، کتف)، پهلوی dōš، هندی باستان doṣan-, doṣ- (بازو، ساعد)' — exactly Nourai's arrow (footnote 7 on the same page covers the homonym دوش 'last night').\"},\n      {\"ref\": \"HRN:130\", \"status\": \"supports\",\n       \"note\": \"Horn, Grundriss no. 584, printed p.130 (HRN.txt leaf 151): '584. (2)dōs ‘Schulter’. aw. daoša- ‘Schulter’ (ZPGl); phlv. dōs; ai. doṣ-, doṣán- ‘Vorderarm, Arm’.' The page number is exact.\"},\n      {\"ref\": \"POK:226\", \"status\": \"supports\",\n       \"note\": \"Pokorny p.226 s.v. dous- lists 'npers. dos ‘shoulder’' beside the Avestan word.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD p.26 s.v. dōš (PHD.txt line 314)\", \"stance\": \"supports\",\n       \"note\": \"'dōš [dws | N ~] shoulder.' followed immediately by 'dōš [dws | N ~] last night, previous evening' — the Middle Persian link the chart leaves implicit.\"},\n      {\"src\": \"HUB\", \"where\": \"Persische Studien (HUB.txt line 8292)\", \"stance\": \"supports\",\n       \"note\": \"'... dōs ‘Schulter’ H. 584; dušman ‘Feind’ H. 565' — Hübschmann files the word under Horn no. 584, i.e. he accepts Horn's Avestan etymology.\"},\n      {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e rishe-ha, pdf p.288 = printed p.289 (ARY_pages.txt line 8480)\", \"stance\": \"supports\",\n       \"note\": \"Headword 'دوش (به چم «کتف»)' with the cognate list 'اوستایی: DAOSH, DAOSHA — پهلوی: DOSH — سانسکریت: DOSHAN, DOSH ...' and the cross-reference 'برهان قاطع ۸۹۸' — an independent modern Persian source that also points to Nourai's own BQT page.\"},\n      {\"src\": \"SYN\", \"where\": \"Buck 4.30 SHOULDER\", \"stance\": \"supports\",\n       \"note\": \"'Av. daos- ‘upper arm, shoulder’ (NPers. dos ‘shoulder’)'.\"}\n     ]\n    }\n   ]\n  },\n\n  # ------------------------------------------------------------- Drassoman\n  {\n   \"entry\": 4,\n   \"root\": \"Drassoman\",\n   \"verdict\": \"transcription_suspect\",\n   \"modern_form\": \"Ancient Greek δράσσομαι (drássomai, Attic δράττομαι) 'to grasp, clutch, take a handful'\",\n   \"note\": \"There is no Greek word 'Drassoman'. The printed page (pdf p.140, image kept at data/verification/sources/refs/ocr/BOOK/140.png) really does read 'Drassoman', so this is Nourai's own misprint/mis-transliteration, not an extraction slip; the word he means is δράσσομαι drássomai, which is exactly the form Jeffery prints on the page Nourai cites (FVQ 130: 'deriving it from δράσσομαι'). The gloss in the box is likewise Jeffery's sentence about the noun δραχμή ('as much as one can hold in the hand', then a measure of weight, lastly a coin), not the meaning of the verb, which is simply 'to grasp'. The etymology δραχμή < δράσσομαι is the traditional one (LSJ, Klein, Skeat, Lokotsch, Jeffery) but not unanimous: Beekes (EDG) takes the by-form δαρχμά as a sign of Pre-Greek origin. Nourai's label 'Greek' for the root box is right — unlike most boxes on these pages this is not an Indo-European reconstruction.\",\n   \"note_fa\": \"سر‌واژهٔ «Drassoman» در یونانی وجود ندارد؛ صورت درست δράσσομαι (drássomai) «در مشت گرفتن، چنگ زدن» است. با دیدن تصویر صفحهٔ چاپی (ص ۱۱۰ کتاب) روشن شد که همین صورت غلط در خود کتاب چاپ شده است، پس خطای خوانش اسکن نیست بلکه خطای چاپی کتاب است. معنایی هم که در جعبه آمده معنای اسم δραχμή است نه معنای فعل. ریشه‌شناسی سنتی (لیدل و اسکات، کلاین، جفری) δραχμή را از همین فعل می‌گیرد، ولی بیکس به سبب صورت کناری δαρχμά آن را وام‌واژه‌ای پیشایونانی می‌داند.\",\n   \"error_in\": \"book\",\n   \"book_prints\": \"Drassoman\",\n   \"correct_form\": \"drassomai (δράσσομαι)\",\n   \"sources\": [\"https://en.wiktionary.org/wiki/%CE%B4%CF%81%CE%B1%CF%87%CE%BC%CE%AE\", \"https://www.etymonline.com/word/dram\"],\n   \"ref_check\": [\n    {\"ref\": \"FVQ:129\", \"status\": \"supports\",\n     \"note\": \"Jeffery, Foreign Vocabulary of the Qur'an p.129-130 (FVQ_pages.txt leaves 146-147): 'Liddell and Scott, however, are doubtless right in deriving it from δράσσομαι and meaning originally “as much as one can hold in the hand”, then a measure of weight and lastly a coin.' Nourai's root box is a verbatim paraphrase of this sentence — including the wording of the gloss.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. dram (KLN_1966.txt line 12221, ~p.467)\", \"stance\": \"supports\",\n     \"note\": \"'... fr. Gk. δραχμή, ‘an Attic weight; a silver coin’, lit. ‘a handful’, rel. to δραγμή, ‘handful’, δράγμα, ‘a sheaf’, lit. ‘as much as one can grasp, a handful’, from the stem of δράσσεσθαι (for *δράχ-ιεσθαι), ‘to clutch, grasp, seize’.'\"},\n    {\"src\": \"SKT\", \"where\": \"Skeat s.v. Dram, Drachm (SKT.txt line 5387)\", \"stance\": \"supports\",\n     \"note\": \"'Gk. δραχμή, a handful, a drachm, used both as weight and coin: cf. δράγμα, as much as one can grasp. — Gk. δράσσομαι, I grasp.'\"},\n    {\"src\": \"LKT\", \"where\": \"Lokotsch no. 523 'dirhem' (LKT.txt line 1348)\", \"stance\": \"supports\",\n     \"note\": \"'das ar. Wort kommt selbst aus gr. δραχμή ... das auf δράττω, δράττομαι zurückgeführt wird u. soviel wie „eine Handvoll“ ... bedeutet' — the Attic spelling of the same verb.\"},\n    {\"src\": \"WIKT\", \"where\": \"en.wiktionary.org δραχμή\", \"stance\": \"partial\",\n     \"note\": \"Derives δραχμή as a verbal noun ('holding') of δράσσομαι, but adds that Beekes takes variants like δαρχμά to show Pre-Greek origin.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Greek\",\n     \"words\": \"draxmon, draxmě\",\n     \"verdict\": \"transcription_suspect\",\n     \"derivation\": \"'draxmě' = δραχμή (drakhmḗ) is right in every respect: an Attic weight of six obols and the silver coin struck to it, formed as a verbal noun on the *δραχ- grade of δράσσομαι (< *δράχ-ιομαι), beside δραγμή 'handful' and δράγμα 'sheaf'. 'draxmon' is not: no Greek *δράχμον is attested as an independent word, the neuter appearing only in compounds such as δίδραχμον 'two-drachma piece' (Klein s.v. didrachma). The printed page shows 'draxmon, draxmě', so the odd form is the book's, not the extraction's. The NOTE 'This may be from a Semitic root' reproduces Jeffery p.129, who reports Boisacq's and Levy's attempt to link Heb./Phoenician drkmn/darkemon and the Persian gold daric — and then rejects it; the Semitic option has no modern following (Beekes's Pre-Greek is today's alternative).\",\n     \"derivation_fa\": \"صورت draxmě یعنی δραχμή درست است: واحد وزن آتنی برابر شش اوبول و سپس سکهٔ نقره، و از دید ساخت اسم‌مصدری است از ستاک *δραχ- فعل δράσσομαι، در کنار δραγμή «یک مشت» و δράγμα «دستهٔ خوشه». امّا draxmon واژه‌ای مستقل در یونانی نیست و صورت خنثای آن فقط در ترکیب‌هایی مانند δίδραχμον دیده می‌شود؛ این هم خطای چاپی کتاب است (با دیدن تصویر صفحه تأیید شد). یادداشت کتاب دربارهٔ ریشهٔ سامی عیناً از جفری (ص ۱۲۹) گرفته شده که خود او آن را رد می‌کند؛ پژوهش امروزی نیز گزینهٔ سامی را نمی‌پذیرد.\",\n     \"error_in\": \"book\",\n     \"book_prints\": \"draxmon, draxmě\",\n     \"correct_form\": \"drakhmē (δραχμή); the neuter -δραχμον only in compounds (δίδραχμον)\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/%CE%B4%CF%81%CE%B1%CF%87%CE%BC%CE%AE\", \"https://www.etymonline.com/word/dram\"],\n     \"ref_check\": [\n      {\"ref\": \"FVQ:129\", \"status\": \"supports\",\n       \"note\": \"FVQ p.129: 'The ultimate origin is the Gk. δραχμή, which passed into Syr. as ...; Some, however, would derive δραχμή from a Semitic source. Boissacq suggests this, and Levy, Fremdw, 118, connects it with Heb. drkmn ... which is the Persian gold Daric' — i.e. both the word and Nourai's NOTE come from this page. Jeffery gives δραχμή, never a form 'draxmon'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. drachma / didrachma (KLN_1966.txt lines 12194, 11353)\", \"stance\": \"supports\",\n       \"note\": \"'drachma, n., 1) an ancient Greek coin; 2) an ancient Greek weight. — L., fr. Gk. δραχμή'; and 'didrachma ... fr. Gk. δίδραχμον, ‘a two-drachma piece’' — the only place a -δραχμον neuter occurs.\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat s.v. Dram\", \"stance\": \"supports\",\n       \"note\": \"Gives δραχμή only, glossed 'a handful, a drachm, used both as weight and coin'.\"},\n      {\"src\": \"LKT\", \"where\": \"Lokotsch no. 523\", \"stance\": \"supports\",\n       \"note\": \"Same derivation of δραχμή from δράττομαι, 'eine Handvoll'.\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Arabic\",\n     \"words\": \"derham\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"Arabic درهم dirham (plural دراهم darāhim, the only form in the Qur'an, Yūsuf 12:20) is beyond doubt ultimately Greek δραχμή; it was already in pre-Islamic poetry ('Antara xxi.21), and the Arab philologists themselves treated it as a loan (al-Jawālīqī, Mu'arrab 66; al-Tha'ālibī, Fiqh 317). What is questionable is the direct Greek → Arabic arrow. Jeffery, on the very page Nourai cites for the note, says the word 'passed into Iranian first as a measure of weight and then as a coin', and that Phlv. dram/draxm 'may be assumed as the source of the Ar. درهم also', an 'early borrowing from the Mesopotamian area'; the -h- of dirham points to the Middle Persian drahm rather than to Greek -χμ- directly, and today's standard account (Wiktionary; Asbaghi) is Greek → MP drahm → Arabic dirham. Klein, on the other hand, writes simply 'Arab. dirham, fr. Gk. δραχμή', i.e. the chart's arrow. Nourai's own NOTE flags the Pahlavi route, so the box is defensible but the arrow should really run from the Pahlavi node.\",\n     \"derivation_fa\": \"«درهم» عربی (جمع: دراهم، در قرآن سورهٔ یوسف ۱۲:۲۰) بی‌گمان در نهایت از یونانی δραχμή است، امّا پیکان مستقیم «یونانی و عربی» جای چون و چرا دارد. جفری در همان صفحه می‌گوید که واژه نخست به ایرانی راه یافته و صورت پهلوی drahm منبع واژهٔ عربی است؛ وجود «ه» در dirham نیز به میانجیگری فارسی میانه اشاره دارد، نه به وام‌گیری مستقیم از یونانی. دیدگاه امروزی (ویکی‌واژه، اصبغی) زنجیرهٔ یونانی ← فارسی میانه ← عربی است. پس با احتیاط پذیرفتنی است و خود نورایی هم در یادداشت به این احتمال اشاره کرده است.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/%D8%AF%D8%B1%D9%87%D9%85\"],\n     \"ref_check\": [\n      {\"ref\": \"TAD:27\", \"status\": \"supports\",\n       \"note\": \"Tobia al-Unaysi, Tafsīr al-alfāẓ al-dākhila (TAD_pages.txt leaf 30, printed p.~27, in the run دردي – دوسر): 'درهم — يوناني δραχμή وهو نقد فضة ووزن أيضاً ... درم الفارسي'. Exactly Nourai's Greek → Arabic arrow and his gloss ('a coin and also a unit of weight'); the same page also carries the درويش entry quoted in the Dregh chart.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. dirhem (KLN_1966.txt line 11556, ~p.443)\", \"stance\": \"supports\",\n       \"note\": \"'dirhem, n., a weight and a silver coin used in various Mohammedan countries. — Arab. dirham, fr. Gk. δραχμή. See drachma.' Klein draws the same direct arrow as the chart.\"},\n      {\"src\": \"FVQ\", \"where\": \"Jeffery p.130\", \"stance\": \"partial\",\n       \"note\": \"'This δραχμή passed into Iranian first as a measure of weight and then as a coin. In Phlv. we find ... dram and ... draxm ... which is the origin of the Mod. Pers. درم and درهم and the Arm. drakhm and may be assumed as the source of the Ar. درهم also.' Jeffery prefers Iranian mediation, not a direct Greek loan.\"},\n      {\"src\": \"WIKT\", \"where\": \"en.wiktionary.org درهم\", \"stance\": \"partial\",\n       \"note\": \"'Borrowed from Middle Persian drahm, borrowed from Ancient Greek δραχμή' — the modern standard route, i.e. via the Pahlavi node rather than straight from Greek.\"},\n      {\"src\": \"LKT\", \"where\": \"Lokotsch no. 523 'dirhem'\", \"stance\": \"supports\",\n       \"note\": \"'Eine Silbermünze von wechselndem Werte ... das ar. Wort kommt selbst aus gr. δραχμή'; also traces the Ottoman drem → Romanian dram and Spanish adarme.\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Pahlavi\",\n     \"words\": \"dram, diram\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Middle Persian drahm 'drachm, silver coin' is written with the Aramaic ideogram ZWZN' (Manichaean MP drhm) and was the standard Sasanian silver coin of about 4.25 g (Nyberg). It is a straight borrowing of Greek δραχμή, taken over in the Seleucid-Parthian coinage of Mesopotamia: Greek -χμ- was rendered MP -hm (drahm), which then simplifies to -m in the by-form dram — Nourai's two spellings 'dram, diram' are that reduced form and the later anaptyctic New Persian shape. Mo'in's own footnote at Borhan p.840 gives both, 'pahlavi dram ... and drahm ... from Greek δραχμή'. The only inaccuracy is that Nourai puts 'diram' (a New Persian spelling) inside the Pahlavi box.\",\n     \"derivation_fa\": \"فارسی میانه drahm (به هزوارش ZWZN’، مانوی drhm) نام سکهٔ نقرهٔ ساسانی به وزن حدود ۴/۲۵ گرم بوده است (نیبرگ). این واژه وام‌گیری مستقیم از یونانی δραχμή است که از ره‌گذر سکهٔ سلوکی و اشکانی در میان‌رودان وارد ایرانی شده؛ خوشهٔ -χμ- یونانی به -hm و سپس با ساده‌شدن به -m بدل گشته و dram به دست آمده است. حاشیهٔ معین بر برهان قاطع (ص ۸۴۰) همین را می‌نویسد. تنها ایراد آن است که صورت diram در واقع فارسی نو است نه پهلوی. ادعای نورایی درست است.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/%CE%B4%CF%81%CE%B1%CF%87%CE%BC%CE%AE\"],\n     \"ref_check\": [\n      {\"ref\": \"FVQ:130\", \"status\": \"supports\",\n       \"note\": \"'In Phlv. we find the ideograms ... dram and ... draxm meaning a silver coin, or sometimes money in general, which is the origin of the Mod. Pers. درم and درهم and the Arm. drakhm'; footnote 2 adds 'Hübschmann rightly derives it from a form *drahm from δραχμή'. Exactly Nourai's Greek → Pahlavi → Persian chain, and both of his Pahlavi spellings.\"},\n      {\"ref\": \"MON:1513\", \"status\": \"partial\",\n       \"note\": \"Mo'in's Farhang-e Fārsī درم (read through abadis.ir, which reproduces the Mo'in entry): '۱ - مسکوک نقره. ۲ - واحد وزن معادل شش دانگ' — the gloss Nourai gives, but the online text of Mo'in omits the Latin-script Pahlavi etymology of the print edition, so the page number itself could not be checked; the same author's footnote in BQT:840 supplies the Pahlavi form.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD p.28 s.v. drahm (PHD.txt line 314)\", \"stance\": \"supports\",\n       \"note\": \"'drahm [ZWZN’ < A zwzn | M drhm, N dir(h)am] drachm.' Gives the ideogram, the Manichaean spelling and the New Persian outcome.\"},\n      {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, glossary s.v. drahm (NYB_vol2_glossary.txt line 1330)\", \"stance\": \"supports\",\n       \"note\": \"'drahm [ZWZN] a silver coin, the drachm 68. 119. — From Gr. δραχμή. In Sassanian time its weight was 4.25 gr. silver.'\"},\n      {\"src\": \"BQT\", \"where\": \"Borhan ed. Mo'in p.840, Mo'in's footnote on درم\", \"stance\": \"supports\",\n       \"note\": \"'# درم — بکسر اول و فتح دوم، پهلوی dram «منا...» و drahm «تاوادیا»، از یونانی δραχμή «نیبرگ ۵۸»، معرّب آن درهم'.\"}\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"Persian\",\n     \"words\": \"deram\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"NP دِرَم deram/diram continues Middle Persian drahm without a break (MacKenzie's entry ends 'N dir(h)am'), with the usual New Persian anaptyxis breaking the initial cluster dr- into dir-/der- and the loss of -h- in the lighter variant. The second script form in the box, دِرهَم derham, is not simply a spelling variant but a doublet: it is the Arabicised form (Mo'in: 'معرّب آن درهم') taken back into Persian from Arabic dirham — a Middle Persian → Arabic → New Persian round trip, so that Persian ends up with both the inherited درم and the re-imported درهم. As a unit of weight it was reckoned at six dāngs.\",\n     \"derivation_fa\": \"«دِرَم» دنبالهٔ بی‌واسطهٔ پهلوی drahm است؛ خوشهٔ آغازین dr- در فارسی نو با واکهٔ میانجی (اناپتیکسی) به der-/dir- شکسته و ‌h نیز در صورت سبک افتاده است. صورت دوم در همان جعبه، یعنی «دِرهَم»، در واقع دوگانه (doublet) است: معرّب همین واژه که از عربی دوباره به فارسی بازگشته است (فارسی میانه ← عربی ← فارسی نو)؛ معین خود می‌نویسد «معرّب آن درهم». ادعای نورایی درست است.\",\n     \"sources\": [\"https://abadis.ir/fatofa/%D8%AF%D8%B1%D9%85/\", \"https://en.wiktionary.org/wiki/%D8%AF%D8%B1%D9%87%D9%85\"],\n     \"ref_check\": [\n      {\"ref\": \"BQT:840\", \"status\": \"supports\",\n       \"note\": \"Borhan-e Qate' ed. Mo'in p.840 (BQT_v2_pages.txt leaf 300), Mo'in's starred footnote: '# درم — بکسر اول وفتح دوم پهلوی dram ... و drahm ... از یونانی δραχμή «نیبرگ»، معرّب آن درهم (بکسر اول و فتح سوم)، واحد سکهٔ نقره ... واحد وزن: معادل شش دانگ'. Covers the Persian node, its gloss and the درهم doublet in the same footnote.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. drahm\", \"stance\": \"supports\",\n       \"note\": \"'... | M drhm, N dir(h)am' — MacKenzie gives the New Persian outcome with the optional h, i.e. both درم and درهم.\"},\n      {\"src\": \"MON\", \"where\": \"Mo'in, Farhang-e Fārsī s.v. درم (via abadis.ir)\", \"stance\": \"supports\",\n       \"note\": \"'۱ - مسکوک نقره. ۲ - واحد وزن معادل شش دانگ' — same definition as the Borhan footnote.\"},\n      {\"src\": \"BQT\", \"where\": \"Borhan ed. Mo'in p.846 s.v. درهم\", \"stance\": \"supports\",\n       \"note\": \"'درهم ... وفتح (رکسر) سوم، معرّب، واحد کوچک نقره و واحد وزن ... (رک: درم)' — Mo'in labels the Persian درهم explicitly معرّب and cross-refers to درم.\"},\n      {\"src\": \"WIKT\", \"where\": \"en.wiktionary.org درهم\", \"stance\": \"supports\",\n       \"note\": \"Lists 'Persian: درهم (derham)' among the descendants of Arabic درهم, confirming the re-borrowing of the h-form.\"}\n     ]\n    }\n   ]\n  },\n\n  # ----------------------------------------------------------------- Dregh\n  {\n   \"entry\": 5,\n   \"root\": \"Dregh\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *dregh- 'unwilling, displeased' (Pokorny 226-227; Walde-Pokorny I 821 f.)\",\n   \"note\": \"The root exists exactly as printed. Pokorny p.226-227: 'Root / lemma: dregh- | Meaning: unwilling, displeased | Note: or perhaps originally “be slack, tough”?'; Walde-Pokorny I 821 heads it 'dregh- (-gh-?) „unwillig, verdrossen“, oder vielleicht ursprünglicher „schlaff, zähe sein“?'. Nourai's language label and gloss are therefore right. What must be qualified is the material: the root's secure witnesses are Germanic (Goth. trigo 'grief', ON tregi, tregr 'unwilling', OHG trāgi 'slow, lazy') and Lithuanian (dryz-ti 'grow slack'); the Avestan word in node #1 is attached by Walde-Pokorny only with a question mark, and Pokorny's 1959 revision of the same entry prints no Iranian material at all. Watkins/AHD has no dregh- (0 hits in AHD_watkins1985.txt).\",\n   \"note_fa\": \"ریشهٔ هندواروپایی *dregh- «ناخواسته، دل‌زده، بی‌میل» همان‌گونه که در کتاب آمده واقعی است؛ پوکورنی (ص ۲۲۶–۲۲۷) و والدهٔ‌پوکورنی (ج۱ ص ۸۲۱) هر دو آن را با همین معنا می‌آورند. امّا گواهان مطمئن آن ژرمنی (گوتی trigo، آلمانی باستان trāgi) و لیتوانیایی است؛ پیوند واژهٔ اوستایی با این ریشه در والده فقط با علامت پرسش آمده و پوکورنی در ویرایش ۱۹۵۹ آن را یکسره حذف کرده است.\",\n   \"sources\": [\"https://en.wiktionary.org/wiki/%D8%AF%D8%B1%D9%88%DB%8C%D8%B4\"],\n   \"ref_check\": [\n    {\"ref\": \"WLD:821\", \"status\": \"supports\",\n     \"note\": \"Walde-Pokorny I 821 f. (WLD_Bd1_pages.txt): 'dregh- (-gh-?) „unwillig, verdrossen“, oder vielleicht ursprünglicher „schlaff, zähe sein“? Got. trigo „Trauer, Widerwille“, anord. tregi ... ags. trega ...', and further down '... av. drigu-, drəgu- „arm, bedürftig, schwach“? (Zup. aaO.; andere Lit. bei Bartholomae Airan. Wb. 777 f.)'. The page is exactly right and it carries both the root and the Avestan word.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"Pokorny p.226-227 (POK_full.txt line 23555)\", \"stance\": \"partial\",\n     \"note\": \"'Root / lemma: dregh- | Meaning: unwilling, displeased ... References: WP. I 821 f., Persson Beitr. 46 f. | Page(s): 226-227.' The root and gloss are confirmed, but Pokorny's material is only Germanic, Lithuanian and (doubtfully) Albanian — he silently dropped the Avestan word that Walde-Pokorny had queried.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 appendix\", \"stance\": \"silent\",\n     \"note\": \"grep of AHD_watkins1985.txt for 'dregh' returns 0 hits; Watkins does not carry the root.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Avestan\",\n     \"words\": \"drigu, dregu, driwi 2\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"All three forms are real Avestan words and Nourai has copied them accurately from Bartholomae: AiW cols 777-778 has '• j. driyav-, g. drigav- : g. *drəgu- Adj. (fem. j. drīvī-) „arm, bedürftig, schwach“' — i.e. Younger Avestan driyav-/drigav- (Nourai's 'drigu'), Gathic *drəgu- ('dregu') and the feminine drīvī- ('driwi'; the '2' is his homonym index). What is only plausible is the arrow from the root: the connection of Av. drigu- with Germanic *dregh- was suggested by Zupitza and printed by Walde-Pokorny I 821 with an explicit question mark, and Pokorny 1959 dropped it. Indo-Iranian points the other way — the Sanskrit comparandum is dhrigu- 'needy', with dh-, which cannot match Gothic trigo < *d-. Modern handbooks therefore start from an Old/Proto-Iranian *drigu- and leave the further PIE connection open.\",\n     \"derivation_fa\": \"هر سه صورت در اوستا واقعی اند و نورایی آن‌ها را از بارتولومه درست نقل کرده است: اوستای متأخر driyav-/drigav-، گاهانی *drəgu- و مؤنث drīvī- به معنای «فقیر، نیازمند، ناتوان» (ستون ۷۷۷–۷۷۸). آنچه فقط با احتیاط پذیرفتنی است پیوند آن با ریشهٔ *dregh- است: والده‌پوکورنی این پیوند را با علامت پرسش آورده و پوکورنی در ۱۹۵۹ حذفش کرده است؛ هم‌ریشهٔ سنسکریت dhrigu- با dh- آغازین با d- ژرمنی نمی‌خواند. پس پژوهش امروزی از ایرانی باستان *drigu- آغاز می‌کند و ریشهٔ دورتر را باز می‌گذارد.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/%D8%AF%D8%B1%D9%88%DB%8C%D8%B4\"],\n     \"ref_check\": [\n      {\"ref\": \"WLD:821\", \"status\": \"supports\",\n       \"note\": \"WP I 821 f.: 'av. drigu-, drəgu- „arm, bedürftig, schwach“? (Zup. aaO.; andere Lit. bei Bartholomae Airan. Wb. 777 f.)' — the page Nourai cites does draw the arrow, but with a question mark he does not reproduce.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"AiW cols 777-778 (BRT.txt line 14140)\", \"stance\": \"supports\",\n       \"note\": \"'• j. driyav-, g. drigav- : g. *drəgu- Adj. (fem. j. drīvī-) „arm, bedürftig, schwach“' with attestations Y.10.13, Yt.10.84, Y.53.9, Y.27.13, and the closing line 'mp. (Pü.) vgl. driyoš, (Pāz. daryōs), np. vgl. darvēš'. All of Nourai's forms, plus the whole downstream chain.\"},\n      {\"src\": \"POK\", \"where\": \"Pokorny p.226-227 s.v. dregh-\", \"stance\": \"silent\",\n       \"note\": \"The 1959 entry lists Gothic, Norse, English, Saxon, Dutch, High German, Lithuanian, Czech/Polish and Albanian material — and no Iranian word at all.\"},\n      {\"src\": \"HRN\", \"where\": \"Horn no. 559, p.124\", \"stance\": \"supports\",\n       \"note\": \"'aw. vergl. driyu- „arm“, fem. driwī- (*driyvī-), driwika- (?)' — the same Avestan forms, cited as the base of the Persian word.\"},\n      {\"src\": \"WIKT\", \"where\": \"en.wiktionary.org درویش\", \"stance\": \"partial\",\n       \"note\": \"Gives Avestan drigu / driγu 'poor, needy' and Old Iranian *drigu-, with Sanskrit dhrigu 'needy' as the Indo-Iranian cognate, but no PIE *dregh-.\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Pahlavi\",\n     \"words\": \"driyôš\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Middle Persian driyōš 'poor, needy' (Book Pahlavi <dlgwš>, hence MacKenzie's transcription driyōš with abstract driyōšīh 'poverty') continues the Old Iranian u-stem *drigu-: intervocalic *-g- weakened to -γ-/-y-, and the -ōš of the ending reflects the old nominative/genitive singular in *-auš (Avestan gen. sg. driyaoš, which Bartholomae cites in the very entry), so the case form was generalised as the stem. Pazand has daryōs. Bartholomae states the chain himself, and Mo'in's footnote at Borhan p.846 repeats it: 'پهلوی driyōš (فقیر، تهی‌دست) ... اوستا drigu-، بارتولمه ۷۷۷'. Nourai's citation BRT:849 is however wrong: column 849 of the Altiranisches Wörterbuch is payah- 'milk' / par- 'to make equal'; the entry stands at cols 777-778, exactly where Mo'in points.\",\n     \"derivation_fa\": \"فارسی میانه driyōš (به خط پهلوی کتابی dlgwš) به معنای «تهی‌دست، نیازمند» دنبالهٔ ستاک *drigu- ایرانی باستان است: g میان‌واکه‌ای به ی/غ نرم شده و پایانهٔ -ōš بازماندهٔ حالت نهادی/اضافی مفرد *-auš است (قیاس کنید با اضافی اوستایی driyaoš) که سپس به جای ستاک نشسته است؛ صورت پازند آن daryōs است. معین در حاشیهٔ برهان قاطع (ص ۸۴۶) همین را با ارجاع به «بارتولمه ۷۷۷» می‌آورد. ارجاع نورایی (BRT:849) نادرست است؛ ستون ۸۴۹ مدخل payah- «شیر» است و مدخل درست در ستون ۷۷۷–۷۷۸ است.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/%D8%AF%D8%B1%D9%88%DB%8C%D8%B4\"],\n     \"ref_check\": [\n      {\"ref\": \"BRT:849\", \"status\": \"not_found\",\n       \"note\": \"Checked: BRT.txt column 849 (running head '849 payah- / par- 850') contains 'j. payah- n. „Milch“' and 'j. par- V. „gleich machen“' — nothing about the poor. The entry Nourai wants is at cols 777-778 ('j. driyav-, g. drigav- ...'), which is also the column Mo'in cites ('بارتولمه ۷۷۷'). The claim itself is fully supported there — only the number is wrong.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD p.28 s.v. driyōš (PHD.txt line 314; PHD_mackenzie.txt line 2063)\", \"stance\": \"supports\",\n       \"note\": \"'driyōš [dlgwš | N daryūš, darwēš] poor, needy. ~īh: poverty.' The Pahlavi spelling and both New Persian outcomes.\"},\n      {\"src\": \"BRT\", \"where\": \"AiW cols 777-778\", \"stance\": \"supports\",\n       \"note\": \"The drigav- entry closes 'mp. (Pü.) vgl. driyoš, (Pāz. daryōs), np. vgl. darvēš; s. HBM aO.' — Bartholomae himself draws Avestan → Pahlavi → New Persian.\"},\n      {\"src\": \"HRN\", \"where\": \"Horn no. 559, p.124\", \"stance\": \"supports\",\n       \"note\": \"'phlv. daryōš, daryōšīh' listed under dervēš.\"},\n      {\"src\": \"NYB\", \"where\": \"Nyberg, Glossary (NYB_vol2_glossary.txt)\", \"stance\": \"silent\",\n       \"note\": \"grep for 'driyo'/'driyos' in the Manual of Pahlavi glossary returns no hit; the word is not in Nyberg's selection of texts.\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Persian\",\n     \"words\": \"darvîš\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"NP درویش darvēš 'poor; religious mendicant' is the direct continuation of MP driyōš: the older Persian shape is daryōš (still in Vis o Rāmīn, p.395), from which darvēš arises by the change of the medial glide y/γ to v next to the labial ō and the raising ō > ē. The extra forms in the box belong here too: دریوز daryūz 'begging' and دریوزگی daryūzagī 'mendicancy' are the z-variant of the same word (Horn lists deryōz, deryōza in one line with dervēš), though Horn admits 'Die neupersischen Formen sind im Einzelnen schwer zu erklären'. From Persian the word went into Ottoman Turkish derviş and thence to all of Europe (Lokotsch no. 496; English dervish 1580s). On the chart's NOTE: al-Unaysi (TAD p.27) does print 'درويش — فارسي «درپيش» معناه قدّام الباب وهو کناية عن الفقير', and Mo'in at Borhan p.846 answers it in as many words — he reports that Vullers and others took it as 'گدای در خانه‌ها' and then writes 'ولی این اشتقاق عامیانه است' ('but this is a folk etymology'). Modern scholarship is unanimously on Mo'in's and Nourai's side.\",\n     \"derivation_fa\": \"«درویش» دنبالهٔ مستقیم پهلوی driyōš است؛ صورت کهن‌تر فارسی دریوش daryōš بوده (در ویس و رامین) و سپس با ابدال ی/غ میانی به و در کنار واکهٔ لبی ō، به darvēš بدل شده است. صورت‌های «دریوز» و «دریوزگی» نیز همین واژه با پایانهٔ z است که هرن (شمارهٔ ۵۵۹) در یک مدخل گرد آورده، هرچند خود می‌گوید توجیه دقیق صورت‌های فارسی دشوار است. از فارسی به ترکی عثمانی derviş و از آنجا به زبان‌های اروپایی رفته است. دربارهٔ یادداشت کتاب: عنیسی (TAD ص ۲۷) واقعاً آن را از «درپیش» گرفته، ولی معین در حاشیهٔ برهان صریحاً می‌نویسد «ولی این اشتقاق عامیانه است» و پژوهش امروزی هم همین را می‌گوید.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/%D8%AF%D8%B1%D9%88%DB%8C%D8%B4\", \"https://www.etymonline.com/word/dervish\"],\n     \"ref_check\": [\n      {\"ref\": \"BQT:846\", \"status\": \"supports\",\n       \"note\": \"Borhan-e Qate' ed. Mo'in p.846 (BQT_v2_pages.txt leaf 306), Mo'in's starred footnote: '# درویش — بفتح اول، پهلوی driyōš (فقیر، تهی‌دست) ... هردو از اوستا drigu- «بارتولمه ۷۷۷» ... ولرس ج۱ ص ۹۳۸ ... ولی این اشتقاق عامیانه است'. Supports both the derivation and Nourai's statement that BQT rejects the 'dar pīš' explanation.\"},\n      {\"ref\": \"HRN:124\", \"status\": \"supports\",\n       \"note\": \"Horn, Grundriss no. 559 on printed p.124 (HRN.txt leaf 145): '559. dervēš „Bettler; arm“, deryōš (Vis und Rāmīn, S. 395, Vers 8), deryōš, deryōz, deryōze. aw. vergl. driyu- „arm“, fem. driwī- (*driyvī-), driwika- (?); phlv. daryōš, daryōšīh.' The page number is exact and it also covers Nourai's extra forms دریوز/دریوزگی.\"},\n      {\"ref\": \"KLN:431\", \"status\": \"not_found\",\n       \"note\": \"Klein 1966 p.431 (KLN_1966.txt leaf 227, two printed pages per leaf) covers 'decree ... defamation' — not dervish. The entry is at leaf 237 ≈ p.450-451: 'dervish, n., a Mohammedan mendicant monk. — Turk. derwish, fr. Pers. darwesh, “beggar; poor”. Cp. Avestic driyu-, fem. driwi-, “poor”.' So Klein says exactly what Nourai claims, but at a page ~20 higher than the citation.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. driyōš\", \"stance\": \"supports\",\n       \"note\": \"'driyōš [dlgwš | N daryūš, darwēš] poor, needy' — gives both New Persian reflexes, daryūš and darwēš, i.e. the daryōš > darvēš step.\"},\n      {\"src\": \"LKT\", \"where\": \"Lokotsch no. 496 'Derwisch' (LKT.txt line 1292)\", \"stance\": \"supports\",\n       \"note\": \"'„Bettler; arm“ [Horn NpEt S. 124, Nr. 559], ebenso tk. derviş „arm, Bettelmönch“; hieraus rum. derviş, it. dervis, frz. derviche, sp. derviche, dtsch. Derwisch, engl. dervish ...' — confirms Horn's page 124 and the route into Europe.\"},\n      {\"src\": \"TAD\", \"where\": \"al-Unaysi p.~27 (TAD_pages.txt leaf 30)\", \"stance\": \"contradicts\",\n       \"note\": \"'درويش — فارسي «درپيش» معناه قدّام الباب وهو كناية عن الفقير' — the rival etymology quoted in the chart's NOTE; a folk etymology, as Mo'in says.\"},\n      {\"src\": \"WIKT\", \"where\": \"en.wiktionary.org درویش\", \"stance\": \"supports\",\n       \"note\": \"'From Middle Persian dlgwš (/driyōš/) ... Avestan drigu, driγu “poor, needy” ... Old Iranian *drigu-'.\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-140.json','w',encoding='utf-8') as f:\n    json.dump(data, f, ensure_ascii=False, indent=2)\n    f.write('\\n')\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk140.py",
 "description": "write verification JSON for page 140"
}
```


### [2026-09-05T20:29:46.055Z] TOOL RESULT

```
written
```


## [2026-09-05T20:29:50.539Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -m json.tool data/verification/page-140.json > /dev/null && echo \"JSON OK\"; head -c 200 data/verification/page-140.json | xxd | head -2; python3 tools/verify_check.py 140",
 "description": "validate JSON and run verify_check"
}
```


### [2026-09-05T20:29:52.273Z] TOOL RESULT

```
JSON OK
00000000: 7b0a 2020 2270 6466 5f70 6167 6522 3a20  {.  "pdf_page": 
00000010: 3134 302c 0a20 2022 626f 6f6b 5f70 6167  140,.  "book_pag
nodes verified: 9/9
node verdicts: {'confirmed': 6, 'transcription_suspect': 1, 'plausible': 2}
root verdicts: {'confirmed': 2, 'transcription_suspect': 1}
ref checks: {'supports': 11, 'partial': 1, 'not_found': 2}
books consulted: {'supports': 27, 'partial': 3, 'silent': 2, 'contradicts': 1} | by book: {'PHD': 5, 'WIKT': 4, 'BRT': 3, 'LKT': 3, 'SYN': 2, 'KLN': 2, 'NYB': 2, 'BQT': 2, 'HRN': 2, 'WLD': 1, 'HUB': 1, 'ARY': 1, 'SKT': 1, 'FVQ': 1, 'MON': 1, 'POK': 1, 'TAD': 1}
```


## [2026-09-05T20:30:11.542Z] AGENT

Done. `verify_check.py 140` reports **0 PROBLEM lines** (9/9 nodes).

**Page 140 (book p. 110) — 3 real entries (Dous, Drassoman, Dregh), 6 redirects skipped**

- Node verdicts: 6 confirmed, 2 plausible, 1 transcription_suspect. Root verdicts: 2 confirmed, 1 transcription_suspect.
- Ref checks: 11 supports, 1 partial, 2 not_found. Books consulted: 27 supports, 3 partial, 2 silent, 1 contradicts (POK, WLD, BRT, HRN, HUB, PHD, NYB, BQT, MON, ARY, KLN, SKT, LKT, FVQ, TAD, SYN, AHD, Wiktionary).

**transcription_suspect (both `error_in: "book"` — verified against the rendered page, saved to `data/verification/sources/refs/ocr/BOOK/140.png`)**
- ROOT *Drassoman* (Greek): no such Greek word; the page really prints "Drassoman" — Nourai's misprint for δράσσομαι *drássomai*. His gloss is Jeffery's sentence about the noun δραχμή, not the verb.
- Entry 4 #1 *draxmon, draxmě*: δραχμή (draxmě) is right; *draxmon is unattested standing alone (neuter -δραχμον only in compounds, e.g. δίδραχμον).

**plausible**
- Entry 4 #2 Arabic *derham* ← Greek directly: Jeffery (the ref Nourai cites), Wiktionary and Asbaghi route it Greek → MP *drahm* → Ar. *dirham*; only Klein draws the direct arrow. Nourai's own NOTE flags this.
- Entry 5 #1 Avestan *drigu/dregu/driwi* ← PIE *dregh-: WP I 821 attaches it with an explicit question mark, Pokorny 1959 dropped the Iranian material, and Skt. *dhrigu-* (dh-) does not match Gmc. *trigo*.

**Bad citations by Nourai (content right, page/column wrong)**
- `BRT:849` (Pahlavi *driyôš*): col. 849 = *payah-* 'milk'. The entry is at AiW cols 777-778 — the column Mo'in himself cites ("بارتولمه ۷۷۷").
- `KLN:431` (*darvîš*): Klein 1966 p. 431 = "decree…defamation"; the *dervish* entry (which says exactly what Nourai claims) is at ~p. 450-451.

**Extraction errors for the owner to fix: none** — the JSON is a faithful transcription of the printed page in every field.
