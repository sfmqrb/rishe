# Verification process log — verify-page-133


## [2026-09-05T20:07:10.232Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 133 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-133.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-133.json. Write /home/sfmqrb/git/rishe/data/verification/page-133.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 133` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T20:07:11.781Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T20:07:12.486Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T20:07:12.504Z] TOOL RESULT

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


## [2026-09-05T20:07:12.859Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-133.txt"
}
```


### [2026-09-05T20:07:12.879Z] TOOL RESULT

```
1	=== PDF page 133 (book page 103) ===
2	--- entry 0 ---
3	ROOT Dhigha -> redirect to Dheigh
4	--- entry 1 ---
5	ROOT [Indo-European] Dhîs : village, earth ?  (refs IEC:191)
6	#1 (parent #0) [Avestan / Old Persian] refs=SYN:1302; KNT:190; BRT:706 | dahyu, dainhu : land, country
7	  #2 (parent #1) [Pahlavi] refs=BQT:902; SNS:242 | deh, dih : village
8	    #3 (parent #2) [Persian] refs=SYN:1302; BQT:902; MON:1585; TZF:13 | deh 2 «دِه ۲ ( دیه )» : village, country ; dehât «دهات ( دهاتی )» : villages ; dehgân «دهگان ( دهقان )» : villager, farmer ; dehxodâ «دهخدا ( دخو )» : owner or ruler of a village | extra: دهبان ، دهدار ، دهکیا ، دهستان ، دهکده
9	  #4 (parent #1) [Avestan] refs=KNT:208 | visa-dahyu, vîspa-dahyu : for all provinces ☞Wi
10	--- entry 2 ---
11	ROOT Dh-mo -> redirect to Dhě 2
12	
```


## [2026-09-05T20:07:15.899Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/extracted/batch/page-133.json",
 "description": "Read page 133 source JSON"
}
```


### [2026-09-05T20:07:15.947Z] TOOL RESULT

```
{
  "pdf_page": 133,
  "book_page": 103,
  "entries": [
    {
      "root": {
        "name": "Dhigha",
        "redirect": "Dheigh"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Dhîs",
        "lang": "Indo-European",
        "refs": "IEC:191",
        "gloss": "village, earth ?"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "SYN:1302; KNT:190; BRT:706",
          "words": [
            {"translit": "dahyu, dainhu", "gloss": "land, country", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "BQT:902; SNS:242",
          "words": [
            {"translit": "deh, dih", "gloss": "village", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "SYN:1302; BQT:902; MON:1585; TZF:13",
          "words": [
            {"translit": "deh 2", "gloss": "village, country", "script": "دِه ۲ ( دیه )"},
            {"translit": "dehât", "gloss": "villages", "script": "دهات ( دهاتی )"},
            {"translit": "dehgân", "gloss": "villager, farmer", "script": "دهگان ( دهقان )"},
            {"translit": "dehxodâ", "gloss": "owner or ruler of a village", "script": "دهخدا ( دخو )"}
          ],
          "script_extra": "دهبان ، دهدار ، دهکیا ، دهستان ، دهکده",
          "note": null,
          "quote": {
            "text": "خواجه پندارد که ده ۲ روزی دهد - این نمی داند که روزی ده ۳ دهد",
            "poet": "Molavî"
          }
        },
        {
          "id": 4,
          "parent": 1,
          "lang": "Avestan",
          "refs": "KNT:208",
          "words": [
            {"translit": "visa-dahyu, vîspa-dahyu", "gloss": "for all provinces", "script": null, "see": ["Wi"]}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Dh-mo",
        "redirect": "Dhě 2"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-05T20:07:18.031Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['IEC','SYN','KNT','BRT','BQT','SNS','MON','TZF','POK','WLD','AHD','PHD','NYB','HRN','HUB','CHEUNG','ARY']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:600])\n\"",
 "description": "Check refs_online entries"
}
```


### [2026-09-05T20:07:19.515Z] TOOL RESULT

```
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118
SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
TZF {"title": "Mohsen Abolghasemi, Tarikh-e Mokhtasar-e Zaban-e Farsi, Bonyad-e Andisheh-ye Eslami 1373/1994", "kind": "website", "url": "https://ketabnak.com/book/81646 (142 pp. PDF; login) ; https://farhangoadabeirani.blogsky.com/1395/07/20/post-1048/ (download post)", "lookup_hint": "Not on archive.org (only his دستور تاریخی زبان فارسی: archive.org/details/20220417_20220417_2237, and تاریخ زبان فارسی on samta.samt.ac.ir / library.tebyan.net/f/Viewer/Pdf/168187 which overlap in content).", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "PDF exists but not downloadab
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol
CHEUNG null
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it
```


## [2026-09-05T20:07:21.985Z] TOOL CALL #5: Bash

```json
{
 "command": "head -80 data/verification/page-127.json && echo ---- && cat tools/verify_check.py | head -60",
 "description": "Look at an existing verification file and checker"
}
```


### [2026-09-05T20:07:22.042Z] TOOL RESULT

```
{
 "pdf_page": 127,
 "book_page": 97,
 "verified_by": "claude-opus-5",
 "verified_on": "2026-09-05",
 "entries": [
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
     "where": "Mann, d-section (grep 'dhem' in IEC.txt)",
     "stance": "silent",
     "note": "Mann has dhen- (2) 'forehead', dhenguhó, dhinió etc. but no *dhem- 'blow, smoke' headword."
    }
   ],
   "nodes": [
    {
     "id": 1,
     "lang": "Avestan",
     "words": "dam; da-dhmainya",
     "verdict": "plausible",
     "derivation": "The Avestan language has no attested finite verb dam- 'to blow': Bartholomae, Altiranisches Wörterbuch 731 f., knows only the Young-Avestan present participle daδmainiia- 'sich aufblasend, -blähend', said of (tree-)frogs at Vd. 14.5 and 18.73, which he analyses as 'ein Praes. auf -ainya- mit Inl.-Red.' and compares directly with 'ai. dhámati \"er bläst\", np. damīdan \"blasen\"'. Nourai's 'da-dhmainya' is that very word in his own transcription — he writes Avestan δ as dh and marks off the reduplication syllable da- with a hyphen — so the form is faithful; but his gloss 'I inflate, breathe' is wrong: it is an adjective/participle 'puffing itself up', not a 1sg verb. 'dam' is the root abstracted from that participle, i.e. Proto-Iranian *damH- 'to blow, breathe; to swell' (Cheung 2007 s.v. *damH³), which is real and is the ancestor of the Persian words in node 2; it is simply not an Avestan word-form. Hence plausible rather than confirmed: right root, misdescribed gloss, and one of the two 'words' is a root citation.",
     "derivation_fa": "در اوستا هیچ فعلِ صرف‌شدهٔ dam- «دمیدن» به‌جا نمانده است؛ بارتولومه در فرهنگ ایرانی باستان (ستون ۷۳۱ به بعد) تنها اسمِ فاعلِ جوان‌اوستاییِ daδmainiia- «باد کرده، خود را باد کننده» را می‌آورد که دربارهٔ قورباغه‌ها به کار رفته (وندیداد ۱۴٫۵ و ۱۸٫۷۳) و آن را ستاکِ حالِ پسوندِ -ainya- با تکرارِ درونی می‌داند و مستقیماً با «dhámati سنسکریت» و «دمیدنِ فارسی» می‌سنجد. صورتِ «da-dhmainya» در کتاب نورایی همان واژه است (او ذالِ اوستایی را dh می‌نویسد و هجای تکرارِ da- را با خط تیره جدا می‌کند)، پس خوانشِ کتاب درست است؛ اما معنایی که به آن داده («من می‌دمم») نادرست است، چون این صورت صفت/اسمِ فاعل است نه فعلِ اول‌شخص. «dam» هم واژهٔ اوستایی نیست بلکه ریشهٔ ایرانیِ باستانِ *damH- «دمیدن، باد کردن» است (چونگ، ذیل *damH³). بنابراین ریشه درست است ولی معنا و صورت‌بندیِ گره با احتیاط پذیرفتنی است.",
     "sources": [
      "https://en.wiktionary.org/wiki/%D8%AF%D9%85%DB%8C%D8%AF%D9%86"
     ],
     "ref_check": [
      {
       "ref": "POK:247",
       "status": "supports",
       "note": "IEW 247 (POK_01.txt line 3517): 'av. daδmainya- ,sich aufblasend, blähend, von Fröschen''  — the same Avestan form under the same root."
      }
     ],
     "consulted": [
      {
       "src": "BRT",
       "where": "Altiran. Wb. 731 f., s.v. daδmainya- (BRT.txt line 13362)",
       "stance": "partial",
       "note": "'j. däSmainya- Adj. \"sich aufblasend, -blähend\", von Fröschen … Eig. PPA. … — Vgl. ai. dhámati \"er bläst\", np. damidan \"blasen\"' — supports the root and the link to Persian, but shows the form is a participle, not '1sg I inflate'; and Bartholomae has no Avestan verb entry dam- 'to blow' (his dam- entries are 'Haus, Wohnung' and a present stem of dar- 'to hold')."
      },
      {
       "src": "CHEUNG",
       "where": "s.v. *damH³ (CHEUNG.txt line 4670 ff.)",
       "stance": "supports",
       "note": "'*AVESTAN: Y Av. daδmainiia- \"blowing up (intr.)\" (V 14.5, V 18.73)' listed as the only Avestan reflex of *damH³."
----
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
```


## [2026-09-05T20:07:34.775Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n 60,200p /home/sfmqrb/git/rishe/tools/verify_check.py",
 "description": "Rest of verify_check"
}
```


### [2026-09-05T20:07:34.809Z] TOOL RESULT

```
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


## [2026-09-05T20:07:35.086Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | head -80",
 "description": "List refs dir"
}
```


### [2026-09-05T20:07:35.134Z] TOOL RESULT

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
```


## [2026-09-05T20:07:39.795Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"dhīs\\|dhis-\\|dhīsos\\|dhisos\" IEC.txt | head -30",
 "description": "grep IEC for dhis"
}
```


### [2026-09-05T20:07:39.861Z] TOOL RESULT

```
2914:dhis- (1) ‘god, godlike’. Cf. dhiio Skt. dhisnyah ‘devout’; dhisnyam /side-altar'; dhisà 'piously'; Osc. fíísna- ‘tempie’; Umb. fiso, acc sg. fisoni (a god); fise, ds. (to a god); ON dis pl. dísir ‘goddess’; Icel. dísa, id. beside vatnadís *naiad'; OCS cf. diosovü, adj. *of a heathen god?
2915:dhis- (2) (?) Per. diha ‘village’; Myc. & Gk. this, thin, gs thinós “earth, bottom, pile, silt’
3392:twās "Tool": Du. dwaas ‘mad; fool; OE dwæs, id.; Norw. cf. dvask ‘dull; idle’; Li. cf. dvésena ‘carrion’; Latv. cf. dvēsele “soul; dvéesma ‘breath’. (Note on Lat. bellua & bestia. These words seem to represent synthetic cpds. whose first element *guer- is embodied in vescor (see guersK- below) with dialectal b- for v-. For bellua cf. also Gk. borós & leía, léon. Oscan forms are ambig. *dhis-?)
3393:dhuesro- (dhuesoro-) see dhueso, dhuesos above, and cf. dhis- Skt. dhvasrah, dhvasirah; Lat. Februus (epi- thet of Pluto); februum, n. pl. februa 'puri- fier; atonements for the dead’
```


## [2026-09-05T20:07:41.253Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=108 && NR<=113 {print \"===== leaf \" NR-1 \" =====\"; print}' IEC.txt | head -200",
 "description": "Print IEC leaves around p191"
}
```


### [2026-09-05T20:07:43.006Z] TOOL RESULT

```
===== leaf 107 =====
teln, v. ‘muddle through’; ON tyrðill (auk' ^ a clumsy bird). Cf. also Cz. drdat ‘totter along’. (Rum. dărdală, s. ‘trembler; stammerer' is ambig.)
düros (1) ‘far, long-lasting, long’. Cf. deuor-, duår-, deuó Skt. düráb, comp. dáviyas ‘distant’; Av. düro; Per. dor, id.; Lat. cf. duro, are “last
düros (2) ‘hard; hard substance’. Cf. duso- ros. (The Lat. & Celt. evidence is ambig.). Cf. WP I, 768 & 778 Oss. dor, dor ‘stone’; Lat. dürus; Ir. dúr “hard; withered; stupid'; Br. dir ‘steel (but W dur pl. -iau “steel represents a form *deur-. W dewr "brave seems to be.a cpd. For W dir 'certain', see dhiros)
dus-, dusi-, px. 'ill-, mis-, hard-, un- (z- gde to duis- and deus-). Cf. dusá, dusoros Skt. dus-, dur-, etc: Av. du&-, duZ-, dus-, etc. OPer. du$-; Arm. suffix arku (in dzajn- arku ‘weeping’, etc.) beside erkn, erkk ‘toil’; Gk. dus-, cf. also o-dúnē, dúē ‘grief, misery’; Ir. do-, Gaul. du-; OBr. do-; MW dy- (in dy- hedd ‘ill-health, sad state’, fr. *dus-séd-); Go. tuz-; OHG zur-; G zer- (also fr. dis-, q. V.); OE ON tor-; e-gde in OE teosu Cham", fr. *deusu-). See next
dusa, io ‘hardship, toil. Cf. dus-, dusnos, dusoros, etc. | Arm. erk (o-st.), erkn, & erkk (pl. form) ‘toil, childbirth; arkk ‘evil’, -arku (suffix: 4H-); Gk. dúē ‘woe’; OHG cf. haga-zussa Cwitch', lit. “hedge-demon?); ON (alleged) tysja “hag, evil spirit; Cz. cf. dna Ceout, fr. *dusna. See dusnos). (For Baltic forms in du-, see dhu-). For OCS dùšdí “rain” cf. Skt. dur-divasah "bad weather, rainy days. For Gk. düsphoros cf. Skt. durbharah and for dusmenés cf. Skt. durmanah, durmanas (adj. & s.); Av. dusmano, n.; Per. dušman, and perh. EMAIb. én-dhuné ‘mockery’; për- dhuni 'disgracefully'; Ir. doim (*poor, wretch- ed", opp. of soim ‘rich’, fr. *su-im-, see su-, px. "well (Arm. t'ánami ‘enemy’ is a LW fr. Per.)
dusoros (dusro-) ‘trying, hard’. Cf. WP I,
düros — dueighos, à (duigh-)
Lë
10
20
25
30
35
40
45
170
768 & 778. See dus-, düros Arm. txur ‘sad’; txrim ‘grieve’; Gk. duerós be- side (o)düromai, v. (grieve', fr. o! + *dusr-). (Ambig. are Lat. dürus, Gaul. düros, Ir. dúr, see düros above); Umb. Sab. dir- (bad, w. -i- fr. *-ü- ? as in pir ‘fire’, etc., but cf. the equally ambig. Lat. dirus)
dusiàio, denom. ‘doubt’. Cf. duis-, duidh-, du- Gk. duázo, Alb. dyshoj, id.
dusimen-, dusmen-, see dus-, dusà
dusió “mar; be marred'. Cf. WP I, 766 & 816. See dus-, dusa, etc. Skt. düsyami “be spoilt’; Gk. cf. dos *mi- serable'; LG cf. tuschen, tüschen ‘extinguish’; (e-gde in) OE teorian (‘falter; tire, exhaust, fr. *deuséio)
dusi-qurios (dus-) “difficult; difficulty’. Cf. dus-, quer- Skt. duskarah (e- or o-gde); Av. dus-korotom *evil deed": Per. dusKar; Olr. doccair, doscer; Ir. docair *uneasy, sad'
dusmen- see dus-, dusà
dusnos, à “evil, sad; evil, sadness, hate. Cf. dus-, dusa, etc. Gk. o-dune (grief, fr. o! interj. + ^; cf. kin- dünos ‘risk’; Arm. erkn, gs erkan ‘toil, labour in childbirth; EMAIb. &n-dhuné (in phr. qell — ‘mock, pér-dhuni *disgracefully"); OHG zorn ‘hate, rage’; MHG zorn (bitter, cruel; rage’. fr. *dusnó-); OE torn ‘cruel, “harsh; offence’; Du. toorn ‘anger’; Cz. dna ‘gout’. (For Cz. dma, Latv. dusmas, etc. see dhusm-)
dus-qur-, see dusi-qur-
duuoim, dat. of type *duuó, see duðu, etc. Gk. duoin; Go. twaim; OHG zweim; OCS cf. düvéma; Li. dviem; Latvian diviem, id.
duåros ‘long-lasting’. Cf. düros (1) Arm. erkar, i-st. long, slow, protracted’; Gk. dérón, dwarón, adv.; Norw. cf. tvaere ut 'spin out, last
dueighos, à (duigh-) dueios, duei-, duoi-, etc. Alb. degë ‘branch’; MHG zwic, ges: Du. twijg; Fri. twiich; OE cf. twíg, beside twigan ‘sto doubt’; Li. dveige ‘pair
===== leaf 108 =====
’; dveigys, m. 'two- year-old’
‘forked branch’. Cf.
171
dueiið (dueið) "make into two, pair, fold, divide into two”. Cf. duoi- MHG zwien 'graft'; Li. dveju, eti “pair off
dueilos, is ‘timid; fear. See next Arm. erkiwy, erkey, i-st. ‘fear’; Gk. deilós ‘timid’
dueinos ‘awful’. Cf. dueilos and WP I, 775 & 816 Gk. deinós; Mir dían ‘sudden, violent, severe’; ON (alleged) ü-tvínn ‘fearless’ (fr. *n- ^). (MIr. déne ‘dash, hustle is < *duei- nio)
dueisió (duis-) (fear, hate’. Cf. duis- & WP I T5 Skt. dvesti je: Av. cf. tbaesayei(mi) "make fear, threaten’; Gk. deísomai ‘shall fear
dueios (dueiios) ‘twofold, paired; two, pair”. Cf. duoios, dueiio, etc. Skt. (ambig. dvayáh; Lycian cf. kviiehi (second? or *other); Ir. deidhe ‘pair; MHG zwi “branch, cutting; OS cf. twio ‘twice’; OE twegen; ON tveir (*two', m.); ON cf. tvi- ‘twofold’; OCS dvoj (ambig.), id.; Li. dvejas, id.; dveji, f. ‘pair
duendilið, see duindilið
duəi, fem. form of duðu, q. v. Tokh. A we, B wi; Alb. dý; OBr. & Br. diu; W dwy; MHG zwei; OE twa; OCS dvé; Li. dvi. (Latv. divas, f. “2? is a ‘new’ formation). Cf. WP I, 817
dui-, px. *'two- bi-. WP I, 818 Skt. dvi-; Av. bi-; Per. cf. dü-, dav-; Tokh. cf. we, wi; Arm. krk-; Gk. di-; OLat. dui-; Lat. bi-; MIr. dé-; OHG zwi-; OE twi-; ON tví-; Li. dvi-. (Latv. cf. dvinis *twin"). See the fol- lowing compounds.
dui-bhàn- in Gk. dipháninos lákhnos; Arm. erkban ‘amphibious, ambiguous’; *-bhàt- in Skt. dvibhatam; Arm. erkbajK ‘doubt, sus- pense; Gk. diphásios, díphatos, diphasía; *-bher- in Gk. díphoros, díphros; Ir. dabhar ‘pitcher’; OHG zwibar, zubar 'two-handled pot; LW in Cz. Cber, Ukr. ceber mus": *-dent-, -dont-, -dnt- in Skt. dvidantah, dvidat; OLat. dvidéns; Lat. bidéns; Li. dvidafitis; *-duid- in Arm. kr-kut (i-st. “twig'); cf. Lat. divido, Ere (Arm. variant zurk 'deprived', represents a variant *di-duid-, isophonic w. Lat.); *-duin-
dueiió (dueió) — duiKsos, ios
20
25
30
35
40
45
172
in Arm. krkin ‘double’, cf. LG twit ‘narrow dividing lane’; E dial. twitton, twit, id.; *-&en-, *-Genes- in Skt. dvi-jánman; Gk. digenés and Lat. bigener, bigeneris; *-gueni- in Skt. dvi- jànih 'bigamous' and ON tví-kveni; *-iug- in Skt. (o-gde) dvyogah; Gk. dí-zux, -zugos & Lat. bi-jugis, -jugus; cf. Latv. div-jugs, s. 'two- in-hand'; *-plos, -plos in Av. bifro; Gk. diploüs, -plóos, -plós; Lat. duplus; Go. tweifls; OHG zwival; OFris. twifil and Du. twijfel; *-ped-, pod-, pd- in Skt. dvi- padah; Av. bib- dəm; Arm. cf. erkot-ani; Gk. di-podēs; Lat. bi-pēs, gs -pedis; cf. OE twi-fete; ON tví- foettr; *-poltos, -pltos in Gk. dí-paltos, di- plásios; Go. -falbs; MHG zwi-valt and ON tví-faldr; *-qusakos (or *-kakhos) in Skt. dvi- khakah, (-$akhah) ‘forked, two-pronged, bi- furcated'; Gk. dípsakos; Per. dū-šāxe and Li. dviSakas; *-rotos, (-rothos) in Lat. birotum, -rota and Li. dvirátis (fr. *rotios)
duidio 'doubt'. Cf. duidh- Gk. dizo, id.; Skt. cf. dvi-, cpds. and follow- ing
duid- (2) ‘seek’ Arm. krktem, id.; Gk. dízēmai, id. (for Gk. zētéð, see iāqueið)
duidh- ‘divided, in two” Skt. dvidhah, adj., dvídhà, adv: Tokh. AB wätk, v.; Oss. cf. dídåg; dudäg (adj. ‘double’; s. split); Alb. cf. dyzash “in two'; dyzoj *fold, double'; OLat. dubo, àre, Lat. dubito; OE cf. lang-twidig(?) (err. for -tidig?)
duigó ‘move, pluck, jerk’. Cf. WP I, 235 Gk. cf. kroko-dízo “card by plucking’; -dismós (the act); MHG zwicken ((2) *pluck); OE twiccian, id.; OCS dviZo, iti & dvigno, noti, v. ‘move’. (A variant *duik- may be represent- ed in Gk. édikon, aor. ‘I threw?
duik- “in two, twofold, halved’. See next Skt. dvisas, adv. “in two'; Arm. kes, gs kiso *half; OS tweho, wm. ‘doubt; Gk. cf. (?) Díkte *a Cretan mountain w. two peaks"?
duiKsos, ios "double, twin,
===== leaf 109 =====
 divided'. Cf. duik-, dui- Oss. dix, duwex (adj. 'divided'; s. (part); Arm. cf. erkics ‘twice’; Ion. dixós; Alb. dysh in two, double’; OS twisk (*twofold'; prep. "between"?
173
duindilo, ið ‘flicker, twinkle, blink’. Cf. dindil- Gk. (ambig.) dendíllo ‘wink, blink’; G zwin- zeln ‘glance’ beside MHG zwinzen ‘blink’
duinos, is (1) ‘double, twin’. WP I, 820 Arm. cf. krkin, gs krkno ('double', fr. *duiduin-); Lat. binus; Ir. díon “second line of a verse’; Li. dvýnas ‘paired; twin’; dvynjs “combined; Latv. dvinis, s. “twin?
duinos, à (2) (duisnos?) ‘turn, spin’. Cf. WP I, 820 Gk. dinos, dinë *'eddy; giddiness; lathe; threshing-floor'; cf. kor-dinéma *head-spin- ning; vertigo’; én-dina (pl. *entrails"); dinéo, v. “spin” (but Aeolic dinna ‘eddy’ suggests a type *duisnà, q. v.); OE twin ‘twine’; Du. twijn, id.; Sw. cf. tvinna 'twine, spin'; Nor. tvinne, id. cf. tvist ( yarn, twist’, fr. *duistós). See duisnos
duis ‘twofold, twice’. WP I, 818 Skt. dvis; Av. bis; Gk. dis (also di- in dí- phthera “split skin"); Alb. cf. dysh “in two; Arm. cf. erkics ‘twice’; OLat. duis; Lat. bis; Ir. dís ‘couple; Go. twis- ‘apart’; OE twis; MHG zwis. See next
duisios ‘double’. Cf. duis, duik-, duiksos Per. cf. dot ‘duplicity’; Arm. erkics “twice? beside erkir ‘secondly’; Gk. dissós, dittós; Alb. dysh. Variant (*duisKios) in OS twisk ‘twofold’; OHG zwiski, MHG zwischel, id. and cf. LG tüsch, wf. “narrow lane between houses’. Cf. also MHG zwisel (*double'; s. ‘fork; G Zwiesel ‘forked branch); EME twixt; G zwischen, etc.
duism “in two, through the middle Gk. dià; Alb. cf. ndér-dym (in doubt, fr. enter- ^); Per. düyum, s, duvum, adj. “second: OE cf. twinn *double'; twiman *waverer, hy- pocrite
duisnos, à “turn, spin; round’. Cf. duinos (2) The Gk. forms are ambig. but cf. Aeol. dín- na ‘eddy’; MHG zwirn, m. (fyarn', if fr. *duisnó-)
duiso, ið ‘threaten; fear. WP I, 775 Skt. dvise ‘hate’; Av. dviš-, țbiš- ‘torment, offend’, Arm. cf. erknčim ‘fear’; Gk. dío ‘scare away’; domat ‘scare; fear’. (Isophones
duindiló, ið — duðu, duuou, duo
20
25
30
35
40
45
174
are OHG zwiron, MHG zwiren ‘run out, fail)
(duiso(n), an extn. of *duis-, q.v. is sug- gested by LLat. *bissones “twins? Provencal bessons, and OS gi-twisan, id.)
duist- ‘twofold, divided, in two'. Cf. duis,
etc. Skt. dvisthah ‘ambiguous’; Tokh. A wást, B wásto, wasto ‘double’; Gk. *distós in di- stázo 'doubt; Alb. i dyshét ‘twofold’; Ir. dís ‘couple’; Olr. cf. diass ‘twosome’; MHG zwist ‘separation; quarrel’; Du. twist ‘quarrel’; ON tvistr ‘disunited’
duitos, ios (-Tios) ‘second’. Cf. dui-, duis,
duðu, etc. Skt. dvitáh “second form of Agni'; dvitiyah ‘second’; Av. bityo; Ober, duvitiya-; Per. dütà; Tokh. A wät, B wate; Alb. i dytë, id. beside dys, aor. dyta ((repeat', vi: Umb. cf. duti (again': Alb. së dyti, id.)
(duo, see duàu. Cf. Skt. dva (archaic dual form); Gk. dó-deka *12 and Lat. duo; OCS dva)
duoidh- ‘double, half, two-way’. Cf. dui-, etc.
Skt. cf. (vrddhi) dvaidhah *double'; Av. dvaidi “doubt, question’; OS twédi, adj. "halt duoiió ‘divide, pair, double’. Cf. duoios MHG zweien, zweigen; OCS dvojo, iti ‘doubt’; Cz. dvojit ‘double’; roz-dvojit ‘divide’ duoil- “division, pair, double LG twél ‘fork’; twélen ‘divide, split’; Lusat. dwél *doubt'; Li. dvailas (pair, brace’; adj. *twin-, fellow-")
duoin- ‘two, in twos, doubly’. Cf. dui-,
duóu, etc. Lat. bini; OLat. duini “two each, by twos, doubly’; binus ‘coupled? MHG zwene ‘two’: OCS cf. dvojnü *twofold'
duoità ‘fear, hate, envy’.
Av. dvaetha; Ir. (ambig.) daod
duoios, duoiios "double: couple, pair. WP
I, 819. Cf.
===== leaf 110 =====
 dui-, duóu, etc. Skt. dvayáh; Homeric doiós, beside doié *doubt; Go. twai, m.(); MHG zweie, f. ‘duality’; ON tveggja, adj. ‘twofold’; OCS dvoj, num. “pair”
duóu, duuóou, duó; f.n. duoi, duuoi ‘two’.
175
WP I, 817
Skt. dvau, dva, duva, fn: dve; Av. dva; Tokh. A wu, wü, B wi, wi, f. we; Oss. dowàá, duwä; Per. dü; Arm. erkuk, erku; Hitt. cf. duwan ‘apart’; Hiero-Hitt. tuvai ‘two’; Myc. duwou-; Gk. dúo, düo beside do- in dódeka; Alb. dy; Lat. duo, duae; Umb. dur, npl. (also) -tuva (sic); Lyc. toáas; OIr. dän. dó; MIr.
dhabros (dhaboros) — dhalghó
176
& Ir. dá, n. dó; OBr. dou, f. diu; Br. dau, f. diu; W dau, f. dwy; Cor. deu, f. dyw; Go. twai, twós, twa, OHG zwo, zwuo; OE twa, f., tü, n.; ON tvau, n.; Sw. två, but cf i tu ‘in two'; OE cf. tuwwa, tuwa ‘twice’; OCS dva, düva, f.n. dvé; Slovene dvo-, cpds.; Li. du, f. dvi; Latv. divi, f. divas; OPr. dwai, m.
Dh
dhabros (dhaboros) (1) 'supreme, sovereign, ruler. Cf. WP I, 824 Per. davar ‘ruler’; Tokh. A tpår, B tápr, tappre *high': Hitt. tapar-, v. ‘rule’; taparriyas ‘ruler’; Lat. faber (ambig.) (as adj. “clever, workman- like’. Speculations in WH: faber, EM ibid.); MHG tapfer “firm, full, heavy, considerable”; G tapfer ‘bold’; OCS dobrü (fine, goog’, and com. Si.)
dhabros (2) ‘puny, trivial’. (In Indo-Iranian this form has become confused with type dabh-, q.v. as in Skt. dabhráh “little, trivial: Av. davro, id., though, formally, metathesis is possible). Cf. dhabh-. E dapper ‘small’; ON dapr, acc.sg. dapran ‘faint, weak, glum’ be- side daprast ‘grow faint’; Icel. depra ‘weak sight’; LG cf. bedeppert ‘flummoxed’ beside SG deppen ‘humiliate, make a fool of; Depp *fool'; Li. cf. dabüs ‘timid’. (A possible cognate of type dheb- occurs in Hitt. tepus *small). Cf. also OE dafte ‘meek, mild”
dhabh- “fitting; fit, able; joint. WP I, 825 Tokh. A tāppo ‘valour, fitness’; Lat. (name) Fabius; Go. ga-daban “fit; happen); OE dafen “fit, proper, mild, good” beside (*-a-) in defe, id.; ON dafna (v. 'thrive); Icel. döf ‘rest’; OCS doba ‘opportunity’; Cz. doba ‘period’; OCS dobli ('strong', fr. *dhabhio-); Slovene dobelj ‘useful, fitting’; Srb. dôb “season, age’; OLi. dabà ‘cuiture; nature, essence’; Li. ‘care’ beside dabùs ‘careful’; Late daba ‘way, habit,
able;
20
25
30
35
40
45
nature’; Finn. LW tapa, id.; Li. cf. dabnùs, dabinti “elegant; to adorn’ dhābh- ‘limp, flaccid’. Cf. dhabros D Skt. (ambig.) -dābhyah (‘frivolous’, in a- ° *serious); Alb. i dobë, í dobët ‘weak’; Sw. dof (‘sultry, blunt, stupid". Infl. of LG? & NG döf ‘stupid’. See dhoubh-); Go. cf. af- dobnan ‘grow dumb’ dhabhló, dhabhró, ið (?) ‘surge’. Cf. dabh- Skt. dabhráh (ocean; EMDu. daveren ‘tremble’; ON dafla ‘dabble, splash? dhadhló, dhadhró, ið (?) ‘waver, tremble’. Cf. dhedher- MHG tatern ‘chatter’; G tattern ‘shake, dod- der, twaddle’; Icel. daðra ‘flirt; Sw. darra ‘tremble’; cf. E dial. daddle ‘stagger, dawdle’. (A form *dhadh- seems to be present in EME to dade ‘to toddle’ and Li. dadu, eti “cackle') dhagh- ‘beautiful, fine, abundant, good, harmonious’ Gaul. dago-; OBr. da; W da ‘good’; MHG tagen, tegen ‘confer, arbitrate’; Du. dagen ‘summon’; G cf. Reichs-tag; Du. Rijks-dag; EME days-man ‘arbitrator’; EMDu. cf. dege- lijk ‘honest’; LG cf. d&g, m & f ‘good man- ners’; Li. dažyti ‘to eeh daZalas “orna- ei: ; dažnas ‘many 3... * Latv daZs, id. dhaloros, is ‘verdant, lush". WP I, 825. Cf. dhalió Arm. dalar (i-st. *green"); Gk. thalerós, id. dhalgho “hold, squeeze'
177
Alb. dal (2) “stop”, tr.; OW dala, daly “hold, detain’; W dal, daly, id.; Br. dalé, daléa, impv. dal! ‘delay, demur’; MHG cf.
===== leaf 111 =====
 (?) talgen ‘knead’. (Cor. dalgh, m. dalghen, f. ‘hold, grip’ represents a formula *dhalghs-)
dhalio (dhaliio, dhales-) ‘fortune, produce, outcome”. Cf. dhalio
Gk. thalía, f. thálea, npl.; W daili, pl deilliau -
*próduce?; (?) OCz. dole ‘fortune, success’; R dolja ((2) ‘destiny’. In sense (1) see dal- ‘part, share’, as in OCS, but SI. forms are ambig.).
dhalið ‘come out, project, succeed’. WP I, 825. Alternative form: dhalno Gk. thállo ‘sprout, bloom’; Alb. dal ‘go out, come out
dhalos, is ‘bud, sprout, excrescence’. Cf. dhalio Gk. thálos, n.id.; Alb. e dalë “boil, blain'
dhálom, is (dhol-?) “mark, end, matter’ (?) See dhol- Ir. dáil (1) "matter, case, decision'; OFris. dól ‘aim’; Fris. & Du. doel, id. (Du. also “sense; boundary”. Cf. be-doelen, v. “intend, mean’; cf. also Fris. doel-stien *boundary- stone’; Skt. dharab, m. “edge, boundary’; dhára “margin, edge, fence, tip’, but -à- and -r- are ambig.)
dhám-, see dhom-
dhambos ‘dim, cloudy; dimness’. Cf. WP I, 824 & 851. Cf. dhmb- Arm. cf. damarim (‘get confused’. Ambig. cf. dhmb-); Gk. thambós, adj., thámbos, m. ‘dim; dimness’; OHG dampf; LG damp ‘steam’; E damp, adj. & n. (Initial d- in OHG MHG and Mod. Ger. unexplained)
dhámol-, see dhemol-, etc.
dhameor- ‘bustling; bustle’ Ir. damhair ‘dashing, eager’; f. "baste: MHG tamer, temer ‘din’; temeren, v. ‘forge’
dhandhəlð, io ‘shake, totter’ Arm. dandayim ‘dally’. Ambig. see dhndhol-; Gk. cf. tanthalüzo, tantharüzo ‘tremble’; E to dandle; MHG cf. tant ‘twaddle’; tanten, v. ‘play tricks. Variants: Arm. dandacem (*waver; rove’, fr. *dhandhitio); Gk. tantha- rüzo: E dial. to dander ‘to stroll. Frisian has a further variant of type *dhanghol- in
dhalio (dhaliio, dhales-) — dheguhlos, is, o(n)
10
20
25
30
35
40
45
178
dangelje ‘to strolP', cf. E to dangle
dhåros, à “firm: firmness'. Cf. dher-, dherm-, dhor- Skt. (ambig.) dharab (adj. holding"); Li. dóras ‘honest’; dorà, f. ‘virtue’; Per. där 'posses- sing’, in cpds.
dhaunos (dhausno-?) *wild animal, wood- land animal. Cf. dheus-, dhous- Hes. thaünon, acc. ‘animat’; Lat. faunus ‘god of woods & fields', fauna “animals; Illyr. cf. *daunas (in Daunus, father of Turnus, in Aeneid XII)
dhàáu-, dhou- “look at, admire, wonder Gk. tháomai, fut. thésomai, cf. thaüma, théà, theetós, Dor. thaetós; ON dá (2) “admire”, dár, n. dátt ‘smitten’; dáendi ‘admiration’. (The vowel of ON dá, etc. as in grár, hár, há)
dhedh- ‘nurse’ Per. dade, id.; cf. S.It. deda, id.; Gk. cf. (*-é-) Tēthús (nurse of Hera) and (alleged) téthe ‘nurse’; Ir. cf. deol, diúl ‘suckling’, isophonic w. Gk. thēlé, see dhēl-; cf. also Ir. dedel ‘she-calf
dhëdh- (hypocorism of a relative) Gk. téthē ‘grandma’; téthís “aunt'; OCS dédü ‘grandpa’; Li. dēdis, id., dede ʻuncłe’; cf. dēdienē “aunt?
dhedherið ‘shake, dither, hesitate, lounge’. Cf. dhadhlo Arm. dederim ‘lounge, loiter; LG dädern ‘frolic; EME didder, v. ‘shiver; Lat. cf. *fibrillare ‘to twitch’ and (o-gde) G tattern ‘tremble; ON daðra ‘dally, flir? but see dhadhló
dhedhló (?) “suck? Lat. cf. fellare, id.; Ir. deolaim, id.
dhedhmos, à ‘statute, law’. Cf. WP I, 829 and dhé-mi, dhídhe-, etc. . Gk. tethmós, thesmós; W deddf, id.; cf. MIr. dethbir (laws; adj. 'legal). See next
dhedho, ið “put, set? (intensive form of dhé-mi, etc.) WP I, 827 OCS deZzdo; Srb. dedem; Li. dedü
dheguhlos, is, ö(n) “burning, heat, radiance’. Cf. dheguhó, dhoguh- and WP I, 849 & 865. Cf. also guheguh- Alb. diell ‘sun’; MIr. del, dellrad ‘brilliance’; Ir. dealán, m. ‘burst of sunshine, brightness,
179
spark, flame, heat, light; deall-rach ‘radiant’; Br. cf. délin ‘steel,
===== leaf 112 =====
 of a tinder-box';; MHG tëgel (?) (Ccrucible', if distinct from tigel, id. cf. Lat. figulus): Li. déglas ‘brand’; dē- galas ‘wick’; pl. ‘fue’; Latv. deglis, degulis “tinder, touchwood, firebrand’
dheguho (dhoguh-) ‘burn, fire’. Cf. dhe- guhlos, dheguhro-, dheguhto- and guheguh-. WP I, 849 Skt. dahàmi; Av. daZai-; Tokh. A tsak-; AB tsák- (also ‘bite, sting"); Alb. djeg, aor. dogja (fr. *dheguhiou, cf. Li. degiaü) beside n-dez (*kindle', fr. *dhoguheio, a factitive); MIr. dóim, Ir. dóighim and dóghaim (cf. OLi. degmi); Br. devi, pp. devet; Cor. dywy; W cf. cyn-neu ‘kindle’; cyn-ne ‘burning’ beside OW deifaw 'roast; Li. degü, OLi. degmi, inf. dégti; Latv. degu, dedzu, inf. degt. Lat. foveo, tr ‘warm’; fomes, -mitis (for the second element "wood cf. termes, trà-mes) seems to represent o-gde factitive
dheguhos, -es-, ios, is ‘burn, burnt matter, fire; burning” Mir. deg, dag ‘flame’; Ir. deigh, daigh ‘fire’; OCS cf. *degüti; Cz. dehet, R dégot ‘tar’; Li. degesys ‘burnt smell; degesas ‘charred spot’; degiai, pl. ‘slag’; degis, m. ‘burn’; Latv. dedzi, pl. ‘charred field”; degas, pl. 'burnt-out ruin'
dheguhros, à, is “burning; burn, burnt matter”. Cf. dheguho, etc. Skt. dahrah “forest fire’; Gk. téphra ‘ashes’; Osc. tefürüm “burnt offering? and tefra “roast pieces? seem to be Gk. LWs; MIr. dagar *blast, pang, dart
dheguhtos, is (fired, burnt; burn, burning, firing, fuel". See dheguho Skt. dagdhah; Tokh. B $akwse (‘brandy’ or sim.); Scyth. tabiti ("Vesta — vowel as in Sc. sagaris, see seküris, à); cf. Gk. Hes. thépta- nos ('kindled': Li. degtinis (burnt); Alb. i djegët ‘burnt’; Ir. dé, gs déithe ‘spark, smoke’; W daith, pl. deithion ‘blaze, flash’; MHG tāht ‘wick’, OCz. dehet, gs dehte ‘tar’; R dëgoť, id.; Li. degtas ‘wick’; degutas ‘tar’; Latv. deguts ‘tar’
dheig- (dhoig-?) ‘shoot, pierce, stab, sew’. Cf. dhig-
dheguhó (dhoguh-) — dheio, dhëmi
10
20
25
30
35
40
45
 
180
(The evidence of Lat. figo, ére ‘pierce, wound" and of Latv. diegst, inf. digt “bud, shoot beside diedzu, diegt “thread, sew' is am- biguous)
dheigó, io “shape, mould, make’. (There is some confusion w. next, q. v.) WP I, 833 Tokh. (ambig.) A tsek-, B tsaik-; Lat. cf. fingo, pf. finxi beside figulo, figlinus, etc.; Osc. cf. fifikus “shalt make’; Fal. fifiked (if not fr. *tuak-, q.v.) “has shaped; MHG tichen, sv.l. *make, form" beside tich *dam'; OE dic: Du. dijk; (?) cf. Cz. diže (trough for kneading dough’, but see next entry); metath. in OCS ziždọ, zidati “build, found”; OLi. Ziedmi, Li. žiedžiù, Ziesti (“fashion on potter's wheel). See next entry
dheigh- ‘shape, earth up; form, wall (There is some confusion with dheig- above). WP I, 833. Cf. dhoigh- Skt. (ambig. prob. o-gde) dehah, am “shape, body’; Av. (pairi-) daezo ‘surrounding fence” beside diz- “earth up, cover’; LW in Arm. dez ‘mound’, dizem ‘pile up’; Gk. teikhos “outer wall, dam’; Ose. feíhüss, acc.pl. ‘walls’; Go. digan (z-gde) ‘shape, mould’; OPr. zeidis (metath. *wall') For Cz. dize ‘kneading- trough” and OHG teic, E dough, etc. see dhoiĉh-. The connexion, if any, with OE digan ‘overcome, survive, benefit’ is obscure
dheió (1) ‘suckle, milk; suck at the breast’. Cf. dhen- (1), dhinió. WP I, 829, and see dhoið Skt. dhayami; Av. dà-; Oss. däin, dajun, pp. dadton; Arm. diem; Gk. inf. thé-sthai "be suckled'; Hes. thenion ‘milk’, gala-thenós, aj. tunweaned'; Lat. cf. fe-mina; OHG Gen. lsg: taju beside MLG dien ‘suck, suckle’; OE dēon ‘suck’; cf. diend ‘suckling’; Sw. di ‘suck’; giva di ‘suckle’; Latv. dejals ‘mother’s milk, accretion of milk’. For Sw. dägga ‘suckle’ and OCS dojo, id. see dhoið. (NB. Per. dāyā ‘nurse, wetnurse, midwife�
```


## [2026-09-05T20:07:50.627Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\n# find line index of dhis- (2)\nfor i,l in enumerate(lines):\n    if l.startswith('dhis- (2)'):\n        idx=i; break\nprint('line',idx+1)\npos=sum(len(l)+1 for l in lines[:idx])\nleaf=t[:pos].count('\\f')\nprint('leaf(0-based)',leaf)\npages=t.split('\\f')\nprint(repr(pages[leaf][:200]))\nprint('---- full leaf ----')\nprint(pages[leaf][:4000])\nEOF",
 "description": "Locate IEC dhis leaf"
}
```


### [2026-09-05T20:07:52.624Z] TOOL RESULT

```
line 2915
leaf(0-based) 119
'uck?\ndhiros ‘firm, sure’. Cf. dhighros. WP I, 857 Skt. dhirahb "lasting, steady, firm’; MIr. & Ir. dir “due, fit”, cf. direach ‘direct, straight, sure, exact, right, true’; W dir ‘certain’; (isophonic'
---- full leaf ----
uck?
dhiros ‘firm, sure’. Cf. dhighros. WP I, 857 Skt. dhirahb "lasting, steady, firm’; MIr. & Ir. dir “due, fit”, cf. direach ‘direct, straight, sure, exact, right, true’; W dir ‘certain’; (isophonic with Li. dýrinti ‘butt in")
dhis- (1) ‘god, godlike’. Cf. dhiio Skt. dhisnyah ‘devout’; dhisnyam /side-altar'; dhisà 'piously'; Osc. fíísna- ‘tempie’; Umb. fiso, acc sg. fisoni (a god); fise, ds. (to a god); ON dis pl. dísir ‘goddess’; Icel. dísa, id. beside vatnadís *naiad'; OCS cf. diosovü, adj. *of a heathen god?
dhis- (2) (?) Per. diha ‘village’; Myc. & Gk. this, thin, gs thinós “earth, bottom, pile, silt’
dhightos — dhmb-
20
25
30
35
40
45
192
(dhit-, extn. of dhi-, q.v.)
Av. dita ‘look’; MPer. ditan, inf. ‘to look, see’;
Per. didam, Kurd. didem, id.
dhià, dhiam- (extn. of dhi-, q. v.) ‘sign, mark, note’ Skt. dhyami ‘think’; dhya ‘meditation’; dhya- nam “thought”, cf. also dhyåmab "dark black’; Gk. séma, Dor. -ā- ‘sign, device, landmark. (For Cz. z-dieti sé, z-dát se see deio (2))
-dhlom (agent-suffix). Cf. -trom Skt. var-dhram ‘thong’; Gk. thus-thla, pl. “instruments in Bacchic ceremonies'; Lat. pà- bulum, pati-bulum, etc.; Cz. Si-dlo, OCS Si-lo *awl', etc.; beside Cz. lepi-dlo ‘gum’; Li. ar- klas *plowshare'
dhlbh- ‘hollow’. Cf. dhelbh-, dholbh- Gk. cf. (variant) óph-thalmos (lit. *eye-hole”, fr. *dhijmo-); OCS dlübo, dlübsti ‘hollow, gouge’; OCS cf. dilübokü, Srb. dubok, Big. dlábok ‘deep’; Li. dilbis “armpit'. (Isophonic are Latv. dilbs ‘forearm’ and dilba, dilbis ‘shin’; Li. dilbos “lower forehead' and Li. dilba “lazy person”, but the connexions are not obvious)
dhlgho (?dhlguh-) ‘stab, wound, burn, smart Gk. cf. ? thálpo (aor. mp. e-thálph-then) (2) ‘sting’; OHG tolg, OS dolg, OFris. dolg ‘wound’; OFris. dolgia, delga, v. ‘wound’; ON dylgjur, pl. ‘rancour’; Li. dilgüs ‘smarting, burning’; dilge ‘nettle’; dilgstu, dilgti ‘burn, be stung’; dilgsiu, eti ‘stab, sting”
dhlso, io ‘crush, wear away’. Cf. dhul- Gk. thláo, adj: thlastós *crush, pound'; OE (?) dylsta ‘pus, filth’; Li. delu and dilstu, inf. dilti ‘wear away, wane’; Latv. dylu & dilstu, dilt, id.
dhm-, dhm-, dhmə (radical element of dhom-, dhüm-, q. v.) (1) “blow; swell Skt. dhma-, dhma ‘blowing; blower’ beside dhmatáh ‘blown’; Hitt. dannattas ‘empty’, Gk. cf. ás-thma (*n-Ks-dhmn-); MHG cf. vra- demen, vre-demen (‘give off vapour, fr. *pro-?); Cz. duty ‘hollow’
-dhmos (deverbative noun-formant) Gk. sta-thmós, skar-thmós, etc. Cf. dhedhmos
dhmb- 'deadened, stupefied; stupor’. See next and dhemb-, dhamb-
-
193
Arm. cf. (ambig.) damarim ‘get muddled’; Gk. (ambig.) thámbos, etc. (*-am- or *-m-); Du. dompen ‘smother’; dompig ‘muggy’; EME dump ‘stupor’; E to dump; Lancs. dial. cf. to dimp ‘stub out’; ON dumpa ‘thump’; Norw. dumpe ‘plump, fall heavily’; Li. diñ- binti ‘flounder’; Latv. (ambig.) dimba ‘scrape, difficulty’
dhmbh- (1) ‘stupefied; stupor’. Cf. dhmb- and dhemb-, dhamb- and WP I, 824 & 840. (There is some confusion between this and the preceding. MHG dumpfen and G dumpf, etc. seem to be a compromise of type *tmb-, see tumb-) Gk. táphos, n. ‘stupor, amazement’; Hes. tha- pan, acc. f. ‘fear’ (uncertainly to kró-taphos ‘temple of head’); Go. dumbs, OHG tumb; OE & Sw. dumb, etc.; Latv. cf. (ambig.) dimba ‘scrape, difficulty’.? *dhmb-. O-gde in Skt. dambhah “fraud”, lit. “bemusement. Cf. also Arm. damarim ‘get confused' (ambig. cf. dhmb-); EMDu. dommeren ‘doze, snooze’
dhmbh- (2) ‘tomb’. See dhnguh- Arm. damban, id.; Gk. (ambig.) táphos. A variant occurs in MHG tümpfel *water-hole? beside (W. Saxon type) tümpel *cunnus'; E
```


## [2026-09-05T20:08:21.737Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KNT dahyu ===\" && grep -n -i \"dahyu\" KNT.txt | head -40 && echo \"=== KNT visadahyu ===\" && grep -n -i \"visadahyu\\|visa-dahyu\\|vispa\" KNT.txt | head -30",
 "description": "grep Kent for dahyu / visadahyu"
}
```


### [2026-09-05T20:08:21.853Z] TOOL RESULT

```
=== KNT dahyu ===
1193:pIE *yikuo-, OP visa- ‘all’, also in visadahyu-; OP nspa- (with Med. sp) in vispaeana-; Av. vispa-, Skt. visva-.
1549:(2) In -u- stems: (Ar.) -au in loc. sg. dahyauv-à, -u- in loc. pl. dahyu-$uvà, -àu- in nom. sg. dahydu-§; see $180. Nom. sg. Dérayava*us and acc. -va'um with -u-, gen. -vahaus with (Ar.) -au-. Perhaps /Pirava, Nile’ with -àv-, to piruš ‘ivory’, cf. Lex. s.v.
1669:-u»- or -v-, as in dahyufwà, атїуйшй@ (cf. Skt.
1917:ing all (kinds of) men’; v1sa-dahyu- ‘containing
2157:Асе. Sg. Masc.: magum, zrafum, gidum; Dära- yava’um; Babirum, Margum; visadahyum; per- haps [agurum].
2178:'alogical to the nom.;? Av. daióhaom graphic for vam); but as second element of a compound we find -dahyum in visadahyum (or -dahyaum, as fum? is ambiguous), and in А?Ра 26 we have DHy"wm*, which may be either DHyaum or DHyum (Av. dahyiim is probably for -уйт). OP loc. dahyauvd is dahyau» like Babirauy, with added -4; but the diphthong is here kept before the added vowel (unlike дабай). Nom. pl. dahyàva has the long diphthong extended from the nom. sg, and represents pAr. -dvas (so also Av. daióhávo) ; this form was extended to serve as acc. pl. in OP (so also in Av.). OP gen. pl. dahyiiném and dahyüvnám is a regular gen. pl. of -u- stems in Aryan (Av. dahyunqm). ОР loc. pl. dahyusud is the -u- stem loe. pl. with ending -su, + the postposition -@; whether phonetically -u$usü or -u&a depends on whether the u of -su was con- sonantized before the added vowel, or retained by analogy ?
2244:I. Adjectives are found in all classes of stems, and the history of their case-forms has been in- cluded with that of the substantives. The com- monest type of adjectival stems ends in -o- for masc. and nt., with -d- for the fem.: nom. pIE -os -om -ü = OP -а? -am -à (§169-§176). The -- stems are skaub-iš -im -ai$, yäumainiš aydu(ma)inis, ušabārim; the -i- stems are acc. sg. yauldatim], probably yau[da"tim], to masc. yaudant-, and nom. pl. aBagainiya to masc. abagaina- (§§177-9]. The -й- stems are paru- (nt. paru», gen. pl. partinam), nom. sg. masc. uedmarsiyu-§ and ulzsnalu-s, ace. sg. masc. visadahyu-m (§§180-3). The consonantal stems are атійрат-, mana"wvin-, tauviyah-, hamap- tar-, hamdtar-, tunuva^t-, all in nom. sg. masc.: artavd, manauviš, taunyd, hamapità, tunuvà with acc. sg. tunuva"tam and gen. sg. tunwa*tahyd of -o- stem formation (§§184-8).
2760:67. ApPosrTIVES occur in the following cases; lack of examples in the other cases is accidental: nom. DB 1.1, 1.53, and almost everywhere; ace. DB 1.54, DPd 2, DNb 4, etc.; gen. DB 3.59, DPd 9-11, XPe 14, etc.; loc. infrequent, DB 1.34f. More often the appositive, if more than а single word or if to an oblique ease, is expressed by an anacoluthie nominative phrase, followed by a resumptive pronoun or adverb ($314a; 8312). Partial appositives occur as in DB 1.34f pasdva drauga dahyawd vasiy аата щй Parsaiy ша Mädaiy utü aniyãwā dahyušuvā ‘afterward the Lie became great in the country, both in Persia and in Media and in other provinces’; also DB 1.401, 1.48f, DSf 25f ikä avaniya aniyā XL ara- Santis baránà ата X X атаќаті bar snd ‘the rubble
3487:31 büjiya : avam : Bardiyam : avàja * уаба : Kabüjiya : Bardiyam : avaja : kürahy 32 à : пазу : azdà : abava : (уа : Bardiya : avajata : раѕауа : Kabijiya : Mudráyam 33 : akiyava : уада : Kabūjiya : Mudrayam : aSiyava : pasáva : kara : апка : abava 34 : pasava : drauga : dahyauvi : vasiy : abava : uta : Parsaiy : ша : Mádaiy : ut 35 d:aniy&uvà : dahyuSuvà ; 0àtiy : Dàrayavaus :х3йуайуа : pa
4447:3 ada : hya : Syátim : ada : martiyahyà : һуа 4 : XSavarSim : xSiyafiyam : akunaué : aivam : 5 parünàm : xSayatiyam : aivam : parünàm : fram 6 àtàram : adam : XSayarsa : xSayafiya : vazraka : 7 xšāyaðiya : хёйуайїуйпаш : x&ayafiya : dahy _ 8 ünàm : paruv : zanànàm : хёйуадіуа : ahyay 9 & : bümlyà : vazrakáyà : düraiy : apiy : Da 10 rayavahaus : x&ayafiyahyà : риса : Haxémanis П iya : 0atiy : Xšayāršā : xšāyaðiya : vasna : 12 Auramazdáhà : imam : duvarfim : visadahyum 13 : adam : akunavam : vasiy : aniyascly : naibam 14 : kartam : апа : Parsi : tya : adam : akunavam : 15 utamaiy : tya : рія : akunaus : tyapatiy : ka 16 riam : vainataly : парага : ava : visam : vaSnà : А 17 uramazdaha : akumà : Qatiy : Xšayāršā : 18 xSayafiya : mam : Auramazda : pātuv : utamai 19 y : xSacam : ut& : tya : manā : kartam : uta : tyamai 20 y : pica : kartam : avaseiy : Auramazda : patuv
5541:dahyu- sb. ‘land, province, district’: GAv. :
5542:daltyu-, LAv. dahyu- daiphu-, NPers. dih ‘village’, Skt. ddsyu- ‘stranger, demon’ (5124.2, $153.IV, $166). Decl., 5183.1. See also visadahyu-.
5543:dahyaus nsf. AmH 5, 8f (as Isf. §814b); DB 1.59; 2.28, 58, 59, 72; 3.9, 11, 20, 28, 66, 75, 79f; 5.4, 13f, 29f; DPd 6. dahydus-maty DB 4.39. dahyüum asf. (853, $72) AsH 8, 11, 13; DPd 15, 18; DNa 53. dahydvam (8124.VY) XPh 88, 58f. dahyaud (dahyuvd Wb.) isf. (M8, §124.2, 8137) DB 1.34.
5544:dahyàva прі. ($124.7) DB 1.18, 17, 18, 28, 41; 2.6°; 4.33; DPe 7, 14; РМа 17, 39; DSe 15f, 32f; DSm 5°; XPh 15. dahyáva apf. DB 1.21, 47, 67; 4.92, XPh 31,35. dahyünüm gpf. DB 1.2; DBa 3; DPa 4; DPe 3; DNa 10; DSb 6f; DSe 9°; DZb 2{°, DZc 5; DE 15; XPa 7f; XPb 15; XPc 7; XPd 10f; XPf 10; XPh 8f; XSc 2°, ХЕ 15; XV 111; А:Ра 11f°; A’Sc 3f; Wb 5; We 6; Wd 6. dahyüv- näm (523.11) РР} 2; DH 1f. dahyusued lpf. DB 1.35.
=== KNT visadahyu ===
1173:pIE *jono-, OP zana- ‘man’ with Med. г, Ау. zana-, Skt. jána-; m OP vispa-cana-, paru- canü-, and (restored month-name) Varka- 2010-; OP d is seen in *wsa-dana- *wispazana-', inferred from the Elamite mi-iš-ša-da-na.
1193:pIE *yikuo-, OP visa- ‘all’, also in visadahyu-; OP nspa- (with Med. sp) in vispaeana-; Av. vispa-, Skt. visva-.
1492:Other instances of z are largely the product of pIE ў and gh in Median ($88, $91), or in OP before consonants ($91, $95); such a 2 became s and then š before n: pIE 0: paruzana-, vispazana-, Varkazana-, vaz-
1770:-I- stems: Arakadri-, Küpisakàni-, Cicirri-, Cišpi-, Pütisuvüri-, Vispauzüti-.
1822:$150. Noun AND ADJECTIVE STEMS WITH SUF- FIX -ya- are a miscellaneous group. They include ai-va- ‘one’; adjective duru-va-, to verbal root dar-; adj. par-uva-; ethnic Par@a-va-, cf. Parsa-; yd-va-, to relative ya-; har-uva-; visa- and (Med.) vispa-, from pIE *yik-yo-; ji-va- ‘living’, unless the v is somehow radical (cf. §216). On Gau- baruva-, see Lex.:s.v.; on fem. aruva- as abstract, see Lex. s.v.
1916:а. The prior element is an adjectival modifier: paru-zana- ‘having many men’; vispa-zana- ‘hav-
2097:Gen. Pl. paruzandnam, vispazanünàm.
2157:Асе. Sg. Masc.: magum, zrafum, gidum; Dära- yava’um; Babirum, Margum; visadahyum; per- haps [agurum].
2178:'alogical to the nom.;? Av. daióhaom graphic for vam); but as second element of a compound we find -dahyum in visadahyum (or -dahyaum, as fum? is ambiguous), and in А?Ра 26 we have DHy"wm*, which may be either DHyaum or DHyum (Av. dahyiim is probably for -уйт). OP loc. dahyauvd is dahyau» like Babirauy, with added -4; but the diphthong is here kept before the added vowel (unlike дабай). Nom. pl. dahyàva has the long diphthong extended from the nom. sg, and represents pAr. -dvas (so also Av. daióhávo) ; this form was extended to serve as acc. pl. in OP (so also in Av.). OP gen. pl. dahyiiném and dahyüvnám is a regular gen. pl. of -u- stems in Aryan (Av. dahyunqm). ОР loc. pl. dahyusud is the -u- stem loe. pl. with ending -su, + the postposition -@; whether phonetically -u$usü or -u&a depends on whether the u of -su was con- sonantized before the added vowel, or retained by analogy ?
2244:I. Adjectives are found in all classes of stems, and the history of their case-forms has been in- cluded with that of the substantives. The com- monest type of adjectival stems ends in -o- for masc. and nt., with -d- for the fem.: nom. pIE -os -om -ü = OP -а? -am -à (§169-§176). The -- stems are skaub-iš -im -ai$, yäumainiš aydu(ma)inis, ušabārim; the -i- stems are acc. sg. yauldatim], probably yau[da"tim], to masc. yaudant-, and nom. pl. aBagainiya to masc. abagaina- (§§177-9]. The -й- stems are paru- (nt. paru», gen. pl. partinam), nom. sg. masc. uedmarsiyu-§ and ulzsnalu-s, ace. sg. masc. visadahyu-m (§§180-3). The consonantal stems are атійрат-, mana"wvin-, tauviyah-, hamap- tar-, hamdtar-, tunuva^t-, all in nom. sg. masc.: artavd, manauviš, taunyd, hamapità, tunuvà with acc. sg. tunuva"tam and gen. sg. tunwa*tahyd of -o- stem formation (§§184-8).
3638:95 ауага : hadé : kara : hyasaty : anu&ta : dha : ViSpauzáti$ : пата : уагда
3645:8 kāram : hamiciyam KT, without R18 уат between the words, 89 Г сўе legible, acc. to Cameron, séttling old disputes; [ujcSuam KT, -Feasma Jn., ucasma Wb., ucasam Kent Lg. 19.225-6; cašma Bv. TPS 1045.53-4, after Jn. IF 25.182-3 (cf. conj. of Spiegel, Altp. Keilinsch. 21n, 218), whence саат Kent; see Lex. s.v. caša-. 0-98 Except as noted, the supplements are those of WB and KT. * RI. records hya as visible before mand pila; but KT omit without comment, ** avahar{[+] KT; avahar- фа] Wb. ZDMG 61.726; avahar(ja] Tm. VS 1.22, Lex. 16, corrected to avahar{da] Tm. CS 21. % Vis[pa]uzia]ti $ KT; Vispjāvaušatiš Rl.; Vispauzati$ WB. " akunava WB; ajkunau[s KT.
4103:Tux Inscriptions or NaAQS-1-RugTAM. DNa = Darius, Nags-1-RustaMm A. 1 baga : vazraka : Auramazda : һуа : im 2 ām :bümtm :adà : hya : avam : asm 9 апат :adà : һуа : martiyam :adà : h 4 ya : Siyatim :adā : martiyahyà 5 :hya : D&rayavaum :xšāyaðiyam : ak 6 unau$ : aivam : parüvnàm : xSdyaé 7 iyam :aivam : parüvnàm : framátà 8 ram : adam : DarayavauS : xsayatiya : va 9 zraka : xSàyafiya : xSdyafiyanim 10 : xSdyaiya : dahyünàm : vispazaná 11 nam : х$йуайуа :abyáyà : шт ` 12 уа :уалаКауй : diiraiapiyf: Vistas 13 pahyà : puça : Haximanisiya : Parsa : P 14 àrsahyà : риса : Ariya : Ariya : ei 15 с̧а :0atiy : Darayavaus : xsaya 16 fiya : vašnā : Auramazdaha : ima : 17 dahyáva : {уй : adam : agarbáyam : 18 apataram : haeà : Ратѕа : adamsàm : 19 patiyaxSayaiy : manā : bàjim : abara 20 ha : tyasàm : hacdma :afahya :ava : a 21 kunava : dàtam : tya : mani : avadis : 22 adaraiya : Mada : Uvja : Parfava : Harai 23 va : Bàxtri$ : Suguda : Üvürazm 24 i$ : Zraka : Harauvatis : Gatagus : Ga 25 dara : Hidug : Saki : haumavargà : Sa 26 kā : tigraxaudà : Bābiruš : A 27 Gura : Arabàya : Mudràya : Armina
4214:DSe = Darius, Susa Е. 1 baga : vazraka : Auramazdà : hya : ima 2 т: bimim : adadé ; һуа : avam : as 3 татат : adadà : hya : martiyam : ad 4 ada : hya : &iyàülim : adad& : mart 5 iyahyü : hya : Darayavaum : XŠm : ak 6 unauš : айбат : parūvnām : XSm : a 7 шат : parüvnüm : framálàram : a 8 dam : Darayavaus : XS : vazraka : XS : XSy 9 anim : XS : dahyünám : vispazanü 10 nam : XS : ahyaya : bümiyà : vaz 11 rakàyà : düraiy : apiy : Vistas 12 pahyà : puça : HazamaniSya : Рат 13 sa : Pārsahyā : рисо : Ariya : Ari 14 ya : ciga : 08tiy : Dàrayavaus : XS : 15 уа&па : Auramazdaha : imá : dahy 16 āva : {уй : adam : agarbayam : apaia 17 ram : hacd : Parsa : adamsdm : pat 18 iyaxíayaty : manā : bajim : abara : 19 tyasam : hacéma : afahya : ava : aku 20 nava : datam : tya : mand : avadis : a 21 dáraya : Майа: Uja : Parðava : Haraiva : 22 Baatris : Suguda : Uvarazmis 23 : Zrdka : Наташайх : Bataguš : Maci 24 уй : Gadàra : Hidus : Зака : haumava 25 rgà : Saká : tigrazaudà : Babir 26 u$ : Авита : Arabéya : Мийгаа : 27 Armina : Katpatuka : Sparda : Yaun 28 à : аву : drayahya : ula : уа 29 y : paradraya : Skudra : Putayà : 30 Kuxiyd : Karka ; 6àtiy : Рата 31 yavau& : XS : vasiy : tya : duskarta 32 m : Gha : ava : naibam : akunavam : da 33 hyáva : ayauda : aniya : aniyam : 34 aja : ava : adam : akunavam : vašnā 39 : Auramazdaha : уаба : aniya : a 36 шуат : пау : jatiy : cind : gà 37 fava : kaSciy : astiy : дат : 38 tya : maná : haeá : avana : tarsat 39 y : улда : hya : tauviyd : tyam :s 40 kauéim : naiy : jatiy : naiy : vi 41 mardatiy : байу : Dérayavaus :
4401:5 XS : vazraka : XŠ : XSyanam : XŠ : dahyünám : vispazanünàm : XŠ : ahyay 6 à : bümiy& : vazrakáyà : düraiy : apiy : Vistáspahyá : puça : Ha
4447:3 ada : hya : Syátim : ada : martiyahyà : һуа 4 : XSavarSim : xSiyafiyam : akunaué : aivam : 5 parünàm : xSayatiyam : aivam : parünàm : fram 6 àtàram : adam : XSayarsa : xSayafiya : vazraka : 7 xšāyaðiya : хёйуайїуйпаш : x&ayafiya : dahy _ 8 ünàm : paruv : zanànàm : хёйуадіуа : ahyay 9 & : bümlyà : vazrakáyà : düraiy : apiy : Da 10 rayavahaus : x&ayafiyahyà : риса : Haxémanis П iya : 0atiy : Xšayāršā : xšāyaðiya : vasna : 12 Auramazdáhà : imam : duvarfim : visadahyum 13 : adam : akunavam : vasiy : aniyascly : naibam 14 : kartam : апа : Parsi : tya : adam : akunavam : 15 utamaiy : tya : рія : akunaus : tyapatiy : ka 16 riam : vainataly : парага : ava : visam : vaSnà : А 17 uramazdaha : akumà : Qatiy : Xšayāršā : 18 xSayafiya : mam : Auramazda : pātuv : utamai 19 y : xSacam : ut& : tya : manā : kartam : uta : tyamai 20 y : pica : kartam : avaseiy : Auramazda : patuv
5542:daltyu-, LAv. dahyu- daiphu-, NPers. dih ‘village’, Skt. ddsyu- ‘stranger, demon’ (5124.2, $153.IV, $166). Decl., 5183.1. See also visadahyu-.
```


## [2026-09-05T20:08:22.645Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT dahyu ===\" && grep -n -i \"dax́yu\\|dahyu\\|daiŋhu\\|dain.hu\\|daŋ\" BRT.txt | head -40",
 "description": "grep Bartholomae for dahyu"
}
```


### [2026-09-05T20:08:22.716Z] TOOL RESULT

```
=== BRT dahyu ===
3398:—  'i'a  nqma  ahmt  ahravai^ma  nama tthmi  YL/.'ia;  —  tum  »J  '>raom  (VS.) ^zaotaste  (sd.)  Vr.j,  7;  —  mal  avabyS daxitJbyS  yaha  -va  W. 13.22;  —  'va  paoi- rlm  aita  paita  frayantu  .  .  framra  V.  8. 19;  —  'vand  (NP.J  parstö.valanhs  Yt5. 91;  86';  —  'vanS  dahyunqm  YLij,i47;
4416:•  j.  an-äxätay  f.  'Unfriede':  vainJi  ahmt nmane  .  .  äxstis  "Um  Y,  60,  5 ;  —  iOm axsisis  'tSisÜa  mi>ra  xsayehe  dahyunqm Yt.  10.2  g.
4681:Abi.  des  Verglichenen:  dahyunqm  yh  'nyi räjöii  Y, tr),iZ;  — yastä  daeiJSng ..  masyqsls tarS.mqstä  °nyiiig  ahmätyS  hBt  arBm(sd.)  .. ". .  die  andern  (alle)  ausser  dem,  der  .  ." Y.45. II.  II)  'ein  anderer,  alius':  yB .  .  'inyeke  v3  srSvayantB  paitUtanH  (sd.) 'f^B  vä  hl  dakmB  srttta  (sd.)  gS^S  daoäiti N. 25;  61,  V. J.9  PUZ.J  —yB  ..  *'imm*^
5024:•  j.  ava.Jasan-  Adj.  "her-,  hinzukommend, gehend  zu  — '  (mit  a  und  Akk):  yasca.. frS.vS  iüsa  (NS.)  haca  daiähaot  °sa  dahyUm ä  Yt/.i?.
5539:•  '].  airya-,  p.  ariya-  1)  Adj.  (fem.  ya-) 'arisch':  'yanam  daRyunqm  . .  tüiryanam dahyunqm  Ytl  13.  i43';' 1°.  87',  5.49, 58,  117,  ig.  56,  69,  V,  ig.  39 ;  —  'yä  dai- tihavd  \i.8.jfi,  52%  58^;  —  'yäbyS  dai- tüulys  Yt.^. 61  \  10.4;  —    yäiyö  (statt
6579:7-531  3-  IS>  Yt. /4- 42;  —  »00  asti  vohu  yeAhe  afm(?)  h>nii  yeAhe  vaim  mahi  ysi mattS  mana  dami  Yt  i.  25;  V,  2j.  3  (?);  saosyants  dahyunqm  "dieses  Hauses  .  ., —  yat  arnAat  airiAä  samö  vX.ap5.t3m3mca  wozu  wir  gehören,  die.."  Vr.//.  13'*'; (sd.)  V.J.  15,  10.  18;  —  negirt:  ndit  mW  '^.4.  5(?);  —  yezi  darnyi  mäzriayasnsü i'xi  "ätihaiJim  {3D0PfA.)'J>  *pasu  vTra  nar»m  aahat  "wenn  der  Mann  der  mazd. "nicht  würde  es  mir  hier  Tiere  und  Men-  Religion  angehört"  Nik./;  2;  — pancanqm sehen  geben"  Yt /J,  la.  PPA.:  ta  nS  aktni  humatahe  ahmt  Y. /o,  16;  i6';  — qsoAu  /iaiS'^räyenteYl.13.1^6.  h)yaha  Skml''^''  räl^i/  (sd.)  yäsmüvatqm  Y. 2^,  11; appmjm  manivä  arshat  nivsitis  (sd.)  Y,  —  negirt;  pancanqm  noit  ahmi  duSmatahe jo.  16;    —  fravalayU  yi    paoirya    (sd.)  nsit    ahmi..    Y.  70.  16;  16'.  S.  noch
6582:airyanqm  dahyunqm  Ytjp.55;  10,  15, 22;  bereit    sein,    dienen    zum  Zweck    von  — '
7467:•  j.  äsu.asp5.'t9ma-  Adj.  'der  die  schnell- sten Rosse  hat':  vTsläsp}  ankam  dahyunqm ••t3m3  *bvat  Yt,5.98.
8644:I   j.    uz-daöhav-,    *uz-dahyav- '>    Adj. (auch  mask.)   'ausserhalb  des  Lands  be- findlich'; a)  'ausländisch':  ädahyunqmta .. 'yunqmüa  (GPm.)  frava^ayS  Y.  2O.  9,  Vr, 16.2.        b)  'ausser  Land  führend';  *xsa- yäe  . .  *'aÄua/  (lSm.)'>  pa^a  AaxlüiJ  {sd.) N.p. Pü.  (w  a):   »M'/i7^,  (lu  b):  /W  u-^/;hltrk.  — ')  NA.  u:diihy-',  s.  aber  J  i,  K  $,  K  7  a  und ädahy.  —  ')  Hd».  daauhulii,  %  löS.  30.
9307:*drußtn  \. 32.12;  —  nSit  urvä%ä  datsi-\     KompE.  —  PFP.  zum  V.  ^kar-.    —    ai  vgl fyas/tl  -fanB  vastrSt  arSm  (sd)  Y.5/.14;       *"':'■''■■  ^-T'-^""  ')  ^"^J-  ''  "■  "  ^""^  ^•"'■ —  ya  ..  'panjs  uropaynntl  yüca  . .  duh.- 1  •  j-  kaurva-  Adj.  'kahl,  unbehaart':  aspahe xiiihm    dahyunam    '^.4^.10;    —    »/a«^  U^-*^«  J^maA*  'j'a^^  YtÄ  21;  31'. iavayasc'-a  Y.^iT.'ii.  .)  im  jAw.  Name|     KompA.  "  -j- ^^;^-  Adj.  -zu  k.U,   »p.
10043:(Dat):  anairyanqm  tat  dahyutiqm  v?r3- "i'fäi  uzjasaiii  H.^S.
10098:meist  mit  mantan-  'menschlich'  verbun- den": 'am  F.  21;  —  'yeÄe  marii!tüS  .  . yS  paoiryS  ahuräi  mazääi  manasca  *gulta silsnifsca  yahmat  haca  fr^W3r?sai  näfö airyanqm  dahyunqm  Yt/_J.  87;  V.  2  j.  2, 2Ö.  5;  —  haca  "yJt  mari^nat  ä  saosyantäi Y.  26.  10;  —  'yehylcä  mnra>nö  \.  13. 7.  a)  neben  ^gav-  (III):  tams  gsui  .. 'yehe  Y.öVi'.aa;  Vr.2;.2;  — fravaiayS.. yqmca  gSui yqm^a  'yehe  Yt  13.86.  Vu- deutlich:  _j'ar«/o  "yehe  maraia"  F.  ^e", ')  Vgl.  Yt  IJ.  87:  "OJH.,  der  als  erster  des AhuraM.  Willen  und  Gebole  annahm,  aus  dem er  schnf  die  Familie  der  ariBchcn  Länder,  den Stamm  der  arischen  Länder".  GM.  ist  der  ersle. Saesyant  der  letzte  Mensch,  Y.  26.  10.  Vgl. noch  Bd.  24.  1,  j,  igff.,  31.  1,  10.  7;  s.  Justi NB.   108.
10827:•  ]•>  g-i  P-  xSä(y)-  V,  'vermögen'.  Praes. 3  jc/a-"  [,  25  ar/ayÄV],  2^  x^aya-,  'xsya-'''. i)  'Macht  haben,  Gewalt  haben,  herr- schen über  — ,  schalten,  verfügen  über  — , besitzen';  mit  a)  Gen.:  iüm  äxs'ieii'  ana- xitsiiia   .  .  xsayeke  dahyunqm  Yt.  10.  29;
10844:•  p.  xsäyaSiya-''  i)  Adj.  (fem.  'y3-)  'im Besitz  der  Herrschergewalt,  KönigswQrde, souverain' ;  Aa/ä  paruviyata  Ayä  amäxam tauml  yä  akc^  Bh. /.  3.  2I  m,  'Herr- scher, König' :  darayJ'v<^us  ya"  *'vazarka'' 'ya*  yanam  'ya"  pärsaiy  "yJ^  dahyUnam  \ Bh./.  I ;  —  darayaf'vi/'us  ya*  *vazarit/'  yc^ yanSm  'yt^  dakyünäm  yc^  ahyäyä  bumiyä D.i2;  j,  5.  I,  6.  2,  4,  16,  18,  ig,  X.  j,  2, 3  3,  5,  7-  3>  Am.  i,  2  '>,  3,  Ao.  /.  2  »_  K.  j, Bb-j.  i;  /.  2C,  2.  iff.,  j.  ifE,  4-1«:,  5. iff.,  D.4-  a,  3,  5-  3.  3.  6^,  3,  4,  s,  7,  J^, /7-3.  X.2.3,  3-3,  4-3,  S,  1.^,4,  7-3, Ao.  J.  3,4;  —  a'ur^mazdä..hycr  däraytr- vt^um    'yam    akiaaus   aivam  parHvnam
11071:Glieder  sind  verbal:  yBi  ztjvä  (nämL  hitOt) *ar»har3La  bvanticS{sA)\.4^.T.  3)bci allen;  a)  D  im  Ap.;  das  letzte  Mal  steht Uta  statt  cä:  pärsamcä  mädamcä  utä  aniyä dakyiivaf"  Bh.  /.  14.  b)  im  Aw,;  i)  die Glieder  sind  nominal ;  a)  sie  folgen  sich  un- mittelbar: nmänyasca  visyasca  santumasca Y.  if).  18  (s.  dazu  18  aA.);  —  aojasca  v»ty- 'inmca  j^armas^a  lavania  Y.  7/.  8 ;  —  sta- rasca  mäsca  >fe'<i/vi-'(7  YL72,25(s.dagegeni_j. 57);  —  vätftnca  vänmca  tnafy^mca  Jyau- humca  Yt  5.120; — hubprvtlmca  uslaMin- tlmca  vanta.bintTmca  Y.  61. 2  (s.  dagegen  7 ; Sp.  570U.);  —  maziUäsca  vahiitasca  srais- tas^a  asayS  Y.  52.  3;  —  apasca  urvaräsca xadirdsca  Y. A3;  —  asavafom  htnümca bavaniiinla  busyantimla  Yr.lS.i; — vTspayä ..slöis  haihyJica  bavqihyäica  büiyqi^yäica \.6S.i3i  —  nm3nanqmcä  vlsqm^a  satttu- nqmca  dahyunqmca  Y.  Ä  7 ;  —  damayä  anu- matayal'a  aiiuxtayaica  * aim.varstayai^a Y.Ä7;  —  d^aurunqscä  rä^aistiscä  väs- tryqscä  ßuyants  Y.  ig.  3;  Yt  ig.  8;  — ahamca  ratümca  paoirimca  tkaisim  Yt/^J. 152;  —  ha^ra  miiräca  rasnuta  uyraca dämSis  upamana  Yt/_J.  47;  —  vispss^a paiti  vansajls  vTspSsca  paiti  frasparrjJ i'JspSsca  paiti  fravaxsS  Y.  jo.  5 ; — haurva- tasca^  fiö  am)r>täta  gSuica  taSnB  gSusca urunS  ä%rasi-a  aoxtsjiämand  hadisasca  Vr. g.  5;  —  beim  Zahlwort:  navaia  navaittfca navaca  sota  navaca  Aazavra  navasSsca baivqn  Yl;_J.S9.  a)mitTmesis:*«ai/x
11327:I.  3)  'Geschlecht,  Stamm,  Nachkom-, menschaft':  gayeie{sA.)  inarti^nS .  .yakmal haca  /räiw^nsat  (näml.  ahurö)  najö  .  , 'nm  airyanqm  dahyunam  Yt.  i_j.  87;  — 'r>m  buyät  ahmya  nmilne  "Nachkommen- menschaft  soll  in  diesem  Haus  , ."  FrD. /;  —  °ra  F. ig.  a)  mit  Abi.:  at yss dasvä  . .  akät  (sd.)  manauhs  siä  °r?m  Y. 32.  z.  [!'D.6.2:  lies  ariyt^.cfii''a^.] KorapA-,  E.;    Ableit.  —  np.  fihr  'Ursprunß'.
12343:•  j.  tüirya-  Adj.  (fem.  'ya-)  'm  den TSrem  gehörig ,  ihnen  eigen'  (usw.): 'yanqm  dahyunqm  Yt  5.  54,  V.J.  42  PüZ., 5.  38  PüZ.;  —  airyanqm  dahyunqm  .  . 'yanqm  da^nqm..sairimanqm  dahyunqm Ytl3.  143;  143;  —  mairyS  'ryS franrase Yt /J.  56,  82;  5.  41;  —  mairxm  'rim franrasyämm  Yt().i8,  22,  ip.77;  Y.Jj.7.
12727:. .  santunamca  dahyunamca   .  .  zantusänS '/ans  (als"  AP.)  YL/j.'isi. Komp.:  dairiAa!'-'i-*'A/iii-.
13095:j,,  g.  dahyav-''  j  dahyu-^''  f  'Landgebiet, Landschaft,  Land',  oft  zugleich  auch  von den  Bewohnern;  a)  im  Aw.:  haraiti  bars .  .  hama  psirisäite  fräpayä  (sd.)  °rihus  ä upaola>ihvasca  Yt ig-\;  —  kahrkasS  .  . yS  naotnyä{sd.)cit  haca  'hihaot  .  .  xrUm aiwi.va&iaiti  Yt.  14.  33;  — par3  *S3mS  al- tanßta  *'iih3us^  anhat  b>rptd{s^)  7-i}sir?m V.  2. 24;  —  nSii  ..  asar?hal:a  /i^fyraf/a 33
13104:—  imUm  'hyilum  a*ur(^mazdä  pstuv  .  . abiy  imäm  'Ayäum  mä  Sjamiy!^ ..hain&Yi. 4.%;h.Q.i.a,{°hyum); —  mäm  a''urt^mazdä patitv  . .  utämaiy  vfiam  Uta  imäm  'Ayäum D.  6.  5;  —  kärc^  arikJ'  abav(^  ..draugt^ 'hyauvä  (LS.)  vasiy  abav<^  utä  pärsaty Uta  mädaiy  utä  aniyr^uvä  dahyuhiVä{zKi k) Bh. /.  10.  A)  in  vorwiegend  oder  aus- gesprochen politischem  Sinn;  I)  im  Ap.; I )  von  den  IVovinzen  (Satrapien)  •>  des  per- sischen Reichs:  imn  'hyäva'  tyä  manä  pa- tiyäi.ia"  (Sp.isi  m.)  vasnä  (^urJ'ntazdäha'' adamSäm  xsäyai  iyJ'  aAam :  pärsc^  ''wjajJ' hnbirus  . .  *Jraharavam  'hyäv<^  23  Bh./.6; 7,  8';  —  imä  'hyäva''  tyä  adam  *adar.<iy hadä   (sd.)    anä  pärsä   kärä  .  ..-   ''uvaja''
13122:j.  'dahyu'ma-,  "dähymna-'*  Adj.  'der I  Provinz,  dem  Land  an-,  zugehörig,  Land-': kaya  ratavS?  nmänyS  vlsyU  zantumS  'mB zardhuärö ptixlöY-ig-iB.  A)  m.Name der  Gottheit  der  Länder*':  "mtm/a  aia- vamm  asahe  ratam  G.3. 7 ;  —  'mähe  ra%wS 0.3.7;  —  uzayeirin^m  .  ,  frädaLvirtm 'trmnca  asavanim  Y.  2,  5;  —  laayeirinai .  .  ß-ädat.vTrai  'mäica  asaone  Y,  /.  5 ;  — ähurBiS  °mahe  Vr.  1. 9.
13581:•  j.  'daaba*  Adj.  (fem.  dähh)  bezeichnet ein  Volk  (und  dessen  Land),  'däkisch.'*^: airyanqm  dahyunqm  . .  dähinqm  dahywiqm narqm  asaonqm frava-ayö\\.l^.\\^;  144.
13991:•  p.    duvard-ay-    m.    Torhalle':    vaiiiä ^ur<^tnazdaka''  imam   °%im    visadahyutn    • (sd.)  adam  akunavam  X.  /,  3.
14909:•  j.  paiti.a'J^^a-  n.  'Wiederkunft,  Rück- kehr'; ahaun/namiä  "ä/v/n  ysi  *iyiyqm dural  aüfjsa  (sd.)  dahyunam  Y,  4^.  6  '>.
16669:haben?"    Y.  47.  5'';    —    vanäayalil   (sd.)        KompE.—  Et.?  Vgl.  Var.  6axr.   Bed.?    Das yqm    natdiitqm   gttl>am    dr?gi-i    baxsaitt       Wort ^steht^^wischen  .^ox/a- und  Wa-.- Pa.: ".  .   das    nachbarliche    Haus,    das    (jetzt  |       "     *       "^""^  ''' noch)  der  i>«^gläubige  (Fürst)  inne  hat"  j  •  p.  ba''da'ka-  Adj.  (fem.  'kä-')  'Untertan; Y.  s°-  3*' j  —  y^  *^  ■  ■  ftaema  . .  gava  \  Untertan,  Vasall':    imä   dahyuve^  tyä  .  .
17594:•  j.  fratsma'tat-  f.  'principatus,  Obrig- keit': mihrä  .  .  fra\ät  vJspi  'tatB  dahyu- nam  yaosaintTi'a{%A.)  rämayäti  Yty.  95; —  da^unam  äaifihupaitis  uta  dahyunam *'täii>'>  Yt/o.  18.
17821:yemi  , ,  imat  am>ia  spptita  .  .  imat  asäu- nqm  varguAls  °iays  (VP.)  Wjra  aiiuihüra Y.  65. 1 2 ;  Ny.  /.  I ;  —  aora  varmkis  upa.- sa^a  .  .  äps  .  .  urvarä  .  .  tüäunqm  fra- vasays  Yt  13. 147;  1. 9,  10. 100,  H.  34,  y, 79,  FrW. /.  3;  —  jamyqn  i^ra  asäunqm .  ,  'iaylf  asöis  basfaza  hacimnä  . .  istSe *vadhar»Aqm  paitiHätSe  ätaranqm  Y.  60. 4;  —  qpqmea  .  .  urvaranqmca  .  ,  asao- nqmla  'hnqm  yasnsm  Vr. 21.  \;  —  yS nä  his  hubinta  *barat  jva  a?aonqtn *says  (als  AP.)  sästa  .  .  hö  anhaiti  za- sulttmS  Yt  /J.  1 8 ;  —  fravasayS  .  .  yä a/raourvisvat  k?r»navainti  irsm  yahmya jaanti  Yt.  y.  26;  —  -says  . .  ya  ahurahe xsayats  dasinqm  upa  yü&yänti  yezi  aim bavaiti  ^alavaxsnuiW.  13. 63  ;  — frasüSTnii uyrä  asäunqm  'fayS  paoirij'  pouru^sata .  .  pouruAatanra  .  .  pouruiasvanS  apitii ashntnä  haväi  käcil  näfäi  . .  tä  yü^yeinti pfianähu  have  asahi  Yt  l^.  65if.;  —  "sayS .  .ya  avai  trayS  aiwyaxsayänti  yat  vouru- kahm  ..yä  ave  strjui  atwyäxsayeinti yqm ^haptöiringS  ..ya  avqm  k^hrpim  aiwyäxsa- yänti  yqm  .  .  hnsäspahe  .  .  ya  avqm *x^rqm  (sd)  aiwyäxSayänti  yqm . .  tara- 'huStrahe  navaca  navaitlsla  navaca  sota nava^a  hatattra  navasSs^a  baevqn  Yt  13. 59—62;  —  "iayS  .  .  yä  vts^&a  ävayänli hamaspa>:maedaim  paiti  ratüm  äat  a^ra vtcar?nii  dasa  pairi  xsa/nö  Yt/J.  49;  — asSunqmcä  'HbyS  yä  nS  iltä  urvSibys  Y. 5Ö.  2 ;  —  asäunqm  '/is  narqmcä  näiri- nqmcä  yazamaidl  Y.^7. 3;  —  °fayS  yä paeirya  (sd.)  anhan  Y.  23.  \;  —  äyeseyesti "vTspaya  asavane  'se"  Y,  2_j.  3;  —  vTspä °iayS  (als  AP.)  asäunqm  yazamaide  ädah- *yunqmca ..  'say5 ..*u%dahyunqmla . .  °iayS.. narqmca  ..'^ayD  ..näirinqmfa  ..  °sayS  yaza- maide  Vr.l6.  2;  7.  i,  10.2,  16.  i;  —  nabä- nazdiäanqm  para.iristanqm  aliirapaitinqm a!>iryanqm  narqm..näirinqm  'iayff  yaza- maide  Y.  26.  T,  8  ff.";  —  a/äunam  "sayd .  .  nmänyä  visya  zantumä  däAyumä  zara- ^ustrSJpmä  Y.  ly.  18;  —  airyanqm'  .  . /ßityanqm'  .  .  sairimanqm'  .  .  säininqm' . .  dahfnqm' . .  vTspanqm'  dakyunqm  narqm .  .  näirinqm  .  .  °sayö"  yasamaide  Yt  13. 143—145;  —  fä  'sayU  .  .  aoßstA  hittti  .  . ya  paoiryanqm  tkaihnam  ya  vä  narqm azätanqm  /rais.car>^rqM  saoiyantqm  Yt. y.i7;'Y./.i8',  23.2,  24.5;  —'  vjipä .  .  'Iay3  .  .  yä    haca   gayät    mariihnai   ä
18871:•  j.  nafah-  n.  'Verwandtschaft,  Familie': gayehe  (sd)  mar^hru}  . .  yaAmat  Aata  frä- ^wpTPsat  (näml.  aAurö  matda)  °/3'^  airya- nam  dahyunatn  Yt. /J.  87.
18929:'(tragen  sva.)  als  Träger,  Stütze  dienen für  — '  (Akk.):  ya^a  lia  väcim  näslma (iPOA.)  ya'ia  vä  saosyantd  dahyunam Y.70.4.
19211:1. 7.       2)  II  •s3y<^  nämc^  dahyuui  msäaiy "'■'  '       ""■  i"eine  Landschaft  namens  JVi  in  Medien"
19314:—  paiHp?r3nt  annm  mainyüm  hala  "na . .  Visa  . .  zatäu  . .  *daAku  V.  JO.  s  j  — paoiryqn  ihalü , .  'nanamüt  vTsqmia  zantu- nqmca  dahyunqmla  Ytfj,  150;  10.18,  Y. äV,  2j.  I.  a)j.  GS.  oderGP.  mit«Ma«Ä- patay-  (sd.""',  Stverz.)  und  nmanS.pa%ni- (sd.'"',  Stverz.) :  'nahe  nmanS.paitfm . .  'nahe nmanspahnlm  VT.3. a  £;  usw.  b)  j.,  g,  mit GS.  ^arff(sd."'',  Sp.  512  f.;' Stverz,),  vom Paradies:    'nl  garS  Y..,#5.8;  50.  4,  57. 15;
19348:•  j.  "nmänya-  Adj.  (fem.  'yä-)  Adj.  'zur Gottheit  Nmänya  gehörig,  mit  ihr  in  Be- ziehung stehend':  mihra..'ya  ratvSvTsya zantuma  dahyuma  zara%u^trB.t3ma  Yt  lO. "5;  —  fravasayS  -yä  vlsyi  ..Y.17.18.
19394:—  manS  J'ur<^tnasds  upasiam  baratuv . .  Uta  imam  dahySum  . .  pätuv  D.  4. 3 ;  — vas^i  (^urJ'mazdäkJ'  manacS  däray<^- vaAaui"D.4.2;  —  iya*  mana  kartam  utä fyc^maiy  /iS'ö*  kartam  X.7.4;  —  avam käram  .  .  hyj*  mana  naiy  gaubataiy*^ Eh.2. 6,  j,3,  14;  2.14.  zu  1  b):  J'urt^- masda  ya'ha  avaina*  imäm  bümim  *yau- d<rHm  (sd.)  pasüvt^dim  martä  fräbart^ mam  (s.  i  i  b)  . .  D.  61 4 ;  — pasavo^  dahyUui mana  abavJ'  Bh.j.  a,  4,  iz.  zu  3): kari^  hy<^  hamüi'iyc^  mana  naiy  gau- &ataiy*'>  Eh.  2.  7,  10.  b  n)  im  jAw.; zu  I  a):  Hat . ,  mana  asti  vjjaymift^m  . . attivam  asti  vJmamiiftim  Yt  /.  a;  — s.  noch  bei  a.  zu  1  b):  mana  raya  .  . pawasla  staorüta  upairi  tarn  vTcarmta Yt  5.  89;  /.  a6  (?).  zu  a):  ya%a  .  . Os  zaofff  mana  yat  ahurakt  matda  Yt ig.  8a;  V.  ig.  14;  —  ar»hu^  y3  mana yai  ahurahe  mazdä  P.  40;  —  zugleich zu  1  a):  manada  yatmm  yat  ahurahe mazda  a^rasca  P.Jp.  11)  schwach- tonige  Formen  stehen  a)  enklitisch i)  hinter  dem  ersten  Wort  des  Satz-  oder Versteils,  von  dem  sie  aber  a)  durch  ein andres  enklitisches  Wort  getrennt  sein können;  a)  hinter  einem  Praenomen; 3)  selten  in  anderer  Stellung;  b)  pro- klitisch5>;  das  hochbetonte  Wort,  an  das sie  sich  anschliessen,  hat  keine  bestimmte Stellung.  I)  Akk,;  a)  im  Ap.;  zu  a  1): avada  mam  cita  amanayJ"  Eh.  2. 6;  — y^a  mam  kame^  Bh.4.4;  D. ö. 4, 17-3)
20527:•  i-i  St  P-"  mi^ra-,  p.  "mitra-"'  m.  'Ver- trag, Abmachung,  Konliakt':  "rim  mä janyä  .  .  Mvaya  tT  asti  (Sp.  270  U.)  'rS drvataäa  asaona^a  Yt.  70.  a ;  —  laiti  aSe 'ra  tava  yat  ahurahe  masdsl  äat  mraot ahurS . .:  xsvas. .  vacaAind . .  sasf3.tnaräs . . pasu.mazS  .  .  staorö.mazB  .  .  vlrS.masS  .  . dai}ihu,mazS  V,  4L  2;  —  vacB paoirim  'nm karmaoiti  *zasts.maz3  alät  framansaiti *zastö.masö  atiät  antan  urvaitya^sA.)  /ra- daäiaiti  y.4-Z'i  —  Äaj'  agiO  'rB  aiwi- druxtö  ästäraili  yB  vacalünB  V.  4.5;  — yö  'nm  aiwt.druzaiti  ytm  vaeahimm  V, 4. 1 1 ;  —  s.  noch  Yt  10. 3,  45, 14. 47,  V. 4.  54  unter  A  n.  a)  im  gAw.  'reli- giöse Bindung,  Verpflichtung':  yS . .  drltä ayanUtn  urvätöis  (sd.)  vä  .  .  'rBibyS  vä \.46.  5.  A)  als  Gottheit*';  1)  im  Ap.: mSm  a'ura^maxdä  utä  °'^r<^  bage^  pätuv Ao.  /.  4;  —  J'urJ'mazdä''  ^anahitc^  utä "'trJ'  Am.4''i  i  i'>ra*).  II)  im  jAw. (yazata-) :  kö  'rtm  aiwi.drusaiti  ks  rasnüm paifijrinaxti  Yt  14-  47;  10.  45;  —  äsu.- aspim  dacäiH  'rö  .  .  ysi  'nm  nsit  aiwi.- druUnti  Yt  ro.  3 ;  —  rasnaoSca  paitLsanfam 'raheca  aiwi.drux/3m  (sd.)  V.  4. 54; — yai vä  dim  aiwLdrusaiti  . .  /rasa  upajcanda- yäti  'rB  grantB  upaJbUtB  Uta  nmämm  .  . Yt/0. 18;  19;  —  apa  HB  haca  azaaAat ,  .  'ra  barBis  anädruxtB  Yt  10.  23;  —  t^sa mainyete  dus:^ar3nä  nSit  vlsp?m  aiwi.- druxtse  'rB  vamaitt  apifma  Yt  70.105; — ■  satayus  antan  pitan  pu^rtmla  . .  asti 'rJYLio.  117;  116;  —  tOm  akB  vakUlasia 'ra  ahi  daiAhuby5..tBm  axstöii  anäxitBiita 'ra  xSayehe  dahyunqm  Yt70.  39;  29;  — tbiHahecil  axlnultahe  (sd.)  °ra  (IS.)  mata rämayeiti  huxsnüitlm  paiti  'rahe  , .  xsiiB- taAe^it  albiHahe  (sd.)  °ra  manB  yaozayäti ax/nßitlm  paiti  *raAeYtio.iog— 111;  120; —  'raAe  da&yunam  dai^hupatsU  Y.  /,  1 1 ; 2.  II,  Yt/0. 145,  75.35;  —  äea  nB  jamyät avahyäi  uyrB  aiwi'^Urd  ..'rB  ralva  dai^hu- paitii  Yt  10.  78;  —  'nm  aiwi.dahyüm  . . 'nm  antar».daRyüm  'rtm  ä.daRyäm  . .  Yt 10.  144;  144*;  —  ci>rä  'rahe/rayana  yasj tarn  da^Bm  slaraitt  ..  Yt  iO.  112;  — kaaa   nB   aria  gavai^im    apayst  paskst
20883:razunm  (sd.)  yS  mqm  mairyö  .  .  paiti pantata  "laqueum  (insidiatoris)  qui  me insidiator  ,,  oppugnavit"  Yt5.  so^J*;  — yö  ktnnavät  (Sp.  447  o.)  yim  yataite MÜrfm  .  .  albists  hyat  Yt.  10.  iio;  — fra paurvö vätqm  vazailt yqm<,^-ai.) pa>ö siti  haomö  ". .  (ad  vias)  quas  vias  .  ." Yt.  Ä33;  —  üvistayaica  ..  huframirtta- ya?ca  ysi  htnti  haoma  sura  "..(vinorum) quae  sunt  vina  .  ."  Vr.  (?.  3;  —  udiyasca rasvas^a  gatris  yailqmta  .  .  masyika  . gairinqm  nilmqm  ddhar>  "et  U.  et  R.  mons et  (alii  monte.s)  quorura  .  .  montium  . ." Yt.  IQ.  6.  c)  yS  NSm.  und  ySi  NPm. stehen,  ohne  Beziehung  zu  einem  Wort  des Übergeordneten  Satzes,  d)  im  Vorder- satz im  Sinn  von  'wenn  wer,  wenn  einer, wenn  man':  yp  kainTti?m  upäiti  .  .pührqm- {sd.)i^  hl  daoäili  mä  .  .  agsa  ya  kaine . . tarO  daxslsm  paraylt  (Sp.  152  u.)  V, /5. 9;  —  y5  ffiirikam  U^ravaittm  . .  xsudrä avi  fraiiharisaiti  hat  aiiihe  asti  paititis (sd.)  V.jtV.67f.;  —  y5  hl  *3p?r»ti3mnai (Sp.  869  o.)  nsil  visäiti  *främrUite  kö  .  . ai>!rapaitinqm\ea^  ..  astryäti  N.  j_j;  — yö  aiuä  bansma^a  */ra stürmte.. aoäi  anye . .  *framravainti  . .  vispaZiqmcd  arwi.snm- vaiti  (sd.)  vispe  ratufryB  N.  6b;  —  y5i pa'^a  utbartnte  spanaüa  irista  naraiM  . . hat  tä  päka  (sd.)  frayqn  .  .  "wenn  man desWegs  hinausträgt  tote  Hunde,.,  sollen  .. V.Ä14;  —  *ySi  dim  */rahincin  *antari ätar>m:a  bar>smaca  anairyanqm  tat  dahyu- nqm  v»r>hrili  uzjasaiti  N.  6(Vj  —  mit  der 1.  Plur.  im  Sinn  von  'wenn  wir,  unsereins': ySi  timäni  hqmiarämahi  (sd.)  . .  alrsmca .  .  aaf  pascaäa  . .  sps  vä  tiä  vä  iri^yat huha  ts  v»i-)^qn  aSe  ySi  mazdayasna  V. 5.39.  b)  im  Nachsatz  im  Sinn  von  'dass einer':  aya  daoia  disyJ/(sA.)ylf..  aiwy'ir?- hqm  (sd.)  nSii  aiwyästi  V.  18. 9.  ß)  adjek- tivisch: yaEca  ß«  narS  . .  Jason  brä^ra vä  haxaya  vH  .  .  yezi  laäS-cinanhö  jasqn .  hqm  ioa  iaSitm  hqm.bäray>n  "quique  . .  vin venerint,  (iis)  ,  ."  V.  4. 44.  Anhang
21020:��»■^r<T .  ./ra-iat  vapa  frahmatato  dahyunqm  |     _  pi^, .  ä/^^/p,  3p.)  „^  gü. :  ufJr<^mmra^.  - yaozainttiia  (nämL  daiiihui)   rämayäti,      1)  wie  mm  \.yaeg-;  1.  aber  ^aui-  No,  3. ".  .  und    di.    io    AulieguDg    gerMmden I     j  ,       j^^,,  __   j,^^  ^^^^  ^ (Provmen)  bmigt  er  zu,  Ruhe'  Yty-9S;  „ch  Pü.  ■Scbarmessei':    •«.&  Jära  «die —  iy»ra*™aö  ^«äa    orW    mJ»  Schneide  des  K"  F..<g. UUiim  piiuda-l,m'<  pailvMtm    monä       z,„  v.  ,«*«..  _  VeL»««»»,..  -   PS.. frsiarir  "ak .4^.  dieseErdein Auflegung [     oiiarai  (np.  wftmi).  —  ■)  So  K ;  M yeU:
21675:mit  ni  i)  'nieder-,  im  Zaume  hahen': apam  napä  . .  /ratät . .  JratsniatätS  dahyu- nqm  yaozainfllca  (näml,  dai^hüs)  nyasäite Yt.y.  95-  a)  festhalten':  narB,.käv5ya aasta  nyäsimnS  (statt  NP.,  näml.  barismd) y.  iff.  ig;  —  yesi  astat  nyäsänhe  yat ax^ar3t3m  (näml  ^ar^tiS)  Vtip.  48;  — tait  il  eis  aAha  drujS  nyasäite  "keiner soll  sich  von  der  Dr.  festhalten  lassen" FrW.6'.i(?).
22410:*)  Nach  mp.  Schriften  mit  AiDahik  identisch; vgl.  Mx.  j/.  24f. :  ahraman  e  sara%u!l  dräyitt  itt haiar  hal  in  din  . .  i  matdaymnän  aj>ik  itti än^äk  at  1000  säl  j^aläiJi  . .  dahem  Hgön  1/08070«« (geschr.  ntkann)»  dahyupeU  dahAk  dir.
23654:reicher Angriff,  Sieg':  aojasca  'rpmla  ifary- nasia  zavanca  Y.  yi.  8,  Yt.  /.  22;  — tanvB  vazdvan  .  ,  tativS  °r»m  Y,  Q8.  11; '(f*)'*;  —  fravasayB  .  .  ya  d3%rJl zbayente  Yt.  13.  2^;  —  anairyanqm tat  dahyunqm  'rsi  uz/asaiti  N,  6^;  Yt. to.zd,  A.  j.  8;  —  tfm  hacät  'nm  vlspO.- ayärfm  (sd.)  Ytij.  54;  —  atäril  'ra  Aa- ^aiie  Yt  14-  44;  5-  69,  ig.  54*;  —  'ra  v»r^ %ra7-ast>möYK.ig.Tq;  11.3,  i4.ii  —  *'ra F.S'K
24334:im  Gegensatz  zu  Haus,  Gau  und  Land*': *i  *sT  äfmän^m  *s>m  vä  sSi^nm  vä dahyam  vä  adat  duiiia(&±ya . .  Y.  j j.  1 8 —  /rasa  upa.scindayäti  mi^rS  .  .  ulc nmätum  uta  'spm  ula  zantam  ula  dahyBm Vt.io.  18;  87,  Y.62.S,  V.tV.  103,  N.^;  — ahmt  nmilne  .  .  ai^he  'si  ahmt  tantvö  .  . aiAhe  daitihvif  Y.  5.  z8;  Vr.  72.  5;  — *nmanyaca  •sya{\S.)ca  zantavala  *daiiha- vai'a  Vr.  J2.  5;  —  nmäne  .  .  'se  (LS.)*'  ■  ■ zantvö  .  .  dauhvö  N.  <?;  P.  77;  —  haca timänät  . .  'sat  .  .  zantaot  .  .  dai^haot  Y. 57.  14;  N.  5;  —  fradditsi  nmänaketa "sahica  (GS,)''  zantlusca  *daAh3usca  Yt. 5.6;  l0.l^,  18,  83,  Y./j.i,  Vr.j.2,  V. 7.41,  42,  p.37,  70.5,  Vytiö;  — /«///.- p3rme  ar)r?m  mainyBm  haca  iimäna  .  , 'sa  .  .  iantu  .  .  *daAhu  V.  70.  5 ;  —  /ra- ff mq  nmänanqmca  'sqmca  zaniunqm/a dahyunqmca  Y.  Ä  7;  27.  i,  Yt,  10,  18,  /j, 150;  —  apjm  aihmnä  Aaväi  kScU  nil/Ji (sd.)  hazayiti  'se(DS.)..zantave..*da^^ave Yt.  13. 66.  a)  GS.  oder  GP.  mit  vTs/c tay  (sd-9>; Stvcrz.):  nmänahe  nmäfW.patSe . . •ss  visfatse . .  Bau  ff u/  satiiupatSe . .  daiAhSiis daiiihupaße  Yt  70. 1 7 ;  usw.
```


## [2026-09-05T20:08:37.659Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nimport re\nfor i,p in enumerate(pages):\n    if 'dahyu- sb.' in p:\n        print('leaf(0-based)',i)\n        print(p[:3000])\n        break\nEOF",
 "description": "Find Kent dahyu leaf"
}
```


### [2026-09-05T20:08:39.464Z] TOOL RESULT

```
leaf(0-based) 214
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
-diy emphatic encl. particle: Av. zi, Skt. hi, Gk. encl. -xı in vai-xı ‘yes indeed’, of-xé ‘not at all’, pIE *ghi ($88, 5191.1). ufraštā-diy DB 4.69 (JAOS 35.351-2; no
```


## [2026-09-05T20:08:39.737Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'visadahyu-' in p and ('adj' in p or 'Adj' in p):\n        print('=== leaf(0-based)',i)\n        idx=p.find('visadahyu-')\n        print(p[max(0,idx-1500):idx+800])\n        print('...')\nEOF",
 "description": "Find Kent visadahyu entry"
}
```


### [2026-09-05T20:08:41.449Z] TOOL RESULT

```
=== leaf(0-based) 81
-à; gausáya is а like formation to gaušā. The i before the -à in usiyd is responsible for the glide -y-, which has spread to gaušāyā as а vowel-separator; the prior à m gauXiyü indicates that the -i- in usiyé also is long!
$190. Apsectives 1х OP have all their cus- tomary uses and forms. For those which are cardi- nal and ordinal numerals, see $204; for the semi-
1! Nom. hamiciya DB 2.93 is predicate to two singular masculine nouns, but is more probably plural than dual; ef. $259. ? The form karšā does not belong here, nor probably artá-cà brazmanty (if во normalized) nor tau- mani-Saty; on these words see the Lexicon s.vv. * On these forms, cf. Kent. Lg. 19.225;
66 | OLD PERSIAN
pronominal antya-, haruva-, һата, $203; for the
demonstrative and determinative adjectives,
which funetion also as pronouns, $199, $200, $202; for the relative, $198; for those which are par-
ticiples, 5239-244.
I. Adjectives are found in all classes of stems, and the history of their case-forms has been in- cluded with that of the substantives. The com- monest type of adjectival stems ends in -o- for masc. and nt., with -d- for the fem.: nom. pIE -os -om -ü = OP -а? -am -à (§169-§176). The -- stems are skaub-iš -im -ai$, yäumainiš aydu(ma)inis, ušabārim; the -i- stems are acc. sg. yauldatim], probably yau[da"tim], to masc. yaudant-, and nom. pl. aBagainiya to masc. abagaina- (§§177-9]. The -й- stems are paru- (nt. paru», gen. pl. partinam), nom. sg. masc. uedmarsiyu-§ and ulzsnalu-s, ace. sg. masc. visadahyu-m (§§180-3). The consonantal stems are атійрат-, mana"wvin-, tauviyah-, hamap- tar-, hamdtar-, tunuva^t-, all in nom. sg. masc.: artavd, manauviš, taunyd, hamapità, tunuvà with acc. sg. tunuva"tam and gen. sg. tunwa*tahyd of -o- stem formation (§§184-8).
II. The oldest comparison of adjectives was by the suffixes -jes-/-ios- for the comparative, -is-to- for the superlative; both added to the root rather than to the stem of the adjective in the positive degree. There are these examples in OP:
Comp. пет. 
...
=== leaf(0-based) 214
Hz. Ap! 136-8) nsn. as sb. ‘handiwork’, DSe 42.
Daha- adj. ‘Dahian’; pl., a province of the Persian Empire: АКК. da-a-an, Gk. Aaa (§76.V; Lg. 18.298; Hz. AMI 8.72). Dahà npm. XPh 26.
dahyu- sb. ‘land, province, district’: GAv. :
daltyu-, LAv. dahyu- daiphu-, NPers. dih ‘village’, Skt. ddsyu- ‘stranger, demon’ (5124.2, $153.IV, $166). Decl., 5183.1. See also visadahyu-.
dahyaus nsf. AmH 5, 8f (as Isf. §814b); DB 1.59; 2.28, 58, 59, 72; 3.9, 11, 20, 28, 66, 75, 79f; 5.4, 13f, 29f; DPd 6. dahydus-maty DB 4.39. dahyüum asf. (853, $72) AsH 8, 11, 13; DPd 15, 18; DNa 53. dahydvam (8124.VY) XPh 88, 58f. dahyaud (dahyuvd Wb.) isf. (M8, §124.2, 8137) DB 1.34.
dahyàva прі. ($124.7) DB 1.18, 17, 18, 28, 41; 2.6°; 4.33; DPe 7, 14; РМа 17, 39; DSe 15f, 32f; DSm 5°; XPh 15. dahyáva apf. DB 1.21, 47, 67; 4.92, XPh 31,35. dahyünüm gpf. DB 1.2; DBa 3; DPa 4; DPe 3; DNa 10; DSb 6f; DSe 9°; DZb 2{°, DZc 5; DE 15; XPa 7f; XPb 15; XPc 7; XPd 10f; XPf 10; XPh 8f; XSc 2°, ХЕ 15; XV 111; А:Ра 11f°; A’Sc 3f; Wb 5; We 6; Wd 6. dahyüv- näm (523.11) РР} 2; DH 1f. dahyusued lpf. DB 1.35.
DHum (842) asf. DSf 58; DSj 6°. DHyaum (553) А2Рә 26. -DHnám gpf. DSa 2; DSd 1; DSf 
...
```


## [2026-09-05T20:08:53.314Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nimport re\nfor i in range(208,222):\n    p=pages[i]\n    nums=re.findall(r'(?m)^\\s*(\\d{2,3})\\s*$', p)\n    heads=[l for l in p.split('\\n') if 'LEXICON' in l.upper() or re.match(r'^\\s*\\d{2,3}\\s',l)]\n    print(i, nums[:6], '|', p.strip().split('\\n')[0][:60])\nEOF",
 "description": "Find printed page numbers near Kent leaf 214"
}
```


### [2026-09-05T20:08:55.445Z] TOOL RESULT

```
208 ['185', '186'] | Skt. jū- ‘press for- ward, impel quickly, excite, promote’, 
209 [] | it (§76.V, 5148.1). Cf. Gray, AJP 58.67; Hz. Klio 8.51, AMI 
210 ['187'] | 1) XPh 23.
211 ['188'] | word of uncertain meaning, Sb 3.
212 ['189'] | fnu, Lt. јеси ‘made’, NEng. do, deed, pIE *dhe-. See also wa
213 [] | 5-6).
214 ['191'] | Hz. Ap! 136-8) nsn. as sb. ‘handiwork’, DSe 42.
215 [] | rada&a, duvaista-. dürau lsn. as adv. ‘afar, far away, far a
216 ['193'] | e 15; DZe 10. drayahya lsn. ($136, §251A; wrongly taken as g
217 [] | n üv-nara- (§142).
218 [] | with Justi, IFA 17.107, ‘Pasargadae’, from paisiyd- ‘writing
219 [] | ‘I pierce (as with a spit)’, Gt. faran ‘to travel’. рамо[т- 
220 [] | tem (530, $148.I, 6154.1), ef. Av. posana- ‘battle’, Skt. pf
221 ['197', '198'] | r-, Gk. rarnp, Lt. pater, Gt. fadar, pIE *poler- (863.11, 87
```


## [2026-09-05T20:09:03.893Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(226,245):\n    p=pages[i]\n    if 'visa' in p or 'vispa' in p or 'vi5a' in p:\n        nums=re.findall(r'(?m)^\\s*(\\d{2,3})\\s*$', p)\n        print('=== leaf',i, nums[:6])\n        for l in p.split('\\n'):\n            if re.search(r'v[il1]s[aā8]', l) and ('adj' in l or 'dahyu' in l or 'zana' in l or 'all' in l):\n                print('   ',l[:400])\nEOF",
 "description": "Find visadahyu entry page in Kent"
}
```


### [2026-09-05T20:09:05.638Z] TOOL RESULT

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 5, in <module>
IndexError: list index out of range
```


## [2026-09-05T20:09:09.776Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('nleaves',len(pages))\nfor i in range(220,len(pages)):\n    p=pages[i]\n    nums=re.findall(r'(?m)^\\s*(\\d{2,3})\\s*$', p)\n    hits=[l for l in p.split('\\n') if re.search(r'v[il1]s[aā8ä]-?\\s*(adj|dahyu)', l)]\n    if hits: print('=== leaf',i,nums[:6]); [print('   ',h[:500]) for h in hits]\nEOF",
 "description": "Find visadahyu entry in Kent lexicon"
}
```


### [2026-09-05T20:09:11.500Z] TOOL RESULT

```
nleaves 232
```


## [2026-09-05T20:09:15.403Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(220,232):\n    p=pages[i]\n    nums=re.findall(r'(?m)^\\s*(\\d{2,3})\\s*$', p)\n    print('=== leaf',i,nums[:8],'|',p.strip().split('\\n')[0][:70])\n    for l in p.split('\\n'):\n        if 'dahyu' in l or 'visa' in l.lower():\n            print('    >',l[:400])\nEOF",
 "description": "Scan Kent last leaves for visadahyu"
}
```


### [2026-09-05T20:09:17.080Z] TOOL RESULT

```
=== leaf 220 [] | tem (530, $148.I, 6154.1), ef. Av. posana- ‘battle’, Skt. pfiana- ‘bat
=== leaf 221 ['197', '198'] | r-, Gk. rarnp, Lt. pater, Gt. fadar, pIE *poler- (863.11, 875.1, 576.1
=== leaf 222 [] | -. — fra&aram asn. XPf 26f, 37.
=== leaf 223 [] | 1; DSe 1°; DSE 1°; D8s 1^; DSt 1; рле 1°; DE 1; XPa 1; XPb 1; XPc 1; X
=== leaf 224 [] | 2; 4.66. abara imf. ($40, $84, 5228.) DB 1.25, 55, 88, 94; 2.25, 34f, 
=== leaf 225 ['201'] | BUyà Isf. DSd 2°; DSf 7, 15, 16, 18, 24^; DSg 2; DSi 2, 4; DS) 1°; DSy
=== leaf 226 [] | 24; 3.70; DPd 1; DPh 9; DSf9; DSp 1°; DH 7; XE 2; XV if; АНе1. [ma8]ji
=== leaf 227 [] | ion), Lt. mort-uos (after vi-vos ‘liv- ing), pIE *mrios ($80, $109, $1
=== leaf 228 ['204'] | so a province of the Persian Empire, ‘Egypt’; тазе. sg. as sb., ‘Egypt
=== leaf 229 [] | d sg. opt. mid. ($223.II, $284.1I) XPh 50. yadiyaiša” (8220, 5228.11, 
=== leaf 230 ['206'] | am. rak-qa-an, АКК. ra-ga-’, Gk. ‘Payys, now Rai near Teheran. kagä ns
=== leaf 231 [] | 1); -vā .. -vä ‘either... or...’: Av. và, Skt. và, pIE *ue, ef. Lt. -v
```


## [2026-09-05T20:09:21.139Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(pages[231][-4000:])\nEOF",
 "description": "Print end of Kent file"
}
```


### [2026-09-05T20:09:23.052Z] TOOL RESULT

```
1); -vā .. -vä ‘either... or...’: Av. và, Skt. và, pIE *ue, ef. Lt. -ve.  z$apa-ü rawca-paíi-a DB 1.20. hya-»à DB 4.68. imai-vä DB 4.71, 78, 77. yadi- vä DNb 25, 29.
vaina- present stem of vb. ‘see (mid.) seem’: Av. vaéna-, NPers. bindd, Skt. véda ‘knows’, vinddte ‘finds’, Lt. videt ‘sees’, videtur ‘seems’; pAr. *uaid- na-, plr. *yaina- ($69, 588.1, $130, $210.III; Reichelt, Aw. Ер. $157). See also Vidafarnah-. vainümiy lst sg. (4226.1) DNb 36, 36f, 39, 40. avaina imf. DB 2.76, 90; DNa 32. vainataiy mid. as pass. (8235.1) DNb 2; XPa 16. vaináhy 2d sg. subj. ($37, $222.11, $227.1) DB 4.70, 73, 77; DNb 29. vaindtiy subj. ($222.11) DS} 5°. vainātaiy subj. mid. as pass. ($222.П) DNb 35.
vau- adj. ‘good’ ($11, §153.1); nt. as sb. ‘the good, (religious) goodness’: Av. nsm. vaphus, nsn. vohu, Skt. nsm. vásuş, nsn. vdsu, pIE *yesu-; in Dérayavau-, Vaumisa-, Vahauka-, Vahyazdata-.
Va'umisa- sb. ‘Vaumisa’, a Persian officer of Darius: Elam. ma-u-mi-i8-8a, АКК. ti-mi-is-st, Gk. (Plutarch) Rutens; cpd. of vatu- and mifra- ‘friend’ (849c, $78, $148.ILD): ‘Friend of the Good’ §160.- Ib; cf. MB Gr. $51). Vaumisa nsm. DB 2.49, 51, 62. Vaumisam asm. DB 2.53, 58.
vaz$- vb. ‘grow’, see (Луах${та-.
Waj- vb. ‘be strong’: Skt. vaj-, бјаз- ‘strength’, Av. aof
```


## [2026-09-05T20:09:32.069Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1910,1925p' KNT.txt",
 "description": "Kent compound section context"
}
```


### [2026-09-05T20:09:32.113Z] TOOL RESULT

```
A*ura-mazdah- ‘Ahuramazda’, lit. ‘Lord Wise"; cf. ~ Lex. s.v.
$161. PossEssivE Apsecrives, often differing from the preceding only by a shift of accent which ean be observed in aecented Sanskrit, words, but cannot be determined in OP or Avestan.
I. Determinative compounds (cf. 8160.1); the OP examples are all names of persons or of places or of months:
a. Accusative: Aspa-canah- ‘Having love of horses’; Baga-yadi- ‘(Month) marked by the wor- ship of the bagas’.
b. Genitive: Arta-xéaga- ‘Having a kingdom of justice’; Aršāma- (from *aría-ama-) ‘Having the might of a hero’; Haxd-manis- ‘Having the mind of a friend’; Garma-pada- ‘(Month) having the place of heat’; Asa-garta- (Тапа) having caves of stone’. :
П. Descriptive compounds (cf. $160.IT.):
а. The prior element is an adjectival modifier: paru-zana- ‘having many men’; vispa-zana- ‘hav-
ing all (kinds of) men’; v1sa-dahyu- ‘containing
all lands’; hama-pitar- ‘having the same father’; ha-matar- ‘having the same mother’; tigra- zauda- "wearing pointed caps’; wéd-marsiyu-
‘having one’s own death’ (see Lex.). Ariya-ciça- "Having Aryan lineage’; Ardu-manz&-
‘Having an upright mind’; Tarma-spdda- ‘Hav-
ing à brave army’; Vahyaz-data- Following the
better law’; Vistdspa- from *višta-aspa- (see
Lex. s.v.) ‘Having ready horses’; @ata-qu-
‘(Land) having hundreds of cattle’ (but see
Lex. s.v.); @ira-vahara- '(Month) having vigor-
```


## [2026-09-05T20:09:32.514Z] TOOL CALL #21: Bash

```json
{
 "command": "sed -n 1,60p tools/ref_page.py",
 "description": "Inspect ref_page tool"
}
```


### [2026-09-05T20:09:32.550Z] TOOL RESULT

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


## [2026-09-05T20:09:44.223Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('SYN.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\n# leaf = printed + 24\nfor pr in (1301,1302,1303):\n    i=pr+24\n    print('==== printed',pr,'leaf',i)\n    print(pages[i][:2500])\nEOF",
 "description": "Buck p.1302 village section"
}
```


### [2026-09-05T20:09:46.023Z] TOOL RESULT

```
==== printed 1301 leaf 1325
_ soileir, lair OHG = zoraht Av. Gidra- VW. goleu, eglur MHG _ klar Br. _ sklaer NHG klar, deutlich
‘Clear, plain’ (to the mind, opposite of ‘obscure’; as in NE a clear statement, the meaning is plain) is generally ex- pressed by words for visually ‘clear, bright’ (15.57), most of them still used in the latter sense. Less common rela- tions are with words for ‘level, plain’, ‘open’, and ‘point out, explain’.
Several of the words listed cover also evident, manifest, obvious’, but others in which this related but eoate a et dif- erent sense is dominant, like NE evident, re offenbar, are not included. te ‘eile Hom. béedos, orig.
plcuous’, as once in Hom.
and reg. in 4
aL SNe? apl-eyr ‘seem’, Sict, di- ‘shine’. ae Brig 168,
‘ cans (in Hom. only ad
A only adv. cada ay ) , tym. dub. Boisacq 855.
he *epris, in Hom. ‘visible, palpa-
lat ? ter a ‘clea amesg a ‘clear’, with sb. evapyera
: déapar
Walde-P. 1.772.
bright? 4pyhs, a&pyés  ‘shinin ma Sa. yrduna- ‘ight, white’, ate, » Bo Grk, aveabe-« isacq 74,
visible, manifest’, in
NG the usual word for ‘evident, clear’ (to the mind) : ¢datyw ‘bring to light, show’, etc., datvouat ‘appear, seem’, Skt. bha- ‘shine’, etc. (15.56, 17.18).
2. Lat. clarus (> It. chiaro, Fr. clair, Sp. claro, Rum. clar), also ‘bright’ (15.57), orig. ‘loud’ (15.45).
Lat. planus ‘level, flat’ (12.71), freq. ‘plain, clear’ (Plaut.+), with adv. plané ‘plainly, clearly’.
Lat. apertus, lit. ‘open’, pple. of ape- rire ‘open’ (12.24), cf. NHG offenbar ‘evident, obvious’.
Lat. évidéns (> It., Sp. evidente, Fr. évident, ME, NE evident, but these mostly ‘obvious, not requiring proof’), orig. of things ‘visible, apparent’, used from Cic. on for Grk. évapyns, cpd. of @ ‘from’ and vidéns, pple. of vidér
==== printed 1302 leaf 1326
e ‘see’ (cf. NHG aus-sehen ‘appear’). Ernout- M. 312.
Lat. perspicuus, orig. ‘transparent’, fr. perspicere ‘see through’.
3. Ir. follus (fr. *wpo-luksu-) ‘bright’ (15.57).
Ir. rail, prob. back-formation to vb.
: so-lus
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
1234 SELECTED INDO-EUROPEAN SYNONYMS
rélaim ‘reveal’, this fr. Lat. re-vélare ‘uncover, reveal’. Walde-P. 2.366. Pokorny, KZ 46.152 f.
NI. léir, more usually, cpd. soiléir (with ameliorative prefix so-), fr. Ir. léir ‘visible’, etym. dub. Walde-P. 2.381.
W. goleu, orig. ‘bright’ (15.57).
W. eglur, etym.?
Br. sklaer, orig. ‘bright’ (15.57).
4, Goth. skeirs = ON skirr ‘clear, bright, pure’, OE scir ‘bright, glittering, clear’ : ON sk@rr ‘bright’ (15.57).
ON skirr, beside skijra ‘explain’, skyring ‘explanation’, fr. a root *skeu-, *ski- beside *skai-, *ski- in preceding group, but otherwise appearing mostly in words for ‘cover’, ‘grow dusk’, etc. For similar peculiar semantic relations in the other formal group, cf. Grk. oxé ‘shade’. Falk-Torp 1008, 1040.
Goth. bairhis ‘bright’ (15.57), also ‘clear, manifest’ (bairht patet = 69dov dre 1 Cor. 15.27).
Goth. swikunfs, cpd. of swi- : swes ‘own’ (cf. OE swutol, below) and -kunps ‘known’ (: kunnan ‘know’), lit. ‘self- known’. Feist 468.
OE swutol (Anglian sweotol), ME sutel, etym. dub., perh. epd., first part : Goth. swi- in swikunps (above) and last part fr. *tal : Grk. 590s (above, 1). “Walde-
_ P. 1.772. Holthausen, IF 20.321.
ME cler, NE clear, fr. OFr. clair (above, 2).
ME pleyn, NE plain, fr. OFr. plain, Lat. planus (above, 2).
Du. klaar (MLG klar > Dan., Sw.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
klar), MHG klar, NHG klar. tp cldrus (above, 2), Mar, fr. Lat,
OHG zoraht, zorft = OF torht ‘sple did, bright, beautiful’ : Ir. an-drocht es neg.) ‘offensive, dark’, fr. the root of Grk. dépxopuar ‘see’, ete. Walde-P. 1.807
NHG deuttich (MHG diutliche adv,), Du. duidelijk, Dan. tydelig, Sw. tydlig, derivs. of NHG deuten (MHG diuien)
; vuten), Du. duiden, Dan. tyde ‘explain, intey- pret’ (cf. NHG bedeutung, etc, ‘mean- ing’, 17.38).
5. Lith. aigkus, beside OLith. ighus prob. : ChSl. jasno, etc. (below). Walde- P. 1.2. Berneker 276.
Lett. skaidrs (Lith. skaidrus ‘fair, clear’ of weather, etc.) : ChSl. ésiz ‘clean’, ON heidr, OHG heitar ‘clear, bright’ (sky, weather, etc.), Skt. ketu- ‘splendor, brightness, sign, mark’, Av. &ibra- ‘apparent, clear’ (below). Walde- 12 P
==== printed 1303 leaf 1327
 pple. of vi-a7ij- ‘make appear, reveal’, orig. ‘beautify, adorn’, epd. of afij- ‘anoint’. Cf. BR 1.77.
Av: Gi6ra~: Lett. skaidrs, ete. (above, 5).
i ' |
f : ' ' '
fo
‘d.
| !
Digitized by Arya Samaj Foundation Chennai and eGangotri
MIND, THOUGHT 1235
17.35 OBSCURE
gaghs, &5ndos, Goth Lith. neaiikus Gk. 4 ST obs ON — myrkr Lett.  neskaidrs G goadns; oxoretvos Dan. dunkel ChSI. rh N t, _ obsctirus Sw. dunkel SCr. nejasan Tal oscuro OE _forsworcen, deorc(?) Boh.  nejasny It. obscur ME _ derk, merke, obscur Pol.  —_ niejasny 4 obscuro NE _ obscure Russ. nejasnyj at obscur Du. duister Skt. (gudha-) " dorche, dorchaide OHG = tunchal Av. ‘View nh doiléir, dorcha MHG tunkel V * aneglur NHG  dunkel, unklar pr _disklaer
‘Obscure’ (to the mind) is expressed py words for visually ‘dark, devoid of light? (cf. ‘darkness’ 1.62 and ‘dark’ in color 15.63), or by neg. epds. of words for lear, plain’ (17.34).
1. Grk., NG lit. acagqs, and Grk. &6y- dos, neg. cpds. of cadis and 870s ‘clear, plain’.
Grk. cxorewwés, lit. ‘dark’.
9. Lat. obsctirus (whence Romance forms), lit. ‘dark’.
3. Ir. dorche, whence dorchaide, lit. ‘dark’.
Nir. doiléir, neg. (do-) of léir ‘clear’.
W. aneglur, neg. of eglur ‘clear’.
Br. disklaer, neg. of sklaer ‘clear’.
4, ON myrkr, ME merke, lit. ‘dark’ (OE mirce ‘dark, wicked’).
OE forsworcen (the usual gloss for lat. obsciirus, but quotable in fig. sense?), pple. of forsweorcen ‘darken, make obscure’, intensive epd. of sweorcan
17.36 SECRET (adj.)
‘become dark, troubled’ = OS swerkan ‘grow dark, cloudy’, OHG giswerc, gi- sworc ‘darkening (by clouds)’, etym. dub. Walde-P. 2.535.
OE deorc ‘dark’, apparently not quot- able in fig. sense, ME derk, NE dark (a dark saying, but not common in this sense). NED s.v. dark, 6.
ME obscur, NE obscure, fr. OFr. obscur (Lat. obsciirus, above, 2).
Du. duister, lit. ‘dark’.
OHG tunchal, MHG tunkel, NHG dunkel (> Dan., Sw. dunkel), lit. ‘dark’.
NHG unklar, neg. of klar ‘clear’.
5. Lith. neaigkus, Lett. neskazdrs, negs. of Lith. aiskus, Lett. skaidrs ‘clear’.
6. SCr. nejasan, etc., general Slavic, negs. of the corresponding words for ‘clear’, SCr. gasan, etc.
7. Skt. gidha-, lit. ‘hidden, secret’ (17.36).
NG Kpurrés, Nabpatos Goth. fulgins Lith. slaptas, pasléptas Lat Kpudos ON leyndr, leyniligr Lett.  slepens, sleps *  occultus, secrétus, Dan. hemmelig (Ignlig) ChSl.  tajinit It clandestinus Sw. hemlig (lénnlig) SCr. tajan Re arelo OE diegel (déagol), dierne Boh. tajny Sp, Secret ME _ secre(t), derne, dizel Pol. tajny es NE
```


## [2026-09-05T20:09:52.439Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"19\\.16\\|VILLAGE\" SYN.txt | head -20",
 "description": "Find Buck VILLAGE section"
}
```


### [2026-09-05T20:09:52.488Z] TOOL RESULT

```
11557:NIr. baile ‘town, village’ (19.16), also ‘home’, as in ag baile ‘at home’.
32693:19.11 Country (“European Countries”) 19.44 Free (adj.) 19.12 Onn’s Native Country 19.45 Commanp, ORDER (vbs.) 19.13 Country vs. Town 19:46 Osry 19.14 Rucion, TERRITORY 19.47 Ler, Permir 19.15 Curry, Town 19.48 ComPEL 19.16 VILLAGE 19.51 Frrenp 19.17 BounDaRyY 19.52 ENemy 19.21 PropriE (Populace) 19.53 ComPANIon 19.22 A Propize, Nation 19.54 NEIGHBOR 19.23 Tripn, Cxuan, Famity (in Wide | 19.55 Srrancser Sense) 19.56 GuEsT 19.31 RuE (vb.), Govern 19.57 Host 1932 Kane 19.58 Ht, Ar (vbs.) 19.33 QuEEN 19.59 Htiyper, PREVENT 19.34 EMPEROR 19.61 Custom 19.85 PRrIncE 19.352 Note on Other Titles of Nobility 19.62 Srarex, QUARRED 19.36 Noszz (sb.), NoBLEMAN 19.63 Puor, Conspiracy 19.37 CrrizEN 19.64 Common (adj.) 19.38 Susszct (sb.) 19.65 Musr (vb.) 19.41 Master 19.71 Note on Terms for Members of a 19.42 Suave Trade or Profession 19.48 Servant 19.72 Wor, ProstiTuTE 19.11 COUNTRY (“European Countries’’) Gtk.  xépa, yf, x0dv Goth. land Lith.  kraStas, Zemé NG —_x:pa, rémos ON land Lett.  zeme Lat. — finés, terra Dan. land ChSl. strana, zemlja It. paese Sw. land SCr. zemlja Fr. pays OE land Boh.  zemé Sp. pats ME land, contree Pol. _ziemia Rum. ard NE country, land Russ. strana I. ltr, crich Du. land Skt.  dega-, vigaya-, jana- Nir. tir OHG lant pada- W. — gwlad MHG lant Av.  dai#hu-, OPers. dah- Br. bro NHG land yu-
32762:4. Goth. weihsa and once haimés ren- der &ypot ‘country’ as contrasted to baurgs ‘rods’ (Lk. 8.34, etc. weihsa; Mk. 5.14 haimés), pls. of weihs, haims ‘xan, Village’ (19.16).
32765:5. Lith. sddzius and kaimas ‘village’ (19.16), both used also for ‘country’ vs. ‘town’ (cf. Senn, Lit. Sprachl.).
32768:6. ChSI. sela (renders éypot Mk. 5.14, Lk. 8.34), pl. of selo ‘field’ (8.12), SCr. selo ‘village’ (19.16) and ‘country’.
32774:Pol. wies ‘village’ (19.16), also ‘coun- try’ vs. ‘town’.
32775:Russ. derevnja ‘small village, hamlet’ (19.16), also ‘country’ vs. ‘town’.
32856:Fr. ville, fr. Lat. villa ‘country house, farm’, late ‘village’ : vicus ‘village’, etc. (19.16). Walde-P. 1.231. Ernout-M. 1103. REW 9330. Gamillscheg 891.
32863:Dan. by = ON byr ‘town, village, farm’, Sw. by ‘village’, etc. (19.16) : Dan., Sw. bo, ON bia, Goth. bauan ‘dwell’ (7.11). Walde-P. 2.142. Falk- Torp 120.
32880:Av. vis-, used of the Mazdayasnian villages or towns (no actual cities), see under ‘village’ (19.16).
32884:19.16 VILLAGE
33826:2. Lat. vicinus (VLat. *vectnus > Romance forms), deriv. of vicus ‘quarter, street’ and ‘village’ (19.16). Ernout-M. 1103. REW 9312.
33833:5. Lith. kaimynas, Lett. kaimin’§ : Lith. kaimas ‘village, country’, kiemas ‘court, farmyard’, Lett. ciems ‘village’, etc. (19.16). Miihl.-Endz. 2.133.
33891:4, Lett. viesis, fem. viesn’a = Lith. viesné ‘female guest’; cf. also vbs. Lith. vieséit, Lett. viesuot ‘be on a visit, be a guest’ : Lith. vies-pats ‘Lord, sovereign’, Goth. weihs, Lat. vicus ‘village’, etc. (19.16). Miihl.-Endz. 4.669 f. Walde- Peat,
33892:Lett. ciemin’§s, fr. ciems ‘village’ (19.16). Cf. ciema tet ‘go on a visit’, like NHG dial. ze dorfe gehen (Grimm 2.1277). Miuhl.-Endz. 1.393, 394.
34322:7. Skt. vegya-, deriv. of veca- ‘house, dwelling’ and esp. ‘house of ill fame, brothel’ (: vic- ‘dwelling, house’, Lat. vicus ‘village’, etc. 19.16).
```


## [2026-09-05T20:09:55.568Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '32884,32960p' SYN.txt",
 "description": "Buck 19.16 VILLAGE text"
}
```


### [2026-09-05T20:09:55.620Z] TOOL RESULT

```
19.16 VILLAGE
Grk.  ké&pn Goth. haims, weiths Lith. kaimas, sodzius NG xpd ON porp, byr Lett. sdadza, ciems Lat.  vicus Dan. landsby ChSl.  vtst It. villaggio Sv. b SCr. _ selo Fr. village OE wic, tin, borp Boh. ves Sp. pueblo, aldea ME village, toun, thorp, Pol. wes : Rum. sat wike Russ. _selo, dereunja Ir. baile (fich) NE village Skt. grama- NIr. baile Du. dorp Av. vis- W. pentref OHG dorf, wich Br. kertadenn MHG dorf
NHG dorf
Words for ‘village’ are based on the notions of ‘dwelling place’ (whence the modest ‘village’, only rarely the ‘town, city’) or ‘field, piece of land’, ‘settle- ment’, etc. A few are connected with words for ‘people’ or ‘multitude’, that is, denoted first the group of inhabitants. Only rarely are they derivatives of words for ‘city, town’ (Fr. village, etc.).
1. Grk. xan, etym. dub. Walde-P. 1.360, 389. Boisacq 544.
Grk. xwpiov ‘place’, also ‘landed prop- erty, estate’, Byz. and NG (xwp.d) ‘vil- lage’, dim. of xépa ‘place, country’ (19,11).
2. Lat. vicus (>Ir. fich, OE wie, OHG wich), Goth. weths, ChSl. visi, Boh. ves, Pol. wieS : Grk. olfkos (sotkos) ‘house’, Skt. vi¢- ‘dwelling place, house’, Av. vis- ‘dwelling place, house, family’, also ‘village’ (Barth. 1456). Lat. vicus is also in part ‘quarter, street’. Walde- P. 1.213. Ermout-M. 1103.
Lat. castellum ‘fortress’ was often used in the Vulgate to render x&yn, hence OF castel in the Gospels and later. Cf. NED s.v. castle.
Fr. village, Prov. villatge (> It. villag- gio, Sp. villaje), derivs. of Fr. ville, Prov. villa ‘city’ (19.15). REW 9330.
Sp. pueblo ‘people’ (19.21) and ‘vil- lage’.
Sp. aldea, fr. Arab. daica ‘piece of land’. REW 2460.
Rum. sat, fr. Alb. fshat id., fr. late Lat. fossatum ‘place surrounded by a moat’ (cf. Byz. ¢occarov ‘camp, army’), deriv. of fossa ‘ditch’. REW 3461. Tiktin 1370. Densusianu 353, 355.
3. Ir. fich (gl. municipium), fr. Lat. vicus (above, 2).
Ir. baile ‘place, town, village’ (K. Meyer, Contrib. 166), NIr. ‘town, vil- lage, home’, and esp. baile beag, lit. ‘little town’, or sraidbhaile, lit. ‘street- town’ (‘village of one street’) vs. baile mor ‘large town’, etym.? Walde-P. 2.141,
W. tref (also ‘homestead’; in NT reg. for ���village’ vs. dinas ‘city’), now esp. pentref (cpd. with pen ‘head’), fr. OW itreb ‘dwelling’ : Ir. atreba ‘habitat’, Umbr. trebeit ‘versatur’, OF porp, OHG dorf ‘village’, etc. Walde-P. 1.757.
Br. keriadenn, dim. of ker ‘city, town’ (19.15), prob. in imitation of Fr. village vs. ville.
4. Goth. haims = ON heimr ‘home, world’, OF ham, OHG heim ‘home’, etc. (7.122), orig. ‘dwelling, resting place’, fr. the root in Grk. xetuar, Skt. ¢7- ‘lie’. Walde-P. 1.259f. Feist 283f. Cf. OE hamel, hamelet (> NE hamlet), dim. of ham, fr. MLG hamm of this group.
Goth. weihs, OE wic, ME wike, OHG wich, see Lat. vicus (above, 2).
ON orp, OE forp, prop, ME thorp, throp, Du. dorp, OHG-NHG dorf =
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
TERRITORIAL, SOCIAL, AND POLITICAL DIVISIONS 1311
Goth. paurp ‘cultivated land, field’ : W. irof, ete. (above, 3).. Falk-Torp 1274. Feist 492.
ON bgr (ber) ‘town, village, farm’ (> OE by, retained in place names Derby, Whitby, etc.; cf. NED s.v. by sb.), Sw. by, Dan. landsby (epd. with land ‘coun- try’; Dan. by ‘city’), orig. ‘dwelling place’ : Goth. bauan, ON baa, etc. ‘dwell’ (7.11). Falk-Torp 120. Hell- quist 115.
OE tin (often renders Lat. vicus), ME toun, and NE town (still locally for what is no more than a village), see un- der ‘city, town’ (19.15).
MB, NE village, fr. OF r. village, vilage (above, 2).
5. Lith. sodzius, Lett. sadza, orig. ‘settlement’ : sodintt ‘set, plant’, ChSl. saditi ‘plant’, Goth. satjan ‘set’, etc. Miuhl.-Endz. 3.801.
Lith. kaimas (beside kiemas ‘court, farmyard’), OPruss. caymis, Lett. ciems, either cognate with (but with West IE guttural) or loanwords fr. the Gmc. group, Goth. haims, etc. (above, 4). Walde-P. 1.360. Miihl.-Endz. 1.394.
6. ChSl. vist, Boh. ves, Pol. wies, see Lat. vicus (above, 2).
SCr., Russ. selo (Pol. sioto obs.) = Ch8&l. selo ‘field’ (8.12).
Russ. derevnja (‘small village, ham- let’, also ‘landed property’, dial. ‘piece of cultivated land’) : Lith. dirva, Lett. druva ‘field’ (8.12). Berneker 186.
7. Skt. gradma-, also ‘community, multitude, troop’ : Slavic gramada ‘heap, mass, multitude’, Lat. gremium ‘lap, bosom’, fr. the root in Grk. dyeipw ‘col- lect, assemble’. Walde-P. 1.591. Uh- lenbeck 83. Berneker 345.
Av. vis-, see Lat. vicus (above, 2).
19.17, BOUNDARY
Grk. — 8pos, Sptov Goth. marka Lith. stena (rubezius, riba)
NG obvopov, dptov ON landam@ri Lett. ruobeZa
Lat. finis, limes Dan. grense ChSl. prédéli
It. Srontiera, confine Sw. grans SCr.  granica
Fy. frontitre, limite OE (ge)m@re, mearc Boh. hranice
Sp. frontera, limite, lin- ME mere, mark, bonde, Pol. granica dero Srounter Russ. granica (rubez)
Rum. hotar, frontiera, mar- NE © boundary, frontier Skt. _ sim@-, stman- gine (border) Av. karana-
Ir. crich Du. grens
NIv. _ teora, crich OHG marcha
W. terfyn, fin MHG marke, grenice
Br. harzou (pl.) NHG © grenze
Most of the words listed are generic for ‘boundary’, covering that between countries and that between lands. But Some are used only or mainly for the former, as Lat. finis (hence pl. finés country’) and the group represented by NE Srontier; some for the latter, as Lat. limes. There are connections with words for ‘end, edge, front, wall’. Several de- Noted originally some: particular physi- cal form of boundary, such as a stake, a
furrow, a blazed trail, etc. There are some loanwords, introduced through contact with adjacent countries.
1. Grk. épos (on. odpes, Arg., Cret. &pos, Corcyr. dpros), spiov, perh. (Att.¢ not orig.) as orig. ‘furrow’ : Lat. wrvwm ‘curved part of a plow’, urvare ‘mark the boundary with a plow’. Walde-P. 2.352. Boisacq 716. Hence adj. ctvo- pos ‘neighboring’, NG _ sb.  civopopv ‘boundary’ (octvopa usual word for the
CC-O0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
1312 SELECTED INDO-EUROPEAN SYNONYMS
‘frontiers’, 8p.a for boundaries between pieces of land).
2. Lat. finis, prob. as orig. ‘fixed mark’ : figere ‘fix’. Walde-P. 1.832. Ernout-M. 363. Walde-H. 1.503. Hence adj. confinis ‘neighboring’, sb. confine (> It. confine, Sp. conjin, etc.).
Lat. limes, -ttis, orig. a path between fields, hence ‘boundary’ (but still mostly between lands, not countries) : limen ‘threshold’, limus ‘sidelong’, etc. Walde- P. 1.158. Ernout-M. 551. Hence It., Fr., Sp. limite (Rum. limitd neolog. fr. Fr.), mostly in secondary uses but also in pl. for ‘boundaries’ of countries; hence also the vb. limitare ‘fix the boundaries’ > Sp. lindar id. with sb. lindero ‘bound- ary’ (between lands).
It. frontiera, Fr. frontiére (> ME frounter, NE frontier, now mostly of the border region; Rum. frontiera, neolog., Sp. frontera), all used only of the bound- ary or boundary region between coun- tries (not between farms, etc.), deriv. of It. fronte, Fr. front, etc., orig. ‘forehead’ (4.205), but here through the secondary ‘front’. REW 3533. NED s.v. frontier.
Rum. hotar, fr. Hung. hatdr id. Den- susianu 1.374 f.
Rum. margine ‘edge’ (12.353), used also for ‘boundary’. Tiktin 953.
Rum. granitd, fr. Slavic, SCr. granica, etc. (below, 6).
3. Ir. crich : Lat. cernere ‘separate, distinguish’, cribrum ‘sieve’, Grk. xptvw ‘separate, distinguish, decide’, ete. Walde-P. 2.584. Pedersen 2.33.
NI. teora, W. terfyn, fr. Lat. terminus ‘bound, end’. Pedersen 1,241, Loth, Mots lat. 211.
W. fin, fr. Lat. finis. Loth. Mots lat. 168.
Br. harzou, pl. of harz ‘obstacle’ and ‘boundary stone’ (cf. Ernault 8.V.), etym.? Henry 158.
4. Goth. marka, OE mearc, ME mark,
OHG marcha, MHG marke : Lat. margo ‘edge’, Ir. mruig, bruig ‘cultivated land, district’, Av. maraza- ‘borderland’ (Barth. 1153; NPers. marz ‘borderland, district’).
The sense of the Gmc. words passed into that of the ‘borderland’ (hence ON mork ‘forest’), as in the borrowed OFr. marches (> ME, NE marches), also ‘dis- trict’, etc. Walde-P. 2.283 f. Feist 347. NED s.v. mark, sb.t.
ON landa-mé@ri, OE (ge)mére, ME (and NE dial.) mere, MDu. mére, orig. the (boundary) ‘stake’, fr. Gmc. *mairia- : Lat. mirus, old moiros ‘wall’, moenia ‘walls’, Skt. mi- ‘fix, build’, ete. Walde- P, 2.239 f. Franck, KZ 37.120 ff. NED S.v. mere, sb.?.
ME bordure, NE border, fr. OF r. bor- dure, deriv., through vb., of bord ‘edge’ (12.353). NED s.v.
ME bonde, NE bound, whence bound- ary (now the most distinctive word), fr. OFr. bodne, bonde, etc. (source also of Fr. borne > NE bourne), MLat. butina, bodina, etc., orig. perh. Celtic(?). NED s.v. bound, sb. REW 1235. Wart- burg 1.465 f.
MHG grenice, NHG grenze (> Du. grens, Dan. grense, Sw. grdns), fr. Pol., Russ. granica (below, 6), and first ap- pearing in the adjacent land of the Ger- man Order. Weigand-H. 1.765. Kluge- G. 216.
5. Lith. stena ‘wall’ (7.27) and ‘boundary’ (now the preferred- word, Senn).
Lith. rubeZius (the usual old word, NT, Kurschat, etc.), Lett. ruobedza, fr. Russ. rubeZ ‘boundary’ (below, 5). Miuhl.-Endz. 3.575. SkardZius 192.
Lith. riba, prob. orig. a clearing or track in the woods where the light shines through : ribéti ‘shine’, raibas ‘spotted’. Buga, Kalba ir Senové 20 f.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
TERRITORIAL, SOCIAL, AND POLITICAL DIVISIONS 1313
6. ChSl. prédéli (reg. for dpiov, in Gospels, Supr., etc.) epd. of délié ‘part’ with pré- ‘through, out, over’, hence lit. “he outer parts’. Berneker 195.
SCr., Pol., Russ. granica, Boh. hrani- ca, deriv. of word seen in ChSl. grant ‘chapter’, Russ. gran’ ‘facet, side’, Boh. hrana ‘edge’ (12.353), etc. Berneker 346. Briickner 155.
```


## [2026-09-05T20:10:03.600Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '32694,32790p' SYN.txt",
 "description": "Buck 19.11 COUNTRY body"
}
```


### [2026-09-05T20:10:03.649Z] TOOL RESULT

```
A ‘Country’ is intended here as the ter- Titory of a whole people or nation (“Eu- Topean countries”), though the words are used also in a more general sense for
The majority are the same as words for ‘land’, but a few are from ‘bound- aries’ or other sources.
1. Words for ‘land’ already discussed
in 1.21, 1301
areas of indeterminate extent.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
1302
Grk. yi, x0év (poet.); Lat. terra, Rum. tard; Ir. tir; Goth. land, etc., general Gme. (in NE now replaced in common use by country); Lith. zemé (formerly so used), Lett. zeme; ChSl. zemlja (reg. for yj including ‘country’, but strana for xépa), SCr. zemlja, Boh. zemé, Pol. ziemia (Russ. zemlja formerly so used, but mostly strana).
2. Grk. xwpa, also ‘space, place’ like xpos, both orig. ‘empty space’ : xfjpos ‘bereft’, Skt. ha- ‘leave’, etc. Walde-P. 1.543. NG xdpa, lit. ‘country’, pop. ‘town’ (19.15).
Grk. zéros ‘place’ (12.11), ‘region’, NG pop. also ‘country’.
3. Lat. fanés, lit. ‘boundaries, limits’, pl. of finis ‘limit, border’ and temporal ‘end’ (14.26).
It. paese, Fr. pays (> Sp. pats), fr. VLat. pagénsis, deriv. of pagus ‘coun- try district’ (19.14). REW 6145. Ga- millscheg 679.
4, Ir. crich (beside more usual #2r), see under ‘region’ (19.14).
W. gulad : Br. glad ‘wealth, fortune’, Ir. flaith ‘ruler’, etc., fr. the root in Ir. foln- ‘rule’, Lat. valére ‘be strong’, OF wealdan, etc. ‘rule’ (19.31). Walde-P. 1.219. Pedersen 1.157.
Br. bro, also ‘region’ as W. bro, see 19.14.
5. ME contree, NE country, fr. OFr. cuntrée, contrée (now mostly ‘country’ in
Digitized by Arya Samaj Foundation Chennai and eGangotri °
SELECTED INDO-EUROPEAN SYNONYMS
more general sense), fr. VLat. contrata (regio), lit. ‘(region) opposite’, deriv. of contra ‘against, opposite’. RIEW 2187 NED s.v. country.
6. Lith. krastas (now more usual than Zemé for ‘country’; cf. Hermann, Lit.- Deutsches Gesprichsb. 22, 36), also ‘re- gion’ and (more orig.) ‘side, edge, shore’ = Lett. krasts ‘shore’, etym. dub. Miihl.-Endz. 2.260.
7. Chl. strana (reg. for xépa), Russ. strana (ChSI. form) = SCr., Boh. strana, Pol. strona, Russ. storona ‘side’ (12.36).
8. Skt. dega-, also ‘region’, lit. ‘direc- tion’ : dic- ‘show, point out’. Uhlen- beck 130.
Skt. visaya-, also ‘territory, realm, kingdom’, as orig. ‘sphere of influence’ : vis- ‘be active’, outside root connections dub. Uhlenbeck 289. Whitney, Roots 161.
Skt. janapada-, cpd. of jana- ‘race’ and pada- ‘station, abode’ (lit. ‘step’ : pad- ‘foot’).
Av. daishu-, dah'yu-, OPers. dahyu- (in OPers. used of the great provinces and also of regions within them; MPers. deh ‘country’, NPers. dih ‘village’), prob. = Skt. dasyu-, the designation of the pre-Aryan inhabitants of India (orig. fnhabitants of the country’?), root con- nections dub. Barth. 706 ff. Uhlenbeck 123.
19.12 ONE’S NATIVE COUNTRY
Grk. xarpls Goth. gabaurps, land Lith.  tevyneé NG marplba ON  fosirjerd (-land) Lett.  tévija, téevzeme Lat. patria Dan. fedreland (fosterland) ChSl. oftétsivtje It. patria Sw. fddernesland, fosterland SCr.  domovina, otaéasivo Fr. _patrie OE éel (éfelland, fa- Boh. vast, oftina Sp. _ patria derépel), eard Pol.  ojezyzna Rum. patrie ME coniree Russ. rodina, otetesivo Ir. atharde, atharthir NE country, fatherland Skt.  svadeca- NIv. tir dhithchais Du. vaderland Wa cigitlad OHG fateruodil Br. §_mamuro MUG vaterheim, vaterland
NHG vaterland
CC-O0. In Public Domain. Gurukul Kangri Collection, Haridwar
TERRITORIAL, SOCIAL, AND POLITICAL DIVISIONS
The notion of ‘one’s native country’ may be expressed by the regular words for ‘country’ with appropriate context, asin NE my country, die for one’s country, which (rather than fatherland, native country, etc.) carry the emotional value of Fr. patrie, NHG vaterland, etc. Where words for ‘country’ are repeated in this list, a similar context is, of course, to be understood.
But in most of the IE languages there are special terms. These are most com- monly derivs. or epds. of the words for ‘father’, possibly, but not necessarily, reflecting semantic borrowing from the Greek zarpis. Much less commonly from words for ‘mother’. Terms lie NE mother country or motherland, though quotable in this sense, are used mainly to denote the relation of a country to its colonies or the home of certain products, etc.
Others are derived from words for ‘home’, ‘birth’, ‘race, family’, and (through ‘possession’) ‘power’.
1. Derivs. or epds. of words for ‘father’ (2.35).
Grk. rarpis (also rarpa, Hom. razp7), NG rarpiéa; Lat. patria (> Romance words); Ir. atharde, atharthir (K. Meyer, Contrib. 144); OE federépel, OHG fateruodil, NE fatherland, NHG vater- land, Dan. fedreland, etc. (see - list); Lith. tévyné, Lett. tévija, téevzeme; ChSl. otieistvije (reg. for rarpis), SCr. otaéasivo, otadzbina, Boh. otéina, Pol. ojczyzna, Russ. otecesivo.
2. NIr. tir dhiithchais, i.e. tir ‘coun- try’ with gen. sg. of MIr., NIr. dathchas
Digitized by Arya Samaj Foundation Chennai and eGangotri
1303
‘inheritance, one’s homeland or country’ (cf. MIr. jfirduchus ‘true native coun- try’), deriv. of MIr. dithaig ‘belonging to, fitting’, NIr. duthaigh ‘estate, land, region’ (19.14).
W. guwlad ‘country’ (19.11) and ‘na- tive country’ (cf. gwladgar ‘patriotic’).
Br. mamvro, cpd. of mamm ‘mother’ and bro ‘country’.
3. Goth. gabaurps ‘birth’, hence as ‘birthplace’ for warpis (Mk. 6.4, Lk. 4.23, 24; but in landa seinamma = els Tv warpida abrod Mk. 6.1).
ON fostrjoré and fostrland, Dan. (arch. or poet.), Sw. fosterland, epds. of fosir ‘fostering’ and words for ‘land’.
OE @fel, eel (freq. for patria in Gos- pels), also éelland and federépel (= OHG fateruodil so used by Tat.) = ON ddal, OHG uodal, uodil inherited ‘estate, patrimony’ (as OE @pel also), with strong grade of root in ON adal ‘nature’, OE efele ‘noble’, OHG adal ‘noble de- scent, nobility’ (NHG adel), etc., prob. : Goth. atta ‘father’, etc. Walde-P. 1.44. Falk-Torp 787, 1480, 1524.
OE eard (for patria in Mt. 13.54, 57, Aelfric, etc.), but mostly more general ‘region’ (19.14).
4. SCr. domovina, fr. dom ‘house, home’ (7.12).
Boh. vlast = ChSl. vlasté ‘power’, Pol. wlosé ‘landed property’, Russ. volost’ ‘district’, fr. the root of ChSI. vlada, vlastt ‘rule’ (19.31). Brickner 625 f.
Russ. rodina, fr. rod ‘descent, race, family’ (19.28).
5. Skt. svadeca-, epd. of sva- ‘own’ and deca- ‘country’.
CC-O0. In Public Domain. Gurukul Kangri Collection, Haridwar
CC-O0. In Public Domain. Gurukul Kangri Collection, Haridwar |
Digitized by Arya Samaj Foundation Chennai and eGangotri
SELECTED INDO-EUROPEAN SYNONYMS
19.13 COUNTRY
(vs. Town) Grk. dypol, xapa Goth. weihsa, haimés Lith. sodzius, kaimas NG oxy ON nd Lett. lauki Lat. ris, agrz Dan. land ChSl.  sela It. campagna Sw. land SCr. _ selo Fy. campagne OE land Boh. _venkov Sp. campo ME land, feeld Pol. wies Rum. {ard NE country Russ. derevnja Ir. Sees Du. land Nir.  tuath OHG lant W. gulad MHG lant Br. maez, ploue NHG land
Many of the words for ‘country’ as listed in 19.11 are used also for ‘country’ vs. ‘city, town’, as NE in the country, NHG auf dem lande, etc. Otherwise this is expressed by words for ‘field’ (often in plural) or derivs. of these, words cognate with others for ‘space’, some for ‘village’, and in a few cases by terms reflecting the notion of ‘outside’.
1. Grk. aypés ‘field’ (8.12), also ‘coun- try’ in this sense, esp. pl. &ypoi (but also sg. Hom.).
Grk. xwpa ‘country’ (19.11), some- times also in this sense.
NG éfox7, in class. Grk. ‘prominence, protuberance’ (so in lit. NG, also kar’ éfoxnv ‘par excellence, especially’), late also ‘extremity’, whence ‘remote place’ and so ‘country’ vs. ‘town’ (els rip éfoxnv ‘in the country’). Koraes, “Araxra 4.2.630.
2. Lat. ris : Av. ravah- ‘space, free- dom’, Goth., OE rim, etc. ‘space, room’, ChSl. ravinii, rovini ‘level’. Walde-P. 2.356 f. Ernout-M. 879.
Lat. ager ‘field’ (8.12), also ‘country’ in this sense, esp. pl. agrz. Cf. Lat. pagus ‘country district’ and the derivs. for ‘country’ (19.11), these also often ‘country’ vs. town, hence words for ‘peasant’.
It. campagna (> Fr. campagne), OF r. champaigne, etc., fr. MLat. campania
(cf. Lat. Campania), fem. of MLat. cam- panius, -eus, deriv. adj. fr. Lat. campus ‘plain, field’ (1.23), whence Sp. campo also ‘country’ vs. ‘town’. REW 1557, Ernout-M. 140.
Rum. {ard ‘country’ (19.11), also in this sense.
3. NI. tuath ‘territory, region’ and ‘country’ vs. ‘town’ (Dinneen), fr. Ir. tuath ‘people, notion’ (19.22).
W. gwlad ‘country’ (19.11), also in this sense,
Br. maez ‘plain, field’ (1.23), also ‘country’ vs. ‘town’.
Br. plowe, formerly ‘parish, commu- nity’ (= W. plwyf), fr. Lat. plébés ‘the common people’ (cf. 19.21). Loth, Mots lat. 196.
4. Goth. weihsa and once haimés ren- der &ypot ‘country’ as contrasted to baurgs ‘rods’ (Lk. 8.34, etc. weihsa; Mk. 5.14 haimés), pls. of weihs, haims ‘xan, Village’ (19.16).
ON, OE land, etc. ‘country’ (19.11), also in this sense general Gmc., except Goth. and NE.
ME feeld ‘field’ (8.12), also ‘country’ vs. ‘town’ (NE field obs. or arch. in this sense; NED s.y. 2).
5. Lith. sddzius and kaimas ‘village’ (19.16), both used also for ‘country’ vs. ‘town’ (cf. Senn, Lit. Sprachl.).
Digitized by Arya Samaj Found
Lett. lauki, pl. of lauks ‘open coun- try, field’ : Lith. laukas ‘field’ (8.12).
6. ChSI. sela (renders éypot Mk. 5.14, Lk. 8.34), pl. of selo ‘field’ (8.12), SCr. selo ‘village’ (19.16) and ‘country’.
Boh. venkov (cf. venek ‘the outside,
TERRITORIAL, SOCIAL, AND POLITICAL DIVISIONS
ation Chennai and eGangotri
1305
country place’), fr. ven ‘out’ = Russ. von, SCr. van, ChSl. viini id.
Pol. wies ‘village’ (19.16), also ‘coun- try’ vs. ‘town’.
Russ. derevnja ‘small village, hamlet’ (19.16), also ‘country’ vs. ‘town’.
19.14 REGION, TERRITORY
Grk.  xwpa, Téros Goth. gawi Lith. Salis, kraSias NG xwpa, Témos, pEpos ON herad, sveit Lett. vidus, mala, puse Lat.  regid, tractus, terri- Dan.  egn, omraade, gebed ChSl. strana
lorium Sw. trakt, omrdde, gebit SCr. kraj, predjel, oblast It. regione, territorio OE eard, land(scipe) Boh. kraj(ina), obvod, Fr. région, territoire, en- ME coniree, regioun, erd oblast
droit NE region, territory Pol. kraina, obwéd Sp. region, territorio Du. streek, gebied Russ. kraj, strana, oblast’ Rum. regiune, finut OHG _ lant(scaf), gawi Skt.  dega-, vigaya-, etc. Ir. crich, mruig MHG _gegende, lantschaft, Av. daithu-, zantu- NIr. duthaigh, ceanntar gGu(we) W. ardal, bro, tiriogaeth NHG  gegend, gebiet, land- Br. bro schaft
It is intended to group together here 2. Lat. regid, lit. ‘a direction, a
the most important of the words that denote an area of indeterminate extent and may serve for various areas inter- mediate between the whole ‘country’ and the ‘city, town’. Most of the words for ‘country’ (19.11) are used also in a more general sense, and some of them are-repeated in this list. Many of the words listed may have a more special technical application in certain periods or contexts, but no strict classification according to larger or smaller scope is feasible. A great number of others that are mainly technical terms for adminis- trative divisions, ‘province, district, canton, parish’, etc., are omitted.
The words are based mainly on vari- ous spatial notions, as ‘place, side, part, extent, line’ and especially ‘boundary’, but several on the notion of possession or rule (‘domain’), as NHG gebiet, etc.
1’ Grk. xépa ‘space, place, country’ (19.11), also ‘region’.
_Grk. rémos ‘place’ (12.11), also ‘re- glon’,
NG uépos ‘part’ (13.23), pop. ‘region’.
(straight) line’, whence ‘boundary line’, and so ‘region, territory’ (hence It. re- gione, etc.) : regere ‘direct, rule’, etc. Ernout-M. 857.
Lat. tractus, lit. ‘a drawing out, ex- tent’, whence ‘extent or stretch of land, tract, region’ : trahere ‘draw’. Ernout- M. 1051.
Lat. territérium (> It. territorio, etc.), deriv. of terra ‘land, country’ (1.21, 19.11). Ernout-M. 1034.
Lat. pagus ‘country district, rural canton’, orig. ‘boundary fixed in the ground’ : pangere ‘fix’. Walde-P. 2.2. Ernout-M. 722 f.
Fr. endroit ‘place’ and ‘region’, orig. ‘right side’, fr. en droit. Gamillscheg 359.
```


## [2026-09-05T20:10:20.988Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD deh ===\" && grep -n -i \"\\bdeh\\b\\|dyh\" PHD.txt | head -20 && echo \"=== PHD dehgan ===\" && grep -n -i \"dehgan\\|dehkan\\|dēhgān\\|dhykn\" PHD.txt | head -10 && echo \"=== NYB ===\" && grep -n -i \"^deh\\|dēh\\| deh \" NYB_vol2_glossary.txt | head -20",
 "description": "MacKenzie and Nyberg for deh"
}
```


### [2026-09-05T20:10:21.158Z] TOOL RESULT

```
=== PHD deh ===
185:~ih: righteousness. ahlaw-dād Phlwb d”t'] alms, charity. ahlayih [kl dyh] righteousness. AN 7 ШЕ, * Md ahlomby [hlmwk' | M ?hImug] heretic. 3
214:a-pus [' BRE] without a son, childless. ár-, v. árdan. 5 āranj "Inc | N ~] elbow.. 9-43. "Ant *a-rāst Prst'] untruth. ārāstan, ārāy- [Pstn!,^Pd- | N ~] prepare, arrange, adorn. ~ién: arrangement, adornment. a-rawüg [”/wbk!] immobile. Ard р | M?yrd, N ~] a goddess; cal. 25th day. ard [KHM A < А gm; п | N ~] flour. агаа [py | (M rd?w)] righteous, truthful. ardan, ār- [THNN-tn' < А V thn; ?l-tn'] grind, mill. ardāyīh ['i?dyh | M?rd?yyh] righteousness, rectitude. ardig [/tyk! | M ?rdyg] battle. ardikkar рук], -kl | M?rdyqr] warlike, warrior. ~ith: doing battle. arduš [”ldwš = Av. aroduš-] a degree of sin. Ardwahišt Prtwhst' | M ?rdywhyst, (N urdībihist)] Right, the second Amahraspand, guardian of fire; cal. 2nd month; 3rd day. arešk [lysk' | M ()rysk, N rašk] envy, jealousy. ~én [-yn'] envious, jealous. ārešn Pim! | M ”7ysn-, N (a)rif] cubit. aryand [?/епа | N ~] horrible. arģawān [*/gwk'*n! | N aryawān] purple. armēšt ["/myst'] inactive, infirm. ~ih: infirmity. armēšt-ģāh [-g’s] secluded place for the infirm. агбуї&п [/wdšn'] growth. ~ig [-y&!] growing, vegetable. ars Dis | M?rs, N ~] tear (drop). artēštār УЯ? | N artēšdār!] warrior. „īh: warriorhood. arus [2/00] white. arwand [wnd] swift, valiant; river Orontes. ~ih: swiftness, valour. arwés [lwys | M ?rwys, N ~] rope. arz [KSP! < А Ар; с | N ~] worth, value. Arzah [Iz h == Av. arazahi-] the eastern continent of the earth. arzan [PE < А prg’; len! | N <) millet. arzàn Plen | M *rz'n, N ~] valuable, worthy. ~ig [-yk'] worthy. ~igih: value, worth, worthiness. arzidan, arz- [?/с-уїп! | N ~] be worth. ~išn: value, worth. arziz (сус | M ?rzyz, N ~] tin, lead. —ën [-yn'] tin, leaden. ārzōg Picwk! | M'wrzwg, N àrzó] desire, lust,
308:dahigān [dhywk’n' | N dihgān] countryman, farmer. dahliz [d^hlyc | (M dhryz), N ~] portico. dahm [d?hm] virtuous, pious; a full member of the Mazdean community, initiate. dahom [hwm | M dhwm, N ~] tenth. dalman [d”/mn' | N dál(man)] lammergeyer, eagle. dam- , ~išn, v. daftan. īdām [d”m | = M] creature, creation. здат [Pm | = M, N ~] tame animal. здат [d’m | P d’mg, N ~] net, snare, trap. dāmād [d?r?t! | M 424, N ~] bridegroom, son-in-law. ~ih: condition of a bridegroom, son-in-law. daménag [dmynk'] fan. damidan [dmytn'] = daftan. dān-, —išn, v. dānistan. -dàn [-d’n' | = M, N ~] suffix, -holder, -container. dàn(ag) [d”x(k)! | N ~a] seed, grain. Н dānāg [4>рА! | М dwg, N dana] knowing, wise. ША zn kh ~ih: knowledge, wisdom. ar dandàn [KK A < А kk’; dnd’n' | = M, N ~] tooth. dānistan, dān- [YDOYTWN-stn' < A У yd‘; d’n-stn' | M d^n-ystn, N ~] know. ~ign: knowledge. ~i8ndmand [- отпа) knowing. dar [BBA < A bb’; dl | M dr, N =] door; palace; chapter, subject. dar [d?] | M d@’r-, N ~] tree, gallows; wood. dar-, -išn, v. dāštan. -dār [-d'/| M -d’r, N ~] suffix, -holder, -keeper. Р darāy [dPg | J ~, N darāy] bell. *darak [dlk'] section, paragraph. darband [B B Abnd | N ~] gate. darbās [dips] palace. dard [dit! | M drd, N ~] pain. ~отапа [отла | M -wmnd, N ~mand] ill, suffering. dārēn [d'/yn! | М drwyn] wooden. darģāh [dig’s | N ~] doorway. dargardih [d*/krtyh | M d’rgyrdyh] crucifixion. dar-handarzbed [BB A-, dl-hndlcpt'] chamberlain. darigbed [dlykpt'] palace superintendent. *darmag [d?/mk!'] fine, delicate. darmān [dim?n! | M drmn, N ~] remedy, medicine. darridan, darr- [SDKWN-tn! < A V sdg; dl-ytn! | N <] split, tear. dàrüg [d"Iwk! | М drwg, N dari] drug, medicament. dār-wāzīg [Tlw cyk! | N dár-bàz] (pole-)acrobat. darz [dlc | N ~] seam. ~ig [-уА! | N darzi] tailor.
312:débag [dyp’k! | N dēbā] brocade. débahr [dyp?hl | P dybhr] anger. pad — dāštan: banish. dég [dyk' | N ~] cauldron. LU) deh [M TA < A m? | M dyh, N ~] country, land; village. 0" гу -ģān [МТА-, dh? »'] = dahigàn. dën [dyn' | = M, N din] religion; cal. 24th day. dēnār [4ут/ | N dindr] (gold) dinar. dēn-āstawān [dyn’stwh’n'], dēn-burdār [dynbwit^l] believing, faithful. dénig [dyny&! | N dini] religious. dénódag [dynwtk'] female, milch. dér, dérand, v. dagr, dagrand. d��s(ag) [dys(k') | M dys] form, appearance. désidan, dēs- (dys-ytn! | M dys-yd] build. déw [SD Y.A < A #02, pl. šydy? | N ~] demon, devil. dēwān [d(p)ywn! | N <] archive, collected writings. déwanag [dyw”nk! | N ~a] demonic, mad. dēwār [dyw?l | M dyw’r, N ~] wall. déw|-ésnih [Š D Y Aysnyh | (M dyw?snyh)] idolatry, devil-worship. ~-ézagih [ŠD Y Ayckyh] = ~-ésnih. dēwēk [dywwk! | № déwuk] leech. dibir [dpy(w)r' | M dbyr, N ~] scribe. ~ih: writing, scribeship. „estān [-st?n! LN ~] school. did [TWB < A twb; dt'] again, then, further. didan, wén- [HZ Y TWN-tn! < A У hzy; dytn', wyn- | M dydn, wyn-, N —, bin-] see. ~išn: sight, seeing. ~i8nig : visible. didar [dyť] | N ~] sight; visible. pad ~ [N padidár] visible. didom [dtwm] second. dil [LB(B)ME < A lb(b)-h; dyl | = M, N ~] heart. dilér [dylywl, dlyl | N ~] brave. diz [KLYTA < A дур; dc | M dyz, N ~] fortress. dē [2, TLYN' < A tryn | M dw, N du] two. ~-ахмапіб [2 !hw)nyk!] relating to both worlds. ~ganag [dwk”nk! | M dwg'ng, N dugāna] double; twin. dok [dwk! | N ~] spindle. dol [del | N —] bucket; astr. Aquarius. dó|-pahikar [dwptkl | N du-paikar] astr. Gemini. ~-pay [2 LGLE, дора | N du-pà] biped, human being. dos [dws | N —] gum; plaster. dē-saxwan [2 shwn'] two-tongued, deceitful. dēsēn [dwsyn'] gummy; plastery; *glazed (pottery). dóst [dwst' | = M, N ~] friend.
318:^-éwüzih [-yxw'cyk | (M dwšw'cyh)) evil speech, calumny. ~+farrag [-plg | P dwéfr] unfortunate. ~-farragih : misfortune. ~-gowisn [-gwbsn'] of evil speech, ill-spoken. ~-humat [-hwmt'] evil thought. ~-hixt [-Awht' | M dwfxwptyy!] evil speech. ~-kām [-2’m] ill-will, malevolence. ~-kanig [-knyk'] hag. — kar LAT difficult. ~-kuni&n [-kwngn'] of evil behaviour, ill-doing. dušmat [dwfmt! = Av. dufmata- | M dw$mtyy!)] evil thought. dušmen [dwsm(y)n' | = M, N dušman] enemy. ~ih: enmity. „ādīh [dušmntyh | M dwkmny’dyh, J dwfmn'dy] enmity, hostility. duš-|-menišn [dwf-myntn!] of evil thought, ill-thinking. --nàm [->”m | N ~] abuse, insult. dušox [dwshw! | M dtws(w)x] hell. ~ig [-yk'] hellish. duš-pādixšā(y) [dušp*thš*(d)) evil ruler. ~th: evil rule, misrule. dušrām [dwsl())m] unhappy. ~ih: unhappiness. dušwār [2001 | M dwšw”r, № ~] difficult, disagreeable. ~ih: difficulty, trouble, misfortune. du&-|-wir [dws-wyl] evil-minded. ~-wurréyisnih [-wlwdsnyh] heresy. c-.xém [-hym] evil-natured. ~-xwadiayih [-hwt'yh] misrule. ~-xwar Lea! | N ~] = dušwār. dušxwaršt [до оной! | M dwkxw styh!] evil deed. duxt [BRTE < A brt-h; dwht' | M dwxt, N ~] daughter. ~ar [dwhtl | N ~] daughter. duz(d) [GN BA < A gnb’; dwc(t) | M dwz, N duzd] thief. ~th [dwe(d)yh] theft. duzidag [dwcytk'] stolen; intercalary (days). duzidan, duz- [dwe-yin' | N duzdidan] steal. dwārīdan / dwāristan, dwür- [dwP?l-ytn!, -stn! | M dwr-] run, move (daevic). ~išn: abode (of demons), hell. dwāzdah [dw'cdh | M dw'zdh, N duwazdah] twelve. ~ап [-’n'] the zodiac.
426:kardan, kun-, (P Каг-) [OBYDWN-in' < А У Фа; krtn!, kwn-, (kl-) | M kyrdn, kwn-, (P kr-), N ~] do, make, act, perform. ~išn, v. kunišn. kardār [krt-, kil | N ~] active; worker, doer. ~th: activity. kard-espās [krtsf?s] servant, attendant. kārezār [A /yc! | M k*ry2*r, N kārzār] battle(-field). kār-framān [%'/p/mn' | М k’rprm’n, Ar. qahramán] manager, overseer. karg [klg | N ~] rhinoceros. kargās [klk’s | N kargas] vulture. kárig [k’lyk'! | N kari] active; warrior. ~ih: activity. kark [АА | N ~] chicken, hen. karkéhan [k/kyhn'] chalcedony. karm [Айт | P krm] action. karmir [klmyr] red, crimson. kār-nāmaģ [Rr mk!] record, chronicle. karr [k/ | M qr, N ~] deaf. karx68 [klhwš | (IN čarxušt)] wine-press. *karzang [kleng | M kyrzng, (ЇЧ xarcang)] crab; astr. Cancer. kas [4 YŠ < A?y£ | M ks, N ~] person, somebody. ~-iz [-c] anybody, (with a negative) nobody. kāskēn [k’skyn'] lapis lazuli. (аб) murw [-&! | N kāskīna] *magpie. ~ën [-yn'] blue-green; of lapis lazuli. kastan, kāh- [R’stn', Ph- | N ~] diminish, decrease, lessen. ~iSn: decrease, diminution. kastār [kst?]] destroyer, wrongdoer. ~ih: destruction, iniquity. kāstār [ks 1] diminisher. kaš [Rs | N ~] armpit. kaSawag [kšwk! | N kašaw] tortoise. kašk [АА | N ~] dried buttermilk. kaštīg [Astyk' | N kaštī] boat, ship. tkawādak [kw’tk'] young; baby; v. kodak. ikay [AYM T < А ?уті | N ~] when? 2kay [kd | N ~] title of the dynasty of Wištāsp (patron of Zoroaster), Kayanian. ~ak [-&!] ruler hostile to Zoroaster. kayk [kdyh! | N ~] flea. kë [MNW < A mn-w | M ky, N ki] who, which. P keč [kyc | = P] person, somebody. kéd [ду | P gydyg] soothsayer, magician. ~igih [-ykyh] soothsaying, prophecy. keh [ks | M kyh, N ~] small(er), less(er), young(er). ~tar [-il | N ~] = keh.
607:~išn: conquest, destruction. wanigarih [4W BDN-, wny-klyh] waste. wany [A(W)BDN' < APbdn | M wny] lost, destroyed. wany(b)ūdīh [4WBDN'butyh, -YHWWNtyh | M wny(b)wdyh] destruction, ruination. iwar [wl | M wr, N bar] breast. *war [w/] lake. Zwar [wl] oath, ordeal. ‘war [wl] shelter, enclosure. war-, v. waridan. warāy [wl”g | J bry] crow. waran [win'] desire, lust. warān [wi’n'] ram. wārān [w’Pn' | M wrn, N bārān] rain. waranig [wlnyk'] greedy. ~ih: greed, lust. waranig [wL nyk! | N bārānī) rain(y). warāz [wl”c | N gurāz] boar. war-čašm [wicfm] with eye(s) in the breast. ward-, v. 'waštan. lwardag [witk! | M wrdg, N barda] captive, prisoner. ~ih: captivity. *warda$ [witk'] on heat (female animal). ~ih: heat. *wardānāģ (wi? mk! | N gardana] (roasting) spit. wardénidan, wardén- [wityn-ytn! | (N gardànidan)] cause to turn; change, alter. wardišn [witšn! | M wrdyšn, N дака] turning, change, metamorphosis. ~ig [-y%!] transient, changeable. ~(ig)ih : transience, mutability. wardyün [wltywn! | P wrdywn, N gardiin] vehicle, carriage, chariot. warg [wlg | N barg] leaf. wārīdan, wār- [w?l-ytn' | M w’r-yst, N bàáridan] rain. warišn [wilsn'] conduct, behaviour. lwarm [wlm | N barm] memory. — kardan: learn by heart, memorize. *warm [wim | N barm] pool, reservoir. wārom [w’lwm] mind. warómand [wl’wmnd] doubtful. ih: doubt. warr [LBWS Y A < A lbw?] wool; garment. warrag [КММА < ?; wlk! | M wrg, N barra] lamb, ram; astr. Aries. wars [wils] hair. lwarz [wle | M wrz, N barz] work, agriculture. *warz [wic | М wrc/z] miracle, miraculous power. *warz [wlz | N gurz] club, mace.
653:~agig [-yk!] movable; intercalary (year). wihir- [whyl- | (M whwr-)] change. —išn: change. wimand [wymnd | = M] boundary, frontier, limit. ~ig, —6mand [-yk', 2wmnd] bounded, limited. *wiméhgén [wmyhkn! | M wymyh-] *shapely. wimustan [uwymwstn! | M wymrz- (< P)] spoil, destroy. win [wn'] vina, lute. wināh [zs | М zoyz)h, N gunàh] sin, crime. winahgar [wsk] | M wwhg’r, (N gunahhar)] sinner. ~ih: sinfulness. wināhīdan, wināh- [wn’s-ytn' | M wyn’h-] spoil, damage, destroy. ~išn: damage, destruction. winastag [wnstk'] spoilt, corrupt. windādan, wind- [HŠKHWN-tn' < А ME, V skh; wnd'tn! | M wynd'd, wynd-} find, obtain, acquire. ~išn: acquisition, earnings. ~ignig : findable. winjišk [zvxcšk! | N gunjišk, binjišk] sparrow. win(n)ārdan, win(n)àr- [wyx?7-tn' | M wyn’r-dn] order, fix, arrange. ~išn: arrangement. win(n)irdan [wynltn' | M wynyrdn) be arranged, established; stay. iwir [wyl | M wyyr] man, hero. *wir [wyl | M wyr-, N bir] memory, mind. *wir [wyl | N bir] thunderbolt. wirāstan, wirāy-, (P wirāz-) [wyl’stn', wyPd-, (wPc-) | M турі, tyr y-, (P wyr st, wyr!z-)] arrange, prepare, cultivate, restore. —jišn(ih): arrangement, preparation. wirég [wlyk! | N guréy] flight, escape. wiréxtan, wiréz- [OL YKWN-tn! < А У ‘rq; wlyhtn', wlyc- | P wryxt, N guréxtan, guréz-] flee, escape. wirdmandih [wy”wmndyh | M wyrwmndyy] memory. wirózag [*wiwck! | (P wrwe)] lightning. wis [wys | = M] village. wisandan, wisān- [ws’n-dn'] separate. —išn(ih): separation. wisay- (ws'd- | M wys’y-] rest. wisbed [wyspt! | M wysbyd] village headman. wisé [wsydy | (P wsyd), N gusë] despatch. ~ kardan: send, despatch. wisistan, wisin(n)- [wsstn', wsyn- | N gusistan, (gusil-)] break, split. wisp [wsp | M wysp] all, every. wispurdan, *wispar- [wspwltn'] tread, trample. wist [20; wyst! | = M, N bist] twenty. wistan, *wih- [SDYTWN-tn' < A V šdh; wstn'] shoot, throw. wistar(ag) [wsti(g) | N bistar] bedding, cover.
1418:country büm, deh, šahr.
2558:land bam, deh, šahr.
4216:village deh, wis.
4823:[140] mastog 19112256 mehtar Vess mastarg > e26 mizagūmand 2061” 406 mizagdārīh AAS 3G mizag 1.5 0G rūynī NINE maškabarzēn NS ey wi? makkizag 1923 556 1-2mašk way deh! ATES dehgiin! uses madār У. о mih мес madan, 1-3mihr мео
=== PHD dehgan ===
=== NYB ===
72:‘SGDH: * “SGA DEH his adoration, v. also SGDH ISLWN-:?SER to tie, to bind | ŠMH-: >47SME (for S'MI*) pt. pass. of SM* to hear ŠTH-: "ŠTE (for S'T E) pt. pass. of ŠTY to drink TRH (Prth): "A TREH his place
221:YDH (Prs): Y' DEH his hand (YAD-) cf YD?
975:Religion 1097-8; hac kunišn 4 im bē out of the activity of this man 5212; — c) late, for pat, as NP bi-: bē ravākēh bavet 37? (gl.); 4717 (gl.); 502° (editorial summary). - 4. adversative conj. but: a) after a negative sentence or a negative part of the sentence: andar déh ne, be pat kustak-é € deh vitart 61%; nē ozančt, bé apäc 6 Käyös Sut 4527, ete.; ne ēvāc ... bé not only...
1249:déh [dyh, MT”) village, settlement, pl. cas. obl. —-än [MT’-’n'; dh’n' 46? gl.], 614-16, 141, 329, 3711-15.27 ete. — Av. OP (706 sgg.) dahyu- ‘country’; Arm. lw. deh ‘district’; MPrs dyh ‘country’ (A-H I); Paz. deh, NP dth. Cf dahyu-pat.
1250:dēhīk [MT°-yk] belonging to a village, a community 37%; pl. cas. obl. ~-dn villag- ers, members of a community 3717-14-17,
1251:dehkin [dhk’n'] villager, pl. cas. obl. ~-dn 149. — A recent formation of deh; NP dihgän, Arab. lw. dihgän- ‘landlord’.
1451:age DkM 6989; tat pat dātistān(ūman>- deh či veh tuvän zatan u éraxtan cigón ka-š pat davreh u drusteh apäk gēbāh through righteousness thou art better able to defeat him and make him lose the case than if thou speakest to him coarsely and roughly (cf s. v. davr) PR 573; — pres. pass. 3d p. sg. éraxtét he is pronounc- ed guilty, opp. buxtet he is acquitted, v. Bthl, ZsR IV, 8; Paz. buxted ... érexted SGV III, 26; kē rāstēh rad pat xudstak eraxtet, ah veh cigon kē družeh rād pat ruvān éraxtét he who suffers loss of prop- erty because of his righteousness is better than the one who suffers the loss of his soul (forfeits his soul) because of his falsity PR 26$-9.] — Two vbs. seem to have coalesced here: 1) črtatan ērēc-, cf Paz. érexted and the caus. érezinidan ‘to condemn’ SGV XI, 257, most probably < abi- + Av. (1479 sq.) raék- ‘to leave in the lurch, to abandon to destruction’ (Bthl IF XII, 112sqq.); 2. éraxtan érang-, most probably a denom. of érang, črangčh 'trouble, delusion' (Paz. ŠGV X, 58 ete.) < *abi-ranga-, cf. an-črang, ranj, ranjak; MPrs ‘yrat, “yrnz- ‘to combat’, Verbum 199. (Bthl, l.c. adopted the reading érazt).
2104:daughter of this farmer 1518-19; Frašāvart i tē pus 2319; pus + mas i Ardavàn 319; vasün martom + andar gehän 49; vas xuähisn i rāpak-karihā xudhet 746-2"; if more than one relative attribute is added the izāfat is repeated before each: 735 etc. ; 2. paraphrased by hàm i (én i, ēt 4, õi 1) and placed before its head w.; this is the definiterelative attribute: häniZar- tuxšt mätist 3612; han i težtom tap 4322-23; ete.; — forming possessives: a) placed after the headw.: 4 man my, % tē thy, 4 amāh our, % šmāh your, but in the 3d p. the encl. pron. is used: 2-5 his, her, 2-Sän their; b) plaeed before the headw. as a definite relative attribute: hàn % man pusar 51?!; & i to humat 78-16; han 7-8 burtär 43%; hàn i amah dēh 5072-3; han + či vēh-dēn 515, ete. — forming the genitive of the interrog. kē: % ke? han + kē? whose?; other constructions with the izäfat, v. the demonstr. pronouns; — after adverbs used as prepositions: peš 4, hacadar 4, hacapar i, miyān +, ete., but the MSS are very little consistent in this respect. — The limit between nominal relative clauses and relative attributes is sometimes floating. — Av. (1199 sqq.) ya-; OP ya- rare, commonly hya- (haya-
2282:ken andar). — 8. as a kind of izäfat, mostly introducing an apposition: hán mart ... ke ahlav Zartuxšt 4919-17, 4317-18, adak-iš čišan guft ke dätär Ohurmazd 58°; han vartēnišn ... ke fraškart-kartārēh i veh 9921-22.25—26. without an antecedent: bavēt . ke Spitāmān Zartuxšt it may be S. Z. 6023; 597: an. imitation of the Av. idioms azom yö ahurö mazdå; hanjamanam fra- barata yo dadvd ahurö mazda ete.; — seldom introducing a gen.: han x¥arrah ke ... Eran dēhān ké-c ahlav Zartuxst
2785:8 [L, ^'w'; KN] či [LH; LH-y 104; ‘L-y 34%, 528-19] prep. to, with vbs. of motion; temporal: until; the sign of the indir. obj. (2277-5 perhaps the sign of the dir. obj. according to Prth. usage); — combined with other prepositions: andar 6, tài 6, or with an adv.: bē 6, fräc o, nazd 6; — governing a subst. or an adv. and forming with them compound pre- positions and adverbs: 6 berön, 6 nazdik, O pasth, 6 patirak, o peš (frac 6 peš, andar 6 peš); in a frame prep.: 6... rón; v. these ws.; — prev.: 6 druž früc mat the drug came to the place 5715-16; jn this case the ideogr. KN is common: 348 twice. 6521, 9422. — The form LH = 67 as a prep. 1612. 4210, 4424-25, 5617, — 6 cannot govern an encl. pron.; if such a pron. is affixed to the prep. it always belongs to the governed subst.: 6-š zäyısn until his birth 44!2; frāc ör-Sän deh vénam I foresee for their country 504; — in certain cases 6 is replaced by the adv. avis (g. v.). — Represents both Av. (163) ava, OP ava, and Av. (180 sqq.) avi, ao; MPrthPrs ’w; Paz. ó. The ideogr. KN originally rep- resented MIr (MPrthPrs) 6h < Av. (171 sq.) avada, OP avadä ‘thus’; in BP, having lost its final -%, it is used as 6, but chiefly
3602:-šān [-8’n'; Ps., inser. -šn] enel. pron., cas. obl. of the pers. pron. 3d p. pl.; independent form ašān (g.v.); follows the same rules as -š, of which it is the secondarily formed pl.: 1. gen. their: api-šān paitiyarak damistän 8611-315; — 2. for, to them: adak-išān garān dusxtäreh bavet 181°; — 3. dir. obj.: apt-šān ... apäc 6 dósax" apakanénd 101!!; — 4. agent: cē-šān Zaréré-c ozat 2613. — Belonging to a prep., which is changed to an adv. and placed afterwards in the sentence: api-šān patiš nē virröyam I do not believe in them 642°; cigén ka-šan ... ayošust avis hilé(nd) as if they pour molten metal on them 10120-21; cigon ka-šān šir i garm patiš andar dösend 10121-22; exception: governed by hac: hac-ısän 1018, v. s. v. haciš; attached to a prep. but belonging . to the. governed subst.: ör-sän deh for (oi) their village 5024; puštv kart" pātufrāsv 1287 the encl. -šan is the agent of kart (an awkward construction); with two enclitics 'pmyšn = api-m-iščin 1289.
4240:vitartan [wtltn'], viturtan [wtwltn'], vi- taštan [wtštn'], vitir- [wtyl-] to pass: andar dašt bē vitart passed over the plain 318; pat kustak + deh vitart passed outside the village 619-17; to pass by 7!1.15.22; bē vitast drove ahead 71’; to cross a bridge 7225.27; to go through a stream 101%. 10323; kë vitīrēndv the passers-by 12815; — pt. vitart, viturt deceased: vitart coll. the deceased 837. 8413; viturtān martūmān 10517. — Av. (640) vi-tar- = OP; MPrth w(y)drdn w(y)dr- (S, MHC); MPrs pres. wdyr- (S); Ps. pt. wilty, pres. wtyl-, wtl-; Paz. vadardan vadirdan, pres. vadar-, va- der-, vadir-; NP guöastan guóar-. Verbum 206, Ghilain 57.
6533:dehevad: dahyupat dër: dagr dērang: dēvāžaī : ny : dév-izakéh did, didica: dit din: dén divéri: dipivaréh dost: ~ dčžax: dčšaxu joisneh dràidan, drä&d: dräyitan dranač: drahnäi
6647:hūbēi: hubód, hubēdēh
```


## [2026-09-05T20:10:21.524Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN dih ===\" && grep -n -i \"dih ‘\\|dih  \\|dih,\\|dihkan\\|dihqan\\|dih«\\|dih \" HRN.txt | head -25",
 "description": "Horn for dih"
}
```


### [2026-09-05T20:10:21.574Z] TOOL RESULT

```
=== HRN dih ===
4150:(Lokalität Sih dih bei Isfahän), memc *ich auch*, öle
4335:(Bund., Men.), /ursandih (AV.).
5191:entlehnt in kurd. duänzdih (hier findet sich noch
5270:588. dih *Dorf*, vergl. dihgän (arab. LW. dihqän, arm.
9525:sich auch IXDDIH (Is. 37, 26) neben JNDDn (Is. 40, 25).
19712:Z'diH 664.
```


## [2026-09-05T20:10:30.775Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5265,5280p' HRN.txt && echo \"=== HUB ===\" && grep -n -i \"dih\\b\\|dihkan\\|dihqan\\|dahyu\" HUB.txt | head -20",
 "description": "Horn 588 and Hübschmann"
}
```


### [2026-09-05T20:10:30.827Z] TOOL RESULT

```
aw. dasa zehn', dasema-; phlv. dahuw; ai. r/ara,
dafamci-; arm. ^as« *zehn' (H. No. 270).
kurd. bei. LW. deh, dah; afj'. las; oss. d. t. das,
däsäm (106); wa/. das^ las, sar. dh, sij'n. J7s, te,
ya;ai. sangl. das, minj. LW. daÄ.
588. dih *Dorf*, vergl. dihgän (arab. LW. dihqän, arm.
LW. dehkan),
ap. dahyU' Xand'; aw. da/yii-; phlv. rfiA bezw. dcA,
da/yulpatj daxyu\paüh (arm. LW. dehpef), vergl. adihlk,
ttzdihtk; ai. ddsyu-,
kurd. daw; af/. LW. rfzA; bei. LW. d^A, dcÄ (58).
Die ursprüngliche np. Aussprache w^ird deh gelautet
haben.
589. dehän, dehen *Mund', dehün *Gedächtniss, Stegreif*,
dehane, dehne 'Zaum, Gebiss •^).
aw. zafan-^ zafar- *Rachen ; phlv. dahün,
=== HUB ===
2249:aus der dih wurde, wie -kert, -gerd (in Namen) zu gird
2250:u. s. w. geworden ist, oder geht np. dih = dlh, dsh,
4503:vahyO, vahistem; dih *Dorf, paz. deh Min. Gl. 60, Shk. 241,
4504:arm. deh in dehpet (= paz. dehvad, phi. dahyupat), nSdeh
4505:u. s. w., ap. dahyaus (nom. sg.), zd. danhu-s, gd. dahyu-,
4508:^maHiyah-, *kalfiyah- und vahyah- zuriickgehen wie np. dih
4509:auf ap. dahyu', Nach Abfall der letzten Silbe (Vokal +
4522:') Da im Neup. neben dih die Form ^i^, Alter also deh steht,
4523:liegt es allerdings nfther, dih = dih aus *daih = *dahy^ also durch
4599:TJeber dih = dth 'Dorf * aus *daAy u. s. w. siehe § 6, c.
7624:bahist, bihist 'Paradies* = zd. vahista-; dih *Dorf\ arm. deh,
7713:metrie', aram. haddam 'Stuck' (Daniel), syr. DIH; andarj
7780:a) Idg. sy = ap.J% = np. h: dih *Dorf', arm. deh =
7781:ap. dahyU" 'Provinz, Distrikt' ; hih gut, besser' = ap. vah-
8158:*Fremdling (5. Jhd.) = ap. '*mzdahyu' = zd. *nisdanhu-
10407:dih 64, 129.
```


## [2026-09-05T20:10:37.924Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4500,4530p' HUB.txt && echo \"==== 7775-7790\" && sed -n '7775,7790p' HUB.txt && echo \"==== 2245-2255\" && sed -n '2245,2255p' HUB.txt",
 "description": "Hübschmann context"
}
```


### [2026-09-05T20:10:37.974Z] TOOL RESULT

```
kasyah- *kleiner ; bih *gut, besser = paz. veh good, better*
Min. Gl. 213, phi. veh (der Schrift nach v^h oder t^h), arm.
veh uberlegen, besser', ap. vahyaz-(data-) ^ zd. ntr. vohu,
vahyO, vahistem; dih *Dorf, paz. deh Min. Gl. 60, Shk. 241,
arm. deh in dehpet (= paz. dehvad, phi. dahyupat), nSdeh
u. s. w., ap. dahyaus (nom. sg.), zd. danhu-s, gd. dahyu-,
Ich nehme mit Andreas (bei Horn Nr. 241) an, dass
np. mih^ kih und bih alte Comparative waren, also auf ap.
^maHiyah-, *kalfiyah- und vahyah- zuriickgehen wie np. dih
auf ap. dahyu', Nach Abfall der letzten Silbe (Vokal +
Konsonant) entstand mp. *ma&y^ *kady^ *vahy und *dahy,
deren ausl. y schwand, nachdem es Umlaut bewirkt
hatte^), wonach sich die mp. Formen: me& = meh, ked-
= keh^ veh und deh^) ergaben. Vgl. dagegen np. dah *zehn*
= ap. *da^a^ zd. dasa, Wenn neben jenen Komparativen
die alten Positive ap. *ma&'y ^kadu- und *va(h)u- im Mittel-
persischen bestehen blieben, so wurden sie zu *mah, *kah
und *vah und spater durch die Komparativform meh, keh,
veh verdrangt.
Ueber np. zirih 'Panzer' siehe § 12, fiber -tr- s.
§ 34, b.
*) Vgl. farrux = phi. farraxv § 4, a.
') Da im Neup. neben dih die Form ^i^, Alter also deh steht,
liegt es allerdings nfther, dih = dih aus *daih = *dahy^ also durch
Epenthese, hervorgehen zu lassen, wie Horn will. Ahnlioh wftre dann
hih = phi. v9h zu erklSren, nicht aber mih und kih (= phi. m-£ und k^s.)
H&bsohmann, Persisohe Studien. 9— 130 —
§ 7. Wie hier bei mh und deh arm. e dem mp. e (e)
= np. i genau entspricht, so konnte auch noch in andern
Fallen ein mp. e auf Grund des Armenischen angenommen
werden, da, wie oben bemerkt, die Armenier pers. a regel-
==== 7775-7790
arm. xorox in Xorox-azat (Sebeos 107) = p. FarruxzdS ^=
Xorazad (Tab. 395) u. s. w. ; arab. Arruxaj aus *Arax^ad
= gr. XoQoxodd bei Isidor von Charax, alter \4pax(jDoia^
ap. harauvatis (Tab. 157).
§ 109. Idg. 8 vor und nach Konsonanten.
a) Idg. sy = ap.J% = np. h: dih *Dorf', arm. deh =
ap. dahyU" 'Provinz, Distrikt' ; hih gut, besser' = ap. vah-
yah' in VohyazdCtta- ; siehe § 6, c ;
b) Idg. sr = ap. r im Anlaut, im Inl. hr, np. r: rod
'Fluss', arm. rot = ap. rautah-, skr. srofas; hazdr 'tausend',
arm. hazar = ap. "^hazahra-, zd. hazatlra-y skw^sahasra-
(vgl. § 96, b) ; aber mit erhaltenem h N. pr. Ahraman, Ahar-
man J Ahrman (bei Fird.), phi. Ahf'tnan^ Ahr{d)man u. s. w.,^ 219 —
arm. Arhmn (neben Haraman), syr. JD"in« Hoffmann,
Auszuge p. 64, zd. AUro mainytcS. Der Name AftasiyOb
(bei Firdusi), Frasiat (bei Tabari, Noldeke, Pers. Stud.
==== 2245-2255
ist auch von den Afghanen entlehnt worden.
588. Dazu arm. deh in mdeh Tremdling*. Ist deh (paz. deh
'Dorf ' Min. Gl. 60, Shk. 241) als altere Form anzusetzen.
*) VgL afgh. LW. las = np. dast *Hand*.— 65 -
aus der dih wurde, wie -kert, -gerd (in Namen) zu gird
u. s. w. geworden ist, oder geht np. dih = dlh, dsh,
das haufig vorkommt, auf mp. dsh zuriick?
589. Bei Rosen, Np. Sprachfiihrer p. 26, 39: ddhdnd*Qe-
bissstiick des Ziigels ; afgh. LW. dahana fem. *the bit
of a bridle', kal dehand, dahnd etc.
593. Ich stelle -des, -dis *ahnlich' zu gr. Jaxv/t/'zeige', dsixrjXov
```


## [2026-09-05T20:10:38.376Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SNS deh ===\" && grep -n \"deh\\|dyh\\|MT\" SNS_pages.txt | head -30",
 "description": "SNS glossary deh"
}
```


### [2026-09-05T20:10:38.436Z] TOOL RESULT

```
=== SNS deh ===
589:                                               Verbum. : See: VMT.
590:                                               VMT .    W.B. Henning, has Verbum des Mittelpersi-
801:        der Turfanfragmente. Gottingen 1933                                (VMT)
1354:                                                                                                                                                  .MMT-/Y1 * -P/V^ .TT-TV-TV-VY/ir*5 .<n
2214:                                                                                                        |vindadan          :    jl)     ^Wvindeh                :       >*         HSKHWN,yh: -*»Wi-v-»>
2220:                                                                                                          ro/TT *5 (A/ti'.«an.II,52)wndyh:jjt                                               UtVi. 1449),
2791:                                                                                                                            .ay-a-t-r-i/T* 5 **                      (V):fca//        ka r'MT.         >*    r^
2804:                                                                                                                            -o            yi**:^:       lj jl   /I .gljSI       ka-s , *MT,s:              -u^*   -
2997:                                                         •   nf-A^/T^              (VMT,     194) ni+ >/7aj                                                                                                          -t   /To^ -Tf-TA
3295:                                                                                                                                     •*it&*O*0.*- ?J*»#3:uzdehIgIh:                 -**J$->-»J<ZX?
3308:         6/Y1 **    vi>* « vjj* ^K*A:uzerin gah:                 <;«jiv''^«                               Ih +                 ja^j '^-) i>-jj- «*•> :dih/deh +
3566:                                                                                                       _a/u^.tt-^-y/w^ -a/*^ .rf-r<MT/r^ .u-r-Y-fi/T^                                    *°
4121: Mir.   My'wr:,^ (Mir. Man. II, 55)hy'r (bwdyh)
5059:                                                                                                                                                  MT
5374:                                                                                                         •TMI-IV-IMMT-^ H-^-Y^-T/A * 1f/Y -*
8066:                                                                      xsapan-:fc-                                            68) s dyh:>iJ* (i4iW>. 1707) saiti-.- L.
9571:                                  <                                :.             ^H* *ttv*£                               •***'**•« :deh/dxh=
9591:                                                                                                            rJU,lJ>i   U>.a^ J deh bad
9597:»^-^<6j#W>^'*'-Jm                           8    da ^g: MG          :        ^U, MZ     y.    M                 r      o **•*( -v, ^, t deh
12143:          .jjjliAKi -j-jI.4 (i)                   darend: yHSNN, nd:                            :       -*mi>*0           I   (       -^^' dehbad              !   •***»)    dahyubadan:               1^^
13065:                     gwk'dyhy  jj^^J /•»> "**->                 I
13196: jurabenfid hS:            __y+* *K*>-6*                                MT/W^ -lo-YI-Y.
13245:                                     .rMTA-Tf/rr** -y/u-s -tt/a^
13799:         V1Y/YT             ^v                   MT/V1            «Am           MA/1Y              o   1*-*
15397:g dyh 196/12
15406:                         wndyh 36/9                          xwrdn 275/13
16307:dandSn fris post 339/19     deh/dih 242/10               dist 313/11                drustih 339/12
```


## [2026-09-05T20:10:43.610Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '9555,9605p' SNS_pages.txt | cat -v | sed 's/\\^L/<FF>/g' | head -60",
 "description": "SNS glossary deh entry context"
}
```


### [2026-09-05T20:10:43.666Z] TOOL RESULT

```
                                                                                      (V)
                                                            .    a.T :       madan:         ln*fi


iraat         a +,/gam-:La Jamiya, a +/gara                              :    &$ rfW
Ian       s.^    (WM-BM-#r.M<zrt.II,59)rodn, md : jili IGNPE.                              11)


                           M-bM-^@M-"
                               t/lV*   .   **W:be madan:                      t"^ "^
nj^l^O**1        ^    **!* :rast           be madan:            \V*4      ^j <&M-BM-;->*>
                      1
                                                                                                                    ^^>-W*M-BM-+-Mnc abar raad:                      ^^
U JhfljUU M-BM-;A *!M-BM-+" >>* o^O*** mihrandroz
                                  <                                :.             ^H* *ttv*M-BM-#                               M-bM-^@M-"***'**M-bM-^@M-"M-BM-+ :deh/dxh=
 -^o^M^^'tf^^                                      :    roihrandrozlh: Ih:                          LM-bM-^@M-^T        M-bM-^@M-^^,
                                                                                                             -o-j'o-i^     dahyu :,-J -/ ;     /   -
                                                                                                                                                        MP':
                                                                                                                                                        .
                                                                                                                                                                 j.   .
                                                                                                                                                                           W
                                                                                                                                                                          -%M     to

                               (i^jiM^ljl J^^-.Jj :mihr+an+droz)

rfxtmyhr              s         >;L    {AiWb.     1186)mi0ro-drug                     :fc-
                                                                                                                                     -u-fv/irJ .rvvrJ
          ^                                                                                                                                                    -vr/rJ
                                                                                                    I




      /       y_..j mihirandrnz             :^ Benning, List, 82
                                                                                                            rJU,lJ>i   U>.a^ J deh bad
                                                                                                                              :




M-BM-;^-^<6j#W>^'*'-Jm                           8    da ^g: MG          :        ^U, MZ     y.    M                 r      o **M-bM-^@M-"*( -v, ^, t deh
                                                                                                                                              badan _   |iv   w ^^

mazga-            :       tM-BM-;          ma55^ n " : t^ij-1-" M-bM-^@M-">M-bM-^@M-" :mazg:
                                                                                                        fe"-: s- nitra-:    ^^         .
```


## [2026-09-05T20:10:55.072Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"pdf page\" SNS_pages.txt | head -5 && echo --- && awk 'NR<=9600 && /pdf page/{last=$0; ln=NR} END{}' SNS_pages.txt; python3 - <<'EOF'\nimport re\nlines=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt',encoding='utf-8',errors='replace').read().split('\\n')\nlast=None\nfor i,l in enumerate(lines[:9600]):\n    m=re.search(r'\\[pdf page (\\d+)\\]',l)\n    if m: last=(i+1,m.group(1))\nprint('last tag before 9571:',last)\nEOF",
 "description": "Find pdf page tag near SNS deh entry"
}
```


### [2026-09-05T20:10:56.944Z] TOOL RESULT

```
---
last tag before 9571: None
```


## [2026-09-05T20:11:00.984Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SNS_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\npos=sum(len(l)+1 for l in lines[:9570])\nprint('leaf(0-based) of deh entry:', t[:pos].count('\\f'), 'of', t.count('\\f'))\npos2=sum(len(l)+1 for l in lines[:16306])\nprint('leaf of index line:', t[:pos2].count('\\f'))\nEOF",
 "description": "SNS leaf numbers"
}
```


### [2026-09-05T20:11:02.630Z] TOOL RESULT

```
leaf(0-based) of deh entry: 138 of 242
leaf of index line: 235
```


## [2026-09-05T20:11:17.040Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nprint('has pdf page tags:', bool(re.search(r'\\[pdf page',t)))\npages=t.split('\\f')\nprint('leaves',len(pages))\n# find printed page markers\nfor i,p in enumerate(pages):\n    if re.search(r'(?m)^\\s*۹۰[۰-۹]\\s*$|^\\s*90[0-9]\\s*$', p):\n        print(i, repr(p[:80]))\nEOF",
 "description": "Inspect BQT vol2 pages file"
}
```


### [2026-09-05T20:11:18.827Z] TOOL RESULT

```
has pdf page tags: False
leaves 684
```


## [2026-09-05T20:11:21.605Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re,json\nd=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nprint(json.dumps(d['BQT'],ensure_ascii=False,indent=1)[:3000])\nEOF",
 "description": "BQT ref details"
}
```


### [2026-09-05T20:11:23.454Z] TOOL RESULT

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
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT
```


## [2026-09-05T20:11:33.332Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if '۹۰۲' in p or '٩٠٢' in p:\n        print('leaf',i,'|',p.strip()[:120].replace('\\n',' / '))\nEOF",
 "description": "Locate BQT printed page 902"
}
```


### [2026-09-05T20:11:35.272Z] TOOL RESULT

```
leaf 127 | ‫چوخدن‬                                                                              ‫‪14‬‬ /     ‫چو خا ‪ -‬بنم‌اول وخای 
leaf 158 | ‫‪ ۵ 64‬وا‬   ‫ست‬ /  /  /  /  / ‫از دم مقرض استادان خیاط ویوستین دوز و ازدم‬                ‫خاشاك ‪ ۱‬ه بروزن چالاك‪.‬ساق علف‪.‬
leaf 174 | ‫‪۷۱۹‬‬                                                                                ‫تنس‬ /  / ‫شاخ آن مرغ‌است وازآن زهگی
leaf 560 | ‫هه اس‬                                                                                                ‫ستاله‬ /  /  / ‫گفتن‬ 
leaf 586 | ‫)‪۷۱‬ات‬ /  / ‫که بجمد و جهنده باشد ‪ -‬و نام درختی است‌در‬           ‫بمعنی ربختن باشد ‪-‬ویمعنی‬         ‫ر‬ /             
leaf 594 | ‫‪۰‬؟(‪-۳۱۱‬‬                               ‫‪o‬‏‬    ‫‪«.‬‬                                    ‫فاون‬ /                  
leaf 648 | ‫‪‎6‬زب ‪٩ ۱‬‬ /  /  / ‫سید‬       ‫وی‬ /            ‫عن‬‫عوزن‬ /                 ‫بر‬         ‫اول ثوالی‬     ‫توح‬ /
```


## [2026-09-05T20:11:40.907Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'قریه' in p or 'بلوک' in p:\n        print('leaf',i, [l.strip()[:90] for l in p.split('\\n') if 'قریه' in l or 'بلوک' in l][:4])\nEOF",
 "description": "Find qarya/boluk in BQT vol2"
}
```


### [2026-09-05T20:11:42.947Z] TOOL RESULT

```
leaf 63 ['\u202bوآن چیزی بود ازکندم وآرد و نان وامثال آن\u202c               \u202bصفاهان را گویند عموما \u202a -\u202cوبلوکی']
leaf 134 ['\u202bيبند © \u202a۶ ,\u202c\u202c                  \u202bحصه وبهره و اصیب هم هت \u202a - ۴\u202cونام قریه\u200cای\u202c']
leaf 320 ['\u202bو در بلخ « دستجرد\u202c       \u202bوستحرد لقمان >\u202c          \u202bد\u202c    \u202bدر مرو دو فربه و در طوس دو قری']
leaf 341 ['\u202bوبسکون\u200cالی وفتح تحتالی» نام قریه\u200cاست ازقرای\u202c']
leaf 430 ['\u202bمفرد روده همگفته\u200cاند \u202a:\u202c\u202c         \u202bکوحار » نامبلوکی است و شهری است مابین\u202c']
```


## [2026-09-05T20:11:46.413Z] TOOL CALL #38: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nprint(json.dumps(d['BQT'].get('scans'),ensure_ascii=False,indent=1))\n\"",
 "description": "BQT scans config"
}
```


### [2026-09-05T20:11:48.171Z] TOOL RESULT

```
[
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
]
```


## [2026-09-05T20:11:55.731Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification && grep -ho \"BQT_v2_pages.txt[^\\\"]*\" page-*.json | head -20; echo ---; grep -ho \"\\\"ref\\\": \\\"BQT:[0-9]*\\\"\" page-*.json | sort -u | head; echo ---; grep -o \"BQT:9[0-9][0-9][^\\\"]\\{0,200\\}\" page-12*.json | head -5",
 "description": "How earlier pages handled BQT vol2"
}
```


### [2026-09-05T20:11:55.827Z] TOOL RESULT

```
BQT_v2_pages.txt (printed ≈ p.672); running head چوبگان
BQT_v2_pages.txt (printed ≈ p.622), s.v. چپق
BQT_v2_pages.txt, grep بنیامین / بن یامین
BQT_v2_pages.txt leaf 134, i.e. printed p. 677 by the running offset (leaf+543), one page off Nourai's citation. Footnote: «اوستا čira (زرنگ، شجاع) «بارتولمه ۵۹۸» ... «معین ...»». So Mo'in supports the Avestan connection and the Bartholomae column, but quotes the stem as čira- (not čirya-) and says nothing about Old Persian.
BQT_v2_pages.txt leaf 134), footnote to چیر
BQT_v2_pages.txt leaf 134 = printed 677) the footnote to چیری reads «... بهلوی čēr ... čīrīh ... ؛ غالب شدن، ظفر یافتن. رک: چیره» — Mo'in gives precisely the Pahlavi forms Nourai puts in this box, though he writes the abstract čīrīh (Nourai čĕrîh).
BQT_v2_pages.txt leaf 134), one page later than the citation: «چیر - بر وزن میر بمعنی غالب شدن و ظفر یافتن و مستولی گردیدن بر دشمنی باشد - و شجاع و دلاور را نیز گویند»; footnote «اوستا čira (زرنگ، شجاع) «بارتولمه ۵۹۸»». Content supports; page number off by one.
BQT_v2_pages.txt at leaf 667, i.e. printed p. ~1210 by the running offset (leaf+543) — about seven pages after Nourai's citation, so the page number cannot be confirmed. The entry itself is there: «سیخ ... معرب «سیخ» ... ترکی «شیش» ... آلتی باریک و دراز که قطعات گوشت را بدان کشند و کباب کنند، بابزن» with the Golestān shāhed «... هزار مرغ بسیخ»; the footnote cites هوبشمان together with Kurdish, Baluchi (فتیله) and Gilaki forms. Mo'in gives no Sanskrit ancestor and no borrowing claim.
BQT_v2_pages.txt and BQT_v3/4 OCR
BQT_v2_pages.txt leaf 377 (= printed p.917; the leaf/page offset is fixed by the 'بقیه در صفحهٔ ۹۰۸' catch-lines), footnote 1 to the headword دیو: 'پهلوی dēv … اوستا daēva (دیو). هندی باستان devá (خدا) «اشتقاق ۵۹۸». این کلمه در قدیم به گروهی از پروردگاران آریایی اطلاق می‌شده ولی پس از ظهور زرتشت و معرفی «اهورامزدا» پروردگاران عهد قدیم با دیوان، گمراه‌کنندگان و شیاطین خوانده شدند، ولی کلمهٔ «دیو» نزد همهٔ اقوام هند و اروپایی — باستثنای ایرانیان — معنی اصلی خود را محفوظ داشته است' — Mo'in's footnote is word for word the sentence Nourai puts in the box.
BQT_v2_pages.txt leaf 368 = printed p.908 (fixed by the catch-lines 'بقیه در صفحهٔ ۹۰۸' on leaf 367 and 'بقیه از صفحهٔ ۹۰۷' on leaf 368), footnote to دیبا: 'پهلوی dēpāk «تاوادیا ۹۱۰»، از هندی باستان dīp-, dīpayati (زبانه کشیدن، پرتو افکندن، درخشیدن) … «اشتقاق ۵۹۱» … اگرچه اشتقاق آن قطعی نیست' and, in the same note, the rival route 'وآن را از ریشهٔ … سومری (لوحه، خط) و اکدی … گرفته‌اند «فاب ۱ ص ۲۱۱»، رک: دستان، دبیر' — Mo'in gives Nourai's chain AND the uncertainty the chart's NOTE reports.
BQT_v2_pages.txt leaf 368 = printed p.908: headword 'دیبا * = بروزن زیبا، قماشی باشد از حریر الوان' with Mo'in's footnote 'پهلوی dēpāk … در فارسی = دیباه، دیبه؛ و دیباچه و دیوان نیز از همین ریشه است، معرب آن دیباج است' — the headword, the gloss 'a colorful cloth', and the extras دیبه/دیباج are all on the cited page.
BQT_v2_pages.txt and incoming/BQT/BQT_v3_pages.txt (ژ section), grep ژورنال
BQT_v2_pages.txt (printed page ≈ leaf+543, i.e. 817-820; the headword block دام runs from Nourai's cited page). The entry's sense 4 is 'هرچیز که جانوران در آن بفریب گرفتار شوند' = snare, and Mo'in's footnote 4 at the bottom of the page reads: 'هندی باستان dāman- (بند، ریسمان، زنجیر)، … ارمنی dam (تور) «امذق ۱۳۰»، پهلوی dām «مناس ۱۷۲»؛ نیز تور ماهیگیری' — Old Indic dāman- 'band, rope, chain', Armenian dam 'net', Pahlavi dām. That is Nourai's arrow, with the same Sanskrit comparandum.
BQT_v2_pages.txt leaf 381 (printed ≈ leaf+543 = 921-924, the last page of the د section, next leaf starting ذ): 'دیهیم ۱ ـ بکسر ها بروزن تعظیم، تاجی که مخصوص پادشاهان است … و بمعنی تخت'; the footnote at the foot of the leaf glosses it as the band 'که بر (افسر) پادشاه ایران بسته می‌شد'. The entry is where Nourai says it is and gives the meaning 'crown' he prints; the scan's footnote is too damaged to read the Greek etymon, which MON supplies.
BQT_v2_pages.txt for درون, leaves 303-305.
BQT_v2_pages.txt leaf 84 ≈ printed p. 627, lines 4834-4838)
BQT_v2_pages.txt leaf 84 (printed ≈ 627 on the leaf+543 offset, i.e. Nourai's 626 within the ±3 drift of that volume): headword «چراغ ـ بروزن فراغ؛ فتیله‌ای باشد که آنرا با چربی و روغن و امثال آن روشن کرده باشند», footnote 9 «کلمهٔ فارسی است که در آرامی و سریانی و نیز عربی (سراج) وارد شده (قرآن، سورهٔ نور)… ادی‌شیر (۹۸) میخواهد کلمهٔ فارسی چراغ را از سریانی مأخوذبداند ولی این امر مشکل است… «جفری ۱۹۹-۱۷۱» شکل پهلوی آن čirāγ است.» Exactly the derivation the arrow draws.
BQT_v2_pages.txt leaf 329 (printed 869), Moʿin's footnote 7: «دوب dub در زبان سومری بمعنی لوحه و خط است. از این زبان وارد اکدی شده ṭuppu … و از این زبانها وارد آرامی شده … نقل از «لغات بیگانهٔ اکدی» تألیف Zimmern»; the continuation on leaf 330 (printed 870) adds «برخی دیگر همان کلمهٔ فارسی و هم یونانی را از کلمهٔ سامی عاریه می‌دانند».
BQT_v2_pages.txt leaf 329 (the leaf carries the دفتر article and its footnotes; the estimated +543 offset in refs_online.json is ~3 leaves too high here — for this stretch printed ≈ leaf + 540). Moʿin's footnote there: «دفتر … را از یونانی diphthéra (پوست حیوانی) دانسته‌اند … دائرةالمعارف اسلام «دفتر»؛ نقل از Hobson-Jobson, Burnell et Yule: Dufter», continuing on p. 870 «از آنجا که در قدیم روی پوست کتابت می‌شده، کتاب را دفتر نامیده‌اند … هرودتس V. 58 … رابطهٔ بین دفتر پارسی با dipi پارسی باستان و ṭuppu اکدی و «دبیر» پارسی نامعلوم است». This is exactly Nourai's source and his gloss 'record book'.
---
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
---
page-126.json:BQT:918
page-126.json:BQT:912/914, Moin), but Wiktionary gives it no etymology and I found no independent scholarly derivation; its -z- would in any case not be a regular Persian development of -g-.
page-126.json:BQT:912,914
```


## [2026-09-05T20:12:01.420Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(358,368):\n    p=pages[i]\n    print('===== leaf',i,'=====')\n    print(p[:1800])\nEOF",
 "description": "BQT vol2 leaves around printed 902"
}
```


### [2026-09-05T20:12:03.140Z] TOOL RESULT

```
===== leaf 358 =====
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
‫داشته باشد وآنرا بگرردن مجرمانو کناهکاران‬                         
===== leaf 359 =====
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



                                  ‫دولك ‪۷۰‬‬                               
===== leaf 360 =====
  ‫‪ ۵‬ات‬   ‫تن‬
                                                                                                    ‫د وگاله‬


 ‫دول = بانالیمجهول بروزن غول د؛لو‬                        ‫دگوافه ‪ ۱‬ه باخفای ثانیوکاف فارسی‬
 ‫آبکتی رگاویند‪ - 9‬و برح دلو را گیفزته‌اند‬                ‫بند و صف آن يك‬ ‫پروزن فلانه ‪ ,‬عدد دگوورا‬
  ‫که بر جحبازدهم باشد ازدوازده بروج فلکی ‪1‬‬                ‫لماز همست ٍِ‪.‬‬  ‫ت‬‫کدو ر‬‫به از‬    ‫او‬‫کتن‪-‬‬‫اس‬
 ‫ویمعتی مکار ومحیل وشطاح ‪ -‬وبی‌حیا ‪ -‬وسفله‬
 ‫هم هت ‪ ۷‬و‪-‬دولآمارا نگیوزبند‪ , ۸‬و آن‬                     ‫گواو مره بکسر واو دوبم ک؛نایه‬
                                                                                     ‫د‬
                                                          ‫واوزمین را بز‬
                                                                      ‫ازشب وروز باشد ‪ -‬وبرج ور ک‬
‫ظرقی باشد مربع و مخروطی شکل که آبرا از‬
                                                                                                    ‫تفا‬         ‫کو‬
 ‫چوب سازند و در مر کز مخروطی آن سوراخی‬
 ‫کنند ومحاذی سوراخ سنگه آسیا نصب نمایند‬                  ‫«کنایه‌از آسمان‌وزمین‬     ‫دو گاهو اره‬
‫و پراز غلهسازند ‪ -‬و تیرکشتی را لفیزته اند‬                                                                 ‫‪.‬‬     ‫ات‬
 ‫وآن چوب بلندی باشد کهدر وسط کشتی بپرای‬
 ‫کنند ‪ -‬وبه‌عنی که وخربطه همآمده است‌چه‬                   ‫را کوبند که در آن‬            ‫کی‬
                                                                                        ‫چسبد‬
                                                                                           ‫و و‬
                                                                                             ‫کوقجه‬
                                                                              
===== leaf 361 =====
                                                                                                             ‫=‬   ‫‪۱‬‬

 ‫دوت آشور‬

‫وصاحب كمال ‪.‬والیاید وآنجنان‬         ‫خود را داشمند‬        ‫دو لا نه = بفتح نون» میوه ایست شبیه‬
‫لباشد‪ -‬ودرعربی‌بمعنی‌مالداری ونبییازی‌ومالیکه‬            ‫میب کوچکی ‪ ۰‬وآن درباغ و صحرا هردو بهم‬
‫یردوخاله‬
       ‫دست بدست ازهم بگیرند؟ ‪ -‬وبمعن ک‬                       ‫میرسد ورنگش سرخ میشود ولذتش مانندآلوی‬
                                         ‫باشد ‪۰6‬‬         ‫رسیده میخوش مدداشد وبك عددخته و(‪ )۱‬داله‬
                                                                                                                 ‫دارد ‪.‬‬
‫دو نان گرم و سرد ک‪-‬نایه از‬
                              ‫آفتاب وماه باشد ‪.‬‬              ‫نقیض‌تکبت‬         ‫»‬
                                                                               ‫تےو‬‫کزن‬
                                                                                    ‫دو لت ‪ = ۲‬برو‬
                                                             ‫باشد ‪ .‬ترد محققین وارستگی از علابق و حصول‬
‫دوو" = بنم اول (‪ )۲‬بروزن حجوم ‪۰‬‬                              ‫مطالب دارین که دیا وآخرت است بود ‪ -‬وترد‬
‫آن درخت‬    ‫که مقل ازرق صم‬           ‫نام درختی است‬
                                                             ‫مجردین زن وقرض‌نداشتن وباشتهای خودخوردن‬
                ‫اش ؛ وبفتح اول همآ مده ات‬
                                                                                      ‫وخواپیدن باشد ‪.‬‬
‫ورن‬   ‫باتستالی مجهول بر‬       ‫دوو بر ت‬                       ‫دو لت خدالی د بکون فوقالی ‪.‬‬
 ‫گزیر » دبیرونویسنده ومشیرا کویند » ودووبر‬               ‫بمعنی دولتمندی باشد ‪ -‬و کبی را نیز گوبند‬
‫از آن جهت میگونن دکه بدوعثر آراسته است ‪:‬‬                     ‫که فیض ا
===== leaf 362 =====
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
  ‫‪ .021 8‬افتانی ‪ 92۱‬استی‪ . 581‬وخی‪ 821. 5201‬شربکلی ‪ .5601‬شغنی‪
===== leaf 363 =====
  ‫دپهنجی‬                                                                                            ‫وروت‬
‫ده انگشت بر دهان گرفتن ‌‬                               ‫ده آل = باهمز؛ ممدوده بروزن‌افلاك‬
‫کنابه ازعجز وتضرع وزاری کردن وفروتنی‌دمودن‬             ‫نامضحالك است ویعضی گوبند ضحاك معرب ده ك‬
                                          ‫باشد ‪. ۴‬‬    ‫است» وچون اوبده عیب که زشتی‌بیکر و کوتاهی‬
‫دهانه = بروزن بهانه > زنگار معد لی‬                     ‫قد وسیاری غرور ونخوت وبی‌شرمی و بیحیابی‬
‫باشد وآن ازکان مس حاصل میشود » ورنگه‌آن‬                ‫وپرخوری رشکم‌خوار ‪ 2۳‬وبدزبانی وظلم وتعدی‬
                                                      ‫وشتاب زد کی ردررغ گوبی و بددلی باشدآ راسته‬
‫ببزی‌وطمم آن شیرین بتلخی مابل بود » ودهنة‬
‫فرنگ همن است » و آلرا در دواها بکار پرید‬                   ‫بودبدین نامش‌خواندند‪ .‬چه‪ 1‬بمه‌نی عآیمبده‬
                                                                                                   ‫است ‪٩‬‏ ‪#.‬‬
‫‏‪ ES‬جهت دقع سموم وداروی چشم» وبهترین‬
  ‫یز‬‫لسب‬‫اا‬   ‫رلنكگه آورید ‪ -‬ول‬
         ‫رجام‬                 ‫آنرا افزم‬                ‫دهان پشت ه بکرنون» منقذسقلی‬
‫کوینده ‪ -‬و هر چیز که شبیه بدهان باشد ‪5‬‬                                  ‫را گویند که سوراخ مقعد باشد ‪.‬‬
‫همجودهانه ودهنة کوه ودهانه ودهنةآب ودهالة‬
                                                       ‫و رای‬        ‫دهان درم ؟ = بفتح اول‬
                   ‫خك ومشك وامثال آن ‪.‬‬
                                                       ‫بی لقطه » خمبازه راکوبند وآن کشودن دهان‬
‫ده بانزده‌دادری » يعني زب وقر‬                         ‫است ببب کثرت خواب و بیاری خمار کیف‬
                          ‫وزیشت وآراش داری ‪.‬‬
                                                                                ‫وکاهلی ‪.‬‬
‫ده پنحی‪ = ۱‬بروزن‌شطراجی‪ ,‬زرقلب
===== leaf 364 =====
   ‫‪-‬‬    ‫‪۰‬‬    ‫یت‬
                                                                                                                                 ‫‪An‬‬



‫مرد بار دلیر وشجاع باشد ‪ -‬و مردم‌کاز کرده‬                             ‫الى و فتح‬           ‫وسکون‬   ‫یکراول‬           ‫‪.‬‬       ‫دهچه‬


 ‫وصاحب غیرت رانیزگفته‌اند‪ -‬وبمعنی حرامزاده‬                            ‫جیم فارسی ‪ ۰‬بزبان دیلم رعیت و دهقان را‬
                                         ‫‪۱‬‬       ‫همآ مده است‬



‫ذهر نکوهی ‪ - ۸‬کات دنیاکردن‬                                             ‫ور نس‬   ‫دم خدا ‪ » ۱‬بکراول‪ ,‬کدخدا‬
‫وبد اگوفتن باشد ‪ ,‬چه دهر بمعنی دنیا و عالم‬                                                              ‫ویزرکف ده را گونند ‪۲‬‬

 ‫سفلی و تکوهی بمعنی عیب جویی و بگدویی‬
                                                      ‫‪۰‬‬   ‫باشد‬
                                                                      ‫دار نده ده را گونند هنی سر کر ده رعایا ومزارع‪-‬‬

  ‫دهر ه ‪٩‬‏ ت بر ورن هره حربه ات‬                                                                                            ‫وه و بدار ‪.‬‬
‫دمته دار ودسته‌اش از هن وسرش‌مانند دای باشد‬
                                                                      ‫ده دله ‪ = ۲‬بفتح اول و سکون انی‬
‫ودرغایت تیزی بوده و بیشتر مردم گیلان دارند‬                             ‫کر دال ابجد ولام مفتوح ‪ ۰‬بیوفا جواهیری‌را‬‫و‬
                                                                      ‫وسی که هردم‌دل بدیگری دهد واو‬      ‫کویته ‪ -‬ک‬
‫گویند‬       ‫ند وبعهي‬
                   ‫افزاری‌است که بدان غله دکرو‬                        ‫ایوالهوی خوانند ‪ -‬ونر دم‌طدفقن آنکه هر لحظه‬
                                                                                                                  ‫ر‬

                    
===== leaf 365 =====
                                                                                           ‫‪6‬‬   ‫= ‪۵‬‬




‫دهگانی س بنتح اول بروزن ارزالی‬                        ‫نکر اول وثالی وسکون‬       ‫‪e ۱‬‏‬   ‫ذهشی‬

‫و‌درقديم رایج‌بوده ‪ -‬ویکس‬
                        ‫نوعی‌از زرباشد آن‬             ‫شبن فرشت ‪ ۰‬بمعنی دادن وهمت وبخشش و عطا‬
                   ‫اول دهقانی وزراعت کردن ‪. ۵‬‬                                     ‫وکرم باشد ‪.‬‬
                                                      ‫ذهشت ‏ بفتح اول وانی وسکون شین‬
                                          ‫باشد ‪.‬‬      ‫وتای‌قرشت» بمعنی‪,‬بکجهتی وبکرنگی وبگانگی‬
‫دهله = بفتح اول بروزن بهله ‪ ۰‬نوعی‬                                                          ‫باشد ‪۶# .‬‬

  ‫صل‬
   ‫تهن‬
     ‫م وپ‬
        ‫ورکه‬
           ‫از خار است که بوتهٌ آن بز‬
‫زمین میباشد واآرا گرن بروزن چمن‌می‌کومند‬
                                                                  ‫‪۰‬‬                            ‫‪۱‬‬    ‫است‬




‫و تشه‬    ‫وه‌طلق بل را نز گفه‌اند خواه از جوب‬          ‫دهقان خلك ح کنامه ازرضوان‌باعد‬
‫فتطره‬   ‫خواه ازسنگه و آ هك ساز ند ‪ +‬ومعری‬      ‫و‬                          ‫که خازن بهشت ات ‪.‬‬
                                     ‫خوانند ‪۶.‬‬
‫‪.‬نابه‬
    ‫دهلیزی ه بر وزن شبخیزی ک‬                          ‫است که زراعت کننده ومز آرع باشد‬   ‫وععنی‌دهقان‬

                                                      ‫و دهقان معرب آنست ‪ -‬ومردم تاربخی و تاریخ‬
‫ثالی و هیم»‬    ‫بفتح اول وسکرن‬   ‫‪-‬‬   ‫دهم‬                                        ‫ویند ‪. ۴‬‬
                                                                                      ‫گز‬‫دان را ن‬

 ‫‪۰:۷۰‬‬         ‫«معئی آفر سن «منای‪‎‬‬   ‫که‬         ‫‪ - ٩۱‬اسم صدز از دادن (ه‪.‬م‪ .).‬بهلوی ‪0‬‬

   ‫وحرنوشت*«تاوادبا ‪»4۵۱‬نز آهده‪ .‬‏ ‪-
===== leaf 366 =====
 ‫=‬    ‫‪6 ۵‬‬   ‫‪۱‬‬
                                                                                            ‫ده مر ده گوی‬


‫و بطعم شدرین بتلخی مابل است ‪۰‬‬                   ‫همیمباشد‬     ‫درخت و بوتهٌ غار است و آنرا معریی شجرتالفار‬
‫‪.‬وبند اگر کسی را‬
               ‫و معرب آن دهنج باشد گ‬                          ‫کوبند ‪ .۱‬وآن چوبی است که چون بوزسش‬
‫زهر ددهباشند بخورد دفع هرکدواگرزهی‬                                              ‫بوی خوش از آن آید ‪: ۴‬‬

‫لخورده باشد بخورد هلاك شود ‪ -‬ودهنه و لجام‬                    ‫ذه مرده گوی = یمعنی پر حرف‬
                              ‫اس را ندزگفته‌اند ‪۱‬‬
                                                                                          ‫وسیار گوی باشد ‪.‬‬
‫ده له ‪ -‬بفتح اول و ضمثالث و ظهور‬                             ‫ده هست ‪ ۲‬د بامیمبروزن بکدست‪.‬‬
‫انی ورابع > زیور وآرایش راکوبند وآنرا هر‬                     ‫فامدرختی‌است که بعربی‌غار گوبند‪ .‬چون‌بسوزانند‬
‫هفت تزخوانند ‪ -‬وبمعتی لتصان کردن هم‌هست‪.‬‬                      ‫بوی خوش دهد ودر بہار وزمستان سبز میباشد‪.‬‬
‫وهر دوچیز را نز گوبند که در کیفیت و کمیت‬                     ‫اکر شاخی ازآن دراراخی وباغ دفن کنند آفتی‬
‫تزديك بهم‌باشند‪ .‬وعدد نود هم هت که دعر بی‬
                                                             ‫که از ارضی وسماوی بپم رها آن شاخ رسد‬
                                         ‫تمعن خوالند ‪.‬‬       ‫وآن باغ و اراضی محفوظ باشد » وبعضی گویند‬
‫ده ودار = بکر اول و دال ابجد‬                                 ‫پاردرختی است کهآ ترا زغار ‪ ۴‬می‌گومندت ومعنی‬
 ‫بالف کشیده بروزن سه و چار » بمعنی دگاریور‬                   ‫ترکی آن ده نفراهسمت‪ .‬باد وعربان مسکران‬

                             ‫و کروفرباشد ‪.‬‬                                                         ‫خوانند ‪.‬‬
‫ذهون ‪ -‬بنتح‌ارل بروزن زبون» بمعنی‬     
===== leaf 367 =====
‫دي‬                                                                                     ‫=‬

‫‪ » ۱‬بروزن افزوده » بمعنی‬      ‫دوه‬
                                ‫ده ب‬             ‫و تحتانی بواو مجپول رسیده و بای فارسی‬
                   ‫عشر باشد که ده بك است ‪.‬‬                          ‫مفتوح مدال ابجد زده ا‬
                                                ‫»مر‌معروف واهی‌منکررا‬




                                     ‫بیان بیست ویکم‬


‫ماه دهم باشد از سال شمسی ‪ ,‬وآن مدت بودن‬
                                                 ‫دی = بقتح اول وسکون انی‪ .‬نام‌ملکی‬
                                                 ‫است که تقددس امور و مصالح دیماه و روز دی‬
‫وتام روزنهم ‪ ۴‬ازهرماه فارسی » ودرین روز ازماه‬
‫بمهر ودیبادین و دیباتر بدوتلق است ‪ -‬د ‏ | وی فارسیان جشن ‪-‬ازند ومد کنند؟ ‪ -‬وبکس‬
  ‫ظ‪ ,‬ممحف « دهوبه »‪ .‬این‌کله درعصر ساسانبان ویز در قرنهای اول اسلام معمول‬         ‫‪۱‬‬
 ‫بود ‪ .‬درالفهرست ابن‌الندیم(چاپ مصري ‪ )۸۳۳‬در موضوع اقل‌دبوان عرب ازفارسی بعربیآمدد‪:‬‬
  ‫صالح‌بن عبدالرحمن مولی‌بنی تمیم که" زیر دست مردایشام بر للفيخ صاحب دیوان حجاج بود‬
  ‫‪ :‬کیفتصنع بدهویه وششوبه؟‬           ‫قیول کرد که آنرا از فارسی بعربی بگرداند ‪ .‬رونام‬
     ‫قال ‪ :‬اکتب عثراً و نصف عشراً » در اینجا ظاهراً ششوبه مصحف « پنجوبه » است »ببااازب‬
  ‫مضیقه در اصطلاح عربی » تاگزیر شده صف عثر را بجای « شثوبه » بشنهاد کند ‪ .‬مب لمات ‪.‬‬
  ‫‪ - ۴‬دراوستا _تاکناا‪ 21‬با ‪ 2۷01021-‬بمعنیآ فربنندہ‪.‬‬    ‫‪ ۴‬هشتم صحیح‌است‪.‬‬
  ‫دادار و آفریدکار است و غالبا صفت اهورمزداست و آن ازمصدر ‪ 21‬بمعنی‌دادن وآفربدن است‪.‬‬
  ‫دی) برای تعین دهه‌ین ماه استممال شده ‪ .‬درمیان سی روز مامه‬      ‫در خود اوستا صفت دئوش [‪-‬‬

  ‫روزهای هشتم و پاتزدهم وبیست وسوم به دی( د=ئوش) موسوم است بنا بر تسمیه بنام ختا‪ .‬برای‬
  ‫بقیه درصفحةٌ ‪۸۰٩‬‏‬
```


## [2026-09-05T20:12:28.688Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad 2>/dev/null || mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad; cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad; curl -sL -o bqt362.jpg \"https://archive.org/download/borhan-ghate-v2/page/n362.jpg\" -w \"%{http_code} %{size_download}\\n\"; file bqt362.jpg",
 "description": "Download BQT vol2 leaf 362 image"
}
```


### [2026-09-05T20:12:33.873Z] TOOL RESULT

```
200 624515
bqt362.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 2569x3970, components 1
```


## [2026-09-05T20:12:38.168Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad; which convert magick pdftoppm; convert bqt362.jpg -crop 2569x900+0+3050 +repage -resize 200% bqt362_foot.png 2>&1 | head -3; ls -la bqt362_foot.png",
 "description": "Crop footnote area"
}
```


### [2026-09-05T20:12:41.332Z] TOOL RESULT

```
/usr/bin/convert
magick not found
/usr/bin/pdftoppm
-rw-rw-r-- 1 sfmqrb sfmqrb 752374 Sep  5 16:12 bqt362_foot.png
```


## [2026-09-05T20:12:43.719Z] TOOL CALL #43: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqt362_foot.png"
}
```


### [2026-09-05T20:12:44.005Z] TOOL RESULT

```

```


## [2026-09-05T20:12:44.002Z] INPUT

[Image: original 5138x1800, displayed at 2000x701. Multiply coordinates by 2.57 to map to original image.]


## [2026-09-05T20:12:58.766Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad; curl -sL -o bqt363.jpg \"https://archive.org/download/borhan-ghate-v2/page/n363.jpg\" -w \"%{http_code}\\n\"; convert bqt363.jpg -crop 2569x700+0+3250 +repage -resize 180% bqt363_foot.png; convert bqt363.jpg -crop 2569x600+0+150 +repage -resize 180% bqt363_head.png; identify bqt363.jpg",
 "description": "Fetch leaf n363 and crop"
}
```


### [2026-09-05T20:13:05.044Z] TOOL RESULT

```
200
bqt363.jpg JPEG 2569x3970 2569x3970+0+0 8-bit Grayscale Gray 256c 692415B 0.000u 0:00.000
```


## [2026-09-05T20:13:07.289Z] TOOL CALL #45: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqt363_head.png"
}
```


### [2026-09-05T20:13:07.462Z] TOOL RESULT

```

```


## [2026-09-05T20:13:07.456Z] INPUT

[Image: original 4624x1080, displayed at 2000x467. Multiply coordinates by 2.31 to map to original image.]


## [2026-09-05T20:13:40.600Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad; convert bqt362.jpg -crop 2569x1300+0+2000 +repage -resize 150% bqt362_mid.png; identify bqt362_mid.png",
 "description": "Crop middle of BQT p902"
}
```


### [2026-09-05T20:13:43.465Z] TOOL RESULT

```
bqt362_mid.png PNG 3854x1950 3854x1950+0+0 8-bit Grayscale Gray 256c 1007.84KiB 0.000u 0:00.000
```


## [2026-09-05T20:13:45.807Z] TOOL CALL #47: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqt362_mid.png"
}
```


### [2026-09-05T20:13:46.116Z] TOOL RESULT

```

```


## [2026-09-05T20:13:46.103Z] INPUT

[Image: original 3854x1950, displayed at 2000x1012. Multiply coordinates by 1.93 to map to original image.]


## [2026-09-05T20:14:02.929Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls -la MON_part1.txt MON_part2.txt 2>/dev/null && head -c 600 MON_part1.txt; echo; echo \"=== ARY files ===\"; ls incoming/ARY 2>/dev/null | head",
 "description": "Check MON and ARY files"
}
```


### [2026-09-05T20:14:02.982Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 4377831 Sep  4 14:06 MON_part1.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 4331421 Sep  4 14:06 MON_part2.txt
0 
2 


چم 
نسم ی 


تمه موی موم 
3 


ماما نا موس ملاس 
روم و3 


2 
7 
س 


همجمج مد هعرج ی وه جر ج مهو موجه و وید جع مج وی ۶ج و وم مب و وج 5 
ادا ما ما زو ماه مرو ماخ( نوم شام 4و منم مخ نامه مدش نامع 

مه مر وه ود 

3 ور 133131313 


هم مشب جج جب بیج چم مدوجو 
چم وم 
جر 


درل ولو ونر نو تلا رت 
11 


مج جرج جر یی میج 6و یوج هو هجوج وی یویر جر دم مور و 555 
و ده ها وی مزا موی 
=== ARY files ===
ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf
ARY_latin_index_pages.txt
ARY_pages.txt
ARY_pages.txt.pages
```


## [2026-09-05T20:14:07.133Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"dahyu\\|dasyu\\|dásyu\" ARY_pages.txt ARY_latin_index_pages.txt | head -20",
 "description": "grep Aryanpur for dahyu"
}
```


### [2026-09-05T20:14:07.222Z] TOOL RESULT

```
ugrep: warning: ARY_pages.txt: No such file or directory
ugrep: warning: ARY_latin_index_pages.txt: No such file or directory
```


## [2026-09-05T20:14:10.324Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && grep -n \"dahyu\\|dasyu\\|dásyu\\|dahyav\" ARY_pages.txt ARY_latin_index_pages.txt | head -20; echo \"=== deh ===\"; grep -n \"^ده\\| ده \\b\" ARY_pages.txt | head -10",
 "description": "grep Aryanpur"
}
```


### [2026-09-05T20:14:10.393Z] TOOL RESULT

```
=== deh ===
797:دهه انگلیس را تسخی رکردند. ساکنان پیشین انگلیس یک قوم هند و اروپایی دیگر یعنی سلت‌ها بودند
3866:ده یونانی (080): 4 مف۳51526 دانمارکی (0۸(75/7): زرل ۱1۲۲
5781:ده اسر دانمارکی (0۸(13): 7028
8249:دهخدا: ۱۰۴۹۵) یکی است. حتی اگر "دشن" با راژه‌ی پهلوی 2۸8118 رابطه‌ای نداشته باشد رابطه‌ی واژه‌های
9353:ملندی (ل77ا0): اد ده 9 (5۸)) ان
9489:آلمانی کهن (027044(7 67اب صاه): 6 (12م6) ید ده 1
11936:پهلری (7شاتلمم): ۸ چک (2507)). ها ده 0:۱
12150:هلندی (بلع۵7: ۹" ده 32 مان
12531:: ده 4 (0156) تاک میدن
14229:ده پرنانی (0/882): ,۱817271 ,۸88113۷8۷۸ 1/80۷ ۱
```


## [2026-09-05T20:14:22.259Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== POK dasyu ===\" && grep -n \"dasyu\\|dásyu\\|dåsyu\\|dahyu\" POK_01.txt POK_02.txt POK_03.txt POK_full.txt | head -20 && echo \"=== POK this/thinos ===\" && grep -n \"thinós\\|thīn\\|θίς\\|thīs \" POK_01.txt POK_full.txt | head -10 && echo \"=== AHD ===\" && grep -n -i \"dheigh\\|dhes\\|dhis\" AHD_watkins1985.txt | head -20",
 "description": "Pokorny and Watkins greps"
}
```


### [2026-09-05T20:14:22.343Z] TOOL RESULT

```
=== POK dasyu ===
=== POK this/thinos ===
=== AHD ===
168:Roots indicating a number of technical operations are attested in most of the lan- guages of the family. One such is teks-, which in some dialects means “to fabricate, espe- cially by working with an ax,” but in others means “to weave” (TEXTILE). A root dheigh-, meaning “to mold, shape,” is applied both to bread (DOUGH) and to mud or clay, whence words for both pottery and mud walls (Ira- nian *pari-daiza, “walled around,” borrowed into Greek as the word that became English PARADISE).
338:bherek-. To shine, glitter. A by-form of bhereg-. Variant form *bhrek-, possible root of various Germanic forms. 1. Germanic *bregdan, to move jerkily (> “to shimmer”), in Old English bregdan, to move quickly, weave, throw, braid: BRAID; UPBRAID. 2. Derivative West Germanic *brigdil-, bridle (referring to the movements of a horse’s head), in: a. Old English bridel, bridle: BRIDLE; b. Middle High German bridel, bridle, rein: BRIDE?. 3. Germanic *bréhw6, eyelid, eyelash, in Old Norse bra, eyelash: BRAE. 4. Germanic “breh(w)an, to shine, forming West Germanic *brehsmo, a bream, in Old French bre(s)me, a bream: BREAM!. [Pok. bherak- 141.] bherg-. To buzz, growl. Germanic *berk- in Old English beorcan, to bark: BARK}. [Pok. bhereg- 138.] bhergh-'. To hide, protect. 1. Germanic *bergan in: a.compound *h(w)als-berg-, “‘neck-protector,” gorget (*h(w)alsaz, neck; see k“el-1); b. compound *skér-berg-, “sword-protector,” scabbard (*skér-, sword; see sker-'). 2. Zero-grade form *bhrgh- in: a. Germanic *burgjan in Old English byrgan, to bury: BURY; b. Germanic deriva- tive *burgisli- in Old English byrgels, burial: BURIAL. 3. a. Germanic *borgén, to borrow (? < “to take care of one’s own interests, entrust, pledge, lend, loan”), in Old English borgian, to borrow: BORROW; b. Germanic de- rivative *borganjan in Old French bargaignier, to haggle (> bargaine, haggling): BARGAIN. [Pok. bhergh- 145.] bhergh-?. High; with derivatives referring to hills and hill-forts. 1. Germanic *bergaz, hill, mountain, in: a. Old English beorg, hill: BARROW?; b. Old Norse berg (> Danish and Norwegian berg), mountain: ICEBERG. 2. Compound *harja-bergaz, “army-hill,” hill-fort (*har- jaz, army; see koro-). 3. Compound *berg-frij-, “high place of safety,” tower (*frij-, peace, safety; see pri-), in Old French berfrei, tower: BELFRY. 4. Zero-grade form *bhrgh- in Germanic *burgs, hill-fort, in: a. Old English burg, burh, byrig, (fortified) town: BOROUGH, BURG; b. Old High German burg, fortress: BURGHER; Cc. Middle Dutch burch, town: BURGOMASTER; d. Late Latin bur- gus, fortified place (> burgensis, city dweller): BOURG, (BOURGEOIS), BURGESS, BURGLAR; FAUBOURG. 5. Suf- fixed zero-grade form *bhrgh-to- possibly in Latin fortis, strong (but this is also possibly from dher-?): FORCE, FORT, FORTALICE, FORTE!, FORTE?, FORTIS, (FORTISSIMO), FORTITUDE, FORTRESS; COMFORT, DEFORCE, EFFORT, ENFORCE, FORTIFY, (PIANOFORTE), REINFORCE. [Pok. bheregh- 140.] bhers-. Quick. Latin festindre (< *fers-ti-), to hasten: FESTINATE. [Pok. bheres- 143.] bhes-', To rub. 1. Zero-grade form with unclear suffix *(bh)s-amadho-, sand (in Greek psamathos), in Germanic *sam(a)dam, *sandam in Old English sand, sand: SAND. 2. Suffixed form *(bh)s-abh- in the further suffixed form *sabh-lo- in Latin sabulum, coarse sand: SABULOUS. 3. Suffixed form *bhs-d- in (i) Greek psén, to rub, scrape: PALIMPSEST (ii) Greek pséphos, ballot, pebble: PSEPHOLO- GY. 4, Perhaps suffixed form *bhs-ilo- in Greek psilos, smooth, simple: EPSILON, PSILOMELANE, UPSILON. [Pok. bhes- 145.] bhes-2. To breathe. Probably imitative. Zero-grade form *bhs- in Greek psukhein (< *bhs-il-kh-), to breathe, hence psukhé, spirit, soul: PSYCHE, PSYCHIC, PSYCHO-; METEMPSYCHOSIS. [Pok. 2. bhes- 146.] bheudh-. To be aware, to make aware. 1. Germanic *(for)beudan (*for, before; see per') in: a. Old English béodan, to proclaim: BID; b. Old English forbéodan, to forbid: FORBID; ¢. Old High German farbiotan, to forbid: VERBOTEN, @: Germanic *tudén- in Old English boda, messenger, hence bodian, to announce: BODE!. 3. Ger- manic *budilaz, herald, in Old English bydel, herald, messenger: BEADLE. 4, Germanic *budam in Old Norse bodh, command: OMBUDSMAN. 5. Sanskrit bodhati, he awakes, is enlightened, becomes aware, and bodhih, perfect knowledge: BUDDHA; BODHISATTVA, BO TREE. [Pok. bheudh- 150.]
377:dapper, heavy, strong; later quick, nimble: DAPPER. [Pok. dheb- 239.] dhegvh-. To burn, warm. Suffixed o-grade form *dhogvh- eye- in Latin fovére, to warm, cherish, foment (> fomen- tare, to foment, and fomes, tinder): FOMENT, FOMITE. [Pok. dhegth- 240.] dh@(i)-. To suck. Contracted from *dheoa(i)-. 1. Suffixed reduced form *dhé-mnd- in Latin fémina, woman (< “she who suckles”): FEMALE, FEMININE; EFFEMINATE. 2. Suf- fixed reduced form *dhé-to- in Latin fétus, pregnancy, childbearing, offspring: FAWN, (FETAL), FETUS; EFFETE, (FETICIDE), SUPERFETATE. 3. Suffixed reduced form *dhé-kundo- in Latin fécundus, fruitful: FECUND. 4. Suf- fixed reduced form *dhé-no- in Latin fénum, faenum, hay ( < “produce”): FENNEL, FINOCHIO; (FENUGREEK), SAIN- FOIN. 5. Perhaps suffixed zero-grade form *dhi-lyo- (< *dhia-lyo-) in Latin filius, son, and filia, daughter (but these are equally possibly from the root bheue-): FILIAL, FILIATE; AFFILIATE, HIDALGO. 6. Suffixed reduced form *dhé-lo- in Latin fél(are, to suck: FELLATIO. 7. Suffixed reduced form *dhé-l-ik- in Latin félix, fruitful, fertile, lucky, happy: FELICITATE, FELICITY; FELICIFIC, INFELIC- Ty. 8. Suffixed reduced form *dhé-ld- in Greek thélé, nipple: ENDOTHELIUM, EPITHELIUM, (MESOTHELIUM). 9. Suffixed reduced form *dhé-l-u- in Greek thélus, female: THEELIN. [Pok. dhéi)- 241.] dheia-. To see, look. Variant form *dhyd- (< *dhyag-) in: a. suffixed form *dhyd-mn in Greek sémeion and séma (stem sémat-), sign: SEMANTIC, SEMATIC; SEMAPHORE, SEMASIOLOGY, SEMEME, SEMIOLOGY, SEMIOTIC; b, San- skrit dhydti, he meditates (< “he observes mentally”): ZEN BUDDHISM. [Pok. dheis- 243.] dheigh-. To form, build. 1. Germanic *daigjén in Old English d%ge, bread kneader: DAIRY. 2. Germanic *-dig- in Old English compound Aléfdige, mistress of a house- hold (< “bread kneader”; Al#f, bread, loaf): LADY. 3. Ex- tended o-grade form *dhoigho- in Germanic *daigaz in: a. Old English dag, dough: pouGH; b. Old High German teic, dough: TEIGLACH. 4. Suffixed zero-grade form *dhigh-ird, in Latin figira, form, shape (< “result of kneading”): FIGURE; CONFIGURATION, DISFIGURE, PRE- FIGURE, TRANSFIGURE. 5. Nasalized zero-grade form *dhi-n-gh- in Latin fingere, to shape: (FAINT), FEIGN, (FEINT), FICTILE, FICTION, FIGMENT; EFFIGY. 6. Nasal- ized zero-grade form *dhi-n-g(h)- in Greek thinganein, to touch: THIGMOTAXIS, THIXOTROPY. 7. Suffixed o-grade form *dhoigh-o- in Avestan daéza-, wall (originally made of clay or mud bricks): PARADISE. [Pok. dheigh- 244.] dhel-. A hollow. 1. Germanic *daljé in Old English dell, valley: DELL. 2. Germanic *dalam in Old English del, valley: DALE. 3. Germanic *del- in Old Norse dzla, wooden gutter on a ship: DALLES. [Pok. 1. dhel- 245.] dhelbh-. To dig, excavate. Germanic *de/ban in Old English de/fan, to dig: DELVE. [Pok. dhelbh- 246.] dhembh-. To bury. Suffixed zero-grade form *dhmbh-o- in Greek taphos (< *thaphos), tomb: CENOTAPH, EPI- TAPH. [Pok. (dhembh-), dhmbh- 248.] dhen-'. To run, flow. Suffixed o-grade form *dhon-ti- in Latin fons (stem font-), spring, fountain: FONT!, FOUN- TaIN. [Pok. 1. dhen- 249.] dhen-2. Palm of the hand. Suffixed form *dhen-r in Greek thenar, palm of the hand: THENAR. [Pok. 2. dhen- 249.] dher-1. To make muddy; darkness. 1. Suffixed form *dher-g- in Germanic *derk- in Old English deorc, dark: DARK. 2. Suffixed zero-grade form *dhr-egh- in: a. Ger- manic ‘suffixed form *drah-sta- in Old English drés, dregs: pross; b. Germanic *dragj6 in Old Norse dregg, dregs: DREGS. 3. Suffixed extended zero-grade form *dhro-bh- in Germanic *drab- in: a. Old English dreflian, to drivel: DRIVEL; b. probably Low German drabbelen, to paddle in water or mire, draggle, akin to the Low German source of Middle English drabelen, to draggle: DRABBLE; C. Middle Irish drab, dregs, probably akin to the Celtic source of DRAB2. 4. Suffixed extended
379:zero-grade form *dhra-gh- in: a. Greek tarassein (Attic tarattein), to confuse, disturb: ATARACTIC; b. Greek trakhus, rough: TRACHEA, TRACHOMA, TRACHYTE. [Pok. 1. dher- 251.] dher-2, To hold firmly, support. 1. Suffixed form *dher-mo- in Latin firmus, firm, strong: FARM, FERMATA, FIRM, FIRMAMENT; AFFIRM, CONFIRM, INFIRM, (INFIR- MARY). 2. Extended form *dhergh- possibly in Latin fortis, strong (but this is also possibly from bhergh-?). 3. Suffixed zero-grade form *dhr-ono- in Greek thronos, seat, throne (< “support”): THRONE. 4. Suffixed form *dher-mn in Sanskrit dharma, statute, law (< “that which is established firmly”): DHARMA. 5. Old Persian dar-, to hold (whence Persian -ddr, ‘“-holder’’): SIRDAR, TAHSILDAR, ZAMINDAR. [Pok. 2. dher- 252.] dher-3, To drone, murmur, buzz. Extended zero-grade form *dhrén- in: a. Germanic *drén- in Old English dran, drén, male honeybee: DRONE}; b. Greek thrénos, dirge, lament: THRENODY. [Pok. 3. dher- 255.] dhers-. To venture, be bold. 1. O-grade form *dhors- and zero-grade form *dhrs- respectively in Germanic *ders- and *durs- in Old English dearr and durst, first and third person singular present and past indicative of durran, to venture: DARE, (DURST). 2. Possibly Latin -festus in: a. infestus, hostile (? < “directed against”; in-, into, against; see en): INFEST; b. manifestus, palpable, evident (< “caught red-handed, grasped by the hand”; manus, hand; see man-2): MANIFEST. [Pok. dhers- 259.] dhés-. Root of words in religious concepts. Possibly an extension of dhé-'. 1. Suffixed form *dhés-yd in Latin fériae (Old Latin fésiae), holidays: FAIR?, FERIA. 2. Suf- fixed form *dhés-to- in Latin féstus, festive (> German Fest, festival): FEAST, (-FEST), (FESTAL), FESTIVAL, FES- TIVE, FESTOON, (FETE), FIESTA; (GABFEST), OKTOBER- FEST. 3. Suffixed zero-grade form *dhas-no- in Latin fanum, temple: FANATIC; PROFANE. 4. Possibly suffixed zero-grade form *dhas-o- becoming *dhes-o- in Greek theos (< *thes-os), god: THEO-; APOTHEOSIS, ATHEISM, ENTHUSIASM, PANTHEON, POLYTHEISM. [Pok. dhés- 259.] dheu-'. Also dheue-. The base of a wide variety of derivatives meaning “to rise in a cloud,” as dust, vapor, or smoke, and related to semantic notions of breath, various color adjectives, and forms denoting defective perception or wits. 1. Suffixed extended zero-grade form *dhii-mo- (<*dhua-mo-), smoke, in: a. Latin fimus, smoke: FUMAROLE, FUMATORIUM, FUMATORY, FUME; FUMARIC ACID, FUMIGATE, FUMITORY, PERFUME; b. Greek thumos, soul, spirit: -THYMIA; ENTHYMEME; c. Greek thumon, thumos, thyme (< “plant having a strong smell”): THYME. 2. Suffixed lengthened zero-grade form *dhi-li- in Latin filigd, soot: FULIGINOUS. 3. Ex- tended form *dheus- possibly in Germanic *dus- in: a. Old English dysig, foolish (< “stupefied,” “confused”): pD1zzy; b. Danish dase, to make drowsy, akin to the probable Scandinavian source of DOZE. 4. Suffixed ex- tended form *dheus-o- in Germanic *deuzam, breathing creature, animal, in: a. Old English déor, animal: DEER; b. Old Norse dyr, animal, deer: REINDEER. 5. Suffixed o-grade form *dhous-o in Slavic *dukh- in Russian dukh, breath, spirit: DUKHOBoR. 6. Variant extended form *dhwes- in nasalized form *dhwens- in Germanic *duns-, dust, meal, in: a. Germanic suffixed form *duns-to- in Old English dist, dust: pustT; b. Old Norse diinn, bird’s down (< “fine like dust”): DOWN?, DUVETYN; (EIDER- Down). 7. Extended zero-grade form *dhus- in Greek thuos, burnt sacrifice, incense (> Latin thus, incense), and ¢huia, cedar: THUJA, THURIBLE; (THURIFER). 8. Suf- fixed extended zero-grade form *dhus-ko- in: a. Ger- manic duskaz in Old English dox, twilight: Dusk; b. Latin fuscus, dark, dusky: OBFUSCATE. 9. Suffixed extended zero-grade form *dhus-no- in Welsh dwn, dull brown color, whence Old English dun(n), dark-brown: DUN2, 10. Zero-grade extended form *dhubh- in Greek tuphein (< *thuphein), to make smoke, and tuphios,
428:ei-'. To go. 1. Full-grade form *ei- in: a. Latin ire, to go: ADIT, AMBIENT, (AMBITION), CIRCUIT, COITUS, COMITIA, EXIT!, EXIT?, INTROIT, ISSUE, OBITUARY, PERISH, PRAE- TOR, PRETERIT, SEDITION, SUBITO, SUDDEN, (TRANCE), TRANSIENT, (TRANSIT), (TRANSITIVE); b. Greek ienai, to go: ION; ANION, CATION, DYSPROSIUM. 2. Suffixed zero-grade form *i-t- in: a. further suffixed form *i-t-yo- in Latin initium, entrance, beginning (in-, in; see en): COMMENCE, INITIAL, (INITIATE); b. Latin comes (stem comit-), companion (< “one who goes with another”; com-, with; see kom): COUNT?; CONCOMITANT, CONSTA- BLE, (VISCOUNT). 3. Suffixed form ‘*i-ter in Latin iter, journey (> Late Latin itinerdre, to travel): (ERRANT), EYRE, ITINERANT, ITINERARY. 4. Extended form *yd- (< *yaa-) in suffixed forms *yd-no-, yd-nu- in: a. Latin Janus, archway, and Jdnus, god of doors and of the beginning of a year: JANITOR, JANUARY, JANUS; b. San- skrit ydnam, way (in Buddhism, “mode of knowledge,” “vehicle”): HiINAYANA, MAHAYANA. [Pok. 1. ei- 293.]
460:es-. To be. 1. Athematic first person singular form *es-mi in Germanic *izm/(i) in Old English eam, eom, am: AM. 2. Athematic third person singular form *es-ti in: a. Ger- manic *is#(i) in Old English is, is: 1s; b. Sanskrit asti, is: SWASTIKA. 3. Optative stem *si- in Germanic *sijai- in Old English sie, may it be (so) in gése (géa, yea; see i- + sie), yes: YES. 4. Participial form *sont-, being, existing, hence real, true, in: a. Germanic *santhaz in Old English s6th, true: SOOTH, SOOTHE; b. suffixed (collective) zero-grade form *snt-yd, “that which is,” in Germanic *sun(dj6, sin (< “it is true,” “the sin is real”), in Old English synn, sin: SIN}; c. Sanskrit sat-, sant-, existing, true, virtuous: SUTTEE; BODHISATTVA, SATYAGRAHA. 5. Basic form *es- in Latin esse, to be: ENTITY, ESSENCE; ABSENT, (IMPROVE), INTEREST, PRESENT!, (PRESENT?), PROUD, (QUINTESSENCE), (REPRESENT). 6. Basic form *es- in Greek einai (present participle ont-, being), to be (in pareinai, to be present): -ONT, ONTO-; (BIONT), HOMOIOUSIAN, PAROUSIA, (SCHIZONT). See extension esu-. [Pok. es- 340.]
486:gel-'. To form into a ball; conventional base of loosely connected derivatives referring to a compact mass or coagulated lump, and to the qualities of viscosity and adhesiveness. I. Words meaning a mass or lump. 1. Ger- manic *klamp- in Middle Low German klumpe, compact group of trees: CLUMP. 2. Germanic *klub(b)- in Old Norse klubba, a lump of wood, club: cLuB!. 3. Germanic *kliw- in Old English cliewan, a ball, ball of wool: cLEW!, (CLUE). 4. Germanic *kiid- in: a. Old English clid, hill, rock: CLOUD; b. Old English clott, lump: CLOD, CLOT, (CLUTTER); ¢. Middle High German kloz, block, lump: KLUTzZ. 5. Germanic *kiit- in Old English clit, patch (< “Jump, piece of stuff, piece of cloth”): CLouT. 6. Ger- manic *klaut- in Old English *cléat, lump, wedge: CLEAT. 7. Extended form *glob- perhaps in Latin globus, ball, globe: GLOBE, (GLOBULE); CONGLOBATE. 8. Extended form *glom- in Latin glomus (stem glomer-), ball: GLOM- ERATE, GLOMERULE; AGGLOMERATE, CONGLOMERATE. 9. Extended form *gléb- in Latin gléba, lump, clod of earth, soil, land: GLEBE. 10. Extended form *gleu- in Greek gloutos, buttock: GLUTEUS. 11. Reduplicated form *gal-gl- dissimilated in Greek ganglion, cystlike tumor, hence nerve-bundle: GANGLION. II. Words meaning to stick, cling. 1. Germanic *klupjan (< *gleb-) in Old English clyppan, to embrace, fasten: cLIp2. 2. Germanic *klimban (< *gle-m-bh-), to hold fast, hold on in climb- ing, in Old English climban, to climb: CLIMB. 3. Ger- manic *klam- in: a. Old English clamm, bond, fetter: (CLAM!), CLAM2; b. Middle Low German klam, stickiness: CLAMMY. 4. Germanic *k/amp- in Middle Dutch klampe, metal clasp: CLAMP. 5. Germanic *kleb- (< *glebh-) in: a. Old English cleofian, to stick, cleave: CLEAVE?; b. Old English clife, goosegrass (a plant with hooked prickles on the stem): CLEAVERS. 6. Germanic *kling- in: a. Old English clingan, to cling: CLING; b. Old English beclenc- an, to hold fast (be-, on all sides; see ambhi): CLENCH, (CLINCH). 7. Germanic *kluk- in Old English clyccan, to clutch: cLuTCH!. 8. Germanic kléw6, remade to *klaw6, in Old English clawu, a claw: CLAW. III. Words meaning “sticky material.” 1. Extended form *glei- in: a. Ger- manic *klajj6-, clay, in Old English clég, clay: CLAY; b. probably Medieval Greek glia, gloia, glue: GLIADIN; MESOGLEA, NEUROGLIA, ZOOGLOEA; C. Russian giei, clay: GLEY. 2. Germanic *kleg- in Danish klagge, mud, akin to the Scandinavian source of English dialectal clag, to daub with mud: cuac. 3. Extended form *gleu- in Latin gliten, glue: GLUE, GLUTEN, GLUTINOUS; AGGLUTINATE, CONGLUTINATE, DEGLUTINATE. 4. Extended form *glit- possibly in Latin glittus, sticky: GLEET. [Pok. 1. gel- 357.]
1309:BITE bheid- BITTER bheid- BITTERN! beu-2 BITUMEN gWet-1 BIVOUAC ambhi, weg-2 BLACK bhel-1 BLACKMAIL méd- BLADDER bhié-2 BLADE bhel-3 BLAIN bhlei- BLAME bha-2 BLANCH bhel-1 BLANCMANGE bhel-1 BLAND mel-1 BLANDISH mel-1 BLANK bhel-1 BLANKET bhel-1 BLARE bhié-1 BLASPHEME bha-2 BLASPHEMOUS bha-2 BLAST bhlé-2 -BLAST melst- BLASTEMA melst- BLASTO- melst- BLASTULA melst- BLATHER bhlé-2 BLAZE! bhel-1 BLEACH bhel-1 BLEAK! bhel-1 BLEAK? bhel-1 BLEAT bhlé-1 BLEMISH bhel-1 BLENCH! bhel-1 BLEND bhel-1 BLENDE bhel-1 BLENNY mel-1 BLESBOK bhel-1, bhugo- BLIND bhel-1 BLINDFOLD bhel-1 BLINI mele- BLINTZ mele- BLISTER bhlei- BLITE mele- BLITZKRIEG bhel-1, gwere-2 BLOAT bhieu- BLOND bhel-1 BLOOM! bhel-3 BLOOM? bhel-3 BLOSSOM bhel-3 BLOW! bhié-2 BLOW3 bhel-3 BLUE bhel-1 BLUNDERBUSS (s)tene- BLUSH bhel-1 BOARD bherdh- BOAST! beu-1 BOAT bheid- BOATSWAIN bheid- BOCACCIO beu-1 BODE! bheudh- BODEGA dhé-1 BODHISATTVA bheudh-, es- BoER bheue-
1390:CONFECT dhé-1 CONFEDERATE bheidh- CONFER bher-1 CONFESS bha-2 CONFETTI dhé-1 CONFIDANT bheidh- CONFIDE bheidh- CONFIDENT bheidh- CONFIGURATION dheigh- CONFIRM dher-2 CONFLAGRANT bhel-1 CONFLAGRATION bhel-1 CONFLATE bhié-2 CONFLICT bhiig- CONFLUENT bhieu- CONFORM merph-
1409:Dart dhabh- DAINTY dek-1 DAIRY dheigh- DAISY agh-2, okw- DALE dhel- DALLES dhel- DAMAGE dap- DAME deme-! DAMN dap- DAMNIFY dap- Dan? deme-! DANDELION dent- DANE dan- DANEGELD gheldh- DANELAW dan-, legh- DANGER deme-1 DaNIsH dan- DAPPER dheb- DARE dhers- DARK dher-! DASTARD dhé-2 DASYURE dens-2 DATE do- DATIVE do- DATUM do- DAUB _albho- DAUGHTER dhugheter- DAUNT deme-2 DAWN agh-2
1429:DIN dhwen- DINGUS _{enk-1 DINOSAUR dwei- DINOTHERE dwei- DIOCESE weik-! DIOECIOUS weik-1 DIOICOUS_ weik-1 DIOPTER oOkW- Dioscuri_ deiw-, ker-3 pip dheub- DIPHTHERIA deph- DIPHYODONT bheue- DIPLO- dwo- DIPLOCARDIAC kerd-1 DIPLODOCUS dek-1 DIPLOE dwo- DIPLOID pel-3 DIPLOMA dwo- DIPNOAN pneu- DIRE dwei- DIRECT reg-! DIRNDL tek- DISARM ar- DISASTER ster-3 DISBURSE bursa DISCERN krei- DISCIPLE dek-! DISCIPLINE dek-? DISCOMFIT dhé-1 DISCORD kerd-1 DISCOURSE kers-2 DISCRIMINATE krel- DIscuss kwét- DISDAIN dek-1 DISEMBOGUE beu-! DISFIGURE dheigh- DISGUST geus- DISK deik- DISMAL deiw-, mel-5 DISMAY magh-! DISMISS (s)meit(9)- DISPARATE pere-1 DISPATCH ped-! DISPEL pel-6 DISPENSE (s)pen- DISPERSE (s)preg- DISPLAY plek- DISPOSE apo- DISPUTE peu- DISQUISITION quaerere DISRUPT reup- DISSECT sek- DISSEMINATE 6-1 DISSENT sent- DISSERTATE ser-3 DISSIDENT sed-1 DISSILIENT sel-4 DISSIPATE swep-2 DISSOCIATE sekw-1 DISSOLVE leu-! DISSONANT swen- DISSUADE swad- DISTANT sta- DISTEND ten- DISTICH steigh- DISTINGUISH _ steig- DISTORT terkw- DISTRACT tragh- DISTRAIN  streig- DISTURB twer-! DITCH dhigw- DITTO deik- DITTY deik- DIURETIC wers-2 DIURNAL deiw- DIVA deiw- DIVARICATE wa- DIVE dheub- DIVERGE wer-3 DIVERT wer-3 DIvEs_ deiw- DIVIDE weidh- DIVINE! deiw- DIVINE? deiw- DIVULSION wel-4 Dizzy dheu-!
1434:DOTE dud- DOUBLE dwo- DOUBLET dwo- DOUBLOON dwo- DOUBLURE dwo- DOUBT dwo- DOUCEUR dik-u- DOUCHE deuk- poucH dheigh- DOUGHTY dheugh- DOUR deru. DOVE! dheu-1 DOWAGER dé- DOWEL dheubh- DOWER do- Down! dhino- pDowN2 dheu-! pown’ dhiino- Dowry do- DOXOLOGY dek-1 DOYEN deki DOZE dheu- DOZEN dekm, dwo- DRAB! der-2 DRAB? dher-! DRABBLE dher-! DRACHMA dergh- DRAFT dhragh- DRAG dhragh- DRAGON derk- DRAGOON derk- DRAIN dreug- DRAKE? derk- DRAMA dera- DRAMATURGE werg- DRAPE der-2 DRASTIC dere- DRAW dhragh- DRAY dhragh- DREAM dhreugh- DREARY dhreu- DRECK sker-4 DREGS dher-1 DRENCH dhreg- DRIFT dhreibh- DRILL! tere-1 DRINK dhreg- DRIP dhreu- DRIVE dhreibh- DRIVEL dher-! DRIZZLE dhreu- -DROME der-1 DROMEDARY der-1 DROMOND der-1 -DROMOUS der-1
1442:EDIBLE ed- EpicT deik- EDIFICE aidh-, dhé-1 EDIFY aidh-, dhé-1 EDITION d6- EDUCATE deuk- EDUCE deuk- EFFACE dhé-1 EFFECT dhé-1 EFFEMINATE dhé(i)- EFFERENT bher-1 EFFERVESCE bhreu-2 EFFETE dh@(i)- EFFICACIOUS dhé-1 EFFICIENT dhé-1 EFFIGY dheigh- EFFLORESCE bhel-3 EFFLUENT bhleu- EFFLUVIUM bhieu- EFFLUX bhlieu- EFFORT bhergh-2 EFFULGENT bhel-1 EFFUSE gheu- EFTSOONS apo- EGEST gerere EGG! awi-
1496:FAINT dheigh- FAIR! pek-1
1505:FEIGN dheigh- FEINT dheigh- FEIST pezd- FELDSPAR pele-2 FELICIFIC dhé(i)- FELICITATE dhé(i)- FELICITY dhé(i)- FELL! p(h)ol- FELL? pel-4 FELLATIO dhé(i)- FELLOW legh-, peku- FELO-DE-SE s(w)e- FELON2 ghel-2 FELT! pel-6 FEMALE dh@(i)- FEMININE dhé(i)- FEMTO- penkwe FEN pen-
1509:FicHu dhig¥- FICKLE pelg-2 FICTILE dheigh- FicTION dheigh- -FID_ bheid- FIDELITY bheidh- FIDUCIAL  bheidh- FIDUCIARY bheidh- FIELD pele-2 FIELDFARE wer-4 FIEND pé@(i)- FIERCE ghwer- Fiesta dhés- FIFE pipp- FIFTEEN penkWe FIFTH penkwe FIGHT pek-2 FIGMENT dheigh- FIGURE dheigh- FILAMENT gWhi- FILAR gWhi- FILARIA gWhi- FILE! gWhi- FILE? peig-1 FILES pu-2 FILIAL dh@(i)- FILIATE dhé(i)- FILIBUSTER pri- FILIFORM gWhi- FILIGREE gre-no-, g¥hi- FILL pele-1 FILLET gWhi- FILLY pau-
1727:LADY dheigh- LAG? leu-1 LAGER legh- LAGOMORPH slég- LAIR legh-
2059:-PARA pere-1 PARABLE gWelg-1 PARABOLA gW¥ele-1 PARACHUTE pere-1 PARACLETE kele-2 PARADE pere-1 PARADIGM deik- PARADISE dheigh-, pert PARADOX dek-! PARAFFIN pau- PARAGRAPH gerbh- PARALLAX al-1 PARALLEL al-1 PARALLELEPIPED ped-! PARALOGISM leg-1 PARALYSIS leu PARAMECIUM mak- PARAMOUNT ad-, per! PARAMOUR amma, pert PARANOIA nous PARAPET peg- PARAPHERNALIA bher-1 PARAPHRASE gWhren- PARAPLEGIA plak-2 PARASOL pere-1, sawel- PARATAXIS tag- PARBOIL beu-! PARCAE pera-1 PARCEL pere-2 PARCENER pere-2 PARDON d6-
2129:PRECINCT kenk-! PRECIOUS per-6 PRECIPITATE kaput PRECISE kae-id- PRECLUDE kleu-3 PRECOCIOUS pekw- PRECURSOR kers-2 PREDATORY ghend- PREDECESSOR ked- PREDICATE delk- pRepicT deik- PREDOMINATE deme-1 PREEMPTION em- PREFACE bha-2 PREFECT dhé-1 PREFER bher-1 PREFIGURE dheigh- PREFIX dhig¥- PREGNABLE ghend- PREGNANT! gene- PREGNANT? per-5 PREHENSILE ghend- PREHENSION ghend- PREJUDICE deik-, yewes- PRELAPSARIAN leb-1 PRELATE telo- PRELECT leg-1 PRELIBATION [éi- PRELUDE leld- PREMATURE ma-1 PREMIER per! PREMISE (s)meit(@)- PREMIUM em- PREMONITION men-1 PREMORSE mer-2 PREMUNITION mel-3 PREPARE pere-! PREPENSE (s)pen- PREPONDERATE (S)pen- PREPOSITION apo- PREPOSTEROUS apo- PREPOTENT _poti- PREPUCE pu-! PREROGATIVE reg-1 PRESAGE sag- PRESBYOPIA per! PRESBYTER pert PRESCIENT skel- PRESCIND  skel- PRESCRIBE skribh- PRESENT! es- PRESENT? es- PRESENTIMENT sent- PRESERVE ser-! PRESIDE sed-! PRESS! per-5 PRESSURE per-5 PRESTIGE streig- PRESUME em- PRETEND ten- PRETERIT el-1!, per? PRETERMIT (s)melt(@)- PRETEXT teks- PRETZEL mregh-u- PREVAIL wal- PREVENIENT gWa- PREVENT gWa- PREVIOUS wegh- PREVISE weld- PREY ghend- PRICE per-6
2349:TEAR? dakru- TECHNICAL teks- TECHNOLOGY teks- TECTONIC teks- TECTRIX (s)teg- TECTUM (s)teg- TEEM! deuk- TEEN? deu-3 TEETER der-1 TEETOTUM teuta- TEGMEN (s)teg- TEGMENTUM (s)teg- TEGULAR (s)teg- TEGUMENT (s)teg- TEIGLACH dheigh- 'TELAMON tele- TELANGIECTASIA ten- TELE- kwel-2 TELEKINESIS kei-3 TELEOLOGY kWel-1 TELEOST kWel-1, ost- TELESCOPE spek- TELEUTOSPORE kwel-1 TELIC kwel-1 TELIUM kwel-1 TELL del-2 TELLURIAN tel- TELLURIC tel- TELLURION tel- TELLURIUM tel- TELLURO- tel- TELO- kwel-1 TELPHER bher-1 TEMERARIOUS teme- TEMERITY teme- TEMPLE! tem- TEMPLE? temp- TEMPLES tem-
```


## [2026-09-05T20:15:43.349Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== POK -i dasyu/dahyu ==\" && grep -n -i \"dasyu\\|dahyu\\|dāsa-\\|dasa-\" POK_full.txt | head -15; echo \"== WLD ==\"; ls WLD* 2>/dev/null; ls | grep -i wld",
 "description": "Pokorny dasyu and WLD files"
}
```


### [2026-09-05T20:15:43.414Z] TOOL RESULT

```
== POK -i dasyu/dahyu ==
19234:dek-; whereas is Old Indie abhi-dasati^ is hostile, attacked ' rather Denomin. of dasa-h 
40500:(originally people, actually " owning hundred cows '), Old Indie nava-gva, dasa-gva-, 
54247:dAsyuvu) ' provide, supply ' (a- = the preposition /7-'in'); hom. 5ua-r|A£Yn^, epithet of death, 
63508:Other congruities are to name ved. astadasa- 1 8, Avestan astadase- 'the 1 8.', gr. 
83567:sedec/m:0\6 Indie s^dasa^6 (Avestan xsvasdasa-'the 16.'). 
87168:'dreizehn': Old Indie trayodasa-= Latin tredecim {*tres-decim); compare gr. rpsK^-Kai- 
== WLD ==
WLD_band3.txt
WLD_band3.txt
```


## [2026-09-05T20:15:47.222Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls incoming/ 2>/dev/null; find /home/sfmqrb/git/rishe/data/verification/sources -iname \"*WLD*\" | head -20",
 "description": "Find WLD files"
}
```


### [2026-09-05T20:15:47.294Z] TOOL RESULT

```
AHD
ARY
BLY
BQT
CEL
FFD
IRN
ISS
KGW
MAG
MFL
MON
OEW
PLA
PRT
_tessdata
TTS
TYL
VIE
WLD
ZAW
فرهنگ ریشه های زبان فارسی (2).pdf
/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt
/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD
/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt
/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf
/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf
/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt
/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt
/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt
```


## [2026-09-05T20:15:51.873Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && grep -n -i \"dasyu\\|dahyu\\|daŋhu\\|danhu\" WLD_Bd1_pages.txt WLD_Bd2_pages.txt ../../WLD_band3.txt 2>/dev/null | head -20; echo \"=== thinos / this ===\"; grep -n \"θίς\\|thīs\\|Sandhaufen\\|Gestade\" WLD_Bd1_pages.txt | head -10",
 "description": "Walde-Pokorny for dasyu / thinos"
}
```


### [2026-09-05T20:15:53.646Z] TOOL RESULT

```
=== thinos / this ===
1244:yvuara alyag ev rf] ovvydsig ley oyer 4 j), uiyiaXog „Gestade“ (wohl nach
78542:   Auf Grund der Bed. „(zusammen)wirbeln“ 'dig, divog „Sandhaufen, bes.
78543:Diine, Gestade, Sandbank, Sandsteppe, Sand auf dem Meeresgrund, Schlamm;
78549: aufgeworfener Sandhaufen am Meeresufer", ntries. sniediien „Schneehiigel“
79919:f. „Sandbank, Gestade, Insel“ (nicht besser als „Hie6ender, fliegender Sand
```


## [2026-09-05T20:15:56.326Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && sed -n '78520,78560p' WLD_Bd1_pages.txt",
 "description": "Walde-Pokorny on Greek this/thinos"
}
```


### [2026-09-05T20:15:56.372Z] TOOL RESULT

```
und anord. djlja „schiitteln“ Neubildung ist; in der Bed. „rase“ vielleicht
aus *dhusio, s. *dheues- ), hvdo>, {tvaCco ds., i) vsXXa ,, Sturm" (s. u. *dheiies-),
ep. duvco „fahre einher, stiirme daher“ (*i9vvfo) oder *&vvia>1 Brugmann
II 2 3, 301, 326), &vvea> ds. (= ai. dhunayati oder aus *&vvefcnl Brugmann
II 2 3, 246, 269), dvvog noXejuog, dg/uy, dgoyog Hes. Mit der Bed. „rauchen
                                              •


(Rauchopfer), riechen" (Lit. bei Boisacq 360, unberechtigter Zweifel bei
Schulze Qu. ep. 330: dvco {&voco, tedvy.a „opfere“ (bei Horn, nur vom un-
blutigen Rauchopfer; dvota „Opfer“,    dvya „Opfertier"), dvog n. „Raucher-
werk (daher lat. tils), Opfergabe, Opfer" (davon dvela „Morser“? s. Boisacq
m. Lit.) dvoeig, dv/jeig „von Opferdampf oder Raucherwerk duftend", dvov
„ein Baum, dessen Holz wegen seines Wohlgeruches verbrannt wurde",
{hia, dva „Thuya", ’dvrjXy „Opfergabe, blutig oder unblutig" ( jon. dvaly-                              :



yaxa     :   att. dvbjyaTa,                 *dvfa-     :
                                                           *&€-, s. Bechtel Lex.     1   68 f., Boisacq s. v.), 9v-
fiekr]   „Opferstatte, Altar" ( ? s. zur Bed. Aly Gl. 5, 60, Kretschmer Gl. 6, 306).

   Auf Grund der Bed. „(zusammen)wirbeln“ 'dig, divog „Sandhaufen, bes.
Diine, Gestade, Sandbank, Sandsteppe, Sand auf dem Meeresgrund, Schlamm;
Haufen iiberhaupt, Erhebung" aus          gebildet wie axjtv-, yt.or/lv-, dsX-
rptv-,       (bdtv-,             vgl. zur    Bed. mnd. dime, nnd. (daraus hd.) Diine, ahd. duna
„promontoriuin, rupes in maris litore prominens" (alter „Diine, Sandbank"),
ags. dun „Hiigel, Berg" (nicht aus ir. dun „feste Stadt" = gall, dunum ,
dt. Zaun), engl. down „Sandhiigel, Diine, Hiigel", mndl. dune „vom Wind
 aufgeworfener Sandhaufen am Meeresufer", ntries. sniediien „Schneehiigel“
 (so auch lett. duhi, diihas „Schlamm“? s. o., und anord. dy „Schlamm“?).
 S. zu dieser Bedeutungsgruppe Persson Beitr. 43, Falk-Torp u. dyne II,
 Boisacq u. dig (wo fiber altere Auffassungen von dig und Diine) und vgl.
 zur Bed.                 klr.    vy-dma „Diine“ zu slav. dmnq „blase".
    Alb. (G. Meyer Alb. Wb. 62 f.) geg. dej,                                 tosk.   den „berausche“              ( *denio

 idg. *dheu-n-, vgl. got. dauns „Dunst").

    Lat. suf-fio, -fire „rauchern“ (suff intention „Raucherwerk"; iiber fimus
 s. o.) aus *-dhu-iio, wie fio „werde“ aus *bhu-iio (s. Yf. LEWb.
                                                                    2
```


## [2026-09-05T20:16:06.697Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Sandhaufen\" POK_full.txt POK_01.txt POK_02.txt | head -10",
 "description": "Pokorny Sandhaufen (this)"
}
```


### [2026-09-05T20:16:06.751Z] TOOL RESULT

```
POK_01.txt:3771:Auf  Grund  der  Bed.  , (zusammen) wirbeln'  d-tg,  ^ivög  , Sandhaufen,  bes. Düne,  Gestade,  Sandbank,  Haufen  überhaupt',  aus  ^d-f-iv,  gebildet  wie a-A-ttv-,  yliotiv-,  ösXcptv-,  chötv-,  vgl.  gr.  ^iXa  ,Haufen'  (Hes.),  zur  Bed. unten  nhd.  Düne;  kaum  mit  Schwyzer  Gr.  Gr.  I  570 ^  zu  ai.  dhisnya-  ,auf einen  Erdaufwurf  aufgesetzt';
```


## [2026-09-05T20:16:07.315Z] TOOL CALL #57: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-05T20:16:07.320Z] TOOL RESULT

```


```


## [2026-09-05T20:16:14.122Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('POK_01.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\npos=sum(len(l)+1 for l in lines[:3770])\nleaf=t[:pos].count('\\f')\nprint('leaf',leaf,'-> printed page',leaf-8)\n# print the root headword above\nimport re\nfor i in range(3770,3700,-1):\n    if re.match(r'^\\s*dheu', lines[i]) or 'dheu-' in lines[i][:40]:\n        print(i+1, lines[i][:200]); break\nprint('\\n'.join(lines[3765:3775]))\nEOF",
 "description": "Pokorny page for this/thinos"
}
```


### [2026-09-05T20:16:15.741Z] TOOL RESULT

```
leaf 274 -> printed page 266
3745 4.  dheu-,  dheuO'  (vermutlich:  dhue-,  vgl.  dio  Erw.  dhue-k-,  dhä-s-)  ,stieben, wirbeln,  bes.  von  Staub,  Rauch,  Dampf;  wehen,  blasen,  Hauch,  Atem; daher  dampfen,  ausdünsten,  rieche
ai.  dhünöti  {dhunöti,  dhuvdti)  ^schüttelt,  bewegt  hin  und  her,  facht  an', Fut.  dhavisyatij  Perf.  dudhäva,  Pass.  dhüydte,  Partiz.  dhutd-h,  dhütd-h  " ,geschüttelt^,  mpers.  dlt  , Rauch';  ai.  dhunäti  ,bewegt  sich  hin  und  her, schüttelt',  Partiz.  dhünäna-,  dhüni-  f.  ,das  Schütteln',  dhünayati  ^bewegt hin  und  her,  schüttelt^,  dhavitram  n.  ,Fächer,  Wedel',  dhavitavyä-  ,anzu- fächeln';  av.  dvaidi  ,wir  beide  bedrängen'?  {*du-vaidl)'^  Kuiper  Nasalpräs. 53  stellt  hierher  ai.  dhvajati  (Dhp.  7,  44),  av.  dvazaiti  , flattert^  (dazu  ai. dhvajd-h  ,Fahne')  aus  *dhu-eg- (?)',
arm.  de-dev-im  , schwanke,  schaukle'  (vgl.  das  ebenfalls  redupl.  Intensiv dhvajd-h  ai.  dö-dhavUi);
gr.  d-icü  (ßdvaa),  lesb.  d^vio) , stürme  einher,  brause,  tobe,  rauche'  {*dhu-iö, V  aus    d^awj   edvaa,   wie   auch   ü   im   ai.  Pass.  dhüydte   und   anord.  dyja    g ,schütteln'   Neubildung   ist;    in   der   Bed.   ,rase'   vielleicht   aus  *dhusiö,  s.  /^ dheues-),  ^vduj,  dvd^w  ds.,  MeXka  ,Sturm'  (s.  S.  269  unter  dheues-),  ep.  divot  j% ,fahre  einher,  stürme  daher^  {^d-vvJ^w),  d^Vvew  ds.  {^-^viifu)),  ^vvog'  ndh- fiOQy    ÖQ^irj,    ÖQÖLiog   Hes.    Mit   der   Bed.    , rauchen    (Rauchopfer),   riechen': -d^Vü)    (^ö-w),    Ts&vyta    ,opfere',    -d-vaia  , Opfer',    ^i(j,cc    ,Opfertier^,  ^vog  n. , Raucher  werk  (daher  lat.  tüs),  Opfergabe,   Opfer'  (davon  ^veia  ,Mörser'?
263
s.  Boisacq  m.  Lit.),  &vÖ£Lg,  d-vrjSiq  ,von  Opferdarapf  oder  Räucherwerk duftend';  S-vov  ^ein  Baum,  dessen  Holz  wegen  seines  Wohlgeruches  ver- brannt wurde',  dv'ia,  &va  ^Thuja',  ^vrilrj  , Opfergabe'  (:ion.  d-valrj^iara -. att.  ^Irj^ccra,  ^^fa-i'^^v-,  s.  Bechtel  Lex.  168  f.,  Boisacq  s.  v.),  dvy,ih] Opferstätte,  Altar'.
Auf  Grund  der  Bed.  , (zusammen) wirbeln'  d-tg,  ^ivög  , Sandhaufen,  bes. Düne,  Gestade,  Sandbank,  Haufen  überhaupt',  aus  ^d-f-iv,  gebildet  wie a-A-ttv-,  yliotiv-,  ösXcptv-,  chötv-,  vgl.  gr.  ^iXa  ,Haufen'  (Hes.),  zur  Bed. unten  nhd.  Düne;  kaum  mit  Schwyzer  Gr.  Gr.  I  570 ^  zu  ai.  dhisnya-  ,auf einen  Erdaufwurf  aufgesetzt';
alb.  geg.  dej,  tosk.  denj  ,berausche',  Med.  ,schwinde  dahin,  schmelze' (*deuniö,  vgl.  got.  dauns  , Dunst'),  dejet  ,fließt,  schmilzt';
lat.  siif-fiö,  -flre  , räuchern'  {sufflmentum  ,Räucherwerk';  über  fimus s.  oben)  aus  *-dhu-nö,  wie  fio  ,werde'  aus  ^hhu-iiö,  foeteo,  -ere  ,übel  riechen, stinken'  auf  Grund  eines  Partiz.  *dJm-oi-to-s  (wie  püteö  von  *pütos)]
hierher  (als  *Aufgeschüttetes)  gall.,  urir.  Jovvov,  latin.  dünum,  air.  n. «-St.  dün  (:lat.  fünus,  s.  S.  260)  ,Burg'  (*Hügel),  acjmr.  din  (ncymr. dinas)  ds.;  air.  dü[a)e,  arch.  doe  ,Wall'  (*dhöuio-);  air.  dumae  m.  , Hügel', gall.  GN  Dumiatis]  auch  air.  de  f.  Gen.  d'lad  , Rauch',  mir.  dethach  ds. (^*dhuiiat-) ;
ags.  dün  m.  f.  ,Höhe,  Berg',  engl,  down  , Sandhügel,  Düne',  mnl.  düne, mnd.  düne,  daraus  nhd.  Düne]  vgl.  zur  Bedeutung  klr.  vy-dma  ,Düne'  zu slav.  d^mq  , blase';  hingegen  ist  germ.  *tü-na-  ,Zaun,  eingehegter  Platz' (aisl.  ags.  tun  ds.,  , Stadt',  nhd.  Zaun)  wohl  kelt.  Lw.;
```


## [2026-09-05T20:16:25.213Z] TOOL CALL #59: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/dahyu%C5%A1",
 "prompt": "Give the full etymology section verbatim: what Proto-Indo-Iranian / PIE etymon is given for *dahyuš, its meaning, and the list of descendants (Avestan, Old Persian, Middle Persian, New Persian, Sogdian etc.). Quote exactly."
}
```


## [2026-09-05T20:16:26.755Z] TOOL CALL #60: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%D9%87#Persian",
 "prompt": "For the Persian entry ده (deh) 'village': quote the etymology verbatim (Middle Persian, Old Persian/Avestan ancestors, any PIE root), and any derived terms such as دهقان, دهات, دهخدا, دهکده, دهستان."
}
```


### [2026-09-05T20:16:27.268Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-05T20:16:37.366Z] TOOL RESULT

```
# Persian ده (deh) - Village Etymology and Derived Terms

**Etymology:**
The word traces back through "Middle Persian _[𐭬𐭲𐭠](/w/index.php?title=%F0%90%AD%AC%F0%90%AD%B2%F0%90%AD%A0&action=edit&redlink=1 "𐭬𐭲𐭠 (page does not exist)")_ (MTA /⁠deh⁠/, "village"), from Old Persian _[𐎭𐏃𐎹𐎠𐎢](/wiki/%F0%90%8E%AD%F0%90%8F%83%F0%90%8E%B9%F0%90%8E%A0%F0%90%8E%A2#Old_Persian "𐎭𐏃𐎹𐎠𐎢")_ (d-h-y-a-u /⁠dahạyau⁠/), from Proto-Iranian _[\*dáhyuš](/w/index.php?title=Reconstruction:Proto-Iranian/d%C3%A1hyu%C5%A1&action=edit&redlink=1 "Reconstruction:Proto-Iranian/dáhyuš (page does not exist)")_ ("Village")."

**Derived Terms:**
- [دهات](/wiki/%D8%AF%D9%87%D8%A7%D8%AA#Persian "دهات") (dehât, "countryside")
- [دهخدا](/w/index.php?title=%D8%AF%D9%87%D8%AE%D8%AF%D8%A7&action=edit&redlink=1 "دهخدا (page does not exist)") (deh-xodâ, "sheriff, village leader")
- [دهقان](/wiki/%D8%AF%D9%87%D9%82%D8%A7%D9%86#Persian "دهقان") (dehqân, "farmer, landlord")
- [دهچه](/w/index.php?title=%D8%AF%D9%87%DA%86%D9%87&action=edit&redlink=1 "دهچه (page does not exist)") (dehče, "peasant")
- [دهک](/w/index.php?title=%D8%AF%D9%87%DA%A9&action=edit&redlink=1 "دهک (page does not exist)") (dehak, "hamlet")
- [دهکده](/w/index.php?title=%D8%AF%D9%87%DA%A9%D8%AF%D9%87&action=edit&redlink=1 "دهکده (page does not exist)") (deh-kade, "small village")
```


## [2026-09-05T20:16:41.717Z] TOOL CALL #61: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%F0%90%8E%AD%F0%90%8F%83%F0%90%8E%B9%F0%90%8E%A0%F0%90%8E%A2",
 "prompt": "Quote the Old Persian entry for dahyu- (d-h-y-a-u): meaning, etymology (Proto-Iranian, Proto-Indo-Iranian, Sanskrit cognate dasyu), and descendants."
}
```


## [2026-09-05T20:16:43.785Z] TOOL CALL #62: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%D9%87%D9%82%D8%A7%D9%86",
 "prompt": "Quote the etymology of دهقان (dehqān) in Persian and in Arabic: Middle Persian dēhgān, the Arabic borrowing دهقان/دهاقين, and the re-borrowing into Persian. Also any note on the historical meaning 'landowner, Iranian gentry'."
}
```


### [2026-09-05T20:16:47.085Z] TOOL RESULT

```
# Old Persian Entry: dahyu-

**Meaning:** The term denotes "land" or "country," as demonstrated in an inscription from Ariaramnes (c. 640-600 BCE) stating: "This is the Persian **land** which I hold."

**Etymology:** The word derives from Proto-Iranian *dáhyuš, which traces back to Proto-Indo-Iranian *dásyuš, ultimately from Proto-Indo-European *des- meaning "enemy, foreigner."

**Sanskrit Cognate:** दस्यु (dásyu), meaning "stranger" or "foreigner."

**Descendants:** The term evolved into Middle Persian 𐭬𐭲𐭠 (mtʾ /deh/), which subsequently developed into Modern Persian ده (deh).
```


### [2026-09-05T20:16:50.208Z] TOOL RESULT

```
# Etymology of دهقان (Dehqān)

## Middle Persian Origin
The word traces back to Middle Persian *dhywkʾn'* (/dahigān/), meaning "countryman, farmer."

## Arabic Borrowing
Arabic borrowed this term as **دِهْقَان** (dihqān), developing meanings including "dehqan, publican" and "alekeeper." The plural form is **دَهَاقِين** (dahāqīn).

## Persian Re-borrowing
Persian received the word back from Arabic as **دهقان** (dihqān/dehġân), though it also retained the form **دهگان** (dehgân) from the original Middle Persian.

## Historical Significance
In historical contexts, the term denoted a **"dihqan"—a local aristocrat in late Sasanian and early Islamic Iran.** This referred to land-owning magnates who constituted Persian gentry during that period. By extension, it could designate Persians/Iranians as opposed to Arab and Turkish populations.

The word's journey reflects linguistic and cultural contact across the Middle East, moving from Persian administrative vocabulary into Arabic and back into Persian with both common and elite connotations.
```


## [2026-09-05T20:16:58.674Z] TOOL CALL #63: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%B8%CE%AF%CF%82",
 "prompt": "Quote the Ancient Greek entry θίς: meaning and etymology (what PIE root is given, Beekes' view, whether it is connected to any Iranian word for village)."
}
```


## [2026-09-05T20:16:59.650Z] TOOL CALL #64: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%D9%87%D8%A7%D8%AA",
 "prompt": "Quote the etymology of دهات (dehāt) in Persian: is it an Arabic-style broken plural of ده? Also give the meaning. And any note on دهاتی."
}
```


### [2026-09-05T20:17:04.964Z] TOOL RESULT

```
# Ancient Greek Entry: θίς

**Meaning:** The word θίς (thī́s) is a masculine noun referring to a heap (especially of sand), beach, shore, sandbank, bar at a river mouth, sand or mud at the sea bottom, or shoreweed.

**Etymology:** According to the Wiktionary entry, "Beekes suggests a Pre-Greek origin" due to the implausibility of alternative explanations. The document does not identify any specific Proto-Indo-European root or connection to Iranian vocabulary for village. The etymology remains uncertain, attributed to a substrate language predating Greek rather than Indo-European ancestry.
```


### [2026-09-05T20:17:06.547Z] TOOL RESULT

```
# Etymology and Meaning of دهات (dehāt)

**Etymology:** The word is formed from "ده" (village) combined with the Arabic suffix "ات". According to the source: "_ده_ ("village") +‎ Arabic _ات_."

**Meaning:** The term denotes either the countryside/rural areas or villages collectively.

**Note on دهاتی:** The derived term دهاتی (dehâti) means "villager"—a person from a rural or village setting.
```


## [2026-09-05T20:17:22.002Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"vispa.dahyu\\|vispö.dahyu\\|vTspa.*dahyu\\|vispanqm  dakyunqm\\|vispanqm dahyunqm\" BRT.txt | head -10; echo \"=== vis- 'all' compounds in BRT ===\"; grep -no \"vTsp[a-zöäü.]*dai\\?[nñh]h*[uy][a-z]*\" BRT.txt | head -20",
 "description": "Search Bartholomae for vispa-dahyu"
}
```


### [2026-09-05T20:17:22.064Z] TOOL RESULT

```
11071:Glieder  sind  verbal:  yBi  ztjvä  (nämL  hitOt) *ar»har3La  bvanticS{sA)\.4^.T.  3)bci allen;  a)  D  im  Ap.;  das  letzte  Mal  steht Uta  statt  cä:  pärsamcä  mädamcä  utä  aniyä dakyiivaf"  Bh.  /.  14.  b)  im  Aw,;  i)  die Glieder  sind  nominal ;  a)  sie  folgen  sich  un- mittelbar: nmänyasca  visyasca  santumasca Y.  if).  18  (s.  dazu  18  aA.);  —  aojasca  v»ty- 'inmca  j^armas^a  lavania  Y.  7/.  8 ;  —  sta- rasca  mäsca  >fe'<i/vi-'(7  YL72,25(s.dagegeni_j. 57);  —  vätftnca  vänmca  tnafy^mca  Jyau- humca  Yt  5.120; — hubprvtlmca  uslaMin- tlmca  vanta.bintTmca  Y.  61. 2  (s.  dagegen  7 ; Sp.  570U.);  —  maziUäsca  vahiitasca  srais- tas^a  asayS  Y.  52.  3;  —  apasca  urvaräsca xadirdsca  Y. A3;  —  asavafom  htnümca bavaniiinla  busyantimla  Yr.lS.i; — vTspayä ..slöis  haihyJica  bavqihyäica  büiyqi^yäica \.6S.i3i  —  nm3nanqmcä  vlsqm^a  satttu- nqmca  dahyunqmca  Y.  Ä  7 ;  —  damayä  anu- matayal'a  aiiuxtayaica  * aim.varstayai^a Y.Ä7;  —  d^aurunqscä  rä^aistiscä  väs- tryqscä  ßuyants  Y.  ig.  3;  Yt  ig.  8;  — ahamca  ratümca  paoirimca  tkaisim  Yt/^J. 152;  —  ha^ra  miiräca  rasnuta  uyraca dämSis  upamana  Yt/_J.  47;  —  vispss^a paiti  vansajls  vTspSsca  paiti  frasparrjJ i'JspSsca  paiti  fravaxsS  Y.  jo.  5 ; — haurva- tasca^  fiö  am)r>täta  gSuica  taSnB  gSusca urunS  ä%rasi-a  aoxtsjiämand  hadisasca  Vr. g.  5;  —  beim  Zahlwort:  navaia  navaittfca navaca  sota  navaca  Aazavra  navasSsca baivqn  Yl;_J.S9.  a)mitTmesis:*«ai/x
17821:yemi  , ,  imat  am>ia  spptita  .  .  imat  asäu- nqm  varguAls  °iays  (VP.)  Wjra  aiiuihüra Y.  65. 1 2 ;  Ny.  /.  I ;  —  aora  varmkis  upa.- sa^a  .  .  äps  .  .  urvarä  .  .  tüäunqm  fra- vasays  Yt  13. 147;  1. 9,  10. 100,  H.  34,  y, 79,  FrW. /.  3;  —  jamyqn  i^ra  asäunqm .  ,  'iaylf  asöis  basfaza  hacimnä  . .  istSe *vadhar»Aqm  paitiHätSe  ätaranqm  Y.  60. 4;  —  qpqmea  .  .  urvaranqmca  .  ,  asao- nqmla  'hnqm  yasnsm  Vr. 21.  \;  —  yS nä  his  hubinta  *barat  jva  a?aonqtn *says  (als  AP.)  sästa  .  .  hö  anhaiti  za- sulttmS  Yt  /J.  1 8 ;  —  fravasayS  .  .  yä a/raourvisvat  k?r»navainti  irsm  yahmya jaanti  Yt.  y.  26;  —  -says  . .  ya  ahurahe xsayats  dasinqm  upa  yü&yänti  yezi  aim bavaiti  ^alavaxsnuiW.  13. 63  ;  — frasüSTnii uyrä  asäunqm  'fayS  paoirij'  pouru^sata .  .  pouruAatanra  .  .  pouruiasvanS  apitii ashntnä  haväi  käcil  näfäi  . .  tä  yü^yeinti pfianähu  have  asahi  Yt  l^.  65if.;  —  "sayS .  .ya  avai  trayS  aiwyaxsayänti  yat  vouru- kahm  ..yä  ave  strjui  atwyäxsayeinti yqm ^haptöiringS  ..ya  avqm  k^hrpim  aiwyäxsa- yänti  yqm  .  .  hnsäspahe  .  .  ya  avqm *x^rqm  (sd)  aiwyäxSayänti  yqm . .  tara- 'huStrahe  navaca  navaitlsla  navaca  sota nava^a  hatattra  navasSs^a  baevqn  Yt  13. 59—62;  —  "iayS  .  .  yä  vts^&a  ävayänli hamaspa>:maedaim  paiti  ratüm  äat  a^ra vtcar?nii  dasa  pairi  xsa/nö  Yt/J.  49;  — asSunqmcä  'HbyS  yä  nS  iltä  urvSibys  Y. 5Ö.  2 ;  —  asäunqm  '/is  narqmcä  näiri- nqmcä  yazamaidl  Y.^7. 3;  —  °fayS  yä paeirya  (sd.)  anhan  Y.  23.  \;  —  äyeseyesti "vTspaya  asavane  'se"  Y,  2_j.  3;  —  vTspä °iayS  (als  AP.)  asäunqm  yazamaide  ädah- *yunqmca ..  'say5 ..*u%dahyunqmla . .  °iayS.. narqmca  ..'^ayD  ..näirinqmfa  ..  °sayS  yaza- maide  Vr.l6.  2;  7.  i,  10.2,  16.  i;  —  nabä- nazdiäanqm  para.iristanqm  aliirapaitinqm a!>iryanqm  narqm..näirinqm  'iayff  yaza- maide  Y.  26.  T,  8  ff.";  —  a/äunam  "sayd .  .  nmänyä  visya  zantumä  däAyumä  zara- ^ustrSJpmä  Y.  ly.  18;  —  airyanqm'  .  . /ßityanqm'  .  .  sairimanqm'  .  .  säininqm' . .  dahfnqm' . .  vTspanqm'  dakyunqm  narqm .  .  näirinqm  .  .  °sayö"  yasamaide  Yt  13. 143—145;  —  fä  'sayU  .  .  aoßstA  hittti  .  . ya  paoiryanqm  tkaihnam  ya  vä  narqm azätanqm  /rais.car>^rqM  saoiyantqm  Yt. y.i7;'Y./.i8',  23.2,  24.5;  —'  vjipä .  .  'Iay3  .  .  yä    haca   gayät    mariihnai   ä
25852:anhSus  dam^rJi  (sd.)  A^  aMya  frärmts Vfrttdäis  sSnghüis  'yantqm  xratavS  (sd.) Y.  4ß.  3 ;  —  tim  adväntm  . .  dagna  'yantqm ya  . .  urväxs'at  (Sp.  1536  o.)  . .  mXid>m  Y. 34. 13;  —  ai  lOi  ai»h»n  'yantS  daHyunqm''^ ySi  x^nüm  (sd.)  .  .  kaäntl  "die  sind  die Retter  der  linder,  welche  . ."  Y.  4^. 12.  b)  im  jAw.;  i)  Plur-,  im  Sinn  von A  2,  von  den  Priestern  als  den  Fortsetzem des  «tfra^MÄrischen  Rettungswerks:  y3- varanS  as  tard^ustrS  . .  kavä  viftäsps  .  . kas!u  'yantam  Aaihyavarpxqm  *asaafiqm Y.12.1;  —  ia^a  *drußm  ..  nT/.na/ama? nTs.nas(lma  'yantS  *drujim  "..  als  S.  werden wir  die  Dr.  wegschaffen"  Y.  61.$;  —  buyama 'yantS  buyama  v»r>%rä)anö  buyama  ahu- rahe  matdh  . .  astayS  (sd.)  Y.  70.  4;  —  yBi taxma  'yantS  ydi  taxma  vpiv^rü/anS  Yt '3-  38;  —  äinaca  manh  asaonqm  Ssnaca manä  yantqm  Vr. //.  3;  Yt /J.  74;  — ya%aca  ximavSya  ahm  Hnaitt  yal  *'yan- tibyS*^  Y.  20. 3;  —  aitm  . .  y3  vtspanqm •yantqm  fraia  (sd.)  xra'^wa  fra^anjayeiti Ytiy.a;  —  nmanake..yeAhe  vatm  maM (Sp.  270  o.)  ySi  'yanis  dahyunqm  Vi.  11. iji);  —  yaha  (Sp.  1246  o.)  lia  v/lam nilslma  ya^a  vä  'yantS  dahyunqm  Y.
=== vis- 'all' compounds in BRT ===
```


## [2026-09-05T20:17:51.558Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\ni=13094\n# search backwards and forwards for 3-digit column numbers\nfor j in range(i-25,i+15):\n    l=lines[j]\n    if re.search(r'(?m)^\\s*7[01][0-9]\\s*$', l) or re.match(r'^\\s*\\d{3}\\s*$', l.strip()):\n        print('colmark line',j+1,repr(l.strip()))\nprint('---- entry ----')\nprint('\\n'.join(lines[13090:13100])[:2500])\nEOF",
 "description": "Find Bartholomae column marker near dahyu"
}
```


### [2026-09-05T20:18:12.908Z] TOOL RESULT

```
colmark line 13071 '706'
colmark line 13097 '707'
colmark line 13100 '708'
---- entry ----
Pü. ;  dahmän  nikait,  erl. :  pa  sardär  däsl  fstel ;
•  j.  dahmö-yaozdäta-  Adj.  (fem.  'tä-) 'von  (einem  oder)  den  D.  richtig  bereitet*: zad^ranqm  .  .  °tanqm  V.  14.  4.
Pü. ;  dahmän  ySidäsrenll,  erl.:  dahmän  tart.
•  p.dahyav-,  j.damhav-(,  dai)h°,  danh'),
j,,  g.  dahyav-''  j  dahyu-^''  f  'Landgebiet, Landschaft,  Land',  oft  zugleich  auch  von den  Bewohnern;  a)  im  Aw.:  haraiti  bars .  .  hama  psirisäite  fräpayä  (sd.)  °rihus  ä upaola>ihvasca  Yt ig-\;  —  kahrkasS  .  . yS  naotnyä{sd.)cit  haca  'hihaot  .  .  xrUm aiwi.va&iaiti  Yt.  14.  33;  — par3  *S3mS  al- tanßta  *'iih3us^  anhat  b>rptd{s^)  7-i}sir?m V.  2. 24;  —  nSii  ..  asar?hal:a  /i^fyraf/a 33
dby  Google
707
dahyav-  A  I
dahyav-  A II
708
```


## [2026-09-05T20:18:21.888Z] TOOL CALL #67: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%AF%D9%87/",
 "prompt": "Quote the فرهنگ معین (Mo'in) section for the headword ده: give the entry text including any bracketed origin tag such as [په.] or [پهلوی] and the definitions (قریه, روستا). Also quote the لغتنامه دهخدا section if it cites برهان قاطع or an etymology."
}
```


## [2026-09-05T20:18:22.959Z] TOOL CALL #68: WebFetch

```json
{
 "url": "https://archive.org/stream/oldpers/oldpers_djvu.txt",
 "prompt": "Find the lexicon entry \"visadahyu-\" in Kent's Old Persian. Quote it verbatim including the gloss and the inscription reference (XPa), and any nearby page number."
}
```


### [2026-09-05T20:18:28.114Z] TOOL RESULT

```
# Entry for ده from Farhang-e Mo'in

According to the **Farhang-e Mo'in** (Mo'in Dictionary) section, the headword ده has two main definitions:

**(دِ) [په.] (اِ.)** روستا، آبادی کوچک
**(دَ) [په.] (اِ.)** عدد اصلی پس از نه

The bracketed tag [په.] indicates a Pahlavi origin. The first entry defines it as "village" or "small settlement," while the second defines it as "the cardinal number ten."

---

# Reference to Loghat-name Dehkhoda

The **Loghat-name Dehkhoda** section traces the term to classical sources, citing **Burhan-e Qate'** as an etymological authority. It identifies the word as عشره (the Arabic term for ten) and provides extensive classical poetry citations demonstrating historical usage across Persian literature.
```


### [2026-09-05T20:18:29.081Z] TOOL RESULT

```
I've searched through the provided content, but I cannot locate a lexicon entry for "visadahyu-" in this document excerpt. The text includes the table of contents, foreword, chapters on linguistic setting, script, phonology, and grammar, but the actual lexicon section (Part III) begins on page 164 and is not fully reproduced in the material provided.

To find this specific entry with its gloss and XPa reference, you would need to consult the complete Lexicon section starting on page 164 of Kent's work.
```


## [2026-09-05T20:18:37.587Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad; curl -s \"https://archive.org/metadata/oldpers\" | python3 -c \"\nimport json,sys\nd=json.load(sys.stdin)\nprint(d.get('server'), d.get('dir'))\nprint([f['name'] for f in d['files'] if f['name'].endswith(('.txt','.djvu','.xml','.pdf'))][:20])\n\"",
 "description": "archive.org metadata for Kent"
}
```


### [2026-09-05T20:18:39.891Z] TOOL RESULT

```
ia600101.us.archive.org /20/items/oldpers
['oldpers.pdf', 'oldpers_djvu.txt', 'oldpers_djvu.xml', 'oldpers_files.xml', 'oldpers_meta.xml', 'oldpers_scandata.xml']
```


## [2026-09-05T20:18:43.393Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad; curl -s -o kent.txt \"https://ia600101.us.archive.org/20/items/oldpers/oldpers_djvu.txt\" -w \"%{http_code} %{size_download}\\n\"; grep -n -i \"visadahyu\" kent.txt | head -10",
 "description": "Download Kent djvu text and search visadahyu"
}
```


### [2026-09-05T20:18:45.909Z] TOOL RESULT

```
200 944060
5441:pIE *yikuo-, OP visa- ‘all’, also in visadahyu-; 
9417:yava’um; Babirum, Margum; visadahyum; per- 
9506:find -dahyum in visadahyum (or -dahyaum, as 
9922:sg. masc. visadahyu-m (§§180-3). The consonantal 
20694:12 Auramazdáhà : imam : duvarfim : visadahyum 
26615:$166). Decl., 5183.1. See also visadahyu-. 
29039:haruva-; 5150). See also visadahyu-, and cf. viba-, 
29045:visadahyu- adj. ‘of or for all countries or 
29049:ince’. visadahyum asm. (§53, 418811) XPa 12.
```


## [2026-09-05T20:18:49.430Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad; sed -n '29030,29060p' kent.txt; echo \"=== page markers nearby ===\"; awk 'NR>28900 && NR<29120 && /^[0-9]{3}$|LEXICON|OLD PERSIAN/ {print NR\": \"$0}' kent.txt",
 "description": "Kent visadahyu entry and page"
}
```


### [2026-09-05T20:18:51.520Z] TOOL RESULT

```
connected with Av. vi-vah-vant- the father of Yima, 
Skt. vivásvant-, $131; despite Bthl. AiW 1452, Hz. 
AMI 1.88.п2). Vivána nsm. DB 3.55, 78. Vi- 
vanam asm. DB 3.58, 60, 65, 71. 


visa- adj. ‘all’: OP (Med.) vispa-, Av. vispa-, 
Skt. víóva-, pAr. *yiSya- (800) for pIE *uiko- 
(OCS vist ‘all’) after -ya- in (Skt.) sdrva- (see OP 
haruva-; 5150). See also visadahyu-, and cf. viba-, 
vispa-.  visahyü gsm. DSa 5; DS} 6. visam nsn. 
DSj 4°; DSI 5. visam asn. DNa 49; DSf 21; DSi 
4°; XPa 16; XPb 25f; XPf 42; XPh 44. 


visadahyu- adj. ‘of or for all countries or 
provinces’ ($161.Па): borrowed in Elam. mz-25- 
ía-da-a-hu-i$ and (with Med. vispa-) Akk. u~- 
1$-pt-da-a-'-1; visa- ‘all’ + dahyu- ‘country, prov- 
ince’. visadahyum asm. (§53, 418811) XPa 12. 


vispa- adj. ‘all’: Median (49.11, $90) for OP 
visa-, q.v. See also wtspazana-. vispā absn. 
A%Sa 5°; Ada 4, Аас 4 (iispa db, $55.1); 
A?Ha 6°. 


vispazana- adj. ‘containing all (kinds of) men’ 
($101.09): borrowed in Elam. mi-iš-ša-da-na, 
from the OP form *visadana-: Med. vispa- ‘all’ + 
=== page markers nearby ===
29000: OLD PERSIAN 
29065: LEXICON 200
```


## [2026-09-05T20:19:00.354Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad; sed -n '28995,29005p' kent.txt; echo ...; sed -n '29060,29070p' kent.txt",
 "description": "Kent running heads"
}
```


### [2026-09-05T20:19:00.424Z] TOOL RESULT

```
Vidarna- sb. ‘Hydarnes’, a Persian, ally of 
Darius against Gaumata: Elam. mi-tar-na, АКК. 
ui-mi-da-ar-na-’, Gk. ‘Todpvns. Perhaps vi- ‘apart’ 


OLD PERSIAN 


+ dar- ‘hold’, as ‘Support, Security’ (831, 41471, 
4164.1, IV), cf. Av. vi-dar- ‘hold apart, support’, 
-darana- ‘stronghold, place of resort’ (Bthl. AiW 
...
from the OP form *visadana-: Med. vispa- ‘all’ + 
Med. zana- ‘man, human being’ ($9.11, §88, $90). 
uspazananim gpf. DNa 10Ї; DSe 9f; DZc 5. 


LEXICON 200 


Vistaspa- sb. ‘Hystaspes’, father of Darius: 
Elam. mi-iš-da-aš-ba, Akk. wufia-as-pa, Gk. 
‘Loraonns. Prior element višta- perhaps pte. of
```


## [2026-09-05T20:19:10.771Z] TOOL CALL #73: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E0%A4%A6%E0%A4%B8%E0%A5%8D%E0%A4%AF%E0%A5%81",
 "prompt": "Quote the Sanskrit entry दस्यु (dasyu): meaning and etymology — what Proto-Indo-Iranian and PIE forms are given, and which Iranian cognates (Avestan daŋhu-, Old Persian dahyu-) are listed."
}
```


## [2026-09-05T20:19:13.250Z] TOOL CALL #74: WebFetch

```json
{
 "url": "https://iranicaonline.org/articles/dehqan",
 "prompt": "Summarise and quote the etymology part of the Encyclopaedia Iranica article DEHQĀN: the derivation from Middle Persian dēh 'village/land' + suffix -gān, the Arabic form dihqān / pl. dahāqīn, the social meaning (landed gentry of late Sasanian and early Islamic Iran), and the later shift to 'peasant, farmer'."
}
```


### [2026-09-05T20:19:15.686Z] TOOL RESULT

```
# Sanskrit दस्यु (dasyu): Etymology and Cognates

## Proto-Indo-Iranian and PIE Forms

According to the Wiktionary entry, the Sanskrit word is "Inherited from Proto-Indo-Iranian *dásyuš ('enemy, foreigner, foreign people, foreign land')," which itself derives from "Proto-Indo-European *des- ('enemy, foreigner')."

## Iranian Cognates

**The webpage does not list any Iranian cognates.** While your question mentions Avestan daŋhu- and Old Persian dahyu-, these terms are not mentioned or discussed anywhere in the provided Wiktionary article content.

The entry only traces the etymology backward through Proto-Indo-Iranian and Proto-Indo-European linguistic ancestors, without providing examples of related words in other ancient languages like Avestan or Old Persian.
```


### [2026-09-05T20:19:16.329Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-05T20:19:20.848Z] TOOL CALL #75: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/d%C3%A1syu%C5%A1",
 "prompt": "Quote the reconstruction page for Proto-Indo-Iranian *dásyuš: meaning, PIE source, and the full descendants list (Indo-Aryan and Iranian branches: Avestan, Old Persian, etc.)."
}
```


### [2026-09-05T20:19:24.552Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-05T20:19:33.346Z] TOOL CALL #76: Bash

```json
{
 "command": "for u in \\\n 'https://en.wiktionary.org/wiki/%D8%AF%D9%87' \\\n 'https://en.wiktionary.org/wiki/%F0%90%8E%AD%F0%90%8F%83%F0%90%8E%B9%F0%90%8E%A0%F0%90%8E%A2' \\\n 'https://en.wiktionary.org/wiki/%D8%AF%D9%87%D9%82%D8%A7%D9%86' \\\n 'https://en.wiktionary.org/wiki/%D8%AF%D9%87%D8%A7%D8%AA' \\\n 'https://en.wiktionary.org/wiki/%CE%B8%CE%AF%CF%82' \\\n 'https://en.wiktionary.org/wiki/%E0%A4%A6%E0%A4%B8%E0%A5%8D%E0%A4%AF%E0%A5%81' \\\n 'https://abadis.ir/fatofa/%D8%AF%D9%87/' \\\n 'https://archive.org/details/oldpers' ; do\n python3 tools/fetch_source.py \"$u\" --note 'pdf page 133, root Dhis / deh, dahyu: etymology check' 2>&1 | tail -2\ndone",
 "description": "Archive web sources"
}
```


### [2026-09-05T20:19:39.973Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/2f1f321e4485b64b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/87ec0b3c2c68c29c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4effccbd94c652de.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3cfe2858c46b8aba.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4c74db6bd02fc8bd.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/233e654f527cad0f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2fcc5454682241ee.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/36e482e4340f0525.txt
```


## [2026-09-05T20:19:54.231Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('SNS_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in list(range(133,143))+list(range(232,240)):\n    p=pages[i]\n    nums=re.findall(r'(?<![\\d/])(\\d{2,3})(?![\\d/])', p)\n    print(i, nums[:12])\nEOF",
 "description": "Look for page numbers in SNS leaves"
}
```


### [2026-09-05T20:19:55.978Z] TOOL RESULT

```
133 ['31', '141', '167', '168', '67', '61', '39', '195', '65']
134 ['63', '137', '142', '16', '36', '120']
135 ['156', '17', '58', '60', '216', '171', '42']
136 ['01', '54', '491', '14', '10', '85']
137 ['11', '387', '42', '310', '59', '310']
138 ['59', '11', '82', '55', '43', '156']
139 ['11', '214', '60', '58', '95']
140 ['45', '588']
141 ['55', '60', '588', '51']
142 ['222', '218', '59']
232 ['11', '10']
233 ['11', '21', '31']
234 ['15', '10', '11', '14']
235 ['13', '12', '15']
236 ['19', '22']
237 ['11', '20', '10']
238 []
239 ['31', '12', '16']
```


## [2026-09-05T20:20:18.333Z] TOOL CALL #78: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqt362.jpg /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/902.png && cat > /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/902.vision.txt <<'EOF'\nBorhan-e Qate' (ed. Mo'in), printed p. 902 = archive.org borhan-ghate-v2 leaf n362\n(checked: leaf n363 carries the printed number ۹۰۳).\nRead from the page image on 2026-09-05 (pdf page 133 verification, root Dhîs / ده).\n\nBody: end of the دو… entries (دوبره، دوبوک), then the section head\n«بیان بیستم — در دال بی‌نقطه با های هوز، مشتمل بر پنجاه لغت و کنایات»\nwith the headwords ده ۱ (=۱۰)، ده ۲ (=دیه)، دهار، دهاژ …\n\nMo'in's etymological footnotes at the foot of p. 902, verbatim:\n\n۱ ـ پهلوی dah «اونوالا ۷۶»، اوستا dasa، هندی باستان dáça، ارمنی tasn، کردی و بلوچی ع deh، dâh، افغانی las، اسی dās، وخی las، dhas، سریکلی dhés، شغنی dhîs، lâs، یغنوبی و سنگلیچی das، منجی dah «اشتق ۵۸۷»، ختنی dasa، دیلی، روزگار نو ج ۴ شمارهٔ ۳ ص ۵۲، گیلکی da.\n\n۲ ـ دیه، پهلوی dêh «تاوادیا ۱۶۰»، پارسی باستان dahyu (سرزمین)، اوستا daxyu، هندی باستان dásyu، کردی dau، افغانی ع dih، بلوچی ع dîh و dêh «اشتق ۵۸۸»، ورک: هوبشمان ایضاً، گیلکی deh. رک: ده‌بوید.\n\n۳ ـ دهار، غار و شکاف کوه بود، اسدی (طوسی) گوید: … «لغت فرس ۱۵۸».\n۴ ـ رک: دهاژ.   ۵ ـ مصحف «دهار» (ه‍.م.).\n\n(«اشتق ۵۸۸» = Horn, Grundriss der neupersischen Etymologie, no. 588;\n «تاوادیا» = Tavadia; «هوبشمان» = Hübschmann, Persische Studien.)\nEOF\nls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/",
 "description": "Save BQT p.902 page image and vision transcription"
}
```


### [2026-09-05T20:20:19.950Z] TOOL RESULT

```
total 10456
drwxrwxr-x 2 sfmqrb sfmqrb   4096 Sep  5 16:20 .
drwxrwxr-x 9 sfmqrb sfmqrb   4096 Sep  5 01:38 ..
-rw-rw-r-- 1 sfmqrb sfmqrb 368375 Sep  4 13:39 0001.png
-rw-rw-r-- 1 sfmqrb sfmqrb   1684 Sep  4 13:39 0001.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 534367 Sep  4 13:39 0049.png
-rw-rw-r-- 1 sfmqrb sfmqrb   2677 Sep  4 13:39 0049.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   1076 Sep  4 15:27 103.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 446843 Sep  4 13:39 1225.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4412 Sep  4 13:39 1225.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   1254 Sep  4 14:18 1225.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 408541 Sep  4 15:42 1275.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3183 Sep  4 15:42 1275.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 122289 Sep  4 16:05 1339.png
-rw-rw-r-- 1 sfmqrb sfmqrb   2421 Sep  4 16:05 1339.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 325629 Sep  4 14:06 1357.png
-rw-rw-r-- 1 sfmqrb sfmqrb   2656 Sep  4 14:06 1357.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 341763 Sep  4 15:53 1382.png
-rw-rw-r-- 1 sfmqrb sfmqrb   2851 Sep  4 15:53 1382.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 447895 Sep  4 14:33 1385.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3725 Sep  4 14:33 1385.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   2008 Sep  4 14:34 1385.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 392691 Sep  4 19:05 1445.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3677 Sep  4 19:05 1445.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   1790 Sep  4 19:14 1445.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 168297 Sep  4 21:39 1452.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3942 Sep  4 21:39 1452.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 443522 Sep  4 14:46 1455.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4392 Sep  4 14:46 1455.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 154569 Sep  4 15:14 1488.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3724 Sep  4 15:14 1488.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 420606 Sep  5 16:13 1624.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3785 Sep  5 16:13 1624.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   1484 Sep  5 16:15 172.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 389471 Sep  4 14:06 1803.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3681 Sep  4 14:06 1803.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 482084 Sep  5 01:38 180.png
-rw-rw-r-- 1 sfmqrb sfmqrb   1288 Sep  5 01:39 180.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 510341 Sep  5 01:38 181.png
-rw-rw-r-- 1 sfmqrb sfmqrb   1196 Sep  5 01:39 181.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 442264 Sep  4 15:37 1878.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4418 Sep  4 15:37 1878.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 368487 Sep  4 15:37 1900.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3698 Sep  4 15:37 1900.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 343118 Sep  4 16:03 1908.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3313 Sep  4 16:03 1908.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 400069 Sep  5 16:14 2099.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3804 Sep  5 16:14 2099.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 442354 Sep  4 15:42 2143.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3763 Sep  4 15:42 2143.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   1063 Sep  5 02:20 220.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 175959 Sep  4 16:03 2222.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4471 Sep  4 16:03 2222.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 186249 Sep  4 19:06 2246.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4787 Sep  4 19:06 2246.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    805 Sep  4 19:14 2246.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 178528 Sep  5 16:12 2396.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4354 Sep  5 16:12 2396.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 166000 Sep  4 14:53 2407.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3983 Sep  4 14:53 2407.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   2615 Sep  4 15:28 31.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 512022 Sep  5 16:12 333.png
-rw-rw-r-- 1 sfmqrb sfmqrb   1339 Sep  5 16:12 333.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   1508 Sep  4 15:27 58.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   1931 Sep  4 15:02 70.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   1606 Sep  4 14:54 72.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 669351 Sep  5 01:38 733.png
-rw-rw-r-- 1 sfmqrb sfmqrb   1152 Sep  5 01:39 733.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 624515 Sep  5 16:20 902.png
-rw-rw-r-- 1 sfmqrb sfmqrb   1658 Sep  5 16:20 902.vision.txt
```


## [2026-09-05T20:20:27.681Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && pdftoppm -f 133 -l 133 -r 200 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg133 && identify pg133.png",
 "description": "Render PDF page 133"
}
```


### [2026-09-05T20:20:29.858Z] TOOL RESULT

```
pg133.png PNG 1700x2200 1700x2200+0+0 8-bit sRGB 46793B 0.000u 0:00.000
```


## [2026-09-05T20:20:32.473Z] TOOL CALL #80: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg133.png"
}
```


### [2026-09-05T20:20:32.830Z] TOOL RESULT

```

```


## [2026-09-05T20:20:32.827Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T20:21:30.750Z] AGENT

Now let me write the verification file.


## [2026-09-05T20:25:35.113Z] TOOL CALL #81: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk133.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\n\ndoc = {\n \"pdf_page\": 133,\n \"book_page\": 103,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [\n  {\n   \"entry\": 1,\n   \"root\": \"Dhîs\",\n   \"verdict\": \"disputed\",\n   \"modern_form\": \"no such Proto-Indo-European root; Persian ده deh continues Proto-Iranian *dahyu- < Proto-Indo-Iranian *dásyuš 'foreign land, foreign people' (Wiktionary: PIE *des- 'enemy, stranger'), while Greek θίς, θινός is Pre-Greek (Beekes) or belongs to PIE *dʰeu- 'to whirl, raise dust' (Pokorny IEW 263)\",\n   \"note\": \"The root box is a verbatim copy of the one place it exists: S. E. Mann, An Indo-European Comparative Dictionary p.191, 'dhis- (2) (?) Per. diha ‘village’; Myc. & Gk. this, thin, gs thinós ‘earth, bottom, pile, silt’'. Mann himself flags the whole headword with '(?)', and it rests on exactly the two items Nourai reproduces — which is also Nourai's gloss 'village, earth ?'. Both halves are today derived elsewhere. (a) The Iranian half: Old Persian dahyu-, Avestan dahyu-/daiŋhu- 'land' correspond to Sanskrit dásyu- 'stranger, non-Aryan, demon' (Kent 190; Buck 1302; Bartholomae 706 ff.); the Sanskrit d- rules out a PIE *dʰ-, which would have given Indo-Aryan dh-, and the -h- of the Iranian word is not a root consonant at all but the regular Iranian reflex of the suffixal *-sy- (Hübschmann, Persische Studien §109a: 'Idg. sy = ap. hy = np. h: dih ‘Dorf’ ... = ap. dahyu-'). A root shaped *dʰis- can therefore not yield dahyu-. (b) The Greek half: Pokorny IEW 263 puts θίς, θινός 'Sandhaufen, bes. Düne, Gestade, Sandbank, Haufen überhaupt' under root '4. dheu-, dheuǝ- ‘stieben, wirbeln’', built 'aus *θϝ-ιν-'; Walde-Pokorny I (s.v. dheu-) has the identical treatment; Beekes (per Wiktionary) prefers a Pre-Greek substrate origin. Neither connects it with an Iranian word for 'village'. Buck, who is Nourai's own source SYN:1302, says of the Iranian word only 'root connections dub.'. So the root box, its language label ('Indo-European') and its gloss are all an isolated 1980s conjecture of Mann's that modern scholarship does not share; the tree hanging under it is nevertheless internally correct from node 1 downwards.\",\n   \"note_fa\": \"جعبهٔ ریشه در این نمودار عیناً از فرهنگ تطبیقی هند و اروپاییِ استوارت مان (ص ۱۹۱) برداشته شده است: «dhis- (۲) (؟) فارسی diha «ده»؛ یونانی this, thinós «خاک، ته، توده، لای»». خودِ مان کنارِ این سرواژه علامت پرسش گذاشته و تمام دستمایه‌اش همان دو واژه‌ای است که نورایی می‌آورد. پژوهش امروزی هر دو نیمه را جای دیگری می‌نشاند: «ده» فارسی از ایرانی باستان *dahyu- و آن از هندوایرانی آغازین *dásyuš (هم‌ریشه با dásyu- سنسکریت به معنی «بیگانه، دشمن») است — دالِ سنسکریت نشان می‌دهد که واکِ آغازینِ هندواروپایی *d بوده نه *dʰ، و «ه» در «ده» اصلاً بخشی از ریشه نیست بلکه بازتابِ قانون‌مندِ *-sy- در ایرانی است (هوبشمان، بند ۱۰۹ الف: «sy هندواروپایی = hy پارسی باستان = h فارسی نو»)؛ و θίς یونانی را پوکورنی (ص ۲۶۳) زیرِ ریشهٔ *dheu- «گرد برانگیختن، چرخاندن» می‌آورد و بیکس آن را پیشایونانی می‌داند. حتی باک، که خودِ نورایی او را گواه گرفته، دربارهٔ ریشهٔ این واژه می‌نویسد «پیوندهای ریشه‌ای مشکوک است». بنابراین پژوهش امروزی ادعای جعبهٔ ریشه را رد می‌کند؛ اما زنجیرهٔ زیرِ آن، از گرهٔ ۱ به پایین، درست است.\",\n   \"sources\": [\n    \"https://en.wiktionary.org/wiki/%F0%90%8E%AD%F0%90%8F%83%F0%90%8E%B9%F0%90%8E%A0%F0%90%8E%A2\",\n    \"https://en.wiktionary.org/wiki/%CE%B8%CE%AF%CF%82\",\n    \"https://en.wiktionary.org/wiki/%E0%A4%A6%E0%A4%B8%E0%A5%8D%E0%A4%AF%E0%A5%81\"\n   ],\n   \"ref_check\": [\n    {\"ref\": \"IEC:191\", \"status\": \"supports\",\n     \"note\": \"IEC.txt line 2915 (leaf 119, the leaf whose running head is 'dhightos — dhmb-' and which carries printed pp. 191-193; the entry stands before the '192' page mark, i.e. on p.191): 'dhis- (2) (?) Per. diha ‘village’; Myc. & Gk. this, thin, gs thinós ‘earth, bottom, pile, silt’'. Mann's page really does say what Nourai's root box says — including the question mark, which Nourai kept in his gloss ('village, earth ?'). The reference supports the citation but is itself the weak point: Mann gives no further cognates and no argument.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"IEW 261-267, esp. p.263 (POK_01.txt line 3771, leaf 274)\", \"stance\": \"contradicts\",\n     \"note\": \"No root *dhis- exists in Pokorny. The Greek word Mann builds on is treated under '4. dheu-, dheuǝ- ... ‘stieben, wirbeln, bes. von Staub, Rauch, Dampf’': 'Auf Grund der Bed. ‘(zusammen)wirbeln’ θίς, θινός ‘Sandhaufen, bes. Düne, Gestade, Sandbank, Haufen überhaupt’, aus *θϝ-ιν-, gebildet wie ἀκτίν-, γλωχίν-, δελφίν-, ὠδίν-'.\"},\n    {\"src\": \"WLD\", \"where\": \"Vergl. Wb. I, s.v. dheu- (WLD_Bd1_pages.txt lines 78542-78549)\", \"stance\": \"contradicts\",\n     \"note\": \"'Auf Grund der Bed. „(zusammen)wirbeln“ θίς, θινός „Sandhaufen, bes. Düne, Gestade, Sandbank, Sandsteppe, Sand auf dem Meeresgrund, Schlamm; Haufen überhaupt, Erhebung“ ... vgl. zur Bed. mnd. düne, nnd. Düne, ahd. duna' — the same verdict as Pokorny, and again no *dhis- headword anywhere in Bd. I.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, d-list (AHD_watkins1985.txt lines 377-379)\", \"stance\": \"silent\",\n     \"note\": \"The appendix runs dheigh- → dhel- → dhelbh- → dhembh- → dhen-¹ → dhen-² → dher-¹ ...; there is no dhis-/dhēs- 'village, earth' root, and no English word is traced to one. Silence rather than disagreement, since no English word reaches the Iranian family here.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 19.11 'Country', printed p.1302\", \"stance\": \"partial\",\n     \"note\": \"'Av. daiŋhu-, dahʸyu-, OPers. dahyu- ... prob. = Skt. dasyu-, the designation of the pre-Aryan inhabitants of India (orig. ‘inhabitants of the country’?), root connections dub. Barth. 706 ff. Uhlenbeck 123.' — Nourai's own source has the family but expressly declines to give it a PIE root.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann p.191, headword dhis- (1)\", \"stance\": \"partial\",\n     \"note\": \"Mann's neighbouring headword 'dhis- (1) ‘god, godlike’. Cf. dhiio Skt. dhisnyah ‘devout’ ... ON dis pl. dísir ‘goddess’' shows that his dhis- (2) is a separate, ad-hoc entry created only to house the two words in question.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Avestan / Old Persian\",\n     \"words\": \"dahyu, dainhu\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"The two forms are impeccable and are exactly Kent's pair: Old Persian dahyu- f. 'land, province, district' (nom. dahyauš, gen.pl. dahyūnām, in the satrapy lists of DB 1.6, DNa 15-30, XPh) beside Gathic Avestan dax́yu-/dahyu- and Young Avestan daŋ́hu-/daiŋhu-; Nourai's 'dainhu' is that Young Avestan daiŋhu- in his own transcription (ŋh written nh). Bartholomae's headword at col. 706 is precisely 'p. dahyav-, j. daŋhav- (, daiŋh°, daŋh°), j., g. dahyav- | dahyu- f. ‘Landgebiet, Landschaft, Land’, oft zugleich auch von den Bewohnern'. What is wrong is the arrow, not the words. The Iranian word is Proto-Indo-Iranian *dásyuš, the exact counterpart of Sanskrit dásyu- 'stranger, non-Aryan, enemy, demon'; PII *-sy- gives Iranian -hy- (whence Young Av. -ŋh- by assimilation before the stem vowel), which is the whole source of the -h-. Since Sanskrit has d- and not dh-, the initial cannot go back to PIE *dʰ-; Wiktionary reconstructs PIE *des- 'enemy, foreigner', Buck and Bartholomae leave the root open. Semantically the Indian and Iranian branches split: in India the word named the hostile aborigines, in Iran the land/province (and, by metonymy, its people) — Buck's guess is that the common starting point was 'inhabitants of the country'. So: right words, right meaning, wrong parent.\",\n     \"derivation_fa\": \"دو صورتِ این گره کاملاً درست‌اند و دقیقاً همان‌هایی هستند که کنت می‌آورد: پارسی باستان dahyu- (مؤنث) «سرزمین، ایالت، شهربانی» — در فهرستِ ساتراپی‌ها در بیستون ۱٫۶ و نقش رستم — در برابرِ گاهانیِ dax́yu-/dahyu- و اوستاییِ نو daŋ́hu-/daiŋhu-؛ «dainhu» در کتاب همان daiŋhu- است که نورایی ŋh را nh می‌نویسد. بارتولومه در ستون ۷۰۶ سرواژه را چنین می‌آورد: «dahyav- پارسی باستان، daŋhav- (daiŋh°, daŋh°) اوستاییِ نو ... مؤنث، «قلمرو، ناحیه، سرزمین»، غالباً هم‌زمان دربارهٔ ساکنانِ آن». اشکال در واژه‌ها نیست، در پیکانِ بالای آن‌هاست: این واژه بازماندهٔ هندوایرانیِ آغازینِ *dásyuš است، برابرِ دقیقِ dásyu- سنسکریت «بیگانه، ناآریایی، دشمن»؛ *-sy- هندوایرانی در ایرانی به -hy- بدل شده (و در اوستاییِ نو با همگونی به -ŋh-) و همین است سرچشمهٔ «ه». چون سنسکریت d دارد نه dh، واکِ آغازین نمی‌تواند *dʰ هندواروپایی باشد. تحول معنایی هم روشن است: در هند این واژه نامِ بومیانِ دشمن شد و در ایران نامِ سرزمین و مردمِ آن. پس ادعای نورایی دربارهٔ خودِ واژه‌ها درست است ولی ریشهٔ بالادستی را پژوهش امروزی رد می‌کند.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/%F0%90%8E%AD%F0%90%8F%83%F0%90%8E%B9%F0%90%8E%A0%F0%90%8E%A2\",\n      \"https://en.wiktionary.org/wiki/%E0%A4%A6%E0%A4%B8%E0%A5%8D%E0%A4%AF%E0%A5%81\",\n      \"https://archive.org/details/oldpers\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"SYN:1302\", \"status\": \"supports\",\n       \"note\": \"Buck, Dict. of Selected Synonyms, §19.11 'Country', printed p.1302 (SYN.txt leaf 1326 area; the running head of the facing page is 'SELECTED INDO-EUROPEAN SYNONYMS'): 'Av. daiŋhu-, dahʸyu-, OPers. dahyu- (in OPers. used of the great provinces and also of regions within them; MPers. deh ‘country’, NPers. dih ‘village’), prob. = Skt. dasyu- ... root connections dub. Barth. 706 ff.' — the words, the glosses and even the onward Middle/New Persian chain, but no PIE root.\"},\n      {\"ref\": \"KNT:190\", \"status\": \"supports\",\n       \"note\": \"Kent, Old Persian, Lexicon p.190 (KNT.txt leaf 214, the leaf that ends with the running head 'LEXICON' and printed 191): 'dahyu- sb. ‘land, province, district’: GAv. dahyu-, LAv. dahyu- daiŋhu-, NPers. dih ‘village’, Skt. dásyu- ‘stranger, demon’ (§124.2, §153.IV, §166). Decl., §183.1. See also visadahyu-.' Nourai's pair 'dahyu, dainhu' and the gloss 'land, country' are lifted straight from here.\"},\n      {\"ref\": \"BRT:706\", \"status\": \"supports\",\n       \"note\": \"Bartholomae, Altiranisches Wörterbuch col. 706 (BRT.txt line 13095; the column marks 706 / 707 / 708 stand at lines 13071 / 13097 / 13100): 'p. dahyav-, j. daŋhav-(, daiŋh°, daŋh°), j., g. dahyav- | dahyu- f. ‘Landgebiet, Landschaft, Land’, oft zugleich auch von den Bewohnern' with Avestan and Old Persian citations (Yt 19.1, V 2.24, Bh 1.6 etc.). Exactly the node as drawn.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KNT\", \"where\": \"Lexicon p.190 s.v. dahyu-\", \"stance\": \"supports\",\n       \"note\": \"see ref_check; Kent adds the Sanskrit equation dásyu- 'stranger, demon' that decides against a *dʰ- root.\"},\n      {\"src\": \"BRT\", \"where\": \"Altiran. Wb. col. 706-708\", \"stance\": \"supports\",\n       \"note\": \"gives the full Avestan/Old Persian paradigm, including the OP instr. dahyauvā (Bh 1.34) and the Young Avestan gen.pl. daŋhunąm; no Indo-European root is offered.\"},\n      {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II, Glossary s.v. dēh (NYB_vol2_glossary.txt line 1249)\", \"stance\": \"supports\",\n       \"note\": \"'dēh [dyh, MTʾ] village, settlement ... — Av. OP (706 sgg.) dahyu- ‘country’' — Nyberg cites the same Bartholomae column 706 that Nourai does.\"},\n      {\"src\": \"SYN\", \"where\": \"Buck p.1302 §19.11\", \"stance\": \"partial\",\n       \"note\": \"'root connections dub.' — explicit refusal to give the family a PIE root, i.e. no support for Nourai's *Dhîs.\"},\n      {\"src\": \"HUB\", \"where\": \"Persische Studien §109a (HUB.txt line 7780)\", \"stance\": \"partial\",\n       \"note\": \"'Idg. sy = ap. hy = np. h: dih ‘Dorf’, arm. deh = ap. dahyu- ‘Provinz, Distrikt’' — shows the -h- is the reflex of a suffixal *-sy-, which is incompatible with a root *dʰis-.\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Pahlavi\",\n     \"words\": \"deh, dih\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Middle Persian dēh 'land, country; village', written either with the Aramaic ideogram MTʾ (Aramaic mātā 'land') or phonetically dyh: MacKenzie, Concise Pahlavi Dictionary p.26, 'deh [MTA | M dyh, N ~] country, land; village'; Nyberg, Glossary s.v., 'dēh [dyh, MTʾ] village, settlement, pl. dēhān'. The phonetic route from node 1 is the standard one, set out by Hübschmann (Persische Studien §6c): OP dahyu- lost its final syllable, giving MP *dahy; the y first umlauted the a and then dropped, yielding dēh — 'nach Abfall der letzten Silbe (Vokal + Konsonant) entstand mp. *mahʸ, *kahʸ, *vahʸ und *dahʸ, deren ausl. y schwand, nachdem es Umlaut bewirkt hatte, wonach sich die mp. Formen meh, keh, veh und deh ergaben' — the same development as MP meh, keh, weh from OP *maθyah-, *kanyah-, vahyah-. Nourai's two spellings are the two attested readings of the same word: dēh is the Middle Persian value (so MacKenzie, Nyberg, Pāzand deh) and dih the later, classical New Persian reading of the same graph; Hübschmann footnotes exactly this doublet ('Da im Neup. neben dih die Form ده, älter also deh steht ...'). Manichaean Middle Persian has dyh, and Armenian borrowed the word early as deh (in dehpet 'district chief' = Phl. dahyupat).\",\n     \"derivation_fa\": \"فارسی میانه dēh «سرزمین، کشور؛ ده»، که در پهلویِ کتابی هم با هُزوارشِ آرامیِ MTʾ (از mātā «سرزمین») و هم آوانگاشتِ dyh نوشته می‌شود؛ مکنزی در فرهنگِ کوچکِ پهلوی می‌آورد «deh [MTA | مانوی dyh] کشور، سرزمین؛ ده» و نیبرگ «dēh [dyh, MTʾ] ده، آبادی، جمع dēhān». راهِ آواییِ آن از گرهٔ ۱ همان است که هوبشمان (بند ۶ ج) شرح داده است: در پارسی باستان dahyu- هجای پایانی می‌افتد و *dahy می‌ماند؛ سپس y نخست a را به e امالـه می‌کند و آنگاه خود می‌افتد و dēh به دست می‌آید — درست همان‌گونه که meh و keh و veh از *maθyah- و *kanyah- و vahyah- پدید آمده‌اند. دو صورتِ «deh, dih» در کتاب دو خوانشِ یک واژه‌اند: dēh خوانشِ فارسیِ میانه (و پازند) است و dih خوانشِ کلاسیکِ فارسیِ نو. ارمنی هم این واژه را زود وام گرفته است (deh در dehpet برابرِ dahyupat پهلوی). ادعای نورایی در این گره درست است.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/%D8%AF%D9%87\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"BQT:902\", \"status\": \"supports\",\n       \"note\": \"Borhan-e Qateʿ ed. Moʿin, printed p.902 = archive.org borhan-ghate-v2 leaf n362 (fixed by leaf n363, which carries the printed number ۹۰۳; page image and my transcription saved as data/verification/sources/refs/ocr/BQT/902.png and 902.vision.txt). Moʿin's footnote 2 to the headword ده reads: «۲ ـ دیه، پهلوی dêh «تاوادیا ۱۶۰»، پارسی باستان dahyu (سرزمین)، اوستا daxyu، هندی باستان dásyu، کردی dau، افغانی ع dih، بلوچی ع dîh و dêh «اشتق ۵۸۸»، ورک: هوبشمان ایضاً، گیلکی deh». Pahlavi dēh, and behind it OP dahyu and Av. daxyu — precisely nodes 1 and 2.\"},\n      {\"ref\": \"SNS:242\", \"status\": \"partial\",\n       \"note\": \"Tavoosi's glossary of Šāyast nē Šāyast does have the entry, and it says what Nourai's node says: SNS_pages.txt leaf 138 carries a 'deh/dih' entry with 'dahyu' beside it, and the neighbouring entries 'deh bad / deh badān : dahyubadān'; the book's word index (leaf 235) lists 'deh/dih 242/10'. But the OCR of this Persian book has no printed page numbers, so I could not confirm that Nourai's '242' is the page where the entry stands rather than the text reference 242/10 that the index gives.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dict. p.26 s.v. deh (PHD.txt line 312)\", \"stance\": \"supports\",\n       \"note\": \"'deh [MTA | M dyh, N ~] country, land; village. ~gān [MTA-, dhʾgʾn'] = dahigān' — the Middle Persian word with exactly Nourai's gloss, plus the derivative that feeds node 3.\"},\n      {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II, Glossary (NYB_vol2_glossary.txt lines 1249-1251)\", \"stance\": \"supports\",\n       \"note\": \"'dēh [dyh, MTʾ] village, settlement, pl. cas. obl. -ān ... — Av. OP (706 sgg.) dahyu- ‘country’; Arm. lw. deh ‘district’; MPrs dyh ‘country’; Paz. deh, NP dih. Cf dahyu-pat.' Nyberg also has dēhīk 'belonging to a village' and dehkān.\"},\n      {\"src\": \"HUB\", \"where\": \"Persische Studien §6c, pp.129-130 (HUB.txt lines 4503-4523)\", \"stance\": \"supports\",\n       \"note\": \"'dih ‘Dorf’, paz. deh Min. Gl. 60, Shk. 241, arm. deh in dehpet (= paz. dehvad, phl. dahyupat) ... ap. dahyauš (nom. sg.), zd. daŋhu-š, gd. dahyu-' and the sound law 'Nach Abfall der letzten Silbe ... entstand mp. *dahy, deren ausl. y schwand, nachdem es Umlaut bewirkt hatte ... deh'.\"},\n      {\"src\": \"HRN\", \"where\": \"Grundriss der neupers. Etymologie no. 588 (HRN.txt line 5270)\", \"stance\": \"supports\",\n       \"note\": \"'588. dih ‘Dorf’, vergl. dihgän (arab. LW. dihqän, arm. LW. dehkan), ap. dahyu- ‘Land’; aw. dahyu-; phlv. dih bezw. deh, dahyu-pat, dahyu-paiti (arm. LW. dehpet), vergl. adihīk, uzdihīk; ai. dásyu- ... Die ursprüngliche np. Aussprache wird deh gelautet haben.' Horn is the '«اشتق ۵۸۸»' that Moʿin cites on BQT p.902.\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Persian\",\n     \"words\": \"deh 2; dehât; dehgân; dehxodâ\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"All four items, and the five extras, are correctly attached. (1) deh 2 «ده ۲» (also written «دیه») 'village, countryside' is the direct continuation of MP dēh (node 2); Moʿin's own headword on BQT p.902 is «۲ ـ دیه» and Horn no.588 notes 'Die ursprüngliche np. Aussprache wird deh gelautet haben', i.e. the classical spelling ده stands for deh, the reading dih being the later school pronunciation. (2) dehât «دهات» is deh with the Arabic sound-plural ات attached inside Persian — an Arabic-morphology plural of a purely Iranian noun, of the type فرمایشات; it has since been re-singularised as a mass noun 'the countryside', whence the Arabic nisba دهاتی dehâti 'villager'. (3) dehgân «دهگان» is inherited: MP dahigān / dēhgān 'countryman, farmer, landowner' = dēh + the adjectival suffix -gān (< Old Iranian *-akāna-); Arabic borrowed it in the Sasanian-to-Umayyad period as دِهْقان dihqān, pl. دَهاقين dahāqīn (Persian g regularly rendered by Arabic q), and Persian took the Arabized shape back, so «دهقان» is a round trip through Arabic and «دهگان» its inherited doublet — exactly the pairing Nourai prints. Semantically the word named the landed gentry of the late Sasanian and early Islamic countryside and only later sank to 'peasant, farmer'. (4) dehxodâ «دهخدا» (colloquially «دخو», the pen-name of ʿAli-Akbar Dehkhodā) = deh + xodâ 'lord, master' (MP xwadāy), 'village headman, owner of the village'; the Borhan itself defines «دهخدا ... کدخدا و بزرگِ ده را گویند ... سرکردهٔ رعایا و مزارع» two leaves later (BQT p.904). The extras are the same stem with ordinary Persian formatives: دهبان (-bān 'keeper'), دهدار (-dār 'holder'), دهکیا (kiā 'chief', a Caspian title), دهستان (-stān 'district', today the official 'rural district'), دهکده (kada 'house, place' > 'hamlet'). The Rumi couplet Nourai quotes («خواجه پندارد که ده ۲ روزی دهد ...») is a pun on the three homographs ده = 'village', 'ten' and the imperative of دادن, which is why the entry is numbered ده ۲.\",\n     \"derivation_fa\": \"هر چهار واژه و پنج واژهٔ افزودهٔ این جعبه به‌درستی به «ده» بسته شده‌اند. ۱) «ده ۲» (و املای کهنِ «دیه») دنبالهٔ مستقیمِ dēh فارسی میانه است؛ سرواژهٔ خودِ معین در حاشیهٔ برهان قاطع ص ۹۰۲ «۲ ـ دیه» است و هرن (شمارهٔ ۵۸۸) می‌نویسد تلفظِ اصیلِ فارسیِ نو deh بوده و dih خوانشِ متأخر است. ۲) «دهات» جمعِ عربیِ سالمِ «ات» است که در خودِ فارسی به یک اسمِ ایرانی بسته شده (از گونهٔ «فرمایشات») و امروز خود اسمِ جنس شده به معنی «روستاها، بیرونِ شهر»، و از آن «دهاتی» با یای نسبتِ عربی ساخته شده است. ۳) «دهگان» صورتِ موروثی است: فارسی میانه dahigān/dēhgān «روستایی، کشاورز، زمین‌دار» از dēh + پسوندِ صفت‌سازِ -gān (از ایرانیِ باستان *-akāna-)؛ عربی آن را در روزگارِ ساسانی و آغازِ اسلام به‌صورتِ «دِهْقان» (جمع: دهاقین) وام گرفت — گافِ فارسی در عربی قاف می‌شود — و فارسی همان صورتِ معرّب را باز پس گرفت. پس «دهقان» یک وام‌گیریِ رفت‌وبرگشتی از راهِ عربی و «دهگان» دوگانهٔ موروثیِ آن است، درست همان جفتی که نورایی چاپ کرده. این واژه نخست نامِ اشرافِ زمین‌دارِ اواخرِ ساسانی و اوایلِ اسلام بود و سپس به «کشاورز» فروکاست. ۴) «دهخدا» (در گفتار «دخو»، تخلصِ علی‌اکبر دهخدا) از «ده» + «خدا» (فارسی میانه xwadāy) «کدخدا، بزرگِ ده» است. افزوده‌ها هم ساخت‌های عادیِ فارسی‌اند: دهبان، دهدار، دهکیا، دهستان، دهکده. بیتِ مولوی که در جعبه آمده بازیِ سه‌گانه با «ده» (آبادی)، «ده» (عدد) و «دِه» (فعلِ امر) است و همین سبب شمارهٔ «ده ۲» است. ادعای نورایی در این گره درست است.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/%D8%AF%D9%87\",\n      \"https://en.wiktionary.org/wiki/%D8%AF%D9%87%D9%82%D8%A7%D9%86\",\n      \"https://en.wiktionary.org/wiki/%D8%AF%D9%87%D8%A7%D8%AA\",\n      \"https://abadis.ir/fatofa/%D8%AF%D9%87/\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"SYN:1302\", \"status\": \"supports\",\n       \"note\": \"Buck p.1302: '... MPers. deh ‘country’, NPers. dih ‘village’' — the Middle-to-New Persian step of this node, in Nourai's own source.\"},\n      {\"ref\": \"BQT:902\", \"status\": \"supports\",\n       \"note\": \"Borhan-e Qateʿ p.902 (leaf n362; transcription saved at data/verification/sources/refs/ocr/BQT/902.vision.txt). The page opens the ده section («بیان بیستم ـ در دال بی‌نقطه با های هوز») with the headwords ده ۱ (ten) and ده ۲ (=دیه), and Moʿin's footnote 2 gives «دیه، پهلوی dêh ... پارسی باستان dahyu (سرزمین)، اوستا daxyu، هندی باستان dásyu ... «اشتق ۵۸۸» ... هوبشمان ایضاً». Nourai's script «دِه ۲ ( دیه )» is Moʿin's headword; دهقان/دهگان and دهخدا follow on pp.903-905 of the same section.\"},\n      {\"ref\": \"MON:1585\", \"status\": \"partial\",\n       \"note\": \"Moʿin's Farhang-e Farsi is on disk only as unusable OCR (MON_part1/2.txt are noise), so I checked the entry through abadis.ir's فرهنگ معین section: 'ده (دِ) [په.] (اِ.) روستا، آبادی کوچک' beside 'ده (دَ) [په.] (اِ.) عدد اصلی پس از نه'. The entry, the numbering of the two homographs and the Pahlavi origin tag [په.] are all as Nourai reports; the web text carries no page numbers, so p.1585 itself could not be confirmed.\"},\n      {\"ref\": \"TZF:13\", \"status\": \"not_checked\",\n       \"note\": \"Abolghasemi, Tarikh-e Mokhtasar-e Zaban-e Farsi — refs_online.json records no copy on archive.org and no local file (only a login-walled PDF on ketabnak). Not accessible.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"HRN\", \"where\": \"Horn no.588 (HRN.txt lines 5270-5276)\", \"stance\": \"supports\",\n       \"note\": \"'588. dih ‘Dorf’, vergl. dihgän (arab. LW. dihqän, arm. LW. dehkan) ... Die ursprüngliche np. Aussprache wird deh gelautet haben.' Horn states the دهگان → Arabic دهقان borrowing that Nourai's bracketed pair encodes.\"},\n      {\"src\": \"PHD\", \"where\": \"MacKenzie p.24 s.v. dahigān (PHD.txt line 308)\", \"stance\": \"supports\",\n       \"note\": \"'dahigān [dhywkʾn' | N dihgān] countryman, farmer' — the Middle Persian antecedent of دهگان/دهقان, with MacKenzie himself equating it to New Persian dihgān.\"},\n      {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II, Glossary (line 1251)\", \"stance\": \"supports\",\n       \"note\": \"'dehkān [dhkʾn'] villager, pl. cas. obl. ~-ān. — A recent formation of deh; NP dihgān, Arab. lw. dihqān- ‘landlord’' — explicitly the Persian→Arabic loan and the -gān formation.\"},\n      {\"src\": \"MON\", \"where\": \"Farhang-e Moʿin s.v. ده, via abadis.ir\", \"stance\": \"supports\",\n       \"note\": \"'ده (دِ) [په.] (اِ.) روستا، آبادی کوچک' — Moʿin tags the word Pahlavi, i.e. inherited, exactly as the chart draws it.\"},\n      {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e rishe-hā-ye hend-o-orupāyi (incoming/ARY/ARY_pages.txt)\", \"stance\": \"silent\",\n       \"note\": \"Greps for dahyu / dasyu / a ده headword return nothing usable: the Latin transliterations in this scan are OCR noise (e.g. 'ده یونانی (080): 4 مف۳51526'), so Aryanpur cannot be used as a cross-check here.\"}\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"Avestan\",\n     \"words\": \"visa-dahyu, vîspa-dahyu\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"The compound is real, is built on node 1 exactly as drawn, and both of Nourai's variants are justified — but it is Old Persian (and its Median doublet), not Avestan. Kent's lexicon p.208 has 'visadahyu- adj. ‘of or for all countries or provinces’ (§161.IIa): borrowed in Elam. mi-iš-ša-da-a-hu-iš and (with Med. vispa-) Akk. u-iš-pi-da-a-ʼ-i; visa- ‘all’ + dahyu- ‘country, province’. visadahyum asm. XPa 12.' It is attested exactly once, in Xerxes' inscription on the Gate of All Nations at Persepolis: 'vašnā Auramazdāha imam duvarθim visadahyum adam akunavam' — 'by the favour of Ahuramazda I made this gateway of-all-lands' (Bartholomae quotes the same sentence under duvarθay- 'Torhalle'). The first member is OP visa- 'all' < PIE *wiḱwo- (Kent §150, §161.IIa 'visa-dahyu- ‘containing all lands’'), whose Median counterpart is vispa- (as in vispazana-); Nourai's second form vīspa-dahyu is therefore not an invention but the Median shape of the same compound, preserved in the Akkadian version of XPa as u-iš-pi-da-a-ʼ-i. What is wrong is the language label: the word is not Avestan. Bartholomae has no compound vīspa-daŋhu-; Avestan expresses the notion only phrasally, vīspanąm dahyunąm 'of all the lands' (Yt 13.143-145). The gloss 'for all provinces' is Kent's 'of or for all countries or provinces', so that is right. Hence plausible: correct etymology and correct source page, wrong language box.\",\n     \"derivation_fa\": \"این ترکیب واقعی است و درست همان‌گونه که در نمودار کشیده شده بر گرهٔ ۱ سوار است، و هر دو صورتی که نورایی می‌آورد پشتوانه دارد — اما پارسی باستان (و گونهٔ مادیِ آن) است، نه اوستایی. کنت در واژه‌نامهٔ خود، ص ۲۰۸، می‌آورد: «visadahyu- صفت، ‘از آنِ همهٔ سرزمین‌ها یا برای همهٔ آن‌ها’؛ در ایلامی mi-iš-ša-da-a-hu-iš و (با vispa- مادی) در اکدی u-iš-pi-da-a-ʾ-i وام گرفته شده؛ visa- ‘همه’ + dahyu- ‘سرزمین، ایالت’. visadahyum در XPa سطر ۱۲». تنها یک بار به‌کار رفته است: در کتیبهٔ خشایارشا بر «دروازهٔ همهٔ ملل» در تخت جمشید: «vašnā Auramazdāha imam duvarθim visadahyum adam akunavam». جزءِ نخست visa- «همه» از *wiḱwo- هندواروپایی است که صورتِ مادیِ آن vispa- است (چنان‌که در vispazana-)؛ پس «vîspa-dahyu» ساختهٔ نورایی نیست بلکه همان گونهٔ مادی است که در ترجمهٔ اکدیِ کتیبه بازتاب یافته. خطا در برچسبِ زبان است: بارتولومه هیچ ترکیبِ اوستاییِ vīspa-daŋhu- ندارد و اوستا این معنا را تنها به‌صورتِ ترکیبِ نحوی «vīspanąm dahyunąm» (یشت ۱۳٫۱۴۳ـ۱۴۵) بیان می‌کند. معنایی که در جعبه آمده («برای همهٔ ایالت‌ها») همان معنای کنت است. بنابراین ریشه‌شناسی و مأخذ درست است ولی جعبهٔ زبان باید «پارسی باستان» می‌بود؛ ادعای نورایی با این احتیاط پذیرفتنی است.\",\n     \"sources\": [\n      \"https://archive.org/details/oldpers\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"KNT:208\", \"status\": \"supports\",\n       \"note\": \"The local KNT.txt is truncated in the middle of the v- entries, so I read the page in the archive.org full text of the same scan (oldpers_djvu.txt, lines 29045-29049, on the 'OLD PERSIAN' page immediately before the running head 'LEXICON 209', i.e. printed p.208): 'visadahyu- adj. ‘of or for all countries or provinces’ (§161.IIa): borrowed in Elam. mi-iš-ša-da-a-hu-iš and (with Med. vispa-) Akk. u-iš-pi-da-a-ʼ-i; visa- ‘all’ + dahyu- ‘country, province’. visadahyum asm. (§53, §188.II) XPa 12.' Kent supports both of Nourai's forms and his gloss, and derives the compound from dahyu- — but labels it Old Persian, not Avestan.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KNT\", \"where\": \"Old Persian §161.II.a (KNT.txt line 1917) and §150 (line 1822), §46 (line 1193)\", \"stance\": \"partial\",\n       \"note\": \"'paru-zana- ‘having many men’; vispa-zana- ‘having all (kinds of) men’; visa-dahyu- ‘containing all lands’' and 'pIE *wiḱwo-, OP visa- ‘all’, also in visadahyu-; OP vispa- (with Med. sp) in vispazana-; Av. vispa-, Skt. viśva-.' Confirms the compound and its make-up, and shows that vispa- is the Median form — so the pair visa-/vispa- is an Old Persian/Median doublet, not an Avestan one.\"},\n      {\"src\": \"BRT\", \"where\": \"Altiran. Wb. s.v. p. duvarθay- (BRT.txt line 13991); vīspa- and daŋhu- entries\", \"stance\": \"partial\",\n       \"note\": \"'p. duvarθ-ay- m. ‘Torhalle’: vašnā auramazdāha imam °θim visadahyum (sd.) adam akunavam X.1,3' — Bartholomae cites the compound only from the Old Persian inscription. He has no Avestan headword vīspa-daŋhu-; the Avestan material is the phrase 'vīspanąm dahyunąm narąm ... nāirinąm' (Yt 13.143-145), i.e. two words, not a compound. This is what makes the chart's 'Avestan' label wrong.\"},\n      {\"src\": \"SYN\", \"where\": \"Buck 19.11 p.1302\", \"stance\": \"silent\",\n       \"note\": \"Buck lists Av. daiŋhu-/OP dahyu- but no compound with 'all'; nothing for or against this node.\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-133.json','w',encoding='utf-8') as f:\n    json.dump(doc, f, ensure_ascii=False, indent=1)\n    f.write('\\n')\nprint('written')\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk133.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-133.json > /dev/null && echo \"JSON OK\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 133",
 "description": "Write and validate page-133.json"
}
```


### [2026-09-05T20:25:38.742Z] TOOL RESULT

```
written
JSON OK
nodes verified: 4/4
node verdicts: {'disputed': 1, 'confirmed': 2, 'plausible': 1}
root verdicts: {'disputed': 1}
ref checks: {'supports': 7, 'partial': 2, 'not_checked': 1}
books consulted: {'supports': 11, 'partial': 4, 'silent': 2} | by book: {'NYB': 3, 'KNT': 2, 'BRT': 2, 'SYN': 2, 'HUB': 2, 'PHD': 2, 'HRN': 2, 'MON': 1, 'ARY': 1}
```


## [2026-09-05T20:26:00.268Z] AGENT

Verification of PDF page 133 (book page 103) is written to `/home/sfmqrb/git/rishe/data/verification/page-133.json`; `verify_check.py 133` reports 4/4 nodes, 0 PROBLEM lines.

**Counts** — root verdicts: 1 disputed. Node verdicts: 2 confirmed, 1 plausible, 1 disputed. Ref checks: 7 supports, 2 partial, 1 not_checked. Books consulted: 11 supports, 4 partial, 2 silent.

**Disputed**
- ROOT `Dhîs` "village, earth ?" — copied verbatim from Mann IEC p.191, where it is already marked "(?)" and rests only on the two words Nourai reprints. Both are now placed elsewhere: Persian *deh* < PIr. *dahyu-* < PII *\*dásyuš* (Skt. *dásyu-*, so PIE *\*d-*, not *\*dʰ-*; the -h- is the reflex of suffixal *-sy-*, Hübschmann §109a), and Greek θίς is Pre-Greek (Beekes) or belongs to *\*dheu-* (Pokorny IEW 263, Walde-Pokorny I). Buck (Nourai's own SYN:1302) says "root connections dub."
- Node #1 `dahyu, dainhu` — forms and glosses are exactly Kent p.190 and Bartholomae col. 706 and are impeccable; only the arrow from *\*Dhîs* is rejected.

**Other findings**
- Node #4 `visa-dahyu, vîspa-dahyu` is labelled **Avestan** but is Old Persian: Kent p.208 s.v. *visadahyu-* "of or for all countries or provinces", attested once at XPa 12 (Gate of All Nations). Nourai's second form is vindicated — Kent notes the Median *vispa-* variant behind the Akkadian *u-iš-pi-da-a-ʼ-i* — but Bartholomae has no Avestan compound, only the phrase *vīspanąm dahyunąm*. Marked plausible (language-label error in the book).
- BQT:902 checked from the page image (leaf n362, verified against printed ۹۰۳ on n363); Moʿin's footnote 2 gives «دیه، پهلوی dêh … پارسی باستان dahyu … اوستا daxyu … هندی باستان dásyu «اشتق ۵۸۸»». Image + transcription saved to `data/verification/sources/refs/ocr/BQT/902.png` and `902.vision.txt`.
- KNT:208 is missing from the truncated local `KNT.txt` (it stops mid-v); read from the archive.org full text of the same scan instead.
- SNS:242 partial (entry found, printed page not confirmable from the OCR); MON:1585 partial (checked via abadis, no page numbers); TZF:13 not accessible; ARY unusable (OCR noise).

**No extraction errors** — the JSON matches the printed page exactly (root name, gloss, all four boxes, Persian script, extras and the Molavi couplet). One cosmetic note: the printed page has an empty box hanging off node #4 (bottom right) that the extraction omits; it carries no text.
