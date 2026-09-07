# Verification process log — verify-page-378


## [2026-09-07T20:16:29.051Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 378 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-378.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-378.json. Write /home/sfmqrb/git/rishe/data/verification/page-378.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 378` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T20:16:31.387Z] AGENT

I'll start by reading the instructions.


## [2026-09-07T20:16:32.097Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T20:16:32.109Z] TOOL RESULT

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


## [2026-09-07T20:16:32.660Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-378.txt"
}
```


### [2026-09-07T20:16:32.672Z] TOOL RESULT

```
1	=== PDF page 378 (book page 348) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Ôus 2, Ôs, Aus 3 : mouth, lip  (refs POK:784)
4	#1 (parent #0) [Avestan] refs=POK:785; SYN:228; KLN:1091; BQT:1049 | âh : mouth ; aošta, aoštra : lip ; uz-ah, zâ 2 : push out of opening, give birth ☞Ud 1 ; zâ-dhana : child holder, womb ☞Dhě 2 ; zâ-âp : spring, river ☞Ab 1
5	  #2 (parent #1) [Persian] refs=MON:1763; IRN:108 | zeh 2 «زه ۲ ( زهیدن ، زاهیدن )» : to give birth ; zehdân «زهدان» : womb ; zahâb «زهاب ( زاب )» : river, spring
6	#3 (parent #0) [Latin] refs=AHD:929; KLN | ôs 2, ôr : mouth, face ; ôscillum : a face mask hung from a tree to swing(oscillate) in the wind
7	  #4 (parent #3) [English] refs=None | oral, orifice, oscillate ; usher
8	--- entry 1 ---
9	ROOT Ow -> redirect to Aw
10	--- entry 2 ---
11	ROOT Owo -> redirect to Aw
12	--- entry 3 ---
13	ROOT Ôwyo -> redirect to Aw
14	--- entry 4 ---
15	ROOT Ozdo -> redirect to Ozgho
16	--- entry 5 ---
17	ROOT [Indo-European] Ozgho, Ozdo : branch, bud, offspring  (refs POK:786)
18	#1 (parent #0) [Pahlavi] refs=POK:786; IEC:863 | azg : branch, offspring
19	  #2 (parent #1) [Persian] refs=BQT:114,115; IEC:863; MON:218 | azğ «ازغ» : branch, shoot ; azm «ازم» : child | extra: اژغ ، آزغ ، ازگ ۱
20	#3 (parent #0) [Sanskrit] refs=IEC:863 | adgah : stalk
21	#4 (parent #0) [Old Norse] refs=AHD:910 | oddi : bud, point, triangle, third or any odd number
22	  #5 (parent #4) [English] refs=None | odd
23	
```


## [2026-09-07T20:16:36.089Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-378.json",
 "description": "Read source JSON for page 378"
}
```


### [2026-09-07T20:16:36.136Z] TOOL RESULT

```
{
  "pdf_page": 378,
  "book_page": 348,
  "entries": [
    {
      "root": {
        "name": "Ôus 2, Ôs, Aus 3",
        "lang": "Indo-European",
        "refs": "POK:784",
        "gloss": "mouth, lip"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:785; SYN:228; KLN:1091; BQT:1049",
          "words": [
            {"translit": "âh", "gloss": "mouth", "script": null},
            {"translit": "aošta, aoštra", "gloss": "lip", "script": null},
            {"translit": "uz-ah, zâ 2", "gloss": "push out of opening, give birth", "script": null, "see": ["Ud 1"]},
            {"translit": "zâ-dhana", "gloss": "child holder, womb", "script": null, "see": ["Dhě 2"]},
            {"translit": "zâ-âp", "gloss": "spring, river", "script": null, "see": ["Ab 1"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "MON:1763; IRN:108",
          "words": [
            {"translit": "zeh 2", "gloss": "to give birth", "script": "زه ۲ ( زهیدن ، زاهیدن )"},
            {"translit": "zehdân", "gloss": "womb", "script": "زهدان"},
            {"translit": "zahâb", "gloss": "river, spring", "script": "زهاب ( زاب )"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "گیرم که خارم خارِ بد، خار از پی گل میزهد - صـرّاف زر هم می نهد جو بر سـر مثقالها",
            "poet": "Molavî"
          }
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD:929; KLN",
          "words": [
            {"translit": "ôs 2, ôr", "gloss": "mouth, face", "script": null},
            {"translit": "ôscillum", "gloss": "a face mask hung from a tree to swing(oscillate) in the wind", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "oral, orifice, oscillate", "gloss": null, "script": null},
            {"translit": "usher", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {"name": "Ow", "redirect": "Aw"},
      "nodes": []
    },
    {
      "root": {"name": "Owo", "redirect": "Aw"},
      "nodes": []
    },
    {
      "root": {"name": "Ôwyo", "redirect": "Aw"},
      "nodes": []
    },
    {
      "root": {"name": "Ozdo", "redirect": "Ozgho"},
      "nodes": []
    },
    {
      "root": {
        "name": "Ozgho, Ozdo",
        "lang": "Indo-European",
        "refs": "POK:786",
        "gloss": "branch, bud, offspring"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Pahlavi",
          "refs": "POK:786; IEC:863",
          "words": [
            {"translit": "azg", "gloss": "branch, offspring", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:114,115; IEC:863; MON:218",
          "words": [
            {"translit": "azğ", "gloss": "branch, shoot", "script": "ازغ"},
            {"translit": "azm", "gloss": "child", "script": "ازم"}
          ],
          "script_extra": "اژغ ، آزغ ، ازگ ۱",
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "IEC:863",
          "words": [
            {"translit": "adgah", "gloss": "stalk", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Old Norse",
          "refs": "AHD:910",
          "words": [
            {"translit": "oddi", "gloss": "bud, point, triangle, third or any odd number", "script": null}
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
            {"translit": "odd", "gloss": null, "script": null}
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


## [2026-09-07T20:16:36.737Z] TOOL CALL #4: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo \"---\" && cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "List verification dir and source matrix"
}
```


### [2026-09-07T20:16:36.793Z] TOOL RESULT

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
---
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


## [2026-09-07T20:17:10.599Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','SYN','KLN','BQT','MON','IRN','AHD','IEC']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:900]); print()\n\"",
 "description": "Inspect refs_online entries"
}
```


## [2026-09-07T20:17:11.376Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n '1,60p' data/verification/page-377.json 2>/dev/null || ls data/verification/page-37*.json",
 "description": "Look at a nearby example output file"
}
```


### [2026-09-07T20:17:11.938Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept head

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based l

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.c

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different paginati

IRN {"title": "Bahram Farahvashi, Iranvij, Tehran University Press 1368/1989", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ایرانویج-بهرام-فره-وشی/ -> https://dl.eliteraturebook.com/storage/img/ایرانویج.pdf (free PDF site; grey) ; Google Books kP8bAAAAIAAJ (1368 ed., no view)", "lookup_hint": "archive.org 'Iranvej' item is a radio programme, not the book; nothing on ketabnak/noorlib. | For pages in a scanned volume use: python3 tools/ref_page.py IRN:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/IRN/IRN_eliteraturebook.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/IRN/IRN_pages.txt"], "page_offset": "222 leaves; printed page = PDF page − 11 (PDF 101 = p.90; chapter openers carry no numeral). 6th printing 1382, same setting as 1368.",

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt", "page_offset": "1985 Watkins ed.: lea

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.", "notes": "", "cites": "column/page number of Mann, An Indo-Europea
```


### [2026-09-07T20:17:11.972Z] TOOL RESULT

```
data/verification/page-37.json
```


## [2026-09-07T20:17:17.354Z] TOOL CALL #7: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/page-317.json'))\ne=d['entries'][0]\nprint(json.dumps({k:v for k,v in e.items() if k!='nodes'},ensure_ascii=False,indent=1)[:2500])\nprint(json.dumps(e['nodes'][0],ensure_ascii=False,indent=1)[:2500])\n\"",
 "description": "Inspect recent output style"
}
```


## [2026-09-07T20:17:18.364Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==793||NR==794' POK_01.txt | head -120",
 "description": "Pokorny p.784-785 (leaf=p+8)"
}
```


### [2026-09-07T20:17:19.579Z] TOOL RESULT

```
{
 "entry": 0,
 "root": "Mad",
 "verdict": "confirmed",
 "modern_form": "PIE *mad- (laryngealist *meh₂d-) 'wet, dripping; fat, well-fed', with the derived sense 'food, fattening' — Pokorny 694-695",
 "note": "The root is genuine and standard. Pokorny 694-695 has 'Root/lemma: mad-  Meaning: wet; glossy, fat, well-fed, intoxicating', and Watkins/AHD (1985 ed., p. 38) has 'mad-. Moist, wet; also refers to various qualities of food' — Nourai's gloss 'wet, also food' is essentially Watkins' wording, and the language label 'Indo-European' is right. Walde-Pokorny II 230-232 is the same article. What is remarkable is that Pokorny's article contains almost the whole of Nourai's chart in the same order: 'ai. madati, madate … mada- m. Rauschtrank = av. maδa-; ai. madgu- ein bestimmter Wasservogel, ein Fisch = np. māγ ein Wasservogel; ai. matsya- m., av. masya Fisch (der nasse; Ableitung von einem -es-St. *mades-); mastu- n. saurer Rahm (*mad-stu-) … arm. macun sauer, geronnene Milch … iran. Worte für Dickmilch, so npers. mast, masīdan … lat. madeō, mattus trunken (*madi-to-s) … ahd. mast Futter, got. mats Speise, ags. mete, mnd. mat(e) Kamerad'. Two modern caveats: (a) Cheung (2007) and LIV split the family into *mad¹ 'to become intoxicated' (PIE *med-) and a separate Indo-Iranian *mad 'to curdle', for which no PIE root is set up; (b) the 'fish' member is no longer taken as certain (see node #1).",
 "note_fa": "ریشهٔ هندواروپایی آغازین *mad- (در نگارش امروزی *meh₂d-) به معنی «خیس، تر، چکه‌کننده؛ فربه و پرورده» و از همین‌جا «خوراک»، ریشه‌ای شناخته و پذیرفته است: پوکورنی (ص ۶۹۴–۶۹۵) آن را با معنی «تر؛ چرب، فربه، مست‌کننده» می‌آورد و واتکینز در پیوست فرهنگ American Heritage نیز «mad-. نمناک، تر؛ همچنین دربارهٔ کیفیت‌های خوراک» دارد؛ پس برچسب زبانی و معنای «wet, also food» در نمودار نورایی درست است. نکتهٔ چشمگیر آنکه تقریباً همهٔ شاخه‌های نمودار — سنسکریت madati و mada-، اوستایی maδa-، سنسکریت madgu- برابر «ماغ» فارسی، سنسکریت mastu- و ارمنی macun برابر «ماست» و «ماسیدن»، لاتینی mattus و واژه‌های ژرمنی mast/mats/mete/mate — همه در همان مقالهٔ پوکورنی و به همان ترتیب آمده‌اند، یعنی نورایی مستقیماً از پوکورنی و واتکینز برداشته است. دو نکتهٔ احتیاطی: نخست آنکه چونگ (۲۰۰۷) و فرهنگ LIV دو ریشهٔ *mad «مست شدن» و *mad «بستن، دلمه شدن» را از هم جدا می‌کنند و برای دومی ریشهٔ هندواروپایی نمی‌سازند؛ دوم آنکه پیوند واژهٔ «ماهی» با این ریشه امروز قطعی دانسته نمی‌شود (بنگرید به گرهٔ ۱).",
 "sources": [
  "https://en.wiktionary.org/wiki/mattus",
  "https://en.wiktionary.org/wiki/meat"

{
 "id": 1,
 "lang": "Avestan",
 "words": "masya 1 : fish; mada : having too much liquid, drunk; mad : a water bird, mina",
 "verdict": "plausible",
 "derivation": "Two of the three items are real Avestan words. (a) masiia- 'fish' (Y. 2.8, Vd. 2.8 etc.) is well attested, and Pokorny 694 derives it, with Skt. matsya-, from an -es-stem *mades- 'the wet one' — this is precisely Nourai's arrow; but Buck (p. 184) already marks it with a question mark, and current handbooks (Martínez García & de Vaan, Introduction to Avestan, p. 32; en.wiktionary s.v. Reconstruction:Proto-Indo-Iranian/mátsyas) call PII *mátsyas 'unknown; possibly borrowed from the BMAC substrate', citing the lack of any relation to *peysk- or *dʰǵʰu-, with the *meh₂d- connection only as an 'alternative theory'. (b) maδa- m. 'intoxicating drink, intoxicated ecstasy' (Bartholomae AiW 1112 'Rauschbegeisterung durch Haoma-Genuss', beside the verb maδ- 'to become intoxicated', Y. 10.8, N. 30) is exactly Pokorny's 'av. maδa- Rauschtrank' — Nourai's gloss 'having too much liquid, drunk' is a loose paraphrase but the derivation is right. (c) 'mad : a water bird, mina' is not an Avestan word at all: Bartholomae records only the verb maδ-, and the water-bird word Nourai wants is Sanskrit madgu-, which Pokorny equates with New Persian māγ ('ai. madgu- ein bestimmter Wasservogel, ein Fisch = np. māγ'). The printed page (see refs/ocr/BOOK/317.png) has exactly what the JSON has, so this is Nourai's own slip — he moved the Sanskrit/Persian bird word up into the Avestan box to give māγ a parent.",
 "derivation_fa": "از سه واژهٔ این گره دو تا اوستایی راستین‌اند. یک: masiia- «ماهی» گواهی‌شده است و پوکورنی (ص ۶۹۴) آن را همراه سنسکریت matsya- از ستاکِ ‎*mades-‎ «آنِ تر» می‌گیرد، یعنی همان پیکان نورایی؛ اما باک (ص ۱۸۴) همان‌جا علامت پرسش گذاشته و پژوهش امروزی (مارتینس گارسیا و دِ فان، ص ۳۲؛ ویکی‌واژه ذیل *mátsyas) خاستگاه این واژه را ناشناخته و شاید وام‌واژه‌ای از زیرلایهٔ باکتریا-مرو (BMAC) می‌داند و پیوند با *meh₂d- را تنها «نظری دیگر» می‌شمارد. دو: maδa- «نوشابهٔ مست‌کننده، سرمستی» (بارتولومه، فرهنگ ایرانی باستان ستون ۱۱۱۲) دقیقاً همان «maδa- = Rauschtrank» پوکورنی است و اگرچه معنایی که نورایی داده («دارای مایع بسیار، مست») دقیق نیست، اشتقاق درست است. سه: «mad» به معنی «پرندهٔ آبی، مینا» هیچ گواهی اوستایی ندارد؛ بارتولومه فقط فعل maδ- را ثبت کرده و واژهٔ پرندهٔ آبی در واقع سنسکریت madgu- است که پوکورنی آن را برابرِ «ماغ» فارسی می‌گذارد. تصویر صفحهٔ چاپی (refs/ocr/BOOK/317.png) نشان می‌دهد متن استخراج‌شده امانتدار
```


### [2026-09-07T20:17:20.860Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-07T20:17:25.672Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for f in POK_01.txt POK_02.txt POK_03.txt POK_full.txt; do printf \"%s pages=%s size=%s\\n\" \"$f\" \"$(awk 'BEGIN{RS=\"\\f\"} END{print NR}' $f)\" \"$(wc -c <$f)\"; done",
 "description": "Count pages in POK files"
}
```


### [2026-09-07T20:17:26.973Z] TOOL RESULT

```
POK_01.txt pages=363 size=981836
POK_02.txt pages=433 size=1137861
POK_03.txt pages=429 size=1170809
POK_full.txt pages=1 size=3971883
```


## [2026-09-07T20:17:31.924Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR>=18&&NR<=24{print \"=== leaf \"NR\" ===\"; print}' POK_03.txt | head -200",
 "description": "Print POK_03 leaves 18-24"
}
```


### [2026-09-07T20:17:33.203Z] TOOL RESULT

```
=== leaf 18 ===
-man-  ,Kälte',  av.  aota-  ,kalt',  ao-dar- , Kälte',  also  zu  einer  Wurzel  au-  (ou-)  ,kalt'  zu  stellen.
WP.  I  222,  WH.  I  88,  Trautmann  20,  Mühlenbach-Endzelin  1,  222  f.
ö{u)i-oza  ,Ei',  d.  h.  ,das  zum  Vogel  gehörige',  schwache  Form  9iözn.
Av.  ap-ävaya-  , entmannt' (?),  falls  aus  apa-ävaya-  ,ohne  Hode',  vgl. apers.  xäya  ,Ei';
gr.   att.  wiöv  (*öui-om),   äol.  djioy  (*öun-om),   dor.   djeov  (*öuei-07n)  ,Ei'; cymr.  wy^  acorn.  uy  ,Ei'  (*äuion  aus  *öu{om)]
784  »  ::?
ohne  w,  das  wohl  im  langdiphthong.  *öuiom  geschwunden  war:
arm.  j«,  Gen.  jvoj  ,Ei'  {*iöio-,  durch  Assimilation  aus  *özo-);  lat.  övi^t^ ,Ei*  nach  Szemerenyi  KZ.  70,  64f.  aus  lat.  *oom,  idg\  *ö2om;
aksl.  ajhce^  slov.  ^o/ce,  acech.  vojce^  cech.  ve;ce  (*öia-  n.)  ,Ei'  ;
schwierig  sind  krimgot.  ada  (got.  *addja),  aisl.  e^r^,  ahd.  ei,  ags.  $« ,Ei*  (germ.  *ajjaz--  ahd.  Fl.  ei^r,  ags.  zgru  erweisen  -es-Stamm);  vielleicht nach  Specht  aus  *9tom,  nicht  verkürzt  aus  urgerm.  *äiiam,  idg.   *öiom.
WP.  I  21  f.,  WH.  II  230,  Trautmann  202,  Specht  Idg.  Dekl.  29;  Specht erklärt  lat.  avis  , Vogel*  aus  dem  endbetonten  idg.  Nom.  Sg.  awm;  y^i oben  S.  86,  wo  ich  noch  gr.  oicovög  ^Raubvogel*  (aus  *alü)v6g,  W.  Schulze Kl.  Sehr.  662)  hätte  erwähnen  sollen.
öui'S  m.  f.  , Schaf,  Gen.  Sg.  öuios-  f.  ouikä  ds.
Ai.  dvi-  m.  f.  jSchaf,  avika-  m.  ds.,  avikä  ,weibliches  Schaf  (=  abg.  ovhcaY dvya-  ,vom  Schaf,  vgl.  gr.  ota;  arm.  hov-iio  (*oui-pa-)  , Schäfer';  gr.  5'tg,  olg (argiv.  Akk.  PI.  ofivg)  , Schaf ,  oXeog  ,vom  Schafe*,  ola,  Ba  , Schaffell',  dehn- stufig ^a  , Schaf  feil,  Saum'  (wie  ai.  ävika-  n.) ;  lat.  ovis^  umbr.  oui^  uvef  Akk. PI.  ,oves'  {au-huhulcus  ,pastor  bovum',  auch  avillus  ,Lamm',  s.  u.  ag^hnos)-, air.  öi  ,Schaf;  cymr.  ewig,  acorn.  eiihic  ,cerva'  {*oulkd)',  aisl.  «r,  ags. eowu,  eowe,  as.  ewi,  ahd.  ouioi,  o«  , Schaf  {^awl,  Gen.  *awjöz),  got.  awistr jSchafstall',  ags.  eowestre  ds.,  ahd.  awist,  ewist  (mit  zu  stä-  , stehen'  ge- hörigem 2.  Gliede  -sto-,  -s^[9]<ro-),  got.  atoepi,  ags.  eowde,  ahd.  ewü  ,Schaf- herde*;  lit.  avts,  lett.  avs  f.  ,Schaf*;  lit.  ävinas,  lett.  avins,  äuns,  apr. awins  , Widder'  =  abg.  ovh-m  ds.;  abg.  ovb-ca  , Schaf.
WP.  I  167,  WH.  II  229,  Trautmann  20f.
I.  öus-  :  9US-  .Mund,  Mündung,  Rand' ;  9us-tä , Lippe',  Qus-tiiom  , Mündung'.
Auf  idg.  *öus  gehen  zurück:  ai.  ä-h  n.  ,Mund'  (vgl.  äs-dn-  sd.,  äsydm  n. ,Mund,  Öffnung'),  av.  äÄ-,  ärdhan-  ds. ;  lat.  ös,  öris  ,Mund,  Antlitz,  Rand, Ufer' ;  aber  mir.  ä  Gen.  Sg.  ,Mund'  aus  *ösos ;
dazu  ä- Ableitung:  ved.  äsayä  ,von  Mund  zu  Mund'  (Instr.);  lat.  öra ,Rand,  Saum,  Grenze,  bes.  Meeresküste',  dazu  cöram  Adv.  (u.  Präp.)  ,an- gesichts,  in  Gegenwart,  vor',  
=== leaf 19 ===
Nachbildung  von  palam,  dam  aus  *co-öro- ,vor  dem  Angesicht  befindlich';  aureae  {öreae)  ,Gebiß  am  Zaum^  davon auriga  {öriga)  ,Wagenlenker'  {-igä  zu  agö)-  ösculum  ,Kuß'  ist  Demin.  von  ös;
aisl.  öss  m.  »Flußmündung'  (germ.  *ösaz\  hierzu  ags.  ör  n.,  öra  m. ,Rand,  Anfang';  aus  ags.  ör  ist  mir.  or  ,ora,  margo,  linea',  acymr.  ör  ds. entlehnt.
Die  schwache  Stufe  idg.  *ous-  erweist:  alb.  ane  ,Seite,  Saum,  Ufer, Borte'  {*ausnä)',  eventuell  auch  hitt.  aÜ,  Gen.  Üsas  n.  ,Mund'  (*aies *ai*os)?  s.  Pedersen  Hitt.  47  f.
785
f-Ableitungen  sind  ai.  östha-  m.  n.  ,Lippe*;  av.  aoHa-^  aostra-  ds.  (*9iw-), Int.  östium  , Eingang,  Flußmündung'  (=  slav.  *ustbje);  aksl.  usta  PL  ,Mund'; slav.  "^usthje  n.  ,Münduag'  ist  anzusetzen  nach  bulg.  üstije^  russ.  üsttje usw.;  vgl.  aksl.  usthna,  slov.  üstna  , Lippe';  aksl.  ustiti  (naustiti)  ,bewegen, anregen»  überreden';  wahrscheinlich  aksl.  wzdia  usw.  ,Zaum';  lett.  ap-aüH f*.austi-)  ,Hal£ter' ;  apr.  austo  ,Mund'  (Nom.  Plur.  ? ;  Akk.  Sg.  äustin\ lit.  duscioti  , schwatzen,  munkeln',  lett.  ausdt  , schwatzen';  ablautend  lit. uosta  f.,  üostas  m.  , Flußmündung,  Haff',  lett.  uosts  m.,  uösta  f.  , Hafen'.
WF.  I  168  f.,  WH.  n  224f.,  Trautmann _19  f.
2.  ous-  :  9US- :  us~  ,Ohr',  erweitert  mit  -i  (pusi-s),  -es  (qusos-  n.)  und  -en.
Av.  usi  Nom.  Du.  ,die  beiden  Ohren,  Verstand,  Sinn',  Instr.  Du.  usi-hya, npers.  hos  (iran.  *au§-)  ,Ohr';
arm.  unlcn  ,Ohr'  (*us-on-ko-m)  •  das  kn  nach  akn  ,Auge';
gr.  dor.  (bg  (*öus)  ,Ohr';  öu  auch  in  öjJ^ara  , Ohren'  Alkm.,  äficp-wsg Theokr.  ,mit  zwei  Henkeln',  dor.  i^-wßddia  , Ohrringe',  vTtsQ-cbirj  , Gaumen', att.  lay-cbg,  hom.  lay-coog  n.  ,Hase'  (*sbg-öusos)  ,mit  schlaffen  Ohren'; 3US-  in  gr.  lak.  a'ög  ,Ohr',  PI.  äavd-a  {^ava-avd-a)  Alkm.,  tarent.  äxa (*av(jara)]  ion.  rtaQ-rj'ioVj  att.  Ttcco-sla^  lesb.  Ttaq-ava  , Schläfe'  (:  air.  arae)-^ gr.  ous-  (Kreuzung  des  nominativischen  öus-  mit  dus-)  in  att.  oi)g  (*odaog) ,Ohr*,  hom.  Gen.  o^axog  {*ova'i}Tog),  (bytlösg  , Ohrringe'  Hes.  (*ous-n-ko-)'^ über  dy.ova)  s.  oben  S.  18,  587 ;  über  att.  dyLgcaad-ai  {*a'/.Q-ovg-)  s.  Schwyzer Gr.  Gr.  1,  348;
alb.  vesh  m.  ,Ohr'  (*öms-,  ös-);
lat.  auris  f.  ,Ohr'  (*ausi-s)'j  aus-cultö  ,horche'  s.  oben  S.  552;
air.  äw,  ö  n.  ,Ohr'  (^*dusos-)'^  air.  arae  m.  , Schläfe'  {*par-ausios)f  Plur. im  ON  Arai-,  gall.  ON  ilrawsiö  ,Orange'  (Thurneysen  KZ.  59,  12);  PN Su-ausiä  L  ,mit  schönen  Ohren';
got.  ausö  n.
=== leaf 20 ===
  ,Ohr'  (germ.  *ausan-) ;  mit  gramm.  Wechsel  (*auzan-) : aisl.  eyra,  ags.  eare,  afries.  are^  as.  ahd.  öra  n.  ,Ohr';  davon  ahd.  ö7'i, mhd.  CBre  ,ÖÄr' ;
lit.  ausis  f.  (älter  auch  m.),  Gen.  PI.  ausy,  (konson.  St.),  lett.  äuss  f. ; apr.  Akk.  PI.  aus  ins  ,die  Ohren',  daneben  ausins  Vok.  m. ;
aksl.  ucho^  Gen.  usese  (s-St.).
WP.  I  18,  WH.  I  85 f.,  Trautmann  18  f.,  Schwyzer  Gr.  Gr.  1,  348,  520.
ozdo-s  ,Ast'.
Arm.  ost  , Zweig,  Ast',  gr.  bZog  ds.,  got.  asts,  ahd.  a
=== leaf 21 ===
st  ,Ast';  mit  Vriddhi *özdos  in   ags.  öst,  mnd.  öst  , Knoten  im  Holz,  Knorren^   (==   ,die  Stelle,
50
786
wo  ein  Ast  vom  Stamme  aasgegangen  ist');  wohl(?)  -ozdo-s  ,(am  StammeV ansitzend',  s.  Präfix  's-,   o-  und  sed-  ,sitzen'.
WP.  I  186,  W.  Schulze  KZ  63,  28.  ''
ozgho-  , Knospe,  Pflanzentrieb,  Zweig'??
Pehl.  azg  ,Ast',  npers.  azay  , Zweig,  Knospe' :  gr.  öa^og,  oaxrj^  dju'/r) , Zweig,  Schößling^;
die  gr.  Worte  eventuell  auch  eine  dem  idg.  *o-zdos  ,5tog'  parallele  Zu- sammensetzung o-zgho-  (:  s'xü),  gxeIv)  ,sich  (am  Stamm)  festhaltend'?
WP.  I  185,  Schwyzer  Gr.  Gr.  2,  491.
p."
oä''-P^~  ^^^  pä-t- :  p9-t-  , füttern,  nähren,  weiden';  Abstraktum  pä-tro-. Arm.  hauran  , Herde'  {*pä-tro-),  hoviv  .Hirt'  (*oui-pä-)]  gr.  dor.  navia' fcXv(y^ovfj^  nävia '  t«  nXrjG^ia ;  lat,  päscö,  -ere,  pävi,  pästum  , lasse  weiden, füttere',  Dep.  , fresse,  weide'  (*päs-scö),  pästor  ,Hirt',  päbulum  , Futter' (*pä-dhlom),  pänis  ,Brot'  (wegen  pastillus  ,Kügelchen  aus  Mehl'  aus  *pa-st- nis);  messap.  rtavög  ,Brot'  ist  lat.  Lw. ;  air.  ain-chess  , Brotkorb' ;  vielleicht als  ven.-illjr.  Element  im  Keltischen  *pä-rO'  , Weide'  in  cymr.  pawr  , Weide', ri.  porion,  davon  Verbalnom.  porij  mbret.  peuriff,  bret.  peuri  ,Weiden'; mit  'tro-  Suffix  aisl.  födr  n.,  ags.  födor  n.,  ahd.  fuotar  , Futter' ;  aksl.  pasg, pasti  , weiden'  (*päs/cö);  toch.  A  päs-,  B  päsk-  , hüten' ;  hiti.  paM-{pahhas-) , schützen'.
Mit  -t'  Weiterbildung:  gr.  ftarsof-iai  ,esse  und  trinke*;  fxrtaaroq  ,ohne Speise  und  Trank';  unsicher  air.  äs{a)id  , wächst'  (,es  mehrt  einen'),  mir. äs  , Wachsen'  {^pät-to-)\  got.  födjan  , ernähren',  aisl.  feda,  ags.  fedan,  as. födian,  ahd.  fuoten  ds.,  ags.  föda,  engl,  food  , Nahrung',  ags.  föstor  ds., aisl. /ös^r  , Erziehung,  Unterhalt'  (*pät-tro-)]  ablaut.  ahd.  kauatot  ,pasta'  (ahd. Gl.  2,  333,  65),  fatunga  .Nahrung',  mnd.  vedeme  f.  , Eichelmast'.
WP.  II  72 f.,  WH.  II  246 f.,  260,  Trautmann  207 f.;  vgl.  auch  1.  pen- , füttern'.
päk-  und  päg-  , festmachen',  teils  durch  Einrammen  (Pflock,  Pfosteii),  teils
durch   Zusammenfügen  (Fuge;   festgefügt,  kompakt,  fest;   z.  T.  auch
Fessel,  Strick);  Präs.  *päg-mi, päk-si, päk-ti]  p^go-  ^Umschließung'.
Ai.   pdi-    (Instr.    PI.   padbhih)    , Schlinge,    Strick',  päsa-   m.    ds.,    pajrd-
, gedrungen,  stark' ;
av.  pas-  , aneinander  befestigen,  zusammenf�
=== leaf 22 ===
�gen',  fsdbiS  ,mit  Fesseln' (über  pourupaxsta-  ,viel,  reich  gefaltet'  s.  Benveniste  BSL.  29,  106  f.) ; gr.  Ttaaaalog,  att.  TV&TraXog  m.  , Pflock,  Nagel'  (-xt-),  Ttr^aau)^  att.  Ttrjzxo) „TtrjywfXL^^  ]  Tzrjyvvj.u  (dor.  -ä-)  , befestige  durch  Hineinschlagen,  Hinein- stecken; lasse  erstarren'  (iTtüyrjv,  TtSTtrjya,  7t7]xT6g),  ftfjyfj.a  n.  , Pflanze,  Gestell', Tt7]yög  ,fest,  stark',  itrjyavov  n.  , Raute',  vav-7irjyög  , Schiffbaumeister',  TtTjyvUg Adj.  f.  , reifig,  eisig',  jtdyog  m.  ,Eis,  Reif  (auch  Dat.  PI.  irrdyeai  , Frost'),  hom. , Felsspitze,  -klippe';  nax^r]  (*7ta^va)   ,Reif,  Frost',  frdyr]   , Schlinge,   Falle'»
^)  S.  auch  unter  Sp-.
50*
788
TvaY.TÖü)   ,mache   fest,   verschließe,    verstopfe',   ä-^a^   ,einfach* ;    Ttd^   Adr.  f ,g-enug!';  hierher  Ttrjyrj,  dor.  näyd  , Quelle';  —
lat.  paclscö  (sek.  -or)  ,einen  Vertrag-  oder  Vergleich  festmachen,  ab-  ' schließen',  alat.  paciö  ,pactiö',  pacunt  ,paciscuntur',  pax,  -eis  t  , Friede- freundliche  Gesinnung'  (umbr.  pase  tua  ,päce  tuä'  in  der  Anrede  an Gottheiten),  palus  , Pfahl'  (aus  *paJc-slos,.  vgl.  Demin.  paxülus)]  pangö (jpepigi',  geneuert  pegi  nach  fregi,  und  panxi)  , befestigen,  einschlagen- aneinanderfügen,  schriftlich  verfassen,  festsetzen'  (zur  Nasalier ung  des Präs.  vgl.  germ.  ^faiBian),  compäges  ,Fuge',  pägina  (*  die  zum  Blatt  ge- fügten Papyrusstreifen)  ,Blatt  Papier,  Seite,  Kolumne',  2>ägus  , Landge- meinde, Dorf,  Bau',  pröpägö,  pr^päges  , Setzlinge',  propägäre  , einen  Setzling in  der  Erde  festmachen,  daher  fortpflanzen';  umbr.  pase  (s.  oben),  paca Adv.  , causa',  osk.  prupukid  ,ex  antepacto?',  umbr.  päl.  marruc.  pacri- ,propitius,  pläcätus';  mir.  äge  , Glied,  Pfeiler'  (*pägio-),  äil  ,angenehm'  ^ (*pägli-]  oder  als  *pökli-  zu  3iis\.  fcegiligr  ds.,  s.  l.*pek-?)]  cymr.  aelod , Glied'  (*paglätu-)  •
germ.  Nasalpräs,  ^faidyan  (:  \dX.  pango)  in  ^ot.  fähan,  aisl.  /ä,  ags./ön, ahd.  fähan,  as.  fähan  und  fangan  , fangen',  got.  gafäh  n.,  aisl.  fengr, ags.  feng  m.,  ahd. /aw^  m.  ,Fang,  Beute';  ahd.  fuoga  ,Fuge',  gafuogi ,passend',  hi-fuoge  ,Ehestifterin',  ahd. /wo^ew,  as.fögian  , fügen',  ags.  gefegan »passen,  verbinden',  mhd.  vagen  , fügen',-  von  *pag-:  as.  fac  , Umfassung, Umzäunung',  mnd.  vak  m.  ds.  und  .Abteilung',  ahd.  fah  ,moenia',  nhd. Fach,  einfach]  von  zeitlicher  Abteilung  ags.  foec  , Zeitraum',  mnd.  vaken, vake,  spätmhd.  gevach  ,oft',   mhd.  drler  vacher  , dreimal' 5
slav.  *paza-  m.  in  sloven.  päz  ,Fuge',  päz  , Bretterwand'.
WP.  II  2  f.,  WH.  II  232 f.,  235 f.,  245  f.,  Trautmann  209.
päii-  , Gewebe'.
Gr.  Ttrjvog  n.,  ic^vr]  f.  , Gewebe'  Hes.,  Ttrjviov  , aufge
=== leaf 23 ===
wickelter  Faden, Gewebe,  Gewand',  7trjVi^oi.iaL  ,webe'  (dor.  TtäviadsTai  Theokr.);  ablaut. lat.  pannus  ,Tuch,  Lappen'  (expressives  nn);  got.  fana  m.  ,Lappen, Schweißtuch',  ahd.  fano  ,Zeug,  Tuch',  nhd.  Fahne,  ags.  fana  m.  ,Fahne, Tuch;  Iris', /ane, /anw  f.  ,Fahne,  Schwertlilie';  unklar,  mir.  an-art  ,lei- nernes  Tuch';  dürfte  man  das  gr.  und  lat.  ä  als  expressiv  auffassen  (vgl. oben  S.  211  zu  gall.  drappus),  könnte  Beziehung  zu  {s)pen-  ,spannen, spinnen^  angenommen  werden.
WP.  II  6,  WH.  II  247  f.
pando-s  , gekrümmt'.
Lat.   pandus    .gekrümmt,    gebogen,    geschweift'    (pandö,    -äre    , biegen, krümmen')  =  aisl.  fattr  {*fanta-)  ,zurückgebeugt,  zurück^ebo-en'. WP.II  6;  s.  unter  1.  pet-.
789
aak',  P^^S~  »schwellen',  bedeutungs-  und  ursprungsverwandt  mit  ba^mb- pa^mp-,  bu-,  pu-  usw.  (oben  S.  94  f.)  , aufblasen,  schwellen'.
Lat.  pänus  (*pank-no-)  , entzündliche  Geschwulst,  Büschel  der  Hirse', rom.  p^'^'^  j  davon  pänlcum  , Pflanze  mit  einem  Büschel' ;  panceps  „e'Axog xtrjyovg  irti  rgaxrjUov"^  Gloss.  (aus  *päno-caps),  pantex  , Wanst,  Gedärme' fauf  Grund  eines  Partiz.  *panc-to-s  , geschwollen,  aufgeblasen');
aksl.  pgciti  se  ,infläri',  pgcina  ,mare',  poln.  pqh  .Knospe',  pek  ,Bündel', russ.  puk  , Bündel,  Büschel,  Strauß',  püca  , Blähung'  usw.;  mit  Media aksl.  pggy  ,corjmbus',  pggvica  ,globulus'.
WP.  II  6,  WH.  II  248.
pap(p)^  Kinderlallwort  für  , Vater;  Speise'.
Gr.  Ttdnrca  Vok.,  -ov  Gen.  ,Papa',  TCctTtaq'  Ttargög  vno'AOQio^a,  TcartTtog Großvater'   (daraus  lat.  pappus),   TtaTcrciag  , Väterchen',   nanTcaCeiv   .Papa sagen';   skyth.  Zevq  JJaTtalog'^   \a.t.  päpa,  pappa  Kinderlallwort  für  , Speise; Vater',  pappö  -äre  , essen';   nhd.  pappen   , essen'  (mit  stockender  Lautver- schiebung durch  nebenhergehende  Neuschöpfung). WP.  II  4,  WH.  II  249,  250;  vgl.  appa  oben  S.  52.
pär-  , zeigen;  sichtbar  sein'.
Gr.  fcsTtocQstv  ,vorzeigen',  Ttsfcagsvat^ov  e'öq)QaGTOv,  aacpig  Hes. ;  lat. päreö,  -ere  ,erscheinen,  sichtbar  sein,  sich  zeigen;  Folge  leisten,  gehorchen', appäreö,  compär
=== leaf 24 ===
eö  , erscheine'  (parret,  nach  Festus  für  päret,  wie  baca  : bacca  usw.).
WP.  II  6,  WH.  II  252  f.
parikä  ,Buhlerin,  Konkubine';  nur  iran.  und  irisch.
Av.  pairikä    , dämonische   Buhlerin',    mp.  parlk,    np.  patn    ,Peri'    (iran. *parlka)]  mir.  a{i)rech  , Konkubine'. Thurneysen  IF.  42,  146  f.,  WP.  II  7.
päsö-s  , Verwandter'?
Gr.  TCTjög,  dor.  rtadg  , Verschwägerter',  naatTai'  ovyysveig  lies.;  lat.  päri- clda  (*päso-kaidä)  jünger  parri-czda  .Mörder  an  nahen  Verwandten';  nach Wackernagel  Gnomon  6,  458  aus  *parso-clda  zu  ind.  purum-  ,Mensch' aus  ai.  '^pursa-.
WP.  II  7,  WH.  II  253  f.
pasto-  ,fest'.
Ai.  pastyd-m  ,Wohnsitz' ;   arm.    hast   (i-St.)   ,fest';   aisl. /as^r,  3i^s.  fcest, as.  fast,  ahd.  festi,  nhd.  fest. WP.  II  7  f.
790  •
paus-  ,los-,  ablassen'.
Gr.  Tiavo)  ,mache  aufhören',  Med.  ,höre  auf,  lasse  ab',  navXa  ,Ruhe', 7iavGu)Xri  ,Rast' ;
apr.  pausto  ,wild',  aksl.  pusU  ,öde,  wüst';  pustüi,  russ.  pustüh,  puskäh ,(los)lassen',  sloven.  delo-pust  ,Feierabend'  usw.
WP.  II  1,  Trautmann  208  f.
päuson-  :  püson-  , Göttername'.
Ai.  Püsdn-  m.  ,vedischer  Gott^  Hüter  und  Mehrer  der  Herden  und  des menschlichen  Besitzes  überhaupt',  gr.  U&v,  ark.  Jj&ixjv  (^TIgvgwv)]  iWyv. (messap.)  PN  Pausö,  -onos,  gall.  (venet.)  PN  Fusa  m. ;  unsicher,  ob  zu  ai. pusyati,  pumäti,  pösati  ,gedeiht,  wächst  zu,  macht  gedeihen,  ernährt', pösa-  m.  , Gedeihen,  Wachstum' ;  s.  unter  1.  pu-.
WP.  II  2;  vgl.  Charpentier  Idg.  Jb.  19,  90.
1.  p^d-,  pBd-  , fassen;  Gefäß';  pedo-  , Gefäß,  Einfassung'.
Ai.  vielleicht  palla-  m.  , Kornbehälter',  palll  .Getreidemaß'  (falls  -II-  aus -dl-)]  ahd.  fazzön,  mhd.  vazzen  ,in  ein  Gefäß  tun,  fassen,  rüsten,  sich bekleiden',  ahd.  fezzil,  mhd.  vezzel  ,Band,  Fessel',  ags.  fetel{s)  m.  , Gürtel', aisl.  fetill  m.  , Schulterband'  (germ.  *fatila-),  ahd.  vazz  , Behälter,  Kasten', as.  fat  n.  , Gefäß',  ags.  faet  n.  , Gefäß,  Faß',  aisl.  fat  n.  , Gefäß,  Kleid'; 3Lgs.  ßetels  ,Gefäß',  ahd.  givazzi  , Bagage',  mhd.  gevxzze,  nhd.  , Gefäß';  got. fetjan,  ags.  fäetan  , schmücken',  aisl.  fseta  ,es  mit  jemandem  zu  tun  haben (,schmücken'  aus  , schön  tun  mit?');  lit.  pMas  , Getreidegarbe',  lett.  peda ,Bund,  Armvoll',  ablaut.  lit.  püodas,  lett.  puods  m.  ,Topf'.
WP.   II  22,  Trautmann  227.
2.  ped-,  päd-  m.  ,Fuß' ;  Nom.  Sg.  p^ts.  Gen.  ped-es/-ös,  Nom.  PI.  ped-es]
verbal    .gehen,    fallen';  pedo-m    ,(Fuß)boden,    Platz',    pedö-,    pedä ,Fußspur'  u.  dgl.;  pedio-  ,den  Fuß  be
```


## [2026-09-07T20:18:00.745Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== AHD ozdo/oddi ===\"; grep -n -i -E 'ozdo|oddi|^os-|ozgho' AHD_watkins1985.txt | head -40; echo \"=== AHD os- mouth ===\"; grep -n -B2 -A20 '^ōs-\\|^os-\\. Mouth\\|Mouth\\.' AHD_watkins1985.txt | head -60",
 "description": "Grep AHD Watkins"
}
```


### [2026-09-07T20:18:00.831Z] TOOL RESULT

```
<persisted-output>
Output too large (29.7KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/tool-results/bcw31t1ch.txt

Preview (first 2KB):
=== AHD ozdo/oddi ===
145:A generic term for “fish” existed, dhghi- (also peisk- in Europe). The salmon (laks-) and the eel (ang”hi-) were known, the latter also in the meaning “snake.” Several birds were known, including the crane (gere-?), the eagle (or-), the THRUSH (trozdo-), the STAR-
812:os-. Ash tree. Germanic “aski- in Old English zsc, ash: ASH?2. [Pok. 6s- 782.] 6s-. Mouth. 1. Latin ds (stem 6r-), mouth, face, orifice, and derivative dstium (< suffixed form *6s-to-), door: ORAL, OS!, OSCULATE, OSCULUM, OSTIARY, OSTIUM, USHER; INOSCULATE, ORIFICE, ORINASAL, OROTUND, OSCITANCY, PERORAL. 2. Possibly Latin auriga, chari- oteer (< *6r-ig-, “he who manages the (horse’s) bit”; -ig-, driving, from *ag-; see ag-): AURIGA. [Pok. 1. 6us- 784.] ost-. Bone. 1. Latin os (stem oss-), bone: 082, OSSEOUS, OSSICLE, OSSUARY; OSSIFRAGE, OSSIFY. 2. Greek osteon, bone: OSTEO-; ENDOSTEUM, EXOSTOSIS, PERIOSTEM, SYN- OSTOSIS, TELEOST. 3. Suffixed form *ost-r- in: a. Greek ostrakon, shell, potsherd: OSTRACIZE, OSTRACOD; b. Greek ostreon, oyster: OYSTER; C. variant form in Greek astragalos, vertebra, ball of the ankle joint, knuck- lebone, Ionic molding: ASTRAGAL, ASTRAGALUS. [Pok. ost(h)- 783.] ous-. Also aus-. Ear. 1. Suffixed form *ous-en- in Ger- manic *auzan- in Old English éare, ear: EAR}. 2. Suffixed form *aus-i- in Latin auris, ear: AURAL!, AURICLE; AURIFORM, ORMER. 3. Latin auscultdre, to listen to (*aus- + *kli-to-, inclined; see klei-): AUSCULTATION, scouT!. 4. Suffixed basic form *ous-os- in: a. Greek ous (stem 6t-), ear: OTIC, OTO-; MYOSOTIS, PAROTID GLAND; b. Greek Jagés, hare (< */ag-ous-, “with drooping ears”; *lag-, to droop; see slég-). [Pok. dus- 785.] owi-. Sheep. 1. Germanic *awi- in Old English ewe, eowu, ewe: EWE. 2. Latin ovis, sheep: OVINE; OVIBOS. [Pok. oui-s 784.] pa-. To protect, feed. Contracted from *pas-. 1. Suffixed form *pé-trom in Germanic *fodram in: a. Old English fédor, fodder: FODDER; b. Old French feurre, fodder: FORAGE; C. Old French forreure, 
...
</persisted-output>
```


## [2026-09-07T20:18:02.085Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== IEC ozgho/ozdo ===\"; grep -n -i -E 'ozgho|ozdo|azg|adgah|adga' IEC.txt | head -40",
 "description": "Grep Mann IEC"
}
```


### [2026-09-07T20:18:02.153Z] TOOL RESULT

```
=== IEC ozgho/ozdo ===
757:asgo(n), ið(n), io “ash, dust Arm. aCiwn (i-st. ash); Gk. áza; Go. azgo; OHG ON aska & com. Gmc.
903:azgo(n), see asgo(n)
1405:ON blanda, all sv. 7 *mix, stir beside OE blendan (uml.) “blind, deceive, confuse’; OCS blozdo, bloditi ert": Latv. (EW?) blandities *wander. Noun forms include OE bland; ON bland ‘mixture; fornication’; OCS blodü and common Sl. “error; fornication'; Li. blandai ‘thickening’; blandà, f. “sediment, dregs; dusk’; blandüs ‘dim, dark bhloné- (?)
1410:bhlosk- “bright; brightness. Variant of bhlusk-, q.v. Mir. blosc 'clear, evident? beside bloscad ‘radiance’. Ambiguous cf. bhlusk-); Li. blas- kù, éti “flash? beside (variant) blazgü, id.
3085:“twist, turn, spin (tr.); Ir. cf. (?) dreas (“bout, turn”, if for *dhre&hso-) (dhrën-, see dhrān-. Vocalism ambiguous in Gk. & Gmc.) Gk. cf. ten-thréne (‘bee or *wasp"); an-thrén& ‘wild bee’; thrénos ‘dirge; OS dràn, Let ‘drone’; OE dræn beside dran, id. (*-oi-?) dhreng- (dhrong-) "wer Go. drigkan, OHG trinkan, etc. («drink', and com. Gmc.); Li. drengiü, ti ‘sleet, pour w. rain’; o-gde in Sw. drank ‘mash; barm’ as well as in G Ge-trank, E to drench, etc: R (Ð cf. driàzgi ‘dirt; twaddle’ (but Pol. drzazga “chip, splinter, log? may be of Wh. R. origin) dhrengh- “slow, sullen, sad, limp, hanging”. Cf. WP I, 813 Per. dirang ‘slow’; Tokh. A trànk-, B treñk- ‘hang’; W dreng, adj. ‘surly’; R cf. drjàgat, drjagnüt ‘dangle’; Li. drengiü, ti (1) “wear out dhrésó, ið (?) “shout, rave’ Gk. thréo ‘shriek’; ON dræsa, f. ‘twaddle’; Latv. cf. (o-gde) draséju ‘yodel, jubilate? dhreudo, io, dhroud-, dhrud- “bully, illtreat, threaten’. Cf. WP I, 870 NG triezen ‘twist, tug, bully); MHG (z-gde) trutzen ‘defy’; Li. (o-gde) draudžiù, draüsti ‘warn, ban’; Latv. draudu, ét ‘threaten’ dhreugh- (1), dhrugh- ‘harm, deceive’. Cf. WP I, 860 & 874 Skt. drohah ‘harm, wrong’; drühyami ‘hurt, offend’; Av. druž- ‘deceive’ beside druxš-, o-gde in draoxš-, id.; LW in Arm. držem, id.; MHG (regen, id. beside (z-gde) troc, gs troges ‘deceit; OS driogan; Du. be-driegen *cheat'; Av. cf. draoyo; Per. durüy ‘falsehood’ dhreugh- (2), dhrough- “good, fit, sprightly, pleasant'. See dhrough- Lat. cf. ? fruor (ambig. ‘enjoy’, if distinct from früx, -gis, frügalis, etc. See bhrüg-); Br. dréó ‘gay, tipsy’; OE dreog ‘fit, sober, serious, gentle beside dréogan ‘behave, experience’; ON drjúgr ‘substantial, lasting’; Li. (o-gde) draugùs ‘sociable’ dhreus- ‘crumble, fall; crumb, fragment(sy Arm. cf. eyğiwr (2) ‘husks’; OE drēosan, v. ‘fall, perish’; drēor, m. ‘blood’; Ukr. cf. dru-
4773:Go. cf. gadi-liggs ‘kinsman’; OHG gato, MHG gatte, OS gi-gado ‘pal; OE gada, id. beside gæd ‘company’, giedd “song, tale’; LG gàd, adj. “pleasant, comfortable”; cf. gad-lich “exact; nearly full-grown’; G gátlich ‘nice, suitable”; OFris. gedda, v. ‘fit, suit; G gatten, v. ‘pair’; EMDu. gade, s. ‘mate’; weder-gade ‘equival- ent’: cf. also E gather, to-gether; G er-gattern; Du. gaderen, ver-; OCS godü “hour, time’; R ‘year’; Cz. hody, pl. ‘feast’; OCS cf. godé, adv. ‘suitably’; Latv. gads ‘year’; cf. Cz. hodina ‘hour’; Srb. godina, f. ‘year’; Li. gadyne ‘epoch, period’. Verbal forms of type *gho- dheio (-iið) in MHG gaten ‘meet, fit’; OFris. gedda “fit, suit’; OCS goZdo, goditi “be suit- able’; Cz. hoditi se, id.; Li. gadiju, ti, v.
6927:W cegyr ‘hemlock’; Li. kekeras (R ‘grozdov-
10309:mand- (2) Skt. mandah ‘slow, limp, dui; OCS mozdo, mọditi ‘hesitate’
10436:fuddled'; W meddw ‘tipsy’; Cor. medhow, Br. mezó, id.; OCS medovü ‘honeyed, sweet médhigos, à “extract, sap, whey, sour milk, juice, essence'. (Variant moidhigos beside més-, mois-^). Skt. cf. médhajah ‘from sacrifice’ beside mé- dhah “juice, essence’; MIr. medg ‘whey’; Ir. meadhg, gs meidhg & mídhg, m. id.; Gallo- Lat. mesga id. (LW in Fr. mégue); OBrit. meid, id.; W maidd, Cor. myth, m. id.; EMDu. cf. meij-kaas ‘curds’; Sw. cf. mes-ost ^whey- cheese’; OCz. miezha, Cz. míza, Pol. miazga (‘sap’, fr. *mëdhiga). (Origin of G Matte un- certain) medhianos (medhionos) *midmost'. See fol- lowing entries Skt. cf. madhyanyah (sic), id.; Per. miyan ‘inside; between; waist, middle; miyane “middle; between’; Kurd. mijan (mi£an) *front-half of plough-beam'; Arm. mi£in, gs miéno, o-st “midmost'; Gk. cf. mesiáne, f. (intermediate layer of cement or sim.); Alb. mi, gs mie ‘heartwood’; Lat. medianus *mid- most'; Mir. medón, Ir. meadhón, meodhan, m. ‘middle; W mewn, prp. ‘inside’; i mewn, adv. id.; OE cf. on middan “in the middle ON meðan ‘meanwhile’; R cf. meZeni, f. *mid- summer”; Cz. cf. mezenec, m. ‘middle finger” medhiol- (medhil-, medhol-) Lat. cf. medulla *marrow, pith'; Ir. méadal, f. ‘paunch’; MHG mittel, adj. & sf., sn. *mid- die; OE middel, adj. & n. id.; ON meðal, miðil, in the phrr. á ~, í — “amid, among medhiomos (medhimo-, medhoamo-) "mid. most. WP II, 261 Skt. madhyamáh; Av. maóomo; Oss. mídámá, adv. ‘inward’; Gk. méson, adv. ‘between’; Alb. i mesëm “midmost? beside ndér-mjemé ('in- termediate’, fr. *enter-medhom-); Osc. messi- mass, fpl.; Go. miduma, f. id.; OHG mittamo, mëtemo ‘mediocre’; OE medeme, meodume, id.; ON mjóóm, pl. mjaómir, f. ‘waist’; Sw. cf. medan ‘while’; MHG mitten, mittene, id. medhio-nokt- *midnight Gk. cf. meso-nüktion, mesa-^; Alb. mes-naté; Romance in It. mezzanotte, Rumansch mez- zanot; OFr. & Fr. minuit; OW meinoeth; MHG mitte-naht; OE midde-neaht, -niht; ON
10686:mesgü (mezg-) (2) 'immerse, soak, steep; plunge’. See next and cf. mosg- (2) WP II, 300. Variant: mosg- in Gmc. and Baltic Skt. májjami, májje, pp: magnah ‘sink’; Lat. mergo, Gre “dip, immerse; overwhelm’; Sw. mäska 'infuse with hot water; mäsk, m. *brewer's mash, residue from malt'; E dial. to mash ‘to infuse’; Li. mazgóju, óti, v. ^wash- clothes'; Latv. mazgaju, at, id. Cf. moiEs-
11088:mol£- ‘drip, milk’. Cf. mel$-, mlĝ- Gk. cf. a-molgaios, adj. *milk-; cf. a-molgeüs *milk-pail'; Srb. mláz, m. ‘drip, drop, jet; Big. mlazí, f. “latex, mucus; mlazgà & mlézga, f. ‘sap’; R cf. molóz-ivo, n. *beestings'; Li. malZi, adj. f. ‘milch’; malZau, yti, v. freq. ‘milk’. Appa- rent variants occur in Oss. marg 'poison' (fr. *molgh- or *molg-?), & Arm. maydz, Let, (gall, fr. *mol$&h- apparently influenced by gaydz 'galP from a type *gholghis, q.v.
11190:Skt. majjà, f. 'brain'; Av. mazga, f. id.; Per. mayz ‘brain, marrow, pith’; Oss. maéz, id.; Tokh. cf. maccunt, pl. ‘brain? beside masiák, B meske, s. «link, joint; LW in W masg, pl. -àu, f. ‘mesh’; OE max, n. ‘net beside mearg, m. n. ‘marrow, pith’; E mesh; OHG maska, f. ‘mesh’; Ger. Masche, f. *knitting-stitch'; LG masch, id.; MHG masche, f. ‘bow, noose’; Sw. maska, f. *knitting-stitch'; ON moskvi, m. ‘mesh’; Li. mázgas ‘knot
11191:mosgos (mosg-) (2) 'steeping, infusion, mash’. Cf. mesgó (2) & moiks- Sw. mäsk, m. brewer's mash'; mäska, v. 'in- fuse, steep’; Eng. dial. mash; Li. cf. mazgóju, óti “wash — things’; Latv. mazgàju, v. ‘wash’
11192:mosghos “bud, shoot. Cf. odsgh-. WP IT, 308 Gk. móschos, m. ‘shoot; young calf; Li. máz- gas, m. (2) ‘buď’; Latv. (alleged) mazgs, m. id. Cf. mosg- (2). (Isophones: ON mergr, Sw. märg, m. *bone-marrow)
11838:nondh- (nndh-) “press, swell, drive’. Cf. WP II, 316 and nnt- (nont-) Per. cf. (z-gde?) nad “increase, abundance"; Hitt. cf. nannahi, v. ‘drive, march’; OCS noZdo, noditi, v. ‘thrust, force’; Pol. cf. nedza, Cz. nouze, R nuždà ‘misery, need'; cf. also
11878:noudheið ‘urge, force’. See next. WP II, 316 Go. naubpjan, v. ‘force’, beside naudi- in naudi- bandi, n. ‘fetter’; OCS nuZdo, nuditi and com. SL, id. (not related to noZdo, noditi, see nondh-); MHG noeten, id.; OE néadian, v. id.; (alleged naudei, ds ‘to force given by SF as OPr., misspelt nautei)
11989:odsghos (odzgos, odhgos), a “shoot, branch, stem'. WP I, 185 Skt. cf. ádgah, m. 'cane, stalk'; Pahl. azg *branch'; Per. azay, (id. and 'shoot); Gk. óskhos, e, mf. id., cf. also ól-oskhos, m. ‘pedicel’; W osg, m. ‘shoot, projection? beside osgl, pl. au. and osglen, f. “branch, twig
12280:com. Sl.; roZdo, roditi, v. (produce, beger, and com. $1.5; R cf. also the adj. rožij, adj. (*robust', fr. *ordhjo-); Finn. LW rotu ‘race, kind'. Gk. orthós, adj. 'straight, right, true, upright? probably belongs here on semantic grounds, but a type *uordh- is possible. Gk. órthros ‘early dawn’ is at any rate isophonic w. Arm. ardar, adj. “Just, right’. (Alleged ardas “Order, clas? NBS : WLS seems to be spurious, or a LW fr. Lat. ordo)
13358:pondheió (pondhio) ‘press, probe, attack’. (Vocalism ambig.) MHG vanten, G venden, wv. “try, probe, find out’; OFris. fandia, wv. ‘visit’; OE fandian, v. “probe, explore, experience, visit"; cf. fandung ‘probe, search, temptation’; OS fandon, v. 'ransack; probe’; OCS poZdo, poditi, v. drive: Pol. pędzić, v. ‘drive’; Cz. pudit, inf. ‘impel’; Srb. puditi, inf. ‘scare off; cf. Pol. ped, m. ‘rush, dash; shoot, bud’; Cz. pud, m. "instinct". Here also EM. vanden, v. ‘visit’
14744:rosg- “twist, branch'. Cf. resg- Skt. (ambig. *-e- or *-o-) rájjuh, f. ‘rope’; OCS rozga, f. “branch, whip, shoot; R rózga, f. *birch-rod'; (e-gde in) Latv. režģi, mpl. (^wic- ker, matting'. See resg-); Li. cf. razgaü, -yti, v. *plait
```


## [2026-09-07T20:18:21.837Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== ozdo ===\"; grep -n -o -E '.{200}ozdo.{400}' AHD_watkins1985.txt | head; echo; echo \"=== oscillate ===\"; grep -n -o -E '.{300}OSCILLATE.{200}' AHD_watkins1985.txt | head; echo; echo \"=== ODD ===\"; grep -n -o -E '.{300}\\bODD\\b.{200}' AHD_watkins1985.txt | head",
 "description": "Grep AHD for ozdo, oscillate, odd"
}
```


## [2026-09-07T20:18:23.044Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['AHD','IEC','SYN','KLN']:\n  e=d[k]; print('##',k,'| cites:',e.get('cites'),'| page_offset:',e.get('page_offset')); print()\n\"",
 "description": "Check cites/page offsets"
}
```


### [2026-09-07T20:18:24.739Z] TOOL RESULT

```
=== ozdo ===
1096:Variant form *trid- in Germanic “thristjan in Old Norse thrysta, to squeeze, compress: THRUST. 3. Latin tridere, to thrust, push: ABSTRUSE, EXTRUDE, INTRUDE, OBTRUDE, PROTRUDE. [Pok. tr-eu-d 1095.] trozdo-. Thrush. 1. Germanic *thrust- in Old English throstle, thrush: THROSTLE. 2. Germanic *thruskj6n- in Old English thrysce, thrush: THRUSH}. 3. Zero-grade reduced form *trzdo- in Latin turdus, thrush: STURDY. 4. Perhaps altered in Greek strouthos, sparrow, ostrich: STRUTHIOUS; (OSTRICH). [Pok. trozdos 1096.] tu-. Second person singular pronoun; you, thou. 1. Lengthened-grade form “ti (accusative “t

=== oscillate ===

=== ODD ===
```


### [2026-09-07T20:18:26.088Z] TOOL RESULT

```
## AHD | cites: page number of the 1975/76 New College Edition; pp. 1505–1550 are the Indo-European roots appendix (look the root up by name) | page_offset: 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.

## IEC | cites: column/page number of Mann, An Indo-European Comparative Dictionary (1984–87) | page_offset: TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>

## SYN | cites: page number of Buck, A Dictionary of Selected Synonyms (1949) | page_offset: leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>

## KLN | cites: page number, continuous across the two volumes (1966–67) | page_offset: KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
```


## [2026-09-07T20:18:39.521Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== uzd/oddi/oddr ===\"; grep -n -o -E '.{150}(uzd|oddi|oddr|Old Norse oddi).{150}' AHD_watkins1985.txt | head; echo \"=== os- ash / sed- s- prefix ===\"; grep -n -o -E '.{100}(ozdo-s|\\*o-zdos|branch).{200}' AHD_watkins1985.txt | head -6",
 "description": "Grep AHD for uzd/oddi"
}
```


### [2026-09-07T20:18:39.858Z] TOOL RESULT

```
=== uzd/oddi/oddr ===
323:ic *bur- in Swedish borre, bur, perhaps akin to the Scandinavian source of Middle English burre, bur: BUR}; b. suffixed form *bhrs-dh- in Germanic *bruzd-, point, needle, in Old Norse broddr, spike: BRAD; C. suffixed form *bhrs-ti- in Latin fastig- ium, summit, top, extremity: FASTIGIATE, FASTIGIUM; d.
943:anic *huson- in Old English hosa, hose, covering for the leg: HOSE; b. suf- fixed form *kus-dho- (or suffixed extended form *kudh- to-) in Germanic *huzdam in Old English hord, stock, store, treasure (< “thing hidden away”): HOARD; c. Rus- sian kishka, gut (< “sheath”), akin to the Slavic source of Yid
=== os- ash / sed- s- prefix ===
55:c, Baltic, Albanian, Celtic, Italic, and Germanic. The present century has seen the addition of two branches to the family, neither of which has left any living trace: Hittite and other Anatolian languages, the earliest attested in the Indo-European family, spoken in what is now Turkey in the second mille
163:ots for grinding are attested, al-* and mele- (MEAL?, MILL). The latter is confined to the European branches of the family. Another European term is sé-', “to sow,” not found in Greek, Armenian, or Indo-Iranian. The verb “to plow” is are-, again a common European term, with the name of the plow, *ara-trom
194:rentiated Indo- European dialects, some of which would doubtless evolve into some of the historical branches of the family tree. We must be content to recognize the Kurgan peoples as speakers of certain Indo-European languages and as sharing a common Indo-European cultural patrimony. The ultimate “cradle”
207:s kak-? and mas are not strictly speak- ing Indo-European, since they are repre- sented in only one branch of the family. There is a relatively small number of such entries in this Dictionary; they are included because of the number of English words among their descendants. Boldface brackets are placed ar
364:sh teld, awning, tent: TILT?. 2. Germanic extended form *telg- in Old English telgor, telgra, twig, branch: TILLER’. 3. Perhaps o-grade form *dol-é- in Latin dolére, to suffer (? < “to be beaten”): DOLE?, DOLOR; CONDOLE, INDO- LENT. 4. Suffixed o-grade form *dold-dhraé in Latin dolabra, a heavy chopping t
415:BINARY; COMBINE. 11. Suffixed form *dwi-ko- in Germanic *twig(g)a, a fork, in Old English twigge, a branch: Twic!. 12. Compound *dwi-plo-, twofold (*-plo-, -fold; see pel-3), in Greek diploos, diplous, twofold: DIPLO-, DIPLOE, DIPLOMA; ANADIPLOSIS. 13. Suffixed reduplicated form *dwi-du-mo- in Greek didum
```


## [2026-09-07T20:18:41.491Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== PHD azg ===\"; grep -n -E '\\bazg\\b|azg ' PHD.txt PHD_mackenzie.txt | head -20; echo \"=== NYB azg ===\"; grep -n -E '\\bazg\\b' NYB_vol2_glossary.txt | head -10; echo \"=== HRN azg ===\"; grep -n -i -E 'azg|azaɣ|azaγ|azay' HRN.txt HUB.txt | head -20",
 "description": "Grep Pahlavi and Persian sources for azg"
}
```


### [2026-09-07T20:18:41.593Z] TOOL RESULT

```
=== PHD azg ===
PHD_mackenzie.txt:3522:mazg [mzg I (M mgj, N mayz)] brain, marrow.
PHD_mackenzie.txt:6108:branch azg, tag.                       bun kulacag.
PHD_mackenzie.txt:8944:spazg                     ~Q»>
PHD_mackenzie.txt:11818:azd, azg                .",r,.     osastar                  \w.v-ut-
PHD.txt:227:azbāy- [*2b*d-] invoke. ~išn: invocation. azd [zd | = M] known. Azdahag Pcydi’k' | M ?zdh?g, (N aždahā)] a legendary ‘dragon’ king, Dahāg. azdénidan, azdén- Pzdyn-ytn'] inform. azēr [%cdl | N zér] below, under. azg [22 | N аху) branch. aziš [hcf | М *cy$, 22у] from him, it; postposition (= az) from, ~-keh [-ks] inferior, subordinate. ~-meh [-ms] superior. āz-kāmaģ [?ck’mk'] greedy. ~ih: greediness. azmüdan, azmāy- ['zmwtn!,?zm'd- | N 2~] = uzmüdan. aznawar Pzrw/l | M ?zn] noble. azraw-, v. azruftan. azray- ['zr'd-] adorn. azruftan, azraw- [)zlwp-tn! | M *zrw-] go out, be extinguished. āzurdan [Pcwltn! | N ~] = āzārdan, āzwar [?*cwl | N ~] greedy. ~ih: greed.
PHD.txt:473:mazg [mzg | (M та], N mayz)] brain, marrow.
PHD.txt:568:spas dāštan, ~ hangárdan: thank, give thanks. spās-dār [sp?sd?] | N sip~] grateful, thankful. ~ih: gratitude. spās|-ešnās [sp’ssn’s] grateful. —ómand [-’wmnd] grateful. spas [sp = Av. 0Bàsa-] space, atmosphere. spaxr [sp?hl | M ‘spxr, N *siparx] merrymaking, revelry. spazg [spzg | (M ‘spgj), N sipazg-] slanderous. «il: slander. spëd [spyt! | M ‘spyd, N sapéd] white. ~ag [-k! | N -a] white (of egg, etc.). —bàg [-p’k!' | N -bā] curd soup. --dàr [-?1 | N -dár] white poplar, aspen. spenag [sp(y)m?k! = Av. spanta-, cf. $annág] holy. ~ ménóg : the Good Spirit. Spig [spyk' | M ‘spyg, (N sapriy)] т. brilliance; 2. sprout, shoot. spihr [spy(y)hl | (M ‘spyr), N sipihr] sphere, sky, firmament, fate. ~ig [-yk'] heavenly. spinjanagih [spne’nkyh] hospitality. spiš [spyš | (N šipt$)) louse. Spitāmān [spyt?m?^n] of the Spitama family. spiz- [spyc- | M “рухіп, *spyz-] 1. shine; 2. sprout. —išn: 1. brilliance; 2. sprouting. spöxtan, spēz- [spwhtn', spwc- | M *spwxt, N sip~] thrust; overstep, disobey; delay, reject. ~išn: delay, rejection; disobedience. SpOz [spwe | N sipóz] disobedience; delay. ~gar LEIT N ~] disobedient; dilatory. sprahm(ag) [splhm(k') | M *sprhm(g), N siparham] flower, fragrant herb. spul [spwl] spleen. spurdan, spar- [spwiltn', spl- | N sip~] tread, trample. spurrig [spwlyk!' | (M ‘spwr), N sipari] entire, complete, perfect. ~ith: completeness, perfection. spurz [*spiz | P “spwrz, N sipurz] spleen. srat (sit! | cf. Ar. sirát] street. sraw [s/wb'] word, spell. srawénidan, srawén- [slwbyn-ytn'] report, broadcast. sraxtag [s/htk! = Av. sraxti-] side, part. sray [sd | N saray] house, hall. Igrāy-, -išn, v. srüdan. srāyīdan, ?sráy- [sPd-ytn! = Av. @rdya-] protect. ~išn: protection. srešk [sl(y)£h | (P srsk), N sirifk] drop, tear. srištan, *srēš- [s/szn! | P sryi-, N sir-~] mix, knead. sri$wadag [s/ystotk! = Av. Oriswa-] a third. sréd [s/zvt! | M srwd, N suród] song.
PHD.txt:1066:branch azg, tāg.
PHD.txt:4773:spéd spēdag spēdbāg spenāg spóxtan spandan Spandarmad sabuk spul spurrigih spurrig spurdan spūz spēz- spinjānagīh spozgar spūzišn sabz spazg spazgīh spar spar- sprahm sprahmag
=== NYB azg ===
=== HRN azg ===
HUB.txt:461:(Wrzl. reg^ in ogiyto u. s. w.) — zd. aiwi + razay^iti
HUB.txt:700:Lehnwortes baz^, bazay (5. Jhd.) istap. *6^0- (+ Suffix),
HUB.txt:2902:Etud. iran. II, 221) = zd. azayo xsva^wMho *Vipem'
HUB.txt:5668:zfidan = phi. vaziitan (pr. vazay-) 'to injure' Shk. 272 gehort ;
HUB.txt:5801:vazay Trosch* ^^ zd. vazaya-; vantdan 'wehen', skr. vah
HUB.txt:7898:vazayGr- u. s. w.
HUB.txt:7973:'Gehirn' = zd. mazga-, ksl. mozgu, idg. mazg'^ho^.
HUB.txt:8119:*) Vgl. auoh i in vazun = vazgun, bSzgun u. s. w. Verkehrt* aus
HUB.txt:8835:Oel' = zd. raoyna-; vazay *Frosch* = zd. vazaya^\ varg,
HUB.txt:8854:dagegen kann mayz 'Gehirn' = zd. mazga- nicht auf ap.
HUB.txt:8855:^mazya- zuriickgefiihrt werden. Wurde schon ap. mazga-
HUB.txt:9552:g) Ap. zg = np. yz: mayz 'Gehirn* = zd. mazga-.
HRN.txt:1796:LW. arab. bäzi, syr. pV2, arm. bazay, kurd. büzt,
HRN.txt:3278:piyazay (203).
HRN.txt:8574:aw. mazga- 'Gehirn'; phlv. mazg; ai. majjdn- 'Mark*.
HRN.txt:8576:(174); bei. mazg (229); sar. muig 'Knochenmark', da-
HRN.txt:9367:1082. vei^ey Frosch', arab. LW. vazayat 'Eidechsenart'.
HRN.txt:9368:aw. vazayä' 'Frosch'; phlv. vazay, vazag.
HRN.txt:10208:42. azg (d. i. azak) 'Ziege (PPÖl.).
HRN.txt:11010:182. spaxff *verleumderisch', spazgth 'Verleumdung' (Men.,
```


## [2026-09-07T20:19:00.123Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== BRT aosta ===\"; grep -n -i -E 'aošta|aosta|aoštra|aostra' BRT.txt | head -10; echo \"=== BRT ah Mund ===\"; grep -n -o -E '.{0,120}(āh-|ā̊h|arəδan).{0,200}' BRT.txt | grep -i -E 'mund|lippe' | head -10; echo \"=== HRN Zweig ===\"; grep -n -i -E 'zweig|knospe' HRN.txt | head -20",
 "description": "Grep Bartholomae and Horn"
}
```


## [2026-09-07T20:19:01.827Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== KLN leaf around p1091 ===\"; for l in 556 557 558; do echo \"--- leaf $l ---\"; awk -v n=$l 'BEGIN{RS=\"\\f\"} NR==n' KLN_1966.txt | head -12; done",
 "description": "Print Klein leaves near p.1091"
}
```


### [2026-09-07T20:19:04.046Z] TOOL RESULT

```
=== BRT aosta ===
2969:fromme,  der  es  zuerst  gelehrt  hat,  dass  •  j.  aosta- m. 'Oberlippe',  Du. 'die  beiden
3148:PPfP.  einer  Basis  jJJJfl'j-,  s-  Erneilcrung (/-Aorist,  vgl.  xlnaosta,  xiiiaosiii)  des  \'.  ilnav-. —  VgL  axsaüla-.
8070:•  j.,  g.  izä-'>  f.  1)  'Stieben,  Eifer",  bes. 'frommer,  Glaub enseifer':  manS  voha  uru- nascä  asiiunqm  n>mascä  yä  ärmaiti/ (sd.) °zäcä  Y.4g.io;  —  mat  vä  padäis  (sd.) yä  frasrütä  (sd.)  -zaya  Y,  50. 8 ;  —  ^vldl- hmnäi  (sd.)  'zäcit  (IS.)  .  .  vahistsm  Y.jr. i;  —  ya%a  'za  (IS.)  viicim  näsima  Y, 70.4.  a)  Plur,  in  Verbindung  väwyaostay- usw.,  Plur.;    °m  yaostayS  fora^tayS  ärma-
10058:mit^ü  i) 'hinzukommen,  gelangen  zu  -' (Akk,):  yat  .  .  masdayasna  päaa  ayatitim (sd.)  vä  . .  nasäum  frajasan  V.  6,  26;  8. 73;  —  hanjamatum  frajasöit  Vd.  17;  — '^raosta  .  .  fräymat  usatffam  sBraya  *vx- vitlm  Yt5. 62;  —  nalmim  Aiyjjw  (sd.) /rajasat  Vd,  2;  15,  17,  18.  3)  'daran
10754:um  die  Herrschaft':  haomB  . .  kmsSnJm apa-xid^rim  (sd.)  nilähaya^  yd  raosta  (sd.) 'mya  (IS.)  Y.p.  24.
10792:—  paoiryh  dasa  'panS  (AP.)  ,  .  tUtryll .  . k3hrp3m  rai'kvjayäti  .  .  "während  der ersten  zehn  Nächte  . ."  Yti'.i3;  —  upa . .  jaymyam  aivqm  vä  avt  °param  duyz vä  .  .  YtÄir;  —  %raosta  'fiiS  '^rityayä Vtj.öz.  b)  als  Zeit  von  Sonnenunter- gang zu  Sonnenuntergang  Tag  und  Nacht, Tag'i>:  ta  'paiiö  (AP.)>r7  +>JÄ(  \. 62.10;
10910:masista  xsnaoma  x'nävayäliV.3.iz;g.^2^; —  äai  tum  nishti>ail..ttar»m^a  asavamm kuxsnvqnS  H.2.13,  Vyt55(wo  ^kjt/h- vänB)-,  —  yS  neu  narsm  aiavamm  .. xsnaosta  vä  xsnävayeite  va  '2.4g;  —  ya- '^raca  x^nätS  asavaYi-i^.^C;  —  xi'nüta- htcit  atbislaAe  i&A.)  ..  manS  yaezayäti'^X. /O.iii;  —  xsnüiS  (NPm.)'*  asdonqm urväfßs  pärayeinli  V. /p.31;  —  yat  alsS nä  .  .  haca  alibyS  nmanaHbyS  xsnütS aUii'ß parayäl  V.5.39;  —  ka%a  ^wa mazää  xsnaosäi  aAurä  "wie  kann  ich  dich zufrieden  stellen,  o  AfAA.f"  Y.46,1;  — ndii  xhtSvayeili  ahurim  mazäqm  .  .  ys mazdqm  tarS  manyete  \t  lO.i^q;  6.4;  — yagcä  xsnaespn  (3PKA.)  ahursm  Aaihyäii /y/joianäi/  fraorit  mazdqm  "und  die, welche  gern  mit  rechtem  Tun  AcAÄhM. zufrieden  stellen"  Y,_jo.  5;  —  tistrjm  .. yj  äa\äiti  kuxlnvqnäi  .  .  ayapta  jaio- yantäi  . .  maiyai  ".  .  dem,  der  (ihn)  zu- frieden stellt  .  ."  Yt  &  49;  7J.  24;  — HstrJm  .  .  yezi  . .  bavaitt  yaltö  xSnaiß frihs  paiti.zanlS  Yt.8.4z;  10.120,  Y.ig. 40;  — yaAmäi  xsnütS  bavaiti  mikrS  ,  . yakmäi  IbistB  bavatti  (sd.)  Yt  JO.87;  28, Y.  62.  9;  —  yä^a  . .  anäzarstä  xsnütA  . . a/bisti  yBbm  (näml.  fravasayö)  . .  /ra- cara'iwe\ti3.ZA;  S^  63.  'S^',  iS7';  — xlnuta  F.5;  —  vaT3h3uS xratüm  manaahS yä  xsnyvTsa  g^s^ä*urvqmm  "aufdass  ich den  Willen  des  VM.  befriedige  und  die Seele  des  Rinds"  Y.  28.  \;  —  mazdä  asä xsmüksm  vilnm  xsnaohmnB  "o  M.  und A.,  indem  ich  es  eurem  Willen  recht machen  will"  Y.  ^.  18.  a)  Des.  'zu- frieden stellen,  zu  Gefallen  sein  wollen': nsit  nä  pouräs  (sd.)  drpgvatö  Ayäi  ^ixs- n  uiS  Y.43.11;  —  ys  masying  Hxsn  uiö .  .  gäul  bagä  x^ürsmnS  (sd.)  Y,  J2,  8;  — y}  dusprJ^rJi  (sd.)  Bxsnusä  (iS.)  Y.  4g. I.  a)  mit  Dat  comm.  'Jemands  Zu- friedenheit gewinnen  wollen  für  — ':  tSm nS  vokB  mal  manavhcl  axiriusö  "des  Zu- friedenheit sollst  du  uns  zu  gewinnen suchen,  sammt  der  des   VM."  Y.  45. 9.
14321:—  yd^ä  ^wä  zTvTiHfK  uzimökz  (sd.)  Y. 46.');  —  *yavatai'>  ^wä  masds  *staomI ufya(s±)cä  Y.43.S;  —  maibyB  %wä sqsträi  (sd.)  v»r?nl  akurä  Y.4^-Z'>  — vakistim  %wa  .  .  akur»m  yäsa  (sd.)  Y. 2Ä8.  zu  I  a):  atzt'h-wäfsuyantailä.. "hwsnlta  (sd.)  latasä  Y.  2p.  6;  —  dazu wohl  auch*':  azSm  tai!  ^wä  /raxsnlisd.) aväml  magdä  Y.  44-  7 1  —  sp^nttm  at %wä  mazda  mingkx  (zA^  V.4J.  5,  7,  9, 11,  13,  ij.  zu  3):  firalaostrai  .. alakyä  da  I  sarSm  ta}  %wä''^  mazdä yäsai^d.)  Y.4p.8;  —  s.  noch  Y.2Ä  5  im Anhang.  Anhang.  Der  Akk.,  dem ein  Vok,  vorhergeht,  ist  dem  Akk.  eines (mit  CS  angeschlossenen)  Subst  koordinirt (Sp.  565  u.);  vgl.  2,  9  (Sp.79ou.):  asä  kaf %wa^''  darisani  (sd.)  manascä  vokü  Y. 28.  s;  s.  zu  2.  B  I  ß)  im  YHapt.;  zu  1): a%a  %iiia  ail  yazamaidiY-sg.i,;  36.\ i.St,  3;  —  kumälm  %wa  .  .  yazat^m  .  . dadsmaidi  Y,  47. 3 ;  —  äzoö  (zu  'hwa-)  ^wä mainya  spStiistä  (näml.  pairT.jasämaidt) Y.36.1;  5;  —  vokB  %tvä  manar^ks  voka %7iia  asa  ..  Y.36.4;  4.  zu  z):  a^ä isBidyämakx  %wä  mazdä  akurä  Y.^^,4;
14479:8oi  SraoStay-
14482:ahm  "hraosta  (3S.)  ahurä  "ausser  deinem
=== BRT ah Mund ===
ugrep: error: error at position 99
n)(?:[^\n\x80-\xbf][\x80-\xbf]*){0,200}
          exceeds complexity limits___/


=== HRN Zweig ===
1152:82. i8tä%, istaky sitak 'Zweig*.
2150:200. berseiu 'Barsomzweig' (Sahn.).
3524:373. tal *Zweig, Stück\
3526:kurd. LW. fäf Zweig'; bei. täk^ n, fä/ 'Blatt (eines
6666:766. Süx 'Zweig, Ast; Hörn (des Stieres), Greweih'.
6671:wa;K. soZ/, sar. so^ 'Zweig', wa;!r. mo, sar. xdo 'Geweih'.
```


### [2026-09-07T20:19:05.307Z] TOOL RESULT

```
=== KLN leaf around p1091 ===
--- leaf 556 ---
 MF.  (=  F.)  negatif  (fern. negative),  fr.  OF.  negatif,  fr.  L.  negativus,  ‘that which  denies’,  fr.  negatus,  pp.  of  negare.  See negate  and  -ive.
Derivatives:  negative,  n.  and  tr.  v.,  negative-ly, adv.,  negative-ness,  n.,  negativ-ity,  n. negator,  n.,  one  who  denies.  —  Late  L.  negator, ft.  L.  negatus,  pp.  of  negare.  See  negate  and agential  suff.  -or.
negatory,  adj.,  expressing  negation.  —  MF.  (= F.)  negatoire,  fr.  ML.  negatorius,  ‘negative’,  fr. L.  negatus,  pp.  of  negare.  See  negate  and  adj. suff.  -ory.
negativism,  n.,  the  opposite  of  positivism.  —  A hybrid  coined  fr.  L.  negativus  (see  negative)  and -ism,  a  suff.  of  Greek  origin, negativist,  n.,  an  adherent  of  negativism.  —  A hybrid  coined  fr.  L.  negativus  (see  negative)  and -ist,  a  suff.  of  Greek  origin.
Derivative:  negativist-ic,  adj. neglect,  tr.  v.  —  L.  neglectus,  pp.  of  neglegere, negligere,  'to  make  light  of,  disregard,  be  in¬ different  to,  neglect’,  compounded  of  *neg(i), ‘not’,  and  legere,  ‘to  pick  up,  gather;  to  read'. See  negate  and  lecture.
neglect,  n.  —  L.  neglectus,  ‘a  neglecting’,  fr. neglectus,  pp.  of  neglegere,  negligere.  See neglect,  v.
Derivatives :  neglect-ful,  adj . ,  neglect-ful-ly,  ad v. , neglect-ful-ness,  n.
negligee,  negligee,  also  neglige,  neglige,  n.,  1)  a woman’s  loose  dressing  gown;  2)  any  careless attire.  — -  F.  neglige  (fern,  negligee),  pp.  of negliger,  ‘to  neglect’,  fr.  L.  neglegere,  negligere. See  neglect,  v.
negligence,  n.  —  ME.  neglvgence,  fr.  MF.  (=  F.) negligence,  fr.  L.  neglegentia,  negligentia,  ‘negli¬ gence’,  fr.  neglegens,  negligens  (gen.  -entis).  See next  word  and  -ce.
negligent,  adj.  —  ME.  negligent,  fr.  MF.  (=  F.) negligent,  fr.  L.  neglegentem,  negligentem,  acc. of  neglegens,  negligens,  pres.  part,  of  neglegere, negligere.  See  neglect,  v.,  and  -ent.
Derivative :  negligent-ly,  adv. negligible,  adj.  —  Formed  with  suff.  -ible  fr.  L. negligere.  See  neglect,  v.  Cp.  F.  negligeable. Derivatives:  negligibil-ity,  n.,  negligible-ness, n.,  negligibl-y,  adv.
negotiable,  adj.  —  See  negotiate  and  -able.
--- leaf 557 ---
 for  *ver og,  fr.  I.-E. •newos,  ‘new’,  whence  also  Goth,  niujis,  OE. neowe,  ‘new’.  See  new  and  cp.  neon,  neoteric, Nerium,  the  first  element  in  neossine  and  the second  element  in  misoneist.
neodymium,  n.,  a  rare  metallic  element  ( chem .)  — ModL.,  shortened  fr.  neodidymia ,  a  name  coin¬ ed  by  the  discoverer  of  this  element  Carl  Auer von  Welsbach  (1858-1929)  fr.  Gk.  veo ‘new’ (see  neo-),  and  ModL.  didymium,  the  name  giv¬ en  by  Mosander  to  a  rare  metal  which  he thought  to  be  a  single  chemical  element;  see  di¬ dymium.  In  1885  von  Welsbach  succeeded  in splitting  didymium  into  two  elements  which  he called  neodidymia  and  praseodidymia  (see  prase¬ odymium).
Neogaea,  n.,  the  Neotropical  zoological  realm.
—  ModL.,  compounded  of  neo-  and  Gk.  yr, , ‘earth’.  See  geo-  and  cp.  the  second  element  in Arctogaea,  Notogaea.
Derivative:  Neogae-an,  adj. neolith,  n.,  a  neolithic  tool.  —  Back  formation  fr. neolithic.
neolithic,  adj.,  pertaining  to  the  later  Stone  Age.
—  Coined  by  John  Lubbock,  the  later  Baron Avebury  (1834-1913),  fr.  Gk.  veo?,  ‘new’,  Xlffo?, ‘stone’,  and  adj.  suff.  -ic.  See  neo-  and  litho-  and cp.  paleolithic.
neologism,  n.,  1)  a  new  word;  2)  introduction  or use  of  new  words  or  of  new  meanings  of  existing words.  —  F.  neologisme,  fr.  neologie.  See  neo¬ logy  and  -ism.
neologist,  n.,  a  person  who  invents,  introduces  or uses  new  words.  —  F.  neologiste,  fr.  neologie. See  neology  and  -ist.
Derivatives:  neologist-ic,  neologist-ic-al,  adjs. neologize,  intr.  v.,  to  make  a  practice  of  using new  words  or  new  meanings  of  existing  words.  — F.  neologiser,  fr.  neologie.  See  neology  and  -ize. neology,  n.,  neologism.  —  F.  neologie,  com¬ pounded  of  neo-  and  Gk.  -XoytS,  fr.  -Xoy°x, ‘one  who  speaks  (in  a  certain  manner) ;  one  who deals  (with  a  certain  topic)’.  See  -logy, neomenia,  n.,  the  time  of  the  new  moon  ( Greek and  Jewish  antiquities)  —  Late  L.,  fr.  Gk.  veo- p.7)VLoc,  ‘the  new  moon;  the  first  of  the  month’, compounded  of  veo?,  ‘new’  (see  neo-),  and  ‘ rv - V7] ,  ‘moon’,  which  is  related  to  pr;v,  gen.  pr,v6?, ‘month’.  See  moon  and  cp.  meno-  and  words there  referred  to.
neomycin,  n.,  an  antibiotic  isolated  by  the  Amer¬ ican  microbiologist  Selman  Abraham  Waks- man  (1888-  ).  —  Coined  fr.  neo-,  myco-  and
suff.  -in.
--- leaf 558 ---
.  ve< pp4c,  ‘kidney’  (see  ne¬ phro-),  and  suff.  -it,  which  goes  back  to  Gk. -fry?  (see  subst.  suff.  -ite);  so  called  in  allusion to  its  supposed  efficacy  against  diseases  of  the kidneys.
nephritic,  adj.,  pertaining  to,  or  affecting,  the  kid¬ neys.  —  Late  L.  nephriticus,  fr.  Gk.  vcspiTixos, ‘pertaining  to  the  kidneys’,  fr.  vcypo?,  ‘kidney’.
See  nephro-.
nephritis,  n.,  inflammation  of  the  kidney  (med,) —  Late  L.  nephritis,  fr.  Gk.  VE9PIT1.5,  fr. veppo?,  ‘kidney’.  See  nephro-  and  -itis.
nephro-,  before  a  vowel  nephr-,  combining  form meaning  ‘kidney’,  or  ‘nephric  and’.  —  Fr.  Gk. VE9P65, ‘kidney’,  which  stands  for  I.-E.  *negwh- rds,  ‘kidney;  testicle’,  and  is  cogn.  with  L. (Praenestine)  nefrdnes  (for  *negwhron-),  ‘kid¬
neys  ;  testicles’,  L.  (Lanuvian)  nebrundines,  ‘kid¬ neys,  testicles’,  ON.  nyra,  Dan.  nyre,  Swed. njure,  ONorw.  nyra,  Norw.  ryggja-nyre,  "kid¬ ney’,  ME.  nere,  MDu.  mere,  Du.  nier,  ‘kidney’, OHG.  nioro,  niero,  ‘kidney,  testicle,  loin’,  MHG niere,  nier,  ‘kidney,  loin’,  G.  Niere,  ‘kidney’  (fr. Teut.  *neurian-,  *neuran-,  fr.  I.-E.  *negwhron-). Cp.  perinephrium.
nephrolith,  n.,  a  renal  calculus  (med.)  —  Com¬ pounded  of  nephro-  and  Gk.  Xi-ffoc,  ‘stone’.
See  -lith.
nephropexy,  n.,  the  fixing  of  a  floating  kidney (med.)  —  Medical  L.  nephropexia,  compounded of  nephro-  and  Gk.  -7r»)5ta,  fr.  ‘a  making
firm,  fastening’,  which  derives  from  the  stem  of 7t7]Yvtjva!.,  ‘to  join,  make  firm’.  See  -pexy.
nephrosis,  n.,  disease  of  the  kidneys  (med.)  — Medical  L.,  coined  by  Muller  in  1905  fr.  Gk. V£cpp6c,  ‘kidney’  (see  nephro-),  and  suff.  -osis.
nephrotomy,  n.,  the  operation  of  cutting  into  the kidney  ( surg .)  — -  Compounded  of  nephro-  and Gk.  -xopta,  ‘a  cutting  of’,  fr.  Topirj,  ‘a  cutting'. See  -tomy.
```


## [2026-09-07T20:19:25.693Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re,io\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\npats=['oral, adj','orifice','usher, n','oscillate','ostium','aosta','aoshta','os, n','os,  n']\nfor p in pats:\n    hits=[(i,l[max(0,l.find(p)-80):l.find(p)+300].replace('\\n',' ')) for i,l in enumerate(leaves) if p in l]\n    print('###',p, [h[0] for h in hits][:8])\n    for i,s in hits[:2]:\n        print('   leaf',i,':',s[:350])\nEOF",
 "description": "Locate Klein entries by leaf"
}
```


### [2026-09-07T20:19:27.262Z] TOOL RESULT

```
### oral, adj []
### orifice [144, 162, 215, 309, 330, 541, 583, 585]
   leaf 144 : poppy  head",  xoTXo; (for  *x65i>.o?),  ‘hollow’,  xuap.  ‘eye  of  a  needle; orifice  of  the  ear’.  OI  r.  cita,  ‘hollow’,  cuass,  ’cave’, Bret,  keo,  ‘cave’,  OI.  svdyatc,  ‘swells’,  sitndh, ‘swollen’,  savas-,  ‘strength,  heroism’,  sdvirah, surah,  ‘strong’,  Gk.  y.-iz iv.  x'isiv,  ’to  become  or be  pregnant’,  /.Oar.,  ‘anything
   leaf 162 : oids  (med.)  —  Formed  fr.  prec.  word  with  suff. -ism. cinclis,  n.,  an  orifice  for  the  protrusion  of  the acontia  of  sea  anemones  (zool.)  —  ModL.,  fr. Gk.  xtyxXii;,  ‘a  latticed  gate’.  See  cincture, cinct,  adj.,  girt,  girdled.  —  L.  cinctus,  pp.  of  cin¬ gere,  ‘to  gird’.  See  next  word, cincture,  n., 
### usher, n []
### oscillate [193, 588]
   leaf 193 : ¬ ed’,  whence  also  OI.  vaheati,  ‘moves  to  and fro’,  vacydte,  ‘swings,  oscillates’,  vakrah,  ‘curv¬ ed,  crooked’,  vaheayati,  ‘slips  away,  deceives’, Avestic  -vashta,  ‘curved’,  L.  vacillare,  ‘to  sway, waver,  vacillate’,  W.  gwaeth  (for  *vakto-), ‘worse’,  gwaethaf,  ‘worst’,  Co.  gweth,  ‘worse’, OE,  woh,  ‘crooked,  perve
   leaf 588 : ive  use  of  6 tsyrj,  ‘vine  with  grapes’, which  is  of  uncertain  origin, oscillate,  intr.  v.,  to  swing  to  and  fro;  tr.  v.,  to cause  to  swing  to  and  fro.  — L.  dscilldt-(um),  pp. stem  of  oscillare,  ‘to  swing,  sway’,  fr.  osciUum, ‘a  swing’,  which  is  of  uncertain  origin, oscillation,  n.  —  L.  bscilldtio,  gen.  
### ostium [589, 892]
   leaf 589 :   n.,  doorkeeper,  esp.  of  a  church.  —  L. ostiarius,  ‘doorkeeper’,  fr.  ostium,  ‘door,  en¬ trance’,  which  is  rel.  to  L.  os,  ‘mouth’,  and  cogn. with  OSlav.  usta,  OPruss.  austo,  ‘mouth’,  Lith. uostas,  uosta,  ‘mouth  of  a  river,  bay’,  Russ. tistije,  ‘mouth  of  a  river’,  OI.  dfthah,  Avestic aoshta,  aoshtra,  ‘lip’,
   leaf 892 :  OF.,  fr.  VL.  ustiarius,  ‘doorkeeper’. fr.  L.  ostiarius,  of  s.m.,  fr.  ostium,  ‘door,  en¬ trance’.  See  ostiary. Derivatives:  usher,  tr.  v.,  usher-er,  n. usine,  n.,  works,  factory.  —  F.,  fr.  North  Eastern F.  wisine,  altered  fr.  Picard  ouchine,  ult.  fr.  L. officina,  ‘workshop,  manufactury’.  See  officinal. Usnea, 
### aosta []
### aoshta [589]
   leaf 589 : a  river,  bay’,  Russ. tistije,  ‘mouth  of  a  river’,  OI.  dfthah,  Avestic aoshta,  aoshtra,  ‘lip’,  OSlav.  ustina,  ‘lip’,  ustiti , ‘to  persuade’.  See  oral  and  adj.  suff.  -ary  and  cp. ostiole,  usher. ostiole,  n.,  a  small  opening,  an  orifice  (bot.)  —  L. ostiolum,  ‘a  little  door’,  dimin.  of  ostium.  See prec.  word  
### os, n []
### os,  n [41, 58, 65, 70, 71, 76, 92, 97]
   leaf 41 : al,  ‘noble family,  noble  descent’  (see  atheling),  and  funs, ‘ready’. alphos,  n.,  a  form  of  leprosoy  (med.)  —  Gk. iXpoc,  ‘dull-white  leprosy’  (whence  L.  alphus, of  s.m.);  cogn.  with  L.  albus,  ‘white’.  See  alb. Alpine,  adj.,  pertaining  to  the  Alps.  —  L.  Al- pinus,  fr.  Alpes,  the  Alps'.  See  alp  and  adj. suff
   leaf 58 : ls  (with  a  certain  topic)’.  See Apis,  a  genus  of  bees,  and  -logy. Apios,  n.,  a  genus  of  plants  of  the  pea  family (bot)  —  ModL.,  fr.  Gk.  £juo4,  ‘pear  tree,  pear’, which  is  a  loan  word  from  an  unknown  source, whence  also  L.  pirum,  ‘pear’  (cp.  pear) ;  so  called from  the  pearlike  form  of  the  tubers. Api
```


## [2026-09-07T20:19:43.073Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nimport re\nfor i in range(585,592):\n    nums=re.findall(r'(?m)^\\s*(\\d{3,4})\\s*$',leaves[i])\n    # also inline page numbers\n    print(i, nums[:6], '|', leaves[i][:80].replace('\\n',' '))\nprint('--- leaf 438 head:', leaves[438][:150].replace('\\n',' '))\n# find 'oral, adj' variants\nfor i,l in enumerate(leaves):\n    if 'See  oral' in l and 'orality' in l or re.search(r'\\boral\\b,\\s*adj', l):\n        print('oral leaf', i, l[:100].replace('\\n',' '))\nEOF",
 "description": "Find printed page numbers in Klein leaves"
}
```


### [2026-09-07T20:19:44.792Z] TOOL RESULT

```
585 ['1094', '1095'] |  coin,  prop,  subst.  use  of  the  adj. aureus,  ‘of  gold,  golden’,  fr.  au
586 ['1096'] | s  American  birds  of  the  family Icteridae.  —  F.  oriol,  fr.  OF.,  fr.  M
587 [] | �orris  root’,  which  is  identical  with  Gk. Epecoe,  gen.  of  Iptc,  ‘iris’
588 [] |   vowel  osche-,  combining  form meaning  the  ‘scrotum’.  —  Fr.  Gk.  Soysov,
589 ['1103'] | a  vowel, osteal,  adj.,  bony.  —  Formed  with  adj.  suff.  -al  fr. Gk.  oot
590 [] | h’.  See oto-  and  cyst. otolith,  n.,  chalky  matter  in  the  internal  ear 
591 ['1106', '1107'] | fr.  OE.  ofen,  rel.  to  OFris., MDu.,  Du.  oven,  OHG.  ovan,  MHG.  oven,  
--- leaf 438 head:  —  ModL.,  fr.  Gk.  eEpeauovr),  ‘a wreath  of  olive  wound  round  with  wool’,  fr. slpo q,  ‘wool’,  which  is  rel.  to  gpiov,  ‘wool’  (see e
oral leaf 583 ts.  —  F.  opticien,  fr.  ML.  optica.  See next  word  and  -ian. optics,  n.,  the  science  tha
```


## [2026-09-07T20:19:50.116Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nl=leaves[583]\ni=l.find('oral')\nprint(l[max(0,i-200):i+2200])\nEOF",
 "description": "Print Klein leaf 583 oral entry"
}
```


### [2026-09-07T20:19:51.516Z] TOOL RESULT

```
ray,  beseech’.  See  oration, oracular,  adj.  —  L.  drdculdrius,  ‘dealing  in  ora¬ cles,  prophetic’,  fr.  oraculum.  See  oracle  and  -ar. Derivatives:  oracular-ly,  adv.,  oracular-ity,  n. oral,  adj.  —  Formed  with  adj.  suff.  -al  fr.  L.  os, gen.  oris,  ‘mouth,  face;  opening,  entrance,  ori¬ fice’,  fr.  *ous-,  whence  the  collective  noun  ora (for  *os-a),  ‘border,  coast’;  cogn.  with  OI.  ah, as-an,  ‘mouth’,  asyam,  ‘mouth;  opening’,  Aves¬ tic  ah-,  ‘mouth’,  Hitt,  aish  (gen.  ishash),  Mir.  a, ‘mouth’,  ON.  oss,  ‘mouth  of  a  river’,  OE.  dr, ‘beginning,  origin,  front’,  ora,  ‘bank,  shore’, Alb.  ant  (for  *ausnd),  ‘side,  border’.  Cp.  coram, orifice,  orle,  orotund,  oscitancy,  ostiary,  ostiole, usher,  Auriga,  vera.
Derivative:  oral-ly,  adv.
orange,  n.  —  ME.  orenge,  orange,  fr.  MF.  orenge (F.  orange),  in  pomme  d' orenge,  fr.  It.  arancia (in  Olt.  melarancia,  lit.  ‘orange-apple’),  fr. Arab,  naranj  (whence  also  Sp.  naranja.  Port. laranja,  MGk.  vcpavxOov),  fr.  Pers.  narang,  fr. OI.  ndrangah,  ‘orange  tree’,  which  is  of  uncer¬ tain  origin.  The  change  of  nar-ange  to  or-ange  is prob.  due  to  the  influence  of  the  name  of  the town  Orange,  an  important  transit  station  for the  oranges  bound  for  the  north  of  France. The  usual  explanation  that  the  change  mention¬ ed  is  due  to  a  confusion  with  F.  or,  ‘gold’  (see aurum),  must  be  abandoned  owing  to  the  fact that  originally  and  for  many  centuries  the  fruit was  called  in  French  pomme  d'orange,  which makes  it  probable  that  orange  was  regarded  as  a place  name.  See  Bloch-Wartburg,  DELF.,  p. 425  s.v.  orange.
Derivative:  orange,  adj.
orangeade,  n.,  a  drink  made  of  orange  juice, water  and  sugar.  —  F.,  formed  fr.  orange  on  the analogy  of  lemonade.  See  prec.  word  and  -ade. orangery,  n.,  a  place  where  orange  trees  are  cul¬ tivated.  —  F.  orangerie,  fr.  orange.  See  orange and  -ery.
orangutan,  n.  —  Malay,  ‘man  of  the  woods,  wild man’,  fr.  orang,  ‘man’,  and  ( h)utan ,  ‘forest, wild’,  used  only  of  the  savage  tribes  inhabiting the  Sunda  Islands.  The  word  was  misunder¬ stood  by  the  Europeans  and  applied  to  this anthropoid  ape.
orate,  intr.  v.,  to  make  a  long  oration.  —  Back formatio
```


## [2026-09-07T20:20:02.176Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==252||NR==253' SYN.txt | head -60",
 "description": "Print Buck SYN p.228 (leaf 252)"
}
```


### [2026-09-07T20:20:03.414Z] TOOL RESULT

```
gri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
E BODY; BODILY FUNCTIONS AND CONDITIONS 215 4 ? ans OF TH 4.203 BRAIN Goth. ; Lith.  smegenys (pl.)
byxeparhos ON hjarnt Lett.  smadzenes Gtke yas Dan. /jerne ChSl. mozgit NG cerebrum Sw. hjarna SCr.  mozak Lat, cervello OB bragen Boh.  mozek 8 cerveau ME brain, hernes (pl.) Pol. mézg Sp. ccrebro 1.) NE brain : Russ. mozg. Rum. reiert (pl. Du. _ hersenen (pl.), brein Skt.  mastigka- if inchinn OHG  hirni Ay. mastrayan- (in pl.) NIr. alae MHG herne W. Wiese NHG _ hirn, gehirn Br | emp
Most of the words for ‘brain’ are cog- 3. Ir. inchinn, W. ymennyd, Br. em- nate with words for ‘head’ or ‘marrow’. | penn, cpds. (like Grk. éyxégados) fr.
Sometimes the plural used as coll., like NE brains, is the usual form.
1, Derivs. of *her(a)s-, etc. seen in Skt. ciras- ‘head’, Grk. xépas ‘horn’, etc. Walde-P. 1.403 ff.. Ernout-M. 177. Walde-H. 1.208. Falk-Torp 410. REW 1826, 1827.
Lat. cerebrum (> Sp. cerebro, Rum. creier used mostly in pl. cerierz), cerebel- lum (>It. cervella, Fr. cerveau); ON hjarni, OHG hirni, etc., general Gme. (except English, where ME hernes, Sc. harns fr. Norse).
2, Grk. eyxébados phrase cpd. fr. & ‘in’ and xedady ‘head’.
NG yvaé, often pl. ra pvadd, fr. Grk. hueXbs, late wvadds ‘marrow’. Cf. Aris- tot. PA 65225 roddots yap kal 6 éyxépados
boxe? nuehés elvar ‘for many think the brain is really marrow’.
words for ‘in’ and ‘head’ (Ir. cenn, etc., 4.20).
4. OE bregen, ME, NE brain, Du. brein, prob. : Grk. Bpexpuos, Bpeypa “front part of the head’. Walde-P. 2.314. NED s.v. brain. Franck-v. W. 91.
5. Lith. smegenys (pl.), Lett. smad- zenes (or pl. -is), ChSl. mozgii, etc. (all the Slavic words) : Skt. majjan-, ON merg, OE mearg, NE marrow, OHG mar(a)g, NHG mark, etc., all ‘marrow’ (Av. mazga once, ‘marrow’ or ‘brain’? NPers. mayz both), root connection? For the association of ‘marrow’ with ‘brain’, see above, 2. Walde-P. 2.309.
6. Skt. ‘skull’ (4.202).
Av. mastrayan- in pl. ‘skull’ (4.202) and ‘brains’ (Yt. 10.72). Barth. 1155.
mastiska- : mastaka-
-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
SELECTED INDO-EUROPEAN SYNON
YMS
216 4.204 FACE
Grk. — xpdawrov Goth. andwairpi, wlits, an- Lith. _vetdas NG Tpbcw7ro dawleizn, ludja Lett. vaigs Lat.  faciés ON andlit ChSl. lice It. Jaccia (viso) Dan.  ansigt SCr. lice Fr. visage Sw. ansikte (anlete) Boh.  tvd¥ Sp. cara (rostro) OE ansjn, andwlita Pol. = twarz Rum. fajd, obraz ME face Russ. ico Ir. agad, enech NE face Skt.  anika- Nir. aghaidh Du. —geztcht Av. ainika-, &iOra- W. wyneb OHG  gesiht, anitlutli, an- Br. dremm nuzzt
MHG  gestht, antlitze_
NHG | gesicht (angesicht,
antlitz)
The face is the most distinguishing and expressive portion of the body, and the words for ‘face’ are most commonly based on the notion of ‘appearance, look’, most of these derived from verbs for ‘see, look’, or in some cases on the no- tion of ‘form, shape’. There is some- times interchange between ‘face’ and ‘cheek’ in the same word or group.
Included in the list Gn parentheses) are some words that are synonyms of those given in first place, either popular (but not vulgar, as NE mug), as It. viso, Sp. rostro, or now restricted to a lofty style, as NHG angesicht, antlitz.
1. Grk. rpdcwzov (in Hom. always pl.), fr. wpos ‘toward’ and deriy. of é7- (IE *ok*-) in dpouat fut. of dpaw ‘see, look’, doce ‘eyes’, dp also ‘face’, etc. (15.51). Hence orig. the ‘appearance, look’.
2. Lat. faciés, orig. ‘form, shape’, then esp. ‘face’, fr. facere ‘make’. Hence, through VLat. *facia, It. faccia, Fr. face (> ME, NE face), Rum. faté (Port. face ‘cheek’, Sp. haz, faz fig.). But the use of Fr. face for the ‘face’ of a person was given up in the 17th cent. (Wart- burg 3.356). Ernout-M. 322. Walde- H. 1.489. REW 3130.
Fr. visage, fr. older vis (now only in vis-d-vis) = It. viso (pop. for faccia), fr. Lat. visus, ‘sight’. REW 9384. Gamill- scheg 893.
Sp. cara (the once quoted ante caram, Corippus in laud. Justini 2.413, is a false reading of ante casam now in the edi- tions of Partsch and of Petschenig), OFr. chiere (> ME chere, NE cheer, NED s.v.), generally taken as fr. Grk, kapa ‘head’. The difficulties are (1) the fact that xapa is only found in poets, (2) the change in sense (but «dpa used for ‘face’ in Soph. El. 1310), (3) the restric- tion of the group to the West. Appar- ently one would have to assume a liter- ary poetical borrowing as the starting point, or else that the Grk. word was in ordinary prose use among those who founded the colonies in Spain and south- ern Gaul. REW 1670. Diez 87. Wart- burg 2.350.
Sp. rostro (pop. word for ‘face’, not vulgar), fr. Lat. rdstrum ‘beak’. REW 7386.
Rum. obraz, fr. Slavic, ChSl. obrazit ‘form, shape, image’ (12.57), SCr. obraz ‘cheek’, ete. Tiktin 1072 f.
3. Ir. agad, NIr. aghaidh, etym.? Pedersen 1.129.
Ir. enech, MW, MBr. enep, W. wyneb, (Br. enep, eneb ‘the opposite’), a cpd. of IE *okv- ‘see’, like Grk. mpéowmov (above, 1) and &dmos ‘facing’, Skt. anika- ‘face’? Walde-P.
```


## [2026-09-07T20:20:04.680Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== BQT v1 ازغ ===\"; grep -n 'ازغ\\|اژغ\\|ازگ' BQT_v1_pages.txt | head -20; echo \"=== MON ازغ ===\"; grep -n 'ازغ' MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt 2>/dev/null | head -20",
 "description": "Grep Borhan and Moin for azgh"
}
```


### [2026-09-07T20:20:04.765Z] TOOL RESULT

```
=== BQT v1 ازغ ===
422:طی همین تفسیر نام‌گروهی ازگزارندگان یا مفسران اوستا نیز یا دگردیده
1300:۸ بازغلامی۳۷018101ع۷82 در بازغلام ۷ (یامر) .
7738:۱ -ر:آزوری. ۴ - ره:آژغ‌وازغ.
7916:بازغلامی 25۳000 , سریکلی 82511188 «گربرسن ص ۰*۷۲ تهرانی 2560008 .
8894:حنگام ٩۱‏ واشاره بچیزی دور باشد ازغیرذوی-
9172:زآهختن نیخ‌ها ازغلاف
11292:۵ ازه - (فتح اول) - : ازغ .
11433:۵ - 1(<۲2800. ۱ - ر۵: ازغ۱ <<
17534:ازغایت سبری میلبطمام نکردن و چیزی‌نشوددن ] و ستگه درازی را یز ود که با رود
18586:پر سر آ هدن - کنابه ازغلبه وافزونی
21350:پیوسته درکنار آب نشیند وازغم آنکه مباداآب
22230:کنابه ازگوشت است که بتازی لحم کوند .9
24160:ویششیدن . ۵ پخضانیدن - بفتح اول وهفتم» فراهم آمدن ازغم ودرد. بغانیدن :
26074:ریز نازگ بسیارتنك دایچ را کوشد .
28336:ازغم و الم بهم رسیده باشد - وفشارش و فشردن
29050:تافتن دل‌باشد ازغم‌والم» د بسکونانی‌هم گفته‌انده
31310:مانند جوشن لیکن غیبهای:نوره درازترازغیبهای
32204:کمانم ازغم آن تبروار فامت تو
=== MON ازغ ===
incoming/MON/MON_2vol_Adena_v1_djvu.txt:10628:ازغ: «ه [- آزغ < اژغ - ازگ] (.) آنچه 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:10820:ازغ: بقه [- ازغ - آژغ - ازگ] (.) 
MON_part2.txt:270:غازغاز: 72ب.«(ص.) از هم شکافته و باز 
MON_part2.txt:272:غازغان: 22 [تر. - قازقان - غزغن] (.) 
MON_part2.txt:1630:غزغان: 00 ا[تر. مغ. - غازغان ‏ غرغن 
MON_part1.txt:10628:ازغ: «ه [- آزغ < اژغ - ازگ] (.) آنچه 
MON_part1.txt:10820:ازغ: بقه [- ازغ - آژغ - ازگ] (.)
```


## [2026-09-07T20:20:12.904Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR>=264&&NR<=266{print \"=== leaf \"NR\" ===\"; print substr($0,1,3000)}' SYN.txt",
 "description": "Print Buck leaves 264-266 (MOUTH)"
}
```


## [2026-09-07T20:20:13.911Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '10620,10640p;10815,10830p' MON_part1.txt",
 "description": "Print Moin azgh entries"
}
```


### [2026-09-07T20:20:14.377Z] TOOL RESULT

```
=== leaf 264 ===
tw
Digitized by Arya Samaj Foundation Chennai and eGangotri_ .
ternal ear), deriv. of ofr ‘hear’, fr. Lat. audire ‘hear’.
3. Ir. cliias, NIv. cluas, W. clust : ON hlust ‘ear’ (beside eyra, cf. Vigfusson s.v.), OE hlyst ‘hearing’, hlystan ‘hear, listen’ (NE listen), etc. fr. IE *fKleu-s-, beside *kleu- in Skt. gru-, Grk. kdb ‘hear’, etc., from which root also Skt, grotra- ‘hearing, ear’, Toch. A klots, B klautso ‘ear’ (SSS, 128, 129). Walde- P. 1.494 f. Pedersen 1.80,
Br. skouarn, Corn. scovarn, W. ysgy- farn (obs.), etym. dub., but perh., fr. a *skeu- beside IE *keu- in Grk. xotw ‘per- ceive, hear’, Lat. cavére ‘beware’, Goth. hausjan ‘hear’, OF scéawian ‘look at’, etc. (15.41, 15.52). Henry 243. Win- disch ap. Ernault, Dict. étym. 377. Less probably Pedersen 2.53.
4, Skt. karna-, Av. karana- (of evil beings), etym.? Walde-P, 1.412, 495.
Av. gaosa-, OPers. gauga- (NPers. gos ‘ear’) : Av. gus ‘hear’, Skt. ghosa- ‘noise’, ghosati ‘sounds, calls’. Walde-P. 1.569.
Ay. us (dual), above, 1.
an inherited group. The others are scure origin.
ae Dies nas-. Walde-P. 2.318. Emout-M. 653, 659. Falk-Torp 779 f. Lat. nasus (> It. naso, Fr. nez, Rum. nas), also pl. narés ‘nostrils, nose’, late sg, naris (>Sp. nariz); ON sg. ngs nostril’, pl. nasar ‘nostrils, nose’, OE nosu, nasu, OHG nasa, etc., general Gme.; Lith. nosis, OPruss. nozy; ChSl. nosit, etc., general Slavic; Skt. nas-,; nas- (in RV only dual, nom. nasd, gen. nasos), Ay., OPers, nah- (sg. and dual in Av., sg. in OPers.). The meaning ‘nostril’ is implied by the early use of dual or pl. forms, but is not necessarily older than ‘nose’, For it may be abstracted from the latter, and the dual was favored by i ae in the case of ‘eyes’, ‘ears’, 2. Grk. pts, gen. pivds, also pl. pives ostrils, nose’ (like Lat. narés), etym.? . Seng ane either : Pr TAG ES i c, (Boisacq 842) or : with query) i ete. (Walde-P. 1.140
Possible, the word being
n
Digitized by Arya Samaj Foundation Chennai and eGangotri
am BODY; BODILY FUNCTIONS AND CONDITIONS 227
gprs OF T 4.23 NOSE Lith. nosis Goth. .--- pis ON nasar Lett. deguns Gre im Dan. nase Chsl. nosit nasus Sw. nisa SCr. nos naso OE nosu Boh. nos nez ME _~ nose Pol. nos nariz NE nose Russ. os Rum. nas Du. neus Skt. nas-, ghrana- sron OHG nasa Av. nah- sron MHG nase i NHG nase Tl Most of the words for ‘nose’ belong to | then orig. a vulgar epithet, displacing Mo:
the IE word, like the following which displaced it in turn.
NG porn, fr. Grk. pizis used by Aris- tot. (HA 52415 ff.) for an organ of the cuttlefish connected with the ink sac, and attested as a vulgar term for ‘snout, n
=== leaf 265 ===
ose’ by Eust., Comm. 950 (oi ri piva pirw xadécavres), prob. : Lith. mute, Skt. mukha- ‘mouth,’ etc. (4.24). Walde-P. 2.310.
3. Ir. srén = W. ffroen, Br. fron ‘nos- tril’ (here in some way Br. fri ‘nose’, MBr. fry), fr. *skrok-na-, prob. : Skt. srakva- ‘corner of the mouth’, and fr. the root in Ir. srennim, Grk. peyxo, péyxw ‘snore, snort’, of imitative origin. Walde-P. 2.705. Pedersen 1.82. Lewis- Pedersen 22.
W. trwyn, OCorn. trein, perh. fr. an imitative group parallel to the preceding (cf. Grk. sbyxos ‘pig’s snout’). Pedersen 1.82. Morris Jones 156.
4. Lett. deguns, etym.?
5. Skt. ghrdna- ‘smell’ and ‘nose’, fr. ghra-~ ‘smell’ (15.21).
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
228 SELECTED INDO-EUROPEAN SYNONYMS
4.24 MOUTH Grk.  orépa Goth. munps Lith.  burna NG oroya ON munnr (midr) Lett. mute Lat. Gs Dan. mund ChSl. usta It. bocca Sw. mun SCr. usta Fr. bouche OE mip Boh. iista Sp. boca ME mouthe Pol. usta, geba Rum. gurd NE mouth Russ. rot Ir. gin, béoil Du. mond Skt. mukha-, Gs-, ete, NIr. _béal OHG mund Ay. Gh-, zafar- W. geneu MHG munt Br. genou NHG mund
The IE word for ‘mouth’ persisted in several languages in the literal sense, in some others in secondary uses, but was to a large extent replaced by other words. Most of these were originally ex- pressions applied to the mouth of ani- mals and vulgarly of persons, like Lat. rostrum, NHG maul, NE jaw, snout, mug, and many others (not included in the list, except where they have become standard words for ‘mouth’). There is frequent association between ‘mouth’ and ‘throat’, ‘jaw’, ‘check’, ‘chin’ or ‘lip’.
1. IE *0(u)s-, *aus-. Walde-P. 1.168. Ernout-M. 714 f.
Lat. ds (also dstiwm ‘door, entrance, river-mouth’, dra ‘edge, coast’); Ir. a (rare); OPruss. austo (Lith. uostas ‘river- mouth’); ChSl. usta, etc., general Slavic (but Russ. usta obs.); Skt. as-, dsan-, asya-, Av. ah- (also Skt. ostha-, Av. aosta- ‘lip’); cf. also ON ass ‘river- mouth’, OF Gr ‘beginning’, dra ‘edge, bank’, etc. But Hitt. ais, gen. issas ‘mouth (Sturtevant, Hitt. Gloss, with refs.) points to a parallel *ais-.
2. Grk. orbpa: Av. staman- ‘dog’s mouth’, W. safn ‘mouth, jaws’ (of ani- mals), MBr. staffn, Br. staon ‘palate’, root connection? Walde-P. 2.648. Ped- ersen 1.78.
3. It. bocca, Fr. bouche, Sp. boca, fr. Lat. bucca ‘puffed-out cheek’ (4.208) and also a pop. substitute for ds (cf. Thes.
s.v.). Ernout-M.110. Walde-H. 2.120, REW 1357.
Rum. gurd (so Alb. gojé ‘mouth’, Fr, gueule ‘mouth, jaws’ of animals, in some dial. common word for ‘mouth’), fr. Lat, gula ‘throat, gullet’ (4.29).
Lat. gurges ‘whirlpool’, late gurga, has through ‘throat’ (Fr. gorge) given dial, words for ‘mouth’; likewise Lat. rastrum ‘beak, snout, mouth’ (of animals, vul- garly of persons), as ORum. rost. REW 3921, 7386
=== leaf 266 ===
us ‘cheek’, etc. (4.207).
Ir. béoil, NIr. béal, see bel ‘lip’ (4.25).
5. Goth. munps, OE mip, OHG mund, ete., general Gmc., prob. : Lat. mentum ‘chin’, etc. (4.209), rather than : Lat. mandere ‘chew’, as preferred in Walde-P. 2.270, Falk-Torp 738. Feist 368. Ernout-M. 608.
6. Lith. burna: Bulg. biirna ‘lip’, Arm. beran ‘mouth’, Ir. bern ‘cleft, gap’, Grk. dapayt ‘cleft, ravine’, ¢dapvyt ‘throat’, etc. Walde-P. 2.159. Traut- mann 40.
Lett. mute: Skt. mukha- ‘mouth’, etc. (below, 8).
7. ChSl. usta, etc., above, 1.
Pol. geba : Boh. huba, SCr. gubica (both ‘mouth’ only in derogatory sense, ‘mug’), Russ. guba ‘lip’, ChSl. gaba ‘sponge’, Lith. gumbas ‘swelling, protu-
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
——aaEEoEEeEEEeEeEeEeEeEOeGGeeeee ee
; Lett. gumba ‘{umor’, sa pera 568. Brickner 138 ff. (Ber- a ae akes two separate groups.) ,; Chsl. rit ‘peak’, SCr. rt a Boh. ret ‘Jip’, etc., these Lee oe. ‘projection’ (whence a th’ or ‘Lip’ through ‘snout’ of ‘ante ae Lat. ort? ‘rise’, Okt. T$va~- ‘thigh’, we S. Lane, AJPh. 54.64.
a git, (beside as-, etc., above, 1)
Digitized by Arya Samaj Foundation Chennai and eGangotri
DY; BODILY FUNCTIONS AND CONDITIONS 229
mukha- : Lett. mute ‘mouth’, OHG mi- la, NHG maul ‘mouth’ (of animals, vul- garly of persons), Lett. maut ‘roar’, etc., an imitative group based on an utterance like Grk. pb, Lat. mu. Walde-P. 2.309 ff.
Skt. vadana-, vaktra- ‘mouth’ as organ of speech, fr. vad-, vac- ‘speak’ (18.21).
Av. zafar- ‘mouth’ (of evil beings) : OE ceafl, NHG kiefer ‘jaw’. Walde-P. 1.570f. Barth. 1657.
4.25 LIP
Gr. xethos Goth. wairiloém (dat. pl.) ar lipa
ie ck ON vorr tt.  lipa ss ala Dan. abe ChSl. ustina - * Jabbro Sw. léppe SCr. usne fr eure OE weler, lippa Boh. vet (pysk) Sp.  labio ME — lippe Pol. warga Rum. buzd NE lp Russ. guba Ir. bal Du. lip Skt. ostha- Nir. _ béal, puisin OHG leffur, lefs Ay. aosta
W. — guefus (weft) MAG: ieee) Br.  gweuz, muzell NHG lppe
Some of the words for ‘lip’ are from the notion of ‘hanging down’ or ‘pro- jecting’. Several are connected with words for ‘mouth’, the lips being the visible part of the mouth.
1. Grk. xefdos, Dor. xfdos, Aeol. XMos (*xédvos; cf. also xedtvn), NG xe (based on pl. 7& xelAn) : ON gjolnar gills’, root connection? Walde-P. 1.682, Falk-Torp 319.
2. Lat. labrum (> It. labro), pl labra, late as f Fike ae em. sg. (> Fr. lévre), ae Sp. labio) : OB lippa, NE 10) fs leffur, lefs, NHG lippe (fr.
» Cle. (see list), root connection un-
Certain, but more prob. : Skt. lamb-
h St Lat. labare ‘slip’, ete. (on IC side, cf, below, 5) than : Lat
mb re sry ba a cg gue. 2.384, Er- 1808 re * Walde-H, 1.738 f. REW ; 18. Falk-Torp 672.
UM. buz¢ R (Cf. below, 3) or like Al
```


### [2026-09-07T20:20:14.421Z] TOOL RESULT

```
است. از طرف دیکّر: از سوی دیگر» از 
جانب دیگر. به دیگر سخنء به عبارت 
ازعاج: و2 [ع.] (مسصم.) از ای 
برانگیختن برخیزانیدن» جنبانیدن» قلع از 
مکان. برآوردن؛ قطع کردن. رون آوردن» 
بیرون بردن لشکر را. گسیل کردن؛ فرستادن» 
بی آرام ساختن» به ستوه و 

ازغ: «ه [- آزغ < اژغ - ازگ] (.) آنچه 
ار شاخه‌های درخت که ببرند و بیرایش 
دهند» آنچه از شاخه‌های درخت انگور 
برند. شوخ و چرک تن. 

از قبل: 2002 [ف. غ.] (حر. اض. مر.) 
از جانب» از سوی, از جهت. 

از قلم افتادن: 7- 2272123 [ع. ف.) 
(مصل.) از نوشته حذف شدن, در هنگام 
نگارش فراموش شدن و به نگارش در 
نبامدن. 

مشبه به کلک با قلم. ازدهای علم: اردهای 
رایت» صورت ازدها که بر علم نقش کنند. 
ازدهافش: 4-.: [- اژدهاوش] (ص‌مر.) 
آنکه به شکل و هیثت اژدها باشد؛ اژدها 
صورت. اژدها منظر. لقبی برای ضحاکك. 
ازغ: بقه [- ازغ - آژغ - ازگ] (.) 
شاخه‌هایی که از درخت بریده باشند» ت رکه» 
شاخة باریکک و لمس. شوخ؛ چ رکث. 
اژکهان: مضه [- اژکهن - اژکان - اژهان 
- اژهن] (ص.) کاهل» تتبل» مهمل» بیکاره. 
ازیر: :22 [- آژیر] (ص.) هوشمندء 
زیرکك» هصوشیار» دکی؛ دانا» عاقل» 
پرهي زگار؛ اون 

اس: (0568 [ع. ۰] (.) سنیاد» سنلاد» بسنورة 
دیوار» شالده» بن» بی. اس اساس: بنیاد و باية
```


## [2026-09-07T20:20:30.133Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== MON ازم ===\"; grep -n '^ازم\\|ازم:' MON_part1.txt | head; echo \"=== BQT v1 page tags near 114 ===\"; grep -n '\\[pdf page 11[0-9]\\]\\|\\[pdf page 12[0-9]\\]' BQT_v1_pages.txt | head -20",
 "description": "Grep Moin azm and BQT page tags"
}
```


### [2026-09-07T20:20:30.201Z] TOOL RESULT

```
=== MON ازم ===
2952:ازمایید» بیازما(ی)» ازماینده» ازمایده)» 
2955:ازمند: 20 (ص‌مر.) ربص 
2958:ازمودن: ۲( )22 (مص م ۱ آزموده 
10722:ازماع: "مست [ع.] (مص‌م.) عزم بر کاری 
10727:ازمان: 2210 [ع.] (مص‌ل.) کهنه شدن» 
25161:ازمون. سختی: کر فتاری. شورش. صح.- در 
36662:ازمنه‌ای که هنوز شواهد و آثار آن موجود 
43099:تلازم: 920۳ [ع. ۰] (مص‌ل.) همراه بودن. 
46697:جازم: ۱۳۳ [ع.] (افا.) بر نده» قطم کنده 
46704:خبر. قول جازم: مشتمل بر اخبار امری به 
=== BQT v1 page tags near 114 ===
```


## [2026-09-07T20:20:32.533Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== CHEUNG zan ===\"; grep -n -E '^\\*?zan|zan-|\\*zanH' CHEUNG.txt | head -20; echo \"=== CHEUNG zah/zā ===\"; grep -n -o -E '.{80}(zādan|zāyīdan|zahīdan|zih).{120}' CHEUNG.txt | head -10",
 "description": "Grep Cheung for zan"
}
```


### [2026-09-07T20:20:32.613Z] TOOL RESULT

```
=== CHEUNG zan ===
2100:comparing the Persian form to Av. barazan- ‘top’. 
5155:dastén/dazan-, Siv. derz-, dirz-/dist, Tr. dasta/darz- ‘to sew’, NP darzan ‘needle’ 
15078:*MIDDLE PERSIAN: MMP zn-, BMP zn- /zan-/ ‘to beat, strike, smite; to play an 
15118:*NWIR: Widely attested: NP zadan/zan-, Zaz. jinayis/jinen-, Gz. Zen-/Zent ‘to beat, 
15130:Rosh. zan-/zod, Sariq. zon-/zed, Yzgh. Zan-/Zud ‘to beat, kill’ || (+ *abi-) Yzgh. 
15132:bizid, Khf. bizoen-/bizod, Rosh. bizin-/bizod, Bart. bizan-/bizód ‘to drive into, 
15135:*MISC: Par. jan-/j6, Orm. zan-/zök ‘to beat, strike’= zan-/jök, zók, jan-/jök, zók || (+ 
24368:Yzgh. tozan-/tazant ‘to turn, whirl’, Sh. (Baj.) täz-/täzd, Rosh. téz-/tézd, Bart. toz-/ 
29768:*us.zazonti by Bartholomae, AIW: 1658 and interpreted as 3р1. SUBJ. ‘they breed’ (*zanH!), but Kellens 
29770:3pl. IND. (*zanH’). 
30019:*zanH! ‘to give birth; (pass.) to be born’ 
30026:*zanHl 465 
30081:466 *zanH2 
30088:born, grow’, Pash. zöwul, zézédal ‘to be born’, Yghn. zan-/zänta ‘bear, give birth; to 
30113:*zanHË ‘to know’ 
30115:*AVESTAN: zan- ‘to know’ || (+ *aua-) ‘to perceive, recognize’ || (+ *pati-) ‘to 
30145:*zanH2 467 
30181:Snàs- (inch.) ‘to get to know, recognize’, NP danistan/dan-, Bal. zan-/zant, Kurd. 
30182:zanin/zan-, Zaz. zanayis/zan-, Tt. (Esh.) zun/zund, Anar. -izono/ezon-, Awrom. 
30183:zanay/-zan-, Fariz. zonást-/zon-, Yar. zönäj-/zön-, Gz. zün-/zünast, (LW) Gil. (Rsht.) 
=== CHEUNG zah/zā ===
```


## [2026-09-07T20:20:36.727Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '30019,30112p' CHEUNG.txt",
 "description": "Print Cheung zanH1 entry"
}
```


### [2026-09-07T20:20:36.771Z] TOOL RESULT

```
*zanH! ‘to give birth; (pass.) to be born’ 

*AVESTAN: YAv. za(n)- ‘to give birth; (pass.) to be born’ || (+ *us-) ‘to breed, 
produce; be produced, bred’ || (+ *ni-) YAv. nizanta- ‘born (in one’s own house)’ 
(F730) > Liste: 67 


*zanHl 465 


Pres. them. red.: IND. 3pl. YAv. zizananti (Yt 13.15), ? YAv. "us.zizanonti (V 3.5; De Vaan 2003: 213), 
INJ. 3pl. YAv. zizanon (Vr 1.3, Vr 2.3), SUBJ. 3sg. YAv. zizanät (Yt 13.142); Partic.: pres. YAv. 
zizanäti (Yt 5.129), fut. med. YAv. zahiiamna- (Y 4.5, 24.10, Vr 11.13), perf. pass. YAv. zäta- (Y 9.5, Y 
65.6, Yt 19.56, etc.); Pass.: IND. 3sg. YAv. zaiieiti (Yt 13.16), 3du. ҮАУ. us.zaiioie (Y 9.10), 3pl. ҮАУ. 
*us.zaiieinti (У 2.41), INJ. Zeg YAv. us.zaiiagha (Y 9.13), 3sg. YAv. хайаа (V 1.17), SUBJ. 35р. ҮАУ. 
zaiiaite (V 19.5), 3pl. YAv. zaiiante (Y 11.6, Vyt 1, Vyt 3, etc.) 

*MIDDLE PERSIAN: MMP z’y(h)-, BMP z” (YLYDWN-) /za-/ ‘to be born; to give 
birth, bear’, MMP z’yn- (sec. caus.) ‘to bear, give birth to, bring forth’ || (+ *a-) 
MMP d ВМР с? /azad/ ‘noble, free’ || (+ *fra-) MMP frzynd, ВМР prznd 
/frazand/ ‘child, son, offspring’ (LW) > DMMPP: 380b f., 84b, 161a 

Pres.: IND. 3sg. MMP z’yyd, z’’yyd, z’yd, 3pl. MMP z’ynd, z’yynd, SUBJ. 3pl. MMP z’y’nd; Pret.: 
IND. Isg. MMP z’dm; Partic.: perf. pass. MMP z'd, (pl) ВМР z’t’n /zadan/, caus. II MMP z’yn’d, 
z’ynyyd; Caus.: pres. IND. 2sg. MMP z’ynyy, 3sg. MMP “z’yn’d; Inf.: ВМР zim /zadan/; Pass.: pres. 
IND. 3sg. MMP z’yhyd, 3pl. MMP z’yhynd 

*PARTHIAN: z’y- ‘to give birth to; be born’, z’dg ‘son’ || (+ *a-) *()jy- ‘to be reborn’, 
"z'd ‘noble’ || (+ *fra-) frzynd ‘child, son’ = Ghilain: 87 f. | DMMPP: 380b f., 84b, 
161a 

Pres.: IND. 3sg. z’yyd, z'yd ‘is born’, Ipl. z’y’m, 3pl. z’ynd ‘they bear’, SUBJ. 3sg. "z'y'h, OPT. 
z’yndyy; Partic.: perf. pass. z'd || (+ *4-) Pres.: IND. 3sg. "ууа, 3р1. ’jynd, "pd 

*KHOTANESE: уѕап- ‘to give birth to’, ysai- (pass.) ‘to be born’, ysyafi- (caus.) ‘to 
cause to be born’ = SGS: 112, 114 

*SOGDIAN: BSogd. zn-, CSogd. zn-, MSogd. zn- ‘to bring forth’ || (+ *abi-) BSogd. 
Bz’yn ‘offspring, son’ || (+ *a-) BSogd. ’’z’y, BSogd. ’’z’y ‘to be born, be produced, 
grow; [tr.] to beget, produce’, MSogd. "y ‘to be born’ || (+ *upa-) MSogd. рх? 
‘birth place’, MSogd. pz’tyk ‘homeland-’ || (+ *fra-) BSogd. Bs’nt’k, Bs’ntk ‘child’ 
(Sims-Williams 1983: 50; MacKenzie, SCE: 39) || (+ *ni-) nyz’tcw (f.) ‘born (in 
one’s own house)’ (Yoshida — Moriyasu 1989: 23) 

Pres.: IND. 3sg. (intr., med. ?) znty (v. Gharib 1965: 99), SUBJ. 3sg. CSogd. zn’t ‘she wants to give 
birth’, IMPV. 2pl. MSogd. znd’ bring forth’; Pret.: tr. IND. 3sg. CSogd. znd’rt, Partic.: pres. CSogd. 
zn'mnty ‘giving birth’ || (+ *a-) Well attested: Pres.: IND. 35р. BSogd. ’’z’yt, BSogd. "zyt, OPT. BSogd. 
тугу, etc. 

*CHORESMIAN: Z d (ppp.) ‘born’, z’dk ‘son’ 

*BACTRIAN: бобо, Cadyo, Cadayo ‘born, native’ || (+ *abi-) “aßlavavo (pl) 
‘descendants’ || (+ *а-) aCu- ‘to be born, be produced’ || (+ *fra-) робо, 
oopCivdo ‘descendant’ || (+ *ni-) viķaðayo ‘born (in one's own house)’ = S-W, 
Bact.: 177b, 173, 230a, 208b 

*NWIR: NP zäyad ‘is born’, Bal. za(y)-/zat, zah-/zahit, Kurd. zayin/zé- (also 
pass./intr.), Zaz. zayis/zén-, Abz. zowa/zon-, Anar. (pres. 35р.) ezoya, Awrom. 
zay/-z-, Tt. (Chal za/zas, (Ram.) zā/zāst ‘to give birth’, Gz. zén-/zint, zent, Gil. 
(Rsht.) zaan/zaj-, Gur. (Kand) za/-zi, Khuns. za-/za, Mah. zö-/zä ‘to bear, bring 


466 *zanH2 


forth’ || (+ *a-) NP azad, Kurd. аха ‘free’, (Sor.) ‘free; hero’, Gz. äzzä ‘free’ || (+ 
*fra-) NP farzand ‘child, son’ (< Pth.) 

*NEIR: Oss. I. zajyn/zad, D. zajun/zad ‘to bear, bring forth [usually of animals]; to be 
born, grow’, Pash. zöwul, zézédal ‘to be born’, Yghn. zan-/zänta ‘bear, give birth; to 
be born’, (orig. caus.) Sh. (Baj.) zi(y)-/zod, Rosh. zay-/zöd, Sariq. zey-/züd, zid ‘to 
bear’, Yi. ziy-/zuy- ‘to bear a child’, Yghn. Zuta ‘child, son’ || (+ *a-) ? Wa. 
yoz-/yozd-, Zit- ‘to bear [of animals]’ || (+ fra-) Sh. rizin, Khf. rizoen, Rosh. rizén, 
Bart. razen, Orosh. rizin, Sariq. rajen ‘daughter’ 

*MISC: Par. zà-, Orm. zay- ‘to be born’ = zay-/zayok || (+ *à-) Arm. (LW) azat ‘free’ 
*SANSKRIT: jan! ‘to produce, cause to be born, create’ (RV+) > EWAia I: 567 f. 

© This root has an impeccable IE etymology. 

«PIE *бепН,- ‘to beget, bear, produce’ = LIV: 163 f. | Pok.: 373 ff. 

*IE COGNATES: Gr. үіүуорол ‘I become, come into being’, OLat. genunt ‘they 
produce’, (ppp.) Lat. nätus ‘born’, Olrish gainethar ‘to descend from, to be 


produced’, Arm. cnanim ‘I am born, bear’, Goth. airba-kunds ‘of earthly origin’ 
*REFERENCES: KPF I: 81b f.; Ivanow 1926: 422; EVP: 103 f.; IIFL I: 302a, 414b; EVP: 103; KPF II: 202; 
Christensen, Contributions I: 67; IIFL П: 277a, 555b; Andreev — PeSéereva: 367a; MacKenzie 1966: 114; 
EVS: 109b, 71b; WIMI: 74; WIM II/1: 86; WIM II/2: 639; Abaev, Slovar' IV: 284 f.; Cabolov 1997: 73; 
Werba 1997: 288 f.; Paul 1998: 320a; Steblin-Kamenskij 1999: 431; Cabolov 2001: 105; Kiefer 2003: 
210; Lecoq 2002: 125; Shahbakhsh: s.v. za(h)-Korn 2005: 109 f., 379 (passim)
```


## [2026-09-07T20:20:57.157Z] TOOL CALL #29: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-07T20:20:57.163Z] TOOL RESULT

```


```


## [2026-09-07T20:21:00.470Z] TOOL CALL #30: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B2%D9%87%D8%AF%D8%A7%D9%86",
 "prompt": "Give the full Persian etymology section for زهدان (zehdân) 'womb', and any related entries for زه."
}
```


## [2026-09-07T20:21:02.530Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%83%C3%A9h%E2%82%81os",
 "prompt": "Give the reconstruction, gloss, and full list of descendants (Latin, Avestan, Sanskrit, Hittite) for this PIE root for 'mouth'."
}
```


### [2026-09-07T20:21:04.778Z] TOOL RESULT

```
# Persian Etymology for زهدان (zehdân)

## Etymology Section
According to the Wiktionary entry, the word زهدان is composed of two elements: "From _زه_ (zah, zih) +‎ _ـدان_ (-dân)."

The term combines a root element زه with the Persian suffix -dân, which is a common suffix used to form nouns denoting containers or places.

## Related Entry: زه
The source references زه as a component, linked within the etymology section, though the full definition of this root element is not provided in the excerpt shown. The suffix ـدان (-dân) is similarly referenced as a productive morphological component in Persian.
```


### [2026-09-07T20:21:08.511Z] TOOL RESULT

```
# Proto-Indo-European Root for "Mouth"

**Reconstruction:** *h₁óh₃s (n.)

**Gloss:** "mouth"

**Descendants:**

1. **Latin:** ōs (from Proto-Italic *ōs)
2. **Sanskrit:** आस् (ā́s) (from Proto-Indo-Aryan *HáHs)
3. **Avestan:** 𐬁𐬵 (āh) (from Proto-Iranian *HáHs)
4. **Hittite:** 𒀀𒄿𒅖 (a-i-iš /aiš/) and 𒅖𒊭𒀸 (iš-ša-aš /iššaš/) (from Proto-Anatolian)

The reconstruction remains debated among scholars, with alternative proposals including *h₁éh₃-s, *h₁óh₁-s, and *(h₁)óh₁-s ~ *(h₁)éh₁-s-e/os, reflecting differing interpretations of laryngeal placement and inflectional patterns across daughter languages.
```


## [2026-09-07T20:21:14.322Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B2%D9%87",
 "prompt": "List all Persian etymologies given for زه (zeh / zah), especially any meaning 'birth / to give birth' and 'seepage water'. Quote the etymology text."
}
```


## [2026-09-07T20:21:14.907Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/odd",
 "prompt": "Give the full etymology of 'odd', including Old Norse oddi, oddr, Proto-Germanic form and PIE root."
}
```


### [2026-09-07T20:21:20.369Z] TOOL RESULT

```
# Persian Etymologies for زه (zeh/zah)

## Etymology 2 (Birth/Childbirth)

**Source text:** "Ultimately from Proto-Indo-European *ǵenh₁- ('to give birth'). Compare Avestan ząθa ('birth'), Sanskrit ja ('son of, birth'), Ancient Greek gónos ('procreation')."

This etymology describes the word's connection to birth-related meanings, including its use as a verb stem and as an archaic noun for childbirth.

## Etymology 3 (Water/Seepage)

**Source text:** "Inherited from Middle Persian *zah, attested in zhʾpk' (zahābag, 'spring, source'). Compare also zhʾk' (zahā, 'depth')."

This etymology links the term to water sources and springs, with derived terms like زهکش (drain/sewer) reflecting this semantic field.
```


### [2026-09-07T20:21:22.725Z] TOOL RESULT

```
# Etymology of "Odd"

The word "odd" traces back through several language layers:

**Old Norse Origin**: The term derives from Old Norse *oddi*, meaning "third or additional number," as seen in *odda-maðr* ("odd man"). The literal meaning of *oddi* is "point of land, angle," related through the concept of a triangle to *oddr*, meaning "point of a weapon."

**Proto-Germanic**: This connects to Proto-Germanic *\*uzdaz*, meaning "pointed upward," which also produced Old English *ord* ("point of a weapon, spear"), Dutch *oord* ("place"), and German *Ort* ("place").

**Indo-European Root**: The ultimate source is PIE *\*uzdho-*, which also gave rise to Lithuanian *us-nis* ("thistle").

**Semantic Shift**: Interestingly, "odd" developed its modern meaning of "strange, peculiar" only around 1580, from the notion of "the odd one out, unpaired one of three." Earlier (c. 1400), it carried the positive sense of "singular" meaning "renowned, rare, choice." The mathematical sense of constituting excess numbers dates to around 1300.
```


## [2026-09-07T20:21:36.621Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== ODD any case ==\"; grep -c 'ODD' AHD_watkins1985.txt; grep -o -E '.{120}ODD.{120}' AHD_watkins1985.txt | head -5; echo \"== ud- root ==\"; grep -o -E 'ud-\\. (Up|Out).{500}' AHD_watkins1985.txt | head -3",
 "description": "Check AHD Watkins for ODD and ud- root"
}
```


### [2026-09-07T20:21:36.708Z] TOOL RESULT

```
== ODD any case ==
8
dud-. To shake, deceive. Germanic root. 1. Norwegian dudra, to quiver, akin to: a. Middle English daderen, to tremble: DODDER!; b. Middle English doder, vine (< “that which quivers in the wind”): DODDER2. 2. Middle English doten, to be foolish
 protect, feed. Contracted from *pas-. 1. Suffixed form *pé-trom in Germanic *fodram in: a. Old English fédor, fodder: FODDER; b. Old French feurre, fodder: FORAGE; C. Old French forreure, trimming made from animal skin, fur (< “sheath, case, 
 SUCCULENT. [Pok. 1. seu- 912.] seut-. To seethe, boil. 1. Germanic *seuthan in Old English séothan, to boil: SEETHE, (SODDEN). 2. Germanic *suth- in: a. Middle Dutch sudde, sudse, marsh, swamp: sups; b. suffixed form *suth-l- in Middle High G
== ud- root ==
```


## [2026-09-07T20:21:47.048Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== zdho ==\"; grep -o -E '.{150}zdho.{250}' AHD_watkins1985.txt | head -5; echo \"== Old English ord ==\"; grep -o -E '.{200}(Old English ord|usnis).{200}' AHD_watkins1985.txt | head -5",
 "description": "Check AHD for ozdho root"
}
```


### [2026-09-07T20:21:47.665Z] TOOL RESULT

```
== zdho ==
== Old English ord ==
```


## [2026-09-07T20:21:54.783Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/uzdaz",
 "prompt": "Give the full etymology of Proto-Germanic *uzdaz, its PIE source, descendants (Old Norse oddr, oddi; Old English ord; German Ort), and any mention of a 'branch' root *ozdos."
}
```


## [2026-09-07T20:21:56.076Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D8%B2%D8%BA",
 "prompt": "Give the Persian entry for ازغ: meaning and etymology (Middle Persian azg, PIE root), if present."
}
```


### [2026-09-07T20:21:58.023Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-07T20:22:00.322Z] TOOL RESULT

```
# Etymology of Proto-Germanic *uzdaz

## PIE Source
The term possibly derives from Proto-Indo-European *úd-s ("up, off") plus *dʰeh₁- ("to set, put, place"). An alternative theory "connected to the root *wes- ('to prick')," linked to Albanian usht (thistle).

## Meaning
The reconstructed noun denotes a "sharp point" or "place."

## Key Descendants

**Old Norse branch:** oddr (Faroese oddur, Icelandic oddur, Norwegian odd, Swedish udd, Danish od)

**West Germanic branch:** 
- Old English ord → English "odd"
- German Ort
- Dutch oord
- Frisian variants (od, Oud, oerd)

## Note on *ozdos
The provided content contains **no mention** of a branch root *ozdos. The only related derived term listed is *uzdijaną.

The entry cites Kroonen's *Etymological Dictionary of Proto-Germanic* as its primary source for this reconstruction.
```


## [2026-09-07T20:22:09.184Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82ozdos",
 "prompt": "Give the reconstruction, gloss, etymology and full descendant list for this PIE 'branch' root, and note any mention of Greek oskhos, Middle Persian azg, or Persian azgh."
}
```


## [2026-09-07T20:22:10.983Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CF%8C%CF%83%CF%87%CE%BF%CF%82",
 "prompt": "Give the Ancient Greek entry ὄσχος: meaning and etymology, including any Iranian (Middle Persian azg) cognates."
}
```


### [2026-09-07T20:22:11.329Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-07T20:22:12.351Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-07T20:22:15.581Z] TOOL CALL #40: WebSearch

```json
{
 "query": "Proto-Indo-European *h₂ozdos \"branch\" Greek ozos Gothic asts Armenian ost wiktionary"
}
```


## [2026-09-07T20:22:17.027Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E1%BD%84%CF%83%CF%87%CE%B7",
 "prompt": "Ancient Greek ὄσχη / ὄσχος: meaning 'vine branch, shoot' and etymology. Any Iranian cognate?"
}
```


### [2026-09-07T20:22:22.578Z] TOOL RESULT

```
Web search results for query: "Proto-Indo-European *h₂ozdos "branch" Greek ozos Gothic asts Armenian ost wiktionary"

Links: [{"title":"ὄζος - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%E1%BD%84%CE%B6%CE%BF%CF%82"},{"title":"Reconstruction:Proto-Indo-European/h₃ósdos - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%83%C3%B3sdos"},{"title":"Proto-Indo-European mythology - Wikipedia","url":"https://en.wikipedia.org/wiki/Proto-Indo-European_mythology"},{"title":"Reconstruction:Proto-Indo-European/h₁óynos - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81%C3%B3ynos"},{"title":"Proto-Greek language","url":"https://en.wikipedia.org/wiki/Proto-Greek_language"},{"title":"Discovering Ancient Greek and Latin: 1.4 Indo-European | OpenLearn - Open University","url":"https://www.open.edu/openlearn/history-the-arts/discovering-ancient-greek-and-latin/content-section-1.4"},{"title":"Graeco-Albanian languages","url":"https://en.wikipedia.org/wiki/Graeco-Albanian_languages"},{"title":"Proto-Indo-European language","url":"https://en.wikipedia.org/wiki/Proto-Indo-European_language"},{"title":"Proto-Indo-European particles","url":"https://en.wikipedia.org/wiki/Proto-Indo-European_particles"},{"title":"Reconstruction:Proto-Indo-European/oḱtṓw - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/o%E1%B8%B1t%E1%B9%93w"}]

Based on the search results, I found detailed information about the Proto-Indo-European root you're looking for:

The Greek word ὄζος (ózos) comes from Proto-Hellenic *ózdos, which derives from Proto-Indo-European *h₃ósdos meaning "branch, twig". Note that the Wiktionary source shows the laryngeal as *h₃, not *h₂ as in your query.

This root is cognate with Old Armenian ոստ (ost, "branch; knot (of tree)") and Old English ōst ("tree knot").

The search results also provide additional language descendants: The Proto-Germanic descendant is *astaz, Proto-Armenian shows Old Armenian ոստ (ost), and there are Old Georgian cognates as well.

I should note that regarding Gothic *asts mentioned in your original query, while the search results discuss Proto-Germanic *astaz (which would be the ancestor of Gothic forms), the specific Gothic form wasn't explicitly listed in these results, though it would be a regular descendant of the Proto-Germanic root.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-07T20:22:23.180Z] TOOL RESULT

```
# Ancient Greek ὄσχη: Etymology and Iranian Cognates

Based on the Wiktionary entry provided, here's what we know about this word's origins:

## Etymology

The entry states that ὄσχη is "explained by Frisk as metaphorical use of ὄσχος (óskhos, 'vine-branch')." However, scholar Beekes suggests an alternative possibility: "the word may well be of Pre-Greek origin."

## Regarding Iranian Cognates

The source document contains **no information about Iranian language connections** to this Ancient Greek term. The etymology section only discusses two theories: either a metaphorical derivation from a Greek root meaning vine-branch, or a Pre-Greek substrate origin.

To investigate potential Iranian cognates, you would need to consult historical linguistic resources beyond what's presented in this Wiktionary entry—particularly comparative Indo-European or Iranian etymological dictionaries that might explore cross-linguistic connections for this anatomical term.
```


## [2026-09-07T20:22:36.248Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"--- head BQT_v1_pages ---\"; head -5 BQT_v1_pages.txt; echo \"--- page markers ---\"; grep -n -m5 'pdf page' BQT_v1_pages.txt; echo \"pages(ff)=\"; awk 'BEGIN{RS=\"\\f\"} END{print NR}' BQT_v1_pages.txt; echo \"--- v2 ---\"; grep -n -m5 'pdf page' BQT_v2_pages.txt; awk 'BEGIN{RS=\"\\f\"} END{print NR}' BQT_v2_pages.txt",
 "description": "Inspect BQT page files structure"
}
```


### [2026-09-07T20:22:37.643Z] TOOL RESULT

```
--- head BQT_v1_pages ---
۱ ۵ ۱! ۱
7 موم ۳ لام
م ۱ 0 و طق صفرررنیاعدریرماروی
۰ ۱ "۳
۳
--- page markers ---
pages(ff)=
777
--- v2 ---
683
```


## [2026-09-07T20:22:44.433Z] TOOL CALL #43: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:114 2>&1 | head -60",
 "description": "Fetch Borhan-e Qate page 114"
}
```


### [2026-09-07T20:22:45.924Z] TOOL RESULT

```
no scan of BQT covers printed page 114 (see 'scans' in refs_online.json)
```


## [2026-09-07T20:22:55.218Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nimport re\n# find leaves containing ازغ or اژغ\nfor i,l in enumerate(leaves):\n    if 'ازغ' in l or 'اژغ' in l:\n        # find printed page number: look for persian digits alone on a line\n        print('leaf',i, [x for x in re.findall(r'(?m)^\\s*([۰-۹]{2,4})\\s*$', l)][:4])\nEOF",
 "description": "Locate azgh leaves in BQT vol1"
}
```


### [2026-09-07T20:22:56.479Z] TOOL RESULT

```
leaf 46 []
leaf 248 []
leaf 252 []
leaf 273 []
leaf 279 []
leaf 326 []
leaf 328 []
leaf 454 []
leaf 476 []
leaf 533 []
leaf 595 []
leaf 685 ['۳۳']
leaf 701 []
leaf 752 []
leaf 770 []
```


## [2026-09-07T20:23:02.422Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in (247,248,252):\n    l=leaves[i]\n    print('==== leaf',i,'====')\n    print(l[:1800])\nEOF",
 "description": "Print BQT v1 leaves 247,248,252"
}
```


### [2026-09-07T20:23:03.871Z] TOOL RESULT

```
==== leaf 247 ====
ده
آ زر نگ - بفتح رأیم بوزن با درنگه .
بمعلی غم سخت و محنت صعب و رنج و هلا کت
باشد - وبمعنی خیارسبز هم پنظ آمده است ٩‏ .
گت یتح الت وسکون خی تقطمدار»
درختان دیگر ببرند و آنرا بعریی * جلمه »
خوانند ؟ .
دوعص
ادع بزای فارسی » پروزن و معنی
آزغ‌است که شاخهای‌درخت بربده‌باشد؟ - ولیف
خرما را فیث گوشد ۰
آز فنداك - بفتح‌فا وسکون نون ودال
اد بالف کشده و یکاف زده 4 قوی قرح را
گویشد . ی
]رز فندا لك « بازای‌فارسی»بروژن‌ومعنی
آزفندالك اس که قوی قرح باشد -
1۳ ۳
] ذ گن « بازای فارسی ساکن وکس
کاف فارسی شوت زده » دری باشد که آ ترا مانتد
پنجره ساخته باشند و از ععب آن وان نگاه
(۱) چب ۲ , چش : آکندن .
آژنگه
کرد . *
] ز هثل » بامیم بروزن پای‌بنده خداوند
حرص داز باشد یمنی حریص وصاحب خواهش »
چهنند بمعنی صاحب وخداوند است . #
| د هون بر وزن واژگون , آزما
و امتحان رااگوینب ۴ ۰
]زر ند - با زای فارسی بر وزن یایند ء
کلی باش که بر روی خشت به نکنند و خشت
دیگر بربالای آنگذارند ‏ وگل و لای‌ته حوض
و جوی را نیز کوبند - و کلابه را هم گفتهاند .
آجیده کردن باشد .
 یتع‎
! ز ثف ین » بروزن‌واخندسن, درمیان
]زر زگ ت‌ بفتح ال وسکون رابع‌وکاف
فارسی , چين و شکنجی را کوین دکه بر روی
و آندام مردم اند خواه از ری و خواه ازروی
بسیاراست ؛ یکی دو مثال که بعض فرهنگها برای آزرنگه با زاه میآورند عن‌بسش شواهد آنرنگه
است و اما معنی خیار سب زکه باين کلمه داده اند پی شك اشتباهی است که ظاهرا تخت صلحب
اداة الفشلاء را دست داده است و مثشاء اشتباه کلمةٌ بادرنگه بوده که برای تعبی وزن آنرنگ دد
سخه ای دیده و آرا معنی‌کلمة آذرنگ صو رکرده است . < لفت نامه 5
۴ ره : آزمایش وآزمودن » درذیل .
ه آزمایش پهلوی صلاوز202ه مرکب از 2 + ۳2 « تب رک ۰۸ صه
ما2۵ < اووالا ۲۳ > رك : آزمودن . ه آزعودی _ ارمتا 217702
م رکب از پیشوند 21 ( < 2ل1 که در پارسی دز» شده) و 118 بمعنی انداز هک فتن ؛ تجربه
کردن » آزما شکردن .
بفیه از صفحةٌ ۳۹
است و در بهلوی نیز 320( بممنی پیری آمده که در ثرهنگهای فارسی هم بمعنی پس
وفرتوت باد شده . فلم ولقب پدر رستم» «زال» و «زر» هر دو 
==== leaf 248 ====
رود 5 با زای هوژ بر وزن ساطور »
صاحب حرص و آز را کونند که حریص باشد .
این لفظ م رکب است حمجو گندور و رنجور -
و بممنی هوسناله هم گفته‌اند ؛ و بر وزن داد کر
آمده‌است که ساحب و خداوند حرص و شره
واز باشده چه آز بمعنی حرص است و وربمعنی
صاحب وخداوند . *
]دوش « بروزن‌آروغ؛ بمعنی پیراستن
باشد بعنی برمدن شاخهای ز.ادنی - و بعضی
ختقوای را کرت مرت رد و وفیره
بربده باشند ؟..
7و با زای فارسی بروزن و ععنی
آزوغ است که شاخهای بربد؟ درخت خرما رتاله
و غیره باشد ۴ - لیف خرمارا نیز گویند .
وی ۰
] ریا 4 س بازای فارسی بروزن تازبانه»
فرشی را کون دکه از خشت بخته و مشگههکرده
سح ر ۰
1 722 < بازای فارسی وبای حطی‌بروزن
تاریخ » , مطلق چرك را کویندعدوعاً و چراه کوشة
7 یدن س بازای فارسی» بروزن ومعنی
اول آزیدن باشد که خلانیدن سوزن و امثال آن
ت ۴ -و آجیده کردن را نز کوه‌ند خواه با
سوزن باشد و خواه بغیر سوزن -
آدير - بر وزن جاکیر ۰ بمعنی آزار
و رنج و محنت باشد .
یر - با زای فارسی بروزن جاگیر »
بععتی (۱) آماده و مهیاکردن باشد مطلفاً - و
تالاب و آبگیر واستشو را نیز گوبند - و بمعنی
غلبه و زبادنی ( ۲ ) - وبانگه وفرباد حم آهده
است - و بمعنی زبرا4 و حشیار و هوشمند حم
هست ۵ -وپرهیزکار را نی زکویند.
]زیر ال « بازای بی‌قطه بال فکشیده
بانگه و فرباد کرد است
مطلقاً اعم از آدمی و ستور .
۲ بر بان » بر وزن بازی چیدن »
بمعنی بانگه کردن و هوشیار و خبردار نمودن -
و مهیا و اماده ساختن باشد .
و بکاف زده » بممنی
دی خصوصاً و بسربی درعص» خوانند ۴ . آر بخ زب ٩۰۷‏ ۱۶
]ر هدن « با زای هوز بر وزن بازیدن حطی و غین قطهدار ۰ تنفر و نفرتی را کویند
بمعتی خلانیدن سوزن وامثال آن باشد - وبمعنی | که از اقوال و افعال کی در ظاهر و باطن بهم
رنگ کردن‌هم کفتماند ۴ - ویممیآزردن, آزاره رسد , #
(۱) چش : - بمعنی . (۲) چك : زیاده.
۱ -ر:آزوری. ۴ - ره:آژغ‌وازغ.
همواره پرآزخ است آن چش فزاکن
کوب یکه دوبوم آتجایر .خانه گرفته‌است
۶ لت نامه > ۴ رك : آجدن.
۰ ریغ* سح ره : : آریخ .
۶ صحف
بغیه در صفحهٌ ۳۹
==== leaf 252 ====
آسمار با میم بروزن شاخار , ورخت ]| کهکثانرا کویند و بعربی مجره خوانند .
وود 1 کرت و مرش ان ا: آ سهان‌ور بسمان - این مثل ات
آیما .۱۰ ۳ زااد ب درجایی کون که شخصی درب رآبر معفول‌جواب
| سهان " ه ممررفت وبعربی سما وفلك ۱
نادرست (۱) گومد .
خوانند» ومعنی ترکیبی آن آسیا مانند است . : ِ
بابار گردیین چه آسیا را آی یز کوشد ۴- سها 4 » بروزن‌آسنانه» سقف خانه را
ویام فرخته‌ایست که مو کل است بر ممات واو را کونند . 0
" عزرائیل خوانند - ونام روز بیست وهفتم باشد از آسمانی ر بان س یعنی زبان آسمانی
هر ماه شمسی و تدییر و مسالح روز مذ کور باو | که مراد از آن زبان ملاشکه باشد .
ملق رد دج ریت وم | هتفرن دشن منک
شمی‌را آسمان گوند ۴ وافداعلم . بغربب و خدعه باشد - و سرگشته و حیران را
سمان مت سس ون رشق یز گوبند .
ایجد .فك دهم را گوید و آن را نك انا آسموغ ۴ - بر وزن آبنوغ » دام
خوانند . دبوست از منابمان اهرمن که سخن چیتی رفتنه
انگیزی و دروغ گفتن و میان د مکس جنگه
(۱) چب ۲ , چش : جواب تا در مقایل .
- اوستا 358080 بمعنیسشکه « بارتولمه ۲۰۷ و ۲۲۰» رگ : آس . چون آسمان را
بان سنکی پنداشته اد از اين رو نام آن در اوستا و پارسی باستان نیز 2511120 میباشد که در
پهلوی و فارسی آسمان کویم « خرده اوستا ۹ ح | » پهلوی 257028 « منای ۲۹۸ *.
کیلکی 250020 , فریزندی 250100110, بر نی 2519110 نطنزی 251۳020 « . اس ۶۲۸5 :
2 0 , سنانی 25۳027 <4 .۲ ص ۱۸۰ وی 0 .۰ 2570210 ۰
بازغلامی 25۳000 , سریکلی 82511188 «گربرسن ص ۰*۷۲ تهرانی 2560008 .
۴ - این توجیه درست نیست. ۳ - آسمان در مزدینا مقدس است وچندبار با زمین
یکجا نام برده شده ( چنانکه در نشتر بشت بند ۸ ۰ مهربشت بند ٩۵‏ وغیره ) . بلر ها از زمين
و آسمان ؛ ایزدانی اراده شده که بنگهیانی سیهر و خالك کماسته شده‌اند : همه ساله زاشتاد واز
آسمسان نن‌وجانت باشادی وکاعتان ؟ (فردوسی بتقل جهاتگیری ) درستا؟۱ بنده ودر دوسپروز؛
کوچك و بزرک بندهای ۷۷ و ۲۸ هردو ابزد آسمان و زاعیاد (زمین) درردبف فرشتگان ماه
باد شده اند . نگهبانی روز یت و هفتم هر ماه با ایزد آسمان است . ابورسسان بیروئی دد
فهرست روز
```


## [2026-09-07T20:23:21.192Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in (273,279):\n    l=leaves[i]\n    print('==== leaf',i,'====')\n    print(l[:2200])\nEOF",
 "description": "Print BQT v1 leaves 273,279"
}
```


### [2026-09-07T20:23:22.474Z] TOOL RESULT

```
==== leaf 273 ====
۰میژ ۲ « بازای‌فارسی» بروژن ومعنی
آمیزاست که آمیختن دوچیز بازیاده بهم‌باشد . *
آهیژه " « بروزن پاکیزه » بمعنی
آميخته است ‏ ومباشرت وجاع رایز گوبند -
ویمعنی مزاح وطسعت هيآ مده‌است ۴ - ویسنعنی
خردم پیر و کهل و رش دو موبه یز هت .
هردم زش دوموبه و پیر و کپل باشد - وبمعنی
آمیخته هم هست - و مردم شاعو وموزون را نیز
گونند .
| هیزه هو » بامیم بروزن پاکیزه روه
مردم رش جو کندم و دو موبه را گویندوسربی
«کهل» خوانند ۵ 1
] هی - بسکون غین نقطه دار » بمعنی
(۷) چب ۲ . چش : نوالعقول .
۱ - رکه : آمیز.
کر دکرده ببی سخن ریزه
۴ رکه : آمیژه .
۵ - اکرشاه حرهفت کشوربود
آن
حقیت‌بودکه درمقابل مجاز است ۷ - وآعیختن
و آمیزش در چیز باشد باهم ۷ - و مباشرت
و مجامعت را نیز گوبند ۸ .
] میقه ود بفتح غین نفطه دار .
بمعنی آهيخته و آميزش - و مجامعت ومباشرت
ماشد .
آ هیقی - بک غین نقطه دار وسکون
تحتالی » بمعنی حقیقی باشد که در مقابل
مجازست*۹ .39
آن بر وزن جان . بمعنی وفت و
حنگام ٩۱‏ واشاره بچیزی دور باشد ازغیرذوی-
المقول (۱) حمجو این که اشاره بچیزی ترديك
است -٩۴‏ ونمك وچاشنی وحالتی و کیفیتی رانیز
گوبن که در حسن میباشد و بتقربر درنمی آبد
اسدی «لفت‌نامه».
نوش آحیغ 4 کوهرآعیغ وغیره. «لفب نامه».
۸ - چوآعیغ برنا شدآراسته
دساتر ۲۳۱ .
#- درطمات مر کب : زهرامی: ۰
۶۰ رکه : آمیغ و فرهنگه
ر یگاهان». « السسجم ۱۷۵ ۰ .
1 < دانشنامه ٩۹٩‏ »- خلطه , مماشرت .
==== leaf 279 ====
اه
۲ هنیا به (۱) - با بای ابجد و نون
و بای حطی وبای بيكك قطةٌ تحتانی بر وزن ۷ -
ات ادن بعتی جاااهوی امه که زوا از
گویند و مربی «تاب» خوانشد .
7 42 - بر وزن نافثه » بععنی آازیده
است که مطلن کشیده باشد اعم از قد کشیده و
شمشیر کنیده و امثال آن ٩‏ - و هارتهای
| هتخت ۲ - بکر ثالث و سکون خای
خن و ای افرشت » یمنی ب رکشید و بر آورد .
]خن ۴ » بروزن دانستن . بمعنی
" کشیدن باشد ۰طلقا اعم از هد کشیدن و شمشبر
از غلاف کشدن - و دست از چیزی کشیدن
و امتال انها ۴ .
باشد مطلقا ؟ .
]هر اهی * - با رای فرشت بر وزن
(۱) چب . چش : آحبیا ۱
رهنمای بیکیهاست .
آ هرمن * - بتتح رای قرئت و میم
بروزن لاف زدن» سمعنی و امن است کمرهنمای
بدیها باشد و بسکون رای فرشت حم کفته اند
که‌بروزنوا کردن باشه۷ . وبسن یکوینهآهرمن
شیطان است چنانکه (۲) بزدان فرشته است و
بضی گویند بزدان دم خداتمای کته آهرمن
نم‌شیطان و این اصح است : وتوبة مسگوشد
که خلی تمه علمت او ارنگی و بهع رسای
شر وفتنه و فاد اوست .
] هرن * - بر وزن باد زن » بععنی
آهرمن است که شبطان باشد .*
]هریهن * - بک رایع و قح میم .
بر وزن ماه ددن بمعنی آهرن است که شیطان
و رهنمای بدیها باشد .
هر یمه * فتح‌هيم » » بمعن ی آهردمن
ست که شیطان و رهنمای بدبها باشد ,3
همند ۸ - بنتح میم و سکون تون
۴ - مرکب از:2 (ییشوند) +-
و آهنجیدن «فاب. ۱ : ۸٩‏ ۶ :
زآهختن نیخ‌ها ازغلاف
وت 2
٩‏ خجسته بی دنام او زردهشت
۲ - رك : بزدان.
کناهکار » عاسی :
۱ چوجنی کسی با کس یکفتگوی
ز پولاد سندائی اننر شتاب
کفش سوختیگربدی آهمند
۴ ره : آهختن. رگ : اهر هررمین-
که آهرمن بدکنش‌را بکشت
دققی ۶ مزدسنا ۱۵۷: ۰۱۷۲ ۱۷۵ *.
ججیزی که سو کند بودی در اوی
کندی » ستی .آهسته کاری فونگف:
شه در صفحةٌ ۷۰
```


## [2026-09-07T20:23:36.953Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in (326,328):\n    print('==== leaf',i,'====')\n    print(leaves[i][:1800])\nEOF",
 "description": "Print BQT v1 leaves 326,328"
}
```


### [2026-09-07T20:23:38.278Z] TOOL RESULT

```
==== leaf 326 ====
از ذست ب رکرفتن
یت و بود گردانیدن باشد .
هوز بالف کشده , نان فطیر را گویند یمن بعنی نافی
که خمیر آن نرسیده باشد .
از دست دهرجستن - بستی از
خر افتادن است که مردن و از عالم رفتن باشد .
از دست رقتن - کناید از بخودی
و بی اختیاری و اضطراب کردن باشد .
ازدست شدن « بسسنی از دست‌رفتن
است که کنابه از بخودی و بی اختباری
و اضطراب کردن باشد .
از دست فز | - بتح فای سنس ,
بمعنی ازدست پزاست که نان فطیر باشد .
ادف - بکر اول و فتح ثالك وسکون
فا . میوهء‌ایت سرخ رنگ و صحراسی و آنرا
بعربی زعرور خوانند ؛ و بفتح اول هم گفته‌اند .
ار دمی بر وزن فمدمی . <سالوری
است غیر معلوم» وبا رای قرشت هم کفته اند .
ازدن » بقثم اول و ثانی و الث
وسکون لون؛ بمعنی رنگ» کردن باشد - وبمعنی
0
و واو 4 صمغ درطات ارجن 3 درخت بادام
را رز گفته‌اند ۳
ارذوی تادی - یی سصغ عریی.
چه ازدو صمغ و تازی عربی را گوبند ,
از ده ت فتح اول ودال ابجد و کسرثانی»
یسعتی رنگه کرده باشد .
۱ رد : آزرمیدخت ۰
ی ناس ۶ .
۵ ازه - (فتح اول) - : ازغ .
۷4
از راستی باشد که هیچ کبمی درآن نباشد .
از دق - با رای فرشت بر وزن ابلق ,
- و در
عربی رنگه کنود را گویند .
ازر گ اند بشه چکیدن ه کنابه
از دقت کردن در فکر و اندیشه باشد .
از رمیدخت » با دال و خای قطه "
دار بر وزن سحر میگفت » نام دخشی پرویزاست
که لشکر بدوبیعت کردند وششماه ملك راندا -
و نم شهری تبز هست که اوبنا کرده است .
ارر نگ بر وژن ید رن , خیار
پادرنگه را گوشد .
از ز بان جستن -کنابدازخطا وسهو
کردن در کفتگو باشد .
از سر با روان شدن» کنابه
از زود روان شدن و بتعجیل رفن باشد .
ازسر ذست « کنابه از گفتن مر قزر
وسختی باشد بیتأمل و فکر - وزود ساختن‌کاری
بی‌اتظار .
ارشکم افتادن - کنابه از مردن
واز عالم دفتن باشد.
از « تج اوز و سکون ثانی و غین
قطه دار . آنجه از شاخهای درخت برند
وییرایش دهند ۴ وآترا بعزبی جلمه گویند .
ارچ - بنتح اول و کون ثالی و کر
تالت و جیم فارسی سا کن » کیاهی اس ت که بر
درخت یجد و آنرا بعربی عشقه خوانند . #
از کات ه با اف فارسی بروزن بمدذات»
عردم بد دل و بد اندرون را گونند .
از کره درفتن 
==== leaf 328 ====
اراد
باشد ٩‏ - و کنابه از مردم شجاع و قهرآلود حم
هت - ورایت و سرعلم را نیز گوبند ۴ -
وپادشاه تال و ححاك ماراترا هم گفته‌اند ۴ .
ادها « با کاف‌معنی آخراژدهاست
که نحاك ماران باشد ۴ .
اژدهای فلك - اثارء بشدنین رأی
و ذنب است - و تلی‌را نیز گویندکه ازجلهة
چهل و حشت صورت فلك باشد ٩‏ .
ارم خح اول و سکون انی و غن
نقطه دار , شاخهابی را گویند که از درخت بریده
باشند و بعربی جلمه خوانند٩‏ .
ار کان با کاف‌بروزن دربان ؛ بمعتی
مردم کاهل و باطل و مهمل و بیکار باشد .
باگد شبکه دار که ازیس آن نگاه توان کرد .
۱
ظ
از گهی -باها پروزنک رکدن : بمعنی
از کهان است که کاهل و باطل و مهمل وبیکار
بش
۸ ۰
آز لد - بفتح اول و انی و سکون نون
و دال ایجد . کلی باشد که بر روی خشت بهن
کنند و خشتی دیگر بربالای آن نهند - و گل
و لای ته حوض را نیز گفته اند .
اژ نگ -بر یزن پلنگ , چين پیشانی
وروی و اندام باشد.
اه « بنتح اول و انی , آهك را گویند
و بعربی کلس و نوره خوانند .
‌ و ۲ ۳
ار هان ‏ با ها بر وزن دربان؛ هردم
کاهل و باطل و مهمل و بیکار باشد .
۱
از هی - بروزن الکن ؛ بمعتی اژهان
است که مردم بکار و مهمل و باطل باشد .
۳
از کهان باها بروزن پهلوان ؛. بمنی از بر ع« بر وزن وزیر » بمعنی هوشمند
از کان است که مردم کاهل و باطل و مهمل | و زبرك و عاقل باشد - و مردم پرهیزکار را نیز
و بیکلر باشد . گویند
بیان سیز دهم
اتاات ی وزن وسام اوه بو وغان فرد
باشد , وآن سبب خواب‌باخمار باکاهلی بپجرسد
و بممتی شیه و تظیر و مانند هم آمده است .
اییادون - بارای قرشت بس وزن
فلاطون ؛ بخ کیاهی است کمغلاف تخم آن‌مانند
غلاف بذرالبنج است - و بعض یگوبند بیخ ستبل
حمعا؛ مار گز تده
کنادء دهان اژدهای علم
۳ - مضغف اژی‌دهاك , مُحالك :
۴ مختف اژی‌دهاك , رك: اژدها,
مفرجام هم زو بامث رها .
دمزدبنا ۳۹ ح ۶ *.
۵ - 1(<۲2800. ۱ - ر۵: ازغ
```


## [2026-09-07T20:24:01.024Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i,l in enumerate(leaves):\n    if re.search(r'(?m)^\\s*ازم\\b', l) or 'ازم ' in l:\n        seg=[m for m in re.finditer('ازم',l)]\n        print('leaf',i,'|', l[max(0,seg[0].start()-100):seg[0].start()+200].replace('\\n',' '))\nEOF",
 "description": "Search BQT v1 for azm"
}
```


### [2026-09-07T20:24:02.323Z] TOOL RESULT

```
leaf 20 |  شرح وتفسیر و توضیح و بیان‌است۰ اگر اصلا یاد کردن اینگو نه لغات‌هزوارش(-< آرامی) درفررهنگهای فارسی لازم باشد » نگفته پیداس ت که باید ریشه و" بن [نها را از همان زبان آرامی یا زبانپای دیگر سامی چون سریانی و عبری و بالاتر از آنها در زبانبای بابلی و آشوری وا کدی بدست آورد . معادل بياری از آنپا در زبان ع
leaf 27 | بانهای ایرانی بلکه آنرا فقط بر مردمی اطلاق میکردند که مر کز آنان شپر سمر قند بوده است ا . در اینجا لازم است بانار استاد فریمان ۴ عضو وابتهٌ فرهنکستان شوروی وفرهنگستان ايران راجم بانتشار وضیر ونشریح‌اسناد معروفی که از کوه «مورغ» تاجیکتان درسال ۲ هم بدست آمده ودرجپان دانش بعنو ان حادنه‌ای بس بزر گ تلق
leaf 94 | گها که‌موٌ لفین این‌دو کتاب در دست داشته| ند بح؟ م < کلالصید فی جوف | لفر 4۱ تن‌زده وتکرار اسامی‌رالازم ندانسته او علاو* براين کتابپا دوماخذ دیکر داشته که ظاهرآ در دستر س جپانگیری وسروری‌نوده است. و آن‌دو عبارت است از : سصرمه سليمانی ر صحاح الادو به. این کتاب بنايگفتة ریوتاً لیف تقی‌اوحدی است ٩‏ که 
leaf 136 | شوشو ناقص‌مینما ید. شرح و توضیح نا گریز در حاشیه توضیحات بیار با ذکر ماآخذ لفات افزوده شده و معانی لازم که در متن نیامده نیز درحاشیه اصافه شده است. 70 ریشه‌های اوستابی ویهلوی وسانسکرت و دیگر لفات زبانهای باستانی و لیجههای ایرانی‌را ازمنابم میم با کر ماأخذ تفل کرده؛ واقات گیلکی ودزفولی وبرخی واژه های
leaf 138 | مقدمه صد وسی و تثری‌تا لیف کند ده‌ها سال تتبم وتحقیق واستغراجلغات ازمتون نظم و نثر فارسی که درمدت هز ار سال نوشته شده‌اند » لازم است و این کاریست که علامهٌ مماصر علی | کبر دهخدادر مدت متجاو زاز چپل سال‌بدان مشفول بوده‌|ند و تتيجةٌ مجاهدهٌ ایشان در اینمدت طولانی < لف
leaf 174 | است بر چند لغت که اولآ نها ضاد نقطهوار باشد. فتار شانز دهم - در حرف طای حطی با حروف تپجی ممتئی بر دوازم الاو ال ایا که ان ات بت ات کین اج ظای نقطه دار باشد . "فتار هفدهم - در حرف عین بی نقطه باحروف تهجی هبتنی‌بر نوزده بدان . "#فتار هحد‌هم- درغین نقطه دار باحروف تهجی‌مبتنی بر هفده‌بیاان. "فتار نوردهم
leaf 188 | یز و ابیداد شود ؛ همان معنی «علوم گردد و وصل و حذف انها دسنتب شروزت عری بود والا در محاورات احتراز لازم است و الفی که در مبان کنات بود بر پنج نوع است : اول الفی باشد که در ماقمل سفن آخر اضال در | ورند وان دو قسم است : یکی مجهت دعای نك و بد باشد همجو «دشمنت بمبراد» و « خدانگاهدار تو بواد » ودیگر "آنک
leaf 198 |  خم۱ : صلمت! ۶ او دوست دائتنی است» و « این کار کردنی‌است » بعنی او لابق آست که دوست دارند و این کر لازم‌است کردن» وخوردن را از رات خوردن ی گویند کهلابق خوردن باشد» وبودنی جزی رآ کوشد که بودن‌آن لازم باشد . » «المعجم ص ۰.۱۸۸ (۲) « حرف تکرم و آن یائی است ملثه که‌دراواخز اسماء عللاعت اکره باشدچناناك «ا
leaf 269 | ماند اعم ازیكك وسوخشاه و تر » چون آب و خالك و خون واك و مش و زهر وقیر دخوی وپلیدی و جزآن , واین ضل لازم ومتمدی آبد : حرآنگ هکه توشنه کیتی بخون بالودی این خنجرآبگون فردوسی «لفت‌طمه». 4 آلوه رد4 : آله. 0 آلیز دی و آلیزدی - جفته افکندن» جتتاگ‌اداختن : نش چون مب رکشت یستیزد ‏ نوسن‌آما بهرسو آلیزد . سراچ
leaf 312 | منی آتش گرفته !) « روزشماری ۱۹-۸ . ۷ رك : روزشماری ۷٩‏ . 8۵ اردو - مجموع میاهیان , مجموعةٌ فشون و لوازم او - لشکرگاه < کاشفری ج ۱ ص۱۱۲ » - نام زبان مردم پا کستان که ممزوجی است از فارسی وخربی و هندی و ترکی . ره : داثرةالمعارف اسلام ولفت‌نامه .
leaf 450 | 25021 «منای۲:۲۹*. د بایستن - در پهلوی 202228420 «منای ۲۹ : ۲» *«اونوالا۳۲۴» و 0هال(22د. «ی رکه ۲۸۲ لازم بودن. واجب بودن» ضرور بودن.
leaf 644 | . در کرد بان بشت مسمعنی جامه‌ای که درزیر زره دوشند» آمده؛ در لگ د4 وندید اد بند ٩‏ ینام جزواساحه ولوازم يك‌مرد جنگی بشمار آمده, بجزاین معانی دراوستا وپهاوی پنام عبارت‌است از دو قطعه ارچ سفید از جنس پتبه که بروی دهان آویخته با دو نوار پیشت سر کره میززنشد . زرنستیان ایران آن دا هروبند» لمتد. این برد؛ 
leaf 695 | و سکون واو وکاف » طبقی باش که بقالان اجناس‌ونانبابان نان در آن نیند ۵ و نام قلعه ای عم هست ور کتار قازم که حضرت رمالت صلوات ال علیه از کنارکرفتد؟ . باه یه - بفتح اول وانی وظهور حای هوز, سل سا بر ان ایم شدماست - و گوشت ت فرم و نازكك را لین 9 نبهر ه - با رای فرشت‌بر وزن طبقحه» قبیازه ٩‏ - بروزن‌خسیازه
leaf 751 | رباست» باربود تنگن‌باب. «خافانی شروالی 44*. ۵ - رك: تتندم . ۱ ۱ - شود در پناعت چو سد سکندر کش خانه سازم ز نار تشنشو . محزی یشابوری ورك : لفت‌فری ۱۷ ۶ ۷ -اسم فاعلاز: تنیدن: ۸ - ظ.از تر کیب «ننومند» (ه.م) این‌ممنی‌ساخثه‌شده. ٩‏ _ ر۵: لك۱: ۰.۳۲۰ ۷ رکه : تنیدن. در قرآن (سورء۱۱. آبه 4۲ وسور؛ ۲۲۳ مذ۲۷) تل
```


## [2026-09-07T20:24:02.393Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i,l in enumerate(leaves):\n    if 'زهدان' in l or 'زهاب' in l:\n        print('leaf',i, '|', ('زهدان' in l), ('زهاب' in l))\nEOF",
 "description": "Find zehdan/zahab in BQT vol2"
}
```


### [2026-09-07T20:24:03.708Z] TOOL RESULT

```
leaf 25 | False True
leaf 278 | True False
leaf 424 | False True
leaf 430 | False True
leaf 457 | True False
leaf 469 | False True
leaf 508 | True False
leaf 510 | False True
leaf 660 | True False
```


## [2026-09-07T20:24:16.804Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; timeout 900 python3 tools/ref_page.py BQT:1049 2>&1 | head -80",
 "description": "Fetch Borhan page 1049"
}
```


### [2026-09-07T20:24:18.255Z] TOOL RESULT

```
no scan of BQT covers printed page 1049 (see 'scans' in refs_online.json)
```


## [2026-09-07T20:24:22.200Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in (457,508):\n    print('==== leaf',i,'====')\n    print(leaves[i][:2000])\nEOF",
 "description": "Print BQT v2 leaves 457,508"
}
```


### [2026-09-07T20:24:23.488Z] TOOL RESULT

```
==== leaf 457 ====
     ‫اززتشت‬                                                                                                               ‫‪-‬‬
                                                                                                                          ‫ی‬


‫باشد اعم‬      ‫به اسزخن‬
                     ‫نا‪-‬‬
                       ‫راد دکهن‬                             ‫‪۹‬‬               ‫‪۵‬‬
                                                       ‫ر ادسم = بفتح شین فرشت بر وزن‬
                                                                                       ‫‪۳‬‬     ‫‪۹۳‬‬                ‫رده‬



                 ‫از نك وید ‪e .‬‏‬                        ‫یاب است وبسی گویندام‬
                                                                          ‫سدر‬
                                                                            ‫ارخفمر‪.‬ناامپ‬
                                                                                       ‫چا‬
 ‫ناههبه از هردر‬
              ‫رادۀ شش دکور‬                                              ‫اچفدراسیاب است که پدرپدر باشد ‪.‬‬
                           ‫حهان واز مخلوفات است ‪.‬‬      ‫وزن لاجورد ؛‬
                                                                  ‫ردم‬
                                                                    ‫بم‬‫راذمر د ‪ = ۴‬با‬
 ‫راد هر یح = کنابه از آهن ات‬                           ‫آزاد مرد است که جوان مرد و کریم‬                                       ‫مخفف‬
 ‫که ازان سیخ ومیخ وزنجیر وامثال آن‌سازند‪.‬‬                                                   ‫باشد ‪.٩‬‏‬           ‫همت‬        ‫صاحب‬
                                                                                                                             ‫و‬
 ‫داد س بروزن لار‪ .‬بمعنی مکان روبیدن‬                    ‫رادو بو ك ‏ بابای ابجدبروزن تارویود‪.‬‬
 ‫باشد همچو گلز ار ولاله‌زار وغله زاروعلف زار ‪-‬‬         ‫اسیاب‬           ‫وئمام سرمابه و‬        ‫تست‬       ‫و‬       ‫کنابه از هت‬
‫کے‬       ‫و نمعتی البوهی و ب
==== leaf 508 ====
‫—‬        ‫‪4 6٩‬‬
                                                                                                               ‫زو‬
‫دیگر وعربان کربه خوانند‪.‬وبلفت زندویازنه(‪)۱‬‬                                    ‫رزبون وحقیر جثه راکونند ‪.‬‬
                               ‫لسر همین معنی دارد‬
                                                           ‫» بمعنی‬     ‫دننگ‬
                                                                          ‫روز‬
                                                                            ‫رو نګ ‪١‬‏ بخ‬
‫‪-‬ا نانی »جهووسکون‌های‬
                    ‫روه‌هنك ب‬                                 ‫زوتزك است که مردم کوزیشت وحفیر باشد‪.‬‬
 ‫کشت‬
   ‫هوشمند »> درخت و‬              ‫بر وزن‬      ‫هوز )‪(۱‬‬        ‫زنوگل ؟ ‏ با کاف فارسی ولاءبروزن‬
‫وزراعت بالیده پرزور باشد؛ وبفتح های هوز هم‬                 ‫که مردم کوزیشت‬         ‫فلندر ‪ ,‬بمعنی زویگه است‬
                                           ‫آهده است‪.‬‬                                                   ‫باشد‪.‬‬   ‫وحقر‬



‫روبج ‪ ۴۰‬بنتم اول بر وزن حویج ‪,‬‬                             ‫پروزن تونی ‪ ۰‬نی زائو‬               ‫درو لی ‪۳‬‬
          ‫رودهای پراز گوشت و پبه کآنده باشد ‪.‬‬


                                                  ‫بیان هفدهم‬
                 ‫در زای نقطه دار با هامشتمل بر سی وهفت لفت و کنات‬

‫است ‪ -‬وچلهٌ کمان ‪ - ۷‬و ابرشم ‪ -‬ورود‪‌:‬تابیده‬                   ‫ن»ی‬
                                                                ‫علی‬
                                                                  ‫م ثا‬
                                                                     ‫بون‬
                                                                       ‫رهه بکر اول و سک‬
‫را ليز کوبند ‪ - ۷‬کونارة هرچیزهم‌هست همچو‬                   ‫باداش ندکی است ‪ -‬و کلمه‌ای باشد که در محل‬
‫آن ‪- ۸‬‬           ‫ال‬
                  ‫تفه‬
                    ‫مه ص‬
                       ‫اوز‬
                         ‫ووض‬
                           ‫ز
```


## [2026-09-07T20:24:33.077Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in (508,509,510):\n    print('==== leaf',i,'====')\n    print(leaves[i][:4000])\nEOF",
 "description": "Print BQT v2 leaves 508-510 fully"
}
```


### [2026-09-07T20:24:34.436Z] TOOL RESULT

```
==== leaf 508 ====
‫—‬        ‫‪4 6٩‬‬
                                                                                                               ‫زو‬
‫دیگر وعربان کربه خوانند‪.‬وبلفت زندویازنه(‪)۱‬‬                                    ‫رزبون وحقیر جثه راکونند ‪.‬‬
                               ‫لسر همین معنی دارد‬
                                                           ‫» بمعنی‬     ‫دننگ‬
                                                                          ‫روز‬
                                                                            ‫رو نګ ‪١‬‏ بخ‬
‫‪-‬ا نانی »جهووسکون‌های‬
                    ‫روه‌هنك ب‬                                 ‫زوتزك است که مردم کوزیشت وحفیر باشد‪.‬‬
 ‫کشت‬
   ‫هوشمند »> درخت و‬              ‫بر وزن‬      ‫هوز )‪(۱‬‬        ‫زنوگل ؟ ‏ با کاف فارسی ولاءبروزن‬
‫وزراعت بالیده پرزور باشد؛ وبفتح های هوز هم‬                 ‫که مردم کوزیشت‬         ‫فلندر ‪ ,‬بمعنی زویگه است‬
                                           ‫آهده است‪.‬‬                                                   ‫باشد‪.‬‬   ‫وحقر‬



‫روبج ‪ ۴۰‬بنتم اول بر وزن حویج ‪,‬‬                             ‫پروزن تونی ‪ ۰‬نی زائو‬               ‫درو لی ‪۳‬‬
          ‫رودهای پراز گوشت و پبه کآنده باشد ‪.‬‬


                                                  ‫بیان هفدهم‬
                 ‫در زای نقطه دار با هامشتمل بر سی وهفت لفت و کنات‬

‫است ‪ -‬وچلهٌ کمان ‪ - ۷‬و ابرشم ‪ -‬ورود‪‌:‬تابیده‬                   ‫ن»ی‬
                                                                ‫علی‬
                                                                  ‫م ثا‬
                                                                     ‫بون‬
                                                                       ‫رهه بکر اول و سک‬
‫را ليز کوبند ‪ - ۷‬کونارة هرچیزهم‌هست همچو‬                   ‫باداش ندکی است ‪ -‬و کلمه‌ای باشد که در محل‬
‫آن ‪- ۸‬‬           ‫ال‬
                  ‫تفه‬
                    ‫مه ص‬
                       ‫اوز‬
                         ‫ووض‬
                           ‫زگرهببان و زه ح‬
                                                            ‫تصین گوبند حمچو آفرین وباركالة ® ‪-‬وبمعنی‬
‫و بفتح اول وظهور ثانی‪ .‬مکان جوشیدن و بر‬                     ‫خوب وخوش هم هت ‪ -‬وزاییدنآ دمی‌وحیوانات‬
   ‫اتشد‪.‬‬  ‫‌ی»بآل‬
               ‫لال‬
                 ‫سی‌ت‬
                    ‫اخفا‬
                       ‫نولو‬
                          ‫آمدن آب ‪-‬ریفتح ت ا‬                ‫دیگر باشد‪٩‬‏ ؛ و باينمعنی بفتح‌اول همآمده‬
‫رهاب = بفتح اول بر وزن شهاب ‪۰‬‬                              ‫‪-‬به‌عنی نطفه وبجه و فرزند همگفته‌اند‬
                                                                                              ‫است و‬
‫تراوبدن آب باشد اکنزار رودخانه وچشمه‌ونالاب‬                 ‫ولپذا فرزند را زمزاد و رحم و بچمدانرا زهدان‬
 ‫‪-‬وضم چشمه را گیوزیند‬
                    ‫وامثال آن ‪٩‬‏ م‬                         ‫شگوته ‪٩‬‏ ؛ و باین معنی بفتح اول همآمده‬

                                ‫ها ‪.‬‬      ‫وكس‪:‬ک‪-‬ون‬
                                                 ‫(‪ )۷‬چ‬                  ‫(‪ )۱‬چك ‪:‬ژند ویاژند ‪.‬‬
                         ‫‪ - ۴‬رك‪ :‬زونگه » زوترك ‪.‬‬              ‫‪ - ۱‬رکه ‪ :‬زودگل ‪ .‬زور که ‪.‬‬
    ‫بممنی زالو » چنالکه در سنگری ‪« 60112‬ك ‪ ۲ .‬ص ‪.» ۹۸۱‬طبری‬                          ‫‪ - ۴‬لهجه ات‬

                           ‫؟ ‏ رك ‪ :‬زواج م رونج ‪۰‬‬                 ‫‪« 1۷‬ساب طبری ‪ › 4۰4‬و رك ‪ :‬زالو ‪.‬‬
                 ‫زه ‪.‬‬   ‫احسن ماك کفت‬      ‫فلك گت‬             ‫ده‬    ‫و قدرگفت‬   ‫کیر‬   ‫قضا کفت‬        ‫_‬    ‫®‬

    ‫‪.‬‬    ‫‪۰۵۹٩‬‏‬   ‫«شاهنامه بخ ج ‪ 4‬ص‬

        ‫‪ ۷‬اوسا ‪( 32۷1 ۳‬وتر کمان ‪ ۰‬رکے) ‪ ¢‬هندی‌باستان_‪[8/9-‬؛‬                   ‫‪.‬‬     ‫دن‬
                                                                                     ‫ی‪:‬‬‫زهرك‬
                                                                                          ‫‪۱‬‬
        ‫بازد از (رسمان»نج)‬       ‫کردی ‪( 1012‬زهکمان) ‪.‬اففانی ‪ : 202‬بلوچی ‪8‬ز «اسشق ‪۷۷۹6۰‬‬
                   
==== leaf 509 ====
  ‫زحراوی‬                                                                                               ‫پات‬
 ‫زهدآن * ‪ -‬بچهدان و قرارکله نطنه‬
                            ‫باشد وبعربی رگحومیند‪.‬‬            ‫باشد وخواه شکاف سنگه ‪ -۱‬و آیی که قرش‬
                                                             ‫یبدا لباشد ‪ - ۴‬و چشمه ای که عرکز اابتد‬
 ‫رهدان نهادن د کنابه از ملچز‬
 ‫شدن درجنکه ومحث رمقرشدن واعتراف لمودن‬                   ‫ریاول لیز‬
                                                                 ‫ک مسعت‬
                                                                      ‫پوبوسته روان باشد ؛ و ببان‬
                                                                                                     ‫آمده أست ‪.‬‬
                ‫برسستی و کم فهمی خود ‪.‬‬
 ‫هد بده = کنابه ازشوخ چشم و شوخ‬                              ‫ازار »‬    ‫رهار ت نکن اول بر وزن‬
                                    ‫دیده وخبره باشد‪.‬‬              ‫ور‬
                                                                   ‫ذجک‬
                                                                     ‫فر‬        ‫مهوضم‬
                                                                                   ‫ک‬         ‫شرمگاه رگاونی‬
                                                                                                   ‫باشد ‪. ۴‬‬
 ‫ر هر = بر وزن فهر ‪ ۰‬حعروفتوسربی‬
   ‫شصهم‪-‬وقهر‬
           ‫خن‬‫وعنی‬
                ‫ض‪-‬بوبم‬
                     ‫ح‪۷‬‬‫نبند‬
                          ‫سوم کو‬                                  ‫زهار » بنتح اول بروزن نمبازا»نگ‬
                                      ‫لیزآمده است ‪.‬‬                                   ‫‪.‬‬   ‫وفرباد وامره را گویند‬




 ‫ز هر آب س بفتح اول بروزن‌زردآب»‬                             ‫رهاره = یکر هردوزای شطه‌دار(‪)۱‬‬
 ‫آبیکه بضی از فواکهولباتات را درآن‌خسانند‬                    ‫ازبی تسین‬     ‫و طهورهر درو های حور )‪: (1‬تمن‬

                                                                                                           ‫باشد ‪. ۴‬‬
‫تا تلخی وشوری که داشته باشد ببرد ‪ -‬و آمی‌را‬
‫لکیوزیند کهبدانپنیر بندند بمنی مابهای که‬                     ‫از‬       ‫عی‬
                                                                       ‫ود »‬
                                                                          ‫ن بن‬
                                                                             ‫ره بنك = بروزن دل‬
                                ‫‪.‬‬     ‫ند‬
                                       ‫کیی‬
                                         ‫شیر را ش‬                                     ‫گردن مدد باشف‪.‬‬

 ‫رراوی ‪ -‬بروزن یضاوی» فلم یکی‬
                            ‫ه‬                             ‫از شیرازه بستن‬         ‫به‬
                                                                                  ‫ا‪-‬‬‫ندن‬
                                                                                      ‫کرر‬
                                                                                        ‫زه ب‬
                                      ‫از اطباست ‪. ۸‬‬                                                          ‫باشد ‪.‬‬


                                               ‫(‪ )۲‬چك ‪ :‬ها ‪.‬‬              ‫(‪ )۱‬چك ‪ - :‬قطه دار ‪.‬‬

                                                                                     ‫‪ ۱‬رك ‪ :‬زهشس‬
               ‫زه‌آبی بدون آندرون سهمگن‪.‬‬                               ‫‪ - ۴‬سوی رود بکااروالیگشن‬
       ‫دلخت فرص ‪٤‬‏‪.¥‬‬    ‫ابوشکوربلخی‪.‬‬


                                                 ‫بلگد ناف وزهارهمه (انگور) از من ربد‬
   ‫‪.‬‬      ‫‪۱‬‬   ‫دامغالی‬    ‫«مسوچهری‬       ‫بردش غشبی‪.‬‬     ‫اندرشده‬        ‫که از اشان س‬

   ‫شهنشاهعالم زحازه گرفت‪.‬‬           ‫بشادی مکی‌الجمن‌برشگفت‬             ‫‪( ۱‬واسطه) ‪ +‬زه‪:‬‬      ‫‪ ۴‬از‪:‬زە‬

       ‫«لخت فرص ‪۹*۵‬‬     ‫فردوسی‌طوسی‪.‬‬


           ‫‪ - ۱‬درزبان کنوبی«زه زدن»‪.‬‬               ‫_ از ‪ :‬زه (ه‪.‬م‪٣+ ).‬‏ دان (بوددمان) ‪.‬‬
   ‫‪ -
==== leaf 510 ====
  ‫‪— ۱‬‬   ‫‪4‬‬    ‫س‬
                                                                                                                    ‫زحرنار‬
‫رهرة میق = کنابه از قطرات باران‬                                     ‫هر باد = بفتح اول وسکون‌الیوثاكت‬
                                                   ‫است ‪.‬‬           ‫و بای ایجد (‪ )۱‬بالف کشیده وبدال زده »یمعتی‬
                                                                   ‫بزاهدر است ‪٩‬‏ ‪ ۰‬و آن مرضی باشد که بعربی‬
 ‫و واو بالف کشیده » خوش خوان و خوش‌الحان‬                                                              ‫خناق گوبندش ‪.‬‬
                                           ‫‪.‬‬     ‫را گوینه‬          ‫ر هر حند = خنده‌ای رگاویند که از‬
 ‫رهز اك * ‪ .‬بروزن بهزاد‪ .‬به‌عنی نسل‬                                                   ‫روی قهر وعضب وخعالت کنند‪.‬‬

                                           ‫وفرزند باشد ‪.‬‬           ‫ز هر خود بکسی ر بختن ‪ -‬کنابه‬
 ‫مگمن اول و ثانی وسکون‬        ‫=‬
                                                                    ‫قهروغضب خودرا تمام‌صرف‬           ‫کتسکه‬
                                                                                                     ‫ی‬   ‫از امن اس‬
 ‫ززههواب و چشمه‬                            ‫شین نقطه‌دار ‪.‬‬
 ‫مدن آب از چشمهباشد‬
                  ‫ودءوضع جوشیدن وآبر‬                               ‫رهر دادو ‏ زهر معلوم است » با‬
                        ‫‪.‬‬   ‫هم هت‬          ‫ولسسن‬         ‫وصفت‬      ‫دال ابجد بالف کشیده و رای قرشت بواو‬
 ‫دم وفقس ر‬       ‫هشت ‪ -‬بروزن بهشت ‪.‬‬
                                  ‫ر‬                                 ‫فاد زهر‬     ‫ومریی‬
                                                                                    ‫رسیده ‏‪ ١‬پازهر را گونند ‪:‬‬
                                                         ‫کو‬
                                                                                                                      ‫خواندد‬

‫رهك ‪ = ۲‬بفتح اول‌وسکون‌نانیو کاف؛‬                                  ‫رهر کر دن ‪ -‬کنابه از تلخ کردن‬
‫شیر زنان وشیر حیوانات نوزابیده باشد و آهرا‬                                                    ‫عیش است‬
 ‫آغوز وفله بگیوزبند وعربان لباء خوانند بکسر‬                         ‫رهر گا = یکرکاف فارسی ‪ ۰‬گیاهی‬
‫کشیده ‪ -‬و در عربی‬           ‫لام و بای ابجد بالف‬                     ‫ت که هر کس اندکی از آن بخورد فی‌الحال‬
 ‫جستن باد سخت باشد ‪ ۰ ۸‬وبکر اول‌هم‌درست‬                                                                        ‫«لاگ گردد ‪.‬‬
                                                     ‫‪.‬‬    ‫است‬
                                                                    ‫ر هر مهر ه = مهره‌ای باشد که بدان‬
 ‫که‬         ‫آلس»ت‬
                ‫‪-‬کر ار‬
                     ‫رهکو نی ‪,‬‬                                                        ‫دفع زهر افعی وغیزه کنند‬
 ‫پشت بای خودرا بضرب وزورهرچه تمام "ر‬                                ‫بفتح اول بروزن بهره؛پوستی‬         ‫زرهره =‬
                        ‫‪.‬‬   ‫رنف‬                ‫ا‬
                                               ‫‪۰‬‬
                                                                   ‫آدمی و حدوانات دیگر‬            ‫ناد پرآب که ‪3‬‬

 ‫فص وف‬       ‫= بروزن د لک‬         ‫‏‪٩‬‬       ‫زهگر‬                     ‫چسیده امت ‪ - ۴‬و کنابه از دلبری و شداعت‬
 ‫انت‪ :‬وآن انگشترمانندی باشف ازشاخ‌واستخوان‬                           ‫بود ‪ -‬وبمعنی شکوفه عربی است ‪ -‬و چامول‬
 ‫و کنابه‌ازفرح‬    ‫وغره که در انگشت ابهام کنند ت‬                        ‫ستاره امت معروف که آ را زاهد خواند ‪۴‬‬
                                  ‫‪. ۶۲‬‬         ‫زنان هم هت‬
                                                                    ‫زهرة تست بفتح‌اول‪ ,‬کنایه آازروشنی‬
 ‫نم اول وسکون ثانی و هیم '‬             ‫=‬       ‫رھم‬                                                                  ‫شب باشد‪.‬‬
                                                                                                ‫(‪ )۱‬چك ‪- :‬‬
   ‫‪ 8‬طایفةٌحکمامتفق شدند که‌مر
```


## [2026-09-07T20:25:02.337Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== PHD zah ==\"; grep -n -o -E 'zah[a-zāēīū-]*[^,;]{0,60}' PHD.txt | head -20; echo; echo \"== PHD zād/zāy ==\"; grep -n -o -E '(zādan|zāyēn|zahag|zahāb)[^.]{0,60}' PHD.txt | head -10; echo \"== NYB zah ==\"; grep -n -E 'zahāb|zahag|zah\\b' NYB_vol2_glossary.txt | head -10",
 "description": "Grep MacKenzie/Nyberg for zah"
}
```


## [2026-09-07T20:25:03.170Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; timeout 900 python3 tools/ref_page.py IRN:108 2>&1 | tail -60",
 "description": "Fetch Iranvij page 108"
}
```


### [2026-09-07T20:25:04.219Z] TOOL RESULT

```
== PHD zah ==
214:zah [Iz h == Av. arazahi-] the eastern continent of the earth. 
382:zahr] astr. the Dragon. ~ dumb: the descending node of the moon.
538:zahr [p’tzhl | N pa(d)zahr] bezoar
673:zahā [zh?(k')] depth. zahabag [zAh'pk! | N zaháb] spring
673:zahag [zhk'
673:zah) child
673:zahagómand [zhk'wmnd] pregnant
673:zahār [2/7 | N ~] womb. *zahih [zhyh] = zahā
673:zahr [zh] | M zhr
673:zahrag [z()Alk! | N ~a] bile
803:zahr.
992:zahr.
995:zahrag.
1223:zahag.
1561:zaha
1561:zahih
2142:zahagómand
2967:zahag
3165:zahr
3206:zahag- отапа.

== PHD zād/zāy ==
673:zahag [zhk', (z^ hk!) | М zhg, N zah) child, offspring
673:zahagómand [zhk'wmnd] pregnant, gravid
947:zādan,
1048:zādan
1223:zahag
2142:zahagómand; v
2967:zahag; (daevic) hunušak,
3206:zahag- отапа
3748:zahābag
5074:zādan! 1-2zrëh zarrën | zargónih - zargon zarigomand zarig zarr(
== NYB zah ==
663:Arzah [lzh, ?lzh] the name of the easternmost continent of the universe 10612; ~ kišvar 867. — Av. (202) arazahi-, which denotes, according to Bthl, the westernmost continent; this is contrary to 867; v. HP II, 21 sq. and Sogd. 28-29.
1625:Ganjak [gnck'] town in Azarbaijan 11715. — Cat. 108 sqq.; Arab Janzah, Kanjah Yàqüt 2,132; cf Šēcīkān.
1878:handäcak [hnd’ck'] measure; ~ nimūtan to measure 1109. — From handāxtan (g. v.); NP andäzah; Talm. lw. hndz? ‘calcu- lation’; Syr. lw. handäzä ‘that. which is measured'.
2199:ibd.; 222, 422-71 passim; 971; 14-16 pas- sim. — MPrs knycg; NP kanizah. Dimin. of kanik; v. also kanisk. (Ps. 122% knysky, v. Barr s.v.).
2312:seven are enumerated 10612-14; Arzah ~ 86’; Savah ~ 868; v. these. — Av. (459) karšvar-; MPrth gyšfr, MPrs kyšwr; Ps. kšwbly ‘the earth’; Paz. kešvar; NP kišvar. As to the etymology cf kisvicàr.
2697:(S); Paz. neža; NP mizah; Arab lw. naizak-. nifrin [nplyn'] curse 9717”. — ni + Av.
3301:riz [Uc] a secret 27», — Av. (1514) razah- ‘solitude’; MPrthPrs r’z; Paz. NP raz; Arm. lw. eraz ‘a dream’; borrowed by all Aram. dialects.
3414:Savah [sw'h, swh] the westernmost part of the universe: ~ ktšvar 868; 106%, — Av. (1562) Savahi, which signifies the easternmost kišvar, v.s. v. Arzah.
5009:arozahi-: Arzah
5311:razah-: raz
```


### [2026-09-07T20:25:05.651Z] TOOL RESULT

```
(no exact page map; using offset 11 -> pdf page 119; check the printed number and re-run with --pdf-page if off)
REF: IRN:108  PDF: data/verification/sources/refs/incoming/IRN/IRN_eliteraturebook.pdf page 119  OCR-lang: fas

۱۸ ایرانویج
می گیرد و پس از آنکه بخش جنوب شرقی ترکیه را آییاری کرد وارد کشور عراق
می‌شود. در این سرزمین از تنگه‌های کوهستانی‌بسیار می گذرد و در ناحیةٌ کردستان
در پائین موصل» آبهای زاب بزرگك وزاب کوچک ك که ازکوههای غربی ایران
سرچشمه می‌گيرند به‌آن می‌پیوندند. این رود زا ب که در فرهنگها وکتابها ی
جغرافیای تاریخی کندن آن را به «زو» پادشاه داستانی ایران نسبت می‌دهند, در
اصل ترکیب شده است از واژه‌های «زه» و «آب» واین ترکیب همانست که در
واژهٌ «زهاب» در نام محل سرپل زهاب» دیده می‌شود. دراين ترکیب زه به
معنی زاینده است از ريشهٌ 22 به معنی زاییدن وزهاب یا زاب به‌معنی رود زاینده
است و بازاینده‌رود هم‌معنی‌است . نام های محلی اين دو زاب درکردستان‌به گویش
محلی «زی بج وکث» بدا 2:27 زاب کوچکه‌و«زی گور»80۷۳2 227 -زاب بزرگك
است .

اروندرود سپس بینْ سامره وبلد وارد دشت میانرودان می‌شود ورسوبات رود
دیاله آن‌را به‌سوی غرب می‌راند. رود دیاله از بهم آمیختن رودهای «سیروان»و
«زالم» و«تنجه‌رو» پدید می‌آید وجای پیوستن این رودها «دوآوان» نام دارد.
دیاله در همه مسیر خود در سرزمین عراق به‌نام یکی از رودهای تشکیل دهنده
آن» سیروان نامیده می‌شود ونزدیک «سلمان پا کك» درجنوب بغداد به دجله می‌ریزد
و دجله را به سوی غرب می‌راند و آن را به فرات نزديکك می‌سازد, رود دجله
پس از پیمودن مسافتی دوباره به‌سو ی کوههای زا گرس باز می گردد ونزدیک عماره
در اثر رسوبا تکرخه به سوی جنوب می‌گراید و در «الغرنه» در ء + کیلومتری
شمال بصره رود فرات به‌آن می‌پیوندد . سپس در شمال جزيره آبادان رود بزرگك
کارون به آن می‌ریزد واروند رود بزرك پس از پیمودن طول جزیرةٌ آبادان به
دریای پارس می‌ریزد. درازای این رود از سرچشمه تا دریای پارس نزديکك به
۰ کیلویتراست ودر سال . ه میلیون تن رسوب دارد که از مقدار رسوب رود
نیل بیشتر است .
```


## [2026-09-07T20:25:28.752Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== line 2965-2975 ==\"; sed -n '2960,2975p' BRT.txt; echo; echo \"== aostra ==\"; grep -n 'aoStra\\|aostra\\|aoBtra\\|aoslra' BRT.txt | head; echo \"== Mund ==\"; grep -n \"'Mund'\" BRT.txt | head -20",
 "description": "Bartholomae aosta, aostra, Mund"
}
```


### [2026-09-07T20:25:28.834Z] TOOL RESULT

```
== line 2965-2975 ==
'9Zi  46;  —  aAy3  veha  'iö  vidi  (sd.) fftanatjM  Y.4ff.  i ;  —  me/u  t/it  paiti  aiin- ttaot   "Sarshai   kva  Aisra  V.  2. 5  PüZ.  (?)
Ableit.  —  aL  •öiai-.  —  \g\.  aosa-.  —  Fü. :  öS. •  j.  aoäah'vant-  Adj,  (fem.  "vaiii-)  'dem
uüdvanayal . .  nOii  °ra  avßirisyät  (s^.)  Yt.  Untergang  ausgesetzt,  vergänglich,  slerb- 5.62;  —  'ra  vatiuhls  ußa.saaa  {%A.)  VLjlich':  azdibl^  ,. 'sati/iat'^yäs?  tanvö  V.4. y.  147;  —  paracil  mraoüs  (sd.)  'r^lcä ;  $0;  —  am  "/uwAs"  'iaauAaiti^^  qshm yairJ  mainyus  drfgvats  ^-  53-T,  —  °ra\isaili  tanva  Aog.4<?;  —  ahmi  dhn  patti F.  7;  —  *°rä(a'>  paraca  tarasl'a  F._ya.     \  fran/nnzal  {&&.)    ahmi  fw    bazal  'lanha
IS.  aus  'aora-  Adj.,  Kompar.  aus  'ava.  —  ai. . ". .  mit   dem  ward  dieser  Sterblich"  V.  2.
vgl-  evata-  Adj.  'inferior'  (wozu  aera-  wie  Ht.  |  ^  püZ.^';  —  yahmat  haca  naicU  bunjayät
T""'7  ^  Hds.  Iu,ra.a,  m,t  k  statt  a;  vgl.  p,_.  ..^.^^_^_  _-;j  j-^^^^^^  6^-^  unsicher.  - *■  ■'■'■  '■  =)    Dk.  JJ.  22.   12:    «  in   pa    äa   äiSmaJul  bül,
•  g.  aoz-  V.  'achten'.     Praes.  i  uz-.       \     näml.  Kavay  Vi,,»-,  vgl.  Dst.  ZA.  j.  39. 'achten  für  -',  mit  dopp.  Aklc. :  ki  kvö  ,  j.  ao§ö.tara-  Adj.  'der  verderblichere,
y}m3  arsdrv  m>at*paouruyÖ  ya'i^a'i^wäy.^YCi.mi'atxe:  'rasiä  ..yai:a  anya  vp&ria zivTitUn  uz^maiT {iVFA.)'*  syao^iatiot  sp?n-\ii/_in_^y^  ^2_
hm  akurim  aiavanim  "wer  ist  es,  der!     Vü.-.  oi  x''ästjiiar,  a\.:  vaiiiii/ar,vai  zöiiar.
fromme,  der  es  zuerst  gelehrt  hat,  dass  •  j.  aosta- m. 'Oberlippe',  Du. 'die  beiden
wir   dich    für   den   förderlichsten  achten,  Lippen''';  'laai(KS.)  paiti  diimmica  -iri-
für  den  in  seinem  Tun  heiligen  gerechten  ratac'a  g'arsu/  V.  7.59'^-
Herrn?"  V.  46.9.  \      VßL  a.'i/ra-.  —  ai.  ^^/*-i-  w.Ö  —  Pü.:  /<i  tän
ai,  ü/iaii  'er  achtet  für  -'.  —  Vgl-  <ii"«iT-.—        "  "A"'  il""  Snia  ^  ndakdt  ^',1,   er!.:    hi  nc
Pü.;  buloiid  iizllan,  Sü.:  «/Mü/«™  J).— D  Kaum         daxlak  i  yruSk  aj^  fa  tn\>TH'xi-Fs  huu!i~.i.   S.
Tichlig  beieugt;  man  verlangte  Konj.;  2um  ?       nocl»  No-  i-  —  '>  Red-  nach  ai.  fiiha-»  und

== aostra ==
11618:(Za/*äoTt75)  zweier  Gläubiger  r)  des  Mi- nisters Visiäspai,  Schwiegersohns  Zara- &aÄr<is">,  Bruders  FraSao^tra%  aus  der ^»j^flfamilie:  °pahe  AvSvaAe  (sd.)  Yt y- 1 03  j  — ya^rS  vS  a/sman[{sd.)  sSrtghänT ..  'pa  (VS.)  hvs^va  (sd.)  Y.  46,  17; 4g.  9 ;  —  tarn  ciitltn  'fS  hvB.gvS  tsldü :^armh  (sd.)  ala  vtnnti  Y.  5/.  18;  — yS  . .  bar?sma  */rasttrmte  ya%a  asava  °p5 */rastfrinaSa  ra/u/rif  li.Sg;  —  amava ya^a  °pü  Az.  2;  2;  Vyt_j;  —  yävaranä *frasaoslra  •/s(ND.)  ..ta  vannilcä (sd.)  . . Y./2, 7;  —  ao/i/a  tT  zarai:uslra  fralaos- tralibya  'pa^bya  Vyt.  //;  —  tarn  (näml. andvltn)  yazaia  -ps  yat  spShm  pairi.- avalnal . .  drvatqm  Yt  5.  68,  a)  °pafie aparamtahe  (sd.)  asaonS  Yt  ij.  127.
14321:—  yd^ä  ^wä  zTvTiHfK  uzimökz  (sd.)  Y. 46.');  —  *yavatai'>  ^wä  masds  *staomI ufya(s±)cä  Y.43.S;  —  maibyB  %wä sqsträi  (sd.)  v»r?nl  akurä  Y.4^-Z'>  — vakistim  %wa  .  .  akur»m  yäsa  (sd.)  Y. 2Ä8.  zu  I  a):  atzt'h-wäfsuyantailä.. "hwsnlta  (sd.)  latasä  Y.  2p.  6;  —  dazu wohl  auch*':  azSm  tai!  ^wä  /raxsnlisd.) aväml  magdä  Y.  44-  7 1  —  sp^nttm  at %wä  mazda  mingkx  (zA^  V.4J.  5,  7,  9, 11,  13,  ij.  zu  3):  firalaostrai  .. alakyä  da  I  sarSm  ta}  %wä''^  mazdä yäsai^d.)  Y.4p.8;  —  s.  noch  Y.2Ä  5  im Anhang.  Anhang.  Der  Akk.,  dem ein  Vok,  vorhergeht,  ist  dem  Akk.  eines (mit  CS  angeschlossenen)  Subst  koordinirt (Sp.  565  u.);  vgl.  2,  9  (Sp.79ou.):  asä  kaf %wa^''  darisani  (sd.)  manascä  vokü  Y. 28.  s;  s.  zu  2.  B  I  ß)  im  YHapt.;  zu  1): a%a  %iiia  ail  yazamaidiY-sg.i,;  36.\ i.St,  3;  —  kumälm  %wa  .  .  yazat^m  .  . dadsmaidi  Y,  47. 3 ;  —  äzoö  (zu  'hwa-)  ^wä mainya  spStiistä  (näml.  pairT.jasämaidt) Y.36.1;  5;  —  vokB  %tvä  manar^ks  voka %7iia  asa  ..  Y.36.4;  4.  zu  z):  a^ä isBidyämakx  %wä  mazdä  akurä  Y.^^,4;
17563:•  j.  fsra-xSaostra-  n.  'Vorwärts-,  Weiter- fliessen':  apqmc3  'r^m  Y.42.6.
18277:•  j.  fräSaoStrayana-  patr.  Adj.  'von  Fra- ^aoslra  stammend,  dessen  Nachkomme': husyao'^nahe  -nahe  Yty.  104;  —  s^ä- dalnahe  'naht  Yt.  13. 104.
20861:yäca  lasmqm  . .  ar>jat  (sd.)  . .  xsmakät (sd.)  vahmai  "quae  faciam  . .  quaeque  . ., (ea) .."  Y.50. 10;  —  kJ  asavayäis piTisai (sd.)  "quis  (est)  fidus  (eomm)  quibus- cum  . ."  Y.  44, 12;  — Jirasaostrai  matbyaca yawibyasca  it  rauhanksi  {^d^  ''..et  mihi ..  et  (Üs)  quibus.."  Y.aA'.S; — mit  Gen. part.:  srQidyai  (sd)  .  ./ravaoSi  yä  (APn.) vTdayai  asis  rainqm  (sd)  ". ,  (ea)  quae  . , debitorum"  Y,_J4.  iz;  —  s.  noch  Y.J/.  6
24607:im  1.  Glied?  -  ')  So  F  i :  NA,  vf.  I  y.^^,.  16;  _  kavac3  'ps  .  .  forasaostrasla
27038:•  J.,  g.  spitäma-'*  Adj.  (fent  'iämi-)  Name einer  iranischen  Familie  *';  a)  im  gAvr.: Aaidataspa  (sd.)  vaxfyä  vS  •tamänhs  Y. 46. 15;  —  von  MaidySi.mir»ha:  maidydi.- mät^Aä  'tamätyS.)  Y.5/.  19; —  von/sal- vastra:  atcä  hsi  scantü  .  ,  xsnüm  (sd.) kavaüa  viitaspS  zara%uftris  (sA)  'tamö firasaostrasca  ". .  Kavay  Vlitaspa  und  der Zara^uitrasd\m,  der  SpttamäK  und  J-ra- saoiira"  Y.  53.  2;  —  von  Pouruastä: pouruHstä  halcat.aspana  (sd)  'tärnl  yezivi dug>drqm  sardhustraAl  Y.^3. 3; —  sonst von  Zara%usira;  unmittelbar  hinter  oder vor  dem  Namen:  tara'kuürB  'tams  V. 2g.  Z;  —  zanihuitrvm  'iam?m  Y.j/.  la; —  zara'iultrake  •tsmahyä  Y.5^,  i;  — 'tamsm  lardhuitr^m  \.4ß.  13;  —  'tamai zara%uärai  Y.51. 11.  b)  im  jAw.: '^rimi^waiS  (sd.)  'tämahe  Vt.J_j.  98;  — sonst  nur  von  Zara'^ustra  als  dem  ^i- /oMiden  Ktn'  it:  yd^a  un/ahtm  'tamai Y.ip.i4;  —  im  Vok.:  afva  te  sävan aojasca  .  .framrava  )r?svB  'tama  Yt.  13.  i ; 5.89,  gi,  i~.2i;  —  mi^nm  ma  Janyh 'tama  Yt/0.  2;  i,  i,  118,  119,  140,  143, /_y.  17,  Y.  6'2.  7,  FrW.  .^.  1;  —  vor  oder hinter  dem  Namen:  avaiata  yS  'tamö zardäiustrS  <ßtvtix.)'V  .ig.T,\iSV.  "'täm^m, 'tämahe''',  'lamai,  'tama  —.
27827:*>  Ich  halte  es  fär  sicher,  dut  Zart&uSira eine  geichichtlicbe  PersöoUcbkeiE  ist,  sowie  dass die  Gä%äs  im  wesentlichen  auf  ihn  lurückgehen. TiELB  GeschRelAIt.'  3.  275  CTklärt  mit  Recht den  Zar.  des  jüngeren  Awesla  (ül  "eine  vSIlig mflhische  Person",  aber  dnss  er  «chon  in  den Gä%äs  "eine  legendarischc  Penon"  sei,  mnss ich  ihm  bestreiten.  Ich  finde  vielmehr,  dass er  uns  hier  darcba,as  körperlich  nnd  meaichlich entgegenicitt.  Sein  Reformationswcrli  ist  noch in  den  ersten  Anlangen  begriffen.  Nur  ent wenige  einflussreiche  Männer  sind  dafür  ge- wonnen, nm  es  aU  Soosyanl  {lA.)  zu  nnterstütien : SD  ausser  dem  Sohn  Iial.väslra{i.  lara^tütray- a) nnd  dem  Vitersbruder /ftiiyöt.m^wAa  inibeson- dere der  Fürst  yäiäipa,  sodann  Jämäiftt,  dessen Minister,  und  Fralaoslra,  deren  beider  Interesse durch  Knüpfung  verwandtschaftlicher  Bande  ge- festigt, wird  -  Zar,  beiratet  Frai.z  Tochter  und gibt  Jim.  seine  jüngste  Tochter  ßimraaslä lar  Ehe  -,  femer  der  TKrer  Fryäna-  (s.  Ntr.}. Auf  der  andern  Seite  setzen  die  den  alten Göttern  iäana-)  wie  Mi^ra,  Haoma  usw.  und ihrem  Kult  treu  bleibenden  Fürsten  {kaii)^-, säslar-)  nnd  Priesler-Lehrer  [kivapan;  uäg-')  wie Bindva,  Grlhma  dem  Neuerer  heftigen  Wider- sland entgegen,  lo  dass  er  häufig  genug  in  bittere Klagen  Bosbrieht  und  der  Besorgnis  Ausdruck gibt,  ob  er  seine  Mission  werde  fortfuhren  können (vgl.  iB.  Y.  46.  i).  Beieichnend  ßr  die  ■Wirk- lichkeit der  Verhältnisse,  unter  denen  die  (7ü^s entstanden  sind,  ist  die  Strophe  Y.Jf.  iz.  Haite ich  sonach  an  Zar.  als  historischer  Figur  durch- aus fest,  so  sehe  ich  doch  anderseits  jeden  Ver- such, die  Zeit  seines  Auftretens  genauer  zu  be- stimmen, für  aussichtslos  an.  Nach  der  heimischen Chronologie  (s.  West  SBE.  47.  xxvm)  würde Zar.%  Geburt  in  das  Jahr  660  v.  Chr.  fallen, und  Jh.  Zor.  174  hält  das  für  wesentlich treffend :  "the  period  . .  just  before  the  Achae- menian  power  [is]  the  approximate  date  of Zoroaster's  life".  Ich  glaube,  wir  werden  wesent- lich weiter  zurückzugreifen  haben,  und  urteile über  Jn.s  Ausführungen  wie  Tiele  GeschRelAlt.> 2.275,430.  Einer  Chronologie,  die  damit  rechnet, dass  ein  Lehrer  des  Glaubens,  der  als  erster 100  Schüler  um  sich  versammelte  (s.  ^sarna-\ 100  Jahre  nach  der  ersten  Verkündigung  der neuen  Lehre  geboren  wird  und  100  Jahre  att stirbt,  kann  ich  kein  Vertrauen  schenken.  S.  auch No.  I  zu  vüläspa-.  —  Die  Angabe,  Zar.  sei  im Weslen  von  Irin  geboren  (s.  rayay-),  ist  mit  der Tatsache,  das«  alle  entscheidenden  Stellen  de* Awesta  (insbes.  Yt.  ig.  66  f.)  auf  Entstehung  im Osten,  in  der  Gegend  des  //äiniinsees  hinweisen, keineswegs  unvereinbar.  Es  lisst  sieb  sehr  wohl begreifen,  dass  der  Reformator  seine  Heimat verlies!,  weil  er  keinen  Anklang  fand,  oder  auch verlassen  musite.  So  mag  sich  auch  seine  starke Betonung  wirtschaftlicher  Giundsätie  (s.  väilrya-) erklären.  Der  Westen  Irans  stand  zweifellos auf  einer  wirtschaftlich  wesentlich  höheren  Stufe als  der  Osten,   wo  man  sich  noch  lange   nicht
== Mund ==
7567:•  j.,  g.  ^äh-,  g.  S»äh-"  n,  'Mund':  tal  nS maiuia  , .  vaocil  hisvä  (sd.)  'hwahyä  üfthö y-J'-3>  —  ahurä  . .  frS  ntä  sTsä  *vao- catihg .  .%WiJ  JjäuAä'i  Y.2S.11;  —  ä/jia (IS.)  F.jd.         [P.2S:  lies  «^wÄa.l
7782:•  j.  anhan-  n.  'Mund';  &.ioa  '^aiqm  tarash •hänö  (GS.)  srasantis  x'arf'hä  bairyänte
14496:•  j.  9-raDh-  n.  'Mund':  -arg  (NS.)'>  F. 23.  a)  Du.  'die  Mundwinkel' :  nazdyd  . . ya^a  *näaha  haca  *gaosalibya  yaha vä  gaosa  haca  ^'anhibya'^  "näher .. als  die Nase  von  den  Ohren  oder  als  die  Ohren von    den   Mundwinkeln   (entfernt    sind)"
22303:Zam  V.  i/fli-,  —  ai,  vaktra-  n.'Mund'.  —  Pu.: göwisn.
30100:•  j.  hizu'ma-  m.  'Mund'":  upa  vH  nastts ralhwät  narahanat  .  .  easmanat  .  .  'mai haca  V._j.  14.
```


## [2026-09-07T20:25:43.253Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -o -E '.{60}(us\\.zan|uz\\.zan|zizanan|us\\.za[a-z]{0,6}).{140}' BRT.txt | head -8; echo \"== zan- gebären ==\"; grep -n -o -E '.{40}zan-  ?V\\..{160}' BRT.txt | head -5; grep -n \"'gebären'\" BRT.txt | head -8",
 "description": "Bartholomae us.zan / zan- gebären"
}
```


### [2026-09-07T20:25:46.281Z] TOOL RESULT

```
21242:w.;  i)  mit  Ind.;  ia} ahtnai  jasal  äyapUm  y  Alpu^rü  us.zayata Y.5,4;  7,  13,  13;  —  moiu  iai  äs  .  ,  y° fräyatayat  .  .  aoi  zqm  Yt 5.65;  —  altat il ..  aiAhe(ßp.\om)  avayam  *dqtimaM y*  
27625:zeugen',  von  Menschen: dvaiibya  haca  mrsbya  dva  nara  us.zayeinte (statt  Du.)  mßiwana  strii'a  nairyas^a  "von dem  Menschenpaar  wird  ein  Menschen- paai  erzeugt . ."  V.  2. 41.  2)  'gebären'; Pass
27625:e- redter Mann  geboren  werden"  Yt,  ij.  16; —  yahmäi  *us.zayäiti*'^  taoiyqs  V)r3%raja haca  apat  kqsaoyai  V.  ig.%\  —  yat  hl pu%r5  us.sayaia  Y.5. 4,  7;  —  yat  hl tum  ussayaaha  Y.  p.  13
27625:  (3DPrM.)  urväxsayo  kiri- säsfasca  Y.p.  10;  —  pu%ra  us.zayänte Az.  I.  3)  '(Tiere)  züchten':  yat  bä patti fralst?m  us.*zazfnti''>  (3SPA.)  pasvasca staoräca  "wo  man  am  meisten  Klein-  un
== zan- gebären ==
27622:'gebären';  1)  von  Menschen;  a)  Ait: SicöM  (nJimlandvIin)  Üaräitii zizanaitt^ (NPf.)  Jaihyante  huzämim  (sd.)  ".  .  ge- bärende Frauen  . ."  Yt.5.87;  —  3r»hqm raya  .  .  Auzämitö  (sd.)  zTzan?nH'''>  (näml. hairiSis)  Yty.  15;  —  ya%a  ha  tsm  zi- zanäp^  yS  .  .  Ytl^.  142;  —  gal%anqm Stshairyeke  (sd.)  .  .  yat  anAairyS  tlzatun Vr. /.  3;  2.3.  b)  Pass.  und  Med.  in pass.  Sinn:  yahmai  zayata  %raltaonS  V, /.  1 7 ;  —  ahmat  haea  puhra  (sd.)  zayaiti^^ Nik.  1;  —  zaySnte  .  .  dasa  ^%ra  Az.5; Vyt.  I,  j;  —  ndil  akmi  nmäne  *zänaite'''* (3PPM,)  ä^rava  naiita  . ,  äat  ,  .  zayinte "nicht  werden  in  diesem  Haus  geboren ein  Priester  noch  .  .,  sondern  es  werden ..geboren  werden  .."  Y.  j/. 6;  —  narqmca zätanqmca  zqkyamnanqmca  ".  .  die geboren  sind  und  künftig  geboren  werden" Y. ^5;  —  s.  noch  zata-  bes.  a)  von Tieren:  bawranqm  */atur3{sd.)  *sTzana- tarn    "der  Biber,  die  vier  Junge  werfen"
27625:mit  US  i)  'erzeugen',  von  Menschen: dvaiibya  haca  mrsbya  dva  nara  us.zayeinte (statt  Du.)  mßiwana  strii'a  nairyas^a  "von dem  Menschenpaar  wird  ein  Menschen- paai  erzeugt . ."  V.  2. 41.  2)  'gebären'; Pass.  'nasci':  ankam  raya  .  .  us  nä  za- yeiti^'>  (Konj.)  vyixanö  ".  .  wird  ein  be- redter Mann  geboren  werden"  Yt,  ij.  16; —  yahmäi  *us.zayäiti*'^  taoiyqs  V)r3%raja haca  apat  kqsaoyai  V.  ig.%\  —  yat  hl pu%r5  us.sayaia  Y.5. 4,  7;  —  yat  hl tum  ussayaaha  Y.  p.  13;  —  yat  hs pu%ra  wj.3(yy(äf  (3DPrM.)  urväxsayo  kiri- säsfasca  Y.p.  10;  —  pu%ra  us.zayänte Az.  I.  3)  '(Tiere)  züchten':  yat  bä patti fralst?m  us.*zazfnti''>  (3SPA.)  pasvasca staoräca  "wo  man  am  meisten  Klein-  und Grossvieh  züchtet"  V,^.  5.
29512:•  3  hav-  V.  'gebären',  von  äafvischen Wesen".     Praes.  11  Aunä-'K
```


## [2026-09-07T20:26:05.322Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== WLD Bd1 ozgho/ozdo ==\"; grep -n -o -E '.{100}(ozgho|ozdo|azg .Ast|óskhos|oa\\^os).{300}' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -6; echo; echo \"== WLD Bd1 'Knospe, Pflanzentrieb' ==\"; grep -n -o -E '.{200}Pflanzentrieb.{300}' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -4",
 "description": "Grep Walde-Pokorny for ozgho"
}
```


### [2026-09-07T20:26:05.410Z] TOOL RESULT

```
== WLD Bd1 ozgho/ozdo ==

== WLD Bd1 'Knospe, Pflanzentrieb' ==
```


## [2026-09-07T20:26:06.969Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== LAT os ==\"; grep -n -o -E '.{60}(ōscillum|oscillum|oscillo).{250}' LAT.txt LEW_1910.txt | head -8; echo \"== LAT os oris ==\"; grep -n -o -E 'ōs,? ?ōris.{200}' LAT.txt | head -4",
 "description": "Grep Ernout-Meillet / Walde for oscillum"
}
```


### [2026-09-07T20:26:08.289Z] TOOL RESULT

```
== LAT os ==
== LAT os oris ==
```


## [2026-09-07T20:26:12.471Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== WLD files ==\"; ls -la incoming/WLD/ WLD_band3.txt 2>/dev/null | head; echo \"== search azg in WLD ==\"; grep -n -i 'azg' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -10; echo \"== search Schößling ==\"; grep -n -i 'schößling\\|schossling\\|Schöfsling' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -10",
 "description": "Check WLD Bd1 file"
}
```


### [2026-09-07T20:26:12.546Z] TOOL RESULT

```
== WLD files ==
-rw-rw-r-- 1 sfmqrb sfmqrb 317372 Sep  4 14:06 WLD_band3.txt

incoming/WLD/:
total 146216
drwxrwxr-x  2 sfmqrb sfmqrb     4096 Sep  4 14:06 .
drwxrwxr-x 23 sfmqrb sfmqrb     4096 Sep  4 14:06 ..
-rw-rw-r--  1 sfmqrb sfmqrb  2993454 Sep  4 14:06 WLD_Bd1_1930_dli_70244_djvu.txt
-rw-rw-r--  1 sfmqrb sfmqrb 42256714 Sep  4 14:06 WLD_Bd1_1930_dli_70244_text.pdf
-rw-rw-r--  1 sfmqrb sfmqrb  4327601 Sep  4 14:06 WLD_Bd1_pages.txt
-rw-rw-r--  1 sfmqrb sfmqrb  2417287 Sep  4 14:06 WLD_Bd2_1927_dli_106624_djvu.txt
== search azg in WLD ==
7497:,,Barsch“, poln. jazd'z, jciszcs (auch jazgarz) „Kaulbarsch‘ f ; s. Trautmann 
11919:Pehl. azg „Ast“ (nachgewiesen von Hubschmann IF. 4, 119, zw. ob nicht 
11920:azd — bgog zu lesen ; doch azg wegen :) np. azay „Zweig, Knospe“ : gr. 
11930:iizgz>, russ. azg „Ende, Kamm“, poln. dial, wbzg (*witzq) „SchoBling“ ( *ongh-sqn 
11933:rechtfertigen, auch wtirde pehl. azg dann als ngh-sqo- eine Ablautstufe neben 
11934:boyog darstellen und waren azg : doyog dann nicht mehr vollstiindig gleich. 
21409:KazQai, Kazgoy.evzat. — Ob in gr. oazivg „Streitwagen“, odztXXa' ziXeidg zo 
41684:(Berneker SlEWb. 302), bulg. glezz, glaz'd „verziehe, verzartele", razgleza 
44141:einander, uberwallen" ; umgestellt zgar- in avi frazgciraiti „flieBt herzu 
50641:dfizJia „Span“, drizhati „schleiBen, spalten, in Stiicke reifien", poln. drzazga 
== search Schößling ==
```


## [2026-09-07T20:26:15.474Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '11905,11945p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt",
 "description": "Print Walde-Pokorny I 185 ozgho entry"
}
```


### [2026-09-07T20:26:15.529Z] TOOL RESULT

```
derselben, bei Baumnamen der Balkansprachen mit Parallelen belegbaren 
Bedeutungsverschiebung wohl auch:) gr. dfib; „Buche; auch Speer, Lanze“ 
(Schrader aaO. 3173, Grdf. freilich kaum *dox[e]a-, Boisacq 107; es scheint 
lautliche Anlebnung an oft's vorzuliegen, wenn auch kaum nacb Fick 
GGA. 1894, 242 eine Kurzform von 6£vipvJMjg), arm. haci „Eache“ (Bar- 
tholomae IF. 1, 304 Anm. m. Lit., Hubschmann Arm. Gramm. I 465) 4 ). 

S. uoch Meringer SBWienAk., phil. Cl. 125, II 8 (will ein Paradigma 
*osi, *os-n-es erschlieBen), Uldenbeck PBrB. 30, 262 (gegen Johansson IF 
14, 323k Hoops Waldb. 121. 


ozgho- „Knospe, Pflanzentrieb, Zweig“. 

Pehl. azg „Ast“ (nachgewiesen von Hubschmann IF. 4, 119, zw. ob nicht 
azd — bgog zu lesen ; doch azg wegen :) np. azay „Zweig, Knospe“ : gr. 
bo yog. ooyg, d>oyg „Zweig, Scho81ing“, Seheftelowitz IF. 33, 141. 1 44 f. 

Die gr. Worte nicht walirsclieinlicher nach Brugmann IF. 19, 379 Anm.. 
Grdr. II 2 2, 816 eine dem idg. *o-zdos parallele Zs. b-zgho- (: I'.ym , 

oyeiv) „sich (am Stamm) festhaltend“ ; Kreuzung von bgog (d. i. bodog) mit 
uboyog (Yf. KZ. 34, 523) wird dem iboyg Hesychs nicht gerecbt. 

Seheftelowitz vergleicht ferner unter Ansatz der \Vz. als ongh- urslav. 
iizgz>, russ. azg „Ende, Kamm“, poln. dial, wbzg (*witzq) „SchoBling“ ( *ongh-sqn 
aksl. qzlo, russ. nzeh „Knoten“) und np. cizm .,(*SchoBling =) SproBling. 
Sobn“; aber ein on\g]zglw- aus *on?jh-sqo wurde nur gr. boyog, nicht aber < boyg 
rechtfertigen, auch wtirde pehl. azg dann als ngh-sqo- eine Ablautstufe neben 
boyog darstellen und waren azg : doyog dann nicht mehr vollstiindig gleich. 
— DaB zu ooyog mit andern Suffixen auch bgog (s. *ozdos ), ferner air. odb 
„Knoten“, cymr. oddf „Anwuchs, Ivnoten“ idoch s. u. i>d(e)go- „Stengel“) 
gehoren sollen. bestreitet Seheftelowitz (Lit.) mit Iiecht. 

ost(h)- ; ost(h;i, ostt.h;r(g), Kasus obi. ost/h)-(e)n- „Knochen“. 

Ai. asflii n., gen. asth-n-ah „Bein, Knochen", av. ast-, asti- n. „Knochen‘\ 
pali ntth 'dnco „Krebs“ (* asthi-lvnms ,knochenhiiutig“, Schulze KZ. 43. 380. vgl. 
zur Bed. gr. bmay.bg ,.Meerkrebs“) ; gr. bar tor ,.Knochen“ (w r ohl *ooreyov ..^bei- 
nernes :i = lat. ossevm. Bgm. II 2 1 . 157; fur Sommers Hdb - 405 *boTf f-ov kann 
weder av. aslava- „mit einem Knoclien versehen“ noeh lat. ossu, asstia als
```


## [2026-09-07T20:26:35.939Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in range(315,345):\n    for m in re.finditer('ازم',leaves[i]):\n        s=leaves[i][max(0,m.start()-60):m.start()+80].replace('\\n',' ')\n        if 'لازم' in s or 'ازمو' in s or 'ازما' in s: continue\n        print(i,'|',s)\nEOF\necho \"=== ARY ازغ ===\"; grep -n 'ازغ\\|اژغ' incoming/ARY/ARY_pages.txt | head -10",
 "description": "Search BQT for azm and ARY for azgh"
}
```


## [2026-09-07T20:26:36.753Z] TOOL CALL #62: WebFetch

```json
{
 "url": "https://www.sanskritdictionary.com/?q=adga",
 "prompt": "What does Sanskrit 'adga' mean according to Monier-Williams and other dictionaries? Give the exact gloss."
}
```


### [2026-09-07T20:26:37.192Z] TOOL RESULT

```
329 |  ۵ . ۲ : ۰۱۸۳ ۷۹ ۰ . اورامانی 5 « ۵ . اورامان۱۲۰ » . اسب را ازمسدر 26 (*88) آریابی بمعنی تلد رفتن» گرفته‌اند .< فاب ۱ : ۲۲۲ و۲۲۹ *. ۱ در پپل
=== ARY ازغ ===
```


### [2026-09-07T20:26:38.636Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-07T20:26:47.008Z] TOOL CALL #63: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/adga",
 "prompt": "Is there a Sanskrit entry अद्ग / adga? Give meaning and etymology if present."
}
```


## [2026-09-07T20:26:47.016Z] TOOL CALL #64: WebSearch

```json
{
 "query": "Sanskrit \"adga\" Monier-Williams \"a stalk\" cane meaning"
}
```


### [2026-09-07T20:26:48.476Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-07T20:26:54.297Z] TOOL RESULT

```
Web search results for query: "Sanskrit "adga" Monier-Williams "a stalk" cane meaning"

Links: [{"title":"Monier-Williams Sanskrit-English Dictionary --स","url":"https://sanskrit.inria.fr/MW/295.html"},{"title":"Adga: 8 definitions - Sanskrit dictionary","url":"https://www.wisdomlib.org/definition/adga"},{"title":"cane - KST (Online Sanskrit Dictionary)","url":"https://kosha.sanskrit.today/word/en/cane"},{"title":"Monier-Williams Sanskrit-English Dictionary -- v - tuninst.net","url":"https://www.tuninst.net/SED-MW/download-prem/v.htm"},{"title":"adga meaning in Sanskrit | adga translation in Sanskrit - Shabdkosh","url":"https://www.shabdkosh.com/dictionary/english-sanskrit/adga/adga-meaning-in-sanskrit"},{"title":"Monier-Williams: A Sanskrit-English Dictionary (1872)","url":"https://gretil.sub.uni-goettingen.de/gretil/6_sres/2_dict/mwse72_u.htm"},{"title":"Monier Williams - Sanskrit-English Dictionary 1872 | PDF","url":"https://www.scribd.com/document/321388649/Monier-Williams-Sanskrit-English-Dictionary-1872"},{"title":"Monier-Williams Sanskrit English Dictionary Page 0498","url":"http://www.ibiblio.org/sripedia/ebooks/mw/0400/mw__0498.html"},{"title":"Monier Williams Sanskrit-English Dictionary","url":"https://www.monierwilliams.com/"}]

Based on the search results, I found information about the Sanskrit word "adga" from the Monier-Williams dictionary and other sources:

According to the Monier-Williams Sanskrit-English Dictionary, "adga" (अद्ग) is a masculine noun. The word means "stalk, stem, cane".

The dictionary also provides alternative definitions: adga can refer to a sacrificial cake (puroḍāśa) made of rice, and it appears in the Atharva-veda (i, 27, 3) as a cane.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-07T20:27:04.313Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\ni=t.find('odsghos')\nprint('char idx',i)\nprint('leaf (ff count before):', t[:i].count('\\f'))\nprint(t[i-200:i+500])\nEOF",
 "description": "Locate IEC odsghos leaf"
}
```


### [2026-09-07T20:27:05.609Z] TOOL RESULT

```
char idx 1668504
leaf (ff count before): 481
id.; Alb. âmë, f. ‘scent,
863
savour’ beside âmëz, f. id.; Latv. osma, f. id. (See EH: SEO: os, n. ‘vapour’; kol-os 'fire- damp', mat-os “smell of food', if fr. *odso-). Cf. also Oss. asmá “thick fog
odsghos (odzgos, odhgos), a “shoot, branch, stem'. WP I, 185 Skt. cf. ádgah, m. 'cane, stalk'; Pahl. azg *branch'; Per. azay, (id. and 'shoot); Gk. óskhos, e, mf. id., cf. also ól-oskhos, m. ‘pedicel’; W osg, m. ‘shoot, projection? beside osgl, pl. au. and osglen, f. “branch, twig
(odhros, see edhros (1) and ordhos (4))
ogh- (1) (?) *intensely-, very-?. Cf. ogholos Arm. cf. h-ogn ‘abundant’; h-ogunk&, pl. (abundance', fr. en-°, or ep-?); Gk. ókha ‘very, excessively’; Icel. cf. aga- 'saturated-';
```


## [2026-09-07T20:27:15.952Z] TOOL CALL #66: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%83%C3%B3sdos",
 "prompt": "Give the reconstruction, gloss, etymology and full descendant list. Does it include any Iranian form (Middle Persian azg, Persian azgh) or Greek oskhos?"
}
```


## [2026-09-07T20:27:17.365Z] TOOL CALL #67: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/oscillate",
 "prompt": "Give the full etymology of 'oscillate', including Latin oscillum, the mask of Bacchus story, and any doubts about the derivation from os 'mouth/face'."
}
```


### [2026-09-07T20:27:22.665Z] TOOL RESULT

```
# Etymology of Oscillate

The word "oscillate" entered English in 1726, deriving from Latin *oscillare*, meaning "to swing." The transitive sense ("cause to swing backward and forward") developed by 1766, and the electronics usage emerged in 1917.

## Latin Origins and the Bacchus Connection

The Latin *oscillum* originally meant "a swing," but this term "usually is identified with the *oscillum* that meant 'little face'" — specifically "a mask of open-mouthed Bacchus hung up in vineyards as a charm." The semantic evolution reportedly proceeded through "the notion of 'swinging in the breeze.'"

## PIE Root and Uncertainties

The ultimate source traces to Proto-Indo-European *\*os-*, meaning "mouth" (related to "oral"). However, the etymology acknowledges some ambiguity: the 1726 English verb may be "a back-formation from oscillation" rather than a direct Latin borrowing. This uncertainty reflects the challenge of tracing precisely how the Bacchus mask connection led to our modern usage of the word.
```


### [2026-09-07T20:27:24.452Z] TOOL RESULT

```
# Proto-Indo-European *h₃ósdos

**Reconstruction:** *h₃ósdos (masculine, non-ablauting thematic o-stem)

**Gloss:** branch, twig

**Etymology:** The entry states it is "Possibly connected in some way to Proto-Indo-Iranian *Hádᶻgas ('knot (in a plant), branch, twig')" and Proto-Celtic forms. These may represent "different simplifications of the same original compound word."

**Regarding Iranian and Greek forms:**

The etymology mentions Middle Persian *ʾzg* ("twig") as a possible cognate within the Proto-Indo-Iranian family, supporting the connection theory. However, the page does **not** list Middle Persian or Persian forms in the formal descendant section.

Similarly, Ancient Greek *óskhos* and *ōskhós* ("young branch") are cited in the etymology as possibly related, but these are presented as showing "substrate alternations" rather than direct descendants. They appear in the etymology discussion but not in the structured descendant list—only Proto-Hellenic *ózdos* appears there.

So while the page acknowledges these Iranian and Greek words as potentially connected etymologically, they're treated as uncertain cognates rather than confirmed descendants.
```


## [2026-09-07T20:27:34.713Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== SKT usher ==\"; grep -n -o -E 'USHER.{0,300}' SKT.txt | head -3; echo \"== SKT ORAL ==\"; grep -n -o -E 'ORAL[,.].{0,300}' SKT.txt | head -3; echo \"== SKT ODD ==\"; grep -n -o -E 'ODD[,.].{0,320}' SKT.txt | head -3; echo \"== SKT OSCILLATE ==\"; grep -n -o -E 'OSCILLATE.{0,250}' SKT.txt | head -3; echo \"== SKT ORIFICE ==\"; grep -n -o -E 'ORIFICE.{0,250}' SKT.txt | head -3",
 "description": "Grep Skeat for English words"
}
```


### [2026-09-07T20:27:36.213Z] TOOL RESULT

```
== SKT usher ==
20496:USHER.
== SKT ORAL ==
12793:ORAL.
19294:ORAL.
19310:ORAL.
== SKT ODD ==
== SKT OSCILLATE ==
== SKT ORIFICE ==
```


## [2026-09-07T20:27:42.534Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '20490,20505p' SKT.txt; echo \"-----\"; sed -n '12788,12800p' SKT.txt; echo \"-----odd\"; grep -n -i -o -E 'Odd, (not even|strange).{0,300}' SKT.txt | head -3; grep -n -i -o -E 'oddi.{0,200}' SKT.txt | head -3",
 "description": "Print Skeat usher, oral, odd"
}
```


### [2026-09-07T20:27:44.078Z] TOOL RESULT

```
—  L.  uma,  um. Ub.  (E)    A.S.  if/,  dat.  pi.  of  D^  «
Us,  tisic,  ace.  pi.  of  m/.-f'Du.  ffms.  IceL.  i»i Sued,  0SJ,  Dan.  m,   G.  uuj  ;   Goth.  « VNJI>,  dat.  and  ace  pL
our.  (E.)     A.  S.  tire,  of  tts ;  gen.  {4. utt,  we.    This  gen.  pi.  became  aj and  was  regularly  <lecUned  as stands  for  ds-trt  *  -^  Goth,  maaro, of  Goib.  nvu.  we.     Dar.  €^r4,  A. our-setf,  ourselves. Use.  sb.  (F.-1-)     ME.
«/,   use,   USige.  — L.  HJM»K
—  L.  usus,  pp.  of  uri,  to  11^     .... pp.    of    dZ',    to    plesue,    to    be (^AW.)     Dar.  me.  vb,  F.  uur. usart,  frcciucnL  of  L  mSi
V  .  u>a£<  ,  ukUHit.I,  Mriicf.. ^«ra^  \nvBa.  (A.  una,  xflit  ^  ^i.^
USHER.
klniBe.  (F,  -  L.)  F.  abuser,  to  use ,~L.  ahus-us,  pp.  of  abuti,  to  uh is««-*L.  d^,  away,  from,  heoce.  amiss; to  Qse.  So  alK)  <hs-use,  mis-use.  i/i-tue. iruse.  (F.*L.)  The  orig.  sense  was lue  up,'  to  go  through  thoroughly  ; ice  to  examine  lhorou[;hly  or  all  over, 'survey-,  the  only  difficulty  in  the  wuid in  its  chnnge  of  sense.  From  /er-, >ughly  ;  and  tue.    ^  Certain.
».  lo  seize  to  one's  own  use.  (F. »
F.  uJurficr.^L.  usurpare,  to  employ,
lire ;   also,  to   usurp,     p.  Clearly  He*
from  us-Hs,  use,  but  the  rest  of  the
19    obscure  ;    perhaps    from    utum
to  break  a  user,  hence  to  assert  a
to  [Key,  Roby) ;  others  suggest  usu-
r,  to  seize  lo  one's  own  use.
-----
Oppugn ;  see  FuAiliam.
Optative,  wishing.  vF.  — L)  Chiefly  as the  name  of  a  mood.  —  F.  ppfaii/.  — 1«  opta- tiuttx,  expressive  of  a  wish.  ■•  L.  optattts^ pp.  of  optart,  to  wi^b.  Allied  to  ap-isn, to  obtun ;  cf.  Skt  dp.  ap,  to  obtjun,  get. (VAP.)
adopt.  (L.)  L.  aJoptare,  to  adopt, choose.  — L.  ad,  to,  for;  iptart,  to  uish.
oopioua,  amule.  (F.  — U)  O.Y.copieus, ^Xjl.  c^^asus,  plentiful.  — 1>  ^/j'a,  plenty; pal  for^v-tf^  —  L.  rtf-(forrwm),  together; ^«  bsjc  mtp-^,  wealth.  Cf.  in^epia,  wont.
lonni
ORAL.
oopy.  (F.-L.^  M.  E. ance ;  the  mod.  sense  is  dae  to tiplication  of  an  original  by  meul — O.  F.  f^pit,  abundance;  ftlvH L.  f#^d.  plenty  (aboveV         ^|
office,  duly.    (F.-L.)      F.  ^ offidum.  duty  pKc-^oiaAM^a^Ma. contr.  from  optficiHm.^X^  ^i'»> of  opa,  wealth  ;  fiutrt.  to  do;| Der.  effi('fr,  F.  ojffUttr,  Low  ~ offie-i-CHS,  F.  cfficitux,  L.  o^
optimism,  the  doctrine the  best.  (L.>     From  L.  oftim' best;  with  suffix   -ism  (Gk. 0P'ti-PHus  is  a  supcrl,  form  fn (i.  c.  choice) ;  cf.  optart,  to
option,  choice.   vF.  — L.) L.  optiomm,  ace.  of  «//!«,  ch( to  L.  opfart,  to  wish  (above).
opment,  wealthy     (F.  — 1-> i!nf/.  — L.  opuUntui,  wc&lthy.  — L. of  «|/Vj,  uealth.     Cf.  Skt.  a^oi,  \ Optic,  relating  to  the  tight.    ( F.  optiqu€.  —  Gk,  orriffiii,  bell sight ;  ci.   t*T^Pt  a  spy.     Fi ow-  (for  0*-)  seen  in  Ionic  Sw~ seen,  Sip-ofiat,  I  shall  see;  cf.  t^ the  eye.     See  Sr«.     ( ^AK.)
autopsy,  [fCTSonal  ins]>ccti« iik.  a^mifia,  a  seeing  with  our's  c
—  Gk.  aur-*li,  self;  and  ^(t,  sight catoptric,  relating  tooplicaj  r
-----odd
1984:oDdir  flooruh  aa  a  flower.
7777:odding, idde;  frura  Irish  and  Gnel.  go^,  to  uod, "  slightly.  Ckarly  shewn  in  Irish  and 1.  gogiHuiUach,  gogglc-cycd.  having wandering  c>es,  from  ffig,  to  move  slightly, and  suil,  a 
9762:oddia,  the  bead.    (K.)    M.  £.  twiU,
```


## [2026-09-07T20:27:56.114Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== FSD oscillum ==\"; grep -n -o -E '.{80}oscillum.{200}' FSD_vol1.txt FSD_vol2.txt FSD_vol3.txt FSD_vol4.txt 2>/dev/null | head -4; echo \"== FSD oddi ==\"; grep -n -o -E '.{80}\\bodd[iaïr].{0,60}(third|point|number).{0,120}' FSD_vol1.txt FSD_vol2.txt FSD_vol3.txt FSD_vol4.txt 2>/dev/null | head -4; echo \"== WEB oscillum/oddi ==\"; grep -n -o -E '.{60}(oscillum|oddi,).{160}' WEB_vol1.txt | head -4",
 "description": "Grep Funk&Wagnalls and Webster"
}
```


### [2026-09-07T20:27:59.556Z] TOOL RESULT

```
== FSD oscillum ==
== FSD oddi ==
== WEB oscillum/oddi ==
```


## [2026-09-07T20:28:03.975Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for f in FSD_vol1.txt FSD_vol2.txt FSD_vol3.txt FSD_vol4.txt WEB_vol1.txt; do echo \"--- $f $(wc -c <$f)\"; head -c 300 $f | tr '\\n' ' '; echo; done",
 "description": "Check FSD/WEB coverage"
}
```


### [2026-09-07T20:28:05.262Z] TOOL RESULT

```
--- FSD_vol1.txt 16441388
FUNK  &   WAGNALLS New  Stand [Reg.  U.  S.  Pat.  02.] OF  THE Dictionary English  Language Upon  Original  Plans ml-cPT'V  p,j j   pOO-e Designed  to  Give,  in  Complete  and  Accurate  Statement,  in  the  Light  of  the  Most Recent  Advances  in  Knowledge,  in  the  Readiest  Form  for  Popu
--- FSD_vol2.txt 16801850
FUNK  &   WAGNALLS New  Standard  Dictionary [Reg.  U.  S.  Pat.  Ofi.l  ■   J OF  THE English  Language Upon  Original  Plans Designed  to  Give,  in  Complete  and  Accurate  Statement,  in  the  Light  of  the  Most Recent  Advances  in  Knowledge,  in  the  Readiest  Form  for  Popular  Use, t
--- FSD_vol3.txt 13277749
FUNK & WAGNALLS New Standard Dictionary (Re» U S P»t (Iff ) • O F T H K English Language Upon Oruunal Fi.ans DfsIGNKD ro CIlVK, JN CoMPIA I F and AcCURAIF SrAIF.MFNI, IN THF' LuJHr OF' I'HF' JVlosT RkCFNI' AdvaNCFS in KnoWI.F DtiF , in I'HF RfADIF'M' KoRM for RoPIILAR l^.SF, I'HF Or FHOGR APF
--- FSD_vol4.txt 16697862
GOVT.  COLLEGE,  LIBRfiRY KOTA  (Raj.) Students  can  retain  library  books  only  for  two weeks  at  the  most. FUNK  &   WAGNALLS New  Standard  Dictionary [Reg  U   S   Pat  Off  1   J OF  THE English  Lan^^uage Upon  Original  Plans Designed  to  Give,  in  Complete  and  Accurate  Statement,
--- WEB_vol1.txt 12198872
s š > f a ete Sy = ¥ P ay * i « t $ n-2024 nO Ti > J 2 < V u E- d Qs z rb HE Sir E Ce E wn ra 3 My ~ ‘Stock | 9 (9) IIIN p 5 EE Ce = > BP ss h iz = i n a, & eo x D Ay P E ERS l k SIN bo 78 3 3 (S (61d Ms “SSpy, n s AN’ H £ ei é or? ts | m É $ ) È N < : V x Ere 4 of v : O N Q ° l % >
```


## [2026-09-07T20:28:13.244Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== FSD oscillare ==\"; grep -l 'oscillare' FSD_vol*.txt; grep -n -o -E '.{100}oscillare.{200}' FSD_vol*.txt | head -4; echo \"== FSD 'oddi' ON ==\"; grep -n -o -E '.{120}(Icel\\.|ON\\.) odd[air].{150}' FSD_vol*.txt | head -4; echo \"== FSD os, oris usher ==\"; grep -n -o -E '.{100}ostiarius.{150}' FSD_vol*.txt | head -3",
 "description": "Grep FSD for oscillare, oddi, ostiarius"
}
```


### [2026-09-07T20:28:13.399Z] TOOL RESULT

```
== FSD oscillare ==
== FSD 'oddi' ON ==
== FSD os, oris usher ==
```


## [2026-09-07T20:28:26.698Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== HUB Zweig ==\"; grep -n -i 'zweig' HUB.txt | head -10; echo \"== HRN zih/zah ==\"; grep -n -o -E '.{0,60}(zih|zah|zdda|zajidan|zdjidan).{0,120}' HRN.txt | grep -i -E 'geb|quell|wasser|mutter|bogen|sehne' | head -10; echo \"== HUB zih ==\"; grep -n -o -E '.{0,60}zih.{0,120}' HUB.txt | head -8",
 "description": "Grep Hübschmann and Horn"
}
```


### [2026-09-07T20:28:31.282Z] TOOL RESULT

```
== HUB Zweig ==
365:82. Die Zuriickfiihrung vonistak 'Sch5ssling, junger Zweig
1926:Praes. xaram (Hafis ed. Rosenzweig I, p. 78, v. 11)
6054:H. 78; istOx 'Zweig* H. 82; isfand *Raute*, isnGsa *Niesen
8947:"^khumbha-?)'^ six *Bratspiess H. 762; sax *Zweig' = skr.
== HRN zih/zah ==
ugrep: error: error at position 107
n|zdjidan)(?:[^\n\x80-\xbf][\x80-\xbf]*){0,120}
                  exceeds complexity limits___/


== HUB zih ==
ugrep: error: error at position 80
[\x80-\xbf]*){0,120}
                    \___exceeds complexity limits
```


## [2026-09-07T20:28:36.593Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== HRN zih ==\"; grep -n 'zih\\b\\|zih ' HRN.txt | head -12; echo \"== HRN zdjidan/zddan gebären ==\"; grep -n -i 'gebären\\|gebiiren\\|geboren' HRN.txt | head -12; echo \"== HUB zih ==\"; grep -n 'zih' HUB.txt | head -10",
 "description": "Grep Horn/Hübschmann for zih"
}
```


### [2026-09-07T20:28:36.669Z] TOOL RESULT

```
== HRN zih ==
5975:677. zih 'Bogensehne*.
5979:kurd. zih 'Bogensehne*; af/. za-l^ bei. j%y (177).
5980:Urform von zih ist "^jtjaka-,
19702:zih 683.
== HRN zdjidan/zddan gebären ==
5709:645. xäden *gebären ; geboren werden*, 'Praes. zay-em,
5714:aw. [/'zan-, zayata gebären; geboren werden, us
5718:kurd. zain gebären ; af/. zez\edal geboren werden',
5719:zez\avul 'erzeugen*, s'opmZ 'gebären'; oss. -eäwclr// 'wachsou*,
5720:zayi (125); bei. zäyag, n. zay 'gebären, hervorbringen*
10136:aw. asna- angeboren, natürlich, eigen* (Geld n er,
== HUB zih ==
2478:zihglr *die Kerbe am Bogenende zur Befestigung der
2479:Sehne' = np. zihglr,
7316:gaoci^ra- = pers. Gdzihr^ ap. *gaucid^''a' = fwaid-^g
8169:zan *Weib* = gd. j^ni- 'Weib'; zih *Bogeusehne' =^ zd. skr.
```


## [2026-09-07T20:28:41.763Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '5705,5725p;5973,5985p' HRN.txt",
 "description": "Print Horn 645 zâdan and 677 zih"
}
```


### [2026-09-07T20:28:41.805Z] TOOL RESULT

```
ap. US' {ustasana-) 'hinauf; aw. us-, uz- 'heraus,
empor ; phlv. uz- (auch w/-, uö- geschrieben); ai. ud,
oss. 'S, -is (216), e- in oss. z[mänfin *zusammenrühren,
vermischen (133) ist unsicher.
645. xäden *gebären ; geboren werden*, 'Praes. zay-em,
zad 'Geburt' {-zad, mlrzä), zaj^ zaje 'Wöchnerin*,
zOq ') junges Huhn', zeh * Junges, Kind', zehdan 'Uterus*,
zehistän 'Fehlgeburt, Placenta' (AM.), jüd.-pers. TIM
(Salemann, Litbl. f. or. Phil. II, 81), zatjlden.
aw. [/'zan-, zayata gebären; geboren werden, us
zayfAte, zata-; phlv. zatan, zay(i)sn, zak (aw. zqda-,
y. 42, 5 b); ai. [/"^aw-, Jdyate, ^ki\ jfati- *6eburt'; arm.
ein 'Geburt', cnanim 'erzeugen' (H. No. 136).
kurd. zain gebären ; af/. zez\edal geboren werden',
zez\avul 'erzeugen*, s'opmZ 'gebären'; oss. -eäwclr// 'wachsou*,
zayi (125); bei. zäyag, n. zay 'gebären, hervorbringen*
(423), 'Za/t 'Sohn' aus "^zatk (418) ; wa/. yäz-am, sar.
zay -am,
646. {\)xär 'Klagen', zäri^ zäre^), zandefi.
ai. 3 l/^ar-, jdrate 'rauschen, schnattern, rufen*,
afy. Sarai 'klagen'; oss. d. zarw?, t. zarin singen'
zitternd' übersetzt — dazu s. aber Bartholomae,
Indog. Forssch. I, 191 Anm.).
677. zih 'Bogensehne*.
Käs. zeh, ze,
aw. jyd' 'Bogensehne; Sehne* (yt. 10, 70, Geldner,
KZ. 30, 514); ai. i^a-.
kurd. zih 'Bogensehne*; af/. za-l^ bei. j%y (177).
Urform von zih ist "^jtjaka-,
678. zehr 'Gift*, zehre 'Galle*.
phlv. zahr 'Gift* (Men.), arm. LW. zahr,
kurd. zahr, zäir, zur 'Gift' ; af/. bei. (297) LW. zahr,
np. zehre 'Galle' aus aw. *zartaka- ('gelb'), ^zad^raka-,
phlv. "^zahrak und identisch mit zehr 'Gift* nach
```


## [2026-09-07T20:28:54.908Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n 'زهدان\\|زهاب' MON_part1.txt MON_part2.txt | head -10",
 "description": "Grep Moin for zehdan/zahab"
}
```


### [2026-09-07T20:28:54.965Z] TOOL RESULT

```
MON_part2.txt:8910:کشتی که زهاب آب‌های کشتی دز آن جمع 
MON_part2.txt:12017:رحم؛ زهدان. (نط.) مجموع سازمان‌ها و 
MON_part2.txt:69042:مهبل: اه [ع.] (.) زهدان؛ بچه‌دان. 
MON_part2.txt:69043:دهانه زهدان ( که نره از آن عبور کند.) 
MON_part2.txt:76279:غلط. نشته؛ چیزهابی که انسان رابه حال 
MON_part2.txt:78768:چیزهابی نظیر دانه‌های معطر (هل» تجم 
MON_part2.txt:80662:بازی سپید پرواز می‌داد و از جیزهابی که 
MON_part1.txt:1524:زهدان؛ رحم 
MON_part1.txt:9723:ارحام: 2۳200 [ع.] 1( ج. رحم» زهدان‌ها. 
MON_part1.txt:21229:بج: لها (.) زهاب و پالایش آب و شراب و
```


## [2026-09-07T20:29:00.790Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n '^زه' MON_part1.txt | head -30",
 "description": "Grep Moin headwords starting zeh"
}
```


### [2026-09-07T20:29:00.852Z] TOOL RESULT

```
1484:زهات. 
1524:زهدان؛ رحم 
22176:زهر مار) بسیار خشمگین. بسیار اندوهناک. 
44573:زه کردن. (امص.) زایش؛ ج. یت 
51363:زه آن را بجای چرم از کهنه و لته سازند؛ 
72342:زه: ابوه بت ادات تسحسین؛ آفرین! 
72350:زه: 700 امتر. معر. زیق | (.) کنارة چیزی. زه 
72358:زهات: -.76 ,2211-20 [ع زه (زهدن) سّ آب 
72367:زهد ورزیدن» رغبت نکردن به دنیا. (امص.) 
72369:زهار؛ ۰۲ (.) آلت تناسل مرد با زن و 
72372:زهازه: 22-2-70 (صت.) ادات تحسین؛ 
72375:زه‌بند 
72384:زه‌بنكد: ۱-0( 7 (امر .) نوعی گردن‌نند. 
72385:زهتاب: 0-.2 [ - زه‌تاننده | (ص‌فا.) آنکه 
72397:زهدیات: 20۳-۱ [ع.] (ص‌نسب.) ج. 
72398:زهدیه؛ آنجه دربارهٌ زهد و پارسایی گفته و 
72401:زهر: 207 (.) ماده‌ای که جانداری را 
72416:زهر؛ ۲ [ع.] .( شکو فه درخت و کیاه؛ 
72420:زهراء: مه [ع. ف. زهرا] (ص.) موّنث 
72426:زهراگین: 2-0 (ص مر .) آمیخته به زهر» 
72429:زهر آلود؛ سمی. تلخ زننده. 
72431:زهرالود: 224 |- زهر آلوده ] (رص مف.) 
72434:زهراب: 2۳-0 [ع زمرآب - زهرابه | 
72441:زهر ابه: )2۸۲-۱2 [- زهر آت ] (امر.) 
72447:زهربار: 220۲-0۲ | - زهر بار نده] (رص‌فا.) 
72450:زهر ۳ ۰ 6(800)-1طه2 (امر .) نگاهی که 
72453:زهر حند: 01 .2 (امر.) خنده‌ای که از 
72456:زهرشناسی: ]-36086-.2 (حامص.) (بر.) 
72464:زهرناک: 1-.7 (ص مر .) زه رآ گین؛ سمی 
72467:زهسر ه. (6-)2201۸ (۱.) (سز.) بوستی است
```


## [2026-09-07T20:29:04.656Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '72336,72400p' MON_part1.txt",
 "description": "Print Moin zeh entries"
}
```


### [2026-09-07T20:29:04.716Z] TOOL RESULT

```
رود: 0 (.) بهر ه) قسمت؛ حصه. 

زویج: [27*3[- زویش] (.) نوعی خوراک 
اه "وه وی با کو تفه آکنده از 
پیه و گوشت 

زه: ابوه بت ادات تسحسین؛ آفرین! 
احسنت! خوشا! 

ره: 700 (امص.) زاییدن» زایش. تراوش اب 
از درز و لای چبزی. (.) نطفه. بجه» فر زند. 
ژه: 260 (.) چلة کمان» وتر. روده تاییده. 
تا 

زه: 700 امتر. معر. زیق | (.) کنارة چیزی. زه 
چشم: : حاشبه و کناره چشم. رت رشه و 
حاشیه و نوار و سجاف آن. زه گریبان: 
آرایش زری یا ابر یشمی گریبان. زه یکتایی: 
وعی از زه و آن رشته‌ای است ابریشمین که 
با تارهای زر و سیم تابیده به گرد آستین یا 
گر بان دوزند. 

زهات: -.76 ,2211-20 [ع زه (زهدن) سّ آب 
- زاب ] (امر.) آبی که از کنار رود» چشمه 
تالاب و غیره تراوش کند. جایی که آب از 
آنجا جوشدء خواه خاک و خواه سنگک 
باشد؛ موضم چشمه. آبسی که قعرش پیدا 
نباشد. چشمه‌ای که بیوسته روان باشد و 
هرگز نایستد. 

رهادت: ام 2202 [ع. زرهسادة] (مسصل.) 
زهد ورزیدن» رغبت نکردن به دنیا. (امص.) 
بی‌میلی به جهان» پرهیزگاری» پارسایی. 
زهار؛ ۰۲ (.) آلت تناسل مرد با زن و 
حوالی آن که موی از آن روبد» شر مگاه. 
موی زهار: موهایی که روی زهار روید. 
زهازه: 22-2-70 (صت.) ادات تحسین؛ 


زه‌بند 


فر هنک فاررسی معین 


۷ «۷ 


زه‌بنكد: ۱-0( 7 (امر .) نوعی گردن‌نند. 
زهتاب: 0-.2 [ - زه‌تاننده | (ص‌فا.) آنکه 
شغلش تابیدن زه و تهیه کردن رشته تافته از 
رودة گوسفند و حیوانات دیگر است. 
رهمسد: 7001 [ع.] (امسص.) بارسایی 
برهی زگاری» اعراض از دنیا. 

رهدان: 200-1 (امر .) جایی در شکم مادر 
که بچه در آن قرار دار د بجه‌دان» رم 
رهدان نهادن: 7.0 (مص‌ل.) ( کد.) 
عاجز شدن در جنگ. (کد.) اعتراف کردن 
بر کم فهمی و سستی خود. 

زهدیات: 20۳-۱ [ع.] (ص‌نسب.) ج. 
زهدیه؛ آنجه دربارهٌ زهد و پارسایی گفته و 
نو شته شود.
```


## [2026-09-07T20:29:30.185Z] TOOL CALL #79: WebFetch

```json
{
 "url": "https://www.wisdomlib.org/definition/adga",
 "prompt": "Give the Monier-Williams and other dictionary definitions of Sanskrit adga (अद्ग), including the Atharvaveda attestation."
}
```


### [2026-09-07T20:29:36.635Z] TOOL RESULT

```
# Sanskrit Adga (अद्ग) - Dictionary Definitions

## Monier-Williams Definition
According to Monier-Williams, adga is "a sacrificial cake (puroḍāśa) made of rice" derived from the root √ad, with the Uṇādi suffix gan. The entry also notes "a cane (?)" attested in the Atharvaveda i, 27, 3.

## Other Dictionary Sources

**Apte's Dictionary:** Identifies adga as "A sacrificial oblation called पुरोडाश (puroḍāśa)" with the Atharvaveda reference at 1.27.3.

**Shabda-Sagara:** Defines it as "Oiled butter" (masculine noun).

**Cappeller:** Lists the meaning as "stalk, stem, cane" (masculine).

**Böhtlingk and Roth:** Provides two interpretations—"roughly a reed stalk, stem" or "a sacrificial cake baked from rice flour."

The primary attestation comes from the **Atharvaveda 1.27.3**, though scholarly sources debate whether the term refers to a sacrificial food item or a plant stem.
```


## [2026-09-07T20:29:51.555Z] TOOL CALL #80: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%D8%B2%D9%87%D8%AF%D8%A7%D9%86|page 378, entry 0 node 2: Persian zehdan 'womb' = zeh + -dan\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%83%C3%A9h%E2%82%81os|page 378, entry 0 root: PIE *h1oh3s 'mouth', descendants Lat os, Av ah, Skt as, Hitt ais\" \\\n \"https://en.wiktionary.org/wiki/%D8%B2%D9%87|page 378, entry 0 node 2: Persian zeh etymologies (birth < PIE *genh1-; seepage < MP *zah)\" \\\n \"https://www.etymonline.com/word/odd|page 378, entry 5 nodes 4-5: English odd < ON oddi < PGmc *uzdaz < PIE *uzdho-, not from 'branch' root\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/uzdaz|page 378, entry 5 node 4: Kroonen on PGmc *uzdaz 'sharp point' < *ud-s + *dheh1-\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%83%C3%B3sdos|page 378, entry 5 root: PIE *h3osdos 'branch', PII *Hadzgas, MP azg as uncertain cognate\" \\\n \"https://en.wiktionary.org/wiki/%E1%BD%84%CF%83%CF%87%CE%B7|page 378, entry 5 root: Greek oskhe/oskhos, Beekes Pre-Greek\" \\\n \"https://www.etymonline.com/word/oscillate|page 378, entry 0 nodes 3-4: Latin oscillum 'little mask of Bacchus' < os\" \\\n \"https://www.wisdomlib.org/definition/adga|page 378, entry 5 node 3: Sanskrit adga 'stalk, cane (?)' AV 1.27.3, MW derives from root ad-\" ; do\n url=\"${u%%|*}\"; note=\"${u##*|}\"; python3 tools/fetch_source.py \"$url\" --note \"$note\" 2>&1 | tail -2; done",
 "description": "Archive web sources"
}
```


### [2026-09-07T20:29:56.006Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/077903743e6b7287.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0bf29c51b8278c76.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f021be6c3bf5c8e0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8a2e2593c04f969d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d8a471abb315c38e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/548622dc9b3e1d06.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/bafde3f3e051b312.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0a3a255f8587a9a4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e682d85112df55fc.txt
```


## [2026-09-07T20:30:04.661Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; ls site/pages/378.jpg 2>/dev/null && echo exists; pdftoppm -f 378 -l 378 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg378 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg378.png",
 "description": "Render PDF page 378"
}
```


### [2026-09-07T20:30:06.624Z] TOOL RESULT

```
site/pages/378.jpg
exists
-rw-rw-r-- 1 sfmqrb sfmqrb 67102 Sep  7 16:30 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg378.png
```


## [2026-09-07T20:30:10.240Z] TOOL CALL #82: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg378.png"
}
```


### [2026-09-07T20:30:10.719Z] TOOL RESULT

```

```


## [2026-09-07T20:30:10.716Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-07T20:30:31.347Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -o -E '.{80}(ous- ?: ?[əe9]us-|Mündung, Rand|9us-t[āa]).{400}' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -4; echo \"---\"; grep -n 'Mündung' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -10",
 "description": "Find Walde-Pokorny I 168 ous- Mund"
}
```


### [2026-09-07T20:30:32.670Z] TOOL RESULT

```
---
```


## [2026-09-07T20:30:37.996Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i 'Miindung\\|Mvindung\\|Mund, Miind\\|„Mund' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -12; echo \"== aosta in WLD ==\"; grep -n 'aosta\\|ao§ta\\|aostha\\|ostha' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -8",
 "description": "WLD grep with OCR variants"
}
```


### [2026-09-07T20:30:38.063Z] TOOL RESULT

```
1326:aus- n. „Ohr, Gehor“, kons. St. (zum -s vgl. idg. o\u\s „Mund“, *nas 
1372:„Mund“ anzunehmen. 
3785:ana-h „Hauch, Atem“ and-h (vielleicht ,,Hauch“ oder „Mund, Kase“, ana- 
3786:nam „Mund, Maul, Gesicht“ mit ind. Vriddhi; „Mund“ als „Atmer, das 
4563:*an-s-ti- zugrunde liege. gvgg nicht zu ai. ananam „Mund, Antlitz“ 
10627:„Niere“, lysto „Wade“, usta „Mund“) in wruss. jal'ity ,,Hoden“, serb. alt 
10825:ous- : ens- „Mund, Miindung, Rand". 
10827:Auf idg. *uus gehen zuriick ai. u-h „Mund“ (vgl. asyam n. „Mund, Maul. 
10830:Lat. os, oris „Mund. Antlitz, Offnung"; ir. a ,,Mund“ (*6s). 
10843:Altn. oss m. „Flufimiindung“ geht auf germ. *osaz zuriick, hierzu ags. 
10868:aksl. usta „Mund : ' (usw. Trautmann 19). Slav, nslsje n. „Miindung“ ist an- 
10872:(Trautmann aaO.); apr. austo „Mund“ (n. plur.?; akk. sg. uustin). lit. dus- 
== aosta in WLD ==
47590:Praes.-St. Oraois- (Oraosta) „zur Reife, Yollendung, Yollkommenheit ge-
```


## [2026-09-07T20:30:41.753Z] TOOL CALL #85: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '10820,10880p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt",
 "description": "Print WP I 168 ous- entry"
}
```


### [2026-09-07T20:30:41.809Z] TOOL RESULT

```
ous- : 3us- 


ous- : ens- „Mund, Miindung, Rand". 

Auf idg. *uus gehen zuriick ai. u-h „Mund“ (vgl. asyam n. „Mund, Maul. 
Offnung einer Wunde"). av. ah- ds. 

Lat. os, oris „Mund. Antlitz, Offnung"; ir. a ,,Mund“ (*6s). 

Dazu u-Ableitung ved. asayd „von Mund zu Mund“ (instr.), lat. ora 
„Rand, Saum, Grenze, bes. Meereskiiste“ (dagegen gr. Coa kaum hierher, 
vielmehr „Saum des Ivleides" nach Sommer Gr. Lautst. 1 S f. als „Besatz 
mit Schaffell“ gleich coa „Schaffell“. Ygl. Bezzenberger-Fick BB. 6, 236). 
Zu lat. ora gehort sicherlioh lat. coram adv. (u. prap.) „angesiehts, in 
Gegenwart, vor". aus com- und einer Form des n-Stammes entstanden. 
Dann ware an einen Akk. (Yanicek 33, Lindsay-Nohl 669, Brugmann 
KG. 451) und nicht an einen Instr. (vgl. Stolz HG. I 132 f. ) zu denken 
Moglich ware auch Yaehbildung von palam, dam (Breal Msl. 15, 138 f.) 
aus *core = *co>n ore. 

Altn. oss m. „Flufimiindung“ geht auf germ. *osaz zuriick, hierzu ags. 
dr, dra „Rand, Anfang“ (vgl. J. Schmidt, Plurbild. 117). Aus ags. dr ist 
mir. or „ora, margo, linea“, acvmr. dr ds. entlehnt. (Bugge KZ. 19, 405 
verteidigt Ansatz germ. *ostas > altn. ass;. Die schwache Stufe idg. *ous- 
erweisen : alb. one ,,Seite, Saum. Ufer, Borte“ (aus *aasna, G. Meyer 
Alb. \Yb. 11) gr. ion. ,-ra oiji'ov, att. rtaoeiu, lesb. naoava faus *-aus-ia mit 
Dehnung des *aus- zu *aus- in der Ivomposition, vgl. J. Schmidt Plurbild. 
407 a). wenn nicht die YYorter zu idg. aus- „Obr, Geh6r“ zu ziehen sind 
(s. sclion Pott Et. Fo. I 1 , 138). Hierher lat. aureae. Oreae ,.Zugel“. Hierzu 
aureax und auriya, drhja „Wagenlenker‘\ Letzteres Wort enthalt -iya zu 
ago und nicht ctwa jni/uni, wie Yanicek 226 will. (Vgl. Yf. LEWb. 2 75). 

Fick I 4 17. 174, 372, II 4 23. Ill 4 29, Falk-Torp 803 (os II; vgl. 
1525;, 1420 (or subst.: vgl. 15S2 , J. Schmidt PI. 117, 221, 407, Yani- 
cek 32 f, Yf. LEWb. 2 s. os. cdscun, auriga. Wiedemann Prat. 37; aas- 
rulum . dscuhun ,.Miindchen, Ivufi' £ , bei denen man (s. spiiter auch austimu, 
osttuni) nicht ctwa an idg. Doppelformen mit *dus : *aus zu denken hat. 
Ausgehen mull man elier von '"on- (Meyer-Liibke ZfromPhil. 25, 357) als 
von *rn- (Skutseh. Rom. Jahresber. 5, 1. 62). da vulgares 0 unterstiitzt 
durch os fur an in die Hochsprache eingedrungen sein kann. Ob bei 
alien genannten Wortern mit d- : cm- Wechsel die Lb'stufe *au- anzunehmen 
ist, bleibt allerdings zweifelhaft. 

t-Ableitungen sind ai. ustliah- „Lippe“, av. aoifa- aostra- ds. {*3 us-), lat. 
(iiistunn (inschr.) u. Ostium (cm : o s. o.) ,,Flu6mundung‘ ! (— slav. *usibje): 
aksl. usta „Mund : ' (usw. Trautmann 19). Slav, nslsje n. „Miindung“ ist an- 
zusetzen nach bulg. ustijc, russ. nslbje usw.: vgl. aksl. ustwia slov. listno 
„Lippe“. aksl. nstiti ( naustiti ) „bewegon, anregen, iiberreden“. Unsicher, 
wenn auch wahrscheinlich ist Zugeborigkeit von aksl. uzcia usw. „Zaum“ 
(Trautmann aaO.); apr. austo „Mund“ (n. plur.?; akk. sg. uustin). lit. dus- 
rioti ,,schwatzen, munkeln“, left, afisdt „schwatzen“. Ablautend lit. uostas 
in. „FluBmiindung, IIatf“, lett. ousts in., iwsta f. ,,Hafen“. 

Die Zugehorigkeit von altn. eyrr f. „Sandbank, sandiger Strand 1 ' zu dieser 
Wurzel (z. B. Kretschmer KZ. 31, 452) ist nicht sicher (Falk-Torp 1420 
(0r subst. 1582, Fick III 4 6b Abzulehnen ist die Yermutung Kretschmers
```


## [2026-09-07T20:31:45.847Z] TOOL CALL #86: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== LEW size/head ==\"; wc -c LEW_1910.txt LAT.txt; echo \"== LEW oscill ==\"; grep -n -i -o -E '.{60}oscill.{200}' LEW_1910.txt | head -4; echo \"== LAT oscill ==\"; grep -n -i -o -E '.{60}oscill.{200}' LAT.txt | head -4; echo \"== LEW os oris ==\"; grep -n -o -E 'os,? -?ōris.{0,200}|ōs, ōris.{0,200}' LEW_1910.txt | head -4; echo \"== LEW 'Mund' ==\"; grep -n -o -E '.{60}Mund.{0,160}' LEW_1910.txt | head -6",
 "description": "Grep Latin etymological dictionaries"
}
```


### [2026-09-07T20:31:47.218Z] TOOL RESULT

```
== LEW size/head ==
 627390 LEW_1910.txt
4618386 LAT.txt
5245776 total
== LEW oscill ==
== LAT oscill ==
== LEW os oris ==
== LEW 'Mund' ==
12054:n IT 119 muffeln IT 128 muh IT 117 Muhme IT 21 mulsch I 508 Mund Il 73 miintschi (schweiz.) IT 227 _. Murmel II 42 murmeln IT 131 murren IT 131 Mus II 100 Muskel II 132 mup IT 56 Muster II 110 Mut IT 115 Mutt IIT 99 Mutterso
```


## [2026-09-07T20:31:55.062Z] TOOL CALL #87: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== LAT ostium ==\"; grep -n -o -E '.{80}ostium.{200}' LAT.txt | head -3; echo \"== LAT 'bouche' os ==\"; grep -n -o -E '.{0,60}(os,? ōris|ōs, ōris|os \\(gén)\\..{0,200}' LAT.txt | head -4; echo \"== LAT oris bouche ==\"; grep -n -o -E '.{80}bouche.{160}' LAT.txt | head -4",
 "description": "Grep Ernout-Meillet for os/ostium"
}
```


### [2026-09-07T20:31:58.950Z] TOOL RESULT

```
== LAT ostium ==
== LAT 'bouche' os ==
ugrep: error: error at position 112
is|os \(gén)\.(?:[^\n\x80-\xbf][\x80-\xbf]*){0,200}
                      exceeds complexity limits___/


== LAT oris bouche ==
```


## [2026-09-07T20:32:02.900Z] TOOL CALL #88: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; head -c 600 LAT.txt | tr '\\n' ' '; echo; echo \"---\"; grep -c 'bouche' LAT.txt; grep -c 'ostium' LAT.txt; grep -c 'oscill' LAT.txt; grep -c 'Mund' LAT.txt",
 "description": "Inspect LAT.txt content"
}
```


### [2026-09-07T20:32:03.002Z] TOOL RESULT

```
DICTIONNAIRE ETYMOLOGIQUE DE LA LANGUE LATINE HISTOIRE DES MOTS PAR A. ERNOUT Membre de 1'Inatilut Profeweur au College de Frmnce ® T f A. MEILLET Membre de 1’lnstitut Profrsneur au Collige de Fraure TROISlfcME fiDITION RBVUB, CORRIGEB KT AUGMENTEB d’UN INDEX PARIS I. TRRAIRIF. G KLINCKSffiCK 11, RUE DE ULLE, ii i95iAVERTISS EMENT On s'est proposA ici de prAsenter un exposA historique du vocabulaire latin. Les deux auteurs du livre se sont partagA la tftche de manifere inAgale. M. A. Ernout a traitA de ce que l'on peut connaitre par 1'6tude des textes. C'est lui qui est resjonsable de to
---
54
18
5
6
```


## [2026-09-07T20:32:06.471Z] TOOL CALL #89: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n 'oscill' LAT.txt | head -6; echo \"-----\"; grep -n 'ostium' LAT.txt | head -8",
 "description": "Locate oscill/ostium lines in LAT"
}
```


### [2026-09-07T20:32:06.546Z] TOOL RESULT

```
2103:tical oscille dans 1 'agina); nn ex. dans P 4 tr., 61, egi, agindui. De
11854:riens et lea glossateura, cillere: mouere, pour expliquer oscillum,
39203:Glose obscure dans P.F.149,5!.: moscillis Cato (lnc.33) pro paruis
44168:oscillum, »•! n. :. diminutif de Bs, Bsculum. Deux sena, le p reni er
44175:laeta, tibique | oscilla ex alta suspendunt mollia pinu.
-----
9616:b) -capas,-capus: hosticapas: hostium captor, P.F.91,5, et hosti-,
19737:agere alqn extorrem ab solo patrio ac dis Penatibus in hostium urbem.
20192:sunt desistunt et in hostium numerum se conferunt. L'emploi transitif
21462:festra, ostium minusculum in sacrario, Macr., 3,13,8, P.F.80,37, dont
22737:tator astat usque ad ostium-, fl&gitdtiO', dif-, ef-, refl&gitU (Catul.
24197:T.L.6,13,1, multitudo hostium nulli rei praeterquam numero freta) est
28668:(comme ciuilis), hostilitas (Tert.); compos^s: hosticapas "hostium
28675:M.L.4435. Cf.S^-Avit, p.3,1 tu praecedis cateruas hostium (= militum
```


## [2026-09-07T20:32:09.672Z] TOOL CALL #90: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '44160,44200p' LAT.txt",
 "description": "Print Ernout-Meillet oscillum entry"
}
```


### [2026-09-07T20:32:09.735Z] TOOL RESULT

```
- 834 ~
cette leyon est appuy 4 e par u jen de sots entre auscultSre et aus-
culdri; cf. Bstium, austium), diff 4 rent far 1 'enploi de SsculB, osculStio
qai, dans la 1. n 4 di cale, onj servi 4 . tradnire avocoro(iW> avacrroptaxn c.
A Bsculor se fattachent Bs culBbundus et les compos 4 s expressifs ad-,
dg~, ex-, per-osculor, 4 vit 4 s par la langue classi que» Sur la diff 4 -
rence entre Bsculum et bSsium, sSuium, v. ces nots. — Ancien, usuel,
classique» Non rosan. v
oscillum, »•! n. :. diminutif de Bs, Bsculum. Deux sena, le p reni er
se rapportant au sens de Os "bouche, orifice", 1 'autre A celui de
Bs "visage", i # petite cavit 4 au nilieu des 14 gunineuses, d*oA s' 4 lance
le gene (Colum.); a" petit n asque (*= oroptaxtOv, 7 tpoow 7 ietov), surtout
de Bacchus, qu'on suspendait aux arbres, notannent dans les vignobles,
de manibre qu'ils fussent agit 4 s par le vent. Cf.Vg.G.a,387sqq», oraque
corticibus sumunt horrenda cauatis, | et te, Bacche, uocant per canina
laeta, tibique | oscilla ex alta suspendunt mollia pinu.
De ce second sens d 4 rive SscillB, -Bs "se balancer (comae les
nasques)", et BscillBtiB.
os ( oss , puis Bs), ossis n. (doublet dssum, cf.Charis., GLK I 139,3,
conservd dans les 1 . ronanes, cf.M.L.6114; et ossu, usitd surtout au
pl» ossua, cf»Charis, ibid. 139,4) : os. — Attestd de tout tenps; pan—
ronan.
D 4 riv 4 s et conposds: i° de *ossosseus-, ossiculum dininutif, tech-
nique ou populaire avec valeur affective, et ses d 4 riv 4 s ossiculStim
(Caec.), ossiculBris (V 4 g.); ossGsus-, ossifragus dont ddrive le non
de "l f orfraie", H.L.6113 (avec un a?); QssipBgina "ddesse qui raf~
fernit les os dea enfants" (Ara.3,30); ossilSgo "tunepr dure (sen-
blable A tm os) ", ossilegus, ossilegium traductione de OCTroXoyoc,
oortoXoyiov; exBs (6 Lucr. 3,73:1.), -ossis (cf. ops), d'oh exossB,-Bs;
3 de ossu —: ossuSrius {—a Sila) et le n» ossuBrium "ossuaire"; os—
suBsus-, os suculum autre forne de ossiculum (cf. geni- et genuculum).
• L'iranien offre la forne du non de l'"os", sans aucun 4largisseaeat:
av. astpm (g 4 n. pl. )j azdiblS, azdebis (c.-A-d. azdb fi instr.pl.), «t
le sanskrit la n$me forne avec un 4 largissenent i/n: dsthi (non.acc.
sg.), asthndh (g 4 n. abi. sg.). Le grec a un d 4 riv 4 th 4 natique odreov;
hitt. ha$t—ai. Le not affecte en-partie des formes populaires ain~
si qu*il ressort du t,h de skr. dsthi et du k— pr 4 fixe dans v.sl. kosti
(pass 4 au f 4 ninin -sous i'influence du non.plur. kosti). TJn traitenent
~ 5 s~ de rst- dans 1 at. os (oss), ossis ne se ret.rouverait nulle part
ailleuTs; il ne reste donc d'autre hypothbse que de partir d’un ancien
oss— et d'adnettre que —t— ou —th— ne sont pas des 4 l 4 nents essentiels
```


## [2026-09-07T20:32:21.909Z] TOOL CALL #91: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -o -E '.{0,80}(orifice|bouche, ?visage|\"bouche\").{0,220}' LAT.txt | sed -n '1,12p'",
 "description": "Find Ernout-Meillet os mouth entry"
}
```


### [2026-09-07T20:32:26.292Z] TOOL RESULT

```
ugrep: error: error at position 111
sage|"bouche")(?:[^\n\x80-\xbf][\x80-\xbf]*){0,220}
                      exceeds complexity limits___/
```


## [2026-09-07T20:32:29.506Z] TOOL CALL #92: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n 'bouche' LAT.txt | sed -n '1,20p'",
 "description": "List bouche lines"
}
```


### [2026-09-07T20:32:29.555Z] TOOL RESULT

```
3764:representee la bouche close, un doigt sur les levres "ore obligato ob-
4440:met dans la bouche d'esclave3 ou d 1 affranchis. Se conjugue pronomina—
7848:bucca, -ae f.: bouche; synonyae faailier de os. Eaploy6 au pl.,
7854:Derives: buccula £. : 1° bouchee; joues (au pl.); 3 ° mentonnibre decasque
7857:(Pl .), buccosus (Gloss.): joufflu; buccella (b. lat.): 1° bouchee, miette;
7863:parasituli ; bucco, -onis m.(et buccus); grande bouche, bavard, sot;
18167:- Sur obdUrdre "boucher" du peut-fetre k une confusion tardive avec
19303:mis dans la bouche des esclayes, e.g. Pl., Am.453 (c'est Sosie qui
20659:contre 1’autre, je bouche" va bien pour le sens, aais se heurte au
25669:gin (geno) "bouche", gall. gen "joue, aenton", got.kinnus "aAchoire,gener
27103:gula, -ae f.: partie de la bouche par laqnelle on avale, gosier,
27104:con, et anssi dans la 1 . populaire, "bouche" (= 5 s; cf. Pl. Au.303-3,
28055:de la bouche; de IA "rester bouche bee" (devant quelqu'un ou quelque
28059:D^riv^s et conposes: hi 5 tus,-Qs m.: ouverture (de la bouche); fente,
28062:et Gargil.); hisco: s'ouvrir, ouyrir la bouche; dehiscS (Varr.);
28067:hiulcus , cf, peto, petulans et petulcus', in-hio,-Ss: etre bouche bee
28071:et a serbe zjhm, zj&ti "ouvrir la bouche" (v.sl .z$jy "je suis beant"
28073:beant" et gewSn "ouvrir la bouche toute grande") et hiscO peut-etre
28075:"etre b^ant", r.al.zintp, zinpti "ouvrir la bouche, devenir b^ant".
30973:Plaute, Am.475 (pour designer du reste Amphitryon et dans la bouche
```


## [2026-09-07T20:32:35.752Z] TOOL CALL #93: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n 'Bs, Bris\\|os, oris\\|Bs (Bris' LAT.txt | head -5; grep -n -o 'Bs, .\\{0,180\\}' LAT.txt | sed -n '1,10p'",
 "description": "Find os oris in LAT"
}
```


### [2026-09-07T20:32:37.121Z] TOOL RESULT

```
21524:Bs, et qui plus tard fut identifide k Junon. Toutefois
44168:Bs, Bsculum. Deux sena, le p reni er
58979:Bs, solitus sum, solSre (pft.solut arch., Cat., Enn., cf.
59953:Bs, -*dul (senlement dans. S^-Ang.), -•Sre: briller,
59983:Bs, spopondi, spOnsum, spondBre: prendre nn engagenent
```


## [2026-09-07T20:32:42.601Z] AGENT

Now I'll write the verification file.


## [2026-09-07T20:40:35.841Z] TOOL CALL #94: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-378.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\n\ne0 = {\n \"entry\": 0,\n \"root\": \"Ôus 2, Ôs, Aus 3\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *h₁óh₃s (n.) 'mouth' — in Pokorny's notation '1. ōus- : əus- \\\"Mund, Mündung, Rand\\\"', with the t-derivative *əus-t- 'lip' and *əus-tiiom 'river-mouth, door' (Pokorny 784-785; Watkins *ōs-)\",\n \"note\": \"The root is genuine, the language label is right and the gloss 'mouth, lip' is right. Pokorny 784 (POK_03.txt leaf 18, the printed number 784 stands in the middle of the article) reads: '1. ōus- : əus- \\\"Mund, Mündung, Rand\\\"; əus-tā \\\"Lippe\\\", əus-tiiom \\\"Mündung\\\". Auf idg. *ōus gehen zurück: ai. ā-h n. \\\"Mund\\\" …, av. āh-, ārədhan- ds.; lat. ōs, ōris \\\"Mund, Antlitz, Rand, Ufer\\\"', and on 785 't-Ableitungen sind ai. ōṣṭha- m. n. \\\"Lippe\\\"; av. aošta-, aoštra- ds. (*əus-), lat. ōstium \\\"Eingang, Flußmündung\\\"'. Walde-Pokorny I 168-169 is the same article verbatim, and Watkins/AHD has 'ōs-. Mouth. … [Pok. 1. ōus- 784.]' — so Nourai's own POK:784 is exactly on target and the AHD reference is the modern standard for the same claim. Nourai's triple headword 'Ôus 2, Ôs, Aus 3' reproduces the ablaut pair *ōus- : *əus- plus the Latin shape, and matches Buck's formulation at 4.24 MOUTH (p. 228): 'IE *o(u)s-, *aus-'. The '2' is Nourai's own numbering (Pokorny numbers this root 1. ōus- and reserves 2. ous- for 'ear'); this is a book-internal convention, not an error. Two modern caveats, neither affecting the chart: (a) the laryngealist reconstruction is *h₁óh₃s, an s-stem noun rather than a verbal root, and the placement of the laryngeals is debated (*h₁éh₃-s, *h₁óh₁-s all proposed); (b) Hittite aiš, gen. iššaš points to a parallel *ais-, which Buck and Pokorny both flag. What is NOT in Pokorny, WP, Watkins, Klein or Buck is the whole 'zā-' half of Nourai's Avestan box — see node #1.\",\n \"note_fa\": \"ریشهٔ هندواروپایی آغازین *h₁óh₃s «دهان» (در نگارش پوکورنی *ōus- : *əus- «دهان، دهانه، کناره») ریشه‌ای شناخته و پذیرفته است؛ برچسب زبانی و معنای «دهان، لب» در نمودار نورایی درست است. پوکورنی در ص ۷۸۴ می‌آورد: «*ōus- : *əus- \\\"Mund, Mündung, Rand\\\"؛ *əus-tā \\\"Lippe\\\"» و سنسکریت ā́s، اوستایی āh- و لاتینی ōs, ōris را زیر آن می‌گذارد، و در ص ۷۸۵ صورت‌های پسوند -t را: سنسکریت óṣṭha- و اوستایی aošta-، aoštra- «لب». والده-پوکورنی (ج ۱ ص ۱۶۸–۱۶۹) همان مقاله است و واتکینز نیز ذیل *ōs- به همان ص ۷۸۴ پوکورنی ارجاع می‌دهد؛ پس ارجاع خودِ نورایی (POK:784) دقیقاً درست است. صورت سه‌گانهٔ سرواژه (Ôus/Ôs/Aus) همان جفتِ آواگردِ *ōus- : *əus- است و با نوشتهٔ باک (ص ۲۲۸) «IE *o(u)s-, *aus-» می‌خواند؛ شمارهٔ «۲» شمارهٔ درون‌کتابی نورایی است، نه خطا. دو نکتهٔ احتیاطی: بازسازی امروزی این واژه را ستاکِ اسمیِ s-دار *h₁óh₃s می‌داند نه ریشهٔ فعلی، و جای واکِ حنجری‌ها مورد بحث است؛ و هیتی aiš بر ستاکِ همسانِ *ais- دلالت دارد. آنچه در هیچ‌یک از این منابع نیست، نیمهٔ «zā-» جعبهٔ اوستایی نورایی است (بنگرید به گرهٔ ۱).\",\n \"sources\": [\n   W + \"Reconstruction:Proto-Indo-European/h₃éh₁os\",\n ],\n \"ref_check\": [\n   {\"ref\": \"POK:784\", \"status\": \"supports\",\n    \"note\": \"POK_03.txt leaf 18 (printed 784 marked inline): '1. ōus- : əus- \\\"Mund, Mündung, Rand\\\"; əus-tā \\\"Lippe\\\", əus-tiiom \\\"Mündung\\\". Auf idg. *ōus gehen zurück: ai. ā-h n. \\\"Mund\\\" …, av. āh-, ārədhan- ds.; lat. ōs, ōris \\\"Mund, Antlitz, Rand, Ufer\\\"'. Exactly the root, label and gloss of the chart. Located with: awk 'BEGIN{RS=\\\"\\\\f\\\"} NR>=18&&NR<=21' POK_03.txt.\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. I 168-169 (WLD_Bd1_1930_dli_70244_djvu.txt line 10825)\", \"stance\": \"supports\",\n    \"note\": \"'ous- : əus- \\\"Mund, Mündung, Rand\\\". Auf idg. *ōus gehen zurück ai. ā-h \\\"Mund\\\" …, av. ah- ds. Lat. os, oris \\\"Mund, Antlitz, Öffnung\\\" … t-Ableitungen sind ai. uṣṭhaḥ \\\"Lippe\\\", av. aošta- aoštra- ds. (*əus-), lat. ostium … \\\"Flußmündung\\\"'. Pokorny's source article; identical content.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. ōs- (AHD_watkins1985.txt line 812)\", \"stance\": \"supports\",\n    \"note\": \"'ōs-. Mouth. 1. Latin ōs (stem ōr-), mouth, face, orifice, and derivative ōstium (< suffixed form *ōs-to-), door: ORAL, OS1, OSCULATE, OSCULUM, OSTIARY, OSTIUM, USHER; INOSCULATE, ORIFICE, ORINASAL, OROTUND, OSCITANCY, PERORAL. … [Pok. 1. ōus- 784.]' — confirms both the root and Nourai's own page reference.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 4.24 MOUTH, p. 228 (SYN.txt leaf 265)\", \"stance\": \"supports\",\n    \"note\": \"'1. IE *o(u)s-, *aus-. Walde-P. 1.168. … Lat. ōs (also ōstium \\\"door, entrance, river-mouth\\\", ōra \\\"edge, coast\\\"); … Skt. ās-, āsan-, āsya-, Av. āh- (also Skt. oṣṭha-, Av. aošta- \\\"lip\\\"). But Hitt. ais, gen. issas \\\"mouth\\\" … points to a parallel *ais-.'\"},\n   {\"src\": \"KLN\", \"where\": \"p. 1091 s.v. 'oral' (KLN_1966.txt leaf 583)\", \"stance\": \"supports\",\n    \"note\": \"'oral, adj. — Formed with adj. suff. -al fr. L. os, gen. oris, \\\"mouth, face; opening, entrance, orifice\\\", fr. *ous-, whence the collective noun ora … cogn. with OI. āh, as-an, \\\"mouth\\\", āsyam, \\\"mouth; opening\\\", Avestic ah-, \\\"mouth\\\", Hitt. aish (gen. ishash), Mir. a, \\\"mouth\\\", ON. oss, \\\"mouth of a river\\\" … Cp. coram, orifice, orle, orotund, oscitancy, ostiary, ostiole, usher, Auriga, vera.'\"},\n   {\"src\": \"IEC\", \"where\": \"Mann p. 168 area — searched IEC.txt for 'ous-', 'ōus-'\", \"stance\": \"silent\",\n    \"note\": \"Mann's dictionary has no lemma matching the 'mouth' root under a spelling I could find (grep for 'ous-', 'ōus', 'ausos' in IEC.txt gave only unrelated 'aus-' entries); recorded as silent, not as disagreement.\"}\n ],\n \"nodes\": []\n}\n\ne0[\"nodes\"].append({\n \"id\": 1,\n \"lang\": \"Avestan\",\n \"words\": \"âh : mouth ; aošta, aoštra : lip ; uz-ah, zâ 2 : push out of opening, give birth ☞Ud 1 ; zâ-dhana : child holder, womb ☞Dhě 2 ; zâ-âp : spring, river ☞Ab 1\",\n \"verdict\": \"disputed\",\n \"derivation\": \"The box mixes two unrelated Iranian families. (a) āh- 'mouth' is real and belongs here: Bartholomae AiW s.v. 'j., g. ā̊h-, g. ¹āh- n. \\\"Mund\\\"' (BRT.txt line 7567, Y. 31.3, Y. 28.11), the direct reflex of *h₁óh₃s beside Skt. ā́s, Lat. ōs; beside it Av. āṅhan- and ā(ə)raṇh- n. 'Mund' (BRT lines 7782, 14496) = Pokorny's 'av. āh-, ārədhan-'. Confirmed. (b) aošta- m. 'Oberlippe', dual 'the two lips' (Bartholomae, BRT.txt line 2969, Vd. 7.59; 'Vgl. aoštra-. — ai. óṣṭha-') is the t-derivative *əus-t- of the same root; Pokorny 785 and WP I 168 both list 'av. aošta-, aoštra-' verbatim, and Klein s.v. ostiary (p. ~1103) has 'OI. ōṣṭhaḥ, Avestic aoshta, aoshtra, \\\"lip\\\"'. Confirmed. (c) 'uz-ah, zâ 2 : push out of opening, give birth' is a false analysis, and it is the hinge on which Nourai hangs the whole Persian branch. The Avestan compound really attested is us.zan- / uz.zan-, i.e. the preverb us-/uz- 'up, out' plus the verb zan- 'to give birth' — Bartholomae s.v. zan- 'gebären' (BRT.txt line 27625): 'mit us: 1) \\\"erzeugen\\\", von Menschen: … dva nara us.zayeinte … V. 2.41; 2) \\\"gebären\\\"; Pass. \\\"nasci\\\": us nā zayeiti … Yt. 13.16; … 3) \\\"(Tiere) züchten\\\": … us.*zazənti … V. 3.5'. Cheung (Etym. Dict. of the Iranian Verb, s.v. *zanH¹ 'to give birth; (pass.) to be born') gives the same paradigm with the '(+ *us-)' preverb and closes with 'This root has an impeccable IE etymology. PIE *ǵenH₁- \\\"to beget, bear, produce\\\" = LIV: 163 f. | Pok.: 373 ff.' — i.e. Pokorny 373, not 784. There is no Avestan word *uz-ah 'push out of an opening'; Nourai has segmented us.zan- as us + āh and thereby attached the 'birth' family to the 'mouth' root. (d) 'zâ-dhana : child holder, womb' is not an Avestan compound; nothing of the kind is in Bartholomae. The word Nourai wants is New Persian زهدان (see node #2), a NP formation zeh + -dān 'container' (the suffix does go back to *dʰeh₁-no-, so his ☞Dhě 2 pointer is right about the second element, but the compound is a millennium too late for the Avestan box). (e) 'zâ-âp : spring, river' is likewise not Avestan but the analysis of NP زهاب/زاب; Farahvashi (IRN 108) and Mo'in give it as زه + آب. So: two words confirmed, three disputed; worst verdict stands.\",\n \"derivation_fa\": \"این جعبه دو خانوادهٔ ناهم‌ریشه را در هم آمیخته است. یک: āh- «دهان» راستین و درست‌جای است؛ بارتولومه در فرهنگ ایرانی باستان (ذیل ā̊h- n. «Mund») آن را ثبت کرده و همان بازماندهٔ مستقیم *h₁óh₃s در برابر سنسکریت ā́s و لاتینی ōs است؛ در کنارش āṅhan- و āraṇh- نیز به همین معنی آمده که همان «āh-، ārədhan-» پوکورنی است. دو: aošta- «لب بالا» و در مثنّی «دو لب» (بارتولومه، وندیداد ۷:۵۹) صورتِ پسوندِ -t همان ریشه است و پوکورنی (۷۸۵) و والده-پوکورنی (ج ۱ ص ۱۶۸) هر دو «aošta-، aoštra-» را عیناً می‌آورند؛ کلاین هم ذیل ostiary دارد. این دو پذیرفتنی است. سه: «uz-ah, zâ ۲» تجزیهٔ نادرستی است و همان لولایی است که نورایی کل شاخهٔ فارسی را بر آن آویخته. ترکیب گواهی‌شدهٔ اوستایی us.zan-/uz.zan- است، یعنی پیشوند us-/uz- «بر، بیرون» + فعل zan- «زادن» (بارتولومه ذیل zan-: «mit us: ۱) erzeugen … dva nara us.zayeinte؛ ۲) gebären، مجهول nasci: us nā zayeiti؛ ۳) züchten: us.zazənti»). چونگ نیز ذیل *zanH¹ همین صرف را با پیشوند *us- می‌آورد و می‌نویسد ریشه‌شناسی هندواروپایی آن بی‌خدشه است: *ǵenH₁- (LIV ۱۶۳ و پوکورنی ۳۷۳)، نه ص ۷۸۴. واژهٔ اوستایی *uz-ah «راندن از دهانه» وجود ندارد. چهار: «zâ-dhana» ترکیب اوستایی نیست؛ آنچه در نظر است «زهدان» فارسی نو است (زه + پسوند ـدان). پنج: «zâ-âp» نیز اوستایی نیست بلکه تجزیهٔ «زهاب/زاب» فارسی است (فره‌وشی و معین: زه + آب). نتیجه: دو واژه درست، سه واژه رد؛ داوری گره «رد‌شده» است.\",\n \"sources\": [\n   W + \"Reconstruction:Proto-Indo-European/h₃éh₁os\",\n   W + \"%D8%B2%D9%87\"\n ],\n \"ref_check\": [\n   {\"ref\": \"POK:785\", \"status\": \"partial\",\n    \"note\": \"POK_03.txt leaf 19 (printed 785): 't-Ableitungen sind ai. ōṣṭha- m. n. \\\"Lippe\\\"; av. aošta-, aoštra- ds. (*əus-), lat. ōstium \\\"Eingang, Flußmündung\\\"' — supports āh (leaf 18) and aošta/aoštra fully, but Pokorny's article contains nothing about zā-, uz-ah, zā-dhana or zā-āp; the Avestan verb zan- is Pokorny 373 f. (a different root).\"},\n   {\"ref\": \"SYN:228\", \"status\": \"partial\",\n    \"note\": \"Buck 4.24 MOUTH p. 228 (SYN.txt leaf 265): 'Skt. ās-, āsan-, āsya-, Av. āh- (also Skt. oṣṭha-, Av. aošta- \\\"lip\\\")'; p. 229 4.25 LIP lists 'Av. aosta'. Supports the mouth/lip words; silent on the zā- words.\"},\n   {\"ref\": \"KLN:1091\", \"status\": \"supports\",\n    \"note\": \"Klein p. 1091 s.v. 'oral' (KLN_1966.txt leaf 583; printed numbers 1094-1095 appear on leaf 585, so leaf 583 = pp. 1090-1091): '… cogn. with OI. āh, as-an, \\\"mouth\\\" … Avestic ah-, \\\"mouth\\\", Hitt. aish …'; the companion entry 'ostiary' (leaf 589, printed 1103) adds 'OI. ōṣṭhaḥ, Avestic aoshta, aoshtra, \\\"lip\\\"'. Exactly Nourai's āh and aošta/aoštra.\"},\n   {\"ref\": \"BQT:1049\", \"status\": \"partial\",\n    \"note\": \"Borhan-e Qate' p. 1049 = BQT_v2_pages.txt leaf 508 (the page opens 'بیان هفدهم — در زای نقطه دار با ها' and carries the زه entry): 'زه … و زاییدن آدمی و حیوانات دیگر باشد … و بمعنی نطفه و بچه و فرزند هم گفته‌اند و لهذا فرزند را زه‌زاد و رحم و بچه‌دان را زهدان گفته'; same page 'زهاب — بفتح اول بر وزن شهاب: تراویدن آب در کنار رودخانه و چشمه و تالاب و امثال آن؛ و چشمه را گویند'. It supports the Persian words of node #2 but is a Persian dictionary: it says nothing about Avestan and nothing about a 'mouth' root; Mo'in's etymological footnote on that page concerns زه 'bowstring' (Av. jyā-, Skt. jyā-), a third homonym.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"BRT.txt line 7567 s.v. ā̊h-; line 2969 s.v. aošta-; line 27625 s.v. zan-\", \"stance\": \"partial\",\n    \"note\": \"Supports 'j., g. ā̊h-, g. ¹āh- n. \\\"Mund\\\"' and 'j. aošta- m. \\\"Oberlippe\\\", Du. \\\"die beiden Lippen\\\" … Vgl. aoštra-. — ai. óṣṭha-'. Contradicts the rest: the us-forms are filed under the verb zan- 'gebären' — 'mit us: 1) \\\"erzeugen\\\" … dva nara us.zayeinte … 2) \\\"gebären\\\"; Pass. \\\"nasci\\\": us nā zayeiti … 3) \\\"(Tiere) züchten\\\" … us.zazənti'. No lemma *uz-ah, no zā-dāna-, no zā-āp-.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"CHEUNG.txt line 30019 ff. s.v. *zanH¹\", \"stance\": \"contradicts\",\n    \"note\": \"'*zanH¹ \\\"to give birth; (pass.) to be born\\\" … *AVESTAN: YAv. za(n)- … || (+ *us-) \\\"to breed, produce; be produced, bred\\\" … This root has an impeccable IE etymology. PIE *ǵenH₁- \\\"to beget, bear, produce\\\" = LIV: 163 f. | Pok.: 373 ff.' — the us- is a preverb, and the root is *ǵenh₁-, not the 'mouth' root.\"},\n   {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 645 (HRN.txt line 5709)\", \"stance\": \"contradicts\",\n    \"note\": \"'645. zāden \\\"gebären; geboren werden\\\", Praes. zāy-em, zād \\\"Geburt\\\" …, zeh \\\"Junges, Kind\\\", zehdān \\\"Uterus\\\", zehistān \\\"Fehlgeburt, Placenta\\\" … aw. √zan-, zayata \\\"gebären; geboren werden\\\", us zayente, zāta-; phlv. zātan, zāy(i)šn, zāk; ai. √jan-, jāyate' — Horn files zeh and zehdān under zādan < Av. zan-, and himself cites the 'us zayente' compound.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I 168-169 (line 10825 ff.)\", \"stance\": \"partial\",\n    \"note\": \"Supports āh and 'av. aošta- aoštra-' as t-derivatives; the article has no Iranian 'birth' material at all.\"},\n   {\"src\": \"AVG\", \"where\": \"AVG.txt — searched for aošta, us.zan\", \"stance\": \"silent\",\n    \"note\": \"Jackson's Avesta Grammar is a grammar, not a lexicon; no entry bearing on the arrow.\"}\n ],\n \"derivation_check\": None\n})\n\ne0[\"nodes\"].append({\n \"id\": 2,\n \"lang\": \"Persian\",\n \"words\": \"zeh 2 «زه ۲ ( زهیدن ، زاهیدن )» : to give birth ; zehdân «زهدان» : womb ; zahâb «زهاب ( زاب )» : river, spring\",\n \"verdict\": \"plausible\",\n \"derivation\": \"All three Persian words are real and correctly glossed, and they really do descend from the Avestan zan-/zā- that stands (wrongly labelled 'uz-ah') in the parent box — so the local arrow is sound even though the root above it is not. The chain Nourai omits is the Middle Persian one, and MacKenzie supplies it: MP zādan, zāy- 'to be born, give birth', with the nouns zahag [zhk'] 'child, offspring' (> NP زه), zahār [zhl] 'womb' (> NP زهار), zahā 'depth' and zahābag [zhh'pk'] 'spring' (> NP زهاب) (PHD.txt line 673). Phonetically: Old Iranian *zan- / ppp. *zāta- > MP zādan/zāy-; the abstract in *-aka- gives MP zahag, whose intervocalic -h- and lost -ag yield NP زه (zeh/zah) 'birth, offspring', and the same stem takes the container suffix -dān (< OIr. *-dāna-, PIE *dʰeh₁-no-) to give زهدان 'womb' — Horn no. 645 lists exactly 'zeh \\\"Junges, Kind\\\", zehdān \\\"Uterus\\\"' under زادن. زهاب continues MP zahābag = زه + آب, which is why the Kurdistan rivers are called زاب: Farahvashi (IRN 108) writes 'در این ترکیب زه به معنی زاینده است از ریشهٔ zā به معنی زاییدن و زهاب یا زاب به معنی رود زاینده است و با زاینده‌رود هم‌معنی است'. Mo'in bracket-analyses زهاب as 'زه (زهدن) + آب = زاب'. One caveat: en.wiktionary keeps the 'seepage' زه (Etymology 3, 'inherited from Middle Persian *zah, attested in zhʾpk\\\\' (zahābag \\\"spring, source\\\")') apart from the 'birth' زه (Etymology 2, '< PIE *ǵenh₁-'), so the identity of زهاب with the birth-root that Mo'in, Farahvashi and Nourai all assume is the traditional Iranian view rather than a settled one. Verdict plausible: words and immediate parent right, Middle Persian stage skipped, ultimate root wrong (see node #1).\",\n \"derivation_fa\": \"هر سه واژهٔ فارسی راستین‌اند و معنایشان درست است، و در واقع از همان zan-/zā- اوستایی می‌آیند که در جعبهٔ بالا — با برچسب نادرستِ «uz-ah» — نشسته است؛ پس پیکانِ همین گره سالم است، هرچند ریشهٔ بالای آن نیست. حلقه‌ای که نورایی انداخته حلقهٔ فارسی میانه است و مکنزی آن را می‌دهد: پهلوی zādan/zāy- «زادن»، و نام‌های zahag «فرزند، زاده» (> «زه»)، zahār «رحم» (> «زهار»)، zahā «گودی» و zahābag «چشمه» (> «زهاب»). از نظر آوایی: ایرانی باستان *zan- و اسم مفعول *zāta- در فارسی میانه zādan/zāy- شد؛ صورت با پسوند *-aka- پهلوی zahag را داد که با افتادنِ -ag به «زه» فارسی نو رسید، و همان ستاک با پسوند «ـدان» (< *-dāna- ایرانی باستان، از *dʰeh₁-no-) «زهدان» را ساخت — هرن (شمارهٔ ۶۴۵) عیناً «zeh (بچه، زاده)» و «zehdān (رحم)» را ذیل «زادن» آورده است. «زهاب» ادامهٔ zahābag پهلوی و همان «زه + آب» است؛ از این‌رو رودهای کردستان «زاب» خوانده می‌شوند: فره‌وشی در ایرانویج (ص ۱۰۸) می‌نویسد «در این ترکیب زه به معنی زاینده است از ریشهٔ zā به معنی زاییدن و زهاب یا زاب به معنی رود زاینده است». معین هم «زهاب» را «زه (زهدن) + آب = زاب» تجزیه کرده است. یک احتیاط: ویکی‌واژه «زه»ِ «تراوش آب» را (از فارسی میانهٔ *zah، گواهی‌شده در zahābag) از «زه»ِ «زادن» (از *ǵenh₁-) جدا می‌کند؛ پس یکی‌دانستنِ «زهاب» با ریشهٔ «زادن» — که معین و فره‌وشی و نورایی هر سه پذیرفته‌اند — دیدگاه سنتی ایرانی است نه حکم قطعی. داوری: با احتیاط پذیرفتنی است.\",\n \"sources\": [\n   W + \"%D8%B2%D9%87\",\n   W + \"%D8%B2%D9%87%D8%AF%D8%A7%D9%86\"\n ],\n \"ref_check\": [\n   {\"ref\": \"MON:1763\", \"status\": \"supports\",\n    \"note\": \"Mo'in, Farhang-e Farsi s.v. زه: '(امص.) زاییدن، زایش. تراوش آب از درز و لای چیزی. (اِ.) نطفه، بچه، فرزند'; s.v. زهدان: '(امر.) جایی در شکم مادر که بچه در آن قرار دارد، بچه‌دان، رحم'; s.v. زهاب: '[زه (زهدن) + آب = زاب] (امر.) آبی که از کنار رود، چشمه، تالاب و غیره تراوش کند …' (MON_part1.txt lines 72342-72398). All three of Nourai's words with his glosses, and Mo'in's own bracket analysis زه + آب. The page number 1763 could not be checked: only the 2-vol Adena abridgement of Mo'in is on disk, with different pagination.\"},\n   {\"ref\": \"IRN:108\", \"status\": \"supports\",\n    \"note\": \"Farahvashi, Iranvij p. 108 (= IRN_eliteraturebook.pdf page 119, fetched with tools/ref_page.py IRN:108): 'این رود زاب … در اصل ترکیب شده است از واژه‌های «زه» و «آب» و این ترکیب همانست که در واژهٔ «زهاب» در نام محل سرپل زهاب دیده می‌شود. در این ترکیب زه به معنی زاینده است از ریشهٔ zā به معنی زاییدن و زهاب یا زاب به معنی رود زاینده است و با زاینده‌رود هم‌معنی است.' — verbatim support for Nourai's 'zâ-âp : spring, river' → زهاب/زاب, from the root zā 'to give birth' (and hence not from a 'mouth' root).\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie p. 98 s.v. zahag etc. (PHD.txt line 673)\", \"stance\": \"supports\",\n    \"note\": \"'zahā [zh?(k')] depth. zahābag [zhh\\\\'pk\\\\' | N zahāb] spring. zahag [zhk\\\\' | M zhg, N zah] child, offspring. zahagōmand [zhk\\\\'wmnd] pregnant, gravid. zahār [zhl | N ~] womb.' — the Middle Persian stage Nourai skips, with the New Persian outcomes he lists.\"},\n   {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' pp. 1049-1051 (BQT_v2_pages.txt leaves 508-510)\", \"stance\": \"supports\",\n    \"note\": \"s.v. زه: '… و زاییدن آدمی و حیوانات دیگر باشد … و بمعنی نطفه و بچه و فرزند هم گفته‌اند و لهذا فرزند را زه‌زاد و رحم و بچه‌دان را زهدان گفته'; s.v. زهدان (leaf 509): 'بچه‌دان و قرارگاه نطفه باشد و بعربی رحم گویند', with Mo'in's footnote 'از: زه (ه.م) + دان (پسوند مکان)'; s.v. زهاب: 'تراویدن آب باشد در کنار رودخانه و چشمه و تالاب و امثال آن'.\"},\n   {\"src\": \"HRN\", \"where\": \"Horn no. 645 (HRN.txt line 5709)\", \"stance\": \"partial\",\n    \"note\": \"Supports the words — 'zeh \\\"Junges, Kind\\\", zehdān \\\"Uterus\\\"' — but files them under zādan < Av. √zan-, ai. √jan-, i.e. contradicts the *ōus- parentage.\"},\n   {\"src\": \"HUB\", \"where\": \"HUB.txt — searched zih, zeh, zahab\", \"stance\": \"silent\",\n    \"note\": \"Hübschmann's Persische Studien treats only زه 'bowstring' (line 8169: 'zih \\\"Bogensehne\\\" = zd. skr. jyā-') and زه‌گیر; nothing on زه 'birth' or زهاب.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"s.v. *zanH¹ (CHEUNG.txt line 30019 ff.)\", \"stance\": \"supports\",\n    \"note\": \"Gives the whole Iranian family, incl. 'MMP z\\\\'y(h)-, BMP z\\\\'\\\\' /zā-/ \\\"to be born; to give birth\\\"' and Balochi 'zah-/zahit', under PIE *ǵenH₁- — supports the Persian words but from the 'birth' root.\"},\n   {\"src\": \"ARY\", \"where\": \"ARY_pages.txt / ARY_latin_index_pages.txt — searched زه, زهدان, زهاب\", \"stance\": \"silent\",\n    \"note\": \"Aryanpur's IE-roots dictionary yielded no entry for these words in the available OCR.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 3,\n \"lang\": \"Latin\",\n \"words\": \"ôs 2, ôr : mouth, face ; ôscillum : a face mask hung from a tree to swing(oscillate) in the wind\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Latin ōs, gen. ōris (with the regular Latin rhotacism of *ōs-es > ōris) 'mouth, face, opening, edge' is the classical reflex of *h₁óh₃s; Pokorny 784 and WP I 168 put it beside Skt. ā́s and Av. āh-, and the same stem yields ōra 'edge, coast' (< *ōs-a), cōram 'in the presence of' (*co-ōro-), ōstium 'door, river-mouth' and the diminutive ōsculum 'little mouth, kiss'. Nourai's second word is also right, and better documented than Klein allows: Ernout-Meillet, Dictionnaire étymologique de la langue latine p. 834, s.v. oscillum — 'diminutif de ōs, ōsculum. Deux sens, le premier se rapportant au sens de ōs \\\"bouche, orifice\\\", l'autre à celui de ōs \\\"visage\\\": 1° petite cavité au milieu des légumineuses, d'où s'élance le germe (Colum.); 2° petit masque (= προσωπεῖον), surtout de Bacchus, qu'on suspendait aux arbres, notamment dans les vignobles, de manière qu'ils fussent agités par le vent. Cf. Vg. G. 2, 387 sqq. … De ce second sens dérive ōscillō, -ās \\\"se balancer (comme les masques)\\\", et ōscillātiō'. That is Nourai's gloss almost word for word, with the Virgilian source (Georgics 2.387-389, the little masks of Bacchus hung in the vines). The dissent to note: Klein s.v. oscillate (p. ~1101) says only 'fr. ōscillum, \\\"a swing\\\", which is of uncertain origin', and Watkins lists OSCULATE and OSCULUM under ōs- but not OSCILLATE; Etymonline keeps the traditional account ('usually is identified with the oscillum that meant \\\"little face\\\"'). So the ōs-etymology of ōscillum is the standard one but not unanimous.\",\n \"derivation_fa\": \"لاتینی ōs با حالت اضافی ōris (با ابدال قانونمندِ s به r میان دو واکه: *ōs-es > ōris) «دهان، چهره، دهانه، کناره» بازماندهٔ کلاسیک *h₁óh₃s است؛ پوکورنی (۷۸۴) و والده-پوکورنی (ج ۱ ص ۱۶۸) آن را در کنار سنسکریت ā́s و اوستایی āh- می‌نشانند، و از همین ستاک ōra «کناره، ساحل»، cōram «در حضور»، ōstium «در، دهانهٔ رود» و مصغّرِ ōsculum «دهانِ کوچک، بوسه» ساخته شده است. واژهٔ دوم نیز درست است و پشتوانه‌ای بهتر از آنچه کلاین می‌پندارد دارد: ارنو و مِیه در فرهنگ ریشه‌شناسی لاتین (ص ۸۳۴) ذیل oscillum می‌نویسند «مصغّرِ ōs، ōsculum … ۲) نقابکِ کوچک (προσωπεῖον)، بیشتر نقابِ باکخوس، که آن را از درختان و بویژه در تاکستان‌ها می‌آویختند تا باد بجنباندش. رجوع کنید به ویرژیل، گِئورگیکا ۲:۳۸۷ به‌بعد … از همین معنی دوم فعلِ ōscillō \\\"جنبیدن (چون نقاب‌ها)\\\" و ōscillātiō پدید آمده». این تقریباً واژه‌به‌واژه همان توضیح نورایی است. نکتهٔ اختلاف: کلاین ذیل oscillate می‌گوید ōscillum «خاستگاهی نامعلوم» دارد و واتکینز نیز OSCILLATE را زیر *ōs- نیاورده؛ اما Etymonline روایت سنتی را نگه داشته است. پس اشتقاق ōscillum از ōs دیدگاه معیار است، هرچند همگانی نیست.\",\n \"sources\": [\"https://www.etymonline.com/word/oscillate\"],\n \"ref_check\": [\n   {\"ref\": \"AHD:929\", \"status\": \"partial\",\n    \"note\": \"AHD:929 is a page of the 1975/76 American Heritage New College Edition main dictionary (the o- range), which is not openly readable; but the IE-roots appendix of that same edition is preserved in Watkins 1985, and its root ōs- (AHD_watkins1985.txt line 812) reads 'ōs-. Mouth. 1. Latin ōs (stem ōr-), mouth, face, orifice, and derivative ōstium (< suffixed form *ōs-to-), door: ORAL, OS1, OSCULATE, OSCULUM, OSTIARY, OSTIUM, USHER; INOSCULATE, ORIFICE, ORINASAL, OROTUND, OSCITANCY, PERORAL' — supports ōs/ōr- and the English node, but OSCILLATE is not in Watkins' list.\"},\n   {\"ref\": \"KLN\", \"status\": \"partial\",\n    \"note\": \"Klein p. 1091 s.v. oral gives 'L. os, gen. oris, \\\"mouth, face; opening, entrance, orifice\\\", fr. *ous-' and cross-refers orifice, ostiary, usher — supports ōs, ōr-. But s.v. oscillate (leaf 588, printed ~1101) Klein writes 'fr. oscillum, \\\"a swing\\\", which is of uncertain origin', i.e. he does not endorse Nourai's ōscillum < ōs.\"}\n ],\n \"consulted\": [\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet p. 834 s.v. oscillum (LAT.txt line 44168)\", \"stance\": \"supports\",\n    \"note\": \"'oscillum, -ī n.: diminutif de ōs, ōsculum. Deux sens, le premier se rapportant au sens de ōs \\\"bouche, orifice\\\", l'autre à celui de ōs \\\"visage\\\" … 2° petit masque (= προσωπεῖον), surtout de Bacchus, qu'on suspendait aux arbres, notamment dans les vignobles, de manière qu'ils fussent agités par le vent. Cf. Vg. G. 2,387 sqq. … De ce second sens dérive ōscillō, -ās \\\"se balancer\\\" …' — the decisive support for Nourai's second word.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I 168-169\", \"stance\": \"supports\",\n    \"note\": \"'Lat. os, oris \\\"Mund, Antlitz, Öffnung\\\" … Dazu ā-Ableitung … lat. ora \\\"Rand, Saum, Grenze\\\" … ōsculum \\\"Mündchen, Kuß\\\"' — Latin ōs/ōris under the same root, with ōsculum as its diminutive.\"},\n   {\"src\": \"POK\", \"where\": \"p. 784-785 (POK_03.txt leaves 18-19)\", \"stance\": \"supports\",\n    \"note\": \"'lat. ōs, ōris \\\"Mund, Antlitz, Rand, Ufer\\\" … ōsculum \\\"Kuß\\\" ist Demin. von ōs … lat. ōstium \\\"Eingang, Flußmündung\\\"'.\"},\n   {\"src\": \"LEW\", \"where\": \"LEW_1910.txt — searched oscill, os oris\", \"stance\": \"silent\",\n    \"note\": \"The local LEW file is only 0.6 MB and appears to be an index/word-list; neither headword could be located in it.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 4,\n \"lang\": \"English\",\n \"words\": \"oral, orifice, oscillate ; usher\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"All four English words descend from Latin ōs, and Watkins' appendix lists three of them under the very root: 'ōs-. Mouth. 1. Latin ōs (stem ōr-) … and derivative ōstium … door: ORAL, OS1, OSCULATE, OSCULUM, OSTIARY, OSTIUM, USHER; INOSCULATE, ORIFICE …'. Individually: oral (1620s) < Late Latin ōrālis, from ōr- + -ālis; orifice < Late Latin ōrificium 'an opening', ōs + -ficium (facere), through Middle French orifice; oscillate (1726, partly a back-formation from oscillation) < Latin ōscillāre 'to swing', from ōscillum (see node #3); usher through the Romance chain — Klein s.v. usher: 'OF., fr. VL. ustiārius, \\\"doorkeeper\\\", fr. L. ōstiārius, of s.m., fr. ōstium, \\\"door, entrance\\\"' (Old French uissier > Anglo-French usser > Middle English ussher, first as the title of the door-keeper of a hall, then 'one who shows people in'). Since ōstium is itself the *ōs-t- derivative of ōs, the whole set is legitimately under this root. Nourai gives the node no reference, but Klein (cited on the Latin parent) and the AHD appendix both cover it.\",\n \"derivation_fa\": \"هر چهار واژهٔ انگلیسی از لاتینی ōs می‌آیند و واتکینز سه‌تای آن‌ها را در پیوستِ فرهنگ American Heritage عیناً زیر همین ریشه آورده است: «*ōs-. دهان … ORAL, OS¹, OSCULATE, OSCULUM, OSTIARY, OSTIUM, USHER؛ INOSCULATE, ORIFICE …». جداگانه: oral (سدهٔ هفدهم) از لاتینی متأخر ōrālis؛ orifice از لاتینی متأخر ōrificium «دهانه» (ōs + ficium از facere) به‌واسطهٔ فرانسهٔ میانه؛ oscillate (۱۷۲۶، تا حدی گشتهٔ پسین از oscillation) از لاتینی ōscillāre «جنبیدن» از ōscillum (بنگرید به گرهٔ ۳)؛ و usher از راه رومی: کلاین ذیل usher می‌نویسد «از فرانسهٔ کهن، از لاتینیِ عامیانه ustiārius \\\"دربان\\\"، از لاتینی ōstiārius، از ōstium \\\"در، درگاه\\\"» — و ōstium خود صورتِ پسوندِ -t همان ōs است. پس همهٔ این مجموعه به‌درستی زیر این ریشه می‌نشیند. نورایی برای این گره ارجاعی نداده، اما کلاین (که در جعبهٔ لاتینی یاد شده) و پیوست AHD هر دو پوشش می‌دهند. ادعای نورایی درست است.\",\n \"sources\": [\"https://www.etymonline.com/word/oscillate\"],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\",\n    \"note\": \"Nourai gives this node no reference of its own (refs=None); the coverage comes from the Latin parent's KLN and AHD:929, both checked there.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"p. 1091 s.v. oral; leaf 589 s.v. ostiary; leaf 892 s.v. usher\", \"stance\": \"supports\",\n    \"note\": \"s.v. oral 'Cp. coram, orifice, orle, orotund, oscitancy, ostiary, ostiole, usher, Auriga, vera'; s.v. usher 'OF., fr. VL. ustiarius, \\\"doorkeeper\\\", fr. L. ostiarius, of s.m., fr. ostium, \\\"door, entrance\\\". See ostiary'; s.v. ostiary 'L. ostiarius … fr. ostium … which is rel. to L. os, \\\"mouth\\\"'.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. ōs- (line 812)\", \"stance\": \"supports\",\n    \"note\": \"'… ORAL, OS1, OSCULATE, OSCULUM, OSTIARY, OSTIUM, USHER; INOSCULATE, ORIFICE, ORINASAL, OROTUND, OSCITANCY, PERORAL' — oral, orifice and usher listed explicitly; oscillate absent from Watkins' list but supplied by Ernout-Meillet (node #3).\"},\n   {\"src\": \"SKT\", \"where\": \"SKT.txt — searched USHER, ORAL, ORIFICE, OSCILLATE, ostiarius\", \"stance\": \"silent\",\n    \"note\": \"Only Skeat's running page-heads ('USHER.', 'ORAL.') survive in this OCR; the entries themselves are unreadable, so Skeat could not be used.\"},\n   {\"src\": \"FSD\", \"where\": \"FSD_vol1-4.txt — searched oscillare, ostiarius, oddi\", \"stance\": \"silent\",\n    \"note\": \"The Funk & Wagnalls OCR did not yield any of these etymology strings.\"}\n ]\n})\n\n# ---------------- entry 5 ----------------\ne5 = {\n \"entry\": 5,\n \"root\": \"Ozgho, Ozdo\",\n \"verdict\": \"plausible\",\n \"modern_form\": \"Two distinct Pokorny lemmas: *ozdo-s 'branch' (Pokorny 785-786; modern *h₃ósdos) and *ozgho- '?? bud, plant-shoot, branch' (Pokorny 786), the latter known only from Iranian and Greek\",\n \"note\": \"Nourai has merged two neighbouring but separate Pokorny entries into one root box, and has widened the gloss. Pokorny 785-786 (POK_03.txt leaves 20-21) has 'ozdo-s \\\"Ast\\\". Arm. ost \\\"Zweig, Ast\\\", gr. ὄζος ds., got. asts, ahd. ast \\\"Ast\\\"; mit Vriddhi *ōzdos in ags. ōst, mnd. ōst \\\"Knoten im Holz\\\" … wohl(?) *o-zdo-s \\\"(am Stamme) ansitzend\\\", s. Präfix *e-, o- und sed- \\\"sitzen\\\"'. Separately, Pokorny 786 has 'ozgho- \\\"Knospe, Pflanzentrieb, Zweig\\\"??  Pehl. azg \\\"Ast\\\", npers. azaɣ \\\"Zweig, Knospe\\\": gr. ὄσχος, ὄσχη, ὤσχη \\\"Zweig, Schößling\\\"' — note Pokorny's double question mark, and note that the two families do NOT share his Iranian material: azg belongs only to ozgho-. Walde-Pokorny I 185 is the fuller version and is where Nourai's third gloss 'offspring' comes from: after listing 'Pehl. azg \\\"Ast\\\" (nachgewiesen von Hübschmann IF. 4, 119 …) np. azaɣ \\\"Zweig, Knospe\\\" : gr. ὄσχος, ὄσχη, ὤσχη \\\"Zweig, Schößling\\\"', WP reports Scheftelowitz's wider comparison 'urslav. ǫzgъ, russ. azg \\\"Ende, Kamm\\\", poln. dial. wązg \\\"Schößling\\\" … und np. azm \\\"(*Schößling =) Sprößling, Sohn\\\"' — and then rejects the reconstruction behind it ('aber ein *on[g]zgho- aus *ongh-sqo würde nur gr. ὄσχος, nicht aber ὄσχη rechtfertigen; auch würde pehl. azg dann als *ngh-sqo- eine Ablautstufe neben ὄσχος darstellen'). Mann (IEC 863, printed page number visible in the file just above the lemma) states the merged root as Nourai does: 'odsghos (odzgos, odhgos), a \\\"shoot, branch, stem\\\". WP I, 185. Skt. cf. ádgah, m. \\\"cane, stalk\\\"; Pahl. azg \\\"branch\\\"; Per. azaɣ, (id. and \\\"shoot\\\"); Gk. óskhos … W osg \\\"shoot\\\"' — this, not Pokorny, is Nourai's real model, and Nourai's own IEC:863 citations on the nodes show he knew it. Modern assessment: en.wiktionary sets up *h₃ósdos 'branch, twig' (Gk. ὄζος, Arm. ost, PGmc. *astaz) and treats Proto-Indo-Iranian *Hádᶻgas 'knot (in a plant), branch' — with MP azg — only as 'possibly connected in some way', 'different simplifications of the same original compound word'; Beekes regards Gk. ὄσχη as 'may well be of Pre-Greek origin'. So: the root exists, the Iranian and Greek members are genuinely compared by every authority, but treating Ozgho and Ozdo as one root with the gloss 'offspring' is Nourai's (and Mann's) simplification, and Watkins/AHD has no such root at all.\",\n \"note_fa\": \"نورایی دو مادّهٔ همسایه ولی جداگانهٔ پوکورنی را در یک جعبه ادغام کرده و معنا را هم گسترده‌تر گرفته است. پوکورنی در ص ۷۸۵–۷۸۶ دارد: «*ozdo-s \\\"شاخه\\\". ارمنی ost، یونانی ὄζος، گوتی asts، آلمانی علیای کهن ast؛ با وریدی *ōzdos در انگلیسی کهن ōst \\\"گره در چوب\\\" … شاید *o-zdo-s \\\"نشسته بر تنه\\\" از پیشوند *o- و ریشهٔ *sed- \\\"نشستن\\\"». و جداگانه در ص ۷۸۶: «*ozgho- \\\"جوانه، شاخهٔ نوروییده\\\"؟؟ پهلوی azg \\\"شاخه\\\"، فارسی نو azaɣ \\\"شاخه، جوانه\\\": یونانی ὄσχος، ὄσχη \\\"شاخه، نهال\\\"» — به دو علامت پرسشِ پوکورنی توجه کنید، و به اینکه مادّهٔ ایرانی تنها به ozgho- تعلق دارد نه به ozdo-. والده-پوکورنی (ج ۱ ص ۱۸۵) صورت مشروح‌تر است و سرچشمهٔ معنای سوم نورایی («فرزند») همان‌جاست: پس از آوردنِ «پهلوی azg (به گواهی هوبشمان، IF ۴:۱۱۹) و فارسی azaɣ در برابر یونانی ὄσχος»، مقایسهٔ گسترده‌ترِ شفتلوویتس را نقل می‌کند که «فارسی azm \\\"(نهال =) زاده، پسر\\\"» را هم بدان می‌پیوندد، و سپس بازسازیِ پشتِ آن را رد می‌کند. مان (IEC ۸۶۳) همان ریشهٔ ادغام‌شده را می‌سازد: «odsghos … \\\"نهال، شاخه، ستاک\\\"؛ سنسکریت ádgah \\\"نی، ستاک\\\"؛ پهلوی azg؛ فارسی azaɣ؛ یونانی óskhos» — و همین، نه پوکورنی، الگوی واقعی نورایی است. ارزیابی امروزی: ویکی‌واژه ریشهٔ *h₃ósdos را می‌گذارد و هندوایرانی آغازین *Hádᶻgas (با پهلوی azg) را تنها «شاید مرتبط» می‌شمارد، و بیکس یونانی ὄσχη را احتمالاً پیش‌یونانی می‌داند. پس ریشه هست و مقایسهٔ ایرانی و یونانی در همهٔ منابع آمده، اما یکی‌کردنِ Ozgho و Ozdo و افزودنِ معنای «فرزند» سادگیِ نورایی (و مان) است؛ واتکینز چنین ریشه‌ای ندارد. داوری: با احتیاط پذیرفتنی است.\",\n \"sources\": [\n   W + \"Reconstruction:Proto-Indo-European/h₃ósdos\",\n   W + \"ὄσχη\"\n ],\n \"ref_check\": [\n   {\"ref\": \"POK:786\", \"status\": \"partial\",\n    \"note\": \"POK_03.txt leaf 21 (printed 786): 'ozgho- \\\"Knospe, Pflanzentrieb, Zweig\\\"??  Pehl. azg \\\"Ast\\\", npers. azaɣ \\\"Zweig, Knospe\\\": gr. ὄσχος, ὄσχη, ὤσχη \\\"Zweig, Schößling\\\" … WP. I 185'; the ozdo-s article stands just before it (leaves 20-21, straddling pp. 785-786). Supports 'branch, bud' and the Pahlavi/Persian members, but (a) Pokorny keeps ozdo- and ozgho- as two lemmas, (b) he marks ozgho- with '??', (c) he has no 'offspring' sense and no Sanskrit or Germanic member under ozgho-.\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. I 185 (WLD_Bd1_1930_dli_70244_djvu.txt lines 11919-11935)\", \"stance\": \"partial\",\n    \"note\": \"'ozgho- \\\"Knospe, Pflanzentrieb, Zweig\\\". Pehl. azg \\\"Ast\\\" (nachgewiesen von Hübschmann IF. 4, 119, zw. ob nicht azd = ὄζος zu lesen; doch azg wegen:) np. azaɣ \\\"Zweig, Knospe\\\" : gr. ὄσχος, ὄσχη, ὤσχη \\\"Zweig, Schößling\\\" … Scheftelowitz vergleicht ferner unter Ansatz der Wz. als ongh- … und np. azm \\\"(*Schößling =) Sprößling, Sohn\\\"; aber ein *on[g]zgho- aus *ongh-sqo würde nur gr. ὄσχος, nicht aber ὄσχη rechtfertigen …'. Supports the root and, uniquely, records Nourai's azm — while rejecting the reconstruction that would join it.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann p. 863 s.v. odsghos (IEC.txt leaf 481)\", \"stance\": \"supports\",\n    \"note\": \"'odsghos (odzgos, odhgos), a \\\"shoot, branch, stem\\\". WP I, 185. Skt. cf. ádgah, m. \\\"cane, stalk\\\"; Pahl. azg \\\"branch\\\"; Per. azaɣ, (id. and \\\"shoot\\\"); Gk. óskhos, e, mf. id., cf. also ól-oskhos, m. \\\"pedicel\\\"; W osg, m. \\\"shoot, projection\\\" beside osgl … and osglen, f. \\\"branch, twig\\\"' — the exact source of Nourai's root box and of three of his four nodes.\"},\n   {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt — searched ozdo, ozgho, ozdho, zdho, 'branch' roots\", \"stance\": \"silent\",\n    \"note\": \"Watkins' appendix has no root *ozdo-/*ozgho- at all (the neighbouring entries run 'os-. Ash tree', 'ōs-. Mouth', 'ost-. Bone', 'ous-. Ear', 'owi-. Sheep'), and ODD is assigned to no root in the 1985 edition.\"},\n   {\"src\": \"SYN\", \"where\": \"SYN.txt — searched 4.4x BRANCH, ozgho, azg\", \"stance\": \"silent\",\n    \"note\": \"Buck has no 'branch' concept section bearing on the Iranian word.\"}\n ],\n \"nodes\": []\n}\n\ne5[\"nodes\"].append({\n \"id\": 1,\n \"lang\": \"Pahlavi\",\n \"words\": \"azg : branch, offspring\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Middle Persian azg 'branch' is well attested and is the anchor of the whole root: MacKenzie, Concise Pahlavi Dictionary, s.v. 'azg [ʾzg | N azɣ] branch' (PHD.txt line 227; the English-Pahlavi index has 'branch azg, tāg', line 1066). Hübschmann established the reading (IF 4, 119) against a possible *azd, and Walde-Pokorny I 185 accepts azg precisely because New Persian azaɣ requires the -g: 'zw. ob nicht azd = ὄζος zu lesen; doch azg wegen: np. azaɣ'. Phonetically Book Pahlavi ʾzg /azg/ continues an Old Iranian *azga- < *h₃ozgʰo-, with the Iranian sound-law that turns PIE *o into a; the Greek partner ὄσχος/ὄσχη 'vine-shoot' shows the same *-sgʰ-/-zgʰ- cluster with Greek devoicing. One qualification on the gloss: MacKenzie, Pokorny and Mann all give only 'branch/shoot'. The 'offspring' half of Nourai's gloss is not a Pahlavi meaning; it is back-projected from NP azm (node #2), which WP itself declines to connect.\",\n \"derivation_fa\": \"«azg» فارسی میانه به معنی «شاخه» گواهی‌شدهٔ روشنی دارد و لنگرِ همهٔ این ریشه است: مکنزی در فرهنگ کوچک پهلوی می‌آورد «azg [ʾzg | فارسی نو azɣ] شاخه»، و در نمایهٔ انگلیسی‌ـ‌پهلوی نیز «branch azg, tāg». هوبشمان (IF ۴:۱۱۹) خوانشِ azg را در برابر *azd احتمالی استوار کرد و والده-پوکورنی (ج ۱ ص ۱۸۵) نیز همین را می‌پذیرد، دقیقاً به این دلیل که «azaɣ» فارسی نو به -g نیاز دارد. از نظر آوایی ʾzg پهلویِ کتابی بازماندهٔ ایرانی باستان *azga- از *h₃ozgʰo- است، با آن قانون آوایی ایرانی که *o هندواروپایی را به a بدل می‌کند؛ همتای یونانی ὄσχος/ὄσχη «نهالِ تاک» همان خوشهٔ *-zgʰ- را با بی‌واک‌شدگیِ یونانی نشان می‌دهد. یک قید در معنا: مکنزی و پوکورنی و مان هر سه تنها «شاخه، نهال» می‌دهند؛ نیمهٔ «فرزند» در معنای نورایی معنایی پهلوی نیست و از «ازم» فارسی نو (گرهٔ ۲) به عقب تابیده شده، همان که والده-پوکورنی از پیوند دادنش خودداری می‌کند. جز این، ادعای نورایی درست است.\",\n \"sources\": [W + \"Reconstruction:Proto-Indo-European/h₃ósdos\"],\n \"ref_check\": [\n   {\"ref\": \"POK:786\", \"status\": \"supports\",\n    \"note\": \"POK_03.txt leaf 21 (printed 786): 'ozgho- \\\"Knospe, Pflanzentrieb, Zweig\\\"??  Pehl. azg \\\"Ast\\\", npers. azaɣ \\\"Zweig, Knospe\\\"' — the arrow root → Pahlavi azg exactly as drawn, though with Pokorny's '??'.\"},\n   {\"ref\": \"IEC:863\", \"status\": \"supports\",\n    \"note\": \"Mann p. 863 s.v. odsghos: '… Pahl. azg \\\"branch\\\"; Per. azaɣ, (id. and \\\"shoot\\\") …'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie p. 16 s.v. azg (PHD.txt line 227); reverse index line 1066\", \"stance\": \"supports\",\n    \"note\": \"'azg [ʾzg | N azɣ] branch.' and 'branch azg, tāg.' — the word, the Book Pahlavi spelling and the New Persian outcome, with no 'offspring' sense.\"},\n   {\"src\": \"NYB\", \"where\": \"NYB_vol2_glossary.txt — searched azg\", \"stance\": \"silent\",\n    \"note\": \"Nyberg's glossary (to the texts he edits) has no azg entry; grep for 'azg' returns nothing.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I 185\", \"stance\": \"supports\",\n    \"note\": \"'Pehl. azg \\\"Ast\\\" (nachgewiesen von Hübschmann IF. 4, 119 …) np. azaɣ \\\"Zweig, Knospe\\\" : gr. ὄσχος …'.\"},\n   {\"src\": \"HUB\", \"where\": \"HUB.txt (Persische Studien) — searched azg, azaɣ, Zweig\", \"stance\": \"silent\",\n    \"note\": \"The demonstration WP credits to Hübschmann is in IF 4 (1894), not in Persische Studien; the local HUB file has only unrelated 'Zweig' words (istāx, sax).\"}\n ]\n})\n\ne5[\"nodes\"].append({\n \"id\": 2,\n \"lang\": \"Persian\",\n \"words\": \"azğ «ازغ» : branch, shoot ; azm «ازم» : child  [extra script: اژغ ، آزغ ، ازگ ۱]\",\n \"verdict\": \"plausible\",\n \"derivation\": \"azɣ is solid; azm is real but its attachment here is expressly rejected by the reference Nourai's own source rests on. (a) ازغ / اژغ / آزغ / ازگ 'a branch cut and trimmed from a tree, a shoot' is exactly what Borhan-e Qate' has: s.v. ازغ (BQT_v1_pages.txt leaf 326, = printed p. 114) 'ازغ — بفتح اول و سکون ثانی و غین نقطه‌دار: آنچه از شاخهای درخت برند و بپیرایش دهند و آنرا بعربی جلمه گویند', and s.v. اژغ two leaves later (leaf 328) 'شاخه‌هایی را گویند که از درخت بریده باشند و بعربی جلمه خوانند', where Mo'in's footnote gives the Pahlavi ancestor 'azg'. Mo'in's own dictionary has both spellings with the variant chain Nourai copies: 'ازغ [= آزغ = اژغ = ازگ] (اِ.) آنچه از شاخه‌های درخت که ببرند و بپیرایش دهند' and 'اژغ [= ازغ = آزغ = ازگ] شاخه‌هایی که از درخت بریده باشند، ترکه، شاخهٔ باریک' (MON_part1.txt lines 10628, 10820). Phonetically MP azg > NP azɣ is the regular Persian change of post-consonantal -g to the voiced velar fricative -ɣ (the same change that gives NP māɣ, zāɣ); the by-forms اژغ and آزغ are secondary (ز/ژ alternation and prothetic lengthening), and ازگ ۱ preserves the Pahlavi -g unchanged, a doublet. (b) ازم 'child' is not a fabrication: Walde-Pokorny I 185 records 'np. azm \\\"(*Schößling =) Sprößling, Sohn\\\"' as part of Scheftelowitz's comparison — and in the very next clause rejects the reconstruction (*ongh-sqo-) that alone would license it, so WP does not derive azm from azg. Neither Mann (IEC 863) nor Borhan (searched leaves 315-345 of vol. 1) nor Mo'in has an entry ازم 'child'; Nourai's BQT:114,115 and MON:218 do not cover it. So the second word is a semantically attractive but unsupported add-on: 'shoot' → 'offspring' is a natural metaphor, but the only book that reports it also says the sound-law does not work.\",\n \"derivation_fa\": \"«ازغ» استوار است؛ «ازم» ساختگی نیست ولی پیوندش به همین جا را همان منبعی که تکیه‌گاه نورایی است صریحاً رد می‌کند. یک: «ازغ / اژغ / آزغ / ازگ» به معنی «شاخهٔ بریده و پیراسته از درخت، نهال» دقیقاً همان است که در برهان قاطع آمده — ذیل «ازغ» (ص ۱۱۴): «بفتح اول و سکون ثانی و غین نقطه‌دار: آنچه از شاخهای درخت برند و بپیرایش دهند و آن را بعربی جلمه گویند»، و دو صفحه بعد ذیل «اژغ»: «شاخه‌هایی را گویند که از درخت بریده باشند»، که در حاشیه معین نیای پهلوی آن را «azg» می‌آورد. فرهنگ معین نیز هر دو نگارش را با همان زنجیرهٔ گونه‌ها که نورایی نقل کرده دارد: «ازغ [= آزغ = اژغ = ازگ]» و «اژغ [= ازغ = آزغ = ازگ] … ترکه، شاخهٔ باریک». از نظر آوایی azg پهلوی به azɣ فارسی نو بدل شده است، بر پایهٔ همان دگرگونی قانونمندِ گ به غ پس از همخوان (مانند «ماغ» و «زاغ»)؛ گونه‌های «اژغ» و «آزغ» ثانوی‌اند (ابدال ز/ژ و کشش آغازی) و «ازگ» گ پهلوی را دست‌نخورده نگه داشته و دوگانهٔ آن است. دو: «ازم» به معنی «فرزند» بی‌پایه نیست: والده-پوکورنی (ج ۱ ص ۱۸۵) در نقلِ مقایسهٔ شفتلوویتس «np. azm \\\"(نهال =) زاده، پسر\\\"» را ثبت کرده — و در جملهٔ بعد بازسازی‌ای را که تنها آن می‌توانست این پیوند را روا بدارد رد می‌کند؛ پس والده-پوکورنی «ازم» را از «azg» نمی‌گیرد. نه مان، نه برهان قاطع (برگ‌های ۳۱۵ تا ۳۴۵ جلد یک جست‌وجو شد) و نه معین مادّهٔ «ازم» به معنی «فرزند» ندارند و ارجاع‌های نورایی (BQT:114,115 و MON:218) آن را نمی‌پوشانند. پس واژهٔ دوم افزوده‌ای است دلنشین ولی بی‌پشتوانه: گذارِ معناییِ «نهال» به «زاده» طبیعی است، اما یگانه کتابی که آن را گزارش کرده خود می‌گوید قانون آوایی جور نمی‌آید.\",\n \"sources\": [W + \"Reconstruction:Proto-Indo-European/h₃ósdos\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:114,115\", \"status\": \"partial\",\n    \"note\": \"Borhan-e Qate' vol. 1 (BQT_v1_pages.txt): leaf 326 s.v. ازغ 'آنچه از شاخهای درخت برند و بپیرایش دهند و آنرا بعربی جلمه گویند' and leaf 328 s.v. اژغ 'شاخه‌هایی را گویند که از درخت بریده باشند و بعربی جلمه خوانند', whose Mo'in footnote reads '[Pahlavi] azg. — ر[ک]: ازغ'. The two leaves are two apart, matching Nourai's 'pp. 114, 115' (the vol.-1 scan has ~212 leaves of front matter, so leaf 326 ≈ printed 114). Supports azɣ and its variants and even the Pahlavi ancestry; but nothing on ازم 'child' anywhere in the ا section (leaves 315-345 searched).\"},\n   {\"ref\": \"IEC:863\", \"status\": \"partial\",\n    \"note\": \"Mann p. 863 s.v. odsghos: 'Per. azaɣ, (id. and \\\"shoot\\\")' — supports azɣ; the lemma has no azm.\"},\n   {\"ref\": \"MON:218\", \"status\": \"partial\",\n    \"note\": \"Mo'in s.v. ازغ 'ه [= آزغ = اژغ = ازگ] (اِ.) آنچه از شاخه‌های درخت که ببرند و بپیرایش دهند، آنچه از شاخه‌های درخت انگور برند' and s.v. اژغ '[= ازغ = آزغ = ازگ] شاخه‌هایی که از درخت بریده باشند، ترکه، شاخهٔ باریک' (MON_part1.txt lines 10628, 10820) — the word plus the exact variant list Nourai prints as extra script. No ازم 'child' in Mo'in. Page 218 itself is not verifiable: only the 2-vol Adena abridgement is on disk.\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. I 185 (line 11930-11934)\", \"stance\": \"partial\",\n    \"note\": \"The only book that has azm: 'Scheftelowitz vergleicht ferner … und np. azm \\\"(*Schößling =) Sprößling, Sohn\\\"; aber ein *on[g]zgho- aus *ongh-sqo würde nur gr. ὄσχος, nicht aber ὄσχη rechtfertigen, auch würde pehl. azg dann als *ngh-sqo- eine Ablautstufe neben ὄσχος darstellen und wären azg : ὄσχος dann nicht mehr vollständig gleich.' Records the word, refuses the derivation.\"},\n   {\"src\": \"BQT\", \"where\": \"vol. 1 leaves 326, 328 (ازغ, اژغ) and leaf 248 (آزوغ/آژوغ 'pruning, cut date-palm branches')\", \"stance\": \"supports\",\n    \"note\": \"Both spellings with the 'cut and trimmed branch' sense, plus the آزوغ/آژوغ by-forms and the cross-reference footnote 'ره: آژغ و ازغ'.\"},\n   {\"src\": \"MON\", \"where\": \"MON_part1.txt lines 10628, 10820\", \"stance\": \"supports\",\n    \"note\": \"See ref_check MON:218; Mo'in's bracketed variant chain [آزغ = اژغ = ازگ] is precisely Nourai's 'extra' script line اژغ ، آزغ ، ازگ ۱.\"},\n   {\"src\": \"ARY\", \"where\": \"incoming/ARY/ARY_pages.txt — searched ازغ, اژغ\", \"stance\": \"silent\",\n    \"note\": \"Aryanpur's dictionary of IE roots in Persian has no entry for this word in the available OCR.\"},\n   {\"src\": \"HRN\", \"where\": \"HRN.txt — searched azg, Zweig\", \"stance\": \"silent\",\n    \"note\": \"Horn's only azg (no. 42, line 10208) is a different word: 'azg (d. i. azak) \\\"Ziege\\\" (PPGl.)' = 'goat'; his 'Zweig' words are istāx (no. 82), tāk (no. 373), šāx (no. 766) — he does not treat ازغ.\"}\n ]\n})\n\ne5[\"nodes\"].append({\n \"id\": 3,\n \"lang\": \"Sanskrit\",\n \"words\": \"adgah : stalk\",\n \"verdict\": \"plausible\",\n \"derivation\": \"The word exists but both its meaning and its membership in this root are uncertain, and only one of Nourai's authorities asserts them. Sanskrit adga- m. is a hapax of the Atharvaveda (AV 1.27.3); Monier-Williams glosses it 'a sacrificial cake (puroḍāśa) made of rice', derived from √ad- 'to eat' with the Uṇādi suffix -gan, and adds 'a cane (?)' with the question mark; Cappeller gives 'stalk, stem, cane'; Böhtlingk-Roth offer both readings ('roughly a reed stalk, stem' or 'a sacrificial cake of rice flour'). So 'stalk' — Nourai's gloss — is one of two competing interpretations of a single Vedic passage. As for the derivation: Mann (IEC 863) is the only book on the shelf that puts it under this root ('Skt. cf. ádgah, m. \\\"cane, stalk\\\"', with his hedging 'cf.'), and Nourai cites exactly that. Pokorny 786 and Walde-Pokorny I 185 list no Indo-Aryan member at all under ozgho-, and Wiktionary's Proto-Indo-Iranian *Hádᶻgas is built on Iranian evidence (MP azg) plus this doubtful Sanskrit word. Phonetically Skt. adga- : Ir. azga- would need PII *Hadzga-, i.e. Sanskrit -dg- against Iranian -zg- — a possible but not routine correspondence, which is part of why the handbooks hedge. Verdict plausible, not confirmed.\",\n \"derivation_fa\": \"واژه وجود دارد، اما هم معنایش و هم عضویتش در این ریشه نااستوار است و تنها یکی از منابع نورایی آن را می‌گوید. سنسکریت adga- تک‌گواهی از اتهرَوَوِدا است (۱:۲۷:۳)؛ مونیر-ویلیامز آن را «نانِ قربانی (puroḍāśa) از برنج» معنی می‌کند و از ریشهٔ √ad- «خوردن» با پسوند اُنادیِ -gan می‌گیرد، و «نی (؟)» را با علامت پرسش می‌افزاید؛ کاپِلِر «ستاک، ساقه، نی» می‌دهد و بوتلینگ و روت هر دو خوانش را نقل می‌کنند. پس «ستاک» — همان معنایی که نورایی داده — یکی از دو تفسیرِ رقیبِ یک بندِ وِدایی است. و در باب اشتقاق: مان (IEC ۸۶۳) یگانه کتابی است که آن را زیر این ریشه می‌نشاند («Skt. cf. ádgah, m. \\\"نی، ستاک\\\"»، با همان «cf.»ِ احتیاطی) و نورایی هم دقیقاً همان را ارجاع داده است. پوکورنی (۷۸۶) و والده-پوکورنی (ج ۱ ص ۱۸۵) هیچ عضو هندوآریایی زیر ozgho- ندارند، و *Hádᶻgas هندوایرانیِ آغازینِ ویکی‌واژه بر گواهیِ ایرانی (azg پهلوی) و همین واژهٔ مشکوک سنسکریت بنا شده است. از نظر آوایی برابریِ adga- سنسکریت با azga- ایرانی به *Hadzga- هندوایرانی نیاز دارد، یعنی -dg- سنسکریت در برابر -zg- ایرانی؛ چنین برابری ناممکن نیست ولی معمول هم نیست، و همین یکی از دلایل احتیاطِ فرهنگ‌نویسان است. داوری: با احتیاط پذیرفتنی است، نه تأییدشده.\",\n \"sources\": [\"https://www.wisdomlib.org/definition/adga\"],\n \"ref_check\": [\n   {\"ref\": \"IEC:863\", \"status\": \"supports\",\n    \"note\": \"Mann p. 863 s.v. odsghos (IEC.txt leaf 481, the printed '863' stands immediately above the lemma): 'odsghos (odzgos, odhgos), a \\\"shoot, branch, stem\\\". WP I, 185. Skt. cf. ádgah, m. \\\"cane, stalk\\\"; Pahl. azg \\\"branch\\\" …' — the arrow and the gloss are Mann's, though his 'cf.' is a hedge.\"}\n   ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"p. 786 (POK_03.txt leaf 21)\", \"stance\": \"silent\",\n    \"note\": \"Pokorny's ozgho- article contains only 'Pehl. azg', 'npers. azaɣ' and the Greek words; no Sanskrit member. Nor does the ozdo-s article (leaves 20-21).\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I 185\", \"stance\": \"silent\",\n    \"note\": \"Walde-Pokorny likewise lists no Indo-Aryan form under ozgho-; the discussion runs Pahlavi–Persian–Greek–Slavic only.\"},\n   {\"src\": \"SYN\", \"where\": \"SYN.txt — searched adga\", \"stance\": \"silent\", \"note\": \"Buck has no entry for this word.\"}\n ]\n})\n\ne5[\"nodes\"].append({\n \"id\": 4,\n \"lang\": \"Old Norse\",\n \"words\": \"oddi : bud, point, triangle, third or any odd number\",\n \"verdict\": \"disputed\",\n \"derivation\": \"The Old Norse word and Nourai's gloss are accurate — oddi m. 'point of land, angle, triangle; a third or odd number', a derivative of oddr 'point of a weapon' — and the gloss is essentially the etymology line of the AHD entry for 'odd' that he cites (AHD:910 is a page of the 1975/76 New College dictionary, in the o- range). But the derivation from the 'branch' root is not the modern view, and Nourai's own preferred authorities do not support it. Pokorny's ozdo-s article (785-786) lists Arm. ost, Gk. ὄζος, Goth. asts, OHG ast and, with Vriddhi, OE ōst / MLG ōst 'knot in wood' — no Old Norse oddi or oddr; his ozgho- article has only Iranian and Greek. Watkins 1985, the revision of the very appendix Nourai's AHD citations point to, has abandoned any such root and assigns ODD to no root at all (grep for 'ozdo', 'zdho', 'ODD', 'Old English ord' in AHD_watkins1985.txt returns nothing relevant). The current account, from Kroonen's Etymological Dictionary of Proto-Germanic via en.wiktionary, is Proto-Germanic *uzdaz 'sharp point', 'possibly from PIE *úd-s (\\\"up, off\\\") + *dʰeh₁- (\\\"to set, put, place\\\")', with an alternative connection to *wes- 'to prick' (cf. Albanian usht 'thistle'); its descendants are ON oddr (> Icel./Far. oddur, Swed. udd), OE ord 'point of a weapon, spear', German Ort, Dutch oord 'place'. Etymonline says the same: 'Proto-Germanic *uzdaz \\\"pointed upward\\\" … PIE *uzdho-, which also gave Lithuanian us-nis \\\"thistle\\\"'. In other words the Germanic word means 'point', not 'branch', it has a West Germanic partner (ord/Ort) that the branch-root cannot explain, and the semantic bridge Nourai needs ('bud' → 'point') is his own. The 'bud' in his gloss belongs to Pokorny's Iranian ozgho- ('Knospe'), not to the Norse word.\",\n \"derivation_fa\": \"خودِ واژهٔ نورس کهن و معنایی که نورایی داده درست است — oddi «دماغهٔ خشکی، زاویه، مثلث؛ عدد سوم یا فرد»، مشتق از oddr «نوکِ سلاح» — و این معنا در واقع همان سطرِ ریشه‌شناسیِ مادّهٔ odd در فرهنگ AHD است که خود او ارجاع داده (AHD:910 صفحه‌ای از متن اصلیِ چاپ ۱۹۷۵/۷۶ در محدودهٔ o است). اما گرفتنِ آن از ریشهٔ «شاخه» دیدگاه امروزی نیست و منابع محبوبِ خود نورایی هم آن را نمی‌پذیرند. مقالهٔ *ozdo-s پوکورنی (۷۸۵–۷۸۶) ارمنی ost، یونانی ὄζος، گوتی asts، آلمانی علیای کهن ast و با وریدی انگلیسی کهن ōst «گره در چوب» را می‌آورد — و هیچ oddi یا oddr نورسی در آن نیست؛ مقالهٔ *ozgho- هم فقط ایرانی و یونانی دارد. واتکینز (۱۹۸۵)، که بازنگریِ همان پیوستی است که ارجاع‌های AHD نورایی به آن اشاره دارد، چنین ریشه‌ای را یکسر رها کرده و ODD را به هیچ ریشه‌ای نسبت نمی‌دهد. روایت کنونی، بر پایهٔ فرهنگ ریشه‌شناسیِ ژرمنی آغازینِ کرونن و به نقل ویکی‌واژه، این است: ژرمنی آغازین *uzdaz «نوکِ تیز»، «احتمالاً از *úd-s هندواروپایی (\\\"بر، برون\\\") + *dʰeh₁- (\\\"گذاشتن، نشاندن\\\")»، با فرضی دیگر پیوند با *wes- «سوزن زدن» (مقایسه کنید با usht آلبانیایی «خار»)؛ بازماندگانش ON oddr، انگلیسی کهن ord «نوک نیزه»، آلمانی Ort و هلندی oord «جای»اند. Etymonline نیز همین را می‌گوید. یعنی واژهٔ ژرمنی معنای «نوک» دارد نه «شاخه»، همتایی در ژرمنی باختری (ord/Ort) دارد که ریشهٔ «شاخه» توضیحش نمی‌دهد، و پلِ معناییِ لازم («جوانه» به «نوک») ساختهٔ خودِ نورایی است؛ «جوانه»ی معنایش در حقیقت از Knospe ایرانیِ *ozgho- پوکورنی آمده، نه از واژهٔ نورسی. پژوهش امروزی این پیکان را رد می‌کند.\",\n \"sources\": [\n   \"https://www.etymonline.com/word/odd\",\n   W + \"Reconstruction:Proto-Germanic/uzdaz\"\n ],\n \"ref_check\": [\n   {\"ref\": \"AHD:910\", \"status\": \"partial\",\n    \"note\": \"AHD:910 is in the o- range of the 1975/76 New College Edition main dictionary, which is not openly readable; Nourai's gloss reproduces that dictionary's 'odd' etymology ('from Old Norse oddi, point of land, triangle, odd number, from oddr, point of a weapon'), so the citation is doubtless faithful to the word and gloss. It cannot, however, support the arrow: the IE-roots appendix of that edition, as revised in Watkins 1985, contains no root *ozdo-/*ozgho- and assigns ODD to no root (searched AHD_watkins1985.txt for ozdo, ozgho, ozdho, zdho, uzd, oddi, 'Old English ord' — nothing).\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"pp. 785-786 (POK_03.txt leaves 20-21)\", \"stance\": \"contradicts\",\n    \"note\": \"'ozdo-s \\\"Ast\\\". Arm. ost \\\"Zweig, Ast\\\", gr. ὄζος ds., got. asts, ahd. ast \\\"Ast\\\"; mit Vriddhi *ōzdos in ags. ōst, mnd. ōst \\\"Knoten im Holz, Knorren\\\"' — the Germanic members of the branch root are asts/ast/ōst, not oddi/oddr; and the ozgho- article next to it is Iranian + Greek only.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 (AHD_watkins1985.txt), roots around ōs-/ost-/ous-/owi-\", \"stance\": \"silent\",\n    \"note\": \"No *ozdo-/*ozgho- root exists in the revised appendix, and ODD appears in it only inside other words (DODDER, SODDEN).\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I 185-186\", \"stance\": \"contradicts\",\n    \"note\": \"WP's ozgho-/ozdos discussion ends by endorsing Scheftelowitz's rejection of the wider Germanic/Celtic annexations: 'Daß zu ὄσχος mit andern Suffixen auch ὄζος (s. *ozdos), ferner air. odb \\\"Knoten\\\", cymr. oddf \\\"Anwuchs, Knoten\\\" gehören sollen, bestreitet Scheftelowitz mit Recht' — i.e. even the Celtic 'knot' words are cut loose, a fortiori the Norse 'point' word.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann p. 863 s.v. odsghos\", \"stance\": \"silent\",\n    \"note\": \"Mann's members are Sanskrit, Pahlavi, Persian, Greek and Welsh; he has no Germanic form under the lemma, so Nourai's Old Norse box has no support even from his main model.\"}\n ],\n \"error_in\": None\n})\n\ne5[\"nodes\"].append({\n \"id\": 5,\n \"lang\": \"English\",\n \"words\": \"odd\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"The edge as drawn — Old Norse oddi → English odd — is correct, and only the root above it is not. Middle English odde (c. 1300, first in the arithmetical sense 'not even, constituting an excess over a pair') is a Scandinavian loan from ON oddi 'a third or additional number' (as in odda-maðr 'the odd man, the one who casts the deciding vote'), literally 'point of land, triangle', a derivative of oddr 'point of a weapon': a triangle is the figure with an extra, unpaired point, whence 'the unpaired one of three'. From there English developed 'singular, rare, choice' (c. 1400) and finally 'strange, peculiar' (c. 1580). The ultimate ancestor is Proto-Germanic *uzdaz 'sharp point' (Kroonen), not a word for 'branch' — see node #4 — so the node's own arrow stands while its pedigree does not.\",\n \"derivation_fa\": \"پیکانِ همین گره — از oddi نورس کهن به odd انگلیسی — درست است و تنها ریشهٔ بالای آن نادرست است. صورتِ انگلیسیِ میانهٔ odde (نزدیک ۱۳۰۰ م، نخست در معنای حسابیِ «فرد، افزون بر جفت») وام‌واژه‌ای اسکاندیناویایی است از oddi نورس کهن «شمارِ سوم یا افزوده» (چنانکه در odda-maðr «مردِ فرد»، آن که رأی قاطع را می‌دهد)، که تحت‌اللفظ «دماغهٔ خشکی، مثلث» است و مشتقِ oddr «نوکِ سلاح»: مثلث شکلی است با نوکِ افزوده و بی‌جفت، و از همین‌جا «تکِ سه‌تا». سپس در انگلیسی معناهای «یگانه، کم‌یاب، برگزیده» (نزدیک ۱۴۰۰) و سرانجام «شگرف، عجیب» (نزدیک ۱۵۸۰) پدید آمد. نیای نهایی ژرمنی آغازین *uzdaz «نوکِ تیز» است (کرونن)، نه واژه‌ای به معنی «شاخه» — بنگرید به گرهٔ ۴ — پس پیکانِ این گره برجاست، هرچند نسب‌نامه‌اش نه.\",\n \"sources\": [\"https://www.etymonline.com/word/odd\"],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\",\n    \"note\": \"Nourai gives this node no reference (refs=None); the parent's AHD:910 is examined at node #4.\"}\n ],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 — searched ODD\", \"stance\": \"silent\",\n    \"note\": \"'ODD' occurs in the appendix only inside DODDER and SODDEN; the word is assigned to no Indo-European root there, though the AHD main dictionary derives it from ON oddi.\"},\n   {\"src\": \"SKT\", \"where\": \"SKT.txt — searched 'Odd, not even', 'oddi'\", \"stance\": \"silent\",\n    \"note\": \"Skeat's entry could not be recovered from this OCR (the hits are OCR noise: 'oddir flooruh aa a flower', 'oddia, the bead').\"},\n   {\"src\": \"KLN\", \"where\": \"KLN_1966.txt — searched 'odd,' and 'oddi'\", \"stance\": \"silent\",\n    \"note\": \"The 'odd' entry falls in a stretch of the scan whose OCR did not yield the headword; no usable text.\"}\n ]\n})\n\ndoc = {\n \"pdf_page\": 378,\n \"book_page\": 348,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-07\",\n \"entries\": [e0, e5]\n}\n\ndef strip_none(o):\n    if isinstance(o, dict):\n        return {k: strip_none(v) for k, v in o.items() if v is not None}\n    if isinstance(o, list):\n        return [strip_none(x) for x in o]\n    return o\n\ndoc = strip_none(doc)\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-378.json','w',encoding='utf-8') as f:\n    json.dump(doc, f, ensure_ascii=False, indent=2)\n    f.write('\\n')\nprint('written')\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-378.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-378.json > /dev/null && echo \"JSON OK\"",
 "description": "Build and validate page-378.json"
}
```


### [2026-09-07T20:40:37.436Z] TOOL RESULT

```
written
JSON OK
```


## [2026-09-07T20:40:42.740Z] TOOL CALL #95: Bash

```json
{
 "command": "python3 tools/verify_check.py 378",
 "description": "Run verify_check for page 378"
}
```


### [2026-09-07T20:40:44.041Z] TOOL RESULT

```
nodes verified: 9/9
node verdicts: {'disputed': 2, 'plausible': 3, 'confirmed': 4}
root verdicts: {'confirmed': 1, 'plausible': 1}
ref checks: {'partial': 9, 'supports': 6, 'not_checked': 2}
books consulted: {'partial': 4, 'contradicts': 4, 'silent': 18, 'supports': 12} | by book: {'WLD': 6, 'HRN': 3, 'POK': 3, 'AHD': 3, 'CHEUNG': 2, 'PHD': 2, 'BQT': 2, 'HUB': 2, 'ARY': 2, 'KLN': 2, 'SKT': 2, 'BRT': 1, 'AVG': 1, 'LAT': 1, 'LEW': 1, 'FSD': 1, 'NYB': 1, 'MON': 1, 'SYN': 1, 'IEC': 1}
```


## [2026-09-07T20:40:51.838Z] TOOL CALL #96: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; ls data/verification/sources/web/ | head -3; f=$(ls data/verification/sources/web/*.json* data/verification/sources/web/index* 2>/dev/null | head -3); echo \"$f\"; grep -o '\"url\": \"[^\"]*\"' data/verification/sources/web/index.json 2>/dev/null | tail -12",
 "description": "Check archived URL index"
}
```


### [2026-09-07T20:40:53.144Z] TOOL RESULT

```
0013bab04a208776.txt
001da4205f642d09.txt
00249560f9f9e9e2.txt
data/verification/sources/web/index.jsonl
data/verification/sources/web/index.jsonl
```


## [2026-09-07T20:40:57.026Z] TOOL CALL #97: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; tail -9 data/verification/sources/web/index.jsonl | python3 -c \"\nimport sys,json\nfor l in sys.stdin:\n    d=json.loads(l); print(d.get('url'))\n\"",
 "description": "Show last archived URLs"
}
```


### [2026-09-07T20:40:58.419Z] TOOL RESULT

```
https://vajehyab.com/moein/%D8%A8%D8%B1%D9%87%D9%86%D9%87
https://en.wiktionary.org/wiki/%D8%A2%D9%87%D9%88
https://en.wiktionary.org/wiki/%D9%86%D8%B4%D8%A7%D9%86
https://www.etymonline.com/word/ocean
https://en.wiktionary.org/wiki/accipiter
https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/peh%E2%82%82-
https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ph%E2%82%82t%E1%B8%97r
https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/p%C3%B3tis
https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/peh%E2%82%82%C7%B5-
```


## [2026-09-07T20:41:05.320Z] TOOL CALL #98: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for u in \"h%E2%82%83%C3%A9h%E2%82%81os\" \"%D8%B2%D9%87%D8%AF%D8%A7%D9%86\" \"word/odd\" \"uzdaz\" \"h%E2%82%83%C3%B3sdos\" \"%E1%BD%84%CF%83%CF%87%CE%B7\" \"oscillate\" \"adga\"; do printf \"%-40s %s\\n\" \"$u\" \"$(grep -c \"$u\" data/verification/sources/web/index.jsonl)\"; done; echo \"--- plain zeh:\"; grep -c '\"https://en.wiktionary.org/wiki/%D8%B2%D9%87\"' data/verification/sources/web/index.jsonl",
 "description": "Verify archived URLs present in index"
}
```


### [2026-09-07T20:41:06.607Z] TOOL RESULT

```
h%E2%82%83%C3%A9h%E2%82%81os             1
%D8%B2%D9%87%D8%AF%D8%A7%D9%86           1
word/odd                                 1
uzdaz                                    2
h%E2%82%83%C3%B3sdos                     1
%E1%BD%84%CF%83%CF%87%CE%B7              1
oscillate                                1
adga                                     1
--- plain zeh:
1
```


## [2026-09-07T20:41:14.444Z] TOOL CALL #99: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; grep -ho 'https://en.wiktionary.org/wiki/Reconstruction[^\"]*' data/verification/page-31*.json | sort -u | head -8",
 "description": "Check URL style in other pages"
}
```


### [2026-09-07T20:41:14.500Z] TOOL RESULT

```
https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/maga%C3%BEs
https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₁lewdʰ-
https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₂ep-
https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/lewk-
https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/mag%CA%B0-
https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/m%C3%A9h%E2%82%82t%C4%93r
https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/m%C3%A1tsyas
https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/Hā́fš
```


## [2026-09-07T20:41:38.331Z] AGENT

Done. `verify_check.py 378` reports **0 PROBLEM lines** (9/9 nodes).

**Page 378 (book p. 348) — 2 charts, 9 nodes; 4 redirect entries skipped**

Verdicts: roots 1 confirmed / 1 plausible · nodes 4 confirmed, 3 plausible, 2 disputed. Ref checks: 6 supports, 9 partial, 2 not_checked. 37 book consultations (12 supports, 4 partial, 4 contradicts, 18 silent).

Disputed:
- **Ôus 2 / Avestan node #1** — `uz-ah, zâ 2`, `zâ-dhana`, `zâ-âp`: there is no Avestan *uz-ah "push out of an opening". The attested form is `us.zan-` = preverb *us-* + verb *zan-* "to give birth" (Bartholomae s.v. zan-, "mit us: erzeugen / gebären / züchten"); Cheung puts it under PIE *ǵenH₁- (Pokorny **373**, not 784). `zâ-dhana` and `zâ-âp` are New Persian زهدان / زهاب, not Avestan. Only `âh` and `aošta/aoštra` belong to the mouth root. Consequently the whole Persian branch (node #2, "plausible") hangs on a wrong root, though زه/زهدان/زهاب themselves are real and do come from *zan-* (Horn no. 645 lists exactly "zeh 'Junges, Kind', zehdān 'Uterus'" under زادن; MacKenzie supplies the missing MP stage zahag / zahār / zahābag).
- **Ozgho / Old Norse `oddi`** — Pokorny's *ozdo-* has Arm. ost, Gk. ὄζος, Goth. asts, OE ōst but no oddi; Watkins 1985 assigns ODD to no root at all; Kroonen/Wiktionary/Etymonline derive it from PGmc *uzdaz "sharp point" < *ud-s + *dʰeh₁-. English `odd` < ON oddi (node #5) is itself confirmed — only the pedigree fails.

Other notable findings:
- `Ozgho, Ozdo` merges **two** separate Pokorny lemmas (785-786 and 786, the latter marked "??"). Nourai's real model is Mann IEC:863 s.v. *odsghos*, which merges them exactly as he does.
- Persian `azm` "child" is not an invention: Walde-Pokorny I 185 records "np. azm '(*Schößling =) Sprößling, Sohn'" from Scheftelowitz — and in the next clause rejects the reconstruction that would license it. It is absent from Borhan, Mo'in and Mann, so his BQT/MON/IEC refs do not cover it.
- Sanskrit `adgah`: a hapax (AV 1.27.3); Monier-Williams glosses it "sacrificial cake … a cane (?)" from √ad-; only Mann links it to this root.
- `ôscillum`: Klein calls it "of uncertain origin", but Ernout-Meillet p. 834 supports Nourai almost verbatim (mask of Bacchus hung in vineyards, Verg. *Georg.* 2.387 ff.).
- BQT:114,115 located as BQT_v1_pages.txt leaves 326/328 (ازغ, اژغ, with Mo'in's footnote "Pahlavi azg"); BQT:1049 as BQT_v2_pages.txt leaf 508; IRN:108 fetched via ref_page.py and quoted verbatim for زه+آب = زاب.

**Extraction errors: none.** The rendered PDF page matches the JSON exactly (checked against the 300 dpi render); no transcription_suspect nodes. 9 web sources archived via fetch_source.py.
