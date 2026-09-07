# Verification process log — verify-page-318


## [2026-09-07T15:49:03.700Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 318 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-318.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-318.json. Write /home/sfmqrb/git/rishe/data/verification/page-318.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 318` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T15:49:06.241Z] AGENT

I'll start by reading the instructions.


## [2026-09-07T15:49:06.898Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T15:49:06.921Z] TOOL RESULT

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


## [2026-09-07T15:49:07.291Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-318.txt"
}
```


### [2026-09-07T15:49:07.307Z] TOOL RESULT

```
1	=== PDF page 318 (book page 288) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Magh1 : might, power  (refs POK:695)
4	#1 (parent #0) [Avestan / Old Persian] refs=POK:695; AHD; KLN:923 | magus, maeg, megan,moghu : Zoroastrian priest ; maguš : magician
5	  #2 (parent #1) [Pahlavi] refs=MON:4248,4421 | magu : Zoroastrian priest ; magu-pat : head priest ☞Per 3
6	    #3 (parent #2) [Persian] refs=MON | moğ «مُغ» : Zoroastrian priest ; mobad, mobed «موبد» : head priest | extra: مَغ ۱
7	  #4 (parent #1) [Arabic] refs=VDQ:374 | majŭs : Zoroastrian
8	    #5 (parent #4) [Persian] refs=MON:3884 | majŭs «مجوس» : Zoroastrian
9	#6 (parent #0) [Greek] refs=None | mağos
10	  #7 (parent #6) [Latin] refs=None | magus
11	    #8 (parent #7) [French] refs=None | 
12	      #9 (parent #8) [English] refs=None | magic
13	#10 (parent #0) [Germanic] refs=AHD; KLN | mag, mahti : power
14	  #11 (parent #10) [English] refs=None | main, might, may
15	#12 (parent #0) [Greek] refs=KLN:919; AHD:780 | mexana, mâxanâ, mexos : means ; maxanikon : a war machine
16	  #13 (parent #12) [Persian] refs=BQT:2039; FSF:311; AFM:164; MON:4384 | manjanîk «منجنیک» : mangonel | extra: منجنیق | NOTE: AHD:793 and KLN:933 derive the English "mangonel" from the Greek word "manganon:charm" which is from Indo-European root "Meng:to beautify".
17	  #14 (parent #12) [Latin] refs=None | mâčina : engine
18	    #15 (parent #14) [French] refs=None | 
19	      #16 (parent #15) [Persian] refs=MON:3701,4312 |  | extra: ماشین ، مکانیک ، مکانیزم
20	    #17 (parent #14) [English] refs=None | machine, mechanic
21	
```


## [2026-09-07T15:49:11.156Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-318.json",
 "description": "Read page 318 source JSON"
}
```


### [2026-09-07T15:49:11.205Z] TOOL RESULT

```
{
  "pdf_page": 318,
  "book_page": 288,
  "entries": [
    {
      "root": {
        "name": "Magh1",
        "lang": "Indo-European",
        "refs": "POK:695",
        "gloss": "might, power"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "POK:695; AHD; KLN:923",
          "words": [
            {"translit": "magus, maeg, megan,moghu", "gloss": "Zoroastrian priest", "script": null},
            {"translit": "maguš", "gloss": "magician", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "MON:4248,4421",
          "words": [
            {"translit": "magu", "gloss": "Zoroastrian priest", "script": null},
            {"translit": "magu-pat", "gloss": "head priest", "script": null, "see": ["Per 3"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "MON",
          "words": [
            {"translit": "moğ", "gloss": "Zoroastrian priest", "script": "مُغ"},
            {"translit": "mobad, mobed", "gloss": "head priest", "script": "موبد"}
          ],
          "script_extra": "مَغ ۱",
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 1,
          "lang": "Arabic",
          "refs": "VDQ:374",
          "words": [
            {"translit": "majŭs", "gloss": "Zoroastrian", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "MON:3884",
          "words": [
            {"translit": "majŭs", "gloss": "Zoroastrian", "script": "مجوس"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Greek",
          "refs": null,
          "words": [
            {"translit": "mağos", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Latin",
          "refs": null,
          "words": [
            {"translit": "magus", "gloss": null, "script": null}
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
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "magic", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD; KLN",
          "words": [
            {"translit": "mag, mahti", "gloss": "power", "script": null}
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
            {"translit": "main, might, may", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 0,
          "lang": "Greek",
          "refs": "KLN:919; AHD:780",
          "words": [
            {"translit": "mexana, mâxanâ, mexos", "gloss": "means", "script": null},
            {"translit": "maxanikon", "gloss": "a war machine", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 12,
          "lang": "Persian",
          "refs": "BQT:2039; FSF:311; AFM:164; MON:4384",
          "words": [
            {"translit": "manjanîk", "gloss": "mangonel", "script": "منجنیک"}
          ],
          "script_extra": "منجنیق",
          "note": "AHD:793 and KLN:933 derive the English \"mangonel\" from the Greek word \"manganon:charm\" which is from Indo-European root \"Meng:to beautify\".",
          "quote": {
            "text": "نباید برو منجنیق و نه تیر - بباید ترا دید آن ناگزیر",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 14,
          "parent": 12,
          "lang": "Latin",
          "refs": null,
          "words": [
            {"translit": "mâčina", "gloss": "engine", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 14,
          "lang": "French",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 16,
          "parent": 15,
          "lang": "Persian",
          "refs": "MON:3701,4312",
          "words": [],
          "script_extra": "ماشین ، مکانیک ، مکانیزم",
          "note": null,
          "quote": null
        },
        {
          "id": 17,
          "parent": 14,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "machine, mechanic", "gloss": null, "script": null}
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


## [2026-09-07T15:49:11.408Z] TOOL CALL #4: Bash

```json
{
 "command": "sed -n '1,200p' data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-07T15:49:11.468Z] TOOL RESULT

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


## [2026-09-07T15:49:32.906Z] TOOL CALL #5: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py; echo ---; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['VDQ','FSF','AFM','BQT','MON','POK','AHD','KLN']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:600]); print()\n\"",
 "description": "Check verify_check.py and ref keys"
}
```


### [2026-09-07T15:49:34.235Z] TOOL RESULT

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
---
VDQ {"title": "Fereydun Badreh'i (tr.), Vazheha-ye Dakhil dar Qor'an-e Majid (Persian translation of Jeffery FVQ with notes), Toos 1372/1993", "kind": "website", "url": "https://noorlib.ir/book/view/12868?pageNumber=<N>&viewType=pdf (page images; viewType=html also exists) ; info: https://noorlib.ir/book/info/12868 ; ketabnak.com/book/51136 (download blocked)", "lookup_hint": "noorlib viewer is JavaScript-rendered (WebFetch/curl get only the site chrome); needs a browser. Since it is a translation of FVQ, verify the substance via FVQ (same entry order); page numbers differ.", "local_file": null, "

FSF {"title": "Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/1984", "kind": "archive_djvu", "url": "https://archive.org/details/20220809_20220809_1444", "lookup_hint": "grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushin book (گزارشی چند درباره شاهنامه).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF.txt"], "page_offs

AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h
```


## [2026-09-07T15:49:43.301Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK_01 offset: leaf=p+8 -> p695 in POK_02? POK_02: leaf=p-344\"\ngrep -n \"magh-\" POK_full.txt | head -40",
 "description": "grep Pokorny magh"
}
```


### [2026-09-07T15:49:43.359Z] TOOL RESULT

```
=== POK_01 offset: leaf=p+8 -> p695 in POK_02? POK_02: leaf=p-344
57162:Maybe alb. {*magh-) math'b'\g, powerful' [common alb. -g > -dh; -k > -//? shift]
```


## [2026-09-07T15:49:44.466Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD magh\"; grep -n -i \"magh\" AHD_watkins1985.txt | head -30\necho \"=== AHD meng\"; grep -n -i \"^meng\\|meng-\" AHD_watkins1985.txt | head -20",
 "description": "grep AHD magh/meng"
}
```


### [2026-09-07T15:49:44.580Z] TOOL RESULT

```
=== AHD magh
710:magh-'. To be able, have power. 1. Germanic *snag- in: a. Old English magan, to be able: May; b. Old French esmaier, to frighten: DISMAY. 2. Germanic suffixed form *mah-ti-, power, in Old English miht, power: MIGHT!. 3. Germanic suffixed form *mag-inam, power, in Old English mzgen, power: MAIN}. 4. Suffixed length- ened-grade form *magh-and-, “that which enables,” in Greek (Attic) mékhané, (Doric) madkhand, device: MA- CHINE, MECHANIC, (MECHANISM), (MECHANO-). 5. Possi- bly suffixed form *magh-u- in Old Persian magus, member of a priestly caste (< “mighty one”): (MAGI), (MAGIC), MAGUS; ARCHIMAGE. [Pok. magh- 695.]
711:magh-. To fight. Hypothetical Old Iranian *ha-maz-an-,
712:“warrior” (*ha-, with < *sm-; see sem-'), possibly borrowed into Greek as Amazén, Amazon: AMAZON. [Pok. magh- 697.]
713:maghu-. Young person of either sex. Suffixed form *magho-ti- in Germanic *magadi-, with diminutive *ma- gadin-, in Old English mezgden, virgin: MAID, MAIDEN. [Pok. maghos 696.]
1235:AMATIVE amma AMATORY amma AMAZON magh-2 AMBAGE ag- AMBASSADOR ag- AMBERGRIS gher-3 AMBI- ambhi AMBIDEXTROUS deks- AMBIENT ei-1 AMBIGUOUS ag- AMBITION ei-1
1257:ARABLE are- ARBALEST arku- ARC arku- ARCADE = arku- ARCANE arek- ARCH! = arku- -ARCH arkhein ARCHAEO- arkhein ARCHAEOPTERYX pet- ARCHAIC arkhein ARCHANGEL angelos ARCHEGONIUM gene= ARCHER arku- ARCHETYPE (s)teu- ARCHI- arkhein ARCHIMAGE magh-! ARCHIPELAGO piak-1 ARCHITECT teks- ARCHITRAVE treb- ARCHIVES arkhein ARCHIVOLT arku-
1429:DIN dhwen- DINGUS _{enk-1 DINOSAUR dwei- DINOTHERE dwei- DIOCESE weik-! DIOECIOUS weik-1 DIOICOUS_ weik-1 DIOPTER oOkW- Dioscuri_ deiw-, ker-3 pip dheub- DIPHTHERIA deph- DIPHYODONT bheue- DIPLO- dwo- DIPLOCARDIAC kerd-1 DIPLODOCUS dek-1 DIPLOE dwo- DIPLOID pel-3 DIPLOMA dwo- DIPNOAN pneu- DIRE dwei- DIRECT reg-! DIRNDL tek- DISARM ar- DISASTER ster-3 DISBURSE bursa DISCERN krei- DISCIPLE dek-! DISCIPLINE dek-? DISCOMFIT dhé-1 DISCORD kerd-1 DISCOURSE kers-2 DISCRIMINATE krel- DIscuss kwét- DISDAIN dek-1 DISEMBOGUE beu-! DISFIGURE dheigh- DISGUST geus- DISK deik- DISMAL deiw-, mel-5 DISMAY magh-! DISMISS (s)meit(9)- DISPARATE pere-1 DISPATCH ped-! DISPEL pel-6 DISPENSE (s)pen- DISPERSE (s)preg- DISPLAY plek- DISPOSE apo- DISPUTE peu- DISQUISITION quaerere DISRUPT reup- DISSECT sek- DISSEMINATE 6-1 DISSENT sent- DISSERTATE ser-3 DISSIDENT sed-1 DISSILIENT sel-4 DISSIPATE swep-2 DISSOCIATE sekw-1 DISSOLVE leu-! DISSONANT swen- DISSUADE swad- DISTANT sta- DISTEND ten- DISTICH steigh- DISTINGUISH _ steig- DISTORT terkw- DISTRACT tragh- DISTRAIN  streig- DISTURB twer-! DITCH dhigw- DITTO deik- DITTY deik- DIURETIC wers-2 DIURNAL deiw- DIVA deiw- DIVARICATE wa- DIVE dheub- DIVERGE wer-3 DIVERT wer-3 DIvEs_ deiw- DIVIDE weidh- DIVINE! deiw- DIVINE? deiw- DIVULSION wel-4 Dizzy dheu-!
1788:MACERATE mag- MACHICOLATE kWel-1 MACHICOLATION kwel-1 MACHINE magh-1 MACHO mas
1792:MAGI magh-!
1793:MAGIC magh-' MAGISTERIAL meg- MAGISTRAL meg- MAGISTRATE meg- MAGMA mag- MAGNANIMOUS ane-, meg- MAGNATE meg- MAGNIFIC meg- MAGNIFICENT meg- MAGNIFICO meg- MAGNIFY meg- MAGNILOQUENT meg-, tolkw- MAGNITUDE meg- MAGNUM meg-
1794:MAGUS magh-! MAHARAJAH meg-, reg-! MAHARANI meg-, reg-! MAHARISHI meg- MAHATMA ��tmen-, meg- MAHAYANA ei-1, meg- MAHOUT meg-, mé-2 Mata ma-2
1795:MAID maghu-
1796:MAIDEN maghu- MAIEUTIC ma-2 MAIGRE mak-
1801:MAIN! magh-! MAINTAIN man-2, ten- MAJESTY meg-
1831:MAY magh-!, meg- MAYHEM mai-t MAYOR meg- MAZAEDIUM _ aidh-, mag-. MAZER smé-
1841:MEATUS mei-1 MECHANIC magh-1 MECHANISM magh-! MECHANO- magh-! MECONIUM mak-1 MECOPTERAN miak-, pet- MEDDLE meik- MEDIAL medhyo- MEDIAN medhyo- MEDIASTINUM medhyo- MEDIATE medhyo- MEDICAL med- MEDICATE med- MEDICINE med- MEDICO med- MEDIEVAL alw-, medhyo- MEDIOCRE medhyo- MEDITATE med- MEDITERRANEAN medhyo-, ters- MEDIUM medhyo- MEDLEY meik- MEDULLA (s)mer-3 MEED mizdho-
1869:MICROPYLE pulé MICTURATE meigh- MID! medhyo- MIDDLE medhyo- MipcaRD medhyo- MIDGE mu-2 MIDRIFF krep- MIDWIFE me-2 MIGHT! magh-! MIGRAINE ker-1 MIGRATE mei-1 MIL! gheslo-
=== AHD meng
747:meng-
749:men-2. To project. 1. Suffixed zero-grade form *mn-to- in a western Indo-European word for a projecting body part, variously “chin, jaw, mouth,” in Germanic *mun- thaz in Old English mith mouth: mouTu. 2. Latin mi- nae, projecting points, threats (> mindri, to threaten): MENACE, MINACIOUS; AMENABLE, DEMEAN!, PROME- NADE. 3. Latin -minére, to project, jut, threaten: EMI- NENT, IMMINENT, PROMINENT. 4. Suffixed o-grade form *mon-ti- in Latin méns (stem mont-), mountain: MONS, (MONTAGNARD), MONTANE, MONTE, MONTICULE, MOUNT!, MOUNT?, MOUNTAIN; AMOUNT, ULTRAMONTANE. [Pok. 1. men- 726, 2. menth- 732.] men-3, To remain. Variant suffixed (stative) form *man-é- in Latin manére, to remain: MANOR, MANSE, MANSION, (MENAGE); IMMANENT, PERMANENT, REMAIN. [Pok. 5. men- 729.] men-‘. Small, isolated. 1. Greek manos, rare, sparse: MANOMETER. 2. Suffixed o-grade form *mon-wo- in Greek monos, alone, only, single, sole: MONAD, MONAS- TERY, MONK, MONO-; PSEUDOMONAD. 3. Possibly also suffixed form *men-i-, a small fish, in Old English myne, mynwe, minnow, perhaps the source of Middle English meneu, a small fish: MINNOW. [Pok. 4. men- 728, meni- 731.] mend-. Physical defect, fault. 1. Latin mendum, menda, defect, fault: MENDICANT; AMEND, EMEND, (MEND). 2. Latin mendax, lying, liar: MENDACIOUS. [Pok. mend(a) 729.) mendh-'. To learn. Zero-grade form *mndh- in Greek manthanein (aorist stem math-), to learn: MATHEMAT- ICAL, (MATHEMATICS); CHRESTOMATHY, POLYMATH. [Pok. mendh- 730.] mendh-?. To chew. 1. Latin mandere, to chew: MANDI- BLE, (MANGE), MANGER. 2. Zero-grade form *mndh- in: a. Greek masasthai (< *math-ya-), to chew: MASSETER; b. Greek mastax, mouth, the model for expressive Greek (Doric) mustax, upper lip, mustache: (MOSTACCIOLI), MUSTACHE; Cc. Greek mastikhan, to grind the teeth: MASTICATE. [Pok. 2. menth- 732.] menegh-. Copious. Germanic *managa- in Old English manig, menig, many: MANY. [Pok. men(e)gh- 730.] meng-. To furbish. 1. Latin mango, furbisher, gem pol- isher, swindler: MONGER. 2. Greek manganon, magic
751:charm, contrivance, engine of war: MANGONEL. [Pok. meng- 731.]
1812:MANEGE man-2 MANES ma-1 MANEUVER man-2, op-1 MANGE mendh-2 MANGELWURZEL_ wrad- MANGER mendh-2 MANGLE! = mai-1 MANGONEL meng- MANIA men-1
1882:MOLTO mel-4 MOLY md6(u)lo- MOLYBDENUM plumbum MOMENT meue- MOMENTOUS meue- MOMENTUM meue- MONAD men-4 MONANTHOUS = andh- MONASTERY men-4 MONAXON aks- MonpDay mé-2 MONEY men-! MONGER meng- MONGREL mag- MONILIFORM mon- MONISH men-1 MONITION men-1 MONITOR men-1 MONK men-4 MONO- men-4 MONOCLE oOkw- MONOCLINIC klei- MONOCLINOUS klei- MONOCOQUE kokkos MONODY wed-2 MONOECIOUS weik-! MONOMER (s)mer-2 MOoNOPHYSITE bheue- MONOPODIUM ped-1 MONOPOLY pel-5 MONOTREME tere-1 MONS men-2 MONSTER men-1 MONTAGNARD men-2 MONTANE men-2 MONTE men-2 MONTH mé-2 MONTICULE men-2 MONUMENT men-! MOOCH meug-! MOOD! mé-1 MOOD? med- MOON mé-2
```


## [2026-09-07T15:49:54.197Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nls POK*; echo \"=== grep magh variants in POK_02\"\ngrep -n \"magh\\|māgh\\|maghos\\|Vermögen\" POK_02.txt | head -30",
 "description": "grep Pokorny 02 for magh"
}
```


### [2026-09-07T15:49:54.249Z] TOOL RESULT

```
POK_01.txt
POK_02.txt
POK_03.txt
POK_full.txt
=== grep magh variants in POK_02
45:lit.  galiü,  galeti  , können',  galiä,  gälios  , Vermögen,  Fähigkeit,  Macht', ne-gäle  f.  , Unwohlsein';
1491:6.  gher-  [ghers-  :  ghre-?)  ,kurz,  klein,  gering'  (auch  ,knapp  werden,  fehlen, nötig  sein'?). Gr.  x^iQf^y  (äol.  x^QQ^'^)  ^-us  *;(€^tw)'  , schlechter',   dazu  Superl.  /fi/^töTog und  die  hom.  Kompar.  xs^^/wv,  x^QV^9  usw.  (s.  Leumann  Mus.  Helv.  2,  2  ff., anders  Schwyzer  Gr.  Gr.  I  538),   /«f^ow,  -6ofj.aL  ,überwältige'.    Dazu  viel- leicht XQV  }^^  ^s*  nötig',   xQ^f^  ,Bedürfnis,  Bedarf,  Not,  Verlangen',  *XQ'fjogy XQS^og,  XQ^OQi  XQ^^Q  ,Bedürfnis,  Verlangen,   Schuld',   XQV^'^^^  ,gebrauchen, benutzen    usw.'  (<  *xQr}i£GdaL)j    daneben    dial.    x^T^-src^at,    XQV!^^   , Sache (die   man   gebraucht),   Ereignis',  PI.  ,Vermögen,   Geld,  Besitz';    s.   anders unter  1.  gher-] air.  gair  ,kurz'  (*gheri-s),  gaire  ,Lebenskürze',  air.  garaitj  nir.  goirid  ,kurz'.
2395:lit.  nuo-y  pa-jegä  ,Kraft,  Vermögen^,  jegiil,  ßgti  ,vermögen,  stark  sein^, lett.Je^a  , Verstand^,  Je^^  , fassen,  verstehen^ ;  ob  hierher  das  isolierte  russ. dial.  jdglyj  ,heftig;  eifrig;  geschwind^?  (s.  Berneker  443).
2531:ablautend  lit.  jaudä  f.  , Verlockung,  Verführung',  wovon  jdudinti  ,je- mands  Leidenschaft  erwecken,  jemanden  verführen',  refl.  ,aufgeregt  sein, sich  erregen',  lett.  jauda  , Vermögen,  Kraft',  jaudät  ,die  nötige  Kraft  haben' ;
4517:gr.  %tdo{.iaL  ^erwerbe'  (=  k§ayati\  Perf.  ytexrrj^ai  ,besitze*,  Yxeavov  (mit unklarem  s)  ,Besitz,  Eigentum,  Vermögen*,  poet.  ytTeag,  Dat.  PL  -nTsaTsaaip ds.,  y,v7j(.icc  n.  ,Erwerb,  Besitz,  Eigentum',  yirfjvog  n.,  PI.  ,Besitz,  Vermögen*, Sg.  ,das  einzelne  Stück  Vieh' ;  mit  demselben  Anlautverhältnis  wie  zwischen xTsivo)  :  gort.  %aTaa-/,eviß  auch  att.  0t Ao-cx^t  [17g]  =  -xrijTiyg;  durch  Kreu- zung von  ey^y.Tr](Tig  und  l'^-Ttäaig  (:  näfxa)  dial.  eyuräffLg  ,Landerwerb'.
5665:magh- :  znägh-  ,können,  vermögen,  helfen';  magh-ti-  , Macht'.
5666:Ai.  maghd-  , Macht,  Kraft,  Reichtum,  Gabe',  maghdvan-,  maghdvat- ,kräftig',  iran.  magu-,  apers.  magus  , Magier,  Zauberer'  (daraus  gr.  (.layog, lat.  magus);
5674:maghos,  -ä  jung^,  maghu-  ^^Knabe,  JüDgliDg,  unverheiratet^  und  zugehörige  # Fem. -Bildungen,  wie  magho-ti-  j'unge  Weiblichkeit^  #
5677:kelt.  *magus  in  gall.  PN  Magu-rlx,  urir.  (Ogam)  Maguno-,  air.  mang,  rriug ^Sklave^;  corn.  maw,  bret.  mao  ^Jüngling,  Diener^,  cymr.  meu-dwy  ^Ej^. Siedler*  (eig.  ,Diener  Gottes^);  Fem.  corn.  mowes  ^Mädchen^,  bret.  maouez ,Frau^;  kelt.  -smo-  Ableitung  in  air.  mäm,  mäam(m)  Jugum,  servitus'- Abstraktum  kelt.  *magot-a]ctä  ^Jungfernschaft,  junge  Weiblichkeit^  (weiter« gebildet  aus  *maghotis  =  got.  magaps,  woraus  kelt.  *maJi^k'^ot-aktä  durch Kontamination  mit  mak'ük'!^o-  ,Kind')  in  mir.  ingen  maccdacJit  ^junges erwachsenes  Mädchen^,  air.  ro-macdact  gl.  ,superadulta^,  mcymr.  macliteit\ acorn.  mahtheid  ^virgo^,  mcorn.  maghteth,  maghtyth  ds._,  bret.  matez  ,Dienst- mädchen^;  Koseform  *magguos  in  gall.  Mapo-no-s  GN,  acymr.  map,  ncjmr.  mal  /, ,Sohn^;  doppelte  Verschärfung  in  urir.  maqqas,  air.  macc,  nir.  mac  ,Sobn'j
5678:got.  magus  ,Knabe^,  aisl.  mggr  ,Sohn,  junger  Mann^,  as.  magu  ,Knabe', ags.  mago  ,Sohn,  Mann,  Diener^;  Fem.  *wa(y)ifi  in  got.  mawi  ,Mädchen' (Gen.  maujös),  aisl.  mär  (Akk.  mey)  , Mädchen^,  Demin.  got.  mawilö,  aisl. meyla,  ags.  meotcle  ^kleines  Mädchen^ ;  Abstraktum  *maghotis  junge  Weib- lichkeit^, woraus  konkret  ,Mädchen^,  in  got.  magaps  ,junge  Frau^,  ags. mcßgep  (engL  maid),  as.  magath,  ahd.  magad,  nhd.  Magd,  Demin.  Mädchen] lett.  mac  (aus  ma§s)  ,klein^
6220:Ai.  maghd-  n.  ,Gabe,  Geschenk',  maghdvan{t)-  , gabenreich,  freigebig'; m.  , Spender',  mamhate  , schenkt,  spendet',  mamhistha-  ,im  höchsten  Maße freigebig,  überaus  reichlich',  mamhdnä  ,gern,  bereitwillig' ;
```


## [2026-09-07T15:49:55.220Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN magus\"; grep -n \"magus\" KLN_1966.txt | head -20\necho \"=== KLN mangonel\"; grep -n -i \"mangonel\" KLN_1966.txt | head -20",
 "description": "grep Klein magus/mangonel"
}
```


### [2026-09-07T15:49:55.313Z] TOOL RESULT

```
=== KLN magus
22430:Mac-,  pref.  in  family  names  of  Gaelic,  Irish  and Scottish  origin.  —  Gael.,  Ir.,  mac,  ‘son’,  fr.  OIr. macc,  ‘son’,  which  is  rel.  to  OW.  map,  Co.  mdh, map.  These  words  are  prob.  rel.  to  OIr.  maitg, mug,  ‘slave’,  and  cogn.  with  OE.  magu,  ‘son,  at¬ tendant,  servant’,  ON.  mogr,  ‘son’,  Goth,  magus, ‘boy,  servant’,  magafrs,  ‘virgin’,  OE.  mxged, m&gd,  ‘maid’.  See  maiden, macabre,  adj.,  pertaining  to  the  dance  of  death. —  F.,  in  danse  macabre,  ‘dance  of  death’,  al¬ tered— owing  to  a  false  reading  — fr.  MF.  danse macabre,  fr.  earlier  Macabre  la  danse,  which  is usually  explained  as  ‘dance  of  the  Maccabees’. The  derivation  of  the  PN.  Macabre  fr.  L.  Ma- chabeus  is  based  on  Machabeorum  chora,  the Medieval  Latin  name  of  the  ‘dance  of  death’ (see  Du  Cange,  Glossarium  mediae  et  infimae Latinitatis,  Paris  1883-87,  s.v.  Machabeorum chora).  It  is  not  improbable  that  the  story  of  the seven  brothers  with  their  mother  and  that  of Eleazar  (II.  Macc.,  chapters  6  and  7),  who  suffer¬ ed  martyrdom,  conveyed  the  idea  of  ‘the  dance of  death’.  For  the  etymology  of  the  name  Ma- chabeus  see  Maccabees.  Some  lexicographers  de¬ rive  macabre  fr.  Syr.  (marqadhtadhi)  m  qabb  re, ‘(dance  of  the)  grave-diggers’,  or  fr.  Arab,  mdq- barah,  ‘cemetery’.
22514:Magdalene,  also  Magdalen,  fem.  PN.  —  Eccles. L.  Magdalene,  fr.  Gk.  Mcq'8aXr]vrl;  ‘Magda¬ lene’,  lit.  ‘woman  of  Magdala’,  fr.  MaybaXa,  fr. Aram.  Maghd^la,  place  on  the  Sea  of  Galilee (see Yerushalmi  ‘Erubhln,  5,1),  lit.  tower,  fr. gsdhal,  ‘he  became  great’ ;  rel.  to  Heb.  gadhdl, ‘he  became  great,  was  great’,  gadhdl,  ‘great’.  Cp. Madeline,  magdalen,  maudlin, mage,  n.,  a  magician.  —  F.,  fr.  L.  magus,  magi¬ cian’.  See  magus  and  cp.  magic,  adj. magenta,  n.,  a  purplish  red  dye.  —  So  called  be¬ cause  it  was  discovered  shortly  after  the  battle of  Magenta  in  1859.
22518:Magi,  n.  pi.,  a  priestly  caste  in  Media  and  Persia. —  L.  magi,  pi.  of  magus.  See  Magus.
22563:—  L.,  fr.  Gk.  jxiyo?,  fr.  OPers.  magush,  ‘magi¬ cian’,  whence  also  Talmudic  Heb.  magosh, Aram,  amgusha,  ‘magician’.
22583:Derivative:  maid-ish,  adj. maidan,  n.,  an  open  space  in  towns  of  India.  — Hind,  and  Pers.  maydan,  fr.  Arab,  maydan. maiden,  n.  —  ME.  meiden,  fr.  OE.  mtegden,  di- min.  of  magged,  mtegd,  ‘maid’,  which  is  rel.  to OS.  magath,  OFris.  maged,  megith,  OHG.  ma- gad,  MHG.  maget,  ‘virgin,  maid',  G.  Magd, ‘maid,  maidservant’,  Madchen,  ‘girl,  maiden, maid’  (prop,  contraction  of  Magdchen,  ’a  little maid  or  maidservant’),  OE.  mago,  ‘son,  man, attendant,  servant’,  ON.  mbgr,  ‘son’,  Goth. magus,  ‘boy,  servant’,  magaps,  ‘virgin’,  and cogn.  with  Avestic  mayava-,  ‘unmarried’,  OIr. maug ,  mug,  ‘slave’,  and  prob.  also  with  Olr. macc,  W.  mab,  ‘son’.  Cp.  may,  ‘maiden  .  Cp. also  Mac-.
31503:word.  Akkad,  tnugi  is  of  uncertain  origin.  It  is not  connected  with  OPers.  magush,  ‘magician’. Rabshakeh,  n.,  title  of  the  Assyrian  dignitary  who treated  with  Hezekiah,  king  of  Judah  (see  II Kings,  ch.  18  and  Is.,  ch.  36).  —  Heb.  rabh- shaqe,  fr.  Akkad,  rab-shaqu,  which  according  to Eberhard  Schrader  denotes  ‘the  chief  officer’  or ‘captain’,  fr.  rab,  ‘chief’,  and  shaqu,  pi.  shaqe, ‘high’  (see  his  Die  Keilinschriften  und  das  Alte Testament,  2nd  edition,  p.  319).  According  to Heinrich  Zimmern  the  meaning  of  rab-shaqu  is ‘chief  cupbearer',  fr.  rab,  ‘chief’,  and  shaqu,  pi. shaqe,  ‘cupbearer’  (see  ZDMG.,  53,  pp.  1 16  If.) For  Akkad,  rab  see  rabbi  and  cp.  the  first  ele¬ ment  in  prec.  word.  Akkad,  shaqu,  ‘high’,  is  of unknown  etymology.  Akkad,  shaqu,  ‘cupbearer’, derives  fr.  shaqu,  ‘to  give  to  drink’,  which  is  rel. to  Heb.  hisftqah,  Aram.-Syr.  ashqt,  Arab,  saqa, Ethiop.  saqa,  ‘he  gave  to  drink’,  Heb.  mashqeH, ‘butler,  cupbearer;  drink’,  shoqeth,  ‘watering trough’,  Aram,  mashqe,  mashtfya,  ‘drink’;  cp. sakia.
=== KLN mangonel
22793:mangle,  n.,  a  machine  for  smoothing  linen.  Du. mangel,  fr.  MDu.  mange,  mangonel  ,  fr.  It. mangano,  fr.  L.  manganum,  fr.  Gk.  jxayyavov, ‘any  means  for  tricking  or  bewitching,  philter, drug’  (whence  izayyavcuEiv,  ‘to  use  charms  of philters’),  fr.  I.-E.  base  *mang-,  ‘to  embellish, dress,  trim',  whence  also  OPruss.  manga, ’whore’,  Mir.  meng,  ‘craft,  deception’,  and  pos¬ sibly  also  Ol.  man  juft,  mahjulah,  ‘lovely,  charm¬ ing,  beautiful’.  Cp.  mangonel,  monger. Derivatives:  mangle,  tr.  v.,  mangl-er,  n.,  mangl¬ ing,  adj.,  mangl-ing-ly,  adv. mangle,  tr.  v.,  to  mutilate.  —  ME.  manglen,  fr. AF.  mangier,  contraction  of  mahangler,  freq.  of OF.  mahaignier,  ‘to  mutilate,  wound’.  See  maim. Derivatives;  mangl-er, n.,  mangl-ing,  adj.,  mangl- ing-ly,  adv.
22796:mangonel,  n.,  military  engine  for  hurling  stones.
24250:mangonel.
```


## [2026-09-07T15:50:02.830Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '5665,5673p' POK_02.txt",
 "description": "Print Pokorny magh entry"
}
```


### [2026-09-07T15:50:02.880Z] TOOL RESULT

```
magh- :  znägh-  ,können,  vermögen,  helfen';  magh-ti-  , Macht'.
Ai.  maghd-  , Macht,  Kraft,  Reichtum,  Gabe',  maghdvan-,  maghdvat- ,kräftig',  iran.  magu-,  apers.  magus  , Magier,  Zauberer'  (daraus  gr.  (.layog, lat.  magus);
arm.  marthankh  ,Hilfsmittel'  (*mag-thra-)]
gr.  (.ifjxog  n.  (dor.  iiä^og),  poet.  (.ifjxaQ  , Hilfsmittel',  (.irjxavrj^  dor.  iiG^avä (>  lat.  machina)  ,Hilf smittel,  Werkzeug,  List' ;
got.  ags.  magan,  aisl.  mega,  maga,  muga,  afries.  muga,  mnd.  mögen,  ahd. magan^  mugan  ,mögen','  1.  Sg.  Präs.  got.  as.  ahd.  mag,  aisl.  mä,  ags.  mseg, afries.  mei;  aisl.  magn,  meg{i)n  n.  , Macht,  Hauptsache',  ags.  masgen,  ahd., as.  magan,  megin  ds.;  got.  mahts  f.  , Macht,  Kraft',  ahd.  as.  mäht,  ags. meaht,  might,  aisl.  mättr  ds. ;
lit.  mägulas  , zahlreich,  viel*;
aksl.  mogg,  mosti  ,können,  vermögen',  jpo-moHi,  Iterat.  po-magati , helfen' usw.,  aksl.  mosth,  russ.  moch  usw.  ,Macht,  Stärke'  (=  got.  mahts).
WP.  II  227,  Trautmann  164 f.,  H.  Güntert,  Weltkönig  108 f.;  falls E.  Fraenkel  (Lexis  1,  169  f.)  richtig  gr.  ^ifjxog  mit  lit.  moJceti  ,können, verstehen'  auf  eine  Wz.  mäkh-  zurückführt,  könnten  die  anderen  Wörter auch  auf  megh- :  mogh-  zurückgehen ;  vgl.  toch.  A  mokats  ,mächtig'.
696
```


## [2026-09-07T15:50:04.074Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== leaf 351 of POK_02 (p695)\"; awk 'BEGIN{RS=\"\\f\"} NR==351' POK_02.txt | head -20",
 "description": "Print POK_02 leaf 351"
}
```


### [2026-09-07T15:50:05.367Z] TOOL RESULT

```
=== leaf 351 of POK_02 (p695)
.  aisl.  lyr  m.  {Heuhiz)  ,Lub,  Gadus  pollichius'  (von der  hellen  Farbe  der  Seiten  und  des  Bauches  des  Fisches),  aisl.  lysa  f. ^Merlüccius  vulgaris,  Merlan',  norw.  lysing  ds.,  vgl.  schwed.  löja,  löga ^Abramis  alburnus'  aus  Haugiön,  nhd.  Lauge  ,Cyprinus  alburnus  und leaciscus');  mhd.  liehsen  ,hell'  (*leuhsna-  =  av.  raoxsna-),  aisl.  Ijös  n. , Licht'  (*leuhsa-),  Igsa  , leuchten,  glänzen,  hell  machen,  erklären,  verkünden' =s  ags.  Hexan,  llxan  ,leuchten' ;
lit,  laükas  , blässig',  laukas  ,Feld'  (, Lichtung'),  s.  oben  ai.  lökd-,  rocd-  usw. ; apr.  luckis  ,  Holzscheit'  (=  ai.  ruci-,  ablaut.  mit  sloven.  Iü6  usw.  , Licht - Span';  FIN  lit.  Laukesä]
abg.  laca  , Strahl'  (loukid,  vgl.  gr.  Xovaaov),  ksl.  auch  luh  m.  , Strahl, Licht'  (=  ai.  roci-,  ahd.  long),  sloven.  lue  f.  , Licht',  PL  , Lichtspäne',  russ. /wc, Strahl',  lu(^d  , Kienspan',  6ech.  louc  ,Kien';  abg.  luna  ,Mond'  [Houk-s-nä, wie  lat.  lüna  usw.) ;
toch.  A  B  luk-  , leuchten,  erleuchten';  A  lok,  lokit,  B  laukito  , fremd', lauke  ,weit'  (vgl.  lit.   laük,  laukan  , hinaus'  von  laukas  ,Feld');
hitt.  luk(k)-  ^leuchten,  zünden'.
2.  mit  der  Bedeutung  , schwarz'  (aus  , glänzend  schwarz'  oder  , verbrannt')  : s.  oben  S.  688;
aber  lat.  läcius  , Hecht'  bedeutet  ,der  Schillernde'.
3.  Mit  leuk-  ,leuchten'  deckt  sich  leuk-  , sehen':
ai.  lökate,  löcate  , erblickt,  wird  gewahr',  lökdyati,  löcdyati  ,betrachtet', löcanam  ,Auge';
gr.  Xevaao)  ,sehe' ;
cymr.  am-lwg,  cyf-lwg,  eg-lwg  ,con3picuus',  go-lwg  , Sehen,  Gesicht'  (auch cymr.  usw.  llygad  ,Auge'  aus  *lukato-) ;
lit.  Idukiu,  Iduktl  ,auf  jemanden  warten',  lükUi  ,ein  wenig  harren',  lett. lükuot  , schauen,  auf  etwas  sehen,  versuchen',  apr.  lauklt  , suchen';  aus , wonach  schauen':  , zielen,  treffen  (werfen)'  und  , erhalten,  bekommen': luciti  se  ,sich  treffen,  geschehen;  müssen';  in  russ.-ksl.  lui^iti  ,jemanden treffen',  usw.
44
690  '
4.  Eine  Parallel wurzel  leuk-  in:  %
Ai.  rü§ant-  ,licht,  hell,  weiß',  ksl.  v^s^lys^  ,kahl',  russ.  Z^/si/J  ,kahl,  blässlr«»*  i dazu  vielleicht  der  Name   des  Luchses  (entw.  von  den  funkelnden  Au?   * oder   eher   nach   seinem   grauweißen    Fell) :    arm.    lusanunk  PL,    <t^^  i»^ IvyyLog  (woher   die  Nasalierung?),   ahd.  luhs,   ags.  lox,   woneben  aschwed' lö  aus  Huha-  (vgl.  etwa  dt.  Fuchs :  got.  fauhö),   lit.  lüHs,   lett.  lusis    an luysis,  abg.  ri/st  (mit  r  statt  l  nach  rbvati  ,ausreißen'?);  nach  Vasmer klärt  sich  das  slav.  r  vielleicht  durch  iran.  Entlehnung;  nicht  ganz  sichte steht   die   Bed.  , Luchs'  für    das   zudem   auf
```


## [2026-09-07T15:50:23.078Z] TOOL CALL #12: Bash

```json
{
 "command": "ls site/pages/318.jpg 2>/dev/null; pdftoppm -f 318 -l 318 -r 200 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg318 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/",
 "description": "Render page 318"
}
```


## [2026-09-07T15:50:24.410Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT magu/mogu\"; grep -n \"moyu\\|moγu\\|magu-\\|maγu\" BRT.txt | head -30\necho \"=== KNT magu\"; grep -n -i \"magu\" KNT.txt | head -20",
 "description": "grep Bartholomae and Kent for magu"
}
```


### [2026-09-07T15:50:24.796Z] TOOL RESULT

```
site/pages/318.jpg
total 144
drwx------ 2 sfmqrb sfmqrb  4096 Sep  7 11:50 .
drwx------ 4 sfmqrb sfmqrb  4096 Sep  7 11:48 ..
-rw-rw-r-- 1 sfmqrb sfmqrb   251 Sep  7 11:49 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 62558 Sep  7 11:50 pg318.png
-rw-rw-r-- 1 sfmqrb sfmqrb 65279 Sep  7 11:49 pg324.png
-rw-rw-r-- 1 sfmqrb sfmqrb    40 Sep  7 11:49 queue.txt
```


### [2026-09-07T15:50:24.849Z] TOOL RESULT

```
=== BRT magu/mogu
19535:•  p.  magav-  {:  j.  moyu-)  Adj.,  bezeichnet einen  medischen  Volksstamm,  fdr  den  die Priesterwürde  vorbehalten  war,  'magisch, Magier'*';  /  martiy^  'gu!  äht^  gaumSt<^ nätnii'  Bh./.ii;  13%  14^,  ^.2,  b;  —  gau- matam  tyam  'gum  Bh./.ijJ,  16,^18.
=== KNT magu
2000:To these names may be added those of three large districts which were not governmental prov- inces: Karmdna, Varkdna, Margus with ethnic Márgava; ethnic Pätišwariš, to an unknown place-name; Нататат&уа, patronymic family- name to Hazémani§; Magus, denoting а member of the priestly clan of Media.
2156:Nom. Sg. Masc.: magus, piruš, sikabrus, ад). ш@татйун$; names of kings, Dérayava'us, Kürus; place-names, Abirddus, Kud"ru&, Qata- gus, Babiru’, Māļruļš, Margus, Hindu.
2157:Асе. Sg. Masc.: magum, zrafum, gidum; Dära- yava’um; Babirum, Margum; visadahyum; per- haps [agurum].
2663:D. As double object, one of the person and the other of the thing: DB 1.44f айа xšaçam tya Gaumdta hya magus айта Kabügiyam ‘this king- ship which Gaumata the Magian took away from Cambyses’ or ‘of which Gaumata deprived Cam- byses’; so also 1.46f, 59, 65f, and its passive in 1.49f hya атат Gaumàlam Шат magum тёасат ditam салтта ‘who might make that Gaumata the Me- dian deprived of the kingship’, DB 4.65 лау Skaurim (= skaubim) пай tunwatam züra akuna- vam ‘neither to the weak nor to the powerful did І do wrong’. DPd 20-2 айа adam yànam jadiya-
2666:E. As appositive to another accusative: DB 1.49f Gaumdtam tyam magum; DPd 21 haw Da- rayavaum xSdyatiyam adadà ‘he created King Darius’.
2798:II. From the originally relative type Gaumdia hya magus (DB 1.44, ete.) without the copula, there came the accusative type Gaumdtam tyam magum (DB 1.49f, etc.), where the articular use is assured.
3488:36 sdva : І martiya : magus : dha : Gaumáta : пата : hauv : udapatatà : hacd : Рай 37 yduvadaya : Arakadri$ : n&ma : Каша : hacd : avadaSa : Viyaxnahya : mah
3492:44 : Darayavaus : xSayafiya : айа : xSacam : tya : Gaumáta : һуа : magus : adin
3494:46 ha : pasiva : Gaumata : һуа : magus : adinà : Kabüjiyam : uta : Pirsam : шй
3496:48 v :xšāyaðiya :abava —— :08tiy : Dàrayavaus : xSayafiya : naiy : aha : martiya : 49 naiy : Разза : naiy : Mada : пазу : amàxam : taumáyà : kaSeiy : һуа : avam : Gau 50 matam : буз : magum : xSacam : ditam : caxriyà : kiraSim : hac& : багат : а 51 tarsa : kàram : vasiy : av&janiy& : һуа : paranam : Bardiyam : adánà : avahyar 52 айу : кагат : avájaniyà : mátyamà&m : xénàsátyy : tya : adam : naiy : Bard
3498:54 iy : pariy : Gaumátam : tyam : magum : yàtà : adam : arasam : pasáva : adam : Aura 55 maz(d)àm : patiyavahyaiy : Auramazdàmaiy : upastàm : арага : Bágayádais :
3511:: {уаш : magum : avàjanam : Sikayauvati$ : n&mà : didà
3520:66 magus : айта : adam : катат : giGava : avàstáyam : Pürsamcà : Madame
3525:70 aval : adam : hamataxSaiy : vani : Auramazdiha : уада : Gaumata : һуа : magu
3527:72 iya : ima : tya : adam : akunavam : pasiiva : уай : xSayabiya : abavam ‚ 73 : Dürayavaus : xSdyabiya : уа : adam : Gaumatam : tyam : magum : avüjanam : ра 74 sīva : I martiya : Agina : пата : Upadarmahya : puça : hauv : udapatalá : Uujai 75 y : kàrahyà ; ava : afaha : adam : Üvjaiy : xiiiyasiya : amiy : pasdva : Uv 76 пуй: hamigiya : ауа :abiy : avam : Aginam : aSiyava : hauv : xšđyaðiya . TI :abava : Üvjaiy : uti : I martiya : Babiruviya : Naditabaira : патол : Ainatrahy
3817:1 :98tiy : Darayavaus : xsayaüiya : ima : t 2 ya:manà :kartam': Babireuv — :98ty : D З árayavaus : xSàyaftya : ima : tya : adam : akuna 4 vam : vasnà : Autamazdiha : һашаһуйуй : баг 5 da : pasáva : yada : xšāyaðiya : abavam : ХІХ : hamaran 6 Я : akunavam : vasnd : Auramazdiha : adamšim : а Т janam : uta : IX : x&ayatty& : agarbiyam : 1 Gaumata : 8 n&ma : magus : aha : hau : adurujiya : ava : абаһа : adam : 9 Bardiya : amiy : hya : Küraus : puça : hauv : Parsam : ha 3 10 migiyam : akunaus : Z Acina : пата : Uvjiya : hauv : adu 11 rujiya : ауаба : afaha : adam : xSiyaliya : amiy : Uvjaiy 12 : hauv : Üvjam : hamigiyam : akunaus : manā : I Naditabaira : n 13 dma : Babiruviya : hauv : adurujiya : avafá : aGaha : 14 adam : Nabukudracara : amiy : hya : Nabunaitahya : puga : 15 hauv : Babirum : hamigiyain : akunaus : I Martiya : na 16 ma : Pársa : hauv : adurujiya : атаба : ađaha : adam : Imani 17 š : amiy : Uvjaiy : cSayasiya : hauv : Üvjam : hamiciya 18 m : akunaus : I Fravarti$ : пата : Mada : hauv : adurujiya 19 : ауада : абаћа : adam : XSa@rita : amiy : UvaxStrahya : taumay 20 à : hauv : Madam : hamiciyam : akunaus : I Cigataxma : пата : Asa 21 gartiya : hauv : adurujiya : ava : afaha : adam : xšāyað 22 iya : amiy : Asagariaiy : UvaxStrahya : taumāyā : hauv 23 : Asagartam : hamigiyam : akunauS : І Frida : nama : 24 Margava : liauv : adurujiya : ааба : ađaha : adam :
3873:: Sàtiy : Darayavaus : xšāyaðiya : тау : martiyà : їуаіу 81 :adakaiy : avada: Ghat : yàtà : adam : Gaumãtam : tyam : magum : ayãjanam :. 82 hya : Bardiya : agaubatà;: adakaiy : imaiy : martiya : hamataxáatà : anudiyd : man
3969:was led to me, and I killed him. After that the DBs е DBc Р province became mine. | :iyam : башта 1 уаш ‚Аф §72. 544-7, Saith Darius the King: Those 2 {8 : bya : magus 2 ina :adu * Jilamites were faithless and by them Ahuramazda а :a дт ду + was not worshipped. I worshipped Ahuramazda; 5 durujiya 4 ауайй * by the favor of Ahuramazda, as was my desire, — ^ 248 : абара : 0: alaha :а thus I did unto them. | айат : Ва б Е x $73. 5.18-20. Saith Darius the King: Whoso 5 rdiya : amiy : hya 1 Sayal ‚ shall worship Ahuramazda as long as (his) - :K 8 Wa- ш strength shall be, of him both living and dead 6 üraus : puça : 9iy:U
4851:The Magus Patizeithes had been left by Cambyses as managing steward of his palace at Susa, and he was one of the few who knew of the death of Smerdis. He had himself à brother who greatly resembled Smerdis in appearance, and, says Herodotus, this brother's name was also Smerdis. Patizeithes put his brother Smerdis on the throne, under the pretense that he was Smerdis son of Cyrus and brother of Cambyses. The false Smerdis, by not admitting to his presence any one who had known the true Smerdis, successfully con- cealed his true identity for some time (61-2). But the news reached Cambyses in Egypt, and he knew the truth, because Prexaspes assured him that he had slain the real Smerdis. Resolved to fight the usurper, he leaped upon his horse to lead his army back to Susa, but as he did во he accidentally struck the point of his sword into his thigh, and from the wound he died (63-6). Thus the false Smerdis ruled for some months; but a Persian
5757:magu- sb. ‘Magian’, member of a priestly order of Media: Flam. ma-ku-i3, АКК. ma-qu-&u, Gk. Méyos ($153.1). Uncertain material on mean- ing and etymology, Kónig, Klotho 4 chap. 12, and RulD 66. magus nsm. DB 1.36, 44, 46, 64, 66, 101; 4.8; DBb 2. magum asm. DB 1.50, 54, 57, 73; 4.81.
```


## [2026-09-07T15:50:32.878Z] TOOL CALL #14: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg318.png"
}
```


### [2026-09-07T15:50:33.221Z] TOOL RESULT

```

```


## [2026-09-07T15:50:33.218Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-07T15:50:49.355Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && pdftoppm -f 318 -l 318 -r 400 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg318hi && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg318hi.png'); print(im.size)\nw,h=im.size\nim.crop((int(w*0.35),int(h*0.355),int(w*0.80),int(h*0.395))).save('ferdowsi.png')\n\"; ls",
 "description": "Crop Ferdowsi line at high res"
}
```


### [2026-09-07T15:50:52.196Z] TOOL RESULT

```
(3400, 4400)
agents.txt
ferdowsi.png
pg318hi.png
pg318.png
pg324.png
queue.txt
```


## [2026-09-07T15:50:54.087Z] TOOL CALL #16: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/ferdowsi.png"
}
```


### [2026-09-07T15:50:54.108Z] TOOL RESULT

```

```


## [2026-09-07T15:50:57.422Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg318hi.png'); w,h=im.size\nim.crop((int(w*0.40),int(h*0.375),int(w*0.80),int(h*0.400))).resize((int(w*0.40*1.6),int(h*0.025*1.6))).save('ferdowsi2.png')\n\"",
 "description": "Crop poem line"
}
```


### [2026-09-07T15:50:59.024Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-07T15:51:00.806Z] TOOL CALL #18: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/ferdowsi2.png"
}
```


### [2026-09-07T15:51:00.854Z] TOOL RESULT

```

```


## [2026-09-07T15:51:00.852Z] INPUT

[Image: original 2176x176, displayed at 2000x162. Multiply coordinates by 1.09 to map to original image.]


## [2026-09-07T15:51:04.260Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg318hi.png'); w,h=im.size\nc=im.crop((int(w*0.40),int(h*0.392),int(w*0.80),int(h*0.412)))\nc=c.resize((c.width*2,c.height*2)); c.save('ferdowsi3.png'); print(c.size)\n\"",
 "description": "Crop poem line lower"
}
```


### [2026-09-07T15:51:05.805Z] TOOL RESULT

```
(2720, 176)
```


## [2026-09-07T15:51:07.643Z] TOOL CALL #20: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/ferdowsi3.png"
}
```


### [2026-09-07T15:51:07.701Z] TOOL RESULT

```

```


## [2026-09-07T15:51:07.699Z] INPUT

[Image: original 2720x176, displayed at 2000x129. Multiply coordinates by 1.36 to map to original image.]


## [2026-09-07T15:51:10.712Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg318hi.png'); w,h=im.size\nc=im.crop((int(w*0.42),int(h*0.404),int(w*0.80),int(h*0.422)))\nc=c.resize((c.width*2,c.height*2)); c.save('ferdowsi4.png'); print(c.size)\n\"",
 "description": "Crop poem line again"
}
```


### [2026-09-07T15:51:12.406Z] TOOL RESULT

```
(2584, 158)
```


## [2026-09-07T15:51:14.239Z] TOOL CALL #22: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/ferdowsi4.png"
}
```


### [2026-09-07T15:51:14.294Z] TOOL RESULT

```

```


## [2026-09-07T15:51:14.291Z] INPUT

[Image: original 2584x158, displayed at 2000x122. Multiply coordinates by 1.29 to map to original image.]


## [2026-09-07T15:51:23.138Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN mangonel full\"; sed -n '22796,22798p' KLN_1966.txt\necho; echo \"=== KLN magus entry\"; sed -n '22560,22566p' KLN_1966.txt\necho; echo \"=== KLN magic\"; grep -n \"^magic,\\|magic,  adj\\|magic,  n\" KLN_1966.txt | head",
 "description": "Klein entries"
}
```


### [2026-09-07T15:51:23.226Z] TOOL RESULT

```
=== KLN mangonel full
mangonel,  n.,  military  engine  for  hurling  stones.
—  OF.  (=  F.  mangonneau),  dimin.  of  ML.  man- gonum,  mangona,  fr.  VL.  *  manganum,  ‘machine  , fr.  Gk.  [liyyavov,  See  mangle,  ‘machine  for smoothing  linen’.
mangosteen,  n.,  an  East  Indian  tree  and  its  fruit.

=== KLN magus entry
magpie,  n.  —  Compounded  of  Mag,  abbrevia¬ tion  of  Margaret  and  pie,  the  bird.  For  sense development  cp.  F.  margot,  ‘magpie’,  fr.  Mar¬ got,  ‘Mag,  Maggy’,  a  pet  form  of  Marguerite, ‘Margaret’.
maguey,  n.,  any  of  various  species  of  Agave.  — Sp.,  fr.  Taino.
Magus,  n.,  one  of  the  Magi;  (not  cap.)  a  magician.
—  L.,  fr.  Gk.  jxiyo?,  fr.  OPers.  magush,  ‘magi¬ cian’,  whence  also  Talmudic  Heb.  magosh, Aram,  amgusha,  ‘magician’.
Magyar,  n.,  Hungarian.  —  Hungarian. Mahabharata,  n.,  one  of  the  two  great  Hindu  ep¬ ics  (the  other  is  Ramayana).  —  OI.  Mahabhara- tah,  lit.  ‘the  great  (story  of  the)  Bharatas’.  OI. maha-,  ‘great’,  is  cogn.  with  L.  magnus,  ‘great’. See  magnum  and  cp.  maharaja  and  words  there referred  to.
mahalcb,  n.,  a  kind  of  European  cherry  (Prunus mahaleb).  —  Arab,  mahiab,  in  VArab.  pronun¬ ciation  mahleb.
maharaja,  maharajah,  n.,  the  title  of  great  Hindu princes.  —  OI.  maharajah,  ‘a  great  king’,  com¬ pounded  of  maha-,  ‘great',  and  rdjan,  ‘king’.  See magnum  and  rajah  and  cp.  Maratha  and  the  first element  in  Mahabharata,  maharanee,  mahatma, mahout.

=== KLN magic
22514:Magdalene,  also  Magdalen,  fem.  PN.  —  Eccles. L.  Magdalene,  fr.  Gk.  Mcq'8aXr]vrl;  ‘Magda¬ lene’,  lit.  ‘woman  of  Magdala’,  fr.  MaybaXa,  fr. Aram.  Maghd^la,  place  on  the  Sea  of  Galilee (see Yerushalmi  ‘Erubhln,  5,1),  lit.  tower,  fr. gsdhal,  ‘he  became  great’ ;  rel.  to  Heb.  gadhdl, ‘he  became  great,  was  great’,  gadhdl,  ‘great’.  Cp. Madeline,  magdalen,  maudlin, mage,  n.,  a  magician.  —  F.,  fr.  L.  magus,  magi¬ cian’.  See  magus  and  cp.  magic,  adj. magenta,  n.,  a  purplish  red  dye.  —  So  called  be¬ cause  it  was  discovered  shortly  after  the  battle of  Magenta  in  1859.
22519:Magian,  adj.,  pertaining  to  the  Magi;  n.;  one  of the  Magi.  —  See  prec.  word  and  -ian. magic,  n.  — -  ME.  magik ,  fr.  MF.  (=  F.)  ma- gique,  fr.  Late  L.  magice,  fr.  Gk.  uxy.xr,  (scil. zz'/yri  )  ■  lit.  ‘magic  art’,  fem.  of  the  adjective jj.x';a-/.6c,  ‘Magian,  magical’.  See  magic,  adj. magic,  adj.  —  ME.  magik,  fr.  OF.  (=  F.)  ma- gique,  fr.  L.  magicus,  fr.  payi xo?,  ‘Magian,  magi¬ cal',  fr.  uayo s,  ‘Magus,  magician’.  See  Magus and  -ic.
22520:Derivatives:  magic-al,  adj.,  magic-al-ly,  adv. magician,  n.  —  ME.  magicien,  fr.  MF.  (=  F.)  ma- gicien,  fr.  OF.  magique.  See  magic,  n.,  and  -ian.
```


## [2026-09-07T15:51:24.730Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN machine\"; grep -n \"machine,  n\\|mechanic,\" KLN_1966.txt | head -5\necho \"=== PHD mow\"; grep -n \"mow \\[\\|mowbed\\|magūy\\|mgw\" PHD.txt PHD_mackenzie.txt | head -20",
 "description": "Klein machine + MacKenzie mow"
}
```


### [2026-09-07T15:51:24.802Z] TOOL RESULT

```
=== KLN machine
22460:machinator,  n.,  plotter,  schemer.  —  L.  machina- tor,  fr.  machindtus,  pp.  of  mdchindri.  See  ma¬ chinate  and  agential  suff.  -or. machine,  n.  —  MF.  (=  F.),  fr.  L.  mdchina,  ‘ma¬ chine,  engine,  fabric,  frame,  device,  trick’,  fr. Dor.  (ia/ava,  corresponding  to  Att.  pvjxavTj, ‘machine,  contrivance,  artificial  means,  expe¬ dient’,  fr.  Dor.  [taxes  (Attic  [tijxos ) ,  ‘contriv¬ ance,  means,  expedient,  remedy’,  fr.  I.-E.  base *magh-,  *mlgh-,  ‘to  be  able’,  whence  also  OSlav. mogq,  moSti,  ‘to  be  able',  OE.  mseg,  ‘I  can’.  See may,  auxil.  v.,  and  cp.  main,  ‘might’,  might.  Cp. also  mechanic.
23250:mechanic,  adj.  —  L.  mechanicus,  fr.  Gk.  pv yccvixop,  ‘resourceful,  inventive;  mechanical’,  fr. pTjxavr;,  ‘means,  invention,  machine".  See machine  and  -ic.
23251:Derivatives:  mechanic,  n.,  mechanic-al,  adj., mechanic-al-ly,  adv.,  mechanic-al-ness,  n.,  me- chanic-ian,  n.,  mechan-ics,  n. mechanism,  n.  —  ModL.  mechanismus,  fr.  Gk.
=== PHD mow
PHD.txt:392:hamēstār, —ih [hmyst!l, -yh] = hamēmāl, ~ih. hamésag [hmyfk! | M hmyšg, N —a] always. ^h : eternity. ~-86z [-swe] ever-burning. hamē-wahār [hmy whl | N haméfa-bahar] marigold. ham-éwénag [Am'dwynk!'] of the same kind, homogeneous. ham-góhr (hmgwhl! | M hmgwhr] of the same substance or nature, consubstantial. ham-ginag [hmgwnk! | M hmgwng] likewise, so. P hāmharz [A())mAlc | P I? mhyrz] adjutant, attendant. hāmīn [A*myn! |= M] summer. ~ig [-yk'] (of) summer. hāmist [KHDE, v. hammis ; )”mst!] all. ham-kār [hmk’l | N ~] collaborator. 7h : collaboration. hāmkišwar [mkyfwl | M. -wr] universe. hammis [KH DE < A k-hdh), ат... ~: together with. hammist [hmyst'] stagnant, peaceful. ~(ag)an [-(kYn'] limbo, the neutral station between heaven and : hell. vl hammóxtan, hammoz- [ALPWN-tn! < A У "Ip: hmwhtn', hmwc-, Ki hmsoz- | M hmwxtn, N āmēxtan, ámóz-] teach; learn. -išn: teaching. hammdxtar [Amwht?!] learner. ~th: learning. hammóz- , ~i8n, v. hammóxtan. —@йг [kmwcek?l | N āmēzgār] teacher. ham-nibardih [hmnpityh] (single) combat. hamēūģ [/tmwg] equal, like. hámón [k mwn' | N kāmūn] level, flat. hámoyén [/?mwdyn!] all. ham-pursag [hmpwrsk!] consulting, taking counsel. ^h : consultation. ham- |-ránih [Am nyh] battle, combat. ~-samiain [-s"m?n!] contiguous. ~-sardag [-sltk'] of the same kind, like. ~-sayag [-sdk! | N hamsáya) neighbour. ~-tag [-t*k! | N hamid] equal, peer. «tan [-tn'] of the same stature, build. ~=-tihmag [-twhmk'] relative, relation. hamwar [hmwl | N hamwār] level, abreast. hámwiür(ag) [%()mw?/, -k! | N hamwdara] always. ham-zamān [hm ODNA | N —] instantly, immediately. handām [And*m | = P, N andàm] member, limb. handarz [hndle | N andarz] advice, injunction, testament. handarzénidan, handarzén- [hndleyn-ytn!] advise.
PHD.txt:491:méx [myh | P myx, N ~] peg, nail. ~ ī gàh: astr. Polaris, pole star. 1-3méz-, v. mézidan, mëzišn, mistan. mēzd [my()zd | № тёз] offering, meal. „bān [-p’n' | N ~] host. mézidan, 'méz- [myc-ytn!] suck. *mézisn [myckn'] blinking, twinkling. mih [mt!] false, contrary, opposite. mihēxt [mytwht!] falsehood. imihr [mtr! | M myhr, N —] Mithra; sun; cal. 7th month; 16th day. tmihr [mtr!, etc.] contract, bond. šmihr [mtr!, etc.] love, friendship. mihrbān [mtr'p?n! | Р myhrb’n, N ~] friendly, kind. mihr-dróz [mtr'dhwc] = mihródruj. mihródruj [mtr?w-, mtrwk-diwe = Av. mitlyo.drujim] contract-breaker. ~th: breaking faith. mihr-zan [mtr'zn'] = mihródruj. mij(ag) [myc(k') | N muz(a)] eyelid; eyelash. mijüg (myc-, myšwk! | IN mizü] lentil. mir-, v. murdan. mistan, 3mëz- [mstn', myc- | N mézidan] urinate. -i$n(ih): urination. mizag [m(y)ck! | N maza] taste. ~darih [-d’lyh] (sense of) taste. ~ӧтапа [отпа] tasty. mizd [m(y)zd | N muzd] reward, hire, pay. ~war [-wbl | N -àr] hireling. *mizné [m(y)znydy] mist, dew. mög [mwk!] shoe. 5 *moy-mard [mgw-mit', -gGBRA | N muy) magus. mör [mwl | N <) ant. mórd [mwlt! | N ~] myrtle. morwārīd [mwlw'lyt! | M mwrwryd, N ~] pearl. *mowbed [mgwpt' | N móbad] Mazdean priest. móy [mwd | N ~] hair. móya$ [mwdk' | N méya] lamentation. móyen [mwdyn'] (made of) hair. moz [mwe | N ~] banana. mózag [mzvck! | N тоха] shoe. *mūdag [mwtk'} spoilt, destroyed. muy [DKRA < А dgP | N mux] date-palm. muhr [muwdl | M mwhr, N ~] seal. Сар [mwhlk! | P mwhrg, N ~a] bead, vertebra, piece (in backgammon, etc.). *muhrišn [*mwtl$n!] excrement. mulān [mwi?n'] belly (daevic).
PHD.txt:3220:priest āsrē, asrén, dastwar, hérbed, mowbed, māns?rbar; ~ hostile to Zoroaster karb; first officiating ~ zēt; second officiating ~ rāspīg.
PHD.txt:4877:ménogwénih! mēnēgīh mēnēgīgīh mēnēgīg mēwag moymard mowbed menišnīg menišn mēzd, mizd mēzdbān miznē mēy mayg mērag namagt Jabar! sah-! sahistan! sahián! mij 13mēx- mēzīdan mijūg
PHD_mackenzie.txt:2750: ham-gOhr [hmgwhl I M hmgwhr] of the same substance or nature,
PHD_mackenzie.txt:2752:ham-aOnag [hmgwnk' I M hmgwng] likewise, so.
PHD_mackenzie.txt:3588:·mowbed [mgwpt l I N mobad] Mazdean priest.
PHD_mackenzie.txt:7345:   mowbed, miinsarbar; ,......, hostile to     prostrate nibem.
```


## [2026-09-07T15:51:37.148Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\n')\nfor ln in [22460,22518,22563,22796]:\n    # search backwards for a page-marker-like line\n    for j in range(ln,max(0,ln-40),-1):\n        m=re.match(r'^\\s*(\\d{2,4})\\s*$', t[j-1])\n        if m:\n            print(ln, '-> nearest preceding numeric line', j, m.group(1)); break\n    else:\n        print(ln,'no marker')\nEOF\ngrep -c \"\" KLN_1966.txt; grep -n \"^\\s*9[12][0-9]\\s*$\" KLN_1966.txt | head",
 "description": "Find page markers in Klein"
}
```


### [2026-09-07T15:51:38.580Z] TOOL RESULT

```
22460 -> nearest preceding numeric line 22423 919
22518 -> nearest preceding numeric line 22488 921
22563 -> nearest preceding numeric line 22539 923
22796 -> nearest preceding numeric line 22788 933
41263
22255:910
22267:911
22308:912
22320:913
22357:914
22368:915
22392:916
22423:919
22488:921
22521:922
```


## [2026-09-07T15:51:51.797Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FVQ majus\"; grep -n -i \"majūs\\|Majūs\\|maju\\|Magian\" FVQ.txt | head -20",
 "description": "grep Jeffery for majus"
}
```


### [2026-09-07T15:51:51.859Z] TOOL RESULT

```
=== FVQ majus
805:the Magians, receive special recognition and favour. Yet as to the identity 
838:Jews and Christians, or between Jews and Magians and in all these 
11968:Like the <^uXJl JA] and the Magians, they represent a group 
13684:of Harun and Qarun ; Harut and Marut ; Yajuj and Majuj, etc. 
16149:(Al-Majus). 
16153:The Magians, or Zoroastrians. 
16168:preach the Magian faith. 2 Others, however, knew that it was derived 
21878:by M. R. Majumdar, M.A., LL.B.
```


## [2026-09-07T15:51:53.437Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AFM manjaniq\"; grep -n \"منجنيق\\|منجنیق\" AFM_pages.txt AFM.txt | head -20\necho \"=== FSF manjaniq\"; grep -n \"منجنیق\\|منجنيق\" FSF_pages.txt | head -20",
 "description": "grep Addi Shir and FSF for manjaniq"
}
```


### [2026-09-07T15:51:53.520Z] TOOL RESULT

```
=== AFM manjaniq
=== FSF manjaniq
16382:          ‫درمشان بده رومیان را زگنج‪...‬‬        ‫(آلت قلعه گیری چککوتر از منجنیق‪ .‬کذا‬
20604:   ‫منجنیق (معرب منجنیک؛ از یونانی مخانیک)‬                           ‫به چهر تو ماند همی چهرهام‬
20608:          ‫نیاید برو [کوه] منجنیق و نهتیر‬                      ‫ز تختم فریدون مگر یک دو تن‬
```


## [2026-09-07T15:51:59.057Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '16140,16180p' FVQ.txt",
 "description": "Jeffery al-Majus entry"
}
```


### [2026-09-07T15:51:59.101Z] TOOL RESULT

```
8 On the whole question of the Qur'anic Mathal, see Buhl in Acta Or., ii, 1-11. 






FOREIGN VOCABULARY OP THE QUR 5 AN 259 

(Al-Majus). 

xxii, 17. 

The Magians, or Zoroastrians. 

They are mentioned in a late Madman verse along with Jews, 
Christians, and Sabians. 

The early authorities know that the sun-worshippers are meant, 
and it was* early recognized that it was a foreign word. 1 Ibn Sida and 

others derived the word from cL said to mean _jwaJ and 



said to mean jS VI, and tell us that it referred to a man^ J) *cL, 

so called because of the smallness of his ears, who was the first to 
preach the Magian faith. 2 Others, however, knew that it was derived 
from the Iranian Magush (LA, viii, 99). 

It is clearly the O.Pers. Magush* with the ace. form of which, 

magum, we can compare the Av. jj6jj( magav or >oig 

_ ^1 ^ 

and Phlv. 3jj$ ma-yoi. 5 From Av. q$$ come the Arm.
```


## [2026-09-07T15:52:01.237Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR>=20560 && NR<=20620' FSF_pages.txt | grep -n \"pdf page\" ; echo \"---\"; sed -n '20595,20615p' FSF_pages.txt; echo \"=== page tag search\"; awk 'NR<=20604 && /pdf page/{p=$0} END{}' FSF_pages.txt; grep -n \"pdf page\" FSF_pages.txt | awk -F: '$1<20604' | tail -3",
 "description": "FSF page context"
}
```


### [2026-09-07T15:52:02.851Z] TOOL RESULT

```
---
‫که از تو مگرداد جاوید بخت‬                                    ‫بهیزدانکهبنشینم آنگه ز پای‬
‫(‪۵-۱۲۱-۳۳‬ع)‬                                          ‫مگر کامت آرم سراسر به جای‬
            ‫ملحم (با پیش اول و زبر سوم ‪-‬تازی)‬                                  ‫‪-۲‬جن جزانکه‪:‬‬
      ‫مری (برهان غیات)‪:‬‬
                      ‫یچةشاب‬
                           ‫نوعی پار‬                  ‫همی بود بوس وکاار و نبید‬
         ‫چو برزد سر از کوهگیتیروز‬                    ‫مگر شیر [زال] کوگور [رودابه] را نشکرید‬
‫زمین را به ملحم بیاراست روز‬                          ‫(‪)۱-۲۷۱-۱۷۵‬‬
‫‏(‪ ٩‬پرویز ‪۷۳۹۱0‬‬                                           ‫‪-۳‬شاید باشد که بودکه امید است‪:‬‬
   ‫منجنیق (معرب منجنیک؛ از یونانی مخانیک)‬                           ‫به چهر تو ماند همی چهرهام‬
‫وتش به سوی‬
         ‫افزاری که باآن سنگ آ‬                        ‫چو آن تو باشد مگر زهره‌ام‬
                  ‫دشمن پتراب می‌کردند‪:‬‬              ‫‏)‪(\OVA-YFF-1‬‬
          ‫نیاید برو [کوه] منجنیق و نهتیر‬                      ‫ز تختم فریدون مگر یک دو تن‬
‫بباید رتاودید آن ناگزیر‬                             ‫برد جان ازین بی‌شمار انجمن‬

‫‪۷۰۱۰۱۵۶0‬‬                                             ‫(‪)۲-۱۲-۲۴۲‬‬

                                          ‫منجوق‬                ‫همی تاخت کز روز بد بگذرد‬
      ‫درفش بیرق «ماهچة علم» (برهان)‪:‬‬                 ‫سپهرش مگر زیر پی نسپرد‬
            ‫همه گوش پر نالة بوق شد‬                   ‫(‪)۲-۶۲-۵۰۳‬‬
=== page tag search
```


## [2026-09-07T15:52:08.990Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '16180,16210p' FVQ.txt",
 "description": "More of Jeffery majus entry"
}
```


### [2026-09-07T15:52:09.034Z] TOOL RESULT

```
i/?, 6 and Heb. 313, as well as the Mod. Pers. i*. 7 In Phlv. 

we also find a form ^^^ tnagofia,* derived directly from 
the O.Pers., and this appears in the Aram. JW1JQX, Gk. /xayoy, 9 
Syr. l*a^0i and the BTtiQ of the Aramaic of the Behistun 
inscription. 10 

Lagarde, GA, 159, would derive ^j^- from the Gk. payo?, and 



1 al-Jawallql, Mu'arrab, 141 ; as-Suyuti, Itq, 324 ; Mutaw, 47 ; al-KhafiijI, 182i 

2 TA, iv, 245 ; LA, viii, 99. 

3 Vide Meillct, Grammaire Du Vieux Perse, p. 148 ; and note Haug, Parsi*, 169. 

4 Bartholomae, Al W, 1111; Horn, Grundriss, 221; Frahang, Glossary, 94; 
llcrzfeld, Paikuli, Glossary, 213. 

6 West, Glossary, 223 ; PPGl, 152 and $, 160 ; Frahang, Glossary, 114. Sco 

also ZDMG, xliv, 671, for its occurrence on a Sasanian gem. 

6 Htibschmann, Arm. Gramm., i, 195. 

7 Vullers, Lex, ii, 1197; BQ, 863. 

8 PPGl, 152 ; Frahang, Glossary, p. 113. In the Assyrian transcription of the 
Behistun inscription it is written magushu. Note also the magustan = priestly order.
```


## [2026-09-07T15:52:11.639Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"pdf page\" FSF_pages.txt | awk -F'[:]' '{print $1, $0}' | awk '$1<20604' | tail -4\necho \"--- and after\"; grep -n \"pdf page\" FSF_pages.txt | awk -F: '$1>20604' | head -2\necho \"=== AFM grep manjaniq variants\"; grep -n \"مجنيق\\|منجن\" AFM.txt AFM_pages.txt | head -10\necho \"=== AFM page 164 tag\"; grep -n \"pdf page\" AFM_pages.txt | sed -n '160,175p'",
 "description": "FSF/AFM page tags"
}
```


### [2026-09-07T15:52:13.122Z] TOOL RESULT

```
--- and after
=== AFM grep manjaniq variants
=== AFM page 164 tag
```


## [2026-09-07T15:52:19.903Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nhead -5 FSF_pages.txt; echo \"===\"; grep -c \"pdf page\" FSF_pages.txt; grep -o \"\\[pdf page [0-9]*\\]\" FSF_pages.txt | head -3\necho \"=== AFM head\"; head -20 AFM_pages.txt; echo; grep -c \"pdf page\" AFM_pages.txt",
 "description": "Inspect FSF/AFM page files"
}
```


### [2026-09-07T15:52:19.982Z] TOOL RESULT

```
   ‫‪۵‬اژهنامکت‬
‫فرهوناکژته‌هایدشوارشاهنامه‬
  SAN    ۹ 75035 7-3
          ۱
  ‎‫ا‬
===
0
=== AFM head
8
0
ܥܝ
ܶܡ 7
ܫ ܢ 0 ܣܚ
.ܡܨ >  )‏ اعم ܨ
3 ܛ 5 62 ܨ ܗ
ܡ 5
1 ` < 3[
1 , 3 5 ܢ
ل ܨ( : :
`( × 2 7 : ̄ܡ
ܝ 2 -. و
/ ܪ ܇ ܐ ܢ
. ܥ يبد < ܲܗ
ܘܨ ܝ ܓ
بي بهم 0 1 1
ܗܨ . ܢ 1 `
ܙ ^ ܢܢ
9 ܪ 1 .° 2

0
```


## [2026-09-07T15:52:24.358Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['FSF','AFM','BQT','MON','VDQ']:\n    e=d[k]; print(k,'| offset:',e.get('page_offset'),'| hint:',str(e.get('lookup_hint'))[:300]); print()\n\"",
 "description": "Page offsets"
}
```


### [2026-09-07T15:52:25.639Z] TOOL RESULT

```
FSF | offset: 484 leaves; edition/printing of this scan not identified — determine offset from printed page numbers on the page text/image when checking | hint: grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushin book (گزارشی چند درباره شاهنامه).

AFM | offset: 198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image | hint: Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').

BQT | offset: vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). | hint: grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --d

MON | offset: None | hint: Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbe

VDQ | offset: None | hint: noorlib viewer is JavaScript-rendered (WebFetch/curl get only the site chrome); needs a browser. Since it is a translation of FVQ, verify the substance via FVQ (same entry order); page numbers differ.
```


## [2026-09-07T15:52:31.797Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\ngrep -n \"منجنيق\\|منجنیق\\|منجنيك\\|منجنیک\" BQT_v4_pages.txt | head -20; echo \"=== count leaves\"; grep -c \"pdf page\" BQT_v4_pages.txt",
 "description": "grep Borhan v4 for manjaniq"
}
```


### [2026-09-07T15:52:31.849Z] TOOL RESULT

```
4813:است که شمبده بازان کنند و آن چنان امت که | منجنیق است و منجنیق معرب منجنيك باشد ‎٩‏
4836:‎٩‏ - درقاموی آمده : منجنيك بمعنی « من چه ليك > بمنی من چه نیکم برای‌کارها(۸)
4838:2 سربانی کی 1 ددع۲ ۰ هربی متجنیق » منجنیکه,
4839:عامیانه منجلق « ژاپا س 4*۹ > ۰ قس : انگ 322880261 ( منجنیق ).
4863:همچو دوت مند پعثی تخنیق (منجنيك) مندالگ « بنتح اول بروزن اند بممنی
15994:هامیان از سیم وزر پرداختن بهکه سنگه منجنیق انداختن .
17940:و ازسرچوب منجنیقآویزند و پر ازسنگه کرده ی 7 ی
17955:۲ - چون هلکی شدم نف بستهٌ منجنیق تن
21622:۹ مسحف «بلکن, منجنیقی باشد بعنی پیلوار افکن . ابوالمتن (بشاری) گفت :
=== count leaves
553
```


## [2026-09-07T15:52:32.001Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/ref_page.py BQT:2039 2>&1 | head -60",
 "description": "Fetch BQT page 2039"
}
```


### [2026-09-07T15:52:39.750Z] TOOL RESULT

```
(no exact page map; using offset -1917 -> pdf page 122; check the printed number and re-run with --pdf-page if off)
REF: BQT:2039  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 122  OCR-lang: fas

اس م بیس منچنيك
هم‌هبت که درخت بزرالینج باشد۱ - وجشم اول» | ويك. يلك را ازکامه بیرون جهاننه و همچنین تلم
حرخت بادام تلخ است ۴ - و بکراول » بمعنی را از دوات ‎٩‏ - و بمعنی کهواره هم هت که
تخم باشد مطلقاً خواء تخم کل‌وخواه تخم.خریزه | بمربی مهد کویند - و بشم اول » مصفر منج‌است
وغیرآن . که زنیور عل باشد۷ - و بممتی‌قرنفل هم‌آمده
منجخ (۱) - بکر اول وسکون ثابی | است . ۱
و جیم مفتوح بغای نقطه دار زده ‏ سنگی باشد هنجل «» بکر لول وتح ثالك وسکون
که بر فلاخن گذارند و اندازند ؛ و باین معتی | ثائی و لام » بمعنی کشکنجیر است و آن چیزی
جای نون لام هم بنظر (۷) آمته ات ۴ . باش دکه بکهیدن‌آن آرزوی کمان کنیدنحاسصل
منج زراوشان « سم ارزو کرزای | خود.
مار یاو رای می‌نقطه وی شله‌دار هر منجلاب « بت ار و ثالك . کوبرا
و بالف کشیده ونون درآخر » تخم کلی است که | کوین دکه دریس حمامها ومطبخهاکنند تاآبهای
آنرا خیری میگوبند ۴ . چی‌کن ومتعمل‌بدانجا رود - وآب پدبو وکنده
منجث - بنتح اولبروزن اسد. بمعنی را نی زکویند ۸ .*
برجستن باشد * - و یکی از جملةٌ شمیده هابی منجنياگ « با کان » بر وزن و همنی
است که شمبده بازانکنند و آن چنان است که | منجنیق است و منجنیق معرب منجنيك باشد ‎٩‏
‏پاره های‌آهن وسنکه ریژه را درکانة آب ریزند وآن فلاخن مانندی است بز رک ه که برسرچویی

(۱) چش : منخج (۱) (۲) خوا: - بنظ . . 9

۱ - درقاموی « منج » معرب هنگه بمعنی‌دانةٌ مسکرآمده » و درکتب طب باین‌معنی.
« بنج » است معرب « بنگه > و رك : ح۹ صفحةٌ قبل. ۴ - ر4: حه صفحهٌ قبل .

۴ - در جهانگیری و رشیدی « ملچخ > باین معنی‌آمده . رك : ملچخ.

۴ - «منج زراوشان » اسم فارسی امت » وآن تخمی‌است شبیه بنانخواه وسرخ وبالیده‌تن
ازآن ونزد بسنی تغم خیری بری‌است. مسکر ومفرح واکثار اومغیر عقل است .» « تحفةٌ حکیم
عژمن >. - رك : جهانگیری ورشیدی . ظ . ازمعنی دوم استخراج کردماند. رد :ح٩‏ ۰

۹ - « منجك » آن بود که مغمبذان [ بدو ] قلم و چیز ها بر جهاند . منجینکه
( ترمذی ) گوید :

بمنجك جهاندی مرا از درت بهانه نهادی تو بر مادرت .؟
2 لغفت فری ص ۲۷۷ ؟ ورك : رشیدی .

۷ - از : منج (ه.م.) ۳۲ که ( پسوند صفیر ).

۸ - اگر برکه‌ای پرکنند از کلاب سگی در وی افتد »کند منجلاب ..

سعدي شیرازی ۸« رشیدی » .

‎٩‏ - درقاموی آمده : منجنيك بمعنی « من چه ليك > پعنی من چه نیکم برای‌کارها(1)
( قه‌اللقةٌ عامیانه ). اصل کلمه مسحف میخنیق از 0625221808 « لیدل واسکات » ۳ بوناتی
32 ۰ سربانی شوی.1دم۲ ؛ عربی متجنیق » منجنیکه,
عامیانه منجلق « ژاپا س 4*۹ > » قس : انگ 322880261 ( منجنیق ).

‏ماجنیق - رك : منجنيك .
```


## [2026-09-07T15:53:01.046Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor w in \"مجوس\" \"منجنیق\" \"ماشین\" \"موبد\"; do echo \"=== $w\"; grep -c \"$w\" MON_part1.txt MON_part2.txt 2>/dev/null; done\necho \"=== HRN mogh/mobad\"; grep -n \"moġ\\|mōbaḍ\\|mobed\\|Magier\" HRN.txt | head -20",
 "description": "grep MON and Horn"
}
```


### [2026-09-07T15:53:02.512Z] TOOL RESULT

```
=== مجوس
MON_part1.txt:0
MON_part2.txt:6
=== منجنیق
MON_part1.txt:6
MON_part2.txt:5
=== ماشین
MON_part1.txt:59
MON_part2.txt:56
=== موبد
MON_part1.txt:3
MON_part2.txt:13
=== HRN mogh/mobad
8553:984. muy, möy 'Magier, Feueranbeter*^), möbed,
8561:') Im späteren Neupersisch ist der Magier zum '(ohristl.) Mönch*
9608:. -^wo^ *Magierhaoma (eine nicht näher zu bestimmende
```


## [2026-09-07T15:53:02.919Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HUB magu\"; grep -n -i \"magu\\|mōbad\\|mobed\\|Magier\" HUB.txt | head -20\necho \"=== LKT manganon/mangonel\"; grep -n -i \"manganon\\|mangonel\\|mandschanik\\|mangan\" LKT.txt | head -10",
 "description": "grep Hübschmann and Lokotsch"
}
```


### [2026-09-07T15:53:02.982Z] TOOL RESULT

```
=== HUB magu
4292:p. 72 etc. (gesprochen moypet), ap. *magupati-.
4406:moy *Magier, arm. mog und (spater) mov (pi. movan), syr.
4408:geschrieben magu^ gesprochen moy^ gr. f-idyog, hebr. yo, ap.
4409:magU' (davon phi. magupat = arm. mogpet = movpet =
7492:*Gro8se*, dial, mas in inasmuydn *Gross-magier (Barbier
8828:Grube* H. 985 ■= zd. maya- Xoch*; muy^ may *Magier
8829:= ap. magu' (= tnayii'); mey *Wolke* = zd. maeya--^ arDy,
8846:marg 'Wiese, Aue', mog *Magier , tSg 'Spitze der Lanze*,
8868:mdbad = phi. magupat,
8879:mogac anderjapet bei Faustus 157), ^YA.magupat, vgl.
8880:ap. magu- *Magier' = phi. mag, np. muy,
=== LKT manganon/mangonel
```


## [2026-09-07T15:53:09.419Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN 984\"; sed -n '8550,8565p' HRN.txt\necho; echo \"=== HUB 4400-4412\"; sed -n '4400,4412p' HUB.txt\necho; echo \"=== HUB 8865-8870\"; sed -n '8865,8872p' HUB.txt",
 "description": "Print Horn/Hübschmann entries"
}
```


### [2026-09-07T15:53:09.483Z] TOOL RESULT

```
=== HRN 984
kurd. mistin 'fegen'; af/. mu/al; bei. musag, n. musay
'reiben*, kratzen, streichen, salben, mahlen' (244).
Eine Doublette zu np. maltden (No. 962).
984. muy, möy 'Magier, Feueranbeter*^), möbed,
ap. magu-; aw. -moyu- in moyu.fbis-? (vergl. Geldner,
*) Irgendjemand hat, wie mir Herr Prof. Nöldeke sagt, irgendwo
(die SteUe war augenblicklich nicht aufzufinden) das als arabisch geltende
medhüs 'sinnlos* für ein persisches Wort (|/ mad' + hös 'Verstand, 8inn*J
erklärt. Ich denke aber, dann könnte es nur mesthös lauten.
') Ganz falsch war natürlich meine Bemerkung ZDMG. 48, 36
Note 34.
') Im späteren Neupersisch ist der Magier zum '(ohristl.) Mönch*
und besonders zum 'Kneipwirt, Zecher* geworden (H ä f i ? häufig), vergl.
auch muybece^ muyän u. a. m.— 221 —
Ved. Stud. II, 19); phlv. magu, magupat (arm. LW.
mog^ mogpet, movpetan movpet), daneben maupat (syr.

=== HUB 4400-4412
= phi. fairaxv; suxtin ^= suxan *Wort', paz. saxun aus
sax^'arij arm. -sohun im N. pr. Bastsohun (bei Mos. Chor.).
Wechsel von a und u: -bad == -bud *Herr (vgl. herbiid,
mobad etc.) = zd. paiti-, arm. -pet ; banafsa 'Veilchen' neben
binafsa, bunafsa, arab. banafsaj, phi. vanavsak^ etc.
Fiir ap. a erscheint mp. o = np. w und 5 in 7nuy =
moy *Magier, arm. mog und (spater) mov (pi. movan), syr.
muy- in muyanandarzbad (Hoffmann, Ausziige p. 50), phi.
geschrieben magu^ gesprochen moy^ gr. f-idyog, hebr. yo, ap.
magU' (davon phi. magupat = arm. mogpet = movpet =
syr. mowed = np. mobad).
*) In der Kegel bleibt aber a bei Labialen.
*) Muwaffaq hat duvam *der zweite* 4, 16, 17; 5, 18 neben

=== HUB 8865-8870
bonum*, phi. murvak Yatk. i. Zar. p. 46, Anm.; marvarld
Terle* (marvarldln *of pearl' JRAS. 1894, p. 488), phi. mar-
vdrlt etc. (NSldeke, Pers. Stud. II, 44) = juapyagirTjg ;
mdbad = phi. magupat,
Aber neben Marv (dazu np. Maro i rod 'Fluss-Merv',
Noldeke, syr. Ghron. 39, arab. Marvarrud bei Yaqut =
arm. Marvirot Laz. Pharp. 233 im Unterschied von der
Hauptstadt, arab. Marv as-sdhijan (Yaqut) = np. Marv
```


## [2026-09-07T15:53:21.730Z] TOOL CALL #39: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-07T15:53:21.739Z] TOOL RESULT

```


```


## [2026-09-07T15:53:23.235Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON ماشین\"; grep -n \"ماشین\" MON_part2.txt | head -5\necho \"=== MON مجوس\"; grep -n \"مجوس\" MON_part2.txt | head -5\necho \"=== MON منجنیق\"; grep -n \"منجنیق\" MON_part1.txt MON_part2.txt | head -5",
 "description": "grep Mo'in text"
}
```


### [2026-09-07T15:53:23.322Z] TOOL RESULT

```
=== MON ماشین
5890:شتدكه ۱ (تو سرط د ماشین). 
6497:(مک.) رل ماشین. 
9654:ماشین‌های خودکار که تا ۱۰۰۰ متر در 
10696:ماشین نصب کنند. دور قالیاق: (مکد.) نواری 
17534:يا ماشین تحریر چیزی روی ورقة بالایی 
=== MON مجوس
6185:شعر. فرزند مجوس: (کد.) شراب. فرزند 
29925:زردشتی» زر تشتی» مجوس. 
48692:مجوس: : ۸1115 |معر . آرا. مجوشا| (ص.) 
48693:فردی از فرق؟ مجوس. مجوسی. (ص.) 
73639:قبرستان مجوس. 
=== MON منجنیق
MON_part1.txt:24970:منجنیق. سردیوار. 
MON_part1.txt:32807:منجنیق. سنکی که از کشتی به شتی غنیم 
MON_part1.txt:50068:بدان پنبه ر سند؛ چرخه. نوعی از منجنیق که 
MON_part1.txt:93420:زخمه. منجنیق. (نو.) هوپیما؛ ج. طیارات. 
MON_part1.txt:95359:کوچکتر از منجنیق که در جنگ‌های قدیم
```


## [2026-09-07T15:53:29.303Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON 48690-48696\"; sed -n '48688,48698p' MON_part2.txt\necho; echo \"=== MON موبد entry\"; grep -n \"^موبد\\|موبد:\\||معر\\|مغ:\" MON_part2.txt | grep \"موبد\" | head -8",
 "description": "Mo'in majus and mobad"
}
```


### [2026-09-07T15:53:29.383Z] TOOL RESULT

```
=== MON 48690-48696
(مسحوره (6-)۱22013۷۷۸2-۸ آمسحر. ع. 
مزوجه] (!.) عمامةً بسیار بزرگی که رجال 
تر کت وا لا ا مانب اش دی نها دید 
(فلسفی. شاه‌عباس ۱۸۰۰۱ ج ۲ مز دو جه. 
مجوس: : ۸1115 |معر . آرا. مجوشا| (ص.) 
فردی از فرق؟ مجوس. مجوسی. (ص.) 
فد وی کی کهااز اه کات 
نباشد؛ مشر ک. (ا بن اسی اصعة ۱۵۱ 
قروینی. بادداشتها ۲۰۷ ۵). 

محوف: ی [ع.] (امف.) آنجه که 

=== MON موبد entry
56921:موبدان. 
92705:موبدان. رئیس آتشگاه. ضح. این کلمه
```


## [2026-09-07T15:53:39.768Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== 92700-92710\"; sed -n '92700,92712p' MON_part2.txt\necho; echo \"=== مغ entries\"; grep -n \"مغ:\\|مغ ۱\\|\\[په\" MON_part2.txt | grep -n \"مغ\" | head -10",
 "description": "Mo'in mobad/mogh"
}
```


### [2026-09-07T15:53:39.845Z] TOOL RESULT

```
=== 92700-92710
به وسیلةٌ نشار آب می‌چرخد و تولید 
الکتریسیته می‌نماید. 

هسیر بد: ۱1-0 (۱.) استاد» امه رعان 
نا کرو آموزنده. بیشوای دینی؛ موند 
موبدان. رئیس آتشگاه. ضح. این کلمه 
مرکب از دو جزء است: نخستین که 2610۳۸ 
باشد به معنی آموزش و تعلیم و جزو دوم 
211111 ( - ید سوند اتصاف) است به معنی 


تست هک ریس تست رظن 


=== مغ entries
```


## [2026-09-07T15:53:42.759Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%D9%86%D8%AC%D9%86%DB%8C%D9%82",
 "prompt": "Give the full etymology sections for Persian منجنیق and Arabic منجنيق (manjanīq): what Greek word is it derived from (μαγγανικόν manganikon or μηχανική mēkhanikē?), any Syriac/Aramaic mediation, and cited sources."
}
```


### [2026-09-07T15:53:49.492Z] TOOL RESULT

```
# Etymology of منجنیق (manjanīq)

Based on the Wiktionary page provided, here's what can be determined:

## Greek Origin

The page states the word is "ultimately from [Ancient Greek](https://en.wikipedia.org/wiki/Ancient_Greek "w:Ancient Greek") _[μαγγανικά](/w/index.php?title=%CE%BC%CE%B1%CE%B3%CE%B3%CE%B1%CE%BD%CE%B9%CE%BA%CE%AC&action=edit&redlink=1 "μαγγανικά (page does not exist)")_ (manganiká)."

The specific Greek form cited is **μαγγανικά** (manganiká), not the alternative forms you mention.

## Etymology Chain

**Ottoman Turkish section:** "Borrowed from Arabic _مَنْجَنِيق_ (manjanīq, 'ballista, catapult'), ultimately from Ancient Greek _μαγγανικά_ (manganiká)."

**Persian section:** "Borrowed from Arabic _مَنْجَنِيق_ (manjanīq)."

## Sources and Mediation

The page provides **no information** about:
- Syriac or Aramaic mediation
- The specific pathway from Greek through intermediate languages
- Scholarly sources documenting the etymological chain

The citations listed are historical dictionaries (17th-19th century Ottoman Turkish lexicons) rather than etymological analyses of the Greek-to-Arabic transmission.
```


## [2026-09-07T15:53:54.754Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/mangonel",
 "prompt": "Full etymology of \"mangonel\" — Greek source word, and whether it is connected to Greek mekhane or manganon."
}
```


## [2026-09-07T15:53:56.525Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/mag%CA%B0-",
 "prompt": "Does this reconstruction page exist? What is the PIE root for 'to be able, have power' (magh-) and its descendants (Greek mekhane, Germanic magan, Old Persian magus)?"
}
```


### [2026-09-07T15:53:59.740Z] TOOL RESULT

```
# Etymology of "Mangonel"

Based on the Online Etymology Dictionary, here's the word's origin:

**Mangonel** entered English in the mid-13th century from Old French *mangonel*, meaning "catapult, war engine for throwing stones." The source traces back through Medieval Latin *mangonum* to Vulgar Latin *\*manganum* ("machine").

## Greek Connection

The ultimate source is Greek *manganon*, defined as "any means of tricking or bewitching." The etymology suggests a possible Proto-Indo-European root *\*mang-* meaning "to embellish, dress, trim," though scholar Beekes proposes it might be Pre-Greek in origin.

## Regarding Mekhane

The document does not address a connection between *manganon* and the Greek word *mekhane*. It only establishes *manganon* as the Greek source and notes uncertainty about whether this root is truly Proto-Indo-European or Pre-Greek.
```


### [2026-09-07T15:54:01.350Z] TOOL RESULT

```
# Proto-Indo-European Root *megʰ-

Yes, this reconstruction page exists on Wiktionary. The PIE root is **\*megʰ-** (with an alternative form **\*magʰ-**), which means "to be able."

## Key Information

The root carries the definition: "to be able," with a synonym being \*ḱek-.

## Notable Descendants

The page documents several descendant forms across Indo-European language families:

- **Sanskrit**: maghá (मघ)
- **Avestan**: moġu
- **Old Persian**: maguš
- **Old Norse**: máttr
- **Old Irish**: smacht
- **Proto-Germanic**: Forms like mahtiz

These descendants reflect the semantic range of ability and power across ancient Indo-European languages, supporting the reconstructed root's meaning and demonstrating how this concept evolved across different linguistic branches.
```


## [2026-09-07T15:54:08.338Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%BC%CE%B7%CF%87%CE%B1%CE%BD%CE%AE",
 "prompt": "Etymology of Ancient Greek μηχανή: from μῆχος, from which PIE root? Doric form μαχανά? Descendants (Latin machina)? Any note that Beekes considers it Pre-Greek?"
}
```


## [2026-09-07T15:54:10.437Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%D9%88%D8%A8%D8%AF",
 "prompt": "Etymology of Persian موبد (mowbad/mobed): Middle Persian form, Old Persian/Avestan source, and the etymology of Persian مغ (moğ) if mentioned."
}
```


### [2026-09-07T15:54:14.293Z] TOOL RESULT

```
# Etymology of μηχανή

**PIE Root:** The word derives from Proto-Indo-European *megʰ- ("to be able"), composed from μῆχος (mêkhos, "means") plus the feminine suffix -ανή.

**Doric Form:** An alternative Doric variant exists: "μᾱχᾰνᾱ́ (mākhănā́)"

**Latin Derivative:** The article doesn't mention Latin *machina* or other Romance language descendants, though it does list Classical Syriac, Coptic, Armenian, and Pashto descendants.

**Beekes' Pre-Greek Theory:** Scholar Robert Beekes "argues for a Pre-Greek origin, based on the infix -αν-, as well as formal difficulties in deriving the word's ablauting paradigm from *megʰ-" and proposes it may be "a doublet of Ancient Greek μάγγανον (mánganon, 'charm, block')."

The traditional etymology connecting it to the PIE root remains standard, though Beekes presents an alternative Pre-Greek substrate hypothesis.
```


### [2026-09-07T15:54:16.907Z] TOOL RESULT

```
# Etymology of Persian موبد (mōbad/mubad)

## Origin Path

The word traces back through Middle Persian to Old Persian. According to the Wiktionary entry: "From [Book Pahlavi needed] (mgwpt' /⁠mowbed⁠/) with the same meaning, from Old Persian _[\*magupatiš⁠](/wiki/Reconstruction:Old_Persian/magupati%C5%A1%E2%81%A0 "Reconstruction:Old Persian/magupatiš⁠")_"

## Literal Composition

The term breaks down as: "literally 'head of the Magi'" combining two elements—_مغ_ (moġ, meaning "magus") and _ـبد_ (-bad, signifying "lord, master").

## Related Forms Across Languages

The word appears in several ancient language borrowings, including Old Armenian _մոգպետ_ (mogpet) and Classical Syriac _ܡܘܒܕ_ (mawbed), demonstrating its wide adoption across the Iranian cultural sphere.

## Modern Meaning

In contemporary Persian, موبد designates "a Zoroastrian priest," reflecting its historical religious significance.
```


## [2026-09-07T15:54:22.474Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%D8%BA",
 "prompt": "Etymology of Persian مغ (moğ) \"magus, Zoroastrian priest\": Middle Persian form, Old Persian/Avestan source."
}
```


## [2026-09-07T15:54:23.696Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%D8%A7%D8%B4%DB%8C%D9%86",
 "prompt": "Etymology of Persian ماشین (māšin) \"machine\": from which language was it borrowed (French machine, Russian, English)?"
}
```


### [2026-09-07T15:54:28.315Z] TOOL RESULT

```
# Etymology of Persian ماشین

Based on the Wiktionary entry, the Persian word ماشین (māšīn) was "Borrowed from French _machine_."

The etymology tree shows the word's journey through multiple languages: it originated from Proto-Indo-European, passed through Ancient Greek (μηχανή), then Latin (māchina), Middle French, and finally French (machine) before being adopted into Persian.
```


### [2026-09-07T15:54:28.992Z] TOOL RESULT

```
# Persian Word: مغ (moġ)

This Wiktionary entry documents a Persian term with two distinct etymologies:

## Etymology 1: Magus
The noun **مُغ** derives from Middle Persian and Old Persian, ultimately tracing to the term for a Zoroastrian priest. The entry notes it means "magus" and provides related terms like گبر (gabar) and مجوس (majus). A historical quotation from 'Orfi Shirazi (c. 1585) illustrates usage: "that you may enter the temples of the **magi** and see [their] arcane secrets."

## Etymology 2: Depth
The adjective **مغ** comes from Middle Persian meaning "hole," and the entry indicates it's a dated term equivalent to "deep" or "abyssal," with synonyms including ژرف (zarf) and عمیق (amiq).

The entry includes detailed pronunciation guides across Classical Persian, Dari, Iranian Persian, and Tajik variants, reflecting the word's historical importance across Persian-speaking regions.
```


## [2026-09-07T15:54:37.666Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in 'https://en.wiktionary.org/wiki/%D9%85%D9%86%D8%AC%D9%86%DB%8C%D9%82' 'https://www.etymonline.com/word/mangonel' 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/mag%CA%B0-' 'https://en.wiktionary.org/wiki/%CE%BC%CE%B7%CF%87%CE%B1%CE%BD%CE%AE' 'https://en.wiktionary.org/wiki/%D9%85%D9%88%D8%A8%D8%AF' 'https://en.wiktionary.org/wiki/%D9%85%D8%BA' 'https://en.wiktionary.org/wiki/%D9%85%D8%A7%D8%B4%DB%8C%D9%86'; do\npython3 tools/fetch_source.py \"$u\" --note \"page 318, root Magh1: manjaniq / mangonel / PIE magh- / mekhane / mobad / mogh / mashin\" 2>&1 | tail -2\ndone",
 "description": "Archive web sources"
}
```


### [2026-09-07T15:54:41.295Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/e668c7b09ba59363.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cfed52b12796f553.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1be95b9ff81fa67b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0c040ca5a27e2b78.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8820ab6a1238ee63.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9ad71b2dc9a98706.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c5358a3bce664991.txt
```


## [2026-09-07T15:54:49.568Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== NYB magu/mowbed\"; grep -n \"magu\\|mgw\\|mowbed\\|mōbad\" NYB_vol2_glossary.txt | head -10\necho \"=== SKT machine/magic/mangonel/might\"; grep -n -i \"^machine\\|^magic\\|^mangonel\\|MACHINE\\|MAGIC (\\|MANGONEL\" SKT.txt | head -10\necho \"=== AFA manjaniq\"; grep -n \"منجنيق\\|Manganon\\|mangan\" AFA.txt | head -10",
 "description": "grep Nyberg, Skeat, Fraenkel"
}
```


### [2026-09-07T15:54:49.637Z] TOOL RESULT

```
=== NYB magu/mowbed
1210:dastavar [dstwbl], cas. obl. dastavareh [dstwblyh] 9815 : 1. valid religious doctrine, custom, law 10871; canon of religious doctrines etc. 109°; decision (of a relig- gious authority): pat ~ % oi 101%; <pat> ~ + Hušetar 96; pat hàn à Husetarmäh ~-éh 9814-15, — 2. an expert in religious matters, a theologian, a Dastur, also of the Zoroastrian clergy in general: a theo- logian 1018; x“atai u dahyupat u sardār u ~ + den 1081-2; pl. cas. obl.: ~-dn u dätavarän u hérpatàn u magupatān u den- burtärän 107'3-14, — MPrs dstwr ‘a priest’ (S); Paz. dastūr, Skr. v. ācārya, guru; NP dastür in profane senses (v. Steingass). — dast- from Av. (746) dqh- ‘to teach’, cf (745) dqstvà ‘religious doctrine’; hence MPrth dst ‘able, skilful? (A-H III). Cf Bailey, ZP 160, n. 5; TPhS 1945, 8.
1832:ham-göhr [hmgwhl] of the same sub- stance 88%, — MPrs hmgwhr (A-H II).
1833:ham-gón [*hmgwn'] = ham-gónak seems to be meant 1051’, corresponding to ētēn ke (for ka or ku) 1. 16; MSS hmk', hmt'.
1834:ham-gónak [hmgwnk'] of the same kind. 1. adj. consistent, coherent, homogeneous: druyist u rast u ~ hast 11191 (but Paz. without the last u, and Skr. v. ičyevam). — 2. adv. in the same manner, in the same way; accordingly ; thus; ~ cigön-am hacapar nipišt in the way I have written above 10212-13, — 545-? read ham-ātvēnak, q. v. MPrs hmgwng; Paz. hamgüna, Skr. v. ttyevam; NP hamgünah. Av. (482) lgaona- ‘hair’.
1835:ham-gobisnéh [hmgwbányh] conversation 10615,
1966:hāvišt [h”wšt'] disciple, priestly novice 1119. — Av. (1806) hävista-; FrP 13 ex- plained by magu (mög) ‘member of the class of Magi’. Bailey, JRAS 1953, 97.
2368:magu-pat
2373:magü [mgw, inscr.], magük [mgwk], még [mwg FrP 13] a Magus, a Magian: Nar- sahē i magi P1:7; cas. obl. magve in magvé-mart [mgwymlt'] pl. cas. rect. the Magians 20°; pl. cas. obl. mög-martän [mwgmlt?n'] 28; magüné [mgwny] pl. cas. rect. 108!!, cas. obl. 11215. — OP magu-, nom. magus, whence Syr. lw. mgüsä, Arab majüs-; Av. only once in the compound (1176) moyu-ibiš- ‘enemy of the Magi. The authentie Milr forms are: 1. NW mög, whence the Arm. lw. mog, NP möy, pl. méydn; 2. SW mov-, v. s. v. magupat. The other forms are archaisms preserved as learned spellings. The pl. maguné re- presents the old gen. pl. of the u-stems: OP *magūnām > *magün + the common ending -é of the cas. obl. sg. spuriously added, ef örsäneh rād 5814 (v.s. v. ētšān and rdd); another ex. of the pl. cas. obl. in -ün is MPrs dušmynwn < *dušmainyū- nam (S; Bthl, ZairWb 152-153). The reading mgwmy is warranted by the in- scriptions.
2374:magu-pat [mgwpt'] chief of the Magi, or: chief Magian, of the head of the Zoroas- trian priesthood 1104; in this sense com- monly ~-dn ~ 10-12, passim; 168. 100?; — a Zoroastrian priest of this class in general: dastavardn u dätavaran u hēr- patün u ~-dn 1078, — The Olr form preserved as an archaic spelling; the authentic Milr forms are: 1. NW mogpat, Arm. lw. mogpet; 2. SW movpat, Arm. lw. also movpet (Etiša), Syr. lw. mwpt?, mwhpt’, mwhbi? ; NP mobad. V. s. v. ‘pat.
3000:1pat [pt'] dignitary, chief 5819. 11418. — Av. (821) pati-; in compounds: hér-pat, dahyu-pat, magu-pat, spüh-pat; cf also rues.
=== SKT machine/magic/mangonel/might
8:+  Refrain  from  automated  querying  Do  not  send  automated  queries  of  any  sort  to  Google's  system:  If  you  are  conducting  research  on  machine translation,  optical  character  recognition  or  other  areas  where  access  to  a  large  amount  of  text  is  helpful,  please  contact  us.  We  encourage  the use  of  public  domain  materials  for  these  purposes  and  may  be  able  to  help.
1194:automiLton,  a  self-moving  machine. (Gk.)  Gk.  airroiAarov,  neut.  of  avro/iaroi, self-moving.  —  Gk.  avrd-,  for  ovrdj,  self; and  a  stem  ftar-,  appearing  in  ^r-ti^,  I seek  after,  strive  to  do.  Cf.  Skt.  ma/d, desired,  pp.  of  mdn,  to  think.  (^MAN.) autonomy,  seU-govemmcnt.  (Gk.)  Gk. avjovo}ila,  independence.  —  Gk.  oiriivo^nr, ijtc,  living  by  one's  own  laws.  — Gk.  avru', self;  and  wifxoftat,  1  sway,  from  vifttty,  to distribute  (see  Nomad).
2241:brake  (i),  a  machine  for  breaking hemp  ;  a  name  for  various  mechanical  con- trivances. (O.  Low  G.)  M.E.  brake.— Low  G. brake,  A  flax-brake;  O.  V>VL.braecket '  a  brake  to  beat  flax ;'  Hexham.  —  Dn. breken,  to  break ;  see  Break.
2946:Capatan.  (F.  — Span.— L.?)  )e.ci\btstan. ^Span.  (c^strantf,  <abrcstante,  an  cnijinc to  raise  weights.  £tym.  uncertain:  but Min&heu'B  Span.  Diet.  0^^3)  ba&  cabtt- itanti  as  the  form,  and  Monlaa's  £tym. Span.  Diet.  (i88i)  has  cabria,  a  crane, and  suggests  Span,  cobra  estantt,  a  fixed (permanent)  goat;  since  the  Span.  eain-A meana  (i)  goat,  (i)  a  machine  for  throw- ing large  clones.  Here  Sp.  ca^^a^L.  i-fl//tf» a  she-goat ;  sec  Oaper  ( i ) ;  and  estantc  =■ L.  sioHtem.  ace  of  x/iimj,  &taudiag,  from ttart,  to  staiid.
4610:■   machine    for  nDOOthing (F*»U*Ck  )     '  CaitHiitr,  to  press (  *   BsHtv.  «*  F.  ioUmdrtr,  to  smootb tti^Mdrt^  tb.,  a  calcntkr.  -  Low  L. a  c^lcihlcr  ;    corniptioo    of    L. a    roller    (as    above).       Der. ;  ■  MKK>iher  of  liaco,  a  aii!>talcen for  tmkmJnr, baL  fF^U-Gk)  Vi.ZnmtfaU. rimi-ulf.  —  L.    cyvif>a,'Mm.  —  Cik. %  a  cyiobal ;  named  from  its  cup- t(ac.  ••  Gk.    xvuBn*    «    cup.  4-  ^kt. a  jar     Allied  to  Oup  ;  aitd  sec iV    CVKLBH.) l,th  a.*L.-Gk.)  M.E.ri/m^, the    orig.    teoiie   w&s  cymlal ; diinc  or  ringing  ot  a  cjuibal. friMn  F.  eAimbaU,  dialectal  roim WarAo^    (above).      Dor.  fhtrntt
10002:Lathe  (i>,  a  machine  for  tuminc  wood, &c.    (Scand.)     Icel.   IdfS   (gen.   /rfB-«r),  a smith's  lathe.     Perhaps  for  Mllrtt,  and  fro A/a^a,  to  larie :  cf.  A.  S.  MlaJ-xt'eoqt,  a  wh of  a  ivell,  for  drawing  water ;  see  Lade  (3).
10647:IjOOm  ( t),  a  machine  for  weaving  cloth. (E-l    M.  E.  iome,  a  tool,  implement,    A.  S- ge-Uma,  a    tool,    implement,    LDiirunicni.     ^ Der.   Meir  io&m,   where  loom    meant   any implement,  hence  a  piece  of  lumiture.
10869:meohanlc,  pertaining  to  machines. (F.  — L.*Gk.)  M.  E  mtchaniMe,  in  the 5<n5e  'mechanic  art.'  — O.  F.  mttrhamiqut, mechanical.  ~  L.  mtchamica.  —  Gk.  tirix^^'^* science  of  machines.  — Gk.  F9X<»^  (above) XloGkerel ;  ace  Maoiilato.
11037:Mangle  {t\  a  roller  for  sm( to  smooth  Unen.  (Du,  —  Low Itorrowed  from  Du.  maMgrUn,  to  1 roll  with  a  rollmg-pio  ;  wutngtl-tttk ing-pin,  cylinder  for  smoothing  Una corresponding  Ital.  word  is  sMiV kind  of  pressc  to  prcssc  buckiom/ Both  Du.  and  Ital.  words  are  trom mamganum,  mangona,  a  military  ins) for  throwing  stones,  worked  with and  winch.  Indeed,  the  Ital.  mtitg^ means  a  mangonel.  —  Gk.  iniftt machine  for  defending  fc of  a  pulley-     Allied  to .
11038:mangonel,  a  war>cn|^ -Gk.)  O.F.ffiiM!;iMM/(lateri a  mangoocL  —  Low  L. of  mangtuut  (above).
=== AFA manjaniq
```


## [2026-09-07T15:54:52.205Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== ARB mo3rb مجوس/منجنیق\"; grep -n \"مجوس\\|منجنيق\" ARB_mo3rb.txt ARB_abdulraheem.txt | head -10\necho \"=== TAD\"; grep -n \"منجنيق\\|مجوس\" TAD_pages.txt | head -10\necho \"=== PLA manganikon\"; grep -n -i \"manǧanīq\\|mangan\\|منجنيق\" incoming/PLA/PLA_pages.txt | head -10",
 "description": "grep Arabic loanword dictionaries"
}
```


### [2026-09-07T15:54:52.291Z] TOOL RESULT

```
=== ARB mo3rb مجوس/منجنیق
ARB_mo3rb.txt:4802:أنى داود ٠‏ تقال الببيق بعد روايته : < نم ماصتعوأ 6 بتركوا روابة الأسيذ ا مجوسى » وأخذوا برواءة : 
ARB_mo3rb.txt:21667:ويقال 2 منجنيق “ و3 ” متجزيق “ بف ار وكيرها ٠‏ وقيل المم والنون فى أوّله 
ARB_mo3rb.txt:21682:ابن دريد» ثم قال عقريه : « على أن المنجنيق أغدمى معرب» ٠‏ (0) فيس « نكان» وهو 
ARB_mo3rb.txt:21683:تخالف لساثر الفسخ وشرح اللبريزى»ه (07) وتمع أيضا ”عانق '" و ””منجنيقات ““* 
ARB_mo3rb.txt:21697:فمربوه وقالوا '”منجنيق““ ٠‏ وم أعرف هذا الشباب قبجاق ولا القصيدة ولا شرحها ٠‏ 
ARB_mo3rb.txt:21715:يق الال أقوام دف طلم 03 بالمنجنيق وصكا ا 
ARB_mo3rb.txt:21739:*” حي المنجنيقٌ حدق ““ > (ه) من قصيدة يهجو بها الهم ) فى ديراه (ص ١‏ مم سو جم). 
ARB_mo3rb.txt:22619:(8) الزياده من ) »ى ٠.‏ ومادة””مجوس“" لم تذ كر فى 2ه 
ARB_mo3rb.txt:22622:استعمل استعالى اسم المنس ٠‏ ف القاموس : « ”” مجوس ©“ كصبور : رجل مسغير الأذثين وضع دينا 
ARB_mo3rb.txt:22623:واكم سرف مج كوش ٠“‏ دجل مجوسى"ج موس » كيودى و ييودى» ٠‏ وكلدة ”منج ' “طبطات 
=== TAD
2598:  ‫مجوس ‪ -‬ف الارامية « مجوشا »‪ 6‬وف اليونانية ‪ 60825‬وف اللائينية كندهةم‬
2601: ‫حكاء ‪ .‬وقال أحد الملماء ان انظ مجوس منذ القرن‬           ‫أسباط مادي ‪0‬‬
=== PLA manganikon
13795:olo»-         mafänig:               Pl.        v. Go                 manganig       q. v.
13797:Grle» - mafänig:                      Pl. v. (5a                       manganiq        q. v.
14084: Mus        -        manganig:
14089:       pers. «U, mangane 4, syr. Bugr”.
```


## [2026-09-07T15:55:04.134Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '14078,14098p' incoming/PLA/PLA_pages.txt\necho \"=== find pdf page tag before 14084\"; grep -n \"pdf page\" incoming/PLA/PLA_pages.txt | awk -F: '$1<14084' | tail -2",
 "description": "Asbaghi manganig entry"
}
```


### [2026-09-07T15:55:05.496Z] TOOL RESULT

```
la           -           anganig:              Pl.     v. zii. manfanig q. v.

sol              -        anfanigi:                  "derjenige,          der       solche    Maschinen        macht".


2
 Mus        -        manganig:
                              v7           "Kriegsmaschine"                    aus    pers.    War.      man
                                                                                                                ua,
                                                                                                                Ce nik
                                                                                                                       3 ?             aus
       pers. «U, mangane 4, syr. Bugr”.

Ja» -                manfanik = manfaniq q. v.

dr      -    mandil:                 "Gürtel"           pers.        6   ?°


Gr%»- manas:                   "Fröhlichkeit"              CT Pers.                  mani®    7 mp.        (rare maniSn re aw.
                 8
       man           .
=== find pdf page tag before 14084
```


## [2026-09-07T15:55:16.155Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== WLD Bd2 magh\"; grep -n \"magh-\\|mägh-\\|maghti\" incoming/WLD/WLD_Bd2_pages.txt | head -10",
 "description": "grep Walde-Pokorny Bd2"
}
```


### [2026-09-07T15:55:16.201Z] TOOL RESULT

```
=== WLD Bd2 magh
14818:                                      magh- magh
14819:                                            :                magh-                              227
14837:magh- magh- „k6nnen, vermogen, helfen“.
14885:magh- „kampfen".
```


## [2026-09-07T15:55:17.728Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== ARY مغ/موبد/ماشین\"; grep -n \"موبد\\|منجنیق\" incoming/ARY/ARY_pages.txt | head -10\necho \"=== IEC magh\"; grep -n \"magh-\\|maghos\" IEC.txt | head -10\necho \"=== SYN able/power magh\"; grep -n \"magh-\" SYN.txt | head -10",
 "description": "grep Aryanpur, Mann, Buck"
}
```


### [2026-09-07T15:55:17.803Z] TOOL RESULT

```
=== ARY مغ/موبد/ماشین
9693:زوت» زوتر زاوتر (به چم "موبد زرتشتی مامور تهیه کردن آب مقدس") / ۳۲۹
=== IEC magh
10257:má$- (3) ‘big. Cf. meg-. WP II, 257 (Evi- dence ambig.) (Av. maz- may be fr. a type *mágh- in view of Skt. mah, etc); Tokh. AB māk ‘much’; Phryg. cf. mazeús; Alb. i madh, f: e madhe ‘big’; Lat. cf. magis (more, adv.); Osc. mais, id.; Lat. cf. macte esto! (“let him be extolled' or sim. whence mactare, v.; perh. also Maia *goddess, the mother of Mercury, hence maius “month of May); OIr. maige, cpds. mag-, adj. (great; Ir. maighe, cpds. magh-, id. beside Ir. méid, mf. ‘quantity’, fr. *magita or sim.); W (uncertainly) maw “expanding. Cf. mágh- (1)
16370:smag- (smago, io) (1) ‘huri, dash, strike’. WP II, 685. (Li. ambig. cf. smagh-) Lat. cf. mactus, adj. (struck; MIr. cf. (?) smacht, m. ‘discipline’; W cf. moi, inf. (“throw out, if for *mawi, cf. maedd-, m. ‘knock’ fr. *smagdo- & mas, f. 'swoon': G schmach- ten, if fr. *smagst-); WG schmacken, v. ‘cast, fling away; Du. smakken, tr. ‘dash, bang, fling’; E smack, s. & v.; LG smacken, wd:
16373:smag- (smagó, ið) (2) ‘fondile’. (Li. ambig. cf. smagh-). WP II, 692 ' Gk. mássó, v. (touch, handle, feel, knead’ beside magís, f. ‘kneaded lump’ and mageus, m. “kneader; wiper; OE smacian, v. ‘coax, flatter’; Li. smagüs, adj. (1) ‘pleasant’
16376:smaghos, à ‘toil, turmoil". (Celt. and Li. am- big. Gk. also, but Bois. untenable) Gk. mákhe, f. ‘battle (a type *mnghå: *mongh-:G Hand-gemenge seems improb- able); cf. mákhlos, adj. ‘fierce; lewd’; Ir. am- big. smag, m. ‘slap’, smaig, f. “discipline” appear to be Eng. LWs, since no vb. occurs); W cf. maon, pl. ‘crowd, surge’; Li. (ambig.) smagus, adj. “sharp, strong, smart’; MHG cf. smaht, sm. (2) ‘faintness’; G schmachten, v. ‘faint’ and perh. Lat. maereo, ere, v. ((mourn', if for *smagher-)
16426:smogos, us ‘toilsome; toil’. Cf. smagh-. (Balt. ambig.). WP II, 692 Gk. mógos, m. “effort; toil; sorrow'; cf. moge- rós & smogerós, adj. ‘laborious’; mógis, adv. “with difficulty’; mogéo, v. ‘toil’; Li. (Zemaité) cf. smagüs, adj. “heavy, difficult’; Latv. smags, id.
=== SYN able/power magh
22513:W. maith, MW meith fr. *mag-tio : Ir. Cas mag- in mag-lorg = mor-lorg ‘big club’, uN magh-slaibh ‘big mountain’, OW digour- ul mechis ‘added’ (?), Ir. do-for-maig ‘in- tio creases’, etc., prob. fr. the root in Lat. We magnus ‘large’, Grk. péyas, etc. Loth, | RC 40.342 f. Walde-P. 2.258 (without in) W. maith). fr
```


## [2026-09-07T15:55:20.981Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '14837,14884p' incoming/WLD/WLD_Bd2_pages.txt",
 "description": "Read Walde-Pokorny magh entry"
}
```


### [2026-09-07T15:55:21.024Z] TOOL RESULT

```
magh- magh- „k6nnen, vermogen, helfen“.
          :




   Gr,               dor. jady^og „Hilfsmittel“,                     dor. juayavd „Hilfsmittel
List;    Werkzeug; Mittel, etvvas zu erlangen“;
   got. fnag (Inf.     magan, Praet. ynahta) „vermag, kann'',                 aisl.   ma (Inf. mega;
vermag nicht idg. e-Yokalismus zu stiitzen, Meillet Msl. 14, 335), ahd. mag
Unagan), as. mag (nitigan), ags. mceg ds.
   aisl. magn, megin „Kraft, Macht“, ags. mcegcn, as. megin, ahd. magan.

megin ds.: got. mahts „Kraft, Macht“, ahd. as. maid, ags. meaht, might,
aisl. mdttr ds.;

   abg. mogq^ most! „konnen, vermogen'', pomosti, iter, pomagati „helfen“
usw., abg. mosth, russ. moch usw\ ,,Macht, Starke" (== got. maids).      Ent-
lehnung der slav. Sippe aus der germ. (Hirt PBrB. 23, 335, Wiedemann
BB. 28, 63, Uhlenbeck PBrB. 30, 300) widerlegt durch Trautmann KZ. 46,
180fiF. (s. auch Berneker II 67 f., 70), der aus der alten Opt.-Form skr.-ksl.

7noz^ „potes", skr. moz, tech. alt.     ,,
                                           potest" got. mageis, magi ein altes
                                                                :




unthem. Praes. "^magli-mi ^mogh-me. Opt. "^nidgh-iem usw^ erschlieBt. Nach
                                  ;


Trubeckoj (Slavia I 14ff.) ware die slav. Form Umbildung eines alten Praet.
  Lehnworte sind (nach Briickner AfslPh. 20, 490)     apr. massi „kann" (aus
poln. moze\   muslngin Acc. „moglich" (umgebildet aus poln. moznij\ lit.
pamagoti „helfen", magoti „nutzen, taugen" (aus dem Slav.).
   Ygl. Osthoff PBrB. 15, 21 Iff., Fickl^ 104, 279, 508 (hier, wie II^ 197,
mit Unzugehorigem, bes. der Sippe ^^megili)- grofi" s. d.), usw.
   Die germ. Sippe trotz \Yiedemann aaO. (auch Collitz Schwach. Praet. 39,
der sich auf das Praet. mahta beruft, das aber nach Sverdrup lA. 35, 8
fiir "^magda stehn kann) nicht zu gr. p.ay.o6g. pfjxog (Wz. mafc- „lang und

diinn"), was auch Entl. der si. Sippe aus dem Germ, zur Yoraussetzung
hatte.
```


## [2026-09-07T15:55:22.371Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"mágh- (1)\" IEC.txt | head -5; echo \"---\"; grep -n \"^mágh-\\|mágh- (1)\\|mághos\" IEC.txt | head -10",
 "description": "Mann magh entry"
}
```


### [2026-09-07T15:55:22.432Z] TOOL RESULT

```
10243:mágh- (1) ‘charm, delight Gk. cf. mákhlos "ustfül'; ON magna, v. ‘charm’; Li. magüs ‘charming, pleasant; magü, éti, v. «allure, attract; impers. w. dat. ‘want, be keen on’; long-gde in W maw "er pansive, indulgent; Du. meug. f. ‘liking’, w. vowel-fronting; Li. mogis, gs -io, m. “delight'. (Isophonic: Ir. magaim, v. *mock")
10257:má$- (3) ‘big. Cf. meg-. WP II, 257 (Evi- dence ambig.) (Av. maz- may be fr. a type *mágh- in view of Skt. mah, etc); Tokh. AB māk ‘much’; Phryg. cf. mazeús; Alb. i madh, f: e madhe ‘big’; Lat. cf. magis (more, adv.); Osc. mais, id.; Lat. cf. macte esto! (“let him be extolled' or sim. whence mactare, v.; perh. also Maia *goddess, the mother of Mercury, hence maius “month of May); OIr. maige, cpds. mag-, adj. (great; Ir. maighe, cpds. magh-, id. beside Ir. méid, mf. ‘quantity’, fr. *magita or sim.); W (uncertainly) maw “expanding. Cf. mágh- (1)
---
10243:mágh- (1) ‘charm, delight Gk. cf. mákhlos "ustfül'; ON magna, v. ‘charm’; Li. magüs ‘charming, pleasant; magü, éti, v. «allure, attract; impers. w. dat. ‘want, be keen on’; long-gde in W maw "er pansive, indulgent; Du. meug. f. ‘liking’, w. vowel-fronting; Li. mogis, gs -io, m. “delight'. (Isophonic: Ir. magaim, v. *mock")
10248:mágh- — māk-
10257:má$- (3) ‘big. Cf. meg-. WP II, 257 (Evi- dence ambig.) (Av. maz- may be fr. a type *mágh- in view of Skt. mah, etc); Tokh. AB māk ‘much’; Phryg. cf. mazeús; Alb. i madh, f: e madhe ‘big’; Lat. cf. magis (more, adv.); Osc. mais, id.; Lat. cf. macte esto! (“let him be extolled' or sim. whence mactare, v.; perh. also Maia *goddess, the mother of Mercury, hence maius “month of May); OIr. maige, cpds. mag-, adj. (great; Ir. maighe, cpds. magh-, id. beside Ir. méid, mf. ‘quantity’, fr. *magita or sim.); W (uncertainly) maw “expanding. Cf. mágh- (1)
```


## [2026-09-07T15:55:34.587Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"mégh-\\|mogh-\\|‘be able\\|'be able\" IEC.txt | head -20",
 "description": "Mann be able root"
}
```


### [2026-09-07T15:55:34.633Z] TOOL RESULT

```
10245:maghido, ið (maghdið) “beat, pound, crush? OW, W maeddu, v. ‘pound, buffet’; OCz. mož- diti, inf. ‘pound, crush’; R možžù, moZZit, id. (OCS po-mozdati ‘weaken’ seems to be related to Gk. mokhthéo ‘toil, suffer’. Cf. mogh- and derivatives)
10482:meih- (variant: mégh-) ‘urinate; urine’. Cf. moigh-, mih-. WP II, 245 Skt. méhàmi, id.; Oss. mizín, pp: míst, id.; Arm. cf. mizem, id. (LW?); Gk. cf. omeíkho, id.; Lat. méio, ére, supine: mictum, id.: OE migan, sv. 1., Fris. mige, ON míga, id.; cf. OFris. mese, s. (urine', fr. *moighs-); Srb. miam, id.; Li. meZu, pf. myZau, inf. myZti,
10984:mogh- (radical element of the following en- tries) “large, powerful, heavy”, etc. (The Skt. forms are ambig. in view of Iranian equivalents of type *maz-). Cf. maháh “big, strong’; compar. mahiyas, superl. mahistha, but cf. Vedic maham, n. ‘great deed, exploit’: Av mayom, n. ‘greatness’, and Skt. mahán, n. ‘greatness: OE mægen, n. ‘strength; feat; force’; Skt. máhas, n. ‘greatness, glory’; ma- hát, pres. pt. ‘strong; great: Olr. mochta ‘mighty’; Go. mahts, etc The velar is explicit in Skt. maghám, n. ‘reward, bounty; OHG mag ‘I can, may’, and OCS mogọ, id. Cf. also OCS moštij ‘worse’. (Speculations on Go. mais, maiza ‘more’; OHG mēro, ON meiri, id. in SF: VWGS: mais)
10998:moghnos (moghinos), om strong, big; strength, size, ability’. WP II, 227 Skt. cf. mahán, n. greatness’. See note on mogh- above); cf. magháh “wealth, power: Av. mayom, n. ‘greatness’; Gk. cf. mos-sün, & -sünos, m. ('tower, scaffold, erection’, if fr. *mogh-dün-, see dünos); OLat. cf. moene, n. "wall: Lt. moenia, npl. ‘city walls; Olr. maigne, adj. ‘mighty’ beside MIr. mog, mogh, adj. ‘big; Cor. men ‘strong, able; OHG ma- gan, n. ‘strength, virtue’; OE mægen ‘might, prowess’; ON megn, adj. ‘strong’; magn, n. as OHG & OE (cf. Eng. “might and main"); OCS cf. moZenije, n. “power? beside R (and com. Sl.) moZnyj “possible?
11000:moghó, moghmi “am able, can’. WP II, 227. Cf. radical: mogh- above Skt. cf. magháh *wealth, power'; Av. mayom, n. ‘greatness, feat; MIr. mog, mogh, adj. ‘big’; Ir. mogh, id. and m. ‘size’; OE maga, w. adj. ‘powerful, able, rich? beside defective vb. mæg; Go. OHG mag ʻI can, may’; OCS (and com. Sl.) mogọ ‘I can’; cf. ne-mogy, adj. ‘im- possible’; R cf. pod-moga, f. ‘sustenance’
11002:moghtis ‘power’. See moghət- and radical mogh-. WP II, 227 Olr. cf. mochta, mogda, adj. ‘mighty’; Ir. mocht, adj. ‘big, bulky’; Gaul. cf. mogeti- (in names); W cf. cy-foeth, pl. au, m. ‘wealth’; Cor. ké-voth, pl. -ow ‘power; wealth’; cf. OCor. ce-fuidoc, adj. ‘mighty’; Go. mahts, f. ‘might, power’; OHG maht, gp mahtio, mehtio, f. id.; ON máttr, m., meht, f. id. (ON makt, f. id. is a LW fr. LG); OCS mosti, f., Cz. moc, f. id.; and com. SL: Finn. LW mahti, id. (Iso- phones: W moeth, pl. au, m. ‘delicacy’; moes, pl. au, f. ‘good manners’, fr. *moghts or *maghts (*mokts, *makts); OW “custom: OCS mošti, fpl. ‘corpse’; Ukr. mošči “relics')
11126:monoghos (for **mo-mogh-?) *much, many, frequent. WP II, 268 Go. manags, OHG manag, manig, menig, OE manig, LG mànnig, Du. menig, G. dial. manch
11401:münió (mün-) Gk. cf. a-múnd “protect, fend off; Ir. máinim, v. “teach; show; advise; MHG münen, wv ‘protect’. (Lat. münio, ire is apparently fr. a type moenio, ultimately *moghnio? See mogh- and cpds.)
13532:pro-ag- (by crasis: próg-, prag-), cf. pro-, ago Per. far-àz, adj. *exalted"; far-azam, v. ‘erect’; Oss. (Graz, s. ‘means, facility’; fárazun, inf. ‘be able’; Arm. ar-ac, i-st. s. “proverb, precept’; Gk. prágos, n. “deed, act; Alb. prodh, m. ‘boon’; prodhë, f. ‘produce, product"; OHG fruohhan, adj. ‘bold’; OS cf. frokno *boldly'; ON froekn, adj. ‘bold’; OCS prazü, m. "breed. ing male animal” beside prozü, prp. ‘through’. Verbal types (pro-ag0, pro0, etc.) cf. Skt. pra- ajakah, m. ‘carter’; Av. paraze(imi), v. “bring along”; Per. farazam ‘erect’; Arm. ar-acem, v. ‘tend animals, graze’; Gk. proágo "drive on, lead on? beside prásso, présso (do, act’, if for *pragio) cf. prágos, eos, n. ‘deed, act’; (W rhoi ‘put, give’ is regarded by JMJ:WQG 1913 as a form of W rhoddi fr. *pro-de-, -dhe- or sim.); cf. E fraught, adj. & freight, s.: G Fracht, fr. a type *pro-aKt- > *pràkt- (: Gk. praktós, práksis, préksis, but Gk. -kh- in the pf. péprakha, péprēkha unexplained)
17003:sphéio ‘thrive, grow fat’. Cf. spotís, sphelos, spheros (2). WP II, 656 Skt. sphaye, mp. id.; Hitt. spiyami & spày-, v. ‘sate oneself; Gk. cf. sphelós, adj. (vigo- rous’: OCS spélü ‘mature’: Cz. do-spély *adult) (Hes.); OCS spéjo, -ati, v. “further, prosper’; — se ‘thrive’; Li. spēju, su-speju, inf. speti, -spëti “have time; mature; succeed'; Latv. spēju, spēt, v. ‘be able’; spēja, f. ‘power, ability’; spējš, adj. “sudden
19476:(tuok-, tuðkeio, tuokio, possible variant of type tök- (2) “be strong’, in Gk. sokéo, v. ‘be able, hold sway’; sókos, adj. ‘stout, strong’; Li. tuokiü, tuókti, v. (2) "be adept', usu. nu-? in this sense)
19757:uär- (3) “strength, force, violence; strong man, champion'. Gk. forms ambig. . Gk. cf. Arés, gs: eps, m. “Mars? beside arë, f. (violence'. Ambig.); cf. also aré-go, v. ‘help’ (if fr. aré + ágo); Gk. (cpd?) Héros, Doric -à-, m. ‘hero’; W gwawr, m. id.; Illyrian (Lat.) cf. Varro, onis, m. ‘robber’; ME warr(e) ‘war’; Du. war, f. ‘confusion’; cf. G Wirr-warr, id.; (LW in Fr. guerre); R vor, m. ‘thief; Li. vara, f. “force, violence’; varu, adv. “by force’; Latv. vara, f. ‘force’; varu, ét, v. ‘be able’; varen, adv. 'mightlily very’; varonis, m. (hero'. Lat. baro, onis is said to be a variant of type varo, m. (1) ‘fool’; (2) *mercenary?)
```


## [2026-09-07T15:55:36.547Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SYN power/able section\"; grep -n \"Grk. μηχανή\\|mekhane\\|machina\" SYN.txt | head -10\necho \"=== HJB mangonel\"; grep -n -i \"mangonel\\|manjaniq\" HJB.txt | head -5\necho \"=== WEB mangonel/machine\"; grep -n -i \"mangonel\" WEB_vol1.txt | head -5",
 "description": "Buck, Hobson-Jobson, Webster"
}
```


### [2026-09-07T15:55:36.634Z] TOOL RESULT

```
=== SYN power/able section
9205:3. It. macinare, Rum. mdcina, fr. VLat. *machindre a new denom. of Lat. machina ‘machine’, with specialization to ‘grind’. REW 5206.
=== HJB mangonel
9644:European  {Madras  GUm.  s.v.).  St. Thomafi's  Mount  is  called  in  Tarn. Parangi  Malai,  from  the  ori^al Portuguese  settlement!  Piringi  is  in TcL = *  cannon,'  (C.  B.  P.X  just  as  in  the medieval  Mahommedan  historians  we find  certain  mangonels  for  sie«;es  called vnaghribi  or  *  Westerns.*  [And  so Farluingi  or  Phirangt  is  used  for  the straight  cut  and  thrust  swords  intro- duce by  the  Portuguese  into  India,  or made  there  in  imitation  of  the  foreign weapon  {Sir  W.  EUioty  Ind.  Antiq,  xv. 30)1  And  it  ma^  be  added  that Baber,  in  describing  the  battle  of P&nipat  (1526)  calls  his  artillery Faran^ha  (see  Aviob,  by  Leyden  and Erskine,  p.  306,  note.  See  also  paper by  Gen.  II.  Maclagan,  R.E.,  on  early Asiatic  fire- weapons,  in  J.A.S.  Beng. xlv.  Pt.  i.  pp.  66-67X
=== WEB mangonel/machine
112366:man/ga-bey, n. [from Mangabey car.] any of several species of | keys of the genus Cercocebus, h longer than the body. i mañ’'găn, n. same as mangonel, mañ’gå-nāte, n. |manganic and -ate.] a salt of K- NaO acid; as, potassium manganale, | man-ga-nése’, n. [Fr. manganèse; It. m i nese; by metathesis from ML. magnetai grayish-white metallic chemical slets R | usually hard and brittle, which rusts like ae but is not magnetic: it is used in the mani facture of alloys of iron, aluminum, and con per: symbol, Mn; atomic weight 54 93; atomic number, 25. Nese i manganese bronze; a compound of zine, cop- per, and a small percentage of manganese. manganese Spar; rhodonite. : _manganese Steel; a hard, malleable and duc- tile steel containing 12 to 14 per cent of man- ganese, f mañ-gå-nē’siăn, a. pertaining to manganese; consisting of manganese or partaking of its qualities, mañ- gå-nē’sious (-shus), a. manganous. man-ga-net/ic, a. same as manganiferous. mafi-gan/ic, a. [manganese and -ic.] | 1. designating or of chemical compoundsin i which manganese has a higher valence than in the corresponding manganous compounds. 2. designating or of an acid, H2MnO,, ex- isting only as salts, the manganates, mañ-gå-nif’ēr-ous, a. [maganese, and L. ferre, to bear.] bearing manganese: said of ores. mañ’gå-nin, 2. [manganese and -in.] an alloy consisting mainly of copper with some man- ganese and nickel: it is used in electrical heat- ing elements, rheostats, etc. 3 man/ga-nite, n. 1. hydrous manganese triox- ide, Mn.Os-H:0, a steel-gray or black, crys- talline mineral with a metallic luster. 3 2. any of a series of salts that may be one sidered as derivatives of manganous acid, hydroxide of tetravalent manganese. man-¢a/ni-um, n. manganese. [Rare.] ed mañ: gan’ō-:sīte, 7. a mineral protoxi manganese. ig- maii/ga-nous, a. [manganese and an] d nating or ot chemical compoun iS in Cor manganese has a lower valence na responding manganic compoun Soa eating: mange, 7.[OFr. mangent, Mangue, eof various from L. manducare, to chew.] any and occas skin diseases of domestic animas, sionally of man, especially one parasitic mite and characterize hair. om man/sgel-war’zel, n. [G., corrupted fr goldwurzel, beet root, mango os zel, a root.] in botany, a E Beta vulgaris, cultivated and u
112394:eaten when ripe, or preserved or pickled when unripe. s 2. the tree that it grows on. 3. pickled muskmelon or cucumber. maini’go bird, the yellow oriole, Oriolus kun- doo, found in India. : maii’go fish, a fish, the tupsee of India. mafi/gold-wur’zel, n. same as mangel-wurzel. mafi/go-nel, n. [OFr. mangonel, from LL. man- gonellus, a mangonel.] a military apparatus formerly used for throwing stones, etc. mafi’/g0-stan, n. same as mangosteen. mafi/go-steen, n. [Malay mangustan.| a tree, pane mangostana, of the tropics; also, its ruit. wild mangosteen; a closely-branched tree, Disopyros embryopteris,-of the East Indies, mañ’go tree, the tree, Mangifera indica, bear- Ing the mango. man/grove, n. [from Port. mangue or Sp. man- gle, from the W. Ind. name.] any of a group of tropical trees or shrubs growing in swampy ground along river banks, with branches that spread and send down roots, thus forming more trunks and causing a thick growth. man’grove hen, the salt-water marsh hen, ae allus longirostris, of the West Indies. an rove sna "pér, a fish, Rhomboplites au- ne ens: called also bastard snapper. pe dea n. [Fr., from native name.] a car- SN roue animal of Africa related to the civ- P AS e Crossarchus obscurus.
```


## [2026-09-07T15:55:47.720Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nmkdir -p data/verification/sources/refs/ocr/BOOK\ncp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg318.png data/verification/sources/refs/ocr/BOOK/318.png\nls -la data/verification/sources/refs/ocr/BOOK/ | head",
 "description": "Copy page PNG for audit"
}
```


### [2026-09-07T15:55:49.255Z] TOOL RESULT

```
total 14276
drwxrwxr-x  2 sfmqrb sfmqrb   4096 Sep  7 11:55 .
drwxrwxr-x 12 sfmqrb sfmqrb   4096 Sep  6 18:36 ..
-rw-rw-r--  1 sfmqrb sfmqrb  71589 Sep  5 10:46 100.png
-rw-rw-r--  1 sfmqrb sfmqrb 104864 Sep  4 19:03 101.png
-rw-rw-r--  1 sfmqrb sfmqrb  68145 Sep  5 10:49 102.png
-rw-rw-r--  1 sfmqrb sfmqrb  79623 Sep  5 10:55 103.png
-rw-rw-r--  1 sfmqrb sfmqrb  78826 Sep  5 10:59 104.png
-rw-rw-r--  1 sfmqrb sfmqrb  82500 Sep  5 11:05 105.png
-rw-rw-r--  1 sfmqrb sfmqrb  55270 Sep  5 11:03 106.png
```


## [2026-09-07T15:55:49.535Z] TOOL CALL #61: WebFetch

```json
{
 "url": "https://www.ahdictionary.com/word/indoeurop.html",
 "prompt": "Find the entry for the root magh-1 or megh- \"to be able, have power\". Quote it, including the derivatives (Germanic magan/may, mahti/might, magin/main; Greek mekhane/machine, mechanic; Old Persian magus, magi, magic)."
}
```


### [2026-09-07T15:55:55.469Z] TOOL RESULT

```
I apologize, but I cannot find an entry for "magh-1" or "megh-" in the provided web page content. The document shows Indo-European roots entries from "ad-" through "bheuə-", but does not include entries beginning with "m". The root you're seeking would appear later in the alphabetical listing (the page indicates there are sections for M through Y that are not included in the text provided).

To locate this entry, you would need to access the full dictionary appendix or navigate to the "M" section of the Indo-European Roots listing.
```


## [2026-09-07T15:56:35.954Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg318hi.png'); w,h=im.size\nc=im.crop((int(w*0.17),int(h*0.115),int(w*0.45),int(h*0.30)))\nc.save('arrows.png'); print(c.size)\n\"",
 "description": "Crop arrow region"
}
```


### [2026-09-07T15:56:37.423Z] TOOL RESULT

```
(952, 814)
```


## [2026-09-07T15:56:39.703Z] TOOL CALL #63: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/arrows.png"
}
```


### [2026-09-07T15:56:39.720Z] TOOL RESULT

```

```


## [2026-09-07T15:57:10.593Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('FSF_pages.txt',encoding='utf-8',errors='replace')\nn=0\nfor i,line in enumerate(t,1):\n    n+=line.count('\\f')\n    if i==20604:\n        print('FSF leaf (0-based ff count) at line 20604:', n); break\nEOF\necho \"=== AFM variants\"; grep -n \"جنيق\\|جنيك\\|جنيق\" AFM.txt AFM_pages.txt | head -10\necho \"=== AFM leaf 172 (164+8)\"; awk 'BEGIN{RS=\"\\f\"} NR==172' AFM_pages.txt | head -30",
 "description": "FSF leaf and AFM page 164"
}
```


### [2026-09-07T15:57:12.105Z] TOOL RESULT

```
FSF leaf (0-based ff count) at line 20604: 421
=== AFM variants
=== AFM leaf 172 (164+8)
زرده ^
زركون ܩ
زراكش 7
زرناب 2
زرنايه م7
ܚܐ ܐܤ
زرنبوك ما
زرنه 1
زرلى ܚܣ
زره بان
7 ل“
ررين 7+4
ܝܚܣ ܢܢ
رغس ܪ«
١١ % 9:‏
زكاره ܀ ( |
زلال ܩܣ
زلميا ܣ
,ܕܚ ܣܝ هم
زمزم هلا
زمبر ير .هلا
رن ١م‏
زنانه ܙ ^
زنس ܘܙ
7 ܣ
3 ܣ
زيل »م
زنياره ولا و١١٠١‏
زنبيله ١م‏
زنتاب 5ه
```


## [2026-09-07T15:57:17.496Z] TOOL CALL #65: Bash

```json
{
 "command": "timeout 300 python3 tools/ref_page.py AFM:164 2>&1 | head -50",
 "description": "Fetch AFM page 164"
}
```


### [2026-09-07T15:57:18.890Z] TOOL RESULT

```
no scan of AFM covers printed page 164 (see 'scans' in refs_online.json)
```


## [2026-09-07T15:57:27.322Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('AFM_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves:',len(pages))\n# find any leaf containing 'منج'\nfor i,p in enumerate(pages):\n    if 'منج' in p or 'مجنن' in p:\n        print('hit leaf',i, p[:200].replace('\\n',' '))\nEOF",
 "description": "Search AFM leaves for منج"
}
```


### [2026-09-07T15:57:28.619Z] TOOL RESULT

```
leaves: 198
hit leaf 91 ܚܝ ܀ ¶ ܚܚ # ١ل‏ ܝܢ ورم في حسجاب الدماغ تحدث عنه 3 مركب من 919 50 وم :ܨ اي ورم ومنة ܨܥ ` ܣܪܣܤܣܡܐ ܨ 11 22 ال سي £ 0:09393 باسره ٠‏ قال الاب لامنس اليسوعي في كتاب الفروق: «انة مأخوذ ܟ اليونالي 6 :ܙ وهو ا
```


## [2026-09-07T15:57:38.863Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('AFM_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in range(100,150):\n    p=t[i]\n    import re\n    hs=re.findall(r'\\(\\s*([^\\)\\n]{2,20})\\s*\\)',p)\n    hs=[h for h in hs if any(c in 'ابتثجحخدذرزسشصضطظعغفقكلمنهوي' for c in h)]\n    if hs: print(i, hs[:6])\nEOF",
 "description": "Find AFM leaf with م headwords"
}
```


### [2026-09-07T15:57:40.330Z] TOOL RESULT

```
100 ['الغاذّروان ', 'شرجع', 'الشيراز', 'الشيرازة', 'الكراز', 'الشركلت ']
101 ['الشأ ركاه ', 'التّري', 'الكية', 'لش ', 'الشِشْنة', 'الخَطْء ']
102 ['المَفَلّم', 'الثأفا نج ', 'الشتن', 'حيط الحيط ', 'الثآقول', 'يط الحيط']
103 ['الشأءؤي »', 'حيط المعيظ ', 'الدُسَكرَان', 'الشك ', 'لدجم والسلجم ', 'الشلّنت']
104 ['الكثار', 'البيهان القاطع ', 'الشنآن', 'الشهارة 13 والشتهيرة', 'الكهدر', 'الشهدارة ']
105 ['الشهرة', 'الشهل ', 'الشأهنشاه ', 'الشأهين ']
106 ['الشويند ', 'الشّوّاظ ', 'الشّولة ', 'الشأشكان', 'شاه بأُوط ', 'الشورنيذ والشهني']
107 ['الشِيطرَج ', '3الغاف ', 'م 25م ', '@ : الثمر ', 'راجع فرتكل : \\ \\ ¥ ']
108 ['الصنّة ', 'الصَت ', 'الصخن ', 'الصاخرة', 'القد ', 'الصاروج']
109 ['صئْجة ', 'الصفدَل']
110 ['الصيدانة ', 'الصيف', 'الصُؤْبآن', 'الضبطر | 98 ', 'الصَتَغْطرى ']
111 ['الضغر', 'الصفرس', 'الصَنْك', 'الصَيْطر والضصّوطر ', 'الطأة']
112 ['الطبرد ارب ', 'الطدس ', 'الطارق ', 'الطنتدر', 'الطأناهجة ', 'الطريآال']
113 ['الطرخون ', 'الطرزرأن', 'الطرَازِدان ', 'وطرمش ܕ', 'الطارمة ', 'الطِرممدَار']
114 ['ܐܨ والطأسك', 'الطأق ', 'الطواق ', 'الطبور ܕ ]ܙ ', 'حيط المحمط ', 'الطِنْفْسَة ']
115 ['١\u200f والطِنْوٌ', 'الطأل ', 'الطوة ', 'الطيعأوى ', 'العدسر', 'العَبْقَرِي ']
116 ['العُصْر', 'العنداوة', 'الشيراء ', 'البرهان القاطع ', 'العَمَاشير']
117 ['التَرقد', 'الغافت', 'الغآر', 'القَوشُ ', 'التَرغاء ']
118 ['التشكر ', 'القن ', 'القادرة', 'الفدرّة ']
119 ['الفرجين ', 'المُرْدُل', 'الفآرس']
120 ['( الفررند ']
121 ['الفأرشريشير']
122 ['النولاذ', 'الفلفل ', '١(\u200f فل ', 'الفنِجَان', 'الفنديرة']
123 ['المْنْك', 'حيط ', 'فأوَانيا', 'الفو', 'الوم ', 'الفوة ']
124 ['ܨ و :ܗܘܬ', 'الفيكجة ', 'القنّة']
125 ['راجع اا ', 'الشَان', '| بج ', 'القَردما ܣ ', 'ܬܐ َّ الغليل ', 'راجع ܐܐ ܗ 9 ']
126 ['القرم', 'حيط المحيط ', 'اي بزد القرمز', 'و1:5١', 'اثعيا 18:1', 'التَرْنْوَة']
127 ['القَمَوَرَة', 'القشنيزة ', 'ܨܐ ص : ܝܐ ', 'القصري', 'القتقص ', 'ܐ المحيبط ']
128 ['القأل', 'القلاط ', 'ايلحم ', 'اللا ', 'القلع ', 'القلة']
129 ['المَلَهان»', 'القليبئع', 'القَمْطَرير', 'القَمَه ', '٠\u200f الشخر3', 'القناخر ']
130 ['المنْد']
131 ['العَندَفيل ', 'القاموسش', 'المهرمآن ', 'الهس ', 'القوش']
132 ['آلكنابة']
133 ['ܬܐܨ والخاصة ', 'الكبكج ', 'حيط الحيط ', 'الكثيراء ']
134 ['الكررّن', 'ألكرس ']
136 ['الك ركاه ', 'الكرويا', 'الكزمازّج ', 'المُمْتِيج ', 'الكشسكول']
137 ['الكاغد', 'ألكف ', 'البيهان القاطع ', 'الكُلاب']
138 ['تكاتان ', 'كير ', 'الكامخ ']
139 ['ألكنك ', 'الكندوج', 'الكنديرة ', 'الكَنْدَرَة', 'أمكندبن ', 'اككْئار']
140 ['آلكوقٍ ']
141 ['كرارة', 'الكارَة', 'خبط الحيط', 'كاش يكوش ', 'ألُولان ']
142 ['البيعان القاطع ', 'اتكال', 'الكلحَة ', 'اللازورد', '١\u200f فرد ܀ \\ ', 'اللَج']
143 ['اللاخشة ', 'اللقّازق ', 'الك ', 'اللادّة ', 'ص : £ \\ ', 'الأور']
144 ['الألي', 'المرونة ', 'المثك', 'الج', 'الأجشون', 'الكّدةِ']
145 ['ܕܙ يون ', 'ننات', 'الرْرَئحوسُ ']
146 ['المرك', 'المزو']
147 ['الأست', 'يط الحيط', '| هد ', 'اللان', 'الأملم', 'النج']
149 ['مضل ', 'لوم ', 'ليَة', 'اقرب الموارد ', '55 المانيدة 7450("']
```


## [2026-09-07T15:57:45.834Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('AFM_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor i in range(149,172):\n    p=t[i]\n    hs=re.findall(r'\\(\\s*([^\\)\\n]{2,20})\\s*\\)',p)\n    print(i, hs[:8])\nEOF",
 "description": "AFM leaves 149-171 headwords"
}
```


### [2026-09-07T15:57:47.358Z] TOOL RESULT

```
149 ['مضل ', 'لوم ', 'ليَة', 'اقرب الموارد ', '55 المانيدة 7450("']
150 ['ص: ܥ ', 'راجع ` لكل :4 ', 'المثاء', 'الا نوب']
151 ['الأنار', 'التبهرج ', '|( ;| ', 'الجر والتخر', 'النخ ']
152 ['الكراز', '|« ', 'حيط المحيط ', 'البرهان القاطع ', 'التأوّرد ', 'شفاء الغليل ', 'التوروز والبيدُوز']
153 ['النرْق', 'شفاء الغذيل ', '| ܕ ', 'الشيسب']
154 ['ܬܐܨ ']
155 ['الشكر ', 'الثلك', 'انرق والنئرقة ', 'مش ']
156 ['التوردجة ', 'التَاوق ', '| ܢܗ ']
157 ['حيط المحبظ ', 'اقرب الموارد ', 'النئبرشت', 'المنّق', 'المازق']
158 ['حيط المحدظ ', 'احرج ', 'الرْد', 'المَرَارجِمْسَان', 'اقرب الموارد ', 'الول ', 'الحليون']
159 ['هما بون ', 'ܐܝܟ ', 'المنْدَاز', '!0:4 ', 'امن ', 'الال ', 'فرنكل ܘܬ ¥ ', 'هوم ']
160 ['| ܙ ', 'الوبر']
161 ['المَارَّج والمَارّق ', 'الإبأرجة', 'الي تدج ', 'اليَرمنآن', 'اليرَنًا', 'التاسمين ']
162 ['يلنجوح ']
163 ['010.050:']
164 []
165 []
166 []
167 []
168 []
169 []
170 []
171 []
```


## [2026-09-07T15:57:53.607Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('AFM_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (147,148,149):\n    print('=== leaf',i)\n    print(t[i][:1500])\nEOF",
 "description": "Dump AFM leaves 147-149"
}
```


### [2026-09-07T15:57:55.209Z] TOOL RESULT

```
=== leaf 147
ܕ 311 تب
( الأست) كامة فارسية اسم للبن ومنة التكردي ,)ܝܝ و ܡܣܬܐ بالسريايّة
الدارحة
(ل) ل قيل فارسي ° ( يط الحيط) والصواب !2 تري
0 المس) النحاس 7
+ ܢ الغلام اسن 85 والوحه 39 00 7 5 امن ܘܟ 0
~ ÷
( !]ܚܝ ) فاسي خض وهو 3 الكف ومنة - بالتركة » 2
0 نوع من اطيب :9 فاسي ܕܫܐ ܐܘ ام ام اللرذان ܠܝ الفرس ]
سمعوا بام جرذان وهي كع صفراء قالوا ܐ جاغوا:« اين موثمان» ( اقرب
ܬܕܐܙܒ) ܕܐܐ ܐ نه
( | هد ) اللقاح 09 وقيل 00 ( 3 .قال في شفاء الغليل 1 `
عق الباذجان معرب
(اللان) 3 مان ܕܬܕ كل عار مانع
(الأملم) دواء ٠‏ وهو ܳܨ ܚܨ ينبت في الهند معرب 11
(النج) منك ك وهو حب اذا أكل < 1 وغير عمَلهُ
1 ܨ ܐܥܘ معرب" ܐܥ وهو ܬܐ )ܒܐ ܐܝܕܒ واضاا
مسه
( | ܐ̈ܫܢܟ ) آلة 2 ܨ 007 ` }1 ܝ اي اناما د
مق ٠‏ وقال ܐ دص :1م 00 0 39
< من 00 وهذه 0 0 ` الواسطة .
ايخ ] ܡܝܓܢܝܩܐ ܐܥ ® ٠و‏ ثممل ان يكون اصل اتكلمة فارسا ` 31
الام مأعذة ع مهنيد يك كا سبى اقول مةئ لك له 001
اساوب ܗ ܐܗܨܢ أو ܚ 5 5 الارتفاع الى فوق وكان
اسم ܬ 06 !]£ ماء £ ويضعون فيه دق 20:03 3 ܢ
2 ان ܣ واحدة فواحدة من الإناء وذلك لا نهم كانوا يطمقون £ الاناء متجتونا
=== leaf 148
< 3:(+ 3 3
يضعون عليه قليلا من اللح ٠‏ فبقدر ما كان يذوب الملح كان الماجنون يخاو ܬܨ تلك
الاحجار الدقيقة الى الخارج
مانيذ ) الجرية: بقيتها مأخوذة من مأرنيده اي 01
+ 0 5144 ܨܢ منش )3 10 الهّة ويوافقفة ܨ 1165
والانتكليزي 11170 ܕܐ ريق 14 اي فكر ونأ ܨ
0 )ܕܐ )381 05 7 موتر اي‎ ١
ܢ‎ 491 3
1 2 ܝ الغنى مأخوذ من معيكار اي دأ به العظمة
1 الخاتم فارسي 59 فعا وقالوا مهرَ
ܫ 0 الور ܟ واصل 1 0 حافظ |
7 0 0 6 90 49577 35 610 والعاؤقة
جان) عد الفرس مركب من 3309 331
06 (3061 ܚܚ اول الشماء 0 نقدم عند ܨ 3 0:3 0-3 بق في ܡ
وهو اليوم السادس عشر من شهر « ܝܢ * وذلك عند نزول ܐܚܨ ا >
للفرس عيدان كبيران ررك 795 56 0 7 5( 5 أن الله
580 فرش فيه 000 9 ܗ يع الأجسام 77 للارواح ܐܨ 105
6 0 الازك واكم م كانوا يترون فيه على جميع الرعايا وال بايا
فيقدمون خم الطعام ܝܢ ب قوم الى 0 11 42 7 ني ذلك اليوم ٠‏
فل كارا لنجاتهم ܦ 4 4 من ظلم ܡܓܢ 31 4:83 01 سئة : ܐ 0
اردشير بن بابك وضع ܝ هذا ܟ .0 رأسه تأجة 31 الذي كان 0750 مثل
الشمس ٠‏ وسن على خلفائه من الملوك ان يعقدوا في ذلك اليوم نفسه التاج على روس
اولادهم ويطلوا أجساءهم بدهن البان٠وكان‏ اأوابذة في المهرجان يدخاون على الماوك
كل ` حاملين 4 ج .ܗܘ ܝܐ 50:4 ܐܝܝ ܐܝܢ والعنب الابيض
1 ܫ 0 في ذلك اليوم من تلك الاثار ودهن 250
00 البان :03 عليه ماء الورد سلم حى م 00 منْ جميع الأوجاع 26
=== leaf 149
د < 35
3010 رةه كامت النساء 3 1011 لعة فيها ܐܠܝ تمر يبب هر رهي
خرزة لوا ` كاون المرجان
ܢ مره
# ( مضل ) 5 5 مركب من مه اي كبير وسالي لي .مسن
1 ܨܝ § البأورة تعريب مما وهو حجر شه 5 وقيل هر ܐܐ تبه
ملو ول يوان فقيه الفرس ܠ المجوس 3:5( وججعة
ܨ
( لوم ) ببى الشبع فارسي تكلموا 4 0:27 ܨ
(ليَة) فشر بشىء من ܇ الأدرية ܣ من ܐܝ اي الخير 1:0 يبه اي
ܝ
( الميبحتج » العنب المطبوخ مركب من تمي )1١(‏ اي <> ومن إبخته اي مطبوخ
وهو عسبل العنب ١‏ كن الاطباء يغلونة مرة ثانية »= والعسل
4 فشحة مجبهة همده 18 رلم اليل قل كلمن انام 1ه
ܨܐܘ واضبطرابه عند السباق٠وقيل‏ هو من الوَدْن لان الل رون فيه «بحبط
الجيط ‏ ܢܘܛ رأبي ان الميدان ܠܚܢ الاصل وهر مركب من ,مي اي الشراب ومن
:0 وهى : الأدوات ܐܛ تاحق الاسماء ܐ¿ على 5 13 £ اول الام
5 3 5 .يشر بون فيه امن ثم اطلتوم على الفسيعة المدء اسان
واعب الخيل ٠‏ وهر مردان بالتركية والكردبة
(( ܨ » الطعام والحوان عليه الطعام ٠‏ قيل ܐܬܐܬ مشتقّة من ܘ ععنى اعطاه
دعي فاعلة ܬܶܢ مفعولة لان الماك ]ܪܬܐ للنامن اي اعطاهم اياها , «وقيل من ماد كيد
اذا تحرك ( اقرب الموارد ) انها | معربة عن ܚܬܪܘ وهو خبز المسميذ با لفارسة 1
܀ لإن صاحب البيت اذا ܐܘ ضيف ܪܟ له من خْبز ܢܒ ܐܰܢ على الموان وأطلقت
5 * بالفارسة على الموان والذي يخدم ( 55 المانيدة 7450("
)١‏ وشرب الفاريي مي 0 0 4 اي سك واامونالي 40¡ أي
1
ܝ
```


## [2026-09-07T15:59:20.347Z] AGENT

Now I'll write the verification file.


## [2026-09-07T16:06:58.353Z] TOOL CALL #70: Bash

```json
{
 "command": "cat > /home/sfmqrb/git/rishe/data/verification/page-318.json <<'JSONEOF'\n{\n  \"pdf_page\": 318,\n  \"book_page\": 288,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-07\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Magh1\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *magʰ- / *megʰ- 'to be able, have power' (derivative *magʰ-ti- 'power')\",\n      \"note\": \"Pokorny IEW 695 f. gives 'magh- : māgh- \\\"können, vermögen, helfen\\\"; magh-ti- \\\"Macht\\\"'; Watkins/AHD lemmatizes it as magh-1 'To be able, have power' with the same page reference ('[Pok. magh- 695.]'). Wiktionary lemmatizes the root as *megʰ- 'to be able' with *magʰ- as a variant. Nourai's language label (Indo-European), the root shape and the gloss 'might, power' are all correct, and every branch he draws off it (Iranian magu-, Greek mēkhanē, Germanic magan/mahti-) is in Pokorny's own entry. The one substantive problem on the page is node #13 (manjanīq), where Nourai's Greek source word is not the one modern scholarship uses; the page's own NOTE already flags the disagreement. Note also two data problems: the printed page draws the Greek magos box (#6) off the Avestan/Old Persian box, but the JSON records parent #0; and the Ferdowsī hemistich is printed نیاید, not نباید.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *magʰ- (در ویکی‌واژه *megʰ-) به معنی «توانستن، توانا بودن» است و مشتق *magʰ-ti- «توان، نیرو» از آن ساخته شده. پوکورنی در صفحهٔ ۶۹۵ کتاب خود آن را «magh- : māgh-، können, vermögen, helfen» آورده و در همان مدخل هم magu- ایرانی و mēkhanē یونانی و magan/mahts ژرمنی را زیر آن نشانده است؛ واتکینز (AHD) نیز با ارجاع به همین صفحه آن را magh-1 «توانا بودن» ثبت کرده است. پس برچسب زبانی، صورت ریشه و معنای «توان، نیرو» که نورایی داده درست است و ادعای اصلی او پذیرفتنی است. تنها گرهِ مسئله‌دار این صفحه «منجنیق» است که ریشه‌شناسی امروزی آن را از μαγγανικόν می‌گیرد نه از μηχανή، و خودِ نورایی هم در یادداشت صفحه به این اختلاف اشاره کرده است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/mag%CA%B0-\",\n        \"https://en.wiktionary.org/wiki/%CE%BC%CE%B7%CF%87%CE%B1%CE%BD%CE%AE\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:695\", \"status\": \"supports\", \"note\": \"POK_02.txt lines 5665-5673 (entry closing with the printed page numeral 696, i.e. it begins on p.695): 'magh- : māgh- ,können, vermögen, helfen'; magh-ti- ,Macht'. Ai. maghá- ,Macht, Kraft, Reichtum, Gabe' ... iran. magu-, apers. magus ,Magier, Zauberer' (daraus gr. μάγος, lat. magus) ... gr. μῆχος n. (dor. μᾶχος) ... μηχανή, dor. μαχανά (> lat. machina) ... got. ags. magan ... got. mahts f. ,Macht, Kraft''. Exactly the root, gloss and branches Nourai draws.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. II 227 (WLD_Bd2_pages.txt lines 14818-14884)\", \"stance\": \"partial\", \"note\": \"Running head 'magh- : magh- 227'; entry 'magh- magh- „können, vermögen, helfen“' with Gk. dor. μᾶχος / μαχανά, Goth. mag / magan, ags. mæg, aisl. magn / megin, ags. mægen, got. mahts / ahd. maht / ags. meaht 'might', OCS mogǫ. Same root and gloss, but the 1927 version lists NO Indic or Iranian material — the 'iran. magu-, apers. magus' line is Pokorny's 1959 addition.\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. magh-1 (AHD_watkins1985.txt line 710)\", \"stance\": \"supports\", \"note\": \"'magh-1. To be able, have power. 1. Germanic *mag- in: a. Old English magan, to be able: MAY ... 2. Germanic suffixed form *mah-ti-, power, in Old English miht: MIGHT. 3. Germanic suffixed form *mag-inam, power, in Old English mægen: MAIN. 4. Suffixed lengthened-grade form *magh-and-, \\\"that which enables,\\\" in Greek (Attic) mēkhanē, (Doric) mākhanā, device: MACHINE, MECHANIC ... 5. Possibly suffixed form *magh-u- in Old Persian magus, member of a priestly caste (< \\\"mighty one\\\"): MAGI, MAGIC, MAGUS. [Pok. magh- 695.]' — Nourai's whole chart in one paragraph.\"},\n        {\"src\": \"IEC\", \"where\": \"Mann, s.v. mogh-, moghó/moghmi, moghtis (IEC.txt lines 10984, 11000, 11002)\", \"stance\": \"partial\", \"note\": \"Mann normalizes the root as 'mogh- (radical element ...) \\\"large, powerful, heavy\\\"' and 'moghó, moghmi \\\"am able, can\\\". WP II, 227' with 'moghtis \\\"power\\\" ... Go. mahts, f. \\\"might, power\\\"'. Same material (he cites WP II 227), but he sets it up under an o-grade lemma and merges it with the *meg- 'big' family.\"},\n        {\"src\": \"SYN\", \"where\": \"Buck (SYN.txt)\", \"stance\": \"silent\", \"note\": \"Buck's synonym lists have no article for 'be able / power' under this root; grep for 'magh-' returns only an unrelated Celtic *mag-tio note (line 22513).\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan / Old Persian\",\n          \"words\": \"magus, maeg, megan,moghu; maguš\",\n          \"verdict\": \"transcription_suspect\",\n          \"derivation\": \"Old Persian maguš (nominative of the u-stem magu-) 'Magian, member of the Median priestly clan' is well attested in the Bīsotūn inscription of Darius I (DB I.36 'I martiya magus āha Gaumāta nāma', and I.44, 46, 50, 54, 64, 66, 101; 4.8), rendered Elam. ma-ku-iš, Akkad. ma-qu-šu; Avestan has the stem only once, in the Younger Avestan compound moγu.tbiš- 'hostile to the Magi' (Y. 65.7) — which is what Nourai's 'moghu' represents. Watkins derives it from a suffixed *magʰ-u- 'the mighty one', hence the placement under this root, though Kent flatly says 'uncertain material on meaning and etymology'. So 'magus/maguš' (OP) and 'moghu' (Av. moγu-) are right. But 'maeg' and 'megan' are NOT Iranian words at all: they are Old English mæg 'I can' (1sg pres. of magan) and magan 'to be able' — the Germanic reflexes that belong in box #10 ('mag, mahti'). The printed page (pdf 318, image saved to data/verification/sources/refs/ocr/BOOK/318.png) shows 'magus, maeg, megan,moghu : Zoroastrian priest' inside the Avestan/Old Persian box, so the JSON is a faithful reading and the misplacement is the book's own: Nourai has spilled two Germanic forms into the Iranian box, where they also acquire the impossible gloss 'Zoroastrian priest'.\",\n          \"derivation_fa\": \"پارسی باستان maguš (حالت فاعلی ستاک u-دار magu-) «مغ، عضو طبقهٔ روحانی ماد» در سنگ‌نوشتهٔ بیستون داریوش بارها آمده است (بند ۳۶ ستون یک: «یک مرد مغ بود، گئومات نام») و صورت ایلامی ma-ku-iš و اکدی ma-qu-šu آن را تأیید می‌کند؛ در اوستا این ستاک تنها یک بار و در ترکیب moγu.tbiš- «دشمن مغان» (یسنا ۶۵/۷) دیده می‌شود که همان «moghu» نورایی است. واتکینز آن را از *magʰ-u- «توانا» می‌گیرد، هرچند کنت ریشه‌شناسی آن را نامعلوم می‌داند. اما دو صورت «maeg» و «megan» به‌هیچ‌روی ایرانی نیستند: اینها انگلیسی کهن mæg «می‌توانم» و magan «توانستن» هستند و جای آنها در جعبهٔ ژرمنی (گرهٔ ۱۰) است. تصویر صفحهٔ چاپی نشان می‌دهد که خودِ کتاب این دو صورت را در جعبهٔ اوستایی/پارسی باستان چاپ کرده، پس خطای چاپی کتاب است نه خطای خوانش اسکن.\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"magus, maeg, megan,moghu : Zoroastrian priest / maguš : magician\",\n          \"correct_form\": \"OP maguš (stem magu-), Av. moγu- (in moγu.tbiš-); the forms maeg and megan are Old English mæg / magan and belong in the Germanic box (#10)\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/mag%CA%B0-\",\n            \"https://en.wiktionary.org/wiki/%D9%85%D8%BA\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:695\", \"status\": \"supports\", \"note\": \"POK_02.txt line 5666: 'iran. magu-, apers. magus ,Magier, Zauberer' (daraus gr. μάγος, lat. magus)' — supports the Iranian words and their being under this root; Pokorny lists no Iranian 'maeg/megan'.\"},\n            {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"AHD_watkins1985.txt line 710, magh-1 §5: 'Possibly suffixed form *magh-u- in Old Persian magus, member of a priestly caste (< \\\"mighty one\\\")'. Watkins hedges with 'Possibly'; and his OE mæg/magan appear in §1-3 under Germanic, not under Iranian.\"},\n            {\"ref\": \"KLN:923\", \"status\": \"supports\", \"note\": \"KLN_1966.txt page marker 923 at line 22539; entry at line 22563: 'Magus, n., one of the Magi; (not cap.) a magician. — L., fr. Gk. μάγος, fr. OPers. magush, \\\"magician\\\", whence also Talmudic Heb. magosh, Aram. amgusha, \\\"magician\\\".' Nourai's gloss 'maguš : magician' is Klein's wording.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"Bartholomae AiW col. 1111 (BRT.txt line 19535)\", \"stance\": \"supports\", \"note\": \"'p. magav- (: j. moγu-) Adj., bezeichnet einen medischen Volksstamm, für den die Priesterwürde vorbehalten war, \\\"magisch, Magier\\\"'; cites Bh. (Bīsotūn) I.36, 14, 4.2 and the accusative 'gaumātam tyam magum'. Gives exactly the OP/Young Avestan pair, and nothing Germanic.\"},\n            {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon s.v. magu- (KNT.txt line 5757)\", \"stance\": \"partial\", \"note\": \"'magu- sb. \\\"Magian\\\", member of the priestly order of Media: Elam. ma-ku-iš, Akk. ma-qu-šu, Gk. Μάγος (§153.1). Uncertain material on meaning and etymology, König, Klotho 4 chap. 12 ... magus nsm. DB 1.36, 44, 46, 64, 66, 101; 4.8; DBb 2. magum asm. DB 1.50, 54, 57, 73; 4.81.' Word and language confirmed; Kent declines to endorse the derivation from *magʰ- 'be able'.\"},\n            {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, glossary s.v. magū (NYB_vol2_glossary.txt line 2373)\", \"stance\": \"supports\", \"note\": \"'OP magu-, nom. magus, whence Syr. lw. mgūsā, Arab. majūs-; Av. only once in the compound (1176) moγu-tbiš- \\\"enemy of the Magi\\\".' Confirms both the OP nominative maguš and the single Avestan attestation.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"magu; magu-pat\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Middle Persian inherits the Old Iranian u-stem directly: the word is written <mgw> and <mgwpt'>, i.e. historically magu, magu-pat, but was actually pronounced mōg (NW) / mow- (SW) by Sasanian times — Nyberg: 'magū [mgw, inscr.], magūk [mgwk], mōg [mwg FrP 13] a Magus, a Magian ... The authentic MIr forms are: 1. NW mōg, whence the Arm. lw. mog, NP mōγ ...; 2. SW mov-. The other forms are archaisms preserved as learned spellings', and 'magu-pat [mgwpt'] chief of the Magi ... the authentic MIr forms are: 1. NW mogpat, Arm. lw. mogpet; 2. SW movpat ...; NP mobad'. MacKenzie normalizes the same graphemes as *moy-mard [mgw-mlt'] 'magus' and *mowbed [mgwpt'] 'Mazdean priest'. magu-pat is a regular Old Iranian bahuvrīhi-type compound magu- 'magus' + pati- 'lord, chief' (Av. paiti-), so literally 'chief of the Magi' — Nourai's gloss 'head priest' is right.\",\n          \"derivation_fa\": \"در فارسی میانه همان ستاک ایرانی باستان به ارث رسیده است و به خطّ پهلوی <mgw> و <mgwpt> نوشته می‌شود، یعنی به‌صورت تاریخی magu و magu-pat؛ اما تلفظ روزگار ساسانی mōg (شمال‌غربی) و mow- (جنوب‌غربی) بوده و نیبرگ همین نگارش‌های کهن را «باستان‌گراییِ حفظ‌شده در املای عالمانه» می‌خواند. مکنزی نیز همین نگاره‌ها را *mowbed [mgwpt] «موبد مزدیسنی» و *mōy-mard [mgw-mlt] «مغ» می‌خواند. magu-pat ترکیبی است از magu «مغ» و pati- ایرانی باستان (اوستایی paiti-) «سرور، سرکرده»، پس معنای «موبدِ بزرگ» که نورایی داده درست است. ادعای نورایی در این گره پذیرفتنی است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D9%85%D9%88%D8%A8%D8%AF\"],\n          \"ref_check\": [\n            {\"ref\": \"MON:4248,4421\", \"status\": \"not_checked\", \"note\": \"Mo'in's Farhang-e Farsi is on disk only as the OCR of a 2-volume reprint (MON_part1/part2.txt) which carries no print pagination, and vajehyab/abadis give entry text without page numbers, so pages 4248 and 4421 of the 6-vol. Amir Kabir edition cannot be located. The substance (MP magu > NP moγ, magupat > mobad) is independently confirmed by Nyberg, MacKenzie, Horn and Hübschmann below.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD p. 57 (PHD.txt line 491; PHD_mackenzie.txt line 3588)\", \"stance\": \"supports\", \"note\": \"'*moy-mard [mgw-mlt', -gBRA | N mug] magus' and '*mowbed [mgwpt' | N mōbad] Mazdean priest' — the Pahlavi graphemes mgw / mgwpt' with the New Persian outcomes.\"},\n            {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, s.vv. magū and magu-pat (NYB_vol2_glossary.txt lines 2373-2374)\", \"stance\": \"supports\", \"note\": \"'magū [mgw, inscr.] ... a Magus, a Magian ... The authentic MIr forms are: 1. NW mōg ... 2. SW mov-. The other forms are archaisms preserved as learned spellings.' / 'magu-pat [mgwpt'] chief of the Magi, or: chief Magian, of the head of the Zoroastrian priesthood ... NP mobad.'\"},\n            {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 984, p. 221 (HRN.txt lines 8553, 8564-8565)\", \"stance\": \"supports\", \"note\": \"'984. muγ, mōγ \\\"Magier, Feueranbeter\\\", mōbed, ap. magu-; aw. -moγu- in moγu.tbiš- ...; phlv. magu, magupat (arm. LW. mog, mogpet, movpetan movpet), daneben maupat' — Horn's chain is Nourai's chain.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"moğ «مُغ»; mobad, mobed «موبد»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP مُغ moγ 'Zoroastrian priest' is the direct continuation of MP mōg (written magu): Old Iranian magu- > MP mōg > NP mōγ/muγ, with the u-stem vowel coloured to ō and the final -u realized as the fricative γ in the Arabic-script spelling; Hübschmann states it flatly — 'für ap. a erscheint mp. o = np. u und ō in muγ = mōγ \\\"Magier\\\" ..., phl. geschrieben magu, gesprochen mōγ, gr. μάγος, ap. magu-'. NP موبد mōbad continues MP mowbed < *magupat < OP *magupatiš 'head of the Magi': the -u- of magu- and the p- of pati- coalesce as mow-, and intervocalic -p- of *-pat- lenites to -b-; Hübschmann's 'mōbad = phl. magupat' and the Syriac loan mwpt'/mwbd' show the same development. In later New Persian poetry مغ drifts to '(Christian) monk' and then 'tavern-keeper, wine-server' (Horn's footnote on Hāfez), while موبد keeps the technical sense. The chart's bracketed «مَغ ۱» is a cross-reference to the first (magus) entry of مغ, as against the homograph مَغ 'hole, deep'.\",\n          \"derivation_fa\": \"«مُغ» ادامهٔ مستقیم فارسی میانهٔ mōg (نگاشتهٔ magu) است: ایرانی باستان magu- > فارسی میانه mōg > فارسی نو مُغ/مۇغ؛ هوبشمان صریح می‌گوید «آنچه در پارسی باستان a است در فارسی میانه o و در فارسی نو u/ō نمایان می‌شود: muγ = mōγ «مغ»؛ در پهلوی magu نوشته و mōγ خوانده می‌شد». «موبد» نیز از فارسی میانهٔ mowbed و آن از *magupat و پارسی باستان *magupatiš «سرِ مغان» است؛ در این تحول -u-ی magu با p-ی pati- به mow- بدل شده و پ در میان دو واکه به ب نرم شده است (قس وام‌واژهٔ سریانی mwbd و ارمنی movpet). در فارسی دری متأخر «مغ» در شعر (به‌ویژه حافظ) به معنی «راهب» و سپس «می‌فروش» هم به کار رفته، اما «موبد» معنای فنی خود را نگه داشته است. عبارت «مَغ ۱» در نمودار ارجاع به مدخل نخست «مغ» است، در برابر همنگارهٔ «مَغ» به معنی «گودی، عمیق». ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%85%D8%BA\",\n            \"https://en.wiktionary.org/wiki/%D9%85%D9%88%D8%A8%D8%AF\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"MON\", \"status\": \"partial\", \"note\": \"No page is given, so nothing specific can be checked; the OCR of Mo'in (MON_part2.txt line 92705 ff.) does carry a هیربد/موبد article — 'پیشوای دینی؛ موبد موبدان. رئیس آتشگاه' with an etymological note breaking a compound into two elements — confirming Mo'in treats mōbad as a Pahlavi compound, but the reference is too vague to verify further.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien pp. ~123 and ~232 (HUB.txt lines 4406-4410, 4292, 8868, 8880)\", \"stance\": \"supports\", \"note\": \"'muγ = mōγ \\\"Magier\\\", arm. mog und (später) mov ..., phl. geschrieben magu, gesprochen mōγ, gr. μάγος, hebr. מג, ap. magu- (davon phl. magupat = arm. mogpet = movpet = syr. mowed = np. mobad)'; also 'mōbad = phl. magupat' and 'ap. magu- \\\"Magier\\\" = phl. mag, np. muγ'; and p. 72 'gesprochen mōypet, ap. *magupati-'.\"},\n            {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 984, p. 221 (HRN.txt lines 8553, 8561, 8564)\", \"stance\": \"supports\", \"note\": \"'muγ, mōγ \\\"Magier, Feueranbeter\\\", mōbed, ap. magu-'; footnote: 'Im späteren Neupersisch ist der Magier zum \\\"(christl.) Mönch\\\" und besonders zum \\\"Kneipwirt, Zecher\\\" geworden (Hāfiẓ häufig), vergl. auch muγbeče, muγān'.\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD p. 57 (PHD.txt line 491)\", \"stance\": \"supports\", \"note\": \"'*mowbed [mgwpt' | N mōbad] Mazdean priest' — MacKenzie himself gives the New Persian outcome mōbad.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Arabic\",\n          \"words\": \"majŭs\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Arabic مَجُوس al-Majūs 'the Magians, Zoroastrians' is a Qur'anic hapax (Q 22:17, a late Medinan verse, where they are listed with Jews, Christians and Sabians); it is a collective with the nisba singular مَجُوسِيّ. The Arab lexicographers themselves knew it was foreign, and Ibn Sīda's folk-etymology from a big-eared man named مج (LA viii.99) is set aside in favour of the Iranian source. Jeffery: 'It is clearly the O.Pers. Magush, with the acc. form of which, magum, we can compare the Av. magav ... and Phlv. ma-γōi'. The one correction to Nourai's arrow is the route: all the sources put an Aramaic/Syriac stage in between rather than a direct Old Iranian → Arabic loan — Nyberg, 'OP magu-, nom. magus, whence Syr. lw. mgūsā, Arab. majūs-'; Jeffery, 'this appears in the Aram. אמגושא, Gk. μάγος, Syr. mgwšā and the מגוש of the Aramaic of the Behistun inscription'; Mo'in tags the Persian entry مجوس as |معر. آرا. مجوشا|, i.e. Arabicized from Aramaic magūšā; al-Unaysi (TAD), 'مجوس - في الآرامية مجوشا'. The -ū- of majūs answers to the Aramaic/Syriac -ū- of magūšā, and Arabic j renders the g of the Aramaic form. Hence plausible rather than confirmed: right ultimate origin, one missing intermediary.\",\n          \"derivation_fa\": \"واژهٔ عربی «مَجوس» (جمع/اسم جمع، مفردِ نسبی «مجوسی») تنها یک بار در قرآن آمده است (حج، آیهٔ ۱۷، از آیات مدنیِ متأخر) و در آن مجوس در کنار یهود و نصارا و صابئان نام برده شده‌اند. لغت‌نویسان عرب خود می‌دانستند که این کلمه بیگانه است و ریشه‌شناسی عامیانهٔ ابن‌سیده (مردی کوچک‌گوش به نام «مج») را کنار گذاشته و آن را از «مگوشِ» پارسی باستان دانسته‌اند؛ جفری نیز می‌گوید «به‌روشنی همان maguš پارسی باستان است». تنها اصلاحی که بر نمودار نورایی وارد است مسیر وام‌گیری است: منابع یکدست میان ایرانی باستان و عربی یک مرحلهٔ آرامی/سریانی می‌گذارند — نیبرگ: «magu- پارسی باستان، حالت فاعلی magus، که وام‌واژهٔ سریانی mgūsā و عربی majūs از آن است»؛ معین نیز در مدخل «مجوس» آن را «معرّبِ آرامیِ مجوشا» می‌داند. واکهٔ کشیدهٔ ū در «مجوس» بازتاب همان ū در magūšā آرامی است و «ج» عربی جانشین g شده است. پس ریشهٔ نهایی درست است اما یک حلقهٔ میانی از نمودار افتاده و ادعای نورایی «با احتیاط پذیرفتنی» است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D9%85%D8%BA\"],\n          \"ref_check\": [\n            {\"ref\": \"VDQ:374\", \"status\": \"partial\", \"note\": \"VDQ (Badreh'i's Persian translation of Jeffery) is only on noorlib in a JavaScript viewer, so p.374 itself could not be opened; per refs_online.json the substance is to be checked in the English original. FVQ pp. 259-260 s.v. المجوس (FVQ.txt lines 16149-16190) says: 'It is clearly the O.Pers. Magush ... Others, however, knew that it was derived from the Iranian Magush (LA, viii, 99) ... In Phlv. we also find a form magōšia, derived directly from the O.Pers., and this appears in the Aram. אמגושא, Gk. μάγος, Syr. mgwšā and the מגוש of the Aramaic of the Behistun inscription.' Supports the origin, adds the Aramaic/Syriac stage Nourai omits.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"FVQ\", \"where\": \"Jeffery, Foreign Vocabulary of the Qur'an pp. 259-260 (FVQ.txt lines 16149-16190)\", \"stance\": \"partial\", \"note\": \"See ref_check: OP maguš is the source, but the transmission runs through Pahlavi magōšia and Aramaic/Syriac; Jeffery also records and rejects Lagarde's derivation of مجوس from Gk. μάγος (GA 159).\"},\n            {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II s.v. magū (NYB_vol2_glossary.txt line 2373)\", \"stance\": \"partial\", \"note\": \"'OP magu-, nom. magus, whence Syr. lw. mgūsā, Arab. majūs-' — same origin, explicit Syriac mediation.\"},\n            {\"src\": \"MON\", \"where\": \"Mo'in, s.v. مجوس (MON_part2.txt line 48692)\", \"stance\": \"partial\", \"note\": \"'مجوس : Magus |معر. آرا. مجوشا| (ص.) فردی از فرقهٔ مجوس. مجوسی' — Mo'in labels it Arabicized from Aramaic مجوشا, not straight from Old Persian.\"},\n            {\"src\": \"TAD\", \"where\": \"al-Unaysi, Tafsir al-alfaz al-dakhila (TAD_pages.txt line 2598)\", \"stance\": \"partial\", \"note\": \"'مجوس - في الآرامية «مجوشا»، وفي اليونانية magos وفي اللاتينية magus' — again Aramaic first.\"},\n            {\"src\": \"ARB\", \"where\": \"al-Jawaliqi, al-Mu'arrab, s.v. مجوس (ARB_mo3rb.txt lines 22619-22623)\", \"stance\": \"supports\", \"note\": \"The Mu'arrab discusses مجوس among the arabized words, quoting al-Qamus' folk etymology ('رجل مصغّر الأذنين وضع دينا') and 'وأصله مِنْج كُوش' — i.e. the classical tradition already treated it as a Persian/Iranian loan.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Persian\",\n          \"words\": \"majŭs «مجوس»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"New Persian مجوس majūs is the Arabic word taken back into Persian — a complete round trip: Old Persian maguš → Aramaic/Syriac magūšā → Arabic majūs (Q 22:17) → New Persian majūs, where it stands beside the inherited native doublet مُغ moγ (node #3) with a narrower, often pejorative or legalistic sense ('Zoroastrian, fire-worshipper, non-Muslim') used in fiqh and in polemic. Mo'in flags the Persian entry with the Arabic-loan tag |معر. آرا. مجوشا| and glosses 'فردی از فرقهٔ مجوس؛ مجوسی', which is exactly Nourai's Arabic → Persian arrow; the pair مغ / مجوس is thus a textbook doublet, one inherited and one borrowed back through Arabic.\",\n          \"derivation_fa\": \"«مجوس» در فارسی نو همان واژهٔ عربی است که به فارسی بازگشته است، یعنی یک دورهٔ کامل وام‌گیری: پارسی باستان maguš ← آرامی/سریانی magūšā ← عربی مجوس (قرآن، حج ۱۷) ← فارسی نو مجوس. این صورت در فارسی در برابر دوگانهٔ بومی و موروثی «مُغ» می‌نشیند، اما معنایی تنگ‌تر و بیشتر فقهی یا جدلی دارد («زردشتی، آتش‌پرست، غیرمسلمان»). معین در مدخل فارسی «مجوس» برچسب |معر. آرا. مجوشا| گذاشته و آن را «فردی از فرقهٔ مجوس» معنی کرده است، و همین درست همان پیکانِ عربی ← فارسی نورایی است. جفتِ «مغ / مجوس» نمونهٔ آشکار دوگانه (doublet) در فارسی است: یکی موروثی و دیگری وام‌گرفته از راه عربی. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D9%85%D8%BA\"],\n          \"ref_check\": [\n            {\"ref\": \"MON:3884\", \"status\": \"partial\", \"note\": \"The print pagination of the 6-vol. Amir Kabir edition is not recoverable from the local OCR, but the entry itself is there: MON_part2.txt line 48692, 'مجوس : Magus |معر. آرا. مجوشا| (ص.) فردی از فرقهٔ مجوس. مجوسی. (ص.) ... مشرک'. Mo'in does derive the Persian word from Arabic (معرّب), as the arrow says.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"Mo'in, s.v. مجوس (MON_part2.txt line 48692)\", \"stance\": \"supports\", \"note\": \"Persian مجوس marked معرّب (Arabicized) from Aramaic مجوشا — an Arabic-mediated loan in Persian, as the chart draws.\"},\n            {\"src\": \"FVQ\", \"where\": \"Jeffery p. 260 (FVQ.txt line 16180)\", \"stance\": \"supports\", \"note\": \"Jeffery cites 'the Mod. Pers. مغ' (Vullers, Lex ii 1197; BQ 863) as the native form alongside the Arabic مجوس, i.e. the two coexist as doublets.\"},\n            {\"src\": \"TAD\", \"where\": \"al-Unaysi (TAD_pages.txt line 2598)\", \"stance\": \"supports\", \"note\": \"Lists مجوس among the words that entered Arabic from outside, with the Aramaic form — the same word Persian re-borrowed.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Greek\",\n          \"words\": \"mağos\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Greek μάγος magos, first in the 5th c. BCE (Herodotus' account of the Median Magi and the false Smerdis, and Aeschylus), is a straight borrowing of Old Persian maguš during the Achaemenid period, with the OP nominative ending -uš remodelled as the Greek o-stem -ος; from it Greek forms μαγικός 'of the Magi, magical' and μαγεία 'magic'. Pokorny states the loan explicitly ('apers. magus ... daraus gr. μάγος, lat. magus'), as do Klein p.923 and Kent's lexicon ('Gk. Μάγος'). Note on the data: the printed page (image at data/verification/sources/refs/ocr/BOOK/318.png) draws this Greek box off the descending stem of the Avestan/Old Persian box, together with Pahlavi (#2) and Arabic (#4) — i.e. its parent in the book is node #1, not the root; the JSON records parent 0, which is an extraction error. Substantively the book's arrow is the correct one.\",\n          \"derivation_fa\": \"یونانی μάγος (magos) نخست در سدهٔ پنجم پیش از میلاد دیده می‌شود (هرودوت در گزارش مغانِ ماد و ماجرای بردیای دروغین، و آیسخولوس) و وام‌واژهٔ مستقیمی است از maguš پارسی باستان در دورهٔ هخامنشی؛ پایانهٔ فاعلی -uš پارسی باستان در یونانی به ستاک o-دار (-ος) بازسازی شده است و از همین صورت μαγικός «مغانه، جادویی» و μαγεία «جادو» ساخته شده. پوکورنی این وام‌گیری را صریح می‌گوید («apers. magus ... daraus gr. μάγος، lat. magus») و کلاین و کنت نیز همین را تأیید می‌کنند. ادعای نورایی درست است. یک نکتهٔ فنی: در صفحهٔ چاپی این جعبهٔ یونانی از ساقهٔ جعبهٔ اوستایی/پارسی باستان منشعب می‌شود (همراه پهلوی و عربی)، پس پدرِ آن گرهٔ ۱ است نه ریشه؛ ثبتِ «parent 0» در فایل استخراج‌شده خطای خوانش اسکن است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/mag%CA%B0-\"],\n          \"ref_check\": [\n            {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"The Greek magos box carries no reference of its own; the parent box's POK:695 and KLN:923 cover it ('daraus gr. μάγος'; 'L., fr. Gk. μάγος, fr. OPers. magush').\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"Pokorny IEW p.695 (POK_02.txt line 5666)\", \"stance\": \"supports\", \"note\": \"'iran. magu-, apers. magus ,Magier, Zauberer' (daraus gr. μάγος, lat. magus)'.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein p.923 s.v. Magus (KLN_1966.txt line 22563)\", \"stance\": \"supports\", \"note\": \"'L., fr. Gk. μάγος, fr. OPers. magush, \\\"magician\\\"' — Greek is the intermediary between Old Persian and Latin.\"},\n            {\"src\": \"KNT\", \"where\": \"Kent, Lexicon s.v. magu- (KNT.txt line 5757)\", \"stance\": \"supports\", \"note\": \"Lists 'Gk. Μάγος' among the foreign renderings of OP magu-, beside Elamite ma-ku-iš and Akkadian ma-qu-šu.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Latin\",\n          \"words\": \"magus\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin magus 'a Magian, a magician' (pl. magi) is a learned borrowing of Greek μάγος in the late Republic and early Empire (Cicero, De divinatione; Pliny, NH xxx, on the magorum ars), with the adjective magicus taken from Greek μαγικός; the plural magi became the fixed designation of the wise men of Matthew 2 in the Vulgate, which is what carried the word through Christian Latin into the vernaculars. Pokorny gives 'lat. magus' as taken from Greek in the same breath as the Greek word; Klein s.v. Magus and s.v. mage/magic gives the same Latin link.\",\n          \"derivation_fa\": \"لاتینی magus «مغ، جادوگر» (جمع magi) وام‌واژه‌ای عالمانه از μάγος یونانی است که در اواخر جمهوری و آغاز امپراتوری روم به کار می‌رود (سیسرون در «دربارهٔ غیب‌گویی»، پلینی در «تاریخ طبیعی» دفتر سی‌ام دربارهٔ magorum ars)، و صفتِ magicus نیز از μαγικός یونانی گرفته شده است. جمعِ magi در ترجمهٔ ولگات برای «مغانِ» انجیل متّی (باب ۲) به کار رفت و همین کاربردِ مسیحی بود که واژه را از لاتینِ کلیسایی به زبان‌های اروپایی رساند. پوکورنی خود «lat. magus» را در پیِ μάγος یونانی می‌آورد و کلاین نیز همین زنجیره را ثبت کرده است. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/mag%CA%B0-\"],\n          \"ref_check\": [\n            {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"No reference in this box; covered by the root's POK:695 ('daraus gr. μάγος, lat. magus') and by Klein p.923.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"Pokorny IEW p.695 (POK_02.txt line 5666)\", \"stance\": \"supports\", \"note\": \"'(daraus gr. μάγος, lat. magus)' — Latin from Greek.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein pp.921, 923 (KLN_1966.txt lines 22514, 22518, 22563)\", \"stance\": \"supports\", \"note\": \"'Magi, n. pl., a priestly caste in Media and Persia. — L. magi, pl. of magus'; 'mage, n., a magician. — F., fr. L. magus'; 'Magus ... — L., fr. Gk. μάγος'.\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"French\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Empty pass-through box for the Old/Middle French stage: OF mage 'magus' and, more importantly for the chain drawn here, OF/MF magique (13th c.) 'magic (art)', from Latin magicus / Late Latin magicē. Klein makes both steps explicit ('mage, n., a magician. — F., fr. L. magus'; 'magic, n. — ME. magik, fr. MF. (= F.) magique, fr. Late L. magice'), so the French link Nourai interposes between Latin and English is real and not a filler.\",\n          \"derivation_fa\": \"این جعبه واسطهٔ خالی و نشان‌دهندهٔ مرحلهٔ فرانسهٔ کهن/میانه است: mage «مغ» و مهم‌تر برای این زنجیره magique (سدهٔ سیزدهم) «(هنرِ) جادو»، از magicus لاتینی و magicē لاتینِ متأخر. کلاین هر دو گام را صریح آورده است («mage از فرانسه، از magus لاتینی» و «magic از انگلیسی میانه magik، از magique فرانسهٔ میانه، از magice لاتینِ متأخر»)، پس حلقهٔ فرانسه‌ای که نورایی میان لاتین و انگلیسی گذاشته واقعی است و پُرکنندهٔ جای خالی نیست. ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/mangonel\"],\n          \"ref_check\": [\n            {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"Empty box with no reference; verified from Klein's 'magic' and 'mage' entries (KLN_1966.txt line 22519).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein p.921 s.vv. mage, magic (KLN_1966.txt lines 22514, 22519)\", \"stance\": \"supports\", \"note\": \"'magic, n. — ME. magik, fr. MF. (= F.) magique, fr. Late L. magice, fr. Gk. μαγική (scil. τέχνη), lit. \\\"magic art\\\", fem. of the adjective μαγικός'.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat, s.v. mechanic and neighbouring French-mediated Greek words (SKT.txt line 10869)\", \"stance\": \"supports\", \"note\": \"Skeat routinely marks this class as '(F. — L. — Gk.)', e.g. 'mechanic ... (F. — L. — Gk.) M.E. mechanike ... — O.F. mechanique', i.e. French is the regular intermediary for Greco-Latin learned words entering English.\"}\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"English\",\n          \"words\": \"magic\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English magic: Middle English magik (Chaucer, late 14th c.) from Old/Middle French magique, from Late Latin magicē (ars), from Greek μαγική (τέχνη) 'the art of the Magi', the feminine of μαγικός, from μάγος — so the word is, at four removes, Old Persian maguš. Klein s.v. magic (n. and adj.) gives precisely this chain, and Watkins files MAGIC, MAGI, MAGUS and ARCHIMAGE under magh-1 §5. The semantic route is 'belonging to the Median priestly caste' → 'Persian religious lore, astrology' → (with Greek and then Christian hostility) 'sorcery'.\",\n          \"derivation_fa\": \"انگلیسی magic از انگلیسی میانهٔ magik (چاسر، اواخر سدهٔ چهاردهم) و آن از magique فرانسهٔ کهن/میانه، از magicē (ars) لاتینِ متأخر، از μαγική (τέχνη) یونانی «هنرِ مغان» ــ مؤنثِ μαγικός ــ و در نهایت از μάγος و maguš پارسی باستان است. کلاین همین زنجیره را در مدخل magic آورده و واتکینز نیز MAGIC و MAGI و MAGUS را زیر ریشهٔ magh-1 نشانده است. تحولِ معنایی چنین بوده: «متعلق به طبقهٔ روحانیِ ماد» ← «دانش دینی و اخترشماریِ ایرانی» ← و سپس با نگاه خوارانگارانهٔ یونانی و آنگاه مسیحی «جادوگری». ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/mag%CA%B0-\"],\n          \"ref_check\": [\n            {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"No reference in this box; covered by Klein p.921 s.v. magic and Watkins magh-1 §5 ('MAGI, MAGIC, MAGUS; ARCHIMAGE').\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein p.921 s.vv. magic n./adj. (KLN_1966.txt lines 22519-22520)\", \"stance\": \"supports\", \"note\": \"'magic, adj. — ME. magik, fr. OF. (= F.) magique, fr. L. magicus, fr. μαγικός, \\\"Magian, magical\\\", fr. μάγος, \\\"Magus, magician\\\"'.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. magh-1 §5 and index (AHD_watkins1985.txt lines 710, 1792-1794)\", \"stance\": \"supports\", \"note\": \"'MAGI magh-1', 'MAGIC magh-1', 'MAGUS magh-1' — the English word is filed under this root via Old Persian magus.\"}\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"Germanic\",\n          \"words\": \"mag, mahti\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Nourai's 'mag' and 'mahti' are the two Germanic stems of this root: (a) the preterite-present verb Proto-Germanic *magan 'to be able' with 1/3sg present *mag (Gothic mag, OHG mag, OS mag, OE mæg, ON má) — a PIE perfect/optative formation, which is why it lacks the -s of the 3sg present; and (b) the ti-abstract *mahti- (< *magh-ti-) 'power, might', Gothic mahts, OHG/OS maht, OE meaht/miht, ON máttr, matched outside Germanic by OCS moštь 'Macht, Stärke'. Pokorny lists both with these very forms, and Watkins gives '*mag-' and 'suffixed form *mah-ti-, power'. To these Germanic also adds *maginam 'strength' (ON magn/megin, OE mægen, OHG magan/megin), the source of English main — see node #11.\",\n          \"derivation_fa\": \"دو صورتی که نورایی آورده («mag» و «mahti») همان دو ستاک ژرمنی این ریشه‌اند: نخست، فعلِ ماضی‌ـحالیِ ژرمنی آغازین *magan «توانستن» با صورتِ مفردِ حال *mag (گوتیک mag، آلمانی علیای کهن mag، انگلیسی کهن mæg، نورس کهن má) که چون در اصل صیغهٔ ماضی نقلیِ هندواروپایی بوده پایانهٔ -s شخصِ سوم را ندارد؛ دوم، اسم مصدرِ ti-دار *mahti- (از *magh-ti-) «توان، نیرو»: گوتیک mahts، آلمانی علیای کهن maht، انگلیسی کهن meaht/miht، نورس کهن máttr، که بیرون از ژرمنی با moštь اسلاوی کلیسایی کهن «قدرت» برابر است. پوکورنی هر دو را با همین صورت‌ها آورده و واتکینز نیز «*mag-» و «صورتِ پسوندیِ *mah-ti-، power» را ثبت کرده است. ژرمنی صورتِ سومی هم دارد، *maginam «نیرو» (نورس magn/megin، انگلیسی کهن mægen)، که خاستگاه main انگلیسی است. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/mag%CA%B0-\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt line 710, magh-1 §1-3: '1. Germanic *mag- in: a. Old English magan, to be able: MAY ... 2. Germanic suffixed form *mah-ti-, power, in Old English miht, power: MIGHT. 3. Germanic suffixed form *mag-inam, power, in Old English mægen, power: MAIN.' Exactly Nourai's 'mag, mahti : power'.\"},\n            {\"ref\": \"KLN\", \"status\": \"supports\", \"note\": \"KLN_1966.txt line 22460 (p.919, s.v. machine): '... fr. I.-E. base *magh-, *māgh-, \\\"to be able\\\", whence also OSlav. mogǫ, mošti, \\\"to be able\\\", OE. mæg, \\\"I can\\\". See may, auxil. v., and cp. main, \\\"might\\\", might.' Klein groups the Germanic forms under the same base.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"Pokorny IEW p.695 f. (POK_02.txt lines 5669-5670)\", \"stance\": \"supports\", \"note\": \"'got. ags. magan, aisl. mega, maga, muga, afries. muga, mnd. mögen, ahd. magan, mugan ,mögen', 1. Sg. Präs. got. as. ahd. mag, aisl. má, ags. mæg, afries. mei; aisl. magn, meg(i)n n. ,Macht, Hauptsache', ags. mægen, ahd., as. magan, megin ds.; got. mahts f. ,Macht, Kraft', ahd. as. maht, ags. meaht, might, aisl. máttr ds.'\"},\n            {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. II 227 (WLD_Bd2_pages.txt lines 14841-14846)\", \"stance\": \"supports\", \"note\": \"Same Germanic list a generation earlier: 'got. mag (Inf. magan, Praet. mahta) ,vermag, kann', ... ags. mæg ds. aisl. magn, megin ,Kraft, Macht', ags. mægen, as. megin, ahd. magan, megin ds.: got. mahts ,Kraft, Macht', ahd. as. maht, ags. meaht, might, aisl. máttr ds.'\"},\n            {\"src\": \"IEC\", \"where\": \"Mann s.vv. moghó/moghmi and moghtis (IEC.txt lines 11000, 11002)\", \"stance\": \"supports\", \"note\": \"'moghó, moghmi \\\"am able, can\\\". WP II, 227 ... Go. OHG mag \\\"I can, may\\\"'; 'moghtis \\\"power\\\" ... Go. mahts, f. \\\"might, power\\\"; OHG maht ...; ON máttr' — Mann's two lemmas correspond to Nourai's two Germanic stems.\"}\n          ]\n        },\n        {\n          \"id\": 11,\n          \"lang\": \"English\",\n          \"words\": \"main, might, may\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All three English words come from the Germanic stems of node #10. may < OE magan, 1sg/3sg pres. mæg (preterite-present), whence ME may; might (n.) < OE miht/meaht < PGmc *mahtiz, with the West Germanic -ht- reflex of *-gh-t-; main (n., 'strength', now only in the alliterative doublet 'might and main') < OE mægen < PGmc *maginam. Watkins files them under magh-1 §1a, §2 and §3 respectively, and Klein cross-refers them at s.v. machine ('See may, auxil. v., and cp. main, \\\"might\\\", might'). The verb might (past of may) belongs with may (OE meahte/mihte), so the box's three items exhaust the native English descendants of the root.\",\n          \"derivation_fa\": \"هر سه واژهٔ انگلیسی از دو ستاک ژرمنیِ گرهٔ پیشین برآمده‌اند: may از انگلیسی کهن magan و صورتِ حالِ mæg؛ might (اسم) از انگلیسی کهن miht/meaht و آن از ژرمنی آغازین *mahtiz، که در آن خوشهٔ *-gh-t- هندواروپایی در ژرمنی غربی به -ht- بدل شده است؛ و main (اسم، «نیرو»، که امروز تنها در ترکیبِ همحرفِ «might and main» مانده) از انگلیسی کهن mægen و ژرمنی آغازین *maginam. واتکینز این سه را به‌ترتیب زیر بندهای ۱الف و ۲ و ۳ ریشهٔ magh-1 نشانده و کلاین نیز در مدخل machine به همین سه ارجاع داده است. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/mag%CA%B0-\"],\n          \"ref_check\": [\n            {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"No reference in this box; the parent box's AHD and KLN cover it — Watkins magh-1 §1a MAY, §2 MIGHT, §3 MAIN (AHD_watkins1985.txt line 710).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985, magh-1 and index (AHD_watkins1985.txt lines 710, 1801, 1831, 1869)\", \"stance\": \"supports\", \"note\": \"Index entries 'MAIN1 magh-1', 'MAY magh-1, meg-', 'MIGHT1 magh-1' — all three under this root.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein p.919 s.v. machine (KLN_1966.txt line 22460)\", \"stance\": \"supports\", \"note\": \"'... whence also OSlav. mogǫ, mošti, \\\"to be able\\\", OE. mæg, \\\"I can\\\". See may, auxil. v., and cp. main, \\\"might\\\", might.'\"},\n            {\"src\": \"POK\", \"where\": \"Pokorny IEW p.696 (POK_02.txt line 5669)\", \"stance\": \"supports\", \"note\": \"Pokorny himself prints the English glosses in the Germanic list: 'ags. mægen ... ags. meaht, might'.\"}\n          ]\n        },\n        {\n          \"id\": 12,\n          \"lang\": \"Greek\",\n          \"words\": \"mexana, mâxanâ, mexos; maxanikon\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The first three are right: Greek μῆχος mēkhos (n.) 'means, expedient, remedy', Doric μᾶχος, and the derived μηχανή mēkhanē 'device, contrivance, engine' with the Doric μαχανά mākhanā, all from *magʰ- 'be able' — Watkins reconstructs 'suffixed lengthened-grade form *magh-and-, \\\"that which enables\\\"', Pokorny prints 'gr. μῆχος n. (dor. μᾶχος), poet. μῆχαρ ,Hilfsmittel', μηχανή, dor. μαχανά (> lat. machina) ,Hilfsmittel, Werkzeug, List''. The fourth item is where the box goes wrong: μηχανικόν is simply the neuter of the adjective μηχανικός 'resourceful, inventive; mechanical' (Klein p.933 s.v. mechanic: 'Gk. μηχανικός, \\\"resourceful, inventive; mechanical\\\"'), not a noun 'a war machine'; the Greek word for the stone-throwing engine is μαγγανικόν manganikon, from μάγγανον 'engine, block, charm' — a different word (AHD meng- 731, Klein s.v. mangle/mangonel). Nourai needs the gloss 'a war machine' to get to منجنیق in node #13, so the mis-gloss and that node's disputed derivation are one and the same problem. A caveat in Nourai's favour: Beekes argues μηχανή is Pre-Greek and 'possibly a doublet of μάγγανον', which would blur the line between the two words.\",\n          \"derivation_fa\": \"سه صورت نخست درست است: یونانی μῆχος (mēkhos) «وسیله، چاره، درمان» و صورتِ دوریِ آن μᾶχος، و مشتقِ μηχανή (mēkhanē) «ابزار، دستگاه، ماشین» با صورتِ دوریِ μαχανά (mākhanā)، همه از ریشهٔ *magʰ- «توانستن»؛ واتکینز آن را از صورتِ پسوندیِ کشیده‌ٔ *magh-and- «آنچه توانا می‌کند» می‌گیرد و پوکورنی هم همین صورت‌ها را با ترجمهٔ «Hilfsmittel, Werkzeug, List» آورده است. اما چهارمین واژه نادرست معنی شده: μηχανικόν تنها صورتِ خنثای صفتِ μηχανικός «چاره‌گر، مبتکر، مکانیکی» است (کلاین، مدخل mechanic) و اسمی به معنی «منجنیق» نیست؛ نامِ یونانیِ آن دستگاهِ سنگ‌انداز μαγγανικόν (manganikon) از μάγγανον است که واژهٔ دیگری است. نورایی به این معنیِ نادرست نیاز دارد تا به «منجنیق» در گرهٔ بعد برسد، پس این لغزشِ معنایی و ریشه‌شناسیِ مورد اختلافِ گرهٔ ۱۳ یک مسئله‌اند. در دفاع از نورایی باید افزود که بیکس μηχανή را پیش‌یونانی و «احتمالاً دوگانهٔ μάγγανον» می‌داند که مرز میان این دو واژه را کم‌رنگ می‌کند. پس این گره «با احتیاط پذیرفتنی» است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%CE%BC%CE%B7%CF%87%CE%B1%CE%BD%CE%AE\",\n            \"https://www.etymonline.com/word/mangonel\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:919\", \"status\": \"supports\", \"note\": \"KLN_1966.txt page marker 919 at line 22423; entry at line 22460: 'machine, n. — MF. (= F.), fr. L. māchina, \\\"machine, engine, fabric, frame, device, trick\\\", fr. Dor. μαχανά, corresponding to Att. μηχανή, \\\"machine, contrivance, artificial means, expedient\\\", fr. Dor. μᾶχος (Attic μῆχος), \\\"contrivance, means, expedient, remedy\\\", fr. I.-E. base *magh-, *māgh-, \\\"to be able\\\"'. The cited page is exactly right for mēkhanē / mākhanā / mēkhos.\"},\n            {\"ref\": \"AHD:780\", \"status\": \"partial\", \"note\": \"Nourai's AHD page numbers on this page (780, 793) are pages of the 1975 New College main dictionary, which is not the volume on disk; the Indo-European appendix content is checkable and supports the first three words — AHD_watkins1985.txt line 710, magh-1 §4: 'Suffixed lengthened-grade form *magh-and-, \\\"that which enables,\\\" in Greek (Attic) mēkhanē, (Doric) mākhanā, device: MACHINE, MECHANIC, (MECHANISM), (MECHANO-)'. Watkins does not put any war-engine sense here.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"Pokorny IEW p.695 (POK_02.txt line 5668)\", \"stance\": \"supports\", \"note\": \"'gr. μῆχος n. (dor. μᾶχος), poet. μῆχαρ ,Hilfsmittel', μηχανή, dor. μαχανά (> lat. machina) ,Hilfsmittel, Werkzeug, List''.\"},\n            {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. II 227 (WLD_Bd2_pages.txt lines 14839-14840)\", \"stance\": \"supports\", \"note\": \"'Gr., dor. μᾶχος „Hilfsmittel“, dor. μαχανά „Hilfsmittel, List; Werkzeug; Mittel, etwas zu erlangen“'.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein p.933 s.v. mechanic (KLN_1966.txt line 23250)\", \"stance\": \"contradicts\", \"note\": \"'mechanic, adj. — L. mechanicus, fr. Gk. μηχανικός, \\\"resourceful, inventive; mechanical\\\", fr. μηχανή, \\\"means, invention, machine\\\"' — μηχανικόν is an adjective, not the name of a war engine; Klein's war engine is at p.933 s.v. mangonel, from μάγγανον.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat s.vv. mechanic and mangle/mangonel (SKT.txt lines 10869, 11037-11038)\", \"stance\": \"partial\", \"note\": \"'mechanic ... — Gk. μηχανική, science of machines'; but 'mangle (1) ... Low L. manganum, mangona, a military instrument for throwing stones ... — Gk. μάγγανον' and 'mangonel, a war-engine ... O.F. mangonel ... of manganum (above)' — the two Greek words are kept apart.\"}\n          ]\n        },\n        {\n          \"id\": 13,\n          \"lang\": \"Persian\",\n          \"words\": \"manjanîk «منجنیک»\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The word is real and old in Persian: منجنیک / منجنیق manjanīk/manjanīq 'mangonel, stone-throwing siege engine', used by Ferdowsī (the hemistich quoted on the page). Nourai derives it from Greek μηχανικόν, and he is not alone: Mo'in's own etymological footnote at Borhan-e Qate' p.2039 says the word is a mis-shapen (مصحّف) *mīxanīq 'from μηχανική (Liddell & Scott)', through Syriac into Arabic منجنیق/منجنیقه, and Noushin's Vazhe-namak p.311 glosses «منجنیق (معرب منجنیک؛ از یونانی مخانیک)». But modern scholarship prefers a different Greek source: Byzantine μαγγανικόν / pl. μαγγανικά (from μάγγανον 'engine, block; charm'), which passed through Syriac ܡܢܓܢܝܩܐ mangānīqā into Arabic مَنْجَنِيق and thence into Persian. That route accounts for the nasal in man-janīq, which μηχανικόν cannot supply, and it is the route of Wiktionary, Etymonline, Klein p.933, Watkins (meng-, Pok. 731) and Skeat; Addi Shir at the very page Nourai cites (AFM p.164) himself prints the Syriac ܡܝܓܢܝܩܐ form and only tentatively adds a Persian folk-etymology 'من چه نيك'. Asbaghi (PLA) likewise routes Arabic manǧanīq through Persian manǧanīk from Persian mangāne + Syriac. Two further wrinkles: (a) Wiktionary makes the Persian word a loan from Arabic, whereas Nourai draws Greek → Persian directly, though Borhan ('منجنیق معرب منجنیک باشد') and Asbaghi support a pre-Arabic Persian manjanīk; (b) Beekes' suggestion that μηχανή and μάγγανον are doublets would partly reconcile the two camps. The chart's own NOTE (AHD:793, KLN:933, root Meng) states the rival view accurately, and that rival view is the one modern scholarship takes.\",\n          \"derivation_fa\": \"واژه واقعی و کهن است: «منجنیک/منجنیق» به معنی دستگاهِ سنگ‌اندازِ محاصره، که فردوسی هم آن را در بیتِ نقل‌شده در همین صفحه به کار برده است. نورایی آن را از μηχανικόν یونانی می‌گیرد و در این کار تنها نیست: معین در حاشیهٔ ریشه‌شناسیِ برهان قاطع (ص ۲۰۳۹) می‌نویسد «اصل کلمه مصحّفِ مِیخَنیق از μηχανική (لیدل و اسکات)» و از راه سریانی به عربی منجنیق و منجنیقه رسیده، و نوشین در واژه‌نامک (ص ۳۱۱) می‌آورد «منجنیق (معرب منجنیک؛ از یونانی مخانیک)». اما ریشه‌شناسیِ امروزی سرچشمهٔ یونانیِ دیگری را ترجیح می‌دهد: μαγγανικόν بیزانسی (جمعِ μαγγανικά) از μάγγανον «دستگاه، افسون»، که از راهِ سریانی mangānīqā به عربی «مَنْجَنِيق» و از آن به فارسی رسیده است. این مسیر «ن»ِ من‌جنیق را توضیح می‌دهد که μηχανικόν از عهدهٔ آن برنمی‌آید، و همان مسیری است که ویکی‌واژه و اتیمونلاین و کلاین و واتکینز (ذیل ریشهٔ meng، پوکورنی ۷۳۱) و اسکیت برگزیده‌اند؛ حتی ادّی شیر در همان صفحهٔ ۱۶۴ که نورایی ارجاع می‌دهد صورتِ سریانی ܡܝܓܢܝܩܐ را می‌آورد و ریشهٔ فارسیِ «من چه نيك» را تنها به‌احتمال می‌افزاید. اصبغی نیز عربی manǧanīq را از فارسیِ manǧanīk و آن را از mangāne می‌گیرد. دو نکتهٔ دیگر: ویکی‌واژه واژهٔ فارسی را وام‌واژه‌ای از عربی می‌داند، در حالی که نورایی پیکان را یکسر از یونانی به فارسی می‌کشد (هرچند برهان قاطع «منجنیق معرب منجنیک باشد» و اصبغی جانب او را می‌گیرند)؛ و بیکس احتمال داده که μηχανή و μάγγανον دوگانهٔ یکدیگر باشند که تا اندازه‌ای دو دیدگاه را به هم نزدیک می‌کند. یادداشتِ خودِ کتاب دیدگاه رقیب را درست نقل کرده و پژوهش امروزی همان دیدگاه رقیب را می‌پذیرد.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%85%D9%86%D8%AC%D9%86%DB%8C%D9%82\",\n            \"https://www.etymonline.com/word/mangonel\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:2039\", \"status\": \"supports\", \"note\": \"Fetched with tools/ref_page.py BQT:2039 (vol. 4 pdf page 122; OCR cached under data/verification/sources/refs/ocr/BQT/). Entry: «منجنياگ «با کاف» ... همان منجنیق است و منجنیق معرب منجنيك باشد» with Mo'in's footnote 9: «در قاموس آمده: منجنيك بمعنی «من چه ليك» ... اصل کلمه مصحف میخنیق از [μηχανική] «لیدل و اسکات» ... سریانی ...؛ عربی منجنیق، منجنیکه، عامیانه منجلق ...؛ قس: انگ mangonel (منجنیق)». This is precisely Nourai's claim, μηχανική included.\"},\n            {\"ref\": \"FSF:311\", \"status\": \"supports\", \"note\": \"Noushin, Vazhe-namak (FSF_pages.txt line 20604, form-feed leaf 421 of 484 — the position matching printed p.311 of ~350): «منجنیق (معرب منجنیک؛ از یونانی مخانیک) افزاری که با آن سنگ آتش به سوی دشمن پرتاب می‌کردند: نیاید برو [کوه] منجنیق و نه تیر / بباید ترا دید آن ناگزیر». Both the Greek 'مخانیک' etymology and the Ferdowsī hemistich Nourai quotes.\"},\n            {\"ref\": \"AFM:164\", \"status\": \"partial\", \"note\": \"Addi Shir, AFM_pages.txt form-feed leaf 147 (the م section; the leaf position matches printed p.164 given leaf+17 across the ي section and index). The entry «( المنجنيق ) آلة ...» is there, but the OCR (Syriac-script confusion) shows Addi Shir citing the SYRIAC ܡܝܓܢܝܩܐ (mangānīqā) form as the intermediary («بالواسطة») and only adding «ويحتمل ان يكون اصل الكلمة فارسيًا ... من چه نيك» as a possibility. So the cited page has the word but supports the manganikon/Syriac route, not μηχανή.\"},\n            {\"ref\": \"MON:4384\", \"status\": \"partial\", \"note\": \"Print pagination of the 6-vol. edition is not recoverable from the local OCR; منجنیق does occur repeatedly in Mo'in's text (MON_part1.txt lines 24970, 32807, 95359 — e.g. 'کوچکتر از منجنیق که در جنگ‌های قدیم'), and Mo'in's etymology for the word is the Borhan footnote checked above, i.e. it supports Nourai.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PLA\", \"where\": \"Asbaghi, Persische Lehnwörter im Arabischen s.v. manǧanīq (PLA_pages.txt lines 14084-14089)\", \"stance\": \"partial\", \"note\": \"'manǧanīq: \\\"Kriegsmaschine\\\" aus pers. منجنیک manǧanīk ... aus pers. منگانه mangāne, syr. ...' — Asbaghi does posit a pre-Arabic Persian manǧanīk (supporting Nourai's arrow direction), but traces it to a mangāne/manganon type with Syriac mediation, not to μηχανή.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein p.933 s.vv. mangonel and mangle (KLN_1966.txt lines 22793, 22796)\", \"stance\": \"contradicts\", \"note\": \"'mangonel, n., military engine for hurling stones. — OF. (= F. mangonneau), dimin. of ML. mangonum, mangona, fr. VL. *manganum, \\\"machine\\\", fr. Gk. μάγγανον'; and s.v. mangle: 'Gk. μάγγανον, \\\"any means for tricking or bewitching, philter, drug\\\" ... fr. I.-E. base *mang-, \\\"to embellish, dress, trim\\\"'. Different root from magh-.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. meng- (AHD_watkins1985.txt lines 747-751)\", \"stance\": \"contradicts\", \"note\": \"'meng-. To furbish. 1. Latin mango ... 2. Greek manganon, magic charm, contrivance, engine of war: MANGONEL. [Pok. meng- 731.]' — exactly the rival derivation the chart's own NOTE reports.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat s.v. mangonel (SKT.txt line 11038)\", \"stance\": \"contradicts\", \"note\": \"'mangonel, a war-engine ... O.F. mangonel ... — Low L. ... of manganum (above)', i.e. from Gk. μάγγανον, 'a military instrument for throwing stones'.\"},\n            {\"src\": \"AFA\", \"where\": \"Fraenkel, Die aramäischen Fremdwörter im Arabischen (AFA.txt)\", \"stance\": \"silent\", \"note\": \"Grep for منجنيق / mangan- in AFA.txt returns nothing; Fraenkel's Aramaic loans do not cover this word in the OCR available.\"},\n            {\"src\": \"LKT\", \"where\": \"Lokotsch (LKT.txt)\", \"stance\": \"silent\", \"note\": \"Grep for mangonel / manganon / Mandschanik in LKT.txt returns nothing.\"}\n          ]\n        },\n        {\n          \"id\": 14,\n          \"lang\": \"Latin\",\n          \"words\": \"mâčina\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin māchina 'machine, engine, contrivance, frame, device, trick' is borrowed not from Attic μηχανή but from the DORIC μαχανά — the tell-tale ā shows the loan came through the Doric-speaking Greek colonies of southern Italy and Sicily (Magna Graecia), the usual channel for early Greek technical borrowings into Latin (cf. Latin machaera, mācellum). Pokorny prints the loan inside the Greek line, 'dor. μαχανά (> lat. machina)', and Klein p.919 spells it out: 'L. māchina ... fr. Dor. μαχανά, corresponding to Att. μηχανή'. From it Latin builds māchinārī 'to contrive', māchinātor, and (with Vulgar Latin *machinare specialized to 'grind') Italian macinare, Romanian măcina. Nourai's gloss 'engine' is one of the classical senses.\",\n          \"derivation_fa\": \"لاتینی māchina «دستگاه، ماشین، ابزار، چاره، نیرنگ» نه از μηχανή آتیکی بلکه از صورتِ دوریِ μαχανά وام گرفته شده است؛ همان واکهٔ ā نشان می‌دهد که وام‌گیری از راه شهرهای یونانی‌زبانِ دوریِ جنوب ایتالیا و سیسیل («یونانِ بزرگ») بوده، که مسیرِ معمولِ وام‌واژه‌های فنیِ کهنِ یونانی در لاتین است (قس machaera و macellum). پوکورنی همین را در دلِ سطرِ یونانی می‌آورد: «dor. μαχανά (> lat. machina)» و کلاین در صفحهٔ ۹۱۹ صریح می‌گوید «لاتینی māchina ... از μαχανά دوری، برابرِ μηχανή آتیکی». از این واژه در لاتین māchinārī «تدبیر کردن» و māchinātor ساخته شده و در لاتینِ عامیانه *machinare با تحول معناییِ «آسیا کردن» به macinare ایتالیایی رسیده است. معنیِ «engine» که نورایی داده یکی از معانی کلاسیک آن است. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%CE%BC%CE%B7%CF%87%CE%B1%CE%BD%CE%AE\"],\n          \"ref_check\": [\n            {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"No reference in this box; the parent's KLN:919 covers it verbatim ('L. māchina ... fr. Dor. μαχανά'), as does POK:695 ('dor. μαχανά (> lat. machina)').\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"Pokorny IEW p.695 (POK_02.txt line 5668)\", \"stance\": \"supports\", \"note\": \"'μηχανή, dor. μαχανά (> lat. machina) ,Hilfsmittel, Werkzeug, List''.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein p.919 s.v. machine (KLN_1966.txt line 22460)\", \"stance\": \"supports\", \"note\": \"'fr. L. māchina, \\\"machine, engine, fabric, frame, device, trick\\\", fr. Dor. μαχανά, corresponding to Att. μηχανή'.\"},\n            {\"src\": \"SYN\", \"where\": \"Buck 9205\", \"stance\": \"partial\", \"note\": \"'It. macinare, Rum. măcina, fr. VLat. *machinare a new denom. of Lat. machina \\\"machine\\\", with specialization to \\\"grind\\\". REW 5206.' — confirms Latin machina and its Romance life, without discussing the Greek source.\"}\n          ]\n        },\n        {\n          \"id\": 15,\n          \"lang\": \"French\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Empty pass-through box for French: Middle French machine (attested from the 14th-15th c., from Latin māchina), plus the learned pair mécanique (adj./n., from Latin mechanicus/mechanica < Gk. μηχανικός) and mécanisme (18th c., from Modern Latin mechanismus). These are the exact three French words that feed the Persian box #16 (ماشین، مکانیک، مکانیزم) and that Klein names as the immediate source of English machine ('MF. (= F.)').\",\n          \"derivation_fa\": \"این جعبهٔ خالی نمایندهٔ مرحلهٔ فرانسه است: machine در فرانسهٔ میانه (از سدهٔ چهاردهم‌ـپانزدهم، از māchina لاتینی)، و همچنین جفتِ عالمانهٔ mécanique (از mechanicus/mechanica لاتینی و μηχανικός یونانی) و mécanisme (سدهٔ هجدهم، از mechanismus لاتینِ نو). همین سه واژهٔ فرانسوی‌اند که به جعبهٔ فارسیِ گرهٔ ۱۶ («ماشین، مکانیک، مکانیزم») می‌رسند، و کلاین نیز machine فرانسهٔ میانه را سرچشمهٔ بی‌واسطهٔ machine انگلیسی می‌داند. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D9%85%D8%A7%D8%B4%DB%8C%D9%86\"],\n          \"ref_check\": [\n            {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"Empty box, no reference; verified from Klein p.919 ('machine, n. — MF. (= F.), fr. L. māchina') and p.933 ('mechanism, n. — ModL. mechanismus').\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein pp.919, 933 (KLN_1966.txt lines 22460, 23251)\", \"stance\": \"supports\", \"note\": \"'machine, n. — MF. (= F.), fr. L. māchina'; 'mechanism, n. — ModL. mechanismus, fr. Gk. ...'.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat s.v. mechanic (SKT.txt line 10869)\", \"stance\": \"supports\", \"note\": \"'mechanic, pertaining to machines. (F. — L. — Gk.) M.E. mechanike ... — O.F. mechanique, mechanical. — L. mechanica. — Gk. μηχανική' — the French stage is Skeat's too.\"}\n          ]\n        },\n        {\n          \"id\": 16,\n          \"lang\": \"Persian\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"The three Persian words in the box (ماشین māšin, مکانیک mekānik, مکانیزم mekānizm) are late, direct French loans of the Qajar/Pahlavi modernization period, taken in with the technical vocabulary that came with the Dār al-Fonūn, the military missions and French-medium schooling — Wiktionary: Persian ماشین 'Borrowed from French machine', with the chain PIE → Gk. μηχανή → Lat. māchina → Middle French → French → Persian; مکانیک < Fr. mécanique, مکانیزم < Fr. mécanisme (the -یزم suffix is the regular Persian rendering of French -isme). Mo'in marks this class of word with the origin tag [فر.] (French). So these are cognates-by-a-long-way of منجنیک in node #13 only if that node's etymology holds; on their own they are unproblematic and confirm Nourai's French → Persian arrow.\",\n          \"derivation_fa\": \"سه واژهٔ این جعبه («ماشین»، «مکانیک»، «مکانیزم») وام‌واژه‌هایی متأخر و بی‌واسطه از فرانسه‌اند که در دورهٔ نوسازیِ قاجاری و پهلوی، همراه با واژگان فنیِ دارالفنون و هیئت‌های نظامی و آموزشِ فرانسوی‌زبان، به فارسی درآمدند: ماشین از machine فرانسوی، مکانیک از mécanique و مکانیزم از mécanisme (پسوندِ «ـیزم» برگردانِ قاعده‌مندِ -isme فرانسوی در فارسی است). ویکی‌واژه زنجیرهٔ هندواروپایی ← μηχανή یونانی ← māchina لاتینی ← فرانسهٔ میانه ← فرانسه ← فارسی را برای «ماشین» می‌آورد، و معین این دسته واژه‌ها را با برچسبِ [فر.] نشان می‌دهد. پس پیکانِ «فرانسه ← فارسی» نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D9%85%D8%A7%D8%B4%DB%8C%D9%86\"],\n          \"ref_check\": [\n            {\"ref\": \"MON:3701,4312\", \"status\": \"not_checked\", \"note\": \"The print pagination of the 6-vol. edition cannot be located in the local OCR (MON_part1/part2 are an unpaginated 2-vol. reprint) and vajehyab/abadis give entry text without pages. ماشین does occur throughout the OCR (e.g. MON_part1.txt line 9654 'ماشین‌های خودکار'), and Mo'in's origin tag for such words is [فر.]; the claim itself is independently confirmed by Wiktionary.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"Mo'in, ماشین in the OCR of the reprint (MON_part1.txt lines 5890, 9654, 10696)\", \"stance\": \"supports\", \"note\": \"ماشین is treated as a modern loan and appears in compounds ('ماشین تحریر', 'ماشین‌های خودکار'); per refs_online.json Mo'in's origin tag for this class is [فر.] = French.\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e Rishe-ha (ARY_pages.txt)\", \"stance\": \"silent\", \"note\": \"Grep for ماشین/مکانیک in ARY_pages.txt returns nothing relevant (the OCR is thin; the only hit in the м range is an unrelated زوت/موبد line at 9693) — Aryanpur's book is about inherited Indo-European roots in Persian, not modern European loans.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein p.919 s.v. machine (KLN_1966.txt line 22460)\", \"stance\": \"supports\", \"note\": \"Confirms the French word that Persian borrowed: 'machine, n. — MF. (= F.), fr. L. māchina'.\"}\n          ]\n        },\n        {\n          \"id\": 17,\n          \"lang\": \"English\",\n          \"words\": \"machine, mechanic\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Both English words descend from Latin māchina / mechanicus and ultimately from Doric μαχανά — that much is certain (machine is first attested in English in the 1540s, mechanic as a noun/adjective already in Middle English). The chart's arrow is only slightly too short: both words reached English through French, not straight from Latin. Klein: 'machine, n. — MF. (= F.), fr. L. māchina'; Skeat: 'mechanic ... (F. — L. — Gk.) M.E. mechanike ... — O.F. mechanique, mechanical. — L. mechanica. — Gk. μηχανική, science of machines'. Since Nourai already has a French box (#15) on this branch and does route English magic (#9) through French, drawing Latin → English directly here is a simplification rather than an error; Watkins likewise files MACHINE, MECHANIC, MECHANISM under magh-1 §4 without the intermediate stages. Verdict plausible: right root, right ultimate source, one intermediary skipped.\",\n          \"derivation_fa\": \"هر دو واژهٔ انگلیسی از māchina و mechanicus لاتینی و در نهایت از μαχανά دوری برآمده‌اند و در این تردیدی نیست (machine نخست در دههٔ ۱۵۴۰ در انگلیسی دیده می‌شود و mechanic پیش‌تر، در انگلیسی میانه). تنها اشکالِ پیکانِ نمودار کوتاه بودنِ آن است: هر دو واژه از راه فرانسه به انگلیسی رسیده‌اند، نه یکسر از لاتین؛ کلاین می‌گوید «machine از machine فرانسهٔ میانه، از māchina لاتینی» و اسکیت «mechanic (فرانسه ← لاتین ← یونانی)، انگلیسی میانه mechanike، از mechanique فرانسهٔ کهن». چون نورایی در همین شاخه جعبهٔ فرانسه (گرهٔ ۱۵) را دارد و در شاخهٔ magic هم انگلیسی را از فرانسه گذرانده، این‌جا کشیدن پیکانِ مستقیم از لاتین به انگلیسی ساده‌سازی است نه خطا؛ واتکینز هم MACHINE و MECHANIC و MECHANISM را بی‌ذکرِ مراحلِ میانی زیر magh-1 نشانده است. پس ادعای نورایی «با احتیاط پذیرفتنی» است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%CE%BC%CE%B7%CF%87%CE%B1%CE%BD%CE%AE\"],\n          \"ref_check\": [\n            {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"No reference in this box; checked against Klein p.919 s.v. machine and p.933 s.v. mechanic (KLN_1966.txt lines 22460, 23250), and Watkins magh-1 §4.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein pp.919, 933 (KLN_1966.txt lines 22460, 23250)\", \"stance\": \"partial\", \"note\": \"'machine, n. — MF. (= F.), fr. L. māchina' — French intermediary; 'mechanic, adj. — L. mechanicus, fr. Gk. μηχανικός' — Klein takes mechanic straight from Latin, so the chart's arrow is defensible for that word.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat s.v. mechanic (SKT.txt line 10869)\", \"stance\": \"partial\", \"note\": \"'mechanic, pertaining to machines. (F. — L. — Gk.) M.E. mechanike, in the sense \\\"mechanic art\\\". — O.F. mechanique ... — L. mechanica. — Gk. μηχανική, science of machines' — French stage explicit.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 magh-1 §4 and index (AHD_watkins1985.txt lines 710, 1788, 1841)\", \"stance\": \"supports\", \"note\": \"'MACHINE magh-1', 'MECHANIC magh-1', 'MECHANISM magh-1' — both English words under this root via Greek mēkhanē.\"},\n            {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century (WEB_vol1.txt line 112394)\", \"stance\": \"silent\", \"note\": \"Webster's entry checked in this range is 'mangonel, n. [OFr. mangonel, from LL. mangonellus, a mangonel.] a military apparatus formerly used for throwing stones' — relevant to node #13, not to machine/mechanic, for which no etymology was located in the OCR.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\nJSONEOF\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-318.json > /dev/null && echo \"JSON OK\"\npython3 /home/sfmqrb/git/rishe/tools/verify_check.py 318",
 "description": "Write and validate page-318.json"
}
```


### [2026-09-07T16:07:00.080Z] TOOL RESULT

```
JSON OK
nodes verified: 17/17
node verdicts: {'transcription_suspect': 1, 'confirmed': 12, 'plausible': 3, 'disputed': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 7, 'partial': 7, 'not_checked': 10}
books consulted: {'supports': 36, 'partial': 10, 'contradicts': 4, 'silent': 4} | by book: {'KLN': 11, 'POK': 6, 'SKT': 5, 'AHD': 4, 'NYB': 3, 'MON': 3, 'KNT': 2, 'PHD': 2, 'HRN': 2, 'FVQ': 2, 'TAD': 2, 'WLD': 2, 'BRT': 1, 'HUB': 1, 'ARB': 1, 'IEC': 1, 'PLA': 1, 'AFA': 1, 'LKT': 1, 'SYN': 1, 'ARY': 1, 'WEB': 1}
```


## [2026-09-07T16:07:05.906Z] TOOL CALL #71: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/ | grep -i 2039 ; ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/318.png; git status --short | head -20",
 "description": "Verify cached artifacts"
}
```


### [2026-09-07T16:07:05.985Z] TOOL RESULT

```
2039.png
2039.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 62558 Sep  7 11:55 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/318.png
 M data/verification/sources/web/index.jsonl
?? data/verification/page-318.json
?? data/verification/page-323.json
?? data/verification/sources/web/052d189616ce306f.txt
?? data/verification/sources/web/055d8f8dea8e42cb.txt
?? data/verification/sources/web/06852d2a8b308072.txt
?? data/verification/sources/web/0c040ca5a27e2b78.txt
?? data/verification/sources/web/0d2b126a3fde2522.txt
?? data/verification/sources/web/0d848321982a4872.txt
?? data/verification/sources/web/0dd85290db568cb6.txt
?? data/verification/sources/web/0e6506b045db0444.txt
?? data/verification/sources/web/13da706ecad297ce.txt
?? data/verification/sources/web/140845579911c711.txt
?? data/verification/sources/web/1543ee2dfdd393e7.txt
?? data/verification/sources/web/1be95b9ff81fa67b.txt
?? data/verification/sources/web/2673d00b315d8145.txt
?? data/verification/sources/web/287c2c9664cae2d4.txt
?? data/verification/sources/web/2db092d794b757d9.txt
?? data/verification/sources/web/33e2a4cffb8a4aae.txt
?? data/verification/sources/web/34a0bddc104d4ee3.txt
```


## [2026-09-07T16:07:29.855Z] AGENT

Page 318 (book p. 288) verified — one entry, root **Magh1**, 17 nodes. `verify_check.py 318`: 17/17 nodes, **0 PROBLEM lines**.

**Verdicts:** root confirmed · nodes: 12 confirmed, 3 plausible, 1 disputed, 1 transcription_suspect. Ref checks: 7 supports, 7 partial, 10 not_checked (mostly empty boxes with no refs). 22 different books consulted.

**Root:** confirmed. Pokorny 695 has the whole chart in one entry — `magh- : māgh- 'können, vermögen, helfen'; magh-ti- 'Macht'`, with `iran. magu-, apers. magus (daraus gr. μάγος, lat. magus)`, `gr. μῆχος / μηχανή, dor. μαχανά (> lat. machina)` and the Germanic `magan / mahts`. Watkins magh-1 matches word for word.

**Flagged items**
- **#13 منجنیک/منجنیق — disputed.** Nourai derives it from Gk μηχανικόν. Mo'in's own footnote at Borhan p. 2039 (fetched) and Noushin p. 311 («معرب منجنیک؛ از یونانی مخانیک») do back him. But modern scholarship (Wiktionary, Etymonline, Klein 933, Watkins *meng-* Pok. 731, Skeat, and Addi Shir on the very page cited) routes Arabic منجنيق from Byzantine μαγγανικόν < μάγγανον via Syriac mangānīqā — which explains the -n- of *man*-janīq. Asbaghi has Arab. manǧanīq ← Pers. manǧanīk ← mangāne. Beekes' suggestion that μηχανή and μάγγανον are doublets partly reconciles them. The chart's own NOTE states the rival view correctly.
- **#1 Avestan/Old Persian — transcription_suspect, error_in: "book".** `magus / maguš / moghu` are fine (OP maguš in Bīsotūn; Av. moγu- in moγu.tbiš-), but **maeg** and **megan** are Old English mæg / magan — Germanic forms that belong in box #10, where they also get the impossible gloss "Zoroastrian priest". The printed page (checked at 200 and 400 dpi; copy at `data/verification/sources/refs/ocr/BOOK/318.png`) prints them inside the Iranian box, so the extraction is faithful and the fault is Nourai's.
- **#4 Arabic majūs — plausible.** Right ultimate origin (OP maguš, Q 22:17) but every source inserts Aramaic/Syriac magūšā: Nyberg "whence Syr. lw. mgūsā, Arab. majūs-", Jeffery pp. 259–60, Mo'in `|معر. آرا. مجوشا|`, al-Unaysi. Nourai's arrow is direct.
- **#12 Greek — plausible.** mēkhos/mākhos/mēkhanē/mākhanā correct; but `maxanikon : a war machine` is wrong — μηχανικόν is the neuter of the adjective 'mechanical, inventive' (Klein 933); the war engine is μαγγανικόν. This mis-gloss is what carries #13.
- **#17 English machine, mechanic — plausible.** Both came via French (Klein "MF. (= F.)", Skeat "O.F. mechanique"); the chart draws Latin → English directly, a simplification, not an error.

**Extraction errors for the owner to fix in `data/extracted/batch/page-318.json`**
1. **Node #6 (Greek mağos) has `parent: 0`; the printed page draws it off node #1.** The arrow leaves the same descending stem from the Avestan/Old Persian box that feeds Pahlavi (#2) and Arabic (#4) — verified on the 400 dpi crop. The book's parentage is also the etymologically correct one.
2. **Node #13 quote text:** JSON has `نباید برو منجنیق و نه تیر`; the page prints **نیاید** (matching Noushin's Vazhe-namak and the Shahnameh).
