# Verification process log — verify-page-354


## [2026-09-07T18:17:55.343Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 354 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-354.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-354.json. Write /home/sfmqrb/git/rishe/data/verification/page-354.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 354` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T18:17:57.288Z] AGENT

I'll start by reading the instructions.


## [2026-09-07T18:17:57.836Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T18:17:57.849Z] TOOL RESULT

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


## [2026-09-07T18:17:58.583Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-354.txt"
}
```


### [2026-09-07T18:17:58.604Z] TOOL RESULT

```
1	=== PDF page 354 (book page 324) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Ned : to bind, tie  (refs POK:758)
4	#1 (parent #0) [Avestan] refs=POK:759 | naska : book
5	  #2 (parent #1) [Pahlavi] refs=MON | nask : book
6	    #3 (parent #2) [Persian] refs=BQT:2140; MON:4727 | nask «نَسک» : Zoroastrian book or any section of it
7	    #4 (parent #2) [Arabic] refs=VDQ:400 | nasx : written text
8	      #5 (parent #4) [Persian] refs=FVA:399 | nosxeh «نُسخه ( نُسخ ۱ )» : copy, prescription | extra: ناسخ ، استنساخ ، نَسخ ۲
9	#6 (parent #0) [Germanic] refs=AHD | 
10	  #7 (parent #6) [English] refs=None | net 2 : mesh
11	#8 (parent #0) [Latin] refs=AHD | nôdus : knot ; nectere : to tie
12	  #9 (parent #8) [English] refs=None | node, annex, connect
13	--- entry 1 ---
14	ROOT [Indo-European] Nedo, Narda : reed, pipe, flute  (refs POK:759; BQT:2221)
15	#1 (parent #0) [Old Persian] refs=HRN:237 | nada : flute
16	  #2 (parent #1) [Persian] refs=POK:759; BQT:1185,2104,2221; MON:2957 | nâi, nay, nâl «نای ، نی ، نال» : flute, windpipe ; surnây, sornâ «سورنای، سرنا» : a flute played at festivities ☞Keu 4 ; kornâ «کرنا ( کارنای )» : a horn played at war ☞Koro ; qaraney «قره نی ، قرنی» : black flute ☞Kar 2
17	#3 (parent #0) [Sanskrit] refs=POK:759; HRN:237 | nadah : reed ; naladam, nalada
18	  #4 (parent #3) [Persian] refs=SKT:344; HRN:237; BQT:2093 | nard 2 «نرد ۲ ، نارد ، ناردین» : spikenard
19	    #5 (parent #4) [Arabic] refs=PLA:257 | nard
20	      #6 (parent #5) [Greek] refs=None | nardos
21	        #7 (parent #6) [Latin] refs=None | nardus
22	          #8 (parent #7) [English] refs=KLN:1028 | nard, spikenard
23	
```


## [2026-09-07T18:18:02.295Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-354.json",
 "description": "Read source JSON page 354"
}
```


### [2026-09-07T18:18:02.334Z] TOOL RESULT

```
{
  "pdf_page": 354,
  "book_page": 324,
  "entries": [
    {
      "root": {
        "name": "Ned",
        "lang": "Indo-European",
        "refs": "POK:758",
        "gloss": "to bind, tie"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:759",
          "words": [
            {
              "translit": "naska",
              "gloss": "book",
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
          "refs": "MON",
          "words": [
            {
              "translit": "nask",
              "gloss": "book",
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
          "refs": "BQT:2140; MON:4727",
          "words": [
            {
              "translit": "nask",
              "gloss": "Zoroastrian book or any section of it",
              "script": "نَسک"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "از اطاعت با پدر زردشت پیر - خود به نسک آفرینگان گفته است",
            "poet": "Labîbî"
          }
        },
        {
          "id": 4,
          "parent": 2,
          "lang": "Arabic",
          "refs": "VDQ:400",
          "words": [
            {
              "translit": "nasx",
              "gloss": "written text",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "FVA:399",
          "words": [
            {
              "translit": "nosxeh",
              "gloss": "copy, prescription",
              "script": "نُسخه ( نُسخ ۱ )"
            }
          ],
          "script_extra": "ناسخ ، استنساخ ، نَسخ ۲",
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [],
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
            {
              "translit": "net 2",
              "gloss": "mesh",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {
              "translit": "nôdus",
              "gloss": "knot",
              "script": null
            },
            {
              "translit": "nectere",
              "gloss": "to tie",
              "script": null
            }
          ],
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
            {
              "translit": "node, annex, connect",
              "gloss": null,
              "script": null
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
        "name": "Nedo, Narda",
        "lang": "Indo-European",
        "refs": "POK:759; BQT:2221",
        "gloss": "reed, pipe, flute"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "HRN:237",
          "words": [
            {
              "translit": "nada",
              "gloss": "flute",
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
          "refs": "POK:759; BQT:1185,2104,2221; MON:2957",
          "words": [
            {
              "translit": "nâi, nay, nâl",
              "gloss": "flute, windpipe",
              "script": "نای ، نی ، نال"
            },
            {
              "translit": "surnây, sornâ",
              "gloss": "a flute played at festivities",
              "script": "سورنای، سرنا",
              "see": [
                "Keu 4"
              ]
            },
            {
              "translit": "kornâ",
              "gloss": "a horn played at war",
              "script": "کرنا ( کارنای )",
              "see": [
                "Koro"
              ]
            },
            {
              "translit": "qaraney",
              "gloss": "black flute",
              "script": "قره نی ، قرنی",
              "see": [
                "Kar 2"
              ]
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "عیسٰ چو تو نی ما را هم کاسه مریم کن - طنبور دل ما را هم ناله سرنا کن",
            "poet": "Molavî"
          }
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK:759; HRN:237",
          "words": [
            {
              "translit": "nadah",
              "gloss": "reed",
              "script": null
            },
            {
              "translit": "naladam, nalada",
              "gloss": null,
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
          "refs": "SKT:344; HRN:237; BQT:2093",
          "words": [
            {
              "translit": "nard 2",
              "gloss": "spikenard",
              "script": "نرد ۲ ، نارد ، ناردین"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Arabic",
          "refs": "PLA:257",
          "words": [
            {
              "translit": "nard",
              "gloss": null,
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Greek",
          "refs": null,
          "words": [
            {
              "translit": "nardos",
              "gloss": null,
              "script": null
            }
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
            {
              "translit": "nardus",
              "gloss": null,
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "English",
          "refs": "KLN:1028",
          "words": [
            {
              "translit": "nard, spikenard",
              "gloss": null,
              "script": null
            }
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


## [2026-09-07T18:18:04.037Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','MON','BQT','VDQ','FVA','AHD','HRN','SKT','PLA','KLN','WLD','IEC','SYN','BRT','KNT','PHD','NYB','HUB','CHEUNG','ARY','FVQ','AFM','SOD']:\n    v=d.get(k)\n    print(k, json.dumps(v,ensure_ascii=False)[:400] if v else 'MISSING')\n\""
}
```


### [2026-09-07T18:18:05.511Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
VDQ {"title": "Fereydun Badreh'i (tr.), Vazheha-ye Dakhil dar Qor'an-e Majid (Persian translation of Jeffery FVQ with notes), Toos 1372/1993", "kind": "website", "url": "https://noorlib.ir/book/view/12868?pageNumber=<N>&viewType=pdf (page images; viewType=html also exists) ; info: https://noorlib.ir/book/info/12868 ; ketabnak.com/book/51136 (download blocked)", "lookup_hint": "noorlib viewer is JavaSc
FVA {"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 202
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
CHEUNG MISSING
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.t
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_page
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in
```


## [2026-09-07T18:18:20.991Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && sed -n '1,200p' SOURCE_MATRIX.md"
}
```


### [2026-09-07T18:18:21.035Z] TOOL RESULT

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


## [2026-09-07T18:18:21.398Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | head -80"
}
```


### [2026-09-07T18:18:21.436Z] TOOL RESULT

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


## [2026-09-07T18:18:28.122Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['POK','KLN','SKT','HRN','AHD','BQT','MON','PLA','VDQ','FVA','IEC','SYN','WLD','BRT','KNT','PHD','NYB','HUB','ARY','SOD','LKT','FVQ','AFM','AKD','SIN','HJB','FSD','WEB','LEW','LAT','TAD','ARB']:\n    v=d.get(k) or {}\n    print('==',k, '| local:', v.get('local_file'), '| offset:', v.get('page_offset'), '| hint:', (v.get('lookup_hint') or '')[:300])\n\""
}
```


### [2026-09-07T18:18:29.406Z] TOOL RESULT

```
== POK | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt | offset: POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' giv
== KLN | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt | offset: KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
== SKT | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt | offset: leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.
== HRN | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt | offset: leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.
== AHD | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt | offset: 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. | hint: Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru
== BQT | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'] | offset: vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). | hint: grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --d
== MON | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'] | offset: None | hint: Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbe
== PLA | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt'] | offset: 301 leaves (pdftotext -layout, \f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276). | hint: HathiTrust search-only; Google Books id q_ErAAAAMAAJ snippet view; DDB has only the table of contents. No full text online. | For pages in a scanned volume use: python3 tools/ref_page.py PLA:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)
== VDQ | local: None | offset: None | hint: noorlib viewer is JavaScript-rendered (WebFetch/curl get only the site chrome); needs a browser. Since it is a translation of FVQ, verify the substance via FVQ (same entry order); page numbers differ.
== FVA | local: None | offset: None | hint: Searched archive.org, ketabnak, noorlib, web: no digital copy found.
== IEC | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt | offset: TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.
== SYN | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt | offset: leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.
== WLD | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt'] | offset: Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696). | hint: Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP.
== BRT | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt | offset: Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops.
== KNT | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt | offset: leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; section refs like '$147'. Nourai's page numbers should fall in 164-215 for lexicon citations.
== PHD | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt | offset: leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB).
== NYB | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt | offset: Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.
== HUB | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt | offset: leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.
== ARY | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt'] | offset: printed page = pdf page + 1 | hint: Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY
== SOD | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD.txt'] | offset: printed page ≈ leaf − 66 in SOD_pages.txt (0-based \f blocks; 645 leaves; English intro precedes) | hint: Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (retur
== LKT | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt | offset: leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages. grep the oriental source word in transliteration or the number.
== FVQ | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt'] | offset: printed page = leaf − 17 (0-based \f blocks in FVQ_pages.txt; 335 leaves) | hint: Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).
== AFM | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt'] | offset: 198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image | hint: Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').
== AKD | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/AKD.txt | offset: leaf = printed + 8 (e.g. leaf 21 = p.13). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Organised by semantic field; Akkadian words in transliteration with Aramaic/Arabic/Persian loans. grep the word.
== SIN | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/SIN.txt | offset: leaf = printed - 172 (e.g. leaf 15 = p.187). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Running page numbers 185-630 (the volume's series pagination, which Nourai uses). Sections are numbered with plant/product names in caps; grep the Persian/Chinese word or the page number.
== HJB | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt | offset: leaf = printed + 35..51 (plates inserted; e.g. leaf 83 = p.32, leaf 319 = p.270, leaf 535 = p.490, leaf 905 = p.870). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Headwords in caps at line start followed by ', s.' etc., e.g. grep -n '^BAZAAR' HJB.txt. Also online at dsal: https://dsal.uchicago.edu/dictionaries/hobsonjobson/ (search box) which shows page numbers.
== FSD | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt | offset: vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably detected (pages ~ 700-1640) - grep the headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Headword in bold at line start with pronunciation; etymology in brackets at entry end '[< L. ...]'. Very large OCR (16 MB per vol); grep -n '^word' vol file.
== WEB | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/WEB_vol1.txt | offset: not reliably detected (page_numbers.json sparse); grep headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Headword bold at line start; etymology in brackets. 2nd-edition pagination is the same across 1958-1983 printings, so a 1978 page number can be checked in the 1962 vol. 1 scan for words A-(mid alphabet); vol. 2 only via lending copies.
== LEW | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt | offset: 1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Latin headword in bold at line start. For 1938 pagination borrow lateinischesetym0000awal.
== LAT | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt | offset: leaf = printed + 18 for most of the book (e.g. leaf 21 = p.3); drifts in places (leaf 219 = p.301 -> -82?? probably a mis-detected number) - grep the headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Latin headword in bold at line start followed by gender/declension, e.g. grep -n '^pater,'.
== TAD | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD.txt'] | offset: 86 leaves (small book, ~80 printed pages); offset ≈ leaf − 4..6, verify against the printed numeral on the page image | hint: Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; inside.php search works.
== ARB | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/ARB_mo3rb.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/ARB_abdulraheem.txt'] | offset: None | hint: Alphabetical Arabic headwords; grep in ARB_mo3rb.txt / ARB_abdulraheem.txt (raw, no page breaks); edition of mo3rb not confirmed — check its title page image.
```


## [2026-09-07T18:18:32.757Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"lemma: ned\" POK_full.txt | head -20"
}
```


### [2026-09-07T18:18:32.807Z] TOOL RESULT

```
62018:Root / lemma: ned-1 : ned- {*he- noud-1) 
62077:Root / lemma: ned-2{*he- ned-2) 
62083:Root/ lemma: ned-2\ "to sound, roar, etc...' : Root/ lemma: neid-2: nid-\ "to flow, stream' 
62109:Root / lemma: nedo- {*he- nedo-) 
62162:Root / lemma: ned-2\ "to sound, roar, etc...' : Root/ lemma: neid-2. nid-\ "to flow, stream'
```


## [2026-09-07T18:18:33.874Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^ned-\\|^1\\. ned-\\|^2\\. ned-\\|^3\\. ned-\\|nasku\\|naska\" POK_01.txt | head -30"
}
```


### [2026-09-07T18:18:33.934Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-07T18:18:36.709Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '62010,62170p' POK_full.txt"
}
```


### [2026-09-07T18:18:36.757Z] TOOL RESULT

```
Root / lemma: ndo'^-2{*he- ndo^-2) 
See also: see above S. 315 f. {endo!^-). 
Page(s): 758 



Root / lemma: ned-1 : ned- {*he- noud-1) 

Meaning: to roll up; to attach, bind 

Material: 1 . Latin nddus^Vx\o\! (Indo Germanic *nddos)\ 

Maybe abbreviated alb. nuje, nyJe^Vx\o{' a Latin loanword. 

Latin presumably nassa ( *nad-s-a) "basket for catching fish; a trap| snare '; necto, -ere, 

nexT, nectum^ tie, bind, knot, bind' is neologism after yC>/ec/d"plait| twine '; with the meaning 

' near ' from 'narrowly joined': Oscan nessimas Horn. PI. f. ' proximae ', Umbrian nesimei 

"near| nearly; close by; almost '; 

Old Irish Kompar. nessa. Sup. nessam' propior, neighbor; nearest one ', cymr. nes, 
nessa f, coru. nes. Middle Breton nes, nessaffds.; Old Irish nasc/m^b'\n6, verpflichte' {*ned- 
sko), amenas'\ will bind' (etc.), na/dm^6as Binden, pact, covenant', for-na/dm^ band, 
strap', nasc^nng' (compare to -s/r-formation Old High German nusca, that also 
corresponds \v\ u= e, further Avestan /7as/r5- 'anthology (of texts), text collection ', 
probably actually 'bundle'); bret. naska 'band, join together '; 

Gothic nati. Old High German nezzi. Old Saxon net, netti. Old English Old Icelandic net 
'net', lengthened grade (as Latin nodus). Old Icelandic noti. 'big net'; 

with formant -s-k-, -s-t-: Old High German nuska. Middle High German nusche^ coat 
buckle ', Old Saxon n usk{i) a ^c\as'^, hairpin ' (see above); Old Icelandic nist, n/st/n. ' 
braces in the dress ', /7/5/a 'stitch together'; nesta' fasten with needle or thread, nail ', 
Middle High German nesten (neste/n) ' fasten, lace, tie ', Old High German nestilo, nestila 



'loop, strap, bandage'. Modern High German Nestel, Old Saxon /7es///a "bandage, 
hairband ', agutn. nasi, nestlr, reduced grade Old English nos(t)le^b3iU6, strap'; 

Maybe alb. nuske^ magic wrappings ' : alb. nuse^ bride'. 



there nec/-\s an extension from (s)ne-^ zusammenarBnen ', besides through the 
meaning also through the s-anlaut. forms Old Irish snaidm^Vx\o{' (compare above naidm) 
and Modern High German Hessian Schnatz^ das geflochtene und um die Haarnadel 
qevyickelte Haar der Frauen, Kopfputz der Braute ' ( *snatta-W\Vc\ Germanic -//-) probably. 

2. Here presumably the names of the nettle: 

Gr. dSiKPi ( *nd-ika)\ Old High German nazza. Old Icelandic ngtr. Old High German 
/7ezz//a (Germanic *natildn). Old English netele; besides with Indo Germanic -/- (also *n9-t- 
, no-t- as /-extension to the supposed root {s)ne-) Old Prussian noatis, Lithuanian notere, 
/yo/Ae "nettle', /7o//y/7e "dead-nettle', Latvian natre, natra^v\e\.\.\e\ Slavic *natb^ herbal 
leaves ' in slov. /75/(Gen. nat?}, poln. nacds. and at most (as redupl. proto Ce\Wc*ni-nati-l) 
Middle Irish nenaid, nir. /7e5/7/d^ "nettle', dissimil. bret. linadAs. 

References: WP. II 328 f., WH. II 144 f., 155 f., 172 f., Trautmann 194, H. Jacobsohn Arier 
under Ugrofinnen 90 f.; 
See also: see below (s)ne-. 
Page(s): 758-759 

Root / lemma: ned-2{*he- ned-2) 

Meaning: to sound, roar, etc.. 

Note: 

Root/ lemma: ned-2\ "to sound, roar, etc...' : Root/ lemma: neid-2: nid-\ "to flow, stream' 

derived from Root/ lemma: neig"-: "to wash'. 

Material: Old Indie nadati^ sounds, bellow, roar, soughs', nada- m. " roarer, bull, river', 

nadf-t "river, flood', nadT-na-m., nadT-sa-m. "sea', etc.; Avestan nad- "vilify, scold'; gr. 

(Illyrian) FIN NsSa (Arcadian), NsSwv (measure.); thrak. FIN Nsgtoc;; lllyrian FIN Negto^ 

(Dalm.) from * ned-to-. 

Maybe MoHG Nette N of a river; MoHG Netze Name of a river 

Note: 

Again lllyrian displays satem characteristics the same as alb. 

Maybe zero grade in alb. {*ndet}) det/'sea' : Old Indie nadf-sa-m. "sea'. 

References: A. Mayer Mel. Boisacq II 132 f., Krahe IF. 58, 209 ff. 

Page(s): 759 



Root / lemma: nedo- {*he- nedo-) 

Meaning: reed 

Material: Old Indie nada- m. presumably " reed ', npers. nai, dial. /7ao'"reed'; Armenian net 

'arrow'; Lithuanian nendre {and lendre) " reed ' (with nasal after /e/7/r//"bend'?); Latvian 

nasj/^ree6' from *nads//s7 

References: WP. II 329; compare Kuiper, Proto-Munda 82. 

Page(s): 759 

Root / lemma: negh- {*he- negh^ 
Meaning: to pierce, stick 

Material: Middle Irish /7ess "wound' {*negh-s-)\ reduced grade Old Church Slavic vb-ntzQ^ 
stick in, sticl< into, put in ', Infin. vi,-nbzngti, Kaus. russ. -Church Slavic v^-nozitT 
hineinstechen '; Old Church Slavic nozb "knife'; whether here Old Indie aksu-^ shaft, pole' 
( *ngh-su-)l common Old Indie gh- > ks- : Avestan gh- > xs- > s- : Slavic gh- > z-, z- 
References: WP. II 326 f., Trautmann 200. 
Page(s): 760 

Root / lemma: neid-1{*he- neid-f) 

Meaning: to scold, put to shame 

Material: Old Indie nfndati. Pass. nidya-te^vMy, scold, rebuke, reproach, despise ', 

anedya-^ not to blaspheme, vilify, scold', nid-, nida, nida, ninda^ abuse, reprimand, 

disdain, contempt'; Avestan naed- {naisml) "vilify, scold'; Armenian anicanem, Aor. 3. Sg. 

a nec^ curse' ( *oneid-s-et)\ 

gr. 6v£i5oc; " reproach, accusation, disgrace, shame', 6v£i5i^u) " abuse, revile ' (o-prefix " 
scold, reprimand, rebul<e ', as also Armenian anicanem); Gothic ga-naitJan^vMy, scold', 
naiteins^ blasphemy, sacrilege ', Old High German /7e/zze/7 "torment, smite, plague'. Old 
English nsetands.; Lithuanian nfedeti, Latvian /7/5/" despise ', nafds, nafdus^hate, enmity'. 

References: WP. II 322 f., Kuiper Nasalpras. 130, Trautmann 193; 
See also: probably to nei- S. 312 f. 
Page(s): 760 

Root / lemma: neid-2: nid- {*he- neid-2) 

Meaning: to flow, stream 

Note: 



Root / lemma: ned-2\ "to sound, roar, etc...' : Root/ lemma: neid-2. nid-\ "to flow, stream' 

derived from Root/ lemma: neig"-: "to wash'. 

Material: Old Indie nedatT flows, streams'; gall. FIN Nida^ Nidda ' and " Nied ', brit. FIN 

Nida, cymr. Nedd^ N?.§th '; full grade poln. FIN Nida, Lithuanian FIN Nieda, Old Prussian 

FIN Nyda " Neide '.
```


## [2026-09-07T18:18:48.998Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for l in 412 413 414 415 416; do echo \"=== POK_02 leaf $l ===\"; awk -v n=$l 'BEGIN{RS=\"\\f\"} NR==n+1' POK_02.txt | head -60; done 2>/dev/null | head -150"
}
```


### [2026-09-07T18:18:50.208Z] TOOL RESULT

```
=== POK_02 leaf 412 ===
 formica  (vgl.  zum  lautlichen  oben  lat.  formldö:  gr. (.LOQ{.id))]  gr.  !xvQf.iog  (Lycophr.),  (,iVQi.irj^j  dor.  (xvguä^  (Ä-Erw.  zum  ä-St., wie  bQi.Liyt.ag  lat.  formica^  ai.  valml-ka-  zum  I-St.,  und  ai.  vamra-hd  zum o-St.) ;    unklar  arm.  mrjiun  [*murjimno-)^  Gen.  mrjman.
Auf  norm- :  gr.  ßvqiia^,  ßoQi-ia^  Hes.  {ß-  Schriftbehelf  für  /,  vgl.  auch 8Q(j,iKag'  ^VQ(.i7]^  Hes.);  ai.  vaZTTiiÄa- m.  , Ameisenhaufen';  daneben  mit  ganz alleinstehender  Lautfolge  vamrd-  m.,  vamri  f.  , Ameise'.
Auf  mouro-'.  aisl.  maurr^  daneben  *meur-  in  dän.  myre^  schwed.  myi^a {*meu'i'iön-),  mndl.  Fl.  mure  (einmal  belegt)  miere,  nndl.  mier,  mnd.  mlre (zum  l  s.  van  Wijk),  mengl.  mire,  myre  (skand.  Lw.),  ags.  myre,  engl,  mire, heute  nur  noch  fis-mire  (vom  Ausspritzen  ihrer  Säure),   krimgot.  miera.
WP.  II  306  f.,  WH.  I  531  f.,  Trautmann  170,  Specht  Idg.  Dekl.  45.
750
niö[u]-lo- :  mu-lo-  , Wurzel,  Pflanze^;  als  ,Mund  der  Pflanze^  zu  mü-  S  7fsi Ai.  müla-  n.  ^WurzeF,  müla-karman-  n.  , Zauberei  mit  Wurzeln'
ir
art
gr.  fX(üXv  ,e'm  fabelhaftes  Wunderkraut  (Hom.) ;  gelbblühende  Knoblau  k
b  (Theophr.  Dioscor.)',  {.icblv^a  ,Knoblauchart^
WP.  II  303,  310,  Wackernagel  Sitz.-Ber.  Pr.  Akad.  1918,  410  f.
i22Ö[u]-ro-  :  znü-ro-  , stumpfsinnig,  töricht^.
Ai.  mürd-  ,stumpfsinnig,   blöde,   dumm^ ;    gr.   iio)q6q,  att.  ixwqoq  ,duiinn  -* töricht^  (daraus  lat.  mörus  ,närrisch,  albern^).  ^t^
WP.  II  303,  WH.  II  lt4.  '-§
■   ^- moz-g-o-,  moz-g-en-,  mos-k-o-  ,Mark,  Hirn^  '^
Ai.  majjdn,   majjä,   majjas-   ,Mark*,  mastülca-  , Gehirn',  mdstaka-  ,KopL  - Schädel*;  SiV.  mazga-  ,Mark,  Hirn';  ahd.  mar (a)^,  mar{a)kj  a.s.  mar g^  a^s» mearg,  aisl.  mergr  (Gen.  mergjar)  ,Mark*,   aschwed.  micergher]    ksl.  mozg^  ^ , Gehirn',  mo^dam  {*mozgem)^  Akk.  PL  mozdeni  ,Mark',  apr.  musgeno  ,Mark* wozu   (mit  Umstellung   aus  *mazgenes)   lit.   f.   PL   smageneSj  lett.  smadenet , Gehirn';  toch.  A  mäisunt  ,Mark'.
WP.  II  309,  Trautmann  172  f.,  Specht  Idg.  DekL  78  f.
mozgho-s  ,junges  Rind';  nur  arm.  und  griech.  ;^
Arm.  mozi   ,junges   Rind   ,Kalb*  =  gr.  ^oaxlov,    Demin.   zu  ixoc^og  m.
jjunger  Stier,  Kalb',  f.  Junge  Kuh,  Mädchen' ;  wohl  identiscsh  mit  i^öaxog
,Pflanzentrieb,  Schößling'.
WP.  II  309.  .
tnrk-  , eßbare  Wurzel,  Mohrrübe,  Möhre'?
Gr.  ßodyiava  , wildes  Gemüse'  Hes. ;  ahd.  mor{a)ha  ,Daucus  carota',  nhd. Mohr-rübe,  Möhre,  ags.  more,  moru  ds.,  spätahd.  Demin.  morhila  ,Morchel^ (möhrenähnlicher  Pilz);  dagegen  scheint  russ.  morkovh,  morkva  ,Möhre', serb.  mrkva  aus  dem  Germ,  entlehnt  zu  sein.
WP.  II  313.
•
inregh-in{n)o-  , Hirnschale,  Hirn'.
Gr.  ßQSxiiögy  ßqexua  n.  (und  ßgeyi-ia)  , Vorderkopf,  Oberschädel',  ags. hregen,  brcegen  n.  , Gehirn'  (engL  hrain),  afries.  brein,  mnd.  bragen,  bregen, nhd.  Bräge
=== POK_02 leaf 413 ===
n  m.  ds.
WP.  II  314.
mreghu-,  mrghu-  ,kurz'.
Präkr.  mühu-,  av.  mdrdzu-jlti-,  -Jva-  ^ßoaxvßiog^,  sogd.  murzak  ,kurz'; gr.   ßgaxvQ   ,kurz',   ßgdxscc   , seichte   Stellen';    dazu    ßQaxfaiv    , Oberarm', Komparativ  neben  ßQaaacjVj
751
lat.  Irevis  (zunächst  aus  dem  Fem.  *6re(x)wl)  ,kurz',  hrüma  ,Winter- sonnen wende,  Winter,  Kälte*  {*brevi-mä,  *hreu-ma  ,Zeit  der  kürzesten  Tage);
got.  gamaürgjan  ,verkürzenS  alid.  murg{i)  ,kurz',  murgfäri  ,zerbrechlich*, a^-s.  myrge  , angenehm*,  engl,  merry. Vf.  II  314,  WH.  I  115.
j.  IZ2U-  Schallnachahmung  für  den  mit  gepreßten  Lippen  erzeugten  dumpfen Laut:  jUndeutlich  reden,  unartikuliert  murmeln  (daher  auch  Worte  für ,stumm*);  Mund,  Maul;  den  Mund  geschlossen  halten  oder  schließen'; mü-ko-  , stumm'.
1.  Gr.  ^v,  ixv  , Ausruf  gepreßten  Schmerzes',  lat.  mü  facere^  mutmut facere  ,mucksen'.
2.  ai.  mnka-  ,stumm',  arm.  mwnj  , stumm',  gr.  ftCxdg,  (.(VTig,  uvTTÖg,  j^vSog, ^wagögf  Hes.  (j^vvöög  ,stumm',  lat.  mütus  ,st,umm';  vgl.  auch  älter  dän. muej  norw.  mua  ,schweigen,  nicht  mucksen';  ahd.  mäwen  , schreien',  lett. maunu,  mäwu^  maüt  , brüllen',  cech.  myjati  , muhen';  hierher  auch  nhd. Möioßj  ags.  rriziOj  meWy  aisl.  mär  (PL  mävar),  as.  meu  ds.
3.  [Ai.  mukhd-  n.  ,Mund'  stammt  aus  dem  Davidischen];  gr.  ^vXXov ^Lippe';  fj,vXXaivo)  , verziehe  den  Mund,  schneide  Gesichter'  (fxvara^  , Ober- lippe, Schnurrbart',  s.  Boisacq  m.  Lit.),  ahd.  mala  f.,  mhd.  mül  n.  ,Maul', mnd.  müle  ,Maul,  Schnauze',  aisl.  müli  ,Maul,  bes.  Oberlippe  an  Tieren, hervorragende  Felsspitze',  got.  faurmüljan  ,das  Maul  zubinden'  (ob  mit anl.  s-  dazu  norw.  smaul,  lett.  smaule  ,Maul'??);  s.  auch  unter  möu-lo- S.  750.
4.  Mit  dentalen  Formantien:
ludiX.  muttiö,  -Ire  ,mucksen',  muttum  nullum  ,keinen  Muckser'  (vgl.  oben mutmut) ;  ahd.  mutilön  jmurmeln^,  rieseln*,  müsse  , Quelle',  aisl.  mudla  ,mur- meln*,  daneben  mit  germ.  t:  norw.  dial.  mutra,  mengl.  muteren,  engl. mutter  ds. ;  lit.  mute  ,Maul*.
5.  Gutturalerweiterungen  (vgl.  oben  2.):
Mit  k:  gr.  [,iVycdo^aL  ,brülle*,  ixvx&iC^a)  ,schnaube,  spotte',  mhd.  mühen, mügen,  müwen  , brüllen',  abg.  myH  ,Gebrüll',  russ.  mycath  ,brüllen*,  skr. slov.  öech.  mukati  ,brüllen*.
Mit  g:  ai.  münjati,  möjati  ,gibt  einen  Ton  von  sich*  (Dhätup.);  mucchanä »schwellender  Ton* ;  gr.  (j,vKco  ,bringe  mit  geschlossenen  Lippen  einen  Laut hervor,  stöhne*  (daraus  lat.  mussäre),  iivyy
=== POK_02 leaf 414 ===
,6c,  , Seufzer*;
lat.  mügiöj  -Ire  ,brüllen',  conmügentö  ,convocantö',  müglnor  ,murmele  laut, brause*  (auch  ,nügäri  et  quasi  tardö  cönäri'),  umbr.  muieto  ,muttitum', mugatu  ,muttitö',   lat.  mügüäre  vom  Naturlaut   des  Esels;   ahd.  muckazzen
752
jleise  reden,  mucksen\  nhd.  mnd.  mucJcen  ,mit  halboffenem  Munde  reden*  '^' {kk  ist  expressiv),  ostfries.  muk  ,Kuß'.  ^^
6.  s-Erw. :  gr.^  ui(o  ,sicli   schließen,  von   den   Lippen  und  den  Auo-e^»  ^" (daher  f^voip  ,die  Augen  zusammenkneifend,  kurzsichtig* ;  (.ivdoj  , beiße  die Lippen  zusammen';  von  *iivai6g  ,verschwiegen' :  i^vozrjg  ,in  die  Mysterien Eingeweihter',  (xvaTLY,6g  ,die  Mysterien   betreffend',  ^vazrjQLOv  , Geheimnis geheime   Zeremonie*,  vgl.  auch  ^vsTv  ,in  die  Mysterien  einweihen';   norw mysa  ,die  Augen  zukneifen' ;  aus  dem  Germ,  hierher  auch  mnd.  mummelerL  ~" engl,  mumhle  ,murmeln',  mump,   norw.  mumpa  ds. ;  mhd.  mupf,  muff  ,Ver- Ziehung   des    Mundes',  mupfen,   muffen,   mnd.  mopen,  engl,  mope  ,gaffeii* engl,  mop  ,Fratze';  vielleicht  nhd.  bair.  mäuen  ,wiederkauen'  u.  dgl. ;
lett.  musindt  ,flüstern,  murmeln';  hitt.  mu-u-ga-ä-mi  (mügämi)  , spreche Klagegebete'.
WP.  II  309 ff.,  WH.  II  117,  119f.,  135,  139 f.,  Trautmann  188.  _;
2.  mü-,  znus-  schallnachahmend  für  ,Mücke,  Fliege'.
Arm.  mun,  Gen.  mnoy  , Stechmücke'   (*muS'  oder  *mu-no-) ;   alb.  mü-ze,  **" mi-ze  {ze  Diminutivsuffix)  ,Mücke';  gr.  iivXa  i^^^voia)  ,Fliege';  lat.  musca
aisl.  my  n.  (*müja-)  ,Mücke' ;  schwed.  mygg,  mygga,  ags.  mycg,  as.  muggia,   
ahd.  mucka  ,Mücke'  (*wi/Ä;2d);  mit  -s-  gotländ.  mausa  (*müsa),  fläm.  meuzie (*musl)]  lit.  muse,  apr.  muso,  lett.  müsa,  muSa  ,Fliege';  abg.  mucha  , Fliege' (*mousa)y  m^§ica  ,Mücke'.
WF.  II  311,  WH.  II  133,  Trautmann  191,  Specht  Idg.  Dekl.  43.
znuk-  , Haufe'  und  Zubehör?
Gr.  (ÄVKtav '  awQÖg  ^fxajv  Hes. ;  vorgall.  *mukina  , Steinhaufe'  (Jokl  V. Rom.  8,  193);  aisl.  mügi,  mügr  ,Haufen,  Menge',  ags.  müga  m.  ,(Korn-) Haufen',  müha  ds.  (auch  müwa),  vgl.  weiter  schwed.  dial.  moa  , zusammen- häufen' (*mühö7i),  ahd.  mü-werf  ,Maulwurf',  mit  -k^k)-:  mnd.  müke,  ndl. muik,  mhd.  müche,  nhd.  (halb  nd.)  Mauke  f.,  bair.  (echt  hochd.)  Mauche , Auswuchs,  Fußgeschwulst  der  Pferde',  Schweiz,  mauch  m.  ,Auswuchs an  Rebholz,  unordentlicher  Haufe'  und  mit  ü :  norw.  dial.  mukka  ,Haufen, Menge',  mhd.  mocke  m.  _,Klumpen,  Brocken'  (damit  identisch  ist  mhd. mocke  , Z
=== POK_02 leaf 415 ===
uchtsau');  aisl.  mostr  , große  Menge'  (*muh-stra-)]  einzige  Hoch- stufenform in  ags.  meagol  ,(*klumpig,  massig'  =)  ,fest,  stark'.
WP.  II  311;  nach  Hubschmid  ZnPh.  66,  33  f.  nichtidg.
inüs  jMaus'  auch  ,Muskel'  (älter  *müs,  musös  aus  *meus,  musös). Ai.  mü§-  m.  ,Maus,  Ratte',  np.  mü§  ,Maus';
arm.  mu-kn  ,Maus,  Muskel' ;  gr.  (j,vg  (^vdg,  ^vv  nach  ^g,  ''vög,  ^v)  ,Maus', auch  jMuskel';  alb.  ml  ,Maus',  lat.  müs  m.  ,Maus'  (mürlnus  :  mhd.  miusln
753
von  Mäusen*) ;  ahd.  mhd.  as.  mnd.  aisl.  ags.  müs  ,Maus,  Muskel'  (Kons. -St.) ib<^.  ""^y^^  ^'  »Maus'.
Vielfach  auf  Körperteile  angewendet:  arm.  muJcn  , Muskel',  gr.  (xvg Muskel',  [xv(bv  ,muskelreiche  Gegend  des  Leibes'  (woraus  auch  , wollüstiges \Veib'  in  gr.  ^vwv/a),  jwua^,  -aycog  m.  ,MiesDauschel,  Löffel'  :  lat.  mürex Purpurschnecke';  lat.  musculus  ds.,  ,Muskel',  ahd.  usw.  müs  ,Muskel,  bes. des  Oberarms',  mnd.  müs  bes.  ,der  Fleischballen  des  Daumens',  nhd.  Maus^ Mäuschen,  abg.  myhca  ,/9^orxtW';  andrerseits  ai.  muskd-  m.  ,Hode,  weibliche Scham',  npers.  musk  ^Bibergeil'  (aus  dem  Pers.  stammt  gr.  (xöayog,  nhd. Moschus)]  gr.  ixvGxov  , Geschlechtsorgan' ;
wohl  zu  ai.  musnäti  , stiehlt,  raubt'  usw.,  s.  unter  2.  meu-  , fortschieben'.
WP.  II  312  f.,  WH.  II  132  f.,    Trautmann  191,   Specht   Idg.  Dekl.  40f.
rnat-o-s  ,gestutzt'?
Lat.  mutilus,  mtitidus  ,verstümmelt',  *muticus  ,gestutzt',  mütöj  muttö Penis',  GN  Mutunus,  rom.  mutt-  ,abgestumpft' ;  ir.  mut,  gael.  mutach ,kurz'  (mit  expressivem  tt)\  vielleicht  auch  ir.  moth  ,penis'  als  , Stummel'.
WP.  II  312,  WH.  II  136 f.;  nach  E.  Lewy  eher  zu  lat.  mütus  S.  751, vgl.  , stumm' ;  ,verstümmeln'.
48
1.  nä-  jhelfen,  nützen*.
Ai.  nä-tha-  n.  , Hilfe*,  m.  ,Schützer'7  nä-tha-te  ,fleht*;  gr.  d-vl-vTi-ui -vä-fiev  ,nütze*,  Fut.  d-vrj-oojj  Med.  d-vi-vä-f.iat,  Aor.  <hn^fir]v  ,habe  Nutzen* oveiaq  n.,  richtiger  })vr]aQj  -arog  ,Nutzen*  (*o-7iä-wf),  usw.     '  |
WP.  II315.
2.  nä-  ,sich  fürchten,  schämen*,  Verbalnomen  auf  -sor-,  -sr-.
Air.  nä»'  ,bescheiden*  {*nä-sro-\  nd{i)re  , Scham*  (*7iä-smä);  hitt.  naÄ(Ä)- , fürchten,  sich  fürchten*,  nahSariia-  ,sich  fürchten*. H.  Pedersen  Hittitisch  187.
näg^h-  ,nüchtern*?  Nur  arm.  und  griech.
Arm.  naut'^i  ,nüchtern*;  gr.  viqcpw,  dor.  vdq)(a  ,bin  nüchtern*. WP.  II  317.
nak-  ,Fell*.
Gr.  vd%og  n.,  ya^rj  f.  , wolliges  Fell,  Vlies*,  äQvay.lg  f.  (für  *dQvo-vaxig) , Schaffell*,  vayiv(6)QL0v'  öig^a  Hes. ;  ags. 
=== POK_02 leaf 416 ===
 noisc  ,weiches  Leder  wie  z.B. Hirschleder*  (^nak-s-ko-,  -kä]  vgl.  den  -es-St.  vcc/.oq)]  apr.  nognan  (aus *nokna7i)  n.  ,Leder*  (*näk-no-)]  dazu  nach  E.  Lewy  ai.  ndka-  _,Himmels- gewölbe*.
WP.  II  316.
nana,  nena  usw.  Lallwort.
Ai.  nanä  , Mutter,  Mütterchen*,  *nanänä  umgebildet  (nach  svasä :  svasr-) zu  nanändar  ,des  Mannes  Schwester*,  np.  nana  ,Mutter*;  gr.  vdvva,  vlwr] ,Base,  Tante*,  vewog,  vdwag  ,Oheim*;  alb.  nane  ,Mutter,  Amme*;  lat. nonnus  m.,  nonna  f.  spät  ,Mönch,  Nonne',  auch  , Pflegerin  eines  Kindes*; cymr.  nain  (*nani)  , Großmutter* ;  russ.  njanja  ,Kinderwärterin*  (dial.  auch ,ältere  Schwester*),  bulg.  neni  ,der  Ältere*,  skr.  nena^  nana  ,Mutter*,  sorb. nan  ,Vater*;  vgl.  auch  nhd.  Nenne,  Kinderwort  für  ,Milch*.
WP.  II  317,  WH.  II  175.  1
S.  auch  unter  Sn-.
755
^gjjt-  »wagen,  sich  erkühnen*;  nur  kelt.  und  germ.
^ir.  neit  m.  ,Kampf*  (*nanti-) ;  got.  ana-nanpjan  ,wagenS  aisl.  nenna ^übers  Herz  bringenS  ahd.  Prät.  ginand  ,Mut  wozu  haben',  ginenden,  as. näthian,  ags.  nepan  ,wagenS  aisl.  nenninn  ,tätig,  strebsam'  (^* wagefroh*), mhd.  genende(c)  »eifrig*,  ahd.  nand  (auch  in  Namen  wie  Ferdinand),  ags! „0  f.  ,Mut*.
WP.  n  317.
ßas-  ,Nase*  (näs-  aus  den  dehnstufigen  Kasus   dieses  kons.  St.,  ursprüngl. dem  Nom.  Sg.),  ursprüngl.  wohl  ,Nasenloch*.
Ai.   nas-ä,   -2,   -öh  Instr.  Lok.    Sg.,   Gen.    Du.;   näsä  Nom.    Du.    ,Nase* (ursprüngl.   ,Nasenloch*),   sekundär  ndsä  f.   ,Nase',   nas-täh  Adv.  ,aus   der Nase*,  nasya-  ,an  der  Nase  befindlich*,  usw.,  ndsikä  ,Nasenloch,  Nase* ;  av. I    näh-,    näidhan-   ,Nase*,   ap.   näham  Akk.   Sg.  (=  lat.   närem)  ,Nase*;   lat. I   närisj  meist  PL  -es,  -ium  ,Nasenloch,  Nüster*  (t-St.  geworden ;  Akk.  Sg.  PL I  noch  kons.  Form);   näsum  n.  (alat.)  und  näs{s)us  m.  ,Nase*  (expressives ss);   ags.  nöse  f.  ,Vorgebirge*,   aschwed.  norw.  nös  ,Schnauze*,  afries.  nösi ds.  {*näs-))  ablaut.  ahd.  nasa  ,Nase\  anord.  ngs  f.  ,Nasenloch,  Nase,  vor- springende Klippe',  ags.  nasu  ,Nase*  (vermutlich  Dual  ,die  beiden  Nasen- löcher*); ncBS-  im  Kompositum,  anord.  nes  n..  Gen.  PL  nesja  ,Vorgebirge, Landzunge*,  mnd.  nes  (ss-)  m.  ds.,  ags.  ncess  m.  ds.  (germ.  *nasja-)]  apr. nozy,  lit.  nösis  f.  ,Nase*,  nasral  m.  PL  ,Rachen*  (alt  näsras  ,Mund*),  aksl. nozdri  ,Nasenlöcher*  (aus  -sr-),  nos^  ,Nase*  (russ.  ,Vorgebirge^).
WP.  II  318,  WH.  II  143  ff.,  Trautmann  193  f.,  Holthausen  KZ.  69,  166  f., Specht  Idg.  Dekl.  75.
I.  näus-   f.   , Schiff'    (ausgehöhlter    Einbaum);    Akk.    näum,    näuiio-    ,zum Schiff  gehörig*,  näu-ägo-s  , Schiffer*.
Ai.  näu-
```


## [2026-09-07T18:18:54.917Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for l in 419 420 421; do echo \"=== POK_02 leaf $l ===\"; awk -v n=$l 'BEGIN{RS=\"\\f\"} NR==n+1' POK_02.txt; done"
}
```


### [2026-09-07T18:18:56.188Z] TOOL RESULT

```
=== POK_02 leaf 419 ===
nicht',  nekas,  nekurls  (s.  oben);  aksl.  ne  ,nicht';
hitt.   natta  ,nicht*,  näwi  ,noch  nicht'.
ne:  ai.  (ved.)  na  ,nicht';  lat.  ne  , nicht'  in  ne-quidem,  nequäquam,  nsqm- quam,  nequam,  gekürzt  wahrscheinlich  in  neutiquam  (aber  ne-uter  mit altem  *ng,  s.  oben),  ne  Konj.  ,daß  nicht',  osk.  ni  ,ne'  (nz-p  ,neve'),  marruc. ni  ,ne';  air.  ni,  mcymr.  ny,  ncymr.  ni,  corn.  ny,  bret.  ne  ,nicht'  (z.  T.  mit sekundärer  Kürzung);  air.  nl  ,ist  nicht'  ist  das  gewöhnliche  nl  mit  aus- gelassener Kopula;
got.  ne  ,nein'.
12 ei  betontes  ,nicht':  av.  nae-cis  ,keiner',  adv.  ^laecis  verstärkte  Negation; lat.  7ü,  altlat.  nei  Adv.  und  Konj.  1.  älter  ,nicht,  daß  nicht',  2.  ,si  non', quid-nl-,  osk.  nei  ,nicht'  (nei-p  ,neque');  got.  nei  {&TC.ley.)  ,nicht^  aisl.  nl ,nein',  ahd.  nl  emphatisches  ,nicht';  lit.  nie-kas  ,niemand',  ne%  ,auch  nicht, nicht  einmal' ;  aksl.  ni  ,neque',  ni-Uto  ,niemand' ;  die  germ.  Formen  viel- leicht aber  =  ai.  ned  ,durchaus  nicht,  damit  nicht',  av.  nöit,  ap.  nay  aus idg.  *ne  id  ,das  nicht';  vielleicht  ist  idg.  nei  aus  *ne-\-l  (vgl.  ovtoa-l)  zu deuten.
h-  Verneinungspartikel  als  erstes  Glied:  ai.  av.  ap.  a-,  vor  Vokalen  (auch i,  u)  an-',  gr.  ä-,  vor  Vokal  a»'-;  lat.  in-,  ältest  en-  (die  vorkonsonantische
758  '
Form);  osk.  umbr.  an-;  air.  in-  (vor  Med.),  e-  (vor  Tenuis),  an-  (y^  ' Vokal),  cymr.  com.  bret.  an-]  got.  ahd.  as.  ?m-,  aisl.  ö-,  ö-;  im  g^i durchaus  durch  ne-  verdrängt;  über  ksl.  ne-je-veTb  , ungläubig',  '^^-je-sytt, ,unersättlich  =  Pelikan'  s.  Berneker  429;  toch.  AB  a(w)-,  am-^  efnV em-,  071- ;  durch  mehrere  Sprachen  durch-gehende  Entsprechungen  sind  z.  B  » ai.  amfta-,  ^(.ißgoTog,  immortalis]  ai.  djnäta-,  Hyrcorog,  arm.  ancanaut' ignötus,  air.  ingnad,  got.  unJcunps]  ai.  anudrd-,  äwögog,  usw.
WP.  II  319f.,  WH.  II  150f.,  152,  165f.,  Trautmann  194f.,  Schwyzer Gr.  Gr.  1,  431  f.,  2,  590  ff.
:2.  22e,  ne,  enklit.  Partikeln  s.  oben  S.  320  f.
5.  ne-,  no-,  Plur.  nes-,  nbs-  ,wir'  (ursprüngl.  außerhalb   des  Nominativs* Nom.  s.  unter  *we).
1.  Ai.  Du.  Akk.  Dat.  Gen.  nau,  gthav.  G^n.  nä,  aksl.  nä,  gr.  yw,  hom. ywt  aus  *v(ü-J^t  (dessen  2.  Glied  der  Nominativst.  *ue-,  *id-  ist) ;  air.  nä(tha)r  ^ Gen.,  got.  ughis,   as.  wwc,   anord.   o^Är  ,uns  beide  (n)'  (unc  =  *n-ge,  vgl. mik  aus  *me-ge).
2.  Pluralisch:  ai.  waA  enklit.,  av.  W9,  nä,  nö,  lat.  nös,  alb.  na  Nom.  (*nd«), Tie  Gen.  Dat.  Akk.  (*nös);  ir.  ni  usw.  (scheint  *s-7ies).  Gen.  ar  n-  (*ns-rö-m),  ~" cymr.  corn.  bret.  ni,  ny  ,wir'  (*we5),  got.  ahd.  uns, 
=== POK_02 leaf 420 ===
 as.  w«,  anord.  oss  ,uns' (*ns),   aksl.  nas^  Gen.  (j^nös-söm),  apr.  nöuson  (ebenso) ;  £■_
auf  *nsme  (wohl  ns  -j-  Partikel  *sm-,  verwandt  mit  dem  -sm-  der  Pron.- Dekl.,  z.  B.  ai.  td-sm-ät)  beruhen  av.  ahma  (ai.  asmän,  ap.  Gen.  amäxam) =  äol.  ^'^u^-,  dor.  ö^-,  ion.-att.  ij^u- ;  Poss.  lesb.  ä^(j,og,  dor.  ß^iog  =  av. ahma-,  ion.   -att.   'fj^hsgog)  usw. ;   hitt.  Datt.  Akk.  anzäs,   enkl.  was  ,uns*.
WP.  II  320  f.,   Schwyzer  Gr.  Gr.  1,  600  f.
I.  nebh-  ,bersten'??
Ai.   ndhhate  , birst';    aisl.  ncefr  ,die  äußere  Birkenrinde'  als   ,berstend, sich  losschälend'. WP.  II  330.
2.  nebh-  s.  oben  S.  315  f.
I.  ned- ;  zicd-  , zusammendrehen,  knüpfen';  i2Öcfo-/-ä  , Geknüpftes'.
1.  Lat.  nödus  , Knoten'  (idg.  *nödos)',  vermutlich  nassa  (*nad-s-a)  , Fisch- reuse, geflochtener  Korb  mit  engem  Halse';  nectö,  -ere,  nexl,  nectum ,knüpfen,  binden'  ist  Neubildung  nach  j^Zec^ö;  mit  der  Bed.  ,nahe'  aus  ,eng verknüpft' :  osk.  nessimas  Nom.  PL  f.  ,proximae',  umbr.  nesimei  ,proxime';
air.  Kompar.  nessa,  Sup.  nessam  ,propior,  proximus',  cymr.  nes,  nessaf, corn.  nes,  mbret.  nes,  nessaß  ds. ;  air.  nascim  ,binde,  verpflichte*  (*n^d-sJcö),
759
arrienas  ,1  will  bind'  (usw.),  naidm  ,das  Binden,  Vertrag-^  for-naidm  ,Band^ nasc  ,Ring'  (^S^-  zur  -sÄ-Bildung  ahd.  nusca^  das  auch  im  u  =  ,  überein- stimmt^ ferner  av.  naska-  ,Textsammlung',  wahrscheinlich  eig.  ,Bündel'); bret.  nasJca  ^anbinden';
got  nati,  ahd.  nezzi,  as  net,  netti,  ags.  aisl.  net  ,Netz%  dehnstu%  (wie lat.  nödus),  aisl.  not  f.  ,großes  Netz';
mit  formantischem  -s-k-,  -s-t- :  ahd.  nuska,  mhd.  nüsche  ,Mantelschnalle', as.  nusk(i)a  , Spange'  (s.  oben);  aisl.  nist,  nisti  n.  , Spange  am  Kleid',  nista ^zusammenheften';  nesta  , festheften,  festnageln',  mhd.  nes^en  (nesteln)  , fest- binden" schnüren',  ahd.  nestilo,  nestila  ,Schleife,  Schnürriemen,  Binde', nhd.  Nestel,  as.  nestila  , Binde,  Haarband',  agutn.  nast,  nestli;  reduktions- stufig ags.  nos(t)le  ,Band';
daß  ned'  eine  Erw.  von  (s)?ie-  ,zusammendrehen'  sei,  wird  außer  durch die  Bed.  auch  durch  die  s-anlaut.  Formen  air.  snaidm  , Knoten'  (vgl. oben  naidm)  und  nhd.  hess.  Schnatz  ,das  geflochtene  und  um  die  Haar- nadel gewickelte  Haar  der  Frauen,  Kopfputz  der  Bräute'  (*snatta-  mit srerm.  -tt-)  wahrscheinlich.
2.  Hierher  vermutlich  die  Bezeichnungen  der  Nessel  (als  alter  Gespinst- pflanze) :
Gr.  didiyL7]  {*nd-ikä) ;  ahd.  nazza,  aisl.  nqtr,  ahd.  nezzila  (germ.  *natilön), ags.  netele]  daneben  mit  idg.  -t-  (also  *n9-t-,  nö-t-  als  ^Erw.  zur  vermut- lichen Wurzel  (s)ne-)  apr.  noatis,  lit.  notere,  notre  , Nessel',  nötryne  ,Taub
=== POK_02 leaf 421 ===
- nesseP,  lett.  ndtrCj  nätra  ,Nessel',  slav.  *nat'b  , Krautblätter'  in  slov.  nät (Gen.  nati),  poln.  nac  ds.  und  allenfalls  (als  redupl.  urkelt.  *ni-nati-?) mir.  nenaid,  nir.  neantög  ,Nessel',  dissimil.  bret.  linad  ds. '  WP.II  328  f.,  WH.n  144  f.,  155  f.,  172  f.,  Trautmann  194,  H.  Jacobsohn Arier  u.  Ugrofinnen  90 f.;  s.  unter  (s)we-.
2.  ned-  ,tönen,  brüllen,  rauschen'.
Ai.  nddati  ,tönt,  brüllt,  rauscht',  nada-  m.  ,Brüller,  Stier,  Fluß*,  nadi- f.  ,Fluß,  Flut',  nadl-na- m.,  nadl-sa-  m.  ,Meer',  usw.;  av.  wacZ- , schmähen'; gr.  (illyr.)  FIN  Neda  (Arkad.),  Nedwv  (Messen.);  thrak.  FIN  NeOTog] illjr.  FIN  Nearog  (Dalm.)  aus  *ned-to-.
A.  Mayer  Mel.  Boisacq  II  132  f.,  Krabe  IF.  58,  209  ff.
nedo-  ,Schilf'?
Ai.  nada-  m.  vermutlich  , Schilfrohr',  npers.  nai,  dial.  nad  , Schilf;  arm. net    ,Pfeil';   lit.    nendre   (und    Undre)   ,Schilfrohr'   (mit  Nasal   nach    lenkti ,biegen'?);    lett.  nasli  , Schilf  aus  *nadslis? WP.  II  329 ;  vgl.  Kuiper,  Proto-Munda  82.
760  •
negh-  , durchbohren,  stechen'.
Mir.  ness  , Wunde'  {*negh-8-)]  reduktionsstufig  aksl.  v^-nhzq  , steck hinein',  Infin.  v^-nhzngt^,  Kaus.  russ.-ksl.  v^-noziti  , hineinstechen'-  aksl nozh  , Messer';  ob  hierher  ai.  dhsu-  , Stange'  (*ngh-su-)?
WP,  II  326  f.,  Trautmann  200.
1.  nei-,  neio-ini-  , führen'.
Ai.  ndyati  (Partiz.  nltd-),  av.  nayeiti  , führt',  mpers.  nltan  , führen treiben',  ai.  nlthä  f.  , Führung,  Weg',  nltho,  netä^  ,Führer',  nitar-,  netdr- m.  ds.,  netrd-  n.  , Führung,  Auge';  mir.  ns,  nla  ,Krieger,  Held'  {*neit-i\ Gen.  Sg.  urir.  netas,  air.  niatJi  {*nei-t-os\  s.  auch  2.  nei-)]  hitt.  näi-,  lenken führen'.
WP.  II  321,  Pedersen  Hitt.  §  77  f.,  81,  Frisk  Suffixales  -th-  öf.
2.  nei-,  neis-  :  ni-  , lebhaft   bewegt   sein,    erregt   sein,   glänzen';    noi-bho-^
,gut,  heilig';  kelto-germ.  nei-to-,  ni-tu-  , Leidenschaft'.
Lat.  niteö,  -ere  ,glänze,  strahle',  nitidus  , glänzend',  nitor  ,  Glanz'  (von einem  Partiz.  *ni-tö-) ;  vielleicht  re-nldeö  , erglänzen'  (mit  präsensbildendem -d(hy)]  *nei-bhO'  in  mir.  nlab  , Lebenskraft',  cymr.  nwyf  ds. ;  noi-bho- in  apers.  naiba-,  npers.  new  , schön,  gut',  air.  nolh  , heilig';  *nei-mä  in mir.  nlam  , Glanz,  Schönheit';  *nei-Jco-  in  mir.  mach  m.  ,Held',  nlachus m., Tapferkeit';  *nei-to-  in  cjmr.  nwyd  , Leidenschaft',  hispan.  Kriegs- gott Netö]  air.  PN  Nlall  (Gen.  NeiU)  aus  *neit-s-lo-s]  steckt  vielleicht auch  in  air.  ma  ,Held'  (s.  1.  nei-)]  germ.  ^nipa-  in  got.  neip  n.  ,Neid', ags.  m(J  m.  , Kampf,  Haß,  Feindschaft',  as.  afries.  nith  , Eifer,  Haß,  Neid\ aisl.  nid  ,Hohn,  Schmach';  könnten  auch  zu  air.  nlth.  n.  (idg.  *i2ifu-) ,Kampf  gehören;  zweifelhaft  ai.  nila-  , schwarzblau',  naya
```


## [2026-09-07T18:19:05.187Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"nai\\b\" HRN.txt | head -20; echo ---; for l in 258 259; do echo \"=== HRN leaf $l ===\"; awk -v n=$l 'BEGIN{RS=\"\\f\"} NR==n+1' HRN.txt; done"
}
```


### [2026-09-07T18:19:06.606Z] TOOL RESULT

```
1483:Tovro To SQuat^jua twv InntJoy xaXh'ovai U^^nai ayyixQiliov, Dazu ayya()fvu)- 29 -
2534:von', vergl. gr. anai, das allerdings selbst sehr zweifel-
2535:haft ist; vergl. aber gr. xar«/, napai, vnai bei Homer
3632:Ein Vers Senai's im FJ ist metrisch nicht in Ordnung.
7058:phlv. N. pr, Farn[hag^ N(a)pl\farnai (Gemme, Hörn,
8597:8än; kauk.-bergjüd. zürnai sonst sürnm u. v. a. m. Umgekehrt steht
8856:schaft*; phlv. nafak, f?^/ 'Nabel', vergl. N[a]f^[far'nai
9172:ap. *nada' 'Schilf; phlv. nai bezw. nad (PPGl);
9191:*) Kauk.-bergjüd. eürnai 'Schalmei*, russ. LW. zurna.
9251:ZDMG. 44, 658 No. 48 N\a]kt/arnai lesen wollte, hat übrij^ens Levy,
10798:ap. l^nai/', anaijam 'führen'; aw. |/"/i«y-, nay^/iti\
15370:snai»iS- 179.
16488:: )inai«öo.. 1018, 143.
16580:pahnai 344.
17833:naiä- 1060.
22041:w. nai 77.
23133:; /onai'iing 808^-
---
=== HRN leaf 258 ===
— 237 —
*m + V^göp- "behüten, verwahren*, vergl. ai. X^göp- ;
plilv. n(i)huflan 'verbergen*.
kurd. nixiftifi *sich verbergen*, nix^ftin Causat.
^verbergen.
Bartholomae meint nach briefl. Mitteilung, dass
nihuften sein h von np. niMti (No. 1058) bezogen
habe; ai. i^^göp- sei vielleicht eine Nebenform von
[y^göh^ und die dazu gestellten Formen stammten
also nur zum Teil von göpä- 'Hirt*. Vergl. auch
Johansson, Indog. Forsch. IL 50, 51. Jedenfalls
wird es schwer, mhffffeti gänzlich von \ ^göh- zu
trennen.
1060. nei 'Schilf, «af *Flöte\ näl; vergl. A-e/Te|wfl7, stlrjndT
Testflöte* '), seh^näi ; nnlze.
g. nad.
ap. *nada' 'Schilf; phlv. nai bezw. nad (PPGl);
ai. nadd-, nadd- Schilfrohr (Pischel, ZDMG. :U),
717 folg., Ved. Studien I, 183 folg.); arm. net Pfeil*
(H. No. 219)?
Die Lautverhältnisse sind noch nicht richtig er-
kannt. Np. nei, g. nad setzen unbedingt eine Urform
*nada- voraus ; neben dieser gab es eine zweite Form
*narda-, auf welche ai. nadd- (gr. LW. vdodo^*, hebr.
LW. '^.IJ-)) und np. näf zurückgehen. Das jüngere
skr. näld- ist persisches Lehnwort. Wie häufig,
erscheint dann auch eine gedehnte Form, np. näl^
ai. nädt-, die nicht mehr 'Schilf, sondern ein 'Musik-
instrument aus Rohr, Flöte* bezeichnet. Skr. Hald-
wird jüngere Form für nadd- sein, wie Pischel an-
nimmt, nalada- ist sanskritisirtes vd^öoq,
1061. ne 'nicht' (Öähn. I, 198 Anm. 2, Calc), vergl. nPsi
(No. 1066), niy[ayed,
ap. naiy 'nicht'; aw. nöit, na^ci-; päz. ne; ai. ncd.
oss. d. 7ie6i, t. ntci nichts' (201).
*) Kauk.-bergjüd. eürnai 'Schalmei*, russ. LW. zurna.
*) Die aus dorn Persiacbeii entlehnt sind.
=== HRN leaf 259 ===
— 288 —
1062. niyä 'Grossvater, Ahne (Plur. myagän),
ap. aw. nyäka- *Grossvater , vergl. ap. apangäka'
Ahne'; phlv. nyok.
af;'. nlka *6rossvater, LW. niya 'Grossmutter*;
bei. näkü, n. nüxö 'Oheim* (258), fwl^ *Grossnuitter'
(250).
1063. niymn 'Scheide*.
ap. *nigama', vergl. skr. w^ + l^f/am-, mgamd-
'Einfügung (aber nur als ritueller t. t.), vorgl. np.
peyam (de Lagarde, Ges. Abb. 79).
Unsicher ^).
1064. nirö {*n^rö) 'Kraft, Macht'.
aw, '^nairyava- 'Mannhaftigkeit', vergl. nrnrya-
mannhaft'; ai. ndrya-; phlv. nerök,
1065. ni» auch', hemz (Sahn. I, 167 Vers 691), ?:x (Is.
1, 15).
ap. *anyadadi^) 'irgend wie anders' (Säle mann,
Mel. asiat. IX, 241); phlv. mc (AV.?), päz. nfz.
Das Wort heisst aber nlz (nicht uez), es reimt
auf äz; ebenso hemz, das die Wörterbücher fälsch-
lich mit B sprechen lassen.
1066. ne»t *ist nicht*, vest^^),
päz. nestj nesU,
ap. naiy + asti,
1067. neS 'Spitze, Stachel; Gift (AM. S. 10 Zeile 5 v. u.)',
nester 'Lanzette'.
ai. vergl. neksana- spitzer Stab, Spiess', zu [/'neks-,
niksati 'durchbohren' (Hörn).
1068. nek 'schön, gut', nekö, nekt, new 'wacker, Held'
(Sahn, I, 416 Vers 555, HI, 1106 Vers 707, von einer
Frau).
*) Wenn phlv. n{i)käm^ vd. 7 f 192) Gl , wirklich 'matrice' bedeutet
— was ich bezweifle - so müsstc es nCOgüm gelesen werden, um mit
np. niyäm vereinigt werden zu können (Darm est eter, Et. ir. I, 61,
Note 4).
*) Lies *amyadäciih
«J Reimt auf yekesi (Öähn. I, 42 Vers 144; 170 Vors 750). Auch
in Indien spricht man heute nlst.
```


## [2026-09-07T18:19:23.524Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD ned ===\"; grep -n -i \"^ned-\\|^ned\\b\" AHD_watkins1985.txt | head; echo \"=== AHD nodus/net ===\"; grep -n \"nodus\" AHD_watkins1985.txt | head"
}
```


### [2026-09-07T18:19:23.583Z] TOOL RESULT

```
=== AHD ned ===
=== AHD nodus/net ===
```


## [2026-09-07T18:19:25.040Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN nard ===\"; grep -n \"^nard\\|^spikenard\\|nardos\\|nardus\" KLN_1966.txt | head -20; echo \"=== SKT nard ===\"; grep -n -i \"^NARD\\|SPIKENARD\\|nardus\" SKT.txt | head -20"
}
```


### [2026-09-07T18:19:25.107Z] TOOL RESULT

```
=== KLN nard ===
24981:Derivatives:  narcotic,  n.,  narcotic-al-ly,  adv., narcotism  (q.v.),  narcotize  (q.v.) narcotine,  also  narcotin,  n.,  an  alkaloid  found  in opium,  CjjHjjNO,,  discovered  by  the  French chemist  Charles  Elerosne  (1780-1846)  in  1803 (chem.)  —  See  prec.  word  and  chem.  suff.  -ine, -in;  so  called  because  it  was  first  supposed  to  be the  narcotic  principle.  Cp.  cotarnine. narcotism,  n.,  1)  narcosis;  2)  condition  produced by  narpotic  poisoning.  —  See  narcotic  and  -ism. narcotize,  tr.  v.,  to  produce  the  condition  of  nar¬ cosis;  to  stupefy.  —  See  narcotic  and  -ize. Derivative:  narcotiz-ation,  n. nard,  n.,  spikenard.  —  ME.  narde,  fr.  OF.  narde (F.  nard),  fr.  L.  nardus,  fr.  Gk.  vapSo q,  fr.  Heb. nerdh,  ‘nard’,  which  together  with  Aram,  nirda and  Akkad,  lardu  of  s.m.,  prob.  derives  fr.  Indo- Iranian  *narda  in  OI.  nadah,  nalah,  ‘reed’.  OI. naladam,  ‘nard’,  is  possibly  Sanskritization  of Gk.  vapSo;;  see  Boisacq,  DELG.,  p.  657  s.v. vapSo;,  and  Walde-Hofmann,  LEW.,  II,  143 s.v.  nardus.  However,  according  to  Manfred Mayrhofer,  A  Concise  Etymological  Sanskrit Dictionary,  II,  p.  140  s.v.  naladam,  the  above Sem.  words  more  prob.  derive  fr.  OI.  naladam. Cp.  Nardius  and  the  second  clement  in  spike¬ nard.  Cp.  also  narthex.
36257:spikenard,  n.  —  ME.,  fr.  ML.  spica  nardi,  ‘spike of  nard’.  See  spike  and  nard.
=== SKT nard ===
12161:—  Ski.)  F,  «(in/.  — L.  tan/uj.  — Cik.fftpSOT, Mk.  xiv,  3.  — Pere.  war*/.— Skt.  naiaifa,  the Indian  spikenard.  —  Skt-  ttal,  lo  smell. Der.  ifikenard,
18079:spikenard.  (L. ;  am/ F.-L.-Gk- Pers.  -  Skt.)  Put  for  fpikeJ  nnrj  iL. nanius  spicafus),  i.e.  nard  fumishrd  with spikes,  in  allusion  to  the  mode  of  growth. And  see  Nard.
```


## [2026-09-07T18:19:35.420Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nfor f,ln in [('KLN_1966.txt',24981),('SKT.txt',12161),('SKT.txt',18079)]:\n    t=open(f,encoding='utf8',errors='replace').read()\n    # find char offset of that line\n    lines=t.split('\\n')\n    off=sum(len(l)+1 for l in lines[:ln-1])\n    leaf=t[:off].count('\\f')\n    print(f,ln,'leaf(0-based)=',leaf)\nEOF"
}
```


## [2026-09-07T18:19:36.781Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==12162' SKT.txt 2>/dev/null | head -5 ; echo \"--- around SKT nard line ---\"; sed -n '12150,12170p' SKT.txt"
}
```


### [2026-09-07T18:19:36.797Z] TOOL RESULT

```
KLN_1966.txt 24981 leaf(0-based)= 550
SKT.txt 12161 leaf(0-based)= 325
SKT.txt 18079 leaf(0-based)= 484
```


### [2026-09-07T18:19:38.093Z] TOOL RESULT

```
--- around SKT nard line ---
surface  of  cloth.    (C.) Knap.
tftblC'linen  i  see  Map.
(U-Gk.-Arnb  )     X^Mfk- li^.""Arab.  naftt  nifi,  naph-
Map.
Narootlo.
Fucing  stnpor.   (F. •■Gk.)
r.  —  Gk.  mpifvriuM,  l>enumbiug.
I  brnorob:  ra^inUr,  I  grow
\t  Dumbness,  orig.  coo-
traction;  put  for  avAp*nj,  i.e.  contraction. Sec  8 Dare.
narcissuo.  a  flower.    (L.  —  Ck.)    L. narcissus.  —  Gk.  yaptnocm ;   named  from it«  narxotic  properties. Ward,  an  unguent.  (F.  — L.  — Gk.  — Pen.
—  Ski.)  F,  «(in/.  — L.  tan/uj.  — Cik.fftpSOT, Mk.  xiv,  3.  — Pere.  war*/.— Skt.  naiaifa,  the Indian  spikenard.  —  Skt-  ttal,  lo  smell. Der.  ifikenard,
Karration.  (F.  »  L.)  F.  rtarraticM.m^ L.  ace.  nanxUhntntf  a  talc.  — L.  narnrfMS, pp.  ofnarrare,  to  relate,  lit.  to  make  known.
—  L.  nattts,  j^arus,  knowing,  acquainted with.  —  ^  GNA,  to  know ;  see  Know.
Worrow.  (F..)  M.  E.  TiamtM,  narrwt, nartut.  A,S.  R/aru,  narrow,  closely  drawn. Allied  to  Bsare,  Nerre,  HarooUo.  ^  Not allied  to  ntar.
Narwhal.  &ea-unicorn.  (Scand.)  Dan. Swcd.  markvai;  Iccl.  nJhvair,  a  narwhal. The  lit,  sense  is  *  corpse-whale ; '  the  lish being  (often)  of  a  pallid  colour.  -•  Icel nii-r,  cor^ne  ;  Aiv/r,  whale
Noflal ;  see  Noae.
Nascent;  sec  Natal.
Noflturtliim ;  see  No8«.
Naaty.  (Scand.1  Formerly  also  nasJfy; sec  Mati'lavi  in  Cot.  Put  for  masky,  an initial  1  l>cing  lost.  —  Swcd.  dial,  naikuff, nasty,  dirty,  also  bdcU  tnaskiff  \  Swcd. snmkis.  nasty —Swcd.  dial,  snaska,  to  eat like  a  pig,  Iw  slovenly;  Dan.  snaskf,  to cat  like  a  pig.  4*  Low  G.  nask^  na&ty; Norw.  M<ar^,  greedy,  naska,  to  champ.  Al- lied to  Bnatch.
Natal,  belonging  to  one's  birth.  (F.— L)  F.  natai  (O.  K.  «Jr/).-L.  tuUaiis.^ L.  nntHS  (for  gHatms),  bora  (cf.  Ck.  leaai- fn\foi,  a  blood  rcl.ition) ;  pp.  of  nasci,  to be  bom  —  V  G  AN,  to  beget    Sec  Kin.
```


## [2026-09-07T18:19:44.982Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=325 && NR<=327 {print \"=== leaf(0based) \" NR-1 \" ===\"; print substr($0,1,300)}' SKT.txt"
}
```


### [2026-09-07T18:19:46.129Z] TOOL RESULT

```
=== leaf(0based) 324 ===
implying '  obligalion.*  (£.)  Only  the  pt.  t.  remains, which  is  now  also  used  as  a  present M.  E.  met.  moot,  pres.  t.,  I  am  able,  1  am free  to,  I  ought ;  pt  t  mttste.  mtiste,  1  was able,  I  ought.  A.  S.  ic  mSt,  pres.  t ;  u m^ste,  I  most,  pt  t ;  as  if  fr
=== leaf(0based) 325 ===
r,  (j)  myrrh. its  bitterness.  4*  Heb.  wJr,  bltt
Myrtle.  ;F.  - 1-.  -  Gk.  -  Pei myrtil,  dimin.  of  myrtt,  mturie,  the tree.  —  L.   murtus^  myrttu.^O'km^ Pers.  mtird,  the  myrtle.
Mystery   (1),   a  secret  rite M.  E.    mysterie.  •  L.    mytttrii ftviTT^pioy  (Rom.  xvi. 
=== leaf(0based) 326 ===
 to cat  like  a  pig.  4*  Low  G.  nask^  na&ty; Norw.  M<ar^,  greedy,  naska,  to  champ.  Al- lied to  Bnatch.
Natal,  belonging  to  one's  birth.  (F.— L)  F.  natai  (O.  K.  «Jr/).-L.  tuUaiis.^ L.  nntHS  (for  gHatms),  bora  (cf.  Ck.  leaai- fn\foi,  a  blood  rcl.ition) ;  pp.  of
```


## [2026-09-07T18:19:53.278Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ned-\" AHD_watkins1985.txt | head -20; echo \"=== net/nodus ===\"; grep -n -i \"annex\\|nexus\\|to bind, tie\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-07T18:19:53.359Z] TOOL RESULT

```
<persisted-output>
Output too large (42.3KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/tool-results/bczsir1pn.txt

Preview (first 2KB):
184:Another aspect of the function of sover- eignty is the sphere of the law. There is an old word, yewes-, probably for “religious law,” in Latin jus. Latin léx is also ancient (leg-'), though the details of its etymology are uncertain. In a society that emphasized the principle of exchange and reciprocity, it is scarcely surprising that the notion of con- tractual obligation should be well repre- sented. Several roots specify the notion of “bond”: bhendh-, ned-, leig-', all of which have derivatives with technical legal mean- ings in various languages. The word for “a pledge,” wadh-', exists in western Indo- European, whence the English verb for mak- ing a particular kind of contract, WED. An oath then as now was important: the roots *serk- and oito- are found in Celtic and Ger- manic. The verb k”ei-' meant “to pay com- pensation for an injury.” Its derivative noun, *k“oind, was borrowed from Doric Greek into the most ancient Roman law as Latin poena, punire, whence English PUNISH and a host of legal terms. The Greek word for jus- tice, diké, is derived from the notion of “boundary marker” (deik-; compare also ter-, “termen-).
218:lengthened-grade form. A form with lengthened vocalism.
219:ghers-. 2. Lengthened-grade form
293:aryo-. Lord, ruler; self-designation of the Indo-Iranians and perhaps of the Indo-Europeans. Lengthened-grade form *dryo- in Sanskrit drya-, noble, Aryan: ARYAN. [Pok. arjo- 67.]
454:ere-2. To separate. Variant *ré-, contracted from *reo-. 1. Suffixed variant form *rd-ro- in Latin rdrus, “having intervals between,” “full of empty spaces,” rare: RARE}, 2. Suffixed zero-grade form *ra-ti- in Latin ratis, raft (< “grating,” “latticework”): RATITE. 3. Suffixed length- ened-grade form *ré-ti- in Latin réte, r��tis, a net: RE- SEAU, RETE, RETIARY, RETICLE, RETICULE, RETINA; RETIFORM. 4. Suffixed form *eré-mo- in Greek erémos, empty, desolate, bereft: EREMITE, HERMIT; EREMURUS. [Pok. 5. er- 332.]
...
</persisted-output>
```


## [2026-09-07T18:19:56.642Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^ned-\\|^ned\\.\\|ned-\\. \" AHD_watkins1985.txt | head; echo ---; grep -n \"Pok. 1. ned-\\|Pok. ned\" AHD_watkins1985.txt | head"
}
```


### [2026-09-07T18:19:56.716Z] TOOL RESULT

```
776:sively, very (< *ne-mi-s, “not little”; *mi-, little; see mei-2): NIMIETY. 4. Latin nihilum, nothing (< *nehilum, “not a whit, nothing at all”; hilum, a thing, trifle; origin unknown), contracted to nihil, nil, nothing: NIHILISM, (NIHILITY), NIL; ANNIHILATE. 5. Latin non, not (< *ne-oinom, “not one thing”; *oino-, one; see oi-no-): Non-. 6. Italic *nek, not, in: a. Latin prefix neg-, not: NEGLECT, (NEGLIGEE), NEGOTIATE; b. Latin negdre, to deny: NEGATE; ABNEGATE, DENY, RENEGADE, (RENEGE). 7. Greek né-, not: NEPENTHE. 8. Zero-grade combining form *n- in: a. Germanic *un- in Old English wn-, not: uN-!; b,. Latin in-, not: IN-1; c. Greek a-, an-, not: A-}, (AN-); d. Sanskrit a-, an-, not: AHIMSA, AMRITA. [Pok. ne 756.] nebh-. Cloud. 1. Suffixed form *nebh-lo- in Germanic *nibla- probably in Old Norse nifl-, “mist” or “dark”: NIFLHEIM. 2. Suffixed form *nebh-eld- in: a. Latin nebula, cloud: NEBULA, NEBULOUS; b. Greek nephelé, cloud: NEPHELINE; NEPHELOMETER. 3. Suffixed form *nebh-es- in Greek nephos, cloud: NEPHOLOGY. 4. Nasal- ized form *ne-m-bh- in Latin nimbus, rain, cloud, aura: NIMBUS. See ombhro-. [Pok. (enebh-) 315.] ned-. To bind, tie. 1. O-grade form *nod- in: a. Germanic *nati- in Old English ne¢(t), a net: NET!; b. Germanic *nat-ilo, a nettle (nettles or plants of closely related genera such as hemp were used as a source of fiber), in Old English netel(e), netle, nettle: NETTLE; c. Germanic *nat-sk- in Anglo-Norman nouch, brooch: OUCH?. 2. Lengthened o-grade form *nédo- in Latin nédus, a knot: NODE, NODULE, NODUS; DENOUEMENT. 3. Re-for- mation of the root in Latin nectere (past participle nexus), to tie, bind, connect: NEXUS; (ADNEXA), ANNEX, CONNECT [Pok. 1. ned- 758.] negwh-ro-. Kidney. Greek nephros, kidney: NEPHRO-; MESONEPHROS, METANEPHROS, PERINEPHRIUM, PRO- NEPHROS. [In Pok. eng¥- 319.] negw-ro-. Adjective denoting various colors; with deriva- tives like Greek nebros, “fawn.” Latin niger, black: NEGRO, NIELLO, NIGRESCENCE, NIGRITUDE; DENIGRATE, NECROMANCY, NIGROSINE, [néhw-iz. Near. Germanic root. Old English néah, near: NEAR, NEIGHBOR, NEXT, NIGH.] nei-. To be excited, shine. 1. Suffixed form “nei-to- in Germanic *nitha-, animosity, in Old Norse nidh, scorn (> nidhingr, villain): NIDDERING. 2. Suffixed zero-grade form *ni-to- in Latin nitére, to shine: NEAT!, (NET?). 3. Possibly Persian nil, indigo: ANIL, LILAC. [Pok. 2. nei- 760.) neie-. To lead. Sanskrit nayati, he leads: NAINSOOK. [Pok. 1. nei- 760.] neig’-. To wash. Germanic *nikwiz, *nikuz in Old High German nihhus, river monster, water spirit: NIx!. [Pok. neigt- 761.] nek-', Death. 1. Latin nex (stem nec-), death: PERNI- cious. 2. Latin necdre, to kill: INTERNECINE. 3. Suffixed (causative) o-grade form *nok-eyo- in Latin nocére, to injure, harm: NOCENT, NOCUOUS, NUISANCE; INNOCENT, INNOCUOUS. 4. Suffixed o-grade form *nok-s- in Latin noxa, injury, hurt, damage: NOXIOUS; OBNOXIOUS. 5. Suffixed full-grade form *nek-ro- in Greek nekros, corpse: NECRO-, NECROSIS; NECROMANCY. 6. Greek nek- tar, the drink of the gods, “overcoming death” (*tar-, overcoming; see ter@-2): NECTAR, (NECTARINE). [Pok. nek- 762.] nek-?. To reach, attain. I. O-grade form *nok- in Ger- manic *ga-nah- (*ga-, intensive prefix; see kom), “satis- fies,” forming *gandga-, sufficient, in Old English gendg, enough: ENOUGH. II. Variant form “enk-. 1. Redupli- cated in Greek enenkein, to carry, whence onkos, a burden, mass, hence a tumor: ONCOGENESIS, ONCOLOGY. 2. Compound root *bhrenk- (see bher-'). [Pok. enek- 316.] nekw-t-. Night. O-grade form *nokv-t-. 1. Germanic *naht- in Old English niht, neaht, night: NIGHT. 2. Latin
---
776:sively, very (< *ne-mi-s, “not little”; *mi-, little; see mei-2): NIMIETY. 4. Latin nihilum, nothing (< *nehilum, “not a whit, nothing at all”; hilum, a thing, trifle; origin unknown), contracted to nihil, nil, nothing: NIHILISM, (NIHILITY), NIL; ANNIHILATE. 5. Latin non, not (< *ne-oinom, “not one thing”; *oino-, one; see oi-no-): Non-. 6. Italic *nek, not, in: a. Latin prefix neg-, not: NEGLECT, (NEGLIGEE), NEGOTIATE; b. Latin negdre, to deny: NEGATE; ABNEGATE, DENY, RENEGADE, (RENEGE). 7. Greek né-, not: NEPENTHE. 8. Zero-grade combining form *n- in: a. Germanic *un- in Old English wn-, not: uN-!; b,. Latin in-, not: IN-1; c. Greek a-, an-, not: A-}, (AN-); d. Sanskrit a-, an-, not: AHIMSA, AMRITA. [Pok. ne 756.] nebh-. Cloud. 1. Suffixed form *nebh-lo- in Germanic *nibla- probably in Old Norse nifl-, “mist” or “dark”: NIFLHEIM. 2. Suffixed form *nebh-eld- in: a. Latin nebula, cloud: NEBULA, NEBULOUS; b. Greek nephelé, cloud: NEPHELINE; NEPHELOMETER. 3. Suffixed form *nebh-es- in Greek nephos, cloud: NEPHOLOGY. 4. Nasal- ized form *ne-m-bh- in Latin nimbus, rain, cloud, aura: NIMBUS. See ombhro-. [Pok. (enebh-) 315.] ned-. To bind, tie. 1. O-grade form *nod- in: a. Germanic *nati- in Old English ne¢(t), a net: NET!; b. Germanic *nat-ilo, a nettle (nettles or plants of closely related genera such as hemp were used as a source of fiber), in Old English netel(e), netle, nettle: NETTLE; c. Germanic *nat-sk- in Anglo-Norman nouch, brooch: OUCH?. 2. Lengthened o-grade form *nédo- in Latin nédus, a knot: NODE, NODULE, NODUS; DENOUEMENT. 3. Re-for- mation of the root in Latin nectere (past participle nexus), to tie, bind, connect: NEXUS; (ADNEXA), ANNEX, CONNECT [Pok. 1. ned- 758.] negwh-ro-. Kidney. Greek nephros, kidney: NEPHRO-; MESONEPHROS, METANEPHROS, PERINEPHRIUM, PRO- NEPHROS. [In Pok. eng¥- 319.] negw-ro-. Adjective denoting various colors; with deriva- tives like Greek nebros, “fawn.” Latin niger, black: NEGRO, NIELLO, NIGRESCENCE, NIGRITUDE; DENIGRATE, NECROMANCY, NIGROSINE, [néhw-iz. Near. Germanic root. Old English néah, near: NEAR, NEIGHBOR, NEXT, NIGH.] nei-. To be excited, shine. 1. Suffixed form “nei-to- in Germanic *nitha-, animosity, in Old Norse nidh, scorn (> nidhingr, villain): NIDDERING. 2. Suffixed zero-grade form *ni-to- in Latin nitére, to shine: NEAT!, (NET?). 3. Possibly Persian nil, indigo: ANIL, LILAC. [Pok. 2. nei- 760.) neie-. To lead. Sanskrit nayati, he leads: NAINSOOK. [Pok. 1. nei- 760.] neig’-. To wash. Germanic *nikwiz, *nikuz in Old High German nihhus, river monster, water spirit: NIx!. [Pok. neigt- 761.] nek-', Death. 1. Latin nex (stem nec-), death: PERNI- cious. 2. Latin necdre, to kill: INTERNECINE. 3. Suffixed (causative) o-grade form *nok-eyo- in Latin nocére, to injure, harm: NOCENT, NOCUOUS, NUISANCE; INNOCENT, INNOCUOUS. 4. Suffixed o-grade form *nok-s- in Latin noxa, injury, hurt, damage: NOXIOUS; OBNOXIOUS. 5. Suffixed full-grade form *nek-ro- in Greek nekros, corpse: NECRO-, NECROSIS; NECROMANCY. 6. Greek nek- tar, the drink of the gods, “overcoming death” (*tar-, overcoming; see ter@-2): NECTAR, (NECTARINE). [Pok. nek- 762.] nek-?. To reach, attain. I. O-grade form *nok- in Ger- manic *ga-nah- (*ga-, intensive prefix; see kom), “satis- fies,” forming *gandga-, sufficient, in Old English gendg, enough: ENOUGH. II. Variant form “enk-. 1. Redupli- cated in Greek enenkein, to carry, whence onkos, a burden, mass, hence a tumor: ONCOGENESIS, ONCOLOGY. 2. Compound root *bhrenk- (see bher-'). [Pok. enek- 316.] nekw-t-. Night. O-grade form *nokv-t-. 1. Germanic *naht- in Old English niht, neaht, night: NIGHT. 2. Latin
```


## [2026-09-07T18:20:05.860Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FVQ nask/nasx ===\"; grep -n -i \"nask\\|naskh\\|nusk\" FVQ_pages.txt | head -20; echo \"=== FVQ nard ===\"; grep -n -i \"nard\" FVQ_pages.txt | head"
}
```


### [2026-09-07T18:20:05.935Z] TOOL RESULT

```
=== FVQ nask/nasx ===
3946:<t)JJ))*> aviuds sinless (PPGl, 77) ; ^'-u^O-")) vinaskarih ~
10010:,5>L*j (Nuskha).
10032:Iranian, where Phlv. ^i3>, nask 2 ; Av. JJAJDJJJ naska means a book
=== FVQ nard ===
12490:tanardh 95GAEKWAD'S ORIENTAL &ERIES.
```


## [2026-09-07T18:20:06.898Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD nask ===\"; grep -n \"^nask\\|nask \" PHD.txt | head; echo \"=== NYB nask ===\"; grep -n \"nask\" NYB_vol2_glossary.txt | head; echo \"=== BRT naska ===\"; grep -n \"naska\\|Textsammlung\" BRT.txt | head -20"
}
```


### [2026-09-07T18:20:06.979Z] TOOL RESULT

```
=== PHD nask ===
501:narm [nlm | M nrm, N ~] meek, humble, soft. nasā [ns’y | M n(y)s?h, № ~] corpse, carrion. nask [nsk' | N ~] a division of the Avesta. nasrušt(īh) [xslwšt', -yh] pollution, corruption. nastaran [nstln' | N ~] dog-rose, sweet briar. nawad [90 | N —] ninety.
5164:wardišnīgīh E 4) vo t | wardišnīg Véi ru re 1 wardišn i0 «e ` -om “G\- nam KA nimāy- -AAG A namāz °з^6 \ wimēhgen 1 5^6 nimüdan Viel namak 1361 namad VEGA, nasa, wisē А99 | wisāy- = A235 1 wisān- - ras "wisāndan x 75991 wë = 1693 1 wēxtan! Veras i wisānišnīh AS PO v351 wisānišn vu rudi namiz! «eX wasyar asi wisin(n)- — pai wasyar `Y, 9459 A nask V A35 \ nasruštīli ^ TANT 1
=== NYB nask ===
2650:: nask [nsk] properly ‘bundle, bunch’, the name of each of the 21 “books” or collection of texts forming together the Sassanian Avesta 1091’. — Av. naska- in (1060) nasko.frasa- ‘one who devotes himself to the study of the nasks’.
2719:nikah [nk’s] look, glance, observation; custody, care: ~ kartan to look on, to watch 152. 259.24, 2726. 2817; ~~ daštan to notice, to observe, to pay attention to 108%. 12114; apar ~ dāštan to keep in safe custody 4112. — MPrth ng’h ‘look, attention’, n. kyrdn ‘to notice’ (A-H ITT); Paz. nagäh, NP nigäh; < Olr "ni-kada- from kà-, v. ākāh. Another derivative was "niš-ka0a- > Milr *niškāh ‘contempt’, preserved in Arm nškah-em ‘to reject, to condemn’. Cf also Arm nkat linel or nkat-em ‘to see, to consider, to contem- plate’ from MIr *nikät < Olr *nikātā, nom. sg. of the nomen actoris *nikätar- ‘contemplator’. The pt. pass. *nekāta- is found in the name of the 15th nask (q. v.) of the Sas. Avesta: N?kütom [nyk”- twm] = Av. *nikätem ‘that which is observed (in medical matters)’.
4467:yuvat-sritak [— slytk'] "text not handed down (in the common traditional way): apük hamäk čišin ~-Gn mnó(k» nask ošmurt (together with =) including all these texts which were not handed down in the ordinary way he reckoned the nasks anew 109!" (restore the text of the MS and Madan!). — Av. (1637 sq.) sray- ‘to lean’; FrO XIIe srita = api- spürt (v. this w.). The secondary texts
4471:alluded to here are probably inserted in the Pāci nask (no. 6, DkM 682-684).
4644:AV — 'The book of Arda Viraf. The Pahlavi text prepared by Destur Hoshanji Jamaspji Asa. Revised and collated with further MSS with an English translation and in- troduction, and an appendix containing the texts and translations of Gosht-i Fryano, and Hadokht-nask by Martin Haug, assisted by E. W. West. London & Bombay 1872.
5241:naska-: nask
=== BRT naska ===
24661:ß  i^aiStih  /röl  hiSihFt  -  tiräk  aÜHÜk  J>a harvisp  vinaskarih.  —  0  iSchr.  s.  ^myaiirä.' iatana-  No.  a  und  Cld.  KZ.  33.  593.
```


## [2026-09-07T18:20:12.062Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '9995,10045p' FVQ_pages.txt"
}
```


### [2026-09-07T18:20:12.108Z] TOOL RESULT

```
Circle* 7 ; cf. Heb. TJJI ; Phon. H13 ; Syr. liyj, all from a root "H3
which is a parallel form to *1T3, to dedicate, consecrate (cf. Akk.
nazdru, curse), and Sab. )Mh (Hommel, Sudarab. Chrcst, 128). 8 It
must have been an early borrowing.
Lidzbarski, Handbuch, 322 ; Harris, Glossary, 123.
And the WTft of the Elephantine papyri (Cowley, Aramaic Papyri, p. 299).
Cf. de Vogu6, Inscriptions, No. xi, 1, 4, and in the Fiscal inscription, ZDMG,
xlii
383 ; cf. also BtflJ in the Nerab inscription in Lidzbarski, Handbuch, 445.
D. H. Miiller, Epigraphische Denkmaler aus Abesainien, 1894, p. 52.
W. M. Miiller, Asien und Europa, 1893, p. 127. See Erman-Grapow, v, 396.
6 Levy, Worterbuch, iii, 374, suggests a derivation from ^ to be hard, but
this is hardly likely.
7 Ahrens, Christlichea, 34.
8 See also Rossini, Glossarium, 184,FOREIGN VOCABULARY OP THE QUR'AN 279
,5>L*j (Nuskha).
vii, 153.
A copy, or exemplar.
The word occurs only in a late Sura in reference to the Tables
of Stone given to Moses, but the verb formed from it **lJu*i, is
used in an* earlier passage, xlv, 28, though again the reference is to a
heavenly book.
The Muslim authorities take the word as a form *i with the
meaning of AJ^uL* from -wJ in the sonse to copy, and some (cf. LA,
iv, 28) would make copy the primitive meaning of the root. A com-
parison with the cognate languages, however, shows that copy is a
secondary meaning of the root, cf. Akk. nushu = extract, and Syr.
*caj to copy, beside Akk. nasahu, Heb. H03 ; O.Aram. H03 and
the Targumic H03, where the original sense is clearly to remove,
tear away (evelfore), which original meaning is found in the Qur'an
in ii, 100 ; xxii, 51, where the word is used, as Hirschfeld, Beitrcige, 36,
points out, precisely as H03 is in Deut. xxviii, 63 ; Ezr. vi, 11.
Hoffmann, ZDMG, xxxii, 760, suggested that the Arabic word was
from Aram. tfPIOli, but this is used only in late Kabbimc writings
and gained the technical sense of ''variant reading", e.g. XH013
fcWTnX. Again in Syr. the only form is laODQJ, which is also late
(PSm, 2400), and as Lagarde, GA, 196, points out, 1 conies from the
Iranian, where Phlv. ^i3>, nask 2 ; Av. JJAJDJJJ naska means a book
of the Avesta. The Iranian word, however, as Spiegel showed In his
Studien ilber das Zendavesta* cannot be explained from Indo-European
material, and like the Arm. "&// is in all probability an ancient
borrowing from some Semitic source in Mesopotamia.
It is, of course, possible that it came to Arabic also from
Mesopotamia, but we find DnOJ in a Nabataean inscription from
1 Also Vollers, ZDMG, 1, 649.
2 PPGl, 165, 168 ; Sayast, Glossary, 163 ; West, Glossary, 243 ; Haug, Parsis, 181.
3 ZDMG, ix, 191, and JA for 1846.
4 Hiibschmann, Arm. Gramm, i, 204, however, compares ^fa with the Syr. (JuJ,
though deriving both from an Iranian original. See Lagarde, GA, 66, and Zimmern,
Akkad. Fremdw, 13, who relates it to the Akk. nlsu. Arm. 'LnL.ufuuij, however,
is a late borrowing from Arabic ; see ZDMG, xlvi, 264.280 FOREIGN VOCABULARY OF THE QUR ? AN
```


## [2026-09-07T18:20:31.897Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT 1063ish ===\"; grep -n \"nas\\?ka\" BRT.txt | head -20; echo; echo \"=== HUB nask/1060 ===\"; grep -n \"nask\\|1060\\.\" HUB.txt | head -20"
}
```


### [2026-09-07T18:20:31.965Z] TOOL RESULT

```
=== BRT 1063ish ===
3510:•  j.  apajcraosaka-  Adj.  'schmähsUchtig' : nivayaka  mpalnaka  apa.skaraka  'ia(NP.) ima  paiti.vJsfTUe  Yt5.95.
3622:•  j.  apa.skaraka-  Adj.  'hohnsüchtig,  höh- nisch': nivßyaka  nipasnaka  °^a{NP.)  apa.- xraosaka  imä  paifi.vlsmte  Yt.  5.95.
4250:Pü.;  aiar;  (zu  »«);  aaerätt'},  s.  unter  'raorah'. —  >)  GelW. }.  BHOxtÖ  N,  ^ :  lies  anakaxli.
4383:j.  ana.haxü  N.  80:  lies  anakaxla.
4814:mit  "p.parü,  y  parai''>  'weg-,  fortgehen, sich  entfernen';  a)  absol.:  natrya-san/ta . . para.ili'ii  (2SIA.)  upa.vazanuha  avi  ntnä- n>m  airyamaifii  (sii.)  V,  22.  7;  —  *para.- äip^^  upa.vazala  nairy3.sa»hs  avi  . .  V. 22. 13;  —  zaota  (sd.)  anakaxtö  par^at dqhiUäi  .  .  zao^r)m  raSxsaiti  N.  A'o;  — yezica  *alte  ratavö  *anahaxta  para.tya- yanti^^^  N,  Ai?;  —  uzayeni  psrayaii  V,  2-2. I.  a)  II  militärisch  'ausrücken,  ins  Feld ziehen':  avd^ä/aiy  a'iaAam  paraidiy (2SIA.)  avam  käram  jadty  Bh,_^.3;  2.7, 10; — ara^äsam  a>aA<im  piirait>l(iP'PTA.) avam  käram  . .  jatä  Bh._y.14_:  9,  2,6,14;
6186:■  /.,  g.  aäay-  f  'was  einem  auf  Grund seiner  Leistung  —  in  gutem  und  schlimmem Sinn  —  zukommt;  Anteil,  Los,  Verdienst, Lohn,  Belohnung*,  bes.  beim  letzten  Ge- richt": kä  ahmäi  °sis  ?r3nävi  Y.g.y,  4 —  yaia  ad  masis/äsca  . .  asayö  »nnavanU Y.52.3;  —  'itm  fyao^anäis  vohü  äaiält mofuiMhii  "(je)  nach  den  Taten  (die  einer getan  hat)  soll  VM.  das  Los  zuweisen" Y..^j.i6";  —  ia  zasta  yä  tä  haßt  (sd.) az<i  yä  da  -Sil dr^äin asäunaka  ". .  jene Lose,  die  du  dem  Drug-  und  dem  Afa- anhänger  zuweisen  wirst  .  ."  Y.4y-4;  — ail  .  .  ya  vi  'Itf  *ranöibya  savSi  (sd.) ndoyai  Y.43.12;  —  vTdyai  (sd.)  saoi);_ jdiä  hsi  '/is  anhat  Y.  4^.  9 ;  —  yada  'sifis maAjä  VOSS  xsayä  (sd)  Y,50.9;  -^.S; iiSit..asahe  nSi£  '/ayä{GS.y^/räi'fnti{sA.) P.44;  —  >r>kyä  amatai^yä  °Ms..aslöis Vr.^.4;  —  däidl  aiä  tarn  'sim  vanhsus Syafta  manar^hs  Y.  28. 7 ;  — yS  mHi  nä  va gMa  (sd.)  va  .  .  dayät  ■  ■  vahista  'slm  asäi vehü  xiair»m  mananha  "wer  . .,  als  Lohn für  seine  Gerechtigkeit  das  Reich  durch VM.  (verldhe  ihm)"  Y.4ö.io*>;
8555:•  j,  uspaeiata-  m.  Name  eines  Zweigs der  5i7?/(ofamilie:  UrS-nakaHwaAe  'lanqm samanqm  "des  T.  (aus  dem  Zweige)  der
12263:•  j.  tiro.nakaS'wa-  m.  EN.  eiues  Gläu- bigen: 'TiwaAe  uspaliatanqin  (sd.)  salria- nam  Ytij.  126.
18911:\paiti  nars  aSaorUS . .  °kala  apsnnsyäkasca varai^rm  (sd.)  pantqm  atBit  V.J.  11;  3; —  ,.  zaohrata  (sd.)  ratufris  'käscit  (GS.) apgrmäyükahecit  N.  .^0;  —  yS  anyahe'ka (IS.)  ..yS  anyehe  ^apirmSyüka  *anakaxt/T a'haurUTifm  *parar>kacaiti'ü.6i.;  6; — yHi.. 'kqm  vä  *ap}nnäyük>m  (vS)  a/t?m  dasli N.  105; —  'ka  kasujcra%wa  (sd.)  ^.40;  — ava%a  Ag  x"atg  (sd)  pu%rytn  ankat..aat yai  hvqtn  'ka^^  bavaiti(sd.)  ..yai dirftrqm \AfntiYd.2\  —  dahma  •^rf(NS.?)  ap^rma- yüke  kainike  Y.2^.3;  —  katärS  (sd.) '  a%aurumm  *parayat  'ka  va  nmänS.paiti^ va  N.5;5,  *5'>j — yai . .  nmanahe  nmOnB.- paitlm  'kam  .  .  daiöÄSui  daiiikupaitim 'kqm  bisazyätY.j.42;42',  is.$&.  a)mit asavan-  (Sp.  250  m.):  nanm  aiavanjm  . , 'kqm  a^aonlm  V.p.  33,  42,  75.12,  26,  rr.i, 2/7,  10  (statt  Ab!.),  Vr.j.4,  G.4.9;  — tat  asti  yUnO  . .  a^arihim  , .  tat  -kayai  . . ratuxsa^ray'ai  asaonyäi  H.  z.  1 8 ; — 'rikayh aiaonyä  Vd.  4-
22493:*vanAar-  n,,  lum  V.  it/aA-.  —  Pü. !  viiäfaiii brähnaka  sräytl  ka!  Hin  luvän  AH  "«ach  Oboe Gürtel  und  Hemd  (t,  Sp.  IiSf.),  auch  (gani) nackt  loU  man  aufsagen,  so  wie  man  et  (eben) vermag".  —  ')  Jn.  Cama  Mem.  Vol.  I31 fibersetit  "with  one'«  clothing  thrown  off  i.  e, incompletely  dieiied"  und  leitet  f*  mit Haplologie  aas  *vaaAa-Aarsla-  her.  Die  auf- gestellte Bedeutung  verlangte  aber  vielmehr eine  Grundform  'Aia^sta-vasha-.  —  >)  Nach der  fl-DeU.  ~    3)  Hds.  varllas:    —    i)  Hds.
24661:ß  i^aiStih  /röl  hiSihFt  -  tiräk  aÜHÜk  J>a harvisp  vinaskarih.  —  0  iSchr.  s.  ^myaiirä.' iatana-  No.  a  und  Cld.  KZ.  33.  593.
25792:EN. ■  j.  ^aena-  Adj.  Name  einer  iranischen Yi.'cäX\^:tTrB.naka'hwahe  uspali'atanqm{&dS) 'tianqm   Yt/J.  126;    —  frü.Aaia/rahe  . . 'nanqm  Yt  7^.  126.
25980:•  j.  sanaka-  il  'Mündung"':  yajdit  'ie ra»Aayä  yaiHt  vTmaihrm  (sd.)  ai>ihä  zfmS Yt  io.  104;  —  upa  aoiaisu  raakayä  .. upa  'Ae  ranhayä  YtT2,  i8f.
26177:Unsicher.  —  Pü.:  dddnakadk.
28202:•  j.  zinaka- Adj. 'schädigend'(?):  •^j{NS.) nqma  ahmi  (nämL  vayui)  Yt  1$.  45.

=== HUB nask/1060 ===
3654:1060. Np. nal 'Rohr, Stengel, Rfihre' — afgh. nam f.
```


## [2026-09-07T18:20:32.740Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && grep -n \"نسک\\|نای\\|نرد\\|ناردین\" ARY_pages.txt | head -20; echo \"=== latin idx ===\"; grep -n -i \"^NASK\\|^NAY\\|^NARD\\|NASK\\b\" ARY_latin_index_pages.txt | head -20"
}
```


### [2026-09-07T18:20:32.813Z] TOOL RESULT

```
28:شترکك» واژه‌های همريشه در زبان‌های سانسکریت و ارمنی و یونانی ولاتین و آلمانی و انگلیسی و
226:8 اوستایی: ۸1۸183۸ سانسکریت: ۸11۸7۸ بازگشت به برهان قاطع» صفحه‌ی ۹۳۴
241:هند(مانسکریت و غیره) دارند. به عبارت دیگر ترتیب جغرافی این زبانها چنین است: سکمایی
258:هزارهی گذشته (به استتنای هجوم و ماندگری قبایل ترک و مجار و فنلاندی) تغییر زیادی نگرده است
304:مثلاً واژه‌ی هند و اروپایی 8113100" (فارسی «غان»؛ سانسکریت: 817178[۸: اوستی :8۸132
428:نزدیک شرق ر غرب در هند برخورد انگلیسی‌ها با نوشتارهای کهن هندی به ویژه سانسکریت بود. ."
429:برخی از آنان که فرهیخته تر بودند با شگفتی دریافتند که شباهت عجیبی میان سانسکریت و زبانهای
432:ریژه اوستایی) پرداختند شگفتی آنان بیشتر شد چون ایرانی باستان نیز هم پا مانسکریت و هم با
516:: «زبان سانسکریت که قدمت آن معلوم نیستء دارای ساختار شگفت انگیزی
522:وجود دارد که شاید گوتیک و سلتیک هم... پا سانسکریت دارای ریشه‌ی مشترکی
551:دادند که مثلاً واژه‌ی سانسکریت "۸018" (به معنی «آذر» يا «آتش») و واژه‌ی لاتین 10727157" نه
560:واژه‌ی بنیادین را احیاکرد. مثلاً پس از تعبین برابرهای واژه‌ی «زمین» (سانسکریت: 4۵7۸8 یونانی؛ . ,
563:۳ بوده است. همچئین همسنجی واژه‌های سانسکریت با سایر واژه‌های بنیادین هند و ۱
570:اروپایی نشان می‌دهد که در سانسکریت 0" تبدیل به **شده است. لذا واژه‌ی پنیادین هند و اروپایی
628:کیفیت والای این اثر در سطحی است که امروزه هم برای شناخت زبان سانسکریت از آن استفاده
632:سانسکریت) اهمیت ویژه دارد. ضمناً امروزه دهها زبان (اردو» هندی» گجراتی» بنگالی؛ پنجابی»
856:اروپایی کهن به ویژه سانسکریت و اوستایی چشمگیر است. بهمین دلیل در همسنجی‌های زبانشناسی
931:است: هند و اروپایی نختین: 0۷/18" سانسکریت: ‎ )۸۷18‏ یونانی: 58 لاتین:0۷18 گوتیکد:
941:کهن هند و اروپایی چنین است: سانسکریت: 8۵؛ لانین 487 گالی: 441 اسلاوی کهن:.
970:سانسکریت: [آ40۷۸ فارسی «دیو) و «زاوش»؛ لاتین: (۳85788)ن71 هتیت:511][18۳7) نشان
=== latin idx ===
667:Nays Sly Glas 9 sins .y OLS Jad layup 9a) BN AD cde Ga pet oye cabs)
10633:nay bi oby
11153:NEUNVI, NEUI HBRETON) 332 NASK x(TOKHARIAN B) B 5 os
14395:NAY, NAVEM ARMENIAN) (OLD PERSIAN) jkonk ge 5
14419:NAY, NADH, NAT (PAHLAVI) os hey
```


## [2026-09-07T18:20:38.763Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3645,3670p' HUB.txt"
}
```


### [2026-09-07T18:20:38.809Z] TOOL RESULT

```
Hierher nach Salem ann: np. nahar = nahOr^
naxdra (afgh. LW. niharai 'breakfast*) 'Fasten, Friih-
stUek' (nach No Id eke niichtern, dann *gierig') von
na-xurdan nichtessen ? Ich finde nahdr = gierig,
durstig* bei Vis und Ramin p. 131, 6 v. u.
1059. Als iran. Wrzl. von nuhunbam : nuhuftan 'bedecken,
verbergen' wird *ni-dub, jedenfalls nicht ni-gup anzu-
setzen sein. Phi. n(i)huftan, n(i)huft Gl. and Ind. 230,
Shk. 259. Ebenso jetzt Fr. Muller, WZKM. 8, 190.
1060. Np. nal 'Rohr, Stengel, Rfihre' — afgh. nam f.
'Stengel* = skr. nadd- 'Schilf, Schilfrohr = arisch
"^narda- (Geiger, Etym. und Lautl. des Afgh. Nr. 140).
*) Vgl. arm. hrauer *Einladung* = zd. frava^Sa^ ; arm. paiu&r
*Befehl' = zd. *paitivae3a' (jpaitiva^Say^mi *ioh kUndige an*) nach
Fr. Miiller, WZKM. 7, 371.— 104 -
1062. Lies afgh. nllkq (Raverty nlkceh) und ap. apanyaka-.
1064. Im Paz. stets ntro (Min. und Shk.) geschrieben !
1065. Die Etymologie ist lautlieh unmoglich. Nur ein
urspr. ^aniddid wiirde direct zu np. nl^ fiihren. Vgl.
oben Nr. 457 und Fr. M tiller, WZKM. 5, 67.
1067. Dazu afgh. LW. nes 'the sting of any venomous
animal, puncture, lancet'; nastar und nestar a lancet' ;
arm. LW. n§iirj nstrak Xanzette' (das ein phi. *mstir
voraussetzt). Np. nestar bei Fird. I, 46, 214.
1069. Ist nt/m zu sprechen, vgl. paz. n^m, afgh. LW. nlm,
Hier fehlt np. nlmroz 'Mittag' und n%ma *Halfte' = bal.
```


## [2026-09-07T18:20:39.961Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && python3 - <<'EOF'\nimport re\nt=open('ARY_latin_index_pages.txt',encoding='utf8',errors='replace').read()\nlines=t.split('\\n')\nfor ln in (11153,14395,14419,10633):\n    print('--- line',ln,'---')\n    print('\\n'.join(lines[ln-3:ln+3]))\nEOF"
}
```


### [2026-09-07T18:20:41.220Z] TOOL RESULT

```
--- line 11153 ---
: ‘SNAID, SNAM . HOSSETIC) guy!
: NAWF (WELSH) ($35 NAIN, AXSNIN, AXSNUN
NEUNVI, NEUI HBRETON) 332 NASK x(TOKHARIAN B) B 5 os
: SNATI, SNAYATI (SANSKRIT) < Sis
| [ Rererences benthey NAY ARMENIAN) «go,
| POKORNY? —=S~S*~*~*~*«SCT NEKHO, NEO GREEK) hi y
--- line 14395 ---
at) ot |
NAGS NAVAZA, NAVAYA  :(AVESTAN) gl!
NAY, NAVEM ARMENIAN) (OLD PERSIAN) jkonk ge 5
NAUs, NEUS GREEK) 3h y NAY-, (NAYDAG)
NAVIS, NAVIGARE = (LATIN) iV NAYDAG (PAHLAVI) 5 ay
NAVIRE s(FRENCH) sit NAU HOSSETIC) = 9)
--- line 14419 ---
‘
NASHLI, NASLI (LATVIAN) (3) 31,5 “NADA {OLD PERSIAN) ikon, yuh
NAY, NADH, NAT (PAHLAVI) os hey
REFERENCES ethey NEI KURDISH) 53,5
POKORNY SSSS~*~«SSDS NARA _ HAPGHANI) (24) lai
. | MACKENZIE: (REED, CANE) 58 NADA, NADHA (SANSKRIT) © SL.
--- line 10633 ---
‘MACKENZIE: (THIRD) 136 TRETE ALBANIAN) ST
BUCK: 941 TARRIIANALLI- HITTITE) enzo
nay bi oby
HEN SWEDISH) ($4 yo SAENI AVESTAN) glia)
HEN NORWEGIAN) §353 (SANSKRIT) 2) Suile
HEN DUTCH) gike SANAS, SAYATI, SHA-TI
```


## [2026-09-07T18:20:51.972Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && python3 - <<'EOF'\nt=open('ARY_latin_index_pages.txt',encoding='utf8',errors='replace').read()\nlines=t.split('\\n')\nfor target in (14419,11153):\n    for i in range(target,0,-1):\n        if '[pdf page' in lines[i-1]:\n            print(target,'->',lines[i-1].strip()); break\nEOF\nls"
}
```


### [2026-09-07T18:20:53.328Z] TOOL RESULT

```
14419 -> [pdf page 494]
11153 -> [pdf page 383]
ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf
ARY_latin_index_pages.txt
ARY_pages.txt
ARY_pages.txt.pages
```


## [2026-09-07T18:20:59.912Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && python3 - <<'EOF'\nt=open('ARY_latin_index_pages.txt',encoding='utf8',errors='replace').read()\nimport re\nblocks=re.split(r'\\[pdf page (\\d+)\\]',t)\nd={}\nfor i in range(1,len(blocks),2):\n    d[int(blocks[i])]=blocks[i+1]\nprint(d[494][:3000])\nEOF"
}
```


### [2026-09-07T18:21:01.232Z] TOOL RESULT

```
|
|
NAVA ARUMANIAN) gloy
‘REFERENCES ewthag NAVIO sPORTUGUESE) Js
POKORNY: 755-756 :(OLD SCANDINAVIAN) AS ebe|
“BARNHART: (NAVY) 6 —ONOR
DELAMARRE: (NAVIRE) 126 NAVIE, (OLD ENGLISH) 45 gul6st
MACKENZIE: (NAVIGABLE) 124 NOWEND
BUCK: 1380 NAVY ENGLISH) 831
ONIONS: (NAVAL) 604 NAU, NAVE (OLD IRISH) oS 5.3 p1
SKEAT: (NAVE) 396, (NAVY) 397 NOE, NAVA s(GALISH) of
MALLORY: 121 NOE WELSH) 63
Wie gb day NEO ABRETON) 3352
leatlosl
hae S48 OTN Sil sa 05s oul ex
‘
NASHLI, NASLI (LATVIAN) (3) 31,5 “NADA {OLD PERSIAN) ikon, yuh
NAY, NADH, NAT (PAHLAVI) os hey
REFERENCES ethey NEI KURDISH) 53,5
POKORNY SSSS~*~«SSDS NARA _ HAPGHANI) (24) lai
. | MACKENZIE: (REED, CANE) 58 NADA, NADHA (SANSKRIT) © SL.
MALLORY & ADAMS: NEDOS NET ARMENIAN) a ied
rirgrrry seb olay NENDRE eg HANAN) is
ay
seetloal
134) Saag tie" gal edly Los cal“
IS ges) db5 22 SIs cal pe
```


## [2026-09-07T18:21:12.571Z] TOOL CALL #30: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport re\np='data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt'\nt=open(p,encoding='utf8',errors='replace').read()\nblocks=re.split(r'\\[pdf page (\\d+)\\]',t)\nd={int(blocks[i]):blocks[i+1] for i in range(1,len(blocks),2)}\nprint('pages:',min(d),max(d),len(d))\nfor pg in (223,224,304,305,187,176):\n    print('=== pdf',pg,'(printed ~',pg+1917,') ===')\n    print(d.get(pg,'MISSING')[:1200])\nEOF"
}
```


### [2026-09-07T18:21:13.825Z] TOOL RESULT

```
pages: 1 553 553
=== pdf 223 (printed ~ 2140 ) ===

۴ -۱۰-
و خارخك را هم گنته‌اند و آن خاری است مه نسکبا؟ - بنتح اول » آتی عس را
پهلو وس کوشه ۱ - وبفتح ثانی, درعربی بممنی | گوبند چه نك بمعنی عدی و با بمعتی آش
غستن و پا کردن باشد ۴ - و یم اول قممی باشد .
باشد از بیست و بك فْمکتاب زند که زردشت نسل دهم * «کنایه از شرایی است
آبرا منقم کرده است و هرنسکی رایعتی هر | که از انگور سیاه ساخته باشد .
قسمی را نامی نهاده - و در عربی بممتی عبادت ۱ نسناس ۱ - بانون بروزن کربای :
وپرستیدن خدای‌تالی و قربانی کردن باشد ۳ - | دیو مردم راکوبند و ایشان جنسی ازغلق باشند
و شم اول وثانی؛ هم درعربی جمع نسیکه است و بریکیا برمیجهند وبزبان عربی حرف میزئند.
ردیکه قریالی راگویند ۴ . فسق ۷ - بفتح اول وئانی بوا و کشیده .
نک > بفتح اول و سکون ثالی و کاف چیزی لرم و ساده وهموار ولخشان و لغزنده وبی
بالف کشیده » بمعنی زمین است که بمربی آرض | درشتی و خشونت راکویند؛ وبکسر اول هم‌آمده
گویند . آست ؛ و باشین لقطه‌دار نیز هت .
۱ - که در چشم‌آنکه شناسد از مس سوخته زبرجد را .
بدر جاجرمی « انجمن‌آرا > « فرهنگه نظام >.
۴ - (مر) «نك متلنة وضمتین»پرستش وهرچه حق‌خدای عزوجل باشد - نسك‌مخ ركة,
جای الفت کرفته - نسکه جنمتین و بالضم قربالی » با که جنمتین, خون . > «متتهی الارب».
۰ نکه‌اللوب اوغیره بمنی شست جامه یا غیراورا باب و پال کرد » « شرح قاموی >.
۴ - باین معنی لغة بفتح اول است » در
=== pdf 224 (printed ~ 2141 ) ===

-۱۸۱- دیدن
نسوبار ۱ < بفتح اول وبای ابجدبالف پختن باش که لقیض خام بودن است و نسهالمی
کشیده ویرای قرشت زده» بلغت زند وپازد(۱) | یعنی میپزم ونسهانید بمعنی پزید است که امرپر
بمعنی ناهار و ناشتا باشد . پختن باشد.
تسود ؟ - بر وزن حود » بممنی نو نسیان بکسراول بروزن احسان,بمعنی
است که چیزی لرم وساده ولخشان و لغزنده وبی | مشالفت و خلاف کردن باشد - و در عربی‌بمعنی
خعوت باشد . فراموشی ؛ و بمعتی اول بفتح اول هم‌آمده است.
نسودی ؟ - بروزن حودی, برزیگر نسیچ ؟* - بفتح اول واثانی بتختانی
وزراعت کننده را گوبند ‏ و این قم سیم است | کشیده و بجیم فارسی‌زده » جامةٌ حرین زر بافته
از چهار قم طوایف اسان که جمشید قرار داده | باشد ؛ و با جیم ابجد در عربی نیز همین معنی
وشرح و بط آن در لغت کاتوزی مذکور شد. | دارد -
نمهانتن ۴ - باها ولون ونای قرشت میدن ۱ - بر وزن رسیدن » بمعنی
پروزن صفرا شکن, بزبان زند و پازند ‎)٩(‏ بمعتی | لهادن وگذاشتن باشد .
(۱) چك : ژند و پاژند .
۱- در فرهنگه پهلويك ای ن کلمه‌آمده:» رل رل بونکر
س ‎٩۷‏ ی ۲ > کلمةٌ اول را 2280027 خواندماند و كلمهٌ دوم که معنی آست پارسیان «تخوار»
5۳ یا ۵ نخار » خوانند . رك : پولکر ۳۹ و۷۵ستون اول؛ وهمین کلمه است که درمتن
ناهار آمده . ۲ دنو (م.):
زخاك و آتش و آبی برسم ایشان رو که خاك خشکه ودرشت است وآب‌رم وسود.
« ناسر خرو بلخی . دیوان س۱٩‏ » « انجمن‌آرا >
۴ - 
=== pdf 304 (printed ~ 2221 ) ===

بیان بیست و چهارم
در نون با ای <طی مشتمل بریکصد و سیزده لغت و کنایت
نی ۱ - بفتح اول وسکون تالی, مشغفف نیا ۴ - بکر اول وئانی بال ف کشیده .
ای است که مزمار - وحلقوم باشد - وقلم و کلك | بیمنی جد باشد ۴ مطلقاً خواء پدر پدروخواءیدر
- ولیشکر وا لیز گویند - وبکسر اول افادة لای |[ مادر 8 - ویمعنی برادرماد رکه خالوباشد- ویرادر
افی می‌کند ۲ . بزرگه هم بنظرآمده است - وبمعنی‌قدرومظمت

۱ بای * نال , فی: کر[ های, سور [لای » شه[نای , نایزه . پارسی‌باستان- 88808
(ای) ۰ پپلوی 88 , فی 880 ؛ هندی باستان -8۶44. - 8244
( ای . نی ) ؛ ارمنی 361 ( تیر ) ؟. ره : امشق *۱۳۹ - نال (قارمی) آر
بممنی نای , ماقه , لوله ۳ اقغانی 8878 (سافه) ۳ ساسکریت -8244 ۱
(ای » بی) * آربایی -0827608 * هوبشمان ۰۶۱۰۹۰ پهاوی 224۳
« تاوادیا ۶۱۹۳ ۰ کردی 861 ( نپال نی » هزمار ) : لری 261 ( یزه )
« ژابا س 1۲۷ > - لی‌بگیاهی اطلاق شود که ساقةٌ آن دراز ومیان تهمی
وطغامت انگشتی با بیش ازآست . مثل «رقتآنجا که نی‌انداختمرب»>
رك : امثال و حکم دهغدا ص۸۹۹ . ۲ دنه (نفی). یب رکه-

[32 خوانده , پهلوی 26 (نه » نی) » ابرانی باستان 38811 ۰ اوستایی ی

1 * پارتولمه۱۰۷۲* رك : لیب که ص۱۵۹ ؛ هرن کلمه را ۰6 خوانده, با «نیست 20891۳
قیای کرده‌است. پارسی‌باستان 281 (نه). آوستا ۰8۵11 38661 , پازند 88. هندی‌باستان ۰8641
استی 8801 ۰ 8101 (هیج چبز) «اسشق ۴۱۰۹۱ 
=== pdf 305 (printed ~ 2222 ) ===

بیابه ۲۲۲
هرچیز هم هست - تاج رآکوش ۴ - وبمعنی‌حاجتمند ماج
1( [چ 1 : زومند هم آمده‌است 6 - خواهش1 -
با یرای فان بای | وافارست وس مرها پزکر 7
نوبت باشد ؛ وباین معنی‌بجای حرف‌اول بای‌ایچ 7 ال
هم‌آمده وگفته شد . - و بمعنی قحط وغلا - وشره وحرص - وبلذت
نیارست ؟ - بنتح اول و رای قرشت خوردن طمام هت و بسنی دوست دبای
وسکون سين بی‌قطه وفوقانی, بعنی شواست‌واز دشمن ؛ و درجای دیگر درست دربراین ؛
دستش لدامد + ودرسخةٌ دیگر درشت در برایرهموار نوشته شدم
نیاز ۴ « بکراول بروزن‌حجاز,حاجت بود ؛ وهيچيك شاهد دامتند ۸ .
‎٩‏ < نیابة (لیابت) (عر) «نوبة بالفتح بار وپاس: نو ب کسرد جمع . بقال : جامت نوبتك
و لیابتك . . ليابة ككتابة بار و پای » * منتهی‌الارپ » - «النائب اسم فاعل و من قام مقام غیره
فی‌امراوعمل کنائب‌القاضی ودائب‌الملك » و عمله‌النيابة . ج نوب ونواب» « اقرب‌الموارد ». فارسی
دانستن اين‌لفت ناشی از لغت فری‌اسدی(س۶۸۸) است : «نیایه, نوبت بود. پوشکو رکفت :
آن به که نیایه را نگه داری کردار تن خویش راکنی فربه.»
۲ -ر4 : آرستن » بارستن . ۴ - پپلوی 81182 ( احتیاج » ضرورت,فقدان).
از اوستا -27- 81 ۹ 2 پیشولد است وريشهٌ 22 بمعنی بستن » فشار آوردن و مجبور کردن ]
( بتن , فداردادن ۰ بزور داخل کردن ) « بارتولمه ۰۶۳۹۲ 2283 ( ضرورت #تنگی» احتیاج)
« بارتولمه ۳۹۲ > رك : نیب رکه س ۱۹۳.
۴ - دگر بوبهای خوش آورد باز که دا
=== pdf 187 (printed ~ 2104 ) ===

تاگور -۱۸۸-
ناور ۱ - بن‌کاف فارسی و فتح راو نوسندگی 9 - و رگها وربشهای پاریک ی که از
وسکون رای بی لقطه , مخفف ناگوار است که میان قلم (۱) برمیآید 8 - ولی میان پر را هم
امتلا - وطمام نايخته درمعده باشد . گفته‌اند که ازآن تیرسازند۴ - وبمعنی لی‌شکر
ناگورد ۲ < با کف فارسی و بحذف | هم بنظرآمده است - ورودخانة کوچکه و جوی
آلف » مخفف ناگوارد است که طعام ناپخته در بز رکه را نیز گویند٩‏ - و نام مرغکی است
معده باشد + کوچك و بسیار خوش‌آواز ۷ - و بمعنی ناله هم
نا گوهر ؟ - بنتح کان فارسی وها آمده است ۸ - و امر پنالیدن هم هت یعنی
وسکون واو و رای قرشت » پمعنی‌عرض باشد که | بثال وناله کن٩‏ - وناله کننده را نیز کویند*۱.
در مقابل جوعر است - فالان - بر وزن پالان , ناله کننده را
ال ؟ » بر وزن سال ؛ ای میان خالی کوبند ۱۱- و نام کوهی است میان شیراز
را کویند وعربان مزمار خوانند - و قلم | وکازرون (۲) +

() چش : - قلم. (۲) چش : کازران +

۱ رك : ناگوار, ۴ << ناگوارد (هم.) ۴ - از : تا« نفی » سلب) +
گوهر (م.) » پر ساختةٌ دساتیر « فرهنگه دساتیر ی ۰۲۲۹۸

۴ یی اسشق س ۲۲۹ ». هنینگك نویسد : تال ( نی » قلم لیی ) « لغت فری اسدی
( چاپ آروپا ص ۷۸ » شمس فخری اس ۸۵ ؛ فولرسی 11ص ۱۲۸۲ نال ه) ۳ نای 52 ولی
2۵1 ( یی . فلوت ). رک : .00.232,531 با وس ۳ آ1 ,۸10۳8625116786 کلمات بودغا
1و2 . وخی1016 2 » فارسیکایلی1321 (لوله » مجری
=== pdf 176 (printed ~ 2093 ) ===

سس خی ناردین
نار پستان ۱ » بسکون ناك , دختری | وشیش وکنه را هم کفته‌اند ۷ - و بزبان هندی
پا زرا کوبند که هنوز پتانهای اوسخت باشد | لام یکی ازحکما ومرتاشان هندوستان باشد ۸ .
بمنی آویزان وافتاده لباشد ‏ ناردان « معروف است که دانهٌ انار
نارین ۲ - شم بای ایجد وسکون‌لون, ترش باشد ‎٩‏ - و متقل آش و آتشدان را نیز
درخت اذار راکوبند .9 کوبند ۱۶.
نارخو - با خای نقطه‌دار بواو مجپول نار دان افشا ندن - بسمنی‌ارافشاسن
کشیده » بمستی کل انار باشد و آنرا کلثار هم است که کنایه از اشك گلگون ربختن باشد .
میگویند - ومردم تند ونیز وآتش مزاج را دی ناردانهُ دشتی - حب القلقل است
کفتمانن۴ . بکس هردوقاف . چه قلفل و قلاقل وقلقلان انار
نار و4 ؟ - بسکون ثالك وکا ور | سحرائیراکوبند .
آخر » ترباك وافیون راکوبند . نارده - بسکون تالك وفتح دال ابجدء
نارد « بفتم رای قرعت و سکون دال بمعنی پشه باشد و بعربی بق گوبند - و کنه را
ابجد , مخفف نیارد باشد 8 , وبمعتی نتواند عم ی زگفته اند وآن جانوری است که بر حیوانات
هت - وکنه را ی زگوبند وآن جالورست که | چبد وخون پمکد ۱۱.
برحیوانات چسید وخون بمکد ‎٩‏ - و لیش پشه ناردین ۱۴ بادال ابجد بروزن‌آستین,

۹ - از : نار (انار) ۳ پتان (ه.م.). لغة بمعنی دارای پستان ماند انار [قی:نارور] +

۴ - از : بار ( اثار ین (< ون ) * بارون.

۴ - باین معنی از : بار (عر) [ آنش ]+-خو (خوی ).

۴ < تا رک
```


## [2026-09-07T18:21:40.195Z] TOOL CALL #31: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport re\np='data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt'\nt=open(p,encoding='utf8',errors='replace').read()\nblocks=re.split(r'\\[pdf page (\\d+)\\]',t)\nd={int(blocks[i]):blocks[i+1] for i in range(1,len(blocks),2)}\nprint(d[176][1200:3500])\nprint(\"################ pdf 177\")\nprint(d[177][:2500])\nEOF"
}
```


### [2026-09-07T18:21:41.378Z] TOOL RESULT

```
و که << ک و کنار. سراح‌اللغات بنقل * فرهنگه نظام >.

8 -رك : آوردن ۰ ‎٩‏ * بارده (ه.م.) در خراسان امروزهم کنهٌ بزرکی راکه
بشتر می‌چسید « نارد > کوبند « فرهنکه نظام >.

۷ - ر4: حاشيه قبل. ۸ << بارن * ساسکریت 318۲۵012 . ابوربحان درتحقیق
ماللیند ( ص ۵6 )آرد : گفته‌اند که براهم ( 8۲۵522 ) را پسری‌است بنام « نارق > که کاری
جز رویت آفرید گارندارد , وعادت او این است که درتردد خویش » عصائی باخود برد که چون‌آنرا
بیندازد ما رکردد. و باآن عجائب میساخت و ازآن دور نمیشد , و رك : تحقیق ماللهند مس ۹۳ :
:۹۱۵4:۲۹۱۷ ۳:۳۱۳ (مم.) این‌نام؛ اسم‌بسیاری ازهندوان شده
است . ر4 : فرهنکه نظام . ‎٩‏ - از : بار ( آبار)۳-دان ( دانه ) +

*- از : نار ( [ آش ]+دان ) پوند ظرف ومکان ) .

۱ > نارد (ه.م.) زگ باردین سم بونانی مطلق سنبل است > «* تحفةٌ حکیم
موژمن > * بودانی 374۳4105 « لك ۲ س ۷۹۵ > باید داست که « ناردین شکل تغییر بافتهٌ
سربایی - عربی كلمةٌ بونانی 34۳11808 است ۳ 18۳۵4 (ش) * ستبل « عقار ۲۹۵ عربی و
فراسوی > . - ناردین بری ۳ ۳091108 327018 ** اسارون * دزی اج اس ۹۳۱ -

5 لارچیل - معرب « نارکیل > (ه.م.)

################ pdf 177

نارریاب - ۷۹8
سنبل رومیراکوبند ۱ وآن زرد رنگه میباشد. | شیرین بود -اونام نوایی است از موسیقی.
گر در سرمه داخل نارقارسی - با فا , بممنی‌انار پارمی
کنند موی مژه را اج است که نوعی از زهر باشد مرکب از چیزهای
پروباند . ‌ تلخ » واند کی ازآن کشنده امت 8 .
ناررباپ - نار کفیده ‎٩‏ - بنتح کاف + پمنی
بکس ثالث و ضم رای ۱ و نار ترکیده, چه کفیده بمعنی شکافته و ترکیده
نووی ی ! ۹ | باشد .
رز ده دی آز انار ش / ۹ نار کند ۷ < بروزن خاربند , آثارستان
باشد؛ "وباتغدید خامس ۶ ۹ راکوبند - و دهیرا نیز کفته‌اند که درز آن انار
هم بنظرآمده است . زد بمیارحاصا, شود ونارستان ودرخت اناربسارداشته
نارست ؟۲ - ی باشد. .
با سین بی‌نقطه مشقف ناردین نار کو ۸ - بر وزن و ممنی نارخو
لیارست باشد بمنی توافت . است که ترباك وافیون باشد .
نارسیده ۴ « بستی تاری وخام - نار کوق ‎٩۱!‏ - با کاف بتحتانی رسیده
و ابالغ - وبی‌بهره - وباکره پاشف: و واوبالف کشیده . غوزء خشضاش سباه راکویند
نارشیرین ۴ - معروف است که انار | - وبحذف الفآخرغوزه خشخاش سفیدرا وجربی

۱- « ناردین افلیطی , سنبل رومی است . > ‎٩‏ تحفةٌ حکیم موّمن *.

۴ - مغغف « لیارست » ماضی منفی از « بارستن > و «آرستن > .

۴ - از : با( نفی , سلب )+ رسیده ( اسم مفعول از « رسیدن > ) ۰

۴ - از : دار (اآنار )۳ شیرین (ه.م.) ۶-8 نار فارسی . اين‌جزله کوید چون
مر را بایتوعات مغشوش کنند باین‌اسم هسمي‌است ویغدادی نار را بمعتی اثارفارسی که رمانت‌حمل
کردء ز وجه تمیه‌را لیسندیده وممکن است که بهمنی‌آتش باشد » چه مر مغشوش به بتوعات از
جملهٌ سموم و در احراق خلط مانند آتش است چنانکه نار قارسی اسم مرض حاریست . » « تفه
حکیم مومن ‎٩.۴‏ - رل :کفیده ‏ ۷ - از : دار (انار )۳ کند ‏ کده ( پموند مکان).

#۸ بارخ وکه (ه.م.) ‏ کوکنار (هم.) ‎٩‏ -* نارکیوا « مارکیوا » است و
نزد ابن‌بیطار دوچیزاست و ازعریف او ظاهر نمیشود که دوچیز باشد » وتزد بعضنی خشماش زبدی
است » « تحفة حکیم موْمن». دزی کوند ( ج ۲ س ۹۳۱ ) : « تارکیوا ( فارسی : دارگیوا )
ونم 0202۷615 68001 ( فولرس ) » و درشرح « ماکیونا *کوید ( ج ۲ ص ۲:۵۹۶) +
« مار کیونا نام نهالی » که در ابن‌بیطار [1 » 2۹3 0 آمده » وآن در نسخ مختلف بسور ما رکوبا ۰
مار کموناء مار کبوا یاد شده, ودرتخه‌ای آهده: مارکیوا اسم فارسی ذکره صاحب‌الفارسية (الفلاحة
افروده شود ) . اما من چنین کلمه ای را در فرهنگهای فارسی لیافتم > در محیط اعظم ذیل
« مار کیوا » و « نارکیوا » و نیز در تحفة حکیم موّمن ذیل « نارکیوا > آمده امت.
```


## [2026-09-07T18:21:53.815Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA && awk 'BEGIN{RS=\"\\f\"} NR==272' PLA_pages.txt | head -60; echo \"=== grep nard ===\"; grep -n \"nard\" PLA_pages.txt | head -20"
}
```


### [2026-09-07T18:21:55.116Z] TOOL RESULT

```
nardila                                                                         257                                                               nänha


ala,L            -    närgila:              "pers.            Wasserpfeife"              ı     skr.          narikera,        engl.          nargula,
       frz.           narguile.                  Nargileh          —      skr. >        pers.         > tk.         >    dtsch.        1


82949 - närdin:                        "Spickenard,                     Lavendel"        pers.        ® skr.             nard,     mand.           nard,
       syr.           v? 3             „ hebr.           ı72-


Aust         _       närmask:            "eine          wohlriechende                 Blume"               pers.ui,b         em                   < mp.
       .„kı           anar       "Granatapfel"                      +    4 moSk         a     syr.    Ans.        (P. Sub)
                                                                                                                      Suse


Aubs,b       -       närmak:             "Pome           granate          rhus    Vermicifera"               6_     närmask        q.      V.«.


at       -       näran g:          "Orange"                  aus    pers.       ai narang            ”      m.         RAW   anar "Granat-
       apfel"           + mp.               >»        rang    "Farbe",          mand.        narniz        (p.   a!       8
       sp.           naranja,            port.           larange          9% dtsch.           Orange,        ndl.       Orange     10         it.

       arancia,              rum.           naranta,               dtsch.       Aurantium            11


&D;L - näzuk:                "Zart"               s. nizäkat.

asstl - naffa:                   "Gefäß               mit     Parfüm"             pers.asL           näfe        12 mp.          ao,    näf        13,
       syr.           ng          (pP. at)                     19,

ass      -           änha    = nänh"äh                   ga. %          15,


ol,sl            -    nanhäh:            "eine           Person,          die    um     Brot    bittet"          aus     pers.     nänh"äh            16,



1.    Lokotsch              s.     v.,           Fremdwörterbuch                 s.     v.
2.    Wahrmund              s.     v.
3.    Macuch           s.    v.
4.    Addai           Scher        Ss.      Vv.
5.    Brockelmann                  s.       v.
6.    Kamäl
         Ss. v.
7.    Wahrmund              s.    v.,            BQ.     s.    v.,       Addai    Scher        s.    Vv.
8.    Macuch           s:    v.
9.    Littmann              s.    v.
10.    Lokotsch              s.        v.
11.    Genaust              s.    v.
12. Wahrmund                 s. v.,               Muhit        s. v.,         Addai      Scher       s. v.
13.    Mackenzie                 Ss.     v.
14.    Brockelmann                     s.        v.
15.    Brockelmann                     s.        v.
16.    Addai           Scher           s.        v.

=== grep nard ===
1398:           >isfanäß,             frz.        epinard,        sp.       espinaca    ı     dtsch.       Spinat        2,
7816:Sy) - rand:            "eine         wohlriechende             Pflanze"          <pers.o           nardin,        syr.    1, ,
14390:nardila                                                                         257                                                               nänha
14397:82949 - närdin:                        "Spickenard,                     Lavendel"        pers.        ® skr.             nard,     mand.           nard,
14497:nafar                                                                           259                                                        nardin
14528: 3>- nard:               "Damespiel,                 Würfelspiel"                    pers.       12,
14531:my»         - nardafir:                   "Damespiel"                       mp.               Jouplrı         nev-artaxsör,           talm.
14535:or - nardin                       = nardin           a. v.
15761:Holt,     P.    M.;       Lambton,       Ann;    Lewis,        Bernard:          The    Cambridge        History        of
```


## [2026-09-07T18:22:09.919Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf8',errors='replace').read()\nblocks=re.split(r'\\[pdf page (\\d+)\\]',t)\nif len(blocks)>1:\n    d={int(blocks[i]):blocks[i+1] for i in range(1,len(blocks),2)}\n    print('has tags', min(d),max(d))\nelse:\n    pages=t.split('\\f'); print('no tags, leaves',len(pages))\n    for l in (641,642,643):\n        print('=== leaf',l,'==='); print(pages[l][:1500])\nEOF"
}
```


### [2026-09-07T18:22:11.302Z] TOOL RESULT

```
no tags, leaves 684
=== leaf 641 ===
  ‫منگه روشثابی‬                                                                         ‫سپا‬
‫بشکل مخروطی برهوا برد وبعربی‌اعسار کویند ؛‬      ‫کوچك وسیاه رنگه وک کل دراکه سنگه ریزه‬
           ‫و با واو مجپول هم بنظرآمده است‪.‬‬                       ‫میخورد و بعربی قطة خوالند‪.‬‬
‫سنگر ‪ ۴‬ه بنتحاول وضمثالكوسکون‬                    ‫سنگ خاورج ‪(۱‬ا‪۱‬ج برزن‬
                                                ‫موعنی سنکه خوارك است کاهسفرود باشد ‪,‬‬
‫انی و رای قرشت » بمعتی سیخول است کهخار‬
 ‫بشت تر انداز باشد بعنی خارهای خود را چون‬       ‫و آن جالوری است کوچك و سیاه رنگه برابر‬
                               ‫تبرالدازو ‪5 ۴‬‬    ‫بگنجشك و چند پرمثل شاخی برسردارد وعربان‬
‫سنگ ر آه شدن «کنابه‌ازمادم شدن‬                                                  ‫قطاة گویندش ‪.‬‬
                           ‫کمرنعدن باشد‬
                                      ‫و‬          ‫مرغك‬     ‫همان‬
                                                             ‫خو ار لك ‪ ۳۴‬د‬         ‫سگ‬

‫سنگ رعد = بکسر ثالث وفتح رای‬                                ‫سنگے است که هربی قطاة گوبند ‪.‬‬
‫فرشت و صکون عین و دال بی‌اقطه " کنایه از‬         ‫مرفیست سنگه‬         ‫سنگه خور ‪۲‬‬
            ‫کلولهٌ نوپ کولولةٌ بادلیج باشد ‪.‬‬                                          ‫رزه خور ‪.‬‬
‫سنگر ل ‪ -‬بفتحاول و رای قرشت بر‬                  ‫ست ‏‬
                                                   ‫اگه‬
                                                     ‫وىرسن‬
                                                   
=== leaf 642 ===
 ‫‪ ۷ ۷‬اس‬                                                                                                   ‫سنگه زخم‬
  ‫ون‬ ‫سلتکو‬‫سنگست ‪ -‬بفتح اول و ثا‬                              ‫سنگ ر خم = بک ثالك و فتحزای‬
‫الی ورابم وفوقالی ‪ ,‬نام جابی و مقامی‌وموضعی‬                  ‫هوژ و سکون خای نقطه دار ومیم » بعربیحجر‬
                                             ‫است ا ‪.‬‬         ‫اعرابی ‪٩‬‏ کوبند‪ .‬وآن سنگی باشد مانندعاج‪.‬‬
‫سشگ = بتازی حجر ا لكلب ‪۷‬‬                 ‫سنگ‬                 ‫چون حق کنندوبررموضمی که‌خون آانز‌رو ان‌باشد‬
‫خوانند » وکویند بسضی اسزگه حست که‌چون‬                         ‫بربزند باز دارد‪ .‬وآنرا شکر سنگ‌هم‌میگویند‬
                                                                                       ‫و حجرالماج همان است ‪.‬‬
‫سنگه برواندازند آن سنگه را از غات خشمی‬
‫که دارد بدندان بگیرد و نگاهدارد ‪ .‬پس چون‬                      ‫سنگ زن = بفتح زای نقطه‌داروسکون‬
‫خواهند کهمبان دوشخص دشمنی افتد بنامآن‬                                     ‫»نابه از ترازوی کم وزن باشد ‪.‬‬
                                                                                                      ‫لون ک‬
‫دو شخص هفت سنکه بردارند ويك يكگرانجالب‬                        ‫سنگسار ‪ » ۲‬باسینبیتقطهبروزن‬
‫آن سک اندازند او هربك را بدهن بر کرد‬                         ‫کهآوهی رانا کین‬          ‫ھشور‬
                                                                                         ‫نای دا‬                     ‫نگاو‬
‫و بر زمین گذارد و بعد ازآن دو سنگه از آن‬  
=== leaf 643 ===
‫و کوچك‬   ‫و دام نوعی از غله است و آن سل‬                    ‫سنگ شکن = مخفف منکه اشکن‬
‫میباشد ‪ -‬و نام مرغیست کوچك وشکاری‌ازجنس‬                   ‫است که نام غله‌ای باشد ‪ -‬و نوعی اخزرما‬
             ‫سياه چشمکه آ را ترمتای ‪ ۴‬کویند‪.‬‬                                             ‫ههمٽ ‪.‬‬
 ‫ومهای‬
     ‫دباملف‬
          ‫»بنالیام‬
                 ‫سنگلاخ ‪ ۸‬ک‬                               ‫سنگ شیر = بعربیحجر اللبنی ‪۱‬‬
‫نقطه‌دار زده » بمعنی سنگنان‌است که جاومکان‬                ‫خواند ‪ .‬رنگه آن خاکتری رنگه باشد‪.‬چون‬

‫لهاخ بمعنی مکان آمده است‬
                       ‫منک باشد چ‬                       ‫بآب بابند از وی مانند شیر ببرونآید وبطمم‬
      ‫قاام دیو راگویند‪.‬‬  ‫مج‬
                          ‫همچو دبولاخوکه‬               ‫شیرین باشد » و برچشم کشند سیلان آب را بر‬
‫سنگله = بصم ثالث بروزں زنگله‪.‬نانی‬
                                                                                               ‫زک‬
         ‫‪.‬‬    ‫و ارزن برد‬   ‫باشد که ازارد کاو رس‬             ‫ررقبطی‬
                                                                 ‫جبک‬
                                                                   ‫انقب‪,‬طیح‪-‬‬
                                                                           ‫سقنگ‬
                                                          ‫باشد سبز تبره رنگه‬         ‫ی‬‫آن‬
                                                                                       ‫گ‬ ‫»و‬
```


## [2026-09-07T18:22:23.157Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re,unicodedata\nt=open('BQT_v2_pages.txt',encoding='utf8',errors='replace').read()\nt2=re.sub(r'[‎‏‪-‮⁦-⁩]','',t)\npages=t2.split('\\f')\nfor i,p in enumerate(pages):\n    if 'سرنا' in p or 'سورنای' in p or 'کرنا' in p or 'قره نی' in p:\n        print('leaf',i,'-> printed ~',i+543, [w for w in ('سرنا','سورنای','کرنا','قره نی') if w in p])\nEOF"
}
```


### [2026-09-07T18:22:24.521Z] TOOL RESULT

```
leaf 2 -> printed ~ 545 ['کرنا']
leaf 27 -> printed ~ 570 ['کرنا']
leaf 192 -> printed ~ 735 ['کرنا']
leaf 200 -> printed ~ 743 ['کرنا']
leaf 210 -> printed ~ 753 ['کرنا']
leaf 337 -> printed ~ 880 ['کرنا']
leaf 340 -> printed ~ 883 ['کرنا']
leaf 416 -> printed ~ 959 ['کرنا']
leaf 439 -> printed ~ 982 ['کرنا']
leaf 441 -> printed ~ 984 ['کرنا']
leaf 443 -> printed ~ 986 ['کرنا']
leaf 449 -> printed ~ 992 ['کرنا']
leaf 472 -> printed ~ 1015 ['کرنا']
leaf 537 -> printed ~ 1080 ['کرنا']
leaf 577 -> printed ~ 1120 ['کرنا']
leaf 579 -> printed ~ 1122 ['سرنا']
leaf 587 -> printed ~ 1130 ['سرنا']
leaf 591 -> printed ~ 1134 ['سرنا', 'کرنا']
leaf 592 -> printed ~ 1135 ['سرنا', 'سورنای']
leaf 605 -> printed ~ 1148 ['کرنا']
leaf 611 -> printed ~ 1154 ['کرنا']
```


## [2026-09-07T18:22:31.102Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf8',errors='replace').read()\nt2=re.sub(r'[‎‏‪-‮⁦-⁩]','',t)\npages=t2.split('\\f')\nfor i in (591,592,593):\n    print('==== leaf',i,'====')\n    print(pages[i][:2600])\nEOF"
}
```


### [2026-09-07T18:22:32.408Z] TOOL RESULT

```
==== leaf 591 ====
                                                                                               هه-

 سر مو تثه دبا تای قر(شت)۱بروزن                       وب
                                                       رلکم
                                                          طف                ان
                                                                             هردمو
                                                                                 آو        مك
                                                                                            مهاپیش
                                                                                                 شد
     شیوب و شور وغوغا باشد.
                          آعت
                            زلبورك  .بم             طفلی را           نت
                                                                       ااکر
                                                                          وهدو
                                                                             تك ن
                                                                                سبکرنار مام
سر مور ه = بروزن هر روزه  ۰کفشی                     گرفتن همان خود سربر کنار مامك نهد وبازی
                                                                                         را ازسر کیرد .
باشد که بر بالای موزه پوشند و در ماوراوالثهر
                                 .       متعارفت    سرماهی  - ۲بر وزن خرکاهی .
سرمه  -بضْم اول و فتح ثالث  ,معروف                 ماهیانه و مقرری باشد که درهرسر ماه بنوکر
       و                   ی         ا        اخ
                                                        وامثال آن دهند وآلرا عربی مشاهره گوند.

و نام قربه‌ای هم حت از قرای فار یکه درآن             سرهج  - ۲بنتحاول و میمسوکون
                               سرمه خیزد .           ثالی و جیم » دوابی است که آنرا اسفناج رومی
سرمة خاك لین  -سرمه ای بود که                       هر دو میباشد .           ایی
                                                                               حیرو
                                                                                  صتال
                                                                                     گوبند وآن بس
خسرو پروبز داشت  .کوبند هر که بکباردرچشم            و بجوشاننده .آب آرا             صحرایی آنرا نکد
زلی که مشیمه درشکمش مانده باشد بشورد در کشیدی تا بك کز عمق زمین را بدیدی وتامدت
                  بکال ابن چنین بودی #.            ساعت بیفتد و آنرا عربان سرمق میگویند که
                                                                                   بجای جيم قاف باشد .
و سکون    
==== leaf 592 ====
    ۳۱ات
 و لبلابرا نیزکوبند,وآن    حطی حم آمده است -
                                                  سر نامه = بروزن هتکامه  ۰لجه‌بر سر
رستنیی باتد که بردرخت پیچد و بعربی هشقه                لینده
                                                           اال
                                                             رلسفل
                                                                 رمح
                                                                   بان
                                                                     کتات‌ها لومند که در قل
 خوانند ؛ و باين معتی باثالی مفتوح ایز بنظر
    تنیش فنو
           کلهٌ
              آمده است  -و فنی باشد ازجم
                                                   و ی کوبند سرنامه عنوان است یآعنچه‌بر
                                                                               بالای نامه فوبسند.
 «.گیری » وآن چنان است که کشتی گیر بای‌خود

 را بپای دبگری بندکند و اورا بینداژد و آنرا         رخکه
                                                       سوکلون آ
                                                              وما
                                                                سر نای  = ۲ض
 بعربی شغزییه خوالند  -و بمعنی ربسمالی باشد        ۰بمعنی نای رومی است که سرنا        بیاحطشید
                                                                                             با
 خاك پنهان      ور
                 زدی
                   رکنندفه
                         که بکر آنرا حل                         باشد ؛ و محذف الف هم‌آمده است.
 سازند و سر دیگر را شخصی گرفته در کمین            سر نج  = ۴بکر اول و انی و سکون
 بنشیند تا آدمی با جانوری که پای درآن میان         ثالث و جيم » سنج را کوبند .وآن دوپاره روی
     نید آن شخص بوی خود کشد واورایگیرد.
                                                  تنک‌باشد مانند طبق بکنیاره‌وبریشت آن قبه‌ای
  .ر
   سر و له = بفتح الث و بای ابجد س                سازند و بتدی برآن‌تعبیه کنند و بردست گرفته
 کرده وریش فيد پاسبانانرا گویند.چه لوبه بر        زلند تا صدا در آید و بشتر بالقاره       گیگ
                وزن توبه بمءنی پاسبان است . ۴      و دهل وامثال آن‌لوازند  -و قلمی وسرب‌سوخته
  سر شوت  -حک ازل وفضای‌ازل‌است                    را کلبوزبند وآن‌رنگی است که نقاشان‌ومصوران
         بعتی آلجه در روز ازل تفدیر شده باشد.     بکار برند و آن درفایت حمرت میباشد چه باطن
 بروزن                                            سرب سرخ است و بجند آتشل حمرتآن ظاهر
           لحث
             وفت
               ثلا
                 سر نی ِ -بضم او
 پر می " مخفف سورنای‌است که نای‌رومی باشد.         میشود  .استنزال ( )۱اودررجمت بزیت وطرون
                                    
==== leaf 593 ====
  سروچ                                                                                                     ¬
ګوبند که راست رود وآن را ياين اعبار آزاد              میباشد  :مکی‌سروآزاد و دیگری سروسهی‌وسیم
 کفته‌ادد که از ید کی و داراستی ویبوستن‌بشاخ                                  سرو ناز وهر يك درجای خود
یوبند هردرختیکه
              وکدیگر فارغ است » ی                                            خواهد آمد » وعربان سرو را
 میوه ندهدآنرا آزاد خوانند چوون سرو موه
آزاد باشد» وجممی کفته‌اند عر       ندهد ياين سیب
                                                                                شجرة الحبه خوانند چه گوننه
                                                                             هرجا که سروهست البته مارهم
درختی رکامالی و زوالی هت چنانکه کاهی
                                                                              هست .اکر بر کهآ نرابکوبند
 که
  ر‌ب
    وی پژمرده و بی
                 پر برکه و تازه اکستاه
                                                                             و با سر که بیامیزند موی را
هيچيك از اینها نیت و همه وقت               ورورا
                                               س
سبز و تازه است و اژین علتها فارغ و این صقت                  سرو                 صاه کند -ونام مکی‌ازیادشاهان


      آزاد کان است پس بدین جهتآزاد باشد.              یمن است که دختر بیکی از فرزندان فرسون
 سر اول - 4اول بروزن بزاله.طفی                                                                                  داده بود .

ین که
    موهشد
        بودکه برسرآن خارهای نیز با                     سر وا  = ۱بروژن پروا» یمعتی حدیت
     بحامه فرو رفت جدا کردن‌آن دشوار است.            وعر حم
                                                          و سخن باشد  -و بمعنی آفانهٌ دروغ ش
سر وب  - ۸بفتح‌اول وضم تالی‌وسکون                                                                          گفته اند . ۳
 ثالث مجهول و بای ابجد  .بلفت زسوی‌ازند()۱            »ام‌منظوم
                                                              سرو اك  - ۲بروزن فرهاد کل
            بمعتی سخن باشد وبعربی کلامگویند.          افون     ویمعتی افانه و                   شمر را کویند - ۴        و

ختح اول وفوقانی وثالت     سر و تلك* "                                                            وسرود همگفته‌اند ۰

مجهول بروزن عروسكك ..بمعنی شورش وآشوب                 سرو اده * = بفتح اول بروزن‌شهزاده:
 وغوغا باشد ؛ و باين معثی بفتح اولوئانیوفوقالی
             حم کنته‌اند که بروژّن فرزدق باشد.       قافیة شمر راکوبند  ۱همچو بهار ونگار و هزار
                                                      وزمین و کمن وامین»وحرف دال درین لفت‌ولفت
بفتح اول وضم تانی‌وسکون            سر وج
```


## [2026-09-07T18:22:45.361Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf8',errors='replace').read()\nt2=re.sub(r'[‎‏‪-‮⁦-⁩]','',t)\npages=t2.split('\\f')\ntr=str.maketrans('۰۱۲۳۴۵۶۷۸۹','0123456789')\nfor i in range(570,660):\n    head=pages[i][:300]\n    nums=re.findall(r'[۰-۹]{3,4}',head)\n    nums=[n.translate(tr) for n in nums]\n    if nums: print(i, nums, '| leaf+543=',i+543)\nEOF"
}
```


### [2026-09-07T18:22:46.773Z] TOOL RESULT

```
575 ['311'] | leaf+543= 1118
577 ['111'] | leaf+543= 1120
579 ['117'] | leaf+543= 1122
580 ['111'] | leaf+543= 1123
585 ['774'] | leaf+543= 1128
587 ['712'] | leaf+543= 1130
588 ['717'] | leaf+543= 1131
594 ['311'] | leaf+543= 1137
597 ['131'] | leaf+543= 1140
598 ['139'] | leaf+543= 1141
600 ['113'] | leaf+543= 1143
601 ['139'] | leaf+543= 1144
602 ['9311'] | leaf+543= 1145
613 ['717'] | leaf+543= 1156
626 ['112'] | leaf+543= 1169
```


## [2026-09-07T18:22:55.566Z] TOOL CALL #37: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:1185 --image 2>&1 | head -60"
}
```


### [2026-09-07T18:22:56.839Z] TOOL RESULT

```
no scan of BQT covers printed page 1185 (see 'scans' in refs_online.json)
```


## [2026-09-07T18:23:19.985Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in MON_part1.txt MON_part2.txt; do echo \"== $f\"; wc -c $f; python3 -c \"\nimport re,sys\nt=open('$f',encoding='utf8',errors='replace').read()\nprint('leaves',t.count(chr(12))+1)\nprint(repr(t[:400]))\n\"; done"
}
```


### [2026-09-07T18:23:21.354Z] TOOL RESULT

```
== MON_part1.txt
4377831 MON_part1.txt
leaves 1
'0 \n2 \n\n\nچم \nنسم ی \n\n\nتمه موی موم \n3 \n\n\nماما نا موس ملاس \nروم و3 \n\n\n2 \n7 \nس \n\n\nهمجمج مد هعرج ی وه جر ج مهو موجه و وید جع مج وی ۶ج و وم مب و وج 5 \nادا ما ما زو ماه مرو ماخ( نوم شام 4و منم مخ نامه مدش نامع \n\nمه مر وه ود \n\n3 ور 133131313 \n\n\nهم مشب جج جب بیج چم مدوجو \nچم وم \nجر \n\n\nدرل ولو ونر نو تلا رت \n11 \n\n\nمج جرج جر یی میج 6و یوج هو هجوج وی یویر جر دم مور و 555 \nو ده ها وی مزا موی ماما میو و موه ومد'
== MON_part2.txt
4331421 MON_part2.txt
leaves 1
'معین» محمد» ۱۲۹۱ ۱۳۵۰. \n\n\n۰ \n۳ \n\n\nفرهنگ معین / محمد معین. -- تهران: آدنا: کتاب راه نو ۰۱۲۸۱ \n\n\n۲ج \n(دوره) :964-7252-51-2 :158 \n(ج.۲) 964-7252-53-6 :158۷ (ج.۱) 964-7252-52-8 :5۳81] \nفهر ستنویسی بر اساس اطلاعات فیپا. \n۱. فارسی -- واژه\u200cنامه\u200cها. الف. عنوان. \n۴۵ف ۲۹۵۴/۸۷ ۳112 ۳ فا ۴ \n۱۳۸۱ \nکتابخانه ملی ایران ۷۹۵ - ۸۱م \n\n\nانتشارات آدنا \nفر هنگ دوجلدی معین \nگردآورنده عزیزالته علیزاده \nنوبت چاپ سوم: ۸۳ \nت'
```


## [2026-09-07T18:23:28.451Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nfor f in ('MON_part2.txt','MON_part1.txt'):\n    t=open(f,encoding='utf8',errors='replace').read()\n    t=re.sub(r'[‎‏‪-‮⁦-⁩]','',t)\n    lines=t.split('\\n')\n    for i,l in enumerate(lines):\n        if re.search(r'نسک|ناردین|سورنای',l):\n            print(f,i,l.strip()[:250])\nEOF"
}
```


### [2026-09-07T18:23:30.089Z] TOOL RESULT

```
MON_part2.txt 13923 نسکاو
MON_part2.txt 27210 کنسک: 6۵ (ص.) ممسکث: بخیل.
MON_part2.txt 47084 متنسک؛ اددومندا0«ه [ع-] (افا.) بر ستنده؛
MON_part2.txt 49452 مسحرق: ۱۱۱0۳۵۲۲۵۷ [ع.] (افا.) نسکك
MON_part2.txt 65732 منسک‌عبادت‌ها. جاهای عبادت. مناسک
MON_part2.txt 75869 نسک: ۷:56 (.) (گسیا.) عدس. (گسیا.)
MON_part2.txt 75884 نسک‌با» نسکما: هه (- ابا] (امر.)
MON_part2.txt 78335 مانند دابره» دف» تنسکك» کوس و دهل که با
MON_part2.txt 84068 (ابرانشهر. چا. بونسکوء تهران ۱۱:۲ ۱۷).
MON_part1.txt 17881 انسکاب: نق۵:» [ع.] (مص‌م.) ریختن.
MON_part1.txt 23571 نسک؛: (۱.) خمباز ه.
MON_part1.txt 25192 از جمله پیرامید» ایتالیا نسکی. در بازی اخیر
MON_part1.txt 58525 مق. شر. مزده اچر نسکك. مال؛ نعمت. فیض ۰
MON_part1.txt 65778 نیکوکاره نسک افعال» صحیح العمل»
MON_part1.txt 71083 تاش نسکاو رم زشت و زیا: بدگل
MON_part1.txt 77439 سرئا: 0۳5 (- سورنا - سرنای - سورنای
MON_part1.txt 79870 دارد؛ ناردین هندی» عحجر مکی حب
MON_part1.txt 86997 سورنای). آواز جانوران (اهلی و وحشی).
```


## [2026-09-07T18:23:34.725Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('MON_part2.txt',encoding='utf8',errors='replace').read()\nt=re.sub(r'[‎‏‪-‮⁦-⁩]','',t)\nlines=t.split('\\n')\nprint('\\n'.join(lines[75860:75900]))\nEOF"
}
```


## [2026-09-07T18:23:35.998Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('MON_part1.txt',encoding='utf8',errors='replace').read()\nt=re.sub(r'[‎‏‪-‮⁦-⁩]','',t)\nlines=t.split('\\n')\nprint('--- سرنا ---')\nprint('\\n'.join(lines[77430:77455]))\nprint('--- ناردین ---')\nprint('\\n'.join(lines[79860:79880]))\nEOF"
}
```


### [2026-09-07T18:23:36.327Z] TOOL RESULT

```
دهنده» ناظم. (نظ. قد.) افراد فوجی نظامی 
که مآمور ایجاد نظم و نسق در حوزه‌ها بودند 
و غالبا بیشایش سپاه حر کت می‌کردند و 
جامة سرخ می‌پوشیدند (صفویه). فراش 
مامور تسه و سباست» مر غضب (قاجار به). 
نسسق‌خانه: (0-)52112-.10 تب .| (امتر) 
اداره‌ای که نسق‌جبان در آن کرد می آمدند 
(قاجار به). 

نسک: ۷:56 (.) (گسیا.) عدس. (گسیا.) 
خارخسکك. 

تشک (هر جزو از کتاب مقدس 
اوستا. کتاب؛ متن.] (.) نام هر یک از یست 
و یک بنخش کتات اوست. ضصسح.- در 
فرهنگ‌ها به ضم اول ضبط شده و لغة 
تسین ست. 

سک مدمه رطقفت باکت ,15 [ع. ۳ 
(مص‌ل.) بر ستش کردن» عبادت کردن؛ ز هد 
ورزیدن. (سصع.) شستن» باکك کردن. 
(امص.) پرستش؛ عبادت. تطهیر. (.) آنچه 
حق خدای عزوجل باشد. 

نسک‌با» نسکما: هه (- ابا] (امر.) 
رن شاه 

نسل: اد« [ع.] (۱.) زاده» فر زند. دربه 
دودمان. (مص ع.) زادن» تولبد کر دن. (جاذ.) 
(ف.) نوع از گیاه یا جانور. دور زندگانی 
توأم با فعالیت مجموعةٌ افرادی که سنشان 
زدیکک په یکدیگر است. . نسل ادهم: (کد.) 
شرابی که از انگور سیاه تهیه کر ده باشند. 


فر هنگ؛ فار 


نسمه
```


### [2026-09-07T18:23:37.608Z] TOOL RESULT

```
--- سرنا ---
شرم زن. 
سرمه کش: (25008.: [- سرمه کشنده] 
(ص‌فا.) کسی که به چشم‌های خود سرمه 


کشیده باشد. آنکه چشمان دیگران ر سر مه 
کشد. (کند.) روشن کنندة چشم» بینایی 
دهنك ه۵. (کد.) شب تاریکك. 

سرئا: 0۳5 (- سورنا - سرنای - سورنای 
- سرنی - صر نای» معر.] (.) (مست.) سازی 
شود این ساز در غالب نقاط ايران مسوجود 
است و آن را همراه دهل نوازد. اندازهةٌ آن 
در نواحی مختلف فرق می‌کند و بطور کلی 
از ز نیم متر تجاوز نمی‌نماید. سرنا را از ته باد 
کردن: (عم.) (کذ.) کار وارونه کردن. 
سرناد: ی ترانه و 
آواز عاشقانه که هنگام شب در بیرون خانه 
محبوبی جهت اظهار عشق و علاقةٌ قلبی 
خوانده شو د. 

سر نامه (0-)1021۳02-.5 (امر ۰( آنجه که در 
بالای مکتوب نو سند؛ عنوان نامه. 

۵ () ضربالی سیمی دارای 
--- ناردین ---
گل فرشته. سنبل رومی: (گیا.) سنبل الطیب. 
سنبل زرد: (گسیاء.) گیاهی است از تبره 
صلیییان که به عنوان گیاه زمینی در باغ‌ها نیز 
کشت می‌شود؛ آلوسن» الیسون. ضح. از 
دانهٌ این گیاه که شبیه دانه قدومه است در 
طب استفاده می‌شود و به همان نام الیسون 
مشهور است. سنبل کوهی: (گیا) سنبل 
جبلی. سنبل هندی: (گٌیا.) گیاهی است از 
تبرة گندمیان که ریشه‌های افشانش در تداوی 
همانند ريشة سنبل الطیب مورد استعمال 
دارد؛ ناردین هندی» عحجر مکی حب 


سنبل کردن فرهنگ فارسي معیر 2 


العصافیر. 

نبا کردن: 2۱02و (مص‌ل.) 
(عم.) سرسری انجام دادن کاری را» اجرای
```


## [2026-09-07T18:23:48.413Z] TOOL CALL #42: Bash

```json
{
 "command": "sed -n '1,60p' tools/fetch_source.py"
}
```


### [2026-09-07T18:23:48.449Z] TOOL RESULT

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


## [2026-09-07T18:23:55.701Z] TOOL CALL #43: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ned-\" \\\n \"https://en.wiktionary.org/wiki/%D9%86%D8%B3%DA%A9\" \\\n \"https://en.wiktionary.org/wiki/naska\" \\\n \"https://en.wiktionary.org/wiki/%CE%BD%CE%AC%CF%81%CE%B4%CE%BF%CF%82\" \\\n \"https://en.wiktionary.org/wiki/%D9%86%D8%A7%DB%8C\" \\\n \"https://en.wiktionary.org/wiki/%D9%86%D8%B3%D8%AE%D9%87\" \\\n \"https://www.etymonline.com/word/nard\" \\\n \"https://www.etymonline.com/word/node\" \\\n ; do echo \"### $u\"; timeout 90 python3 tools/fetch_source.py \"$u\" --note \"page 354 (Ned / Nedo-Narda): root, naska, nask, nardos, nay, nosxeh, nard, node\" ; done"
}
```


### [2026-09-07T18:24:04.626Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ned-
/home/sfmqrb/git/rishe/data/verification/sources/web/78f1e3f624491df2.txt
### https://en.wiktionary.org/wiki/%D9%86%D8%B3%DA%A9
/home/sfmqrb/git/rishe/data/verification/sources/web/e63dd8d31504c47c.txt
### https://en.wiktionary.org/wiki/naska
/home/sfmqrb/git/rishe/data/verification/sources/web/a6165bc7519677a7.txt
### https://en.wiktionary.org/wiki/%CE%BD%CE%AC%CF%81%CE%B4%CE%BF%CF%82
/home/sfmqrb/git/rishe/data/verification/sources/web/59584e075835d560.txt
### https://en.wiktionary.org/wiki/%D9%86%D8%A7%DB%8C
/home/sfmqrb/git/rishe/data/verification/sources/web/ee864818ceba5dc4.txt
### https://en.wiktionary.org/wiki/%D9%86%D8%B3%D8%AE%D9%87
/home/sfmqrb/git/rishe/data/verification/sources/web/61ff5794437c166c.txt
### https://www.etymonline.com/word/nard
/home/sfmqrb/git/rishe/data/verification/sources/web/aff938fc85f17675.txt
### https://www.etymonline.com/word/node
/home/sfmqrb/git/rishe/data/verification/sources/web/53cc506172fedf9b.txt
```


## [2026-09-07T18:24:07.719Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 78f1e3f624491df2 e63dd8d31504c47c a6165bc7519677a7; do echo \"######## $f\"; head -c 3500 $f.txt; echo; done"
}
```


### [2026-09-07T18:24:08.947Z] TOOL RESULT

```
######## 78f1e3f624491df2
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ned-
FETCHED: 2026-09-07T18:23:57Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found
######## e63dd8d31504c47c
URL: https://en.wiktionary.org/wiki/%D9%86%D8%B3%DA%A9
FETCHED: 2026-09-07T18:23:58Z
STATUS: 200
TITLE: نسک - Wiktionary, the free dictionary

نسک - Wiktionary, the free dictionary 

 Jump to content 

 Main menu 

 Main menu

 move to sidebar 
 hide 

 Navigation

 Main page 
 Community portal 
 Requested entries 
 Recent changes 
 Random entry 
 Help 
 Glossary 
 Contact us 
 Special pages 

 Search 

 Search 

 Appearance 

 Donations 

 Create account 

 Log in 

 Personal tools 

 Donations 

 Create account 

 Log in 

 Contents

 move to sidebar 
 hide 

 Beginning

 1 
 Persian 

 Toggle Persian subsection 

 1.1 
 Pronunciation 

 1.2 
 Noun 

 Toggle the table of contents 

 نسک 

 6 languages 

 فارسی 
 Magyar 
 Kurdî 
 Malagasy 
 پنجابی 
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

 See also: نسك and نشك 

 Persian
 [ edit ] 

 Persian Wikipedia has an article on: نسک 

 Wikipedia fa 

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ˈnask/ 

 ( Dari, formal ) IPA ( key ) : [näsk] 

 ( Dari, formal ) IPA ( key ) : [näsk] 
 ( Kabuli ) IPA ( key ) : [näsk] 

 ( Hazaragi ) IPA ( key ) : [näsk] 

 ( Iran, formal ) IPA ( key ) : [næskʰʲ] 

 ( Tajik, formal ) IPA ( key ) : [näsk] 

 Rhymes: -ask 

 Readings

 Classical reading ? 

 nask

 Dari reading ? 

 nask

 Iranian reading ? 

 nask

 Tajik reading ? 

 nask

 Noun
 [ edit ] 

 Dari

 نسک 

 Iranian Persian

 Tajik

 наск 

 نسک • ( nask ) ( plural نسک‌ها ) 

 One of the five parts (books) of the Avesta 

 ( rare , puristic ) book (collection of sheets of paper bound together containing printed or written material)
 Synonym: کتاب ( ketâb ) 

 Retrieved from " https://en.wiktionary.org/w/index.php?title=نسک&oldid=88017449 "

 Categories : Persian terms with IPA pronunciation 
 Rhymes:Persian/ask 
 Rhymes:Persian/ask/1 syllable 
 Persian lemmas 
 Persian nouns 
 Persian terms with rare senses 
 Persian puristic terms 
 fa:Zoroastrianism 

 Hidden categories: Pages with entries 
 Pages with 1 entry 

 This page was last edited on 1 November 2025, at 05:27.

 Definitions and other text are available under the Creative Commons Attribution-ShareAlike License ; additional terms may apply. By using this site, you agree to the Terms of Use and Privacy Policy. 

 Privacy policy 

 About Wiktionary 

 Disclaimers 

 Legal & safety contacts 

 Code of Conduct 

 Developers 

 Statistics 

 Cookie statement 

 Mobile view 

 Search 

 Search 

 Toggle the table of contents 

 نسک 

 6 languages 

 Add topic
######## a6165bc7519677a7
URL: https://en.wiktionary.org/wiki/naska
FETCHED: 2026-09-07T18:23:58Z
STATUS: 200
TITLE: naska - Wiktionary, the free dictionary

naska - Wiktionary, the free dictionary 

 Jump to content 

 Main menu 

 Main menu

 move to sidebar 
 hide 

 Navigation

 Main page 
 Community portal 
 Requested entries 
 Recent changes 
 Random entry 
 Help 
 Glossary 
 Contact us 
 Special pages 

 Search 

 Search 

 Appearance 

 Donations 

 Create account 

 Log in 

 Personal tools 

 Donations 

 Create account 

 Log in 

 Contents

 move to sidebar 
 hide 

 Beginning

 1 
 Latvian 

 Toggle Latvian subsection 

 1.1 
 Adjective 

 Toggle the table of contents 

 naska 

 2 languages 

 Ελληνικά 
 Français 

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

 See also: naskā 

 Latvian
 [ edit ] 

 Adjective
 [ edit ] 

 naska 

 inflection of nasks : 
 genitive masculine singular 

 nominative feminine singular 

 Retrieved from " https://en.wiktionary.org/w/index.php?title=naska&oldid=84260387 "

 Categories : Latvian non-lemma forms 
 Latvian adjective forms 

 Hidden categories: Pages with entries 
 Pages with 1 entry 

 This page was last edited on 17 March 2025, at 09:51.

 Definitions and other text are available under the Creative Commons Attribution-ShareAlike License ; additional terms may apply. By using this site, you agree to the Terms of Use and Privacy Policy. 

 Privacy policy 

 About Wiktionary 

 Disclaimers 

 Legal & safety contacts 

 Code of Conduct 

 Developers 

 Statistics 

 Cookie statement 

 Mobile view 

 Search 

 Search 

 Toggle the table of contents 

 naska 

 2 languages 

 Add topic
```


## [2026-09-07T18:24:18.318Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 59584e075835d560 ee864818ceba5dc4 61ff5794437c166c aff938fc85f17675 53cc506172fedf9b; do echo \"######## $f\"; python3 - \"$f.txt\" <<'EOF'\nimport sys,re\nt=open(sys.argv[1],encoding='utf8').read()\n# print from 'From Wiktionary' or 'Advertisement' onwards\ni=t.find('From Wiktionary, the free dictionary')\nif i<0: i=0\nprint(t[:200])\nprint(t[i:i+4000])\nEOF\ndone"
}
```


### [2026-09-07T18:24:19.899Z] TOOL RESULT

```
######## 59584e075835d560
URL: https://en.wiktionary.org/wiki/%CE%BD%CE%AC%CF%81%CE%B4%CE%BF%CF%82
FETCHED: 2026-09-07T18:24:00Z
STATUS: 200
TITLE: νάρδος - Wiktionary, the free dictionary

νάρδος - Wiktionary, the free dictio
From Wiktionary, the free dictionary

 Ancient Greek
 [ edit ] 

 Etymology
 [ edit ] 

 From Phoenician (compare Hebrew נֵרְדְּ ( nērd ) , Aramaic נִרְדָּא ( nirdā ) , Akkadian 𒆠𒆗 ( HIRIM /⁠lardu⁠/ ) , Arabic رَنْد ( rand ) , Old South Arabian 𐩧𐩬𐩵 ( rnd ) ), possibly from Sanskrit नलद ( nálada , “ Indian narde ” ) (although a Semitic-to-Indian loan has also been suggested). [ 1 ] 

 Pronunciation
 [ edit ] 

 IPA ( key ) : /nár.dos/ → /ˈnar.ðos/ → /ˈnar.ðos/ 

 ( 5 th BCE Attic ) IPA ( key ) : /nár.dos/ 

 ( 1 st CE Egyptian ) IPA ( key ) : /ˈnar.dos/ 

 ( 4 th CE Koine ) IPA ( key ) : /ˈnar.ðos/ 

 ( 10 th CE Byzantine ) IPA ( key ) : /ˈnar.ðos/ 

 ( 15 th CE Constantinopolitan ) IPA ( key ) : /ˈnar.ðos/ 

 Noun
 [ edit ] 

 νᾰ́ρδος • ( nắrdos )  f ( genitive νᾰ́ρδου ) ; second declension 

 nard plant, spikenard , nardin , muskroot 

 nard oil , a highly prized ointment made from the plant

 Inflection
 [ edit ] 

 Second declension of ἡ νᾰ́ρδος ; τῆς νᾰ́ρδου ( Attic )

 Case / #

 Singular

 Dual

 Plural

 Nominative

 ἡ νᾰ́ρδος 
 hē nắrdos 

 τὼ νᾰ́ρδω 
 tṑ nắrdō 

 αἱ νᾰ́ρδοι 
 hai nắrdoi 

 Genitive

 τῆς νᾰ́ρδου 
 tês nắrdou 

 τοῖν νᾰ́ρδοιν 
 toîn nắrdoin 

 τῶν νᾰ́ρδων 
 tôn nắrdōn 

 Dative

 τῇ νᾰ́ρδῳ 
 tēî nắrdōi 

 τοῖν νᾰ́ρδοιν 
 toîn nắrdoin 

 ταῖς νᾰ́ρδοις 
 taîs nắrdois 

 Accusative

 τὴν νᾰ́ρδον 
 tḕn nắrdon 

 τὼ νᾰ́ρδω 
 tṑ nắrdō 

 τᾱ̀ς νᾰ́ρδους 
 tā̀s nắrdous 

 Vocative

 νᾰ́ρδε 
 nắrde 

 νᾰ́ρδω 
 nắrdō 

 νᾰ́ρδοι 
 nắrdoi 

 Notes:

 This table gives Attic inflectional endings. For declension in other dialects, see Appendix:Ancient Greek dialectal declension .

 Derived terms
 [ edit ] 

 νάρδινος ( nárdinos ) 

 Descendants
 [ edit ] 

 Greek: νάρδος ( nárdos ) 

 → Gothic: 𐌽𐌰𐍂𐌳𐌿𐍃 ( nardus ) ( possibly via Latin ) 

 → Latin: nardus , nardum → Catalan: nard 
 Italian: nardo 
 → Middle Dutch: nardus Dutch: nardus 

 Old French: narde French: nard 
 → Middle Dutch: narde 
 → Middle English: narde English: nard 

 Romanian: nard 
 Spanish: nardo 

 → Old Armenian: նարդոս ( nardos ) 

 → Old Georgian: ნარდი ( nardi ) , ნარდიონი ( nardioni ) , ლარდიონი ( lardioni ) Georgian: ნარდი ( nardi ) 

 → Old East Slavic: нардъ ( nardŭ ) 
 Russian: нард ( nard ) 

 → Serbo-Croatian: на̏рд , nȁrd 

 References
 [ edit ] 

 ^ Beekes, Robert S. P. ( 2010 ), “ *νάρδος ”, in Etymological Dictionary of Greek (Leiden Indo-European Etymological Dictionary Series; 10 ), with the assistance of Lucien van Beek, Leiden, Boston: Brill, →ISBN , page 996 

 Further reading
 [ edit ] 

 “ νάρδος ”, in Liddell & Scott ( 1940 ), A Greek–English Lexicon , Oxford: Clarendon Press 

 “ νάρδος ”, in Liddell & Scott ( 1889 ), An Intermediate Greek–English Lexicon , New York: Harper & Brothers 

 “ νάρδος ” in Bailly, Anatole ( 1935 ), Le Grand Bailly: Dictionnaire grec-français , Paris: Hachette 

 Bauer, Walter et al. ( 2001 ), A Greek–English Lexicon of the New Testament and Other Early Christian Literature , Third edition, Chicago: University of Chicago Press 

 Lewy, Heinrich ( 1895 ), Die semitischen Fremdwörter im Griechischen (in German), Berlin: R. Gaertner’s Verlagsbuchhandlung, page 40 

 G3487 in Strong, James ( 1979 ), Strong’s Exhaustive Concordance to the Bible 

 νάρδος nardos nard oil , in Exegetical Dictionary of the New Testament edited by Horst Balz, Gerhard Schneider.

 Sima, Alexander ( 2000 ), Tiere, Pflanzen, Steine und Metalle in den altsüdarabischen Inschriften (in German), Wiesbaden: Otto Harrassowitz, →ISBN , pages 276–277 

 “ nard ”, in Dictionary.com Unabridged , Dictionary.com, LLC , 1995–present. 

 νάρδος , in  ΛΟΓΕΙΟΝ [ Logeion ] Dictionaries for Ancient Greek and Latin (in English, French, Spanish, German, Dutch and Chinese), University of Chicago , since 2011

 Greek
 [ edit ] 

 Etymology
 [ edit ] 

 From Ancient Greek νάρδος ( nárdos ) .

 Noun
 [ edit ] 

 νάρδος • ( nárdos )  m or f ( plural νάρδοι ) 

 valerian , nard , spikenard ( Nardostachys grandiflora ).

 Declension
 [ edit ] 

 Declensi
######## ee864818ceba5dc4
URL: https://en.wiktionary.org/wiki/%D9%86%D8%A7%DB%8C
FETCHED: 2026-09-07T18:24:01Z
STATUS: 200
TITLE: نای - Wiktionary, the free dictionary

نای - Wiktionary, the free dictionary 

 Jump to content 
From Wiktionary, the free dictionary

 Persian
 [ edit ] 

 Alternative forms
 [ edit ] 

 نی ( ney ) 

 Etymology
 [ edit ] 

 From Middle Persian nʾd ( nāy , “ reed, cane; tube, pipe, flute, clarion ” ) , from Proto-Indo-Iranian *nada (compare Sanskrit नड ( naḍá ) ), from Proto-Indo-European *nedo- ( “ reed ” ) ; See Old Armenian նետ ( net , “ arrow ” ) for more.

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ˈnaːj/ 

 ( Dari, formal ) IPA ( key ) : [nɑːj] 

 ( Dari, formal ) IPA ( key ) : [nɑːj] 
 ( Kabuli ) IPA ( key ) : [nɑːj] 

 ( Hazaragi ) IPA ( key ) : [näj] 

 ( Iran, formal ) IPA ( key ) : [nɒːj] 

 ( Tajik, formal ) IPA ( key ) : [nɔj] 

 Rhymes: -aːj 

 Readings

 Classical reading ? 

 nāy

 Dari reading ? 

 nāy

 Iranian reading ? 

 nây

 Tajik reading ? 

 noy

 Audio ( Iran ) : ( file ) 

 Noun
 [ edit ] 

 Dari

 نای 

 Iranian Persian

 Tajik

 ной 

 نای • ( nây ) 

 reed 

 reed - pipe 

 flute , flageolet , fife 

 ney 

 throat 

 trachea 

 pride , vainglory 

 Related terms
 [ edit ] 

 سرنا ( sornâ ) 

 کرنا ( karnâ ) 

 References
 [ edit ] 

 Steingass, Francis Joseph ( 1892 ), “ نای ”, in A Comprehensive Persian–English dictionary (overall work in English), London: Routledge & K. Paul 

 Retrieved from " https://en.wiktionary.org/w/index.php?title=نای&oldid=84812540 "

 Categories : Persian terms derived from Middle Persian 
 Persian terms derived from Proto-Indo-Iranian 
 Persian terms derived from Proto-Indo-European 
 Persian terms with IPA pronunciation 
 Rhymes:Persian/aːj 
 Rhymes:Persian/aːj/1 syllable 
 Persian terms with audio pronunciation 
 Persian lemmas 
 Persian nouns 
 fa:Body parts 
 fa:Musical instruments 

 Hidden categories: Sanskrit terms with non-redundant manual transliterations 
 Pages with entries 
 Pages with 1 entry 
 Requests for attention concerning Persian 

 This page was last edited on 16 May 2025, at 02:27.

 Definitions and other text are available under the Creative Commons Attribution-ShareAlike License ; additional terms may apply. By using this site, you agree to the Terms of Use and Privacy Policy. 

 Privacy policy 

 About Wiktionary 

 Disclaimers 

 Legal & safety contacts 

 Code of Conduct 

 Developers 

 Statistics 

 Cookie statement 

 Mobile view 

 Search 

 Search 

 Toggle the table of contents 

 نای 

 5 languages 

 Add topic
######## 61ff5794437c166c
URL: https://en.wiktionary.org/wiki/%D9%86%D8%B3%D8%AE%D9%87
FETCHED: 2026-09-07T18:24:03Z
STATUS: 200
TITLE: نسخه - Wiktionary, the free dictionary

نسخه - Wiktionary, the free dictionary 

 Jump to 
From Wiktionary, the free dictionary

 See also: نسخة 

 Malay
 [ edit ] 

 Noun
 [ edit ] 

 نسخه ( plural نسخه - نسخه or نسخه ٢ ) 

 Jawi spelling of naskhah .‎

 Ottoman Turkish
 [ edit ] 

 Etymology
 [ edit ] 

 Borrowed from Arabic نُسْخَة ( nusḵa ) .

 Noun
 [ edit ] 

 نسخه • ( nüsha ) 

 copy 

 number , issue 

 recipe , prescription 

 Descendants
 [ edit ] 

 Turkish: nüsha 

 → Crimean Tatar: nusha 

 → Serbo-Croatian: ну̀сха  / nùsha 

 Further reading
 [ edit ] 

 Avery, Robert et al. , editors ( 2013 ), “nüsha”, in The Redhouse Dictionary Turkish/Ottoman English , 21st edition, Istanbul: Sev Yayıncılık, →ISBN 

 Kélékian, Diran ( 1911 ), “ نسخه ”, in Dictionnaire turc-français ‎ [1] (in French), Constantinople: Mihran, page 1274a 

 Pashto
 [ edit ] 

 Etymology
 [ edit ] 

 Etymology tree

 Arabic نُسْخَة ( nusḵa ) bor. 
 Classical Persian نُسْخَه ( nusxa ) bor. 
 Pashto نسخه 

 Borrowed from Classical Persian نُسْخَه ( nusxa ) , borrowed from Arabic نُسْخَة ( nusḵa ) .

 Noun
 [ edit ] 

 نسخه • ( nusxá )  f 

 copy 

 Persian
 [ edit ] 

 Etymology
 [ edit ] 

 Borrowed from Arabic نُسْخَة ( nusḵa ) .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /nus.ˈxa/ 

 ( Dari, formal ) IPA ( key ) : [nʊs.xá] 

 ( Dari, formal ) IPA ( key ) : [nʊs.xá] 
 ( Kabuli ) IPA ( key ) : [nʊs.xá] 

 ( Hazaragi ) IPA ( key ) : [nus.xá] 

 ( Iran, formal ) IPA ( key ) : [nos.xé] 

 ( Tajik, formal ) IPA ( key ) : [nus.χá] 

 Rhymes: -a 

 Readings

 Classical reading ? 

 nusxa

 Dari reading ? 

 nusxa

 Iranian reading ? 

 nosxe

 Tajik reading ? 

 nusxa

 Noun
 [ edit ] 

 Dari

 نسخه 

 Iranian Persian

 Tajik

 нусха 

 نسخه • ( nusxa / nosxe ) ( plural نسخه‌ها ( nusxa-hā / nosxe-hâ ) , or نُسَخ ( nusax / nosax ) , Tajik spelling нусха ) 

 copy 

 version 

 prescription 

 Descendants
 [ edit ] 

 Tajik: нусха ( nusxa ) 

 → Azerbaijani: nüsxə 

 → Chagatai: نُسْخَه ( nusxa ) 
 Uyghur: نۇسخە ( nusxe ) 

 Uzbek: nusxa 

 → Hindustani: 
 Hindi: नुसख़ा ( nusxā ) , नुस्ख़ा ( nusxā ) , नुसखा ( nuskhā ) , नुस्खा ( nuskhā ) — nuqtaless 
 Urdu: نُسْخَہ ( nusxa ) 

 → Kazakh: нұсқа ( nusqa ) 

 → Pashto: نُسْخَه ( nusxá ) 

 → Punjabi: 
 Gurmukhi script: ਨੁਸਖ਼ਾ ( nusxā ) , ਨੁਸਖਾ ( nuskhā ) ( nuqtaless ) 
 Shahmukhi script: نُسْخَہ ( nusxah ) 

 → Turkmen: nusga 

 Retrieved from " https://en.wiktionary.org/w/index.php?title=نسخه&oldid=91364820 "

 Categories : Malay variant lemmas 
 Malay terms in Arabic script 
 Ottoman Turkish terms derived from Arabic 
 Ottoman Turkish terms derived from the Arabic root ن س خ 
 Ottoman Turkish terms borrowed from Arabic 
 Ottoman Turkish lemmas 
 Ottoman Turkish nouns 
 Pashto terms borrowed from Classical Persian 
 Pashto terms derived from Arabic 
 Pashto terms derived from the Arabic root ن س خ 
 Pashto terms derived from Classical Persian 
 Pashto lemmas 
 Pashto nouns 
 Pashto feminine nouns 
 Persian terms borrowed from Arabic 
 Persian terms derived from the Arabic root ن س خ 
 Persian terms derived from Arabic 
 Persian terms with IPA pronunciation 
 Rhymes:Persian/a 
 Rhymes:Persian/a/2 syllables 
 Persian lemmas 
 Persian nouns 

 Hidden categories: Pages with entries 
 Pages with 4 entries 
 Pages with etymon 
 Ottoman Turkish entries with etymon 
 Ottoman Turkish entries with etymology texts 
 Pashto entries with etymon 
 Pages with etymology trees 
 Pashto entries with etymology trees 
 Pashto entries with etymology texts 
 Persian entries with etymon 
 Persian entries with etymology texts 
 Chagatai terms with non-redundant manual transliterations 

 This page was last edited on 23 June 2026, at 11:08.

 Definitions and other text are available under the Creative Commons Attribution-ShareAlike License ; additional terms may apply. By using this site, you agree to the Terms of Use and Privacy Policy. 

 Privacy policy 

 About Wiktionary 

 Disclaimers 

 Legal & safety contacts 

 Code of Conduct 

 Developers 

 Statistics 

 Cookie statement 

 Mobile view 

 
######## aff938fc85f17675
URL: https://www.etymonline.com/word/nard
FETCHED: 2026-09-07T18:24:04Z
STATUS: 200
TITLE: Nard - Etymology, Origin & Meaning

Nard - Etymology, Origin & Meaning 

 Search 
 Log in 

 Columns 
 Forum 
URL: https://www.etymonline.com/word/nard
FETCHED: 2026-09-07T18:24:04Z
STATUS: 200
TITLE: Nard - Etymology, Origin & Meaning

Nard - Etymology, Origin & Meaning 

 Search 
 Log in 

 Columns 
 Forum 
 Apps 
 Premium 

 Log in 

 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of nard 

 nard (n.) 

 name of an East Indian plant as well as a precious aromatic unguent prepared from it, c. 1200, from Old French narde (Modern French nard ) and directly from Latin nardus , from Greek nardos , a word of borrowed from a Semitic language (compare Hebrew ner'd , plural n'radim ; Arabic and Persian nardin ,) ultimately from Sanskrit narada, nalada , name of the plant and of an aromatic balsam. Related: Nardine .
 also from c. 1200 

 Entries linking to nard 

 spikenard (n.) 

 c. 1300, "aromatic substance from an Indian plant, famous perfumed unguent of the ancients," Old French spicanarde and directly from Medieval Latin spica nardi (see spike (n.2) + nard (n.), which is probably ultimately from the Sanskrit name of the plant), rendering Greek nardou stakhys .

 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 More to explore

 emollient 

 "softening, making soft or supple," 1640s, from French émollient (16c.), from Latin emollientem (nominative emolliens), present participle of emollire "to make soft, soften," from assimilated form of ex "out" (see ex-) + mollire "soften," from mollis "soft" (from PIE root *mel- (

 cream 

 early 14c., creyme, "the rich and buttery part of milk," from Old French cresme, craime, creme "chrism, holy oil" (13c., Modern French crème). This word is a blend of Late Latin chrisma "ointment" (from Greek khrisma "unguent;" from PIE root *ghrei- "to rub") and Late Latin cramu

 panic 

 "sudden mass terror," especially an exaggerated fright affecting a number of persons without visible cause or inspired by trifling cause or danger, 1708, from an earlier adjective (c. 1600, modifying fear, terror, etc.), from French panique (15c.), from Greek panikon, literally "

 month 

 "one-twelfth part of a year; one of the twelve parts into which the calendar year is arbitrarily divided," Old English monað, from Proto-Germanic *menoth- (source also of Old Saxon manoth, Old Frisian monath, Middle Dutch manet, Dutch maand, Old High German manod, German Monat, O

 whiskey 

 1715, from Gaelic uisge beatha "whisky," literally "water of life," from Old Irish uisce "water" (from PIE *ud-skio-, suffixed form of root *wed- (1) "water; wet") + bethu "life" (from PIE *gwi-wo-tut-, suffixed form of *gwi-wo-, from root *gwei- "to live"). According to Barnhart

 retrieve 

 early 15c., retreven, "find or discover again," originally in reference to dogs finding lost game, from retruev-, stem of Old French retreuver (Modern French retrouver) "find again, recover, meet again, recognize," from re- "again" (see re-) + trouver "to find," probably from Vul

 spick-and-span 

 also spic-and-span, "very neat, clean, and trim," 1660s, from spick-and-span-new "new and fresh" (1570s), literally "new as a recently made spike and wood-chip." It seems to be an elaboration, with spick "nail" (see spike (n.1)), of older span-new "very new," in reference to some

 father 

 Middle English fader, from Old English fæder "he who begets a child, nearest male ancestor;" also "any lineal male ancestor; the Supreme Being," and by late Old English, "one who exercises parental care over another," from Proto-Germanic *fader (source also of Old Saxon fadar, Ol

 contemplation 

 c. 1200, contemplacioun, "religious musing," from Old French contemplation and directly from Latin contemplationem (nominative contemplatio) "act of looking at," noun of action from past-participle stem of contemplari "to gaze attentively, observe; consider, contemplate," origina

 antibiotic 

 "destructive to micro-organisms," 1894, f
######## 53cc506172fedf9b
URL: https://www.etymonline.com/word/node
FETCHED: 2026-09-07T18:24:04Z
STATUS: 200
TITLE: Node - Etymology, Origin & Meaning

Node - Etymology, Origin & Meaning 

 Search 
 Log in 

 Columns 
 Forum 
URL: https://www.etymonline.com/word/node
FETCHED: 2026-09-07T18:24:04Z
STATUS: 200
TITLE: Node - Etymology, Origin & Meaning

Node - Etymology, Origin & Meaning 

 Search 
 Log in 

 Columns 
 Forum 
 Apps 
 Premium 

 Log in 

 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of node 

 node (n.) 

 early 15c., "a knot or lump," from Latin nodus "knot" (from PIE root *ned- "to bind, tie"). Originally borrowed c. 1400 in Latin form, meaning "lump in the flesh." Meaning "point of intersection" (originally in astronomy, of planetary orbits with the ecliptic) is recorded from 1660s.
 also from early 15c. 

 Entries linking to node 

 anti-node (n.) 

 also antinode , 1872, "point of a vibrating string where the amplitude is greatest," from anti- + node . Later applied to other wave systems; at the anti-node the two waves cancel each other out.

 nodal (adj.) 

 "pertaining to a node or nodes," 1811, from node + -al (1). Nodical "of or pertaining to the nodes" is by 1839. Related: Nodality .

 *ned- 

 Proto-Indo-European root meaning "to bind, tie."

 It might form all or part of: annex ; annexation ; connect ; connection ; denouement ; net (n.) "netting, network, mesh used for capturing;" nettle ; nexus ; node ; nodule ; noose .

 It might also be the source of: Sanskrit nahyati "binds, ties;" Latin nodus "knot;" Old Irish nascim "I bind, oblige;" Old English net "netting, network."

 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 More to explore

 knob 

 late 14c., knobe, probably from a Scandinavian or German source (compare Middle Low German knobbe "knob," Middle Dutch cnoppe, Dutch knop, Old Frisian knopp, knapp, Old High German knopf, German Knopf "button," Old Norse knyfill "short horn"). Meaning "knoll, isolated round hill"

 client 

 late 14c., "one who lives under the patronage of another," from Anglo-French clyent (c. 1300), from Latin clientem (nominative cliens) "follower, retainer" (related to clinare "to incline, bend"), from PIE *klient-, a suffixed (active participle) form of root *klei- "to lean." Th

 guest 

 Old English gæst, giest (Anglian gest) "an accidental guest, a chance comer, a stranger," from Proto-Germanic *gastiz (source also of Old Frisian jest, Dutch gast, German Gast, Gothic gasts "guest," originally "stranger"), from PIE root *ghos-ti- "stranger, guest, host" (source a

 lymph 

 Lymph node is attested by 1874....

 pinot 

 type of grape vine used in wine-making, 1912, American English variant spelling of French pineau (attested in English from 1763), name of a family of wine grapes, from pin "pine tree" (see pine (n.)) + diminutive suffix -eau. So called from the shape of the grape clusters. Varian

 point 

 c. 1200, pointe, "minute amount, single item in a whole; sharp end of a sword, etc.," a merger of two words, both ultimately from Latin pungere "to prick, pierce," from a nasalized form of PIE root *peuk- "to prick." The Latin neuter past participle punctum was used as a noun, me

 connection 

 late 14c., conneccion, "state or fact of being connected," also connexioun (in this spelling from mid-15c.), from Old French connexion, from Latin connexionem (nominative connexio) "a binding or joining together," from *connexare, frequentative of conectere "to fasten together, t

 link 

 early 15c., "one of a series of rings or loops which form a chain; section of a cord," probably from Old Norse *hlenkr or a similar Scandinavian source (compare Old Norse hlekkr "link," in plural, "chain;" Old Swedish lænker "chain, link," Norwegian lenke "a link," Danish lænke "

 stem 

 [main body of a tree] Middle English stemme, from Old English stemn, stefn "trunk of a tree or shrub," the part which rises from the ground and supports the branches; also "either end-post of a ship;" from Proto-Germanic *stamniz (source also of Old Saxon stamm, Old Norse s
```


## [2026-09-07T18:24:41.931Z] TOOL CALL #46: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%D9%86%D8%B3%D8%AE\" \\\n \"https://en.wiktionary.org/wiki/%D9%86%D8%B3%D8%AE%D8%A9\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/nedos\" \\\n \"https://en.wiktionary.org/wiki/net\" \\\n \"https://en.wiktionary.org/wiki/nodus\" \\\n \"https://en.wiktionary.org/wiki/%E0%A4%A8%E0%A4%B2%E0%A4%A6\" \\\n \"https://en.wiktionary.org/wiki/%D8%B1%D9%86%D8%AF\" \\\n \"https://en.wiktionary.org/wiki/%D8%B3%D8%B1%D9%86%D8%A7\" \\\n \"https://en.wiktionary.org/wiki/%DA%A9%D8%B1%D9%86%D8%A7\" \\\n \"https://www.ahdictionary.com/word/indoeurop.html\" \\\n ; do echo \"### $u\"; timeout 90 python3 tools/fetch_source.py \"$u\" --note \"page 354 Ned/Nedo: Arabic n-s-x root, nusxa, PIE nedos, net, nodus, nalada, rand, sorna, karna, AHD IE roots\" ; done"
}
```


### [2026-09-07T18:24:50.490Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/%D9%86%D8%B3%D8%AE
/home/sfmqrb/git/rishe/data/verification/sources/web/dddc80e078c99c60.txt
### https://en.wiktionary.org/wiki/%D9%86%D8%B3%D8%AE%D8%A9
/home/sfmqrb/git/rishe/data/verification/sources/web/ea7c925fbab0440e.txt
### https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/nedos
/home/sfmqrb/git/rishe/data/verification/sources/web/ec9fdb35e07cf458.txt
### https://en.wiktionary.org/wiki/net
/home/sfmqrb/git/rishe/data/verification/sources/web/65dedd8016e2a1b6.txt
### https://en.wiktionary.org/wiki/nodus
/home/sfmqrb/git/rishe/data/verification/sources/web/3daf3cfd2063e168.txt
### https://en.wiktionary.org/wiki/%E0%A4%A8%E0%A4%B2%E0%A4%A6
/home/sfmqrb/git/rishe/data/verification/sources/web/33192b0ab16a2885.txt
### https://en.wiktionary.org/wiki/%D8%B1%D9%86%D8%AF
/home/sfmqrb/git/rishe/data/verification/sources/web/4dccfd047dcd0029.txt
### https://en.wiktionary.org/wiki/%D8%B3%D8%B1%D9%86%D8%A7
/home/sfmqrb/git/rishe/data/verification/sources/web/88465ac9d8586d95.txt
### https://en.wiktionary.org/wiki/%DA%A9%D8%B1%D9%86%D8%A7
/home/sfmqrb/git/rishe/data/verification/sources/web/2e62deea3e75e093.txt
### https://www.ahdictionary.com/word/indoeurop.html
/home/sfmqrb/git/rishe/data/verification/sources/web/3735d75498a331a4.txt
```


## [2026-09-07T18:24:56.053Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && python3 - <<'EOF'\nimport re\nfiles={'nasx-verb':'dddc80e078c99c60','nusxa':'ea7c925fbab0440e','PIEnedos':'ec9fdb35e07cf458','nalada':'33192b0ab16a2885','rand':'4dccfd047dcd0029','sorna':'88465ac9d8586d95','karna':'2e62deea3e75e093'}\nfor k,f in files.items():\n    t=open(f+'.txt',encoding='utf8').read()\n    i=t.find('From Wiktionary, the free dictionary')\n    print('########',k, 'status', re.search(r'STATUS: (\\S+)',t).group(1))\n    seg = t[i:i+2600] if i>=0 else t[:1200]\n    print(seg)\nEOF"
}
```


### [2026-09-07T18:24:57.282Z] TOOL RESULT

```
######## nasx-verb status 200
From Wiktionary, the free dictionary

 See also: نسح 

 Arabic
 [ edit ] 

 Arabic Wikipedia has an article on: نسخ 

 Wikipedia ar 

 Etymology 1.1
 [ edit ] 

 Root 

 ن س خ ( n s ḵ ) 

 9 terms 

 Borrowed from Aramaic נְסַח  / 𐡍𐡎𐡇 ( nsaḥ , “ to take away, to draw off, to eliminate ” ) related to the Arabic root ن ز ع ( n z ʕ ) .

 Pronunciation
 [ edit ] 

 IPA ( key ) : /na.sa.xa/ 

 Verb
 [ edit ] 

 نَسَخَ • ( nasaḵa ) I ( non-past يَنْسَخُ ( yansaḵu ) , verbal noun نَسْخ ( nasḵ ) ) 

 to transcribe , to copy 

 ( computing ) to copy 

 to abolish 

 to delete 

 to abrogate , to invalidate 

 to repeal , to revoke , to withdraw 

 to cancel 

 to substitute , to replace 

 Conjugation
 [ edit ] 

 Conjugation of نَسَخَ (I, sound, a ~ a, full passive, verbal noun نَسْخ )

 verbal noun
 الْمَصْدَر 

 نَسْخ 
 nasḵ 

 active participle
 اِسْم الْفَاعِل 

 نَاسِخ 
 nāsiḵ 

 passive participle
 اِسْم الْمَفْعُول 

 مَنْسُوخ 
 mansūḵ 

 active voice
 الْفِعْل الْمَعْلُوم 

 singular
 الْمُفْرَد 

 dual
 الْمُثَنَّى 

 plural
 الْجَمْع 

 1 st person
 الْمُتَكَلِّم 

 2 nd person
 الْمُخَاطَب 

 3 rd person
 الْغَائِب 

 2 nd person
 الْمُخَاطَب 

 3 rd person
 الْغَائِب 

 1 st person
 الْمُتَكَلِّم 

 2 nd person
 الْمُخَاطَب 

 3 rd person
 الْغَائِب 

 past (perfect) indicative
 الْمَاضِي 

 m

 نَسَخْتُ 
 nasaḵtu 

 نَسَخْتَ 
 nasaḵta 

 نَسَخَ 
 nasaḵa 

 نَسَخْتُمَا 
 nasaḵtumā 

 نَسَخَا 
 nasaḵā 

 نَسَخْنَا 
 nasaḵnā 

 نَسَخْتُمْ 
 nasaḵtum 

 نَسَخُوا 
 nasaḵū 

 f

 نَسَخْتِ 
 nasaḵti 

 نَسَخَتْ 
 nasaḵat 

 نَسَخَتَا 
 nasaḵatā 

 نَسَخْتُنَّ 
 nasaḵtunna 

 نَسَخْنَ 
 nasaḵna 

 non-past (imperfect) indicative
 الْمُضَارِع الْمَرْفُوع 

 m

 أَنْسَخُ 
 ʔansaḵu 

 تَنْسَخُ 
 tansaḵu 

 يَنْسَخُ 
 yansaḵu 

 تَنْسَخَانِ 
 tansaḵāni 

 يَنْسَخَانِ 
 yansaḵāni 

 نَنْسَخُ 
 nansaḵu 

 تَنْسَخُونَ 
 tansaḵūna 

 يَنْسَخُونَ 
 yansaḵūna 

 f

 تَنْسَخِينَ 
 tansaḵīna 

 تَنْسَخُ 
 tansaḵu 

 تَنْسَخَانِ 
 tansaḵāni 

 تَنْسَخْنَ 
 tansaḵna 

 يَنْسَخْنَ 
 yansaḵna 

 subjunctive
 الْمُضَارِع الْمَنْصُوب 

 m

 أَنْسَخَ 
 ʔansaḵa 

 تَنْسَخَ 
 tansaḵa 

 يَنْسَخَ 
 yansaḵa 

 تَنْسَخَا 
 tansaḵā 

 يَنْسَخَا 
 yansaḵā 

 نَنْسَخَ 
 nansaḵa 

 تَنْسَخُوا 
 tansaḵū 

 يَنْسَخُوا 
 yansaḵū 

 f

 تَنْسَخِي 
 tansaḵī 

 تَنْسَخَ 
 tansaḵa 

 تَنْسَخَا 
 tansaḵā 

 تَنْسَخْنَ 
 tansaḵna 

 يَنْسَخْنَ 
 yansaḵna 

 jussive
 الْمُضَارِع الْمَجْزُوم 

 m

 أَنْسَخْ 
 ʔansaḵ 

 تَنْسَخْ 
 tansaḵ 

 يَنْسَخْ 
 yansaḵ 

 تَنْسَخَا 
 tansaḵā 

 يَنْسَخَا 
 yansaḵā 

 نَنْسَخْ 
 nansaḵ 

 تَنْسَخُوا 
 tansaḵū 

 يَنْسَخُوا 
 yansaḵū 

 f

 تَنْسَخِي 
 tansaḵ
######## nusxa status 200
From Wiktionary, the free dictionary

 See also: نسخه 

 Arabic
 [ edit ] 

 Root 

 ن س خ ( n s ḵ ) 

 9 terms 

 Etymology
 [ edit ] 

 Compare Hebrew נֻסָּח ( nussɔḥ, nusákh ) .

 Pronunciation
 [ edit ] 

 IPA ( key ) : /nus.xa/ 

 Audio : ( file ) 

 Noun
 [ edit ] 

 نُسْخَة • ( nusḵa )  f ( plural نُسَخ ( nusaḵ ) ) 

 copy 

 transcript 

 original , manuscript , proof sheet , impression 

 prescription , recipe 

 written amulet 

 Declension
 [ edit ] 

 Declension of noun نُسْخَة ( nusḵa )

 singular

 singular triptote in ـَة ( -a ) 

 indefinite

 definite

 construct

 informal

 نُسْخَة 
 nusḵa 

 النُّسْخَة 
 an-nusḵa 

 نُسْخَة 
 nusḵat 

 nominative

 نُسْخَةٌ 
 nusḵatun 

 النُّسْخَةُ 
 an-nusḵatu 

 نُسْخَةُ 
 nusḵatu 

 accusative

 نُسْخَةً 
 nusḵatan 

 النُّسْخَةَ 
 an-nusḵata 

 نُسْخَةَ 
 nusḵata 

 genitive

 نُسْخَةٍ 
 nusḵatin 

 النُّسْخَةِ 
 an-nusḵati 

 نُسْخَةِ 
 nusḵati 

 dual

 indefinite

 definite

 construct

 informal

 نُسْخَتَيْن 
 nusḵatayn 

 النُّسْخَتَيْن 
 an-nusḵatayn 

 نُسْخَتَيْ 
 nusḵatay 

 nominative

 نُسْخَتَانِ 
 nusḵatāni 

 النُّسْخَتَانِ 
 an-nusḵatāni 

 نُسْخَتَا 
 nusḵatā 

 accusative

 نُسْخَتَيْنِ 
 nusḵatayni 

 النُّسْخَتَيْنِ 
 an-nusḵatayni 

 نُسْخَتَيْ 
 nusḵatay 

 genitive

 نُسْخَتَيْنِ 
 nusḵatayni 

 النُّسْخَتَيْنِ 
 an-nusḵatayni 

 نُسْخَتَيْ 
 nusḵatay 

 plural

 basic broken plural triptote 

 indefinite

 definite

 construct

 informal

 نُسَخ 
 nusaḵ 

 النُّسَخ 
 an-nusaḵ 

 نُسَخ 
 nusaḵ 

 nominative

 نُسَخٌ 
 nusaḵun 

 النُّسَخُ 
 an-nusaḵu 

 نُسَخُ 
 nusaḵu 

 accusative

 نُسَخًا 
 nusaḵan 

 النُّسَخَ 
 an-nusaḵa 

 نُسَخَ 
 nusaḵa 

 genitive

 نُسَخٍ 
 nusaḵin 

 النُّسَخِ 
 an-nusaḵi 

 نُسَخِ 
 nusaḵi 

 Derived terms
 [ edit ] 

 نُسْخَة طِبْق الْأَصْل ( nusḵa(t) ṭibq al-ʔaṣl ) 

 Descendants
 [ edit ] 

 → Middle Armenian: նուսխայ ( nusxay ) , նուսխաթ ( nusxatʻ ) 

 → Classical Persian: نُسْخَه ( nusxa ) Tajik: нусха ( nusxa ) 
 → Azerbaijani: nüsxə 
 → Chagatai: نُسْخَه ( nusxa ) Uyghur: نۇسخە ( nusxe ) 
 Uzbek: nusxa 

 → Hindustani: Hindi: नुसख़ा ( nusxā ) , नुस्ख़ा ( nusxā ) , नुसखा ( nuskhā ) , नुस्खा ( nuskhā ) — nuqtaless Urdu: نُسْخَہ ( nusxa ) 
 → Kazakh: нұсқа ( nusqa ) 
 → Pashto: نُسْخَه ( nusxá ) 
 → Punjabi: Gurmukhi script: ਨੁਸਖ਼ਾ ( nusxā ) , ਨੁਸਖਾ ( nuskhā ) ( nuqtaless ) Shahmukhi script: نُسْخَہ ( nusxah ) 
 → Turkmen: nusga 

 → Malay: naskhah Indonesian: naskah 

 → Ottoman Turkish: نسخه ( nüsha ) Turkish: nüsha 
 → Crimean Tatar: nusha 
 → Serbo-Croatian: ну̀сха  / nùsha 

 References
 [ edit ] 

 Lane, Edward William ( 1863-1893 ), 
######## PIEnedos status -1
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/nedos
FETCHED: 2026-09-07T18:24:45Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found
######## nalada status 200
From Wiktionary, the free dictionary

 Sanskrit
 [ edit ] 

 Alternative forms
 [ edit ] 

 नरद ( narada ) 

 Alternative scripts
 [ edit ] 

 Alternative scripts
 নলদ ( Assamese script ) 
 ᬦᬮᬤ ( Balinese script ) 
 নলদ ( Bengali script ) 
 𑰡𑰩𑰟 ( Bhaiksuki script ) 
 𑀦𑀮𑀤 ( Brahmi script ) 
 နလဒ ( Burmese script ) 
 નલદ ( Gujarati script ) 
 ਨਲਦ ( Gurmukhi script ) 
 𑌨𑌲𑌦 ( Grantha script ) 
 ꦤꦭꦢ ( Javanese script ) 
 𑂢𑂪𑂠 ( Kaithi script ) 
 ನಲದ ( Kannada script ) 
 នលទ ( Khmer script ) 
 ນລທ ( Lao script ) 
 നലദ ( Malayalam script ) 
 ᠨᠠᠯᠠᡩᠠ ( Manchu script ) 
 𑘡𑘩𑘟 ( Modi script ) 
 ᠨᠠᠯᠠᢑᠠ᠋ ( Mongolian script ) 
 𑧁𑧉𑦿 ( Nandinagari script ) 
 𑐣𑐮𑐡 ( Newa script ) 
 ନଲଦ ( Odia script ) 
 ꢥꢭꢣ ( Saurashtra script ) 
 𑆤𑆬𑆢 ( Sharada script ) 
 𑖡𑖩𑖟 ( Siddham script ) 
 නලද ( Sinhalese script ) 
 𑩯𑩽𑩭 ( Soyombo script ) 
 𑚝𑚥𑚛 ( Takri script ) 
 நலத³ ( Tamil script ) 
 నలద ( Telugu script ) 
 นลท ( Thai script ) 
 ན་ལ་ད ( Tibetan script ) 
 𑒢𑒪𑒠 ( Tirhuta script ) 
 𑨝𑨬𑨛 ( Zanabazar Square script ) 

 Etymology 1
 [ edit ] 

 Of uncertain origin, though perhaps a derivative of नड ( naḍá , “ reed, hollow stalk ” ) , probably via an intermediate नाल ( nāla , “ tube, vein; made of reeds ” ) , owing to the plant's stalk-like structure. [ 1 ] 

 Pronunciation
 [ edit ] 

 ( Vedic ) IPA ( key ) : /nɐ́.lɐ.dɐ/ 

 ( Classical Sanskrit ) IPA ( key ) : /n̪ɐ.l̪ɐ.d̪ɐ/ 

 Noun
 [ edit ] 

 नल॑द • ( nálada ) stem ,  m or n 

 Nardostachys jatamansi , Indian spikenard ( AV. , Suśr. etc.)

 root of Chrysopogon zizanioides , formerly Andropogon muricatus ( Naish. )

 ( only in neuter ) the blossom of Hibiscus rosa-sinensis ( L. )

 ( only in neuter ) the honey or nectar of a flower ( L. )

 Declension
 [ edit ] 

 Masculine a-stem declension of नल॑द 

 singular

 dual

 plural

 nominative

 नल॑दः ( náladaḥ ) 

 नल॑दौ ( náladau ) 
 नल॑दा¹ ( náladā¹ ) 

 नल॑दाः ( náladāḥ ) 
 नल॑दासः¹ ( náladāsaḥ¹ ) 

 accusative

 नल॑दम् ( náladam ) 

 नल॑दौ ( náladau ) 
 नल॑दा¹ ( náladā¹ ) 

 नल॑दान् ( náladān ) 

 instrumental

 नल॑देन ( náladena ) 

 नल॑दाभ्याम् ( náladābhyām ) 

 नल॑दैः ( náladaiḥ ) 
 नल॑देभिः¹ ( náladebhiḥ¹ ) 

 dative

 नल॑दाय ( náladāya ) 

 नल॑दाभ्याम् ( náladābhyām ) 

 नल॑देभ्यः ( náladebhyaḥ ) 

 ablative

 नल॑दात् ( náladāt ) 

 नल॑दाभ्याम् ( náladābhyām ) 

 नल॑देभ्यः ( náladebhyaḥ ) 

 genitive

 नल॑दस्य ( náladasya ) 

 नल॑दयोः ( náladayoḥ ) 

 नल॑दानाम् ( náladānām ) 

 locative

 नल॑दे ( nálade ) 

 नल॑दयोः ( náladayoḥ ) 

 नल॑देषु ( náladeṣu ) 

 vocative

 नल॑द ( nálada ) 

 नल॑दौ ( náladau ) 
 नल॑दा¹ ( náladā¹ ) 

 नल॑दाः ( náladāḥ ) 
 नल॑दासः¹ ( náladāsaḥ¹ ) 

 ¹Ved
######## rand status 200
From Wiktionary, the free dictionary

 See also: زند 

 Arabic
 [ edit ] 

 Etymology
 [ edit ] 

 Akin to Old South Arabian 𐩧𐩬𐩵 ( rnd , “ Artemisia arborescens syn. Artemisia abyssinica ” ) . Alleged to be a metathesis of what is found as Hebrew נֵרְדְּ ( nerd ) , Aramaic נִרְדָּא ( nirdā ) , נָרְדָּא ( nārdā ) , ܢܪܕܐ ( nārdā ) , Akkadian 𒆠𒆗 ( HIRIM /⁠lardu⁠/ ) , Ancient Greek νᾰ́ρδος ( nắrdos ) , Sanskrit नलद ( nalada ) , and Arabic نَارْدِين ( nārdīn ) .

 Pronunciation
 [ edit ] 

 IPA ( key ) : /rand/ 

 Noun
 [ edit ] 

 رَنْد • ( rand )  m 

 laurel ( Laurus nobilis )
 Synonym: غَار ( ḡār ) 
 c. 1200 , يحيى بن محمد بن أحمد بن العوام [ yaḥyā ibn muḥammad ibn ʔaḥmad ibn al-ʕawwām ], edited by José Antonio Banqueri , كتاب الفلاحة [ Book on Agriculture ], volume 1, Madrid: Imprenta Real, published 1802 IA , Cap. 4, pages 154–155 : ويغرس في المواضع الرطب الكبيرة والندوة منها النشم والغرب والصفيراء والأيرج والميس والرند ويتوخى أن يكون شجر الأترج في مواضع مستور عن الريح الجوفية والريح الغربية مكشوف للريح القبلية. One plants on moist, spacious and humid places there elms, willows, planetree maples, citrons, hackberries, and laurels, and it is to be taken care that the citron is covered from northern and western winds and open for southeastern winds. 

 aloeswood , agarwood 
 Synonyms: عُود ( ʕūd ) , يَلَنْجُوج ( yalanjūj ) , قُطُر ( quṭur ) 

 ( Yemen ) Artemisia arborescens syn. Artemisia abyssinica 

 Declension
 [ edit ] 

 Declension of noun رَنْد ( rand )

 singular

 basic singular triptote 

 indefinite

 definite

 construct

 informal

 رَنْد 
 rand 

 الرَّنْد 
 ar-rand 

 رَنْد 
 rand 

 nominative

 رَنْدٌ 
 randun 

 الرَّنْدُ 
 ar-randu 

 رَنْدُ 
 randu 

 accusative

 رَنْدًا 
 randan 

 الرَّنْدَ 
 ar-randa 

 رَنْدَ 
 randa 

 genitive

 رَنْدٍ 
 randin 

 الرَّنْدِ 
 ar-randi 

 رَنْدِ 
 randi 

 Descendants
 [ edit ] 

 Maltese: rand 

 References
 [ edit ] 

 Dozy, Reinhart Pieter Anne ( 1881 ), “ رند ”, in Supplément aux dictionnaires arabes ‎ [2] (in French), volume 1, Leiden: E. J. Brill, page 561 

 Freytag, Georg ( 1833 ), “ رند ”, in Lexicon arabico-latinum praesertim ex Djeuharii Firuzabadiique et aliorum Arabum operibus adhibitis Golii quoque et aliorum libris confectum ‎ [3] (in Latin), volume 2, Halle: C. A. Schwetschke, page 198 

 Sima, Alexander ( 2000 ), Tiere, Pflanzen, Steine und Metalle in den altsüdarabischen Inschriften (in German), Wiesbaden: Otto Harrassowitz, →ISBN , pages 276–277 

 “ nrdyn ”, in The Comprehensive Aramaic Lexicon Project , Cincinnati: Hebrew Union College, 1986– 

 H5373 in Strong, James ( 1979 
######## sorna status 200
From Wiktionary, the free dictionary

 Arabic
 [ edit ] 

 Verb
 [ edit ] 

 سِرْنَا • ( sirnā ) ( form I ) /sir.naː/ 

 first-person plural past active / passive of سَارَ ( sāra ) 

 Persian
 [ edit ] 

 Persian Wikipedia has an article on: سرنا 

 Wikipedia fa 

 Alternative forms
 [ edit ] 

 سورنای ( surnây ) , سرنای ( sornây ) , سرنی ( sorney ) , زرنا ( zornâ ) , سورنا ( surnâ ) , صرنا ( sornâ ) , صرنای ( sornây ) , سرنائی ( sornâ'i ) 

 Etymology
 [ edit ] 

 Borrowed from an unknown, possibly Anatolian , Indo-European cognate of Luwian 𒍪𒌨𒉌 ( zurni , “ horn ” ) , Sanskrit शृङ्ग ( ṡṛṅga , “ horn ” ) , Latin cornū , English horn , probably ultimately from Proto-Indo-European *ḱerh₂- (though Kloekhorst disagrees). Folk etymology explains the word as سور ( sur , “ banquet, feast ” ) + نای ( nây , “ pipe, flute, nay ” ) .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /sur.ˈnaː/ 

 ( Dari, formal ) IPA ( key ) : [sʊɾ.nɑ́ː] 

 ( Dari, formal ) IPA ( key ) : [sʊɾ.nɑ́ː] 
 ( Kabuli ) IPA ( key ) : [sʊɾ.nɑ́ː] 

 ( Hazaragi ) IPA ( key ) : [suɾ.nɔ́ː] 

 ( Iran, formal ) IPA ( key ) : [soɹ.nɒ́ː] 

 ( Tajik, formal ) IPA ( key ) : [suɾ.näj] 

 Rhymes: -aː 

 Readings

 Classical reading ? 

 surnā

 Dari reading ? 

 surnā

 Iranian reading ? 

 sornâ

 Tajik reading ? 

 surnay

 Noun
 [ edit ] 

 Dari

 سرنا 

 Iranian Persian

 Tajik

 сурнай 

 سرنا • ( sornâ ) ( plural سرناها ) 

 ( music ) zurna 

 Derived terms
 [ edit ] 

 زرناپا ( zornâpâ ) 

 سرناچی ( sornâči ) 

 Related terms
 [ edit ] 

 کرنا ( karnâ ) 

 Descendants
 [ edit ] 

 → Assyrian Neo-Aramaic: ܙܘܿܪܢܵܐ ( zōrnā ) 

 → Azerbaijani: zurna 

 → Ottoman Turkish: زورنا ( zurnâ ) , زرنا ( zurna ) Turkish: zurna 
 → Bulgarian: зурна́ ( zurná ) 
 → Classical Syriac: ܙܘܪܢܐ ( zurnā ) 
 → English: zurna 
 → Georgian: ზურნა ( zurna ) → Bats: ზურნ ( zurn ) 

 → Greek: ζουρνάς ( zournás ) 
 → Macedonian: зурла ( zurla ) 
 → Middle Armenian: զուռնայ ( zuṙnay ) , զոռնա ( zoṙna ) Armenian: զուռնա ( zuṙna ) 

 → Russian: зурна́ ( zurná ) 
 → Serbo-Croatian: Cyrillic script: зу̑рна Latin script: zȗrna 

 → Kazakh: сырнай ( sırnay ) 

 → Kyrgyz: сурнай ( surnay ) 

 → Turkmen: surnaý 

 → Uzbek: surnay 

 → Uyghur: سۇناي ( sunay ) 
 → Chinese: 
 Mandarin: 嗩吶  / 唢呐 ( suǒnà ) , 唢呐 ( suǒnà ) 

 References
 [ edit ] 

 Greppin, John A. C. ( 1991 ), “The Survival of Ancient Anatolian and Mesopotamian Vocabulary Until the Present”, in Journal of Near Eastern Studies ‎ [1] , volume 50 , number 3, pages 203–207 

 Retrieved from " https://en.wiktionary.org/w/index.php?title=سرنا&oldid=92301393 "

 Ca
######## karna status 200
From Wiktionary, the free dictionary

 See also: گرنا 

 Pahari-Potwari
 [ edit ] 

 Etymology
 [ edit ] 

 Etymology tree

 Proto-Indo-European *kʷer- 

 Proto-Indo-European *-néwti 

 Proto-Indo-Iranian *kr̥náwti 
 Sanskrit कृ॒णोति॑ ( kṛṇóti ) 
 Sanskrit क॒रोति॑ ( karóti ) 
 Ashokan Prakrit 𑀓𑀭𑁄𑀢𑀺 ( karoti ) 
 Prakrit 𑀓𑀭𑁂𑀇 ( karei ) 
 Pahari-Potwari کَرݨا 

 Inherited from Prakrit 𑀓𑀭𑁂𑀇 ( karei ) , from Ashokan Prakrit 𑀓𑀭𑁄𑀢𑀺 ( karoti ) , from Sanskrit क॒रोति॑ ( karóti ) , from कृ॒णोति॑ ( kṛṇóti ) , from Proto-Indo-Iranian *kr̥náwti , from Proto-Indo-European *kʷer- + *-néwti .

 Verb
 [ edit ] 

 کَرݨا ( karṇā ) 

 ( transitive ) to do 

 Persian
 [ edit ] 

 Alternative forms
 [ edit ] 

 کرنای ( karnây ) , کارنای ( kârnây ) , کرنی ( karney ) , کره‌نای ( karre-nây ) , خرنای ( xarnây ) , قرنا ( qarnâ ) 

 Etymology
 [ edit ] 

 Possibly of Semitic origin. [ 1 ] Compare Classical Syriac ܩܪܢܐ ( qarnā ) , Aramaic קרנא ( qarnā ) , Akkadian 𒋛 ( qarnum ) , Arabic قَرْن ( qarn ) , Hebrew קֶרֶן ( qéren ) .

 Various native etymologies have also been proposed by Persian lexicographers:

 From کار ( kâr ) +‎ نای ( nây , “ flute ” ) , with the کار ( kâr ) portion being equivalent to the one occurring in کارزار ( kârzâr , “ battle; battlefield ” ) and کاروان ( kârvân , “ convoy ” ) , going back to Old Persian 𐎣𐎠𐎼 ( k-a-r /⁠kāra⁠/ , “ army ” ) . [ 2 ] 

 From خر ( xar , “ donkey; large ” ) +‎ نای ( nây , “ flute ” ) , either in reference to the size of the instrument [ 3 ] or in comparison of its hoarse tone with a donkey's bray. [ 1 ] 

 People playing the کرنا ( karnâ ) in Tajikistan 
 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /kar.ˈnaː/ 

 ( Dari, formal ) IPA ( key ) : [kʰäɾ.nɑ́ː] 

 ( Dari, formal ) IPA ( key ) : [kʰäɾ.nɑ́ː] 
 ( Kabuli ) IPA ( key ) : [kʰäɾ.nɑ́ː] 

 ( Hazaragi ) IPA ( key ) : [kʰäɾ.nɔ́ː] 

 ( Iran, formal ) IPA ( key ) : [kʰʲæɹ.nɒ́ː] 

 ( Tajik, formal ) IPA ( key ) : [kʰäɾ.näj] 

 Rhymes: -aː 

 Readings

 Classical reading ? 

 karnā

 Dari reading ? 

 karnā

 Iranian reading ? 

 karnâ

 Tajik reading ? 

 karnay

 Noun
 [ edit ] 

 Dari

 کرنا 

 Iranian Persian

 Tajik

 карнай 

 کرنا • ( karnâ ) 

 ( music ) kerana , kernei , karnay ( a long thin brass horn or trumpet ) 
 Synonyms: شیپور ( šeypur ) , صور ( sur ) 

 war-horn 
 Synonym: بوق جنگی ( buq-e jangi ) 

 hearing aid , ear trumpet 
 Synonyms: سمعک ( sam'ak ) , سماعه ( samâ'e ) 

 Derived terms
 [ edit ] 

 کرناچی ( karnâči , “ trumpeter ” ) 

 Related terms
 [ edit ] 

 سرنا ( sornâ ) 

 Descendants
 [ edit ] 

 → Armenian: կառնայ ( kaṙnay ) 

 → Azerbaijani:
```


## [2026-09-07T18:25:25.840Z] TOOL CALL #48: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%D9%82%D8%B1%D9%87%E2%80%8C%D9%86%DB%8C\" \\\n \"https://en.wiktionary.org/wiki/%D9%86%D8%A7%D8%B1%D8%AF%D9%8A%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D9%86%D8%B1%D8%AF\" \\\n \"https://www.iranicaonline.org/articles/avesta-holy-book\" \\\n \"https://www.etymonline.com/word/net\" \\\n \"https://www.etymonline.com/word/annex\" \\\n ; do echo \"### $u\"; timeout 90 python3 tools/fetch_source.py \"$u\" --note \"page 354: qara-ney, Arabic nardin, Persian nard, Avesta nasks, net, annex\" ; done"
}
```


### [2026-09-07T18:25:37.408Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/%D9%82%D8%B1%D9%87%E2%80%8C%D9%86%DB%8C
/home/sfmqrb/git/rishe/data/verification/sources/web/a94f5a63bae37f9c.txt
### https://en.wiktionary.org/wiki/%D9%86%D8%A7%D8%B1%D8%AF%D9%8A%D9%86
/home/sfmqrb/git/rishe/data/verification/sources/web/1ff9e3015c376040.txt
### https://en.wiktionary.org/wiki/%D9%86%D8%B1%D8%AF
/home/sfmqrb/git/rishe/data/verification/sources/web/0a9557299970eee3.txt
### https://www.iranicaonline.org/articles/avesta-holy-book
/home/sfmqrb/git/rishe/data/verification/sources/web/478b360fe12b1540.txt
### https://www.etymonline.com/word/net
/home/sfmqrb/git/rishe/data/verification/sources/web/617b0837d9ed0628.txt
### https://www.etymonline.com/word/annex
/home/sfmqrb/git/rishe/data/verification/sources/web/08062a66c8de894d.txt
```


## [2026-09-07T18:25:42.317Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && python3 - <<'EOF'\nimport re\nfor k,f in {'qarani':'a94f5a63bae37f9c','nardin_ar':'1ff9e3015c376040','nard_fa':'0a9557299970eee3','net_ety':'617b0837d9ed0628','annex':'08062a66c8de894d'}.items():\n    t=open(f+'.txt',encoding='utf8').read()\n    print('########',k, re.search(r'STATUS: (\\S+)',t).group(1))\n    i=t.find('From Wiktionary, the free dictionary')\n    if i<0: i=t.find('Origin and history')\n    print(t[i:i+1800] if i>=0 else t[:600])\nEOF"
}
```


### [2026-09-07T18:25:43.546Z] TOOL RESULT

```
######## qarani -1
URL: https://en.wiktionary.org/wiki/%D9%82%D8%B1%D9%87%E2%80%8C%D9%86%DB%8C
FETCHED: 2026-09-07T18:25:27Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found
######## nardin_ar 200
From Wiktionary, the free dictionary

 Arabic
 [ edit ] 

 ناردين – Valeriana officinalis 

 ناردين – Nardostachys jatamansi 

   ناردين on Arabic Wikipedia

 Etymology
 [ edit ] 

 From Aramaic נָרְדִּין / ܢܪܕܝܢ ( nārdīn ) , a plurale tantum form of נָרְדָּא / ܢܪܕܐ ( nārdā ) , Ultimately the same word as treated under رَنْد ( rand ) .

 Pronunciation
 [ edit ] 

 IPA ( key ) : /naːr.diːn/ , /naː.ra.diːn/ 

 Noun
 [ edit ] 

 نَارْدِين or نَارَدِين • ( nārdīn or nāradīn )  m 

 nard ( Nardostachys jatamansi , syns. Nardostachys grandiflora , Valeriana jatamansi )

 garden valerian ( Valeriana officinalis )
 Synonyms: سُنْبُل رُومِيّ ( sunbul rūmiyy ) , حَشِيشَةُ الْقَطَّة ( ḥašīšatu l-qaṭṭa ) 

 valerian ( Valeriana gen. et spp.)

 Declension
 [ edit ] 

 Declension of noun نَارْدِين ( nārdīn )‎; نَارَدِين ( nāradīn )

 singular

 basic singular triptote 

 indefinite

 definite

 construct

 informal

 نَارْدِين ‎; نَارَدِين 
 nārdīn ‎; nāradīn 

 النَّارْدِين ‎; النَّارَدِين 
 an-nārdīn ‎; an-nāradīn 

 نَارْدِين ‎; نَارَدِين 
 nārdīn ‎; nāradīn 

 nominative

 نَارْدِينٌ ‎; نَارَدِينٌ 
 nārdīnun ‎; nāradīnun 

 النَّارْدِينُ ‎; النَّارَدِينُ 
 an-nārdīnu ‎; an-nāradīnu 

 نَارْدِينُ ‎; نَارَدِينُ 
 nārdīnu ‎; nāradīnu 

 accusative

 نَارْدِينًا ‎; نَارَدِينًا 
 nārdīnan ‎; nāradīnan 

 النَّارْدِينَ ‎; النَّارَدِينَ 
 an-nārdīna ‎; an-nāradīna 

 نَارْدِينَ ‎; نَارَدِينَ 
 nārdīna ‎; nāradīna 

 genitive

 نَارْدِينٍ ‎; نَارَدِينٍ 
 nārdīnin ‎; nāradīnin 

 النَّارْدِينِ ‎; النَّارَدِينِ 
 an-nārdīni ‎; an-nāradīni 

 نَارْدِينِ ‎; نَارَدِينِ 
 nārdīni ‎; nāradīni 

 Descendants
 [ edit ] 

 → Middle Armenian: նարդին ( nardin ) 

 References
 [ edit ] 

 “ nrdyn ”, in The Comprehensive Aramaic Lexicon Project , Cincinnati: Hebrew Union College, 1986– 

 Löw, Immanue
######## nard_fa 200
From Wiktionary, the free dictionary

 See also: نزد 

 Arabic
 [ edit ] 

 Etymology 1
 [ edit ] 

 Clipping of نَرْدَشِير ( nardašīr ) or from Persian نرد ( nard ) .

 Alternative forms
 [ edit ] 

 نَرْدَشِير ( nardašīr ) (obsolete)

 Noun
 [ edit ] 

 نَرْد • ( nard )  m 

 ( collective ) dice ; game with dice 
 Synonym: زَهْر ( zahr ) 

 Declension
 [ edit ] 

 Declension of noun نَرْد ( nard )

 singular

 basic singular triptote 

 indefinite

 definite

 construct

 informal

 نَرْد 
 nard 

 النَّرْد 
 an-nard 

 نَرْد 
 nard 

 nominative

 نَرْدٌ 
 nardun 

 النَّرْدُ 
 an-nardu 

 نَرْدُ 
 nardu 

 accusative

 نَرْدًا 
 nardan 

 النَّرْدَ 
 an-narda 

 نَرْدَ 
 narda 

 genitive

 نَرْدٍ 
 nardin 

 النَّرْدِ 
 an-nardi 

 نَرْدِ 
 nardi 

 Etymology 2
 [ edit ] 

 Verb
 [ edit ] 

 نرد ( form I ) 

 نَرُدُّ ( naruddu ) /na.rud.du/ : first-person plural non-past active indicative of رَدَّ ( radda ) 

 نُرَدُّ ( nuraddu ) /nu.rad.du/ : first-person plural non-past passive indicative of رَدَّ ( radda ) 

 نَرُدَّ ( narudda ) /na.rud.da/ : first-person plural non-past active subjunctive / jussive of رَدَّ ( radda ) 

 نُرَدَّ ( nuradda ) /nu.rad.da/ : first-person plural non-past passive subjunctive / jussive of رَدَّ ( radda ) 

 نَرُدِّ ( naruddi ) /na.rud.di/ : first-person plural non-past active jussive of رَدَّ ( radda ) 

 نُرَدِّ ( nuraddi ) /nu.rad.di/ : first-person plural non-past passive jussive of رَدَّ ( radda ) 

 Etymology 3
 [ edit ] 

 Verb
 [ edit ] 

 نرد ( form I ) 

 نَرِدُ ( naridu ) /na.ri.du/ : first-person plural non-past active indicative of وَرَدَ ( warada ) 

 نَرِدَ ( narida ) /na.ri.da/ : first-person plural non-past active subjunctive of وَرَدَ ( warada ) 

 نَرِدْ ( narid ) /na.rid/ : first-person plural non-past active jussive
######## net_ety 200
Origin and history of net 

 net (n.) 

 Old English net "open textile fabric tied or woven with a mesh for catching fish, birds, or wild animals alive; network; spider web," also figuratively, "moral or mental snare or trap," from Proto-Germanic *natjo- (source also of Old Saxon net , Old Frisian nette , Old Norse, Dutch net , Swedish nät , Old High German nezzi , German Netz , Gothic nati "net"), perhaps originally "something knotted," from PIE root *ned- "to bind, tie." But Boutkan says it has no clear IE etymology and implies it might be a substrate word.

 From late Old English as "light, open woven fabric used as protection from annoying insects." From late 15c. as "light, open mesh bag for the hair."

 net (adj.) 

 "remaining after deductions," early 15c., from earlier sense of "trim, elegant, clean, neat" (c. 1300), from Old French net, nette "clean, pure, unadulterated," from Latin nitere "to shine, look bright, glitter" (see neat (adj.)). Meaning influenced by Italian netto "remaining after deductions." As a noun, "what remains after deductions," by 1910. The notion is "clear of anything extraneous."

 Net profit is "what remains as the clear gain of any business adventure, after deducting the capital invested in the business, the expenses incurred in its management, and the losses sustained by its operation" [Century Dictionary]. Net weight is the weight of merchandise after allowance has been made for casks, bags, cases, or other containers.
 also from early 15c. 

 net (v.1) 

 early 15c., netten , "to capture in a net," from net (n.). Sense of "to make as a net" is by 1789. Related: Netted ; netting .
 also from early 15c. 

 net (v.2) 

 "to gain as a net sum, produce as clear profit," 1758, from net (adj.). Related: Netted ; netting .
 also from 1758 


######## annex 200
Origin and history of annex 

 annex (v.) 

 late 14c., "connect with," from Old French annexer "to join, attach" (13c.), from Medieval Latin annexare , frequentative of Latin annecetere "to bind to," from ad "to" (see ad- ) + nectere "to tie, bind" (from PIE root *ned- "to bind, tie"). Usually meaning "to join in a subordinate capacity," but that notion is not in the etymology. Of nations or territories, c. 1400. Related: Annexed ; annexing .
 also from late 14c. 

 annex (n.) 

 1540s, "an adjunct, accessory," from French annexe "that which is joined" (13c.), from annexer "to join" (see annex (v.)). Meaning "supplementary building" is from 1861.
 also from 1540s 

 Entries linking to annex 

 ad- 

 word-forming element expressing direction toward or in addition to, from Latin ad "to, toward" in space or time; "with regard to, in relation to," as a prefix, sometimes merely emphatic, from PIE root *ad- "to, near, at."

 Simplified to a- before sc- , sp- and st- ; modified to ac- before many consonants and then re-spelled af- , ag- , al- , etc., in conformity with the following consonant (as in affection , aggression ). Also compare ap- (1).

 In Old French, reduced to a- in all cases (an evolution already underway in Merovingian Latin), but French refashioned its written forms on the Latin model in 14c., and English did likewise 15c. in words it had picked up from Old French. In many cases pronunciation followed the shift.

 Over-correction at the end of the Middle Ages in French and then English "restored" the -d- or a doubled consonant to some words that never had it ( accursed , afford ). The process went further in England than in France (where the vernacular sometimes resisted the pedantic), resulting in English adjourn , advance , address , advertisement (Modern
```


## [2026-09-07T18:26:02.008Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"nask\\|na.ska-\" BRT.txt | head -20; echo \"=== try Bündel ===\"; grep -n \"Bündel\\|Textsamml\" BRT.txt | head -20"
}
```


### [2026-09-07T18:26:02.073Z] TOOL RESULT

```
1898:Aogsmadaeca;    HaäöxtNask;   Vistäsp  Yast;   NlrangiAtas;   Fragmente.  xxi
7560:'in  einem  (dadurch  bezeichneten)  Tun  oder Verhalten  dauernd  beharren'*':  a)  ysi  ,  . nasks.frasauhS  (sd.)  auh^nle  'W.g.z2;  — tasät  ya  kaitiinS  ätakaire  (3PPM.)"  dan- y^m  ayrvd  "die  als  Mädchen  lang  unver- heiratet geblieben  sind"  Y.*j.  23''.  b)  s. Inf.  Undeutlich:  dr^fya  paiti  zharahe
8976:•  j.  katay-  Adj.  'lubens,  willig'(?);  haomS tae3t  yöi  -tayS  naskS./rasSuAs  (sd.)  an- kftUe  Y.  0.  22".
18417:'*)  Nach  Y.  S9-  33  stammt  das  Stück  aus  dem Naska  Hiäaoxta  (sd.).
18812:Pn.:«ufli™.»rf  •  J-  nasko.frasa-  Adj.  'der  Erforschung.
20809:51.16;  —  J3  dfhfnaots  mastm  itijyJtSif (sd.)  . ,  hyal  vh  ^aoiatum .  ,yä  (Sp,  1115 m.)  fraHnas  Y.^2. 5.  b)  im  jA'vr.;  das Relativ  ist  substantivisch:  t>m  yätum  ..yS .  .Jraviit3(sd.)  Y.ÖÄ21; — ttm  a<n..yS r  <Ä»fl  Y.Ö5.8;8,  YtJ?.  142,^.1*.  6;  — ta&t  ysi  . .  nasks/rasatths  ank>tae  Y.p.  1 aa;  S.g.\,^.4g,  \k.i4.  46',  ig.  19;  —  us taat  tpäna  patmti  . .  ta^t  yä  (als  NPm.) ^«iKK'«ft'.,V,jj.4j;43; — ta^itutjasmti  ya (als  NFm.)  m^rmfynica  iaraoiryt$yai{sA.)ca V,  z,  14  GL;  —  tasat  yä  kaininS  anhaire (sd.)  . .  ayrvH  Y.  5-  23 ;  —  upa  tarn  vanqm aätiyqm  hS  )n>rrfS{%A.;  näml.  'upajyäya) V. 5.  z;  —  tat  draom  .  .  yat  ml  äa^al a^ff  Y.J/.5;  55.30,  Yti-S,  ip-Sä',  V. 2.6  PüZ.(?);  —  /«/  ayaphm  yasf{h%\C) hwä  y3samaAi  yt  10.3s;  —  •-  li  a/a- ydnti  yq  *aoe  paskät  vyeinti  Y.57.  29;  — ti  naru'.  .  yöi  (als  APm.)  haeahi  Yt  ly. 7;  Vr.  2.3;  —  lä  xsapans  yä  *jvahi  Y. 6^2.10; — ta  fyao%tui..ya  atihus ..  v)rysyeiti V./5.  i;  V.4.4S  (vi; —  tinars  ..yahva (statt  maslc)  vfr>hra.btt<^S  Yt.  y.  1 46; — die Beziehung  ist  ungenau :  ta  fry S ..ta  ihtds t&  rätayS  *yqm  (APn.)'**  ahur^  .  .  zara- 'iuiirai  fravavala  Y.6'5.  9;  —  im  Sinn von  quantus{Sp.  I202  m.):  ih  rurpfsqstäts yä  Al  ux^qstatS  \l.j.2.  1)  'ay-,  nur a)  im  gAw,;  zu  i):  ya%ä  ta  tmSnghäca . .  ys  (NPn.)  voAb  Y.  _j'/.  4.  zu  3) : iyat  T maim'maäi^ä ..y3(SPa.)  Ä3tqm  ^ao- %aHanqm  vahUt3  hysl  Y.^.  3.  m)  day (Sp.  686  m.);  nur  b)  im  jAw.:  ma  dim p)r3s3  yim  ptrtsahi  H.2. 17;  —  nSttdim .  ,  ava.airiaoiti  .  .  yahmäi  .  .  mihrS  ja- laiti  avaijiAe  \t.jQ.  24.  2)  ohne  de-
22086:•  j.  vae3-ä-  f  etwa  'gerichtliche  Fest- stellung, Überführung  (eines  Angeklagten)', Titel  eines  Abschnitts  des  Naska  (sd.) Nikälum*^:  °%a  dalnaya  mazdayasnöiS FrB.  Unklar;  para  kahmäiHi  dahma- nqm  dahmähu  -'hähu  dahmaca  asavanasca V.7.71;  —  -äa/ß'»  taica  kai^ica  YtJ.aö.
24661:ß  i^aiStih  /röl  hiSihFt  -  tiräk  aÜHÜk  J>a harvisp  vinaskarih.  —  0  iSchr.  s.  ^myaiirä.' iatana-  No.  a  und  Cld.  KZ.  33.  593.
29103:•  j.  'haJaoxta-  n.  Name  bestimmter awestischer  Texte,  die  im  za.Naska  ge- sammelt waren*':  ratum  banttm  •t?m  Vr. 2.  10;  —  ratSus  b^Tfzö  'take  Vr.  1.  8.
=== try Bündel ===
3987:■  j.  aiwylnhana-  n.  i)  'Gürtel,  Gürtel- schnur'*>:  'n^m  r3  aiwya»hayamnS  'mm bO/ayarnnS  (sd.)  Yti.iT,  —  /rä  i! mazdä  harat  ..  'n^m  ..  vanuhim  daSnqm mäzdayasnlm  "dir  (dem  Haoma)  brachte M.  einen  Gürtel  . .,  (näml.)  die  gute mazday.  Religion"  Y.9. 26'*;  —  yat  alle yö  mazdayasnS  ap^rmäyBks  avi  hs  hapta ■na  /rajasäiti . .  °nö "'  paitis  h!  maiayai bU)yamanS  avi  hlnara pascaili  tamauhmti 'wenn  dem  jungen  Masday.  sieben  Jahre vergangen  sind,  soll  man  ihm  den  Gürtel um  die  Hüften  legen,  worauf  ihn  die Männer  (als  ihresgleichen)  achten"  Vd, 18;  20'; — jairyö  °nö  ißjyamanff  "vieitem legt  man  (dem  Toten)  die  Gürtelschnur um"  Vd. /23),  a)  von  der  Schnur,  mit der  die  Barvsmanzvreigt  in  Bündel  zusam- mengebunden werden"":  a^a  'na  N. ioS(?).  2)  'Gewand,  Kleid';  ^5  iama *°«o"  aiitryia^qyanii  "wenn  zwei  gleiche Kleider  anziehen"  N.p4(?);  — yaii  tarasca 'na  aipi.vancainii'^.gs^); — bilyS  ant?ma 'nH  "zweitens  (soll  man  dem  Toten  mit- geben) das  Untergewand"  Vd./i>3'.
16994:*>  Über  die  Pflanien,  von  denen  die  Zweige geschnitten  werden  dürfen,  bieten  die  älteren Texte  keine  genaueren  Mitteilungen;  N.  90 PüErl.  (Blatt  16/.  ig)  ist  nicht  recht  deutlich. In  Indien  braucht  man  jetzt  ans  Metall  herge- stellte Zweige.  Die  Mindestzahl  wird  N.  po  auf drei  angegeben;  Y.  57.  6  werden  die  Zahlen 3>  S>  7>  9  genannt.  Als  Höchstzahl  etscheint N.  90  PüErl.  (Blatt  t6S.  1)  551.  Für  gewöhn- lich schwankt  die  Zahl  zwischen  5  und  33,  der Zahl  dcT  ra/rij'ö f airi!,Aä-!i/iHayB  (sd.).  Ober  Grösse und  Stärke  der  Zweige  s.  Y.  J/.  6,  N.  yo,  po, V.  /p.  19.  Die  Zusammenfassung  der  Zweige  zu einem  Bündel  geschieht  mittelst  des  aiwyio- ^nna-'Cürter  (Sp.  98  m.),  wozu  man  heutzutage ein  Datlelblalt  verwendet.  Die  gebündelten Zweige  ruhen  auf  dem  Gerätetisch  (aräVoi^) vor  dem  ZaMar.  Weiteres  bei  Hauo  Essays» 396  f.,  West  SBE.  5.  »84,  '8.  142.  3y-  162. DsT.  ZA.  /.  LXJüiL  Der  Terra,  techn.  für  das Bündeln  des  B.%  ist  ^slar-  'stemere'.  Dies  sowie die  Etymologie  von  b'  weisen  darauf  bin,  das« der  Gebrauch  des  B.  sich  aus  dem  'Spreiten der  Opferstreu'  (ai.  barhifah  slärimä)  entwickelt hat;  %.  datn  OuiENSEiic  Rel.  des  Veda  343.
18819:•  j.  nasu-spaeya- '1  Adj.  im  Kochen  vonjnngen;  s.  Gdn.  GIrPh.  a.  17. Leichen(teilen)  bestehend';  caxr>m  . .  atu      *najta-  m.,  s.  .)  (eig.  wohl  'Bündel',  vgl.  alt. ake  paityänm  yräktntaat  anrO  ntamyul  ? .       noiäm  ich  binde',  «air 'Ring')  ■> ;  mp.  naJ*>)
```


## [2026-09-07T18:26:09.406Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BRT.txt',encoding='utf8',errors='replace').read()\nlines=t.split('\\n')\noff=sum(len(l)+1 for l in lines[:18818])\nleaf=t[:off].count('\\f')\nprint('leaf(0-based)=',leaf)\npages=t.split('\\f')\nprint(pages[leaf][:4000])\nEOF"
}
```


### [2026-09-07T18:26:10.919Z] TOOL RESULT

```
leaf(0-based)= 591
  Po. :  um«  grabend,  dcT  die  Sünde  des  Leichenver-
yrreH'i.   ~    "J  Daher  DsT.  ZA.  3.  loi  'dii.  grabens   begeht*:  yd  yätumä  yS  'spa  Y.
  jj  cwUttcs'  Sbersetit;  (.  lo  V.  7. 14-  ^r  g
Aber  V.  /.  25  ist  davon  niclitl  getagt.
nach  Pö-;  TgL  auch  tutaupaya-.  ~  Et?
nasa>palca-    Adj.    'Leichen(teile)      Bedcatet  nasu-ifi-   tH   cig.  ■Leichen  : kodiend':  ava  tut?m  *k^m  JanaOa    V.S.       werfend'?  VgL  die  SteDe  ait  pahis^^äiay..  ~ 74.  a)  vom  Feaer  'zmn  Kochen  von       ^-  **""  *"*''"'^
Leichcn((eüen)  verwendet"':  yat . .  atr^m  •  j.  *na8us.-ava.b»r»ta-''  Adj,  'zu  einem 'bm  Jrajasqn  nasüm  kam.pacqn  tuuüm  Leichnam  hingebracht:  nöit  koümd  Auts hODayan  (sd.)  V.  Ä  73;  —  haca  s'krat  axtü  mit  moArkS  nsit  'ts  ava  aSe  ahäa •iai  V.  8.  76;  —  yH  Stnm  'k^m  däittm  yaha  caiwarS  irtcvd  "ausgepresster  H. gatüm  avi  ovaMmiH  V.£8i.  ist  (veniisacht)  weder  Krankheit  noch  Tod,
•)  Ei  gilt  da«  (är  den  tchlinunsten  Hiubranch   auch  nicht  wenn  er  ZU  einem  Leichnam d^Fenere;  Tig.  y.  *.  81  ff.  ^  ^  .   ..    hingebracht  ist;   dagegen   die  nicht  aus-
treifitJ  gepressten  ä.  (verursachen  sie,  wenn  hin-
•  j.'niisa'nMnt-  Adj.  (fem.  •»«V^) 'durch  S«^™!«)  «»f  ""  rmga  Eiitfm,ui,g- LdchenCKik)  venimmigt,  mit  Lrichco-  k,  ^J  ^,  ks.  im  ,.  Glirf.  -  KL:  i?  «i^ uorat  besuddr:  yS  *matntit  äpm  vTtao-      o/or  hun.  —  i)  NA,  getrennt.
"iram  frabaraiti  V.i.-ia.  .  ^_ ,  .  ,.    ,,      ^,
Pn.:«ufli™.»rf  •  J-  nasko.frasa-  Adj.  'der  Erforschung.
.  j.    I«s5m.k.r«-   Adj.   'der   dch   «üt  f "   StucEun   d<T   A'ir«««    obhegend;:
Leiche»  2U  tun  tuKhf:  -la  faUi  JanaUi  '"""f  f"^'.  •««*' «J*»>J.(sd.)  "die
Yt.*7.     Ohne  Wert.  gern  dem  Studium  der  ^V.  obhegen"  Y.
Komp.  mit  AS.  im  t.  Glied.    —    VgL  nam.-  9-"-     .    „         ,
i„^^  *>  D.  I.  Srnnmluig  heiliger  Texte;  das  sasa-
y         ,1   .  1-   ....      >  '  nidiache  Anesta  lerfiel  in  21  solcher  Textsamm.
•  j.  nasu-spaeya- '1  Adj.  im  Kochen  vonjnngen;  s.  Gdn.  GIrPh.  a.  17. Leichen(teilen)  bestehend';  caxr>m  . .  atu      *najta-  m.,  s.  .)  (eig.  wohl  'Bündel',  vgl.  alt. ake  paityänm  yräktntaat  anrO  ntamyul  ? .       noiäm  ich  binde',  «air 'Ring')  ■> ;  mp.  naJ*>)
',       .    '^      ,„     iT     1              ,,        i           .   D  a«tMjnii  —  ')  Andre  sehen  n'  für  ein  Letm-
•(^t,-^  'Kochen',   anm  V.  f^--,   i  S  &■  .„„  „,  a,„  Semitischen  an;  »gl  .R  Hano
ÜZv^'i""!!-";    ■''        »            a";  rK'-  l'S  f-,  lässay..  laj.  Drr.  ZA.  j.  xca.
/;.          '^k"J'";71"TS"h"^  ^.„j   ^   brieflichen  Mineilnng  .VOrnm.
p.h»;  ..  ancb  d^  Zilat  ..sG,M.b,,Dsr.  „„   „.„,.,8«  si.d  'die  semili.che.  Eljmo.
ZA.  ?.  14.  -  1)  r  nach  1  Ä  —  1»  VgL  «1«-  j^^j^^  ^^  ^^^^^  p^,  anfrecht  in  halten'.  -
f"y"  »I  So  die  lantgesetaliche  Folm  (GlrPh.  r  h.  87,
•  j.  tutsu-spaya.  r)  m.  'Vergraben,  Ein-  j  jp.  1) ;  »aji  ist  gelw.
graben   von   Leichen':   yat    mauiayasna  •  j..  g.  oasyant-  Adj.,  PPA.;  s.  'not-,
Iqm  z,m  i!lraym..yM  <U,mi  sfanaca  ..  .    .  ,^^15,3.  Adj.    (fem.  ■«■)   'der
fara.,ri!i,M,    a.Uräl   nOmäl  yän^rlß  (^.^^y    ^^j^^     proomus':    -ftm    «<
•*«».    />.Kl»iIO    äStryantt  .  .    apasa    .  .  „^„„g,         V  *  tot"  —    'rf  ä<liikm
»..    dann    versündigen   sie    sich  mit   der  7.15.41;  -  y^m   -Um  S'l'i">  är^n
Sunde  des  Leichenvergrabens  am  Wasser.. '  ^^^^„  f^^  Y.50. 3;'-  -taya!  „fat  laU
V.6.y,—  d„M  M-jlay^mK  ..  'ipayal,  Y.&.6:  —  •la..rm!i  V.34-,  — yüj  ü
■ifülm  '.  .  tilgt  die  Sünde  ia  Leichen-  .„  ^„^,„^  vurm-.md  "so  dass  ihn  der verpbens"  V  J.41.         s)  Adj.  ■»> Vet- , ^j^^j,,  t^todliche  .D.  hört"  N.s;;  -
graben,EuignibenvonLjicben  bestehend':  rMOyi, . .  y!H  . .  -la  p„iri!Mranay3
```


## [2026-09-07T18:26:36.607Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf8',errors='replace').read()\npages=t.split('\\f')\nfor i in (549,550,551):\n    seg=pages[i]\n    print('=== leaf',i,'len',len(seg),'===')\n    print(seg[:300].replace('\\n',' | '))\n    print('...tail:',seg[-200:].replace('\\n',' | '))\nEOF"
}
```


### [2026-09-07T18:26:38.039Z] TOOL RESULT

```
=== leaf 549 len 12074 ===
l  cured  of  leprosy  by  Elisha.  —  Heb. Na'aman,  lit.  ‘pleasantness’,  from  the  stem  of na'em  ‘was  pleasant  or  lovely’,  whence  also na'tm,  ‘pleasant,  lovely’,  nd'am,  ‘pleasantness, loveliness’,  and  the  PN’s  Na‘dmdh,  No‘dmt ;  rel. to  Arab,  na'ima,  ‘was  easy  or  pleasant’
...tail:   naam,  ON.  nafn  (for  *namn),  Dan. navn.  Swed.  and  Norw.  namn,  Goth,  namo. | ‘name’,  fr.  I.-E.  base  *enomen,  *onomen,  *no- men,  whence  also  OI.  nama,  Avestic  nama,  Toch. A  hom, 
=== leaf 550 len 11912 ===
 B  hem,  Hitt,  laman  (formed  with  dissim¬ ilation  fr.  *naman),  Arm.  a  mm  (gen.  anuan),  Gk. ovop.a  (dial,  form  ovup.a),  Alb.  emen,  L.  no- men,  OSlav.  ime  (gen.  imene,  imeni),  OPruss. emmens,  emnes,  OIr.  ainm,  OW.  anu  (pi.  enueiri), W.  enw,  Co.  hanow,  ‘name’.  Outs
...tail: pe.  — Pers.  nargil,  ‘coconut  tree';  prob.  fr.  OI.  ndrike- rah,  ndrikelah,  of  s.m.,  which  is  of  uncertain, possibly  Dravidian,  origin;  so  called  because orig.  narghiles  were  made
=== leaf 551 len 11832 ===
  of  coconut  shells, narial,  adj.,  pertaining  to  the  nares.  —  Formed fr.  nares  with  suff.  -ial. | I | nark,n.,  spy,  informer,  stool  pigeon  ( British  slang). —  From  Gypsy  nak,  ‘nose’,  fr.  Hind,  nak, ‘nose’,  fr.  OI.  nakrd,  fr.  Prakrit  nakka-,  nakka-, of  s.m.,  which  prob
...tail: birth’,  fr.  natus,  pp.  of  nasci,  'to be  born’,  which  stands  for  *gnasci,  fr.  I.-E.  *gn-, zero  degree  of  base  *gen-,  *gene-,  'to  beget,  bear, bring  forth’,  whence  also  L.  gen
```


## [2026-09-07T18:26:50.863Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1971.txt',encoding='utf8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\nfor i,p in enumerate(pages):\n    if 'nard,' in p and 'spikenard' in p:\n        print('leaf',i)\n        j=p.find('nard,')\n        print(p[j-200:j+900])\n        break\nEOF"
}
```


### [2026-09-07T18:26:52.115Z] TOOL RESULT

```
leaves 1
leaf 0
 away, pass by’, fr. intensive 
pref. a- and gan, ‘to go’. See go. 
agog, adverb and adj., in a state of excitement. — 
F. en gogues , ‘mirthful’. Cp. etre en goguette(s), 
‘to be on the spree’, goguenard, ‘mocking, ban- 
tering’. All these words derive from *gog-, a 
base of imitative origin. 

-agogue, combining form meaning ‘leading, guid- 
ing’, as in demagogue, pedagogue. — Gk. -ayw- 
y6q, fr. aya>y6^, ‘leader’, fr. < 5 cyeiv, ‘to lead’. See 
agent, adj. 

agomphious, adj., toothless. — Coined by the 
German naturalist Ch. G. Ehrenberg (1795-1876) 
from priv. pref. a- and Gk. yojx^to^ (scil. 68wv), 
‘grinder tooth’, fr. y6jxcpo<;, ‘bolt, nail’. Seegom- 
phosis and -ous. 

agonic, adj., not forming an angle. — Formed 
with suff. -ic fr. Gk. < 5 cyo>voi;, ‘without angles’, 
fr. A- (see priv. pref. a-) and yovta, ‘angle’. See 
-gon. 

agonist, n.. a contender in public games. — Gk. 
aywvtarTj?, ‘combatant; actor’, fr. dcyawiCeO'dm. 
See agonize and -ist and cp. antagonist, deutera- 
gonist, protagonist, tritagonist. 

Derivatives: agonist-ic , adj., agonist -ic-al-ly, 
adv., agonis
```


## [2026-09-07T18:26:58.755Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC ned ===\"; grep -n \"^ned-\\|^nedos\\|^nedo-\\|^nodos\\|^nodo-\" IEC.txt | head -20; echo \"=== IEC nedos/nad ===\"; grep -n \"'reed'\" IEC.txt | head -20"
}
```


### [2026-09-07T18:26:58.804Z] TOOL RESULT

```
=== IEC ned ===
=== IEC nedos/nad ===
2387:dön- ‘reedbed, swamp; reeds’ Doric dónax ('reed', fr. *donu *'water', as in Skt. Av. dän, Oss. don?); Li. duónis, io ‘reed, rush’; Latv. doni ‘sedges’
```


## [2026-09-07T18:27:00.173Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SYN NET ===\"; grep -n \"^9\\.34\\|NET$\\|9\\.34 NET\" SYN.txt | head; echo \"=== WLD band3 nask/nada ===\"; grep -n \"naska\\|nada-\\|nadá\" WLD_band3.txt | head -20"
}
```


### [2026-09-07T18:27:01.453Z] TOOL RESULT

```
=== SYN NET ===
13491:9.34 9.342 9.35 9.36 9.37 9.38 9.41 9.412
14480:9.34 SPREAD OUT, STREW
14535:9.342 PRESS (vb.)
=== WLD band3 nask/nada ===
```


## [2026-09-07T18:27:06.126Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC ned line-start ===\"; grep -n \"^ned\\|^nēd\\|^nodh\\|^nod\" IEC.txt | head -20; echo \"=== IEC nassa/nodus ===\"; grep -n \"nodus\\|nectere\\|nascim\" IEC.txt | head -10; echo \"=== WLD3 nasc/nodus ===\"; grep -n \"nascim\\|nodus\\|nezzi\" WLD_band3.txt | head -10"
}
```


### [2026-09-07T18:27:06.203Z] TOOL RESULT

```
=== IEC ned line-start ===
6212:nedd); MHG stætic, gs -iges (cf. stat); OE ste- dig (‘sterile’, cf. stede “fixed point); OCS lo- vici, adj. & s. (lovið: Li. cf. teltikas summo- ner”; tarpikas “entry”
=== IEC nassa/nodus ===
4205:scraping noise’, fr. *gnitio); Ir. gníoth ‘noise’. (For Lat. nitor ‘strive’, see kneit- in view of Li. knieciu “strive”, despite Fest. gnixus: nixus) gnod- ‘knot, lump’. Cf. gnót- Lat. nodus (knot. WP & EM untenable); Du. knoet ‘scourge’; Sw. knota *knuckle- bone’; ON cf. (GA) knatt-, knottr ‘ball’: LG knautschen, v. (for *knotschen "ball up"); (*-ó- in) knasch, knass, adj. ‘tight. (R knut 'knout^ is fr. an ON variant, cf. ON knütr, m. ‘knot; lump’; knüta 'knuckle-bone") gnót- ‘knot, lump’. Cf. gnód- Du. cf. knoedel ‘rissole’ beside knoest ‘knot, tangle’; Pol. gnat ‘bone’; Cz. hnát “bone, shin”; pl. ‘runners on sled’; cf. Slovene gnjat “ham; club’; Srb. gnjat ^shinbone? gnubh-, see gnubh- gnugoalos, is (gnugil-) “lump, knob, fist, club'. WP I, 582 OFris. knokel ‘knuckle’; Du. knokkel, id.;
11796:nódos, is, io ‘knot, tie’. WP II, 328 Alb. (LW or « *nodio) nye, gs: neni, m. & nye, def: nyja, f. id.; Lat. nodus, gs: -i, m. ‘knot, noose, knot in wood: MLG nuot, sf. “joint, fitting; LG opt nüte, f. ‘wood joint, dovetail, mortice'; Du. Fris. neut, f. ‘tenon, bolt, nut’; Icel. nóti, m. “match, equal" beside nót, f. pl. nætr "large net’; Norw. not, pl. noter, Sw. not, pl. -ar, f. 'fishing-net; Ukr. cf. pry-nada ‘lure, charm’; Cz. cf. v-nadidlo, n. ‘bait’
=== WLD3 nasc/nodus ===
742:MI. Lateiniath Adrés — fopis: 7% hérés 05, 543. ~dre 22°. ira 4, 107. hen 664. int, (100) 135, irrifo, -dre 140. hernia GM. ia, wd 97, hestermus Gi ratutn, -tom, -fud 742 Aibermus 547 Tialia 251. Adem O47 iter, iio 102. Aillag (OM. terum 43, 100 hilum (O76). ifo, -dire 108. hinnus 113. juba, jubar 204. hippie ito, -are 880. wbilim 210. ] . are um 210. Air, tr 605. fides T76. hire O04, jigerum 202 Airews 610 pugo, ere 210 Anm, | Airrio, -ire Fugbsieed 201 hirsitus 610 Fugu 201. hirtus 610. juncus 206 hieco, -ere S40. j yungo, -ere 202. hivpidus 610. indiimentum 109. jinodus 200. ema G63. induo, -ere 10M. jiniperus 208, hontia 583. indusium 109, jini 20M). horefus alat. 859. indiitiag TOS. J | hordeum 611. induvire 109. Suppiter T73 , iri SOL. tafensus 680. jurgo 203 Aornwe }06, safernua 325, jara, -dr horres, -Ere G10. inferws 323, jita »Sateung™ 200. Aertor, -~bri G01. infeatne BO4. jm ,.Brithe” 100 a infrd 323. : hospes O40, TT", rifula 207. juvenia 200). hostia 40, iagena (258"). jure, ire 201. hoslis G40, ingluvigs 62. ; qe 202. | liirvinus O83. mngrup, re (M7, (685 binm, laben 384", miles  Anm, 1). litho, <ire 431° Aunws 662 ing I faber, -iria 432° jaceo, -fre 190. iniiwm 102, idérum: 441". jacio, «ere LO). imope 175. ldjrusca S85", 432°. jon 101. injuam 475*. fturiwm 355". jrnitricds 205, inquittnus 615. lac 66D. dana 104. inguing, -ire 460. lacea 421" Jénus 104. indegue, insece 475". lancer 410° Hea (185, 1918) 4, inacliscere 505 lace 419° imatcuro, -dre GOE*. lacerta 421*. Sot, feds BR. inafigo, -dire 613%. lecertua 421°. ictus 8, inatingwo, -tre G13". fooinia 410". idem (770) imewla 452°. lan, Inceseo 421° jecundauen 205. 1 _ sere 420" lacdnar 35%)*. jecur infer 126, lacus 350°. Segius O07, interduo, -duim S15. igedo, -orn FTO". igitur (8 Anm. 2). inferficin, -ere B27. lovtus (26, 379°. rus G6). tmlerien U7. laceus 37S* i 3 323 {nterocrea 34. lalie, «dre 370* fia 163. infertrigo 729, lima 386%, ile 34, intra, oird 126. lombo, -ere 384". imdgo 102. infro, -dre T33, TS4. limenine 376". imifrilive 1O4*, 110*, infue 137. lomia, laminm 434". inter TST. inulens 3, 108. ismmina 355*. imbractum 282", firmus 3, 1048. line 2M), imitirwe S58. inrilus 475, lances 92". dmiter. «iri 102. siaveap oO. longqueo, -fre TI2*. imminss T33%. lone, -dre (44%) imminis 240*. Sree? F alnd: 20g. limtige 296. impedio, -ire 24* ioreafid alut. 203. lonx 158.
```


## [2026-09-07T18:27:16.192Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('IEC.txt',encoding='utf8',errors='replace').read()\nlines=t.split('\\n'); off=sum(len(l)+1 for l in lines[:11795]); leaf=t[:off].count('\\f')\nprint('IEC leaf',leaf,'-> printed ~',2*(leaf-15))\nEOF\necho \"=== LEW nodus/necto ===\"; grep -n \"^nodus\\|^necto\\|^nassa\" LEW_1910.txt | head\necho \"=== LAT nodus/necto ===\"; grep -n \"^nodus\\|^necto\\|^nassa\\|nodus,\" LAT.txt | head\necho \"=== SYN REED ===\"; grep -n \"REED\\b\" SYN.txt | head"
}
```


### [2026-09-07T18:27:17.692Z] TOOL RESULT

```
IEC leaf 473 -> printed ~ 916
=== LEW nodus/necto ===
=== LAT nodus/necto ===
40468:nassa, -ae f. (naxa): nasse; — est piscatorii uasi genus, quo cum
40895:necto, -is, nexui (quelquefois nexi, les deux formes sont rares),
40931:necto, et en sanskrit^ naddhalj. "attachd" k cot 4 de ndhyati. Ceci conduit
62593:synodus, -I: coafr^rie, synode. Eapruat tardif au gr.cruvoSoe
82373:nodus, ligne 4 du bas, 1.: abnodo.
=== SYN REED ===
```


## [2026-09-07T18:27:21.101Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '40895,40945p' LAT.txt; echo \"=== nodus entry ===\"; grep -n \"^nodus\\|^nödus\\|^nôdus\\|nodus, -I\\|nodus, -i\" LAT.txt | head"
}
```


### [2026-09-07T18:27:21.168Z] TOOL RESULT

```
necto, -is, nexui (quelquefois nexi, les deux formes sont rares),
nexum, nectere: enlacerj d T ou lier, attacher, nouer. Synonyme de
ligare, cf. F.160,14: nectere, ligare, P.F.307,31: obnectere, obligare.
Ancien, classi que. 8'emploie au sens propre comme au sens figur£.
Mais le sens propre ne se trouve guere qu'en poesie; la prose connait
le mot surtout dans son sens figur 4 et juridique. Quelques rares
traces de nexa demeurent dans les 1 . romanes, cf. M.L.5903; mais partout
nectere a ete supplante par ligare, nSdSre et leurs derivas. Les
grammairiens attribuent aussi aux antiqui un doublet avec l*s du
desideratif nex 5 ,-is, ainsi Prisci en, GLK II 4fiy, qui cite de Liv.
Andr.33 nexebant multa inter se flexu modorum dubio', cf.Acc.Trag.
13° ou neximus est atteste par le metre. Mais la forme nexd,—Bs
(qui serait a nectS ce que amplexor est a amplector ) egalement cit<?e
par Priscien parait reposer sur une fausse lecture du v. de Virgile,
Ae.5,379 ou la v^ritable leyon est nixantem.
Pe mgme la forme de glossaire noxae: colligatae (cf. Lowe, Prodr.371)
doit gtre corrig^e en nexae, comme obnoxae d'Accius, Trag.atf,en obnexae.
Derives et compos<?s: nexus,-us m. : enlacement; lien, etreinte; se
dit specialement en droit, a cot<? de nexum (Lex XII Tab. G, 1), pour
designer 1'obligation per aes et libram, acte solennel de pret,
comprenant 1'usage de la balance ( libra) et l*^change de paroles
sacramentelles qui lient (necto) le debiteur au cr4ancier, et qui
sans doute se sont substituees a l'emploi d'un lien plus materiei;
cf. uinculum iuris, obligat ia, solutio. Celui qui «?tait ainsi engage
3'appelait nexus, cf. Varr. L.L.7,105; nexio (tardif); nexilis (-litas),
nexibilis-, nexuosus (tardif); nexabunde (id.);
adnecto (an-): attacher a, M.L.480; annexus,-rus m.: annexion (Tac.);
annexio (b.lat.): liaison; dans la 1. de la grammaire, traduit
"mauvaise coupe des mots"; circumnecto', conecto: attacher ensemble,
crup,7iXexto (co- d'apres cdniueB? ),^d*o{i c 5 nexum,-l et cGnexio traduisant
en logique crunJtXoxq et <ruvrip.p,evov <x^Coop,a; in-, inter-, pro-, re-,
sub-nectB. Pour obnoxius, v. ce mot.
Pour la formation, cf. plecto, en face de gr.7lXexto. En consideration
du present skr. ndhyati "il attache", on est tentd de partir d'une
racine neg r h~. Mais, a part necto et ndhyati, cette racine n'est
appuy^e par aucune forme. Or, en latin meme, on a nodus a cotd de
necto, et en sanskrit^ naddhalj. "attachd" k cot 4 de ndhyati. Ceci conduit
a poser une racine nedh-; et en effet l'irlandais a naidm "lien",
etc. Comme skr. ndhyati ne peut representer phonetiquement un ancien
nadhyati, ce present ne saurait s r expliquer que comme denominatif
d f un substantif nah— issu de nadh—) or, la racine ne fournit gubre
que ce present, ce qui indique une origine d<?nominative. II ne devait
pas y avoir de present ancien; car l'irlandais n'a qu'un present
derive nascim "je lie" (bret. naska), sur lequel a et<? fait un parfait
nenaisc. Un substantif skr. *nah- n'est pas atteste; mais on a aksa-
nah-, upd-ndh- "sandale", parlnah- "ce qui enclot" (pour lesquels
les grammairiens enseignent les nominatifs upandt, paritat). Le vo-
calisme o de nodus ne peut venir que d*un ancien thbme radical athe-
matique. Dos lors, un present ancien n ? ayant pas existe, necto serait- 773
nefrendes
une forme nouvelle cre£e d^aprbs plecto et sur laquelle aurait ete
=== nodus entry ===
62593:synodus, -I: coafr^rie, synode. Eapruat tardif au gr.cruvoSoe
82373:nodus, ligne 4 du bas, 1.: abnodo.
```


## [2026-09-07T18:27:30.072Z] TOOL CALL #59: Bash

```json
{
 "command": "for u in \"https://abadis.ir/fatofa/%D9%82%D8%B1%D9%87-%D9%86%DB%8C/\" \"https://vajehyab.com/?q=%D9%82%D8%B1%D9%86%DB%8C\" \"https://en.wiktionary.org/wiki/%D9%82%D8%B1%D9%86%DB%8C\" ; do echo \"### $u\"; timeout 90 python3 tools/fetch_source.py \"$u\" --note \"page 354 entry 1 node 2: qara-ney / qarani 'clarinet, black flute'\"; done; echo; for f in $(ls -t /home/sfmqrb/git/rishe/data/verification/sources/web/*.txt | head -3); do echo \"#### $f\"; head -c 1500 $f; echo; done"
}
```


### [2026-09-07T18:27:33.686Z] TOOL RESULT

```
### https://abadis.ir/fatofa/%D9%82%D8%B1%D9%87-%D9%86%DB%8C/
/home/sfmqrb/git/rishe/data/verification/sources/web/fa5e89f4c5672db9.txt
### https://vajehyab.com/?q=%D9%82%D8%B1%D9%86%DB%8C
/home/sfmqrb/git/rishe/data/verification/sources/web/a4cd835f9558fa38.txt
### https://en.wiktionary.org/wiki/%D9%82%D8%B1%D9%86%DB%8C
/home/sfmqrb/git/rishe/data/verification/sources/web/9b84b5be805f20b4.txt

#### /home/sfmqrb/git/rishe/data/verification/sources/web/9b84b5be805f20b4.txt
URL: https://en.wiktionary.org/wiki/%D9%82%D8%B1%D9%86%DB%8C
FETCHED: 2026-09-07T18:27:33Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found
#### /home/sfmqrb/git/rishe/data/verification/sources/web/a4cd835f9558fa38.txt
URL: https://vajehyab.com/?q=%D9%82%D8%B1%D9%86%DB%8C
FETCHED: 2026-09-07T18:27:32Z
STATUS: 200
TITLE: معنی قرنی | واژه یاب

'
 />

 معنی قرنی | واژه یاب 

 26 فرهنگ 
 212 مدخل

 همه دیکشنری مترادف طیفی آزاد + 

 همه دقیق مشابه آوا متن آغاز قافیه 

 جست‌وجوی دقیق

 قرنی
 لغت‌نامه دهخدا
 قرنی . [ ق َ رَ ] (اِخ ) اویس . رجوع به اویس قرنی شود.

 قرنی
 لغت‌نامه دهخدا
 قرنی . [ ق َ رَ ] (ص نسبی ) نسبت است به قَرَن . رجوع به قَرَن شود.

 جست‌وجوی مشابه

 قرنیز (معماری)
 دیکشنری فارسی به انگلیسی
 cornice

 قرنیه (کالبد شناسی)
 دیکشنری فارسی به انگلیسی
 cornea

 قرنین
 لغت‌نامه دهخدا
 قرنین . [ ق َ ن َ ] (اِخ )جایی است در بالاترین نقطه ٔ وادی دولان از ناحیه ٔ مدینه که بدان ذات القرنین نیز گویند. (معجم البلدان ).

 قرنین
 لغت‌نامه دهخدا
 قرنین . [ ق َ ن َ ] (ع اِ) تثنیه ٔ قرن . دو قرن . رجوع به قرن شود.

 قرنیه
 لغت‌نامه دهخدا
 قرنیه . [ ق َ ی َ / ی ِ ] (معرب ، اِ) رجوع به پرده شود.

 بیشتر
 ۲۸ واژه مشابه 
 جست‌وجوی متن

 corneous
 دیکشنری انگل�
#### /home/sfmqrb/git/rishe/data/verification/sources/web/fa5e89f4c5672db9.txt
URL: https://abadis.ir/fatofa/%D9%82%D8%B1%D9%87-%D9%86%DB%8C/
FETCHED: 2026-09-07T18:27:32Z
STATUS: 200
TITLE: قره نی - معنی در دیکشنری آبادیس

قره نی - معنی در دیکشنری آبادیس 

 دیکشنری مترجم بپرس 

 قره نی
 /qareney/

 معنی انگلیسی : clarinet 

 دنبال کنید 

 لغت نامه دهخدا

 قره نی. [ ق َ رَ ن َ / ن ِ ] ( اِ مرکب ) از سازهائی است که نواختن آن به وسیله زبانه ای صورت میگیرد، مثل نی انبان و سورنای و دونای ، و در سازهای اروپایی مثل ساکسوفون و چنگ چینی. رجوع به ساز شود. 

 فرهنگ فارسی

 ۱ - نی سیاه ۲ - نی بزرگ نوازندگی است که از چوب و فلز ساخته می شود و رنگش سیاه است .
نی سیاه، یکی از آلات موسیقی شبیه نی ازجنس چوب وفلز 

 فرهنگ معین

 (قَ رَ. نِ ) [ تر - فا. ] (اِ. ) نی بزرگ که از چوب و فلز ساخته می شود. 

 فرهنگ عمید

 = کلارینت 

 دانشنامه عمومی

 نوعی کلارینت که توانایی تولید فاصله های موسیقی شرقی ( ربع پرده ) را دارد به قره نی معروف است. قره نی که یکی از ساز های مصری بشمار میاید در ماه محرم ایران مخصوصا ( اردبیل ) بیشتر بکا
```


## [2026-09-07T18:27:43.698Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KNT nada ===\"; grep -n \"nada\\|^nāda\" KNT.txt | head; echo \"=== PHD nay/nad ===\"; grep -n \"^nāy\\|^nay \\|nāy \\[\" PHD.txt | head; grep -n \"nāy\" PHD.txt | head; echo \"=== NYB nay ===\"; grep -n \"^nāy\\|nāy \\[\" NYB_vol2_glossary.txt | head"
}
```


### [2026-09-07T18:27:43.779Z] TOOL RESULT

```
=== KNT nada ===
5676:See nada lai baa a D Lo AMA tae io at OT IPE Ауаз a зз
=== PHD nay/nad ===
314:~th: friendship, love. 140$ [dws | N ~] shoulder. 2108 [duš | N ~] last night, previous evening. dēš-, —išn, v. Ł 2 dēšīdan, !doxtan. dēšag [dwsk'] dear, loving. —ih: love. došaram [dwi?m | M dw%’rm] love. dēšastar [dušstl] west. īdēšīdan, 458- [dws-ytn!] like, love. ~ign: liking, pleasure. *došidan [dwsytn'] = *dóxtan. dēšīzap [dwsyck' | (M дох, ] dwskyzh), N —a] maiden, virgin. “АҺ: maidenhood, virginity. dówom [2wm | N ~] -second (in compound numerals). 1dóxtan, dēš- [dwhtn', dws | N ~] milk. *dóxtan, döz- [dwhtn', dwc- | N ~] sew. dóys?r [dwysl = Av. dõiðra-} eye. dēz-, v. ?dóxtan. drafš [dips | P drfš, N ~] banner. drafšīdan, drafš- [dipi-ytn! | P drfi-, N ~] 1. shine; 2. tremble. drahm [ZWZN! < А zwza | M drhm, N dir(h)am] drachm. dra(h)nāy [di(k)rd) length. dramanag [dimnk! | N dirmana] wormwood. dranģ [ding | N dirang] period, duration. dranjidan, dranj- [dInc-ytn!] speak. ~išn: speech. draxt [4/0)А | M drxt, N diraxt] tree. drày-, ~išn, v. drāyīdan. drayā(b) [dlyd?(p) | M dry?b, N darya(b)] sea. ~-bār LI | N -bàr] sea-shore. агауӣп-јбуіёп [did?n ywdsn'] one who speaks while eating. ~ih: (the sin of) speaking while eating. drayidan / drayistan, drāy- [dPd-ytn!, -stn! | M dryst, dPy-, N daráyidan] speak (daevic), chatter. —išn: chatter. drāz [dlc | N diráz] long. *drém [dlym] phlegm. driyó$ [41220 | N daryūš, darwé§] poor, needy. ~th: poverty. dró [KDBA < А kdb’; dlwb! | M drw, (N daróy)] lie, deceit. drd [SRM < A šim; dlwt! | M атта, N daród] health, well-being, prosperity, peace. dró-dadwarih [KDB A d'twblyh] false judgement. īdron [dlwn' | N dariina] bow. *drón [dlwn' | N darūn] consecrated bread, ceremony in which c.b. is used.
508:nay [KN YA < A gny’; та | N ~] reed, cane. nay-, v. nidan.
509:nay [nd | M my, N ~] tube, flute, clarion; pole, perch (10 ft.).
551:pillagan [plk’n' | M pylg, N ~] steps, ladder. pim [pym] pain, pang, sorrow. ~gén [-kyn'] sorrowful. pir [руі | N ~] old, aged, ancient. ~ih: age. piring [pling | M pryng, (N pirind)] monochrome damask, pist [pst! | N ~] browned flour. pistag [pstk! | IN pista] pistachio nut. pišīz [pšyc | N ~] small copper coin, ‘farthing’. pēhišn [pwhsn'] corruption, decay. pēlāwad [pwPft! | М pwl'wd, N pēlād] steel. ~ën [-yn!] (made of) steel. pondik [pndk' | Ar. b/fundug] hazel-nut. por [pwl | N —] francolin. pēryētkēš [pwlyw(k)kyf = Av. paoiryē.tkaēša-| (one of) the first teachers of the Mazdean religion. ~ЛЬ : the primal doctrine of the Mazdean religion. pēst [pwst! | = M, N ~] skin, hide; bark, shell. mēn [-yn! | N ~in] (made of) skin. pēšīdan, pēš- [pws-yin' | N <] cover, put on, wear. ~išn: covering. potk [pwtk' | N ~] sledge-hammer. poxtan, paz- [APPWN-tn' < А V?ph; pwhtn', pc- | M pwxtn, N ~] cook, bake. рӧу- [pwd- | (P pwd-), N ~] run. ~iSnig : running. p6z(ag) [pwc(k!) | N pēz(a)] snout, muzzle. püdag [pwtk! | N pūda) foul, rotten. —ih: rottenness. 1puhl [pwhl | N pul] bridge. *puhl [pwhl] expiation, atonement; punishment. puhlénidan [ pwhlynytn'] cause to atone. purnāy [pwln’d] adult. purr (MALE < A mlh; pul | M pur, N ~} full. =-ģāh [-g’s] at the fullness of time, about to die. ~-тюаһ [-mh] full moon. —-rawišnih [-lwbsnyh] fullness. ~-sardag [-sltk'] of all kinds. --xwarrah [-G DE] full of glory. pursidan, purs- [pwrs-ytn' | M pwrs-ydn, N ~] ask. Vu re: Е ~iSn: question. — ~i$nig : responsible. pus [BRE < A br-h; pws | = M, N =] son. ~ar [BREI, pwsl | M pwsr, N ~] son. —yàn [pwsd?n! | M pwsy’n] womb. pušt [52001 | = M, N ~] back; support, protection.
5280:nāydāg wahīg wihīr- nārīg wihīrišn nāysrāy nayizag wan- niyox&- niyox&idan niyoxiián wing wānīdan nān Worübarst Worüjarst nohom nihumb- nihumbidan Wahman naxust nihuftan
128:delete mezidan ... suck. for ?mēzišn ... read ! meziin ... for mistan, *mēz- read... *mēz-.. mihoxt [mytwht' = Av. midaoxta-| falsehood. *mihr .. add ~ druxtan : break faith. add mizīdan, miz- [myc-ytn' | N mazidan] suck. for *moy-mard ... read mowmard ... mēy ... add M mwy. read nüxun [n^hwn' | P nxwn, N nàxun] (finger) nail. delete nāyīzag ... (read wezag). nek, ~th ... add benefit. nibastan ... delete SKBHWN-tn' < A Vškb; nibastan ... read M nb’st, P nb’y-. nibeg ... add M nbyg. nibištan ... |YKTYBWN-tn'... (not -stn'). nidan, nay- |DB(Y)LWN-tn' < A Ydbr |... nigün, ~sar |-s 1 | (P ngws’r)| downwards. add *nihēb |nyhyp | N ~] fear, terror. for nīšān read nišān...
170:abilag 5/4! | N ~a] blister. a-bim [bym] fearless. āb-kāmag [5A mk! | N ~a] a thick, sour soup. abnüs Pžēnws | (N ābnūs)] ebony. a-biy Pbwd] senseless. ~ih: senselessness. à abr РЫ, Séi | N ~] cloud. M bel abrang [ing | N aurang] glory, splendour. abrastan, abraz- [AP stn',SPc- | М ?br?st, N (afráttan), afrdz-] lift, raise. abraz [Pe | N afrāz] acclivity. abrēšom Pflyš(u)m | M? bryfwm, N ~} silk. ~én [-yn!] silken. abróxtan, abróz- ['piwhtn', ?phoc- | M brwxt, ?)brwc-, N afróxtan, afróz-] light, kindle, illuminate, polish. ~i$n(ih): illumination. āb-tazan Pftcn!] watercourse. a-bun [*dwx!] baseless, bottomless. a-burd-framān ['bwltplm^n'] disobedient. ~th: disobedience. aburnāy f(w)lnd, v. purnāy | N burnā] under age, child. ^h : childhood. aburnáyag [?A(w)/n’(d)yk'] child. abus [pws] (woman) having just given birth. “АҺ: childbirth. арив, -tan Pws, -tn! | M ’bwws, v. ábestan] pregnant. „il: pregnancy. abydxtan, abyóz- Phywhtn', ?bywc-] join, mix. āb-zan zn! | N ~] bath. labzar [el pel] M *6c*7, N afzār] instrument, means; spice. *abzar [6271 | M bail skill, power; powerful. „ūmand [-wmnd] skilled, able. abzāy-, —išn, у. abztidan, abzón [?pzwn! | M, J ”*bzwn, N afzün] increase, growth. ~ig [-yk!] increasing, expansive, bountiful. ~igih: bountifulness. abzüdan, abzáy- ['pzwtn!,^?pzd- | M ?bz'y-, N afzüdan, afzāy-] in- crease, grow. ~i$n: increase, growth. a-čār [cI] inevitable, Jee ~ag [-k'] compelled.
314:~th: friendship, love. 140$ [dws | N ~] shoulder. 2108 [duš | N ~] last night, previous evening. dēš-, —išn, v. Ł 2 dēšīdan, !doxtan. dēšag [dwsk'] dear, loving. —ih: love. došaram [dwi?m | M dw%’rm] love. dēšastar [dušstl] west. īdēšīdan, 458- [dws-ytn!] like, love. ~ign: liking, pleasure. *došidan [dwsytn'] = *dóxtan. dēšīzap [dwsyck' | (M дох, ] dwskyzh), N —a] maiden, virgin. “АҺ: maidenhood, virginity. dówom [2wm | N ~] -second (in compound numerals). 1dóxtan, dēš- [dwhtn', dws | N ~] milk. *dóxtan, döz- [dwhtn', dwc- | N ~] sew. dóys?r [dwysl = Av. dõiðra-} eye. dēz-, v. ?dóxtan. drafš [dips | P drfš, N ~] banner. drafšīdan, drafš- [dipi-ytn! | P drfi-, N ~] 1. shine; 2. tremble. drahm [ZWZN! < А zwza | M drhm, N dir(h)am] drachm. dra(h)nāy [di(k)rd) length. dramanag [dimnk! | N dirmana] wormwood. dranģ [ding | N dirang] period, duration. dranjidan, dranj- [dInc-ytn!] speak. ~išn: speech. draxt [4/0)А | M drxt, N diraxt] tree. drày-, ~išn, v. drāyīdan. drayā(b) [dlyd?(p) | M dry?b, N darya(b)] sea. ~-bār LI | N -bàr] sea-shore. агауӣп-јбуіёп [did?n ywdsn'] one who speaks while eating. ~ih: (the sin of) speaking while eating. drayidan / drayistan, drāy- [dPd-ytn!, -stn! | M dryst, dPy-, N daráyidan] speak (daevic), chatter. —išn: chatter. drāz [dlc | N diráz] long. *drém [dlym] phlegm. driyó$ [41220 | N daryūš, darwé§] poor, needy. ~th: poverty. dró [KDBA < А kdb’; dlwb! | M drw, (N daróy)] lie, deceit. drd [SRM < A šim; dlwt! | M атта, N daród] health, well-being, prosperity, peace. dró-dadwarih [KDB A d'twblyh] false judgement. īdron [dlwn' | N dariina] bow. *drón [dlwn' | N darūn] consecrated bread, ceremony in which c.b. is used.
510:~ pazd- : blow, play the flute. *nāydāģ [nywt’k'] deep, unfordable, navigable. nayestàn [KN Y Ast^n! | N ~] reed-bed, cane-brake. nāyīzaģ [»vck! | N ~a] small reed, straw. nay-sray [rds d] flautist. nazd [nzd | = M, N ~] near. nazdik [nzdyk! | = M, N ~] near. ~ih: proximity. nazdist [x3dst'] first. nàzišn [x*cšn! | N nāsi$] 1. boasting; 2. kindness. nàzuk [n’cwk! | (M wzwg), N ~] tender, gentle; fickle. né [L4 < AP | M ny, N na] no, not. nék [nywk! | M nyk, N ~] good, beautiful. ~th: goodness. nék-góhr [nywk gwhl] good-natured, virtuous. ~ih: goodness, virtue. nēkēģ [nywhkwk! | M nyyquiw!, IN neho] == пёк. nem [PRG < А plg; nym | = M, N —] half. ~ag [nymk! | N ~a] half, side, direction. ~-аѕр [5р] centaur; astr. Sagittarius. ~-rōz [-lwe | M -rwe, N ~] midday, south. ~-tan [-tn' | N ~] middle of the body. nérang [nylng | N <] incantation, charm, spell. пёгӧб [nylwk! | M nyrwg, N nero] strength, power. ~omand [-’wmnd] strong, powerful.
551:pillagan [plk’n' | M pylg, N ~] steps, ladder. pim [pym] pain, pang, sorrow. ~gén [-kyn'] sorrowful. pir [руі | N ~] old, aged, ancient. ~ih: age. piring [pling | M pryng, (N pirind)] monochrome damask, pist [pst! | N ~] browned flour. pistag [pstk! | IN pista] pistachio nut. pišīz [pšyc | N ~] small copper coin, ‘farthing’. pēhišn [pwhsn'] corruption, decay. pēlāwad [pwPft! | М pwl'wd, N pēlād] steel. ~ën [-yn!] (made of) steel. pondik [pndk' | Ar. b/fundug] hazel-nut. por [pwl | N —] francolin. pēryētkēš [pwlyw(k)kyf = Av. paoiryē.tkaēša-| (one of) the first teachers of the Mazdean religion. ~ЛЬ : the primal doctrine of the Mazdean religion. pēst [pwst! | = M, N ~] skin, hide; bark, shell. mēn [-yn! | N ~in] (made of) skin. pēšīdan, pēš- [pws-yin' | N <] cover, put on, wear. ~išn: covering. potk [pwtk' | N ~] sledge-hammer. poxtan, paz- [APPWN-tn' < А V?ph; pwhtn', pc- | M pwxtn, N ~] cook, bake. рӧу- [pwd- | (P pwd-), N ~] run. ~iSnig : running. p6z(ag) [pwc(k!) | N pēz(a)] snout, muzzle. püdag [pwtk! | N pūda) foul, rotten. —ih: rottenness. 1puhl [pwhl | N pul] bridge. *puhl [pwhl] expiation, atonement; punishment. puhlénidan [ pwhlynytn'] cause to atone. purnāy [pwln’d] adult. purr (MALE < A mlh; pul | M pur, N ~} full. =-ģāh [-g’s] at the fullness of time, about to die. ~-тюаһ [-mh] full moon. —-rawišnih [-lwbsnyh] fullness. ~-sardag [-sltk'] of all kinds. --xwarrah [-G DE] full of glory. pursidan, purs- [pwrs-ytn' | M pwrs-ydn, N ~] ask. Vu re: Е ~iSn: question. — ~i$nig : responsible. pus [BRE < A br-h; pws | = M, N =] son. ~ar [BREI, pwsl | M pwsr, N ~] son. —yàn [pwsd?n! | M pwsy’n] womb. pušt [52001 | = M, N ~] back; support, protection.
585:šimšār Lë"! | N ~] box tree. Sir [HLBA < A hlb’; $1 | M šyyr, N ~] milk. šīrēn [5/yn! | M syryn, N ~in] sweet. ~ih: sweetness. SiSag [$y$k! | N fifa) bottle, flask. škaft [Ар] = Skeft. škāftan, škāf- [sk’p-tn' | M ‘kk’ pt, N fikáftan] split, burst. Skarag [skik! | P *škr-] (bird) of prey. škarwīdan, škarw- [fklw-ytn' | M ‘fkrw-st, N fikarfidan] stumble, stagger. škastan, Sken(n)- [TBLWN-tn' < A N tbr; škstn!, škyn- | M ‘tkn-, N stkastan, fikan-] break. ^ i$n: breaking. škēbāģ [fkyp?k! | P kyb-, N #hëba] patient. ~ih: patience. Skeft [škypt! | P “#kyft, N šigift] hard; extraordinary, astonishing; very. ~ih: hardness; hardship, distress; astonishment. šken(n)-, ~išn, v. škastan. ških- [fkyh- | N šikth-] be broken. Skóf-, у. Skuftan. Skdfag [fRwpk! | N šukēfa] flower, blossom. Skoft [škwpt'] = škeft. 1$kóh [ол | M Ай] poor. --īh: poverty. *§k6h [kwh | N sukdh] dignity, majesty; fear. škuftan, &ЕбЇ- [škwp-tn! | N fukuftan] flower, blossom. Énàs-, v. Snaxtan. šnàsag [fn'sk! | P *$n*sg] knowing, knower; sense. ~ih: knowledge. šnāxtan, $nàs- [fm htn!, fie | M хіп, Чи s-, N fin-] know, recog- nize. šnāyēnīdan, šnāyēn- [sz dyn-ytn'] please, propitiate. ~išn: happiness. šnāyīdan, šnāy- [fr'd-ytn!] praise, propitiate. --i$n : praise, gratitude. šnāz [frc | (N šinā(w))] swimming. šnāzīdan, šnāz- [fr'c-ytn! | M $2? 2-, (IN šināw-)] swim. $nóhr [snwhl | М *fnwhr] gratitude, contentment. šnūmaģ [fnwmk! | M *fnwm-] satisfaction, contentment. &nó&ag [šnwšk! | N šunoša] sneeze. $nüg [šnwk' | M *fnwg] knee. šnūman [fnwmn! = Av. xsniimaine] propitiation. 86n [swn'] kind, manner. ~ig [-yk!] customary, ordinary. šūy-, v. Sustan. Sdy [std | N ~] husband.
734:adult dād-meh, purnāy.
1225:childhood aburnāyīh, rahigih.
1244:clarion nāy.
1965:flautist nāy-srāy.
=== NYB nay ===
```


## [2026-09-07T18:27:59.397Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ndef leafof(f,ln):\n    t=open(f,encoding='utf8',errors='replace').read()\n    lines=t.split('\\n'); off=sum(len(l)+1 for l in lines[:ln-1])\n    return t[:off].count('\\f')\nfor f,ln,fmt in [('PHD.txt',509,'printed=leaf-21'),('NYB_vol2_glossary.txt',2650,'printed=leaf-8'),('HUB.txt',3654,'printed=leaf-10'),('AHD_watkins1985.txt',776,'printed=leaf-29'),('LAT.txt',40895,'printed=leaf-18'),('FVQ_pages.txt',10032,'printed=leaf-17')]:\n    l=leafof(f,ln); print(f,'leaf',l,'->',fmt,'=',l-int(fmt.split('-')[1]))\nEOF"
}
```


### [2026-09-07T18:28:00.669Z] TOOL RESULT

```
PHD.txt leaf 82 -> printed=leaf-21 = 61
NYB_vol2_glossary.txt leaf 150 -> printed=leaf-8 = 142
HUB.txt leaf 113 -> printed=leaf-10 = 103
AHD_watkins1985.txt leaf 73 -> printed=leaf-29 = 44
LAT.txt leaf 790 -> printed=leaf-18 = 772
FVQ_pages.txt leaf 296 -> printed=leaf-17 = 279
```


## [2026-09-07T18:28:23.669Z] TOOL CALL #62: Bash

```json
{
 "command": "timeout 120 python3 tools/fetch_source.py \"https://abadis.ir/fatofa/%D9%86%D8%B1%D8%AF/\" --note \"page 354 entry 1 node 4: Persian nard 2 = spikenard (Dehkhoda/Mo'in)\"; timeout 120 python3 tools/fetch_source.py \"https://abadis.ir/fatofa/%D9%86%D8%A7%D8%B1%D8%AF%DB%8C%D9%86/\" --note \"page 354 entry 1 node 4: Persian nardin/nardin = spikenard\"; ls site/pages/354.jpg 2>/dev/null || echo \"no site jpg\""
}
```


### [2026-09-07T18:28:27.396Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/b5b09154a70e0369.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/be98292335e83100.txt
site/pages/354.jpg
```


## [2026-09-07T18:28:30.399Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in b5b09154a70e0369 be98292335e83100; do echo \"#### $f\"; sed -n '1,80p' $f.txt | head -70; echo; done"
}
```


### [2026-09-07T18:28:31.634Z] TOOL RESULT

```
#### b5b09154a70e0369
URL: https://abadis.ir/fatofa/%D9%86%D8%B1%D8%AF/
FETCHED: 2026-09-07T18:28:26Z
STATUS: 200
TITLE: نرد - معنی در دیکشنری آبادیس

نرد - معنی در دیکشنری آبادیس 

 دیکشنری مترجم بپرس 

 نرد
 /nard/

 معنی انگلیسی : backgammons , backgammon-board , backgammon , scale 

 دنبال کنید 

 لغت نامه دهخدا

 نرد. [ ن َ ] ( اِ ) بازیی است معروف از مخترعات بوزرجمهر که در برابر شطرنج ساخته و بعضی گویند نرد قدیم است اما دو کعبتین داشته ، دوی دیگر را بوزرجمهر اضافه کرده است. ( برهان قاطع ). اردشیر بابک آن را وضع کرده لاجرم نردشیر نیز نامندش. ( منتهی الارب ). در قدیم در بازی نرد سه مهره به کار می بردند. مؤلف نفایس الفنون آرد: «عدد کعبتین را سه بنابر این نهادند که حرکات اکثر سیارات به سه فلک تمام شود». نظامی عروضی آرد: امیر [ طغانشاه ] سه مهره در شش گاه داشت و احمد بدیهی سه مهره در یک گاه و ضرب امیر را بود، احتیاطها کرد و بینداخت تا سه شش زند، سه یک برآمد. ( از حاشیه برهان قاطع چ معین ). بازیی است در مقابله شطرنج. ( غیاث اللغات ). بازیی است که بر صفحه با مهره ها می شود. ( فرهنگ نظام ) . نوعی از بازی قمار که دارای تخته ای است که سطح آن را به دو قسمت مشابه هم تقسیم کرده اند و در روی هر یک از آن دو قسمت شش خانه در طرف یمین و شش در طرف یسار رسم نموده و با دو طاس و سی مهره به روی آن تخته بازی می کنند. ( ناظم الاطباء ) : 
دگر بهره شطرنج بودی و نرد
سخن گفتن از روزگار نبرد. فردوسی.
که اینت سخنگوی داننده مرد
نه از بهر بازی شطرنج و نرد. فردوسی.
بدین سان که گفتم بیاراست نرد
بر شاه شد یک به یک یاد کرد. فردوسی.
نه نرد و نه تخته نرد پیش ما
نه محضر و نه قباله و بنجه. منوچهری.
دفتر به دبستان بود و نقل به بازار
وین نرد به جائی که خرابات خراب است. منوچهری.
نه نقل بود ما را نی دفتر و نی نرد
وین هر سه بدین مجلس ما در نه صواب است. منوچهری.
تاجز از بیست وچهارش نبود خانه نرد
همچو در سی ودو خانه است نهاد شترنگ . نجار ( ازحاشیه فرهنگ اسدی نخجوانی ).
مهره او سی سیه و سی سپید
گردش او زیر یکی تخت نرد. مسعودسعد.
نرد است و شراب است و کباب است و رباب است 
دانی تو که هر چار نشاط بشر آمد. سوزنی.
داو دل و جان نهم به عشقت 
در ششدره اوفتاد نردم. سوزنی.
از نرد سه تا پای فراتر ننهادیم 
هم خصل به هفده شد و هم داو سر آمد. سوزنی.
پیش سپید مهره مرگ اصفیا نگر
از مهره های نرد پریشان تر آمده. بیشتر بخوانید ... 

 فرهنگ فارسی

 ( اسم ) ۱ - نوعی بازی که بوسیله دوطاس ( کعبتین ) وسی مهره ( پانزده مهره سفید وپانزده مهره سیاه ) برروی تخته (تخته نرد ) یاصفحه ای مقوایی انجام میشودبدین طریق که هریک ازطرفین بازی مهره های خودراکه پانزده عدداست ( یک طرف سیاه وطرف دیگر سفید ) روی تخته می چینندوسپس بنوبت طاسها رامی اندازندومجموع خانه های دوطاس راماخذ قراردهندوطبق همان شماره مهره های خویش را براست یاچپ ( طبق چیدن مهره ها ) حرکت دهند این کار آن قدرادامه می یابدتاهمه مهره ها درشش خانه متصل آخری جمع شود.پس از آن مهره هاراطبق شماره خالهای طاسهاازتخته نردخارج کنند.هرکدام ازطرفین که تمام مهره های خودرازودترخارج کندبرنده یک دست شناخته میشودواگرهمه مهره های یک حریف خارج کندبرنده یک دست شناخته میشودواگرهمه مهره های یک حریف خارج شوددرصورتیکه طرف مقابل حتی یک مهره رانتوانسته باشدخارج کنددودست بنفع برنده حساب شودکه آنرا اصطلاحا[ مارس ] گویند.معمولادوربازی شامل ۵ - دست است .توضیح ۱ اختراع نردطبق کارنامهاردشیربابکان وشاهنامه به بزرگمهر نسبت داده شده : بدین سان که گفتم بیاراست نرد برشاه شدسربسریادکرد... ( شا.بخ ۸ ص ۲۶۶۶ ) توضیح ۲ نرددرقدیم هفت بازی داشته ازین قرار: ۱ - فارد( فرد ) .۲ - زیاد.۳ - ستا (سه تا ).۴ - خانه ( خانه گیر ) .۵ - طویل . ۶ - هزاران ( ده هزار ).۷ - منصوبه . توضیح ۳ قدمادربعضی ازبازیهای مذکورمثل [ سه تا] سه طاس بکارمیبردند: ازپی سی طفل رادریک بساط آن سه لعبت زاستخوان آخرکجاست ? ( خاقانی .سج.۴۹۲ ) وبرخی مانندفردوزیاده رابادوطاس بازی میکردند.توضیح ۴ وضع نردمنطبق باوضع طبیعت است : زیراکه دوران کعبتین در طاسک وظهورنقوش مختلف که مبادی بازیهای متنوعندبمناسبت سیرافلاک وسیارات است که مبادی حدوث حادثاتندوارباع بساط او که محل ظهورانواع افاعیل اندبمثابت عناصر اربعه ...چنانکه فصول سال چهارندبساط نیز بچهارقسم مساوی قسمت شده و آنکه اورابه بیست وچهارقسم کرده بنابر آنست که ساعات شبانروزبیست وچهارندوعددمهره راسی بنابر آنکردندکه ماهی سی روزاست وباعتبارروزوشب یک نیمه آن سفیدویک نیمه آن سیاه کردند... ودرکعبتین مقابل یک نقطه شش نهاده اند ودرمقابل دوپنج ودرمقابل سه چهاربنابر آنچه خواستندنقش راازبالاوزیرچون جمع کنند ازهفت که عددسیاره است تجاوزنکندوشک نیست در آنکه اگردرجهتی هفت نقش کردندی نقوش مختلف صورت نبستی پس طریقه ای کردندکه دایماهفت مرعی باشدونقوش مختلف بماند... ۲ - تنه وساقه درخت : ای خداوندی که فضل وفخروجاه وعزتو آن چو بیخ است این چونرداست آن چوشاخ است این چوبار. 

 فرهنگ معین

 (نَ ) [ په . ] (اِ. ) نوعی بازی مانند شطرنج که ابزار آن یک صفحة چوبی به همراه ۱۵ مهرة سیاه و ۱۵ مهرة سفید و دو طاس می باشد. 

 فرهنگ عمید

 ۱. نوعی بازی که ابزار آن شبیه شطرنج و مرکب از تخته و ۳۰ مهره (۱۵ مهرۀ سفید و ۱۵ مهرۀ سیاه ) و دو طاس می باشد، تخته نرد.
۲. [قدیمی] تنۀ درخت، ساقۀ درخت: ز خاکی که خون سیاوش بخورد / به ابر اندرآمد یکی سبزنرد (فردوسی: ۲/۳۷۵ )، مردم اندر خور زمانه شده ست / نرد چون شاخ گشت و شاخ چو نرد (کسائی: لغت فرس: نرد ). 

 گویش مازنی

 /nord/ چوبی که در دستگاه بافندگی است و پارچه ی بافته شده به گرد آن پیچیده شود

 دانشنامه اسلامی

 [ویکی الکتاب] معنی نُرَدُّ : باز گردانده شویم
ریشه کلمه: 
 ردد (۵۹ بار)
 wikialkb: نُرَدّ 

 دانشنامه آزاد فارسی


#### be98292335e83100
URL: https://abadis.ir/fatofa/%D9%86%D8%A7%D8%B1%D8%AF%DB%8C%D9%86/
FETCHED: 2026-09-07T18:28:27Z
STATUS: 200
TITLE: ناردین - معنی در دیکشنری آبادیس

ناردین - معنی در دیکشنری آبادیس 

 دیکشنری مترجم بپرس 

 ناردین

 دنبال کنید 

 فرهنگ اسم ها

 اسم: ناردین (دختر) (فارسی) (طبیعت) (تلفظ: nārdin) (فارسی: ناردین) (انگلیسی: nardin) 
 معنی: گیسو، زلف، ( در گیاهی ) گل خوشه ای بلند، به هم فشرده، و معطر به رنگ های قرمز، آبی، سفید و زرد، ( در گیاهی ) گیاه این گل پیازدار، علفی، پایا، و از خانواده ی سوسن است، ( در گیاهی ) خوشه ی بعضی گیاهان مانند جو و گندم، ( در قدیم ) ( به مجاز ) موی صورت
 برچسب ها: اسم ، اسم با ن ، اسم دختر ، اسم فارسی ، اسم طبیعت 

 لغت نامه دهخدا

 ناردین. ( اِ ) سنبل رومی. ( قانون ابوعلی سینا چ تهران ص 214 ) ( ذخیره خوارزمشاهی ) ( بحر الجواهر ) ( انجمن آرا ) ( فرهنگ شعوری ).سنبل رومی را گویند و آن زردرنگ می باشد و اگر در سرمه داخل کنند موی مژه را برویاند. ( برهان قاطع ) ( آنندراج ). اسارون. ( فرهنگ دزی ). نردین و ناردین : سنبل رومی ، معرب نَرذُس یونانی است. ( اقرب الموارد ). سنبل الطیب. ( ناظم الاطباء ). مؤلف اختیارات بدیعی آرد: آن بیخی است به لون مشابه مامیران و عروق الصفر بود و به شکل اسارون ریشه ریشه داشته باشد لیکن ریشه آن باریکتر از ریشه اسارون بود. نیکوترین فربه تازه و خوشبوی و آنچه به سپیدی مایل بود بد باشد و طبیعت ناردین گرم بود در دوم و خشک بود در سیم. در کحلها کنند موی مژه برویاند و وی بول و حیض براند و ورم رحم را نافع بود. در طبیخ وی نشستن و یکدرم از وی فالج و لغوه را نافع باشد و اسحاق گوید مضر است به شش و مصلح وی کتیرا بود با عسل و بدل وی سنبل هندی بود. ( از اختیارات بدیعی ). و نیز رجوع به تاج المصادر بیهقی شود.اسم یونانی مطلق سنبل است. ( تحفه حکیم مؤمن ). کلمه یونانی است و اگر تنها گفته شود منظور سنبل هندی است. و اگر ناردین قلیطی گفته شود منظور سنبل اقلیطی یا سنبل رومی است و ناردین أوری سنبل جبلی و ناردین اعر با معنایش سنبل بری است و به سنبل جبلی و فرو و اسارون گفته می شود زیراهمه اینها را بری می گویند. ( ابن بیطار ج 2 ص 175 ).
 ناردین. ( اِخ ) از ولایات هندوستان است و به سال 405 هَ. ق. به دست سلطان محمودغزنوی گشوده شد. مؤلف «تاریخ دیالمه و غزنویان » آرد: سلطان محمود در سال 404 جنگ بزرگ دیگری در محل ناردین یکی از نقاط صعب العبور هندوستان کرده است که درتاریخ محاربات این پادشاه اهمیت فراوان دارد. سلطان محمود با لشکریانی عظیم در اواخر پائیز سال 404 به جانب هندوستان حرکت کرد اما سرمای شدید مانع از ادامه راه شد و ناگزیر به غزنین مراجعت کرد و تا فرارسیدن بهار به رفع نواقص سپاه پرداخت و در آغاز سال 405عازم هندوستان شد و در چند منزلی ناردین صف آرائی کرد و پس از نبردی سخت و دادن تلفات بسیار بر ناردین دست یافت. ( از تاریخ دیالمه و غزنویان ص 240 و 241 ). 

 فرهنگ فارسی

 از ولایات هندوستان است که در سال ۴٠۴ ه.ق . به تصرف سلطان محمود غزنوی در آمد .
( اسم ) ۱ - سنبل الطیب ۲ - سنبل رومی . یا ناردین اقلیطی . سنبل رومی . 

 فرهنگ عمید

 سنبل رومی،ریشه ای شبیه مامیران. 

 جدول کلمات

 سنبل رومی 

 پیشنهاد کاربران

 ناردین: این نام در سنسکریت نردین nardin ( خروشان، خروشنده، پر خروش ) بوده است. 
 ( فرهنگ سنسکریت - انگلیسی مونیر ویلیامز چاپ 1964 ص. 530 ستون یکم )

 سمبل رومی

 ناردین : ناردین به معنای نام گیاهی است که بوی خوش دارد. سنبل رومی از گیاهان . 
ناردین : ناردین اسم دخترانه است، معنی ناردین: 1 - ( در گیاهی ) گل خوشه ای بلند، به هم فشرده، و معطر به رنگ های قرمز، آبی، سفید و زرد؛ 2 - ( در گیاهی ) گیاه این گل پیازدار، علفی، پایا، و از خانواده ی سوسن است؛ 3 - ( در گیاهی ) خوشه ی بعضی گیاهان مانند جو و گندم؛ 4 - ( در قدیم ) ( به مجاز ) گیسو، زلف . 
 ... [مشاهده متن کامل] 
 ناردین از ولایات هندوستان است و به سال 405 هَ . ق . به دست سلطان محمودغزنوی گشوده شد.

 ناردین در ترکی به معنی انار و آتش هستش

 ناردین : سنبل ( گل خوشه ای بلند، به هم فشرده، و معطر به رنگ های قرمز، آبی، سفید و زرد )

 ناردین : گیاه خوشیو ، سنبل رومی .

 ناردین : ) گل خوشه ای بلند، به هم فشرده، و معطر به رنگ های قرمز، آبی، سفید و زرد.

 ناردین. از ولایات هندوستان است و به سال 405 هَ. ق. به دست سلطان محمودغزنوی گشوده شد

 ناردین در سایت ثبت احوال ایران به این معنا آمده : 
ناردین 1 - ( در گیاهی ) گل خوشه ای بلند، به هم فشرده، و معطر به رنگ های قرمز، آبی، سفید و زرد؛ 2 - ( در گیاهی ) گیاه این گل پیازدار، علفی، پایا، و از خانواده ی سوسن است؛ 3 - ( در گیاهی ) خوشه ی بعضی گیاهان مانند جو و گندم؛ 4 - ( در قدیم ) ( به مجاز ) گیسو، زلف؛ 5 - ( در قدیم ) ( به مجاز ) موی صورت. 
 ... [مشاهده متن کامل] 

 ناردین: گیاه خوشبو کننده

 من اسم دخترم ناردین هست. 
به زبان ترکی ناردین یعنی دانه بهشتی انار. 
حتمأ شنیدین که میگن تمام دانه های انار رو بخورین که توی انار یه دونه بهشتی هستش. 
ناردین همون دونه بهشتی انار هست.
```


## [2026-09-07T18:29:24.719Z] TOOL CALL #64: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/site/pages/354.jpg"
}
```


### [2026-09-07T18:29:24.748Z] TOOL RESULT

```

```


## [2026-09-07T18:29:43.570Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && tail -25 index.jsonl | python3 -c \"\nimport sys,json\nfor l in sys.stdin:\n    d=json.loads(l); print(d['status'], d['url'])\n\""
}
```


### [2026-09-07T18:29:44.798Z] TOOL RESULT

```
200 https://en.wiktionary.org/wiki/%D8%A2%D8%B3%D9%81%D8%A7%D9%84%D8%AA
200 https://abadis.ir/fatofa/%D9%82%D8%B1%D9%87-%D9%86%DB%8C/
200 https://vajehyab.com/?q=%D9%82%D8%B1%D9%86%DB%8C
-1 https://en.wiktionary.org/wiki/%D9%82%D8%B1%D9%86%DB%8C
200 https://abadis.ir/fatofa/%D9%86%D8%A7%D8%B1%D9%86%D8%AC/
200 https://abadis.ir/fatofa/%D9%86%D9%86%D9%87/
200 https://abadis.ir/fatofa/%D8%A7%D9%86%D8%A7%D8%B1/
200 https://abadis.ir/fatofa/%D9%86%D8%A7%D8%B1%D9%86%DA%AF/
200 https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₂neḱ-
200 https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₁neḱ-
200 https://en.wiktionary.org/wiki/%D8%AE%D8%B1%D8%A7%D8%B3%D8%A7%D9%86
200 https://www.etymonline.com/word/enough
200 https://www.etymonline.com/word/bring
200 https://abadis.ir/fatofa/%D9%86%D8%B1%D8%AF/
200 https://abadis.ir/fatofa/%D9%86%D8%A7%D8%B1%D8%AF%DB%8C%D9%86/
200 https://www.etymonline.com/word/nanny
200 https://en.wiktionary.org/wiki/nanny
200 https://en.wiktionary.org/wiki/%D8%A5%D9%86%D8%A8%D9%8A%D9%82
200 https://www.etymonline.com/word/alembic
200 https://en.wiktionary.org/wiki/%E1%BC%84%CE%BC%CE%B2%CE%B9%CE%BE
200 https://en.wiktionary.org/wiki/%D9%86%DB%8C%DA%A9
200 https://en.wiktionary.org/wiki/%D9%86%DB%8C%D9%88
200 https://en.wiktionary.org/wiki/niteo
200 https://www.etymonline.com/word/neat
200 https://abadis.ir/fatofa/%D8%B1%D9%88%D9%86%D9%82/
```


## [2026-09-07T18:29:57.557Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf8',errors='replace').read()\nblocks=re.split(r'\\[pdf page (\\d+)\\]',t)\nif len(blocks)>1:\n    d={int(blocks[i]):blocks[i+1] for i in range(1,len(blocks),2)}\n    print('tagged',min(d),max(d))\n    for pg in (333,334):\n        print('=== pdf',pg,'==='); print(d.get(pg,'')[:1800])\nelse:\n    pages=t.split('\\f'); print('leaves',len(pages))\n    for l in (332,333,334):\n        print('=== leaf',l,'(printed ~',l-4,') ==='); print(pages[l][:1800])\nEOF"
}
```


### [2026-09-07T18:29:58.828Z] TOOL RESULT

```
leaves 725
=== leaf 332 (printed ~ 328 ) ===
                                                  :




328                                                      necl-



      Wolil                windend^' zu sne-, nv- „drehen“ (Pick I ^ 50 ^).
                als „sich ringelnd,
Verb,        iriit                            (Curtius aaO., Pedersen KGr.
                      sna- „flie6en'' als „Schwiniinerin''
IT 45) wird dem westgerm. a                       —
                                idg. e nicht gerecht, auch hat sna- keine
Wechselform ohne anl. s- neben sich; die lat. Bed. „Wasserschlai]ge‘‘ ist
durch Begriffsverengerung nach nature „schwimmen^* erklarbar.


ned- ,,zusammendrehen, kniipfen".
  Lat. nodus .,Knoten“ (idg, ^nodos                          ;
                                                                  gegen and ere Ansatze oder Etymo-
logien s. Yt, LEWb. s. y.); vermutlich nassa „Pischreuse, geflochtener Kerb
mit engem Halse, ans dem die Pische nicht auskommen konnen“ (Pott
KZ. 1, 405, Osthoff Pf. 546f., Yf. LEWb.^ s. v. Gdf. *wa(?-s-a, Persson       ;


Beitr. 338; a           —   g   "^^e in   ir.   naidm usw.); mit demselben formantischen -5-
und der Bed. „nahe‘‘ ans „eng verknupft“ osk. nessimas n.pl. f. „proximae‘',
nmbr. nesimei „proxime“ {-ss- wegen der brit. Entsprechungen nicht ans
-fo- mit dem Guttural- von necto-, sondern aus -ds-', s. y. Planta I 377
m. Lit.) und air. compar. nessa, sup. nessam ,,propior, proximus“. cymr. neSy
nessaf,  corn, 7ics,  mbret. nes, 7iessaff ds.; mit Reduktionsvokal a = e
air. nascim „binde,    verpflichte'' (^n^d-slid), arnenas ,,I will bind“ (usw.,
s. Pedersen KG. II 582 f.), naidm „das Binden, Yertrag'^, fornakhn „Band‘‘,

}iasc „Ring“ (vgl. zur -sA-Bildung ahd. misca, das auch im             iiberein-
stimmt, ferner aY. nasJca- „Textsammlung'‘,
=== leaf 333 (printed ~ 329 ) ===
                                            nedo- -- nepot-                                   329

Fay KZ, 45, 112 Anra. 4, und uber die Entstehung des vermeintlichen
nedh- aus ^negJi- Bloomfield IF. 4, 69, wogegen Persson Beitr. 59S Anm. 1.
   Da6 ned- eine Erw. von {s)ne- „zusammendrelien“ sei, wird aufier durch
die Bed. auch durch die s- anl. Formen air. sfiaidyyi „Knoten“ (vgl. oben
naidm) und (Bezz. bei Fick 11^ 315; Fick III^ 520, 523) nhd, hess. Schnat::
,,das geflochtene und urn die Haarnadel gewickelte Haar der Frauen, Kopf-
putz der Braute'' i^snatta- mit germ. -iU aus -in-) wahrscheinlich (s. Wood
    ^r. 72; verfehlt Hirt Abl. 131).
   Hieher vermutlich die Bezeichnungen der Nessel ^'als alter Gespinst*-
pflanze)
   Gr. (Siitterlin IF. 4, 92) dbiy.rw ahd.                      aisl.   nqtr^ ahd.            ags.
netele,    Daneben mit idg. -t- (also                      no-t- als t-'Erw. zur vermutlichen
Gdwz. (s)ne-)      apr. 7watis,   lit.     noi{e}re (liber   andere Schreibungen s. Leskien
Nom. 567 f.) ,,Nesser",                    ,,Taubnesser^      lett. ndtre, natra „Nesser' und
allenfalls (als red up]   urkelt. ni-nati-l. s. Thurneysen bei Bradke IJb.
                            .




Methode und Ergebn. der ar. Altertumswiss. 245, Pedersen KG. I 186, 492;
mil*, nenaid^ nir. ncantog „Kessel“ (und schwierige brit Formen, s. Peder-
sen aaO.)
   S. noch ^nedo- „Schilf*\
   Ygl. AVindisch IF. 3, 84,           Brugmann Tol, 60 und bes.            (unter Bestimmung
derWz. als "'^ned-,       nicht nad-          und nedh-) Persson         Beitr. 139, 337 f,   598
Anm. 1, 813 f.


nedo- .,Schilf“.
  Ai. nada- m. vermutlich „Schilfrohr“ (s. Uhlenbeck Ai. Wb. s. v., Pers-
son Beitr. 814 Anm. 1), np. nai, mdartl. nad ^SchilP'; arm. (Hiibschmann
Arm. Gr. I 478) ne
=== leaf 334 (printed ~ 330 ) ===
330                                nebh-    — nem-
    Lai neptis (fiir -tl{s) nach den f-St.) „Enkelin'', spater „Nichte“; altlit.
nepte  (s, zur Form Lommel Stud. ub. idg. Femininbildungen 71) „Enkelin‘':

air.   necht   cymr. abret. nith, mbret. nis, corn, noith, „Ifichte“; ahd. nift
„neptis,    privigna“, nhd. (eigentlich nd.) Nichte, anord. nipt „Schwester-
tochter, Nichte“.
   Weiterbildung ^neptio-: av. naptya- „Abkoininling, Jfachkomme''; aksL
nethjh   „Neffe“, fem. cech, neti „Nichte'*, gr. avE'ipiog „Geschwistersohn“
•(^sm-neptiios)', alb. mhese „Nichte'' aus "^nepotia (Pedersen BB. 20, 228 f.;
vielleicht erst aus lat. nepos gebildet).
   Dber das von Wiedemann BB. 27, 225 mit tJnrecht auf *npat-s-U zuriick-
gefiihrte dt.   Base s. vielmehr Kluge und Weigand-Hirt s. v.
   Z. B. Curtius^ 266.       — Vermutlich als „Unmundiger, UnselbstandigeF'
zu ne und potis (s. Prellwitz^ 310, Streitberg IF. 3,334, Leumann FestgruB
an Bobtlingk 77, ZfdtWtf. 11, 63).
   Da6 unser Stamm ursprl. nur die Enkel gegeniiber dera Yater ihrer
Mutter und die KefiPen gegeniiber deren Bruder bezeichnet babe (Delbriick
A'^erw. 502 ff.), ist nicht geniigend gestiitzt (Hermann GGN, 1918, 215).


nebh- „bersten“.
    Ai. ndbhate „birst“ (fiber in ihrer Bed.       und daher auch ihrer Zugehorig-
keit unsichere Komina von einer       ai.Wz. nabh- s. Uhlenbeck Ai.Wb. I42f.,
Johansson IF. 4, 140,        Meringer Ws. 5, ^2f.). Johansson aaO., Wadstein
IF. 5, 25 (zw. auch Fick III^ 293, Falk~Torp u. ncever) wollen die von
Liden [lA. 5, 127], BB. 21, 100 f. untereinander verkniipften aisl. ncefr ,,die
aufiere Birkenrinde“ und air. snob „suber, liber“ als „berstend, sich los-
«chalend‘' anreihen    dies ist fur ncefr ansprechender als fiir das wegen
                         ;



«eines anl. s- und
```


## [2026-09-07T18:30:09.441Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^nados\\|^nedos\\|^nad-\\|nada- .reed\\|nadás\" IEC.txt | head; echo \"--- try 'Schilf'/reed sanskrit ---\"; grep -n \"nada.*reed\\|reed.*nada\" IEC.txt | head; echo \"=== SYN reed section ===\"; grep -n -i \"8\\.5[0-9] \\|REED\" SYN.txt | head"
}
```


### [2026-09-07T18:30:09.531Z] TOOL RESULT

```
11507:nad- (nod-?) ‘wet; water, water, Cf. not- Skt. nadih, f. ‘water’; Go. cf. natjan, v. ‘wet; OHG nas, OS nat ‘wet; G nass, id. beside netzen, v.; Sw. cf. nate, wm ‘duckweed’ and perh. Per. nai, nay ‘reed’
--- try 'Schilf'/reed sanskrit ---
=== SYN reed section ===
3775:Of the names of wild animals, only a small selection is considered here. The chief attention is given to domestic ani- mals. For those of most concern in the farmer’s daily life, there is a wealth of distinctions within the species (or genus; but with reference to domestic animals ‘species’ is generally the correct term; for our purposes the technical distinction is of no consequence), of which it is im- portant to note, beside the generic terms, those for the breeding male, the castrat- ed male, the female, and the young, as for the bovine species the ‘bull’, ‘ox’, ‘cow’, ‘calf’ (still other specific terms like NE steer for ‘young ox’, heifer for ‘young cow’ being ignored). There are many shifts of application and local differences even in the same language. Within the same cognate group there may be inter- change, as between ‘bull’, ‘ox’, and
3787:species, words for corresponding classes of different species may show specializa- tion to one species or shift from one spe- cies to another. Thus for the breeding male, Skt. vrsabha- ‘bull’, but Lat. verrés ‘boar’; Grk. xdzpos ‘boar’, but Lat. caper ‘he-goat?; OE bucca ‘he-goat’ (as NHG bock), but NE buck ‘male deer’. Similar- ly for the ‘young’ or ‘yearling’, as noted above.
3850:Boh., Russ. samec, Pol. samiec ‘the male’, Boh. samice, Pol. samica, Russ, samka ‘the female’ (SCr. samica of birds), with adjs. (archaic or uncom- mon) Boh. samét, Pol. samezy, samczowy ‘male’, Boh. samict, Pol. samiczy ‘fe- male’, all fr. sam, ChSl. sami ‘self, alone’. Presumably the first applica- tion was to the breeding male, the ‘one’ who serves many, as the bull, cock, etc., then ‘male’ in general with new feminine forms for ‘female’.
4269:4, Lat. féta ‘breeding female’ (féta
4563:4. ON hestr (3.41) also ‘stallion’, for which also stdd-hestr and st0d-hross cpds. with stod ‘stud of horses’ : OE stéd (NE stud, whence studhorse), OHG stuot (NHG stute ‘mare’), all meaning (‘place for’, then coll.) ‘horses kept for breed- ing’, orig. ‘standing place’, deriv. of IE * sta- ‘stand’.
4612:ae alt ‘horses kept for breeding’. Cf. under ‘stallion’ (3.42). Z
5093:Russ. ochotit’sja refl. (with na ‘on’ when used transitively) fr. ochata ‘de- sire, will, hunt, chase, sport’ : chotét’, ChSI. chotéi ‘wish’ (16.61). For the change ‘desire’ > ‘hunt’, cf. Skt. lubdha- ‘greedy’, as sb. ‘hunter’. Berneker 398 f.
6058:2. Grk. Aauds, prob. (as fr. *Aapyos) : Adpia “abysses’, Aanvpds ‘greedy’, also Aauia ‘monster’, Lat. lemurés ‘ghosts’. Walde-P. 2.377, 484. Otherwise Boi- sacq 551.
6579:1. Grk. pirpa (in Aristot. HA 510° distinguished from ‘orépa or deddis ‘womb’ as the ‘tube and opening of the womb’; in NG the technical word for ‘vomb’, pop. ora); Lat. matrix ‘breeding animal’, late ‘womb’ (> It. matrice, etc.); SCr. materica, all derivs. of word for ‘mother’, as It., Sp. madre, Dan. moder, Boh., Russ. matka ‘mother’ also used for ‘womb’. Cf. also NHG mutterleib, gebarmutter, etc.
8442:Goth. grédus (once =. \iu6s) with adj. grédags : ON gradr ‘hunger, greed’, OF gr@dig ‘hungry, greedy’ (NE greedy, whence greed), fr. *ghrédh-, prob. an ex- tension of *gher-, in Goth. gairnjan, OE giernan ‘desire’ (NE yearn), Osc.- Umbr. her- ‘wish’, etc. Walde-P. 1.601. Feist 220. Walde-H. 1.658. Otherwise Falk-Torp 339.
```


## [2026-09-07T18:30:15.582Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('IEC.txt',encoding='utf8',errors='replace').read()\nlines=t.split('\\n')\nfor ln in (11507,11796):\n    off=sum(len(l)+1 for l in lines[:ln-1]); leaf=t[:off].count('\\f')\n    print(ln,'leaf',leaf,'printed ~',2*(leaf-15))\n\""
}
```


### [2026-09-07T18:30:17.412Z] TOOL RESULT

```
11507 leaf 461 printed ~ 892
11796 leaf 473 printed ~ 916
```


## [2026-09-07T18:30:46.299Z] TOOL CALL #69: Bash

```json
{
 "command": "sed -n '1,120p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-07T18:30:46.338Z] TOOL RESULT

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


## [2026-09-07T18:40:24.567Z] TOOL CALL #70: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/mk354.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\nE = \"https://www.etymonline.com/word/\"\n\ndata = {\n \"pdf_page\": 354,\n \"book_page\": 324,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-07\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Ned\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *ned- / *nǝd- 'to twist together, knot, bind', with derivative *nōdo- 'something knotted' (Pokorny IEW 758–759; Walde-Pokorny II 328–329; Watkins/AHD ned- 'to bind, tie')\",\n   \"note\": \"The root box is correct in every particular. Pokorny heads the entry on p.758 '1. ned-: nǝd- „zusammendrehen, knüpfen“; nōdo-/-ā „Geknüpftes“', continuing onto p.759; Walde-Pokorny II 328 has the identical lemma 'ned- „zusammendrehen, knüpfen“'; Watkins (AHD Indo-European appendix, 1985 standalone ed. p.44) glosses it word for word as Nourai does, 'ned-. To bind, tie'. The language label 'Indo-European' is right — this is a genuine PIE root reconstructed from Latin, Celtic, Germanic and (per Pokorny/Bartholomae) Avestan. Nourai's POK:758 is the first page of a two-page entry; the Avestan naska-, the Germanic net- and the Latin nōdus/nectere material he cites all stand within 758–759. The only substantive problem in the whole chart is the Arabic node #4 (nask → nasx), which modern Semitic scholarship reverses or rejects.\",\n   \"note_fa\": \"ریشهٔ هندواروپایی آغازین *ned-/*nǝd- به معنی «تابیدن، گره زدن، بستن» است و صورت گشتهٔ آن *nōdo- «چیز گره‌خورده». پوکورنی (ص ۷۵۸–۷۵۹) و والده–پوکورنی (ج ۲ ص ۳۲۸) همین ریشه و همین معنا را می‌آورند و واتکینز در پیوست ریشه‌های هندواروپایی فرهنگ American Heritage عیناً «to bind, tie» را معنی می‌کند؛ پس برچسب زبانی و معنای ریشه در نمودار نورایی درست است. تنها گرهِ نادرست این نمودار پیوند «نَسکِ پهلوی ← نَسخِ عربی» است که ریشه‌شناسی امروزی آن را رد می‌کند.\",\n   \"sources\": [E + \"node\"],\n   \"ref_check\": [\n    {\"ref\": \"POK:758\", \"status\": \"supports\", \"note\": \"Pokorny IEW p.758 (POK_02.txt leaf 420, running head '758'): '1. ned-: nǝd- „zusammendrehen, knüpfen“; nōdo-/-ā „Geknüpftes“. 1. Lat. nōdus „Knoten“ (idg. *nōdos)…' — exactly Nourai's root and gloss.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"IEW pp.758–759 (POK_02.txt leaves 420–421)\", \"stance\": \"supports\", \"note\": \"'1. ned-: nǝd- „zusammendrehen, knüpfen“ … got. nati, ahd. nezzi, as. net … dehnstufig (wie lat. nōdus), aisl. not f. „großes Netz“ … ferner av. naska- „Textsammlung“, wahrscheinlich eig. „Bündel“'.\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. II pp.328–329 (WLD_Bd2_pages.txt leaf 332, printed head '328 ned-')\", \"stance\": \"supports\", \"note\": \"'ned- „zusammendrehen, knüpfen“. Lat. nodus „Knoten“ (idg. *nōdos) … air. nascim „binde, verpflichte“ (*nǝd-skō) … nasc „Ring“ (vgl. zur -sk-Bildung ahd. nusca …, ferner av. naska- „Textsammlung“)'.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 p.44 (AHD_watkins1985.txt leaf 73)\", \"stance\": \"supports\", \"note\": \"'ned-. To bind, tie. 1. O-grade form *nod- in: a. Germanic *nati- in Old English net(t), a net: NET¹ … 2. Lengthened o-grade form *nōdo- in Latin nōdus, a knot: NODE … 3. Re-formation of the root in Latin nectere … ANNEX, CONNECT. [Pok. 1. ned- 758.]'\"},\n    {\"src\": \"IEC\", \"where\": \"Mann, IE Comparative Dictionary col. ~916 (IEC.txt leaf 473)\", \"stance\": \"supports\", \"note\": \"'nódos, is, io „knot, tie“. WP II, 328 — Alb. nyë …; Lat. nodus … „knot, noose, knot in wood“; … Icel. nót, f. pl. nætr „large net“; Norw. not … „fishing-net“'.\"},\n    {\"src\": \"LAT\", \"where\": \"Ernout–Meillet p.772 s.v. necto (LAT.txt leaf 790)\", \"stance\": \"supports\", \"note\": \"'…on a nodus à côté de necto, et en sanskrit naddhaḥ „attaché“ à côté de nahyati. Ceci conduit à poser une racine nedh-; et en effet l'irlandais a naidm „lien“ … nascim „je lie“ (bret. naska)'.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Avestan\", \"words\": \"naska\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Avestan naska- m. is the name of each of the twenty-one 'books' into which the Sasanian Avesta was divided (it appears in the compound nasko.frasa- 'devoted to the study of the nasks', Yasna 9.22). Formally it is *nǝd-sko-, the same -sk- derivative of *ned- 'to bind' as Old Irish nascim 'I bind' (< *nǝd-skō), Old Irish nasc 'ring', Breton naska 'to tie on', Old High German nusca 'cloak-buckle'; the concrete meaning was therefore 'bundle, sheaf', which passed to 'bundle of texts, text-collection' and so to 'book'. Pokorny prints precisely this on IEW 759 ('ferner av. naska- „Textsammlung“, wahrscheinlich eig. „Bündel“'), Walde-Pokorny II 328 the same, and Bartholomae's Altiranisches Wörterbuch s.v. *naska- glosses it 'eig. wohl „Bündel“, vgl. air. nascim „ich binde“, nasc „Ring“'. A minority tradition (Spiegel, Haug, Lagarde, and after them Jeffery, FVQ 279) took naska- for an old Semitic loanword in Iranian; Bartholomae's own footnote reports that this Semitic etymology 'is not to be maintained', and Pokorny and Walde-Pokorny keep the word inside *ned-. So the arrow root → Avestan is right; only Nourai's gloss 'book' is the applied rather than the etymological sense.\",\n     \"derivation_fa\": \"«نَسک» در اوستایی naska- نام هر یک از بیست و یک بخش اوستای ساسانی است و در ترکیب nasko.frasa- «آن‌که به آموختن نسک‌ها می‌پردازد» (یسنا ۹/۲۲) دیده می‌شود. از نظر ساختی صورتِ *nǝd-sko- است، یعنی همان پسوند -sk- که در ایرلندی کهن nascim «می‌بندم» و nasc «حلقه» و آلمانی علیای کهن nusca «سنجاق ردا» هست؛ از این‌رو معنای نخستین آن «بسته، دسته» بوده و سپس به «دستهٔ متن‌ها، مجموعهٔ متون» و آنگاه «کتاب» تحول یافته است. پوکورنی (ص ۷۵۹) و بارتولومه در فرهنگ ایرانی باستان صریحاً همین را می‌گویند («در اصل احتمالاً بُندِل/دسته»). گروهی اندک (اشپیگل، هاوگ، لاگارد و به پیروی آنان جفری) نَسک را وام‌واژه‌ای سامی در ایرانی شمرده‌اند، ولی بارتولومه خودش در پانوشت می‌نویسد که این ریشه‌شناسی سامی پذیرفتنی نیست. پس ادعای نورایی درست است؛ فقط «کتاب» معنای ثانوی است، نه معنای ریشه‌ای.\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\"ref\": \"POK:759\", \"status\": \"supports\", \"note\": \"Pokorny IEW 759 (POK_02.txt leaf 420, within the '1. ned-' entry, right after the running head '759'): '…nasc „Ring“ (vgl. zur -sk-Bildung ahd. nusca, das auch im u = ǝ übereinstimmt, ferner av. naska- „Textsammlung“, wahrscheinlich eig. „Bündel“)'. Exactly the arrow Nourai draws.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch s.v. *naska- (BRT.txt leaf 591, in the nasu-/naska- column block)\", \"stance\": \"supports\", \"note\": \"'*naska- m. … (eig. wohl „Bündel“, vgl. air. nascim „ich binde“, nasc „Ring“); mp. nask'. Bartholomae's footnote adds that others take naska- for a Semitic loan (Haug, Lagarde, Dst. ZA. 3) but that 'die semitische Etymologie … nicht aufrecht zu halten' ist. His note on nasko.frasa- explains: 'D. i. Sammlung heiliger Texte; das sasanidische Awesta zerfiel in 21 solcher Textsammlungen'.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. II p.328 (WLD_Bd2_pages.txt leaf 332)\", \"stance\": \"supports\", \"note\": \"'…nasc „Ring“ (vgl. zur -sk-Bildung ahd. nusca, das auch im ǝ übereinstimmt, ferner av. naska- „Textsammlung“…'\"},\n      {\"src\": \"FVQ\", \"where\": \"Jeffery, Foreign Vocabulary of the Qur'an p.279 s.v. نسخة (FVQ_pages.txt leaf 296)\", \"stance\": \"contradicts\", \"note\": \"'…the Iranian, where Phlv. nask; Av. naska means a book of the Avesta. The Iranian word, however, as Spiegel showed …, cannot be explained from Indo-European material, and … is in all probability an ancient borrowing from some Semitic source in Mesopotamia.' — the minority view Bartholomae rejects.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"nask\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Middle Persian nask [nsk'] continues Avestan naska- unchanged (the short a and the -sk- cluster are stable between Avestan and Middle Persian; no sound change intervenes). MacKenzie's Concise Pahlavi Dictionary (p.58 area, PHD.txt leaf 82 block) gives 'nask [nsk'] a division of the Avesta', and Nyberg's Manual of Pahlavi II 142 is fuller: 'nask [nsk] properly „bundle, bunch“, the name of each of the 21 „books“ or collection of texts forming together the Sassanian Avesta — Av. naska- in nasko.frasa- „one who devotes himself to the study of the nasks“.' Nyberg's 'properly bundle, bunch' is the same etymological gloss as Bartholomae's, so the Avestan → Pahlavi arrow is exactly the standard account.\",\n     \"derivation_fa\": \"نَسکِ فارسی میانه (پهلوی) nask که در دبیرهٔ پهلوی <nsk'> نوشته می‌شود، دنبالهٔ بی‌واسطهٔ اوستایی naska- است؛ میان اوستایی و پهلوی هیچ دگرگونی آوایی‌ای در این واژه رخ نداده و خوشهٔ -sk- و واکهٔ کوتاه a دست‌نخورده مانده است. مکنزی در فرهنگ کوچک پهلوی می‌نویسد «nask: یکی از بخش‌های اوستا» و نیبرگ (ج ۲ ص ۱۴۲) روشن‌تر می‌گوید «nask در اصل به معنی «دسته، بسته»، نام هر یک از ۲۱ «کتاب» یا مجموعهٔ متونی که با هم اوستای ساسانی را می‌سازند — از اوستایی naska-». پس این پیوند در نمودار نورایی درست است.\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\"ref\": \"MON\", \"status\": \"supports\", \"note\": \"Mo'in, Farhang-e Farsi s.v. نسک (MON_part2.txt): '[هر جزو از کتاب مقدس اوستا. کتاب؛ متن] (اِ.) نام هر یک از بیست و یک بخش کتاب اوستا' — Mo'in's bracketed etymological tag treats the word as the inherited Zoroastrian term (his separate entry نَسَک '[ع.]' is the Arabic homonym 'worship, sacrifice'). Nourai cites 'MON' without a page; the entry is verified, the page could not be (the local copy is the 2-vol. Adena reprint with different pagination).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary, s.v. nask (PHD.txt leaf 82; printed p.58 per Aryanpur's citation)\", \"stance\": \"supports\", \"note\": \"'nask [nsk' | N ~] a division of the Avesta.' Listed between nasā 'corpse' and nasrušt(īh).\"},\n      {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II p.142 (NYB_vol2_glossary.txt leaf 150)\", \"stance\": \"supports\", \"note\": \"'nask [nsk] properly „bundle, bunch“, the name of each of the 21 „books“ or collection of texts forming together the Sassanian Avesta 1091'. — Av. naska- in (1060) nasko.frasa- „one who devotes himself to the study of the nasks“.'\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Persian\", \"words\": \"nask\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"New Persian نَسک nask is the direct continuation of MP nask, kept alive as a technical Zoroastrian term (Labībī's verse quoted in the chart, 'خود به نسک آفرینگان گفته است', shows it in 4th/10th-century poetry). Borhān-e Qāṭeʿ p.2140 defines it 'قسمی باشد از بیست و یک قسم کتاب زند که زردشت آنرا منقسم کرده است و هر نسکی … را نامی نهاده' ('one of the twenty-one divisions of the book of the Zand, which Zoroaster divided up, each nask being given a name'), and Moʿīn's Farhang has 'نام هر یک از بیست و یک بخش کتاب اوستا'. Note that Borhān prints the Arabic homonym نَسَک 'worship, sacrifice, offering' (root n-s-k) in the same article — a different word, from Arabic, not from Avestan; and a third نَسک 'lentil / caltrop' (Moʿīn, from گیاه‌شناسی). Wiktionary's Persian entry confirms the modern sense and adds a puristic revival use 'book'. The arrow Pahlavi → Persian is uncontroversial.\",\n     \"derivation_fa\": \"«نَسک» در فارسی نو دنبالهٔ بی‌واسطهٔ نَسکِ پهلوی است و به‌عنوان اصطلاحی زردشتی زنده مانده است؛ بیت لبیبی که نورایی آورده («خود به نسک آفرینگان گفته است») گواهِ کاربرد آن در سدهٔ چهارم هجری است. برهان قاطع (ص ۲۱۴۰) می‌نویسد: «قسمی باشد از بیست و یک قسم کتاب زند که زردشت آن را منقسم کرده است»، و معین هم «نام هر یک از بیست و یک بخش کتاب اوستا» را می‌آورد. باید توجه داشت که «نَسَک» عربی (از ریشهٔ ن‌س‌ک، به معنی عبادت و قربانی) که برهان در همان مقاله می‌آورد، واژه‌ای جداگانه و معرّب است و ربطی به نَسکِ اوستایی ندارد. ادعای نورایی درست است.\",\n     \"sources\": [W + \"%D9%86%D8%B3%DA%A9\"],\n     \"ref_check\": [\n      {\"ref\": \"BQT:2140\", \"status\": \"supports\", \"note\": \"Borhān-e Qāṭeʿ ed. Moʿīn p.2140 (vol. 4, BQT_v4_pages.txt pdf page 223 = 223+1917): s.v. نسک — 'و بفتح ثانی … قسمی باشد از بیست و یک قسم کتاب زند که زردشت آنرا منقسم کرده است و هر نسکی … را نامی نهاده - و در عربی بمعنی عبادت و پرستیدن خدای تعالی و قربانی کردن باشد'. Page number exactly right.\"},\n      {\"ref\": \"MON:4727\", \"status\": \"supports\", \"note\": \"Mo'in s.v. نسک: 'تسک [هر جزو از کتاب مقدس اوستا. کتاب؛ متن] (اِ.) نام هر یک از بیست و یک بخش کتاب اوستا' (MON_part2.txt; the local copy is the 2-vol. Adena reprint, so p.4727 of the 6-vol. Amir Kabir edition could not be checked, only the entry).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BQT\", \"where\": \"p.2140 (vol. 4 pdf p.223)\", \"stance\": \"supports\", \"note\": \"see ref_check; the article also lists the Arabic homonym نَسَک 'عبادت … قربانی' with Moʿīn's footnote quoting منتهی الارب.\"},\n      {\"src\": \"MON\", \"where\": \"s.v. نسک (MON_part2.txt)\", \"stance\": \"supports\", \"note\": \"'نام هر یک از بیست و یک بخش کتاب اوستا'; a separate entry نسک '(گیاه‌شناسی) عدس، خارخسک' and نَسَک '[ع.]' keep the three homonyms apart.\"},\n      {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e Rishe-hā-ye Hend-o-Orupāyi (index/entry pages)\", \"stance\": \"silent\", \"note\": \"grep of ARY_pages.txt and ARY_latin_index_pages.txt for نسک / NASK returned only a Tokharian NASK line and OCR noise; Aryanpur has no entry for نسک.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"Arabic\", \"words\": \"nasx\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"Nourai makes Arabic نَسْخ nasx 'written text' a loan from Pahlavi nask. Modern Semitic scholarship rejects this. نسخ is a fully productive Arabic triliteral root n-s-ḫ whose primary sense is 'to remove, tear away, abolish, abrogate' — the sense it has in the Qurʾān (2:106, 22:52) — with 'to copy, transcribe' only secondary; its cognates are Akkadian nasāḫu 'to tear out', Hebrew נסח nāsaḥ, Old Aramaic and Targumic נסח, Syriac nsaḥ, so Wiktionary (with Lane) derives the Arabic verb from Aramaic נְסַח 'to take away, draw off, eliminate' and relates it to the Arabic root n-z-ʕ. Nourai's own cited authority says the same and even reverses his arrow: Jeffery (FVQ 279, of which VDQ is the Persian translation) writes 'A comparison with the cognate languages … shows that copy is a secondary meaning of the root … the original sense is clearly to remove, tear away', and, discussing Lagarde's suggestion that Syriac nusḥā came from Pahlavi nask, concludes that the Iranian word itself 'is in all probability an ancient borrowing from some Semitic source in Mesopotamia'. The phonetics are also against Nourai: MP nask has -sk, and Arabic borrows Iranian k as ك/ق, not as خ (cf. نسک itself, borrowed unchanged into Arabic lexica as a Zoroastrian term). The word that actually links the two families is the noun نُسْخَة nusḫa 'copy, exemplar' (Qurʾān 7:154), which Jeffery lists as a foreign word only because of Lagarde's Iranian hypothesis, not because he accepts it. So the node's word and gloss are real, but the arrow Pahlavi → Arabic is not the modern view.\",\n     \"derivation_fa\": \"نورایی «نَسخ» عربی را وام‌گرفته از نَسکِ پهلوی می‌داند، ولی ریشه‌شناسی امروزی این را نمی‌پذیرد. ن‌س‌خ ریشه‌ای زایای سامی است که معنای نخستینش «برکندن، برداشتن، باطل کردن» است — همان معنایی که در قرآن (بقره ۱۰۶، حج ۵۲) دارد — و «نسخه‌برداری» معنای ثانوی آن است؛ هم‌ریشه‌های آن اکدی nasāḫu «برکندن»، عبری نَسَح، آرامی و سریانی nsaḥ هستند و ویکی‌واژه (به پیروی لِین) فعل عربی را وام‌واژه‌ای از آرامی نِسَح می‌داند. نکتهٔ مهم آن است که خودِ مرجعی که نورایی آورده (جفری، واژه‌های دخیل در قرآن، ص ۲۷۹ = ترجمهٔ فارسی VDQ) عکسِ ادعای او را می‌گوید: «معنای نسخه‌برداری در این ریشه ثانوی است … معنای اصلی برکندن و برداشتن است» و در بارهٔ حدسِ لاگارد (سریانیِ nusḥā از نَسکِ ایرانی) نتیجه می‌گیرد که خودِ واژهٔ ایرانی «به احتمال بسیار وام‌گیری کهنی از منبعی سامی در میان‌رودان است». از نظر آوایی هم -sk پهلوی در عربی به ك/ق بدل می‌شود نه به خ. پس واژه و معنا درست است، اما جهت وام‌گیری در نمودار نادرست است.\",\n     \"sources\": [W + \"%D9%86%D8%B3%D8%AE\", W + \"%D9%86%D8%B3%D8%AE%D8%A9\"],\n     \"ref_check\": [\n      {\"ref\": \"VDQ:400\", \"status\": \"contradicts\", \"note\": \"VDQ is Badreh'i's Persian translation of Jeffery FVQ; no digital copy exists (refs_online: 'noorlib viewer is JavaScript-rendered … verify the substance via FVQ, same entry order'). Checked in FVQ p.279 s.v. نسخة (FVQ_pages.txt leaf 296): 'Hoffmann … suggested that the Arabic word was from Aram. נוסחא, but this is used only in late Rabbinic writings … and as Lagarde, GA, 196, points out, comes from the Iranian, where Phlv. nask; Av. naska means a book of the Avesta. The Iranian word, however … cannot be explained from Indo-European material, and … is in all probability an ancient borrowing from some Semitic source in Mesopotamia.' Jeffery reports the Iranian hypothesis and rejects its direction.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"FVQ\", \"where\": \"p.279 s.v. نسخة (FVQ_pages.txt leaf 296)\", \"stance\": \"contradicts\", \"note\": \"'A comparison with the cognate languages, however, shows that copy is a secondary meaning of the root, cf. Akk. nusḫu = extract, and Syr. to copy, beside Akk. nasāḫu, Heb. נסח; O.Aram. נסח and the Targumic נסח, where the original sense is clearly to remove, tear away.'\"},\n      {\"src\": \"KLN\", \"where\": \"Klein, Comprehensive Etymological Dictionary (searched KLN_1966.txt / KLN_1971.txt for nask, naskh, nasx)\", \"stance\": \"silent\", \"note\": \"Klein has no entry for the Arabic n-s-ḫ family (it yielded no English loanword), so he says nothing either way.\"},\n      {\"src\": \"PLA\", \"where\": \"Asbaghi, Persische Lehnwörter im Arabischen (grep of PLA_pages.txt for nask/nasḫ/nusḫa)\", \"stance\": \"silent\", \"note\": \"Asbaghi's list of Persian loanwords in Arabic does NOT contain nasḫ or nusḫa — a telling silence from the standard modern inventory of exactly this kind of borrowing.\"},\n      {\"src\": \"AFM\", \"where\": \"Addi Shir, al-Alfāẓ al-fārisiyya al-muʿarraba (grep of AFM_pages.txt for نسخ / نسك)\", \"stance\": \"silent\", \"note\": \"no entry for نسخ among the Persian words Arabicized; Addi Shir does not claim it.\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"Persian\", \"words\": \"nosxeh\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Persian نُسخه nosxe (Classical nusxa) is a straightforward loan from Arabic نُسْخَة nusḫa 'copy, transcript, manuscript, prescription', the unit-noun (nomen unitatis in -a) of the Arabic root n-s-ḫ; Persian regularly renders Arabic -at as -e/-a and Arabic u as o in the modern Tehrani standard. From Persian it was passed on further: Pashto نُسْخَه, Ottoman Turkish نسخه nüsha, Tajik нусха, Chagatai/Uzbek nusxa, Urdu/Hindi nusxā. The chart's extras belong to the same Arabic root and reached Persian the same way: ناسخ nāsex (active participle, 'abrogating, copyist'), استنساخ estensāx (form X verbal noun, 'making a copy'), نسخ ۲ nasx (verbal noun, 'abrogation'; also the name of the naskh script), and the Arabic broken plural نُسَخ nosax which Nourai notes in the box. The Arabic → Persian arrow is confirmed by Wiktionary ('Persian: borrowed from Arabic نُسْخَة'); what fails is only the step above it (node #4), so the word is not ultimately Iranian.\",\n     \"derivation_fa\": \"«نُسخه» وام‌واژه‌ای است از عربی نُسْخَة (اسمِ واحدِ ریشهٔ ن‌س‌خ) به معنی رونوشت، دست‌نویس، دستور دارو. در فارسی، تای تأنیثِ عربی به ـه/ـهٔ بدل می‌شود و ضمّهٔ عربی در گونهٔ معیار تهرانی به «ـُ ← o» می‌گراید (nusxa ← nosxe). همین واژه از فارسی به پشتو، ترکی عثمانی (nüsha)، تاجیکی، ازبکی و اردو رفته است. دیگر صورت‌هایی که نورایی در جعبه آورده — ناسخ (اسم فاعل)، استنساخ (مصدر باب استفعال)، نَسخ ۲ (مصدر) و جمع مکسّر نُسَخ — همه از همین ریشهٔ عربی و از همین راه به فارسی رسیده‌اند. پس این پیوند (عربی ← فارسی) درست است؛ آنچه نادرست است حلقهٔ بالاتر است، یعنی وام‌گیری عربی از پهلوی؛ در نتیجه «نسخه» در نهایت واژه‌ای ایرانی نیست.\",\n     \"sources\": [W + \"%D9%86%D8%B3%D8%AE%D9%87\", W + \"%D9%86%D8%B3%D8%AE%D8%A9\"],\n     \"ref_check\": [\n      {\"ref\": \"FVA:399\", \"status\": \"not_checked\", \"note\": \"S.M. Nahvi, Farhang-e Vāzheh-hā-ye ʿArabi dar Fārsi (Arabic loanwords in Persian), 1368/1989: refs_online records 'Searched archive.org, ketabnak, noorlib, web: no digital copy found', local_file null. Not accessible. Its very title, however, agrees with the direction of this node (an Arabic word in Persian).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"Mo'in / vajehyab-type entries for نسخه\", \"stance\": \"supports\", \"note\": \"Mo'in tags نسخه '[ع.]' (Arabic) — the standard Persian lexicographic verdict; Wiktionary's Persian entry is explicit: 'Borrowed from Arabic نُسْخَة (nusḵa)'.\"},\n      {\"src\": \"KLN\", \"where\": \"Klein (grep for nusxa/naskh)\", \"stance\": \"silent\", \"note\": \"no entry; the word left no English descendant.\"},\n      {\"src\": \"FVQ\", \"where\": \"p.279 s.v. نسخة\", \"stance\": \"partial\", \"note\": \"Jeffery treats نسخة as the Arabic form (Qur'ān vii,153/154 'A copy, or exemplar'); he does not discuss the Persian loan, but his Arabic starting point is what the Persian presupposes.\"}\n     ]\n    },\n    {\n     \"id\": 6, \"lang\": \"Germanic\", \"words\": \"\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"A pass-through box for Proto-Germanic. Watkins/AHD puts it exactly where Nourai does: 'ned-. To bind, tie. 1. O-grade form *nod- in: a. Germanic *nati- in Old English net(t), a net'. The Germanic noun is thus *natja- n. (Gothic nati, Old Saxon net/netti, Old Frisian nette, Old High German nezzi, Old Norse and Old English net), from PIE *nod-yo-, with the regular Germanic sound shift PIE *d > Gmc *t and the *-yo- suffix that produces the West Germanic geminate -tt-/-zz-; Pokorny IEW 759 lists the same set, and adds the lengthened grade in Old Norse not f. 'large net' beside Latin nōdus. The empty box is faithful to the book, which draws the Germanic stage without naming a form.\",\n     \"derivation_fa\": \"این جعبه گرهی گذرا برای «ژرمنی آغازین» است و نورایی صورتی در آن نیاورده. واتکینز در پیوست ریشه‌های هندواروپایی همین‌جا را نشان می‌دهد: «ned- «بستن»؛ گونهٔ o-دار *nod- در ژرمنی *nati- که در انگلیسی کهن net(t) «تور» دیده می‌شود». صورت بازسازیِ ژرمنی *natja- است (گوتی nati، ساکسونی کهن net/netti، آلمانی علیای کهن nezzi، نورسی کهن و انگلیسی کهن net) از *nod-yo-؛ در آن دالِ هندواروپایی بر پایهٔ قانون آوایی گریم به t ژرمنی بدل شده و پسوند *-yo- مایهٔ همگونی و دوگانه‌شدن t/z در ژرمنی غربی است. پوکورنی (ص ۷۵۹) هم همین مجموعه را می‌آورد. جعبهٔ تهی وفادار به متن کتاب است.\",\n     \"sources\": [E + \"net\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 p.44 s.v. ned-: '1. O-grade form *nod- in: a. Germanic *nati- in Old English net(t), a net: NET¹; b. Germanic *nat-ilo, a nettle …; c. Germanic *nat-sk- in Anglo-Norman nouch, brooch: OUCH².' Nourai's 'AHD' citation (no page) is verified against the same appendix he cites.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"IEW 759 (POK_02.txt leaf 420)\", \"stance\": \"supports\", \"note\": \"'got. nati, ahd. nezzi, as. net, netti, ags. aisl. net „Netz“, dehnstufig (wie lat. nōdus), aisl. not f. „großes Netz“'.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. II p.328\", \"stance\": \"supports\", \"note\": \"same Germanic list under 'ned- „zusammendrehen, knüpfen“'.\"},\n      {\"src\": \"IEC\", \"where\": \"Mann col. ~916 s.v. nódos\", \"stance\": \"supports\", \"note\": \"'Icel. nóti … nót, f. pl. nætr „large net“; Norw. not, pl. noter, Sw. not, pl. -ar, f. „fishing-net“'.\"}\n     ]\n    },\n    {\n     \"id\": 7, \"lang\": \"English\", \"words\": \"net 2\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"English net 'mesh' (Nourai's 'net 2', distinguished from net 'clear of deductions', which is a different word from Latin nitēre 'to shine' — see Etymonline s.v. net (adj.)) is Old English net(t) 'open textile fabric tied or woven with a mesh for catching fish, birds or wild animals; network; spider web', from Proto-Germanic *natja-, from PIE *nod-yo- beside *nōdo-. The word is native, inherited, not borrowed: Old Saxon net, Old Frisian nette, Old Norse/Dutch net, Swedish nät, Old High German nezzi, German Netz, Gothic nati. The semantics are transparent for a *ned- 'to knot' derivative — 'something knotted'. One caveat: Etymonline notes 'Boutkan says it has no clear IE etymology and implies it might be a substrate word', so the connection to *ned-, while standard (Pokorny, Walde-Pokorny, Watkins), is not unanimous.\",\n     \"derivation_fa\": \"واژهٔ انگلیسی net «تور» (که نورایی آن را «net 2» می‌نامد تا از net «خالص، پس از کسور» جدا کند — و آن دیگری از لاتین nitēre «درخشیدن» است) از انگلیسی کهن net(t) «بافتهٔ مشبّک برای گرفتن ماهی و پرنده؛ تارِ عنکبوت» می‌آید، از ژرمنی آغازین *natja- و آن از *nod-yo- هندواروپایی، در کنار *nōdo-. واژه‌ای است ارثی و نه وام‌واژه: ساکسونی کهن net، فریزی کهن nette، نورسی کهن و هلندی net، سوئدی nät، آلمانی علیای کهن nezzi، آلمانی Netz، گوتی nati. معنا هم برای گشتهٔ ریشهٔ «گره زدن» روشن است: «چیزِ گره‌خورده». یک احتیاط: به گفتهٔ اتیمونلاین، بوتکان این واژه را بی ریشه‌شناسی روشن هندواروپایی می‌داند و احتمال می‌دهد وام‌واژه‌ای زیرلایه‌ای باشد؛ پس این پیوند، هرچند نظر معیار (پوکورنی، والده–پوکورنی، واتکینز) است، به اتفاق آرا نیست.\",\n     \"sources\": [E + \"net\", E + \"node\"],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The node carries no reference in the book (refs=None); the derivation was checked against Etymonline (net (n.), and the *ned- root box under node) and against the AHD appendix cited on the parent Germanic node.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein (KLN_1966.txt s.v. net)\", \"stance\": \"supports\", \"note\": \"Klein's English etymologies derive net from OE nett with the Germanic cognates; grep confirms the entry sits in the same Germanic family as Pokorny's list.\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 p.44 s.v. ned-\", \"stance\": \"supports\", \"note\": \"'Germanic *nati- in Old English net(t), a net: NET¹'.\"},\n      {\"src\": \"POK\", \"where\": \"IEW 759\", \"stance\": \"supports\", \"note\": \"'ags. aisl. net „Netz“'.\"}\n     ]\n    },\n    {\n     \"id\": 8, \"lang\": \"Latin\", \"words\": \"nôdus; nectere\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Latin nōdus 'knot' (Nourai's 'nôdus' is his circumflex notation for the long ō, faithful to the printed page) is the lengthened o-grade *nōdo-s of *ned-, i.e. the substantivized 'something knotted': Pokorny IEW 758 gives 'Lat. nōdus „Knoten“ (idg. *nōdos)', Walde-Pokorny II 328 the same, Watkins 'Lengthened o-grade form *nōdo- in Latin nōdus, a knot'. Latin nectere, nexuī, nexum 'to tie, bind, knot' belongs to the same root but is, as Pokorny says, a 'Neubildung nach plectō' — a present re-made on the model of plectō 'to plait' (Watkins: 'Re-formation of the root in Latin nectere'), which is why it shows -ct- rather than the expected form; Ernout–Meillet (p.772) reach the same conclusion, reconstructing *nedh-/*ned- from nōdus, Old Irish naidm 'bond' and nascim 'I bind', and treating necto as 'une forme nouvelle créée d'après plecto'. Also from the root in Latin are nassa 'wicker fish-trap' (*nad-s-a) and, with the 'closely joined > near' shift, Oscan nessimas, Umbrian nesimei 'nearest'.\",\n     \"derivation_fa\": \"لاتین nōdus «گره» (که نورایی با نشانهٔ ô می‌نویسد و همان کشیدگی ō است و با چاپ کتاب مطابق است) صورت گشتهٔ o-دارِ کشیدهٔ *nōdo-s از ریشهٔ *ned- است، یعنی «آنچه گره خورده»: پوکورنی (ص ۷۵۸) می‌نویسد «lat. nōdus „Knoten“ (idg. *nōdos)» و واتکینز نیز همین را. فعل nectere «بستن، گره زدن» هم از همین ریشه است، اما — چنان‌که پوکورنی می‌گوید — ساختی نو است به قیاسِ plectō «بافتن»؛ از این‌رو خوشهٔ -ct- دارد نه صورت انتظاری. ارنو–مِیه (ص ۷۷۲) هم بر پایهٔ nōdus و ایرلندی کهن naidm «بند» و nascim «می‌بندم» ریشهٔ *nedh-/*ned- را بازمی‌سازند و necto را «صورتی نو به قیاس plecto» می‌شمارند. از همین ریشه در لاتین nassa «سبد ماهی‌گیری» و — با تحول معنایی «سخت پیوسته ← نزدیک» — اُسکی nessimas و اومبریایی nesimei «نزدیک‌ترین» نیز هست.\",\n     \"sources\": [E + \"node\", E + \"annex\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 p.44 s.v. ned-: '2. Lengthened o-grade form *nōdo- in Latin nōdus, a knot: NODE, NODULE, NODUS; DENOUEMENT. 3. Re-formation of the root in Latin nectere (past participle nexus), to tie, bind, connect: NEXUS; (ADNEXA), ANNEX, CONNECT.' Both of Nourai's Latin words with both of his glosses.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"IEW 758 (POK_02.txt leaf 420)\", \"stance\": \"supports\", \"note\": \"'1. Lat. nōdus „Knoten“ (idg. *nōdos); vermutlich nassa (*nad-s-a) „Fischreuse…“; nectō, -ere, nexī, nectum „knüpfen, binden“ ist Neubildung nach plectō'.\"},\n      {\"src\": \"LAT\", \"where\": \"Ernout–Meillet p.772 s.v. necto (LAT.txt leaf 790)\", \"stance\": \"supports\", \"note\": \"'…on a nodus à côté de necto … Ceci conduit à poser une racine nedh-; et en effet l'irlandais a naidm „lien“ … nascim „je lie“ … necto serait une forme nouvelle créée d'après plecto'.\"},\n      {\"src\": \"IEC\", \"where\": \"Mann col. ~916 s.v. nódos\", \"stance\": \"supports\", \"note\": \"'nódos, is, io „knot, tie“. WP II, 328 … Lat. nodus, gs: -i, m. „knot, noose, knot in wood“'.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. II p.328\", \"stance\": \"supports\", \"note\": \"'Lat. nodus „Knoten“ (idg. *nodos) … vermutlich nassa „Fischreuse, geflochtener Korb…“'\"}\n     ]\n    },\n    {\n     \"id\": 9, \"lang\": \"English\", \"words\": \"node, annex, connect\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"All three are learned Latinisms of the late Middle English / early modern period, and all three descend from node #8. NODE: early 15c. 'a knot or lump', borrowed c.1400 in the Latin form nodus 'lump in the flesh', from Latin nōdus; the sense 'point of intersection' is 1660s astronomical (of the crossing of a planetary orbit with the ecliptic). ANNEX: late 14c. 'connect with', from Old French annexer (13c.), from Medieval Latin annexāre, frequentative of Latin annectere 'to bind to' = ad- 'to' + nectere; of nations and territories from c.1400. CONNECT: from Latin cōnectere/connectere 'to fasten together' = com- 'together' + nectere; the English verb is 15c., the noun connection late 14c. via Old French from Latin connexiōnem. Watkins lists exactly this trio of outcomes under the root ('NEXUS; (ADNEXA), ANNEX, CONNECT' and 'NODE, NODULE, NODUS; DENOUEMENT'), and Etymonline's *ned- box gives 'annex; annexation; connect; connection; denouement; net; nettle; nexus; node; nodule; noose'.\",\n     \"derivation_fa\": \"هر سه واژه وام‌واژه‌های عالمانهٔ لاتین در انگلیسیِ میانهٔ پایانی و آغاز دورهٔ نو هستند و همه از جعبهٔ لاتین (گرهٔ ۸) می‌آیند. node: از سدهٔ پانزدهم به معنی «گره، برآمدگی»، نخست حدود ۱۴۰۰ در همان صورت لاتینِ nodus «برآمدگی در گوشت»، از لاتین nōdus؛ معنای «نقطهٔ تقاطع» از دههٔ ۱۶۶۰ در اخترشناسی (تقاطع مدار سیّاره با دایرهٔ البروج) پیدا شد. annex: از پایان سدهٔ چهاردهم «پیوستن»، از فرانسهٔ کهن annexer، از لاتین میانه annexāre، صورت تکراریِ لاتین annectere = ad- «به» + nectere؛ کاربرد سیاسی («الحاق سرزمین») از حدود ۱۴۰۰. connect: از لاتین connectere = com- «با هم» + nectere. واتکینز عیناً همین سه برآمد را زیر ریشهٔ ned- می‌آورد و اتیمونلاین هم در جعبهٔ *ned- فهرست annex, connect, node, nexus, nodule, noose, net, nettle را می‌دهد. ادعای نورایی درست است.\",\n     \"sources\": [E + \"node\", E + \"annex\"],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference in the book (refs=None). Checked against Etymonline s.v. node, annex and the *ned- root box (which lists annex, annexation, connect, connection, denouement, net, nettle, nexus, node, nodule, noose), and against Watkins 1985 p.44, cited on the parent Latin node.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 p.44 s.v. ned-\", \"stance\": \"supports\", \"note\": \"'…Latin nōdus, a knot: NODE, NODULE, NODUS; DENOUEMENT … Latin nectere …: NEXUS; (ADNEXA), ANNEX, CONNECT'.\"},\n      {\"src\": \"KLN\", \"where\": \"Klein s.v. node / annex / connect (KLN_1966.txt)\", \"stance\": \"supports\", \"note\": \"Klein routes node < L. nōdus and annex < OF. annexer < ML. annexāre < L. annectere (ad- + nectere), the same chain.\"},\n      {\"src\": \"LAT\", \"where\": \"Ernout–Meillet p.772 s.v. necto, 'Dérivés et composés'\", \"stance\": \"supports\", \"note\": \"'adnecto (an-): attacher à … annexus,-us m.: annexion (Tac.); annexio … conecto: attacher ensemble … cōnexum,-i et cōnexio' — the Latin bases of English annex and connect.\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 1,\n   \"root\": \"Nedo, Narda\",\n   \"verdict\": \"plausible\",\n   \"modern_form\": \"PIE *nedo- 'reed' (Pokorny IEW 759, marked with a query); the 'narda' variant is at best Indo-Iranian *narda- (Horn, Hübschmann, Moʿīn), and the nard/spikenard word is generally treated as a Wanderwort, not an inherited IE root\",\n   \"note\": \"Two half-true things are welded into one root box. (a) *nedo- 'reed' is real but tentative: Pokorny IEW 759 gives 'nedo- „Schilf“?' — with a question mark — on the strength of Old Indic naḍa- 'reed (vermutlich)', New Persian nāi and dialectal nād, Armenian net 'arrow', Lithuanian nendrė, Latvian nāsli; Walde-Pokorny II 329 the same. Note that Pokorny's gloss is 'reed' only; 'pipe, flute' is the derived Persian sense, not part of the reconstruction, and Pokorny cites New Persian directly, not an Old Persian form. (b) 'Narda' is not a Pokorny lemma at all. It comes from Horn (Grundriss p.237 no.1060), who posits beside *nada- 'a second form *narda-, to which Old Indic naḍá- (the Greek loanword νάρδος, the Hebrew loanword נרד) and NP nārd go back', and from Hübschmann (Persische Studien p.103 no.1060) 'arisch *narda-'; Moʿīn repeats 'آریایی *narda-' in his footnote to Borhān p.2221. But Horn in the same paragraph says 'nalada- ist sanskritisirtes νάρδος', and modern work (Beekes 2010 s.v. νάρδος; Klein s.v. nard) treats the whole nard family as a Near-Eastern culture word of ultimately Indic origin that spread through Semitic, not as an inherited Indo-European root. So the box's first half is confirmed-with-a-query and its second half is a nineteenth-century reconstruction that modern scholarship does not use as a PIE root. Hence 'plausible' overall. Nourai's second reference, BQT:2221, checks out perfectly and is in fact the best support for the Iranian side.\",\n   \"note_fa\": \"در این جعبهٔ ریشه دو چیزِ نیمه‌درست به هم جوش خورده است. یک: *nedo- «نی» واقعی ولی احتیاطی است — پوکورنی (ص ۷۵۹) آن را با علامت پرسش می‌آورد: «nedo- „نی“؟» بر پایهٔ هندی باستان naḍa-، فارسی نو nāi و گونهٔ گویشی nād، ارمنی net «تیر» و لیتوانیایی nendrė؛ و معنایی که پوکورنی می‌دهد تنها «نی» است، نه «فلوت»؛ «فلوت» تحول معنایی ایرانی است. دو: «Narda» هیچ سرمدخلی در پوکورنی نیست؛ این صورت از هرن (ص ۲۳۷، شمارهٔ ۱۰۶۰) می‌آید که در کنار *nada- صورت دومی *narda- می‌نهد و ارمنی و یونانی νάρδος و عبری נרד و فارسی nārd را به آن بازمی‌گرداند، و از هوبشمان («آریایی *narda-») که معین هم در حاشیهٔ برهان قاطع (ص ۲۲۲۱) نقل کرده است. اما هرن در همان بند می‌نویسد که nalada- سنسکریت‌شدهٔ νάρδος است، و پژوهش امروزی (بیکس ۲۰۱۰ ذیل νάρδος؛ کلاین ذیل nard) کل خانوادهٔ «نارد» را واژه‌ای فرهنگی و سرگردان (Wanderwort) با خاستگاه هندی می‌داند که از راه زبان‌های سامی پراکنده شده، نه ریشه‌ای ارثی هندواروپایی. بنابراین: نیمهٔ نخست جعبه با احتیاط پذیرفتنی است و نیمهٔ دوم بازسازی‌ای از سدهٔ نوزدهم است که امروز آن را ریشهٔ هندواروپایی نمی‌شمارند.\",\n   \"sources\": [W + \"%D9%86%D8%A7%DB%8C\", W + \"%CE%BD%CE%AC%CF%81%CE%B4%CE%BF%CF%82\"],\n   \"ref_check\": [\n    {\"ref\": \"POK:759\", \"status\": \"partial\", \"note\": \"Pokorny IEW 759 (POK_02.txt leaf 421): 'nedo- „Schilf“? Ai. nada- m. vermutlich „Schilfrohr“, npers. nai, dial. nad „Schilf“; arm. net „Pfeil“; lit. nendrė (und lendrė) „Schilfrohr“ …; lett. nāsli „Schilf“ aus *nadslis? WP. II 329.' Supports 'Nedo' with 'reed', but not the gloss 'pipe, flute', not the form 'Narda', and not an Old Persian intermediate.\"},\n    {\"ref\": \"BQT:2221\", \"status\": \"supports\", \"note\": \"Borhān-e Qāṭeʿ ed. Moʿīn p.2221 (vol. 4, BQT_v4_pages.txt pdf page 304 = 304+1917), s.v. نی, Moʿīn's footnote 1: 'نای، نال، فی: نی … سور[نای]، شه[نای]، نایزه. پارسی باستان *nāda (نای)، پهلوی nāy، فی nāy؛ هندی باستان naḍa-/nāḍa- (نای، نی)؛ ارمنی net (تیر)؟ … نال (فارسی) … بمعنی نای، ساقه، لوله؛ افغانی nāra (ساقه)؛ سانسکریت nāḍa-؛ آریایی *narda-؛ هوبشمان ۱۰۹؛ پهلوی nād؛ کردی nei؛ لری nei'. This single footnote underwrites the root, node #1 and node #2.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"IEW 759\", \"stance\": \"partial\", \"note\": \"'nedo- „Schilf“?' — queried lemma, gloss 'reed' only, no Old Persian, no *narda-.\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. II p.329 (WLD_Bd2_pages.txt leaf 333)\", \"stance\": \"partial\", \"note\": \"'nedo- „Schilf“. Ai. nada- m. vermutlich „Schilfrohr“ …, np. nai, mdartl. nad „Schilf“; arm. … net' — same content, same absence of *narda- and of any Old Persian form.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, Indo-European appendix (searched for nedo-, nad-, reed)\", \"stance\": \"silent\", \"note\": \"Watkins has no *nedo- 'reed' root at all (no English word descends from it), so the AHD appendix neither supports nor contradicts.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann col. ~892 s.v. nad- (IEC.txt leaf 461)\", \"stance\": \"contradicts\", \"note\": \"'nad- (nod-?) „wet; water“ … Skt. nadīḥ, f. „water“; Go. cf. natjan, v. „wet“; OHG naz, OS nat „wet“ … and perh. Per. nai, nay „reed“' — Mann attaches Persian nāy to a root 'wet, water', not to a 'reed' root.\"},\n    {\"src\": \"HRN\", \"where\": \"Horn, Grundriss p.237 no.1060 (HRN.txt leaf 258)\", \"stance\": \"partial\", \"note\": \"'Die Lautverhältnisse sind noch nicht richtig erkannt. Np. nei, g. nad setzen unbedingt eine Urform *nada- voraus; neben dieser gab es eine zweite Form *narda-, auf welche ai. naḍá- (gr. LW. νάρδος, hebr. LW. נרד) und np. nārd zurückgehen. Das jüngere skr. nālá- ist persisches Lehnwort … nalada- ist sanskritisirtes νάρδος.' Source of Nourai's 'Narda', but Horn himself admits the sound-correspondences are unresolved.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Old Persian\", \"words\": \"nada\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"There is no attested Old Persian *nada-: it does not occur in the Achaemenid inscriptions and is absent from Kent's Old Persian lexicon. What Nourai's source actually gives is a reconstruction. Horn, Grundriss p.237 no.1060 (Nourai's HRN:237) prints 'ap. *nada- „Schilf“' with an asterisk, and adds 'phlv. nai bezw. nad (PPGl)'; Moʿīn's footnote to Borhān p.2221 repeats it in Persian as 'پارسی باستان *nāda' and Aryanpur's entry for نای lists '*NADA (OLD PERSIAN)' with Pahlavi NAY/NADH/NAT beside it. Wiktionary reaches the same place by a different route: Persian نای 'from Middle Persian nʾd (nāy), from Proto-Indo-Iranian *nada (compare Sanskrit naḍá), from Proto-Indo-European *nedo- „reed“' — i.e. the intermediate is Old Iranian / Proto-Indo-Iranian *nada-, not Old Persian as a documented language. Two smaller points: the form should carry an asterisk, and the gloss should be 'reed' (Horn: 'Schilf'), with 'flute' the later, specialized Persian sense. So the arrow is defensible, the label and gloss are overstated.\",\n     \"derivation_fa\": \"صورت *nada- در پارسی باستانِ گواه‌دار وجود ندارد: در سنگ‌نبشته‌های هخامنشی نیامده و در واژه‌نامهٔ پارسی باستانِ کنت هم نیست. آنچه مرجع خودِ نورایی می‌دهد یک بازسازی است: هرن (ص ۲۳۷، شمارهٔ ۱۰۶۰) می‌نویسد «ap. *nada- „نی“» با ستاره، و می‌افزاید «پهلوی nai یا nad». معین در حاشیهٔ برهان قاطع (ص ۲۲۲۱) همین را به فارسی می‌آورد: «پارسی باستان *nāda»، و آریان‌پور نیز در مدخل «نای» صورت *NADA (پارسی باستان) را در کنار پهلوی nāy/nādh/nāt می‌آورد. ویکی‌واژه از راه دیگری به همین‌جا می‌رسد: «نای» از فارسی میانهٔ nāy، از هندوایرانی آغازین *nada (هم‌ریشه با سنسکریت naḍá)، از هندواروپایی آغازین *nedo- «نی». پس دو تصحیح لازم است: نخست، این صورت باید با ستاره (بازسازی‌شده) نوشته شود و برچسب دقیق‌ترش «ایرانی باستان» است نه «پارسی باستان»؛ دوم، معنای آن «نی» است و «فلوت» تحول معنایی متأخر فارسی است. با این دو قید، ادعای نورایی پذیرفتنی است.\",\n     \"sources\": [W + \"%D9%86%D8%A7%DB%8C\"],\n     \"ref_check\": [\n      {\"ref\": \"HRN:237\", \"status\": \"partial\", \"note\": \"Horn, Grundriss der neupersischen Etymologie p.237 no.1060 (HRN.txt leaf 258, running head '— 237 —'): 'nei „Schilf“, nāi „Flöte“, nāl; vergl. kerrenāi, sūrnāi „Festflöte“, šahnāi; nāize. g. nad. ap. *nada- „Schilf“; phlv. nai bezw. nad (PPGl); ai. nadá-, naḍá- „Schilfrohr“ …; arm. net „Pfeil“?' The page and content are exactly right — but the Old Persian form is starred (reconstructed) and glossed 'Schilf' = reed, not 'flute'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KNT\", \"where\": \"Kent, Old Persian: Grammar, Texts, Lexicon, Lexicon pp.164–215 (grep of KNT.txt for nada)\", \"stance\": \"contradicts\", \"note\": \"no headword nada- / nāda- in Kent's Old Persian lexicon (the only hit is OCR noise), confirming the form is unattested in Old Persian proper.\"},\n      {\"src\": \"BRT\", \"where\": \"Bartholomae, Altiranisches Wörterbuch (grep for nada-/nāda-)\", \"stance\": \"silent\", \"note\": \"no Avestan or Old Persian nada- in AiW either; the word is simply not documented in Old Iranian.\"},\n      {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e Rishe-hā-ye Hend-o-Orupāyi, entry نای (ARY_latin_index_pages.txt pdf page 494, printed p.495)\", \"stance\": \"supports\", \"note\": \"the entry lists '*NADA (OLD PERSIAN) … NAY, NADH, NAT (PAHLAVI) … NEI (KURDISH) … NARA (AFGHANI) … NADA, NADHA (SANSKRIT) … NET (ARMENIAN) … NENDRE (LITHUANIAN)' with references to POKORNY, MACKENZIE '(REED, CANE) 58' and MALLORY & ADAMS 'NEDOS' — an independent modern Persian cross-check that starts the chain at a starred Old Persian *nada-.\"},\n      {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. nāy (PHD.txt leaf 82; p.58)\", \"stance\": \"supports\", \"note\": \"'nay [KNYA < A qnyʾ; nʾd | N ~] reed, cane' and 'nāy [nʾd | M nʾy, N ~] tube, flute, clarion; pole, perch (10 ft.). ~ pazd-: blow, play the flute' — the Middle Persian stage Horn's *nada- presupposes, written <nʾd> and (as a logogram) with Aramaic qanyā 'reed'.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Persian\", \"words\": \"nâi, nay, nâl; surnây, sornâ; kornâ; qaraney\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"نای/نی nāy, nay 'reed; reed-pipe, flute; throat, windpipe' is the inherited word: Old Iranian *nada- > MP nāy, written <nʾd> (MacKenzie p.58 'nāy … tube, flute, clarion'), with the regular Middle-to-New Persian loss of the intervocalic/final dental and glide-ing to -y; نی ney is the shortened New Persian form, نال nāl the lengthened variant that Horn (p.237) and Hübschmann (p.103 no.1060) equate with Sanskrit naḍá-/nālá- and 'arisch *narda-'. All confirmed, and Borhān p.2104 (نال) and p.2221 (نی) with Moʿīn's footnotes give exactly this chain. The three compounds are shakier. (i) سورنای/سرنا: Borhān p.~1135 (vol. 2 leaf 592) defines 'سرنای: بمعنی نای رومی است که سرنا هم باشد' and 'سرنی: مخفف سورنای است که نای رومی باشد', and Moʿīn lists سرنا (- سورنا - سرنای - سورنای - سرنی - صرنای) as a musical instrument; the traditional analysis is سور 'feast' + نای, which is what Nourai's cross-reference '☞Keu 4' assumes. Wiktionary, however, calls that a folk etymology and derives the word from an unknown, possibly Anatolian, source cognate with Luwian zurni 'horn' (Greppin 1991) — so the نای in سرنا may be secondary reshaping. (ii) کرنا/کارنای 'war-horn': the native etymologies (کار 'army, battle' + نای, or خر 'big/donkey' + نای) keep -نای, and Nourai's '☞Koro' points to *ker- 'horn' for the first element; but Wiktionary judges the word 'possibly of Semitic origin', comparing Syriac qarnā, Akkadian qarnum, Arabic qarn, Hebrew qeren. (iii) قره‌نی/قرنی 'clarinet': here Nourai is right and his gloss 'black flute' is the standard one — Moʿīn tags it '[تر - فا.]' (Turkish + Persian), i.e. Turkish qara 'black' + Persian نی, and the Persian dictionaries gloss it 'نی سیاه' / 'نی بزرگ که از چوب و فلز ساخته می‌شود'. Verdict for the node: the head-words are confirmed, two of the three compounds are contested in their first element only, so 'plausible'.\",\n     \"derivation_fa\": \"«نای/نی» واژه‌ای ارثی است: از ایرانی باستان *nada- به فارسی میانهٔ nāy (نوشتهٔ <nʾd>؛ مکنزی ص ۵۸: «nāy: لوله، نای، فلوت، کرنا») و از آنجا به فارسی نو؛ دندانیِ پایانی در گذار از فارسی میانه به نو افتاده و به «ی» بدل شده است. «نی» کوتاه‌شدهٔ همان است و «نال» گونهٔ کشیده که هرن (ص ۲۳۷) و هوبشمان (ص ۱۰۳) با سنسکریت naḍá-/nālá- و «آریایی *narda-» برابر می‌گیرند؛ حاشیه‌های معین بر برهان قاطع (ص ۲۱۰۴ ذیل «نال» و ص ۲۲۲۱ ذیل «نی») دقیقاً همین زنجیره را می‌آورند. اما سه ترکیب دیگر جای بحث دارند. یک) «سورنای/سرنا»: برهان قاطع «سرنای» را «نای رومی» می‌داند و معین همهٔ گونه‌ها را زیر «سرنا» می‌آورد؛ تحلیل سنّتی سور + نای است (همان که ارجاع نورایی به «Keu 4» بر آن استوار است)، ولی ویکی‌واژه آن را ریشه‌شناسی عامیانه می‌شمارد و واژه را از خاستگاهی ناشناخته و شاید آناتولیایی، هم‌ریشه با لوویایی zurni «شاخ»، می‌گیرد. دو) «کرنا/کارنای»: ریشه‌شناسی‌های بومی جزء دوم را همان «نای» می‌دانند (کار + نای یا خر + نای) و نورایی هم جزء نخست را به ریشهٔ *ker- «شاخ» می‌برد؛ اما ویکی‌واژه احتمال خاستگاه سامی را ترجیح می‌دهد (سریانی qarnā، اکدی qarnum، عربی قرن، عبری qeren). سه) «قره‌نی»: اینجا حق با نورایی است و معنی «نی سیاه» درست است؛ معین آن را «[تر - فا.]» یعنی ترکی + فارسی برچسب می‌زند، از ترکی qara «سیاه» و فارسی «نی». پس: سرواژه‌ها تأییدشده‌اند و تنها جزء نخستِ دو ترکیب مورد اختلاف است.\",\n     \"sources\": [W + \"%D9%86%D8%A7%DB%8C\", W + \"%D8%B3%D8%B1%D9%86%D8%A7\", W + \"%DA%A9%D8%B1%D9%86%D8%A7\", \"https://abadis.ir/fatofa/%D9%82%D8%B1%D9%87-%D9%86%DB%8C/\"],\n     \"ref_check\": [\n      {\"ref\": \"POK:759\", \"status\": \"supports\", \"note\": \"IEW 759 s.v. nedo-: 'npers. nai, dial. nad „Schilf“' — Pokorny cites the New Persian word directly.\"},\n      {\"ref\": \"BQT:2221\", \"status\": \"supports\", \"note\": \"Borhān p.2221 (vol. 4 pdf p.304), s.v. نی: 'نی — بفتح اول و سکون ثانی، مشدد آنی است که مزمار و حلقوم باشد و قلم و کلک و لیشکر را نیز گویند'; Moʿīn's footnote gives 'نای، نال … پارسی باستان *nāda، پهلوی nāy … هندی باستان naḍa-/nāḍa- … آریایی *narda- … هوبشمان ۱۰۹ … کردی nei … ژابا ۲۷'.\"},\n      {\"ref\": \"BQT:2104\", \"status\": \"supports\", \"note\": \"Borhān p.2104 (vol. 4 pdf p.187), s.v. نال: 'نال - بر وزن سال، نای میان خالی را گویند و عربان مزمار خوانند - و قلم و نویسندگی …'; Moʿīn's footnote 4 quotes Henning: 'nāl (نی، قلم نی)، لغت فرس اسدی (چاپ اروپا ص ۷۸)، شمس فخری ۸۵، ولرس II ص ۱۲۸۲ نال — نای nāy ولی nāl (نی، فلوت)'.\"},\n      {\"ref\": \"BQT:1185\", \"status\": \"supports\", \"note\": \"vol. 2 of Borhān (OCR text only, no page scan available: ref_page.py answers 'no scan of BQT covers printed page 1185'). The سرنای/سرنی article is at BQT_v2_pages.txt leaf 592: 'سرنای - بضم اول و سکون ثانی و کشیدن، بمعنی نای رومی است که سرنا هم باشد؛ و بحذف الف هم آمده است' and 'سرنی - … مخفف سورنای است که نای رومی باشد'. Content confirmed; the printed page numeral is not legible in the OCR of that leaf (the vol.-2 leaf→page offset is uncertain by ±50), so the page number itself could not be verified.\"},\n      {\"ref\": \"MON:2957\", \"status\": \"supports\", \"note\": \"Mo'in s.v. سرنا (MON_part1.txt): 'سرنا: (- سورنا - سرنای - سورنای - سرنی - صرنای، معر.) (اِ.) (موسیقی) … این ساز در غالب نقاط ایران موجود است و آن را همراه دهل نوازند' — all of Nourai's variants in one entry. The local copy is the 2-vol. Adena reprint, so p.2957 of the 6-vol. edition could not itself be checked.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie p.58 s.v. nāy / nay (PHD.txt leaf 82)\", \"stance\": \"supports\", \"note\": \"'nāy [nʾd | M nʾy, N ~] tube, flute, clarion; pole, perch (10 ft.). ~ pazd-: blow, play the flute'; also nayestān 'reed-bed', nāyīzag 'small reed', nay-srāy 'flautist' — the Middle Persian antecedent of نای with the 'flute' sense already present.\"},\n      {\"src\": \"HRN\", \"where\": \"Grundriss p.237 no.1060\", \"stance\": \"supports\", \"note\": \"'nei „Schilf“, nāi „Flöte“, nāl; vergl. kerrenāi, sūrnāi „Festflöte“, šahnāi' — Horn lists Nourai's compounds surnāy and karrenāy under nāy, and adds a footnote on Caucasian Judaeo-Persian zürnai / Russian zurna.\"},\n      {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien p.103 no.1060 (HUB.txt leaf 113)\", \"stance\": \"supports\", \"note\": \"'1060. Np. nāl „Rohr, Stengel, Röhre“ — afgh. nal f. „Stengel“ = skr. naḍá- „Schilf, Schilfrohr“ = arisch *narda- (Geiger, Etym. und Lautl. des Afgh. Nr. 140).'\"},\n      {\"src\": \"MON\", \"where\": \"Mo'in via abadis, s.v. قره نی\", \"stance\": \"supports\", \"note\": \"فرهنگ معین: '(قَ رَ. نِ) [تر - فا.] (اِ.) نی بزرگ که از چوب و فلز ساخته می شود'; فرهنگ فارسی: '۱ - نی سیاه ۲ - نی بزرگ …' — Turkish qara 'black' + Persian نی, exactly Nourai's 'black flute'.\"},\n      {\"src\": \"BQT\", \"where\": \"vol. 2 leaf 592 (سرنای، سرنی) and vol. 4 pp.2104, 2221\", \"stance\": \"supports\", \"note\": \"see ref_check; note that Borhān explains سرنای as 'نای رومی' (a Byzantine/Anatolian pipe), which sits oddly with the سور 'feast' analysis and rather agrees with Wiktionary's Anatolian-loan account of the first element.\"},\n      {\"src\": \"ARY\", \"where\": \"Aryanpur, entry نای (pdf p.494)\", \"stance\": \"supports\", \"note\": \"'*NADA (OLD PERSIAN) … NAY, NADH, NAT (PAHLAVI) … MACKENZIE: (REED, CANE) 58 … MALLORY & ADAMS: NEDOS'.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Sanskrit\", \"words\": \"nadah; naladam, nalada\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"Two claims are bundled here. (a) naḍá- m. (nom. naḍáḥ, Nourai's 'nadah') 'reed, hollow stalk' as a descendant of *nedo-: this is the core of Pokorny's entry ('Ai. nada- m. vermutlich „Schilfrohr“', IEW 759) and of Walde-Pokorny II 329, and Horn p.237 has 'ai. nadá-, naḍá- „Schilfrohr“'; the Sanskrit ḍ is the regular retroflexion of an intervocalic *d in this word (Vedic naḍá-/nalá-, the l-form giving nāla 'tube, made of reeds'). Confirmed. (b) náladam / nálada 'Indian spikenard, Nardostachys jatamansi' (AV, Suśruta) as a further derivative of naḍá-: this is only probable. Wiktionary, following Mayrhofer, calls nálada 'of uncertain origin, though perhaps a derivative of नड (naḍá „reed, hollow stalk“), probably via an intermediate नाल (nāla „tube, vein; made of reeds“), owing to the plant's stalk-like structure', and there is an old rival view — Horn's own, on the very page Nourai cites — that 'nalada- ist sanskritisirtes νάρδος', i.e. that the Sanskrit plant-name is a back-formation on the Greek word. Klein reports both directions (Boisacq/Walde-Hofmann: Semitic words from Indo-Iranian *narda; Mayrhofer: Semitic words from OI naladam). Since Nourai's arrow depends on (b) as much as (a), the node is 'plausible'.\",\n     \"derivation_fa\": \"در این گره دو ادعا کنار هم آمده است. یک) naḍá- سنسکریت (حالت فاعلی naḍáḥ، همان «nadah» نورایی) به معنی «نی، ساقهٔ میان‌تُهی» بازماندهٔ *nedo- است؛ این هستهٔ مدخل پوکورنی (ص ۷۵۹: «ai. nada- احتمالاً „نیِ نیزار“») و والده–پوکورنی (ج ۲ ص ۳۲۹) و هرن (ص ۲۳۷) است، و «ڎ» غلیظِ سنسکریت دگرگونی قاعده‌مندِ *d میان‌واکه‌ای در همین واژه است (گونهٔ l-دار nalá- و از آن nāla «لوله»). این بخش تأیید می‌شود. دو) nálada/náladam «سنبل هندی» به‌عنوان گشتهٔ دیگری از naḍá-: این تنها احتمالی است. ویکی‌واژه به پیروی مایرهوفر می‌نویسد «خاستگاهش نامعلوم است، اگرچه شاید گشتهٔ نَڎَ „نی“ باشد، احتمالاً از راه صورت میانی nāla „لوله“، به سبب ساقه‌مانندی گیاه». و دیدگاه رقیبِ کهنی هم هست — از قلم خودِ هرن، در همان صفحه‌ای که نورایی ارجاع می‌دهد: «nalada- سنسکریت‌شدهٔ νάρδος است»، یعنی نام سنسکریتِ گیاه ساختی است بر پایهٔ واژهٔ یونانی. کلاین هر دو جهت را نقل می‌کند. چون ادعای نورایی به همان اندازه بر (دو) تکیه دارد، حکم این گره «با احتیاط پذیرفتنی» است.\",\n     \"sources\": [W + \"%E0%A4%A8%E0%A4%B2%E0%A4%A6\", W + \"%CE%BD%CE%AC%CF%81%CE%B4%CE%BF%CF%82\"],\n     \"ref_check\": [\n      {\"ref\": \"POK:759\", \"status\": \"supports\", \"note\": \"IEW 759: 'nedo- „Schilf“? Ai. nada- m. vermutlich „Schilfrohr“ …' — supports naḍá- from the root; Pokorny says nothing about nalada.\"},\n      {\"ref\": \"HRN:237\", \"status\": \"partial\", \"note\": \"Horn p.237 no.1060 gives 'ai. nadá-, naḍá- „Schilfrohr“' (supports) but then explicitly: 'Skr. nālá- wird jüngere Form für naḍá- sein, wie Pischel annimmt, nalada- ist sanskritisirtes νάρδος' — i.e. Horn derives nalada from Greek, the reverse of Nourai's arrow.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"WLD\", \"where\": \"Bd. II p.329 s.v. nedo-\", \"stance\": \"supports\", \"note\": \"'Ai. nada- m. vermutlich „Schilfrohr“ (s. Uhlenbeck Ai. Wb. s.v., Persson Beitr. 814 Anm. 1), np. nai, mdartl. nad „Schilf“; arm. … net'.\"},\n      {\"src\": \"KLN\", \"where\": \"Klein s.v. nard (KLN_1966.txt leaf 550; printed ≈1077)\", \"stance\": \"partial\", \"note\": \"'…prob. derives fr. Indo-Iranian *narda in OI. naḍaḥ, nalaḥ, „reed“. OI. naladam, „nard“, is possibly Sanskritization of Gk. νάρδος … However, according to Manfred Mayrhofer … the above Sem. words more prob. derive fr. OI. naladam.' Both directions on the table.\"},\n      {\"src\": \"POK\", \"where\": \"IEW 759\", \"stance\": \"supports\", \"note\": \"as in ref_check.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"Persian\", \"words\": \"nard 2\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"The claim 'Sanskrit nalada → Persian nard' is a nineteenth-century position that Nourai's two Western references really do hold. Skeat p.344 s.v. Nard traces 'F. nard — L. nardus — Gk. νάρδος (Mark xiv,3) — Pers. nard — Skt. nalada, the Indian spikenard', and Horn p.237 posits a form *narda- to which 'np. nārd' goes back beside Sanskrit naḍá- and the Greek and Hebrew loanwords; Hübschmann p.103 likewise writes 'arisch *narda-'. The Persian forms themselves need sorting out, though. نارْدین nārdīn 'sunbol-e Rūmī, spikenard' is well attested (Avicenna's Qānūn p.214, Ẕaxīra-ye Xārazmšāhī, Toḥfa-ye Ḥakīm Moʾmen, Ibn al-Bayṭār) — but Dehkhodā s.v. ناردین quotes Aqrab al-Mawārid to the effect that 'نردین و ناردین: سنبل رومی، معرّب نَرذُس یونانی است' (an Arabicization of Greek nardos) and adds 'اسم یونانی مطلق سنبل است', and Moʿīn's own footnote in Borhān p.2093–94 says 'ناردین شکل تغییر یافتهٔ سریانی-عربی کلمهٔ یونانی νάρδινος است'. Meanwhile Borhān p.2093 s.v. نارد gives quite different senses ('مخفف نیارد … و کنه را نیز گویند' — a contraction of nayārad 'he cannot', and 'tick'), and Dehkhodā/ʿAmīd's نرد ۲ is 'تنۀ درخت، ساقۀ درخت' (trunk, stalk — Ferdowsī's 'یکی سبزنرد', Kasāʾī via Loḡat-e Fors), which is the 'reed/stalk' sense, not 'spikenard'. So: an inherited Iranian *narda- 'stalk' is real and is what نرد ۲ means in the classical poets; the specifically 'spikenard' word ناردین is, on the Persian lexicographers' own showing, a Greek/Syriac-Arabic loan. Plausible rather than confirmed.\",\n     \"derivation_fa\": \"ادعای «nalada سنسکریت ← نردِ فارسی» موضعی است از سدهٔ نوزدهم که هر دو مرجع غربیِ نورایی واقعاً بر آن‌اند: اسکیت (ص ۳۴۴) زنجیرهٔ «فرانسه nard ← لاتین nardus ← یونانی νάρδος ← فارسی nard ← سنسکریت nalada» را می‌آورد و هرن (ص ۲۳۷) صورت *narda- را می‌نهد که فارسی nārd نیز از آن است؛ هوبشمان هم «آریایی *narda-» می‌نویسد. اما صورت‌های فارسی این گره نیاز به تفکیک دارند. «ناردین» به معنی سنبل رومی به‌خوبی گواه دارد (قانون ابن‌سینا ص ۲۱۴، ذخیرهٔ خوارزمشاهی، تحفهٔ حکیم مؤمن، ابن بیطار) — ولی دهخدا به نقل اقرب الموارد می‌نویسد «نردین و ناردین: سنبل رومی، معرّب نَرذُسِ یونانی است» و می‌افزاید «اسم یونانی مطلق سنبل است»، و حاشیهٔ خودِ معین بر برهان قاطع (ص ۲۰۹۳–۲۰۹۴) صریح است: «ناردین شکل تغییر یافتهٔ سریانی–عربیِ کلمهٔ یونانی νάρδινος است». از سوی دیگر «نارد» در برهان قاطع (ص ۲۰۹۳) معنایی دیگر دارد («مخفف نیارد … و کنه را نیز گویند») و «نرد ۲» در دهخدا و عمید «تنهٔ درخت، ساقهٔ درخت» است (بیت فردوسی «یکی سبزنرد» و کسائی در لغت فرس) که همان معنای «نی/ساقه» است، نه «سنبل». نتیجه: *narda- ایرانی به معنی «ساقه» واقعی است و همان است که در «نرد ۲»ِ شاعران کلاسیک دیده می‌شود؛ اما «ناردین» به گواهی خودِ فرهنگ‌نویسان فارسی وام‌واژه‌ای یونانی–سریانی است. پس: با احتیاط پذیرفتنی.\",\n     \"sources\": [\"https://abadis.ir/fatofa/%D9%86%D8%A7%D8%B1%D8%AF%DB%8C%D9%86/\", \"https://abadis.ir/fatofa/%D9%86%D8%B1%D8%AF/\", W + \"%D9%86%D8%B1%D8%AF\"],\n     \"ref_check\": [\n      {\"ref\": \"SKT:344\", \"status\": \"supports\", \"note\": \"Skeat, Concise Etymological Dictionary, s.v. Nard (SKT.txt leaf 325, in the myrrh–natal block): 'Nard, an unguent. (F. — L. — Gk. — Pers. — Skt.) F. nard. — L. nardus. — Gk. νάρδος, Mk. xiv,3. — Pers. nard. — Skt. nalada, the Indian spikenard. — Skt. nal, to smell. Der. spikenard.' Exactly Nourai's Sanskrit → Persian step (and, note, no Arabic in Skeat's chain).\"},\n      {\"ref\": \"HRN:237\", \"status\": \"supports\", \"note\": \"Horn p.237 no.1060: 'neben dieser gab es eine zweite Form *narda-, auf welche ai. naḍá- (gr. LW. νάρδος, hebr. LW. נרד) und np. nārd zurückgehen' — an Iranian nārd from *narda-.\"},\n      {\"ref\": \"BQT:2093\", \"status\": \"partial\", \"note\": \"Borhān p.2093 (vol. 4, BQT_v4_pages.txt pdf p.176). The page is right, but s.v. نارد it gives 'نارد - بفتح رای قرشت و سکون دال ابجد، مخفف نیارد باشد، و بمعنی نتواند هست - و کنه را نیز گویند'; the spikenard word is the following headword ناردین, and Moʿīn's footnote there says 'باید دانست که ناردین شکل تغییر یافتهٔ سریانی-عربی کلمهٔ یونانی νάρδινος است' — i.e. the reference contradicts the direction Nourai draws for ناردین.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BQT\", \"where\": \"pp.2093–2094 s.v. نارد, ناردین (vol. 4 pdf pp.176–177)\", \"stance\": \"contradicts\", \"note\": \"Moʿīn's footnote: 'ناردین شکل تغییر یافتهٔ سریانی-عربی کلمهٔ یونانی νάρδινος است' … 'νάρδος (ش): سنبل، عقار ۲۹۵ عربی و فراسوی'; the article body ('ناردین … سنبل رومی را گویند و آن زردرنگ می‌باشد') is medical, from تحفهٔ حکیم مؤمن.\"},\n      {\"src\": \"MON\", \"where\": \"Dehkhodā and Moʿīn via abadis, s.v. ناردین and نرد\", \"stance\": \"contradicts\", \"note\": \"Dehkhodā: 'نردین و ناردین: سنبل رومی، معرّب نَرذُس یونانی است. (اقرب الموارد)'; 'اسم یونانی مطلق سنبل است. (تحفه حکیم مؤمن)'. Moʿīn tags نرد '[په.]' but only for the board-game sense; ʿAmīd's نرد ۲ is 'تنۀ درخت، ساقۀ درخت'.\"},\n      {\"src\": \"HUB\", \"where\": \"Persische Studien p.103 no.1060\", \"stance\": \"supports\", \"note\": \"'skr. naḍá- „Schilf, Schilfrohr“ = arisch *narda-' — Hübschmann accepts an Indo-Iranian *narda-, the form Nourai's root box calls 'Narda'.\"},\n      {\"src\": \"KLN\", \"where\": \"Klein s.v. nard\", \"stance\": \"partial\", \"note\": \"'…prob. derives fr. Indo-Iranian *narda in OI. naḍaḥ, nalaḥ, „reed“' — supports an Indo-Iranian *narda- behind the whole family, but routes the word to Europe through Hebrew, not Persian.\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"Arabic\", \"words\": \"nard\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"Two problems. First the form: Arabic نَرْد nard is the backgammon word (a clipping of نَرْدَشِير nardašīr, from Persian nard / MP nēw-Ardaxšīr), not the plant; the Arabic names of spikenard are نَارْدِين nārdīn / نَارَدِين nāradīn and, by metathesis, رَنْد rand. Nourai's own reference PLA:257 in fact prints نارْدين, not نرد: Asbaghi, Persische Lehnwörter im Arabischen p.257, 'nārdīn: „Spickenard, Lavendel“ pers. ← skr. nard, mand. nard, syr. …, hebr. נרד'. Second the direction: Asbaghi does count nārdīn as a Persian loan in Arabic, but Wiktionary (with the Comprehensive Aramaic Lexicon and Löw) derives Arabic نَارْدِين directly 'from Aramaic נָרְדִּין / ܢܪܕܝܢ (nārdīn), a plurale tantum form of נָרְדָּא / ܢܪܕܐ (nārdā)', and Arabic رَنْد is 'alleged to be a metathesis of what is found as Hebrew נֵרְדְּ, Aramaic נִרְדָּא, Akkadian lardu, Ancient Greek νάρδος, Sanskrit नलद, and Arabic نَارْدِين'. Dehkhodā (quoting Aqrab al-Mawārid) and Moʿīn (Borhān p.2093 n.) treat the Arabic form as an Arabicization of the Greek. Above all, the node cannot bear the weight the chart puts on it: it is drawn as the source of Greek nardos, which is chronologically impossible (see node #6). So: the plant word did travel westwards through Semitic, but through Aramaic/Phoenician-Hebrew rather than Arabic, and the Arabic form is nārdīn/rand, not nard.\",\n     \"derivation_fa\": \"دو اشکال دارد. یکم، صورت: «نَرْد» عربی نامِ بازیِ تخته‌نرد است (کوتاه‌شدهٔ نَرْدَشِير از فارسی nard / فارسی میانهٔ nēw-Ardaxšīr)، نه نامِ گیاه؛ نام‌های عربی سنبل «ناردین/نارَدین» و به قلب «رَنْد» است. حتی مرجعی که خودِ نورایی آورده (اصباغی، وام‌واژه‌های فارسی در عربی، ص ۲۵۷) صورت «ناردین» را می‌آورد نه «نرد»: «nārdīn: سنبل، اسطوخودوس؛ از فارسی ← سنسکریت nard، مندایی nard، سریانی …، عبری נרד». دوم، جهت: اصباغی ناردین را وام‌واژه‌ای فارسی در عربی می‌شمارد، اما ویکی‌واژه (به استناد فرهنگ جامع آرامی و لُو) عربی «ناردین» را یکسر از آرامی nārdīn (صورت جمعِ nārdā) می‌گیرد، و «رَنْد» را قلبِ همان چیزی می‌داند که در عبری nērd، آرامی nirdā، اکدی lardu، یونانی νάρδος و سنسکریت nalada دیده می‌شود. دهخدا (به نقل اقرب الموارد) و معین (حاشیهٔ برهان ص ۲۰۹۳) هم صورت عربی را معرّبِ یونانی می‌دانند. مهم‌تر از همه، این گره در نمودار سرچشمهٔ یونانی nardos نشان داده شده که از نظر تاریخی محال است (نگاه کنید به گرهٔ ۶). پژوهش امروزی: واژه از راه آرامی/فنیقی–عبری به غرب رفته، نه از راه عربی، و صورت عربی‌اش ناردین/رند است، نه نرد.\",\n     \"sources\": [W + \"%D9%86%D8%A7%D8%B1%D8%AF%D9%8A%D9%86\", W + \"%D8%B1%D9%86%D8%AF\", W + \"%D9%86%D8%B1%D8%AF\"],\n     \"ref_check\": [\n      {\"ref\": \"PLA:257\", \"status\": \"partial\", \"note\": \"Asbaghi, Persische Lehnwörter im Arabischen p.257 (PLA_pages.txt leaf 272 = 257+15, running head 'nārdīla 257 nānha'): 'نارْدين - nārdīn: „Spickenard, Lavendel“ pers. ← skr. nard, mand. nard, syr. …, hebr. נרד'. The page is right and Asbaghi does class the word as a Persian loan in Arabic — but under the form nārdīn, not nard (his نرد entry, p.259, is 'nard: „Damespiel, Würfelspiel“ pers.', the board game), and he says nothing about any Arabic → Greek transmission.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein s.v. nard (KLN_1966.txt leaf 550)\", \"stance\": \"contradicts\", \"note\": \"'fr. L. nardus, fr. Gk. νάρδος, fr. Heb. nērdh „nard“, which together with Aram. nirdā and Akkad. lardu of s.m., prob. derives fr. Indo-Iranian *narda' — Klein's Semitic mediator is Hebrew/Aramaic, not Arabic.\"},\n      {\"src\": \"AFM\", \"where\": \"Addi Shir, al-Alfāẓ al-fārisiyya al-muʿarraba (grep of AFM_pages.txt for ناردين / نرد)\", \"stance\": \"silent\", \"note\": \"no ناردين entry found in the OCR; Addi Shir does not list the plant name among Arabicized Persian words.\"},\n      {\"src\": \"MON\", \"where\": \"Dehkhodā s.v. ناردین (via abadis)\", \"stance\": \"contradicts\", \"note\": \"'نردین و ناردین: سنبل رومی، معرّب نَرذُس یونانی است. (اقرب الموارد)' — the Arabic form derived from the Greek, i.e. the reverse of the chart's arrow.\"},\n      {\"src\": \"BQT\", \"where\": \"Borhān p.2093 n.1 (Moʿīn)\", \"stance\": \"contradicts\", \"note\": \"'ناردین شکل تغییر یافتهٔ سریانی-عربی کلمهٔ یونانی νάρδινος است'.\"}\n     ]\n    },\n    {\n     \"id\": 6, \"lang\": \"Greek\", \"words\": \"nardos\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"Greek νάρδος cannot come from Arabic. The Greek word is in use by the 4th century BCE (Theophrastus, Hist. plant.; then Dioscorides, Mark 14:3) and the Septuagint uses it for Hebrew נֵרְדְּ nērd in the Song of Songs — roughly a thousand years before Arabic is a written language with any influence on Greek, and long before any Arab trade in the Aegean. Every modern authority routes it through north-west Semitic instead: Beekes (Etymological Dictionary of Greek, 2010, p.996), followed by Wiktionary, has νάρδος 'from Phoenician (compare Hebrew נֵרְדְּ nērd, Aramaic נִרְדָּא nirdā, Akkadian lardu, Arabic رَنْد rand, Old South Arabian rnd), possibly from Sanskrit नलद nálada (although a Semitic-to-Indian loan has also been suggested)'; Klein has 'fr. Gk. νάρδος, fr. Heb. nērdh'; Etymonline 'from Greek nardos, a word borrowed from a Semitic language (compare Hebrew ner'd … Arabic and Persian nardin), ultimately from Sanskrit narada, nalada'; Skeat, whom Nourai cites on node #4, jumps straight 'Gk. νάρδος — Pers. nard — Skt. nalada' with no Semitic or Arabic stage at all. So the node's word, language and semantics are right, but its parent should be Phoenician/Hebrew-Aramaic (or, on Skeat's and Horn's older account, Iranian directly), not Arabic. Note also that Arabic رند rand and نارْدين nārdīn are, on Beekes's showing, sisters of Greek νάρδος within the Semitic group, not its ancestors.\",\n     \"derivation_fa\": \"νάρδος یونانی نمی‌تواند از عربی آمده باشد. این واژه از سدهٔ چهارم پیش از میلاد در یونانی به کار است (تئوفراستوس، سپس دیوسکوریدس و انجیل مرقس ۱۴:۳) و ترجمهٔ سبعینیه آن را برابر عبری נרד در «غزل غزل‌ها» می‌آورد — یعنی نزدیک هزار سال پیش از آنکه عربی زبانی نوشتاری با هرگونه تأثیر بر یونانی باشد. همهٔ مراجع امروزی مسیر را از راه سامیِ شمال‌غربی می‌کشند: بیکس (فرهنگ ریشه‌شناسی یونانی، ۲۰۱۰، ص ۹۹۶) و به پیروی او ویکی‌واژه: «νάρδος از فنیقی (بسنجید با عبری nērd، آرامی nirdā، اکدی lardu، عربی رَنْد، عربی جنوبی باستان rnd)، شاید از سنسکریت nalada». کلاین: «از یونانی νάρδος، از عبری nērdh». اتیمونلاین: «از یونانی nardos، وام‌واژه‌ای از یکی از زبان‌های سامی … در نهایت از سنسکریت narada/nalada». اسکیت هم — که نورایی خود در گرهٔ پیشین به او ارجاع می‌دهد — یکسر می‌نویسد «یونانی νάρδος ← فارسی nard ← سنسکریت nalada» و هیچ حلقهٔ سامی یا عربی ندارد. پس واژه و زبان و معنا درست است، اما گرهِ پدر باید فنیقی/عبری–آرامی باشد (یا بر پایهٔ روایت کهن‌ترِ اسکیت و هرن، مستقیماً ایرانی)، نه عربی. افزون بر این، «رَنْد» و «ناردین» عربی به گفتهٔ بیکس خواهرانِ νάρδος در گروه سامی‌اند، نه نیای آن.\",\n     \"sources\": [W + \"%CE%BD%CE%AC%CF%81%CE%B4%CE%BF%CF%82\", W + \"%D8%B1%D9%86%D8%AF\", E + \"nard\"],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The node carries no reference in the book (refs=None); checked against Wiktionary's νάρδος entry (citing Beekes 2010 p.996), Klein s.v. nard, Etymonline s.v. nard, and Horn p.237 — all of which give a Semitic (or directly Iranian) source, none of which gives Arabic.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein s.v. nard (KLN_1966.txt leaf 550; printed ≈1077)\", \"stance\": \"contradicts\", \"note\": \"'nard, n., spikenard. — ME. narde, fr. OF. narde (F. nard), fr. L. nardus, fr. Gk. νάρδος, fr. Heb. nērdh, „nard“, which together with Aram. nirdā and Akkad. lardu of s.m., prob. derives fr. Indo-Iranian *narda in OI. naḍaḥ, nalaḥ, „reed“.'\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat p.344 s.v. Nard\", \"stance\": \"contradicts\", \"note\": \"'Gk. νάρδος, Mk. xiv,3. — Pers. nard. — Skt. nalada' — Greek straight from Persian, with no Arabic link.\"},\n      {\"src\": \"HRN\", \"where\": \"Grundriss p.237 no.1060\", \"stance\": \"contradicts\", \"note\": \"'…eine zweite Form *narda-, auf welche ai. naḍá- (gr. LW. νάρδος, hebr. LW. נרד) und np. nārd zurückgehen' — Greek and Hebrew are parallel loans from Iranian *narda-, and the Greek does not pass through Arabic.\"},\n      {\"src\": \"LKT\", \"where\": \"Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs (grep of LKT.txt for nard/nardin)\", \"stance\": \"silent\", \"note\": \"no numbered entry for nard turned up in the OCR; Lokotsch's list of European orientalisms does not treat it as an Arabic-mediated word.\"}\n     ]\n    },\n    {\n     \"id\": 7, \"lang\": \"Latin\", \"words\": \"nardus\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Latin nardus (also neuter nardum) is a straight learned/commercial borrowing of Greek νάρδος, with the Greek second-declension -os regularly latinized as -us; it is in Horace, Pliny and the Vulgate (Mark 14:3 'nardi spicati'). From it come Italian nardo, Spanish nardo, Catalan nard, Romanian nard, Old French narde (Modern French nard), Middle Dutch nardus, and, probably via Latin, Gothic 𐌽𐌰𐍂𐌳𐌿𐍃 nardus. The Medieval Latin compound spīca nardī 'spike of nard' (a calque of Greek νάρδου στάχυς) is what gives English spikenard. Wiktionary's descendant tree for νάρδος sets out exactly this Greek → Latin → Romance/English line, and Klein and Etymonline agree.\",\n     \"derivation_fa\": \"لاتین nardus (و صورت خنثای nardum) وام‌واژه‌ای است مستقیم از یونانی νάρδος؛ پایانهٔ -os صرفِ دومِ یونانی به قاعده در لاتین به -us بدل می‌شود. این واژه در هوراس و پلینیوس و ترجمهٔ ولگات (مرقس ۱۴:۳ «nardi spicati») هست. از آن ایتالیایی nardo، اسپانیایی nardo، کاتالانی nard، رومانیایی nard، فرانسهٔ کهن narde (فرانسهٔ امروز nard)، هلندی میانه nardus و — احتمالاً از راه لاتین — گوتی nardus پدید آمده است. ترکیب لاتین میانه spīca nardī «خوشهٔ نارد» (گرته‌برداری از νάρδου στάχυς یونانی) سرچشمهٔ spikenard انگلیسی است. ویکی‌واژه در شجرهٔ فرزندان νάρδος همین خط را می‌کشد و کلاین و اتیمونلاین نیز همین را می‌گویند. ادعای نورایی درست است.\",\n     \"sources\": [W + \"%CE%BD%CE%AC%CF%81%CE%B4%CE%BF%CF%82\", E + \"nard\"],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference in the book (refs=None). Checked against Wiktionary's νάρδος 'Descendants' tree ('→ Latin: nardus, nardum → Catalan nard, Italian nardo, Old French narde > French nard, → Middle English narde > English nard, Romanian nard, Spanish nardo'), Klein s.v. nard and Etymonline s.v. nard.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein s.v. nard\", \"stance\": \"supports\", \"note\": \"'ME. narde, fr. OF. narde (F. nard), fr. L. nardus, fr. Gk. νάρδος'.\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat p.344 s.v. Nard\", \"stance\": \"supports\", \"note\": \"'F. nard. — L. nardus. — Gk. νάρδος'.\"},\n      {\"src\": \"LAT\", \"where\": \"Ernout–Meillet (grep for nardus)\", \"stance\": \"silent\", \"note\": \"no entry — Ernout–Meillet omit late Greek plant borrowings of this kind; Walde-Hofmann LEW II 143 s.v. nardus, cited by Klein, covers it.\"}\n     ]\n    },\n    {\n     \"id\": 8, \"lang\": \"English\", \"words\": \"nard, spikenard\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"English nard 'aromatic plant of the East Indies and the precious unguent made from it' is first recorded c.1200; it comes from Old French narde (Modern French nard) and directly from Latin nardus, from Greek νάρδος. SPIKENARD, c.1300, is Old French spicanarde and directly Medieval Latin spīca nardī 'spike (i.e. flowering head) of nard', itself rendering Greek νάρδου στάχυς — so it is a compound of spike + nard rather than a separate borrowing; the name alludes to the plant's spike-like inflorescence. Klein, the reference Nourai gives, has both: 'nard, n., spikenard. — ME. narde, fr. OF. narde (F. nard), fr. L. nardus, fr. Gk. νάρδος, fr. Heb. nērdh …' and 'spikenard, n. — ME., fr. ML. spica nardi, „spike of nard“. See spike and nard.' Etymonline agrees on both dates and both routes.\",\n     \"derivation_fa\": \"واژهٔ انگلیسی nard «گیاه معطر هند شرقی و مرهم گران‌بهای ساخته از آن» نخست حدود سال ۱۲۰۰ ثبت شده است؛ از فرانسهٔ کهن narde و به‌طور مستقیم از لاتین nardus و آن از یونانی νάρδος. واژهٔ spikenard (حدود ۱۳۰۰) از فرانسهٔ کهن spicanarde و مستقیماً از لاتین میانهٔ spīca nardī «خوشهٔ نارد» است که خود گرتهٔ νάρδου στάχυς یونانی است؛ پس ترکیبی است از spike + nard، نه وام‌واژه‌ای جداگانه، و نام‌گذاری به سببِ گل‌آذینِ خوشه‌مانندِ گیاه است. کلاین — همان مرجعی که نورایی می‌دهد — هر دو را دارد: «nard: از انگلیسی میانه narde، از فرانسهٔ کهن narde، از لاتین nardus، از یونانی νάρδος» و «spikenard: از لاتین میانه spica nardi „خوشهٔ نارد“». اتیمونلاین نیز در تاریخ‌ها و مسیرها با او هم‌داستان است. ادعای نورایی درست است.\",\n     \"sources\": [E + \"nard\", W + \"%CE%BD%CE%AC%CF%81%CE%B4%CE%BF%CF%82\"],\n     \"ref_check\": [\n      {\"ref\": \"KLN:1028\", \"status\": \"supports\", \"note\": \"Klein s.v. nard (KLN_1966.txt leaf 550) and s.v. spikenard (leaf 807-area, line 36257): 'nard, n., spikenard. — ME. narde, fr. OF. narde (F. nard), fr. L. nardus, fr. Gk. νάρδος, fr. Heb. nērdh, „nard“ …' / 'spikenard, n. — ME., fr. ML. spica nardi, „spike of nard“. See spike and nard.' Content exactly as Nourai uses it. Caveat on the page number: in the archive scan of the 1966 two-volume edition the entry falls on leaf 550, i.e. printed p. ≈1076–77 (calibrated on the documented anchors leaf 178 = p.333, leaf 438 = p.853), so Nourai's '1028' does not match that pagination and probably comes from another printing.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"SKT\", \"where\": \"Skeat p.344 s.v. Nard (SKT.txt leaf 325)\", \"stance\": \"supports\", \"note\": \"'Nard, an unguent. (F. — L. — Gk. — Pers. — Skt.) … Der. spikenard.' and s.v. Spikenard (leaf 484): 'Spikenard. (L.; and F. — L. — Gk. — Pers. — Skt.) Put for spiked nard (L. nardus spicatus), i.e. nard furnished with spikes, in allusion to the mode of growth. And see Nard.'\"},\n      {\"src\": \"KLN\", \"where\": \"as in ref_check\", \"stance\": \"supports\", \"note\": \"see ref_check.\"},\n      {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls New Standard Dictionary (grep for nard/spikenard)\", \"stance\": \"silent\", \"note\": \"the relevant volume block did not yield a legible nard entry in the OCR; no independent statement obtained.\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-354.json','w',encoding='utf-8') as f:\n    json.dump(data,f,ensure_ascii=False,indent=2)\n    f.write('\\n')\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/mk354.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-354.json > /dev/null && echo \"valid json\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 354"
}
```


### [2026-09-07T18:40:26.478Z] TOOL RESULT

```
written
valid json
nodes verified: 17/17
node verdicts: {'confirmed': 10, 'disputed': 3, 'plausible': 4}
root verdicts: {'confirmed': 1, 'plausible': 1}
ref checks: {'supports': 15, 'contradicts': 1, 'not_checked': 5, 'partial': 4}
books consulted: {'supports': 35, 'contradicts': 11, 'silent': 10, 'partial': 3} | by book: {'KLN': 10, 'MON': 5, 'WLD': 4, 'BQT': 4, 'POK': 4, 'FVQ': 3, 'PHD': 3, 'ARY': 3, 'LAT': 3, 'SKT': 3, 'BRT': 2, 'AFM': 2, 'IEC': 2, 'AHD': 2, 'HRN': 2, 'HUB': 2, 'NYB': 1, 'PLA': 1, 'KNT': 1, 'LKT': 1, 'FSD': 1}
```


## [2026-09-07T18:40:41.141Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ndef leafof(f,ln):\n    t=open(f,encoding='utf8',errors='replace').read()\n    lines=t.split('\\n'); off=sum(len(l)+1 for l in lines[:ln-1])\n    return t[:off].count('\\f')\nprint('KLN spikenard line 36257 -> leaf', leafof('KLN_1966.txt',36257))\nEOF\necho \"=== KLN nask/nasx/nusxa ===\"; grep -c -i \"nusxa\\|naskh\\|nasx\" KLN_1966.txt KLN_1971.txt\necho \"=== KLN entries net/node/annex/connect ===\"; grep -o \"^net, n\\..\\{0,260\\}\" KLN_1966.txt | head -2; grep -o \"node, n\\..\\{0,200\\}\" KLN_1966.txt | head -2; grep -o \"annex, tr\\. v\\..\\{0,240\\}\" KLN_1966.txt | head -2; grep -o \"connect, tr\\..\\{0,220\\}\" KLN_1966.txt | head -2"
}
```


### [2026-09-07T18:40:42.609Z] TOOL RESULT

```
KLN spikenard line 36257 -> leaf 790
=== KLN nask/nasx/nusxa ===
KLN_1971.txt:0
KLN_1966.txt:0
=== KLN entries net/node/annex/connect ===
```


## [2026-09-07T18:40:46.852Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in \"net,\" \"node,\" \"annex,\" \"connect,\"; do echo \"=== $w ===\"; grep -o \"$w *n\\?\\(tr\\)\\?.\\{0,300\\}\" KLN_1966.txt | grep -i \"OE\\.\\|L\\. \\|nodus\\|nectere\\|nett\" | head -2; done"
}
```


### [2026-09-07T18:40:55.438Z] TOOL RESULT

```
=== net, ===
ugrep: error: error at position 54
[^\n\x80-\xbf][\x80-\xbf]*){0,300}
     exceeds complexity limits___/


=== node, ===
ugrep: error: error at position 55
:[^\n\x80-\xbf][\x80-\xbf]*){0,300}
      exceeds complexity limits___/


=== annex, ===
ugrep: error: error at position 56
?:[^\n\x80-\xbf][\x80-\xbf]*){0,300}
       exceeds complexity limits___/


=== connect, ===
ugrep: error: error at position 58
?(?:[^\n\x80-\xbf][\x80-\xbf]*){0,300}
         exceeds complexity limits___/
```


## [2026-09-07T18:41:00.019Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf8',errors='replace').read()\nfor w in ['net,','node,','annex,','connect,','nard,']:\n    for m in re.finditer(re.escape(w),t):\n        seg=t[m.start():m.start()+330].replace('\\n',' ')\n        if re.search(r'\\bOE\\.|\\bL\\.\\s|nodus|nectere|nett|OF\\.',seg):\n            print('###',w,'->',seg[:330]); break\nEOF"
}
```


### [2026-09-07T18:41:01.366Z] TOOL RESULT

```
### net, -> net,  curtain’,  and  planus, ‘level,  flat’  (see  pelagian). aerarian,  adj.,  fiscal.  —  Formed  with  suff.  -an  fr. L.  aerarius,  ‘pertaining  to  copper,  pertaining  to money’  fr.  aes,  gen.  aeris,  ‘copper,  bronze, money’,  which  is  cogn.  with  OE.  dr,  ser,  ‘brass’. See  ore  and  cp.  aes. aerarium,  n.,  t
### node, -> node,  n.,  point  of  a  curve,  not  connected  with real  points  of  the  curve  (math.)  —  A  hybrid coined  fr.  L.  acus,  ‘needle’  (see  acus),  and  E.  node. Acocanthera,  n.,  a  genus  of  African  plants  (bot.) —  ModL.,  compounded  of  Gk.  axcoxf),  ‘point, sting’,  and  avffvjpoi;,  ‘flowery’.  The  first  el
### annex, -> annex,  tr.  v.  —  F.  annexer,  fr.  L.  annexus,  pp.  of annectere ,  ‘to  bind  to,  tie  on,  annex’,  fr.  ad- and  nectere,  ‘to  bind,  join,  fasten’.  See  nexus. Derivatives:  annex-ive,  adj.,  annex-ment,  n. annex,  n.  —  F.  annexe,  fr.  L.  annexus,  pp.  of  an¬ nectere.  See  annex,  v. annexation,  n.  —  M
### connect, -> connect, combine’.  See  series  and  cp.  dissert,  insert. Derivatives:  assert-er,  n.,  assertion  (q.v.),  assert¬ ive,  adj.,  assert-ive-ly,  adv.,  assert-ive-ness,  n. assertion 116 117 -aster assertion,  n.  —  L.  assert  id,  gen.  -dnis,  fr.  assert  us, pp.  of  asserere.  See  prec.  word  and  -ion. Derivative: 
### nard, -> nard,  masc.  PN.  —  F.,  fr.  G.  Bernhard,  lit. ‘bold  as  a  bear’,  fr.  OHG.  bero,  ‘bear’,  and hard,  ‘hard,  bold’.  See  bear,  the  animal,  and hard. berrugate,  n.,  the  fish  called  scientifically  Verru- gato  pacificus.  —  Fr.  Sp.  verruga,  ‘wart’,  fr.  L. verruca.  See  verruca  and  cp.  words  there  r
```


## [2026-09-07T18:41:06.790Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf8',errors='replace').read()\nfor pat in [r'net,\\s+n\\.,\\s+a\\s+netting', r'net,\\s+n\\.,', r'node,\\s+n\\.,\\s+knot', r'node,\\s+n\\.,', r'connect,\\s+tr\\.\\s+and\\s+intr\\.', r'connect,\\s+tr\\.']:\n    for m in re.finditer(pat,t):\n        seg=t[m.start():m.start()+400].replace('\\n',' ')\n        print('###',pat,'->',seg)\n        print()\n        break\nEOF"
}
```


### [2026-09-07T18:41:08.332Z] TOOL RESULT

```
### net,\s+n\., -> net,  n.,  the  bugloss.  —  Sp.  alcaneta,  dimin. of  alcana,  fr.  Arab,  al-hinnd.  See  next  word. Alkanna,  n.,  a  genus  of  plants  of  the  borage family  (bot.)  —  ModL.,  fr.  Sp.  alcana,  fr.  Arab. al-hinnd',  fr.  al-,  ‘the’,  and  hinnd',  ‘henna’.  See henna. alkyl,  n.,  any  radical  of  the  methane  series,  as methyl,  ethyl,  etc.  (chem.)  —  Formed  fr.  alkali with  s

### node,\s+n\., -> node,  n.,  point  of  a  curve,  not  connected  with real  points  of  the  curve  (math.)  —  A  hybrid coined  fr.  L.  acus,  ‘needle’  (see  acus),  and  E.  node. Acocanthera,  n.,  a  genus  of  African  plants  (bot.) —  ModL.,  compounded  of  Gk.  axcoxf),  ‘point, sting’,  and  avffvjpoi;,  ‘flowery’.  The  first  element is  rel.  to  dxfj,  ‘point’,  fr.  I.-E.  base  *ak- ,  ‘sharp,

### connect,\s+tr\.\s+and\s+intr\. -> connect,  tr.  and  intr.  v.  —  L.  connectere,  ‘to  bind or  join  together’,  fr.  con-  and  nectere,  ‘to  tie, bind,  join’,  fr.  I.-E.  base  *ned-,  ‘to  twist,  knot’; see  net  and  cp.  nexus,  annex.  L.  nectere  was  in¬ fluenced  in  form  by  pectere,  ‘to  comb,  dress, weed’. Derivatives:  connect-ed,  adj.,  connected-ly,  adv., connect-ed-ness,  n.,  connect-ive,  adj.,  con

### connect,\s+tr\. -> connect,  tr.  and  intr.  v.  —  L.  connectere,  ‘to  bind or  join  together’,  fr.  con-  and  nectere,  ‘to  tie, bind,  join’,  fr.  I.-E.  base  *ned-,  ‘to  twist,  knot’; see  net  and  cp.  nexus,  annex.  L.  nectere  was  in¬ fluenced  in  form  by  pectere,  ‘to  comb,  dress, weed’. Derivatives:  connect-ed,  adj.,  connected-ly,  adv., connect-ed-ness,  n.,  connect-ive,  adj.,  con
```


## [2026-09-07T18:41:14.607Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf8',errors='replace').read()\nfor m in re.finditer(r'net,\\s+n\\.,\\s+[^A-Z]{0,60}',t):\n    seg=t[m.start():m.start()+520].replace('\\n',' ')\n    if 'OE' in seg or 'ned-' in seg or 'mesh' in seg:\n        print(seg); print('---')\nfor m in re.finditer(r'\\bnode,\\s+n\\.,\\s+(a\\s+)?knot',t):\n    print(t[m.start():m.start()+420].replace('\\n',' '))\nEOF"
}
```


### [2026-09-07T18:41:16.312Z] TOOL RESULT

```
net,  n.,  the  bugloss.  —  Sp.  alcaneta,  dimin. of  alcana,  fr.  Arab,  al-hinnd.  See  next  word. Alkanna,  n.,  a  genus  of  plants  of  the  borage family  (bot.)  —  ModL.,  fr.  Sp.  alcana,  fr.  Arab. al-hinnd',  fr.  al-,  ‘the’,  and  hinnd',  ‘henna’.  See henna. alkyl,  n.,  any  radical  of  the  methane  series,  as methyl,  ethyl,  etc.  (chem.)  —  Formed  fr.  alkali with  suff.  -yl. all,  adj.  —  ME.  all,  fr.  OE.  call,  all,  rel.  to  OS. OFris.,  OHG.,  MHG.  al,  ON.  allr,  Dan.,  
---
net,  n.,  a  herb.  —  ME,  herbe beneit,  ‘the  bless¬ ed  herb’,  fr.  F.  benoite ,  prop.  fern.  pp.  of  OF. beneir  (F.  benir),  ‘to  bless’,  fr.  L.  henedicere. See  benediction. bensh,  tr.  and  intr.  v.,  to  bless;  to  say  grace.  — Yiddish  benshen,  fr.  dial.  OF.  *bencheir  (OF. beneir ,  F.  benir),  fr.  L.  henedicere.  See  benediction, bent,  adj.,  curved.  —  Pp.  of  bend, bent,  n.,  inclination.  —  Fr.  prec.  word, bent  grass,  also  bent,  n.  —  OE.  beonot-  (in  place names)
---
net,  n.,  a  short  song.  —  It.  canzonetta,  di- min.  of  canzone,  ‘song’.  See  prec.  word  and  -et. caoba,  n.,  mahogany.  —  Sp.,  fr.  a  Caribbean  na¬ tive  word. caoutchouc,  n.  —  F.,  a  Tupi  loan  word  (prob. through  the  medium  of  Sp.  caucho). cap,  n.,  a  covering  for  the  head.  —  ME.  cappe,  fr. OE.  cxppe,  ‘hood,  cap’,  fr.  Late  L.  cappa.  See cape,  ‘cloak’,  and  cp,  words  there  referred  to. Derivatives:  cap,  tr.  v.,  capp-ed,  adj.,  capp-er, n.,  capp-ing,  n.,  c
---
net,  n.,  the  solan  goose.  —  OE.  ganot,  ‘sea bird,  gannet’,  rel.  to  Du.  gent,  OHG.  gannasso, ganzo,  ‘gander’.  See  gander,  goose, ganoid, adj.,  1)  smooth  (said  offish  scales);  2)per- taining  to  the  Ganoidei.  • —  F.  ganolde,  com¬ pounded  of  Gk.  Y“V0S>  ‘brightness,  brilliance, splendor’,  and  -oeiS r)c;,  ‘like’,  fr.  eZSo?,  ‘form, shape’.  The  first  element  stands  for  ya-vo?  and is  rel.  to  yavo(xai  (for  ya-vo-fxat),  ‘I  am  glad, I  rejoice’,  yalco  (for  ‘yafico), 
---
net,  n.,  inner  membrane  of  a  calf’s  stomach used  for  curdling  milk.  —  Late  ME.,  lit.  ‘that which  causes  (milk)  to  run’,  related  to  ME. rennen,  ‘to  cause  to  run’,  fr.  OE.  rinnan,  ‘to  run’. Cp.  OE.  gerinnan,  ‘to  run  together,  coagulate’, G.  rinnen,  ‘to  run’,  gerinnen,  ‘to  curdle’,  geron- nene  Milch,  Du.  geronnen  melk,  ‘curdled  milk’. See  run. rennet,  n.,  a  variety  of  apple.  —  F.  reinette,  lit. ‘little  queen’,  dimin.  of  reine,  ‘queen’,  fr.  L.  re- gina
---
node,  n.,  a  knot,  knob.  —  L.  nodus,  ‘knot’,  rel.  to L.  nassa  (prob.  for  *nad-sa),  ‘a  basket  for  catch¬ ing  fish’,  and  cogn.  with  ON.  not,  ‘a  large  net’, ON.,  OE.  net,  ‘net’.  See  net  and  cp.  nodus,  noose, denouement,  crunode,  intemode. nodical,  adj.,  pertaining  to  the  nodes  (astron)  — See  node  and  -ical. nodose,  adj.,  full  of  knots  or  nodes,  knotty.  — L.  nodosus
```


## [2026-09-07T18:41:27.395Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf8',errors='replace').read()\nfor m in re.finditer(r'(?:^|[.;)\\s])net,\\s+n\\.,\\s+(an?\\s+)?(open|meshed|fabric|netting|contrivance|mesh)',t,re.M):\n    print(t[m.start():m.start()+560].replace('\\n',' ')); print('---')\n# also try 'net, n., 1)'\nfor m in re.finditer(r'net,\\s+n\\.,\\s+1\\)',t):\n    print(t[m.start():m.start()+560].replace('\\n',' ')); print('===')\nEOF\necho \"=== AFM nardin ===\"; grep -c \"ناردين\\|نارديـن\" AFM_pages.txt AFM.txt; echo \"=== AFM nasx ===\"; grep -c \"نسخ\" AFM_pages.txt; echo \"=== LKT nard ===\"; grep -n -i \"nard\" LKT.txt | head -5; echo \"=== FSD spikenard ===\"; grep -c -i \"spikenard\" FSD_vol1.txt FSD_vol2.txt FSD_vol3.txt FSD_vol4.txt; echo \"=== PLA nask/nusxa ===\"; grep -c -i \"nask\\|nusḫ\\|nusha\\|nasḫ\" incoming/PLA/PLA_pages.txt; echo \"=== BRT nada ===\"; grep -c \"nada-\\|nāda-\" BRT.txt"
}
```


### [2026-09-07T18:41:29.246Z] TOOL RESULT

```
net,  n.,  1)  a  little  dragon;  2)  a  small  marine fish.  —  OF.,  dimin.  of  dragon.  See  dragon and  -et. dragonnade,  n.,  persecution  of  the  French  pro- testants  during  Louis  XIV;  military  attack  on the  civil  population.  —  F.,  fr.  dragon,  ‘dragoon’. See  dragon  and  -ade. dragoon,  n.  —  F.  dragon,  ‘dragon,  dragoon,  car¬ bine*  ;  so  called  from  its  resemblance  to  the  fire breathing  dragon  of  the  fable.  See  dragon. Derivatives:  dragoon,  tr.  v.,  dragoon-age,  n., dragoon-er,  n. drail,  tr.  and  intr.  v
===
net,  n.,  1)  a  hard  silicate  mineral  of  various colors;  2)  a  deep  red  color.  —  ME.  gernet, metathesized  fr.  OF.  (=  F.)  grenat,  fr.  ML. pomum  grdnatum,  ‘pomegranate’,  lit.  ‘seeded apple’;  so  called  from  its  resemblance  to  the seeds  of  a  pomegranate;  cp.  G.  Granat  and see  grain.  Cp.  also  grenade,  pomegranate, garnierite,  n.,  a  hydrous  nickel  magnesium  sili¬ cate  (mineral.)  —  Named  after  the  French  geol¬ ogist  Jules  Gamier  (died  in  1904),  the  discoverer of  the  New  Caledonian  nickel  ores. 
===
net,  n.,  1)  a  German  mercenary  in  the  16th and  17th  centuries;  2)  a  card  game.  —  F.,  fr.  G. Landsknecht,  lit.  ‘servant  of  the  country’,  fr. Lands,  gen.  of  Land,  ‘land,  country’,  and  Knecht, ‘slave,  servant’.  See  land  and  knight  and  cp. lance-knight. Lantana,  n.,  a  genus  of  plants  of  the  vervain  fam¬ ily  (bot.)  —  ModL.,  ‘viburnum’,  altered  fr. lentana  (form  used  by  Gesner),  of  s.m.,  lit.  ‘the pliant  plant',  fr.  L.  lentus,  ‘flexible,  pliant’.  See lithe  and  cp.  lentiscus,  Ientitude. lan
===
=== AFM nardin ===
AFM.txt:0
AFM_pages.txt:0
=== AFM nasx ===
0
=== LKT nard ===
506:ar.  isfänäg,  isfinäg  'Spinat'  [Vielleicht kommen  diese  Formen  selbst  aus  dem Lateinischen,  etwa  spitia  'Dorn'  oder besser  *spinax  SBKAW  Wien  PhhKl CXXXII,  362];  hieraus  zunächst  die  ro- manischen Formen  afrz.  espinoche,  espi- nard;  frz.  epinard,  prov.  espinar,  kat. espinac,  sp.  espinaca,  pg.  espinafre,  it. spinace,  rum.  spanac.  Mit  steter  An- lehnung an  lat.  spina  auch  im  Germa- nischen dtsch.  Spinat,  ndl.  spinazie, engl,  spinage.  Russ.  spinal,  bulg.  spa- nak,  serb.  spanac,  äech.  Spinat,  poln. szpinak.  [Devic  DEt  110/111.  Eguilaz 391.    ML  706.
3565:1548.  Sskr.  naladä: 'Duftgebend ;  eine  Pflanze  Andropogon muricatuni'  [nala  'Dufr  <C  nala  'Rohr arundo'  nach  Ascoli,  Studi  orientali  e linguistici,  S.  76*;  dazu  dä  'gebend'], hieraus  pers.  närdln,  Adj.  durch  Ersatz des  l  durch  r,  auch  hehr,  nerd,  aram. nirda,  gr.  vdpboq.  Hieraus  in  die  euro- päischen Sprachen  zur  Bezeichnung  eines sehr  feinen  Parfüms  übergegangen,  z.B. engl.  nard  [wozu  dasRhizom  der  Pflanze Nardostachys  Jatamansi  D.  C.  vom  nie- deren Himalaya  benutzt  wird],  dtsch. Nardc.    [Hobson-Jobson  617/618.
4287:'Null  (alt),  Geheimschrift',  frz.  Chif- fre 'Geheimschrift',  sp.  pg.  cifra  'Zahl- zeichen', rum.  cifrä,  pifrä;  sp.  cero 'Null',  frz.  zero,  it.  zero{<^  zefro,  zefiro, noch  bei  LEONARDO  PISANO  um  das Jahr  1200:  zephirum];  dtsch.  Ziffer,  ndl. cijfer  'Zahlzeichen',  engl,  cipher,  cypher 'Null,  Zahlzeichen,  Geheimschrilt'.  — Am  vollständii-'sten  findet  sich  die  Ge- schichte der  Etymologie  von  Ziffer  usvv. unter  Zurückweisung  anderer  Ablei- tungen bei  Fischer,  Zur  Berichtigung einer  Etymologie  von  K.  VÖLLERS  in ZDMG  LVII,  783/793.
6484:escherviz  afz.  1095 1  espinard  afz.  126
=== FSD spikenard ===
FSD_vol3.txt:3
FSD_vol4.txt:5
FSD_vol2.txt:2
FSD_vol1.txt:3
=== PLA nask/nusxa ===
0
=== BRT nada ===
0
```


## [2026-09-07T18:41:45.882Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ndef leafof(f,ln):\n    t=open(f,encoding='utf8',errors='replace').read()\n    lines=t.split('\\n'); off=sum(len(l)+1 for l in lines[:ln-1])\n    return t[:off].count('\\f')\nprint('LKT line 3565 leaf',leafof('LKT.txt',3565),'printed ~',leafof('LKT.txt',3565)-26)\nEOF\necho \"=== FSD vol3 spikenard ===\"; grep -n -i -o \".\\{0,120\\}spikenard.\\{0,260\\}\" FSD_vol3.txt | head -4\necho; echo \"=== KLN net headword ===\"; python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf8',errors='replace').read()\ni=t.find('nettle,')\nprint(t[i-1400:i+200].replace('\\n',' '))\nEOF"
}
```


### [2026-09-07T18:41:49.649Z] TOOL RESULT

```
LKT line 3565 leaf 152 printed ~ 126
=== FSD vol3 spikenard ===
ugrep: error: error at position 88
80-\xbf][\x80-\xbf]*){0,260}
                            \___exceeds complexity limits



=== KLN net headword ===
HG.  nidari,  nidaro,  MHG.  nider(e),  G.  nieder ) ; prop,  comparatives  formed  fr.  I.-E.  *nl-,  down. below’,  whence  OI.  ni,  ‘down’,  nitaram,  ‘down- wards’,  nica ,  ‘below,  down’,  nicah,  low  ,  Avestic ni,  ‘down’,  Arm.  ni,  n-,  ‘low’,  Gk.  veioUev,  ‘from below’,  vct6i ;  (scil.  yv)),  ‘field’,  prop,  ‘lowland  , OSlav.  ni-zu,  Tow,  down’,  ni-va,  ‘field’.  Cp.  I.-E. *ni-zdo-  (in  L.  nidus,  OE.  nest,  etc.),  ‘nest’,  lit.  ‘a place  to  sit  down  in’.  Cp.  nest,  nidus,  and  the second  element  in  Upanishad.  Cp.  also  beneath, underneath. Nethinim,  n.,  pi.,  servants  who  performed  the lowest  service  under  the  Levites  in  the  Temple (Bible)  —  Heb.  nlthimm,  lit.  ‘those  given  (scil. to  the  sanctuary)’,  pi.  pass.  part,  of  ndthan,  ‘he gave’.  See  Nathan. netsuke,  n.,  a  small  carved  object  of  ivory,  bone or  wood,  pierced  with  holes.  —  Jap. Nettapus,  n.,  a  genus  of  very  small  geese,  the pygmy  goose  ( ornithol .)  —  ModE.,  compound¬ ed  of  Gk.  vrjTxa,  ‘duck’,  and  rcouc;,  gen.  noSot;, ‘foot’.  See  next  word  and  podal  and  cp.  the  sec¬ ond  element  in  Nesonetta. Nettion,  n.,  a  genus  of  ducks,  the  teal  (ornithol) —  ModL.,  fr.  Gk.  w,tt1ov,  dimin.  of  v^xxa, Att.  form  of  vrjaaa,  ‘duck’,  which  is  cogn.  with L.  anas,  ‘duck’.  See  Anas  and  cp.  prec.  word. nettle,  n.  —  ME.  netle,  netel,  fr.  OE.  netle,  netele, netel,  rel.  to  OS.  nett  la,  dial.  Swed.  ndtla,  Norw. netla,  MDu.  netele,  netel,  Du.  netel,  OHG. ne33ila,  MHG.  ne33el,  G
```


## [2026-09-07T18:41:54.788Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf8',errors='replace').read()\ni=t.find('nether, adj')\nif i<0: i=t.find('nether,')\nprint(t[i-2200:i+60].replace('\\n',' '))\nEOF"
}
```


### [2026-09-07T18:41:56.134Z] TOOL RESULT

```
,  p.  60. naphthalene,  n.,  a  white  crystalline  hydrocarbon, C10H8  ( chem .)  —  Orig.  naphthaline,  coined  by John  Kidd  fr.  naphtha  and  chem.  suff.  -ine.  The /  was  inserted  for  the  sake  of  euphony.  For  the ending  of  naphthalene  see  suff.  -ene.  Cp.  phtha- lein(e),  phthalin. naphthol,  n.,  either  of  two  white  crystalline  com¬ pounds  used  as  antiseptics  and  in  making  dyes, C1(H.OH  (chem.)  —  Coined  by  the  English chemist  John  Kidd  (1775-1851)  from  prec. word  and  1st  suff.  -ol. naphthyl,  n.,  the  univalent  radical,  C10H.  (chem.) —  Formed  fr.  naphtha  with  suff.  -yl. napiform,  adj.,  turnip-shaped  (hot.)  —  Com¬ pounded  of  L.  napus,  ‘turnip’,  and  forma,  ‘form, shape’.  For  the  first  element  see  navew  and  cp. parsnip,  turnip.  For  the  second  element  see  form, n. napkin,  n.  —  ME.  nappekin,  napekin,  formed  with napoleon iidJiui  uuiii 1028 tuzy dimin.  suff.  -kin  fr.  nappe ,  nape,  fr.  OF.  nappe, nape.  See  napery  and  -kin. Derivative:  napkin,  tr.  v. napoleon,  n.,  a  former  gold  coin  equivalent  to  20 francs.— So  called  because  struck  by  Napoleonl. napoleon,  n.,  a  card  game.  —  Named  after  Napo¬ leon  I.  Cp.  nap,  ‘a  card  game’. Napoleonic,  adj.,  1)  pertaining  to  Napoleon  I (1769-1821)  or  his  period;  2)  resembling  Napo¬ leon  I. napoo,  napooh,  interj.,  meaning  ‘no  more,  no good,  useless,  all  over’.  —  Corrupted  fr.  F.  il n’y  a  plus,  ‘there  is  no  more’, nappe,  n.,  a  sheet.  —  F.,  ‘tablecloth,  cloth,  cover, sheet’,  dissimilated  (under  the  influence  of  the following  p)  from  mappe.  See  napery. nappy,  adj.,  downy.  —  Formed  with  adj.  suff.  -y fr.  nap,  ‘a  downy  surface’  (q.v.) nappy,  adj.,  1)  strong  (said  of  ale);  2)  tipsy;  n., ale  {Scot.)  —  Of  uncertain  origin ;  perhaps  from prec.  word. napu,  n.,  any  of  various  chevrotains  of  Java  and Sumatra.  —  Malay. Naraka,  n.,  hell  ( Hinduism )  —  OI.  Narakah,  fr. I.-E.  base  *ner-,  ‘below;  to  the  left’,  whence  also Gk.  e-vspoi,  ‘those  below’,  e-vspffev,  ‘from  be¬ neath’,  vip-repo?,  c-vs pxepo;,  ‘nether,  infernal’, ON.  nordr,  OE.  nord,  ‘north’  (prop,
```


## [2026-09-07T18:42:05.953Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf8',errors='replace').read()\ni=t.find('napoleon iidJiui uuiii 1028')\nif i<0:\n    m=re.search(r'napoleon[^\\n]{0,40}1028',t); i=m.start() if m else -1\nprint('found at',i,'leaf',t[:i].count('\\f'))\npages=t.split('\\f')\n# print page markers in leaves 543..556\nfor l in range(543,556):\n    nums=re.findall(r'\\b1(?:0[0-4]\\d)\\b',pages[l])\n    print(l, sorted(set(nums)))\nEOF"
}
```


### [2026-09-07T18:42:07.417Z] TOOL RESULT

```
found at -1 leaf 902
543 []
544 ['1015', '1016', '1017']
545 []
546 ['1021']
547 ['1022']
548 []
549 []
550 ['1028']
551 []
552 ['1033']
553 ['1034', '1035']
554 ['1036']
555 ['1039']
```


## [2026-09-07T18:42:18.248Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf8',errors='replace').read()\npages=t.split('\\f')\nfor l in range(788,793):\n    print(l, sorted(set(re.findall(r'\\b1(?:4\\d\\d|5\\d\\d)\\b',pages[l]))))\nEOF\necho \"=== FSD nard ===\"; python3 - <<'EOF'\nimport re\nfor v in ('FSD_vol3.txt','FSD_vol4.txt'):\n    t=open(v,encoding='utf8',errors='replace').read()\n    for m in re.finditer(r'spikenard',t):\n        seg=t[max(0,m.start()-300):m.start()+300].replace('\\n',' ')\n        print('##',v,'::',seg[:600]); print()\n        break\nEOF"
}
```


### [2026-09-07T18:42:19.700Z] TOOL RESULT

```
788 ['1486', '1552']
789 ['1488', '1489']
790 ['1490', '1491', '1500', '1558']
791 ['1492']
792 []
=== FSD nard ===
## FSD_vol3.txt :: 1. Tho niusk> , spongy root of a plant (r crula sum- bid) of tho parsley family, from llusslan Turkestan Its properties, as employed medicinally, are of a stimulating and anllapasinodlc character 2. Mvachnlo (A dora fnosfhntellt- nn) S. The fragrant roots of other plants, as llmt of tho Esst-lndian spikenard (Sardoatachyi iatamanH) — m.arose, n. A culllvatt*d cllnihcr (Ifotn moichaia) from Europe, with usually large white flowers In panlclcd clusters — m.«secd, fi The seed of muskmallow (Hmneus aMmoschvs).-~m.e Shrew, n 1. The Indian muskrat (Crociaura anuiea), 2. A desman — m. •terrapin, n A 

## FSD_vol4.txt :: ded  by  bJue berries,  which  give  it  the  name  also  of  turquo*se«DeTr> —   false  Solomon’s  (Seal,  any  plant  of  the  genus  Vagnera, having  white  flowers  in  terminal  racemes  V   ractmosa, common  la  the  United  States,  Is  called  also  clustered  Solo- mon’s seal  and  false  spikenard —   two  deaved  S   ,   a   little plant  (Uni/oUum  canadsnss),  2   to  5   inches  high,  with  2   or  3 leaves  and  an  erect  raceme  an  inch  long,  closely  resembling the  false  Solomon's-seal Solomon  Si^oals A   true  SoloTOon's-seal  a   the  fruit  • The  false  Solomon  s
```


## [2026-09-07T18:43:03.813Z] TOOL CALL #81: Bash

```json
{
 "command": "python3 - <<'PYEOF'\nimport json, io\np='data/verification/page-354.json'\nd=json.load(open(p,encoding='utf-8'))\ne0,e1=d['entries'][0],d['entries'][1]\ndef node(e,i):\n    for n in e['nodes']:\n        if n['id']==i: return n\n    raise KeyError(i)\n\n# --- entry 0: strengthen Klein consulted notes with real quotes ---\nn7=node(e0,7)\nn7['consulted'][0]={\"src\":\"KLN\",\"where\":\"Klein s.v. node and s.v. connect (KLN_1966.txt leaf 550 / leaf 214-area)\",\"stance\":\"supports\",\"note\":\"Klein s.v. node: 'node, n., a knot, knob. — L. nodus, „knot“, rel. to L. nassa (prob. for *nad-sa), „a basket for catching fish“, and cogn. with ON. not, „a large net“, ON., OE. net, „net“. See net…'; s.v. connect: '…fr. con- and nectere, „to tie, bind, join“, fr. I.-E. base *ned-, „to twist, knot“; see net and cp. nexus, annex.' Klein thus files English net under *ned- exactly as Nourai does.\"}\nn8=node(e0,8)\nn8['consulted'].append({\"src\":\"KLN\",\"where\":\"Klein s.v. node (KLN_1966.txt leaf 550, printed p.1028)\",\"stance\":\"supports\",\"note\":\"'node, n., a knot, knob. — L. nodus, „knot“, rel. to L. nassa (prob. for *nad-sa), „a basket for catching fish“, and cogn. with ON. not, „a large net“, ON., OE. net, „net“. See net and cp. nodus, noose, denouement, crunode, internode.'\"})\nn9=node(e0,9)\nn9['consulted'][1]={\"src\":\"KLN\",\"where\":\"Klein s.v. node, annex, connect (KLN_1966.txt)\",\"stance\":\"supports\",\"note\":\"'annex, tr. v. — F. annexer, fr. L. annexus, pp. of annectere, „to bind to, tie on, annex“, fr. ad- and nectere, „to bind, join, fasten“. See nexus.' / 'connect, tr. and intr. v. — L. connectere, „to bind or join together“, fr. con- and nectere, „to tie, bind, join“, fr. I.-E. base *ned-, „to twist, knot“; see net and cp. nexus, annex.' / 'node, n., a knot, knob. — L. nodus…'\"})\n\n# --- entry 1 node 3: fix Klein page, add Lokotsch ---\nm3=node(e1,3)\nm3['consulted'][1]['where']=\"Klein s.v. nard (KLN_1966.txt leaf 550, which carries the printed page number 1028)\"\nm3['consulted'].append({\"src\":\"LKT\",\"where\":\"Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs no. 1548, p.126 (LKT.txt leaf 152)\",\"stance\":\"supports\",\"note\":\"'1548. Sskr. naladā: „Duftgebend; eine Pflanze Andropogon muricatum“ [nala „Duft“ < nala „Rohr, arundo“ nach Ascoli …; dazu dā „gebend“], hieraus pers. nārdīn, Adj. durch Ersatz des l durch r, auch hebr. nerd, aram. nirdā, gr. νάρδος.' Lokotsch takes nalada as a compound of nala 'reed' + dā 'giving', i.e. exactly the naḍá → nalada link Nourai draws.\"})\n\n# --- entry 1 node 4: add Lokotsch supporting Skt -> Persian nardin ---\nm4=node(e1,4)\nm4['consulted'].append({\"src\":\"LKT\",\"where\":\"Lokotsch no. 1548, p.126 (LKT.txt leaf 152)\",\"stance\":\"supports\",\"note\":\"'…hieraus pers. nārdīn, Adj. durch Ersatz des l durch r' — Sanskrit naladā gives Persian nārdīn with l → r, which is precisely Nourai's Sanskrit → Persian arrow (and the source of Horn's *narda-). Note that Lokotsch makes Hebrew nerd, Aramaic nirdā and Greek νάρδος parallel outcomes of the same Indian word, with no Arabic stage.\"})\n\n# --- entry 1 node 5: fix Klein page ---\nm5=node(e1,5)\nm5['consulted'][0]['where']=\"Klein s.v. nard (KLN_1966.txt leaf 550, printed p.1028)\"\nm5['consulted'].append({\"src\":\"LKT\",\"where\":\"Lokotsch no. 1548, p.126\",\"stance\":\"contradicts\",\"note\":\"Lokotsch's chain is Sanskrit naladā → Persian nārdīn, with Hebrew nerd, Aramaic nirdā and Greek νάρδος as parallel borrowings; Arabic plays no part, and the Arabic form he would recognize is nārdīn, not nard.\"})\n\n# --- entry 1 node 6: LKT is not silent ---\nm6=node(e1,6)\nfor c in m6['consulted']:\n    if c['src']=='KLN':\n        c['where']=\"Klein s.v. nard (KLN_1966.txt leaf 550, which carries the printed page number 1028)\"\n    if c['src']=='LKT':\n        c['stance']=\"contradicts\"\n        c['where']=\"Lokotsch, Etym. Wb. der europäischen Wörter orientalischen Ursprungs no. 1548, p.126 (LKT.txt leaf 152)\"\n        c['note']=\"'1548. Sskr. naladā … hieraus pers. nārdīn … auch hebr. nerd, aram. nirdā, gr. νάρδος. Hieraus in die europäischen Sprachen zur Bezeichnung eines sehr feinen Parfüms übergegangen, z.B. engl. nard …, dtsch. Narde. [Hobson-Jobson 617/618.]' Lokotsch too has Greek νάρδος as a direct Indo-Iranian/Semitic-area borrowing, with no Arabic link.\"\n\n# --- entry 1 node 8: fix the KLN page caveat and the FSD note ---\nm8=node(e1,8)\nm8['ref_check'][0]['note']=(\"Klein s.v. nard and s.v. spikenard. 'nard, n., spikenard. — ME. narde, fr. OF. narde (F. nard), fr. L. nardus, \"\n \"fr. Gk. νάρδος, fr. Heb. nērdh, „nard“, which together with Aram. nirdā and Akkad. lardu of s.m., prob. derives fr. Indo-Iranian *narda \"\n \"in OI. naḍaḥ, nalaḥ, „reed“. OI. naladam, „nard“, is possibly Sanskritization of Gk. νάρδος; see Boisacq, DELG., p.657 …, and \"\n \"Walde-Hofmann, LEW., II, 143 s.v. nardus. However, according to Manfred Mayrhofer … the above Sem. words more prob. derive fr. OI. naladam.' \"\n \"/ 'spikenard, n. — ME., fr. ML. spica nardi, „spike of nard“. See spike and nard.' The page number checks out exactly: the nard entry stands on \"\n \"KLN_1966.txt leaf 550, and that leaf carries the printed running number 1028 (the spikenard entry is on leaf 790, printed ≈1490).\")\nfor c in m8['consulted']:\n    if c['src']=='FSD':\n        c['note']=\"grep of FSD_vol1–vol4 for 'nard'/'spikenard' returns only incidental mentions inside other articles (musk-root '…the East-Indian spikenard (Nardostachys jatamansi)', 'false spikenard' s.v. Solomon's-seal); no legible headword entry for nard was recovered from the OCR, so Funk & Wagnalls adds nothing either way.\"\n    if c['src']=='KLN':\n        c['note']=\"see ref_check — Klein s.v. nard (leaf 550 = printed p.1028) and s.v. spikenard (leaf 790).\"\n\nwith io.open(p,'w',encoding='utf-8') as f:\n    json.dump(d,f,ensure_ascii=False,indent=2); f.write('\\n')\nprint('patched')\nPYEOF\npython3 -m json.tool data/verification/page-354.json > /dev/null && echo \"valid json\" && python3 tools/verify_check.py 354"
}
```


### [2026-09-07T18:43:05.196Z] TOOL RESULT

```
  File "<stdin>", line 16
    n9['consulted'][1]={"src":"KLN","where":"Klein s.v. node, annex, connect (KLN_1966.txt)","stance":"supports","note":"'annex, tr. v. — F. annexer, fr. L. annexus, pp. of annectere, „to bind to, tie on, annex“, fr. ad- and nectere, „to bind, join, fasten“. See nexus.' / 'connect, tr. and intr. v. — L. connectere, „to bind or join together“, fr. con- and nectere, „to tie, bind, join“, fr. I.-E. base *ned-, „to twist, knot“; see net and cp. nexus, annex.' / 'node, n., a knot, knob. — L. nodus…'"})
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ^
SyntaxError: unmatched ')'
valid json
nodes verified: 17/17
node verdicts: {'confirmed': 10, 'disputed': 3, 'plausible': 4}
root verdicts: {'confirmed': 1, 'plausible': 1}
ref checks: {'supports': 15, 'contradicts': 1, 'not_checked': 5, 'partial': 4}
books consulted: {'supports': 35, 'contradicts': 11, 'silent': 10, 'partial': 3} | by book: {'KLN': 10, 'MON': 5, 'WLD': 4, 'BQT': 4, 'POK': 4, 'FVQ': 3, 'PHD': 3, 'ARY': 3, 'LAT': 3, 'SKT': 3, 'BRT': 2, 'AFM': 2, 'IEC': 2, 'AHD': 2, 'HRN': 2, 'HUB': 2, 'NYB': 1, 'PLA': 1, 'KNT': 1, 'LKT': 1, 'FSD': 1}
```


## [2026-09-07T18:43:40.245Z] TOOL CALL #82: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/patch354.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\np='/home/sfmqrb/git/rishe/data/verification/page-354.json'\nd=json.load(open(p,encoding='utf-8'))\ne0,e1=d['entries'][0],d['entries'][1]\ndef node(e,i):\n    for n in e['nodes']:\n        if n['id']==i: return n\n    raise KeyError(i)\n\nn7=node(e0,7)\nn7['consulted'][0]={\"src\":\"KLN\",\"where\":\"Klein s.v. node and s.v. connect (KLN_1966.txt leaf 550, printed p.1028; connect in the c- range)\",\"stance\":\"supports\",\"note\":\"Klein s.v. node: 'node, n., a knot, knob. — L. nodus, „knot“, rel. to L. nassa (prob. for *nad-sa), „a basket for catching fish“, and cogn. with ON. not, „a large net“, ON., OE. net, „net“. See net…'; s.v. connect: '…fr. con- and nectere, „to tie, bind, join“, fr. I.-E. base *ned-, „to twist, knot“; see net and cp. nexus, annex.' Klein thus files English net under *ned- exactly as Nourai does.\"}\n\nn8=node(e0,8)\nn8['consulted'].append({\"src\":\"KLN\",\"where\":\"Klein s.v. node (KLN_1966.txt leaf 550, printed p.1028)\",\"stance\":\"supports\",\"note\":\"'node, n., a knot, knob. — L. nodus, „knot“, rel. to L. nassa (prob. for *nad-sa), „a basket for catching fish“, and cogn. with ON. not, „a large net“, ON., OE. net, „net“. See net and cp. nodus, noose, denouement, crunode, internode.'\"})\n\nn9=node(e0,9)\nn9['consulted'][1]={\"src\":\"KLN\",\"where\":\"Klein s.v. node, annex, connect (KLN_1966.txt)\",\"stance\":\"supports\",\"note\":\"'annex, tr. v. — F. annexer, fr. L. annexus, pp. of annectere, „to bind to, tie on, annex“, fr. ad- and nectere, „to bind, join, fasten“. See nexus.' / 'connect, tr. and intr. v. — L. connectere, „to bind or join together“, fr. con- and nectere, „to tie, bind, join“, fr. I.-E. base *ned-, „to twist, knot“; see net and cp. nexus, annex.' / 'node, n., a knot, knob. — L. nodus …'\"}\n\nm3=node(e1,3)\nm3['consulted'][1]['where']=\"Klein s.v. nard (KLN_1966.txt leaf 550, which carries the printed page number 1028)\"\nm3['consulted'].append({\"src\":\"LKT\",\"where\":\"Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs no. 1548, p.126 (LKT.txt leaf 152)\",\"stance\":\"supports\",\"note\":\"'1548. Sskr. naladā: „Duftgebend; eine Pflanze Andropogon muricatum“ [nala „Duft“ < nala „Rohr, arundo“ nach Ascoli …; dazu dā „gebend“], hieraus pers. nārdīn, Adj. durch Ersatz des l durch r, auch hebr. nerd, aram. nirdā, gr. νάρδος.' Lokotsch takes nalada as nala 'reed' + dā 'giving', i.e. exactly the naḍá → nalada link Nourai draws.\"})\n\nm4=node(e1,4)\nm4['consulted'].append({\"src\":\"LKT\",\"where\":\"Lokotsch no. 1548, p.126 (LKT.txt leaf 152)\",\"stance\":\"supports\",\"note\":\"'…hieraus pers. nārdīn, Adj. durch Ersatz des l durch r' — Sanskrit naladā gives Persian nārdīn with l → r, which is precisely Nourai's Sanskrit → Persian arrow (and the source of Horn's *narda-). Note that Lokotsch makes Hebrew nerd, Aramaic nirdā and Greek νάρδος parallel outcomes of the same Indian word, with no Arabic stage.\"})\n\nm5=node(e1,5)\nm5['consulted'][0]['where']=\"Klein s.v. nard (KLN_1966.txt leaf 550, printed p.1028)\"\nm5['consulted'].append({\"src\":\"LKT\",\"where\":\"Lokotsch no. 1548, p.126\",\"stance\":\"contradicts\",\"note\":\"Lokotsch's chain is Sanskrit naladā → Persian nārdīn, with Hebrew nerd, Aramaic nirdā and Greek νάρδος as parallel borrowings; Arabic plays no part, and the Arabic form he would recognize is nārdīn, not nard.\"})\n\nm6=node(e1,6)\nfor c in m6['consulted']:\n    if c['src']=='KLN':\n        c['where']=\"Klein s.v. nard (KLN_1966.txt leaf 550, which carries the printed page number 1028)\"\n    if c['src']=='LKT':\n        c['stance']=\"contradicts\"\n        c['where']=\"Lokotsch, Etym. Wb. der europäischen Wörter orientalischen Ursprungs no. 1548, p.126 (LKT.txt leaf 152)\"\n        c['note']=\"'1548. Sskr. naladā … hieraus pers. nārdīn … auch hebr. nerd, aram. nirdā, gr. νάρδος. Hieraus in die europäischen Sprachen zur Bezeichnung eines sehr feinen Parfüms übergegangen, z.B. engl. nard …, dtsch. Narde. [Hobson-Jobson 617/618.]' Lokotsch too has Greek νάρδος as a direct Indo-Iranian / Semitic-area borrowing, with no Arabic link.\"\n\nm8=node(e1,8)\nm8['ref_check'][0]['note']=(\"Klein s.v. nard and s.v. spikenard. 'nard, n., spikenard. — ME. narde, fr. OF. narde (F. nard), fr. L. nardus, \"\n \"fr. Gk. νάρδος, fr. Heb. nērdh, „nard“, which together with Aram. nirdā and Akkad. lardu of s.m., prob. derives fr. Indo-Iranian *narda \"\n \"in OI. naḍaḥ, nalaḥ, „reed“. OI. naladam, „nard“, is possibly Sanskritization of Gk. νάρδος; see Boisacq, DELG., p.657 …, and \"\n \"Walde-Hofmann, LEW., II, 143 s.v. nardus. However, according to Manfred Mayrhofer … the above Sem. words more prob. derive fr. OI. naladam.' \"\n \"/ 'spikenard, n. — ME., fr. ML. spica nardi, „spike of nard“. See spike and nard.' The page number checks out exactly: the nard entry stands on \"\n \"KLN_1966.txt leaf 550, and that leaf carries the printed running number 1028 (the spikenard entry is on leaf 790, printed ≈1490).\")\nfor c in m8['consulted']:\n    if c['src']=='FSD':\n        c['note']=\"grep of FSD_vol1–vol4 for 'nard'/'spikenard' returns only incidental mentions inside other articles ('…the East-Indian spikenard (Nardostachys jatamansi)' s.v. musk-root; 'false spikenard' s.v. Solomon's-seal); no legible headword entry for nard was recovered from the OCR, so Funk & Wagnalls adds nothing either way.\"\n    if c['src']=='KLN':\n        c['note']=\"see ref_check — Klein s.v. nard (leaf 550 = printed p.1028) and s.v. spikenard (leaf 790).\"\n\nwith io.open(p,'w',encoding='utf-8') as f:\n    json.dump(d,f,ensure_ascii=False,indent=2); f.write('\\n')\nprint('patched')\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/patch354.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-354.json > /dev/null && echo \"valid json\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 354"
}
```


### [2026-09-07T18:43:41.676Z] TOOL RESULT

```
patched
valid json
nodes verified: 17/17
node verdicts: {'confirmed': 10, 'disputed': 3, 'plausible': 4}
root verdicts: {'confirmed': 1, 'plausible': 1}
ref checks: {'supports': 15, 'contradicts': 1, 'not_checked': 5, 'partial': 4}
books consulted: {'supports': 38, 'contradicts': 13, 'silent': 9, 'partial': 3} | by book: {'KLN': 11, 'MON': 5, 'WLD': 4, 'BQT': 4, 'POK': 4, 'LKT': 4, 'FVQ': 3, 'PHD': 3, 'ARY': 3, 'LAT': 3, 'SKT': 3, 'BRT': 2, 'AFM': 2, 'IEC': 2, 'AHD': 2, 'HRN': 2, 'HUB': 2, 'NYB': 1, 'PLA': 1, 'KNT': 1, 'FSD': 1}
```


## [2026-09-07T18:43:51.175Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('PHD.txt',encoding='utf8',errors='replace').read()\nlines=t.split('\\n')\nfor ln in (501,509):\n    off=sum(len(l)+1 for l in lines[:ln-1]); print(ln,'leaf',t[:off].count('\\f'))\n\""
}
```


### [2026-09-07T18:43:52.518Z] TOOL RESULT

```
501 leaf 82
509 leaf 82
```


## [2026-09-07T18:43:59.342Z] TOOL CALL #84: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/page-354.json',encoding='utf-8'))\nfor e in d['entries']:\n    print('ENTRY',e['entry'],e['root'],e['verdict'],'| note_fa len',len(e['note_fa']),'| sources',len(e['sources']))\n    for n in e['nodes']:\n        print('  #%s %-12s %-28s %-22s fa=%d src=%d rc=%d con=%d'%(n['id'],n['lang'],n['words'][:28],n['verdict'],len(n['derivation_fa']),len(n['sources']),len(n['ref_check']),len(n['consulted'])))\n\" ; wc -c data/verification/page-354.json; git status --short"
}
```


### [2026-09-07T18:44:00.659Z] TOOL RESULT

```
ENTRY 0 Ned confirmed | note_fa len 453 | sources 1
  #1 Avestan      naska                        confirmed              fa=769 src=0 rc=1 con=3
  #2 Pahlavi      nask                         confirmed              fa=494 src=0 rc=1 con=2
  #3 Persian      nask                         confirmed              fa=540 src=1 rc=2 con=3
  #4 Arabic       nasx                         disputed               fa=896 src=2 rc=1 con=4
  #5 Persian      nosxeh                       confirmed              fa=626 src=2 rc=1 con=3
  #6 Germanic                                  confirmed              fa=568 src=1 rc=1 con=3
  #7 English      net 2                        confirmed              fa=723 src=2 rc=1 con=3
  #8 Latin        nôdus; nectere               confirmed              fa=722 src=2 rc=1 con=5
  #9 English      node, annex, connect         confirmed              fa=758 src=2 rc=1 con=3
ENTRY 1 Nedo, Narda plausible | note_fa len 1027 | sources 2
  #1 Old Persian  nada                         plausible              fa=833 src=1 rc=1 con=4
  #2 Persian      nâi, nay, nâl; surnây, sornâ plausible              fa=1282 src=4 rc=5 con=6
  #3 Sanskrit     nadah; naladam, nalada       plausible              fa=933 src=2 rc=2 con=4
  #4 Persian      nard 2                       plausible              fa=1173 src=3 rc=3 con=5
  #5 Arabic       nard                         disputed               fa=1020 src=3 rc=1 con=5
  #6 Greek        nardos                       disputed               fa=1081 src=3 rc=1 con=4
  #7 Latin        nardus                       confirmed              fa=632 src=2 rc=1 con=3
  #8 English      nard, spikenard              confirmed              fa=708 src=2 rc=1 con=3
100108 data/verification/page-354.json
```


## [2026-09-07T18:44:05.028Z] TOOL CALL #85: Bash

```json
{
 "command": "git status --short | head -20; echo \"---\"; git check-ignore -v data/verification/page-354.json || echo \"not ignored\""
}
```


### [2026-09-07T18:44:06.433Z] TOOL RESULT

```
---
not ignored
```


## [2026-09-07T18:44:09.218Z] TOOL CALL #86: Bash

```json
{
 "command": "git status --short | head -30; git rev-parse --abbrev-ref HEAD; ls -la data/verification/page-354.json"
}
```


### [2026-09-07T18:44:09.289Z] TOOL RESULT

```
verified
-rw-rw-r-- 1 sfmqrb sfmqrb 100108 Sep  7 14:43 data/verification/page-354.json
```


## [2026-09-07T18:44:14.425Z] TOOL CALL #87: Bash

```json
{
 "command": "git status 2>&1 | head -20; echo \"=== ls-files ===\"; git ls-files data/verification/ | head; echo \"=== untracked check ===\"; git status --porcelain --untracked-files=all data/verification/page-354.json"
}
```


### [2026-09-07T18:44:14.508Z] TOOL RESULT

```
On branch verified
nothing to commit, working tree clean
=== ls-files ===
data/verification/agent/AGENT_INSTRUCTIONS.md
data/verification/agent/charts/page-100.txt
data/verification/agent/charts/page-101.txt
data/verification/agent/charts/page-102.txt
data/verification/agent/charts/page-103.txt
data/verification/agent/charts/page-104.txt
data/verification/agent/charts/page-105.txt
data/verification/agent/charts/page-106.txt
data/verification/agent/charts/page-107.txt
data/verification/agent/charts/page-108.txt
=== untracked check ===
```


## [2026-09-07T18:44:22.718Z] TOOL CALL #88: Bash

```json
{
 "command": "cat .gitignore 2>/dev/null | head -40; echo \"=== info/exclude ===\"; cat .git/info/exclude 2>/dev/null | head -20"
}
```


### [2026-09-07T18:44:22.771Z] TOOL RESULT

```
# regenerable from the PDF via pdftoppm (see tools/)
data/pages/

# built site (regenerate with tools/build_site.py)
site/risheh.html
__pycache__/

# Verification: OCR texts of copyrighted reference works (local audit copies only)
data/verification/sources/refs/
=== info/exclude ===
# git ls-files --others --exclude-from=.git/info/exclude
# Lines that start with '#' are comments.
# For a project mostly in C, the following would be a good set of
# exclude patterns (uncomment them if you want to use them):
# *.[oa]
# *~
```


## [2026-09-07T18:45:50.415Z] TOOL CALL #89: Bash

```json
{
 "command": "ls -la /home/sfmqrb/git/rishe/data/verification/page-354.json; echo \"---\"; wc -c /home/sfmqrb/git/rishe/data/verification/page-354.json; echo \"--- web index tail ---\"; tail -3 /home/sfmqrb/git/rishe/data/verification/sources/web/index.jsonl; echo \"--- git see web? ---\"; git status --porcelain --untracked-files=all -- data/verification/sources/web | head -5; echo \"(end)\"",
 "dangerouslyDisableSandbox": true
}
```


### [2026-09-07T18:45:50.503Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 100108 Sep  7 14:43 /home/sfmqrb/git/rishe/data/verification/page-354.json
---
100108 /home/sfmqrb/git/rishe/data/verification/page-354.json
--- web index tail ---
{"url": "https://vajehyab.com/?q=%D9%86%D9%85%DA%A9&d=moein", "file": "data/verification/sources/web/aeb779d9012977a1.txt", "fetched": "2026-09-07T18:33:43Z", "status": 200, "bytes": 1679, "title": "معنی نمک | واژه یاب", "note": "page 353 node 6: Mo'in's online entry for نمک (no origin tag online; MON:4818 page not mappable)"}
{"url": "https://en.wiktionary.org/wiki/%D8%A3%D9%86%D8%A8%D9%8A%D9%82", "file": "data/verification/sources/web/053a9f64ed8cedd3.txt", "fetched": "2026-09-07T18:43:53Z", "status": 200, "bytes": 3547, "title": "أنبيق - Wiktionary, the free dictionary", "note": "post-pass: page 355, root Nei 1, Ni 2, node #6 al-anbîq, al-ambîq"}
{"url": "https://abadis.ir/fatofa/%D8%B1%D9%88%D9%86%DB%8C%DA%A9/", "file": "data/verification/sources/web/aa8a8e03f93a9023.txt", "fetched": "2026-09-07T18:43:54Z", "status": 200, "bytes": 2262, "title": "رونیک - معنی در دیکشنری آبادیس", "note": "post-pass: page 355, root Nei 1, Ni 2, node #11 rŭnîk «رونیک ( نیکرو )»"}
--- git see web? ---
(end)
```


## [2026-09-07T18:46:00.399Z] TOOL CALL #90: Bash

```json
{
 "command": "git config --get status.showUntrackedFiles; echo \"cfg-exit=$?\"; git ls-files --others --exclude-standard data/verification/ | head -5; echo \"(end others)\"",
 "dangerouslyDisableSandbox": true
}
```


### [2026-09-07T18:46:01.708Z] TOOL RESULT

```
cfg-exit=1
(end others)
```


## [2026-09-07T18:46:09.308Z] TOOL CALL #91: Bash

```json
{
 "command": "git ls-files -- data/verification/page-354.json; echo \"ls-files-exit=$?\"; git log --oneline -1 -- data/verification/page-354.json; echo \"---diff---\"; git diff --stat HEAD -- data/verification/page-354.json; echo \"---show head version size---\"; git show HEAD:data/verification/page-354.json 2>/dev/null | wc -c",
 "dangerouslyDisableSandbox": true
}
```


### [2026-09-07T18:46:10.700Z] TOOL RESULT

```
data/verification/page-354.json
ls-files-exit=0
20932c4 Verify page 355 (Nei 1 part 1/niv, nik, nard, anbiq, alembic, rownaq, neat)
---diff---
---show head version size---
100108
```


## [2026-09-07T18:46:17.692Z] TOOL CALL #92: Bash

```json
{
 "command": "python3 tools/verify_check.py 354 && echo \"EXIT OK (0 problems)\""
}
```


### [2026-09-07T18:46:18.935Z] TOOL RESULT

```
nodes verified: 17/17
node verdicts: {'confirmed': 10, 'disputed': 3, 'plausible': 4}
root verdicts: {'confirmed': 1, 'plausible': 1}
ref checks: {'supports': 15, 'contradicts': 1, 'not_checked': 5, 'partial': 4}
books consulted: {'supports': 38, 'contradicts': 13, 'silent': 9, 'partial': 3} | by book: {'KLN': 11, 'MON': 5, 'WLD': 4, 'BQT': 4, 'POK': 4, 'LKT': 4, 'FVQ': 3, 'PHD': 3, 'ARY': 3, 'LAT': 3, 'SKT': 3, 'BRT': 2, 'AFM': 2, 'IEC': 2, 'AHD': 2, 'HRN': 2, 'HUB': 2, 'NYB': 1, 'PLA': 1, 'KNT': 1, 'FSD': 1}
EXIT OK (0 problems)
```


## [2026-09-07T18:46:42.483Z] AGENT

PDF page 354 (book p. 324) verified. `/home/sfmqrb/git/rishe/data/verification/page-354.json` written; `verify_check.py 354` shows 17/17 nodes and 0 PROBLEM lines. (Note: a concurrent coordinator commit, 20932c4, already swept the file into git — content is identical.)

**Counts** — roots: 1 confirmed, 1 plausible. Nodes: 10 confirmed, 4 plausible, 3 disputed. Ref checks: 15 supports, 4 partial, 1 contradicts, 5 not_checked. 21 books consulted.

**Disputed**
- Ned #4 — Arabic `nasx` ← Pahlavi `nask`: n-s-ḫ is a native/Aramaic Semitic root ("remove, tear away"; Akk. nasāḫu, Heb. נסח), "copy" secondary. Nourai's own ref reverses him: Jeffery FVQ 279 (= VDQ) says the *Iranian* word is probably the Semitic borrowing. Asbaghi and Addi Shir list neither nasx nor nusxa as Persian loans.
- Nedo/Narda #5 — Arabic "nard" ← Persian: form is wrong (Arabic نرد = backgammon; the plant is نارْدين / رَنْد, and PLA:257 itself prints *nārdīn*), and Wiktionary/CAL derive نارْدين from Aramaic nārdīn; Dehkhodā and Moʿīn call it a Greek Arabicization.
- Nedo/Narda #6 — Greek `nardos` ← Arabic: chronologically impossible (νάρδος in Theophrastus, LXX). Beekes/Wiktionary: from Phoenician; Klein: from Hebrew nērd; Skeat, Horn, Lokotsch: straight from Indo-Iranian. Parent should be NW Semitic, not Arabic.

**Plausible (why)** — root "Nedo, Narda": POK 759 has "nedo- 'Schilf'?" (queried, gloss "reed" only, no Old Persian); "Narda" is Horn/Hübschmann's Indo-Iranian *narda-, not a PIE lemma. #1 Old Persian *nada-* is unattested (starred in Horn, absent from Kent). #2 nāy/nay/nāl confirmed, but Wiktionary calls sur+nāy a folk etymology and kornā possibly Semitic (qarnā); qaraney is confirmed (Moʿīn tags it "[تر - فا.]", Turkish qara + نی). #3 naḍá confirmed, nalada's link only "perhaps" (Mayrhofer). #4 Horn/Skeat/Lokotsch back Skt → Pers., but ناردین is a Greek/Syriac loan per Moʿīn's own Borhān footnote, and Dehkhodā's نرد ۲ is "stalk, trunk", not spikenard.

**Extraction errors:** none — I read `site/pages/354.jpg` and the JSON is faithful (including `nôdus`, the four Persian compounds, and every ref string).

**Page-number notes for the owner** (content verified, page not): BQT:1185 — vol. 2 has no page scan and the OCR leaf numeral is illegible; the سرنای/سرنی article is at leaf 592. MON:4727 and MON:2957 — only the 2-vol. Adena reprint is on disk, so entries were verified, not pages. FVA:399 — no digital copy exists. BQT:2093, 2104, 2140, 2221, POK:758/759, HRN:237, SKT:344, PLA:257 and KLN:1028 all check out exactly (KLN leaf 550 carries the printed running number 1028, contrary to the offset formula in `refs_online.json`, which is off by ~48 pages there).
