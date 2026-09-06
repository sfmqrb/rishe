# Verification process log — verify-page-227


## [2026-09-06T15:20:46.370Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 227 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-227.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-227.json. Write /home/sfmqrb/git/rishe/data/verification/page-227.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 227` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T15:20:48.010Z] AGENT

I'll start by reading the agent instructions.


## [2026-09-06T15:20:48.720Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T15:20:48.736Z] TOOL RESULT

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


## [2026-09-06T15:20:49.094Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-227.txt"
}
```


### [2026-09-06T15:20:49.107Z] TOOL RESULT

```
1	=== PDF page 227 (book page 197) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Isto : a suffix meaning most or last  (refs KLN:35)
4	#1 (parent #0) [Avestan / Old Persian] refs=KNT:191,202 | išta : a superlative suffix
5	  #2 (parent #1) [Avestan] refs=KNT:202; TZF:26; BQT:2133 | aša-vah-išta, arta-vah-išta : best justice ☞Ar ; vah-išta : best place, heaven ☞Su 1 ; zôižd-išta : most abominable, ugly ☞Gheis ; tanj-išta : most pulled together, tight ☞Tenk
6	    #3 (parent #2) [Persian] refs=MON; BQT; TZF | Ordîbehešt «اردیبهشت» : "best justice" ; behešt «بهشت» : "best place" ; zešt «زشت» : ugly ; tang «تَنگ ( تنگنا ، تنگه )» : tight
7	  #4 (parent #1) [Avestan] refs=KNT:202; TZF:26; BQT:2133 | nazd-išta : closest, first ☞Sed ; frâ-išta : most plentiful ☞Pel 1 ; mas-išta, math-išta, maz-išta : greatest ☞Mâk,Meg ; kas-išta : least ☞Kak 3
8	    #5 (parent #4) [Persian] refs=MON; BQT; TZF | naxost «نخست ( نزدیک )» : "closest", first ; farhast «فَرهَست» : too much, magic ; mehast «مِهَست» : greatest ; kâst «کاست» : least, deficiency, lacking
9	  #6 (parent #1) [Avestan] refs=BQT; KNT:191; POK:775 | spenta-išta : holiest ☞Kwen ; duva-išta : furthest away ☞Deu 2 ; druw-išta : healthiest ☞Deru 1 ; âs-išto : fastest ☞Ôku ; sra-ěšta : most beautiful, best ☞Krei
10	    #7 (parent #6) [None] refs=None | 
11	  #8 (parent #1) [Germanic] refs=KLN:543; AHD:448 | istaz, isto
12	    #9 (parent #8) [Old English] refs=KLN:1007; AHD:126 | -est, -ost ; lat-est : latest, last ; bet-est : best ; maě-st : most ; fyr-st : first
13	      #10 (parent #9) [English] refs=AHD; KLN | -est ; last ; best ; most ; first
14	--- entry 1 ---
15	ROOT Iu -> redirect to Yu
16	
```


## [2026-09-06T15:20:52.088Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/extracted/batch/page-227.json",
 "description": "Read source JSON for page 227"
}
```


### [2026-09-06T15:20:52.125Z] TOOL RESULT

```
{
  "pdf_page": 227,
  "book_page": 197,
  "entries": [
    {
      "root": {
        "name": "Isto",
        "lang": "Indo-European",
        "refs": "KLN:35",
        "gloss": "a suffix meaning most or last"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "KNT:191,202",
          "words": [
            {"translit": "išta", "gloss": "a superlative suffix", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Avestan",
          "refs": "KNT:202; TZF:26; BQT:2133",
          "words": [
            {"translit": "aša-vah-išta, arta-vah-išta", "gloss": "best justice", "script": null, "see": ["Ar"]},
            {"translit": "vah-išta", "gloss": "best place, heaven", "script": null, "see": ["Su 1"]},
            {"translit": "zôižd-išta", "gloss": "most abominable, ugly", "script": null, "see": ["Gheis"]},
            {"translit": "tanj-išta", "gloss": "most pulled together, tight", "script": null, "see": ["Tenk"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "MON; BQT; TZF",
          "words": [
            {"translit": "Ordîbehešt", "gloss": "\"best justice\"", "script": "اردیبهشت"},
            {"translit": "behešt", "gloss": "\"best place\"", "script": "بهشت"},
            {"translit": "zešt", "gloss": "ugly", "script": "زشت"},
            {"translit": "tang", "gloss": "tight", "script": "تَنگ ( تنگنا ، تنگه )"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 1,
          "lang": "Avestan",
          "refs": "KNT:202; TZF:26; BQT:2133",
          "words": [
            {"translit": "nazd-išta", "gloss": "closest, first", "script": null, "see": ["Sed"]},
            {"translit": "frâ-išta", "gloss": "most plentiful", "script": null, "see": ["Pel 1"]},
            {"translit": "mas-išta, math-išta, maz-išta", "gloss": "greatest", "script": null, "see": ["Mâk", "Meg"]},
            {"translit": "kas-išta", "gloss": "least", "script": null, "see": ["Kak 3"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "MON; BQT; TZF",
          "words": [
            {"translit": "naxost", "gloss": "\"closest\", first", "script": "نخست ( نزدیک )"},
            {"translit": "farhast", "gloss": "too much, magic", "script": "فَرهَست"},
            {"translit": "mehast", "gloss": "greatest", "script": "مِهَست"},
            {"translit": "kâst", "gloss": "least, deficiency, lacking", "script": "کاست"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "نیست را هست کند تنبل اوی - هست را نیست کند فرهستش",
            "poet": "Abŭ-Nasr Marghzî"
          }
        },
        {
          "id": 6,
          "parent": 1,
          "lang": "Avestan",
          "refs": "BQT; KNT:191; POK:775",
          "words": [
            {"translit": "spenta-išta", "gloss": "holiest", "script": null, "see": ["Kwen"]},
            {"translit": "duva-išta", "gloss": "furthest away", "script": null, "see": ["Deu 2"]},
            {"translit": "druw-išta", "gloss": "healthiest", "script": null, "see": ["Deru 1"]},
            {"translit": "âs-išto", "gloss": "fastest", "script": null, "see": ["Ôku"]},
            {"translit": "sra-ěšta", "gloss": "most beautiful, best", "script": null, "see": ["Krei"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": null,
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 1,
          "lang": "Germanic",
          "refs": "KLN:543; AHD:448",
          "words": [
            {"translit": "istaz, isto", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Old English",
          "refs": "KLN:1007; AHD:126",
          "words": [
            {"translit": "-est, -ost", "gloss": null, "script": null},
            {"translit": "lat-est", "gloss": "latest, last", "script": null},
            {"translit": "bet-est", "gloss": "best", "script": null},
            {"translit": "maě-st", "gloss": "most", "script": null},
            {"translit": "fyr-st", "gloss": "first", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "English",
          "refs": "AHD; KLN",
          "words": [
            {"translit": "-est", "gloss": null, "script": null},
            {"translit": "last", "gloss": null, "script": null},
            {"translit": "best", "gloss": null, "script": null},
            {"translit": "most", "gloss": null, "script": null},
            {"translit": "first", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {"name": "Iu", "redirect": "Yu"},
      "nodes": []
    }
  ]
}
```


## [2026-09-06T15:20:52.975Z] TOOL CALL #4: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo ---- && ls data/verification/sources/refs/ | head -80",
 "description": "List verification dir and refs"
}
```


### [2026-09-06T15:20:53.030Z] TOOL RESULT

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
----
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
```


## [2026-09-06T15:20:56.834Z] TOOL CALL #5: Bash

```json
{
 "command": "head -60 data/verification/page-202.json && echo \"=== verify_check ===\" && sed -n 1,80p tools/verify_check.py",
 "description": "Inspect an existing verification file and checker"
}
```


### [2026-09-06T15:20:56.884Z] TOOL RESULT

```
{
 "pdf_page": 202,
 "book_page": 172,
 "verified_by": "claude-opus-5",
 "verified_on": "2026-09-05",
 "entries": [
  {
   "entry": 0,
   "root": "Gwa, Gwâ, Gwen 2",
   "verdict": "confirmed",
   "modern_form": "PIE *gʷem- 'to go, to come' (with the collateral root *gʷeh₂- / *gʷā- 'to step, go'); Pokorny IEW 463-465",
   "note": "Pokorny's entry, which begins on p.463 exactly as Nourai cites, is headed 'gʷā-, gʷem- „gehen, kommen; zur Welt kommen, geboren werden“; gʷm̥-ti-s f., gʷem-tu-s m. „Gang, Schritt“', and it is deliberately a double entry (I. gʷā-, II. gʷem-), which is why Nourai's box carries two names, 'Gwa, Gwâ'. His third name 'Gwen 2' reflects the *gʷem- > *gʷen- variant Pokorny himself notes ('Unthematisch *(e)-gʷem-t (> *e-gʷen-t)', and Latin advenam / veniō with -n- for -m-); it is not a separate root in any modern handbook, so it is Nourai's own labelling convenience rather than an error of substance. Watkins/AHD 1985 heads the same material 'gʷā-. Also gʷem-. To go, come'; Cheung splits it into *gaH¹ (PIE *gʷeh₂-, Pok. 463 f.) and *gam¹ (PIE *gʷem-, Pok. 464 f.). The gloss 'to walk, to step, to come, to go' is an accurate rendering. Two words in the chart do not belong to this root: Avestan 'gâv' in node 6 (a misprint) and 'thamân' in node 12 (an unidentifiable form), and one Persian word, nîyâm (node 3), is derived by modern scholarship from a different root (*ni-dā-, not *ni-gam-). Everything else on the page is standard, well-attested Iranian etymology.",
   "note_fa": "جعبهٔ ریشه درست است: پوکورنی در صفحهٔ ۴۶۳ فرهنگ خود مدخل «gʷā-, gʷem-» را با معنای «رفتن، آمدن؛ به جهان آمدن، زاده شدن» آورده و همان‌جا نام‌های gʷm̥-ti-s و gʷem-tu-s «گام، رفتار» را می‌افزاید؛ پس هر دو صورت «Gwa/Gwâ» و «Gwem» از یک مدخل‌اند و برچسب «هندواروپایی» و معنای «راه رفتن، گام برداشتن، آمدن، رفتن» درست است. نام سوم «Gwen 2» گونهٔ *gʷen- است که خود پوکورنی (در *e-gʷen-t و در veniō لاتین) یاد کرده و در کتاب‌های امروزی ریشهٔ جداگانه‌ای به شمار نمی‌رود؛ این نام‌گذاری از خود نورایی است نه خطای علمی. واتکینز (پیوست AHD) نیز همین ماده را «gʷā-, also gʷem-: رفتن، آمدن» آورده و چونگ آن را به دو ریشهٔ *gaH¹ و *gam¹ بخش کرده است. در سراسر این صفحه تنها سه لغزش هست: صورت «gâv» در گرهٔ ۶ (غلط چاپی)، صورت «thamân» در گرهٔ ۱۲ (صورتی که در هیچ فرهنگی یافت نشد) و واژهٔ «نیام» در گرهٔ ۳ که پژوهش امروزی آن را از ریشهٔ دیگری (*ni-dā-) می‌داند.",
   "sources": [
    "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/gʷem-"
   ],
   "ref_check": [
    {
     "ref": "POK:463",
     "status": "supports",
     "note": "POK_02.txt line 1790 (the leaf whose running numbers are 463-465): 'gʷā-, gʷem- „gehen, kommen; zur Welt kommen, geboren werden“; gʷm̥-ti-s f., gʷem-tu-s m. „Gang, Schritt“, Verbaladjektiv gʷm̥-to-s. I. gʷā-: ... 2. gʷem-: ...'. The same pages carry 'av. gātu-s „Ort, Liegerstatt, Sessel, Thron“, apers. gāθu- ds.', 'av. gā-man- n. „Schritt“', 'av. jantu (*gʷem-tu-)' and 'av. jasaiti „er geht“' — i.e. Pokorny 463 alone underwrites the root box and nodes 1, 2 and 6."
    }
   ],
   "consulted": [
    {
     "src": "WLD",
     "where": "Bd. I 675-677 (WLD_Bd1 djvu line 42665 ff., running head 'gʷem-, gʷā-')",
     "stance": "supports",
     "note": "'gʷem-, gʷā-' … 'ai. gātram „Glied, Körper“; ai. gātu- „Gang, Weg, Raum, Ort“, av. gātu-s „Ort, Platz; Liegerstatt, Sessel, Thron“, ap. gāθu … ai. vi-gāman- n. „Schritt“ … av. gāman- n. „Schritt“'. This is the source Pokorny 463 abridges (Buck cites it as 'Walde-P. 1.675 ff.')."
    },
    {
     "src": "AHD",
     "where": "Watkins 1985, g-list (AHD_watkins1985.txt line ~539)",
     "stance": "supports",
     "note": "'gʷā-. Also gʷem-. To go, come. 1. Germanic *kuman in a. Old English cuman, to come: COME … 3. Suffixed zero-grade form *gʷm̥-yo- in Greek bainein, to go, walk, step, with basis (< *gʷm̥-ti-), a stepping, tread, base'. Same double root, same gloss."
    },
    {
     "src": "CHEUNG",
     "where": "s.v. *gam¹ (CHEUNG.txt lines 7307, 7478) and *gaH¹ (line 7054)",
     "stance": "supports",
     "note": "'*gam¹ \"to come\" … «PIE *gʷem- “to go; come” = LIV: 209 f. | Pok.: 464 f.»'; and '«PIE *gʷeH₂- “to go, stride” = LIV: 205 | Pok.: 463 f.»'. Cheung's *gam¹ article lists, as its New-Persian outcome, exactly Nourai's harvest: 'NP zamān “time” … NP gām “step, pace” … NP āmadan … NP pay(g)ām “message”, NP pay(g)ambar … NP anjuman “company, assembly, club”'."
    },
    {
     "src": "SYN",
     "where": "Buck §10.47/10.48 (SYN.txt line 17514 f.)",
     "stance": "supports",
     "note": "'2. IE *gʷem-, *gʷā-. Walde-P. 1.675 ff. … Skt., Av., OPers. gam- \"go, come\" (Skt. gacchati, Av. jasaiti, sk̑o- presents like Grk. baskō; Av. jam- without prefix mostly \"come\"; also Av., OPers. ā-jam- \"come\", whence NPers. amadan \"come\")'."
    },
    {
     "src": "KLN",
     "where": "p.318 s.v. 'come' (KLN_1966.txt line 8320, page marker 318 at the foot)",
     "stance": "supports",
     "note": "'come … fr. I.-E. base *gʷem-, “to go; to come”, whence also OI. gámati, gacchati … Avestic jamaiti “goes” … Cp. the collateral base *gʷā- in OI. agām (aor.), Gk. ébēn (aor.), “I went”'."
    }
   ],
   "nodes": [
    {
     "id": 1,
     "lang": "Avestan / Old Persian",
     "words": "gam : to come, step; jam, jantu : to go",
=== verify_check ===
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


## [2026-09-06T15:20:58.390Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['KLN','KNT','TZF','BQT','MON','POK','AHD','BRT','HRN','HUB','PHD','NYB','WLD','IEC','SYN','SKT','WEB','FSD','ARY','CHEUNG']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:400])\n\"",
 "description": "Show refs_online entries for relevant abbreviations"
}
```


### [2026-09-06T15:21:00.103Z] TOOL RESULT

```
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
TZF {"title": "Mohsen Abolghasemi, Tarikh-e Mokhtasar-e Zaban-e Farsi, Bonyad-e Andisheh-ye Eslami 1373/1994", "kind": "website", "url": "https://ketabnak.com/book/81646 (142 pp. PDF; login) ; https://farhangoadabeirani.blogsky.com/1395/07/20/post-1048/ (download post)", "lookup_hint": "Not on archive.org (only his دستور تاریخی زبان فارسی: archive.org/details/20220417_20220417_2237, and تاریخ زبان فار
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
CHEUNG null
```


## [2026-09-06T15:21:57.589Z] TOOL CALL #7: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['KLN','KNT','POK','BRT','BQT','AHD','MON','TZF','HRN','HUB','PHD','NYB','IEC','SYN','ARY','SKT','FSD','WEB','WLD']:\n    v=d.get(k) or {}\n    print('==',k, '| local:', v.get('local_file'), '| offset:', v.get('page_offset'), '| hint:', (v.get('lookup_hint') or '')[:300])\n\"",
 "description": "Print page offsets and hints"
}
```


### [2026-09-06T15:22:00.290Z] TOOL RESULT

```
== KLN | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt | offset: KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
== KNT | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt | offset: leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; section refs like '$147'. Nourai's page numbers should fall in 164-215 for lexicon citations.
== POK | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt | offset: POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' giv
== BRT | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt | offset: Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops.
== BQT | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'] | offset: vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). | hint: grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --d
== AHD | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt | offset: 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. | hint: Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru
== MON | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'] | offset: None | hint: Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbe
== TZF | local: None | offset: None | hint: Not on archive.org (only his دستور تاریخی زبان فارسی: archive.org/details/20220417_20220417_2237, and تاریخ زبان فارسی on samta.samt.ac.ir / library.tebyan.net/f/Viewer/Pdf/168187 which overlap in content).
== HRN | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt | offset: leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.
== HUB | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt | offset: leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.
== PHD | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt | offset: leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB).
== NYB | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt | offset: Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.
== IEC | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt | offset: TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.
== SYN | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt | offset: leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.
== ARY | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt'] | offset: printed page = pdf page + 1 | hint: Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY
== SKT | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt | offset: leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.
== FSD | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt | offset: vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably detected (pages ~ 700-1640) - grep the headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Headword in bold at line start with pronunciation; etymology in brackets at entry end '[< L. ...]'. Very large OCR (16 MB per vol); grep -n '^word' vol file.
== WEB | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/WEB_vol1.txt | offset: not reliably detected (page_numbers.json sparse); grep headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Headword bold at line start; etymology in brackets. 2nd-edition pagination is the same across 1958-1983 printings, so a 1978 page number can be checked in the 1962 vol. 1 scan for words A-(mid alphabet); vol. 2 only via lending copies.
== WLD | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt'] | offset: Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696). | hint: Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP.
```


## [2026-09-06T15:22:07.953Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 205 206 207 216 217 218; do echo \"=== leaf $n ===\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' KNT.txt | head -60; done",
 "description": "Print Kent leaves around cited pages"
}
```


### [2026-09-06T15:22:09.775Z] TOOL RESULT

```
=== leaf 205 ===
, 66, 70f, 78f, 80, 91, 92; 3.1, 9, 11, 20, 21,
181
28, 29, 40f, 49f, 53, 54, 64, 69, 75, 76f, 83, 83f; 4.1, 3, 5, 11, 17, 21f, 25, 31, 33, 36f, 37, 40, 43f, 45f, 50, 53, 57, 59, 62, 67 bis, 70, 72, 7161, 80, 86f, 87, 88; 5.1, 3f, 14f, 18, 20f, 301, 34; DBa 1, If, 2, 21, 5, 9, 14; DBb 6; DBc 6f; DBd6f; DBe 9; DBF 5f; DBg 6f; DBh 8f; DBi 9f; DB) 4f; DPa 1, 2, 3; DPd 5, 6, 19; DPe 1, 2, 3, 6, 19; DNa 8, 9, 10, 11, 15, 31, 34, 40, 48; DNb 5f, 59; DSb 2, 3f, 5f, 7; DSI lf; D8m 6°; DE 12f, 13, 14f, 16f; XPa 6, 7 bis, 8, 11, 18; XPb 12, 13, 14f, 16, 22; XPd 9 bis, 10, 11, 15; XPe 1, 2; XPf 8f, 9, 10, 11f, 16, 25f, 28, 35, 36, 44; ХРе 2, 6; XPh 7, 7f, 8, 9, 14, 15, 29, 29f, 56f; X82 1, 2; XSc 1°, 1, 1f°, 8°, 3f°; XE 121, 13f, 14f, 16; XV 10 bis, 11, 12f, 17, 17f; A!Pa 9°, 10°, 11°, 12°, 171, 20; Ае 2, 2°, 3, 4; A*Pa 5f ($2478), 9 bis, 10, 11, 21f, 24; Wa 3f; Wb If, 2f, 4f, 5f; We 2f, 3f, 5f, 6f; Wd 3, 4, 5f, 6f; AVsb-d.
z5dyaüiyam asm. AsH 7f; DPd 2f; DNa 5, 6f, 391; DNb 4f; DSm 4; DSt 5f°; DE 7f, 9; XPa 4, 5; ХРЬ 7f, 9f; XPd 5f, 7; XPf 5, 6f, 281; XPh 4f, 5f; XE 8, 10; XV 6, 7f; А!Ра 6°, 7°; MPa 7.
asdyahiyahya gsm. AmH 3; AsH 3f; CMb 2; DB 3.59; DPd 10f; DNe 2; DNd 1f; XPa 10; XPb 19f; XPd 13f; XPe 3f; XPf 14; XPh 11; XSc 2; XE 191; XV 15; А!Ра 15°, z5iyatiya as gsm. ($818.П) АзРа 121, 14, 15, 16, 17f.
хїйуабтуб npm. DB 1.8 (or nsf. adj. ?), 10, 10; 4.51; DBa 13, 16, 17f.
тїйуабёшй apm. DB 4.7, 32.
asayahiyandm gpm. AmH 2; AsH 2; DB 1.11; DBa 2; DPa 2f; DPe 2f; DNa 9; D8b 4f; DE 14; XPa 7; XPb 13f; XPd 10; XPe 2f; XPf 9; XPh 8; XSc 1; XE 14; XV 11; A!Pa 10f°; Wb 3f; We 4f; Wd 4f. zíayatiyanám (552.11) А? 2f; A’Pa 10. On the title "king of kings', see von Wesen- donk, Or. Stud. Pavry 488-90.
XŠ пз. (842) DPb; DPh 1 ter, 4; DSa 1 bis, 2, 3; DSc bis; рва 1 bis, 1° bis, 3°; DSe 8°, 8, 9°, 10°, 14°, 31°, 42, 50°; DSf 6 quater, 8, 55°; DSg 1° quater, 3°; DSi 1, I? ter, 3; DSj 1 bis, 1°, 2°, 5; DSk 1 bis, 2, 4; DSm 1° bis, 2°, 3°; Обр 1°; DSo 3°; DSt 7°, 10°; DSy 1 bis, 2 bis; DZb 1, 2 bis, 3°; DZe 5 ter, 5°, 7; DH 1 ter, 3; ХРе 6 ter, 7, 10, 11; ХР} quinquies; АЧ ter; D’Sa 2°; D’Sb 1° ter, 1, 8°; А?8а 1 quater; A’Sb ter; A?Sd 1 quater, 2; A*Ha 1 bis, 1° bis; A?Hb; A?He 7, 8 ter, 16 bis; SDa; SXa 2; SXb 2; SXc 1; XVs; AVsa.
Хт asm. DSe 5, 6; ХРе 4, 5; D'Sa 3; А?Не 5, 6. XSyam DSf 4, 4f, 10, 15; 17; DSi 8°; DSn 2; DSp 2; DZe 3.
182
Xšyā gsm. DZc 3; A!He 10, 11, 12,13. X Shyà DPe; DPi; ХРе 9, 14; XP^; XPk; XH; АЧ bis; D'Sb 2°; A’Sa 1, 2 bis, 3; A'Sb; Ае 0; A?Ha 2, 3, 3°, 4. XSahyi (853) А84 2. XSyahya XP}; XSyahiya (827) XPjv. XS as gsm. (8313.1) A!Hb.
XSanam gpm. XPc6. XSyánàm Га 11; DSc; DSd 1; DSe 8f; DSf 6; DSg 1°; DSi 1°; DS} 1; DSk 1f; DSm 1°; DSy 1; DZb 2; Рӯе 5; ХР}; АЧ; D'Sb 1°; A’Sa 1; A'8d 1; A?Ha 1°; A’He 8. XSyanam (§52.11]) DPh 1; DH 1. XSyana (§52.V) A?Sb.
X SaydrSan- sb. ‘Xerxes’: Elam. ik-Se-ir-28-Sa, АКК. hi-&-"-ar-áa, Gk. ép£ns: from хќауа- ‘king’, Ау, z&aya-, to root z$ay-, + arsan- ‘male’ ($181): ‘Hero among Kings’, cf. Skt. rdja-rsabha- (Bthl. AiW 550; but Hz. AMI 1.121n, Bv. Gr. §290, take second part to be arša- ‘just’, on which cf. §162.n1, $187.n2; ef. also Hz. AMI 7.82-137, esp. 135-6, on which see Henning, BSOS 10.502-3). Decl., 6187.
Хїауйгёй пэт. XPa 6, 11, 17; XPb 116, 21, XPc 6, 9; XPd 8f, 15; XPe 1; XPf 8, 15, 27, 44; XPg 1; XPh 7, 18, 28f, 56; XP} bis; XPk; XSa 1; XSe 1°, 3°; ХЕ 12; XV 9, 16; А!Ра 19f; A?Pa 16, 16f (both as gen., $313.ITI); Ха 1; SXb 1f; SXe 1; XVs.
XSayarsam asm. XPa 4; XPb 7; ХРе 4; XPd 5; XPf 5; XPh 4; XE 7f; XV 6.
X Saya[rsiha] gsm. XPi; [XfayárMüha XH. X Saydrsahyd ($57) А!Ра 14f; АЛ bis; A?Ha 3, 3f. Xéayárcahyü (849b) A’Sa 2 bis. Xšayāršähyā А?Не 12, (as nom., $818.1) 12f. Xarsada&yà, q.v.
тёпа- vb. "learn, come to know, know’: Av. xind-, Skt. jñā-, Gk. yeyrwoxw, Lt. gnóscó, NEng. know, pIE *gné- (806, $110, 8212). See also zínav-, dan-. | adünà imf. (NPers. dánàm, 568, $210) DB 1.51; DSq 3. x&ndsahy 2d
=== leaf 206 ===
 sg. subj. (8212, $227.1) DNa 42. xindsdtiy subj. ($02, $97, 5110, $122) DB 1.52.
azinav- vb. ‘hear, satisfy’ ($96): cf. Av. zšnav- ‘Genüge haben an’, adj. zínav- ‘Genüge leistend’, ріс. zšnůta-, sb. zínütay- ‘Zufriedenstellung’ (Bthl. AiW 557-60); apparently an extension of root zinà- ‘learn’ (cf. pIE *40- and *doy- ‘give’), with semantic development ‘learn, hear of, hear’, and ‘hear, hearken to, satisfy’ (Lg. 15.171; ef. also Bv. TPS 1945.47-50). Hz. ApI 238-40 gives an impossible equation with Skt. éru- ‘hear’ (pIE
OLD PERSIAN
*flu-); Sen 247, 251, has wrong meanings. Р}.
sani, Acme 1.319-20, gives another etymology, -
See also uzsnav-.
z5nula- past pte. pass. ($71, 3242.1), cf. uzšnav-: zSnuta nsm. ‘satisfied’ DNb 26. |xsnutam) nsn. ‘heard’ DNb 53.
à + zínav-: dxSnautiy (§71, $122, $208) ‘satisfy’ DNb 24. āzšnavāhy 2d sg. subj. (§227.1) ‘satisfy’ DNb 29f. äzšnudiy 2d sg. ішу. ($208, §237.1) ‘hear’ DNb 54.
gaifa- sb. ‘(living) personal property, cattle’: Av. gaébü- ‘individual living being, pl. world; household, property’, РЫ. géhdn ‘world’ (from gen, pl.), to root pIE *g*ei- seen in OP jiv- (869, $101, $151). For varying interpretations, see Tm. Lex, 85, with lit. — ga26àm-cà (S89) asf. DB 1.65.
gaud- vb. ‘conceal’: Av. gaoz-, Skt. githati (§88). apa- + gaud- ‘conceal, hide away’: apagau- dayahy 2d sg. subj. (§227.1) DB 4.55, 51. apagaudaya 2d sg. inj. (5215, §224, §227.II, $237) DB 4.54. gaub- vb. ‘say’, mid. ‘call one’s self’ (§213): Sas. РЫ. gowét ‘he says’, NPers. goydd, inf. guftán: perhaps a -bh- extension of pIE root *gheu- seen with -s- extension in gauga- (q.v.; Ву. BSLP 31.2.70). gaubataiy mid. (42851) DB 2,21, 31, 51; 3.15, 59. agaubaté imt. mid. DB 1.84, 93; 2.66f; 3.35, 55 (written agauratà, 454.11), 89f; 4.82. agauba^ià 3d pl. imf. mid. ($28617) DB 293. gaubdtaty subj. mid. (5285.1) DB 2.84; 3.86.
Gaubarwa- sb. ‘Gobryas’, ally of Darius against Gaumata: Flam. kam-bar-ma, Akk. gu-ba- ru-’, Gk. TwBpins; from gav- ‘cattle’ + *baruva-, cf. Skt. bharu- ‘lord’, to vb. bar- ($85.П, $101, $122, $142, $143.II, $150, $1581, $160.Ib): ‘Cattle- Possessor’ (Justi, IFA 17.111; otherwise Foy, ZDMG 54360). Gaubaruva nsm. DB 4.84; 5.7, 9, 11; DNe 1.
Gaumdta- sb. ‘Gaumata’, Median pretender who took the name Smerdis ($164.I): Elam. kam- ma-ad-da, АКК. gu-ma-a-lá; from gav- ‘cattle’ + pte. mdta- of unknown meaning ($242.II). Gau- mata nsm. DB 1.36, 44, 46, 64, 65, 70; 4.7; DBb 1f. Gaumdiam asm. DB 1.49f, 54, 57, 73; 4.81.
gausa- sb. ‘ear’: Av. gaosa-, NPers. gas, Skt. ghóga- ‘noise’; Iran. root *gaus- ‘hear’, pIE *gheus-
(670, 5101, $1431). диа adm. ($189) DB 274, — |
| КИ adven as n Le ЧЕР Г PERDE :
ок ALES
e
LESIN EI EOE PE EERE СООТУ
I aen i bag ih oea CAU Lin aE M iig Án
LEXICON
89. gaušāyā idm. (5189; with sg. ending, Lg. 19.225) DNb 53.
gafu- sb. ‘place, throne, place of battle’
(JNES 4.49-50): Av. gdtav- дабш-, NPers. gah, Skt. gütu-, to pAr. root gam-, pIE *g*em- ‘come’ ($68, $81, $158.11, §179.n2). давит asm. DNa 41f. дйбарй lsm. ($137, $182.IT) DB 1.62f, 66, 69; DNa 36; DNb 35 (INES 4.49-50); DSe 36f, 44, 44f; XPf 33 (as abl., $182.III, though without hacé: Lg. 941-6; Ву. BSLP 33.2.148-50; Wb. А 41.319-20; Sehaeder, SbPAW 1935.503; Hz. AMI 4.130-2, 8.45, ApI 177-80), 85; XPh 34.
gad- vb., see jad-.
Ga*dara- sb. ‘Gandara, Gandaritis’, a prov- ince of the Persian Empire: Elam. gan-da-ra, Akk. gan-da-ri. See also Gadáraya-. Сайдта nsm. DB 1.16; DPe 1.18; DNa 24f; DSe 24°; DSm 9°; XPh 25. Gadārā absm. DSf 34.
Ga"déraya- adj. ‘Gandarian’: adj. to preced- ing ($144.III, $167). Gadàraya пзш. APP 12.
Ga*dutava- sb. ‘Gandutava’, a district in Arachosia: Elam. gan-du-ma-+. Cf. Tm. Lex. 86. Gadutava пет. DB 3.66.
gan- vb., see jan-. gand- vb., see gasta-.
gam- vb. ‘come’: Av. gam-, Skt. gam-, Gk. Ваши, Lt. venió, Gt. qiman, pIE g*em- ($101, $244). See also gdéu-.
à + gam- ‘come’: бјата opt. (Skt. gamyat; §67.1, §101, $122, $132.2, $218.11, $293.I, §228.IT) DPd 19.
ava- + gam- ‘go dow
=== leaf 207 ===
n, fall down’: [avagmat]a nsf. past pte. ($244) DSe 46f (conj. of Kent, cf. JAOS 54.46).
рата + gam- ‘go forth’: paragmata nsf. past pte. ($101, $103.IV, §122, 8132.2, §244) DNa 44f.
ham- + gam- ‘come together, assemble’: ha"- gmaté npm. past pte. ($101, $1081У, $1322, $140.V, $244) DB 2.32, 38, 43, 52, 58; 3.65. See also Надтаійла-.
gay- vb., see Jiv-. gara- ‘devouring’, see bdtugara-.
garta- sb., either ‘cave’ or ‘wagon’, see Asa- garla-.
Garmapada- adj. ‘Garmapada’, the fourth month, June-July: Elam. kormabadas, АКК. du-
183
'"üzu. From garma- ‘heat’, Av. garama-, Skt. gharmá-, Lt. formus ‘hot’, NEng. warm, pIE *gthormo-, cf. Gk. bepuos (with analogical -e-), + pada- ‘step, station’ ($29, §31, $149.1, $161.Ib, $165): ‘Heat-Station Month’. — Garmapadahya gsm, DB 1.42; 3.71, 46.
gav- sb. ‘cow, cattle’ ($101): Av. gau£, Skt. gaus, Gk. fois, NEng. cow, pIE nom. *g*dus: in Gaubaruva-, Gaumäla-, perhaps in Gatagu-.
gasta- adj. ‘repugnant, evil’; пі, as sb., ‘evil, harm’: past pte. ($85, $242.I) of vb. *gant- *gandh- ‘smell’, Av. ganti- ‘evil odor’ (AIW 493), duZ-gantt- ‘evil-smelling’ (AiW 757), Skt. gandhá- ‘odor’ (Bv. Gr. $179); for meaning, ef. Lt. odor ‘smell’, бй ‘(I have smelled), I hate’, odium ‘dislike, hatred’. Not abstract to same root, *gant-tdi-, nom. gasta', abl. shortened by haplology, as taken by Hz. AMI 8.68, ApL 173-7. gastá nsf. DNa 57f. дазій absn. DNa 52; XPh 57; ASa 5°; A’Sde 4 (gasta da, db; $53); A?Ha 6°.
gud- vb., see gaud-.
gub- vb., see gaub-.
grab- vb. ‘seize (аз possession), seize (as prisoner)’, pres. garbaya- (§30, $217): Av. grab-, pres. gaurvdya-, Skt. grabh-, pres. grbhdyah, NEng. grab, pIE *ghrebh-. See also Patigraband-. agar- . bayam Ist sg. imf. DB 24 bis; 4.7, 32; 5.25f; DNa 17; DSe 16; DZe 8. agarbáya imf. DB 2.88; 3.74, 90°; 5.12. agarbaya* 3d pl. imf. 04232.) DB 2.18; 3.48, 49; 5.27f. agarbayalà imf. mid. (§235.11) DB 1.42, 43, 81; 3.82f. When meaning ‘seize as prisoner’ (DB 2.4 second occurrence, 13, 88; 3.48, 49, 74, 90; 4.7, 32; 5.12, 25f, 27f) per- haps not agarb- but ágarb-, from à + grab- (see below).
à + grab- ‘seize (as prisoner)’: dgarbita пзш. past pte. pass. ($80, §217, $232.11) DB 2.73. For uncertain examples, see under grab- (uncom- pounded).
-cé (i.e. -cd) enel. conj. ‘and’: GAv. -@, LAv. -€a, Skt. ca, Gk. тє, Lt. -que, pIE уш, ~... -cé ‘both ... and’ DB 1.65, DNb 32; cà .. . -cã ula ‘both ... and... and’ DB 1.66-7. -cé DB 1.65 ter, 66, 66f; DPd 9f; DNb 32 bis; XPh 41, 51, 54. -ca-maiy DNb 28, 51, 52 (§51).
+++ canüm, see ustasand-.
canah- sb. ‘desire’, see Aspacanah-; cf. also kam-.
184 | 631689 V, ОГ car- vb. ‘move’, see abicarig; cf. also under
ucara-. cdra- (5126), see ucüra-.
| caša- sb. ‘eye’: to root in Skt. caks- ‘see,
speak’, derivatives cdksas- cakşu- cakgus- caksan-, and Ау. čašman-, Phi. NPers. čašm ‘eye’; initial u- of ucasma is an error (Bv. TPS 1945.53-4, quoting Jn. IF 25.182). The stem is caSa-, not caKman- (Kent, Lg. 19.225-6), since the nom.-acc. of nt. casman- would be cašmā and not ca$ma. Cf. $102, $143.I, $187.n1l. Attempts to explain the erroneous u- of ucaima, Wb. ZDMG 61.726; Wackernagel, KZ 61.205-8. саат asn. DB 2.75, 89 (Cameron found ст“ legible in 89, but only the final me in 75); caSa{m} (case and form uncer- tain) DSq 2.
ci- interrog.-indef. pron. ‘what, any’; col- lateral stem (8201) to OP ka-. See also -ciy, cid, cind, cijükara-.  ciš-ciy asn. ‘anything’ (§9.VI, $105, 5132.2, §201) DB 1.58, Lt. quicquid, pIE *q*id-q*id: reduplicated form with Med. sandhi; see OP -ciy for exact cognates.
-ciy encl. particle, emphasizing or generaliz- ing, nsn. or asn. of с1-: Ау, -Git, Skt. eid, СК. т, Tat. quid, pIE *q*id (840, §84, $113, 5191.11, §201, 6998.11). In the following combinations: aciy (q.v.) ХРЇ 21. aniyaš-ciy nsn. DB 4.46; XPa 13; aniya&-c (452.1) XPh 41f; aniyai-ciy npm. XPf 29. avas-ccy nsn. DNb 55; asn. DNb 5
=== leaf 216 ===
rada&a, duvaista-. dürau lsn. as adv. ‘afar, far away, far and wide’ (GAv. düiré, LAv. duire, Skt. d'ré; $65, 6191.111) DNa 44. duraty apiy DSe 11, DZe 6, DE 18, XPa 9, XPb 18, XPe 8, XPd 13, XPf 13, XPh 10, XE 18, XV 14, A'Pa 14f°, A’He 17. düraiapiyy DNa 12, dürayapiy DNa 46 ($18, $136).
duradasa adv. ‘from afar’, with preceding hacá: dūra- + adv. -dä asin отада + abl. -ša asin avada&a (§135, 5191.1; ЈАО 54.37).  DSf 23.
duruj- vb. ‘lie, deceive’: Av. druj- ‘le’ (draog-, Bthl. AYW 767), pres. druZasti, sb. druzé ‘principle of evil, devil’, Skt. drúhyatí ‘deceives’, Gm. trügen, pIE *dhrugh- (876.111). See alsodrauga-. adu- rujiya imf. (§101, $103.IV, $113, 5128, 4132.1, 2, 3, $214, 5228.11) DB 1.39, 78; 3.80; 4.8, 10f, 13, 16, 18, 21, 24, 261, 29; DBb 2; DBc 2; DBd 2; DBe 3f; DBf 1; DBg 2; DBh 2f; ОВ! 2f; DB} 2f. adurujiyasa" 3d pl. imf. ($214, §218.1, $232.III) DB 4.34f. duruxiam nsn. past pte. pass. ($103.IV, $122, $128, 8132.1, 3, $242.I) DNb 52, 5f; asn. DB 4.44f, 49f.
duruva- adj. ‘firm, secure’: Av. drva-, Skt. dhruvd-; deriv. to root in OP ‘dar- ($122, $128, $150). durwä nsf. DB 4.39.
duvatsta- adj. ‘very long, very far’: superl. to dūra- ($156.IIL, §190.11 $191.0; МВ Gr. $275), ef. Skt. davisthd- with slightly different formation.
192 OLD PERSIAN
duvais[ta]m asn. as adv. ‘for a long time’ DPe 23 (cf. remarks s.v. hyà).
duvara- sb. ‘door’: Av. dvar-, Skt. dhvar-, Gk. дора, Lt. forés, NEng. door, Lith. dvéras ‘court- yard’, pIE *dhuor- dhur- and its extended forms *dhyoro- etc.; see also duvarfi-. duvarayd-maiy lsn. ($186) DB 2.75; 89f.
duvari- sb. ‘portico, colonnade’: duvar- ‘door’ + varði- ‘cover, protection’, to root var- ‘cover’, with haplology ($34, $129, $152.IV, §160.Ia; ВЫ. AIW 766). duvarfim asm. XPa 12.
duvitdparanam adv. ‘one after the other, in succession’, a meaning agreeing with Elam. Samak- mar ‘ex ordine’: duvità ($191.11, $204.IT), MPers. dit ‘one or other of two’ (Bthl., quoted by Tm. Lex. 102), ef. OP duviliyam ‘a second time’, Skt. 0015 ‘twice’, Lt. bis, + paranam ‘before, previ- ously’ (Tm. 1.е., and Vdt. Stud. 1.8). This is better than Tm.’s "long aforetime', adv. duvità ong’, GAv. дайа, Skt. dvità (cf. OP duvaistam), + paranam (as above); also than KT's duvità- parnam ‘in two lines’, contaming the cognate of Skt. parnd- ‘wing’ (supported by Wb. ZDMG 61.724-5, KIA 10-1, and by Hz. AMI 1.112n). DB1.10; DBa 17.
duvitiya- adj. ‘second’: GAv. daibitya-, LAv. bitya-, Skt. dvitiya-, pLE *dyitiio- (676.11, 51441, 5204.1). See also duwilàáparanam. дилат, asn, as adv. ‘a second time’, DB 2.87f, 57, 3.77; as inner obj., ‘a second (uprising), DB 3.24 (not duvitiya-ma udapalalà ‘was second to rise up from me’, as Bthl. AiW 964 takes it, since udapatatà nowhere else takes an expression of the person against whom uprising is made).
duš- insep. prefix ʻi: Av. dui-, Skt. dus-, Gk. dve- ($76.Ш); in dušiyāra-, duskarta-.
dusiyara- sb. ‘evil year, bad harvest, famine’: duš- + yar- ‘year’ made thematic, Av. ydr-, Gk. ёра ‘season’, NGm. Jahr ($140.VIT, $143.IT). dušiyāram nsn. DPd 19. dudiyard absn. DPd 17.
| du$karia- ad). ‘ill-done’, opposite of naiba- (Hz. ApI 1434): duš- + karta- ‘done, made’, past pte. pass. tokar-. duskartam nsn. DSe 31f; XPh 42. draug- vb., see duruj- and draujiya-.
drauga- sb. *the Lie", the evil force opposed to Ahuramazda, Ávestan Druj: Av. draoga-, NPers.
dury, Skt. drógha- droha- ‘(malicious) injury’, pIE *dhrougho-, cf. NGm. Trug ‘deceit’, and OP duruj-, draujana-, draujiya- (870, 576.11, $101, $108.IV, $106, $122, $128, 5132.2, 3, $143.I, V). drauga nsm. DB 1.34, 434; DPd 20. draugà absm. DB 437; DPd 17f.
draujana- adj. ‘deceitful’, i.e. ‘adherent of the Lie’: deriv. of drauga- (§101, 5132.2, 5147.1), cf. GAv. drogvant- ‘adherent of the Dru? (Hz. Apl 140-1). draujana nsm. DB 4.38, 63, 68. drauja- nam asm. DNb 12.
draujiya- vb. ‘regard as a lie’, denom. to drauga- (S217). [Отау уау 2d sg. subj. (§222.11, §227.1) DB 4.43.
drayah- sb. ‘sea’: Av. zrayah-, NPers. dáryà, ·
Skt. jrdyas- ‘expanse’, pIE *órejos- (§88, $113, $128, $156.II). Decl, §185.1. See also para- draya. draya asn. DB 5.23; DP
=== leaf 217 ===
e 15; DZe 10. drayahya lsn. ($136, §251A; wrongly taken as gen., Hz. АрІ 141-3) DB 1.15, DPe 14, DSe 28°; drayahiyà ($27) XPh 23.
naiy adv. ‘not’: Av. 207, РЫ. në, Skt. ned; :
from pIE *ne, Skt. na, Lt. ne-scio ‘I don't know’, -+ Эа, asn. of pron. i-, Lt. id, OP id-am, ete. (869, 884, $191.1, $291.11, §292a). DB 1.32, 48, 49 ter, 52, 53, 71, 91°; 221, 24, 31, 51, 84; 3.15, 86; 4.44, 47 bis, 51, 55, 58, 63 bis, 63f, 64°, 65 bis; 5.16°, 31; DPd 11; DNb 7f, 12, 13, 21, 23, 36, 40; DSe 36, 40 bis, 43°; DS} 3; XV 22. nai-maiy (836) DB 4.64. nai-ma DNb 8, 10, 19. nai- pati-mà (8133) ОМ 20. nai-&im DB 4.49. naty- diš ($136) DB 4.73, 78.
naiba- adj. ‘beautiful, (religiously) good’, re- .
placing GAv. vahu- ‘good’, and opposite of duš- karta- (Hz. AMI 8.68, ApI 266-7): NPers. nē ‘brave, good’ ($11, §75.V, $148.11). пафа nsf. DPd 8. naibam nsn. XPa 13, 16; XPg 4; XV 20. naibam asn. DSe 32°; DSi 4^; DSp 2f°; XPh 43.
naucaina- adj. ‘of cedar’: NPers. nóZ, пдѓап ‘pine cone’; therefore naucaina- ‘pine-cone-shaped’ ($147.11), appropriate to the cedar (König, Burg- bau 53-4; Hz. AMI 3.58). naucaina nsm. DSf 30f. |
nab- vb. ‘perish’, causative (8123.2, $215) "in- jure; destroy’: Aw. )nas-) ӨЮ. naé-, Gk. vexus
7 ыйсы аЙ eet NUI ШЕЛ, АМАА а аз an ШО. Дені. Zr é
DD де 5... anes
LEXICON
‘corpse’, Lt. acc. nec-em ‘destruction’, nocet ‘harms’, pIE *nek- (887).
vi- + nab- caus. ‘injure, harm’: vindPayatiy (8215) DNb 17f. viyanatlaya imf. (§122, $1232, $215) DB 4.66. vinátayá"tiy За pl. subj. (8222.1I, §232.1) A’Sa 5°, A?Ha 7° (conj. Kent). vinátayais opt. ($215, $223.II, $228.11) DNb 20, 21. vi- nastahyd gsn. past pte. pass. as sb. ($03, $122, $242.11) DNb 18.
Nadi"labaira- sb. ‘Nidintu-Bel, a Baby- lonian rebel: Elam. nu-ti-ut-be-ul, Akk. ni-din-ti- йе] (§75.V, §76.V, $107). Naditabaira пзш. DB 1.77, 92f; 2.1; 4.12; DBd 1. Naditabairam asm. DB 1.80, 84; 24, 5. Naditabairahyà gsm. DB 1.85, 89, 95.
napüt- sb. ‘grandson’: Av. Skt. napat-, Lt.’
nepos, pIE *nepot- (875.1, §110, $142). napa nsm. (§124.5, §188.1) AmH 4; DB 1.3; DBa 4; А:Ра 16°.
Nabukudracara- sb. ‘Nebuchadrezzar’, son of Nabonidus; name assumed by the rebels Nidintu- Bel and Arkha: Elam. nab-ku-tur-ra-sir, Akk. nabu-kudurri-ugur (82, 833, §75.V, $128, §163.- VD. Nabukudracara nsm. DB 3.80f, 89; 4.14, 29f; DBd 3f; written Nabukuracara ($52.V) DBi 5f. Nabuk*dracara (822) DB 1.78f, 84, 93.
Nabunaita- sb. ‘Nabonidus’, last king of the New Babylonian Empire, 556-39. в.с: Elam. na- bu-ni-da, Akk. nabü-na'id; Gk. Aaßivnros (Hat. 1.74, ete.). Nabunailahyà gsm. DB 1.79. Na- bunaitahya (§36.1Vb) DB 3.81; 4.14, 30; DBd 5f; DBi 7f.
niman- sb. ‘name’: Ау. náman-, NPers. пат, Skt. náman-, Lt. nomen, pIE *nómen-, cf. Gk. буора, NEng. name ($109, $110, 5155.11). See also Andmaka-. náma^, suffixless lsn. used with mase. and nt. generic nouns to denote specification ($112, $187, §251C, §312): DB 1.28, 30, 36, 37, 74, 77, 92; 2.8f, 9, 14°, 19, 22, 29, 38, 49, 65, 79, 82, 95; 3.5, 12, 13, 22 bis, 31, 34, 44, 51, 56, 78, 84; 4.8, 10, 12f, 15f, 18, 20, 23, 26, 29, 83 bis, 84 bis, 85, 86°; 5.5, 8, 27; DSe 45°; DSf 31, 46; Юле 9; XPf 18, 19; А?Не 14f; A?Pa 19, 20; Sa 2f. nama, either asn. *ndmá ог lsn. лата” (with lengthened grade), specialized for similar use with fem. generic nouns because of similarity of end- ing ($67.1T, $187, §249L, $312; cf. Tm. Lex. 105,
193
with lit.; not with Foy, KZ 35.11, 37.505, IF 12.172n, nor with Debrunner, IF 52.153): DB 1.58, 58f; 2.271, 39, 44, 52, 59, 72; 3.11, 23, 61, 66, 12, 19; 54°.
nay- vb. ‘lead’: Av. nayeitt, Skt. náyati. Conj., §213. anaya imf. DB 2.88; 3.88°; 5.12. [ajnaya" 3d pl. imf. ($232.11) DB 5.28. anayatá imf. mid. as pass. ($235.П) DB 1.82, 2.73; 5.26". Some or all of these are possibly ànay-, from à + nay-. | fra- + nay- ‘lead forth, provide’: fránayam Ist sg. imf. ($226.11) DB 1.87.
nar- sb. ‘man’: Av. Skt. nar-, Gk. дир, cf. Lt. Ner-6; i
=== leaf 218 ===
n üv-nara- (§142).
nàv- sb. ‘ship’: Skt. ndus, Gk. vais, Lt. nav-is, pIE *ndv- ($142). See also ndviyd-. [naval прі. (8183.1V) DZe 11 (supplied by Tm. Lex. 52).
navama- adj. ‘ninth’: Ау. паота-, Skt. navamá-, pAr. navama- remade from pIE neyeno- after pAr. dasama- ‘tenth’ ($14911, $204IV), ef. Lt. nénus.  navama пзш. DB 1.10; DBa 10f.
naviyd- fem. adj. as sb., ‘navigability’, i.e. ‘impossibility of fording the river on foot’: Av. nàvaya- ‘navigable’, Skt. navyd-, adj. to nàv- ‘ship’ (§144.V). Hardly collective, ‘collection of ships, flotilla’, and certainly not lsf. to nav-, ‘on ship- board’; ef. König, RulD 70-1, and esp. Kent, JAOS 62.269-71 (with lit.), 63.67. ^ nàviyà nsf. DB 1.86.
nàh- sb. ‘nose’: Av. nàh-, Skt. nds-, Lt. narés, NEng. nose, pIE *nds- (5110, $142).  náham asm. (81181, §185.1V) DB 2.74, 88f.
ni- prep. and verbal prefix ‘down’: Ау. ni, Skt. ni-, pIE *ni; in adv. nipadiy, and with verbs ar-, kan-, cay-, pa10-, yam-, std-, had-.
nij- verbal prefix ‘away’: sandhi form of pIE *nis- before voiced stops, generalized, cf. Av. niš-, Skt. niş- ($120); with verb ay- ‘go’.
nipadiy phrasal adv. and prep., ‘on the track of, close after’: prep. ni- + loc. padiy, to pad- ‘foot’ ($76.11, $136, $140, $191.1V). тарайту adv. DB 2.73; prep. with acc. DB 3.73.
nipisti- sb. ‘impression’: deriv. of ni- + paid- ($152.11).  [niplisftiya] Isf DB. 4.90 (conj. of Kent, JAOS 62.268).
194 OLD PERSIAN
niydka- sb. ‘grandfather’: Av. nyáka- ($146.- HI); ef. apaniyüka-. {nilyaka nom. DSI 13; [n*yd|kama (522; for -Кат-тату, $41, §52.1, $130, $138.I) asm. A’Sa 4.
niyaSadayam, see had-.
Nisdya- sb. ‘Nisaya’, a district in Media: Elam. nu-is-fa-ja, Akk. ni-is-sa-a-a (5116). Per- haps from ni- ‘down’ + sdya-, to root Av. st- say- Tie’, Skt. §-, Gk. кт. ‘Ties’, pIE *kei-. Nisdya nsm. DB 1.58. |
niXadayam, see had-.
nüram adv. ‘now’: Av. nürom; from pIE *ná ‘now’ (Av. nū, Skt. пй, Lt. nu-nc, NEng. now) + final of (pAr.) *düram ‘long’ (§148.1), cf. düraty. DB 4.53.
pä- vb. ‘protect’: Av. pà-, pres. рйи, РЫ. pátan, Skt. pà-, pres. pati (ablaut, §122). See also zíacapüvan-. apayaiy lst sg. imf. mid. (Ву. BSLP 33.2.151-2; Kent, Lg. 9.42; S71, $214, $233.1II; wrongly to Skt. pt- ‘swell’, Wb. ЖА 41.820-1) XPf 39. padiy 2d sg. imv. (5208, §237.1) DPe 21f. pätwv (§208, $297.IT) AsH 12, 14; DPd 16; DPh 10; DNa 52; DSe 50; DSf 57; DS} 6°; D8n 2°; роз 7°; DSt 8°; ОН 8; XPa 18, 20; XPb 28; ХРе 12, 15; XPd 18; ХР 45, 48; XPg 13; XPh 57; Хе 5^; XV 25f; А:Ра 226; D'Sa 3; A?Hb^; A?He 19. pätw 3d pl. іту. (§237.1T) A'Sa 5°; A’Sd 4; А?На 6°; A?Pa 25. pála пзш. past ptc. pass. (§242.IT) DPe 22. pati- + pã- mid. ‘protect one’s self against’, with Ласа + abl.: райїрауаш@ (828; not wrongly written, despite MB Gr. §69) 2d sg. imv. mid. ($71, §214, 5297.11) DB 4.38.
paié- vb. ‘cut, engrave, adorn’: Av. paésa- ‘adornment’, Skt. pisdtz ‘cuts, adorns’, Gk. токіћоѕ ‘variegated’, OCS pisati ‘to write’, pIE *peik-, cf. Lt. pingit ‘embroiders, paints’ (Wb. AfOF 7.42). Cf. also nipišti-, parsiyd-, Paišiyđwwādā-, pisa-. аріа imf. DSf 54 (§211; cf. Konig, Burgbau 72). [ар #} уа] imf. pass. ($220) DB 4.91 (JAOS 62.268). [pjisia nsf. past pte. pass. ($242.1) DSf 42 (Bv. BSLP 30.1.62; Konig, Burgbau 71; not dista with Hz. Apī 121-5].
mi- + pub- ‘engrave, inscribe, write’: niyapat- Sam Ist sg. aor. ($02, $102, $130, $218.T, $226.IT) DB 4.71. mipaislanaty inf. ($03, $122, $288) XV 24f. nipislam asf. past ptc. pass. (803) XV 22f.
nipistü npf. XPh 31. nipistam nsn. ($122) DB 441, 47f; DNb 57°; DSe 52.
paišiyā- sb. ‘script, written text’: deriv. of pai- (§89, §144.V). See also Parsiyduvada-. ри nsf. DB 4.91 (conj. of Kent, JAOS 62.268).
PaiSiyd'uvdda- sb. ‘Paishtyauvada’: АКК. pi- &-"-hu-ma-du. Perhaps,
```


## [2026-09-06T15:22:21.516Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 215 226 227; do echo \"=== leaf $n ===\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' KNT.txt | head -50; done",
 "description": "Print Kent leaves 215, 226, 227"
}
```


### [2026-09-06T15:22:23.241Z] TOOL RESULT

```
=== leaf 215 ===
Hz. Ap! 136-8) nsn. as sb. ‘handiwork’, DSe 42.
Daha- adj. ‘Dahian’; pl., a province of the Persian Empire: АКК. da-a-an, Gk. Aaa (§76.V; Lg. 18.298; Hz. AMI 8.72). Dahà npm. XPh 26.
dahyu- sb. ‘land, province, district’: GAv. :
daltyu-, LAv. dahyu- daiphu-, NPers. dih ‘village’, Skt. ddsyu- ‘stranger, demon’ (5124.2, $153.IV, $166). Decl., 5183.1. See also visadahyu-.
dahyaus nsf. AmH 5, 8f (as Isf. §814b); DB 1.59; 2.28, 58, 59, 72; 3.9, 11, 20, 28, 66, 75, 79f; 5.4, 13f, 29f; DPd 6. dahydus-maty DB 4.39. dahyüum asf. (853, $72) AsH 8, 11, 13; DPd 15, 18; DNa 53. dahydvam (8124.VY) XPh 88, 58f. dahyaud (dahyuvd Wb.) isf. (M8, §124.2, 8137) DB 1.34.
dahyàva прі. ($124.7) DB 1.18, 17, 18, 28, 41; 2.6°; 4.33; DPe 7, 14; РМа 17, 39; DSe 15f, 32f; DSm 5°; XPh 15. dahyáva apf. DB 1.21, 47, 67; 4.92, XPh 31,35. dahyünüm gpf. DB 1.2; DBa 3; DPa 4; DPe 3; DNa 10; DSb 6f; DSe 9°; DZb 2{°, DZc 5; DE 15; XPa 7f; XPb 15; XPc 7; XPd 10f; XPf 10; XPh 8f; XSc 2°, ХЕ 15; XV 111; А:Ра 11f°; A’Sc 3f; Wb 5; We 6; Wd 6. dahyüv- näm (523.11) РР} 2; DH 1f. dahyusued lpf. DB 1.35.
DHum (842) asf. DSf 58; DSj 6°. DHyaum (553) А2Рә 26. -DHnám gpf. DSa 2; DSd 1; DSf 6; 056 1^; D8i 4°; DSk 2; РӘ 2°. DHyünam
LEXICON
DSy 2; ХР); АЧ; D'Sb 1; A’Sa 1; А84 1; А?На 1°; А?Не 8; A?Pa 11.
idi- vb. ‘see’: Av. *dá(y)- ‘see’ (Bthl. AW 124), NPers. diddn, Skt. dhi- ‘think’. didzy 2d sg. mv. (865, $129, 5209, $218.II, $237.1) DNa 41; DNb 57.
*di- vb. ‘take by force (a thing from a person, 2 acc.), deprive (a person of a thing, 2 acc.)’: Av. zinditi ‘harms’ (zyà-, Bthl. AYW 1700), Skt. jináti ‘oppresses’, jdyati ‘conquers’ ($88), ef. Gk. Bia ‘violence’. айтат Ist sg. imf. (5210.1, $226.II) DB 1.59. айта imf. (5210.1, $228.IT) DB 1.44f, 46, 66. ditam asm. past ріс. pass. (82421) DB 1.50. |
-di- enel. pron. ‘him, them’, usually with masc. antecedent: Av. di- (Bthl. AiW 684); start- ing by wrong division of pasdvad-im etc., where -im is acc. to *is, Lt. is, and extended (§195.II; Caland, KZ 42.173; Mt. MSLP 19.535, Gr. $166); on competition with pron. -%i-, see Bv. Gr. 645.
-dim asm. (5195.1) in pasdva-dim (with fem. an- tecedent) DNa 33; anu-dim DNb 16, 18; avabá- dim DNb 17; hau-dim ВЕ 32.
-diš apm. (8195.1) in tyà-di$ DB 1.65 (with collective sg. masc. antecedent); nazy-di& DB 4.78, 18; paribarüh?-di$ DB 4.74; vikanah*-dis DB 4.77; avafà-di$ DB 5.17, 33; ava-di$ DNa 21, DSe 20°, XPh 19; 00-015 DNb 46f (with nt. antecedent); hau-di$ DSs 6° (with antecedents of different genders). Written as separate word in drauga diš DB 4.34 (with fem. antecedents); pasdva diš DB 4.35; avaba diš DB 4.36.
daiy DB 5.11, as separate word, properly vi? with wrongly inserted divider following; read viy- ататда with Wb. ZfA 46.55, see under mard- (not apm. with Kent, JAOS 62.278; not gen.-dat. sg. with Wb. KIA 73n, Bv. Gr. $845, Gray AJP 53.69).
-diy emphatic encl. particle: Av. zi, Skt. hi, Gk. encl. -xı in vai-xı ‘yes indeed’, of-xé ‘not at all’, pIE *ghi ($88, 5191.1). ufraštā-diy DB 4.69 (JAOS 35.351-2; not pron. apm., with Bv. BSLP 31.2.63-4, Gr. $845); hardly vasnd-[dily XPg 7f (despite Lg. 9.320; see under apiy); 7‘va-diy A’Sd 3 (JAOS 51.229).
didà- sb. ‘wall, stronghold, fortress’: N Pers. diz, pIE *dhióhà-, cf. Skt. dehi- ‘wall’, Gk. réxos,
191
NEng. dike, ditch (676.011, 588, §148.IV, 5166). Cf. also paradayadàm. й nsf. DB 1.58; 2.39, 44; 3.61, 72; DSe 46; DSf 42. didäm asf. DB 2.78; DSe 48°; DSf 54.
dipi- sb. ‘inscription’: Elam. tup-pi, Akk. duppu (5152.1): borrowed from Sumerian dup- (Ву. Gr. §282; hardly contamination of Jran. *ripi- = Skt. lipi- ‘smearing, writing’, with Sum. dup-, as taken by Pisani, Riv. Stud. Or. 14.320, as Skt. lipi- ‘writing’ indicates writing with ink rather than engraving on stone) 4:4] nsf. DB 4.90, 91f. dzpim asf. DB 4.42, 48, 70, 73, 77, 89; XV 22, 24. dipiyd lsf. (§179.V) DB 447.
dug- vb., see hadugá-.
Dubála- sb. ‘Dubala’, a district in Baby- lonia: Elam. du-ib-ba--- ($6, $107). Dubala пет. DB 3.79.
dūra- adj. ‘far (in time or space)’: Av. düra-, . NPers. dür, Skt. dürd- (5148.1). See also dü
=== leaf 226 ===
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
=== leaf 227 ===
24; 3.70; DPd 1; DPh 9; DSf9; DSp 1°; DH 7; XE 2; XV if; АНе1. [ma8]jiSta-ISàm] DB 5.27. mati&- lam asm. DB 2.20, 83; 3.12, 31, 57, 85; 5.6, 8, 12, 28; XPF 32.
Müda- (S166.IIT) adj. ‘Median’; masc. as sb. ‘Media’, a province of the Persian Empire: Elam. ma-da, АКК. ma-da-a-a, Gk. pl. Mado.
(1) ‘Median’: Mada nm. DB 1.49; 2.14°, 16, 18, 82; 418; DN 1°; APP 2, Madam asm. DB 2.21, 82; 3.30. Mada npm. DSf 50, 54. Майа] ipm. DB 2.23. MddatSuva lpm. DB 2.23.
(2) ‘Media’: Мада пзш. DB 1.15°, 41; 2.7; DPe 10; DNa 22; DSe 21°; Рб 8°; XPh 19. Madam asm. DB 1.47; 2.22, 28f, 48f, 68, 65 bis; 3.32f; 4.20. Méddam-ca DB 1.66f. Madaiy lsm. DB 1.84, 59; 2.15, 17, 22, 28, 66 bis, 72, 92; 3.77; DBe 10f.
tman- vb. ‘think’: Av. man-yele, Skt. mán- yale, Gk. utuova ‘(I bave thought of,) I desire’, Lat. memini ‘I remember’, pIE *men-. See also manah-. maniyary lst sg. mid. (§214, 5238.1) DNb 38. amaniyazy lst sg. imf. mid. (8214, 6233.11) DSI 3f. mantydhaiy 2d sg. subj. mid. (831, $222.11, §234.1) DB 4.39 (manl. . .); DPe 20 (maniydhay, $27, 552.11); DNa 38 (maniya- [...); XPh 47 (maniyaty, without the h*: $27, $52.VI, Lg. 13.302; Hz. AMI 8.66, ApI 243-4). maniyál|taty) sub). mid. (5222.1) DB 4.50.
^man- vb. ‘remain’: Av. man-, iterative pres. manaya- (8123, $215), Gk. pvo, Lt. maneo; prob- ably specialization of pIE *men- ‘think’ (see ‘man-) in meaning ‘remain thinking. amdnaya imf. DB 2.48, 63; amünaiya ($48) DB 2.28.
mana'uwin- adj. ‘mindful, wilful, hot-tem- pered’: from manah- + -win- (§155.V), cf. Lg. 15.170, JNES 4.47 (Hz. ApI 242 otherwise, wrongly). manauvis (remade from -07, $187) пэш. DNb 13.
manah- sb. ‘thinking power, power of will’ (Jn. Iran. Rel. $70; Kent, JNES 445-7, 232): Av. manah-, Skt. mánas-, Gk. дё ‘courage’, pIE *menos *menes- (5124.4, 4156.1). Decl., $185.I. See also manawin-, and -manis- with reduced grade in second syllable, in Ardumuni&, Harā- manik, perhaps [manis-. тапа&-са (8105) asn.
DNb32. manahà isn. (JNES 4.45; wrongly gen., Hz. ApI 240-2 and Sen 235) DNb 14.
méaniya- sb., probably ‘personal property’ in the houses; nt. adj. as collective sb., from тӣпа-, GAv. demüna-, Ау. nmana- ‘abode, house’ ($126), extension of root seen in Skt. dáma- ‘house’, Gk. 0óuos, Lt. domus. For varying views, see Tm. Lex. 116, with lit.; Gray, JAOS 21.17, 33.281-3; Bthl. AiW 1168; MB Gr. §261; Fay, JAOS 34.330-1. méaniyam-cé asn. DB 1.65.
+mamaita, see Atamatta-.
тауйта- sb. ‘doorknob’: Skt. maytikha- ‘peg’, perhaps to Skt. mi- (pres. minétz) ‘fix (as in the earth) ($100, 5148.11); ef. Hz. Ар] 258-9. mayüxa пзш. DPi; XPi.
mar- vb. ‘die’: Av. mar-, pres. miryeite ($122, $214), Skt. mriydte, Lt. moritur, pIE *mer-. See also uvdmarsiyu-, marika-, maria-, martiya-. amarijalü imf. mid. (835.1, $285.II) DB 1.43.
marika- sb. ‘person of lower rank, subject’, as shown by АКК. *"gal-la ‘menial’: contracted ($23.1) for *mariyaka-, deriv. of stem in Skt. (Vedic) márya- ‘young man, stallion’, ef. Skt. maryakd- ‘little man (said of a bull among cows)’, Phi. mérak (from *maryaka), Gk. шера ‘boy, girl’ (from *merjak-); ultimate root pIE *mer-, OP mar- (5122, 5146.11). Cf. Hz. ApI 251-3, Bv. TPS 1945.43-4. татка узш. DNb 50, 55, 59°.
Müru- sb. ‘Maru’, a town in Media (ef. König, RulD 71): Elam. ma-ru-i$, АКК. ma-ru-’. Mälrulš nsm. DB 2.22.
M árgava- adj. ‘Margian’: adj. to Margu-, with vriddhi ($126, $143.11, V, VI). Малаа nsm. DB 3.12; 4.24.  Mürgavaibis ipm. DB 3.16.
Margu- sb. ‘Margiana’, a province of the Persian Empire: Elam. mar-ku-i$, АКК. mar-gu-’, Gk. Mapyos, Мару:аиу (S31, $153.1). See also Márgava-. Margué пэт. DB 2.7; 3.11. Mar- gum asm. DB 4.25. Margaw lsm. ($114) DB 4.25; DBj 5f.
marta- ріс. as ad]. ‘dead’: Av. marata-,-N Pers. murd, Skt. mrid-, Gk. Вротос (for *Sparós, with vowel assimilat
```


## [2026-09-06T15:22:39.325Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^-est\" KLN_1966.txt | head; echo ---; grep -n \"^-ist\" KLN_1966.txt | head; echo ---; grep -n \"^most,\" KLN_1966.txt | head; echo ---; grep -n \"^best,\" KLN_1966.txt|head; echo ---; grep -n \"^first,\" KLN_1966.txt|head; echo ---; grep -n \"^last,\" KLN_1966.txt|head",
 "description": "Grep Klein for suffix and superlative entries"
}
```


### [2026-09-06T15:22:39.461Z] TOOL RESULT

```
13663:-est,  suff.  forming  the  superlative  degree  of  ad¬ jectives  and  adverbs.  —  ME.,  fr.  OE.  -ost,  -est, rel.  to  ON.  -astr,  -str,  OHG.  -isto,  -osto,  G.  -est, Goth,  -ists,  -osts,  and  cogn.  with  Gk.  -taro;, OI.  -iffha;  formed  orig.  from  the  compar.  suff. through  the  addition  of  a  suff.  beginning  with  t. See  compar.  suff.  -er  and  cp.  Anchistea,  Calista, Callisto,  kakistocracy,  protista.
13664:-est,  -st,  suff.  of  the  second  person  singular  in¬ dicative  of  English  verbs  (as  in  doest,  dost,  did- dest,  didst,  etc.)  —  ME.,  fr.  OE.  -ast,  -est,  -st, rel.  to  OHG.  -ist,  -ost,  -est,  G.  -est,  -st,  Goth,  -is, -os  -ais,  ON.  -r,  -ar,  -ir,  and  cogn.  with  Gk.-;,  L. -s,  OI.  -si,  second  person  sing,  endings  of  verbs, establish,  tr.  v.  —  ME.  establissen,  fr.  OF.  esta- bliss-,  pres.  part,  stem  of  establir  (F.  etablir),  fr. L.  stabilire,  ‘to  make  firm  or  stable’,  fr.  stabilis, ‘firm,  stable’.  See  stable,  adj.,  and  verbal  suff. -ist  and  cp.  stablisi!.
---
20006:-ist,  suff.  forming  a)  agent  nouns  from  verbs  in -ize  (e.g.  apologist,  dramatist)',  b)  nouns  de¬ noting  the  adherent  of  a  certain  doctrine,  prin¬ ciple  or  custom  (e.g.  socialist).  —  F.  -iste,  fr. L.  -ista,  fr.  Gk.  -10x7)4,  which  stands  for  -kj-xt)4 and  is  formed  fr.  -ia-  (ending  of  the  stem  of  the verbs  in  -IE[eiv)  and  agential  suff.  -xf)4.  Cp. -ism,  -ize.  Cp.  also  -ast.
20007:-ister,  suff.  —  OF.  -istre,  formed  fr.  original  -isle, on  the  false  analogy  of  the  word  ministre  (see minister).  Cp.  e.g.  chorister,  fr.  choriste,  fr. Eccles.  L.  chorista.
20014:-istic,  adj.  sufF.  —  L.  -isticus  (often  through  the medium  of  F.  -istique),  fr.  Gk.  prop,
26444:-ist.
---
24482:most,  adj.  —  ME.  mest,  mast,  most,  fr.  OE.  mxst, mast  (used  as  superl.  of  micel,  ‘large,  great, much’),  formed  fr.  OE.  ma,  ‘more’,  and  superl. suff.  -est ;  rel.  to  OS.  mest,  ON.  mestr,  Du.  meest, OHG.,  MHG.,  G.  meist,  Goth,  moists,  ‘most’, and  to  E.  more  (which  has  influenced  the  vowel of  ME.,  E.  most).  See  mickle  and  superl.  suff. -est  and  cp.  almost.
---
4827:best,  adj.  —  ME.,  fr.  OE.  best,  dissimilated  fr. betst,  rel.  to  ON.  beztr,  Du.  best,  OHG.  be^isto, MHG.,  G.  best,  Goth,  batists,  ‘best’,  OE.  batian, ‘to  become  better’,  bot,  ‘remedy,  cure,  improve¬ ment,  compensation’,  and  possibly  cognate  with OI.  bhadrah,  ‘favorable,  good’,  Avestic  hubadra-, lucky’.  Cp.  better.  Cp.  also  batten,  ‘to  grow fat’,  boot,  ‘advantage’.  For  the  dissimilation  of
---
14781:first,  adj.  —  ME.  first,  ftrsle,  fr.  OE .fyrst,  rel.  to OS.,  OHG.  furist,  ON.  fyrslr,  Dan  forste, OFris.  ferest,  ‘first’,  OFris .fersta,  MDu.  vorste, Du.  vorst,  OS.,  OHG.  furisto,  MHG.  fiirste, G.  Fiirst,  ‘prince’.  These  words  are  prop,  super¬ latives  formed  fr.  I.-E.  'prS-,  ‘before’,  whence
---
21194:last,  adj.  —  ME.  last,  dissimilated  fr.  latst,  con¬ traction  of  latest,  fr.  OE.  latost,  superl.  of  Ixt, adj.,  late,  adv.;  rel.  to  the  superlatives  OFris. lest,  MDu.  latest,  laest,  lest,  Du.  laatst,  OHG. Ie33ist,  Ut33dst,  MHG.  Ie33‘st,  lest,  G.  letzt,
```


## [2026-09-06T15:22:52.195Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nimport re\nlines=t.split('\\n')\n# map line no -> leaf index\nleaf=0; lm={}\nfor i,l in enumerate(lines,1):\n    lm[i]=leaf\n    leaf+=l.count('\\f')\nfor ln in [13663,20006,24482,4827,14781,21194]:\n    lf=lm[ln]\n    print('line',ln,'leaf',lf,'approx printed page',(lf-12)*2,'-',(lf-12)*2+1)\nEOF",
 "description": "Map Klein line numbers to leaves/pages"
}
```


### [2026-09-06T15:22:54.192Z] TOOL RESULT

```
line 13663 leaf 295 approx printed page 566 - 567
line 20006 leaf 443 approx printed page 862 - 863
line 24482 leaf 540 approx printed page 1056 - 1057
line 4827 leaf 99 approx printed page 174 - 175
line 14781 leaf 322 approx printed page 620 - 621
line 21194 leaf 466 approx printed page 908 - 909
```


## [2026-09-06T15:23:02.557Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nlines=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\n')\ndef near(ln,w=40):\n    for i in range(max(0,ln-w),min(len(lines),ln+w)):\n        s=lines[i].strip()\n        if re.fullmatch(r'\\d{2,4}',s) or re.fullmatch(r'\\d{2,4}\\s+[A-Za-z-]+',s):\n            print(ln,'->',i+1,repr(lines[i][:60]))\nfor ln in [13663,24482,4827,14781,21194,20006]:\n    near(ln); print('--')\nEOF",
 "description": "Find page-number markers near Klein entries"
}
```


### [2026-09-06T15:23:04.337Z] TOOL RESULT

```
13663 -> 13637 '542'
13663 -> 13648 '543'
13663 -> 13685 '544'
13663 -> 13696 '343'
--
24482 -> 24467 '1006'
24482 -> 24468 '1007'
24482 -> 24495 '1008'
24482 -> 24496 '1009'
--
4827 -> 4811 '166'
4827 -> 4823 '167'
--
14781 -> 14818 '596'
14781 -> 14819 '597'
--
21194 -> 21155 '866'
21194 -> 21180 '867'
21194 -> 21201 '868'
21194 -> 21221 '869'
--
20006 -> 20012 '820'
--
```


## [2026-09-06T15:23:12.843Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nlines=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\n')\nidx=[i for i,l in enumerate(lines) if l.strip() in ('34','35','36') and i<3000]\nprint(idx)\nfor i in idx:\n    print('===',lines[i].strip(),'line',i+1)\nfor i in range(idx[0]-30, idx[-1]+5) if idx else []:\n    print(i+1, lines[i][:300])\nEOF",
 "description": "Look at Klein page 35 region"
}
```


### [2026-09-06T15:23:14.858Z] TOOL RESULT

```
[1861, 1910]
=== 35 line 1862
=== 36 line 1911
1832 Aesopian,  adj.,  pertaining  to,  or  resembling  Ae¬ sop.  —  Formed  with  suff.  -an  fr.  L.  Aesopius, ‘Aesopian’,  fr.  Aesopus,  fr.  Gk.  A’tatono?,  the Greek  fable  writer.
1833 Aestas,  n„  the  goddess  of  summer  in  Roman mythology.  —  L.  aestas,  ‘summer’.  See  estival, aesthete,  n.  —  See  esthete, aesthetic,  adj.  —  See  esthetic, aestival,  adj.  —  See  estival, aestivate,  intr.  v.  —  See  estivate, aestivation,  n.  —  See  estivation, aether,  n.  —  S
1834 aethogen,  n.,  boric  nitrite  (chem.)  —  Lit.  produ¬ cing  heat’,  fr.  Gk.  alffo?,  ‘burning,  heat,  fire  , and  -yevr,;,  ‘produced  by’  (but  used  m  the  mod¬ ern  sense  ‘producing’).  For  the  first  element see  ether  and  cp.  next  word.  For  the  second element  see  -gen.
1835 Aethousa,  n„  a  genus  of  plants  of  the  carrot  fami  , (bot.)  —  ModL.,  fr.  Gk.  atflovax,  burning, fiery’,  fern.  pres.  part,  of  aiffeiv,  ‘to  light  up, kindle,  burn’,  whence  alffoc;,  ‘burning  heat.
1836 copper  rust.
1837 L.  aeruginosas,  ‘full  of  rust’,  ether.  This  genus  of  plants  was  prob.  called
1838 Aethousa  (‘the  burning  or  fiery  one’)  in  allusion to  the  bright  leaves, aetio-.  —  See  etio-. aetiology,  n.  —  See  etiology, aeto-  combining  form  meaning  ‘eagle’,  as  in Aetosaurus.  —  Gk.  Sexo-,  fr.  coexo 4,  asxo?, ‘eagle’,  which  stands  for  *af  texo?,  lit.  ‘a  large 
1839 Aetosaurus,  n.,  a  genus  of  reptiles  of  the  Triassic period  (paleontol.)  —  ModL.,  compounded  of aeto-  and  Gk.  oxupoq,  ‘lizard’.  See  sauro-. af-,  assimilated  form  of  ad-  before/, afar,  adv.  —  Formed  fr.  a-,  ‘on’,  and  far. afeard,  afeared,  adj.,  afraid  (archaic).  — 
1840 Derivatives:  affable-ness,  n.,  affabl-y,  adv. affair,  n.  —  ME.,  fr.  OF.  afaire  (F.  affaire), from  the  phrase  a  faire,  ‘to  do’,  fr.  L.  ad,  ‘to’, and  facere,  ‘to  do’.  See  ad-  and  fact  and  cp.  ado and  to-do.
1841 affect,  tr.  v.,  to  act  upon.  —  L.  affectus,  pp.  of  af- ficere,  ‘to  do  something  to’,  fr.  ad-  and  facere (pp.  factus),  ‘to  make,  do’.  See  fact  and  cp. affettuoso.  For  the  change  of  Latin  a  (in  factus) to  e  (in  af-fectus)  see  accent  and  cp.  words  there refer
1842 Derivatives:  affect-ed,  adj.,  affect-ing ,  adj.,  af- fect-ing-Iy,  adv.,  affection  (q.v.) affect,  tr.  v.,  to  make  a  pretence  of;  to  feign.  — F.  affecter,  fr.  L.  affectare,  ‘to  strive  after,  aim at’,  freq.  of  afficere  (pp.  affectus),  ‘to  do  some¬ thing  to’.  See  pre
1843 Derivatives:  affection  (q.v.),  affect-ed,  adj.,  af- fect-ed-ly,  adv.,  affect-er,  n.,  affection  (q.v.), affect-ive,  adj.  (cp.  F.  affectif,  fern,  affective), affect-ive-ly,  adv.,  affect-iv-ity,  n. affectation,  n.  —  L.  affectatio,  gen.  -dnis,  ‘a  striv¬ ing  after’,  fr.  affe
1844 affection,  n.,  feeling.  —  F.,  fr.  L.  affectionem ,  acc. of  affectid,  ‘a  permanent  state  of  feeling',  fr. affectus,  pp.  of  afficere ,  ‘to  do  something  to’. See  affect,  ‘to  act  upon’,  and  affect,  ‘to  make  a pretence  of’.
1845 Derivatives:  affection-al,  adj..  affection-al-ly, adv..  affect-ion-ate,  adj.,  affect-ion-ate-ly,  adv. affection,  n.,  an  acting  upon.  —  F.,  fr.  L.  affec- tidnem,  acc.  of  affectid.  See  affection,  ‘feeling’, affeer,  tr.  v.,  to  confirm  (Old  English  law).  —  AF. aferer,  cor
1846 ‘to  tax’,  fr.  VL.  *afforare ,  fr.  ad-  and  L.  forum, ‘public  place,  market’,  in  VL.  also  ‘market  price, tariff’  (whence  OF.  fuer,  ‘price,  tariff,  tax).  See forum.
1847 afferent,  adj.,  bringing  inward  (physiol.)  —  L. afferens,  gen.  -ends,  pres.  part,  of  afferre,  ‘to bring  or  carry  to’,  fr.  ad-  and  ferre,  ‘to  bear, carry’.  See  bear,  ‘to  carry’,  and  -ent  and  cp. efferent.
1848 affettuoso,  adj.  and  adv.,  with  feeling  (mus.)  — It.,  adj.,  fr.  L.  affectuosus,  ‘full  of  affection  or love’,  fr.  affectus ,  ‘love,  goodwill’,  fr.  afficere (pp.  affectus),  ‘to  do  something  to,  to  affect  a person  with  something’.  See  affect,  ‘to  act  upon  . affiance
1849 Derivative:  ajfianc-er,  n.
1850 affiche,  n.,  poster.  —  F.,  formed  fr.  d,  ‘to’  (see  a), and  ficher,  ‘to  drive  in  (a  stake  or  a  nail),  to stick,  fix,  fasten’,  fr.  VL.  *ftgicare  (contracted into  *ficcare),  freq.  of  L .figere,  ‘to  fix,  attach’. Cp.  It.  ficcarc,  OProven?.  ficar,  Sp.  hincar,  ‘to t
1851 affiliable,  adj.  — ■  Formed  fr.  next  word  with  suff.
1852 -able.
1853 affiliate,  tr.  v.  —  L.  affiliatus,  pp.  of  affilidre,  ‘to adopt  as  a  son’,  fr.  ad-  and  filius,  ‘son  .  See
1854 filial.
1855 Derivatives:  affiliat-ed,  adj.,  affiliation  (q.v.) affiliation,  n.  —  F.,  fr.  ML.  affWdtionem,  acc.  of affiliatio,  fr.  L.  affiliatus,  pp.  of  affilidre.  See  af¬ filiate  and  -ion.
1856 affine,  n.,  a  relative  by  marriage  (obsoi.)  —  OF. afftn,  fr.  L.  affinis,  ‘neighboring,  related  by  mar¬ riage’,  lit.  ‘bordering  on’,  fr.  ad-  and  finis,  ‘bor¬ der,  end’.  See  fine  ‘end’,  and  cp.  the  second element  in  chromaffin,  paraffin.
1857 Derivative:  afftne-ly,  adv.
1858 affined,  adj.  —  F.  affine,  fr.  OF.  afftn,  fr.  L.  af¬ finis.  See  prec.  word  and  -ed. affinity,  n.,  i)  relationship  by  marriage;  2)  close relationship;  3)  similarity:  4)  mutual  attraction, 5)  (chem.)  the  tendency  of  atoms  of  certain  ele¬ ments  to  combine.  —  F.  a
1859 affirm,  tr.  and  intr.  v.  —  OF.  afermer,  fr.  L.  af- firmare,  ‘to  make  steady,  to  strengthen,  corro¬ borate’,  fr.  ad-  and  firmdre,  ‘to  make  firm  or steady,  to  strengthen’,  fr.  firmus,  ‘firm  .  See
1860 affirmation
1861 04
1862 35
1863 firm,  adj.  F.  affirmer  and  E.  affirm  have  been refashioned  after  Latin  affirmare. affirmation,  n.  —  F.  affirmation,  fr.  L.  affirma- tionem,  acc.  of  affirmatio,  fr.  affirmatus,  pp.  of affirmare.  See  prec.  word  and  -ion. affirmative,  adj.  —  F.  affirmatif  (fern,  affi
1864 Derivative:  affirmative-ly,  adv. affix,  tr.  v.  —  ML.  affixare,  freq.  of  L.  affigere  (pp. affixus),  ‘to  fasten,  fix,  or  attach  to’,  fr.  ad-  and figere,  ‘to  fasten,  fix’.  See  fix  and  cp.  affiche. Derivatives:  affix-al,  adj.,  affix-ation ,  n.,  affix- er,  n.,  affix-tu
1865 affix,  n.  —  F.  affixe,  fr.  L.  affixum,  neut.  of  affix¬ us,  pp.  of  affigere.  See  affix,  v. afflatus,  n.,  inspiration.  —  L.  afflatus ,  ‘a  blowing, breathing,  inspiration’,  fr.  afflatus,  pp.  of  af- flare,  ‘to  blow  on’,  fr.  ad-  and  flare,  ‘to  blow’. See  blow,  v., 
1866 afflict,  tr.  v.,  to  distress.  —  L.  ajflictare,  ‘to  dam¬ age,  harass,  torment,  distress’,  freq.  of  affigere (pp.  afflictus),  ‘to  cast  down,  throw  down,  over¬ throw’,  fr.  ad-  and  fligere  (pp.  flictus),  ‘to strike’,  which  is  cogn.  with  Gk.  <pXf|3eiv,  ‘to press,  crus
1867 Derivatives:  affliet-ed,  adj.,  afflict-er,  n.,  afflict¬ ing,  adj,,  afflict-ing-ty ,  adv.,  affliction  (q.v.),  af- ftict-ive,  adj.,  afflict-ive-Iy,  adv. affliction,  n.  —  F.,  fr.  L.  afflictidnem,  acc.  of  af- flictid ,  ‘pain,  suffering,  torment’,  fr.  afflictus,  pp. of  affli
1868 Derivative:  affluent,  n.,  a  tributary, afflux,  n.  —  L.  affluxum,  neut.  pp.  of  affluere,  "to flow  to’.  See  prec.  word  and  cp.  flux. Derivative:  afflux-ion,  n. afford,  tr.  v.  —  ME.  aforthen,  fr.  OE.  gefordian, ‘to  further’,  fr.  pref.  ge-  and  fordian,  ‘to  further’ 
1869 afforest,  tr.  v.,  to  turn  into  a  forest.  —  ML. afforestare,  fr.  ad-  and  forestare,  fr.  Late  L. forestis  (scil.  silva),  ‘open  woodland’.  See  forest
1870 and  cp.  words  there  referred  to.
1871 Derivatives :  afforest-ation,  n.,  afforest-ment,  n. affranchise,  tr.  v.  —  Fr.  F.  affranchiss-,  pres.  part, stem  of  affranchir,  ‘to  free,  set  free,  liberate’,  fr. a,  ‘to’  (see  a),  and  franc,  fern,  franche,  ‘free’.  See ad-  and  franchise.
1872 Derivative:  affranchise-ment,  n. affray,  tr.  v.,  to  frighten.  —  ME.  afraien,  affraien, formed — with  change  of  prefix — fr.  OF.  esfreer, *esfreier  (F.  effrayer ),  ‘to  frighten,  terrify’,  fr. Gaul.-L.  *exfridare,  'to  put  out  of  peace’, fr.  L.  ex-,  ‘out  of’  (see  ex-),
1873 affray,  n.  —  ME.  afrai,  affrai,  fr.  OF.  esfrei  (F.
1874 effroi),  fr.  esfreer,  *esfreier.  See  prec.  word, affricate,  n.  ( phonetics ).  —  L.  affricatus,  pp.  of affricare,  ‘to  rub  against’.  See  affricate,  v. affricate,  tr.  v.,  to  rub ;  to  grate  on.  —  L.  affricatus, pp.  of  affricare,  ‘to  rub  against’,  fr.  ad-  and  fri- ca
1875 affright,  tr.  v.,  orig.  spelled  af  right.  Meta-
1876 thesized  fr.  afyrht,  fr.  OE.  dfyhrt,  pp.  of  dfyrhtan, ‘to  frighten’,  fr.  a-  (see  intensive  pref.  a-)  and fyrhtan.  See  fright,  v.  For  the  spelling  affright (with  double  /)  see  afford.  Derivatives:  affright, n.,  affright-ed,  adj.,  affright-ed-ly,  adv. affront,  tr.  v.
1877 Derivatives:  affront ,  n.,  affront-ed,  adj.,  ajjront- ed-ly,  adv.,  affront-ed-ness,  n.,  aflront-er ,  n.,  af- front-ive,  adj.,  affront-ive-ness,  n. affronte,  adj.,  facing  each  other  (her.)  —  F.,  pp.
1878 of  affronter,  ‘to  affront’.  See  affront, affuse,  tr.  v.,  to  pour  upon.  —  L.  affusus,  pp.  of affundere,  ‘to  pour  upon’,  fr.  ad-  and  fundere, ‘to  pour’.  See  fuse,  ‘to  melt’  and  cp.  confuse,  in¬ fuse,  refuse,  suffuse,  transfuse. afTusion,  n.  —  L.  affusid,  gen.  -o
1879 afield,  adv.  —  OE.  on  felda,  ‘in  the  field’.  See  a-, ‘on’,  and  field.
1880 afikoman,  less  exactly  afikomen,  n.,  a  piece  of matzah  broken  off  front  the  central  of  the  three matzoth,  used  at  the  end  of  the  meal  in  the Seder  service  ( Jewish  religion).  —  Heb.  aphi- qomdn,  fr.  Gk.  £7Uxci>piov,  ‘festal  procession after  the  meal’,  prop,  sub
1881 |
1882 i
1883 t
1884 i
1885 ‘banquet,  merrymaking,  revel’.  See  comedy, afire,  adv.  and  adj.  —  Formed  fr.  a-,  ‘on’,  and fire.
1886 aflame,  adv.  and  adj.  —  Formed  fr.  a-  ‘on’,  and flame.
1887 aflicker,  adv.  and  adj.,  flickering.  —  Coined  by Browning  fr.  a-,  ‘on’,  and  flicker, afloat,  adv.  —  Formed  fr.  a-,  ‘on’,  and  float, aflower,  adv.  and  adj.  —  Coined  by  Swinburne fr.  a-,  ‘on’,  and  flower.
1888 aflush,  adv.  and  adj.,  flushing.  —  Formed  fr.  a-, ‘on’,  and  flush,  ‘a  blush’, aflush,  adv.  and  adj.,  on  a  level,  even.  —  Formed fr.  a-  ‘on’,  and  flush,  ‘level’, afoot,  adv.  and  adj.  —  Formed  fr.  a-,  ‘on’,  and foot.
1889 afore,  adv.  —  ME.  afore,  aforn,  fr.  OE.  on  foran. See  a-,  ‘on’,  and  fore.
1890 a  fortiori,  adv.,  all  the  more.  —  L.,  from  the stronger  (reason)’,  fr.  d,  ‘front  and  abl.  of fortior,  compar.  of fortis,  ‘strong’.  See  a-,  ‘from’, fort  and  -ior.
1891 afraid,  adj.  —  Orig.  pp.  of  affray,  ‘to  frighten’, afreet,  n.,  an  evil  demon  or  jinni. —  Translitera¬ tion  of  Arab.  ‘ ifrit  (in  vulgar  pronunciation ‘ afrft) ;  name  of  an  evil  demon  or  monstrous giant  in  Mohammedan  mythology, afresh,  adv.  —  Formed  fr.  a-,  ‘on’,  
1892 Afrikander,  n.,  a  South  African  native  of  Dutch descent.  —  Formed  fr.  Du.  Afrikaner,  ‘African’, with  d  inserted  on  analogy  of  Du.  Hollander, Englander,  etc.
1893 aft,  adv.  —  OE.  seftan,  ‘behind’,  rel.  to  Goth. aftana,  ‘from  behind’,  prop,  superlatives  formed fr.  OE.  ref,  af,  of,  resp.  Goth,  af,  ‘of’,  with  the Teut.  superlative  suff.  -ta,  which  corresponds  to the  I.-E.  superl.  suff.  -to  (cp.  Gk.  npcoToc,  ‘first’, superl.  
1894 after,  adv.  and  prep.  —  ME.  after,  efter,  fr.  OE. sefter,  ‘behind  in  place  or  time’,  rel.  to  ON.  eptir , ‘after’,  aptr,  ‘back’,  Dan.,  Swed.  efter,  OHG. aftar.  Goth,  aftra,  aftaro,  ‘behind’,  and  cogn. with  Gk.  £rau--r(p-u>,  ‘farther  off’.  Suff.  -ter  has comparativ
1895 '  . .
1896 -te-me-  are  cogn.  with  OI.  -ta-ma  (e.g.  in sreshthatamah,  ‘most  brilliant’,  dntamah,  ‘next’), Avestic  -d-mo  (in  vahishtodmo,  ‘best’),  L.  -tu- mus,  -ti-mus  (in  op-tumus,  op-dmus,  ‘best’,  in- timus,  ‘innermost’).  E.  aftermost  (fr.  ME.  efte¬ meste)  was  influenced  in  for
1897 afterward,  afterwards,  adv.  —  OE.  eefterweard, compounded  of  sefter,  ‘behind’,  and  -weard, ‘toward’.  See  after  and  -ward,  -wards, ag-,  assimilated  form  of  ad-  before  g. aga,  agha,  n.,  a  title  of  rank,  esp.  in  Turkey.  — Turk,  agha,  ‘chief,  master,  lord’,  rel.  to  
1898 agama,  n.,  name  of  various  Indian  scriptures (Hinduism).  —  OI.  agamah,  lit.  ‘coming  up’, from  particle  a-,  ‘toward’,  and  the  stem  of  ga¬ mut  i,  ‘goes’.  OI.  a-  is  rel.  to  Avestic  a-  and  cogn. with  Gk.  £-  (e.g.  in  £-ff!Xeiv,  ‘to  will’),  tj-  (e.g. in  VPsnk,  ‘li
1899 Agama,  n.,  a  genus  of  lizards  ( zool .)  —  ModL., fr.  Sp.  agama,  which  is  of  Caribbean  origin. Agamemnon,  n.,  king  of  Mycenae,  leader  of  the Greeks  against  Troy.  —  L.,  fr.  Gk.  ’Ayapipvcjv, which  prob.  stands  for  *’Aya-pL8pcov,  lit.  ‘rul¬ ing  mightily’,  fr.  &yav, 
1900 agami
1901 aggregate
1902 a -^-enlargement  of  base  *me-,  ‘to  measure’.  See meditate  and  cp.  Medea,  Medusa  and  the  second element  in  Andromeda,  Diomedes,  Ganymede, agami,  n.,  the  trumpeter  (a  South  American bird).  —  F.,  fr.  Galibi  agamy. agamic,  adj.,  asexual  (biology).  —  Formed  with suff.  -
1903 Agamidae,  n.,  a  family  of  lizards  (zool.) — ModL., formed  fr.  agami  with  suff.  -idae. agamo-,  before  a  vowel  agam-,  combining  form meaning  ‘asexual’.  —  Gk.  ayocp.0-,  fr.  aya|jLO<;, ‘unmarried’.  See  next  word, agamous,  adj.,  cryptogamous  (hot.)  —  L.  agamus, fr.  Gk.  #
1904 Agapanthus,  n.,  a  genus  of  plants  of  the  lily  family (bot.)  —  ModL.,  lit.  ‘flower  of  love’,  fr.  Gk. ayaTtr),  ‘love’,  and  xvffoc;,  ‘flower’.  See  agape, n.,  and  anther.
1905 agape,  adv.  and  adj.,  gaping.  —  Lit.  ‘on  the  gape’ ; coined  by  Milton  fr.  pref.  a-,  "on’,  and  the  noun gape.  Derivative:  agape,  adj. agape,  n.,  love  feast  of  the  early  Christians.  — L.,  fr.  Gk.  aydcTtY),  ‘love’,  pi.  ayaTrat,  ‘love  feast’, fr.  dcyamxv,  ‘to  love
1906 Agapornis,  n.,  a  genus  of  parrots  ( ornithol. )  — ModL.  lit.  ‘bird  of  love’,  compounded  of  «yam], ‘love’,  and  opvic,  ‘bird’.  See  agape,  n.,  and  orni- tho-.
1907 agar-agar,  n.,  a  gelatinous  substance  obtained from  dried  seaweed.  —  Malay, agaric,  n.,  any  fungus  of  the  genus  Agaricus.  — L.  agaricum,  fr.  Gk.  dyaptxov,  ‘larch  fungus’, named  fr.  Agaria,  a  place  in  Sarmatia,  abound¬ ing  in  this  kind  of  fungi.  Derivative :  agari
1908 Agastache,  n,,  the  giant  hyssop  (bot.)  —  Gk.  ayde- cttxx’J?*  ‘rich  in  ears  of  corn’,  compounded  of ayav,  ‘much’,  and  osayyc,  ‘ear  of  corn’.  The first  element  is  of  uncertain  origin.  It  possibly derives  fr.  I.-E.  *mga-  and  is  rel.  to  Gk.  usyx;, ‘great,  large’; 
1909 agastric,  adj.  having  no  stomach  (zool.)  —  Form¬ ed  fr.  priv.  pref.  a-,  and  Gk.  vxo-nrp,  ‘stomach’. See  gastric.
1910 agate,  n.,  a  kind  of  chalcedony.  —  F.,  fr.  L. achates,  fr.  Gk.  iyi-rry,  which  is  of  ncertain origin.  The  name  of  the  river  Achates  m  Sicily,
1911 36
1912 as  well  as  the  name  of  the  faithful  friend  of  Ae¬ neas,  prob.  derive  from  Gk.  kyfj-ry.  See  Frisk, GEW.,  I,  p.  199  s.v.
1913 agate,  adv.,  on  the  way.  —  Formed  fr.  a-,  ‘on’, and  gate,  ‘street’.
1914 Agatha,  fern.  PN.  — -  L.,  fr.  Gk.  ayaOy,  fern,  of dyadic,  ‘good’.  See  agatho-.
1915 Agathis,  n.,  a  genus  of  timber  trees  of  the  pine family  (bot.)  —  ModL.,  fr.  Gk.  dyalHp,  ‘ball  of thread’,  which  is  of  unknown  origin, agathism,  n.,  the  doctrine  that  all  things  tend toward  good.  —  Formed  with  suff.  -ism  fr.  Gk. dyaffo?,  ‘good’.  See  agatho-. ag
```


## [2026-09-06T15:23:34.375Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in \"vahišta\" \"vahi.ta\" \"zōiždišta\" \"zoizdi\" \"nazdišta\" \"nazdi.ta\" \"fraēšta\" \"fraešta\" \"masišta\" \"mazišta\" \"kasišta\" \"spəništa\" \"spəništa\" \"druuišta\" \"drvišta\" \"āsišta\" \"asišta\" \"sraēšta\" \"sraešta\" \"tanjišta\" \"taniišta\"; do echo \"== $w\"; grep -n -m4 \"$w\" BRT.txt; done",
 "description": "Grep Bartholomae for Avestan superlatives"
}
```


### [2026-09-06T15:23:37.291Z] TOOL RESULT

```
Exit code 1
== vahišta
== vahi.ta
2476:—  inVerbindung  mit  x^'aFpat^j'a-.  Aaxaji5 Im  einem  Satz,  der  einem  vorhergehenden ..  kudaena  naiuaUt  mPiö.ao]anhd  (sd.)  Relativsatz  inhaltlich  koordinirt  ist '*': /ru- aesqm  sfaSfaHya  hizvöXt.ig.^^.  2)  auf.  zaiiUlmca  .  .  ytri/id  pourBsca  b»r3jayan ein  Relativum  als  dessen  Korrelat;  a)  ad- 1  nagciica  aiAka  yasäiti  zyänsi  (sd)  Y.  65. jektivisch  (vgl  i  aa) ;  yi  ätnm  . .  ava.-  11;  —  dämSH  urvalsl  .  .  yahmi  sp>ntä baraiti  . .  cvat  ahmäi  natre  mTsd»m  anhat  ^wil  mainyS  urvaisi  jasö  (sd.)  mazdä V.cV.81.  a)  Das  adjekt  Pron.  vertritt  |  :e/flir,7  oAmJ  W:4ä  »H7«aw,4fl  "bei  welchem laL  eius,  eorum  (s.  i  a  a):  yö  mam  .  ,  Ende  du  mit  .  .,  o  M.,  mit  XL,  bei  dem zinät  nöil  ahmi  nmäne  *z3naile  a^rava..'  du  mit  VM.  kommen  wirst"  Y.  4J.6{.;  — aal  ahmi  nmäne  .  .  "wer  .  .,  in  dessen  s.  noch  ahmya  3.  3)  Das  Neutr.  oder Hause  .  .,  sondern  in  seinem  Haus  , ."  Fem.  Sing,  bezieht  sich  substantivisch  auf Y. //.5f.;  —  mit  Numeruswechsel  "> :  _>'ö..  den  Inhalt  eines  Satzes,  bes.  Vordersatzes haom»nvandaita..frä..abyötanubyökaom5  (s.  Z  4);  a)  GSn. 'dess'  sva.  'dafür':  yatba- visäite  (sd)  baliazäi  "quilibet . .  laudat, . .  ■  väni  aiwi.sasto  .  .  eis  atiihe  asti  baSsazö eorum  corporibus  . ."  Y.  jo.  8.  b)  sub-  (sd.)  Yt7.^34;  —  AS  mim  ava>a  vjrj- stantivisch:  yi  maibyä  yaol  ahmäi  asSlt\nüiti  ya^a  ..  Sl  ait?he  asti  uzvar?z)m (sd.)   vahista  .  .    cöiüm  Y.  46.18;  19;  — j  (sd)  V-iS-^^f.;  37,  57,  68';  —  d:7tü  hi
3170:Uta  %rayam  vahiltanqm  amiiyS  (sd.) bw^ata  . .  "^raj/am  'tatiqm  aiwi'hyö  buyata V.J.V  17;  —  'y,i  maiyä  Uä  (APn.)  daniö vaxhnii  dagi5jsuitif(%A..)  Y._32.  4; —  aya *mainiv3  varatä  (sd.)  yi  dngvH  'tä Timyö  . .  Y.  30. 5 ;  —  yi  ..  yazli  apä  . . 'bm    mantüm    (sd.)    Y.j;^.  4.  a)    mit
4153:künftige  (jenseitige)  Leben':  disyäl  aAmai naire  oval  mlzd>m  parS.asn3i  °fguhe  vazd- fary  vahistahe  omAsusV. p. 44;  ij.8,  Y.55. a,  A.3.7.  d)  s.  zu  A  1  d.  3)  mit  a) vaAista-  Adj.,  b)  acisla-  Adj.;  a)  'das  beste Sein,  Dasein,  Leben;  Ort  des  besten  Daseins, Paiadies':  vahisfym  'hüm  asaonam  raoca- wAbb  (Stverz.)  vIspB.ci^iJ^rjm'^.g.iii  usw.; S./.a?;  —  nöithl. .  bi-at. .  vaAi/tJ  '»Aus ySmanayat  ahurahe  masdä  oval  vispanqm *aastpm  (sd.)  .  .  yat  srrfoi  daoiarihum P.  40, ;  Y,  (to.  1 1 ;  —  as^m  yS  ahurS .  .  aoi urune  uri'äsma  (sd.)  dalsayeni  vakUtimca 'hüm  P.  3S;  V. /<?.  2  9 ;  —  vazdvar»  vahisiahe 'ai^is  V.  5. 44;  —  vahistajtSs>m  (sd.) TohUtahe  'riASusV.  1S.6;  —  tarS p^r^tümcit hl  urvänmt  vahisl^m  'ham  fraparaymi  .  . it  vahistät  'tihapt  Y.  if),6;  7;  —  i'lsp^m asmanpm  vahtst^m  3  °hüm  baraiti'S.24; V.7.S2,  '^f^. 3.1"^;— vahistahe  'vASu^ vahistqm  ayanqm  yazamatde  Vr.  7. 2 ;  — yatJrS  paurrd  usshistaiti  paräiti  vahistahe •w>i7»/V.;Ä26;5.6i,Y.7/.i6,YLy.i34. P. 4:9;  —  vahislai  •r^heYyi.33;  —  ia^ä 'uhSuS  vaAistahyS  paourvJm  ku%S  (sd.) Y.  44. 3.  b)  'das  schlechteste  Sein,  Da- sein, Leben;  Ort  des  schlechtesten  Seins, HöUe':  vTspa  humaia  ..  vaAistpm*°tAlim"'' *asaiti  vispa  dusmala  acisl^m  *'ijhüm"^ *asaüt  FrW.  3. 2 ;  — ya^ääl  anhat  apsniim (sd.)  '»Aus  aaslS  ärygt'atqm  at  asäum vakistim  manö  Y.30. 4 ;  —  avi  lim  spayüt. . t)mS  .  .  äca  aastpm  äla  'hüm  ä  V.J. 35;
4820:—  zu' :  xshms  asamqm  unänö  pärayeinii . .  avi  garS  nmänam  V.  75.32;  —  x3  patti apqm  paräiti  .  .  a^ra  . .  V.  jj.  51;  — xraosyS-taraca  (sd.)  .  .  hv5  urva  paräiti par3.asnäi  amihe  yaia  . .  V,  13. 8;  —  ya- tärö  paurvs  us>hiUaiti  paräiti  vahiltahe atshsus  y .  iS.^d.  2)  'aus  (dem  Haus) gehen  auf  — ,  zum  Zweck  der  Verrichtung von-'  (Akk.):  *kat!lmS  timänahe  a'iauru- fi9m{sd.)  pärayäf^''  N.  /;—  para  paoiryö äiti  (näml.  a^aururitm)  para  bityö  aiti para  "hrityS  äiti  aita  paräyaiti  ycc^a gae'^äbyS  *k)nti  "es  geht  der  erste  (auf Priesterdienst)  aus  . .  der  zweite  . .  der dritte.,;  es  gehen  die  weg,  die  (zum  Schutz) für  den  Hausstand  da'gelassen  worden) sind"  N, 2 (?)"'; — katärsm  *ä'irava  ctiauru- n>m  Vä  parayat  galiaiiqm  vä  asp^nns (sd.)  avat  N.^;  —  katärS  a'^aurun?rn ''parayat  nSirika  vä  nmätiSpaitiH  väi yezica  vä  ga^hä  vTmä  (sd.)  *katarascit ''parayat  N.  5;  *5";  —  *cvät  ''aiwtstXm parayap  'irixsapar>m  .  .  yS  haoys  (sd.)  . . paräiti  nsit  .  .  anaiwistim  (sd.)  ästryanti N.  4.  a)  mit  haca  und  Instr.:  cval  .  . äiirava  a'iaurumm  haca  ^gafi^äbis^para' yat  N,  4-  3)  'sich  an  etwas  (Akk.) machen':  yö  nar)m  ..  kasyat»he{%d.)  sanhai daoaili  vl^va  aval  hava  xraiwa  paräiti "—  wissentlich  mit  voller  Absicht  macht  er sich  daran— "V,  15- 2.  4)  'hingelangen zu  — '  sva.  'sich  verschaffen':  ffi.j(Akk.),. kaine-.tarS  äaxit^m  pärayät  tarS  ap»mca urvarqmfa  yezica  . .  tarS  (sd.)  daxst>m paräiti  . .  "nicht  soll  das  Mädchen  heim- lich sich  die  Regel  (wieder)  verschaffen, heimlich  sich  Wasser  und  Kraut  verschaf- fen .."  V.i5,9f.
== zōiždišta
== zoizdi
28149:zoizdiSta-
== nazdišta
== nazdi.ta
2782:{upa  mit  Akic.);  para  n  *gaosp}nta  ...will,  cupiti  potens,  glücklich':  am^rstäiti baodasla  urvän^mca  */rai^ämahi  nazdista  '■  *asaonö  urvä  °sö  "in  Ewigkeit  (wird)  die upa  >war}sta  raoca  V.34.  [Seele    des  -4Aanhängers    glücklich    sein"
6259:—  antar)  i^ädamaü  'iiionis"  (IP.)  Vr.  21. 3.  'P-S^i  —  °Ai<JW  (VS.)  pu%ra  kava vJstaspa  ^y\-53',  45  (wo  'säum);  —  ratui 'iava  V.ö.ii;  Vr.5.6;  —  'laonB  aiahe raiwü  rafufritlm  Y.  22.3,  71. 3;  — yqmca bipaitistänqm  '/aonim  Y.  13,1;  —  °/at»ti- nqm  ärmaiti.paoiryanqmY .21.2; — Jiaisa- nqm  . ,  sasnSgüsqm  . .  'iaonqm  '/aoninqmca ..  nabänazdistanqm  ..  -saonqm  'iaoninamia .  .  af&rapaitinqm  'iaonqm  .  .  ai'i:ryanqm 'iaonqm  .  .  naram  'iaonqm  .  .  näirinqm 'saoninqm  Y.  26. 4— 8;  gf.^,  Vr, /.  3';  — ä'irai'antm  'iavamm  ,.  rdialitär^m  °iara- mm  .  .  västrXm  fiuyant^m  'iavanjm  .  . nmänS.paitlm  °!avan»m  .  .  nmänB.pa'inUn 'iavanjm  (statt  fem.)*>  aiaAe  raiüm  Q.4 7  f.;  7—9";  —  zaotanm  'savamm  ,- sraoiävar3zim  'iavafum  G.  J.  5;  5*;  — Aai^yavarxsqm  'iaonqm  haOiyavamtnqm -saoninqm  V.17.14;  14*,  G.J.7';  —  saoi- yantqm  'iaonqm  Y.  ;4-i.  *i~-li  Vr-5-i. 22,1,  Ytii,i7;  —  äsna?a  mana  'iaonqm äsna/a  mana  saoiyantqm  Vr.  /i.  3 ;  — fravasays  .  .  yamca  staoyB  (sd.)  'iävaoyj {DP.)YU3.88(f);~ädaAyunqm/a  'iaonqm .  ,  uzdaAyunqmca  'saonqm  Vr.  16.  z;  — irtrüuiqm  'iaonqm  .  .  Jvantqm  'saonqtn Y,  24. 5 ;  —  vup>m  'Savamm  h3iit»mca bavantimia  bü^anipmca  Y.  2^4,  Vr, /Äs;
17822:sae^antätvirshraynaiY.  26. 10; — gSuicä hudätahs  gayehyäcä  mard^nB  .  .  °itm  Y. y-  7;  2j.  a,  26.  S,  Yt  13.  87;  —  «ÄM^ zar^uStrahe  ipitämahe  asaons  -sie  Y.  6S. 22;  3. 2,  4. 23, 16. 2,  23. 2,  24-  S,  7'-  2-  Vr. /ö,  2,  YtÄ  2,  J_J.  87,  Vd.(?;  —  ahe  nars aSaonS  'Jtm  yazamaide  yS  asmffj^ativä nqma  Yt,  /. 30;  13. 95 ff.  (oft),  Y. 23. 2, 26. 5% FrW.  2. 1,  3;  —  hvSuyä  asaonyä  'sim  Yt ''5-^39!  '39f-'*;  —  kanyä  *va}>uis  asaonya [. .]  °slm  Yt  13.  141 ;  141  f.'°;  —  auch  dem AÄM.  und  andern  Gottheiten  wird  eine Fr.  KUgeschrieben**':  vispanqmca  anAqm paoiryanqm  'Sinqm  .  .  °sm  avqm  yqm ahurahe  masda  .  .  °iay5  .  .  ya  ampsanqm spintanqm  .  .  yqmca  ährö  urväzistake  .  . yqmca  sraohhe..yqmca  alnSyqmca  apH.. YtJ^.  80-86;  Y.26.2i.,  V./»?.'4; — äyese yelti  *ä  *fravaM<y)'^  ahurahe  mazdä  am»- sanqm  sparUanqm  . .  Y.  25. 2 ;  —  gaom  (statt Gen.)  agvJS-dätahe  urunB  °Sim  S.2.  I2;i2; —  sogar  den  Fravalay  selber  (!) :  aSäunqm "sinqm  uyranqm  .  .  paoiryjJkaisanqm  'si- nqrrt  nabänazdistanqm  'ünqm  '/ayU  xihaiä ayantu  ahmya  nmaneYt.i3.1s6.  A)/ra- vaHnqm  a)  (näral,  mä)  heisst  der  i .  Monat  im Jahr^:  asäunqm  'sinqmY.i. 11.  ß)(näml, ayar?)  heisst  der  19,  Monatstag:  asäunam 'sinam  uyranam  S.j.  19;  vgl. 2. 19,  Y.10.5. •)*Nach  dem  GrBd.  (s,  DsT.  ZA.  3.  500, Blocket  RHR.J2. 104)  ist  der  Mensch  aus  fünf Bestandteilen lusammengesetit:  ian,yän,  nmän, äiinai  aad /ravakr.  Vom  letzten  heisst  es; y>ti- vahr  an  i  pcs  i  Öhrmazd  i  :^aiäl,  und  über  sein Verhältnis  mm  fiß/ö»  wird  geiagt:  ruvän  S/ra. vakr  pativast,  ku  iän  rm/ä»  marnjcmtan  ne  tiniän. S.  noch  DkB.  269  {218.  6):  io  (fravahr)  haf  lan yut  bavtt  lan  hil  lör  u  aiär  mänri.  Die  Schaffung der  fr.  (bei  West;  "prolotypes,  primary  ideas of  the  good  creations")  ist  nach  Bd.  /.  8, 34.  1 zu  Beginn  des  ersten  Mitleniums  erfolgt;  nach 2.  10  f.  entscheiden  sie  sich,  'lan  tariaiihä'  gegen die  Welt  der  Driig  zu  liämpfen.  Über  ihre,  ins- besondere  kiiegeiischeTäligkeitalsSchutzgeister und  Manen  gibt  das  ihnen  gewidmete  Yt  13 Auskunft.  Ihre  Zahl  wird  Yt.  13.  59  ff.  auf  99  999 eingegeben,  vgl.  jcludra-*)  and  Mx.  4g.  16,  52. 23,  29;  weniger  bestimmt  Yt.  13.  64,  66.  All- jährlich während  der  letzten  fünf  Tage  der sechsten  (letzten)  Jahreszeit  und  der  sich  an- schliessenden fünf  Schalttage  kommen  dieManen, ihre  frühere  Heimat  zu  besuchen  (Yt.  13.  49) und  werden  dann  besonders  gefeiert  (s.  hantas- pa%niae<iaya-)ii).  Vgl.  noch  Cld.  Totenverehrung 48,  BahadoorN.  D.  Khandalawala  Cama  Mem. Vol'  205,  JN.  GIrPh.  2.  643,  SÖDEftBLOM  RHR. 3g.  229,  373,  La  vie  future  7.  Das  Nichtauf- treten  der  fr.  in  den  (eig.)  Gä%äs  (s.  unten  No.  l) ist   bemerkenswert;    zum  Teil   aber   entspricht
18569:•  j.  nabä-nazdista-  Adj.  'der  verwandt- schaftlich nächststehend  e,  nächstverwandte'; ~i:ris  satifii  hana.ci^anqm  (sd.)  ttarqm 'lanqm  para.baraiti  V.  4.  5 ;  —  'tarn  fil . . *'asihrai/i  N.p;  —  kS  ht  .  .  ai^rapaiü-
== fraēšta
== fraešta
== masišta
== mazišta
== kasišta
== spəništa
== spəništa
== druuišta
== drvišta
== āsišta
== asišta
== sraēšta
== sraešta
== tanjišta
== taniišta
```


## [2026-09-06T15:23:46.921Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '28140,28160p' BRT.txt | cut -c1-600; echo \"=== headwords ===\"; grep -nE \"^ *[a-zA-Zäöü.ç?3>'’ə]{2,14}i[SsšŠ]ta-\" BRT.txt | head -60",
 "description": "Inspect BRT zoizdista and superlative headwords"
}
```


### [2026-09-06T15:23:49.296Z] TOOL RESULT

```
•)  Bd.  13.  a  ;  köf  i  sarlaz  »  ki  asl  täf  i  maiaü. Ich  nehme  an ,  dass  vor  4sl  -  am  Anfang  der Zeile  in  K  -  /a  iusi  i  ausgefallen  ist,  das  dem aw.  pär^ittarim  arüS  entspräche.  Der  Mtimüa- Berg  erhebt  sich  im  I]intergmnd  über  dem  vor- gelagerten 2.-Gebirg.  Die  Lage  des  Zfr'  wird Yl.  rg.  I  ebenso  bestimmt  wie  die  der  Ifaraiti ; vyl.  unter /«/dya-.
Et.  und  Bed.7  Wohl  Komp.  mit  oder  Ableit aus  z>iid-.  —  ')  Oder  Stamm  'at-7    S.  No.  a.
—  >)  Oder  GS.  lu  'm-?;  S  3S6-  —  J>  So  nach der  unlergeschri ebenen  /'Jsini/Iesung  in  K. Der  Pahlaviteit  hat  zrdli,  worin  man  da* letzte  Zeichen  fälschlich  für  'und'  genommen hat.
■  j.  z«r98ö.k3r9ta-  Adj.  'das  Herz  heraus- schneidend': taica  narS  g?r^SJifntäs- (sd.)rtr  '/Jj(NPm.)A  V.7.24.
Komp.  mit  CS.  loa  1.  Glied.  —  Pü. :  dil  hrrf-
«iinömand.
•  j.  zöiinav-,  g.  zöiS«nav-  Adj.  (fem. "«£-)   'zusammenschreckend,    schaudernd,
dby  Google
i693
zoizdiSta-
zi  2  A
1694
bebend',  vor  Frost:  avi  lanuye  'nuye(,DS{.) V,7.  70;  —  mit  Gen.  (Abi.)  der  Ursache: aodinscä  "»S  (NDm.)  r/Jss{sd.)  Y.jr.  12.
Za  ioiia-.  —  Pü.:  ialäifn,  ialaiäien,    (lu  V.)
erl.!  «man. ■  j.  zöizdiäta-  Adj.  'der  schau derhaßeste, abscheulichste',  von  den  xrafslra-:  ajaitala 'laca  .  .  xrafslra  Yt. 21.  \\  —  ya\ia  -fäis xrafstrsis  V.  7.  a.
Snperl.     lu     einem    V.    *sSiU5-    'schaudern
machen',  vgl.  zöilnav-  and  vasdä- :  xtasdüla;
—  Pü. :  *baiaklum,  erl. :  rtmatilum.
•  ].,  g.  z^O«-  n.  'Geburt,  Entstehung; Erzeugung,  Erschaffung':  y3  ..  häirinnqm "hat  ^gariwqn  yaozdahäid  Y.  65.  2;  — fra  t!  '"kintca  vaxsak»mca  .  .  frasnaymi V.2/.6;  —  zara%uitrahe  .  .  yehe  '"haiia vaxsaS^a  urvassn  äpS  .  .  Yt  y.  93;  93', V.  2t.  4;  —  atfhSu^  '^si  paouruyekyä  "bei  | der  ErschafTiing  des  ersten  Lebens"  Y.  1 48.  6;  43.  Si—para  Ups  . .  dät?hsit  para  ' nari  .  .  •%3t  Y.  ig.&;  —  kasnä  '^a  pa/S  ; asakya  *paouruyö  "wer  ist  durch  Er- schaffung der  Vater  des  A.,  der  erste?" Y.44-3.  [Y.^Ä
KompE.  —  Zum  V.  tzan-,  aus  ar.  'saniha-, S  13.  —  Pü.:  zät,  (lu  V.  31):  zäyisn,  Ua  Y. tg)i  dahisn.
•  j.   zahyamna-  Adj.,  PPi7(Fut.)M,:  s.
=== headwords ===
7440:asiSta-  338
20129:masiSta-
21787:'yöiSta-  1398
23343:'vahiSta-  a  1400
28149:zoizdiSta-
```


## [2026-09-06T15:23:59.425Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -noE \"[a-zA-Zäöüçə'’.\\*3>?]{2,16}i[SsšŠ]ta-\" BRT.txt | awk -F: '{print $2}' | sort | uniq -c | sort -rn | head -60",
 "description": "List all -išta- forms in Bartholomae OCR"
}
```


### [2026-09-06T15:24:01.152Z] TOOL RESULT

```
      3 vaAista-
      3 irista-
      2 vahista-
      2 tbista-
      2 pairiSta-
      1 *zrazdiSta-
      1 zoizdiSta-
      1 zöista-
      1 znöista-
      1 yöiSta-
      1 'yöiSta-
      1 vozista-
      1 'vista-
      1 vispe.mazista-
      1 'vahiSta-
      1 'vaedista-
      1 vaedista-
      1 ssviSta-
      1 ssriSta-
      1 spsnista-
      1 'sista-
      1 raodas.pairista-
      1 ranjiSta-
      1 räkitista-
      1 pouru.iSta-
      1 paitLyüiäiSta-
      1 o.räinista-
      1 Onwaxäista-
      1 oasiSta-
      1 nazdista-
      1 masiSta-
      1 manS.vista-
      1 maftiSta-
      1 kasiSta-
      1 Japiista-
      1 'irista-
      1 ioaxsista-
      1 häviSta-
      1 hamista-
      1 häiSista-
      1 düraefraiSta-
      1 darvziSta-
      1 *darista-
      1 ''darBziSta-
      1 dahmö.pairista-
      1 äzista-
      1 avacirista-
      1 asiSta-
      1 aoJiSta-
      1 a>ääiSta-
```


## [2026-09-06T15:24:14.578Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for pat in \"asiSta-\" \"masiSta-\" \"kasiSta-\" \"nazdista-\" \"spsnista-\" \"ranjiSta-\" \"ssriSta-\" \"vispe.mazista-\" \"'vahiSta-\"; do echo \"######## $pat\"; grep -n -F -- \"$pat\" BRT.txt | head -3 | while IFS=: read ln rest; do sed -n \"${ln},$((ln+3))p\" BRT.txt | cut -c1-900; echo \"  --- (line $ln)\"; done; done",
 "description": "Print Bartholomae contexts for superlatives"
}
```


### [2026-09-06T15:24:16.818Z] TOOL RESULT

```
######## asiSta-
asiSta-  338
yehyäcä  hStmmyäsaitl  (sd.)  mi^aAyä  yais ksi  'va  (NPn.)  Y.j^^.i.
Ableit.  {mit  Vrddhi^)  aus  i>r>iav-.  —   ai  vgl.
ärjava-  n.  —  Pü.:  afi/ai.
  --- (line 7440)
^''2^/?'  'p}-^^-    ,  ,,    „  •  j.  kasiSta-  Adj.  a)  'der  kleinste':  'iaÄe
»ri3vB  jrat9m}m    tbists  .  .    maotmane  .  .
•  j.  karsnaz-  m.  Name  einer  iranischen  masUtahe  V>.  10;  JÄ  44PUZ.  b)  'der Yz.TsM%\  yasmaoyö  parö  'nazS  {'^'2.)  hvira  geringfügigste':  yö  n��  matiltim  yasmm baon  sn-isfa  Yt.  13.  38.                                    yasäite  'titn  ^yasnat  frsyatät  (sd.)  Yt/.  24;
zEt.  und  Bed.  vll.  ai.  krina-  Adi.  'ichwart'.  ^            -   r^i  i,                               .     J  -     \      1
  --- (line 9387)
•  j.  oasiSta-  Adj.  (fem.  'tä-)  'der  am besten  zu  Grunde  richtet';  a)  mit  Akk.: jaynista  'la  (VS.)  tayüm^a  hazanuharamca Yt. /2. 8.  b)  absol.:  artrahe  maittySui 'tqm'^  dalnqm   äalvayasnanqm   Y.  72.  11.
Supeil.  lum  V.  *nai;  mit  kaus.  Bedeatung(t). —  Fü.;  fehlt.  —  ')  Lesung  unsicher.
•  j.  nasu-kaäa'  m.  'Leichenwärter' *>:  alte
°sa  nisAiiaita  avavat  haca  iristaHhyö ya%a  %rigäim . .  kam  aSe  matsma  baray»n yaÄbyd  alte  'ia  frasnyante  var>sasca  ta- nBmca  V.  A'.  1 1 ;  —  aSaliqm  'ianqm  Vd. 4;  —  yat  altahe  'ia ''  avi  hl  bansnümla yaozda%äiti  frasnayäiti  var»s»m  vä  tanBm vä  Vd.4-
  --- (line 18789)
######## masiSta-
masiSta-
fangreich':  andvJm  .  ,  'sttam  .  .  yS  asti avavaiti  masS .,  V.  ö^.  3 ;  —  tarn . ,  »maita 'siti  ädlahi  Yt.JO.30;  —  äaya..xratüm pascalta  •sitim  matanhm  afiairi.a'isntn (sd.)  Y.  62. 4.
Ahleit.  ant  mos- ;  Tgl.  naiäa-'}.  ~  Pü. :  mai. ~  ')  Vgl.  noch  lu  p.  "Maiäaam.  —  >)  Vgl, fti.  iarit-  und  kaHla-'i
•j.inasijtta-,p.ma9i$ta-Adj.'dergrÖsste'j i)  der  Ausdehnung  nach :  kasistahe  .  . mahmahe  .  .  °tahe  3r>svS  frat3m3m  iMsü V.  6. 14.  2)  U  dem  Rang  nach:  a*wra*- matdä  . .  hyer  -tJ'  baganam  D.4.1;  X. 6. 1.  a)  bes.  'der  Oberste'  cinerTruppe: AyO*  tnadaiitiva  *t^  akJ'  Bh.  2. 6;  —  hyJ' avahyä  karahyS  °ta*  äk^  Bh,_j.  11;  11, 2.4;  —  avamiam  'tarn  akunavam  Bh.2. 6;  I4,^.6j9,I4,  5.1,4; —  avam  'tarn akunavcl'ts  "den  machten  sie  zu  ihrem Obersten"  Bh.j.3,  5.1.
  --- (line 20129)
######## kasiSta-
^''2^/?'  'p}-^^-    ,  ,,    „  •  j.  kasiSta-  Adj.  a)  'der  kleinste':  'iaÄe
»ri3vB  jrat9m}m    tbists  .  .    maotmane  .  .
•  j.  karsnaz-  m.  Name  einer  iranischen  masUtahe  V>.  10;  JÄ  44PUZ.  b)  'der Yz.TsM%\  yasmaoyö  parö  'nazS  {'^'2.)  hvira  geringfügigste':  yö  n��  matiltim  yasmm baon  sn-isfa  Yt.  13.  38.                                    yasäite  'titn  ^yasnat  frsyatät  (sd.)  Yt/.  24;
zEt.  und  Bed.  vll.  ai.  krina-  Adi.  'ichwart'.  ^            -   r^i  i,                               .     J  -     \      1
  --- (line 9387)
######## nazdista-
•  j.  nabä-nazdista-  Adj.  'der  verwandt- schaftlich nächststehend  e,  nächstverwandte'; ~i:ris  satifii  hana.ci^anqm  (sd.)  ttarqm 'lanqm  para.baraiti  V.  4.  5 ;  —  'tarn  fil . . *'asihrai/i  N.p;  —  kS  ht  .  .  ai^rapaiü-
,.  ästryeitiJ  *ts  N.  ij;  —  'lanqm  ioa asaonqm  aiaoninqmca  ahümid  datnqmca  . . Y.2(J.6; — vUpanqm  akmya  nmane  'tanqm paraÄristanam  .  .  fravasayS  "von  allen verstorbenen  Ifächstverwandten  dieses Hauses  .  ."  \.26.T,  j.  18.
Ar.  'iiahAä-naaiisIlia-  eig.  'der  der  Familie, Verwandtschaft  nächtt  stehende*.  Ar.  'nahhä. f.  'Nabel;  Familie';  ahd.  naba  'Nabe',  letl. naba  'Nabel';  vgl.  näfa-  m.;  Richter  1F.  p. 309.  —  ai.  näö/iSafdiitha-n  m.  EN.  (Ableit. ans  ar.  'naih').  —  Pü. ;  nabänaiiHsl  (Transskr.), SQ.:  ncaänvävanikaläh  'novem  familise  pro- pinqui'»).  —  ')  nahlf  (BB.  12.  105}  eiistirt nicht.  —  »)  Nach  V,  13.  i  ff.  wären  das: l)£hem,  2)Kinder,  3)  Geschwister.  4)  Gross- eitcm.  5)  Enkelkinder,  6)  Kinder  der  Ge- schwister, 7)  Geschwister  der  Eltern,  8  und 9)  deren  Kinder  und  Enkelkinder.  Vgl.  nava- naplya:
•  p.  nabukudra£ara-  m.  EN.  eines  baby- lonischen Fürsten  (Nebuhadnaar,  Sohn  des Nabonedos) :  1  martiya^  bäbiruviycr  nadt'ta- bairc^  .  .  avaUa  adurujiy<^:  adam  'ra* aptiy  hya*  nabunailahya  pu^''e^  Bh.  r.  ifij 18,  19,  4-  3,  Bh.  d;  —  iyam  arax^  aduru-
  --- (line 18569)
######## spsnista-
yäsä  (sA)  *'inySui ..  spmtakyä  ..  ^yao%anä Y.  28.  i'\  a)  mit  vanAav-  konkret von  dem,  des  Geist,  Sinn  gut  ist,  in  koU. Sinn:  *°inySuUä  *var3hSus  vlsfä  data spintahyäca  nsrsi  syaohana  . .  Jiairigaiig (sd.)  y.  34-  2'>.  2)  im  jAw.:  oAmäi rtaetnäi  ,  .  yahmäi  .  .  mihrS.drux^  na^a Hnyu  faiti.faite  Yt  10.  19;  —  mit  sptrUa-. spmtat  haia  °nyaoi..aihm  Hhnm  FrW./o. 40.  n)  'Geist'ahBezeichnungunkÖrpei- licher  Wesen;  I)  von  dem  Geist  Verstorbe- ner; nur  im  gAwr.:  yahrä  'inyu^  dngvats anqsat{Sg.io^^  o.) par3  Y.^.j.  2) von Gottheiten;  a)  im  gAvr.;  mit  spsnista- von  Asa,  Arm.,  VM. :  at  ahura  h)S  'inyUm iara%ui^trS  v?rmif(sd.)  miuda  yasß  Hscä sfSnistö:  aäm . .  armaitii . .  vohä . .  manatifiä ^.43-  i6j  —  voaAitart  Stars  vsi  ahurahya masdh  ahT  'myuS  vSi  (sd.)  ahyä  sjifniits aMY.s6.3;
yoaAAM.,m\tmainyaoya-.  ahura fu  mazdä .  .  'inySus  mainyaoyehe  Y.4-  7";  —  mit sp3ntS.t}ma-.  ahurahe  matdä  ..yS  nS  data ,  .  ys  Hnyus  sp3nts.tsml}  Y.  /.  j ;  Yt.  j,  1 2 ; —  mitJ^yatWa-:  ahura  mazda  'inyffCVS.) splnisia  datar»  gal&anqm  astvaitinqm (Stverz.)  aiäum  V.  2.  i  usw.  2)  insbes. von  den  'beiden  Geistern',  die  das  gute und  das  böse  Prinzip  vertreten  *' ;  im  g  Aiw. : al  la  'inya  (ND.)  *paouruyF  yH  ySmä  (sd.) . .  manahiÜH  vacahilä  fyao%anSi  hX  vahyS akim{sAi)ca  Y.30.  3;  —  atcS  hyat  ts  hlm °twyS(ND.)  yaj«a^i«(Sp.  501  o.)paourBTm dasde  goEmcä  a/yait{m(sd,)ca  Y.,90. 4;  — anhSusiSp.ioC  u.)  °i«>fl(AD.)  ^paountyi yayä  spanyi(sd.)  UitT mravat ySrn  angnm. nSit  Hä  manä  .  .  nSit  varana  (sd.)  . .  ha- laitUf  Y.  45-  2 ;  —  ayä  *'iniv3  varatä  (sd.) yS  dngvä  aäitä  vnr^�
33. 6;   spftita    'inyB    sraotü    matdä
ahurlf  Y.45.6;  —  /ä  da  •inya  sptniä matdä  . ,  aSrJ  . .  vldaitlm  (sd)  ranSibya Y.47,6;  5;  —  yoAml  sfimia  irws  *inyB
  --- (line 19882)
######## ranjiSta-
•  j.  ranjiSta-  Adj.  (fem.  •/«-)  'der  sich am  leichtesten  bewegt,  der  flinkste';  /ra- vaiii  yazamaide  . .  rtvls  . .  °ia  Yt  JJ.  75 —  fravasayS .  .ya  .  .'tä  fravaamnanqm Yt  13.  26;  —  mtrrjohe  .  .  vän^nahe  . . yB  vayam  asH  äsiUs  HS  fravasimnanam
Superl.  zu  ra-jeni:  —  ai.  vgL  lighi}tha-  Adj.  — Npu.j  fehlt.
•  j.  ranjyö  Adv.  'leichter,  fliDker*:  r* ^vazainte  (/?)'>  m^B  "flmker  fahren  sie dahin,  die  sich  an  dir  berauschen"  Y. 10. 19.
ASn.  aas  *r>njyah'  Adj.,  Kompar.  in  rajoB-. —  VgL  aj.  rä;hiyai;  laghiyat-  Adj.;  li>w. ranjk  'leicht'  (Gewicht),  tlink*  (Ross).  —  Pä.r ii^i.  —  >)  Fehlt  wegcD  des  vonasgehendea •//;  vgl.  vorher.
  --- (line 25445)
######## ssriSta-
J575  üb- mit  ä  —  ssriSta-  'ST^
faiS..:^aiai^(iA.)  \.34.ii;  —  vafdäJ  \.^i.\^-,32.ft;  —  diidi  mäi . . awLmOii läsnanqm  fsd.^  jqm  . .  ilttl  aii  a^rS  hainsti  ipfniää  maiitrü  wuttdJ  briHrntj' Y.4A. 3.  yüiti  manaoAä  r-t-Aä  •mihi  "scfafnk  mir..
mit  a  Verheisseii,  in  Aassicht  stellen':  Uasterblicbkdt  und  Wohlfahrt  durch  den at  tH  atrim  . .  *ajjil)m'> ..  stzi  rapafäi  beüigsten  Gast,  o  J/i,  Kiaft  mid  Bestand ctirä-ovaahjm  (iA.)  ¥,^4.4.  durch  YM.    bei    dem    Richtereprach"    V,
mit /rJ  i/rS)  'lehren,  ofiienbaren',  mit  5J-7-  4»  'Reden,  Spreeben  lüber  Je- dopp.  Akk.:  ahyä  xraiü  JrS  mi  s3stü  mandes)':  ^J  nar^m  aSaraiam  ain^.z^ifs- vahistä  "durch  seine  Weisheit  lehre  a  mich  «Jt  .  .  kavfanhs  Isd.)  'ahäi  da-iäiti ,  V. das  Beste"  Y.  45, 6; — '/rtuasta-.       a)mit   /J- a*'-  5f    Tled^    Woti":    *ambm9wf
  --- (line 26247)
######## vispe.mazista-
•  j.  vispe.mazista-  Adj.  'der  grösste allen':   ra%wqm    °ianqm  yDt  fanti  aiahe ratavB  A.  j.  1,
Komp.  mit  (pron.)  NP.  im   t.  Glied.    —  Vgl.
•  j.  viape  ratavö  (NP.)  'alle  Ratat/,  Be- zeichnung eines  Buchs  des  Awesta;  ge- wöhnlich ^Visparad"  genannt  (s.  dazu  GIrPh. 2.  5):  mä  eis  m!  ätihqm  taokranqm  fra- tmharät  ya  nüil  staotanqm  yesnyanqm Jma/S  (sd.)  V  r*  Yt.  JO.  I2a'>.
■)  VII.  sind  die  beiden  letiten  Wörter  V  r* Glosse.
  --- (line 24480)
######## 'vahiSta-
'vahiSta-  a  1400
'tsm  manS  (Sp.  11380.)  Y.J7.7.  a)mit Dat  oder  Gen.  'für  -':  agn/ta  (sd.)  vacä sSnghamahX  aiibyö  .  .  atcil  a^byö  'ta Worte  . .  denen  sehr  genehm  . ."  Y.
I ;  —  sraota  *g}ul.llii  'tä  .  .  ävannä vTcihaAyä {sd.)  Y.30.  2'>;  —  at  fravaxfyä atghsus  akya 'ttm  "ich  wil!  reden  von  dem, was  fUr  dieses  Leben  das  beste  ist"  Y. 45.4;  46.10;  —  tqtn  dalnam  ya  Aatam (Sp.  268  o.)  'ta  Y.44.10;'—  zuglefch mit  ergänzendem  Inf.:  vacS  srßidyai  (sä.) Ayat  marf/aHiyff  'ttm  Y.45.  S;  —  mit Gen.  part:  ai  vaidimnäi  'tä  säsnanqm (sd.)    yqm   .  .    sastl  .  .   ahuru    Y.48.'y,
ya  hatqm  (Sp.  368  o.)  yyad^ananqm •tä  hyai  übdifyä  ahubya  Y.^jj.  3;  8  (Sp. 718  o.).  a)  bes.  in  eschatologischem Sinn:  hyai  äamä  *tl yajsn  (sd.)  mlidl  Y. 49-  9;  —  .iflSa  avA}u/  'takyä  paourvTm ka%s  (^t.)  saidyai  Y.44.2;  —  yahaca
  --- (line 23343)
```


## [2026-09-06T15:24:41.561Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -noE \"[a-zA-Zäöüçə'’.\\*3>?]{0,10}(iSta|ista|iäta|isla|iita)-\" BRT.txt | awk -F: '{print $2}' | sort -u | grep -iE \"^(dr|dv|du|sr|ss|ta|tq|as|oas|fr|na)\" | head -40; echo \"=== search sraesta ===\"; grep -n -iE \"sraes|srae.ta|'der schönste'|schönste\" BRT.txt | head -10; echo \"=== drv ===\"; grep -n -iE \"drviita|drvista|'der gesündeste'|gesündeste\" BRT.txt | head -10; echo \"=== tanjista/tqjista ===\"; grep -n -iE \"tqjista|tanjista|tqziita|'am festesten'\" BRT.txt | head",
 "description": "More Bartholomae superlative searches"
}
```


### [2026-09-06T15:24:43.574Z] TOOL RESULT

```
asiSta-
fradariäta-
fraoirisiäta-
naidisla-
nazdista-
oasiSta-
ssriSta-
ssviSta-
=== search sraesta ===
7051:•  j.  ^i  Inteij.  des  Anrufs,  vor  dem  Vok.: äi  a^äum  zaräiultra  Yt.  1.26,  /o.  137,  ig. 53,  V./<V.i,  aPUZ.,  Vyt.  72;  —  ai  sraesa rtg-a  Y.  57.  28,  V./(V.  22;  —  äi  mi%ra vouru^aoyaoite  Yt.lO.42,  93,  115;  —  äi äuzda  artra  mainyö  V.  ig.  9.
10198:nät/rä  1)  Inkoh. 'aufwachen':  h3  s^af- iiä'ia  frayris>mnS  H.  /.  13;  —  x^a/ttät /rayris;»Nnauqmll.i.i3\ai.  2)Kaus. 'aufwecken': rt'fl.^Mi'  dahmät  aoxte *frii'i^  mä narf  *gärayBis  yat  ratus  frilsis  *äjasäl'^ vXiaiti  dim  frayrärayS  nOitfrayräyräyäti aliff  ratufris  *yd  jayära  "Ein  D.  sagt  zum andern:  'Weck  mich  auf,  Mann,  wenn  die Gebetastunde  kommt'.  Der  iibemimmts ihn  zu  wecken,  bringt  ihn  aber  nicht wach.  (Dann)  ist  der  r.,  der  wach  war" N.  ig;  —  sraesB  a^'Ö  aotn  mtnyim  fra- yrsrayeifi  pars.dari  tiqma  V.  /tS'.  33,
12944:'zu  Gesicht  bekommen,  erbUcken,  er- schauen': caräitii  .  .  yqm  it  yava  carSiti- aqm  hhrpa  sraiitqm  dädansa  ". ,  das  an Gestalt  schönste  von  den  Mädchen,  d^s ich  je  zu  Gesicht  bekommen  habe"  H. 2.10;  Y.5.  i;  —  ttla  kal  %ws  dansäni matuuca  vokü  vaidfmnS  "o  A.,  werde  ich dich  erschauen  und  den  VM.  als  ein wissender"  Y.  2Ä5";  —  a/a  vahisia  .. darjsäma  %W3  pairi  %WS  jamyama hanam  %wa  Aaxma  (sd.)  Y.  60.  la";  — kumqsdrä  (sd.)  asä  yecä  yä  raocübls  dan- jflöljSKM.)  urvasa^.30.\.-,  —  dar?sat'^ F.  i4;  —  darsstä.'.  a)  vom  visionären Erschauen:  hyaf  hufä  aipAsui  zaiiSi  dan- sjm  paourvim  "als  ich  dich  zuerst  er- schaute bei   der  Schaffung   des  Lebens"
16687:•  j.  'bawray-m.'Biber',  f. 'Biberweibchen': yat  asti  'ris  sragsta  yä^a  yat  asti  gaonS.- t?ma  'ris  öavaili  upäpö  "da^  Biberweibchen ist  am  schönsten,  insofern  es  am  dichtesten behaart  ist;  der  Biber  ist  ein  Wassertier" Yt.5.129').
18219:•  j.  fräyah-  Adj.  (fem.  •yehl-)  1)  'der mehrere,  plus':  nait  aevB  .  .  dva  . .  %rayS .  .  'yanAs  .  .  fra/md  (Sp.  360  u.)  P.  44'^ —  caiti  na  agvahe  pasvB  (sd.)  ..  a^a  dva aha  hryqm  .  .  an/qm  *kahyacit  tdoa *°yaaAqm  '*  ". .  ebenso  bei  zwei,  ebenso bei  drei  . .;  (je)  eins  dann  bei  jedem mthr"  N.  6y,  —  paniasatbl/c'a  . .  *'yJbTs- /a/(sd.).'o">  aAmäjVr.S.i.  a)  'mehr  als geaugiZnvieV :  daAmff  daUya  draona . .'^•yii^ draonä  s^arS  mdhatte  N.  30;  —  daitrm  gSui dragnS ..  *'y?^>  \daitlm\g3its  draonö^ups.- u^mns  N.  jj.  a)  n,  als  SubsL  'Überschuss, Überfluss':  tu  bairyeinte  yaisqm  dim  'ys voAunqm  ".  .  bei  denen  schon  Überfluss vongutenDingenist"  V.j.ag.  2)  ohne kompar.  Bedeutung  'sehr  viel,  sehr  zahl- reich': aal  dl/  ava^jayamahl  'yeAts{APL) Y.  4.  S-  a)  ASn,  °yS  als  Adv.  zur  Ver- stärkung des  Superlativs*':  yaiAe  aztm  *ys tbaysntqm  sraätim  susruye  va^m  "der unter  denen,  die  (mich)  rufen,  die  schönste
19041:US  (Sp.  426  M.)  asraesyanam  tanunam  asahe  yS  n°  jyölämi^ä.)  hanar}  vtnasti . .  olnatshB .  .''vlZaiti'^  'S.  15;  N. ^2,  Nik.i;  —  «"  «S  . ,,  Y.^/.  15;  —  yöi  n*  aspm  mainyanta  (sd.) aSvan'  dva  n°*  ..asahe  tf  asayS  fräl3fiii'>  ■\.34-^\  —  yallam  n'  kvarstäis  vai  (sd.) (Sp.  360  u.)  V.44;  V.J5. 48»;  —  n°  na  duivarstä  ¥.49.4;  —  tacit  . .  ya  n°  va
19305:j.  Hmöi  N.  8-,  lid  nmänäl •  j,nrnäna-,g.,j.''dflniana-'',j.'V;'«ff»a- n.  'Behausung,  Haus',  von  jedem  zum Aufenthalt  für  Menschen  (Götter)  und Haustiere  dienenden  Bauwerk,  sowie  auch von  dem  zu  einem  Anwesen  gehörigen Gebäudekomplex;  I)  von  Wohnungen  fUr Menschen  (und  Götter):  yanyS buyä  'nshu ma^yäkanqm  Y.  6i.\;  —  ahmi  *ne  ya^ m!^ayasnBi^{Stve.Tz.)  V.5.45;  —  vasö.. mazdayasna  ahe  'nahe  myasd>m  äaihyäril V,  &22J  —  ätacäni  sünm  'mm  drvatS Yt-5'  3S;  —  <Mi  'tarn  yim  ^alpaihjm Yt5.63;  62;  —  ha%ra  'ni  avastaya  ka~ t>mca  /raslamb>m{s,ü.)Si  ..  V.  2. 26;  — yat  bä  paiti  nä  a/ava  'mm  uedasta  ä%ra- vai  gaomavat  nsirivat  ..  V.J.  2;  15.  ai; —  mürnm  . .  ylF  stunä  v^ärayeiti  iirtsi- mitahe  'nahe  Yt /O.  28;  30;  —  tBm..°na inasilä  ..  dahähi  YtJO.30; —  sraohm .. yS  driyaolca  . .  amava£  'mm  hüm.täsH  Y. $'j.  10;  —  as>m  yS  ahurB  masda  . .  yas> tat  'npm  ahnmm  srirtm  raoximm  frs- d^rirsrym  V.  22.1^;  \.Sy.2i;  —  iaiiihe ka^he  apayisire  'mm  htitaite  hi^ättm  Yt. 5.  loi;  —  aliqm  "nä  hvihätä  .  .  hUhfUe Vti7.  8;  V./j.  4g;  —  hubaotUl  ba^aite °mm  yeAhe  'ne  asis  varmhi  . .  psta  mda- ^aite  Yt.ij.6;  ij.107;  —  iha  ml  tum (nämL./4/fl)  hamJaranuha  *antary.ar^?m •nahe  srJrahe  Ytzj.öo;  jj.  147, 156';  — alU  . .  ramyai  i%a  upa  tmai  °mm  yat ahüiri  Y./O.i;  6'o.2,  Yt  14.41; — vainti ahmi  'ne  sraesS  Y.  tfo.  5;  Yt7j.  52,  FrD. /3;  —  vUfa  'na  sraoiö.psta  yazamaide  Y. 57-34)  —  damt  ha^a  ahmüt 'nät  ..rhyeja ■  •  ^'yeyenti  yejihe  *'?ya*'  sraoh  . .  astf paiti^ants  Y.57. 14;  /o.  7;  —  mä  yave imat  'mm  i^'annS  frazakXi  Y.60.  7;  Vyt 5;  —  xihsii  äfrlnstttu  {jis-viA.  fravas<rfS) ahmya  'ne  vattuhim  asim  . .  xsnüiä  para- yantu  haca  ahmst  'nät . .  msüm  gtnzänä pärayantu  haca  ahmst  'nät  ahmSkfm^a mazdayasnanqm  Yt  13. 157;  Y.  2j.  3;  — aai  ahmSi  'näi  dähäiti  gluica  vqhwa  vlra- nqm/a  Yt.!0.  a8;  —  äat  ..  ahe  'nahe/ra- pi^iws  gäu^  .  -  Y.  j.  3 ;  —  t^it  ahmi  'ne *sänaite  ä^rava . .  äat  ahmi  'ne  Sayhnte  da- hahaca..Y.ii,6;  — /raddhsi  ahe'naheY. 52.4;  4.5,  Vr./J.  13*;  —  'n?m  hS  manyaita paraJa%B  V.  ;*.  28;  ■ —  (8«  miknäi  daiva *aipi.jaiti  'ne  aiAhai  gundayai  (sd.)  V,  3.
20173:—  at  fravaxsya  vTspanqm  Htm  "ich  will reden  von  dem,  der  der  grösste  ist  von allen"  Y.  4S-  6;  5?-  8;  —  ahur?m  mazdqm , .  'hm  yazahm  Y.  16.  1;  —  ahurS  mazds yB  'ts  yazatanqm  yB  vahiltB  yazatanqm Yt.  77. 16;  70.  142 ;  —  ätarl . .  'ta  yazata Ny.  j.  4.  b)  in  Verbindung  mit  vaki^ta- imd  sral^ta-:  ya%a  nS  'täsca  vahistasSa sraeitasia  a/ayS  ^nnavante  Y.S2. 3;  —  as/a zadhranqm  'taca  vahiitaca  sralliai^a  N.£^;
20174:—  dämqn  .  .  y3  kätqm  'tala  vakistaca sraeitata  Vr.  72. 4;  —  vJspanqm  narqm näirinqmca  .  .  yüi  Aiiti  .  .  'tau  vahiitaca srasstaca  V. 2.  27;  27;  —  tat  nqma  .  .  yat tl  asti  'tim^a  vakilttmca  sralit?mia  Yt. 7.  5;  —  damqm  mäzdayamim  .  ,  ys  .  . *tacä  vahiitaca  sraiitäca  Y.  72, 9 ;  —  airya- mamm  mq%ranqm  'hm  .  .  vahist>m  .  , sralttfmYi.^.^; — siaota  asahe  yat  'taheta vahistahela  sraiUahe^a  Yt7_j.  gi;92;  — /ravastm  avqm  yqm  ahurahe  ,  .  'tqmüa vakiHam^a  sragäqmäiY.26.a;  —  ahurahe mazdi  .  .  Haheca  vahÜtaheia  sraläahe^a Y.  1. 1.
23166:1)  'fahren';  i)  Irans.;  a)  von  Zugtieren sva.  'ziehen*:  srao&m  ..yim  ..  aurvanlS .. vatmti  Y.57.  37;  Yt.  ;o.  68,  47,  77. 12;  — aurvants  . .  vazimna  yim  vohüm  sraohm Y. 57.29;  —  s.  noch  'vazäna-,  b)  vom Wind;  a'hra  pascaUa  vazaite  vätB  .  . varymca  maiy>mca  fyanhumta  avi  ('hin zu  . .')  asä  . .  YL<y,  33.  c)  vom  Fahrer, sva.  'lenken':  y&  *paourvS  väsim  vataite VL5.  11;  —  s.  noch  Absol.  2)  intrans.; a)  von  Zugtieren:  ahmya  väse  vatänte ("a^warS  aunian/s"a.ndtmW^enz\eheTi,," YtJO.iag.  b)  vom  Fahrer;  Akt  und Med:  dahmS..  banmnS  vä  vazimnS  vS ". .  reitend  oder  fahrend"  N.  J7 ;  —  talints . . barmtB  .  .  vaz?nts  nSit  framanyenU  (sd.) "laufend  . .  reitend  , .  fahrend  . ."  Yt  10.  ao; —  fravaiayB  . . ya  aojislä  vaz>ntqm  Yt 13.  a6;  —  ahmya  *vasa  (sd.)  vazsmna (NSf.)  Yt  5.  n ;  —  dasimm  hl  upa  ar^m vazaite  .  .  sraess  Ytro.  100;  100,  laö', 70;  —  vTspS  hl  ypa  *ar^j  vastnti yä  apB  Yt  10.  100;  —  mi^r)m  ,  .  ys vUpähu  harsvShu  .  ,  vataite  ^ar»nS.dä YtJO.i6;  107;  — yat  d^ra  para.jasaiti vaztmnB  (näml.  mihrB)  Yt.70.  loi;  86, 74. 2 ;  —  nixiata  ahmät  vazata  atarl YtJO.  127.  c)    von    Heer  und   Volk
=== drv ===
=== tanjista/tqjista ===
```


## [2026-09-06T15:25:16.030Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### PHD\"; grep -nE \"^(wahi|ardwahi|zišt|zšt|tang|naxust|mahist|kahist|kāhist|drust|frāy|frēh|nazd)\" PHD.txt | head -30; echo \"### PHD grep loose\"; grep -nE \"\\b(zišt|naxust|mahist|kahist|drust|wahišt)\\b\" PHD.txt | head -20",
 "description": "Grep MacKenzie for MP forms"
}
```


### [2026-09-06T15:25:16.098Z] TOOL RESULT

```
### PHD
444:mahist [msst!, mhst! | M mhyst, N ~] greatest. makóg [mkwk' | M mkwg, N mako(k)] boat. mālīdan [m’lytn' | N ~] = muštan.
507:naxust [nhwst' | M nxwst, N ~} first.
3935:tangible giriánig, griftarómand.
5356:drustéw dz društāwāz društīh društ
5461:drustih drust
5462:drustabed
### PHD grep loose
125:did ... add other. add dig |YTMAL < А *?{т?1 | N di] yesterday. delete *drém ... (read balgam) drubušt ... add protective. drust [drw(d)st' ... duš-čihr ... add ill-natured. duš-nām [-n^m | (M dwjn'm), N ~] add ill-famed. dušwār [dwáw?l | (M dwjw'r), ... ékanag ... for obedient read loyal, faithful. ~th : for obedience read loyalty, faithfulness. for Farrēbāg... read KFarrēbāy [pinb(^)g] ... frayad |pl(y)d^t' | N faryad] ... delete M pry'd. frazand |prz/znd | ... frusag ... add M prwšg. garódman ... read | P grdm'n. gazdum |gcd(w)m, gzd(w)m |... guftàr ..., ~th : add eloquence. hambar |hm-, hnb] |... add  hamest |hmyst'] whose good and bad deeds weigh equal. ~(ag)an |-(k)^n'] limbo, the neutral station between heaven and hell. delete hammist ..., ~(ag)an ... handarz ... add M °’ndrz. hammoxtan, hammoz-, ~i8n : add learning. hast |TWMNYA < A tmny ; ... add hūg [HZWLYA < A hzyr’; hwk' | M hwg, N xiig] pig. add hūkar(ag) |hwkl(k') | N xükara] porcupine. (not hedgehog) add *huzārag [hwc’lk | N хијага) little, small, few. !jadag ... add fortune. jüdan ... | M jwwdn, jwy- ... add karawuš [kl wš| N ^] wine-press. delete karbunag ... read karbūg |klpwk', klbwk'| lizard. kardagān ... add service (ofthe gods). delete karxēš vds
316:drón yaštan: consecrate the sacrificial bread. drēš [410] mark, branding; punishment. ~ag [-k!] *desolation. drēšīdan, dro$- [d/w$-ytn'] brand. drēūšom [dlwšwm] mark. droz-, v. druxtan. drózan [dlwen! | M, J drwzn] lying, liar. ^h: falsehood. drubušt [di(w)pwst'] fortress. ~ih: defence, fortification. drüdan, *drün- (HCDLWN-tn! < A У hsd | M ача, (dwr-), N durüdan, diraw-] reap, mow. drust [drw(y)st' | (M dryst), N durust] right; well, healthy. —Ih: righteous; health. drustabed [drwystpt'] chief physician. društ [dlwšt' | N durust] harsh, rough, severe. ~ih: harshness, severity. ~-Awaz, ~-éwaz [-p'c, ~yw’c] harsh-spoken. druwand [dlwnd | M drwnd] evil, sinful, unrighteous. ~īh: sin, unrighteousness. druxtan, dróz- [dlwhtn', dlwc- | M drwxt, drwz-] lie, deceive. druz [dlwe | (P drwj)] demon. айа [dwt! | M dwd, N ~] smoke. düdag [dwtk! | N —a] family. dudigar [dtykl | M dwdygr, N digar] second. duj-, = duš-. ~-daft [dwsdpt'] ill-breathing, short of breath. ~-dānāg [dwšd”7?k!] ignorant. ~-dén [dwšdyn' | M dwjdyn-] of evil religion. «=dēys*rīh [dwsdwyslyh] the evil eye. ~-gand (dtwsgnd | P dwjgnd] stinking. ~-gandih: stench. dum(b) [dwm(b') | N ~] tail. ~dmand [-'wmnd) tailed. ааг [LH YK'! < А rhyq; dul | M dur, N ~] far, distant, remote. durgar [dwlgl | N ~] carpenter. dusraw [dwslwb!] notorious, dishonoured. ^Ah : notoriety, dishonour. duš- [dws- | = M] ill-, evil-. ~īh: evil, wickedness. ~-абаһ [dw??^ Es] foolish, stupid, ignorant. ~-абаһіһ : foolishness, stupidity. ~-arz [2 ic] worthless. 7--Ca&m [-cém] envious. —-Ca$mih: envy. ~-tihr [-cyhl | M dwfcyhr] ugly, hideous.
422:kabk [АрА! | N ~] partridge. ~-anjir [acyl | N ~] a kind of francolin. kabód [kpwt! | N ~] grey-blue; pigeon. kabótar [kpwil | M kbwtr, N ~] pigeon. kāč [с | N kāš(ki)], ~ ka: would that, if only. кадар [01А] game, joke. кадар [ktk' | M kdg, N kada] house. ~-banig [-b'mwk! | N Radbanü] mistress, lady of the house. ~ig [-yk'] domestic; servant. ~-xwaday [-hwty | P gdyxwd?y, N kadxudā] householder, master of the house. kadām [ktm | M kd?m, N кийат) which, what. c--iz-é(w) [-c-H D] whichever. kadar [kt] who, which. 7-iz-é(w) [-c-H D] whoever. kaf [kp | N —] foam, slime. kaf-, v. kaftan. kafč [kpc | N ~] ladle, skimmer. ~ag [-А! | N ~a] spoon. kafš, ~ag [kps, -k! | N Аар] shoe. ~gar [-k/ | N ~] shoemaker. kaftan, kaf- [kp-in' | P kft, kf-] fall. kah [TBNA < A tbr | N ~] chaff, straw. kān-, ~i§n, v, kāstan. _ kahas [kts | М khs] channel, sewer. kāhēnīdan, káhén- [R'hyn-ytn!] decrease, lessen (tr.). kühidan [P hytn! | N ~] = kastan. kahist [ksst'] least. kah-rubāy [Ара | N —rubá] amber. kahwan [khwbn' | M qhwn, N kukan] old. kākom [RP Rkwm | N ~] stoat. ~ i spéd: ermine. kālbod [Аро | (M k*/byd), N ~] body, shape, form. ~ӧтапа [-wmnd] corporeal. kam [km | M kmb, N ~] little, small, few; v. kem. kam [Em | = M, N ~j will, desire, purpose. kàm-, v. kāmistan. 1катаб [k?mk! | N kama] kinds of gruel, or soup. ?kümag [k?*mk! | N kama] = kam. «-hanjām [-hnc’m] gaining one’s end, successful. -~-hanjamih: success. „ūmand [-wmnd] willing(ly), desirous. ~-widar [-wt?l | N kām-gučār] successful, independent. ~-xwaday [-Awt^y] independent, absolute. kamal [kml | (M km?7)] head (daevic). ~ig [-yR!] chief (daevic).
444:mahist [msst!, mhst! | M mhyst, N ~] greatest. makóg [mkwk' | M mkwg, N mako(k)] boat. mālīdan [m’lytn' | N ~] = muštan.
507:naxust [nhwst' | M nxwst, N ~} first.
593:tan-bahr [żn'Þ’ hl] physique. tand [tnd | = P] faint, languishing. ~ih: faintness, langour. | tan-drust [tn'drw(y)st! | N ~] healthy, whole. ~ih: health. tang [ing | = M, N ~] narrow, tight. ~ih: narrowness; distress. tanig [tn'yk! | N tani] bodily, corporal. tanigard(ig) [tnykrt(yk)! | M inygyrd] corporeal. ` tanīhā [tn'y/? | M tnyP?, N tanha] alone. tanómand [tn wmnd | N ~] corporeal. “АҺ: corporeality. tan-tdhmag [tn'twhmk'] (sap) of plants. tanuk [tnwk! | N ~] thin, shallow, tanür [tnw] | M tnwr, N ~] oven. tar [LCDr! < A l-sd; tl | M tr] over, through, across. ~ kardan, ~ menidan: abuse, despise. -tar [-z# | (M -dr), N ~] suffix forming comparative adjectives. tar [2] | M гу] darkness. tarāzēnīdan, tarāzēn- [tcyn-ytn!] weigh. tarázüg [tPcwk! | (P tPzwg), N tarazü] balance, scales; astr. Libra. targ [tlg | N ~] helmet. tarģumān [tigm?n! | M trgwmn] interpreter. tarig/k [PIyk! | M гуур, N tárik!] dark. ~th: darkness. tarist [¢/st'] = tar. tar-mānīh [t/m’nyh] perversity. tar-menišn [tImynin! | N tarmanist] perverse; contemptuous. 7h : perversity; contempt. tarr [t/, LC Dr (in error, v. tar) | N —] moist, fresh. ~ag [tik! | N ~a] vegetable. tars [2/5 | M trs, N ~] fear, respect. tarság [ts k! | M trs’g, N tarsā] Christian. tarsāģāh [15(?)/?5] respectful, reverent. ~ih: respect, reverence. tarsidan, tars- [tls-ytn' | (M tyrs??dn), N ~] fear, be afraid. tarwénidan, tarwēn- [t/zvyn-ytn! | M trw-] overcome, conquer. tas [25 | N ~] die (for gaming). tasum [tswm | = M] fourth. tāšīdan, tāš- [O i-ytn!'] cut, cleave; create. taSkanag [tšknk!] under-shirt. tašt [tšt' | N ~] bowl. tāšt [021] *certainty. ~ig [-yk'] certain. tāwān [1?(d)w’n' | N ~] compensation, obligation. taxl [t?% | (M thr), P txl, N talx] bitter.
680:žzēn [zyn! | N zin] saddle. zēn-abzār [zyn'pe!l | N zinafzár] horse-armour. zēnāwand [zy>zond] alert, vigilant. zēndān [zynd?n! | = M, N zindān] prison. «bān [-p?*x! | N -ban] jailer. ~ig [-yk! | N -i] prisoner. zënënidan, zënën- [zynyn-ytn!] look after, preserve. zēnhār [zyn)?] | N zinhàr] protection. zénig [zynyk!] armed. *zibāl [zb | N zībāl] swift (horse, etc.). zih [zyh | N zih] bow-string. zindag [zy(w)ndk! | M zyndg, N zinda] alive, living. ~th: life. zindakkar [zywndkkl | M zyndkr] vivifier, reviver. zinénidan, zinén- [zynyn-ytn'] damage, harm. zirak [zylk' | M zyr, N ~] wise, clever. zistan, v. ziwistan. zišt [zyst! | = P, N ~] hateful, ugly. ziwénidan, ziwén- [zywyn-ytn! | M zywyn-] vivify, revive. zi(wi)stan, zi(w)- [zyz-stn! | M zywystn, zyw-, N zistan] live. zi(w)išn [zywšn! | M zyysn] life; livelihood. ~ih: life, living. --6mand [-”xmnd] living, alive. ziyānaģ [zyd?nk'] young woman. zīyišn, v. zī(w)išn. zofāy [zwp'd | M zwp’y] deep; depth. *~ih: depth. ` zofr [zwpl | M zwwpr, J zwrf, (N žarf)) deep. —šy [2d] depth. ~-payag [-p'dyk'] deep. zóhr [zwhl | M zwhr] libation, offering. zor [z())wl | M zwr, N ~] power, strength. Bay ge J ~ig, ~dmand [-yk!, -wmnd | M -mnd, N —mand] powerful, strong. d z^ 201 [zwt! = Av. zaotar-] first officiating priest. ~ih: office of 201. Zraw-, v. zruftan. !zréh [zlyh | P zryh] sea, lake. *zréh [ziyh | N zirih] armour. zruftan, zraw- [zlwp-tn'] = azruftan. zūd [zwt! | M zwd, N ~] quick(ly). ^h : speed. zür [zwl | M z*wr] false, deceitful.
1956:first ahy, fradom, naxust, nazdist.
2146:greatest ayre, mahist.
2223:hateful gizistag, zišt.
2236:healthy drust, tandrust.
2588:least kahist, kamist, nidom; at — pad kamistih.
3038:paradise  garódmàn, (garasmān), wahišt; (worthy) оў ~ garēdmānīg, wahištīg.
3446:right drust.
3452:rightness drustīh.
4298:well (a.) drust.
4883:māzdēsn mahist, māst māzandar māš, maxš roynt
4885:mādayār mādišt mādagīh mādagīg 1*mādag mādagwar mādar Abt, mex ābgēnag! mēhan mēzd may, meh Sahrestan! ‘mahist men- moymard! menidan mënög
5052:kimaghanjamih "age ” 425 kāmagxwadāy ^A pr 563 kāmgār > 56 8 1-2kāmag ($e 3 kāmagwidār ` 156 3 kāmrawāg 1 ө» e 4 kāmistan uerg s kastar `, Let 4 kástan 101635 4 kāč Q» 5 kābēn wars kāpūr N vays kādag Y4ve» 5 wast 25 A wasxwüstag 1341223920 эу "kay 24 drat “ys drodádwarih! >) мео 5 у kch SIE kahist 1825-65 4
5241:wasswarih naxsag waxšišn wahistig wahišt wüdám ` wādgirdag wād wādrang wüdrangboy wādbān nabānazdišt tāt
```


## [2026-09-06T15:25:31.036Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -noE \"(frahist|frahist|nazdist|kamist|mahist|kahist|nidom|fradom)[^ ]{0,3} \\[[^]]*\\][^.]*\\.\" PHD.txt | head -20; echo \"=== NYB ===\"; grep -nE \"\\b(frahist|nazdist|mahist|kahist|zišt|naxust|wahišt|tang|drust)\\b\" NYB_vol2_glossary.txt | head -25",
 "description": "Grep MacKenzie and Nyberg for MP superlatives"
}
```


### [2026-09-06T15:25:32.787Z] TOOL RESULT

```
325:fradom [AWLA < Ar. !?wD; pltwm | (M prtwm)] first.
325:frahist [p/h(y)st! | (M pryst)] most (superlative of freh), frahixtag [plhhtk' | N farhixta] educated, trained, skilled.
422:kahist [ksst'] least.
424:kamist [Amyst'] least.
444:mahist [msst!, mhst! | M mhyst, N ~] greatest.
510:nazdist [x3dst'] first.
512:nidom [nytwm] least, smallest.
=== NYB ===
1244:davr [dpl] course, rough, a nickname of King Yazdagird I: 115’, in Arab sources (references v. Cat. 67) transliterated dafr and translated al-fazz-; renders Av. (1789) harata- ‘well-fed’ Vd. 224; stout, robust, of a warrior DkM 75°. Often written ddpl: PR 5? (ddplyh =:) davréh u drustéh antonyms of carpeh u datistanéh; also in BdA, v. s. v. Gafr-gav, where the constant confusion between ~ and gafr is dealt with. Paz. dawar (Bd Antià 431°; SGV V, 61. 74 is uncertain, and emended by West and de Menasce). — Olr *dabra-, re- presented by Av. (680) dawrd-mačši- ‘possessing well-fed sheep’; Markwart’s etymology (Cat. 1. c.) is untenable.
1283:dipivar [dpywr] secretary ŠPrs: 9. 15. Pl: 7; pl. eas. obl. —-an mahist the chief secretary 1119. 1821. 1925, — FrP 15, MS K dpywl (= dipīvar). Olr "dipi-vara- from OP dipi- ‘inscription’, BP dyp ‘document’, MPrth dyb ‘letter’ + "vara- from Av. (1360) 'var- ‘to cover, to hide, to preserve’, thus ‘he who preserves the documents’. Early contracted to dipir: Arm lw. dpir Yoxupaveóc; KZSPrth 1. 24 dpyrwpt = Prs l. 29 dpyrpt, Gr. trans- literation diBuporr, ‘chief secretary’; M PrthPrs dbyr; NP dibir, dabir (but Paz. "diver, v. next w.). Cf Bailey, BSOS VII, 1933, 76-77.
1367:with -uvt- > -uyt- and -št- > -st-. MPrth drwst; MPrs dryst; Paz. d(u)rust, drust; NP durust.
2380:mahist [mhst'] v. mas.
2478:mas [ms] great, big, also used as comp. (+ hac ‘than’), sup. masist [msst'] and mahist [mhst']: kū-š sok mas bit hac apürik gäv its hoofs were bigger than (those of) the other cows 49?-? (gl.); great of rank 38. 52%; ~ martin (pl. cas.
2483:w., pl. cas. obl. hacis-—-àn men of higher rank than oneself, one’s superiors 704; pus i ~ the eldest son 318; nātrīk i ~ the First Lady (of the harem) 4121; kunom ~ hac I shall do greater things than... 5214; pat han 1 ~ gobišn in a loud voice 4521; — masist kirpak 6971; masist rah the most excellent way 761’; dipivaran mahist the Head Scribe 1118, 1821, 19%; mahist aštak 36°; — adv. by far 977°, — Av. (1154) mas-, masan-, comp. (1156) masyah-, sup. (1155) masista-; OP *ma- Oan-, comp. *madyah-, sup. madišta-; hence in Milr: NW mas (MPrth only adv.), comp. masdtar (v. the next w.), sup. masišt (MPrth msyšt), but SW "mah . (not attested so far), comp. mahy, méh (MPrs mhy A-H I) Paz. meh, mehe, „mahi; NP mih (used as pos.), sup. mahist (MPrs mhystg ‘presbyter’ A-H II). BP has taken over NW mas as pos. and comp., and as sup. both SW mahist and NW masist, but developed, according to the SW rule: -št- > -st-, to masist, a hybrid between SW and NW. Possibly, however, -s- was pronounced -h- through- out in SW; Paz. only mahest.
2655:nax®ist [nhwst'] the first 3512. 1114; adv. 1163. — MPrth nxwst; MPrs nxwst; Paz. naxust; NP nuzust; sup. of the pre- ceding w. l
2667:nazdist [nzdst', nzdyst'] first: adj. 357; adv. 963, — Av. (1060) nazdista-.
3206:*raftenitan [SGY TN-tynytn'] "to form flocks: hàn 1 zivandak góspand frahist 6 ham *rafténit *has brought flocks of living cattle together in the greatest number 3819-3, — If correctly handed down, it may be explained as a den. of *raft ‘drove, flock’, from raftan.
3719:tang [tng] narrow 48%. — MPrth tn(n)g ‘distress’ (MHC); MPrs tng (S); NP tang.
3720:tangéh distress, straits 6615,
3790:šmār, the lemma signifying: ‘tog = ac- count, reckoning’. Paz. hmar represents the NW form of SW āmār, g. v.; Arm. lw. toiž < *tauža- ‘fine, penalty’, tugan < *taugana- id., v. further s. v. tērtan and ham-tožik. — Coincides in spelling with tangēh, but 4619-3! must refer to the Last Judgement, thus to the last settle- ment of aecounts.
4068:welk-] great, big, high, lofty, passim; regularly placed before its head w., seldom: after (41?. 724); in titles great, chief: ~ framatar (g. v.); ~ šahridar (q.v.); — subst., pl. cas. obl. ~-dn the magnates HajA:6 [RB’n]. B:6 [welk’n]. 42. 1133, 16? [wewlg'n'], v. Christensen, Sass. 100. 110sq. — OP vazrka-; MPrthPrs wzrg; Arm. lw. vzurk, vzork, vzruk; Paz. guzurg, guzarg; NP buzurg. No comp. and sup.; for these forms meh, mahist are used; v.s. v. mas.
5244:nazdista-: nazdist
6139:tng: tang
6746:naxust: naxlist
6950:zarin: zarrén zindaa: zivandak zindan: zčndan zišt: zčšt zivastan: zivistan zreh, zrih: zrah zufaé: zahyäi zufr: ~ Zuhūdaa - Zuhūda | : Yahüd
7135:firah: Frai-zišt
7257:mih (mahist): mas mihmän: mahmančh mir: mérak miyànji: miyànjikeh mizd, muzd: mizd mčbad: magu-pat mü, müy: mod muhrah: muhrak müq: mök
```


## [2026-09-06T15:25:46.126Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2645,2660p' NYB_vol2_glossary.txt | cut -c1-1500; echo \"########## zišt\"; grep -n \"zišt \\[\" NYB_vol2_glossary.txt | head; grep -n \"z.št \\[z\" NYB_vol2_glossary.txt | head",
 "description": "Read Nyberg naxust context and zišt entry"
}
```


### [2026-09-06T15:25:46.203Z] TOOL RESULT

```
napa ;
narm [nlm] soft 472°. — V. also s. v. *a- namr-tom.
Narsah [nrshy] n. pr. masc. P 1:7 (twice). — Av. (1054) Natryē.saņha-; MPrth nrysf- yzd; MPrs nrysh-yzd (A-H I); Arm Nerseh.
nasäi [ns’y] corpse 6021. 727. 942%. — Av. (1057) nasu-, ace. nasāum, pl. nom. na- sāvē; MPrth ns’w; MPrs ns’h (A-H I); NP nasā ‘dead’.
Nasibin [*ns(y)byn'] Nisibis. (syr Nsibin) 11425.
: nask [nsk] properly ‘bundle, bunch’, the name of each of the 21 “books” or collection of texts forming together the Sassanian Avesta 1091’. — Av. naska- in (1060) nasko.frasa- ‘one who devotes himself to the study of the nasks’.
Navizak [nw’ck'] a town in Bactria 113%. — Cat. 34.
naxcir [nhcyl] hunting 3!*-!? etc. - MPrth nacyr ‘game, prey’ (MHC); KZŠPrth 1. 24 nhšyr(-pty) = Prs 1. 30 nhcyr(-pt); MPrs nheyhr (S, A-H I); NP naxeir ; borrowed: Arm naxčir-k* ‘massacre’; Syr nahšira, etc., v. Telegdi 228; Bailey, BSOAS XI, 1943, 774; XIII, 1949, 122. Asmussen, AO XXX, 1961, 1-20.
| side of 5716, 7418; pat han i...
Nax"-Ohurmazd [nhw ’whrmzdy] n. pr. masc. P 1:6. - MPrthPrs nwx ‘beginning, the first of anything’; ~ ‘foremost is O'.
nax®ist [nhwst'] the first 3512. 1114; adv. 1163. — MPrth nxwst; MPrs nxwst; Paz. naxust; NP nuzust; sup. of the pre- ceding w. l
Nayāzem [Paz.] one of Zartuxšt's fore- fathers 471. — This form with an initial n- (quite unmistakable in the Dk MS) is also found in Vicarkart i dénik 28 (Na- yazem); in other sources (also Arab.) without n-: BdA p. 235! Ayazim, BdJ 79' Ayazemni, etc.
nayitan [DBYLWN-tn, DBLWN-tn'] nay- to conduct, to bring, to lead; ideogr. + x, for pres. 3d p. pl. nayénd 6515; ideogr. + x, for pt. pass. = pret. 3d p. nayit 122°. 515. 5717. 11719. — Av. (1042) nay-; MPrs inf. nyydn (A—H I), pt. nyyd (A-H II); FrP 20 DBLWN-tn' = (K) nytn' read nayičan; (Sı) nyytn' read nyaičan (for nayióan) ; (S,) ideogr. + NP nayidan; P ideogr. + NP na’idan; only one MS (O) has Phl nytn', Paz. ničan.
The pres. forms given in Paz. are: (K)
naió naim; (P) NP na’id nym; (S,) NP n@id nym, but (Paz.) nyid nyem; Paz. Mx 7423 nied, 9017 niend.
nazd [nzd] 1. adj. near: — bäm daybreak 53; without bam, subst. daybreak 6°, cas. obl. nazdéh 4413, — 2. adv. ~ 6 near, short- ly before 10513. — 3. prep. near to 50°; with 5627. — Av. (1061) comp. nazdyö; MPrs nzd (S, A-H IT); NP nazd.-
########## zišt
2781:Nizišt [nzyšt'] n. pr. of a dev 721, — Paz. Nizist, Nīž(t)št.
4540:zēšt [zySt'; GNY?] ugly, disgusting 319-12. 6121, 756.8; 5724 zyšt gl. to the ideogr. GNY? not known in the FrP. — MPrth zystyft ‘nastiness’; Paz. NP zist; ci Av. (1693) zdizdista- ‘the most loathsome’, (1651) zaēša- ‘hideous’.
```


## [2026-09-06T15:26:11.413Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in \"tang\" \"zi\\xc5\\xa1t\" \"nuhust\" \"nuxust\" \"bihi\\xc5\\xa1t\" \"bihist\" \"mahist\" \"farhist\" \"frahist\" \"k\\xc3\\xa2stan\" \"kastan\"; do echo \"== $w\"; grep -n -m3 -P \"$w\" HRN.txt | cut -c1-400; done",
 "description": "Grep Horn for the Persian words"
}
```


### [2026-09-06T15:26:13.433Z] TOOL RESULT

```
== tang
3733:af/. tangat/l; wsi/, t^mg, sar. tong,
8997:Käs. Q. vergl. angastän^ batangastdn (s. v. nigc^
== zišt
== nuhust
== nuxust
== bihišt
== bihist
2521:Die Aussprache behist ist die ursprüngliche ; in bihist
== mahist
8692:mahist, päz. meh (PPGL); arm. vergl. mec gross' (H.
== farhist
== frahist
== kâstan
== kastan
6890:aw. \^8caüd'^), scindai/^Urzerhrechen ; phlv. skastan
```


## [2026-09-06T15:26:20.058Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for ln in 2521 8692 3733; do echo \"### $ln\"; sed -n \"$((ln-8)),$((ln+8))p\" HRN.txt | cut -c1-500; done; echo \"==== hässlich/zist ====\"; grep -n -m6 -iE \"h.sslich\" HRN.txt | cut -c1-300; echo \"==== zuerst ====\"; grep -n -m8 -iE \"zuerst|nu.ust|na.ust\" HRN.txt | cut -c1-300",
 "description": "Horn contexts"
}
```


### [2026-09-06T15:26:21.969Z] TOOL RESULT

```
### 2521
Ich kann den Verdacht nicht unterdrücken, dass
auch np. ber/ Teil' (Sahn. I, 77 Anm. 11, Calc), ber/e
hierher gehören ; dann natürlich auch afy. LW. bar/a,
bra/a ^Anteil', vergl. Hörn, Indog. Forsch. H, 138
Anm.
246. bihiSt^ behist ^Paradies'.
(äw, mhista- 'bester; phlv. vahist; ai. väsistha-.
LW. kurd. behist.
Die Aussprache behist ist die ursprüngliche ; in bihist
ist der erste Vokal dem zweiten angeglichen.
247. be, ehe 'ohne'.
phlv. ape- (päz. atve-)^ z. B. ape'\htm, ape]vnäs etc.,
be (ZPGl.), vergl. arm. LW. ape]niaz,
kurd. af/. bei. LW. bt- resp. he-.
*) Fr. Müller, WZKM. 5, 186, Anm. vergleicht aw. vahhana'
*Kleid\ was ganz unwahrscheinlich iat.- 57 ~
Eine über das Pehlevi hinausgehende iranische Form
### 8692
nicht* (H. No. 200).
kurd. me-; afy. ma-; oss. d. t. ma- nicht' (prohi-
bitiv) (173).
999. mih gross*, mehist ^), mihtnj mihter.
g. mas gross*, master.
ap. vergl. ma&ista- grösster*; aw. masyao grösser*;
phlv. mas gross, grösser, grössest', masist, mas(i)st,
vergl. 7nas[mayan *Grossmagier (AlbSnlnl), masTh%
mahist, päz. meh (PPGL); arm. vergl. mec gross' (H.
No. 191).
af/. masar 'älter, Herr*.
Vergl. zu bih (No. 241).
1000. mihr *Sonne; Liebe', mihr[ban 'freundlich, wohl-
wollend*.
ap. Mid^ra^, vergl. Vaulmisa-; aw. Mi&ra-, mi&ra^
'Vertrag*; phlv. mür, päz. mihir (vergl. Meherdates,
Tac, MsQfiBQorig^ Proc, skr. LW. mihird- *Sonne');
### 3733
397. tenuk *düun, zart, fein'.
ai. tanu-, tdnuka- *dünn, fein\
kurd. tenik; oss. f(wäg (248); bei. tanak, n. fana/,
fanaU (377); sar. tanük,
398. teng 'en^Q,
aw. tahcista- (Superl. von ta/tna- 'kräftig'); phlv. tanf/
eng', tmigih 'Enge'; arm. fanjr 'dicht' (H. No. 110).
kurd. tenk *enge; bei. tank, n. tanJc, tahanH (378);
af/. tangat/l; wsi/, t^mg, sar. tong,
Vergl. auch Bartholomae, Studien II, 44, 51.
399. tenlden 'drehen, spinnen', tede 'Spinnengewebe*, tane
'Zettel, Aufzug (am Webstuhl)'.
aw. [/^tan-; phly, tatak, vd. 7 (36) (für aw. täfdaena-):
ai. |/"^aw-, tanoti, 'dehnen, spannen'.
400. tHj tu, tö (FirdüsT)^) 'du, vergl. -et 'dein', -tan 'euer'.
ap. iuvam 'du'; aw. tum, tväm, tu, tava; päz. tö {tu);
ai. tvdm, tdva; arm. du 'du' (H. No. 85).
==== hässlich/zist ====
5861:(Geldner, 3 Yasht, 128ji); phlv. zist 'hässlich' (Men.).
5862:af/. LW. zl/t; sar. ir^ Verdorben, schlecht, hässlich'.
5967:*hässlich'.
==== zuerst ====
92:jene Etymologie zuerst aufgestellt habe. So ist die Pionier-
1887:*) Die indogermanische Wurzel vehh'^ veph', vtra'rtü. wthen^ zuerst
1966:geht an* geschieden, worauf Rückert zuerst aufmerksam gemacht hat.
2343:Wort wohl zuerst für indogermanisch erklärt.
3351:856. 2}es 'zuerst, zuvor, pester ^ j)Psin^ pesäm 'Stirn'.
4368:II, 42 folg., und nehme an, dass das s sich zuerst
5545:de Lagarde, Ges. Abh. 225; zuerst Reland,
5591:2) Wohl zuerst erkannt von Rückert, ZDMO. 10, 279.— 140 -
```


## [2026-09-06T15:26:41.773Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -m6 -iE \"kräftigste|kraftigste\" BRT.txt | cut -c1-400; echo \"=== taxma ===\"; grep -n -m4 -E \"taxma-\" BRT.txt | cut -c1-200; echo \"=== HUB ===\"; grep -n -m6 -iE \"teng|tang|bihist|behist|mahist|zist\" HUB.txt | cut -c1-300",
 "description": "Bartholomae kräftigste and Hübschmann greps"
}
```


### [2026-09-06T15:26:41.856Z] TOOL RESULT

```
16532:•  j.  baeäazyö.tuma-  Adj.  'der  heilkräftigste,
=== taxma ===
11331:•  p,  tSi&'a°'taxma-  m.  EN.  eines  Sagar- tiers,  der  sich  gegen  Darius  I.  empörte,
11819:taxma-  62Ö
11841:*  j-i  g-  (.  P-)  taxma-  Adj.  (fem.  °mä-) 'fortis,  tapfer,  tüchtig,  energisch,  helden- haft'; a)  von  a)  Menschen  und  ß)  Göttern: a)  masyänqm  .  .  'manqm  V.  20.  i ;  �
11847:•  p,  taxma-späda-  m,  EN.  eines  Heer- führers Darius  I, :  'dc^  näma'  madei'  Bh. 2.14;  14.
=== HUB ===
1655:398. Np. tang enge, bedrangt' geh5rt zu tanjldan zusammen-
1657:und taiij (Nr. 394) u. s. w. Vgl. tang u bandt obli-
1658:gation' JRAS. 1894, 452. — Dazu auch tang *Sattel-
1660:tang *Sattelgurt' (Dames p. 60) kurd. taiig 'Gurt',
1664:dumStbng *Schwaiizriemen*, afgh. ta-tang *Sattelgurt',
1665:tang ^Sattelgurt*.
```


## [2026-09-06T15:26:51.375Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1640,1670p' HUB.txt | cut -c1-300; echo \"=== HUB other ===\"; grep -n -m8 -iE \"bihi.t|vahi.ta|mahi.t|na.ust|zi.t 'h|nazd\" HUB.txt | cut -c1-300",
 "description": "Hübschmann tang entry and others"
}
```


### [2026-09-06T15:26:51.439Z] TOOL RESULT

```
I, 335, V. 302) genannt, vgl. afgh. LW. tak ^running
about', tag Vunning, gait, pace, walk'. tJber np. taj
'Krone = ap. Haga- s. oben Nr. 367.
Hierher: np. talx *bitter, paz. tahal = phi. taxr
Shk. 268, afgh. trl^, f. tarxa *bitter , pamir dial, trac,
trac (Geiger, Etym. und Lautl. des Afgh. Nr. 235).
Die persischen Fornien weisen auf iranisch *taxra-,
das vielleicht zu Nr. 394 geh5rt.
394. Ich stelle np. tanjtdan zusammenziehen' zu skr. tafiCf
faflj, pr. tanakti 'zusammenziehen*.
395. Dass tund *schnell, heftig, scharf, spitz' (Fird. Ill,
1703, 3642) (aus *tuvant-?) nahe verwandt mit tuvdn
VermSgend, fahig' sei, glaube ich nicht.
396. Zu tundar 'Donner JRAS. 1894, 452 gehort afgh.
LW. tandar *Donner , echt afgh. ^aw^'Donner (Geiger).
398. Np. tang enge, bedrangt' geh5rt zu tanjldan zusammen-
ziehen', auch angusto et aegro esse animo', skr. tanc
und taiij (Nr. 394) u. s. w. Vgl. tang u bandt obli-
gation' JRAS. 1894, 452. — Dazu auch tang *Sattel-
gurt' (Shah. Ill, 1537, 728 - Noldeke), bal LW.
tang *Sattelgurt' (Dames p. 60) kurd. taiig 'Gurt',
naftafig *Mitte des Leibes' (beim Pferd, eigentl. *Nabel-
gurt') Socin, kurd. Samml. II, 294 (die Seiten 293—294— 49 —
kommen doppelt vor!), 339, osset. dxtong 'Bauchgurt*,
dumStbng *Schwaiizriemen*, afgh. ta-tang *Sattelgurt',
tang ^Sattelgurt*.
399. Dazu np. tanasta 'tela araneae', afgh. LW. tanista
*Spinnewebe , tdnista *the warp in weaving'. KaS. tUnS
Aufzug' Shuk. 91 = np. tWna.
400. Np. to *du, paz. tho d. i. to Min. GI. 198, Shk. 269
= zd. tava wie man *ich' = zd. mana etc., Fr. Mil Her,
=== HUB other ===
2438:662. Np. ziSt 'hassHch, abscheulich' stellt Fr. Mtiller,
4492:bihist = bahist Paradies', zd. vahiSta- *beste' (sc. ahu-
5465:hist, bihist *Paradies* =■■ paz. vahest Shk. 270, Min. Gl. 204,
5466:zd. vahista-; bayo *Braut', skr. vadhu; bBxtan 'sieben = paz.
5536:= mp. ^vahiStazad Hoffmann, Ausziige p. 15, Nr. 100;
6511:arisch "^naphas-) neben zd. nabanazdista-, skr. nabhi- *Nabel
6712:zd. asa-vahista-; Farvardm 'der erste Monat' = phi. fra-
7019:nazd *nahe = zd. nazda-, skr. comp. nediyas-] sassanid.
```


## [2026-09-06T15:26:57.899Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### 2438\"; sed -n '2436,2450p' HUB.txt | cut -c1-300; echo \"### 4488\"; sed -n '4486,4498p' HUB.txt | cut -c1-300; echo \"### 6705\"; sed -n '6705,6720p' HUB.txt | cut -c1-300",
 "description": "Hübschmann zišt, bihišt, Ordibehešt contexts"
}
```


### [2026-09-06T15:26:57.966Z] TOOL RESULT

```
### 2438
661. Np. zaryun bedeutet auch 2) viridis et amoenus —
afgh. zaryun green, verdant, fresh'.— 70 —
662. Np. ziSt 'hassHch, abscheulich' stellt Fr. Mtiller,
WZKM. 8, 96 zu zd. zdiMa- unrein', zdisnu- ^), zdista-
(nur in vizdiSta-f var. mzvdiSta- vd. 8, 10?), wie schon
Justi im Wb.
663. Zd. zafaV", zafan- *Mund* wird zu skr, Jabh schnappen
nach, mit dem Maule packen', Jambha* *Zahn, Gebiss,
Rachen* gehSren, so dass hier die Wurzelformen g^aph
und g^abh neben einander liegen. Np. zav *SpaIt, Riss'
(Nr. 649) konnte auch zu skr. jabh gehSren.
666. Np. zamistdn 'Winter : »am *Kalte* = tobistan *Sommer*
: tdb *Hitze'. Mit paz. damistan, das auch ich fiir falsch
halte, vergleicbt N old eke np. datna = arab. LW.
damaq *Wind und Schnee vereint*.
### 4488
(A gat bias), lat. Segestani (Am mi an), arm. Sagastan^
gr. ^juxaavarrj (Isidor Char.). Im modernen Np. ist auch
das a der Prap. ba (= paz. pa) zu i geworden JRAS.
1894, 444.— 129 —
b) Durch Assimilation an vorangehendes oder folgen-
des i:
bihist = bahist Paradies', zd. vahiSta- *beste' (sc. ahu-
*VVelt'); bizisk Arzt' s. p. 128; bisyar Viel* ebenda.
c) einigemal durch Umlaut von a vor auslautendem h
(aus &y oder hy):
mih 'gross* = paz. meh *gross, grSsser Min. Gl. 138,
Shk. 258, phi. m-s (= meS)^ ap. sup. madista- *der Oberste', zd.
comp. masyah' grSsser; kih *klein' = pfiz. keh 'inferior Min.
### 6705
diphthongs)** Blochmann, JA8B. XXXVII, I, 8.
') Doch bleibt auch spater S in paStra *entgegen', paSiruftan
*entgegennehmen\ guSaStan 'vorbeigehen', gudastan Vorbeilassen*, dSar
*Feuer*, taSarv 'Fasan* fRebhuhn* nach Sal. Shuk.), kdyaS *Papier*
gumbaS 'KuppeV, Sal. Shuk. p. 12.-- 190 -
b) Ap. t nach r = phi. t^ paz. d, np. d: Ardtbahist
'der zweite Monat' = phi. Art(a)v(a)hist 61. and Ind. 87,
zd. asa-vahista-; Farvardm 'der erste Monat' = phi. fra-
vartm 61. and Ind. 87, zd. fravasinqm (gen. pi.), vgl.
0ovQdlyav {= vsavia) bei Menander; Ardastr^ Sirin, Art asir
(alter Artases), gr. ^JtQTantlgtjg u. s. w. BB. 4, 35, alter immer
Arta- ; ArdavSin, arm. -4r^at;aw, gr. ^Agva^avoq u. s.w. Dazu bei
Horn ard 13, 6arrf 195, 6«rrfa 196 Anm., ^rard 656, sarcJ 731,
gardam 886, ^wrrf899, -^irrf 900, ^irrf 901, gurda 905; fc(Xrrf
833, mard 972, nahard 1025, mrrf*/ 1078 u. s.w., die Infini-
tivendung -rfaw {kardan = ap. cartanaiy) neben -<an nach
```


## [2026-09-06T15:27:09.403Z] TOOL CALL #27: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:2133 --image 2>&1 | tail -40",
 "description": "Fetch Borhan page 2133"
}
```


### [2026-09-06T15:27:16.164Z] TOOL RESULT

```
(no exact page map; using offset -1917 -> pdf page 216; check the printed number and re-run with --pdf-page if off)
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/2133.png
REF: BQT:2133  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 216  OCR-lang: fas

بیان نهم
در نون با زای نقطه‌دار مشمل برشش لغت
نزار ۱ < بکس اول بروزن شکارء لاغر ‏ | ابجد » مخفف نزديك است ‎٩‏ .3
وضمیف راکویند ۴ - و کوشتی که درآن چربی فزم ۷ « بکر اول وسکون ثالی ومیم.
تباغد ۴ بخاری که درایام زمستان وغیره پدیدآ ید وملاصق
نزج ۴ د بفتح اول وئانی‌وسکون جیم. زمین باشد و هوا را تاريك سازد ؛ وبازای فارسی
بام شهری اس ت که بارمنیه ههور است .۱" هم‌آمده است و بعربی ضباب میگوبند ؛ و بفتح
زد ی « بفتح اول و سکون ثالی ,و دال. | اول نیز درست است .
‎٩‏ - پهلوی 81287 (ضمیف . محتاج ) « اوتوالا ‎٩۰‏ > » دراراك (سلطانآباد) 8828۶
( ضعیف » ناتوان ) ۸« مکی‌نژاد > .
۴ - چون خدمت او کردی واو درتونگه کرد فربه شوی از نعمت اوکر چه تزاری.
« فرخی سیستانی ص ۳۷۷ ۰
۴«( از گوشتها)آنکه تزارتر بود طبیمت خعك بکند .» * الابنیه عن حقایق‌آلادویه:
لحوم » . ۴ - درممجم‌البلدان وحدودالعالم ونخبة‌الدهر در مظان کلمه نیافتم .
8 - ر4: ترزديك اوستا -88242 (نزديك), هندی باستان -۵41[/85 ۰8 ۰8641910112
کردی وانغانی81248 . سربکلی 8124 « اسشق ۰4۱۰۲۹ ‎٩‏ - بمعنی قرب ...۰
پپلوی ... ۰ جثب + در حدود ...:
چو نزد ده و دو رسانید سالز برافراخت یال بلی پور زال ۰
منسوب به فردوسی طوسی .
۷ یم (هم.) : طبری 0 ( ابر [ ابری که تزديك زمین است ) ] « واژه نامه
مد در خراسان و زد نیز 362171 بمعنی مه و باران تم‌نم است « فرهنگه نظام » :۶ نزم »
آن بخار بو دکه بتازی ضباب کوبند . عنصری ( بلخی ) کفع :
زمیخ و نز که بد روز روشن از مه تیر چنان مود که تاری شب از مه‌آبان .»
« لغت فرسی صس ۰.۳4۳
نردوك - پپلوی 822201 ( نزديك ) از : برد (ه«م.) + يك ( نبت ) . رك :
نیب رکه ص ۱۵۵ ؛ نیز پپلوی 8824154 «اسشق۱۰۲۹* «اوتوالا ۵۹* » کردی 81206 (نزديك»
قرب ) » 86216 , ال2زه . 2820۴ « ژاباص 4۱۹ نی زکردی 816 ( نزديك » پهلوی)
مشفق نزو « ژابا صس 4۲۸ > ۰ بلوچی 82211 , 382120 , 3321 اسدق ۱۲۹ ؛ کیلکی
26 ۰ فریزندی وبرئی 22216 , نطلنزی 8270118 «که . ۱ س۲۹۳* ۰ سمنانی 82211
و 38201 ۰ سرخه‌بی 32261۷ ۰ شهمیرزادی 18216 « که . ۲ س ۱۹۳ ؛ پهلوی ... »
جنب ...۰ قرب را مات ساحیدبوان رقم ۰ وصورت حالش (حال رقیق را ) بیان
کردم . > «کلستان س ۳۷ . ۱
```


## [2026-09-06T15:27:29.466Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && for w in فرهست مهست نخست; do echo \"=== $w\"; grep -c \"$w\" BQT_v3_pages.txt BQT_v4_pages.txt 2>/dev/null; done; echo; grep -n \"فرهست\" BQT_v3_pages.txt | head -5 | cut -c1-200",
 "description": "Grep Borhan v3/v4 OCR for farhast, mehast, naxost"
}
```


### [2026-09-06T15:27:31.287Z] TOOL RESULT

```
=== فرهست
BQT_v4_pages.txt:0
BQT_v3_pages.txt:3
=== مهست
BQT_v4_pages.txt:7
BQT_v3_pages.txt:8
=== نخست
BQT_v4_pages.txt:11
BQT_v3_pages.txt:5

19780:‏فرهست ۴ بر وزن بدست ؛ ‎eae‏
19828:‏۷۶ . صادق هدایت درمجلةٌ موسیقی ‎Tl‏ : ۸ در ‎rth‏ فرهست 4 ‎oad‏ فرس نوشته : « پازند
19846:‏هست را نیست کند فرهستش .» و قس : هست واستا
```


## [2026-09-06T15:27:36.310Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 - <<'EOF'\nt=open('BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\n# find leaf index for line 19780\nleaf=0\nfor i,l in enumerate(lines,1):\n    if i==19780: break\n    leaf+=l.count('\\f')\nprint('leaf(0-based #ff before):',leaf)\n# print the page block\nblocks=t.split('\\f')\nprint('total blocks',len(blocks))\nb=blocks[leaf]\nprint(b[:3000])\nEOF",
 "description": "Print Borhan page containing farhast"
}
```


### [2026-09-06T15:27:38.107Z] TOOL RESULT

```
leaf(0-based #ff before): 272
total blocks 721
[pdf page 273]
ob ‏بر وزن شرت » بمعنی‎ ODS
. ‏وشوکت وشکوممندی باشد‎

فر‌هحت ۱ - بروزن‌سرسخت. ماضی
فرهختن است یمنی ادب کرد وتادیب فرمود.

‎oe J‏ ۲ - بفتح اول والث بروزن
برجتن » بمعنی تربیت کردن و ادب آموختن
وتأدیب لمودن ‎ath‏ و بمعنی آویختن هم‌آمده
است؛ ‎Say‏ ثالث هم درست است .

‏فرهخته۴ - بر وزن برجسته, بمعنی
ادب کرده و تادیب تموده باشد .

‏فرهست ۴ بر وزن بدست ؛ ‎eae‏
‏جادو وجادوبی ‎es‏ وساحری باشد .

‏فر همنك = بنتح اول ‎ky‏ بروزن‌سك
لوند ۰ ‎ew‏ قرربب ونزديك ‎Path‏ - ویمعنی
صاحب عقل و خردمند هم آمده است ۷ ؛وبة
‎Syl‏ و سکون ثانی هم کفته‌الد که پروژن ‎AAS‏

‏باشد .
فرهنج ‎ones‏ شطرنج ۰ بمعنی علم
(۱) چك : کشو:

‏۱ - رك:فرهختن.
ای شمن اهسته باش زان بت بدخو

‏۴ - پپلوی ‎fr@hest‏ ( صيقة تفضیلی از « فره » بمنی ‎(he‏ بمعتی ب

‏مرو اعد

‎bss‏ و داتس و عقل وادب است ۷ - وکناییرا
نیز گونند که مشتمل باشد برلغات فارسی ۷ -
و نام ماد رکیکاوی هم هست ۴ - وشاخ درختیر!
کوبند که آنرا بخوابانند و ‎SE‏ بر بالای ‎OF‏
‏بربز ند تابیخ‌بگیرد و از آنجا ب رکنده بجای‌دیگر
نهال‌کنند ۸ - و نام دوایی نیز هست که آنرا
کشوث (۱) ‎aay‏ و تخم آنرا بزرالکشوث
خوانند ‎٩‏ .

‏فرهنجد - مضارع فرهنجیدن است
‎on‏ ارب کند ‎aly‏ تماید .

‏فر ‎p= OD‏ وزن سر پنجه . مردم
با ادب و خوش روی و ‎SS‏ صورت و سیرت را
گوند .

‏فرهنجیدن *۱- بروزن‌برهم‌چیدن .
پمعنی اد بکردن و تأدیب نمودن باشد .

‏فر هنجیك۱۵ ‎po‏ وزن برهم چیده .

‏بمعنی ادب کرده شده و تأدیب پذی‌نده باشد.

‏۴ - رك : فرهیشتن . ۴ اسم مفعول از * فر‌ختن * :

‎OW‏ بت فرهشته تست , هست نوآموز.
دقیقی طوسی « لفت فرس 45۷ > ۰
نشر ‎ule?‏

‏۷۶ . صادق هدایت درمجلةٌ موسیقی ‎Tl‏ : ۸ در ‎rth‏ فرهست 4 ‎oad‏ فرس نوشته : « پازند
«فرایت * بمعنی فراوانتر و ‎forks‏ میباشد و ربعلی بجادوئی ندارد , چنانکه در تعریف لفت‌فره
(س4۲6) و لفت فرابته « فراسته » ( ص۰٩4‏ ) همین کتاب ‎cal)‏ فرس ) اشار» شده است.»
ممهذا اسدی این شاهد را از ابوضرمرغزی برای معنی جادوبی آوردء :

‏نست را هست کند تنبل اوی
‎cil?‏ فری ص ۰۱۹ .

‏© - فرهمند بدکنش ‎Sp‏ مرو

‏۹ - رك : جهانگیری .
فرهنگه, فرنج .
مرو را در هتر بفرهنجد

‏۷ رك : فرهنگ . ‎A‏
‎ae ۰‏ : افرهنج .
توسنی از سرش یداهنجد ‎ .‏ سنائی غزنوی «جهانگیری».

‏هست را نیست کند فرهستش .» و قس : هست واستا

‏تا نگردی دردهند و آهمند .

‏« ناصرخرو بلخی ۱۲۳* «جپانگیری».
- رك: فرهانج ۰
۶ از: فرهنج ‎Cadet‏ (پوندمسدری):

‏۱ اسم مقعول از «فرهنجیدن» («م.) +
```


## [2026-09-06T15:27:59.912Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 - <<'EOF'\nimport re\nfor vol in ['BQT_v4_pages.txt']:\n    t=open(vol,encoding='utf-8',errors='replace').read()\n    blocks=t.split('\\f')\n    for w in ['مهست','نخست','کاست']:\n        hits=[i for i,b in enumerate(blocks) if re.search(r'(^|\\n)\\s*'+w+r'\\s*[۰-۹0-9]', b) or ('\\n'+w+' ') in b]\n        print(vol,w,'headword-ish blocks:',hits[:10])\nEOF",
 "description": "Locate Borhan v4 headwords"
}
```


### [2026-09-06T15:28:01.572Z] TOOL RESULT

```
BQT_v4_pages.txt مهست headword-ish blocks: []
BQT_v4_pages.txt نخست headword-ish blocks: []
BQT_v4_pages.txt کاست headword-ish blocks: []
```


## [2026-09-06T15:28:04.482Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 - <<'EOF'\nt=open('BQT_v4_pages.txt',encoding='utf-8',errors='replace').read()\nblocks=t.split('\\f')\nfor w in ['مهست','نخست','کاست']:\n    hits=[i for i,b in enumerate(blocks) if w in b]\n    print(w,hits)\nEOF",
 "description": "Find blocks containing the words"
}
```


### [2026-09-06T15:28:06.467Z] TOOL RESULT

```
مهست [30, 65, 151, 232, 413, 498]
نخست [9, 35, 55, 141, 205, 265, 275, 473, 481]
کاست [80, 186, 294, 301, 405, 419, 461]
```


## [2026-09-06T15:28:14.075Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 - <<'EOF'\nt=open('BQT_v4_pages.txt',encoding='utf-8',errors='replace').read()\nblocks=t.split('\\f')\nimport re\nfor i in [151,205]:\n    b=blocks[i]\n    print('#####',i, b.split('\\n')[0])\n    for w in ['مهست','نخست']:\n        for m in re.finditer(w,b):\n            print(' ...',b[max(0,m.start()-250):m.start()+250].replace('\\n',' | '))\n    print()\nEOF",
 "description": "Print Borhan contexts for mehast/naxost"
}
```


### [2026-09-06T15:28:15.708Z] TOOL RESULT

```
##### 151 [pdf page 152]
 ... ارات‌وخاهاه وامثال | دام درخت سوس است و ییخ آن را بجربی اسل | آن » وآنرا لنگر هم میگویند. | الوی وامابع‌الو ی کوبند . مه هرد ۱ -» بکر ارل و قح ناك , | ۱- مهری‌بکی پیرفزاره آوا پرآورده بزار ‏ چون تندراندر مرغزارجانیبهرجا ريخته. | « خاقانی شروالی ص ۳۸۸ ۰ |  | ۴ - مهست از: مه ( بز رکه )۲ست ( پوند صفت عالی )ء دراوستا 13285181218صفقت | عالی از 388 ( ۳ مه . بز رکه ) است بمعنی مهترین « فاب ۱ اس 0۹ »۰ پهلوی 2288151 | « اسشق ۹۹۹ : |  | نختین سرنامه کفت از مهست شهنشاء کسرای بزدان پرست . | فردوسی طوسی ۸« شاهتامةٌ بخ چ ۸ امس ۲۳۱
 ... ر ‏ چون تندراندر مرغزارجانیبهرجا ريخته. | « خاقانی شروالی ص ۳۸۸ ۰ |  | ۴ - مهست از: مه ( بز رکه )۲ست ( پوند صفت عالی )ء دراوستا 13285181218صفقت | عالی از 388 ( ۳ مه . بز رکه ) است بمعنی مهترین « فاب ۱ اس 0۹ »۰ پهلوی 2288151 | « اسشق ۹۹۹ : |  | نختین سرنامه کفت از مهست شهنشاء کسرای بزدان پرست . | فردوسی طوسی ۸« شاهتامةٌ بخ چ ۸ امس ۲۳۱۹ | معنی متن صحیح لیست . ۴ از : مه ( مغخفف ماء )+ شید (ه.م.) قن : خورشید . |  | ۴ - مهك 1ط2 2 ۳ منکه ۳۱811 ( فولرس آ1 ۰ ۱۲۳4 ) ۳ 996ن1ق76 (فر) «عقار | اف - (م) « مهماز بروزن مفتاح » آهنی اس

##### 205 [pdf page 206]
 ...  > » قن : لخری » نپاز + | سپه دشمن او را رمه‌ای دا ن که درو به چراننده شبات وله ره جو نخراز. | قرخی سیستانی « رشیدی » « انجمن‌آرا > | ۴ -کردی 8751 ( بچهٌ اول , ارشد) « ژابا ص 2۱۸ > » اسفهانی 387271 (نختن). | جهانگیری کوید : «لخر با اول مضموم بثانی‌زده بممتی نخست باشد , و نخری لخستین راکویند.» | قی : راز . ۴ - مصحف « خر > رك : فخری- 6 - مصحف «خری» (ه.م.) | ‎٩‏ - پازند 8871051 ( پپلوی 382151 ۰ اوستا 3221151018 ) « باروچا صس ۳۷۳ *. | ۷ -رك : خستن. ۸ - 313280830 . شپری ببغارا که جغرافی نوسان اسلامی | آرا دف > هم نا
```


## [2026-09-06T15:28:31.865Z] TOOL CALL #33: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-06T15:28:31.873Z] TOOL RESULT

```


```


## [2026-09-06T15:28:36.187Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%86%D8%AE%D8%B3%D8%AA",
 "prompt": "Give the full Persian etymology section for نخست (naxost): Middle Persian form, Old/Proto-Iranian reconstruction, any mention of a superlative suffix -išta, and whether it is related to nazd/nazdišta."
}
```


## [2026-09-06T15:28:37.941Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AA%D9%86%DA%AF",
 "prompt": "Give the full Persian etymology for تنگ (tang) 'narrow, tight': Middle Persian form, Proto-Iranian reconstruction, PIE root, and any mention of a superlative in -išta or of Avestan tanjišta / tanč- 'to pull tight'."
}
```


### [2026-09-06T15:28:43.196Z] TOOL RESULT

```
# Persian Etymology of نخست (naxost)

## Middle Persian Form
According to the document, the Middle Persian form is **nxwst** (naxwist, "first").

## Proto-Iranian Reconstruction
The etymology traces back through two Proto-Iranian stages:
- **\*naxwist-** ("first")
- **\*naxu-** ("first, in front, high")

The document notes this has "uncertain origin, with no known cognates outside Iranian."

## Superlative Suffix
The page does not mention any superlative suffix like -išta in relation to نخست.

## Relationship to nazd/nazdišta
The document makes **no reference** to nazd or nazdišta. The only cognate relationship mentioned is to Northern Kurdish *nexrî* ('first-born') and Old Armenian *նախ* (nax), described as "an Iranian borrowing."

The etymology section emphasizes the word's obscure origins within Iranian languages, lacking external comparative evidence.
```


### [2026-09-06T15:28:44.560Z] TOOL RESULT

```
# Persian Etymology of تنگ (tang) 'narrow, tight'

Based on the Wiktionary entry, here's the documented etymology:

**Middle Persian form:** The entry states the word was "inherited from Middle Persian" with the form listed as (tng /⁠tang⁠/, "narrow, tight")

**Proto-Indo-European root:** The source traces it further back, noting it comes "from Proto-Indo-European *[\*tenk-](/w/index.php?title=Reconstruction:Proto-Indo-European/tenk-&action=edit&redlink=1)" meaning "to compact," with a possible connection to "*[\*ten-](/wiki/Reconstruction:Proto-Indo-European/ten-)" meaning "to stretch."

**Related cognates:** The entry mentions the word is cognate with Persian تنجیدن (tanjīdan, "to squeeze") and Old Armenian թանկ (tʻank).

**Notable limitation:** The provided content does not include any mention of superlatives in -išta, Avestan tanjišta, or tanč- formations. These Proto-Iranian or Avestan details are not documented in this particular Wiktionary entry.
```


## [2026-09-06T15:29:17.940Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== CHEUNG tanj/θanj ===\"; grep -n -m8 -E \"θanǰ|θanj|\\*tanč|tanjīdan|tanjidan\" CHEUNG.txt | cut -c1-300; echo \"=== CHEUNG kah/kas ===\"; grep -n -m6 -E \"\\*kah|kāstan|kāhistan\" CHEUNG.txt | cut -c1-250; echo \"=== ARY ===\"; for w in تنگ نخست بهشت زشت کاست; do echo \"-- $w\"; grep -c \"$w\" incoming/ARY/ARY_pages.txt; done",
 "description": "Cheung and Aryanpur greps"
}
```


### [2026-09-06T15:29:19.825Z] TOOL RESULT

```
=== CHEUNG tanj/θanj ===
24631:*NWIR: NP tanjidan/tanj- ‘to squeeze; to twist, roll together; to draw tight; to be 
41589:tanjidan/tanj-, 378 
56344:*staup (s.v.), *tanč (s.v.), 
=== CHEUNG kah/kas ===
=== ARY ===
-- تنگ
4
-- نخست
28
-- بهشت
1
-- زشت
2
-- کاست
2
```


## [2026-09-06T15:29:22.581Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '24615,24660p' CHEUNG.txt | cut -c1-300",
 "description": "Read Cheung *tanč entry"
}
```


### [2026-09-06T15:29:22.628Z] TOOL RESULT

```
*tanó ‘to twist (together), become narrow, dense, constrict’ 
*MIDDLE PERSIAN: MMP tnz- ‘to strain, press’, BMP tng /tang/ ‘narrow’ 


c DMMPP: 325b 
Partic.: pres. MMP tnz’g’n (pl.) 


378 *tand 


*PARTHIAN: tncysn ‘prohibition’, tng ‘1. suffering, distress; 2. narrow; distressing’ 
c DMMPP: 324b f. 

*KHOTANESE: (+ *ш-) byamjsa-, bätamjsa- ‘astringent’ 

*NWIR: NP tanjidan/tanj- ‘to squeeze; to twist, roll together; to draw tight; to be 
distressed, sad’, Bal. tancit/tanc- ‘to fasten strongly, roll strongly, squeeze’, ? tajén- 
‘to stretch’, NP tang, Bal. tank ‘narrow’ 

*NEIR: Wa. tanz-/tanzd-, tanz-/tanzd- ‘to fortify the warp [of textiles]; to draw a web 
[of spiders]’, Sh. taZ-/tiZd, Sariq. toZ-/tiZd ‘to pull, draw, haul, drag, stretch’, Pash. 
tat ‘close, thick’, ? Sh. (Baj.) taxc-/tixt, Rosh. taxs-/taxst ‘to puff, smoke’. Ф Wa. 
tanz-/tanzd-, tanz-/tanzd- are unconnected with YAv. 0anj- ‘to pull, draw’, etc. 
(ant), 

*SANSKRIT: ѓайс ‘to pull together, coagulate, solidify’ (YV+) = EWAia I: 614 

*PIE *tenk- (*temk- ?) ‘to twist together, pull oneself together, condense’ = LIV: 
625 | Pok.: 1068 

*IE COGNATES: Lith. tenkü (tekti) ‘I stretch, reach, attain’, Olrish -téici ‘solidifies, 
coagulates’, (ppp.) Olrish técht ‘solidified’, ON péttr ‘close, thick’, Lith. tánkus 
‘dense, thick; frequent’ 


*REFERENCES: Horn1893: 88 f.; Fraenkel II: 1077; EVS: 82a; DKS: 282a; Abaev, Slovar’ III: 285; Werba 
1997: 189 f.; Steblin-Kamenskij 1999: 354; Shahbakhsh: s.v. tané-; Korn 2005: 168 f., 365 


*tand ‘to languish, faint’ 

*PARTHIAN: tnd ‘faint, languishing’. 0 The Parthian form cannot be analysed as the 
past participle of *tamH, which would rather be *taHta- > *täta-. > DMMPP: 324b 
*SANSKRIT: fand ‘to become tired, paralysed’ = EWAia I: 623
```


## [2026-09-06T15:29:34.584Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -m10 -E \"^\\*ka[hs]|\\*kas ‘|to become small|to diminish\" CHEUNG.txt | cut -c1-200",
 "description": "Cheung root for kāstan"
}
```


### [2026-09-06T15:29:34.634Z] TOOL RESULT

```
3471:*kas', cf. LIV, ibid. 
3516:*kas! ‘to look, appear’ and *čaš! ‘to teach, show’ meets semantic difficulties. 
13067:pàris- ‘to diminish [intr.]’, päramj- (caus.) ‘to diminish [tr.] > SGS: 10, 82, 81 
16286:*kasl 245 
16320:*kas! ‘to look, appear’ 
16391:*kas? ‘to attach’ 
16409:*kas4 247 
16416:*kas? ‘to fall’ 
16434:*kas! ‘to be small, diminish, lessen’ 
16439:*MIDDLE PERSIAN: MMP gh-, ВМР k’h- /kah-/ ‘to diminish, decrease, lessen’, MMP
```


## [2026-09-06T15:29:37.116Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B2%D8%B4%D8%AA",
 "prompt": "Give the full Persian etymology for زشت (zešt/zišt) 'ugly': Middle Persian form, Proto-Iranian reconstruction, and whether Avestan zōiždišta- 'most abominable' or the root zaēš-/zōiš- 'to shudder' is mentioned."
}
```


### [2026-09-06T15:29:43.271Z] TOOL RESULT

```
# Persian Etymology of زشت (zešt/zišt) 'ugly'

Based on the Wiktionary entry, here is the etymological chain:

**Middle Persian**: The word descends from Middle Persian *zyšt'* (/zišt/), meaning "hateful, ugly."

**Avestan**: This Middle Persian form was borrowed from Avestan *zaēša*, which connects to the root concept of aversion or disturbance.

**Proto-Indo-Iranian**: The etymology traces to *\*ȷ́ʰáyždas* from this earlier language family.

**Proto-Indo-European**: The ultimate source is *\*ǵʰéysd-os*, derived from *\*ǵʰeysd-* meaning "anger, agitation."

The entry does not specifically mention *zōiždišta-* ('most abominable') or elaborate on distinct roots like *zaēš-* versus *zōiš-* ('to shudder'). It simply notes the Avestan form *zaēša* as the immediate source, with the semantic field relating to negative emotional states and disturbance rather than detailed variants of the root morphology.
```


## [2026-09-06T15:29:54.466Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '16434,16470p' CHEUNG.txt | cut -c1-300",
 "description": "Read Cheung *kas1 diminish"
}
```


### [2026-09-06T15:29:54.514Z] TOOL RESULT

```
*kas! ‘to be small, diminish, lessen’ 

*AVESTAN: YAv. kasu- ‘small, little’ (Yt 8.29), Yt 14.17, V 7.59, etc.), ҮАУ. 
kasiiah- ‘young’ (V 5.24, V 14.5, V 15.2, etc) 

*MIDDLE PERSIAN: MMP gh-, ВМР k’h- /kah-/ ‘to diminish, decrease, lessen’, MMP 
k’hysn, q’hysn ‘diminution’ = DMMPP: 205a, 201b 

Pres.: IND. 3sg. MMP qhyd, BMP k’hyt /kahéd/, Inf.: ВМР k’hynytn /kahénidan/ (from MX) 
*KHOTANESE: (+ *ni-) nyassa- ‘deficient, bad’ 

*CHORESMIAN: (+ *us-) sks- ‘to become short? = Samadi: 182 

*NWIR: NP kastan/kah- ‘to lessen, diminish’, Nn. käs, Tr. kas ‘little; young’, Varz. 
kas ‘little’ 

*NEIR: Oss. I. kæstær *young(er), little’ || ? I. &-gas, D. &-gas (+ neg. *a-) ‘whole, 
integer || (+ *ui-) D. igas *whole(some), healthy, alive’, Wa. kas ‘young man, lad, 
youth’ 

*SANSKRIT: kasü- (m.) PN ‘the Small One’ (RV 8.5.37) = EWAia I: 330 

© This apparently Пг. root has no certain IE provenance. It may even be an 
exclusively Ir. root, if the Skt. name kasü- is some sort of a borrowing, cf. EWAia, 
l.c.: "als „iranisch-westindoarische Dialekt-Isoglosse” aufzufassen ?". 

«PIE 9 Pokorny, Le cites NHG hager ‘gaunt, haggard’, Lith. kaséti ‘to lessen, 
become thin, dry’ as possible cognates. The origin of NHG hager (incl. Engl. 
haggard < Fr. hagard < Germanic ?) is obscure though, Seebold (Kluge 2002: 383b) 
considers Skt. krsä- ‘id.’ as a semantically more satisfactory connection to NHG 
hager. As for the Lith. form, it appears to have a variant katéti, both forms have a 
popular flavour according to Fraenkel I: 227b f. = LIV: — | Pok.: 521 f. 


248 *kaš
```


## [2026-09-06T15:29:55.754Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D9%87%D8%B4%D8%AA",
 "prompt": "Give the full Persian etymology for بهشت (behešt) 'paradise': Middle Persian form, Avestan vahišta- and any mention of vahišta ahu- 'best existence' and of the superlative suffix."
}
```


### [2026-09-06T15:30:02.044Z] TOOL RESULT

```
# Persian Etymology of بهشت (behešt)

Based on the Wiktionary entry, here's the etymology:

The word traces back to **Middle Persian** _𐭥𐭧𐭱𐭲𐭩_ (wahišt), which derived from **Old Persian** _\*vahištah_. The ultimate source is **Proto-Iranian** _\*Hwáhišt-Háhuš_, described as literally meaning "best existence."

The entry notes: "From [Proto-Iranian](https://en.wikipedia.org/wiki/Proto-Iranian_language "w:Proto-Iranian language") _[\*Hwáhišt-Háhuš](/w/index.php?title=Reconstruction:Proto-Iranian/Hw%C3%A1hi%C5%A1t-H%C3%A1hu%C5%A1&action=edit&redlink=1 "Reconstruction:Proto-Iranian/Hwáhišt-Háhuš (page does not exist)")_ ("بهست-هستی", literally "best existence")."

The entry also documents cognates in **Northern Talysh** and **Baluchi**, supporting this Indo-Iranian lineage. Additionally, there's a secondary etymology noting that بهشت functions as the superlative form of an obsolete adjective.
```


## [2026-09-06T15:30:18.986Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==431' POK_02.txt | head -40 | cut -c1-200; echo \"#### grep POK_full for -isto superlative\"; grep -n -m6 -iE \"Superlativ.{0,40}(isto|-isto-)|isto-suffix\" POK_full.txt POK_01.txt POK_02.txt 2>/dev/null | cut -c1-250",
 "description": "Pokorny page 775 and superlative suffix"
}
```


### [2026-09-06T15:30:22.157Z] TOOL RESULT

```
#### grep POK_full for -isto superlative
POK_full.txt:76361:probably a superlative *karpistos " suitable best of all for the picking '); Old Icelandic harfr
```


## [2026-09-06T15:30:28.404Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in POK_01.txt POK_02.txt POK_03.txt; do echo -n \"$f leaves: \"; awk 'BEGIN{RS=\"\\f\"} END{print NR}' $f; done; echo \"--- find 'ōku' entry\"; grep -n -m5 -E \"^ *ō̆?k[ûuü]-|ōku-|ok̑u-\" POK_full.txt | cut -c1-200; grep -n -m3 \"lemma: ōk\" POK_full.txt",
 "description": "Pokorny leaf counts and ōku entry"
}
```


### [2026-09-06T15:30:30.133Z] TOOL RESULT

```
POK_01.txt leaves: 363
POK_02.txt leaves: 433
POK_03.txt leaves: 429
--- find 'ōku' entry
```


## [2026-09-06T15:30:33.118Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=430 && NR<=432 {print \"=== leaf\",NR; print substr($0,1,1200)}' POK_02.txt",
 "description": "Print Pokorny leaves 430-432"
}
```


### [2026-09-06T15:30:35.011Z] TOOL RESULT

```
=== leaf 430

=== leaf 431

=== leaf 432
```


## [2026-09-06T15:30:38.963Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Page(s): 77[3-6]\" POK_full.txt | head; echo ---; grep -n -B18 \"Page(s): 775\" POK_full.txt | grep -E \"lemma|Meaning|Page\" | head -20",
 "description": "Find Pokorny page 775 entries"
}
```


### [2026-09-06T15:30:39.024Z] TOOL RESULT

```
63317:Page(s): 773 
63376:Page(s): 774 
63380:Page(s): 774 
63384:Page(s): 774 
63408:Page(s): 774 
63513:Page(s): 775 
63729:Page(s): 775-777 
64385:Page(s): 773 
64411:Page(s): 773 
64437:Page(s): 775 
---
63513:Page(s): 775 
63729:Page(s): 775-777 
64437:Page(s): 775
```


## [2026-09-06T15:30:41.678Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '63490,63520p;63700,63740p' POK_full.txt | cut -c1-250",
 "description": "Read Pokorny entries on p.775"
}
```


### [2026-09-06T15:30:41.732Z] TOOL RESULT

```
atta 

compare maked. Otto-lobus^ 8 hill '; Latin odd; Old Irish oc/?//?- (nasalization after secht 
n- and noi n-)\ cymr. wyth, ncorn. eath, bret. eiz{*ochtT, older -Jfrom -o); Gothic ahtau. Old 
Icelandic atta. Old High German Old Saxon ahto. Old English eahta; Lithuanian astuo-nr. 
Old Church Slavic osmb (reshaped after the ordinals osmb); Tocharian B okt, A okat 

ordinals: Latin octavus (compare also Oscan Uhtavis ' Oktavius ') probably from 
*octduos. Old Phrygian otuFoi Fetei "in 8. years' {*oRtduoi uetesi); gr. Ionian Attic 
6y5o(F)o(; (6 after £p5o|JO(;), obstructed in oySoriKOVTa (hom. to oyScbKOvra reshaped after 
OKTib), compare Latin octuaginta^QO\ the former model from septuag/nta and arisen anew 
in very late time after the latter again; 

after the ordinals to septm {and deRm) have been directed Old Indie astama-, Avestan 
astama-, gall, oxtumetos. Old Irish ochtmad, cymr. wythfed, Lithuanian asmas. Old 
Prussian asman (Akk.), Old Church Slavic osmb {oRtmo-)\ compare Tocharian A oRtant, B 
oRtante^Vne eighth', alb. f. e teta^ the eighth ', m. i teti^ the eigth ' 

Other congruities are to name ved. astadasa- 1 8, Avestan astadase- 'the 1 8.', gr. 
6KTCji)(Kai)5£Ka, Latin octodecim. Old High German aMozehan^8^, gr. OKTOKoaioi, Latin 
oct/ngentr 800'. 

References: WP. I 172 f., WH. II 199 f., Trautmann 15 f. 
Page(s): 775 



Root / lemma: ok"- , {*{*hek'^h- ) 

Meaning: to see; eye 


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
```


## [2026-09-06T15:30:50.589Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -A4 -E \"^Root / lemma: o[k̑'\\\"]\" POK_full.txt | grep -E \"lemma|Meaning\" | head -20; echo ---; grep -n -B3 -A3 \"swift\" POK_full.txt | grep -E \"lemma:|Meaning: .*swift\" | head -20",
 "description": "Find Pokorny ōḱu- swift lemma"
}
```


### [2026-09-06T15:30:50.664Z] TOOL RESULT

```
63386:Root / lemma: ok- 
63388-Meaning: to think over, *understand, see 
63517:Root / lemma: ok"- , {*{*hek'^h- ) 
63519-Meaning: to see; eye 
63525:Root / lemma: ok"- : to see; eye derived from Root / lemma: deik- : to show' : Root / 
63527-lemma: dek-1\ "to take, *offer a sacrifice, observe a custom' [common lllyrian-Baltic d- > 
---
2778:Hence Root/ lemma: aig-\ (goat) is identical with Root/ lemma: aig-3\ (to move swiftly, 
29542-Root / lemma: etro- 
29543:Meaning: hurried, swift 
29546:Root/ lemma: etro-\ "hurried, swift' derived from Root/ lemma: at(e)r-\ fire' 
41391:Meaning: to move swiftly, to fight
```


## [2026-09-06T15:30:57.963Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -iE \"lemma: o[kḱ]u|okus|ōk̑u\" POK_full.txt | head; echo \"--- meaning quick/fast\"; grep -n \"Meaning:\" POK_full.txt | grep -iE \"quick|fast|swift\" | head; echo \"--- POK_02 text search for 'ōk̑ú'\"; grep -n -m5 -E \"ok.u-s|okus \" POK_02.txt POK_03.txt | cut -c1-200",
 "description": "Search Pokorny for ōḱu- swift"
}
```


### [2026-09-06T15:30:58.046Z] TOOL RESULT

```
76621:Material: Gr. OKuSpaivu), OKu^opai "rage against, grolle', aKu9p6(; (diss, from *aKu5-9p6c;) " 
--- meaning quick/fast
6297:Meaning: glittering, white, fast 
12472:Meaning: quick 
29543:Meaning: hurried, swift 
41391:Meaning: to move swiftly, to fight 
44929:Meaning: to drive, force to move quickly 
51001:Meaning: quick, hasty 
51016:Meaning: quick, hasty 
63321:Meaning: to swell; strong, *fast, swelling, lump, water 
64415:Meaning: quick 
65098:Meaning: quick, perky 
--- POK_02 text search for 'ōk̑ú'
```


## [2026-09-06T15:31:00.554Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '64410,64445p' POK_full.txt | cut -c1-300",
 "description": "Read Pokorny lemma at line 64415 (quick)"
}
```


### [2026-09-06T15:31:00.693Z] TOOL RESULT

```
Page(s): 773 

Root / lemma: oRu-s 

Meaning: quick 

Grammatical information: Kompar. oRios, Super!. oRisto- 

Material: Old Indie as'^- "quick, fast', Kompar. asTyan, Superl. asistha-, Avestan asu- 

"quick, fast', Kompar. asya, Superl. asista, gr. u)ku(;, wkigtoc;, poet. cbKUTaroq, Latin ocior^ 

faster', Superl. dc/ss//77^s (lacks Positive), acymr. di-auc, ncymr. di-og, corn, di-oc, bret. di- 

ec'idle', actually " unquick '; 

perhaps in ablaut to aR-, o^- "sharp' (above S. 18 f.); then Latin ac^-/oec//^s 'swift-footed' 
and accipiter^ hawk, falcon' (above S. 19) could also belong here; 

Maybe zero grade in alb. {*ccipiter) sk/ptar'eag\e man', shq/pe ^eag\e', sk/fter^ hawk, flying 
fast'. 

A cognate *d^-/'c»- (compare to forms "a^-Ao- besides *aR-u-) is perhaps the base from 
Church S\ay\c Jastrgbb ' hawk'. 

References: WP. I 172, WH. II 198. 
Page(s): 775 

Root / lemma: or-, ar- 
Meaning: to speak; to call 
Material: 

In a- grade: 

Hittite aruua/-' adore ' (also ania-^ ask the oracle a question '?).
```


## [2026-09-06T15:31:23.230Z] TOOL CALL #50: Bash

```json
{
 "command": "grep -rl '\"words\": \"\"' data/verification/page-1*.json data/verification/page-2*.json 2>/dev/null | head -3; python3 - <<'EOF'\nimport json,glob\nfor f in sorted(glob.glob('data/verification/page-*.json')):\n    d=json.load(open(f))\n    for e in d.get('entries',[]):\n        for n in e.get('nodes',[]):\n            if not n.get('words'):\n                print(f, n.get('id'), n.get('verdict'), (n.get('derivation') or '')[:220])\n                raise SystemExit\nEOF",
 "description": "Find how empty nodes were handled before"
}
```


## [2026-09-06T15:31:23.564Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1358,1372p' NYB_vol2_glossary.txt | cut -c1-700",
 "description": "Nyberg drust entry"
}
```


### [2026-09-06T15:31:25.208Z] TOOL RESULT

```
data/verification/page-103.json
data/verification/page-105.json
data/verification/page-107.json
data/verification/page-101.json 5 plausible Pass-through node: Arabic zumurrud زُمُرُّد 'emerald' does go back to Greek smaragdos, but not directly: Wiktionary derives Arabic zumurrud from Persian zumurrud (< Middle Persian ʾwzmbwlt /uzumburd/ < Greek), i.e. Persi
```


### [2026-09-06T15:31:25.245Z] TOOL RESULT

```
društ [dlwšt] rough, harsh, coarse, v. next w. — NP durušt.
društ-ēvācihā [-->dw*eyh”] in a manner characteristic of a društ-ēvāc, a man : whose speech is coarse, a coarse-spoken man 412. — V, ēvāc.
driitan [HSD-1-WN-tn'] to cut off, to mow: apar drut 41’. — FrP 18 drutan drun-; Paz. pres. drün- (Mx); NP durüdan dirav-, but durün ‘a measure of corn’.
druvand [dlwnd] wicked, evil, of Ahriman 642-7 and passim; of human beings 10°. 3414, 6625, 964. 10711 — subst. 7213, 7417, pl. eas. obl. —-än 461, 5313, 7220, 7421, 75°. 10226, 10322, used as cas. rect. 10114-18, — Av. (774 sqq.) dragvant-, drvant- ‘be- longing to the drug' (v. druž); MPrs drwnd (S, A-H II); Paz. daruand, dar- vand.
druvandéh wickedness 68°; the state of being wicked 74?4; coll. the wicked 8215 (Paz. substitutes darčg). — Paz. daruandi.
druväsp [dlw'sp'] 211% must designate the lower end of the arrow, but its ety- mology is quite obscure: *druva- ‘firm’ (v. druyist) + ? — it cannot be the Aves- tan (783) deity Drvāspā.
druxtan [dlwhtn'] drēž- [dlwe-] to deceive 7712; to speek falsehood, to lie 867°; to break (a treaty) DkM 70°, where the inf. druatan. — Av. (767) draog-, OP draug-; MPrs cf drwxtyh ‘untruthfulness’ (A-H II); Paz. pres. drūž- (Mx).
druyist [drwdst'] safe and sound, whole; right, exact, accurate: P2:9.10 (twice). 1418, 2222 etc. passim. — The letters are unmistakable in P2. Av. (782) drva- (= druva-); OP durwa- ‘firm, secure’, sup. *druvista-, whence in SW druyist
Dür-äsrav
with -uvt- > -uyt- and -št- > -st-. MPrth drwst; MPrs dryst; Paz. d(u)rust, drust; NP durust.
druyisteh [dtwdstyh] v. tan-druyisteh.
druž [dlwc'] all that is false, untrue, wrong, deceptive: 1. the world of Guile and Untruth, conceived as a personal cosmic power, 3822, 9313. — 2. individual manifestations of this power, demons, conceived as feminine supernatural be- ings: sg. 5716-25, 583. 9620-24, 9817-19, 101% (voc.). 1023-14; ~ ; anāštēh 671; ^ 4 spazgeh 6811-12; ~ 7 ahramög 10124-25; pl. cas. rect. ~ 648. 65*. 9721, 9819 (of human beings). 10224-27, 1033; pl cas. obl. —-än in the set phrase devün u ~-dn 75" ete. (voc. 9027). V. also mthr-druz, mihrčin-druž. — Av. (778 sqq.) drug-, nom. druxš, gen. drüjö; MPrs drwaš (S); Paz. drü£.
druzéh falsity, unrighteousness 66°; a troop, band of fiendish beings 986%, V. also mihrdin-družčh.
Dugdáv [dwkt'wb'] n. pr., Zartux&t's mother 4112, 425.824, 432, 47°92, — Av. (748) Duydo.va-.
dumb [dwmb'] tail: brit. ~ 2418, v. brī- tan; burritak-—-& (-& in attributive po- sition) 302-3, v. burritak. — Av. (749) duma-; NP dumb, dunb. Cf. gaz-dum, gaz-dumb.
```


## [2026-09-06T15:31:40.690Z] TOOL CALL #52: Bash

```json
{
 "command": "pdftoppm -f 227 -l 227 -r 150 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg227 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render PDF page 227"
}
```


### [2026-09-06T15:31:43.636Z] TOOL RESULT

```
total 4468
drwx------ 2 sfmqrb sfmqrb   4096 Sep  6 11:31 .
drwx------ 4 sfmqrb sfmqrb   4096 Sep  6 10:51 ..
-rw-rw-r-- 1 sfmqrb sfmqrb    638 Sep  6 11:28 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  92182 Sep  6 10:55 bqt1854.png
-rw-rw-r-- 1 sfmqrb sfmqrb  66580 Sep  6 10:57 bqt2023.png
-rw-rw-r-- 1 sfmqrb sfmqrb  69965 Sep  6 11:25 bqt2242crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  28189 Sep  6 11:25 bqt2417crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb 431133 Sep  6 11:16 bqt2420_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb   9548 Sep  6 11:25 bqt2meta.json
-rw-rw-r-- 1 sfmqrb sfmqrb  81018 Sep  6 11:16 build213.py
-rw-rw-r-- 1 sfmqrb sfmqrb   6504 Sep  6 11:13 c1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3402 Sep  6 11:22 c224_n10.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4812 Sep  6 11:28 c224_n12.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4744 Sep  6 11:22 c224_n1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3203 Sep  6 11:28 c224_n7.png
-rw-rw-r-- 1 sfmqrb sfmqrb  12820 Sep  6 11:27 c229_bibua.png
-rw-rw-r-- 1 sfmqrb sfmqrb   5308 Sep  6 11:27 c229_greek.png
-rw-rw-r-- 1 sfmqrb sfmqrb   5313 Sep  6 11:27 c229_persian.png
-rw-rw-r-- 1 sfmqrb sfmqrb   7793 Sep  6 11:13 c2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4371 Sep  6 11:13 c_gacele.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3485 Sep  6 11:16 c_harmathan.png
-rw-rw-r-- 1 sfmqrb sfmqrb  12347 Sep  6 11:20 c_hdr.png
-rw-rw-r-- 1 sfmqrb sfmqrb   9147 Sep  6 11:16 c_herman2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3841 Sep  6 11:16 c_herman.png
-rw-rw-r-- 1 sfmqrb sfmqrb  12691 Sep  6 11:20 c_ieuo.png
-rw-rw-r-- 1 sfmqrb sfmqrb   2071 Sep  6 11:26 c_ijlak2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  14654 Sep  6 11:20 c_ijlak.png
-rw-rw-r-- 1 sfmqrb sfmqrb  12239 Sep  6 11:20 c_latis.png
-rw-rw-r-- 1 sfmqrb sfmqrb   6280 Sep  6 11:13 c_mag.png
-rw-rw-r-- 1 sfmqrb sfmqrb   6971 Sep  6 11:03 crop1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   8619 Sep  6 11:03 crop2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   5240 Sep  6 11:03 crop3.png
-rw-rw-r-- 1 sfmqrb sfmqrb  12820 Sep  6 11:05 crop_germ.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3408 Sep  6 11:05 crop_guthjo.png
-rw-rw-r-- 1 sfmqrb sfmqrb 111118 Sep  6 11:19 crop_habl.png
-rw-rw-r-- 1 sfmqrb sfmqrb   9001 Sep  6 11:05 crop_node12.png
-rw-rw-r-- 1 sfmqrb sfmqrb   5564 Sep  6 11:05 crop_node1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   5286 Sep  6 11:05 crop_varathra.png
-rw-rw-r-- 1 sfmqrb sfmqrb  11652 Sep  6 11:13 c_xzn.png
-rw-rw-r-- 1 sfmqrb sfmqrb  83691 Sep  6 11:19 gen215.py
-rw-rw-r-- 1 sfmqrb sfmqrb   2303 Sep  6 11:25 j.json
-rw-rw-r-- 1 sfmqrb sfmqrb    228 Sep  6 11:06 jscheck.js
-rw-rw-r-- 1 sfmqrb sfmqrb  37376 Sep  6 11:09 mk201.py
-rw-rw-r-- 1 sfmqrb sfmqrb  77132 Sep  6 11:11 mk207.py
-rw-rw-r-- 1 sfmqrb sfmqrb  61121 Sep  6 11:11 mk208.py
-rw-rw-r-- 1 sfmqrb sfmqrb  80041 Sep  6 11:14 mk214.py
-rw-rw-r-- 1 sfmqrb sfmqrb  67513 Sep  6 11:27 mk217.py
-rw-rw-r-- 1 sfmqrb sfmqrb  17605 Sep  6 11:25 mk218.py
-rw-rw-r-- 1 sfmqrb sfmqrb  50138 Sep  6 11:24 mk222.py
-rw-rw-r-- 1 sfmqrb sfmqrb  17907 Sep  6 11:25 part1.json
-rw-rw-r-- 1 sfmqrb sfmqrb  54688 Sep  6 10:58 pg201.png
-rw-rw-r-- 1 sfmqrb sfmqrb  70083 Sep  6 10:52 pg204.png
-rw-rw-r-- 1 sfmqrb sfmqrb  77858 Sep  6 10:52 pg206.png
-rw-rw-r-- 1 sfmqrb sfmqrb  67371 Sep  6 10:53 pg207.png
-rw-rw-r-- 1 sfmqrb sfmqrb  59146 Sep  6 10:53 pg208.png
-rw-rw-r-- 1 sfmqrb sfmqrb  53054 Sep  6 11:00 pg209.png
-rw-rw-r-- 1 sfmqrb sfmqrb  74515 Sep  6 11:02 pg211.png
-rw-rw-r-- 1 sfmqrb sfmqrb 141781 Sep  6 11:03 pg212hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  75961 Sep  6 11:02 pg212.png
-rw-rw-r-- 1 sfmqrb sfmqrb  83761 Sep  6 11:03 pg213.png
-rw-rw-r-- 1 sfmqrb sfmqrb  83752 Sep  6 11:01 pg214.png
-rw-rw-r-- 1 sfmqrb sfmqrb 194102 Sep  6 11:05 pg215hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb 117034 Sep  6 10:54 pg215.png
-rw-rw-r-- 1 sfmqrb sfmqrb  76564 Sep  6 11:13 pg216.png
-rw-rw-r-- 1 sfmqrb sfmqrb  82798 Sep  6 11:16 pg217.png
-rw-rw-r-- 1 sfmqrb sfmqrb 147278 Sep  6 11:13 pg218hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  82099 Sep  6 11:13 pg218.png
-rw-rw-r-- 1 sfmqrb sfmqrb  71937 Sep  6 11:19 pg219.png
-rw-rw-r-- 1 sfmqrb sfmqrb  63280 Sep  6 11:18 pg220.png
-rw-rw-r-- 1 sfmqrb sfmqrb  71497 Sep  6 11:18 pg221.png
-rw-rw-r-- 1 sfmqrb sfmqrb 118895 Sep  6 11:16 pg222hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  84108 Sep  6 11:16 pg222.png
-rw-rw-r-- 1 sfmqrb sfmqrb  79615 Sep  6 11:18 pg223.png
-rw-rw-r-- 1 sfmqrb sfmqrb  90848 Sep  6 11:22 pg224hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  55412 Sep  6 11:15 pg224.png
-rw-rw-r-- 1 sfmqrb sfmqrb 161218 Sep  6 11:26 pg226hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  74322 Sep  6 11:19 pg226.png
-rw-rw-r-- 1 sfmqrb sfmqrb  54381 Sep  6 11:31 pg227.png
-rw-rw-r-- 1 sfmqrb sfmqrb  52519 Sep  6 11:25 pg228.png
-rw-rw-r-- 1 sfmqrb sfmqrb  78760 Sep  6 11:27 pg229hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  42112 Sep  6 11:26 pg229.png
-rw-rw-r-- 1 sfmqrb sfmqrb 147680 Sep  6 11:20 sns167.jpg
```


## [2026-09-06T15:31:47.007Z] TOOL CALL #53: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg227.png"
}
```


### [2026-09-06T15:31:47.033Z] TOOL RESULT

```

```


## [2026-09-06T15:32:01.546Z] TOOL CALL #54: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json,glob,os\nout=[]\nfor f in sorted(glob.glob('data/extracted/batch/page-*.json')):\n    pg=int(os.path.basename(f).split('-')[1].split('.')[0])\n    d=json.load(open(f))\n    v=None\n    vp=f'data/verification/page-{pg}.json'\n    if not os.path.exists(vp): continue\n    vd=json.load(open(vp))\n    ve={e.get('entry'):e for e in vd['entries']}\n    for i,e in enumerate(d['entries']):\n        if e['root'].get('redirect'): continue\n        for n in e['nodes']:\n            if not n['words'] and n.get('lang') is None:\n                x=ve.get(i,{})\n                vn={m['id']:m for m in x.get('nodes',[])}.get(n['id'])\n                if vn: out.append((pg,n['id'],vn.get('verdict'),(vn.get('derivation') or '')[:180]))\nfor o in out[:8]: print(o)\nprint('total',len(out))\nEOF",
 "description": "Find previous verdicts for truly empty nodes"
}
```


### [2026-09-06T15:32:04.125Z] TOOL RESULT

```
(121, 9, 'unverified', 'An empty box: on the printed page (pdf 121 = book p.91) the arrow out of the Old Persian box points to a rectangle with no language label, no reference and no words — a layout arte')
(137, 6, 'unverified', 'There is nothing to verify: on the printed page (p.107 = pdf 137) the box hanging to the right of the Old Persian box is a completely EMPTY double-ruled rectangle — no language lab')
(171, 5, 'unverified', "Empty pass-through box: on the printed page (pdf p. 171) the box to the right of 'Avestan / Old Persian zana 1' is drawn but contains no language label and no words, so there is no")
(180, 12, 'unverified', "A blank box. The printed page (pdf p.180, kept at data/verification/sources/refs/ocr/BOOK/180.png) shows a genuinely empty double-ruled rectangle to the right of the 'Old Persian u")
(187, 2, 'unverified', 'There is nothing to verify. On the printed page (book p.157 = pdf 187) the arrow leaving the Avestan box runs right across the chart into a plain double-ruled rectangle that carrie')
(189, 2, 'unverified', 'Empty pass-through box: on the printed page (pdf p. 189, book p. 159; see data/verification/sources/refs/ocr/BOOK/189.png) the box to the right of the Avestan box is drawn but left')
(190, 4, 'unverified', 'A blank double-bordered box that the Avestan node arrows into on the printed page (verified on the 400 dpi render of pdf p.190). It carries no language label and no words, so there')
(192, 20, 'unverified', 'A completely blank rectangle to the right of the second Avestan box (âzŭtay, zav 2), reached by an arrow from it on the printed page (checked on the page image). It has no language')
total 21
```


## [2026-09-06T15:32:18.549Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### Watkins superlative\"; grep -n -m6 -iE \"superlative\" AHD_watkins1985.txt | cut -c1-250; echo \"### IEC -isto\"; grep -n -m8 -E \"^-isto|^-is-to|isto-|ōkus|okus\" IEC.txt | cut -c1-200; echo \"### WLD Bd1 p172\"; python3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\nb=t.split('\\f')\nprint(len(b))\nfor leaf in (180,181,182):\n    s=b[leaf] if leaf<len(b) else ''\n    if 'k̑u' in s or 'ōku' in s or 'ōk̑' in s or 'schnell' in s:\n        print('leaf',leaf, s[:1500])\nEOF",
 "description": "Watkins, Mann, Walde-Pokorny checks"
}
```


### [2026-09-06T15:32:21.029Z] TOOL RESULT

```
### Watkins superlative
280:al-1, Beyond. 1. Variant *ol-, “beyond,” in: a. suffixed forms “*ol-se-, *ol-so- in Old Latin ollus in Latin ille (feminine illa); “yonder,” that: ALARM, ALERT, ALLIGA- TOR; b. suffixed forms “*ol-s, *ol-tero- in Latin uls, *ulter, ul
317:aus-?. To draw water. Suffixed form *aus-yo- in Latin haurire, to draw up: EXHAUST, HAUSTELLUM, HAUSTO- RIUM. [Pok. aus- 90.] awi-. Bird. I. 1. Latin avis, bird: AVIAN, AVIARY, AVI- ATION; AVICULTURE, AVIFAUNA, BUSTARD, OCARINA, OSPREY, OSTRICH. 
425:eghs. Out. 1. Variant *eks in: a. Latin ex, ex-, out of, away from: EX!, Ex-; b. Greek ex, ek, out of, from: ECTO-, EXO-, EXOTERIC, EXOTIC; SYNECDOCHE. 2. Suffixed (com- parative) variant form *eks-tero- in Latin exterus, out- ward (feminine abla
442:en. In. 1. Germanic *in in: a. Old English in, in: IN; b. Germanic (comparative) *inn(e)ra in Old English innera, farther in, inner: INNER; C. Germanic *innan in Old English binnan, within (be, by; see ambhi + innan, in, within): BEN!. 2, Latin i
661:ladh-. To be hidden. 1. Greek léthé, forgetfulness: LETH- ARGY, LETHE. 2. Zero-grade form *ladh- (< *bdh-), with nasalized form *landh-, in Greek lanthanein (aorist lathein), to escape the notice of, with middle anthanes- thai, to forget: LANTH
675:leis-?. Small. Germanic comparative */ais-iz(a) and super- lative */ais-ista- in Old English comparative lés, léssa and superlative ést, rest: LEAST, LESS.
### IEC -isto
6274:-istos (-isthios) (1) superlative extn.
6276:-istos (2), collective extn.
8539:Kakio (Kakos, us) “jump; jumper; jumping, agile, springy’. Cf. WP I, 334 Oss. sag ‘stag’; Gk. kekío (Doric: -à-) jump’; Li. Sóku, ti and $okiü, -éti “jump, dance’; cf. Sokus �
11072:moks-, mokust- (?) “case, sheath, pod'. Cf. mokos (1) Skt. cf. makusthah, m. ‘kind of bean’ beside ma$ákah (“skin bottle. Phonology uncertain); (Ober, maska, Per. mask, id. said to be a
11079:moks-, mokust- — molks- (molsk-, molks-)
### WLD Bd1 p172
895
leaf 180                                                 -                            i                                                )     :




172                                                            <3ku-s        — oktu(u)

27,    1 7   4f . ,
                         dessen Yerkniipfung der bait. Worte mit                                         ar. klid-   n.   „H6hle,
Offnung         1
                    ,   A;/(«- „Quelle,         Brunnen“ unter idg. *o<jho- qho- nicht vorzuziehen  :




ist    (s. u.       qhena x - „graben“).
      Ygl.      Curtius                PL 38Stf., Johansson BB. 18, 25;
                             463; bes. J. Schmidt
BrugmannI 2 613f.. II 2 1, 132, 173, 309, II 2 2, 202.       Verkehrt will                                    —
Lewy KZ. 40, 422 oq'i- „sehen‘ mit s-ecfi- „sehen, sagen“ und u-eq'i- „enog“
                                                                i




unter Annahme verschiedener Praeformanten vermitteln. Es ist ja gar
nicht ausgemaclit,                       daB die verbalen Anwendungen                                   in   unserer Sippe    das
altere seien.


oku-s         „schnell‘\
      Ai. (leu- ,,schnell“,                  Komp. (inyirn. Sup. unstha-, av. Cisu- „schnell“, Komp.
ttst/Ct,     Sup. asiZta-.               gr.       lat. d dor ,.schneller“, Sup.
                                               Jjttvs.         tbyJcov.            mxtaxos,
ocissimus (Positiv fehlt), acymr.          ncymr. diog, corn, dio
```


## [2026-09-06T15:32:30.059Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '6270,6290p' IEC.txt | cut -c1-700",
 "description": "Read Mann -istos entry"
}
```


### [2026-09-06T15:32:30.107Z] TOOL RESULT

```
-ister-, adj. theme Av vairy-astaro; Gk. ar-isterà; Lat. sin-ister; OHG win-ister. Cf. also ON ístr, n.; Sw. ister (peritoneal fat’, fr. *en-istero; cf. OPr. instran, n. id.)
-isti, adv. extn. Cf. -iski Gk. cf. skuth-istí, phrug-istí, thrąk-istí; Alb. -isht
(ist-, crasis of a type esost-, q.v.)
Lat. cf. iste, ista, istud; OCS istü ‘selfsame, certain, being, true'; Slovene isti, ista, isto ‘the same’; Latv. ists ‘genuine’
-istos (-isthios) (1) superlative extn.
Skt. cf. -isthah; Av. -isto; Gk. -istos; Go. -ists (and. com. Gmc.); Lat. cf. juxta (*lug(i)stå)
-istos (2), collective extn.
Gk. cf. platán-istos ‘grove of plane-trees'; OCS -ište (fr. *istiom)
isius, see isios (1)
it, ito “as, so, as it were, indeed”. Cf. WP I, 100 Skt. íti; Av. it; Lat. ita; Li. it; Latv. it ‘really, very'
-ità (-otà), abstract formant. Cf. guiuotos, à and the formant -tàt-
Skt. cf. mah-ita, -atā ‘greatness’; Gk. cf. día-
-iskos, à — -itios
10
20
30
35
40
45
436
ita (“way of life’, a wd. of disputed etym. Cf. itis ‘going’, below); W cf. lleu-ad, pl. -adau ‘moon’; Go. aggw-ipa ‘oppression’; OS diur- itha "respect: MHG schem-ede, vüll-ede “shame, fulness’; OE strengt, fylp “strength, filth’; Cz. cf. nov-ota ‘novelty’
```


## [2026-09-06T15:32:45.602Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/-est",
 "prompt": "Give the full etymology entry for the superlative suffix -est: Old English -ost/-est, Proto-Germanic *-istaz/-ostaz, PIE *-is-to-, and any mention of Sanskrit -istha-, Greek -istos, Gothic -ists. Also quote what it says about best, most, first, last if present."
}
```


## [2026-09-06T15:32:47.801Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%81%D8%B1%D9%87%D8%B3%D8%AA/",
 "prompt": "Does this page have an entry for فرهست? Quote the Dehkhoda / Moin / other dictionary definitions and any etymological note (Pahlavi frahist, superlative of freh)."
}
```


### [2026-09-06T15:32:51.472Z] TOOL RESULT

```
I appreciate your detailed request, but I need to be transparent: the webpage content provided doesn't actually contain etymology entries for the superlative suffix "-est" or the related words you mentioned (best, most, first, last).

The content shows only the Etymonline website's navigation, header, footer, and menu structure—not the actual dictionary entries themselves. To provide the etymological information you're seeking (Old English forms, Proto-Germanic roots, PIE origins, Sanskrit and Greek comparatives, etc.), I would need the actual entry pages from Etymonline, which aren't included in what was shared.

To find this information, you'd need to visit etymonline.com directly and search for "-est" or visit the individual entry pages for those words.
```


### [2026-09-06T15:32:55.114Z] TOOL RESULT

```
# فرهست Entry

Yes, this page contains an entry for فرهست with multiple dictionary definitions.

**Dehkhoda Dictionary:**
"در زبان پهلوی فرهست صیغه تفضیلی از فره به معنی بسیار، و خود به معنی بیشتر است" (In Pahlavi, frahist is the comparative form of freh meaning "much," itself meaning "more").

**Moin Dictionary:**
The entry lists two meanings: (1) "بسیار، زیاد" (much, abundant) and (2) "سحر، جادو" (magic, sorcery).

**Amid Dictionary:**
Defines it as "سِحر، جادو" (magic, sorcery), providing a poetic citation.

The etymological note traces the word to Pahlavi *frahist*, explained as a superlative form derived from *freh* (meaning "much/many").
```


## [2026-09-06T15:33:01.989Z] TOOL CALL #59: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/-est",
 "prompt": "Give the English superlative suffix -est etymology: Middle English, Old English -ost/-est, Proto-West Germanic/Proto-Germanic *-ōstaz/*-istaz, PIE *-istos, and cognates (Gothic -ists, Sanskrit -iṣṭha, Greek -ιστος, Avestan -išta)."
}
```


## [2026-09-06T15:33:03.427Z] TOOL CALL #60: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%85%D9%87%D8%B3%D8%AA/",
 "prompt": "Does this page have an entry for مهست? Quote the Dehkhoda / Moin definitions and any etymology (Pahlavi mahist, Avestan mazišta, superlative of مه)."
}
```


### [2026-09-06T15:33:07.798Z] TOOL RESULT

```
# Etymology of English Superlative Suffix -est

The superlative suffix **-est** traces back through multiple language stages:

**English Heritage:**
From "Middle English _[-est](#Middle_English)_, from Old English _[-est](#Old_English)_, _[-ost](/wiki/-ost#Old_English "-ost")_" and ultimately "Proto-West Germanic _[\*-ist](/wiki/Reconstruction:Proto-West_Germanic/-ist "Reconstruction:Proto-West_Germanic/-ist")_."

**Deeper Roots:**
The suffix derives from Proto-Germanic forms that connect to Proto-Indo-European _\*-istos_, showing remarkable stability across language families over millennia.

**Cross-Linguistic Cognates:**
Related forms appear in sister languages including Gothic, Sanskrit, Greek (-ιστος), and Avestan, demonstrating the ancient Indo-European origin of this morpheme.

**Modern Function:**
Today, English speakers append -est to adjectives and adverbs to express superlative degree: "longest, biggest, fastest"—a grammatical pattern preserved from prehistoric times.
```


### [2026-09-06T15:33:08.442Z] TOOL RESULT

```
# Entry for مهست

Yes, this page contains a dictionary entry for مهست.

**Dehkhoda Definition:**
"سنگین و گران" (heavy, weighty) and "مهترین. بزرگترین" (most distinguished, greatest)

**Moin Definition:**
"مهمترین و بزرگترین" (most important and greatest)

**Etymology:**
The page notes that مهست shares a root with English "master/mastery" and Greek "megisti/megasty." The root is identified as مه/مس, meaning greatest, most important, highest, or most abundant. However, the specific etymological connection to Pahlavi or Avestan forms you mentioned is not explicitly stated in this content.
```


## [2026-09-06T15:33:19.019Z] TOOL CALL #61: Bash

```json
{
 "command": "mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg227.png data/verification/sources/refs/ocr/BOOK/227.png && for u in \"https://en.wiktionary.org/wiki/نخست\" \"https://en.wiktionary.org/wiki/تنگ\" \"https://en.wiktionary.org/wiki/زشت\" \"https://en.wiktionary.org/wiki/بهشت\" \"https://en.wiktionary.org/wiki/-est\" \"https://abadis.ir/fatofa/فرهست/\" \"https://abadis.ir/fatofa/مهست/\"; do timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 227, root Isto: superlative suffix -išta and its Persian/English outcomes\" 2>&1 | tail -2; done",
 "description": "Archive web sources and copy page image"
}
```


### [2026-09-06T15:33:26.118Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/9af4affdf884fb80.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3c0babba0e34bb38.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/158f7158c77499bf.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/89d8b292d6ecb9b3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/04dfa715b1b56e7e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c58def9fe275bdac.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c725f68ca861e09c.txt
```


## [2026-09-06T15:33:50.394Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -m2 -E \"^-EST|^BEST|^MOST|^FIRST|^LAST\" SKT.txt | cut -c1-400; echo; grep -n -m1 -A3 \"^BEST\" SKT.txt | cut -c1-400; echo; grep -n -m1 -A3 \"^FIRST\" SKT.txt | cut -c1-400; echo; grep -n -m1 -A3 \"^MOST\" SKT.txt | cut -c1-400",
 "description": "Skeat entries for best/first/most"
}
```


### [2026-09-06T15:33:50.499Z] TOOL RESULT

```
9966:LAST.
```


## [2026-09-06T15:33:53.776Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -m3 -iE \"^ *(best|first|most)[ ,(]\" SKT.txt | cut -c1-500; echo \"--- last\"; sed -n '9960,9975p' SKT.txt | cut -c1-400",
 "description": "Skeat lookups"
}
```


### [2026-09-06T15:33:53.848Z] TOOL RESULT

```
11281:most  (E.)*  M.E.  moit,  mestt.  -  A.  S. iwttf/  +Icel  mtstr,  G.  mtitt^  Goth.  *ftaiits\ dom    as   Aryan    form    MAG-YaN&'TA»
15862:most  likely  solution  is  that  which  derives
15989:Best  (1),  repose.  (E.)  A.  S.  rest,  ntst, rest.  ^-  Du.  mst,  Don.  Swed.  «j/,  Icel rost  (the  distance  between  two  resting- places),  Goth,  rasta  <a  stage),  O.  H.  O. rcsta,  rest.  Allied  to  Ski.  ra-ti,  pleasure, Gk.  ipojij,  rest.  \^  RA.)
--- last
Xiaroeny.  robbery.  (F.-L.)  The -^  is an  E.  addition.  — O.  K.  iarrtcin  (F.  /ara'N), Ifticeny.  —  L.  latrociitium,  robbery  ;  formed with  suflix  -cinium  (as  in  tirthdnium)  from lairo,  a  robber.  Allied  to  Gk.  Xarfis,  a hireling,  ased  in  a  bad  sense ;  the  base appcarx  in  Gk.  Aaf ,  to  get,  seen  in  diroAau- <«>•,  to  get,  enjoy  ;  cf.  L.  iucrutHt  g
Larch,  a  tree,  (F.-L-Gk.)  O.K. lar^i't,  'the  larch  : '  Col.  — L.  Jan'cem,  icc. ot  /arix,  a  larch.  — Gk.  Adpi^,  a  latch.
lATd.  (F.-L.)  O.  F.  iard.^h.  iarda, tarida,  lard,  fat  of  bacon.  Cf.  Uk.  Kap6t, nice.  Aa/Mfof.  fat.  Dor.  lard-tr^  from  O.  F. lardier,  a  tub  to  keep  bacon  in.  hence  a room  in  which  to  keep  bacon  and  meat. Abo  itUcr-lard.
Large.  (F.-L.)  F.  /or^.-L.  fargiu, great.
largess,  a  liberal  gift.  (F.-L.)  F. iar^ifCt  bounty.  — Low  L.  iargifia*,  not found,  put  for  L.  lar^tu,  a  b«stovrtng.— L,  lar^/tts,  pp.  of  largiri,  to  bestow.  mL. iarguj.  Urge,  liberal,
Urk  (1),  a  bird.  (E.)  Another  form  is ^rock  (Bitms).  M.  £.  larJu,  also  iatre «ri.  — A-S.  liwcrct.  later  laucrce,  Uferu. +  Icel.  tavirki,  a  lark  :  Low  G.  ietoerkt, O.  H.G.  ierthha,  G.  Urvhc,  Du.  U€wwrikt Swed.  iarka,  Dan  l^rJU.  p.  The  Icel. l^virki  >  woffcgf  of  w>ft»  ftm  ta,  craft. fiVif,  workf    '         *     '  &.  idwtrt^^JJktf-
LAST.
nwrra*,  worker  of  guile.    The to  some  supersiiiioo  which bird  as  of  ill  omen.
Ijark  (3).  a  game,  Tun.  (EJ intrusive,  the   spelling  being should  rather  be  /oak  (aa  as M.E.  lak,   iokx    (Northern)   /d td£,  sport,  play,  contest.'^ Icel Uk.  Dan.  ieg,  Goth,  iaih ;  cf.  G to  skip  for  joy.     Der.  wed-ioci (where  it  is  a  suffix).
Xianim :  short  for  Alarum.
Larva.  (E.)     l^-iama,  a  gb used  as  a  scientific  name  lor  a
Larynx.    (L.-Gk.)     L.  j
larynx      Der.  iaryng-itit.
Lascar,    a    native    £.    In (Per*. )     Pers.  iashkarf,  a  soldi an  army.
LasoiviouB.  (L.)    Com iasciuus,    lustful.       Cf.    Km caress.  Ski.  lash^  to  desire,  las^ (V  RAS.)
Lash  u)>  to  hind  firmly  tOj{ Da.  lajschtn,  to  join,  scarf  tO£ a  piece,  joint,  scam.  So  also Dan.  iaske,  to  scarf.  Swed. scarf,  joint.  The  verb  is  fro whidi  further  appears  in  Low  C flap,  G.  lascke,  a  flap,  grnove timber.  The  orig,  form  was  p with  the  sen^e  of  flap  ;  see  bel
```


## [2026-09-06T15:34:18.228Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -m6 -E \"fraiSta|fraeSta|fraista|frai.ta|'der meiste|meisten'\" BRT.txt | cut -c1-350",
 "description": "Bartholomae fraēšta"
}
```


### [2026-09-06T15:34:18.279Z] TOOL RESULT

```
13765:•  j.  'duS.dätay- ''  f  'schlechte  Einsicht, Mangel  an  Einsicht':  'iayä»  (GS.  als  AblS.) fraista  dmantS  "wegen  Mangels  an  Ein- sicht sind  die  meisten  glaubensfeiadlich" Aog.  sOm.
14910:Zum  V.  ^«w-.  —  ■".  vgl.  pralyägamana-  n.  — Pü. :  apäc  ratilniA.  —  ')  Vgl.  lu  pain./a%an- und  düraefraiSta-,
17494:'am  meisten'",  nach  Zahl,  Menge,  Um- fang usw.:  mq%raväkahe  .  .  yS  'Um  . . a/irmairyanqm  (Gen.  part  als  Obj.) . .  ava.- jaynat  Yt  1^.105;  —  yat  ba  paiti  'hm kärayeiti  .  .  yavanqnüa  västranqtnca  (sd,; Gen.  part  als  Obj.)  V.  3.  4;  ~  yat  bä paiti  't»m  viksnte  .  .  girihqm  (Gen.  part als  Obj.)  
17498:dl  NSn.(Subj.),  in  V.  3.  5,  6,  12,  aa,  Yt.  13. 105  aU  ASn.  (Obj.)  genommen  werden,  S. aber  die  übrigen  Stellen  und  den  Gebrauch unstes  'am  meisten'.  S.  auch  fräyö  Adv,  — ")  Wie  gr.  ffJjiorov;  s.  KÜHNER  Ausf.Gr.d. Griech.Spr.>  2.  26.  —  31  Vgl.  V.  3.  15,  wo •hm   fehlt.
17499:•  g.  'fraeSta-  m.  'Gesandter,  Bote':  yavsi vTspsi  'tänhs  hr^hämä  "fiir  alle  Zeit  wollen wir  (deine)  Gesandten  sein"  V-^j?.  8".
21808:•  j.  "ytyi^&y^  fraiataii^  (sd.)  F.^e.
```


## [2026-09-06T15:34:23.351Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '17486,17496p' BRT.txt | cut -c1-400",
 "description": "Bartholomae fraēšta headword"
}
```


### [2026-09-06T15:34:23.410Z] TOOL RESULT

```
^ac\A'^:ta^ryascit  fiaca  xlafhs  vänntya  . . fyanhvaityä'*  "auch  in  dunkler  Nacht, (welche  sva.)  wenn  es  .  .  hagelt"  Yt  16. 10,  2)  von  den  Hengsten  der  Arsdvl:
cahwärS  arhina  .  .  misti  .  .  värttUaica sntaiiniaica  srasStaa^a  *fyanhuniaica  3' (3PPM.)  "vier  Hengste  . .  durcheinander lassen  sie  es  regnen  und  schneien  und triefen  und  hageln"  Ylj.  120.
S  '53-  3-  —  ''  Vgl  snarg-  No.  1.—  =»  Lesung  un- sicher; besser  vU.  mit  J  10  fyanhuntyi, S  iSl  d  o,  —  3)  NA.  \»,\/ryai>k'  ohne  Be- merkung;  ebenso  Wo.  Doch  wohl Dmckfe hier.
•  j.  fyanhvattt-  Adj.  (fem.  'vaitl-y'', PPA.:  s.JyarfAva-.
')  Unsicher,  s. /yasflma-  No.  2.
Praes.  27  fii^ya-.
yai^a  aete  nasävö  frikyeiHca  (statt  Plur.) puyäila  "und  wenn  die  Leichname  ver- faulen und  verwesen"  V.ö'.  28; —  'ß-iHyani-.
Et.?").  —    Pa.  naslai'),  —  ">  ai.  mrityaä  'er lerßllt*  reimt  wohl  as\i  fr&y',  ist  aber  nicht identisch  damit,  wie  Gdn.  GIrPh.  *.  52  wilL — ")  Zu  'nas-;  vgl.  dagegen  lU  aftAyant-. •  j.  'fraeöta-  Adj.  'der  meiste'  an  Zahl: *^dus.dätayä  (Sp.7S3m.)  'tai^Yva..)  drvanfö Aog.  $6;  F.  y.  a)  ASn.  'Um  als  Adv.
'am  meisten'",  nach  Zahl,  Menge,  Um- fang usw.:  mq%raväkahe  .  .  yS  'Um  . . a/irmairyanqm  (Gen.  part  als  Obj.) . .  ava.- jaynat  Yt  1^.105;  —  yat  ba  paiti  'hm kärayeiti  .  .  yavanqnüa  västranqtnca  (sd,; Gen.  part  als  Obj.)  V.  3.  4;  ~  yat  bä paiti  't»m  viksnte  .  .  girihqm  (Gen.  part als  Obj.)  V.J.  22;  —  ya^  b3  paiti  'tim bavainü  .  .  g^r
Kompar.  laparau-.  —  Aul  ar.  *pr<4J)iitha;  mit a  aus  uridg.  >.  —  Wgl /räyoA-.  —  Pü.;/«- Uli,  —  0  In  V.  3.  10  könnte  'lfm  syntaktisch
dby  Google
```


## [2026-09-06T15:35:03.086Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nfor f,ws in [('BQT_v1_pages.txt',['بهشت','تنگ']),('BQT_v2_pages.txt',['زشت'])]:\n    t=open(f,encoding='utf-8',errors='replace').read()\n    b=t.split('\\f')\n    for w in ws:\n        # find blocks where the word appears with an adjacent footnote marker style\n        hits=[(i,x.count(w)) for i,x in enumerate(b) if x.count(w)>=3]\n        print(f,w,hits[:6])\nEOF",
 "description": "Locate Borhan pages for behešt, tang, zešt"
}
```


### [2026-09-06T15:35:05.238Z] TOOL RESULT

```
BQT_v1_pages.txt بهشت [(311, 5), (547, 3)]
BQT_v1_pages.txt تنگ [(747, 4), (748, 7), (749, 8), (750, 4), (751, 8)]
BQT_v2_pages.txt زشت []
```


## [2026-09-06T15:35:08.808Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nb=t[311]\nprint(b.split('\\n')[0])\nfor m in re.finditer('بهشت',b):\n    print('...',b[max(0,m.start()-200):m.start()+200].replace('\\n',' | '))\n    print('---')\nEOF",
 "description": "Read Borhan behešt page"
}
```


### [2026-09-06T15:35:10.665Z] TOOL RESULT

```
آردسهشت
... هم‌هست | بسیار وسیم - و مضفف اکردوان هم باشد . | ازذو 4 » بر وزن مرغوله . نلم آشی | است مانشد کاچی و آنرا از آرد عیده پزند . | ار دی .- «نم اول , مخغف اردی بپشت | باشد . و آن نام ماه دوم است ازسال‌شمسی ۴ | از ۵ یبهشت * « بن‌اول » بمعنیآتش | است که بعربی نار خوانند . و تام عاه حوم(») | است از سال شمسی و بودن آفتاب در برح تور | و نام روز سیم از هر ماه شمسی باشد - و نام | فرشته‌ای هم هست که محافظت کوحها کند و | ندييي آمور
---
... بمعنیآتش | است که بعربی نار خوانند . و تام عاه حوم(») | است از سال شمسی و بودن آفتاب در برح تور | و نام روز سیم از هر ماه شمسی باشد - و نام | فرشته‌ای هم هست که محافظت کوحها کند و | ندييي آمور و مصالح ماه اردی بهشت و روز | اردی‌بهشت تملق بدو دارد » و بتابر فاعدث کلی | که نزد فارسیان مقرر است که چون تام ماه با | نام روز موافق آ ید آنروز راعد کنند وجشن | مازند. دربن ماه این روز را عید کنند و جشن | نمایند و آنرا اردی بپ
---
... بعربی نار خوانند . و تام عاه حوم(») | است از سال شمسی و بودن آفتاب در برح تور | و نام روز سیم از هر ماه شمسی باشد - و نام | فرشته‌ای هم هست که محافظت کوحها کند و | ندييي آمور و مصالح ماه اردی بهشت و روز | اردی‌بهشت تملق بدو دارد » و بتابر فاعدث کلی | که نزد فارسیان مقرر است که چون تام ماه با | نام روز موافق آ ید آنروز راعد کنند وجشن | مازند. دربن ماه این روز را عید کنند و جشن | نمایند و آنرا اردی بپشتگان همم خوانند
---
... ند. دربن ماه این روز را عید کنند و جشن | نمایند و آنرا اردی بپشتگان همم خوانند جتح | اول . درین روز نك است بعصبد و آتشکنتنم | رفتن و از بادشاهان حاجت خود خواستنر گت | وکارزار شدن! »ومعنی‌تر کیبی‌این لفت‌مانندبهشت | سیاسی . کیهان. ۲۷۷ . | «هیرون * گونند . | که از شمال بچنوب ۹ | سدوم ریزد « فاعوس مقدس۲ ۳۹-۲ . | ۴ پپلوی ۸۲۵۳۵0 نلم پنج تن از | ۴۳ رك : اردببهشت . | است . شا وهیشته مکی از | فبه + صفیحة ۱۰
---
... اهان حاجت خود خواستنر گت | وکارزار شدن! »ومعنی‌تر کیبی‌این لفت‌مانندبهشت | سیاسی . کیهان. ۲۷۷ . | «هیرون * گونند . | که از شمال بچنوب ۹ | سدوم ریزد « فاعوس مقدس۲ ۳۹-۲ . | ۴ پپلوی ۸۲۵۳۵0 نلم پنج تن از | ۴۳ رك : اردببهشت . | است . شا وهیشته مکی از | فبه + صفیحة ۱۰
---
```


## [2026-09-06T15:35:17.074Z] TOOL CALL #68: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/page-121.json'))\nfor e in d['entries']:\n    for n in e['nodes']:\n        if n['id']==9:\n            print(json.dumps(n,ensure_ascii=False,indent=1)[:2500])\n\"",
 "description": "Inspect previous empty-node record"
}
```


### [2026-09-06T15:35:18.860Z] TOOL RESULT

```
{
 "id": 9,
 "lang": null,
 "words": "",
 "verdict": "unverified",
 "derivation": "An empty box: on the printed page (pdf 121 = book p.91) the arrow out of the Old Persian box points to a rectangle with no language label, no reference and no words — a layout artefact of Nourai's chart software, probably a slot he meant to fill with the New Persian or English continuation of asā-dāru 'ebony' (compare the parallel empty Germanic box, #13, which at least keeps its label). There is nothing to verify; the extraction is faithful to the page.",
 "derivation_fa": "این جعبه در صفحهٔ چاپی خالی است: نه نام زبان دارد، نه ماخذ، نه واژه. پیداست که نورایی جایی برای ادامهٔ asā-dāru گذاشته و آن را پر نکرده است. چیزی برای راستی‌آزمایی وجود ندارد؛ خوانش اسکن نیز با صفحه مطابق است.",
 "sources": [],
 "ref_check": [
  {
   "ref": "None",
   "status": "not_checked",
   "note": "the node carries no references in the book."
  }
 ],
 "consulted": [
  {
   "src": "BOOK",
   "where": "printed page pdf 121 (book p.91), copied to data/verification/sources/refs/ocr/BOOK/121.png",
   "stance": "silent",
   "note": "the box is empty on the page itself."
  }
 ]
}
```


## [2026-09-06T15:42:24.729Z] TOOL CALL #69: Bash

```json
{
 "command": "python3 - <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW = \"https://en.wiktionary.org/wiki/\"\nS_NAX = W+\"نخست\"; S_TANG = W+\"تنگ\"; S_ZESHT = W+\"زشت\"; S_BEH = W+\"بهشت\"; S_EST = W+\"-est\"\nA_FAR = \"https://abadis.ir/fatofa/فرهست/\"; A_MEH = \"https://abadis.ir/fatofa/مهست/\"\n\ndoc = {\n \"pdf_page\": 227,\n \"book_page\": 197,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-06\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Isto\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE superlative suffix *-is-to- (*-isto-), i.e. the zero grade *-is- of the comparative *-yos-/-yes- plus the *-to- of ordinal/superlative adjectives; > Skt. -iṣṭha-, Av. and OP -išta-, Gk. -istos, Proto-Germanic *-istaz / *-ōstaz > OE -est/-ost > E -est\",\n   \"note\": \"The root box is not a lexical root but a morpheme, and as a morpheme it is entirely real and standard. Mann (IEC) lists it as a headword: '-istos (-isthios) (1) superlative extn. Skt. cf. -iṣṭhaḥ; Av. -išto; Gk. -istos; Go. -ists (and com. Gmc.)'. Pokorny illustrates it in situ on the very page Nourai cites at node 6 (IEW 775 s.v. oḱu-s 'quick': 'Kompar. oḱios, Superl. oḱisto-', with Skt. āśiṣṭha-, Av. āsišta, Gk. ōkistos), and Walde-Pokorny I 172 has the same paradigm. Klein s.v. -est (p.543) states the same descent and adds that the suffix was 'formed orig. from the compar. suff. through the addition of a suff. beginning with t'. The language label 'Indo-European' is right. The gloss is half right: '(a suffix meaning) most' is exactly it; 'or last' is loose — the suffix never meant 'last', and Nourai presumably has in view English last/latest, which are -est superlatives of late. One further caveat on the chart as a whole: Nourai writes the suffix detached ('vah-išta', 'kas-išta', 'nazd-išta'), which is a didactic hyphenation, not the way the forms are printed in Bartholomae or Kent.\",\n   \"note_fa\": \"جعبهٔ ریشه در این صفحه واژه نیست، بلکه یک وند است، و به عنوان وند کاملاً درست و شناخته‌شده است: پسوند صفت عالی هندواروپایی آغازین *-is-to- که از صورت بی‌واکهٔ *-is- (از پسوند صفت برتر *-yos-) به‌علاوهٔ *-to- ساخته شده و در سنسکریت -iṣṭha-، در اوستایی و پارسی باستان -išta-، در یونانی -istos و در ژرمنی *-istaz بازتاب یافته است. مان (فرهنگ تطبیقی هندواروپایی، ذیل -istos) همین وند را سرمدخل کرده و پوکورنی در همان صفحهٔ ۷۷۵ که نورایی در گرهٔ ۶ بدان ارجاع می‌دهد صورت‌های oḱisto- / āšiṣṭha- / āsišta / ōkistos را در کنار هم آورده است. پس برچسب «هندواروپایی» و معنای «بیشترین» درست است؛ تنها افزودهٔ «یا آخِر» بی‌جاست، زیرا این وند هرگز معنای «آخِر» نداشته و نورایی گویا واژهٔ انگلیسی last (صفت عالی late) را در نظر داشته است. ادعای کلی نورایی در این جعبه درست است.\",\n   \"sources\": [S_EST],\n   \"ref_check\": [\n    {\"ref\": \"KLN:35\", \"status\": \"partial\",\n     \"note\": \"Klein 1966 p.35 (KLN_1966.txt lines 1893-1896, between the page markers '35' and '36') is s.v. 'aft' and 'after': 'aft ... prop. superlatives formed fr. OE. æf, af, of ... with the Teut. superlative suff. -ta, which corresponds to the I.-E. superl. suff. -to (cp. Gk. prōtos \\\"first\\\")' and, under 'after', '-te-me- are cogn. with OI. -ta-ma ... Avestic -tə-mō (in vahishtō.təmō \\\"best\\\"), L. -tumus, -timus'. So the page does discuss Indo-European superlative suffixes and even cites an Avestan vahišta- compound, but it treats *-to-/*-tem̥o-, NOT *-isto-. Klein's page for the suffix Nourai is charting is 543, which he cites correctly at node 8.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"IEC\", \"where\": \"Mann, s.v. -istos, p.436 (IEC.txt line 6274)\", \"stance\": \"supports\",\n     \"note\": \"'-istos (-isthios) (1) superlative extn. Skt. cf. -isthah; Av. -isto; Gk. -istos; Go. -ists (and com. Gmc.); Lat. cf. juxta' — the root box as a headword in a modern IE dictionary.\"},\n    {\"src\": \"POK\", \"where\": \"IEW 775 s.v. oḱu-s (POK_full.txt line 64412, 'Page(s): 775')\", \"stance\": \"supports\",\n     \"note\": \"'Root / lemma: oḱu-s. Meaning: quick. Grammatical information: Kompar. oḱios, Superl. oḱisto-. Material: Old Indic āśú- ..., Superl. āśiṣṭha-, Avestan āsu- ..., Superl. āsišta, gr. ōkús, ōkistos ... Latin ōcior, Superl. ōcissimus'.\"},\n    {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 172 s.v. ōku-s (WLD_Bd1_pages.txt leaf 180)\", \"stance\": \"supports\",\n     \"note\": \"'ōku-s \\\"schnell\\\". Ai. āśu- \\\"schnell\\\", Komp. āśīyān, Sup. āśiṣṭha-, av. āsu- \\\"schnell\\\", Komp. āsyā, Sup. āsišta. gr. ōkús, ōkistos, lat. ōcior \\\"schneller\\\", Sup. ōcissimus' — the older layer of the same statement.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. leis-2 (AHD_watkins1985.txt line 675)\", \"stance\": \"supports\",\n     \"note\": \"'leis-2. Small. Germanic comparative *lais-iz(a) and superlative *lais-ista- in Old English comparative lǣs, lǣssa and superlative lǣst: LEAST, LESS' — Watkins operates with exactly the Germanic *-ista- of node 8.\"},\n    {\"src\": \"KLN\", \"where\": \"p.543 s.v. -est (KLN_1966.txt line 13663)\", \"stance\": \"supports\",\n     \"note\": \"'-est, suff. forming the superlative degree of adjectives and adverbs. — ME., fr. OE. -ost, -est, rel. to ON. -astr, -str, OHG. -isto, -osto, G. -est, Goth. -ists, -osts, and cogn. with Gk. -tato-, OI. -iṣṭha-; formed orig. from the compar. suff. through the addition of a suff. beginning with t.'\"}\n   ],\n   \"nodes\": []\n  }\n ]\n}\n\nnodes = []\n\nnodes.append({\n \"id\": 1, \"lang\": \"Avestan / Old Persian\", \"words\": \"išta : a superlative suffix\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Correct and well documented. In Old Iranian the inherited *-isto- appears as -išta- (the -s- of *-isto- becoming -š- after i by the ruki rule), added to the bare adjective stem: vaŋhu- 'good' → vahišta-, mas- 'great' → masišta-, kasu- 'small' → kasišta-, āsu- 'swift' → āsišta-, dūra- 'far' → OP duvaišta-. Kent states the equation explicitly under maθišta- (Old Persian, pp.201-202): 'superl. to pIE *mak-ros ... + superl. suffix -isto- (§117, §156.II, §190.I), Gk. -isto-, Av. -išta-, Skt. (with aspiration) -iṣṭha-'. In Middle Persian the suffix survives as -ist (mahist, kahist, frahist, nazdist, naxust), and in New Persian only in petrified words (behešt, zešt, nokhost, mehest), the productive superlative having been rebuilt as -tarin. Nourai's citation form 'išta' (rather than -išta-) and his detached hyphenation are presentational, not errors of substance.\",\n \"derivation_fa\": \"این گره درست است. در ایرانی باستان پسوند *-isto- به صورت -išta- درمی‌آید (تبدیل s به š پس از i بر پایهٔ قاعدهٔ «روکی») و مستقیماً به ستاک صفت می‌پیوندد: vaŋhu- «نیک» ← vahišta-، mas- «بزرگ» ← masišta-، kasu- «خرد» ← kasišta-، āsu- «تیز، تند» ← āsišta-، و در پارسی باستان dūra- «دور» ← duvaišta-. کنت در فرهنگ پارسی باستان (ص ۲۰۱–۲۰۲، ذیل maθišta-) همین را می‌گوید: «پسوند صفت عالی -išta-؛ در یونانی -isto-، در اوستایی -išta-، در سنسکریت -iṣṭha-». در فارسی میانه این پسوند هنوز زایاست (mahist، kahist، frahist، nazdist، naxust) و در فارسی نو تنها در واژه‌های سنگ‌شده مانده است (بهشت، زشت، نخست، مهست)، زیرا صفت عالی با پسوند «-ترین» بازساخته شد. ادعای نورایی در این گره درست است.\",\n \"sources\": [],\n \"ref_check\": [\n  {\"ref\": \"KNT:191\", \"status\": \"supports\",\n   \"note\": \"Kent's lexicon, pp.191-192 (KNT.txt leaves 215-216): p.191 ends with 'dūra- adj. \\\"far (in time or space)\\\": Av. dūra-, NPers. dūr, Skt. dūrá-. See also dū[vaišta-]' and p.192 continues 'duvaišta- adj. \\\"very long, very far\\\": superl. to dūra- (§156.III, §190.II), cf. Skt. daviṣṭha- with slightly different formation. duvaiš[ta]m asn. as adv. \\\"for a long time\\\" DPe 23'.\"},\n  {\"ref\": \"KNT:202\", \"status\": \"supports\",\n   \"note\": \"Kent pp.201-202 (KNT.txt leaves 226-227) s.v. maθišta-: 'adj. \\\"greatest\\\" ... Av. masišta-, NPers. mähist, Gk. mēkistos \\\"longest\\\"; superl. to pIE *mak-ros ... pIE root *mak- \\\"be long and slender\\\" + superl. suffix -isto- (§117, §156.II, §190.I), Gk. -isto-, Av. -išta-, Skt. (with aspiration) -iṣṭha-'. This single sentence underwrites the whole node.\"}\n ],\n \"consulted\": [\n  {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch, passim (BRT.txt: cols. 338 asišta-, 1400 vahišta-, 1693 zōizdišta-, and masišta-, kasišta-, nabā-nazdišta-, spəništa-, ranjišta-, darəzišta-)\", \"stance\": \"supports\",\n   \"note\": \"Bartholomae has a long series of -išta- superlatives as headwords, each marked 'Superl. zu ...' (e.g. 'ranjišta- Adj. \\\"der sich am leichtesten bewegt, der flinkste\\\" ... Superl. zu ranj-'), which is the direct evidence that -išta- is a productive Avestan superlative suffix.\"},\n  {\"src\": \"PHD\", \"where\": \"MacKenzie, A Concise Pahlavi Dictionary, pp.325, 422, 424, 444, 507, 510\", \"stance\": \"supports\",\n   \"note\": \"The Middle Persian continuations of the suffix are listed as ordinary words: 'frahist [p/h(y)st'] most (superlative of frēh)', 'kahist [ksst'] least', 'kamist least', 'mahist greatest', 'naxust first', 'nazdist first'.\"},\n  {\"src\": \"IEC\", \"where\": \"Mann s.v. -istos, p.436\", \"stance\": \"supports\",\n   \"note\": \"'Av. -isto' is listed among the reflexes of the IE superlative extension -istos.\"}\n ]\n})\n\nnodes.append({\n \"id\": 2, \"lang\": \"Avestan\",\n \"words\": \"aša-vah-išta, arta-vah-išta : best justice; vah-išta : best place, heaven; zôižd-išta : most abominable, ugly; tanj-išta : most pulled together, tight\",\n \"verdict\": \"disputed\",\n \"derivation\": \"Three of the four words are impeccable, the fourth does not exist. (1) Av. aṣ̌a-vahišta- is the Gathic Aməša Spənta Aṧa Vahišta 'Best Truth/Right Order' (aṣ̌a- 'truth, cosmic order' + vahišta- 'best'); the Old Persian equivalent has arta- for aṣ̌a-, whence Nourai's second shape arta-vah-išta; his gloss 'best justice' is the usual free rendering of aṣ̌a. (2) vahišta- 'best', superlative of vaŋhu-/vohu- 'good', occupies col.1400 ff. of Bartholomae, where sense 3 is precisely 'das beste Sein, Dasein, Leben; Ort des besten Daseins, Paradies' — i.e. the elliptic vahišta- ahu- 'best existence' that Nourai glosses 'best place, heaven'. (3) zōiždišta- is real and means exactly what he says: Bartholomae col.1693 f. 'zōizdišta- Adj. \\\"der schauderhafteste, abscheulichste\\\", von den xrafstra- ... Superl. zu einem V. *zōizd- \\\"schaudern machen\\\", vgl. zōišnav- und zaēša-'. (4) 'tanj-išta' is NOT an Avestan word: it is in neither Bartholomae's superlative series nor his tanč-/θanj- articles. Nourai has evidently built it out of Horn's guess (Grundriss no.398, 'teng \\\"enge\\\": aw. [superlative] ... Superl. von taxma- \\\"kräftig\\\"') crossed with Hübschmann's correction (Pers. Studien no.398: 'Np. tang \\\"enge, bedrängt\\\" gehört zu tanjīdan \\\"zusammenziehen\\\", skr. tanc, tañj'). Modern Iranian etymology (Cheung s.v. *tanč) knows no superlative here at all and even separates YAv. θanj- 'to pull, draw' from this root. The node therefore takes the worst verdict, though only its last word is at fault.\",\n \"derivation_fa\": \"سه واژه از چهار واژهٔ این گره بی‌عیب است و چهارمی اصلاً وجود ندارد. یکم، اوستایی aṣ̌a-vahišta- همان «اردیبهشت» (اشه وهیشته) از امشاسپندان است: aṣ̌a- «راستی، نظم کیهانی» + vahišta- «بهترین»؛ صورت پارسی باستان آن با arta- به جای aṣ̌a- است، و ترجمهٔ نورایی («بهترین داد») برگردانی آزاد اما پذیرفتنی است. دوم، vahišta- صفت عالی vaŋhu- «نیک» است و بارتولومه (ستون ۱۴۰۰ به بعد) معنای سوم آن را «بهترین هستی؛ جایگاه بهترین هستی، بهشت» می‌آورد، یعنی همان ترکیب کوتاه‌شدهٔ vahišta- ahu-. سوم، zōiždišta- نیز واقعی است: بارتولومه (ستون ۱۶۹۳) آن را «هراس‌انگیزترین، زشت‌ترین» و صفت عالی از فعلی به معنی «لرزاندن، هراساندن» می‌داند. اما چهارم، «tanj-išta» در هیچ فرهنگ اوستایی نیست؛ پیداست که نورایی آن را از حدس هرن (که «تنگ» را از صفت عالی اوستایی می‌گرفت) و تصحیح هوبشمان (که آن را به «تنجیدن» پیوند می‌داد) ساخته است. پژوهش امروزی (چونگ، ذیل ریشهٔ *tanč) هیچ صفت عالی‌ای در کار نمی‌بیند. پس ادعای نورایی در سه واژه درست و در واژهٔ چهارم ساختگی است.\",\n \"sources\": [S_TANG],\n \"ref_check\": [\n  {\"ref\": \"KNT:202\", \"status\": \"partial\",\n   \"note\": \"Kent p.202 states the suffix (s.v. maθišta-, quoted at node 1) but none of these four words is in the Old Persian lexicon; it supports the morphology, not the individual forms.\"},\n  {\"ref\": \"TZF:26\", \"status\": \"not_checked\",\n   \"note\": \"Abolqasemi, Tārix-e moxtasar-e zabān-e fārsi p.26 — no copy on archive.org or on disk (refs_online.json: 'Not on archive.org').\"},\n  {\"ref\": \"BQT:2133\", \"status\": \"partial\",\n   \"note\": \"Fetched with tools/ref_page.py BQT:2133 (vol.4, pdf p.216; image cached at data/verification/sources/refs/ocr/BQT/2133.png). The page carries نزار / نزج / نزد / نزدیک, and Mo'in's footnote reads 'نزدیک: اوستا nazdišta (نزدیک) ... پهلوی nazdīk از: نزد + یک'. It is therefore evidence for the nazd-išta of node 4, not for the four words of this node.\"}\n ],\n \"consulted\": [\n  {\"src\": \"BRT\", \"where\": \"cols. 1400 (vahišta-), 1693-1694 (zōizdišta-); BRT.txt lines 23343, 28149\", \"stance\": \"supports\",\n   \"note\": \"'vahišta-' with the eschatological use 'vahištəm ahūm ... Ort des besten Daseins, Paradies'; and 'j. zōizdišta- Adj. \\\"der schauderhafteste, abscheulichste\\\", von den xrafstra- ... Superl. zu einem V. *zōizd- \\\"schaudern machen\\\", vgl. zōišnav- und zaēša-'. No entry tanjišta- anywhere in the dictionary.\"},\n  {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, s.v. zēšt (NYB_vol2_glossary.txt line 4540)\", \"stance\": \"supports\",\n   \"note\": \"'zēšt [zyšt'] ugly, disgusting ... MPrth zystyft \\\"nastiness\\\"; Paz. NP zišt; cf. Av. (1693) zōizdišta- \\\"the most loathsome\\\", (1651) zaēša- \\\"hideous\\\"' — Nyberg makes the same connection as Nourai, with a 'cf.'.\"},\n  {\"src\": \"CHEUNG\", \"where\": \"Etymological Dictionary of the Iranian Verb, s.v. *tanč (CHEUNG.txt line 24615)\", \"stance\": \"contradicts\",\n   \"note\": \"'*tanč \\\"to twist (together), become narrow, dense, constrict\\\". MIDDLE PERSIAN: ... BMP tng /tang/ \\\"narrow\\\" ... NP tanjīdan/tanj-, NP tang ... PIE *tenk- \\\"to twist together\\\" = Pok.: 1068'; and 'Wa. tanz- ... are unconnected with YAv. θanj- \\\"to pull, draw\\\"'. No superlative *tanjišta- is posited at any stage.\"},\n  {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien no.398 (HUB.txt line 1655)\", \"stance\": \"contradicts\",\n   \"note\": \"'Np. tang \\\"enge, bedrängt\\\" gehört zu tanjīdan \\\"zusammenziehen\\\" ... skr. tanc und tañj (Nr. 394)' — Hübschmann rewrites Horn's Avestan-superlative derivation as a plain derivative of the verb.\"}\n ]\n})\n\nnodes.append({\n \"id\": 3, \"lang\": \"Persian\",\n \"words\": \"Ordîbehešt «اردیبهشت» : \\\"best justice\\\"; behešt «بهشت» : \\\"best place\\\"; zešt «زشت» : ugly; tang «تَنگ ( تنگنا ، تنگه )» : tight\",\n \"verdict\": \"disputed\",\n \"derivation\": \"Ordibehešt and behešt are textbook cases and are exactly as drawn; zešt is the traditional but not the current account; tang does not belong here. (1) اردیبهشت: Av. aṣ̌a-vahišta- → OP *ṛta-vahišta- → MP Ardwahišt (the second month and the third day of every month) → NP Ordibehešt; Hübschmann prints the chain as 'Ardībahišt \\\"der zweite Monat\\\" = phl. Art(a)v(a)hist ..., zd. aša-vahišta-', the Old Persian rt giving MP rd, and the Avestan š of vahišta staying. (2) بهشت: Av. vahišta- (ahu-) → MP wahišt → NP behešt, with the regular Middle-to-New-Persian w- > b- and the a > i/e assimilation to the following vowel; Horn no.246: 'bihišt, behist \\\"Paradies\\\". aw. vahišta- \\\"bester\\\"; phlv. vahist; ai. vásiṣṭha-', Hübschmann adding 'bihist = bahist \\\"Paradies\\\", zd. vahišta- \\\"beste\\\" (sc. ahu- \\\"Welt\\\")' and noting that behist is the older pronunciation, bihist an assimilation. (3) زشت: MP zišt 'hateful, ugly' (MacKenzie p.680) → NP zešt. Nourai's parent zōiždišta- is the derivation of Justi and Fr. Müller, reported by Hübschmann (no.662) and echoed by Nyberg ('cf. Av. zōizdišta-'); modern Wiktionary derives MP zišt directly from Av. zaēša- 'hideous' < PII *ȷ́ʰáyždas < PIE *ǵʰéysd-os (Nourai's own cross-reference 'Gheis'), i.e. from the root noun rather than from the superlative. Same family, different formation — plausible, not proven. (4) تنگ: MP tang 'narrow, tight' → NP tang (and the derivatives tangnā, tange); Cheung derives it from the Iranian root *tanč- (PIE *tenk-, Pokorny 1068), and Wiktionary the same, with no superlative anywhere in the chain. The word is genuinely related to Nourai's cross-referenced root 'Tenk', but it reaches Persian as a plain adjective, not through an -išta superlative.\",\n \"derivation_fa\": \"دو واژهٔ نخست این گره درست و کتابی است، سومی پذیرفتنی با احتیاط، و چهارمی نادرست. «اردیبهشت» از اوستایی aṣ̌a-vahišta- «بهترین راستی» است که در پارسی باستان *ṛta-vahišta- و در فارسی میانه Ardwahišt (نام ماه دوم و روز سوم هر ماه) شده و در فارسی نو «اردیبهشت»؛ هوبشمان همین زنجیره را می‌آورد و دگرگونی rt پارسی باستان به rd پهلوی را قاعده‌ای می‌داند. «بهشت» از اوستایی vahišta- (کوتاه‌شدهٔ vahišta- ahu- «بهترین هستی») از راه پهلوی wahišt است؛ w آغازی در فارسی نو به b بدل شده و a نخست به کسره همگون شده است (هرن، شمارهٔ ۲۴۶: «بهشت … اوستایی vahišta- «بهترین»، پهلوی vahist»). «زشت» از فارسی میانهٔ zišt است؛ پیوند آن با zōiždišta- اوستایی از یوستی و فریدریش مولر است (هوبشمان، شمارهٔ ۶۶۲) و نیبرگ نیز با «قس» همان را یاد می‌کند، اما ویکی‌واژه و پژوهش امروزی آن را یکراست از zaēša- اوستایی (از ریشهٔ هندواروپایی *ǵʰeysd- «هراس، خشم») می‌گیرند، یعنی از خود ریشه نه از صیغهٔ تفضیلی؛ پس این بند «با احتیاط پذیرفتنی» است. اما «تنگ» از فارسی میانهٔ tang است و چونگ و ویکی‌واژه آن را مستقیماً از ریشهٔ ایرانی *tanč- (هندواروپایی *tenk-) می‌دانند؛ هیچ صفت عالی‌ای در میان نیست و این بند از ادعای نورایی رد می‌شود.\",\n \"sources\": [S_BEH, S_ZESHT, S_TANG],\n \"ref_check\": [\n  {\"ref\": \"MON\", \"status\": \"partial\",\n   \"note\": \"Cited without volume/page. Mo'in's own etymological footnotes (in his edition of Borhan-e Qāṭeʿ) do carry these words — see BQT below — but Mo'in's Farhang-e Fārsi as reproduced online (vajehyab/abadis) gives only the bracketed origin tag, so the reference can be confirmed only in substance, not at a page.\"},\n  {\"ref\": \"BQT\", \"status\": \"supports\",\n   \"note\": \"Borhan-e Qāṭeʿ ed. Moʿin, vol.1, s.v. اردیبهشت (BQT_v1_pages.txt leaf 311): the entry explains اردی as 'مخفف اردیبهشت' and 'نام ماه دوم است از سال شمسی ... و نام روز سیم از هر ماه', with Moʿin's footnote giving the Avestan '[ا]شا وهیشته' (OCR 'شا وهیشته') and the Pahlavi form — the same chain the chart draws.\"},\n  {\"ref\": \"TZF\", \"status\": \"not_checked\", \"note\": \"Abolqasemi's history of Persian is not available online or on disk.\"}\n ],\n \"consulted\": [\n  {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no.246 (HRN.txt line 2521) and no.398 (line 3733)\", \"stance\": \"partial\",\n   \"note\": \"no.246 'bihišt, behist \\\"Paradies\\\". aw. vahišta- \\\"bester\\\"; phlv. vahist; ai. vásiṣṭha-. ... Die Aussprache behist ist die ursprüngliche' — supports behešt; but no.398 'teng \\\"enge\\\": aw. [t...]išta- (Superl. von taxma- \\\"kräftig\\\"); phlv. tang \\\"eng\\\"' is the very superlative guess that Hübschmann and Cheung have since discarded.\"},\n  {\"src\": \"HUB\", \"where\": \"Persische Studien p.129 (HUB.txt line 4492), p.190 (line 6712), no.662 (line 2438)\", \"stance\": \"supports\",\n   \"note\": \"'bihist = bahist \\\"Paradies\\\", zd. vahišta- \\\"beste\\\" (sc. ahu- \\\"Welt\\\")'; 'Ardībahišt \\\"der zweite Monat\\\" = phl. Art(a)v(a)hist ..., zd. aša-vahišta-'; 'Np. zišt \\\"hässlich, abscheulich\\\" stellt Fr. Müller ... zu zd. zōiždišta- ..., wie schon Justi im Wb.'\"},\n  {\"src\": \"PHD\", \"where\": \"MacKenzie pp.680, 593, 3038 (index)\", \"stance\": \"supports\",\n   \"note\": \"'zišt [zyšt'] hateful, ugly'; 'tang [tng] narrow, tight'; and in the English index 'paradise garōdmān, wahišt' — the Middle Persian ancestors of zešt, tang and behešt, without any etymology attached.\"},\n  {\"src\": \"CHEUNG\", \"where\": \"s.v. *tanč\", \"stance\": \"contradicts\",\n   \"note\": \"Middle Persian tang and NP tang, tanjīdan are put directly under the root *tanč < PIE *tenk-; no superlative step.\"}\n ]\n})\n\nnodes.append({\n \"id\": 4, \"lang\": \"Avestan\",\n \"words\": \"nazd-išta : closest, first; frâ-išta : most plentiful; mas-išta, math-išta, maz-išta : greatest; kas-išta : least\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"All four are attested Old Iranian -išta- superlatives, and the glosses are right. nazdišta- 'nearest' (superlative to nazd 'near', comparative nazdyō) is best attested in the compound nabā-nazdišta- 'next of kin' (Bartholomae: 'der verwandtschaftlich nächststehende, nächstverwandte'); its Middle Persian continuation nazdist means 'first' (MacKenzie p.510; Nyberg 'nazdist ... Av. nazdišta-'), which is where Nourai's added gloss 'first' comes from. fraēšta- (Nourai's frâ-išta) is Bartholomae's 'j. fraēšta- Adj. \\\"der meiste\\\" an Zahl ... Kompar. frāyaŋh-. Aus ar. *praHišta ... Pü.: frahist' — note that Bartholomae himself already gives the Pahlavi outcome frahist that surfaces in node 5. masišta- is Younger Avestan, mazišta- its variant (vīspe.mazišta- 'greatest of all'), and maθišta- is the Old Persian form (Darius' Ahuramazdā maθišta bagānām 'greatest of the gods'), so the node's language label 'Avestan' is one word too narrow. kasišta- is Bartholomae's 'kasišta- Adj. a) \\\"der kleinste\\\" b) \\\"der geringfügigste\\\"', superlative to kasu- 'small'.\",\n \"derivation_fa\": \"هر چهار صورت این گره در متون ایرانی باستان گواه دارد و معناها درست است. nazdišta- «نزدیک‌ترین» (صفت عالی nazd، با صفت برتر nazdyō) بیش از همه در ترکیب nabā-nazdišta- «نزدیک‌ترین خویشاوند» به کار رفته است؛ بازماندهٔ فارسی میانهٔ آن nazdist به معنای «نخستین» است (مکنزی ص ۵۱۰؛ نیبرگ: «nazdist … اوستایی nazdišta-») و معنای دوم نورایی («نخست») از همین‌جاست. fraēšta- را بارتولومه «بیشترین (از نظر شمار)» می‌آورد و صفت برتر آن frāyaŋh- را یاد می‌کند و حتی برابر پهلوی آن یعنی frahist را می‌دهد. masišta- و گونهٔ mazišta- اوستایی است و maθišta- صورت پارسی باستان (در «اهورامزدا بزرگ‌ترین ایزدان» از داریوش)؛ پس برچسب «اوستایی» برای این یک واژه تنگ است. kasišta- نیز در بارتولومه «کوچک‌ترین، ناچیزترین» است، صفت عالی kasu-. ادعای نورایی در این گره درست است.\",\n \"sources\": [],\n \"ref_check\": [\n  {\"ref\": \"KNT:202\", \"status\": \"supports\",\n   \"note\": \"Kent pp.201-202 s.v. maθišta-: 'adj. \\\"greatest\\\" ... Av. masišta-, NPers. mähist ... superl. ... + superl. suffix -isto- ..., Gk. -isto-, Av. -išta-, Skt. -iṣṭha-'; the attestations maθišta / maθištam follow. Directly covers the mas-išta / math-išta / maz-išta line.\"},\n  {\"ref\": \"BQT:2133\", \"status\": \"supports\",\n   \"note\": \"Borhan vol.4 printed p.2133 (pdf p.216, cached PNG at data/verification/sources/refs/ocr/BQT/2133.png): the نزد / نزدیک article carries Moʿin's footnote 'نزدیک: اوستا nazdišta ... پهلوی nazdīk از: نزد + یک', exactly the Avestan form Nourai puts in this node.\"},\n  {\"ref\": \"TZF:26\", \"status\": \"not_checked\", \"note\": \"no copy of Abolqasemi available.\"}\n ],\n \"consulted\": [\n  {\"src\": \"BRT\", \"where\": \"BRT.txt lines 17494 (fraēšta-), 9387 (kasišta-), 18569 (nabā-nazdišta-), 20129 (masišta-), 24480 (vispe.mazišta-)\", \"stance\": \"supports\",\n   \"note\": \"'j. fraēšta- Adj. \\\"der meiste\\\" an Zahl ... Kompar. frāyaŋh-. Aus ar. *praHišta ... Pü.: frahist'; 'j. kasišta- Adj. a) \\\"der kleinste\\\" ... b) \\\"der geringfügigste\\\"'; 'j. nabā-nazdišta- Adj. \\\"der verwandtschaftlich nächststehende\\\"'; 'j. masišta-, p. maθišta- Adj. \\\"der grösste\\\" 1) der Ausdehnung nach ... 2) dem Rang nach: ahuramazdā ... maθišta bagānām'; 'vispe.mazišta- Adj. \\\"der grösste von allen\\\"'.\"},\n  {\"src\": \"NYB\", \"where\": \"Nyberg II s.v. mas (line 2478 ff.) and nazdist (line 2667)\", \"stance\": \"supports\",\n   \"note\": \"'mas ... sup. masist and mahist ... Av. (1154) mas-, masan-, comp. (1156) masyah-, sup. (1155) masišta-; OP *maθan-, comp. *maθyah-, sup. maθišta-'; 'nazdist [nzdst', nzdyst'] first: adj., adv. — Av. (1060) nazdišta-'.\"},\n  {\"src\": \"PHD\", \"where\": \"MacKenzie pp.325, 422, 444, 510\", \"stance\": \"supports\",\n   \"note\": \"The Middle Persian reflexes stand side by side: 'frahist ... most (superlative of frēh)', 'kahist least', 'mahist greatest', 'nazdist first'.\"},\n  {\"src\": \"HRN\", \"where\": \"Horn no.999 (HRN.txt line 8692)\", \"stance\": \"supports\",\n   \"note\": \"'mih \\\"gross\\\", mehist ... ap. vergl. maθišta- \\\"grösster\\\"; aw. masyaŋh \\\"grösser\\\"; phlv. mas ..., masist, mas(i)st ..., mahist, pāz. meh'.\"}\n ]\n})\n\nnodes.append({\n \"id\": 5, \"lang\": \"Persian\",\n \"words\": \"naxost «نخست ( نزدیک )» : \\\"closest\\\", first; farhast «فَرهَست» : too much, magic; mehast «مِهَست» : greatest; kâst «کاست» : least, deficiency, lacking\",\n \"verdict\": \"disputed\",\n \"derivation\": \"Two of the four are exactly right, two are misattached. (1) نخست: Nourai derives it from nazdišta- 'closest' (hence his parenthetic gloss نزدیک). Phonetically that is impossible — Old Iranian -zd- gives MP -zd-, not -x(w)-, and Av. nazdišta- did in fact yield MP nazdist 'first' (MacKenzie p.510; Nyberg: 'nazdist ... Av. nazdišta-'), a word that simply died out. NP naxost continues MP naxust (Manichaean Middle Persian and Parthian nxwst), which Nyberg files as the superlative of nax(w) 'beginning, the first of anything', and which Wiktionary traces to Proto-Iranian *naxwist- < *naxu- 'first, in front'. The -išta suffix is thus right, the base is wrong. (2) فرهست: exactly right. Av. fraēšta- 'most' → MP frahist 'most' (Bartholomae himself gives 'Pü.: frahist'; MacKenzie p.325 'frahist ... most (superlative of frēh)') → NP farhast. Borhan defines فرهست as 'magic, sorcery', which is why Nourai's gloss is double; Moʿin's footnote and Sadeq Hedayat, whom he quotes there, show that this sense rests on a misunderstanding in Asadi's Loghat-e Fors, the word really meaning 'more, most' — and Dehkhoda says the same ('در زبان پهلوی فرهست صیغه تفضیلی از فره به معنی بسیار'). The verse Nourai prints, 'نیست را هست کند تنبل اوی / هست را نیست کند فرهستش' by Abu-Nasr Marghzi, is the very shāhed Asadi used. (3) مهست: right. Av. masišta-/OP maθišta- → MP mahist (Nyberg: SW mahist beside NW masist) → NP mahist/mehest 'greatest'; Moʿin's footnote in Borhan analyses it as 'مه (بزرگ) + ست (پسوند صفت عالی)'. (4) کاست: misattached. NP kāst is the past stem of kāstan/kāh- 'to diminish' (Cheung *kas¹ 'to be small, diminish, lessen': 'NP kāstan/kāh-'), a verbal noun, not a superlative; the true New-Persian-era heir of kasišta- is MP kahist 'least' (MacKenzie p.422), which did not survive. Right root, wrong formation.\",\n \"derivation_fa\": \"دو واژه از چهار واژهٔ این گره درست و دو تای دیگر به نادرست به این ریشه بسته شده است. «نخست»: نورایی آن را از nazdišta- «نزدیک‌ترین» می‌گیرد (و از همین‌رو در کنارش «نزدیک» نوشته است)، اما این از نظر آوایی شدنی نیست؛ -zd- ایرانی باستان در فارسی میانه -zd- می‌ماند و بازماندهٔ راستین nazdišta- همان nazdist پهلوی به معنی «نخستین» است که از میان رفت. «نخست» دنبالهٔ naxust پهلوی (و پهلوی اشکانی nxwst) است که نیبرگ آن را صفت عالی nax(w) «آغاز، سرِ هر چیز» می‌داند و ویکی‌واژه از ایرانی آغازین *naxu- «پیشین» می‌گیرد؛ پس پسوند درست است و پایه نادرست. «فرهست» کاملاً درست است: اوستایی fraēšta- «بیشترین» ← پهلوی frahist (خود بارتولومه برابر پهلوی را frahist آورده) ← فارسی «فرهست»؛ معنای «جادو» که در برهان قاطع آمده، بنا بر حاشیهٔ معین و یادداشت صادق هدایت و نیز دهخدا («در زبان پهلوی فرهست صیغهٔ تفضیلی از فره به معنی بسیار»)، از بدفهمی اسدی در لغت فرس برخاسته و بیت ابونصر مرغزی که نورایی نقل کرده همان شاهد اسدی است. «مهست» نیز درست است: اوستایی masišta- / پارسی باستان maθišta- ← پهلوی mahist ← فارسی مهست؛ معین در حاشیهٔ برهان می‌نویسد «مهست از: مه (بزرگ) + ست (پسوند صفت عالی)». اما «کاست» ستاک گذشتهٔ «کاستن/کاه-» است (چونگ، ریشهٔ *kas «کم شدن») نه صفت عالی؛ بازماندهٔ kasišta- در فارسی میانه kahist «کمترین» بود که به فارسی نو نرسید. پس در دو بند پژوهش امروزی ادعای نورایی را رد می‌کند.\",\n \"sources\": [S_NAX, A_FAR, A_MEH],\n \"ref_check\": [\n  {\"ref\": \"MON\", \"status\": \"supports\",\n   \"note\": \"Checked through abadis.ir, which reproduces Dehkhoda and Moʿin: s.v. فرهست 'در زبان پهلوی فرهست صیغه تفضیلی از فره به معنی بسیار، و خود به معنی بیشتر است' (Dehkhoda), Moʿin '۱. بسیار، زیاد ۲. سحر، جادو'; s.v. مهست Dehkhoda 'مهترین، بزرگترین', Moʿin 'مهمترین و بزرگترین'.\"},\n  {\"ref\": \"BQT\", \"status\": \"supports\",\n   \"note\": \"Borhan-e Qāṭeʿ vol.3, pdf p.273 (printed ≈1480): headword 'فرهست: بر وزن بدست، به معنی جادو و جادویی و ساحری باشد', with Moʿin's footnote 'پهلوی frahist (صیغهٔ تفضیلی از «فره» به معنی [بسیار]) به معنی بیشتر' and the long note quoting Hedayat ('پازند فرایست به معنی فراوان‌تر و بیشتر می‌باشد و ربطی به جادویی ندارد') together with the Abu-Nasr Marghzi verse Nourai prints. And vol.4, pdf p.152 (printed ≈2069), footnote to مهست: 'مهست از: مه (بزرگ) + ست (پسوند صفت عالی)، در اوستا masišta/mazišta صفت عالی از mas (مه، بزرگ) است به معنی مهترین ... پهلوی mahist'.\"},\n  {\"ref\": \"TZF\", \"status\": \"not_checked\", \"note\": \"no copy of Abolqasemi available online or on disk.\"}\n ],\n \"consulted\": [\n  {\"src\": \"PHD\", \"where\": \"MacKenzie pp.325, 422, 444, 507, 510\", \"stance\": \"partial\",\n   \"note\": \"'frahist ... most (superlative of frēh)', 'mahist ... greatest', 'naxust [nhwst'] first', 'nazdist [nzdst'] first', 'kahist [ksst'] least' — the Middle Persian evidence that naxust and nazdist are two different words and that kasišta- gave kahist, not kāst.\"},\n  {\"src\": \"NYB\", \"where\": \"Nyberg II s.v. naxᵛist (line 2655), Naxᵛ-Ohurmazd (line 2654), nazdist (line 2667)\", \"stance\": \"contradicts\",\n   \"note\": \"'naxᵛist [nhwst'] the first ... MPrth nxwst; MPrs nxwst; Paz. naxust; NP nuxust; sup. of the preceding w.' — and the preceding word is 'Naxᵛ-Ohurmazd ... MPrthPrs nwx \\\"beginning, the first of anything\\\"'. Nyberg thus makes naxust the superlative of nax(w), while nazdišta- is entered separately as the source of nazdist.\"},\n  {\"src\": \"CHEUNG\", \"where\": \"s.v. *kas¹ 'to be small, diminish, lessen' (CHEUNG.txt line 16434)\", \"stance\": \"contradicts\",\n   \"note\": \"'AVESTAN: YAv. kasu- \\\"small, little\\\", YAv. kasiiah- \\\"young\\\"; MIDDLE PERSIAN: ... k'h- /kah-/ \\\"to diminish\\\"; NWIR: NP kāstan/kāh- \\\"to lessen, diminish\\\"' — kāst is the past stem of this verb, not a reflex of kasišta-.\"},\n  {\"src\": \"BRT\", \"where\": \"s.v. fraēšta- (BRT.txt line 17494)\", \"stance\": \"supports\",\n   \"note\": \"'Aus ar. *praHišta ... Pü.: frahist' — Bartholomae himself carries the Avestan superlative through to the Pahlavi word that underlies فرهست.\"}\n ]\n})\n\nnodes.append({\n \"id\": 6, \"lang\": \"Avestan\",\n \"words\": \"spenta-išta : holiest; duva-išta : furthest away; druw-išta : healthiest; âs-išto : fastest; sra-ěšta : most beautiful, best\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"All five are real superlatives and the glosses are right; only one language label needs adjusting. spəništa- (Nourai's analytic 'spenta-išta') is the superlative of spənta- 'bounteous, holy' and is the standing Gathic epithet of Ahura Mazdā's mainiiu- (Bartholomae s.v. mainiiu-: 'mit spəništa- von Aša, Ārm., VM.'; Y.43.16, 45.6, 47.6) — hence Nourai's cross-reference to his root 'Kwen'. duvaišta- 'furthest, longest' is Old Persian, not Avestan: Kent p.192 'duvaišta- adj. \\\"very long, very far\\\": superl. to dūra-, cf. Skt. daviṣṭha-; duvaiš[ta]m asn. as adv. \\\"for a long time\\\" DPe 23'; that is exactly the page (191/192) Nourai cites, so the reference is right and only the box's label is loose. druwišta- 'soundest, healthiest' is the superlative of druua- 'firm, sound' (OP duruva-) and Nyberg reconstructs it as the direct source of MP druyist/drust > NP dorost: 'Av. drva- (= druva-); OP durwa- \\\"firm, secure\\\", sup. *druvišta-, whence in SW druyist ... with -uvt- > -uyt- and -št- > -st-; MPrth drwst; Paz. drust; NP durust'. āsišta- 'swiftest' is the superlative of āsu- and stands in Pokorny on the cited page (IEW 775 s.v. oḱu-s: 'Avestan āsu- \\\"quick, fast\\\", Kompar. āsyā, Superl. āsišta'); Nourai's 'âs-išto' is the nominative singular masculine āsišto. sraēšta- 'most beautiful' (to srīra-) is attested chiefly in the fixed Avestan triad masišta- vahišta- sraēšta- ('the greatest, the best and the most beautiful', Y.1.1, Y.12.9, Yt.13.91 etc.).\",\n \"derivation_fa\": \"هر پنج صورت این گره صفت عالی راستین‌اند و معناها درست است؛ تنها یک برچسب زبانی نیاز به اصلاح دارد. spəništa- صفت عالی spənta- «سپند، مقدس» است و در گاهان صفت همیشگی «مینوی» اهورامزدا (بارتولومه، ذیل mainiiu-)؛ ارجاع نورایی به ریشهٔ «Kwen» نیز درست است. duvaišta- «دورترین، درازترین» پارسی باستان است نه اوستایی: کنت در ص ۱۹۲ آن را صفت عالی dūra- می‌داند و شاهد DPe 23 را می‌آورد — یعنی همان صفحه‌ای که نورایی ارجاع داده؛ پس ماخذ درست است و تنها برچسب جعبه گشاد است. druwišta- «تندرست‌ترین» صفت عالی druua- (پارسی باستان duruva-) است و نیبرگ آن را سرچشمهٔ مستقیم drust پهلوی و «درست» فارسی می‌داند («سوپرلاتیو *druvišta-، با تحول -št- به -st-»). āsišta- «تندترین» صفت عالی āsu- است و پوکورنی در همان صفحهٔ ۷۷۵ آن را آورده است. sraēšta- «زیباترین» (از srīra-) بیشتر در سه‌گانهٔ ثابت اوستایی masišta- vahišta- sraēšta- به‌کار رفته است. ادعای نورایی در این گره درست است.\",\n \"sources\": [],\n \"ref_check\": [\n  {\"ref\": \"KNT:191\", \"status\": \"supports\",\n   \"note\": \"Kent pp.191-192: dūra- at the foot of p.191, and at the head of p.192 'duvaišta- adj. \\\"very long, very far\\\": superl. to dūra- (§156.III, §190.II), cf. Skt. daviṣṭha- ... duvaiš[ta]m asn. as adv. \\\"for a long time\\\" DPe 23'.\"},\n  {\"ref\": \"POK:775\", \"status\": \"supports\",\n   \"note\": \"Pokorny IEW 775 s.v. oḱu-s 'quick': 'Kompar. oḱios, Superl. oḱisto-. Material: Old Indic āśú- \\\"quick, fast\\\", Kompar. āśīyān, Superl. āśiṣṭha-, Avestan āsu- \\\"quick, fast\\\", Kompar. āsyā, Superl. āsišta, gr. ōkús, ōkistos ...' — the exact word āsišta of this node, plus the suffix of the root box.\"},\n  {\"ref\": \"BQT\", \"status\": \"not_checked\",\n   \"note\": \"cited without volume or page; Borhan is a Persian dictionary and has no Avestan headwords, so there is no page to check for these five Avestan superlatives.\"}\n ],\n \"consulted\": [\n  {\"src\": \"BRT\", \"where\": \"BRT.txt lines 19882 (spəništa- s.v. mainiiu-), 20173-20174 (the masišta-/vahišta-/sraēšta- triad), col.338 (āsišta-)\", \"stance\": \"supports\",\n   \"note\": \"'mit spəništa- von Aša, Ārm., VM.: at ahura hyat ... spəništō'; 'in Verbindung mit vahišta- und sraēšta-: yaθa nō masištasca vahištasca sraēštasca ... Y.1.1, Vr.12.4, Yt.13.91'; and the headword 'āsišta-' (col.338).\"},\n  {\"src\": \"NYB\", \"where\": \"Nyberg II s.v. druyist (NYB_vol2_glossary.txt line 1366 f.)\", \"stance\": \"supports\",\n   \"note\": \"'druyist [drwdst'] safe and sound, whole; right, exact ... Av. (782) drva- (= druva-); OP durwa- \\\"firm, secure\\\", sup. *druvišta-, whence in SW druyist ... with -uvt- > -uyt- and -št- > -st-. MPrth drwst; MPrs dryst; Paz. d(u)rust, drust; NP durust.'\"},\n  {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 172 s.v. ōku-s\", \"stance\": \"supports\",\n   \"note\": \"'av. āsu- \\\"schnell\\\", Komp. āsyā, Sup. āsišta' — the same superlative one generation of scholarship earlier.\"},\n  {\"src\": \"PHD\", \"where\": \"MacKenzie p.316 s.v. drust\", \"stance\": \"supports\",\n   \"note\": \"'drust [drw(y)st' | (M dryst), N durust] right; well, healthy' — the Middle Persian reflex of *druvišta-.\"}\n ]\n})\n\nnodes.append({\n \"id\": 7, \"lang\": None, \"words\": \"\",\n \"verdict\": \"unverified\",\n \"derivation\": \"An empty box. On the printed page (pdf 227 = book p.197, copied to data/verification/sources/refs/ocr/BOOK/227.png) the arrow leaving the third Avestan box runs right across the chart into a plain double-ruled rectangle with no language label, no reference and no words — the slot where the Persian outcomes of the five superlatives (above all دُرُست from druwišta-) would have gone, left unfilled. There is nothing to verify, and the extraction is faithful to the page.\",\n \"derivation_fa\": \"این جعبه در صفحهٔ چاپی خالی است: نه نام زبان دارد، نه ماخذ و نه واژه‌ای. پیکان از جعبهٔ سوم اوستایی به مستطیلی تهی می‌رود که جای بازتاب‌های فارسی این صفت‌های عالی (به‌ویژه «درست» از druwišta-) بوده و نورایی آن را پر نکرده است. چیزی برای راستی‌آزمایی نیست و خوانش اسکن با صفحهٔ چاپی مطابق است.\",\n \"sources\": [],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the node carries no references in the book.\"}],\n \"consulted\": [\n  {\"src\": \"BOOK\", \"where\": \"printed page pdf 227 (book p.197), copied to data/verification/sources/refs/ocr/BOOK/227.png\", \"stance\": \"silent\",\n   \"note\": \"the box is empty on the page itself.\"}\n ]\n})\n\nnodes.append({\n \"id\": 8, \"lang\": \"Germanic\", \"words\": \"istaz, isto\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Standard. Proto-Germanic inherited *-isto- as the strong superlative *-istaz (Gothic -ists, ON -astr/-str) beside the parallel *-ōstaz (Gothic -ōsts, OHG -ōsto), and in weak/adjectival inflection as *-istan- (OHG -isto), which is Nourai's second shape 'isto'. Klein sets out the whole set on the page Nourai cites: 'ME., fr. OE. -ost, -est, rel. to ON. -astr, -str, OHG. -isto, -osto, G. -est, Goth. -ists, -osts, and cogn. with Gk. -tato-, OI. -iṣṭha-'. Watkins works with the same reconstruction (Germanic superlative *lais-ista- s.v. leis-²), and Wiktionary routes English -est through Proto-West Germanic *-ist. The derivation from node 1's Old Iranian -išta- is of course not a descent but a shared inheritance from PIE — the chart's arrows always mean 'goes back to the same box above', and here that box is the IE suffix, so nothing is misstated.\",\n \"derivation_fa\": \"این گره استاندارد است. ژرمنی آغازین همان *-isto- هندواروپایی را به دو صورت به ارث برد: *-istaz در صرف قوی (گوتی -ists، اسکاندیناوی کهن -astr) و *-istan- در صرف ضعیف (آلمانی علیای کهن -isto) که همان صورت دوم نورایی، یعنی isto، است؛ در کنار آن گونهٔ *-ōstaz نیز هست (گوتی -ōsts). کلاین در همان صفحه‌ای که نورایی ارجاع داده، همهٔ این صورت‌ها را کنار هم می‌آورد و آن‌ها را با -istos یونانی و -iṣṭha- سنسکریت هم‌ریشه می‌داند. باید توجه داشت که پیکان از گرهٔ ایرانی به ژرمنی در این نمودار به معنی وام‌گیری نیست؛ هر دو میراث مشترک از هندواروپایی‌اند و جعبهٔ بالادست همان وند هندواروپایی است. ادعای نورایی درست است.\",\n \"sources\": [S_EST],\n \"ref_check\": [\n  {\"ref\": \"KLN:543\", \"status\": \"supports\",\n   \"note\": \"Exactly right: the page marker '543' stands at KLN_1966.txt line 13648 and the entry '-est, suff. forming the superlative degree of adjectives and adverbs. — ME., fr. OE. -ost, -est, rel. to ON. -astr, -str, OHG. -isto, -osto, G. -est, Goth. -ists, -osts, and cogn. with Gk. -tato-, OI. -iṣṭha-; formed orig. from the compar. suff. through the addition of a suff. beginning with t' follows at line 13663.\"},\n  {\"ref\": \"AHD:448\", \"status\": \"not_checked\",\n   \"note\": \"Nourai's AHD numbers here are pages of the 1975 American Heritage Dictionary body text (p.448 would fall in the E-words, i.e. the '-est' entry), and that edition is not open online; the 1985 Watkins standalone reprint of the appendix has different pagination. See the 'consulted' entry for what Watkins does say.\"}\n ],\n \"consulted\": [\n  {\"src\": \"KLN\", \"where\": \"p.543 s.v. -est\", \"stance\": \"supports\", \"note\": \"quoted above; the Germanic set *-istaz/*-ōstaz with Gothic -ists, -osts.\"},\n  {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. leis-2 (AHD_watkins1985.txt line 675)\", \"stance\": \"supports\",\n   \"note\": \"'Germanic comparative *lais-iz(a) and superlative *lais-ista- in Old English comparative lǣs, lǣssa and superlative lǣst: LEAST, LESS'.\"},\n  {\"src\": \"IEC\", \"where\": \"Mann s.v. -istos, p.436\", \"stance\": \"supports\", \"note\": \"'Go. -ists (and com. Gmc.)'.\"}\n ]\n})\n\nnodes.append({\n \"id\": 9, \"lang\": \"Old English\", \"words\": \"-est, -ost; lat-est : latest, last; bet-est : best; maě-st : most; fyr-st : first\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"All correct, in Klein's own words. Old English had both allomorphs -ost and -est (Klein p.543), and the four examples are the standard textbook ones. lætost/latost 'latest' → ME latst → last: Klein p.867 'last, adj. — ME. last, dissimilated fr. latst, contraction of latest, fr. OE. latost, superl. of læt'. betst, uncontracted betest 'best': Klein p.167 'best, adj. — ME., fr. OE. best, dissimilated fr. betst, rel. to ON. beztr ..., Goth. batists'. mǣst 'most' (Nourai's 'maě-st' is his rendering of the ligature ǣ): Klein p.1007 'most, adj. — ME. mest, mast, most, fr. OE. mǣst, mast (used as superl. of micel), formed fr. OE. mā \\\"more\\\", and superl. suff. -est; rel. to ... Goth. maists'. fyrst/fyrest 'first': Klein p.597 'first, adj. — ME. first, fr. OE. fyrst, rel. to OS., OHG. furist, ON. fyrstr ... These words are prop. superlatives formed fr. I.-E. *pr̥-, \\\"before\\\"' — i.e. *pr̥-isto-, so it too is an -isto- superlative, just built on a preposition rather than an adjective.\",\n \"derivation_fa\": \"همهٔ داده‌های این گره درست است. انگلیسی باستان هر دو گونهٔ -ost و -est را داشت (کلاین ص ۵۴۳) و چهار نمونهٔ نورایی همان نمونه‌های کلاسیک‌اند: latost «دیرترین» که در انگلیسی میانه به latst و سپس last بدل شد؛ betst (صورت کوتاه‌نشدهٔ betest) «بهترین»؛ mǣst «بیشترین» که کلاین آن را «mā (بیشتر) + پسوند صفت عالی -est» تحلیل می‌کند؛ و fyrst/fyrest «نخستین» که خود صفت عالی ریشهٔ هندواروپایی *pr̥- «پیش» است، یعنی *pr̥-isto-. نگارش «maě-st» در کتاب برگردان نورایی از ǣ انگلیسی باستان است و خطای چاپی یا خوانشی نیست. ادعای نورایی درست است.\",\n \"sources\": [S_EST],\n \"ref_check\": [\n  {\"ref\": \"KLN:1007\", \"status\": \"supports\",\n   \"note\": \"Page marker '1007' at KLN_1966.txt line 24468, and 'most, adj. — ME. mest, mast, most, fr. OE. mǣst, mast (used as superl. of micel, \\\"large, great, much\\\"), formed fr. OE. mā, \\\"more\\\", and superl. suff. -est; rel. to OS. mest, ON. mestr, Du. meest, OHG., MHG., G. meist, Goth. maists, \\\"most\\\"' at line 24482 — the page covers the maě-st of this node.\"},\n  {\"ref\": \"AHD:126\", \"status\": \"not_checked\",\n   \"note\": \"a page of the 1975 AHD body text (p.126 falls among the b-words, i.e. the entry 'best'), which is not open online.\"}\n ],\n \"consulted\": [\n  {\"src\": \"KLN\", \"where\": \"pp.167 (best), 543 (-est), 597 (first), 867 (last), 1007 (most)\", \"stance\": \"supports\",\n   \"note\": \"'best ... fr. OE. best, dissimilated fr. betst'; 'last ... fr. OE. latost, superl. of læt'; 'first ... fr. OE. fyrst ... prop. superlatives formed fr. I.-E. *pr̥-, \\\"before\\\"'.\"},\n  {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etymological Dictionary s.v. most (SKT.txt line 11281)\", \"stance\": \"supports\",\n   \"note\": \"'most (E.) M.E. most, mest. — A.S. mǣst; + Icel. mestr, G. meist, Goth. maists' — an independent witness for OE mǣst.\"},\n  {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. leis-2\", \"stance\": \"supports\",\n   \"note\": \"'Old English ... superlative lǣst: LEAST' — the same OE superlative type.\"}\n ]\n})\n\nnodes.append({\n \"id\": 10, \"lang\": \"English\", \"words\": \"-est; last; best; most; first\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"The Modern English column is simply the phonetic continuation of the Old English one and needs no separate argument: OE -est/-ost > ME -est > E -est (the only productive superlative suffix left, beside the analytic 'most X'); OE latost > ME latst > last (with the -t- of the contracted superlative preserved and the vowel shortened before the consonant cluster); OE betst/betest > best; OE mǣst > ME mest/most > most (the vowel of more having influenced the form, as Klein notes); OE fyrst/fyrest > ME first > first. Klein covers each of the five, and Nourai's own AHD/KLN references are the standard authorities for them.\",\n \"derivation_fa\": \"ستون انگلیسی نو صرفاً دنبالهٔ آوایی ستون انگلیسی باستان است و به استدلال جداگانه نیاز ندارد: -est/-ost انگلیسی باستان به -est امروزی رسیده که تنها پسوند صفت عالی زایای انگلیسی است؛ latost به latst و سپس last؛ betst به best؛ mǣst به mest/most (کلاین یادآور می‌شود که واکهٔ more در صورت most اثر گذاشته است)؛ و fyrst به first. کلاین هر پنج واژه را پوشش می‌دهد و ارجاع‌های خود نورایی (AHD و KLN) در این‌جا همان مرجع استاندارد امروزی‌اند. ادعای نورایی درست است.\",\n \"sources\": [S_EST],\n \"ref_check\": [\n  {\"ref\": \"KLN\", \"status\": \"supports\",\n   \"note\": \"Klein 1966 has all five entries: -est (p.543), last (p.867), best (p.167), most (p.1007), first (p.597), each with the Old English superlative as its immediate ancestor.\"},\n  {\"ref\": \"AHD\", \"status\": \"not_checked\",\n   \"note\": \"cited without a page; the 1975 AHD body text is not open online. Its modern successor (ahdictionary.com) gives the same descent for -est, best, most, first and last.\"}\n ],\n \"consulted\": [\n  {\"src\": \"KLN\", \"where\": \"pp.167, 543, 597, 867, 1007\", \"stance\": \"supports\", \"note\": \"see node 9 for the quotations.\"},\n  {\"src\": \"SKT\", \"where\": \"Skeat s.v. most (SKT.txt line 11281) and last (line 9966 ff.)\", \"stance\": \"supports\",\n   \"note\": \"Skeat likewise derives most from A.S. mǣst and last from the contracted superlative of late.\"},\n  {\"src\": \"AHD\", \"where\": \"Wiktionary/AHD online s.v. -est\", \"stance\": \"supports\",\n   \"note\": \"'From Middle English -est, from Old English -est, -ost, ... from Proto-Indo-European *-istos' — the modern statement of the chain.\"}\n ]\n})\n\ndoc[\"entries\"][0][\"nodes\"] = nodes\nwith open(\"data/verification/page-227.json\",\"w\",encoding=\"utf-8\") as f:\n    json.dump(doc,f,ensure_ascii=False,indent=1)\n    f.write(\"\\n\")\nprint(\"written\")\nPYEOF\npython3 -m json.tool data/verification/page-227.json > /dev/null && echo \"valid json\" && python3 tools/verify_check.py 227",
 "description": "Write and validate page-227 verification"
}
```


### [2026-09-06T15:42:27.171Z] TOOL RESULT

```
written
valid json
nodes verified: 10/10
node verdicts: {'confirmed': 6, 'disputed': 3, 'unverified': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 12, 'partial': 3, 'not_checked': 9}
books consulted: {'supports': 25, 'contradicts': 5, 'partial': 2, 'silent': 1} | by book: {'BRT': 5, 'PHD': 5, 'NYB': 4, 'CHEUNG': 3, 'KLN': 3, 'AHD': 3, 'IEC': 2, 'HUB': 2, 'HRN': 2, 'SKT': 2, 'WLD': 1, 'BOOK': 1}
```


## [2026-09-06T15:42:56.140Z] AGENT

Verification of PDF page 227 (book p. 197) is written to `/home/sfmqrb/git/rishe/data/verification/page-227.json`; `python3 tools/verify_check.py 227` reports 10/10 nodes, 0 PROBLEM lines.

**Page 227 — root "Isto" (PIE superlative suffix *-is-to-); entry 1 (Iu) is a redirect, skipped**
- Verdicts: root confirmed; nodes 6 confirmed, 3 disputed, 1 unverified (the empty box #7, checked on the page image, copied to `sources/refs/ocr/BOOK/227.png`).
- Ref checks: 12 supports, 3 partial, 9 not_checked (TZF has no copy anywhere; AHD:448/126 are 1975 AHD body-text pages, not open online).
- Best finds: KNT:201-202 s.v. maθišta- states the suffix verbatim; POK:775 (oḱu-s, "Superl. oḱisto-", Av. āsišta) supports both the root box and node 6; Mann IEC has "-istos" as a headword; Bartholomae s.v. fraēšta- even gives "Pü.: frahist".

Disputed items:
- #2 `tanj-išta` — no such Avestan word in Bartholomae; Nourai built it from Horn no.398 (since discarded) plus Hübschmann's tanjīdan link.
- #3 `tang` تنگ — Cheung (*tanč < PIE *tenk-) and Wiktionary derive MP/NP tang straight from the root, no superlative step. (`zešt` is only plausible: the zōiždišta- link is Justi/Fr. Müller/Nyberg's "cf."; Wiktionary derives MP zišt from Av. zaēša-.)
- #5 `naxost` نخست — phonetically impossible from nazdišta-; Av. nazdišta- gave MP nazdist "first" (a lost word), while naxust is the superlative of nax(w) "beginning" (Nyberg; Wiktionary PIr *naxu-). `kâst` کاست is the past stem of kāstan/kāh- (Cheung *kas¹); kasišta- gave MP kahist, not kāst.
- Confirmed on the same node: `farhast` = MP frahist, superlative of frēh (Borhan/Moʿin footnote + Dehkhoda; the "magic" sense is Asadi's misreading), and `mehast` = Av. masišta-/OP maθišta- > MP mahist.

No extraction errors: the JSON matches the printed page word for word (including "maě-st" for OE mǣst and the Abu-Nasr Marghzi verse). Only nit: node 6's `duva-išta` and node 4's `math-išta` are Old Persian, though the box is labelled Avestan — noted in the derivations, not counted as errors. Seven web pages archived via `fetch_source.py`; file left uncommitted.
