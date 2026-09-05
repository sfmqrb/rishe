# Verification process log — verify-page-98


## [2026-09-05T14:35:48.788Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 98 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-98.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-98.json. Write /home/sfmqrb/git/rishe/data/verification/page-98.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 98` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T14:35:50.360Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T14:35:51.072Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T14:35:51.091Z] TOOL RESULT

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


## [2026-09-05T14:35:51.272Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-98.txt"
}
```


### [2026-09-05T14:35:51.285Z] TOOL RESULT

```
1	=== PDF page 98 (book page 68) ===
2	--- entry 0 ---
3	ROOT Bhru 2 -> redirect to Bher 5
4	--- entry 1 ---
5	ROOT Bhu -> redirect to Beu 1
6	--- entry 2 ---
7	ROOT Bhudh -> redirect to Bhun
8	--- entry 3 ---
9	ROOT [Indo-European] Bhugo : male animal of various kinds  (refs POK:174)
10	#1 (parent #0) [Avestan] refs=POK:174; AEF:272 | buza, bŭza : buck, goat
11	  #2 (parent #1) [Pahlavi] refs=BQT:271; AEF:272 | buc, bŭž : goat
12	    #3 (parent #2) [Persian] refs=None | boz «بُز» : goat
13	#4 (parent #0) [Germanic] refs=AHD | bukkaz : male animal
14	  #5 (parent #4) [English] refs=None | buck
15	#6 (parent #0) [Celtic] refs=AHD | bukkos : male goat
16	  #7 (parent #6) [English] refs=None | butcher
17	--- entry 4 ---
18	ROOT [Indo-European] Bhun, Bhudh : base, bottom  (refs POK:174; IEC:124)
19	#1 (parent #0) [Avestan] refs=POK:174 | bŭnô, bŭnâ : base
20	  #2 (parent #1) [Pahlavi] refs=BQT:304; AEF:288 | bun : base ; bun-dât : foundation
21	    #3 (parent #2) [Persian] refs=BQT:304; BRT:968; NYB:50; AEF:288,290 | bon 1 «بُن ۱» : base, foundation, house ; boneh «بُنه» : house, nest, shelter ; bonyâd «بنیاد» : foundation, establishment
22	#4 (parent #0) [Old English] refs=KLN:189; AHD:1510 | botm : lowest part
23	  #5 (parent #4) [English] refs=None | bottom
24	#6 (parent #0) [Latin] refs=AHD | fundus : bottom
25	  #7 (parent #6) [English] refs=None | foundation, fundamental, profound
26	
```


## [2026-09-05T14:35:54.250Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/extracted/batch/page-98.json",
 "description": "Read source JSON for page 98"
}
```


### [2026-09-05T14:35:54.286Z] TOOL RESULT

```
{
  "pdf_page": 98,
  "book_page": 68,
  "entries": [
    {
      "root": {
        "name": "Bhru 2",
        "redirect": "Bher 5"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Bhu",
        "redirect": "Beu 1"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Bhudh",
        "redirect": "Bhun"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Bhugo",
        "lang": "Indo-European",
        "refs": "POK:174",
        "gloss": "male animal of various kinds"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:174; AEF:272",
          "words": [
            {"translit": "buza, bŭza", "gloss": "buck, goat", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "BQT:271; AEF:272",
          "words": [
            {"translit": "buc, bŭž", "gloss": "goat", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": null,
          "words": [
            {"translit": "boz", "gloss": "goat", "script": "بُز"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "bukkaz", "gloss": "male animal", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "buck", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Celtic",
          "refs": "AHD",
          "words": [
            {"translit": "bukkos", "gloss": "male goat", "script": null}
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
            {"translit": "butcher", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Bhun, Bhudh",
        "lang": "Indo-European",
        "refs": "POK:174; IEC:124",
        "gloss": "base, bottom"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:174",
          "words": [
            {"translit": "bŭnô, bŭnâ", "gloss": "base", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "BQT:304; AEF:288",
          "words": [
            {"translit": "bun", "gloss": "base", "script": null},
            {"translit": "bun-dât", "gloss": "foundation", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:304; BRT:968; NYB:50; AEF:288,290",
          "words": [
            {"translit": "bon 1", "gloss": "base, foundation, house", "script": "بُن ۱"},
            {"translit": "boneh", "gloss": "house, nest, shelter", "script": "بُنه"},
            {"translit": "bonyâd", "gloss": "foundation, establishment", "script": "بنیاد"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "چو سیمرغ را بچه شد گرسنه - به پرواز بر شد دمان از بنه",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Old English",
          "refs": "KLN:189; AHD:1510",
          "words": [
            {"translit": "botm", "gloss": "lowest part", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "bottom", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "fundus", "gloss": "bottom", "script": null}
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
            {"translit": "foundation, fundamental, profound", "gloss": null, "script": null}
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


## [2026-09-05T14:35:54.949Z] TOOL CALL #4: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T14:35:54.998Z] TOOL RESULT

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


## [2026-09-05T14:36:28.805Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['POK','AEF','BQT','AHD','KLN','IEC','BRT','NYB','PHD','HRN','HUB','WLD','SYN','MON','ARY','SKT']:\n    v=d.get(k)\n    print('===',k, json.dumps(v,ensure_ascii=False)[:900])\n\"",
 "description": "Inspect refs_online entries"
}
```


### [2026-09-05T14:36:30.787Z] TOOL RESULT

```
=== POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry
=== AEF {"title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence", "kind": "catalog", "url": "https://openlibrary.org/works/OL38785552W (vol. 1, 1356) ; 2015 complete ed. «فرهنگ ریشه‌شناسی فارسی» (مهرافروز) print-only: https://www.gisoom.com/book/11154690/ ; German original: https://archive.org/details/grundrissderneu00horngoog", "lookup_hint": "Not online (searched archive.org, ketabnak, noorlib, web; only bookshop listings). Because it is a translation of Horn/Hübschmann, verify AEF citations against HRN (archive.org, see Western agent's refs; local HRN.txt) and HUB (local HUB.txt): the entry order (آ–خ) follows Horn's numbering. The 2015 complete edition was retitled 'فر
=== BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.c
=== AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt", "page_offset": "1985 Watkins ed.: lea
=== KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based l
=== IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.", "notes": "", "cites": "column/page number of Mann, An Indo-Europea
=== BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's BRT numbers are Bartholomae's COLUMN number
=== NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.", "notes": " local_files: /home/sfmqrb/
=== PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsian
=== HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.", "notes": "OCR of German Fraktur-free text is decent; Persian
=== HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.", "notes": "Built from djvu.xml (no hocr); OCR quality moderate.", "cites": "page number of Hübschmann, Persische Studien (1895)"
=== WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015.106625 (Band 3 duplicate)", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_
=== SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept head
=== MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different paginati
=== ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt"], "page_offset": "printed page = pdf page + 1
=== SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.", "notes": "Nourai says '1882-1967'; the
```


## [2026-09-05T14:36:34.563Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==183 || NR==182' POK_01.txt | head -140",
 "description": "Print Pokorny page 174 area"
}
```


### [2026-09-05T14:36:36.538Z] TOOL RESULT

```
.  bi-iost  N.  PL,  ag's.  breost,  aisl.  5?'ios^  ^Brusf^,  schwund- stufig' go^-  brusts  f.  PL,  ahd.  6?*?<5^,  nhd.  Bmist]  as.  brustian  ^knospen^ (slav.  ^bTbsU  Jvnospe^),  nhd.  Brös-chen  (aus  dem  md.)  , Brustdrüse  des Rindes';  schwäb.  Brüste,  bair.  Brilsel,  Briesel,  Bries  ds.,  dän.  brissei, scliwed.  halfbräss,  mit  Ä:-Suffix  dän.  bryske,  engL  brisket  ^Brust  der  Tiere^
AisL  briösk  ^Knorpel^,  mhd.  h-üsche,  nhd.  Brausche  ^Beule^^  nhd.  diaL hrausche,  brauschig  ^turgidus^  wulstig^^  brauscJien  ,aufschwellen^
Russ.  brjücho  ^Unterleib,  Bauch,  Wanst^,  diaL  brjüchnuth  , weichen, quellen,  anschwellen^,  cech.  alt.  brück,  bfucho,  heute  brich,  bficho  ,Bauch* usw.  {*bhreuso-s,  -m);
hierher  auch  klr.  brost'  f.  dial.  brost  m.  ,Knospe',  hulg-.  b')i,s(t)  m. jjüngere  Sprossen'^,  skr.  brst  m.  ds.,  bi'stina  ,Laub^
WP.  II  197 f.,  Feist  107  f.,  108  f.
2.  bhreu-s-  ,zerbrechen,  zerschlagen^  zerkrümeln  u.  dgV,  Erw.  von  1.  bhrmi-.
Alb.  breshen,  bresher  ,HageP,  wenn  eig-.  ,Kürnchen,  mica^  (^  =  i^^o-  ^'0? lat.  frustum  ,ein  Brocken,  Stückchen,  Bissen^  (aus  *bhrus-to-)'^
air.  brau  , zerschmettere,  zerschlage^  {*bhrüsiö,  gall.  brus-,  frz.  bruiser),  mir. brüire,  brüile  , Bruchstück^,  bruan  ds.,  bruar  ,Bruchstücke^,  brosna  (*brus- tonio-)  ,Reisig'bündeF,  galL  *bruskiä  ,Gestrüpp',  afrz.  broce  ds.,  mir.  brusc ,Krümchen*  usw.;  air.  bronnaim  ,schädig"e^  (*bhrusnämi)  (Subjunktiv  robria von  *bris-  ,brechen^  entlehnt,  s.  unter  bhrei-)]  mcymr.  breu,  ncymr.  brau jgebrechlich^,  mcorn.  bre^o  ,g*ebrochen^  (*bhrönso-)]  mbret.  briisun  ,Krüm- chen^  (*brous-t-)]
ags.  briesan  (^brausjan),  brysan  (*brüsjan)  ,zerbrechen  trans.,  zerschlagen^, engl,  bruise  ,quetschen^,  wahrscheinlich  auch  ahd.  brösma,  mhd.  brösem, bröseme,   brösme  ,Brosame,  Krume,  Bröckchen^;   ags.   brosnian   ,zerfallen^
WP.  II  198  f.,  WH.  I  553.
3.  bhreus-,  bhrüs-  ,brausen,  wallen,  rauschen,  hervorquellen  oder  -sprießen,
sich  bauschen,  Büschel,  Gestrüpp  u.  dgl.^,  besonders  in  germ.  Worten;
vielleicht  zu  1.  bhreu-s-]  auch  eine  jüngere  Schallvorstellung  (ähnlich
skr.  brüjim,  brujiti  ,summen,  von  einer  Menge  Bienen^,  Berneker  89)
kann  mitgewirkt  haben. Mhd.  briisen  , brausen',  brüs  ,das  Brausen^  ndd.  brüsen,  ,brausen,  sieden; eihg    sein    (von    Menschen);    sich   ausbreiten,   neue   Triebe   machen   (von Pflanzen);   besprengen,  bespritzen'    (vgl.  nhd.  Brause)  (daraus   dän.  bruse
172  9
ds.),  ndl.  bruisen,  früher  bruischen  ,scliäumen^  brausen', 
 ndd.  brüsken  da? mhd.  bräsche  ^Brause,  Wasserbrause^  aschwed.  brüsa  ,einherstürmen<i norw.  mdartl.  brösa  ^SturmböeS  aisl.  brusi  ^Ziegenbocke  isl.  bruskr  ^Büschel Besen^  engl,  brush  .Bürste,  Pinsel,  Quast,  Schwanz  (des  Fuchses/,  bi-us) loood  ,Gebüsch,  Gestrüpp^  mengl.  bruschen,  engl,  to  brush  ,mit  Kraft  sic| stürzen'^,  norw.  dial.  brauska^  bruska  und  brausta,  brusta  ,sich  Ram machen,  sich  gewaltsam  hervordrängen';  schwed.  bruska  ,knistern,  lärmeu'J
Mit  germ.  Hruska-z  ,GestrüppS  Hruskan  ,knistern'  {-sk-  kann  idg.  z^ sein)  vergleicht  man  die  baltoslav.  Gruppen  lit.  bruzgai  PI.  ,Gestrüppf briauzgä  ,Schwätzer',  bruzgii,  4ti  ,rascheln',  russ.  brjuzgdju,  -dth  ,murmeln< brjuzzdth  ,brummen,  murren,  knurren'  usw.;  doch  sind  die  Verba  vielleichj eine  erst  baltoslav.  Schallbildung.  Wegen  der  germ.  Bed.  ,spritzen'  is vielleicht  andererseits  russ.  bryzgaju,  -ath  ,spritzen,  sprühen'  usw.  zu' vergleichen.
WP.  II  199  f.,  Trautmann  38.
bbroisqo-,  bhrisqo-  ,herb  von  Geschmack'.
Russ.-ksl.  obrezgnuti,  obrhzgnuti  ,sauer  werden',  cech.  bresk  ,herber  Ge-^^ schmack',  poln.  brzazg  ,unangenehmer,  herber  Geschmack;  üble  LauneVgl^ russ.  brezgdth  (alt  brezgati)  ,sich  ekeln' ;  zunächst  zu  norw.  bj^isk  ,bitterer  ^^: Geschmack',  brisken  ,bitter,  herbe';  wohl  zu  bhrei-  ,schneiden'  (wie  mndl.  Ji; brine  ,Salzwasser').  V.
WP.  II  206.
j.  bhrü'  , Augenbraue',  z.  T.  mit  anlautendem  Vokal,  idg.  o-  oder  a-  (vollere  v Wurzelform?);  nach  Persson  Beitr.  17  liegt  ein  verdunkeltes  Kompo-J^; sitionsglied  "^oku-  ,Auge'  (mit  Kons.-Assimilation)  vor.  y'
Ai.  bh'ü-h  f.,  Akk.  bhrüv-am  ,Braue',  aA^  brvat-  f.  (Du.)  ,Brauene  npers.  T ehm,  brü  ds.  (Hübschmann  lA.   10,  24);
gr.  öq)Qvg,  -vog  f.  ,Braue',  übertragen  .erhöhter  Rand,  Hügelrand*  (nach  | Meillet  BSL  27,  129 f.  mit  griech.  Vokalprothese?);
maked.  dßQOvreg  ,dcpQveg'  (von  Kretschmer  Einl.  287  in  äßqovfeg  geän- dert; von  Meillet,  s.  Boisacq  733  Anm.  3,  wegen  der  anderweitig  bezeugten Form  äßqoxeg  und  wegen  av.  brvat-  festgehalten);
mir.  brüad  Gen.   Du.,  bräi,  bröi  Nom.  Du.  f.  ,Brauen'  (zum  Diphthong  W s.  Thurneysen  Grammar  199),  air.  forbru  Akk.  PL  (*bhrüns  :  A
```


## [2026-09-05T14:36:42.451Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"bhudh\\|bhug\\|bhü.g\\|bhu.g.o\\|Bock\" POK_01.txt | sed -n '1,60p'",
 "description": "Grep Pokorny for bhugo/bhudhmen"
}
```


### [2026-09-05T14:36:42.508Z] TOOL RESULT

```
189:Gf.  «1?,  -y(^9  ,Ziege^  arm.  aic  , Ziege';   tiefstufig  n,v.  izaena-  ,aus  Leder* (eio-entlich  ,aus  Ziegenleder'  wie  gr.  aXysiog^  vgl.  die  gleichen  Bedeutungs- rerhältnisse  bei  *ago-  ,Bock').     Vielleicht  orientalisches  Kulturwort. WP.  I  8,  Specht  KZ.  66,  13.
1451:Ein  idg.  Nebeneinander  von  bhäug-  (:  bhdvg-  :  bhug-)  und  bhäg-  ist  äußerst unwahrscheinlich;  vgl.  W.  Schulze  KZ.  27,  428  =  Kl.  Sehr.  55.
2133:cymr.    bodd   (*bhudha)   , freier  Wille,    Zustimmung',   corn.    both  , Wille'
2139:Mit  ü  (vgl.  Hirt  Idg.  Gr.  II  96):  got.  anabüsns  f.  , Gebot'  (^-bhudh-sni-), as.  ambüsan  f.  ds.,  ags.  bysen  f.  , Beispiel,  Vorbild',  aisl.  bysn  n.  ,Wunder' (aus  ,* Warnung'),  bysna  ,vorbedeuten,  warnen';
2161:Ai.  bhujati  ,biegt,  schiebt  weg',  bhugnd-h  ,gebogen',  bhüja-h  ,Arm',  bhujä ,Windung,  Arm',  bhögd-h  ,Windung  einer  Schlange;  Ring'  (:  ahd.  boug)] nis-bhuj-  ,schieben',  Pass.  ,sich  drücken,  entwischen';
2162:vielleicht  hierher  alb.  bute  ,weich'  aus  *bhug{h)-to-  ,biegsam';
2531:bhudh-m(e)n     ,Boden^;     einzelsprachlich    teils     zu     *bhudh-mo-,     teils .  i^ *bhudh-no-j  daneben  mit  schon  idg.  Metathese  *bhundho-  >  *bhnnd(A
2534:Maked.  ON  TLvöva  (*bhudhna),  dissimil.  Kvöva?
2538:hhügO'Sf  Koseform  bhukko-s  ,Bock^  (fem.  auf  -ä  ,Ziege^).
2539:Zigeun.  biczni  ,Ziege'^;  av.  büza  m.  , Ziegenbock*",  npers.  buz  ,Ziege^ ,Bock^;
2541:mir.  bocc,  pocc,  nir.  boc,  poc,  cymr.  bwch,  com.  boch,  bret.  bouch ,Bock^,  dazu  mir.  boccänach  ,Gespenst^;
2542:germ.  '^bukka-  (nach  Pedersen  Litteris  7,  23  f.  aus  dem  Kelt.  entlehnt?) in  aisl.  bukkr,  bokkr,  bokki,  ags.  bucca,  nengl.  buckj  ahd.  mhd.  boc,  -ckeSf nhd.  Bock.
4815:unklar  ist  thrak.  eßqog  ,Bock^
4868:2,  er-,  eri-  ,Bock;  Schaf,  Kuh,  Damtier*^;  vielleicht  ursprünglich  ,Horntier'.    "^
4873:in  apr.  eristian  ,Lämmchen',  lit.  {j)erasj  lett.  jers  ,Lamm^,  litt,  mend  ^ , Lammfleisch'  =  russ.-ksl.  jarina  ,Wolle',  usw.,  sind  wohl  bsl.  *eTO': ,Bock'  und  *jörä-  ,Jahr'  (s.  oben  S.  297)  vermischt  worden;
4874:ahd.  irah  ,Bock'  usw.  ist  aus  lat.   hircus  entlehnt.
5024:ai.  drsati  ,fließt';  ferner  mit  der  Bed.  ,männlich'  (aus  ,benetzend,  Samen ergießend')  ai.  fsa-JÄa-Ä  , Stier',  aja-rsahhd-h  , Ziegenbock',  av.  apers.  arsan ,Mann,  Männchen',  gr.  hom.  ^qotjv,  att.  ^qqtjv,  ion.  äol.  kret.  eqotjV  (ohne J^- !)  , männlich'  (dazu  "^aQvrjJ^ög,  hom.  dgreiög  , Widder'  =  att.  äovecjg,  äol. dQvrjadsQ  f.,  dazu  dQvsvo)  , mache  einen  Luftsprung,  tauche',  eigentlich  ,mache einen  Bocksprung',  dcQvevTrjQ  ,wer  einen  Purzelbaum  schlägt,  einen  Luft- sprung macht',  Lit.  bei  Boisacq  u.  dqvsiög  und  dQve.vTTjQ  Nachtr.),  wohl auch  ahd.  or[re]huonj  anord.  oo^re  ,Auerhahn'  (daraus  durch  Kreuzung  mit ahd.  ür,  ürohso  das  mhd.  ürhan,  nhd.  Äuerhahn).
```


## [2026-09-05T14:36:46.136Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2520,2560p' POK_01.txt",
 "description": "Print Pokorny bhudh-men / bhugos context"
}
```


### [2026-09-05T14:36:46.175Z] TOOL RESULT

```
(vgl.  dort  zur  Bed.  ai.  bhdrvati  ,kaut,  verzehrt^,   auch  bsl.   *bhreu-q-,
-k-  ^darüberstreifen,  abbröckeln').
Lat.  früx,  -gis  f.  ,Fruchf  ==  umbr.  Akk.  PL  frif^fri  ,fragesS  \^i.  frügl
(Dat.  *,zum  Gebrauche^  =)  ,tauglich^,  fruorj  -i,  früctus  und  fruitus  siim
.genieße'^   (aus  *früguor,   das  für  *frügor   eingetreten   ist?),  früniscor  _,ge-
nieße'  {^früg-nlscoi^,  frümentum  ^Getreide',  osk.  fruktatiuf  (^frügetätiöns)
,früctus^
Got.   brükjan,    ahd.    brühhan,    as.    brükan,    ags.  brücan   ,brauchen^^   got. brüksj  ahd.  brühlii,  ags.  bryce  ,brauchbar^ WP.  II  208,  WH.  I  552  f.
i
174
hhrugh-no-  ^Zweig^  Stengel^  vielleicht  in   Beziehung-  zu   hlireii-  ,sprießenc Cymr.    hrioyn-en   f.    ,Binse^;   acorn.    brunnen   gl.    juncus^   scirpus^,  brej hroenn-enn  ds.  (aus  urk.   *hrugno-)]  ags.  hrogn{e)  f.,  ^Zweig,  Busch^,  noi* dial.  hrogn{e)  ^Baumzweig,  Kleestengel,  Himbeerstrauch^ WP.  II  208.
bhudh-m(e)n     ,Boden^;     einzelsprachlich    teils     zu     *bhudh-mo-,     teils .  i^ *bhudh-no-j  daneben  mit  schon  idg.  Metathese  *bhundho-  >  *bhnnd(A
Ai.  budhnd-h  ,Grund_,  Boden^;  av.  Mnö  ds.  (*bJiundhno-),  daraus  ent lehnt  arm.  bun  ds.,  während  arm.  an-dund-lc  ^Abgrund^  aus  *bhundl assimiliert  scheint.  Aus  uriran.  *bundhas  stammt  tscherem.  pundas  ^Boden^
Gr.  Ttv&^rjv  (*cpvd'-)  m.  ,Boden,  Fuß  eines  Gefäßes^  nvvöa^  m.  ds.  (f (pvvda^  nach  Ttv-d-f-ii^v,  Schwyzer  Gr.  Gr.  I  71,  333).
Maked.  ON  TLvöva  (*bhudhna),  dissimil.  Kvöva?
Lat.  fundus,  -l  m.  ,Boden  eines  Gefäßes,  Grund^  {*bhundhos)j  profundvS\ ,t\Qi'  =  mir.  bond,  bonn  m.  ^Sohle,  Grundlage,  Stützet
Ahd.  bodam,  nhd.  Boden,  as.  bodom,  ags.  *bodm  >  mengl.  bothem  ml neben  ags.  botm  m.  >  engl,  bottom  und  ags.  bodan  ,Boden,  Grund^,  an.^ botn  ,Boden^,  ags.  bydme  ,Schiffsboden^  neben  bytme,  bytne  ds.,  aisl.  bytna ,m  einen  Boden  enden^,  mit  unklarem  Dental  Wechsel;  es  scheint  ein  urgerm. *bupma-  zugrunde  zu  liegen,  das  wohl  analogisch  zu  erklären  ist;  vgl. Petersson  Heterokl.  18,  Sievers-Brunner  167,  Kluge ^^  unter  siedeln.  Über nhd.  Bühne,  ursprgl.  ,Bretterboden',  angebl.  aus  germ.  *buni,  idg.  Hudhniä, s.  Kluge  ^^  unter  Bühne.
WP.  II 190,  WH.  I  564f.,  867,  Porzig  WuS.  15,  112 ff.  (dagegen  Kretschmer Gl.  22,  116);  vgl.  auch  Vendryes  MSL.  18,  305ff.
hhügO'Sf  Koseform  bhukko-s  ,Bock^  (fem.  auf  -ä  ,Ziege^).
Zigeun.  biczni  ,Ziege'^;  av.  büza  m.  , Ziegenbock*",  npers.  buz  ,Ziege^ ,Bock^;
arm.  buz  ,Lamm^;
mir.  bocc,  pocc,  nir.  boc,  poc,  cymr.  bwch,  com.  boch,  bret.  bouch ,Bock^,  dazu  mir.  boccänach  ,Gespenst^;
germ.  '^bukka-  (nach  Pedersen  Litteris  7,  23  f.  aus  dem  Kelt.  entlehnt?) in  aisl.  bukkr,  bokkr,  bokki,  ags.  bucca,  nengl.  buckj  ahd.  mhd.  boc,  -ckeSf nhd.  Bock.
Das  im  Konsonantismus  abweichende  ai.  bukka-h  ,Ziegenbock^  (unbelegt) ist  wohl  von  bukkati  ,bellt^  (s.  unter  1.  beu-,  bu-)  beeinflußte  hypochoristische Umbildung  eines  *bhüja-  =  av.  büza-.  Auch  npers.  dial.  boca  ,junge  Ziege', päm.  buc,  bü^  scheinen  Ergebnis  ähnlicher  Umbildung  zu  sein.
WP.  II  189  f.,  Pedersen  Litteris  7,  23  f.,  Martinet  Gemination  182.
D.
dS'  .Hüssig-,  fließen^  dänu-  f.  ,Fluß^
Ai.  dä-na-  n.  .die  beim  Elefanten  zur  Brunstzeit  aus  den  Schläfen uuellende  Flüssigkeit^,  dd-nu-  n.  f.  jede  träufelnde  Flüssigkeit,  Tropfen, Tau^7  av.  dä-nu-  f.  ,Fluß,  Strom*^,  osset.  don  ,Wasser,  Fluß^;  russ.  FIN  Don^ crräcisierter  skyth.  FIN  Tava'ig]  die  russ.  FIN  Dniepr  und  Dniestr,  alt  Dana- pris  und  Danastius  aus  skyth.  *Dä7iu  apara  ,hinterer  Fluß^  und  *Dänu nazdya-  ^vorderer  Fluß^;  av.  YN  Dänavö  Fl.  ,Flußanwohner^  (im  Rgveda Zu  Wasserdämonen  geworden,  fem.  GN  Dänu-),  skyth.  Nomadenvolk,  auch in  Griechenland,  daher  (?)  gr.  VN  Javaoij  ägypt.  Danuna ;  mit  Formans  -mo- arm.  tamuk  ,feucht,  benetzt^,  tamkanam  fyQalvu),  madefio^  und  vermutlich o-r.  ör]fj.6g  (urgr.  Q  oder  r]?)  ,Fett  von  Tieren  und  Menschen^,  womit  alb. dhj ame  yFettj  Speck,  Talg^  in  noch  nicht  geklärter  Weise  zusammenhängt; das  Fett  kann  als  das  beim  Braten  flüssig  werdende  benannt  sein  (vgl. aksl.  loj  ,adeps'^  :  lijati  ,gießen^).  Hierher  auch  kelt.  Dänuvius  ,Donau'^, gall.  ON  Condäte  ,Confluens^;  sechs  engl.  Fl  Don  (*dänu-)j  cymr.  FIN Donwy  (*dänuuia).
Benveniste  stellt  zu  arm.  tam-uk  noch  hett.  dame{ii)k-  ,als  Regen  fallen' (BSL  33,  143).  -
WP.  I  763,  M.Förster  Tkemse  145 f.,  Kretschmer  Gl.  24,  1  ff.,  15 ff., Mel.  Pedersen  76  ff.,  Benveniste  BSL  33,  143.
da  :  dg-  und  däi-  :  d9i  :  di-  ,teilen,  zerschneiden,  zerreißen',  ursprgl.  athemat. Wurzelpräsens;    Nominalbildungen    dä-mo-s  f.  ,Volksabteilung',   dä- ter-   ,Zerleger',   dä-tro-m  ,Zugeteiltes',   dä-tu-   ,Teil',   ddi-lO'  ,Teil-, di-t-  ,Zeitabschnitt'. Ai.  däfi,  dydti  ,schneidet  ab,   mäht,   trennt,  teilt',  Partiz.  dind-h,  ditd-hj komponiert  ava-ttah  ,abgeschnitten',  diti-h  ,das  Verteilen',  dänam  ,das  Ab- schneiden', dändm  n.  , Verteilung,  Teil',  dätu  n.  ,Teil',  dätdr-  m.  (=  Sai- 'TQÖg)    ,Schnitter',    däträm    , Zugeteiltes',    dätram    n.    ,Sichel',    npers.    dära ,Gehalt',  das  ,Sichel';  ai.  dayä  ,Teilnahme,  Mitgefühl'  =  ddyate  (^ddi-etai) ,teilt,  nimmt  Anteil,  hat  Mitgefühl;  zerstört'.
gr.  daioiiai  med.  ,teile,  verteile'  mit  wohl  nach  Fut.  daiaoi  und  den folgenden  Worten  bewahrtem  i  (lautgesetzlich   ddrjTat  Konj.  0  375  ,wird
176
zerstört);  daig^  -rög,  dairrj,  hom.  auch  daityq,  -voq  ,Portion^  Mahl^  Opfer'  (; dätu)]    SairvfKbv  ^Gast'  (als  ^dem  Mahle    beiwohnend'),   dairgög  ,der   Y^ Schneider' (:  ai.  c^ä^ar-),   daitgöv  jPortion^  (:  Si.i.  dätrdm]    das   ai   dieser  i Worte  ist  teils  lautgesetzlich  —  äi,  di  — ,  teils  analogisch,  wie  im  kr? Perf.    dedaia^ai    zu    öarso^uaL,    vgl.    auch    kret.   daTaig    ^Teilung',    xa^? daiaxal  ^Verteiler  von  Früchten'),  daivvj^i  ,bewirte^  wohl  auch  Salftcov ,Gott,  Göttin;  Geschick'  (eigentlich  ,zuteilend;  oder  ,Totengott  als  LeicheJ fresser',  Porzig  IF.  41,  169 ff.,  Kretschmer  Gl.  14,  228 f.;   über  des  Arcl lochos  daliJ,cov  ^darjf.Lcov''  s.  u.  *dens-  ,hohe   Geisteskraft');    öalZw,  Fut.  -[ Aor.  -fa  ,teilen,  zerschneiden,  zerstören'  (auf  Grund  eines  *dä-J^6-g  ,z^ schnitten,  zerstört'),  U-öaxog'  dtöialQsrog  Hes.y  ödvog  n.  ,Zins,  Wucher' (s Grund  eines  Partiz.  *dd-n6-s  =  ai.  dind-hj  vgl.  ddvag'  fisglöag)]
gall.  arcanto-danos  ,monetarius'  als  ,das  Silber  verteilend'.
Mit  Formans  -mo-  :  dämos  f.  ,Volk' :  gr.  dfjf.Log,  dor.  öänog  m.  ,(Voll abteilung)  Volk,  Gebiet;  in  Atben  der  einzelne  Gau',  air.  däm  f.  ,Gefolj Schaft,  Schar',  acymr.  dauii  ,cliens',  ncymr.  daw^  daiof  ,Schwiegersohn4 offenbar  alter  fem.  o-Stamm;  dazu  hett.  da-ma-a-is  (damai§?)  ,ein  Andere Fremder',  aus  ,*fremde  Leute',  ursprgl.  ,*Volk',  Pedersen  Hitt.  51  ff.
Mit  Formans  -lo-  vielleicht  aksl.  däh  ,Teil'  (*ddi-lo-)  (s.  unter  *di , spalten');  über  air.  fo-dälim  usw.  s.  ebendort.  Hierher  gehört  wohl  auci got.  dails  ,Teil',  runeninschr.  dali]lipun  ,teilten',  aisl.  deillj  ags.  dcel,  ahc teil  m.  ,Teil';  aisl.  deila  f.  ,Teilung,  Zwiespalt',  ahd.  teila  f.  ,Teilun^ aisl.  deila j  ags.  döelan,  ahd.  teilan  ,teilen'  usw.  Sie  können  kaum  aus  dei SlaA^,  wohl  aber  aus  dem  Ven.-IUyr.  stammen,  da  die  Wzlform  "^ddi-  ii südillyr.  PN  Dae-tor  bezeugt  ist.  Eine  Nebenform  idg.  dhdi-  neben  ddi Aväre  unglaubhaft.
Mit  Tiefstufe  di-  :  arm.  ti.  Gen.  tioy  ^Alter,  Jahre,  Tage,  Zeit'  {*di-t[^ oder  *dl-to-y  "^di-tä),  ahd.  zU  f.  (n.  Isidor),  as.  ags.  tid,  anord.  tid  f.  ,Zeit Stunde'  {*tip-,  idg.  *dl-t-,  ursprgl.  ,Zeitabschnitt'),  dazu  anord.  fidr  ^üblich^ häufig',  ags.  tldan  ,vorfallen',  anord.  tida  ,trachten,  streben';  anord.  tl-i ,zerpflücken,  einzeln  herausnehmen,  ausscheiden,  reinigen';
über  got.  til  ,passend'  usw.  s.  unter  2.  ad-,  über  got.  dails  unter  3.  <ZeZ;|
hierher    dagegen    ahd.   zlla   ,Reihe,    Linie'^    westfäl.    tue   ,Garbenreihe';J nhd.  Zeile,  wohl  aus  *tld-ld-.
p-Er Weiterung  däp-,  dQp-:  dop-no-,  -ni-  , Opfermahl': ai.  däpayati  ,teilt';  arm.  taun  (*dap-ni-)  ,Fest';  gr.  ddjtTü)  {*da7ti(ü)\ .zerreiße,  zerfleische,  zerlege',  mit  Intensivredupi.  Sagdamü)  ,zerreiße, {yiTTjfAaTa)  verprasse',  öanavri  f.  ,Aufwand,  besonders  aus  Bewirtung  (;  dafi} erwachsender',  dartavog  ,verschwenderisch',  öartaväa}  ,wende  auf  (daraus^ lat.  dapinö  ,tische  auf),  öaipdög  (Empedokles),  öayjdrjg  ,(*verschwenderisch)j
```


## [2026-09-05T14:37:04.748Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD bhugo/bhudh ===\" && grep -n \"bhūgo\\|bhugo\\|bhū-go\\|bhudh-\\|bhudh\" AHD_watkins1985.txt | head -20",
 "description": "Grep AHD Watkins"
}
```


### [2026-09-05T14:37:04.800Z] TOOL RESULT

```
=== AHD bhugo/bhudh ===
345:bhudh-
347:bhudh-. Bottom, base. (The precise preforms of the words listed below are obscure.) 1. Old English botm, bottom: Bottom. 2. Dutch bodem, (ship’s) bottom: BOT- TOMRY. 3. Latin fundus, bottom, base: FOND?, FOUND!, FOUNDER, FUND, FUNDAMENT, FUNDUS; LATIFUNDIUM, PROFOUND. [Pok. bhudh- 174.]
348:bhugo-. Male animal of various kinds; stag, ram, he-goat. 1. Germanic *bukkaz (possibly borrowed from the Celtic form in 2. below) in: a. Old English buc, bucca, stag, he-goat: BUCK}; b. Middle Dutch boc, bok, buck: BLEs- BOK, BONTEBOK, SPRINGBOK, STEENBOK; C. Old High German boc, buck: GEMSBOK. 2. Celtic *bukkos, he-goat, in Old French boc, buck: BUTCHER. [Pok. bhiigo-s 174.]
1309:BITE bheid- BITTER bheid- BITTERN! beu-2 BITUMEN gWet-1 BIVOUAC ambhi, weg-2 BLACK bhel-1 BLACKMAIL méd- BLADDER bhié-2 BLADE bhel-3 BLAIN bhlei- BLAME bha-2 BLANCH bhel-1 BLANCMANGE bhel-1 BLAND mel-1 BLANDISH mel-1 BLANK bhel-1 BLANKET bhel-1 BLARE bhié-1 BLASPHEME bha-2 BLASPHEMOUS bha-2 BLAST bhlé-2 -BLAST melst- BLASTEMA melst- BLASTO- melst- BLASTULA melst- BLATHER bhlé-2 BLAZE! bhel-1 BLEACH bhel-1 BLEAK! bhel-1 BLEAK? bhel-1 BLEAT bhlé-1 BLEMISH bhel-1 BLENCH! bhel-1 BLEND bhel-1 BLENDE bhel-1 BLENNY mel-1 BLESBOK bhel-1, bhugo- BLIND bhel-1 BLINDFOLD bhel-1 BLINI mele- BLINTZ mele- BLISTER bhlei- BLITE mele- BLITZKRIEG bhel-1, gwere-2 BLOAT bhieu- BLOND bhel-1 BLOOM! bhel-3 BLOOM? bhel-3 BLOSSOM bhel-3 BLOW! bhié-2 BLOW3 bhel-3 BLUE bhel-1 BLUNDERBUSS (s)tene- BLUSH bhel-1 BOARD bherdh- BOAST! beu-1 BOAT bheid- BOATSWAIN bheid- BOCACCIO beu-1 BODE! bheudh- BODEGA dhé-1 BODHISATTVA bheudh-, es- BoER bheue-
1313:BOLD bhel-2 BOLE! bhel-2 BOLL bhel-2 BOLLIX bhel-2 BOLOMETER gW¥ele-1 BOLSHEVIK bel- BOLSTER bhelgh- BOLT! bheld- BOMB bamb- BOMBARD bamb- BONANZA deu-2 BONBON deu-2 BOND bhendh- BONDAGE bheue- BONHOMIE deu-2, dhghem- BONITO deu-2 BONNE deu-2 BONNYCLABBER band- BONTEBOK bhugo- BONUS deu-2 BOOBY baba- BOODLE bheue- BOOK bhago-
1314:BOOM? bheue- BOON! pbha-2 BOON2 deu-2 BOOR bheue- BOOT? bhad- BOOTH bheue- BORDELLO bherdh- BORDER bherdh- BORE! bher-2 BORE’ bher-1 Boreas gWero-1 BOROUGH bhergh-2 BORROW bhergh-1 BORSCHT bhar- BOSCAGE busk- BOSOM beu-1 BOTH ambh6o BOTHRIUM bhedh- BO TREE bheudh- BOTTOM bhudh- BOTTOMRY bhudh- BOTULIN gWet-3 BOTULINUM gWet-3 BOTULISM gWet-3 BOUCLE beu-1 BOUGH bhaghu- BOUILLABAISSE beu-! BOUILLON beu-1 BOULDER bhel-2 BOULE! gWele-1 BOULE? beu-! BOULEVARD bhel-2, werg-
1324:BRIO gWere-2 BRIOCHE bhreg- BRISANCE bhréi- BRISTLE bhar- BRITTLE bhreu-1 BRONCHIECTASIS  ten- BRONCHO- gWere-4 BRONCHUS gWere-4 BRONTOSAUR bhrem-! BROOD bhreu-2 BROOK? bhriig- BROOM bhrem-2 BROTH bhreu-2 BROTHEL bhreu-' BROTHER bhrater- BROW bhri- BROWN bher-3 BROWSE bhreus-1 BRUIN bher-3 BRUISE bhreus-2 BRUMAL mregh-u- BRUNET bher-3 BRUT gWere-2 BRUTE gWere-2 BUBO beu-! BUCCAL beu-1 BUCEPHALUS gWou- BUCK! bhugo- BUCKAROO wak- BUCKBOARD beu-! BUCKLE! beu-! BUCKLE? beu-1 BUCKSHEE bhag-' BUCKWHEAT bhago- BUCOLIC gou-, kWel-1 BuppHA bheudh- BUDGET bhelgh- BUDGE! beu-1 BUGLE! gWou- BUGLOss gldgh- BUILD bheue- BULGE bhelgh- BULIMIA gWou-, leia- BULK! bhel-2 BULL! bhel-2 BULL? beu-1 BULLA beu-1 BULLATE beu-1 BULLET beu-! BULLETIN beu-1 BULLION beu-1 BULLY? beu-1 BULWARK bhel-2, werg- BUNCO bheg- BUND! bhendh- BUND? bhendh- BUNDESRAT ar- BUNDLE bhendh- BUNG peuk- BUNGLE bheg- BUPRESTID gWou- BUR! bhar- BURDEN! bher-1 BURG bhergh-2 BURGESS bhergh-2 BURGHER bhergh-2 BURGLAR bhergh-2 BURGOMASTER bhergh-2 BURIAL bhergh-! BURIN bher-2 BURN! gWher- BURN? bhreu-2 BURNET bher-3 BURNISH bher-3 BURSA bursa BURSAR bursa BURSE bursa BURST bhres- BURY bhergh-1 BUSHEL? bhau- BUSK! busk- BUSK? s(w)e-
1326:BUSTARD awi- BUSTLE s(w)e- BUT ud- BUTCHER bhugo- BUTT! bhau- BUTTER gWou-, teue- BUTTOCK bhau- BUTTON bhau- BUTTRESS bhau- BUTYRIC g¥ou- BUXOM bheug-3 BUZZARD beu-2 BY! ambhi BYRE bheue-
1526:FOLIAGE bhel-3 FOLICOLOUS _bhel-3 FOLIO bhel-3 FOLIUM bhel-3 FOLKMOTE mdd- FOLLICLE bhel-2 FOLLICULITIS bhel-2 FOMENT dheg¥h- FOMITE dheg¥h- FOND? bhudh- FONDANT gheu- FONDUE gheu- FONT! dhen-1 FONT? gheu- FOOD pa-
1534:FOUND! bhudh- FOUND? gheu- FOUNDER bhudh- FOUNTAIN dhen-! FOUR kWetwer- FOURTEEN kWetwer- FOURTH kWetwer- FOWL pleu-
1544:FROLIC fik-, preu- FROM per? FRONTISPIECE spek- FROST preus- FROTTAGE bhréi- FROWARD per! FRUCTIFY bhrig- FRUGAL bhriig- FRUGIVOROUS bhrig- FRUIT bhriig- FRUITION bhriig- FRUMENTACEOUS _ bhrig- FRUMENTY bhriig- FRUSTULE bhreus-2 FRUSTUM bhreus-2 FRY! bher-4 FUGACIOUS bheug-1 -FUGE bheug-! FUGITIVE bheug-1 FUGLEMAN man-1, pleu- FUGUE bheug-! FUHRER per-2 FULCRUM bhelg- FULGENT bhel-1 FULGURATE bhel-1 FULIGINOUS dheu-1 FULL! pele-1 FULMAR pu-2 FULMINATE bhel-1 FUMARIC ACID dheu-1 FUMAROLE dheu-1 FUMATORIUM dheu-! FUMATORY dheu-1 FUME dheu-! FUMIGATE ag-, dheu-! FUMITORY dheu-1, ters- FUNAMBULIST al-2 FUNCTION bheug-2 FUND bhudh- FUNDAMENT bhudh- FUNDUS_ bhudh- FUNGIBLE bheug-2 FUNNEL gheu-
1557:GAST gheis- GASTRIC gras- GASTRO- gras- GASTRULA gras- GATHER ghedh- GAUCHE weng- GAUD gau- GAUDY! gau- GauDY? gau- GAUGE ghalgh- GAUNTLET? klou- GAUR gWou- GAVEL? ghabh- GAWK ghow-é- GAYAL gWou- _ GEANTICLINE gé GEAR garwian GEGENSCHEIN gagina, skeei- GELANDESPRUNG lendh-2, spergh- GELATIN gel-3 GELATION gel-3 GELD! ghel-3 GELD2 gheldh- GELDING ghel-3 GELID  gel-3 GELIGNITE egni- GELT! gheldh- GEM gembh- GEMINATE yem- GEMINI yem- GEMMA gembh- GEMMATE gembh- GEMMULE gembh- GEMOT mdéd- GEMSBOK bhugo- GEMUTLICH mé-1 GEMUTLICHKEIT mé-1 -GEN gene- GENDARME gene- GENDER gene- GENEALOGY genoe- GENERAL gene- GENERATE genoe- GENERATION geno- GENERIC gene- GENEROUS gene- GENESIS gene- -GENESIS gene- GENIAL! gene- GENIAL? genu-2 GENICULATE genu-1 GENITAL gene- GENITIVE gene- GENITOR gene- GENIUS gene- GENOCIDE gene- GENOTYPE gene- GENRE gene- GENS gene- GENT! gene- GENTEEL gene-
1736:LATHER leu(@)- LATIFUNDIUM bhudh- LATITUDE stele- LATRINE leu(@)- -LATRY [6-1
2136:PRO-2 per? PROBABLE per! PROBE pert PROBITY per! PROBLEM gWele-1 PROBOSCIS g¥6- PROCEED ked- PROCLAIM kele-2 PROcLITIC § klei- PROCLIVITY klei- PROCREATE ker-3 PROCTITIS prdkto- PROCTOLOGY prdkto- PROCTOR cura PROCTOSCOPE prdkto- PROCUMBENT keu-2 PROCURATOR cura PROCURE cura PROCYON kwon- PRODIGAL ag- PRODIGY ég- PRODROME der-1 PRODUCE deuk- PROFANE dhés- PROFESS bha-2 PROFESSOR reg-! PROFFER bher-1 PROFICIENT dhé-1 PROFILE gWhi- PROFIT dhé-1 PROFLIGATE bhiig- PROFOUND bhudh- PROFUSE gheu- PROGENITOR gene- PROGENY gene- PROGLOTTID glégh- PROGNOSIS gnd- PROGRAM gerbh- PROGRESS ghredh- PROHIBIT ghabh- PROJECT yée- PROLAN al-3 PROLAPSE leb-1 PROLATE tele- PROLEGOMENON leg-! PROLEPSIS (s)lag¥- PROLETARIAN al-3 PROLIFEROUS _al-3 PROLIFIC al-3 PROLIX wleik- PROLOCUTOR tolkw- PROLOGUE leg-1 PROLONG del-1 PROLUSION leid- PROMENADE men-2 PROMINENT men-2 PROMISCUOUS meik- PROMISE (s)meit(e)- PROMOTE meue- PROMPT em- PRONE per! PRONEPHROS _ negwh-ro- PRONOUN no-men- PRONOUNCE neu-! PROOF per! PROPAGATE pag- PROPEL pel-6 PROPEND (8)pen- PROPER pert PROPERTY per? PROPHET bha-2 PROPHYLACTIC phulax PROPINQUITY per? PROPIONIC ACID peie- PROPITIOUS pet- PROPOLIS pele-3 PROPORTION pere-2 PROPOSE apo- PROPRIOCEPTION per! PROPRIOCEPTOR per? PROPTOSIS pet- PROPYLAEUM pulé PROPYLON pulé PROROGUE reg-1 PROS- pert PROSCRIBE skribh- PROSE wer-3 PROSECUTE sekw-1 PROSELYTE leudh-1 PROSOMA teue- PROSOPOPEIA kWwel-2, per! PROSPECT spek- PROSPER spé-1 PROSTATE sta- PROSTHESIS dhé-1 PROSTITUTE sta- PROSTOMIUM ste-men-
2280:SPRINGBOK bhugo-, spergh-
2290:STEEL stak- STEENBOK bhugo-, stei- STEEP! (s)teu- STEEPLE (s)teu- STEER! sta
```


## [2026-09-05T14:37:05.920Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC bhundh/bhudh ===\" && grep -n \"^bhudh\\|^bhundh\\|^bhug\\|^bhūg\\|bhundho\" IEC.txt | head -20",
 "description": "Grep Mann IEC"
}
```


### [2026-09-05T14:37:05.965Z] TOOL RESULT

```
=== IEC bhundh/bhudh ===
1870:bhudh-, theme of emphatic vb. “to be? Osc. cf. fufens ‘they were; W byddent, id.
1872:bhudhmn- (bhudno-) “base, bottom, stock, stump, root, stone'. WP II, 190 Skt. budhnáh, -ám; Av. buno; Per. bun; Oss. bín, bun, beside bíndur, cpd. (bín + dür “boundary stone; farm); LW in Arm. bun (i-st. ‘trunk, root, origin); Gk. puthmén; cf. Gk. (Anatolian? Phryg.?) púndax "bottom", cf. bhrgh- for a ref. to pürgos; Alb. bun “mark, goal; spring-head, mountain hut? be- side buzém *yule-log', fr. *bhudhimn-); Lat. fundus; MIr. Ir. bun "base, root, foot? beside bond, bonn “sole of foot; Mir also bunne ‘spring, source’; Gallo-Lat. bodina *bound- ary; Br. men bonn (‘boundary stone’. LW in OFr. bonde, E bound); W bon 'stem, base, stock; OBr. cf. bon-ed ‘race, nobility: W bonedd, id.; Ligur. cf. Bodin-cus (river-name of Po, said to mean *bottomless"); variants in OHG bodam; Du. bodem as against OE botm; ON botn; Cz. cf. bedna “chest, box’;
1875:bhudhó, ið “wake, watch, care, notice’. WP II, 147. Cf. bheudh-, bhudhros Skt. búdhye, intr.; cf. budháh (^wise'. LW in Arm. but “watchful'); Av. fra-būiðye; OE bodian; OFris. bodia; MHG boten; ON boóa; OCS büzdo, büdéti ‘keep watch, be awake” (and com. SI.); Li. budüà, and budiù, budeti, id. Nasal-infix in Gk. punthánomai (lit. "am roused': “hear of")
1876:bhudho(n) (1) in OHG boto ‘messenger’; cf. ON boði, id. & OE bod ‘message’. See bhudho above
1877:bhudho(n) (2) “creature” Gk. puthón; (Rustic) Lat. bufo (*toad', assi- milated conss. as in barba, bulla) beside LLat. bufus, bufa a poisonous insect; Lat. cf. also fullo ((2) ‘earwig’, fr. *bhudlon, cf. E bottle 'fly); Ir. bod ((boor, cpds. *'bird") (the expected form *bodán does not occur); SWG Butten 'polecat; LG budde “earth- worm, louse’; OE budda ‘beetle’; EME boude *corn-worm'; ONorw. budda ‘young animal’
1878:bhudhros “awake, alert’. Cf. bhudho, io. WP II, 148 Skt. cf. budbah ‘wise’; Av. (zaeni) budro ‘alert’; (Iran. LW in Tk. bidar, id.?); OCS büdrü, id. (and comm. S1.); Li. budrüs, id.
1879:bhugo, ið (1) “bend, turn, flee’. WP II, 144. Cf. bhugho, bheugó Skt. bhujami, pp. bhugnábh; Lat. fugio, ire; Gk. cf. éphugon, aor. ‘I fled, feared”; inf.: phugein; Ir. boghaim “bend, arch'. Ambig. cf. bhugho; MHG bochen ‘defy’ beside bocken ‘be bowed, sink’; OFris. buckia ‘bend, bow’; G (sich) bücken; Norw. bukka; Sw. bocka, id.; Li. cf. bügstu, bügti (“be frightened'. Ambig. cf. bhugho)
1880:bhugo, ið (2) ‘beat Gk. cf. s-phuzo ‘pulsate’, s-phugmós ‘pulse’; MHG bochen ‘knock’ beside buch ‘cudgel’; (Alemannic) G pochen: Dan. poge ‘knock’
1881:bhugos, à ‘bend, turn, flight’. Cf. bhugo & bhugho. WP II, 144 Skt. bhujah w. secondary -j-: ‘curve, branch, arm’; Gk. fugé, füza, f. ‘flight’; Lat. fuga, id.; G buck (2) ‘timid’; Li. cf. bügus (‘dan-
1882:bhudhó, ið — bhukió
1891:bhugho, io ‘turn, bend, fold”. Cf. bhugo Gk. (synth. cpd.) ptüsso “fold? beside ptüx, gs ptukhós, also ptukhé, f; Ir. (ambig.) boghaim ‘bend, arch’; ON buga ‘bow, beng’; Go. (Crimean) boga, OHG and OE boga ‘bow’; cf. Norw. bugne ‘bend’? & G Bucht ‘bay’; E bight beside EME bought ‘arch’. Doubtfully to Go. bugjan ‘buy, and ON byggja ‘hire out, pledge’. Cf. OE bygu & byga ‘curve, bend, angle’: ON bugr, id.
1892:bhught-, bhughtiom, io “bend, turn, exchange barter’. Cf. bhugho Per. (?) büyée ‘wrapper; Myc. cf. puktalia (queried: ‘a garment); G Bucht ‘bay’; E bight, id. beside EME bought ‘arch’; ON býti; Norw. bytte ‘barter, exchange, deal beside bukt, bukte “bend”, w. phonology of LG
1895:bhugh- ‘bogey, insect. Cf. WP II, 117 W bw ‘bogey; ME bugge ‘scarecrow’; cf. E bug “insect? and bugbear (cpd.); Li. bu£Zys, io ‘bogey; insect?
1947:bhundh- (?). Cf. Lat. -bundus; OCS bodo “shall be’. See bhüio, bhuiio
1948:bhundh- (infixed form of bhudh-, q. v.). Cf. WP IT, 147 Gk. cf. punthánomai ‘get to know’; Li. bun- dù, büsti, intr. ‘wake’
```


## [2026-09-05T14:37:20.352Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ntxt=open('IEC.txt',encoding='utf-8',errors='replace').read()\nlines=txt.split('\\n')\n# find leaf index of line 1872\ncnt=0\nfor i,l in enumerate(lines,1):\n    cnt+=l.count('\\f')\n    if i==1872:\n        print('leaf(0-based) approx',cnt)\n        break\nEOF",
 "description": "Locate IEC leaf for bhudhmn"
}
```


## [2026-09-05T14:37:21.811Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT buna ===\" && grep -n \"buna-\\|būna\\|bũna\\|bnna-\" BRT.txt | head -20; echo \"=== BRT buza ===\"; grep -n \"büza\\|buza-\\|būza\" BRT.txt | head -20",
 "description": "Grep Bartholomae"
}
```


### [2026-09-05T14:37:21.981Z] TOOL RESULT

```
leaf(0-based) approx 79
```


### [2026-09-05T14:37:22.053Z] TOOL RESULT

```
=== BRT buna ===
17315:967                  bi&amrüta-                       —  buna-                     968
17362:tyMn.—  II  Vgl.  iBed.  as.  /.'j 'Heilung'  nnd  ,  j.^  g,  buna- "  m.  'Gnind,  Boden,  Tiefe'
=== BRT buza ===
12295:•  j.  tizi.srvä-  Adj.  (mask.  •wo-)  'mit  spitzem Gehörn':  büzahe  . .  'vake  Yt  14-  »5-
17385:■  j.  büza-  m,  'Ziege,  Ziegenbock':  'zake kfkrpa  rPnahe  "in  der  Gestalt  eines  wilden Ziegenbocks"  Yt.  74. 35-
```


## [2026-09-05T14:37:29.345Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '17355,17395p' BRT.txt",
 "description": "Print Bartholomae buna/buza context"
}
```


### [2026-09-05T14:37:29.388Z] TOOL RESULT

```
Terdetbt;    5.  dain  Jl'sTI  Bd.   119  b    und   das  S,  tAii--.  —  rü.;  fehlt.
np.  Zitat  bei  Sp.  Komm.  /.  2ÖE.  ,  y   +bu8ra.«)    m.     EX.  eines  Gläubigen:
•  j--  g-  bug-  f.  j)  'I^sung,  Rettung"^:  ".ra^e  d}:;^rjsp7t)  aJUi-jJ  "des  Ät  Sohns 'uji  F.16.          2)  'Busse'":  yi  vi  iasiui  des  Z».  .  .'"  Yt /J.  106.
ae'iaahö  (sd.)  ä  maxUtam  ayjmaite  *'üjim  £'=;-  'anfmetksam',  rnm  V.  U-d-,  vgL  M^m.
Y   ,,  ,,                              '  '■'i'-J-  Adj.    ^    0   So   Fl;    -NA.   hat    ^-"8-
7        V,                  T,-    ■        ^      i'  .     ■  ZDMG.  ,-ü.  Ö9S  No.
Znm  \.  /a.\';    —    Pa,  (i-j    1';    /■'.>.',    uu  2  :  j         1
tyMn.—  II  Vgl.  iBed.  as.  /.'j 'Heilung'  nnd  ,  j.^  g,  buna- "  m.  'Gnind,  Boden,  Tiefe'
nhd.  6;.,,,.     Bed.   1  i=.  unsicher,  s-  Pu.  .^,„   ^w>i^'  tma,?Aaht  \.iq.Al\  —  '»
m  ].karapanv  'ra^u-y-imni:  boxta  rnaA^"  ja/ran.im  Tairyanam  Y./p.4i;  XX-i^-^i,
FrU.a.a.  , —   .^„  xrayaTfh!  Vl/OSi;    —    dStati
•  j.  buxtay-  £  lleuleD,  Fauchen':  bu;jhi  (sd.)  .  .  *p-ä  'iiät  iaHntii  Aog.77;  — (sd.,1  nama  ahmi  -tii  nqma  ahini  YL;5.47.  yawU  Ums  . .  'n.V  /iJxtayj  \si.)  V.^.j;
dby  Google
969
bunava-
byaräan-
970
—  'mm  ä  F.  4a(?),         a)  'das  Unterste,
Unterseite'  (nur  Ableit).
Ableit.  —  Aus  ar.  *iAua'i*na;  %  34.  —  np, bun;  vgl.  aL  iudhnä- m.,  Fä.  bundha-  m.  —  Pü.i bun.  —  1)  »  ist  überall  ausaer  Y.53.  7  besser bezeugt.
•  j.  buoa'va-  Adj,  'von  der  Unterseite' stammend':  aspaim  vanspm  .  ,  vamaiti kalärS  ayravi' (sd.)  vä  °v5  vä  Yt  t6.  lo,
»Suff,  s.  S  20a  —  Npü.!  ai  dam.
•  g,,  j.'\  p.  bümi-  f.  'Erde';  II  («ä/«  'mim ,  .  avam  asmänam  D.  6.  i,  X.  i.  i,  6,  i, Ao.i.i  {tto'mäm);  D.6.4;  —  paitt 'mxm kaptai^yqm  Vt  JJ).  26;  —  raocaicä  .  . •mm^a  vTipäcä  vcha  Y.J/.  i;  42.  y,  — 'myä  (GS.)  haptai^e  (sd.)  Y.  32.  3;  — \xl3y^iya'  ahyäyä  'mtya  ^vazarkayil  D. 6.  2,  X.  /.  2 ;  Am.  7,  3,  Ao.  /.  2,  D.  72.
Ableit.  —  Zum  V.  iai^.  —  ai.  bhuml-  f.,  mp. (Pü.),  np.  büni.  —  ■)  Im  jungem  Awesta  nicht üblich  (V.  42.  3  stammt  aas  Y.j/.  i,  Yt./p. 26  erinnert  an  Y.  ja.  3).  Hier  stebl  dafär zum-,  vgL  iwfH  aimamm  . .  imqm  jqm  Yt.  ^J.  3 mit  D.  Ä  1.
•  j.  bümya-  m.  Name  eines  Bergs  oder Gebirgs:  ahma}  ha^a  garayS  fraoxfyan .  xitvS  >ry3urs(sd.)  hapta^ö  'yd  Yt.  ig.  2.
AbleiL  aus  bümi-?;    ai.  iAnmya-  AA],  'teirenus'.
•  j.  buye  Inf,  '(etwas)  zu  werden',  mit Nom.  ag,  {v^.bav-  3):  a/rinämi  vavanva *vanal.pjJaM(s±)  b'  vTspsm  aurvak^m  . . vavam  b'  rakiiiya  mananha  . .  nijan3  b' vlspe  dusmainyü  . .  sas?  (sd.)  b°  vavAäuca müde  A.7.  lof.
Zum  V.  bav'.  —  ai.  •bküve;  %  i6S.  19.
•  j.,  g.  buray-  Adj.  "reichlich;  völlig,  voll- kommen': 'uiri  gaos  'uiri  ^an^a  °u:ri vastra  'uiri  anyaHbyS  mazäayasnaübyöyyi. 4^ ;  —  masdä  dadat  ahurS  . .  'ärsis  ä  . . :^'apa^yai  (sd.) . .  Y.  ?7. 2 1.  a)  Akk.  mit 'kar-  'etwas  (Akk.)  völlig  machen  sva. (Erhofftes)  erfüllen  mit-'  (Instr.)":  mat- damüä  'airiiä  ksrt^ä  räitl  isi  xrapaitJ (sd.)  ahmat  hyat  aibl  hyat  mtzditn  . .  V. 40.J.  '        '
Zum  ann.  V.  ban^I  'bastate'.  —  ai.  bhutay- Adj.  —  P6.;  bovandak,  bovandaklh,  Sil.:  iani- pürnatvam.  —  ')  Vgl.  Y.  29. 10  unter  äpana-.
■  j.  büza-  m,  'Ziege,  Ziegenbock':  'zake kfkrpa  rPnahe  "in  der  Gestalt  eines  wilden Ziegenbocks"  Yt.  74. 35-
AblelL  —  np.  (NpS.)  bui.     Weitres  bei  Schba.
DBR  Reallcx.  9S5.
•  j.  buzya-  Adj.  'von  Ziegen  herrührend, caprinus':  paya^ham ..'zyanamca  V.j.sa.
Ableit,  aus  büsa-,  —  Pü, :  mäläi  i  buz  fem.
•  g,  *büätay-'>  f.  'Werden',  Plur,  'die werdenden,  künftigen  Dinge'":  Ayat  *a 'ti/'i  *vasas>jxsa%rahyä  dyä  "auf  dass  ich mir  die  künftigen  Dinge  des  unumschränkten Reiches  erwerbe"  '^.43.  8.
Zum  J-Aor,  des  V,  bav;  vgl,  büidym.  —  Pü. : ka  an  i)  li<rvft  nemakih  -  kii  tan  •'  fasln  bmitt  - pa  iämak  ^^alaiih  äalähtl  -  ku  pätixsähth  fia afSyast  ä  dahühel-,  Su,:  jw  '■rfl«  bhasii4yati  svtc- chayä  räjyaiya  dälS.  —  ')  NA.  äbüila;  s.  aber KZ.  30,  3 18,  —  J>  Falsch  S  55-  a.  —  J)  S.  ä No.  21.
•  j.  buäyant-  Adj.  {km.'yäntl-.  'yqi^y-) PPi7(Fut)A.:  s.  bav-.
Ableit.
•  j.  büäytptä-  f.   Name  der  Dalvl  der
Schläfrigkeit'*:  Bat  matre  fradvaraiti  'ta- dar^ögava . .  iiiti  daomna  ^afsata  malya- i^w/röFrW.70.4i;Yt./o.97j  —  -ta  darr/B.- gava  ks  vJspim  ahüm . .  hakat  raocarthqm frayrate  nix^abdayäti  V.  18.16;  —  'tayä zairina  ..  'ta  yä  darryS^ava  V.  77, 9;  — taurvayeiti  "ftw"  zairimm  Yt75.  a.
```


## [2026-09-05T14:37:30.207Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==80' IEC.txt | grep -n \"\" | head -40",
 "description": "Print IEC leaf 79 for page numbers"
}
```


### [2026-09-05T14:37:31.883Z] TOOL RESULT

```
1:, à, is) "ball, round creature, bubble’. Cf. bubul- and bhubhos (2) Arm. bubul ənkujz ‘walnut’; Lat. bulla (dial. or expressive: “boss, knob, stud, seal, bubble’. Assim. as in barba is also possible); MHG (Alemannic type) popeln ‘bubble’; G bub- beln, id.; LG Bobbel, bobbeln, s & v id.; Fris. Du. bobbel “lump, pimple, bubble'; Sw. bubbla v. ‘bubble’; Cz. dim. bebelka ‘louse’; Li. bubulis, io “ball, pellet; Latv. bubulis "knot in yarn’
2:bhud- ‘stumpy, blunt; stump, chunk? Arm. cf. but ((blunt, fr *bhudtó- or
3:bhubbh- — bhudhmn- (bhudno-)
4:10
5:15
6:20
7:25
8:30
9:35
10:40
11:45
12:118
13:*bhudstó-); Ir. (ambig.) bod "boor": MHG butze ‘bit’; LG butt ‘clod’; adj. ‘blunt’; Du. ` bot n. ‘tip, bone’; f. ‘bud’; adj. ‘blunt’; Du. & Fris. bot (also: silly”); OE cf. buttuc “stub, butt, corner of land’ beside bytt ‘corner of land'; G Boss “peg on ploughbeam', cf. bos- sig ‘wild, defiant; ON butr “butt, stump’: Li. bude "lichwake mushroom’. (Verbal ex- tensions in MHG butzen *jolt'; OFris. botta, id.; LG botten “beat flax’; Du. botsen ‘crash’, fr. *bhudsKo) | : bhüdo(n) ‘burst, sprout, projection’ Ir. búdán ‘frontal bone of horned animal; stump’; MHG büse ‘sprout; outburst be-
14:. side būzen ‘swell, sprout'; E bout; Fris. bût
15:‘pal’; Du. (?) buit (booty. The semantic link obscure)
16:(bhüdü, cf. abhu)
17:(bhudtós, see bhud- Arm. but ‘blunt: Norw. buttet *dumpy?)
18:bhudh-, theme of emphatic vb. “to be? Osc. cf. fufens ‘they were; W byddent, id.
19:bhüdhlos, à, om, ön “existence, being, crea- ture'. Cf. WP II, 141 OE bold ‘dwelling’; Cz. bydlo, id.; Li. büklà,. büklé, id. (Lat. fulló ‘earwig, beetle may represent a variant *bhudlo- cf. OE botl, n. ‘dwelling’; Eng. bottle ‘fly’. Cf. bIue-bottle)
20:bhudhmn- (bhudno-) “base, bottom, stock, stump, root, stone'. WP II, 190 Skt. budhnáh, -ám; Av. buno; Per. bun; Oss. bín, bun, beside bíndur, cpd. (bín + dür “boundary stone; farm); LW in Arm. bun (i-st. ‘trunk, root, origin); Gk. puthmén; cf. Gk. (Anatolian? Phryg.?) púndax "bottom", cf. bhrgh- for a ref. to pürgos; Alb. bun “mark, goal; spring-head, mountain hut? be- side buzém *yule-log', fr. *bhudhimn-); Lat. fundus; MIr. Ir. bun "base, root, foot? beside bond, bonn “sole of foot; Mir also bunne ‘spring, source’; Gallo-Lat. bodina *bound- ary; Br. men bonn (‘boundary stone’. LW in OFr. bonde, E bound); W bon 'stem, base, stock; OBr. cf. bon-ed ‘race, nobility: W bonedd, id.; Ligur. cf. Bodin-cus (river-name of Po, said to mean *bottomless"); variants in OHG bodam; Du. bodem as against OE botm; ON botn; Cz. cf. bedna “chest, box’;
21:119
22:R cf. bodnarí ‘cooper: LL budinarius (fr. Gall)
23:bhudhó, ið “wake, watch, care, notice’. WP II, 147. Cf. bheudh-, bhudhros Skt. búdhye, intr.; cf. budháh (^wise'. LW in Arm. but “watchful'); Av. fra-būiðye; OE bodian; OFris. bodia; MHG boten; ON boóa; OCS büzdo, büdéti ‘keep watch, be awake” (and com. SI.); Li. budüà, and budiù, budeti, id. Nasal-infix in Gk. punthánomai (lit. "am roused': “hear of")
24:bhudho(n) (1) in OHG boto ‘messenger’; cf. ON boði, id. & OE bod ‘message’. See bhudho above
25:bhudho(n) (2) “creature” Gk. puthón; (Rustic) Lat. bufo (*toad', assi- milated conss. as in barba, bulla) beside LLat. bufus, bufa a poisonous insect; Lat. cf. also fullo ((2) ‘earwig’, fr. *bhudlon, cf. E bottle 'fly); Ir. bod ((boor, cpds. *'bird") (the expected form *bodán does not occur); SWG Butten 'polecat; LG budde “earth- worm, louse’; OE budda ‘beetle’; EME boude *corn-worm'; ONorw. budda ‘young animal’
26:bhudhros “awake, alert’. Cf. bhudho, io. WP II, 148 Skt. cf. budbah ‘wise’; Av. (zaeni) budro ‘alert’; (Iran. LW in Tk.
```


## [2026-09-05T14:37:46.187Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 82 83; do echo \"--- leaf $n ---\"; awk -v N=$((n+1)) 'BEGIN{RS=\"\\f\"} NR==N' IEC.txt | head -6; done",
 "description": "Check IEC page 124 area"
}
```


### [2026-09-05T14:37:47.669Z] TOOL RESULT

```
--- leaf 82 ---
*bhuluis) ‘hill’; Norw. bylle “boil, ulcer; Li. LW? bülve ‘potato’, perh. fr. Pol. bulwa, id. cf. Ukr. bul'ba, id.
bhüm, aor. theme lsg. of bhii, q.v. Gk. éphün; OCS bymü, bymi, etc.; Skt. cf.
123
2.3s ábhüh, ábhüt
bhüm- (bhümn-, bhümå) ‘growth; cultiva- tion, ground, soil". Cf. IL, 141 Skt. bhümih, bhüman; Av. bümis; Per. büm; Ober cf. bümaj "earth Gk. phüma; Alb. bimë ‘plant’; Lat. (gloss) Toma ‘earth’; OE cf. byne, adj. (cultivated'; LG büne 'embank- ment
bhumbho ‘resound’. Cf. bhmbh-. WP II, 107 Du. bommen ‘bang’; Li. bumbü, eti ‘babble’; cf. Alb. bumáll, m. (*dungbeetle', isophonic with Li. bumbólas “large bud")
--- leaf 83 ---
. bong ‘conceited’; Alb. bungé ‘lump, gnurl; Lat. fungus, m. ‘growth, fungus, blight, wax round wick; OHG bunga, f., bungo, wm. ‘lump, hump; knob’; G Bun- ge ‘drum; bownet'; Fris. bonge ‘bladder, blister’; Icel. bunga ‘lump’; Latv. bungas, fpl. “drum”
bhunĝos, ios (3, õ(n)) ‘bulge, hump, lump’. Cf. bhunghos, å Arm. bunc (o-st. ‘clod’); OFris. bunka ‘bone’; Fris. bonke, id.; Du. bonk, m. ‘lout; hob- nail’; f. “lump, large bone’; E bunch; ON bunki ‘heap’, Dan. bunke, id.; Sw bunke ‘cask’; cf. orm-bunke ‘fern’; Sw. dial. bunke ‘heap, hillock’; Finn. LW punkka ‘cask’
125
bhur- ‘pierce, cut, bore’. See bhraio
bhür-, is, à, om (1) ‘pile, mass, crowd’ Skt. bhürih *mass'; Av. büiri, n. id.; Gk. cf. la-phüron ‘plunder’; ge-phüra ‘mound, bridge’; Li. būrys, io ‘crowd, flock; W (*-u-) cf. bwr ‘embankment
bhür- (2) ‘dark, dun, grey, brown’ Oss. bür ‘fawn, yellow’; It. (Gallo-Lat.) buro ‘dark’; Gk. cf. porphuró- (in cpds., fr. *bhur- bhur-); Pol. cf. bury (“dark grey”, fr. *bhau- ro-?: R buryj ‘brown’; Hes. phurós ('dun, roan’ or sim.)
```


## [2026-09-05T14:37:47.745Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD bun/buz ===\" && grep -n \"^bun\\|^buz\\|^būz\\|bun-dahišn\\|bundahišn\" PHD.txt | head -20; echo \"=== PHD_mackenzie ===\"; grep -n \"^bun\\|^buz\" PHD_mackenzie.txt | head -20",
 "description": "Grep MacKenzie"
}
```


### [2026-09-05T14:37:47.809Z] TOOL RESULT

```
=== PHD bun/buz ===
292:*brinj [binc | (M bryng), N birinj] bronze, brass. ~én [-yx!] bronze, brazen. brinómand [blyn’wmnd] delimited. brištan, bréz- [blystn', blyc- | M bryz-, N biristan] roast. brüg [blwk' | M brwg, N abrü] (eye)brow. büdan, b(aw)- [YHWWN-tn! < A yhwwn, У hwh; bwtn', b- | M bwdn, bw-, N büdan] be, become. bawišn: becoming, genesis. büf [bwp | N <), *büg [bwk'] owl. buland [bwind | = M, N ~] high. būm [bwm | N ~] land, earth, country. ~-€andag [-cndk'] earthquake. Ibun [bwn' | = M, N ~] base, foundation, bottom. *bun [bwn! | N ~] = wan. bunag [bznk! | N ~a] baggage; abode, camp. — daštan: dwell, settle. bun-dahišn(īh) [bzundhšn!, -yh] primal creation. bunih [bwnyh] beginning. buništ [bwnyst! | = M] foundation. ~ag [-k'] principle. bun-kadaģ [bwnktk'] original house, home. bun-xān [bwnh?n'] source. bur-, —išn, v. buridan. burāģ [bzoP RU] cutting, sharp. burām-, v. bram-. burd [bwit! | M bwrd] patient. ~ih: patience. burdan, bar- [Y BLWN-tn! < А У ybl; bwltn', bl- | M Бата, br-, N <] carry, bear, take, endure. ~išn: bearing, behaviour. burdār [bwit!]] bearer; womb. ~ih: patience. burd-ešnēhr [bwit! fnwhl | P bwrdyfnwhr] grateful, thankful. burg [bwig | (Ar. burj)] tower. buridan, bur- [bwl-ytn! | M bwr-, N ~] = bridan. —j$n: cutting. Burz [bwic] the god of agriculture. Burzénmihr [bwlcynmtr!] the third major Fire of Sasanian Eran, that of husbandmen. burzidan, burz- [bwlc-ytn'] praise, honour. ~i$n: praise, honour. —iŠnié : praiseworthy. buš [ро | N ~] mane. būšāsp [bwPsp | M bwsy'sp, N ~] sleep, sloth; dream. * but [bwt! | = M, N ~] Buddha; idol. buz [AZ < A ‘z; Бос | N ~] goat.
1113:bun kulāčag.
1114:bunch, bundle dastag.
=== PHD_mackenzie ===
1651:buna~ [bwnk I N .....,a] baggage; abode, camp.
1654:bun-dahisn(ih) [bwndhSn , -yh] primal creation.
1656:bunih [bwnyh] beginning.
1657:bunist [bwnyft I = M] foundation .
1660:bun-kada~ [bwnktk l ] original house, home.
1661:bun-xan [bwnh)n ] source.
1692:buz [AZ < A cz ; bwc IN.....,] goat.
11147:bunag                         , .s\\\    1-2beI                             ......,,,
11148:bunkadag                  \jl'"    \\\   bOxtar                    ~~"
11149:bunist                    \~,\\          b6xtarih                 ~~\j
11150:bunistag                \~'ttN\\\
11812:buzl , xaz                   S»    o~marag                    ,~t'"
```


## [2026-09-05T14:38:08.236Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ntxt=open('IEC.txt',encoding='utf-8',errors='replace').read()\nlines=txt.split('\\n')\ncnt=0\nfor i,l in enumerate(lines,1):\n    cnt+=l.count('\\f')\n    if i in (1947,1948,1891,1879):\n        print(i,'leaf',cnt, l[:120])\nEOF\necho \"--- leaf 82 full ---\"\nawk 'BEGIN{RS=\"\\f\"} NR==83' IEC.txt | tr '\\n' '\\n' | sed -n '1,80p' | grep -n \"bhun\\|^12[0-9]\"",
 "description": "Locate IEC leaves for bhundh"
}
```


### [2026-09-05T14:38:10.753Z] TOOL RESULT

```
1879 leaf 80 bhugo, ið (1) “bend, turn, flee’. WP II, 144. Cf. bhugho, bheugó Skt. bhujami, pp. bhugnábh; Lat. fugio, ire; Gk. cf. ép
1891 leaf 80 bhugho, io ‘turn, bend, fold”. Cf. bhugo Gk. (synth. cpd.) ptüsso “fold? beside ptüx, gs ptukhós, also ptukhé, f; Ir. (a
1947 leaf 82 bhundh- (?). Cf. Lat. -bundus; OCS bodo “shall be’. See bhüio, bhuiio
1948 leaf 82 bhundh- (infixed form of bhudh-, q. v.). Cf. WP IT, 147 Gk. cf. punthánomai ‘get to know’; Li. bun- dù, büsti, intr. ‘wa
--- leaf 82 full ---
3:123
11:bhüm- (bhümn-, bhüma) — bhun$os, ios (à, ó(n))
20:124
22:bhun- (1) *base, foundation, floor, board- ing’. (Some forms are ambig. cf. bhudhmn-, bhudno-, bhouon-) Av. buna ‘floor’; Alb. bun *"log-cabin', etc. is ambig. cf. bhudno-; Ir. bun (*base', ambig. cf. bhudno-); MHG büne, bün “board, ceil- ing, stage; G (fr. LG) Buhne ‘scaffolding, boarding) may, like Bühne ‘stage’ be referable to type *bhudhmn-, bhudno-.
23:bhun- (2) ‘gush; pour Alb. cf. bunoj, T buroj “well up, spring’; ON buna ‘gush’; Ir. cf. buinne, m. ‘gush’
24:bhundh- (?). Cf. Lat. -bundus; OCS bodo “shall be’. See bhüio, bhuiio
25:bhundh- (infixed form of bhudh-, q. v.). Cf. WP IT, 147 Gk. cf. punthánomai ‘get to know’; Li. bun- dù, büsti, intr. ‘wake’
26:bhung- (infixed form of bhug- (1), q.v.) *turn, apply' Skt. bhunágmi, bhufiàmi “enjoy, use, eat etc.; Lat. fungor, -1 ‘do, suffer, conform to, furnish with" etc.
27:bhung- (2) (infixed form of bhug- (1) in sense of "Dee? Gk. phuggáno ‘flee’; E bunk, id.
28:bhunghelis (or bhungolis) ra furry animal Lat. cf. fungalis, id.; Alb. bungél ‘weasel’; G cf. (?) Bunkel, m. ‘squat person, dumpling’
29:bhunghos, à ‘hump, bulge, growth; drum; bulging’, etc. Cf. bhun$- Kurd
```


## [2026-09-05T14:38:18.156Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== NYB leaf 58 (p.50) ===\" && awk 'BEGIN{RS=\"\\f\"} NR==59' NYB_vol2_glossary.txt | head -60",
 "description": "Print Nyberg glossary p.50"
}
```


### [2026-09-05T14:38:21.592Z] TOOL RESULT

```
=== NYB leaf 58 (p.50) ===
. 2713; of the corresponding official at Arjasp’s court 2511, 287... A Prth. Arsacid title, adopted by the Sassanid kings of the 3d c., but later replaced by vazurg framatär (v. the 2nd w.); survived in independent Armenia governed by Arsacids (until A. D. 430) and in Georgia. Sas. inser. Prth byths, Prs bythšy KZSPrth a) 1. 23, b) l. 25, c) l. 27 = Prs ll. 29. 31. 33 Gr. v. a) Bde (in the list of the late Artaxšēr's officials), b) miridēng of Shapur’s own vizier, c)
www.parsianjoman.org | oe zl ejt
bitaxs
rarudenc; patron. Prth 1. 28 = Prs 1. 24 bythškn, Gr. v. rırıdıyav; Paikuli = KZS. Arm. lw. bdeašx (Hübschmann, AG 119 sg.). Georg: Armazi bilinguis (Nyberg, Eranos 44, 1946, 228-243; 233 sqq.) bthš, Gr v. nırıadEng also on gems found there (l.c.; v. also Eränsahr 169), Armazi “Aram.” inscr. (Altheim & Stiel, FuF 35, 1961, 172-178) pyihš; native K art'veli patiaxsi, pitiaxši (Hübschmann, Tschen- keli). Syr. lw. ptahšā, ptakša (often faultily vocalized), aftakšā (Hoffmann, Auszüge p. 34 n. 275). Amm. Marc. XXIII, 6: 14 vitaxae (“id est magistri equitum"), Gr. Hesych. Btorač, read Birač. In dealing with its etymology the indigenous form bythš should; as a matter of course, be given preference before any deviating forms in foreign languages. In its oldest form it is, however, found in Arm bdea&r < *bdiaxs: -d- must be secondary (an original d would have given 7) and go back to a f, voiced because of its proximity to the preceding b, which consequently must be the original initial consonant, not p (pt- would have re- mained); this phonetic state is cogently conclusive in favour of an original form "bitiyaxši-. The first element is *bitīya- ‘the second’, NW form of "dvitiya; Av. (963 sg.) bitya-, MPrth. bdyg (Nyberg, l. e. 237 n. 2; Henning, Iranistik 62 n. 2); the second element has been explained by Pagliaro (RSO XII, 1929, 164 sqq.) as *axsi- ‘eye’ (in Av. derivatives, v. also apaxš); *bītīya-axši- ‘the second eye’ of the King, based on the idea, well attested by the classical authors. and well ana- lysed by P., of the King’s officials as his “eyes”. Thus any etymology starting from initial ptt- is peremptorily excluded; pit- for bit- must be due to a secondary development in the borrowing languages. Pagliaro, l.c. 160-168; Eilers IIJ V, 1962, 209 sq. (quotes Armazi pythé, but ignores bihš!); Benveniste, Titres 65; Rundgren, OrSu XII (1963), 1964, 89-98 (oh!); ete.
būžišn
bizišk [bešk'] a medicine-man, a physician, pl. cas. obl. ~-dn in yātūk- -ān witch- doctors 43%, — Olr. "bišaz-ka- (cf Skr bhisaj-, whence in NW (with meta- thesis) "bizaška- > bizišk (MPrth v. next w.; Arm. lw. bžišk), in SW *bisadka- > *bisa0ka- > bišihk (MPrs bšyhk). In NP the NW form bizisk, later pizisk.
biziškēh medical treatment, healing; me- dicine 448. 1092. — MPrth bzyskyft (MHC).
bod [bwd] 1. consciousness 312. 642%, — 2. scent, fragrance 891°; [incense PR 1112]. — 1. Av. (919) baodah- ‘perception’ ; Paz. boi. 2. Av. (918) baoöi- MPrth bwd?e?r ‘aromatic herbs’ (S); Arm. lw. boir-k‘; MPrs bwy (A-H II); Paz. NP boi. Cf böstän. — bwd 81° is probably a fault for bryn = brin (q. v.).
Bör-gäv [bwl TWR’] n. pr. 47%. - “Hav-
ing cattle with the colour bór", v. next w.
bor-*gil [bwlkl] the name of one of the two armies comman
```


## [2026-09-05T14:38:28.772Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^bun\\b\\|^bun \\|^bun-\\|^bunag\\|bun-dāt\\|bun-dād\\|bundāt\" NYB_vol2_glossary.txt | head -20",
 "description": "Grep Nyberg for bun"
}
```


### [2026-09-05T14:38:28.819Z] TOOL RESULT

```
1038:bun [bwn] bottom 102% ; foundations 1138; root 9375; beginning 81!; the primordial revelation 1118-9-21, 11219; — capital, stock of spiritual values acquired through meri- torious deeds: a ~ i... kartan to add (a value) to a p.'s spiritual stock 7912-14; 6 — bavet it affects a p.’s spiritual stock = detracts from it 652%. 8124, — Av. (968) būna-; MPrthPrs Paz. NP. — V. bundahišn and bunyastak.
1040:bun-dahišn [bwndhän'] the laying of foundations — the primordial creation 100%; cas. obl. ~-éh: pat ~-éh 7911. 80? (Paz. bundahašn). — V. dātan.
6500:bun: ~
```


## [2026-09-05T14:38:31.007Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN bun/buz ===\" && grep -n \"bun 'Grund\\|bun ,Grund\\|^ *[0-9]*\\. *bun\\|buz .Ziege\\|bunjäd\\|bunyäd\\|bunjad\" HRN.txt | head -20; echo \"--- HRN grep buz ---\"; grep -n \"buz\" HRN.txt | head -20",
 "description": "Grep Horn"
}
```


### [2026-09-05T14:38:31.083Z] TOOL RESULT

```
=== HRN bun/buz ===
--- HRN grep buz ---
2256:214. buzurg 'gross'.
2420:Busserl \ poln. LW. huzia, buziak etc. (Miklosich, 37,
4306:. y^erbuze, /erbtu^) *Melone' (wörtl. *Eselsgurke').
4307:phlv. /arböjhia, kharbuzak (PP61.), vergl. höjlna =
10255:Vergl. unter np. xerbuze (oben No. 474) und de
10261:boi^ ^Heilung, buzem 'heilen, retten, befreien' (H. No. 57).
22156:buzem 51,
```


## [2026-09-05T14:41:48.321Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ntxt=open('NYB_vol2_glossary.txt',encoding='utf-8',errors='replace').read()\nlines=txt.split('\\n')\ncnt=0\nfor i,l in enumerate(lines,1):\n    cnt+=l.count('\\f')\n    if i in (1038,1040,1041,1042):\n        print(i,'leaf',cnt,'=> printed p.',cnt-8, l[:200])\nEOF\necho \"--- bunyastak ---\"; grep -n \"bunyastak\\|bunyast\" NYB_vol2_glossary.txt | head",
 "description": "Locate Nyberg bun page"
}
```


## [2026-09-05T14:41:49.707Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN 'bun' ===\"; grep -n \"bun\\b\" HRN.txt | grep -iv \"buzurg\\|verbun\\|bunt\" | head -30",
 "description": "Grep Horn for bun"
}
```


### [2026-09-05T14:41:50.177Z] TOOL RESULT

```
1038 leaf 60 => printed p. 52 bun [bwn] bottom 102% ; foundations 1138; root 9375; beginning 81!; the primordial revelation 1118-9-21, 11219; — capital, stock of spiritual values acquired through meri- torious deeds: a ~ i... kart
1040 leaf 60 => printed p. 52 bun-dahišn [bwndhän'] the laying of foundations — the primordial creation 100%; cas. obl. ~-éh: pat ~-éh 7911. 80? (Paz. bundahašn). — V. dātan.
1041 leaf 60 => printed p. 52 bunyaštak [bwnyštk'] primordial cosmic principle 6211, 645, — Paz. bunyašt, bun- yast, Skr. v. mūlāspada.
1042 leaf 60 => printed p. 52 burritak [bwlytk'] pt. cut off: ~-dumb 30? = brit-dumb (g. v.) — From burritan, burr-, secondary form of britan, — NP.
--- bunyastak ---
1038:bun [bwn] bottom 102% ; foundations 1138; root 9375; beginning 81!; the primordial revelation 1118-9-21, 11219; — capital, stock of spiritual values acquired through meri- torious deeds: a ~ i... kartan to add (a value) to a p.'s spiritual stock 7912-14; 6 — bavet it affects a p.’s spiritual stock = detracts from it 652%. 8124, — Av. (968) būna-; MPrthPrs Paz. NP. — V. bundahišn and bunyastak.
6503:ec) : bunyastak
```


### [2026-09-05T14:41:50.234Z] TOOL RESULT

```
=== HRN 'bun' ===
2352:4316), vergl. gözbun *Wallnussbaum*.
2356:af/. vana 'Baum'; oss. d. ^bun, t. -bin *Wald' (67);
2358:arm. LW. bun 'Stamm (eines Baumes), Schaft*.
2359:229. {2)bun 'Fundament, Grund*, vergl. bunyad {*bundad),
2360:aw. buna- 'Grund, Boden'; phlv. bun, mand. LW.
2362:Unterstes'; arm. bun 'Natur, (pvaig\ adj. naturalis,
2364:kurd. bim; oss. d. bun, t. bin 'Boden', t. bin 'unter
2366:bun *unter*, daneben wündr 'Erde, Boden.
2376:^) Hübschmann, No. 61, wirft zwei verschiedene arm. bun
4478:wa/. Imbun,
9899:228. Vergl. auch servbun *Cypressenbaum (Sahn. I, 156
9900:Vers 489, 160 Vers 561), /ärbun 'Teufelszwirn' (AM.
19139:bun 229.
22155:bun 228, 229.
```


## [2026-09-05T14:41:58.484Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2345,2380p' HRN.txt; echo \"=== HRN Ziege ===\"; grep -n \"Ziege\" HRN.txt | head -20",
 "description": "Print Horn 228-229 and grep Ziege"
}
```


### [2026-09-05T14:41:58.536Z] TOOL RESULT

```
Um vor Täuschungen zu bewahren, sei hier erwähnt,
dass dieses von Vullers construirte persische bul
vielmehr das arabische ebu% bu'l 'Vater des . . . .' ist,
welches secundär auch vor persische Worte getreten
ist; bulhös ist btt^l heves (Nöldeke, mündliche Mit-
teilung).
228. {i)hun XBaum)stamm, -Stumpf (Sahn. III, 1742 Vers
4316), vergl. gözbun *Wallnussbaum*.
Käs. bend, bene (s. v. direkt)?
aw. vanä' 'Baum'; phlv. van; ai. vdna- 'Baum,
Wald'.
af/. vana 'Baum'; oss. d. ^bun, t. -bin *Wald' (67);
bei. gvan, gön Vilde Pistazie (?) (133).
arm. LW. bun 'Stamm (eines Baumes), Schaft*.
229. {2)bun 'Fundament, Grund*, vergl. bunyad {*bundad),
aw. buna- 'Grund, Boden'; phlv. bun, mand. LW.
NDJD Tundament'; ai. budhnd^^) 'Boden, Grund,
Unterstes'; arm. bun 'Natur, (pvaig\ adj. naturalis,
genuinus Cangestammt') 2).
kurd. bim; oss. d. bun, t. bin 'Boden', t. bin 'unter
(66); bei. biinä *unten* (42); wa;^'. bön, §iyn. bon, sar.
bun *unter*, daneben wündr 'Erde, Boden.
np. bune bedeutet dann auch 1) 'Haus, Heimat*
(Sa dl, Bostän, 8, 117), dazu arm. bnak 'Wohnort'
*) Hh'^hnd', vergl. Hörn, Am. Journ. of Phil. XI, 90. Jackson,
Avesta Grammar, S. 273, hat die awestisohe Vertretung von Nasalis
sonans durch u, ü angenommen, ebenso Dr. Andreas (nach brieflicher
Mitteilung), während Bartholomae, Ind. Forsch. I, 492, anderer
Meinung ist. Für aw. buna- — das ich Übrigeos bunna- lese (KZ. 32,
577) — nimmt der Letztere als arische Grundform ^bhundJina- an
(Studien II, 94).
^) Hübschmann, No. 61, wirft zwei verschiedene arm. bun
zusammen. Vergl. auch S. Bugge KZ. 32, 5, der Indog. Forsch. I,
455 noch arm. p^unj dazu stellt.— 53 —
(vgl. de Lagarde, GgA. 1871 Seite 1103, 1104);
2) *6epäck', phlv. bunak *Gepäck, La^er', Nöldeke,
=== HRN Ziege ===
2248:213. bu» *Ziege, Bock', bme (AM. S. 10, Zeile 1 v. u.), buj,
2249:Semnän : boca 'junge Ziege' ; wohl nicht np. bece, wie
2253:'Bock', bukka- 'Ziege'; arm. buc 'Lamm' (H. No. 60).
2712:phlv. pacm (Bund.) ; bei. pädin, n. päsin 'Ziegenbock,
2713:männliche wilde Ziege* (290).
4431:488. x^Ht 'Ziegel, Backstein'.
4432:aw. istya- 'Ziegel, Backstein' ; phlv. /ist ; skr. isfakOr-
8106:notirt : hüzle *junge Ziege', desle 'Händchen', yellele 'Bischen, Stückchen*,
8176:942. göspendj gösfend 'Kleinvieh, Schaaf, Widder, Ziege'.
8660:'Haar (eines Menschen), Ziegenhaar' (247).
10208:42. azg (d. i. azak) 'Ziege (PPÖl.).
10209:ai. ajd' *Bock , ajd- 'Ziege' ; lit. osys, lett. aßs *Ziegen-
10210:bock*, ozMi *Ziege'. Dazu wohl auch arm. aic (H. No. 16),
10211:gr. al^ und aw. iza^na- 'aus (Ziegen)fell- (?) , ledern
```


## [2026-09-05T14:41:59.714Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HUB bun ===\"; grep -n \"bun 'Fundament\\|229\\. \\|buz\\|Ziege\" HUB.txt | head -20",
 "description": "Grep Hübschmann"
}
```


### [2026-09-05T14:41:59.764Z] TOOL RESULT

```
=== HUB bun ===
933:213. Das in der Anmerkung erwahnte phi. xarbuz (Bdh.
936:vor: xarbuz eine Ziegenart, oqv^ Deuter. 14, 5 und
948:fehlt. — Dazu auch afgh. LW. buzarg *a saint, an elder,
1013:229. Ich nehme daher nach wie vor ein einheitliches arm.
1938:488. Lies afgh. LW. xa^ta 'Ziegel*.
3066:dafur buztna, buzina etc. gebraucht.
3811:51. Was soil Kanbujiya- bedeuten? Arm. buz-em etc. halte
5111:np. buzurg gross* = ap. vazrka-, arm. vzurk, vzruk (vgl.
5188:das auf ein altphl. vaz'rkan (= np. buzurgdn, ap. vazrkdnam)
5222:Elise 20, 5) = np. buzurg, phi. inschr. vzrkan (s. oben),
5375:Tab. 140, 480; YiztbuzU (Joh. Kath. 54) = p. YazdbdzS^,
5618:vznik gross = np. buzurg; v^ni 'Stein, Fels', zd. vaema-?;
5746:neben paz. vazurgi *Gr5sse' Shk. 272, np. buzurg, Oflfenbar
6383:201; burrfdan *schneiden H. 212; buz 'Ziege, Bock* H. 213
6385:band *Band* H. 219; bus 'Mahne H. 220; bun 'Fundament
6421:positis natiirUoh b statt r, vgl. phi. xarbuz, np. xarbanda, darband,
6444:dak *Trunkenbold' = np. xarbanda ; xarbnz 'eine Ziegenart'
6445:= phi. syr. talmud. xarbuz 'Esel-ziege*; Xoroh-but N. pr.
7879:rizetn (P. 13 x^airizqm) ace. sg., nur yt. 10, 14; buziirf/
7895:azat *frer {g^) H. 19; hazU 'Arm {g'^h) H. 167; huz ^Ziege'
```


## [2026-09-05T14:42:09.439Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2244,2262p' HRN.txt; echo \"=== HUB 229 ===\"; sed -n '1005,1030p' HUB.txt; echo \"=== HUB 213 ===\"; sed -n '928,955p' HUB.txt",
 "description": "Print Horn 213 and Hübschmann 213/229"
}
```


### [2026-09-05T14:42:09.500Z] TOOL RESULT

```
wa;^. warünam^ warittam 'schneiden, mähen, scheeren'
(Tomaschek, 867, und nach ihm auch Geiger, Laut-
lehre des Balücl § 7, 2, stellen dieses Wort meiner
Meinung nach fälschlich zu skr. {/'rav-, lav-),
213. bu» *Ziege, Bock', bme (AM. S. 10, Zeile 1 v. u.), buj,
Semnän : boca 'junge Ziege' ; wohl nicht np. bece, wie
Houtum-Schindler ZDMG. 32, 535 meint.
aw. büza- 'Bock'; phlv. büj, vergl. /ar^bes:^ yßr^btj
(lies /ar]6w0, ;far]6wj'), Bund. 3); skr. vergl. btikka-
'Bock', bukka- 'Ziege'; arm. buc 'Lamm' (H. No. 60).
kurd. bizin ; af/. wuz ; bei. LW. bfiz (37) ; wa;^. buc,
bilc, sangl. wuz, minj. woza, si/n. sar. waz,
214. buzurg 'gross'.
mäz. bazarg.
*) Kä§. hürndn etc. haben secundär wieder das alte rn des Praesens
erhalten; dialektisch findet sich die Überführung in die neunte Klasse
häufig (vergl. Fr. Müller SWAW. Vol. XLV, 1864, Seite 283, Hern,
KZ. 32, 580 No. 6).
*) Bartholomae setzt Studien II, 107 Anm. 4, 180 die Wurzel
=== HUB 229 ===
*) ^S^' P^^- viSkar *Jagd' naoh Justi, aber 'wilderness* nach
West..^ 31 ~
228. Arm. bun 'Starnm, Schaft* ist nicht = np. bun *Baum'
(in gdz^bun^ sarv-hun etc.) = zd. vana- *Baum* = phi.
van, da ein aus dem Mittelpersischeii ins Altarmeni-
sche entlehntes "^van hier eben *van, nicht bun lauten
wurde. Also ist Horn's Bemerkung 2) zu Nr. 229
nicht richtig.
229. Ich nehme daher nach wie vor ein einheitliches arm.
hun *Stanun, Stiel, Schaft, Abstammung, Ursprung,
Grund, Wesen, Ende' an = paz. phi. bun 'Grundlage,
Wurzel, Ursprung, Anfang', skr. budhna- *Boden, Grund,
das Unterste, Fuss eines Baumes, Wurzel', gr. nv&jLi/jy
*Grund, Boden, unterste Ende, Stammende*. Vgl. arm.
nizakabun 'Lanzenschaft* -^ np. bun i nEf'a 'Lanzen-
schaft*, Gegensatz arm. nizdkateg 'Lanzenspitze*. Im
Falle aber, dass arm. bun aus alterem *budn ent-
standen ware, musste es fiir original gelten. Horn's
Behauptung in Anm. 1 : idg. ^ = zd. u, u ist trotz
Jackson und Andreas unerwiesen und falsch. Arm.
p'ww/ 'Halm* geh5rt trotz Bugge nicht hierher, ebenso
wenig np. buna *Lager, Gepack\ bal. LW. bunag *Gepack*
(Geiger, Lautlehre p. 24), arm. bnak 'Wohnung',
bnakem Vohne'.
231. Np. hiinafSu *Veilchen ^ phi. vanavsak (fiir vanafsak)
nach Fr. Muller WZKM. 7, 368 = zd. ^vanavaxsa-
=== HUB 213 ===
*grndmi zu grtnami (f'estgruss an Roth p. 186).
^) Bartholomae, Stud. II, 107 setzt als Grundforra *bhrmtanai
an, aber der persrsche InfinitiT wurde von der Wurzel gebildet, lautete
also wohl *brUanaiy, Als idg. Particip pass, setzt B. auch ^bhfritd-s
neben *bhrU6'8 (Studien II, 180) an.— 29 -
213. Das in der Anmerkung erwahnte phi. xarbuz (Bdh.
57, 8, West, PT. I, 48) = 'Esel-ziege, das Noldeke
im Syrischen nachweist, liegt auch im Armenischen
vor: xarbuz eine Ziegenart, oqv^ Deuter. 14, 5 und
nach Franker s Mitteilung im babylonischen Talmud,
Tractat HuUin 59*", ist also echt. — Np. hii» auch im
Afghanischen als LW. haz a he-goat*, bza a she-goat',
bdzina 'Maroquin . — Auflfallig sind die dialektischen
(semn. wa;j.) Formen mit c, in denen wohl ein Suffix
steckt.
214. Im Altpersischen ist vazrka- gross' zu lesen mit r-
Vokal (KZ. 27, 111), im Phi. vazrk^) (HajtabSd-Inschrift
Z. 6), spater vazurg Gl. and Ind. 236, paz. guzurg
Min. 61. 95, np. hu»urg» Horn's Bemerkungen gegen
den r-Vokal im Persischen (KZ. 32, 572 flg.) sind ver-
fehlt. — Dazu auch afgh. LW. buzarg *a saint, an elder,
an ancestor, 2) great, venerable'.
215. Zu ba^m *Gesellschaft, Gastmahl, Gelage' (Fird. I,
23, 13), afgh. LW. bazm *an assembly, a company, a
banquet' geh5rt, wie Fr. Miiller schon bemerkt hat
(WZKM. 7, 368), das arm. LW. bazmel sich zu Tische
setzen , dvanXivai Marc. 6, 39 etc., bazmakan *der zu
Tische sitzt, Gast' etc. Dazu np. bazmgah 'Ort des
```


## [2026-09-05T14:42:23.687Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN bottom ===\" && grep -n \"^bottom\\|bottom, n\" KLN_1966.txt | head -10; echo \"=== KLN butcher ===\"; grep -n \"^butcher\\|butcher, n\" KLN_1966.txt | head -5; echo \"=== KLN buck ===\"; grep -n \"^buck,\" KLN_1966.txt | head -5",
 "description": "Grep Klein"
}
```


### [2026-09-05T14:42:23.757Z] TOOL RESULT

```
=== KLN bottom ===
5378:bottomry
5419:bottomry,  n.,  bond  by  which  the  vessel  is  hypo¬ thecated  for  the  loan  of  the  money  advanced on  the  security  of  the  ship.  —  A  blend  of  bot¬ tom,  in  the  sense  of  ‘ship’,  and  Du.  bodemerij, ‘bottomry’,  fr.  MLG.  hodmen,  verbodmen,  fr. bodem,  ‘bottom;  to  lend  a  ship  and  its  cargo’.
=== KLN butcher ===
5955:butcher,  n.  —  ME.  bocher,  boucher,  fr.  OF. bochier  bouchier  (F.  boucher),  ‘butcher  ,  lit. ‘one  who  slaughters  bucks’,  fr.  bouc,  ‘buck’.  See buck,  ‘male  deer’,  and  -er  (representing  OF. -ier).
5957:butchery,  n.  —  ME.  bocherie,  fr.  OF.  bocherie, boucherie  (F.  boucherie ),  fr.  boucher.  See  but¬ cher  and  -y  (representing  F.  -ie).
=== KLN buck ===
5773:buck,  n.,  the  body  of  a  wagon  (dial.)  —  OE.  buc, ‘body’,  rel.  to  ON.  bukr,  Swed.,  Norw.  buk, Dan.  bug,  OFris.  buk ,  MDu.  buuc,  Du.  bulk, OHG.  bdh,  bCthhes,  MHG.  bitch,  G.  Bauch, ‘belly,  abdomen’,  fr.  I.-E.  base  *bhdu-,  *bhu-, ‘to  swell’,  whence  also  boil,  ‘inflammation’.  Cp. bucket.  Cp.  also  the  second  element  in  sillabub,
5777:buck,  t.v.,  to  soak  in  lye.  —  ME.  bouken,  rel.  to MLG.  biiken  (whence  Swed.  byka,  Norw.  bykja, Dan.  byge),  G.  bauchen ,  beuchen,  and  to  beech (q.v.);  lye  was  orig.  made  of  beech  ashes, buck,  n.,  male  deer,  stag;  dandy.  —  ME.  bucke, fr.  OE.  bucca,  ‘he-goat’,  bucc,  ‘male  deer’,  rel. to  OS.  buck,  MDu.  buc,  boc  Du.  bok,  OHG., MHG.  boc,  G.  Bock,  ON.  bokkr,  bukkr,  Dan. buk,  and  cogn.  with  Avestic  biiza,  ‘buck’,  Pers. buz,  ‘buck,  goat’.  Arm.  buc,  ‘lamb’.  OIr.  bocc and  W.  bwch  are  prob.  Teut.  loan  words.  Cp. butcher.  Cp.  also  bocking,  ‘smoked  herring’,  and the  second  element  in  kleeneboc,  gemsbok,  grys- bok,  springbok.
```


## [2026-09-05T14:42:24.352Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls -la BQT_v1_pages.txt && grep -n \"pdf page 27[0-9]\" BQT_v1_pages.txt | head -20",
 "description": "Inspect BQT v1 pages file"
}
```


### [2026-09-05T14:42:24.399Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 2247721 Sep  4 14:06 BQT_v1_pages.txt
```


## [2026-09-05T14:42:31.603Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -5 BQT_v1_pages.txt && grep -n \"pdf page\" BQT_v1_pages.txt | head -5 && grep -c \"pdf page\" BQT_v1_pages.txt",
 "description": "Check BQT page tag format"
}
```


### [2026-09-05T14:42:31.659Z] TOOL RESULT

```
۱ ۵ ۱! ۱
7 موم ۳ لام
م ۱ 0 و طق صفرررنیاعدریرماروی
۰ ۱ "۳
۳
0
```


## [2026-09-05T14:42:32.480Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5370,5385p' KLN_1966.txt",
 "description": "Print Klein bottom area"
}
```


### [2026-09-05T14:42:32.541Z] TOOL RESULT

```
bore,  n.,  tidal  wave.  —  ME.  bore,  ‘wave,  billow’, fr.  ON.  bara,  ‘wave’,  lit.  ‘that  which  is  borne or  carried’,  rel.  to  ON.  bera ,  ‘to  bear’.  See  bear, ‘to  carry’.
bore,  past  tense  of  bear.  —  ME.  See  bear,  ‘to carry’.
Boreades,  n.,  pi.  the  wind  gods  Zetes  and  Calais, (Greek  mythol.)  —  L.,  fr.  Gk.  BopedSoa,  lit.  ‘the sons  of  Boreas’,  fr.  Bop£a?.  See  Boreas, boreal,  adj.,  pertaining  to  Boreas;  northern.  — L.  borealis,  fr.  boreas.  See  next  word  and  adj. suff.  -al.
Boreas,  n.,  the  god  of  the  north  wind  in  Greek mythology.  —  L.,  fr.  Gk.  Bop &u.q,  fr.  (5op£ai;, ‘north  wind’,  which  is  of  uncertain  origin.  It possibly  stands  for  I.-E.  *gwore-yas  and  orig. meant  ‘mountain  wind’,  and  is  cogn.  with  OI. girth,  Avestic  gairi,  ‘mountain’,  Alb.  gur,  ‘rock’, OSlav.  gora,  ‘mountain’,  Lith.  g'tre,  ‘forest’.  Cp. bora,  Boreades,  boreal  and  the  second  element in  Hyperborean.  Cp.  also  Croat, borecole,  n.,  kind  of  cabbage.  —  Prob.  fr.  Du. boerenkool,  lit.  ‘peasant’s  cabbage’.  See  boor and  cole.
boric,  adj.,  pertaining  to,  or  containing,  boron (chem.)  —  See  boron  and  -ic.
Boris,  masc.  PN.  —  OSlav.,  lit.  meaning  ‘fight’, rel.  to  OSlav.  barjg,  brati  (for  *bor-ti),  ‘to  fight  , and  cogn.  with  L.  ferire,  ‘to  strike’.  See  bore, ‘to  pierce’.
born,  borne,  pp.  of  bear.  —  ME.  boren,  fr.  OE. boren,  pp.  of  beran.  See  bear,  ‘to  carry', borne,  adj.,  narrow-minded.  —  F.,  lit.  "limited’.
boron
bottomry
pp.  of  borner,  ‘to  limit’,  fr.  OF.  (=  F.)  borne, ‘limit’,  fr.  earlier  bodne,  a  word  of  Gaulish origin.  See  bourn  and  bound,  ‘limit’.
boron,  n,,  name  of  a  non-metallic  element  ( chem .) —  Originally  called  by  the  English  chemist  Sir Humphrey  Davy  (1778-1829)  boracium,  because drawn  fr.  boracic  (—  boric)  acid.  See  borax. The  ending  -on  in  boron  is  due  to  the  analogy of  carbon ,  where,  however,  the  ending  -on  be¬ longs  to  the  stem.
borough,  n.  —  ME.  burgh,  burwe,  fr.  OE.  burg, burh,  burg,  rel.  to  OS.,  OFris.,  burg,  ‘castle’, ON.  borg,  ‘wall,  castle’,  MDu.  burch,  borch, borcht,  Du.  burchl,  burg,  OHG.  burg,  burc, buruc,  ‘fortified  place,  citadel’,  MHG.  burc, G.  Burg,  ‘castle’,  Goth,  baurgs,  ‘city’,  OE.  beorg, etc.,  ‘mountain’.  These  words  prob.  derive  fr. I.-E.  base  *bhergh-,  ‘high’,  whence  also  Arm. berj,  ‘high  place',  OSlav.  bregu,  ‘bank  (of  a river)’,  W.  bera,  ‘stack,  pyramid’,  Mir.  bri,  acc. brig,  ‘hill’,  Toch.  A  parkas,  ‘long’,  Hitt,  parkush, ‘high’,  OI.  bfhdnt-,  Avestic  blrlzant-,  ‘high’, OCeltic  Brigantes,  lit.  ‘the  high  ones’  (cp.  Bur¬ gundians,  fr.  Late  L.  Burgundiones,  lit.  ‘high¬ landers’),  prob.  also  OL.  forctus,  ‘good’,  L. fortis  (fr.  OL.  forctis),  ‘strong’,  see  Walde-Hof- mann,  LEW.,  I, pp.  535-36,  s.v. fortis, and  Kluge- Mitzka,  EWDS.,  p.67,  s.v.  Berg.  Cp.  barrow, ‘mountain,  mound’,  bourgeois,  burgage,  burgess, burgh,  burgrave,  Burgundy,  canterbury,  faubourg, gaussbergite,  ghetto,  Hapsburg,  hauberk.  Cp.  al¬ so  Brahma,  fort,  and  the  second  element  in  bar- bicane.  Cp.  also  the  suff.  -bury  in  English  place names,  which  comes  fr.  OE.  byrig,  the  dative sing  of  OE.  burg.  Base  *bhcrgh-  is  prob.  an  en¬ larged  form  of  base  *bher-,  ‘to  carry,  lift’.  See bear,  ‘to  carry’.
Borrichia,  n.,  a  genus  of  plants  of  the  thistle family  (bot.)  —  ModL.,  named  after  the  Danish botanist  Olof  Borrich.  For  the  ending  see  suff.
-ia.
borrow,  tr.  and  intr.  v.  —  ME.  borwen,  fr.  OE. borgian,  ‘to  lend;  to  borrow’,  fr.  borg,  ‘pledge, security',  rel.  to  ON.  borga ,  ‘to  become  bail  for, to  guarantee’,  MDu.  borghen,  ‘to  protect,  guar¬ antee’,  OHG.  boragen,  borgen,  ‘to  beware  of; to  spare;  to  remit  a  debt',  G.  borgen,  ‘to  bor¬ row;  to  lend’,  biirgen,  ‘to  become  bail  for,  to guarantee’,  OE.  beorgan,  OHG.  bergan,  ‘to  hide, save’.  See  bury.
Derivatives:  borrow-er,  n.,  borrow-ing,  n.
```


## [2026-09-05T14:42:38.405Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"bottom\" KLN_1966.txt | head -20",
 "description": "Grep Klein bottom entry"
}
```


### [2026-09-05T14:42:38.454Z] TOOL RESULT

```
1126:aback,  adv.  —  OE.  on  bzc.  See  a-,  ‘on’,  and  back, abacus,  n„  1)  frame  with  beads  for  calculation; 2)  (archil.)  slab  at  the  top  of  a  column.  —  L. abacus,  fr.  Gk.  afjaE.,  gen.  afiaxoc;,  ‘a  square tablet  strewn  with  dust’,  fr.  Heb.  abhdq,  ‘dust’, fr.  root  a-b-q,  ‘to  fly  off’.  The  first  type  of  abacus was  a  board  covered  with  dust,  whence  its  name. Abaddon,  n.,  the  bottomless  pit.  —  Heb.  dbhad- ddn,  ‘destruction’,  fr.  abhadh,  ‘he  perished’,  which is  rel.  to  Aram,  abhadh,  ‘he  perished’,  Ugar.  ’hd, ‘to  perish’,  Ethiop.  abada,  ‘he  wandered  about’, Arab,  abada,  ‘it  (the  animal)  fled  in  fright’, abaft,  adv.,  astern,  aft;  prep.,  behind.  —  Formed fr.  a-,  ‘on’,  and  OE.  beseftan,  fr.  be,  ‘by,  at’, and  seftan.  ‘behind’.  See  be-  and  aft. abalienate,  tr.  v.,  1)  to  alienate;  2)  to  remove.  — L.  abalienatus,  pp.  of  abalienare,  ‘to  remove’, lit.  ‘to  make  alien  from’,  fr.  ab-  and  alienare. See  alienate.
1277:abysm,  n.,  poetic  for  abyss.  —  OF.  abisme  (F. abime),  fr.  Eccles.  L.  *abismus  (whence  also OProven?.  abisme,  Sp.  and  Port,  abismo),  form¬ ed  on  analogy  of  words  ending  in  -ismus  (fr.  Gk. -ia[x6?;  see  -ism),  fr.  L.  abyssus.  See  abyss. Derivative:  abysm-al,  adj. abyss,  n.  —  L.  abyssus,  ‘bottomless  pit’,  fr.  Gk &(Juccroc;  (scil.  Aluvt]),  ‘bottomless,  unfath¬ omed  (pool)’,  fr.  a-  (see  priv.  pref.  a-)  and (3uaa6?,  ‘depth,  bottom’,  which  is  related  to (Julios,  of  s.m.  Cp.  abysm.
3130:Apollyon,  n.,  the  destroying  angel  of  the  bottom¬ less  pit,  the  equivalent  of  Heb.  dbhaddSn  (see Abaddon).  —  Gk.  ct7xoXXuciJv,  pres.  part,  of £txoXX6eiv,  ‘to  destroy  utterly’,  fr.  <x7xo  (see apo-)  and  6XX6eiv,  ‘to  destroy’,  which  is  rel.  to SXe&pot;,  ‘destruction,  ruin’.  Cp.  Olethreutidae and  the  second  element  in  Azolla. apologetic,  adj.,  1)  apologizing;  2)  defending  in writing  or  speech.  —  F.  apologetique,  fr.  L.  apo- logeticus,  fr.  Gk.  dc7ToXoyyTi.x6;,  ‘fit  for  de¬ fense’,  fr.  ixTtoXoyeta^ai,  ‘to  speak  in  defense’, fr.  aTxoXoyia,  ‘defense’.  See  apology.
4506:base,  n.,  bottom;  foundation,  pedestal.  —  F.,  fr. L.  basis,  fr.  Gk.  (idci^,  ‘a  stepping,  step,  pede¬ stal,  foot,  base’,  from  the  stem  of  (3aivto,  ‘I  go’, which  prob.  stands  for  *(3avLCt>,  fr.  *P<x|z-io), fr.  l.-E.  base  *gwem-,  'to  go;  to  come’,  whence also  L.  venio  (prob.  for  *gwmio),  ‘I  come’,  Goth. qiman,  OE.  cuman,  ‘to  come’.  See  come  and  cp. venue,  ‘arrival’.  Cp.  also  basis,  abasia,  acrobat, aerobatics,  amphisbaena,  Anabaena,  anabas,  ana¬ basis,  -bates,  bathmism,  batophobia,  bema,  cata- basis,  diabase,  adiabatic,  diabetes,  ecbatic,  gyno- base,  hyperbaton,  metabasis,  Odobenus,  Ori- batidae,  parabasis,  presby-,  stereobate,  stylobate. As  a  term  of  chemistry  base  was  introduced  by the  French  chemist  Guillaume-Fran^ois  Rou-
4762:Benthamite,  n.,  a  follower  of  Bentham.  —  See prec.  word  and  subst.  suff.  -ite. benthos,  n.,  the  fauna  and  flora  of  the  bottom  of the  sea.  —  Gk.  psvffo!;,  ‘depth  of  the  sea’,  prob. rel.  to  ViStoz.  ‘depth’,  but  influenced  in  form by  ttsvOoc.  ‘grief’.  See  bathos, bentonite,  n.,  a  porous  clayey  mineral.  — Named after  Fort  Benton  in  Wyoming,  U.S.A.  For  the ending  see  subst.  suff.  -ite. benumb,  tr.  v.  —  ME.  binomen,  pp.  of  biniman, fr.  OE.  beniman,  ‘to  deprive’,  lit.,  ‘to  take  away’.
5378:bottomry
5416:Derivatives:  bottle,  tr.  v.,  bottl-ed ,  adj. bottom,  n.  —  ME.  botme,  botome,  fr.  OE.  botm , ‘lowest  part,  depth,  bottom’,  rel.  to  OS.  bodom, ON.  botn,  OFris.  boden,  ‘soil’,  Du.  bodem, OHG.  bodam,  MHG.,  bodem,  G.  Boden, ‘ground,  soil,  earth’,  and  cogn.  with  OI.  budh- nah,  Gk.  ‘foundation,  bottom’,  L.
5417:fundus  (metathesis  for  *fudnos),  ‘bottom ;  piece of  land,  farm’,  Olr.  bond  (metathesis  for  *bodn), ‘sole  of  the  foot’.  Cp.  found,  ‘to  establish’,  foun¬ der,  v.,  fund,  fundament,  profound.
5418:Derivatives:  bottom,  adj.  and  v.,  bottom-less, adj.,  bottomry  (q.v.)
5419:bottomry,  n.,  bond  by  which  the  vessel  is  hypo¬ thecated  for  the  loan  of  the  money  advanced on  the  security  of  the  ship.  —  A  blend  of  bot¬ tom,  in  the  sense  of  ‘ship’,  and  Du.  bodemerij, ‘bottomry’,  fr.  MLG.  hodmen,  verbodmen,  fr. bodem,  ‘bottom;  to  lend  a  ship  and  its  cargo’.
5421:Cp.  F.  bomerie,  ‘bottomry’,  which  also  derives fr.  Du.  bodemerij.
5583:break,  tr.  and  intr.  v.  —  ME.  breken,  fr.  OE. brecan,  rel.  to  OS.  brecan,  OFris.  breka,  Du. breken,  OHG.  brehhan,  MHG.,  G.  brechen, Goth,  brikan,  and  cogn.  with  L.  frangere,  past tense  fregl,  ‘to  break’,  OI.  (giri')-bhrdj,  ‘breaking forth  (out  of  the  mountains)’,  fr.  I.-E.  base *bhreg-,  ‘to  break’.  A  parallel  base  *bheg-  ap¬ pears  in  OI.  bhanakti,  ‘he  breaks’,  Arm.  be- kanem,  ‘I  break’,  bek,  ‘broken’,  Olt.  com-boing, ‘he  breaks’.  The  disappearance  of  the  r  in  this secondary  base  is  prob.  due  to  the  nasalization of  the  base.  Cp.  brake,  ‘instrument  for  breaking flax’,  brake,  ‘contrivance  for  stopping  motion’, brash,  braxy,  bray,  ‘to  crush',  breach,  breek, brick,  bricole,  brioche,  brook,  n.  Cp.  also fraction  and  words  there  referred  to. Derivatives:  break,  n.,  break-able,  adj.,  break- agen,  n.,  breaker  (q.v.),  break-ing,  n. breaker,  n.,  one  who,  or  that  which,  breaks.  — Formed  fr.  break  with  agential  suff.  -er. breaker,  n.,  a  small  cask.  —  Sp.  barrica,  ‘cask. See  barrel  and  cp.  barricade, breakfast,  n.  —  Prop,  ‘the  meal  that  breaks  the fast.  Cp.  F.  dejeuner,  ‘to  breakfast’,  fr.  L.  dis- jejunare,  ‘to  break  the  fast’  (see  dejeuner,  dinner). bream,  n.,  a  fish.  —  ME.  breme,  brem,  fr.  F. breme,  fr.  OF.  braisme,  fr.  Frankish  *brahsima, which  is  rel.  to  OHG.  brahsima,  of  s.m.;  prob. fr.  Teut.  base  *brehwan,  ‘to  shine’,  which  is  rel. to  I.-E.  *bherek-,  ‘to  shine,  be  white’.  See  braid, bream,  tr.  v.,  to  clean  a  ship’s  bottom.  —  Du.
7039:Cerion,  n.,  a  genus  of  snails  (zool.)  —  Gk.  x^ptov, ‘honeycomb’,  fr.  >0] po?,  ‘beeswax’.  See  cere,  n. ceriph,  serif,  n.,  a  horizontal  line  at  the  top  or bottom  of  a  capital  letter.  —  Prob.  fr.  Du. schreef,  ‘stroke,  dash’,  which  is  rel.  to  schrijven, ‘to  write’,  fr.  L.  scribere.  See  scribe  and  cp. sanserif.
9880:-ciila,  L.  fern,  dimin.  suff..  corresponding  to masc.  -cuius,  neut.  -culum.  —  Sec  -cule. cul-de-sac,  n.,  a  blind  alley.  —  F.,  lit.  ‘bottom of  a  bag’.  For  the  etymology  of  F.  cut  see  culet. F.  de,  ‘of,  from",  derives  fr.  L.  de,  ‘from,  away from’ ;  see  de-.  For  the  origin  of  F.  sac  see  sac. -cule,  dimin.  subst.  suff.  —  F.  -cule,  fr.  L.  -cuius (masc.),  -cula  (fern.),  or  -culum  (neut.)  Cp.  -cle. culet,  n.,  i)  the  facet  forming  the  bottom  of  a
9882:brilliant;  2)  armor  covering  the  hinder  part  of the  body.  —  F.,  dimin.  of  cul,  ‘backside,  poste¬ rior,  bottom’,  fr.  L.  cuius,  ‘posterior,  fundament’, which  is  cogn.  with  OIr.  cul,  W.  cil,  ‘back’.  Cp. culot,  culotte,  bascule,  recoil  and  the  first  ele¬ ment  in  cul-de-sac.  For  the  ending  see  suff.  -et. Culex,  n.,  a  genus  of  mosquitoes.  —  L.  culex, ‘gnat’,  cogn.  with  OIr.  cuil  (for  *ku-li)  ‘gnat’, W.  cylionen,  ‘gnat,  fly’,  Co.  kelionen,  ‘fly’  and prob.  also  with  OI.  sula-,  ‘spear,  spit’.  These words  possibly  derive  fr.  I.-E.  *kul-,  enlargement of  base  *kd-,  ‘pointed’,  whence  also  L.  caucus, ‘wedge’.  See  coin.
9896:Derivative:  culminat-ion ,  n. culot,  n.,  a  small  sheet  iron  cup  inserted  into  the base  of  projectiles.  —  F.,  ‘bottom  of  lamps  or crucibles,  metal  end  of  crucibles’,  dimin.  of  cul, ‘bottom’.  See  culet  and  cp.  next  word, culotte,  n.,  breeches.  • —  F.,  fr.  cul,  ‘bottom’.  See culet  and  cp.  prec.  word.  Cp.  also  sansculotte, culottic,  adj.,  wearing  breeches.  —  Formed  with suff.  -ic  fr.  F.  culotte,  ‘breeches’.  See  prec.  word, culpability,  n.  —  Late  L.  culpabilitas,  ‘guilt,  cul¬ pability’,  fr.  L.  culpabilis.  See  next  word  and  -ity. culpable,  adj.  —  ME.  culpable,  coupable,  fr.  OF. culpable,  coupable  (F.  coupable),  fr.  L.  culpd- bilis,  ‘worthy  of  blame,  culpable’,  fr.  culpa, ‘blame,  fault’,  which  is  rel.  to  Oscan  kulupu, of  s.m.  It  is  possible  that  the  original  meaning of  L.  culpa  was  ‘blow’,  in  which  case  it  is  quite probably  cogn.  with  Gk.  xoXatpo?  (whence  L. colaphus),  ‘a  blow  with  the  fist,  a  box  on  the ear’,  fr.  I.-E.  base  *qola-,  ‘to  strike,  hew’.  See coup,  and  -able  and  cp.  culprit  and  disculpate, exculpate,  inculpate.
10294:Danaides,  Danaids,  n.  pi.,  the  fifty  daughters  of Danaiis,  king  of  Argos,  who — with  the  ex¬ ception  of  Hypermnestra — killed  their  hus¬ bands,  at  their  father’s  command.  For  this crime  they  were  condemned  to  draw  water  per¬ petually  with  vessels  that  had  no  bottoms (Creek  mythol.)  —  L.  Danaides, fr. Gk.  AavxtSc^, ‘daughters  of  Danaiis’,  fr.  Aava6?  ‘Danaiis’. See  Danaiis.
10584:Derivative:  deemster-ship,  n. deep,  adj.  —  ME.  deop,  dep,  deep,  fr.  OE.  deop, rel.  to  OS.  diop,  OFris.  diap,  Du.  diep,  OHG. tiof,  tiuf,  MHG.,  G.  tief,  ON.  djupr,  Dan.  dyb, Swed.  djup,  Goth,  diups,  ‘deep’,  fr.  Teut.  base *deupa-,  ‘deep’,  corresponding  to  I.-E.  base *dheubh-,  *dhubh-,  whence  Luh.  dubits,  ‘deep, hollow’,  duobe,  ‘pit’,  Lett,  dubens,  ‘bottom’, OSlav.  duno  (for  *dhubno-),  Czech,  Slov.,  etc. dno,  ‘bottom’,  OIr.  domain  (for  *dhubni-),  ‘deep’, domun  (for  *dhubno-),  ‘world',  W.  dwfn,  ‘deep’. Cp.  depth,  dip,  dive,  dope,  dopper.
10771:demeritorious,  adj.,  blameworthy.  —  Formed with  suff.  -orious  fr.  VL.  demeritum,  ‘fault’.  See demerit,  n.,  and  cp.  meritorious, demersal,  adj.,  sunk  to  the  bottom  (said  of  the eggs  of  fish).  —  Formed  with  adj.  suff.  -al  from the  obsolete  verb  demerse,  ‘to  immerse’,  fr.  L. demersus,  pp.  of  demergere,  ‘to  submerge’,  fr.  de- and  mergere,  ‘to  plunge,  immerse'.  See  merge.
14016:exergue,  n.,  space  on  a  coin  between  the  bottom of  the  design  and  the  rim.  —  F.,  fr.  ML.  exer- gum,  lit.  ‘(space)  outside  the  work’,  a  word coined  fr.  Gk.  IE,  ‘out  of’  and  Ipyov,  ‘work’. See  2nd  ex-  and  ergon.
```


## [2026-09-05T14:42:40.048Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"page\" BQT_v1_pages.txt | head -5; echo \"---formfeeds---\"; python3 -c \"\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nprint('ff count',t.count(chr(12)))\nprint(repr(t[:300]))\n\"",
 "description": "Check BQT v1 structure"
}
```


### [2026-09-05T14:42:41.679Z] TOOL RESULT

```
---formfeeds---
ff count 776
'\x0c۱ ۵ ۱! ۱\n7 موم ۳ لام\nم ۱ 0 و طق صفرررنیاعدریرماروی\n۰ ۱ "۳\n۳\nم و اس مر هر وه او\n7 رین خلت ریز یتایب بره ات\nلف\u200cبال ۶۲ .یرک\nا اند کل داي رشب , رمع\nفان تا تا\nرن 9 3\nکرحم تن\nاد شش مرا\nمو رم | مر\nوک رهب اه نات مج\nلش\nوان روکد ور\n۱ و\nطراول ؛ | ع اس\nچاپ دوم فروردین ۱۳۴۳\nبا تجدید نظر کامل\nبسرمایه کنابفروشی ا'
```


## [2026-09-05T14:42:53.813Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nfor f,ln in [('KLN_1966.txt',5416),('KLN_1966.txt',5773),('KLN_1966.txt',5955)]:\n    t=open(f,encoding='utf-8',errors='replace').read().split('\\n')\n    c=0\n    for i,l in enumerate(t,1):\n        c+=l.count('\\f')\n        if i==ln:\n            print(f,ln,'leaf',c,'=> printed pp ~',(c-12)*2,(c-12)*2+1)\n            break\nEOF",
 "description": "Compute Klein page numbers"
}
```


## [2026-09-05T14:42:54.733Z] TOOL CALL #33: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:271 2>&1 | head -60",
 "description": "Fetch Borhan-e Qate page 271"
}
```


### [2026-09-05T14:42:55.701Z] TOOL RESULT

```
KLN_1966.txt 5416 leaf 111 => printed pp ~ 198 199
KLN_1966.txt 5773 leaf 120 => printed pp ~ 216 217
KLN_1966.txt 5955 leaf 124 => printed pp ~ 224 225
```


### [2026-09-05T14:43:01.398Z] TOOL RESULT

```
no scan of BQT covers printed page 271 (see 'scans' in refs_online.json)
```


## [2026-09-05T14:43:10.766Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==112' KLN_1966.txt | head -3; echo \"...tail...\"; awk 'BEGIN{RS=\"\\f\"} NR==112' KLN_1966.txt | tail -3; echo \"=== leaf 110 head ===\"; awk 'BEGIN{RS=\"\\f\"} NR==111' KLN_1966.txt | head -3",
 "description": "Inspect Klein leaf 111 for page numbers"
}
```


## [2026-09-05T14:43:11.996Z] TOOL CALL #35: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nprint(json.dumps(d['BQT'],ensure_ascii=False,indent=1))\n\"",
 "description": "Inspect BQT ref entry details"
}
```


### [2026-09-05T14:43:22.044Z] TOOL RESULT

```
 ambi-,  amphi-.
bother,  tr.  and  intr.  v.  —  Of  uncertain  origin. Derivatives:  bother,  n.,  botheration  (q.v.), bothe r-er,  n.
botheration,  n.,  bother  (colloq.)  —  A  hybrid coined  from  the  verb  bother  and  -ation,  a  suff. of  Latin  origin.
...tail...
bourgeois,  n.,  a  size  of  printer’s  type  (print).  — Named  after  Bourgeois,  a  French  type  founder, bourgeoisie,  n.,  middle  class.  —  F.,  fr.  bourgeois.
See  bourgeois,  ‘middle  class’, bourn,  bourne,  also  burn,  n.,  a  stream.  —  ME. burne,  borne,  fr.  OE.  brunna,  burna,  rel.  to  OS., OHG.  brunno,  ON.  brunnr,  Norw.  brunn,  brynn, Dan.  brand,  Swed.  brunn,  OFris.  burna,  MLG., MDu.  borne,  Du.  bron,  MHG.  brunne,  brun,
G.  Brunnen  and  Born,  Goth,  brunna,  ‘well, spring’,  and  cogn.  with  Gk.  <pp£ixp,  ‘well,  spring’. Arm.  albeur  (gen.  aiber),  ‘source’,  Russ,  brujd, ‘current’,  bruit',  ‘to  stream  with  force’.  For more  cognates  see  barm,  brand,  bread,  brew, broil  (in  both  senses),
=== leaf 110 head ===
.  bordage,  border,  bordure.  Cp. also  prec.  word.
Derivatives:  border,  v.,  border-ed,  adj.,  border¬ er,  n.
bordure,  n.,  a  border  around  a  shield  (her.)  —
```


### [2026-09-05T14:43:23.585Z] TOOL RESULT

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
 "notes": "Persian OCR is mediocre: headwords and Mo'in's footnotes (e.g. '۱ - رك: ابر کوه', Pahlavi/Avestan Latin forms) are mostly readable but with many character errors; search with short substrings and tolerate errors. BQT_v1_pages.txt was built from the djvu.xml; BQT_v2_pages.txt from pdftotext -layout of the _text.pdf. Volumes 3–5 (roughly ح/خ–ی and the تعلیقات volume) are not online in full text; for those use Dehkhoda quotations of Borhan/Mo'in via vajehyab/abadis/parsi.wiki, or page images on noorlib (different edition). | Vols 3-5 scans (image only) in incoming/BQT; vols 1-2 have OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt. Offsets verified by eye at several pages (v3 drifts by ~4 pages; page_map gives exact positions once built). || UPDATE: vols 3-5 now downloaded (image-only PDFs, verified as Mo'in's edition from title pages and the Latin footnotes) and OCRed locally. Image-only scan OCRed locally with tesseract 5 (fas.traineddata from github.com/tesseract-ocr/tessdata_fast, stored in incoming/_tessdata). *_pages.txt = 'fas' model (best for Persian); *_pages_faseng.txt = 'fas+eng' model (better for the Latin-script Pahlavi/Avestan etyma, worse for Persian). Pages separated by \\f; leaf N = N-th \\f-block 0-based = PDF page N+1. Search with short substrings and tolerate OCR errors. Provenance caveat: picofile is a general file host, the uploads are not from a library; treat as a grey copy (the book is in copyright in Iran). | vol 4 (م–ی) OCR text, tesseract fas+eng, pages tagged [pdf page N], printed = pdf+1917 | vol 5 (ta'liqat) OCR text, printed = pdf-5 | vol 3 (ش–ل) OCR text (689/721 pages), printed ≈ pdf+1203..1209",
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


## [2026-09-05T14:43:42.986Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for L in 489 490 491 492 493; do echo \"=== leaf $L ===\"; awk -v N=$((L+1)) 'BEGIN{RS=\"\\f\"} NR==N' BQT_v1_pages.txt | head -25; done",
 "description": "Print BQT v1 leaves around printed p.271"
}
```


### [2026-09-05T14:43:44.629Z] TOOL RESULT

```
=== leaf 489 ===
است درحضرموت. کویت. درآنجا چاهی امت که
ارواح کفار و عنافین آنجا جمم شوند .
بر هو 3 - با واومجهول بروزن محموده
چیزیرا کوبند که ترديك بوختن رسیدموحرارت
آشس رن آ ثرا کردانیده و زرد کرده باشد .
بر هون -» بفتح اول بر رزن مجنون ؛
هر چیز مان خالی ۳ مانئد حالهٌ ماه
1
و دایره‌ای که از پرگار کشند - و چوب بندی
و خاربست- وحصار- و در خانه ومحوطه_ وغانة
کوچك را نیز کفته‌اد - وآریش و زیت رائیز
رازبانج است ۱ .کویند از دوزبکه آقاب‌ببرج
حمل میرود ح رکه هر روز ز يك درهم نخم‌راز بانه
با يك درهم فند سفید سفوف کند و تا سه ماه‌در
خوردن آن مداومت نمابد در نمام سال مریض
نشود ؛ و جمیم گزندکان تخم رازبانه خورند
بجهت روشنایی چشم . و افمی چشم‌خود راببهت
روشنابی و نقوت برآن مالد . #
برههی ؟ » بتح اول و ثالی و حیم
بروزن قلمزن» بمعنی بت‌پرست و زناربند باشد
و حکما و دانثه‌ندان و پیر و مرشد بت‌پرستان
و هندوان و آته تش‌پرستانرا هم میگوند -واصیل
و نجیب هنود را نز برهم نگویند » و بفتح‌اول گویند - و بمعنی کمر گاه و کم رکوه هم بنظر
و سکون انی بوزن کر کدن هم آمده است . آمده است ؛ و بنم اول لبز درستست .
دل ۲ ۰ ۳ . ۱
=== leaf 490 ===
و کار بهوده و بیفایده کردن باشد . #
پر ود قلكك - کنابه ازماه است که‌قمر
باشد - و ژحل را نی زگفته‌اند 3
بر لژزن - بکر اول و تحتانی مجهول
بروزن شیمن » پرویزن باشد که بعربی غرپال
و علپال کوبند ۴ -و بممئی ترشی بالا هم آمده
لت - و ابه‌ای را نز گویند که از کل ساخته
باشند و بربالای آن‌نان پزند » و بقتح اول‌بمعنی
بر لژ ۵ » بکسر اول وئالث مجهولبروزن
سفیده . صمفی است دوایی شبیه بمسطکی وآن
سبك و خشك و بدبوی‌میباشد » و حمربان‌باززد
ریانما۰ با حای بی شطذ ولام
مشدد بالف کشیده , بربان باتره و پودنه وترخان
و نان و ییاز اون ۰
بریحی ۱ با چیم بر وزن رسیدن »
تنوری باش د که در آ نکماج و نان سنکك پزند ۰
و جربی فرن گوبند بضم فا .
بریخ زدن- بنتجبای حطی, کنایه از
خاطر محو نمودن و تلم نبردن و فرأمو شکردن
سونایدیدساختن‌ومعد وم گردانیدن- وهیچ‌انگاشتن
باشد -
بر بخ و شتن » کنابه‌از هیچ‌انگاشتن
- وکارییمدار و بی‌اثر کردن وضایم ساختن کاری
۱ - رك : برزن و پریزن . ۴ - رك : پرویزن . ۴ ٩‏ بریجن » پهلوی .
0 , ابرانی‌باستان [0۲21 * (یختن » برشتن) «اسفا ۱ : ۲ س ۷۱ *.
=== leaf 491 ===
سه اوه -ت
رای تس ی
آن بکار برند و بردمید کیها یز مالند .
یر بش - بکسر اولو انی رسکون‌تاث
و شین قرشت » بمعنی آخربراش است کهپاتیدن
و فروشاندن باشد . #
‌ بخ - یر اولبررزن دریغ » خوشة
نگور با
برین" ۱ بفتح اول‌بروزن‌قرین »بمعنی
بلایین باشد یمنی بلند ترین و بالا ترین » چه
فلك‌الافلاك را باين اعنبار سپهر برین کفته‌اند -
و صبا را یز گویند چه بادبرین باد صبا است -
ر بمعتی رخنه و شکاف هم آمده است. ۳ - ونام
آتشکده‌ای‌یز هست ۴ - و بضم‌اول پارچة كوچك
و حلال‌داری باشد که از خریزه و حندوانه بریده
باشند ۴ - و.بکسر اول هر سوراخ را گویند
عموماً و سوراح تنور:را خصوصاً .
بر یی « منم اولرکسر انی بتحتانی
رسیده و نون همکسور بنین نقطهدار زده » بمعنی
بربدن و برش باشد 9 - و بمعنی راندن شکم
و بربدن آن «م هست ؛ بمعتی اينکه کویا شکم
او را از غات درد مینك .
بر دنه تب بکسر اول بروزن‌نگینه ؛یمعنی
برین است که هی سوراخ باشد عموماً - وسوراخ
شور باشف خصوصاً .
=== leaf 492 ===
راد ب‌آمده
پز اد بر آهفه - زیی را گویند که
بسیار پیر شده باشد و سال بسیاری بر وگذشته
باشد .
باشد که از چستن است - و بمعنی وزنده‌هم‌هت
که از وزیدن باشد۱ ,چه درفارسی با و داو بهم
بدبیل می‌بابنده واین لفظ را بيختر. بر باد اطلاق
کنند . #
افه یر وزن خزانه . بممنی جهنده
باشد - و بمعتی وزنده هم هست ۴ .
بز باد - پر وزن پرداز (۱) » معروف
است و آنرا بعرمی بباسه خوانند ؛ و بسنی
بند پوست جوز است و بسضی دربگر گونند
" شکوفه و کل و بهار جوز است واقه اعلم .
بلق فقو » با بای فارسی و نون و تای
ععلی بدحهید ؟ .
تع ۵ :ود
افزاری باشد که بدان زنگه آینه و تیغ وامثال
و بضم اون وفتح اول وبابای فارسی هم احده‌است -
بز ۵ ییدان ۴ « بکر اول ۰ یمنی یال
کردن زنگه از روی آمینه و ئیغ و امتال آزد
بر دودن ‌ بروزن بربودن ۰ بمعئی
بزدابیدن است که پاك کردن و جلا دادن زنگه
باشد از دوی آبینه و تیغ و غیره .
زد اه بروزن‌صفراه بلفت زسوپازند(۷)
=== leaf 493 ===
آب بندند( ‏ و سکون ثابی گوی باشد که آب
درآن جمع شود - و رنگهآبرا نیز کوبند . *
بز چا لهفلاك - کنابه از برج جدی
است .
بز سم - بنتح اول و انی و سین بی
قطه و میم. و سکون الك . جل وزغ را گویند
و آن چیز سبزی باشد مانند ابریش مکه در روکه
آب بهم میرسد و وزغ در آن‌پنهان میشودوه‌عنی
ثر کیبی آن وزغ پنهان است چه سمه بمعنی
پنهان همآمده است. وآذرا بعربی طحلب کوبند
ضم طای حطی .
بز غش ۷ پم اول و الث و سکون
" الی و شین فرشت ج , ففب یکی از ازلاه اضحستر
و طایفةٌ اٍبشانرا پزغشیه خوانند .
ز گنج - بنم اول و نالثر سکون ثانی
و لون و جیم » چیزست که بدان پومت‌رادبا
و زراعت کننده را کویند ٩‏ ۱
پز رد گهاهیك - نا حکیمی است
استاد و پرورنده پرویزین انوشیروان بوده ۴ . ۷
۹ یز سك ه بضم اول و کس انی وسکون
سین بی‌نقطه, کای . دانهاست که آنرا بعربی‌عدس
خوانند .
بر شاث- بکر اول بر وزن سرشك »
حکیم و طبیب وجراح را گویند ؛ و بابای‌فارسی
هم آمده است ۴ .
```


## [2026-09-05T14:44:00.119Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"buz\\|būz\\|buc\\|bûz\" BQT_v1_pages.txt | head -20; echo \"=== leaf 492 full ===\"; awk 'BEGIN{RS=\"\\f\"} NR==493' BQT_v1_pages.txt | tail -30",
 "description": "Search BQT for buz footnote"
}
```


### [2026-09-05T14:44:01.966Z] TOOL RESULT

```
=== leaf 492 full ===
افه یر وزن خزانه . بممنی جهنده
باشد - و بمعتی وزنده هم هست ۴ .
بز باد - پر وزن پرداز (۱) » معروف
است و آنرا بعرمی بباسه خوانند ؛ و بسنی
بند پوست جوز است و بسضی دربگر گونند
" شکوفه و کل و بهار جوز است واقه اعلم .
بلق فقو » با بای فارسی و نون و تای
ععلی بدحهید ؟ .
تع ۵ :ود
افزاری باشد که بدان زنگه آینه و تیغ وامثال
و بضم اون وفتح اول وبابای فارسی هم احده‌است -
بز ۵ ییدان ۴ « بکر اول ۰ یمنی یال
کردن زنگه از روی آمینه و ئیغ و امتال آزد
بر دودن ‌ بروزن بربودن ۰ بمعئی
بزدابیدن است که پاك کردن و جلا دادن زنگه
باشد از دوی آبینه و تیغ و غیره .
زد اه بروزن‌صفراه بلفت زسوپازند(۷)
تخم زراعت را کوند ۵ مطلفاً بعنی حر چی زکه
سهت خوردن حوانات کاشته هسشود .
یز رگ - بنتم اول و ثالت و سکون
ثانی و کاف 0 دانه‌است که از آن روغن چراغ
گیرتد و بعربی تتان گوبند - و بضم اول وئانی
ممروف است که فیض کوچك باشد ٩‏ - و نام
مقامیست از موسیقی .
زد کااد - باکاف بروزن‌شرمسار»برزنگر
۴ - ولات دارم و کنج وخزانه
۴ رك : زدردن.
بقمه از صفحهٌ ۲۷۱
ول .: فرهنگ رومتابی ۵4-۷6۲ .
( برهان فاطع»۳)
```


## [2026-09-05T14:44:19.871Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### leaf 491 (p.271) FULL ###\"; awk 'BEGIN{RS=\"\\f\"} NR==492' BQT_v1_pages.txt; echo \"### leaf 492 (p.272) HEAD ###\"; awk 'BEGIN{RS=\"\\f\"} NR==493' BQT_v1_pages.txt | head -14",
 "description": "Print BQT p.271 fully"
}
```


### [2026-09-05T14:44:21.731Z] TOOL RESULT

```
### leaf 491 (p.271) FULL ###
سه اوه -ت
رای تس ی
آن بکار برند و بردمید کیها یز مالند .
یر بش - بکسر اولو انی رسکون‌تاث
و شین قرشت » بمعنی آخربراش است کهپاتیدن
و فروشاندن باشد . #
‌ بخ - یر اولبررزن دریغ » خوشة
نگور با
برین" ۱ بفتح اول‌بروزن‌قرین »بمعنی
بلایین باشد یمنی بلند ترین و بالا ترین » چه
فلك‌الافلاك را باين اعنبار سپهر برین کفته‌اند -
و صبا را یز گویند چه بادبرین باد صبا است -
ر بمعتی رخنه و شکاف هم آمده است. ۳ - ونام
آتشکده‌ای‌یز هست ۴ - و بضم‌اول پارچة كوچك
و حلال‌داری باشد که از خریزه و حندوانه بریده
باشند ۴ - و.بکسر اول هر سوراخ را گویند
عموماً و سوراح تنور:را خصوصاً .
بر یی « منم اولرکسر انی بتحتانی
رسیده و نون همکسور بنین نقطهدار زده » بمعنی
بربدن و برش باشد 9 - و بمعنی راندن شکم
و بربدن آن «م هست ؛ بمعتی اينکه کویا شکم
او را از غات درد مینك .
بر دنه تب بکسر اول بروزن‌نگینه ؛یمعنی
برین است که هی سوراخ باشد عموماً - وسوراخ
شور باشف خصوصاً .
ثر لون - با ناكك مجهول و فتح راو بر
وزن دوبدن » علتی است که در بدن آدمی پیدا
مشود و هرچند برمی‌آبد پپن میگردد وخاری
میکند و آنرا درهندوستان داد میگویندوییی
قوبا خوانند ء و باینمعتی بروزن فرعون‌ودلخون
حم آمده است - و بروزن افیون کردا کرددهان
را کوبند .
« فتح اول وسکون ثافی ۰ رسمه ین
و قاعده و فانون وظرز و روش را گوبند - وامر
بریزبدن بمعنی وزیدن هم هست ٩‏ - و مخفف
بزم باشد که مجلس عيش ومهمانی است > وزمین
و یشنة بلند - و تیغ کوه را نیز گفته‌اند - و با
تشدید انی در عربی جامهٌ رسمانی ۷ - واسباب
۱ - مرکباز : بر (ل+ ین(یوندسبت).  .‏ ۴
س
داسفا ۱ : ۲ ص ۱۷۲۹ ».
تسیک
بعربی تیس خوااند با
نای‌قرشت بروزن‌قیس ۸
از عصدر بر بدن. رله:ح 4.
۴ - ازمصدر بر مدن ه پهلوی ۲18
۹ _ ود :
شه درصفحةٌ ۷
### leaf 492 (p.272) HEAD ###
راد ب‌آمده
پز اد بر آهفه - زیی را گویند که
بسیار پیر شده باشد و سال بسیاری بر وگذشته
باشد .
باشد که از چستن است - و بمعنی وزنده‌هم‌هت
که از وزیدن باشد۱ ,چه درفارسی با و داو بهم
بدبیل می‌بابنده واین لفظ را بيختر. بر باد اطلاق
کنند . #
افه یر وزن خزانه . بممنی جهنده
باشد - و بمعتی وزنده هم هست ۴ .
بز باد - پر وزن پرداز (۱) » معروف
است و آنرا بعرمی بباسه خوانند ؛ و بسنی
بند پوست جوز است و بسضی دربگر گونند
" شکوفه و کل و بهار جوز است واقه اعلم .
```


## [2026-09-05T14:44:38.574Z] TOOL CALL #39: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-05T14:44:38.579Z] TOOL RESULT

```


```


## [2026-09-05T14:44:41.197Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD Bd2 p.189-190 (bhudh/bhugo) ===\"; grep -n \"bhudh-m\\|bhū̆g̑o\\|bhugo\\|bhū.g.o-s\\|Ziegenbock\" incoming/WLD/WLD_Bd2_pages.txt | head -20",
 "description": "Grep Walde-Pokorny Bd2"
}
```


### [2026-09-05T14:44:41.245Z] TOOL RESULT

```
=== WLD Bd2 p.189-190 (bhudh/bhugo) ===
12344:                                                   bhol-    — bhugo-                             189
12389:      Ziegeun. buzni ,.Ziege“: av. biiza- m. „Ziegenbock“, np. buz „Ziege, Bock“;
12392:hiicc    „Dainhirsch,             Mannchen gewisser Tierarten“, bucca „Ziegenbock“, abd.
12399:   Weder im Anlaut nocb im Gutt. fiigt sicb ai. bukkali ,,Ziegenbock“, un-
12415: 190                                bhudhero-s??   — bhudh-men-
12444:bhudh-meu- „Bodeu“; bhudhmno- einzelsprachlich teils zu bhudhmo-, teils
16819:„Ziegenbock“; lit. mekenu, -enti „meckem, stammeln“; klr. mekaty „meckern,
```


## [2026-09-05T14:44:44.810Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '12380,12405p' incoming/WLD/WLD_Bd2_pages.txt; echo \"==== bhudh-men ====\"; sed -n '12444,12475p' incoming/WLD/WLD_Bd2_pages.txt",
 "description": "Print Walde-Pokorny bhugo and bhudhmen"
}
```


### [2026-09-05T14:44:44.868Z] TOOL RESULT

```
nicht        —
           vgl. arm. o    — nacb Fick I ^ 88, 267, 489 als ,.glanzend“, blank
                                     \



zu ai. blias-^ s. "^bhd- j.glanzen'' und Hiibscbmann und Liden aaO.

bhfigo- „Bock'‘              (f.   „Ziege“).
      Ziegeun. buzni ,.Ziege“: av. biiza- m. „Ziegenbock“, np. buz „Ziege, Bock“;
      arm. biic „Lamm'‘; germ, "^buhka- (^bhugno-^l oder vielleicbt eber hypo-
koristiscbe         Konsonantendehnung) in aisl. bukkr.^ bokkr^ bokki „Bock“, ags.
hiicc    „Dainhirsch,             Mannchen gewisser Tierarten“, bucca „Ziegenbock“, abd.
mhd.         bor^ -ekes      „Bock“;
                               hocc (nir.   air. cymr. bu'ch.) corn. 6oc/?, bret.
bouc'h „Bock'‘              beweist gegen Stokes IF. 2, 169 Gdf. hhugno-.^
                            (das nir. -c
s. Zup.KZ. 36, 235, der darum kelt. ^bukko- fiir aus dem Germ, entlehnt h^t).

   Weder im Anlaut nocb im Gutt. fiigt sicb ai. bukkali ,,Ziegenbock“, un-
belegt und etymologisch nur mit Yorbebalt zu verwerten: wenn richtig,
ist     es    alien falls      eine      nach      ai.   biikkdra-h „Gebriili    des L6wen“, bukkati
„bellt“       (s.   hti-    fiir   dumpfe Schalleindrucke)              erfolgte hypokoristische Urn-
bildung eines ^hhfija- = av. buza-.                           Aucb np, mdartl. boca ,,iunge Ziege“,
pam. buCy hiic scheinen Ergebnis einer ahnlicben Umbildung zu sein.
   Ygl. Fickl^ 92, 267,495, IIM79, 111^273; UhlenbeckPBrB. 19, 329f.,
==== bhudh-men ====
bhudh-meu- „Bodeu“; bhudhmno- einzelsprachlich teils zu bhudhmo-, teils
       zu bhudhno-,    s.   J. Schmidt Krit.           101, 111;   daneben mit Binnennasal
       bhundh-y woneben auch bliund-.
   Ai.   bhudnd-h „Grund, Boden“; ao. bUno- ds. (aus %hun^hia-,, Bthl.
Wb. 968 f.);      arm. bun ds. (iran. Lw. ? s. Hiibschmann Arm. Gr. I 430 f.,
 Meillet Msl. 12, 430; ob letzterer arm. andimdk"                mit Recht als
 Mischung von *bhundos mit einem zu dheubjp „tieP‘ gehorigen *dhtibnos
 oder Vendryes Msl. 18, 309 als Ass. aus bhundh- deutet, ist ganz fraglich;
 unbefriedigend Pedersen KZ. 39, 353)
    Gr. Tiv^fi^v „Boden, Wurzelende*", nvvda^ „Grund, Boden'* (fur "^(pvvda^
 nach 7ivd/j,i^v)
    Lat. fundus „Grund, Boden“, profundus „tief“; mir. bond^ bonn „solea^‘
 (aber bun „Wurzel8tock das untere Ende“, mcymr. bon ds., mir. bunad
 „Ur8prung‘', cymr. ftonnetZds., bonheddig        aus unverwandtem
 s. Pickn^ 177, Pedersen KG. I 361 f., 363 f., II 21);

    AisL botn m., ags. bodan m. und botm (engl. bottom),^ as. bodom^ ahd.
 bodam „Boden“ {d vor m nicht zu t verschoben? oder in Beziehung zum
 freilich ebenfalls ratselhaften
                                 p von ags. bypme^ bypne ,,Boden, Kiel“ neben
 bytme^ botm^ bodan ds ?      Germ, -t- stammt aus Formen wie gr. jzvvdaS,
 8. Pick         275, auch Falk-Torp u. b0dker, bankas, b^tte I, II iiber an-
klingende, aber unverwandte germ. Worte).
    Abg.       „Bodea“ lit. diignas ds., gall.      „Welt“ durch Anlehnung
an *dhub- „tief‘ aus ^bzdno umgestellt? oder urspriingl. zu dhub gehorig
nach Bemeker 245 f.?
    Curtius 262.    Ob wie ai. bhumi-h, bhuml^ av. bumiSy ap. bumis „Erde*‘
zu *b]ieua, bhu- „fieri“? DaB bhudh- und dh{e)uh\p- „tief‘ als Umstellungs-
formen ursprgl. eins gewesen seien (Vendryes Msl. 18, 305 ff., wo sogar
mundus „Welt“ diesem Kreise zugeteilt wird), ist schon wegen der ab-
weichenden Bed. nicht uberzeugend; dafi bhudh- „Boden“ als „das tiefe,
untere“ benannt sei, ist nicht zu erweisen, auch nicht durch lat. profun-
```


## [2026-09-05T14:44:52.108Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== ARY latin index buz/bun ===\"; grep -n \"BUZ\\|BUN\\|BONYAD\\|BOZ\" incoming/ARY/ARY_latin_index_pages.txt | head -20",
 "description": "Grep Aryanpur index"
}
```


### [2026-09-05T14:44:52.156Z] TOOL RESULT

```
=== ARY latin index buz/bun ===
1033:BUN y DLAI Y alae Ay STS Blaby gb Foe chlo Same abt sal y oe
3623:BOCK (SWEDISH) 5 yo BUZA AAVESTAN) gl) —
3627:BWCH WELSH) 59 BUC, BUZ ARMENIAN) 5,
3746:OLD HIGH GERMAN) pf galt BUN, BUN (PAHLAVI) 5.34
3748:BODEN (GERMAN) gllT BHUDENO, BUNA
3749:BOTM — (OLD ENGLISH) 4S 53S) BUN ARMENIAN) .+,\
3751:BUND DANISH) jlaila FUNDUS (LATIN) 3
3754:BUN, BOND —:(OLD IRISH) 4S 545 2! FONDO L(TALIAN) .g\Stx\
3841:BUZE ALBANIAN) S\ST BUZA (4L}(RUMANIAN) gly, }
3847:SKEAT: (BUSS) 82 BUZIA (POLISH) glo)
3857:BAKAC POLISH) long) BUAS, BUZA GREEK) li,
3890:BUNDRUS, —-(LITHUANIAN) =) BUD-, BAOTHI-, —{AVESTAN) ply!
3891:BUNDO BAODHA, BAODHI, BAOITHI
4026:BUNDU (LITHUANIAN) gig) BIUDAN, BIDJAN (GOTHIC) oS 3
7091:HUN, BUNI ABRETON) 6.3. SOMNO SUTALIAN) gli!
7223:ZDRAVY, ZBOZI (CZECH) So HU., HUBAYA AVESTAN) .gt3!
9375:” CCI Sil sy BUNT J2 5s eal eg
15396:AR SWEDISH) 645 y+ HEYIN, HEBUN §— (KURDISH) «2,5
15529:‘REFERENCES both, SIBUN GOTHIC) S38
15531:‘BARNHART: (SEVEN) 989 SIBUN (OLD SAXON) pS pS
```


## [2026-09-05T14:44:53.481Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SYN goat ===\"; grep -n \"3\\.36 GOAT\\|GOAT\" SYN.txt | head -10; echo \"=== SYN bottom ===\"; grep -n \"12\\.35 BOTTOM\\|BOTTOM\" SYN.txt | head -10",
 "description": "Grep Buck synonyms"
}
```


### [2026-09-05T14:44:53.546Z] TOOL RESULT

```
=== SYN goat ===
4470:‘gray’, etc. Walde-P. 1.602f. TFalk- | ssdéi ‘suck’. 3.36 3.37 3.38 GOAT HE-GOAT KID (Generic or feminine) Grk. al (xlpatpa) Tp&yos épidos NG ylét, fem. yida  rpa&yos, rpayl karolxe Lat. capra hircus, caper haedus It. capra becco, capro capretto Fr. chevre, bique bouc chevreau, biquet Sp. cabra, chiva cabrén cabrito Rum. capré lap caprioard Ibe, gabor boce menn(dn) Nir. gabhar boc mionnan W. gafr bweh myn Br. gaor bouc’h gaorig Goth. gaits Sante pueceis | ON get hafr (bukkr) kid | Dan. ged buk kid Sw. get bock kid OE gat bucca, hafor ticcen, hécen ME pote bucke kide NE goat he-goat kid Du. geit bok geitje OHG  geiz, ziga boc zicki(n), kizzt(n) - MHG geiz, zige bock 2ickelin NHG ziege, geiss bock zicklein Lith. oka ozys ozelis, ozkutis Lett. kaza Gzis kazlens ChSl. koza koztlit koztle SCr. koza jarac Jare, kozlié Boh. koza kozel kizle Pol. koza koziot koéle Russ. koza kozel kozlenok Skt. _aja-; fem. aja- aja-, chaga- “a Av. i tlcts biza-
=== SYN bottom ===
21850:12.34 BOTTOM
```


## [2026-09-05T14:45:01.399Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\np='incoming/ARY/ARY_latin_index_pages.txt'\nt=open(p,encoding='utf-8',errors='replace').read().split('\\n')\nlast=None\nfor i,l in enumerate(t,1):\n    m=re.search(r'\\[pdf page (\\d+)\\]',l)\n    if m: last=m.group(1)\n    if i in (3623,3627,3746,3749,3751,3754):\n        print(i,'pdfpage',last,'|',l[:120])\nEOF",
 "description": "Find ARY pdf pages for buz/bun"
}
```


## [2026-09-05T14:45:02.462Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4470,4490p' SYN.txt | head -40; echo \"=== 12.34 BOTTOM ===\"; sed -n '21850,21880p' SYN.txt",
 "description": "Print Buck goat and bottom sections"
}
```


### [2026-09-05T14:45:03.189Z] TOOL RESULT

```
3623 pdfpage 127 | BOCK (SWEDISH) 5 yo BUZA AAVESTAN) gl) —
3627 pdfpage 127 | BWCH WELSH) 59 BUC, BUZ ARMENIAN) 5,
3746 pdfpage 131 | OLD HIGH GERMAN) pf galt BUN, BUN (PAHLAVI) 5.34
3749 pdfpage 131 | BOTM — (OLD ENGLISH) 4S 53S) BUN ARMENIAN) .+,\
3751 pdfpage 131 | BUND DANISH) jlaila FUNDUS (LATIN) 3
3754 pdfpage 131 | BUN, BOND —:(OLD IRISH) 4S 545 2! FONDO L(TALIAN) .g\Stx\
```


### [2026-09-05T14:45:03.236Z] TOOL RESULT

```
‘gray’, etc. Walde-P. 1.602f. TFalk- | ssdéi ‘suck’. 3.36 3.37 3.38 GOAT HE-GOAT KID (Generic or feminine) Grk. al (xlpatpa) Tp&yos épidos NG ylét, fem. yida  rpa&yos, rpayl karolxe Lat. capra hircus, caper haedus It. capra becco, capro capretto Fr. chevre, bique bouc chevreau, biquet Sp. cabra, chiva cabrén cabrito Rum. capré lap caprioard Ibe, gabor boce menn(dn) Nir. gabhar boc mionnan W. gafr bweh myn Br. gaor bouc’h gaorig Goth. gaits Sante pueceis | ON get hafr (bukkr) kid | Dan. ged buk kid Sw. get bock kid OE gat bucca, hafor ticcen, hécen ME pote bucke kide NE goat he-goat kid Du. geit bok geitje OHG  geiz, ziga boc zicki(n), kizzt(n) - MHG geiz, zige bock 2ickelin NHG ziege, geiss bock zicklein Lith. oka ozys ozelis, ozkutis Lett. kaza Gzis kazlens ChSl. koza koztlit koztle SCr. koza jarac Jare, kozlié Boh. koza kozel kizle Pol. koza koziot koéle Russ. koza kozel kozlenok Skt. _aja-; fem. aja- aja-, chaga- “a Av. i tlcts biza-
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
—— = by Arya Samaj Foundation Chennai and eGangotri
ANIMALS 165
rj femi-
‘Goat’. The generic and ; en are taken together, since the Sie are generally those used in generic
sens let, Rev. ét. sl. 5.8, brings to- ether under a series of alternating forms E hat are here given separately,
s t ; ee ay alt etc. (1), OHG ziga ete. (4), Lith. ozys, Skt. aja- (7), and Chsl. koza (6).
1, Grk. até (mostly 7, rarely also 6) : Arm. aic ‘goat’, Av. izaena- ‘of (goat's) skin’, perh : Skt. ejatz ‘stirs, moves’, etc. Walde-P. 1.8f., 11.
Hence dim. alyidvov ‘kid’, whence NG wld. generic for ‘goat? (ra yidua), with new fem. vida ‘she-goat’.
Grk. xiuapos (6, also #), xinarpa, orig. ‘yearling’ : Skt. hima- ‘winter’, Lat. bimus (*bi-himos) ‘two years old’, etc. Walde-P. 1.547.
2. Lat. capra (> It., Sp. capra, Fr. chévre, Rum. caprd), fem. to caper ‘he- goat’ (3.37).
Fr. bique, prob. fr. a calling cry REW 1099. Wartburg 1.358 ff.
Sp. chiva, masc. chivo, source?
3. Ir. gabor, NIr. gabhar, W. gafr, Br. gaor, gavr, perh. with unexplained init. variation : Lat. caper, etc. So Thurney- sen, Gram. 189, Z. celt. Ph. 13.108 ff. Otherwise Walde-P. 1.533, 547. es Goth. gaits, ON geit, OE gat, etc., a general Gme. word: Lat. haedus kid ; perh. Lith. Zaidziu, Zaisti ‘play’ as =H Jump, gambol’. Walde-P. 1.527.
feist 186.
st sae ga, MHG zige, NHG ziege, MG me 2 ticcen, OHG zickt(n), Crk ie ean; NHG zicklein, perh. : ih ea. a ie (Hesych.), Arm. Walde-p. ee root connection?
5. Lith. ozka, new fem. fr. oZys ‘he- Boat’ : Skt. aja-, ete. (below, 7
6. ChSL. koza, ete. thse:
, €tc., the general Slavic
word, with Lett. kaza fr. Russ., perh. : OE hécen, MLG hoken ‘kid’, root con- nection? Walde-P. 1.336. Berneker 595.
=== 12.34 BOTTOM ===
12.34 BOTTOM
is NG sino. Goth. Lith. dugnas lat, fundus ON _botn, grunnr Lett. dibens i fondo Dan. bund ChSl. diino a fond Sw. botten SCr. dno a fondo OE botm, grund Boh. dno fund Me anu grounde Pol. dno Mr" jottom Russ. dno V. bun Du. bodem Skt.  budhna- Br. cae (bon) He bodam, grunt Av. biina-
Oueled nee Boaetrs boden
oden
CC-O0. In Public Domain. Gurukul Kangri Collection, Haridwar
| | |
856 SELECTED INDO-EUROPEAN SYNONYMS
Most of the words for ‘bottom’ belong to an inherited group common to Grk., Lat., Gmc. and Indo-Iranian, or to an- other group common to Balto-Slavic.
1. IE *bhu(n)d(h)- with various suf- fixes, Walde-P. 2.190. Ernout-M. 401 f. Walde-H. 1.564 f.
Grk. rv§uqv; Lat. fundus (> Romance words); ON boin, OE botm, etc., general Gme.; Skt. budhna-, Av. buna-; Ir. bond ‘sole of the foot’.
2. NG pop. wézos, fr. class. Grk. razos ‘path’ (10.72), through the Byz. meaning ‘floor’ (7.26).
3. Ir. bun, W. bon (both also ‘trunk’ or ‘stump’ of a tree), perh. orig. ‘blow’ (cf. W. bonclust ‘box on the ear’), fr. root *bhen- in Goth. banja ‘blow, wound’ (Walde-P. 2.149), with semantic devel- opment ‘blow’ > ‘club’ > ‘stock, trunk of a tree’ > ‘bottom’. Cf. Fr. bout ‘end’, orig. ‘blow’ (12.35). G.S. Lane, Lan- guage 13.22 f.
12.35
Grk.  axpos adj., axpov, Goth. andeis
axpa, mépas ON endi NG &xpa, &xpn Dan.  ende Lat. ezirémus adj., extré- Sw. anda
mum 0} 0) ende It. capo, eslremo, etc. ME _ ende Fr. bout } NE end Sp. cabo, exiremo, etc. Du. einde Rum. capdt OHG enti Ir (for)cenn MHG ende Nir. _deireadh NHG ende W. pen Br. penn
‘End’ is understood here, of course, in the spatial sense, not in the temporal, though the latter is to a large extent ex- pressed by the same words (14.26), nor in the frequent secondary sense of ‘pur- pose’. In Greek and Latin ‘end? is often expressed by adjectives in agreement with nouns denoting the object referred to.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
W. gwaelod, Br. goueled : W. gwael ‘low, base’, Ir. fael ‘evil’, further nae nections dub. Stokes 259 (: Lat. a but cf. Walde-P. 1.214). :
4. ON grunnr (only ‘bottom’ of the sea), OF grund, ME grounde ‘bottom’ and ‘surface of earth, ground’ (NE ground), OHG grunt (gl. Lat. fundus) MHG grunt ‘bottom, abyss’, etc, (NHG grund), ef. Goth. grundu-waddjus ‘foun- dation wall’, root connection dub, Walde-P. 1.656. Falk-Torp 3524. Feist 222.
5. Lith. dugnas (*dubnas), Lett. (*du- bens >) dibens, ChS]. dino (*diibno), etc., general Slavic = Gall. dubno-, dumno- ‘world’ (in Dubno-rix) : Lith. dubus ‘deep, hollow’, Goth. diups, etc. ‘deep’, W. dwn, Ir. domain ‘deep’, etc. Walde- P. 1.848. Miihl.-Endz. 1.465. Berne- ker 245 f.
END Lith. galas Lett. gals ChSl. kontct
SCr. kona, kraj Boh. _ konec, kraj Pol. koniec
Russ. konec, kraj Skt. _ anta-, pranta- Ay. karana-
1. Grk. &akpos ‘at the farthest point, uttermost’ (also ‘highest’, whence its use for ‘top’, 12.33), e.g. axpn xelp ‘end of the arm’ = ‘hand’ (Hom.), am’ éxpa? obpavay éws &xpwy abrGy ‘from one end of heaven to the other’ (NT). Hence also as sbs. éxpov and dxpa, NG pop. &xpt-
Grk. zépas, Hom. zefpap, fr. *atprap : arépav ‘on the other side’, Skt. para- far,
Digitized by Arya Samaj Foundation Chennai and eGangotri a 4
31.
: a, TEPHOYs Lat. terminus
Grk. nit only rarely for more d
pound eet fr. the root of Lat. trans
```


## [2026-09-05T14:45:14.720Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D8%B2",
 "prompt": "Give the full Persian section: etymology of بز (boz) 'goat' — Middle Persian form, Proto-Iranian, Avestan, PIE reconstruction, and any cited references (Cheung, Hasandust, MacKenzie)."
}
```


## [2026-09-05T14:45:16.125Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D9%86",
 "prompt": "Give the full Persian section for بن (bon): etymology — Middle Persian, Proto-Iranian, Avestan būna-, PIE, meanings, and cited references."
}
```


## [2026-09-05T14:45:17.401Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D9%86%DB%8C%D8%A7%D8%AF",
 "prompt": "Give the Persian etymology of بنیاد (bonyâd): Middle Persian form, components, meaning, cited references."
}
```


## [2026-09-05T14:45:18.386Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/butcher",
 "prompt": "Full etymology of \"butcher\" — Old French bouchier, boc, Frankish/Gaulish/Celtic origin, dates."
}
```


### [2026-09-05T14:45:26.561Z] TOOL RESULT

```
# Persian بز (boz) 'goat' — Etymology

## Etymology Chain

**Middle Persian:** The entry indicates inheritance from Middle Persian with the notation "[Book Pahlavi needed]" (AZ /⁠buz⁠/), (bwc /⁠buz⁠/), showing the phonetic form without providing the actual script.

**Proto-Iranian:** Inherited from *bujáh

**Proto-Indo-Iranian:** Derived from *bʰuȷ́ás

**Proto-Indo-European:** From *bʰuǵ- ("buck, he-goat")

## Cognates & References

The page notes cognacy with English "buck" (male goat) and Thracian *būzas. However, the specific scholarly references cited (Cheung, Hasandust, MacKenzie) are not mentioned in this Wiktionary entry. The etymological information provided traces the word back through standard linguistic reconstruction layers without citing those particular reference works.
```


### [2026-09-05T14:45:28.678Z] TOOL RESULT

```
# Persian Etymology of بنیاد (bonyâd)

**Middle Persian Form:** The word derives from Middle Persian /⁠bun-dāt⁠/, which came from Old Persian *buna datiy*, literally meaning "placed it in the foundation."

**Components:** The term breaks down into related Persian words:
- "بن" (bon) = foundation
- "دادن" (dâdan) = to give

**Original Meaning:** The etymological root references the act of establishing or laying a foundation, connecting the physical sense of placement with the abstract concept of basis or groundwork.

**Modern Financial Sense:** The dictionary notes that "the financial sense is of modern usage and probably a semantic loan from European languages, e.g. French *fondation*." This reflects how the term expanded beyond its structural meaning to encompass institutional foundations and trusts in contemporary usage.
```


### [2026-09-05T14:45:29.490Z] TOOL RESULT

```
# Persian Section for بن (bon)

## Etymology 1: Bottom/Foundation/Root

**Etymology Source:** From Middle Persian (script not provided in source), Proto-Iranian *buHnáh, Proto-Indo-Iranian *bʰudʰnás, ultimately from PIE *bʰudʰmḗn.

**Meanings:** "bottom," "foundation," "root"

**Pronunciation:** Classical Persian /ˈbun/; Iranian Persian [bon]

**Derived Terms:** بنگاه (bongâh, "organization, institution") and بن‌بست (bon-bast, "dead-end")

## Etymology 2: Bush/Tree (Archaic)

**Etymology Source:** From late Middle Persian (earlier form ون /wan/, "tree; stock, stem"), related to Classical Syriac بَنَ (ban, "terebinth"), Proto-Indo-Iranian *wán- ("tree, wood"). Cognates include Pashto ونه and Sanskrit वन (vana, "forest, grove").

**Meanings:** "bush," "tree" (marked as archaic)

**Derived Terms:** گلبن (golbon), خاربن (xârbon), سروبن (sarvbon)

## References

The entry cites Steingass (1892), Vullers (1855), Ciancaglini (2008), and Laufer (1919) as scholarly sources.
```


### [2026-09-05T14:45:30.614Z] TOOL RESULT

```
# Etymology of "Butcher"

The word "butcher" originated around 1300 from Anglo-French *boucher*, derived from Old French *bochier*. The term likely stems from *bouc*, meaning "male goat," which traces back to Frankish *\*bukk* or a related Germanic source, possibly with Celtic influences (*\*bukkos*, "he-goat").

**Key timeline:**
- **c. 1300**: First recorded as "one who slaughters animals for market"
- **1520s**: Figurative sense emerged meaning "brutal murderer"
- **1560s**: Verb form developed, meaning "kill or slaughter for food"
- **1640s**: Extended figuratively to mean "bungle or botch"

Interestingly, Old English had an earlier term: *flæscmangere*, literally "flesh-monger," before the Norman French word became standard.
```


## [2026-09-05T14:45:35.010Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D9%86%D9%87",
 "prompt": "Give the Persian etymology of بنه (bone/boneh): Middle Persian bunag, meaning, and how it relates to بن (bon)."
}
```


## [2026-09-05T14:45:36.440Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/bottom",
 "prompt": "Full etymology of \"bottom\" — Old English botm, PIE root, cognates including Sanskrit budhnah, Latin fundus, Greek pythmen."
}
```


## [2026-09-05T14:45:38.593Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/buck",
 "prompt": "Full etymology of \"buck\" (male deer/he-goat) — Old English bucca/bucc, Proto-Germanic *bukkon, PIE, and any note about Celtic borrowing or Iranian/Persian buz, Avestan buza."
}
```


## [2026-09-05T14:45:40.274Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0ud%CA%B0m%E1%B8%97n",
 "prompt": "Give the reconstruction, meaning, and descendants of PIE *bʰudʰmḗn — including Avestan, Persian, Latin fundus, Old English botm, Greek pythmēn."
}
```


### [2026-09-05T14:45:41.178Z] TOOL RESULT

```
# Persian Etymology of بنه

Based on the Wiktionary entry, the etymology states: "From _[بن](/wiki/%D8%A8%D9%86#Persian "بن")_ (bon) + _[ـه](/wiki/%D9%80%D9%87#Persian "ـه")_ (\-e)."

The word is formed through suffix addition rather than from Middle Persian. The entry shows بنه (bone) derives from the root بن (bon) combined with the Persian suffix ـه (-e), which is a common nominalization marker in the language.

The Wiktionary page does not mention Middle Persian *bunag* specifically. It does reference Old Armenian բնակ (bnak) as a comparative form, suggesting shared Indo-European etymological roots, but the direct Persian formation involves the simpler process of suffixing the base element.
```


### [2026-09-05T14:45:42.990Z] TOOL RESULT

```
# Etymology of "Bottom"

The word "bottom" has ancient roots tracing back through multiple language families. According to etymonline, it comes from "Middle English _botme_, from Old English _botm_" meaning "ground, soil, foundation, lowest or deepest part of anything."

The term likely derives from the Proto-Indo-European root "*bhudhno-" meaning "bottom," with cognates appearing across Indo-European languages: Sanskrit _budhnah_, Latin _fundus_ ("bottom, piece of land, farm"), Greek _pythmen_ ("foundation"), and Old Irish _bond_ ("sole of the foot").

## Semantic Evolution

The noun's meaning expanded over time. While it originally referred to physical lowest points, by the 1570s it acquired the sense of "fundamental character, essence." The colloquial reference to "the sitting part" emerged in 1794.

Several idiomatic phrases became established during different periods: "get to the bottom of" (1773), "bottoms up" (1875), and "from the bottom of one's heart" (1540s).

The verb form emerged in the 1540s, initially meaning "to put a bottom on," before expanding to "reach the bottom of" by 1808.
```


### [2026-09-05T14:45:43.770Z] TOOL RESULT

```
# Etymology of "Buck" (Male Deer)

The word "buck" meaning a male deer traces back to Old English *bucca*, originally referring to a male goat. According to the source, it derives from Proto-Germanic *\*bukkon*, which appears across Germanic languages (Old Saxon *buck*, Dutch *bok*, German *Bock*, Old Norse *bokkr*).

The ultimate origin may be a PIE root *\*bhugo*, evidenced in cognates like Avestan *buza* ("buck, goat") and Armenian *buc* ("lamb"). However, the source notes uncertainty: "some speculate that it is from a lost pre-Germanic language."

The article does not mention Celtic borrowing or Persian *buz*. It only references the Avestan cognate and notes the possibility of an unknown pre-Germanic source, suggesting the word's deeper genealogy remains somewhat mysterious despite documented Germanic descent.
```


### [2026-09-05T14:45:46.500Z] TOOL RESULT

```
# Proto-Indo-European *bʰudʰmḗn

**Reconstruction:** *bʰudʰmḗn (masculine noun)

**Meaning:** "bottom"

**Etymology:** The term possibly derives from metathesis of *dʰewbʰ- ~ *dʰubʰ- ("deep") combined with the agentive suffix *-mḗn.

**Key Descendants:**

- **Germanic:** Proto-Germanic *buttaz, *butmaz (English "bottom")
- **Italic:** Latin *fundus* ("foundation, estate")
- **Greek:** Ancient Greek πυθμήν *pythmḗn* (bottom of a ship)
- **Celtic:** Proto-Celtic *bundos*
- **Indo-Iranian:** Sanskrit and related languages
- **Armenian:** Old Armenian *andund* (with negative prefix)
- **Albanian:** *bythë*

The word exhibits an athematic, hysterokinetic inflection pattern. Notably, the oblique stem may have simplified from *bʰudʰ(m̥)n-* to *bʰudʰn-*, potentially leading to reanalysis as a thematic o-stem *bʰudʰnós* in daughter languages.
```


## [2026-09-05T14:45:53.823Z] TOOL CALL #54: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%D8%A8%D8%B2\" \\\n \"https://en.wiktionary.org/wiki/%D8%A8%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D8%A8%D9%86%DB%8C%D8%A7%D8%AF\" \\\n \"https://en.wiktionary.org/wiki/%D8%A8%D9%86%D9%87\" \\\n \"https://www.etymonline.com/word/butcher\" \\\n \"https://www.etymonline.com/word/bottom\" \\\n \"https://www.etymonline.com/word/buck\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0ud%CA%B0m%E1%B8%97n\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"pdf page 98, roots Bhugo / Bhun-Bhudh: boz/bon/bonyad/boneh, butcher, bottom, buck, PIE bhudhmen\" 2>&1 | tail -2\ndone",
 "description": "Archive web sources"
}
```


### [2026-09-05T14:45:58.688Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/61a2dfa31d089c46.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6c993f667bc5dfb4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/583ade914ef994db.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6bc26d3a64747005.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d31e3006e3e293fa.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/92bfc03e0b45ab3c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6d7869f76c4dfe2c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f186c32f36235f1f.txt
```


## [2026-09-05T14:46:08.645Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== ARY latin index pdf p.127 (buz cluster) ===\"; sed -n '3610,3640p' incoming/ARY/ARY_latin_index_pages.txt; echo; echo \"=== ARY latin index pdf p.131 (bun cluster) ===\"; sed -n '3740,3760p' incoming/ARY/ARY_latin_index_pages.txt",
 "description": "Print Aryanpur index clusters"
}
```


### [2026-09-05T14:46:08.702Z] TOOL RESULT

```
=== ARY latin index pdf p.127 (buz cluster) ===
BORR, BERJA (OLD NORSE) oS 4335
BER OLD FRISIAN) opp S23
[pdf page 127]
BL AW
ONIONS: (BORE) 108 ‘REFERENCES bethany
SKEAT: (BORE) 68, (BHER) 752. «POKORNY; = SSs=S~S~S~«w
AMINDAROV: * . 208 BARNHART: (BORE) 107-108
Se Nee , . iu day MACKENZIE: (CUT) 109
. BUCK: (CUT) 556, (BORE) 592
leatlaal
02S gob} Maj ee 2 Sale 9 JU) gal om
a gph 602 S Gla Fogg) GUL; 22 05s cal om
op hin O45 22 3a nl ow
BOCK (SWEDISH) 5 yo BUZA AAVESTAN) gl) —
BUK NORWEGIAN) 5533 Buc PAHLAVI) 5345,
BOK (DUTCH) g4che BIZIN KURDISH) 53,5
BOCC HOLD IRISH) 5543 p! WEZA AFGHAN] (3-4) g3\
BWCH WELSH) 59 BUC, BUZ ARMENIAN) 5,
BOC AGABLIC) SIE BUCCA LATIN) 3
BOUCH HBRETON) 6p Bouc HPRENCH) sili
BECCO (SPANISH) g\ ile!
REFERENCES Ucathany (OLD SCANDINAVIAN) i655 hes!
POKORNY: 114 BUKKR
BARNHART: (BUCK) 122 BUKKR (OLD NORSE) pS es5
DELAMARRE: 132 BOCK HOLD SAXON) pS gi pS
‘MACKENZIE: (Goat) 116 OLD HIGH GERMAN) pS galt
BUCK: 164-166 BOC, BUKKA
ONIONS: (BUCK) 122-123 BOCK GERMAN) glST
SKEAT: (BUCK) 77 BUC, HOLD ENGLISH) pS 51531
AMINDAROY: (GOAT) 231 BUCCA
MALLORY & ADAMS: BHUGOS BUCK ENGLISH) 153)

=== ARY latin index pdf p.131 (bun cluster) ===
Sn aie CAF
Apu tat og Le wale
: mae SUA
.
emis BOOM eam |
BODEM —-(OLD FRISIAN) iS 52.3 BONO HAVESTAN) pleas!
OLD HIGH GERMAN) pf galt BUN, BUN (PAHLAVI) 5.34
BODAM BUDHNA, (SANSKRIT) oy Svailee
BODEN (GERMAN) gllT BHUDENO, BUNA
BOTM — (OLD ENGLISH) 4S 53S) BUN ARMENIAN) .+,\
BOOTEN ENGLISH) golS31 PYTHMEN, PUTHMEN :(GREEK) gy
BUND DANISH) jlaila FUNDUS (LATIN) 3
BOTTEN (SWEDISH) 58 yo FOND (FRENCH) Wil
BODEM (DUTCH) «sacle FONDO (SPANISH) ,glilys!
BUN, BOND —:(OLD IRISH) 4S 545 2! FONDO L(TALIAN) .g\Stx\
“BON 2OVELSH) 1535 FUND RUMANIAN) ley,
BONN, BOND. (GAELIC) SIE BOTN, (OLD SCANDINAVIAN) 24S 5-hes\
hued 7 BYTNA
aera BOTN OLD NORSE) 695 335
BODAM — (OLD SAXON) 4S ip-Ste
[pdf page 132]
```


## [2026-09-05T14:46:23.787Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"bun-dāt\\|bun-dat\\|bundāt\\|bunak\\|bunag\\|būz\\b\" MON_part1.txt MON_part2.txt 2>/dev/null | head -10; echo \"--- MON persian bez/bon ---\"; grep -n \"بُز\\|بُن ۱\\|بنیاد\" MON_part1.txt | head -10",
 "description": "Grep Mo'in Farhang-e Farsi"
}
```


### [2026-09-05T14:46:23.871Z] TOOL RESULT

```
--- MON persian bez/bon ---
10830:دیوار» شالده» بن» بی. اس اساس: بنیاد و باية 
11658:بزرگک خانواده. بای بنا» بنیاد ساختمان. 
13705:یدرداری. اصالت رای: با بنیادی اند شه» 
13853:اصل: 8 0( بیخ» بن» بنیاد. 
25315:انقباد. دقت. . بیخ و بن: ۰ ريشه و بنیاد سر و بن: 
25322:قرار» برقراری. بنیاد» اساس. (نحو) شکل. 
25509:بنداد: 00 [- بنیاد] (امر.) بنیاد؛ اساس. 
25765:بنلاد: ۱00-0 [قس. بنداد؛ بنیاد] (امن.) بنای 
25779:بنوره: (00-۷21266 [قس. بنلاد؛ بنیاد] 
25835:بنیاد: 0 (امر.) شالدهء بی دیوار»
```


## [2026-09-05T14:46:30.337Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '25505,25515p;25833,25840p' MON_part1.txt; echo \"=== MON بنه ===\"; grep -n \"^بنه:\\|بنه: \" MON_part1.txt | head -5",
 "description": "Print Mo'in bondād/bonyād entries"
}
```


### [2026-09-05T14:46:30.429Z] TOOL RESULT

```
نودن. عزم اقدامی داشتن. 


ننداد 
بنداد: 00 [- بنیاد] (امر.) بنیاد؛ اساس. 
اصل هر چیز. پشتیبان. 

سندار: ۱-۱-۲ [- سنه‌دار] (افا. ص‌مر.) 
رشه‌دار. کسه‌دار؛ خانه‌دار» صاحب تجمل 
و مکنت» مابه‌دار. مالک صاحب ملک 
(بیشتر در خراسان). کسی که خراج جنسی را 
بنیآدم: 1 - مها [ع. در اصل: بنین آدم] 
(امر.) اولاد آدم آدمیان» مردمان. 
بنیاد: 0 (امر.) شالدهء بی دیوار» 
بنلاد» بنیان. بیخ» پایه» اصل» ریشه. بنیاد به 
آب بردن: (- ناد به آب رسانیدن) (کد.) 
شاد استوار کردن. ناد بر یخ نهادن: بی‌ شبات 
کردن. 
پستیادسنج: لودع.ت (افا.) ژرف‌نگر؛ 
=== MON بنه ===
25790:بنه: (60-)۱212 (.) طنات بار یکت. 
25792:بنه: (م‌مسهط (امر.) (گیا.) درختی از تبرة 
25817:بنه: (م-)002-2 (امر.) بیخ درخت» اصل»
```


## [2026-09-05T14:47:03.897Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('AHD_watkins1985.txt',encoding='utf-8',errors='replace').read().split('\\n')\nc=0\nfor i,l in enumerate(t,1):\n    c+=l.count('\\f')\n    if i in (347,348): print(i,'leaf',c)\nEOF\npython3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nprint(d['AHD'].get('page_offset'))\"",
 "description": "Locate AHD leaf for bhudh"
}
```


## [2026-09-05T14:47:04.273Z] TOOL CALL #59: Bash

```json
{
 "command": "sed -n '1,80p' /home/sfmqrb/git/rishe/tools/verify_check.py",
 "description": "Read verify_check script"
}
```


### [2026-09-05T14:47:05.685Z] TOOL RESULT

```
347 leaf 39
348 leaf 39
1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.
```


### [2026-09-05T14:47:05.721Z] TOOL RESULT

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


## [2026-09-05T14:47:07.996Z] TOOL CALL #60: Bash

```json
{
 "command": "sed -n '80,160p' /home/sfmqrb/git/rishe/tools/verify_check.py",
 "description": "Read rest of verify_check"
}
```


### [2026-09-05T14:47:08.038Z] TOOL RESULT

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


## [2026-09-05T14:47:29.922Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nfor f,lns,off in [('HRN.txt',[2248,2359],21),('HUB.txt',[933,1013],10),('BRT.txt',[17362,17385],None),('SYN.txt',[21850],24),('WLD_x',[],None)]:\n    if f=='WLD_x': continue\n    t=open(f,encoding='utf-8',errors='replace').read().split('\\n')\n    c=0\n    for i,l in enumerate(t,1):\n        c+=l.count('\\f')\n        if i in lns:\n            print(f,i,'leaf',c,'printed p.',(c-off) if off else '?')\nEOF",
 "description": "Compute printed pages for Horn/Hübschmann"
}
```


### [2026-09-05T14:47:35.808Z] TOOL RESULT

```
HRN.txt 2248 leaf 70 printed p. 49
HRN.txt 2359 leaf 73 printed p. 52
HUB.txt 933 leaf 39 printed p. 29
HUB.txt 1013 leaf 41 printed p. 31
BRT.txt 17362 leaf 545 printed p. ?
BRT.txt 17385 leaf 545 printed p. ?
SYN.txt 21850 leaf 925 printed p. 901
```


## [2026-09-05T14:48:01.583Z] AGENT

Now I'll write the verification file.


## [2026-09-05T14:54:46.868Z] TOOL CALL #62: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build98.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW_BOZ = \"https://en.wiktionary.org/wiki/%D8%A8%D8%B2\"\nW_BON = \"https://en.wiktionary.org/wiki/%D8%A8%D9%86\"\nW_BONYAD = \"https://en.wiktionary.org/wiki/%D8%A8%D9%86%DB%8C%D8%A7%D8%AF\"\nW_BONEH = \"https://en.wiktionary.org/wiki/%D8%A8%D9%86%D9%87\"\nE_BUTCHER = \"https://www.etymonline.com/word/butcher\"\nE_BOTTOM = \"https://www.etymonline.com/word/bottom\"\nE_BUCK = \"https://www.etymonline.com/word/buck\"\nW_BHUDHMEN = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0ud%CA%B0m%E1%B8%97n\"\n\ndata = {\n \"pdf_page\": 98,\n \"book_page\": 68,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [\n  {\n   \"entry\": 3,\n   \"root\": \"Bhugo\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *bʰūǵo-s 'buck, he-goat' (fem. *bʰūǵā 'she-goat'), with a hypocoristic/expressive by-form *bʰukko-s\",\n   \"note\": \"Pokorny p. 174 heads the entry «bhū̆ǵo-s, Koseform bhukko-s ‚Bock‘ (fem. auf -ā ‚Ziege‘)» and lists exactly the branches Nourai draws: av. būza-, npers. buz, arm. buz/buc, mir. bocc / cymr. bwch, germ. *bukka- (aisl. bukkr, ags. bucca, nengl. buck). Watkins/AHD prints «bhugo-. Male animal of various kinds; stag, ram, he-goat» — Nourai's gloss is AHD's wording verbatim, and the language label 'Indo-European' is correct. Two caveats that do not overturn the root: (a) the etymon is confined to Iranian, Armenian, Celtic and Germanic (Skt. bukka- is unattested, a lexicographers' word), so several handbooks treat it as a regional/Wanderwort rather than a securely PIE root; (b) the Germanic geminate -kk- is not a regular reflex of *-ǵ-, and Pokorny, Walde-Pokorny (Zupitza) and Pedersen all argue about whether Germanic borrowed from Celtic or Celtic from Germanic. Mann (IEC) has no 'he-goat' root at all — his bhugo- entries mean 'bend, flee' and 'beat'.\",\n   \"note_fa\": \"ریشهٔ هندواروپایی آغازین *bʰūǵo- «بز نر، تکه» (مادینهٔ آن *bʰūǵā «بز») که پوکورنی در صفحهٔ ۱۷۴ فرهنگ خود با همین صورت و همین معنا آورده و شکل نوازشی/تأکیدی *bʰukko- را نیز در کنار آن نهاده است؛ واتکینز در پیوست ریشه‌های هندواروپایی فرهنگ American Heritage معنای آن را «جانور نرِ گونه‌های مختلف» داده که همان عبارتی است که نورایی عیناً نقل کرده. برچسب زبانی و معنای ریشه هر دو درست است. تنها نکتهٔ احتیاطی این است که این واژه جز در ایرانی، ارمنی، سلتی و ژرمنی دیده نمی‌شود و همگونی مضاعف -kk- در ژرمنی از دیدگاه آوایی بی‌قاعده است؛ از این رو برخی پژوهشگران آن را واژه‌ای فرهنگی/سرگردان می‌دانند نه ریشه‌ای اصیل. ادعای نورایی دربارهٔ خودِ ریشه درست است.\",\n   \"sources\": [E_BUCK, W_BOZ],\n   \"ref_check\": [\n    {\"ref\": \"POK:174\", \"status\": \"supports\", \"note\": \"POK_01.txt line 2538 (the leaf that carries the printed page number 174): «hhügO'Sf Koseform bhukko-s ,Bock^ (fem. auf -ä ,Ziege^). … av. büza m. ,Ziegenbock^, npers. buz ,Ziege^ ,Bock^; arm. buz ,Lamm^; mir. bocc, pocc … germ. '^bukka- … ags. bucca, nengl. buck». Exactly Nourai's root, gloss and branches.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"IEW p. 174 s.v. bhū̆ǵo-s\", \"stance\": \"supports\", \"note\": \"«bhū̆ǵo-s, Koseform bhukko-s ‚Bock‘ (fem. auf -ā ‚Ziege‘)»; adds «germ. *bukka- (nach Pedersen Litteris 7, 23 f. aus dem Kelt. entlehnt?)».\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. II p. 189 s.v. bhūgo-\", \"stance\": \"supports\", \"note\": \"WLD_Bd2_pages.txt line 12344 running head «bhol- — bhugo- 189»; entry «bhügo- ‚Bock‘ (f. ‚Ziege‘). Ziegeun. buzni ‚Ziege‘: av. būza- m. ‚Ziegenbock‘, np. buz ‚Ziege, Bock‘; arm. buc ‚Lamm‘; germ. *bukka- (*bhugno-? oder vielleicht eher hypokoristische Konsonantendehnung)»; also «Zup. KZ. 36, 235, der darum kelt. *bukko- für aus dem Germ. entlehnt hält».\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 p. 10 (local AHD_watkins1985.txt line 348)\", \"stance\": \"supports\", \"note\": \"«bhugo-. Male animal of various kinds; stag, ram, he-goat. 1. Germanic *bukkaz (possibly borrowed from the Celtic form in 2. below) … BUCK. 2. Celtic *bukkos, he-goat, in Old French boc, buck: BUTCHER. [Pok. bhūgo-s 174.]» — the whole chart in one entry.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann pp. 118-125 (bhud- … bhung-)\", \"stance\": \"silent\", \"note\": \"grep '^bhug' IEC.txt: Mann has only «bhugo, iō (1) ‚bend, turn, flee‘» and «bhugo, iō (2) ‚beat‘» — no 'he-goat' root anywhere; Mann simply does not recognise this etymon.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 3.36-3.37 GOAT / HE-GOAT, pp. 164-166\", \"stance\": \"supports\", \"note\": \"the comparative table gives Av. būza- under HE-GOAT beside OE bucca, OHG boc, ON (bukkr), Nir. boc, W. bwch, Br. bouc'h, Fr. bouc — the same set of forms as the chart.\"},\n    {\"src\": \"ARY\", \"where\": \"Aryanpur, Latin index [pdf page 127] s.v. بز\", \"stance\": \"supports\", \"note\": \"the index cluster lists BUZA (AVESTAN), BUC (PAHLAVI), BUC/BUZ (ARMENIAN), BIZIN (KURDISH), BOCC (OLD IRISH), BWCH (WELSH), BOUC (FRENCH), BUC/BUCCA (OLD ENGLISH), BUCK (ENGLISH), with references «POKORNY: 174 … MALLORY & ADAMS: BHUGOS» — an independent modern Persian source reproducing Nourai's tree.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Avestan\", \"words\": \"buza, bŭza\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Young Avestan būza- m. 'he-goat', attested once, Yašt 14.35, būzahe kǝhrpa raēvatō 'in the shape of a wild he-goat' (Bartholomae, AiW col. 969-970). It continues PIE *bʰūǵo- with the regular Indo-Iranian outcome (*bʰ > b, *ǵ > z by the satem palatalisation, so *bʰūǵo- > Proto-Iranian *būja- > Av. būza-). The derived adjective būzya- 'caprinus, of goats' (Vd. 5.52) shows the stem was fully alive. Nourai's double transcription 'buza, bŭza' is just the ambiguity of Avestan ū in older transliterations; the vowel is long.\",\n     \"derivation_fa\": \"اوستایی būza- (نرینه) «بز نر، تکه»، یک بار در یشت ۱۴ بند ۳۵ به کار رفته است: būzahe kǝhrpa «به پیکر بز نرِ وحشی» (بارتولومه، فرهنگ ایرانی باستان، ستون ۹۶۹). این واژه بازماندهٔ *bʰūǵo- هندواروپایی است؛ در شاخهٔ هندوایرانی *ǵ کامی به z بدل شده (قانون زبان‌های اقمار/ساتم) و *bʰ به b؛ پس *bʰūǵo- ← ایرانی باستان *būja- ← اوستایی būza-. صفت būzya- «بزی، از بز» نیز در وندیداد ۵ بند ۵۲ آمده است. دو صورت «buza, bŭza» در کتاب تنها اختلاف شیوهٔ آوانگاری است و واکه در اصل کشیده است. ادعای نورایی درست است.\",\n     \"sources\": [W_BOZ],\n     \"ref_check\": [\n      {\"ref\": \"POK:174\", \"status\": \"supports\", \"note\": \"«av. büza m. ,Ziegenbock^» printed in the *bhūǵo-s entry on p. 174 (POK_01.txt line 2539).\"},\n      {\"ref\": \"AEF:272\", \"status\": \"not_checked\", \"note\": \"Khaleqi-Motlaq's Asās-e Ešteqāq-e Fārsi is not online; but it is the Persian translation of Horn, and Horn's corresponding entry no. 213 (Grundriss p. 49) reads «213. buz ‚Ziege, Bock‘ … aw. būza- ‚Bock‘» — i.e. the claim Nourai attributes to AEF is verifiable in AEF's original.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch col. 969-970\", \"stance\": \"supports\", \"note\": \"BRT.txt line 17385: «j. būza- m. ‚Ziege, Ziegenbock‘: būzahe kǝhrpa … ‚in der Gestalt eines wilden Ziegenbocks‘ Yt. 14. 35. — Ableit. — np. (NpS.) buz»; and line ~17387 «j. būzya- Adj. ‚von Ziegen herrührend, caprinus‘ … Pū.: māyā i buz».\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. II p. 189\", \"stance\": \"supports\", \"note\": \"«av. būza- m. ‚Ziegenbock‘, np. buz ‚Ziege, Bock‘» heading the Iranian evidence for *bhūgo-.\"},\n      {\"src\": \"HRN\", \"where\": \"Horn no. 213, p. 49\", \"stance\": \"supports\", \"note\": \"«213. buz ‚Ziege, Bock‘ … aw. būza- ‚Bock‘; phlv. būj … skr. vergl. bukka- ‚Bock‘ … arm. buc ‚Lamm‘».\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"buc, bŭž\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Book Pahlavi <bwc>, read buz, 'goat' — MacKenzie's Concise Pahlavi Dictionary p. 20: «buz [AZ < A ʿz; bwc | N ~] goat», i.e. the word is normally written with the Aramaic ideogram AZ (Aram. ʿēz 'goat') and phonetically <bwc>. Av. būza- > MP buz is regular: intervocalic/final Old Iranian z is kept, and the long ū is shortened before the final consonant in the Middle Persian syllable. Nourai's two forms are the two nineteenth-century readings of the same graph: Horn (no. 213) transcribes Pahlavi <bwc> as būj, older Parsi tradition as būž, while MacKenzie 1971 standardised buz; the letter <c> of Nourai's 'buc' is the transliterated Pahlavi character, not a separate word. So neither form is an error.\",\n     \"derivation_fa\": \"فارسی میانه (پهلوی) در نوشتار کتابی <bwc>، خوانده buz «بز»، که مکنزی در فرهنگ کوچک پهلوی (ص ۲۰) چنین آورده است: «buz [هزوارش AZ از آرامی ʿz؛ bwc] بز». یعنی این واژه بیشتر با هزوارش آرامی AZ نوشته می‌شده است. تحول اوستایی būza- به پهلوی buz قاعده‌مند است: z ایرانی باستان بر جای می‌ماند و ū کشیده در هجای بسته کوتاه می‌شود. دو صورت «buc, bŭž» که نورایی آورده در واقع یک واژه‌اند: buc آوانگاری حرف‌به‌حرفِ نویسهٔ پهلوی است و būž/būj خوانشی است که هرن (شمارهٔ ۲۱۳) و سنت پارسیان به کار می‌بردند، در برابر خوانش امروزی buz. پس خطای چاپی یا خطای خوانش در کار نیست و ادعای نورایی درست است.\",\n     \"sources\": [W_BOZ],\n     \"ref_check\": [\n      {\"ref\": \"BQT:271\", \"status\": \"supports\", \"note\": \"BQT_v1_pages.txt leaf 491 = printed p. 271 (fixed by the footnote «بقیه از صفحهٔ ۲۷۱» at the foot of the next leaf): the two-column OCR of that page carries the headword بز with «... بعربی تیس خوانند» ('in Arabic it is called tays, he-goat') and «بروزن قیس»; the page is the Borhān entry for بز that Mo'in footnotes.\"},\n      {\"ref\": \"AEF:272\", \"status\": \"not_checked\", \"note\": \"AEF not online; its German original Horn no. 213 (p. 49) has «phlv. būj», exactly Nourai's second Pahlavi form.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD p. 20 s.v. buz\", \"stance\": \"supports\", \"note\": \"PHD.txt line 292: «buz [AZ < A ʿz; bwc | N ~] goat» — Pahlavi <bwc>, New Persian identical.\"},\n      {\"src\": \"HRN\", \"where\": \"Horn no. 213, p. 49\", \"stance\": \"supports\", \"note\": \"«aw. būza- ‚Bock‘; phlv. būj, vergl. xar-būz … Bund.» — Horn's Pahlavi transcription is būj, Nourai's bŭž.\"},\n      {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien p. 29 (note to Horn 213)\", \"stance\": \"partial\", \"note\": \"«Das in der Anmerkung erwähnte phl. xarbuz (Bdh. 57,8) = ‚Esel-ziege‘, das Nöldeke im Syrischen nachweist, liegt auch im Armenischen vor … Np. buz auch im Afghanischen als LW. buz ‚a he-goat‘» — confirms the Pahlavi word but discusses only the compound.\"},\n      {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II\", \"stance\": \"silent\", \"note\": \"grep '^buz' in NYB_vol2_glossary.txt: the glossary of Nyberg's selected texts has no buz entry (his texts do not contain the word).\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Persian\", \"words\": \"boz «بُز»\", \"verdict\": \"confirmed\",\n     \"derivation\": \"New Persian بُز boz 'goat' continues Middle Persian buz unchanged in consonants; the Classical Persian short u of buz has become the mid vowel o of modern Iranian Persian (buz > boz), the same shift as in خوش xwuš > xoš. The word is old and common in New Persian (Borhān-e Qāteʿ p. 271, glossed with Arabic تیس tays for the male). Dialect and neighbouring-language forms confirm the Iranian pedigree rather than a loan: Kurdish bizin, Balochi buz, Pashto wuz, Wakhi buc/büc, Shughni/Sarikoli waz, Munji woza (Horn no. 213). Armenian buc 'lamb' is an old Iranian loanword, not a source.\",\n     \"derivation_fa\": \"«بُز» در فارسی نو دنبالهٔ مستقیم فارسی میانهٔ buz است؛ تنها دگرگونی، تبدیل واکهٔ کوتاه u در فارسی کلاسیک به o در فارسی امروزِ ایران است (buz ← boz)، همان تحولی که در «خوش» نیز دیده می‌شود. برهان قاطع (ص ۲۷۱) این واژه را با معادل عربی «تیس» برای نرِ آن آورده است. صورت‌های گویشی و زبان‌های ایرانی همسایه ایرانی‌بودن واژه را تأیید می‌کنند و جای گمان وام‌گیری نمی‌گذارند: کردی bizin، بلوچی buz، پشتو wuz، وخی buc، شغنی/سریکلی waz، مُنجی woza (هرن، شمارهٔ ۲۱۳). ارمنی buc «بره» خود وام‌واژه‌ای ایرانی است نه سرچشمه. ادعای نورایی درست است.\",\n     \"sources\": [W_BOZ],\n     \"ref_check\": [\n      {\"ref\": \"none\", \"status\": \"not_checked\", \"note\": \"the node carries no refs= in the book; the chain Pahlavi buz > NP boz is covered by the parent node's BQT:271 and by POK:174 («npers. buz ‚Ziege, Bock‘»).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BQT\", \"where\": \"Borhān-e Qāteʿ ed. Moʿin p. 271 s.v. بز\", \"stance\": \"supports\", \"note\": \"BQT_v1_pages.txt leaf 491: the بز entry, «... بعربی تیس خوانند» — the Persian headword is on the page Nourai cites.\"},\n      {\"src\": \"HRN\", \"where\": \"Horn no. 213, p. 49\", \"stance\": \"supports\", \"note\": \"«213. buz ‚Ziege, Bock‘, būze … kurd. bizin; afγ. wuz; bal. LW. būz (37); waχ. buc, büc, sangl. wuz, minǰ. woza, šiγn. sar. waz».\"},\n      {\"src\": \"ARY\", \"where\": \"Aryanpur, index [pdf page 127]\", \"stance\": \"supports\", \"note\": \"Persian بز listed with AVESTAN BUZA and PAHLAVI BUC and PIE BHUGOS, citing Pokorny 174 and MacKenzie.\"},\n      {\"src\": \"WIKT\", \"where\": \"en.wiktionary.org/wiki/بز, Persian section\", \"stance\": \"supports\", \"note\": \"«Inherited from Middle Persian (AZ /buz/, bwc /buz/), from Proto-Iranian *bujáh, from Proto-Indo-Iranian *bʰuȷ́ás, from Proto-Indo-European *bʰuǵ- ‘buck, he-goat’; cognate with English buck».\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"Germanic\", \"words\": \"bukkaz\", \"verdict\": \"plausible\",\n     \"derivation\": \"Proto-Germanic *bukkaz / *bukkōn- 'he-goat, buck' (ON bukkr, bokkr, OE bucca 'he-goat' and bucc 'male deer', OS buck, OHG boc, G Bock, Du. bok). Semantically and formally it matches PIE *bʰūǵo-, but the match is not phonetically regular: PIE *ǵ should give Gmc. *k (Grimm) but not a geminate, so *-kk- must be explained either by Kluge's law from a suffixed *bʰuǵ-nó- (so Walde-Pokorny's alternative *bhugno-, and Kroonen 2013) or by expressive/hypocoristic gemination (Walde-Pokorny's preferred option, Martinet). Pokorny goes further and asks whether Germanic simply borrowed the word from Celtic (following Pedersen, Litteris 7, 23f.), while Zupitza (KZ 36, 235) argued the borrowing ran the other way; Etymonline records the further suspicion that it comes 'from a lost pre-Germanic language'. Nourai's plain arrow root → Germanic is what AHD draws, but AHD itself hedges it ('possibly borrowed from the Celtic form').\",\n     \"derivation_fa\": \"ژرمنی آغازین *bukkaz / *bukkōn- «بز نر» (نورس کهن bukkr، انگلیسی کهن bucca «بز نر» و bucc «گوزن نر»، آلمانی Bock، هلندی bok). از نظر معنایی با *bʰūǵo- هندواروپایی می‌خواند، اما از نظر آوایی بی‌قاعده است: *ǵ هندواروپایی در ژرمنی باید k بدهد نه kk مضاعف. برای توجیه این همخوان مضاعف دو راه پیشنهاد شده است: یا از صورت پسوندی *bʰuǵ-nó- بر پایهٔ قانون کلوگه (والده‑پوکورنی و کرونن)، یا کشش تأکیدی/نوازشی همخوان (والده‑پوکورنی و مارتینه). افزون بر این، پوکورنی به پیروی از پدرسن این احتمال را پیش می‌کشد که ژرمنی این واژه را از سلتی وام گرفته باشد، حال آنکه تسوپیتسا عکس آن را می‌گفت، و اتیمآنلاین حتی از زبانی پیش‑ژرمنی و ناشناخته سخن می‌گوید. پیکان بی‌قید نورایی همان چیزی است که AHD رسم کرده، ولی خود AHD آن را با «شاید وام‌گرفته از صورت سلتی» مشروط کرده است؛ پس این حلقه «با احتیاط پذیرفتنی است».\",\n     \"sources\": [E_BUCK],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"AHD_watkins1985.txt line 348: «1. Germanic *bukkaz (possibly borrowed from the Celtic form in 2. below) in: a. Old English buc, bucca, stag, he-goat: BUCK». The form and the arrow are AHD's, but AHD explicitly qualifies the descent as possibly a Celtic loan — Nourai drops the qualification.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"IEW p. 174\", \"stance\": \"partial\", \"note\": \"«germ. *bukka- (nach Pedersen Litteris 7, 23 f. aus dem Kelt. entlehnt?) in aisl. bukkr, bokkr, bokki, ags. bucca, nengl. buck, ahd. mhd. boc, -ckes, nhd. Bock» — the parenthesis raises the loan alternative.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. II p. 189\", \"stance\": \"partial\", \"note\": \"«germ. *bukka- (*bhugno-? oder vielleicht eher hypokoristische Konsonantendehnung)» — the geminate is admitted to be problematic.\"},\n      {\"src\": \"KLN\", \"where\": \"Klein, CEDEL s.v. buck 'male deer' (p. ~217)\", \"stance\": \"partial\", \"note\": \"KLN_1966.txt line 5773: «OE. bucca ‚he-goat‘, bucc ‚male deer‘ … cogn. with Avestic būza ‚buck‘, Pers. buz ‚buck, goat‘, Arm. buc ‚lamb‘. OIr. bocc and W. bwch are prob. Teut. loan words» — Klein reverses the direction Nourai's chart implies for Celtic and treats Germanic as inherited.\"},\n      {\"src\": \"SYN\", \"where\": \"Buck 3.37 HE-GOAT, pp. 164-166\", \"stance\": \"supports\", \"note\": \"OE bucca, ON (bukkr), OHG boc, NHG bock listed as the Germanic word for 'he-goat'.\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"English\", \"words\": \"buck\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Old English bucca 'he-goat' and bucc 'male deer' fell together in Middle English bucke, whence modern buck; the geminate simplified and final -a was lost in the regular ME reduction of unstressed endings. The 'male deer' sense won out in standard English by the 14th century, the 'he-goat' sense surviving in compounds (buckskin) and in the South African -bok borrowings (springbok, gemsbok, steenbok) that AHD lists under the same root.\",\n     \"derivation_fa\": \"انگلیسی buck از انگلیسی کهن bucca «بز نر» و bucc «گوزن نر» می‌آید که در انگلیسی میانه در صورت bucke یکی شده‌اند؛ همخوان مضاعف ساده شده و پایانهٔ بی‌تکیهٔ -a طبق قاعدهٔ عمومی انگلیسی میانه افتاده است. از سدهٔ چهاردهم معنای «گوزن نر» غالب شده و معنای «بز نر» تنها در ترکیب‌ها و در وام‌واژه‌های آفریقای جنوبی مانند springbok و gemsbok بازمانده است. ادعای نورایی درست است.\",\n     \"sources\": [E_BUCK],\n     \"ref_check\": [\n      {\"ref\": \"none\", \"status\": \"not_checked\", \"note\": \"no refs= on the node; the OE > NE step is covered by the parent's AHD citation («Old English buc, bucca, stag, he-goat: BUCK»).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein, CEDEL s.v. buck 'male deer'\", \"stance\": \"supports\", \"note\": \"«buck, n., male deer, stag; dandy. — ME. bucke, fr. OE. bucca, ‚he-goat‘, bucc, ‚male deer‘» (KLN_1966.txt line 5773).\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 p. 10 s.v. bhugo-\", \"stance\": \"supports\", \"note\": \"«Old English buc, bucca, stag, he-goat: BUCK¹»; index line «BUCK! bhugo-».\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict. s.v. BUCK\", \"stance\": \"supports\", \"note\": \"listed by Aryanpur's reference block for بز as «SKEAT: (BUCK) 77» — Skeat likewise takes NE buck from OE bucca.\"}\n     ]\n    },\n    {\n     \"id\": 6, \"lang\": \"Celtic\", \"words\": \"bukkos\", \"verdict\": \"plausible\",\n     \"derivation\": \"Proto-Celtic/Gaulish *bukkos 'he-goat' is reconstructed from Old Irish bocc, pocc (Mod.Ir. boc, poc), Welsh bwch, Cornish boch, Breton bouc'h, and is the form AHD puts behind Old French boc/bouc. Its relation to the root is the mirror image of the Germanic problem: the -kk- is again irregular for *-ǵ-, and the handbooks disagree about the direction of borrowing. Pokorny (after Pedersen) suspects Germanic took the word from Celtic; Walde-Pokorny cites Zupitza (KZ 36, 235) for exactly the opposite, «kelt. *bukko- für aus dem Germ. entlehnt», and Klein says flatly that «OIr. bocc and W. bwch are prob. Teut. loan words». So the arrow PIE root → Celtic is one defensible reading among several, not a settled fact.\",\n     \"derivation_fa\": \"سلتی آغازین/گالی *bukkos «بز نر» صورتی است بازسازی‌شده از ایرلندی کهن bocc/pocc، ولزی bwch، کورنی boch و برتونی bouc'h، و همان است که AHD پشتِ فرانسهٔ کهن boc/bouc می‌نشاند. اشکال آوایی همان اشکال شاخهٔ ژرمنی است: همخوان مضاعف -kk- بازتاب قاعده‌مند *ǵ نیست. دربارهٔ جهت وام‌گیری نیز اختلاف هست: پوکورنی به پیروی از پدرسن گمان می‌برد ژرمنی از سلتی گرفته باشد، اما والده‑پوکورنی از تسوپیتسا نقل می‌کند که «سلتی *bukko- خود وام‌گرفته از ژرمنی است»، و کلاین نیز صریح می‌گوید ایرلندی کهن bocc و ولزی bwch احتمالاً وام‌واژه‌های ژرمنی‌اند. بنابراین پیکان «ریشهٔ هندواروپایی ← سلتی» یکی از خوانش‌های ممکن است، نه امری قطعی؛ با احتیاط پذیرفتنی است.\",\n     \"sources\": [E_BUTCHER],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt line 348: «2. Celtic *bukkos, he-goat, in Old French boc, buck: BUTCHER» — Nourai's node and its child come straight from this line.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"IEW p. 174\", \"stance\": \"supports\", \"note\": \"«mir. bocc, pocc, nir. boc, poc, cymr. bwch, corn. boch, bret. bouc'h ‚Bock‘, dazu mir. boccánach ‚Gespenst‘» — the Celtic set is real; Pokorny's doubt concerns only which branch lent to which.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. II p. 189\", \"stance\": \"contradicts\", \"note\": \"«s. Zup. KZ. 36, 235, der darum kelt. *bukko- für aus dem Germ. entlehnt hält» — i.e. Celtic *bukko- borrowed from Germanic, so not an independent descendant of the root.\"},\n      {\"src\": \"KLN\", \"where\": \"Klein, CEDEL s.v. buck\", \"stance\": \"contradicts\", \"note\": \"«OIr. bocc and W. bwch are prob. Teut. loan words».\"},\n      {\"src\": \"SYN\", \"where\": \"Buck 3.37 HE-GOAT\", \"stance\": \"supports\", \"note\": \"Nir. boc, W. bwch, Br. bouc'h, Ir. bocc listed as the Celtic words for 'he-goat'.\"}\n     ]\n    },\n    {\n     \"id\": 7, \"lang\": \"English\", \"words\": \"butcher\", \"verdict\": \"plausible\",\n     \"derivation\": \"English butcher is c. 1300 Anglo-French boucher, Old French bochier / bouchier 'butcher', a -ier agent noun literally 'one who slaughters he-goats', from Old French bouc 'he-goat'. That much is undisputed and is Klein's account («ME. bocher, boucher, fr. OF. bochier … lit. 'one who slaughters bucks', fr. bouc, 'buck'»); Middle English -er for OF -ier is regular. The disputed link is the one Nourai draws, bouc < Celtic *bukkos: AHD asserts it, but Etymonline states the word is «probably from Frankish *bukk or some other Germanic source, or from Celtic *bukkos», and Klein derives OF bouc from Germanic. Since Frankish *bukk and Gaulish *bukkos would both give OF bouc, the Gaulish route cannot be proved from the French form alone. Hence the node is accepted for the English–French part but only plausible as drawn from the Celtic parent.\",\n     \"derivation_fa\": \"واژهٔ انگلیسی butcher نخستین بار در حدود سال ۱۳۰۰ میلادی به صورت انگلونرمن boucher دیده می‌شود، از فرانسهٔ کهن bochier/bouchier «قصاب»، که اسم فاعلِ ساخته‌شده با پسوند ‑ier از bouc «بز نر» است، یعنی در اصل «کسی که بز نر می‌کشد» (کلاین). تبدیل ‑ier فرانسوی به ‑er انگلیسی میانه قاعده‌مند است. آنچه محل اختلاف است همان پیکانی است که نورایی کشیده، یعنی bouc از سلتی *bukkos: فرهنگ AHD همین را می‌گوید، اما اتیمآنلاین می‌نویسد این واژه «احتمالاً از فرانکی *bukk یا سرچشمه‌ای ژرمنی دیگر، یا از سلتی *bukkos» است و کلاین نیز آن را ژرمنی می‌داند. چون هر دو صورتِ فرانکی و گالی در فرانسهٔ کهن bouc می‌دادند، از روی صورت فرانسوی نمی‌توان داوری کرد. پس بخش انگلیسی‑فرانسویِ زنجیره پذیرفته است ولی حلقهٔ سلتی تنها «با احتیاط پذیرفتنی است».\",\n     \"sources\": [E_BUTCHER],\n     \"ref_check\": [\n      {\"ref\": \"none\", \"status\": \"not_checked\", \"note\": \"no refs= on the node; the parent's AHD citation covers it («Celtic *bukkos … in Old French boc, buck: BUTCHER»), and the AHD index confirms «BUTCHER bhugo-».\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein, CEDEL s.v. butcher (p. ~224)\", \"stance\": \"partial\", \"note\": \"KLN_1966.txt line 5955: «butcher, n. — ME. bocher, boucher, fr. OF. bochier, bouchier (F. boucher), ‚butcher‘, lit. ‚one who slaughters bucks‘, fr. bouc, ‚buck‘. See buck, ‚male deer‘» — same chain, but Klein's buck entry makes the Celtic forms Germanic loans, so his bouc is ultimately Germanic, not Celtic.\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 p. 10 and index\", \"stance\": \"supports\", \"note\": \"«Celtic *bukkos, he-goat, in Old French boc, buck: BUTCHER»; index «BUTCHER bhugo-».\"},\n      {\"src\": \"ETYMONLINE\", \"where\": \"etymonline.com/word/butcher\", \"stance\": \"partial\", \"note\": \"«c. 1300, from Anglo-French boucher, from Old French bochier … probably from bouc ‚male goat‘, from Frankish *bukk or some other Germanic source, possibly with Celtic influence (*bukkos ‚he-goat‘)» — Germanic first, Celtic only 'possibly'.\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 4,\n   \"root\": \"Bhun, Bhudh\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *bʰudʰmḗn / *bʰudʰ-no- 'bottom, base', with an inner-IE metathesised by-form *bʰundʰ-\",\n   \"note\": \"Both of Nourai's citations check out, and each covers one half of his double root name. Pokorny p. 174 heads the entry «bhudh-m(e)n ‚Boden‘; einzelsprachlich teils zu *bhudh-mo-, teils zu *bhudh-no-, daneben mit schon idg. Metathese *bhundho- > *bhundh-» — that is the 'Bhudh' member and the source of the nasal in 'Bhun'. Mann (IEC) p. 124 has a separate headword «bhun- (1) ‚base, foundation, floor, boarding‘. (Some forms are ambig. cf. bhudhmn-, bhudno-) Av. buna ‚floor‘ … Ir. bun» — that is the 'Bhun' member, and Mann's fuller entry bhudhmn- (bhudno-) 'base, bottom, stock, stump, root' stands on pp. 118-119. Watkins/AHD prints «bhudh-. Bottom, base. (The precise preforms of the words listed below are obscure.)» — the same gloss Nourai gives. The gloss 'base, bottom' and the label 'Indo-European' are correct; the only nuance is that 'Bhun' is not a separate root but the nasalised/reanalysed stem of *bʰudʰ-no-.\",\n   \"note_fa\": \"ریشهٔ هندواروپایی آغازین *bʰudʰmḗn و ستاک کوتاه‌شدهٔ آن *bʰudʰ-no- «بُن، کف، ته»، با صورت دگرگون‌شده (قلب/درج غُنّه) *bʰundʰ- که خودِ پوکورنی آن را هندواروپایی می‌داند. هر دو ارجاع نورایی درست‌اند و هر یک نیمی از نام دوگانهٔ ریشه را پوشش می‌دهد: پوکورنی در صفحهٔ ۱۷۴ می‌نویسد «bhudh-m(e)n ‚Boden‘ … daneben mit schon idg. Metathese *bhundho-»، و مان (فرهنگ تطبیقی هندواروپایی) در صفحهٔ ۱۲۴ سرواژهٔ جداگانهٔ «bhun- (۱) ‚base, foundation, floor‘، اوستایی buna» را دارد. واتکینز نیز در AHD همان معنای «ته، بُن» را می‌آورد. برچسب زبانی و معنا درست است؛ تنها نکته آن است که «Bhun» ریشه‌ای مستقل نیست، بلکه گونهٔ غُنّه‌دارِ همان *bʰudʰ-no- است.\",\n   \"sources\": [W_BHUDHMEN, E_BOTTOM],\n   \"ref_check\": [\n    {\"ref\": \"POK:174\", \"status\": \"supports\", \"note\": \"POK_01.txt line 2531 (page 174): «bhudh-m(e)n ,Boden^; einzelsprachlich teils zu *bhudh-mo-, teils *bhudh-no-, daneben mit schon idg. Metathese *bhundho- > *bhundh-. Ai. budhnáh ,Grund, Boden^; av. būnō ds. (*bhundhno-) … Lat. fundus … Ahd. bodam … ags. botm m. > engl. bottom».\"},\n    {\"ref\": \"IEC:124\", \"status\": \"supports\", \"note\": \"IEC.txt leaf 82, immediately after the printed page number 124: «bhun- (1) ‚base, foundation, floor, boarding‘. (Some forms are ambig. cf. bhudhmn-, bhudno-, bhouon-) Av. buna ‚floor‘; Alb. bun …; Ir. bun (‚base‘, ambig. cf. bhudno-)» — Mann's headword bhun- with Nourai's gloss 'base'. Mann's longer bhudhmn- (bhudno-) entry ('base, bottom, stock, stump, root, stone'; Skt. budhnáh, Av. buno, Per. bun, Lat. fundus, OE botm) is at pp. 118-119.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"IEW p. 174\", \"stance\": \"supports\", \"note\": \"see ref_check; Pokorny explicitly derives Av. būnō from *bhundhno- and Lat. fundus from *bhundhos.\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. II p. 190 s.v. bhudh-men-\", \"stance\": \"supports\", \"note\": \"WLD_Bd2_pages.txt line 12444: «bhudh-men- ‚Boden‘; bhudhmno- einzelsprachlich teils zu bhudhmo-, teils zu bhudhno- … daneben mit Binnennasal bhundh-, woneben auch bhund-. Ai. bhudnáh ‚Grund, Boden‘; av. būno ds. (aus *bhundhna-, Bthl. Wb. 968 f.); arm. bun ds. (iran. Lw.?) … Gr. πυθμήν … Lat. fundus … ags. bodan m. und botm (engl. bottom)».\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 p. 10 (AHD_watkins1985.txt line 347)\", \"stance\": \"supports\", \"note\": \"«bhudh-. Bottom, base. (The precise preforms of the words listed below are obscure.) 1. Old English botm, bottom: BOTTOM. … 3. Latin fundus, bottom, base: FOND, FOUND¹, FOUNDER, FUND, FUNDAMENT, FUNDUS; LATIFUNDIUM, PROFOUND. [Pok. bhudh- 174.]»\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 12.34 BOTTOM, pp. 855-856\", \"stance\": \"supports\", \"note\": \"«1. IE *bhu(n)d(h)- with various suffixes, Walde-P. 2.190 … Grk. πυθμήν; Lat. fundus (> Romance words); ON botn, OE botm, etc., general Gmc.; Skt. budhna-, Av. būna-; Ir. bond ‚sole of the foot‘»; the table lists 'Pers. bun'.\"},\n    {\"src\": \"ARY\", \"where\": \"Aryanpur, Latin index [pdf page 131] s.v. بن\", \"stance\": \"supports\", \"note\": \"the cluster lists BUNO (AVESTAN), BUN (PAHLAVI), BUDHNA/BHUDENO/BUNA (SANSKRIT/PIE), BUN (ARMENIAN), PYTHMEN (GREEK), FUNDUS (LATIN), FOND (FRENCH), BOTM (OLD ENGLISH), BOTTOM — Nourai's tree reproduced by an independent modern Persian source.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Avestan\", \"words\": \"bŭnô, bŭnâ\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Young Avestan būna- m. 'ground, bottom, depth' (nom. sg. būnō; Nourai's two forms are the nominative būnō and the stem būna-). Bartholomae, AiW col. 968, glosses it «‚Grund, Boden, Tiefe‘ … a) ‚das Unterste, Unterseite‘» and derives it «Aus ar. *bhudhna-, § 34», i.e. from Proto-Indo-Iranian *bʰudʰná- with loss of the dental cluster and compensatory lengthening (*-udʰn- > -ūn-), matching Skt. budhná-. Pokorny and Walde-Pokorny prefer to route it through the nasalised *bʰundʰna-. Bartholomae adds the derivative būnauua- 'coming from below' (Yt. 16.10) and expressly notes «np. bun; vgl. ai. budhná- m. … Pū. bun», i.e. the Pahlavi and New Persian continuations Nourai's chart draws below.\",\n     \"derivation_fa\": \"اوستایی نو būna- (نرینه) «بُن، کف، ژرفا»؛ دو صورتی که نورایی آورده در واقع صورت فاعلی مفرد būnō و ستاک būna- است. بارتولومه در ستون ۹۶۸ فرهنگ ایرانی باستان معنای «Grund, Boden, Tiefe» (بُن، کف، ژرفا) را می‌دهد و آن را «از آریایی *bhudhna-» می‌گیرد، یعنی از هندوایرانی *bʰudʰná- که با افتادن خوشهٔ دندانی و کشیده‌شدن جبرانی واکه به ūn رسیده است، درست همتای سنسکریت budhná-. پوکورنی و والده‑پوکورنی ترجیح می‌دهند آن را از صورت غُنّه‌دار *bʰundʰna- بگیرند. بارتولومه در همان مدخل می‌افزاید «np. bun … Pū. bun»، یعنی همان دنبالهٔ پهلوی و فارسی نو که نورایی در نمودار خود کشیده است. ادعای نورایی درست است.\",\n     \"sources\": [W_BON, W_BHUDHMEN],\n     \"ref_check\": [\n      {\"ref\": \"POK:174\", \"status\": \"supports\", \"note\": \"POK_01.txt line 2532 (p. 174): «Ai. budhnáh ,Grund, Boden^; av. būnō ds. (*bhundhno-), daraus entlehnt arm. bun ds.» — exactly the Avestan form and gloss of the node.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch col. 968\", \"stance\": \"supports\", \"note\": \"BRT.txt line 17315 running head «967 biš-amrūta- — būna- 968»; the entry «j., g. būna- m. ‚Grund, Boden, Tiefe‘ … Aus ar. *bhudhna-; § 34. — np. bun; vgl. ai. budhná- m., Pā. bundha- m. — Pū. bun».\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. II p. 190\", \"stance\": \"supports\", \"note\": \"«av. būno ds. (aus *bhundhna-, Bthl. Wb. 968 f.)» — cites the same Bartholomae column Nourai gives on the Persian node.\"},\n      {\"src\": \"SYN\", \"where\": \"Buck 12.34 BOTTOM\", \"stance\": \"supports\", \"note\": \"the table row for Avestan reads «Av. būna-» under BOTTOM.\"},\n      {\"src\": \"HRN\", \"where\": \"Horn no. 229, pp. 52-53\", \"stance\": \"supports\", \"note\": \"«aw. buna- ‚Grund, Boden‘; phlv. bun»; Horn's footnote records Bartholomae's alternative reading bunna- and his Aryan preform *bhundhna-.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"bun; bun-dât\", \"verdict\": \"plausible\",\n     \"derivation\": \"Middle Persian bun <bwn'> 'base, foundation, bottom' is well attested and is the regular continuation of Old Iranian *buna- (MacKenzie p. 20; Nyberg II p. 52 «bun [bwn] bottom; foundations; root; beginning … Av. (968) būna-», citing the very Bartholomae column Nourai cites). The second word is weaker: MacKenzie and Nyberg record bun-dahišn 'primal creation', buništ(ag) 'foundation', bun-xān 'source', bun-kadag 'original house' and bunag 'baggage; abode, camp', but no bun-dāt. The form is a reconstruction: Horn, no. 229, writes «vergl. bunyād (*bundād)» with an asterisk, and Wiktionary's Persian entry derives بنیاد from MP bun-dāt, itself from an Old Persian phrase *buna dātiy 'he laid (it) in the foundation'. The compound (bun 'base' + dād, past stem of dādan 'to lay, set, give') is morphologically impeccable and Moʿin still records a New Persian doublet بنداد bondād 'foundation, basis', which is the unmetathesised survival of it; but Nourai prints the Pahlavi form without the asterisk it deserves.\",\n     \"derivation_fa\": \"فارسی میانهٔ bun (نوشتار <bwn'>) «بُن، پایه، ته» به‌خوبی گواهی شده و دنبالهٔ قاعده‌مند ایرانی باستان *buna- است؛ مکنزی (ص ۲۰) و نیبرگ (دفتر دوم، ص ۵۲) آن را با ارجاع به همان ستون ۹۶۸ بارتولومه که نورایی نیز یاد کرده، آورده‌اند. اما واژهٔ دوم استوارتر از حدس نیست: در فرهنگ‌های پهلوی bun-dahišn «آفرینش نخستین»، buništ(ag) «بنیاد»، bun-xān «سرچشمه» و bunag «بنه، اردوگاه» ثبت شده است، ولی bun-dāt نه. این صورت بازسازی است: هرن در شمارهٔ ۲۲۹ آن را با ستاره می‌نویسد «vergl. bunyād (*bundād)»، و ویکی‌واژه «بنیاد» را از فارسی میانهٔ bun-dāt و آن را از عبارت پارسی باستان *buna dātiy «در بُن نهاد» می‌گیرد. ساخت واژه (bun + dād، ستاک گذشتهٔ دادن) بی‌عیب است و معین هنوز صورت «بنداد» را در فارسی نو به معنی «بنیاد، اساس» ضبط کرده که همان صورت بی‌قلبِ آن است. با این همه، نورایی صورت پهلوی را بدون ستاره چاپ کرده؛ پس این گره «با احتیاط پذیرفتنی است».\",\n     \"sources\": [W_BONYAD, W_BON],\n     \"ref_check\": [\n      {\"ref\": \"BQT:304\", \"status\": \"not_found\", \"note\": \"BQT vol. 1 has no local page scan for p. 304 (tools/ref_page.py BQT:304 answers 'no scan of BQT covers printed page 271/304'), and BQT_v1_pages.txt around the corresponding leaf (~524) is Persian OCR of poor quality in which no بن headword could be isolated; the citation could not be read. Nourai repeats BQT:304 on the Persian node, where the بن entry with Moʿin's footnote would stand.\"},\n      {\"ref\": \"AEF:288\", \"status\": \"not_checked\", \"note\": \"AEF not online. Its German original, Horn no. 229 (Grundriss pp. 52-53), reads «229. (2)bun ‚Fundament, Grund‘, vergl. bunyād (*bundād), aw. buna- ‚Grund, Boden‘; phlv. bun» — which is precisely what Nourai attributes to AEF, including the Pahlavi/*bundād element.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD p. 20\", \"stance\": \"partial\", \"note\": \"PHD.txt line 292: «bun [bwn' | = M, N ~] base, foundation, bottom», and next to it «bunag [bwnk' | N ~a] baggage; abode, camp», «bun-dahišn(īh) primal creation», «buništ foundation», «bun-kadag original house, home», «bun-xān source» — MacKenzie has the simplex and four compounds but NOT bun-dāt.\"},\n      {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II p. 52\", \"stance\": \"partial\", \"note\": \"NYB_vol2_glossary.txt line 1038: «bun [bwn] bottom 102⁵; foundations 113⁸; root 93⁷⁵; beginning 81¹ … — Av. (968) būna-; MPrthPrs Paz. NP. — V. bundahišn and bunyaštak»; line 1041 «bunyaštak [bwnyštk'] primordial cosmic principle … Paz. bunyašt, bunyast». No bun-dāt; Nyberg's nearest form is bunyaštak. (Nourai cites NYB:50 on the child node; the entry actually stands on p. 52 of the glossary.)\"},\n      {\"src\": \"HRN\", \"where\": \"Horn no. 229, pp. 52-53\", \"stance\": \"supports\", \"note\": \"«vergl. bunyād (*bundād)» — Horn reconstructs exactly Nourai's Pahlavi compound, but marks it with an asterisk.\"},\n      {\"src\": \"WIKT\", \"where\": \"en.wiktionary.org/wiki/بنیاد\", \"stance\": \"supports\", \"note\": \"«From Middle Persian bun-dāt, from Old Persian *buna dātiy, literally ‚placed it in the foundation‘ (بن + دادن)».\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Persian\", \"words\": \"bon 1 «بُن ۱»; boneh «بُنه»; bonyâd «بنیاد»\", \"verdict\": \"plausible\",\n     \"derivation\": \"(a) bon بُن 'base, foundation, root, beginning' is MP bun unchanged but for the Classical u > modern o; it is the standard word, and Moʿin's Borhān and Horn no. 229 give the same Iranian comparanda (Kurd. bin, Ossetic bun/bin, Balochi bunā 'below', Wakhi bōn, Shughni bon). (b) bonyâd بنیاد 'foundation' is MP *bun-dād with the very common Persian metathesis of the cluster -nd- plus glide, bun-dād > bunyād (Horn: «bunyād (*bundād)»); Moʿin still lists the unmetathesised doublet بنداد bondād 'بنیاد؛ اساس', which proves the chain. The modern 'foundation, charitable trust' sense is a 20th-century calque on French fondation. (c) boneh بُنه 'household goods, baggage, camp, home' is the disputed item: Wiktionary analyses it synchronically as bon + -e, and MacKenzie's MP bunag [bwnk'] 'baggage; abode, camp' (explicitly glossed 'N ~a', i.e. NP boneh) puts it in the same family; Horn no. 229 also lists «np. bune … 1) ‚Haus, Heimat‘ (Saʿdī, Bustān 8,117), 2) ‚Gepäck‘, phlv. bunak». But Hübschmann, Persische Studien p. 31, expressly excludes it: after rejecting Arm. pʿunǰ he adds «ebenso wenig np. buna ‚Lager, Gepäck‘, bal. LW. bunag ‚Gepäck‘, arm. bnak ‚Wohnung‘, bnakem ‚wohne‘» — i.e. boneh does not belong with bun. Modern Persian etymology (MacKenzie, Wiktionary/Hasandust) sides with Horn against Hübschmann, but the objection stands on record, so the node as a whole is plausible rather than confirmed. The Ferdowsī verse quoted in the book («چو سیمرغ را بچه شد گرسنه / به پرواز بر شد دمان از بنه») uses بنه in exactly the 'nest, home' sense Nourai glosses.\",\n     \"derivation_fa\": \"الف) «بُن» دنبالهٔ بی‌واسطهٔ فارسی میانهٔ bun است و تنها u کلاسیک به o امروزی بدل شده؛ هرن در شمارهٔ ۲۲۹ همتایان ایرانی آن را می‌آورد: کردی bin، آسی bun/bin، بلوچی bunā «زیر»، وخی bōn، شغنی bon. ب) «بنیاد» از فارسی میانهٔ *bun-dād است با قلبِ خوشهٔ -nd- و افزوده‌شدن غلت y؛ هرن خود می‌نویسد «bunyād (*bundād)». گواه قاطع این تحول آن است که معین هنوز صورت بی‌قلبِ «بنداد» را به معنی «بنیاد؛ اساس» ضبط کرده است. معنای امروزی «مؤسسه و نهاد خیریه» گرته‌برداری سدهٔ چهاردهم خورشیدی از fondation فرانسوی است. ج) «بنه» موردِ اختلاف است: ویکی‌واژه آن را ساختِ «بن + ـه» می‌داند و مکنزی صورت پهلوی bunag «بنه، بار و بنه؛ اردوگاه، خانه» را درست پیش از bun آورده و برابر فارسی نو آن را «بنه» نوشته است؛ هرن نیز «np. bune ۱) خانه و وطن (سعدی، بوستان) ۲) بار و بنه، phlv. bunak» را در همان مدخل ۲۲۹ می‌آورد. اما هوبشمان در «مطالعات فارسی» ص ۳۱ صریحاً آن را از این خانواده بیرون می‌گذارد: «همچنین نه فارسی نو buna ‚بار و بنه، اردو‘ و نه بلوچی bunag و نه ارمنی bnak». ریشه‌شناسی امروزی جانب هرن و مکنزی را می‌گیرد، ولی چون ایراد هوبشمان ثبت است، این گره در مجموع «با احتیاط پذیرفتنی است». بیت فردوسی که در کتاب نقل شده («چو سیمرغ را بچه شد گرسنه / به پرواز بر شد دمان از بنه») دقیقاً «بنه» را به همان معنای «آشیانه، خانه» به کار برده است.\",\n     \"sources\": [W_BON, W_BONYAD, W_BONEH],\n     \"ref_check\": [\n      {\"ref\": \"BQT:304\", \"status\": \"not_found\", \"note\": \"no local scan of Borhān vol. 1 p. 304 (ref_page.py refuses: 'no scan of BQT covers printed page …'), and the OCR text of the corresponding leaf could not be resolved into a بن headword. Not readable; the surrounding entries confirm only that leaf ≈ p. 304 falls in the ب section.\"},\n      {\"ref\": \"BRT:968\", \"status\": \"supports\", \"note\": \"Bartholomae col. 968 (BRT.txt line 17315 running head «967 … būna- 968») is exactly the Avestan būna- entry, and it explicitly ends «— np. bun; vgl. ai. budhná- m. … — Pū. bun», i.e. Bartholomae himself draws the line to New Persian bun that Nourai's arrow draws.\"},\n      {\"ref\": \"NYB:50\", \"status\": \"partial\", \"note\": \"Nyberg's bun entry is on p. 52 of the Glossary, not p. 50 (NYB_vol2_glossary.txt leaf 60; p. 50 carries bitaxš–bōr). The content supports the claim: «bun [bwn] bottom; foundations; root; beginning … — Av. (968) būna-; MPrthPrs Paz. NP», with a cross-reference to bunyaštak. Two-page citation slip.\"},\n      {\"ref\": \"AEF:288,290\", \"status\": \"not_checked\", \"note\": \"AEF not online; Horn no. 229 (pp. 52-53), of which AEF is the Persian translation, carries both the bunyād (*bundād) derivation and the np. bune 'Haus, Heimat / Gepäck' material that these two page references must cover.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"HRN\", \"where\": \"Horn no. 229, pp. 52-53\", \"stance\": \"supports\", \"note\": \"«229. (2)bun ‚Fundament, Grund‘, vergl. bunyād (*bundād), aw. buna- ‚Grund, Boden‘; phlv. bun … kurd. bin; oss. d. bun, t. bin ‚Boden‘ … np. bune bedeutet dann auch 1) ‚Haus, Heimat‘ (Saʿdī, Bostān 8,117) … 2) ‚Gepäck‘, phlv. bunak ‚Gepäck, Lager‘» — all three of Nourai's Persian words.\"},\n      {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien p. 31 (note to Horn 229)\", \"stance\": \"contradicts\", \"note\": \"«Arm. pʿunǰ ‚Halm‘ gehört trotz Bugge nicht hierher, ebenso wenig np. buna ‚Lager, Gepäck‘, bal. LW. bunag ‚Gepäck‘ (Geiger, Lautlehre p. 24), arm. bnak ‚Wohnung‘, bnakem ‚wohne‘» — Hübschmann detaches بنه from بن.\"},\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD p. 20\", \"stance\": \"supports\", \"note\": \"«bunag [bwnk' | N ~a] baggage; abode, camp» set immediately beside «bun … base, foundation, bottom» — MacKenzie's 'N ~a' equates it with NP boneh.\"},\n      {\"src\": \"MON\", \"where\": \"Moʿin, Farhang-e Fārsi s.vv. بنداد / بنیاد / بنه\", \"stance\": \"supports\", \"note\": \"MON_part1.txt line 25509 «بنداد: [- بنیاد] (امر.) بنیاد؛ اساس. اصل هر چیز»; line 25835 «بنیاد: (امر.) شالوده، بن دیوار، بنلاد، بنیان، بیخ، پایه، اصل، ریشه»; line 25817 «بنه: (امر.) بیخ درخت، اصل» and line 25790 «بنه: … بار» — the بنداد doublet is the decisive evidence for bun-dād > bunyād.\"},\n      {\"src\": \"WIKT\", \"where\": \"en.wiktionary.org/wiki/بن (Persian, Etymology 1)\", \"stance\": \"supports\", \"note\": \"«From Middle Persian, from Proto-Iranian *buHnáh, from Proto-Indo-Iranian *bʰudʰnás, from PIE *bʰudʰmḗn; bottom, foundation, root», with derived بنگاه, بن‌بست.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"Old English\", \"words\": \"botm\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Old English botm 'ground, soil, foundation, lowest or deepest part' beside bodan and (Mercian) *bodm; the Germanic group (ON botn, OS bodom, OHG bodam, Du. bodem) goes back to a Proto-Germanic *butmaz/*buþmaz which continues PIE *bʰudʰ-m(e)n-. The Germanic dental is famously irregular — Pokorny already notes «mit unklarem Dentalwechsel; es scheint ein urgerm. *buþma- zugrunde zu liegen, das wohl analogisch zu erklären ist» — and Watkins covers himself with «the precise preforms of the words listed below are obscure»; the -tt-/-t- of English is usually explained from the Kluge-law geminate. The membership of the word in the root, which is all Nourai's arrow asserts, is not in doubt.\",\n     \"derivation_fa\": \"انگلیسی کهن botm «کف، زمین، پایه، ژرف‌ترین بخش» در کنار bodan و صورت مرسی *bodm؛ گروه ژرمنی (نورس کهن botn، ساکسون کهن bodom، آلمانی علیای کهن bodam، هلندی bodem) به ژرمنی آغازین *butmaz/*buþmaz بازمی‌گردد که دنبالهٔ *bʰudʰ-m(e)n- هندواروپایی است. همخوان دندانی در ژرمنی بی‌قاعده است و خودِ پوکورنی می‌نویسد «با تناوب دندانیِ نامعلوم؛ گویا صورت پایهٔ ژرمنی آغازین *buþma- بوده که باید قیاسی توضیح داده شود»، و واتکینز نیز هشدار می‌دهد که «صورت‌های پیشینِ دقیقِ واژه‌های زیر مبهم‌اند». اما عضویت این واژه در همین ریشه ــ که تنها ادعای پیکان نورایی است ــ محل تردید نیست. ادعای نورایی درست است.\",\n     \"sources\": [E_BOTTOM],\n     \"ref_check\": [\n      {\"ref\": \"KLN:189\", \"status\": \"supports\", \"note\": \"Klein, CEDEL s.v. bottom (KLN_1966.txt line 5416): «bottom, n. — ME. botme, botome, fr. OE. botm, ‚lowest part, depth, bottom‘, rel. to OS. bodom, ON. botn … and cogn. with OI. budhnah, Gk. [πυθμήν] ‚foundation, bottom‘, L. fundus (metathesis for *fudnos) … Cp. found, ‚to establish‘, founder, fund, fundament, profound.» Nourai's gloss 'lowest part' is Klein's own wording, and Klein's cross-references are exactly Nourai's nodes #5-#7. (In the local 1966 scan the entry sits on the leaf whose running heads are 'boron | bottomry', which the file's leaf-to-page formula puts at pp. 198-199 rather than 189 — a small page-number slip or a different printing; the content is unambiguous.)\"},\n      {\"ref\": \"AHD:1510\", \"status\": \"supports\", \"note\": \"the 1976 AHD appendix runs pp. 1505-1550 and bhudh- is an early b-root, so p. 1510 is the right place; in the 1985 standalone Watkins the same entry is on p. 10: «bhudh-. Bottom, base … 1. Old English botm, bottom: BOTTOM.»\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"CEDEL s.v. bottom\", \"stance\": \"supports\", \"note\": \"see ref_check — full cognate set including L. fundus «metathesis for *fudnos».\"},\n      {\"src\": \"POK\", \"where\": \"IEW p. 174\", \"stance\": \"supports\", \"note\": \"«Ahd. bodam, nhd. Boden, as. bodom, ags. *bodm > mengl. bothem, neben ags. botm m. > engl. bottom … mit unklarem Dentalwechsel; es scheint ein urgerm. *buþma- zugrunde zu liegen».\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. II p. 190\", \"stance\": \"supports\", \"note\": \"«Aisl. botn m., ags. bodan m. und botm (engl. bottom), as. bodom, ahd. bodam ‚Boden‘ (d vor m nicht zu t verschoben?)».\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 p. 10\", \"stance\": \"supports\", \"note\": \"«1. Old English botm, bottom: BOTTOM»; index «BOTTOM bhudh-».\"},\n      {\"src\": \"SYN\", \"where\": \"Buck 12.34 BOTTOM\", \"stance\": \"supports\", \"note\": \"«ON botn, OE botm, etc., general Gmc.» listed under IE *bhu(n)d(h)-.\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"English\", \"words\": \"bottom\", \"verdict\": \"confirmed\",\n     \"derivation\": \"OE botm > ME botme, botome > NE bottom, with the regular Middle English insertion of a svarabhakti vowel between the consonant and the syllabic nasal and later loss of the final -e. The abstract sense 'fundamental character, essence' appears by the 1570s and the colloquial 'the sitting part' in 1794 (Etymonline); the nautical sense 'hull of a ship' gave the derivative bottomry, which AHD likewise files under this root.\",\n     \"derivation_fa\": \"انگلیسی کهن botm ← انگلیسی میانه botme/botome ← انگلیسی نو bottom؛ در انگلیسی میانه میان همخوان و خیشومیِ هجایی واکه‌ای میانجی افزوده شده و سپس ‑e پایانی افتاده است. معنای انتزاعی «ذات و اساس» از حدود ۱۵۷۰ میلادی و معنای عامیانهٔ «نشیمنگاه» از ۱۷۹۴ گواهی شده است (اتیمآنلاین)؛ معنای دریایی «بدنهٔ کشتی» نیز واژهٔ bottomry را پدید آورده که AHD آن را ذیل همین ریشه می‌آورد. ادعای نورایی درست است.\",\n     \"sources\": [E_BOTTOM],\n     \"ref_check\": [\n      {\"ref\": \"none\", \"status\": \"not_checked\", \"note\": \"no refs= on the node; covered by the parent's KLN:189 and AHD:1510 («Old English botm, bottom: BOTTOM»).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"CEDEL s.v. bottom\", \"stance\": \"supports\", \"note\": \"«ME. botme, botome, fr. OE. botm».\"},\n      {\"src\": \"ETYMONLINE\", \"where\": \"etymonline.com/word/bottom\", \"stance\": \"supports\", \"note\": \"«Middle English botme, from Old English botm ‚ground, soil, foundation, lowest or deepest part of anything‘ … from PIE root *bhudhno- ‚bottom‘ (source also of Sanskrit budhnah, Latin fundus, Greek pythmen, Old Irish bond)».\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 index\", \"stance\": \"supports\", \"note\": \"«BOTTOM bhudh- BOTTOMRY bhudh-».\"}\n     ]\n    },\n    {\n     \"id\": 6, \"lang\": \"Latin\", \"words\": \"fundus\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Latin fundus, -ī m. 'bottom of a vessel; ground, piece of land, farm' from *bʰudʰ-no- via the metathesised *bʰundʰos that Pokorny posits for the root («Lat. fundus, -ī m. ‚Boden eines Gefäßes, Grund‘ (*bhundhos), profundus ‚tief‘ = mir. bond, bonn ‚Sohle, Grundlage‘»); Klein describes the same thing as «metathesis for *fudnos», since Latin *-dn- is not tolerated. Initial PIE *bʰ- > Latin f- is the regular word-initial reflex. From fundus come fundāre 'to lay a foundation', fundāmentum, fundātiō and profundus 'deep'.\",\n     \"derivation_fa\": \"لاتینی fundus «ته ظرف؛ زمین، ملک، مزرعه» از *bʰudʰ-no- و از راه صورتِ قلب‌شدهٔ *bʰundʰos که پوکورنی برای این ریشه بازمی‌سازد: «Lat. fundus ‚Boden eines Gefäßes, Grund‘ (*bhundhos), profundus ‚tief‘». کلاین همین را «قلب از *fudnos» می‌نامد، زیرا خوشهٔ ‑dn‑ در لاتینی پذیرفتنی نیست. تبدیل *bʰ هندواروپایی در آغاز واژه به f لاتینی قاعده‌مند است. از fundus فعل fundāre «بنیاد نهادن» و واژه‌های fundāmentum، fundātiō و profundus «ژرف» ساخته شده‌اند. ادعای نورایی درست است.\",\n     \"sources\": [E_BOTTOM, W_BHUDHMEN],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt line 347: «3. Latin fundus, bottom, base: FOND, FOUND¹, FOUNDER, FUND, FUNDAMENT, FUNDUS; LATIFUNDIUM, PROFOUND».\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"IEW p. 174\", \"stance\": \"supports\", \"note\": \"«Lat. fundus, -ī m. ‚Boden eines Gefäßes, Grund‘ (*bhundhos), profundus ‚tief‘ = mir. bond, bonn ‚Sohle, Grundlage, Stütze‘».\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. II p. 190\", \"stance\": \"supports\", \"note\": \"«Lat. fundus ‚Grund, Boden‘, profundus ‚tief‘; mir. bond, bonn ‚solea‘».\"},\n      {\"src\": \"KLN\", \"where\": \"CEDEL s.v. bottom\", \"stance\": \"supports\", \"note\": \"«L. fundus (metathesis for *fudnos), ‚bottom; piece of land, farm‘».\"},\n      {\"src\": \"SYN\", \"where\": \"Buck 12.34 BOTTOM, p. 856\", \"stance\": \"supports\", \"note\": \"«Lat. fundus (> Romance words)» under IE *bhu(n)d(h)-, with Ernout-Meillet 401 f. and Walde-Hofmann 1.564 f.\"}\n     ]\n    },\n    {\n     \"id\": 7, \"lang\": \"English\", \"words\": \"foundation, fundamental, profound\", \"verdict\": \"confirmed\",\n     \"derivation\": \"All three are Latin-via-French borrowings on fundus. foundation: L. fundātiō, -ōnis (< fundāre 'to lay the bottom of, found') > Old French fondation > Middle English foundacioun (14th c.). fundamental: L. fundāmentum 'foundation' (fundāre + -mentum) > fundāmentālis, in English from the 15th c. profound: L. profundus 'deep' (prō- 'forward, before' + fundus) > Old French profond > ME profound. AHD lists FOUND¹, FUNDAMENT and PROFOUND under bhudh- (with FOND, FOUNDER, FUND, FUNDUS, LATIFUNDIUM); foundation and fundamental are the ordinary derivatives of the first two, so the node is right as drawn.\",\n     \"derivation_fa\": \"هر سه واژه وام‌گیری‌های لاتینی‑فرانسوی از fundus هستند. foundation از لاتینی fundātiō (از fundāre «بنیاد نهادن») از راه فرانسهٔ کهن fondation در سدهٔ چهاردهم میلادی به انگلیسی میانه رسیده است. fundamental از لاتینی fundāmentum «بنیاد» (fundāre + پسوند ‑mentum) و صفت fundāmentālis، از سدهٔ پانزدهم. profound از لاتینی profundus «ژرف» (پیشوند prō- + fundus) از راه فرانسهٔ کهن profond. فرهنگ AHD واژه‌های FOUND، FUNDAMENT و PROFOUND را ذیل همین ریشه آورده و foundation و fundamental مشتق‌های عادی دو واژهٔ نخست‌اند؛ پس گره چنان‌که کشیده شده درست است. ادعای نورایی درست است.\",\n     \"sources\": [E_BOTTOM],\n     \"ref_check\": [\n      {\"ref\": \"none\", \"status\": \"not_checked\", \"note\": \"no refs= on the node; covered by the parent's AHD citation, whose word list under bhudh- includes FOUND¹, FUNDAMENT and PROFOUND, and by the AHD index lines «FOUND! bhudh-», «FUNDAMENT bhudh-», «PROFOUND bhudh-».\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 p. 10 and index\", \"stance\": \"supports\", \"note\": \"AHD_watkins1985.txt lines 1526/1534/2136: «FOND? bhudh-», «FOUND! bhudh- … FOUNDER bhudh-», «FUND bhudh- FUNDAMENT bhudh- FUNDUS bhudh-», «PROFOUND bhudh-».\"},\n      {\"src\": \"KLN\", \"where\": \"CEDEL s.v. bottom\", \"stance\": \"supports\", \"note\": \"Klein's own cross-reference list at the end of the bottom entry: «Cp. found, ‚to establish‘, founder, v., fund, fundament, profound».\"},\n      {\"src\": \"SYN\", \"where\": \"Buck 12.34 BOTTOM, p. 856\", \"stance\": \"supports\", \"note\": \"«Lat. fundus (> Romance words)» — the Romance/English descendants are recognised as a group.\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith open('/home/sfmqrb/git/rishe/data/verification/page-98.json','w',encoding='utf-8') as f:\n    json.dump(data,f,ensure_ascii=False,indent=1)\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build98.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-98.json > /dev/null && echo \"JSON valid\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 98",
 "description": "Write and validate page-98 verification"
}
```


### [2026-09-05T14:54:50.960Z] TOOL RESULT

```
ok
JSON valid
nodes verified: 14/14
node verdicts: {'confirmed': 9, 'plausible': 5}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 8, 'not_checked': 9, 'partial': 2, 'not_found': 2}
books consulted: {'supports': 41, 'partial': 8, 'silent': 1, 'contradicts': 3} | by book: {'KLN': 8, 'WLD': 6, 'HRN': 6, 'SYN': 6, 'AHD': 5, 'POK': 4, 'PHD': 3, 'WIKT': 3, 'BRT': 2, 'HUB': 2, 'NYB': 2, 'ETYMONLINE': 2, 'BQT': 1, 'ARY': 1, 'SKT': 1, 'MON': 1}
```


## [2026-09-05T14:55:11.928Z] AGENT

Done — 0 PROBLEM lines.

**Page 98 (book p. 68)** — 3 redirect entries skipped (Bhru 2, Bhu, Bhudh); 2 real entries, 14 nodes.

- **Roots:** 2 confirmed (Bhugo, Bhun/Bhudh)
- **Nodes:** 9 confirmed, 5 plausible, 0 disputed, 0 transcription_suspect, 0 unverified
- **Ref checks:** 8 supports, 2 partial, 2 not_found, 9 not_checked (mostly AEF, which is not online — checked against its German original Horn instead)

Key findings:
- Both root citations check out exactly: Pokorny p. 174 carries *both* `bhū̆ǵo-s ,Bock'` and `bhudh-m(e)n ,Boden'`; Mann (IEC) p. 124 has the separate headword `bhun- (1) 'base, foundation'`, which is where Nourai's second root name comes from. AHD's `bhugo-` gloss "Male animal of various kinds" is quoted verbatim by Nourai.
- Aryanpur (independent modern Persian cross-check) reproduces both trees node-for-node.
- The 5 `plausible` nodes: (Bhugo) Germanic *bukkaz, Celtic *bukkos and English *butcher* — the geminate ‑kk‑ is irregular and Pokorny/Pedersen, Zupitza/Walde-Pokorny, Klein and Etymonline disagree on which of Germanic/Celtic borrowed from the other, or whether it is pre-Germanic substrate; AHD itself hedges ("possibly borrowed from the Celtic form"). (Bhun) Pahlavi node — `bun` is solid (MacKenzie, Nyberg) but `bun-dāt` is unattested: Horn writes it with an asterisk `*bundād`; Moʿin's New Persian doublet بنداد is the best evidence for it. Persian node — Hübschmann (Persische Studien p. 31) expressly detaches بنه from بن; MacKenzie's MP `bunag` and Wiktionary side with Horn against him.
- Nourai's "buc, bŭž" for Pahlavi is **not** a corruption: it is the transliteration `<bwc>` plus Horn's reading `būj/būž` of the same graph (MacKenzie standardised it to `buz`). No transcription flags; no extraction errors — the JSON matches the chart faithfully.

Two small citation slips by Nourai (content still supports him): **NYB:50** — the `bun` entry is on p. 52 of Nyberg's Glossary (p. 50 is bitaxš–bōr); **KLN:189** — Klein's `bottom` entry sits on the leaf with running heads "boron | bottomry" (≈ pp. 198-199 by the local scan's leaf formula).

Not readable: **BQT:304** (Borhān vol. 1 p. 304) — no local page scan and the OCR of that leaf is unusable; marked `not_found` on both nodes that cite it. BQT:271 *was* confirmed (the بز entry, pinned by the "بقیه از صفحهٔ ۲۷۱" catchline).

8 web pages archived via `fetch_source.py` (Wiktionary بز/بن/بنیاد/بنه + PIE *bʰudʰmḗn, Etymonline buck/butcher/bottom).
