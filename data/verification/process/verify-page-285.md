# Verification process log — verify-page-285


## [2026-09-06T21:48:11.723Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 285 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-285.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-285.json. Write /home/sfmqrb/git/rishe/data/verification/page-285.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 285` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T21:48:13.415Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T21:48:14.120Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T21:48:14.133Z] TOOL RESULT

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


## [2026-09-06T21:48:14.140Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-285.txt"
}
```


### [2026-09-06T21:48:14.159Z] TOOL RESULT

```
1	=== PDF page 285 (book page 255) ===
2	--- entry 0 ---
3	ROOT [Sanskrit] Kulanjâ : a plant (alpina galanga)  (refs SIN:545)
4	#1 (parent #0) [Persian] refs=MON:1437; SIN:545 | xalanj, xalang «خلنج ، خلنگ» : galingale
5	  #2 (parent #1) [Arabic] refs=PLA:112 | xalanj, xalanjan
6	    #3 (parent #2) [Middle Latin] refs=KLN:635 | galinga
7	      #4 (parent #3) [English] refs=SIN:545; AHD:539; KLN:635 | galingale | NOTE: AHD:539 & KLN:635 derive it from Chinese "Ka0-Liang Čaing: ginger from Kao-Liang". SIN:545 calls this a translation error.
8	--- entry 1 ---
9	ROOT Kumb -> redirect to Gěu 1
10	--- entry 2 ---
11	ROOT [Indo-European] Kund, Kundos : blunt, stout, stocky, rough  (refs IEC:588,589)
12	#1 (parent #0) [Persian] refs=IEC:588 | kond 1 «کند ۱» : blunt, dull, not sharp ; kondî «کندی ۱» : dullness
13	#2 (parent #0) [Sanskrit] refs=IEC:588,589 | kunthah : blunt, strong, hero
14	  #3 (parent #2) [Persian] refs=MON:3088 | kond 2 «کند ۲» : a strong fighter, hero ; kondî 2 «کندی ۲ (کُندا ، گُندا)» : courage ; kondâvar «کنداور ، گنداور» : fighter
15	#4 (parent #0) [Armenian] refs=IEC:588 | kunt, kund : stocky
16	--- entry 3 ---
17	ROOT Kundos -> redirect to Kund
18	--- entry 4 ---
19	ROOT [Indo-European] Kung, Kunki, Kungios : corner  (refs IEC:588,1635)
20	#1 (parent #0) [Persian] refs=IEC:588,1635 | konj «کنج» : corner, hunchback ; konj-kâv «کنجکاو» : "digging into corners", curious
21	#2 (parent #0) [Sanskrit] refs=IEC:1635 | kunče : bend
22	#3 (parent #0) [Armenian] refs=IEC:1635 | knčirn : knot, twist
23	#4 (parent #0) [Dutch] refs=IEC:1635 | konk
24	  #5 (parent #4) [English] refs=IEC:1635 | hunch, hunch-back | NOTE: KLN:750 claims it could be a deformation of "hump"
25	
```


## [2026-09-06T21:48:18.021Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-285.json",
 "description": "Read source JSON for page 285"
}
```


### [2026-09-06T21:48:18.058Z] TOOL RESULT

```
{
  "pdf_page": 285,
  "book_page": 255,
  "entries": [
    {
      "root": {
        "name": "Kulanjâ",
        "lang": "Sanskrit",
        "refs": "SIN:545",
        "gloss": "a plant (alpina galanga)"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "MON:1437; SIN:545",
          "words": [
            {"translit": "xalanj, xalang", "gloss": "galingale", "script": "خلنج ، خلنگ"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Arabic",
          "refs": "PLA:112",
          "words": [
            {"translit": "xalanj, xalanjan", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Middle Latin",
          "refs": "KLN:635",
          "words": [
            {"translit": "galinga", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "English",
          "refs": "SIN:545; AHD:539; KLN:635",
          "words": [
            {"translit": "galingale", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": "AHD:539 & KLN:635 derive it from Chinese \"Ka0-Liang Čaing: ginger from Kao-Liang\". SIN:545 calls this a translation error.",
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Kumb",
        "redirect": "Gěu 1"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Kund, Kundos",
        "lang": "Indo-European",
        "refs": "IEC:588,589",
        "gloss": "blunt, stout, stocky, rough"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "IEC:588",
          "words": [
            {"translit": "kond 1", "gloss": "blunt, dull, not sharp", "script": "کند ۱"},
            {"translit": "kondî", "gloss": "dullness", "script": "کندی ۱"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "نه شمشیر کنداوران ۲ کند ۱ بود - که کین آوری زاختر تند بود",
            "poet": "Sa`dî"
          }
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "IEC:588,589",
          "words": [
            {"translit": "kunthah", "gloss": "blunt, strong, hero", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "MON:3088",
          "words": [
            {"translit": "kond 2", "gloss": "a strong fighter, hero", "script": "کند ۲"},
            {"translit": "kondî 2", "gloss": "courage", "script": "کندی ۲ (کُندا ، گُندا)"},
            {"translit": "kondâvar", "gloss": "fighter", "script": "کنداور ، گنداور"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "نگه کن سواران و گندآوران - چو بهرام و چون زنگهٔ شاوران",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Armenian",
          "refs": "IEC:588",
          "words": [
            {"translit": "kunt, kund", "gloss": "stocky", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Kundos",
        "redirect": "Kund"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Kung, Kunki, Kungios",
        "lang": "Indo-European",
        "refs": "IEC:588,1635",
        "gloss": "corner"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "IEC:588,1635",
          "words": [
            {"translit": "konj", "gloss": "corner, hunchback", "script": "کنج"},
            {"translit": "konj-kâv", "gloss": "\"digging into corners\", curious", "script": "کنجکاو"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "گر همچو روح راه نیابی بر آسمان - اصحاب کهف وار برو کنج غار گیر",
            "poet": "Sanâî"
          }
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "IEC:1635",
          "words": [
            {"translit": "kunče", "gloss": "bend", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Armenian",
          "refs": "IEC:1635",
          "words": [
            {"translit": "knčirn", "gloss": "knot, twist", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Dutch",
          "refs": "IEC:1635",
          "words": [
            {"translit": "konk", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": "IEC:1635",
          "words": [
            {"translit": "hunch, hunch-back", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": "KLN:750 claims it could be a deformation of \"hump\"",
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-06T21:48:18.246Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-06T21:48:18.282Z] TOOL RESULT

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


## [2026-09-06T21:48:23.355Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['SIN','IEC','PLA','MON','KLN','AHD','POK','WLD','SYN','HJB','LKT','SKT','ARY','BQT','HRN','HUB','FSD','WEB','DEV','PHN','LAM','DOZ','AFM','TAD','RCH']:\n    v=d.get(k)\n    if v: print(k, json.dumps(v,ensure_ascii=False)[:600]); print()\n\""
}
```


### [2026-09-06T21:48:25.400Z] TOOL RESULT

```
SIN {"title": "B. Laufer, Sino-Iranica, Chicago 1919 (Field Museum Anthr. Ser. XV.3, pp. 185-630)", "edition_found": "1919", "kind": "archive_djvu", "url": "https://archive.org/details/sinoiranicachine153lauf", "identifier": "sinoiranicachine153lauf (also sinoiranicachin00laufgoog, jstor-29782155)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SIN.txt", "page_offset": "leaf = printed - 172 (e.g. leaf 15 = p.187). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "loo

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 lea

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

HJB {"title": "H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)", "edition_found": "1903 Crooke edition (pagination identical to the 1968 reprint)", "kind": "archive_djvu", "url": "https://archive.org/details/hobsonjobsonagl02croogoog", "identifier": "hobsonjobsonagl02croogoog (others: bub_gb_6Z5iAAAAMAAJ, hobsonjobsonglos00yulerich, india.history.resource.89053)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt", "page_offset": "leaf = printed + 35..51 (plates inserted; e.g. leaf 83 = p.32, leaf 319 = p.270, leaf 535 = p.4

LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt

WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W

DEV {"title": "L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876", "edition_found": "1876", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairety00devi", "identifier": "dictionnairety00devi (also dictionnairetym02devigoog, fr105comparative41)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt", "page_offset": "leaf = printed + 26 (pp. <80) to +30 (pp. >84), e.g. leaf 29 = p.3, leaf 118 = p.88. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.

PHN {"title": "A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, Paris 1866", "edition_found": "1866", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairetym01pihagoog", "identifier": "dictionnairetym01pihagoog (others: bub_gb_QnsSAAAAIAAJ, dictionnairetym00pihagoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt", "page_offset": "leaf = printed + 31 (e.g. leaf 33 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://ar

LAM {"title": "H. Lammens, Remarques sur les mots français dérivés de l'arabe, Beyrouth 1890", "edition_found": "1890", "kind": "archive_djvu", "url": "https://archive.org/details/remarquessurles00lammgoog", "identifier": "remarquessurles00lammgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAM.txt", "page_offset": "leaf = printed + 57 (e.g. leaf 59 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "French headword in caps at line start wit

DOZ {"title": "R. Dozy, Oosterlingen: Verklarende lijst der Nederlandsche woorden die uit het Arabisch, Hebreeuwsch, Chaldeeuwsch, Perzisch en Turksch afkomstig zijn, Leiden 1867", "edition_found": "1867", "kind": "archive_djvu", "url": "https://archive.org/details/oosterlingenver00dozygoog", "identifier": "oosterlingenver00dozygoog (also ...01dozygoog, ...02dozygoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DOZ.txt", "page_offset": "leaf = printed + 11..13 (e.g. leaf 15 = p.2, leaf 43 = p.32). local file has \\f between leaves (0-based leaf index i == i-th form-feed 

AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/

TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640", "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; insi

RCH {"title": "J. Richardson, A Dictionary, Persian, Arabic and English, new ed. by F. Johnson, London 1829 (Lahore reprint 1984)", "edition_found": "1829 Johnson edition (DLI scan, 1814 leaves)", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.24303", "identifier": "in.ernet.dli.2015.24303 (other editions: 1806-10 a-dictionary-persian-arabic-and-english-vol.-i, india.history.resource.17812; 1852 Johnson dictionarypersia00johnuoft)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/RCH.txt", "page_offset": "leaf ~= printed + 93..94 (e.g. leaf 336 =
```


## [2026-09-06T21:48:30.423Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SIN leaf 373 (p545) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==374' SIN.txt | head -80\necho \"=== SIN grep galanga ===\"; grep -n -i 'galang\\|kulanj\\|galingale\\|khalanj' SIN.txt | head -40"
}
```


### [2026-09-06T21:48:32.150Z] TOOL RESULT

```
=== SIN leaf 373 (p545) ===
njan comes  from  India;  and,  as  was  recognized  long  ago,  the  Arabic  word is  derived  from  Sanskrit  kulanja,11  which  denotes  Alpinia  galanga. The  European  forms  with  ng  (galangan,  galgan,  etc.)  were  suggested  by the  older  Arabic  pronunciation  khulangan.12  In  Middle  Greek  we  have
1  Achundow,  Abu  Mansur,  p.  76.
2  Persian  Dictionary,  p.  113.
I  Concerning  ginger  among  the  Arabs,  cf.  Leclerc,  Traite*  des  simples,  Vol.  II, p.  217;  and  regarding  its  preparation,  see  G.  Ferrand,  Textes  relatifs  a  l'Extreme- Orient,  p.  609.
4  Cf.  the  discussion  of  E.  Hultzsch  and  F.  W.  Thomas  in  Journal  Roy.  As.  Soc, 1912,  pp.  475,  1093.   See  also  Yule,  Hobson-Jobson,  p.  374.
6  The  curious  word  for  "ginger"  in  Kuca  or  Tokharian  B,  tvankaro  (S.  Levi, Journal  asiatique,  191 1,  II,  pp.  124,  137),  is  not  yet  explained.
6  Science  Papers,  p.  373.
7  Chinesische  Studien,  p.  219.
8  Glossary  of  Reference,  p.  102.
9  G.  Ferrand,  Textes  relatifs  a  l'Extr6me-Orient,  p.  31.
10  Ibid.,  p.  259.  Cf.  also  Achundow,  Abu  Mansur,  p.  60.
II  Roediger  and  Pott,  Z.  K.  d.  Morgenl.,  Vol.  VII,  1850,  p.  128.
n  E.  Wiedemann  (Sitzber.  Phys.-Med.  Soz.  Erl.,  Vol.  XLV,  1913,  p.  44)  gives as  Arabic  forms  also  xaulangdd  and  xalangan.
546  Sino-Iranica
KokovT^ia,  xauXtfei',  and  7aXaYyd;  in  Russian,  kalgdn.  The  whole  group has  nothing  to  do  with  Chinese  kao-liah-kiah.1  Moreover,  the  latter refers  to  a  different  species,  Alpinia  officinarum;  while  Alpinia  galanga does  not  occur  in  China,  but  is  a  native  of  Bengal,  Assam,  Burma, Ceylon,  and  the  Konkan.  Garcia  da  Orta  was  already  well  posted  on the  differences  between  the  two.2
8.  Abu  Mansur  mentions  the  medical  properties  of  mdmirdn.3 According  to  Achundow,4  a  rhizome  originating  from  China,  and called  in  Turkistan  momiran,  is  described  by  Dragendorff,  and  is  re- garded by  him  as  identical  with  the  so-called  mishmee  (from  Coptis teeta  Wall.),  which  is  said  to  be  styled  mamiraUn  in  the  Caucasus.  He further  correlates  the  same  drug  with  Ranunculus  ficaria  {x&'&bviov to  fxiKpov),  subsequently  described  by  the  Arabs  under  the  name mamirun.  Al-Janki  is  quoted  by  Ibn  al-Baitar  as  saying  that  the mdmirdn  comes  from  China,  and  that  its  properties  come  near  to those  of  Curcuma;1'  these  roots,  however,  are  also  a  product  of  Spain, the  Berber  country,  and  Greece.6  The  Sheikh  Daud  says  that  the  best which  comes  from  India  is  blackish,  while  that  of  China  is  yellowish. Ibn  Batuta7  mentions  the  importation  of  mdmirdn  from  China,  saying that  it  has  the  same  properties  as  kurkum.  Hajji  Mahomed,  in  his account  of  Cathay  (ca.  1550),  speaks  of  a  little  root  growing  in  the mountains  of  Succuir  (Su-cou  in  Kan-su),  where  the  rhubarb  grows, and  which  they  call  Mambroni  Cini  (mdmlrdn-i  Clnl,  "mamiran  of China").  "This  is  extremely  dear,  and  is  used  in  most  of  their  ail- ments, but  especially
=== SIN grep galanga ===
2424:6  In  another  passage  of  his  work  (Ch.  14,  p.  10)  he  has  the  same  text  under Ian  nai  |JLf  *  (Kcempferia  galanga),  but  here  he  merely  adds  that  the  description of  the  Yu  yan  tsa  tsu  is  "a  little  like  Ian  nai."
3591:The  word  galangal,  denoting  the  aromatic  rhizome  of  Alpinia galanga,  is  not  of  Chinese  origin,  as  first  supposed  by  D.  Hanbury,6 and  after  him  by  Hirth7  and  Giles.8  The  error  was  mainly  provoked by  the  fact  that  the  Arabic  word  from  which  the  European  name  is derived  was  wrongly  written  by  Hanbury  khalanjan,  while  in  fact  it  is khulanjan  {xulandZan),  Persian  xawalinjdn.  The  fact  that  Ibn  Khor- dadzbeh,  who  wrote  about  a.d.  844-848,  mentions  khulanjan  as  one  of the  products  of  China,9  does  not  prove  that  the  Arabs  received  this word  from  China;  for  this  rhizome  is  not  a  product  peculiar  to  China, but  is  intensively  grown  in  India,  and  there  the  Arabs  made  the  first acquaintance  of  it.  Ibn  al-Baitar10  states  expressly  that  khulanjan comes  from  India;  and,  as  was  recognized  long  ago,  the  Arabic  word is  derived  from  Sanskrit  kulanja,11  which  denotes  Alpinia  galanga. The  European  forms  with  ng  (galangan,  galgan,  etc.)  were  suggested  by the  older  Arabic  pronunciation  khulangan.12  In  Middle  Greek  we  have
3605:KokovT^ia,  xauXtfei',  and  7aXaYyd;  in  Russian,  kalgdn.  The  whole  group has  nothing  to  do  with  Chinese  kao-liah-kiah.1  Moreover,  the  latter refers  to  a  different  species,  Alpinia  officinarum;  while  Alpinia  galanga does  not  occur  in  China,  but  is  a  native  of  Bengal,  Assam,  Burma, Ceylon,  and  the  Konkan.  Garcia  da  Orta  was  already  well  posted  on the  differences  between  the  two.2
4483:Galangal,  name  not  derived  from  Chi- nese, 545.
5351:Alpinia  galanga  545,  546
5491:Kaempferia  galanga  427 Kaempferia  pundurata  313 Killingea  monocephala  544
```


## [2026-09-06T21:48:42.286Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== IEC leaf around p588 (leaf ~309) ===\"; for n in 308 309 310; do echo \"--- leaf $n ---\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N+1' IEC.txt | head -60; done"
}
```


### [2026-09-06T21:48:46.622Z] TOOL RESULT

```
=== IEC leaf around p588 (leaf ~309) ===
--- leaf 308 ---
�boar’; Li. kiaülé ‘sow’
koulos, is, io (2) ‘round, plump; ball’. Br. kül “fat, plump'; Pol. kula "ball bullet, pommel’; Ukr. kulja “ball, globe’; Cz. koule, id.; R kuP, m. ‘mat-bag, sackfuP; Finn. LW kuula ‘bal’. Cf. also ON haull ‘hernia? and Srb. kulje, fpi. “abdomen”
kounā (keun-) ‘marten, sable’. (Classical forms derive fr. OPer.) Ober. (in Gk.) cf. kaunáke ‘sabie fur’; kauná- kes “fur coat; LW in Assyr. also in gaunakka, and in Lat. gaunaca ‘fur’; ?Gallo- Lat. gunna (gown, fur garment’. LW in Cz. houné ‘shaggy coat'. Initial cons. obscure); OCS kuna (*mar- ten’. LW fr. Sl. in Mod. Gk. kounádi, id.); cf. (e-gde) R écunica “party of sable-hunters'; Li. kiauné ‘marten’; Latv. cauna, id.
koupeio, koupio ‘pile up’. See koupos Cz. kupiti, inf., id.; Li. kaupiu, -ti, id.
koupos, à ‘pile, heap, hill, mountain’. WP I, 372 Av. kaofo ‘hump; mountain'; OPer. kaufa-, id.; Alb. (ambig.) kapë, f. ‘shock of sheaves, pile, bundle’; Olr. (ambig.) cuan (&band, troop’? if fr. *koupna); EME & dial. heaves, want- heaves '*molehill?); OCS kupü, Srb. küp ‘heap’; Li. kaüpas “pile, clod'; LW in Finn. kupo ‘sheaf
(kouros, see kauros ‘cock’)
kouiios, om ‘holding; holder, fastener’ Skt. kaviyah, am *bridle-bit'; cf. also kavah "mi. serly; Hes. koion ‘pledge, hostage'; ON cf. heyja (1) “hold; conduct; organize; acquire"; Latv. (?) kaveju “linger, dally'
kouilos, om (?) ‘hollow, dome’. Cf. koiliom Gk. koilos, kóilos, adj. 'hollow'; koilía, f. id.; OLat. cf. Juno Couella ‘Juno of the Heavens’ beside coelum, caelum 'sky'; Cor. cf. cowl, m. ‘maw’. See next
kouos, à ‘hollow, pit, cavity’. Hes. kóos, id.; It. covo, cova, id.; Sp. cueva, id.; Skt. cf. kav-andhah, -am “barrel, belly, trunk’; Gk. cf. kó-bathos ‘cup’
krab- “dash, rush, attack, snatch'. (Evidence ambig. Cf. krob-) OE hrepian, hreppan ‘touch, attack’; MHG raffen, reffen ‘snatch’; ME & LG rapen ‘snatch, rape’; Du. rapen ‘amass, roughcast';
541
reppen ‘press’; zich — ‘hurry’; cf. rap, adj. ‘nimble; ON hrapa ‘hurl, hasten, tumble’; cf. hrapaór ‘haste’; Li. cf. krabždù, -déti, intr. ‘scuttle’; Latv. cf. krabināju ‘snatch’
krad- (kradāið) ‘shake, dash’. See next & cf. krd- Gk. kradáo, kradaíno, tr. ‘shake’; OE hratian ‘ush’; ON hrata, intr. ‘stagger’; hret, n. ‘storm’; mHG razzen ‘rage’
kradelos, à ‘shaking; shake, rattle’. Cf. krad-, (krd-) & krotolos (1) Gk. kradalós “easily shaken’; krádalos "De. branch’; OE hratele, f. 'yellowrattle'; Du. ratel, m. ‘rattle’ beside reutel ‘rattle in throat; chatter, muttering”, fr. *kradilo-; verbal types: MHG razzeln; Du. ratelen (rush, clatter’, etc.); LG roeteln (*-a-), id.
krádos, om, à “crust, surface’. (Evidence ambig.) Alb. krodhé “crust of bread; scab'; Go. cf. hrot, n. (roof, garret’, lit. ‘surface, top); OHG ruo; (‘soot’: G Russ); Du. roet, id.; OCS cf. (?) krada ‘pyre’. Variants: W crawd (coating, surface’, fr. *krat-, *krot- or *krt-; crawen, f. ‘crust? from a possible *krá$- wh. equates equally w. Alb. krodh&)
kradh- *hurt, harm'. (Evidence ambig.). Mir crád, Ir. crádh ‘torture, anguish’; crádim, cráidim, Ir. crádhaim (torture, vi: ON hræða ‘disquiet’; cpds. hroeóu-
kragilis, os (kragul-) (?) (radical: krag-) W craell, f. ‘aridity’; Du. rekel (2) ‘rake, good- for-nothing'; Icel. hrókl, n. ‘aberration’. Cf. the radical in ON hrak-, cpds. ‘wretched’; mod. hrak ‘trash’; af-hrak ‘outcast’; hrekja, v. ‘reject’. (Latv. kraġis ‘nag? seems to be a LW fr. G Kracke, id.)
kräeg, ið ‘caw, croak’. See next Gk. krázo, pf. kekraga, id.; Lat. pro-crago, ere, pf. -cràxi 'shout'; OE cf. hrace, hracu ‘throat, gorge’: MHG rache, wm. d: Sw. cf. rackla, v. ‘cough up, hawk’; Slovene cf. kro- guljiti ‘ring’; Cz. cf. krahuj, krahujec 'sparrow- hawk
kra
--- leaf 309 ---
gos ^a raucous bird". See above, and cf. krogió Per. (ambig.) kalāy ‘crow’; Hes. kragós, adj. ‘brawling’; cf. Gk. krázo, v. ‘caw’; G Racke
krad- (kradaio) — kraks-
10
20
25
30
35
40
45
542
“a corvine bird"; cf. rackeln, v. ‘caw’; Pol. cf. krogulec *sparrow-hawKk ; Li. krágas ‘coot, dab- chick'. Long-grade in MHG ruoch, Du. roek, OE hroc ‘rook’; OCS kraguj 'sparrow-hawk
krak- (1) “sharp, rough, rugged? Lat. cf. craceó, ere (“grow slim, taper’. Fest.); Br. krak ‘short, sharp’; MHG rach, gs rahes *rough, steep”. (See next for Enn. > Fest.: cra- centes)
krak- (2) (rock, rough ground’. Cf. krok- ' (2) and krak- (1) Br. krag, pl. kragu ‘flint, pebble’; Ir. W. craig "rock beside W crag “crust, coat, shell’; long- gde in Alb. krok 'stony ground” (fr. *-à-) (LW in Eng. crag). (The hapax cracentes is prob. ‘bracing themselves")
krak- (krak-) (3) (?) ‘monster’ Gallo-Lat. cf. cracatius “a large fish’; Li. krake ‘kind of carp’; long-gde in Cz. krak (/sea-mon- ster', fr. *krak-)
krak- (4) limb, leg, foot, step’. (Evidence ambig.) Rum. (substr. or Sl. LW?) crac ‘thigh’; cracá, f. ‘branch’; Cz. krok, m. ‘footstep’ beside (*-a-) OCS krakiü, id.
krak- (5) ‘raucous creature’ Blg. cf. krókon ‘raven’; Li. krakë *bee-eater'; krakis, m. id.; Latv. krakis “hag, crone'. See following entries
krakoró, ið ‘cackle, croak’. Cf. karkar-, kre- kor- Skt. (ambig.) cf. krakarah Cheron" See kreko- ro-); Lat. cracero, åre, v. ‘cackle, croak’; Slo- vene cf. krokár ‘raven’
krako, ið ‘caw, croak’. Cf. krak- (5), krok-, kark-. Onomat. WP I, 414 Alb. krrok, krókem, id. (krr- an expressive variant); Lat. craco, are, id.; W crawcio, id. denom.; OCS kračọ, krakati (also com. SL), id.; Li. krokiu, -ti ‘grunt’; Latv. kràcu, krakt 'rattle, roar, snore'
kraks- (1) ‘scab, crust; scabby’, etc. W crach, m. & adj. “mange; mangy’; Cor cragh *scurf, scab; scabby’; OE cf. hrescian (que- ried: ‘flake off); R kroxà ‘crumb’; króxi, pl. ‘scraps’. Cf. also W craith, pl. creithiau, f. (scar on body? < *kraktis)
kraks- (2)
543
Slovene krohot, m. ‘guffaw’; Latv. cf. krak&ket “crack, crash’
kram- ‘rise, go forward, be forward, be exu- berant, boast Skt. kramami ‘go, march, possess, conquer’; krame, mp. “succeed”; OS hrom-, cpds. 'exu- berance'; OE hreman ‘boast; MHG rüemen ‘boast’; ruom, m. “praise, boasting’; OCS cf. kramola ('sedition, tumult, uproar', also Blg. & Slovene, id.)
kramb- ‘dry, hard; hardening, crust. See next Hes. krámbos ‘dry’; m. ‘shrivelling blight in grapes’; W cram 'incrustation'; cramen ‘scab’; Br. krémen ‘ingrained dirt" (vowel ambig.), cf. MHG ramph, -e (*cramp, spasm; disaster”, if for Gmc. *hr-); Du. ramp, m. ‘disaster’; MLG ramp, -e ‘epilepsy; disaster’. Isophonic: ON hreppa ‘catch, get’; Icel. hrappur 'im- postor’. Variant: Li. kråmas, m. ‘scab’; Latv. krama 'scurf', fr. kramos, å, q. v.
kramos, à, kramn- ‘scab, crust’. Cf. krambos, knàm-. WP II, 583 W crafen ‘flake, crust’; Br. kroen, kroenn, coll. id.; (cf. W variants: crawen “crust? and croen, pl. crwyn “skin, hide’; crofen *erust?); Li. krà- mas, usu. kramai, pl. ‘scurf; Latv. krama, id. (The W variants: crawen & crofen are ambig. cf. knam- and a possible *krabh-)
krank- “noise, jarring, grating, jar, grate". WP I, 414. Cf. kronk-. (The evidence is ambig., and is based on onomat.). Cf. krauk- Per. kulank ((crane" bird); Tokh. B kranko ‘cockerel; ON hregg, n. ‘storm, blast; (Cz. krucet is from krauk-, q.v.); Li. krankiü, ti, v. ‘croak’; cf. krankalas, krankanas, kranklys ‘rook, crow'; Late (ambig.) kroka (2) ‘teal
kranos, à ‘spring, source’. WP I, 488 Gk. kréne (Lesbian: -à-), id.; Alb. krue, T krua, gs kroni, kroi, id.; W c
--- leaf 310 ---
rawn, Cor. croen catch, ment, pool; W cf. croni, v. ‘dam’
krap- (krapl-) EME to ravel (tuntwist, unravel. The mod. mng. contaminated by Nor. Fr. raviller “to muddle’); EMDu. ravelen, as EME, then “to tangle’; NGer. rebbeln ‘card, ripple, shred; Ice! cf. hrafl, n. ‘scraps’; Li. cf krap-stas ‘hackle, carding-comb'. Isophonic: Blg. ù-
kram- — krauk-
15
20
25
30
35
40
45
544
krop ‘torture’; R kropát, v. ‘botch, mangle? kraps- ‘grab, snatch; rapacious; grab, sei- zure’ Br. krafa ‘seize, snatch; scratch, engrave’; kraf ‘seizure’; kraf, m. ‘stylus’: kraf, krav ‘stitch’; W craff ‘quick, keen; secure’; m. pl. -au ‘clasp, cramp’; craffu, v. ‘secure, grip’; Cor. crafa, v. ‘grip’; crāf, adj. ‘tenacious’; s. pl. crafow "basting-stitch"; cf. crefny, adj. ‘grasping, gree- dy’; OE hrespan ‘strip, despoil’; hresp ‘spolia- tion’ krās- (?) ‘glory, praise’ ON hrósa, v. ‘praise’; hrósan, f. ‘praise; boast- ing’; hræsni, f. id.; mod. Icel. hrós, n. ‘praise’; OCS krasa ‘beauty’ (and com. Sl.); Latv. cf. krāšns 'splendid'. See Supt. K : krās- (krast-, see karst-). Variant in W cras ‘toasted, parched, arid’; Br. kraz, id. krateið ‘overpower’. See kratos Gk. kratéo ‘rule’; OCS krostọ, krotiti (tame' and com. Sl.) kratos, is, us “strong; strength, power, force’. WP I, 354 Skt. krátuh “power, will, ability’; Av xratus ‘wisdom’; Ober xraQu-, id.; Gk. kratüs *power- ful”; krátos, n. ‘power’; W crad, craid, m. (“vig- our, force’, fr. *kratos, *kratis); OHG hrad ‘swift; OE hrad “swift, active; ON hraór, id.; OCS cf. krotükü ('tame', lit. overpower- ed"). Isophonic: Li. kratüs (rough, uneven’ krátos, à, is 'enclosure, envelope” W crawd “coating, surface’; OE hréóa 'goat- skin cover, mantle’; cf. hroó-girela ‘crown’; Li. krótai, krótos, mfpl. "lattice, grille’; Latv. krats ‘cage, prison’. (W and OE ambig.) kratsos, ios (?) Lat. crassus ‘fat, gross’; ON hress “hale, hear- ty’; hressa, Lat v. ‘cheer’ (kraug-, variant of krauk-, q. v.). (WP I, 417, 477 & II, 573) Hes. kraugós ‘woodpecker’; Gk. kraugé ‘croak, caw’ krauk- ‘caw, croak; crow, raven’. (Variant: krauk-) EMAIb. krak, mod. krrak ‘a bird of crow type’; OE hrēa (Crumble in the bowels’? Cf. hream ‘uproar’, fr. *kraukmo-?); Pol. Ukr. kruk ‘raven’; Latv. kraukjs ‘rook’ beside krauklis
545
‘raven’. Cf. also Pol. kruczec ‘growl, rumble in bowels’; Cz. krucet ‘croak; rumble in bowels’: Li. kraukiü, ti ‘groan, creak’; Latv. cf. kraukaju ‘hawk, cough up’. Variant in Skt. kró$ah “cry”; ut-kró$ah “osprey?
kraupióo ‘rouse, incite, bully’ (kroup-?) ON hreyfa ‘stir’; Pol. krupic sie ‘bicker’; Li. kraupiü, ti ‘scare; scold, bully’. Ambig: OCZ. krupý, adj. ‘boorish’
kraus- (krausro-) ‘hard’ (krousro-?) Cf. krus-, krust- Gk. cf. kraüros “hard, brittle, coarse’; OCS. kruchü ‘chip, fragment; Cz. kruchy ‘brittle, crisp’; cf. krusec ‘grain of salt, granule’; OCS kruSínü "hard: krusící "metal" (Skt. krüráh ‘tough, hard, cruel, sore); Av. xrüro, id. sug- gests a relationship *-ou-:-ü-, of which *-ou-, or *-au- recurs in OHG bro hrawer: OE hréaw, ON hrár ‘raw’, while *-ü- appears in Lat. crüdus, crüdelis. Extn. in ON hraustr ‘valiant, strong’; hreysti, f. ‘valour’; hreysta, v. ‘encourage’)
krăuos, à (1) ‘mass, heap’ Olr. cró (2) “lot, dead man's property’; Li. krova, kraujà “load, pile’; Latv. cf. krāvums ‘congeries, mass’; verbal in Li. krauju, -ti, Latv. krauju & krauju, -t ‘pile up, load’. Extn. in W crawr ‘heap, huddle’
kráuos (2) ‘cover, shed, shelter, roof. WP I, 477 Olr. cr
```


## [2026-09-06T21:48:55.899Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== kund ===\"; grep -n 'kund-\\|kundos\\|kunthah\\|kunth' IEC.txt | head -30\necho \"=== kung ===\"; grep -n 'kunk-\\|kungios\\|kunki\\|knčirn\\|kncirn' IEC.txt | head -30"
}
```


### [2026-09-06T21:48:55.960Z] TOOL RESULT

```
=== kund ===
8389:kundos ‘stolid, stout, ponderous, stocky’ Arm. kunt & kund, gs knti & kndi, abl. -av “bald; squat, stocky’; Per. kund ‘blunt; stupid’; Hes. kundós ‘stolid, unwavering’; Fris. hont ‘stout fellow, sturdy fellow’. Cf. the variant Skt. kunthah (blunt, fr. a type *kundsios or sim.)
8397:kuntsios (?), kundsios (?) ‘docked, short’. See kund- Skt. kunthah ‘blunt’; R kücyj ‘docked’; Cz. cf. kucel ‘clod, lump?
=== kung ===
4496:gungos (2) ‘incoherent, dumb’. Cf. gungos (1) Hind. gungà ‘dumb’; Per. gung, id.; Gk. cf. gogguzo (mutter, fr. *eunguio); Alb. cf. gung “hard to crack, impotent’; Big. cf. gágna *stam- mer; OCS cf. gognavü, -nivü ‘muttering. Hitt. kunk- is a wd. of uncertain meaning. Cf. also Skt. gufijami ‘hum, buzz (: Gk. goggüzo *tmurmur) and OCS gognajo ‘croon’. LW in Alb. gungás, id.
8390:kungios, io (kungos, à) (1) ‘bulge, hump, mass'. Cf. kunkos, kunkolos & next Skt. kufijah ‘thicket’; Alb. cf. kungé ‘hump, swelling, dome'. Ambig. cf. kunk-); E hunk, hunch (according to dial.); Li. kungis, io, m. *potbelly'; Latv. kungis “belly? beside kungu- lis (and kunkulis *Iump^), w. denasalized tra- ditional parallels in kogars, kogurs ‘tuft
8391:kungios (kung-) (2) (?) ‘corner’. Cf. kungios (1) Per. kunj (kung), id.; MDu. (alleged) honc ‘corner’; Du. Fris. honk, s. ‘home’. (Iso- phonic: E hunch “inspiration, idea; hunch- back’; Du. honk (2) “aim, target")
8392:kunkolos, is, à “ball, Jump, knob, peak’. Cf. kungios (1), kunkos, konkolos Alb. (ambig.) küngull, m. ‘marrow, pumpkin; Li. kufikulas ‘bubble’; kunkulýs, m. “bubble; post, pillar’; Latv. kunkulis ‘small lump”
8395:*kunkio (?)). (The phonology of Oss. kunc, kuncä ‘bellows’ is uncertain)
```


## [2026-09-06T21:48:58.907Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '8375,8405p' IEC.txt"
}
```


### [2026-09-06T21:48:58.956Z] TOOL RESULT

```
kumbulið (kumblið) lumber along, dawdle, potter MLG hümpeln ‘potter, dawdle’; LG humpeln limp’; Du. hompelen, id..; Cz. kublat *con- fuse’; kublat se ‘dally, dawdle, potter’; cf.
kumbolos, à, ios — kunkos, à, io
10
20
25
30
35
40
45
588
kubla, m. f. s. ‘idler’; Li. cf. (variant) kum- brinu, -ti, v. ‘amble along, be huddled’
(kumolos (1) and (2), see Supt: K)
kump- “bend, hump, crook’. Cf. WP I, 350, 373 & 376. (Cf. kumb- with some ambiguity in the Celtic forms) Skt. kumpah, adj. ‘with arm crooked'; MIr. comm ‘trunk, waist; W cf. cwman (2) ‘tump’; E dial. (ambig.) hum ('arse', cf. kum-); Du. (?) hom ‘milt’; Pol. kepa ‘hillock; tuft; clump of trees; Li. kumpas (hunchbacked'; kümpa ‘Jump, bump, gnur!’ beside Li. & Latv. kum- pis, m. ‘ham’; Latv. cf. also kumpju, t, v. “get humped, grow hunchbacked'; Li. kumpstu, kumpti ‘get bent’; Finn. LW kumpu ‘hillock’
(kundəlos, see kondulos)
kundos ‘stolid, stout, ponderous, stocky’ Arm. kunt & kund, gs knti & kndi, abl. -av “bald; squat, stocky’; Per. kund ‘blunt; stupid’; Hes. kundós ‘stolid, unwavering’; Fris. hont ‘stout fellow, sturdy fellow’. Cf. the variant Skt. kunthah (blunt, fr. a type *kundsios or sim.)
kungios, io (kungos, à) (1) ‘bulge, hump, mass'. Cf. kunkos, kunkolos & next Skt. kufijah ‘thicket’; Alb. cf. kungé ‘hump, swelling, dome'. Ambig. cf. kunk-); E hunk, hunch (according to dial.); Li. kungis, io, m. *potbelly'; Latv. kungis “belly? beside kungu- lis (and kunkulis *Iump^), w. denasalized tra- ditional parallels in kogars, kogurs ‘tuft
kungios (kung-) (2) (?) ‘corner’. Cf. kungios (1) Per. kunj (kung), id.; MDu. (alleged) honc ‘corner’; Du. Fris. honk, s. ‘home’. (Iso- phonic: E hunch “inspiration, idea; hunch- back’; Du. honk (2) “aim, target")
kunkolos, is, à “ball, Jump, knob, peak’. Cf. kungios (1), kunkos, konkolos Alb. (ambig.) küngull, m. ‘marrow, pumpkin; Li. kufikulas ‘bubble’; kunkulýs, m. “bubble; post, pillar’; Latv. kunkulis ‘small lump”
kunkos, à, io “lump, hump, bulge’. Cf. kung-, elc. Alb. (ambig.) kungë, f. id.; (R (ambig.) küca ‘heap, mass, crowd" preferably to kaukos (1), q.v); Li. cf. kunksoti, inf. ‘bulge; huddle together; Latv. cf. kunce, f. (*tadpole', fr.
589
*kunkio (?)). (The phonology of Oss. kunc, kuncä ‘bellows’ is uncertain)
kūnos ‘lump, swelling, body’. Cf. WP I, 367 Per. kün ‘arse’; Br. kin “bud, germ of wheat’; ON honn, gs hüns, m. (1) ‘knob’; Li. kūnas “body”; Latv. cf. künis (2) “abdomen
kuntsios (?), kundsios (?) ‘docked, short’. See kund- Skt. kunthah ‘blunt’; R kücyj ‘docked’; Cz. cf. kucel ‘clod, lump?
kūpā, os, is (1) ‘hollow, container, cup- shape, bonnet’. WP I, 372 Skt. kūpah ‘ditch, hollow’; Hiero-Hitt. kupas (queried: ‘tomb’); (?) Lyc. cf. gopa, gopu ‘tomb’; Myc. cf. kupera (queried: kupélla 'goblets'); Hes. küpe “hut; boat; Lat. cüpa ‘barrel’; MIr. cúa ‘cup, bowl’; ON hüfr “hull, hulk’; húfa ‘cap, bonnet; vault’; Sw. huv, m. ‘penthouse’; huva, f. ‘hood’; Du. huif ‘coif, hood, awning, hamper, basket-cart?; OE hyf, f. ‘hive’; OFris. hüve, f. ‘hood’; OHG hüba, G Haube, id.; Cz. (LW?) kypa ‘dyer’s vat’; Finn. LW kuoppa ‘hollow’
kūpā, os (2) ‘effervescence’. Cf. kupið (2) and kuprið. See next E (fr. Scots) hives ‘rash, eczema’; Cz. cf. ná- kyp ‘puff-pudding’
kupəlos (kupilos) ‘bulge, swelling, mass, pile; bulging, luxuriant. WP I, 373 Hes. cf. kúpalon (queried: ‘allocation, lot); Gk. cf. küpellon ‘bulging cup’; OHG hubil, MHG hübel, hubel, m. ‘hil’; Du. cf. heuvel, m. (id. but phonology ambig.); Li. kuplùs, adj. ‘spreading, luxuriant’; Latv. kupls ‘dense, bushy’. See next
kupəros, å ‘hump, bulge; humped, bulging’. WP I, 373. Cf. kupolos Oss. cf. Kubír “bud; hill beside Kubár (*ball, lump’. Phonol. uncertain); Gk. küparos ‘butt’; MIr. cúar “bent; hoop, circle; swelling; OHG hovar, MLG hover, OE hofer, hofor ‘hump’; Li. kuprà, id.; Latv. kupris, id.; Finn. LW kupera ‘humped’; kuperuus ‘hump’
kupəst-, kupst- ‘hump, hollow’ Ir. cuas ‘hollow’; Li. kupstas ‘hillock’; kupstis, gs -čio ‘pile’
kupið (kupàio) (1) ‘browbeat, bully, bawl, - brawl
künos — kur-
10
```


## [2026-09-06T21:49:12.535Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n 'kn[čcs]irn\\|kncirn\\|knjirn\\|kunč\\|kunce\\|kunc[ae]\\b' IEC.txt | head -20\necho \"--- find printed page 1635 ---\"\ngrep -n '^1635$\\|1635' IEC.txt | head -20"
}
```


### [2026-09-06T21:49:14.614Z] TOOL RESULT

```
8393:kunkos, à, io “lump, hump, bulge’. Cf. kung-, elc. Alb. (ambig.) kungë, f. id.; (R (ambig.) küca ‘heap, mass, crowd" preferably to kaukos (1), q.v); Li. cf. kunksoti, inf. ‘bulge; huddle together; Latv. cf. kunce, f. (*tadpole', fr.
--- find printed page 1635 ---
```


## [2026-09-06T21:49:18.011Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nwc -l IEC.txt; awk 'BEGIN{RS=\"\\f\"} END{print NR\" leaves\"}' IEC.txt\necho \"--- last lines ---\"; tail -20 IEC.txt\necho \"--- grep 163x page markers ---\"; grep -n '16[0-9][0-9]' IEC.txt | tail -20"
}
```


### [2026-09-06T21:49:19.967Z] TOOL RESULT

```
20498 IEC.txt
858 leaves
--- last lines ---
‘moisture’; OCS vlaZinú, Cz. vlahý and vlažný ‘damp’, fr. *uolg-. Variant of type ulog- in OE wlzec E wlacu, adj. 'tepid) Lusatian wloha ‘moisture’ confirms o-gde, as Latv. velgs, adj., velgt, v. beside valgs, valgt ‘moist; become moist. Skt. vrjánam, n., vrjanih ‘sky; cloud? is isolated
ulgh- ‘tepid’. Variant of ulg- (?). Cf. uolgh- Arm. gayğ, Let id.; Icel. volgur, id.
ulguó, v., ulguos, us, s. ‘surge’. Variant in ON ulguh-? but cf. uluos, uluió Gk. cf. (?) kas-albás, gs: -albádos, f. (harlot', if for *kmt-, q. v. and *ulgu-); Lat. vulgus, gs: -i, m. & n. ‘crowd, rabble’ beside volgiolum, n. ‘roller’; volgi-vagus ‘wandering, strolling’; Icel. cf. volk, n. ‘billowing; toil’ (beside ylgja, f. ‘swell, surge’ fr. (?) *ulguhiə. Lat. vulba ‘bag, budget, late Lat. bulga is ambig. Skt. várgā ‘sect, class’ seems to be unrelated)
(ulio (1) ‘wind, wrap’, see uluið; (2) ‘boil’, see ulāið)
ulksuos, à (ul'suos, à) (?) ‘sorcerer, prophet Gk. cf. (?) álsos, n. ‘sacred grove’; ON cf. volva ‘prophetess’; OCS vlüxvü, m. ‘prophet’; vlüxvij, adj. *magical'; Blg. vláxva, m. *high- wayman'; LW in Finn. velho ('sorcerer', vocal- ism of Finn. verho “top”, cf. urks- (4))
ulm- ‘surge, billow; wide mouth, gulf’. WP I, 298. Gk. ambig. & uncertain Skt. ürmíb, mf. ‘wave, billow’; Gk. cf. lámos, m. ‘gulf; lámia, f. ‘monster, wide-mouthed fish’; cf. lamurós ‘deep, awful; riotous’; Arm. cf. aymuk, gs: aymki, ab. s. aymkav, s. *up- roar’; OE wylm, m. ‘surge, billow, boiling’; G (7) Wolm, m. ‘archway, porch, curved ba- nister’; ON olmr, adj. ‘wild, boisterous’. (Iso- phone: Li. vilminti, inf. ‘cheat’)
uln- (1) (ulna, ulon-) ‘wool’. WP I, 206. (Var- iant initial in Oss.) Skt. urna, f. id.; Av. cf. una, f. “lock, curl’; Oss. cf. qun, Dig. gun, s. ‘wool, hair’; Hitt. cf. hulana-, Luvian hulani- (queried: *wool"); Lat. lana, f. id.; Ir. olann, gs: olna & olla, f. id.; W gwlan, OBr. gulan, Breton gloan, m. id.; OHG wolla, f. id.; Go. wulla, f. id.; OE wull, wll f. id.; ON ull, ds: ullu, f. id.; OCS vlüna, Cz. vina, Pol. wełna, Big. vlána, id.; Li. vilna, Latv. vilna, id.
ulgh- — ulquos, is
20
25
30
35
40
45
1554
uln- (2) (ulnis, à) ‘surge, wave’. WP I, 302- 3. (Gk. ambig.) Oss. wlän ‘wave’; Arm. cf. alik, gen. aleaç, abl. aleawk, id.; Gk. cf. alés, halés, adj. ‘surg- ing’; but Gk. hális, adv. (“in a mass’ equally fr. a type *uluit-, see uluió and extns.); Alb. valë, pl. id., f. ‘wave’; OE wll m. ‘fountain’; OCS vlüna, Cz. vina, f. (2) ‘wave’; Li. vilnis, i&s, f. id.; Latv. vilnis, id.
(ulnio (1) see uluið; (2) see ulaið) (1) only in Skt. ürnómi, v. ‘envelop’; (2) only in Gmc. cf. Go. wulan and OE wylian 'seethe? beside wyllan, v. id. (fr. *ulnio)
ulquátis, os *tearer, devourer, killer’. Cf. ul- quos (1) Skt. vrkátih, m. ‘robber, murderer’; Slovene volkác ‘Alsatian dog’; Li. vilkátas, m. *wer- wolf; Late vilkatis, vilkacs, id.
ulquio ‘she-wolf’. Cf. ulquos (1) Skt. vrkih, id.; OE welt id. MHG (Upper Ger) wülpe, id.; ON ylgr, ds: ylgi, id.; Li. vilke, id.
ulquó, ið (ambiguous consonantism, unless related to type ulquos, etc. see next). Skt. varke, mp. ((seize', but cf. type *uelk-) beside vrkah (2) '(plough'; Srb. vučem, v. ‘drag’; cf. OCS (hapax) vlüci, s. (Ccaltrop? or sim.); Li. vilkiu, eti, v. ‘wear — a garment’; cf. vilktas, m. (tech. *priming); L--- grep 163x page markers ---
23:11. 1987. 1573-1684 (uolobhis-uupsios + Supplement + Corrigenda)
44:In his Grammatica linguae Anglicanae, dated 1651, Dr. Wallis correctly equated 37 English words with their Latin and Greek cognates. These were reproduced by Dr. Samuel Johnson in the fifth edition of his Dictionary of the English Language (1773) with a comment as follows, translated from Wallis's Latin:
12384:Skt. at, adv. ‘then’; cj. also: OCz. & Cz. at 1655
19333:Cf. tump-. WP II, 618. (Gk. equated with Czech by Komensky in 1648). Cf. tupos Arm. (Gem, v. (*beat, fr. *tups- or fr. *dups-. Ambig.); Gk. tüpto, v. id.; Alb. typ, v. id.; OCS tüpajo, -ati, v. id. (and 'palpitate); Cz. tepu, tepati, v. tr. ‘tap, bang”; tepot, m. *beat- ing, banging’; R tópat, inf. ‘stamp, tramp’; Blg. cf. táptja, v. (stamp; knead': OCS tù- püsto, tüpütati, v. stamp"); Slovene cf. tépsti, inf. “beat, thrash’; It. cf. táppete, m. ‘scuffle’: Cz. tepot)
```


## [2026-09-06T21:49:26.391Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n 'SUPPLEMENT\\|Supplement' IEC.txt | head -20\necho \"---\"; sed -n '12370,12395p' IEC.txt | cut -c1-300"
}
```


### [2026-09-06T21:49:26.453Z] TOOL RESULT

```
23:11. 1987. 1573-1684 (uolobhis-uupsios + Supplement + Corrigenda)
127:VAN Wu. N.: Etymologisch Wb. der nederlandse Taal, 1912. With Supplement by C. B. van Haeringen, 1936. Reprint Staatsdrukkerij- en Uitgeverijbedrijf, den Haag 1949
---
Initial vowel ambig. Alb. ah, m. “beech'; OHG ask, OE zsc, m., ON askur, m. ‘ash’. Gk. oxüe, f. ‘beech’ re- presents a variant, and equates w. Alb. ashe (holly, fr. *oksio)
(0smà, variant of type odmā, q.v. See od- (3))
Gk. osmé, f. *smell'; Latv. osma, f. id. (but Latv. d > s before -m-, cf. the derivative drausma ‘threat’, fr. draudu, ét ‘threaten’. The sigmatic element is implied in Gk. ár-ōma, n. ‘scent’, lit. ‘good smell’, cf. ar-, and in br- 6mos, m. ‘stench’, lit. “heavy smell’, c
(Osn-, see ósis 'ashtree")
(Osnà, is, io, formative element of several plant-names in Gk. but of uncertain back- ground)
osth- (osthn-, o'st-) ‘bone’. WP I, 185. Cf. ostrk-, osku Skt. ásthi, asthán, n., Av. astis, pl. asta, m. id. beside ascus, m. ‘shin’; Oss. (dim. type) ástág, stág, id.; Hitt. hastai (for "hast id.; Gk. ostéon, n. “bone, kernel, rib”; ostón, n. “shell, jar; Alb. asht, pl: eshtna
osthrk-, ostrk- (ostrk-) 'ossified substance, bone, potsherd, pot, tile, ceramic, brick, crust. Cf. osth- “above, and ostrk-
Skt. istakà, f. ‘brick’; cf. also an-ásthakab, adj. ‘boneless’; Av. istya gs: istyehe, s. ‘brick’; Ober, isti-, id.; Pahl. xastak, Per. xišt, id.; Gk. óstrakon, n. ‘tile beside ostakós, Doric: asta-
895
kós, m. ‘crab’; W cf. as-gwrn, pl. es-gyrn, m. ‘bone’; Cor. as-corn, id.; Arm. cf. oskr & oskor, gs: OSker, ab. s. oskerb, s. ‘bone’. A similar formation occurs in Cz. kostrč, gs: kostrce (sic), m. ‘coccyx in relation to kost, f. ‘bone’
(osus, see osus ‘good’, in view of Gk. áotos "best fr. *osu- & (Gk.) -atos)
(otolos, see atolos)
-őt (-ot) (1) ablative singular inflexion Vedic cf. sanát *from early times'; Per. fardà ‘tomorrow’; Arm. aftu, s. ‘morning’; ajnu ‘thus’; Gk. amós, hamõs somehow’, fr. *sm- Ot) beside pos, Kos ‘somehow’; hos 'as'; tos "thus, cf. also Delphic woíkó ‘from the house”; Li. 
ot, oti (2)
Skt. at, adv. ‘then’; cj. also: OCz. & Cz. at 1655
(oudh- (1), see audh- “joint, part, limb, mem- ber”)
oudh- (audh-?) (2) ‘weave’
OE cf. eaden, pp. ‘fated’, ON auðinn, adj. ‘determined’; OLi. audmi, mod. audZiu, inf: austi, v. ‘weave’; audai, mpl. ‘warp’ beside (Lalis) üdis, m. gs: üdZio “day's weaving; Latv. auZu, aust, v. as Li.; audi, mpl. ‘textile, texture”
oudh- (3) ‘shoe’. Cf. oudh- (2) (?)
Gk. (Phrygian) oudon, gs: -ónos, m. “felt shoe; Arm. awd, Let ‘shoe’; cf. Lat. odo, üdo, m. (/shoe'. LW via Gk.)
(ouk-, o-gde formula to euk-, ük-, q.v. in OCS učọ, učiti, v. ‘train’, na-uka, f.; Li. áukle, Latv. aukle, f. ‘nurse’; Li. aukleja, f. ‘training’. Z-gde in Skt. ucyàmi "am accustomed")
ouk- (2) “offering, sacrifice’.
Umb. cf. ukar, gs: ukri ‘temple’ (vocalism cf. turuf ‘bulls: Lat. tauros and tuto 'city': Li. tautas); Lat. cf. sub-ücula, f. ‘sacrificial cake of wheat, oil and honey; Li. aukà, f. “victim, sacrifice”
(oukst-, possible alternative to aukst-, q.v.)
ouros, om (əur-) ‘water, brine; moisture, mire'. Cf. ieuros, eul-
Skt. (ambig.) olah, adj. *wet'; Gk. oüron, n. ‘urine’ beside án-auros, adj. ‘waterless’; aüra, f. *water-nymph'; Lat. cf. ürina, f. ‘water,
```


## [2026-09-06T21:49:43.901Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n 'kumolos\\|krās- (krast' IEC.txt | head\necho \"=== last leaf number and page markers near end ===\"\nawk 'BEGIN{RS=\"\\f\"} {n=NR} END{print n}' IEC.txt\ngrep -c 'Supt' IEC.txt\ngrep -n 'Supt: K' IEC.txt | head -5"
}
```


### [2026-09-06T21:49:46.094Z] TOOL RESULT

```
7808:krop ‘torture’; R kropát, v. ‘botch, mangle? kraps- ‘grab, snatch; rapacious; grab, sei- zure’ Br. krafa ‘seize, snatch; scratch, engrave’; kraf ‘seizure’; kraf, m. ‘stylus’: kraf, krav ‘stitch’; W craff ‘quick, keen; secure’; m. pl. -au ‘clasp, cramp’; craffu, v. ‘secure, grip’; Cor. crafa, v. ‘grip’; crāf, adj. ‘tenacious’; s. pl. crafow "basting-stitch"; cf. crefny, adj. ‘grasping, gree- dy’; OE hrespan ‘strip, despoil’; hresp ‘spolia- tion’ krās- (?) ‘glory, praise’ ON hrósa, v. ‘praise’; hrósan, f. ‘praise; boast- ing’; hræsni, f. id.; mod. Icel. hrós, n. ‘praise’; OCS krasa ‘beauty’ (and com. Sl.); Latv. cf. krāšns 'splendid'. See Supt. K : krās- (krast-, see karst-). Variant in W cras ‘toasted, parched, arid’; Br. kraz, id. krateið ‘overpower’. See kratos Gk. kratéo ‘rule’; OCS krostọ, krotiti (tame' and com. Sl.) kratos, is, us “strong; strength, power, force’. WP I, 354 Skt. krátuh “power, will, ability’; Av xratus ‘wisdom’; Ober xraQu-, id.; Gk. kratüs *power- ful”; krátos, n. ‘power’; W crad, craid, m. (“vig- our, force’, fr. *kratos, *kratis); OHG hrad ‘swift; OE hrad “swift, active; ON hraór, id.; OCS cf. krotükü ('tame', lit. overpower- ed"). Isophonic: Li. kratüs (rough, uneven’ krátos, à, is 'enclosure, envelope” W crawd “coating, surface’; OE hréóa 'goat- skin cover, mantle’; cf. hroó-girela ‘crown’; Li. krótai, krótos, mfpl. "lattice, grille’; Latv. krats ‘cage, prison’. (W and OE ambig.) kratsos, ios (?) Lat. crassus ‘fat, gross’; ON hress “hale, hear- ty’; hressa, Lat v. ‘cheer’ (kraug-, variant of krauk-, q. v.). (WP I, 417, 477 & II, 573) Hes. kraugós ‘woodpecker’; Gk. kraugé ‘croak, caw’ krauk- ‘caw, croak; crow, raven’. (Variant: krauk-) EMAIb. krak, mod. krrak ‘a bird of crow type’; OE hrēa (Crumble in the bowels’? Cf. hream ‘uproar’, fr. *kraukmo-?); Pol. Ukr. kruk ‘raven’; Latv. kraukjs ‘rook’ beside krauklis
8368:küm- (?). Cf. kumb-, kumolos Alb. kum, v. ‘cram’; kümem ‘swell’; i kümur, adj. ‘chubby’; Ir. cf. cüm “body, shape’; cum-
8386:(kumolos (1) and (2), see Supt: K)
=== last leaf number and page markers near end ===
858
228
6670:(kalbhā, see Supt: K)
6939:(kel- (1) ‘swift, see Supt: K)
6940:(kel- (2) “high”, see Supt: K and kelo (1))
7209:kin- ‘start, move, do, perform’. WP I, 362 & 510 and cf. Supt: K Skt. &inomi ‘put, arrange, pile, build’; Hitt. kina(mi) (queried: 'stir, move, begin"); Gk. kinéo, id.; Lat. -cinor, -cinari (do act in cpds. ratio-^, latro-^, patro-?^, leno-?. Cf. -ci- nium, s. form); OCS po-Cíng, inf. -Ceti ‘begin’; R po-éat, inf. “begin; tap a cask’; OCz. ve-, za-Cnu, -Cieti ‘begin’ beside OCS (and com. Sl.) Cinü ‘act’; cf. also Gk. apó-kinos “escape; a comic dance’; Latv. cina ‘struggle, fight
7250:klad- (1), see Supt: K
```


## [2026-09-06T21:49:53.767Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad\ncurl -s --max-time 60 \"https://ia-fts.archive.org/api/v1/search/hits_inside?item=mann-an-indo-european-comparative-dictionary-1984-1987&q=kn%C4%8Dirn&scope=all&size=10\" | head -c 3000\necho; echo \"=== try 2 hunch corner ===\"\ncurl -s --max-time 60 \"https://ia-fts.archive.org/api/v1/search/hits_inside?item=mann-an-indo-european-comparative-dictionary-1984-1987&q=%22kungios%22&scope=all&size=10\" | head -c 3000"
}
```


### [2026-09-06T21:49:55.773Z] TOOL RESULT

```
=== try 2 hunch corner ===
```


## [2026-09-06T21:49:58.506Z] TOOL CALL #15: Bash

```json
{
 "command": "curl -s -o /dev/null -w \"%{http_code}\\n\" --max-time 30 \"https://archive.org/metadata/mann-an-indo-european-comparative-dictionary-1984-1987\" ; echo \"---\"; curl -s --max-time 30 \"https://archive.org/metadata/mann-an-indo-european-comparative-dictionary-1984-1987\" | head -c 800"
}
```


### [2026-09-06T21:50:01.933Z] TOOL RESULT

```
200
---
{"alternate_locations":{"servers":[{"server":"dn710105.ca.archive.org","dir":"/0/items/mann-an-indo-european-comparative-dictionary-1984-1987"},{"server":"dn760003.eu.archive.org","dir":"/0/items/mann-an-indo-european-comparative-dictionary-1984-1987"}],"workable":[{"server":"dn710105.ca.archive.org","dir":"/0/items/mann-an-indo-european-comparative-dictionary-1984-1987"},{"server":"dn760003.eu.archive.org","dir":"/0/items/mann-an-indo-european-comparative-dictionary-1984-1987"}]},"created":1788731401,"d1":"ia902900.us.archive.org","d2":"ia802900.us.archive.org","dir":"/17/items/mann-an-indo-european-comparative-dictionary-1984-1987","files":[{"name":"Mann - An Indo-European Comparative Dictionary (1984-1987).epub","source":"derivative","original":"Mann - An Indo-European Comparative Dicti
```


## [2026-09-06T21:50:04.418Z] TOOL CALL #16: Bash

```json
{
 "command": "curl -s --max-time 30 \"https://archive.org/metadata/mann-an-indo-european-comparative-dictionary-1984-1987\" | python3 -c \"\nimport json,sys\nd=json.load(sys.stdin)\nfor f in d['files']: print(f['name'], f.get('size'))\n\""
}
```


### [2026-09-06T21:50:06.426Z] TOOL RESULT

```
Mann - An Indo-European Comparative Dictionary (1984-1987).epub 2121286
Mann - An Indo-European Comparative Dictionary (1984-1987).pdf 75622175
Mann - An Indo-European Comparative Dictionary (1984-1987)_chocr.html.gz 51141410
Mann - An Indo-European Comparative Dictionary (1984-1987)_djvu.txt 3698758
Mann - An Indo-European Comparative Dictionary (1984-1987)_djvu.xml 45262215
Mann - An Indo-European Comparative Dictionary (1984-1987)_hocr.html 93307559
Mann - An Indo-European Comparative Dictionary (1984-1987)_hocr_pageindex.json.gz 10999
Mann - An Indo-European Comparative Dictionary (1984-1987)_hocr_searchtext.txt.gz 1486201
Mann - An Indo-European Comparative Dictionary (1984-1987)_jp2.zip 1165905241
Mann - An Indo-European Comparative Dictionary (1984-1987)_page_numbers.json 171319
Mann - An Indo-European Comparative Dictionary (1984-1987)_scandata.xml 275575
__ia_thumb.jpg 6096
mann-an-indo-european-comparative-dictionary-1984-1987_archive.torrent 31962
mann-an-indo-european-comparative-dictionary-1984-1987_files.xml None
mann-an-indo-european-comparative-dictionary-1984-1987_meta.sqlite 20480
mann-an-indo-european-comparative-dictionary-1984-1987_meta.xml 1446
```


## [2026-09-06T21:50:12.297Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad\ncurl -sL --max-time 300 -o IEC_full_djvu.txt \"https://archive.org/download/mann-an-indo-european-comparative-dictionary-1984-1987/Mann%20-%20An%20Indo-European%20Comparative%20Dictionary%20%281984-1987%29_djvu.txt\"\nls -la IEC_full_djvu.txt; wc -l IEC_full_djvu.txt\ngrep -n 'kn[čcs]irn\\|kungios\\|kunkios' IEC_full_djvu.txt | head -20"
}
```


### [2026-09-06T21:50:15.758Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 3698758 Sep  6 17:50 IEC_full_djvu.txt
121635 IEC_full_djvu.txt
43180:kungios, io (kungos, à) (1) ‘bulge, hump, 
43189:kungios (kung-) (2) (?) ‘corner’. Cf. kungios 
43197:kungios (1), kunkos, konkolos 
117849:Skt. konah “corner, angle'. Cf. kungios (2) and 
117855:Per. kun£ “corner”? is ambig. Cf. kungios (2))
```


## [2026-09-06T21:50:18.103Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad\nsed -n '117820,117880p' IEC_full_djvu.txt"
}
```


### [2026-09-06T21:50:18.156Z] TOOL RESULT

```
(kuKolos (?) beside kiKalos? in Oss. Gisil 
little? and Latv. kusls ‘puny’. Isophonic in 
Skt. kúsalah ‘fitting, skilled? and in Av. kusro 
‘corner’) 

(kuKs-, kusK- in G huschen ‘whisk, dash; 
jolt’; Husch, m. id.; Du. hossen ‘jolt’ and Latv. 
kustu, inf. kustēt ‘stir, move’) 

(kuls- ‘cover, protection? ? in Hitt, gulsas for 
*kulsas ‘potective deity’ & OHG, Du. hulsa, 
huls, f. ‘pod, shell’, but cf. Kls- for Gmc. 


1635 


forms) 

(kumbó in Lat. -cumbo, Gre, cpds. “lie? and 
Norw. humpe, v. (limp) 

(kumolos, is ? “tip, peak” in Lat. cumulus 
‘pile’; Ir. comhal ‘hood’, W cwfl, id. and R 
komeP *butt-end'. Isophones: OHG humbal, 
m. ‘drone’, Sw. humla *bumble-bee". Cf. WP I, 
389 for this word) 

(kunios, keunios in Lat. cuneus *wedge' and 
Skt. konah “corner, angle'. Cf. kungios (2) and 
WP I, 33 & 465 and keunios as an entry 
in main index) 

(kunki-, kunkir- in Skt. kufice, mp. “bend”, 
Arm. knčifn ‘knot, twist" and Cz. kucera eur, 
Per. kun£ “corner”? is ambig. Cf. kungios (2)) 

(küprio- in Hes. küpros ‘henna’, küprion 
‘plantain’ and R kipréj *willowherb') 

(kurs- in Lat. curr-üca ‘warbler’ or sim. 
and Ir. corr ‘bittern’ also *crane") 

(kursó in Lat. curro, Gre "ron" and MHG 
hurren “rush? beside OHG hursken ‘spur on’. 
See Kurs- (2)) 

N.B. Ambiguity as between IE*k and *k 


on the one hand, and *k and *qu on the- 


other sets up a degree of uncertainty in some 
of the above forms. The only IE language 
that distinguishes all three phonemes is Ar- 
menian (k, s and K). 

(Kàd-, Kådəst-, KadsK- in Ir. cáidh ‘chaste, 
pure’, cádhas, f. ‘veneration’ & Fris. hoask, 
Du. heusch ‘friendiy’)
```


## [2026-09-06T21:50:29.146Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN galingale ===\"; grep -n -i 'galingale\\|galanga\\|galingal' KLN_1966.txt KLN_1971.txt | head -20\necho; echo \"=== KLN hunch ===\"; grep -n -i \"^hunch\\|hunch, \" KLN_1966.txt KLN_1971.txt | head -20"
}
```


### [2026-09-06T21:50:29.221Z] TOOL RESULT

```
=== KLN galingale ===
KLN_1971.txt:99350:galangale, n. — See galingale. 
KLN_1971.txt:99470:galingale, n., an aromatic root of the ginger 
KLN_1971.txt:99471:family. — OF. galingal , formed — through the 
KLN_1971.txt:99472:medium of MGk. yaXayya and ML. galanga — 
KLN_1966.txt:15677:Galago,  n.,  a  genus  of  African  lemurs  (zool.)  — ModL.,  from  native  African  name, galangale,  n.  —  See  galingale.
KLN_1966.txt:15697:Galilee,  name  of  the  northern  province  of  wes¬ tern  Palestine.  —  L.  Galilaea,  fr.  Gk.  raXiXata, fr.  Heb.  Haggdlil,  lit.  ‘the  district’,  shortened  fr. Gflil  haggoyim,  ‘the  District  of  nations’  (Is. 8:23).  Haggdlil  was  the  name  of  a  district  in  the hill  country  of  Naphtali  (see  Josh.  20:7  and 21:32).  and  it  was  only  at  a  relatively  later  period that  it  began  to  denote  the  territory  of  Palestine north  of  the  Emek  Jezreel  (Esdraelon).  For  the etymology  of  Heb.  galil,  ‘district’,  see  gelilah. galimatias,  n.,  jargon.  —  F.,  ‘nonsense,  gibberish  , prob.  a  deformation  of  Late  L.  balhmathia,  in¬ decent  songs'.  For  the  etymology  of  this  latter word  see  Du  Cange,  Glossarium  mediae  et  in- fimae  latinitatis,  s.v.  balare. galingale,  n.,  an  aromatic  root  of  the  ginger family.  —  OF.  galingal,  formed— through  the medium  of  MGk.  yaXxyyoc  and  ML.  galanga fr.  Arab,  khalanjdn,  fr.  Pers.,  ult.  fr.  Chin.  Ko- leung-keung,  lit.  ‘mild  ginger  from  the  region of  Kao’.

=== KLN hunch ===
KLN_1971.txt:35268:cp. clump and clunch, hump and hunch, lump 
KLN_1971.txt:49372:and bunch, hump and hunch, lump and lunch. 
KLN_1971.txt:116847:hunch, n., 1 ) hump; 2 ) a thick piece. — Prob. al- 
KLN_1971.txt:116853:Derivative: hunch, tr. v. 
KLN_1971.txt:141314:For a similar alteration cp. hunch, which prob. 
KLN_1966.txt:5857:bunch,  n.  —  Prob.  fr.  bump,  in  the  sense  of  ‘swel¬ ling’.  For  the  connection  of  bump  with  bunch cp.  clump  and  clunch,  hump  and  hunch,  lump and  lunch.
KLN_1966.txt:7991:Derivatives:  clumsi-ly,  adv.,  clumsi-ness,  n. clunch,  n.,  a  kind  of  limestone.  —  Cp.  Du.  Mont, klomp,  of  s.m.,  ‘lump’,  and  see  clump.  For  the connection  between  dump  and  clunch  cp.  bump and  bunch,  hump  and  hunch,  lump  and  lunch. clung,  past  tense  and  pp.  of  ding.  —  ME.  pp. clunge(n),  fr.  OE.  clungen,  fr.  clingan,  ‘to  shrivel, contract’.  See  cling.
KLN_1966.txt:17301:haunch,  n.,  hip.  —  Earlier  hunch,  fr.  ME.  hanche, haunche,  fr.  OF.  (=  F.)  hanche,  fr.  Teut. *hanka;  cp.  MDu.  hanke,  ‘haunch’.
KLN_1966.txt:18247:hunch,  n.,  1)  hump;  2)  a  thick  piece.  —  Prob.  al¬ tered  fr.  hump.  For  a  similar  alteration  cp.  lunch, which  prob.  derives  fr.  lump.  Cp.  hunk. Derivative:  hunch,  tr.  v.
KLN_1966.txt:22316:lunation,  n.,  time  between  two  successive  new moons.  —  ML.  lunatio,  fr.  L.  luna,  ‘moon’.  See lune  and  -ation  and  cp.  lunate, lunch,  n.  —  Prob.  altered  fr.  lump,  ‘piece’  (the original  meaning  of  lunch  was  ‘piece,  lump  ). For  a  similar  alteration  cp.  hunch,  which  prob. derives  fr.  hump.
```


## [2026-09-06T21:50:37.160Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport io\nfor fn,targets in [('KLN_1966.txt',['galingale,  n.,  an  aromatic','hunch,  n.,  1)  hump'])]:\n    data=open(fn,encoding='utf-8',errors='replace').read()\n    leaves=data.split('\\f')\n    for i,l in enumerate(leaves):\n        for t in targets:\n            if t in l:\n                print(fn,t[:20],'leaf',i)\nEOF"
}
```


### [2026-09-06T21:50:39.189Z] TOOL RESULT

```
KLN_1966.txt galingale,  n.,  an  leaf 344
KLN_1966.txt hunch,  n.,  1)  hum leaf 404
```


## [2026-09-06T21:50:46.511Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA\ngrep -n -i 'alan[ğgǧj]\\|ḫalang\\|xalang\\|halang\\|hulang' PLA_asbaghi_1988_ia_djvu.txt | head -20"
}
```


### [2026-09-06T21:50:46.570Z] TOOL RESULT

```
4309:>ow>do palangmosk, parankmosk 12 Byr. yaug? + 
8734:zus - balang: Pl. v-zaäs balang Ss. balanf 12, 
8766:afrz. galanga, sp., pg., ait. galanga, sp. garengal, frz. garengal, 
8767:ahd. galangan 2 . 
14609:mzuhb - talangabin = tarangabin q. v. 6, 
15268:sof>Do Palangmusk ®, syr. J„-oog,% (pers. Alaıs ) 9 
15416:Arab _ falangamisk = faranfamiäk q. v. 5 
15466:uw - fank: "Wiesel; Biber" pers. ”, wahrscheinlich aus pers. —ıL palang
```


## [2026-09-06T21:50:48.383Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA\nsed -n '8740,8790p' PLA_asbaghi_1988_ia_djvu.txt"
}
```


### [2026-09-06T21:50:48.434Z] TOOL RESULT

```
9. Addai Scher s. v., albasa s. v. 
4. FM. Ss. v. 

5. Muhit s. v. 

6. Fremdwörterbuch s. v. 
7. FM. s. v., albasa s. v. 
8. BQ. s. v. 

9. Muhit s. v. 

10. Addai Scher s. v. 

11. Muhit s. v. 

12. Muhit s. v. 


balanı 112 banädiris 


ee - halanf: "ein Baum, aus dessen Holz Gefäße gemacht werden" pers. 1, 


Olails - halanfan: "Alpinia (maranta)" pers. cu. hulanfän, aind. kulafig, 
afrz. galanga, sp., pg., ait. galanga, sp. garengal, frz. garengal, 
ahd. galangan 2 . 


.ır 2 4 - 
Groule - bulangabin: "Essig u. Honig" aus dem ar. pbul + pers. „by angabin 
vgl. sikanfabin 


Jr - hambarfi: "Granatwerfer". 


2 - bumbara: "Bombe" aus dem pers. o,L,> hompäre ® — mp. \xr xumb + 
s-» pärag. 


#23 - bumbaridi = humbardi s. humbardi. 


2 
auf - humbfa: "großer Krug für Wein od. Korn" aus dem pers. 6 bumbag a 
mp. Ip xumb 5, 


ae - bambiq: "Keller aus Holz mit gewölbtem Dach" aus dem pers. £ ham
```


## [2026-09-06T21:50:58.974Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor f in MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt; do echo \"=== $f ===\"; grep -n 'خلنج\\|خلنگ\\|خولنجان' \"$f\" | head -10; done"
}
```


### [2026-09-06T21:51:00.883Z] TOOL RESULT

```
=== MON_part1.txt ===
6391:که با آن رنگ دیگر باشد. چپار» خلنگث» 
6392:خلنج» بیس ای را او 
10436:لا.] (.) (گیا.) درختجه‌ای از تيرة خلنگ‌ها 
34627:شدن, ابلق گشتن» خلنگ گردیدن. به 
57245:۹ توصداه [ - خلنج] (ص.) دو رنگ» 
57248:خلنگ؛ 8۵ (.) (گیا.) گیاهی است از 
57249:تیةٌ خلنگ‌ها که بصورت درختچه با علفی 
57252:می‌روید؛ علف جاروب؛ خلنج. خلنگ‌ها: 
57267:خلنگ: ۱۵۵8۵ - خلنج ] (ا.) گرفتن اعضا و 
=== MON_part2.txt ===
=== incoming/MON/MON_2vol_Adena_v1_djvu.txt ===
6391:که با آن رنگ دیگر باشد. چپار» خلنگث» 
6392:خلنج» بیس ای را او 
10436:لا.] (.) (گیا.) درختجه‌ای از تيرة خلنگ‌ها 
34627:شدن, ابلق گشتن» خلنگ گردیدن. به 
57245:۹ توصداه [ - خلنج] (ص.) دو رنگ» 
57248:خلنگ؛ 8۵ (.) (گیا.) گیاهی است از 
57249:تیةٌ خلنگ‌ها که بصورت درختچه با علفی 
57252:می‌روید؛ علف جاروب؛ خلنج. خلنگ‌ها: 
57267:خلنگ: ۱۵۵8۵ - خلنج ] (ا.) گرفتن اعضا و 
=== incoming/MON/MON_2vol_Adena_v2_djvu.txt ===
```


## [2026-09-06T21:51:02.510Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '57235,57275p' MON_part1.txt"
}
```


### [2026-09-06T21:51:02.564Z] TOOL RESULT

```
تبر 5 چسننده. 


: : ۲6۱۱ (.) حشم» غضب. 

و ین : 20121 -۲۵۱ [ع. . ف. -خل 
(ع.) + انجیین (معر. . انگیین)] (امر.) شربتی 
نی با شکر و قند سازند؛ 


۹ توصداه [ - خلنج] (ص.) دو رنگ» 
ای شاه و مد 

خلنگ؛ 8۵ (.) (گیا.) گیاهی است از 
تیةٌ خلنگ‌ها که بصورت درختچه با علفی 
است و قرب ۰ گونه از آن شناخته شده 
و اکثر در آفريقا و نواحی گرم و معتدل 
می‌روید؛ علف جاروب؛ خلنج. خلنگ‌ها: 


(گیا.) تیرةٌ بزرگی از گیاهان دو له‌ای پیوسته 
جام که اکثر شامل گُیاهانی است بصورت 
درختچه يا درخت و گاه هم علفی هستند و 
اغلب مختص نواحی گرم‌اند. برگ‌های 
انواع مختلف این تبره غالبا ساده و بدون 
گوشوارکك و گل‌هایش نر و ماده و دارای 
قطعات ۴ با ۵ تابی است. کاسة گل در 
بعضی گونه‌ها به رنگ جام و در برخی نیز 
کاسبرگ‌ها جدا از هم هستند میوهٌ این 
گیاهان حقه یا شفت است و برخی از انواع 
ان سمی است. 

خلنگ: ۱۵۵8۵ - خلنج ] (ا.) گرفتن اعضا و 
کندن به ناخن. 

خلو: ۷ [ع.] (ص.) تهی» خالی. ببزار. 
خلو: (۷) 010۷ [ع.] (مص‌ل.) خالی شدن» 
تهی گشتن. تنها بودن. (امص.) تنهایی. 
خلوت: اما [ع. خلوءة] (مصل.) تنهابی 
گزیدن» تنها نشستن. (امص.) تنهایی» انزوا. 
(تص.) مجموعه‌ای است از مخالفات نفس و
```


## [2026-09-06T21:51:22.668Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v2 خلنج ===\"; grep -n 'خلنج\\|خلنگ\\|خولنجان' BQT_v2_pages.txt BQT_v1_pages.txt 2>/dev/null | head -20\necho \"=== HRN/HUB ===\"; grep -n -i 'chalang\\|halang\\|ḫalang\\|galangal' HRN.txt HUB.txt | head -20\necho \"=== RCH ===\"; grep -n -i 'khalanj\\|khulanjan\\|galangal' RCH.txt | head -10\necho \"=== LKT galgant ===\"; grep -n -i 'galgant\\|galanga' LKT.txt | head -20"
}
```


### [2026-09-06T21:51:22.763Z] TOOL RESULT

```
=== BQT v2 خلنج ===
BQT_v2_pages.txt:1531: ‫خرودارو نوشته شده است که خولنجان باشد‬                  ‫کوبند و آنرا بعربی شمورالسقالبه با صاد وبای‬
BQT_v2_pages.txt:3755:  ‫» وار وی کمان وتر خدنگو چوب‌خلنج بار افند ‪« ».‬حدود‬                 ‫وجنگ فگر وتوانگر وسار تعمت‬
BQT_v2_pages.txt:9433:       ‫نقیض پخته باشد ‪ - ۷‬و خامه را‬                          ‫خولنجان باشد » و آن رستنیی است دوابیکه‬
BQT_v2_pages.txt:9852:      ‫رك ‪ :‬خولنجان‬              ‫‪۴‬‬    ‫ودر آ نجمن‌آرا همین بیت برای (خاور؟ بمعتی مورچه شاهد آمده است ‪.‬‬
BQT_v2_pages.txt:12153:                    ‫اول وسکون انی ک‬                            ‫کهآ نرا خولنجان کویند» وبسنی گفته‌اند درختی‬
BQT_v2_pages.txt:13215:                                      ‫شبیه بشفتالو ‪.‬‬     ‫خلنج ‪ » ۴‬بنتح اول و انی و سکون‬
BQT_v2_pages.txt:13235:                                ‫وچ‬      ‫آمده استھ ‏‬      ‫خلنگ ‪ ۴‬بنتماول بروزن پلنگه‪,‬‬
BQT_v2_pages.txt:13236:                                                          ‫بمعنی خلنج است که دورنگه وابلق باشد ® ‪-‬‬
BQT_v2_pages.txt:13250:  ‫اسم فاعل‬           ‫‪۴‬‬           ‫خلنگه (ه‪.‬م‪).‬‬      ‫‪۳‬‬           ‫‪ ۱‬کے رك‪ :‬خلم > خل » خله ‪.‬‬
BQT_v2_pages.txt:13251:                                                        ‫‪ = ۴‬خلنج («‪.‬م‪).‬‬        ‫از خلیدن («‪.).‬‬
BQT_v2_pages.txt:13253:             ‫خلنگه ‪.‬‬          ‫ااز رونگکهردد‬       ‫ن‬
=== HRN/HUB ===
=== RCH ===
35313:p^jU-  khdivttshy  A   cucumber  kept  for  seed, p   JjU-  khdzcnly  Rust. p^l^\J«bk  khUiCuUnjdny  Galangale.
36370:khusraic^ddruy  Galangale.
37129:p   khalanj  also  khilanj^  Of  two  colours.  Piebald.  KhU lar{j^  A   black  pigeon  with  mottled  wings.  KhUii\j^  Torpor  of the  limbs.  A   scratching  with  the  nails.
37130:A   khalanj  (or  p   khulanj),  A   tree  from  which  they  make beams,  or  wooden  bowls.  A   wooden  platter.
37131:A   khalanj dn^  The  root  galangale.
37664:P   kh'dlinjan,  Galangale.
37987:^   khnlattjuny  The  herb  galangale.
44928:SY  rimas^ty  Galangale.  (Burhdn^i  kdtif^J)
47473:^   saped^idky  A   shrub  used  in  tanning,  galangale.
48280:**  zurty  A   heap  of  com.  Galangale.
=== LKT galgant ===
1926:'Eine  dem  Ingwer  verwandte  Pflanze, Galanga'  aus  Indien  und  China,  die  im MA  im  Orient  und  Okzident  als  Arznei- kraut benutzt  wurde;  hieraus  mgr.  yc- XcIyt«,  mlat.  galanga,  it.  galanga,  afrz. galange,  garingal,  frz.  le  galanga,  sp. pg.  galanga;  mengl.  galingale,  galger ['lebhaft  sein'],  engl,  galingale,  dtsch. Galgant{'w\xvzQ\);  russ.  bulg.  kalgan,  serb. galgan,  cech.  galgän,  poln.  galgan, 'galgant.  [Nach  Hirth  ChinFW  201/203 ist  ar.  halangän  auf  chin.  ko-Uung- kiung,  d.  h.  milder  Ingwer  von  Kao- tschau-fu,  einem  Regierungsbezirke,  aus dem  die  Galgantwurzel  besonders  be- zogen wird,  zurückzuführen.  In  der  Tat wird  der  Galgant  von  IBN  HURDADBA um  875  als  chinesisches  Erzeugnis  er- wähnt; er  muß  vor  dem  12.  Jahrhundert durch  Vermittlung  der  Araber  bis  nach
1929:Deutschland  gekommen  sein,  da  schon die  heilige  HILDEGARD  von  Bingen t  1179  eine  Abhandlung  über  ,die medizinischen  Vorzüge  des  Galgant " geschrieben  hat.]  [DE  271.  Eguilaz404. ML  1856.
4991:Galgant  795
5778:mhd.  1100 ö«/«  864 GaZan  864 ^ra/an«  864 Galanterie  864 Galgant  795 Galniei  1149 Gamaschen  633 Gambit  661 ganfen  j.  659
6518:gaban  971 gaharit  1030 gabeile  974 gäühe  1714 gaife  994 gaüan  741 lyaZa  864 galanga  795 galange  afz.  795 galant(erie)  864 galanthomme  864 gatnache>!  633 ganse  1056 garatnaches  dial.  633 garbin  674 garde-boeuf  11 garingal  afz.  795 garo(u)  1155 ^awp?  1002 <7a«e  702.  1147 gazelle  699 5rö2:p«<>  1059 gecko  701 gehene  afz.  705 gShenne  705 gene(r)  705 genetCte)  2192 genette  685 gengeli  744 gerbo(ise)  936 gJiazel  698 giaour  632 giberne  641 </«7c<  9.t1 GtV?«-«  951 gingembre  1930 ^tV«/"«'  2234 .9jVo/?*'  1085 giroflee  1085 gnacarS  1546 godemetim  afz.  633 golgotha  743 gomtne  gutte  712 pon^  558 gouape  1002 goudon  703 goudron  1128 gouge  728 goujat  728 $fOM?e  741 goum  747 goumhie  750 gourbi(l)  1252 gourgandine  677 Graa?  731 grubeau  673 grabeler  673 Gr^ai  731 gulbre  632
7076:I  galanga  765
7431:gabulum  974 gaitanum  644 galanga  795 ^«Z/a  (mucata)  647 ^««a  1059 gehenna  705 yelseviinum  942 genius  723 gerboa  936 5'?fcrt  641 gypsiim  716
8145:galanga  795
```


## [2026-09-06T21:51:34.776Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '1918,1932p' LKT.txt\necho \"=== PHD kund ===\"; grep -n -i \"kund\\b\\|kund \\|kundāg\\|gund\" PHD.txt PHD_mackenzie.txt | head -20\necho \"=== NYB kund ===\"; grep -n -i \"kund\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-06T21:51:34.844Z] TOOL RESULT

```
'Abort'  [Kelekian  Kämüs  547;  aus  ar. Jialü  'leer;  Einöde'];  hieraus  hnlg. hale, serb.  hala  'dass.'.     [Bern  SlEtWb  383.
792.  Ar.  Halab:
N.  pr.,  Stadt  im  nördlichen  Syrien: Aleppo,  dazu  das  Adj.  halabt  'aus  Aleppo, aleppinisch';  hieraus  die  Bezeichnung für  einen  'Seiden-  und  Wollstoff':  sp. alepl,  alepin,  frz.  aUpine,  dtsch,  Aleppin. [Devic  DEt  15.    Lammens  Rem  10.
793.  Hebr.  hälal:
'Preisen',  davon  pi'el  hillel,  imper  2. plr.  hallelü  'preiset!',  dazu  hebr.  jäh, die  übliche  Kurzform  für  den  Gottesnamen JahH'§  [Jehova],  also  hallelüjäh,  gr.  dWr)- Xoü'ia  'preiset  Gott!'.  In  viele  Sprachen übergegangen:  lat.  alleluia,  frz.  alleluia; dtsch.  Alleluja,  ndl.  halleluja,  engl. alleluia,  alleluiah,  halleluiah;  russ.  al- lihija,  poln.  aleluja  und  zahlreiche  dial. Ableitungen;  bulg.  aleluija  'Unsinn'  [zu dieser  pejorativen  Bedeutung  von  Wort- verbindungen der  christlichen  Liturgie vgl.  WuS  V,  127  Anm.  3].
794.  Ar.  haläl:
'Erlaubt',  ebenso  tk.  halal  'dass.,  er- laubter Gewinn,  Segen' ;  aus  der  tk.  Gruß- formel halal  olsun!  'möge  dir  Heil blühen!'  nahm  man  rum.  halal  'Heil, Segen',  besonders  in  der  Redensart: halal  sä-ft  fiel
795.  Ar.  halang^än:
'Eine  dem  Ingwer  verwandte  Pflanze, Galanga'  aus  Indien  und  China,  die  im MA  im  Orient  und  Okzident  als  Arznei- kraut benutzt  wurde;  hieraus  mgr.  yc- XcIyt«,  mlat.  galanga,  it.  galanga,  afrz. galange,  garingal,  frz.  le  galanga,  sp. pg.  galanga;  mengl.  galingale,  galger ['lebhaft  sein'],  engl,  galingale,  dtsch. Galgant{'w\xvzQ\);  russ.  bulg.  kalgan,  serb. galgan,  cech.  galgän,  poln.  galgan, 'galgant.  [Nach  Hirth  ChinFW  201/203 ist  ar.  halangän  auf  chin.  ko-Uung- kiung,  d.  h.  milder  Ingwer  von  Kao- tschau-fu,  einem  Regierungsbezirke,  aus dem  die  Galgantwurzel  besonders  be- zogen wird,  zurückzuführen.  In  der  Tat wird  der  Galgant  von  IBN  HURDADBA um  875  als  chinesisches  Erzeugnis  er- wähnt; er  muß  vor  dem  12.  Jahrhundert durch  Vermittlung  der  Araber  bis  nach
63
[Ar.  halfä'.
Deutschland  gekommen  sein,  da  schon die  heilige  HILDEGARD  von  Bingen t  1179  eine  Abhandlung  über  ,die medizinischen  Vorzüge  des  Galgant " geschrieben  hat.]  [DE  271.  Eguilaz404. ML  1856.
796.  Ar.  halfä':
Stipa  tenacissima  oder  arundo  epigeios, eine  Pflanze  aus  der  Familie  der  Gra- mineen [sp.  esparto  'Spartogras'],  aus der  man  Malten,  Hüte,  Schnüre,  Seile für  Ziehbrunnen,  Säcke  u.  ähnl.  macht; hieraus  mit  ar.  Art.  prov.  aufo,  frz.  (alt) auffS,  (neu)  alfa  'Spartgras',  auch  papier alfa\  prov.  aufiS  'Schlafmütze';  dtsch. Halfa^vas.  [Devic  DEt  47/48.  DE  100. ML  4002.
797.  Tk.  hali:
=== PHD kund ===
PHD.txt:384:ёгбһ [glwh | N guroh] group, crowd. gubrág [gwpl’k'] awake, alert, vigilant. ģubrās- [gwp/”s-] = wigras-, v. wigrádan. ģuftan, $0(w)- [YMRRWN-, YMLLWN-tn! < A ymlwn, V тЇ; gwptn', gwb- | M gwptn, gw-, N ~, gā(y)-] say, speak. ~išn: speech. ģuftār [gwpt?] | N ~] speaker. ~ih: (power of) speech. gugiin- [gwk’n- | M gwg^n-] destroy. gugar(i)dan, gugar- [gwk”/-(y)tn! | N guwár-idan] digest. tuģāy [gwk*dy | M gwg'y, N guwah] witness. ~ih: testimony. ģūh [gwh | N —] dung, excrement. guhrayénidan, guhrayén- [gw AP yn-ytn!] waken, arouse. gul [gwl | N ~] flower, rose. ботап [gwnmn! | = M, N ~] doubt. ~par [-A/] casting doubt. ~ig [-yk'] doubtful. ~ih, ~igih: doubt. gumardag [gwmltk'] appointee, deputy. ģumārdan, gumār- [gwm’l-tn' | М gwm'r-dn, N gumāštan, gumar-] appoint, commission, entrust. gumbad [gwmbt' | N ~] dome, fire-temple. £umég [gwmyk! | M gwmyg] mixture. guméxtan, gumēz- [gx”myhtn!, gwmyc- | M gwmyxtn, gwmyz-] mix. ~išn: mixing, mixture; = gumézagih. gumëzag [gwmyck'] mixture. ~th: the Mixture, (the duration of) this material world. Jgund [gwnd | = P] army, troop; group, gathering. *gund [gwnd | N ~] testicle. gung [g(w)ng | N ~] dumb. ģurbaģ [gwibk! | N ~a] cat. Бита [gwlt! | P gwrd, N ~] hero. lih: heroism, bravery. gurdag [gwltk! | N ~a] kidney. *gurdih [ewityh] (some piece of) armour. gurdwār [gwltw’!] befitting a hero. ёпгр [gwlg | N ~] wolf. gurganig [gw/g”nyk! | N ~i] of (the province) Gurgan. gursag [ewlsk] | N gurusna !] hungry. «ЛЬ: hunger. Suën [gvfn! | N ~] male. gusnag [gwšnk! | J gušna] hungry. Gušnasp [gwšn(*)sf] the second major Fire of Sasanian Eran, that of warriors. £yà$ [gyw'k! | M gy'g, N jay] place.
PHD.txt:430:kē(x)šīdan, kū(x)š- [kz(4)$-ytn! | M htos-ydn, N kēšīdan) strive, struggle, endeavour. ~iSn: strife, combat. ~iSnig : energetic. Кбу [kwd | N ~] street, lane. ki [AYK < A’yk | M kw, N kū, hi] where; that; than, ~ Буар [N лија] where. ~ tā: so that. kūč(ak) [Awe(k!) | N kūčak] small. kak [kwk'] small, short. kulāčag [kwľck' | N kulīča] small, round bun. kulāf [kwl”5 | N kuláh] cap, bonnet. ~ak [-k!] | N ~hak] little cap; calyx. kulang [Ring | N ~] crane. kullag [kwlk'] locust. kumig [Awmyk'] stomach. kun-, -išn, v. kardan, kunišn. кар [STE < A *st-h; kwn! | N ~] rump, buttocks, anus. kundāģ [knd^k! | M qnd’-, N kunda] magician, soothsayer. ~ih: magic, astrology. kundur [kwndl | N ~] frankincense. kunišn [kwnsn' | M kwnyšn] action, deed. ~gar LA | M -gr] doer, performer. kunjid [ŠM% < А пг; kwnc(y)t! | N ~] sesame. kün-marz [Rzonmlc] sodomite; sodomy. kurkum [kwlkwm] saffron. kurrag [kwlk' | N ~a] foal, colt. 1kust [Ruwst!] side, direction; district. kust [kwst' | Ar. qust] costus. kustag [kwstk! | M Rwstg] = !kust. ~bed [-pt'] district-commander. kustig [kwstyk! | N ~i] sacred girdle. kuštan, kuš- [NK SWN-tn! < А V nks; kwi-tn! | M kwšt, kws-, N ~] kill.
PHD.txt:839:army gund, hén, laskar, spāh.
PHD.txt:878:astrology axtar(a)marih, kundāgīh.
PHD.txt:2083:gathering  čīnišn, ` harróbiin(ih); (group) gund, hanjaman.
PHD.txt:2164:group dastag, groh, gund.
PHD.txt:2696:magic jādūgīh, kundāgīh.
PHD.txt:2697:magician jādūg, kēd, kundāg.
PHD.txt:3735:soothsayer kéd, kundāg, mur w-ni&.
PHD.txt:3960:testicle gund.
PHD.txt:4074:troop gund.
PHD.txt:5038:nay! kundāgīh kundāg nayestān! kandan kanīg kanīzag xwan-! xwandan! -gen
PHD_mackenzie.txt:2618:llgund [gwnd IN......,] testicle.
PHD_mackenzie.txt:5955:angel frestag; guardian ,...., frawahr,   army gund, hen, laskar, spiih.
PHD_mackenzie.txt:6675:   (group) gund, hanj'aman.                      character huxem; of ,...., religion
PHD_mackenzie.txt:6720:group dastag, groh, gund.                harmful pad-zyan, resken, zyangar,
PHD_mackenzie.txt:7780:testicle gund.                            thunder (n.) yarranag.
PHD_mackenzie.txt:7807:tongue uzwan, (zuwan).                   troop gund.
=== NYB kund ===
2195:kandak [knd’k] astrologer, pl. cas. obl. =«-ān 1319, - MPrs qnd?yy ‘magic, astrol- ogy’, List 84; NP kundā ‘sorcerer, astrologer, wise', cf Bailey, TPhS 1955, 72-74.
2237:ikartan [krtn'; klty; ‘BYDWN-t'] kun- [ BYDWN-;forms v. I, 179; pres. 3d p.sg. kwnd: read kund] to make, to do, to per- form, to exercise, to commit, to cause, to bring about; to manufacture, to construct (hac ‘of’ a material); — forms active deriva- tive vbs. a) from v.ns. in -išn, e.g. āsāyišn ^ to repose, azbäyisn ~ to invoke; gar- zišn, īzišn, koxšišn, nikērišn, pursišn, za- nisn ete.ete. ~ ; b) from other nouns: čfrin, amoxtareh, appar, hampursakeh, tak, varz ete. ete. —, v. the resp. ws.; — with a pred. adj., e.g. 73. 34" etc.; girt kart = girt kartak (g. v.); vat-kart v. vat; or a pred. subst., e.g. api-$ ... bitaxš kunom 2510-11; . with kart as its cognate obj. P2:6-7. 8 [read (TB =) nev kart" kunän that I may do good deeds]. — With prev.: andar 6 kar ~, v. kar; api-§ Mānušcihr andar 6 Patisz"argar kart he brought M. (as a captive) to P. 1164-5, cf Bd A p. 2315-5; — apüc ~ to repel 42*3 gl.; to reflect 1125; — pat ddr apar ~ to crucify a p. 208; — bé ~ to remove 65; — berön asmän kunst he wil turn them out of heaven 10318; — frāc ~ to send forth 161!5; to bring forth, to produce 48?9; to attempt 81?!. — NB: man kart HWH-wm 374-5 for man kart-om by me it was done, v.s. v. h- and -m. — *BYDWN.x,ot' = kunät 5314, cf BY- DWN-x,-yd = 2nd p.sg.kunēKnS VII, 11. — Av. (444 sqq.) tkar-, pres.ko ranu-; OP kar- kunav-; MPrth kyrdn kr-; MPrs kyrdn kwn-; Paz. NP kardan kun-; cf s.v. hangirtikeh.
4744:Markwart, Josef, Wehrot und Arang. Untersuchungen zur mythischen und geschicht- lichen Landeskunde von Ostiran. Hrsg. von Hans Heinrich Schaeder. Leiden 1938. [Also Marquart, J.] V. also Cat., Ēranšahr.
4858:WZKM = Wiener Zeitschrift far die Kunde des Morgenlandes.
7246:kuhan, kahun: kahvančh kunda: kandak
```


## [2026-09-06T21:51:48.715Z] TOOL CALL #27: Bash

```json
{
 "command": "sed -n '1,60p' tools/fetch_source.py"
}
```


### [2026-09-06T21:51:48.759Z] TOOL RESULT

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


## [2026-09-06T21:51:57.212Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wiktionary.org/wiki/galingale\" \\\n \"https://www.etymonline.com/word/galingale\" \\\n \"https://en.wiktionary.org/wiki/%DA%A9%D9%86%D8%AF\" \\\n \"https://en.wiktionary.org/wiki/%DA%A9%D9%86%D8%AC\" \\\n \"https://en.wiktionary.org/wiki/hunch\" \\\n \"https://www.etymonline.com/word/hunch\" \\\n \"https://en.wiktionary.org/wiki/%E0%A4%95%E0%A5%81%E0%A4%A3%E0%A5%8D%E0%A4%A0\" \\\n \"https://en.wiktionary.org/wiki/%D8%AE%D9%84%D9%86%D8%AC\" \\\n \"https://en.wiktionary.org/wiki/%D8%AE%D9%88%D9%84%D9%86%D8%AC%D8%A7%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%DA%AF%D9%86%D8%AF%D8%A2%D9%88%D8%B1\" ; do\n  python3 tools/fetch_source.py \"$u\" --note \"page 285 verification (galingale / kond / konj / hunch)\" 2>&1 | tail -1\ndone"
}
```


### [2026-09-06T21:52:05.551Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/791ac44ffac65f35.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ef38195e62a71b47.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3eb7829a79ec8ef1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/20ca11854e804bbb.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0746b4c6f8262838.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/805d876a2041de25.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4dc7776ebfb967c9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/96647a4f999123b0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a80bcdb7237e3096.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/27a46996f811cf90.txt
```


## [2026-09-06T21:52:07.696Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in 791ac44ffac65f35 ef38195e62a71b47; do echo \"=== $f ===\"; grep -n -i -A6 'Etymology' $f.txt | head -60; done"
}
```


### [2026-09-06T21:52:09.503Z] TOOL RESULT

```
=== 791ac44ffac65f35 ===
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
--
148: Etymology
149- [ edit ] 
150-
151- From Middle English galingale , from Old French galingal , from Arabic خَلَنْجَان ( ḵalanjān ) , from Persian قولنجان ( qulenjân, qulanjân ) , from Sanskrit कुलञ्जन ( kulañjana ) , perhaps from Chinese 高良薑 ／ 高良姜 ( gāoliángjiāng ), from 高涼  / 高凉 ( Gāoliáng ) (a prefecture or county in China) + 薑  / 姜 ( jiāng , “ ginger ” ) .
152-
153- Pronunciation
154- [ edit ] 
=== ef38195e62a71b47 ===
4:TITLE: Etymonline - Online Etymology Dictionary
5-
6:Etymonline - Online Etymology Dictionary 
7-
8- Search 
9- Log in 
10-
11- Columns 
12- Forum
```


## [2026-09-06T21:52:16.527Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"=== کند (3eb78) ===\"; sed -n '100,260p' 3eb7829a79ec8ef1.txt"
}
```


### [2026-09-06T21:52:16.582Z] TOOL RESULT

```
=== کند (3eb78) ===

 3.2.1 
 Noun 

 3.2.1.1 
 Related terms 

 3.2.1.2 
 Descendants 

 3.2.2 
 Further reading 

 3.3 
 Etymology 3 

 3.3.1 
 Pronunciation 

 3.3.2 
 Noun 

 3.3.2.1 
 Descendants 

 3.4 
 Etymology 4 

 3.4.1 
 Noun 

 3.5 
 Etymology 5 

 3.5.1 
 Noun 

 3.5.1.1 
 Derived terms 

 3.6 
 Etymology 6 

 3.6.1 
 Pronunciation 

 3.6.2 
 Verb 

 4 
 Urdu 

 Toggle Urdu subsection 

 4.1 
 Adjective 

 Toggle the table of contents 

 کند 

 10 languages 

 فارسی 
 Français 
 Bahasa Indonesia 
 Kurdî 
 Malagasy 
 Norsk bokmål 
 پنجابی 
 Русский 
 Slovenščina 
 Тоҷикӣ 

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

 See also: گند 

 Khalaj
 [ edit ] 

 Adjective
 [ edit ] 

 کُند ( kund or künd ) 

 Arabic spelling of kund , künd ( “ blunt ” ) 

 Pashto
 [ edit ] 

 Noun
 [ edit ] 

 کند • ( kand )  m 

 ravine , gorge 

 pit 

 honeycomb 

 References
 [ edit ] 

 “ کند ”, in Pashto Dictionary , Peshawar, Pakistan: Pukhtoogle, 2020 . 

 Pashtoon, Zeeya A. ( 2009 ), “ کند ”, in Pashto–English Dictionary , Hyattsville: Dunwoody Press 

 Persian
 [ edit ]
```


## [2026-09-06T21:52:18.599Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nsed -n '260,420p' 3eb7829a79ec8ef1.txt"
}
```


### [2026-09-06T21:52:18.648Z] TOOL RESULT

```
 [ edit ] 

 Etymology 1
 [ edit ] 

 Perhaps ultimately related to the root of Old Armenian ճաղատ ( čałat , “ bare, bald ” ) . [ 1 ] Of dubious connection to Sanskrit कुण्ठ ( kuṇṭhá , “ blunt, dull ” ) .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ˈkund/ 

 ( Dari, formal ) IPA ( key ) : [kʰʊn̪d̪] 

 ( Dari, formal ) IPA ( key ) : [kʰʊn̪d̪] 
 ( Kabuli ) IPA ( key ) : [kʰʊn̪d̪] 

 ( Hazaragi ) IPA ( key ) : [kʰun̪d̪̥] 

 ( Iran, formal ) IPA ( key ) : [kʰon̪d̪̥] 

 ( Tajik, formal ) IPA ( key ) : [kʰun̪d̪] 

 Rhymes: -und 

 Readings

 Classical reading ? 

 kund

 Dari reading ? 

 kund

 Iranian reading ? 

 kond

 Tajik reading ? 

 kund

 Adjective
 [ edit ] 

 کند • ( kond ) ( comparative کندتَر , superlative کندتَرین ) 

 blunt 

 dull 

 slow 

 Descendants
 [ edit ] 

 → Azerbaijani: künd 

 → Azerbaijani: küt 

 → Khalaj: kund 

 → Turkish: küt 

 References
 [ edit ] 

 ^ Bulletin of the School of Oriental and African Studies, University of London. (1961). United Kingdom: The School, p. 479 

 Further reading
 [ edit ] 

 Asatrian, Garnik ; Arakelova, Victoria ( 2001 ), “Blunt, Bald and Wise: Iranian kund(-) ”, in Iran and the Caucasus ‎ [1] , volume 5, pages 201–206 

 Etymology 2
 [ edit ] 

 Noun
 [ edit ] 

 کند • ( kond ) 

 fetter , clog ; stocks 

 Related terms
 [ edit ] 

 کنده ( konde ) 

 Descendants
 [ edit ] 

 → Armenian: կունդ ( kund ) 

 Further reading
 [ edit ] 

 Asatrian, Garnik ; Arakelova, Victoria ( 2001 ), “Blunt, Bald and Wise: Iranian kund(-) ”, in Iran and the Caucasus ‎ [2] , volume 5, pages 201–206 

 Steingass, Francis Joseph ( 1892 ), “ کند ”, in A Comprehensive Persian–English dictionary (overall work in English), London: Routledge & K. Paul, page 1053 

 Etymology 3
 [ edit ] 

 Etymology tree

 Sanskrit क्षद् ( kṣad ) der. ? 
 Sanskrit खण्ड ( khaṇḍa ) bor. 
 Persian کند 

 Borrowed from Sanskrit खण्ड ( khaṇḍa ) .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ˈkand/ 

 ( Dari, formal ) IPA ( key ) : [kʰän̪d̪] 

 ( Dari, formal ) IPA ( key ) : [kʰän̪d̪] 
 ( Kabuli ) IPA ( key ) : [kʰän̪d̪] 

 ( Hazaragi ) IPA ( key ) : [kʰän̪d̪̥] 

 ( Iran, formal ) IPA ( key ) : [kʰʲæn̪d̪̥] 

 ( Tajik, formal ) IPA ( key ) : [kʰän̪d̪] 

 Rhymes: -and 

 Readings

 Classical reading ? 

 kand

 Dari reading ? 

 kand

 Iranian reading ? 

 kand

 Tajik reading ? 

 kand

 Noun
 [ edit ] 

 کند • ( kand ) 

 candied sugar 

 Descendants
 [ edit ] 

 Descendants
```


## [2026-09-06T21:52:27.787Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\ngrep -n -i 'Etymology' -A14 20ca11854e804bbb.txt | sed -n '1,40p'\necho \"==== persian section ====\"\nawk '/^ Persian$/,0' 20ca11854e804bbb.txt | head -80"
}
```


### [2026-09-06T21:52:29.553Z] TOOL RESULT

```
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
69-
70- 1.3.1 
71- Descendants 
72-
73- 1.4 
74- References 
75-
76- Toggle the table of contents 
--
148: Etymology
149- [ edit ] 
150-
151- Uncertain. Related to Sanskrit कुञ्चित ( kuñcita , “ curved, bent, crooked ” ) , कुञ्चन ( kuñcana , “ contraction ” ) , Old Armenian կնճիռն ( knčiṙn , “ knot ” ) .
152-
153- Pronunciation
154- [ edit ] 
155-
156- ( Classical Persian ) IPA ( key ) : /ˈkund͡ʒ/ 
157-
158- ( Dari, formal ) IPA ( key ) : [kʰʊnd͡ʒ] 
159-
160- ( Dari, formal ) IPA ( key ) : [kʰʊnd͡ʒ] 
161- ( Kabuli ) IPA ( key ) : [kʰʊnd͡ʒ] 
162-
==== persian section ====
 Persian
 [ edit ] 

 Etymology
 [ edit ] 

 Uncertain. Related to Sanskrit कुञ्चित ( kuñcita , “ curved, bent, crooked ” ) , कुञ्चन ( kuñcana , “ contraction ” ) , Old Armenian կնճիռն ( knčiṙn , “ knot ” ) .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ˈkund͡ʒ/ 

 ( Dari, formal ) IPA ( key ) : [kʰʊnd͡ʒ] 

 ( Dari, formal ) IPA ( key ) : [kʰʊnd͡ʒ] 
 ( Kabuli ) IPA ( key ) : [kʰʊnd͡ʒ] 

 ( Hazaragi ) IPA ( key ) : [kʰund͡ʒ̥] 

 ( Iran, formal ) IPA ( key ) : [kʰond͡ʒ̥] 

 ( Tajik, formal ) IPA ( key ) : [kʰund͡ʒ] 

 Rhymes: -und͡ʒ 

 Readings

 Classical reading ? 

 kunj

 Dari reading ? 

 kunj

 Iranian reading ? 

 konj

 Tajik reading ? 

 kunj

 Noun
 [ edit ] 

 کنج • ( kunj / konj ) ( plural کنج‌ها ( kunj-hā / konj-hâ ) , Tajik spelling кунҷ ) 

 corner 

 Descendants
 [ edit ] 

 → Azerbaijani: künc 

 → Armenian: քունջ ( kʻunǰ ) 

 → Georgian: ქუნჯი ( kunǯi ) 

 → Ottoman Turkish: كنج ( künc ) Turkish: künc 
 → Armenian: քիւնճ ( kʻiwnč ) 

 References
 [ edit ] 

 Nourai, Ali ( 2011 ), An Etymological Dictionary of Persian, English and other Indo-European Languages , page 255 

 Retrieved from " https://en.wiktionary.org/w/index.php?title=کنج&oldid=89607841 "

 Categories : Persian terms with unknown etymologies 
 Persian terms with IPA pronunciation 
 Rhymes:Persian/und͡ʒ 
 Rhymes:Persian/und͡ʒ/1 syllable 
 Persian lemmas 
 Persian nouns 

 Hidden categories: Pages with entries 
 Pages with 1 entry
```


## [2026-09-06T21:52:36.807Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"=== wikt hunch ===\"; grep -n -i 'Etymology' -A10 0746b4c6f8262838.txt | sed -n '20,80p'\necho \"=== etymonline hunch ===\"; grep -n -i 'hunch' 805d876a2041de25.txt | head -30"
}
```


### [2026-09-06T21:52:36.876Z] TOOL RESULT

```
=== wikt hunch ===
189- Pronunciation
190- [ edit ] 
191-
192- IPA ( key ) : /hʌnt͡ʃ/ , /hʌnʃ/ 
=== etymonline hunch ===
1:URL: https://www.etymonline.com/word/hunch
4:TITLE: Hunch - Etymology, Origin & Meaning
6:Hunch - Etymology, Origin & Meaning 
54: Origin and history of hunch 
56: hunch (v.) 
58: "raise or bend into a hump," 1650s; earlier "to push, thrust" (c. 1500), of unknown origin. Perhaps a variant of bunch (v.). Related: Hunched ; hunching .
61: hunch (n.) 
63: 1620s, "a push, a thrust," from hunch (v.) in its older sense. The figurative meaning "a hint, a tip" (a "push" toward a solution or answer), is recorded by 1849 and led to that of "premonition, presentiment" (by 1904).
66: Entries linking to hunch 
72: hunchback (n.) 
74: "person with a hunched back," 1712, back-formation from hunchbacked (1590s; see hunch ).
94: c. 1400, "bulging, convex," from Late Latin gibbus "hunchbacked," from Latin gibbus "a hump, a hunch," as an adjective, "...
98: It progresses by hunch, vision, and intuition....
120: Share hunch 
124: https://www.etymonline.com/word/hunch Copy 
127: <a href="https://www.etymonline.com/word/hunch">Etymology of hunch by etymonline</a> Copy 
130: Harper, D. (n.d.). Etymology of hunch. Online Etymology Dictionary. Retrieved September 5, 2026, from https://www.etymonline.com/word/hunch Copy 
133: Harper Douglas, "Etymology of hunch," Online Etymology Dictionary, accessed September 5, 2026, https://www.etymonline.com/word/hunch. Copy 
136: Harper, Douglas. "Etymology of hunch." Online Etymology Dictionary, https://www.etymonline.com/word/hunch. Accessed 5 September, 2026. Copy 
139: D. Harper. "Etymology of hunch." Online Etymology Dictionary. https://www.etymonline.com/word/hunch (accessed September 5, 2026). Copy 
146: Dictionary entries near hunch 
152: hunch 
153: hunchback
```


## [2026-09-06T21:52:43.417Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nsed -n '175,200p' 0746b4c6f8262838.txt\necho \"=== خلنج wikt ===\"; sed -n '100,200p' 96647a4f999123b0.txt\necho \"=== خولنجان wikt ===\"; sed -n '100,200p' a80bcdb7237e3096.txt"
}
```


### [2026-09-06T21:52:43.487Z] TOOL RESULT

```
 hide 

 From Wiktionary, the free dictionary

 English
 [ edit ] 

 Etymology
 [ edit ] 

 Assibilated variant of hunk , of uncertain origin.

 Alternatively, a derivative of hump , via an earlier Middle English *hunche , *humpchin , from *hump +‎ -chin, -chen ( diminutive suffix ) , equivalent to hump +‎ -kin . In the sense of an intuitive impression, said to be from the old gambling superstition that it brings luck to touch the hump of a hunchback.

 Pronunciation
 [ edit ] 

 IPA ( key ) : /hʌnt͡ʃ/ , /hʌnʃ/ 

 Audio ( US ) : ( file ) 

 Rhymes: -ʌntʃ 

 Noun
 [ edit ] 

=== خلنج wikt ===
 Noun 

 2.3 
 Further reading 

 Toggle the table of contents 

 خلنج 

 5 languages 

 فارسی 
 Magyar 
 Malagasy 
 Polski 
 پښتو 

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

 Arabic
 [ edit ] 

 خَلَنْج – Calluna vulgaris 

   خلنج on Arabic Wikipedia

 Etymology
 [ edit ] 

 Borrowed from Classical Persian خلنگ ( xalang , “ heather ” ) 

 Pronunciation
 [ edit ] 

 IPA ( key ) : /xa.land͡ʒ/ 

 Noun
 [ edit ] 

 خَلَنْج • ( ḵalanj )  m 

 heather , various Ericeae  plants
 c. 910 , Aḥmad ibn Muḥammad ibn al-Faqīh al-Hamaḏānī , Kitāb al-Buldān ‎ [1] : وَلَهُمُ ٱلثِّيرَانُ ٱلْأَرْمِينِيَّةُ، وَٱلشَّاهْ بَلُّوطُ، وَٱلْ خَلَنْجُ ٱلْكَثِيرُ، وَيَتَّخِذُونَ مِنْهُ عَجَائِبَ. walahumu ṯ-ṯīrānu l-ʔarmīniyyatu, waš-šāh ballūṭu, wal- ḵalanju l-kaṯīru, wayattaḵiḏūna minhu ʕajāʔiba. And they have Armenian apricot, chestnut, and much heather , and they obtain miracles from it. 

 Declension
 [ edit ] 

 Declension of noun خَلَنْج ( ḵalanj )

 singular

=== خولنجان wikt ===
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

 Arabic
 [ edit ] 

 خولَنْجَان 

 Arabic Wikipedia has an article on: خولنجان 

 Wikipedia ar 

 Alternative forms
 [ edit ] 

 خَلَنْجَان ( ḵalanjān ) 

 Etymology
 [ edit ] 

 From Persian قولنجان ( qulanjân, qulenjân ) , from Sanskrit कुलञ्जन ( kulañjana ) , possibly from Chinese 高良薑 ／ 高良姜 ( gāoliángjiāng ).

 Pronunciation
 [ edit ] 

 IPA ( key ) : ( classicized ) /xaw.lan.d͡ʒaːn/ , ( originally and dialectally ) /xuː.lan.d͡ʒaːn/ 

 Noun
 [ edit ] 

 خَوْلَنْجَان or خُولَنْجَان • ( ḵawlanjān or ḵūlanjān )  m 

 galangal ( Alpinia gen. et spp. and especially Alpinia officinarum )

 Declension
 [ edit ] 

 Declension of noun خَوْلَنْجَان ( ḵawlanjān )‎; خُولَنْجَان ( ḵūlanjān )

 singular

 basic singular triptote 

 indefinite

 definite

 construct

 informal

 خَوْلَنْجَان ‎; خُولَنْجَان 
 ḵawlanjān ‎; ḵūlanjān 

 الْخَوْلَنْجَان ‎; الْخُولَنْجَان 
 al-ḵawlanjān ‎; al-ḵūlanjān 

 خَوْلَنْجَان ‎; خُولَنْجَان 
 ḵawlanjān ‎; ḵūlanjān
```


## [2026-09-06T21:52:59.830Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SKT ===\"; grep -n -i 'galingale\\|galanga' SKT.txt | head -5\necho \"=== FSD ===\"; grep -n -i 'galingale\\|galanga' FSD_vol1.txt FSD_vol2.txt | head -5\necho \"=== WEB ===\"; grep -n -i 'galingale\\|galangal' WEB_vol1.txt | head -5\necho \"=== HJB ===\"; grep -n -i 'galangal\\|galingale' HJB.txt | head -5\necho \"=== DEV/PHN ===\"; grep -n -i 'galanga\\|garingal' DEV.txt PHN.txt | head -10\necho \"=== AFM ===\"; grep -n 'خولنجان\\|خلنج' AFM_pages.txt | head -10\necho \"=== TAD ===\"; grep -n 'خولنجان\\|خلنج' TAD_pages.txt | head -10"
}
```


### [2026-09-06T21:52:59.964Z] TOOL RESULT

```
=== SKT ===
23699:French  from  Spanish  from  Arabic,  am* ber,  cotton  (i),  fonfnre,  galingale,  garble, garbage,  genet,  ;ennet  (genact),  lackey Jacquey).  mojJc  (masque),  masquerade, mosque,  ogee  (ogive),  racket  (1)  traquct), realgar,  ream,  »umach,  syrup  (sinip),  tabby, talc,  tare  (3),  tariff,  zenith,
=== FSD ===
FSD_vol1.txt:12930:tuberous,  aromatic  rootstocks  and  terminal  spikes,  racemes, or  panicles  of  curious  and  handsome  flowers.  A.  nutans, the  shellflower.  Is  In  ornamental  cultivation  for  Its  flowers; A.  vittata,  the  striped  alplnla,  for  its  leaves;  and  other species  for  the  rootstocks.  See  galangal.  2.  [a-]  Any plant  of  this  genus.  ( <   Prospero  Alpin,  It.  botanist.] .
FSD_vol1.txt:12931:A   special  monkish  form  of  it,  the  Gothic,  Is  In  use  in  Ger-  al'pl-nln,  1   al'pi-nin;  2   fiFpi-nln,  n.  Chem.  A   yellow many,  Denmark, and  Norway.—  telegraphic  a.,  one  of  the  crystalline  compound  (CnHizOe)  found  in  galangal. various  alphabets  used  in  telegraphy.  See  telegraph.—  AJ-pPnus,  1   ol-prnQs;  2   al-pl'nus,  Prospero  0 >/ji1553-2/» al  pha-bet,  rf.  To  alphabetize.— al"pha-bet-a'rl-an,  n.  1617).  An  Italian  botanist  and  medical  writer.  Al'plnL
FSD_vol1.txt:56004:cam-pliane',  1   kam-fen';  2   cilm-fan',  n.  Chem.  A   hy-  galangal  root, pothetical  hydrocarbon  (CioHia)  from  which  camphor  cam'phor-lzc,  1   kam'for-ciz;  2   cfim'for-Iz,  vt.  (-ized; and  related  compounds  are  derived,  making  together  -izTng.]  To  campboratc.
FSD_vol1.txt:65032:tree  (Platcmus  ortenialls).  [Hind.,  <   Per.  chendr.]  che- nar'*tree"?;  chl-nar'«tree"t. chI'na*root",  l   dhai'na-rtit';  2   chl'na-root*,  n.  1.  The knotty  rootstock  of  an  Oriental  shrubby  climber  (Smilax china),  or  of  various  American  smllaxes,  as  the  bastard china-root  (5.  pseudo*chlna).  2.  Galangal.— Carolina
FSD_vol2.txt:29137:ga-lan'gal,  1   go-lan'gal;  2   ga-lan,'gal,  «,  1.  The  aromatic stimulant  rootstocks  of  various  East-Indian  herbs  of  the ginger  family  (Zingiberaceas);  e.spectally.  several  species  of Alpinia,  as  A.  galanga,  A.  ojficlnarum,  and  A.  racetnvsa,  and &   species  ot  Kiempferia,  IC.  galanga.  2.  A. sedge.  SeecALiN- GALB.  [ME.  galingale,  galange,<  OF.  galingal,  galange,< LL.  galanga,  <   At.  khalanjan,  <   Chin.  Ko-liatig^kiang,  <   Ko in  Canton,  +   Zfanff,  mHd,+  Wawff,  ginger.]  ga-Ian'gat;  ga- lange't.—  edible  galangal,  a   species  (Cyperus  esculeritus) that  spreads  extensively  by  means  of  Its  tuber-bearing  root- stocks and  often  proves  a   pest  in  cultivated  fields;  the  yel- low nut-grass.— lank  g.,  a   perennial  cyperus  (Cyperus strigosus)  with  tuber-like  corms  and  culm  1-3  feet  high; found  in  wet  places  in  the  eastern  United  States. ga-lang"»ga-Iang',  1   g8-mn''«gs-iao';  2   ga-lang'-ga-iitag',  n.
=== WEB ===
79502:ga-lan’gaAl, ga-lan’gale, n. same as galingale.
79575:ga-lette’, n. [Fr.] a thin cake; a buttered roll. Ga-lé’us, n. the typical genus of the family Galeide. gale’wort, n. in botany, same as gale. Ga-li’bi, n. any member of a subdivision of Carib Indians living in the Guianas. Ga-li’ciin (-lish’un), a. 1. of Spanish Galicia, its people, or language. 2. of Polish Galicia or its people. Ga-li‘cidn, n. 1. a native or inhabitant of Spanish Galicia. 3 wee Portuguese dialect of the Spanish alicians. 3. a native or inhabitant of Polish Galicia. Gal-i-lé/An, a. pertaining or belonging to Gal- ileo, the Italian astronomer and physicist (1564-1642); as, the Galilean telescope. Galilean telescope; a telescope having a con- cave eyepiece. Pee Gal-i-lé/An, a. [L. Galileus; Gr. Galilaios. of or pertaining to Galilee, from Galilaia, Galilee; Heb. Galil, Galilee, lit., a circle.] relating to Galilee, an ancient division of northern Pales- tine, or its people. A Last came, and last did go, z The pilot of the Galilean lake.—Milton. ; Gali-lé/an, n. 1. a native or inhabitant o! Galilee. 2. in Jewish history, one of a class among the Jews, during the reign, of Augustus: | resisted the payment of tribute to Rome. 3. a Christian. the Galilean; Jesus. Gd gal/i-lee, n. (OFT. galilee, from L. Galeri Galilaia, Galilee, Heb. Galil, Gali ee 2 circle.] a porch or chapel at the west €. of some medieval churches. gal-i-m4/ti-ds (-shi-us), 1. (Fr., berish.] confused speech; confused or nonsensical talk. She ran into absurdities i scarce credible a al-i-mé/ta wood, |a nativ: a aiai S white bully tree, Dipholis salicifolia ; the West Indies. 3 f _ gol- gal’in-gale, 7. IME Ors galingal; ML. | 1ga; Ar. khalanjan. ‘ vari- oot the pun; ene aromatic root stem of wily: ous East Indian plants of the oe owing in 2. a sedge with a pungent roo Je the south of England; sweet sedge. Also galangal, (ane a aa al-idn-gee’, n. z a Een a sail intoa navy, fr a man-of-war.] a Turki All that a careless eye could see
=== HJB ===
7896:1298.— <' This  Island  (Java)  is  of  surpass- ing wealth,  producing  blaok  pepper,  nutmegs, spflcenard,  galingale,  onbeM,  cloves.  .  •  ." ^Marco  PoU,  ii.  254.
=== DEV/PHN ===
DEV.txt:1374:Galanga.  Esp.  et  portug.  galanga,  anc.  franc,  galangal , garlngal,  angl.  galangale.  Le  nom  de  cette  plante,  origi- naire  des  Indes,  nous  est  venu  par  l'arabe  (jUxLjw  kha-
DEV.txt:3505:Galanga.
DEV.txt:3506:Galaoffal,  voy.  Galanga.
DEV.txt:3507:Galangale,  angi  voy.  Galanga,
DEV.txt:3508:Galanguo,  voy.  Galanga.
DEV.txt:3522:Garingal,  voy.  Galanga.
DEV.txt:3778:Lonquas,  voy.  Galanga.
DEV.txt:4752:^jyjliw  turc,  voy.  Kadine. ijLk  voy.  Khan. *jLi.  pers.  voy.  Khan. ^.Jsi^  pers.  voy.  Khédive. ^Iji^  voy.  Caratch. *jb*^  voy.  Kharbega. S7^  voy.  Gorge. »^\y^  turc,  voy.  Rusma. cjyi*iw  voy.  Artichaut. i_;.^-.ii.  voy.  Garoube. iôj^  voy.  Garoube. ^^ji».  voy.  Magasin. AjLjyii.  voy.  Kazine. ob.^  k-^  vov.  Hatti-cliérii. (j^\$  ia^  voy.  Hatti-chorif. ^^.♦iai^  voy.  Ketmie. 'sMjL^  voy.  Gaphar. ybjLi^  voy.  Caftan. Li'^K^  voy.  Glialef. (jljs\J<£^  voy.  Galanga. «xjLjAii-  voy.  Galite. ^j^w*»^  voy.  Khamsin. *sÂ.3w  voy.  Alfange. ts*^^!^  voy.  Algorithme. ooLo^^  pers.  voy.  Gourmand, ^~Aji.  jaeî's.  voy.  Gheirantbo. c^w^  voy.  Cheiranthc.
DEV.txt:5103:^l^iCitJ  mer/,  voy.  Galanga.
=== AFM ===
=== TAD ===
```


## [2026-09-06T21:53:09.989Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nls site/pages/285.jpg 2>/dev/null; pdftoppm -f 285 -l 285 -r 300 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg285 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg285.png"
}
```


### [2026-09-06T21:53:12.522Z] TOOL RESULT

```
site/pages/285.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 84487 Sep  6 17:53 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg285.png
```


## [2026-09-06T21:53:14.535Z] TOOL CALL #37: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg285.png"
}
```


### [2026-09-06T21:53:15.190Z] TOOL RESULT

```

```


## [2026-09-06T21:53:15.187Z] INPUT

[Image: original 2550x3300, displayed at 1546x2000. Multiply coordinates by 1.65 to map to original image.]


## [2026-09-06T21:53:37.407Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK kund/kunt ===\"; grep -n 'kundos\\|kunt-\\|kunthá\\|kuṇṭha\\|kuntha' POK_full.txt POK_01.txt POK_02.txt POK_03.txt 2>/dev/null | head -10\necho \"=== POK kunk/kunč ===\"; grep -n 'kuñc\\|kunc-\\|kuñca\\|knčirn' POK_full.txt 2>/dev/null | head -10\necho \"=== WLD band3 ===\"; grep -n 'kunt\\|kunj\\|kunk' WLD_band3.txt | head -10\necho \"=== AHD watkins ===\"; grep -n -i 'hunch\\|galingale\\|kunth' AHD_watkins1985.txt | head -10\necho \"=== SYN blunt/dull ===\"; grep -n -i 'kuṇṭha\\|kuntha\\|blunt' SYN.txt | head -10"
}
```


### [2026-09-06T21:53:37.513Z] TOOL RESULT

```
=== POK kund/kunt ===
=== POK kunk/kunč ===
=== WLD band3 ===
=== AHD watkins ===
530:*kunnan in Old English cunnan, to know, know how to, be able to (Old English first and third singular can from Germanic *kann from o-grade *gona-): CAN}, CON2, CUN- NING; b. Germanic causative verb *kannjan, to make known, in Old English cennan, to declare, and Old Norse kenna, to name (in a formal poetic metaphor): KEN, KENNING; c. Germanic *kunthaz in Old English cath, known, well-known, usual, excellent, familiar: (COUTH); UNCOUTH; d. Germanic *kunthithd in Old English cyth(the), cyththu, knowledge, acquaintance, friendship, kinfolk: KrTH. 3. Suffixed form *gné-sko- in Latin (g)n6- Scere, cognéscere, to get to know, get acquainted with: NOTICE, NOTIFY, NOTION, NOTORIOUS; (ACQUAINT), COG- NITION, (COGNIZANCE), (CONNOISSEUR), (QUAINT), REC- OGNIZE. 4. Suffixed form *gné-ro- in Latin igndrdre, not to know, to disregard (i- for in-, not; see ne): IGNORANT, IGNORE. 5. Suffixed form *gn6-dhli- in Latin nobilis, knowable, known, famous, noble: NOBLE. 6. Redupli- cated and suffixed form *gi-gn6é-sko- in Greek gignd- skein, to know, think, judge (and *gnd- in gndm6n, a judge, interpreter): GNOME2, GNOMON, GNOSIS; AGNOSIA, DIAGNOSIS, PATHOGNOMIC, PHYSIOGNOMY, PROGNOSIS. 7. Suffixed zero-grade form “gna-ro- in Latin gndrus, knowing, expert, whence narrdre (< *gnarrare), to tell, relate: NARRATE. (8. Traditionally but improbably re- ferred here are: a. Latin nota, a mark, note, sign, cipher, shorthand character: NOTE; ANNOTATE, CONNOTE, PRO- THONOTARY; b. Latin norma, carpenter’s square, rule, pattern, precept: NORM, NORMA, NORMAL; ABNORMAL, ENORMOUS.) [Pok. 2. gen- 376.]
=== SYN blunt/dull ===
8130:Skt. munda- ‘with shaven head’ (also ‘hornless, blunt’), perh.: Skt. 7d- ‘crush, rub’, etc. Walde-P. 2.288 (287),
8184:1. Grk. xw¢és, in Hom. ‘dull, blunt? (xawpdv Bédos ‘blunt missile’) and ‘mute, noiseless’ (xipart xwd ‘with noiseless wave’), later both ‘dumb’ and ‘deaf’ (so still in NT), but NG xougés only ‘deaf’, prob. : xndqv ‘drone’, ChSl. chabiti ‘spoil’, pochabii ‘foolish’, Boh. ochabiti ‘make loose, weak’. Walde-P. 1.348. Boisacq 452.
8189:4. Goth. baups, etym. dub. Possibly as orig. ‘blunt’ : MDu. bot ‘dull, stupid’, LG butt ‘blunt, coarse’, Norw. dial. buit ‘blunt’, cf. also Arm. bot‘ ‘blunt’. Pers- son, Beitrige 256. Feist 86. Otherwise Walde-P. 2.190 (cf. above, 3).
8190:ON daufr, OF déaf, OHG toub, etc., general Gmc. (in most cases also in the sense of ‘dull, slow’ of mind or body; Goth. only in this sense, daubata hairto ‘dulled heart’, Mk. 8.17): ON deyfa ‘blunt, stupefy’, dofinn ‘dull, drowsy’ (Dan. doven ‘lazy’ 4.92), MHG touben ‘stupefy’, etc., Grk. ridw ‘raise a smoke, stupefy with smoke’, suddds ‘blind’ (4.97), ete., here also Goth. dumbs ‘dumb’, etc., OHG tumb ‘stupid, dumb, deaf’ (4.96), fr. *deu-bh- extension of IE *dheu- in Skt. dhia- ‘shake’, dhtima- ‘va- por, smoke’, Grk. 6iw ‘rush, rage’ and numerous other formations, with a com- mon notion of ‘whirling, rapid, dizzy motion’, applied to various physical and mental phenomena, and including some
14740:6. ChSl. remistvo (Supr., etc.), Boh. Femeslo, Pol. rzemtosto (desto), Russ. remeslo : Lith. remesas, Lett. remesis ‘craftsman, carpenter’, OPruss. romestud ‘ax’, all prob. fr. the root of Lith. ram- tyte ‘cut, carve’, Lett. ramstit ‘hew, saw’ (with a blunt tool), further con- nections dub. Mithl.-Endz. 3.509 f. Briickner 475. Buga, Kalba ir Senové 279. : ChSl. chytrostt (Jagié, Entstehungs- gesch. 415), deriv. of chytrit ‘skilled, crafty’ : Russ. chitryj ‘cunning, crafty’, Bulg. hitur ‘wise’, SCr. hitar ‘quick, ex- perienced, skilled’, etc. Berneker 414.
24780:gs ‘ on trai 204 f. Hellquist 1236. ott ce slow, fr. OF slaw ‘dull (of 0B, ruggish, lazy’ : ON sijor, slitr, é etc. ‘dull, blunt’ (15.79).
27095:15.79 BLUNT, DULL
27099:Sp. boto, embotado ME blunt, dul(l) Pol. lepy
27100:Rum.  tocit NE blunt, dull Russ. tupoj -Ir. mael Du. stomp Skt. alikgna- Nir. maol OHG  sléo Av. ee
27107:2. Lat. hebes, beside hebére ‘be blunt’, etym. dub. Walde 1.349. Ernout-M. 447 (suggesting borrowing). Walde-H. 1.637 £.
```


## [2026-09-06T21:53:43.914Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '27095,27125p' SYN.txt\necho \"=== HRN kund/kunǰ ===\"; grep -n 'kund\\|kunǰ\\|kunj\\|gund' HRN.txt | head -20\necho \"=== HUB ===\"; grep -n 'kund\\|kunǰ\\|kunj\\|gund' HUB.txt | head -20"
}
```


### [2026-09-06T21:53:43.985Z] TOOL RESULT

```
15.79 BLUNT, DULL
Grk.  dsBAbs Goth. Lith. atSipes, bukas NG auBXbs ON sljor Lett. neass, truls Lat. —_hebes, obtisus Dan.  slgv, stump ChSl. itqpit
It. ottuso, smussato Sw. slé SCr.  tup
Fr. émoussé OE Gstynt Boh. tupy
Sp. boto, embotado ME blunt, dul(l) Pol. lepy
Rum.  tocit NE blunt, dull Russ. tupoj -Ir. mael Du. stomp Skt. alikgna- Nir. maol OHG  sléo Av. ee
W. pul MHG slé, stumpf
Br. souc’h, dall, tougn NHG  stumpf
The words listed are used both of a point and of an edge, but in several it is clear that the former application is the earlier. The most frequent connection is with words for ‘cut’, ‘strike’, ‘beat’, ‘stamp’, etc., here as ‘cut off’, etc. Some- times the development is through ‘shortened, mutilated’, or from ‘weak, inefficient’. In a few cases the applica- tion to mentality, usually secondary, is the earlier.
1. Grk. dyBdbs, fr. *éurus : &padds
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
‘weak, tender’, prob. fr. the root in Lat. mollis, Grk. padaxés ‘soft’, etc. (15.75). Walde-P. 2.285, 292).
2. Lat. hebes, beside hebére ‘be blunt’, etym. dub. Walde 1.349. Ernout-M. 447 (suggesting borrowing). Walde-H. 1.637 £.
Lat. obtiisus (> It. ottuso), fr. obtun- dere ‘beat’, of a weapon ‘beat back wd point, dull’, cpd. of tundere ‘beat pound’. Ernout-M. 1064.
It. smussato, pple. of smussare, fr. Fr.
SENSE PERCEPTION
ser ‘tO dull’, pple. émoussé, deriv. "Tt. mozzo ‘cut off, shortened’, fr. a +mutios beside mutilus ‘cut off,
nortened, mutilated’. REW 5792. s
grnout-M. Port. boto (Sp. embotar ‘to dull’, ”
le. embotado), Fr. bot in piedbot ‘club- foot’, loanword fr. Gniti; ef. Du: bot, LG but ‘blunt’, NE butt ‘thick end’, belong- ing to the same group as OFr. bouter igtrike’, etc. fr. Frank. *bdtan or *but- jan ; OF béatan ‘beat’, etc. (9.21). REW 1228¢. Wartburg, 1.455 ff.
Rum. tocit, fr. oct ‘make blunt, dull’, this fr. Slavic, ef. SCr. tociti ‘whet, grind off the edge’. Tiktin 1616.
3, Ir. mael, Nir. maol, also ‘bald, hornless’ : OW mail ‘mutilum’, W. moel ‘bare, bald, hornless’, fr. the root *maz- in Goth. maztan ‘cut, hew’, etc. Walde- P. 2.222.
W. pul, origin?
Br, souc’h : Ir. socc ‘snout’. Thurney- sen ap. Ernault, Dict. étym. 382.
Br. dall, lit. ‘blind’ (W., Ir. dall ‘blind’, cf. ME dul(l), below).
Br. tougn also ‘shortened,
snub-
‘d
(@)styntan, for-styntan
(NE stint), ON stytta tluttr ‘shore’ OE stunt ‘foolish’, ON oth te» etc., prob. fr. the root of
* Slautan ‘shove’, Lat. tundere ‘beat?
=== HRN kund/kunǰ ===
783:40. ägäh, kundig, Kunde'.
785:äkäsimtan, arm. LW. akah 'kundig'; ai. Kiä^-, ka^ate
797:kundäre Form und ü ursprünglich sein müsste. Auch
1398:Die augenscheinlich sekundäre Bildung enjäften
3509:Sekundär wird zu täften ein Infinitiv tayten gebildet;
4381:neunten indischen Klasse sekundär wieder eingeführt
5239:np. döstdär ist eine sekundäre Missbildung.
6512:Np. senjJdm (mit sekundärem Infinitiv se/ten —
6515:^wiegen* ist ein sekundäres Denominativum von seng,
6696:II, 24, VIII, 1 ist gewiss erst sekundär wie cübän
7031:phlv. gund 'Heer ; arm. L\V. gu7id 'Heer, arab.
7547:868. kund 'stumpf; tapfer*.
8129:936. gunde *Hefenballen (für ein BrotV.
8130:aw. gunda- (vd. 3, 32) 'Teig (Geldnor, KZ. 24,
8131:549 Note 4); phlv. gundak.
8221:Die Bedeutung 'Edelstein* ist erst sekundär; sie
8479:Die sekundäre Bedeutung von gel. merz 'Damm, der durch einen Fluss
8484:*) Sekundäres v wie in phlv. marvärU^ np. mervärld gegen arab.
8796:wohl erst sekundär (an ein phlv. *mata/, wie von
10817:149. n{i)v{i)hlnltan 'kund tun, vd. 17 (26) u. ö. (nach
=== HUB ===
1869:gund (in Kunigunde etc.) aus pers. "^gund.
2923:805. Arm. gund 'Abtheilung eines Heeres, Corps, Schar'
2925:junud^ ajndd 'Soldaten*, syr. guddd *Schar', mand. gunda
2926:(N5ldeke, Mand. Gr. 78), phi. gund weisen in ihrer
2929:stellern des 7. Jhd., wahrend gund (mit g) im 5. Jhd.
3120:868. Np. kund *stumpf = bal. kunt *stumpf, grob, einfaltig*
3122:kund Vir strenuus* zu trennen, vgl. kunda^ kundavar,
3345:936. Dazu arm. LW. gund 'Kugel', gndak *Kugel, Ball,
4565:nur in yetkar 'Brief, Urkunde ™ np. yadgar *Erinnerungs-
5706:wahrend sich m- vor n (vgl. phi. v(i)nas = np. gundh) noch
5713:gefunden, da das aus pers. gundh entstandene arab. jfunah
5725:Umschreibungen des Pehlevi sind (vgl. vanas- neben gundh)
6827:Phi. zu pat- werden musste (§ 3), wodurch t sekundftr vor
7058:arm. murhak 'Urkunde' (5. Jhd.), skr. mudra- *Siegelring,
7504:246, ap. ^nikad^a- ; agah *kundig = paz. agah Min. Gl. 29,
7530:gundh ^), arab. jun^ (Koran), phi. v(i)ndd^, 1st arm. vnas
8026:Verstand*?; kunjid, kunjld 'Sesam*, hsA, kundld^ (Dames
8504:nigah 'Anblick', phi. nikas Gl. and Ind. 246; agdh 'kundig',
8811:stank', zd. gainti-; gandum 'Weizen, skr. godhuma-; gunda
8812:'Hefenballen', zd. gunda-; gos 'Ohr ^= ap. gausa-; gun
```


## [2026-09-06T21:53:54.619Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN 7540-7560 ===\"; sed -n '7540,7562p' HRN.txt\necho \"=== HRN 7025,7040 ===\"; sed -n '7022,7042p' HRN.txt\necho \"=== HUB 3110,3135 ===\"; sed -n '3108,3135p' HUB.txt\necho \"=== HUB 2918,2935 ===\"; sed -n '2918,2935p' HUB.txt"
}
```


### [2026-09-06T21:53:54.695Z] TOOL RESULT

```
=== HRN 7540-7560 ===
867. (2)kemer 'Höhe, Berg* etc. (IDD Is. 2, 10).
aw. kamere^a- 'Kopf*; phlv. kamal (wie Bartho-
lomae zu lesen vorschlägt, der kamer eda- als aus
Vermischung der Wörter ai. kakühh-, kakud-, skr.
kapdla-^ lat. caput und ai. mürdhän- entstanden an-
sieht).
kenär s. keran (No. 846).
868. kund 'stumpf; tapfer*.
skr. (bezw. präkr.) kunfha- 'stumpf.
Vergl. Rückert, ZDMG. 8, 280.
np. ktmdaver hat nach Nöldeke (mündliche Mit-
teilung) im Öähnäme immer die Bedeutung 'stolz'.
»J Nöldeke, Pars. Studien II, 40.
U r n , QrundriHB d. noup. Ktyniolog-ie. ] 3- 194 —
869. kenden graben', Praes. ken-em,
ap. aw. \/kan- graben'; phlv. kantan (Bund.), kandau
(AV., PPGl.), paz. /andan; ai. l/khan-, khdnati.
kurd. kendn; af/. kandal; oss. t. vergl. nijgänin
'begraben' (Urform "^Mnin^ 203); arm. vergl. akan
diOQvy/iia (H. No. 3).
Auf die mit kh anlautende Form der Wurzel gehen
np. (arab.) yendeq Graben , phlv. xantak, np. /öw«j, /an
'Haus' (No. 405) und /am 'Quelle' (No. 466) zurück;
=== HRN 7025,7040 ===
sevük,
af/. /vai 'schlüpfrig, glatt'.
Hübschmann, KZ. 27, 107 Note, gleichzeitig
Darinesteter, Et. ir. I, 85.
S.
seil s. sed (No. 725).
r.
805. yund, yunde Schaar, Menge; versammelt' (Belege in
SF und FJ, letzterer aus Daqiql).
phlv. gund 'Heer ; arm. L\V. gu7id 'Heer, arab.
LW. jiind 'Heer*; kurd. LW. grmd , jund 'Dorf (H.-
Sch).
skr. vptdä' 'Schaar, Truppe, Heer (Nöldeke, münd-
liche Mitteilung).
Die Stadt Crunde-Säpür {^Vandev-Sapür gehört nicht
hierher, vergl. Nöldeke, TabarT-Ubersetzung S. 42
Anm.
F.
806. fer^fere 'Kleie'.
Nöldeke (mündliche Mitteilung) vergleicht lat.
fiirfur 'Kleie, Gemeng*, das zu gr. Tjooffvofo 'sich un-
=== HUB 3110,3135 ===
zd. taxma--, tc^yah-, tandista^. Also Horn's *kamnyao
eine wuste Bildung! Vgl. Fr. Muller, WZKM.
7, 368.
867. Das Verhaitniss von np. kamar 'altitude, collis, tumu-
lus, saxum* = afgh. LW. kamar 'the middle of a moun-
tain, precipice, cliff, the high bank of a river' zu zd.
kamereda" 'Kopf der Devas u. s. w. = phi. kamdr^)
ys. 56, 12, 4 (Sp.) sowie zu arm. kamar '6ew5lbe,
Bogen, Kuppel, Halle* = gr. Kajudga (xa^idgtj schon
bei Hero dot) *Gewolbe' = lat. camera, np. LW.
kamra 'Gewolbe, Stalf (N 6 1 d e k e , Pers. Stud. H, p. 40)
ist mir unklar.
868. Np. kund *stumpf = bal. kunt *stumpf, grob, einfaltig*
(Geiger) = skr. (prakr.) kunthar- 'stumpf. Davon
kund Vir strenuus* zu trennen, vgl. kunda^ kundavar,
869. Horn bemerkt mit Recht, dass auf paz. xandan
(= kandan) nichts zu geben ist. Das angefiihrte
phi. xantak (wo vorkommend?) kann nur das falsch
ins Pehlevi umschriebene arab. pers. xandaq = arm.
xandak (bei Steph. Asol. und Spateren!) sein, dessen
regulare np. Form kanda^) ist. Afgh. kanql (im Praes.
')>Kdnnte, obwohl nicht mit I geschrieben, doch (naoh Bartho-
1 m ae) katnal gelesen werden und entsprSche dann einem ap. ^kamarda-
= zd. ^hamareSa-,
') Die Nebenform xati' zu Jean 'graben' stUtzt sich im Iranischen
eigentlich nur auf dieses arabisch-pers. xandaq, da die etym. Erkl&rungen
von xana^ xd,n und xanl (Nr. 465, 466) doch nicht als durchaua sic her
gelten konnen.- 89 -
=== HUB 2918,2935 ===
cheval alezan* Justi-Jaba Diet.
803. Zd. xsa^rya- ist im Neup. durch sahn vertreten.
Also Ser 'L5we' davon zu trennen.
804. Phi. SSpOk (Jasna 61, 11) = ap.*ariaipa- oder *xsvaipa-?
Vgl. oben Nr. 800.
805. Arm. gund 'Abtheilung eines Heeres, Corps, Schar'
(bei den S^ltesten Schriftstellern) = arab. /wwd, pi.
junud^ ajndd 'Soldaten*, syr. guddd *Schar', mand. gunda
(N5ldeke, Mand. Gr. 78), phi. gund weisen in ihrer
Uebereinstimmung auf urspr. anl. g, nicht v, Im
Armen. findet sich g = pers. g aus v erst bei Schrift-
stellern des 7. Jhd., wahrend gund (mit g) im 5. Jhd.
belegt und vor diesem entlehnt ist. Daher Zusammen-
hang mit skr. vpida- oder zd. vq^toa- unwahrsehein-
lich.
806. Die Zusammenstellung widerspricht alien Lautgesetzen.
808. Lies ap. Vindafamd (im Nominativ, Thema Vinda-
famah-), Np. farrux gliicklich' = phi. farraxv setze
```


## [2026-09-06T21:54:07.661Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FSF گندآور ===\"; grep -n 'گندآور\\|گند آور\\|کنداور\\|گنداور' FSF_pages.txt FSF.txt 2>/dev/null | head -10\necho \"=== MON کنداور ===\"; grep -n 'کنداور\\|گنداور\\|گندآور' MON_part1.txt MON_part2.txt | head -10\necho \"=== BQT کنداور ===\"; grep -n 'کنداور\\|گنداور\\|گندآور' BQT_v2_pages.txt BQT_v1_pages.txt incoming/BQT/BQT_v3_pages.txt incoming/BQT/BQT_v4_pages.txt 2>/dev/null | head -10"
}
```


### [2026-09-06T21:54:07.747Z] TOOL RESULT

```
=== FSF گندآور ===
FSF.txt:9701:برفتند زان روی کنداوران 
FSF.txt:25539:سپهدار پرکین و کنداوری 
FSF.txt:28214:بزرگان هر شهر و کنداوران 
FSF_pages.txt:7112:     ‫‪(-۲‬اسم فاعل از پروردن)‪ :‬پرورنده‪:‬‬                            ‫برفتند زان روی کنداوران‬
=== MON کنداور ===
MON_part2.txt:26976:کندا؛ 8 (قس. کند» کندا گر کنداور] 
MON_part2.txt:26988:کنداور: ۲02۵82۲ (ص‌فا.) شجاع» دلسر» 
MON_part2.txt:26992:«کنداور» , کند آور»»۱ گنداور, و رگند آور» 
MON_part2.txt:27015:فیلسوف می‌دهند و در این صورت کنداور 
MON_part2.txt:27020:رکنداور» با کاف تازی (- د کندا + ور]به ‏ 
MON_part2.txt:27026:مع‌هذا « کنداوری» را مسامحه به معنی 3 ۱ 
=== BQT کنداور ===
incoming/BQT/BQT_v3_pages.txt:36567:‎By ۸‏ : کنداکر کنداور . درین صورت «کندا » بمعنی شجاعت و دلیری است مر کب‌از:
```


## [2026-09-06T21:54:09.932Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '26965,27035p' MON_part2.txt"
}
```


### [2026-09-06T21:54:09.984Z] TOOL RESULT

```
قرار داشتن ضربه‌های میزان‌ها در یک قطعه 

طولانی و ممتد؛ مق. تند. (نق. مینیاء) خط 

کلفت» قلم گیری کلفت؛ مق. تنك. 

کندا؛ 3 (ص. 1.) جادوگر ساحرء» عالم 

به احکام نجوم» کاهن. فیلسوف» حکیم. 

کندا؛ 8 (قس. کند» کندا گر کنداور] 

(.) شجاعت. دلیری. 

کنداگر: ۲-۲ [معر .] (اص.) شجاع» دلیر. 

کندامویه: ()«۳« (امر.) مویی که 

چون کودک زاده شود در بدن او باشدء 

موی مادرزاد. 

کنداور: ۲02۵82۲ (ص‌فا.) شجاع» دلسر» 


بهلوان. . ضصح. این لغت در کتب بصورت 
«کنداور» , کند آور»»۱ گنداور, و رگند آور» 
ضبط شده و آن را به معانی شجاع و دلیر و 
پهلوان سپهسالار و سردار» منجم و حکیم 
آورده‌اند. نولدکه و هرن و هویشمان (اسشق 
- هوشمان ۸۲۷ آن را با کاف تازی از 
رشه «کند» به معنی شجاع گرفته‌اند. ولف 
نیز در فهرست شاهنامه رکند آور» و 
« کند آوری» را با کاف تازی آورده اشت: 
بنابرین کند آور باید مرکب از: کندا 
(شجاعت) + ور (سوند اتصاف) باشد» نه 
از: کند (شجاع) + آور (آورنده)» چه 
بآور» در کلمات مرکب از اسم آید. در 
لغت‌نامهٌ دهخدا در کلمةه «آور» آمده: کلمةُ 
کند آور) چون گفته‌های فر هنگ‌نویسان در 
عربی یا فارسی و مضموم یا مفتوح بودن 
کاف مضطرب است» معنی مجموع مرکب 
آن ظاهر نیست» چه گاهی جزء اول کلمه را 
«کندام گر فته‌اند و گاهی «گند, اصل کلمة 
جند عرب دانسته‌اند و از اين‌رو «کند آور را 
حکیم فیلسوف معنی کر ده‌اند و گٌندآور را 
معنی قاثد و سپهسالار داده‌اند. معنی فیلسوف 
برای کند آور درست نمی‌نماید» چه خود 
«کنداء را فرهنگ‌نویسان» معنی حکیم و 
فیلسوف می‌دهند و در این صورت کنداور 
معنی معقولی ندارد و اگر کلمةٌ «گند آور» 
مرکب از کند به معنی جند باشد» معانی 
شجاع و دلیر در آن هی ۳ 
از مجموع اين مباحث چنین نتیجه می‌گيريم: 
رکنداور» با کاف تازی (- د کندا + ور]به ‏ 
معنی شسجاع و دلیر لفةٌ صحیح است. ۱ 
رگند آور» با کاف پارسی [ - کند ( جند) + 3 
آور(نده)] سه معنی لشکر آراه سه‌آرا: ۲ 
سیهسالا ر هم درست است. به معنی منجم و 3 
حکیم فا خداه صحیح است ته وکندآون 13 
مع‌هذا « کنداوری» را مسامحه به معنی 3 ۱ 


کندذهن 


فرهنکگ فارسی معین 


۰۳
```


## [2026-09-06T21:54:24.139Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n '^کند' MON_part2.txt | head -30\necho \"---\"; grep -n 'کند؛' MON_part2.txt | head -20"
}
```


### [2026-09-06T21:54:24.202Z] TOOL RESULT

```
547:کند؛ علت غائی ( کشاف اصطلاحات, لذ.) 
640:کند؛ غین الیسیر. 
1427:کند» آنجه کبر و نخوت آورد. 
1742:کند (مقصود از قوهٌ منفعله رطوبت و مقصود 
2012:کندرین در آن حل شده است؛ بافت 
4157:کند؛ مق. کت عربت. 
6516:کند. فر مانداری نظامی:حکو مت نظام یکه در 
6727:کند؟ متححد د. 
9865:کند» سط‌پذیر؛ مق. قابل انقباض. قابل 
9877:کند؛ انعکاس پذیر. قابل انقباض: آنچه که 
9892:کند؛ تبدیل پذیر. قابل تجز یه: آنچه که بتوان 
10324:کند. میانه‌رو. کسی که نامه یا پیغام بجایی 
10455:کند. نوعی آهن است که از آن تیغ‌های 
10568:کند. (۱.) آب باران را کد در یک محل. 
10923:کند؛ مقنن. 
11101:کندن قبا. (مصل.) آماده شدن» مهیا شدن. 
12003:کند؛ مق. قرار منع تعقیب. فرار منع تعقیب: 
12581:کند. 
12832:کند و فروشد؛ گوشت‌فروش. 
13584:کند. 
13867:کند علامت تغییر دهنده در بالا و بایین قلاب 
15748:کند. قول جارم: (منط.) قضیه‌ای که مفید 
16868:کندن لباس و لخت شدن و آماده گردیدن 
17265:کند. از (ز) کار مانده: از کار افتاده. از (ز) 
17303:کندن و شخم زدن و گل مالی و نظایر. 
17910:کند؛ مور کاری (سخن؛ دارو» ضرت 
18724:کند؛ خشککن. کاغذ هوایی: کاغذ اطفال. 
20218:کند. کبوتر حرم: کبوتری که در اطراف 
25186:کندن: (عم.) آن را به پایان رسانیدن. 
25437:کند (غم.)؛ سرهنگ. 
---
400:علی(ع) با یکی از ایمه غلو کند؛ ج. غلات 
547:کند؛ علت غائی ( کشاف اصطلاحات, لذ.) 
640:کند؛ غین الیسیر. 
801:می‌کند؛ دد زیرفکی. غده‌های تناسلی: 
1283:آب عمیق که شخص را غرق کند؛ گودالی 
1525:مسافران و بینوایان را نوازش کند؛ 
2329:شود و آب باران در آن نفوذ نکند؛ غلتان. 
2721:ك_ آنکه تولید غم کند؛ غمآور. . (۱.) 
2749:وی بهترین کود را برای زراعت تهیه می‌کند؛ 
2844:که حکایت از اندوه کند؛ مراسلة غم‌انگیز. 
4075:آنجه از حد تحاوز کند؛ زباده از حد؛ سبار؛ 
4157:کند؛ مق. کت عربت. 
4239:شوهردار دوستی و هم‌صحبتی کند؛ ج. 
6181:جانوري که در اب زیست کند؛ حبوان ابی. 
7519:کسان را فصد کند؛ رگزن. 
7696:حمایت و تعهد کند؛ فاضل پرور. 
7824:زمان ( گذشته حال يا آینده) کند؛ ج. افعال. 
7864:نفی ببان کند؛ مق. فعل مفست. فعل وصفی: 
9208:می‌کند؛ دستگاه ضبط صوت. 
9473:آن با یکدیگر بحث کند؛ علم وظایف
```


## [2026-09-06T21:54:27.918Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '26905,26968p' MON_part2.txt"
}
```


### [2026-09-06T21:54:27.970Z] TOOL RESULT

```
و اه (عم.) تکه کومت 
کوچکی که بر سیخ کشند با قیمه کنند دکنات 
کنجه: کنجه‌پی. 

کنچه: 0 [- کنج] (ص.) خری که 
زير دهانش ورم کرده باشد. خر دم بر ید ه. 


کنحه 


.۱ فرهنگ فارسی معین 


کنجه: (۲00[:0-0 (.) نوعی شیرینی طرز 

تهیه: خمیر گوش‌فیل را نازک و لوز کنند و 

در میان لوز مغز قطاب کرده لوز دیگر در 

لای آن نهند و چهار گوشه‌اش را فشار دهند 

یا مثل بقچه چهار گوشه را بهم فشار داده 

میانش را خالی گذارند و پس از سرخ شدن 

قند باشند. 

کنخت: ۲۵:۵0 (.) جوهر (تیغ» شمشیر). 

بی کنخت: بی جوهر. 

کند: ۵«ها (.) جراحت» ریش. 

کند؛ 2۵ [- کنت > قند» معر. کندن] 

(پس.) محل و موضع و قریه و شهر و آن 

بصورت سوند در اسامی امکنةٌ ماوراءالنهر 

دیده می‌شود: اوزکند. (- کنده] (ص‌مف.) در 

ترکیبات به معنی «کنده آید. 

کند: ۱۸۸4 (.) گریز. 

9 ۵ (شجاع» خشن] (ص.) دلیر؛ 

دلاور» شجاع. 

کند: ۲0۰۵ [- کنده] (ا.) کنده‌ای که بر بای 

مجرمان و گریز پایان نهند. 

کك: : 1070 (ص.) کسی با چیزی که آهسته و 
آرام حرکت کند؛ بطیْ) مق. تیغ 

و شمشیر و چاقو و کاردی که دم آن تن 

نباشد و به سختی برد؟ مق. تنده تیز. (هس.) 

قرار داشتن ضربه‌های میزان‌ها در یک قطعه 

طولانی و ممتد؛ مق. تند. (نق. مینیاء) خط
```


## [2026-09-06T21:54:39.750Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== ARY کنج/کند ===\"; grep -n 'کنج\\b\\|کنج ‪\\|^کنج\\|کند ' incoming/ARY/ARY_pages.txt | head -15\necho \"=== ARY latin index ===\"; grep -n -i 'KONJ\\|KOND\\|KUNJ\\|KUND' incoming/ARY/ARY_latin_index_pages.txt | head -15\necho \"=== BQT کنج ===\"; grep -n 'کنج ‪\\|کنج »' incoming/BQT/BQT_v3_pages.txt | head -10"
}
```


### [2026-09-06T21:54:39.827Z] TOOL RESULT

```
=== ARY کنج/کند ===
121:حاشیه‌ی سرزمین‌های هند و اروپایی را محقق می‌کند و پعید است که جنبش کوچگری هند و
997:می‌کند که زنده بودن و نوکری کردن را به سلطنت در جهان مردگان ترجیح می‌دهد.
1028:در میان اعیانگال رواج داشت و اگر شوهر به طرز سرا رآمیزی می‌مرد» زن‌های او مورد شکنجه قرار
1265:زین هم پژوهشگران آینه بناندکاری راک این کتاب آغازکرده است دابا لکند و جایگاه استین
1367:7 و آلمانی 83[ کنجکاری‌انگیز است. ۳
1975:1 ۲- 8168۸7 ,0217088 این واژه را فقط تا ریشه‌ی لاتین پیگیری می‌کند ‏ دا اش برع ورد
4106:0) ذکری از واژه‌های رُرمنی این فهرست نمی‌کند و آنها را وابسته به واجریشه‌ی ۹۱۷۳۲ می‌داند (صفحه‌ی
6430:چم این واژه در زیان لیترانی: گوشه کنج.
10293:هند و اروپایی 8781۰ را نامسجّل می‌کند و بهمین دلیل در جلو واجریشه‌ی مندارلاییای (شاید) آورده‌ام.
15375:۱ 081۸31۸88 واژه‌ی "وبز" را بعنوان یک واژه‌ی فارسی ذکر می‌کند ولی من این واژه را در هیچ‌کدام از ا
=== ARY latin index ===
1575:-KUND — (OLD ENGLISH) ep JS AZATAZAD APAHLAVD) 5 ay
1582:POKORNY, SS*~*~*~*«TSTS -KUNDS AGOTHIC) S38
1584:‘MACKENZIE: (FREE) 115 KUNDR
6442:SKUDROS, SKAUDRUS CODAYATI, SKUNDATE.
=== BQT کنج ===
36317:‏سراج ‎gull‏ راجی « رشیدی » « لاحدب , کنج » « مهذب الاسماء » .
43747:‎(a) ‏مسحف «ک رکنج » («.م.) < ک رکانج‎ . Bas
48605:‎EO ۹40 gel?‏ کنج » زاوبه - خلوت . خلوتگاه ‎Se‏ کناره = دستهٌآوند - دکمه, کره.
```


## [2026-09-06T21:54:45.706Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== ARY 6415-6440 ===\"; sed -n '6415,6440p' incoming/ARY/ARY_pages.txt\necho \"=== BQT v3 48595-48615 ===\"; sed -n '48595,48620p' incoming/BQT/BQT_v3_pages.txt"
}
```


### [2026-09-06T21:54:45.767Z] TOOL RESULT

```
=== ARY 6415-6440 ===
پارسی باستان (۶8۶1۸۷ 012): 2117۸185 لینوانی (01۵/4هتاب7لا). 1۸5
کردی (0[57نام): وا
افغانی (پشتو)(4۳0/۸01): تن پسگشت‌ها ۸87۵۵۵5
سانسکریت (54(/588/7): مهل۲۸2۸ بطق مهد
برنانی (072810): و۱۱ 41 (۲013 ,#5تا78ا))
لانین (00ا7مل): 5 48 (0.3۳7) امین دا
گونیک (ع007771): دا برهان قاطع ‏ ۶۱
انگلیسی کهن (5ا20 صاه): ق۲] ,1307 فرهنگ معین : ۱۳۷۱
روسی (ا55ا): 1۸ لغت‌نامه دهخدا: ۸۵
هه
[pdf page 218]
چراء چریدن» چراندن / ۲۱۹
یادداشت:
۱ هیچیک از پسگشت‌های فارسی ریشه‌ی اين واژه را نمی‌دهند.
۲ چم این واژه در زبان سانکریت؛ انخنا, ۰
چم این واژه در زیان لیترانی: گوشه کنج.
چم این واژه در زبان لاتین: دشت,
چم این واژه در زبان پونانی؛ کج کردن؛ دارای انحناکردن.
۳ واژه‌های انگلیسی 2۸8/0 و آلمانی ۸۱188 از همین واجريشه آمده‌اند.
اوستایی (/4557:40): -13۸3 ,07۸۸71
پارسی باستان ((۵ا۶58۵ 0ا :)0‏ مهف پسگشت‌ها کطالق عم
پهلوی (امنتنمم: #هاتفتل تفای 1 1
کر دی (8/01517): :5ل2 لاک ۱۸۸
مات ,ا01اتمتکاتن 6 (116,)۳۸8782 (10تفقی)
اففانی (پشتر) (۸707۸۷1): 3 ۰ ناه
سانسکریت (58/7/(ه5): 7 (7۲ف68۸ ,۲۸8۶7۸۰)
=== BQT v3 48595-48615 ===
‏دوم همریشه وبععنی گردیدن وگرداندن‌است. لفة بمعنیس کین گردان(ه.م.) ورك ‎US FF‏
ورك : ح٩‏ ص۱۸۲ ۷ ک کار ‎pa)‏ ۸ - دراوراق مالوی‌بپپلوی ۳۵
«کو گرد . -ولفور» ,1 ‎(Henning, A list of Middle Persian..., 3505, XI,‏
‎p ۰3‏ )ک وکرد ‎Soufte)‏ فر) جنمی است بیط و جامد » برنگه زرد لیموبی » بی‌مزه وبی
بو . وزن‌مخضصوص‌آن ۵ است ودره ۱۱۶ درجه ذوب میشود ودر 440/۵ درجه بجوش‌میآید.
ک و کرد در طبیعت بوفور بصورت سولفورها با سولفانها , با صورت ‎gel‏ خویش درحوالی کوههای
آتشفشان یافت میشود .

‏» گوشه - بضم اول و کر سوم ( در لهجهٌ مرکزی ) و بقتح ‎OT‏ ( در تلفظ قدیم ) 4
اوستا - ‎ogaoshaka‏ . کردی 802 , 805۲6 . بلوچی ¢ 805۳086 ‎ys.‏ 805126
‎EO ۹40 gel?‏ کنج » زاوبه - خلوت . خلوتگاه ‎Se‏ کناره = دستهٌآوند - دکمه, کره.
[pdf page 657]
My

ممدیی است وآن بشاری باشد دخالی که بعضی
ازآن درزیر زمین منجمد میشود وبعضی ازفرجها
و تراکهای کوه برمیآبد و در ‎WIM‏ برروی
‎e‏ می‌لشیند وک وکرد میشود , و گرداحمر
از جواهر است ومعدن‌آن دروادی موران میباشد
و موران آنجا مقابل بزی ميشوند. گوبشد درشب
مالند آتش میدرخشد چنانکه روشنابی آن چند
فرسخ میرود » وچون از ممدن بیرون آورنداین
خاصیت ندارد وآن جزواعظم ا کسیر است‌چنانکه
سیماب را ابوالارواح خوانند و ‎LT‏ ابوالاجاد
نامند . گرم و خشك است در چهارم و اقعام ‎OT‏
‏منافع بسپار دارد (۱).
```


## [2026-09-06T21:54:54.509Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v4 کنج ===\"; grep -n '‏کنج\\|کنج ‪۴\\|کنج ‪»\\|کنج «' incoming/BQT/BQT_v4_pages.txt | head -10\necho \"=== BQT v4 lines with کنج ===\"; grep -c 'کنج' incoming/BQT/BQT_v4_pages.txt\ngrep -n 'کنج' incoming/BQT/BQT_v4_pages.txt | head -20"
}
```


### [2026-09-06T21:54:54.581Z] TOOL RESULT

```
=== BQT v4 کنج ===
=== BQT v4 lines with کنج ===
151
293:حن فکرده‌ایم‌و کليةٌ توضیحاتوتعلیقات راور جلد پنجمکنجا نيده‌ايم -
753:و شکنج راکوبند ‎٩‏ - وشکاف و تراك دیوار را | و دال به تحتانی رسیده و بسین بی نقطه ساکن
758:بخش عدو از کنج و فسمت تو تا کنج بود , مار باد و ملره.
1135:و رل :کنجینة کنجوی ص ۱۳۹ ۰
1498:آمد و چون نهاوند كوچك بود وکنجایش سپاه | ازآن دختر بهم رسید 9 .
2051:نظامی کنجوی «کنجینه مس ۰۹۱۶۱
2053:« نظامی کنجوی . مغزن‌آلاسرار . چاپ ارمغان ص ۰*۱۲
2055:نظامی کنجوی « کنجینه س ۶۱۸۱ -
2471:کنجعك راکوبند و بعربی عصفور خوانند. ملحق شده ‎٩‏ - و درعربی جوهرست سرخ *۱.
2681:بمرد وجمان مرده ری ماند از او شد آن کنج با شاهی و رنگه و بو.
2729:8 - (عر ) « مرز » شکنجیدن بالگشتان نرم لرم بی‌کزند ... و عیب 40 کردن - و
2820:سابقه سالار جهان قدم مرسله پیوندکلوی قلم. نظامی کنجوی در حمدخدا
2847:نظامی کنجوی « کنجینةٌ کنجوی ص ۱۶۲ *.
2875:مرش با « بسکون میم ببعتی مرغ | بزبان کنجشك وآبرا بزبان عریی شان‌السافیر
2957:نظامی کنجوی «کنجینه ص۱۶۳ >.
3041:کنجوی‌س ۰۹۱۸۳ ۷ - از ابلیی ( عیطان )ی ( نبت ) .
3250:۴ -ظ . بمعنی اختلاط و امتزاج عناصراست . نظامی کنجوی ممال‌مزاج راآورده :
3252:کنجینه صس ۱۶۳ *.
3286:مژدقان . ۴ - از: مزد۳-ور ( پوند اتصاف ودارندکی) < بر ( بردن ) [ قی: کنجور,
3870:که نظامی کنجوی درخرو وشیرین برای الحان باربدیآورده , لخن‌دهم است :
```


## [2026-09-06T21:55:02.998Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SKT hunch ===\"; grep -n -i 'hunch' SKT.txt | head -5\necho \"=== FSD hunch ===\"; grep -n -i 'hunch,' FSD_vol2.txt FSD_vol3.txt | head -5\necho \"=== WEB hunch ===\"; grep -n -i 'hunch, n\\|hunch,' WEB_vol1.txt | head -5\necho \"=== DEV galanga full ===\"; sed -n '1370,1395p' DEV.txt"
}
```


### [2026-09-06T21:55:03.108Z] TOOL RESULT

```
=== SKT hunch ===
8968:HUNCH.
8969:Hunch,  a  hump,  roand  mass.  fB.)  A ao-uliKcl  form  oi  kook,  q.  v.  Cf.  G  Mmke, the  bent  back,  h<kktr,  a  hunch  on  the back.  And  cf.  Skt.  kui^k^  to  bend,  vith kuch,  to  l-end.
=== FSD hunch ===
FSD_vol2.txt:49518:1910).  An  English  astronomer;  “the  father  of  modern  as-  buinp;  hunch,
FSD_vol2.txt:49927:.   H.RouTLEDOBioputariij.,i.8ciertcap.3...lK.i:s,issi.  Hum'phrey,  1   hwm'fn;  2   httm'fry,  «.  1.  A   masculine  per- hunch,  1   hondh;  8   httneh,  ».  I.i.  lo  To  thrust  with  the 4.  rcolloq  ]   .4ny  chrome  cutaneous  eruption  supposed  sonal  name  JJ-  Mm'‘rlt;  P.  elbow,  shoulder,  or  fiat;  push  suddenly;  jostle;  jog;
=== WEB hunch ===
92881:hunch, v.i. to move forward jerkily; push;
92895:hunch, n. [form of hump.]
92899:hunch, 2.t.; hunched (huncht), pt., pp.; hunch- ing, ppr. to draw (one's body, etc.) into the shape of a hump; form into a hump; as, don’t hunch your back so.
=== DEV galanga full ===
G
Gabelle.  Esp.  alcahala,  alcavala,  ffahela,  portug.  alca- rala ,  gabella ,  il  al.  gahella.  Les  mots  alcahala,  alcavala,  si- gnifiant impôt,  ^^/ire.  viennent  certainement  de  l'arabe  iiiLoUî al-qahâla,  qui  a  été  employé  dans  le  même  sens  (de  la  ra- cine Jajj  qahal,  recevoir,  prendre).  Mais  Diez  conteste  que la  même  étymologie  convienne  à  gabela,  gahella,  gabelle, qu'il  veut  tirer  de  l'anglo-saxon  gafid,  gofol.  La  seule raison  qu'on  donne  pour  rejeter  l'étymologie  arabe,  c'est que  le  ^  </  ne  deviendrait  jamais  g  dans  les  langues  ro- manes. M.  Dozy^  fait  remarquer  avec  raison  que  l'italien écrit  aussi  cahalla,  cahella  (la  permutation  entre  c  et ^- n'est pas  rare  en  cette  langue).  D'ailleurs  on  a  plusieurs exemples  de  ^  ^  devenant  ^  (p.  ex.  algodon,  coton,  de ^J^fjoton^,  et  de  toute  façon  rien  ne  s'oppose  à  l'identifi- cation de  tous  ces  termes  avec  le  terme  arabe.
Gâche.  Personne  n'a  songé  à  comparer  ce  mot  à  l'espa- gnol alguaza,  penture,  gond,  pas  même  M.  Dozy  en  éta- blissant l'origine  arabe  du  terme  aragonais^.  Cette  origine même  tend  à  confirmer  l'identité  des  deux  termes;  car
l'arabe  iJyJî  ar-razza  signifie  à  la  fois  gond  et  gâche.  (Voy. plus  loin  au  mot  Mortaise.)
Galanga.  Esp.  et  portug.  galanga,  anc.  franc,  galangal , garlngal,  angl.  galangale.  Le  nom  de  cette  plante,  origi- naire  des  Indes,  nous  est  venu  par  l'arabe  (jUxLjw  kha-
'   Gloss.  p.  75.
-  Gloss.  p.  i3i.  «Les  Aragonais,  dit  M.  Dozy,  doivent  Tavoir  reçu  do personnes  qui  ne  pouvaient  pas  prononcer  le  r,  et  qui,  par  conséquent, étaient  aussi  obligées  dans  cette  circonstance  de  ne  pas  assimiler  la  consonne de  l'article  à  la  première  consonne  du  substantif. '7
124  DICTIONNAIRE  ÉTYMOLOGIQUE
landjân.  On  la  nomme  aussi  langas,  lanquas,  qui  est  le  ma- lais (j^îjXjtî  langkoiias.  L'ancienne  forme  vulgaire  est  ga- langue:  ç^La  pulpe  d'artichaud ,  cuicte  en  bouillon  de  chair, mangée  avec  sel,  poyvrc  et  galangue  en  poudre,  sert  à l'acte  vénérien.  J7  ÇAgrkult.  et  maison  rustique,  de  Jean  Lie- bault,  liv.  II,  cil.  XIV,  p.  200.)
Gamache.  Mot  vieilli  qui  signifiait  guêtres,  et  que  Diez lire  de  gamba.  (Littré.)  La  vraie  étymologie,  je  crois  pou- voir l'affirmer,  est  le  nom  d'une  ville  africaine,  j^^ÎJsi Gadamès  (dans  l'Etat  de  Tripoli),  célèbre  par  ses  cuirs c^ moelleux  comme  une  étoffe  de  soie??,  dit  un  auteur arabe  ^  Dans  le  Quercy,  le  Rouergue  et  sans  doute  en plusieurs  autres  parties  de  la  France  méridionale ,  on  ap- pelle encore  garamaches  (^gorromatzos)  les  grandes  guêtres ou  jambières  de  cuir  des  cavaliers  et  les  grosses  bottes  à l'écuyère.  Le  mot  nous  est  sans  doute  venu  par  l'espagnol guaclamaci,  portug.  guadamecim,  qui  désignait  autrefois une  espèce  de  cuir  fabriqué  d'abord  à  Gadamès  et  plus tard  en  Espagne  même  -.
Gambir.  Substance  astringente,  analogue  au  cacbou,  que les  Malais  mâchent  avec  le  bétel ^  et  que  l'industrie  eu- ropéenne emploie  pour  la  tannerie.  On  écrit  quelquefois gambier,  à  la  façon  hollandaise.  C'est  le  malais  yf^gambir, nom  d'un  arbre  de  l'archipel  Indien,  le  Nauclea gambir  des naturalistes,  dont  les  feuilles  fournissent  cette  substance par  décoction  ^.  Celle-ci  est  nommée  par  les  Malais  j.js>X  XjÏ^ gketah- gambir,  gomme  de  gambir,  du  mot  ax^  ghetah  ou gatah,  gomme,  baume.
'   Voy.  Dozy,  Gloss.  p.  ;i8u. ''  Ibid.
'   Dans  son  Ilerbanum  Amboinemo,  fe  bolanislo  Uunipi"  cite  l'arbre  /;«m- hirlaiit,  qui  esl  le  malais  c:>ji)  y^y gambir  lâout,  jjainbir  do  luex .
^
DES  MOTS  D'ORIGINE  ORIENTALE.  li>5
Ga>dasuli.  Plante  des  Indes  orientales  cullivée  dans nos  serres  ponr  ses  Heurs  et  son  parfum.  Du  malais  J^Jo;^ gandasofdi.  On  peut  voir  ce  que  dit  Tabbë  Favre  ^  de  l'ori- gine de  ce  nom,  dont  la  première  partie  paraît  être  le sanscrit ^^7//r/^,  odeur.
Gandole.  Plante  des  Indes  orientales  qu'on  mange  a la  façon  des  épinards  (^gandola,  àe  Rumpf).  Du  malais J^  Jsj;K  gandola  ou  goumlola.
Garbin.  Vent  du  sud-ouest,  liai,  garbino.  De  l'arabe j-ft  gharhl,  occidental,  adjectif  dérivé  de  lj^  gharh, coucbant,  occident,  mot  d'où  vient  aussi  le  nom  du  Ma- greh,  en  arabe,  Vr*^  maghreh  ou  maghrib,  occident, Afrique  occidentale,  et  notre  terme  maugrehin,  habitant  du Magrch,  Maure.
Gaupe.   Est-ce  l'arabe  iC/^  qahha,  vieille  femme,  cour- tisane, qu'on  tire  de  l^^  qahab,  tousser,  par  allusion  au loussement  dont  les  courtisanes  se  servent  pour  attirer  les chalands?  Les  dictionnaires  persans  et  turcs  donnent  aussi , iuk,  x^ï,  qahpè,  qahpè,  dans  le  même  sens;  et  Richard- j|  son ,  AiLaw  »skÂ  qahbè-khaneh ^  ^^  a  brothel  ??  ;  qahba  est  actuel- •  lement  le  terme  usité  en  Algérie.  Le  patois  napolitain  ap- i  pelle  giiappa  une  femme  hardie,  batailleuse,  matamore. ^  (  Voy.  J\aples  et  les  Napolitains,  par  M.  Marc  Monnier,  dans le  Tour  du  Monde,  IV,  p.  228.)  (iomp.  les  termes  d'argot populaire  gouape,  goiiapeiir.
Gazelle.  Esp.  gaceln,  gacele,  gacel,  autref.  algacel;  por- tug.  gazella,  ital.  gazzeUa.  De  l'arabe  JIji  ghazâl,  même sons.  Buffon  a  donné  le  nom  à^aJgazelle  h  une  espèce  de
'-  Die  t.  mal.-fr.  1.  P',  p.  ZiAu.
U^^^
1^26  DICTIONNAIRE  ÉTYMOLOGIQUE
gazelle,  qui,  selon  Giivier,  ne  diiïère  pas  de  la  gazelle proprement  dite.
Gecko.  Espèce  de  lézard  des  contrées  chaudes.  Valen- tijn  prétend  que  les  Javanais  se  servaient  des  humeurs sécrétées  par  cet  animal  pour  empoisonner  leurs  flèches. En  malais,  (^Si^^  ghëJwcj ,  par  imitation  de  son  cri.  Dans les  mots  terminés  par  un  ^  ^,  cette  finale  se  fait  à  peine sentir.
Géhenne.  Ce  vocable  biblique  peut  être  cité  comme  un curieux  exemple  de  la  transformation  de  sens  que  peut  su- bir un  mot  par  l'effet  du  temps  et  des  circonstances.  La vallée  d'Hinnom  ou  du  fils  d'Hinnom,  en  hébreu  Qjn"}3  \3 gêi  hen-hinnom,  ou  simplement  gêi  hinnom,  était  un  lieu  de plaisance,  au-dessous  des  murs  de  Jérusalem  :  ç^De  belles fontaines  répandoient  leurs  eaux  dans  tous  les  jardins,  doni la  verdure  et  les  beautés  rendoient  ce  lieu  très-agréable. 11  y  avoit  aussi  beaucoup  d'arbres  fruitiers  et  des  plantes d'une  odeur  merveilleuse  ^  ??  Les  Juifs  s'avisèrent  d'y  bâ(ir un  temple  à  Moloch,  à  qui  ils  sacrifiaient  des  victimes  hu- maines. Le  roi  Josias  ayant  supprimé  ce  culte  sanglant, et  voulant  rendre  cette  place  souillée  désormais  exécrable à  tous  les  Juifs,  y  fit  répandre  toutes  les  immon(fices  de la  ville.  Après  avoir  été  un  but  de  promenade,,  un  lieu  de délices,  la  vallée  d'Hinnom  devint  un  objet  d'horreur,  si bien  qu'à  une  époque  postérieure  géhenne  fut  synonyme d'enfer.  Plus  tard,  ce  ne  fut  que  la  torture.  Et  enfin,  le mot  se  contractant  en  gêne  a  perdu,  de  nos  jours,  presque toute  l'énergie  de  ses  significations  antérieures.
```


## [2026-09-06T21:55:16.060Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nawk '/^ Sanskrit$/,0' 4dc7776ebfb967c9.txt | head -60"
}
```


### [2026-09-06T21:55:17.591Z] TOOL RESULT

```
 Sanskrit
 [ edit ] 

 Alternative forms
 [ edit ] 

 Alternative scripts
 কুণ্ঠ ( Assamese script ) 
 ᬓᬸᬡ᭄ᬞ ( Balinese script ) 
 কুণ্ঠ ( Bengali script ) 
 𑰎𑰲𑰜𑰿𑰙 ( Bhaiksuki script ) 
 𑀓𑀼𑀡𑁆𑀞 ( Brahmi script ) 
 ကုဏ္ဌ ( Burmese script ) 
 કુણ્ઠ ( Gujarati script ) 
 ਕੁਣ੍ਠ ( Gurmukhi script ) 
 𑌕𑍁𑌣𑍍𑌠 ( Grantha script ) 
 ꦏꦸꦟ꧀ꦜ ( Javanese script ) 
 𑂍𑂳𑂝𑂹𑂘 ( Kaithi script ) 
 ಕುಣ್ಠ ( Kannada script ) 
 កុណ្ឋ ( Khmer script ) 
 ກຸຓ຺ຐ ( Lao script ) 
 കുണ്ഠ ( Malayalam script ) 
 ᡬᡠᢏᡱᠠ ( Manchu script ) 
 𑘎𑘳𑘜𑘿𑘙 ( Modi script ) 
 ᢉᠤᢏᢍᠠ᠋ ( Mongolian script ) 
 𑦮𑧔𑦼𑧠𑦹 ( Nandinagari script ) 
 𑐎𑐸𑐞𑑂𑐛 ( Newa script ) 
 କୁଣ୍ଠ ( Odia script ) 
 ꢒꢸꢠ꣄ꢝ ( Saurashtra script ) 
 𑆑𑆶𑆟𑇀𑆜 ( Sharada script ) 
 𑖎𑖲𑖜𑖿𑖙 ( Siddham script ) 
 කුණ‍්ඨ ( Sinhalese script ) 
 𑩜𑩒𑩪 𑪙𑩧 ( Soyombo script ) 
 𑚊𑚰𑚘𑚶𑚕 ( Takri script ) 
 குண்ட² ( Tamil script ) 
 కుణ్ఠ ( Telugu script ) 
 กุณฺฐ ( Thai script ) 
 ཀུ་ཎྛ ( Tibetan script ) 
 𑒏𑒳𑒝𑓂𑒚 ( Tirhuta script ) 
 𑨋𑨃𑨘𑩇𑨕 ( Zanabazar Square script ) 

 Etymology
 [ edit ] 

 Post-Vedic, which casts some doubt on a relationship with Classical Persian کُنْد ( kund , “ blunt, dull, slow ” ) . Turner notes the wide variation of forms in this word family—see Prakrit कुंठ ( kuṃṭha ) —, and therefore suggests substrate origin. Compare Kannada ಕುಣ್ಟ ( kuṇṭa , “ cripple ” ) and Telugu కుంటి ( kuṇṭi , “ lame, crooked ” ) . Part of the Indo-Aryan "defective" group of words.

 Pronunciation
 [ edit ] 

 ( Classical Sanskrit ) IPA ( key ) : /kuɳ.ʈʰɐ/ 

 Adjective
 [ edit ] 

 कुण्ठ • ( kuṇṭha ) stem 

 blunt , dull 

 stupid , indolent , lazy , foolish
```


## [2026-09-06T21:55:32.318Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://www.sanskritdictionary.com/?iencoding=iast&q=kuNTha&lang=sans&action=Search\" \\\n \"https://en.wiktionary.org/wiki/%DA%A9%D9%86%D8%AF%D8%A7%D9%88%D8%B1\" \\\n \"https://en.wiktionary.org/wiki/%E0%A4%95%E0%A5%81%E0%A4%B2%E0%A4%9E%E0%A5%8D%E0%A4%9C%E0%A4%A8\" \\\n \"https://www.ahdictionary.com/word/search.html?q=galingale\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 285 verification: kuntha gloss / kondavar / kulanjana / AHD galingale\" 2>&1 | tail -1\ndone"
}
```


### [2026-09-06T21:55:35.926Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/edb410933288e2e6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/57b60cd1d5c5022e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/df30a9efa9a5a7c5.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/bdc06d855490dcfa.txt
```


## [2026-09-06T21:55:40.103Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"=== sanskritdictionary kuNTha ===\"; grep -n -i 'kuṇṭha\\|kuntha' edb410933288e2e6.txt | head -20\necho; echo \"=== kulañjana ===\"; grep -n -i -A6 'Etymology' df30a9efa9a5a7c5.txt | sed -n '25,60p'\necho; echo \"=== AHD galingale ===\"; grep -n -i 'galingale\\|khalanjan\\|Chinese' bdc06d855490dcfa.txt | head -20"
}
```


### [2026-09-06T21:55:40.184Z] TOOL RESULT

```
=== sanskritdictionary kuNTha ===
1:URL: https://www.sanskritdictionary.com/?iencoding=iast&q=kuNTha&lang=sans&action=Search

=== kulañjana ===

=== AHD galingale ===
1:URL: https://www.ahdictionary.com/word/search.html?q=galingale
4:TITLE: American Heritage Dictionary Entry: galingale
6:American Heritage Dictionary Entry: galingale
```


## [2026-09-06T21:55:42.859Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"=== AHD ===\"; sed -n '1,120p' bdc06d855490dcfa.txt\necho \"=== kulanjana ===\"; sed -n '140,180p' df30a9efa9a5a7c5.txt"
}
```


### [2026-09-06T21:55:42.913Z] TOOL RESULT

```
=== AHD ===
URL: https://www.ahdictionary.com/word/search.html?q=galingale
FETCHED: 2026-09-06T21:55:35Z
STATUS: 200
TITLE: American Heritage Dictionary Entry: galingale

American Heritage Dictionary Entry: galingale 

 HOW TO USE THE DICTIONARY
 To look up an entry in The American Heritage Dictionary of the English Language, use the search window above. For best results, after typing in the word, click on the “Search” button instead of using the “enter” key.
 Some compound words (like bus rapid transit, dog whistle, or identity theft ) don’t appear on the drop-down list when you type them in the search bar. For best results with compound words, place a quotation mark before the compound word in the search window.
 guide to the dictionary 

 THE USAGE PANEL
 The Usage Panel is a group of nearly 200 prominent scholars, creative writers, journalists, diplomats, and others in occupations requiring mastery of language. Annual surveys have gauged the acceptability of particular usages and grammatical constructions.
 The Panelists 

 NEED HELP SOLVING A CROSSWORD PUZZLE?

 Go to our Crossword Puzzle Solver and type in the letters that you know, and the Solver will produce a list of possible solutions.

-->
 AMERICAN HERITAGE DICTIONARY APP
 The new American Heritage Dictionary app is now available for 
 iOS and Android. 

 THE AMERICAN HERITAGE DICTIONARY BLOG
 The articles in our blog examine new words, revised definitions, interesting images from the fifth edition, discussions of usage, and more.

 OPEN DICTIONARY PROJECT

 Share your ideas for new words and new meanings of old words!

 Start Sharing Now! 

 --> See word lists from the best-selling 100 Words Series!
 Find out more! 

 INTERESTED IN DICTIONARIES?
 Check out the Dictionary Society of North America at http://www.dictionarysociety.com 

 gal·in·gale (g ă l  ĭ n-g ā l ′ ) 
 Share: 

 Tweet 

 n. 1. Any of various sedges of the genus Cyperus, especially C. longus of Europe, having rough-edged leaves, reddish spikelets, and aromatic roots.
 2. See galangal .

 [Middle English, aromatic root of any of several kinds of plants, galangal; see GALANGAL .]

 The American Heritage® Dictionary of the English Language, Fifth Edition copyright ©2022 by HarperCollins Publishers. All rights reserved.

 Indo-European & Semitic Roots Appendices
 Thousands of entries in the dictionary include etymologies that trace their origins back to reconstructed proto-languages. You can obtain more information about these forms in our online appendices:
 Indo-European Roots 
 Semitic Roots 
 The Indo-European appendix covers nearly half of the Indo-European roots that have left their mark on English words. A more complete treatment of Indo-European roots and the English words derived from them is available in our Dictionary of Indo-European Roots .

 American Heritage Dictionary Products
 The American Heritage Dictionary, 5th Edition

 The American Heritage Dictionary of Idioms

 The American Heritage Roget's Thesaurus

 Curious George's Dictionary

 The American Heritage Children's Dictionary

 CONTACT US 
 Customer Service 
 Make Me An Author 
 Ebooks Help with Glose Reader 
 ABOUT US 
 Company Profile 
 Leadership Team 
 Corporate Social Responsibility 
 HarperCollins Careers 
 HarperCollins Imprints 
 HarperGreen 
 Social Media Directory 
 Accessibility 
 FOR READERS 
 Browse Reading Guides 
 FOR AUTHORS 
 Submit a Manuscript 
 Report Piracy 
 Agent Portal 
 MEDIA 
 Publicity Contacts 
 Press Room 
 SERVICES 
 HarperCollins Speakers Bureau 
 Library Services 
 Academic Services 
 Desk & Exam Copies 
 Review Copies 
 OpenBook API 
 Marketing Partnerships 
 COVID-19 RESOURCES & PERMISSIONS 
 Permissions for Adult Online Readings 
 Permissions for Kids Online Readings 
 SALES & RIGHTS 
 Booksellers & Retailer Ordering 
 HarperCollins Catalogs 
 Permissions 
 Subsidiary Rights 
 Media Rights and Content Development 
 GLOSE APP 
 iPhone 
 Android 

 GLOBAL DIVISIONS 
 HarperCollins US 
 HarperCollins Canada 
 HarperCollins Christian 
 HarperCollins Australia 
 HarperCollins India 
 HarperCollins UK 

=== kulanjana ===
 hide 

 From Wiktionary, the free dictionary

 Sanskrit
 [ edit ] 

 Alternative forms
 [ edit ] 

 कुलञ्ज ( kulañja ) 

 Alternative scripts
 [ edit ] 

 Alternative scripts
 কুলঞ্জন ( Assamese script ) 
 ᬓᬸᬮᬜ᭄ᬚᬦ ( Balinese script ) 
 কুলঞ্জন ( Bengali script ) 
 𑰎𑰲𑰩𑰗𑰿𑰕𑰡 ( Bhaiksuki script ) 
 𑀓𑀼𑀮𑀜𑁆𑀚𑀦 ( Brahmi script ) 
 ကုလဉ္ဇန ( Burmese script ) 
 કુલઞ્જન ( Gujarati script ) 
 ਕੁਲਞ੍ਜਨ ( Gurmukhi script ) 
 𑌕𑍁𑌲𑌞𑍍𑌜𑌨 ( Grantha script ) 
 ꦏꦸꦭꦚ꧀ꦗꦤ ( Javanese script ) 
 𑂍𑂳𑂪𑂖𑂹𑂔𑂢 ( Kaithi script ) 
 ಕುಲಞ್ಜನ ( Kannada script ) 
 កុលញ្ជន ( Khmer script ) 
 ກຸລຎ຺ຊນ ( Lao script ) 
 കുലഞ്ജന ( Malayalam script ) 
 ᡬᡠᠯᠠᠨᡳᠶᡯᠠᠨᠠ ( Manchu script ) 
 𑘎𑘳𑘩𑘗𑘿𑘕𑘡 ( Modi script ) 
 ᢉᠤᠯᠠᡛᠽᠠᠨᠠ᠋ ( Mongolian script ) 
 𑦮𑧔𑧉𑦷𑧠𑦵𑧁 ( Nandinagari script ) 
 𑐎𑐸𑐮𑐘𑑂𑐖𑐣 ( Newa script ) 
 କୁଲଞ୍ଜନ ( Odia script ) 
 ꢒꢸꢭꢛ꣄ꢙꢥ ( Saurashtra script ) 
 𑆑𑆶𑆬𑆚𑇀𑆘𑆤 ( Sharada script ) 
 𑖎𑖲𑖩𑖗𑖿𑖕𑖡 ( Siddham script ) 
 කුලඤ‍්ජන ( Sinhalese script )
```


## [2026-09-06T21:55:49.103Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nawk '/Etymology/{f=1} f' df30a9efa9a5a7c5.txt | sed -n '1,40p'"
}
```


### [2026-09-06T21:55:51.123Z] TOOL RESULT

```
 Etymology 

 1.4 
 Pronunciation 

 1.5 
 Noun 

 1.5.1 
 Descendants 

 1.6 
 References 

 Toggle the table of contents 

 कुलञ्जन 

 3 languages 

 हिन्दी 
 Malagasy 
 संस्कृतम् 

 Entry 

 Discussion 

 English 

 Read 

 Edit 

 View history 

 Tools 

 Tools
```


## [2026-09-06T21:55:54.417Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\ngrep -n 'Perhaps\\|Chinese\\|Descendants\\|galangal\\|Alpinia\\|Persian' df30a9efa9a5a7c5.txt | head -20\necho \"---\"; sed -n '/^ Etymology$/,/^ Noun$/p' df30a9efa9a5a7c5.txt | tail -40"
}
```


### [2026-09-06T21:55:56.370Z] TOOL RESULT

```
77: Descendants 
193: Perhaps borrowed from Chinese 高良薑  / 高良姜 ( gāoliángjiāng ) , from 高涼  / 高凉 ( Gāoliáng ) (a prefecture or county in China) + 薑  / 姜 ( jiāng , “ ginger ” ) .
209: Descendants
212: → Classical Persian: قُولَنْجَانْ ( qūlanjān ) → Arabic: خُولَنْجَان ( ḵūlanjān ) , خَلَنْجَان ( ḵalanjān ) → Middle Armenian: խօլնջան ( xōlnǰan ) , խօլնճան ( xōlnčan ) 
213: → Persian: خاولنجان ( xâwlanjân ) , خولنجان ( xawlinjān ) , خالولنجان ( xālūlinjān ) → Old Anatolian Turkish: خولنجان ( havlincan ) Ottoman Turkish: خولنجان ( havlincan ) Turkish: havlıcan 
222: Categories : Sanskrit terms borrowed from Chinese 
223: Sanskrit terms derived from Chinese 
---
 Etymology
 [ edit ] 

 Perhaps borrowed from Chinese 高良薑  / 高良姜 ( gāoliángjiāng ) , from 高涼  / 高凉 ( Gāoliáng ) (a prefecture or county in China) + 薑  / 姜 ( jiāng , “ ginger ” ) .

 Pronunciation
 [ edit ] 

 ( Vedic ) IPA ( key ) : /ku.lɐɲ.d͡ʑɐ.nɐ/ 

 ( Classical Sanskrit ) IPA ( key ) : /ku.l̪ɐɲ.d͡ʑɐ.n̪ɐ/ 

 Noun
```


## [2026-09-06T21:56:11.106Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '13210,13245p' BQT_v2_pages.txt\necho \"=== pdf page tag near ===\"; awk 'NR<=13245 && /\\[pdf page/ {p=$0} END{print p}' BQT_v2_pages.txt\nsed -n '13200,13215p' BQT_v2_pages.txt | grep -n 'pdf page'\ngrep -n '\\[pdf page' BQT_v2_pages.txt | awk -F: '$1<13215' | tail -2"
}
```


### [2026-09-06T21:56:12.876Z] TOOL RESULT

```
                                                                                               ‫گعص‬
                                                                                                 ‫سر‬
                              ‫وشامخ ‪,‬هنی رفیم (‪. )۲‬‬      ‫حل » م اول وکسرثانی و سکون‬
 ‫حلو گر ده = بم اول وکاف فارحی؛‬                          ‫نون » کسی را گونن دکه پیوسته آب غلیظ ازینی‬
 ‫نوعی‌ازآلوی بزرکه‌باشد‪ .‬وبعضی کوبندمیوه‌ایست‬                                          ‫او روان شود ‪.‬‬
                                      ‫شبیه بشفتالو ‪.‬‬     ‫خلنج ‪ » ۴‬بنتح اول و انی و سکون‬
                                                         ‫نون وجیم » هرچیز دورنگه باشد و بعربی ابلق‬
 ‫خلو لا = بضم اول ونانی‌مجهول وکر‬
                                                         ‫خوانند ؛ وباینمعتی بکسراول بروزن شکنج هم‬
‫لام بورزن فلوئیا» بی‌شرم و بی‌باك و بیحیا را‬
                                                         ‫آمده است ‪ -‬و کبوتری را نز گونند که تمامآن‬
 ‫کوبند ‪ -‬ومردم دیواله مزاج کرفاهتمه‌اند ‪- ۷‬‬
‫و چیزبرا لیر کوبند که هرکس خواهد او را‬                  ‫سیاء بود مگربك پربادوپرازبال او کهسفید‬
                                                         ‫میباشه ‪ -‬وبکراول وثالی بروزن برنج ‪ .‬گرفتن‬
 ‫متصرف‌شودمانعی لداشته باشد ‪ -‬وعلت مالیخولیا‬
                                    ‫را همگفته‌اند ‪5‬‬                        ‫دن بناخن باشد ‪.‬‬
                                                                                         ‫کضانو‬
                                                                                             ‫اع‬
                                                          ‫خلنده ‪ = ۴‬بفتح اول بر وزن دولده‪.‬‬
 ‫خله ‪ -‬بفتع اول و الی " چوب درازی‬
                                                               ‫باندرون رونده ومجروح کننده راکویند ‪.‬‬
‫که بدان کشتی میرانشد ؛ وبایتمعنی جضم اول‌هم‬
 ‫و فرو رونده‬             ‫ده‬
                          ‫لینکه‬
                              ‫خیز‬
                                ‫وچ‬      ‫آمده استھ ‏‬      ‫خلنگ ‪ ۴‬بنتماول بروزن پلنگه‪,‬‬
                                                          ‫بمعنی خلنج است که دورنگه وابلق باشد ® ‪-‬‬
 ‫درجایی باشد مالند سوزن و جوال دوز و درفش‬
‫وامثال آن ‪٩‬‏ ‪ -‬وبمعنی خالی هم آمده امت که‬                ‫کورفتن اعنارا نگیوزیند بناخن ؛ وبکر اول‬
 ‫در برابر پراست ‪*٩-‬‏ وبادبرا نیز گویند خلنده‌در‬                                                ‫‪۰‬‬   ‫هت‬   ‫هم‬


 ‫مک‪٩‬‏ ‪ -‬ودردی که بسك ناگاهدریپلو ومقا» ل‬                ‫خلو = نم اول بروزن غلو‪ .‬بمعنی آلو‬
 ‫بهم‌رسد ‪۱٩-‬‏ وهرزه گویی وحذبان راهمکفته‌اند‪.‬‬            ‫باشدا »و آن میوه‌است معروف» ولوعی ازا لوی‬


=== pdf page tag near ===
```


## [2026-09-06T21:56:31.887Z] TOOL CALL #56: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py"
}
```


### [2026-09-06T21:56:31.925Z] TOOL RESULT

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


## [2026-09-06T21:57:22.230Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n 'kunj\\b\\|kunj,\\|kunj ' RCH.txt | head -10\necho \"--- kanj/gunj ---\"; grep -n -i 'hunchback\\|hump-backed' RCH.txt | head -10"
}
```


### [2026-09-06T21:57:22.303Z] TOOL RESULT

```
23016:A   iadahkunj  (ii  of  q)  Being  constituted  head  man
49216:Tlie  inhabitants  of  the  desert,  (met.)  Trees,  grass,  and  the  like. sakana^i  kanutiy  Charcoal.  {Uurhdn^i  kdti^') p   saknajy  A   kind  of  bitumen  brought  from  Syria.  Sa^ kunj  or  sukunjy  A   putrid  smell  from  the  mouth.  One  who  has  a fetid  breath.  Sikunjy  A   cough.  Shaving,  scraping.  Choice, p   sikanjuhtn  (or  sikangHhhi)^  Oxymel.
--- kanj/gunj ---
1032:XII.  ihdiddb  (from  ihdaxodaba)^  Being  hump-backed.
2614:aWI  ttjna-a^  Hump-backed.  A   sheep  whose  horns  bend backwards.
2887:A   ahjaHj  Crooked,  hump-backed,  hawk-nosed.
2896:A ihddh^  (iv  of  c.yhV>.)  Making  one  hump-backed; giving  an  inclination.
2918:A   ihdiddby  (xii  of  c.,,>iX>>)  Being  hump-backed.
16644:A   bazdicd^  Hump-backed  (woman), p   buzdydnldan^  To  assist  a   woman  in  labour.
22274:inclined.  Being  hump-backed.
29696:<   Aj^ju8u-a  (from  U^)  FalHng  flat  on.  Being  hump-backed.
31129:A   ^ji^janafiy  A   grave.  A   winding-sheet.  Jununy  Madness. A^^^junu^a  (from  t:^).  Falling  prostrate  upon,  or  bending down  towards.  Being  hump-backed.
33105:backed. Being  favorably  inclined,  benevolent.  High  ground, billy.  Hump-backed.  Hadib,  Hump-backed.
```


## [2026-09-06T21:57:27.796Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '26855,26910p' MON_part2.txt"
}
```


### [2026-09-06T21:57:27.847Z] TOOL RESULT

```
: ۷01 (ص.) گو ژیشت» قوزی. 
کنجد: 164- ,۲۵۵124۵ [- کنجید| (.) (گیا.) 
گیاهی است از رده دو لیه‌بی‌های بو سته 
گلبرک که سردستة تبرٌ کنجدها می‌باشد. 
این گیاه یکث ساله است و ارتفاعش بالغ بر 
یک متر است. قسمت فوقانی ساقه‌اش 
بوشیده از کرک می‌باشد ولی قسمت‌های 
تحتانی آن عاری از ک رک است. برگ‌هایش 
در قسمت قاعده بنطور متتناوت و در 
قسمت‌های انتهایی ساقه بطور متقابل قرار 


فررهنگ فارسی معین 


۱ ۱ 
گرفته. پهنک برگ‌ها بیضوی و دراز و 
نوک تبز است و در قسمت قاعده ساقه 
پهن‌تر از قسمت انتهایی است. گل‌های ۹1 
که بطور منفرد در کنارةٌ ب رگ‌های قسمت 
انتهایی ساقه قرار دارد» شامل قطعات ۵ تایی 
پیوسته بهم می‌باشد ولی تعداد پرچم‌ها ۴ 
عدد است. میوه‌اش کپسولی و محتوی 
دانه‌های کو چکك مسطح و بیضوی است. 
دانه‌های کنجد به سبب دارا بودن مواد روغن 
قابل استخراج تنها قسمت مورد استفاده گیاه 
است؛ سمسم» جلجلان کنجد ساه: (گیا.) 
گیاهی است از تبر5 نعناعبان و از دسته علف 
کر به ها است که بکساله است و دارای 
گل‌های آبی و گاهی زرد است. از دانه‌های 
سیاه رنگ و ریز این گیاه روغن خشکث 
شو نده‌ای حاصل می‌شو د که علاوه بر آنکه 
در برخی نقاط به مصرف تغذیه می‌رسد» در 
ساختن ورنی نیز از آن استفاده می‌کنند. گیاه 
مذکور در اکثر نقاط جهان (از جمله شمال و 
مغرب و جنوب ایران) می‌رو بد. 

کنجر: -0۲ ,122۸۲ [هند. قس . کنج | (ص.) 
بزرگ جثه (فیل)» وی هیکل (پیل). 
کنحکاو: « لحم [ - کنج کاونده] (ص‌فا.) 
آنکه کنجکاوی کند؛ متفحصء غوررس. 
کنجکاوی: -۲۰:5۷ (حامص.) تفحص 
دقیق» غوررسی. 

کنجل: الما آهم‌چیده] (ص.) هر چیز 
درهم کشیده و چین و شکن بهم رسانیده. 
دست و پایی که انگشتانش درهم کشیده 
شده باشد. خمیر نانی که در تنور افتاده و در 
میان آتش بخته شده باشد. 

و اه (عم.) تکه کومت 
کوچکی که بر سیخ کشند با قیمه کنند دکنات 
کنجه: کنجه‌پی. 

کنچه: 0 [- کنج] (ص.) خری که 
زير دهانش ورم کرده باشد. خر دم بر ید ه.
```


## [2026-09-06T21:57:32.974Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '26840,26858p' MON_part2.txt"
}
```


### [2026-09-06T21:57:33.028Z] TOOL RESULT

```
کنتور: ۲00۲ (.) (فز.) آلنی که مقدار 
مصرف برق» آب» گاز و غبره را در یک 
خانه یا یک موسسه تعیین کند کنتور ساعتی: 
(فز.) کنتور برقی که مصرف برق را در 
ساعات شب و روز جدا کانه تعیین نماید. 
کنج: آمها (ا.) گوشت ت باره‌ای است که از 
انتهای کام آو بخته . کنج و کام کردن: سق 
کودک را برداشتن. 
کنج: ۲۵ [قس. کنجر ] (ص.) بزرگ جثه و 
قوی هیکل (فیل). ضح.- در فهرست و لف 
این کلمه نیامده. 
کنج: آجه۲ (.) کوشة 4 (خانه و جز آن)» 
زاویه. کنج خلوت : گوشه‌ای رن 
کنج: : ۲۵ [- کنجل - کنجلککك] (.) چین و 
شکنی که در بدن» جامه» فرش و غبره افتد. 
: ۷01 (ص.) گو ژیشت» قوزی. 
کنجد: 164- ,۲۵۵124۵ [- کنجید| (.) (گیا.) 
گیاهی است از رده دو لیه‌بی‌های بو سته 
گلبرک که سردستة تبرٌ کنجدها می‌باشد.
```


## [2026-09-06T21:57:40.879Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nmkdir -p data/verification/sources/refs/ocr/BOOK\ncp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg285.png data/verification/sources/refs/ocr/BOOK/285.png\nls -la data/verification/sources/refs/ocr/BOOK/285.png"
}
```


### [2026-09-06T21:57:40.940Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 84487 Sep  6 17:57 data/verification/sources/refs/ocr/BOOK/285.png
```


## [2026-09-06T21:57:50.238Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"=== etymonline galingale ===\"; grep -n -i 'galingale\\|galangal' ef38195e62a71b47.txt | head -10\necho \"=== گندآور ===\"; wc -l 27a46996f811cf90.txt; grep -n -i 'no entry\\|does not\\|Persian' 27a46996f811cf90.txt | head -5\necho \"=== کنداور ===\"; wc -l 57b60cd1d5c5022e.txt; grep -n -i 'Persian\\|Etymology' 57b60cd1d5c5022e.txt | head -5"
}
```


### [2026-09-06T21:57:50.323Z] TOOL RESULT

```
=== etymonline galingale ===
1:URL: https://www.etymonline.com/word/galingale
=== گندآور ===
5 27a46996f811cf90.txt
=== کنداور ===
5 57b60cd1d5c5022e.txt
```


## [2026-09-06T22:05:08.033Z] TOOL CALL #62: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk285.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW = \"https://en.wiktionary.org/wiki/\"\n\ndoc = {\n \"pdf_page\": 285,\n \"book_page\": 255,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-06\",\n \"entries\": [\n\n  # ---------------- entry 0 : Kulanjâ ----------------\n  {\n   \"entry\": 0,\n   \"root\": \"Kulanjâ\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"Sanskrit कुलञ्जन kulañjana (var. कुलञ्ज kulañja) 'galangal, Alpinia galanga'\",\n   \"note\": \"The root box is right: Sanskrit kulañja(na) is the name of Alpinia galanga and is the recognised source of the Arabic drug-name. Laufer, Sino-Iranica p.545 (SIN:545, Nourai's own reference) says in so many words 'the Arabic word is derived from Sanskrit kulanja, which denotes Alpinia galanga'. Two flaws in the box itself: the gloss prints 'alpina galanga' for Alpinia galanga (a misprint in the book, faithfully extracted), and Nourai spells the headword Kulanjâ where the sources have kulañja / kulañjana. The chart's NOTE reproduces the old dispute correctly — AHD (1975) and Klein p.635 make the word ultimately Chinese kao-liang-kiang 'ginger of Kao-liang', Laufer p.545-546 calls that an error ('The whole group has nothing to do with Chinese kao-liah-kiah … Alpinia galanga does not occur in China, but is a native of Bengal, Assam, Burma, Ceylon and the Konkan'). Modern scholarship has not settled it: Wiktionary keeps the Chinese source but only as 'perhaps'. Either way the Sanskrit word is the immediate ancestor of the Persian/Arabic/European forms, so the root box stands. The real problem on this page is the Persian node (#1): Nourai has substituted the unrelated Persian word خلنج/خلنگ 'heather, piebald wood' for the actual Persian mediator خولنجان/قولنجان.\",\n   \"note_fa\": \"ریشهٔ این خانواده در سنسکریت است: kulañja / kulañjana نام گیاه Alpinia galanga (خولنجان). لاوفر در «سینو-ایرانیکا» ص۵۴۵ ــ که خودِ نورایی به آن ارجاع می‌دهد ــ صریحاً می‌نویسد واژهٔ عربی از سنسکریت kulanja گرفته شده است. بنابراین جعبهٔ ریشه درست است، هرچند در چاپ کتاب «alpina galanga» به جای «Alpinia galanga» آمده که غلط چاپی است. دربارهٔ خاستگاه چینی (kao-liang-kiang «زنجبیل کائولیانگ») که کلاین و AHD می‌گویند و لاوفر آن را خطای ترجمه می‌خواند، پژوهش امروزی هنوز قطعی نیست؛ ویکی‌واژه آن را با قید «شاید» می‌آورد. اشکال اصلی این نمودار در گرهٔ فارسی است: نورایی «خلنج/خلنگ» (نوعی درخت دورنگ، خلنگ/اریکا) را به جای واسطهٔ راستین یعنی «خولنجان/قولنجان» نشانده است.\",\n   \"sources\": [\n     W + \"galingale\",\n     W + \"%E0%A4%95%E0%A5%81%E0%A4%B2%E0%A4%9E%E0%A5%8D%E0%A4%9C%E0%A4%A8\",\n     \"https://www.ahdictionary.com/word/search.html?q=galingale\"\n   ],\n   \"ref_check\": [\n     {\"ref\": \"SIN:545\", \"status\": \"supports\",\n      \"note\": \"Laufer, Sino-Iranica p.545 (SIN.txt line 3591, leaf 373 = printed 545): '…as was recognized long ago, the Arabic word is derived from Sanskrit kulanja, which denotes Alpinia galanga. The European forms with ng (galangan, galgan, etc.) were suggested by the older Arabic pronunciation khulangan.' Same page: 'the Arabic word from which the European name is derived was wrongly written by Hanbury khalanjan, while in fact it is khulanjan (xulandzan), Persian xawalinjan.'\"}\n   ],\n   \"consulted\": [\n     {\"src\": \"KLN\", \"where\": \"1966 ed. leaf 344 = p.635 s.v. galingale\", \"stance\": \"partial\",\n      \"note\": \"'galingale, n., an aromatic root of the ginger family. — OF. galingal, formed—through the medium of MGk. γαλαγγα and ML. galanga, fr. Arab. khalanjan, fr. Pers., ult. fr. Chin. Ko-leung-keung, lit. \\\"mild ginger from the region of Kao\\\".' Klein has the Persian link but no Sanskrit, and makes the ultimate source Chinese.\"},\n     {\"src\": \"LKT\", \"where\": \"no. 795 'Ar. halangan' (LKT.txt line 1926 = printed p.63)\", \"stance\": \"partial\",\n      \"note\": \"Lokotsch heads the entry with Arabic ḫalangān and follows Hirth: 'ist ar. halangan auf chin. ko-liung-kiung, d. h. milder Ingwer von Kao-tschau-fu … zurückzuführen'; he notes Ibn Ḫurdāḏbih c.875 lists it as a Chinese product. No Sanskrit.\"},\n     {\"src\": \"FSD\", \"where\": \"vol. II line 29137 s.v. galangal\", \"stance\": \"partial\",\n      \"note\": \"'[ME. galingale, galange, < OF. galingal, galange, < LL. galanga, < Ar. khalanjan, < Chin. Ko-liang-kiang …]' — Latin form galanga, Chinese ultimate source, no Sanskrit.\"},\n     {\"src\": \"DEV\", \"where\": \"p.123-124 s.v. Galanga (DEV.txt line 1374)\", \"stance\": \"supports\",\n      \"note\": \"'Galanga. Esp. et portug. galanga, anc. franç. galangal, garingal, angl. galangale. Le nom de cette plante, originaire des Indes, nous est venu par l'arabe khaulandjân' — Devic makes the plant Indian and the route Arabic, as Laufer does.\"}\n   ],\n   \"nodes\": [\n\n    {\"id\": 1, \"lang\": \"Persian\", \"words\": \"xalanj, xalang\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"Two different Persian words have been welded together here. (a) خلنج xalanj / خلنگ xalang is a native Persian tree-name: Borhan-e Qate' defines خلنج as 'anything two-coloured, which in Arabic is called ablaq (piebald)' and خلنگ as 'the same as خلنج, two-coloured and piebald'; Mo'in's lexicon defines خلنگ as a shrub of the Ericaceae, 'broom-grass', synonym خلنج; Richardson lists 'p khalanj also khilanj, of two colours, piebald' and 'A khalanj (or p khulanj), a tree from which they make beams or wooden bowls'. That is heather / Erica arborea, whose mottled root-wood was turned into bowls — nothing to do with the ginger-family rhizome. Wiktionary's Arabic entry خَلَنْج ḵalanj 'heather, various Ericeae plants' is explicitly 'Borrowed from Classical Persian خلنگ (xalang, \\\"heather\\\")', with a citation from Ibn al-Faqīh (c. 910). (b) The Persian word that actually carried Sanskrit kulañjana westwards is خولنجان / خاولنجان / قولنجان (xawalinjān, qulanjān): Laufer p.545 writes 'Persian xawalinjān', Asbaghi p.112 gives Arabic ḫalanǧān 'Alpinia' as from Persian ḫulanǧān and Sanskrit kulañja, and Richardson has 'P khālinjān, galangale' and 'P khulanjān, the herb galangale' as separate headwords from خلنج. Nourai's gloss 'galingale' on خلنج/خلنگ is therefore wrong, and the arrow Skt kulañja → NP xalanj/xalang does not hold: the heather-word is not a Sanskrit loan at all.\",\n     \"derivation_fa\": \"در این گره دو واژهٔ جداگانه به هم آمیخته شده است. «خلنج/خلنگ» واژه‌ای بومی فارسی است: برهان قاطع خلنج را «هر چیز دورنگ که به عربی ابلق خوانند» و خلنگ را «به معنی خلنج است که دورنگ و ابلق باشد» تعریف می‌کند؛ معین نیز خلنگ را درختچه‌ای از تیرهٔ خلنگ‌ها (اریکا/علف جاروب) و مرادف خلنج می‌داند؛ ریچاردسون هم آن را «دورنگ، ابلق» و «درختی که از چوبش کاسه و تیر می‌سازند» می‌آورد. ویکی‌واژه نیز عربیِ «خَلَنْج» را وام‌واژه‌ای از فارسی «خلنگ» به معنی اریکا می‌شمارد. اما واسطهٔ راستینِ سنسکریت kulañjana در راه غرب، «خولنجان/خاولنجان/قولنجان» است؛ لاوفر صورت فارسی را xawalinjān می‌نویسد و اصباغی (ص۱۱۲) عربی ḫalanǧān را از فارسی ḫulanǧān و سنسکریت kulañja می‌گیرد. پس معنیِ «galingale» برای خلنج/خلنگ نادرست است و پیکان «کولنجای سنسکریت ← خلنج فارسی» پذیرفتنی نیست: پژوهش امروزی این دو را دو واژهٔ جدا می‌داند.\",\n     \"sources\": [W + \"%D8%AE%D9%84%D9%86%D8%AC\", W + \"%D8%AE%D9%88%D9%84%D9%86%D8%AC%D8%A7%D9%86\"],\n     \"ref_check\": [\n       {\"ref\": \"MON:1437\", \"status\": \"partial\",\n        \"note\": \"Mo'in's lexicon entry (checked in the 2-vol Adena reprint OCR, MON_part1.txt lines 57245-57252; the 6-vol p.1437 has no local pagination): 'خلنج [= خلنگ] (ص.) دو رنگ' and 'خلنگ … (گیا.) گیاهی است از تیرهٔ خلنگ‌ها که بصورت درختچه یا علفی است … علف جاروب؛ خلنج.' Mo'in gives heather/piebald, not galingale, and no Sanskrit etymology — so the reference has the word but not Nourai's claim.\"},\n       {\"ref\": \"SIN:545\", \"status\": \"contradicts\",\n        \"note\": \"SIN.txt line 3591 (printed p.545): Laufer's Persian form is 'xawalinjan', and he stresses that the Arabic is khulanjan (not khalanjan) — i.e. the Persian mediator is خولنجان, not خلنج/خلنگ.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"BQT\", \"where\": \"vol. 2, BQT_v2_pages.txt lines 13215 and 13235\", \"stance\": \"contradicts\",\n        \"note\": \"'خلنج، بفتح اول و ثانی و سکون نون و جیم، هرچیز دورنگ باشد و بعربی ابلق خوانند' ; 'خلنگ، بفتح اول بروزن پلنگ، بمعنی خلنج است که دورنگ و ابلق باشد'. Borhan knows no galangal sense for these words; its galangal entries are under خولنجان (lines 9433, 12153).\"},\n       {\"src\": \"RCH\", \"where\": \"RCH.txt lines 37129-37131, 37664, 37987\", \"stance\": \"contradicts\",\n        \"note\": \"Richardson separates them: 'p khalanj also khilanj, Of two colours. Piebald.' / 'A khalanj (or p khulanj), A tree from which they make beams, or wooden bowls.' / 'A khalanjān, The root galangale.' / 'P khālinjān, Galangale.' / 'P khulanjān, The herb galangale.'\"},\n       {\"src\": \"PLA\", \"where\": \"Asbaghi p.112 (PLA_asbaghi_1988_ia_djvu.txt lines 8766-8767)\", \"stance\": \"partial\",\n        \"note\": \"Two separate lemmas on the same page: 'ḫalanǧ: \\\"ein Baum, aus dessen Holz Gefäße gemacht werden\\\" pers.' and 'ḫalanǧān: \\\"Alpinia (maranta)\\\" pers. ḫulanǧān, aind. kulaǧing [kulañja], afrz. galanga …'. Only the second has the Sanskrit source.\"},\n       {\"src\": \"MON\", \"where\": \"MON_part1.txt lines 57245-57252\", \"stance\": \"contradicts\",\n        \"note\": \"خلنگ = Ericaceae shrub, 'علف جاروب'; خلنج = 'دو رنگ'. No galingale.\"}\n     ]},\n\n    {\"id\": 2, \"lang\": \"Arabic\", \"words\": \"xalanj, xalanjan\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"Both Arabic words are Persian loans, but of different Persian words, and only one of them belongs to this root. خَلَنْج ḵalanj 'heather, Erica/Calluna; wood turned into bowls' is borrowed from Classical Persian خلنگ xalang 'heather' (Wiktionary, with a c. 910 citation from Ibn al-Faqīh's Kitāb al-Buldān: 'wa-l-ḵalanju l-kaṯīru, wa-yattaḵiḏūna minhu ʿajāʾiba'); Asbaghi p.112 also gives ḫalanǧ simply as 'pers.'. خَوْلَنْجَان / خُولَنْجَان / خَلَنْجَان ḵawlanjān ~ ḵalanjān 'galangal (Alpinia)' is from Persian خولنجان/قولنجان, itself from Sanskrit kulañjana; Asbaghi p.112 gives exactly 'ḫalanǧān … pers. ḫulanǧān, aind. kulañja'. The Arabicised forms show the regular treatment of Persian x- and -ng- (Pers. -ng > Arab. -nǧ, since Arabic has no /g/), and the nisba-like ending -ān is the Persian plant-suffix carried over. So the node is right that these Arabic forms come from Persian; it is wrong to present ḵalanj and ḵalanjān as one word descending from Sanskrit through خلنج.\",\n     \"derivation_fa\": \"هر دو صورت عربی وام‌واژهٔ فارسی‌اند، اما از دو واژهٔ فارسیِ متفاوت. «خَلَنْج» به معنی خلنگ/اریکا و چوبی که از آن ظرف می‌تراشند، از فارسی «خلنگ» گرفته شده (ویکی‌واژه با شاهدی از «کتاب البلدان» ابن‌الفقیه، حدود ۲۹۷ هجری)؛ اصباغی نیز آن را تنها «pers.» می‌داند. اما «خَوْلَنْجَان/خَلَنْجَان» به معنی گیاه Alpinia از فارسی «خولنجان/قولنجان» و آن از سنسکریت kulañjana است (اصباغی ص۱۱۲: ḫalanǧān … pers. ḫulanǧān، aind. kulañja). در معرّب‌سازی، «گ» فارسی به «ج» بدل شده است چون در عربی /g/ نیست. پس ادعای «فارسی ← عربی» درست است، ولی یکی‌انگاشتنِ خلنج و خلنجان و کشیدن هر دو به سنسکریت پذیرفتنی نیست.\",\n     \"sources\": [W + \"%D8%AE%D9%84%D9%86%D8%AC\", W + \"%D8%AE%D9%88%D9%84%D9%86%D8%AC%D8%A7%D9%86\"],\n     \"ref_check\": [\n       {\"ref\": \"PLA:112\", \"status\": \"partial\",\n        \"note\": \"Asbaghi, Persische Lehnwörter im Arabischen p.112 (running head 'ḫalanǧ 112 banādiris', PLA_asbaghi_1988_ia_djvu.txt lines 8764-8767) has the two words as separate lemmas: 'ḫalanǧ: \\\"ein Baum, aus dessen Holz Gefäße gemacht werden\\\" pers.' and 'ḫalanǧān: \\\"Alpinia (maranta)\\\" pers. ḫulanǧān, aind. kulaǧing, afrz. galanga, sp., pg., ait. galanga, sp. garengal, frz. garengal, ahd. galangan'. Supports 'from Persian' but not Nourai's single chain.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"SIN\", \"where\": \"p.545 (SIN.txt line 3591)\", \"stance\": \"partial\",\n        \"note\": \"'the Arabic word … was wrongly written by Hanbury khalanjan, while in fact it is khulanjan (xulandzan), Persian xawalinjan' — Laufer insists the galangal word is khulanjān.\"},\n       {\"src\": \"KLN\", \"where\": \"p.635 s.v. galingale\", \"stance\": \"partial\",\n        \"note\": \"'fr. Arab. khalanjan, fr. Pers., ult. fr. Chin.' — Klein uses the khalanjān variant and stops at 'Pers.' without naming the Persian form.\"},\n       {\"src\": \"LKT\", \"where\": \"no. 795\", \"stance\": \"partial\",\n        \"note\": \"Headword 'Ar. ḫalangān'; Lokotsch derives it from Chinese, not from Persian or Sanskrit.\"},\n       {\"src\": \"AFM\", \"where\": \"AFM_pages.txt / AFM.txt, grep 'خلنج' and 'خولنجان'\", \"stance\": \"silent\",\n        \"note\": \"Addi Shir's list of Persian loans in Arabic returns no hit for either spelling in the OCR text.\"}\n     ]},\n\n    {\"id\": 3, \"lang\": \"Middle Latin\", \"words\": \"galinga\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"The Arabic drug-name reached Latin Europe through the Byzantine drug trade: Middle Greek γαλάγγα, whence Medieval Latin galanga (the form printed by Klein p.635, by Funk & Wagnalls 'LL. galanga', by Webster 'ML. galanga' and by Lokotsch no.795 'mlat. galanga'), used in the Salernitan and later herbals from the 11th-12th c. Alongside it a nasal-infixed variant with -ing- circulated (whence Old French galingal/garingal, Middle Dutch/German galgan, Middle English galingale) — this is the form Nourai spells 'galinga'. The book does print 'galinga' (page image checked), so the extraction is faithful; but no reference cited on this page prints that exact Latin lemma, and KLN:635, the reference Nourai attaches to the box, prints galanga. Treat 'galinga' as a back-formation from the -ing- Romance forms rather than as a quotable Medieval Latin headword.\",\n     \"derivation_fa\": \"نام دارویی عربی از راه بازرگانیِ دارو در قلمرو بیزانس به لاتینِ سده‌های میانه رسید: یونانی میانه γαλάγγα و از آن لاتینِ میانه galanga ــ همان صورتی که کلاین (ص۶۳۵)، وبستر، فانک‌واگنالز و لوکوچ (شمارهٔ ۷۹۵) می‌آورند. در کنار آن صورتی با «ـنگ» رواج داشت که فرانسهٔ کهن galingal/garingal و انگلیسی میانهٔ galingale از آن است؛ همین صورت است که نورایی «galinga» نوشته است. تصویر صفحهٔ چاپی نشان می‌دهد کتاب واقعاً «galinga» دارد (پس خطای خوانش اسکن نیست)، ولی هیچ‌یک از مراجع یادشده این سرواژهٔ لاتین را به این شکل ندارند؛ با احتیاط پذیرفتنی است.\",\n     \"sources\": [W + \"galingale\"],\n     \"ref_check\": [\n       {\"ref\": \"KLN:635\", \"status\": \"partial\",\n        \"note\": \"Klein 1966 leaf 344 (= p.635): 'OF. galingal, formed—through the medium of MGk. γαλαγγα and ML. galanga, fr. Arab. khalanjan'. Klein's Latin form is galanga, not galinga; and he routes the word through Old French, which the chart omits.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt line 79575 s.v. galingale\", \"stance\": \"partial\",\n        \"note\": \"'gal'in-gale, n. [ME. …; OF. galingal; ML. gal[an]ga; Ar. khalanjan]' — ML galanga.\"},\n       {\"src\": \"FSD\", \"where\": \"vol. II line 29137 s.v. galangal\", \"stance\": \"partial\",\n        \"note\": \"'< OF. galingal, galange, < LL. galanga' — the Latin lemma is galanga.\"},\n       {\"src\": \"LKT\", \"where\": \"no. 795\", \"stance\": \"partial\",\n        \"note\": \"'hieraus mgr. γαλάγγα, mlat. galanga, it. galanga, afrz. galange, garingal, frz. le galanga' — again galanga, with the -ing- only in the Romance forms.\"}\n     ]},\n\n    {\"id\": 4, \"lang\": \"English\", \"words\": \"galingale\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Middle English galingale (13th c., in cookery and medical texts; Chaucer's 'Nutemuge to putte in ale … And notemuge and galyngale') from Old French galingal/garingal, from the Medieval Latin/Middle Greek forms above, from Arabic ḵalanjān. Sense in English: originally the aromatic rhizome of Alpinia (galangal), later transferred to the European sedge Cyperus longus, whose root smells similar — the American Heritage Dictionary (5th ed.) still lists both senses and refers galingale to galangal. The chart's NOTE is an accurate report of the dispute: AHD (1975) and Klein p.635 give the Chinese origin ('mild ginger from the region of Kao'), Laufer p.545-546 calls it an error. Modern reference works have not resolved it — Wiktionary derives galingale from Middle English < Old French < Arabic < Persian قولنجان < Sanskrit कुलञ्जन, 'perhaps from Chinese 高良薑'.\",\n     \"derivation_fa\": \"انگلیسی میانه galingale (سدهٔ سیزدهم میلادی، در متن‌های آشپزی و پزشکی، از جمله در چاسر) از فرانسهٔ کهن galingal/garingal و آن از لاتینِ میانه و یونانی میانه و سرانجام از عربی «خلنجان». معنیِ نخستِ آن ریشهٔ معطر Alpinia بود و سپس به نوعی جگن اروپایی (Cyperus longus) نیز اطلاق شد؛ فرهنگ American Heritage هنوز هر دو معنی را می‌آورد. یادداشت نمودار درست گزارش شده است: کلاین و AHD خاستگاه چینی می‌دهند و لاوفر آن را خطای ترجمه می‌خواند؛ ویکی‌واژه امروز همان زنجیرهٔ سنسکریت ← فارسی ← عربی ← فرانسهٔ کهن ← انگلیسی را می‌آورد و خاستگاه چینی را با قید «شاید». ادعای نورایی در این گره درست است.\",\n     \"sources\": [W + \"galingale\", \"https://www.ahdictionary.com/word/search.html?q=galingale\"],\n     \"ref_check\": [\n       {\"ref\": \"KLN:635\", \"status\": \"supports\",\n        \"note\": \"Klein 1966 leaf 344 = p.635 s.v. galingale: 'an aromatic root of the ginger family. — OF. galingal … fr. Arab. khalanjan, fr. Pers., ult. fr. Chin. Ko-leung-keung, lit. \\\"mild ginger from the region of Kao\\\"' — exactly the Chinese claim the chart's NOTE attributes to KLN:635.\"},\n       {\"ref\": \"SIN:545\", \"status\": \"supports\",\n        \"note\": \"SIN.txt lines 3591 and 3605 (pp.545-546): 'The word galangal … is not of Chinese origin, as first supposed by D. Hanbury, and after him by Hirth and Giles. The error was mainly provoked by the fact that the Arabic word … was wrongly written by Hanbury khalanjan' ; 'The whole group has nothing to do with Chinese kao-liah-kiah.' — the chart's 'SIN:545 calls this a translation error' is accurate.\"},\n       {\"ref\": \"AHD:539\", \"status\": \"not_checked\",\n        \"note\": \"AHD:539 is a page of the 1975 New College Edition main dictionary, which is not open on archive.org. The online AHD 5th ed. entry for galingale gives only '[Middle English …; see GALANGAL]'. That the 1975 AHD gave the Chinese etymology is corroborated by Klein, Funk & Wagnalls and Lokotsch, which all print it.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"SKT\", \"where\": \"SKT.txt line 23699\", \"stance\": \"partial\",\n        \"note\": \"Skeat's appendix lists 'galingale' among the words that came to English 'French from Spanish from Arabic' — Arabic route confirmed, no further detail.\"},\n       {\"src\": \"HJB\", \"where\": \"HJB.txt line 7896\", \"stance\": \"supports\",\n        \"note\": \"Hobson-Jobson quotes Marco Polo (1298) on Java: 'producing black pepper, nutmegs, spikenard, galingale, cubebs, cloves' — the word is in English use as an Eastern drug-name.\"},\n       {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt line 79575\", \"stance\": \"supports\",\n        \"note\": \"'gal'in-gale … 1. the aromatic root stem of various East Indian plants of the ginger family; 2. a sedge with a pungent root … in the south of England' — both senses, Arabic etymology.\"},\n       {\"src\": \"FSD\", \"where\": \"vol. II line 29137\", \"stance\": \"supports\",\n        \"note\": \"'ga-lan'gal … 1. The aromatic stimulant rootstocks of various East-Indian herbs of the ginger family … especially several species of Alpinia, as A. galanga … 2. A sedge. See GALINGALE.'\"}\n     ]}\n   ]\n  },\n\n  # ---------------- entry 2 : Kund, Kundos ----------------\n  {\n   \"entry\": 2,\n   \"root\": \"Kund, Kundos\",\n   \"verdict\": \"disputed\",\n   \"modern_form\": \"Mann IEC *kundos 'stolid, stout, ponderous, stocky' — a Mann-only reconstruction; not a recognised PIE root\",\n   \"note\": \"Nourai's root box reproduces Mann's headword accurately (IEC p.588 'kundos \\\"stolid, stout, ponderous, stocky\\\"'; p.589 'kuntsios (?), kundsios (?) \\\"docked, short\\\". See kund-'), and Nourai's gloss 'blunt, stout, stocky, rough' is a fair paraphrase. But the reconstruction is Mann's alone. Pokorny's IEW has no such root (grep of POK_full/POK_01-03 for kundos/kunt-/kuntha returns nothing), Walde-Pokorny's register has nothing, and Watkins/AHD has no *kund-. Worse, the two limbs Mann builds it on are both suspect in current scholarship: Sanskrit कुण्ठ kuṇṭha is post-Vedic and Turner's wide formal variation points to a non-Indo-Aryan substrate word (cf. Kannada kuṇṭa 'cripple', Telugu kuṇṭi 'lame'), and Old Armenian kunt/kund is generally taken as an Iranian loanword, not an inherited cognate. Wiktionary accordingly calls the Persian-Sanskrit link 'dubious' and prefers a connection with Old Armenian ճաղատ čałat 'bare, bald' (following Asatrian & Arakelova, 'Blunt, Bald and Wise: Iranian kund(-)', Iran and the Caucasus 5 (2001) 201-206). So the box should read 'Iranian/Indo-Aryan regional word', not 'Indo-European'.\",\n   \"note_fa\": \"جعبهٔ ریشه دقیقاً از مان (فرهنگ تطبیقی هندواروپایی، ص۵۸۸: kundos «کودن، ستبر، سنگین، خپل») گرفته شده و برگردان نورایی هم درست است؛ اما این بازسازی تنها از آنِ مان است. در «فرهنگ ریشه‌شناختی هندواروپایی» پوکورنی چنین ریشه‌ای نیست، در والده-پوکورنی و در فهرست واتکینز/AHD هم نیامده. افزون بر این، دو پایهٔ استدلال مان امروز مورد تردید است: «کُنْثَه»ی سنسکریت پس‌ودایی است و ترنر پراکندگی صورت‌های آن را نشانهٔ واژه‌ای زیرلایه‌ای (غیرهندوآریایی) می‌داند (قس. کانادایی kuṇṭa «لنگ»، تلوگو kuṇṭi)، و «kunt/kund» ارمنی را وام‌واژه‌ای ایرانی می‌شمارند نه هم‌ریشهٔ موروثی. ویکی‌واژه پیوند فارسی-سنسکریت را «مشکوک» می‌خواند و به پیروی از آساتریان و آراکلوا (۲۰۰۱) پیوند با ارمنی کهن čałat «کچل، برهنه» را محتمل‌تر می‌داند. پس عنوان «هندواروپایی» برای این ریشه پذیرفتنی نیست.\",\n   \"sources\": [W + \"%DA%A9%D9%86%D8%AF\", W + \"%E0%A4%95%E0%A5%81%E0%A4%A3%E0%A5%8D%E0%A4%A0\"],\n   \"ref_check\": [\n     {\"ref\": \"IEC:588,589\", \"status\": \"supports\",\n      \"note\": \"Mann, IEC p.588 (IEC.txt line 8389, printed page marker '588' at line 8380): 'kundos \\\"stolid, stout, ponderous, stocky\\\". Arm. kunt & kund, gs knti & kndi, abl. -av \\\"bald; squat, stocky\\\"; Per. kund \\\"blunt; stupid\\\"; Hes. kundos \\\"stolid, unwavering\\\"; Fris. hont \\\"stout fellow, sturdy fellow\\\". Cf. the variant Skt. kunthah (blunt, fr. a type *kundsios or sim.)'. p.589 (line 8397): 'kuntsios (?), kundsios (?) \\\"docked, short\\\". See kund-. Skt. kunthah \\\"blunt\\\"; R. kucyj \\\"docked\\\"'. Nourai's box is a faithful summary.\"}\n   ],\n   \"consulted\": [\n     {\"src\": \"POK\", \"where\": \"POK_full.txt / POK_01-03, grep 'kundos', 'kunt-', 'kuntha'\", \"stance\": \"silent\",\n      \"note\": \"No such root in Pokorny's IEW; the word family is not treated there at all.\"},\n     {\"src\": \"WLD\", \"where\": \"WLD_band3.txt (Register), grep 'kunt', 'kunj', 'kunk'\", \"stance\": \"silent\",\n      \"note\": \"Nothing in the Walde-Pokorny index.\"},\n     {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt, grep 'kunth'\", \"stance\": \"silent\",\n      \"note\": \"Watkins' list of IE roots has no *kund-; the only hits are Germanic *kunthaz 'known' (root *gnō-), unrelated.\"},\n     {\"src\": \"SYN\", \"where\": \"Buck 15.79 'BLUNT, DULL' (SYN.txt line 27095 ff.)\", \"stance\": \"silent\",\n      \"note\": \"Buck's synonym table for 'blunt' lists Skt. atīkṣṇa- and gives no Persian or Sanskrit kund-/kuṇṭha- word, i.e. he does not treat this as an inherited IE lexeme.\"}\n   ],\n   \"nodes\": [\n\n    {\"id\": 1, \"lang\": \"Persian\", \"words\": \"kond 1; kondî\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"New Persian کُند kond 'blunt, dull, not sharp; slow' is a genuine, well-attested word (Sa'di's line quoted on the page uses it in exactly that sense), with the abstract کندی kondi 'dullness, bluntness' formed with the regular Persian abstract suffix -ī. Horn, Grundriss no.868, gives 'kund \\\"stumpf; tapfer\\\"' and compares 'skr. (bezw. prākr.) kuṇṭha- \\\"stumpf\\\"'; Hübschmann no.868 endorses the Sanskrit/Prakrit comparison and adds Balochi kunt 'stumpf, grob, einfältig' (Geiger), which shows the word is Iranian and not a recent Indian loan. What is uncertain is the deeper history: no Middle Persian *kund 'blunt' is recorded (MacKenzie's Concise Pahlavi Dictionary has only gund 'army' and *gund 'testicle'; Nyberg's glossary likewise), and Wiktionary calls the Sanskrit connection 'dubious', preferring a link with Old Armenian čałat 'bald' after Asatrian & Arakelova. So the word and its Iranian pedigree are safe; the ascent to an Indo-European *kundos is not.\",\n     \"derivation_fa\": \"«کُند» در فارسی نو به معنی «تیز نه، کودن، آهسته» واژه‌ای اصیل و پرکاربرد است (بیت سعدی در همین صفحه نیز آن را در همین معنی به کار برده) و «کندی» با پسوند اسم‌مصدرساز «ـی» از آن ساخته شده. هرن (شمارهٔ ۸۶۸) آن را با سنسکریت/پراکریت kuṇṭha- «کند» می‌سنجد و هوبشمان همین سنجش را می‌پذیرد و بلوچی kunt «کند، خشن، ساده‌دل» را نیز گواه می‌آورد؛ پس ایرانی‌بودن واژه مسلم است. اما پیشینهٔ دورترش روشن نیست: در فارسی میانه صورت *kund «کند» ثبت نشده (مکنزی و نیبرگ تنها gund «سپاه» دارند) و ویکی‌واژه پیوند با سنسکریت را «مشکوک» می‌خواند. بنابراین خودِ واژه و ایرانی‌بودنش تأیید می‌شود، ولی بردنِ آن به ریشهٔ هندواروپاییِ *kundos با احتیاط پذیرفتنی است.\",\n     \"sources\": [W + \"%DA%A9%D9%86%D8%AF\"],\n     \"ref_check\": [\n       {\"ref\": \"IEC:588\", \"status\": \"supports\",\n        \"note\": \"IEC.txt line 8389 (p.588): 'kundos … Per. kund \\\"blunt; stupid\\\"' — Mann does list New Persian kund directly under the root, as the chart draws it.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"HRN\", \"where\": \"no. 868 (HRN.txt line 7547, printed p.193)\", \"stance\": \"supports\",\n        \"note\": \"'868. kund \\\"stumpf; tapfer\\\". skr. (bezw. prākr.) kuṇṭha- \\\"stumpf\\\". Vergl. Rückert, ZDMG. 8, 280. np. kundāver hat nach Nöldeke … im Šāhnāme immer die Bedeutung \\\"stolz\\\".'\"},\n       {\"src\": \"HUB\", \"where\": \"no. 868 (HUB.txt lines 3120-3122, printed p.88-89)\", \"stance\": \"partial\",\n        \"note\": \"'Np. kund \\\"stumpf\\\" = bal. kunt \\\"stumpf, grob, einfältig\\\" (Geiger) = skr. (prakr.) kuṇṭha- \\\"stumpf\\\". Davon kund \\\"vir strenuus\\\" zu trennen, vgl. kunda, kundavar.' Hübschmann accepts the Sanskrit comparison for 'blunt' but insists the 'brave' word is a different lexeme.\"},\n       {\"src\": \"PHD\", \"where\": \"PHD.txt s.v. k- section (grep 'kund')\", \"stance\": \"silent\",\n        \"note\": \"MacKenzie has no Middle Persian kund 'blunt'; only kundāg 'magician', kundur 'frankincense', gund 'army', *gund 'testicle'.\"},\n       {\"src\": \"NYB\", \"where\": \"NYB_vol2_glossary.txt (grep 'kund')\", \"stance\": \"silent\",\n        \"note\": \"Nyberg's Pahlavi glossary has only kandak/kundā 'astrologer, sorcerer'; no kund 'blunt'.\"},\n       {\"src\": \"MON\", \"where\": \"MON_part2.txt line 26893 ff.\", \"stance\": \"supports\",\n        \"note\": \"Mo'in has 'کند … (ص.) تیغ و شمشیر و چاقو و کاردی که دم آن تیز نباشد … مق. تند، تیز' — blunt, opposite of 'sharp'; and separately 'کند [شجاع، خشن] (ص.) دلیر، دلاور، شجاع'.\"}\n     ]},\n\n    {\"id\": 2, \"lang\": \"Sanskrit\", \"words\": \"kunthah\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"Sanskrit कुण्ठ kuṇṭha is real, but its meaning is 'blunt, dull; stupid, indolent, lazy, foolish' — there is no attested sense 'strong, hero'. Nourai's gloss 'blunt, strong, hero' looks like a bridge invented to license node #3 (Persian kond 2 'hero'); Mann, the source cited, glosses it only 'blunt' (IEC p.588 'the variant Skt. kunthah (blunt …)'; p.589 'Skt. kunthah \\\"blunt\\\"'). The derivation is also disputed at a deeper level: kuṇṭha is post-Vedic, and the great formal variation across Middle and New Indo-Aryan (Turner's kuṃṭha etc.) points to a substrate origin, with Dravidian look-alikes (Kannada kuṇṭa 'cripple', Telugu kuṇṭi 'lame'); it belongs to the Indo-Aryan 'defective' word-group rather than to an inherited IE root. Mann himself only derives it from a hypothetical *kundsios 'or sim.', flagged with a question mark.\",\n     \"derivation_fa\": \"«کُنْثَه» (kuṇṭha) در سنسکریت واژه‌ای واقعی است، اما معنایش «کند، کودن، تنبل، نادان» است و معنیِ «نیرومند، پهلوان» برای آن گواهی ندارد؛ خودِ مان هم فقط «blunt» ترجمه کرده است. افزودن «strong, hero» به‌ظاهر برای پل‌زدن به گرهٔ بعدی (کُند ۲ «پهلوان») بوده است. از سوی دیگر خاستگاه واژه نیز محل تردید است: kuṇṭha پس‌ودایی است و ترنر گونه‌گونیِ گستردهٔ صورت‌های آن را در زبان‌های هندوآریایی میانه و نو نشانهٔ واژه‌ای زیرلایه‌ای می‌داند، با همانندهای دراویدی (کانادایی kuṇṭa «لنگ»، تلوگو kuṇṭi). پس ریشه‌شناسیِ هندواروپاییِ نورایی برای این گره از سوی پژوهش امروزی رد می‌شود.\",\n     \"sources\": [W + \"%E0%A4%95%E0%A5%81%E0%A4%A3%E0%A5%8D%E0%A4%A0\"],\n     \"ref_check\": [\n       {\"ref\": \"IEC:588,589\", \"status\": \"partial\",\n        \"note\": \"IEC.txt line 8389 (p.588): 'Cf. the variant Skt. kunthah (blunt, fr. a type *kundsios or sim.)'; line 8397 (p.589): 'kuntsios (?), kundsios (?) \\\"docked, short\\\". See kund-. Skt. kunthah \\\"blunt\\\"'. Mann has the word here, but glosses it 'blunt' only — never 'strong, hero' — and marks the intermediate type with a question mark.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"POK\", \"where\": \"POK_full.txt, grep 'kuntha'\", \"stance\": \"silent\",\n        \"note\": \"Pokorny does not list Skt kuṇṭha under any root.\"},\n       {\"src\": \"SYN\", \"where\": \"Buck 15.79 BLUNT, DULL\", \"stance\": \"silent\",\n        \"note\": \"Buck's entry for 'blunt' does not use Skt kuṇṭha at all (Skt. atīkṣṇa- is given instead), i.e. it is not treated as the inherited Indic word for 'blunt'.\"},\n       {\"src\": \"HUB\", \"where\": \"no. 868\", \"stance\": \"partial\",\n        \"note\": \"Hübschmann accepts skr. (prakr.) kuṇṭha- 'stumpf' as the match for Persian kund 'blunt' — but only for 'blunt', and he explicitly detaches the 'brave' sense.\"}\n     ]},\n\n    {\"id\": 3, \"lang\": \"Persian\", \"words\": \"kond 2; kondî 2; kondâvar\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"The words exist, but not by this route. (a) Mo'in (the very reference cited, MON:3088) devotes a long note to کنداور and concludes: 'کنداور with Arabic kāf (= کندا \\\"courage\\\" + ور suffix of possession) meaning brave and valiant is the correct form; گندآور with Persian gāf (= گند (=جند \\\"army\\\") + آورنده) meaning marshaller of troops, commander, is also correct' — i.e. Mo'in separates the two spellings Nourai lumps into one node, and derives گنداور from گند 'army', not from any 'hero' word. (b) The verse Nourai prints under this node is Ferdowsi's 'نگه کن سواران و گندآوران', which uses precisely the گندآور form; that word goes back to Middle Persian gund 'army, troop' (MacKenzie: 'gund [gwnd] army, troop; group, gathering'; Horn no.805 'phlv. gund \\\"Heer\\\"; arm. LW gund; arab. LW jund'), + āwar 'bringer, leader'. (c) Hübschmann no.868 states flatly that Persian kund 'vir strenuus', with kundā and kundāvar, is to be kept apart ('zu trennen') from kund 'blunt'. So deriving kond 2 / kondā / kondāvar from Sanskrit kuṇṭha 'blunt' is not supported by any source cited or consulted; Mo'in's کندا 'courage' + ور is the accepted analysis of the k- form, and گندآور belongs to gund 'army'.\",\n     \"derivation_fa\": \"خودِ واژه‌ها هستند، اما این راهِ اشتقاق درست نیست. معین در همان مدخلی که نورایی به آن ارجاع می‌دهد (فرهنگ فارسی، «کنداور») پس از بحثی مفصل نتیجه می‌گیرد: «کنداور با کاف تازی [= کندا + ور] به معنی شجاع و دلیر لغت صحیح است؛ گندآور با کاف پارسی [= گند (جند) + آورنده] به معنی لشکرآرا، سپهسالار هم درست است.» یعنی معین همان دو صورتی را که نورایی در یک گره جمع کرده از هم جدا می‌کند و «گندآور» را از «گند/جند» (سپاه) می‌گیرد. شاهدِ فردوسیِ همین گره («نگه کن سواران و گندآوران») نیز دقیقاً صورتِ «گندآور» است که به فارسی میانهٔ gund «سپاه، گروه» (مکنزی؛ هرن شمارهٔ ۸۰۵) + «آور» بازمی‌گردد. هوبشمان (شمارهٔ ۸۶۸) هم صریحاً می‌گوید کُند «مرد دلاور» با کندا و کنداور را باید از کُند «تیزنه» جدا کرد. پس گرفتنِ این واژه‌ها از kuṇṭha سنسکریت را پژوهش امروزی نمی‌پذیرد.\",\n     \"sources\": [],\n     \"ref_check\": [\n       {\"ref\": \"MON:3088\", \"status\": \"contradicts\",\n        \"note\": \"Mo'in s.v. کنداور (MON_part2.txt lines 26988-27030): 'این لغت در کتب بصورت «کنداور»، «کندآور»، «گنداور» و «گندآور» ضبط شده … نولدکه و هرن و هوبشمان آن را با کاف تازی از ریشهٔ «کند» به معنی شجاع گرفته‌اند … بنابرین کندآور باید مرکب از: کندا (شجاعت) + ور (پسوند اتصاف) باشد … نتیجه می‌گیریم: «کنداور» با کاف تازی [= کندا + ور] به معنی شجاع و دلیر لفظ صحیح است؛ «گندآور» با کاف پارسی [= کند (جند) + آور(نده)] به معنی لشکرآرا، سپهسالار هم درست است.' Mo'in also has 'کندا … (ا.) شجاعت، دلیری' (line 26976). Nothing about Sanskrit, and the گندآور spelling is assigned to جند/gund 'army'.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"HUB\", \"where\": \"no. 868 (HUB.txt line 3122)\", \"stance\": \"contradicts\",\n        \"note\": \"'Davon kund \\\"vir strenuus\\\" zu trennen, vgl. kunda, kundavar' — the 'brave man' word must be separated from kund 'blunt'.\"},\n       {\"src\": \"HRN\", \"where\": \"nos. 868 and 805 (HRN.txt lines 7547 and 7031)\", \"stance\": \"partial\",\n        \"note\": \"Horn does group 'kund \\\"stumpf; tapfer\\\"' in one entry (so he would allow Nourai's link), but he also has '805. gund, gunde \\\"Schaar, Menge; versammelt\\\" … phlv. gund \\\"Heer\\\"; arm. LW gund; arab. LW jund', and quotes Nöldeke that kundāvar in the Šāhnāme always means 'stolz/proud'.\"},\n       {\"src\": \"PHD\", \"where\": \"PHD.txt s.v. gund\", \"stance\": \"contradicts\",\n        \"note\": \"MacKenzie: 'gund [gwnd | = P] army, troop; group, gathering' — the Middle Persian base of گندآور.\"},\n       {\"src\": \"FSF\", \"where\": \"FSF.txt lines 9701, 25539, 28214 (Shahnameh glossary quotations)\", \"stance\": \"partial\",\n        \"note\": \"Noushin's Shahnameh word-list cites the verses with کنداوران/کنداوری but offers no Sanskrit etymology.\"},\n       {\"src\": \"BQT\", \"where\": \"vol. 3, BQT_v3_pages.txt line 36567\", \"stance\": \"partial\",\n        \"note\": \"'… کنداکر، کنداور. درین صورت «کندا» بمعنی شجاعت و دلیری است، مرکب از…' — Borhan/Mo'in's footnote analyses کنداور as کندا 'courage' + ور, agreeing with MON:3088 and not with Nourai.\"}\n     ]},\n\n    {\"id\": 4, \"lang\": \"Armenian\", \"words\": \"kunt, kund\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"Old Armenian կունդ kund / կունտ kunt 'bald; squat, stocky' is exactly what Mann prints at IEC p.588, so the node reports its source correctly. But the standard view is that Armenian is the borrower, not a sister branch: Armenian has taken a very large stratum of Middle Iranian vocabulary, and Wiktionary lists Armenian կունդ kund among the descendants of Persian کند, i.e. a loan from Iranian rather than an inherited reflex of a common IE *kundos. Asatrian & Arakelova's study 'Blunt, Bald and Wise: Iranian kund(-)' (Iran and the Caucasus 5, 2001) treats the whole 'blunt/bald' family as Iranian and considers a link with Old Armenian ճաղատ čałat 'bare, bald' rather than a shared IE root. The arrow root → Armenian is therefore formally possible in Mann's system but is more probably Persian → Armenian.\",\n     \"derivation_fa\": \"«կունդ/կունտ» ارمنی کهن به معنی «کچل؛ خپل، ستبر» همان است که مان در ص۵۸۸ می‌آورد، پس گزارش نورایی از منبعش درست است. اما دیدگاه رایج آن است که ارمنی در اینجا وام‌گیرنده است نه شاخهٔ خواهر: ارمنی لایهٔ بسیار بزرگی از واژگان ایرانی میانه را وام گرفته و ویکی‌واژه «کունդ» را در شمار بازماندگان فارسی «کند» می‌آورد. آساتریان و آراکلوا (۲۰۰۱) نیز این خانواده را ایرانی می‌دانند و به جای ریشهٔ مشترک هندواروپایی، پیوند با ارمنی کهن čałat «کچل» را مطرح می‌کنند. بنابراین پیکان «ریشه ← ارمنی» در دستگاه مان ممکن است، ولی محتمل‌تر «فارسی ← ارمنی» است.\",\n     \"sources\": [W + \"%DA%A9%D9%86%D8%AF\"],\n     \"ref_check\": [\n       {\"ref\": \"IEC:588\", \"status\": \"supports\",\n        \"note\": \"IEC.txt line 8389 (p.588): 'kundos … Arm. kunt & kund, gs knti & kndi, abl. -av \\\"bald; squat, stocky\\\"' — the form and gloss in the chart are Mann's verbatim.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"HUB\", \"where\": \"Persische Studien, e.g. nos. 805, 936 (HUB.txt lines 2923, 3345)\", \"stance\": \"partial\",\n        \"note\": \"Hübschmann's method throughout is to treat Armenian words of this shape as Iranian loanwords: 'Arm. gund \\\"Abtheilung eines Heeres\\\" … phl. gund'; 'arm. LW. gund \\\"Kugel\\\"'. He does not adduce Arm. kunt/kund as an inherited cognate of Persian kund.\"},\n       {\"src\": \"POK\", \"where\": \"POK_full.txt, grep 'kunt-'\", \"stance\": \"silent\",\n        \"note\": \"Pokorny records no Armenian kunt/kund under any root.\"},\n       {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt\", \"stance\": \"silent\",\n        \"note\": \"No entry.\"}\n     ]}\n   ]\n  },\n\n  # ---------------- entry 4 : Kung, Kunki, Kungios ----------------\n  {\n   \"entry\": 4,\n   \"root\": \"Kung, Kunki, Kungios\",\n   \"verdict\": \"plausible\",\n   \"modern_form\": \"Mann IEC *kungios (2) 'corner' (p.588) + supplementary *kunki-, *kunkir- (p.1635); no corresponding Pokorny root\",\n   \"note\": \"The three headwords are taken straight from Mann: IEC p.588 has 'kungios (kung-) (2) (?) \\\"corner\\\". Cf. kungios (1). Per. kunj (kung), id.; MDu. (alleged) honc \\\"corner\\\"; Du. Fris. honk, s. \\\"home\\\". (Isophonic: E hunch \\\"inspiration, idea; hunch-back\\\"; Du. honk (2) \\\"aim, target\\\")', and the Supplement, p.1635, has '(kunki-, kunkir- in Skt. kuñce, mp. \\\"bend\\\", Arm. knčiṙn \\\"knot, twist\\\" and Cz. kučera \\\"curl\\\". Per. kunǰ \\\"corner\\\" is ambig. Cf. kungios (2))'. Nourai's box is thus an accurate condensation, but two cautions must be added: Mann marks kungios (2) itself with '(?)', and everything in the Supplement is printed in parentheses, Mann's own convention for material he regards as uncertain — indeed he there calls Persian kunǰ 'ambig[uous]'. Pokorny, Walde-Pokorny and Watkins have no such root. Wiktionary's Persian کنج entry says 'Uncertain. Related to Sanskrit कुञ्चित (kuñcita, \\\"curved, bent, crooked\\\"), कुञ्चन (kuñcana, \\\"contraction\\\"), Old Armenian կնճիռն (knčiṙn, \\\"knot\\\")' — the same comparanda, with the same reservation (and, note, it cites Nourai p.255, this very page, so it is not fully independent).\",\n   \"note_fa\": \"هر سه سرواژه مستقیماً از مان گرفته شده است: در ص۵۸۸ «kungios (kung-) (۲) (؟) \\\"گوشه\\\". فارسی kunj (kung)؛ هلندی میانه honc \\\"گوشه\\\"؛ هلندی و فریزی honk \\\"خانه\\\"» و در پیوستِ ص۱۶۳۵ «(kunki-, kunkir- در سنسکریت kuñce \\\"خم شدن\\\"، ارمنی knčiṙn \\\"گره، پیچ\\\" و چکی kučera \\\"فر\\\". فارسی kunǰ \\\"گوشه\\\" مبهم است)». پس گزارش نورایی امانت‌دارانه است، اما دو نکته را باید افزود: مان خودِ kungios (2) را با «؟» می‌آورد و همهٔ مدخل‌های پیوست را در پرانتز ــ نشانهٔ تردیدِ خودِ او ــ چاپ کرده و فارسی kunǰ را «مبهم» خوانده است. در پوکورنی، والده-پوکورنی و واتکینز چنین ریشه‌ای نیست. ویکی‌واژه هم دربارهٔ «کنج» می‌نویسد «نامعلوم؛ مرتبط با سنسکریت kuñcita \\\"خمیده\\\" و kuñcana \\\"انقباض\\\" و ارمنی کهن knčiṙn \\\"گره\\\"» ــ همان شواهد و همان احتیاط (و البته خودِ همین صفحهٔ نورایی را مأخذ می‌دهد، پس یکسره مستقل نیست). ادعای نورایی با احتیاط پذیرفتنی است.\",\n   \"sources\": [W + \"%DA%A9%D9%86%D8%AC\"],\n   \"ref_check\": [\n     {\"ref\": \"IEC:588,1635\", \"status\": \"supports\",\n      \"note\": \"p.588 = IEC.txt line 8391 (local OCR); p.1635 is in the Supplement, missing from the local IEC.txt (which stops at p.1554) — read instead in the archive.org full text (item mann-an-indo-european-comparative-dictionary-1984-1987, _djvu.txt line 117849 ff.): '(kunki-, kunkir- in Skt. kuñce, mp. \\\"bend\\\", Arm. knčiṙn \\\"knot, twist\\\" and Cz. kučera \\\"curl\\\". Per. kunǰ \\\"corner\\\" is ambig. Cf. kungios (2))'. Both cited pages say what the chart says, with Mann's own question-marks.\"}\n   ],\n   \"consulted\": [\n     {\"src\": \"POK\", \"where\": \"POK_full.txt, grep 'kunc', 'kuñc', 'knčirn'\", \"stance\": \"silent\",\n      \"note\": \"No root of this shape in Pokorny.\"},\n     {\"src\": \"WLD\", \"where\": \"WLD_band3.txt (Register), grep 'kunj', 'kunk'\", \"stance\": \"silent\",\n      \"note\": \"Nothing in the Walde-Pokorny index.\"},\n     {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt\", \"stance\": \"silent\",\n      \"note\": \"Watkins' appendix has no *kung-/*kunk- root.\"},\n     {\"src\": \"SYN\", \"where\": \"Buck (SYN.txt), 'corner'\", \"stance\": \"silent\",\n      \"note\": \"Buck's synonym article for 'corner' does not use a *kung- root or the Persian word.\"}\n   ],\n   \"nodes\": [\n\n    {\"id\": 1, \"lang\": \"Persian\", \"words\": \"konj; konj-kâv\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"New Persian کنج konj 'corner, angle, nook' is old and universally attested (the Sanā'ī verse on the page, 'برو کنج غار گیر', uses it in the ordinary spatial sense), and Mo'in's lexicon confirms both of Nourai's glosses as separate homographic headwords: 'کنج (ا.) گوشهٔ (خانه و جز آن)، زاویه' and 'کنج (ص.) گوژپشت، قوزی' (hunchbacked) — so 'corner, hunchback' is not an invention. کنجکاو konjkāv is a transparent Persian compound کنج 'corner' + کاو, the present stem of کاویدن kāvidan 'to dig, probe' (Mo'in analyses it '[= کنج‌کاونده] آنکه کنجکاوی کند؛ متفحص، غوررس'), literally 'one who digs into corners' = inquisitive — exactly Nourai's paraphrase; the abstract کنجکاوی follows with -ī. What remains uncertain is only the prehistory of konj itself: Mann files it under *kungios (2) but flags it '(?)' and in the Supplement calls it 'ambig.', and Wiktionary labels the etymology 'Uncertain', comparing Sanskrit kuñcita 'curved, bent' and Old Armenian knčiṙn 'knot'. No Middle Persian antecedent is recorded in MacKenzie or Nyberg.\",\n     \"derivation_fa\": \"«کنج» در فارسی نو به معنی گوشه و زاویه واژه‌ای کهن و پرکاربرد است (بیت سنایی در همین صفحه، «برو کنج غار گیر»، در همین معنی است) و معین هر دو معنیِ مورد نظر نورایی را در دو مدخلِ جداگانه می‌آورد: «کنج (ا.) گوشهٔ خانه و جز آن، زاویه» و «کنج (ص.) گوژپشت، قوزی». «کنجکاو» نیز ترکیبی شفاف است از «کنج» + «کاو» (ستاک حال کاویدن)، و معین آن را «[= کنج‌کاونده] آنکه کنجکاوی کند؛ متفحص، غوررس» معنی می‌کند ــ درست همان «کاوش در گوشه‌ها» که نورایی نوشته است. آنچه نامعلوم می‌ماند پیشینهٔ خودِ «کنج» است: مان آن را زیر *kungios (۲) با علامت پرسش می‌آورد و در پیوست «مبهم» می‌خواند، و ویکی‌واژه ریشه را «نامعلوم» می‌داند و تنها با سنسکریت kuñcita «خمیده» و ارمنی knčiṙn «گره» می‌سنجد. در فارسی میانه نیز صورتی برای آن ثبت نشده است.\",\n     \"sources\": [W + \"%DA%A9%D9%86%D8%AC\"],\n     \"ref_check\": [\n       {\"ref\": \"IEC:588,1635\", \"status\": \"partial\",\n        \"note\": \"p.588 (IEC.txt line 8391): 'kungios (kung-) (2) (?) \\\"corner\\\" … Per. kunj (kung), id.' — Persian is indeed listed under the root, but with Mann's question mark; the Supplement p.1635 (archive.org _djvu.txt line 117855) then downgrades it: 'Per. kunǰ \\\"corner\\\" is ambig.'\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"MON\", \"where\": \"MON_part2.txt lines 26845-26857 and 26902-26905\", \"stance\": \"supports\",\n        \"note\": \"'کنج (ا.) گوشهٔ (خانه و جز آن)، زاویه' ; 'کنج (ص.) گوژپشت، قوزی' ; 'کنجکاو [= کنج‌کاونده] (ص‌فا.) آنکه کنجکاوی کند؛ متفحص، غوررس' ; 'کنجکاوی (حامص.) تفحص دقیق، غوررسی'.\"},\n       {\"src\": \"PHD\", \"where\": \"PHD.txt, grep 'kunj'\", \"stance\": \"silent\",\n        \"note\": \"MacKenzie records no Middle Persian *kunj 'corner' (only kunjid 'sesame').\"},\n       {\"src\": \"HRN\", \"where\": \"HRN.txt, grep 'kunǰ/kunj'\", \"stance\": \"silent\",\n        \"note\": \"Horn's Grundriss has no entry for kunǰ 'corner'.\"},\n       {\"src\": \"HUB\", \"where\": \"HUB.txt line 8026\", \"stance\": \"silent\",\n        \"note\": \"Hübschmann mentions only kunjid/kunjīd 'Sesam'; no کنج 'corner'.\"},\n       {\"src\": \"BQT\", \"where\": \"BQT_v3_pages.txt line 48605 (footnote to گوشه)\", \"stance\": \"partial\",\n        \"note\": \"Mo'in's footnote to گوشه glosses it 'کنج، زاویه - خلوت، خلوتگاه' and derives گوشه from Avestan gaoshaka — showing کنج is the plain synonym of گوشه, but Borhan/Mo'in give no etymology for کنج itself.\"}\n     ]},\n\n    {\"id\": 2, \"lang\": \"Sanskrit\", \"words\": \"kunče\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"The form is Mann's transcription of Sanskrit कुञ्चते kuñcate (middle-voice, 3sg.) 'bends, curves, contracts', from the root कुञ्च् kuñc- 'to bend, make crooked' — hence the participle कुञ्चित kuñcita 'curved, bent, crooked' and the noun कुञ्चन kuñcana 'contraction'. Mann prints it in the Supplement exactly as Nourai has it, 'Skt. kuñce, mp. \\\"bend\\\"' (mp. = medio-passive), so the word and gloss are right. The link to the 'corner' root is the semantic step 'bend' > 'angle, corner' — plausible in itself, but Mann himself parenthesises the whole entry and calls the Persian member 'ambig.', so this is a comparison rather than a demonstrated derivation. Skeat, independently, connects English hunch with 'Skt. kuñc, to bend', which shows the comparison has a long pedigree even where the root is not reconstructible.\",\n     \"derivation_fa\": \"این صورت، آوانگاشتِ مان از سنسکریت kuñcate (سوم‌شخص مفرد در وجه میانه) «خم می‌شود، منقبض می‌شود» از ستاک kuñc- «خم کردن» است؛ از همین ستاک kuñcita «خمیده، کج» و kuñcana «انقباض» ساخته شده است. مان در پیوست دقیقاً همان‌گونه که نورایی آورده می‌نویسد: «Skt. kuñce, mp. \\\"bend\\\"». پس واژه و معنی درست است. پیوند آن با ریشهٔ «گوشه» بر پایهٔ تحول معنایی «خمیدگی ← زاویه، گوشه» است که فی‌نفسه پذیرفتنی است، ولی چون مان کل مدخل را در پرانتز آورده و عضو فارسی را «مبهم» خوانده، این بیشتر یک سنجش است تا اشتقاقی اثبات‌شده. اسکیت نیز به‌طور مستقل انگلیسی hunch را با «kuñc سنسکریت، خم شدن» می‌سنجد.\",\n     \"sources\": [W + \"%DA%A9%D9%86%D8%AC\"],\n     \"ref_check\": [\n       {\"ref\": \"IEC:1635\", \"status\": \"supports\",\n        \"note\": \"Mann, Supplement p.1635 (archive.org full text, _djvu.txt line 117853): '(kunki-, kunkir- in Skt. kuñce, mp. \\\"bend\\\", Arm. knčiṙn \\\"knot, twist\\\" and Cz. kučera \\\"curl\\\"…)' — the form and gloss are Nourai's, verbatim.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"SKT\", \"where\": \"SKT.txt line 8969 s.v. Hunch\", \"stance\": \"supports\",\n        \"note\": \"Skeat: 'Hunch, a hump, round mass … Cf. G. Höcker, the bent back … And cf. Skt. kuñc, to bend, with kuch, to bend.' — independent use of the same Sanskrit root in this comparison.\"},\n       {\"src\": \"POK\", \"where\": \"POK_full.txt, grep 'kuñc'\", \"stance\": \"silent\",\n        \"note\": \"Pokorny does not treat Skt kuñc-.\"},\n       {\"src\": \"SYN\", \"where\": \"SYN.txt\", \"stance\": \"silent\",\n        \"note\": \"Buck does not cite kuñcita/kuñcana in his 'corner' or 'bend' articles.\"}\n     ]},\n\n    {\"id\": 3, \"lang\": \"Armenian\", \"words\": \"knčirn\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"Old Armenian կնճիռն knčiṙn 'knot, wrinkle, twist' is a real and well-attested word (still Modern Armenian կնճիռ knčiṙ 'wrinkle'), and Mann's Supplement p.1635 lists it in exactly the shape and sense Nourai prints. Wiktionary's Persian کنج entry names the same word as a comparandum. Whether it is a cognate reflex of a root *kunki- or an Armenian formation of its own is undecidable on the evidence: no Armenian etymological authority (Hübschmann, Acharyan) is quoted by Mann, the entry is in his parenthesised Supplement, and neither Pokorny nor Watkins knows the root. So the node is a legitimate report of its source, but no more than plausible.\",\n     \"derivation_fa\": \"«կնճիռն» (knčiṙn) در ارمنی کهن به معنی «گره، چین، پیچ» واژه‌ای واقعی و پرشاهد است (در ارمنی امروزی نیز کնճիռ «چین و چروک»)، و مان در پیوست ص۱۶۳۵ آن را با همین صورت و همین معنی آورده است؛ ویکی‌واژه هم در مدخل «کنج» فارسی همین واژه را برای سنجش می‌آورد. اما اینکه بازماندهٔ ریشه‌ای *kunki- باشد یا ساختی درون‌ارمنی، با این شواهد تعیین‌شدنی نیست: مان هیچ مرجع ریشه‌شناسی ارمنی (هوبشمان، آچاریان) نقل نمی‌کند و مدخل در پیوستِ پرانتزی اوست، و پوکورنی و واتکینز چنین ریشه‌ای نمی‌شناسند. پس گزارشِ نورایی از منبعش درست است، ولی بیش از «با احتیاط پذیرفتنی» نیست.\",\n     \"sources\": [W + \"%DA%A9%D9%86%D8%AC\"],\n     \"ref_check\": [\n       {\"ref\": \"IEC:1635\", \"status\": \"supports\",\n        \"note\": \"Supplement p.1635 (archive.org _djvu.txt line 117853): 'Arm. knčiṙn \\\"knot, twist\\\"' — exactly as the chart has it.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"POK\", \"where\": \"POK_full.txt, grep 'knčirn'\", \"stance\": \"silent\",\n        \"note\": \"Not in Pokorny.\"},\n       {\"src\": \"HUB\", \"where\": \"HUB.txt (Persische Studien), grep 'knč'\", \"stance\": \"silent\",\n        \"note\": \"Hübschmann's Persian Studies does not treat this Armenian word (it is not an Iranian loan for him).\"},\n       {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt\", \"stance\": \"silent\",\n        \"note\": \"No entry.\"}\n     ]},\n\n    {\"id\": 4, \"lang\": \"Dutch\", \"words\": \"konk\",\n     \"verdict\": \"transcription_suspect\",\n     \"error_in\": \"book\",\n     \"book_prints\": \"konk\",\n     \"correct_form\": \"honk (Middle Dutch honc)\",\n     \"derivation\": \"There is no Dutch word konk meaning 'corner'. Mann's entry, which is the sole reference given, reads: 'kungios (kung-) (2) (?) \\\"corner\\\" … Per. kunj (kung), id.; MDu. (alleged) honc \\\"corner\\\"; Du. Fris. honk, s. \\\"home\\\"' — the Germanic form is honc/honk with h-, the regular Germanic reflex of an IE velar (*k > Gmc. h by Grimm's law), which is precisely what makes it a possible cognate; a Dutch form with initial k- would be phonologically impossible as an inherited relative of *kung-. The printed page (PDF p.285, book p.255, image saved as data/verification/sources/refs/ocr/BOOK/285.png) does show 'konk', so the extraction is faithful and the error is Nourai's own — most likely he normalised the initial to match the root's k-. Note also that Mann marks the Middle Dutch form '(alleged)' and glosses modern Du./Fris. honk as 'home', not 'corner'.\",\n     \"derivation_fa\": \"در هلندی واژه‌ای به شکل «konk» به معنی «گوشه» وجود ندارد. مدخل مان ــ که تنها مأخذ این گره است ــ چنین است: «kungios (kung-) (۲) (؟) \\\"گوشه\\\" … فارسی kunj؛ هلندی میانه (منسوب) honc \\\"گوشه\\\"؛ هلندی و فریزی honk \\\"خانه\\\"». صورت ژرمنی با «h» آغاز می‌شود، یعنی همان بازتاب قانون‌مندِ ک هندواروپایی در ژرمنی بر پایهٔ قانون گریم (k > h)، و اتفاقاً همین است که آن را هم‌ریشهٔ ممکن می‌سازد؛ صورتی هلندی با «k» آغازین نمی‌تواند بازماندهٔ موروثیِ *kung- باشد. تصویر صفحهٔ چاپی (صفحهٔ ۲۵۵ کتاب) نشان می‌دهد که خودِ کتاب «konk» چاپ کرده است؛ پس این خطای چاپی/سهو نویسنده است، نه خطای خوانش اسکن. افزون بر این، مان صورت هلندی میانه را «منسوب/ادعایی» می‌خواند و honk امروزی را «خانه» معنی می‌کند نه «گوشه».\",\n     \"sources\": [],\n     \"ref_check\": [\n       {\"ref\": \"IEC:1635\", \"status\": \"partial\",\n        \"note\": \"The Germanic member is at IEC p.588 (line 8391), not p.1635: 'MDu. (alleged) honc \\\"corner\\\"; Du. Fris. honk, s. \\\"home\\\"'. The Supplement entry at p.1635 lists only Skt kuñce, Arm. knčiṙn and Cz. kučera. Either way Mann's form is honc/honk, never konk.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"DOZ\", \"where\": \"DOZ.txt (Dozy, Oosterlingen — Dutch words of Oriental origin)\", \"stance\": \"silent\",\n        \"note\": \"No konk/honk; the book only covers Dutch orientalisms, so it has nothing to say either way.\"},\n       {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 18247 s.v. hunch\", \"stance\": \"contradicts\",\n        \"note\": \"Klein derives English hunch from hump and cites no Dutch source at all, let alone konk.\"},\n       {\"src\": \"POK\", \"where\": \"POK_full.txt\", \"stance\": \"silent\",\n        \"note\": \"No Germanic *hunk-/*hank- 'corner' root.\"}\n     ]},\n\n    {\"id\": 5, \"lang\": \"English\", \"words\": \"hunch, hunch-back\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"English hunch is not derived from any Dutch word in current scholarship, and Mann — the reference cited — does not derive it either: at IEC p.588 he expressly puts it in a parenthesis as merely 'Isophonic: E hunch \\\"inspiration, idea; hunch-back\\\"; Du. honk (2) \\\"aim, target\\\"', i.e. a chance formal similarity, not a genealogical link. Etymonline: 'hunch (v.) \\\"raise or bend into a hump\\\", 1650s; earlier \\\"to push, thrust\\\" (c. 1500), of unknown origin. Perhaps a variant of bunch (v.)'; the noun is 1620s 'a push, a thrust', with 'hint, tip' from 1849 and 'premonition' by 1904; hunchback (1712) is a back-formation from hunchbacked (1590s). Klein p.750 — which the chart's own NOTE cites — says 'hunch, n., 1) hump; 2) a thick piece. — Prob. altered fr. hump. For a similar alteration cp. lunch, which prob. derives fr. lump. Cp. hunk.' Wiktionary makes it an 'assibilated variant of hunk', alternatively a diminutive of hump. Skeat calls it 'a nasalised form of hook' and only then compares Skt kuñc 'to bend'. So the chart's NOTE is right and the arrow it hangs on is not: the English word is of obscure native origin, first attested only around 1500-1650, far too late for an inherited IE etymon, and there is no Dutch intermediary.\",\n     \"derivation_fa\": \"در پژوهش امروزی، انگلیسی hunch از هیچ واژهٔ هلندی گرفته نشده است؛ خودِ مان هم ــ که تنها مأخذ این گره است ــ چنین نمی‌گوید: او در ص۵۸۸ آن را در پرانتز و تنها با عنوان «هم‌آوا/isophonic» کنار honk هلندی می‌نهد، یعنی شباهت آوایی تصادفی، نه پیوند نسبی. اتیمآنلاین: «hunch (فعل) \\\"برآمده کردن، قوز کردن\\\"، حدود ۱۶۵۰؛ پیش‌تر \\\"هل دادن\\\" (حدود ۱۵۰۰)، خاستگاه نامعلوم؛ شاید گونه‌ای از bunch»؛ اسمِ آن از ۱۶۲۰ به معنی «هل»، از ۱۸۴۹ «اشاره، سرنخ» و از ۱۹۰۴ «حس ششم»؛ hunchback (۱۷۱۲) اشتقاق پس‌رونده از hunchbacked (۱۵۹۰) است. کلاین (ص۷۵۰) ــ که خودِ یادداشت نمودار به او ارجاع می‌دهد ــ می‌نویسد «احتمالاً دگرگون‌شدهٔ hump، همان‌گونه که lunch از lump». ویکی‌واژه آن را گونهٔ سایشی‌شدهٔ hunk می‌داند و اسکیت صورتی خیشومی‌شده از hook. پس یادداشت نمودار درست است و پیکانی که بر آن استوار شده نادرست: این واژه بومی و دیرآیند (سدهٔ شانزدهم-هفدهم) است و واسطهٔ هلندی ندارد.\",\n     \"sources\": [\"https://www.etymonline.com/word/hunch\", W + \"hunch\"],\n     \"ref_check\": [\n       {\"ref\": \"IEC:1635\", \"status\": \"contradicts\",\n        \"note\": \"The English word appears at IEC p.588 (line 8391), not p.1635, and only as '(Isophonic: E hunch \\\"inspiration, idea; hunch-back\\\"; Du. honk (2) \\\"aim, target\\\")' — Mann's 'isophonic' label explicitly denies a derivation. (Mann's kungios (1), same page, does list 'E hunk, hunch (according to dial.)' under 'bulge, hump, mass', but that is the hump-word, not the corner-word.)\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 18247, leaf 404 ≈ p.750\", \"stance\": \"contradicts\",\n        \"note\": \"'hunch, n., 1) hump; 2) a thick piece. — Prob. altered fr. hump. For a similar alteration cp. lunch, which prob. derives fr. lump. Cp. hunk.' — confirms the chart's NOTE and excludes the Dutch route.\"},\n       {\"src\": \"SKT\", \"where\": \"SKT.txt line 8969\", \"stance\": \"partial\",\n        \"note\": \"Skeat: 'Hunch, a hump, round mass. (E.) A nasalised form of hook … And cf. Skt. kuñc, to bend' — native English origin, though he does compare the Sanskrit root.\"},\n       {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt line 92895\", \"stance\": \"contradicts\",\n        \"note\": \"Webster: 'hunch, n. [form of hump.]'\"},\n       {\"src\": \"FSD\", \"where\": \"FSD_vol2.txt line 49927\", \"stance\": \"partial\",\n        \"note\": \"Funk & Wagnalls' first sense is 'to thrust with the elbow, shoulder or fist; push suddenly; jostle; jog' — the c.1500 'push' sense Etymonline makes primary, again with no Dutch etymon.\"}\n     ]}\n   ]\n  }\n ]\n}\n\nwith open(\"/home/sfmqrb/git/rishe/data/verification/page-285.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(doc, f, ensure_ascii=False, indent=1)\n    f.write(\"\\n\")\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk285.py"
}
```


### [2026-09-06T22:05:10.179Z] TOOL RESULT

```
ok
```


## [2026-09-06T22:05:13.845Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 -m json.tool data/verification/page-285.json > /dev/null && echo \"JSON OK\"\npython3 tools/verify_check.py 285"
}
```


### [2026-09-06T22:05:16.763Z] TOOL RESULT

```
JSON OK
nodes verified: 13/13
node verdicts: {'disputed': 4, 'plausible': 7, 'confirmed': 1, 'transcription_suspect': 1}
root verdicts: {'confirmed': 1, 'disputed': 1, 'plausible': 1}
ref checks: {'partial': 6, 'contradicts': 3, 'supports': 6, 'not_checked': 1}
books consulted: {'contradicts': 8, 'partial': 17, 'silent': 17, 'supports': 7} | by book: {'HUB': 6, 'POK': 5, 'BQT': 3, 'MON': 3, 'KLN': 3, 'WEB': 3, 'FSD': 3, 'SKT': 3, 'HRN': 3, 'PHD': 3, 'LKT': 2, 'SYN': 2, 'AHD': 2, 'RCH': 1, 'PLA': 1, 'SIN': 1, 'AFM': 1, 'HJB': 1, 'NYB': 1, 'FSF': 1, 'DOZ': 1}
```


## [2026-09-06T22:05:24.080Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 - <<'EOF'\nimport json\ncited=set()\nd=json.load(open('data/verification/page-285.json'))\ndef walk(o):\n    if isinstance(o,dict):\n        for k,v in o.items():\n            if k=='sources':\n                cited.update(v)\n            else: walk(v)\n    elif isinstance(o,list):\n        for x in o: walk(x)\nwalk(d)\nidx={}\nfor line in open('data/verification/sources/web/index.jsonl'):\n    r=json.loads(line); idx[r['url']]=r\nfor u in sorted(cited):\n    r=idx.get(u)\n    print((\"OK  \" if r and r.get('status')==200 else \"MISS\"), r.get('status') if r else None, r.get('bytes') if r else '', u)\nEOF"
}
```


### [2026-09-06T22:05:25.901Z] TOOL RESULT

```
OK   200 6328 https://en.wiktionary.org/wiki/%D8%AE%D9%84%D9%86%D8%AC
OK   200 4470 https://en.wiktionary.org/wiki/%D8%AE%D9%88%D9%84%D9%86%D8%AC%D8%A7%D9%86
OK   200 3155 https://en.wiktionary.org/wiki/%DA%A9%D9%86%D8%AC
OK   200 8272 https://en.wiktionary.org/wiki/%DA%A9%D9%86%D8%AF
OK   200 7013 https://en.wiktionary.org/wiki/%E0%A4%95%E0%A5%81%E0%A4%A3%E0%A5%8D%E0%A4%A0
OK   200 4159 https://en.wiktionary.org/wiki/%E0%A4%95%E0%A5%81%E0%A4%B2%E0%A4%9E%E0%A5%8D%E0%A4%9C%E0%A4%A8
OK   200 3389 https://en.wiktionary.org/wiki/galingale
OK   200 13784 https://en.wiktionary.org/wiki/hunch
OK   200 4322 https://www.ahdictionary.com/word/search.html?q=galingale
OK   200 5494 https://www.etymonline.com/word/hunch
```


## [2026-09-06T22:05:44.894Z] AGENT

Done. `/home/sfmqrb/git/rishe/data/verification/page-285.json` written; `verify_check.py 285` reports 13/13 nodes, **0 PROBLEM lines**.

**Page 285 (book p. 255) — 3 entries, 13 nodes**
- Node verdicts: confirmed 1, plausible 7, disputed 4, transcription_suspect 1. Root verdicts: confirmed 1 (Kulanjâ), plausible 1 (Kung), disputed 1 (Kund).
- ref_checks: supports 6, partial 6, contradicts 3, not_checked 1 (AHD:539, 1975 New College ed. not open online).

**Disputed / flagged**
- *Kulanjâ* #1 Persian `xalanj, xalang` — the galangal word is Persian خولنجان/قولنجان (Laufer p.545 "Persian xawalinjān"); خلنج/خلنگ is a separate native word = heather/piebald wood (Borhan, Mo'in, Richardson; Asbaghi p.112 keeps ḫalanǧ and ḫalanǧān as two lemmas). Nourai conflated two words.
- *Kund* ROOT — Mann-only reconstruction; absent from Pokorny, Walde-Pokorny, Watkins. Skt kuṇṭha is post-Vedic/substrate (Turner), Arm. kund an Iranian loan.
- *Kund* #2 Skt `kunthah` — gloss "strong, hero" unattested (Mann glosses only "blunt"); origin likely non-IE substrate.
- *Kund* #3 Persian `kond 2 / kondî 2 / kondâvar` — MON:3088 (the cited ref) **contradicts**: Mo'in splits کنداور (= کندا "courage" + ور) from گندآور (= گند/جند "army" + آورنده); the Ferdowsi verse printed here is the گندآور word (MP *gund* "army", MacKenzie; Horn 805). Hübschmann 868: "kund *vir strenuus* **zu trennen**" from kund "blunt".
- *Kung* #5 English `hunch, hunch-back` — Mann calls it only "isophonic" with Du. honk; Etymonline "unknown origin, c. 1500"; Klein 750 "prob. altered fr. hump". No Dutch route.
- *Kung* #4 Dutch `konk` — **transcription_suspect, error_in: book**. Page image confirms the book prints "konk"; Mann's form is MDu. *honc* / Du.-Fris. *honk* (h- is required by Grimm's law). Extraction faithful. Page PNG saved to `data/verification/sources/refs/ocr/BOOK/285.png`.

**Extraction errors for the owner: none** — the JSON matches the printed page throughout (including "galinga", "konk", and the root gloss's "alpina galanga", all of which are the book's own misprints).

Note for the library: local `IEC.txt` stops at p.1554 and lacks Mann's Supplement (pp. 1573-1684), where IEC:1635 lives; I read it from the archive.org full text of the same item.
