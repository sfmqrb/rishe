# Verification process log — verify-page-155


## [2026-09-05T20:27:35.530Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 155 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-155.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-155.json. Write /home/sfmqrb/git/rishe/data/verification/page-155.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 155` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T20:27:37.328Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T20:27:38.189Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T20:27:38.202Z] TOOL RESULT

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


## [2026-09-05T20:27:38.356Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-155.txt"
}
```


### [2026-09-05T20:27:38.370Z] TOOL RESULT

```
1	=== PDF page 155 (book page 125) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Ens : meet with hostile intent  (refs WLD1:134)
4	#1 (parent #0) [Avestan] refs=WLD1:134; BRT:361 | ans-tha, asta 1 : enmity ; astai : to hate ; ans-ra, as-ra, anra, angra : devilish
5	  #2 (parent #1) [Avestan] refs=POK:726; KGW:46; SIN:1179; ETM:35 | anra-mainyu, angra-manyu, ahra-manyu : evil spirit ☞Men 1
6	    #3 (parent #2) [Persian] refs=BQT:2083; FSF:36 | ahrîman «اهریمن» : devil | extra: آهرمن
7	#4 (parent #0) [Old Persian] refs=WLD1:134 | arika, ahrika : adversely disposed
8	--- entry 1 ---
9	ROOT [Indo-European] Epi, Opi : at, near, against  (refs POK:323; KLN:1065)
10	#1 (parent #0) [Avestan / Old Persian] refs=KLN:530; POK:57 | aipi : to, toward, also ; aipi-areta : set, determined ☞Ar ; apiy, ape, apaya
11	#2 (parent #0) [Latin] refs=AHD | ob : to against, before
12	  #3 (parent #2) [English] refs=None | obtain, offer, oppose, omit
13	#4 (parent #0) [Greek] refs=AHD | epi : on, over, among ; epi-skopos : one rank above bishop ☞Spek
14	  #5 (parent #4) [Old Persian] refs=MON:1901; FSF:228 | skuba : bishop, priest
15	    #6 (parent #5) [Persian] refs=MON:1901; FSF:228 | sekubâ «سکوبا» : a Christian bishop
16	  #7 (parent #4) [Arabic] refs=MON:270; TAD:3 | osqof : bishop
17	    #8 (parent #7) [Persian] refs=MON:270; FSF:44 | osqof «اسقُف» : bishop
18	  #9 (parent #4) [Latin] refs=AHD | episcopus, biscopus : priest ; epi-děmia : (illness) among people ☞Dâ ; epi-lěpsia : hold upon
19	    #10 (parent #9) [English] refs=AHD | Episcopal, bishop, epidemic, epilepsy
20	
```


## [2026-09-05T20:27:41.185Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-155.json",
 "description": "Read source JSON for page 155"
}
```


### [2026-09-05T20:27:41.224Z] TOOL RESULT

```
{
  "pdf_page": 155,
  "book_page": 125,
  "entries": [
    {
      "root": {
        "name": "Ens",
        "lang": "Indo-European",
        "refs": "WLD1:134",
        "gloss": "meet with hostile intent",
        "note": "WLD expresses uncertainty about derivation of these words"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "WLD1:134; BRT:361",
          "words": [
            {"translit": "ans-tha, asta 1", "gloss": "enmity", "script": null},
            {"translit": "astai", "gloss": "to hate", "script": null},
            {"translit": "ans-ra, as-ra, anra, angra", "gloss": "devilish", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Avestan",
          "refs": "POK:726; KGW:46; SIN:1179; ETM:35",
          "words": [
            {"translit": "anra-mainyu, angra-manyu, ahra-manyu", "gloss": "evil spirit", "script": null, "see": ["Men 1"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:2083; FSF:36",
          "words": [
            {"translit": "ahrîman", "gloss": "devil", "script": "اهریمن"}
          ],
          "script_extra": "آهرمن",
          "note": null,
          "quote": {"text": "ز فریادرس زور و فریاد خواست - از آهرمن بد کنش داد خواست", "poet": "Ferdowsî"}
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "WLD1:134",
          "words": [
            {"translit": "arika, ahrika", "gloss": "adversely disposed", "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Epi, Opi",
        "lang": "Indo-European",
        "refs": "POK:323; KLN:1065",
        "gloss": "at, near, against"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "KLN:530; POK:57",
          "words": [
            {"translit": "aipi", "gloss": "to, toward, also", "script": null},
            {"translit": "aipi-areta", "gloss": "set, determined", "script": null, "see": ["Ar"]},
            {"translit": "apiy, ape, apaya", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "ob", "gloss": "to against, before", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "obtain, offer, oppose, omit", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "epi", "gloss": "on, over, among", "script": null},
            {"translit": "epi-skopos", "gloss": "one rank above bishop", "script": null, "see": ["Spek"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Old Persian",
          "refs": "MON:1901; FSF:228",
          "words": [
            {"translit": "skuba", "gloss": "bishop, priest", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Persian",
          "refs": "MON:1901; FSF:228",
          "words": [
            {"translit": "sekubâ", "gloss": "a Christian bishop", "script": "سکوبا"}
          ],
          "note": null,
          "quote": {"text": "نوشتند نامه به هر کشوری - سکوبا و بطریق و هر مهتری", "poet": "Ferdowsî"}
        },
        {
          "id": 7,
          "parent": 4,
          "lang": "Arabic",
          "refs": "MON:270; TAD:3",
          "words": [
            {"translit": "osqof", "gloss": "bishop", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Persian",
          "refs": "MON:270; FSF:44",
          "words": [
            {"translit": "osqof", "gloss": "bishop", "script": "اسقُف"}
          ],
          "note": null,
          "quote": {"text": "سقف گفت کاین نیست کاری گران - که پیش از تو بودند چندی سران", "poet": "Ferdowsî"}
        },
        {
          "id": 9,
          "parent": 4,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "episcopus, biscopus", "gloss": "priest", "script": null},
            {"translit": "epi-děmia", "gloss": "(illness) among people", "script": null, "see": ["Dâ"]},
            {"translit": "epi-lěpsia", "gloss": "hold upon", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "Episcopal, bishop, epidemic, epilepsy", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-05T20:27:41.935Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T20:27:41.981Z] TOOL RESULT

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


## [2026-09-05T20:28:06.129Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['WLD','BRT','POK','KGW','SIN','ETM','BQT','FSF','KLN','AHD','MON','TAD','KNT','PHD','HRN','HUB','NYB','IEC','SYN','SKT','LEW','LAT','FVQ','AFM','PLA','ARB','LKT','ARY']:\n    v=d.get(k)\n    print('###',k, json.dumps(v,ensure_ascii=False)[:700] if v else 'MISSING')\n\""
}
```


## [2026-09-05T20:28:06.864Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo ---- && sed -n 1,60p data/verification/page-124.json"
}
```


### [2026-09-05T20:28:08.031Z] TOOL RESULT

```
### WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015
### BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between 
### POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index 
### KGW {"title": "J. Ibrahim, Kulturgeschichtliche Wortforschung: Persisches Lehngut in europäischen Sprachen, Wiesbaden 1991", "edition_found": null, "kind": "google_books_preview", "url": "https://books.google.com/books?id=OUtZZNSUi3cC (partial preview) ; HathiTrust uc1.b3624504 search-only", "identifier": null, "local_file": null, "page_offset": null, "lookup_hint": "Google Books limited preview only (index pages).", "notes": "RE-SEARCH 2026-09: preview only (Google Books partial view usable for spot checks); no PDF on the author's site jamshid-ibrahim.net; purchase from Harrassowitz."}
### SIN {"title": "B. Laufer, Sino-Iranica, Chicago 1919 (Field Museum Anthr. Ser. XV.3, pp. 185-630)", "edition_found": "1919", "kind": "archive_djvu", "url": "https://archive.org/details/sinoiranicachine153lauf", "identifier": "sinoiranicachine153lauf (also sinoiranicachin00laufgoog, jstor-29782155)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SIN.txt", "page_offset": "leaf = printed - 172 (e.g. leaf 15 = p.187). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Running page numbers 185-630 (the volume's series pagination, which Nourai uses). Sectio
### ETM {"title": "Mohsen Abolghasemi, Risheh-shenasi (Etimoloji), Qoqnus 1374/1995", "kind": "catalog", "url": "https://ketabnak.com/book/107170/ (no download) ; https://ketab.ir/book/2ebb5f53-ba49-4955-98f4-d419919d0ebc ; purchase: https://adinehbook.com/gp/product/9643110451", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: no digital copy on any permitted platform; catalogue/purchase only."}
### BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.c
### FSF {"title": "Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/1984", "kind": "archive_djvu", "url": "https://archive.org/details/20220809_20220809_1444", "lookup_hint": "grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushin book (گزارشی چند درباره شاهنامه).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF.txt"], "page_offset": "484 leaves; edition/printing of this scan not identified — determine offset from printed page 
### KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO pri
### AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifie
### MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol 
### TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640", "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; inside.php search works.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD_pag
### KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archiv
### PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<ident
### HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the 
### HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by parag
### NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's 'NYB' nu
### IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstruct
### SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i
### SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i
### LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.o
### LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for most of the book (e.g. leaf 21 = p.3); drifts in places (leaf 219 = p.301 -> -82?? probably a mis-detec
### FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt"], "page_offset": "printed page = leaf − 17 (0-based \\f blocks in FVQ_pages.txt; 
### AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt"], "page_offset": "19
### PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 leaves (pdftotext -layout, \\f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276).", "loo
### ARB {"title": "al-Jawaliqi, al-Mu'arrab min al-kalam al-a'jami, Tehran 1966 (reprint of Ahmad M. Shakir's Cairo 1361/1942 edition)", "kind": "archive_djvu", "url": "https://archive.org/details/mo3rb (probably the Shakir edition) ; https://archive.org/details/almo3rab_gwaliqy_f_abduraheem (F. 'Abd al-Rahim ed., Damascus 1990) ; also uc1.aa0003615705 / AAlexandrina-148752 (Sachau's Leipzig 1867 ed.) ; text on shamela.ws", "lookup_hint": "Alphabetical Arabic headwords; grep in ARB_mo3rb.txt / ARB_abdulraheem.txt (raw, no page breaks); edition of mo3rb not confirmed — check its title page image.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/ARB_mo3rb.txt", "/home/sfmqrb/git
### LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages.
### ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", "local_file": ["/home/sfmqrb/git/rishe/
```


### [2026-09-05T20:28:08.077Z] TOOL RESULT

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
page-129.json
page-130.json
page-131.json
page-133.json
page-135.json
page-137.json
page-138.json
page-144.json
page-146.json
page-311.json
page-31.json
page-32.json
page-33.json
page-345.json
page-34.json
page-35.json
page-36.json
page-37.json
page-38.json
page-39.json
page-40.json
page-41.json
----
{
  "pdf_page": 124,
  "book_page": 94,
  "verified_by": "claude-opus-5",
  "verified_on": "2026-09-05",
  "entries": [
    {
      "entry": 0,
      "root": "Dhě 2",
      "verdict": "confirmed",
      "modern_form": "PIE *dʰeh₁- 'to put, place; to do' (Pokorny 235-239 dʰē-2; Watkins/AHD dhē-¹)",
      "note": "The root box is right on all three counts. Pokorny's own lemma reads 'Root / lemma: dʰe-2, Meaning: to put, place, say' with 'Page(s): 235-239', so Nourai's 'Dhě 2 : to do, set' with POK:235 reproduces Pokorny's numbering and gloss exactly; Watkins in the AHD appendix has 'dhē-¹. To set, put. Contracted from *dheə ... [Pok. 2. dhē- 235]', and Wiktionary's reconstruction page glosses *dʰeh₁- 'to do; to put, place'. The Iranian material of the chart is likewise Pokorny's own: 'with full grade Avestan Old pers. dāta-', 'Avestan ni-δaiti- „laying down, putting away, hiding“', 'Avestan gao-δi- / gao-δana- „milk container“', 'Avestan dāman-, dąman- n. „site, creature“'. Three things in Part 1 need correcting rather than the root itself. (1) The Avestan mouth-veil is paiti.dāna-, not 'paiti-dâma' (node #3) — a misprint in the printed book, and one that Mo'in's footnote on the very page Nourai cites (Borhān p.418) refutes. (2) apa-dāna- (node #6) is Old Persian, not Avestan, and means 'palace, columned hall'; 'the concealed part of a palace' is Kent's etymological comparison with Skt. apadhā-, not the word's attested sense. (3) Pahlavi dast-war (node #13) does not belong to this root at all: Horn p.127, the page Nourai cites, and Nyberg II 61 both derive it from the root daṇs-/dąh- 'to teach', and Wiktionary offers only *dasta-bara- 'hand-bearer' or *danh- 'to teach'. A fourth, smaller point: the gloss 'to settle, to give' on node #11 mixes this root with PIE *deh₃- 'to give', a distinction Nourai's own reference FFD:52 (Abolghasemi p.52) draws explicitly. Two of the four boxes on the Persian side, the Sogdian box and both of the Persian outcomes of the law-branch check out completely, and Gharib's Sogdian entry γwδʾak even carries the Avestan etymology Nourai draws.",
      "note_fa": "خودِ ریشه کاملاً درست است: پوکورنی در صفحات ۲۳۵–۲۳۹ مادهٔ dʰē-2 را با معنای «نهادن، قرار دادن» آورده و واتکینز در پیوست فرهنگ American Heritage همین را می‌گوید؛ مواد ایرانی نمودار (dāta-، ni-δaiti-، gao-δana-، dāman-) هم عیناً از همین مادهٔ پوکورنی است. سه لغزش در بخش یکم هست: ۱) صورت اوستایی «پنام» paiti.dāna- است نه paiti-dāma — خطای چاپی کتاب؛ ۲) apadāna پارسی باستان است نه اوستایی و معنایش «کاخ، تالار بار» است؛ ۳) پهلوی dastwar هیچ ربطی به این ریشه ندارد و هرن (ص ۱۲۷) و نیبرگ (ج۲ ص ۶۱) آن را از ریشهٔ daṇs-/dąh- «آموختن» می‌گیرند. نکتهٔ کوچک‌تر آنکه معنای «دادن» در خانهٔ ۱۱ متعلق به ریشهٔ دیگر *deh₃- است و ابوالقاسمی در همان FFD:52 این دو را جدا کرده است. در مجموع، ادعای نورایی دربارهٔ خودِ ریشه درست است.",
      "sources": [
        "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/d%CA%B0eh%E2%82%81-"
      ],
      "ref_check": [
        {
          "ref": "AHD:1512",
          "status": "supports",
          "note": "Watkins's Indo-European appendix (local file AHD_watkins1985.txt line 375): 'dhē-¹. To set, put. Contracted from *dheə ... [Pok. 2. dhē- 235.]' — the same list Nourai cites by its 1975 New College page 1512 (roots are alphabetical over pp.1505-1550, so 'dhē-' falls in the right place); the copy on disk is the 1985 standalone reprint with different pagination."
        },
        {
          "ref": "POK:235",
          "status": "supports",
          "note": "POK_full.txt lines 22276-22510: 'Root / lemma: dʰe-2 / Meaning: to put, place, say' ... 'References: WP. I 826 ff ... Page(s): 235-239'."
        }
      ],
      "consulted": [
        {
          "src": "POK",
          "where": "pp.235-239, dʰē-2",
          "stance": "supports",
          "note": "supplies not only the root but every Iranian form of the chart: 'Avestan Old pers. data-', 'Avestan ni-δaiti- f. „laying down, putting away, hiding“', 'Avestan gao-δi- „milk container“', 'Avestan gao-δana- n. „milk container“', 'Avestan daman-, dąman- n. „site, creature“'."
        },
        {
          "src": "WLD",
          "where": "Bd. I pp.826-830 (p.828)",
          "stance": "supports",
          "note": "the parent article of Pokorny's; p.828 carries 'av. ni-δaiti- f. „das Niederlegen, Ablegen, Verbergen“', 'Ai. dhāna-m „Behälter“ ... av. gao-dana- n. „Milchgefäß“', 'av. dāman-, dąman- n. „Stätte, Wohnstätte; Geschöpf“'."
        },
        {
          "src": "AHD",
          "where": "Watkins 1985, s.v. dhē-¹",
          "stance": "supports",
          "note": "'To set, put. Contracted from *dheə.' Same gloss as Nourai's 'to do, set'."
        },
        {
          "src": "Wiktionary",
          "where": "Reconstruction:Proto-Indo-European/dʰeh₁-",
          "stance": "supports",
          "note": "'*dʰeh₁- (perfective): to do; to put, place.'"
        }
      ],
      "nodes": [
        {
          "id": 1,
          "lang": "Avestan",
          "words": "ma[n]dz-dha; ahura-mazdha",
          "verdict": "confirmed",
```


## [2026-09-05T20:28:13.370Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; ls; python3 - <<'EOF'\np='/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt'\nimport re\nt=open(p,encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(len(pages))\nfor i,pg in enumerate(pages[:6]):\n    print('--- leaf',i,pg[:200].replace('\\n',' | '))\nEOF"
}
```


## [2026-09-05T20:28:13.678Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"aŋra\\|angra\\|aŋhra\" BRT.txt | head -40"
}
```


### [2026-09-05T20:28:16.057Z] TOOL RESULT

```
WLD_Bd1_1930_dli_70244_djvu.txt
WLD_Bd1_1930_dli_70244_text.pdf
WLD_Bd1_pages.txt
WLD_Bd2_1927_dli_106624_djvu.txt
WLD_Bd2_1927_dli_106624_text.pdf
WLD_Bd2_pages.txt
895
--- leaf 0             GOVERNMENT OF INDIA |  ARCHEOLOGICAL SURVEY OF INDIA |  |                CENTRAL |             ARCHEOLOGICAL |                 LIBRARY | ACCESSION NO. jj03?7 | CALL No. gJ3 Wafjpok |                  f_ | D
--- leaf 1 
--- leaf 2 
--- leaf 3                       ALOIS WALDE |  |  | VERGLEICHENDES WftRTERBDCH |                                 DER |  |  |      INDOGERM ANISCHEN SPRACHEN |  |                 HERAUSGEGEBEN UND BEARBEITET |                      
--- leaf 4 CENTRAL A,.            ,   JRIGAL |    LIBRARY, NlvV .,w.rU. | Am. N# .^.557- | D**.,      . |                4-.   SS' | cwi                         /V* »#tf MM* | 
--- leaf 5                                                            •                      n |  |  |  |  |                                        Vorrede. |   Das   vorliegende       Werk laSt        uns erst so reckt emp
```


### [2026-09-05T20:28:16.104Z] TOOL RESULT

```
4112:•  j.  aDra-'>,  g.  angra-  Adj.  'feindlich; Feind';  katär^m  ä  'rS  vä  hi-S  va°rS  y3.. cyaithat  hvS  ndit  ayjm  'rB  mainyet!  "bei welchem  von  beiden  ist  der  Feind?  Oder ist  der  der  Feind,  der  .  .  Wie  ists?  Soll dernicht  für  einen  Feind  gehalten  werden?" Y.  44- 12;  —  al  tsi  vJsp^ng  -ring  *asaonS adarS  "denn  alle  ..^iaanhänger  machen die  (ja)  zu  Feinden"  Y.  43- 1 5-  a)  mit mainyOT-  m.  'der  arge,  böse  Geist'  ^Ahri- man')  im  Gegensatz  zu  spanyah-,  sp^ttia—. mainyü  .  .  yayä  spanyä  (sd.)  üitl  mraval ySm  'r»m  Y.  45-  2',  —  tä  i/raiasays) '■  taaa  wvMfJ  hist>nia  yat  *mainyu  däman
4553:angraya
4561:•  g.  angra-  Adj.:  s.  unter  ai^a-.
4562:•  g.  angrayä  Adv.  'feindseliger,  böslicher Weise,  arglistig';  yä  a°  karapatiB  umpa- yeintii^A.)  Y.^Ä'.io.
4563:Zu  angra;  %  253.  3.   —    Pü.:   kl  lüräk  (etl.: latir)  h'iid.
4620:131  angraya
4626:•  g.  angra-  Adj.:  s.  unter  aura-,
4627:•  g.  angraya  Adv.  'feindseliger,  böslicher Weise,  arglistig':  ya  a'  karapanB  urüpa- yanti  (sd.)  Y.4Ä10.
4628:Zu  angra-,  %  aj^.  3.   —   Pü.:   kt  züräk  (erl.r laiär)  hhtd. j.  anusvi  aiita  N.  707:  lies  anusavan/a.
10609:mönnäat  (sd.)  .  .  jyStSul  .  .  'tum  ('Plan')  |  itJ.107 Y-J2.9;  — ya  angrayä  karapanS  urspa- ydntJ  (sd.)  yäcä  'tä  (IS.,  'Absicht')  dus»- xid^ra  .  .  'S:.  48.  10;  —  vT6vä  avoi kava  Orca  ('Absicht')  paraiti  V.  75. 2.  a)  'Geisteskraft,  Einsicht,  Verstand  ; Gedächtnis  kraft,  Weisheit':  mana  'üwa^a ästica  (sd.)  Yt/.  26;  —  tat  müi  'tSui ('Verstand')  manankascä  vTä%?m  (sd.)  Y. .,^6'.  18;  —  hyat  .  .  ma-dj  .  .  gal^ascä tasü  damäsca  (sd.)  . .  -tus'cä  (AP. ;  'Geistes- kräfte').. Y.j/.i  i;  —  data  't^us  ('Geistes- kraft')  ..rdzA^f  vaha  sähtt  (sd.)  mananha Y,  50. 6 ;  —  hvd  -'iwa  ('Geisteskraft')  damis (sd.)  ahm  Y.  _?/.;;  —  vJdva  yai^l  güzrä (sd.)  singha»hg..vai3hsul  °'>:ina  ('Geistes- kraft') mananhö  Y.48.3;  —  aiJ  h^m firasvä  (sd.)  Jiw,?  '>wit  ('Verstand')  Y. 53-y<  —  *vfm4   aiat  hava   -^wa  Y.21
11162:•  j.  faO'wars.zangra-  Adj.  'mit  vier Fussknöcheln,  vieriiissig',  von  i/a^schea Wesen";  vikrks  'rS  V.iS.ii;  —  vfhr- kanqmca  "ranqm  Y.p.  18.
17300:•  j.  bt-zangra-,  "z^ngra-  Adj.  'mit  zwei Fussknöcheln,  zweiTdssiz',  von  ^n^schen Wesen'*:  maityS  drvä  'zangrd  ava%a abmaeyö  'V.5. 35;  —  maiyäca  'angra (NP.)  Yt.5.  89; —  mairyanamca  "zangra- nqm  astmaoyanamla  'zangranam  vihrka- nqmca  ca%war3.zangranqm  Y.ff.  18;  — yasca  dim  Jana^  . .  vthrk^m  yim  'zangnm dagvayasnsm  V.  7. 5  a  PilZ.
19691:•  j.  mat.ditnan-  Adj.  'sammt  seinen  Ge- schöpfen, seiner  Schöpfung':  hamistayatca . .  angrake  *mainySul  °manS  duidämanS Y.61.2.
19886:urvaisi  jass  (Sp.  494  o.)  matda  xia%rä ahml  vohü  manatihs  Y.43.6;  —  azfm täis%wä  fraxhil (sd.)  avami mazda  spstUH 'inyü  vispanqm  dätänm  Y.44-Ti  —  ahmst '''inyJus  rSr^^dnfi (sd.)  dngvani5..spmtat Y.47.4;  —  mainyü  (Sp.  1125  m.)  yayä spanyi  (sd.) . .  mravai  ylm  angram  Y.  4^.  2 ; ■ayü  *mainivä(Sp.  ri25  o.)  varat3..aüm tyui  spStUstS  y!  xraozdtÜJng  asSnS  vaste (sd.)  Y.JO,  s;  —  :^l(hr3m  daidlta  %wil.. fpSni^ta  °inyB  matdä  ". .  per  tuum  sanctissi- mum    spiritum,    o  M."   Y.43.2;  jy.  ra,
19888:nüiiya  (sd.)  xinstjm  Y.31. 3";  —  ts  (näml. s^ä^rä)  matdä  'inya  uxlyS  (sd.)  yl  ä nürSm^  . .  hämS  Y.31.  7'';  —  ahyä  *°in- ySuS  tvSm  ahl  tä  (Sp.  905  m.)  sf>nt^  ys ahmäi  gqm  .  .  hJmJa/at  Y.47.  3;  —  at tBi  mazds  tPm  'inysm  asaox^ayantyä  *ta- r^idyayä  (sd.)  .  .  Y.  J5.9;  —  äw?  ä  giul tala  (sd.)  as  *xratui  °inySus  masda  ahurä Y.31. 9  '^.  b)  der  Geist  des  Bösen  heisst angra-,  aka-  oder  dngvant-'.  mainya  (Sp. 1125  m.)  . .  yayä  spanyä  Biff  mravai  y^'" angr»m  Y.  45-  2 ;  —  hyat  vä  aka  manatahä ying  äafvSng  akascä  °inyul .  .  Jyaeharum fraSnas  ..  */«>■;»  (sd.)  Y.^2.s«;  — aya  *Mainivä(Sp.ii25m.)z'aratä y? drugvä acists  vfntys  Y.30.%.  b)  im  jAw.: ihä  'inyB  mamanaiti . .  vaoiatar!  . .  z/3- v>r>zätarS  Y.  ij.  4;  —  paslaäa  .  .  yat 'inyB  dSmqn  daSiltgin  Y.57. 17;  Yt.  TJ.yß ^'inyu);  —  yüthistB  'iniv&  damqn  V.  ig. 42;  Y.ip.is,  Yt.  13.  T  6  {'nivä);'^  ya%a apimim  'nivä  anhat  nivaiti/  Y.  10. 16; '9-9'>  —  "^'i  ■  •  ^hmi  paiti  nairi  dva *'inyu  rSnaisA.)  ava.stsvhat  ■V.7.52;  — rar  antarp  eam  asmammca  druja  (Sp.  781 m.)  °nivä  vaonyät  Yt.i3.iy,\^.  a)der Geist  des  Guten*'  heisst  spmta-,  spanyak-x ..yatmainyB  dqman  daCoTtfm yasia  spmtd 'inyul  yasca  attrö  Y.J7.r7;  Ytjy.76, 75.43,  Vyt.  47;  —  dqma  .  .  yi  hinti spfntahe  'inySus  Yttf.i;  Y.j.16,  Ä  6, 27.2,  Vr,/2.4,  Yt.Ä48,  70.142,  i^.^, V.5.33.  yi.  aS,  Vyt,5/;  —  yat  sp^ntS 'inyus  vitärayal  asmamm  Yt.  ij,  a8;  39, V./p.  9;  —  yS  dc&vä  Spante  »inyui  Yt 10.  r43;  —  avanayeni  spantim  'inyBm hala  . .  garS  nmSna  uspatayeni  anram 'inyBm  .  ,  haea  duiaaha;  tl  ml  vaifm 'kanjaysnte  spmtatla  'inyus  araras&i  Yt. ig,  44;    —    sfaranS  yahmi  paiti  "para-
23627:'kanqm   It^warijsangranqm  Y.p.  i8;
25528:•  g.  urüpa'ya-  den.  Praes.  31  '(Schein- bilder,  falsche  Vorstellungen  hervorrufen sva.)  täuschen,  betrügen' "':  *maäaAya  (sd.) yä  angrayä  karapanB  uropayäntl  yäiä xrata  äus»xsa%ra  dahyunqm  ". .  Rausch- Iranks  . .,  durch  den  böslich  die  Karapan und  durch  den  mit  Absicht  die  üblen Herrscher  der  Länder  betrügen"  \.48. 10.
27648:KompE.  —  Vgl.  'sangro:  —  ai.  jäiighä-  f. 'Unterschenkel',  mp.  (Pü.)  tang,  oss.  »ÖKgä 'Unterschenkel'.  — ')  ImOegens.  va'tangra-. —  ')  Hds.  sinha,  aoa.
27649:•  j.  zangra-,  smgra-,  ztara-'''^  m. 'Knöchel  (des  Fusses)',  von  i/a Ansehen Wesen".
```


## [2026-09-05T20:28:22.769Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '4090,4130p' BRT.txt"
}
```


### [2026-09-05T20:28:22.818Z] TOOL RESULT

```
•  j.  aßa-  m,,  Plur,  'Schaden,  Verlust, damnum':  yas?  tat  faiti  . .  tayus  . .  para.- baraiti  dasa  anat  paiti  'sS  (AP.)  eikayai (sd.)  V.7^,io.
Et  ?  VU.  aus  *ä'tp-iB.-<-\  lu  lat.  dam»um.  — Vgl.  aßmaii:  —  Pü.-.  ßV,  (Transskr.).  — •)  Etwa  wie  diwia-  aus  *diJbzÄi-}
•  g.  a-f3uyaat-  Adj.  'der  keine  Viehzucht treibt,  Feind  der  Viehzucht':  ysi  ..a^?tium var^dm  (sd.)  . .  fsuyasü  (sd.)  °yant8  (NP.) Y.419.4.
Pü. :  hal  an  i  aßönhiihi.
•  j.  aß-äSra-'*  Adj.  'den  Samen  des Wassers  enthaltend',  von  Sternen*':  Hstrim staivm  °r»n  Yt<?.4;  —  vlspe  starB  'ra S.IM3;  Yt/i'.z9;—  U.ira  gufra  'raukö
aora-  104
V.27.13; — stärqm'ranqm  z»masct^ranam urvarS.ci>ranqm  S.  /.  13;  Yt  8.  39;  — tUtrtm  Uär?m  . .  yahmäi  . .  fradäkat ahurS  .  .  'ralsva'^  smistai  yS  'raiibyB  (als Instr.) "'  aiti  (sd.)  raox^miha  vatsmnl  Yt
Ä45.
*)  Sie  sind  nach  Mx.  4g.  7  bestimmt:  pa awiiyÜH  i  5p  (nach  SD.:  vj-ddkaye  /layaiai),  d.  i. '2ur  Mehrung  des  Wassers'.
PB.;  Sp  hkrai.  —  O  NA.  auch  ohne  Trennung.
—  >)  NSml.  *ilirt!U,  slmbyS.
•  j.  afS-ta£ma-  Adj.  'wo  Wasserläufe  sind': gairJscä  'nB{AP.)"  Y.42.2.
Pü.;  äp  tacan.  —  ')  Unthem.;  unrichtig  S  ./ci/-
•  g.  aföman-  n.  'Schaden,  Nachteil':  yairii V}  'mänt  (AP.)  ssngkani  nsil  anafsmqm dsjämäspä  hvdgi'ä  ..  yi  . .  "wo  ich  (nur) eure  Nachteile "'  melden  will  —  nicht  die Vorteile  — ,  o/am.  Hv...,  vor  dem,  der.." Y.4Ö.17"-
KompE.  —    lEt.  S.  aßa-,  —    Fü.:  palmSnSi.
—  ')  D.  i.  die  Nachteile,  Schädigungen,  die
ihr  —  die  aiavan   des  Glaubens  wegen  von
seilen  der  ärfgranl-  erfahr!;  vgl.  Y.^y-  H-  — ')  Anders  Jn.  Zor.  77,  wo  weilere  Lilt.  — 3)  In  Verwechslung  mit  aßmati-.
•  j.yS  avdoa  nsit  aiuiyasti {sA.)  .."anuha vaca  ^tarspiUwa  ..  ii.i$.  [N. ":  lies avha;  s.  VA-,]
Pu.:  undeutlich, j,  aifuha,  at9ukaya',  s.  at^hvä-, j.  aaukar}tlät>m  V.  4.  49:  lies  haiiuk'. j.  ai>uhe,  'him:  s.  aaiav-.
•  j.  aDuhi-  f.:  s.  unter  ahü-.
j.  amthyat  Vi.  /o.  9,  51;  s.  auhvä-.
•  j.  aDra-'>,  g.  angra-  Adj.  'feindlich; Feind';  katär^m  ä  'rS  vä  hi-S  va°rS  y3.. cyaithat  hvS  ndit  ayjm  'rB  mainyet!  "bei welchem  von  beiden  ist  der  Feind?  Oder ist  der  der  Feind,  der  .  .  Wie  ists?  Soll dernicht  für  einen  Feind  gehalten  werden?" Y.  44- 12;  —  al  tsi  vJsp^ng  -ring  *asaonS adarS  "denn  alle  ..^iaanhänger  machen die  (ja)  zu  Feinden"  Y.  43- 1 5-  a)  mit mainyOT-  m.  'der  arge,  böse  Geist'  ^Ahri- man')  im  Gegensatz  zu  spanyah-,  sp^ttia—. mainyü  .  .  yayä  spanyä  (sd.)  üitl  mraval ySm  'r»m  Y.  45-  2',  —  tä  i/raiasays) '■  taaa  wvMfJ  hist>nia  yat  *mainyu  däman
dai'Jimt  yasca  sp?ntS  mair^us  'rosca  Yt. 13.16;  15.  43,  !j.  19,  Y.57.  17,  Vyt.  4-7, V.  13.  i,  S,  iS.  2  PüZ.;  —  aAurJ  mazäa  . . °rS  mainyus  H.2.17— 35;  —  t?margüxs bavät  'rS  mainyus  zfmarguxö  iariinii  daii'a
dby  Google
FrW.  4.3;  —  'rahe  mainySus  dämanam ^'^  '5'  3i  —  y^t  titarat  °rS  matnyus dähim  alahe  .  .  antan  pairi.aväit^m  (sd.) fokuca  mattö  atarsca  /J  hg  taurvayatsm tba^ä  °rahe  mainySus  drvats  Yt  7_J,  7  7  f. ; 13;  — yint  nöit  tiurr/pttte  'rS  mainym nsit  yatavS  fairikssca  Vt  1^.44;  —  ailm dahakim..yqm..  drujim  fraca  k>rmlat  'rS mainyus  Y.(?.8;  —  aal  ahe  paityarim  frä- ijrMiat  'rö  mainyus . .V.l. 2;  'J0.3,Aog.2^; —  pairiAä  .  .  yä  uzdtihat  'rS  mainyuS  .  , paiHj>r)tSe  Yt,  A",  39;  —  taxm?m  urupi  .  . yat  barata  'tvm  mainyBm  framitim  (sd.) aspake  JaArpa  ^risatjm  aiwi.gämanam Vt./^.  29;  — paiti.psrme  'nm  mainyBm V, /o.  5;  —  fränämiliti  duhjarstavari'  °r3 mainyus  ax^amanS  Yt/p.  96;  3.^;  — naiHs  xsayät  °rö  mainyus  duzdalnS  FrW. 4.  a ;  —  xsnagiira  akurahe  mazdä  tarSidlti 'raAe  mainyius  Yt.  i.  o;  —  daxstanam  ydi Amli  'rahe  ntainySus  daxstim  V.  2.  29;  P, 2-2,  Y,  7i>,  11;  —  apayafUamah^a  'rahe mainyius  xrafstra  Yt.  21.1;  —  'rif  mainyus . .  dtävanam  daivS  V.  ig.\;  —  vJspB.mahr- käatca  pairi  drvatat  yat  -rst  mainyaot VL/_j.7i;  /0.118,  Y.2-j~-i,  V.'/o.ie;  — ai  duida  °ra  mainyS  V.ii).^;  g,  1,44,  lt. 10,  Yt//.  19; —  iaÖx  dusda  'ra  mainyö V.  i^,  1 2 ;  —  *'rahe ''  *mainy9us  duzdamanH Y.  Ö/.  2;  V. /p.6;  —  skutara  "ra  mainyö V.  79. 3;  —  "rS  mainyus  pouru.mahrkS (Stveri.)  Yt  10. 97 ;  usw.
KompA. ;  Ableit.  —  Aus  ar.  *aira-,  lu  einer  ar. Basis  'ans-;  s.  qita-,  ariia-,  ahifrailay-  und Bthl.  BB.  S.  22o;  S  2^  No.  1,  woiu  noch Wilhelm  Mus.  8. 123.  —  rop.  ahraman,  arm. LW.  arhmn;  s.  dazu  Hbh.  AGr.  /.  26.3)  — Pü. :  dnnak,  bei  den  Paisen  ^a»ä  gelesen; ich  lese  versuchsweise  niräj,  IF.  /2. 93i  Sale- MANH  GliPh.  I.  366  will  anräk.  Sij. :  hanlä. —  I)  Vgl.  No.  Z.  —  ")  NA.  angr';  s.  Var.  — J(  ^p.aArT/nan,  gt.'Apnnävnf  setieo  eine  urir. Nebenfoini  *ahri}it-  Toraus.
•  j.  aBr5.mainyav-  Adj,  'dem  bösen Geist  entstammt,  zur  Schöpfung  des  bösen Geists  gehörig' :  iaAe  vaca  vanai  . .  kana zaya  mana  dqma  'yus  (IP,  als  APn.) ''  V. /»).8;  —  -ffl/  tat  dqma  spmfs.matnyava ailauhqm  dämanam  .  .  Aazatpraja  "yus (nämb  dama;  IP.  als  APn.)''  paiti.jasaiti V.13.1.  '
Ableit.  10  aarö  mainyul  (NS.).  —  Pü. :  türäi mtnök.  —  ')  VgL  lu  yälav-  No.  I  und  iiüpä/a Jifma  . .  aiamS  V.  7/.  ö.
•  j.  aorBjnainyava-    Adj.    'dem   bösen
anhav-  106
Geist  entstammt,  zur  Schöpfung  des  bösen Geists  gehörig':  yat  bs  patti  fraist^m bavainti    yavanqm  gyr^iqm  V._J. lo;  22;
—  kahyäcit  'yavanqm  xrafstranqm  V.  16. 12;  —  ma  hwä  ^'yavS  manisiis  * ästaraita Vyt.  J7(?);  —  kat  tat  dqma  "yava  (statt NSn.)  'J  altarfhqm  drlmanam  V.  ij.  5.
Ableit  lu  dOrä  mainyus  (NS.).  —  Fü,:  iütäi mtnit.  —  ■>  An  dipna  nn geglichen?  Oder Pluralfarm,  weit  d<^ia  ASn.  und  APn.  ist? Vgl.  spinlö.maiHyava-  No.  I.
•  j,  aDha-  m.  'Lager,  Lagerstätte':  yS  hl 'nhat  nasdistsm  nmämm  uzdasta  "wer  das ihrer  (der  Hündin)  Lagerstätte''  nächst- gelegene Haus  gebaut  hat,  . ."  V.75.21.
Zum  u.  V.  Bosalr.  —  \'gl.  asla-.  —    Pü. :    i? hac  Si  noidist  man  u^dät  eslel,  erl. :  kui  länak dar  niad.  aah'  ist   also  nicht  besonders  aus- gedrückt. —  O  Wo  sie  geworten  hat. j.  auhatiia  Yt.  10.   129;  lies  ayai»h°.
•  j.  a-Dhaoävmna-  Adj,  (fem.  'ml-)  'nicht ver-,    austrocknend' :   yat  kprptiaoi  .  ■    °ne
|(ADf.)  äpa  urvaire  Y.5.4;  Yt  79.32. *kaasimna-,  PPM.  lu  *haosa;  Praes.  2.  —  Vgl aL  iüfyati  'er  vertrocknet',  np.  sSüdan  'ver- dorrt sein',  gr.  aIo(.  —  Vgl.  huska-.  —  Pü. : undeutl.,  dazu  die  Erl.:  an  i  ne  afiäyojl  Ausk ne  Ausi;  SQ. :  aSaft.  —  »  Zu  Yt.  1$.  16  fälsch- lich aai/iis',  s.  S  26S.  57.
•  j.  a-nhaiSya-  Adj.  'unlauter':  °^lm frafravayahi  tUm  yS  ahurS  maxdä  .  .  aoi zrayS  püitihm  "schwemmst  du  ,  .,  was unlauter  ist,  fort  . .  zum  See  .^.i^' V. 5. 76;
—  para  oAmäJ  yat  hiin  aSm  *draog»m i'äHm  '%Jm  Hnmäne  (sd.)  paiti.barata Yt/p.33-
ai.  asafyä-  Adj.  —  Pü. ;  anäikärän,  erL :  nasäk i  nikän,    dazu  die  Bern.:    asi  ie  aHarianlkän
```


## [2026-09-05T20:28:22.976Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"Feindschaft\" BRT.txt | head -30"
}
```


### [2026-09-05T20:28:23.021Z] TOOL RESULT

```
7844:•  ]-•  S-  S[sta-  m.  'Hass,  Feindschaft; Feindseligkeit':  %wahya  mazda  °tä  (IS.) urvataAyäisd.)  Y.34.&; — yü  gä^ä  asrü- vayd  *'ta  (IS.)"'  vH  tarff.waiti  v3  tanUm *piryetti  "wer  die  G.  nicht  aufsagt  aus Hass  oder  Trotz,  verwirkt  den  Leib"  N. 41;  —  kS  *tff'^  **J  *iarS.»iaitis' (sd.)  N. 41;  —  cim  aosaaAi  aoSaaukaiti  'Um Uaiti  tanva  Aog.  4S(?);  —  a  f/  dvafsSng (sd)  ..  anale  -tqsca  Y.  44-i4)  —  y^ maiiyä  yaoi  akmsi  .  .  vaAista  . .  SStiim  . . 'tftig  ahtnai  y7  nä  astät  (als  Inf)  daidüä ".  .  Feindschaft  (aber)  dem,  der  uns  zu befeinden  vorhat"  Y.  ^.  18;  —  °ta  ava- spayama  vä  Vyt.  44.  a)  DS.  '/ai  als Id£  sbes.
12078:•  j.  tarö.tbaeäah-  Adj.  'der  die  Anfein- dungen, Feindschaften  überwindet':  '/ff (HSm.y^  ..l6ae^g.tard  nqma  aÄmiYtlS-47.
12512:Eig.  'die  Feindschaft  der  D.  bildeod',  d.  L 'TOn  den  D.  befeindet'.  —  Wegen  des  Stamm- ansatiei  und  der  Kaiusbildung  $  3^4-  — >)  SoMf3;  NA.  mit'Fi  daaiaif,  wai  wegen t  weniger  wahrscheinlich.
14746:•  j.  tbaeäah-,  g.  dvaeSah-  n.  i)  'An- feindung, Feindschaft,  Feindseligkeif:  iTr- pSng  any^ng  matnySu^  spasya  (sd,,  'ich' näml.2flr.)  °sar?ka  Y.44-ii;  — paityaogsl (sd.)  lä  (näml.  iyao^ani)  aAmai  jassit 'lanAa  (IS.)    Y.  46.  8.  a)    sonst    nui^
14766:•  j.  tbaeiÖJata-  Adj.  'durch  Feindschaft getötet':  yat  afte  yä  sps./ata^a  (sd.)  .  . 'ta^a  V.7.3.
14768:•  j,  tbaeSö.tara-  Adj.  'der  die  Anfeindungen, Feindschaften  überwindet':  tarS.lbaiss  (sd.) .  ,  °rS  nqma  ahmt  Yt  /j.  47.
14772:•  j.  tbaeSö.taurvayffSttma-  Adj.  'der die  Feindschaften  am  besten  überwindet';
14775:•  j.  tbaeäö.par^ta-  Adj.  'aus  Feindschaft, in  feindseliger  Absicht  gefragt':  uia  hl fraiha  (sd.)  paiti.mravSne  navaca  navai- tXmla  xruidranqm  °tanqm  yat  mqtn  p»r>- sai ..  "..  auf  die  99  schwierigen,  in  feind- seliger Absicht  gefragten  (Fragen),  wenn  . ." Ytj.  82'';  —  iard^uströ  asaritS  aka manatgka  xrüzdya  'tanqm  ",  .  durch  die Schwierigkeit  der  in  feindseliger  Absicht gefragten  (Fragen)"  V.  ig.  4.
15117:•  g.  paity-aogat  Adv.  itickwäits,  zurack': f  ts  ahmäi  jassit  ävaglanha  tamiSm  a "znrüclc  auf  ihn  sollen  sie  (näniL  die  Taten) sich  mit  Feindschaft  gegen  seine  Person wenden"  Y.  46. 8.
16898:ks  ava%a  dafnqm  ..  vl.barai  V,  2.  42;  —  , aat  "hwa  (näml.  haonam) . .  trurrfa  viivanca  , vXbann  Y.  10.  11;  —  mit  Abi.  des  woher? und  Dat  des  wohin?:  yahmäl  iahmäiat (sd.)  nalmanqm  vätB  ahrS  baoi\im  vi- baraiti..  V.S.80.  3)  '(Daevisches)^'^ weg-, fortschaffen':  vT nS  tbiyvatqm  (bal^bl^ vi  manS  bara  gramintam  "schaff  fort  unsrer Feinde  Feindschaften,  fort  der  ergrimmten Anschlag"  Y.5. 28.
24115:•  j.  vi'dvaestva-  Adj.  'nicht  anzufeinden, dem  keine  Feindschaft  droht,  was  anhaben kann'":  das)mS  yat  ahmi  .  .  HaäirudasS imal  'vd  ". .  vierzehntens  bin  ich  das: unerreichbar  für  Anfeindung"  Yt/.  S;  — yasnahe  haptafihatsis  . .  yU  fravaoce  maza amava  virihraja  °vü  Vr.  15.  3.
25677:•  g.  urväta-  d.  'Bestimmui^,  Gebot'; a)derGfitter:  %waAyä  matää  qstä  Uahyä "aus  Feindschaft  wider  dein  Gebot,  o  M."  j Y.  J4. 8  ■>;  —  hyat  tä  Uä  sasa^a  (sd.)  j-ä mazää  dadat  ^.30.  ii'^;  —  ta  v!  'tä mannte  . .  sfnghamahT  "eurer  Gebote  ein- gedenk . ."  Y.31. 1  "j  —  aväts  'täfi  yä ts  matää  dfdarizS  "nach  jenen  Bestim- mungen, an  denen  du,  o  M.,  festhalten willst"  Y. 44..  IS-  b)  der  Drug:  asibyS ySi  •läii  drüjS  .  .  vlm^rmcaia  (sd.)  Y. 31.1.
29196:rechter  Feindschaft  beseelt,  ein  echter  und ichter  Feind';    's\i    hyat  isöyä   dngvSifi at  *asaom  raßnS   hy3m    aojsngkvat   "ein echter  Feind  will  ich,  so  gut  ich  es  ver- mag,  dem  ^r;<fgenossen  sein,  aber  eine kraftvolle    Stütze    für    den    .J/aanhänger" Y.43-^- P6. :  äikärai  ieti/är,  Npü. !  äsiara  ätar  tUhanda. —  1)  NA  trennt.
```


## [2026-09-05T20:28:36.218Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '7840,7870p' BRT.txt; echo \"=== col markers near ===\"; awk 'NR>7700 && NR<7900 && /^[a-zA-Zšžāēīōū°ə\\x27.-]+ +[0-9]{2,4}$/ {print NR\": \"$0}' BRT.txt"
}
```


## [2026-09-05T20:28:36.527Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"361\" BRT.txt | sed -n '1,40p' | grep -i \"asta\\|ast\" | head"
}
```


### [2026-09-05T20:28:37.955Z] TOOL RESULT

```
>i.  ämia-  m.  —  Pü. :  hac  ö/än  an  raiiin.  — .)  VgL  'rJm...
•  j.  i^sav-  m.  'Schoss,  Zweig*  der  Haoma- pfianze:  ^ävaiitJ  alte  'sai'S  arihin  "wie gross  sollen  die  Zweige  sein?"  N.  to8;  — havamm  (sd.)  . .  yd  'sus  (AP.)  hangmr- vayäti  Y.jo.i.
KompE.  —  ai.  amiäv-  m.;  ■>.  dazu  Roth ZDMG.  jj.  684.  —  l'a-:  l^t.
ß,  '"ifsahitä  Y,  4S.  l:  s.  HS-  mit  No.  i.
•  ]-•  S-  S[sta-  m.  'Hass,  Feindschaft; Feindseligkeit':  %wahya  mazda  °tä  (IS.) urvataAyäisd.)  Y.34.&; — yü  gä^ä  asrü- vayd  *'ta  (IS.)"'  vH  tarff.waiti  v3  tanUm *piryetti  "wer  die  G.  nicht  aufsagt  aus Hass  oder  Trotz,  verwirkt  den  Leib"  N. 41;  —  kS  *tff'^  **J  *iarS.»iaitis' (sd.)  N. 41;  —  cim  aosaaAi  aoSaaukaiti  'Um Uaiti  tanva  Aog.  4S(?);  —  a  f/  dvafsSng (sd)  ..  anale  -tqsca  Y.  44-i4)  —  y^ maiiyä  yaoi  akmsi  .  .  vaAista  . .  SStiim  . . 'tftig  ahtnai  y7  nä  astät  (als  Inf)  daidüä ".  .  Feindschaft  (aber)  dem,  der  uns  zu befeinden  vorhat"  Y.  ^.  18;  —  °ta  ava- spayama  vä  Vyt.  44.  a)  DS.  '/ai  als Id£  sbes.
Ans  ar.  *a«j-lha- ;  ygl,  (Et.  unter  aora- ').  — Pü.;  aiuufih,  (EU  N,  41)  erl,!  ka  gäwit  ku  den ntsi;  [iD  V.  44):  anasi  iat;  Sü.:  nSsäiatvam, anäitiiatvam  'Ungläubigkeit'.  —  >>  Hds.  ifslä.
—  »)  Ganz  Verkehrtes   bei  Dst.  ZA.  r.  309.
•  g.  ^^  Inf."  'zu  befeinden':  asting (sd.)  ahmäi  yf  nä  qr  daidltä  Y.40.18.
Zu  einer  Basis  ar.  '*ans-,  %.  airra-.  —  Vgl.  1 ^Af.  —  Ptt.!  anasak.  —  0  Zu  S  25*.  a  e  e.  I
t^Ö.bug-  363
!•  j.  a^'  V.  'schnüren'.  Praes,  3  aza- (/lyäza-yK         Inf.  qzatthe.
'schnüren'  sva.  'einengen,  bedrängen': s.  Inf.
mit  Kf 'einschnüren,  einzwängen':  ha  hi maiofm  nyäsala  "sie  schnürt  sich  ihre TaiUe"  Ytj.137'*.  a)  'hineinzwängen in  — '  (Akk.):  täst>m  däuru  .  .  stamanim he  aoat  nyszaym  ".  .  ein  zugeschnittenes Stück  Holz..;  in  sein  Maul  sollen  sie  es dann  hineinzwängen"  V, /J.30.
Vgl.  gt.  äna,  lat  angö;  s.  auch  qzah-  und No.  I.  —  Pü.:  awialan.  —  «)  Ob  statt  nyas" geschr.?  VgL  S  ^68.  3  a;  s.  aber  np.  niyäz 'Maogel'  bei  Hbm.  AGr.  /.  105,  Weiteres, auch   la    aL    anSha,   IF.  8.  235.    —  »)   VgL
•  J.  lucaBhe  InC  'zu  bedrängen,  in  Not zu  bringen':  ava^he  narqm  asaonqm  qz° duwarltavarxsam  Yt.  13. 39.
Zum  V.  qs-.  —  Vgl.  qsah:
•  j.  ^ah-  n.  i)  'Ein-,  ZusammenschnU- rung*  der  Kehle,  'Erdrosselung'  (nur Komp.).  3)  'Bedrängung,  Enge,  Not; Gefangenschaft':  mi^nm  .  .  yS  nargm  .  . ipa  'zatshat  .  .  fäyajanhat  baraiti  apa nö  haca  'zaahat  apa  haca  'satihibyö (DP.)'>  harSiS^l.  10,22V,— th  nS 'tahucit hals  %rayente  YL 13. 1 46 ;  Vy  t.  $0;  —  yd  AÜ
frayazaite  . .  kahmaiHt  °zat)Aqm  biwivä Yt.  ry.  41;  —  ravasla  o^idrimla  (sd.)  . . aiaonö  stsil  'eas/a  dtäa'intiUa  . .  drvats stSisY.S.8; — yas/a  ml  ail^m  nanm  "zö <vi  avag>r?pt>m  ravöhu  paiti  uzbäraya£ 'imd  wer  den  .  .,  der  in  Gefangen- schaft verbracht  ist,  wieder  in  Freiheit versetzt"  V.  r<?.  10;  —  haoma  .,  yalcit ■zahu  dirilärihs  Jaininam  *upa  *d?rfzaAu (sd.)  Y.  io.17.  a)  liS.  'zaKAe  als  Inf.
sbes.
KompA.,  E.  —  Zum  V.  qz-.  —  ai.  dniAas-  a.
—  PQ.:    langlA,  Sü.    (lU  Y.  8):    näslihyam.  —
I)  zF.  s.  S  3St.
j.  ^zB.jata-  Adj.  'durch  Erdrosselung getötet" :  yat  alte  yä  sps.jataca  (sd.) . .  °tala V.7-3.
Pu.;  langlk  iai,  ei[.:  pa  xafak'ih.
j.  ^ö.büg-  Adj.  (auch  fem.)  'aus  Be- drängnis, Not,  Gefangenschaft  errettend, befreiend':  xratüm  .  .  alavan»m  'büßm -avatdqm  V.  18.  6 '';  —  */rasainttm  .  . 'bußtit'^  hiiJrqm  Y.  ^2.5;  — frazantöis  .  , ■büjd"''  kvlrayi  Yt.j_5.134.
Pü. :  hai  tangVi  idxtärlh,  erL :  hac  döias^  'aus
ob,Google
i  —  Hia  1 3  364
Vgl.  V.  iS.  10.  —  '>  S.  [  d»r?iaj  'oa  srävayaoyat  Vyt^ff.  3)'von nun  an,  künftig':  i-i'^a  °oa  Aista/ie  anyehc ift-a/v  (sd)  ,.  V,^,  ag;  —  ba'ja  'oa  aoii hr7>i  (sd.)  V.J.  27;  27.  a)  loa  apqm (sd.)  'von  nun  an':  zätö  äiirava  ..  "oa  apqiti vJjasaüi..daliiaW.i3.')a,;  95'.  3)'dann, alsdann':  imat  nmäium  yaolda^itne  imq *'oa''>  vacd /ramrt-a  V.//.4; — ai-i  aküm .  .  *s3mS  janhsntu  .  .  'iiriiajca  (sd.)  °wi . . gfus  afia./asat  V.  2,  a  2  £
■     ■  ■ '  Adv.  -  P6. ;  fMr '),  (lu  V.  //) :  ün^Ji. JA.  aia;  s.  aberVar.  —  ")  Vgl.  zu  'lia
[Vgl.  nDter  yc:\ j.,  ß.  T:  s.  'ay-  und  i.
=== col markers near ===
```


### [2026-09-05T20:28:38.006Z] TOOL RESULT

```
21242:Formen:  tai  möi  daidr  ahura  hy  mazää rapin(sA.)  tavä  Y.51.  18;  —  neben  einem Objektsakk. :  iahä  . .  sanm  (sA)  caränl.. *äsi»itlm  (sd.)  x/mäAam  kyatcü  mSi /iyät voxs  also  (sd.)  Y.  44. 17;  —  neben  einem Inf.:  Ayal  (zu III)  vTs}nta[sA.)  dngvantftn avS  hyaiiä  gäul  jaidyai  (sd.)  mraol  Y. ^2.14.  b)  im  jAw.;  i)  mit  Ind.;  ia} ahtnai  jasal  äyapUm  y  Alpu^rü  us.zayata Y.5,4;  7,  13,  13;  —  moiu  iai  äs  .  ,  y° fräyatayat  .  .  aoi  zqm  Yt 5.65;  —  altat il ..  aiAhe(ßp.\om)  avayam  *dqtimaM y*  %wä  didvJsma  Y.^Äi;  ' —  i'mai  .  . Stävi/Um  ^yad^tiim  maSya  viminti  .  .  y kainyS  uzvätaydnti  Yt.  ly.  59;  — ya%a/rä toa  (sd.)  amraot  y*  dim  a/iBmisd.ya  .  . adadat  Y.ig.13;  —  ankam  raya  ufar)- natshala  (nämL  asti)  y  bavainti  halat.- pu%rä  Yt/j.  15.  2)  mitKonj.:  avat ayaptim  dazdi  ml  y  bavStii  aiwi.vanyä . . vlstäsptm  ..  ydka  (Sp.  1247  u.)  aztm  ni- janäni  ..  Ytf.  117;  34,  38,  50,  S4>  S«. 73.  82.  109,  "3.  P-4,  Jj-ia',  16',  38', 32i  361  40;  —  kaimai  .  .  tat  da'inm daysty  hl  atihat  :^airyqn{%A^  a/yamtum Yl  13.  50;  —  avahela  paiti  yqnahe  y  h! da%at . .  pähave  zsvar)  Yt.i6.6i.;  —  aam ai^he  asti  usvamim  y  nä  kasvikamal . .  avarstanqm  naire  . .  ajasta  .  .  daositi  V. if^-ZTi  vgl.  noch  V.7.5'.43  unter3;  —  aval hi  masyS  arüiim  (sd.)  y  iistamm  bun/a- _y.T/V.  7,  71;  —  ä/  zaoiars(sd.)  kairim ankai  .  J  (y)^^  gä'^/'is/a  fi-asravaysiti  . . aat  hävananS  (sd.;  nämL  kairim  attkaC) y  kaom>mca  akunavat..aat*atravaxlahe y'  ätnmca  aiwi.vaxsayät ,  .  N.  72  f.;  74~ j6^.  3)  mit  Opt;    aom    aiäAe   asti
26954:(Sp.  13610.)  ..yastl  nSla  •(ffY.43.16;  — p^ä%rfm  daidita  %wa  *cütiw3  (Sp.  585  o.) ■Ö  maitvyü  Y.  43- " ;  JE?- 1 2.  5'-  7.  3<J- 1 ;
```


## [2026-09-05T20:28:50.661Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; python3 - <<'EOF'\nt=open('WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nimport re\nfor i,pg in enumerate(pages):\n    m=re.search(r'\\b1(3[0-9])\\b',pg[:300])\n    if 'ans-' in pg or 'anes-' in pg:\n        pass\n# find leaf containing printed page 134: search for header lines\nfor i,pg in enumerate(pages[120:170],start=120):\n    head=pg.strip().split('\\n')[0][:100]\n    print(i,'|',head)\nEOF"
}
```


### [2026-09-05T20:28:52.611Z] TOOL RESULT

```
120 | )
121 | ekuo-                                                               113
122 | 114                                              eg-, <5g-, eg-   — eg-
123 | eghi-    — eg(h)om                                                   115
124 | ;
125 | et(e)n               eter-                                               117
126 | 118                                                eti-s   — ed
127 | \                      :   )                                                                        
128 | 120                                                           ed
129 | edh   epi-                          121
130 | 122                                         epi, opi, pi
131 | epop, opop                                                          123
132 | 124                                                      eps-,   eph-   em-
133 | ;                                                    )
134 | 126                                                                            en
135 | en    — eneu, enu                                                   127
136 | 128                                eneuen, neun, enug            — enek-, nek-, enk-, nk-
137 | yvexys „einen Speerwurf weit“                                =
138 | 130                enedh-, endh-               — (enebh-) ombh-, nObh- (nebh-?), mbh
139 | :                                                                    g                              
140 | 132                    eu(o)nien-, (o)nomen-, nomen-, e n(„)men-             — enos-, onos'
141 | eng-,   ong   engj-, gg«en                           133
142 | 134                                                ent-   — ens-
143 | er-, or-   — er-                            135
144 | i                                           :                   ;
145 | ct-                                        (37
146 | :                                        ]
147 | er-                                                                139
148 | ;
149 | -                                                                          ;                        
150 | )          ;
151 | :
152 | 144                                                                    ere-, re-
153 | ;                                                           :
154 | 146                                                ereb-, orob, rob-            — er?5d-
155 | erk             ergh                                                          147
156 | 14S                                             erd-    — er(a!d-, er(a dh-
157 | :     )                                                                                           :
158 | :                                           ;                    :
159 | ;g
160 | 152                                                         el(eu)        el - : ol-
161 | ,                                :                                                                  
162 | 154                                                             el-
163 | ;,
164 | i    :,6                                                                            5(i)l&   —   ele
165 | „Ellenbogen, \Yinkel“ (-11- aus -In- der synkopierten Kasus, vgl. Pedersen
166 | :                                                                       ,
167 | ;
168 | .                                               .
169 | b                                                                             -
```


## [2026-09-05T20:28:56.264Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; awk 'BEGIN{RS=\"\\f\"} NR==143' WLD_Bd1_pages.txt"
}
```


### [2026-09-05T20:28:58.019Z] TOOL RESULT

```
134                                                ent-   — ens-
  *neg'ih-ros „Niere, Hode“ („rundliche Anschwellung", vgl. zur Bed.
lit.inkstas „Niere“ und „Hode“; -ro- und -en- vielleicht Entwicklungen
aus einem alten rjn- St., Pedersen KZ. 32, 247 f.) in:
       gr. vEfpgog,       meist PI., ,,Nieren“, praenestin. nefrones, lanuvin. nebrundines
„Nieren,        Hoden“ (a. zum lautlichen Yf. IF. 19, 102);
       ahd. nioro „Niere“,T. auch „Hode“, mengl. mnd. nere, aschwed. mure,
                                  z.

aisl. riyra „Niere“ (germ. *neuron- aus *neguhron-; der aisl. Umlaut ist aus

einer Umbildung *nenrion - zu erklaren), aber fern bleiben air. aru „Niere“,
cymr. avert f. ds. (irrig Yf. Uber alteste spraehliche Beziehungen zwischen
Kelten und Italikern 48 f. ; als nicht iiberzeugt bekennt sich mit Recht
Pokorny brieflich).
  Curtius 316, Osthotf IF. 4, 271 f. (Lit.) Yf. LEWb. 2 386, 513.                   Nicht
iiberzeugend Charpentier KZ. 46, 44 ( *n-gu-cn zu [iov-fiwv usw.).

                                       :<
ent- „anzetteln, weben                      (?).

  Alb. ent, hit „webe, zettle das Gewebe an“ (G. Meyer Berl. Phil. Wchschr.
1891, 570, Alb. St. Ill 24    ai. dtka- m. „Gewand, Mantel“, av. adka-, atka-
                                             ',



m. „Oberkleid, Mantel* (nicht nach Hirt Abl. 137 von einer Wzf. et[e\q-
                                        1
                                        ’




neben *teq- „weben“), gr. (doch s. u.) utt o/uai ,,ziehe die Kettenfaden auf
den Webstuhl auf, webe“ (aus *azioucu mit analogischem tt statt aa nach
Art der Gutturalstamme, wie z. B. egexxco von egexgg), dtd£o/zcu ds. (Ent-
gleisung, vgl. z B. Curtius 5 319, Debrunner IF. 21, 216), aofia, dtaojua
 „Kettenfaden“ (strittig ist jon. i$doTies „herausstehende wollige Faden am
 Gewebe“, s. Boisacq 261, Fraenkel IF. 32, 121; dvziog „Weberschiffchen“
 klingt nur zufallig in der Bed. an, wohl zu avriog „gegeniiber“, Prellwitz 2
 42).   Schrader, zuletzt bei Hehn Ivulturpfl. 8 573, s. auch Bartholomae
 Airan. AYb. 61.
    Air. etach „Kleid“, mir. etim „kleide“ (Strachan BB. 20, 32) vielmehr *en-
 4- *teg- „decken“ (s. Pedersen KG. II 655; auch nicht nach Lagercrantz
 Z. gr. Ltg. 71, Marstrander IF. 20, 352f. als pnt- zu gr. jzdrog' evdvjua rrjg
"Hoag Hes.).
   Die gr. Sippe aber wohl vielmehr mit a = idg. 3 oder a zu iftoiov, dor.
axQtov „der (stehende) Kettenfaden beim Gewebe, Aufzug des Gewebes“,
bv)xQifiog „nebeneinandergereiht wie die Kettenfaden des Aufzuges, die
tjxQia sni xq> yxgtq)“ (Bezzenberger BB. 5, 313, Ehrlich KZ. 40, 375, Bechtel
Lexil. 1 30 f. ohne anl. _p-, daher nicht zu *uei- „flechten, weben“ oder zu
                      ;


ahd. wilt „Kleid“, Lit. bei Boisacq 330 mit Anm. 2, der freilich 1009 rjxQiov
trotzdem zu ai. vatavc „weben“ stellt, s. u. au- „flechten“).      Auch das —
 ar.     a-   ist   doppeldeutig.


 ens- „in feindseliger Absicht treffen"?
   Die Gruppe ist unsicher. Man konnte an einen Zusammenhang folgender
 Worter denken: ai. asand ,AYurfgeschoB“, astra-m „Gescho6, YVurfwaffe“,
 dsyati „wirft, schleudert“, av. rmJiyeiti ds. (Fick I 4 171). Dazu av. qsta- m.
 „Feindschaft, Yerfolgung, HaB“, ( *ans-tha Bartholomae Wb. 361), qstai inf.
 „zu befeinden“, gpav. angra-, av. atom- „feind, arg, bose“) aus *ans-ra- oder
 *as-ra- s. Johansson IF. 2, 26).   Ygl. ap. cthi-fraSlay „strenges Gericht“
 (Kompositionsform der ro-Stamme auf i ) arika „feindlich gesinnt’ ( *ahrika).
                                                              ;
                                                                                1
```


## [2026-09-05T20:29:24.745Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== POK ens/ans ===\"; grep -n \"ens-\\|\\*ans-\" POK_full.txt | head -20; echo \"=== POK epi opi lemma ===\"; grep -n \"epi, opi\\|Root / lemma: epi\" POK_full.txt | head -20"
}
```


### [2026-09-05T20:29:24.805Z] TOOL RESULT

```
=== POK ens/ans ===
9334:Root / lemma: ken-2, kens-, keni-, kenu-\ "to rub, scrape off; ashes' must have come from 
16554:Archilochos Saipoov "Sanpwv' see below *dens- " high mental power '); Sa'i'^u), Fut. -^co, 
17183:cfens-1. 
18047:Root / lemma: dens-1 
18097:compare finally Schwyzer Gr. Gr. I 307 and see below dens-2. 
18102:Root / lemma: dens-2 
18106:contradict the explanation of *5au) from *dnsd{see above under dens-1)\ indeed from W. 
50146:Root / lemma: Rens- 
61083:Root / lemma: menot. Gen. meneses, from which menes-, mens- mes-, men- 
61092:(conservative Gen. PI. mens-um), menstruus^ monthly ' (GN Mena\s gr. loanword), 
67803:Root / lemma: pes-2, nasalized pens- 
73562:belongs prakr. samgha/to Rens-, above S. 566. 
85658:compare /e/7i/-5"thin' and die extensions tengh-, tenk-, temp-, tens-. 
85754:Root / lemma: tens- 
87413:Root / lemma: tres- tens- ( *teres-) 
=== POK epi opi lemma ===
27210:Root / lemma: epi, opi, pi 
29331:Root / lemma: epi-
```


## [2026-09-05T20:29:25.610Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== KNT arika ===\"; grep -n -i \"arika\\|ahrika\" KNT.txt | head -20; echo \"=== KNT apiy ===\"; grep -n \"apiy\" KNT.txt | head -20"
}
```


### [2026-09-05T20:29:25.673Z] TOOL RESULT

```
=== KNT arika ===
521:abiyajavayam XPg 9, and abijdvayam ХРЕ 40. niyasaya DNb 5, 46, 49, probably for *niyayasaya. [a]fiya[s?]ya DB 4.91, perhaps for *atiyayasiya. marika- DNb 50, 55, 59°, cf. Phi. mérak, Skt.
1526:*mer- ‘die’ in marika- ‘menial person’ (see Lex. s.v.), *mor- in martiya ‘man’ (see Lex. s.v.), *mr- in marta ‘dead’, uvä-maršiyuš ‘by self- death’ (see Lex. s.v.); perhaps *m»r- in amari- yata ‘he died’ (cf. Av. miryeite ‘he dies’).
3895:КІ. has the following correct readings, in which he records as legible certain eharacters, here indicated by roman type, which were not visible to KT: ! Dàá]rayava- [ш 3 г [yaBiya; ? ham[igiyam; * mand : І Naditabaira, ? Asagar|ta:y; “adujrujzya; ?0ü]tiy; 9 һуа; * ha}- mahydyd; % arika; " діри; ™taumd; 9 Dérayavaus; 8 agaubata; ** ada|kajy; % пата (prior occurrence); 83 Parga; 8 Guz]rahyá; “ Guu[baruva.
3954:2 paltiy Wb. 2-3 a[vd}jmet Hinz. * фот Kent (after Wb.). 5 тт KT, U}mamazta later editors; А атаа Hüsing; A]mamaita Hinz, after Wb. 7 [I] RI. 4 [Üvjiya] WBn; aja Foy (not avjàja). ula : daiy : marda RI., KT; corrected to ula : viyamarda, with wrongly inserted divider, by Wb. ZfA 46.55; see also M4 and note 3, and Lex. s.v. mard-. 1? {tyamSaém} WBn. 5 a{vaty Kent, for Hinz's afvā. 15 [hamigiyd : аһа] Hinz; farika] Hinz later. M [лају : ayadiya] Hinz; A[uramazdám] Wb. KIA. 19 ya[dátaiy Tm. VS. ? [utà Foy; artah]yà |: bavatiy Hinz, after Oppert’s translation ; mariah]ya Wb., [5015] Kent JNES 7.107 n5.
5050:arika- adj. ‘evil, faithless’: deriv. (6146.11) of *asra-, GAv. angra-, LAv. apra- ‘hostile, enemy’, to рАт. root *ans-, seen in Av. qsta- ‘hate, enmity’; ef. also Av. (nom.) avrd mainyus ‘evil spirit, Ahriman’ (Bthl. AiW 189); not to Skt. art- ‘en- emy’ (MB Gr. §273), nor to Skt. alikd- (Wacker- nagel, KZ 59.28-9). алка nsm. DB 1.22, 33; 4.63. ага npm. DB 5.15°, 31°.
5775:mar- vb. ‘die’: Av. mar-, pres. miryeite ($122, $214), Skt. mriydte, Lt. moritur, pIE *mer-. See also uvdmarsiyu-, marika-, maria-, martiya-. amarijalü imf. mid. (835.1, $285.II) DB 1.43.
5776:marika- sb. ‘person of lower rank, subject’, as shown by АКК. *"gal-la ‘menial’: contracted ($23.1) for *mariyaka-, deriv. of stem in Skt. (Vedic) márya- ‘young man, stallion’, ef. Skt. maryakd- ‘little man (said of a bull among cows)’, Phi. mérak (from *maryaka), Gk. шера ‘boy, girl’ (from *merjak-); ultimate root pIE *mer-, OP mar- (5122, 5146.11). Cf. Hz. ApI 251-3, Bv. TPS 1945.43-4. татка узш. DNb 50, 55, 59°.
=== KNT apiy ===
665:The emphatic adverb apiy is sometimes at- tached to the preceding as an enclitic, and some- times separated from it by a divider. The en- chtie pronoun diš is preceded by a divider in DB 4.34, 35, 36. At DB 5.11, wa : Чаш : marda is probably to be emended to wa : viyamarda, with wrongly inserted divider? other peculiarities in connection with enclitics are given in §133.
708:Cf. also the sandhi phenomena of düraiapiy DNa 12, dürayapiy DNa 46, and the same as two words, diraty ариу.
737:П. The -1- may be omitted in final -aiy: | Auramazda-tay DB 4.58, for -іату. mantyahay DPe 20, for -haty. ula-may A’Sde 4, for uta-maty (which is in db). Cf. forms of düraiy, with enclitic apiy (5186).
1638:$133. Encursis is a frequent phenomenon in OP. The enclities are the following: Pronouns: Ist sg. асе. -md, gen. -maty, abl. -ma. 2d sg. gen. -taiy. За sg. acc. -йт, gen. -Saiy, abl. -$a; pl. acc. -&$, gen. -Sàm. acc. -dum; pl. acc. -di$. pl. aec. -àà (dubious; only in avabasa-lé DB 4.72), Coordinating conjunctions: -eà ‘and’, -vë ‘or’. Postpositions: d, patiy; both also as separate words before or after their nouns. Adverbs and particles: -am, -kavy, -ciy, -dty, never separately. -apiy, -paliy both also separately. Miscellaneous: уа in mátya DB 4.43, 48, 71; yadatya XPh 35f (miswritten yadàya XPh 39), cf. yada : tya XPh 29. müm, elsewhere orthotone, in mātyamäm DB 1.52. rádiy in avahya-radiy DB 1.6f, etc.; also separ- ately. Double enclisis: mé-tya-mém DB 1.52; rauca- pati-vd,, DB .1:207 aatpati-mé DNb 20; avā-
1655:düraiy + арту, which is most often two words, appears as duraiapiy, without the y, and also as dürayapiy, showing the development of
1674:$139. CONTRACTION or VOWELS IN SANDHI is to be expeeted in combination with enclities, but the situations which produce it rarely oceur in ОР; there is one probable instance, vaina[pi]y XPz 71, for vasnd + apiy.
2269:Ending in -ї: apiy (also enclitic), uparty, -diy, patiy (also enclitic).
3068:$311. Tur Position оғ Encurric Wonps, The enclitics of OP may be divided into four groups: (1) pronominal forms -mazy -mā -ma, -taty, -Sary -šim -Sim -S8, -dim -dik; (2) adv. рабу, conj. tya; (3) conjj. -cd, -vd, айуу. apiy -ciy -diy; (4) postpositions (see §133 for others in fixed com- binations; §134-§139 for phonetic phenomena).
3071:тё-шв DB 1.52, 4.43, 48, 71, рану in ima pati- maiy DNb 32f despite nai-pati-mà DNb 20. Regu- lar orthotone mdm is written with the preceding in md-tya-mam DB 1.52. On adv. patiy, see П; on apiy, see III; on the postpositions, see IV.
4103:Tux Inscriptions or NaAQS-1-RugTAM. DNa = Darius, Nags-1-RustaMm A. 1 baga : vazraka : Auramazda : һуа : im 2 ām :bümtm :adà : hya : avam : asm 9 апат :adà : һуа : martiyam :adà : h 4 ya : Siyatim :adā : martiyahyà 5 :hya : D&rayavaum :xšāyaðiyam : ak 6 unau$ : aivam : parüvnàm : xSdyaé 7 iyam :aivam : parüvnàm : framátà 8 ram : adam : DarayavauS : xsayatiya : va 9 zraka : xSàyafiya : xSdyafiyanim 10 : xSdyaiya : dahyünàm : vispazaná 11 nam : х$йуайуа :abyáyà : шт ` 12 уа :уалаКауй : diiraiapiyf: Vistas 13 pahyà : puça : Haximanisiya : Parsa : P 14 àrsahyà : риса : Ariya : Ariya : ei 15 с̧а :0atiy : Darayavaus : xsaya 16 fiya : vašnā : Auramazdaha : ima : 17 dahyáva : {уй : adam : agarbáyam : 18 apataram : haeà : Ратѕа : adamsàm : 19 patiyaxSayaiy : manā : bàjim : abara 20 ha : tyasàm : hacdma :afahya :ava : a 21 kunava : dàtam : tya : mani : avadis : 22 adaraiya : Mada : Uvja : Parfava : Harai 23 va : Bàxtri$ : Suguda : Üvürazm 24 i$ : Zraka : Harauvatis : Gatagus : Ga 25 dara : Hidug : Saki : haumavargà : Sa 26 kā : tigraxaudà : Bābiruš : A 27 Gura : Arabàya : Mudràya : Armina
4105:28 : Katpatuka : Sparda : Yauna : бака : {уау : pa 29 radraya :Skudra : Yauna : takabarà : Рибу 30 à : Каўуя : Maciya : Karka : дану : D 31 drayavaus : xšāyaðiya : Auramazda : ya 32 & : avaina : imàm : bümim : yaudatem : 33 pasávadim : manā : frábara : mam : 28d 34 уадуат :akunaus : adam : x&àyatiya 85 :amiy.:.vasnd : Auramazdahd : a 30 damSim : gafava : niyašādayam : tyašā 37 m : adam : afaham : ava : akunava : yabā : mam: 38 Ката : aha : yadipatiy : maniyáhaty : t 39 ya :ciyakaram.: dha : ava : dahyiva 40 :tyà : Darayavaus : xSayafiya 4] :adáraya : patikarà : didiy : tyaiy : g 42 àfum : baratiy : vadā : xSnasahy : 43 adataiy : azdà : bavatiy : Pārsahyā : 44 martiyahyà : diraiy : artes : pa 45 ràgmatà : adataiy : azdà : bavāti 46 y :Parsa :martiya : dürayapiy : hacà : Pa 47 rsà : partaram : patiyajata : 6itiy : Da 48 rayavauS : xSdyafiya : aita : буа : karta 49 m :ava :visam : vasnà : Auramazdaha : ak 50 unavam : Àuramazdá(ma)iy : upastàm : aba 51 ra : yütà : kartam : akunavam : mém:A 52 uramazdà : pàtuv : аса : gasid : utama 53 iy : vitam : uta : imàm : dahyàum : aita : ada 54 m : Auramazdam : jadiyámiy : aitama 55 iy : Auramazda : dadatuv : 56 martiya : hyà : Auramazdah 57 & : framana : hauvtaty : gas 58 tā : ma : adaya : раб : .. 50 {уаш : ristim : mà 60 : avarada : mà : stabava Nores то DNa: The text of DNa now rests upon the photographs of F. Stolze (Persepolis: Berlin, 1882) and of А. Sevruguin (accessible in Wb. Grab, Plates 2-3). The following readings, which either replace older wrong readings or confirm older doubted readings, are assured by the photographs; the restorations agree with the length of the gaps: ^? framatà- | ram; ™ düraiapty; 9 patiyazsayaty; 9^? aba[ra]- | ha; * adáraiya (for nor- malization, ef. $48); 25 haumavargá ; * akunava; * yadi- patiy : maniy|ühaty : t]- | ya (for -haiy, cf. note on DB 4.39); * {aha} Wb.; “ no space for [mand] before ga6um; £ a[va]dà; **düraiy; 4 dárayapiy; ® Auramazda(ma)ty, with omission of те; 6 ga(sta], see Lex. s.v. (not sero+). Other textual notes: 3° [ра]- | radraya, after other oc- currences, see Lex. s.v.; not [ta]- | radraya. *^* Put- (älyä, after other occurrences, see Lex. svt; not Put[i]yà. 2 yauldatim] ВЕ, sée Lex: ву. yaud-; hardly yaufdinim],
4214:DSe = Darius, Susa Е. 1 baga : vazraka : Auramazdà : hya : ima 2 т: bimim : adadé ; һуа : avam : as 3 татат : adadà : hya : martiyam : ad 4 ada : hya : &iyàülim : adad& : mart 5 iyahyü : hya : Darayavaum : XŠm : ak 6 unauš : айбат : parūvnām : XSm : a 7 шат : parüvnüm : framálàram : a 8 dam : Darayavaus : XS : vazraka : XS : XSy 9 anim : XS : dahyünám : vispazanü 10 nam : XS : ahyaya : bümiyà : vaz 11 rakàyà : düraiy : apiy : Vistas 12 pahyà : puça : HazamaniSya : Рат 13 sa : Pārsahyā : рисо : Ariya : Ari 14 ya : ciga : 08tiy : Dàrayavaus : XS : 15 уа&па : Auramazdaha : imá : dahy 16 āva : {уй : adam : agarbayam : apaia 17 ram : hacd : Parsa : adamsdm : pat 18 iyaxíayaty : manā : bajim : abara : 19 tyasam : hacéma : afahya : ava : aku 20 nava : datam : tya : mand : avadis : a 21 dáraya : Майа: Uja : Parðava : Haraiva : 22 Baatris : Suguda : Uvarazmis 23 : Zrdka : Наташайх : Bataguš : Maci 24 уй : Gadàra : Hidus : Зака : haumava 25 rgà : Saká : tigrazaudà : Babir 26 u$ : Авита : Arabéya : Мийгаа : 27 Armina : Katpatuka : Sparda : Yaun 28 à : аву : drayahya : ula : уа 29 y : paradraya : Skudra : Putayà : 30 Kuxiyd : Karka ; 6àtiy : Рата 31 yavau& : XS : vasiy : tya : duskarta 32 m : Gha : ava : naibam : akunavam : da 33 hyáva : ayauda : aniya : aniyam : 34 aja : ava : adam : akunavam : vašnā 39 : Auramazdaha : уаба : aniya : a 36 шуат : пау : jatiy : cind : gà 37 fava : kaSciy : astiy : дат : 38 tya : maná : haeá : avana : tarsat 39 y : улда : hya : tauviyd : tyam :s 40 kauéim : naiy : jatiy : naiy : vi 41 mardatiy : байу : Dérayavaus :
4401:5 XS : vazraka : XŠ : XSyanam : XŠ : dahyünám : vispazanünàm : XŠ : ahyay 6 à : bümiy& : vazrakáyà : düraiy : apiy : Vistáspahyá : puça : Ha
4424:19 :apiy : Vistaspahy
4447:3 ada : hya : Syátim : ada : martiyahyà : һуа 4 : XSavarSim : xSiyafiyam : akunaué : aivam : 5 parünàm : xSayatiyam : aivam : parünàm : fram 6 àtàram : adam : XSayarsa : xSayafiya : vazraka : 7 xšāyaðiya : хёйуайїуйпаш : x&ayafiya : dahy _ 8 ünàm : paruv : zanànàm : хёйуадіуа : ahyay 9 & : bümlyà : vazrakáyà : düraiy : apiy : Da 10 rayavahaus : x&ayafiyahyà : риса : Haxémanis П iya : 0atiy : Xšayāršā : xšāyaðiya : vasna : 12 Auramazdáhà : imam : duvarfim : visadahyum 13 : adam : akunavam : vasiy : aniyascly : naibam 14 : kartam : апа : Parsi : tya : adam : akunavam : 15 utamaiy : tya : рія : akunaus : tyapatiy : ka 16 riam : vainataly : парага : ava : visam : vaSnà : А 17 uramazdaha : akumà : Qatiy : Xšayāršā : 18 xSayafiya : mam : Auramazda : pātuv : utamai 19 y : xSacam : ut& : tya : manā : kartam : uta : tyamai 20 y : pica : kartam : avaseiy : Auramazda : patuv
4481:XPc = XERXES, PERSEPOLIS C. 1 Бара : vazraka : Auramazda : hya : пойт : bümim : 2 ада : hya : avam : asmànam : ada : һуа : marti 3 yam : ada : һуа : Siyátim ; ada : martiyahyà 4 : һуа : Xšayāršām : XS8m : akunaus : aivam : pa 5 rūnām : XSm : aivam : pariinam : framátàram 6 :adam : XSayarsa : XS : vazraka : XŠ : XSanam : XS: 7 dahyünàm : paruv : zandndm : XS : аһуйуй : b 8 ümiyà : vazrakiya : düraiy : apiy : Darayava 9 haus : XShya : puça : Haxāmanišiya : 6atiy : X 10 šayāršā : XS : vazraka : vašnā : Aurahya Mazdaha : i 11 ma ; hadis : Dárayavaus : XS : akunaus : hya : manā : 12 pità : mim : Auramazda : pátuv : hada : baga 13 ibis : utd : tyamaty : kartam : uta : tyamaiy : 14 pica : Darayavahau’ : XShyá : камат : avaSely 15 : Auramazda : pátuv : hada : bagaibis
4514:18 : düraiy : apiy : DarayavahauS : xš 14 dyafiyahya : риса : Нахатапёуа :
4524:13 aya : düraiy : apiy : Dárayavaha
4648:12 : adam : XSayarsa : x84 18 yafliya : vazraka : x$àyati 14 ya : xšāyaðiyānām : xs 15 ауайтуа : dahyünàm : раг 16 uzanànàm : x Sayafiya : 17 ahiyáyà : bimiya : va 18 zrakáyà : düraiy : apiy 19 : Dárayavahaus : xSayabtya 20 hyà : риса : HaxámaniSiya TRANSLATION ОЕ XE: $1. 1-11. ... (= XPa 1-6). $2. 12-20. ... (2 XPa 6-11).
4656:9 framàátàram : adam : Xšayāršā : 10 x&àyafiya : vazraka : хёдуабуа : 11 xšāyaðiyānām : xšāyaðiya : da 12 hyünàm : paruv : zanànàm : x$ 13 àya8iya : ahy&yà : bümiyà : va 14 zrakày& : düraiy : apiy : Daraya 15 vahaus : xšāyaðiyahyā : риса : Ha 16 x&manisiya :0ütiy : XSayársá 17 : xSayabiya : Dārayavauš : xSiya 18 буа : һуа : manā : pitä : hauv : va 19 502 : Auramazdaha : vasiy : tya : 20 naibam : akunauég : uta : ima : st 21 änam : hauv : niyastdya : katanaiy 22 : yaniy : dipim : naiy : nipist 23 ām : akunaus : pasáva : adam : ni 24 yastéyam : та : dipim : піра 25 iStanaiy : màm : Auramazda : pa 26 tuv : hada : бадафт : utämai 27 y : zSaqam : Ша : атану : kartam
```


## [2026-09-05T20:29:36.055Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '27210,27280p' POK_full.txt"
}
```


### [2026-09-05T20:29:36.105Z] TOOL RESULT

```
Root / lemma: epi, opi, pi 

Meaning: at, by 

Note: (also with lengthened grade -ei, -o/in the final syllable); partially in the meaning with 

abbreviated dd^i, do^i. 

Material: Old Indie api^a\so, in addition' (Adv.), seldom ved. preposition m. locative 'by, in', 

prefix api-, pi- 'to, by' {pi- in pi-dtiana- n. ' covering, cover, lid ', pi-natiyati^ tethered, 

fastened to', py-ul<sna-^ cover of the bow ': gr. TTT-uxn " crease, layer ', if from *ni-uxc(, 

nTuaaoo 'lay, place together, crease ', pTdayati: nis^oj, s. *sed^, common Old Indie gti- > 

ks- 

Avestan aipi, ap. apiy, adnominal 'about - to, by (Akk.), by (temporal, Lok.), after 
(temporal, Instr.)', Adv. 'in addition also, likewise also, particularly, specially, especially, 
particular: in particular, peculiarly, separately, extra, notably; hereafter, later', prefix 'to'; 



with lengthened grade of final syllable Avestan 5/oe 'after' (m. Akk.), compare apaya M\t. " 
hereafter, prospectively ', -yoe emphasizing particle; 

Armenian ei/"and, also'; *pr\'r\ aniaut h- united verbs, as h-agan/m'puW myself to '? 

Gr. sni, sm 'auf to, an', adnominal with dative (= Indo Germanic Lok., Instr., Akk., Gen., 
prefix, EniGGOv to uoTEpov yevopsvov Hes. (i.e. probably ' progeny ', basic form *£ni-Tio-, 
Schuize, Kl. Schr. 70 ff., 675), ni- prefix (see above); op/"\n hom. 6ni-9£(v) "behind, 
afterwards', Ionian Attic 6nia9£(v) ds. (-a- after np6a9£(v), compare also 6TTia(a)u) 
"behind, backwards'; hereafter ' {*opi-tid), oniaraTOc; " hindmost, last'; orr-cbpa "autumn', S. 
343); presumably (with Indo Germanic contraction from *opi-oq"'\.o *opTq", to *c»^"'- "see') 
6ni:-TT£uu) "stare at', TTap9£vonTna " girl gazer, onlooker ', *6ijj (formation as aijj, Latin abs, 
a|j(pi(;, see below Italian ops-) base from 6\^t, Aeolic b\]^\ "late';about gr. £TT-£i "there' see 
above S. 284; 

lllyrian PN Epi-cadus {coru'pare gr. K£Ka5[j£voc; " parading, showing off); Venetic PN 
Opi-tergium {\.o Tergesfe ^Tnest', Old Bulgarian trhgb' marketplace '; alb. tregu' 
marketplace '); Messap'\c pt- do {* do- f) "bore profit'; 

alb. epere' situated above '; lllyrian Epirus{*epi-uerid) " situated above, highland ' : 
£>7^"lrland' {*epi-uerid^ enclosed land, hill, island), cymr. Ywerddon 6s. {*uiuerdon, *epi- 
uerionos) [common lllyrian n > nd > d\. 

Latin Oit* adnominal m. Akk. " prep, with ace, in front of, before; in return for; because of, 
on account of. Old Latin also " around, round about, all around, near together, in close 
proximity ', and prefix from op- before voiced consonant originated (as abiroxxx ap[oJ)\ op 
still in operioirom *op-verid, oportetirom *op-vorteV it is necessary, needful, proper, 
becoming, or reasonable; it behooves; I (thou, he, etc.) must or ought '; about opacuss. 
EM2 703 and above S. 54; *ops- (see above) usually before /-in compound, e.g. o(p)s- 
tenda, Oscan up, op^by' with Abl. (= *lnstr.); 

Old Irish /arn-, /arm-waiter, afterwards, in the next place, secondly ' m. Dat., perhaps 
Neutr. a derivative *e/0/-/'c»-/77(Thurneysen Gr. 516); ep/- seems also obstructed in Old Irish 
fa-da/m' close ' (compare Latin ob-dd), ei-thech^ perjury ' (compare gr. £ni-opK£(jo), Eriu 
"Irland' (^ephuerid^ enclosed land, hill, island) = cymr. Ywerddon6s. {*uiuerdon, *epi- 
uerionos), nir. eibheairb\aze, glow' {* epi-b^elo-); 

op/"\n Old Irish ofbellm. "blaze, glow' = cymr. ufelm. "spark' {*op/-b^e/o-); cymr. uffarn, 
bret. ^/fe/77 "ankle' {opi-spernS); 



Gothic /)%//77a (formation as aftuma'\as\!) " subsequent, later'; ibdaljaxr\. " descent, 
slope'. Old English eofolsian^ blaspheme ' {*eb-halsian), eofut, eofotu. "blame' {*eb-hat)\ 

in addition perhaps also the group "evening': Old Norse aptann, eptann, west-Germanic 
with ^Old English sefenm. n.. Old Saxon aband. Old High German aband, perhaps the
```


## [2026-09-05T20:29:36.775Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"angra\\|aŋra\\|Ahriman\" POK_full.txt | head -20; echo \"=== men-1 lemma ===\"; grep -n \"Root / lemma: men-1\" POK_full.txt | head; "
}
```


### [2026-09-05T20:29:36.871Z] TOOL RESULT

```
5344:gorge' (" curve, canyon, a bay; an inlet ' as to q^koq, = Germanic *angra-)\ 
5357:*angra {up to gender = Latin *ancrae) in Old Norse angr^ bay, curve ' (in local names like 
36669:Avestan za/7^a/77 'ankle of the foot', -zangra-{\n compounds) ds., zero grade Old Indie 
39376:alb. hangra'\ ate' : Armenian eker' ate ' (common Avestan Greek Armenian aorist prefix); 
=== men-1 lemma ===
```


## [2026-09-05T20:29:45.019Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR>27210 && NR<27340 && (/Page\\(s\\)/||/References/)' POK_full.txt; echo \"=== men denken ===\"; grep -n \"menos-\\|Root / lemma: men-\\|mens-\" POK_full.txt | head -20"
}
```


### [2026-09-05T20:29:46.900Z] TOOL RESULT

```
References: WP. I 122 f., Pedersen Lycian and Hittite 23, Schwyzer Gr. Gr. I 325, 550^, 
Page(s): 323-325 
References: WP. I 123 f., Kluge^ S. 689. 
Page(s): 325 
=== men denken ===
61083:Root / lemma: menot. Gen. meneses, from which menes-, mens- mes-, men- 
61092:(conservative Gen. PI. mens-um), menstruus^ monthly ' (GN Mena\s gr. loanword),
```


## [2026-09-05T20:29:50.298Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"^Root / lemma: men\" POK_full.txt | head; echo ---; grep -n \"Page(s): 726\\|Page(s): 726-728\" POK_full.txt | head"
}
```


### [2026-09-05T20:29:50.395Z] TOOL RESULT

```
61083:Root / lemma: menot. Gen. meneses, from which menes-, mens- mes-, men- 
61742:Root / lemma: meni- 
---
59499:Page(s): 726 
59529:Page(s): 726 
59673:Page(s): 726-728
```


## [2026-09-05T20:29:52.811Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '59530,59560p' POK_full.txt; echo \"......\"; sed -n '59600,59675p' POK_full.txt | grep -n -i \"mainyu\\|Avestan\\|meaning\\|lemma\" | head -20"
}
```


### [2026-09-05T20:29:52.886Z] TOOL RESULT

```
Root / lemma: mehn-3 

Meaning: to think, mind; spiritual activity 

Note: extended mehneh-. mnah-ar\6 mneh-, irienei-. mehi- 

Material: Old Indie manyate^ thinks ', Avestan mainyeiteAs., ap. ma/nyahay {\n6o 

Germanic *men-i-o-, = gr. |jaivo|jai " bucket, careen, fly, travel at a reckless speed ', Old 

Irish -muiniur, Slavic mbnjg^ mean, indicate ', see below). Old Indie Perf. ma-mne, mene, 

manay-ati^\s keen, eager', mana-yu-^keeu, eager, godly, pious', manJ-sa^ wisdom, 

reason; devotion, prayer' {*menei-: irienT-); Old Indie manute^ thinks '; manati^ mentions ' 

(= Lithuanian menu, poln. -miong, Czech -menu); Old Indie manayati^ honors ', (: 

Lithuanian /'s-mon/s' reason'), Avestan m^nayen'one could believe'; Supin. Old Indie 

mantum, participle Perf. mata- " thought ' (= gr. auT6-|jaT0c;, Latin commentus, Lithuanian 

mintas. Old Irish derm at); 

from the J-basis (= gr. [jva-): Old Indie mnata-^ mentions '; mnayate' it is mentioned '; 

Old Indie manas-, Avestan manah-n. "sense, mind' (= gr. ijevoO; Old Indie durmanas [= 
bua\\zyr\(^; ap. Haxa-man/s ' Axoi\[Jit\/r\q " von Freundessinn beseelt '; Old Indie manman- 
"sense, mind, thought, notion' (= Old Irish menme); mantar-^t\r\\nker' (= gr. Msviajp, Latin 
commentor); mun/'-m. "the eager, seer (compare pavric;), ascetic'; mantra- m. " religious 
......
1:ze/77s/a "vengeance, revenge' (common Slavic alb. ze- prefix) see Root/ lemma: mei-t(h)-2 
17:(compare Old Prussian mentimai^ we lie', compare z. meaning still commentum' an 
76:Root / lemma: mehn-4
```


## [2026-09-05T20:29:58.566Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== PHD ===\"; grep -n -i \"ahreman\\|ahriman\\|ʾhlmn\" PHD.txt PHD_mackenzie.txt | head -10; echo \"=== NYB ===\"; grep -n -i \"ahriman\\|ahreman\\|Ahrmen\" NYB_vol2_glossary.txt | head -10"
}
```


### [2026-09-05T20:29:58.633Z] TOOL RESULT

```
=== PHD ===
PHD.txt:188:~ih : immortality. ahr Phl] dread, fury. ahrüftan, ahram- P4Pftn', *hm- | M hr’ рїп, ? hr? m-] raise, lead up. Ahreman ['Al(y)mn! | М ?hrmyn, N ~] the Evil Spirit. >
PHD.txt:1815:evil (a.) akēmand, апар, druwand, wad(ag), wattar, duš-; ~ deed dušxwaršt; ~ eye aš, dujdoys?rih; ~ rule dušpādixšāyīh; ~ ruler dušpādixšā(y); — speech dušēwāz- ih, dušhüxt; — spirit Ahreman, gannág mēnēg; ~ thought duš(hu)- mat; of ~ behaviour duškunišn; of — religion agdén, dujdén; of — speech duš-gēwišn; of — thought dušmenišn.
PHD.txt:4387:Ahreman Akóman Arzür Astwihad
PHD_mackenzie.txt:958: Ahreman ['hl(y)mn l 1M 'hrmyn,     '      N.....,] the Evil Spirit.
PHD_mackenzie.txt:6526:    ih, dushuxt;          spirit Ahreman,          eye caSm, doysar ; evil ......        as,
PHD_mackenzie.txt:8026:Ahreman                      Jeh
PHD_mackenzie.txt:12346:axtarmlir          ~~tbuI           Ahreman
=== NYB ===
319:Ahriman [’hlmn'] 32-34. 62-63. 71 ete. passim. — Av. (104 sg.) angra- mainyu-, anra- mainyu- (angra-, anra- < *ahra-); MPrthPrs ’hrmyn; Arm. lw. Ahrmn; Paz. Aharman; NP Aharman, Ahraman, Ahriman. Cf Bailey, BSOS VII, 1934, 295 sq.
350:akärihistan [~-yhstn'] pass. of the pre- ceding vb.: Ahriman bē akārihēt A. will be incapacitated, powerless 7719-11,
423:anakéh-kamak [~-k?’mk'] evil-intention- ed, malignant, of Ahriman 7724, anākēh-kāmakēh evil intention, malig- nancy, of Hešm 7215,
468:"p: api-š, ”pm’n' or (Ps.) *pmn: api- man, ’pt’n': api-tän, "p$^n! or (Ps.) *pšn: api-ščin: 1. and, introducing and coordi- nating sentences, e.g. andar-rón andar šut api-$ guft 1818-14; coordinating substan- tives if the second subst. is determined by an encl. pron., e. g. zantšn + Ahriman api-š visütakän 8819; also preceded by u: u api-t 6°, u api-š 7822, u api-sdn 79°, etc. — 2. introducing the apodosis after ka 94. 1025, 5225-27, 5418; after cigon 931; after an isolated w. having the character of a protasis: hämöden api-š hàn zan... ayyāt būt all this [to supply: engaging his attention], the remembrance of that woman came upon him 11'!-!*; — taking up the sentence again after a preceding digression: han zan u hàn fradand 1-8... api-man ne özat 1212-3. — Av. (82 sg.) aipi, OP apiy ‘moreover, further’, both encl. and often only emphasizing: OP düraiy apiy (and other spellings) ‘very far’; surviving in Milr -p(?), g. v. Along with it there must have existed a fully stressed form "dpi; id.-europ. "dpi (Gr postp. Ézt, prep. èni), whence the gen- uine Arm. eu ‘and’; it is the counterpart of Gr ču, Lat et (eti-am). This "dpi > Milr ap, in the sense of ‘and’ and in the apodosis, is normally used in the Sassa- nian official language as the bearer of encl. pronouns beginning the sentence, but in fact occasionally occurs alone, as in the Ps. (several instances, v. Gloss.); PR 231.14, 347. 404; PhlY 31! (intro- ducing the apodosis). Apparently it was counted among the archaisms which need- ed explanation, because it was included in the FrP (ch. 24). Paz. has preserved some remnants of the archaic form: awam = api-m SGV VII, 22, awama = api-mān ibd. VI, 47. X, 28. 35; Paz. AV, ed. Antiā, Päz. texts 35818; hawasq = api- gan SGV V, 62, etc.; the Paz. forms reg- ularly occurring may be shortened allegro forms of api-m ete., v.s.v. u. The equi- valents of api-m etc. given by the FrP are wm, wt, wš, which seem to coincide
491:?apak [LWTH] 1. a) adv. together: (ka- nicak virtual dat.) andar ham Sap ~ bit in that same night he was together with the girl 16!-?; referring back to an encl. pron.: sih (restore the reading “30”, v. 28th) 4-$ ~ pat asp which was with him on the horse 8? (v.s.v. i and ef andar); Sih-& ... —-aš pat asp nišast estat 89: as prepositions do not govern an encl. pron. ~ must be the adv., and -aš refer to the following pat asp or to the whole sentence. — b) prep. together with, with, in all its senses, passim; in spite of 118; ~ man 5?*; ~ amäh 19, ~ smäh 1918, ~ disin 82; ēvak ~ dit with each other 7818. 799. 1071, — 2. adj. prostrate, knocked down, lying on one’s back: čvak apar, ~ dit, apar ēstūt hend o en kar they set about this act (making coition), the one above, the other lying on her back 4314-4; ka Ahriman ~ A. being knocked down (lying senseless) 914 (the enel. -4 after ~ belongs to the following, taking up the preceding subj. Ohurmazd which begins the period), a wordplay — not understood by the Pazandist — with — hämöden yazdan u amahraspandän |. 5—6, the first
534:apa-sistan ['psstn'] apčsistan [’pysstn'] apa-sih- ['psh-, *psyh-] or apésih- ['py- syh-], to be destroyed, annihilated: bē apasihet will be annihilated, of Ahriman 644, of the wicked 103! (in both passages ’pshyt' in the printed editions); — bē apäyet apesihät (subju. 3d p. sg.) vis ? Pourusäsp the manor of P. (must be =) is evidently going to be destroyed 441°; nē be apesistan <i> vis 1 Pourušāsp rād not in order that the manor of P. might be destroyed 4421. My spellings apasihät, apasistan in Dk are to be corrected; the scribe of the Dk MS (now available in re- production) constantly writes all forms of this vb. and its derivatives ’pys-, keeping the two letters y and s distinct with a care not very common in Phl. writing (in 441° he wrote by a slight slip of pen ’p’s- instead of ’pys-). The form apēsīhāt 441° is directly confirmed by MPrs ’bysyh’d (S). — < apa- + Av. (1547) saéd-, pres. pass. "apa-sidyati > Milr *apa-siy-é > apa-sihet or apa-styy-ēt > apa-siyét > apasthét; Paz. awasihed, awasthend; M Prth ?bsyst ‘dried’, Ghilain 83. The form with -ē-: apésihét etc. goes back to *apa- hisidyatt with pres. reduplication (cf Av. ava-hisióyat which is, however, perf. opt.). The active pres. ‘to destroy’ was *apa- sind- > apa-sinn- (always spelt ’psyn-): apa-sinnčt, apa-sinnisn (Paz. awa-sinasn) ; from this are formed the secondary infini- tives apa-sinnitan (BdJ 15%, apésinni- tan (Mx 2771), apasinnistan (KnA 79). Bal sinday ‘to break’, Skr chid- (< Id.- = europ. aci pres. chinad-, chind- (Lat.
802:collected and the members of his family acquired — (when it) is lost and gone PT 16613-15; — common theological term ex- pressing the nothingness of Ahriman and the evil powers, especially from an escha- tological point of view: ~ -éh $ Ganäk menči DkM 852, v. also ~ -büteh; andar višuft- A hrimaneh, ~-druzéh), apasihit deveh u nést-paitiyarakéh in a state where Ahriman has been destroyed, the drugs defeated, the devs annihilated, and there are no adversaries DD 798-?; den. vb. avinnitan [>wbynytn']: opt. avinnēš DkM 83811; avinnitäreh DD 7514; avinnenitan, pass. avinnihistan ibd. 765-5; etc.]. — Paz. avin, Skr v. an-upakärin ‘doing no service, useless, fruitless’ (Mx), vikala ‘defective, impaired’ (SGV). FrP ch. 25 gives full evidence as to sense and etymology of this w.: "wbyn'. ’yen. L'YT'.nyst'. heš. heyš (var. hes!, ?zy$), Paz. óbin (K öbin). ēzin (var. aizin, Arab letters ’zyn, ’yzn) rwid nist aziš (var. ajiš), the lemma being: ^wbyn': écin (LYT' =) nast haciš; com- mentary: — l. &in < *atva-cina ‘even one thing’, with neg. ‘no one thing, nothing at all’: Av. (594) -cina encl. emphasizing part. in neg. sentences, (595) cina- ‘whoever’, (595, 762) dväcina ‘two men whoever they may be’, (24) aēvā- cina in obscure context ;. 2. L“YT' glossed by nēst, and ambiguous keš elucidated; 3. the lemma says: *wbyn' means: ‘no one thing comes from it, there is no gain from it’. The reading is almost self-evi- dent: a-vinn <  "a-vinda- from Av. (1318 sqq.) *vaéd- ‘to find, to acquire, to share, to gain’, thus ‘not gaining’; also representing Av. (348) o-vindan- ‘left without any share' (of the food, of dogs Vd. 1378). As to the assimilation of -nd- > -nn-, common in SW, cf MPrs bn = bann < band; BP apa-sinn- (v. s. v. apa- sistan), nivinn- < ni-vind- (g. v.). — This etymology was already given in HP II, and I maintain it firmly. The most un- happy idea of Geiger (WZKM XL, 107), taking ^wbyn as an Aram. ideogr. and
855:ayyastan ['dybstn'] to long for, to yearn for: i ka-t 6 včnišn 1 Ahriman . . . ayyast since thou hadst (such a) longing to see A. 76?, impers. constr., cf Lat. tibi lubuit; — [pres. ayyds- DkM 4837-8 Cod.
1174:dak [d^k'], v. hu-däk, kār-dāk, véh-dak. dälman [d'lmn'] a raptorial bird, prob- ably the vulture 942128, — < *darnu- mani-, SW form of Av. (1683) zaranu- mani-, an epithet of the kahrkasa, v. karkas. — Phl. Vd. in à commentary on T? has ~ with the NP gl. bim ‘owl’. — NP dalman. V. Bailey, ZP 137 n. 2. dam [d’m] creation, preferably referred to Ohurmazd, but also to Ahriman: created being 637; — coll. the created beings, the created world 31?! and passim ; ~ u dahišn, v. dahišn; — pl. cas. obl. ~-ãn 7319. 7624. 7716, 7917. 8012, 8922-28, 10215. — From dà-, v. datan; Av. (736) dämi-; MPrthPrs d?m; Paz. dam, Skr. v. srsti; NP dam of animals.
1361:druvand [dlwnd] wicked, evil, of Ahriman 642-7 and passim; of human beings 10°. 3414, 6625, 964. 10711 — subst. 7213, 7417, pl. eas. obl. —-än 461, 5313, 7220, 7421, 75°. 10226, 10322, used as cas. rect. 10114-18, — Av. (774 sqq.) dragvant-, drvant- ‘be- longing to the drug' (v. druž); MPrs drwnd (S, A-H II); Paz. daruand, dar- vand.
```


## [2026-09-05T20:29:59.570Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== HRN ===\"; grep -n -i \"ahriman\\|ahrman\" HRN.txt | head -10; echo \"=== HUB ===\"; grep -n -i \"ahriman\\|ahrman\" HUB.txt | head -10"
}
```


### [2026-09-05T20:29:59.646Z] TOOL RESULT

```
=== HRN ===
10703:126. 'fvafstar 'schädliches, ahrimanisches Getier.
=== HUB ===
7787:man J Ahrman (bei Fird.), phi. Ahf'tnan^ Ahr{d)man u. s. w.,^ 219 —
```


## [2026-09-05T20:30:15.347Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/leaf.py <<'EOF'\nimport sys\nf=sys.argv[1]; \nlines=open(f,encoding='utf-8',errors='replace').read().split('\\n')\nfor ln in sys.argv[2:]:\n    ln=int(ln)\n    txt='\\n'.join(lines[:ln])\n    print(f, 'line',ln,'-> 0-based leaf', txt.count('\\f'))\nEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/leaf.py data/verification/sources/refs/PHD.txt 188\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/leaf.py data/verification/sources/refs/NYB_vol2_glossary.txt 319 468\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/leaf.py data/verification/sources/refs/HUB.txt 7787\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/leaf.py data/verification/sources/refs/KNT.txt 5050"
}
```


## [2026-09-05T20:30:15.936Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '7780,7795p' HUB.txt"
}
```


### [2026-09-05T20:30:17.220Z] TOOL RESULT

```
data/verification/sources/refs/PHD.txt line 188 -> 0-based leaf 28
data/verification/sources/refs/NYB_vol2_glossary.txt line 319 -> 0-based leaf 20
data/verification/sources/refs/NYB_vol2_glossary.txt line 468 -> 0-based leaf 28
data/verification/sources/refs/HUB.txt line 7787 -> 0-based leaf 229
data/verification/sources/refs/KNT.txt line 5050 -> 0-based leaf 192
```


### [2026-09-05T20:30:17.257Z] TOOL RESULT

```
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
II, p. 6), phi. Frasiydk (Phi. Min. 25, 14) = zd. franrasyanem
(ace.) ist entstellt. Man soUte *Afrara8yan erwarten.
c) Idg. ns (= ap. nh ?) - np. ng : dial, mang *Mond* =
iran. *mawAa- = idg. ^mEns- (neben np. mdh = ap. mah- oder
maha- = idg. *wa5«-, siehe oben p. 97). Vgl. zd. saAha-
```


## [2026-09-05T20:30:28.092Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==193' KNT.txt | head -5; echo \"....\"; awk 'BEGIN{RS=\"\\f\"} NR==193' KNT.txt | tail -3"
}
```


## [2026-09-05T20:30:29.952Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== MON اهریمن ===\"; grep -n \"اهریمن\" MON_part1.txt MON_part2.txt | head -5; echo \"=== MON سکوبا ===\"; grep -n \"سکوبا\" MON_part1.txt MON_part2.txt incoming/MON/*djvu.txt | head -5; echo \"=== MON اسقف ===\"; grep -n \"اسقف\" MON_part1.txt MON_part2.txt | head -5"
}
```


### [2026-09-05T20:30:33.499Z] TOOL RESULT

```
-, GAv. angra-, LAv. apra- ‘hostile, enemy’, to рАт. root *ans-, seen in Av. qsta- ‘hate, enmity’; ef. also Av. (nom.) avrd mainyus ‘evil spirit, Ahriman’ (Bthl. AiW 189); not to Skt. art- ‘en- emy’ (MB Gr. §273), nor to Skt. alikd- (Wacker- nagel, KZ 59.28-9). алка nsm. DB 1.22, 33; 4.63. ага npm. DB 5.15°, 31°.
Ariya- adj. ‘Aryan’ (perhaps Ariya-, §126): Ау. atrya-, Skt. drya- ‘noble’, cf. NPers. ёгт ‘Iran, Persia’, Irish Eire ‘Ireland’, to pIE root *er-, OP ar- (585.1, §144.1). See also Ariyacica-, Artydramna-. Ariya паш. DNa 14; DSe 13; XPh 18. ariyd isn. as sb. ‘in Aryan (language) DB 4.89.
Ariyacica- adj. ‘of Aryan lincage’ (5161.18): Ariya- + ciga-. Artyacica пет. XPh 13; Ariya cica (written as two words, $44) DNa 14f, DSe 18f.
Ariydramna- sb. ‘Ariaramnes’, great-grand- father of Darius: Elam. har-ri-ia-ra-wm-na, АКК. ar-ja-ra-am-na-', Gk. 'Ариараштѕ. From ariya- + pass. pte. of d-ram- (8131; Av. Skt. ram- ‘to be at peace, to pacify’): ‘Having the Aryans at peace’ (8161.]1c). Hardly Ariyà pl. + ramna- (Foy, KZ 35.9), or Ariya- + aramna- pres. pte. mid. to ar- (Hz. Ар! 287). Anydramna nsm. AmH 1, 4, 9; DB 1.5; DBa 7; as gsm. AsH 3 ($313.1). Ariydramnahyé gsm. DB 1.5; DBa 7.
aruvü- sb. ‘action’ (JNES 444, 52; 53511, $150; so also Bv. TPS 1945.42-3): fem. to adj. arwa-, Av. aurva- ‘schnell, tapfer’ (Bthl. AiW 200), doublet to Av. aurvant- (q.v., under aru- vasta-).  aruváyà \sf. DNb 38 (inscribed afuvayá, $55.11; not anwasa with Wb. Grab 28, KIA 94;
....
Arza- sb. ‘Arkha’, an Armenian rebel (531, $164.V): Elam. ha-rak-ga, АКК. a-ra-hu. Атта nsm. DB 3.78, 91°; 4.28f; DBil. Arzam asm. DB 3.82, 89.
arjana- sb. ‘ornamentation’, as shown by АКК. : si-im-ma-nu-u ‘decoration’ (§84, §126, 8147.1): for meaning, see JAOS 51.208, 53.13, 53.19, Schaeder, Arch. Anz. 47.272-4, against Hz.’s ‘lime- stone’ (AMI 3.52-3) and ‘building material’ (ApI 88-93). Cf. Av. pres. arga- ‘be worth’, Skt. árhati, and Ars. РЫ, arzün, NPers. arzün, Av. arojah- ‘worth, value’, Skt. argha-. — arjanam nsn. DSI 41f; arjanam-Sary DSf 23°.
arta- sb. ‘Law, Justice’, an archangel attend- ing Ahuramazda: pte. to ar- as sb., Av. aša- and arata-, Skt. rid- ‘cosmic order’, Lt. ortus -‘risen, originated’, pIE *rto- ($30, $66, 5242.1). See also Artaxsaca-, arlavan-, Artavardiya-. ^ arid-cà isn. (8252.1, Lg. 21.223-9) XPh 41, 50f, 531 (not with Hartmann, OLZ 40.145-60; nor with Nyberg, Rel. 367, 478; Bailey ap. Nyberg, Rel. 478; Henning, TPS 1944.108; hardly, with Sen 155, artäcã braz- maniy apn. ‘and the divine fulfillments’; nor with Pisani, Riv. Stud. Or. 19.85-8, as elliptic dual ‘Arta and Brazman’, the -cé connecting with the preceding Auramazdém, and Brazman being the OP for the Av. vohü man ‘Good Though
```


### [2026-09-05T20:30:33.603Z] TOOL RESULT

```
=== MON اهریمن ===
MON_part1.txt:18979:اهریمن: «مصنه [ ِِ ۳ و ِ 
MON_part1.txt:18984:از پیروان اهریمن؛ هر فرد از شیاطین؛ ج. 
MON_part1.txt:19731:شمال آمده و جایگاه اهریمن و دیوان و 
MON_part1.txt:29429:آمده؛ مخلوق اهریمنی» دیو. آفت» بلاه 
MON_part1.txt:30348:طریقت. جای» محل» ۳ پردة اهریمنی: 
=== MON سکوبا ===
=== MON اسقف ===
MON_part2.txt:12666:روحانی سیحی بین اسقف و شماس. کاهن؛ 
MON_part2.txt:17027:کاتولیی: :7:01 (ص.) یشوای اسقفان. 
MON_part1.txt:12885:اسقف: ۲ (معر. وکیل] (.) درجه‌ای از 
MON_part1.txt:97597:عصای اسقف» عصایی که در تفرج بدست
```


## [2026-09-05T20:30:37.650Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== اسقف ===\"; sed -n '12880,12900p' MON_part1.txt; echo \"=== اهریمن ===\"; sed -n '18970,18995p' MON_part1.txt"
}
```


### [2026-09-05T20:30:37.731Z] TOOL RESULT

```
=== اسقف ===

اسسقاط: .5 [ع.] (مسصم.) انکندن 
انداختن. حذف کردن. (امص.) فرسودگی. 
(ص.) (تد.) هر چیز کهنه و مندرس. 
اسقام: ری [ع.] (مصم.) بیمار کردن. 
اسقف: ۲ (معر. وکیل] (.) درجه‌ای از 
درجات آیین مسیح که پایین تر از «مطران» و 
بالاتر از کشیش است؛ ج. اساقفه. 
اتتگسارت؛ اقاته (ع.] (مصم.) خاموش 
کردن» زبان بستن. 

اسکاف: تقامه [ع.] (ص.) کفشگر» 
کفشدوز. 

اسکان: مه [ع. (مص م.) سا کن کردن. 
خانه‌نشین کردن. 

اسکدار: 22۲ [لهجه‌ای از اسکدار و 
معر.] (ص‌مر. امر.) بیکك سوار» پیکك بیاده. 
خریطه و کیسة پیک‌ها که نام‌ها را در آن 
گذارند. بایگاه و منزل پیک‌ها. 
=== اهریمن ===

است که حول محوری (بنام محور اتکاء) 


۳۳۳۳ تا 
کمتری می‌توان اجسام سنگینی را به حرکت 


در آورد. 
اهریمن: «مصنه [ ِِ ۳ و ِ 
آهرامن - آهرمن - و - هریمه» خرد 


خبیت» عقل پلید] (.) (اخ.) شیطان. هر یک 
از پیروان اهریمن؛ هر فرد از شیاطین؛ ج. 
اهر پمنان. 
اهل: 2 [ع.] (.) خاندان. مردم. باشنده» 
بم» ساکن. زن. سزاوار» شاسته. نجیب» 
اصیل. امت هر د بیغمر: اهل موسی» امل 
عبسی) فیس ات آفا وج 
امسلاک: 0 ([ع.] (مسصم.) نیست 
گردانیدن» نابود کردن» هلاک کردن. 
اهلی: ۲1« [ع. ف.] (ص‌نسب.) منسوب به 
ال جانوری که به انسان و خانة وی انس 
گیرد (از چهارپا و پرنده). 
اهلیت: :20-7 [ع. اهلية] (مسص‌جه.)
```


## [2026-09-05T20:30:48.145Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for w in سکوبا اسقف اهریمن آهرمن; do echo \"=== FSF $w ===\"; grep -n \"$w\" FSF_pages.txt | head -5; done"
}
```


## [2026-09-05T20:30:48.399Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== TAD اسقف ===\"; grep -n \"سقف\\|أسقف\" TAD_pages.txt | head -10"
}
```


### [2026-09-05T20:30:49.910Z] TOOL RESULT

```
=== FSF سکوبا ===
2327:                ‫‪- 5000510‬پارسی‪ :‬سکوبا‪:‬‬                ‫باشد» (صحاج) «معتمد و امین»‬
3068:                                                           ‫سکوبا بدو گفت کای نامدار‬
5188:‫سکوبا و بطریق و هر مهتری‬
15225:                               ‫سسخ‬‫به‬                                        ‫سکوبا (با پیش اول)‬
15230:‫ص ‪ ۲۲‬چنین می‌نویسد‪« :‬آنچه معتقد‬                   ‫سکوبا و بطریق و هر مهتری‬
=== FSF اسقف ===
2328:         ‫به اسقف چنین گفت کای دستگیر‬                              ‫(جهانگیری ‪-‬رشیدی ‪-‬برهان)‪:‬‬
2371:           ‫از ناصر خسرو (دیوان ‪:)۲۳۳-۳‬‬                ‫اسقف (باپیش اول و سوم و سکون دوم) س=قف‬
12744: ‫(‪)۶-۸۷۲-۳۱۰۰۱‬‬                                         ‫به اسقف چنین گفت کای دستگیر‬
15223: ‫«سگزی‪ ,‬یعنی سیستانی‪ .‬چه مردم سیستان‬                                ‫به وا اسقف نگاه کنید‪.‬‬
15227:‫در تاریخ سیستان بارها از «سجستان» که‬              ‫ان سقف اسقف» لاتینی ‪ 50۲0050‬به‬
=== FSF اهریمن ===
701:‫اهریمن به خوالیگری نزد ضحاک می‌آید‪:‬‬                  ‫نشستند‬     ‫وردن‬
2181:‫اهریمن به ضحاک می‌آموزد که پدر را‬
3204:                           ‫از هز‬                     ‫ز بد بسته شد دست اهریمنی‬
5363:‫ضحاک بااهریمن پیمان بسته و سوگند یاد‬                            ‫به ناکام می‌رفت باید ز دهر‬
5365:‫اهریمن به ضحاک می‌گوید پدرت را‬                         ‫(‪)۴-۶۲۱-۲۶۱‬‬
=== FSF آهرمن ===
838: ‫دلش شوه جان آهرمنست‬                             ‫‪-۲‬در ترکیب ب‪+‬آرزو‪ :‬بنابرمیلو دلخواه‪:‬‬
1729:‫از آهنجیدن ‏ آهنگیدن به معنی آهیختن‪.‬‬           ‫از آهرمن بدکنش دادخحواست‬
4348:‫نه از ادم از تخم آهرمنی‬                                                         ‫رفته‌اند گوید‪:‬‬
4349: ‫(مه‪)۰۳۰۲۳۴۲۱‬‬                                                        ‫دلش را بپیچید آهرمنا‬
8286: ‫(تاریخ سیستان ‪ :)۵۷۱‬پس حمزه به تاحتن‬           ‫بسایدت سوهان آهرمنی‬
```


### [2026-09-05T20:30:49.959Z] TOOL RESULT

```
=== TAD اسقف ===
128:                ‫لفل ونان قلطء دمع معنأه ولابة الاسقف ورعمته‬            ‫‪١‬‬
1015:  ‫معناه اسقف‬          ‫م‪0‬‬‫وثاني ‪5‬‬         ‫خوري اسيف و‪3‬خوريسمبوس ‪-‬‬
1019: ‫لان خوري اسقفيكا تكتبه العامةيكونمعناه قربة الاسقف تأمل وهو في الاصل‬
1020:                      ‫م راكب من ‪3503‬اع أي قربة وصفع ومن ‪50501‬ؤوأمع أي سقف‬
1564: ‫الارامية ‪ 2‬س إبدا ‪ 4‬أى وضع اليد ومعنى ذلك ان الاسقف بععي فلانا الدرجة‬
```


## [2026-09-05T20:30:57.723Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/leaf.py data/verification/sources/refs/FSF_pages.txt 2327 2371 15225 15227 5188 1729\ncd data/verification/sources/refs; grep -n \"\\[pdf page\" FSF_pages.txt | head -3"
}
```


### [2026-09-05T20:30:59.538Z] TOOL RESULT

```
data/verification/sources/refs/FSF_pages.txt line 2327 -> 0-based leaf 54
data/verification/sources/refs/FSF_pages.txt line 2371 -> 0-based leaf 54
data/verification/sources/refs/FSF_pages.txt line 15225 -> 0-based leaf 306
data/verification/sources/refs/FSF_pages.txt line 15227 -> 0-based leaf 306
data/verification/sources/refs/FSF_pages.txt line 5188 -> 0-based leaf 109
data/verification/sources/refs/FSF_pages.txt line 1729 -> 0-based leaf 43
```


## [2026-09-05T20:31:02.030Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"##### leaf 54 (اسقف)\"; awk 'BEGIN{RS=\"\\f\"} NR==55' FSF_pages.txt; echo \"##### leaf 306 (سکوبا)\"; awk 'BEGIN{RS=\"\\f\"} NR==307' FSF_pages.txt"
}
```


### [2026-09-05T20:31:03.838Z] TOOL RESULT

```
##### leaf 54 (اسقف)
 ‫اشنان‬                                          ‫‪۵۱‬‬


                   ‫(با پیش اول و دوم ‪-‬تازی)‬          ‫گمارند و او را استوار گویند و اینشغل را‬
‫یی ‪ :‬لانیش‬        ‫در این‬     ‫بشو ان مده‬                 ‫یسشن‬
                                                           ‫رانح‬
                                                              ‫وو‬‫یند‬
                                                                  ‫اغو ا‬
                                                                      ‫رای‬
                                                                        ‫اور‬
                                                                          ‫تی‬
                ‫‪- 5000510‬پارسی‪ :‬سکوبا‪:‬‬                ‫باشد» (صحاج) «معتمد و امین»‬
         ‫به اسقف چنین گفت کای دستگیر‬                              ‫(جهانگیری ‪-‬رشیدی ‪-‬برهان)‪:‬‬
 ‫ز ایسران یکی نامجویم دبسیر‬                                       ‫فرستاد بااو یکی استوار‬
 ‫(‪)۶-۷۱-۴۵۱‬‬                                            ‫یک آن کسووار‬    ‫زندبه‬
                                                                           ‫نیوا‬
                                                                              ‫زا‬
         ‫سقف گفت کاین نیست کاریگران‬                   ‫‏(‪٩‬رویز ‪)۹۱۴۱‬‬
                                                                 ‫پ‬
 ‫که پیش از تو بودند چندی سران‬                        ‫مهندس رومی برای خسرو پرویز کاخ‬
 ‫(‪)۶-۳۲-۶۵۲‬‬                                          ‫نوی بنا نهاده ولی برای ساختن ایوان به‬
                                       ‫اشتاب‬          ‫خسرو می‌گوید شتاب نکن چون ممکن‬
                                    ‫شتات‪:‬‬            ‫است ایوان فرو ریزد‪ .‬خسرو شتاب دارد‬

           ‫کاهین باره را نیست پایاب اوی‬              ‫و گفتة او را نمی‌پذیرد‪ .‬مهندس چهار سال‬
‫اوی‬      ‫شرتاب‬
             ‫درنگی شزوداشی‬                           ‫ناپدید می‌شود‪ .‬وقتی نزد خسرو می‌آید‬
 ‫(‪)۲-۲۹۱-۶۹۲‬‬                                         ‫خسرو از او می‌پرسد نایدید شدنت برای‬

                      ‫اشقر (بروزن استر)‬                                ‫بچوهد؟ رومی می‌گوید‪:‬‬
   ‫اسب قهوه‌ای رنگ کهر‪ .‬و مطلق اسب‪:‬‬                         ‫چنین گفت رومی که گرشهریار‬
                ‫برینگونه تا برگزید اشقری‬              ‫فرستد مرابایکی استوار‬
 ‫یکی بادپایی گشاده بری‬                                        ‫بگویم بدان کاردان پسوزشم‬
 ‫(‪)۷-۲۷۲-۰۴۱‬‬                                          ‫به پوزش بجا آید افروزشم‬
                                      ‫اشکردن‬          ‫‏(‪٩‬رویز ‪۹۱۷۳6‬‬
                                                                ‫پ‬
                 ‫به واه شکردن نگاه کنید‪:‬‬              ‫رومی به استوار نشان می‌دهد که بنا فرو‬
                           ‫اشنان (با پیش اول)‬        ‫نشسته است و اگر در آن زمان ایوان را‬
 ‫گیاهیست که در رخت‌شویی و شست‌و‬                               ‫می‌ساخت بنااز بن فرو می‌ریخت‪.‬‬
‫شوی بدن بکار می‌رود مانند جوبک که‬                     ‫از تاریخ سیستان (‪« :)۸۰۲‬یعقوب به قلعه‬

 ‫امروز بکار می‌برند‪( .‬جهانگیری ‪-‬رشیدی‬                         ‫استواری نشاند و باز سیستان امد»‬

                                  ‫‪-‬رهان)‪:‬‬
                                        ‫ب‬                             ‫‪-۲‬به معنی سخت» محکم‪:‬‬
               ‫شدرت‬
                  ‫ذر ان‬
                      ‫گ گاز‬
                          ‫کنون اختر‬                               ‫پسرش آگنرانمایه اسفندیار‬
‫به دکان شد و برد اشنان به دشت‬                        ‫استوار‬     ‫رست‬
                                                                  ‫ددان‬
                                                                     ‫ند گر‬
                                                                         ‫ابن‬
                                                                           ‫به‬
 ‫(‪)۶۲۷۲۰-۰۲۳‬‬                                          ‫(‪)۶-۵۳۱۰-۰۱۱۱‬‬
           ‫از ناصر خسرو (دیوان ‪:)۲۳۳-۳‬‬                ‫اسقف (باپیش اول و سوم و سکون دوم) س=قف‬

##### leaf 306 (سکوبا)
 ‫سگزی‬                                       ‫‪۳.۳‬‬

                          ‫سکزی (با زبر اول)‬                                        ‫ماه سال‪:‬‬

    ‫منسسوکبسبتهان (عربی؛ سجستان؛‬                            ‫زچین روی یکسر به ایران نهاد‬
 ‫در فرهنگ‌ها مطالب نادرستی دربارة‬                 ‫به روز سفندارمذ بامداد‬
 ‫سگزی و سگستان آمده است (از آنجمله‬                ‫(پ‪۹‬رویز ‪)۷۵۴۲‬‬

  ‫برای نمونه‪ :‬رشیدی چنین می‌نویسد‬
 ‫«سگزی‪ ,‬یعنی سیستانی‪ .‬چه مردم سیستان‬                                ‫به وا اسقف نگاه کنید‪.‬‬
 ‫وگری مشهورند و‬        ‫‌یج‬‫ختتجان‬
                               ‫سسخ‬‫به‬                                        ‫سکوبا (با پیش اول)‬
            ‫لهذا سیستان راسگستان گویند»)‪.‬‬         ‫پیشوای مذهبی در آیین مسیحی (معرب‬
‫در تاریخ سیستان بارها از «سجستان» که‬              ‫ان سقف اسقف» لاتینی ‪ 50۲0050‬به‬
  ‫معرب سگستان است نامبرده شده است‪.‬‬                                   ‫واژ؛ اسقف نگاه کنید)‪.‬‬
 ‫بهار مصحح تاریخ سیستان در زیرنویس‬                           ‫نوشتند نامه به هر کشوری‬
‫ص ‪ ۲۲‬چنین می‌نویسد‪« :‬آنچه معتقد‬                   ‫سکوبا و بطریق و هر مهتری‬
 ‫علمای علم لغت است سیستان مصحف‬                    ‫(‪)۶-۶۳-۹۵۴‬‬

 ‫سگستان است که مملکت سکه‌ها باشد و‬                                ‫سگالش (اسم مصدر از سکالیدن)‬
 ‫این «سکه» مردمی بوده‌اند از عشایر‬                                               ‫اندیشیدن‪:‬‬

 ‫آریایی که بعد از انقراض دولت‬                                   ‫نشستند بیدار هر دو به هم‬
  ‫هخامنشی در حدود ‪ ۰۳۱‬ق ‪.‬م‪ .‬ادوراییل‬              ‫وم‬
                                                   ‫سگالش گرفتند بر بیش ک‬
‫عهد اشکانیان وارد آن سرزمین شده و تا‬              ‫(‪)۳-۶۵-۲۳۴۸‬‬
 ‫خود‬      ‫فتات‬
             ‫ر تح‬
                ‫ص را‬
                   ‫تنجاب‬
                       ‫موپ‬
                         ‫سند‬                                                         ‫سکالیدن‬
 ‫قدرااردند و قبل از آن نامسیستان «زرنگا»‬                                         ‫اندیشیدن‪:‬‬

‫بوده است کهنامشهر «زرنگ» از آن گرفته‬                            ‫کسی کو بود شهریار زمین‬
                              ‫شده است‪».‬‬           ‫نه بازیست بااو سگالید کین‬
‫پروفسور هرتسفلد درین‌باره چنین گوید‪:‬‬              ‫)‪(1-۵۸-۷۰1‬‬

 ‫«از زمان سیروس (تقریباً ‪۵‬ق‪0‬بل از میلاد)‬                                   ‫(ناصر ‪:)۹۳۲-۵۱‬‬
 ‫تادور؛ اسکندر‪ .‬این ساکاها در آن طرف‬                     ‫مرتو رانیکی سگالد یار تو‬
 ‫سغد یعنی در فرغانه سکونت داشتند‪ .‬در‬              ‫چون مر او را توشوی نیکوسگال‬
 ‫سالنامه‌های دولت چين اسم آنها در‬                                    ‫(ویس ‪:)۲۹۲-۲۷۱‬‬
 ‫اواسط مائهدوم قبل از میلاددر آن حدود‬                   ‫بدان روزی که از تو شد چه نالی؟‬
  ‫هها‬
    ‫برده می‌شود‪ .‬هدمران موقع اآستن ک‬              ‫وز آن روزی که نامد چه‌سگالی؟‬
 ‫مورد تهاجم سایر ملل آسیای مرکزی‬                    ‫(سیاست‌نامه ‪ :)۸۸‬تدبیر کار او بسگالند‪.‬‬
```


## [2026-09-05T20:31:30.409Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==44' FSF_pages.txt | head -40"
}
```


## [2026-09-05T20:31:30.852Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; timeout 600 python3 tools/ref_page.py BQT:2083 2>&1 | head -60"
}
```


### [2026-09-05T20:31:32.078Z] TOOL RESULT

```
           ‫آن بادساری از دل بیرون کن‬
 ‫اکنون کهپخته گشتی آوهسته‬
                                       ‫آهنج‬            ‫ز فریادرس زور و فریاد خواست‬
‫از آهنجیدن ‏ آهنگیدن به معنی آهیختن‪.‬‬           ‫از آهرمن بدکنش دادخحواست‬
‫کشیدن «آهنج‪ :‬آهختن‪ ,‬آهنجیدن‪ ,‬کشیدن‪,‬‬           ‫‏(‪)۵٩۲-۴۷۳-۵‬‬

‫برکشیدن» (صحاح ج‪-‬هانگیری ‪-‬رشیدی ‪-‬‬                                                    ‫آهستکی‬
‫برهان)ء «و از اینجاست «دود آهنج» یعنی‬                  ‫(نقیض شتابزدگی)» نرمش» وقار‬
       ‫دودکش حمام و بخاری» (رشیدی)‪:‬‬            ‫مر او [رودابه ]راستودند یک یک مهان‬
           ‫کمان بفکن از دست و ببر بیان‬        ‫همان کز پس پسرده بسودش نهان‬
‫بر آهنج و بگشای تیغ از میان‬                     ‫زبالاو دی لارو آهستگی‬
 ‫(‪)۶-۸۸۲-۸۵۱۱‬‬
                                               ‫ز بسسایستگی هسم ز شسایستگی‬
                 ‫از رودکی (نقل صحاحلفرس)‪:‬‬      ‫‪۸۵۱۲۴۳‬‬
             ‫آورن ده مردمان مر رنج را‬                  ‫از ناصر خحسرو (دیوان ‪:)۶۹۳-۴۱‬‬

‫بیش کرده رنج جان آهنج را‬                                         ‫بیابی ز من شرم و آهستگی‬
      ‫از اسدی ( گرشاسب‌نامه ‪:)۶۷۲-۳۴۱‬‬         ‫اگر شرمگن مرد و آهسته‌ای‬
          ‫یکی مرد فرزانه ز ایران زمین‬                            ‫از ترجمة تفسیر طبری (‪:)۲۳‬‬
‫چنین گفت با پهلوان گزین‬                       ‫«شتاب زدگی اندر کارها از کاردیو است و‬

          ‫که‌گر سیر بر سنگ آهن‌ربای‬                                  ‫آهستگی از کار خدای»‪.‬‬

 ‫بمالی نیاهنجد اهن زجای‬                                               ‫از سیاست‌نامه (‪:)۱۲۱‬‬
          ‫بهسرکه از آنپس چو شوییش باز‬         ‫«و هر که شتابزده باشد و آهستگی‬
‫دگر ره کش نزدش آهن فراز‬                           ‫ندارد همواره پشیمان و غمناک باشد»‬
                                       ‫آهنک‬                                            ‫آهسته‬

‫فدررهنگ‌هاء بطور کلی» بهمعنی قصد و‬             ‫آرام» نسرم» خسوشبو خوش‌سلوک»‬
‫یابسند‪ .‬آهنگ‬
           ‫وشت‬
             ‫نو‬‫یو‌عزم‬
                    ‫مجه‬
                      ‫تو‬                                     ‫‪۰‬‬      ‫خوشرفتار‪:‬‬
    ‫وای‬
      ‫‌اه‬
        ‫سنی‌ه‬
            ‫ن مع‬
               ‫ا به‬
                  ‫ونامه‬
```


### [2026-09-05T20:31:39.197Z] TOOL RESULT

```
(no exact page map; using offset -1917 -> pdf page 166; check the printed number and re-run with --pdf-page if off)
REF: BQT:2083  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 166  OCR-lang: fas

سضا ساسا میوان
چه کیمیاکر را میناکر هم میگویند ۱ - و نام | شحاك 9 .3
قلمه‌است مابین لار و هرموز ۴. میئوس - بکر اول و سکوت آخر
میناسم - بمنی سیاء سم وسيزسم . که سین بی نقطه باشد ‏ نام پادشاهی است که
میناگ - بروزن زبرك » کیاهی باش د که بدرویشی افتاد و یار پربشان شد و دیگر پار
ازآن جاروب سازند . بیادشاهی رسید .
همین ۴ - بروزن نیکو. بهشت راکویند مینوی خااك - با خای له دار ,
وبعربی جنت خوانند - وآسمانر| هم گفته اند - کنایه ا زکور وقیر ومدفن باشد .
و بمعنی مینا هم آمده است که آبگينهٌ سفید میق - با نانی‌مجپول بروزن دیو » بمعنی
والوان باشد۴ - وزمرد وزیرجد را نیز کوبند۴ . | موی باشد که عربان شمرخوانند٩‏ - و در بسنی
مینو باك - با بای ابجد بر وزن نیکو | ازبلاد تاك انگور راکویند بعنی‌درخت انگور۷ .
زاد » نام شهری و مدینه ای بوده در زمان میواد < بروزن ومعنی می‌باد اس ت که
۱ - یز جهالگیری برای ان معنی بدین شمر مولوی استناد جسته :
نادر | کسیری که از وی انیم تاب بر ظلامی زد بگرش آفتاب
بوالمجب میناکری کز يك عبل بت چندین خاصیت رابرزحل.
« مثنوی چاپ نیکلسن دفترچهارم ص ۳۱۳
لیکن درین شمر دز همان معنی مشهور درست مینماید « فرهنگه نظام » .
۴ -ظ . مراد ۶ میناب » است . رك : جغرافیای سیاسی. کیهان ص4۸4 .
۳ - اوستایی 3221072۷8 (روحی, آسمانی) «بارتولمه ۱۱۳۹ ۰ مشتق از-/[۳۸12
« پارتولمه ۱۱۳۹ ۶ ورك : لیب رکه ص ۰۱-۱۵۰ نیز اوستایی 328680۵1 ( روح »آسمان ) «اسشق
۱ ». درپهلوی 608۴ , جمم 22680620 (که ۵2۵8 . 136288280 در مینوخرد
۰ فووشته شده) آمدء و3 من وکه > ازرهٌ پارسی باستان - 0182/1 ۳ اوستابی-/[78818
(روح) مطابق است . قس : پپلوی 22206 * اوستایی -2821 وغیره . پازند 8282(/6(روح)
یز از اوستا ناشی است « هویشمان ۱۶۱۱ *» دراوراق مانوی ( پهلوی ) 7278۷۷8 (آسمانی) »
0 ( روان ) آمد. , 8505 ....8679120 ۸۸:4416 0۶ افنا ۸ موقنمطع17 )
(85. 2 را ,12 ۴ - رك :ح وه صفحهٌ قبل .
اد مینوآ باد ؛ نام بادیه‌ای بروز گارضسا که از خوش ی که بود. آسدی (طوسی) کوید:
ز خوشی بود میئو آپاد نام چو بگذشت ازو پپلوان شادکام .
« لت فری ص ۰۴۱۱۹
ولی چنین نامی در شاهنامه نیامدء . رك : فهرست ولف . ۱
۹ مو ۱ جم اول ) موی («.م.) :
دو دستتو شل به » دوگوش توکر دو چشم و بی لور و پر میو به -
پور بهای جامی «جهانگیری» «رشیدی».
و رك : فرهنگه نظام . ۷ «میو ( بفتی اول ) (ه.م.) * میوانه « فرهنگه نظام»؛.کردی
7۷ ( با که ) ‎٩‏ ژایا س ۰2۱۲
5 میفوچهر - رك : منوچهن .
```


## [2026-09-05T20:31:50.381Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"اهریمن\\|اهرمن\" BQT_v1_pages.txt | head -20"
}
```


### [2026-09-05T20:31:50.434Z] TOOL RESULT

```
3363:دیگر ايزدان آمده وبعدها در آبین زروانی پروردگار بزرکه موجد مزدا و اهریمن شمرده شده
7908:خوانند . دبوست از منابمان اهرمن که سخن چیتی رفتنه
15280:6 رك: اهریمن . ۹
15283:. هرن » بر وزن بهمن » بمعنی اهرمن
15292:اهرمن‌است که رهنمای بدیها باشد چنان‌که‌بزدان
25339:باهمال خود انسائرا می‌فر سمف. دراومتا بری جنس موّث «حادو» مصوب شده که ازطرف اهریمن
30560:٩‏ - زنی پلشت ونلاتوف و اهرمن کردار
```


## [2026-09-05T20:31:54.148Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/leaf.py data/verification/sources/refs/BQT_v1_pages.txt 15280 15283 15292; cd data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==311' BQT_v1_pages.txt | head -60"
}
```


### [2026-09-05T20:31:56.173Z] TOOL RESULT

```
data/verification/sources/refs/BQT_v1_pages.txt line 15280 -> 0-based leaf 409
data/verification/sources/refs/BQT_v1_pages.txt line 15283 -> 0-based leaf 409
data/verification/sources/refs/BQT_v1_pages.txt line 15292 -> 0-based leaf 409
اردشیران
" قهر وخشم یز آمده است٩‏ ؛ و فلم پسر ساسان
این همن که اول ماسانان بوده ات و او را
اردشیر بایکان میگفته اند ۰ واک‌لسره ابشان
اند - و تلم پسر شیروبه بن پرویز هم هست - و
کی را نیز گوبند که در قوت و شجامت بی
تهپور و جبن باشد .
اردشیر ان ۴ - بالف و نون » نوتی
از مرواست و آن گیاهی باشد خوشبوی لیکن
ار دشیر جر ه ضم خای نقطه دار
و فتح رای بی‌نقطهٌ مشدد » نام‌الکه‌ایست بز رکه
از ولات فار ی که شیراز و میمند وس‌منکان(۱)
)۱ صیمکان * لفت‌نامه * .
مج وه اح
و برخان (۷) و سیراف و کازرون و کم فیروز
از آن الکه است و رسم کرد؛ اردشیر باشد » و
بحضنی گویند رسم کرد نمررود بن کنمان است؟ .
ار ذشیر ۵ارو « با دال بی شله
بالف کشیده و رای بی تقطه‌بواو رسیده ؛ بمعنی
اردشیران است وآن داروبی باشد درنهایت تلخی.
اردفناقی « بح اول و کس انی و
سکون * اث و فتح فا و نون نالف کشیده ‏ وکس
فای دیگر شحتانی رسده ۰ بللت بوهانی نباتی
است صحرابی , جهت کزند کی جانوران خصوصاً
زئبور طللا کنشد نافم باشد . و آثرا یعربی قثاه
الحمار خوانند . #
م کب بمنی اه آردشیر واردشیر پادشاهی است
کیت
ارو
۵ اردل ماهی - نوعی ازماهیان
۰ ۹ ۱
استخواندار , که در آب های ابران چندان ‌
زباد نت کلا۱6 850 « دربای خزر ‌
۷ > .
بقبه از صفحه ٩٩‏
است »متیر از مقدی . اما وبراف مشق از وبر بمعنی مرد و هوش و خرد است » کلمه بمعنی
```


## [2026-09-05T20:32:00.049Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==410' BQT_v1_pages.txt | head -70"
}
```


### [2026-09-05T20:32:01.642Z] TOOL RESULT

```
٩۸4 -
احریمه
اه - ختح اود و سکون انی : بسحنی آء
باشد و آن کلبه ات" که دود وفت اضوی
وحسرت گویشد.
اهاد ‏ بروزن هار : پالومه ای که بر
کاغذ و شوربای ی که بر جامه ماللد ٩‏ .*
اهر - بروزن بهر ۴ ان موضی است
از آ ذربایجان که رودخانٌ عظیمی دارد ۴ - ونام
درختی هم هس تکه ثم رآنرا زبا نکنجشك‌وبعرمی
لسان العصافیر خوانند و شکوفه و بپار آنرا
ستبل‌الطب خواند ۴ .
اهر امین * - بروزن‌تردامن» راهنمای
دی ها را گویند ؛ و شیطان- و دیوانه را یز
کگفته اند .
اهر ان بفتح
بفتح اول و سکون ثانی‌والث
آهر ۵ - بروزن همدم . چویی باشد که
هریسه را بدان کویند .
الهرهن * « بعتح‌تاك بروزن‌ک رکدن,
6 رك: اهریمن . ۹
است » و شیطان و دیو را نز گود : و بکس
ثاك هم آمده است .
. هرن » بر وزن بهمن » بمعنی اهرمن
باشد که رهنمای‌بدیها و شطان است ۵ - وجن
پا کشتاسب هم سلف بوده یعنی‌ه رکدام باگلدختر
قیصی راداشته‌اند - و بزبان‌هندی مندان‌زرگری
و آهنگربراگویند . :
اهر ون بروزن عجنون , تلحکیمی
بوده‌است بپودی که در جمیح علوم‌خصوصا درعلم
طب مهارنی ماع داشته ۷ .
اهر هی ۲ - بر وزن لفزبدن . بمعنی
اهرمن‌است که رهنمای بدیها باشد چنان‌که‌بزدان
رهنمای لیکی است . و شیطان و دیو و جن را
اهر یمه ۰ بروزن شمنه «راهنمای
بدیها باشد » و شیطانرا نیژ گویند .
۴ - م رکز
۴ - ۳۳8۱۲16 دای ۱۹4*.
کرده اس
ست «فاموس‌الاعلام تر کی*.
بقیه درصفحةً ۳
```


## [2026-09-05T20:32:13.285Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for n in 404 406 408 410 412 414; do echo \"--- NR=$n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' BQT_v1_pages.txt | head -3; done"
}
```


### [2026-09-05T20:32:15.094Z] TOOL RESULT

```
--- NR=404
ی و ای
ع ‏ به ۷ ج جم حممي یه ۶" چا + ف ( ۲[ ج هو مه
۳ 2
--- NR=406
کردن باشد و آلرا بعربی جارت خوانند که
کتاخی باشد ؟ .
اوستاك » بر وزن نوشباد ۰ داننده
--- NR=408
٩ لب‎
است که در مقابل حنیش باشد ءو اوج معوّب
آدت .
--- NR=410
٩۸4 -
احریمه
اه - ختح اود و سکون انی : بسحنی آء
--- NR=412
۱ اهور * - بنتع اول و ثالث و سکون
ثانی و زای نقطمدار ۰ نلم تیرآندازی بوده بفایت
قادرانداز در زمان انوشیروان » کوبند باسیف ذو
--- NR=414
۱۳ات ایدغ
ایاره گیر ۱ -بر وزن کنار هگیر ».
محاسب و نوبسنده را گویند .
```


## [2026-09-05T20:32:23.785Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; ls site/pages/155.jpg 2>/dev/null; pdftoppm -f 155 -l 155 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg155 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-05T20:32:26.117Z] TOOL RESULT

```
site/pages/155.jpg
total 15592
drwx------ 2 sfmqrb sfmqrb    4096 Sep  5 16:32 .
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
-rw-rw-r-- 1 sfmqrb sfmqrb   56126 Sep  5 16:29 build136b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   13830 Sep  5 16:22 build136.py
-rw-rw-r-- 1 sfmqrb sfmqrb   66341 Sep  5 16:28 build139.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53260 Sep  5 16:29 build142.py
-rw-rw-r-- 1 sfmqrb sfmqrb   21485 Sep  5 16:29 build148.py
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep  5 16:18 kent.txt
-rw-rw-r-- 1 sfmqrb sfmqrb     222 Sep  5 16:30 leaf.py
-rw-rw-r-- 1 sfmqrb sfmqrb   57617 Sep  5 16:20 mk129.py
-rw-rw-r-- 1 sfmqrb sfmqrb   74680 Sep  5 16:26 mk131.py
-rw-rw-r-- 1 sfmqrb sfmqrb   33365 Sep  5 16:25 mk133.py
-rw-rw-r-- 1 sfmqrb sfmqrb   42635 Sep  5 16:29 mk140.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51288 Sep  5 16:30 mk143.py
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep  5 16:13 oldpers_djvu.txt
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
-rw-rw-r-- 1 sfmqrb sfmqrb   96854 Sep  5 16:29 pg151.png
-rw-rw-r-- 1 sfmqrb sfmqrb   39131 Sep  5 16:28 pg153.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63033 Sep  5 16:30 pg154.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77057 Sep  5 16:32 pg155.png
-rw-rw-r-- 1 sfmqrb sfmqrb  124379 Sep  5 16:31 pg159_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   27814 Sep  5 16:31 pg159.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4694 Sep  5 16:31 pg159_word.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4868 Sep  5 16:14 prt.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  333088 Sep  5 16:16 sod135_c.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1817364 Sep  5 16:16 sod135.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  101641 Sep  5 16:15 sod136_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1892712 Sep  5 16:15 sod136.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   56398 Sep  5 16:26 write144.py
```


## [2026-09-05T20:32:29.449Z] TOOL CALL #40: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg155.png"
}
```


### [2026-09-05T20:32:29.806Z] TOOL RESULT

```

```


## [2026-09-05T20:32:29.804Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T20:33:26.777Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== AHD epi ===\"; grep -n -i \"^epi\\b\\|epi-\\.\" AHD_watkins1985.txt | head; grep -n \"epi\\.\" AHD_watkins1985.txt | head; echo \"=== AHD search 'Pok. epi' ===\"; grep -n \"Pok. epi\" AHD_watkins1985.txt | head"
}
```


### [2026-09-05T20:33:26.850Z] TOOL RESULT

```
=== AHD epi ===
446:epi. Also opi. Near, at, against. 1. Latin ob, ob-, before, to, against: OB-. 2. Greek epi, on, over, at: EPI-. 3. Greek opisthen, behind, at the back: OPISTHOBRANCH, OPIS- THOGNATHOUS. 4, Zero-grade “pi-, on, in Greek piezein, to press tight (see sed-1). 5. Old Church Slavonic ob, on, in Russian oblast’, oblast: OBLAST. 6. Prefix *op- in *op-wer-yo-, to cover over (see wer-5). [Pok. epi 323.]
1467:EPI- epi
446:epi. Also opi. Near, at, against. 1. Latin ob, ob-, before, to, against: OB-. 2. Greek epi, on, over, at: EPI-. 3. Greek opisthen, behind, at the back: OPISTHOBRANCH, OPIS- THOGNATHOUS. 4, Zero-grade “pi-, on, in Greek piezein, to press tight (see sed-1). 5. Old Church Slavonic ob, on, in Russian oblast’, oblast: OBLAST. 6. Prefix *op- in *op-wer-yo-, to cover over (see wer-5). [Pok. epi 323.]
=== AHD search 'Pok. epi' ===
446:epi. Also opi. Near, at, against. 1. Latin ob, ob-, before, to, against: OB-. 2. Greek epi, on, over, at: EPI-. 3. Greek opisthen, behind, at the back: OPISTHOBRANCH, OPIS- THOGNATHOUS. 4, Zero-grade “pi-, on, in Greek piezein, to press tight (see sed-1). 5. Old Church Slavonic ob, on, in Russian oblast’, oblast: OBLAST. 6. Prefix *op- in *op-wer-yo-, to cover over (see wer-5). [Pok. epi 323.]
```


## [2026-09-05T20:33:27.719Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== KLN bishop ===\"; grep -n \"bishop\" KLN_1966.txt | head -10; echo \"=== SKT bishop ===\"; grep -n \"bishop\" SKT.txt | head -5"
}
```


### [2026-09-05T20:33:27.785Z] TOOL RESULT

```
=== KLN bishop ===
1301:aeariatre,  adj.,  bad-tempered.  —  F.,  ‘contrary, crabbed,  quarrelsome’,  orig.  meaning  ‘possess¬ ed  by  a  demon’,  formed  with  pejorative  suff. -atre,  from  the  name  of  Acharius,  bishop  of Noyon  in  the  7th  cent.,  renowned  for  curing folly.  The  suff.  -atre  derives  fr.  OF.  -astre,  fr.  L. -aster;  see  -aster.
3320:Derivatives:  arch-ly,  adv.,  arch-ness ,  n. arch-,  pref.  meaning  ‘chief,  principal’,  as  in  arch¬ duke ,  archbishop.  —  ME.  arche-,  fr.  OE.  arce-,
3333:archbishop,  n.  —  ME.  archebischop ,  fr.  OE.  arce- biscop,  fr.  Eccles.  L.  archiepiscopus,  fr.  Eccles. Gk.  apxt£mcnco7ro?,  lit.  ‘chief  bishop’,  fr.  Gk. apyi-  (see  archi-)  and  Imaxonoc,  ‘bishop’.  See
3334:bishop.
3335:archbishopric,  n.  —  M  H.archehischopriche,  fr.  OE. arcebiscoprlce.  See  arch-  and  bishopric  and  cp. prec.  word.
3859:Derivatives:  atmometr-ic,  adj.,  atmometr-y,  n. atmosphere,  n.  —  Compounded  of  Gk.  dxpop, ‘steam,  vapor’,  and  cnpoupa,  ‘ball,  sphere’;  see atmo-  and  sphere.  The  word  atmosphere  was  first used  by  the  English  bishop  and  scientist  John Wilkins  (1614-72)  in  1638  with  reference  to  the moon  (which  in  reality  has  no  atmosphere). Derivatives :  atmospher-ic,  atmospher-ic-al,  adjs., atmospher-ic-al-ly,  adv.,  atmospher-ics,  n.pl. atocia,  n.,  sterility  of  the  female  (med.)  —  Medi¬ cal  L.,  fr.  Gk.  axoxla,  ‘sterility’,  fr.  6x0x04, having  never  yet  brought  forth’,  fr.  4-  (see  priv. pref.  a-)  and  XOX04,  ‘childbirth,  parturition’, which  is  rel.  to  xoxefx;,  ‘father’,  in  the  pi., ‘parents’.  See  -tocia,  toco-,  and  cp.  anatocism, atoll,  n.,  a  coral  island.  —  Malayalam.
5065:bisect,  tr.  v.,  to  cut  in  two.  —  Formed  fr.  bi-  and L.  secare,  pp.  sect  us,  ‘to  cut’.  See  section. Derivatives:  bisect-ion,  n.,  bisect-or,  n. bisexual,  adj.  —  Formed  fr.  bi-  and  sexual, bishop,  n.  —  ME.  biscop ,  bischop,  fr.  OE.  bis- ceop,  biscop,  fr.  L.  episcopus,  ‘overseer,  super- intendant’,  in  Eccles.  L.,  ‘bishop’,  fr.  Gk.  £-1- axottoq,  ‘overseer’,  fr.  km,  ‘on,  over’,  and  ctxottoc, ‘watcher’.  See  epi-  and  -scope  and  cp.  episcopal. Cp.  also  obispo.
5066:Derivative:  bishop,  tr.  and  intr.  v. bishopric,  n.  —  OE.  bisceoprice,  biscoprice,  com¬ pounded  of  bisceop,  biscop,  ‘bishop’,  and  rice ‘dominion’.  See  prec.  word  and  Reich, bismite,  n.,  bismuth  trioxide  (mineral.)  —  Coined fr.  next  word  and  subst.  suff.  -ite. bismuth,  n.,  name  of  a  metallic  element  (chem.)  — G.  Bismuth  (now  spelled  Wismut),  Latinized  by Georgius  Agricola  (in  1530)  into  bisemutum. The  origin  of  the  word  is  uncertain.  It  is  not connected  with  Arab,  ithmid,  ‘antimon’,  as  most lexicographers  would  have  it. bismuto-,  bismutho-,  combining  form  meaning ‘bismuth’.  —  See  prec.  word, bisnaga,  n.  a  kind  of  cactus.  —  Port,  bisnaga  (cp. Sp.  biznaga),  fr.  Arab,  bisndj,  secondary  form  of bastindj,  fr,  L .pastindca,  ‘parsnip’.  See  parsnip, bison,  n.,  wild  ox.  —  F.,  fr.  L.  bison,  fr.  OHG. wisunt  (MHG.,  G.  wisent),  which  is  rel.  to  OE. wesand,  ON.  visundr,  and  cogn.  with  OPruss. wis-sambrs,  ‘aurochs’,  and  with  L.  vissio, ‘stench’.  The  bison  is  named  after  the  peculiar odor  of  musk  emitted  by  it  during  the  rutting season.  See  weasel.
5679:Derivatives:  Brobdingnag-ian,  adj.  and  n. brocade,  n.,  a  rich  figured,  woven  fabric.  —  Sp. brocado,  fr.  broca,  fr.  ML.  broccare,  ‘to  prick, emboss’,  fr.  L.  broccus,  ‘projecting’  (said  esp. of  teeth).  Cp.  It.  broccato,  F.  brocart,  and  see broach,  n.  For  the  ending  see  suff.  -ade. Derivatives:  brocade,  tr.  v.,  brocad-ed,  adj. brocard,  n.,  a  law  maxim.  —  F.  brocard,  fr.  ML. brocardus,  of  s.m.,  fr.  Brocardus,  fr.  Burchardus, G  Burckard,  bishop  of  Worms,  who  in  the  1st half  of  the  nth  cent,  compiled  an  ecclesiastical canon.
6806:cathedra,  n.,  the  seat  of  a  bishop.  —  L.,  fr.  Gk. xaffcSpa.  See  chair  and  cp.  ex  cathedra.
=== SKT bishop ===
872:Arch-,  frtfx,  chief.  (L.-Gk.5  The form  arxM-  i«  due  to  A.  S.  arr/-,  as  in  artt- kiuiofi,  an  archbishop.  This  form  was boaowcd  from  L.  anhi-  ->  Gk.  Vx^'i  '^ ia  d^X''****''''^^*'*!  on  archbishop.  •-  Gk. ^PXU\r,  to  be  first,  to  rule;  cf.  Gk.  &pxht
3120:Cathedral.  U-  -  Gk.)  L.  cath<drah's eaUsia  =  a.  cathedral  church,  or  one  which has  a  bishop's  throne.  — Low  L.  cathedra, a  throne  — Gk.  iva&cO/xi,  a  seat  —  Gk.  «a^, for  jrarii,  down;  and  \hpa,  a  seat,  chair, from  li»iUkx  (  >-^S-/o^cu),  I  at ;  sec  Sit.
4405:crosier.  (F.  -  Tcut.)  M.  E.  croecr^ croscr,  8ic.  FonneH,  with  suffii  -<r,  from M.  E.  cnxc,  in  the  same  sense  of  'bishop's staff.'  — U.  F.  eroce,  *a  crosier,*  Cot. ;  mod. F.  (rosse-  Low  L.  trocia.^O.  F.  eroi,  a crook;  see  crochet  above.  ^  Nol  from crcii,  to  whidi  it  is  only  uUtntately  re- lated.
5920:Epiacopal.  ( F.  -  L.  -  GL.)  O.V  .episcopal. ■-  L.  episcopalis,  beloiignng  to  a  bishop, -•L.  tpiscoptts,  a  bishop.»Gk.  Jvio«uiTtif, &a  over-seer,  bishop.  *  Gk.  imi.  upon ; VKovM,  one  that  watdics.  (V^I^AK.)  Sec Scope.
13185:papal,  belonging  to  the  pope.  (F.  — L. —  Gk.^  F.  /d/tf/.-Low  L.  papalis,  adj., from  L.  papa,  a  bishop,  spiritual  father.  •• Gk.  iraro,  vdrra,  vocative  of  rdvor,  niv* wot.  papa,  father  (above).
```


## [2026-09-05T20:33:40.248Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nprint(d['KLN']['page_offset']); print(d['KLN'].get('lookup_hint'))\nprint('---AHD---'); print(d['AHD'].get('page_offset')); print(d['AHD'].get('lookup_hint'))\nprint('---FSF---'); print(d['FSF'].get('page_offset'))\nprint('---TAD---'); print(d['TAD'].get('page_offset'))\nprint('---BQT---'); print(d['BQT'].get('page_offset'))\n\""
}
```


## [2026-09-05T20:33:41.452Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"^ob-, pref\\|ob-,  pref\\|obit\\b\" KLN_1966.txt | head -5; echo \"=== epi- pref ===\"; grep -n \"epi-,  pref\\|epi-, pref\" KLN_1966.txt | head -5"
}
```


### [2026-09-05T20:33:42.349Z] TOOL RESULT

```
KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
---AHD---
1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.
Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.).
---FSF---
484 leaves; edition/printing of this scan not identified — determine offset from printed page numbers on the page text/image when checking
---TAD---
86 leaves (small book, ~80 printed pages); offset ≈ leaf − 4..6, verify against the printed numeral on the page image
---BQT---
vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
```


### [2026-09-05T20:33:42.411Z] TOOL RESULT

```
6949:Derivatives:  cenobit-ic,  cenobit-ic-al,  adjs.,  ceno- bit-ic-al-ly,  adv.,  cenobit-ism,  n. cenoby,  n.  —  See  coenobium.
20061:‘neck  of  land,  isthmus,  any  narrow passage’.  Cp.  Abeona,  abiturient,  adit,  ambit, ambition,  anion,  cation,  circuit,  coeno-,  coetus, coition,  coitus,  comitia,  commence,  count,  ‘title of  nobility’,  dysprosium,  errant,  exeat,  exeunt, exit,  eyre,  ichno-,  inevitable,  initial,  introit,  ion, issue,  isthmus,  jadoo,  janitor,  jaun,  limit,  obit, obituary,  perish,  praetor,  preterit,  Rathayatra, sedition,  seditious,  sudden,  trance,  transient, transire,  transit.  Cp.  also  oath  and  the  second element  in  wide.
20120:Derivatives:  jacobit-icai,  adj.,  Jacobit-ism,  n.
25837:ob-,  pref.  meaning  T)  toward  to;  2)  against;  3) across,  over,  upon;  4)  down;  5)  completely’.  — L.  ob-  (before  c ,/,  g,p,  assimilated  into  oc-,  of-, og-,  op-;  before  m,  ob-  becomes  o-),  fr.  ob,  ‘to¬ ward,  against,  in  the  way  of;  about;  before;  on account  of;  instead  of’,  which  is  rel.  to  Oscan op,  up,  Umbr.  os  (for  *ops),  and  cogn.  with  Gk. om-  in  omO-s(v),  Ion.  and  Att.  oma-O-E  (v), ‘behind,  at  the  back,  after’,  omato,  ‘backward’, o^e,  Lesbian  Tate  in  the  day,  at  even’,  Hitt. appizzis,  ‘younger,  youngest’,  Lith.  ap-,  apt-, ‘about,  near’;  fr.  I.-E.  base  *opi-,  which  stands in  gradational  relationship  to  I.-E.  *epi-,  whence Gk.  e-i,  ‘on,  upon’.  See  epi-  and  cp.  oper¬ culum,  opisometer,  opistho-,  opsimath,  overt, cover,  covert,  Oscines,  ostensible.
25855:obiit,  v.,  he  died.  —  L.  3rd  pers.  sing.  perf.  of obire,  ‘to  die’.  See  obit.
=== epi- pref ===
```


## [2026-09-05T20:33:48.955Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/leaf.py data/verification/sources/refs/KLN_1966.txt 25837 5065; cd data/verification/sources/refs; grep -n \"^epi-\" KLN_1966.txt | head -5; grep -n \"epi-,  *pref\\|‘on,  upon’\" KLN_1966.txt | head -8"
}
```


### [2026-09-05T20:33:50.654Z] TOOL RESULT

```
data/verification/sources/refs/KLN_1966.txt line 25837 -> 0-based leaf 570
data/verification/sources/refs/KLN_1966.txt line 5065 -> 0-based leaf 103
13351:epi-,  before  a  vowel  ep-,  before  an  aspirate  eph-, pref.  meaning  ‘on,  beside,  among,  above,  an¬ terior’.  In  chemistry  this  pref.  denotes  relation of  some  kind  to  a  specified  compound.  —  Gk. ini-,  in-,  £9-,  fr.  ini,  ‘on,  upon;  up  to,  over, after;  at;  beyond,  besides’,  cogn.  with  OI.  dpi, ‘also,  besides’,  Avestic  aipi,  ‘also;  to,  toward’, Toch.  -pi.  Arm.  ev,  ‘also,  and’,  and  in  gradat¬ ional  relationship  to  Gk.  6m-  in  omlle(v).  Ion. and  Att.  5ma9i(*),  ‘after,  behind’,  L.  ob,  ‘to¬ ward,  against,  in  the  way  of;  about;  before;  on account  of;  instead  of’.  Cp.  ob-  and  words  there referred  to.  Cp.  also  the  first  element  in  bias, bishop.  For  Teut.  cognates  see  even,  ‘evening’, epiblast,  n.,  the  outer  layer  of  the  embryo  (biot.) —  Compounded  of  epi-  and  Gk.  (UXacrn iq,  ‘bud, sprout,  shoot’.  See  -blast.
2587:ana-,  before  a  vowel  an-,  pref.  meaning:  1)  up, upward;  2)  back,  backward,  against;  3)  again, anew;  4)  exceedingly;  5)  according  to.  —  Gk. ava-,  dtv-,  ‘up  to,  upward,  up,  toward;  exceed¬ ingly;  back,  backward;  against’,  fr.  ava,  ‘up, on,  upon;  throughout;  again’,  rel.  to  avw, ‘above’,  and  cogn.  with  Avestic  ana,  ‘on,  upon’, L.  an-  in  anheldre,  ‘to  pant,  gasp’,  Goth,  ana, OE.  on,  an,  OSlav.  na,  Lith.  mi,  OPruss.  no,  na, ‘on,  upon';  fr.  I.-E.  base  *ano-,  ‘on,  upon, above’.  Cp.  on  and  a-,  ‘on’.  Cp.  also  the  pref. in  anhelafion.
13362:epicondyle,  n.,  a  surface  or  process  above  a  con¬ dyle  (anat.)  —  Orig.  used  to  denote  ‘the  lateral epicondyle  of  the  humerus’.  The  name  is  er¬ roneous.  It  was  coined  by  the  French  anatomist and  surgeon  Francois  Chaussier  (1746-1828)  fr. epi-  and  condyle.  The  correct  form  should  have been  paracondyle  (in  accordance  with  the  mean¬ ing  of  Gk.  7rap<i,  ‘beside’,  in  contradistinction to  ini,  which  means  ‘on,  upon’).  See  Joseph Hyrtl,  Onomatologia  anatomica,  pp.  200-201. A  similar  erroneous  anatomical  term  (also coined  by  Chaussier)  is  epitrochlea  (q.v.) Epicrates,  n.,  a  genus  of  nonpoisonous  boas (zool.)  —  ModL.,  fr.  Gk.  tnix.pxnr£,  ‘having mastery,  superior’,  fr.  ini  (see  epi-)  and  xpaxop, 'strength,  power’.  See  -cracy. epicure,  n.,  one  given  up  to  sensual  enjoyment. —  L.  Epicurus ,  fr.  Gk.  ’ETttxoupop,  Greek  philo¬ sopher  said  to  have  regarded  sensual  enjoyment as  the  highest  good.
19812:lit.  ‘(away)  from  the  eyes’.  See  ab-  and  ocular. Derivatives:  inveigle-ment,  n.,  inveigl-er,  n. invent,  tr.  v.  —  ME.  inventen,  fr.  L.  inventus,  pp. of  invenire,  ‘to  find’,  prop,  ‘to  come  upon’,  fr. in-,  ‘in’,  and  venire,  ‘to  come’.  See  come  and  cp. venue,  ‘arrival’.  For  sense  development  6p.  Hitt. wemiya-,  ‘to  find’,  prop,  ‘to  come  upon’,  OSlav. na-iti,'  to  find’,  fr.  na,  ‘on,  upon’,  and  iti,  ‘to  go’, OE.  findan,  ‘to  find  out’,  fr.  I.-E.  base  *pent-, ‘to  go’  (see  find).
25837:ob-,  pref.  meaning  T)  toward  to;  2)  against;  3) across,  over,  upon;  4)  down;  5)  completely’.  — L.  ob-  (before  c ,/,  g,p,  assimilated  into  oc-,  of-, og-,  op-;  before  m,  ob-  becomes  o-),  fr.  ob,  ‘to¬ ward,  against,  in  the  way  of;  about;  before;  on account  of;  instead  of’,  which  is  rel.  to  Oscan op,  up,  Umbr.  os  (for  *ops),  and  cogn.  with  Gk. om-  in  omO-s(v),  Ion.  and  Att.  oma-O-E  (v), ‘behind,  at  the  back,  after’,  omato,  ‘backward’, o^e,  Lesbian  Tate  in  the  day,  at  even’,  Hitt. appizzis,  ‘younger,  youngest’,  Lith.  ap-,  apt-, ‘about,  near’;  fr.  I.-E.  base  *opi-,  which  stands in  gradational  relationship  to  I.-E.  *epi-,  whence Gk.  e-i,  ‘on,  upon’.  See  epi-  and  cp.  oper¬ culum,  opisometer,  opistho-,  opsimath,  overt, cover,  covert,  Oscines,  ostensible.
26285:on,  prep.  —  ME.,  fr.  OE.  on,  an,  rel.  to  OS.  an, ON.  a,  Du.  aan,  OHG.  ana,  MHG.  ane,  G.  an, Goth,  ana,  ‘on,  upon’,  and  cogn.  with  Avestic ana,  ‘on",  Gk.  avi,  ‘on,  upon’,  L.  an-  in  an- helare,  ‘to  pant,  gasp’,  OSlav.  na,  OPruss.  no, na,  ‘on,  upon’,  Lith.  nuo,  ‘down  from’,  fr.  I.-E. base  *ano,  ‘on’.  Cp.  a,  prep.,  the  first  element  in anlaut  and  in  unless  and  the  second  element in  upon  and  in  the  verb  don.  Cp.  also  ana-,  ano-. Derivative:  on,  adj.
32269:rely,  intr.  v.  —  ME.  relien,  generally  derived  fr. L.  religdre,  ‘to  fasten  together’,  fr.  re-  and  ligare, ‘to  bind’  (see  ligament).  It  is  more  prob.  how¬ ever,  that  it  is  formed  fr.  re-  and  lie,  ‘to  recline’. Accordingly,  the  exact  spelling  should  be  relie ; the  spelling  -ly  shows  the  influence  of  the  nu¬ merous  words  ending  in  -ly  (as  apply,  comply, etc.)  This  latter  etymology  of  the  word  also  ex¬ plains  why  the  verb  rely  is  construed  with  the prep,  ‘on,  upon’.
```


## [2026-09-05T20:34:01.025Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/leaf.py data/verification/sources/refs/KLN_1966.txt 13351; cd data/verification/sources/refs; echo \"--- leaf 544 head ---\"; awk 'BEGIN{RS=\"\\f\"} NR==545' KLN_1966.txt | head -6; echo \"--- leaf 277 head (epi?) ---\"; awk 'BEGIN{RS=\"\\f\"} NR==278' KLN_1966.txt | head -4"
}
```


### [2026-09-05T20:34:03.099Z] TOOL RESULT

```
data/verification/sources/refs/KLN_1966.txt line 13351 -> 0-based leaf 288
--- leaf 544 head ---
 like  a  mummy,  to  dry  up,  shrivel.  — F.  momifier,  compounded  of  momie,  ‘mummy’, and  -fier,  ‘to  make  into’,  fr.  L.  -  fiedre,  fr. facere,  ‘to  make,  do’.  See  mummy  and  -fy. mummy,  n.,  an  embalmed  body.  —  ME.  mummie, fr.  OF.  (=  F.)  momie,  fr.  ML.  mumia,  fr.  Arab. mumiyah,  ‘mummy’,  fr.  Pers.  mum,  ‘wax’. Derivative:  mummy,  tr.  v..  to  mummify, mump,  intr.  v.,  to  mumble;  to  whine  like  a  beg¬ gar.  —  Obsol.  Du.  mompen,  ‘to  cheat,  deceive’, orig.  prob.  ‘to  mumble,  whine’  (cp.  Du.  mom¬ melen,  mompelen,  ‘to  mutter,  mumble’);  of  imi¬ tative  origin  Cp.  mumble, mump,  n.,  a  grimace  {obsol.)  —  Fr.  prec.  word, mump,  n.,  mumps.  —  See  mumps, mumper,  n.,  a  deceitful  beggar.  —  Formed  fr.
mump,  v.,  with  agential  suff.  -er. mumps,  n.,  an  infectious  disease,  characterized by  the  swelling  of  the  salivary  glands;  parotitis. —  Fr.  mump,  ‘grimace’,  so  called  in  allusion  to the  patient’s  appearance, munch,  intr.  and  tr.  v.,  to  chew.  —  ME.  monchen, prob.  imitative;  not  connected  with  F.  manger, ‘to  eat’.  Cp  crunch.
Derivatives:  munch,  n.,  munch-er,  n. Munchausen,  n.,  inexact  for  Munchhausen  in  the name  of  Baron  Karl  Friedrich  Hieronymus  von Munchhausen  (1720-97),  a  German  adventurer.
1015
who  served  in  the  Russian  army  against  the Turks;  pretended  author  of  a  book  of  wildly exaggerated  exploits  really  written  by  Rudolph Erich  Raspe  (1734-94),  and  entitled  Baron Munchausen,  Narrative  of  his  Marvellous  Trav¬ els  (published  in  1785).
Derivatives:  Munchausen-ism,  n.,  Munchausen- ize,  intr.  v.
--- leaf 277 head (epi?) ---
h’,  and  yapi?, ‘grace,  delight’.  The  first  element  is  cogn.  with OI.  sdras-,  ‘pond’.  For  the  second  element  see Charis.
elephant,  n.  —  ME.  elifaunt,  olifaunt,  fr.  OF.  oli- font  (F.  elephant),  fr.  L.  elephantus ,  fr.  Gk. sXsT>a;  (gen.  -av-ro;).  The  first  element  of  Gk. iX-ltpat;  appears  also  in  Hamitic  eju,  ‘elephant’, whence  prob.  Pers.  p-il,  Arab,  ph-il,  Mishnaic Heb.  p-il,  of  s.m.  The  second  element  is  an Egyptian  loan  word.  Cp.  MEgypt.  yb,  ‘ele¬ phant’,  whence  Yebu  (Heb.  Yebh),  original name  of  the  island  Elephantine;  cp.  also  the second  element  in  Heb.  shen-habbim,  ‘ivory’, lit.  ‘tooth  of  the  elephant’,  and  OI.  tbhah,  ‘ele¬ phant’.  See  ivory  and  cp.  Ebuma.  Cp.  also element.
Derivatives:  elephantiac  (q.v.),  elephantiasis (q.v.),  elephant-ic,  adj.,  elephantine  (q.v.),  ele- phant-oid,  elephant-ous,  adjs. elephantiac,  adj.,  one  who  has  elephantiasis.  —  L. elephantiacus,  rel.  to  elephantiasis.  See  next word.
elephantiasis
```


## [2026-09-05T20:34:15.173Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for n in 287 288 289 290; do echo \"--- leaf $n:\"; awk -v n=$((n+1)) 'BEGIN{RS=\"\\f\"} NR==n' KLN_1966.txt | grep -oE \"^[0-9]{3,4}$|^ ?[0-9]{3,4} ?$\" | head -3; done; echo; awk 'BEGIN{RS=\"\\f\"} NR==289' KLN_1966.txt | grep -nE \"[0-9]{3}\" | head -5"
}
```


### [2026-09-05T20:34:16.855Z] TOOL RESULT

```
--- leaf 287:
528
529
--- leaf 288:
531
--- leaf 289:
532
533
--- leaf 290:
534
535

10:Se?),  ‘freckle’,  fr.  ini  (see  epi-)  and  7, >.105, ‘sun’.  See  helio-  and  cp.  words  there  referred  to. Ephemera,  n.,  the  genus  of  the  Ephemerida  (en- tomol.)  —  ModL.,  fr.  Gk.  itpTjuspov,  ‘dayfly’, prop.  neut.  of  iqjrjpepop,  ‘lasting  but  a  day, short-lived’,  used  as  a  noun,  fr.  ini  (see  epi-) and  ■fjpipa,  ‘day’.  See  hemero-. ephemeral,  adj.,  living  only  for  a  day;  short¬ lived,  fleeting.  —  Lit.  meaning  ‘of  one  day’; formed  with  adj.  suff.  -al  fr.  Gk.  iy^iLepoc.  See prec.  word.
14:Ephialtes,  n.,  a  giant  slain  by  Apollo  (Greek  my- thol.)  —  L.,  fr.  Gk.  ’Etfiikvrfi,  of  uncertain origin.  The  explanation  of  the  ancients  that  the name  derives  from  the  verb  ttpiXksaSou,  ‘to leap  upon’,  is  prob.  folk  etymology.  See  Frisk, GEW.,  pp. 508-509.
23:Derivative:  epiblast-ic,  adj. epic,  adj.  —  L.  epicus,  fr.  Gk.  67:1x61;,  ‘epic’,  fr. £7104,  ‘word,  song’,  in  pi.,  ‘epic  poetry’.  See epos  and  -ic  and  cp.  epopee.
28:epicene,  adj.,  of  common  gender  (gramm.)  —  L. epicoenus,  fr.  Gk.  6711x00104,  ‘common,  pro¬ miscuous’,  fr.  6m  (see  epi-)  and  xoivop,  ‘com¬ mon’.  See  coeno-.
31:epichorial,  adj.,  pertaining,  or  restricted,  to  a country  or  a  district.  —  Formed  with  adj.  suif. -al  fr.  Gk.  6mxtl)pto?,  ‘in,  or  of,  the  country’, fr.  671!  (see  epi-)  and  x“P“>  ‘country’.  See
```


## [2026-09-05T20:34:24.450Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for n in 569 570 571; do echo \"--- leaf $n:\"; awk -v n=$((n+1)) 'BEGIN{RS=\"\\f\"} NR==n' KLN_1966.txt | grep -oE \"^ ?[0-9]{3,4} ?$\" | head -3; done"
}
```


### [2026-09-05T20:34:26.258Z] TOOL RESULT

```
--- leaf 569:
1064
--- leaf 570:
1066
--- leaf 571:
1067
1068
```


## [2026-09-05T20:34:33.693Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/leaf.py data/verification/sources/refs/TAD_pages.txt 128 1015; cd data/verification/sources/refs; echo \"=== leaf 8 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==9' TAD_pages.txt | head -40"
}
```


### [2026-09-05T20:34:35.486Z] TOOL RESULT

```
data/verification/sources/refs/TAD_pages.txt line 128 -> 0-based leaf 4
data/verification/sources/refs/TAD_pages.txt line 1015 -> 0-based leaf 28
=== leaf 8 ===
                             ‫|قنوم ارامية ‪ 9 72‬قَدُوما ‪ 4‬معناه الشخص‬
 ‫في الفارسية ل‪2‬نكر» وفىاليونانية اله عرببها المرساة والموجل‬           ‫اجر‬

 ‫جيل يوناني‪#‬وألعههدوع (إوتجيليون )معناه خير بشارة وبشرى فرح‬
‫(نكليس ) عريها الجرى‬
                   ‫نقليسوحتكلس ‪ -‬يوناني ‪59‬ا‪600‬ي» إ‬
                                                               ‫والثلقوالصباور‬
        ‫هنا أراعى « عرب » أايلغرب‬
                                ‫صلةلولك‬
                                      ‫أجتا‬
                                         ‫اوريا ‏ ايطالي ‪#‬مه‬
                                ‫اوضة ‪ -‬ري وله يشارف عدر‬
‫أوقة‪ 5‬في اللددينية ‪3‬ن وفي اليونانية ‪#‬أعاىتاه براد مهاجزاء من|ثنيعشر‬

              ‫معناه مربع وعربية اليحر البط‬      ‫داتع يوناني ‪56‬‬

‫اوكاريستيا واوخاريستيا يوناني ‪2‬ناوذوداءنظا معناه نعمة وشكر أحسن‬
                                                        ‫وبراد به القريان المقكدس‬
                     ‫‪,‬نصاغوجي ‪ -‬يوناني ‪ ©8808351‬معناه مدخل وتوطئة‬

 ‫ارشّونة وقونة ‪ -‬يوناني ‪ ©7001‬معناءصورة وشبه ومثال وكثال أما نصمة في‬


‫ايطالي قجلاعناا‪ 61‬معناه لغة نفوذ وفي الطب هوالبلنمالوبابي‬          ‫إيتفاونسا‬
                                                            ‫برادفه العزلة الصدرية‬

‫إبوان عبس فارمي <ايوان» براد به قاعة الدار ومشارفها ومله الوان كدري‬




                                ‫بعش أحرها التي يشددها اللمدان ويفتحونها ويرتقولما‬
```


## [2026-09-05T20:34:40.744Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==5' TAD_pages.txt | head -50"
}
```


### [2026-09-05T20:34:42.384Z] TOOL RESULT

```
                                                                       ‫‪0‬‬
                ‫لفل ونان قلطء دمع معنأه ولابة الاسقف ورعمته‬            ‫‪١‬‬

                          ‫معناه الذهب الخالص‬    ‫‪ 3‬اوناني‪80210‬‬       ‫‪2‬‬

                                ‫برشيم‪ 6‬معناءالخرير‬   ‫‪1‬ريسم ‪--‬فارمي ‪0‬‬


                              ‫‪ 2‬بق ‪ -‬فارسى « اتريز ‪ 4‬معناه يصب الماء‬


         ‫‪ --‬فارمي وهو فتحة مربعةفيجوفها لسان تعلق بطرف الحزام‬      ‫دم‬

         ‫بلس ‪ -‬بناني ‪5‬هامطذتك معناه كذ"اب وكام وهو من امماء الثشيطان‬
     ‫ابنوس ‪ -‬فاليونانية ومدعاة وهو خشب اسود شديد الصلابة شجره ينبت‬
                          ‫افلهيند فيكون بالطبعاسمههندي‬
‫اثير ب‪-‬وناني انه ومطنانه احترق ولمع واهلوعقنددماء أعلىجهة‬
‫افليجو وأنتاها وألمعما وعندالشعراء الهواء والسماء وافليطعبليعيات بدل على‬
 ‫حالة شديدة الدقة ولكنها غاايلةعفٌيدد بزعمون انها ‪٠‬ننشرة‏ فايلكون والمادة‬
‫المحسوسة غاطدة فها ويحتمل أينكون هذا الاثير عل الماذبية أيضأ أما فيعل‬
 ‫|‬                                    ‫‪30‬‬             ‫تت‬   ‫‪0‬‬
 ‫الكتمياء فبراد بهمواد |ليةتطير وهارامحة ذكية وهى تستحضر بعزل الماء من‬
                                           ‫كمحمول‬
                                                ‫لمض‬
                                                  ‫احوا‬
                                                     ‫الكحول بأاونحاد ال‬
                         ‫معناه يزه الخلق وشر يف‬      ‫‪-‬نابي ‪56‬‬
                                                            ‫أثيل و‬

                          ‫فارسي « انخور ‪ 6‬مرادفه مأوى الدواب‬   ‫أخور ب‬


     ‫اخيول ‪ -‬وناني ‪#‬أناءة مقطوع من ‪80‬تتاءة ومعناه فق وهو نباث وصلف‬
‫رأس‬      ‫أربعحبات تشبه‬
                     ‫زهربننسجي اللونوثمره‬
                                        ‫رأبيض وصنف آخر له‬‫هر‬
                                                          ‫منه له زه‬

                                                  ‫الافعى مرادفه رأس الافعى‬

                    ‫معنأه متهم الاعتهاد‬           ‫اروذ كس ع وناني ‪5‬‬
```


## [2026-09-05T20:34:53.629Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==6' TAD_pages.txt | head -30"
}
```


### [2026-09-05T20:34:55.332Z] TOOL RESULT

```
 ‫‪--‬فينيعي وفيالعبرانية « ارحمان ‪ 6‬وهو حيوان في جوف صدفة‬       ‫اراد‬
 ‫|اكتشفه الفينيقيون فيالدهر‪ "2‬الحامس عشرقبل المسيح فصيموا بدمه الاثواب‬
     ‫الحريرية وأطلقوا الارجوان علىالثوب نفهقترجمه اليونان بلغسهم « برفير»‬
 ‫ارخون واركون ‪ -‬ووناتي ده«اعمة مناه المبتدأ والاول من كل شيء‬
                                                   ‫والرئيسوالقائدوالزعيم‬
 ‫ارضي شوكي ‪(--‬عاميةوهو أسخف وأسمج وأرك تعريب عرف حتى‬
 ‫الآن م)أخوذ من ‪4‬ناةطعناءة الافرنسية‪ ]0‬وههنذههمجنةءاة الايطالية وهذه‬
    ‫من ‪ 210362613‬الاسبانية وهذه من الخرشوف العربية وأصل منبته بلاد اليش‬
    ‫دغن ب يوناني ‪0082‬عم‪ 0:‬معناه عضو وآلهواز له طرب ذات أناييب‬
                ‫يوناني غمائه)‪ 1-162‬معناهفراش ويرومرقد جيد‬         ‫ا‬
‫أزادرخت ‪ -‬فارسي اوزادوقك معنا برس وعو اشنه شر النقنا‬
 ‫روت ح‪ -‬بوناني م ركبمن ‪ 3‬يتعنىغيرو‪ 8002‬بمعنىحي وهوغاز عنصري‬
                          ‫لا رائحةولالمول لاون وقد يدخل بتركيب الموا‪.‬‬
 ‫ايطالي ‪ 0‬عمعناه وحدة وهو ورقة من ورقاللعب ذات نقطة واحدة‬        ‫اس ‪-‬‬

 ‫إسبائخ س فارسي«اسفائغ» وهو ببقسلتةانية تشبهالسلق 'يسلق ورقها وبوكل‬
‫إسبيداج ‪ -‬قارسي « سفيداتك » سفيد في الفارسية معناه أبيض وأنّكفي‬
 ‫العبرائية معناه رصاص وهو بياض الرصاص وبال لدفيالكيميا كربونات الرصاص‬
                                    ‫استاذ فارمي «استاد معناه مع‬
‫يوناني ‪ 761818‬تاد أزانفة وهو لقنفضة كان يساوي فى أثينا‬          ‫إستار‬
      ‫ْ‬                                                       ‫أربعة دراهم‬
                                               ‫)‪ (0‬سى بالدهر مأئة سئة‬
```


## [2026-09-05T20:34:58.644Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==7' TAD_pages.txt | head -30"
}
```


### [2026-09-05T20:35:00.365Z] TOOL RESULT

```
‫معاه أخبار تارمحية وقد استعمابا العرب ععى‬           ‫اساطير ‏ بوناني ‪8‬‬
                                                            ‫خرافات وحكابات‬
                                     ‫استبرق ‪ -‬فارسي معناه الديباج الغديظ‬
                                   ‫اسرب ‪ -‬فارسي «سيرب» معناه رصاص‬
        ‫إسطيل واصطيل ‪ -‬لاتيني ‪#‬دااناطهاة معناه مأوى الخيل والدواب‬
‫خا لان | رانم كن من ‪ 807653‬أى ك كب وهلاةطه‪:‬ذا أُخذ وكان‬
 ‫الفلكيون القدماء يعرفون حركة الكوكب مبذه الآلة ويعينورن موضعه‬
                                                             ‫ويعيسون ارتقاعه‬

                       ‫يونالي تاواع ‪ 1015‬معئاه عنصر وأعيل‬     ‫ب‬
                                                                      ‫د‪5‬ي‬
                                                                        ‫‪95‬‬

                    ‫معتأد عله حربية وطائفة سفن‬      ‫اسطول ‪ 8-3‬وناني ‪8‬‬


‫ملدابةمرادفهمودوقابمة‬
                    ‫اسطوانة ‪ 5-3‬فارسي ‪ 0‬أستون « هماه دعامة وقوات ا‬


                                                            ‫ايضا فيالطبيعيات‬
‫نحري جسمه متخلخل‬          ‫اون‬
                            ‫و وه‬
                               ‫ينعصر‬
                                   ‫حه م‬
                                      ‫معنا‬          ‫إمفنج ‪ -‬يوناني ‪5‬‬



‫يوناني وومزمء ‪5‬أمء معناه فى الاصل الملاحظ والمدير وفى عرف‬          ‫انيف‬
```


## [2026-09-05T20:35:15.280Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -c \"\" MON_part1.txt; grep -n \"سکوبا\\|اسقوف\\|سقوبا\" incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head; echo \"=== ARY ===\"; grep -n \"اهریمن\\|اسقف\" incoming/ARY/ARY_pages.txt | head"
}
```


### [2026-09-05T20:35:15.362Z] TOOL RESULT

```
99339
=== ARY ===
2804:۸ اهریمن ‏ :
```


## [2026-09-05T20:35:16.936Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== LKT bishop/episcopus ===\"; grep -n -i \"episcop\\|Bischof\" LKT.txt | head -8; echo \"=== AFM اسقف ===\"; grep -n \"سقف\" AFM_pages.txt | head -5; echo \"=== FVQ ===\"; grep -n -i \"usquf\\|episcop\" FVQ.txt | head -5"
}
```


### [2026-09-05T20:35:17.012Z] TOOL RESULT

```
=== LKT bishop/episcopus ===
2403:1006.  Ar.  kä'id: 'Befehlshaber'  [vom  Vb.  käda  'leiten, regieren'];  hieraus  mit  ar.  Art.  sp.  al- caide  'Kommandant  einer  Festung',  pg. 'dass.,  Richter'  [infolge  Kontamination mit  al-kadiy  s.  hier  Nr.  984],  engl,  al- caide,  alcalde  'Festungskommandeur, höchster  Zivilbeamter  einer  Stadt;  Ge- fängniswärter'; siz.  caJiiM 'Rädelsführer' [alt  gaitu  'Richter'],  kat.  sp.  cayado, gayato,  pg.  cajado  'Hirten-  oder  Bischofs- stab' [da  der  Hirle  das  Haupt  oder  der Führer  seiner  Herde  ist].  |DE  79. Eguilaz  126.  ML  6898.  GrSVociSic 229.  GIBBS  in  American  Journal  of Science  &  Arts  XXXIII,  324.
=== AFM اسقف ===
221:2 وهو بعناه ويطاق ايضاً على سقف المت 8 قرن .0 به اليونالي 00
=== FVQ ===
```


## [2026-09-05T20:35:24.113Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '2795,2815p' incoming/ARY/ARY_pages.txt; echo \"=== leaf ===\"; python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/leaf.py incoming/ARY/ARY_pages.txt 2804; grep -n \"\\[pdf page\" incoming/ARY/ARY_pages.txt | sed -n '1,2p'"
}
```


### [2026-09-05T20:35:25.749Z] TOOL RESULT

```
ارمنی (۵//547/۸۷): ال
یه لین ووتمم: 006 رقن شاناه‌تآرهنای پسگشت‌ها 333
اسلاوی که (0ملاً نات صم: 6 ق۶030
071 :00 ,121117 رتا[ن12 0 (13872728) مد هام
لهستانی (5ا۳0): و زرد ۱2 9 (8[105) 802
روسی (8514(4نا): تا[نا12 ,لل1نا029 0 (0۲) #مقلو
ینوا نی ما71 5ل): 0 ,۸۷1 برهان قاطع : ۱۳۸
۸171 فرهنگ معین : ۳۵
[pdf page 97]
۸ اهریمن ‏ :
یادداشت.
۱ چون هیچکدام از پسگشت‌ها به رابطه‌ی واژه‌های فارسی و پهلری وکردی این فهرست با واژه‌ی اوستایی و دیگر
واژه‌های آن اشاره‌ای نکرده‌اند» در جلو واجریشه‌ی هند و اروپایی (شاید) آورده‌ام را
۲ واژه‌های لاتین 13۷0-0771۸88 (به چم "لاس" و آپوشاکه) و 8807۷1۸8 (به چم "پرست منار و یروا هن
آلباس") نیز از همین ربش‌اند. ۹
۳ چم اکثر واژه‌های غیرایرانی اين فهرست: پوشا کد» پوشیدن» کفش. :
اوستایی (488740): ,۸00 آلمانی کهن (0274۸00 107 صان):
۸ ۸۷63۸ ,11۸18۲55 61 ,۸۸6
پهلری (1/ماللمه): آلمانی (0874/۸00): نداد
۸13۸1 ,۸13813۸۵ انگلیسی کین (5#لا2۷0 صا): 8۲05
۱ سانسکریت (54(/872077): 1 انگلیسی (۸/01/870): ۸
=== leaf ===
incoming/ARY/ARY_pages.txt line 2804 -> 0-based leaf 96
1:[pdf page 1]
10:[pdf page 2]
```


## [2026-09-05T20:35:32.593Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==98' incoming/ARY/ARY_pages.txt | head -40"
}
```


### [2026-09-05T20:35:34.345Z] TOOL RESULT

```
[pdf page 98]
اهورا هرمز اهورامزدا / ۹۹
چم این واژه در زبان ابلندی کهن: اندوه» غم.
ریشه‌ی اوستایی این واژه دارای دو بخش است» بخش نخست آن در این ,فهرست پیگیری شده است» برای
شناخت بخش دوم آن به آمنش " بازگشت شود.
ِ
اوستایی (//472374): ۰ برشقاناتل۸ ,دلاقل۸ 055
۸ نررس کهن (۸/078 010): وق
پارسی باستان (/(۳8۵]۸ 010): ۰ بشااتا۸ انگلیسی کهن (تلولسا8۸0 010): 08
۸۸3/۸70۸3
پهلوی (1اتلمم): 0۸0 پسگشت‌ها شرت دی
00 2000
سانسکریت (54(79807): ,8ناقم وتاق۸ 31 بطل2/ 2/۸02
۸ + ۶۲۵۶ ال ب‌لقطلله ۱
پرنانی 076220): 5 41 (ت51ه) ۱
گوتیکه (007[7/0): 8 ,۸۷855 برهان قاطع + ۹ ۱
ایسلند ی‌کهن (070۸1۸7/(م5 0ا0): 0
اوستایی (4/:37۸4): 10۸ پرتغالی (۳0/71701888): آتا۸0
پارسی پاستان (۷(ای۳8 ۰۰:۵۵ ۸۲۸ ابرندی کهن (تتکلها صا۵): 10
۲ پهلری (۸(1ات۸): ۰ 8۸۷-۰ ,50۸3 ,3:۸3 گالی (5لله0): 0
۹ "کرد (68[/8: ,۷1۸ ,160۸ بشا1[13
ا سانسکریت (5/580007): ۰۰ ب8ل1 با17۸738[ پسگشت‌ها 5
۸ 9 ت20
یرنانی 076870): 17۸[ 7 (161) :ما05
لاتین (7100مل): از 30 :۱25
فرانسه (۳88(07): 1 5 (118۳) ۸/700
اسپانیایی (۸/18[3ط6): ۸01 برهان قاطع : 1۹۳
ایتالیایی (۷(فله)): 011
```


## [2026-09-05T20:35:41.590Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==97' incoming/ARY/ARY_pages.txt | tail -30"
}
```


### [2026-09-05T20:35:43.337Z] TOOL RESULT

```
۸ اهریمن ‏ :
یادداشت.
۱ چون هیچکدام از پسگشت‌ها به رابطه‌ی واژه‌های فارسی و پهلری وکردی این فهرست با واژه‌ی اوستایی و دیگر
واژه‌های آن اشاره‌ای نکرده‌اند» در جلو واجریشه‌ی هند و اروپایی (شاید) آورده‌ام را
۲ واژه‌های لاتین 13۷0-0771۸88 (به چم "لاس" و آپوشاکه) و 8807۷1۸8 (به چم "پرست منار و یروا هن
آلباس") نیز از همین ربش‌اند. ۹
۳ چم اکثر واژه‌های غیرایرانی اين فهرست: پوشا کد» پوشیدن» کفش. :
اوستایی (488740): ,۸00 آلمانی کهن (0274۸00 107 صان):
۸ ۸۷63۸ ,11۸18۲55 61 ,۸۸6
پهلری (1/ماللمه): آلمانی (0874/۸00): نداد
۸13۸1 ,۸13813۸۵ انگلیسی کین (5#لا2۷0 صا): 8۲05
۱ سانسکریت (54(/872077): 1 انگلیسی (۸/01/870): ۸
(۵(18-813801) -ناتتان۸ بشاانا ۸/28 هلدی (ل0770): 16
17 ,ک۸ا۸2 ایرلندی کهن (574ل18 010):
ارمنی (/(4/8714): ۸ 06 00005
برنانی 088/0): ۸076173181 ,۸1071181 سلتی (کلتی) (۴8776): ۸16 ,6تآه۸ت[8
لاتین ((7ضا):
5 ,۸008 ,۸1087115 دا6ن۸ پسگشت‌ها گر
فراسه (۳۸/04): 1555 60 0و2
ایتالیایی (/(۸لمله): ۸0501۸ 4 (۸(08) +17
پرتغالی (۳0717010295): ۸015۸ 7 (۸111۸) ۸/21
گرتیک (00771/6): ۸۳۷0۷۷5 ,۸001۷108 :010/5
ایسلندی کهن (0107۸74۸(ه52 0ا0): 7 (1اقاآناع اند م1658ه۸)
7 ب۸۷0 برهان قاطع : ۸۹
ساکسونی کهن ((54340 ا0): 6
یادداشت:
۱ چم این واژه در زبان‌های رومانس: تنگی‌خاطر» تشویش.
چم اين واژه در زبان‌های ژرمنی: ننگی؛ تنگه» باریکك.
چم این واژه در زبان انگلیسی نوین: خشم.
```


## [2026-09-05T20:35:58.942Z] TOOL CALL #58: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-05T20:35:58.947Z] TOOL RESULT

```


```


## [2026-09-05T20:36:03.680Z] TOOL CALL #59: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D9%87%D8%B1%DB%8C%D9%85%D9%86",
 "prompt": "Give the full etymology section for Persian اهریمن (Ahriman): the Middle Persian form, the Avestan source, and any Proto-Indo-European root proposed for aŋra-. Quote verbatim."
}
```


## [2026-09-05T20:36:05.978Z] TOOL CALL #60: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%B5%CF%80%CE%AF%CF%83%CE%BA%CE%BF%CF%80%CE%BF%CF%82",
 "prompt": "Give the etymology of Ancient Greek ἐπίσκοπος (epískopos): its components, meaning, and the list of descendants/borrowings into Latin, Syriac, Arabic, Persian and Armenian. Quote verbatim."
}
```


### [2026-09-05T20:36:08.596Z] TOOL RESULT

```
# Etymology of Persian اهریمن

Based on the Wiktionary content provided, here is the complete etymology section:

The entry states: **"Inherited from Middle Persian _ʾhlmn'_ (/⁠ahreman⁠/)."**

Unfortunately, the webpage does not include information about the Avestan source or any Proto-Indo-European root proposed for the *aŋra-* element. The etymology section is limited to the Middle Persian ancestor, without deeper historical linguistic details that would show the connection to earlier Zoroastrian terminology or Indo-European roots.

To obtain comprehensive etymological information including Avestan forms and PIE roots, you would need to consult more specialized linguistic or religious studies sources beyond what this Wiktionary entry provides.
```


### [2026-09-05T20:36:12.592Z] TOOL RESULT

```
# Etymology of Ancient Greek ἐπίσκοπος (epískopos)

## Components

The word combines:
- **ἐπί** (epí) - "upon/over" (from Proto-Indo-European *h₁épi)
- **σκοπός** (skopós) - derived from the root *speḱ- meaning "to look/see"
- The suffix **-ος** (-os) for masculine nouns

## Meaning

The word literally means "one who looks upon" or "overseer/watcher," which evolved to mean "bishop" in Christian contexts.

## Descendants Listed

The Wiktionary entry only documents descendants into:
- **Ottoman Turkish**: piskopos
- **Turkish**: piskopos
- **Romanian**: episcop

**Note**: The page does not provide information about borrowings into Latin, Syriac, Arabic, Persian, or Armenian. While the word eventually entered these languages historically, this particular Wiktionary entry limits its documented descendants to the languages listed above.
```


## [2026-09-05T20:36:17.530Z] TOOL CALL #61: WebFetch

```json
{
 "url": "https://www.iranicaonline.org/articles/ahriman",
 "prompt": "What does this article say about the etymology and forms of Ahriman: the Avestan Aŋra Mainyu, the meaning of aŋra-, the Middle Persian and New Persian forms? Quote key sentences."
}
```


## [2026-09-05T20:36:18.650Z] TOOL CALL #62: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/bishop",
 "prompt": "Give the full etymology of 'bishop' verbatim, including Greek episkopos, Latin episcopus, Late Latin/Vulgar Latin ebiscopus/biscopus, and Old English biscop."
}
```


### [2026-09-05T20:36:19.827Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-05T20:36:25.528Z] TOOL RESULT

```
# Etymology of Bishop

The word "bishop" traces its lineage through several languages:

**Greek Origin:** The root is Greek *episkopos*, meaning "watcher, (spiritual) overseer," combining *epi-* ("over") + *skopos* ("one that watches").

**Latin Stage:** This became Late Latin *episcopus*, which the Church adopted as a title for ecclesiastical leaders.

**Old English:** The word entered English as *bisceop*, borrowed from the Latin form.

**Romance Language Variants:** Late Latin *episcopus* evolved differently across languages—Spanish *obispo*, Italian *vescovo*, and French *évêque* each developed distinct forms from the same root.

**Germanic Spread:** Old Saxon *biscop* and Old High German *biscof* show the word's adoption in Germanic languages.

The entry notes this represents "a curious example of word-change," as English and French versions derived from the same source "not to have a letter in common," with English dropping initial and terminal syllables while French softened consonants.
```


## [2026-09-05T20:36:29.133Z] TOOL CALL #63: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A3%D8%B3%D9%82%D9%81",
 "prompt": "Give the etymology of Arabic أسقف (usquf) 'bishop' verbatim: source language (Greek/Syriac), intermediate Syriac form, and descendants (Persian, Turkish, etc.)."
}
```


## [2026-09-05T20:36:30.909Z] TOOL CALL #64: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/anhras",
 "prompt": "Does this page exist? If so give the reconstruction, meaning and etymology (PIE root) for the Proto-Iranian word behind Avestan aŋra- 'evil'."
}
```


### [2026-09-05T20:36:32.827Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-05T20:36:35.029Z] TOOL RESULT

```
# Etymology of Arabic أسقف (usquf) 'Bishop'

**Source Language:** Ancient Greek *ἐπίσκοπος* (epískopos)

**Intermediate Form:** The word traveled through Classical Syriac *ܐܦܣܩܘܦܐ* (ʾeppisqoppā) before entering Arabic.

**Key Descendants:**

- **Persian languages:** Classical Persian, Dari, Iranian Persian, and Tajik adopted *usquf*
- **Turkic:** Ottoman Turkish *اسقف*, modern Turkish *üskuf*
- **Malay/Indonesian:** *uskup* (borrowed from Arabic via Persian)
- **Swahili:** *askofu*
- **South Asian:** Hindi and Urdu variants (*asqaf*)
- **Cypriot Arabic and Maltese:** Local Arabic dialect forms (*iskof*, *isqof*)

The word ultimately derives from Proto-Indo-European roots related to "seeing" or "watching," reflecting the episcopal role of oversight in Christian tradition.
```


## [2026-09-05T20:36:41.486Z] TOOL CALL #65: WebSearch

```json
{
 "query": "Avestan aŋra- \"evil\" etymology Proto-Indo-European *h₂enǵʰ- angra mainyu narrow anger"
}
```


## [2026-09-05T20:36:42.118Z] TOOL CALL #66: WebSearch

```json
{
 "query": "سکوبا شاهنامه اسقف سریانی معرب episcopos فردوسی"
}
```


### [2026-09-05T20:36:50.612Z] TOOL RESULT

```
Web search results for query: "سکوبا شاهنامه اسقف سریانی معرب episcopos فردوسی"

Links: [{"title":"اسقف - معنی در دیکشنری آبادیس","url":"https://abadis.ir/fatofa/%D8%A7%D8%B3%D9%82%D9%81/"},{"title":"اسقف به انگلیسی - معنی در دیکشنری آبادیس","url":"https://abadis.ir/fatoen/%D8%A7%D8%B3%D9%82%D9%81/"},{"title":"اسقف - ویکی‌پدیا، دانشنامهٔ آزاد","url":"https://fa.wikipedia.org/wiki/%D8%A7%D8%B3%D9%82%D9%81"},{"title":"اسقف | در فرهنگ لغات ها (دهخدا،معین و ... ) + سایر منابع اطلاعاتی | جدول یاب","url":"https://www.jadvalyab.ir/fa2fa/%D8%A7%D8%B3%D9%82%D9%81"},{"title":"واژه نامه شاهنامه - کلمه ها و عبارات بخش پادشاهی اسکندر - ویکی شاهنامه","url":"https://wikishahnameh.com/%D9%88%D8%A7%DA%98%D9%87-%D9%86%D8%A7%D9%85%D9%87-%D8%B4%D8%A7%D9%87%D9%86%D8%A7%D9%85%D9%87-%DA%A9%D9%84%D9%85%D9%87-%D9%87%D8%A7-%D9%88-%D8%B9%D8%A8%D8%A7%D8%B1%D8%A7%D8%AA-%D8%A8%D8%AE%D8%B4-%D9%BE%D8%A7%D8%AF%D8%B4%D8%A7%D9%87%DB%8C-%D8%A7%D8%B3%DA%A9%D9%86%D8%AF%D8%B1/25543/"},{"title":"شهربَراز: نام رسته‌های کلیسایی","url":"http://shahrbaraz.blogspot.com/2011/01/blog-post_16.html"},{"title":"قصیده ترسائیه خاقانی – فصلنامه فرهنگی پیمان","url":"https://paymanonline.ir/%D9%82%D8%B5%DB%8C%D8%AF%D9%87-%D8%AA%D8%B1%D8%B3%D8%A7%D8%A6%DB%8C%D9%87-%D8%AE%D8%A7%D9%82%D8%A7%D9%86%DB%8C/"},{"title":"نام رسته‌های کلیسایی | Shahrbaraz / شهربراز","url":"https://shahrbaraz.wordpress.com/2011/01/16/%D9%86%D8%A7%D9%85-%D8%B1%D8%B3%D8%AA%D9%87%E2%80%8C%D9%87%D8%A7%DB%8C-%DA%A9%D9%84%DB%8C%D8%B3%D8%A7%DB%8C%DB%8C/"}]

Based on the search results, I can provide you with information about this Persian/Arabic linguistic query:

The word "اسقف" (asqaf - bishop) is an Arabic word that comes from the Greek "Eπίσκοπος / episkopos". Iranians borrowed this word from Syriac and called it "سکوبا" (skoba), and the same meaning appears in Ferdowsi's Shahnameh.

Ferdowsi used "سکوبا" (skoba) in the Shahnameh in a general sense, as evidenced by the verse: "They wrote letters to every ruler - skoba and patriarch of every land," and scholars like Saeed Nafisi and Mohammad Ma'in have pointed to this meaning and the correct etymological root.

In English, these terms are known as "Bishop," which is the highest religious position in Christianity, generally assigned to administrative and supervisory duties.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-05T20:36:51.188Z] TOOL RESULT

```
Web search results for query: "Avestan aŋra- "evil" etymology Proto-Indo-European *h₂enǵʰ- angra mainyu narrow anger"

Links: [{"title":"AVESTAN LANGUAGE ii. The phonology of Avestan - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/avestan-language/avestan-language-ii-the-phonology-of-avestan/"},{"title":"Indo-European etymology : Query result","url":"https://starlingdb.org/cgi-bin/response.cgi?root=config&basename=%2Fdata%2Fie%2Fpiet&text_number=1280&single=1"},{"title":"Aeshma","url":"https://en.wikipedia.org/wiki/Aeshma"},{"title":"Proto-Indo-European mythology - Wikipedia","url":"https://en.wikipedia.org/wiki/Proto-Indo-European_mythology"},{"title":"Proto-Indo-Iranian language - Wikipedia","url":"https://en.wikipedia.org/wiki/Proto-Indo-Iranian_language"},{"title":"Etymology of Some Demononyms in the Uzbek Language","url":"https://scientificbulletin.com/index.php/AJOUP/article/download/1940/2058/2671"},{"title":"Ahriman — Grokipedia","url":"https://grokipedia.com/page/Ahriman"},{"title":"www.academia.edu","url":"https://www.academia.edu/35712370"}]

Based on the web search results, here's what I found regarding the etymology of Avestan aŋra- "evil":

The term aŋra- "evil" in Young Avestan developed through a phonological change where medially hr became ŋr, with a Vedic cognate asrá- "painful."

Regarding the Proto-Indo-European etymology, angra- is linked to concepts of affliction, constriction, or anger, possibly deriving from Proto-Indo-European *h₂enǵʰ- ("narrow" or "tight"), evoking a sense of binding harm.

The term aŋra- appears as part of the compound Avestan aŋra-mainyu-, which developed through medieval forms such as Ahriman/Ahremen and persists in modern Iranian languages. The Avestan compound Angra Mainyu literally translates to "destructive spirit" or "evil mind," with angra denoting "destructive," "hostile," or "evil," and mainyu signifying "spirit," "mind," or "mentality."


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-05T20:37:02.303Z] TOOL CALL #67: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%B3%DA%A9%D9%88%D8%A8%D8%A7/",
 "prompt": "Quote the dictionary entries for سکوبا, especially the فرهنگ معین (Mo'in) and لغت‌نامه دهخدا entries, including any etymological tag (origin language) and the Shahnameh verse."
}
```


## [2026-09-05T20:37:04.445Z] TOOL CALL #68: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82en%C7%B5%CA%B0us",
 "prompt": "Does this page list Avestan aŋra- or Sanskrit aṃhu-? Give the reconstruction, meaning and the Indo-Iranian descendants."
}
```


### [2026-09-05T20:37:06.579Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-05T20:37:08.553Z] TOOL RESULT

```
# Dictionary Entries for سکوبا

**Farhang-e Mo'in (Mo'in Dictionary):**
"(سُ) (اِ.) اسقف" — indicating the word means "bishop."

**Loughetnāme-ye Dehkhoda (Dehkhoda Dictionary):**
"نام مرد ترسا" (a man's name) and "نام راهبی است که حضرت عیسی مسیح بدیر او رفته به آسمان صعود کرد" — referring to a monk at whose monastery Jesus Christ ascended to heaven.

**Shahnameh Reference (Ferdowsi):**
One verse demonstrates usage: "سکوبا و رهبان سوی شهریار / برفتند با هدیه و با نثار" — depicting clergy traveling to a ruler with gifts.
```


## [2026-09-05T20:37:16.913Z] TOOL CALL #69: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82en%C7%B5%CA%B0-",
 "prompt": "Give the reconstruction, meaning, and the full descendant list, especially any Indo-Iranian (Avestan, Sanskrit) forms. Does it mention Avestan aŋra- or ązah-?"
}
```


## [2026-09-05T20:37:17.915Z] TOOL CALL #70: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A7%D8%B3%D9%82%D9%81/",
 "prompt": "Quote the فرهنگ معین (Mo'in) entry for اسقف including its bracketed origin tag, and any Dehkhoda note on the word's Greek/Syriac origin."
}
```


### [2026-09-05T20:37:23.045Z] TOOL RESULT

```
# Proto-Indo-European Root *h₂enǵʰ-

**Reconstruction:** *h₂enǵʰ-

**Meanings:** The root conveys three related senses:
1. To constrict, tighten, compress
2. Narrow, tight
3. Distressed, anxious

**Notable Descendants:**
- Ancient Greek: ἄγχω (ánkhō, "I compress, strangle")
- Latin: angō ("I cause pain"); angustus ("narrow, close"); ānxius
- Proto-Germanic: *angustiz ("narrowness, tightness, anxiety")
- Albanian: angësht
- Old Armenian: անձաւ (anjaw)
- Proto-Slavic: *vę̄zàti

**Regarding your specific inquiry:** The page does not mention Avestan aŋra- or ązah-. Additionally, no Indo-Iranian descendants appear in the derived terms list provided. The documentation focuses primarily on Hellenic, Italic, and Germanic reflexes, with limited other language family coverage.
```


### [2026-09-05T20:37:23.780Z] TOOL RESULT

```
# فرهنگ معین Entry for اسقف

**فرهنگ معین definition:**
"(اُ قُ) [معر.] (اِ.) از یونانی گرفته شده به معنای پیشوای عیسوی که مرتبه اش"

The entry indicates the word derives from Greek, meaning a Christian leader whose rank exceeds that of a priest.

**Dehkhoda note on origin:**
The Dehkhoda section mentions the term originates from the Greek root *episkopos*, meaning "overseer," and notes that Iranians also derived a variant form (*skooba*) from the Syriac version of this same Greek word, which appears in the Shahnameh with comparable significance.
```


## [2026-09-05T20:37:37.440Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== BRT aipi ===\"; grep -n \"aipi\\b\\|• *j\\. *aipi\" BRT.txt | head -8; echo \"=== BRT aipi.ereta ===\"; grep -n \"aipi\\.\\|aipi-\" BRT.txt | head -12"
}
```


### [2026-09-05T20:37:37.506Z] TOOL RESULT

```
=== BRT aipi ===
2930:•  j.  aot-  V.,  nur  mit  aipi  'begreifen'. Frxes.  2  aota-.
3656:aipi
3670:Vgl.  aipi,  apaya,  apqm  und  lum  Ausgang  aoe.
3680:•  j.,  g.  aipi,  p.  apiy  I)  Adv.  i)  'dazu auch,  desgleichen  auch',  ein  neues  Subjekt anreihend,  von  dem  die  gleiche  Aussage gilt:  at  yuS  dasva  .  .  akät  mananhs  sl<l cihr^m  . .  yasca  vä  . .  yazatte  . .  ^yaotnqm 'pl  daibitilnn  yäis  ..  "..  desgleichen  auch die   (eure)  Taten,    durch   die  . ."  Y.32.
3682:83  aipi  I  2  a
3684:sa3^3rJ{iA.)  . .  ya  ..  vav}r?SSi  pairlJült ..  yäia  var?^aitg  '/LcTblJ  Y.  25,4;  — ai^qmät  ä  ahtnJ  .  .  vTci>3i  (sd.)  -/)"■■>  Y. j2. 8.  a)  mit  Neg.;  'nicht  hinfort  mehr, länger":  »»3  ^I^ä  *fX  äsbävayal  (sd.)  Y. Jt.i7.  3)  'auch,  gar,  besonders',  das vorherg.  Wort  hervorhebend:  maS^a  .  . pirs^u  'pi  ffi/ajii/Vjy  "die  Wolken,  die  sich gar  weithin  verbreiten"  YLA40;  io.44; —  \daraiy  'piy  "gar  fernhin"  X.7. 2;  D, 6'.a,  4";  —  ai'e  °pi  dai'jyanlS  "'äx£  y^a^ besonders  hinsehend"  Yt/0.45;  45;  — *avat  'pi  ya^a  . .  "soviel  gerade  (,  eben) aIs.."V.ö'.io;22,Äa3,J7.7.  I^Praen. 1)  mit  Akk.  a)  'über  —  hin';  a)  zeitlich: dar>-^3mHt  °pi  zrvätam  Y.  6-1. 3 ;  Yt  i^. aö,  ß)  räumlich:  vTspqmHl  'pi  imqm  sqm Y. 57.33; — liuire fraväitUßA.)  tq%ryqm  °pi xSapamm  Yt  74. 1 3 ;  —  yavat  anu  "pi  *i}iti garayS  visasiar?  vlsptm  aval  °pi..  "so  gross der  Raum  ist,  über  den  hin  sich  die  üerge erstrecken,  über  all  den  Raum  hin  . ." Yt. 7p.8.  b)  'bei':  k?m  ksm  °pi  nmäm "bei  Jedem  im  Haus"  Yt.  5. 102.  2)  mit Lok.  'bei',  zeitlich:  mi^nm ..yahmi  ssire m%%rS.dru}5  'pi  %n<isi  paun'a{sA.)  masyS- kunhs  ". .  bei  dessen  Gericht  . ."  Yt.  lo. 8of?).  3)  mit  Instr.  'nach',  zeitlich: s.  aipi  tä,  aipi  taiS  bes.  III)  Praev. {m\\.kan',  karat-,  gart-,  gam-,  vai-,  varpi- ua.).  [IIBh.4.8:  lies  utämaty^'»; —  Y.
3687:•  j.  aipi.awra-  Adj.  (fem.  °rä-)  'bewölkt': iq'iryaiHt  haca  xsafnS  .  .  "rayü  Yt  14.. 31  •>.
3689:•  j.  *aipi.9r«tö.-gitav- ')  Adj.  (auch  fem.) 'der  einen  fest  bestimmten,  fest  zugewie- senen Platz  hat  (,  den  er  nicht  verlassen darf)':  yat  ahmt  nmJne..  nilirika  daxsta- vaitj  anhat  yat  v.l  *sk^dS.aipi.jatS [pisirsY'>  'tus  (NSf)  "wenn  in  dem  Haus . .  eine  Frau  die  Regel  hat''  oder  wenn sie  wegen   eines   ihr   zugefügten  körper- 1
=== BRT aipi.ereta ===
3687:•  j.  aipi.awra-  Adj.  (fem.  °rä-)  'bewölkt': iq'iryaiHt  haca  xsafnS  .  .  "rayü  Yt  14.. 31  •>.
3689:•  j.  *aipi.9r«tö.-gitav- ')  Adj.  (auch  fem.) 'der  einen  fest  bestimmten,  fest  zugewie- senen Platz  hat  (,  den  er  nicht  verlassen darf)':  yat  ahmt  nmJne..  nilirika  daxsta- vaitj  anhat  yat  v.l  *sk^dS.aipi.jatS [pisirsY'>  'tus  (NSf)  "wenn  in  dem  Haus . .  eine  Frau  die  Regel  hat''  oder  wenn sie  wegen   eines   ihr   zugefügten  körper- 1
3690:aipi.daßdav-
3694:•  j.  '''aipi.karata'^  Inf.,  mit  asii  'er  ist eingedenk,  hat  Acht  auf  — '  (Gen.):  vis- paz'a  vilcS  mazds.fraoxta  .  .  ySi  huiti  "la dusmatahe  ".  .  die  Acht  haben  auf  das, was  übel  gedacht  ist"  Y.  71.7;  7*.
3696:•  j.  aipi-dara- Adj. 'hinterhergehend':  'n (NSm.)  nqma  ahmi  YtJ5.45.
3698:•  j.  aipLJatay-  f  i)  'Einschlagen  auf —' (Akk.):  'IS  (LS.)  gqm  hufJnA^m  ya'ia ra'^oFstä  "im  Einschlage^  auf  das . .  Rind (ist  der  Hund)  wie  der  Krieger"  V.  j  j, 4S(?).  a)  'Schlagen,  Zufügen  durch Schlag'  (nur  Komp.).  °jaiti  als  Inf. sbes.         [V.5.59:  lies  sk3nd0.aipi.jats.]
3700:•  j.  *aipi.Jaiti"  Inf  'einzuschlagen  auf—, zu  erschlagen':  i'ia  mi'inilt  daiiia  0°  ,  , gundayäi  (sd.)  ", .  um  auf  die  D.  einzu- schlagen , .""  V.J.32.
3709:•  j,  aipi.dahyav-  Adj.  (auch  mask.)  'der hinter  dem  Land  ist' ;  mi'i^r.in  pairi.dahyiim .  .  'yütn  (ASm.)  Yt  to.  1 44.
3713:aipi.dvanara-
3718:„^..,   .gl.  aipi.mvra;  yt  14.  31-  |0-S.  49-
3720:•j.aipi-«bao)^-Adj.'hLnterhereinbiegend';  ,;„„.„_  „p.  vgl.  0*^/01.  (■tjhwanger').  - •7?  (NSm.)  nama  ahmi  Yt  /5. 45.  ■)  Vgl.  Pü.  zu  apu%rya:
3723:.  y  aipi-paramna-  Ad,.,  PPM.;  s.  l^i^.    ,  ^^^^.  „^j^^  p^^,_  ^jj^  j^g^  kinderlos  ist"
```


## [2026-09-05T20:37:38.885Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== LEW ob ===\"; grep -n \"^ob\\b\\|ob, Präp\\|ob 'gegen\" LEW_1910.txt | head -5; echo \"=== LAT ob ===\"; grep -n \"^ob\\b\" LAT.txt | head -5; echo \"=== SYN epi ===\"; grep -n \"epi, opi\" SYN.txt IEC.txt | head -5"
}
```


### [2026-09-05T20:37:38.965Z] TOOL RESULT

```
=== LEW ob ===
=== LAT ob ===
10644:ob causa*; et par un affaiblissement continu, en est arrive A se sub-
14869:ob il figure, et il n'a cessi d'etre usuel. Particulibrenent friquent
28910:ob-, prae-, pro-, re- M.L.7189, sub-, super-, tra-iecto, M.L.8843,
38615:ob moenia offerre imperat" . Terme technique de sens plus large que
41353:ob eam rem noxam nocuerunt', et Dig., 5 °>i 6,338 0 3, noxae appellatione
=== SYN epi ===
```


## [2026-09-05T20:38:27.457Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== BRT arika ===\"; grep -n \"arika\" BRT.txt | head -5; echo \"=== POK ar-1 page ===\"; grep -n \"Root / lemma: ar-1\\|Root / lemma: ar-\" POK_full.txt | head -3; echo \"=== AHD ens/ans ===\"; grep -n \"^ans\\|^ens\\|hostile intent\" AHD_watkins1985.txt | head -5; echo \"=== IEC epi ===\"; grep -n \"^epi \\|epi-, prep\\|opi-\" IEC.txt | head -5"
}
```


### [2026-09-05T20:38:27.540Z] TOOL RESULT

```
=== BRT arika ===
3665:—  y!^  anyake  nairika  . .  yS  anyahe  *°ha (IS.)^  ..  a'^aurutum  *pararikacaiii  (sd.) N.  7;  77;  —  yat  he  aoxte  aisa  yeiihe  'ks hacatsuha  ms  *ana  "ka  (VS.)  N.5;  7,  *y, *io,  10 ;  —  'ktm  iiahmB.kßrpl)m  *syaokn3m.- v>r}Nm  (sd.)  V.7J.23;  ¥.2^.27.
5367:•  p,  arika-''  Adj.  'feindlich  gesinnt,  feind- sehg':  yaiia  naiy  °ka''  aham  naiy  drau- jana" . .  naiy  züra''kara''  Bh.  4. 1 3  i  —  ^/a*
6598:yä  oder_>'J(?)  vll.  sva.  'es  geschieht,  kommt vor,  dass  ..':  asit'i^  yä  *ayar3Aa^a  sparr/a (sd.)  YL/0.  laöGl.;  —  asti'*''  yS gavasnaAe (sd.)  snäuya  jya  Yt  10. 1 28  Gl.  III)  als j  Praedilcatsverbnm  (Kopula).  Das  Praedikat ist  I)  ein  Substantiv,  das  mit  dem  Subjekt im  Numerus  und  Kasus,  oder  ein  Adjektiv, das  auch  im  Genus  kongruirt.  A)  I  im Ap.  (die  Kopula  folgt  dem  Praedikat): adam  bardiyä'  amiy  .  .  adam  xsäya'iiya* amiy  Bh.  b,  h;c-f*,  h-j^,  Bh.  7.5,  11,  16', -■3>  S'  55.  13-  4.2*,  D.(t.4;  —  adam xsaya%iy£^  amiy  asagartaiy  ""uvaxstraAyä laumäyä  Bh.2.  i4,4.2,Bh.g,;  —  adamsäm xsäya^iyt^  äham  Bh. /.  6;  —  ka"bujiy<^ ,  .paruvam  idä  xsäya'^iya"  ähJ^  Bh. /.  10; —  g  *duvitäiaranam  (sd.)  vayam  xsäya- üyä  amahy  Bh.  j.  4;  —  tyaiy  paruvam xsäya'iiyä  aha"  Bh.  7.  4;  —  kalä  pa- ruviyata'  hyä  amäxam  taumä  xsäya'iiyä (sd.)  äh(^  Bh.  j.  3 ;  —  adam  pärta''  amiy D.  77. 3 ;  —  martiyJ^  Ayo*  draujana'' ahatiy  Bh.^.5,  14;  14,  5;  —  Äj'u*  daustä <Ua*.  .  hyi^  arika''  äha*  Bh. /.  8;  2.4,  6, 3-  II,  5.4;  —  tyaisaiy  fratamä  martiyä anusiyä  äha"täi'>  Bh.  ;.  13;  J.  7,  8,  11,  13, /.  7;  —  negirt:  ya^ä  naiy  arika"  äham Bh..:^.  13;  13  ^  —  ty^  adam  naiy  bardiya'' amiy    Bh.  7.  13.  B  [)    im   jAwr.    (Die
7382:•  p.  *ävä'*  Adv.  'so  lang',  mit  dem Korrelat  yävä:  ysvä  lawnü  (sd.)  ahatiy il-  avaiy  parikarä  "quamdiu  potestas  ertt, tamdiu  .  ,"  Bh.-^i5.
9196:vOstrajiqm'a  urvaranamca  ifars>S.bair-\  1  mit /a^iy 'pflegen,  Sorge  tragen  für —' yanqm  V.j,4;  —  yj  yaom  kärayeili  ÄJ'(Akk.):  imäm  dipim  ..  imaivä  patiiarä alim  k.lrayeiti  "wer  Getreide  durch  Aus- '  mätyj"  vikanühy  ylvä  (sd.)  *taum!l  ahatiy säen  anbaut,  der  baut  das  Asa  an"  '^.*svä  avaiy  parikarä  ". .  solang  pflege J.31.  isie"   Bh..^  15;    —  yadiy  .  .   utämaiy  .  .
=== POK ar-1 page ===
6622:Root / lemma: ar-1', themat. (a)re-, heavy basis are-, re- and /-basis (a)n-, rei- 
6967:Root / lemma: ar-2ex er- 
7000:Root / lemma: ar-3 
=== AHD ens/ans ===
=== IEC epi ===
3242:dhugh- “good, adequate, proper, acceptable. Cf. dhough- Ober cf. ha(m)-dugà ‘feat, record, statute’; Myc. cf. opi-suko- “an operative subject to tribute’; Olr. cf. dual, Ir. dual ‘due, proper’; OHG tugan; OE dugan; ON duga 'avail, suf- fice beside OE dogian ‘endure’; ON dugr ‘strength’; cf. also OHG tugida, tugund; OE dugup “virtue”; Venetic fugont-, fougont-; Li. cf. džiuga ‘joy’. Extn. in Gk. sukhnós “long, numerous, frequent’; OLat. duenos, Fest duo- nus; Lat. bonus. (Go. daühts ‘feast’ is of ambig. origin. See dhu£gh-)
3644:epi (pi) "on, by, at, near. WP I, 122 Skt. Av. ápi; Oss. fe-, fi-, px; Arm. h- (j-) as in h-arnem (rise: Gk. ep-órnümi, -órnu- mai; h-awraj ‘stepfather’: Gk. epi-pátor, id.); beside ev, cj. "and: Lyc. epi (ambig. “after”); Myc. & Gk. en Lat. cf. -pe in quip-pe, nem-pe, sae-pe; Umb. (?) ie-pi ‘thither’; Olr. cf. fí-ad 'in front of; OW i-ad ‘crown of
7141:keuuó (keuo), ið “hear, perceive, observe, understand’. Cf. káueio (kou-) Cypr. cf. a-keüo “tend, care for, do-keüo “watch, lurk for’; Ir. cf. do-chiu, at-chiu “I see’; OCS £ujo, čuti ‘sense, notice? beside Cuvajo, čuvati “hear, watch’ (and com. S1.); R cüju, tüjaP ‘sense’; cf. also OCS Cuvü ‘feeling’; Slovak Cuv, Cz. Civ ‘nerve’. A synthetic cpd. seems to be present in Gk. opi-pteüO ‘gaze after
11112:món- (mónios, io, iom) ‘shape, form, con- cept'. Cf. man- (Skt. ambig.), men-. Skt. (ambig.) manah ‘likeness; manam *opi- nion; intention; pride; manyah ‘respectable, seemly’; manin, adj. ‘pensive; Arm. mujn, gs muno, o-st ‘beauty’; -mujn, cpds. ‘-like’; cf. t-mujn, adj. ‘improper’; Gk. cf. mor-món, gs -mónos, m. (bugbear, lit. *death-apparit- ion"); -monion, -monía (in plant-names); Lat. -monium, -monia in sessi-? 'rood-loft, shrine’; patri-; testi-; and in caeri-monia, sancti-, the first concrete, the second abstract; Br. cf. màn, f. (appearance, person’ from *mon-? since IE -o- gives Bret. ei Cz. cf. maně, OCz. maní (Cinvoluntarily, lit. “by appear- ance); Latv. mons, m., mona, f. (“payment in kind”, cf. Lat. patrimonium). A verbal form arises in Per. manam, inf: manistan, v. fresem- ble
11966:obhi, obh- ‘athwart, against, at. WP I, 124 Skt. abhí, adv. prp. ((2) ‘toward, near, for, with- out. Isophonic with unrelated abhí ‘aroung’, see mbhi. Fusion of two roots. Thus Bois. & Kent); Av. aiwi (2), id.; OPer. abiy, id.; Hitt. (ambig.) apiya, adv. ‘there, then’; Myc. (am- big.) opi, opi- (' upon, but cf. *od-bhi: Gk. n- osphi "apart. and cf. óphata, npl. *plow-chains? if fr. *obh-mto); Lat. ob, prp. “before, op- posite, at, to, for, owing to’; OCS obf, obü ‘beyond’; Cz. cf. ob den, ob dûm “every other , . ». (Isophonic: Li. abēja *doubt': ON ef, if, n. id., efa, ifa, v. id.) (ambig.)
```


## [2026-09-05T20:38:27.668Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"^obtain,\\|^offer,\\|^oppose,\\|^omit,\" KLN_1966.txt | head -6"
}
```


### [2026-09-05T20:38:27.743Z] TOOL RESULT

```
26130:offer,  tr.  and  intr.  v.  —  ME.  offren,  fr.  earlier offrien,  fr.  OE.  offrian,  ‘to  bring  offering,  to sacrifice’,  fr.  L.  offeree,'  to  bring  before,  present, offer’,  fr.  ob-  and  ferre,  ‘to  bear,  carry’;  see bear,  ‘to  carry’,  and  cp.  words  there  referred  to. The  sense  development  of  the  English  word  was influenced  by  F.  offrir,  ‘to  offer’.  See  bear, ‘to  carry’,  and  cp.  confer  and  words  there referred  to.
26131:offer,  n.  —  ME.  offre,  fr.  OF.  (=  F.)  offre,  verbal n.  fr.  offrir,  ‘to  offer’,  fr.  VL.  *  offer  ire,  which corresponds  to  L.  offeree.  See  offer,  v. offering,  n.  —  ME.  offring,  offering,  fr.  OE.  off- rung,  ‘offering’,  verbal  n.  fr.  offrian,  ‘to  offer’. See  offer,  v.,  and  subst.  suff.  -ing. offertory,  n.,  that  part  of  the  mass  at  which  offer¬ ings  are  made;  the  offerings  themselves.  — <  Eccles  L.  offertorium,  ‘place  to  which  offerings
```


## [2026-09-05T20:38:39.335Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR>6622 && NR<6800 && /Page\\(s\\)/' POK_full.txt | head -2; echo \"=== BRT arika col ===\"; sed -n '5360,5372p' BRT.txt | grep -oE \"^[a-zA-Z°.-]+ +[0-9]{2,4}$|[0-9]{3}\" | head; sed -n '5355,5370p' BRT.txt | head -20"
}
```


### [2026-09-05T20:38:41.151Z] TOOL RESULT

```
=== BRT arika col ===
Zum
•<  Adv.
PQ.:
JaH\  Sü.;  sampärnam.  —  1)  Vgl,  Dbr.  ALS. 146.  —  ')  Eig.  'von  -  her'  sva.  'wegen,  be- treffs'. —  J)  Anders  Btkl.  AF.  2.  166,  Gd\. KZ.  27-  24*.  583,  aS.  263,  BB.  i^.  z6o.  —  ; <)  Vgl.  auch  zu  'ar-,  'ar-.
•  j.  *ar»m.uxtay  ■'  f.  'rechtes,  angemesse- nesSprechen':  *ar7m.maiH  *kumata  mamne (sd.)    "uxti    küxta     anm.varsti     kvarasta
Pu. ;  bavandak  gekoisn.  —  ')  Hds,  anm  müxr.
•  g.  ar^m.piS'wä-  f.  'Mitlag,  Mittagszeit': ks .  .  dat  ks  ya  usä  '>wj  xsajiaca  "wer (schuf)  den  Morgen,  den  Mittag  und  die Nacht?"  y.44-5.
Vel.  tafi%-^j..  ~  Eig.  'die  zum  Mahl  (vgl. filav)  passende  Zeit';  s.  Y.  g.  11.  Vgl.  lit. /ctiit  'Mittag'  und  FiCK  Wb.  i\.  80.
•  j.  *ar9m.matay- "  f.  'rechtes,  ange- messenes Denken':  -matti  *humata  mamne (sd)  *arfm.uxli  .  .  *ar;im.variii  P.  25.
Pü.:  bavandak  meitiin.  —   ■>  Ausg.  trennt.
•  j.  *aram.varstay-''  f.  'rechtes,  ange- messenes Handeln';  anm-maiti  *humata mamne{sä.)''arim.uxti . .  °ti  hvansia  P.25.
Pü. :  bavandak  kunisn.  —  ')  Ausg.  trennt. g.  arÄY.jj.  9:  lieSfl-rÄ;s.  ^ar-. j.  bm  aySnIi  FrW.  4.   1:  lies  öm  ma,'.
•  p,  arika-''  Adj.  'feindlich  gesinnt,  feind- sehg':  yaiia  naiy  °ka''  aham  naiy  drau- jana" . .  naiy  züra''kara''  Bh.  4. 1 3  i  —  ^/a*
"ka''  ski^  avam  *''ufrasatam  aparsam  Bh. /.8;  —  pasavJ'  karJ'  'ka"  abavJ'  Bh. /.  10.
AbleiL  aus  ir.  'ahta-  (j.  a,!ra-\  vgl.  aki\  — •)  Man  kann  auch  är'  und  ara/^*  lesen ;  vgl. IIORN  NpEt.  6,  Hbm.  FSt.  6.
•  j.  a-iritay-  f.  'Bekacken',  mit  Akk.  ver- bunden: 'tö  (LS.)  panliimm  ya^ä  jahika "(der  Hund)  kackt  auf  dem  Weg  wie  die Hure"  V.y.4S.
```


## [2026-09-05T20:38:52.683Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR>6600 && NR<7000 && (/Page\\(s\\)/ || /^Meaning/ || /^Root \\/ lemma/)' POK_full.txt | head -8"
}
```


### [2026-09-05T20:38:54.647Z] TOOL RESULT

```
Page(s): 67 
Root / lemma: ar-1', themat. (a)re-, heavy basis are-, re- and /-basis (a)n-, rei- 
Meaning: to move, pass 
Page(s): 55-61 
Root / lemma: ar-2ex er- 
Meaning: to distribute 
Page(s): 61
```


## [2026-09-05T20:39:06.550Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '1,120p' tools/verify_check.py"
}
```


### [2026-09-05T20:39:06.608Z] TOOL RESULT

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


## [2026-09-05T20:39:15.273Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for u in \\\n 'https://en.wiktionary.org/wiki/%D8%A7%D9%87%D8%B1%DB%8C%D9%85%D9%86' \\\n 'https://en.wiktionary.org/wiki/%CE%B5%CF%80%CE%AF%CF%83%CE%BA%CE%BF%CF%80%CE%BF%CF%82' \\\n 'https://www.etymonline.com/word/bishop' \\\n 'https://en.wiktionary.org/wiki/%D8%A3%D8%B3%D9%82%D9%81' \\\n 'https://abadis.ir/fatofa/%D8%B3%DA%A9%D9%88%D8%A8%D8%A7/' \\\n 'https://abadis.ir/fatofa/%D8%A7%D8%B3%D9%82%D9%81/' \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82en%C7%B5%CA%B0-' ; do\n python3 tools/fetch_source.py \"$u\" --note 'page 155 (Ens / Epi-Opi): ahriman, episkopos/usquf/sekuba, PIE *h2engh-' 2>&1 | tail -2; done"
}
```


### [2026-09-05T20:39:21.137Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/3df5ac2e23203c54.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3bf6c64a27b603d5.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9619e70c6866e11c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8d00de371dde26c9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/afa4cdb125b9d9f9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/70f7bc6e05a1d642.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2bf8785b7aaf20b2.txt
```


## [2026-09-05T20:41:10.913Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg155.png data/verification/sources/refs/ocr/BOOK/155.png && ls -la data/verification/sources/refs/ocr/BOOK/ | head"
}
```


### [2026-09-05T20:41:12.729Z] TOOL RESULT

```
total 5068
drwxrwxr-x  2 sfmqrb sfmqrb   4096 Sep  5 16:41 .
drwxrwxr-x 10 sfmqrb sfmqrb   4096 Sep  5 16:21 ..
-rw-rw-r--  1 sfmqrb sfmqrb  71589 Sep  5 10:46 100.png
-rw-rw-r--  1 sfmqrb sfmqrb 104864 Sep  4 19:03 101.png
-rw-rw-r--  1 sfmqrb sfmqrb  68145 Sep  5 10:49 102.png
-rw-rw-r--  1 sfmqrb sfmqrb  79623 Sep  5 10:55 103.png
-rw-rw-r--  1 sfmqrb sfmqrb  78826 Sep  5 10:59 104.png
-rw-rw-r--  1 sfmqrb sfmqrb  82500 Sep  5 11:05 105.png
-rw-rw-r--  1 sfmqrb sfmqrb  55270 Sep  5 11:03 106.png
```


## [2026-09-05T20:52:57.286Z] TOOL CALL #80: Write

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build155.py",
 "content": "# -*- coding: utf-8 -*-\nimport json, io\n\nW_AHRIMAN = \"https://en.wiktionary.org/wiki/%D8%A7%D9%87%D8%B1%DB%8C%D9%85%D9%86\"\nW_EPISK = \"https://en.wiktionary.org/wiki/%CE%B5%CF%80%CE%AF%CF%83%CE%BA%CE%BF%CF%80%CE%BF%CF%82\"\nETY_BISHOP = \"https://www.etymonline.com/word/bishop\"\nW_USQUF = \"https://en.wiktionary.org/wiki/%D8%A3%D8%B3%D9%82%D9%81\"\nAB_SEKUBA = \"https://abadis.ir/fatofa/%D8%B3%DA%A9%D9%88%D8%A8%D8%A7/\"\nAB_OSQOF = \"https://abadis.ir/fatofa/%D8%A7%D8%B3%D9%82%D9%81/\"\nW_ANGH = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82en%C7%B5%CA%B0-\"\n\ndoc = {\n  \"pdf_page\": 155,\n  \"book_page\": 125,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-05\",\n  \"entries\": [\n\n  # ============================== ENTRY 0 : Ens ==============================\n  {\n    \"entry\": 0,\n    \"root\": \"Ens\",\n    \"verdict\": \"plausible\",\n    \"modern_form\": \"Walde-Pokorny's doubtful lemma *ens- 'in feindseliger Absicht treffen' (WP I 134); dropped by Pokorny 1959 and by Watkins/AHD. Modern handbooks derive Av. aŋra- either from Proto-Iranian *anhra- < *n̥s-ro- (Bartholomae's base *ans-, kept by Kent) or connect it with PIE *h₂enǵʰ- 'narrow, constricting'.\",\n    \"note\": \"The root box is a faithful copy of the page Nourai cites. WLD Bd. I p.134 heads the article literally 'ens- „in feindseliger Absicht treffen“?' — with the question mark — and opens 'Die Gruppe ist unsicher', which is exactly what the chart's own note ('WLD expresses uncertainty about derivation of these words') reports. But the lemma has no independent life: Pokorny's IEW (1959), the revision of Walde-Pokorny, has no *ens- at all (searched POK_full.txt for the lemma), and Watkins's AHD appendix has no such root either, so 'Indo-European Ens' is a 1927 reconstruction that later comparative work abandoned. What survives of it is the Indo-Iranian base *ans- that Bartholomae posited for ạsta-/aŋra- and that Kent still uses in 1950; the competing modern proposal ties aŋra- to PIE *h₂enǵʰ- 'narrow, tight, distressing' (Lat. angustus, angor, anxius, Goth. aggwus, Eng. anguish, anger), which is the derivation Aryanpur prints under اهریمن. Everything hanging under the root box — the Avestan words, the compound, Ahriman, and Old Persian arika- — is solid; only the PIE label above them is shaky. Hence 'plausible'.\",\n    \"note_fa\": \"خودِ ریشه نقلِ دقیقی است از همان صفحه‌ای که نورایی یاد کرده است: والده–پوکورنی در جلد یکم صفحهٔ ۱۳۴ مادهٔ ens- «با قصدِ دشمنی برخورد کردن» را با علامت پرسش آورده و خود می‌نویسد «این خانواده نامطمئن است». اما پوکورنی در ویرایش ۱۹۵۹ این ماده را یکسره حذف کرده و در پیوستِ ریشه‌های هندواروپایی واتکینز نیز نیامده است؛ آنچه پا بر جاست همان ستاکِ هندوایرانی *ans- است که بارتولومه برای ạsta- و aŋra- بازساخته و کنت نیز پذیرفته است. رقیبِ امروزین این رای، aŋra- را به ریشهٔ *h₂enǵʰ- «تنگ، فشرده» (لاتین angustus، انگلیسی anguish/anger) می‌برد — همان چیزی که آریانپور ذیلِ «اهریمن» آورده است. پس در یک کلام: ادعای نورایی دربارهٔ خودِ ریشه با احتیاط پذیرفتنی است، هرچند همهٔ شاخه‌های زیرِ آن درست‌اند.\",\n    \"sources\": [W_ANGH, W_AHRIMAN],\n    \"ref_check\": [\n      {\"ref\": \"WLD1:134\", \"status\": \"supports\",\n       \"note\": \"WLD_Bd1_pages.txt leaf 142 (printed p.134, running head 'ent- — ens-'): 'ens- „in feindseliger Absicht treffen“? Die Gruppe ist unsicher. Man könnte an einen Zusammenhang folgender Wörter denken: ai. asanā „Wurfgeschoß“ ... Dazu av. ạsta- m. „Feindschaft, Verfolgung, Haß“ (*ans-tha Bartholomae Wb. 361), ạstai inf. „zu befeinden“, gav. angra-, av. aŋra- „feind, arg, böse“ aus *ans-ra- oder *as-ra- ... Vgl. ap. ahi-frašāay „strenges Gericht“ ... arika „feindlich gesinnt“ (*ahrika).' Root name, language label, gloss and the chart's uncertainty note all come from this one page — including Nourai's BRT:361 citation, which WLD prints inside the article.\"}\n    ],\n    \"consulted\": [\n      {\"src\": \"WLD\", \"where\": \"Bd. I p.134 (leaf 142 of WLD_Bd1_pages.txt)\", \"stance\": \"supports\",\n       \"note\": \"the whole entry-0 chart is this page: 'ens- „in feindseliger Absicht treffen“?' with av. ạsta-, ạstai, gav. angra-/av. aŋra- and ap. arika (*ahrika).\"},\n      {\"src\": \"POK\", \"where\": \"IEW 1959, whole volume\", \"stance\": \"silent\",\n       \"note\": \"no 'ens-'/'ans-' lemma anywhere in POK_full.txt (grep 'Root / lemma: .ns-' returns only dens-1/2, tens-, pens-, ṛens-); Pokorny simply did not carry Walde's doubtful article over into the 1959 revision.\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 appendix\", \"stance\": \"silent\",\n       \"note\": \"grep of AHD_watkins1985.txt for 'ans-'/'ens-'/'hostile intent' finds no such root headword; the appendix has no Indo-European root for aŋra-.\"},\n      {\"src\": \"KNT\", \"where\": \"Lexicon s.v. arika- (KNT.txt leaf 192)\", \"stance\": \"supports\",\n       \"note\": \"'to pAr. root *ans-, seen in Av. ạsta- „hate, enmity“' — Kent still operates with the base Walde reconstructed, which is the only part of 'Ens' modern Iranists use.\"},\n      {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e rishe-hā, pdf p.97 s.v. اهریمن\", \"stance\": \"contradicts\",\n       \"note\": \"Aryanpur's cognate list for اهریمن is Latin ANGUSTUS / ANGOR / ANXIUS, Gothic AGGWUS, French ANGOISSE, Italian ANGOSCIA, with the notes 'چم این واژه در زبان‌های ژرمنی: تنگی، تنگه، باریک' and 'چم این واژه در زبان انگلیسی نوین: خشم' — i.e. he puts aŋra-/Ahriman under PIE *h₂enǵʰ- 'narrow', not under Walde's *ens-.\"}\n    ],\n    \"nodes\": [\n\n    {\n      \"id\": 1, \"lang\": \"Avestan\",\n      \"words\": \"ans-tha, asta 1; astai; ans-ra, as-ra, anra, angra\",\n      \"verdict\": \"confirmed\",\n      \"derivation\": \"All three items are copied straight out of the two authorities. (a) Av. ạsta- m. 'hatred, enmity, hostility' — Bartholomae AiW col. 361: 'ạsta- m. „Hass, Feindschaft; Feindseligkeit“ ... Aus ar. *ans-tha-; vgl. (Et. unter aŋra-)'; the *-tha- is the Indo-Iranian abstract suffix (*ans-tha- > *anstha- > ạsta- with the regular Avestan loss of n before s and svarabhakti ạ-). Nourai's 'asta 1' is his own homonym number, not a form. (b) ạstāi, the Gathic infinitive 'to be hostile to' (Y.49.18 'aštēŋg ahmai yē nā ạstāi daidītā'), Bartholomae col. 362: 'Zu einer Basis ar. *ans-, s. aŋra-'. (c) aŋra-/angra- 'hostile; enemy, evil', Bartholomae col. 104-106: 'j. aŋra-, g. angra- Adj. „feindlich; Feind“ ... Aus ar. *anra-, zu einer ar. Basis *ans-'; Younger Avestan aŋra- shows the Iranian change *-nsr- > *-nhr- > -ŋr-, while the Gathic spelling angra- keeps the cluster, and *as-ra- (Johansson's alternative that WLD also records) is Nourai's 'as-ra'. So both the forms and the arrow from the root box are the sources' own.\",\n      \"derivation_fa\": \"هر سه صورت عیناً از بارتولومه و والده–پوکورنی گرفته شده است. اوستایی ạsta- «کین، دشمنی» (فرهنگ ایرانی باستان، ستون ۳۶۱) از هندوایرانی *ans-tha- است که در آن پسوند مصدریِ -tha- به ستاک افزوده شده و نونِ پیش از s افتاده است؛ ạstāi مصدر گاهانی «دشمنی کردن» است؛ و aŋra-/angra- «دشمن، بد، اهریمنی» از *ans-ra- یا *as-ra-. دگرگونی آوایی روشن است: خوشهٔ *-nsr- در ایرانی به -nhr- و سپس در اوستای متأخر به -ŋr- بدل شده، در حالی که املای گاهانی angra- همان خوشه را نگاه داشته است. ادعای نورایی درست است.\",\n      \"sources\": [W_AHRIMAN],\n      \"ref_check\": [\n        {\"ref\": \"WLD1:134\", \"status\": \"supports\",\n         \"note\": \"the page names all three: 'av. ạsta- m. „Feindschaft, Verfolgung, Haß“ (*ans-tha Bartholomae Wb. 361), ạstai inf. „zu befeinden“, gav. angra-, av. aŋra- „feind, arg, böse“ aus *ans-ra- oder *as-ra- (s. Johansson IF. 2, 26)'.\"},\n        {\"ref\": \"BRT:361\", \"status\": \"supports\",\n         \"note\": \"BRT.txt line 7844, the entry standing immediately before the running column head 'aŋzō.bug- 363': 'ạsta- m. „Hass, Feindschaft; Feindseligkeit“ ... Aus ar. *ans-tha-; vgl. (Et. unter aŋra-)', and next to it 'ạstāi Inf. „zu befeinden“ ... Zu einer Basis ar. *ans-, s. aŋra-'. Nourai's page 361 is exact (it is also the page WLD itself cites).\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"BRT\", \"where\": \"cols. 361-362 (ạsta-, ạstāi) and cols. 104-106 (aŋra-)\", \"stance\": \"supports\",\n         \"note\": \"'j. aŋra-, g. angra- Adj. „feindlich; Feind“ ... Aus ar. *anra-, zu einer ar. Basis *ans-; s. ạsta-, ariia-, ahiδrāδay- und Bthl. BB. S. 220'.\"},\n        {\"src\": \"WLD\", \"where\": \"Bd. I p.134 s.v. ens-\", \"stance\": \"supports\",\n         \"note\": \"same three words, same reconstructions, and the explicit alternative '*ans-ra- oder *as-ra-' that produces Nourai's doublet 'ans-ra, as-ra'.\"},\n        {\"src\": \"KNT\", \"where\": \"Lexicon s.v. arika-\", \"stance\": \"supports\",\n         \"note\": \"'deriv. of *aṇra-, GAv. angra-, LAv. aŋra- „hostile, enemy“, to pAr. root *ans-, seen in Av. ạsta- „hate, enmity“' — Kent repeats Bartholomae's chain unchanged in 1950.\"}\n      ]\n    },\n\n    {\n      \"id\": 2, \"lang\": \"Avestan\",\n      \"words\": \"anra-mainyu, angra-manyu, ahra-manyu\",\n      \"verdict\": \"confirmed\",\n      \"derivation\": \"Av. aŋrō mainiiuš (Gathic aŋrəm mainiiūm) 'the Hostile Spirit', still two words in the Gathas: Y.45.2 'mainyū ... yayā spanyå ... mravaṯ yəm aŋrəm', 'of the two spirits the holier said to the hostile one'. Bartholomae files the phrase under aŋra- itself: 'a) mit mainyu- m. „der arge, böse Geist“ (Ahriman) im Gegensatz zu spanyah-, spəṇta-'. The second member mainiiu- 'spirit, mind' is the -yu- noun of the root man- 'to think' (Av. mainyeite), PIE *men- (Pokorny 726-728, which lists 'Avestan mainyeite' first among the verbs) — exactly what Nourai's POK:726 and his cross-reference to root 'Men 1' claim. The three spellings of the chart are the three real chronological layers: Gathic angra-mainyu-, Younger Avestan aŋra-mainyu-, and *ahra-manyu, the pre-form with h that Bartholomae posits ('ap. Ahriman-, gr. Ἀρειμάνιος setzen eine urir. Nebenform *ahri̯a- voraus') and that Nyberg states outright: 'angra-, aṇra- < *ahra-'. It is that h-form, not the Avestan one, that yields Middle Persian Ahreman.\",\n      \"derivation_fa\": \"اوستایی aŋrō mainiiuš «مینوی دشمن، گوهرِ بد» در گاهان هنوز دو واژهٔ جداست (یسنا ۴۵ بند ۲). بخش دوم، mainiiu-، از ریشهٔ man- «اندیشیدن» (هندواروپایی آغازین *men-، پوکورنی ۷۲۶–۷۲۸) ساخته شده و همان است که در فارسی میانه mēnōg «مینو» شده است؛ پس ارجاعِ نورایی به ریشهٔ Men درست است. سه املای نمودار سه لایهٔ تاریخی‌اند: angra-mainyu گاهانی، aŋra-mainyu اوستای متأخر، و *ahra-manyu صورتی که بارتولومه و نیبرگ (angra-, aṇra- < *ahra-) بازساخته‌اند و همین صورت، نه صورت اوستایی، به فارسی میانهٔ Ahreman رسیده است. ادعای نورایی درست است.\",\n      \"sources\": [W_AHRIMAN],\n      \"ref_check\": [\n        {\"ref\": \"POK:726\", \"status\": \"supports\",\n         \"note\": \"POK_full.txt line 59530 ff.: 'Root / lemma: meːn-3, Meaning: to think, mind; spiritual activity ... Old Indic manyate „thinks“, Avestan mainyeite ds., ap. mainyahay ... Old Indic manas-, Avestan manah- n. „sense, mind“', Page(s): 726-728 — the article covers the -mainyu element, which is what the arrow needs.\"},\n        {\"ref\": \"KGW:46\", \"status\": \"not_checked\",\n         \"note\": \"Ibrahim, Kulturgeschichtliche Wortforschung (Wiesbaden 1991) is Google-Books preview only per refs_online.json; no copy reachable.\"},\n        {\"ref\": \"SIN:1179\", \"status\": \"not_found\",\n         \"note\": \"Laufer's Sino-Iranica occupies pp.185-630 of Field Museum Anthr. Ser. XV.3, so there is no page 1179 to check; SIN.txt has no 'Ahriman'/'Angra' passage either. Either the number is a misprint or 'SIN' here is not Sino-Iranica.\"},\n        {\"ref\": \"ETM:35\", \"status\": \"not_checked\",\n         \"note\": \"Abolghasemi, Risheh-shenasi (Qoqnus 1374) — refs_online.json records no digital copy on any permitted platform.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"BRT\", \"where\": \"cols. 104-106 s.v. aŋra-\", \"stance\": \"supports\",\n         \"note\": \"'a) mit mainyō- m. „der arge, böse Geist“ (Ahriman) im Gegensatz zu spanyah-, spəṇta-. mainyū .. yayā spanyā ... mraval yəm aŋrəm Y.45.2'; and the note 'ap. ahriman-, gr. Ἀρειμάνιος setzen eine urir. Nebenform *ahri̯a- voraus'.\"},\n        {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II (Glossary) p.12 s.v. Ahriman\", \"stance\": \"supports\",\n         \"note\": \"'Av. (104 sg.) angra- mainyu-, aṇra- mainyu- (angra-, aṇra- < *ahra-); MPrthPrs ʾh rmyn; Arm. lw. Ahrmn; Paz. Aharman; NP Aharman, Ahraman, Ahriman' — all three of Nourai's spellings, in that order.\"},\n        {\"src\": \"POK\", \"where\": \"pp.726-728 meːn-3\", \"stance\": \"supports\",\n         \"note\": \"supplies the etymology of the second member ('Avestan mainyeite').\"}\n      ]\n    },\n\n    {\n      \"id\": 3, \"lang\": \"Persian\",\n      \"words\": \"ahrîman «اهریمن» (also آهرمن)\",\n      \"verdict\": \"confirmed\",\n      \"derivation\": \"Av. aŋrō mainyuš (through the by-form *ahra-manyu of node 2) > Middle Persian Ahreman, written ʾh l(y)mnʹ in Book Pahlavi and ʾhrmyn in Manichaean and Parthian script (MacKenzie, Concise Pahlavi Dictionary p.7 'Ahreman [ʾAhl(y)mnʹ | M ʾhrmyn, N ~] the Evil Spirit'; Nyberg II 12), Pazand Aharman > New Persian آهرمن / اهرمن / اهریمن. Hübschmann, Persische Studien p.219, sets the word out under the rule that Indo-Iranian sr gives Persian r initially but keeps h medially: 'aber mit erhaltenem h N. pr. Ahraman, Aharman, Ahrman (bei Fird.), phl. Ahrman, Ahr(a)man u.s.w., arm. Arhmn, syr. ʾhrmn, zd. Aŋrō mainyuš' — that is precisely the arrow of the chart, and it also licenses the chart's second spelling آهرمن, the form Ferdowsi uses (the quoted line 'ز فریادرس زور و فریاد خواست – از آهرمن بدکنش داد خواست' stands in Noushin's Shahnameh glossary s.v. آهرمن). The -i- of ahriman is a late anaptyctic vowel breaking the Ahrman cluster; the sense 'devil' is the ordinary post-Sasanian generalisation of the name of the Zoroastrian Evil Spirit, and Mo'in still glosses the word etymologically as 'خرد خبیث، عقل پلید' — a literal rendering of aŋra- mainiiu-. Wiktionary: 'Inherited from Middle Persian ʾh lmnʹ (/ahreman/)'.\",\n      \"derivation_fa\": \"«اهریمن» از فارسی میانهٔ Ahreman (به خط پهلوی ʾh l(y)mnʹ، در مانوی و پارتی ʾhrmyn) است و آن از اوستایی aŋrō mainyuš — دقیق‌تر از صورتِ دارای h یعنی *ahra-manyu — می‌آید. هوبشمان در مطالعات فارسی (ص ۲۱۹) همین زنجیره را ذیل قاعدهٔ تبدیل sr آورده و صورت‌های آهرمن، اهرمن و اهریمن را کنار هم نهاده است؛ مکنزی و نیبرگ نیز همین را دارند. یای «اهریمن» واکهٔ میانجی و متأخر است که خوشهٔ hrm را می‌شکند، و صورت «آهرمن» که در بیت فردوسی آمده همانی است که نوشین در واژه‌نامک ذیل آهرمن آورده است. معنیِ «دیو، شیطان» تعمیمی است پس از دورهٔ ساسانی، چنان‌که معین نیز در پرانتز معنای تحت‌اللفظی «خرد خبیث، عقل پلید» را ثبت کرده است. ادعای نورایی درست است.\",\n      \"sources\": [W_AHRIMAN],\n      \"ref_check\": [\n        {\"ref\": \"BQT:2083\", \"status\": \"partial\",\n         \"note\": \"Borhan-e Qateʽ is alphabetical and its اهرمن/اهریمن/اهریمه entries stand in vol. 1 (BQT_v1_pages.txt leaf 409-410): 'اهرمن ، بر وزن بهمن ، بمعنی اهرمن باشد که رهنمای بدیها و شیطان است' / 'اهریمن ... رهنمای بدیها باشد چنان‌که یزدان رهنمای نیکی است', not at p.2083. Fetching the cited page (python3 tools/ref_page.py BQT:2083 -> vol.4 pdf p.166) lands in the م section, on مینو/مینا, whose Moʼin footnote reads 'اوستایی mainyu (روح، آسمان) ... درپهلوی mēnōk ... بارتولمه ۱۱۳۹ ... هویشمان' — i.e. it documents the -mainyu half of the name but not the headword اهریمن. The printed page 155 of Nourai really does read 'BQT:2083' (page image checked, copied to data/verification/sources/refs/ocr/BOOK/155.png), so the odd number is the book's, not the extraction's.\"},\n        {\"ref\": \"FSF:36\", \"status\": \"supports\",\n         \"note\": \"Noushin's Vāzhe-nāmak has آهرمن with exactly the verse of the chart — FSF_pages.txt leaf 43: 'ز فریادرس زور و فریاد خواست / از آهرمن بدکنش دادخواست'. In the scan on disk the page carries the printed number 40, not 36; the scan is a different printing from Nourai's Donya 1363 copy (the divergence grows through the book: اسقف = his p.44, scan p.51; سکوبا = his p.228, scan p.303), so the content, not the number, is what matches.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"HUB\", \"where\": \"Persische Studien p.219 (leaf 229 of HUB.txt)\", \"stance\": \"supports\",\n         \"note\": \"'aber mit erhaltenem h N. pr. Ahraman, Aharman, Ahrman (bei Fird.), phl. Ahrman, Ahr(a)man u.s.w., arm. Arhmn, syr. ʾhrmn, zd. Aŋrō mainyuš'.\"},\n        {\"src\": \"PHD\", \"where\": \"p.7 s.v. Ahreman\", \"stance\": \"supports\",\n         \"note\": \"'Ahreman [ʾAhl(y)mnʹ | M ʾhrmyn, N ~] the Evil Spirit'; MacKenzie's index of English meanings also gives 'evil spirit — Ahreman, gannāg mēnōg'.\"},\n        {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II p.12\", \"stance\": \"supports\",\n         \"note\": \"'Ahriman [ʾh lmnʹ] ... Paz. Aharman; NP Aharman, Ahraman, Ahriman'.\"},\n        {\"src\": \"BQT\", \"where\": \"vol. 1, leaf 409-410 s.v. اهرمن / اهریمن\", \"stance\": \"supports\",\n         \"note\": \"'راهنمای بدیها باشد ... و شیطان و دیو و جن را [گویند]' — the gloss 'devil' of the chart; Moʼin's footnote on the leaf is illegible in the OCR.\"},\n        {\"src\": \"MON\", \"where\": \"Farhang-e Farsi s.v. اهریمن (MON_part1.txt line 18979)\", \"stance\": \"supports\",\n         \"note\": \"'[... آهرامن - آهرمن - و - هریمن، خرد خبیث، عقل پلید] (اخ.) شیطان' — Moʼin lists the variant آهرمن that the chart prints in brackets and translates the Avestan compound literally.\"},\n        {\"src\": \"HRN\", \"where\": \"Grundriss der neupersischen Etymologie\", \"stance\": \"silent\",\n         \"note\": \"Horn has no numbered article for اهریمن; the only hit in HRN.txt is no. 126 'ʾafstar „schadliches, ahrimanisches Getier“', which uses the adjective in passing.\"}\n      ]\n    },\n\n    {\n      \"id\": 4, \"lang\": \"Old Persian\",\n      \"words\": \"arika, ahrika\",\n      \"verdict\": \"confirmed\",\n      \"derivation\": \"OP arika- 'hostile, disloyal, faithless' is real and well attested in Darius's Behistun text — nom. sg. arika DB 1.22, 1.33, 4.63, nom. pl. arikā DB 5.15, 5.31 — always in the loyalty formula 'yaθā naiy arika āham naiy draujana' 'as I was not disloyal, not a liar' (Bartholomae s.v. p. arika-). Kent's lexicon derives it exactly as the chart does: 'arika- adj. „evil, faithless“: deriv. of *aṇra-, GAv. angra-, LAv. aŋra- „hostile, enemy“, to pAr. root *ans- ... not to Skt. ari- „enemy“, nor to Skt. alīká-', and Bartholomae's own note is 'Ableit. aus ir. *ahra- (j. aŋra-)'. The second spelling 'ahrika' of the chart is not an attested Old Persian writing but Walde-Pokorny's starred reconstruction on the very page Nourai cites ('arika „feindlich gesinnt“ (*ahrika)'), the same *ahra- that gives Ahriman; it should carry an asterisk. Formation: *ahra- + the adjectival suffix -ka- (Kent §146.11), with the regular Old Persian loss of intervocalic h before r in *ahrika- > arika- (Bartholomae adds that one may also read ārīka-).\",\n      \"derivation_fa\": \"پارسی باستان arika- «دشمن‌خو، نافرمان» در سنگ‌نوشتهٔ بیستون (ستون یک، بندهای ۲۲ و ۳۳ و ...) در عبارتِ «naiy arika āham naiy draujana» آمده است. کنت آن را مشتقی از *aṇra- (همان aŋra- اوستایی) از ستاک *ans- می‌داند و بارتولومه نیز می‌نویسد «مشتق از ایرانی *ahra-»؛ پس این کلمه هم‌ریشهٔ اهریمن است. ساخت: *ahra- + پسوند صفتی -ka-، و h پیش از r در پارسی باستان افتاده است. نکته آنکه صورت دوم، ahrika، ضبطی مستند نیست بلکه بازساختِ ستاره‌دارِ والده–پوکورنی در همان صفحهٔ ۱۳۴ است و باید با * نوشته می‌شد. در مجموع ادعای نورایی درست است.\",\n      \"sources\": [W_AHRIMAN],\n      \"ref_check\": [\n        {\"ref\": \"WLD1:134\", \"status\": \"supports\",\n         \"note\": \"the closing lines of the article: 'Vgl. ap. ahi-frašāay „strenges Gericht“ (Kompositionsform der ro-Stämme auf i); arika „feindlich gesinnt“ (*ahrika)' — both of Nourai's spellings, one attested and one starred, come from this line.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"KNT\", \"where\": \"Old Persian, Lexicon s.v. arika- (leaf 192 of KNT.txt)\", \"stance\": \"supports\",\n         \"note\": \"'arika- adj. „evil, faithless“: deriv. (§146.11) of *aṇra-, GAv. angra-, LAv. aŋra- „hostile, enemy“, to pAr. root *ans-, seen in Av. ạsta- „hate, enmity“ ... arika nsm. DB 1.22, 33; 4.63. arikā npm. DB 5.15, 31.'\"},\n        {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch, Old Persian section s.v. arika- (BRT.txt line 5367)\", \"stance\": \"supports\",\n         \"note\": \"'p. arika- Adj. „feindlich gesinnt, feindselig“ ... Ableit. aus ir. *ahra- (j. aŋra-); vgl. aka-. — Man kann auch ārʹ und arīkʹ lesen; vgl. Horn NpEt. 6, Hbm. PSt. 6.'\"},\n        {\"src\": \"WLD\", \"where\": \"Bd. I p.134\", \"stance\": \"supports\",\n         \"note\": \"'arika „feindlich gesinnt“ (*ahrika)'.\"}\n      ]\n    }\n\n    ]\n  },\n\n  # ============================== ENTRY 1 : Epi, Opi ==============================\n  {\n    \"entry\": 1,\n    \"root\": \"Epi, Opi\",\n    \"verdict\": \"confirmed\",\n    \"modern_form\": \"PIE *h₁epi / *h₁opi 'at, on, near, against' (Pokorny 323-325 'epi, opi, pi'; Watkins/AHD 'epi, also opi. Near, at, against')\",\n    \"note\": \"Both of Nourai's references check out to the exact page. Pokorny's article is headed 'Root / lemma: epi, opi, pi; Meaning: at, by' and closes 'References: WP. I 122 f. ... Page(s): 323-325', so POK:323 is the first page of the article; Klein p.1065 s.v. ob- says of Latin ob 'fr. I.-E. base *opi-, which stands in gradational relationship to I.-E. *epi-', which is why Nourai's root box carries both ablaut shapes. Watkins gives the gloss almost word for word ('Near, at, against'). The whole Greek-Latin-English side of the chart is standard and uncontroversial. Two things need adjusting inside the tree rather than at the root: the Persian branch (nodes 5-6) labels the Syriac-mediated New Persian word سکوبا 'Old Persian', which is impossible — there is no Achaemenid word for 'bishop'; and the gloss of Greek epi-skopos as 'one rank above bishop' is a slip for 'overseer'. The chart is otherwise a good illustration of the same Greek word reaching Persian twice, once through Syriac (سکوبا) and once through Arabic (اسقف).\",\n    \"note_fa\": \"ریشه و هر دو مأخذِ نورایی دقیق‌اند: پوکورنی در صفحات ۳۲۳–۳۲۵ مادهٔ epi, opi, pi «نزد، بر، در برابر» را آورده و کلاین در صفحهٔ ۱۰۶۵ ذیل ob- می‌نویسد که لاتین ob از *opi- است و *opi- و *epi- دو درجهٔ آوایی یک ریشه‌اند — همین است که نورایی هر دو صورت را در سرِ نمودار نشانده است. دو لغزش درونِ نمودار هست: یکی آنکه «سکوبا» را پارسی باستان خوانده، در حالی که وام‌واژه‌ای فارسی نو از راه سریانی است؛ دوم آنکه معنای epi-skopos «ناظر، سرپرست» است نه «یک رتبه بالاتر از اسقف». در مجموع، این نمودار نمونهٔ خوبی است از ورودِ دوبارهٔ یک واژهٔ یونانی به فارسی: یک بار از سریانی (سکوبا) و یک بار از عربی (اسقف).\",\n    \"sources\": [W_EPISK, ETY_BISHOP],\n    \"ref_check\": [\n      {\"ref\": \"POK:323\", \"status\": \"supports\",\n       \"note\": \"POK_full.txt line 27210: 'Root / lemma: epi, opi, pi | Meaning: at, by | Material: Old Indic api ... Avestan aipi, ap. apiy ... Gr. ἐπί ... Latin ob ...', with 'References: WP. I 122 f. ... Page(s): 323-325'.\"},\n      {\"ref\": \"KLN:1065\", \"status\": \"supports\",\n       \"note\": \"Klein 1966, leaf 570 of KLN_1966.txt = printed pp.1065-1066 (verified from the page numerals on leaves 569/571): 'ob-, pref. ... fr. L. ob, „toward, against, in the way of“ ... fr. I.-E. base *opi-, which stands in gradational relationship to I.-E. *epi-, whence Gk. ἐπί, „on, upon“. See epi-.'\"}\n    ],\n    \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"pp.323-325 epi, opi, pi\", \"stance\": \"supports\",\n       \"note\": \"the article contains, in this order, the Avestan/Old Persian, the Latin and the Greek boxes of the chart.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. I p.122 (leaf 130, running head 'epi, opi, pi')\", \"stance\": \"supports\",\n       \"note\": \"Pokorny's own source article, cited by him as 'WP. I 122 f.'\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. epi\", \"stance\": \"supports\",\n       \"note\": \"'epi. Also opi. Near, at, against. 1. Latin ob, ob-, before, to, against: OB-. 2. Greek epi, on, over, at: EPI-. ... [Pok. epi 323.]' — Nourai's gloss is Watkins's word for word.\"},\n      {\"src\": \"IEC\", \"where\": \"Mann, s.v. epi (pi)\", \"stance\": \"supports\",\n       \"note\": \"'epi (pi) „on, by, at, near“. WP I, 122. Skt. Av. ápi; Oss. fe-, fi-; Arm. h- ... Myc. & Gk. epi ...' — but Mann keeps Latin ob in a separate lemma, see node 2.\"}\n    ],\n    \"nodes\": [\n\n    {\n      \"id\": 1, \"lang\": \"Avestan / Old Persian\",\n      \"words\": \"aipi; aipi-areta; apiy, ape, apaya\",\n      \"verdict\": \"confirmed\",\n      \"derivation\": \"Avestan aipi and Old Persian apiy are the regular Iranian continuations of *h₁epi: Pokorny p.323 has 'Avestan aipi, ap. apiy, adnominal „about – to, by (Akk.), by (temporal, Lok.)“, Adv. „in addition also, likewise also, particularly“, prefix „to“; with lengthened grade of final syllable Avestan āpe „after“ (m. Akk.), compare apaya „hereafter, prospectively“' — which is where the chart's three Old Persian shapes 'apiy, ape, apaya' come from, in Pokorny's own order. Bartholomae cols. 82-83 sets it out in the same terms ('j., g. aipi, p. apiy: Adv. „dazu auch, desgleichen auch“ ... „auch, gar, besonders“; Praep. mit Akk. „über — hin“, „bei“'), and Klein p.530, the page Nourai cites for this box, glosses it exactly as the chart does: 'Avestic aipi, „also; to, toward“'. In Old Persian apiy is the enclitic emphasiser of the formula dūraiy apiy 'even far away' (DNa 12, DSe 11, XPa etc.). The second item, aipi-areta, is Av. aipi.ərəta- 'firmly allotted, determined', the participle of ar- 'to fit, allot' with the preverb, attested in the compound aipi.ərətō.gātu- 'having a firmly assigned place' (Bartholomae); Nourai's cross-reference to root 'Ar' and his POK:57 are therefore right, that page falling inside Pokorny's ar-1 (pp.55-61).\",\n      \"derivation_fa\": \"اوستایی aipi و پارسی باستان apiy دنبالهٔ قاعده‌مند هندواروپایی *h₁epi اند. پوکورنی (ص ۳۲۳) همین سه صورتِ پارسی باستان را یکجا آورده است: apiy و با کششِ هجای پایانی اوستایی āpe «پس از» و apaya. در سنگ‌نوشته‌های هخامنشی، apiy جزء دومِ ترکیبِ dūraiy apiy «حتی از دوردست» است. صورت aipi-areta همان aipi.ərəta- «معین، مقرر» است که از ریشهٔ ar- «برازیدن، بخش کردن» ساخته شده و در ترکیب aipi.ərətō.gātu- آمده است؛ پس ارجاع نورایی به ریشهٔ Ar و به صفحهٔ ۵۷ پوکورنی (درون مادهٔ ar-1، صفحات ۵۵–۶۱) درست است. ادعای نورایی درست است.\",\n      \"sources\": [W_EPISK],\n      \"ref_check\": [\n        {\"ref\": \"KLN:530\", \"status\": \"supports\",\n         \"note\": \"Klein 1966 leaf 288 carries the printed numerals 530/531 and holds the entry: 'epi-, before a vowel ep-, before an aspirate eph-, pref. ... — Gk. ἐπί- ... cogn. with OI. ápi, „also, besides“, Avestic aipi, „also; to, toward“, Toch. -pi, Arm. ev, „also, and“ ... Cp. ob-.' Nourai's gloss 'to, toward, also' is Klein's.\"},\n        {\"ref\": \"POK:57\", \"status\": \"supports\",\n         \"note\": \"p.57 lies inside 'Root / lemma: ar-1, themat. (a)rə-, heavy basis arə-, rē- ... Meaning: to move, pass ... Page(s): 55-61' — the root of the ərəta- of aipi.ərəta-, and the article Nourai's cross-reference '☞ Ar' points to.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"BRT\", \"where\": \"cols. 82-83 s.v. aipi\", \"stance\": \"supports\",\n         \"note\": \"'j., g. aipi, p. apiy I) Adv. 1) „dazu auch, desgleichen auch“ ... 3) „auch, gar, besonders“ ... II) Praep. 1) mit Akk. a) „über — hin“ ... b) „bei“'; the neighbouring article ends 'Vgl. aipi, apaya, apəm und zum Ausgang āoe' — Nourai's trio apiy/ape/apaya is Bartholomae's.\"},\n        {\"src\": \"KNT\", \"where\": \"Old Persian §133, §186 and the texts (DNa 12, DSe 11)\", \"stance\": \"supports\",\n         \"note\": \"'Adverbs and particles ... -apiy, -patiy both also separately'; 'dūraiy + apiy, which is most often two words, appears as dūraiapiy ... and also as dūrayapiy'.\"},\n        {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II p.20 s.v. api-\", \"stance\": \"supports\",\n         \"note\": \"'Av. (82 sg.) aipi, OP apiy „moreover, further“ ... Along with it there must have existed a fully stressed form *ápi; id.-europ. *ápi (Gr postp. ἔπι, prep. ἐπί)' — Nyberg also cites Bartholomae's column 82 for aipi, confirming the column reference used above.\"},\n        {\"src\": \"POK\", \"where\": \"p.323\", \"stance\": \"supports\",\n         \"note\": \"'Avestan aipi, ap. apiy ... Avestan āpe „after“ (m. Akk.), compare apaya „hereafter, prospectively“'.\"}\n      ]\n    },\n\n    {\n      \"id\": 2, \"lang\": \"Latin\", \"words\": \"ob\",\n      \"verdict\": \"confirmed\",\n      \"derivation\": \"Latin ob 'towards, against, in front of, on account of' (Old Latin also 'around, near'), prefix ob- with the assimilations oc-/of-/og-/op- and o- before m. Pokorny p.324 derives it from the o-grade of the same root: 'Latin ob adnominal m. Akk. ... and prefix from op- before voiced consonant originated ...; op still in operio from *op-verio, oportet from *op-vorteti', comparing Oscan up, op. Watkins lists it as the first branch of the root ('1. Latin ob, ob-, before, to, against: OB-'), and Klein p.1065 says explicitly 'fr. I.-E. base *opi-, which stands in gradational relationship to I.-E. *epi-'. One dissent worth recording: Mann's Indo-European Comparative Dictionary puts Latin ob under a different lemma, 'obhi, obh- „athwart, against, at“' together with Skt. abhí, Av. aiwi, OPers. abiy; Ernout-Meillet likewise allow that Latin ob may continue both *opi and *obhi, which fell together. The majority position, and all three books Nourai relies on, put it where the chart does.\",\n      \"derivation_fa\": \"حرف اضافهٔ لاتین ob «به سوی، در برابر، پیشاپیش» از درجهٔ o دارِ همین ریشه (*opi) است؛ پوکورنی صورت op- را در operio و oportet برجای‌مانده می‌داند و با اسکی و امبریایی up/op می‌سنجد؛ کلاین نیز همین را می‌گوید. یک نکتهٔ احتیاطی: من (Mann) در فرهنگ تطبیقی خود ob لاتین را زیر مادهٔ دیگری (*obhi، همریشه با سنسکریت abhí و اوستایی aiwi) آورده است؛ ارنو–مییه نیز احتمال آمیختگی این دو را می‌دهند. با این همه رایِ غالب همان است که نورایی آورده و ادعای او درست است.\",\n      \"sources\": [ETY_BISHOP],\n      \"ref_check\": [\n        {\"ref\": \"AHD\", \"status\": \"supports\",\n         \"note\": \"Watkins 1985 s.v. epi: '1. Latin ob, ob-, before, to, against: OB-' — Nourai's gloss 'to against, before' is a transcription of this line.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"POK\", \"where\": \"p.324 within epi, opi, pi\", \"stance\": \"supports\",\n         \"note\": \"'Latin ob ... prep. with acc., in front of, before; in return for; because of ... and prefix from op- before voiced consonant originated ...; op still in operio from *op-verio, oportet from *op-vorteti'.\"},\n        {\"src\": \"KLN\", \"where\": \"p.1065 s.v. ob-\", \"stance\": \"supports\",\n         \"note\": \"'fr. L. ob ... which is rel. to Oscan op, up, Umbr. os (for *ops) ... fr. I.-E. base *opi-, which stands in gradational relationship to I.-E. *epi-'.\"},\n        {\"src\": \"IEC\", \"where\": \"Mann s.v. obhi, obh-\", \"stance\": \"partial\",\n         \"note\": \"'obhi, obh- „athwart, against, at“. WP I, 124. Skt. abhí ... Av. aiwi, id.; OPer. abiy, id.; ... Lat. ob, prp. „before, opposite, at, to, for, owing to“' — Mann assigns Latin ob to *obhi rather than to *opi.\"}\n      ]\n    },\n\n    {\n      \"id\": 3, \"lang\": \"English\", \"words\": \"obtain, offer, oppose, omit\",\n      \"verdict\": \"confirmed\",\n      \"derivation\": \"All four are Latin ob- compounds that reached English through French or directly from Latin, and all four show the assimilations of the prefix noted at node 2. obtain < ME obteinen < OF obtenir < L. obtinēre (ob + tenēre 'to hold'). offer is the oldest: Klein s.v. offer, 'fr. OE. offrian, „to bring offering, to sacrifice“, fr. L. offerre, „to bring before, present, offer“, fr. ob- and ferre, „to bear, carry“' — borrowed into Old English already in the Christian mission period, later re-shaped by French offrir. oppose < OF opposer, a French remodelling of L. opponēre (ob + pōnere) on poser; the prefix is assimilated ob- > op- before p. omit < L. omittere (ob + mittere), where ob- becomes o- before m. Nourai gives the node no reference, and none is needed: this is the standard Latin-to-English chain covered by Klein and Skeat.\",\n      \"derivation_fa\": \"هر چهار واژه ترکیباتِ پیشوندِ لاتینی ob- اند که از راه فرانسه یا مستقیم از لاتین به انگلیسی راه یافته‌اند و همه همگونیِ پیشوند را نشان می‌دهند: obtain از obtinēre (ob + tenēre)، offer از offerre (ob + ferre) که همان انگلیسی کهن offrian است و در دورهٔ تبلیغ مسیحیت وام گرفته شده، oppose از opponēre (ob مانندِ p شده: op-) و omit از omittere (ob پیش از m به o- بدل شده). زنجیره معروف و بی‌اختلاف است و ادعای نورایی درست است.\",\n      \"sources\": [ETY_BISHOP],\n      \"ref_check\": [\n        {\"ref\": \"None\", \"status\": \"not_checked\",\n         \"note\": \"the node carries no reference in the book; the chain is covered by Klein and Skeat, quoted under 'consulted'.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"KLN\", \"where\": \"s.v. offer (KLN_1966.txt line 26130) and s.v. ob-\", \"stance\": \"supports\",\n         \"note\": \"'offer ... fr. OE. offrian ... fr. L. offerre, „to bring before, present, offer“, fr. ob- and ferre'; the ob- article lists the assimilations 'before c, f, g, p, assimilated into oc-, of-, og-, op-; before m, ob- becomes o-' that account for oppose and omit.\"},\n        {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etymological Dictionary, s.vv. obtain / omit\", \"stance\": \"supports\",\n         \"note\": \"Skeat carries the same Latin ob- compounds; grep of SKT.txt shows the ob- prefix articles with 'L. ob, against, near'.\"}\n      ]\n    },\n\n    {\n      \"id\": 4, \"lang\": \"Greek\", \"words\": \"epi; epi-skopos\",\n      \"verdict\": \"plausible\",\n      \"derivation\": \"Greek ἐπί 'on, over, at, among' is the direct reflex of *h₁epi (Pokorny p.323 'Gr. ἐπί ... „auf, to, an“, adnominal with dative'; Watkins '2. Greek epi, on, over, at: EPI-'), and ἐπίσκοπος is ἐπί + σκοπός 'watcher', from the root *speḱ- 'to see' with the Greek metathesis spek- > skep-/skop-; Klein s.v. bishop: 'fr. Gk. ἐπίσκοπος, „overseer“, fr. ἐπί, „on, over“, and σκοπός, „watcher“'. Nourai's cross-reference '☞ Spek' is therefore right. What is wrong is his gloss: ἐπίσκοπος means 'overseer, inspector' in classical Greek (a civic official; also used of gods 'watching over'), and in Christian Greek from the 1st century it denotes the bishop himself — not, as the chart says, 'one rank above bishop'. The chart's own Latin and English boxes below translate the same word as 'bishop', so the gloss contradicts the rest of the tree. Everything else in the node is confirmed; the node is marked plausible because of that gloss.\",\n      \"derivation_fa\": \"یونانی ἐπί «بر، روی، میان» بازتابِ مستقیم *h₁epi است و ἐπίσκοπος مرکب است از ἐπί و σκοπός «نگهبان، دیده‌بان» از ریشهٔ *speḱ- «دیدن» (با قلبِ spek- > skop- در یونانی)؛ پس ارجاع نورایی به ریشهٔ Spek درست است. اما معنایی که در نمودار آمده («یک رتبه بالاتر از اسقف») خطاست: این واژه در یونانی کلاسیک «ناظر، بازرس» و در یونانی مسیحی خودِ «اسقف» است، چنان‌که خانه‌های لاتین و انگلیسیِ همین نمودار آن را bishop ترجمه کرده‌اند. پس ریشه‌شناسی درست است و تنها معنیِ ثبت‌شده باید اصلاح شود.\",\n      \"sources\": [W_EPISK, ETY_BISHOP],\n      \"ref_check\": [\n        {\"ref\": \"AHD\", \"status\": \"supports\",\n         \"note\": \"Watkins 1985 s.v. epi: '2. Greek epi, on, over, at: EPI-' — supports the Greek box; Watkins does not gloss episkopos, which is where the chart's own gloss goes astray.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"POK\", \"where\": \"p.323\", \"stance\": \"supports\",\n         \"note\": \"'Gr. ἐπί, ἔπι „auf, to, an“, adnominal with dative (= Indo-Germanic Lok., Instr., Akk., Gen.), prefix'.\"},\n        {\"src\": \"KLN\", \"where\": \"p.530 s.v. epi- and p.170-ish s.v. bishop\", \"stance\": \"supports\",\n         \"note\": \"'bishop ... fr. L. episcopus, „overseer, superintendant“, in Eccles. L., „bishop“, fr. Gk. ἐπίσκοπος, „overseer“, fr. ἐπί, „on, over“, and σκοπός, „watcher“. See epi- and -scope.'\"},\n        {\"src\": \"Wiktionary\", \"where\": \"ἐπίσκοπος\", \"stance\": \"supports\",\n         \"note\": \"ἐπί (from PIE *h₁épi) + σκοπός (root *speḱ-) + -ος, literally 'one who looks upon', hence 'overseer', in Christian use 'bishop'.\"}\n      ]\n    },\n\n    {\n      \"id\": 5, \"lang\": \"Old Persian\", \"words\": \"skuba\",\n      \"verdict\": \"disputed\",\n      \"derivation\": \"There is no Old Persian *skuba, and there cannot be one: Kent's Old Persian lexicon (the whole Achaemenid corpus) has no such word, and a term for a Christian bishop is four centuries younger than the last Old Persian inscription. سکوبا is a New Persian word of the Sasanian/early Islamic period, first met in Ferdowsi, borrowed not from Greek directly but from the Syriac of the Church of the East — Syr. ʾep(p)isqōpā / ʾasqōpā ቨ Gk. ἐπίσκοπος — with loss of the unstressed initial syllable ʾepi- and retention of the Aramaic determinate ending -ā (whence Persian -ā of سکوبا). Dehkhoda states this outright ('the Iranians took سکوبا from the Syriac form of the same Greek word; it occurs in the Shahnameh'), and Noushin's Shahnameh glossary sends the reader from سکوبا to اسقف and Latin episcopus. So the arrow Greek → this box is right in substance but the language label is wrong, and the box is not a separate stage: it is the same word as node 6. The printed page really does read 'Old Persian' (page image checked and archived), so the error is Nourai's, not the extraction's.\",\n      \"derivation_fa\": \"واژه‌ای به نامِ skuba در پارسی باستان وجود ندارد و نمی‌تواند داشته باشد: در واژه‌نامهٔ کنت از کلّ پیکرهٔ هخامنشی چنین واژه‌ای نیست، و اصلاً اصطلاحی مسیحی چند قرن پس از دورهٔ پارسی باستان پدید آمده است. «سکوبا» وام‌واژه‌ای فارسی نو است که نه یکسره از یونانی بلکه از راه سریانی کلیسای شرق (ʾep(p)isqōpā از ἐπίσκοπος) وارد شده است؛ هجای آغازین افتاده و پایانهٔ معرفهٔ آرامی ـا برجا مانده است. دهخدا همین را می‌گوید و نوشین در واژه‌نامک از سکوبا به اسقف و episcopus ارجاع می‌دهد. پس ریشه درست است ولی برچسبِ «پارسی باستان» خطاست و این خانه مرحله‌ای جدا از خانهٔ بعدی نیست؛ خطا از خود کتاب است نه از خوانش اسکن.\",\n      \"error_in\": \"book\",\n      \"book_prints\": \"Old Persian | MON:1901; FSF:228 | skuba : bishop, priest\",\n      \"correct_form\": \"New Persian سکوبا sokūbā, borrowed from Syriac ʾep(p)isqōpā < Greek ἐπίσκοπος (no Old Persian stage)\",\n      \"sources\": [AB_SEKUBA, W_USQUF],\n      \"ref_check\": [\n        {\"ref\": \"MON:1901\", \"status\": \"partial\",\n         \"note\": \"Moʼin does have the headword (سکوبا '(سُ) (اِ.) اسقف', read on abadis.ir), and its alphabetical place (س) fits a page in the 1900s of the continuous pagination, but the entry gives only the meaning — it says nothing about Old Persian.\"},\n        {\"ref\": \"FSF:228\", \"status\": \"partial\",\n         \"note\": \"Noushin, Vāzhe-nāmak, s.v. سکوبا (p.303 of the scan on disk, leaf 306; his edition is paginated differently): 'سکوبا (با پیش اول) پیشوای مذهبی در آیین مسیحی (معرب ... اسقف، لاتینی episcopus، به واژهٔ اسقف نگاه کنید)' with the chart's Ferdowsi couplet. Noushin treats it as a Christian-Greek loan into Persian; he never calls it Old Persian.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"KNT\", \"where\": \"Old Persian, Lexicon (pp.164-215)\", \"stance\": \"contradicts\",\n         \"note\": \"no entry skuba- or anything like it; the Old Persian lexicon contains no ecclesiastical vocabulary at all.\"},\n        {\"src\": \"MON\", \"where\": \"Farhang-e Farsi s.v. سکوبا (via abadis.ir)\", \"stance\": \"partial\",\n         \"note\": \"'(سُ) (اِ.) اسقف' — meaning only, no Old Persian claim.\"},\n        {\"src\": \"Dehkhoda\", \"where\": \"Loghatnameh s.v. اسقف / سکوبا (via abadis.ir)\", \"stance\": \"contradicts\",\n         \"note\": \"Dehkhoda derives سکوبا from the Syriac form of Greek episkopos and cites its use in the Shahnameh — a New Persian loan through Syriac, not an Old Persian inheritance.\"}\n      ]\n    },\n\n    {\n      \"id\": 6, \"lang\": \"Persian\", \"words\": \"sekubâ «سکوبا»\",\n      \"verdict\": \"plausible\",\n      \"derivation\": \"The word itself is genuine and its ultimate origin is exactly what the chart says. سکوبا (Moʼin vocalises it sokūbā, Noushin 'با پیش اول', i.e. with u in the first syllable) is 'a Christian bishop' in Ferdowsi — the chart's couplet 'نوشتند نامه به هر کشوری / سکوبا و بطریق و هر مهتری' stands verbatim in Noushin's glossary — and it comes, through Syriac, from Greek ἐπίσκοπος, alongside بطریق (patriarch) and other Syriac church titles that entered Persian in the Sasanian period. The one thing that does not hold is the arrow: its drawn parent, the 'Old Persian skuba' of node 5, does not exist, so this box is not the descendant of the box above it — the two are one and the same word. Verdict plausible: right word, right ultimate source, spurious intermediate stage.\",\n      \"derivation_fa\": \"خودِ واژه اصیل است و خاستگاه نهایی‌اش همان است که نورایی گفته: «سکوبا» (معین: سُکوبا) در شاهنامه به معنای پیشوای مسیحی است — همان بیتی که در نمودار آمده عیناً در واژه‌نامک نوشین نقل شده — و از راه سریانی از یونانی ἐπίσκοπος آمده، در کنار «بطریق» و دیگر عنوان‌های کلیسایی که در روزگار ساسانی به فارسی راه یافته‌اند. آنچه درست نیست خودِ پیکان است: پدرِ رسم‌شده («پارسی باستان skuba») وجود ندارد و این دو خانه یک واژه‌اند؛ پس با احتیاط پذیرفتنی است.\",\n      \"sources\": [AB_SEKUBA],\n      \"ref_check\": [\n        {\"ref\": \"MON:1901\", \"status\": \"supports\",\n         \"note\": \"Moʼin s.v. سکوبا: '(سُ) (اِ.) اسقف' — the meaning of the chart ('a Christian bishop'); read on abadis.ir, which reproduces Farhang-e Moʼin.\"},\n        {\"ref\": \"FSF:228\", \"status\": \"supports\",\n         \"note\": \"FSF_pages.txt leaf 306 (printed p.303 of this scan): 'سکوبا (با پیش اول) پیشوای مذهبی در آیین مسیحی ... لاتینی episcopus ... نوشتند نامه به هر کشوری / سکوبا و بطریق و هر مهتری' — word, meaning and quotation all as printed in the chart.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"FSF\", \"where\": \"Vāzhe-nāmak s.v. سکوبا (leaf 306)\", \"stance\": \"supports\",\n         \"note\": \"quoted above; Noushin cross-refers to his own اسقف entry, i.e. he regards سکوبا and اسقف as two shapes of one Greek word.\"},\n        {\"src\": \"MON\", \"where\": \"Farhang-e Moʼin s.v. سکوبا (abadis.ir)\", \"stance\": \"supports\",\n         \"note\": \"'(سُ) (اِ.) اسقف'.\"},\n        {\"src\": \"Dehkhoda\", \"where\": \"Loghatnameh (abadis.ir)\", \"stance\": \"partial\",\n         \"note\": \"records سکوبا with a Shahnameh citation and derives it from the Syriac reflex of Greek episkopos — compatible with the chart's ultimate source, incompatible with the 'Old Persian' box between them.\"}\n      ]\n    },\n\n    {\n      \"id\": 7, \"lang\": \"Arabic\", \"words\": \"osqof\",\n      \"verdict\": \"confirmed\",\n      \"derivation\": \"Arabic أُسقُف usquf (pl. أساقفة asāqifa) 'bishop' is a Christian loan from Greek ἐπίσκοπος, taken over through the Aramaic/Syriac of the Christian communities of Syria and Mesopotamia: Classical Syriac ܐܦܣܩܘܦܐ ʾeppisqōpā, from which Arabic has the aphaeretic ʾ(u)squf on the fuʻlul pattern; the popular association with سقف 'roof' is secondary. Nourai's own reference, al-ʿUnaysi's dictionary of foreign words in Arabic, states the Greek source in as many words on the page cited. He draws Greek → Arabic directly and leaves out the Syriac stage that Wiktionary and the Arabic lexicographers name; that is a simplification of the route, not an error in it.\",\n      \"derivation_fa\": \"عربی أُسقُف (جمع: أساقفة) وام‌واژه‌ای مسیحی از یونانی ἐπίσκοπος است که از راه سریانی ʾeppisqōpā وارد عربی شده؛ هجای آغازین افتاده و واژه بر وزن فُعلُل قالب گرفته است؛ پیوند اشتقاقی آن با «سقف» عربی ریشه‌شناسی عامیانه است. طوبیا العنیسی در همان صفحه‌ای که نورایی یاد کرده می‌نویسد «أسقف – یونانی». تنها نکته آن که نورایی میانجیِ سریانی را نیاورده است؛ این خلاصه‌کردن است نه خطا. ادعای نورایی درست است.\",\n      \"sources\": [W_USQUF, AB_OSQOF],\n      \"ref_check\": [\n        {\"ref\": \"TAD:3\", \"status\": \"supports\",\n         \"note\": \"TAD_pages.txt leaf 6 (the third page of the alphabetical list, i.e. printed p.3): 'أسقف – يوناني [ἐπίσκοπος] معناه في الأصل الملاحظ والمدير وفي عرف [الكنيسة]...' — exactly Nourai's claim, and note that al-ʿUnaysi's gloss 'the observer and the director' is the correct sense of episkopos, against the chart's own Greek gloss.\"},\n        {\"ref\": \"MON:270\", \"status\": \"supports\",\n         \"note\": \"Moʼin s.v. اسقف (read on abadis.ir): '(اُ قُ) [معر.] (اِ.) از یونانی گرفته شده به معنای پیشوای عیسوی که مرتبه‌اش [از کشیش بالاتر است]' — 'معرّب, from Greek', both halves of Nourai's arrow. The print edition (MON_part1.txt) has the same entry: 'اسقف: (معر. ...) درجه‌ای از درجات آیین مسیح که پایین‌تر از مطران و بالاتر از کشیش است؛ ج. اساقفه'.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"TAD\", \"where\": \"p.3 s.v. أسقف\", \"stance\": \"supports\",\n         \"note\": \"quoted above.\"},\n        {\"src\": \"Wiktionary\", \"where\": \"أسقف\", \"stance\": \"supports\",\n         \"note\": \"'Borrowed from Ancient Greek ἐπίσκοπος (epískopos), via Classical Syriac ܐܦܣܩܘܦܐ (ʾeppisqoppā)'; descendants include Classical/Iranian Persian usquf, Ottoman Turkish اسقف, Malay uskup, Swahili askofu.\"},\n        {\"src\": \"AFM\", \"where\": \"Addi Shir, al-Alfāẓ al-fārisiyya al-muʿarraba\", \"stance\": \"silent\",\n         \"note\": \"grep of AFM_pages.txt for سقف returns only the Arabic سقف 'roof' in another article — as expected, since Addi Shir collects Persian, not Greek, loans in Arabic.\"},\n        {\"src\": \"MON\", \"where\": \"Farhang-e Farsi s.v. اسقف\", \"stance\": \"supports\",\n         \"note\": \"tags the word معرّب and traces it to Greek.\"}\n      ]\n    },\n\n    {\n      \"id\": 8, \"lang\": \"Persian\", \"words\": \"osqof «اسقُف»\",\n      \"verdict\": \"confirmed\",\n      \"derivation\": \"New Persian اسقف osqof 'bishop' is the Arabic word re-borrowed into Persian after the conquest — Moʼin marks it معرّب (an Arabicised form) and defines it 'درجه‌ای از درجات آیین مسیح که پایین‌تر از مطران و بالاتر از کشیش است', with the Arabic plural اساقفه — and Wiktionary lists Classical, Dari, Iranian Persian and Tajik usquf among the descendants of Arabic أسقف. Ferdowsi already uses it (the chart's couplet 'سقف گفت کاین نیست کاری گران / که پیش از تو بودند چندی سران' is printed in Noushin's glossary under اسقف, together with 'به اسقف چنین گفت کای دستگیر'). This box and node 6 are the two halves of a genuine doublet: one and the same Greek word entered Persian twice, once through Syriac as سکوبا and once through Arabic as اسقف.\",\n      \"derivation_fa\": \"«اسقف» فارسی وام‌گیری از عربی أسقف است پس از اسلام؛ معین آن را معرّب می‌داند و معنایش را «درجه‌ای از درجات آیین مسیح که پایین‌تر از مطران و بالاتر از کشیش است» می‌آورد (جمع عربی: اساقفه). فردوسی نیز آن را به‌کار برده و نوشین همین دو بیت را ذیل اسقف آورده است. نکتهٔ جالب آنکه «اسقف» و «سکوبا» دوگانهٔ (doublet) یک واژهٔ یونانی‌اند: یکی از راه عربی و دیگری از راه سریانی. ادعای نورایی درست است.\",\n      \"sources\": [AB_OSQOF, W_USQUF],\n      \"ref_check\": [\n        {\"ref\": \"MON:270\", \"status\": \"supports\",\n         \"note\": \"Moʼin, اسقف: '[معر.] ... از یونانی گرفته شده ...' (abadis.ir) and, in the print text on disk, 'اسقف: (معر. ...) درجه‌ای از درجات آیین مسیح ... ج. اساقفه' (MON_part1.txt line 12885). The alphabetical position (اسـ) fits p.270 of vol. 1.\"},\n        {\"ref\": \"FSF:44\", \"status\": \"supports\",\n         \"note\": \"FSF_pages.txt leaf 54 (printed p.51 of this scan): 'اسقف (با پیش اول و سوم و سکون دوم) ... (با پیش اول و دوم – تازی) ... [ἐπίσκοπος] پارسی: سکوبا', followed by the two Shahnameh couplets, the second of which ('سقف گفت کاین نیست کاری گران / که پیش از تو بودند چندی سران') is the one the chart quotes. Noushin marks it تازی (Arabic) and gives سکوبا as its Persian counterpart — he, unlike the chart, sees the two as parallel, not as ancestor and descendant.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"MON\", \"where\": \"Farhang-e Farsi / Farhang-e Moʼin s.v. اسقف\", \"stance\": \"supports\",\n         \"note\": \"'معرّب ... از یونانی'.\"},\n        {\"src\": \"FSF\", \"where\": \"Vāzhe-nāmak s.v. اسقف (leaf 54)\", \"stance\": \"supports\",\n         \"note\": \"the chart's Ferdowsi couplet, with 'تازی' as the origin tag and 'پارسی: سکوبا'.\"},\n        {\"src\": \"Wiktionary\", \"where\": \"أسقف, descendants\", \"stance\": \"supports\",\n         \"note\": \"Classical Persian / Dari / Iranian Persian / Tajik usquf listed as borrowings from the Arabic.\"}\n      ]\n    },\n\n    {\n      \"id\": 9, \"lang\": \"Latin\", \"words\": \"episcopus, biscopus; epi-děmia; epi-lěpsia\",\n      \"verdict\": \"plausible\",\n      \"derivation\": \"episcopus is right: Church Latin took ἐπίσκοπος over unchanged in the earliest Latin Bible translations (2nd-3rd c.), and Klein glosses it as the chart's box does, 'L. episcopus, „overseer, superintendant“, in Eccles. L., „bishop“'. 'biscopus' is not a Latin word as written: what is attested in Late/Vulgar Latin is (e)biscopus, with aphaeresis of the unstressed e- and voicing of -p- to -b-, and it is that form, not classical episcopus, that gave OE biscop, OS biscop, OHG biscof — so the box is right in substance but the form should be starred or written ebiscopus. The gloss 'priest' is loose: an episcopus outranks a presbyter. The other two items are Greek rather than Latin words: ἐπιδημία 'a stay among the people' (ἐπί + δῆμος, whence Nourai's cross-reference '☞ Dâ'), which acquired the medical sense in the Hippocratic corpus and reached Latin as a medical borrowing, and ἐπιληψία 'a seizing upon' (ἐπί + λαμβάνω 'seize'), Late Latin epilepsia. Putting them in a Latin box is a shortcut of the chart's layout; both glosses are otherwise accurate.\",\n      \"derivation_fa\": \"episcopus درست است: لاتینِ کلیسایی در ترجمه‌های نخستین کتاب مقدس (سدهٔ دوم–سوم میلادی) همان ἐπίσκοπος را بی‌دست‌کاری وام گرفته است. اما biscopus واژه‌ای لاتین بدین صورت نیست؛ آنچه مستند است صورت لاتینِ عامیانهٔ (e)biscopus است که با افتادن e- و نرم‌شدن p پدید آمده و همین صورت است که به انگلیسی کهن biscop رسیده؛ پس باید ستاره‌دار نوشته می‌شد. دو واژهٔ دیگر، epidemia و epilepsia، در اصل یونانی‌اند (ἐπί + δῆμος و ἐπί + λαμβάνω) و از راه اصطلاحات پزشکی به لاتین راه یافته‌اند؛ نشاندنِ آنها در خانهٔ لاتین ساده‌سازی نمودار است. بنابراین این خانه با احتیاط پذیرفتنی است.\",\n      \"sources\": [ETY_BISHOP, W_EPISK],\n      \"ref_check\": [\n        {\"ref\": \"AHD\", \"status\": \"partial\",\n         \"note\": \"Watkins's epi article names the Greek and Latin branches and sends the English words EPI-, OB- etc. to them, but it does not list episcopus/biscopus or the medical compounds individually; the detail has to come from Klein and Skeat.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"KLN\", \"where\": \"s.v. bishop and archbishop\", \"stance\": \"supports\",\n         \"note\": \"'bishop ... fr. OE. bisceop, biscop, fr. L. episcopus'; 'archbishop ... fr. OE. arcebiscop, fr. Eccles. L. archiepiscopus, fr. Eccles. Gk. ἀρχιεπίσκοπος, lit. „chief bishop“'.\"},\n        {\"src\": \"SKT\", \"where\": \"Skeat s.v. Episcopal\", \"stance\": \"supports\",\n         \"note\": \"'Episcopal. (F. – L. – Gk.) O.F. episcopal. – L. episcopalis, belonging to a bishop, – L. episcopus, a bishop. – Gk. ἐπίσκοπος, an over-seer, bishop. – Gk. ἐπί, upon; σκοπός, one that watches.'\"},\n        {\"src\": \"Etymonline\", \"where\": \"s.v. bishop\", \"stance\": \"partial\",\n         \"note\": \"gives Late Latin episcopus and the Romance reflexes (Sp. obispo, It. vescovo, Fr. évêque) but writes the Germanic source as Late Latin episcopus, i.e. it does not print 'biscopus' as a Latin headword.\"}\n      ]\n    },\n\n    {\n      \"id\": 10, \"lang\": \"English\", \"words\": \"Episcopal, bishop, epidemic, epilepsy\",\n      \"verdict\": \"confirmed\",\n      \"derivation\": \"bishop < ME biscop, bischop < OE bisceop/biscop, an early loan (before the 7th c., with the Roman mission) from Vulgar Latin (e)biscopus for L. episcopus; Etymonline calls the pair bishop / French évêque 'a curious example of word-change', the two reflexes of one Latin word 'not to have a letter in common', English having dropped the first and last syllables. Episcopal < OF episcopal < Late Latin episcopālis, a learned re-borrowing of the same word, which is why English has the doublet bishop / episcopal. epidemic < French épidémique < Medieval Latin epidemia < Gk ἐπιδημία. epilepsy < Middle French épilepsie < Late Latin epilepsia < Gk ἐπιληψία. Every one of the four therefore continues Greek ἐπί and, through it, the root of the chart.\",\n      \"derivation_fa\": \"bishop از انگلیسی میانه biscop و آن از انگلیسی کهن bisceop، وام‌واژه‌ای کهن (پیش از سدهٔ هفتم میلادی) از لاتین عامیانهٔ (e)biscopus است؛ جالب آنکه همین واژه در فرانسه به صورت évêque درآمده و این دو حتی یک حرف مشترک ندارند. Episcopal وام‌گیری عالمانهٔ دوبارهٔ همان کلمه است (دوگانهٔ bishop/episcopal)، و epidemic و epilepsy از راه فرانسه و لاتینِ متأخر از یونانی ἐπιδημία و ἐπιληψία آمده‌اند. هر چهار در نهایت به ἐπί و از آنجا به ریشهٔ نمودار می‌رسند؛ ادعای نورایی درست است.\",\n      \"sources\": [ETY_BISHOP],\n      \"ref_check\": [\n        {\"ref\": \"AHD\", \"status\": \"supports\",\n         \"note\": \"Watkins s.v. epi: '2. Greek epi, on, over, at: EPI-' — the appendix routes all the English EPI- words, bishop included through episcopus, to this root.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"KLN\", \"where\": \"s.v. bishop (KLN_1966.txt line 5065)\", \"stance\": \"supports\",\n         \"note\": \"'bishop, n. — ME. biscop, bischop, fr. OE. bisceop, biscop, fr. L. episcopus ... fr. Gk. ἐπίσκοπος ... See epi- and -scope and cp. episcopal. Cp. also obispo.'\"},\n        {\"src\": \"SKT\", \"where\": \"Skeat s.v. Episcopal\", \"stance\": \"supports\",\n         \"note\": \"quoted at node 9.\"},\n        {\"src\": \"Etymonline\", \"where\": \"s.v. bishop\", \"stance\": \"supports\",\n         \"note\": \"'Greek episkopos „watcher, (spiritual) overseer“ ... Late Latin episcopus ... Old English bisceop', with Old Saxon biscop and Old High German biscof.\"}\n      ]\n    }\n\n    ]\n  }\n  ]\n}\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-155.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(doc, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"written\")\n"
}
```


### [2026-09-05T20:52:57.314Z] TOOL RESULT

```
File created successfully at: /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build155.py (file state is current in your context — no need to Read it back)
```


## [2026-09-05T20:53:03.897Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && sed -i 's/ʾasqōpā ቨ Gk\\./ʾasqōpā < Gk./' build155.py && grep -c \"ቨ\" build155.py; python3 build155.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-155.json > /dev/null && echo \"JSON OK\""
}
```


### [2026-09-05T20:53:06.584Z] TOOL RESULT

```
0
written
JSON OK
```


## [2026-09-05T20:53:28.977Z] TOOL CALL #82: Bash

```json
{
 "command": "python3 tools/verify_check.py 155"
}
```


### [2026-09-05T20:53:31.422Z] TOOL RESULT

```
nodes verified: 14/14
node verdicts: {'confirmed': 10, 'plausible': 3, 'disputed': 1}
root verdicts: {'plausible': 1, 'confirmed': 1}
ref checks: {'supports': 16, 'not_checked': 3, 'not_found': 1, 'partial': 4}
books consulted: {'supports': 38, 'silent': 2, 'partial': 4, 'contradicts': 2} | by book: {'MON': 5, 'KLN': 5, 'BRT': 4, 'KNT': 4, 'POK': 4, 'NYB': 3, 'SKT': 3, 'Wiktionary': 3, 'WLD': 2, 'Dehkhoda': 2, 'FSF': 2, 'Etymonline': 2, 'HUB': 1, 'PHD': 1, 'BQT': 1, 'HRN': 1, 'IEC': 1, 'TAD': 1, 'AFM': 1}
```


## [2026-09-05T20:53:50.161Z] AGENT

Page 155 (book p. 125) verified — `data/verification/page-155.json`, `verify_check.py 155` shows 14/14 nodes, 0 PROBLEM lines.

**Counts** — roots: 1 confirmed (Epi/Opi), 1 plausible (Ens). Nodes: 10 confirmed, 3 plausible, 1 disputed. Ref checks: 16 supports, 4 partial, 1 not_found, 3 not_checked.

**Flagged items**
- `disputed` — Epi/Opi #5 "Old Persian skuba": there is no Old Persian word for 'bishop' (absent from Kent's lexicon, and the term postdates the Achaemenids by centuries). سکوبا is a New Persian loan from Syriac ʾeppisqōpā < Gk. ἐπίσκοπος (so Dehkhoda; Noushin cross-refers it to اسقف). The printed page really reads "Old Persian" — Nourai's error, not the extraction's; page PNG archived to `data/verification/sources/refs/ocr/BOOK/155.png`.
- `plausible` — root **Ens**: faithful to WLD I 134 (which itself heads it "ens- …?" and says "Die Gruppe ist unsicher"), but Pokorny 1959 and Watkins dropped the lemma; Aryanpur puts aŋra-/اهریمن under *h₂enǵʰ- 'narrow' (Lat. angustus, Eng. anger) instead.
- `plausible` — Epi #4: gloss "epi-skopos: one rank above bishop" is a slip; it means 'overseer' and denotes the bishop himself (the chart's own Latin/English boxes say "bishop").
- `plausible` — Epi #6 sekubā (real word, right ultimate source, but its drawn parent #5 doesn't exist) and #9 (Latin box: "biscopus" is Vulgar Latin *(e)biscopus, not Latin; epidemia/epilepsia are Greek).

**Reference problems (author's, not the data's)**
- `BQT:2083` for اهریمن: Borhan's اهرمن/اهریمن entries are in vol. 1; p. 2083 falls in the م section (مینو, whose Moʼin footnote does document Av. mainyu- / Phl. mēnōg). Recorded as `partial`.
- `SIN:1179`: Sino-Iranica only runs pp. 185–630 — no such page (`not_found`). `KGW:46` and `ETM:35` are not obtainable.
- `FSF` page numbers (36, 44, 228) don't match the scan on disk (40, 51, 303) — different printing, content matches.
- Precise hits: WLD I 134 (source of the whole first chart, including Nourai's own BRT:361), BRT 361/362, POK 323–325 and 726–728, POK 57 (ar-1), KLN 530 and 1065 (both verified against the printed page numerals), TAD 3, MON 270.

**No extraction errors found** — the JSON matches the printed page throughout (refs, words, glosses, quotes, language labels).
