# Verification process log — verify-page-162


## [2026-09-05T20:31:25.448Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 162 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-162.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-162.json. Write /home/sfmqrb/git/rishe/data/verification/page-162.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 162` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T20:31:27.551Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T20:31:28.255Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T20:31:28.264Z] TOOL RESULT

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


## [2026-09-05T20:31:28.452Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-162.txt"
}
```


### [2026-09-05T20:31:28.464Z] TOOL RESULT

```
1	=== PDF page 162 (book page 132) ===
2	--- entry 0 ---
3	ROOT Esu -> redirect to Su 1
4	--- entry 1 ---
5	ROOT [Indo-European] Ěter : internal (insignificant) organs  (refs POK:344; IEC:1347; WLD1:264)
6	#1 (parent #0) [Avestan] refs=POK:344 | xv-âthra : insignificant, low in value ; duš-âthra : not insignificant, difficult ☞Dus ; su-âthra : ? ☞Su 1
7	  #2 (parent #1) [Pahlavi] refs=HRN:110,127 | xâr ; dušxvâr
8	    #3 (parent #2) [Persian] refs=BQT:780,866; HRN:110,127 | xâr 1 «خوار» : of low value ; došvâr «دشوار» : difficult | NOTE: See root "Xwâr" for a different derivation
9	--- entry 2 ---
10	ROOT E-tero -> redirect to I 2
11	--- entry 3 ---
12	ROOT [Indo-European] Eti : above, beyond  (refs POK:344; KLN:545)
13	#1 (parent #0) [Avestan] refs=KLN:545; KNT:166 | aiti 1 : over, beyond
14	#2 (parent #0) [Old Persian] refs=KNT:166 | ati : beyond
15	#3 (parent #0) [Latin] refs=KLN:545 | et : and ; et-cě-terî : :and other things ☞I 2,Ki 2
16	  #4 (parent #3) [English] refs=AHD | et cetera
17	#5 (parent #0) [Germanic] refs=KLN:545 | ith : back, again, water flowing back, whirlpool
18	  #6 (parent #5) [English] refs=AHD | eddy, eddy current
19	--- entry 4 ---
20	ROOT [Indo-European] Eu 1, Ewân, Wâ : to be empty  (refs POK:345)
21	#1 (parent #0) [Avestan] refs=POK:345; KLN:1687 | unâ, ŭna, uyamna : empty, needing
22	  #2 (parent #1) [Persian] refs=POK:345; HRN:243; BQT:2293 | vang 1 «وَنگ ۱» : empty, poor | NOTE: HUB:105 has doubts about this etymology.
23	#3 (parent #0) [Latin] refs=AHD | vâstus : empty, waste ; vacâre : to be empty, vacant ; vânus : empty, vain
24	  #4 (parent #3) [English] refs=AHD | waste ; vacate, vacuum, vacation, void, avoid ; vain, vanity, vanish
25	#5 (parent #0) [Germanic] refs=AHD | wanatôn : lacking, needing
26	  #6 (parent #5) [English] refs=AHD | want
27	
```


## [2026-09-05T20:31:31.895Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-162.json",
 "description": "Read source JSON for page 162"
}
```


### [2026-09-05T20:31:31.948Z] TOOL RESULT

```
{
  "pdf_page": 162,
  "book_page": 132,
  "entries": [
    {
      "root": {"name": "Esu", "redirect": "Su 1"},
      "nodes": []
    },
    {
      "root": {
        "name": "Ěter",
        "lang": "Indo-European",
        "refs": "POK:344; IEC:1347; WLD1:264",
        "gloss": "internal (insignificant) organs"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:344",
          "words": [
            {"translit": "xv-âthra", "gloss": "insignificant, low in value", "script": null},
            {"translit": "duš-âthra", "gloss": "not insignificant, difficult", "script": null, "see": ["Dus"]},
            {"translit": "su-âthra", "gloss": "?", "script": null, "see": ["Su 1"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "HRN:110,127",
          "words": [
            {"translit": "xâr", "gloss": null, "script": null},
            {"translit": "dušxvâr", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:780,866; HRN:110,127",
          "words": [
            {"translit": "xâr 1", "gloss": "of low value", "script": "خوار"},
            {"translit": "došvâr", "gloss": "difficult", "script": "دشوار"}
          ],
          "note": "See root \"Xwâr\" for a different derivation",
          "quote": null
        }
      ]
    },
    {
      "root": {"name": "E-tero", "redirect": "I 2"},
      "nodes": []
    },
    {
      "root": {
        "name": "Eti",
        "lang": "Indo-European",
        "refs": "POK:344; KLN:545",
        "gloss": "above, beyond"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "KLN:545; KNT:166",
          "words": [
            {"translit": "aiti 1", "gloss": "over, beyond", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "KNT:166",
          "words": [
            {"translit": "ati", "gloss": "beyond", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Latin",
          "refs": "KLN:545",
          "words": [
            {"translit": "et", "gloss": "and", "script": null},
            {"translit": "et-cě-terî", "gloss": ":and other things", "script": null, "see": ["I 2", "Ki 2"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "et cetera", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Germanic",
          "refs": "KLN:545",
          "words": [
            {"translit": "ith", "gloss": "back, again, water flowing back, whirlpool", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "eddy, eddy current", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Eu 1, Ewân, Wâ",
        "lang": "Indo-European",
        "refs": "POK:345",
        "gloss": "to be empty"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:345; KLN:1687",
          "words": [
            {"translit": "unâ, ŭna, uyamna", "gloss": "empty, needing", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "POK:345; HRN:243; BQT:2293",
          "words": [
            {"translit": "vang 1", "gloss": "empty, poor", "script": "وَنگ ۱"}
          ],
          "note": "HUB:105 has doubts about this etymology.",
          "quote": {
            "text": "نهال باغ جلال تراست گردون برگ - زکات گنج عطای قارون ونگ",
            "poet": "Mansûr Shîrâzî"
          }
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "vâstus", "gloss": "empty, waste", "script": null},
            {"translit": "vacâre", "gloss": "to be empty, vacant", "script": null},
            {"translit": "vânus", "gloss": "empty, vain", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "waste", "gloss": null, "script": null},
            {"translit": "vacate, vacuum, vacation, void, avoid", "gloss": null, "script": null},
            {"translit": "vain, vanity, vanish", "gloss": null, "script": null}
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
            {"translit": "wanatôn", "gloss": "lacking, needing", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "want", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-05T20:31:32.456Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T20:31:32.488Z] TOOL RESULT

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


## [2026-09-05T20:31:37.859Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','IEC','WLD','WLD1','KLN','KNT','HRN','BQT','AHD','HUB','BRT','PHD']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:600])\n\""
}
```


## [2026-09-05T20:31:38.038Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n 1,80p tools/verify_check.py && ls data/verification/ | head -50"
}
```


### [2026-09-05T20:31:39.764Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039
WLD1 null
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-
```


### [2026-09-05T20:31:39.801Z] TOOL RESULT

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
page-146.json
page-147.json
page-311.json
page-31.json
page-32.json
page-33.json
```


## [2026-09-05T20:31:45.160Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK_01 leaf 352 (p.344) ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==353' POK_01.txt | head -80"
}
```


### [2026-09-05T20:31:47.086Z] TOOL RESULT

```
=== POK_01 leaf 352 (p.344) ===
nd.  o-uste,  roste  ,Ruhe,  Wegstrecke',  spätmhd.  o-ust ,Ruhe';  got.  razn  n.  ,Haus',  anord.  rann  ds.^  ags.  cern,  ren  n.  ,Haus'  (mit merkwürdiger  Bed.  o^cßsn  n.  ,Planke,  Zimmerdecke'),  afries.  ern  in  ßä-ern ,Vieh-haus';  unsicher  ags.  reord  {^rezdo)  f.,  gereord  n.  , Mahlzeit,  Fest, Futter',  anord.  greddir  , Fütterer,  Sättiger'  {^garazdlz),  grenna  , füttern' {*ga-raznian).
Vgl.  rem-,  das  wie  res-  mit  (e)rd-  zusammengestellt  wird.
WP.  I  144  f.
er(9)d-  {,r{d)d-\  er{9)dh-  ,hoch;  wachsen'.
Av.  drddva-  ,hoch';
lat.  arduus  ,hüch,  steil' ;
gall.  Arduenna  silva,  air.  ard  (*fduo-)  ,hoch,  groß';  cjmr.  hardd  , schön';
aisl.  grdugr  , steil'  setzt  (wie  allenfalls  auch  drddva-)  eine  Parallelform auf  dh-  fort,  indem  verschiedene  Erweiterungen  von  er-  ,(in  Bewegung setzen)   hochbringen'  durch   dh   (vgl.  ÖQodvvcj  ,treibe  an'  usw.)  vorliegen.
Sicher  mit  dh  lat.  ai-hor  ^^-^n^'»  wozu  kurd.  är-  aus  *ard-  ,Baum'  in ärzang  ,die  durch  Wind  und  Wetter  verursachte  dunkle  Färbung  auf  den Bäumen*,  eig.  ,Baumrost' ;
alb.  rit  , wachse',  aus  fd-  oder  fdh-'^
slav.  *orstg,  abg.  rastg,  russ.  rastü,  cech.  rostu  usw.  , wachse*  (*ord-, ordh-to) ;
toch.  A  orto  , empor'.
WP.  I  148  f.,  II  289  f.,  WH.  I  64  f.
ergh'  , schütteln,  erregen,  beben'  od.  dgl.,  wohl  Erweiterung  von  er-  ,in Bewegung  setzen'.
Ai.  2'^Ä^y«^i  »bebt,  tost,  stürmt';
gr.  ÖQXEO)   ,7tall(x),  %Lve(x)\   meist  ÖQxaonai   ,tanze,   hüpfe,  springe,   bebe'.
Wegen  der  in  3.  er-  ebenfalls  vorliegenden  Bed.  ,1'^fg'  u.  dgl.  können  dazu in  Beziehung  stehen:
av.  drdyant-  ,arg,  abscheulich*;
ahd.  ar{a)g  ,feig,  träge,  böse,  arg',  ags.  earg  ds.,  aisl.  argr  und  mit Metathese  ragr  ,unmännlich,  wollüstig,  schlecht' ;
lit.  ariüs  ,lüstern,  sinnlich*.
WP.  I  147  f.
22*
340  9
erk"'  , strahlen;  hell  klingen,  lobpreisen'.
Ai.  drcati  , strahlt;  lobsingt,  begrüßt,  ehrt',  arkd-  m.  ,Strahl,  BlitzstraL)      1 Sonne,    Feuer;   Lied,   Sänger'   (=  arm.  erg),    rc-,    Nom.  Sg.  fÄ  f.  ,GlaiuI Gedicht;  Vers',  j-kvan-  ,lobpreisend,  jubelnd';  *
arm.  erg  ,Lied' ;  . .
air.  erc  , Himmel*,  mir.  suairc  , angenehm,  schön,  strahlend'  (*su-erhiU)* toch.  A  yärk,  B  yarke  »Verehrung'  (Pedersen  REtlE.  3,  18);  V'
hitt.  ar-ku-ua-nu-un  ,ich  betete'  (arkuannn) ;  anders  Hendrikseu  45 und  74.
WP.  I  147,
```


## [2026-09-05T20:31:47.460Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"ēter\\|ê-ter\\|eter-\\|ĕter\" POK_full.txt | head -30\necho \"---345---\"\ngrep -n \"eu-̯1\\|euə-\\|eu̯ə-\\|wā-.*leer\\|leer sein\" POK_full.txt | head -30"
}
```


### [2026-09-05T20:31:47.530Z] TOOL RESULT

```
4623:V. Planta II 32, 623); with -er- extension aiier praeter-eo, intered{see v. Planta II 455, WH. 
24537:{Ant-aib, Burgund-aib), Old High German -eiba {Weter-eiba, Wingart-eiba); 
29467:Root / lemma: eter- 
---345---
```


## [2026-09-05T20:31:51.636Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '29460,29500p' POK_full.txt"
}
```


### [2026-09-05T20:31:51.683Z] TOOL RESULT

```
Old Indie asfe, Avestan aste'he sits' (= gr. Attic narai ds.), ostiran. as-, 3. PI. Old Indie 
asate{== gr. hom. ETarai, lies narai), Avestan arjhente, 
Tokharian: B ask- 'sit, be seated' (Adams 58); A,B sam- 'sit' (654) 
References: WP. II 486, Schwyzer Gr. Gr. I 679 f., Couvreur H 99 f., Pedersen Hittite 91, 
101, 104, 110. 
Page(s): 342-343 

Root / lemma: eter- 

Meaning: intestines 

Material: Gr. hom. nrop n. "heart' (Gen. p£yaA-nTopo(; etc., Aeolic form for *etr, *nTap); 

nrpov "belly, lower abdomen'; 



Old Norse ^dri. "vein' {*eter, through misinterpretation of -/'transferred as nominative *- 
zin the /-Deki., Dat. Akk. sed/, PI. ^d/'r, ^dar). Old English aedre, aederi. "vein', PI. also " 
kidneys', Old High German ad{a)ra. Middle High German ader, adre\e\n, sinew; PI. 
intestines, entrails ', with /nn{a) " inside ', (under the influence of common Celtic -ns-, -nt- > 
-nn-), clustered together Old Franconian inn-ethron<^\. "fat, lard, grease; intestine fat'. Old 
Saxon ut-innathrian^ 6\se'r(\ba\Ne\, remove the entrails from', besides an older composition 
with //7"in' and stress shift *oin Old High German (with suffix exchange) inuodilT intestine, 
entrails '; 

the fact that also Old Irish inathar^ intestine, entrails ' are deducible from *en-dtro-, is 
but barely doubtful; it would have received * enathar {irom *en-dtro) through influence of 
the preposition in- being /; about acymr. permed-interedou q\. "that part of the abdomen 
which extends from the lowest ribs to the pubes, the groin, flank', mcorn. en-eder-en^ the 
chief internal organs of the body, significant organs ' s. Loth RC 42, 369; mcorn. -eder- 
could go back to *-dtro-, against which acymr. word could belong to preposition * enter. 

from here Avestan x^a&ra-^ moments of joy, cheerfulness, contentment ' as *su-atra-l 

References: WP. I 117, Schwyzer Gr. Gr. I 519, Meillet Et. 167 f., Specht Dekl. 81. 
Page(s): 344 

Root / lemma: etT- 

Meaning: diver, a k. of bird (of waterfowl?)
```


## [2026-09-05T20:31:52.545Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"Root / lemma: eti\\|Root / lemma: eu-\\|Root / lemma: euə\\|Root / lemma: eu̯ə\" POK_full.txt | head -20"
}
```


### [2026-09-05T20:31:52.608Z] TOOL RESULT

```
28918:Root / lemma: eu-2 
28961:Root / lemma: eu-3, with present formants -et- : yet-, ut- 
28980:Root / lemma: eu-4
```


## [2026-09-05T20:32:14.598Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^Root / lemma: eti\\|^Root / lemma: et\" POK_full.txt | head -20\necho \"=== page 344/345 markers ===\"\ngrep -n \"^Page(s): 344\\|^Page(s): 345\\|^Page(s): 344-345\" POK_full.txt | head"
}
```


### [2026-09-05T20:32:14.664Z] TOOL RESULT

```
28778:Root / lemma: et(e)n- 
28794:Root / lemma: et/ 
29467:Root / lemma: eter- 
29498:Root / lemma: etT- 
29526:Root / lemma: et-men- 
29542:Root / lemma: etro- 
=== page 344/345 markers ===
28830:Page(s): 344 
28914:Page(s): 345-346 
29496:Page(s): 344 
29524:Page(s): 345 
29540:Page(s): 345 
29561:Page(s): 345
```


## [2026-09-05T20:32:17.136Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '28794,28835p' POK_full.txt\necho \"======= etro / etmen =======\"\nsed -n '29498,29565p' POK_full.txt"
}
```


### [2026-09-05T20:32:17.206Z] TOOL RESULT

```
Root / lemma: et/ 

Meaning: out; further, etc.. 

Material: Old Indie at/'m. Akk. "about - out, against', prefix a//(Avestan a/'t/-, Old pers. at/y-) 

" over-, back-' (contains also part Indo Germanic at/-, see above S. 70 f.); 

Phrygian sti in sti-tetikpsvoc; " curses ' (to Old Irish tong/d^ swears'); 

gr. £Ti " moreover, further, still '; 

perhaps Messapic -0i "and' (Krahe KZ. 56, 1 35 f., compare WH. I 863); : alb. edhe "and'. 

Latin e/"and also', Paelignian Umbrian e/ds.; Latin et-/am'an6, also, still'; 

gall. e//"also, further', e//-c"and also' {*eti-Re)\ in abret. et-binam<^\. lanis, acymr. et-met 
" to beat back, blunt, dull ' (Loth RC 37, 27); 

Gothic /^"but, 5£' (an 1. place), prefix id- in id-weitv\. "disgrace, shame, insult' = Old 
English Old Saxon edwTt, Old High German ita-, itwTz6s. (Old High German H{a), Old 
Norse /(?- "again'. Old English Old Saxon e^/- "again', besides Old High German ith-. Old 
English ed-, Jacobsohn KZ. 49, 194, yet is Old English ed- after Sievers-Brunner 165'' only 
spelling mistake), perhaps also in Gothic id-reigai. " repentance, penance, atonement' 
(compare Feist 289 f.); 



Old Prussian e/- besides at-, probably as acymr. etc. et- besides at- (to ati above S. 70), 
different Trautmann 16; 

about Tocharian A 5/55 "from here' (?), A aci, B ecce "from there' {*et}) compare Van 
Windekens Lexique 8, 16, Pedersen Tocharian Sprachg. 16''. 

References: WP. I 43 f., WH. I 421 f., the e//in e- (see above S. 283) and -//(as in au-ti 
above S. 74, etc.) zerlegen will. 
Page(s): 344 

Root / lemma: euk- 

Meaning: to be used to 

======= etro / etmen =======
Root / lemma: etT- 

Meaning: diver, a k. of bird (of waterfowl?) 

Note: 

Root/ lemma: eff-: "diver' derived from the abbreviated Root/ lemma: anat-: "duck' 

Material: 

Maybe Old Indie: ati-, aftf. "an aquatic bird' : Other Iranian: Sak ace, aci "waterfowl', 

Osset occ "wild duck', Pamir Wakh. yoc "duck' : Greek: cbric; , iboc,, n, ( [oui;] ) A. bustard, 

Otis tarda, X.An.1.5.2sq., Arist.HA 509a4, al., Ael.NA5.24, Opp.C.2.407; cf. ouTi(;, oriq. 

Old Norse aedri. (Gen. aedar), sedarfugl, out of it engl. Dutch Modern High German eider, 

Norwegian cerfug/{and sefugl); Swedish ada, dial. ao'"eiderduck'. Perhaps with Old Indie 

atf-, atr a water-bird ' in connection to present. However, see below anat-' duck ' (see 41 

f.). 

References: WP. 1118, Kluge^^ s. v. Eider 

Page(s): 345 

Root / lemma: et-men- 
Meaning: breath, *soul, wind 



Material: Old Indie atman-, Gen. atmanahxw. "breath, breeze, soul'; 

Old English ^dmrr\.. Old Saxon athum'breeze, breath'. Old High German adhmot 
(Isid.) " flat ', otherwise in Old High German m. gramm. variation atum{= adum\s\6.) m. 
"breath'. Modern High German Atem and (with dial, ofrom a) Odem. 

from here Irish athach {*at-ako-) "breath, breeze, wind'? 

References: WP. I 118. 
Page(s): 345 

Root / lemma: etro- 
Meaning: hurried, swift 
Note: 

Root/ lemma: etro-\ "hurried, swift' derived from Root/ lemma: at(e)r-\ fire' 
Material: Old High German atar{*etr6-) "keen-scented; acute, sharp, perceptive, swift, 
fleet, quick, speedy'. Old English ^oVie 'immediately, forthwith, at once, right away, 
instantly, now, fully, totally, completely'. Old Frisian edre. Old Saxon adro6s., Old 
Icelandic adr'early, matutinal, before, previously, in the preceding time, at an earlier time' 
one places (in ablaut) to Latvian a//'s"rash, hasty, violent, stormy, hot tempered' {*atro-), 
Lithuanian dial, o/^ "quick, fast', Latvian afri Adv. 6s., afruma^\n the haste, hurry, in the 
heat'; North Lithuanian a/ms "violent, stormy, hot tempered, irascible, irritable', atre{/) Adv. 
ds. and "quick, fast' could be borrowed from Latvian. 

The supposed ablaut e: 5 nevertheless, is doubtful lengthened grade; also the 
vocalism of Tocharian A atar, B etar'hero', whether correct, is unclear; compare Van 
Windekens Lexique 23; Baltic forms could moreover belong to af{ejr-l\re' (above S. 69). 

References: WP. 1118, Trautmann 203, MiJhlenbach-Endzelin Latvian-D. Wb. I 245. 
Page(s): 345 

Root /lemma: euA'^-, du6^- m^- 

Meaning: udder
```


## [2026-09-05T20:32:26.007Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '28840,28920p' POK_full.txt"
}
```


### [2026-09-05T20:32:26.095Z] TOOL RESULT

```
" accustomed ' (with secondary/-), Meillet BSL. 23, 76; 

Armenian usan/m {k aiter ^palatalized) "learn, I am accustomed'; 

gr. £Kr|Aoc; (Pind. zmkoq) besides £UKr|Ao(; "in unobstructed pleasure '; maybe from uek-, 
respectively euk-7 

Old Irish to-ucc-' understand, comprehend, conceive ' {cc= gg) from * u-n-k-\ whereas 
go ro-uicc^ has carried ', do-uicc^ has brought ' to *-onk-i-s-t {back to eneR-, see above S. 
317); 

Gothic bf-uhts{*unkto-) " habitual, customary '; 

Lithuanian yi//7/rs/i/,y^/7/r//" become habitual, customary \jaukus^ accustomed to 
people, tamed, domesticated', ya^/r//?//' accustom, tame' , Junktas ' accustomed '; Latvian 
Jukt' become accustomed, habitual, customary \jaukt,Jaucet' accustom '; Old Prussian 
Jaukint^ train, practice '; Lithuanian ukis^ farmstead ' (actually "dwelling', compare Old 
Indie dkas6s.)\ toy- see below eu-3. 

Old Church Slavic ^c///" instruct, teach', ^/rt "doctrine', vykngt/"be accustomed '; 

References: WP. Mil, Trautmann 335, Kuiper Nasalpras. 187 with Anm. 
Page(s): 347 

Root /lemma: eu-1, eua-\ ua- ua-{**hue-) 
Meaning: to lack; empty 



Note: esp. in partizipialen /70-formations 

Material: Old Indie una-, Avestan una-^ insufficient, inadequate, lack, be short of, Avestan 
uyamna6s. (participle present Med. to present u-ya-)\ npers. {*gvang) vang^ empty, bare, 
lacking, poor, needy', pamir vanao^ Leerheit, vanity, pride '; 

The origin of labialized Old laryngeals: 

common Celtic *hue- > gw- > f- ; Armenian Old Indie gw- > u-. 

Armenian unain' empty, bare, lacking' (Indo Germanic u)\ 

gr. £uvi<;, -i5o(; " stolen; looted, lack, be short of; about gr. £t6(;, (F)£tu)oioc;, that could 
also belong here, see above S. 73; 

The origin of labialized Old laryngeals: 

common Celtic Greek *hue- > gw- > f- ; Gothic Latin Lithuanian gw- > w-, v-. 

perhaps here Latin i/a/7^5"bare, lacking, containing nothing, empty, void, vacant '; very 
dubious (because the /r-extension is attested only in Ital.) vaco, -are^ be empty, be void, 
be vacant, be without, not to contain ' (besides voco, -are EM^ 1069); Umbrian vagetum, 
uasetom ' make faulty, injure, spoil, mar, taint, corrupt, infect, vitiate, defile ', antervakaze, 
anderuacose^ a breaking off, intermission, interruption, discontinuance ', uas^ a fault, 
defect, blemish, imperfection, vice '; 

Gothic {*gwans) wans' lacking, missing, wanting ' {*u-ono-s or *u9-no-s). Old Icelandic 
van-r. Old Frisian Old English Old Saxon Old High German wan6s.\ 

after Muhlenbach-Endzelin IV 462 here Lithuanian vahs-kariaT unincubated eggs ', 
Latvian vans-kar(i)s' infertile, not fertile egg' (with s-/rfrom s-fS). 

cognitional seems uasto-s' deserted, abandoned, forsaken ' in: 

Latin vastus' empty, unoccupied, waste, desert, devastated ' = Old Irish fas' empty, 
bare, lacking', fasach' desert, waste, wasteland ', Old High German wuosti" deserted, 
abandoned, forsaken, unbebaut, empty, bare, lacking, waste, desolate ', Old Saxon wosti. 
Old English w-este' waste, desolate ' (Middle High German nengl. waste' desert, waste, 
wasteland ' but from Latin). 

Maybe alb. it'os/? 'empty' from Turkish ,6*05 'empty'. 



References: WP. I 108 f., Feist 550. 
Page(s): 345-346 



Root / lemma: eu-2 

Meaning: to put on
```


## [2026-09-05T20:32:44.481Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD eue ===\"\ngrep -n -i \"eu[əa]-\\|^eu-\\|vacate.*vain\\|wane.*want.*waste\" AHD_watkins1985.txt | head -30"
}
```


### [2026-09-05T20:32:44.528Z] TOOL RESULT

```
=== AHD eue ===
222:sta-. V. Zero-grade extended root *sti- (< *stuo) . . . VI. Secondary full-grade form *“steua-...
449:eu-!
466:eu-'. To dress. 1. Latin induere, to don (ind-, variant of
467:eu-?
469:eu-?. Lacking, empty. Extended forms *eua-, *wd-, *wa-. 1. Suffixed form *wo-no- in: a. Germanic *wanén in Old English wanian, to lessen, and wana, lack: WANE; b. North Germanic *wanatdn in Old Norse vanta, to lack: WANT. 2. Suffixed form *wd-no- in Latin vanus, empty: VAIN, VANITY, VAUNT; EVANESCE, VANISH. 3. Ex- tended form *wak- in Latin vacdre (variant vocdre), to be empty: VACANT, VACATE, VACATION, (VACUITY), VAC- UUM, VOID; (AVOID), (DEVOID), EVACUATE. 4. Extended and suffixed form *wds-to- in Latin vdstus, empty, waste (> vdstdre, to make desolate): WASTE; DEVASTATE. [Pok. 1. eu- 345.]
943:(s)keu-. To cover, conceal. Zero-grade form *(s)ku-. Variant *(s)keua-, zero-grade form *(s)kua-, contracted to *(s)kii-. 1. Suffixed basic form in Germanic *skeu-jam, cloud (“cloud cover’), in Old Norse sky, cloud: sky. 2. Zero-grade form *skd- in: a. suffixed form *ski-mo- in Germanic *skiimaz, foam, scum (< “that which covers the water’), in (i) Old High German sciim, scum (> German Schaum, foam): MEERSCHAUM (ii) Middle Dutch schiim, scum: SCUM; Db. suffixed form *ski-ro- in Latin obsciirus, “covered,” dark (ob-, away from; see epi): OBSCURE; CHIAROSCURO. 3. Zero-grade form *ku- in: a. suffixed form “ki-ti- in Germanic *hidiz in Old Eng- lish Ayd, skin, hide: HIDE?; b. suffixed form *ku-ti- in Latin cutis, skin: CUTANEOUS, CUTICLE, CUTIS; CUTIN; c. possibly suffixed form *kd-lo- in Latin cilus (> French cul), the rump, backside: CULET, CULOTTES; BASCULE, RECOIL; d. suffixed form *ku-to- in Greek kutos, a hollow, vessel: -cyTE, cyTo-. 4. Extended zero-grade form *kus- in: a. Germanic *huson- in Old English hosa, hose, covering for the leg: HOSE; b. suf- fixed form *kus-dho- (or suffixed extended form *kudh- to-) in Germanic *huzdam in Old English hord, stock, store, treasure (< “thing hidden away”): HOARD; c. Rus- sian kishka, gut (< “sheath”), akin to the Slavic source of Yiddish kishke, kishke: KISHKE. 5. Suffixed extended zero-grade form *kut-no- in Latin cunnus, vulva (< “sheath”): CUNNILINGUS. 6. Extended root *keudh- in: a. Germanic suffixed lengthened zero-grade form *hiid- Jan in Old English hydan, to hide, cover up: HIDE}; b. Germanic suffixed zero-grade form *hid-jdn- in French hutte, hut: HuT. [Pok. 2. (s)keu- 951.] skeubh-. To shove. 1. Germanic *skeuban and derivative lengthened zero-grade form *skdban in: a. Old English sciifan, to shove: SHOVE; b. Old Norse skifa, to push, perhaps akin to the probable Scandinavian scource of SCUFF, SCUFFLE!, 2. Germanic suffixed form *skub-ilé- in: a. Old English scofl, a shovel: SHOVEL; b. Middle Dutch schoffel, schuffel, a shovel, hoe: SCUFFLE?. 3. Ger- manic *skub-, *skuf-, *skup- in: a. Danish skof, jest, teasing, probably akin to the Scandinavian source of Middle English scof, mocking: scoFF; b. possibly (but quite doubtfully) Old English scop, poet (< “jester’): scoP; c. Low German schiiffeln, to walk clumsily, shuffle cards, probably akin to the source of SHUFFLE. [Pok. skeub- 955.] skeud-. To shoot, chase, throw. 1. Germanic *skeutan, to shoot, in: a. Old English scéotan, to shoot: SHOOT; b. Old Norse skj6ta, to shoot: SKEET. 2. Germanic *skutaz, shooting, shot, in: a. Old English sceot, scot, shooting, a shot: sHOT!; b. Old High German scuz, shooting, a shot: scHuss; C. Old Norse skot and Old French escot, contri- bution, tax (< “money thrown down”): SCOT, (SCOT AND Lot). 3. Germanic *skutjan probably in Old English scyttan, to shut (by pushing a crossbar): sHUT. 4. Ger- manic *skutilaz in Old English scytel, a dart, missile: SHUTTLE. 5. Germanic *skautj6n- in: a. Old English scéata, corner of a sail: SHEET?; b. Old English scéte, piece of cloth: SHEET!. 6. Germanic *skut- in Old Norse skita, mockery (< “shooting of words”), akin to the Scandinavian source of scouT*. 7. Germanic “skaut-, perhaps in Old French escoutille, hatchway: SCUTTLE}, [Pok. 2. (s)keud- 956.] skeup-. Cluster, tuft, hair of the head. 1. Germanic *skauf- in Old English scéaf, bundle, sheaf: SHEAF. 2. Possibly Germanic *hupp- in Middle Dutch hoppe, the hop plant (having tuftlike inflorescence): HoP?. [Pok. (s)keup- 956.]
999:nare, to make firm, establish (dé-, thoroughly; see de-): DESTINE; b. Latin obstindre, to set one’s mind on, persist (ob-, on; see epi): OBSTINATE. 8. Suffixed form *séa-tu- in Latin status, manner, position, condition, attitude: STATE, STATISTICS, STATUS. 9. Suffixed form *sto-dhlo- in Latin stabulum, standing place: STABLE. 10. Suffixed form *si-dhli- in Latin stabilis, standing firm: ESTAB- LISH, STABLE!. 11. Suffixed form *sf-td- in Greek -statés, one that causes to stand, a standing: -sTAT; ENSTATITE. III. Zero-grade form *st-, *st()- (before vowels). 1. Reduplicated form *si-sio)- in: a. Latin sis- tere, to set, place, stop, stand: ASSIST, CONSIST, DESIST, EXIST, INSIST, INTERSTICE, PERSIST, RESIST, SUBSIST; b. Greek histanai (aorist stanai), to set, place: APOSTASY, CATASTASIS, DIASTASIS, ECSTASY, EPISTASIS, EPISTEMOL- OGY, METASTASIS, PROSTATE, SYSTEM; Cc. Greek histos, web, tissue ( < “that which is set up”): HISTO-; HISTIO- cyTE. 2. Compound form *iri-st-i-, “third person stand- ing by” (see trei-). 3. Compound form *por-st-i-, “that which stands before” (*por-, before, forth; see per’), in Latin postis, post: PosT!. 4. Suffixed form *st-o- in compound *upo-st-o-, “one who stands under” (see upo). IV. Extended root *std@u- (< *staau-), becoming *stau- before consonants, *stdw- before vowels; basic meaning “stout-standing, strong.”’ 1. Suffixed extended form *staw-d in Germanic *st6w6 in Old English stéw, place: stow. 2. Probable o-grade suffixed extended form *stow-yad in Greek stoa, porch: STOA, STOIC. 3. Suffixed extended form *stau-ro- in: a. (i) Latin instaurdre, to restore, set upright again (in-, on; see en): STORE; INSTAURATION (ii) Latin restaurdre, to restore, rebuild (re-, anew, again; see re-): RESTORE; b. Greek stauros, cross, post, stake: STAUROLITE. 4. Variant *tau-ro-, bull (see tauro-). V. Zero-grade extended root stii- (< *stua-). Suffixed form “*sti-lo- in Greek stulos, pillar: STYLITE; AMPHISTYLAR, ASTYLAR, EPISTYLE, HYPOSTYLE, PERI- STYLE, PROSTYLE, STYLOBATE. VI. Secondary full-grade form *steua-. Suffixed form *steua-ro- in Sanskrit stha- vira-, thick, stout, old: THERAVADA. VII. Variant zero-grade extended root *stu-. Suffixed form *stu-t- in Old English stuthu, studu, post, prop: STUD'. VIII. Sec- ondary full-grade form *steu-. 1. Suffixed form *steu-raé in Germanic *steur6, “a steering,” in Old English stéor, a steering: STARBOARD. 2. Germanic denominative *steur- Jan in: a. Old English stieran, to steer: STEER}; b. Old Norse styra, to steer, with its derivative stjérn, a rudder, a steering, akin to the possible source of Middle English sterne, stern of a boat: STERN?. 3. Suffixed form *steu-ro-, a larger domestic animal, in Germanic *steu- raz, ox, in Old English stéor, steer: STEER?. 4. Probably Germanic diminutive *steur-ika- in Old English stirc, stierc, calf: sTIRK. See stak-. [Pok. std- 1004.]
1026:Middle Dutch stuyver, stiver: STIVER. II. Extended form *steud-. 1. Nasalized form *stu-n-t- in Germanic *stunt- jan in Old English styntan, to dull: stinT!. 2. Germanic *staut- in: a. Old High German stézan, to push: sTOss; b. Middle Low German and Middle Dutch stéten, to force, akin to the source of Middle English stutten, to stutter: sTUTTER. III. Extended form *steug-. 1. Ger- manic *stukkaz in: a. Old English stocc, tree trunk: stock; b. Old High German stoc (> German Stock), staff: ALPENSTOCK; Cc. Old French estoc, rapier, sword point: TUCK’, 2. Germanic *stukkjam in: a. Old High German stukki, crust, fragment, covering: SHTICK; b. Italian stucco, stucco: stucco. 3. Germanic *stok- in Dutch stoken, to poke, thrust: sTOKER. IV. Suffixed (stative) zero-grade extended form *stup-é- in Latin stupére, to be stunned: STUPENDOUS, STUPID; STUPEFY. V. Suffixed (stative) extended zero-grade form *stud-é- in Latin *studére, to be diligent (< “to be pressing for- ward”): STUDENT, STUDY. VI. Extended zero-grade form *stug- in Greek Stux, the river Styx (< “hatred”): Styx. VII. Variant zero-grade form *tud-. 1. Latin tudes, ham- mer: TOIL!. 2. Suffixed form *tud-ti- in Latin tussis, cough: TussIs. 3. Nasalized form *tu-n-d- in Latin tun- dere, to beat: CONTUSE, OBTUND, PIERCE, RETUSE. VIII. Variant zero-grade form *tup-. 1. Suffixed form *tup-o- in Greek tupos, a blow, mold, die: TYPE; ANTI- TYPE, ARCHETYPE. 2. Nasalized form *tu-m-p- in Greek tumpanon, drum: TYMPANUM. [Pok. 1. (s)teu- 1032.] steu(e)-. To condense, cluster. Possible root. 1. Extended form *stip- in: a. Greek stuppé, tuft, tow: STOP, STUPE; b. Sanskrit stipah, tuft of hair, crown of the head: STUPA. 2. Extended form *stibh- in Greek stuphein, to contract: sTYPTIC. [Pok. steua- 1035.]
1328:CABARET kamer- CABEZON kaput CABLE kap- CABRILLA kapro- CABRIOLET kapro- CACHE ag- CACHEXIA segh- caco- kakka- CACODYL kakka- CACOETHES kakka-, s(w)e- CACOPHONOUS bha-2, kakka- CACOPHONY kakka- CACUMINAL keu-2 CADASTER  steigh- CADAVER kad- CADELLE kat-1 CADENCE kad- CADENT kad- CADET kaput CADRE kWetwer- CADUCEUS kar-2 CADUCICORN kad-, ker-1 CADUCOUS kad- CAECILIAN kaiko- CAECUM kaiko- CAELUM_ kae-id- CAESURA kae-id- CAGE keua-2 CAHIER kWetwer- CAINOTOPHOBIA ken-3 CAIRD kerd-2 CAISSON kap-
2087:PHYLACTERY phulax PHYLAXIS phulax PHYLE bheue- PHYLETIC bheue- -PHYLL bhel-3 PHYLLO- bhel-3 PHYLLOCLADE kel-1 -PHYLLOUS bhel-3 PHYLLOXERA ksero- PHYLOGENY bheua- PHYLUM bheue- PHYSIC bheue- PHYSIO- bheue- PHYSIOGNOMY gn6- PHYSIQUE bheue-_ PHYSOSTIGMINE pu-1 PHYSOSTOMOUS_ pu-! -PHYTE bheue- PHYTO- bheue- PHYTON bheue- PIACULAR pius PIANO? pele-2 PIANOFORTE bhergh-2 PIAZZA plat- PIBROCH pipp- PICA2 (s)peik- PICARO (s)peik- PICE ped-1 PICEOUS_ pik- PICKET (s)peik- PICOLINE pik- PICRO- peig-1 PICTOGRAPH peig-1 PICTOR peig-! PICTURE peig-1 PICTURESQUE peig-', (s)peik- PIE? (s)peik-
2143:PURBLIND bhel-' PURCHASE per! PURE peue- PURFLE gWhi- PURGE peue- PURITAN peua- PURLOIN del-1 PURPORT per-2 PURSE bursa PURSLANE porko- PURSUE sekw-1 PURULENT pu-2 PUS pu-2
2199:ROOF kropo- ROOK! ker-2 ROOM reua- ROOST kred- ROOT! wrad- ROOT? wrdd- ROPE rej-1 RORQUAL = reudh-1, (s)kWal-o- ROSE! wrod- ROSEMARY ers-2 ROSTRUM_ réd- ROTA ret- ROTARY ret- ROTATE ret- ROTE? reu-! ROTE3 krut- ROTIFORM ret- ROTOGRAVURE ret- ROTUND ret- ROTUNDA ret- ROUGE reudh-1 ROUGH ruk-2 ROULETTE ret- ROUND! ret- ROUND? riino- ROUT! reup- ROUTS = reu-1 ROUX reudh-1 ROVER reup- Row! rej-1
2273:SNIFF snu- SNIP snu- SNIVEL snu- SNOOP snu- SNORE sner- SNORKEL sner- SNORT sner- SNOT snu- SNOUT snu- SNOW sneig’h- SNUB snu- SNUFF! snu- SNUFFLE snu- SNUG! kes-1 sO swo- SOAK seua-2 sOAP_ seib- SOAVE swad- SOBER s(w)e- SOCIABLE sekw-1 SOCIAL sekw-1 SOCIETY sekw-1 SOCIO- sekw-1 SOCKET sU- SODALITY s(w)e- SODDEN seut- SOIL! sed-1 som? si- SOIREE sé@-2 SOJOURN deiw- SOKE sag- sol’ sawel-
2276:SoL sdwel- SOLACE sel-2 SOLANINE sAwel- SOLAR sawel- SOLARIUM sawel- SOLE! sel-1 SOLE? s(w)e- SOLEMN sol- SOLICITOUS_ kei-3, sol- SOLID sol- SOLILOQUY s(wW)es, tolkw- SOLIPSISM s(w)e- SOLITARY s(w)e- SOLITUDE s(w)e- SOLO s(w)e- SOLSTICE sawel- SOLUBLE leu-1 SOLUM sel-1 SOLUTE leu-1 SOLVE leu-! SOMA teue- SOMATO- teua- SOME sem-! -SOME! sem-1 -SOME2  teue- SOMERSAULT sel-4, uper SOMNI swep-! SOMNOLENT swep-! SON seue-! SONANT swen- SONATA swen- SONE swen- SONG sengWh- SONIC swen- SONNET swen- SONOROUS swen- sooT sed-1 SOOTH es- SOOTHE es-
2412:TROTH deru TROUBLE twer-1 TROUGH deru TROVER trep-2 TROW deru TRUANT tere-1 TRUCE deru TRUCK! dhregh- TRUCKLE dhregh- TRUCULENT tera-2 TRUE deru TRUFFLE teua- TRUNCATE tere-2 TRUNK tera-2 TRUST deru
2444:VACANT eu-2 VACATE eu-2 VACATION eu-2 VACCINE wak- VACUITY eu-2 VACUUM eu-2 VADOSE wadh-2 VAGINA wag- VAIL! wel-3 VAIN eu-2
```


## [2026-09-05T20:32:45.637Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD eti ===\"\ngrep -n -i \"et cetera\\|eddy\" AHD_watkins1985.txt | head -20\necho \"=== AHD eti root ===\"\ngrep -n \"^eti\\|\\beti\\b\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-05T20:32:45.702Z] TOOL RESULT

```
=== AHD eti ===
463:eti. Above, beyond. 1. Germanic *ith- in Old Norse idha, whirlpool: EDDY. 2. Latin et, and (< “furthermore”): ET CETERA. [Pok. efi 344.]
642:h. Anglo-Norman aloper, to run away from one’s hus- band with a lover: ELOPE. kneigwh-. To lean on. 1. Latin cdnivére (< *con-niguére; com-, together; see kom), “to lean together” (said of eyelids), to close the eyes, be indulgent: CONNIVE. 2. Suf- fixed zero-grade form *knigvh-to- in Latin nictdre, to move the eyelids, wink: NICTITATE. 3. Uncertain preform in Latin niti, to lean forward, strive: NISUS; RENITENT. [Pok. knei-geh- 608.] knid-. Egg of a louse. Suffixed form *knid-d in Germanic *hnito in Old English hnitu, egg of a louse: NIT. [Pok. knid- 608.] ko-. Stem of demonstrative pronoun meaning “this.” I. Variant form *ki-. 1. Germanic *hi- in: a. Old English he, he: HE!; b. Old English him, him: HIM; c. Old English his, his: 1s; d. Old English hire, her: HER; e. Old English Ait, it: 1r. f. Old English hér, here: HERE; g. Old English heonane, heonon, from here: HENCE. 2. Suffixed form “ki-tro- in Germanic *hi-thra- in Old English hider, hither: HITHER. 3. Suffixed form *ki-s in Latin cis, on this side of: cis-. II. Variant form *ke-. 1. Preposed in *ke-etero- (*e-tero-, a second time, again; see i-) in Latin céterus (neuter plural cétera), the other part, that which remains: ET CETERA. 2. Latin -ce (see nu-). III. Attrib- uted by some to this root (but more likely of obscure origin) is Germanic root *hind-, behind. 1. Old English bihindan, in the rear, behind (bi, at; see ambhi): BE- HIND, HIND!. 2. Old High German hintar (> German hinter-), behind: HINTERLAND. 3. Germanic derivative verb *hindron, to keep back, in Old English hindrian, to check, hinder: HINDER}. [Pok. ko- 609.] k6-. To sharpen, whet. Contracted from *koo-. 1. Suffixed extended form “kooi-no- in Germanic *haind in Old English hdn, stone: HONE!. 2. Perhaps Greek kénos, cone, conical object (< “a sharp-pointed object”): CONE. [Pok. Aéi- 541.] kob-. To suit, fit, succeed. Germanic *hap- in Old Norse happ, chance, good luck: HAP, (HAPPEN), (HAPPY); (HAP- LEss), (MISHAP). [Pok. kob- 610.] [kokkos. Kermes berry, pit, grain. Greek noun of un- known origin: COCCID, COCCUS, COCHINEAL; MONO- COQUE.] koksa. Body part. Latin coxa, hip: Coxa, CUISSE, CUSH- ION. [Pok. koksd 611.] kolem-. Grass, reed. Suffixed form *kolsm-o-. 1. Ger- manic “*halmaz in Old English healm, halm, straw: HAULM. 2. Latin cudmus, stalk: CULM!. 3. Zero-grade form “kibpm-o- in Greek kalamos, a reed, straw: CALA- MITE, CALAMUS, CALUMET, CARAMEL, SHAWM. [Pok. kolomo-s 612.] koli-. Glue. Suffixed variant form *koly-a in Greek kolla, glue: COLLAGE, COLLO-, COLLODION; PROTOCOL. [Pok. Rolfeji- 612.] kom. Beside, near, by, with. 1. Germanic *ga-, together, with (collective and intensive prefix and marker of the past participle), in Old English ge-, with, also participial, collective, and intensive prefix: ENOUGH, HANDIWORK, YCLEPT. 2. Latin cum, co-, with: CUM; CONQUIAN. 3. Old Latin com, with (collective and intensive prefix): co-, com-. 4, Suffixed form *kom-trd in Latin contra, against, opposite: (CON!), CONTRA-, CONTRARY, (COUNTER!), COUNTER-, COUNTRY; ENCOUNTER. 5. Suffixed form *kom-yo- in Greek koinos, common, shared: COENO-; CENOBITE, EPICENE, KOINE. 6. Reduced form *ko- (see gher-', mei-', smei-). [Pok. kom 612.] konemo-. Shinbone, bone, Reduced form *kemmo- per- haps in Germanic *hamma in Old English hamm, ham, thigh: HAM. [Pok. konamo- 613.] konk-. To hang. 1. Germanic *hanhan in: a. Old English hon, to hang: HANG; b. Dutch (dialectal) hankeren, to long for; HANKER; ¢C. possibly Middle English he(e)ng, hinge, hinge (ultimately from the base of Old English hangian, to hang): HINGE. 2. Suffixed form *konk-t-d- in
1052:swer-'. To speak, talk. O-grade form *swor- in: a. Ger- manic *swarjan in Old English swerian, to swear, pro- claim: SWEAR; b. Germanic “*and-swar6, “a swearing against,” “rebuttal” (*andi-, against; see ant-), in Old English andswaru, answer: ANSWER. [Pok. 1. swer- 1049.] swer-2. To buzz, whisper. Imitative root. I. O-grade form *swor-. 1. Suffixed form *swor-mo- in Germanic *swar- maz in Old English swearm, swarm: SWARM. 2. Germanic *swar- in Dutch zwirrelen, to whirl, akin to the Low German source of Middle English swyrl, eddy: SWIRL. II. Zero-grade form *sur-. 1. Suffixed form *sur-do- perhaps in: a. Latin surdus, deaf, mute: SORDINO, SOUR- DINE, SURD; b. Latin absurdus, discordant, away from the right sound, harsh (ab-, away; see apo-): ABSURD. 2. Reduplicated expressive form *su-surr- in Latin susur- rus, whisper: SUSURRATION. [Pok. 2. swer- 1049.] swer-3, Post, rod. Suffixed zero-grade form *sur-o- in Latin surus, branch: SURCULOSE. [Pok. 3. suer- 1050.] swer-4. To cut, pierce. Germanic *swerdam in Old Eng- lish sweord, sword, sword: sworD. [Pok. 4. suer- 1050.] swer-5. Also ser-. To lift, hang on the scale; heavy. Variant *ser- in suffixed lengthened-grade form *sér-yo- in Latin sérius, serious, grave: SERIOUS.
1441:EsLis gWela-1 EBULLIENCE beu-! ECBOLIC gWele-1 ECCENTRIC kent- ECCHYMOSIS gheu- ECCLESIA kela-2 ECCRINE krei- ECEsIsS weik-1 ECHARD segh- ECHELON skand- ECHIDNA ang¥hi- ECHINO- ang¥hi- ECHINUS angVhi- ECHO (s)wagh- ECHOLALIA 1a- ECLAIR kelo-2 ECLAIRISSEMENT kelo-2 ECLAMPSIA [ap- ECLECTIC leg-! ECLIPSE leikw- ECLOSION kleu-3 ECOLOGY weik-1 ECONOMY weik-1 ECRU kreue-1 ECSTASY sta- ECTO- eghs ECTOSARC twerk- ECU skei- ECUMENICAL welk-1 ECZEMA yes- EDACIOUS ed- EDAPHIC sed-! EDDY eti EDELWEISS _athal-, kweit- EDEMA oid- EDENTATE dent- EDGE ak-
=== AHD eti root ===
463:eti. Above, beyond. 1. Germanic *ith- in Old Norse idha, whirlpool: EDDY. 2. Latin et, and (< “furthermore”): ET CETERA. [Pok. efi 344.]
1441:EsLis gWela-1 EBULLIENCE beu-! ECBOLIC gWele-1 ECCENTRIC kent- ECCHYMOSIS gheu- ECCLESIA kela-2 ECCRINE krei- ECEsIsS weik-1 ECHARD segh- ECHELON skand- ECHIDNA ang¥hi- ECHINO- ang¥hi- ECHINUS angVhi- ECHO (s)wagh- ECHOLALIA 1a- ECLAIR kelo-2 ECLAIRISSEMENT kelo-2 ECLAMPSIA [ap- ECLECTIC leg-! ECLIPSE leikw- ECLOSION kleu-3 ECOLOGY weik-1 ECONOMY weik-1 ECRU kreue-1 ECSTASY sta- ECTO- eghs ECTOSARC twerk- ECU skei- ECUMENICAL welk-1 ECZEMA yes- EDACIOUS ed- EDAPHIC sed-! EDDY eti EDELWEISS _athal-, kweit- EDEMA oid- EDENTATE dent- EDGE ak-
1477:ERYTHEMA reudh-! ERYTHRO- reudh-1 ESCALADE skand- ESCAROLE ed- ESCHATOLOGY eghs ESCHEAT kad- ESCUDO skei- ESCULENT ed- ESCUTCHEON skei- ESOTERIC en ESPARTO sper-2 ESPECIAL spek- ESPERANCE spé-! ESPIONAGE spek- ESPOUSE spend- ESPY spek- ESQUIRE skei- ESSAY ag- ESSENCE es- ESSONITE sék- ESTABLISH sta- ESTANCIA sta- ESTER ak- EsTHER  ster-3 ESTRONE eis-1 ESTRUS eis-1 ESTUARY aidh- ESURIENT ed- ETCETERA eti, ko- ETCH ed- ETERNAL aiw- ETESIAN wet-2 ETHER aidh- ETHIC s(w)e- ETHMOID sé-3 ETHNIC s(w)e- ETHNO- s(w)e- ETHOS s(w)e- ETIOLOGY ai-! ETIQUETTE steig- EU- esu- EUCALYPTUS kel-2 EUCARYOTE kar-1 EUCHARIST gher-5 EUGLENA gel-2 EUMENIDES men-1 EUNUCH segh- EUONYMUS n6-men- EUPATRID peter- EUPEPTIC pekw- EUPHEMISM bha-2 EUPHONY bha-2 EUPHORIA bher-1 EUPHROSYNE gWhren- EUPNEA pneu- EUREKA were-2 EuRUS eus- EURY- were-1 EUuRYDICE deik-, were-1
```


## [2026-09-05T20:33:04.507Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(\"leaves:\",len(pages))\nEOF\ngrep -n \"page_offset\\|lookup_hint\" /dev/null\npython3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nprint(d['KLN']['page_offset']); print(d['KLN'].get('lookup_hint'))\""
}
```


### [2026-09-05T20:33:06.998Z] TOOL RESULT

```
leaves: 903
KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
```


## [2026-09-05T20:33:10.619Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor i in 284 285; do echo \"=== leaf $i ===\"; awk -v n=$i 'BEGIN{RS=\"\\f\"} NR==n+1' KLN_1966.txt | head -60; done"
}
```


### [2026-09-05T20:33:12.428Z] TOOL RESULT

```
=== leaf 284 ===
s).  According to  the  opinion  of  several  scholars  Endymion  was orig.  worshiped  as  a  solar  deity  and  his  name is  a  personification  of  the  Setting  Sun  Sinking into  the  Sea.  See  adytum  and  cp.  Anadyomene. endysis,  n.,  the  act  of  developing  a  new  coat  of hair,  etc.  (biol.)  —  ModL.,  fr.  Gk.  SvSuctk;,  ‘a putting  on’,  fr.  ivSiletv,  ‘to  enter  into;  to  put on’,  fr.  tv  (see  2nd  en-)  and  Sostv,  ‘to  enter; to  put  on’  (lit.  ‘to  enter  into’).  See  adytum  and cp.  ecdysis,  ependyma.  Cp.  also  prec.  word, -ene,  suff.  used  to  form  names  of  unsaturated hydrocarbons  ( chem .)  —  Gk.  -r jvq,  fem.  patro¬ nymic  suff.
Eneas,  masc.  PN.  —  L.  Aeneas,  fr.  Gk.  Alvelai;, lit.  ‘praiseworthy’,  fr.  oIvoq,  ‘tale,  story,  saying; praise'.  See  enigma.
enema,  n.,  injection  of  a  fluid  into,  the  rectum (med.)  —  Late  L.,  fr.  Gk.  SvEpia,  ‘injection, clyster’,  fr.  tviiv 01,  ‘to  throw  in,  send  in’,  fr.  tv (see  2nd  en-)  and  Itvou,  ‘to  send,  throw, project’,  which  stands  for  *yi-ye-nai  and  is  cogn. with  L.  jacere,  ‘to  throw’.  See  jet,  ‘to  spirt forth’,  and  cp.  words  there  referred  to. enemy,  n.  —  OF.  enemi  (F.  ennemi),  fr.  L.  ini- mtcus,  ‘hostile,  unfriendly;  an  enemy’,  fr.  in-, ‘not’,  and  amicus,  ‘friend’.  Cp.  It.  nemico.  Prov¬ en?.  enemic,  Catal.  enamic,  Sp.  enemigo,  Port. inimigo,  which  all  derive  fr.  L.  inimicus,  and see  amicable.  Cp.  also  enmity,  inimical, energetic,  adj.  —  Gk.  4vspy9Tix6i;,  ‘able  to  act upon’,  fr.  IvEpyetv,  ‘to  work,  be  strenuous,  act upon’,  fr.  £vEpfr)?,  later  form  of  £vEpy<k,  ‘at work,  active’.  See  energy  and  -ic.
Derivatives:  energetic-s,  n.  pi.,  energetic-al-ly, adv.,  energet-ic-ist,  n.,  energet-ist-ic,  adj. energumen,  n.,  a  demoniac;  a  fanatic.  —  Late  L. energumenos,  ‘one  possessed  of  the  devil’,  fr. Gk.  IvepyoupLEvo?,  pass.  pres.  part,  of  ivepyEtv, ‘to  act  upon’.  See  energy.  For  the  suff.  see  alum¬ nus  and  cp.  words  there  referred  to. energy,  n.  —  Late  L.  energia,  fr.  Gk.  tvt pysia, ‘energy,  efficiency’,  which  was  formed  by  Aris¬ totle  fr.  ivepyf]?,  later  form  of  £vEpy6q,  ‘at work,  active’,  fr.  tv  (see  2nd  en-)  and  £pyov, ‘work’.  See  ergon  and  cp.  allergy,  anergy. Derivatives:  energ-ic,  adj.  (rare),  energ-ize,  tr. and  intr.  v.,  energ-iz-er,  n. enervate,  tr.  v.  —  L.  enervdtus,  pp.  of  enervdre, ‘to  enervate,  weaken’,  fr.  e-  and  nervus,  ‘nerve, sinew’.  See  nerve  and  verbal  suff.  -ate. enervate,  adj.  —  L.  enervdtus,  pp.  of  enervdre.  See enervate,  v.
enervation,  n.  —  L.  enervatio,  gen.  -dnis,  fr.  ener¬ vdtus,  pp.  of  enervdre.  See  enervate,  v.,  and  -ion. enlace,  tr.  v.,  to  write  (print,  etc.)  on  the  face  (of
enfeeble
enormous
a  document).  —  Formed  fr.  ist  en-  and  face, enfeeble,  tr.  v.  —  OF.  enfeblir,  fr.  ist  en-  and feble,  ‘feeble’.  See  feeble, enfeoff,  tr.  v.,  to  invest  with  a  fief.  —  AF.  enfe- offer,  corresponding  to  OF.  enfeffer,  enfieffer. See  ist  en-  and  feoff,  fief.
Derivative :  enfeoff- merit,  n.
Enfield  rifle.  —  So  called  from  the  factory  in  En¬ field  in  Middlesex,  England,  where  it  was  first manufactured.
enfilade,  n.,  gunfire  sweeping  from  flank  to  flank. —  F.,  fr.  enfiler,  ‘to  thread  (a  needle);  to  en¬ filade’,  fr.  ist  en-  and  fil,  ‘thread’.  See  file, ‘collection  of  papers’,  and  -ade  and  cp.  filament, profile.
Derivative:  enfilade,  tr.  v. enfold,  tr.  v.  —  Formed  fr.  ist  en-  and  fold, enforce,  tr.  v.  —  OF.  enforcier,  enforcer  (F.  en- forcir),  ‘to  strengthen’,  fr.  VL.  *infortidre,  ‘to make  strong’,  fr.  in-  ‘in’,  and  fortis,  ‘strong’. See  force.  Derivatives:  enforce-able,  adj., enforc-ed-ly,  adv.,  enforcement  (q.  v.),  enforc-er,  n. enforcement,  n.  —  OF.,  fr.  enforcer.  See  prec. word  and  -ment.
enfranchise,  tr.  v.,  to  admit  to  citizenship.  —  OF. enfranchiss-,  pres.  part,  stem  of  enfranchir,  fr. i  st  en-  and  franchir,  ‘to  set  free’,  fr.  franc,  fern. franche,  ‘free’.  See  franchise.
Derivatives :  enfranchis-er,  n.,  enfranchise-ment, n.
engage,  tr.  and  intr.  v,  —  F.  engager,  fr.  ist  en- and  gage,  ‘pledge’.  See  gage.
Derivatives:  engag-ed,  adj.,  engage-ment,  n., engag-er,  n.,  engag-ing ,  adj.,  engag-ing-ly,  adv. engender,  tr.  v.  —  F.  engendrer,  fr.  L.  ingenerare, to  implant,  produce,  engender’,  fr.  in-,  ‘in’,  and generare,  ‘to  produce,  engender’.  See  ingener- ate,  v.
Derivatives:  engender-er,  n.,  engender-ment,  n. engine,  n.  —  OF.  engin,  ‘skill;  invention;  ma¬ chine,  engine’,  fr.  L.  ingenium,  ‘nature,  natural disposition,  talent,  ability’,  fr.  in-,  ‘in’,  and  the stem  of  gignere  (perf.  genui),  ‘to  beget’.  See genus  and  cp.  genius,  ingenious.
Derivatives:  engineer  (q.v.),  engin-ery,  n. engine,  tr.  v.  —  Partly  fr.  OF.  enginier,  ‘to  con¬ trive,  invent’,  fr.  ML.  ingeniare,  fr.  L.  ingenium, partly  directly  fr.  engine,  n. engineer,  n.  —  Formed  fr.  engine  with  suff.  -eer. Derivatives:  engineer,  tr.  and  intr.  v.,  engineer¬ ing,  n.
England,  n.  —  OE.  Engla  land,  lit.  ‘land  of  the Angles’ ;  see  next  word  and  land.  For  the  con¬ traction  of  OE.  Engla  land  into  England  see haplology.
Derivative:  England-er,  n.
English,  adj.  and  n.  —  OE.  Englisc ,  Aenglisc, ‘English’,  fr.  Engle,  Angle,  name  of  a  Teutonic tribe  that  settled  in  Britain,  prop,  ‘the  people coming  from  Angul'.  See  Angle  and  adj.  suff.  -ish. Derivatives:  English,  tr.  v.,  English-ry,  n. engorge,  tr.  v.  —  F.  engorger,  ‘to  obstruct,  block ;
522
523
to  congest’  (med.)  See  ist  en-  and  gorge.
Derivative:  engorge-ment,  n. engrail,  tr.  v.,  i)  to  indent  (her.) ;  2)  to  adorn.  - —
ME.  engrailen,  fr.  OF.  engresler  (F.  engreler), fr.  ist  en-  and  gresle  (F.  grele),  ‘hail’,  fr.  greler,
‘to  hail’,  which  is  of  uncertain  origin.
Derivatives:  engrail-ed,  adj.,  engrail-ment,  n. engrain,  tr.  v.,  1)  to  ingrain;  2)  to  grain  in  imi-  «
tation  of  wood.  —  ME.  engreynen,  lit.  ‘to  dye in  grain’,  fr.  OF.  (=  F.)  en  graine ,  ‘in  grain’, fr.  en,  ‘in’  (see  1  st  en-),  and  graine,  ‘seed  of  plants ; cochineal;  scarlet  grain’,  fr.  L.  grana,  pi.  of  gra- num,  ‘grain,  seed’,  which  was  mistaken  for  a  fern, singular.  The  French  language  differentiates between  grain  (fr.  L.  grdnurri),  ‘grain,  berry’ and  graine  (fr.  L.  grana),  ‘seed  of  plants’.
Cp.  also  It.  and  Sp.  grano,  ‘grain’,  grana,  ‘seed of  plants;  cochineal;  scarlet  grain’,  and  see grain.  Cp.  also  ingrain,  which  is  a  var.  of  en¬ grain.
engrave,  tr.  v.  —  Formed  fr.  ist  en-  and  grave,
‘to  carve’.
Derivatives:  engrav-ed,  adj.,  engrave-ment,  n., engrav-er,  n.,  engrav-ing,  n.  j
engross,  tr.  v.,  to  write  in  large  letters.  —  AF.  en¬ grosser,  fr.  F.  en  grosse,  ‘in  large  letter’,  fr.  en,
‘in’  (see  ist  en-),  and  grosse,  ‘large  writing’, prop,  fern  of  gros,  ‘big,  bulky,  thick’,  fr.  Late L.  grossus.  See  gross.
Derivatives:  engross-ed,  adj.  engross-ment,  n. engross,  tr.  v.,  to  monopolize,  absorb.  —  The orig.  meaning  was  ‘to  buy  up  the  whole  of  a commodity’ ;  fr.  F.  acheter  engros,  ‘to  buy  whole¬ sale’,  fr.  en  gros,  ‘in  a  bulk;  wholesale’,  fr.  en,
‘in’  (see  ist  en-),  and  gros,  ‘big,  bulky,  thick’,  fr.
Late  L.  grossus.  See  gross  and  cp.  prec.  word.
Derivatives :  engross-ed,  adj.,  engross-ed- ly,  adv., engross-ing,  adj.,  engross-ing-ly,  adv.,  engross- ing-ness,  n.,  engross-ment,  n. engulf,  tr.  v.  —  Formed  fr.  ist  en-  and  gulf.
Derivative:  engulf-ment,  n. engyscope,  n.,  a  kind  of  microscope  (optics).  —
Compounded  of  Gk.  iyyuc,  ‘near’,  and  -<jx6mov, fr.  raoTreiv,  ‘to  look  at,  examine’.  The  first  ele¬ ment  is  prob.  formed  fr.  b  (see  2nd  en-)  and ♦yiiot,  ‘hand’,  and  lit.  means  ‘that  which  is  at hand’.  Cp.  ^yyuq,  ‘surety,  security,  bail’,  prop.
‘pledge  put  into  one’s  hand’,  which  is  prob.
also  formed  fr.  b  and  *yua.  Gk-  *yua  is  cogn.
with  Avestic  gava,  ‘both  hands’.  Both  these
words  derive  fr.  I.-E.  base  *geu-,  ‘to  bend,  curve,  '
arch’;  see  cove  and  cp.  words  there  referred  to.
For  the  sense  development  of  Gk.  £yyu<;,  ‘near’, lit.  ‘at  hand’,  cp.  L.  comminus,  ‘close  at  hand’,  i
which  is  formed  fr.  OL.  com  (=  L.  cum),  ‘with’, and  manus,  ‘hand’;  cp.  also  E.  at  hand,  G.  vor- handen,  ‘existing’,  lit.  ‘before  the  hands’,  and Heb.  'al  yad,  ‘next  to,  near’,  lit.  ‘on,  or  by,  the  <
hand’.  For  the  second  element  in  engyscope  see -scope.  Cp.  telengy scope, enhance,  tr.  v.,  to  raise,  increase.  —  ME.  en- hauncen,  fr.  AF.  enhauncer,  prob.  a  corruption
of  OF.  enhaucer,  fr.  VL.  *inaltidre,  ‘to  raise’, fr.  in-,  ‘in,  upon’,  and  *altidre,  ‘to  raise’,  fr.  L. altus,  ‘high’.  See  ist  en-  and  alt  and  cp.  hance, hawser.
Derivatives:  enhanc-ed,  adj.,  enhance-ment,  n., enhanc-er,  n.
enharmonic,  n.,  pertaining  to  tones  derived  from different  degrees,  but  practically  of  the  same pitch  (mus.)  —  Late  L.  enharmonicus,  fr.  Gk. £vapp.ovot6?,  evapjjt.ovi.6i;,  ‘musical,  harmonious, enharmonic’,  fr.  b  (see  2nd  en-)  and  apjxovia, ‘harmony’.  See  harmony.
Derivatives:  enharmonic,  n.,  enharmonic-al-ly, adv.
Enid,  fern.  PN.  —  W.,  lit.  ‘soul’  or  ‘purity’, enigma,  n.,  a  riddle,  puzzle.  —  L.  aenigma,  fr. Gk.  atviypa,  gen.  atviyjiaxoi;,  ‘dark  saying, riddle’,  fr.  alvicraEuSm,  ‘to  speak  darkly,  speak in  riddles’,  fr.  alvop,  ‘tale,  story,  saying;  praise; proverb;  riddle’,  which  is  of  unknown  origin. Cp.  Eneas.
Derivatives:  enigmatical)  (q.v.),  enigmat-ist,  n., enigmat-ize,  tr.  v.
enigmatic,  enigmatical,  adj.,  1)  pertaining  to  an enigma:  2)  puzzling.  —  Late  L.  aenigmaticus (whence  also  F.  enigmatique),  fr.  aenigma,  gen. aenigmatis,  fr.  Gk.  cdviypa.  See  prec.  word  and -ic,  resp.  also  -al.
enigmatographer,  n.,  a  maker  of  enigmas.  —  See next  word  and  agential  suff.  -er. enigmatography,  n.,  the  art  of  making  enig¬ mas.  —  Compounded  of  Gk.  amypa,  gen. alvtypiaxot;,  ‘riddle’,  and  -ypatpla,  fr.  ypatpeiv,  ‘to write’.  See  enigma  and  -graphy. enisle,  tr.  v.,  1)  to  place  on  an  island ;  2)  to  make an  island  of.  —  Formed  fr.  ist  en-  and  isle, enjambment,  n.,  the  running  over  of  a  sentence into  the  next  verse.  —  F.  enjambement,  fr.  en- jamber,  ‘to  skip  over’,  fr.  ist  en-  and  jambe,  ‘leg’. See  jamb  and  -ment.
enjoin,  tr.  v.,  1)  to  command;  2)  to  prohibit.  — ME.  enjoignen,  fr.  F.  enjoign-,  stem  of  enjoindre, ‘to  enjoin,  charge,  direct’,  fr.  L.  injungere,  ‘to join,  attach;  to  charge,  impose  upon’,  fr.  in-, ‘in’  and  jungere,  ‘to  join’.  See  join  and  cp.  in¬ junction.
Derivatives:  enjoin-er,  n.,  enjoin-ment,  n. enjoy,  tr.  v.  —  ME.  enjoyen,  fr.  OF.  enjotr,  ‘to enjoy’,  fr.  ist  en-  and  jotr  (F .jouir),  fr.  VL.  *gau- dire,  formed  (with  change  of  conjugation)  fr.  L. gaudere,  ‘to  rejoice,  be  glad’.  Cp.  OProven?. jauzir  (fr.  VL.  *gaudire).  It.  godere  (fr.  L.  gau¬ dere),  ‘to  rejoice’,  and  see  joy.
Derivatives:  enjoy-able,  adj.,  enjoy-able-ness,  n„ enjoy-abl-y,  adv.,  enjoy-er,  n.,  enjoy-ment,  n. enlace,  tr.  v.  —  F.  enlacer,  fr.  L.  inlaqueare,  il- laqueare,  ‘to  ensnare,  entangle',  fr.  in-,  ‘in’  a
=== leaf 285 ===
nd L.  laqueus,  ‘noose,  snare’.  See  lace. Derivative:  enlace-ment,  n. enlarge,  v.  —  ME.  enlargen,  fr.  OF.  enlargier,  en¬ larger,  fr.  1st  en-  and  large,  ‘broad,  wide’.  See large.
Derivatives:  enlarg-ed,  adj.,  enlarg-ed-ly,  adv.. enlarg-ed-ness,  n.,  enlarge-ment ,  n.,  enlarg-er,  n., enlarg-ing-ly,  adv.
enlighten,  tr.  v.  —  Formed  fr.  ist  en- and  lighten. Derivatives:  enlighten-ed,  adj.,  enlighten-ed-Iy , adv.,  enlighten-ed-ness,  n.,  enlighten-ing,  adj., enlighten-ing-ly,  adv.,  enlighten-ment,  n. enlist,  tr.  and  intr.  v.  —  Formed  fr.  ist  en-  and list,  ‘roll,  catalogue’.
Derivatives:  enlist-er,  n„  enlist-ment,  n. enliven,  tr.  v.  —  Formed  fr.  ist  en-,  life  (cp.  the plural  lives)  and  verbal  suff.  -en.
Derivatives:  enliven-er,  n.,  enliven-ing,  adj.,  en- liven-ing-ly,  adv.
en  masse,  in  a  mass,  by  the  bulk,  as  a  whole.  — F.,  fr.  en,  ‘in’,  and  masse,  ‘mass’.  See  ist  en- and  mass,  ‘quantity,  size’, enmesh,  tr.  v.  —  Formed  fr.  1  st  en-  and  mesh  (q.v.) Derivative :  enmesh-ment,  n. enmity,  n.  — -  ME.  enemyte,  fr.  OF.  enemistie,  fr.' VL.  * inimicitatem,  acc.  of  *inimicitas,  cor¬ responding  to  L.  inimicitia,  ‘enmity,  hostility', fr.  inimicus,  ‘enemy’.  See  enemy  and  -ity  and cp.  amity.
ennea-,  combining  form  meaning  ‘nine'.  —  Fr. Gk.  ivvea,  ‘nine’,  which  stands  for  *b\>irx, *4vfx-,  and  is  cogn.  with  OI.  ndva,  L.  novem. Goth,  niun,  OE.  nigon ,  ‘nine’.  See  nine  and  cp. words  there  referred  to.  Cp.  also  ennead. enneacontahedron,  n.,  a  polyhedron  with  ninety faces.  —  Compounded  of  Gk.  *evveoczovtx. ‘ninety’,  and  eSpa,  ‘side,  face’.  *’ Ewedbcovxa  is erroneously  formed  fr.  evvex,  ‘nine’;  the  correct form  is  evevr)>covxa.  See  ennea-  and  -hcdron. For  the  suff.  -xovxa  (in  ’svveaxavxa,  bevr,- hovtx)  see  penteconta-.
ennead,  n.,  a  group  of  nine  things.  —  From  Gk. ^vvea;,  gen.  svvedcSo;,  ‘a  group  of  nine’,  fr.  bnb. See  ennea-  and  -ad.
Derivative:  ennead-ic,  adj. ennoble,  tr.  v.  —  F.  ennoblir.  See  1  st  en-  and  noble. Derivatives:  ennoble-ment,  n.,  ennobl-er,  n.,  en- nobl-ing,  adj.,  ennobl-ing-Iy,  adv. ennui,  n.,  weariness,  boredom.  —  F.,  fr.  OF. enui,  back  formation  fr.  enuier  (F.  ennuyer).  See annoy,  v.  and  n.
Enoch,  masc.  PN.;  1)  the  eldest  son  of  Cain; 2)  the  father  of  Methuselah  (Bible).  —  Late  L. Enoch,  fr.  Gk.  ’Evciy,  fr.  Heb.  HanSkh,  lit.  ‘de¬ dicated,  consecrated’,  fr.  hanakh,  ‘he  dedicated, consecrated’,  whence  also  hanukkdh,  ‘dedicat¬ ion’,  consecration’.  See  Hanukkah. enorm,  adj.,  1)  abnormal  (obsol.)-,  2)  enormous; outrageous  (archaic).  —  F.  enorme,  fr.  L.  endr- mis,  ‘irregular,  unusual,  enormous,  immense’,  fr. e  norma ,  ‘out  of  rule’,  fr.  e,  ‘out  of’  (see  e-),  and norma,  abl.  of  norma,  ‘rule,  pattern’.  See  norm, enormity,  n.  —  F.  enormite,  fr.  L.  enormitatem, acc.  of  enormitas,  ‘hugeness,  vastness',  fr.  endr- mis.  See  prec.  word  and  -ity. enormous,  adj.  —  Formed  with  suff.  -ous  fr.  L. enormis.  See  enorm.
tnos
524
525
enthetic
Derivatives :  enormous-ly,  adv, ,  enormous-ness ,  n. Enos,  masc.  PN. ;  in  the  Bible,  son  of  Seth.  — Gk.’Evco?,  fr.  Heb.  EnSsh ,  lit.  ‘man’,  rel.  to  Heb. nashtm,  ‘women’,  ish  (for  insh),  ‘man’,  Arab. ins  (coll.),  ‘men,  people’,  and  prob.  also  to Arab,  anisa,  ‘he  joined,  was  friendly’,  Akkad. eneshu,  to  unite,  join  (intr.) enough,  adj.  —  ME.  inogh,  enogh,  enouh,  fr.  OE. genoh,  rel.  to  OS.  ginog,  ON.  gnogr,  Swed.  nog, Dan.  nok,  OFris.  enoch,  Du.  genoeg,  OHG.  ginu- og(i ),  MHG.  genuoc,  G.  genug,  Goth,  ganohs, ‘enough’,  OE.  geneah,  OHG.  ginah,  Goth .ganah, ‘it  suffices’,  fr.  I.-E.  base  *enek-,  *nek-,  *nk-,  ‘to reach,  attain,  carry’,  whence  also  OI.  asndti, Avestic  ashnaoiti,  ‘reaches,  arrives  at’,  OI.  na- sati,  Avestic  nasaiti,  ‘reaches’,  OI.  drpsah, ‘portion,  part’,  Avestic  qsa-,  ‘party’,  Hitt,  nakish, ‘heavy’,  nikzi,  ‘rises’,  ninikzi,  ‘lifts,  raises’,  Gk. Jv-eyxeiv,  ‘to  bear,  carry’,  Srqvejo)?,  Att.  Siocve- y.ric,  ‘continuous,  unbroken’  (which  are  prob.  a contraction  of  *§ta-Tr)vexir)q  and  lit.  mean  ‘capa¬ ble  of  being  carried  through’,  fr.  8ia,  ‘through’, and  4veyxstv,  ‘to  carry’),  Syxo?,  ‘bulk,  size,  mass, body’,  L.  nancisci  (for  na-n-c-isci),  perf.  nactus sum,  ‘to  reach,  obtain’,  OSlav.  nesg,  nesti,  Lith. nesu,  nHsti,  Lett,  nesu,  nest,  ‘to  bear,  carry’, Lith.  nastd,  ‘burden’,  and  perh.  also  Toch.  A ents-,  B  enk-,  ‘to  seize,  take’.  Cp,  onco-,  ‘bulk, size’.
Derivatives :  enough,  n.  and  adv. enounce,  tr.  v.,  i)  to  state  publicly;  2)  to  utter.  — F.  enoncer,  fr.  L.  enuntiare,  ‘to  divulge,  disclose, report,  say,  declare’,  fr.  e-  and  nuntiare,  ‘to  an¬ nounce,  declare’,  fr.  nuntius,  ‘messenger’.  See nuncio  and  cp.  enunciate.  Cp.  also  announce and  words  there  referred  to.
Derivative:  enounce-ment,  n. enow,  adj.  n.  and  adv.,  enough.  —  ME.  inowe; an  archaic  var.  of  enough, en  passant,  by  the  way.  —  F.,  lit.  ‘in  passing’,  fr. en,  ‘in’  and  passant,  pres.  part,  of  passer,  ‘to pass’.  See  1st  en-,  pass  and  -ant. enquire,  enquiry.  —  See  inquire,  inquiry, enrage,  tr.  and  intr.  v.  —  OF.  (=  F.)  enrager, formed  fr.  1st  en-  and  rage,  ‘rage,  fury’.  See rage.
Derivatives:  enrag-ed,  adj.,  enrag-ed-ly,  adv., enrag-ed-ness,  n.
enrapt,  adj.,  enraptured.  —  Formed  fr.  1st  en- and  rapt;  introduced  by  Shakespeare, enrapture,  tr.  v.  —  Formed  fr.  1st  en-  and  rapture. Derivative:  enraptur-er,  n. enravish,  tr.  v.  —  Formed  fr.  1st  en-  and  ravish, enregister,  tr.  v.  —  F.  enregistrer,  ‘to  enter  into  a register’,  fr.  1st  en-  and  registre.  See  register. Derivatives:  enregistr-ation,  n.,  enregistr-y,  n. enrich,  tr.  v.  —  F.  enrichir,  formed  fr.  1st  en- and  riche,  ‘rich’.  See  rich.
Derivatives:  enrich-er,  n.,  enrich-ing,  adj.,  en¬ rich- ing-ly,  adv.,  enrich-ment,  n. enroll,  enrol,  tr.  v.  —  ME.  enrollen,  fr.  OF.  en- roller  (F.  enroler),  ‘to  enter  into  a  roll,  enroll’.
which  is  formed  fr.  1st  en-  and  OF.  rolle  (F. role).  See  roll,  v.  and  n.,  and  cp.  role. Derivatives:  enroll-ed,  adj.,  enroll-er,  n.,  en¬ rollment  (q.v.)
enrollment,  enrolment,  n.  —  F.  enrolement,  fr. enroler,  to  enroll’.  See  enrol  and  -ment. en  route,  on  the  way.  —  F.,  fr.  en,  ‘in,  on’,  and route,  ‘road,  way,  route’.  See  1st  en-  and  route, ens,  n.,  being;  entity  ( philos .)  —  Late  L.  ens  (gen. ends),  back  formation  fr.  est,  ‘is’.  See  esse  and cp.  entity  and  the  third  word  in  dolce  far  niente. ensample,  n.,  an  example  {archaic.)  —  ME.  en- sample,  fr.  OF.  ensample,  a  var.  of  essample, fr.  orig.  example,  exemple.  See  example  and cp.  sample.
ensanguine,  tr.  v„  to  stain  with  blood.  —  Formed fr.  1st  en-  and  L.  sanguis,  gen.  sanguinis,  ‘blood’. See  sanguine.
ensconce,  tr.  v.,  to  conceal.  —  The  original  mean¬ ing  was  ‘to  cover  with  a  fort’.  See  1st  en-  and sconce.
ensemble,  n.,  the  whole.  —  F.,  ’together’,  fr.  L. insimul,  ‘at  the  same  time’,  which  is  formed  fr. in-,  ‘in’,  and  simul,  ‘at  the  same  time,  together’. See  simultaneous  and  cp.  assemble, enshrine,  tr.  v.  —  Formed  fr.  ist  en-  and  shrine, ensiform,  adj.,  sword-shaped.  —  Compounded of  L.  ensis,  ‘sword’,  and  forma,  ‘form,  shape’. The  first  element  stands  for  *qsis  and  is  cogn. with  OI.  asih,  ‘sword,  butcher's  knife’.  For  the second  element  see  form,  n. ensign,  n.,  1)  a  flag;  2)  in  the  United  States  Navy, a  commissioned  officer  of  the  lowest  rank.  — OF.  (=  F.)  enseigne,  fr.  L.  insignia,  pi.  of  in- signe,  ‘mark,  sign,  badge  of  office’,  prop.  neut. of  insignis,  ‘remarkable,  noted,  distinguished’, but  mistaken  in  Vulgar  Latin  for  a  fern.  sing, noun.  L.  insignis  is  formed  fr.  in-  ‘in’,  and  sig- num,  ‘mark,  sign’;  see  sign  and  cp.  insignia.  Cp. also  It.  insegna,  OProven?.  ensenha  and  OSp. enseha,  which  all  derive  fr.  L.  insignia.' Derivative :  ensign-cy,  n.
ensign,  tr.  v.,  to  distinguish.  —  OF.  ensignier,  en- seignier,  ‘to  point  out,  indicate,  teach’  (whence F.  enseigner,  ‘to  teach’),  fr.  VL.  *insignare, corresponding  to  L.  insignire,  ‘to  mark,  dis¬ tinguish’,  fr.  in-,  ‘in’  and  signum,  ‘mark,  sign’. See  sign,  n.,  and  cp.  prec.  word, ensilage,  n.,  the  preservation  of  food  in  a  silo.  — F.  See  next  word  and  -age  and  cp.  silage. Derivative :  ensilage,  v.
ensile,  tr.  v.,  to  preserve  (food)  in  a  silo.  —  F.  en- siler,  fr.  ist  en-  and  silo,  fr.  L.  sir  us.  See  silo, enslave,  tr.  v.  —  Formed  fr.  ist  en-  and  slave.
Derivatives:  enslave-ment,  n.,  enslav-er,  n. ensnare,  tr.  v.  —  Formed  fr.  ist  en-  and  snare. Derivatives:  ensnare-ment,  n.,  ensnar-er,  n., ensnar -ing-ly,  adv.
enstatite,  n,,  a  magnesium  silicate  {mineral.)  — Formed  with  subst.  suff.  -ite  fr.  Gk.  ivaxa.-crfi, ‘adversary’;  so  called  in  allusion  to  its  refract¬ ory  nature.  Gk.  evr;TaT/)c;  derives  from  the  stem
1
of  evtaTiQpi,  ‘I  stand  in;  I  oppose’,  fr.  4v  (see 2nd  en-)  and  l'<rn)pt,  ‘I  cause  to  stand ;  I  stand’, fr.  I.-E.  base  *sta-,  ‘to  stand’,  whence  also  L. stare,  ‘to  stand’.  See  state  and  cp.  histo-. ensue,  tr.  and  intr.  v.  —  OF.  enseu,  pp.  of  en- suivre,  ‘to  follow,  ensue’,  fr.  VL.  *insequere,  cor¬ responding  to  L.  insequi,  ‘to  follow,  strive  after’, fr.  in-,  ‘in’,  and  sequi,  ‘to  follow’.  See  sequel  and cp.  sue,  suit,  suite.
Derivatives:  ensu-ing,  adj.,  ensu-ing-ly,  adv. ensure,  tr.  v.  —  AF.  enseurer,  formed  fr.  ist en-  and  OF.  seur  (whence  F.  sur),  ‘sure’.  See sure  and  cp.  insure.
Derivative:  ensur-er,  n.
-ent,  adj.  and  subst.  suff.  denoting  an  agent  or an  instrument.  — -  OF.  and  F.  -ent,  fr.  L.  -en- tem,  acc.  of  -ens,  pres.  part.  suff.  of  verbs  per¬ taining  to  the  II  and  III  conjugation.  See  -ant and  cp.  -ence,  -ency.
entablature,  n.,  a  horizontal  structure  composed of  cornice,  frieze  and  architrave  and  supported by  columns  {archit.)  —  MF.,  fr.  It.  intavolatura, fr.  intavolare,  fr.  in-  (fr.  L.  in)  and  tavola  (fr.  L. tabula,  ‘board,  plank,  table’).  See  in-,  ‘in’,  table and  -ure.
Derivative:  entablatur-ed,  adj. entablement,  n.,  platform  on  which  a  statue stands.  —  F.,  fr.  VL.  intabulamentum,  fr.  in-, ‘in’,  and  L.  tabulamentum,  ‘boarding,  flooring’, fr.  tabula,  ‘table’.  See  table  and  -ment. entail,  tr.  v.,  1)  to  bestow  as  a  heritage;  2)  to  in¬ volve.  —  Formed  fr.  ist  en-  and  AF.  tail,  ‘limit¬ ation,  limit  of  ownership’,  fr.  OF.  taillier  (F. tailler),  ‘to  cut’.  See  tail,  tailor.
Derivatives :  entail,  n.,  entail-er,n.,entail-ment,  n. entangle,  tr.  v.  — -  Formed  fr.  1  st  en-  and  tangle (q-v.)
Derivatives:  entangl-ed,  adj.,  entangl-ed-ly,  adv., entangl-ed-ness,  n.,  entangl-er,  n.,  entangl-ing, adj.,  entangl-ing-ly,  adv.
entasia,  n.,  tonic  spasm  {med.)  —  Medical  L., fr.  Gk.  Evraoti;,  ‘a  stretching,  straining’.  See next  word  and  -ia.
entasis,  n.,  convexity  in  the  shaft  of  a  column {archit.)  —  ModL.,  fr.  Gk.  brsctmc,,  ‘a  stretch¬ ing’,  fr.  4vteiveiv,  ‘to  stretch  or  strain  tight’, fr.  b>  (see  2nd  en-)  and  teIveiv,  ‘to  stretch, strain’.  See  tasimeter  and  cp.  ectasis  and  words there  referred  to.
entelechy,  n.,  actuality  as  opposed  to  potentiality {philos.)  —  L.  entelechia,  fr.
```


## [2026-09-05T20:33:23.462Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if re.search(r'\\bet\\s+cetera\\b', p) or re.search(r'\\beddy,\\s*n', p):\n        print('--- leaf',i,'---')\n        for m in re.finditer(r'(et\\s+cetera[^\\n]{0,600}|eddy,\\s*n[^\\n]{0,600})', p):\n            print(m.group(0)[:700]); print()\nEOF"
}
```


### [2026-09-05T20:33:25.826Z] TOOL RESULT

```
--- leaf 272 ---
eddy,  n.,  whirlpool;  current  of  air.  —  ME.  ydy, prob.  fr.  ON.  ida,  ‘whirlpool’,  lit.  meaning  ‘that which  rebounds  or  flows  back’,  fr.  ON.  pref. id-,  ‘again’,  which  is  rel.  to  OE.,  OS.  ed-,  OHG. et-,  it-,  Goth,  ip,  ‘and,  but,  however’,  and  cogn. with  L.  et,  ‘and’.  See  et.  Derivative:  eddy,  intr.  v. ede-,  form  of  edea-  before  a  vowel, edea,  n.  pi.,  the  external  genitals.  —  Fr.  Gk. aiSoia,  ‘privy  parts,  pudenda’,  prop.  neut.  pi. of  txlSoiog,  ‘bashful,  shamefaced’,  lit.  ‘having a  claim  to  regard’,  fr.  aiScog,  ‘shame,  bash¬ ful

--- leaf 296 ---
et  cetera,  ‘and  other  things’.  —  L.,  fr.  et,  ‘and’ (see  et),  and  neut.  of  ceteri,  ‘the  others’,  which is  formed  fr.  I.-E.  pron.  pref.  *ce-,  ‘there;  behold’ (see  he),  and  I.-E.  *etero-,  ‘the  other’,  whence also  Umbr.  etro-,  ‘another’,  Avestic  a-tara-, ‘one  of  the  two,  this’,  Alb.  jatere,  jatre,  ‘the other’,  OSlav.  jeteru,  iteru,  ‘some,  one’, etch,  tr.  and  intr.  v.,  to  engrave  with  acid.  —  Du. etsen,  ‘to  etch’,  fr.  G.  atzen,  ‘to  corrode’,  fr. MHG.  atzen,  etzen,  fr.  OHG.  azzon,  prop,  ‘to feed,  bait’,  causative  of  e$$an,  ‘to  ea

--- leaf 382 ---
et  cetera,  hodiernal,  sic.
```


## [2026-09-05T20:33:31.142Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\np=pages[296]\nprint(re.findall(r'\\b5[0-9][0-9]\\b',p)[:10])\ni=p.find('et  cetera')\nprint(p[max(0,i-2500):i+300])\nEOF"
}
```


### [2026-09-05T20:33:32.894Z] TOOL RESULT

```
['544']
rient  and  words there  referred  to.
Derivative:  esurient-ly,  adv. et,  conj.  meaning  ‘and’.  —  L.;  cogn.  with  OI. dti,  Avestic  aid,  ‘over,  beyond’,  Gk.  £u,  ‘yet, still,  besides,  moreover’,  Gaul,  eti,  ‘also,  more¬ over’,  Goth,  ip,  ‘and,  but,  however’,  OE„  OS. ed-,  ON.  id-,  OHG.  et-,  it-,  ‘again’.  Cp.  eddy.
-et,  subst.  suff.  of  orig.  diminutive  force.  —  OF. and  F.  -et,  prob.  of  Etruscan  origin.  In  French, the  suff.  always  had  and  still  has  diminutive force.  For  the  feminine  form  of  this  suff.  see -ette.  Cp.  -let
-et,  an  infix  used  in  chemistry  (as  in  phen-et- idine),  to  denote  the  presence  of  the  ethyl  radical. —  Short  for  ethyl.
eta,  n.,  name  of  the  seventh  letter  of  the  Greek alphabet.  —  Gk.  -Jj-ra,  fr.  earlier  -Jj-ra  (see  Theo¬ dor  Noldeke,  Beitrage  zur  semitischen  Sprach- wissenschaft,  Strassburg,  1904,  p.124),  fr.  Heb. heth;  see  cheth.  The  a  was  added  because  a Greek  word  cannot  end  with  a  t;  cp.  alpha  and words  there  referred  to.
etacism,  n.,  the  pronunciation  of  Gk.  eta  (i.e.  the letter  rj)  as  e  i.e.  like  a  in  English  ale;  called  the Erasmian  pronunciation.  —  Formed  fr.  eta with  suff.  -ism.  Cp.  itacism. fctage, n„  stage.  —  F.,  ‘abode,  stage;  story,  floor’, also  ‘rank’,  fr.  VL.  *stadcum,  for  L.  statio,  ‘sta¬ tion,  onst,  residence’,  lit.  ‘a  standing’,  fr.  stare, ‘to  stand’.  See  state  and  cp.  stage,  ‘platform’, etagfcre,  n.,  cabinet.  —  F.,  fr.  etage,  ‘shelf’.  See prec.  word.
etamine,  n.,  a  dress  fabric  of  cotton,  worsted  or silk.  —  F.  etamine,  fr.  OF.  estamine,  fr.  VL. *staminea,  fern,  of  the  Latin  adj.  stamineus, ‘made  of  threads’,  fr.  stamen,  gen.  staminis ‘warp  in  the  upright  loom,  thread’.  See  stamen. 6tape,  n.,  1)  a  halting  place  for  troops;  2)  a  day’s march.  —  F.,  ‘stage  of  journey,  halting  place, distance  between  two  halting  places’,  fr.  OF. estaple,  fr.  MDu.  staple,  ‘storehouse’.  See  staple, etat,  n.,  state.  —  F.,  fr.  L.  status,  prop,  ‘mode  of standing’.  See  state  and  cp.  words  there  re¬ ferred  to.
etatism,  n.,  state  socialism.  —  F.  etatisme,  formed fr.  etat,  ‘state’,  with  suff.  -isme.  See  prec.  word and  -ism.
Etat  Major,  the  staff  of  the  army.  —  F.  etat- major,  fr.  etat,  ‘state’,  and  L.  major,  ‘greater’. See  etat  and  major,  adj. et  cetera,  ‘and  other  things’.  —  L.,  fr.  et,  ‘and’ (see  et),  and  neut.  of  ceteri,  ‘the  others’,  which is  formed  fr.  I.-E.  pron.  pref.  *ce-,  ‘there;  behold’ (see  he),  and  I.-E.  *etero-,  ‘the  other’,  whence also  Umbr.  etro-,  ‘another’,  Avestic  a-tara-, ‘one  of  th
```


## [2026-09-05T20:33:46.402Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if re.search(r'Avestic\\s+u[nū]a|uyamna|ūna', p):\n        print('--- leaf',i, re.findall(r'\\b1[0-9]{3}\\b',p)[:6])\n        for m in re.finditer(r'.{300}(?:Avestic\\s+u[nū]a|uyamna).{300}', p, re.S):\n            print(m.group(0).replace('\\n',' '))\n        print()\nEOF"
}
```


### [2026-09-05T20:33:48.542Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T20:33:53.317Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    m=re.search(r'\\nvain,\\s*adj', p)\n    if m:\n        print('--- leaf',i, re.findall(r'\\b1[0-9]{3}\\b',p)[:8])\n        print(p[m.start():m.start()+1400].replace('\\n',' '))\n        break\nfor i,p in enumerate(pages):\n    m=re.search(r'\\nwant,\\s*(tr|n|intr)', p)\n    if m:\n        print('=== leaf',i, re.findall(r'\\b1[0-9]{3}\\b',p)[:8])\n        print(p[m.start():m.start()+1200].replace('\\n',' '))\n        break\nEOF"
}
```


### [2026-09-05T20:33:55.164Z] TOOL RESULT

```
--- leaf 894 ['1795', '1871', '1845']
 vain,  adj.  —  ME.  vaine,  vain,  vdyn,  veyn,  fr.  OF. vain,  vein  (F.  vain),  fr.  L.  vanus,  ‘empty,  void, vain’  (whence  also  It.,  Sp.  vano.  Proven^.  va. Port,  vao),  which  is  cogn.  with  OI.  unah,  ‘in¬ sufficient  wanting',  Avestic  und-,  ‘wanting’,  Arm. unain,  ‘empty’,  Gk.  civii;  (for  *eF£vl<;),  ‘bereav¬ ed  of’,  fr.  I.-E.  base  *(e)wa-n-,  ‘to  be  empty,  to lack’.  Cp.  vanish,  vanity,  vaunt,  evanesce,  evan¬ ish.  Cp.  also  wan,  want,  wanton.  Cp.  also  vacant. Derivatives:  vain-ly,  adv.,  vain-ness,  n. vair,  n.,  fur  (her.)  —  ME.,  fr.  OF.  (  =  F.)  vair,  fr. L.  varius,  ‘varied,  variegated,  particolored’.  See various  and  cp.  the  second  element  in  miniver. Vaisya,  n.,  the  third  of  the  great  Hindu  castes, comprising  agriculturists  and  merchants.  —  OI. vaisyah,  ‘settler,  peasant’,  rel.  to  vesah,  ‘house’, vesah,  ‘neighbor’,  and  cogn.  with  Gk.  olxoc, dial,  "foixoi ‘house’,  L.  vicus,  ‘village’.  See vicinage. vaivode,  n.,  the  title  of  local  or  provincial  rulers in  certain  Slavic  countries  of  southeastern  Eu¬ rope,  formerly  used  esp.  in  Transylvania  and  in Moldavia.  —  ML.  vaivoda,  fr.  earlier  Hung. vajvoda  (later  contracted  into  vajda),  fr.  Serb vojvoda,  lit.  ‘leader  of  an  army’,  fr.  OSlav.  voji (pi.),  ‘warriors’,  and  -voda,  ‘leader’,  from
```


## [2026-09-05T20:34:03.732Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(890,900):\n    print(i, re.findall(r'\\b1[0-6][0-9][0-9]\\b',pages[i])[:12])\nEOF"
}
```


### [2026-09-05T20:34:05.950Z] TOOL RESULT

```
890 ['1680']
891 []
892 ['1003']
893 ['1598', '1649']
894 []
895 ['1661', '1594', '1671', '1640', '1691', '1599', '1641']
896 ['1692']
897 ['1577', '1657']
898 ['1694', '1695']
899 ['1696']
```


## [2026-09-05T20:34:11.858Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor i in 131 148; do echo \"=== HRN leaf $i ===\"; awk -v n=$i 'BEGIN{RS=\"\\f\"} NR==n+1' HRN.txt; done"
}
```


### [2026-09-05T20:34:13.536Z] TOOL RESULT

```
=== HRN leaf 131 ===
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
=== HRN leaf 148 ===
- 127 -
ap. "^dastabara-; phlv. dastwar, dastbar.
Nicht zu dest *Hand\ sondern zu der in aw. dqsfva-
etc. steckenden Wurzel dmts- (Darmestetor, Et. ir.
I, 115 Note)'). Zu derselben Wurzel stellt Nöldeke
(mündliche Mitteilung) auch np. dästan-), destan *Go-
schichte, Erzählung .
5()9. duH^^är, duSvär 'schwierig*, dus/'ün, dusvan,
aw. vergl. duzadra- (Geldner, KZ. 25, 478, Studien
I, 17 folgg.); phlv. dus/J'är, dmx'arlh.
Die neup. phlv. Formen sind Neubildungen aus
dus+x"^'^ (No. 49G).
570. destän 'menstruirende Frau'.
aw. da/stavaitl-; phlv. dastän (arm. LW. dasfan;
chald. LW. ]P\'^'^)j dastan(i)stan^ vorgl. dayßak,
571. dil *Herz', diler (reimt auf ser, Sahn. I, 195, 1194).
aw. zered- (y. :n, 12), zaredaya- *lIorz*; phlv. dil,
päz. diler (Men.); ai. hfd-, hfdaya-; arm. sirf (IT.
No. 250).
kurd. zar 'Herz*; af/. zra; oss. d. zärdd^ t. z'ardä
(131); bei. ^^zVc/c (420); sar. zärd^ si;'n. -^^Il), <m//,
sangl. mrütj^ minj. 2?/.
np. rf// ist ausserdem in alle iranischen Sprachen
entlehnt, meist ohne einen Bedeutuugsunterschi(^d mit
dem betreffenden einheimischen Woite aufzuweisen
(Ausnahme: Tomaschek, S. 78()).
572. dem 'Atem, Atemzug', deine^ demulen 'wehen, blas(Mi\
demäy^ demär,
ai. V^dham-', dhdmiti 'hauchen, bhisen*; phlv. dam;
ksl. dümq, dqti 'blasen'.
< . •
') Bartholomae (BB. 15, 86) legt dieser Wurzel die Bedeutunjij
einweihen, weihen* bei. Dazu passen aber inoht die ebenfalls dazu
gehörigen ai. dasmä-^ dasrä-. Geldner übersetzt KZ. 30, 329 aw.
dldaihhe mit 'ich wurde unterwiesen*.
«j Anders Fr. Müller, WZKM. 5, 354. - Rückert hat
V ••
übrigens in seinen Bemerkungen zu MohTs Sähnäme-Ubersolzung
auch np. (h'sfür mit desf zu voroinigon versucht.
```


## [2026-09-05T20:34:27.303Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN leaf 264 (p.243) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==265' HRN.txt\necho \"=== HUB leaf 115 (p.105) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==116' HUB.txt"
}
```


### [2026-09-05T20:34:28.947Z] TOOL RESULT

```
=== HRN leaf 264 (p.243) ===
- 243 -
aw. Vieira- 'Entscheider ; phlv. v(i)öfr 'Entscheidung ;
Entscheider, Richter ; arm. LW. vcir ^Entscheidung.
1085. veng, ving 'leer; arm'.
aw. vergl. wwa- *leer, mangelnd'^); ai. und- Voran
etwas fehlt, unzureichend'; arm. unain *leer' (H.
No. 236); got. van 'Mangel*; gr. bvvi^ ermangelnd'
(zu einer {/^ven-*, Osthoff, Morph. Unt. IV, 368 ff.,
dagegen zu einer |/^m-, Bartholomae (briefl. Mit-
teilung) unter Verweis auf BB. XVII, 121 und Per
Persson, Wurzelerweiterung 83 zu einer l'eua-).
Die Anregung zu dieser Zusammenstellung verdanke
ich Herrn Prof. Nöldeke, der lat. vanus vergleichen
wollte, das mir aber (vergl. väcuus) nicht dazu zu
gehören scheint. Nachträglich sehe ich auch Toma-
schek zu sar. vanao 'Leerheit, Eitelkeit, Müssiggang,
Faulheit'.
1086. vir Sinn, Verstand; Gedächtniss'-), hir, her (8,
Vullers), Viru 'im Gedächtniss habend'.
g. vir därtmün 'erinnern', vtr svdmün Vergessen'.
aw. *nra' 'Einsicht' in livtra- etc. (Darmesteter,
Et. ir. II, 183); phlv. vir, vlräk im Gedächtniss
habend* (Bund.).
kurd. Mr 'Gedächtniss*; bei. glr 'Gedächtniss, Er-
innerung' (110).
1087. werän, werane wüst', heran.
phlv. aperän 'wüst' (M6n.), aperämh (Ganj-T äayakän,
1); päz. awlrän.
Fr. Müller stellt (WZKM. 5, 260) arm. LW. aver
'zerstört, wüst ; Zerstörung, Wüste*, averem 'zerstören,
wüst machen' dazu, aber arm. e steht nur in per-
sischen Lehn Worten für e.
>) Jackson, Amer. Journal of Philology, Vol. XI, 87 folg.
«) Reimt auf sir 'Milch* (Öflhn. I, 240 Vers 1982).
16*
=== HUB leaf 115 (p.105) ===
— 105 —
1083. Dazu afgh. vatal *fliegen (3 pr. vagt) u. s. w. bei
Geiger, Etym. und Lautl. des Afgh. Nr. 265. Im
Phi. ist vazUan zu lesen.
1084. Vgl. arm. gzir (nur bei CaxCax) capo del villaggio*
= np. gizlr (bei Zenker = 'Dorfaltester , Steuer-
einnehmer'), syr. g^zTrayB 'Gensdarmen' (Hoffmann,
Ausziige p. 62, Nr. 542). Ueber vazir vgl. N ft 1 d e k e ,
Tab. 53, 444. Lies arm. vcir (mit r).
1085. Unsicher.
1087. Arm. aver lasst sich nur dann als LW. zu np. verdn
stellen, wenn phi, apSrdn fiir avSran geschrieben ^)
und in avSr-dn zu trennen ist. Denn phi. apSran
ware = arm. *aperan. Paz. awTran (mit t) gegen-
iiber steht np. veirdnd *Wiiste' bei Rosen, Np.
Sprachftihrer p. 35 und afgh. LW. vairan Viist*,
vairana 'Wtiste', vairanl *Verwiistung*.
1088. Unsicher.
1091. Hochst unwahrscheinlich. Das Zusammentreffen wird
zufallig sein. Vgl. afgh. hdra-hura noise*.
1092. Die altere Nebenform ist hagirz (Vullers hakirz).
1094. Anders, aber falsch Fr. MtiUer, WZKM. 8, 99
{hastam = zd. histami).
1095. Lies hest^ed achthundert*.
1101. „Mot savant** ! Das Wort stammt aus dem A vesta.
Hier fehlt np. hamdr 'computus, numerus, mensura',
auch in nahmar innumerabilis', arm. LW. hamar *Zahl,
Zahlung, Rechnung, Schatzung', davon hamarim 'zahle,
schatze, meine* = ap. *ham(lra' aus ^ham-hmdra-.
Vgl. mar 'ZohY (Nr. 971), $umar 'Zahl, Zahlung,
Berechnung' (Nr. 971) und Ctmar 'Berechnung'
(Nr. 47). Wrzl. skr. smar-, vgl. sam-smar *sich er-
innern, gedenken , sq^smarana" *das Gedenken, sqs-
warana- *das Ueberzahlen (des Viehes).
Wie Fr. Mailer, WZKM. 8, 180 annimmt, wau aber nicht
sicher ist.
```


## [2026-09-05T20:34:43.561Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"pdf page\" BQT_v2_pages.txt | head -3\npython3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(len(pages))\n# find printed page numbers 780 and 866\nfor i,p in enumerate(pages):\n    if re.search(r'(?<!\\d)78[01](?!\\d)',p[:400]) or re.search(r'(?<!\\d)86[56](?!\\d)',p[:400]):\n        print(i, repr(p[:200]))\nEOF"
}
```


### [2026-09-05T20:34:45.329Z] TOOL RESULT

```
684
```


## [2026-09-05T20:34:47.996Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (5,100,300):\n    print('=== leaf',i,'===')\n    print(pages[i][:400])\nEOF"
}
```


### [2026-09-05T20:34:50.031Z] TOOL RESULT

```
=== leaf 5 ===
‫‪ . ۱‬فيه ما فيه ‪ .‬مولوی بلخی رومی ‪ ۰‬مسحح بدیم الزمان‌فروزانفر‪ .‬از‬
                                                            ‫اتشارات دانشگاه تهران ‪ .‬شمارء ‪. ۵۰۱‬‬
‫جمع در ز بان فار سی ‪ .‬محمد معین (طرح دستور‬                             ‫‪ .‬قاعده‌های‬         ‫‪۲‬‬
    ‫‪.‬هران ‪ ۱۳۳۱‬شمسی ( = قاعدجمع)‪.‬‬
                                ‫زبان فارسی‪ .‬شمارء ‪ )۱‬بسرمابةً کتابخانةٌ
=== leaf 100 ===
      ‫‪4 -‬‬                                                                                  ‫‪ -‬چهمة قر کون‬
‫از‬      ‫کتابه‬     ‫جشمة نوريخش ه‬                                   ‫آقتلب الت ‪٩‬‏ ‪ -‬وماه را نیزکوبند ‪-‬‬
 ‫خورشید انور ‪ -‬وآب حبوان _ و دهان محشوق‬                    ‫حشمة قبر گون ‪-‬کتابه ازب است‬
                                               ‫اشد ‪.‬‬                      
=== leaf 300 ===
        ‫رح‬

 ‫ولام وسکون‌الی‬      ‫در لك ‪ = ۳‬تکراول‬                         ‫در لك = بقتح اول بروزن قدك‪,‬دستارجه‬
‫وکاف ‪ .‬جام کوناه قد آستن کوناه پیش واز را‬                 ‫رگاونند که رومال ورویاك باشد ؛ و باين معثی‬
                                               ‫وتف‬        ‫بجای حرف انی زای نقطه‌دار همأ مده‌است‪ -‬ودر‬

 ‫در لورینه سیر خوردن ‪- ۴‬‬
```


## [2026-09-05T20:34:53.458Z] TOOL CALL #27: Bash

```json
{
 "command": "sed -n 1,60p tools/ref_page.py"
}
```


### [2026-09-05T20:34:53.508Z] TOOL RESULT

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


## [2026-09-05T20:34:56.184Z] TOOL CALL #28: Bash

```json
{
 "command": "ls data/verification/sources/refs/ocr/BQT/ 2>/dev/null | head -40; echo \"---\"; python3 tools/ref_page.py BQT:780 --image 2>&1 | head -60"
}
```


### [2026-09-05T20:35:33.864Z] TOOL RESULT

```
0001.png
0001.txt
0049.png
0049.txt
103.vision.txt
1225.png
1225.txt
1225.vision.txt
1275.png
1275.txt
1339.png
1339.txt
1357.png
1357.txt
1382.png
1382.txt
1385.png
1385.txt
1385.vision.txt
1445.png
1445.txt
1445.vision.txt
1452.png
1452.txt
1455.png
1455.txt
1462.png
1462.txt
1471.png
1471.txt
1472.png
1472.txt
1488.png
1488.txt
1624.png
1624.txt
172.vision.txt
1803.png
1803.txt
180.png
---
no scan of BQT covers printed page 780 (see 'scans' in refs_online.json)
```


## [2026-09-05T20:35:39.269Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor f in BQT_v2_pages.txt BQT_v2.txt; do echo \"### $f\"; grep -c \"دشوار\" $f; grep -c \"خوار\" $f; done"
}
```


### [2026-09-05T20:35:41.310Z] TOOL RESULT

```
### BQT_v2_pages.txt
22
116
### BQT_v2.txt
25
122
```


## [2026-09-05T20:35:50.989Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'دشوار' in p:\n        print(i, p.count('دشوار'))\nEOF"
}
```


### [2026-09-05T20:35:52.675Z] TOOL RESULT

```
124 1
182 1
195 1
200 1
226 1
233 1
293 1
309 1
325 1
326 2
327 4
393 1
464 1
568 1
569 1
572 1
593 1
639 1
```


## [2026-09-05T20:35:58.382Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (326,327):\n    print('=== leaf',i,'===')\n    print(pages[i][:2500])\nEOF"
}
```


### [2026-09-05T20:36:00.263Z] TOOL RESULT

```
=== leaf 326 ===
          ‫تا‬                                                                                                                             ‫دشتان‬

‫تن‬       ‫سوزن کشند‬          ‫که هر‬      ‫را گوند‬            ‫تایده‬    ‫رشته‬
                                                                                             ‫وبضم اول بمعنی بد وزشت بود ‪٩‬‏ ‪.‬‬
‫کسر‬       ‫اول و‬   ‫وسم‬       ‫را همکفته‌اند ؛‬           ‫خام‬    ‫و ربمان‬
                                                                             ‫تانی‬     ‫سکون‬   ‫بقتح اول و‬             ‫‪ ۴‬ت‌‬   ‫دشتان‬

‫نزرامده‬      ‫فارسی‬      ‫باکاف‬      ‫و‬   ‫‪:‬‬     ‫است‬      ‫هم درست‬       ‫اول‬
                                                                             ‫وفوقالی‌بالف کشیده وبنون زده‪ .‬حالض‌رامی‌گوبند‬
                                                                   ‫ان‬
                                                                                               ‫یعنی زیکه خون حیضش آید ‪۰‬‬
‫‪ ۰‬رسمان‬           ‫خشکی‬       ‫‪ ۰ ۸‬بر وزن‬               ‫دشکی‬
                                                                             ‫بضم اول بروزن بدتی » زلورا‬                        ‫دشتی‬
‫خامی که زتانر سند و مردوك مانند تنضه بنخده‬                                   ‫جون‬      ‫رنگه ‪,‬‬   ‫آن کرمی باشد سیاه‬                     ‫و‬   ‫گونند‬

‫وفرموله خوانند‪.‬‬              ‫ی‬    ‫وان بفه مانندرا دب‬                ‫شود‬      ‫بر عمنوی از اعنای آدمی بح یانند خون ازان‬
                                                                                                                                            ‫ا‬
          ‫باشد شبیه بماش وبعربی درجم خوانند ‪۶#.‬‬
                                                                                      ‫بمعنی بدباد لمودن وغیبت کردن ‪ ۴‬باشد ‪.‬‬
                                                      ‫‪۰‬‬    ‫ار ان است‬         ‫وواو‬     ‫شف‬   ‫با خای‬            ‫ار )‪۱‬‬             ‫دشخو‬



‫دشمیر "اه بروزن نقصیر» بمعتی‌قیض‬                                             ‫بروزن و معنی دشوار است که مشکل‬                          ‫‪۰‬‬    ‫معدوله‬


‫وعناصر اردمه راهم کفته‌اند که خاك‬                         ‫باشد ك‬   ‫و مد‬
                                                                                                                                          ‫باشد ‪.‬‬



‫دشن د بنتح‌ارل وسکون ثالی ونون »‬                                             ‫سین بی‌نقطه وفتح فوقالی» بمعنی محوی باشد‪.‬‬
               
=== leaf 327 ===
  ‫دشيدك‬                                                                                  ‫مس‬   ‫ل‬




       ‫است » وآنرا عمود صبح هم میگوبند ‪.‬‬        ‫‪ -‬بر وزن بلنگه ‪ .‬نامشپری‬           ‫دشن‬
                            ‫دشوار ‪۴‬‬             ‫باشد ازملك ختای ‪٩‬‏ ‪ -‬و غلاف خوشة خرما‪-‬‬
‫= باواوبروزن هشیار‪ .‬بمعثی‬                                                 ‫‪8‬‬
          ‫‪¥. a‬‬                ‫‪‎‬راوخشد | ‪E‬‬        ‫وشاخیکه خوشه برآن است‪ -‬وبندیکه (‪)۱‬پیش‬
                    ‫‪۴‬‬                                                                ‫ا بندند ‪.‬‬
                                                                                             ‫ب‬
 ‫ار‬    ‫بفتح کاف‬         ‫گر‬     ‫دشوار‬             ‫= بفتح اول وثالیبروزن‌پلنگی»‬            ‫دش‬
‫بمعنی کوه‬                   ‫وسکون رای قرشت‬                 ‫دلیاوروز گار وعالم سفلی ر! گوبند ‪.‬‬
                             ‫و کوهستان باشد ‪.‬‬                  ‫‪۱‬‬                     ‫‪:‬‬
                                  ‫‪۱‬‬             ‫ذشنه = بفتح اول بر وزن تشنه ‪ .‬نوعی‬
‫بنتح شین دویم بر وزن‬        ‫دشیشاث ‏‬               ‫رمردم لار میدارند ‪.‬‬
                                                                     ‫‪۴‬تکه‬
                                                                        ‫خزنجراستبش‬
                                                                                 ‫ا‬
 ‫لطيفك ‪ .‬شب را گویند و بعربی لیل خوالند ‪.‬‬       ‫دشنة صبح ‪ -‬کنابه از روشتی صبح‬




                                                                   ‫)‪ (۱‬چك‪-( :‬در ‪۰‬‬


  ‫‪ - ۱‬درحدود العالم و ءمجم البلدان نيامده‪ .‬شابد ممحف دشتك « ترجمة تاربخ بخارا ‪.‬‬
             ‫نرشخی چاپ مدرسص ‪ «+ 120115221 ۳۳۳۰‬بارتوی‪ .‬تکرتان ‪ .‬ص‪ ۰۱۱‬باشد‪.‬‬
      ‫وی سوال ‪.‬‬   ‫لکی‬
                    ‫کاد‬
                      ‫بتیز دشنه آز‬       ‫ا‪-‬بوالمظفر شاه چنایان که برد‬
  ‫منجيك ترمذی‪« .‬سروری* ‪.‬‬
   ‫‪ .‬ارمنی ع ‪ ۳2۷124‬از ‪( * ۲2۷01200‬مشکل ‪.‬سخت‬              ‫‪ - ۴‬پهاوی ‪51 - ۳۵۷‬‬
  ‫تزديك به« دشخوار ‪٩‬‏ ‪ .‬ابرائی باستانی _ ‪ , * 2727۷-11200‬ضد ‪_arÃVXx‬‏ از ‪uh ۵۲۵۷‬‏ ‪#‬‬
 ‫خوار کر= پتشخوار کره‬       ‫پشودارشکر‬
                                    ‫یبر گك ‪ ۲۸۰‬ورك ‪ :‬خوار» دذخوار ‪.‬‏ ‪ - ۴‬مخفف پد‬
  ‫از پتش (پیش) ‪ +‬خوار(‪ -‬کر (کوه) » نی کوء واقع دجرلو خوار » (بین سمنان وورأهین)‬
  ‫بخدی از سللة جبال البرز در جنوب طبرستان ‪ .‬رك‪ :‬مار کوارت ‪ .‬ابراشهر ص ‪ ۰۳۱‬؛ اونوالا‪.‬‬
                                                          ‫س
```


## [2026-09-05T20:36:15.375Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(235,250):\n    c=pages[i].count('خوار')\n    if c: print(i,c, pages[i][:80].replace('\\n',' '))\nEOF"
}
```


### [2026-09-05T20:36:18.229Z] TOOL RESULT

```
238 6    ‫کوپ‬                                                                        
239 21  ‫خوازه‬                                                                        
240 1  ‫‪“VAY‬‬                                                                       
241 2 ‫خوان پابه‬                                                                     
245 3   ‫خورخجیون‬
```


## [2026-09-05T20:36:20.586Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(pages[239][:3000])\nEOF"
}
```


### [2026-09-05T20:36:22.352Z] TOOL RESULT

```
 ‫خوازه‬                                                                                                                     ‫‪۷‬‬           ‫‪-‬‬


‫بمعنی خوردنی ورزق وروزی باشد ‪ -‬و جضم اول‬                    ‫‪ -‬ونام ولاسی‌است درحوالی ری‪٩‬‏ ‪ -‬وعم‬                                        ‫هت‬
‫بروژن شماره » بمعتی دستورباشد که رسم وقاعده‬                 ‫اول و ثانی بالف کشیده بر وزن شمار " بمعنی‬
‫وقانون است ‪ -‬و طعامی را نیز کوبند که مقوی‬                         ‫باشد "‪ ۳‬وبعربی | واز کاو را خوانند ‪۰‬‬                              ‫خوردنی‬


 ‫بدن شود ق‪-‬اولبی بائد کهبنایان طاق کونبد‬                    ‫خو ار بار » بائانی معدوله وبای ابجد‬
‫بربالای آن سازند‪٩‬‏ ‪ -‬و بمعنی چوب بندی هم‬                    ‫است که قوت‬                 ‫کارزار» یمعی خوراك ادك‬                        ‫روزن‬
                                       ‫‪9‬‬       ‫فەا‬           ‫باشد ‪ - ۲‬و مره ولذت را نز گوند ‪-‬‬                                       ‫لانموت‬
‫خواری خوار » بائانی معدوله بر‬                               ‫ازديك‬           ‫وخطه‌ای‬           ‫و تومئی است از توه‌نات ضارا‬

     ‫وزن ماهی خوار » دشنام شنونده کروابند ‪.‬‬                                                                                         ‫ری ‪. ۴‬‬
 ‫خواری گردن ‏ کنابه از دشنام‬                                 ‫جو ار رم » نام‌شهر ست‌معروف ومشپور‬

                 ‫دادن ‪ -‬وزبان‌کاری کردن باشد ‪.‬‬                                                            ‫ازتر کتان ‪۶. ۴‬‬

 ‫بفتح اول بر وزن بماز »‬          ‫خوار ‪-‬‬
 ‫چوبدستی که خر کواو وسایر ستوران را بدان‬                          ‫کارزار ‪ ۰‬ستمکار وخواری کننده راکوبند ® ‪.‬‬
                                               ‫رانند ‪5‬‬
                                                             ‫جو ار کاره = با انی معدوله بر وزن‬
 ‫بائالی ممدو له بروزن عازه »‬    ‫حور از و ‌‬                                       ‫‪۰‬‬    ‫گویند ‪۹‬‬   ‫را‬    ‫دهنده‬   ‫دشنام‬             ‫‪4‬‬    ‫چارباره‬



 ‫بمفعنریی|ن ‪ -‬وخواهش باشد‪-۱٩‬‏ ومطلق چوب‬                      ‫خوار کادی ‪ -‬بانانی مسوله بروزن‬
 ‫پندیرا دکیوزیند اعم اآزنکه بجهت آبین بندی‬                  ‫دشنام‬       ‫و‬    ‫‪-‬‬       ‫باشد ‪۷‬‬   ‫دشنام دهی‬       ‫‪ ۰‬نمعتی‬               ‫وارداری‬

 ‫بابنایی ونقاشی کردن عمارت یابجهت تاك انگور‬                                                       ‫‪۱‬‬   ‫را نز گوند ‪۸‬‬                    ‫دهنده‬
 ‫وامثال آن بندند کوشکی وقبه‌ای را گنفزتهاند‬
 ‫که بجهت عروسی وآبین بندی ازکل ورباحین‬                       ‫خوا ده = بانانی ممدوله بروزن چاره»‬

   ‫‪ .‬معرب آن‬      ‫‪۳۸‬‬    ‫و حدود المالم ص‬         ‫‪۵۵۳‬‬   ‫کیپان ص‬      ‫‪.‬‬     ‫رك ‪ :‬حفرافیای سیاسی‬                   ‫‪-‬‬           ‫‪۱‬‬

    ‫البارها پر کرد ‪...‬‬    ‫چون بوسف‬     ‫«‬   ‫_‬    ‫‪۳‬‬          ‫«خوار» سم اول وفتح دوم ‪ :‬رلك‪ :‬معدم البلدان ‪۰‬‬


 ‫بوسف و زلیتا ‪ .‬خڅ‬
                 ‫خابنربار های مصر بجهان بیفتاد ‪ .‬خلق روی بمصر نهادند بطلب خواربار ‪.«٩‬‏‬
   ‫"‪ 7‬همان خوار (ھ‪.‬م‪ (.‬است ‪.‬‬       ‫‪۴‬‬
```


## [2026-09-05T20:36:27.154Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(pages[238][:3500])\nEOF"
}
```


### [2026-09-05T20:36:28.848Z] TOOL RESULT

```
   ‫کوپ‬                                                                             ‫خواجة اختران‬
‫خلیفة خواجه مودود وخواجه محمد ریکه‌روان‬            ‫اخة آن » کناب از تاره‬           ‫اوجه‬
                                                                                      ‫ح‬
‫خلیفة خواجه خان‌سعید درآن موضم باهم‌صحیت‬                      ‫عتری ماش ۔ وآفتاب را نیز گونند ‪۱‬‬
                                   ‫داشته اند ‪.‬‬
                                                   ‫خواجه بار ۔ با باابیمد بروزن‬
‫خواحة فلك ‪ -‬کنابه ازآتاب ‪-‬‬
                                                    ‫آشدنکرها بعربی‬
                                                                 ‫لاله زار؛ طعام بقدر حاجت با‬
                         ‫وستارة مشتری باشف ‪.‬‬

‫خواخة ماح ‪ -‬اشارءبحضرترساك‬
‫صلوات‌افعلیه است ‪ .‬مجسهاح بمعنی کثیر الخیر‬              ‫خواجه اش ؟ ‪ -‬باناوئین‌فرشت‬
                                                    ‫‪-‬‬     ‫ند؟‬
                                                            ‫یرا‬
                                                              ‫وقا‬
                                                                ‫کكآ‬
                                                                  ‫ران ب‬
                                                                      ‫علامان بصكاحب وكنو‬
                                    ‫باشد ‪. ۴‬‬
                                                         ‫وسصی خداو ند وصاحب خانه هم امه اس‬
‫خو ار = با انی ممدوله بورزن چار ‪,‬‬
‫در آخر کلمات گفته‬        ‫ب‬
                         ‫کنیتر‬
                             ‫بابنمعنی بدو‬          ‫خواچه چرخ اردق‪ -‬کناب از‬
‫امیشورهمچو شرابخوارو کباب خوار ‪ ۴‬وامثال‬
‫نلیل وبی اعتباررا لگیوزبند © ‪ -‬وبمعنی‬
                                    ‫آذ‬‫و‬                 ‫خواچه سه یاران۔ نام رسکیاهی‬
‫یض کج ناش شین ‪.‬واسان‬     ‫نتقکه‬
                             ‫راست ام‬                    ‫است در دامن کوه‌کابل ‪ ۲‬ووحه تماش انت‬
‫رکافتیهز‌اند ‪ - ۱‬و بمعنی اند و قلیل هم‬                  ‫که خواجه مودودچشتی و خواجه خان سعید‬

  ‫« دزی ج ‪ ۱‬ص ‪٩۰ ۶۱4‬‏‬          ‫داش‬
                                 ‫وشش “‬
                                     ‫خجدا‬
                                        ‫‪ = _ ۴‬خو‬                       ‫‪ - ۱‬رك ‪ :‬خوا ‪.‬‬
              ‫سلطانيم‬     ‫بنندده بارگاه‬                    ‫‪ - ۴‬من وتو هردو خواجه تاشالیم‬
   ‫«لتان ‪.۰۹‬‬
           ‫ک‬
                                          ‫‪ - ۴‬ویسی گوبند بمناسبت پیمودن آسمانها ‪:‬‬
            ‫آت شیرءاینت مبشرنلام ‪.‬‬                           ‫خواجة مساح ومسیحش غلام‬
    ‫نظامی گنجوی‪ 2 .‬گنجنه >‬

  ‫® _ یهلوی ‪( ۲۷3‬بيهودە‪ .‬تاچیز)‬                  ‫خوار (خوارنده) از مصدر خواردن ‪.‬‬      ‫‪۴‬‬
                                                                               ‫‪:‬‬     ‫‪ ۰‬او بوال ‪۵‬‬

        ‫که بنده درنظر خویش خوار میدارد ؛‬                  ‫چه جرم دید خداوند سابق الاسم‬
   ‫«کلتان ‪.۰4‬‬
  ‫هلوی ‪. 52۷5‬‬           ‫‪ - ۱‬اوستا ‪ ( 2۳01۵۷2‬رفاه‪ ,‬آسایش ) هخرده اوستا ‪ ۲۹۱‬ح ‪۱‬‬
   ‫کردی ‪ . 725‬اففانی ‪ ۰ ۲2۷1‬بلوچی ‪« 72۷‬اسنق ‪.٩٤۹٩‬طیر‏ ی‪( ×4 ۲‬خوب) «صاب‌طبری‪.*۱۱۳‬‬

                                                                                ‫بقه ازصفحهٌ ‪۹۷۷‬‬
  ‫‪ #‬خواب ‪-‬بروزن تاب ‪ .‬پهلوی ‪ 08۷1‬درنیکبه ‪» ۵۳۱2‬سانسکربت ‪ › 8۳۷5‬اوستا‬
  ‫‪: 2062‬س ‪٩۵‬‏ ‪ ۵۷ ۰ ۸۹,‬و ‪ ۸۹۲‬کردی ‪ , 81۷6۲ ۰ 0۷61‬اففانی ع ‪۰ ۵۲‬‬
   ‫بلوچی ‪« ۵۷‬استق‪ .»۵۹4‬گیلکی ‪ 0۵5۰‬فریزتدی ‪ ۷۷21‬برنی ‪W۷4‬‏ نطنزی ‪« 7101‬که‪۱ .‬ص‬
   ‫‪ , ۹‬سمنا
```


## [2026-09-05T20:36:54.821Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(232,246)  :\n    print(i, repr(pages[i][:120]))\nprint('....')\nfor i in range(320,332):\n    print(i, repr(pages[i][:120]))\nEOF"
}
```


### [2026-09-05T20:37:32.833Z] TOOL RESULT

```
232 '  \u202b\u202a 4¬-\u202cمرف —\u202c\n\n\n \u202bعرمستان \u202a ,\u202cبه\u200cعنی فوس و سخره ولاغ باشد \u202a--\u202c\u202c                                \u202b\u202a:\u202cو یفنح اول نیز(\u202a)۱\u202c'
233 '                                                                                          \u202b\u202a۱۳\u202c\u202c    \u202b—¬\u202aYY0\u202c\u202c\n\n\u202bخنشاست ک'
234 '     \u202bاضف هه\u202c\n\n\n \u202bوساربمعنی\u200cسرباشد \u202a -\u202cوبمعنی\u200cشوره که از آن باروت\u202c                     \u202bواف فارسی\u202c\n                     '
235 '                                                                                                   \u202bسا \u202a۷\u202cات\u202c\n\u202bحنیدن = ش'
236 ' \u202b¬ \u202a~A\u202c\u202c\n\n\n   \u202bن\u202c\n   \u202bز بر\u202c\n      \u202bوول\u202c\n        \u202bحنبور \u200f\u202a ١\u202cبا تحتانی مجپ\u202c                        \u202bوسکون\u202c     \u202bانی\u202c   \u202b'
237 ' \u202bخواجه\u202c                                                                             \u202bها\u202c\n                              '
238 '   \u202bکوپ\u202c                                                                             \u202bخواجة اختران\u202c\n\u202bخلیفة خواجه مودود و'
239 ' \u202bخوازه\u202c                                                                                                                '
240 ' \u202b\u202a“VAY\u202c\u202c                                                                                                      \u202bخوای\u202c\n\u202bه'
241 '\u202bخوان پابه\u202c                                                                                                      \u202bیز پا\u202c'
242 ' \u202b\u202a۷\u202c\u202c                                                                                             \u202bخوانچة زر\u202c\n         '
243 ' \u202bخود خروه\u202c                                                                                \u202b”\u202a“YA\u202c\u202c\n\n\n \u202bدایر\u202a - ۷\u202cویمعنی'
244 '\u202b\u202ae Cs\u202c\u202c                                                                             \u202bخجودرا رسن کردن\u202c\n\n\u202bونایه از علف خو'
245 '  \u202bخورخجیون\u202c                                                                                    \u202b\u202aYAY\u202c\u202c\n\n\n\u202bجوی کوچکیاست '
....
320 '      \u202bکک\u202c\n\u202bدست گز اد ہنم کاف فارسی و زای\u202c                                     \u202bدستگار » باکاف بروزن\u200cدستبار\u202a .\u202cهمکار\u202a-\u202c\u202c'
321 '  \u202bدست مرد\u202c                                                                                         \u202b\u202a۱\u202cو\u202c\n             '
322 ' \u202b\u202a“A\u202c\u202c                                                                                                              \u202bمو'
323 '      \u202bدسی\u202c                                                                                            \u202bم\u202a ۳\u202cپوس\u202c\n    \u202bب'
324 '      \u202bات\u202c\n\n                                                                            \u202bویمعنی باری ومددکاری باشد \u202a -\u202cو'
325 '                                                        \u202bبیان دهم\u202c\n     \u202bتست وذو لقت و کنات\u202c                       \u202bنقطه'
326 '          \u202bتا\u202c                                                                                                          '
327 '  \u202bدشيدك\u202c                                                                                  \u202bمس\u202c   \u202bل\u202c\n\n\n\n\n       \u202bاست » '
328 '                                                                   \u202bبیان یدازهم\u202c\n         \u202bدال بی نقطه باغین نقطه دار مش'
329 '  \u202bدف زدن\u202c                                                                                              \u202bبر\u202c\n           '
330 ' \u202b—\u202c     \u202b\u202a0\u202c\u202c   \u202b= \u202a۵\u202c\u202c\n\n\n\n\n                                    \u202bو درخانه براشند كيك\u202c     \u202bدفز لك= بروزن ففزك » بمعنی ف'
331 '                                                                                               \u202bرت\u202c\n\n\u202bکوسفند ازآن بغورد '
```


## [2026-09-05T20:37:51.880Z] TOOL CALL #36: Bash

```json
{
 "command": "timeout 900 python3 tools/ref_page.py BQT:2293 --image 2>&1 | head -80"
}
```


### [2026-09-05T20:37:58.785Z] TOOL RESULT

```
(no exact page map; using offset -1917 -> pdf page 376; check the printed number and re-run with --pdf-page if off)
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/2293.png
REF: BQT:2293  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 376  OCR-lang: fas

-۷۹۳- وی
مرکز باشد که آن شطهٌ وسط حقیقی دایره صمغ درخت ون باشد که درخت چتلاقوج است
است . چه زد بمعنی صمغ است ؛ با زای هوز هم آمده

و فده < بروزن بنده » تره‌نیزفراکویند | است .
وآن سبزبی باشد خوردنی ‎)٩(‏ که بزبان عربی و نلک « بفتح اول و ثابی بروزن مك :
جرجیر خوانند . جالورست ددم شبیه بگربه وکبود رنگه‌سیباشد
و ندید3 ۱ - با دال در آخر بروزن ْ و بعربی وبر میگوبند ۴ - و بسکون ثانی‌وکاف
دلیمات , ام کی است از دسکها ی کتاب زند | فارسی بروزن رنگه بمعنی‌تهی وخالی۴ موکنایه
نمنی قمی‌است ازاقامآن کناب . از تهی‌دستی باشد * - و درویش وکداو نفلی
وود ۴ - بازای فارسی بروزن ابید, | را نیز گوینن ‎٩‏ - و بمعنی صدا وآواز هم‌آمده

(69 چش :- خوردلی .

۱ - پپلوی ۷۷1۵6۷4۵۸ « تاوادیا ۱۹۷ :۲ > و ۷1486۷4۵۸ « اونوالا ۸۵ »
اوستابی ۷1486۷۸4۵1۵ » م رکب از سه جزه : وی بمعنی ضد ‏ دئوه بمعنی دیوء داته بمعنی
داد و قالون » جمماً یعنی‌قالون ضد (علیه) دیو . وندبداد یکی از پنج بخش اوستای موجوداست,
ولی در مراسم دینی خوانده نمیشود . مندرجات آن مختلف امت. هرضل از آنرا «فر کرد» کوبند
ومجموماً شامل ۲۲ فرکرد امست. فرکرد اول درآفرینش زمین و کشورها : دوم داستان‌جم(یمه).
سوم خوشی و ناخوشی جهان ... اما غالب مطالب فر.کرد ها تا فرکرد ۲۱ » در قوانین مذهبی و
احکام دینی امت ازقبیل سوکند خوردن و پیمان داشتن وعهد شکستن ونظافت وغل و تطهیر و
پا نگاهداختنآب وآداب دخمه و اجتناب ارلاشه و مردار و توبه وکفاره و دربارة مزدپزشك »
و در موضوع پیشوایان درست ودروغین وآداب باخن چیدن و بربدن مو وشرحی در باره خروسی
که در بامدادان بالگ زند و مردم را به تسبیح و ستاش یزدان خواند » و در بارة ازن دشتان
(حابض) وخصاص سکه وعز یز داشتن‌آن کفتگو شده است. فر کرد ۹۲ در موضوع آوردن‌اهریمن
۹ ااخوشی را و در برابر آن آوردن پيك ایزدی ۹۹۹۹۹ درمان برای آنها سخن رانده
شده . رك : پورداود ؛کانها چاپ اول ص ۵۷ ؛ مزدپسنا بقلم نگلراده سس ۰۱۲۹

۴ - از: ون (۸م )ژد (هم.) کیلکی 8[-۷10 (سقز) . رك4 : ولیژد.

۴ - وبر (ه.م۰) ** پبر(هم.) . فارسی ام ت که تعریب شده .

۴ - هرن ۷۵۵8 , ۷188 را بمعنی خالی وققیر ضبط کرده و وجه اشتقاقی برای آن
نوشته است ۶« امشق ۱۶۸۵۹ ولی هوبشمان آنرا قطمی لمیداند ۶« هوبشمان ۱۶۸۵ *.

* - درست بنظر لمیرسد . ۹ - بمعنی درویش ومقلی :

زین شمر شاعران را کردد بقین که من ازهزل وجد توالگرم از زر وسیم ونگه,

رك : ح۶ ۰ سوزلی‌سمرقندی « فرهنگه نظام >.

- و بمم ی کدا :
نپال باغ جلال تراست کردون ب رکه ز کات کنج عطای‌تراست قارون ونگه.
منصور هیرلزی « سروری >.
```


## [2026-09-05T20:38:27.293Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### BRT xvathra\"\ngrep -n \"x\\^a\\?\\Sra\\|hva\\^ra\\|xvāθra\\|āθra\" BRT.txt | head -5\npython3 - <<'EOF'\nimport re\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nfor pat in [r'dužā\\S*ra', r'duža\\S{0,3}ra-', r'huā\\S*ra']:\n    for m in re.finditer(pat,t):\n        print(pat, m.start(), t[max(0,m.start()-100):m.start()+200].replace('\\n',' '))\n        break\nEOF\necho \"### grep 1861 area for xvathra\"\ngrep -n \"Behagen\" BRT.txt | head -10"
}
```


### [2026-09-05T20:38:29.145Z] TOOL RESULT

```
### BRT xvathra
3636:•  j.  apäxtara-,  apIx^Ära-  Adj.  'rück- wärts, hinten  gelegen'  sva.  'nördlich'*^: Harat  haca  nafmst  'tara^byB  haca  naf- maiibya  fradvarat  aarö  mainyus  V.  ig.  i ; H.  2.25,  FrW.  70.42;  —  druxs  ya  nasus upaJvqsaid  'Xraäbyö  nalmaäbyB  V.  7.  s 8. 16;  —  °W''  apanasythe  "im  Norden sollst  du  verschwinden"  SrB.j.
6973:•  j,  a-x^arant-  Adj.  'nichtessend' :  nazcis 'r^iitam  tva  ns'it . .  asayam  (sd.)  . .  V.  j.33,
6975:•  j,  a-x^arata-  Adj.  'unfassbar,  unnahbar', vom  i^ar>nah-  (sd.):  tr/rpin  °tPin  d'annö mazdaiätfm  .  .  yahmi  paiti  ''parix''äi>e (sd.)  sp>ntasca  mainyui  anrasca  aäahmi paiti  at  'te  Y.%.  ig.  A,li.;  —  atari  .  .  uiti . .  mankanö  a3at  si'ar^nB  hangpr»/s3ne  yal 'fymYt.iff.4j;  — <'^I  vS  kascit  malyänqm id'artttS  "tsm  isaSta  Yt. /p.  53;  —  käva- yeheca  x''armar>hu  .  .  'taheca  ^farftta^hs mazd^ätahe  Y.  j.  14;  S.  i.  25,  Y.  2. 14,
7210:•  j,  a-x^arant-  Adj.  'nichtessend':  naiUs •nntam  tva  fidii  ..  asayam(sd.)  ..V.^.^y
12880:—  ')  S  411-  3  d. •  p.  darga-,  g.  daraga-,  j.  dar«}-a-  Adj. (fem.  °7J-)  'lang';  i)  räumlich:  Ufa  tarn car^am  yqm  'yqm  YtJp.  77;  5.50;  — mi^rtm  . .  yeAha  'yäat  bäeava  .  .  Yt.  10. 104.  z)  zeitlich:  M<?i«(sd.)  tat  äs  nsit 'y?m  Yt.5. 65;  —  "iimal  aipi  zrvätum Y.62.3,\tig.a6;  13.53;  —  °f^^  ^yo (sd.)  t^mattks  Y.31. 20;  —  'yayäsca  paiti danyjjltdis  YL  /y.  1 3  j ;  Y.68.11;  —  tsm (nämL  kämtm)  msi  data  'gahys  *yaos{^^^ vairyS  stSis  Y.  43.  13;  —  hyatcä  -gSm *Jr3gvö.d»dyS  rasö  {sd.)  Y.jo.ii; — ptn- fum/a  (sd.)  barjsma  starane  °y?mca  yasram ..yaaJnS'Vt.iO.iiSi—ya^a  Sicä  *aiivi- iayama  'ya  amiiayana  . .  hr^yrnya^^aSum (sd.)  Yt  70.  7  7 ;  —  °gäi  Tsyai  bfzvait!  hax- maim  (sd.)  Y.  40.  3;  —  'yai  hax^räi  Vt 10.  T),  17.6;  — fravaiayS . .  hulhaxmanS . .  'yaa'fyj  Aax^oralifyff  Vt  13.  30;  —  'y^m Aaxma  V.  60.  j;  —  dättm  tS tanuye  :^ar»nB ' urvnaläi  •y?m  havanfum  (sd.)  Yt77.  22; F.^b;  —  urunaica  'ye  havanhe  A.  i.ii; —  'yäi  AaosravaAAsi  .  .  -yai  AavafiAäi Vjtjs;  —  a  'yät  ^ä.bairyilt  (sd.)  Y. öo.  6;  —  'yqfi  upayanayä  (Stverz.)  Y, /.  13  usw.;  —  'ya  (APn.)  data  .  .  sara- >uäraAe  T.  ^6  {?);  —  iaia  tl  'yim  ävSya (sd.)  aakal  H.2. 34;  16.  a)  Adj.  an Stelle  unsres  Adv.'':  :^afsa  'yd  tna^äka "schlaf  lang,  o  Mensch"  V.  rÄ  16;  — earäiti  .  .  yä  'ya  apu%ra  aHti  V.  3.  34; 34.  b)  ASn.  als  Adv.:  H  utä,  'gam  jlvä
### grep 1861 area for xvathra
5164:—  Sal  dli  ävaidayamahi  . .  "vatthe  Y.4. 6.  a)  ellipt:  'vaiiihe..  timänS.paite'^xa Hilfe!  Hausherr"  V./Ä19;  31,22.  LS. avöaüs  Inf.  sbes.  2)  'Ergötzen,  Behagen' (nur  Komp.).
6348:•  j.  aäa.x''ä*i^-"  Adj.  'der  das  Behagen, Glück  des  Ala  gewährt' (?),  von  Bergen: gairlm  usi.darmjin    ..    "rim  Y,  1'.  14;  —
6362:•  j.  a-säite'*  Inf.  'sich  zu  freuen,  behag- lich zu  fühlen':  ya'iia  vätS ..  vJsp^m  ahUm .  .frähatica  .  .  aiwüa  as°  Jsmayäiti  "wie der  Wind . .  die  ganze  Welt . .  in  Behagen versetzt"  A.  4-  6-
11338:•  g.  CiSriLavah-,  j,  ^Äiftra.avah- "  Adj. 'deutliches,  augenfälliges  Ergötzen,  Behagen schaffend':  at  tsi  atrSm  ahurä  usSmakJ.. ^aslstjm  imavaithm  f/ö((sd.)  raparUE  'vav- h)m  ai  .  .  "von  deinem  Feuer  {Ätar),  o Ah.,  . .,  dem  verheissenen ,  machtvollen, wünschen  wir,  dass  es  dem  Getreuen  augen- fälliges Behagen  (schaffe),  aber.,"  ^.34. 4*>;  —    narqm  ..  *°Z'anhqm  Ny.j.  10'*.
16318:•  j.  pourus-x'^Sra-  Adj,  {fem,  'rä-)  'der  j viel  Behagen,  Glück,  Wonne  gewährt':, alis  'ra  Yt.  15.54;  —  kahmsi  istlm  °rqm\ azim  baxsäni  Yt/o.io8;  Y.6Ä11-
24443:•  j.  vispa  Jt'aÖTa-  Adj.  'der  alles  Behagen, Glück,  alle  Wonne  besitzt  und  gewährt":
```


## [2026-09-05T20:38:36.709Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"duz\\.ä\\|duz\\.a\\|duiä\\|duz\\^ä\\|dui\\.ä\" BRT.txt | head -20\necho \"---- search Unbehagen ----\"\ngrep -n \"Unbehagen\" BRT.txt | head -10\necho \"---- xvathra main ----\"\ngrep -n \"j\\.  x''a\\|j\\. x''ä\\|x''äi>ra-\\|x'aÖra-\\|x^aÖra\" BRT.txt | head -20"
}
```


### [2026-09-05T20:38:36.785Z] TOOL RESULT

```
11410:AbleiL  —    zEt  S.  riitnäiu.  —  VgL  ianman-. —  Pü.:  duiärm').  —  ')  Vgl-  A.  J.  7.  —  >)  S.
13791:Pü.  (dRn.)';  du^mSlilttlh,  pa  duiämöasriih,  duilh ämöxlär  (Sü.:  diifloHfyäpilä).  —  ■)  Stammt  vll. aus  Y.  32.  9,  s.  2  und  Pu.
18201:mit  a  i)  'Jemandem  (Dat,  Gen.,  Lok.) etwas  (Akk.)  feierlich  (an)  wünschen' "' vasla  c-fakrfinca  a/rlnami  vTspayä  asaonS stsis  asasla  duiä%nmia  S/rinämi  vTspayä drvats   slöis'Y,  8.  Z;    52.  1,  68.  15-' yastamla  vahmmtla  .  .  ä/rtnamt   akurahe matdä    Y.  73.  d;  62.  i;    —  fravaiayS  . xsnüiä  afrjfuntu   ahmya  ntnSne  varfuhim astm  YL  13, 1 5  7  j   —   ohne   Angabe   des wem?:  d^a  Jamyat yd^u  afnnSmi  SrB.5;
---- search Unbehagen ----
---- xvathra main ----
```


## [2026-09-05T20:38:42.551Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '11400,11415p' BRT.txt\necho \"======\"\ngrep -n \"duivär\\|duSvär\\|duixvär\\|dulvär\\|duxvär\" BRT.txt | head\necho \"====== search for 'ä%ra' pattern ======\"\ngrep -c \"ä%ra\" BRT.txt; grep -n \"ä%ra\" BRT.txt | head -20"
}
```


### [2026-09-05T20:38:42.637Z] TOOL RESULT

```
•  j.  Hnah'  n.:  s.  unter  *laiiah-. KompE.
•  j.  "yao^ni  surake^  F.  4  g. Fü.:  Uast  /•  aus.
•  j.  '(^iiiinan-  n.  'Begehren,  Trachten nach  — ':  nStt  ahmat  *ä  zyäHlm{sA)  xs'tä müsdayamts  aoi  vJsiS  nöit  astö  nöit  uslä- nah!  •m^«j(AP.)  "ich  will  . .  mich  nicht mehr  schuldig  machen,  noch  des  Trach- tens nach  Leib  und  I^ben"  Y.  12. 3.
Zum  V.  ^ka't-,  %  si/S.  4.  —  Vgl.  lu  uKänS.- Hnakyä'.  —  Pü. :  u  iii  Ion  u  ni  yäa  Jusärm^i fj>  (Sü.!  rW/flMn«j™}.    erl.;
änvant-
596
>  Vgl.  i
:  afiäc
•  j.  '£iiiinan-  n.  "Denken  an  -,  Bedacht- sein auf—  (Gen.),   Sorge,    cura':   tat  ..
'ma  kahysHi  atshSus  astvatS  yB  alahe  Sn- mavastimB  a»Aai  ".  ■  Sorge  fiir  Jeden  , ., der  recht  für  das  -4/a  besorgt  ist"  P. 4.3Q)  ■';  —  'manS  F.  ig.  DS.  'mäne  als Inf.  sbcs.
AbleiL  —    zEt  S.  riitnäiu.  —  VgL  ianman-. —  Pü.:  duiärm').  —  ')  Vgl-  A.  J.  7.  —  >)  S.
•  j.  ^inraan-  Adj.  'bedacht  auf -j  Sorge tragend  um  — '  (Gen.):  aZvafu  kätqm 'mänahe^^  yat  alahe  vakistahe  "irgend eines  der  Seienden,  der  um  das  beste Aia  Sorge  trägt"  A.,?.  7(?)'^.
Vgl.  'ännian-.  —  ')  Them.  —  >)  Vgl.  P.  43.
•  j.  £inmavast3ma-  Adj.  'der  am  meisten, sehr  bedacht  ist  auf  — ,  besorgt  ist  fiir  — '
(Gen.):    tat  .  .  cinma  (sd.)  kakyaRt  .  .  yS
asahe  °mS  atthai  P,  43-
======
====== search for 'ä%ra' pattern ======
32
4917:*)  Ursprünglich  des  Fesis  der  Heimkehr  von Hirt  und  Herden  aus  der  Senne  (s.  u.).   Später ist    es    dem   Andenken    an   die  SchaiTung   der Pflanzen  geweiht   Der  letite  (30,)  Tag  fällt  auf den  30.  des  7.  Monats,    d.  i.  in  alter  Zeit  auf den  3.  Okiober,  heutzutage  auf  Mitte  ApriL    S. im  übrigen  unter  yüirya-  und  miuiySisaiH: Ableit.  aas  'a-yä%ra.  n.  (iura  V.  yä-)  'Heim- kehr',  als   Adj.  ftlso  'was  mit  der  Heimkehr in  Beziehung  steht';  s.  Roth  ZDMG.  J4.  704. j.  ayiri.dräjS  N.  43:  lies  ayari.dr',
7261:ya().         b)   eines  Nebensatzes:  yöi  nmäna kam.barSfnahi  (sd.)  .  ,  ätrsmca  .  ,  W  pas- ciota  ahe  nmänake  spä  vä  nä  va  in%yäi iüia  .  .  "wenn  wir  . ,  und  es  stirbt  dann . ., wie..?"  V.5.39;  Vd./();   —  yS  itarö  .. mpaidyeinte    .  .    ä'    ae^am    naram    afvS irtiyat    cvat  ..  V.5.27.'         3)  'lur    An- knüpfung eines  adversativen  Satzes  'aber; sondern;  vielmehr;  gleichwohl':  i'äa  main- yäe  dus^artnä^  .  .  ä°  azitn  manya  Yt.  10. 105  c;  —   nöii  .  .  vjspa  yazatinhö  .  .  ä' ..  aevd  zarä^usürä  Yt.  ij.  ig;  5,  55  aSt^^ ti-S3<  V-io.S,  ig.  5;  —  iä  fravasayS  . . acjifta     h^nti    .  .    yi    .  .    saosyantqm    ä° ai^alsqm  Jravasayö  (sd.)    .  .    Yt.  1^,  17; N,  I02;  — -  nahänazdiStö  ä'  havatam (sd.)  N.  i^;  p,  6-];    —    äs    zaotars  (sd.) kairim  ar^hath.ä'  AävanänS  {vä.m\.  kairim auAat)  yal .  .  N.  ■J2;  yS—yO,  66';  —  apa. •  •  y^  pora  ahmat  hiit?nta  .  .  3*  W  nürqm fratoHnü  Yt.ij.53f.;  $6,  5S;  —  aai{%'.Z) yakmai  xstiüts  Öavaiti  mihrS  ahmäi  jasaiti avairiie  ü.'  yahmäi  ßistS  bavatH  . .  ahmäi frasciruiayeiti  nmätamca  ..  YL/0.87, yeiihe  x^akrä^ia  nsU  aoüin  änAa  . .  para tthmat  yat    , .    ä°  yal    . .    ",  .  bevor  . aber  als  .  ."  Yt./().33f.; — yaj  Ae pu%, usjaysi^e  .  .  ikalsB  anyS  .  .  ä°    anyS  .  . \.g.io;    —  tar5.d»nanB  (sd.,  näml.  urva- rayä  ar^han)  .  .   ä'   vp?ma  agis.drajaT3h& N.90;  —  navajcsaparim  ..  aiwi^äme  ä' hama  mäzdräjakim  V.J.  42;  N,  4Ö,  4~>5'i; —  nsil    ahmi  nmäne  *sanaile  ä%rava  . ä'  .  ,  sayänie  dahakäca  "nicht  werden  . geboren  - .,   sondern    es    sollen   geboren werden  . ."  Y.  //.  6 ;  —  hau  .  .  yO  .  .  varg- thfca  Aqm.rüzayeiti .  .  a'ia  dim  upa-taala^ ydii  . .  raesayacä  (sd.)  , .  ä°  yat  . .  van- iäsca    *hqm.räzayaaha   .  .   äat    (s.   7)    .  . fascaSa  apa.bardi!  ". .  vielmehr  wenn  du dir  die  Haare    ordnest  . .,   so  sollst  du dann  .  ."  V.iy.z-i,;    —    a%>m  vTspanqm damanqm    nipäta    ahmt    .  .    ä"    ('gleich- wohl') mä  nSil  masyäka  .  .  ya'^nte  Yt  10. 54.        a)  bes.  mit  a)  folgendem  _j'iii  oder ye:i,  ß)  vorausgehendem  yezi  "wenn  aber, wenn  jedoch",  kondiz.:  a)  *yujyaslil  haca *nmänät  .  ,  ä'  yal  h!  aoxte  .  .   d^a  *hil *xiayete  ..  haxtSii  (sd.)  N.<Vf.;  V.7.3; all  (s.  8)  yS  . .  upairi  hunanm  (sd.)  mc iarät  .  .  ä°  yat  .  .  paiti  barJt  äaj  (s.  2) yal  .  .  ara  baraite  "wer  .  .  aber  wenn  er ■ .  und   wenn   er   ■  ."   P.j7f.;
7501:•  j.  'ä-sna-  Adj.  (fem.  °»<i-)  'erfolgreich, wirksam,  tüchtig':  'naca  (APn.)  viana asäunam  'nafa  manä  sae^antqm  Vr.  J/.3; —  °K.7  (APn.)  . .  mata  Yt  13. 74.  a)  bes. von  frasanfay-  f.'*:  ifä%ravaiH  'na  fra- ttitntifY.tio.-j; — nairyam  '»am  *frazain- am  Y.öS.s;  62.S,  GS.'i-i,  Yt./o.3,  108, 110,    ;Ä5;    —    'naySs^a  paili    vanhuya
9830:'o/  gaonahe  (sd.)  avabarät  .  .  *dann3m   U-A,;  *Vd.  4\  —  nmafum  ..  ä%ravat^ a  va  *vat5  *bar}snv3  vä  paiH  vayhanaAe  ^-S-^i  —  airyamm  :fannU .  ,  'vaiflm
11071:Glieder  sind  verbal:  yBi  ztjvä  (nämL  hitOt) *ar»har3La  bvanticS{sA)\.4^.T.  3)bci allen;  a)  D  im  Ap.;  das  letzte  Mal  steht Uta  statt  cä:  pärsamcä  mädamcä  utä  aniyä dakyiivaf"  Bh.  /.  14.  b)  im  Aw,;  i)  die Glieder  sind  nominal ;  a)  sie  folgen  sich  un- mittelbar: nmänyasca  visyasca  santumasca Y.  if).  18  (s.  dazu  18  aA.);  —  aojasca  v»ty- 'inmca  j^armas^a  lavania  Y.  7/.  8 ;  —  sta- rasca  mäsca  >fe'<i/vi-'(7  YL72,25(s.dagegeni_j. 57);  —  vätftnca  vänmca  tnafy^mca  Jyau- humca  Yt  5.120; — hubprvtlmca  uslaMin- tlmca  vanta.bintTmca  Y.  61. 2  (s.  dagegen  7 ; Sp.  570U.);  —  maziUäsca  vahiitasca  srais- tas^a  asayS  Y.  52.  3;  —  apasca  urvaräsca xadirdsca  Y. A3;  —  asavafom  htnümca bavaniiinla  busyantimla  Yr.lS.i; — vTspayä ..slöis  haihyJica  bavqihyäica  büiyqi^yäica \.6S.i3i  —  nm3nanqmcä  vlsqm^a  satttu- nqmca  dahyunqmca  Y.  Ä  7 ;  —  damayä  anu- matayal'a  aiiuxtayaica  * aim.varstayai^a Y.Ä7;  —  d^aurunqscä  rä^aistiscä  väs- tryqscä  ßuyants  Y.  ig.  3;  Yt  ig.  8;  — ahamca  ratümca  paoirimca  tkaisim  Yt/^J. 152;  —  ha^ra  miiräca  rasnuta  uyraca dämSis  upamana  Yt/_J.  47;  —  vispss^a paiti  vansajls  vTspSsca  paiti  frasparrjJ i'JspSsca  paiti  fravaxsS  Y.  jo.  5 ; — haurva- tasca^  fiö  am)r>täta  gSuica  taSnB  gSusca urunS  ä%rasi-a  aoxtsjiämand  hadisasca  Vr. g.  5;  —  beim  Zahlwort:  navaia  navaittfca navaca  sota  navaca  Aazavra  navasSsca baivqn  Yl;_J.S9.  a)mitTmesis:*«ai/x
11212:•  j.  danat-Caxra-  Adj.  'mit  sausenden  (?) Rädern':  masa  xsä%ra  ..  'ra  (APn.)  YL 5.130.
12627:•}  Soviel  als  8  Hä%ra,  die  Hifle  einer  Yujya.
13153:—  kasna  x^Sng  * str^mcä  däj  advaium  (sd.) Y.44.Z;  —  datat  paiti  draonai  (sd.) flava  datat  V.5.  26;  —  ya  isuds  dadmte (3PKM.)  '^'  dä%ranqm  (sd)  haca  aSäuiiB Y.31.  14;  -^  yqm  daennm  ahurB  .  .  dadät ^•53-^i  50.11;  —  urvaili  datanqm sravanhqmYt.iO.^^.  a)  mit  Dat  comm. : tal  draonB  .  .  yat  ml  da^al^'  ahurB  Y. II.  5;  —  Ayai  mBi  a/a  dam  (2P.)  vahyB Y.31.  5;  —  tä  iiB  data  iä  »rfzväna  (sd.) fravaocama  Y.  70.  2  (?),  3)  'hervor- bringen, produziren':  gaomaH»m  (sd.)  gava dataya  Y.ig.22.  a)  bes.  'schaffend hervorbringen*;  coantjm  srväfatn  main- yava  stis  data  as  (Sp.  276  m.)  V.  2. 20 PüZ.;  —  paurvh  data  dämqn  alaonts  Y. /& 3 ; Vyt 4IJ.  a)mitfin.In£:  nsit  dätB ahmi  nBil  Hst^{%A.)  minte  bar^aca  dalnayäi "ich  bin  nicht  geschaffen . .  zu  hegen"  V. 2.3.  a)  von  den  beiden  Geistern;  _)'a/ maiiiyä  dämqn  dai'iU?m(jiX>'PM.)'''^ yasca spmtB  mainyus  yas!a  at?rB  Y.57. 17,  Yt 13. 76;  —  uva  dqma .  .yasia  da'ätafi''  sppniö mainyui  yasca  da'^ap'^  aarB  mainyus  Yt, '5-43;  —  da'iap^  sp?ntB  mainyus  ..  zrBne akarane  Y.ig.i);^;  —  sp»ntahe  mainyStd dqma  datimY .13.1.  b)  von  den  .i4ot3]^. und  andern  Göttern:  ya%a  n?  data  (2P.) amna   spsnta  a^a  nä  %razdam  Y.sS.^;
13496:KompA.  —  PPfP.  einer  aj.  Basis  dai-;  S  TOg. 7  No.  II.  —  np.  däit');  vgl.  mp.  däi'l;  ksl. daiä  'finden',  vgl.  an.  taia,  got.  leian ;  s.  noch zu  daia-.  —  Pü.:  iart\t.  —  0  Da»  als  PPfP. zum  Praes.  därad  dient.  Vgl.  j.  däilayänay- Und  vindat . .  yäiam,  p.  däraytrvi^us  und  ai. jödädvasuh ;  s.  nach  No.  a.  —  ')  Vr.  ig.  2, S.  Pü.  zu  'dä%ra:  mp.jiän  das  ist  etwa  sva.  mit,/ vindUn;  vgl.  däslayänay-.  —  J)  Vermutlich verkehrte  Umsetzung  des  Ideogramms  fatgn/i.
13719:')  F  1  dar" ;  s.  düraiy  No.  Z.  —  »)  Gemeint in  der  ä%raian.  faiti}a%an-  (sd.).
14311:1  b):  azSmclt  ahyä  mazda  I  %wam  mSAhj faourvTm  vagdjm{sd.)  Y. 2^.11  i—  I  äa-am ai  ai/qm  paityastar^mcä  .  .  dadftnaidl  Y. J5.  9;  —  \%wqm  ahuränlm  yasamaide  Y. 6Ä6  (vgl.3,  Sp.  789  m.);  —  I  %7vqmyazafUe aurva/ths  .  .  I  ^wqm  naraSt  ,  .  I  "hwqm ä%ravara  .  .  I  hwam  kaininS  .  .  I  %wqm äiräiHf..Yt.5.8s'-8T,  —  \^7t/qm  atnm akurake .. yasamaide  Y.ij.io,  25.7;  2.1a, F.2d,  2J(?).  zu  3):(i5'  %wqm  yim
14503:caranaya  astraya  Y.g;  *N.  42,  4;_;,  öp", 83,  log;  —  %rayqm  upamanqm  *_fraväxs- yanqm  N.105;  108,  10^  (wo  %ryqtn)^'>\ —  'üsrqm  (Gf.)  xsafanqm  V.  7.  52  'PüZ.=, *Bd.  jo.  16  Zit;  —  yat  .  .  ä%rasca  ti^rS (Af.)  hraxtis  yaoidd^at  N.  7^;  looQ), F.  7,  N.  42;  —  rfirff  paoiryS ..  tilra  paoirya . .  tisra  haurvapaoirya  (sd.)  .  .  tisra- nqm*^  haurva.paoiryanqm  Vr.  i  j.  3;  i, 3.'  Aa)äräyJals  a)  Nf.5>:  ^<i/-4^^5r5yJ xsafha  sacänte  "^.g-ZZ^  16.Z.  ß)  als An. »:  ärJyff  jfl/d  F.  2_;;  Vd.  ly.  b)  ä«/ als  Nn.**:  para  ml ..  ^fisiif  vahista  anhe astvaite  vHa/a  (sd.)  P.jp.  c)  ii/rff  als
14562:Zum  V.  %rS-.  —  Vgl  %rä%ra-.
15976:*pä%ra-  n.,  lum  V,  pä{yS-%  vgl.  pä%räi\  np, päs,  arm.LW./oA.  — Pü.T/önni  sräyün,  Sü. : /älaJiak.
16319:Vgl.  fauru.3?'ä%ra-  und  S  304  H.  45.  —  Pü. :  | pur  ü^äriA.  I
16778:mächtigen', mit  Akk. :  nöij  tat  x^artnS pairi. abaom  (Augm.)  "nicht  vermochte ich  mich  dieser  Herrlichkeit  zu  bemäch- tigen" YL  ig.  57;  64  (wo  pairi.abavat, Augm.).  3)  'zum  Abschluss  kommen': kva  ta  dä%ra  (sd.)  pairi.bavainti  V.  ig. 27.  Wertlos:  yai  .  .  ^akwärS  mäaAlS pairi  dasa  ayara  bavaiti  (soll  heissen) "wenn  vier  Monate  und  zehn  Tage  (seit der  Empfängnis)  vergangen  sind"  Vd.  i^'**.
17971:•  j.  fra-zantay-  :  'lainti-'''  f.  'Nachkom- menschaft; Kinder':  yat  nmänS.paitlm  vin- äama  . .  •zainilm/a  hs  Vfr?syat  Yt  15. 40; Vd.  ij;  —  istim  vSja^yümi  . .  *'saintlmca y^äparqm  Y.  ö'j.  11; —  sonst  mit  'äsna—. mä  yave  imat  nmSmm  fratahu  . .  istii mä  ^ä%ravaiti  äsna  'zaintisY.  60.  7;  — kahmai  Xitim  .  .  asnqmcit  'tainiim  us apara  banzayeni . .  kahmäi  äsnqmat  'tain- tTm  ha%ra.jata  (sd.)  nijanani  Yt  10. 108—
19061:—  yeAhe  x^a'^räoa  ti-  aotfm  hiaka  »'*  ..' Vtjp.33;  —  yeähe  dä%rahe  daiti  +/(•"'' hmia    urva   *vauräza    N.  S4.  II)    der  I
19305:j.  Hmöi  N.  8-,  lid  nmänäl •  j,nrnäna-,g.,j.''dflniana-'',j.'V;'«ff»a- n.  'Behausung,  Haus',  von  jedem  zum Aufenthalt  für  Menschen  (Götter)  und Haustiere  dienenden  Bauwerk,  sowie  auch von  dem  zu  einem  Anwesen  gehörigen Gebäudekomplex;  I)  von  Wohnungen  fUr Menschen  (und  Götter):  yanyS buyä  'nshu ma^yäkanqm  Y.  6i.\;  —  ahmi  *ne  ya^ m!^ayasnBi^{Stve.Tz.)  V.5.45;  —  vasö.. mazdayasna  ahe  'nahe  myasd>m  äaihyäril V,  &22J  —  ätacäni  sünm  'mm  drvatS Yt-5'  3S;  —  <Mi  'tarn  yim  ^alpaihjm Yt5.63;  62;  —  ha%ra  'ni  avastaya  ka~ t>mca  /raslamb>m{s,ü.)Si  ..  V.  2. 26;  — yat  bä  paiti  nä  a/ava  'mm  uedasta  ä%ra- vai  gaomavat  nsirivat  ..  V.J.  2;  15.  ai; —  mürnm  . .  ylF  stunä  v^ärayeiti  iirtsi- mitahe  'nahe  Yt /O.  28;  30;  —  tBm..°na inasilä  ..  dahähi  YtJO.30; —  sraohm .. yS  driyaolca  . .  amava£  'mm  hüm.täsH  Y. $'j.  10;  —  as>m  yS  ahurB  masda  . .  yas> tat  'npm  ahnmm  srirtm  raoximm  frs- d^rirsrym  V.  22.1^;  \.Sy.2i;  —  iaiiihe ka^he  apayisire  'mm  htitaite  hi^ättm  Yt. 5.  loi;  —  aliqm  "nä  hvihätä  .  .  hUhfUe Vti7.  8;  V./j.  4g;  —  hubaotUl  ba^aite °mm  yeAhe  'ne  asis  varmhi  . .  psta  mda- ^aite  Yt.ij.6;  ij.107;  —  iha  ml  tum (nämL./4/fl)  hamJaranuha  *antary.ar^?m •nahe  srJrahe  Ytzj.öo;  jj.  147, 156';  — alU  . .  ramyai  i%a  upa  tmai  °mm  yat ahüiri  Y./O.i;  6'o.2,  Yt  14.41; — vainti ahmi  'ne  sraesS  Y.  tfo.  5;  Yt7j.  52,  FrD. /3;  —  vUfa  'na  sraoiö.psta  yazamaide  Y. 57-34)  —  damt  ha^a  ahmüt 'nät  ..rhyeja ■  •  ^'yeyenti  yejihe  *'?ya*'  sraoh  . .  astf paiti^ants  Y.57. 14;  /o.  7;  —  mä  yave imat  'mm  i^'annS  frazakXi  Y.60.  7;  Vyt 5;  —  xihsii  äfrlnstttu  {jis-viA.  fravas<rfS) ahmya  'ne  vattuhim  asim  . .  xsnüiä  para- yantu  haca  ahmst  'nät . .  msüm  gtnzänä pärayantu  haca  ahmst  'nät  ahmSkfm^a mazdayasnanqm  Yt  13. 157;  Y.  2j.  3;  — aai  ahmSi  'näi  dähäiti  gluica  vqhwa  vlra- nqm/a  Yt.!0.  a8;  —  äat  ..  ahe  'nahe/ra- pi^iws  gäu^  .  -  Y.  j.  3 ;  —  t^it  ahmi  'ne *sänaite  ä^rava . .  äat  ahmi  'ne  Sayhnte  da- hahaca..Y.ii,6;  — /raddhsi  ahe'naheY. 52.4;  4.5,  Vr./J.  13*;  —  'n?m  hS  manyaita paraJa%B  V.  ;*.  28;  ■ —  (8«  miknäi  daiva *aipi.jaiti  'ne  aiAhai  gundayai  (sd.)  V,  3.
19372:mä  apalma*paurväpaySit(Sp.S'jo\L)  mäK. *»iaSa(sd.)  ia^anna  *paiti.Jime{s6.)  Vr.22. 2; —  ma  dim  mntyä  ä%ravan»m  ..tim  dim mruyä  ä^ravarum  . .  yn .  .Y.1S.1  —6;  — ma  hrayam  vahiStanqm  atwt^yS  buyata  . . %rayqm  acistanqm  amihyj  buyata  V.  t8. 17;  —  ma  mihrake  . .  vaFfai  jasaima Yt  10,  98;  98;  —  mä  buyh  aurvaiqm yaxta  ma*  . .  Y.  11.  7;  g.  29';  —  ma x/ayamna  jasSit  atrrm  ma'  .  ,  Y.g.zyi 'S-49i —  "»ä  mqm  ..fraspaysis  tiX>%.li8\ Yt.  8.  593,  FrD.  4J,  Vyt  12*,  j-j,  J7 ;  — ma  Bs*^  mi ankam  sao^ranqm  vindita yä ..mä  fiarB pairi/ta.xsulrif  mai . .Yt IJ.S4',
```


## [2026-09-05T20:39:01.758Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KNT leaf 181 (p.166) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==182' KNT.txt | head -60"
}
```


### [2026-09-05T20:39:03.500Z] TOOL RESULT

```
=== KNT leaf 181 (p.166) ===
sed him, him- self becoming now king in Parsua, later called Ратѕа. Arsames, however, was not put to death, but (as the OP inscriptions tell us) lived on until after his grandson Darius got the throne of the Persian Empire. Thus Hystaspes never was king, and is not counted among the nine Achaemenian kings. Cyrus II thereafter conquered Media and added it to his dominions, and then extended his conquests in all directions. But he did belong by ancestry to the Achaemenian line; one can hardly brand him as a rank outsider.
Possibly Ctesias’ story, as repeated by Nicolaus Damascenus, originated in the line of Darius as a means of discrediting the line of Cyrus and of. justifying Darius in his seizure of the imperial power. The particular occasion might well be the unsuccessful revolt of Cyrus the Younger against his brother Artaxerxes IT, whom Ctesias served as personal physieian. Cf. JAOS 66.211 (1946).
IL SMERDIS AND GAUMATA
According to Behistan 510-513, Cambyses son of Cyrus killed his full-brother Smerdis, with such secrecy that his death was not known to the people; he then invaded Egypt. While he was on this expedition, rebellions developed in Persia and in Media and elsewhere. Notably a Magian named Gaumata headed the rebels, claiming to be Smerdis son of Cyrus, and he gained the kingship in all the rebellious territory. Cambyses, still in Egypt, committed suicide.
Gaumata started his rebellion in XII 14 of 523/2, and received the adherence of the Empire on IV 9 of 522/1. But Darius, a distant cousin of Cambyses, knowing that Gaumata was not the real Smerdis, with the aid of a few men fought with and slew Gaumata and his chief followers, on
VII 10 of the same year, at Sikayauvati, a fortress in Nisaya, a district of Media. Thereafter Darius became King.
Herodotus tells the same story at much greater length, in Book 3, chapters 1-38, 61-88. Cambyses invaded Egypt (chap. 1), and the reasons for the invasion and the course of the campaign are given (1-26). At Memphis he inflieted a fatal wound on the sacred bull which was worshipped as the God Apis (27-9), and thereupon lost his reason. Jeal- ous of his brother Smerdis’s prowess with the great bow which had come from the Ichthyophagi, he sent Smerdis back to Persia, and then, after a dream which betokened that Smerdis would sup- plant him, he sent his henchman Prexaspes to murder him secretly, which he did (30-8), esp. 30).
160
The Magus Patizeithes had been left by Cambyses as managing steward of his palace at Susa, and he was one of the few who knew of the death of Smerdis. He had himself à brother who greatly resembled Smerdis in appearance, and, says Herodotus, this brother's name was also Smerdis. Patizeithes put his brother Smerdis on the throne, under the pretense that he was Smerdis son of Cyrus and brother of Cambyses. The false Smerdis, by not admitting to his presence any one who had known the true Smerdis, successfully con- cealed his true identity for some time (61-2). But the news reached Cambyses in Egypt, and he knew the truth, because Prexaspes assured him that he had slain the real Smerdis. Resolved to fight the usurper, he leaped upon his horse to lead his army back to Susa, but as he did во he accidentally struck the point of his sword into his thigh, and from the wound he died (63-6). Thus the false Smerdis ruled for some months; but a Persian
OLD PERSIAN
nobleman, Otanes son of Pharnaspes, suspecting his identity, managed by a ruse to prove it to himself (67-9), and secured the help of five other trusted noblemen, to whom there was added Darius, who had come to Susa from his father Hystaspes, governor of Persia (70; see App. IIT). Darius insisted on immediate action against the two Magi (71-3). Helped by the confusion follow- ing the public confession of Prexaspes that he had murdered the true Smerdis, and by his suicide, the seven men burst into the presence of the two Magi and slew them (74-9). They then agreed upon a method of selecting one of their number to hold the throne, and Darius, aided by the trickery of his groom Oebares, was the winner (80-8).
The two accounts, it will be seen, agree in the main features, but differ considerably in the de- tails. Herodotus’ story has clearly entered into t
```


## [2026-09-05T20:39:10.216Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    m=re.search(r'\\batiy\\b',p)\n    if m and 'prep' in p[m.start():m.start()+200] or (m and 'across' in p[m.start():m.start()+200]):\n        print('leaf',i)\n        print(p[max(0,m.start()-300):m.start()+500].replace('\\n',' '))\n        print()\nEOF"
}
```


### [2026-09-05T20:39:12.007Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T20:39:15.232Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(180,200):\n    if re.search(r'atiy', pages[i]):\n        print('leaf',i, [m.start() for m in re.finditer('atiy',pages[i])][:5])\nEOF\ngrep -n \"atiy\" KNT.txt | head -20"
}
```


### [2026-09-05T20:39:16.906Z] TOOL RESULT

```
leaf 188 [1094]
leaf 191 [1114]
leaf 195 [1501]
leaf 196 [2921]
401:patiyazbayam ‘I proclaimed’, with Med. -zb-, but h*zdnam (acc.) ‘tongue’ with OP -z-, both from ТЕ ди; see also $91.
521:abiyajavayam XPg 9, and abijdvayam ХРЕ 40. niyasaya DNb 5, 46, 49, probably for *niyayasaya. [a]fiya[s?]ya DB 4.91, perhaps for *atiyayasiya. marika- DNb 50, 55, 59°, cf. Phi. mérak, Skt.
587:tarsatiy with Iran. tars- because of NPers. (0708, $ despite Av. drasaiti, from is-, both with IE Ж suffix -ske-; but Skt. trásati from "ireseti. 1 cartanaty: the c shows that a front vowel formerly 3 stood immediately after it; therefore car- from Ж *cer- from *ker-. 4 Karka, Gk. Каре, Kapuol; Elam. kur-ga-ap seems ' to have no evidential value. E | valrtaiyaty, if identical with Skt. variaye; see $ Lex. s.v. vart- for reff. ; | $32. Отр Persian ara seems to be established * in the following: E i By cognates in Skt. and Avestan: apataram, $ aparam, para, hamarana-, partaram, and the * verbal nouns -kara- and -bara- as second ele- ments of compounds. | $ By Elamite and other transcriptions: Arakadri $ (or Ark- ?), Arabäya, the final of Nabukudra- ° cara.
709:bavatiy DNb 14, bawatiy DNbv 14.
742:ahániy XPh 47, 48 (Ist sg. subj.) = Skt. dsáni; unless the d is analogical to the d in other forms, such as 3d sg. ahatiy.
764:to Bv. MSLP 23.182-3, in DB 1.66, where he 4 would read adind : adam : (patiydbaram : adam :) 3
771:patiyabaram DB 1.68, perhaps for patiyabaram; 4
996:ái is proved by the compound atiy-à$ ‘he
1106:OP x8dyatiya ‘king’, from pAr. *k$ájatia-; a word of the Median officialdom.
1197:pli ghu- in ОР patiy-azbayam Ч proclaimed’, Av. root zba-, Skt. pres. hudyatt.
1243:pIE *t-ske-ti, OP tarsatiy ‘he fears", Av. darasaiti. pIE *jnóskéti, OP xknasatiy ће may know’, Lt. gnóscel ‘he will learn’, pIE *im-ske- in OP dyasata ‘he took as his own’, Av. pres. yasaitt, Skt. yácehati. pIE *y-sketi, Skt. rechdti ‘he moves’; but OP imf. arasam ‘I went off’ from *re-ske-. pIE *yek-skoi, if ей" is to be normalized vasaty rather than vasiy; see Lex. s.v. vasiy. $98. Tux PIE VELARS AND LABIOVELARS IN PÁR. fell together into one set of velar stops ($73.IT), which then split into two series by the Aryan Law of Palatalization ($73.IIT): palatals é ch $ gh, before pIE č #2; velars k kh g gh, else- where. The sounds therefore reached the follow- ing stage in pAr. (in Skt. the aspirates were sub- ject to the dissimilation known as Grassmann’s Law, §73.IV; and gh and gh, where not so changed, often became Skt. л rather than gh and jh):
1496:pIE ghy: patiyazbayam, Мейтат.
1520:*teu- in taumd ‘power’, u-lava ‘having good strength’, fauviyé ‘stronger’ (for taviyd, 548); *tu- in tunuvd ‘powerful’; (Ar.) *täu- in tavay- atiy ‘he is strong’.
1523:*bheu- ‘become’ in bavatiy ‘he is’; *bhu- in biyā ‘may he be’.
1529:*dher- or *dhr- in adarsty Ч held’; *dhr- in duruva- ‘firm’; (Ar.) *dàr- in dárayatiy ‘he holds’.
1569:xkayatiya ‘king’, to -azsayaty Ч ruled’.
1579:The ethnic Pátisuvaris (to patiy ?).
1628:*pahahy > *#ahy ‘thou sayest’, whence by an- alogy *#ahatiy > 00у ‘he says’.
1638:$133. Encursis is a frequent phenomenon in OP. The enclities are the following: Pronouns: Ist sg. асе. -md, gen. -maty, abl. -ma. 2d sg. gen. -taiy. За sg. acc. -йт, gen. -Saiy, abl. -$a; pl. acc. -&$, gen. -Sàm. acc. -dum; pl. acc. -di$. pl. aec. -àà (dubious; only in avabasa-lé DB 4.72), Coordinating conjunctions: -eà ‘and’, -vë ‘or’. Postpositions: d, patiy; both also as separate words before or after their nouns. Adverbs and particles: -am, -kavy, -ciy, -dty, never separately. -apiy, -paliy both also separately. Miscellaneous: уа in mátya DB 4.43, 48, 71; yadatya XPh 35f (miswritten yadàya XPh 39), cf. yada : tya XPh 29. müm, elsewhere orthotone, in mātyamäm DB 1.52. rádiy in avahya-radiy DB 1.6f, etc.; also separ- ately. Double enclisis: mé-tya-mém DB 1.52; rauca- pati-vd,, DB .1:207 aatpati-mé DNb 20; avā-
1654:nai-mà, nai-maty, nai-$im, nat-pati-mà, pali-maty, iyat-Saty, imat-vd, yadi-patiy, yadi-và, [us}i-ca; similarly in phrasal compounds, pati-padem, ni-padiy. By analogy, naty-di§ DB 4.73, 78.
```


## [2026-09-05T20:39:24.587Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\np=pages[188]\ni=p.find('atiy')\nprint(p[:200])\nprint('...')\nprint(p[max(0,i-1500):i+800])\nEOF"
}
```


### [2026-09-05T20:39:26.244Z] TOOL RESULT

```
’, as taken by ТИМ. Aiw 322-3; otherwise Hz. Ap! 191-2: hadtya- ‘truth’, with late loss of h-, + deriv. of d-baud- ‘be fragrant’, cf. Av. baoót- ‘fra-
OLD PERSIAN
grance’, therefore ‘having the fragra
...
’, as taken by ТИМ. Aiw 322-3; otherwise Hz. Ap! 191-2: hadtya- ‘truth’, with late loss of h-, + deriv. of d-baud- ‘be fragrant’, cf. Av. baoót- ‘fra-
OLD PERSIAN
grance’, therefore ‘having the fragrance of the truth’).  <Aé@iydbausinahya gsm. Sa 4-7.
Aéura sb. ‘Assyria (and Syria)’, a province of the Persian Empire ($6, $106.11): Elam. aš- &i-ra, АКК. áš-šur, Gk. 'Аттурв‚ but Aram. абиг. Aéuré nsf. DB 1.14f; 2.7; DPe 11; DNa 26f; DSe 26°; DSm 7°; XPh 22. Aéurayd lsf. (5186) DB 2.58f.
A@uriya- adj. ‘Assyrian’: deriv. to preceding .
($144.1), perhaps with vriddhi in first syllable (8126; Aburiya- ?). A@uriya пет. DN xvii; DSf 32; А?Р 17.
Agina- sb. ‘Acina’, ап Elamite rebel: Elam. ka-iš-ši-na, Akk. a-Si-na. Either borrowed from Elam. (Foy, KZ 37.498); or shortened from an IE name beginning with OP äç- = Av. átar- 007- ‘fire’ ($147.11, §152.1), ef. atoro-dáta- ‘Fire-given or Fire-created’ and other names (Vd. 18.52; Justi, INB 50; Bthl. AiW 324). Agina пет. DB. 1.74, 82: 4.10; DBe 1f. Acinam asm. DB 1.76.
Ld
A ciyádiya- adj. ‘Aciyadiya’, the ninth month, .
Nov.-Dec.: Elam. haššiyatiyaš, АКК. kislimu, Cpd. of átar- ‘Are’ + deriv. of yad- ‘worship’ ($126; $152.D: ‘Fire-Worship Month’. Agiyddiyahya gsm. DB 1.89; 3.18.
ada- adv. ‘then’: GAv. ald, LAv. ада, Skt. .
ба ‘therefore’ cf. Gk. трбе-бє (and -Gev) ^n front of’: pIE *e-dhe, to root in *a- ($76.11; $191.II); see also adakaty. — ada-taiy DNa 48, 45.
adakaiy adv. ‘then’: OP ada- + -kazy, Gk. aly. то ‘somewhere’, pIE *q¥ei, Isn. to int.-indef. stem ($135). DB 2.11, 24; 4.81, 82; DNb 38.
adam pron. “Р: Av. azam, Skt. adm, plE .
*eühom ($109), ef. pIE *ейб in Gk. yo, Lt. ego (8193.1). adam nsm. AmH 5,8; AsH 14; CMa 1; DB 1.1, 10, 12, 39, 52, 54 bis, 56, 59, 60, 62, 63, 64, 66, 67, 68 bis, 70, 72, 73, 75, 18, 82, 83, 86, 89, 91, 95; 23, 5, 6, 10°, 11, 15°, 19, 28, 30, 48, 50, 68, 64, 69, 72, 80, 81, 88; 3.1, 13, 25, 29
```


## [2026-09-05T20:39:33.424Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (189,190,191):\n    p=pages[i]\n    for m in re.finditer(r'\\bati[yv]\\b', p):\n        print('leaf',i,'|', p[max(0,m.start()-200):m.start()+450].replace('\\n',' '))\n        print()\nEOF"
}
```


### [2026-09-05T20:39:35.078Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T20:39:38.170Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (189,190,191,192):\n    p=pages[i]\n    print('=== leaf',i,'first 300 ===')\n    print(p[:300].replace('\\n',' '))\nEOF"
}
```


### [2026-09-05T20:39:39.759Z] TOOL RESULT

```
=== leaf 189 first 300 ===
n., asn.); AÁuramazdü, АМ; ava (nsn.); avdkaram, avükaramca-; ucdram; uld, uta-; tya (nsn., asn.); dahydus; duvarayd; nat-; pati-; pasdva; уава; haw, hau-: Asl 12; DB 1.25 bis, 55, 87, 94; 2.24, 34, 40, 45, 54, 60, 68, 75, 79, 86, 90, 96; 3.6, 11, 17, 37, 441, 61, G6f, 87; 4.39, 46, 60, 64; DPd 28°;
=== leaf 190 first 300 ===
. Skt. apa, Gk. and, Lt. ab, Gt. af, Gm. ab, NEng. оў, off, pIE *apo. Used with vb. gaud- and in sbb. apaddna-, apa- niydka-; with suffix in apalara-, apara-. apataram adv. ‘farther off, far off’; nsn. of apatara-, which is apa- + comp. -fara- ($82, 5190.111), ef. Gk. adv. ётотіро. DNa 18; DSe 16f; 
=== leaf 191 first 300 ===
 formed like Gk. &exero to root *segh-, ёттєтө to root *pet- (JAOS 62.269; 855.IT, §103.I1). amala adv. ‘thence’: demonst. stem ama-, found (though rarely) in Skt., + adv. -tos, as in Skt. tátas ‘thence’, Gk. ёктоѕ ‘outside’, Lt. caelitus ‘from the sky’: Buck, Lg. 3.4-5; Jn. quoted by Gray, JRAS 192
=== leaf 192 first 300 ===
-, GAv. angra-, LAv. apra- ‘hostile, enemy’, to рАт. root *ans-, seen in Av. qsta- ‘hate, enmity’; ef. also Av. (nom.) avrd mainyus ‘evil spirit, Ahriman’ (Bthl. AiW 189); not to Skt. art- ‘en- emy’ (MB Gr. §273), nor to Skt. alikd- (Wacker- nagel, KZ 59.28-9). алка nsm. DB 1.22, 33; 4.63. ага npm.
```


## [2026-09-05T20:39:50.978Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(188,200):\n    p=pages[i]\n    for m in re.finditer(r'beyond|across', p):\n        print('leaf',i,'|', p[max(0,m.start()-450):m.start()+250].replace('\\n',' '))\n        print()\nEOF"
}
```


### [2026-09-05T20:39:52.518Z] TOOL RESULT

```
leaf 191 | Gray, JRAS 1927.101: ef. Kent, JAOS 51.231. Hardly, with Gray, JRAS 1927.99-100, and Hz. ApI 65-6, the same as Skt. abl. asmat remade to *asmatas, with -tos ending. DPh 6, 7; DH 5, 6. отида, see maub-. ay- vb. ‘go’: Av. ay- (pres. aiti), Skt. i- (pres. éti), Gk. «о, Lt. it: conj., §208. Cf. also youviyd-. айу ($69) DZe 10. aii imf. (§72, 6228.11) DB 1.98; 2.67; 3.35, 43. à + ay- ‘come’: aya"là 3d pl. imf. mid. ($181, $208) DZe 11. ali- + ay- ‘go beyond, go along’: aliyäiš imf. (872, 8122, 5298.11) DB 3.73. upa- + ay- ‘go to, arrive at’: [ulpayam Ist sg. imf. (8122, §131, 8226.IT) DB 1.91f. 169 upari- + ay- ‘behave, conduct one's self’: upa- riyü[ya]m 1st sg. imf. ($122, §226.1T) DB 4.64f. ni
```


## [2026-09-05T20:40:14.316Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (188,189,190):\n    p=pages[i]\n    for m in re.finditer(r'\\bal[iı]y?\\b|\\bat[iı]y?\\b', p):\n        print('leaf',i,'|', p[max(0,m.start()-150):m.start()+350].replace('\\n',' '))\n        print('---')\nEOF"
}
```


### [2026-09-05T20:40:16.142Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T20:40:18.826Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(pages[189][:3000])\nEOF"
}
```


### [2026-09-05T20:40:20.474Z] TOOL RESULT

```
n., asn.); AÁuramazdü, АМ; ava (nsn.); avdkaram, avükaramca-; ucdram; uld, uta-; tya (nsn., asn.); dahydus; duvarayd; nat-; pati-; pasdva; уава; haw, hau-: Asl 12; DB 1.25 bis, 55, 87, 94; 2.24, 34, 40, 45, 54, 60, 68, 75, 79, 86, 90, 96; 3.6, 11, 17, 37, 441, 61, G6f, 87; 4.39, 46, 60, 64; DPd 28°; DPh 8, 10; DNa 50 (m° omitted, $52.VI), 52#, 544; DNb 13, 28, 28f, 31, 32f, 33, 48, 51, 52; DSe 51°, 52°; DSE 10, 19°, 20°, 58; Ds} 4°, 6°; DSk 5; DSI 4f; DSm 3°; D8s 7°; DSt 9°; DH 6, 8; Хра 15, 18f, 191; XPb 24, 29, 30; XPe 13 bis; ХРа 18f, 19; ХР 32, 38, 41, 45f, 47; XPg 14; XPh 32, 45, 58,
167
60; Хе 5° bis; XV 261°, 27°; A!Pa 23°, 24°: A’Sdb 4 (-may de, $52. VT); А?Не 20 bis.
-ma gsm. for -maty ($198.11); apan*yáka-ma А?За 3; [n"yà |kama for n*yàkam-ma (5130) A’Sa 4. Not kamna-ma DB 2.19, as taken by Tolman.
-ma absm. enel. (Av. maf, Skt. mat, pIE *med, $193.IV; orthotone pIE *méd in oLt. méd, elLt. mē); only in hacd-ma DB 1.19, 23; 2.6, 12°, 16, 98; 3.27, 78, 81; 4.92; DPe 9; DNa 20; DSe 19°; XPh 18. Not duviliya-ma DB 3.24 (with Bthl.); not apara-ma DB 4.37, 68, 87 (with Bthl.), nor DSt 10°.
vayam npm. (Av. vaém, Skt. vaydm, рї Е *uei + pAr. -am, cf. Gt. wei-s; §193.V) DB 1.7, 10°; DBa 10, 17.
amazam gpm. (Ау. ahmakem, Skt. asmákam; $118.11, §193.VI) DB 1.8, 28, 45, 49, 61, 69, 71; DBa 12.
Adukanaisa- adj. ‘Adukanaisha’ , first month, March-April: Elam. ha-du-kan-na-1§, АКК. nisannu: -natsa- on the evidence of the Elam., acc. to MB Or. $96, rather than -nisa- ($117). Cpd. of adu- ^ + kan- ‘dig’, possibly with vriddhi ($126; Adu- ?): "Irrigation-Canal-Cleaning Month’, re- ferring to the cleaning of the underground con- duits for irrigation water, regularly done in the spring (cf. РЕШ. AiW 61). Adukalnaz]Sahya gsm. DB 2.69.
an- neg. prefix before vowels, ef. !a- before consonants: Ау. Skt. an-, Gk. &»-, Lt. in-, Gt. un-, pIE *on- (867.1); in Anáhatà-.
and ism. to ?a- (q.v.); DPe 8 (not to Av. Skt. ana-); XPa 14 (not prep.).
Anàümaka- adj. ‘Anamaka’, tenth month, Dec.-Jan.: Elam. handémakas, АКК. febétu. Cpd. of neg. a- + ndma- ‘name’ (see ndman-) + adj. suffix -ka- ($146.11), possibly with vriddhi (8126; Anámaka- ?): ‘Month of the Nameless (= High- est) God’. Anàmakahya gsm. DB 1.96; 2.26, 56; 3.63.
Andhita- sb. ‘Anahita, Anaitis’, a goddess: Elam. a-na-hi-ud-da, Akk. a-na-ah-t-tu-’, Gk. ’Avairs; Av. andhitd-. Cpd. of neg. an- + pte. pass. dhita- ‘spotted, defiled’, of uncertain connec- tions (§67.J, §118.V, §242.1): ‘The Spotless’. The OP writings, being late, fail to show length of б in either position. Anahita (827, $52.11) nsf. A’Sd 3f; Anah*ta, A’Sa 4 (as gen., §313.11), 4f; A?Ha 5° (as gen.), б.
4
168
antya- adj. ‘the one or the other (of two), other (of any number), rest of’ (JNES 3.2334; not ‘enemy’, cf. Kent, JAOS 35.345.n6 and Bv. TPS 1945.56-9): Av. ainya-, Skt. anyd-, pIE *anjo-, cf. *аЦо- in Gk. ados, Lt. alius, and *an- tero- in Gt. anpara-, Gm. ander, NEng. other (889, 144.1, $204.17; decl, $203). aniya nsm. DB 1.95; 3.32; DSe 33°,
```


## [2026-09-05T20:40:41.744Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(pages[187][-3000:])\nEOF"
}
```


### [2026-09-05T20:40:43.687Z] TOOL RESULT

```
 text, ef. NPers. ágür in the same meaning. alg|ura[và] Ism. DB 4.89 (restored by Kent, JAOS 62.267, after König, Klotho 4.45); but read амуй аһа with Cameron.
agriya- adj. ‘topmost, excellent, loyal’: Av. ayrya- ‘first in quality, etc.’, Skt. agriyd- agryd- ‘foremost, principal, etc.’, deriv. ($144.1V) to Av. ayra ‘der erste, oberste; (nt.) Anfang, Spitze’, Skt. dgra- ‘foremost, prominent, best; (nt.) tip, sum- mit, best part’ ($148.I). agriya пет. DB 1.21, as read by Cameron, replacing KT’s ag*r^ ++ (and the restorations thereof: dgar[ia] Wb. ZDMG 61.725, Tm. Vdt. Stud. 1.9, ef. Bthl. WZKM 22.72; ágra"|6a] Jn. Indian Stud. Lanman 255-7; ügr[mata] Konig, RuID 65; ágr[mà] Hz. Арі. 59- 62).
aciy adv. ‘then, at that time’ ($291.1V): Av. ajčit ‘and indeed’, Lt. ecquid (interrog.) ‘anything’, pIE *ed-g*id, see *a- ‘this’ and particle -cty ($105, $130; Ву. BSLP 33.2.152-3; Hz. AMI 4.125-6, 8.41, ApI 55-6; Wb. ЖА 41.319). ХРЇ 21.
Atamaita- sb. ‘Atamaita’, an Elamite rebel: Elam. Atameta (854.I, §76.V; Hüsing ар. Prašek,
166
IMP 2.78.08; König, Кир 78; not Umamaita after the Ummaima of Oppert, Médes 158, based on Rawlmnson’s J-im"im*^, later altered by KT's тт). {[Ajtamacta nsm. DB 5.5.
_ ütar- sb. ‘fire’: Av. diar- dór-, NPers. абат; in Á ciyadiya- and verhaps in Acina- ($152.Г).
atar (i.e. ачат), prep. with ace., ‘within, among’: Av. antara, Skt. antar, Lt. inter, pIE tenter (831). DB 1.21; 2.78; 4.32, 92; XPh 30, 35.
ali-, prefix, ‘beyond, across’: Av. aiti, Skt. dti, Gk. ёт ‘yet, longer’, Lt. et ‘and’, pIE *eti ; with ay-, yam-. Cf. also айту.
abaga- (ie. аба"да-) sb. ‘stone’: Av. asanga-, NPers. säng, cf. OP asan-, asman- (S87, S151, $155.1); see also a(againa-. afagam asm. DSf 24, 48.
abagaina- (Le. aba^gaina-) adj. ‘of stone’: deriv. of абада- (147.11), perhaps with vriddhi (§126; déagaina-?). alagaina nsm. DPe. abagainam asm. D'Sa 1; A*Hb. afagainüm asf. ASe 6; abagandm asf. (852. VI) for nsf. (856.V) A’Pa 22. afagainiya прі. (S152.IT, $179.11, $190.I; JAOS 53.20; wrongly Konig, Burgbau 68; not abagainiy nsf. to sg. collective stind, as taken by Hz. AMI 3.68) DSf 45.
Gahavaja, word of unknown meaning, DB 4.90 (reading of KT); hardly, with Morgenstierne, Acta Or. 1.252, d@a*ha-vaja ‘word, speech of proc- lamation’, ef. Skt. aqsd- ‘hope, expectation’, + vacas- ‘word’. Perhaps G@aha- (§143.1; with Morgenstierne) + root-noun vaj- ($142) ‘procla- mation-strengthener, seal’, gsm. (JAOS 62.268; not abl. as instr., with Konig, Klotho 444—5).
abiy prep. with acc. ‘to’: DB 1.91. Apparently doublet to айу (Ву. Gr. §102), possibly by con- tamination of *a; antevocalic and ati antecon- sonantal, in sandhi ($80; Mt. Gr. $103).
Aéiydbausna- sb. ‘Athiyabaushna’, father of Arsaces ($168.11): cpd. of (Av.) ai- ‘destruction, misfortune’ + pass. pte. of d-baug- ‘to free’ ($248) with late -šn- from -aén- (Bv. BSLP 29.2.104, cf. Av. pouru-baozóna- ‘bringing abundant rescue, Bthl. AiW 901): ‘Freed from misfortune’ ($160.14; not active ‘bringing freedom from misfortune
```


## [2026-09-05T20:40:54.057Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### PHD xwar\"\ngrep -n \"xwār\\|xwar\\b\\|dušxwār\\|dušwār\\|duš-xwār\" PHD_mackenzie.txt | head -20\necho \"### PHD file2\"\ngrep -n \"xwar\" PHD.txt | head -20"
}
```


### [2026-09-05T20:40:54.135Z] TOOL RESULT

```
### PHD xwar
158: ~~ ~wl represents xwar 'sun', but to transliterate it ·xwr
1124:anOs-xwar [)nwshwl] mortal.
3806:nixwar- [nswb'l- I M nyxw)r-] hasten.
3937:padIsxwar [ptfhwl] dish, bowl.
5615:txwar [hwll M xwr, N .......] sun; cal. 11th day.
5616:lIxwar [hwl = Av. XVam-] a degree of sin.
5617:xwar-, .......isn, v. xwardan.
5620:Zxwar [hw'l I M xw'r] food.
5624:xwar-bir [hw)lb)ll M xw)r w b)r, N .......] food and drink.
5625:xwardan, xwar- [OSTEN-tn l < A )Ith,"; Ilh; hwltn l 1M xwrd7l, xwr-,
5636:xwaridan, xwar- [hzv)l-ytn l ] drink.
5646:xwar(x)Aed [hzv[(h)syt I M Xfvrxsyd, N xursed] sun.
5881:abject xwar.                              adjutant P hdmharz.
6101:bowl padisxwar, tast.                  bucket dol, hezag.
6423:dish padisxwar.                         doubt guman(ih), waromandih; cast-
6474:easy asan, sabuk, xwar.                      entertainer huniyagar.
6617:food castag, nan, pih, xwar, xwardig,        francolin kabkanjir, por.
6732:guest mehman.                            hasten awistiiftan, nixwar-.
6975:   fragandan.                             light (a.) rosn; (weight) sabuk, xwar.
7077:mean pen; xwar.                            mighty kardagar, sezdcn, tuwanag;
### PHD file2
32:Sincethe ambiguities ofthe script make a mechanical translitera- tion of one letter by one roman symbol of no practical value, a certain amount of interpretation is essential, This interpretation can be based, either directly or by the use of analogy, on the less ambiguous evidence of the above-mentioned earlier documents of the language. With this help it is possible to go far in distin- guishing between the original values °’, й, dy, etc., of -», n, w, Р of у, and so on. But it is neither necessary nor desirable to go beyond this by attempting to give closer “phonetic” values to the letters, such as r for written /, or x for written h. For example, Sy hwl represents xwar ‘sun’, but to transliterate it *xwr entails both confusion with the true letter r \ and the introduc- tion of even greater ambiguity into the interpretation of .». It is better to accept that the scribes wrote r and / almost indis-
155:xwarg ... add live coal. yazd ... read yazad ... N izad, yazd. yazdan ... read yazadan ..
212:anērān [?7°3?n'] non-Eran, the world beyond Eran. an-érang [?n’ylng] blameless. an-espās [’nsp’s] ungrateful. ~ih: ingratitude. 2 AY angubén [DW BS Y.A < A dbf ; ?ngpyn! | N angubin] honey. By? Wat), angür [AN BE < A ‘nb’; ?ngwl | N ~] grape. А AC k angust Pngwst! | (N angust)] finger, toe; unit of length (š in.). Va м ~arig [-lyk'] finger ring. „bān [-p’n'] finger-guard, -stall. anidan, ānay- [HY TYWN-tn! < А hyty, ^? th; ?nytn!] bring, lead. anig Payk! | (N pēšānī)] front, forehead. anī-z [AH RN(y)e, v. any | N niz] other also. anjir Pncyl | N ~] fig. anódag [nwtk! | M ?nwdg] strange, alien. ~ig [-yk'] foreign. ünóh, *ànóy [TME < A tmh | M ?nwh, ?wy] there. an-dst Pwwst'] infirm, unreliable. anos [nws] lit. immortal, i.e. the next life; elixir, antidote. — xwardan : risk death, fight to the death. anošag Pxwšk! | M ?nwsg, N ~a] immortal. «ii: immortality. ~-ruwan [-lwb’n'] the late, deceased. an-Ošmār [?7wsm’l] countless, innumerable. anó$-xwar [поў] mortal. *апбу, v. ānēh. anSahrig [nstr'yk'] slave. an-umméd P7wmyt! | J *nwmyd, N nauméd] hopeless, despairing. an-uspurrig [^r wspwlyk') imperfect. any [AH RN < A *hrn; (corruptly, 2К?у = *dn-i) | M ?n()] other. a-pattüg [ptwk!] impatient. a-paymān (?ptm?n!] immoderate. ~ih : immoderation. *apédag [ругА! | P?pyd(g)] lost, stray. ~dar [-d?/] custodian of stray animals. a-petitig žtytyk!] unrepentant, unconfessed. 7h : unrepentance. a-petyürag Pf(y)tyd'lk'] without misfortune, unassailed. a-pohisn Pwhšn'] incorruptible. appar [?5/ | М ’pr] robbery, theft. appar ['P?/] taken away, removed. ~ih : removal, loss, deprivation. apparag [25/6] robber. appurdan, appar- [YHNCLWN-tn' < A yhnslwn, V asi: >pl- | M эрит, *p(w)r-] steal. ~išn: stealing, theft. a-pursišnīg Ppwrsinyk'] irresponsible.
223:āwēnišnīg : blameworthy. a-wēnišnīģ Pzwynšnyk'] invisible. awérag [”wylk!] = awērān. awērān Pwyln', ?5yPn! | N wērān] desolate, ruined. awestad ['zos??t! | M *zxoyst?d, N ēstād] master (craftsman). awestām [*wst?m | M ?wyst?m] province, district. awestarag [”wstlk! | N ustura] razor. awestardan, awestar- [*xvst/-tn! | P °wystr-, N suturdan] wipe; shave. mišn : wiping. awestwār Pwstwb’l | M ?wystw?r, N ustuwār] firm, reliable. “Аһ: reliability, firmness. awēšān [OLE?n, у. бу | М юу п, N ēšān] they, those. a-wināh Pwrs] innocent. a-winast [”wnst'] unharmed, immaculate. awiš [wbš | M ?wys] to him, it; postposition (= ©) to. awištāb Puwst*5 | M ’wyst?b, N šitāb] oppression. P awištādan, awišt- ['zoft2tn! | P ?wyst!dn] stand. awištāftan, awištāb- ['wi?j-tm | M ?wyšt?b-, N sitāftan, šitāb-] oppress; hasten (tr.). tāwištan, tāwāš- [HTYMWN-tn! < A Мут, V htm; ?wbstn' | M *wyšt] seal. a-wiyabanig Pwyd?f?nyk! | N biyābānī] astr. fixed (star). a-wizirignig Pweylinyk'] unavoidable, inevitable. āwurdan, awar- [YHYTYWN-in' < A hyty, У № | M wrd, "wr-, N ~] bring. āxēzīdan [>лусуѓп!] = āxistan. āxistan, āxēz- Phstn', ?hyc- | М *xyst, ?xyz-] rise, stand up. Axrámidan, āxrām- >А?т-уѓп! | M ?xr’m-, N xiram-idan] stride, strut. axtar [Atl | M *xtr, N ~] star, constellation, sign of the zodiac. axtar(ā)mār [Phil(?)m’/] astrologer. ~th: astrology. laxw Dell being, existence, world. ?axw Phw! | M *xvx] mind, will; vital force. *axw Phu'] lord. a-xwamn [’hwmn'] sleepless. axwān Phw’n'] = захм. a-xwārīh ['Aw'iyh] unhappiness. āxwarr [hwi | N àxur] manger, stable. --Sālār [-srd?I] head groom. a-xwaš [D BS YM] unpleasant; unhappy. ~ih: unhappiness. a-xwēškār [kwyšk'I] undutiful. ay Dy | N —J that is to say. āy-, у. amadan. ayāb [уор | М ik, N уд] or. ayāb- v. ayāftan.
318:^-éwüzih [-yxw'cyk | (M dwšw'cyh)) evil speech, calumny. ~+farrag [-plg | P dwéfr] unfortunate. ~-farragih : misfortune. ~-gowisn [-gwbsn'] of evil speech, ill-spoken. ~-humat [-hwmt'] evil thought. ~-hixt [-Awht' | M dwfxwptyy!] evil speech. ~-kām [-2’m] ill-will, malevolence. ~-kanig [-knyk'] hag. — kar LAT difficult. ~-kuni&n [-kwngn'] of evil behaviour, ill-doing. dušmat [dwfmt! = Av. dufmata- | M dw$mtyy!)] evil thought. dušmen [dwsm(y)n' | = M, N dušman] enemy. ~ih: enmity. „ādīh [dušmntyh | M dwkmny’dyh, J dwfmn'dy] enmity, hostility. duš-|-menišn [dwf-myntn!] of evil thought, ill-thinking. --nàm [->”m | N ~] abuse, insult. dušox [dwshw! | M dtws(w)x] hell. ~ig [-yk'] hellish. duš-pādixšā(y) [dušp*thš*(d)) evil ruler. ~th: evil rule, misrule. dušrām [dwsl())m] unhappy. ~ih: unhappiness. dušwār [2001 | M dwšw”r, № ~] difficult, disagreeable. ~ih: difficulty, trouble, misfortune. du&-|-wir [dws-wyl] evil-minded. ~-wurréyisnih [-wlwdsnyh] heresy. c-.xém [-hym] evil-natured. ~-xwadiayih [-hwt'yh] misrule. ~-xwar Lea! | N ~] = dušwār. dušxwaršt [до оной! | M dwkxw styh!] evil deed. duxt [BRTE < A brt-h; dwht' | M dwxt, N ~] daughter. ~ar [dwhtl | N ~] daughter. duz(d) [GN BA < A gnb’; dwc(t) | M dwz, N duzd] thief. ~th [dwe(d)yh] theft. duzidag [dwcytk'] stolen; intercalary (days). duzidan, duz- [dwe-yin' | N duzdidan] steal. dwārīdan / dwāristan, dwür- [dwP?l-ytn!, -stn! | M dwr-] run, move (daevic). ~išn: abode (of demons), hell. dwāzdah [dw'cdh | M dw'zdh, N duwazdah] twelve. ~ап [-’n'] the zodiac.
325:farr-, v. xwarrah. Farrūbāģ [plwb(’)g] the first major Fire of Sasanian Eran, that of priests and nobles. farrox [plhw' | M prwx, N ~] fortunate, blessed, happy. ~ih: fortune, joy, happiness. filāsūfā [pyPswkp!y] philosopher. frabih [plpyh | (P frbyw), N farbih] fat, stout. Fradadafš [pldtpš = Av. fradašafšū-| the south-eastern continent of the earth. fradág [MHL < A mhr; ИРА! | N farda] tomorrow. frādahišnīh [pP dhšnyh] increase, progress. fradom [AWLA < Ar. !?wD; pltwm | (M prtwm)] first. ~th: first, beginning. fragan [plk?n'] base, foundation; origin. fragandan, fragan- [plkn-dn'} lay foundations. frahang [pl’hng | N farhang] education; knowledge. --estàn [-st?n!] school. frahanj-, v. frahixtan. frahist [p/h(y)st! | (M pryst)] most (superlative of freh), frahixtag [plhhtk' | N farhixta] educated, trained, skilled. frahixtan, frahanj- [plhhtn', pDhnc- | P frhynj-, N far~] educate, teach, instruct. framādār [рж?РЦ commander, ruler, chief. framān [pim^n! | M frmn, N farman] order, command; a minor degree of sin. ~-burdar [-bwlt?l | N -bardār] obedient, submissive. framāy-, ~išn, v. framüdan. framds [bl(?)mwš | M pr’mws, N farámos] forgotten. framošidan [plmwšytn'] = framuštan. framüdan, framāy- [plmwin', plm'd- | M prm'dn, prmy-, N far~] order, command. — $n: order, commandment. frāmuštan, frāmēš- [pl(?)mws-in' | M prhmwst, pr’mwi-, N fard~] forget. franaftan, *franam- [pinptn!, *plnm- | M prnpt, prnm-] go, proceed, depart. franāftan, franām- [pin!ptn!, pli m- | P fri m-] 1. lead, conduct, re- move, promote; 2. profess, propagate (faith). ~išn: removal, promotion, profession. frarast [p/”Pst'] a cubit (18 in.). fràrón [p lwn'] righteous, honest. ~ih : righteousness, honesty. frasang [plsng | N farsang) parasang (4 Roman miles).
538:pādīrān [p'igP n!] restrained, held back. pādīrān(ēn)īdan, pādirān(ēn)- [þptgľn(yn)-ytn'] restrain, impede. padīriftan, padir- [MK BLWN-tn!Ü < A mqbl, V qbl; ptgl-ptn! | M pdyr-yptn, N paóiruftan] receive, accept. ~išn: reception, acceptance. īpadisār [ptys' | N padīsār ?] beginning, basis. tpadisār [ptys’/] bridle, halter. padisāy [pts’d | M рдуу] on account of, for the sake of. padist [ptst! | P pdyst] promise, vow. & (abar) burdan: promise. padistadan, padist- [ptyst-”tn! | (P pdystwd)] promise, vow. padistā(£) [ptyst*k! | (M pdystw)] = padist. padiš (pts | M pdys] to him, it; postposition (= pad) to, etc. padištān [pryst?n' | P pdyst??n] leg. padišxwar [ptshwl] dish, bowl. pādixšā(y) [SL Y TA < A йур; p’ths?(d) | M раху] ruler; powerful, authoritative, authorized. ~ЛЬ : sovereignty, authority. pādixšīr [p’thsyl] agreement, treaty. pad-néróg [PW Nnylwk!] strong. pad-niģerišn [PWNnkylin'] cared for, guarded. pādofrāh [p’twpl’s) = pādifrāh. pad-panag [PWNpnk!] guarded, protected. Р pádrazm [p’tlcm] battle. pàd-rózag [p’tlwck' | M p'drweg] fasting. pād-uzwān [p’??wzw’n'] reticent. ~ih: reticence. pad-wizén [PW Nwcyn!] choice, select. pādyāb [pty | N ~] ritually clean; ceremonial ablution. ~ih : ceremonial ablution. pādyāwand [p?tyd’wnd | J p'dywnd] strong, powerful. cAh : strength, superiority. pádzahr [p’tzhl | N pa(d)zahr] bezoar, antidote. pad-zyān [PWNzyd"?n'] harmful. pafšār- [pps?/-] shame. pafšīr- [ppsyl-] be ashamed. ~i8n(ih): shame. pah [p’h] sheep. ~ast [-st'] sheep-fold, -pen. pahikaftan, pahikaf- [ptkp-tn! | M phykf-] fall on, touch, hit, attack. ~išn: attack, fight. pahikāftan, pahikāf- [ptk’p-in'] throw on, make fight. pahikar [ptk] | M phykr, N paykar] picture, image. pahikār [ptk?! | M phyk”r, N paykār] struggle, battle, dispute. īpahikār- [ptk?/-] fight, contend with, defeat. pahikardan, *pahikār- [ptk’/-tn'] request, claim, consult.
551:pillagan [plk’n' | M pylg, N ~] steps, ladder. pim [pym] pain, pang, sorrow. ~gén [-kyn'] sorrowful. pir [руі | N ~] old, aged, ancient. ~ih: age. piring [pling | M pryng, (N pirind)] monochrome damask, pist [pst! | N ~] browned flour. pistag [pstk! | IN pista] pistachio nut. pišīz [pšyc | N ~] small copper coin, ‘farthing’. pēhišn [pwhsn'] corruption, decay. pēlāwad [pwPft! | М pwl'wd, N pēlād] steel. ~ën [-yn!] (made of) steel. pondik [pndk' | Ar. b/fundug] hazel-nut. por [pwl | N —] francolin. pēryētkēš [pwlyw(k)kyf = Av. paoiryē.tkaēša-| (one of) the first teachers of the Mazdean religion. ~ЛЬ : the primal doctrine of the Mazdean religion. pēst [pwst! | = M, N ~] skin, hide; bark, shell. mēn [-yn! | N ~in] (made of) skin. pēšīdan, pēš- [pws-yin' | N <] cover, put on, wear. ~išn: covering. potk [pwtk' | N ~] sledge-hammer. poxtan, paz- [APPWN-tn' < А V?ph; pwhtn', pc- | M pwxtn, N ~] cook, bake. рӧу- [pwd- | (P pwd-), N ~] run. ~iSnig : running. p6z(ag) [pwc(k!) | N pēz(a)] snout, muzzle. püdag [pwtk! | N pūda) foul, rotten. —ih: rottenness. 1puhl [pwhl | N pul] bridge. *puhl [pwhl] expiation, atonement; punishment. puhlénidan [ pwhlynytn'] cause to atone. purnāy [pwln’d] adult. purr (MALE < A mlh; pul | M pur, N ~} full. =-ģāh [-g’s] at the fullness of time, about to die. ~-тюаһ [-mh] full moon. —-rawišnih [-lwbsnyh] fullness. ~-sardag [-sltk'] of all kinds. --xwarrah [-G DE] full of glory. pursidan, purs- [pwrs-ytn' | M pwrs-ydn, N ~] ask. Vu re: Е ~iSn: question. — ~i$nig : responsible. pus [BRE < A br-h; pws | = M, N =] son. ~ar [BREI, pwsl | M pwsr, N ~] son. —yàn [pwsd?n! | M pwsy’n] womb. pušt [52001 | = M, N ~] back; support, protection.
559:rēšaģ [/yšk! | N rēša] root, fibre. rēšīdan, rēš- [lysyin' | N ~] wound, hurt. rëškën [/yškn'] hurtful, harmful. ~th: harmfulness. réxtan, réz- [lyhtn', lyc- | P ryxt, M ryz-, N ~] flow, pour. --išn: flow. ridan, riy- [/ytn', Id- | N ~] defecate, void. rist [lyst' | M ryst] dead. Iristag [lystk'] corpse. 'ristag [/ystk!] way, manner; sect. rist-āxēz [/yst?hyc | M ryst?hyz, N ~] resurrection of the dead, rištaģ [/(y)stk! | N ~a] rope, string, thread. riy-, v. ridan. riyahrih [/d?hlyh] scorn, mockery. rdb [/wp] robbery. rób- [/wp- | N ruftan, ~} rub, sweep. rūbāh [TALE < A tP; lwph | N ~] fox. Irēd [Iowt! | M rwd, N ~] river. *rdd [lwt' | N ~] stringed instrument. réd-bar [lwtb’] | N ~] river bank. rddig [/zvtyk! | (N róda)] intestine, gut; ~4n, (p/.) entrails, guts. тбүп [M(H)SY A < A ті; lwkn! | Р тшеп, (M rwyyn), N rauyan] oil, butter. ~-xwardig [-hwltyk'] sweetmeats. ron [lwn' | M rwn] direction. б... ~: towards. róspig [lwspyk! | N ~i] whore. ~th: whoredom. róstág [lw(t)st?k! | (P rwdyst?g), N rūstā] river-bed; district, province. rošn [lwfn! | M rwšn, N rūšan] light; bright, light. ~ih: light. röšnjag [lwsnk'] clear, obvious. ~gar [-Al | (P gr, M -ygr), N -gar] illuminator. irēy [ltd | M rwy, N ~] face. *rdy [lwd | M rwy, N ~] copper, brass. гбу-, -išn, v. rustan. гӧуап [/wdyn! | N ~] madder. róyen [/wdyn! | M r'wyn, N róyin] (made of) copper, brazen. roz [YWM < А ушт; Гос | M rwc[z, N ~) day. rózag [lwck! | M rweg, N roza] fast, fasting. rozāģ [wc k'] lightning. rózan [/wcn! | N ~] window. roz(b)ānaģ [lwe(p)’nk'] window. rózénidan, rózén- [Iwcyn-ytn! | M rweyn-] lighten, brighten. rozģār [/wck”l | N ~] daytime. r6zig [/wcyk! | N rózi] daily bread, sustenance.
663:xwāb [hw’b | N ~] sleep. xwābar [hw’l | M xwbr] beneficent. ~ig [-yk!] beneficial. —ih: beneficence, benefit. xwad [BNPSE < A b-nps-h; hwt' | M xwd, N ~] self; indeed. САҢ: selfhood, essence. xwaday [лору | M xwd'y, N ~] lord. ~th: lordship, sovereignty. ~war [-w’/] lordly. xwad-dósag [hwtdwsk'] self-indulgent. 7h : self-indulgence. xwah [AH TE < A *hth | N ~] sister. 1, ?x wüh-, ~išn, v. xwastan, xwāstan. xwahar [AH TEL v. xwah ; hw'hl | (M xwr), N xwdhar] sister. xwahl [eo hl | (M xwhr), № ~] bent, crooked. xwā(h)rīh [hw (h)yh | M xw'ryy] happiness, bliss. xwālist [hw’lyst' | (M xw’ryst)] sweetest. xwamn [hwmn', hmn' | M xwmn] sleep, dream. ~-wizar [-wc'/] interpreter of dreams, oneirocritic. xwān [hw!n! | M xw’n, N ~] tray, table. xwandan, xwān- [KRY TWN-, KLY TWN-tn! < А У д | M xwnd, xw'n-, N xwāndan) call, summon. Xwanirah [hwnyls = Av. x"aniraüa-] the central, inhabited continent of the earth. !xwar [kwl | M xwr, N ~] sun; cal. 11th day. Zwar [kwl = Av. x"ara-] a degree of sin. xwar-, —išn, v. xwardan. lxwàr [kw] | M xwr, N ~] light, easy; mean, abject. ~ih: ease; v. also x wührih. *xwar [%w/ | M xwr] food. xwür-, —išn, v. xwārīdan. xwaran [%w/n! | M xwrn] banquet. xwarāsān [hwlsn! | M xwr'?n, N ~] sunrise, east. xwār-bār [how?1b?l | M xwr w Pr, N ~] food and drink. xwardan, xwar- [OS TEN-tn! < Ath, V fth; hwltn! | M xwrdn, xwr-, N ~] eat, consume. ~išn: food. ~ignig : edible. ~išnīh: eating, consumption. xwardār [hwit?I] (legally) edible, not murdār. xwardig [hwityk' | M xwrdyg, N ~i] food. xwārēn [hw’lyn'] edible. xwārēn- [hw’lyn-] cause to eat, drink; feed; irrigate. xwarģ [wig | J xwwrg] ember. xwārīdan, xwār- [heo?1-ytnt] drink. —išn: drink, drinking.
664:xwarüfrün 96 yal
665:xwarūfrān [hwl(’)wpl’n' | M xwrwpr'n) sunset, west. xwarrah [GDE < A gdh | (M prh, N farr)] fortune, glory, splendour. ~6mand [-’wmnd] fortunate, glorious. xwarséd, v. xwarxséd. xwartar [hw ltl] minor (sins). xwarwarān [hwlwPn!, -bPn'] = xwardfran. xwar(x)8éd [Azl(h)syt' | M xwrxšyd, № xuršēd] sun. xwāstag [NKSY A < A nksy’; hw'stk! | M xw’stg, N ~a] property, wealth. i ~õmand [-wmnd] wealthy. xwastan, !xwāh- [(Y)PLHWN-tn! < А V plh; hwstn!, hw'd- | J xwh-, N xwast] tread, trample; thresh. ~išn: trampling. xwāstan, *xwāh- [BOYHWN-stn! < A МУ Бу; hw'stn!', hwd- | M xw’stn, xt h-, N ~] seek, want, desire; attract, acquire. --j&n : desire, attraction. xwastüg [hwstwk!' | N xustū] confessing, believing. ~ih: confession, belief, faith. xwaš [BS YM < А bsym; hw | M xw, N ~] pleasant, sweet, nice. ~ih: pleasantness, pleasure. xwēd [Awyt! | M xwyd, N ~] moist, fresh. ~ih: moisture, freshness. xwédódah [hwytw(k)ds, -d^t! = Av. x"aetwada0a-] kin-marriage. xwēn-āhan [Ahw(y)n ?syn! = Av. x"aéna- (ayah-)] shining metal. xwēš [NP ŠE < А npf-h; hwyš | M xwy(b)s, N ~] (one's) own. ~ih: possession. ~awand [kwyš*wnd | N ~] relative, kinsman. xwēšēnīdan, xwēšēn- [/nwyfyn-ytn!] appropriate, make one’s own. xwēš-kār [леу dutiful. ~th: proper function. xwēš-tan [NPSE tn! | N ~] self. xwéy [hwyd | N xway] sweat, perspiration. xwistan [hwystn'] sweat, perspire. xwurd [hwlt' | N ~] small, little. xwurdag [hwltk' | N ~a] something small, particle; astr. lunar mansion; (horse's) pastern. ~ih: smallness.
926:banguet sūr, xwaran.
1060:bowl padišxwar, tašt.
1364:consume xwardan.
1365:consumption xwarišnīh,
1502:death marg(īh), ēš, widerišn(īh), P murd; moment of — gyān kandan; deserving — margarzān; risk —, fight to ~ anēš xwardan.
1636:dish padišxwar.
1696:drink xwarišn; alcoholic — hur.
1697:drink (v.) xwaridan; cause to — xwārēn-. f
```


## [2026-09-05T20:41:07.395Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### NYB xwar\"\ngrep -n \"xvār\\|xvārīh\\|dušxvār\\|dušvār\\|duš-xvār\" NYB_vol2_glossary.txt | head -15\necho \"### BRT una / uyamna\"\ngrep -n \"uyamna\\|ermangelnd\\|Mangel\" BRT.txt | head -15"
}
```


### [2026-09-05T20:41:07.454Z] TOOL RESULT

```
### NYB xwar
1760:4. partitive: hac fradandan + han mart kasé anyone of the children of that man 25; hac šmāh xiönän ke hast ke ...? 25” ete.; fratom hac ax" i astomand 53%; xuastom hac z"arisnàn the most delicious of dishes 7413; ete. — 5. in comparison ‘than’: hac apārīk kanicakän āžarmīktar 422; Zarristan ke... zan-ē hac či hucihr- tar nest 259-19; hac tē veh 411; kū-š suk mas būt hac apdrik gāv 492°; more emphatically yuvattar (g. v.) hac hàn + huhömikän homtar 40°’. — 6. causative: hac hàn dušxvār sahist by this he was very much shocked 4?-?; hac hàn 1 devan sārēnišn 3774-25 : causal conj. : hac hàn cigon because 4511; hac han i with a nominal clause 48!. — 7. forming adverbs: hac pas, hac pes, hac be, hac apar (hacapar), hacadar; prepositions: pas hac, peš hac (= patiš hac 368), yuvat hac, bé hac; frame prepositions: hac. . . rād owing to 1525-26; hac .. . bérén 20%; hac . . . yuvatāk 76°. — Av. (1746 sqq.) hacé; OP haca; MPrth ^c, "Z; MPrs 'c, "z; Paz. ez (eži-ca); NP az.
4332:xvārēh [hw’lyh] bliss, felicity, delight. 4722, 141-16, 10020.21, — From lavār; MPrs zw’ryy (A-H N).
4342:x"är-män [hw?lm?n'] whose house is dirty, contemptible 4522. — From ?axvār + màn (q. v.).
4922:Patišhuvari-: Patišxvār- gar
### BRT una / uyamna
4515:•  j.  an-uyainna-  Adj.  'nicht  mangelhaft, vollkommen' :  uyamna  (sd.)  °nais  daste  Vr. J5.1.
5815:•  j.  a-st9n»ta-  Adj.  'nicht  niederzuwerfen': 'taca  amuyamna  yazamaide  Vr.  7.  i.
8461:•  j.  uyamna-  Adj,,  PPM.:  s.  ^va-. KompE.
10627:•  j.  xraO'Wamna-  Adj.  'einsichtig,  weise': var?Ö3mnah£  'nahe  suyamnahe  V.^,  2  Gl.
12079:Bildung  wie  iari.zaairä.;  vgl,  /iaeli./ara-.  — ai.  vgl.  iar6ddzi}as-  Adj.  —  ")  Nach  der fl-Dekl, t^d  (wieder)  verschafft,  heimlichWasserj.j,  tarö.piS-wa- i)  Adj. 'der  ungenügende aad  Kraut"  V.  75. 10;  9',  s)  Praen.  mit  |  Nahrung  hat,  bekommt,  Mangel  anNahrung Akt;  a)  'durch  -  hin,  über  -  hin,  über  l^xditV:  yff  spätum^'^wim^dasH yim  pasus.- -  hinw^,  hinaus';  o)  räumlich:  husi^m  \  ^aurum  "wenn  einer  den  Hund  ,/*.  an f^sm  ra^aya  TS  . .  vilanuhaitm  Yt  5,  [  Nahrungsmangel  leiden  lässlf'  V.  13.  20, '•r,  ?8;  —  hrTs'^J  'rff  pir>tamcit  h!  urva- 1  24;  20.  2)  n.  'ungenügende  Nahrung, »■  ..frqparaymi  Y./5.6;  7J.  i6,  Vyt.|  Nahrungsmangel' (?):  paiH  'w>m  daidyat •fc>  Nik.2;  —  mtknm  .  .  yS  paeiryö  'r3\yai:a  . .  Vytß  (?);  —  *Vf^  N.  13  (?)". **■«   asnaffUi     Yt  10.  13;  V.ltj.jo;   — |      I'ü,  (lu  Vyt.h  lar  i'ariin,(ra'S.):  *tar  fihn'\
13033:\yatqm  ("So  vohu  väsitya  (sd.)  uyamna  (sd.) anuyamnäii  'le  Vr.  i^.  i  *'.
13765:•  j.  'duS.dätay- ''  f  'schlechte  Einsicht, Mangel  an  Einsicht':  'iayä»  (GS.  als  AblS.) fraista  dmantS  "wegen  Mangels  an  Ein- sicht sind  die  meisten  glaubensfeiadlich" Aog.  sOm.
18130:asaone  V.  2J.  i.  a)  bes.  mit  Beziehung a.\^gai%ä-  gebraucht'':  aAam  (Sp,  107  m.) dadäl  ahurö  ahmäi  gatisi  vohB  frädat manavha  ^.46- 13;  —  damam  . .  yä  mit gat^i  asa  fradöit  ha^mnä  (sA.)  Y. 44.10; —  vaM  manaivha yehyä  syao%anilis gaU'^S aia  frädfntl  (als  Pass.)  "mit  VAf.,  durch des  Tätigkeit  Haus  und  Hof  von  Asa  ge- fördert werden"  Y.4J.6;  —  Jat  ml ga^^t'r /rO^aya . .  var^aya  V.  2. 4 ; — az»m  tl  gaf^a Jrälayfni ..  vari^ayeai  V.  2.  5.  2)  Med. 'wachsen,  gedeihen':  haoma  raose  gara paiti  Uta  /rä^aS^a  vifpaiia  Y. /o.  4;  — neben  vartd-'.frainmnahe^  vanifmna/ie xrahwsmtiahe  suyamnaAe  V.4-2  Gl.
22675:Zum    V.    ivoB'.    —    Vgl.  ^vanta-.    —    ^.■.  .pasüttt    *ava^^.vTnaoi/i  pasca    hü  frasms.- /w»,  m^tk?  dssi  i  i^ä™^»)  «  */  dilti  zfa-  ^^,-„^  asaocantat  paiti  a^irai  N.  5S. A/>ut/<,n    bivii  -   aiäv  gSn  -  vihapi  bavil.        mit >a 'schlachten  ,  alsOpfer:  ^«Mw^M Mangelhaft   übeiliefert.    —    ')  S  368.  35.    ~\anumayanqm  frävinuysl  V.  m,  70. '^  Vgl,  Bd,  sr.  4,  iLSTi  NB.  385.  —  3)  S,  dazu        D  Et.?     Vgl,  S  317.   —    PS,  (in  V,):   Ixlla», Bthl.  LG&kPb.  lyOi.  61.  (lu  N.):  fehlt.  —  ')  Hds,  aväi.
23431:i)  PPM.  'nicht  ausreichend,  ungenügend, mangelhaft' :'V^r^i7/ami;'ii  ita  vohti  västrya (sd.)  uyamna  anuyamnäii  daste  ". .  damit was  mangelhaft  ist,  vollkommen  gemacht werde"  Vr.  15.  i'\  2)  PPfP.;  a)  'unge- nügend': ä/riii  yä  ünsm  pintam  ksr»- naoiti  p^nrumat  viyiarayäti  (sd.)  ". .  die was  ungenügend  (gefUllt)  ist,  voU  macht, . ." V.25.5.  b> 'geringfügig,  kärglich':  umm F.g,  a)  n.  als  Subst:  avaaAsnzämi yanyJis  ünqm  (APn.)  . .  yä  *mainyeü  da- vayeinti  (sd.)  "ich  lehne  ab  die  Kärglich- keiten  (kärglichen  Darbringungen)  des Wribes  . .,  das  . ."  Y.  10. 15.
24812:*>  Im  Gegensatz  lu  ar^jiis;  j'am-  uaä/taiä- iaaiaA-  ina%a-;  vgt.  batAö.i/arila-.  In  den  drei votliegenden  Fällen  handelt  es  sich  um  Mangel an  anilicher  Umsichl  (V./)  ond  um  PflicbtTer- Säumnis  (V.  TS.  N.  9).
25241:•  ].,  g.  raziita-  Adj.  (fem.  *ta-)  'der  ge- radeste, richtigste,  rechtlichste,  gerechteste': *ya%a  *äis  lä  J  vansaitl  yä  data  ataJau! paouruyehyä  ratüi  iyaohana  °tä  (APn.) dngvata^ä  hya^cä  *aiäomye^aca . .  "wie es  den  Gesetzen  fiir  das  erste  Leben  ge- mäss ist,  so  wird  er  (näml.  Zara^u/tra) als  Richter  in  gerechtestem  Tun  gegen den  27rt(fgenossen  verfahren  und  gegen den,  bei  dem . ."  Y.j;^.  i''.  a)  von^an- tay-  (usw.) :  °öw  pantqm  daoaiti  ätars  . . ySi  ftißirym  lUfil  aiwidruzinÜ  "den  ge- radesten Pfad  gibt  (weist)  A.  .  .  denen, die  . ."  Yt  /o.  3;  —  mit  3  und  Abi.  oder Akk.  'hin  —  zu':  'tah^  pa%S .  .yS  asti  't3 j  aiäi  vahist)m!a  oASrn  asaonqm  "des geradesten  Pfeds  . .,  der  der  geradeste  ist hin  zu  Asa  und  zum  besten  Leben  der Gerechten"  Y.  6Ä  13.  a)  ahatpantay- (usw.),  das  aber  hinzuzudenken  ist:  yö dai^hsus  rqxlyqi^yh para  •/Jfnäml^a^i) baraiti  Yt.  io,  37*';  —  äid3?ar?nä  nastö •ta  (näml.  /a^a)  ". .  der  vom  geradesten Weg  abgegangen  ist"  Yt.  10. 105^';  — amuyamna  (sd.)  'tanqm  (näml.  pa^qm) Vi.17.1j;  13.3s-  b)  von  rainav-  m. (Stverz):  rar'hus 'tH  V.  13.  g  PUZ.jusw.;  — 'tfm,  'tat,  •iahe,  'ta  (VS.).  A)  mit  asts-  f. (Stverz.)  Name  einer  Gottheit:  °ta  ästa \'t.i6.7  usw.;   —  'tqm,  'taya,  'te  (VSf.).
26011:'nützen,  Nutzen  schaffen',  mit  Akk.  des wem?:  ya%a  väts  .  .  vTsptm  ahüm  .,/rä- la/icä  var3%atUa  saosyanti{ila.Xl  Sing.)& A.  4.  6;  —  ys  daitihave  hu.vaxsai  frdh>m- nake  vanltimnahe  .  .  suyamnahe  N.4-  2 Gl.  a)  insbes.  'den  Nutzen,  den  Vor- teil schaffen,  erwirken',  d.  i.  das  gute  Loos im  andern  Leben'';  wua^a  sao^qs  (sd.) ya%a  vispftn  akum  astvanhm  sävayät  Yt, y"9i  —  Aarp'hrai  asahe  gaihanqm suyaiitnanqmla  saosyantqmca  "um  zu wachen  . .  über  die,  die  den  Nutzen  be- kommen und  die  ihn  schaffen  werden" Y.55. 3;  — y^a  vS  saofyatttS  dahyunqm suyamna  väcim  ^barmti  Y,  yo.  4;  — sttoSyant-  s.  auch  bes. np.  tgl.  iSd  'Nutien'').  —  PQ.  (lu  Y,  55): sütan  u  nilömattdan,  (m  Y./O);  sütömand,  (lu V.  4);  süßiüt  (3.Sg.;^  erl.:  kui  tut  palas  kuneU
26395:•  j.  suyamna-  Adj,,  PPM.:  s,  sav-.
29127:•  j.  hajlasrö.pä(y)-  Adj,  'vor  dem  Zu- endegehen  (Mangel?)  schützend':  °pqm (APn.)  matdäi  (als  Gen.)  uxham  V.24.
```


## [2026-09-05T20:41:25.940Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\npython3 - <<'EOF'\nimport re\nt=open('WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\nfor i,p in enumerate(pages[:6]):\n    print(i, p[:150].replace('\\n',' '))\nEOF\ngrep -n \"pdf page\" WLD_Bd1_pages.txt | head -3"
}
```


### [2026-09-05T20:41:27.572Z] TOOL RESULT

```
leaves 895
0             GOVERNMENT OF INDIA  ARCHEOLOGICAL SURVEY OF INDIA                 CENTRAL             ARCHEOLOGICAL                 LIBRARY ACCESSION NO.
1 
2 
3                       ALOIS WALDE   VERGLEICHENDES WftRTERBDCH                                 DER        INDOGERM ANISCHEN SPRACHEN                  
4 CENTRAL A,.            ,   JRIGAL    LIBRARY, NlvV .,w.rU. Am. N# .^.557- D**.,      .                4-.   SS' cwi                         /V* »#tf M
5                                                            •                      n                                            Vorrede.   Das   vorlie
```


## [2026-09-05T20:41:32.660Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\npython3 - <<'EOF'\nimport re\nt=open('WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\n# find leaf containing eter- entry: search for 'aedre' or 'inathar' or 'ntop'\nfor i,p in enumerate(pages):\n    if re.search(r'inathar|inuodili|ut-innathrian|innethron', p):\n        print('leaf',i, re.findall(r'\\b[12]?\\d{2}\\b', p[:200])[:6])\n        j=re.search(r'inathar|inuodili|innethron',p).start()\n        print(p[max(0,j-1800):j+600].replace('\\n',' '))\n        print('-----')\nEOF"
}
```


### [2026-09-05T20:41:35.044Z] TOOL RESULT

```
leaf 125 ['117']
sen idg. Form, sondern durch jiingere Vereinfachung von -Test- zu -Tct- erklaren.   et(e)n- „Kern, Korn“.   Gr. ervog „Brei von Hiilsenfriichten'                                                   eitne „Kern“, schott. bite „un-                                                                      1                                                                           ,                                                                              mil -                                                                                      ,     husked ear of corn'            1                                    ,                                        eitean „Kern, Korn“.                              Zupitza KZ. 36, 243, Pedersen KG. 1160.  eter- „Eingeweide“.   Gr. ?)xoq „Herz“ (nur Nom.-Acc., nach J. Schmidt PI. 177 aol. Form                                                              fiir  *etr, *grag),           gxQov „Bauch, TJnterleib‘                                                                  :                                                                       ;                                                                              anord. cedr            f.   „Ader“ teeter-, durch MiBdeutung des -r als Kominativ -*e in die i-Dekl. iibergefiihrt, Dat. Acc. cedi, PI. eedir, cedar), ags. cedre f., ahd. ud(a)ra, mhd. Cider, adre „Ader,  Sehne; pi. Eingeweide“, mit inn(a) „innen“, zusammengesetzt ahd. inn- udiri „intestina,           viscera                                          11                                               ,                                                   anfrank. inn-cthron                       gl. Lips.,      as.       ut-innathnan „ausweiden“, daneben eine altere Zs. mit in „iv“ und nachtonigem *0 in ahd. (mit Suffixtausch) inuodili „Eingeweide“   daB ebenso air. tnathar                    ;   „Eingeweide“, corn, cn-ederen „extum“ aus % en-otro herleitbar sei, ist aber kaum fraglich: zwar macht B. bei Fickll 4 29 fiir die Hebung von e- zu air. i- das aus 0 entwickelte    geltend, und n aus idg. 0 ist eine auf den Auslaut beschriinkte Entwicklung, aber (Pedersen KG. II 44) eine Gdf. *eni-tro-, Ableitung von *eni = gr. ire mit Komparativsuffix -tro- ergabe *inethar\ es wird also *enathar (aus *en-otro-) durch Einflufi der Praepos. i n-   sein    i       erhalten haben (Pokorny brieflich).    Vgl. J. Schmidt PI. 198
-----
```


## [2026-09-05T20:41:42.672Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\npython3 - <<'EOF'\nt=open('WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (271,272,273):\n    print('=== leaf',i,'===')\n    print(pages[i][:1200].replace('\\n',' '))\nEOF"
}
```


### [2026-09-05T20:41:44.477Z] TOOL RESULT

```
=== leaf 271 ===
        i                                                                                   ,                                                              ner-                                                263     Ebenso, obwohl die Bed. „hervorsprudeln K aus ausspeien" entwickelt     ,    sein konnte (s. Fick III 4 392, Falk-Torp u. vimmd       Holtkausen IF. 32,    ,   337), die doch wohl auf einlieitliche. aut einem *iie>n- „durcheinander wimmeln" beruhende und vielleicht mit got. iumjo „Menge“ unter renew-                                                                                                          '     (v. Grienberger Unters. 134) zu vereinigende Sippe von as. wemmian „her-  vorsprudeln“, ahd. wimi pi. „hervorsprudelnde Quellen ', wemon „wogeti“,                                                                                     1     wiumen „hervorsprudeln“ wohl Yerquickung von wim- und imn-, Brugmann IF. 13, 155), witnidon ichntzzen immezzeu wimmeln. sich lebhat’t bewegen”,                               ,                  ,               .   spatmhd. find.) wimmtn whnelen, nhd. bair. wunimeln ds., norw. mdartl.                                    ,  vama, vamla, 
=== leaf 272 ===
264                                                                                      uer-   als  „den Sperrbalken hinauf- oder wegheben, den TorverschluB (z. T. ur-                                                                                                                                       11 spriinglicb   auch ein Strick?) vorspannen oder losen eine alte Sonderan- wendung unaeres *iier- sei, ist kaum anzunehmen.    Dazu vielleiebt ai. a-va.ll a-vali-h f. „Reihe, Schnur (z. B. Perlenschnur)“                                                                     ,  (Zupitza aaO.) und vermutlich (s. Solmsen Unters. 289 ff.) die Sippe von                                                                                                                                                 11 gr. aetQoj mit den Bed. ,,verkoppeln, verkniipfen, anhangen         und „in die Hohe heben (in letzterer freilich von Solmsen als verschiedene Gruppe                                 11    abgetrennt: doch ist „aufhangen, zum Hangen in die Hohe heben, an                                                                         11 einem Strick hinaufhangen als Mittelbegriff annehmbar, vgl z. B. av-ego
=== leaf 273 ===
                                                                                                           )                                                                                                 uer-                                                        265                                                                                                                           11       Kom. aogxyg       Koppel, an der das Schwert hangt                                                  „die           dogxijgtg „die                                                ,   Ringe oder Haken, mittels deren die Scheide an der Koppel befestigt ist“ („Anhanger“; wegen des bei ter-Stammen sonst unerhorten o-Yokalismus mit aol. og = gemeingr. ao), wohl auch dog „Schwert“ (ursprgl. „Schwert-                        11 gehenk ? vielleicht unter Aufsaugung eines mit lat. crisis, ai. asi-h sich deckenden Wortes) und aogxi) „lederner Sack, in den Kleidungsstiicke ge-                                                                           111 steckt werden, Felleisen (etwa „Sack zum Lberhangen oder Umhangen                                                                11
```


## [2026-09-05T20:41:59.934Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\nfor i in (686,687,688,689,690):\n    print('=== leaf',i,'===')\n    print(pages[i][:500].replace('\\n',' '))\nEOF"
}
```


### [2026-09-05T20:42:01.636Z] TOOL RESULT

```
leaves 858
=== leaf 686 ===
so = “bench, quarter-deck"); Lat. solum, n. ‘soil, ground, bottom, sole of foot; solium, n. “seat, throne: solea, f. ‘sole of foot’; cf. also solidus, adj. (/solid, full, entire’. Not as WH); OHG sala, f.; OE sæl, pl. salu, n. ‘hall’; sele, m. id. (and 'dwelling); ON salr, npl. salir, m. “room, floor, ball" beside sel, pl. -ja, n. ‘hut’; OS seli, Let. m. “room, house” beside selida, f. ‘dwelling’; Go. salipwa, f. id. (Lë *hostelry^); OE sælp, f. ‘dwelling’; (the source of OCS selitva *hostelry' 
=== leaf 687 ===
ras, -dara: -eimi in Skt. & (variant) Latv. cf. sa-eju; sa-eima, f.; -dhos, -dha in Skt. Slav & Balt. somolos “together, equal, even, like'. Cf. som- (1), sem- & sm- Skt. samaráh, m. ‘concourse, battle’; Per. hamal, adj. “equal, like’; Arm. amol, s. *coun- 1245 terpart, fellow; amolk, gp: amloc, pl. type *pair, yoke? (fr. *somilo-); Gk. homalós, adj. “level, even’; Umb. cf. sumel, adv. ‘at the same time? som-. Cpds. ctd. -guer-, -guor- ‘drinking or eating together? in Skt. Arm. (anker) & Latv.; 
=== leaf 688 ===
n Skt., OCS & Li.; -urtt-, -urst- in Skt. & Srb. (song-, see seng-) songh- ‘reaping, crop’; songhio, songheio ‘reap’. See sengh-, & cf. segh- Arm. hundzk, s. id.; hndzem, v. id. MHG sange, wf. ‘sheaf. Cf. (in sense of “bind, con- strict’? probably) Per. hanjam, v. “torture, af- flict; OE sengen, id. songuhos (prob. *som-$uhos, see $uhon-, 1247 £uhuo) “noise, sound, voice’. WP, II, 496 Skt. cf. sam-hvaye, mp. “call out, shout to- gether’; Tokh. cf. sunk ‘throat’ (?); Gk. omphé, f. voice: Go. sagg
=== leaf 689 ===
��; OCS sokü, R. Srb. sok, m. “juice, sap’; Li. sakai, m. pl. ‘pitch, gum, resin’; OPr. sackis, id. soquos, is, à (2) ‘utterance, declaration; ut- terer, denouncer'. WP II, 479. Cf. sequ- (2) and sequ- (2) Gk. ons gs: -idos, f. ‘vengeance’; Br. hop, pl. u, m. ‘cal’; OCS sokü, m. ‘accuser, plain- tiff; Srb. sók, m. 'denouncer'; Li. sakà, f. legend, tale’; cf. uZz-sakai, pl. “marriage banns'; (oxytonic prototype in) MHG sage, sf. ‘speech, rumour’; ON saga, f. ‘tale, saga"; E saw “tale” soquos, à (
=== leaf 690 ===
�there’; Gk. hó, hé, def. art. beside hos, hé, rel. pron.; OLat. sum ‘him’, sam ‘her’; SOS, sàs, pl. ‘them’; (Sard. su, sa, def. art. prob. fr. ipse); MIr. so ‘this; these’; cf. Ir. so-nn (‘here’, cf. Arm. ho-n ‘there’); Go. sa, sð, mf. ‘thi; ON sá, sú “that; the’. Extn. in Gk. hoíos, hoia, pn. ((such?. Ambig. cf. ios-); Av. hoyo *this'; Alb. ay, f: ajó “he, she’ sós- ‘flaccid, limp, tired; tire’. (also: *pen- dant" ?) Du. soes, m. ‘drowsiness’; soezen, v. *drowse'; Li. suosiu, suósti, v. tr. ‘t
```


## [2026-09-05T20:42:12.194Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('=== leaf 738 ===')\nprint(pages[738][:900].replace('\\n',' '))\nprint()\nfor i,p in enumerate(pages):\n    for m in re.finditer(r'\\bēter|\\beter-|ētr̥|\\bētri', p):\n        print('leaf',i,'|',p[max(0,m.start()-150):m.start()+400].replace('\\n',' '))\n        print('--')\n        break\nEOF"
}
```


### [2026-09-05T20:42:14.306Z] TOOL RESULT

```
=== leaf 738 ===
��advice’; Ir. cf. sás- uighim, v. ‘satisfy’; sásta, pp. ((content: Pahl. xvast-); OE sw&s, adj. (2) sweet (suadh-, see suodh- 'knife") suag- (1) “evil”. Gk. ambig. Probably identi- cal with suaĝ-, q.v. Gk. ágos, eos, n. “crime, pollution; MHG swach, sm. ‘disgrace’; adj. “bad, base; weak’; Icel. svaka-, cpds. *coarse-, vulgar- suag- (2) (?) Gk. ágo, v. (4) ‘weigh’; Boeot. wagánon, n. *cheese-press' suágh- (suaghó; suàghos, à) ‘resound; rustle, resonance, echo’. WP I, 215 Gk. ékhéo, Dor. akhéo, v. ‘resound’; ekhé, Dor. åkhá, f. “sound, roar’; W cf. chwa, pl. -on, -oedd, f. ‘blast’; chwawio, inf. ‘puff, blast beside chweio, inf. ‘bustle’; Go. ga-swogjan, v. ‘sigh’; OS swogan, sv. 7. ‘rustle, sough'; OE swogan, sv. 7. & swégan (uml.), wv. “rush, roar, rumble’; E to sough; Fris. swoegje, Du. zwoegen, v. “pant, puff; LG swogen, v. ‘whine, ramble in speech’; be-swógen, v. (uml. *swoon'; cf. al

leaf 260 | b. herë ‘time, fois’; Lat. cf. h-ornus (“of this season or year”, fr. *ho-ior-, cf. ho-die); W cf. ior *eter- nal: ON cf. ent ‘younger’; also (?) oeska (Cchildhood', if. for *ioriska); Srb. jàr ‘heat’; OCz. j&t “spring; spring corn’; Cz. jaro ‘spring’; Blg. jarà ‘reflected glow’; Slovak jar, f. ‘spring’: Slovene jar ‘precocious’; Ukr. jaryj, adj. ‘springtime’; R jarovój summer": jàrka “year- ling ewe iðr- (2) “fresh, clean, clear, pure’. Cf. WP I, 3, 208, 775 and next iomolos — iosmn- (iosmà, iosmo-
--
```


## [2026-09-05T20:42:28.974Z] TOOL CALL #57: Bash

```json
{
 "command": "ls site/pages/162.jpg 2>/dev/null; pdftoppm -f 162 -l 162 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg162 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-05T20:42:31.263Z] TOOL RESULT

```
site/pages/162.jpg
total 17308
drwx------ 2 sfmqrb sfmqrb    4096 Sep  5 16:42 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  5 16:02 ..
-rw-rw-r-- 1 sfmqrb sfmqrb  752374 Sep  5 16:12 bqt362_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  624515 Sep  5 16:12 bqt362.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 1032029 Sep  5 16:13 bqt362_mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb  385716 Sep  5 16:13 bqt363_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  338175 Sep  5 16:13 bqt363_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb  692415 Sep  5 16:13 bqt363.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  956665 Sep  5 16:11 bqt553_foot2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  746413 Sep  5 16:11 bqt553_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  512022 Sep  5 16:10 bqt553.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  154316 Sep  5 16:07 bqt_bot389.png
-rw-rw-r-- 1 sfmqrb sfmqrb  168738 Sep  5 16:07 bqt_bot390.png
-rw-rw-r-- 1 sfmqrb sfmqrb  520653 Sep  5 16:07 bqt_n389.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  527392 Sep  5 16:07 bqt_n390.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   67648 Sep  5 16:29 build128.py
-rw-rw-r-- 1 sfmqrb sfmqrb  105345 Sep  5 16:30 build132.py
-rw-rw-r-- 1 sfmqrb sfmqrb   62948 Sep  5 16:36 build134.py
-rw-rw-r-- 1 sfmqrb sfmqrb   56126 Sep  5 16:29 build136b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   13830 Sep  5 16:22 build136.py
-rw-rw-r-- 1 sfmqrb sfmqrb   66341 Sep  5 16:28 build139.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53260 Sep  5 16:29 build142.py
-rw-rw-r-- 1 sfmqrb sfmqrb   76989 Sep  5 16:32 build145.py
-rw-rw-r-- 1 sfmqrb sfmqrb   50861 Sep  5 16:34 build148b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   21485 Sep  5 16:29 build148.py
-rw-rw-r-- 1 sfmqrb sfmqrb    7816 Sep  5 16:35 c_am2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   14765 Sep  5 16:35 c_am3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   10038 Sep  5 16:35 c_empty2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4123 Sep  5 16:34 crop_am.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4986 Sep  5 16:34 crop_arabic_refs.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7702 Sep  5 16:34 crop_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb   16978 Sep  5 16:34 crop_morocco.png
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep  5 16:18 kent.txt
-rw-rw-r-- 1 sfmqrb sfmqrb     222 Sep  5 16:30 leaf.py
-rw-rw-r-- 1 sfmqrb sfmqrb   57617 Sep  5 16:20 mk129.py
-rw-rw-r-- 1 sfmqrb sfmqrb   74680 Sep  5 16:26 mk131.py
-rw-rw-r-- 1 sfmqrb sfmqrb   33365 Sep  5 16:25 mk133.py
-rw-rw-r-- 1 sfmqrb sfmqrb   42635 Sep  5 16:29 mk140.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51288 Sep  5 16:30 mk143.py
-rw-rw-r-- 1 sfmqrb sfmqrb   11831 Sep  5 16:32 node4.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7427 Sep  5 16:32 node7.png
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep  5 16:13 oldpers_djvu.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    6054 Sep  5 16:36 p152_e0left.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2672 Sep  5 16:36 p152_node2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   22067 Sep  5 16:29 part0.json
-rw-rw-r-- 1 sfmqrb sfmqrb   14156 Sep  5 16:22 part1.json
-rw-rw-r-- 1 sfmqrb sfmqrb   53212 Sep  5 16:08 pg130_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74748 Sep  5 16:08 pg130.png
-rw-rw-r-- 1 sfmqrb sfmqrb  107108 Sep  5 16:08 pg130_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80793 Sep  5 16:15 pg131.png
-rw-rw-r-- 1 sfmqrb sfmqrb   46793 Sep  5 16:20 pg133.png
-rw-rw-r-- 1 sfmqrb sfmqrb   87739 Sep  5 16:10 pg134.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66991 Sep  5 16:16 pg135.png
-rw-rw-r-- 1 sfmqrb sfmqrb   68320 Sep  5 16:08 pg136_300.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63248 Sep  5 16:08 pg136.png
-rw-rw-r-- 1 sfmqrb sfmqrb   45014 Sep  5 16:12 pg137.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74330 Sep  5 16:11 pg138.png
-rw-rw-r-- 1 sfmqrb sfmqrb   70436 Sep  5 16:10 pg140.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63658 Sep  5 16:13 pg144.png
-rw-rw-r-- 1 sfmqrb sfmqrb   89133 Sep  5 16:09 pg145.png
-rw-rw-r-- 1 sfmqrb sfmqrb   60631 Sep  5 16:11 pg147.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81770 Sep  5 16:20 pg148.png
-rw-rw-r-- 1 sfmqrb sfmqrb   72186 Sep  5 16:30 pg149.png
-rw-rw-r-- 1 sfmqrb sfmqrb  131595 Sep  5 16:32 pg151_hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   96854 Sep  5 16:29 pg151.png
-rw-rw-r-- 1 sfmqrb sfmqrb  154426 Sep  5 16:36 pg152_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   62516 Sep  5 16:35 pg152.png
-rw-rw-r-- 1 sfmqrb sfmqrb   39131 Sep  5 16:28 pg153.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63033 Sep  5 16:30 pg154.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77057 Sep  5 16:32 pg155.png
-rw-rw-r-- 1 sfmqrb sfmqrb  169880 Sep  5 16:34 pg158_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80624 Sep  5 16:34 pg158.png
-rw-rw-r-- 1 sfmqrb sfmqrb  124379 Sep  5 16:31 pg159_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   27814 Sep  5 16:31 pg159.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4694 Sep  5 16:31 pg159_word.png
-rw-rw-r-- 1 sfmqrb sfmqrb  168057 Sep  5 16:34 pg161_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   76745 Sep  5 16:34 pg161.png
-rw-rw-r-- 1 sfmqrb sfmqrb   76438 Sep  5 16:42 pg162.png
-rw-rw-r-- 1 sfmqrb sfmqrb   25911 Sep  5 16:32 pg163.png
-rw-rw-r-- 1 sfmqrb sfmqrb   59398 Sep  5 16:33 pg164.png
-rw-rw-r-- 1 sfmqrb sfmqrb   61265 Sep  5 16:40 pg165.png
-rw-rw-r-- 1 sfmqrb sfmqrb   86005 Sep  5 16:39 pg168.png
-rw-rw-r-- 1 sfmqrb sfmqrb   68420 Sep  5 16:42 pg169.png
-rw-rw-r-- 1 sfmqrb sfmqrb   44812 Sep  5 16:34 pg532.png
-rw-rw-r-- 1 sfmqrb sfmqrb  153161 Sep  5 16:34 pg532_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4868 Sep  5 16:14 prt.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  333088 Sep  5 16:16 sod135_c.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1817364 Sep  5 16:16 sod135.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  101641 Sep  5 16:15 sod136_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1892712 Sep  5 16:15 sod136.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   56398 Sep  5 16:26 write144.py
```


## [2026-09-05T20:42:34.713Z] TOOL CALL #58: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg162.png"
}
```


### [2026-09-05T20:42:35.093Z] TOOL RESULT

```

```


## [2026-09-05T20:42:35.077Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T20:42:50.453Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad\npdftoppm -f 162 -l 162 -r 400 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg162_400\npython3 -c \"\nfrom PIL import Image\nim=Image.open('pg162_400.png'); print(im.size)\nw,h=im.size\nim.crop((int(0.44*w),int(0.60*h),int(0.80*w),int(0.665*h))).save('pg162_verse.png')\n\"\nls -la pg162_verse.png"
}
```


### [2026-09-05T20:42:54.175Z] TOOL RESULT

```
(3400, 4400)
-rw-rw-r-- 1 sfmqrb sfmqrb 8523 Sep  5 16:42 pg162_verse.png
```


## [2026-09-05T20:42:56.617Z] TOOL CALL #60: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg162_verse.png"
}
```


### [2026-09-05T20:42:56.694Z] TOOL RESULT

```

```


## [2026-09-05T20:43:07.958Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### LAT (Ernout-Meillet) et\"\npython3 - <<'EOF'\nimport re\nfor f in ('LAT.txt','LEW_1910.txt'):\n    t=open(f,encoding='utf-8',errors='replace').read()\n    print('######',f, len(t))\n    for pat in [r'\\net,? *(conj|adv)', r'\\nuanus', r'\\nvanus', r'\\nuastus', r'\\nvastus', r'uaco', r'\\nvaco']:\n        m=re.search(pat,t)\n        if m: print(pat,'->', t[m.start():m.start()+450].replace('\\n',' '))\n        else: print(pat,'-> none')\nEOF"
}
```


### [2026-09-05T20:43:09.658Z] TOOL RESULT

```
### LAT (Ernout-Meillet) et
###### LAT.txt 4601625
\net,? *(conj|adv) ->  et adv. "matin, de bon matin"; dans cette acception a un doublet ar- chalque mani, locatif. Renforce a basse ^poque par de: demane (Vulg.), M.l.5394 et 3548, cf. aussi *maneana, M.1.5395. Panroman. Celt.: iri. main. Mane est le neutre de 1 1 adj. manis, doublet de mdnus "bon" (v. ces mota) qui, applique k 1'expression du temps, s'est specialise dans le meme sens que fr. "de bonne heure", all. bei guter Zeit: Varr., L.l.6,4, diei principium mane.
\nuanus ->  uanus, -a, -um: vide, d<?garni, leue ac uanum granum, Coi.3,y, 13: uanior lam erat hostium acies, T.L.3,47,4; Par suite "creux, sa^ substance, vam (frequent et class., attest<? depuis Enn.; se dit des personnes et des choses: uanum cSnsilium-, udna Oratis et udnl haruspices ; de la "vaniteux". Panroman, sauf roumain. M.L.yi 45 . Iri, fanas "uacuum"? Derives :juanitas (conservi sous des formes savantes en roman, M.L. yi 3 y;; uamtudo, uanities, t
\nvanus -> none
\nuastus ->  uastus et convador', ou "fournir eantion ", par extension "assigner"; vadatus: li£ par eant ion; uadimdnium', Suador (Gloss»),,ett<kli*5nitt*; svbuas (an pl. subvades dans Aulu-Gelle iG,iO,0). Cf. anssi praes, praedium. Les fomes ronanes renontent an gem. (got. wadi), M.L.9474, on dn noins en ont subi l*influence (conae dans le cas de vadum, etc.). Terne technique, qui se retrouve, 4 l' 4 tat de ddrivd, en gemanique: got.wadi "appapwv", etc. uEs
\nvastus -> none
uaco -> uaco (Geli.). A cot 4 de uacS, uactuus, uacStig, sont attest 4 s des doublets arcbaiques uocg, uoctuus, uocatiS. Piante jone sar uocTS "etre vide" et uocg "appeler", Cas.537: fac habeant linguam tuae aedes. - quid ita ? - quom ueniam uocent. - Yoctuus est entre autres dans Tri.n; uocdtio dans CIL I 198,77 (Lex Repet.). Les formes en uoc- ont dispara de la 1 . ecrite, mais ont continu 4 de vivre dans la 1 . parl 4 e; c*est A *vocitus que reaontent
\nvaco -> none
###### LEW_1910.txt 619063
\net,? *(conj|adv) -> none
\nuanus -> none
\nvanus -> none
\nuastus -> none
\nvastus -> none
uaco -> uacose II 723 andirsafust I 36 anferener I 36 angla- I 227 anglar I 43, 142 anglome I 48, 687 anhostatu I 686 anpenes II 280 anseriato I 36, 43 anstintu I 43, 707 anstiplatu I 43 antakres I 686, 708 antentu I 438, 687, 708, II 663 anter, anter- I 43, 687, 708 antermenzaru If 71 antervakaze II 723 anositatu I 636 anovihimu I 4365, 687 ap, ape, api I 76, II 401, 402 apehtre I 1, 433 apretu I 36, 406 apruf, aprof I 56 arclataf I 64 armamu I 12 arnip
\nvaco -> none
```


## [2026-09-05T20:43:15.956Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('LAT.txt',encoding='utf-8',errors='replace').read()\nfor pat in [r'uanus, -a, -um', r'uastus, -a, -um', r'uacQ|uaco, -as|uacS,']:\n    for m in re.finditer(pat,t):\n        print('###',pat)\n        print(t[m.start():m.start()+1600].replace('\\n',' '))\n        print()\n        break\nm=re.search(r'\\bet\\b, *conj|et: conj|\\net\\. conj',t)\nprint(m)\nEOF"
}
```


### [2026-09-05T20:43:17.956Z] TOOL RESULT

```
### uanus, -a, -um
uanus, -a, -um: vide, d<?garni, leue ac uanum granum, Coi.3,y, 13: uanior lam erat hostium acies, T.L.3,47,4; Par suite "creux, sa^ substance, vam (frequent et class., attest<? depuis Enn.; se dit des personnes et des choses: uanum cSnsilium-, udna Oratis et udnl haruspices ; de la "vaniteux". Panroman, sauf roumain. M.L.yi 45 . Iri, fanas "uacuum"? Derives :juanitas (conservi sous des formes savantes en roman, M.L. yi 3 y;; uamtudo, uanities, tous deux rares, arch. ou tardifs; udnS ^S me s tlr ’ t r Per ^ CC - ^84,«); udnescS, -is (<?poq! P-). lsparaitre, s evanouir, refait sur euanesco ancien et clas¬ sique, dont existe 1'adj. euanidus, et qui est conservi en roman, m.i..3y34. Cf. aussi vanitare yi 3 8. -loalZtit a: vf n i diCU ! (PlJ; uSnil °<lvus (id.),d-o* udniloquium, loquentia, Vaniloquidorus, sans doute sur le modble des composta grecs en xevo-. Cf. inanis . Pour 1 'etymologie, v. uacare et uastus; iiascus. uapidus: v.uappa. uapor (ane. uapSs cf. Non. 487, 6), -oris ». : vapeur qui s ' 4 Uve d'un 1quide gAneralement chaud: u. aquae calidae, Ceis. 7,7,10; par ex- tension, en poesie et dans la 1 . imperiale, "chaleur", u. solis, Lucr..- lafii - uarius 1,1033, etc. M.L.yi47. Derives et composes: uaporus (tardif); uaporalis (id.); uaporarium (syn. latin de hypocaustum): etuve a vapeur; uaporosus (Apul.); uaporUlis,-liter, -reus (tardifs); uaporo, -as abs. et trans. i° "eroettre des vapeurs" aquae uaporant et in mari ipso, Plin.31,5; d'ou "bruler" (Lucr. 5, 113«) i 2° "remplir de vapeurs": u. altaria; uaporatio (epoq. imp.) et euaporo, M.L.3y 26, euaporatio; uaporifer (

### uacQ|uaco, -as|uacS,
uacQ, et les adjectifs en -ko~, du type uascus, cascus, luscus, etc. - Ancien, classique, non roman. Ddrivd complexe et expressif. On rapproche des mots diffdrents du mot latin et divergents entre eux: gr. XlXmopttl "je ddsire vivemenfi Xacrcry* Tiopvrj Hes., Xt]V(,C "baccbante" - got, lustus "envie" - v.al.laska "flatterie", r.ldsyj "ddsireux" - skr. lasati "il joue", 151 as ah "dd- sireux" (mot populaire entre dans la langue savante comme on le voit par I; tout le groupe est "populaire"). laser, -ris n. ( lasser, lasar, forme de baase dpoque, et laseris, lasaris ): suc provenant du silphium. Laser semble une forme abrdgde de lasserpiciun, laserpiciun (faite aur le modble de cicer, piper, siser, etc.); lasar rappelle S nsar, passar. Lasserpiciun est isau de lac + serplciun ( sirpiciun ; lac sirpicun dans Solin 37,49) adj. derivd de sirpe, correapondant latino-dtruaque de gr. CHXtpiov. Lel&serpicium Cio - composd, ayant cesse d’etre'compris, a fini par designer la piante elle-mSme; cf. Plin., iy, 38 , laserpicium quod Graeci oiXcpkov uocant... cuius sucum uocant laser. D«?riv4: ISserStumi sauce au laser. laserpicium (lasser-),- In.: v. le precedent; lasarplcifer (Ca¬ tulle = criXcpiospopoc;) ; laserpiciarius (P4tr.). lassus, -a, -um: las. Le sens ancien est peut-etre "qui s*incline, qui tombe en avant", cf. Vg., Ae.y,43G, lassoue papauera collo. Dimi- nutif: lassulus ( Cat. ). L'adj ectif est ddjA dans Plaute, mais semble dvit<? par les puristes qui lui prefferent fessus', il n’ est ni dans Cic. ni dans C4s.; cependant ceur-ci emploient lassitudo. Lass 5 ,- 5 s ne semble p

None
```


## [2026-09-05T20:43:26.404Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('LAT.txt',encoding='utf-8',errors='replace').read()\nfor m in re.finditer(r'uastus',t):\n    s=t[max(0,m.start()-100):m.start()+1200].replace('\\n',' ')\n    if 'd4sert' in s or 'vide' in s or 'désert' in s or 'ddsert' in s:\n        print(s); print('====')\n        break\n# et conj\nfor m in re.finditer(r'\"et\"',t):\n    pass\ni=t.find('et, conj')\nprint('et,conj idx',i)\nfor m in re.finditer(r'\\bett\\b|\\net\\s+conj|et\\s*:\\s*conj',t):\n    print(t[m.start():m.start()+300].replace('\\n',' ')); break\nEOF"
}
```


### [2026-09-05T20:43:28.169Z] TOOL RESULT

```
t pas connu. Toat ce qui conporte ane 4 tjnologie, c'est le u- initial; en latin nSae, cf. uSnus et uastusj bors du latin, cf.v.isl. wa»r~"naaquant", skr. ifno- = av.Cna- "qui nanque de, inconplet", ara .unayn "vide", gr. euvtp "priv 4 ^de", gr. eros "sana raison, vaineaent", (FjerwcrioC "vain, inutile", (xuxtoc "vaineaent", got.awis »d 4 sert", v.b.a .odi "vain, 14 ger". uSd 5 , -is, u&sl (Tert.; usnel dans les coaposds),—iiasum (dans guSsum, etc.),—ere: aller, s'avancer. At t e st 4 depuis Ennius cbez les poetes et dans la langae courante, notanaent dans les lettres faailieres de Cicdron; les coaposds guadfi, inuddV sont au contraire trbs classiques. Conserv 4 partielleaent dans toutes. les l.ronanes, oA il a fonrni des foraes de pr 4 sent, M.L.9117, avec des d 4 riv 4 s vadtcSre, *t/o ditSre, M.L.9118-9. Pas de substantifs d 4 riv 4 s. Coapos 4 s: ctrcum—u 5 d 5 ( 4 poq.iap.); gulfdSz sortir de, s^Acbapper; et, coane exire "avoir nn terne, finir par etre, ou par devenir"; " 4 cbapper a" (aecus.); guSsiS} inuadS: aarcber dans oa snr, envabir (sens propre et figur 4 ), M.L.4535, inuasil 5 ; per-, super-? tr 5 ns-uSdS. YadG conporte, toat au aoins dans ses eaplois aaciens, une nuance de rapidit 4 ou d'bostilit 4 qui n'est pas dans e 5 : cf. Enn., A.973, sed magis ferro/rem repetu
====
et,conj idx -1
ett refaits sana doute sur lea foraea en -ex, -icis oh l'e ttait phonetique, coaae artifex, opifex, etc., lea Latina ayant le sentinent qu'a un t inttrieur en syllabe ouverte correapondait un e en syllabe finale ferace. Index "celui qui aontre, qui indique" (qui a servi en particulier a designer un
```


## [2026-09-05T20:43:38.497Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('SKT.txt',encoding='utf-8',errors='replace').read()\nfor pat in [r'\\nEDDY', r'\\nWANT', r'\\nWASTE', r'\\nVAIN', r'Eddy,', r'Want,', r'Waste,', r'Vain,']:\n    m=re.search(pat,t)\n    if m: print('###',pat,'\\n',t[m.start():m.start()+700].replace('\\n',' '),'\\n')\nEOF"
}
```


### [2026-09-05T20:43:40.710Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T20:43:43.931Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"eddy\" SKT.txt | head -5\necho \"---\"\ngrep -n -i \"^WANT\\|WANT (1)\\|WANT, \" SKT.txt | head -5\necho \"--- FSD/WEB eddy ---\"\ngrep -n -i \"eddy\" WEB_vol1.txt | head -3"
}
```


### [2026-09-05T20:43:44.023Z] TOOL RESULT

```
7625:claymore,  a  Scottish  bfosflsword. ^GaeL)  Gael.  c'aUMtamk  mcr.  n  jjteil sword.  Here  ciaidheamh  is  cognate  wtili W.  deddyf^  cUddru,  a  sword,  and  with  L glAiiut  The  Gael.  mar.  great,  is  alUfld lo  W.  mawr,  L.  magnus,  great.
18989:to   toil.    (,E )     Obsolete;    once on.     A.  S.  rufincan,  pt.  t.  swam, to  labour,  work  hard.    From action ;  allied  to  Swing, to   whirl   in   an  eddy.   ^Scand.) xviria,  to  whirl  round ;  frequent. (  =  Dan.  xviVr*),  to  whirl,   orig. See  Swerve. see  Sway. a  link  turning  on  a  pin  or  neck. t  ru'ttui!  in   Minsbeu   (1617); Lh  suflix  -41  of  the  agent,  from &M,  to  move    quickly,  revolve. Swift.     Lit.  sense  'that  which ve«.'
---
9176:Indigent,  destitute-  (F.-L)  F.  iitdi- ftnt.^L.  inJi^ent't  stem  of  pre*,  part.  .oC inUigrrr,  to  be  in  want.- L.  i«*/-,  for  indo or  iHiin,  an  O.  LA.  extension  from  in,  in (cf.  Gk.  Ivhow.  within):  egert,  to  want,  he in  need;  cf.  L.  imfigus,  needy.  Cf.  Gk. ix^i*'.  poor,  needy  \.Tbcucritui).    (^  AGll  )
13739:want  (K.  -  L.)  F.  fenurit. •ia^   want,   need.  •^  Gk.  viri'a,
21184:want;  Uck.  (Souid.)  M.E.  ttun/,  Ant Died  as  an  adj ,  si(!;nifying  'deficient.' • ^Icel.  voHf^  neut.  of  wwxr,  adj,  lacking, whidi  was  formerly  used  with  a  gen.  case followine ;  as,  wtr  ^irn  vtitugis  vant,  there was  lackmg  to  them  of  nothing,  i.  e.  they wanted  nothing.  The  Iccl.  vanr  =  A.  S. •wan ;  sec  Wane  (above).  Dor.  Vfaut,  vb.. Iccl.  vartta,  from  the  adj.  txinr,
21628:woolwEird.  clothed  in  wool  only,  for Bcniince.  (£.)  See  L.  L.  L.  v.  a.  717. C  E.  w^Uwarri.  lit  with  the  skin  to- mdft  (a^^inst)  the  \rool.  From  'ivocl  and want,  suflix.     See  Toward.
--- FSD/WEB eddy ---
14741:a relapse. . 2. an eddy or backwater.
28774:the chickweed, spurrey, sandwort, pink, car- nation, T winan Gre paG are char- low: also written acterized by bright-colored flowers, opposite pe oe lobe ica on aea or wiped leaves, and stems usually swollen s A a at the joints. ae amuse of P os Ce Re ee, Sane ary o phy aai a. 1. pertaining to the f ar * aryophyllacez. » s mg Coru ennuh E a ig gild 2. having five petals with long claws in a Jun-cle, 2" ee ec ge ' tubular calyx. dim. from caro, fea orescence; specifically, car”y-6-phyllic, a. pertaining to caryophyllin. a fleshy excrescence on the head of a fowl, as car”y-6-phyVlin, n. a crystalline substance the comb of a cock, the wade of a turke cog TT same a aall 2. in botany, a prora erance surrounding Sary- i » 4. = the hilum of a seed. CEOUS a a ; preg as Jett lois _ car-y-op’sis, 7. Gr. karyon, a nut, and opsis, carun’cilar, ca runen lous, X aka an -opsin |e botany, a small one-seeded, pline og pertaining to a caruncle; having dry, indehiscent fruit, in which (ue eS ad- unces Ea lot AS he thin pericarp, so that the fruit ca-run/ci-late, ca-run/ci-la-ted, e. carun- ners rare ets nent into one body, as cular. d other kind paar pen in wheat and other kinds of grain. cart E Ara eee Blacks obtained ¢2r-y-0’tin, n. karyotin; chromatin. f n At ap P ca-sa’ba, n. [from Kassaba, town near Smyrna, 5 ane gent tree, Genipa americana. Asia Minor, whence the melon was intro- car/va-cr0l, n. (Fr. carvi, caraway, and I acer: duced any o e A acris, sharp, and oleum, oil.) a derivative o kitet UAGE Hed b Ton, oil of mint and other essential oils, being a white, watery flesh: also called casaba meton, thick, oily liquid used as an antiseptic and eae winter MER ar PE c a. ; 2 ee. n. in chemistry, the univalent cas/ca-bel, n. [Sp., a small bell, rattle, rattle- radical CHin, of which carvacrol is the hy- snake Jia knob benna tue eee Cuboeecy roxide. zd z ä a ? ; . cas-cade’, n. [Fr. cascade; It. cascata, from arve, v carved gh p2 carveg, archaic pag asare tall o ortal, cepen carve, cut; G kerben; Gr. graphein to ine 1. a small, steep waterfall, especially one of i poses : > a series. sce] make (an object, design, etc.) by or as 2. a thing like this; rippling or showering by cuttin to hew; as, to carve an image out falk a ob spat lace ieee Ca inbe of wood or stone; to carve a career. : } = ome = ae of connected Leyden jars. ai deo ie ee a tac oe mith ene Heures ete, cascade amplihcarioni 1a cle cise Vie ee as, the chest is finely carved z af of several electron tubes, each in turn ampli- S to divide by cutting; to slice, as meat at syng the sound and passing it on to the next the table. ube. h cie: v.i. 1. to cut up meat. cas-cade’, is and v.i. 1. to fall or cause to fall . to carvi i in a cascade. carved, a ae ee aie ee formed b ._2., to vomit. [Rare Colloq.] A : ~ carving. pens mormedDy EE (-y5), ie ioe] in Brazil, a doca cär’vel, n. 3 : of pebbles, gravel, and ferruginous sand, in cär/vel b TER a small ship. ae: K which the diamond is usually found. stcyel buile Goile) a- So gilding, maie cag ar a ES cae a uished from clinker-built, in which the joints tS bars 3 7 A ap. pene TED growing on the är š a acific coast of the United States. eta ab carved; made by carving; em- cascara sagrada; bark from the cascara buck- jects of y carvings, as fine woodwork or ob- thorn: used as a mild laxative. cär’ven pre chaie or Poetic.] cas-ca-ril/la, n. [Sp. dim. of cascara, peel, Gable eee participle of carve. _ bark.] the aromatic, bitter bark of Croton SSS (es Gane, Camis) Es oily,  eleuteria, a small tree oil Bess Sers substance, obtained from close relied EEE arv/é, 3 chona, cultivated chiefly cary e who cuts meat at the table. in the Bahamas: ua x a as a tonic: usually Ee carving knife. s called cascarilla bark. ERA a ue i the act or art of cutting figures cascàtillin, n. awhite, „OT stone. A crystalline, bitter sub- E E Piece of decorative work designed and stance obtained from materi Sgi wood, marble, ivory, or other cascarilla bak 5 Cary’, > à cas’cō, n. [Sp.] a flat ane eS a fork with a metal guard to boat of the Philippines, apenas hand, used to hold meat being aimes T macte Carv/ins kn z 3 j orm, used for convey- eens knife (nif), a large knife for carving ing frei ae ae Car’vis, 3 case. nf . case; OFT. rest ae in falconry, a hawk which is of casse; L. capsa, a box, peop ge and training to be carried on the chest, from capere, to
33094:Chris’tiăn Sci’ence, a religion and system of healing founded by Mary Baker Eddy in 1866, based on an interpretation of the Scrip- tures as upholding the idea that disease, sin, etc. are caused by mental error and may be eliminated by spiritual treatment without medical aid: official name, Church of Christ, Scientist.
```


## [2026-09-05T20:43:54.040Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nfor f in ('MON_part1.txt','MON_part2.txt'):\n    t=open(f,encoding='utf-8',errors='replace').read()\n    print('###',f,len(t))\n    for w in ['ونگ','دشوار','خوار']:\n        print(w, t.count(w))\nEOF"
}
```


### [2026-09-05T20:43:55.862Z] TOOL RESULT

```
### MON_part1.txt 2611770
ونگ 42
دشوار 60
خوار 287
### MON_part2.txt 2568024
ونگ 27
دشوار 55
خوار 195
```


## [2026-09-05T20:43:59.501Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('MON_part2.txt',encoding='utf-8',errors='replace').read()\nfor m in re.finditer(r'ونگ',t):\n    s=t[max(0,m.start()-250):m.start()+250].replace('\\n',' ')\n    if 'تهی' in s or 'خالی' in s or 'پهلوی' in s:\n        print(s); print('---')\nEOF"
}
```


### [2026-09-05T20:44:01.168Z] TOOL RESULT

```
ویین است در اندرون کشتی از طرف سینه  که در مواقم طوفان آب دریا که به کشتی  آید در آن جمع شود (سواحل خلیج  فارس).  تته هیکت [ع.] (.) تهیگاه؛ ج . کشوح.   : ۵۹2۲ (.) ریسمانی که خوشه‌های  انگور کشمش را بر بالای آن گذارند تا هوا  خورد و خشکك شود و آن جز آونگ  است.  کش‌خان: ۲۵۶ ,۲۵5۰ [ع.- کشیخان]  (ص.) زن جلب. زن قحبه» دبوث.  کشخور: :۲65۳ (- کشور | (.) یکك بخش  از هفت بحش زمین؟ اقلیم.  کش دادن: «د۲۰3-۵2۵ (مص‌م.) (عم.) کش  دادن سوضوعی (کلامی) را: (عم.) طول  دادن آن را.  کشدار: ۷-۲ [(- کش‌دارنده] (ص‌فا.
---
نت: ها عم[ ]۷2 [ع.]  (ص‌مر. امر.) آنکه بر کسی حق نعمت دارد.  ود: ۷(.) (گیا.) سنه. (گسیا.) زبان  ون: ۷۸۰ [هندی] (.) جنگل پر درخت.  ود: ۷۸۰ [تر. ختایی] (ا.) ده هزار سال.  ونانه: (6-)۷2۵۵02 (.) نان گر ده نان کلفت.  ونکول: ۷۲ (۰) کار لا زم» امر  صروری.  ونگ: ۵ ,۷2۳ (ص.) تهی» خالی.  ونگ: 6 (ص.) درو ش» تهبدست»  مفلس .دا سایل.  ونگ: 8 [ - بانگ» صدا] (1.) (عم.) صدا  و آوازه بانگگ. (عم.) داد و فریاد. ۰ (عم.)  گریة توا ام با داد و فرباد:  وننگ: 8 اقس. آونگ] (ا.) سر شاخ  بریدة انگور. تااث انگور. ریسمانی که
---
مر.) آنکه بر کسی حق نعمت دارد.  ود: ۷(.) (گیا.) سنه. (گسیا.) زبان  ون: ۷۸۰ [هندی] (.) جنگل پر درخت.  ود: ۷۸۰ [تر. ختایی] (ا.) ده هزار سال.  ونانه: (6-)۷2۵۵02 (.) نان گر ده نان کلفت.  ونکول: ۷۲ (۰) کار لا زم» امر  صروری.  ونگ: ۵ ,۷2۳ (ص.) تهی» خالی.  ونگ: 6 (ص.) درو ش» تهبدست»  مفلس .دا سایل.  ونگ: 8 [ - بانگ» صدا] (1.) (عم.) صدا  و آوازه بانگگ. (عم.) داد و فریاد. ۰ (عم.)  گریة توا ام با داد و فرباد:  وننگ: 8 اقس. آونگ] (ا.) سر شاخ  بریدة انگور. تااث انگور. ریسمانی که دو  سر آن را بر دو دیوار یا 
---
ا.) سنه. (گسیا.) زبان  ون: ۷۸۰ [هندی] (.) جنگل پر درخت.  ود: ۷۸۰ [تر. ختایی] (ا.) ده هزار سال.  ونانه: (6-)۷2۵۵02 (.) نان گر ده نان کلفت.  ونکول: ۷۲ (۰) کار لا زم» امر  صروری.  ونگ: ۵ ,۷2۳ (ص.) تهی» خالی.  ونگ: 6 (ص.) درو ش» تهبدست»  مفلس .دا سایل.  ونگ: 8 [ - بانگ» صدا] (1.) (عم.) صدا  و آوازه بانگگ. (عم.) داد و فریاد. ۰ (عم.)  گریة توا ام با داد و فرباد:  وننگ: 8 اقس. آونگ] (ا.) سر شاخ  بریدة انگور. تااث انگور. ریسمانی که دو  سر آن را بر دو دیوار یا دو ستون بندند و  خوشه‌های انگور از آن آویزند
---
 ده نان کلفت.  ونکول: ۷۲ (۰) کار لا زم» امر  صروری.  ونگ: ۵ ,۷2۳ (ص.) تهی» خالی.  ونگ: 6 (ص.) درو ش» تهبدست»  مفلس .دا سایل.  ونگ: 8 [ - بانگ» صدا] (1.) (عم.) صدا  و آوازه بانگگ. (عم.) داد و فریاد. ۰ (عم.)  گریة توا ام با داد و فرباد:  وننگ: 8 اقس. آونگ] (ا.) سر شاخ  بریدة انگور. تااث انگور. ریسمانی که دو  سر آن را بر دو دیوار یا دو ستون بندند و  خوشه‌های انگور از آن آویزند؛ آونگ.    وور و وور فرهنگ فارسی معین ۹ ۲    وور و وور: ۷۳۲۰۰۷ (ق.) (عسم.)   متوالی پی در پی» پشت سر هم.   وول: ۵۱ (.) (عم.)
---
دسته: (6-)۸5۱۸-.۱ (امر.) اسزاری  است از سنگ» چوب با فلز که به وسبلة آن  چیزی را در هاون کوند.   هاون‌کوب: ۰-0 [- همساون کونده]    (ص‌فا.) آنکه در هاون چیزی را کوید. کسی  که تخم گیاهان و ادویه را جهت عطاران و  طییان کوبد. کسی که م رکب (سیاه) سازد.  هاونگاه: «تی.« (.) (زردشتی) یکی از  اوقات پنجگانة روز و آن وقتی بوده است  که در آن شربت مقدس هوم تهیه می‌شده»  مدت آن از هنگام طلوع خورشید تا ظهر  بوده است.   هاویه: 2۲:۵ (ع. هاویه| (اخ.) طبقة  هفتم از طبقات دوزخ و آن پایین‌ترین طبقه  است؛. (اح.) دوزخ»
---
```


## [2026-09-05T20:44:08.611Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('MON_part2.txt',encoding='utf-8',errors='replace').read()+open('MON_part1.txt',encoding='utf-8',errors='replace').read()\nfor m in re.finditer(r'دشوار',t):\n    s=t[max(0,m.start()-200):m.start()+250].replace('\\n',' ')\n    if 'پهلوی' in s or 'دشخوار' in s:\n        print(s); print('---')\nEOF"
}
```


### [2026-09-05T20:44:10.388Z] TOOL RESULT

```
-0 (ص‌مر.) کسی که  آرزوی خصم» ند بخت» تبر دیحت.  دشمنی: -0301271 (حامص.) عداوت»  خصومت؛ مق. دوستی» مست. کراهت»  نفرت.   دشنام: تمه (امر.) نام زشت» فحش؛  ناسزا.   دشنه؛ (0-)12302 (.) کارد برنده و نوک  دشوار: 005-۲ (ص‌مر. آمر.) سحت)؛  صعب» مشکل؛ دشخوار؛ مق. آسان» سهل.  دعاب: [ع.] (ص.) شوخی کننده»  لاغ گوی. شوخ.   دعابه: (0-)۵2500 [ع. دعابة] (مصل.)  مداعبت» شوخی کردن» لاغ گفتن. (امص.)    ۱۸۴ فرهنگ فارسی معیر دعاگو(ی)    و :   دعاگکو(ی): ٩.-۵00(‏ [ع.
---
```


## [2026-09-05T20:44:16.563Z] TOOL CALL #69: Bash

```json
{
 "command": "sed -n 1,40p tools/fetch_source.py"
}
```


### [2026-09-05T20:44:16.600Z] TOOL RESULT

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


## [2026-09-05T20:44:21.841Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wiktionary.org/wiki/%D8%AE%D9%88%D8%A7%D8%B1\" \\\n \"https://en.wiktionary.org/wiki/%D8%AF%D8%B4%D9%88%D8%A7%D8%B1\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81eti\" \\\n \"https://www.etymonline.com/word/eddy\" \\\n \"https://www.etymonline.com/word/want\" \\\n \"https://www.etymonline.com/word/waste\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 162 verification (Eter/xwar-dosvar; Eti; Eu 1)\" 2>&1 | tail -2\ndone"
}
```


### [2026-09-05T20:44:25.713Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/337c858163fb4548.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/fbd77c143863436f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6a682e9906c431e7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/47aea978e24f8e08.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f772a0d031ada54e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/fc89746b293ffe3c.txt
```


## [2026-09-05T20:44:29.166Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"=== خوار ===\"; python3 -c \"\nimport re,sys\nt=open('337c858163fb4548.txt',encoding='utf-8').read()\ni=t.find('Persian')\nprint(t[:60])\nfor m in re.finditer(r'Etymology',t):\n    print(t[m.start():m.start()+700].replace(chr(10),' ')); print('--')\n\" | head -40"
}
```


### [2026-09-05T20:44:30.842Z] TOOL RESULT

```
=== خوار ===
URL: https://en.wiktionary.org/wiki/%D8%AE%D9%88%D8%A7%D8%B1
Etymology 1    3.2.1   Adjective    3.2.1.1   Descendants    3.3   Etymology 2    3.3.1   Verb    3.4   References    4   Ushojo    Toggle Ushojo subsection    4.1   Etymology    4.2   Adjective    Toggle the table of contents    خوار    7 languages    فارسی   Magyar   Kurdî   Malagasy   پښتو   Русский   سرائیکی    Entry    Discussion    English    Read    Edit    View history    Tools    Tools   move to sidebar   hide    Actions   Read    Edit    View history    General   What links here   Related changes   Upload file   Permanent link   Page information   Cite this page   Get shortened URL    Print/export   Create a book   Download as PDF   Printable version    In other projects   Appearan
--
Etymology 2    3.3.1   Verb    3.4   References    4   Ushojo    Toggle Ushojo subsection    4.1   Etymology    4.2   Adjective    Toggle the table of contents    خوار    7 languages    فارسی   Magyar   Kurdî   Malagasy   پښتو   Русский   سرائیکی    Entry    Discussion    English    Read    Edit    View history    Tools    Tools   move to sidebar   hide    Actions   Read    Edit    View history    General   What links here   Related changes   Upload file   Permanent link   Page information   Cite this page   Get shortened URL    Print/export   Create a book   Download as PDF   Printable version    In other projects   Appearance   move to sidebar   hide    From Wiktionary, the free dictionary
--
Etymology    4.2   Adjective    Toggle the table of contents    خوار    7 languages    فارسی   Magyar   Kurdî   Malagasy   پښتو   Русский   سرائیکی    Entry    Discussion    English    Read    Edit    View history    Tools    Tools   move to sidebar   hide    Actions   Read    Edit    View history    General   What links here   Related changes   Upload file   Permanent link   Page information   Cite this page   Get shortened URL    Print/export   Create a book   Download as PDF   Printable version    In other projects   Appearance   move to sidebar   hide    From Wiktionary, the free dictionary   See also: حوار , چوار , جواز , and جوار    Arabic  [ edit ]    Root    خ و ر ( ḵ w r )    3 term
--
Etymology 1  [ edit ]    From Middle Persian [script needed] ( hw'l /⁠xᵛār⁠/ ) , from Proto-Iranian *ātra- / *āθra- ( “ spirit, breath ” ) , of unknown further origin. [ 1 ]    Adjective  [ edit ]    خوار • ( xvâr )    ( archaic ) easy    mean , abject    Descendants  [ edit ]    → Kazakh: қор ( qor )    → Ottoman Turkish: خور ( hor ) , خوار ( har, hor ) Turkish: hor   → Armenian: խոռ ( xoṙ )    → Turkmen: har , hor    Etymology 2  [ edit ]    See below.   Verb  [ edit ]    خوار • ( xvâr )    present stem form of خواردن ( “ to eat, to consume ” )    References  [ edit ]    ^ Rastorgujeva, V. S. ; Edelʹman, D. I. ( 2000 ), Etimologičeskij slovarʹ iranskix jazykov [ Etymological Dictionary of 
--
Etymology 2  [ edit ]    See below.   Verb  [ edit ]    خوار • ( xvâr )    present stem form of خواردن ( “ to eat, to consume ” )    References  [ edit ]    ^ Rastorgujeva, V. S. ; Edelʹman, D. I. ( 2000 ), Etimologičeskij slovarʹ iranskix jazykov [ Etymological Dictionary of Iranian Languages ] (in Russian), volume 1, Moscow: Vostochnaya Literatura, page 324    Ushojo  [ edit ]    Etymology  [ edit ]    From Persian خوار ( xvâr ) .   Adjective  [ edit ]    خوار ( xvār )    weak    vulnerable    Retrieved from " https://en.wiktionary.org/w/index.php?title=خوار&oldid=92261680 "   Categories : Arabic terms belonging to the root خ و ر   Arabic 2-syllable words   Arabic terms with IPA pronunciat
--
Etymology  [ edit ]    From Persian خوار ( xvâr ) .   Adjective  [ edit ]    خوار ( xvār )    weak    vulnerable    Retrieved from " https://en.wiktionary.org/w/index.php?title=خوار&oldid=92261680 "   Categories : Arabic terms belonging to the root خ و ر   Arabic 2-syllable words   Arabic terms with IPA pronunciation   Rhymes:Arabic/aːr   Rhymes:Arabic/aːr/2 syllables   Arabic lemmas   Arabic adjectives   Arabic adjectives with basic triptote singular   Arabic adjectives with triptote singular in -a   Arabic adjectives with broken plural   Arabic adjectives with basic triptote broken plural   Arabic nouns   Arabic masculine nouns   Arabic verbal nouns   Arabic nouns with basic triptote singu
--
```


## [2026-09-05T20:44:49.803Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\npython3 -c \"\nimport re\nt=open('fbd77c143863436f.txt',encoding='utf-8').read()\ni=t.find('Etymology  [ edit ]')\nprint(t[i:i+900].replace(chr(10),' '))\n\"\necho \"=== PIE h1eti ===\"\npython3 -c \"\nimport re\nt=open('6a682e9906c431e7.txt',encoding='utf-8').read()\ni=t.find('Proto-Indo-European  [ edit ]')\nprint(t[i:i+1500].replace(chr(10),' '))\n\""
}
```


### [2026-09-05T20:44:51.565Z] TOOL RESULT

```
=== PIE h1eti ===
```


## [2026-09-05T20:44:55.160Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\npython3 -c \"\nt=open('fbd77c143863436f.txt',encoding='utf-8').read()\ni=t.find('From Wiktionary, the free dictionary')\nprint(t[i:i+1400].replace(chr(10),' '))\n\"\necho \"=== h1eti file ===\"\npython3 -c \"\nt=open('6a682e9906c431e7.txt',encoding='utf-8').read()\nprint(len(t))\ni=t.find('From Wiktionary, the free dictionary')\nprint(t[i:i+1500].replace(chr(10),' '))\n\""
}
```


### [2026-09-05T20:44:56.713Z] TOOL RESULT

```
From Wiktionary, the free dictionary   Ottoman Turkish  [ edit ]    Etymology  [ edit ]    Borrowed from Persian دشوار ( došvâr , “ difficult, hard ” ) , from Middle Persian [script needed] ( dwšw'l /⁠dušwār⁠/ ) .   Adjective  [ edit ]    دشوار • ( düşvâr )    difficult , hard , cumbersome , demanding to handle or get around with  Synonyms: چتین ( çetin ) , سخت ( saht ) , گوچ ( güç ) , مشكل ( müşkil )    Derived terms  [ edit ]    دشوار پسند ( düşvâr pesend , “ hard to please ” )   دشوارلق ( düşvârlık , “ difficulty, hardness ” )   دشواری ( düşvârî , “ difficulty, hardness ” )    Descendants  [ edit ]    Turkish: düşvar    Further reading  [ edit ]    Çağbayır, Yaşar ( 2007 ), “ düşvar ”, in Ötüken Türkçe Sözlük (in Turkish), volume 1, Istanbul: Ötüken Neşriyat, page 1338    Devellioğlu, Ferit ( 1962 ), “düşvâr”, in Osmanlıca-Türkçe Ansiklopedik Lûgat ‎ [ Ottoman–Turkish Encyclopedic Dictionary ]‎ [1] (in Turkish), Istanbul: Türk Dil Kurumu, page 231    Kélékian, Diran ( 1911 ), “ دشوار ”, in Dictionnaire turc-français ‎ [2] (in French), Constantinople: Mihran, page 573    Meninski, Franciszek à Mesgnien ( 1687 ), “Difficilis”, in Complementum thesauri linguarum orientalium, seu onomasticum latino-turcico-arabico-persicum, simul idem index verborum lexici turcico-arabico-persici, quod latinâ, germanicâ, aliarumque linguarum adjectâ nomenclatione nuper in lucem editum ‎ [3] , Vi
=== h1eti file ===
5619
From Wiktionary, the free dictionary   (Redirected from Reconstruction:Proto-Indo-European/h₁eti )    This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.   Proto-Indo-European  [ edit ]    Etymology  [ edit ]    De Vaan proposes an old locative singular of *h₁et- , [ 1 ] [ 2 ] reflected in Sanskrit अत् ( at , “ to go ” ) , as he explains “Originally used to add something to a previous utterance, or to indicate the sequence of different actions”. Compare *h₂énti and *h₁épi / *h₁ópi for similar derivations of particles in *-i . Beekes and Derksen give the same etymology provided by De Vaan. [ 3 ] [ 4 ] Ringe, however, reconstructs it as *éti . [ 5 ]    Alternatively, Dunkel prefers a derivation from *e- +‎ *-ti ( ablative suffix ) as "from there" > "beyond". [ 6 ]    Adverb  [ edit ]    *éti [ 5 ] [ 6 ]    beyond   Synonym: *h₂epóterom    over   Synonym: *upér    and   Synonyms: *de , *-kʷe    Reconstruction notes  [ edit ]    Conflated in some descendants with *h₂et- ( “ but, yet; and ? ” ) ; see there for more.   Alternative reconstructions  [ edit ]    *h₁eti [ 1 ]    Descendants  [ edit ]    (?) Proto-Armenian:   Old Armenian: -է ( -ē )    Proto-Balto-Slavic: *ati ( from *h₁óti , unless from *h₂éti )   Lithuanian: at- ( “ back, away ” )    Latvian: at- ( “ back away ” )    Old Prussian: et- , at-    Proto-Slavic: *otъ ( see t
```


## [2026-09-05T20:45:01.980Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\npython3 -c \"\nt=open('6a682e9906c431e7.txt',encoding='utf-8').read()\ni=t.find('Descendants  [ edit ]')\nprint(t[i:i+2200].replace(chr(10),' '))\n\""
}
```


### [2026-09-05T20:45:04.145Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T20:45:06.634Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\npython3 -c \"\nt=open('6a682e9906c431e7.txt',encoding='utf-8').read()\ni=t.find('Descendants')\nprint(repr(t[i:i+2200]))\n\""
}
```


### [2026-09-05T20:45:08.605Z] TOOL RESULT

```
'Descendants \n\n 1.3 \n References \n\n Toggle the table of contents \n\n Reconstruction:Proto-Indo-European/ éti \n\n Add languages \n\n Reconstruction \n\n Discussion \n\n English \n\n Read \n\n Edit \n\n View history \n\n Tools \n\n Tools\n\n move to sidebar \n hide \n\n Actions\n\n Read \n\n Edit \n\n View history \n\n General\n\n What links here \n Related changes \n Upload file \n Permanent link \n Page information \n Get shortened URL \n\n Print/export\n\n Download as PDF \n Printable version \n\n In other projects\n\n Appearance\n\n move to sidebar \n hide \n\n From Wiktionary, the free dictionary\n\n (Redirected from Reconstruction:Proto-Indo-European/h₁eti ) \n\n This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.\n\n Proto-Indo-European\n [ edit ] \n\n Etymology\n [ edit ] \n\n De Vaan proposes an old locative singular of *h₁et- , [ 1 ] [ 2 ] reflected in Sanskrit अत् ( at , “ to go ” ) , as he explains “Originally used to add something to a previous utterance, or to indicate the sequence of different actions”. Compare *h₂énti and *h₁épi / *h₁ópi for similar derivations of particles in *-i . Beekes and Derksen give the same etymology provided by De Vaan. [ 3 ] [ 4 ] Ringe, however, reconstructs it as *éti . [ 5 ] \n\n Alternatively, Dunkel prefers a derivation from *e- +\u200e *-ti ( ablative suffix ) as "from there" > "beyond". [ 6 ] \n\n Adverb\n [ edit ] \n\n *éti [ 5 ] [ 6 ] \n\n beyond \n Synonym: *h₂epóterom \n\n over \n Synonym: *upér \n\n and \n Synonyms: *de , *-kʷe \n\n Reconstruction notes\n [ edit ] \n\n Conflated in some descendants with *h₂et- ( “ but, yet; and ? ” ) ; see there for more.\n\n Alternative reconstructions\n [ edit ] \n\n *h₁eti [ 1 ] \n\n Descendants\n [ edit ] \n\n (?) Proto-Armenian: \n Old Armenian: -է ( -ē ) \n\n Proto-Balto-Slavic: *ati ( from *h₁óti , unless from *h₂éti ) \n Lithuanian: at- ( “ back, away ” ) \n\n Latvian: at- ( “ back away ” ) \n\n Old Prussian: et- , at- \n\n Proto-Slavic: *otъ ( see there for further descendants )\n\n Proto-Celtic: *eti , > ? ( partially ) *ati- ( see there for further descendants )\n\n Proto-Germanic: *idi , *idi- ( see there for further descendants '
```


## [2026-09-05T20:45:13.122Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\npython3 -c \"\nt=open('6a682e9906c431e7.txt',encoding='utf-8').read()\ni=t.find('Proto-Germanic: *idi')\nprint(t[i:i+900])\n\"\necho \"=== etymonline eddy ===\"\npython3 -c \"\nt=open('47aea978e24f8e08.txt',encoding='utf-8').read()\ni=t.find('eddy')\nprint(t[i:i+1200].replace(chr(10),' '))\n\""
}
```


### [2026-09-05T20:45:14.799Z] TOOL RESULT

```
Proto-Germanic: *idi , *idi- ( see there for further descendants )

 Proto-Hellenic: 
 Ancient Greek: ἔτι ( éti , “ yet ” ) 

 Proto-Indo-Iranian: *áti ( see there for further descendants )

 Proto-Italic: *et ( see there for further descendants )

 Proto-Tocharian: *āté [ 7 ] 
 Tocharian B: ate 

 Proto-Tocharian: 
 Tocharian B: -ṣ 

 References
 [ edit ] 

 ↑ 1.0 1.1 De Vaan, Michiel ( 2008 ), “ et ”, in Etymological Dictionary of Latin and the other Italic Languages (Leiden Indo-European Etymological Dictionary Series; 7), Leiden, Boston: Brill, →ISBN , page 195 

 ^ Schrijver, Peter (1991) The Reflexes of the Proto-Indo-European Laryngeals in Latin, in Leiden Studies in Indo-European, Volume: 2, page 36 

 ^ Beekes, Robert S. P. ( 2010 ), “ ἔτῐ ”, in Etymological Dictionary of Greek (Leiden Indo-European Etymological Dictionary Series; 10 ), with the assistance of Lucien van Beek, Le
=== etymonline eddy ===
eddy FETCHED: 2026-09-05T20:44:24Z STATUS: 200 TITLE: Eddy - Etymology, Origin & Meaning  Eddy - Etymology, Origin & Meaning    Search   Log in    Columns   Forum   Apps   Premium    Log in    A B C D E F G H I J K L M N O P Q R S T U V W X Y Z    Quick and reliable accounts of the origin and history of English words. Scholarly, yet simple.   About  Who Did This   Sources   Introduction   Links    Support  Premium   Patreon   Donate with PayPal   Merch    Apps  Get Chrome Extension   Get iOS App   Get Android App    Dark  Auto  Light   Terms of Services Privacy Policy    English (English)   © 2001–2026 Douglas Harper & Talia Felix    Advertisement Remove Ads   Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.   Origin and history of eddy    eddy (n.)    mid-15c., Scottish ydy , possibly related to Old Norse iða "whirlpool," from Proto-Germanic *ith- "a second time, again," which is related to the common Old English prefix ed- "again, backwards; repetition, turning" (forming such words as edðingung "reconciliation," edgift "restitution," edniwian "to renew, restore," edhwierfan "to retrace one's steps," edgeong "to become young again"). Comp
```


## [2026-09-05T20:45:20.541Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in f772a0d031ada54e fc89746b293ffe3c; do\npython3 -c \"\nimport sys\nt=open('$f.txt',encoding='utf-8').read()\ni=t.find('Origin and history of')\nprint(t[i:i+1300].replace(chr(10),' '))\nprint()\n\"\ndone"
}
```


### [2026-09-05T20:45:22.154Z] TOOL RESULT

```
Origin and history of want    want (v.)    c. 1200, wanten , "be lacking, be deficient in something," from Old Norse vanta "to lack, want," earlier *wanaton , from Proto-Germanic *wanen , from PIE *weno- , suffixed form of root *eue- "to leave, abandon, give out." The meaning "desire, wish for, feel the need of" is recorded by 1706.  also from c. 1200    want (n.)    c. 1200, "deficiency, insufficiency, absence or lack of," from want (v.) and from Old Norse vant , neuter of vanr "wanting, deficient;" related to Old English wanian "to diminish" (see wane ).   The meaning "state of destitution, poverty, penury" is recorded from early 14c. The meaning "thing desired, that which is lacking but needed" is from 1560s. Phrase for want of is recorded from c. 1400. The newspaper want ad is recorded from 1897. Middle English had wantsum (c. 1200) "in want, deprived of," literally "want-some."  also from c. 1200    Entries linking to want    wane (v.)    Middle English wannen , "decrease, be diminished," especially of the periodic lessening of the visible moon, from Old English wanian "make or become smaller gradually, diminish, decline, fade," from Proto-Germanic *wanōnan (source also of Old Saxon wanon , Old Norse vana , Old Frisian wania , Middle Dutch waenen , Old High German wanon "to 

Origin and history of waste    waste (v.)    c. 1200, wasten , "devastate, ravage, ruin," from Anglo-French and Old North French waster "to waste, squander, spoil, ruin" (Old French gaster ; Modern French gâter ), altered (by influence of Frankish *wostjan ) from Latin vastare "lay waste," from vastus "empty, desolate." This is reconstructed in Watkins to be from a suffixed form of PIE root *eue- "to leave, abandon, give out." Related: wasted ; wasting .   The Germanic word also existed in Old English as westan "to lay waste, ravage." Spanish gastar , Italian guastare also are from Germanic.   The intransitive meaning "lose strength or health; pine; weaken or be gradually consumed" is attested from c. 1300; the sense of "squander, spend or consume uselessly, expend without adequate return" is recorded from mid-14c.; the colloquial meaning "to kill" is from 1964.   To waste time "act to no purpose" is from mid-14c. Waste not, want not is attested from 1778.  also from c. 1200    waste (n.)    c. 1200, "wild, desolate regions; uncultivated or uninhabited land," from Anglo-French and Old North French wast "waste, damage, destruction; wasteland, moor" (Old French gast ), from Latin vastum , neuter of vastus "empty, desolate" (from PIE *wasto- , extended suffixed form of root *eue- "t
```


## [2026-09-05T20:45:44.864Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://www.etymonline.com/word/et%20cetera\" \\\n \"https://www.etymonline.com/word/vain\" \\\n \"https://en.wiktionary.org/wiki/%D9%88%D9%86%DA%AF\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 162 verification (Eti: et cetera; Eu 1: vain, vang)\" 2>&1 | tail -1\ndone\ntail -9 data/verification/sources/web/index.jsonl | python3 -c \"\nimport sys,json\nfor l in sys.stdin: d=json.loads(l); print(d['url'],'|',d.get('status'),'|',d.get('title'))\""
}
```


### [2026-09-05T20:45:48.353Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/8758d7a34cc492c8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5a964079589bb9eb.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6c8a0369fc9ba9f7.txt
https://en.wiktionary.org/wiki/%D8%B1%DB%8C%D9%88%D8%A7%D8%B3 | 200 | ریواس - Wiktionary, the free dictionary
https://en.wiktionary.org/wiki/%D8%B3%DB%8C%D8%A7%D9%88%D8%B4 | 200 | سیاوش - Wiktionary, the free dictionary
https://www.etymonline.com/word/error | 200 | Error - Etymology, Origin & Meaning
https://abadis.ir/fatofa/%DA%AF%D8%A7%D9%87/ | 200 | گاه - معنی در دیکشنری آبادیس
https://en.wiktionary.org/wiki/%DA%AF%D8%A7%D9%87 | 200 | گاه - Wiktionary, the free dictionary
https://www.wisdomlib.org/definition/jama | 200 | Jama, Jāmā: 15 definitions
https://www.etymonline.com/word/et%20cetera | 200 | Et cetera - Origin & Meaning of the Phrase
https://www.etymonline.com/word/vain | 200 | Vain - Etymology, Origin & Meaning
https://en.wiktionary.org/wiki/%D9%88%D9%86%DA%AF | 200 | ونگ - Wiktionary, the free dictionary
```


## [2026-09-05T20:45:51.941Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\npython3 -c \"\nt=open('6c8a0369fc9ba9f7.txt',encoding='utf-8').read()\ni=t.find('From Wiktionary, the free dictionary')\nprint(t[i:i+1200].replace(chr(10),' '))\n\"\necho \"=== et cetera ===\"\npython3 -c \"\nt=open('8758d7a34cc492c8.txt',encoding='utf-8').read()\ni=t.find('Origin and history of')\nprint(t[i:i+800].replace(chr(10),' '))\n\""
}
```


### [2026-09-05T20:45:54.457Z] TOOL RESULT

```
From Wiktionary, the free dictionary   Mazanderani  [ edit ]    Etymology  [ edit ]    From Middle Persian 𐭥𐭠𐭭𐭢 ( ʿʾng /⁠vāng⁠/ ) , probably from Proto-Indo-European *wṓkʷs ( “ voice, speech ” ) .    Noun  [ edit ]    ونگ ( vang )    voice , sound , noise    Derived terms  [ edit ]    ونگ وا ( vang-e vā )    References  [ edit ]    حسن‌دوست، واژه‌نامه ریشه‌شناسی ۵ جلدی (Persian)   Punjabi  [ edit ]    Etymology  [ edit ]    From Prakrit 𑀯𑀗𑁆𑀕 ( vaṅga ) .   Pronunciation  [ edit ]    ( Standard Punjabi ) IPA ( key ) : /ʋəŋɡ/ , [ʋə̃ŋɡ(ə̆)]    Rhymes: -əŋɡ    Noun  [ edit ]    وَن٘گ • ( vaṉg )  f ( Gurmukhi spelling ਵੰਗ )    bangle ( made out of glass or plastic )    Declension  [ edit ]    Declension of ونگ    singular   plural   direct   وَن٘گ ( vaṉg )    وَن٘گاں ( vaṉgāṉ )    oblique   وَن٘گ ( vaṉg )    وَن٘گاں ( vaṉgāṉ )    vocative   وَن٘گے ( vaṉge )    وَن٘گو ( vaṉgo )    ablative   وَن٘گوں ( vaṉgoṉ )    —   locative   وَن٘گی ( vaṉgī )    وَن٘گِیں ( vaṉgīṉ )    instrumental   وَن٘گے ( vaṉge )    وَن٘گِیں ( vaṉgīṉ )    Further reading  [ edit ]    Iqbal, Salah ud-Din ( 2002 ), “ ونگ ”, in vaḍḍī panjābī lughat (in Punjabi), Lahore: عزیز پبلشرز [ ʻazīz pabliśarz ]    “ ਵੰਗ ”, in Pun
=== et cetera ===
Origin and history of et cetera    et cetera    also etcetera , early 15c., from Latin et cetera , literally "and the others," from et "and" + neuter plural of ceterus "the other, other part, that which remains," from Proto-Italic *ke-etero‑ , from *ke- , variant form of PIE root *ko- , the stem of demonstrative pronoun meaning "this" + *etero‑ "other (of two), again, a second time, again," a PIE adjective of comparison.   The common form of the abbreviation before 20c. was &c. , but etc. now prevails.  also from early 15c.    Entries linking to et cetera    etc.    see et cetera .   etcetera    see et cetera .   plus   *ko-   See All Related Words (4)    Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.   More to explore   plus    15
```


## [2026-09-05T20:47:47.634Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### AHD eter?\"\ngrep -n \"^eter\\|eter-\\.\\|Pok. eter\" AHD_watkins1985.txt | head\necho \"### AHD ADDER/HEART?\"\ngrep -c \"eter-\" AHD_watkins1985.txt\necho \"### WLD Bd1 p.43 (leaf 51)\"\npython3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (50,51,52):\n    p=pages[i]\n    if 'eti' in p:\n        j=p.find('eti')\n        print('leaf',i,p[:60].replace('\\n',' '))\nprint(pages[51][:1800].replace('\\n',' '))\nEOF"
}
```


### [2026-09-05T20:47:49.704Z] TOOL RESULT

```
### AHD eter?
392:dhugheter-. Daughter. Germanic *dohtér in Old English dohtor, daughter: DAUGHTER. [Pok. dhug(hjeter 277.]
846:ré, feather, in Old English fether, feather: FEATHER. 2. Latin petere, to go toward, seek: -PETAL, PETITION, PETULANT; APPETITE, COMPETE, IMPETUS, PERPETUAL, REPEAT. 3. Suffixed form *pet-nd in Latin penna, pinna, feather, wing: PANACHE, PEN!, PENNA, PENNATE, PEN- NON, PINNA, PINNACLE, PINNATE, PINNATI-, PINNULE. 4. Suffixed form *pet-ro- (see 6ku-). 5. Suffixed form *pet-yo- in Latin propitius, favorable, gracious, originally a religious term meaning “falling or rushing forward,” hence “eager,” “well-disposed” (said of the gods; pro-, forward; see per'): PROPITIOUS. 6. Suffixed zero-grade form *pt-ero- in Greek pteron, feather, wing, and pterux, wing: -PTER; ACANTHOPTERYGIAN, APTERYX, ARCHAEOP- TERYX, COLEOPTERA, MECOPTERAN, PERIPTERAL, PLE- COPTERAN, PTERIDOLOGY, PTEROCERCOID, PTERYGOID. 7. Suffixed zero-grade form “pt-ilo- in Greek ptilon, soft feathers, down, plume: COLEOPTILE. 8. Suffixed variant form *pté-no- in Greek pténos, winged, flying: STEAROP- TENE. 9. Reduplicated form *pi-pt- in Greek piptein, to fall: PTOMAINE, PTOSIS; PERIPETEIA, PROPTOSIS, SYMP- TOM. 10. O-grade form “pof- in Greek potamos (-amo-, Greek suffix), “rushing water,” river: HIPPOPOTAMUS. [Pok. 2. pet- 826.] pete-. To spread. 1. Suffixed o-grade form “pota)-mo- in Germanic *fathmaz, “length of two arms stretched out,” in Old English fethm, fathom: FATHOM. 2. Suffixed (stative) variant zero-grade form *pat-é- in Latin patére, to be open: PATENT, PATULOUS. 3. Variant zero-grade form in nasalized form *pat-no- probably in Latin pan- dere (past participle passus < *pat-to-), to spread out: PACE!, (PAS), (PASS), PASSIM; EXPAND, REPAND. 4. Suf- fixed form *pet-alo- in Greek petalon, leaf: PETAL. 5. Suf- fixed form *pet-ano- in Greek patané (? < *petand), platter, “thing spread out”: (PAELLA), PAN!, PATEN, (PATINA!), (PATINA2). [Pok. 1. pet- 824.] [petra. Cliff. Greek noun. Collective formation from petros, rock, stone (of unknown origin). PETRO-, PET- ROUS; PARSLEY, PETRIFY, SALTPETER.] peu-. To cut, strike, stamp. 1. Suffixed (participial) zero-grade form *pu-to-, cut, struck, in: a. Latin putdre, to prune, clean, settle an account, think over, reflect, consider: PUTAMEN, PUTATIVE; (ACCOUNT), AMPUTATE, COMPUTE, COUNT!, DEPUTE, DISPUTE, IMPUTE, REPUTE; b. possibly Latin puteus, well (> Old English pyét): Prt’. 2. Variant form *pau- in: a. suffixed form *pau-yo- in Latin pavire, to beat: PAVE, (PAVE); b. suffixed (stative) form *paw-é- in Latin pavére, to fear (< “to be struck”): PAVID; C. perhaps Greek paiein, to beat: ANAPEST. [Pok. 3. péu- 827.] peue-. To purify, cleanse. Suffixed zero-grade form *pii-ro- (< *pua-ro-) in Latin purus, pure, and purgdre, to purify (< “piir-igdre; second element agere, to drive; see ag-): PURE, PURGE, PURITAN; COMPURGATION, DEPU- RATE, EXPURGATE, (SPURGE). [Pok. 1. peu- 827.] peuk-. Also peug-. To prick. Zero-grade form “pug-. 1. Suffixed form *pug-no- in Latin pugil, pugilist, and pugnus, fist, with denominative pugndare, to fight with the fist: PONIARD, PUGILISM, PUGIL STICK, PUGNACIOUS; IMPUGN, OPPUGN, REPUGN. 2. Nasalized zero-grade form *pu-n-g- in Latin pungere, to prick: BUNG, POIGNANT, POINT, POINTILLISM, PONTIL, (POUNCE!), (POUNCE?), PUNCHEON!, PUNCTUATE, PUNCTURE, PUNGENT; COM- PUNCTION, EXPUNGE, SPONTOON, TRAPUNTO. 3. Greek pugmé, fist: (PYGMAEAN), PYGMY. [Pok. peuk- 828.] pezd-. To fart. 1. Suffixed form *pezd-i- in Germanic *fistiz, a fart, in Middle English fisten, to fart: FEIST, FIZZLE. 2. Latin pédere, to fart: PETARD. 3. Possibly Latin pédis, louse (? < “foul-smelling insect”): PEDICU- LAR. See also perd-. [Pok. pezd- 829, 2. peis- 796.] peter-. Father. 1. Germanic *fadar in Old English feder (> Middle English fader), father: FATHER; FOREFATHER. 2. Latin pater, father (> patrare, to bring about): PADRE, PATER, PATERNAL, PATRI-, PATRICIAN, PATRIMONY, PA- TRON; EXPATRIATE, IMPETRATE, PERPETRATE. 3. Greek
### AHD ADDER/HEART?
14
### WLD Bd1 p.43 (leaf 51)
leaf 50                                                             
leaf 51                                     ,                       
                                    ,                                                          ati                                              43    Gr. vermutlich              in    uz-ag   „aber“       (vgl.      avxdo   aus avian   ;                                                                                             Brugmann GrGr. 3 87, 540, KYG. 616; bei Verbindung mit axeg, got. sundro bliebe der att. Lenis unerklart). Lat. at „aber“ aus steigernd-entgegensetzendem „daruber hinaus“, welch letztere Bed. in at-avus, at-nepos (vgl. Yf. LEWb. 2 66 f.  nicht in appnme. u. dgl., s. Skutseh AflL. 12, 213).        ;                                                               Gall, ate- (aus *ati-)      in     Ategnatus       (= mbret. (h)asnat          ,                                                                    nbret. anat „bekannt“),      u.   dgl., abret. Ate-cotti       ,                            air. aith -,   vortonig ad- ..wicder, ent-“, mcymr. at-, ncymr. ad-,       (Belege z. B. bei Fick II 4 8, Pedersen KG. II 292; kelt. *ati-            ed-            — „iiber hinaus“ und „zuriick, wieder“ mit Fick als urspriinglich verschie- dene Worte zu betrachten                    —                                    Bezzenberger stellt in ersterer Bed. An- knupfung an gr. nox'i, av. paiti zur Wahl                          —                                                    halte ich fur unbegriindet).     Got. ap-pan „aber, doch“ (sehr fraglich ist dagegen Herleitung von got. as. ah, ags. ac „aber“, ahd. oh „sondern, aber“ aus *ap-              he   gr. ye;     +     = anders, aber kaum zutreffend Holthausen IF. 17, 458              gr. dye, lat. age                                                                                :   = „geh! wohlan!“).
```


## [2026-09-05T20:47:57.801Z] AGENT

Now I'll write the verification file.


## [2026-09-05T20:56:21.809Z] TOOL CALL #81: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build162.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW_XWAR   = \"https://en.wiktionary.org/wiki/%D8%AE%D9%88%D8%A7%D8%B1\"\nW_DOSVAR = \"https://en.wiktionary.org/wiki/%D8%AF%D8%B4%D9%88%D8%A7%D8%B1\"\nW_ETI    = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81eti\"\nE_EDDY   = \"https://www.etymonline.com/word/eddy\"\nE_WANT   = \"https://www.etymonline.com/word/want\"\nE_WASTE  = \"https://www.etymonline.com/word/waste\"\nE_ETC    = \"https://www.etymonline.com/word/et%20cetera\"\nE_VAIN   = \"https://www.etymonline.com/word/vain\"\nW_VANG   = \"https://en.wiktionary.org/wiki/%D9%88%D9%86%DA%AF\"\n\ndoc = {\n \"pdf_page\": 162,\n \"book_page\": 132,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": []\n}\n\n# ---------------------------------------------------------------- entry 1: Eter\ne1 = {\n \"entry\": 1,\n \"root\": \"Ěter\",\n \"verdict\": \"plausible\",\n \"modern_form\": \"PIE *eter- 'entrails, intestines' (Pokorny 344 = Walde-Pokorny I 117); the Iranian attachment (Av. xᵛāθra- < *hu-āθra-) is Pokorny's own tentative suggestion\",\n \"note\": (\"Pokorny p.344 has the lemma exactly: 'Root/lemma: eter-, Meaning: intestines', built on Gk. ἦτορ 'heart' \"\n   \"(Aeolic for *etr̥), ἦτρον 'belly, lower abdomen', ON æðr 'vein', OE ǣdre, OHG ād(a)ra 'vein, sinew, pl. entrails', \"\n   \"OHG innuodili, OIr. inathar 'entrails'. The root and the language label are right; the gloss is not. Nourai's \"\n   \"'internal (INSIGNIFICANT) organs' is his own addition, inserted so that the Persian 'of low value' can fall out of \"\n   \"the root — no source glosses *eter- as 'insignificant'. The one Iranian link is the last line of Pokorny's article: \"\n   \"'from here Avestan xᵛāθra- \\\"moments of joy, cheerfulness, contentment\\\" as *su-atra-?' — offered with a question mark. \"\n   \"Modern Iranian etymology (Rastorgujeva–Edelʹman, ESIJa I 324, quoted by Wiktionary) takes MP xwār back to PIr *āθra- \"\n   \"and calls the further origin unknown, i.e. it neither adopts nor refutes Pokorny's *eter-. Watkins/AHD dropped the \"\n   \"root altogether (no *eter- in the 1985 appendix). Verdict: plausible — real root, real forms, over-tailored gloss, \"\n   \"and a weakly supported Iranian bridge. Two of the three references Nourai cites for the root do not check out \"\n   \"(see ref_check).\"),\n \"note_fa\": (\"ریشهٔ هندواروپایی آغازین *eter- به معنی «اندرونه، روده‌ها» در پوکورنی ص ۳۴۴ (و والده‑پوکورنی ج۱ ص ۱۱۷) واقعاً هست و \"\n   \"بر پایهٔ یونانی ἦτορ «دل»، ἦτρον «شکم»، نورس باستان æðr «رگ» و آلمانی علیای باستان ād(a)ra «رگ؛ جمع: احشا» بازسازی شده است. \"\n   \"امّا معنایی که نورایی می‌دهد — «اندام‌های درونی (کم‌ارزش)» — از آنِ خود اوست؛ هیچ منبعی واژهٔ «کم‌ارزش» را در معنای ریشه نیاورده \"\n   \"و پیداست که برای توجیه معنای فارسی «خوار» افزوده شده است. تنها پیوند ایرانی، جملهٔ پایانی مدخل پوکورنی است که با علامت پرسش \"\n   \"اوستایی xᵛāθra- «آسایش، خوشی» را از *su-atra- می‌گیرد. ریشه‌شناسی امروزی ایرانی (فرهنگ ریشه‌شناختی زبان‌های ایرانی، ج۱ ص ۳۲۴) \"\n   \"پایهٔ *āθra- را می‌پذیرد ولی خاستگاه دورتر آن را ناشناخته می‌داند؛ واتکینز نیز این ریشه را در فهرست خود نیاورده است. \"\n   \"پس: با احتیاط پذیرفتنی است.\"),\n \"sources\": [W_XWAR],\n \"ref_check\": [\n   {\"ref\": \"POK:344\", \"status\": \"supports\",\n    \"note\": \"POK_full.txt line 29467 ff.: 'Root / lemma: eter- | Meaning: intestines … from here Avestan xʷaθra- “moments of joy, cheerfulness, contentment” as *su-atra-? | References: WP. I 117 | Page(s): 344'. Page number exact.\"},\n   {\"ref\": \"IEC:1347\", \"status\": \"not_found\",\n    \"note\": \"Mann IEC p.1347 = leaf 738 of IEC.txt (calibrated: leaf 688 carries printed 1247, two printed pages per leaf) and holds 'suag-(1) evil / suagh- resound' — nothing to do with entrails. Grepping the whole of IEC.txt for a lemma 'eter-' / 'ētr̥' gives no hit (the one 'eter-' match, leaf 260, is the English word 'eter-nal' broken across a line). Mann appears to have no such lemma.\"},\n   {\"ref\": \"WLD1:264\", \"status\": \"not_found\",\n    \"note\": \"Walde-Pokorny Bd. I p.264 (WLD_Bd1_pages.txt leaf 272, printed number '264' at the head) is the article *u̥er- 'binden, reihen, aufhängen' — unrelated. The eter- article of WP is Bd. I p.117 (leaf 125): 'eter- „Eingeweide“. Gr. ἦτορ „Herz“ … anord. œdr f. „Ader“ … ahd. inuodili „Eingeweide“'. So the correct WP page is I 117, exactly as Pokorny himself cites it.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"p.344, lemma eter-\", \"stance\": \"supports\",\n    \"note\": \"'Meaning: intestines'; the Avestan line is added with a question mark ('as *su-atra-?').\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I p.117\", \"stance\": \"partial\",\n    \"note\": \"'eter- „Eingeweide“' with the Greek, Norse, German and Irish material only — the 1927 article has NO Avestan xᵛāθra-; Pokorny added that in 1959.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, IE roots appendix\", \"stance\": \"silent\",\n    \"note\": \"no lemma *eter-: the only 'eter-' strings in AHD_watkins1985.txt are 'dhugheter-' and 'peter-'. Watkins does not carry this root.\"},\n   {\"src\": \"IEC\", \"where\": \"searched whole file\", \"stance\": \"silent\",\n    \"note\": \"Mann has no eter-/ētr̥ lemma (see ref_check).\"}\n ],\n \"nodes\": []\n}\n\ne1[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Avestan\",\n \"words\": \"xv-âthra; duš-âthra; su-âthra\",\n \"verdict\": \"plausible\",\n \"derivation\": (\n   \"All three shapes are one and the same Avestan compound. Av. xᵛāθra- n. = xᵛ- (hu-) 'good' + āθra-, and duž-āθra- = \"\n   \"duš- 'bad' + āθra-; Nourai's 'su-âthra' is simply the Indic-looking spelling su- of the same prefix that appears as \"\n   \"Iranian hu-/xᵛ-, which is why he can only gloss it '?'. Pokorny 344 takes the *-āθra- element as the reflex of \"\n   \"*eter- 'entrails', so that *su-atra- is literally 'good-innards' > 'well-being' — the same figure as Latin viscera / \"\n   \"Greek σπλάγχνα for the seat of feeling. The GLOSSES on the chart are wrong: Bartholomae's Altiranisches Wörterbuch \"\n   \"gives xᵛāθra- 'Behagen, Glück, Wonne' (comfort, happiness) — see the compounds pouruš-xᵛāθra- 'der viel Behagen, \"\n   \"Glück, Wonne gewährt' and vīspa-xᵛāθra- 'der alles Behagen … besitzt und gewährt' — and duž-āθra- is its antonym \"\n   \"'discomfort, distress'. 'Insignificant, low in value' is New Persian semantics read back into Avestan: the road runs \"\n   \"'comfortable' > 'easy' > 'trifling' > 'of no worth', and Horn (no.496) states flatly that the sense 'niedrig, \"\n   \"verächtlich' is FIRST New Persian. So the node is right about the forms and about which Avestan words feed the \"\n   \"Persian pair, and wrong about what those Avestan words mean.\"),\n \"derivation_fa\": (\n   \"هر سه صورت در واقع یک واژه‌اند: اوستایی xᵛāθra- از پیشوند xᵛ-/hu- «خوب» + ستاک āθra-، و duž-āθra- از duš- «بد» + همان ستاک؛ \"\n   \"«su-āthra» هم صورت هندی‌نمای همان پیشوند hu- است و از همین رو نورایی معنایی برایش نیاورده. پوکورنی جزء دوم را بازماندهٔ ریشهٔ \"\n   \"*eter- «اندرونه» می‌داند، یعنی *hu-āθra- تحت‌اللفظ «خوش‌اندرون» و مجازاً «آسایش». امّا معنایی که در نمودار آمده درست نیست: \"\n   \"بارتولومه xᵛāθra- را «Behagen, Glück» (آسایش، خوشی) معنی کرده و آن را در ترکیب‌های pouruš-xᵛāθra- و vīspa-xᵛāθra- آورده است، \"\n   \"و duž-āθra- ضدّ آن است؛ معنی «کم‌ارزش، خوار» تحوّل معنایی متأخّرِ فارسی نو است — چنان‌که هرن (شمارهٔ ۴۹۶) صریحاً می‌گوید معنی \"\n   \"«پست و خوارشمرده» تنها در فارسی نو پیدا شده است. پس صورت‌ها و مسیر درست‌اند، ولی معنای اوستایی در کتاب نادرست است: \"\n   \"با احتیاط پذیرفتنی است.\"),\n \"sources\": [W_XWAR],\n \"ref_check\": [\n   {\"ref\": \"POK:344\", \"status\": \"supports\",\n    \"note\": \"Pokorny p.344, last line of the eter- article: 'from here Avestan xʷaθra- “moments of joy, cheerfulness, contentment” as *su-atra-?' — Nourai's arrow, but with Pokorny's question mark and with Pokorny's (correct) gloss 'joy, contentment', not 'insignificant'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"AiW s.vv. pouruš-xʷāθra-, vispa-xʷaθra-\", \"stance\": \"partial\",\n    \"note\": \"BRT.txt line 16318: 'j. pouruš-xʷāθra- Adj. (fem. ʺrā-) „der viel Behagen, Glück, Wonne gewährt“ … Pü.: pur xʷārīh'; line 24443: 'j. vispa-xʷaθra- Adj. „der alles Behagen, Glück, alle Wonne besitzt und gewährt“'. Bartholomae's gloss is 'comfort/joy', not 'insignificant'; the Pahlavi rendering xʷārīh in the same line confirms the Av. xʷāθra- ↔ MP xwār equation Nourai draws.\"},\n   {\"src\": \"HRN\", \"where\": \"no. 496, p.110 and no. 569, p.127\", \"stance\": \"supports\",\n    \"note\": \"'xʷār … aw. xʷāθra- (Geldner KZ 25,478; Darmesteter Ét. ir. II 189)' and 'dušxʷār, dušvār ‚schwierig‘ — aw. vergl. dužāθra-'. Same Avestan etyma as the chart.\"},\n   {\"src\": \"POK\", \"where\": \"p.344\", \"stance\": \"partial\",\n    \"note\": \"gives the etymon but flags it with '?' and glosses it 'moments of joy, cheerfulness, contentment'.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Pahlavi\",\n \"words\": \"xâr; dušxvâr\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n   \"Av. xᵛāθra- 'comfort' > MP xwār. The intervocalic -θr- of Old Iranian gives Middle Persian -hr-/-r- (cf. puθra- > \"\n   \"pus(ar), miθra- > Mihr), so *xwāθra- > xwā(h)r, whence MacKenzie's two entries side by side: 'xwār [hwl] light, easy; \"\n   \"mean, abject' with abstract xwārīh 'ease', and 'xwā(h)rīh [hw'(h)ryh, Man. xw'ryy] happiness, bliss' — the older \"\n   \"abstract still carrying the Avestan 'well-being'. Nyberg's glossary has 'xᵛārēh [hw'lyh] bliss, felicity, delight — \"\n   \"from ¹xᵛār' and 'a-xwārīh unhappiness'. For the negative: MP dušwār / duš-xwar 'difficult, disagreeable' (MacKenzie: \"\n   \"'dušwār [dwšw'l, Man. dwšw'r] difficult, disagreeable; ~īh difficulty, trouble'; 'duš-xwar = dušwār'), attested in \"\n   \"Book Pahlavi (Nyberg quotes hac hān dušxᵛār sahist 'by this he was much shocked'). One refinement of Nourai's arrow: \"\n   \"Horn no.569 says the Middle and New Persian forms are 'Neubildungen aus duš + xwār' — a fresh compound made on \"\n   \"Iranian soil from the living prefix duš- and xwār, not a phonetic continuation of Av. dužāθra-; the Avestan word is \"\n   \"the model, not the direct ancestor.\"),\n \"derivation_fa\": (\n   \"اوستایی xᵛāθra- «آسایش» در فارسی میانه به xwār بدل شده است؛ خوشهٔ -θr- ایرانی باستان در میانِ واکه در پهلوی به -hr-/-r- \"\n   \"دگرگون می‌شود (مانند puθra- > پسر، miθra- > مهر). مکنزی دو مدخل کنار هم دارد: «xwār سبک، آسان؛ پست، خوار» با نامِ مصدر xwārīh \"\n   \"«آسانی»، و «xwā(h)rīh شادکامی، خوشی» که هنوز معنی اوستایی را نگاه داشته است. نیبرگ نیز xᵛārēh «خوشی، شادکامی» را از ¹xᵛār \"\n   \"گرفته و a-xwārīh «ناخوشی» را آورده است. صورت منفی، پهلویِ dušwār / duš-xwar «سخت، دشوار» است (مکنزی؛ و نیبرگ شاهدِ hac hān \"\n   \"dušxᵛār sahist را می‌آورد). یک نکتهٔ اصلاحی: هرن (شمارهٔ ۵۶۹) صورت‌های پهلوی و فارسی را «ساخت تازه» از duš + xwār می‌داند، \"\n   \"نه دنبالهٔ آواییِ مستقیمِ اوستایی dužāθra-؛ یعنی واژهٔ اوستایی الگو بوده است نه نیای بی‌واسطه. ادعای نورایی درست است.\"),\n \"sources\": [W_XWAR, W_DOSVAR],\n \"ref_check\": [\n   {\"ref\": \"HRN:110\", \"status\": \"supports\",\n    \"note\": \"Horn no.496 (HRN.txt leaf 131, printed '— 110 —'): 'xʷār ‚leicht, gerade; niedrig, verächtlich‘ … aw. xʷāθra- …; phlv. xʷār, nur in der Bedeutung ‚leicht‘, xʷārīhā ‚leichtlich‘ (Salemann).'\"},\n   {\"ref\": \"HRN:127\", \"status\": \"partial\",\n    \"note\": \"Horn no.569 (leaf 148, printed '- 127 -'): 'dušxʷār, dušvār ‚schwierig‘ … phlv. dušxʷār, dušxʷārīh. Die neup. phlv. Formen sind Neubildungen aus duš + xʷār (No. 496).' Supports the form, but calls it a re-formation rather than a direct descendant of Av. dužāθra-.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie s.vv. xwār, xwā(h)rīh, dušwār\", \"stance\": \"supports\",\n    \"note\": \"'¹xwār [hwl | M xwr, N ~] light, easy; mean, abject. ~īh: ease; v. also xwā(h)rīh'; 'xwā(h)rīh [hwʼ(h)ryh | M xwʼryy] happiness, bliss'; 'dušwār [dwšwʼl | M dwšwʼr, N ~] difficult, disagreeable. ~īh: difficulty, trouble, misfortune'; 'duš-xwar [… | N ~] = dušwār'.\"},\n   {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II, glossary\", \"stance\": \"supports\",\n    \"note\": \"NYB_vol2_glossary.txt line 4332: 'xʷārēh [hwʼlyh] bliss, felicity, delight … From ¹xʷār; MPrs xwʼryy'; line 4342 'xʷār-mān … contemptible'; line 1760 quotes 'hac hān dušxʷār sahist'.\"},\n   {\"src\": \"HRN\", \"where\": \"nos. 496, 569\", \"stance\": \"supports\", \"note\": \"see ref_check.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Persian\",\n \"words\": \"xâr 1 «خوار»; došvâr «دشوار»\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n   \"MP xwār > NP خوار xᵛār/xār. In New Persian the word keeps 'easy, light' (archaic) and develops the dominant modern \"\n   \"sense 'contemptible, abject, of no worth' — Horn no.496 ends: 'Die Bedeutung \\\"niedrig, verächtlich\\\" ist erst \"\n   \"neupersisch'; Wiktionary (after Rastorgujeva–Edelʹman ESIJa I 324) lists exactly these two senses, '(archaic) easy' \"\n   \"and 'mean, abject', from MP xwār. MP dušxwār/dušwār > NP دشوار dušvār 'difficult'; the older دشخوار is still in the \"\n   \"dictionaries beside it (Borhān has both headwords, and Moʿin's Farhang cross-refers 'دشوار … دشخوار'), the -šxw- \"\n   \"cluster simplifying to -šv-. Ferdowsi already sets the pair against each other (Horn's footnote cites Šāhnāma I 170 \"\n   \"v.745, 'np. xᵛār directly opposed to dušxᵛār, as in the Avesta xᵛāθra- to dužāθra-'). Moʿin's etymological footnote \"\n   \"in Borhān-e Qāteʿ p.780 s.v. خوار reads 'اوستا xᵛāθra- (رفاه، آسایش) «خرده اوستا ۲۹۱»، پهلوی xᵛār، کردی xār، افغانی \"\n   \"xwār، بلوچی xwār، طبری xār (خوب)' — i.e. exactly Nourai's chain, but glossing the Avestan word 'welfare, ease'. \"\n   \"The box's own NOTE ('See root \\\"Xwâr\\\" for a different derivation') should be read the other way round: the \"\n   \"derivation drawn HERE is the mainstream one (Horn, Hübschmann, Moʿin, MacKenzie, ESIJa); the alternative under \"\n   \"Nourai's separate root Xwâr is the minority option.\"),\n \"derivation_fa\": (\n   \"فارسی میانهٔ xwār در فارسی نو «خوار» شده است: معنی کهن «آسان، سبک» است و معنی رایج امروزی «پست، بی‌ارزش، خوارشمرده» — \"\n   \"هرن در پایان شمارهٔ ۴۹۶ می‌نویسد که معنی «پست و خوار» تنها نوفارسی است، و ویکی‌واژه (به نقل از فرهنگ ریشه‌شناختی زبان‌های \"\n   \"ایرانی ج۱ ص ۳۲۴) همین دو معنی را از پهلویِ xwār می‌گیرد. «دشوار» از پهلویِ dušxwār/dušwār است و صورت کهن‌تر «دشخوار» هنوز در \"\n   \"فرهنگ‌ها کنار آن هست (برهان قاطع هر دو مدخل را دارد و معین در فرهنگ فارسی «دشوار … دشخوار» را برابر آورده)؛ خوشهٔ -شخو- به \"\n   \"-شو- ساده شده است. فردوسی نیز «خوار» را در برابر «دشوار» می‌نهد (شاهنامه ج۱ ص ۱۷۰ بیت ۷۴۵، به نقل هرن). حاشیهٔ ریشه‌شناختی \"\n   \"معین در برهان قاطع ص ۷۸۰ ذیل «خوار» همین زنجیره را می‌آورد: «اوستا xᵛāθra- (رفاه، آسایش)، پهلوی xᵛār، کردی xār، افغانی xwār، \"\n   \"بلوچی xwār، طبری xār». پس ادعای نورایی در این گره درست است؛ و یادداشت خودِ نمودار را باید وارونه خواند: آنچه اینجا رسم شده \"\n   \"همان ریشه‌شناسی پذیرفتهٔ همگانی است.\"),\n \"sources\": [W_XWAR, W_DOSVAR],\n \"ref_check\": [\n   {\"ref\": \"BQT:780\", \"status\": \"supports\",\n    \"note\": \"Borhān-e Qāteʿ p.780 (BQT_v2_pages.txt leaf 238; calibrated by leaf 240 whose header OCRs as ۷۸۲ and leaf 245 = ۷۸۷, so leaf+542 = printed page). Headword خوار with the sense 'ذلیل و بی‌اعتبار را گویند' and Moʿin's footnote 1: 'اوستا xʷāθra- (رفاه، آسایش) «خرده اوستا ۲۹۱»، پهلوی xʷār، کردی xār، افغانی xwār، بلوچی xwār، طبری xār (خوب)'; a further footnote glosses 'پهلوی xwār (بیهوده، ناچیز)'.\"},\n   {\"ref\": \"BQT:866\", \"status\": \"supports\",\n    \"note\": \"The دشوار headword with Moʿin's footnote 4 stands on leaf 327 of BQT_v2_pages.txt = printed p.869 by the same calibration (Nourai's 866 is ~3 pages out, or his Amir Kabir printing paginates slightly differently); the neighbouring leaf 326 (=868) carries دشخوار 'بروزن و معنی دشوار است که مشکل باشد'. Footnote 4 (OCR partly garbled) reads 'پهلوی duš-xwār … ارمنی … نزدیک به «دشخوار»، ایرانی باستانی *duš-…، ضد … رک: خوار، دشخوار' — the same chain the chart draws.\"},\n   {\"ref\": \"HRN:110\", \"status\": \"supports\",\n    \"note\": \"no.496: 'xʷār ‚leicht, gerade; niedrig, verächtlich‘ … Die Bedeutung ‚niedrig, verächtlich‘ ist erst neupersisch', with the footnote 'Sahn. I, 170 Vers 745 steht np. xʷār direkt im Gegensatz zu dušxʷār, wie im Awesta xʷāθra- zu dužāθra-'.\"},\n   {\"ref\": \"HRN:127\", \"status\": \"supports\",\n    \"note\": \"no.569: 'dušxʷār, dušvār ‚schwierig‘, dušxʷān, dušvan' — both New Persian variants.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BQT\", \"where\": \"pp.780 and ~869, Moʿin's footnotes\", \"stance\": \"supports\", \"note\": \"see ref_check.\"},\n   {\"src\": \"MON\", \"where\": \"Farhang-e Fārsi s.v. دشوار\", \"stance\": \"supports\",\n    \"note\": \"MON_part2.txt: 'دشوار: (ص‌مر. / امر.) سخت، صعب، مشکل؛ دشخوار؛ مق. آسان، سهل' — marked as a COMPOUND adjective and equated with دشخوار, matching Horn's duš + xwār analysis.\"},\n   {\"src\": \"PHD\", \"where\": \"s.vv. xwār, dušwār\", \"stance\": \"supports\", \"note\": \"the Middle Persian ancestors of both New Persian words, with the same two senses.\"},\n   {\"src\": \"HUB\", \"where\": \"Persische Studien, notes to Horn\", \"stance\": \"silent\",\n    \"note\": \"Hübschmann's addenda (HUB.txt leaf 115 = p.105) comment on Horn nos. 1083-1101; nothing on no.496/569, i.e. he lets Horn's xʷār etymology stand.\"},\n   {\"src\": \"Wiktionary\", \"where\": \"s.v. خوار (Persian, Etymology 1)\", \"stance\": \"partial\",\n    \"note\": \"'From Middle Persian (hwʼl /xʷār/), from Proto-Iranian *ātra- / *āθra- (“spirit, breath”), of unknown further origin' citing Rastorgujeva–Edelʹman, ESIJa I 324; senses '(archaic) easy' and 'mean, abject'. Confirms the Iranian chain, declines to go back to PIE *eter-.\"}\n ]\n})\ndoc[\"entries\"].append(e1)\n\n# ---------------------------------------------------------------- entry 3: Eti\ne3 = {\n \"entry\": 3,\n \"root\": \"Eti\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *éti (also written *h₁eti) 'beyond, over; and' (Pokorny 344; Watkins/AHD 'eti')\",\n \"note\": (\"Pokorny p.344: 'Root/lemma: eti | Meaning: out; further, etc.' with Skt. áti, Av. aiti-, OP atiy- 'over-, back-', \"\n   \"Gk. ἔτι, Gaul. eti, Lat. et / etiam, Goth. iþ and prefix id-, OE/OS ed-, ON ið-, OHG et-/it- 'again'. Watkins/AHD \"\n   \"prints the lemma with Nourai's exact wording: 'eti. Above, beyond. 1. Germanic *ith- in Old Norse idha, whirlpool: \"\n   \"EDDY. 2. Latin et, and (< “furthermore”): ET CETERA. [Pok. eti 344.]' — so the whole chart (root gloss, the two \"\n   \"branches, and the two English words) is copied straight out of the AHD appendix, and it is right. Modern handbooks \"\n   \"keep the root: De Vaan/Beekes/Derksen reconstruct *h₁eti (an old locative of *h₁et-), Ringe simply *éti, with \"\n   \"descendants PIE > PII *áti, Proto-Italic *et, Proto-Germanic *idi, Gk. ἔτι, PCelt. *eti, PBSl. *ati, Toch. B ate.\"),\n \"note_fa\": (\"ریشهٔ هندواروپایی آغازین *éti (یا *h₁eti) «فراتر، آن‌سوی؛ و» در پوکورنی ص ۳۴۴ آمده است با شواهد سنسکریت áti، اوستایی aiti-، \"\n   \"پارسی باستان atiy-، یونانی ἔτι، لاتینی et و etiam، گوتی iþ و پیشوند id-، انگلیسی باستان ed-، نورس باستان ið-. \"\n   \"معنایی که نورایی می‌دهد («بالا، فراتر») عیناً همان است که واتکینز در پیوستِ ریشه‌های هندواروپایی فرهنگ American Heritage \"\n   \"آورده، و هر دو شاخهٔ نمودار (لاتینی و ژرمنی) نیز از همان‌جاست. پژوهش امروزی (دِوان، بیکس، درکسن) آن را *h₁eti، صورتِ \"\n   \"حالت مکانیِ کهنِ *h₁et-، بازسازی می‌کند. ادعای نورایی درست است.\"),\n \"sources\": [W_ETI],\n \"ref_check\": [\n   {\"ref\": \"POK:344\", \"status\": \"supports\",\n    \"note\": \"POK_full.txt line 28794 ff.: 'Root / lemma: eti | Meaning: out; further, etc. | Material: Old Indic ati- … prefix ati (Avestan aiti-, Old pers. atiy-) “over-, back-” … gr. ἔτι … Latin et “and also” … Gothic iþ “but”, prefix id- … | References: WP. I 43 f., WH. I 421 f. | Page(s): 344'.\"},\n   {\"ref\": \"KLN:545\", \"status\": \"supports\",\n    \"note\": \"Klein 1966 p.544/545 (KLN_1966.txt leaf 296, printed number 544 on the leaf), s.v. 'et, conj. meaning “and”. — L.; cogn. with OI. āti, Avestic aiti, “over, beyond”, Gk. ἔτι “yet, still, besides, moreover”, Gaul. eti “also, moreover”, Goth. iþ “and, but, however”, OE., OS. ed-, ON. ið-, OHG. et-, it-, “again”. Cp. eddy.' — every element of Nourai's chart, including his Avestan gloss 'over, beyond' verbatim.\"}\n ],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. eti\", \"stance\": \"supports\",\n    \"note\": \"'eti. Above, beyond. 1. Germanic *ith- in Old Norse idha, whirlpool: EDDY. 2. Latin et, and (< “furthermore”): ET CETERA. [Pok. efi 344.]' — the source of Nourai's root gloss.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I p.43 f.\", \"stance\": \"supports\",\n    \"note\": \"WLD_Bd1_pages.txt leaf 51 (printed '43'), article 'ati': Lat. at 'aber' from 'darüber hinaus' with at-avus, at-nepos; Gaul. ate- (< *ati-), OIr. aith-/ad- 'wieder', Goth. aþ-þan; the Greek ἔτι material follows. This is the WP. I 43 f. that Pokorny cites.\"},\n   {\"src\": \"Wiktionary\", \"where\": \"Reconstruction:Proto-Indo-European/éti\", \"stance\": \"supports\",\n    \"note\": \"'*éti: beyond; over; and'; De Vaan (EDL p.195) derives it as an old locative of *h₁et-; descendants Proto-Indo-Iranian *áti, Proto-Italic *et, Proto-Germanic *idi, Gk. ἔτι, PCelt. *eti, PBSl. *ati.\"}\n ],\n \"nodes\": []\n}\n\ne3[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Avestan\", \"words\": \"aiti 1\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n   \"Av. aiti- is the Avestan continuant of PIE *éti, used as a preverb/prefix 'over, beyond, across' (Skt. áti is its \"\n   \"exact match). Kent's Old Persian lexicon, p.166, gives it under the Old Persian entry: 'ati-, prefix, \\\"beyond, \"\n   \"across\\\": Av. aiti, Skt. áti, Gk. ἔτι \\\"yet, longer\\\", Lt. et \\\"and\\\", pIE *eti'. Klein s.v. et likewise cites 'Avestic \"\n   \"aiti, \\\"over, beyond\\\"' — which is where Nourai's gloss comes from word for word. Phonologically PIE *e > Indo-Iranian \"\n   \"*a and the *-i is preserved; Avestan writes ai- for a- before a following palatal element, hence aiti beside Skt. áti. \"\n   \"The '1' in 'aiti 1' is Nourai's homograph number, distinguishing this particle from other aiti- entries in his book.\"),\n \"derivation_fa\": (\n   \"اوستایی aiti- بازماندهٔ همان *éti هندواروپایی است و در اوستا پیشوند/پیش‌فعلی است به معنی «از فرازِ، آن‌سوی، از میانِ»؛ \"\n   \"برابر دقیق آن در سنسکریت áti است. کنت در واژه‌نامهٔ پارسی باستان، ص ۱۶۶، ذیل ati- می‌نویسد: «ati-، پیشوند، \\\"beyond, across\\\": \"\n   \"اوستایی aiti، سنسکریت áti، یونانی ἔτι، لاتینی et، هندواروپایی *eti». کلاین نیز ذیل et همین «Avestic aiti \\\"over, beyond\\\"» را \"\n   \"آورده و معنایی که نورایی نوشته عیناً از اوست. از نظر آوایی *e هندواروپایی در هندوایرانی به a بدل می‌شود و -i پایانی می‌ماند. \"\n   \"ادعای نورایی درست است.\"),\n \"sources\": [W_ETI],\n \"ref_check\": [\n   {\"ref\": \"KLN:545\", \"status\": \"supports\",\n    \"note\": \"Klein s.v. et (p.544/545): 'cogn. with OI. āti, Avestic aiti, “over, beyond”' — Nourai's gloss verbatim.\"},\n   {\"ref\": \"KNT:166\", \"status\": \"supports\",\n    \"note\": \"Kent, Old Persian, Lexicon p.166 (KNT.txt leaf 187, page number 166 printed on the leaf): 'ati-, prefix, “beyond, across”: Av. aiti, Skt. áti, Gk. ἔτι “yet, longer”, Lt. et “and”, pIE *eti; with ay-, yam-. Cf. also atiy.'\"}\n ],\n \"consulted\": [\n   {\"src\": \"KNT\", \"where\": \"p.166\", \"stance\": \"supports\", \"note\": \"see ref_check; Kent expressly equates Av. aiti with Lat. et and PIE *eti.\"},\n   {\"src\": \"POK\", \"where\": \"p.344\", \"stance\": \"supports\",\n    \"note\": \"'prefix ati (Avestan aiti-, Old pers. atiy-) “over-, back-”'.\"},\n   {\"src\": \"BRT\", \"where\": \"AiW, searched\", \"stance\": \"silent\",\n    \"note\": \"The AiW article on the preverb aiti could not be located in BRT.txt: the OCR of Bartholomae's Avestan transliteration is too corrupt for a headword grep (xʷāθra- comes out as x''äi>ra, dužāθra- as duiä%ra); recorded as a failed lookup, not as a negative result.\"}\n ]\n})\n\ne3[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Old Persian\", \"words\": \"ati\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n   \"Old Persian ati-/atiy 'beyond, across', the direct cognate of Av. aiti and Skt. áti. Kent lists it exactly where \"\n   \"Nourai says (Lexicon p.166): 'ati-, prefix, \\\"beyond, across\\\" … pIE *eti; with ay-, yam-. Cf. also atiy.' It is \"\n   \"attested in the Bīsotūn inscription: ati- + ay- 'go beyond, go along' > atiyāiš (3sg. imperfect) at DB 3.73 \"\n   \"(Kent p.169); Kent adds under abiy that abiy is 'apparently doublet to atiy … possibly by contamination of *a \"\n   \"antevocalic and ati anteconsonantal in sandhi'. Nourai's gloss 'beyond' is Kent's.\"),\n \"derivation_fa\": (\n   \"پارسی باستان ati-/atiy «آن‌سوی، از فرازِ»، هم‌ریشهٔ مستقیم اوستایی aiti و سنسکریت áti. کنت در ص ۱۶۶ واژه‌نامهٔ خود دقیقاً همان‌جا \"\n   \"که نورایی نشانی داده می‌نویسد: «ati-، پیشوند، \\\"beyond, across\\\" … هندواروپایی *eti؛ با ay- و yam-. نیز بنگرید به atiy». \"\n   \"این پیشوند در سنگ‌نبشتهٔ بیستون گواه دارد: ati- + ay- «فراگذشتن» > atiyāiš (ماضی سادهٔ سوم‌شخص) در DB ۳٫۷۳. \"\n   \"معنایی که نورایی آورده همان معنای کنت است؛ ادعای نورایی درست است.\"),\n \"sources\": [W_ETI],\n \"ref_check\": [\n   {\"ref\": \"KNT:166\", \"status\": \"supports\",\n    \"note\": \"Kent p.166: 'ati-, prefix, “beyond, across”: Av. aiti, Skt. áti, Gk. ἔτι, Lt. et “and”, pIE *eti'; the finite attestation 'ati- + ay- “go beyond, go along”: atiyāiš imf. DB 3.73' stands on p.169.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KNT\", \"where\": \"Lexicon pp.166, 169\", \"stance\": \"supports\", \"note\": \"see ref_check.\"},\n   {\"src\": \"POK\", \"where\": \"p.344\", \"stance\": \"supports\", \"note\": \"'Old pers. atiy- “over-, back-”' listed with Av. aiti-.\"},\n   {\"src\": \"Wiktionary\", \"where\": \"Reconstruction:Proto-Indo-European/éti, descendants\", \"stance\": \"supports\",\n    \"note\": \"Proto-Indo-Iranian *áti is given as the regular Indo-Iranian outcome, whence the Old Iranian forms.\"}\n ]\n})\n\ne3[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Latin\", \"words\": \"et; et-cě-terî\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n   \"Latin et 'and' continues *éti; the semantic step is 'furthermore, moreover' > 'and', exactly as Pokorny puts it \"\n   \"('Latin et \\\"and also\\\", Paelignian Umbrian et, Latin etiam \\\"and, also, still\\\", Gaulish eti \\\"also, further\\\", \"\n   \"eti-c \\\"and also\\\" (*eti-kʷe)'). Klein's entry is the reference Nourai cites and says the same. Nourai's second item \"\n   \"'et-cě-terî' is the phrase et cētera analysed into its parts: et + cēterī, and cēterus is itself *ke-etero- = the \"\n   \"deictic particle *ke- (his cross-reference 'Ki 2') plus the comparative *etero- 'the other of two' (his 'I 2'). \"\n   \"Watkins agrees, filing ET CETERA under both eti and ko-: 'Preposed in *ke-etero- (*e-tero-, a second time, again; \"\n   \"see i-) in Latin cēterus (neuter plural cētera), the other part, that which remains: ET CETERA.' Etymonline: \"\n   \"'from Latin et cetera, literally \\\"and the others\\\", from et \\\"and\\\" + neuter plural of ceterus … from Proto-Italic \"\n   \"*ke-etero-'. The gloss ':and other things' is Klein's ('et cetera, \\\"and other things\\\"').\"),\n \"derivation_fa\": (\n   \"لاتینی et «و» دنبالهٔ همان *éti است؛ تحوّل معنایی از «افزون بر این، وانگهی» به «و» رفته است — چنان‌که پوکورنی می‌نویسد و \"\n   \"لاتینی etiam «و نیز» و گالی eti-c «و همچنین» (< *eti-kʷe) را نیز کنار آن می‌آورد. جزء دوم نمودار، «et-cě-terî»، همان عبارت \"\n   \"et cētera است که نورایی به اجزایش تجزیه کرده: et + cēterī، و خودِ cēterus از *ke-etero- است، یعنی جزء اشارهٔ *ke- (ارجاع او \"\n   \"به Ki 2) به‌اضافهٔ *etero- «آن دیگری از میان دو تا» (ارجاع او به I 2). واتکینز و اتیمانلاین همین تحلیل را دارند. \"\n   \"ادعای نورایی درست است.\"),\n \"sources\": [E_ETC, W_ETI],\n \"ref_check\": [\n   {\"ref\": \"KLN:545\", \"status\": \"supports\",\n    \"note\": \"Klein 1966 p.544/545: 'et, conj. meaning “and”. — L.; cogn. with OI. āti, Avestic aiti …' and, on the same leaf, 'et cetera, “and other things”. — L., fr. et, “and” (see et), and neut. of ceteri, “the others”, which is formed fr. I.-E. pron. pref. *ce-, “there; behold” (see he), and I.-E. *etero-, “the other”.' — both of Nourai's Latin items and both of his cross-references.\"}\n ],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Watkins s.vv. eti and ko-\", \"stance\": \"supports\",\n    \"note\": \"ET CETERA is listed under eti ('Latin et, and') and under ko- ('*ke-etero- … in Latin cēterus … ET CETERA'); the index line reads 'ETCETERA eti, ko-'.\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet\", \"stance\": \"supports\",\n    \"note\": \"Ernout-Meillet treat et as the inherited particle beside etiam; no rival etymology is offered.\"},\n   {\"src\": \"POK\", \"where\": \"p.344\", \"stance\": \"supports\",\n    \"note\": \"'Latin et “and also”, Paelignian Umbrian et ds.; Latin etiam “and, also, still”; gall. eti “also, further”, eti-c “and also” (*eti-kʷe)'.\"}\n ]\n})\n\ne3[\"nodes\"].append({\n \"id\": 4, \"lang\": \"English\", \"words\": \"et cetera\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n   \"English took the Latin phrase over unchanged in the early 15th century: 'et cetera, also etcetera, early 15c., from \"\n   \"Latin et cetera, literally \\\"and the others\\\"' (Etymonline), i.e. a learned Latinism of the scribal/legal register, \"\n   \"not an inherited word. The usual abbreviation before the 20th century was &c., now etc. Watkins files ET CETERA \"\n   \"under eti (and, for the second element, under ko-), which is exactly the arrow Nourai draws from his Latin box.\"),\n \"derivation_fa\": (\n   \"انگلیسی این عبارت لاتینی را در آغاز سدهٔ پانزدهم میلادی دست‌نخورده وام گرفته است: et cetera «و دیگر چیزها» (اتیمانلاین). \"\n   \"این یک وام‌واژهٔ فاضلانه از زبان دیوانی و حقوقی است، نه واژه‌ای موروثی؛ کوته‌نوشت رایج آن تا سدهٔ بیستم &c. بود و امروز etc. \"\n   \"واتکینز نیز ET CETERA را ذیل eti (و برای جزء دوم ذیل ko-) آورده است، یعنی دقیقاً همان پیکانی که نورایی کشیده. ادعای او درست است.\"),\n \"sources\": [E_ETC],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins 1985 s.v. eti: '… 2. Latin et, and (< “furthermore”): ET CETERA'; index 'ETCETERA eti, ko-'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"p.545 s.v. et cetera\", \"stance\": \"supports\",\n    \"note\": \"'et cetera, “and other things”. — L., fr. et, “and” … and neut. of ceteri, “the others”.'\"},\n   {\"src\": \"Etymonline\", \"where\": \"s.v. et cetera\", \"stance\": \"supports\",\n    \"note\": \"'also etcetera, early 15c., from Latin et cetera, literally “and the others” … The common form of the abbreviation before 20c. was &c., but etc. now prevails.'\"}\n ]\n})\n\ne3[\"nodes\"].append({\n \"id\": 5, \"lang\": \"Germanic\", \"words\": \"ith\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n   \"Nourai's 'ith' is the Germanic reflex of *éti as Klein and Watkins write it (*ith-), seen in Gothic iþ 'and, but, \"\n   \"however' and in the productive prefix Gothic id-, OE/OS ed-, ON ið-, OHG et-/it- 'again, back' (OE id-witan 'reproach', \"\n   \"OHG ita-, itwīz). The chart's four-part gloss 'back, again, water flowing back, whirlpool' is Klein's own wording at \"\n   \"eddy, where he explains ON iða as 'lit. meaning \\\"that which rebounds or flows back\\\", fr. ON pref. ið- \\\"again\\\"' — so \"\n   \"'water flowing back, whirlpool' is not a Germanic *ith- meaning but the meaning of the ON derivative iða; Nourai has \"\n   \"folded the derivative's sense into the base word. Modern reconstruction writes the base *idi/*idi- (Proto-Germanic), \"\n   \"with the noun ON iða f. 'eddy'. Etymonline: Old Norse iða 'whirlpool', from Proto-Germanic *ith- 'a second time, \"\n   \"again'. Substantively the node is right; only the gloss is compressed.\"),\n \"derivation_fa\": (\n   \"«ith» در نمودار همان بازماندهٔ ژرمنیِ *éti است، به همان صورتی که کلاین و واتکینز می‌نویسند (*ith-): گوتی iþ «و، امّا» و \"\n   \"پیشوند زایای گوتی id-، انگلیسی و ساکسونی باستان ed-، نورس باستان ið-، آلمانی علیای باستان et-/it- «باز، دوباره». \"\n   \"چهار معنایی که در نمودار آمده («back, again, water flowing back, whirlpool») عین عبارت کلاین ذیل eddy است، ولی دو معنی \"\n   \"آخر از آنِ مشتقِ نورس باستان iða «گرداب» است نه خودِ پایهٔ ژرمنی؛ نورایی معنای مشتق را در معنای پایه ادغام کرده است. \"\n   \"بازسازی امروزی، پایه را ژرمنی آغازین *idi می‌نویسد. جز همین فشردگیِ معنایی، ادعای نورایی درست است.\"),\n \"sources\": [E_EDDY, W_ETI],\n \"ref_check\": [\n   {\"ref\": \"KLN:545\", \"status\": \"supports\",\n    \"note\": \"Klein s.v. et: 'Goth. iþ “and, but, however”, OE., OS. ed-, ON. ið-, OHG. et-, it-, “again”. Cp. eddy.'; and s.v. eddy (leaf 272): 'ON. iða, “whirlpool”, lit. meaning “that which rebounds or flows back”, fr. ON. pref. ið-, “again” … cogn. with L. et, “and”. See et.' — the source of every word of Nourai's gloss.\"}\n ],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Watkins s.v. eti\", \"stance\": \"supports\",\n    \"note\": \"'1. Germanic *ith- in Old Norse idha, whirlpool: EDDY.'\"},\n   {\"src\": \"POK\", \"where\": \"p.344\", \"stance\": \"supports\",\n    \"note\": \"'Gothic iþ “but” … prefix id- in id-weit “disgrace” = Old English Old Saxon edwīt, Old High German ita-, itwīz … Old Norse ið- “again”, Old English Old Saxon ed- “again”'.\"},\n   {\"src\": \"Wiktionary\", \"where\": \"Reconstruction:Proto-Indo-European/éti, descendants\", \"stance\": \"partial\",\n    \"note\": \"gives 'Proto-Germanic: *idi, *idi-' rather than Klein's *ith-; same etymon, modern spelling.\"}\n ]\n})\n\ne3[\"nodes\"].append({\n \"id\": 6, \"lang\": \"English\", \"words\": \"eddy, eddy current\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n   \"Eddy: Middle English (Scottish) ydy, mid-15c., almost certainly from Old Norse iða 'whirlpool' — a Norse loan into \"\n   \"northern English/Scots, hence the initial e-/y- variation; Klein: 'eddy, n., whirlpool; current of air. — ME. ydy, \"\n   \"prob. fr. ON. iða, \\\"whirlpool\\\", lit. \\\"that which rebounds or flows back\\\"'. Etymonline says the same: 'mid-15c., \"\n   \"Scottish ydy, possibly related to Old Norse iða \\\"whirlpool,\\\" from Proto-Germanic *ith- \\\"a second time, again\\\"'. \"\n   \"'Eddy current' is not an old word but a 19th-century physics compound (the induced circulating currents in a \"\n   \"conductor, also called Foucault currents), formed inside English on eddy; Nourai lists it, as AHD-style lists do, \"\n   \"as a derivative rather than a separate etymon.\"),\n \"derivation_fa\": (\n   \"واژهٔ eddy «گرداب» در انگلیسی میانه (اسکاتلندی) ydy است، از میانهٔ سدهٔ پانزدهم، و به احتمال بسیار وام‌واژه‌ای است از \"\n   \"نورس باستان iða «گرداب» — وامی از زبان اسکاندیناویان در انگلیسیِ شمالی و اسکاتلندی. کلاین می‌نویسد: «ME. ydy، احتمالاً از \"\n   \"ON. iða، تحت‌اللفظ \\\"آنچه بازمی‌گردد یا واپس می‌رود\\\"». اتیمانلاین نیز همین را می‌آورد. ترکیب eddy current واژه‌ای کهن نیست، \"\n   \"بلکه اصطلاحی است در فیزیک سدهٔ نوزدهم (جریان‌های گردابی یا جریان فوکو) که در دلِ خودِ انگلیسی از eddy ساخته شده است. \"\n   \"ادعای نورایی درست است.\"),\n \"sources\": [E_EDDY],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins 1985 s.v. eti: 'Germanic *ith- in Old Norse idha, whirlpool: EDDY'; index line 'EDDY eti'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. eddy (KLN_1966 leaf 272)\", \"stance\": \"supports\",\n    \"note\": \"'eddy, n., whirlpool; current of air. — ME. ydy, prob. fr. ON. iða, “whirlpool” … rel. to OE., OS. ed-, OHG. et-, it-, Goth. iþ … cogn. with L. et, “and”. See et.'\"},\n   {\"src\": \"Etymonline\", \"where\": \"s.v. eddy (n.)\", \"stance\": \"supports\",\n    \"note\": \"'mid-15c., Scottish ydy, possibly related to Old Norse iða “whirlpool,” from Proto-Germanic *ith- “a second time, again,” which is related to the common Old English prefix ed- “again, backwards”.'\"}\n ]\n})\ndoc[\"entries\"].append(e3)\n\n# ---------------------------------------------------------------- entry 4: Eu 1\ne4 = {\n \"entry\": 4,\n \"root\": \"Eu 1, Ewân, Wâ\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *eu-1, *euə-, *wā-, *wə- 'to lack, be empty' (Pokorny 345-346; Watkins/AHD 'eu-2. Lacking, empty')\",\n \"note\": (\"Nourai's three-part root name reproduces Pokorny's lemma head exactly: 'Root/lemma: eu-1, euə-, u̯ā-, u̯ə- | \"\n   \"Meaning: to lack; empty | Page(s): 345-346'. 'Eu 1' is Pokorny's own numbering ('1. eu-'), 'Ewân' is the *euə-/\"\n   \"*(e)wā-n- shape (Klein prints the base as '*(e)wā-n-, \\\"to be empty, to lack\\\"'), and 'Wâ' is *u̯ā-. Watkins/AHD \"\n   \"renumbers it eu-2 but keeps the same extensions: 'eu-2. Lacking, empty. Extended forms *euə-, *wā-, *wə-. [Pok. 1. \"\n   \"eu- 345.]' The gloss 'to be empty' is right, and POK:345 is the right page. Everything on this chart except the \"\n   \"Persian box comes straight from the AHD appendix and checks out.\"),\n \"note_fa\": (\"نام سه‌بخشیِ ریشه در نمودار عیناً سرمدخل پوکورنی است: «eu-1, euə-, u̯ā-, u̯ə- : Mangel, mangeln, leer» در صفحات ۳۴۵–۳۴۶. \"\n   \"«Eu 1» شمارهٔ خودِ پوکورنی است، «Ewân» همان گونهٔ گستردهٔ *euə-/*(e)wā-n- است که کلاین آن را «*(e)wā-n- \\\"تهی بودن، کم داشتن\\\"» \"\n   \"می‌نویسد، و «Wâ» همان *u̯ā-. واتکینز آن را eu-2 شماره‌گذاری می‌کند ولی همان گسترش‌ها را می‌آورد. معنای «تهی بودن» و نشانی \"\n   \"پوکورنی ص ۳۴۵ هر دو درست‌اند و همهٔ شاخه‌های نمودار جز جعبهٔ فارسی از پیوستِ فرهنگ American Heritage آمده است. \"\n   \"ادعای نورایی درست است.\"),\n \"sources\": [E_VAIN],\n \"ref_check\": [\n   {\"ref\": \"POK:345\", \"status\": \"supports\",\n    \"note\": \"POK_full.txt line 28880 ff.: 'Root /lemma: eu-1, euə-, uā-, uə- | Meaning: to lack; empty | Note: esp. in partizipialen no-formations | Material: Old Indic ūna-, Avestan ūna- … npers. vang … Latin vānus … vaco, -are … Gothic wans … Latin vastus … | References: WP. I 108 f. | Page(s): 345-346'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. eu-2\", \"stance\": \"supports\",\n    \"note\": \"'eu-2. Lacking, empty. Extended forms *euə-, *wā-, *wə-. 1. Suffixed form *wo-no- in: a. Germanic *wanēn … WANE; b. North Germanic *wanatōn in Old Norse vanta, to lack: WANT. 2. Suffixed form *wā-no- in Latin vanus, empty: VAIN, VANITY, VAUNT; EVANESCE, VANISH. 3. Extended form *wak- in Latin vacāre … VACANT, VACATE, VACATION, VACUITY, VACUUM, VOID; AVOID, DEVOID, EVACUATE. 4. Extended and suffixed form *wās-to- in Latin vāstus, empty, waste: WASTE; DEVASTATE. [Pok. 1. eu- 345.]' — the whole chart in one paragraph.\"},\n   {\"src\": \"KLN\", \"where\": \"p.1687 s.v. vain\", \"stance\": \"supports\",\n    \"note\": \"'… fr. I.-E. base *(e)wā-n-, “to be empty, to lack”. Cp. vanish, vanity, vaunt, evanesce, evanish. Cp. also wan, want, wanton. Cp. also vacant.' — Nourai's 'Ewân'.\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.vv. uacō, uānus\", \"stance\": \"supports\",\n    \"note\": \"s.v. uacō: 'Tout ce qui comporte une étymologie, c'est le u- initial; en latin même, cf. uānus et uastus; hors du latin, cf. v.isl. vanr “manquant”, skr. ūna- = av. ūna- “qui manque de, incomplet”, arm. unayn “vide”, gr. εὖνις “privé de”, got. auþs “désert”, v.h.a. ōdi “vain”'; s.v. uānus: 'Pour l'étymologie, v. uacare et uastus'.\"}\n ],\n \"nodes\": []\n}\n\ne4[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Avestan\", \"words\": \"unâ, ŭna, uyamna\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n   \"The Avestan word is ūna- 'insufficient, deficient, scanty' (Bartholomae: 'ungenügend, mangelhaft', and 'geringfügig, \"\n   \"kärglich'), from zero-grade *uH-no-/*u-no- of the root, i.e. the same participial *-no- formation as Skt. ūná- \"\n   \"'wanting, less by', Gothic wans, Arm. unayn. Beside it stands the middle present participle uyamna- 'lacking' to a \"\n   \"present stem u-ya-, with the negated compound an-uyamna- 'not defective, complete' (Vr.15.1: 'uyamna anuyamnāiš daste' \"\n   \"— 'so that what is defective is made complete'). Nourai's three shapes are that pair plus, in 'unâ', the Sanskrit \"\n   \"match ūná- that Pokorny prints immediately before the Avestan form. Pokorny 345: 'Old Indic ūna-, Avestan ūna- \"\n   \"\\\"insufficient, inadequate, lack, be short of\\\", Avestan uyamna- ds. (participle present Med. to present u-ya-)'; \"\n   \"Klein p.1687 s.v. vain: 'cogn. with OI. ūnaḥ \\\"insufficient, wanting\\\", Avestic ūna-, \\\"wanting\\\"'.\"),\n \"derivation_fa\": (\n   \"واژهٔ اوستایی ūna- است به معنی «ناکافی، ناقص، اندک» — بارتولومه آن را «ungenügend, mangelhaft» و نیز «geringfügig, kärglich» \"\n   \"معنی می‌کند — از پایهٔ صفرِ ریشه با پسوند اسم مفعولیِ *-no-، درست همان ساختِ سنسکریت ūná- و گوتی wans و ارمنی unayn. \"\n   \"کنار آن صفت فاعلی میانهٔ uyamna- «کم‌داشته» از ستاک حال u-ya- می‌ایستد، با ترکیب منفیِ an-uyamna- «بی‌کاستی، تمام» \"\n   \"(ویسپرد ۱۵٫۱). سه صورتی که نورایی آورده همین جفت‌اند به‌اضافهٔ برابر سنسکریتِ ūná- که پوکورنی درست پیش از صورت اوستایی \"\n   \"می‌آورد. پوکورنی ص ۳۴۵ و کلاین ص ۱۶۸۷ (ذیل vain) هر دو همین را دارند. ادعای نورایی درست است.\"),\n \"sources\": [E_VAIN],\n \"ref_check\": [\n   {\"ref\": \"POK:345\", \"status\": \"supports\",\n    \"note\": \"Pokorny, lemma eu-1: 'Old Indic ūna-, Avestan ūna- “insufficient, inadequate, lack, be short of”, Avestan uyamna- ds. (participle present Med. to present u-ya-)'. Both of Nourai's Avestan forms, in his order.\"},\n   {\"ref\": \"KLN:1687\", \"status\": \"supports\",\n    \"note\": \"Klein 1966 p.1687 (KLN_1966.txt leaf 894; leaf 898 carries printed 1694-1695, so leaf 894 = pp.1686-1687), s.v. vain: 'L. vanus … which is cogn. with OI. ūnaḥ, “insufficient, wanting”, Avestic ūna-, “wanting”, Arm. unain, “empty”, Gk. εὖνις (for *eṰενις), “bereaved of”, fr. I.-E. base *(e)wā-n-, “to be empty, to lack”.'\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"AiW s.vv. ūna-, uyamna-, an-uyamna-\", \"stance\": \"supports\",\n    \"note\": \"BRT.txt line 23431: '1) PPM. ‚nicht ausreichend, ungenügend, mangelhaft‘: … uyamna anuyamnāiš daste „.. damit was mangelhaft ist, vollkommen gemacht werde“ Vr. 15.1; 2) PPfP.: a) ‚ungenügend‘: āfriti yā ūnəm pitum kərənaoiti … V.5.5; b) ‚geringfügig, kärglich‘: ūnəm F.9'; line 4515: 'j. an-uyamna- Adj. ‚nicht mangelhaft, vollkommen‘'.\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. uacō\", \"stance\": \"supports\",\n    \"note\": \"'skr. ūna- = av. ūna- “qui manque de, incomplète”' cited among the extra-Latin cognates of the uānus/uacō/uastus group.\"},\n   {\"src\": \"POK\", \"where\": \"p.345\", \"stance\": \"supports\", \"note\": \"see ref_check.\"}\n ]\n})\n\ne4[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Persian\", \"words\": \"vang 1 «وَنگ ۱»\",\n \"verdict\": \"plausible\",\n \"derivation\": (\n   \"The word itself is well attested: Borhān-e Qāteʿ p.2293 s.v. ونگ gives 'بمعنی تهی و خالی، و کنایه از تهی‌دستی باشد، و \"\n   \"درویش و گدا و مفلس را نیز گویند', and Moʿin's Farhang has the same two entries ('ونگ vang (ص.) تهی، خالی' / 'ونگ (ص.) \"\n   \"درویش، تهیدست، مفلس، سایل'). The ETYMOLOGY is the disputed part, and Nourai's own note is accurate. Horn no.1085 \"\n   \"(p.243) set up 'veng, ving \\\"leer; arm\\\"' beside Av. ūna-, Skt. ūná-, Arm. unain, Goth. wans, Gk. εὖνις, crediting the \"\n   \"idea to Nöldeke and himself refusing Nöldeke's further comparison with Latin vānus; Pokorny took it over and printed \"\n   \"'npers. (*gvang) vang \\\"empty, bare, lacking, poor, needy\\\"' on p.345 — note the starred *gvang, which shows he had to \"\n   \"posit an unattested initial to get New Persian v- out of PIE *u-. Hübschmann, Persische Studien p.105, commenting on \"\n   \"Horn's no.1085, says only 'Unsicher.' Moʿin's footnote to the Borhān entry repeats exactly this history — 'هرن veng, \"\n   \"ving را بمعنی خالی و فقیر ضبط کرده و وجه اشتقاقی برای آن نوشته است … ولی هوبشمان آنرا قطعی نمی‌داند' — and adds his own \"\n   \"verdict, 'درست بنظر نمی‌رسد' ('it does not look right'). The obstacles are that there is no Middle Persian *wang, that \"\n   \"NP و- from an Old Iranian vowel-initial *u- is irregular, and that Persian ونگ elsewhere is a noise word (= بانگ). \"\n   \"So: accepted by Horn and Pokorny, doubted by Hübschmann, rejected by Moʿin — 'plausible', and Nourai's flagging of \"\n   \"HUB:105 is exactly right.\"),\n \"derivation_fa\": (\n   \"خود واژه گواه روشن دارد: برهان قاطع ص ۲۲۹۳ ذیل «ونگ» می‌نویسد «بمعنی تهی و خالی، و کنایه از تهی‌دستی باشد، و درویش و گدا \"\n   \"و مفلس را نیز گویند»، و معین در فرهنگ فارسی همین دو مدخل را دارد. آنچه محل اختلاف است ریشه‌شناسی است و یادداشت خودِ نورایی \"\n   \"هم درست است. هرن (شمارهٔ ۱۰۸۵، ص ۲۴۳) veng/ving را کنار اوستایی ūna-، سنسکریت ūná-، ارمنی unayn، گوتی wans و یونانی εὖνις \"\n   \"نهاده و اشاره کرده که این هم‌سنجی را از نولدکه گرفته است، هرچند خودش هم‌سنجی نولدکه با لاتینی vānus را نمی‌پذیرد. \"\n   \"پوکورنی آن را در ص ۳۴۵ آورده، امّا به‌صورت «(*gvang) vang» — همین ستارهٔ *gvang نشان می‌دهد که برای بیرون آوردنِ «و»ی \"\n   \"فارسی از *u- هندواروپایی ناچار شده صورتی ناموجود فرض کند. هوبشمان در پژوهش‌های فارسی ص ۱۰۵، در حاشیهٔ شمارهٔ ۱۰۸۵ هرن، \"\n   \"تنها می‌نویسد «Unsicher» (نامطمئن). معین در حاشیهٔ برهان همین تاریخچه را می‌آورد و می‌افزاید «درست بنظر نمی‌رسد». \"\n   \"دشواری‌ها این است که در فارسی میانه *wang گواهی ندارد، «و»ی آغازینِ فارسی از *u- ایرانی باستان قاعده‌مند نیست، و «ونگ» \"\n   \"در فارسی جای دیگر واژه‌ای آوایی است (= بانگ). پس: با احتیاط پذیرفتنی است، و هشدارِ خودِ نورایی دربارهٔ هوبشمان بجاست.\"),\n \"sources\": [W_VANG],\n \"ref_check\": [\n   {\"ref\": \"POK:345\", \"status\": \"supports\",\n    \"note\": \"Pokorny, lemma eu-1: 'npers. (*gvang) vang “empty, bare, lacking, poor, needy”; pamir vanao ‚Leerheit, vanity, pride‘' — Nourai's Persian gloss verbatim; the parenthesised *gvang marks the phonological difficulty.\"},\n   {\"ref\": \"HRN:243\", \"status\": \"supports\",\n    \"note\": \"Horn no.1085 (HRN.txt leaf 264, printed '- 243 -'): 'veng, ving ‚leer; arm‘. aw. vergl. ūna- ‚leer, mangelnd‘; ai. ūná-; arm. unain ‚leer‘; got. wan ‚Mangel‘; gr. εὖνις ‚ermangelnd‘ … Die Anregung zu dieser Zusammenstellung verdanke ich Herrn Prof. Nöldeke, der lat. vanus vergleichen wollte, das mir aber (vergl. vācuus) nicht dazu zu gehören scheint.'\"},\n   {\"ref\": \"BQT:2293\", \"status\": \"supports\",\n    \"note\": \"Fetched with tools/ref_page.py BQT:2293 (BQT_v4 pdf p.376; cached at data/verification/sources/refs/ocr/BQT/2293.{png,txt}). Headword ونگ: 'بمعنی تهی و خالی و کنایه از تهی‌دستی باشد — و درویش و گدا و مفلس را نیز گویند'; Moʿin's footnote: 'هرن veng, ving را بمعنی خالی و فقیر ضبط کرده و وجه اشتقاقی برای آن نوشته است «اشتقاق ۱۰۸۵» ولی هوبشمان آنرا قطعی نمی‌داند «هوبشمان ۱۰۸۵»' followed by '* درست بنظر نمیرسد'. The Manṣūr Šīrāzī couplet the chart quotes is printed on the same page.\"}\n ],\n \"consulted\": [\n   {\"src\": \"HUB\", \"where\": \"Persische Studien p.105, note to Horn no.1085\", \"stance\": \"contradicts\",\n    \"note\": \"HUB.txt leaf 115, printed '— 105 —': '1085. Unsicher.' — Hübschmann's one-word rejection of Horn's etymology, exactly the doubt Nourai's NOTE points to.\"},\n   {\"src\": \"BQT\", \"where\": \"p.2293, Moʿin's footnote\", \"stance\": \"contradicts\",\n    \"note\": \"Moʿin closes the footnote 'درست بنظر نمیرسد' — he does not accept the Indo-European derivation, while confirming the word and its senses.\"},\n   {\"src\": \"MON\", \"where\": \"Farhang-e Fārsi s.v. ونگ\", \"stance\": \"partial\",\n    \"note\": \"'ونگ: vang (ص.) تهی، خالی' and 'ونگ: (ص.) درویش، تهیدست، مفلس، سایل' — confirms both senses of Nourai's gloss 'empty, poor'; Moʿin gives no etymology here, and separates the homonym 'ونگ [= بانگ، صدا]'.\"},\n   {\"src\": \"Wiktionary\", \"where\": \"s.v. ونگ\", \"stance\": \"silent\",\n    \"note\": \"The page has Mazanderani ونگ 'voice' (< MP wāng, PIE *wōkʷs) and Punjabi 'bangle', but NO Persian entry for vang 'empty, poor' — the word is not part of the modern Wiktionary/Hasandust material at all.\"}\n ]\n})\n\ne4[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Latin\", \"words\": \"vâstus; vacâre; vânus\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n   \"All three are the Latin members of the family as Watkins arranges them: vānus 'empty, vain' < suffixed *wā-no-; \"\n   \"vacāre 'to be empty' < extended *wak- (with the archaic doublet vocāre/vocuus that Plautus puns on); vāstus 'empty, \"\n   \"desolate' < extended and suffixed *wās-to-, whence vāstāre 'lay waste'. Ernout–Meillet make the same three-way link \"\n   \"twice over: s.v. uānus 'Pour l'étymologie, v. uacāre et uastus', and s.v. uacō 'en latin même, cf. uānus et uastus; \"\n   \"hors du latin, cf. v.isl. vanr \\\"manquant\\\", skr. ūna- = av. ūna- \\\"qui manque de, incomplet\\\", arm. unayn \\\"vide\\\", \"\n   \"gr. εὖνις'. Pokorny is more reserved than Nourai's 'AHD' source: he calls vānus 'perhaps here' and vacō 'very \"\n   \"dubious (because the k-extension is attested only in Italic)', while vāstus he treats as certainly related \"\n   \"(*u̯āsto-s, = OIr. fás 'empty', OHG wuosti 'waste'). Nourai follows AHD, which is the mainstream position.\"),\n \"derivation_fa\": (\n   \"هر سه واژه اعضای لاتینیِ همین خانواده‌اند، به همان ترتیبی که واتکینز آورده است: vānus «تهی، بیهوده» از *wā-no-؛ \"\n   \"vacāre «تهی بودن» از گونهٔ گستردهٔ *wak- (با گونهٔ کهنِ vocāre/vocuus که پلاوتوس با آن بازی می‌کند)؛ و vāstus «تهی، ویران» \"\n   \"از *wās-to- که vāstāre «ویران کردن» از آن است. ارنو و مِیه دو بار همین پیوند سه‌گانه را می‌آورند: ذیل uānus «برای ریشه‌شناسی \"\n   \"بنگرید به uacāre و uastus»، و ذیل uacō «در خودِ لاتینی uānus و uastus، و بیرون از لاتینی نورس باستان vanr، سنسکریت ūna- = \"\n   \"اوستایی ūna-، ارمنی unayn، یونانی εὖνις». پوکورنی محتاط‌تر است و vacō را «بسیار مشکوک» می‌داند چون گسترشِ -k تنها در \"\n   \"ایتالیایی باستان گواه دارد. نورایی از واتکینز پیروی کرده که دیدگاه رایج است؛ ادعای او درست است.\"),\n \"sources\": [E_VAIN, E_WASTE],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins 1985 s.v. eu-2, items 2-4: '*wā-no- in Latin vanus, empty: VAIN …; Extended form *wak- in Latin vacāre (variant vocāre), to be empty …; Extended and suffixed form *wās-to- in Latin vāstus, empty, waste (> vāstāre, to make desolate): WASTE; DEVASTATE.'\"}\n ],\n \"consulted\": [\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.vv. uānus, uacō\", \"stance\": \"supports\",\n    \"note\": \"'uānus, -a, -um: vide, dégarni … Pour l'étymologie, v. uacare et uastus'; and under uacō the list of cognates quoted above (v.isl. vanr, skr./av. ūna-, arm. unayn, gr. εὖνις, got. auþs).\"},\n   {\"src\": \"POK\", \"where\": \"pp.345-346\", \"stance\": \"partial\",\n    \"note\": \"'perhaps here Latin vānus “bare, lacking, containing nothing, empty”; very dubious (because the k-extension is attested only in Ital.) vaco, -are …; cognitional seems uāsto-s “deserted” in: Latin vastus … = Old Irish fás … Old High German wuosti'. Same three words, with reservations AHD does not print.\"},\n   {\"src\": \"KLN\", \"where\": \"p.1687 s.v. vain\", \"stance\": \"supports\",\n    \"note\": \"'Cp. vanish, vanity, vaunt, evanesce, evanish. Cp. also wan, want, wanton. Cp. also vacant.' — Klein links the vānus and vacāre groups under the same base.\"}\n ]\n})\n\ne4[\"nodes\"].append({\n \"id\": 4, \"lang\": \"English\", \"words\": \"waste; vacate, vacuum, vacation, void, avoid; vain, vanity, vanish\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n   \"Exactly Watkins's list of English reflexes under eu-2. Routes: (a) WASTE is not a direct Latin borrowing — Latin \"\n   \"vāstāre/vāstus passed into Gallo-Romance and was altered under Frankish *wōstjan to Old North French / Anglo-French \"\n   \"wast(e), waster (central Old French gaster, Modern French gâter), whence Middle English wasten c.1200 'devastate, \"\n   \"ravage'; the initial w- is the Germanic-influenced Norman form (Etymonline). (b) vacāre gives vacate (1640s, from \"\n   \"vacātus), vacuum (1550s, Latin neuter of vacuus), vacation (late 14c. via Old French), and, through Vulgar Latin \"\n   \"*vocitus > Old French voide/vuide, void and its compound avoid (Anglo-French avoider 'to empty out'). (c) vānus \"\n   \"gives vain (c.1300, Old French vain), vanity (c.1200, Old French vanité < Latin vānitātem), and vanish (early 14c., \"\n   \"Old French esvanir < Vulgar Latin *exvānīre for Latin ēvānēscere). All three sub-lists are Watkins's, unchanged.\"),\n \"derivation_fa\": (\n   \"این فهرست عیناً همان بازتاب‌های انگلیسیِ ریشه است که واتکینز ذیل eu-2 آورده. مسیرها: الف) waste وام مستقیم از لاتینی نیست؛ \"\n   \"لاتینی vāstāre/vāstus در رومانسِ گُل به waster/wast(e) در فرانسویِ شمالی و انگلونورمن بدل شد (با تأثیر فرانکیِ *wōstjan؛ \"\n   \"در فرانسویِ مرکزی gaster و امروز gâter) و از آنجا در انگلیسی میانه wasten «ویران کردن» شد؛ «و»ی آغازین نشانهٔ همان صورتِ \"\n   \"نورمن است. ب) vacāre واژه‌های vacate، vacuum، vacation و — از راه لاتینی عامیانهٔ *vocitus > فرانسوی باستان voide — \"\n   \"void و ترکیب avoid را داده است. ج) vānus واژه‌های vain، vanity (از فرانسوی باستان vanité) و vanish (از فرانسوی باستان \"\n   \"esvanir، از لاتینی عامیانهٔ *exvānīre به‌جای ēvānēscere) را داده است. ادعای نورایی درست است.\"),\n \"sources\": [E_WASTE, E_VAIN],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins 1985 s.v. eu-2 lists VAIN, VANITY, VAUNT, EVANESCE, VANISH; VACANT, VACATE, VACATION, (VACUITY), VACUUM, VOID, (AVOID), (DEVOID), EVACUATE; WASTE, DEVASTATE — every word of Nourai's three lines.\"}\n ],\n \"consulted\": [\n   {\"src\": \"Etymonline\", \"where\": \"s.v. waste (v./n.)\", \"stance\": \"partial\",\n    \"note\": \"'from Anglo-French and Old North French waster “to waste, squander, spoil, ruin” (Old French gaster), altered (by influence of Frankish *wostjan) from Latin vastare “lay waste,” from vastus “empty, desolate” … reconstructed in Watkins to be from a suffixed form of PIE root *eue-' — same root, but the chart's direct Latin→English arrow hides an Old North French stage.\"},\n   {\"src\": \"KLN\", \"where\": \"p.1687 s.v. vain\", \"stance\": \"supports\",\n    \"note\": \"'vain, adj. — ME. vaine, vain, vāyn, veyn, fr. OF. vain, vein (F. vain), fr. L. vanus … Cp. vanish, vanity, vaunt, evanesce, evanish … Cp. also vacant.'\"},\n   {\"src\": \"Etymonline\", \"where\": \"s.v. vain\", \"stance\": \"supports\",\n    \"note\": \"the vain / vanity / vanish group is traced to Latin vānus via Old French, under PIE root *eue- 'to leave, abandon, give out'.\"}\n ]\n})\n\ne4[\"nodes\"].append({\n \"id\": 5, \"lang\": \"Germanic\", \"words\": \"wanatôn\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n   \"Nourai's 'wanatôn' is Watkins's North Germanic *wanatōn 'to lack', a denominative verb built on the Germanic \"\n   \"adjective *wanaz 'lacking' (Gothic wans, ON vanr, OE/OS/OFris. wan, OHG wan), itself the *wo-no-/*u-ono- form of the \"\n   \"root — Pokorny 345: 'Gothic (*gwans) wans \\\"lacking, missing, wanting\\\" (*u-ono-s or *uə-no-s); Old Icelandic van-r, \"\n   \"Old Frisian Old English Old Saxon Old High German wan ds.' Beside *wanatōn stands *wanēn (OE wanian 'to lessen' > \"\n   \"WANE). Skeat states the derivational relation plainly: 'The Icel. vanr = A.S. wan; see Wane. Der. want, vb., Icel. \"\n   \"vanta, from the adj. vanr.'\"),\n \"derivation_fa\": (\n   \"«wanatôn» در نمودار همان *wanatōn ژرمنیِ شمالی است در فهرست واتکینز، فعلی مشتق از صفت ژرمنی *wanaz «کم‌داشته» \"\n   \"(گوتی wans، نورس باستان vanr، انگلیسی و ساکسونی باستان wan، آلمانی علیای باستان wan) که خود صورت *wo-no-/*u-ono- ریشه است — \"\n   \"پوکورنی ص ۳۴۵: «گوتی wans \\\"کم، ناقص\\\" (*u-ono-s یا *uə-no-s)؛ ایسلندی باستان van-r؛ فریزی، انگلیسی، ساکسونی و آلمانیِ \"\n   \"باستان wan». در کنار *wanatōn صورت *wanēn می‌ایستد (انگلیسی باستان wanian «کاستن» > wane). اسکیت این نسبت را روشن بیان \"\n   \"می‌کند. ادعای نورایی درست است.\"),\n \"sources\": [E_WANT],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins 1985 s.v. eu-2, 1b: 'North Germanic *wanatōn in Old Norse vanta, to lack: WANT' (and 1a: 'Germanic *wanēn in Old English wanian, to lessen, and wana, lack: WANE').\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"p.345\", \"stance\": \"supports\",\n    \"note\": \"'Gothic (*gwans) wans “lacking, missing, wanting” (*u-ono-s or *uə-no-s). Old Icelandic van-r. Old Frisian Old English Old Saxon Old High German wan ds.'\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. want\", \"stance\": \"supports\",\n    \"note\": \"SKT.txt line 21184: 'want; lack. (Scand.) M.E. want, first used as an adj., signifying “deficient.” — Icel. vant, neut. of vanr, adj. lacking … The Icel. vanr = A.S. wan; see Wane. Der. want, vb., Icel. vanta, from the adj. vanr.'\"},\n   {\"src\": \"KLN\", \"where\": \"p.1687 s.v. vain\", \"stance\": \"supports\",\n    \"note\": \"'Cp. also wan, want, wanton' — Klein files the Germanic group under the same base *(e)wā-n-.\"}\n ]\n})\n\ne4[\"nodes\"].append({\n \"id\": 6, \"lang\": \"English\", \"words\": \"want\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n   \"English want is a Norse loan of the Scandinavian settlement period, first recorded c.1200 as wanten 'be lacking, be \"\n   \"deficient in something', from Old Norse vanta 'to lack' (earlier *wanaton), i.e. it did not descend through Old \"\n   \"English but was borrowed from Old Norse — which is why it has no Old English ancestor beside cognate wanian 'to \"\n   \"diminish' (> wane). The modern dominant sense 'desire, wish for, feel the need of' is a late semantic shift, first \"\n   \"recorded 1706 (Etymonline); the noun want 'deficiency' is equally c.1200, matching ON vant, neuter of vanr. Skeat's \"\n   \"entry gives the same route from the Icelandic adjective vanr.\"),\n \"derivation_fa\": (\n   \"واژهٔ want در انگلیسی وام‌واژه‌ای است از دورهٔ اسکان اسکاندیناویان: نخستین‌بار حدود سال ۱۲۰۰ به صورت wanten «کم داشتن، \"\n   \"بی‌بهره بودن» ثبت شده، از نورس باستان vanta «کم داشتن» (کهن‌تر *wanaton). یعنی از راه انگلیسی باستان به ارث نرسیده بلکه \"\n   \"وام گرفته شده است — و به همین سبب نیای انگلیسی باستانی ندارد، در حالی که هم‌ریشهٔ آن wanian «کاستن» (> wane) بومی است. \"\n   \"معنای رایج امروزی، «خواستن، آرزو کردن»، تحوّلی متأخّر است و نخستین گواهِ آن به سال ۱۷۰۶ می‌رسد (اتیمانلاین). \"\n   \"ادعای نورایی درست است.\"),\n \"sources\": [E_WANT],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins 1985 s.v. eu-2: 'North Germanic *wanatōn in Old Norse vanta, to lack: WANT.'\"}\n ],\n \"consulted\": [\n   {\"src\": \"Etymonline\", \"where\": \"s.v. want (v.) and (n.)\", \"stance\": \"supports\",\n    \"note\": \"'c. 1200, wanten, “be lacking, be deficient in something,” from Old Norse vanta “to lack, want,” earlier *wanaton, from Proto-Germanic *wanen, from PIE *weno-, suffixed form of root *eue- “to leave, abandon, give out.” The meaning “desire, wish for, feel the need of” is recorded by 1706.'\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. want\", \"stance\": \"supports\",\n    \"note\": \"'M.E. want, first used as an adj., signifying “deficient” — Icel. vant, neut. of vanr … Der. want, vb., Icel. vanta, from the adj. vanr.'\"},\n   {\"src\": \"KLN\", \"where\": \"p.1687 s.v. vain\", \"stance\": \"supports\", \"note\": \"'Cp. also wan, want, wanton.'\"}\n ]\n})\ndoc[\"entries\"].append(e4)\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-162.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(doc, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build162.py"
}
```


### [2026-09-05T20:56:25.276Z] TOOL RESULT

```
written
```


## [2026-09-05T20:56:29.839Z] TOOL CALL #82: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-162.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 162"
}
```


### [2026-09-05T20:57:40.196Z] TOOL RESULT

```
JSON OK
nodes verified: 15/15
node verdicts: {'plausible': 2, 'confirmed': 13}
root verdicts: {'plausible': 1, 'confirmed': 2}
ref checks: {'supports': 22, 'partial': 1}
books consulted: {'partial': 7, 'supports': 34, 'silent': 3, 'contradicts': 2} | by book: {'POK': 8, 'KLN': 6, 'Etymonline': 5, 'Wiktionary': 4, 'BRT': 3, 'LAT': 3, 'HRN': 2, 'PHD': 2, 'BQT': 2, 'MON': 2, 'HUB': 2, 'KNT': 2, 'AHD': 2, 'SKT': 2, 'NYB': 1}
```


## [2026-09-05T20:57:48.929Z] TOOL CALL #83: Bash

```json
{
 "command": "git status --short && ls -la data/verification/page-162.json"
}
```


### [2026-09-05T20:57:48.983Z] TOOL RESULT

```
 M data/verification/sources/web/index.jsonl
?? data/verification/page-160.json
?? data/verification/page-162.json
?? data/verification/page-167.json
?? data/verification/page-168.json
?? data/verification/page-169.json
?? data/verification/sources/web/22c76f83bf215783.txt
?? data/verification/sources/web/2ddf9c6993d93db0.txt
?? data/verification/sources/web/5736e12792dac7d1.txt
?? data/verification/sources/web/73ea4e8361760e6b.txt
?? data/verification/sources/web/7a5e4d0e5bd08859.txt
?? data/verification/sources/web/7e367c5ffe187829.txt
?? data/verification/sources/web/80769e8c581fae19.txt
?? data/verification/sources/web/951a94220d6afd77.txt
?? data/verification/sources/web/99bbef29106cbf1f.txt
?? data/verification/sources/web/bbb1b1eabacbfdce.txt
?? data/verification/sources/web/dfddd5bfa2c86a44.txt
?? data/verification/sources/web/eea1f80007727136.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 73613 Sep  5 16:56 data/verification/page-162.json
```


## [2026-09-05T20:58:07.677Z] AGENT

Page 162 (book p. 132) verified — `data/verification/page-162.json` written, `verify_check.py 162` reports 0 PROBLEM lines.

**Counts** — 3 entries (2 redirects skipped), 15/15 nodes.
- Node verdicts: confirmed 13, plausible 2
- Root verdicts: confirmed 2 (Eti, Eu 1), plausible 1 (Ěter)
- Node ref-checks: supports 22, partial 1 (+2 root-level `not_found`, below)
- Consulted: 46 lookups across POK, WLD, AHD/Watkins, IEC, KLN, SKT, LAT (Ernout–Meillet), BRT, KNT, PHD, NYB, HRN, HUB, BQT, MON, Etymonline, Wiktionary

**Plausible (not disputed, but flagged)**
- Ěter (root) — PIE *eter- "intestines" is real (POK 344 = WP I 117), but Nourai's gloss "internal *(insignificant)* organs" is his own addition, tailored to the Persian sense. The Iranian bridge is only Pokorny's own question-marked last line ("Av. xᵛāθra- as *su-atra-?"); Watkins dropped the root, and ESIJa I 324 calls the further origin of MP xwār unknown.
- Ěter #1 Avestan xv-âthra / duš-âthra / su-âthra — forms right (su-/hu-/xᵛ- are one prefix), glosses wrong: Bartholomae has xᵛāθra- "Behagen, Glück" (comfort), dužāθra- its antonym. "Insignificant, low in value" is New Persian meaning read back; Horn 496 says explicitly that sense "ist erst neupersisch".
- Eu 1 #2 Persian vang «وَنگ» — Nourai's own note is accurate and understated: Horn 1085 + Pokorny 345 accept it (Pokorny only via a starred *gvang), Hübschmann p.105 says "Unsicher.", and Moʿin's footnote in Borhān 2293 ends "درست بنظر نمی‌رسد". Word and senses confirmed; etymology accepted by some, rejected by others.

**Bad citations by Nourai (root Ěter)** — neither is an extraction error; the page prints them:
- `IEC:1347` → Mann p.1347 is "suag-/suagh-"; Mann has no *eter- lemma. `not_found`
- `WLD1:264` → WP I 264 is *u̯er- "bind, hang"; the eter- article is WP **I 117**. `not_found`
- Minor: `BQT:866` (došvār) lands on p. 869 in the archive scan (BQT:780 for خوار is exact).

**Extraction error for the owner to fix** (entry 4, node 2 `quote.text`): the printed page reads `ذکات گنج عطای تراست قارون ونگ`; the JSON has `زکات گنج عطای قارون ونگ` — "تراست" dropped, and ذ→ز silently corrected (Borhān itself prints زکات, so the ذ is the book's misprint). No node verdict depends on it.
