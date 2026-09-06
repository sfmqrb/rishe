# Verification process log — verify-page-254


## [2026-09-06T16:08:40.459Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 254 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-254.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-254.json. Write /home/sfmqrb/git/rishe/data/verification/page-254.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 254` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T16:08:42.033Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T16:08:42.738Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


## [2026-09-06T16:08:42.782Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-254.txt"
}
```


### [2026-09-06T16:08:42.794Z] TOOL RESULT

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


### [2026-09-06T16:08:42.802Z] TOOL RESULT

```
1	=== PDF page 254 (book page 224) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Ken : young, fresh  (refs POK:563)
4	#1 (parent #0) [Avestan] refs=POK:563; SOD:190 | kan 2, kaine, kainîn, kaimyâ : young girl ; kan-yâ, kain-ika : small woman
5	  #2 (parent #1) [Pahlavi] refs=FSF:275; HRN:194 | kanik : young girl ; kaničak : young girl
6	    #3 (parent #2) [Persian] refs=BQT:1715; HRN:174 | kanîz «کنیز» : maid | extra: کنیزک
7	  #4 (parent #1) [Sogdian] refs=SOD:190 | knc : girl ; knc`k : young girl
8	#5 (parent #0) [Latin] refs=POK:563 | re-cens : fresh, new
9	  #6 (parent #5) [English] refs=None | recent
10	--- entry 1 ---
11	ROOT Keng -> redirect to Keg
12	--- entry 2 ---
13	ROOT [Indo-European] Kenk 1; Koksâ : heel, knee; hip  (refs POK:566)
14	#1 (parent #0) [Avestan / Old Persian] refs=KLN:735; BRT:456 | kaša : arm pit ; karš : to pull
15	  #2 (parent #1) [Persian] refs=HRN:191; BQT:1653,1657,1755 | kešâleh «کشاله» : crutch ; kešîdan «کشیدن» : to pull ; kaškŭl «کشکول» : Dervish's cup that is "carried by the shoulder" ; tîr-kaš «تیرکش» : bag for carrying arrows, quiver ☞Steig ; kîš 1 «کیش ۱» : distorted form of "tîr-kaš", quiver ; kîš 2 «کیش ۲» : a "kîš 1"-looking island south of Iran | extra: ترکش
16	#3 (parent #0) [Latin] refs=AHD:326 | coxa : hip ; coxînus : hip rest
17	  #4 (parent #3) [Old French] refs=AHD | cuisse, coissin : cushion
18	    #5 (parent #4) [Persian] refs=VOP:296 | kŭsan «کوسن» : cushion
19	    #6 (parent #4) [English] refs=None | cushion
20	#7 (parent #0) [Germanic] refs=AHD | hanhila : heel
21	  #8 (parent #7) [English] refs=None | heel
22	--- entry 3 ---
23	ROOT Kenk 2 -> redirect to Keg
24	
```


## [2026-09-06T16:08:45.760Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-254.json",
 "description": "Read source JSON for page 254"
}
```


### [2026-09-06T16:08:45.794Z] TOOL RESULT

```
{
  "pdf_page": 254,
  "book_page": 224,
  "entries": [
    {
      "root": {
        "name": "Ken",
        "lang": "Indo-European",
        "refs": "POK:563",
        "gloss": "young, fresh"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:563; SOD:190",
          "words": [
            {"translit": "kan 2, kaine, kainîn, kaimyâ", "gloss": "young girl", "script": null},
            {"translit": "kan-yâ, kain-ika", "gloss": "small woman", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "FSF:275; HRN:194",
          "words": [
            {"translit": "kanik", "gloss": "young girl", "script": null},
            {"translit": "kaničak", "gloss": "young girl", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:1715; HRN:174",
          "words": [
            {"translit": "kanîz", "gloss": "maid", "script": "کنیز"}
          ],
          "script_extra": "کنیزک",
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 1,
          "lang": "Sogdian",
          "refs": "SOD:190",
          "words": [
            {"translit": "knc", "gloss": "girl", "script": null},
            {"translit": "knc`k", "gloss": "young girl", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Latin",
          "refs": "POK:563",
          "words": [
            {"translit": "re-cens", "gloss": "fresh, new", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "recent", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Keng",
        "redirect": "Keg"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Kenk 1; Koksâ",
        "lang": "Indo-European",
        "refs": "POK:566",
        "gloss": "heel, knee; hip"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "KLN:735; BRT:456",
          "words": [
            {"translit": "kaša", "gloss": "arm pit", "script": null},
            {"translit": "karš", "gloss": "to pull", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "HRN:191; BQT:1653,1657,1755",
          "words": [
            {"translit": "kešâleh", "gloss": "crutch", "script": "کشاله"},
            {"translit": "kešîdan", "gloss": "to pull", "script": "کشیدن"},
            {"translit": "kaškŭl", "gloss": "Dervish's cup that is \"carried by the shoulder\"", "script": "کشکول"},
            {"translit": "tîr-kaš", "gloss": "bag for carrying arrows, quiver", "script": "تیرکش", "see": ["Steig"]},
            {"translit": "kîš 1", "gloss": "distorted form of \"tîr-kaš\", quiver", "script": "کیش ۱"},
            {"translit": "kîš 2", "gloss": "a \"kîš 1\"-looking island south of Iran", "script": "کیش ۲"}
          ],
          "script_extra": "ترکش",
          "note": null,
          "quote": {
            "text": "آسمان گر سلاح بربندد - تیر تدبیر تو نهد در کیش ۱",
            "poet": "Anvarî Abîvardî"
          }
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD:326",
          "words": [
            {"translit": "coxa", "gloss": "hip", "script": null},
            {"translit": "coxînus", "gloss": "hip rest", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Old French",
          "refs": "AHD",
          "words": [
            {"translit": "cuisse, coissin", "gloss": "cushion", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "VOP:296",
          "words": [
            {"translit": "kŭsan", "gloss": "cushion", "script": "کوسن"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 4,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "cushion", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "hanhila", "gloss": "heel", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "heel", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Kenk 2",
        "redirect": "Keg"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-06T16:08:46.612Z] TOOL CALL #4: Bash

```json
{
 "command": "sed -n '1,200p' data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-06T16:08:46.654Z] TOOL RESULT

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


## [2026-09-06T16:09:09.726Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','SOD','HRN','BQT','FSF','KLN','BRT','AHD','VOP','MON','PHD','NYB','CHEUNG','SKT','LEW','LAT','IEC','SYN','WLD','ARY']:\n    v=d.get(k)\n    print('===',k, json.dumps(v,ensure_ascii=False)[:600] if v else 'MISSING')\n\""
}
```


## [2026-09-06T16:09:10.063Z] TOOL CALL #6: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe/data/verification/ | head -50; echo ---; sed -n '1,60p' /home/sfmqrb/git/rishe/data/verification/page-202.json"
}
```


### [2026-09-06T16:09:11.714Z] TOOL RESULT

```
=== POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_
=== SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=
=== HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 
=== BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118
=== FSF {"title": "Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/1984", "kind": "archive_djvu", "url": "https://archive.org/details/20220809_20220809_1444", "lookup_hint": "grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushin book (گزارشی چند درباره شاهنامه).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF.txt"], "page_offs
=== KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h
=== BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1
=== AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,
=== VOP {"title": "Mahshid Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi, Alborz 1371/1992", "kind": "none", "url": null, "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found (only unrelated similar-title books, e.g. Zomorrodian's فرهنگ ریشه‌شناختی واژه‌های دخیل اروپایی, ketabnak 132354).", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: nothing — no catalogue record with a scan, no ebook. Decoys: ketabnak 132354 (Zomorrodian), Google Books RwdkAAAAMAAJ (Nahid Shahidi 1997, no view). Purchase second-hand only."}
=== MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
=== PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-
=== NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf
=== CHEUNG MISSING
=== SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves
=== LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f b
=== LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for mos
=== IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 
=== SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves
=== WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039
=== ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it
```


### [2026-09-06T16:09:11.765Z] TOOL RESULT

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
```


## [2026-09-06T16:09:16.301Z] TOOL CALL #7: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','SOD','HRN','BQT','FSF','BRT','KLN','AHD']:\n    v=d[k]; print('===',k); print(' offset:',v.get('page_offset')); print(' hint:',str(v.get('lookup_hint'))[:500]); print(' local:',v.get('local_file'))\n\""
}
```


### [2026-09-06T16:09:18.006Z] TOOL RESULT

```
=== POK
 offset: POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
 hint: Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?bas
 local: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt
=== SOD
 offset: printed page ≈ leaf − 66 in SOD_pages.txt (0-based \f blocks; 645 leaves; English intro precedes)
 hint: Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get serv
 local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD.txt']
=== HRN
 offset: leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
 hint: Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.
 local: /home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt
=== BQT
 offset: vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
 hint: grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf imag
 local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt']
=== FSF
 offset: 484 leaves; edition/printing of this scan not identified — determine offset from printed page numbers on the page text/image when checking
 hint: grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushin book (گزارشی چند درباره شاهنامه).
 local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF.txt']
=== BRT
 offset: Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
 hint: Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops.
 local: /home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt
=== KLN
 offset: KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
 hint: Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
 local: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt
=== AHD
 offset: 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.
 hint: Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New Colleg
 local: /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt
```


## [2026-09-06T16:09:21.009Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"Page(s): 56[3-7]\" POK_full.txt | head -30"
}
```


### [2026-09-06T16:09:21.052Z] TOOL RESULT

```
45252:Page(s): 565 
45284:Page(s): 565 
45307:Page(s): 565 
45327:Page(s): 566 
45720:Page(s): 563-564 
45746:Page(s): 564 
45764:Page(s): 567 
46242:Page(s): 567-571 
49260:Page(s): 564-565 
50142:Page(s): 566 
50169:Page(s): 566 
50199:Page(s): 567 
50215:Page(s): 564
```


## [2026-09-06T16:09:21.947Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"^ken-\\|^kenk-\\|^kōk\\|^koks\" POK_02.txt POK_01.txt | head -30"
}
```


### [2026-09-06T16:09:21.990Z] TOOL RESULT

```
POK_02.txt:3436:ken-  jleer,  nichtig*;  nur  griech.  und  armen.
POK_02.txt:3468:kenk-,  konk-   , schwanken',   ursprüngl.  »hangen,   geistig   in   Schwebe   sein'. Ai.    sdTdkate    , schwankt,    zweifelt,    fürchtet',    saidkä   , Besorgnis,   Furcht Zweifel',  sai^kita-  , besorgt';
POK_02.txt:4234:koksä  jKörperteilbenennung'  (arisch  auch  *kokso-s).
```


## [2026-09-06T16:09:24.410Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '45700,45770p' POK_full.txt; echo ====; sed -n '45320,45345p' POK_full.txt; echo ====; sed -n '50135,50210p' POK_full.txt"
}
```


### [2026-09-06T16:09:24.485Z] TOOL RESULT

```
Exit code 1
Middle Irish cinim^ rise, puff up, originate ', c/n/ud^ gender, sex, stem, line '; Old Irish 
ce/7e/" gender, sex', acymr. cenetl, ncymr. "gender, sex, nation'; perhaps also acymr. 
mcymr. cein, ncymr. cain. Middle Breton quen. Old Irish -from Brit. - ca//7 "beautiful' (: gr. 
Kawjoc, "beautiful' = " young '?); genuine Irish is cain{*keni-) ds.; 

Middle Irish cano, Canada wolf cub', cymr. cenau^youug dog or wolf {*ken9ua. ken-); 

gall. Cintus, Cintugnatos {^ Primigenitus '), Old Irish cetne, cet- " previous ', cymr. etc. 
cyn(t)^ previous, before, rather', c>77/a/"the first'; 

burgund. hend/nos' king'; controversial Gothic hindumists^ extreme, hindermost ', Old 
High German hintana, hintar^ behind ', Old English hindema^ the last ' ("new, not old, 
young, fresh, recent '); 

Old Church Slavic i/b- na-cbnq, -J^//"begin', zac^f/"6s.; receive (of woman)', konb' 
beginning ', kontcb "end'. Old Church Slavic c§do "kid, child' (if not loanword from Modern 
High German Kind, s. Berneker 154); with flexible s- Upper Serbian sceho^ the last-born 
child ', russ. scenok^young dog'. Old Church Slavic sten§^ a young animal, whelp '. 

References: WP. I 397 f., Wackernagel-Debrunner III 112 f. 
Page(s): 563-564 

Root / lemma: ken-4 

Meaning: to strain, strive 

Material: Gr. kovsTv snsiysaGai, svspysTv, kovsi an£u5£, rpsxe, Kovapcbrspov 

5paaTiKU)T£pov Hes., KOvr|Tai GspanovTS^, ayKOvouc; Siqkovouc;, SouAouq Hes., Siqkovoc;, 

Ionian 5inKovo(; " servant, messenger, attendant or official in a temple or religious guild, 

esp. in the Christian church, deacon, servile, menial ', syKOVEU) " o be quick and active, 

esp. in service, urge on, incite ', sy-Kovit; " maid '; 



Latin conor, -an" to undertake, endeavor, attempt, try, venture, seek, aim, make an 
effort, begin, make trial of; 

proto Celtic *kan-{\n6o Germanic *kdn-) " accomplish ' in mcymr. d/gon/'make', 
dichawn, digawn, cymr. dichon, digon' can ', digon' sufficient ', acymr. MN Guoccawn, 
mcymr. gochawn, gogawn^ distinguished ', abr. MN Uuocon. 

References: WP. I 398 f., WH. I 262. 
Page(s): 564 

Root / lemma: kenth(o)- 
Meaning: rag, cloth 
Note: also ket(h)-l 
Material: 

Old Indie kantha' repaired dress'; Armenian k'ot'anak^ 6xess, cover'; 

gr. K£VTpu)v " skirt from rags ' meaning leans from Latin; 

Latin cento^ a rag cushion, patchwork quilt '; 

without nasal Old High German hadarai. "rag, clout' {*hat^rd, Indo Germanic *kotra). 
Modern High German Hadern, in addition with Aderivative Middle High German Hadel, 
ablaut. Modern High German dial. Hudel, therefrom hude/n' smear'. 

References: WP. I 402 f., WH. I 200. 
Page(s): 567 

Root / lemma: kerd-1 

Meaning: to girdle 

Note: only Celtic and Slavic 
(eval):1: === not found
```


## [2026-09-06T16:09:29.913Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '45680,45700p' POK_full.txt; echo \"-----A\"; sed -n '45300,45330p' POK_full.txt; echo \"-----B\"; sed -n '50130,50205p' POK_full.txt"
}
```


### [2026-09-06T16:09:29.996Z] TOOL RESULT

```
5. 5-extension: Latvian /r/75Js/5 "small mosquito ' (as knisis, fen /s//s irom the /-basis). 

References: WP. I 392 ff., WH. I 217 f., 11166 f. 
Page(s): 559-563 



Root / lemma: ken-3 

Meaning: to appear, be born; to begin; young 

Material: Old Indie kamna-^ young ', compounds Sup. kanlyas-, kanistha-, kanistha-, 

kanya. Gen. PI. kanTnam {o\6er n-stem) "girl', Avestan ka/ne, kaim-, kainJn- ds.; 

gr. Kaiv6(; ' fresh, egregious '; 

Latin /'ece/75 "fresh, young, new', actually " lately arisen, not long in existence, fresh, 
young, recent '; 

Middle Irish cinim^ rise, puff up, originate ', c/n/ud^ gender, sex, stem, line '; Old Irish 
-----A
Gothic huhrus, with gramm. variation Old Norse hungr. Old English hunger. Old High 
German hungar{*knkru-) "hunger' (= gr. kqk-); ablaut. Old Norse /7a "plague, torment, 
smite' {*hanhdn); 

Lithuanian /ra/7/ra"pain, agony', kankinti^ afflict ', /re/7M"harm'. 

References: WP. I 401, Trautmann 126, Wissmann Nom. postverb. 42. 
Page(s): 565 

Root / lemma: kenk-3 

Meaning: knee-cup, heel 

Material: Old Indie karjkala-m. n. "bone, skeleton '; 

Old Norse ha {* hanha-) in ha-motm. " ankle joint, heel joint ', ha-sini. ' Kniesehne des 
Hinterbeins bei Tieren, Fersensehne beim Menschen ', Old English hoh-sinui.. Old Frisian 
ho-sene^ heel tendon ', Old English /7d/7 "calcaneus, heel bone ' {* hanha-). Old Norse haell 
"calcaneus, heel bone ' {*hanhila-). Old English he/am. "calcaneus, heel bone '; 

Lithuanian kenk/e' popliteus, muscle located in the back of the knee ', k/'nka'6s., hock, 
joint in the hind leg of a quadruped; shank, leg ', Latvian c/nks/a ' s\ne\N in the knee-bend '. 

References: WP. 1401. 



Page(s): 566 



-----B
German Middle High German henken ' hang ' from *hengjan, therefrom Modern High 
German Henkel, Swiss henkeF sling, strap ', compare Middle High German henger iron 
hook, handle, part of an object designed to be gripped by the hand '; in addition probably 
Old High German hahila, -alai.. Middle Low German haleu. ' pothook, metal hook used to 
hang or lift pots ' {*hanhild)\ 

Hittite ga-an-ki {kankJ) ' hangs '. 

References: WP. I 382 f., WH. I 307; compare above kak- and keg-. 



Page(s): 566 



Root / lemma: Rens- 

Meaning: to proclaim, announce 

Material: Old Indie samsayat/" aWows to recite, proclaims, announces ' (= Latin censed), 

samsati^ recites, praises ', samsa- m. " laudation, glorification prayer ', sastf-i. " laudation ' 

{*l<ns-), sasai. " song of praise to God '; 

Avestan sah- " to make publicly known, publish, proclaim, announce ', Optat. sahyal, 
sast/-^\Nord, instruction '; sanghaite. Old pers. z?a//y" speaks, announces' {*^a(n)hat})\ 

alb. thom'\ say' {*Rensmi), 2. Sg. thua, thue, ablaut, participle than^ said ' {* thonsno); 

Latin censed, -ere^ examine, assess ', Oscan censamur^ censeior ', censaum^ to tax, 
assess, rate, estimate ', keenzstur, kenzsur{= censor. Old Indie saifistar-^ he recites there 
'), an-censtot = in-censa^ non censa ', Latin census {: Old Indie sasta-h^ spoken, praised 
'), censtom-en^ in censum ', Kenssurine/s Gen. (= Censormus); 

Old Bulgarian s^/b " to say ' (older root Aorist? compare Meillet, Slave commun2 209). 

References: WP. I 403, WH. I 198 ff., EM3 201. 
Page(s): 566 

Root / lemma: Rent- 

Meaning: to stick 

Material: Gr. kevtsoo (from the 5. Jhd.; older:) *K£VTaj, Aor. Ksvaai 'prick', Ksvrpov 'sting, 

prick' (forms-AO-) ' pricking ', kevtojp ' goader, driver ' (to KEvrpov shaped after other -Twp 

besides -ipo-), Kzaioc, ' embroidered ' (*k£vt-t6(;), Ksarpov ' pointed iron', Kzaipoq, 'arrow', 

KEOTpa f. ' pointed hammer ', kovt6(; ' pole, punting-pole, pike, crutch, goad ' (out of it Latin 

contuses., whereof /Oe/rc»/7/a/7"actu ally ' to question strictly '); 

Old Irish cinteir {LaWu loanword) ' a spur ', cymr. cethr^v\d\\\ corn, kenferds., bret. kentr 
' spur ' (borrowing aller from Latin centrum ' the stationary foot of the compasses ', 
Pedersen KG. I 198, is barely provable, but probably; Vendryes Mel. Saussure 319 allows 
only the ir. word to derive from Brit.); 

Old High German hantag' sharp'; Gothic handugs'mse'. Old Norse hannarr' skilful, 
smart' from *hant^ara-, actually 'sharp witted, shrewd'?; (under the influence of common 
Celtic -n^, -nt- > -nn-). 



Latvian sfts (= Lithuanian *sintas) ' liunting spear '. 

References: WP. I 402. 
Page(s): 567 



Root / lemma: Ren- 

Meaning: empty, puny
```


## [2026-09-06T16:09:40.603Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"lemma: koks\\|lemma: kenk\\|lemma: keg\" POK_full.txt"
}
```


### [2026-09-06T16:09:40.654Z] TOOL RESULT

```
44506:Root / lemma: keg- keng- and kek-, kenk- 
45254:Root / lemma: kenk-1 
45286:Root / lemma: kenk-2 
45309:Root / lemma: kenk-3
```


## [2026-09-06T16:09:43.433Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '44506,44520p' POK_full.txt; echo \"-----1\"; sed -n '45254,45300p' POK_full.txt; echo \"-----koksa\"; grep -n \"koks\" POK_full.txt | head"
}
```


### [2026-09-06T16:09:43.510Z] TOOL RESULT

```
Root / lemma: keg- keng- and kek-, kenk- 

Meaning: hook, grappling hook, handle 

Note: compare das similar Rak-, Rank-, and Renk-, Ronk- 

Material: Npers. cang^ claw, nail, fist' {*kengo-)\ 

Middle Irish ail-chengi. " rake, weapon rack ' (: Lithuanian kenge, see below); 

Germanic *hakan-, *hdka-, *hekan-rc\. "hook' in: Old Icelandic PN Hakim, 'hook', haka 
f. 'chin'. Old English haca rw. 'bar, bolt', haeccei. ' crosier, crozier, bishop's staff; Old 
Icelandic hakrm. ' Frechling ', Old High German hako, haggo'hook', Old English hocm. 
'hook'. Middle Low German hok, hukvc\. ' angle, point, edge, foreland, promontory ', Old 
Icelandic h0kjai. {*hdkidn-) ' crutch ', h0kill rr\. ' Hinterbug '; with intensive Gemination: 
-----1
Root / lemma: kenk-1 

Meaning: to bind, girdle 

Material: Old Indie /ra/7C5/e(Dhatup.) "binds', kahcuka-m. "armor, coat of mail, garment 

made of linked metal rings, jerkin, corsage', kancTi. "belt, girdle'; 

gr. KiYKAi(; " lattice, latticework, trellis, structure of interwoven strips of wood or metal ' (to 
I from £ s. Solmsen Beitr. I 214 f.), KOKaAa n. PI. " walls ' {*knk-), no5o-KaK(K)r| " foot 
plague, a kind of stocks '; 

Latin cingo, -ere^ go around, surround, encompass, environ, gird, wreathe, crown ', 
Umbrian sihltu^ go around, surround, encompass, environ, gird, wreathe, crown ', perhaps 
also gihgera^ a lattice, enclosure, grating, grate, balustrade, bars, railings, bar in a court of 
justice ' {*kinkeda-); Latin -^for c derailment due to the ambiguous cinxi, cincfum aiter 
present as dingo, mingo; WH. I 217 places here Celtic cing-^ march, step, stride, strut' 
(different above S. 439), whether originally "*turn in circles '; however, the variation of the 
Auslauts would be easy to understand, as the page 439 accepted initial sound variation; 
still different about Celtic c//7^-Kuiper Nasalpras. 168 f.; 

Lithuanian kinkau, -ytr harness horses '. 



An unnasalized root form */re/r- one seeks in Old Indie kaca-xw. " hair of the head 
("*fastened together '?); scar, band, strap' and Latin cicatrix ^ scar, scratch ' (due to a 
*cicare irorw *cecare^ tie together, heal ')? 

References: WP. I 400 f., WH. I 211, 216 f. 
Page(s): 565 

Root / lemma: kenk-2 

Meaning: to burn, be dry; a burning feel (hunger, thirst) 

Material: Old Indie karjksati^ longs for' (' brennend verlangen '), /r5/ra/e(Dhatup.) " covets, 

thirsts '; common Old Indie gh- > ks- 

gr. K£YK£i TTEivg (after Aor. *KaK£Tv originated a new present *KaYK(jo, compare:) 
KOYKopEvnc; ^nPCK^ TO) cpopu) Hes., hom. noAuKayKriq (Siijja) ' parching, very dry ', KaYKavo(; 
"arid', KayKoivsi GaAnsi, ^npa'vsi Hes., KayKaAsa KaraKEKaupEva Hes.; KaKi0ri(; aTpo(po(; 
apnEAoq; kokiGec; Aijjrips^; kokiGq Aipripa Hes. (in the ending supposed Schuize Kl. Schr. 
329 *5ydh--burn'); 

Gothic huhrus, with gramm. variation Old Norse hungr. Old English hunger. Old High 
-----koksa
47877:Note: (Aryan also *kokso-s)
```


## [2026-09-06T16:09:46.084Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '47870,47910p' POK_full.txt"
}
```


### [2026-09-06T16:09:46.127Z] TOOL RESULT

```
References: WP. I 455, Berneker 656 f., Trautmann 147. 
Page(s):610 

Root / lemma: koRsa {*hogha) 

Meaning: a part of body (foot, hip. etc..) 

Note: (Aryan also *kokso-s) 

Material: Old Indie kaksai., kaksa-m. 'Achselgrube, Gurtgegend the Pferde', Avestan 

kasa- m. "Achsel' (proves -ks-); common Old Indie gh- > ks- 

Latin coxai. 'hip, haunch'; 

Maybe Rumanian coapsa 'thigh' : alb. /ro/fe/7a 'thigh', kafsha ' an\ma\ (*meat)', kafshq/"b\te 
(like an animal)' common Rumanian-lllyrian k^'hs- > phs-, fs-.. 

Old Irish cosst 'foot', abrit. Apy£vt6-ko^O(; perhaps ' white foot ' (but cymr. coesleg' is 
borrowed from Latin); 

Old High German hahs/na' knee bow of the hind leg ', Middle High German hehse. 
Modern High German Hachse, Hesse Bavarian Haxn. 

References: WP. I 456 f., WH. I 188, 283, 858. 
Page(s):611 

Root / lemma: kol(eli- 

Meaning: glue 

Note: 

Root / lemma: kol(eli- : 'glue' derived from a reduction of the extended *glei-b'^- Root / 

lemma: gel-1\ 'to curl; round' [see above]. 

Material: Gr. koAAq ' glue ' (*K6Aja); 

Middle Dutch Middle Low German /7e/e/7 'stick, glue' {*haljan)\
```


## [2026-09-06T16:10:05.869Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== AHD kenk\"; grep -n \"^kenk\\|^koks\\|hanhila\\|hanhilaz\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-06T16:10:05.917Z] TOOL RESULT

```
== AHD kenk
613:kenk-1. To gird, bind. Variant form *keng- in Latin cingere, to gird: CINCH, CINCTURE, CINGULUM; EN- CEINTE2, PRECINCT, SHINGLES, SUCCINCT. [Pok. 1. kenk- 565.]
614:kenk-2. To suffer from hunger or thirst. Suffixed zero-grade form *knk-ru- in Germanic *hungruz in Old English hungor, hungur, hunger: HUNGER. [Pok. 2. kenk- 565.]
615:kenk-’. Heel, bend of the knee. 1. Germanic *hanhaz in Old English héh, heel: HocK!. 2. Germanic *hanhilén- in Old English héla, heel: HEEL!. [Pok. 3. kenk- 566.] kens-. To proclaim, speak solemnly. Form *kens-é- in Latin cénsére, to judge, assess, estimate, tax: CENSOR, CENSUS; RECENSION. [Pok. kens- 566.]
```


## [2026-09-06T16:10:06.446Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== KLN recent/heel/cushion/coxa\"; grep -n \"^recent,\\|^heel,\\|^cushion,\\|^coxa,\\|^hip,\" KLN_1966.txt | head"
}
```


### [2026-09-06T16:10:06.505Z] TOOL RESULT

```
== KLN recent/heel/cushion/coxa
9492:coxa,  n.,  the  hip  (anat.)  —  L.,  ‘hip’,  cogn.  with
17435:heel,  n.,  the  hind  part  of  the  foot.  —  ME.  hele, heele,  fr.  OE.  hiela,  hela,  contracted  fr.  OE. *hohila,  dimin.  of  OE.  hoh,  ‘heel’;  rel.  to  ON. hxll,  OFris.  hel,  hela,  Du.  hiel.  See  hock,  ‘joint’, and  dimin.  suff.  -le.
17827:hip,  n.,  the  haunch.  —  ME.  hipe,  hippe,  hupe,  fr. OE.  hype,  rel.  to  Du.  heup,  OHG.,  MHG.  huf, G.  Hiifte,  Goth,  hups,  ‘hip’,  fr.  I.-E.  base *qeu-b-,  ‘to  bend’,  whence  also  Gk.  xu|3ot;, ‘hollow  above  the  hip  of  cattle’.  See  cubicle  and cp.  hive.
17829:hip,  n.,  melancholy.  —  For  hyp,  which  is  short  for
17831:hip,  interj.  used  in  applauding  (as  in  hip,  hip, hurrah).  —  Of  imitative  origin, hipe,  also  hvpe,  n,,  a  kind  of  throw  in  wrestling.
```


## [2026-09-06T16:10:13.054Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '9490,9496p' KLN_1966.txt; echo \"-----pagemark near coxa\"; awk 'NR>=9400 && NR<=9560 && /^ *[0-9]{2,4} *$/ {print NR\": \"$0}' KLN_1966.txt; echo \"-----near heel\"; awk 'NR>=17300 && NR<=17600 && /^ *[0-9]{2,4} *$/ {print NR\": \"$0}' KLN_1966.txt"
}
```


### [2026-09-06T16:10:14.649Z] TOOL RESULT

```
Derivative:  cowslipp-ed,  adj.
cox,  n.  and  tr.  v.  ( colloq .)  —  Short  for  coxswain.
coxa,  n.,  the  hip  (anat.)  —  L.,  ‘hip’,  cogn.  with
OI.  kaksah,  kaksd,  ‘armpit’,  OE.  huh,  ‘heel’,  and with  the  first  element  in  OE.  hoh-sinu,  ‘hock sinew’.  See  hock,  ‘joint  in  the  hind  leg  of  a horse’,  and  cp.  cuisse,  cushion,  Quixotic. Derivative:  cox-al,  adj.
coxalgia,  n.,  pain  in  the  hip  (med.)  —  A  Medical Latin  hybrid  coined  fr.  L.  coxa,  ‘hip’,  and  Gk. -aXyia,  fr.  iiXyoq,  ‘pain’.  See  prec.  word  and
-algia.
Derivative:  coxalg-ic,  adj.
-----pagemark near coxa
-----near heel
```


## [2026-09-06T16:10:19.918Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"^73[0-9]$\\|^ 73[0-9] $\" KLN_1966.txt | head; echo \"---formfeeds\"; grep -c $'\\f' KLN_1966.txt"
}
```


### [2026-09-06T16:10:21.651Z] TOOL RESULT

```
17792:730
17793:731
17835:732
17851:733
17887:734
17900:735
17937:736
17947:737
17960:738
17981:739
---formfeeds
902
```


## [2026-09-06T16:10:23.665Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '17887,17905p' KLN_1966.txt"
}
```


### [2026-09-06T16:10:23.726Z] TOOL RESULT

```
734
hawwdh ,  ‘tent-village,  village’,  which  prob.  de¬ rives  fr.  base  h-w-h,  ‘to  gather’,  and  is  rel.  to Arab,  hawa,  ‘he  collected,  gathered’,  hiwa\ ‘circle  of  tents’.
ho,  interj.  —  Imitative.  Cp.  whoa, hoaetzin,  n.  —  See  hoatzin. hoar,  adj.  —  ME,  har,  hor,  fr.  OE.  hdr,  ‘gray, gray-haired,  old’,  rel.  to  ON.  hdrr ,  of  s.m.,  OS., OHG.  her,  ‘distinguished,  noble,  glorious,  ex¬ cellent’,  MHG.  her,  ‘distinguished,  noble, proud,  gay,  holy’,  G.  hehr,  ‘exalted,  august, noble,  sublime’,  Herr,  ‘lord,  master’,  herrlich, ‘glorious,  excellent’,  fr,  Teut.  base  *haira,  cor¬ responding  to  T.-E.  *koiro-\  cp.  Mir.  cfar, ‘dark’, fr.  base  *keiro-,  a  vowel-gradation  form  of *koiro-.  Cp.  Herr,  herring,  and  the  second  ele¬ ment  in  mynheer,  younkcr.  Cp.  also  hue. Derivatives:  hoar,  n.,  and  intr.  and  tr.  v.,  hoar-y, adj.,  hoar-i-ness,  n.
hoard,  n.  —  ME.  hord,  fr.  OE.  hord,  rel.  to  OS. hord ,  ON.  hodd,  OHG.,  MHG.,  G.  hort ,  Goth. huzd,  ‘treasure’,  lit.  ‘hidden  treasure’,  fr.  I.-E. *quz-dho-.  The  first  element  in  this  base  means ‘hidden’;  see  hide,  ‘to  conceal’,  and  cp.  words there  referred  to.  The  second  element  in  *quz- dho-  means  ‘placed’,  fr.  base  *dhe-,  *dho-,  ‘to place’,  whence  also  Gk.  -ctffcvai,  ‘to  place’, OE.  don,  ‘to  do’.  See  do  and  cp.  theme.  Cp,  also treasure.
hoard,  tr.  and  intr.  v.  —  ME.  horden,  fr.  OE. hordian,  fr.  hord.  See  hoard,  n.
Derivatives:  hoard-er,  n.,  hoarding  (q.v.) hoarding,  n.,  the  act  of  one  who  hoards.  — Formed  fr.  hoard,  \.,  with  -ing,  suff.  forming verbal  nouns.
hoarding,  n.,  a  temporary  fence.  —  Formed  with subst.  suff.  -ing  fr.  obsol.  E.  hoard,  fr.  OF. hourd,  hourt,  hort,  ‘scaffold',  which  is  of  Teut. origin.  Cp.  OHG.  hurd,  ‘hurdle’,  and  see
hurdle.
hoarhound,  n.  —  See  horehound. hoarse,  adj.  —  ME.  hors,  fr.  earlier  has,  fr.  OE. has,  rel.  to  OS.  hes,  ON.  hdss,  Dan.  hies,  Swed, hes,  Du.  hees,  OHG.  heisi,  heis,  MHG.  heise, heiser,  earlier  G.  heisch,  G.  heiser,  ‘hoarse’. These  words  prob.  meant  orig.  ‘dried  out; rough’,  and  are  rel.  to  OE.  hat ,  etc.,  ‘hot’;  see hot.  The  insertion  of  the  r  in  ME.  hors  is  prob. due  to  the  influence  of  harsh.
Derivatives:  hoarse-ly,  adv.,  hoarse-ness,  n. hoatzin,  hoaetzin,  n.,  a  bird  of  S.  America.  —  Sp., fr.  Nahuatl  uatzin.
hoax,  n.  and  tr.  v.  —  Fr.  earlier  hocus.  See  hocus- pocus.
Derivative:  hoax-er,  n.
hob,  n.,  i)  a  rustic;  a  clownish  lout :  2)  a  fairy.  — Fr.  Hob,  a  pet  form  of  Robin.  Cp.  hobgoblin, hob,  n.,  projection  at  the  side  of  a  fireplace;  peg. —  Of  uncertain  origin.  Cp.  hub. hobble,  intr.  v.,  to  go  haltingly,  to  limp;  tr.  v., to  cause  to  go  haltingly.  —  ME.  hobelen;  rel. to  Du.  hubbelen,  ‘to  rock  from  side  to  side’.
735
freq.  of  hobben,  ‘to  toss,  to  rock’.  Cp.  hopple and  hobby,  ‘a  small  species  of  falcon’. Derivatives:  hobble,  n.,  hobbler  (q.v.),  hobbl- ing-ly,  adv.
hobbledehoy,  also  hobbadehoy,  hobbedehoy,  n., a  clumsy  youth.  —  Of  uncertain  origin, hobbler,  n.,  one  who,  or  that  which,  hobbles.  — Formed  from  the  verb  hobble  with  agential suff.  -er.
hobbler,  n.,  a  retainer  who  maintained  a  horse for  military  service  (Engl,  hist.)  —  ME.  hobler, hobeler,  a  blend  of  OF.  hobin,  hobi,  ‘a  small horse’  (see  hobby,  ‘a  nag’),  and  OF.  hobeler, ‘to  skirmish’,  fr.  OF.  hober,  ‘to  bestir  oneself; shake,  agitate’,  which  is  of  Teut.  origin.  Cp. Du.  hobben,  ‘to  toss’,  and  see  hobble, hobby,  n.,  a  small  species  of  falcon.  —  ME.  hobi, hoby,  fr.  OF.  hobet,  dimin.  of  hobe,  ‘falcon’ (whence  also  F.  hobereau,  ‘hobby;  squireen’), fr.  OF.  hober,  ‘to  bestir  oneself’.  See  prec.  word, hobby,  n.,  1)  a  nag;  2)  hobby  horse;  3)  favorite occupation.  —  ME.  hobin,  ‘nag’,  fr.  OF.  hobin, hobi,  ‘a  small  horse’,  orig.  ‘the  ambling  animal’, fr.  OF.  hober,  ‘to  bestir  oneself’.  See  hobby, ‘a  species  of  falcon’,  and  cp.  aubin. hobgoblin,  n.,  i  t  (cap.)  Robin  Goodfellow;  2)  an elf,  goblin ;  3)  a  bogey.  —  Compounded  of  hob, ‘a  kind  of  fairy’,  and  goblin, hobnail,  n.  —  Compounded  of  hob,  ‘fairy’,  and nail.
Derivative:  hobnail-ed,  adj. hobnob,  intr.  v.,  to  be  on  intimate  terms.  —  A var.  of  early  ModE.  hab  nab,  fr.  OE.  habban, ‘to  have’,  and  nabban,  contraction  of  ne  habban, ‘not  to  have’.  Hence  hobnob  orig.  meant  ‘have or  have  not’.  See  have.
hobo,  n.,  a  tramp  ( American  Slang).  —  Of  un¬ known  origin.
```


## [2026-09-06T16:10:29.854Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '17905,17945p' KLN_1966.txt | grep -n \"hock\" "
}
```


### [2026-09-06T16:10:29.921Z] TOOL RESULT

```
3:Hobson's  choice,  n.  —  So  called  after  Thomas Hobson  (died  in  1631),  who  had  livery  stables  at Cambridge  and  let  out  horses  to  customers  on the  condition  that  they  had  to  take  the  animal standing  in  the  stable  nearest  to  the  stable  door, hock,  n.,  the  joint  in  the  hind  leg  of  a  horse.  — ME.  hough,  hoch,  fr.  OE.  hoh,  ‘heel’,  rel.  to  the first  element  in  ON.  ha-sin,  OE.  hoh-sinu,  ‘hock sinew’,  OHG.  hahsa,  MHG.  hahse,  G.  Hachse, ‘hock’,  ON.  hzll,  OE.  hsela,  ‘heel’,  and  cogn. with  OI.  kaksah,  kakfd,  Avestic  kasha,  ‘armpit’, L.  coxa,  ‘hip’,  Lith.  k'mka,  kenkle,  ‘knee  joint’, cinksla,  ‘knee  sinew’,  OIr.  coss,  ‘foot’.  Cp.  bough. Cp.  also  heel.  Cp.  also  coxa.  For  the  second element  in  ON.  hd-sin,  OE.  hoh-sinu,  see  sinew. Derivative:  hock,  tr.  v.,  to  hamstring, hock,  n.,  white  Rhenish  wine.  —  Orig.  ‘wine  of Hochheim’,  abbreviation  of  obsol.  hockamore, ‘wine  of  Hochheim’,  fr.  G.  Hochheimer,  fr.
6:hockey,  n.  —  Prob.  fr.  OF.  hoquet,  ‘bent  club, shepherd’s  crook’,  formed  with  suff.  -et  fr.  OF. hoc,  ‘a  hook’,  which  is  of  Teut.  origin  (cp.  OE. hoc  and  see  hook);  prob.  so  called  because played  with  clubs  hooked  slightly  at  the  end.
```


## [2026-09-06T16:10:38.129Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"Achsel\" BRT.txt | head -20"
}
```


### [2026-09-06T16:10:38.200Z] TOOL RESULT

```
6146:•  j.  3a&i-  in.  'Achsel':  'ifayh  (GD.)  F.^g.
9456:•  j.  'kasa-  m.  Achselhöhle  :  dastmm  ■  ^L  vgl.  *r7>onii«j.  Adj.  'begehrend',  drao- (bz.  Ajf^/n)  'W/W  V.  Ä  48-50*,  <?.  17,  18^;'  Adj.  'carus'.  —  S.  noch  kima-.—  Pü.  (lu  Y.): —    ;;aV    hts    bardii    nfa    'Um    N.  2.?;  — '      =^ähll.%ü.isamlhau;  (zyi^^^y.tallihinim   -
21701:schnui  umbinden,  umlegen':  iva  i^ra aiwyitthayänte  atairi  iasatibya  cvat  am- xyhTskayinti  "wo  sollen  sie  hier  die  Gürtel I  schnür  anlegen?  Unterhalb  der  Achsel- höhlen. In  welcher  Grösse  sollen  sie  si- I  anlegen?"  N.iSj;  —  aiwyasta^^  maidas •^yasna  gli^ä  srävayaf  «Sil  anaiwyOsta  (sd.) 'N.(?5;  —  ya%a  ia%aca  dakmd  staota ,yesf>ya  haurva  dahäiti  .  .  barymns  v3 vaz?mnS  va  aiwyastS  a%a  raA(/"nT  "wie
```


## [2026-09-06T16:10:38.646Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"kainin\\|kainin-\\|kaine\\|kanya\\|kainika\" BRT.txt | head -20"
}
```


### [2026-09-06T16:10:38.699Z] TOOL RESULT

```
2469:—  lia  yaoilayö  .  .  ärmalayö  vatiuhxm iibls  ahm  . .  yazamaidl  ". .  sammt  denen die  gute  A.  .  ."  \.^8.2;  —  ttm  yaz>nia kainina  . .  äa>al  aibyasHt  (DPf.)  tat  avat •lyaftim  YL/j.41;  —  Hwqm  iaininö  .  . "iwam  earilitis  . .  jaioyante  . .  tum  tä aiibyö^  nisirinaväki  Yt.  5. 87 ;  —  mit  Nu- merus Wechsel**:  yeii  arskat  anästUtS  vä anaiwijravanS  (sd.)  v3  dalnqm  aitäeit aäbyS   *s^aaAaiti   3stavanalil>yS  V.J.  40;
2533:*'te  *yffi'^  fracarinti  , .  aiialiqm  .  .  N.  ,paiqn  ,  ,  'na  ,  ,  triltm  k>hrp}m  hvan.- ^.  III)  In  folgenden  Fallen  brauchen  i  t/arwr« -f?rv«aii/V.  5. 13,  3)  'dann'  im wir  den  Sing,  mit  'ein'  (unbestimmter  Ar- !  Sinn  von  'in  der  Folge'  und  'in  Folge tikel),  den  Plur.  artikellos  (vgl.  ^aisa- 111}  j  dessen',  einen  Zwischensatz  hinter  einem yesica  .  .  upairi  'l^m  iristim  .  .  Ajr^zy^lf '  SaU  mit  yai  einleitend:  y^i  ndii  nidan- yaia  .  ,  "und  wenn  (man)  .  .  auf  einem  sayilnte  —  ''ja  kl  alte  sünö  vä  .  .  fraja- Toten  ..  liegen  lässt  .  ."  V.5.61;  — yö\s,yi>  —  kä  Af  asU  äiaX.ö.^T,  —  yaii'a vastnm  upaiiharizatti  upatri  °t»m  tristem  |  vaoeäp  aiSö  m7  Aanqm  .  .  p3r>saKuAa  — "wenn  einer  ein  Gewandstück  auf  einem '  "'la  ae^a  y<J  kaine  hanqm  . .  p?nsaili  , .  — Toten  liegen  lässt"  V.Äaj;  —  bei  rela- 1 'ort  assa  yS  kaine  altahmat  puir.lt  *mi- tivisch  angeschlossenem  Nomen:  yat  "te^  manxlstti  —  '^Aapanta  .  .  vfri^qn  .  . yöi  tnazdayasna  . ,  taci.apaya  nasSum  fra-  [  V.  /J.  1 3  f. ;  —  yeii  mit  Aari^nm  baraili jasqn  "wenn  Mazday.  auf  einen  Leich-  -  "da  aisa  yö  afirinüyakö  adJityö.an- nam  in  fliessendem  Wasser  stossen"  V.  6.  Aarj^nin  (sd.)  iri^ät  —  ^'>para  A!  iri- 26;  <y.73,  7-36.  \sittt5  rais?m  cikayat  .,  V.7j.i6.
2561:'''tt  *yöP^  fracarmii  . .  aitaSsqm  .  .  N.  patan  .  .  'oa  .  .  agtJm  k>hrp>m  hvar».- ij.  III)  In  folgenden  Fällen  brauchen  j  i/awjrjw  fo/vwuc/ V.  5. 1 3.  3)  'dann'  im mir  den  Sing,  mit  'ein'  (unbestimmter  Ar- 1  Sinn  von  'in  der  Folge'  und  'in  Folge tikel),  den  Flur,  artikellos  {vgl,  ^aila-  III) '  dessen',  einen  Zwischensatz  hinter  einem jcsVJ  .  .  upairi  'tim  iristim  .  .  k>r>zyllt.  Satz  mit  ytzi  einleitend:  ye:i  mit  mdart- ya>a  .  .  "und  wenn  (man)  .  .  auf  einem  l  sayanfe  —  'ca  he  alte  sünS  vä  .  .  fraja- Toten  . .  liegen  lässt  .  ."  V.  5. 6 1 ;  —  /^ ,  JiW^  —  kä  hl  asti  Wia  V.  6".  47 ;  —  yesila vastnm  upaifharizaiti  upairi  ^tfm  iristtm  ^  vaocät  aSsö  nä  hanqm  .  .  p>r?sat3uha  — "wenn  einer  ein  Gewandstiick  auf  einem  .  '<,a  aSsa  y.J  kaine  hanqm  ..p^nsititi  . .  — Toten  liegen  lässt"  V.  ^'.23;  —  bei  rela-,°ö(J  a^ia  yä  kaine  aetakmut  puir-at  *mi- tivisch  angeschlossenem  Nomen:  yat  °te\mar?x^iliti  —  '^hat<anta  .  .  7>)r?zyqn  .  . yei  mazdayasna  . .  taH.apaya  nasHum  fra- '  V.  /5. 1 3  f ;  —  yai  nöii  har^'^nm  baraiti jasqn  "wenn  Mazday.  auf  einen  Leich-  —  °ofl  aila  yS  ap^rinlyükö  adaityo.at3- nam  in  fliessendem  Wasser  stossen"  V.  6. '  harsirim  (sd.)  iriiyäi  —  ^para  he  iri- 26;  ^.73,  7-36-  \Hntö  raSsim  cikayat  ..  V./j.iö.
2801:Irrlehrer,  der  . ."  \.g,$i{.;  —  yavat  °fa *gaintii  upankacaili  (sd.)  V.  7.  56;  — yavat  'sa  ilß  bySrixfi  (sd.)  .  ,  frabavai \.i4.\y,  — yavat  -lö  spä  anya{sA.) )asö V./5.48,  a)mitrelativischemAnschIuss: "jS  zT  asti  baslazyö.t3mö  .  .yal  *mahnm.- sppni»m.baei'azyd  (sd.)  V.  7.44;  —  '/a  bi~ paitisiana  (sd.)  y3  kaine  V.  75. 19;  19;  — vXsp»m  ä  ahmst.,  yat  -ia  yö  apsntinyBkB uxjasnf  (sd.)  "bis  es,  das  Kind  . ,"  V.  75. 15;  —  'sa  yS  *ar?mBiidd'a.W3.  2)  auf ein  Relativum  als  dessen  Korrelat,  sub- stantivisch: ci'at  dra)ö  avaMUlüt  '^a  yö näirikaya  . .  !^ar>^3tn  frabamt  V.  /J.  4 1 ; —  °sö  .  .  aitayä  vihrkayh  (sd.)  Jq'^-wS.' tarö  *at3kat  . .  ya^a  spä  vtkrkake  k»r?- naoiti  V.  y .  4 1 ;  — "/?  ratufris  *yö  jayara N.if};  24,  60;  —  'sa  yetjhe  apirinSyükö ^•9i  7;  —  °^'''  zaoiranqm  tnaziltaca  . . yiJ  *naire  asaone  *daste  N.^4.  III)  In
3664:—  ym  'k3  frashavat  (sd.)  satta  ki  paoi- rfm  frasnäoay^n  aitahe  yat  'kahe  V.  16.  ^ ; /J.44.4S;  —  näirika  'kasiaV.3.\\;y, — nitrHatüt  •iahecil  N..40;  —  näirikqm w  *'ibm  (va)  N.  105;  —  nairinqmca 'ioMOMca  kainikanamca  Y.6S.12;  —  ttai- riie  'keQ)  kainike  Y.'2?.5;  —  nairikqm ..  mbmtmiit  (sd.)    "Awi^V. 5.38;  75.48;
4489:•  j.  an-upaeta-  Adj.  'noch  nicht  zu  be- gatten, noch  nicht  reif  fiir  — '  (Gen.),  von Mädchen:  ydi  kainina  °ta^'>  masyänqm "Mädchen,  die  noch  nicht  reif  sind  für Männer"  Yt.Z/.sS;  S4.  J5-39-
4820:—  zu' :  xshms  asamqm  unänö  pärayeinii . .  avi  garS  nmänam  V.  75.32;  —  x3  patti apqm  paräiti  .  .  a^ra  . .  V.  jj.  51;  — xraosyS-taraca  (sd.)  .  .  hv5  urva  paräiti par3.asnäi  amihe  yaia  . .  V,  13. 8;  —  ya- tärö  paurvs  us>hiUaiti  paräiti  vahiltahe atshsus  y .  iS.^d.  2)  'aus  (dem  Haus) gehen  auf  — ,  zum  Zweck  der  Verrichtung von-'  (Akk.):  *kat!lmS  timänahe  a'iauru- fi9m{sd.)  pärayäf^''  N.  /;—  para  paoiryö äiti  (näml.  a^aururitm)  para  bityö  aiti para  "hrityS  äiti  aita  paräyaiti  ycc^a gae'^äbyS  *k)nti  "es  geht  der  erste  (auf Priesterdienst)  aus  . .  der  zweite  . .  der dritte.,;  es  gehen  die  weg,  die  (zum  Schutz) für  den  Hausstand  da'gelassen  worden) sind"  N, 2 (?)"'; — katärsm  *ä'irava  ctiauru- n>m  Vä  parayat  galiaiiqm  vä  asp^nns (sd.)  avat  N.^;  —  katärS  a'^aurun?rn ''parayat  nSirika  vä  nmätiSpaitiH  väi yezica  vä  ga^hä  vTmä  (sd.)  *katarascit ''parayat  N.  5;  *5";  —  *cvät  ''aiwtstXm parayap  'irixsapar>m  .  .  yS  haoys  (sd.)  . . paräiti  nsit  .  .  anaiwistim  (sd.)  ästryanti N.  4.  a)  mit  haca  und  Instr.:  cval  .  . äiirava  a'iaurumm  haca  ^gafi^äbis^para' yat  N,  4-  3)  'sich  an  etwas  (Akk.) machen':  yö  nar)m  ..  kasyat»he{%d.)  sanhai daoaili  vl^va  aval  hava  xraiwa  paräiti "—  wissentlich  mit  voller  Absicht  macht  er sich  daran— "V,  15- 2.  4)  'hingelangen zu  — '  sva.  'sich  verschaffen':  ffi.j(Akk.),. kaine-.tarS  äaxit^m  pärayät  tarS  ap»mca urvarqmfa  yezica  . .  tarS  (sd.)  daxst>m paräiti  . .  "nicht  soll  das  Mädchen  heim- lich sich  die  Regel  (wieder)  verschaffen, heimlich  sich  Wasser  und  Kraut  verschaf- fen .."  V.i5,9f.
5397:•  j.  auru5a.bäzav-    Adj.    (auch   : 'weissarmiß':  kaininö  kihrpa  . .  "Zfh  \^o.,  .  ^  ,,     ,
6193:AaSmnä  W.öo.^;  —  Aaomanam  •A»7  .  . eistsis  basidsa  haHmnanqm  Vr.  p.  i ;  — yamäüa  .  .  yat  /aymasyS  'Ms  .  .  ratu/ri- tsi/Vr.g.S.  a)  sonst  mit  vauhav-  Adj.: 'silvanuhi  srTra  xssi'kni ..  kainins  kfhrpa srTrayä  Yt  13.  107;  —  'stm  vaauklm x^Bii-nXm  bsrfsaitlm  .  .  dv/oarym  ahurahe mazdi  li'aKhanm  aimsanqm  spmli Yt77.i  f.;  3',  18.2,;  —  kubaotiäl  baohaite timäfum  yetihe  nmänt  °Hi  vamthi  süra paha  nida^aite  \t.17.6;  —  upa-staota yasatanqm  .  .  patH-stayata  rai^ya  'sif" vanuki  yi  b^rxaitiMX.i'j.i'};  21,  26,  54, 57.  58,  59,  ro.68,  7Ä4;  —  ava£  ayapUm dasäi  MI  'sis  (als  VS.)  vanuhi  y3  btr^saiti YL  77.  25;  6,  7;  —  vaauhim  .  .  ädqm vaauhtm  -hm  aca  mla  mrümaide  Y.  '68. ai;  Vr.  ^i;  —  mihnm  .  .  yim  kalaite 'Tis  vanuhi  parmdica  Yt/0.66;  Ä38,  Y. 13.  I,  Vyt.  8;  —  'ssis  vanhuyh  eistsis tmnkuyä  Y. /.14,  V. /p.39,  Yt. //.  16;  — sraoss . .  •«/  vatfuhi  iha  milbnatu  . .  upa imai  nmilTum  Y,  10.  i;  i,  57.  3,  Vr.  7,  i, 7/.  16;  —  ■■//«  vatmklm  .  .  ^ar»nJ..  sofS mazdaoähm  Y.  2. 14,  8.2.25;  Y. /(».ö;  — :x?ahr3Jisyeie  (sd)  paiti  '/si/ck  vanAuyä dar3i?m  haxma  Y,  60,  7,  a)  'söis  va- ti/iuyj.  (näml,  ayan')  heisst  der  25.  Monats- tag: °Ms  vanhuyh  BstSis  .  ,  ^tp^J  .  . pärMdyä  S.J.2S;  vgl.  2.25,  \.  16.6. •«/  FrD.  7  (?).        [V.  4- 45-  lies  asWa
7536:•  j.  'i-zäta-  Adj.  (fem.  Ha-)  'adeHg,  edel, vornehm':  °ta  F.  7;  —  kainins  . .  "tayi raevasci^raya  H.  2.9;  —  kainlnö  . .  rafvat ai^r^m  (sd.)  °taya  Yt5.64;  —  'tarn  hutao- sam  Yt9.i6.
7554:Nur  Med."*  i)  'sitzen':  iisfe  F.  7;  — *Äist?mnö  vcl  anhand  va  "stehend  oder sitzend"  N.J7;  — frataire  gätvs  st^ha- nqm  fratarSJairt  (sd.)  gati'd  niiäoaysis H.  2. 14;  —  yaihe  .  .  vispähu  paiti  ban- zähu  . .  spasff  auhäire  (3PPM  )'>  mvirahe Yt.  io. 45 ;  —  a2sqm  vatitn»ha  ..  gatui paiti  *ar»h^nte*  <'  "ihre  Frauen  sitzen  auf dem  Lager  Yt/7. 10.  a)  'da  sitzen': aisqm  kaininS  Stfhinle''^  qymfipaiois(ad.).. YLiy.ii.        z)  mit  a)  Mj.  oder  b)  Absol.
7648:•  j.  «r«dat.fadrt-  f.  EN.  der  Mutter  des Astvat.)r>ta-  (sd,)*':  kanya  "fiuryä  asaottyfi .  .  ya  visßa.taurvairi  natna  Yt/j.  142.
7738:•  j.  «rszvant-  Adj,  (fem.  'vaiti-)  'gerad- gewachsen, stramm':  kainind  k;>hrpa  srJraya .  .  uskäi  yäslaya  'vai>yB  (GSf.)  Yt.  5. 64.
8478:—  mä  .  .  kaine  .  .  tarS  daxslim  pärayat (sd.)  tarö  ap?mca  (sd.)  'ramea  V./5.9; 10;  —  avi  tu  dim  disyata  (sd)  yä  apasca 'r-hca  zao>nhca  Y. A3,  a)  Du.  in Verbindung  mit  sp-  Du.;  yat  iurmaot a»haosimne  äpa  (Sh-erz.)  °vaire  Y.  9.  4; usw.  2)  mit  einer  einschränkenden Bestimmung :  aisma  .  .  yat  vä  aitaaham  . . 'ranam  yat  ätn.ciiranam  V.  ^75;  — altayh  °raya  aian^ar?}  V . S.-j ^-y  —  upa .  .  nmärum  baoiayaH  un-äsnayä  fä  .  . kamcit  v<l  hubaoi'At^manqm  °ranam  \.S. 2 ;  —  aoa  az»m  yS  ahurö  masda  °rä  bal- iasy'i  uzbamn  ".  .  die  Heilkräuter  . ."  V. JO.4;  —  ynän^m  vä  .  .  kamcit  vä  vlta- afianam(sd.)°ranainY.ij.i4; — yavanqmca vtlstranqm^a  'ranqm'a  :far?i5.bairyartqm (sd.)V.J.4;  —  'raaqm  s^awrlranqi'i  (sä.) Yt/>5S;  Vr.2/.i;  —  'rShu  paiti  barss- manyäku  Y.  2.11,  "Y't /0.14s;  —  imqmcä 'rqm  bansmanim  Y.  22.3,  a)  durch Namensnennung:  aetayh  *rayh  ya  i-aoÜ ha'jana^aia  V.  14.  4;  V.J.  3,  22.  i,  62.  9
8848:—  icayö  äal  ('quaenam')  aSe  raocä  (sd.) aw/ij«.._f?..  V.2.39;  iMia.  a)  Kopula fehlt:  kai  vS  xsa^rim  kä  T/tls  (sd.)  syao- :^anai  Y.34.5;  —  60  *qst0  *iä  *tarö.- maitiP'>  ti.41;  —  kä  yä' kaine  Y. 14.11;
10090:Des.  '(zu  gewinnen,  zu  erlangen  suchen sva.  fUr  seinen  Zweck)  ausfindig  zu  machen suchen':  yeiica  vaccill  a!s3  nä  hanq> aaa^qm  (?)  *jijiiaauAa  pinsanuha  aOaia (sA,  3)  aisa  yä  kaine  hanqm  aäal^qm *ßjis/fiti  pinsäiti  "und  wenn  der  Mann sagt:  'such  eine  Alte ..  ausfindig  zu  machen, frag  sie!'  —  das  Mädchen  sucht  dann  .." V.,5.,3f.
10732:Undeutlich:  '^wqm  kainind  vähre yaona '"hra  . ,  jaiöyänte  Yt5.  87;  —  nava  dru- jaiti  '"kra^byS  V.4.  10  PUZ.;  —  '%r?m' Vyt4S;    —    '^rd!    DkB.  131.  '"ir^m
11844:J^.  7  2 ;  —  nsit  kau  *'mS  yö  nsit  asa  *°mS P.  47  '* ;  —  'mumca  nmänö.paitlm  Yt  5. 8  7 10. 112,  /7.1z;  —  hsuca  'manam  tanci'tö P.25;  ~  hlu  (näml.  kaine)  ..'"ma  (NSf.) V./5,  30;  —  °mS'ä:raaaonB\t.^.(i\,  14-40, ig.  91;  87,  J.  105,  117,  /J.  99,  Vyt26';  Vt. 5.11,  Az.3;  Yt7jj.  28;5.  53,  58,  19,  42; ^■9^»  I03i  ■<'6'  •'^1  '37-  ^)amjsimam ippntanqm  ..  "manqm  Y.  26".  3;  —  vaini 'manqm  taxm5.t»m3m  Vt.  75.  57;  —  vätS "BiJ  V.j^i.  13,  Yt  J5.46,  Vyt.24;  Yt/0. 127, Y.7.  26,  S.2.30,  Y./.  IS,  2.  15,  7/.Z3;  Yt. JO.65,  140';  Y. 57.  II,  33',  j.  20,4-23.  V. J&I4,S./.  17;  —  vays 'ma  (VSm.)  Yt. 75.  57;  —  fravasls..  'mä  (AFS.)  . .  tana/ta Yt7j.  7s;  32,33;  —  aj  %7VS  mSnghai 'miniüä  spmltm  mazdä  "für  einen  starken und  heiligen  will  ich  dich  halten,  o  M." Y.  43-  4-  b)  von  Tieren;  vamsahe  .  . 'mähe  Yt.  74. 15;  —  -mähe  ttunyahe  Yt. 74.  36'. KompA,  E.;  Ableit.  —  Vgl.  tqsyai-,  lanHsla-. —  np.  lahm  'stark';  mp.  VgL  lak,  laklk;  ahd. vgl  digan  'Held'.  — Pii.:  taklk  (im  PPG I.  mit nhv  erklärt),  Npii.:  zürSvar.  —  ')  So  nach Pü. ;  lü  an  lakik  kl  nl  pa  akräkih  laklk.
12100:•  j.  tauruna-  Adj.  'jung'  von  Menschen und  Tieren:  yS  yaiia  pu'hnm  "mm  hao- mam  vanäalta  masyS  "wer  den  H.  wie einen  jungen  Sohn  lobt"  Y.  10. 8;  —  spä 'äj  "ein  junger  Hund"  V, 5. 30";  —  spämm .  .  yim  »ffw»  V.  13. 1  $,  23,  27».  a)  m. 'Knabe':  ma  apinnHyu  'na  mS  kainina anupaitä  (sd.)  mafyänqm  "nicht  unmündige Knaben,  nicht ..  Mädchen"  Yt,/7. 54;  55.
12441:asahya  axäyai  (sd.)  ggnedim  Y.  37, 17;  — aiäunqm  . .  uruns  .  .  kudüJiatanqmAt  .  . yailqm  vahehl^  'na  vanainti  va  vSnghm va  vaonarS  va  H.  3g.  z;  —  karapanS kavayasca  .  .  ySng  ^S  urva  ::^a!^a  xrao- dat  (sd.)  'na  Y.46.11;  —  Ö  dngvats *tnandaHg  *9r?tael  (sd.)  haihim  yehya urvü  xraodaiti , .  Y.  ji,  13;  —  tsm  *vä ahsm  dtTgvantS  .  .  'na  nailal  (sd.)  Y.^y/. so;  zT.  verwendet  V.f.  fia;  s.  a;  —  ySi .  .  aiäm>m  vandtn  (sd.)  . .  töi  daoiStig dqn  yS  drsgvats  °na  ",.  die  —  in  AnDaiva Haus  fUr  das  Ich  des  ^rv^enossen!"  Y. 4^.  4*>.  a)  im  jAiv.:  alaonqm ..  ahümla 'nam/ai*  iaooasäi  urvänsmca  fravaiSmia yagamaide  Y.  a6.  4;  —  asni  iyazamaide\ manä  . .  °nä  [yazamaidi]  saoryantqm  yaaa- vtaide  Yt  13.  7^;  —  aisS  zT  växs . .  a  va^S ahunB  vaityS . .  uruna^a  'tiaca  (IS.)  span- vanti  (sd.)  H.  J.  4;  —  'nqm  .  .  yaoldai- är/a  dha  zl  aifihä  asH  yaosdaitis  kahmai- Ht  ..  havaya  tnsvS  'naya  yl  hvqm  'nqm yaozdaite  humataisla  ..  V.  10.  19*';  —  um vä  ahOm  drvaniö  *^a  *'na  msirtnttyJJ [a/isiäi  a/fuhe]  V.  5. 6a;  —  aiiihä  dim vütaya  fr-Jmita  (sd.)  salayeiti  ya  hava 'naT>  kaininS  k>hrpa  srlrayh  .  .  aat  Alm aoxta  ..yS  nars  asaonü  urva  alca  Karditis ahi  ..?  äat  hl paiH.aoxta  ya  hava  'na  .. az?m  ba  U  ahmt  .  .  yä  hava  'na  *:^ai- paihejanvö  {sd.Y'  H.2.9— 11; — arahvam 'nqm  V.^.ai  PüZ.s),  io.  19  PüZ.
```


## [2026-09-06T16:10:44.355Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR>=9200 && NR<=9500 && /^[0-9]{3,4}$/ {print NR\": \"$0}' BRT.txt; echo \"--- context 9450\"; sed -n '9440,9460p' BRT.txt | cut -c1-200"
}
```


### [2026-09-06T16:10:46.360Z] TOOL RESULT

```
9266: 453
9269: 454
9345: 457
9463: 463
--- context 9450
komplr.  itt  :*o«i-.   .-  mp.  *^^,  np.  kih.  -  Zeichnung  einer  Klasse  von   (männlichen
Pö.;  km;  s.  No.  I.  —   ■)  Pü.!  ke  mart .  .  ö  Und    weiblichen)   Wesen   der   A/i/ischen
an  I  iämai  ,,  :iajS.  erl.:  ta  sai^an  i  5  öi<m  Schöpfung:      Aamtstayas'a     nühntayal^a
Aj.«7i  ifl...^.)  AndersDsT.ZA.2.221  nach  .^„„^^^     ^i^i„am:a  .   .     'lakeca    -mhca
Dk.  8.  44-  57(?).  y_  ßl  ^                 *                                         -"
•  j,  kasvika-  Adj.  (fem.  'kä-)  'ganz  gering-  Ableit.  —  E[g.  vU.  'was  für  ein  (abscheulicher) fÜgig':  'kamcina  yanhuyanam  (sd.)  avan-  schwarzer  (Kerl)',  ilal.'negraccio'.eb
Abtat  III  ii,«..  -  IV:  i./.*.  _  ^„    ,jL  ^^,„.  ,i.i,w.(«ii,i  •♦.,,..
•  j.    kasvis-    1)    m.    Name    eines   Ge-j     .i;,  m,-'.  s.  hbm.  KZ.  z/.  104.  AGr. /.  162.
brechen.,  einer  Kranklieit  od.  dgl..   »13,     T,l^::J;'ZLtXZ}X'\''TJ'r7„,Z,Z '  .    ,„^,  I      deutsche  Bauer   bezeicbuet  nie  Zigeuner  als
ii:jr-<j  frakavB  .  .  ml  'vis  (NS.)  mä  -braune  Teufel'.  —  .)  Zs.  15.  1  macbt  das Z'izbärii  V.2. 29.  a)  als  Dal!'a  perso-'  Wort  lum  EN.  —  3)  Vgl.  zu  kaxuii-. nifizirt:
EbPSlammansatzunsicber.  —  Fu.:kdnddnn3>.  _
—  0  NA.  ma^ajr-.  —  "  Der  Vergleich  mit]  •  ).,  g.  KS-  V.  'verfangen  nach  -. ai.  karfku-  f.  'Krätze'  (Bthl.  Stud.  1.  53)  istj  Praes.  27  kaya-,  Perf  I  idk-;  l-KaX.  
.'   '"  ;  ,  ,         1     'verlangen  nach-,  wünschen' :  fravasayB
•  1.  'kas-  V.  lehren.  Praes.  i  oir-.  ^j   jj^„i  „„-irnK   diaytnl,   Jlins
I)  lehren,  mit  Dat.  der  Pers.  und  Akk.  ,j^a//^,„  /ajtu/i  Vt. ;.?.  24.  a)  spez. der  Sache:  ^'it  'ttra^äli  (sd)  'mqinm  ,g„„  t,.„„„  i^^^^  wollen',  auch  mit ail,n  N. 
eJ^re':Tr''."denXS'el^.,:'sS-3"'-  "»  i'"  »»»'l»  "«'l'  rahUtaMai.yav ai.  f<i.r/c  'er  sieht",  mp.  i//o/tf«r4  (s.  lu  z^K/qi,  kennen  lernen  will,  die  Landwirtschaft P0>,  äj/itt 
•  j.  'kasa-  m.  Achselhöhle  :  dastmm  ■  ^L  vgl.  *r7>onii«j.  Adj.  'begehrend',  drao- (bz.  Ajf^/n)  'W/W  V.  Ä  48-50*,  <?.  17,  18^;'  Adj.  'carus'.  —  S.  noch  kima-.—  P�
■    -  "  s-      -I         »T    o  -   -1      ii    T7  I       ■)  Nim ,    virnveidyii.     —    »)    Vgl.   iSt.  Gdn,
v..iak,a-  m.,  mp.  (Pu),  np.  .*a.-;  vgl.  af^.  kse  ^      ^^j,j,^_     ^*   '«  *■     J .       ."       >  ,J.   ,  .  ■         ,1  '  j.  iJ<J/?aö«flBam  Aog.  77:  lies  ^'J'%,f3fli
•  1.  'kasa-  m.  Sichzutunmachen  mit  — "';  .  ,,  ,  ...  „nm  n  j  i»  n ,,.'  ,,1  •  1.  'kala-  Adj.,  PPiP.:  s.  'kan-  und  «a-'J. UartUDg  ')                                   
KompE.  -  Aas  ir.  'kcHa-  (.g1.  i»«ya-i  S  ^/?.        entscheiden,  «ohin  -i^/«.  gehör..
```


## [2026-09-06T16:10:54.013Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '9266,9350p' BRT.txt | cut -c1-190"
}
```


### [2026-09-06T16:10:54.063Z] TOOL RESULT

```
453
karst-  mit  apa
karapan-
454
irisyst  (soll  heissen)  "sie  sollen  nicht  an M.  OperationeQ  austUhren,  und  nicht  soll  er durch  Operationen  Schaden  tun,  .  .  .  wenn sie  Operiren,  wenn  er  durch  Operatio
mit  apa  'abschneiden':  yS  süne  ,  .  apa vä  hl  pai'iyqnt  kirntiaiti  V,i_j.  10.
mit  aipi  'ab-,  entzwei-,  in  Stücke  zer- schneiden': hakat  vTspi  aipi.kgr^titaiti "alles  schneidet  er  .  .  in  Stücke"  Yt.  JO-  7  2 ; —  i'JiÖ  massdd.fraoxia . .  yüi  a
mit  avi  'entzweischneiden'  (?):  yS  ras- mattS  k»r3ntaydti  .  .  avi  rasmanS  k9r>n- tayeiti  ,  .  v»ri^rafnS  Yt/^.öz,
mit  3  'durch  Schneiden  gestalten, schaffen',  von  AAura:  azjm  y5  akurö mazdä  yas?  tal  nmämm  äk^rtfum  V.22.1. mit  upa  Tiineinschneiden  in  —  (Akk.), anschneiden':  daü
mit  paiti  und  ava  vll.  'hineinschneiden bis  auf  — '  (Akk.):  aya?ihalnsu  kantais azdibls  (für  AP.)  paiti  ava.k>r>i:ylt  "mit eisernen  Messern  soll  man  (ihm)  bis  auf die
mit  fra  oder  fraca  i)  'zerschneiden': matdayasna  ai/ä  vasträ  fraca  k^rintm ni/a  kaftay.n  V.  7, 12;  —  ^a%warJ  da- raonä  frakTrmtmti  aiwi.:i'ar>nti  Vd. 10.  a)  'durch  
und(far*w«/)**jr/H/fl,  PPA.  —  31  Es  handelt »ich  um  eine  Straftnarler,  Vll.  ist  azdibii  als Subj.,  k3rf%yäl  als  Pas5.  (mit  Aktivendung)  za nehmen ;  'die  Knochen  sol
•  p,  karta-  Adj.:  s.  unter  'iirjta-.
•  j.  'karata-  m.  'Messer':  ayanhalnäi^ °tsis  azdibti  paiti  ava-ksrii^yät  (sd.)  V. 4-50-  a)  insbes.  als  Waffe,  'Dolch- messer, Dolch':  yallam  zeyanqm  rdiniM ,  .  bityd
ipi'kir/ntai'til^'^'^'^^''"  Yt.;4.27;  —  "'■'«?«    -^'^y^-- 5  \d3ranam     hukintanam     '"'*  '"  --■■
'ta  (IS.)  . Yt/0.42;  —  imäsf  tl srvä  hyär»  arllayas^a 'tayasc'a  iaP.y  V.ij.g.
KoropA,  —  Zum  V.  iarit-.  —  Vgl.  ai.  kattari- t.  'Jagdmesser*,  np.  iärif  'Messer'.  —  Pü. : iärl,  {lu  V.  14)  erl.:  sampi/r  'Schwert'.  — ')  Wie  von  einem  j'-
•  j.  "karata-  m.  Name  eines  Kleidungs- stücks (?):  yS  aiwySnkayäite  °tssca  aratu- /0'jN.cV7(?).
Vgl.  n-irtiay  und  Blocket  RL- JJ-  187,  der 'guenille'   übersetit;    anders  wieder  Lex.  56.
—  Pü.:  iarßn(}). j.  karitayasca  V.  //.  9:  s.  ^karila-  mit  No.  1.
•  j.  karatö.d^sav-  m.  Name  des  Hahns:
aisS  mirjrjs  ys  parB-dars    aisS  mjriyS  yd
°sui  ä'kirS  väcfm  surunaoiti  FrW.  !0.  41.
Eig.  'mit  Messern  (d.  i.  den  Sporen)  beissend
(d.  i.  verwundend)'.  —  "dqsav-  Adj-,  lum  >i.
V.  däsali'i  vgl.  'dqsHra-,  —  Ptt. :  kartak  därüin^).
—  ')  So  nach  DsT. ;  ob  vielmehr  iiii-/«^  i/a»- i/öh}  oder  iärlai  fa5isn  (zu  np.  gaiidan)?
j.  kar3tö.baeäaza-  Adj.  '(Arzt)  der  mit
*drujim  fraca    kinntat   anrS   otj,«^»/ dem^Messer  kurjrt':  >a//ffKrK.^a?/<i3a  (sd.) Y.o.  8;      yä    aurS  hanjasaiite  °z!sca  (NS.)'>  urvarS-ialiatSsca
urvarS-balsatSsca ma^rS.balsasSsca  V.  7,  44;  —  °zB  Yt._j.6.
Pii, :  ke  pa  kirt  biSaziiüt.   —  ')  S  ^OJ  H-  43-
•  j.,  g.  karapan-:  karafn-  m.  i)  im  gAw.
Bezeichnung  gewisser  der  sa^^^w^schen ^f.'skoHami)  'ich  schneide';  iW/aä)  'ge- 1  Religion  feindlicher  Lehrer  und  Priester*': Mhnitten';  m^^>^^W«0.^-Pü.^*^^^  '/''    "^''^''^
II  .)f*;,L!'-o7/"jriTverstiimmelteUä'ä  kavä  ..\.44-  2°;  —  .V^'^-  *grihm<l Formen.  Man  erwartete  »i^^jr/jK/j/,  »i-riHÄwA  [(sd.)    aM  varata   'pa   xsairimcä    Tianqm
<wi   yam    gae%q
mamyui  fräksnntal  avi  imqm  tanüm  V.
20.3;  Aog.  ÄiV;  — frakirfste'''^    asts.
i'ioüiuf  Aog.^/'i  —  s.  noch  frah^rfsis.'.
ai.  kr-Hiäti,   ijTitayaä.  iftyätc  (Pass.);   k^tläh\
dby  Google
45 5  karapan-  2  —  Ttars-  456
*drußtn  \. 32.12;  —  nSit  urvä%ä  datsi-\     KompE.  —  PFP.  zum  V.  ^kar-.    —    ai  vgl fyas/tl  -fanB  vastrSt  arSm  (sd)  Y.5/.14;       *"':'■''■■  ^-T'-^""  ') 
für  gewisse  Feinde  des  Volks  und  Glaubens.         '  _        ,       ..-.,.  1    -,
ä»  MazdayameT*h    vis/an^m  tbihatam   '  \  l^urvo^aosa-  Adj.  ^«'1  kahlen,  tin-
pairikanamca   'sihram    kkoyam    '>^«fÜ '■*«""""*'  °^''*'' ^t-*  =»■ Y.p.  i8;'Yl  jj.  135;    —    'pänS   X\..'4.i,\*  J-   kaurvö.duma-   Adj.    'mit   kahlem, FrW.  3.
•)  Vgl.  unter  usig-,   bes.  BB,  A  127;    femer  kaurvahe  °mahe  Yt.Ä  21,
W£STSBE.jEr.iii,  .#7  19.  Späterhin  mildem'  j  tji„rvö.bar»sa-  Adj.  'mit  kahlem, TÖllicen  Sieg  der  soraaHJiHschen  Religion,  ist.  .  ,  ^  ti  1  n-.  i  i  ^  i  i  i  �
der  fl'aa/ischen  (vorsaraSai/^schen)  Religion  ver- j .  .  kaurvahe  °Sahe  Yt.ö.  21.
'"f  ^V  ~  ""'■"'"'^ -iT' ^^'  l,^^"  .         or    '•  J-   karsna-   m.   EN.   eines  Gläubigen: Ableit.  —  ai.  vgl.  kalpa-  m.  'Ritus'.   —    Pfi. :  i         ■      
karp,  mit  der  E?].  {für  kayak  u  karp):  pa  Ä/'  '«<'^    Ubaurvatanahe  (sd.)    awon^      des i  yazaläH  karr  u  kör,  woiu  die  np.  Erl. ;  kar  u   K.,  Sohns  des   Zb
Itehrter  Reihenfolge):  adari^ä  airotäraJca.^^  ,  ^^  karsnayana-  patr.   Adj.  'von  Karsna
')  S.  noch  BARTHfiLEMV  Gab.  57.  ■'  ,    <  .1     n  1      -  ,  ^    t
Stammend,  dessen  Nachkomme  :  vträspahe
•  g.  *karapo.tat-    f.    'die    Karapatt(sA.)-\  {^±)  '.„ahe  Yt. /^.  108;  loS'.
Schaft':  anäW  a  vlJDnäsä  ya  'ias^ä  (NS.)'*|      Ableit.  aus  karma-  EN.    Auffällige  Bildung.
kmtsscä     aväil    am  y}„g  ..    "deshalb  L    ■     «tarl-   V.  'trahere',   nur   mit  Praev.
ist  die  Karapan-  und  Ä^z-a^schaft   dem  p^^^s.  2  karAa-,  24  kar^aya-.
Untergang  verfallen   durch   die   (gerade),       ^^^    „^^    .(„,[(    si^h)    fortschleppen': D^  ^- 1       i'-^j'^'  ,.    r.       .  \dafva..vain3mnfm*apa.kttrsayml^ixA.y'^
jatms  haca  ma/yäkaiioyo     vor  aller  Augen
■e  karp  hrnd.  —   '>  iF.  s.  S  393-
•  j.  kahrpuna-  m.  Name  eines  a'aft'ischen  j  schleppten  sie  die  Weiber  den  Menschen Tiers'*:  baivan  alinam  spakanqm  •■nanqmX-^^^'  Yt. /g.  80".
ava.janyai  "zehntausend  Hundsschlangen,       ^jit   ava   '(mit  sich)   herabtühren,   an- (nämlich)  K. .  ."  V.14.  5.  schwemmen':  ana  tä  vaiötm  (sd.)  ayä  . .
Pü.:  transskt.  (karpun^) ^\t  der  Erl. :  «är  ,' I  ^^^-^  ^^.^^,^  „^^„,„  ava.kar»smü  späfum tanakll],    dazu  noch:    sakihii  t  tu  afiji:  o  kuti,'  „        ,  ,
nülnii  "handisch,  weil  er  sich  rückwärts  auf  ^'^  ■  ■  ■  •  d»™  l«im  Vierten  Mal  Schwem- den  Hintern  setzt",  —  »    DsT.s  Zusammen-'  men  sie  einen  Lei
Stellung  des  Worts  mit  np.£-«ria 'Katie' (ZA.  1  tti.  kdrsati,  np.  kasiJaii,  arm.  LW.  Haritl;  s. 3.  211)  ist  falsch;  das  wäre  Aw.  'gthrpa'  dam  Hbm.  KZ.  36.  166.  �
.     „  ,_,    ,  ,      .     ,  die  Abschreiber   apa   lu   apata   ausgeglichen
•  j.    'karana-  m.    Ohr',   uzw.  rfnÄ^ischer       haben;  vgl.  Yt.  ,0.  125.-»)  Anders  freilich Wesen":    lai  drvalö   drvatyiisca    asi    usi ■     Dk.  /.  4.  44  (S
ai.  iarna-  m.    —    rii.:  undeutlich.    —     0  Im  ,     „™..     .        ,  1 -.„  ■
Cegensaii  zv  «i-;  sd.  mit  No.  5.  0    '(Flussiges)  ausschütten;    ausgiessen
.    „  ,,.,.,        .        .        ,    -  in  -'  (Akk.):    ya'äta  yat  htm    (näml.  zaü-
•  ].  »kanina;  Adj.  'taub  :  ndtl  avä  zaoirä  1  ;^^^^,  ^,^-.  _  _  ,,^^^^  _  _  ^^„^,v  "als  ob Paai.vise    yä      mävöya     frarmkarinb  .  .^^  ^j^  ^j^^^  Schlange
'nasca  "i\5-^^-  ,  ^     .  .  ,  ,     „    .,  ; schUttete"N.4<?-       2)'(Samen)ausschütten,
si.  karna-    Ka\.    'stut lohne ,    np.  kor   'taub  ;  '  .  ,^  -  ■    ,     .        ,      .
s.  femer  KZ.  36.  15.  aussaen,  (Getreide)  durch  Aussaat  gewin-
...  ^     .  ,.     ,^    .     j    .     ,         nen':  aUavat  karitanam  {yavanam)  aHa-
.    ,.    kairya-     i)    Ad,,    'faciendus'    (nur     ,_^^  _^^^^^^^^^  ^^d.)  V.7.35-
Komp.).         2)  n. 'Geschäft, Tätigkeit,  Amt':        „p.  i;:;/a«  -säen' (Inf.  zu /jW,   %.  lkar-\   -
Hs  zaotar^  (sd.)   'rXm   atihat  N.  72.  |      Vgl.  Itor-  and  iMltari-;  \\ii. kiraydii itaTsia-
dby  Google
457
ikar£-
*liarsla-
4S8
='  np.  kärad :  iiila '1.  —  Pü.  (zu  l);  rtxlan, (in  a):  miau.  —  ')  Nicht  ganz  zutrefTcDd Hbu.  PSLS6,  HoKN  GIrPh.  zb.  140;  ^.tffäti gehört  nicht  dazu.
•  j,  %ari-  V.  'einfurchen'.  Praes.  3'* iarsa:  —  PPfP.  'karsta-,  PFP.  karsya-\ ln£  karstSe.
```


## [2026-09-06T16:11:06.729Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== CHEUNG kars\"; grep -n \"\\*karš\\|karš \" CHEUNG.txt | head -20"
}
```


### [2026-09-06T16:11:06.779Z] TOOL RESULT

```
== CHEUNG kars
57374:*karH’, *karš/*xrah
```


## [2026-09-06T16:11:07.895Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== HRN kanz/kesh\"; grep -n -i \"kanīz\\|kaniz\\|kanīzak\\|kešīdan\\|kasīdan\\|kašīdan\\|kasîdan\" HRN.txt | head -20"
}
```


### [2026-09-06T16:11:07.948Z] TOOL RESULT

```
== HRN kanz/kesh
```


## [2026-09-06T16:11:10.869Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"kars\" CHEUNG.txt | head -40"
}
```


### [2026-09-06T16:11:10.917Z] TOOL RESULT

```
15989:*karaja- ~ *krsta- (i.e. root *kars-/*xrah-) in Pir. cf. Emmerick 1966: 612; Sims- 
16048:*kars/*xrah 241 
16092:*kars/*xrah ‘to draw, plough’ 
16097:Pres. them.: IND. 3pl. YAv. auua.karosonti (V 5.5), OPT. 35р. YAv. apa.karsöit (N 48), ҮАУ. 
16098:pairi.karsöit (V 19.21), 3р1. YAv. karsaiion (Yt 19.80) 
16117:242 *kars/*xrah 
16169:*SANSKRIT: kars ‘to pull, drag, plow’ (RV+) = EWAia I: 319 
16175:9 The root *kars- appears to have a rare variant *xrah-, with a different kind of 
16178:striking as well. The root *kars-/xrah- specifically refers to the ploughing process, 
16180:*kars-/xrah- and *karH’- either show mutual influence, cf. Sh. kiräx(t), etc., or are 
16247:*NEIR: Oss. I. kaerdyn/karst, D. kaerdun/karst ‘to cut (to pieces)’, Sh. xicand-/Xicryd, 
22634:І. skaryn/skerst, D. skarun/skarst ‘to explore, look around, seek; to grope one’s 
33512:kars-, 241 
46698:keerdun/karst (D), 244 
46699:keerdyn/karst (1), 244 
47039:skarun/skarst (D), 346 
51516:kars, 242 
55146:(s.v.), *kars/xrah (s.v.), *rap/f 
55898:*Huad, *iat (s.v.), *kars/xrah 
56429:*Напё, *kars/*xrah, *kauc, 
56589:*CarH (s.v.), *kars/xrah 
56890:(s.v.), *kars/xrah (s.v.),
```


## [2026-09-06T16:11:12.129Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"kanîz\\|kaniz\\|kanîzak\" HRN.txt | head; echo \"--- Horn leaf for p.191 = leaf 212, p.194 = leaf 215, p.174 = leaf 195\"; awk 'BEGIN{RS=\"\\f\"} NR==213' HRN.txt | cut -c1-400"
}
```


### [2026-09-06T16:11:13.786Z] TOOL RESULT

```
--- Horn leaf for p.191 = leaf 212, p.194 = leaf 215, p.174 = leaf 195
— 191 -
854. UuHt *Seite, Flanke', hu^Vl^ kustl 'Gürtel', vergl.
hergustvuan (No. 205) ; kusftgir 'Ringkämpfer (AM. 2()6
Zeile 8).
phlv. ktist^ kustak 'Seite*, kusttk^),
855. kuSten 'tödten', nt^^t^lD (Qiss. Dan.).
aw. l/ftaos-, kusaiti 'tödten'; phlv. kustan, vergl. asö]-
kvs (für aw. asavaynya-, vd. 5 (47)); skr. KÄö5-, kusnäti
'zerreissen' (?).
kurd. LW. (?) kustin 'tödton*; bei. L\V. (?) kuäag,
n. ßusay 'todten, scli lachten (207).
856. feesß/ ^Schildkröte ; Krebs (Zodiac, Sahn. I, 77 Vers
285)', keseto (dial.).
aw. kasyapu' 'Schildkröte' oder *Krebs' (Geldner,
KZ. 25, 503, 5()6j ; skr. (Brhm.) kagydpa- 'Schildkröte .
af/. kasy 'Schildkröte'; bei. käsib (190).
857. Ä-e«efc 'Elster .
Toniaschek, Painirdialokte S. 771, veigkM'cht aw.
karsiptan-^ phlv. kars{i)ft (L)eutun*i: nicht sicher), wa/.
karjöpc, sar. karjopc, si;'n. ksebc 'ElstiM-'.
858. kiSver^ kesver 'Ph-dteil'.
aw. karsvar- 'Weltteil'; phlv. kisvar^).
859. kesläen ziehen'.
aw. [/^km's-, karsayefi^); phlv. kasttan; ai. 1. [/^kars-,
• kdrsati, karmyati 'ziehen, schleppen'.
kurd. kisän ziehen'; af>'. k/dl; bei. kasay, n. /i'asay
'ziehen, abziehen, herausziehen' (19:^); arm. LW. (?)
Karsem 'ziehen*.
») Syr. LW. J^D^'ID, J^nDD, p^DDIp; ai'ab. LW. kustij (de
Lagarde, Ges. Abb. 59, 60); bei. LW. kustl (143). — Aber nicht gehört
dazu lat. c^ista *Rippe*, das Meringer, Sitzb. WAW. CXXV, *Beitr. z.
indg. Decl.*, 42, mir nicht einleuchtend, zu ai. dbthi- 'Knochen* stellt.
') Eine Volksetymologie in 'Selections of Zätsparnm* (West
P. T. I) 7, 9.
») Aw. [/has- will Hübschmann ZDMG. 44, 558 ausser Betracht
lassen.
```


## [2026-09-06T16:11:20.586Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== leaf 195 (p.174)\"; awk 'BEGIN{RS=\"\\f\"} NR==196' HRN.txt | cut -c1-1500; echo \"=== leaf 216 (p.194)\"; awk 'BEGIN{RS=\"\\f\"} NR==216' HRN.txt | cut -c1-1200"
}
```


### [2026-09-06T16:11:22.724Z] TOOL RESULT

```
=== leaf 195 (p.174)
174
'Schakal'; plilv. sayäL LW. türk. caqal; ngr. rtjayuh;
deutsch Schakal etcJ).
Die neupersische Form muss statt *seyal stehen;
denn np. s vertritt nicht etwa ai. q\ Als bereits
arisch wird der Schakal auch in der neuesten (4.)
Auflage von Fick's Indog. Wörtbch. , S. 212, an-
genommen 2). über das heutige Vorkommen des
Schakals im Orient heisst es bei Brehm, Säuge-
tiere I-, 545: 'Der Schakal verbreitet sich' von Indien
mit Ceylon aus über den Westen und Nordwesten
des Erdteils, die Euphratländer, Persien, Palästina
und Kleinasien etc.*
In np. seyäl, sunüden (No. 795) und sä/ (No. 766)
entspricht s sicher sanskritischem ^•; andere Fälle
wie äs (No. 29) oder susten (No. 782) können zweifel-
haft sein, während die Zusammenstellung von np.
siften reiben, kratzen'^) mit aw. aiu)i]siföis, yt. 14, 35
(Geldner, 3 Yasht 77) geradezu falsch ist.
786. sikär *Jagd', vergl. hisgerd (No. 224), sikerden, sekere,
iskere 'Jagdhabicht'.
phlv. äkar Magd' (vd. 5 (134) Gl.), sakra Magdhabicht'
(Bund.).
oss. LW. sk'ärun 'treiben, jagen (v. Stackeiberg,
ZDMG. 43, 672)4).
aw. "^aiwis (doch vergl. No. 221) + [/^kar- (de
Lagarde, Beitr. z. altb. Lex. 42, Pers. Stud. 75);
aber dann gewiss nicht zu [/kar- 'tun, machen*, wie
de Lagarde will, sondern zu [/kar- in np. nigär^
niijerlden. Die ursprüngliche Bedeutung findet sich
^) Vergl. auch Miklosich, Denkschr. WAW. 34, 271; 37, 20.
^) Nach anderen wäre hebr. '^Ultfi? 'Fuchs', Schakal' damit identisch
(s. Rödiger-Öesenius, Wörterbuch, S. 1457).
') Die Grundbedeutung von np. sißen ist nicht klar. Mit AbuM
Ma*änl- Versen lässt sich nichts erweisen.
^) Schon Tomaschek, Centralasiat. Studien, II, 891 (wo auch
manches Falsche) hat das ossetische Wort zu dem neupersisohen
gestellt.
=== leaf 216 (p.194)
- 194 —
869. kenden graben', Praes. ken-em,
ap. aw. \/kan- graben'; phlv. kantan (Bund.), kandau
(AV., PPGl.), paz. /andan; ai. l/khan-, khdnati.
kurd. kendn; af/. kandal; oss. t. vergl. nijgänin
'begraben' (Urform "^Mnin^ 203); arm. vergl. akan
diOQvy/iia (H. No. 3).
Auf die mit kh anlautende Form der Wurzel gehen
np. (arab.) yendeq Graben , phlv. xantak, np. /öw«j, /an
'Haus' (No. 405) und /am 'Quelle' (No. 466) zurück;
vergl. auch feryen neu gegrabener Wasserkanal' neben
ferken etc. Auf päz. /andan ist gar nichts zu geben,
vergl. päz. /ähUan^ /m u. a. m.
J. V. Fierlinger erklärt KZ. 27, 335 das ap. aw.
kan- gegenüber ai. khan- durch Analogiebildung nach
der schwachen Wurzelstufe, Bartholomae, ib. 367
Anm. 2 durch solche nach den mit Praefixen kon-
sonantischen Auslauts zusammengesetzten Formen.
870. kentz 'Jungfrau, Mädchen', kenizek,
maz. klja (?) ').
aw. kanyä-^ kaini7i-, kainikä- 'Jungfrau, Mädchen';
phlv. kanik, phlv. päz. kaMöak bezw. kanTjak, kanlzak
(PPGL); ai. kanyä-, kanijd-.
Durch dasselbe Suffix weitergebildet wie dösüe,
nrDirn (Is. 23, 4, 12) 'Jungfrau .
871. kiitäh, küteh 'klein, kurz'; ködek 'Kind, Kleines,
Foetus, Embryo (AM.)'.
aw. kutaka- 'klein'; phlv. kütak bezw. kötak,
bei. künd, n. Jcund 'kurz, nahe' (209); afy. LW. (?)
kötah,
np. küiäh entbehrt auflfälliger Weise der Lautver-
schiebung. Für ködek ist eine Grundform *kvataka-
anzusetzen (wie dö aus dva-, tö aus tvam u. a. m.).
Zum Pronominalstamm kva-, kn-?
872. hüze 'Topf.
aw. /awza- *Topf'; arm. LW. kuz.
Da mir Geldner's Übersetzung (vergl. KZ. 25, 583
^) Dazu auch kurd. kic?
```


## [2026-09-06T16:11:31.909Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== SOD knc\"; grep -n \"knc\" SOD_pages.txt | head -20"
}
```


### [2026-09-06T16:11:31.956Z] TOOL RESULT

```
== SOD knc
17283:     GMSrl 247; kncYwS% MDiii p25
17287:4752 knc>k S                         (JT^)*^^                       *»knpy pw-, knPy pr'n, kmby(y), kPn-
17289:       kainika; MP knyg; qnycq =*»knc, kneyk
17293:        MDii, A-16,7 pl39.7, pi. knc'ku C2, AV 26, ob.
17302:     kancik =»knc>k
```


## [2026-09-06T16:11:32.775Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== FSF kanizak\"; grep -n \"کنیز\\|کنیزک\" FSF_pages.txt | head -10"
}
```


### [2026-09-06T16:11:32.834Z] TOOL RESULT

```
== FSF kanizak
1253:                       ‫عبدالقادر د‬             ‫کنیزی که برایش نان و آب می‌آورد‬
1256:    ‫شاهنامه رابهاین شکل شاهد می‌آورد‪:‬‬           ‫می‌کند که شیر گرمبرایش بیاورد‪ .‬کنیزک‬
7654:              ‫کنیزک پسر زاد روزی یکی‬
18236:                                      ‫کندر‪ .‬برهان] خمره‌ایست کهدر آن عسل و کنیزک‬
18249: ‫«بوی بنفشه ایدون چون بوی کنیزکان»‬                         ‫بدو گفت زین خواسته هیچ ماند‬
18288:                 ‫کنیزک [دختر شا‬                                                   ‫سرانجام‪:‬‬
18295: ‫ز هر چیز گنجی بیاراسته‬                                       ‫چو کاوس روی کنیزک بدید‬
22987: ‫از هندسه [معرب واژة پارسی اندازه] ‪+‬ی‬           ‫دادند‪ .‬سپس به یاری کنیزکی اآزنجا‬
```


## [2026-09-06T16:11:36.289Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '17275,17310p' SOD_pages.txt; echo \"--- leaf of line 17283\"; awk 'NR<=17300{n+=gsub(/\\f/,\"\")} END{print \"formfeeds before:\",n}' SOD_pages.txt"
}
```


## [2026-09-06T16:11:37.146Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR>=18270 && NR<=18300' FSF_pages.txt | cut -c1-300; echo \"--- pdf page tag near\"; awk 'NR>=18150 && NR<=18300 && /pdf page/ {print NR\": \"$0}' FSF_pages.txt"
}
```


### [2026-09-06T16:11:38.176Z] TOOL RESULT

```
                                                                   C2, 60R30: BSTii 889, 30
         light-loaded
         MSP p46                .                            4763 knph S                          {Ji^r ^     i^S 4aU-
                                                                  kam/nb/p =»skfs, qmp
 4750 kne M               *            (^f)<^j^>                   assault, stratagem
      kanc (qnc) ©<Av. kainika -^kne'k
                                                                   Sund. KG 465; MSP n p46 "dodge"; STSC 146, 5,
                                                                     6
     GMSrl 247; kncYwS% MDiii p25
      gi
4751 qnc =» kne                                              4764 knpy B, M, S    (jy> ^* j-*)^ '^ <>yr^ ^
                                                                  kambe/i (qmpy) ©<*kambiyah\ Parth. kmbyft
4752 knc>k S                         (JT^)*^^                       *»knpy pw-, knPy pr'n, kmby(y), kPn-
     kance (qncq, qnck/cyy) <D<Av. kainya-,                       lack, shortage
       kainika; MP knyg; qnycq =*»knc, kneyk
                                                                   Benv. Notesiv 515.16; Hen. Texts. 732; VJ 53, 80,
     small girl, child
                                                                     1318; TSP 3.22, 6.106 & etc.; STii 9.18; BSTBL,
        MDii, A-16,7 pl39.7, pi. knc'ku C2, AV 26, ob.
                                                                     Dhy. 126; SCE 499; Sogdica. 64.7, 15; MDii
          P*. qncqty; kneyiyh BBB e22; GMS 247, 957
                                                                     1.120; knph, Frag. Len. 68.4, 7
4753 qncq      C ==» kne'k
                                                             4765 knpy}kh S                                   ^^y^
4754 qnck/cyy  M =$ kne'k                                         kambyak
                                                                  shortage
4755 kneyk M                               o'_h- j^> <>^>
     kancik =»knc>k
                                                                  MDii p!65 A-15.4

     GMS 995-, Hen. Talcs. 472, 42e                          4766 knpy'strh B                       ^Txf jU t^j^f
       girl                                                       kambistar
4756 qncystr C                                Jolyr >^*-->        particularly short
     kancistar
                                                                  TSP 2.433; Hen. Texts. 734; Benv. TSP,
        younger girl                                                knpfstkh; GMS 1289, 1302; MSP bl91
--- leaf of line 17283
formfeeds before: 255
```


### [2026-09-06T16:11:40.113Z] TOOL RESULT

```
‫پس از رنج بسسسیار و راه دراز‬                     ‫کزدام نژاد است؟ و‬
                                                                 ‫بیشه افتاده است و ا‬
 ‫ابر زاب لستان فراز‬           ‫بامد‬                                  ‫پاسخ دختر که‪:‬‬
 ‫بدو خسروی نامور شسهریار‬                                ‫بدو گفت من خویش گرسیوزم‬
‫شهی کش نبد کس به‌صد شهر یار‬                      ‫به شاه آفریدون کشید پروزم‬
‫مر آن اه رانام گسورنگ بود‬                                           ‫و باز چندین بیت سپستر‪:‬‬
‫کزو تسیغ فرهنگ بی‌زنگ بود‬                                       ‫وراگفت از مام حاتونيم‬
‫یکی دخترش بود کز دلبری‬                           ‫ز سوی پدر بر فریدونیم‬
 ‫پبری راب رخ کردی از دلبری‬                                       ‫نیایم سپهدار گرسیوزست‬
 ‫مرو رازنضی کابلی دایه بود‬                        ‫برآن مرز خرگاه او مرکزست‬
‫را مایه بود‬ ‫وگ‬ ‫رنن‬ ‫یسسو‬
                      ‫ن‌اف‬
                         ‫که‬                     ‫طوس و گیو دل بهدختر می‌بازند و برسر‬
‫بدین لاله گرسخفته بود از نهفت‬                    ‫آنکه دختر از آکندامیک از دو پهلوان‬
 ‫که شتاهی گرانانه نادت سب‬                         ‫در می گیردو‬       ‫اث بین آندو کمک‬
‫مان زان نويد‬
           ‫دده‬
             ‫اش‬‫شه]‬
                 ‫کنیزک [دختر شا‬                                                   ‫سرانجام‪:‬‬

 ‫همی بدنهان رازه دل پرامید‬                                    ‫میانشان چو ان داوری شد دراز‬
                         ‫‪-۲‬به‌معنی برده‪:‬‬         ‫میانجی برآمد یکی سرفراز‬
‫افراسیاب برای آشتی باسیاوش و رستم‪.‬‬                         ‫که این را بر شاه ایران برید‬
                       ‫بهگرسیوز گوید‪:‬‬            ‫بدان کو دهد هر دو فرمان برید‬
        ‫به نزد سیاوش بر خواسته‬                         ‫پهلوانان با دختر نزد کاوس می‌آیند‪:‬‬
 ‫ز هر چیز گنجی بیاراسته‬                                       ‫چو کاوس روی کنیزک بدید‬
        ‫غلام و کنيزک پبر هم دویست‬               ‫بخندید و لبرابه دندان گزید‬
 ‫بگویش کهبا تو مرا جنگ نیست‬                      ‫‏)‪(OY-4-1‬‬
‫(‪)۸۰۴-۵۲-۳‬‬                                                   ‫سپس کاوس به پهلوانان می‌گوید‪:‬‬
 ‫کوس‬                                         ‫‪۳۹۹‬‬

--- pdf page tag near
```


## [2026-09-06T16:11:51.245Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR<=18288{n+=gsub(/\\f/,\"\")} END{print \"leaf idx:\",n}' FSF_pages.txt; echo \"--- total leaves\"; grep -c $'\\f' FSF_pages.txt; echo \"--- head of that leaf\"; awk 'BEGIN{RS=\"\\f\"} NR==402' FSF_pages.txt | tail -5 | cut -c1-200"
}
```


### [2026-09-06T16:11:53.246Z] TOOL RESULT

```
leaf idx: 371
--- total leaves
479
--- head of that leaf
                ‫خوابست و رخش می‌چرخد‪:‬‬                      ‫‪-۱‬انداختن‪ .‬رهاکردن تیرکامزان‪:‬‬
         ‫چو در سبزه دید اسب را دشتوان‬                             ‫چو بیند برو بازوی و مغفرت‬
‫گشاده زبان سوی او شد دوان‪.‬‬                          ‫حدنگی بباید گشاد از برت‬
 ‫(‪)۰۲-۹۹-۸۳۴‬‬                                       ‫(‪)۶۷۹-۵۲-۴‬‬
```


## [2026-09-06T16:12:01.842Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==248' FSF_pages.txt | head -8 | cut -c1-250"
}
```


### [2026-09-06T16:12:03.459Z] TOOL RESULT

```
                                             ‫‪rf‬‬

                  ‫آنها چاره‌جویی می‌خواهد‪:‬‬                      ‫چو دریای سبز اندر آید ز جای‬
      ‫گرانمایگان پاسخ آراستند‬                      ‫نسدارد دم اتش تنیز پسای‬
                                                  ‫‏)‪(EYF-11۸-1‬‬
     ‫که گر نامداران سقلاب و چین‬                    ‫(یعنی تف آتش تیز در برابر موج دریا‬
 ‫به ایران همی رزم جستند کوین‬                                             ‫تاب ایستادگی ندارد)‬
                                                   ‫لف‬
```


## [2026-09-06T16:12:11.121Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== PHD kanig\"; grep -n \"kanīg\\|kanig\\|kanīzag\\|kanizag\" PHD.txt PHD_mackenzie.txt | head -10; echo \"== NYB\"; grep -n \"kanīk\\|kanik\\|kanīčak\" NYB_vol2_glossary.txt | head -10"
}
```


### [2026-09-06T16:12:11.188Z] TOOL RESULT

```
== PHD kanig
PHD.txt:318:^-éwüzih [-yxw'cyk | (M dwšw'cyh)) evil speech, calumny. ~+farrag [-plg | P dwéfr] unfortunate. ~-farragih : misfortune. ~-gowisn [-gwbsn'] of evil speech, ill-spoken. ~-humat [-hwmt'] evil thought. ~-hixt [-Awht' | M dwfxwptyy!] evil speech. ~-kām [-2’m] ill-will, malevolence. ~-kanig [-knyk'] hag. — kar LAT difficult. ~-kuni&n [-kwngn'] of evil behaviour, ill-doing. dušmat [dwfmt! = Av. dufmata- | M dw$mtyy!)] evil thought. dušmen [dwsm(y)n' | = M, N dušman] enemy. ~ih: enmity. „ādīh [dušmntyh | M dwkmny’dyh, J dwfmn'dy] enmity, hostility. duš-|-menišn [dwf-myntn!] of evil thought, ill-thinking. --nàm [->”m | N ~] abuse, insult. dušox [dwshw! | M dtws(w)x] hell. ~ig [-yk'] hellish. duš-pādixšā(y) [dušp*thš*(d)) evil ruler. ~th: evil rule, misrule. dušrām [dwsl())m] unhappy. ~ih: unhappiness. dušwār [2001 | M dwšw”r, № ~] difficult, disagreeable. ~ih: difficulty, trouble, misfortune. du&-|-wir [dws-wyl] evil-minded. ~-wurréyisnih [-wlwdsnyh] heresy. c-.xém [-hym] evil-natured. ~-xwadiayih [-hwt'yh] misrule. ~-xwar Lea! | N ~] = dušwār. dušxwaršt [до оной! | M dwkxw styh!] evil deed. duxt [BRTE < A brt-h; dwht' | M dwxt, N ~] daughter. ~ar [dwhtl | N ~] daughter. duz(d) [GN BA < A gnb’; dwc(t) | M dwz, N duzd] thief. ~th [dwe(d)yh] theft. duzidag [dwcytk'] stolen; intercalary (days). duzidan, duz- [dwe-yin' | N duzdidan] steal. dwārīdan / dwāristan, dwür- [dwP?l-ytn!, -stn! | M dwr-] run, move (daevic). ~išn: abode (of demons), hell. dwāzdah [dw'cdh | M dw'zdh, N duwazdah] twelve. ~ап [-’n'] the zodiac.
PHD.txt:424:kaman [kin’n' | = M, N ~] bow. 5; 7 ~dar [-d'] | N ~] archer, bowman. ha er mae 4 ba kamar [kml | N —] waist; belt, girdle. ~-band [-bnd | N ~] belt. kāmģār [Emil | P k?*mg?*r, N ~] powerful, absolute. kamist [Amyst'] least. —jh: pad ~ih, at least. kāmistan, kām- [YCBEN-stn' < A ysbh, V shh; k*m-(y)stnt M k*m-yst] want, desire. kám|-rawág [km izvb*k! | N ~rawa] successful. ~-Z1(w)isn [-zywsn'] free, independent. kam-zór [kmzwl | N ~] weak. ~ih: weakness. kan-, v. kandan, kanar [kwl | N ~] side, edge; embrace. ~ag [-k' | M kr?rg, N ~a] edge, limit, boundary. --agómand [-k’wmnd | M -gwmnd] limited, finite. kandan, kan- [HPLWN-tn! < А V hpr; kn-dn', -tn! | M knd, N ~] dig; raze, destroy. kanig [knyk! | M knyg] girl, maid. kanizag [knyck! | M knycg, N kaniz(ak)] — kanig. kantigr [kntgl] quiver. kāpūr [ро | Ar. kāfūr] camphor. kar-, v. kardan. 1Kar [21 | M Pr, N ~] work, deed, affair. ~ framüdan: put to use. 2kàr [%'7], pl. —àn: (other) people. зкаг [%'/] butter. kār-, v. kištan. karafs [klips | N ~] celery. kār-āgāh [РА | N ~] skilled, experienced. ~ih: skill, experience. karak [krk! | N ~] quail. karan [kľn' | P bein, N ~] side, edge, end, limit. kārawān [%?/zv?x! | P k*rw'n, N kārwān] caravan, military column. ~ig [-yk! | N ~7] caravaneer, traveller. karb [klp] priest hostile to Zoroaster. karbāš [5/0 | N karbas, etc.] lizard. karbunag [k/pnk!, klbnk'] lizard. kard [krt! | M kyrd, N ~] action; matter, affair. кага [SK YN A < A skyn’; Kit! | N ~] knife. ikardag [kltk!] division, section, portion. *kardag [krtk!, kltk! | N karda] action. kārdāg [k'/d?k'] traveller, wanderer, migrant. kardaģān [Art-, Rlt&?n! | M kyrdg”n) action. kardagàár [Artk?l | M kyrdg’r, № ~] mighty. C 6084 E
PHD.txt:2103:girl kanig, maiden.
PHD.txt:2123:kanizag; v. daughter,
PHD.txt:2186:hag du&kanig.
PHD.txt:2701:maid kanig, kanizag, paristar.
PHD.txt:5038:nay! kundāgīh kundāg nayestān! kandan kanīg kanīzag xwan-! xwandan! -gen
PHD.txt:5411:Gušnasp duškām dēšagīh dēšag, gūšag duškanīg duškunišn duškar dušrām dušrāmīh dušram dušramīh dušmenīh dušmen dušmenišn dušmenādīh dušmenīlh
PHD.txt:5446:gon gonag dowom drustih drust gowizar gozénag gugay gugay gugayih gugayih gugan- gokanig gokan doganag gugar- gugārīdan gugārdan dēk gēūgirdūmand gogird даг, рог, gul dol gurbag
PHD_mackenzie.txt:2136: .......·kanig [-knyk ] hag.
== NYB
1324:ing duš-kanik (an independent w. "duš does not exist), but perhaps meant as dust-tar, NP dust ‘foul, ugly’, — Paz. doši ‘folly’ (SGV X, 58 ete.).
1395:duš-kanik [dwšknyk] bad, ugly maiden © 155.6.
1421:rad (v. below). 1. HN’: ~ nāmaky this inscription (here above) P 2:3; ~ vizand hac yātūkēh i ~ kanik 373: ~-ic évak hac avdéh the following is one of the miracles 4474; kē hac ~ aštak, veh he
2016:homānāk [hwm’n’k] like, similar, re- sembling: nézak ~ like a javelin 8517; 8515, 864. 10427; pūt hangošitak (q. v.) ~ 7613; 865; 6 ~ 119-120 passim; kanik-& i 6 kanikän ne ~ à maiden who does not look like maidens 754; ētūn ctgēn
2199:ibd.; 222, 422-71 passim; 971; 14-16 pas- sim. — MPrs knycg; NP kanizah. Dimin. of kanik; v. also kanisk. (Ps. 122% knysky, v. Barr s.v.).
2201:kanik
2204:kanik [knyk] virgin, maid 37-38 passim; 73 passim; 754-7. — Av. (439) kainyä-, kaini-; MPrthPrs knyg; Paz. kanik.
2225:karp [klp'], cas. obl. karpēk [klpyh] 95**, the external, visible form of living be- ings: der-pattäi ... ~ dārēnd they will have their external form everlasting (= an everlasting bodily form) 10515; — as the second element of a compound: mdtak ~ having female shape 5717; pat kanik ~ in the shape of a maiden 731; 6 martom karpéh into human shape 9526; mart ~~, martë [GBR? 4-1] ~ 104%; 9621, 9819; 6 hàn 4 uštur ~ 9915, — Av. (467 sq.) kahrp-; Arm. lw. kerp; MPrs kyrb (A-H I), but Paz. karf.
5202:ka-: cē kā- (kāta-): kātak kadā: kad kaēnā-: kēn kaēš-: nām-cišt kaēta-: kēt ka60: cihénitan kahrkäsa-: karkäs kahrpuna-: *karbök kainyä-, kaini: kanik kämä-: kam kamarä-: kamar kamoroča-: kamar kambištem: kčm
5654:kfwn: kahvanéh kmbyg, qmbyft = qmbystn | com knyg: kanik
```


## [2026-09-06T16:12:12.115Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; head -5 incoming/BQT/BQT_v3_pages.txt; echo ---; grep -n \"pdf page\" incoming/BQT/BQT_v3_pages.txt | head -3"
}
```


### [2026-09-06T16:12:12.173Z] TOOL RESULT

```
[pdf page 1]
[NOT OCRED - use tools/ref_page.py]
[pdf page 2]
7
Ub
---
1:[pdf page 1]
3:[pdf page 2]
24:[pdf page 3]
```


## [2026-09-06T16:12:24.635Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT; python3 - <<'EOF'\nimport re\np='BQT_v3_pages.txt'\ntxt=open(p,encoding='utf-8',errors='replace').read()\n# split by [pdf page N]\nparts=re.split(r'\\[pdf page (\\d+)\\]',txt)\npages={}\nfor i in range(1,len(parts),2):\n    pages[int(parts[i])]=parts[i+1]\nprint('pages:',min(pages),max(pages),len(pages))\nfor n in [446,447,450,451,508,509,548,549]:\n    t=pages.get(n,'')\n    print('---pdf',n,'len',len(t), repr(t[:120]))\nEOF"
}
```


### [2026-09-06T16:12:26.142Z] TOOL RESULT

```
pages: 1 721 721
---pdf 446 len 2513 '\n--1۵۳-\n\n\u200eUIT\u200f توپ است ؛ و \u200egene\u200f دیگ رکویند سنگی\nباشد که در منجنیقگذارند و پرحصار الدازند با\nبر خصم \u200eVas\u200f و وجه \u200ehas\u200f آ'
---pdf 447 len 2360 '\n\u200e—\\et— _ 8\u200f\nکشمود ۲ » بروزن \u200eaiid\u200f دلبدعتی\n\n\u200fومحرالی \u200ecol\u200f ؛ و بسن یگوند نام جابی\u200cومقامی\nاست در حوالی دشت مور ۸ .\n\n\u200fآگش'
---pdf 450 len 2531 '\n-۱4۷- کیش\nونوشته است \u200e٩\u200f مطلقاً خواه خط عربی\u200cباشدوخواه\nقارسی وهندوی وغیره؛ وبعضی بمعنی\u200cخط ونوشته\n\u200eain\u200f اول کفته اند و خ'
---pdf 451 len 1678 '\nبیان پانزدهم\nدر کاف تازی با عين بی نقطه مشتمل بر پنج لغت و کنایت\n\nکب غزال , کعب الغزال -\nتوعی از شکر پاره \u200eath\u200f ؛ و نوع'
---pdf 508 len 2150 '\n\u200ex ۷۷۵7\u200f ۳\nهم\u200cآمده است ؛ وباین \u200eem\u200f اول\u200cهم کفته\u200cاند.\n\n\u200fکنیسه ۳ - بکر اول و ثالی بتستانی\nرسیده و فتح سن بی \u200eabet\u200f , معبد'
---pdf 509 len 2255 '\nکواده مکی\n\nبمعنی اول کواده است که چوب آستان در خانه\nباشد ؛ و بفتح اول هم آمده است .\nکوادون \u200eA\u200f - بنم\u200cاولبروزن همایون,\n\u200e'
---pdf 548 len 2213 '\n۱۷۵۱\n\nبخوردنی \u200eath\u200f واین حال بیشتر زان آبستن را\nچم رت ۱ ۰\n\nکیادش- بفتع اول و دابع بر وزت\nجفاکشی .نام یکی از چهار پسر کی'
---pdf 549 len 2456 '\nکیان خره\nباشد که حرارت وبرودت ورطوبت \u200emel pty\u200f\nوعناصراربمه را یز کوبند - واصل وبنای\u200cهرچیز\n\u200ewld\u200f - و مرزبالرا هم میکوند '
```


## [2026-09-06T16:12:37.341Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT; python3 - <<'EOF'\nimport re\np='BQT_v3_pages.txt'\ntxt=open(p,encoding='utf-8',errors='replace').read()\nparts=re.split(r'\\[pdf page (\\d+)\\]',txt)\npages={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}\nfor w in ['کشکول','کنیز','کشاله','ترکش','کیش','کشیدن']:\n    hits=[n for n,t in pages.items() if w in t]\n    print(w, hits[:15])\nEOF"
}
```


### [2026-09-06T16:12:39.090Z] TOOL RESULT

```
کشکول [138, 393, 446, 483]
کنیز [13, 133, 233, 287, 337, 481, 508, 587]
کشاله []
ترکش [60]
کیش [61, 64, 72, 76, 77, 87, 104, 223, 224, 243, 274, 313, 340, 440, 450]
کشیدن [39, 55, 84, 88, 110, 119, 129, 202, 205, 218, 228, 256, 274, 288, 291]
```


## [2026-09-06T16:12:48.335Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT; python3 - <<'EOF'\nimport re\np='BQT_v3_pages.txt'\ntxt=open(p,encoding='utf-8',errors='replace').read()\nparts=re.split(r'\\[pdf page (\\d+)\\]',txt)\npages={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}\nfor n in [446,450,483,508]:\n    print('========= pdf',n)\n    print(pages[n][:2400])\nEOF"
}
```


### [2026-09-06T16:12:50.167Z] TOOL RESULT

```
========= pdf 446

--1۵۳-

‎UIT‏ توپ است ؛ و ‎gene‏ دیگ رکویند سنگی
باشد که در منجنیقگذارند و پرحصار الدازند با
بر خصم ‎Vas‏ و وجه ‎has‏ آنکوشك‌سوراخ
کننده باشد چه کشك مخفف کوشكث است‌وانجیر
‎me‏ سوراخ هم‌آمده است ۲ .

‎GES = FO‏ نفد کشکینه
است که نان جو باشد ؛ و بعض ی کوبند ‎Babb‏
‏که ازآرد جو و آرد ‎WL‏ وآرد گندم وآردنشود
مجموعه را بپم آمیخته خمیر کنند و بپزند ؛
و بعضی دیگر گویند کندم بربان است که‌درظرفی
کنند و ماهیابه درآن ریزند و ییاز خام و ساق
چقندر و ‎phi‏ خرفه درآن داخل کنند ودرآ فتاب
گذارند تا ترش گردد .

‏کشکو ؟ - بر وزن بدرو ۵ ‎wie‏

‎OS‏ که آش جو باشد - ‎thy‏ مرغی هم

‏هت ‎Le‏ وسقید که ‎oT‏ را عکه خواند .

‏کشکول = بروزن مقبول » بسنی کدا
باشد یعنیشخصی که کدایی کند - وکاسة کشکول
کاسة کدا را گویند ۷ و ععنی ت رکیبیآ نکشیدن
بدوش است چه کش بممنی کشیدن و کول دوش
وکتف را کرد و با کداییکننده این معنی
هست - وکاسه‌ای را نیز گویند که کدامان دارند
- و آنچه مشهور است ظرفی باشد که ۳ براباندام
کشتی سازند .

‏کشکهای پر توه = بفتح اولوثانی»
بمعنی خطوط شماعی است چه کشك بمعنی خط
باشد و پرتو بمعنی شعاع .

‏کشکهی ‎٩‏ » بر وزن بروین » بمنی
اول ‎ET‏ است که نان جو باشد - و الیرا نیز
کویندکه ازآرد ‎WL‏ و نضود ‏ و کندم وجودرهم

‎: ‏که کشکنجیر غیر از منجنیق است‎ WL, ‏انوری‎ ce gil - ٩

‏نه منجئیق بسقفش وسد نه کشکنجیر

‏نه تیرچرخ ونه سامان برشدن بوهق.
* انوری چاپ لبریز ص ‎ANYE‏

‎: ‏کشکنجیر ثیر میانداختند‎ Slee ‏منوچهری‎ ce oul

‏داد جشن مه رکان امپهید عادل دهد

‏آن کجا تنها بکشکتجیربندازد زرنگ (خدنگه) .

‏? منوچهری ص4۸٩‏ .

‏و از ‎So bed‏ نیز همین ‎er‏ برمیآید. رلد: فرهنگه نظام ‎GUT.‏ مینوی نوشته‌اند: کشکنجیر
بعنی سوراخ ‎BET‏ کوشك . ‎OT)‏ نوعی ازآلات قلمه کشابی بوده است که بدان سنگپای کلان
با تبرهای بز که وستبر بدبوار قلعه با باروی شهر پرتاب ‎her Cae‏ واز ضربت آن‌دبوارسوراخ
و خراب میشده است ‎J).‏ : تعلیقات نوروزنامه ‎۱۲٩ oe‏ - ۱۳۰ .

‏۴ رك : الچیردن . ۴ - مخفف « کشکینه » (هم.) .

‎kashkaw - ۴‏ = کشکاب (هم.) = کشکر (هم.) . ۵ - بفتح راء .

‎SKS AV gn) ‏کیک رکه‎ me ‏«کشکر» « رتیدی‎ Gee ‏ظ‎ - ٩
‏علامه دهضدا » ؛ در عریی « کشکول  بفتح اول » مولف‎ GEG ‏آلیس‌الطالبین بخاری متملق‎ «
‏کل‌شی.‎ cole gies ) ‏کل » ( بضم اول و کسر دوم و خم چهارم‎ ET? ‏کوید ازآرامی‎ a?
‏و مراد محفظهایت که درریشان و کدایان هرچه از مردم ستانند درآن دهند - کشکول پوست‎
‏بخط استوا عمل مبآیید و شبیه بکشتیی‌است بارنگهياه,‎ thay ‏است که درجزایر‎ gle dew
‏تابتوان بدست آویخت , وآن‌کاسة کدابی‎ wae ‏سوراخ کنند و زنجیر با رسمان‎ VT ‏دوطرف‎
‏مغز نارجیل‎ OT ‏دروبشاست ؛ و آلگاه که بر درخت است دو کشکول بهم چپیده است و درمیان‎
. ‏فرهنگه دسالی
========= pdf 450

-۱4۷- کیش
ونوشته است ‎٩‏ مطلقاً خواه خط عربی‌باشدوخواه
قارسی وهندوی وغیره؛ وبعضی بمعنی‌خط ونوشته
‎ain‏ اول کفته اند و خط بطلان را بکر اول ؛
و بفتح اول و انی بمعنی خطی باشد که بکشند
خواه بر دیوار و خواه بر زمین (۱) وخواه بقلم "
وچوب و انگشت و غیره - وتنگه چاروا را نیز
کوبند و آن نواری باشد که بر زین و ‎NG‏
‏دوزند ۴ - و بععنی کدا و گدايی‌کننده ۴ -
و بمعئی آسانی در برابر دشواری نیز کفته‌اند -
و بر چار پایان هم حمل کردماند - و با تشدید
انی حیوان پالان افکنده را گوبند ۴ .

کشی * = بنتح اول و ثانی بتحنالی
کنیده . بمعنی خوشی و تندرستی باشد ؛ وباین

معنی ‎GEL‏ فارسی هم‌آمده است ۰

کشیخان ۱ ۰ بروزن پیخان ‎ian‏
‎Oy‏ و بچشم خود بن باشد ب کشیخانی
بمعنی دبوئی است ‎He‏

کشیده ۲ ۰ بر وزن رسیده | بمعنی
وزن کرده - و بلند ودراز باشد چه « کشیدمروه
مردم رو دراز و « کشیده ریش * مردم دراز رش
راگویشد - و در خراسان بمعنی نشثی باشد که
ژنان بر روی پارچه میدوزند ۸ - و مشتی
خواهتد ‎Ty‏ بزند ‎٩‏ .

کشیش ۰۱ بروزن حشیش ‎beta‏

و ‎ol,‏ نمابان و زاهدان و عالمان صاری ‎eth‏
‏وممرب ‎OT‏ قمیس است بکسر قاف .

() چش : - وخواه بر زمین .

۱ - « که , خط که اندر کشند , کثه گویند . » « لفت فری ص14۱ *.

۰ در دستوراللغه ( معنی : بطان ) و نیز مهذب‌الاسماء ‎Lat)‏ : بطان ) همین لفت
‎JK‏ رفته « فرهنگ نظام + طبری 851 ( تنگ اسب ) « واژه نامه ۵۷۹ *.

‎Gh, «- ۴‏ راکثه خوالند یعنی که مال مردم را بخودکشد . » «لفت ‎Ht‏

‏قی: ‎kesh raftan‏ ( دزدیدن » ربودن ) در تهرانی . ۴ - ‎Gat,‏ هم بمعنی «حیوان
پالان افکنده»آورده ‎Ll‏ شاهد نیاورده است . 8 از :کش ۲+-ی ( حاصل مسدر).بتشدید
شین هم‌آمده . 1 - رك : کشخان . ۲ - اسم مقعول از « کفیدن *.

‎a‏ - قسمی از فلاب دوزی که روی پارچه با ابربشم ‎OTL‏ میکردند و گلابتونآ ترا
هم کشیده میگفاند « فرهنگ نظام » - یز بمعنی زر وسیمی که از حدیده گذر دهند *
شخصم ز فرقت تو چو زر کشیده شد ‎ye‏ ز حرت تو چو سیم کشید هگیر.
‎ey les ow‏ فرهنگه نظام *.
‎٩‏ - سیلی‌را کشیده گوبند. *- قس:عربی‌قسیس» ‎+e) qeshshisha» yt‏
کاهن) «ممجمیات عربیه - سامیه ص۱۷۹ *ژابا ۰۳۳۹ , آرامی 085[115[38 (شیخ,کاهن) ‎Kp?‏
‏© کثیدن - بکر اول و فتح چهارم ( در ‎ted‏ مر کزی ) و بفتح اول ؛ از :کش +
بدن ( پسوند عصدری ) . جزو اول در اوستا - ‎Karsh‏ < بارتولمه 4۵5 » « تب رک ص ‎NTA‏
‎sae‏ باستان - ‎)karsh‏ کشیدن), پپلوی 6251020 . کردی 18180 ( کشیدن) ‎GUN.‏
‏81 . بلوچی ‎kashag‏ . ۷۵51028 ( کشیدن , برداشتن ) , ارمنی ( ‎karshem (t¢‏
( کشیدن ) « اسشق ۸۵۹ * در اوراق مانوی ( پپلوی ) 8658 ( ‎oat‏ . کوشیدن )
‎Henning , A list of Middle Persian..., BSOS,IX,1.p.84 )‏ ) امتداد دادن «
‎ata‏ کردن » دراز کردن » مثبسط کردن - بسوی خود آوردن » با خود ب
========= pdf 483

‎CLS‏ بت اول و ‎gt‏ بالف کنیده
‎ems‏ زده » ‎yk‏ است مشهور ۱ - و |
کوبند که بر روی اخگر و زغال پز سس و کليچة
خیمه را نیز کفته‌اند و ‎ath glass oT‏ مان
سوراخ که برسرستون خیمه محکم کنند ۴ ؛ وبا
جیم فارسی هم‌آمده است .

‏کمادد یوس ۴ ‎pee‏ اول و دال
‎sen!‏ وسکون رای قرشت وبای حطی‌بواو کشیده
وبین معقص زده » لفتی است ‎gy,‏ ومعنی‌آن
جربی بلوطالارض‌باشد وآن کیاهی است‌سبزردگه
وبیار تلم و آنرا در ابتدای اسشقا دهند افع
است .

‏کماس = بنتم او بر وزن مملی »
‎yy‏ از تنکه باشد و آن کرد و پهن وکردن

‎els ‏کوماج , بان‎  »یدیشره‎ gsm ٩

‎“a qs ‏فرهنکه‎ rag
: ‏کویند . جامی کوید‎
‏کماچ خیمه را ماند که هوان‎

‏مهوت

‏کوتاه میباشد باندام کاسه پشت و ‎NAST‏ سفال
وچوب هم میازند ۴ و ‎pty‏ شبانان وصافران
دارند - ‎Ly‏ چویین وکشکول کدایان را هم
گفته‌اند ۵ - و بمعنی کم و اندك هم‌آمده است
که عربان قلیل خوانشد ۷ ؛ وبدو معنی ‎cael‏
‏اول وتشدید ‎git‏ هم گفته‌اند .

‏کماسه بضم اول وفتح سین بی‌قطه »
کاریز کن وچاء جوی را کوبند ۷ - وبععنی‌شاهد
و زن فاحشه و قحبه هم‌آمده است - و ‎ghd‏ را
یز کوبنه بمنی ‎AT Spat‏ مردی و زلی‌هر
دو داشته باشد - ونام کوهی‌است ازولات‌خراسان
- و بقتح اول بمعن ی کمای است که تنگهگردن
کوناه وکاسه چوبن باشد ۸ .
کماصی ‎٩‏ ۰ با سین بی ضله بر وزن

‎Sort‏ ازآرد برنج و غیرآن و شکر

‏۴ - رشیدی‌آرد : ه کلیچةٌ خیمه را بمشابهت ‎oT‏ ( نان ) کماچ

‏ز ‎OUT Sy‏ بدندان یم نره. ©

‎germandrée , chamédrys = xamaidhrus yt» ‏کماذربوی . از‎ = ۴
‏تحت‌لفظ عربی‎ Leg ‏و بلوطالارض‎ RAY» Ye ‏دزی‎ « petit chéne ,) officinale (

‏از بام ‎Git‏ آن است « عفار ۱۸۹ ف *.

‏۴ کمامه «رشیدی» . «کمای » کوزه‌هابوو

‏پپن از سفال که در زیر بغل درآویزند . چنانکه ابوالعبایکوید :

‏گیرم که ترا اکنون سه خانه کمای است

‎ye 6‏ : سروری ؛ رشبدی :
رود بسوی عم ب رکتف تهاده جراب

‎ohh ‏ره‎ - ٩

‎» ‏یکی نامه که چندت همه‌کای است.‎ gt
Nee ‏لفت فری‎ «

‏رود ‎oly‏ فنا در بغل گرفته کمای.
شمس ‎Spb‏ .

‏۷ - جهانگیری نیز در معنی اول گوند : «کاری نکن باشد

‏وآن را کمانه یز گوبند » وباین معنی« کماسه» تصحیفی است از « کمانه .کار کن باشدو کومش.

‏.همین ‎Soy‏ « لت فری ‎٩ 4٩۷‏ ورك : کمانه ‎MLSs‏

‎el‏ بلخ کماسه کری تکو داند

‎: ‏کیان (هم)‎ A
‏که از کماسه می‌اندر پیاله کرداند.‎

‏سوزلی سمرقندی « رشیدی ©

‎٩‏ - از : کمای ‎GAC ST gee)‏ ( اس مصدر ) ؛ درلهجةً تهرانی ( مخصوصاً درتداول

‏زین ) [عقصه :
آب‌آن ‎ate‏ ز ابتدای وجود

‏به کماسی کند » نه بفزاید .

‏سراج راجی « رشیدی >
‎olay)‏ اطع ۴۱)

========= pdf 508

‎x ۷۷۵7‏ ۳
هم‌آمده است ؛ وباین ‎em‏ اول‌هم کفته‌اند.

‏کنیسه ۳ - بکر اول و ثالی بتستانی
رسیده و فتح سن بی ‎abet‏ , معبد ‎ApS‏ را
کون .

‏گنیش؟ = ‎bee‏ ول و ثالی ‎glut‏
‏کشیده و بشن اقطه‌دار زده 6 بمعتی کردار است
خواء نيك باشد و خواه کردار بد (۱)

‏بهم تبدیل مییابند ۱ - و نم اول وفتح تحتالیء
در عربی نامیرا گوبند که در اول آن اب یا ام
باشد همچو ابوالمعانی وام‌کلتوم .

‏کنیز ه بفتح اول بروزن تمیز» معروف
است که پرستار و ‎Kies‏ زنان باشد و بعربی
جاربه خوانند ۴ - و دخثر بکر دوشیزه را نیز
‎aT‏ - و بمعنی بن و بخ خوشة خرما ورطب

‏بیان بیست*و یکم

‏درکاف تازی با واو مشتمل ‎Meas»‏ و ببست وهفت لغت و کثابت

‎aly ‏باشد و‎ aly ole ‏اول و سکون ثالی » مردم و بز رکه را کویند ۱ که‎ pe ‏ه‎ ST
‏فراخ | کوچك وتنگه راکود- وبمعنی چه‌شد و کجا‎ oly ‏زبرك و عاقل باشد ۵ - و بضم اول‎

‏(۱) چش : خواه‌يك باشد وخواه بد ۰ ۰ (۲) خم۱: بردوصد *

‎pl ۱‏ ( دوم شخص جمم ) ازمصبر «کردن © در بیض لهجههای ایرانی .قس: دهیت
)= رهید) « قابوسنامه چاپ نفیی ص ۱۸۲ و مقدمه ص مه » ۰ بخوانیت ( ۳ بخوانید) « ‎Ted‏
‏ص ۱۵۹ و مقدمه ص مب ‎٩‏ . ۴ اوستا ‎kainika_. kainin_ . kanya_‏ ( دختر
جوان ) . پهلوی 18 ‎soe.‏ باستان ‎kanyd‏ , 802 , و این کلمه م کب است از :
کن (زن) + یز ( پوند صفیر [ < یزء (دوشیزه )] ‎gel‏ ۰۸۷۰ قی :کنيزك ( پهلوی,
پازند 1۵01621 ) « اسئق - هوبشمان *۸۷ » امُروزه بمعنی‌زن استو مجازاً بمعنی‌زن‌پرستار
استممال میشود :

‏دستت چو نمی رسد به بیبی درباب کنیز مطبخی را ۰ (مثل)

‏۴ ره : کنشت . کنيسة در عربی معبد بپود و صاری و کفار را کفته‌اند ؛ و امروزد
در ‎ie‏ معبد بهود را «کتیی» وممید صاری را « كثية » ومعبد مسلمانان را «جامع»(ومسجد)
و معید بت پرستان را هیکل کونند « اقرب‌الموارد » هدایت کوید : « کنیسه ؛ معید بهودوهاری
است . پسآنجه صاحب ‎Oy‏ معبد گبران کفته خطای فاحشی است » « مقدمهٌ الجمن آرا در
اشتباهات برهان » و محشی چك (س ‎٩۱۲‏ ح ) ‎altel‏ قاموی همین قول را آورده .

‏۴ < کش ‎(ge)‏ قی : بخشیش ‎Ay)‏ : رسالة اسم مصدر بقلم لگارنده س ۱۲۳ )

‏9 -قی : کاو ‎wants‏ این بیت داصر خسرو را شاهد آورده :

‏کو نبود آنکه دن پرستد هرکز دن‌که پرسند مگرکه ‎dale‏ کودن؟
در دیوان ناصر خسرو چاپ تپران س ۳۳۹ ?5 ‎Cp.)‏ آمده , ولی چون «کودن » در مسراع
دوم آمده ظاهراً گوبند. خواسته استآترا بدوجزه * کو» و « دن » در عصراع ‎Jal‏ بیاورد.بنابرین
باحتمال قوی در شمر مزبور ‎GEL‏ تازی است . ۱ = کوی .
```


## [2026-09-06T16:13:20.041Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT; python3 - <<'EOF'\nimport re\np='BQT_v3_pages.txt'\ntxt=open(p,encoding='utf-8',errors='replace').read()\nparts=re.split(r'\\[pdf page (\\d+)\\]',txt)\npages={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}\nfor n in [551,552,553]:\n    print('========= pdf',n)\n    print(pages[n][:2600])\nEOF"
}
```


### [2026-09-06T16:13:22.600Z] TOOL RESULT

```
========= pdf 551

وچیزی دا یز کویند که بدان طلا ‎Sealy oy‏
‎UT‏ بپم ‎as, Ses‏ وآلرابسریی لحم خواند۱ -
و پزبان ‎er‏ پممنی مکر و حیله - و جنگه
وجدال - وحایض شدن زن باشد ۴ ۰

. ‏با بای فارسی بروزن اژدها‎ - YAS
weg ‏بردع بوده واو را‎ ak ‏تلم زلی است که‎
. ۴ ‏میگنته وممرب آن قیدافه است‎

کیرخ - با اود ‎gh‏ رسیده و رای
بی‌هطةٌ مقتوح ‎Gln‏ تقطمدار زده » دوتختمیان
پیوسته ‎ath‏ وقرآن و کتاب.برآن پندوصربی
رحل خوانند ؛ ‎orks‏ معنی باکاف فرسی‌هم آمده
است واسح آن است * ۰

kin ge 1 ay ‏بر وزن‎ 2 IS
‏ونگاهداختن وحصول چیزهایی باشد که پیش از‎
+ ‏در ذهن پوشیده بودم‎ yl

گیریان ۱ ‎shh‏ حطی بر وزن
میهمان » ییمتی فد وقربان باشد وآن‌پدلی‌است
که خود را با دنگری را ‎oly‏ ازبلا برهاشد.

کیره با ول ‎gt‏ کشیده وبزای نتطهرار
زده ۰ بسعنی تمد باشد ۷ رآنرا از پشم مالند
و جریی لید (۱) کویند .

)و9

‎oe”‏ - بکس اول وسکون تانی‌وسین
‎tty‏ » چن و شکنج راگویند ۸ - و بعربی
توبره وخر ‎aly‏ را خوانند ‎٩‏ .

‏کیسر گو نه ۲۰ - بنتع اول ‎ty‏
‏ونون آخر وسکون ثالی ورای فرشت‌وکان‌فارسی
‎aly‏ رسیده ۰ نام دوائی است که ‎Bae BT‏
فولیون و بعربی جمده گویند . برقان ‎Wake‏

‎+ ‏است‎ Gib

‎oj, ۲ oS‏ اشکنه‌برسمانیرا
کویند که بوقت رشتن بر ‎Uo‏ پیچیده شود -

‏کیص و۱۲ - بنتح‌اول وسکون ثالی‌وئالت
بواوکشیده » بمعنی کی رکونه است وآن‌عوالی
باشد که ‎wan‏ جمده گویشد .

‏کیسه بر دو ختن - کنایه از توفع

‏اشتن بافراط باشد .

‏کیمه بصا بون‌ددن - کنابه از
خرح کردن وخالی نمودن باشد +

‎gla”‏ = بررزن ریته دارتضیرا
‎San‏ چیزها بوقت ارزانی بخرد ونگادارد
ودر ایام کرالی بفروشد ۱۳ .

‎SEP gods”‏ بسنی‌سن

‏(۱) خم ۱ :کید .

‎gan? - ۱‏ لیم ‎Ub‏ و نقره یبای موحده است .۰ « رشیدی ‏ .
۴ - رگ : منتهیآلارب » محیط المحیط , منتخب اللقه .

‏۴ رك : قدافه » ورك : رشیدی .

‏۴ - و :گیرخ . ۵ - ظ:گیر: قی: ور.

‎٩‏ - «کیربان بای حطی بوزن میهمان » در ‎Oley‏ فدا وقربان ؛ وین صحیف است.
‎AT Om‏ بوزن ومعتنی قربان (است) » «سراج اللغات بنفل فرهنگهه نظام چ سم )

‏۲ - را : جهانگیری » رشیدی ۰

‎. ‏سیم وزر .» «منتهی‌الارب»‎ LS ‏بالکس‎ FH) - ٩

‏۸ -۱کنون یز ‎KIS‏ بهمن ممتی است .

‎Ay NO‏ :کیسو.

‏0-«کینه + ریسمان پردوك پیچپدن بود چون ‎ule‏ . عنسری (بلخی) کوید 0

‏م رکه‌تابد(باید . دهضدا) کسته کیسته را دور باشد بناوه کرسنه را»

‏«لغت فری 8۸ ۰*6

‎۰ ‏د کی وفروهه وفرموكه نیز خوانند .» «رشیدی»‎ UP
. ‏رد : کی رکونه » ورك : فهرست مخزن‌الادوبه‎ ۴

‏۴-کفرودین را یست در بازار عشق

‎AS‏ چون خ مکیسوی تو.
‎Slim‏ غز لوی «رشیدی».
(برهای فاطع ‎(tre‏

========= pdf 552

—\vee~

شدن باشد ‎ute‏ چیزی صورت اسلی خود رارها

کند وصورت دیگر بهتر از آن بگیرد .
کیش با ‎gt‏ مجهول بروزن رش»
بممنی تر کش باشد وآن ‎gle‏ است که‌تیرد رآن
کنند وبر کمر بندند ‎٩‏ - ویمعنی دین ومذحب
‎chy‏ هم آمده ‎col‏ ۴ ۰- وپرمرغالرا گویند
مطلفاً ‎Lye‏ پری که برتیر اصب کنند ‎phe‏
‏شپری است در جزیره‌ای از دربا و ‎Ol‏ بهرموز
اثتهار دارد ؛ و وجه این آن است که چون بر
بلندیهای اطراف‌هرموز ‎aisle ae Teg‏ کیش که
ت رکش باشد پنظ درمیآبد ۴ - ونوعی ازجامه

بو که از کتان بافند 6 - ‎(by‏ جانوری‌است که"

از پوستآن پوستین کنند ۱ - ودرخت شمشادرا

۱ - رك : قی رکش » ت رکش :
آسمان. کر ‎OE‏ بر بندد

"را یز گفته اند ۷ - ولنظی است که ‎Ke‏
‎ee‏ بازی در محل خودکویند4 و ‎OT‏ چنان
است که مهره‌ای ازمهره‌های شطرنج را درجابی
کذارند که در یکی از ‎Steerer Tighe‏
دارد شاء حریف الاح ازآن ‎ale‏ بر خیزد با
‎aS oT oe‏ - ورادن ودور تمودن مر غ‌راییر

"باین لفظ کنند » واين لفظ امراست بردور ‎ed‏

ورفتن ‎em,‏ دور شو وبروه ودرشطریج ليز همین
ممتی را دارد ‎t‏

‎oh = ‘ de ۱‏ اول ومیم‌بروزن
روش مند » ‎eins‏ جیاری و ‎AB‏ باشد بلفت
زد واوستا .

‏ی ‎So‏ اول بروزن تیخمچر

‏تیر ‎et‏ تو نهد د رکیش +
*انوری آبیوردی چاپ تبربزس ۴۱۲۲ .

‎késh= ۴‏ اوستا- 686508)(اعتراف » عهد),پهلوی(851] )5 ‎(poryotkésh:‏
‏ارمنی ‎kesh‏ «اسشق*۸۸» . در اوستا «تکششه» در مورد ‎ter sel nT‏ استممال شده » درمقایل
‎Uy‏ (دین) ؛ ولی در فارسی کیش بممنی مطلق آیين ودین آمده :

‏لب با قوت ‎Ky‏ وال چنگه
۴ - زرای اوست‌کار ملك و ملت

‏می چون لمل وکیش زرنهتی.

‏دقیقی طوسی ۰
چوتیر چارکیش از فاق وییکان +
عبدالغادرنایینی «جپانگیری» «رشیدی».

‎«AT? - ۴‏ جزیره‌ای‌ازجزایر بحر فاری » ودر تاریخ وصاف اس تکه چون‌ازهکانهای

‏مرتفع بینند زمین آن بهیئت کیش یمنی ت رکش تمابد وقیس معرب ‎OT‏ وبهرموز اشتهار دارد ۰ >
«سراج اللفات بنقل فرهنگه نظام» . بمد از قشم مهمترین جزيرة ماحلی ایران* کیش» است که
۵ کیلو متر طول و ۸ کیلومتر عرض دارد و ‎Maly‏ تنگه ای بمرض ۱۸ کیلومتر ازساحل ‎tie‏
‏شده» این‌تنگه بخویی فابل کشتیرالی است . جمعیت آن قریب 40*۰ تن ‎col‏ «جغرافیای‌طبیعی
کیهان +۱۰ ورك : معجم‌البلدان : قیس. این جزبرء غیرجزبر؛ هرموز (هرمز) است ولی‌دد
زمان اهمیت ‎tye‏ هرمز» کیش با دیگر جزایر خلیج فاری جزو منطفةً حکمرافن پادشاه هرمز
بود . 6 خیش ‎(pe)‏ , قی : بزدی«کیش» (مقنعة زن) » درسبزواره کیش‌حمام» يك
‎os 5‏ است «فرهنگه نظام» . ۲ - 5 : جهانگیری» رشیدی ۰

‏۷ - رك : جپانگیری » رشیدی .> ‎OAT‏ 1510 بشمشاداهای کوناه ‎Soy‏ که در
‎leans Liste‏ کارند , اطلاق‌شود . ۸ - قی : کشت ‎Sy)‏ : شه در هم نکتاب) .

‎٩‏ - از دساتیر «فرهنگه دساتیر ۰۷۹۷۲ . ‎V0‏ کیخ «کین ۰ رمس باش دکهبر

‎۱ : ‏چشم نید . ابوشعیب (هروی) کوید‎ Bye
ere ‏چشم هن .سرخ است ی و سدع‎ EF Sle ae
NPA RA Oe?

========= pdf 553

کوشهای چشم ‎dey‏ وکیرا که چشم‌درد کند
گوبند (۱) .

‎be ge LAT‏ بر حق باشد
چه‌کی بمعنی عادل وغباد بمعنی برحق است -
ونم پادشاهی هم بوده مشهور در ابران ودر عهدا
‎plots!‏ بزرکتر ازو لبود . صد ‎JL‏ پادشاهی
وملك ‎gly‏ کرد » ودرین زمان ‎LET‏ نوسند که
بجای ‎oe‏ فاف باشد ودر فرس قدیم حرف قاف

‎JUS‏ - بروزن ‎Sab‏ مردمرددپیشه
وجماش و کوچه گرد و صاحب عربده و بدست
ولوند رااگوبند » وبلین معنی بجای حرف ای
نون هم آمده است .

‏کیفره بفتح اول بروزن حیدر, مکافات
‎SG‏ و مکافات بدی را گوبند و بعریی جزا
خوانند ۴ — وظرفی باشد تفار مانند که ماست
‎ows‏ وبرزیگران شیر و ماست در آن کنند
و کار آن از کنار تغاراندك بلند ترمیباشد۴
وناودانی هم دارد ماتند جرغتو وبلبله و مشك
دوغ - وهرچیز را نیز گوبتد که شیر وماست‌در

‎(VD‏ خم ۱ : -گویند

‏- از :کی (هم.) ‏ ناد ‎Cpa)‏ -

‎{YON

‏آو کته ‎ot‏ تمه ایست که در ‎ol‏
‏طلمی بته‌الد وهیچکس ‎ond‏ بررگرفتن ‎OT‏
‏قلعه نیافته است - و سنگیرا نیز کویند که بر
کنگر؛ قلمه نپند تا چون غنیم ترديك آید بر
سراو زنند و بعربی مترس خوانند ؛ وباین معتی
بکسر اول‌هم آمده‌است © - وندامت‌وپشیمانیرا
یز ‎WS‏ -واهرورودخانة آ بر اهم کنتهالد۷ -
ویمعنی محثت ورلج وحیف باشد ۸

‎SPOS‏ بنتح اول وناك و سین
بی‌نقطه بالف کشیده و بمیم زده ۰ بمعتی کتمان
است‌وآن سر نگاهداشتن رازها باشد بمنی‌اقهای
راز تکردن .

‏کیفوس* © بپروزن افوی » بمعنی
‎cole‏ ات و آن بذل کردنی باشد بتا بر
وجونب بحاچت ‎gan‏ از ‎veel‏ شود .6

‏کی لهر اسب"۱ » از ‎dhe‏ بادشاهان
کیانی است که کیقباد و کیضرو و کیکاوی‌باشد.
کویند چون‌در ‎sae‏ لهراسب پادشاهی‌ازوبزر کت
‎ays‏ لفط کی را برآن زیاده کردند و کی‌لهراست
‎Wass‏

‎6 SET « ‏ممحف‎ ۴ sake : ‏رگ‎

‏جماشی ‎oy‏ . آن که پنهانك دوست را بیند گوبند « گیغالکی کرد» . بوشکور (بلخی) گفت :

‏بکیغالگی رفته از پنجپیر

‏رمیده از اومرغك گرمسیر . »

‏رشید ی گوید : این لفت تصحیف است صحیح «کتغال» است

‏۴ - ماررا هر چند بهتر پروری
۴ - شیرعشاق بپستان دربیارشدست

‏۵ رك : رشدی

‏« لت فری ۰۲۳۰ .
چون یکی < ‎AS oT ge‏ بری-
‎a Cyl‏ فرهنکه نظام ».

‏چشم ‎Sols‏ فروریزد در کی
طیان بمی ‎‘by Sle‏ : رشیدی .

‏۱ - فزهنگها بیت ابوشکور ( رل : ح ‎Cr‏ را برای این

‏معنی شاهد آووده‌اند ورشیدی کوید « دربیت ابوشکور بمعنی مکافات بدی نیز توا گفت»وهمین

‎۲ . ‏است‎ oc
. ‏«سروری*‎

‎. ‏-ظ . بر ساختة فرقة آنرکبوان‎ ٩
‏اساطیری «کیالی»»‎ LL ‏شاعان‎ Ly -۱
. ‏ورك : خباد‎ ,» LAS: ‏کیقیاه - رك‎

‏« در ‎Ses‏ وفائی مسطور است که بزبان بعی از ‎OLY,‏ اهر باشد.»
۸ - ظ . از همان بیت ابوشکوز استتباط کرده‌اند .

‎5 ‏از: کی («.م.) + لهراسب(«م.)‎ ute
‏لفط «کری» کی را اطلاق کرده اند.‎
```


## [2026-09-06T16:13:55.869Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== KLN recent\"; grep -n \"^recent,\" KLN_1966.txt; echo \"== KLN cushion/cuisse\"; grep -n \"^cushion,\\|^cuisse,\" KLN_1966.txt; echo \"== SKT\"; grep -n \"^recent\\|^cushion\\|^heel\" SKT.txt | head"
}
```


### [2026-09-06T16:13:55.940Z] TOOL RESULT

```
== KLN recent
== KLN cushion/cuisse
9879:cuisse,  cuish,  n..  usually  in  the  pi.,  armor  for  pro¬ tecting  the  thigh.  —  ME.  cuissues,  fr.  OF.  cuis- seaux,  pi.  of  cuissel,  fr.  cuisse,  ‘thigh’,  fr.  L. coxa,  ‘hip’,  whence  also  It.  coscia,  ‘thigh’,  Rum. coapsa,  ‘hip,  thigh’,  O Proven?,  coissa,  cueisa, ‘thigh',  Catal.  cuxa,  OSp.,  Port,  coxa,  of  s.m. See  coxa  and  cp.  cushion.
== SKT
```


## [2026-09-06T16:13:57.431Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; ls site/pages/254.jpg 2>/dev/null; pdftoppm -f 254 -l 254 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg254 && echo done"
}
```


### [2026-09-06T16:13:59.906Z] TOOL RESULT

```
site/pages/254.jpg
done
```


## [2026-09-06T16:14:02.610Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"cushion,\" KLN_1966.txt | head -3; echo \"--- recent\"; grep -n \" recent, adj\\|recent,  adj\" KLN_1966.txt | head -3; grep -n \"^recens\\|recens,\" KLN_1966.txt | head"
}
```


### [2026-09-06T16:14:02.699Z] TOOL RESULT

```
9493:OI.  kaksah,  kaksd,  ‘armpit’,  OE.  huh,  ‘heel’,  and with  the  first  element  in  OE.  hoh-sinu,  ‘hock sinew’.  See  hock,  ‘joint  in  the  hind  leg  of  a horse’,  and  cp.  cuisse,  cushion,  Quixotic. Derivative:  cox-al,  adj.
10006:ciiscote,  ciisceote,  of  uncertain  origin, cushion,  n.  —  ME.  quisshin,  cusshin,  fr.  OF.  cois- sirt,  cussin  (F.  coussin ),  fr.  ML.  *coxinus,  fr.  L. coxa,  ‘hip’;  see  coxa  and  cp.  cuisse.  Cp.  also It.  cuscino  and  Sp.  cojin,  which  are  French  loan words.  The  orig.  meaning  of  OF.  coissin  was ‘hip  cushion’.
10007:Derivatives:  cushion,  tr.  v.,  cushion-ed,  adj., cushion-y,  adj.
--- recent
31893:-onis,  fr.  recensus,  pp.  of  recensere,  ‘to  count, enumerate,  survey’,  fr.  re-  and  censere,  ‘to  rate, estimate’.  See  censor  and  -ion. recent,  adj.  —  MF.  (=  F.)  recent ,  fr.  L.  recentem, acc.  of  recens,  ‘new,  fresh’,  which  is  formed  fr. re-  and  I.-E.  base  *qen-,  whence  also  OI.  kani- nah,  ‘young’,  kana,  kanya,  ‘girl’,  Gk.  xaiv6<; (for  *xav,6c ),  ‘new’,  Gaul.  Cintu-  —  OIr.  cetu-, ‘first’,  Mir.  drum,  ‘I  descend  from’,  ciniud, ‘tribe,  family’,  OSlav.  nacinq,  nacqti,  zacinq , zacqti,  ‘to  begin’,  koni,  ‘a  beginning’,  konici, ‘end’  (prop,  ‘the  beginning  of  the  other  end  of a  row’).  Cp.  -cene,  cenosite,  Cenozoic,  cncenia, kainite.  Cp.  also  rinse.
6948:-cene,  combining  form  denoting  certain  periods in  geology,  as  in  Eocene.  —  Introduced  by  the British  geologist  Sir  Charles  Lyell  (1797-1875) fr.  Gk.  xatvoe,  ‘new’,  which  is  cogn.  with  L. recens,  gen.  -ends,  ‘new’.  See  recent  and  kainite. cenobite,  coenobite,  n.,  a  member  of  a  religious order  living  in  a  community.  —  Eccles.  L.  coe- nobita,  ‘a  cloister  brother’,  fr.  coenobium,  ‘a  con¬ vent’,  fr.  Gk.  xoivopiov,  ‘life  in  community, monastery’,  fr.  xoivo?,  ‘common’,  and  plop, ‘life’.  For  the  first  element  see  coeno-,  for  the second  see  bio-.
31867:recension
31890:recense,  tr.  v.,  to  review,  revise.  —  Back  forma¬ tion  fr.  L.  recensere.  See  recension, recension,  n.,  review,  revision.  —  L.  recensio,  gen.
31893:-onis,  fr.  recensus,  pp.  of  recensere,  ‘to  count, enumerate,  survey’,  fr.  re-  and  censere,  ‘to  rate, estimate’.  See  censor  and  -ion. recent,  adj.  —  MF.  (=  F.)  recent ,  fr.  L.  recentem, acc.  of  recens,  ‘new,  fresh’,  which  is  formed  fr. re-  and  I.-E.  base  *qen-,  whence  also  OI.  kani- nah,  ‘young’,  kana,  kanya,  ‘girl’,  Gk.  xaiv6<; (for  *xav,6c ),  ‘new’,  Gaul.  Cintu-  —  OIr.  cetu-, ‘first’,  Mir.  drum,  ‘I  descend  from’,  ciniud, ‘tribe,  family’,  OSlav.  nacinq,  nacqti,  zacinq , zacqti,  ‘to  begin’,  koni,  ‘a  beginning’,  konici, ‘end’  (prop,  ‘the  beginning  of  the  other  end  of a  row’).  Cp.  -cene,  cenosite,  Cenozoic,  cncenia, kainite.  Cp.  also  rinse.
32949:rinse,  tr.  v.  —  ME.  rincen ,  fr.  OF.  re'incier,  rain- cier  (F.  rincer),  prob.  dissimilated  fr.  recincier, fr.  VL.  *recentiare,  ‘to  make  fresh,  to  wash, cleanse  with  water’,  fr.  Late  L.  recentare ,  ‘to make  fresh',  fr.  L.  recens,  gen.  recentis,' new, fresh’.  See  recent.
```


## [2026-09-06T16:14:11.662Z] TOOL CALL #45: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg254.png"
}
```


### [2026-09-06T16:14:12.015Z] TOOL RESULT

```

```


## [2026-09-06T16:14:12.013Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T16:14:28.477Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '16090,16200p' CHEUNG.txt"
}
```


### [2026-09-06T16:14:28.547Z] TOOL RESULT

```
*kars/*xrah ‘to draw, plough’ 
*AVESTAN: YAv. Каг$- ‘to draw (furrows), plough’ || (+ *apa-) ‘to drag away’ || (+ 


*aua-) ‘to draw down’ || (+ *pari-) ‘to draw around’ © Liste: 15 
Pres. them.: IND. 3pl. YAv. auua.karosonti (V 5.5), OPT. 35р. YAv. apa.karsöit (N 48), ҮАУ. 
pairi.karsöit (V 19.21), 3р1. YAv. karsaiion (Yt 19.80) 


"MIDDLE PERSIAN: MMP krs-, qrs- ‘to pull, draw’ || kyst (pret. stem) ‘to sow, plant’ 


(supplet. stem of k’r-, *karH) > DMMPP: 208b 
Pres.: IND. 1р1. MMP krsym: Partic.: perf. pass. II MMP qrsyd || Partic.: perf. pass. MMP kyst 


*PARTHIAN: kyst (pret. stem) ‘to sow, plant’ (supplet. stem of k’r-, *karH?) 
=> Ghilain: 96 | DMMPP: 202b 

Partic.: perf. pass. kyst, qyst 

*SOGDIAN: BSogd. хг ‘to pull, attract’, CSogd. xš ‘to drag’ || (+ *apa-) BSogd. 
"px r/n$, CSogd. рхёп ‘to remove, eliminate’ || (+ *a-) BSogd. ’’k’ys(-) ‘to pull out’ 


242 *kars/*xrah 


|| (+ *ui-) BSogd. wx’rs, CSogd. wxs, MSogd. wxnš ‘to deliver, save’ || (+ *ham-) 
BSogd. ’nx’s-, CSogd. nxš- ‘to withdraw, retire’, (caus.) SSogd. ’nxrs(-) ‘to 
subjugate, overtake [i.e. to cause to withdraw]’ (on *r see GMS: $147) 

Pres.: IND. 3sg. BSogd. xrst, OPT. 3sg. dur. BSogd. xns’y ’Stn; Impf.: IND. 3sg. CSogd. xs; Inf.: pret. 
CSogd. xst, MSogd. ’kstyy (Sogd.Tales: 469), MSogd. ksty (ВВВ: 35), MSogd. kstyy (BBB: 42) || Pres.: 
IND. 35р. CSogd. grwst, SUBJ. 159. CSogd. qrwsn; Partic.: pres. CSogd. qrwsny || (+ *apa-) Pres.: IND. 


35р. BSogd. ’px’rst, BSogd. ’px’nst, BSogd. px’nst, SUBJ. 1sg. BSogd. px’rs’n, 35р. BSogd. px ns't, 
IMPV. BSogd. рх ri? (GMS: $698: subj.); Inf.: BSogd. ’px’rs’y, BSogd. ’px’ns’y, BSogd. px’ns’y || (+ 
*2-) Pres.: IND. 3pl. BSogd. ’’k’ys’ntw || (+ *ui-) Pres.: IND. 35р. BSogd. wx’rst, SUBJ. 1sg. BSogd. 
уух т°п, 3sg. CSogd. wxst, PREC. 3sg. MSogd. wnxsytyy; Impf.: IND. 3sg. CSogd. wyxs; Fut.: IND. 
3sg. CSogd. wxstq’; Partic.: pres. CSogd. wxsnw; Inf.: BSogd. cnn wx’rs’y || + *ham-) Pres.: SUBJ. 3sg. 


BSogd. "nx '$'t; Caus.: fut. IND. 159. SSogd. SSogd. ’nxrs’m km 

*CHORESMIAN: xSy- ‘to draw, drag’, xSs- (sec. pass./inch.) ‘to be dragged’, m/xry- 
(caus. ?) ‘to draw’ || (+ *apa-) pxry- ‘to draw out’ || (+ *upa-) bks- ‘to feed’ (< *‘to 
look after’) || (+ *pati-) pcxrs- (intr./inch.) ‘to pull oneself back; to stop, become 
quiet/still’, p’cxr- (caus. ?) ‘to restrain, pull back’. o The Chor. formation m/xry- 
reflects an old caus. *xrahaja-, after which the intervoc. -h- disappeared. 
Subsequently, the long *4 was shortened in front of *; which is in line with other 
ЕП. languages. = Samadi: 242, 240, 21, 164 f., 147 

*BACTRIAN: Kıbaryo ‘plough-(ox)’ (U8) => S-W, Bact.: 199b 

*NWIR: Widely attested: NP kasidan/kas- ‘to pull, draw’, Bal. kast, kaš(š)it/kaš(š)-, 
Kurd. (Kurm.) Kisin/Kis-, Kesan/kes-, (Sor.) kisan/kisé- ‘to drag [intr.], crawl, be 
drawn, slip, flow’, Zaz. kiristis/kiréSen- ‘to drag’, Abz. kesa/kes-, Anar. -ikeso/ 
(impv.) ikis, Awrom. kesay/kes- ‘to draw, pull’, Fariz. -ki$ä-/-kis-, Yar. -kisa/-kis-, 
Gz. kás-, keš-/käšā, Gil. (Rsht.) -kaSe-, Gur. (Kand.) kisa-/-kis-, Ham. kásayán/Kes-, 
Isfah. kesän/kes-, Khuns. kes-/kesa, Mah. kis-, Nn. kisa/kis-, Natan. -kiS-/kis-, Siv. 
kis-, kes-, käš-/kišā, kešā, Soi bä-nkisa (sic!), Tal. kaše, Varz. kasä/kas- ‘to draw, 
pull’ 

*NEIR: Oss. I. xaessyn/xast, D. x&ssun/ast (< I. ?), xaersun/xarst ‘to carry; to breed, 
raise; to cultivate, plant; to last, endure’, Wa. xa$-/xaSt- ‘to draw, pull, drag; to 
carry’, Yghn. kis-, kis-/kista ‘to sow’, xaš-/xášta ‘to draw’, Yi. xóš-/xíšč-, M. xas- 
‘to pull, drag’, ? Sh. kiräx(t), Rosh. kiréx-t, Yzgh. xarax-, Вагі. Ciröxt, Orosh. kiroxt 
‘to remove, haul, drag’, Khf. хахё ‘ploughing’, M. kugo ‘plough’ (*krsaka-) || (+ 
*abi-) Oss. I. ivxzersyn/ivxerst, D. evxaersun/evxa(r)st ‘to put across across a river, 
dangerous place; to lead someone; to help someone who is in trouble, danger; to 
rescue, save’ || (+ *ham-) Oss. I. æxxæssyn/æxxæst ‘to reach, attain’, D. 
ænxæssun/ænxast ‘to seize, grab’ 

*MISC: Par. kas ‘eyebrow’ (kas kan- ‘to pull, stretch, contract’ < NP) 

*SANSKRIT: kars ‘to pull, drag, plow’ (RV+) = EWAia I: 319 


*kartl 243 


9 The root *kars- appears to have a rare variant *xrah-, with a different kind of 
ablaut (i.e. Schwebeablaut), similar to *fras-/pars-. This may therefore account for 
the initial x- in some Iranian forms. The frequent loss of the liquid *r is quite 
striking as well. The root *kars-/xrah- specifically refers to the ploughing process, 
after which the field can be sown in, i.e.*karH^-. As a consequence, the roots 
*kars-/xrah- and *karH’- either show mutual influence, cf. Sh. kiräx(t), etc., or are 
part of a suppletive paradigm. 

*PIE *K"els- ‘to plough’ = LIV: 388 f. | Pok.: 639 

*IE COGNATES: Hitt. /gulsanzi/ ‘they scratch into’, Gr. téAoov (n.) ‘last furrow of the 
field’ 

*REFERENCES: KPF I: 82b, 144b f., 248b; Ivanow 1926: 420; IIFL I: 267b; KPF II: 217; Christensen, 
Contributions I: 71, 169 f., 262; IIFL II: 216a, 269a; Abrahamian 1936: 116, 130; Lambton 1938: 41a, 
77b; Abaev, Slovar’ I: 556, 223 Ё; Andreev — PeSéereva 273a, 357a Ё; MacKenzie 1966: 100; EVS: 41b, 
99b; WIM I: 69; WIM II/1: 78; WIM III: 111; Abaev, Slovar’ IV: 188 ff.; Werba 1997: 171; Paul 1998: 
303b; Steblin-Kamenskij 1999: 406; Cabolov 2001: 555; Cheung 2002: 247 f., 108 ff.; Lecoq 2002: 147 
ff., 153 (passim); Korn 2005: 318, 392 


*kart! ‘to cut’ 

*AVESTAN: YAv. kart- ‘to cut’ || (+ *aua-) ‘to cut down to’ || (+ *upa-) ‘to cut on’ || 
(+ *fra-) ‘to cut up’ > Liste: 15
```


## [2026-09-06T16:14:42.771Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== HRN Köcher\"; grep -n \"Köcher\\|Kocher\" HRN.txt | head -10; echo \"== HUB\"; grep -n -i \"kaniz\\|kanīz\\|kanik\" HUB.txt | head -10"
}
```


### [2026-09-06T16:14:42.829Z] TOOL RESULT

```
== HRN Köcher
3396:'Köcher, (z. B. vd. 4 (137)), patkärok (AV.).
3800:406. Ur^) 'Pfeil', tlrkes, terkes 'Köcher 5^).
3832:80); vergl. auch mhd. ^(5^rÄ;is *Köcher* bei Wolfram sowie Miklosich,
10676:120»»»« kantlr 'Köcher (vd. 14 (36); Yätk. Zar. S. 52
11378:bedeutet wohl nicht 'Köcher (Geiger, Yätkär-i
== HUB
```


## [2026-09-06T16:14:44.688Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== MON kusan\"; grep -n \"کوسن\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head -5; echo \"== ARY kanız/kesidan\"; grep -n \"کنیز\\|کشیدن\\|کیش\" incoming/ARY/ARY_pages.txt | head -10"
}
```


### [2026-09-06T16:14:44.771Z] TOOL RESULT

```
== MON kusan
incoming/MON/MON_2vol_Adena_v1_djvu.txt:7472:خارصینی. از ای زو انهات اناد کوسنت که 
MON_part1.txt:7472:خارصینی. از ای زو انهات اناد کوسنت که 
== ARY kanız/kesidan
1618:معنی این واژه در زبان‌های ژرمنی؛ ترس» درکشیدن.
8302:دمیدن (به چم "نفس کشیدن" و "فرت کردن یا ورزیدن") / ۲۸۳
8433:چم اين واژه در زبان‌های رمانس (لاتین و فرانسه و غیره): دوام آوردن» طول کشیدن» به درازا کشیدن,
11222:جم این واژه در زبان‌های غپرابرانی؛ نفس نفس زدن» با صدا با به سختی نفس کشیدن,
11494:چم این واژه در زبان یونانی: شیهه کشیدن. :
12053:۱ ۲ چم این واژه در زبان سانسکریت: کشیدن» دریدن
12070:۱ بازگشت به: کشیدن» چرخ.
12668:چم این واژه در لیتوانی: غنودن» درازکشیدن,
15140:ال ها دنل پسگشت‌ها کیش دی
15492:چم این واژه در زبان‌های سانسکریت و لیتوانی: حمل کردن؛ بردن» کشیدن.
```


## [2026-09-06T16:14:48.138Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '3795,3840p' HRN.txt"
}
```


### [2026-09-06T16:14:48.180Z] TOOL RESULT

```
löschen' (400).
405. teheniy tehm *stark'^).
V
ap. Cid^ra^ta/ma- N. pr.; aw. ta/nia-; im PehlevT
nicht belegt.
406. Ur^) 'Pfeil', tlrkes, terkes 'Köcher 5^).
ap. vergl. Tigra-, med. riy()iif xaXovöi t6 tohvf^ia ol
Mrjöoi (Dionys. Eusthat. 994); aw. tiyri- Tfeil'; phlv.
tir *Pfeir.
LW. kurd. tlr, tlrek; bei. ttr, n. fir *Pfeil, Kugel'
(387).
über Tir =: aw. Tistrya- vergl. zuletzt Nöldeke,
Persische Studien I, 33 folg. und auch Bartholomae,
ZDMG. 44, 554. Ich möchte die Entstehung von Tir
durch Contraction aus Tistrya- mit Geiger, Etym. d.
BalüöT s. V. tlrhand 'Sternbild des Orion (No. 388) doch
nicht für durcliaus unmöglich halten. Zwar bleibt
aw. str gewöhnlich im Np. erhalten, indess vergl.
beide aw. pistra-^ deren Verhältniss zu phlv. pesak
etc. allerdings nicht klar ist. Ganz unwahrscheinlich
ist jedenfalls A. Stein' s Meinung, der (Zoroastrian
Deities on indo-scythic Coins, Indian Antiquary, 1886
S. 93) die Bedeutung von tir 'Pfeil* auf den Gottes-
namen Tir übertragen sein lässt. Die dort erwähnten
Münzen haben die Form TEIPO.
*J FJ hat folgende Belegverse des altertümlichen Wortes aus
Pirdüsl:
h^nezd'ik'i sengul ftristäd^ büd
hemänä kX sah ü Wiemzäd^ büd
und
fShem hesi^ der pehl^äm zebän
hemerdi füzün z*ezdehä-yl dem an
Dr. Landauer belegt mir das Wort aus Srthn. I, 228 Vers 1768,
III, 1524 Vers 497 {tehm), IXT, 1109 Vers 754, 1617 Vers 2125 (Wtem).
') Tir reimt auf qir (Sahn. I, 112 Vers 900); falsch auf ser in
dem unechten Verse Sahn. I, 212 Anm. 8, Calc.
*) Daraus ital. tttrcasso, franz. carqitois (de Lagarde, Ges. Abh.
80); vergl. auch mhd. ^(5^rÄ;is *Köcher* bei Wolfram sowie Miklosich,
Denkschr. WAW. Band 38, 53 s. v. terlces.-- 92 -
407. tere *finster , tereyt^) (auch in Indien spricht man heute
nur ttre).
aw. *tq3ri/a-, vergl. tar, tank (No. 370) ; phlv. terak,
LW. afy. ttra; bei. n. feray (274); siyn. t4r,
408. f^;s: *scharf, heftig; schnell', tej 'PfeiF; tese *Axt*2).
g. ^f/ 'scharf; mäz. tTjf,
ap. vergl. ^i5rra[/a?*rfa-; aw. bröi&rö.]tapJa^ mit
```


## [2026-09-06T16:14:54.700Z] TOOL CALL #50: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-06T16:14:54.707Z] TOOL RESULT

```


```


## [2026-09-06T16:14:59.830Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%A9%D9%86%DB%8C%D8%B2",
 "prompt": "Give the full Persian etymology of کنیز (kaniz): Middle Persian form, Old Iranian/Avestan antecedents, suffix analysis, and any cited sources (Hasandust, MacKenzie, Horn). Also any mention of کنیزک."
}
```


## [2026-09-06T16:15:01.116Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%A9%DB%8C%D8%B4",
 "prompt": "List all Persian etymologies given for کیش (kēš / kiš): the one meaning 'quiver', the one meaning 'religion/creed', and any island name. Quote the etymological derivations and any Middle Persian/Avestan forms and cited sources."
}
```


### [2026-09-06T16:15:06.720Z] TOOL RESULT

```
# Persian Etymology of کنیز (kaniz)

Based on the Wiktionary entry, here is the documented etymology:

## Middle Persian Form
The entry traces کنیز to a variant of کنیزک (kanizak), which derives from Middle Persian *knyck'* /kanīzag/, described as a "diminutive of [script needed] (knyk' /⁠kanīg⁠/, 'maid')."

## Proto-Iranian Origins
The word ultimately comes from Proto-Iranian *kanyáH* meaning "small girl; maiden," which continued into Proto-Indo-Iranian *kanyáH*.

## Linguistic Connections
The entry notes that کنیز is "cognate with Sanskrit कन्या (kanyā)," establishing its Indo-European heritage.

## Noted Limitation
The Wiktionary entry contains a significant gap: it indicates "[script needed]" for the Middle Persian forms, suggesting the original scripts are missing from the documentation.

## Sources Not Cited
The entry does not reference Hasandust, MacKenzie, Horn, or other specialized etymological sources you mentioned. The Wiktionary article provides only the basic etymological chain without detailed scholarly citations for these technical details.
```


### [2026-09-06T16:15:08.362Z] TOOL RESULT

```
# Persian Etymologies for کیش

Based on the Wiktionary entry, here are the Persian etymologies listed:

## Etymology 1 (Religion/Creed)
The entry states it was "Inherited from Middle Persian 𐭪𐭩𐭱 (kyš /⁠kēš⁠/, 'faith; dogma')." The Middle Persian form and its meaning are provided, but no further ancient source or Avestan cognate is cited in this section.

## Etymology 2 (Chess Term - "Check")
This meaning derives from a different origin: "Presumably onomatopoeic, used to scare off chickens, gaining the meaning of 'go away, run' and then being used in chess to literally, '(king) go away', referring how the king has to make a move to survive."

The entry cites the Dehkhoda Dictionary as the source for this etymology but provides no Middle Persian or Avestan forms.

## Etymology 3 (Proper Noun - Kish Island)
The entry provides no etymology for the island name—it simply identifies کیش as "Kish Island, an Iranian island in the Persian Gulf" with no historical derivation offered.
```


## [2026-09-06T16:15:16.867Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/cushion",
 "prompt": "Give the full etymology chain for English 'cushion': Middle English, Old French/Anglo-Norman forms, Vulgar/Medieval Latin *coxinus/culcitinum, Latin coxa, and any competing derivation (e.g. from culcita). Quote the text."
}
```


## [2026-09-06T16:15:17.726Z] TOOL CALL #54: WebSearch

```json
{
 "query": "حسن‌دوست ریشه‌شناسی «کیش» ترکش تیردان فارسی"
}
```


### [2026-09-06T16:15:23.701Z] TOOL RESULT

```
# Etymology Chain for English "Cushion"

Based on the Wiktionary entry, here is the complete etymological progression:

**Middle English → Old French → Vulgar Latin → Latin**

The entry states: "From Middle English *quysshyn*, from later Old French *coissin* (modern *coussin*), from Vulgar Latin *\*coxīnus* ("seat pad"), derived from Latin *coxa* ("hip, thigh")"

The text indicates the Vulgar Latin form *coxīnus* represents a "seat pad" meaning, with the suffix possibly modeled after Latin *pulvīnus* ("pillow"). The ultimate source traces to Proto-Indo-European *\*koḱs-* meaning "joint, limb."

**Competing Derivation:**

The etymology section does not present an alternative derivation from *culcita*. However, the translations section lists Latin *culcita* (f) as a synonym for cushion, suggesting this was a parallel Latin term for the concept rather than a competing etymological source for the English word specifically.

The documented chain shows a direct line: coxa (Latin body part) → coxīnus (Vulgar Latin seat pad) → coissin (Old French) → quysshyn (Middle English) → cushion (Modern English).
```


### [2026-09-06T16:15:26.683Z] TOOL RESULT

```
Web search results for query: "حسن‌دوست ریشه‌شناسی «کیش» ترکش تیردان فارسی"

Links: [{"title":"کیش (تارت) - ویکی‌پدیا، دانشنامهٔ آزاد","url":"https://fa.wikipedia.org/wiki/%DA%A9%DB%8C%D8%B4_(%D8%AA%D8%A7%D8%B1%D8%AA)"},{"title":"معنی ترکش | لغت‌نامه دهخدا","url":"https://www.vajehyab.com/dehkhoda/%D8%AA%D8%B1%DA%A9%D8%B4"},{"title":"(PDF) نقد فرهنگ ریشه‌شناختی زبان فارسی [نوشتۀ دکتر محمد حسن‌دوست Review of \"An Etymological Dictionary of the Persian Language,\" by M. Hassandoust]","url":"https://www.academia.edu/24471058/%D9%86%D9%82%D8%AF_%D9%81%D8%B1%D9%87%D9%86%DA%AF_%D8%B1%DB%8C%D8%B4%D9%87_%D8%B4%D9%86%D8%A7%D8%AE%D8%AA%DB%8C_%D8%B2%D8%A8%D8%A7%D9%86_%D9%81%D8%A7%D8%B1%D8%B3%DB%8C_%D9%86%D9%88%D8%B4%D8%AA%DB%80_%D8%AF%DA%A9%D8%AA%D8%B1_%D9%85%D8%AD%D9%85%D8%AF_%D8%AD%D8%B3%D9%86_%D8%AF%D9%88%D8%B3%D8%AA_Review_of_An_Etymological_Dictionary_of_the_Persian_Language_by_M_Hassandoust_"},{"title":"معنی ترکش | فرهنگ فارسی معین","url":"http://www.vajehyab.com/moein/ترکش"},{"title":"محمد حسن‌دوست - ویکی‌پدیا، دانشنامهٔ آزاد","url":"https://fa.wikipedia.org/wiki/%D9%85%D8%AD%D9%85%D8%AF_%D8%AD%D8%B3%D9%86%E2%80%8C%D8%AF%D9%88%D8%B3%D8%AA"},{"title":"جزیره کیش - ویکی‌پدیا، دانشنامهٔ آزاد","url":"https://fa.wikipedia.org/wiki/%D8%AC%D8%B2%DB%8C%D8%B1%D9%87_%DA%A9%DB%8C%D8%B4"},{"title":"محمد حسن دوست نویسنده کتاب فرهنگ ریشه شناختی زبان فارسی(5جلدی) | ایران کتاب","url":"https://www.iranketab.ir/profile/23034-mohammad-hasandust"},{"title":"کتاب فرهنگ ریشه‌شناختی زبان فارسی (جلد 5)","url":"https://fanuus.org/library/%D9%81%D8%B1%D9%87%D9%86%DA%AF-%D8%B1%DB%8C%D8%B4%D9%87%D8%B4%D9%86%D8%A7%D8%AE%D8%AA%DB%8C-%D8%B2%D8%A8%D8%A7%D9%86-%D9%81%D8%A7%D8%B1%D8%B3%DB%8C-%D8%AC%D9%84%D8%AF-5/"}]

Based on the search results, here's what I found regarding your query about حسن‌دوست's etymological work on the Persian words کیش, ترکش, and تیردان:

Mohammad Hassandoust is the author of the Etymological Dictionary of the Persian Language.

Regarding the specific words you asked about:

**ترکش (Turkash) / تیردان (Tirdān):**
Turkash means arrow-holder (tirdān). It is a shortened form of "tirkash" meaning arrow-holder, where the vowel pattern was changed from kasra to fatha for brevity and the ya was deleted.

**کیش (Kīsh):**
According to the search results, Dehkhoda (a major Persian lexicographer) connects the name Kīsh with "turkash" and the place for arrows. Additionally, in Pahlavi Persian, kīsh refers to an underground canal (qanat).

The search results show that Hassandoust's etymological dictionary is a comprehensive reference work on Persian language origins, though the specific entries he provides for these words aren't detailed in these particular search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-06T16:15:32.343Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://www.vajehyab.com/dehkhoda/%DA%A9%DB%8C%D8%B4",
 "prompt": "Quote Dehkhoda's entry for کیش, especially the senses 'ترکش/تیردان' (quiver) and any statement that it is a shortened/altered form of تیرکش, plus the island sense."
}
```


## [2026-09-06T16:15:34.244Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%DA%A9%D9%88%D8%B3%D9%86/",
 "prompt": "What do the dictionaries (Moein, Dehkhoda, Amid) say about the Persian word کوسن — its meaning and its stated foreign origin (French coussin / English cushion)?"
}
```


### [2026-09-06T16:15:38.396Z] TOOL RESULT

```
I appreciate your interest in the Dehkhoda dictionary entry for کیش (Kish), but I need to be direct: the webpage content provided doesn't actually contain the detailed entry you're requesting.

The visible text only shows:

"کیش . (اِخ ) از شهرهای اکد بوده است . (ایران باستان ج 1 ص 113)."

This single entry defines کیش as a city from ancient Akkad, without mentioning the senses you're looking for (ترکش/تیردان meaning quiver, any etymological notes about تیرکش, or island-related meanings).

To get the comprehensive Dehkhoda entry with those specific senses, you would need to access the full dictionary entry directly through the واژه یاب website or a complete Dehkhoda dictionary source.
```


### [2026-09-06T16:15:40.459Z] TOOL RESULT

```
# Persian Dictionaries on کوسن

Based on the Abadis dictionary page, here's what the three major Persian dictionaries state:

**Dehkhoda Lexicon**: Describes it as "a medicinal plant that aids digestion" (noted in Dehkhoda's handwriting), along with the meaning of "pillow/cushion."

**Moein Dictionary**: Defines کوسن as "بالش، بالشتک" (pillow, small pillow).

**Amid Dictionary**: Specifies it as "a small decorative pillow placed on furniture for support."

**Regarding Foreign Origin**: The page does not explicitly state an etymological connection to French *coussin* or English *cushion*. However, the English translations provided are "cushion, pillow"—linguistically consistent with Romance language origins. The dictionaries present these as established Persian equivalents rather than discussing the word's etymological journey from European languages.
```


## [2026-09-06T16:15:52.701Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%DA%A9%D9%86%DB%8C%D8%B2' --note 'page 254, root Ken, Persian kanîz: MP kanīzag dim. of kanīg, PIr *kanyáH' ; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/cushion' --note 'page 254, root Kenk1/Koksâ, English cushion < OF coissin < VL *coxīnus < L coxa < PIE *koḱs-' ; python3 tools/fetch_source.py 'https://abadis.ir/fatofa/%DA%A9%D9%88%D8%B3%D9%86/' --note 'page 254, node 5 Persian kûsan «کوسن» cushion: Mo'\"'\"'in/Amid glosses' 2>&1 | tail -20"
}
```


## [2026-09-06T16:15:55.550Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== ARY latin index\"; grep -n -i \"KANIZ\\|KESIDAN\\|KESHIDAN\\|KISH\" incoming/ARY/ARY_latin_index_pages.txt | head; echo \"== SYN girl/heel/hip\"; grep -n \"4\\.36 HEEL\\|HEEL$\\|4\\.37 HIP\\|GIRL\" SYN.txt | head"
}
```


### [2026-09-06T16:15:57.007Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/0d31b6067f20bea3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6b1c540fab1cf0fc.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9cfab87b71f3334c.txt
```


### [2026-09-06T16:15:58.932Z] TOOL RESULT

```
== ARY latin index
8557:DEvo- (GAUKISH) zEU (RUMANIAN) gle,
11808:(4515 SIMENGLISH) palS3t KISHTAN APAHLAVD (5 3h,
11809:CULTIVATE KISHAGH BALUCHD gr ge
11829:REFERENCES beta KASHITAN, KESHIDAN, KESH-
11830:POKORNY, = SSSsSt~CS~«aD KISHIN KURDISH) 52,5
14084:MEKKISH HITTITE) ca MAESTRO S(TTALIAN) gid
== SYN girl/heel/hip
2255:| CHAPTER 2 MANKIND: SEX, AGE, FAMILY RELATIONSHIP 9.1 Man! (Human Being) 2.47 GRANDMOTHER 9.91 Man? (vs. Woman) 2.48 GRANDSON 2.92 Woman 2.49 GRANDDAUGHTER 2.93 MALE’ 2.51 UNcLE 9.94 TeMALE 2.52 AUNT 9.942 Sex 2.53 NEPHEW | 9.25 Boy 2.54 NIECE 9.26 GIRL 2.55 CousIN | 2.27 CHILD 2.56 ANCESTORS 2.28 INFANT 2.57 DESCENDANTS 231 HUSBAND 2.61 Fatuer-1n-Law ~ 2.32 Wire 2.62 Morser-in-Law 2.33 Marry 2.63 Son-1n-Law 2.34 Marriage; WEDDING 2.64 DauGuHTEr-in-LAw 2.35 FaTHER 2.65 BrotuEr-in-Law 2.36 MoTHER 2.66 SisteR-1n-Law | 2.37 PARENTS 2.71 STEPFATHER 2.41 Son 2.72 STEPMOTHER 2.42 Daucuter 2.73 STEPSoN | 2.43 Cuiup (Son or Daughter) 2.74 STEPDAUGHTER 2.44 BroTuHEr 2.75 ORPHAN 2.45 SISTER 2.76 Wipow 2.452 BrotHEer(s) AND SISTER(s) 2.81 RELATIVES 2.46 GRANDFATHER 2.82 FamiIny 2.1 MAN! (Human Being) oy ae por Goth. manna Lith.  Zmogus, pl. Zmonés iy ae eee s oN maor, gumi Lett. cilveks It. heinb - an. —menneske ChSl. elovékit Tr. iter an menniska SCr. Eoujek Sp. hombre ME man(n), guma Boh. tlovtk Rum. om man Pol. czlowiek Tr. duine NE man Russ. elovek Nir. duine Du. mensch Skt.  manu-, purusa- W. dyn OHG man, mannisco, gomo Av. __masya-, masyaka-, Br. den MHG mensch OPers. martiya- NHG mensch
2404:2.26 GIRL
```


## [2026-09-06T16:16:02.531Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '2404,2440p' SYN.txt | cut -c1-1500; echo \"=== ARY kesidan page\"; awk 'NR>=11790 && NR<=11840' incoming/ARY/ARY_latin_index_pages.txt | cut -c1-200"
}
```


### [2026-09-06T16:16:04.614Z] TOOL RESULT

```
2.26 GIRL
wats 4}, Kopy, TapOEevos
2.27 CHILD
mats
2.28 INFANT
vamos, matéloy, Bpedos
Grk. ais 8, Kbpos xopn, xoplrat, kowé\Aa aa.sl Bpédos, pwpd NG  é7#pt puella puert infans Lat. si x ragazza fanciullo, bimbo bambino ie It. rag ‘oune fille enfant petit enfant, bébé n J he : Tr. gargo ha nino criatura uchacho muchach 0 , SPs iaiat (fat) fata i copilag, prunc 5 ‘ ingen elap, lenab noidiu Ir. Ab ail cailin leanbh, pdiste naoidhe NIr. hachgen, hogyn geneth, hogen plentyn maban W. note 2 plac’h bugel, krouadur bugelig, krouadurig Br. Pp mawt barn barn Goth. magus ON " piltr mer, stilka — barn ungbarn Dan. dreng, Norw. gut pige, Norw. jente barn sped barn es coe poste flicka barn spadt barn OE cnapa, entht mezden bearn, cild cild ME _ knave, lad, boy maid(en), girle, lasce ee (barne) enfaunt, babe, babi boy (lad) girl (maid, lass) child infant, baby (babe) a aad meisje kind kind OHG knabo, kneht magad kind, barn kind MHG knabe, kneht maget kind kind NHG knabe méddchen kind sdugling, kleines kind Lith. vatkas mergaité, mergelé varies ei Lett.  puisis, pucka meita érns pupa berns ChSl.  otroki dévica, otrokovica détt otrote, mladinict SCr.  djetak djevojke dijete djeteSce Boh.  chlapec, pachole, hoch holka, divka dité dét'atko, nemluvné Pol.  chlopiec dziewczyna dziecko, dzieci¢ dzieciatko, niemowle¢ Russ. mal'tik devica rebenok (d:tt, pl.) mladenec Skt. bala, kumara- balz-, kumari-, kanya- bdla-, kumara-, ete. bala-, cicu-, etc. Av. kainya aperanayuka-
2.25, 2.26, 2.27. Several of the words
A noticeable number of the modern
for ‘boy’ and ‘girl’ are correlative mascu- line and feminine forms, as Grk. 6 za‘s, 4 wats, Lat. puer, puella, It. ragazzo, ragazza, Sp. muchacho, muchacha, Goth. magus, mawt, Skt. bala-, bali-. In such cases the discussion will be under ‘boy’.
The Same words often apply to ‘boy’ Og ‘girl’ and to a young male or female Servant, attendant’. Hither the former or the latter may be the earlier meaning, as indicated by the etymology.
Since ‘boy’ and ‘girl’ are, with refer- ange to the parents, the ‘son’ and ‘daugh- ss the words for the former may also ; ae and in part are the usual ones ee atiter. See 2.43, 2.44. The ex- i in the opposite direction also
Curs, but less frequently,
words for ‘boy’, ‘girl’, and ‘child’ were originally colloquial nicknames, deroga- tory or whimsical, in part endearing, and finally commonplace. These, as is natural, are of the most diverse, and in part obscure, origin. The enumeration of the colloquial expressions that are in occasional or dialectic use would fill a volume. They are based on names of animals and all sorts of inanimate ob- jects, like NE kid, brat (orig. ‘cloth, rag’), flapper (in U.S.), NHG bengel (‘cudgel’), etc.
Many such are collected in v. Friesen, De germ. mediageminatorna; Brug- mann, Sichs. Ges. d. Wiss. 1906.173; Johanssen, KZ 36.373 ff.; Bjorkman, IF 30.257 ff.; Much, Wort. u. Sach.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar a
AD A Ea Meena Gs
88
1.45; Ivan Pauli, ‘Enfant’, ‘gargon’, ‘fille’ dans les langues romanes (426 pp.!); Taylor, Mod. Lang. Notes 1929. 309 ff.; Hilding Bick, The Synonyms for ‘Child’, ‘Boy’, ‘Girl’ in Old English (271 pp.).
Here only those that have become the usual words are considered, unless in-
cidentally.
2.25. ‘Boy. 1. Grk. rats, gen. rar- d6s (fr. *rafid-) ‘boy, girl, child’, NG matot ‘child’ (fr. dim. zaidiov), Lat. puer ‘boy’, whence puella ‘girl’ : Skt. putra-, Av. puéra- ‘son’, Osc. puklum ‘filium’, Pael. puclois ‘pueris’, Skt. pota- ‘young of an animal’, Grk. zaipos ‘little’, Lat. putus ‘boy’ (rare), pusillus ‘very small’, Goth. fawaz ‘few’, etc., all fr. the notion of ‘small’. Walde-P. 2.75 ff. Ernout-M. 782, 790.
Grk. xépos (mostly poet.), Ion. xodpos, fr. *xopros, with fem. xdpy ‘girl’, Ion. koUpn, Dor. xwpa, Arc. kdpfa : xopévvupe ‘satisfy’ orig. ‘nourish’, Lat. créscere ‘grow’, ete. Walde-P. 1.408. Hence NG xépy ‘girl, daughter’ or xopizo. with dim. suffix.
NG dye ‘boy’ (of school age), dim. of Grk. awpos ‘untimely, immature’. Cf. &ywpos in a late Theban epitaph of a youth of 23 years (Glotta 15.174).
2. It. ragazzo (whence ragazza ‘girl’), in earliest use ‘stableboy, servant’, orig. dub. REW 7019.3. Pauli, op. cit. 143.
Fr. gargon, OF r. gars (nom.), garcon ‘servant, young man’, of Gmc. orig., perh. fr. a Frank. *wrakjo = OFris. wrekkio = OHG reccheo ‘exile, adven- turer’ (NHG recke), OE  wrecca ‘exile, wretched person’ (NE wretch), Gamillscheg 457f. Bloch 1.327. Other- wise (fr. a Frank. *wurkjo ‘worker’) REW 9578a.
Sp. muchacho, with fem. muchacha
~~ Digitized by Arya Samaj. Foundation Chennai and eGangotri
SELECTED INDO-EUROPEAN SYNONYMS
‘girl’, perh. through mocho fr. Lat. mutilus ‘maimed’. REW 5791.
Rum. bdiat, generally taken as pple. of bdia ‘bathe’ (mostly tmbaia). So Tiktin, Saineanu, s.v. Otherwise REW 887, fr. a bdta ‘streicheln’, easier seman- tically, if bdia in this sense exists (not in Tiktin and unknown to informant).
Rum. fd (mow used only in certain phrases), fr. Lat. fétus ‘offspring’. REW 3273. Hence fem. fatd ‘girl’ (so with Diez, Densusianu, and Pauli, op. cit. 71, more probably than as directly fr. Lat. féta ‘pregnant, newly delivered’, with shift of application to ‘one capable of childbearing’, as REW 3269, Puscariu 588, Tiktin s.v.).
3. Ir. mace ‘boy’ and ‘son’ (NIr. mac, W., Br. mab ‘son’), see under ‘son’ (2.41),
NIr. buachaill ‘boy, servant, cow- herd’, fr. MIr. buachaill ‘cowherd’, like W. bugail ‘cowherd’, Corn. bugel ‘herds- man, shepherd’, Br. bugel ‘child’: Grk. Bouxédos ‘cowherd’. Walde-P. 1.696. Pedersen 1.54. Henry 47.
W. bachgen, cpd. of bach ‘little’ and cen of cenau ‘offspring’ : Ir. cinim ‘spring from’, cenél ‘race’, etc. Pedersen 2.33.
W. hogyn, prob. new masc. to hogen ‘girl’ (2.26).
Br. paotr ‘boy, valet’, MBr. pautr, loanword through OFr. fr. Gme. Cf. OFr. pautraille ‘canaille’, orig. ‘pack of ragamuffins’, LG palirig ‘ragged’, NE paliry, dial. palt ‘rubbish’, Dan. pjalt ‘rag’, etc. Henry 217. Falk-Torp 831.
=== ARY kesidan page
KUSHNATI, KUSH- KAOSH, KUSHAITI, KUSHATI
THEINEIN (GREER) gly, PAHLAVI) 5 34g
KUENZI HITTITE) asa KUSHTAN, KOXSHITAN
KUSHTIN (KURDISH) 159,
KUSHAG, KUSHAGH:(BALUCHD gz sh
BO
[pdf page 405]
pent | OF
BUCK: (KILL) 288-290 ‘REFERENCES eentheg
SKEAT: (GWHEN) 754 POKORNY =—S*~*~*~*~«O ID
VFA-N FEA hs Jo ebb aby MACKENZIE: (KILL) 120
ot
oe
alo “estat” |y lal y tn sejly gel Jol BUCK -1
Wp AT 1 Sadler V5 92 05 atl pe
see ay aj! y "G25" Clans LAT” Godly
[euumvare Tate lm rhe |
CULTIVAR (PORTUGUESE) Ji y, KARAYEITI (AVESTAN) gl)
(4515 SIMENGLISH) palS3t KISHTAN APAHLAVD (5 3h,
CULTIVATE KISHAGH BALUCHD gr ge
. AFGHAND (4) glk
‘REFERENCES bcwhey KARAL, KAREL
poRmR ee] chRAT, oan ea SL
BARNHART: CALATI, KARSUS, CHAR
(COLONY) 190, (CULTIVATE) 241 TELOS, POLOS (GREER) hi
MACKENZEE: (TILL) 137 COLERE LATIN) oY
BUCK: CULTIVER FRENCH) «1,3
(CULTIVATE, TILL) 493-494 CULTIVAR (SPANISH) lies
SKEAT: (COLONY) 122 COLTIVARE H(UTALIAN) .g\dts\
10" sebGdby CULTIVA RUMANIA) «gag,
«teeta
EA Ty HEN
wore OLY ili Obj 235 atl ee oT
7 .
[pdf page 406]
os
Tv | Dds
KJEL ALBANIAN) gist KARSH-, KARSHA. :(AVESTAN) gles,
PAHLAVI) 5 shay
REFERENCES beta KASHITAN, KESHIDAN, KESH-
POKORNY, = SSSsSt~CS~«aD KISHIN KURDISH) 52,5
MACKENZIE: KASHAG, KASHAGH :(BALUCHI) gx ss
(DRAM) 111, (PULL) 129 AAFGHANT) (su) lidh
BUCK: KXAL, KASHAWEL
(DRAW, PULL) 571-572 KARSH., KRSH- :(SANSKRIT) y Sle
170 ebb ub, KARSHEM ARMENIAN) gis)
sentloal
. CAPS 45h
SKARP, SKERP AAVESTAN) gee sl
(4slt)(OLD HIGH GERMAN) oS gllT KAMNA, KAMBISHTEM
SCARF HOLD PERSIAN) jel) pe,
```


## [2026-09-06T16:16:15.084Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nt=open('incoming/ARY/ARY_latin_index_pages.txt',encoding='utf-8',errors='replace').read()\nparts=re.split(r'\\[pdf page (\\d+)\\]',t)\npages={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}\nprint(pages[406][:1800])\nEOF"
}
```


### [2026-09-06T16:16:16.933Z] TOOL RESULT

```
os
Tv | Dds
KJEL ALBANIAN) gist KARSH-, KARSHA. :(AVESTAN) gles,
PAHLAVI) 5 shay
REFERENCES beta KASHITAN, KESHIDAN, KESH-
POKORNY, = SSSsSt~CS~«aD KISHIN KURDISH) 52,5
MACKENZIE: KASHAG, KASHAGH :(BALUCHI) gx ss
(DRAM) 111, (PULL) 129 AAFGHANT) (su) lidh
BUCK: KXAL, KASHAWEL
(DRAW, PULL) 571-572 KARSH., KRSH- :(SANSKRIT) y Sle
170 ebb ub, KARSHEM ARMENIAN) gis)
sentloal
. CAPS 45h
SKARP, SKERP AAVESTAN) gee sl
(4slt)(OLD HIGH GERMAN) oS gllT KAMNA, KAMBISHTEM
SCARF HOLD PERSIAN) jel) pe,
SCHARF (ULGERMAN) glT KAMNA, *KANBIYAH, KANBISHTA
(QL(OLD ENGLISH) 4S godt KAM, KEM s(PAHLAVD) (5 34,
SCEARP KEM, KIM KURDISH) 525 at
SHARP (4UMENGLISH) p81 KAM = NR ADOC
SHARP (4UN(DANISH) Slats KAM “4APCHAND (uty) gh
SKARP (4U}(SHEDISH) 5.8 yo KHRAMBOS GREER) gli
SKARP (4Lt}(NORHEGIAN) 5335 (4L}(OLD SCANDINAVIAN) AS Gotha!
SCHERP (4LEx(DUTCH) gale SKARPR
SKARP()L4Y(OLD SAXON) oS pS
(4LM(OLD FRISIAN) oS 534.3
```


## [2026-09-06T16:16:30.482Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; grep -n \"kainin\\|kainika\\|kanyä\\|kanya\" WLD_Bd1_1930_dli_70244_djvu.txt | head -10; echo \"== koksa\"; grep -n \"kok̂sā\\|koksä\\|koksa\\|Achselgrube\" WLD_Bd1_1930_dli_70244_djvu.txt | head -10; echo \"== hanhila\"; grep -n \"hanhila\\|kenk\" WLD_Bd1_1930_dli_70244_djvu.txt | head -10"
}
```


### [2026-09-06T16:16:30.567Z] TOOL RESULT

```
== koksa
2574:arm. anut „Achselgrube“ (zuniichst aus *asmif). 
21089:ahd. hegidraosa ..Hode" (nicht besser dariiber Siitterlin, s. u. koksa: und 
21277:(verscbieden von kakia ,,Achselgrube“; Zupitza Gutt. Ill); ahd. hag ,.Ein- 
25238:striipp“ (Fick I 4 182) sind Sonderanwendungen von kakm ^Achselgrube 1 ' 
28738:Ai. kaksd, kaksa-h „Achselgrube, Gurtgegend der Pferde", av. kasa- m. 
28767:Anschauung, die *koksa ursprgl. ausdriickte, ist noch vollig dunkel. Siitter- 
28773:Yerfehlt Lewy KZ. 40,423 {*koksa- sei Redupl. von *aksa). 
== hanhila
21154:y.rjrog), hall „Pflock, Stock" ( *hanhila-; Liden Uppsalastud. 89f. ; da- 
21978:iiber ai. kaca-, apr. kexti s. u. *kenk- „giirten“), vielleicht gleichzeitig 
24048:kt'^r-. keng-, kek-, kenk- 
24051:keg-, keng- und kek-, kenk- etwa kleiner Pflock, bes. zum Aufhangen, 
25182:q e ii3qd- — kenk- 
25211:1. kenk- „giirten, umbinden, anbinden“. 
25244:kenk qen-q(e)l-o- 
25256:— Gegen Beziekung zu *kenk- „Kniekehle“ s. d. 
25258:2. kenk- „brennen (dorren), weh tun; auch bes. von brennendem Durst 
25282:3. kenk- etwa „Kniekehle oder Ferse".
```


## [2026-09-06T16:16:34.057Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; sed -n '25282,25305p' WLD_Bd1_1930_dli_70244_djvu.txt; echo \"-----koksa\"; sed -n '28735,28775p' WLD_Bd1_1930_dli_70244_djvu.txt; echo \"-----ken-3\"; grep -n \"„jung\\|frisch hervorkommen\\|kanina\" WLD_Bd1_1930_dli_70244_djvu.txt | head"
}
```


### [2026-09-06T16:16:34.124Z] TOOL RESULT

```
3. kenk- etwa „Kniekehle oder Ferse". 

Lit. kenkle „Kniekehle", khika „ds., Hesse", lett. cinksla „Sehne in der 
Kniebeuge"; anord. ha- ( *hanha -) in ha-mot „Sprunggelenk, Fersengelenk", 
hd-sin „Kniesehne des Hinterbeins bei Tieren, Fersensehne beim Menschen", 
ags. hoh „Ferse" ( : *hanha -), anord. hall „Ferse“ ( *hanhila -), ags. hcla m. 
„Ferse“. Zupitza Gutt. 115, KZ. 37, 399. — Als nasallosen Yerwandten 
betrachtet Fick III 4 67 ahd. hack a f, „Ferse“, nhd. Hacke ( *koknd ), anord. 
hpkill „Kniegelenk am HinterfuB", sowie die Sippe von lat. coxa: da 
letztere idg. *kokso- ist (av. ka&a -), ware die Annahme notig, daB bait. 
kenk-, kink- den ausl. Palatal durch Angleichung an den Anlaut durch 
Yelar ersetzt hatte. Die weitere Vermutung, daB Zshang mit *kenk- 
„giirten" unter „krumm sein" bestehe, ware wegen des anl. Yelars dieser 
Wz. dann um so bestimmter abzuweisen, ist aber auch bei Beschrankung 
auf den Yergleich von kenk- ,,giirten" mit bait, kenk-, kink- und germ. 
hanha- der Bed. halber nicht einleuchtend. S. auch Petersson IF. 35, 271. 

(qen-q(e)l-o- „beweglich, unstet".] 

Ai. cahcala- „beweglich, unstet" wurde verglichen mit gr. y.iyy.log „Bach- 
stelze, oqveov nvy.vdjg tijv ovgdv y.ivovv Hes." (Fritzsche C. St. 6, 315 f., 
Brugmann C. St. 7, 289 ; gr. t aus e vor -j- Gutt. Kons. nach Solmsen 
Beitr. I 215)? Das ind. Wort ist aber sicher wie ai. caiicuryate, carcur- 

-----koksa

qoksa „Korperteilbenennung“ (arisch auch *kokso-s !. 

Ai. kaksd, kaksa-h „Achselgrube, Gurtgegend der Pferde", av. kasa- m. 
,,Achsel u (erweist -ks -) ; lat. coxa „Hiifte“; air. coss f. „Fu6“, abrit. Agyev- 
r6-xo£og etwa „Wei6fuB“ (aber cymr. coes ist trotz Bezzenberger BB. 16, 246, 
Solmsen Stud. 31 Anm. 1, aus dem Lat. entlehnt, ygl. Loth Re. 18, 91, 
Foy IF. 6, 33 1 , Zupitza Gutt. 66, 104, 115); ahd. liahsa „Kniebug des Hinter- 
beins“, mhd. liehse, nhd. Hdchse, Hesse, bair. Haxn (Curtius 5 154, weitere 
Lit. bei Zupitza aaO., wo auch zur Bedeutungsfrage). Zu cech. kosinka 
„Flugel“, mahr.-rech. kosirek , kosarek „Feder am Hut" (Prusik Krok VI 
[IA. 3, 104] ; es ware ein Bed.-Yerhaltnis wie zwischen lat. ala : axilla ) siehe 
Berneker 580. 

Unter einer Gdbed. „Bug" sucht man (s. Bezzenberger BB. 12, 239, 
Wiedemann BB. 28, 15) nicht uberzeugend als ,.krumm, gebogen" auch 
russ. usw. kos* „schrag, schief", aksl. kosa „Sichel, Sense" zu ermitteln 
(so zw. auch Berneker 581 ; anders Petersson IF. 35, 269ff., AfslPh. 36, 138 : 
kom aus *qop-so- ,.xajuy.’6g“ ? ? — Ist kosa vielleicht doch zu Ices- „schneiden“ 
zu stellen?). Desgleichen lat. costa „Rippe“, aksl. kostb „Ivnochen“, serb. 
auch „Rippe". Ganz fraglich ist andrerseits Peterssons IF. aaO. An- 
kniipfung von *kok-so- unter einer Wz. kegQi)- an lit. kezojit , -oti „sachte 
einhergehen", keza „FuB“ und gar an aksl. koza „Ziege“ (*„hiipfend“) ; die 



kop(h)elo-s, kap(h)elo-s — qo fa- 


457 


Anschauung, die *koksa ursprgl. ausdriickte, ist noch vollig dunkel. Siitter- 
lin IF. 29, 129 will westf. hiage f. „die Weichen; die Linie, wo sich der 
Bauch an den Schenkel schlieBt 4 ', ahd. hega-druos , hegi-druosa f. „Hode, 
Sehamteil“, vergleichen, doch s. iiber dieses vielmehr u. kak- „mannliche 
Geschlechtsteile“. 

Yerfehlt Lewy KZ. 40,423 {*koksa- sei Redupl. von *aksa). 

kop(h)elo-s oder kap h)elo-s „Karpfenart“. 
-----ken-3
6588:(von Kretschmer KZ. 31, 466 dagegen zu *itu- „jung“ gestelltj : lit. jaw 
10016:Gr. tlaffOQ ,,Hirseh‘ - (*eln-bho-s), „junger Hirsch" ( *elnos ; gegeii 
12781:2. ieu- „jung‘\ Positiv iuw-n- f : i"ii-), Komp. ieu-ius-. 
12783:Ai. yuvan- (yuva, Gen. yancth < „jung: Jtingling", f. yum, Komp. Sup. 
12799:oac, mir. vc, cymr. mimic, bret. iuouank , acorn, iouenc , mcorn. yoivynk „jung“, 
12809:LBW b. n.juvuiis, Boisaeq s. v. , lat . juvencus, -u „junger Stier. junge Kuh, 
12811:ags. geong „jung" i'urg. *jilnga.: aus juwmigdz ; dazu ein ncuer Komp. 
16643:Gr. Yovdo; m. „junger Bart, I’laum. mit dem ersten Bart ausbrechender 
21383:junger Hund", umbr. leaf el, gen. katles „catulus“; aisl. hadna f. „junge 
25042:1. ken- „frisch hervorkommen (vielleicht eigentlich : sprieBen, hervorstechen),
```


## [2026-09-06T16:16:42.069Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; sed -n '25042,25075p' WLD_Bd1_1930_dli_70244_djvu.txt"
}
```


### [2026-09-06T16:16:42.121Z] TOOL RESULT

```
1. ken- „frisch hervorkommen (vielleicht eigentlich : sprieBen, hervorstechen), 

sich soeben einstellen, entspringen, anfangen; auch von Tierjungen 
und Kindern". 

Ai. kantna „jung", Komp. Sup. kanTyas-, kanistha -, kanisthd-, hand , 

kanyd „Hadchen", ay. kainya-, kaini , kainln ds. ; gr. y.atvog „neu, uner- 



398 


ken- 


hort“ (abweiehend von Wackernagel Verm. Beitr. 38 mit xalvv/uai „zeiehne 
mich aus“ verbunden als *y.atd-vvucu : -rog, doch s. Boisacq u. yaivvjuai; 
die ar. Worte — bis auf kann — und das gr. Wort aus dieser Basis qendi-, 
a. Brugmann IF. 17, 365f.); lat. recens ,,friscb, jung, neu" (so schon Doder- 
lein Lat. Syn. IV, 1831, 96f.) eigentlich „gerade vom Ursprung, der Ge- 
burt her" (s. auch Vf. LEWb. 2 * s. v., wo fiber andere Deutungen; unan- 
nehmbar auch Ehrlich BPhW. 1911, 1575): mir. cinim „entspringe“, cinis 
„ortus est", cinind „Geschleelit, Stamm", air. ccncl „Geschlecht", acymr. 
cenetl , ncymr. cenedl „Geschlecht, Nation" (sehr unsicher ist Pedersens 
KG. I 23 Gleichsetzung von acymr. mcymr. cein , ncymr. rain, mbret. quen, 
air. — aus dem Brit. — coin „schon“ mit gr. y.aivog; „schon“ = „jung“?); 
aksl. (trotz Wiedemann BB. 27, 193 If.) rs-, na-cMia , -ecti „anfangen", zn- 
cdi „ds.; empfangen (vom Weibei", kom „Anfang“, komcb „Ende“ (z. T. 
in neuern Slavinen auch ,,Spitze“) (d. i. „der Anfang einer Reihe vom 
andern Ende angesehen“, oder nach Berneker „Spitze"; lat. cuneus bleibt 
gegen Wiedemann BB. 27, 19S fern, s. Liden arm. St. 79, Yf. LEWb. 2 s. v. ; 
ebenso, gegen Fick III 4 15 an. hvammr ,,Winkel“'.
```


## [2026-09-06T16:16:54.481Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== IEC\"; grep -n \"^kēn\\|^kenkos\\|^koksa\\|^kok̂sā\\|koksā\" IEC.txt | head; grep -n \"kaninos\\|kanyā\\|recens\" IEC.txt | head; echo \"== LEW recens/coxa\"; grep -n \"^recens\\|^coxa\" LEW_1910.txt LAT.txt | head"
}
```


### [2026-09-06T16:16:54.555Z] TOOL RESULT

```
== IEC
== LEW recens/coxa
LAT.txt:14253:coxa, -ae f.: hanche, oa de la hanche, et par extension "cuisse",
LAT.txt:14262:coxarius (Pelag.); coxendix f.: articulation de-la hanche: ossa ex
```


## [2026-09-06T16:16:57.036Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '14253,14275p' LAT.txt; echo \"== LAT recens\"; grep -n \"recens\" LAT.txt | head -5"
}
```


### [2026-09-06T16:16:57.106Z] TOOL RESULT

```
coxa, -ae f.: hanche, oa de la hanche, et par extension "cuisse",
cf. Cela.4,37, coxas et poplites-, 4,30, coxis proxima genua sunt-, 3 0 par
analogie "angle rentrant" (Groa., Hyg.). ” Atteste k partir de Nigidius.
A reaplac 4 dans les langues roaanes femur qui n 1 eat deaeur 4 que dans
un dialecte rh 4 to-roaan, cf. M.L.3399,3340. - Panroaan; britt. coes
" j aabe 11 .
Derives: coxus,-a,-un: claudus (rare et populaire, C. Cilnius Maecenas,
Gloss.), cf.esp.cojo M.L.3393a; coxo, -Unis a. (Gloss.); coxosus id.;
coxlgo, -as id.; coxale: veteaent couvrant les haaches (rare, tardif);
coxarius (Pelag.); coxendix f.: articulation de-la hanche: ossa ex
acetabulis pernarum, circa quae coxendices uertuntur, Plin.38,49,
uertebrae in coxa(c£. c lacendlx "genus conchae") et coxendicus (Pelag.).
Le aot doit designer une articulation en g 4 n 4 ral; car les aots cor-
respondants s'appliquent a des articulations diverses: iri. coss "pied",
v.h.a . hahsa "partie de derriere de 1 1 articulation du genou", skr. kaksah
et feafejS "aisselle". - Ceci pos 4 , on est tente de rapprocher axis;
pour a/o, cf. auris; pour le k- , cf. costa,
coxendix: v. le pr 4 c 4 dent.
coxim, cossim adv.: k croppetons (rare et populaire, 3 ex. en tout:
Poap., Varr., Apul. ). Cf. incoxo, -as: Non.39,8 incoxare in coxam sidere.
Pomponius Pannuceatis (97): neque interim cacandi causa unquam incoxaui
nate. Non atteste en dehors de ce passage. Le rapprochement avec coxa
semble du k l' 4 tyaologie populaire; la racine est la meae que dans
== LAT recens
9762:distributions (par tete, 5«xm 5tecpaXr|v), les recensements (capite censi)-,
11052:rang de chacun, je fais le recensement", et censor 1., ion du magistrat
11080:recSnsed: recenser, 4 num 4 rer; passer un revue; r 4 viser; recensio
11081:(Cic.); recensitio (Dig.); recensus (Su 4 t.).
41189:piscis itidemst amator lenae: nequamst nisi recens. Est devenu une
```


## [2026-09-06T16:17:05.651Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"Cushion\\|CUSHION\" SKT.txt | head -5; echo ---; grep -n \"Heel, the hinder\\|Heel (1)\\|Recent,\" SKT.txt | head -5"
}
```


### [2026-09-06T16:17:05.704Z] TOOL RESULT

```
---
15749:pvmtjvB,  tending  to  recover.  (L.) *rativ$u,  (properly)  recoverable.  •> trart  (.above). lant ;  se«  Orvod. Atlon ;  aee  Create. minate ;  sec  Crime, dt ;  see  OreeoflDt. jigle.  Beatify.  Stc, ;  wc  Recent, nbent;  see  Covey. ;>erative ;  see  Becover. r ;  STC  OurreDt. HUlt ;  see  Cause.
```


## [2026-09-06T16:17:15.208Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"lemma: k.els\\|lemma: kʷels\\|lemma: qṷels\\|lemma: kuels\" POK_full.txt | head; grep -n \"Page(s): 639\\|Page(s):639\" POK_full.txt | head"
}
```


### [2026-09-06T16:17:15.272Z] TOOL RESULT

```
52758:Page(s): 639-640
```


## [2026-09-06T16:17:17.571Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '52720,52760p' POK_full.txt"
}
```


### [2026-09-06T16:17:17.618Z] TOOL RESULT

```
of the soil ', //7cc»/e/'e "inhabit, to be at home, abide, dwell ', incola^ an inhabitant, resident ', 
inquilTnus^ of foreign birth ', Esquiliae^ the largest of the seven hills of Rome '; about 
anculus " a man-servant ' see above; 

colus, -ust m. or -/"f. "distaff' {*k"elos^ spindle'), collus, -/"m. (Old Latin), collum, -/"n. " 
the neck, the neck (of a flask or bottle), (of the poppy), mountain ridge ' {*k"ol-so-, Gothic 
ha Is); 

Old Irish cur cart ' (Dual. *k^old); Middle Irish coir head' = 

Old Church Slavic kolou.. Gen. /ro/ese "wheel', PI. kola 'cart ' (mixture from k^olo-m. 
and k"eles-v\.)\ 

Icelclo-, k^olclo-il) "wheel' in: 

In a- grade: 

Old Indie cakra-m. n. (pronunciation secondary) " cartwheel, disc, circle ', Avestan 
caxra-m. "wheel'. 

In zero- grade: 



gr. KUKAoq " circle ', PI. kukAoi and kukAq " wheels ' 

In e- grade: 

Old Icelandic hjol, hvel {*k"ek"elon-, Germanic *hweh(w)ula-) n., Old English hweol {ev\Q\. 
wheel), besides hweowol, ^n/eo^o/ (Germanic *hweg{v\/}ula-). Middle Low German wel 
"wheel'; also Frisian fiar\s probably eine dissimilation-form for *hwewla-\ compare also 
Phrygian kIkApiv " big, giant bear ' ('cart '), Lithuanian kaklas, Latvian kokis " neck '; 
Tocharian A kukal, B kokale " cart '. 

Lengthened grade perhaps (as ' twiddled, twisted, rotated, revved, revolved, round ') 
Old Icelandic hva//an6 hollru. (latter from dem Dat. PI. holumiroxw hvalum) 'roundish hill'. 

References: WP. I 514 f., WH. I 45, 245 ff., 250, 846, Trautmann 125. 
Page(s): 639-640 

Root / lemma: lrel-2{*k''ehul-)
```


## [2026-09-06T16:17:23.646Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"kelson\\|last furrow\\|Furche des Ackers\\|k.els-\\|kars.ti\\|karsati\" POK_full.txt | head -20; echo \"---POK_02 furche\"; grep -n \"letzte Furche\" POK_02.txt POK_03.txt | head"
}
```


### [2026-09-06T16:17:23.711Z] TOOL RESULT

```
45968:Lithuanian karseti, intensiv karstu, karstT become old ', iskarsqs^ frail before age ', 
52653:s-extension in Old Indie karsu-f. "furrow, headland ', karsati, krsatr turn over, rotate 
---POK_02 furche
```


## [2026-09-06T16:17:27.028Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '52630,52665p' POK_full.txt; echo \"---page\"; awk 'NR>=52600 && NR<=52680 && /Page\\(s\\)/' POK_full.txt; grep -n \"lemma: k\" POK_full.txt | awk -F: '$1>52400 && $1<52700' | head"
}
```


### [2026-09-06T16:17:29.694Z] TOOL RESULT

```
with voiced final sound Old Church Slavic kazQ, kazaf/^s\r\o\N, urge, remind', u-kazb " a 
showing forth, exhibiting, a setting forth, exposition, proving, proof ' (also kaznb " decision, 
judgement, alignment '), probably Indo Germanic *k"eg-bes\6es *k"ek-l common Old Indie 
gh- > ks- : Slavic gh- > z-, z- 

References: WP. I 510 f., Schwyzer Gr. Gr. I 326, 519. 
Page(s): 638-639 

Root / lemma: k^'e-l {*k''ehu-) 
See also: s. unk^o- 
Page(s): 636 

Root /lemma: k^el-l, k''el9-{*k'^ehulah-) 
Meaning: to turn; wheel; neck? 
Material: 

In a- grade: 

Old Indie carati, calatT moves, walks, grazes, drives ' etc. (heavy basis in caritum, carita-, 
cTrna-, carftra-v\. "foot, leg', carcOryamana-, curtf-, also probably tuvi-kOrmf-^ energetic, 
vigorous '), lengthened grade cara-m. " way ', etc.; Avestan caraiti^ versatur, obliegt einer 
Tatigkeit ' etc., carana-^i\e\6\ Old pers. parikara^cuWSyaieY; 

s-extension in Old Indie karsu-f. "furrow, headland ', karsati, krsatr turn over, rotate 
something, plow ', Avestan karsa-m. n. "furrow', karsa/t/"r\6ge, mark with ridges '; 



Tocharian A kallas^ brings ', preterit sel, PI. /ra/5/'(Pedersen Tocliar. 183). 

In e- grade: 

alb. sjel, sjeir turn round, twist, turn over, bring' {*k"'el-)\ besides A/e/"bring, bear' 
{*k"'oleid), a-sur willow ', sule " boat ', (Note: Occidental (western) Romance languages 
prefix e-, a-), per-kul, perku/'bend, curve ' ( *k"'e/-n-), kulp, kulper, kulpra " forest shoot 
'(*A-V-bh-); 
---page
Page(s): 638 
Page(s): 638-639 
Page(s): 636 
52439:Root / lemma: k''ei-1(t){*k''ehu-tj Note: common Proto Germanic -u- > -u-, -y-, -/-. 
52551:Root / lemma: k''ei-2{*k''ehu-) Note: common Proto Germanic -u- > -u-, -y-, -/-. 
52638:Root / lemma: k^'e-l {*k''ehu-) 
52642:Root /lemma: k^el-l, k''el9-{*k'^ehulah-)
```


## [2026-09-06T16:17:41.113Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== PLA kaskul\"; grep -n -i \"kaskul\\|kaškūl\\|كشكول\" incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head; echo \"== AFM\"; grep -n \"كشكول\\|الكشكول\" AFM.txt | head; echo \"== BQT v1 tarkash\"; grep -n \"ترکش\" BQT_v1_pages.txt | head"
}
```


### [2026-09-06T16:17:41.187Z] TOOL RESULT

```
== PLA kaskul
== AFM
5523:( الكشسكول) قدح اللَكَّدَي يجمع فيه 3 2 كشكول وهو رك من 
== BQT v1 tarkash
```


## [2026-09-06T16:17:44.512Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '5518,5530p' AFM.txt; echo \"--- page tag\"; awk 'NR>=5400 && NR<=5530 && /pdf page/ {print NR\": \"$0}' AFM_pages.txt 2>/dev/null | tail -3; grep -n \"الكشسكول\\|كشكول\" AFM_pages.txt | head"
}
```


### [2026-09-06T16:17:47.012Z] TOOL RESULT

```
ܐ الدياثة 10:52 9 كفيكان 
وهو الديوث 

+ ( )ܥܰܪܶܐ ) فاسي محض وهو ماء الشعير الطبوخ 

( الكشسكول) قدح اللَكَّدَي يجمع فيه 3 2 كشكول وهو رك من 


ܥ 9)\ ( 


س ܕܨ ܙ لب 

--- page tag
3462:( الكشسكول) قدح اللَكَّدَي يجمع فيه 3 2 كشكول وهو رك من
```


## [2026-09-06T16:17:52.840Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR<=3462 && /pdf page/ {p=$0} END{print p}' AFM_pages.txt; sed -n '3458,3470p' AFM_pages.txt"
}
```


### [2026-09-06T16:17:54.660Z] TOOL RESULT

```
دكش ) 0 رقعة الشطرنج فارسيّة اضلها كشت أي 0)
ܐ الدياثة 10:52 9 كفيكان
وهو الديوث
+ ( )ܥܰܪܶܐ ) فاسي محض وهو ماء الشعير الطبوخ
( الكشسكول) قدح اللَكَّدَي يجمع فيه 3 2 كشكول وهو رك من
ܥ 9)\ (س ܕܨ ܙ لب
053 3 1090 اى :كتف أورفن ܐ المحتمل ان تكون ارام يل <
من ܪܫܦ اي جمّع ومن ‫
ܝ ` 0 4
(5063 0:1008 5 او بدت الصيف 7 1 نه ܨ ال لحرة
لضيقة اللقيرة وتطلق ايضاً على الشتاء وعلى عش الطائر
0 الكرستّه فارسيّتها كته ٠‏ واظن ان الكرسنة لغة فيها
١‏ 31 ) تعر يب ܐ“ وهو ارا 1 | ܨ الذقيق والحليب 1
```


## [2026-09-06T16:18:09.565Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"^ken-\\|^kens-\\|^koks-\\|^kek-\\|kok̑s\\|COXA\\|CUSHION\\|CUISSE\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-06T16:18:09.609Z] TOOL RESULT

```
642:h. Anglo-Norman aloper, to run away from one’s hus- band with a lover: ELOPE. kneigwh-. To lean on. 1. Latin cdnivére (< *con-niguére; com-, together; see kom), “to lean together” (said of eyelids), to close the eyes, be indulgent: CONNIVE. 2. Suf- fixed zero-grade form *knigvh-to- in Latin nictdre, to move the eyelids, wink: NICTITATE. 3. Uncertain preform in Latin niti, to lean forward, strive: NISUS; RENITENT. [Pok. knei-geh- 608.] knid-. Egg of a louse. Suffixed form *knid-d in Germanic *hnito in Old English hnitu, egg of a louse: NIT. [Pok. knid- 608.] ko-. Stem of demonstrative pronoun meaning “this.” I. Variant form *ki-. 1. Germanic *hi- in: a. Old English he, he: HE!; b. Old English him, him: HIM; c. Old English his, his: 1s; d. Old English hire, her: HER; e. Old English Ait, it: 1r. f. Old English hér, here: HERE; g. Old English heonane, heonon, from here: HENCE. 2. Suffixed form “ki-tro- in Germanic *hi-thra- in Old English hider, hither: HITHER. 3. Suffixed form *ki-s in Latin cis, on this side of: cis-. II. Variant form *ke-. 1. Preposed in *ke-etero- (*e-tero-, a second time, again; see i-) in Latin céterus (neuter plural cétera), the other part, that which remains: ET CETERA. 2. Latin -ce (see nu-). III. Attrib- uted by some to this root (but more likely of obscure origin) is Germanic root *hind-, behind. 1. Old English bihindan, in the rear, behind (bi, at; see ambhi): BE- HIND, HIND!. 2. Old High German hintar (> German hinter-), behind: HINTERLAND. 3. Germanic derivative verb *hindron, to keep back, in Old English hindrian, to check, hinder: HINDER}. [Pok. ko- 609.] k6-. To sharpen, whet. Contracted from *koo-. 1. Suffixed extended form “kooi-no- in Germanic *haind in Old English hdn, stone: HONE!. 2. Perhaps Greek kénos, cone, conical object (< “a sharp-pointed object”): CONE. [Pok. Aéi- 541.] kob-. To suit, fit, succeed. Germanic *hap- in Old Norse happ, chance, good luck: HAP, (HAPPEN), (HAPPY); (HAP- LEss), (MISHAP). [Pok. kob- 610.] [kokkos. Kermes berry, pit, grain. Greek noun of un- known origin: COCCID, COCCUS, COCHINEAL; MONO- COQUE.] koksa. Body part. Latin coxa, hip: Coxa, CUISSE, CUSH- ION. [Pok. koksd 611.] kolem-. Grass, reed. Suffixed form *kolsm-o-. 1. Ger- manic “*halmaz in Old English healm, halm, straw: HAULM. 2. Latin cudmus, stalk: CULM!. 3. Zero-grade form “kibpm-o- in Greek kalamos, a reed, straw: CALA- MITE, CALAMUS, CALUMET, CARAMEL, SHAWM. [Pok. kolomo-s 612.] koli-. Glue. Suffixed variant form *koly-a in Greek kolla, glue: COLLAGE, COLLO-, COLLODION; PROTOCOL. [Pok. Rolfeji- 612.] kom. Beside, near, by, with. 1. Germanic *ga-, together, with (collective and intensive prefix and marker of the past participle), in Old English ge-, with, also participial, collective, and intensive prefix: ENOUGH, HANDIWORK, YCLEPT. 2. Latin cum, co-, with: CUM; CONQUIAN. 3. Old Latin com, with (collective and intensive prefix): co-, com-. 4, Suffixed form *kom-trd in Latin contra, against, opposite: (CON!), CONTRA-, CONTRARY, (COUNTER!), COUNTER-, COUNTRY; ENCOUNTER. 5. Suffixed form *kom-yo- in Greek koinos, common, shared: COENO-; CENOBITE, EPICENE, KOINE. 6. Reduced form *ko- (see gher-', mei-', smei-). [Pok. kom 612.] konemo-. Shinbone, bone, Reduced form *kemmo- per- haps in Germanic *hamma in Old English hamm, ham, thigh: HAM. [Pok. konamo- 613.] konk-. To hang. 1. Germanic *hanhan in: a. Old English hon, to hang: HANG; b. Dutch (dialectal) hankeren, to long for; HANKER; ¢C. possibly Middle English he(e)ng, hinge, hinge (ultimately from the base of Old English hangian, to hang): HINGE. 2. Suffixed form *konk-t-d- in
1402:CUBE keu-2 CUBICLE keu-2 CUBIT keu-2 CUCKING STOOL kakka- CUD gWet-1 CUDGEL ku- CUESTA kost- CUIRASS sker-1 CUISINE pekw- CUISSE koksa CULET (s)keu- CULINARY pekw- CULLET kwel-1 CULLIS kagh- CULM! kolem- CULMINATE kel-6 CULOTTES (s)keu- CULT kWel-1 CULTIVATE kwel-1 CULTRATE skel-1 CULTURE kvel-1 CULVER kel-5 cum kom CUMMERBUND bhendh-, kamer- CUMULATE keue-2 CUMULUS keue-2 CUNCTATION konk- CUNNILINGUS leigh-, (s)keu- CUNNING gné- CUNT ku-
1404:CUPID kwép- CUPIDITY kwép- CUPOLA keu-2 CUPULE keu-2 CUR gere-2 CURATE cura CURATOR cira CURB sker-3 CURD greut- CURE cira CURETTE cira CURIA wWi-ro- CURIO cira CURIOUS cira CURL ger-2 CURRENT kers-2 CURRIER sker-1, CURSIVE kers-2 CURSOR kers-2 CURT sker-1 CURTAL sker-1 CURTILAGE gher-1 cuRTSY gher-* CURULE kers-2 CURVATURE sker-3 CURVE sker-3 CURVET sker-3 CUSHION koksa
```


## [2026-09-06T16:18:19.118Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -o \"RECENT [a-zA-Z0-9ʷᵉ*-]*\" AHD_watkins1985.txt | head; echo \"---\"; grep -no \"ken-. To be born[^.]*\\.\\|ken-\\. Fresh[^.]*\\.\" AHD_watkins1985.txt | head; grep -c \"\" AHD_watkins1985.txt; grep -on \"ken-[0-9]*\\. [A-Z][a-z]*\" AHD_watkins1985.txt | head"
}
```


### [2026-09-06T16:18:19.193Z] TOOL RESULT

```
RECENT ken-3
---
2463
608:ken-2. Hypothetical
```


## [2026-09-06T16:18:21.488Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '608,612p' AHD_watkins1985.txt | fold -w 200 | grep -n -A3 \"ken-3\""
}
```


### [2026-09-06T16:18:21.545Z] TOOL RESULT

```
15:man notten, to nod, perhaps akin to Middle English nodden, to nod: Nop. [Pok. 2. ken- 559.] ken-3, Fresh, new, young. 1. Suffixed form *ken-t- in Latin recens, young, fresh, new (re-, again; see re-):
16- RECENT. 2. Suffixed zero-grade form kn-yo- in Greek kainos, new, fresh (> kainotés, newness): -CENE; CAINO- TOPHOBIA, CENOGENESIS, CENOZOIC, KAINITE. [Pok. 3. ken- 563.] ken-4, Empty. Suffixed form 
17-*ken-wo- in Greek kenos (< *kenwos), empty: KENOSIS; CENOTAPH. [Pok. ken- 564.] ken-5, Hypothetical base of several roots associated with the notions “to compress,” “something compressed.” 1. 
18-Germanic root *hnekk-, “neck” (a narrow or com- pressed part), in: a. Old English hnecca, neck: NECK; b. Old Norse hnakkur, saddle, and Old Norse hnakki, back of the neck, perhaps akin to the sour
```


## [2026-09-06T16:18:40.157Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '1,120p' tools/verify_check.py"
}
```


### [2026-09-06T16:18:40.196Z] TOOL RESULT

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


## [2026-09-06T16:18:45.846Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg254.png data/verification/sources/refs/ocr/BOOK/254.png && ls -la data/verification/sources/refs/ocr/BOOK/254.png"
}
```


### [2026-09-06T16:18:45.910Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 71025 Sep  6 12:18 data/verification/sources/refs/ocr/BOOK/254.png
```


## [2026-09-06T16:26:16.956Z] TOOL CALL #79: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/page-254.json",
 "content": "{\n \"pdf_page\": 254,\n \"book_page\": 224,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-06\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Ken\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *ken- 'fresh, new, young; to appear, be born' (Pokorny IEW 563-564 'ken-3'; Walde-Pokorny I 397 f. '1. ken-'; Watkins/AHD 'ken-3')\",\n   \"note\": \"Pokorny's entry on the page Nourai cites is headed 'ken-3, Meaning: to appear, be born; to begin; young', and its material is exactly the two branches Nourai draws: 'Old Indic kanína- \\\"young\\\" ... kanyā. Gen. Pl. kanīnām \\\"girl\\\", Avestan kaine, kainī-, kainīn- ds.' and 'Latin recens \\\"fresh, young, new\\\", actually \\\"lately arisen\\\"'. Watkins heads the same root 'ken-3. Fresh, new, young. 1. Suffixed form *ken-t- in Latin recens ... (re-, again) : RECENT'. So the language label (Indo-European), the shape of the root (Ken = *ken-) and the gloss 'young, fresh' are all correct, and both daughters on the chart belong to it. Only one form on the chart is wrong: the Avestan 'kaimyâ' in node 1, which is a misprint for kainyâ (Av. kainyā-). Everything else on this entry is textbook Iranian and Latin etymology and is supported by Horn 194, Bartholomae, MacKenzie, Nyberg, Gharib and Mo'in's footnote in Borhan-e Qate' 1715.\",\n   \"note_fa\": \"جعبهٔ ریشه درست است. پوکورنی در صفحهٔ ۵۶۳ فرهنگ خود مدخل «ken-3» را با معنای «پدیدآمدن، زاده‌شدن؛ آغازیدن؛ جوان» آورده و همان‌جا دو شاخه‌ای را که نورایی رسم کرده گرد هم نهاده است: از سویی سنسکریت kanína- «جوان»، kanyā «دختر» و اوستایی kaine, kainī-, kainīn-، و از سوی دیگر لاتین recens «تازه، جوان، نو». واتکینز (پیوست AHD) نیز همین ریشه را «ken-3: تازه، نو، جوان» می‌نامد و recens را به صورت re- + *ken-t- تحلیل می‌کند، درست همان‌گونه که نورایی «re-cens» نوشته است. پس برچسب «هندواروپایی»، صورت ریشه و معنای «جوان، تازه» هر سه پذیرفتنی است. تنها لغزش این مدخل صورت «kaimyâ» در گرهٔ ۱ است که غلط چاپی کتاب به‌جای kainyâ (اوستایی kainyā-) است.\",\n   \"sources\": [\n    \"https://en.wiktionary.org/wiki/%DA%A9%D9%86%DB%8C%D8%B2\"\n   ],\n   \"ref_check\": [\n    {\n     \"ref\": \"POK:563\",\n     \"status\": \"supports\",\n     \"note\": \"POK_full.txt line 45686 ff. (block ending 'Page(s): 563-564'): 'Root / lemma: ken-3 | Meaning: to appear, be born; to begin; young | Material: Old Indic kanína- \\\"young\\\", compounds Sup. kanīyas-, kanistha-, kanyā. Gen. Pl. kanīnām (older n-stem) \\\"girl\\\", Avestan kaine, kainī-, kainīn- ds.; gr. kainós \\\"fresh, egregious\\\"; Latin recens \\\"fresh, young, new\\\"'. The page Nourai cites is precisely this entry.\"\n    }\n   ],\n   \"consulted\": [\n    {\n     \"src\": \"WLD\",\n     \"where\": \"Bd. I 397 f. (WLD_Bd1 djvu line 25042, headword '1. ken-')\",\n     \"stance\": \"supports\",\n     \"note\": \"'1. ken- „frisch hervorkommen (vielleicht eigentlich: sprießen, hervorstechen), sich soeben einstellen, entspringen, anfangen; auch von Tierjungen und Kindern\\\". Ai. kanína „jung\\\" ... kanā, kanyā „Mädchen\\\", av. kainya-, kainī, kainīn ds.; gr. kainós „neu\\\"; lat. recens „frisch, jung, neu\\\"'. This is the source Pokorny 563 abridges — and it prints the Avestan as kainya-, which settles the 'kaimyâ' misprint.\"\n    },\n    {\n     \"src\": \"AHD\",\n     \"where\": \"Watkins 1985, k-list (AHD_watkins1985.txt line 608)\",\n     \"stance\": \"supports\",\n     \"note\": \"'ken-3. Fresh, new, young. 1. Suffixed form *ken-t- in Latin recens, young, fresh, new (re-, again; see re-): RECENT. 2. Suffixed zero-grade form *kn̥-yo- in Greek kainos, new, fresh. [Pok. 3. ken- 563.]'\"\n    },\n    {\n     \"src\": \"SYN\",\n     \"where\": \"Buck §2.26 'GIRL' (SYN.txt line 2404 ff., comparative table)\",\n     \"stance\": \"supports\",\n     \"note\": \"Buck's table for 'girl' lists 'Skt. bālā-, kumārī-, kanyā-' and 'Av. kainyā' as the ordinary words — i.e. the Indo-Iranian kanyā/kainyā family is the standard word for 'girl', as the chart assumes.\"\n    },\n    {\n     \"src\": \"KLN\",\n     \"where\": \"p.1330 s.v. 'recent' (KLN_1966.txt line 31893)\",\n     \"stance\": \"supports\",\n     \"note\": \"'recent, adj. — MF. (= F.) récent, fr. L. recentem, acc. of recens, \\\"new, fresh\\\", which is formed fr. re- and I.-E. base *qen-, whence also OI. kanīnah, \\\"young\\\", kanā, kanyā, \\\"girl\\\", Gk. kainós ... \\\"new\\\"'. Klein's *qen- is the same root written in his notation.\"\n    }\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Avestan\",\n     \"words\": \"kan 2, kaine, kainîn, kaimyâ : young girl; kan-yâ, kain-ika : small woman\",\n     \"verdict\": \"transcription_suspect\",\n     \"derivation\": \"Avestan has a whole cluster of forms of this root for 'girl, maiden': kanyā- / kainyā- (Skt. kanyā-), kainī- (whence the vocative/nom. kaine of the Vidēvdād passages), the n-stem kainīn- and the diminutive kainikā-, all from PIE *ken- 'young, fresh' with the *-yo-/-ien- and *-ko- suffixes; Bartholomae's Wörterbuch cites them from V.15.9-13, Yt.5.87, Yt.17.54 etc., and Nyberg gives the columns (Av. 439). Four of the five forms on the chart are right: kaine = kainī-, kainîn = kainīn-, kan-yâ = kanyā-, kain-ika = kainikā-. 'kan 2' is Nourai's own cross-reference label for the root-stem kan-, not an attested Avestan noun by itself. But 'kaimyâ' is not an Avestan word and cannot be one: the printed page (see PNG) really does read 'kaimyâ', so the extraction is faithful and the fault lies with the book — Walde-Pokorny I 397 prints 'av. kainya-', and m for n is a straightforward typesetting slip in Nourai's own text.\",\n     \"derivation_fa\": \"در اوستا خوشه‌ای از صورت‌های این ریشه به معنای «دختر، دوشیزه» هست: kanyā-/kainyā- (سنسکریت kanyā-)، kainī- (که صورت ندایی/فاعلی آن kaine است)، ستاک نونی kainīn- و مصغّر kainikā-؛ همه از هندواروپایی آغازین *ken- «جوان، تازه» با پسوندهای *-yo-، *-ien- و *-ko-. بارتولمه این صورت‌ها را از وندیداد ۱۵٫۹ و یشت ۵٫۸۷ و ۱۷٫۵۴ شاهد آورده و نیبرگ نیز ستون ۴۳۹ او را ارجاع داده است. چهار صورت از پنج صورت نمودار درست است، ولی «kaimyâ» در اوستایی وجود ندارد؛ تصویر صفحهٔ چاپی نشان می‌دهد که خودِ کتاب «kaimyâ» چاپ کرده است، پس خطای خوانش اسکن نیست بلکه غلط چاپی کتاب است و صورت درست kainyâ (اوستایی kainyā-) است، چنان‌که والده-پوکورنی (جلد ۱ ص ۳۹۷) «av. kainya-» آورده. «kan 2» نیز نام ارجاعی خود نورایی برای ستاک kan- است نه واژه‌ای مستقل.\",\n     \"error_in\": \"book\",\n     \"book_prints\": \"kaimyâ\",\n     \"correct_form\": \"kainyâ\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\n       \"ref\": \"POK:563\",\n       \"status\": \"supports\",\n       \"note\": \"POK_full.txt (block 'Page(s): 563-564'): 'Avestan kaine, kainī-, kainīn- ds.' — Pokorny lists exactly kaine / kainīn, and the Indic kanyā beside them.\"\n      },\n      {\n       \"ref\": \"SOD:190\",\n       \"status\": \"supports\",\n       \"note\": \"Gharib, Sogdian Dictionary, entries 4750-4756 (SOD_pages.txt leaf 255 ≈ printed p.189/190): '4750 knc M kanc (qnc) <Av. kainika ->knc'k' and '4752 knc'k S kance (qncq, qnck/cyy) <Av. kainya-, kainika; MP knyg'. Gharib himself derives the Sogdian words from the Avestan forms of this node — so the citation covers the Avestan box as well as the Sogdian one.\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"BRT\",\n       \"where\": \"Altiranisches Wörterbuch, s.v. kaine / kainīn- (BRT.txt lines 2533, 2561, 4489, 8478, 10090)\",\n       \"stance\": \"supports\",\n       \"note\": \"'yeziča vaocāt aēšō nā hanąm .. pərəsaŋuha — ā aēša yō kaine hanąm .. pərəsaiti' (V.15.13 f.), 'mā .. kaine .. tarō daxštəm pārayāt' (V.15.9), 'yōi kainina °taē masyanąm \\\"Mädchen, die noch nicht reif sind für Männer\\\"' (Yt.17.55): Bartholomae's citations show kaine and the plural kainina in exactly the sense 'girl, maiden'.\"\n      },\n      {\n       \"src\": \"WLD\",\n       \"where\": \"Bd. I 397 (WLD_Bd1 djvu line 25046)\",\n       \"stance\": \"partial\",\n       \"note\": \"'ai. kanína „jung\\\" ... kanā, kanyā „Mädchen\\\", av. kainya-, kainī, kainīn ds.' — supports the derivation but prints kainya-, not the chart's 'kaimyâ'.\"\n      },\n      {\n       \"src\": \"NYB\",\n       \"where\": \"Manual of Pahlavi II, s.v. kanik (NYB_vol2_glossary.txt line 2204) and the Avestan index (line 5202)\",\n       \"stance\": \"supports\",\n       \"note\": \"'kanik [knyk] virgin, maid ... — Av. (439) kainyā-, kainī-; MPrthPrs knyg; Paz. kanik'; the index entry reads 'kainyā-, kainī: kanik'. Nyberg's Avestan starting point is kainyā-, again confirming that the chart's 'kaimyâ' should be kainyâ.\"\n      }\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Pahlavi\",\n     \"words\": \"kanik : young girl; kaničak : young girl\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Middle Persian kanīg (written knyk') 'girl, maid' continues Old Iranian *kanī-kā- (Av. kainikā-), with the regular Middle Persian loss of the final syllable and voicing of intervocalic -k- to -g- in the Book-Pahlavi reading; the diminutive kanīzag (knyck', Manichaean knycg) is built on it with the productive Middle Persian diminutive -ag added to a stem kanīz- < *kanī-čī- / *kanī-čaka-, the č being the palatalisation of the diminutive *-ka- before a front vowel. The older transliteration of knyck' as 'kaničak' (so Horn, and the Pazand tradition) is what Nourai prints; MacKenzie reads the same spelling as kanīzag, which is simply a later reading convention for the same word, and the two are not different lexemes. Both meanings on the chart, 'young girl', are right.\",\n     \"derivation_fa\": \"فارسی میانه kanīg (نوشتهٔ knyk') «دختر، کنیز» دنبالهٔ ایرانی باستان *kanī-kā- (اوستایی kainikā-) است؛ هجای پایانی افتاده و -k- میان‌واکه‌ای در خوانش پهلوی به -g- نرم شده است. صورت مصغّر kanīzag (knyck'، مانوی knycg) با پسوند تصغیر -ag بر همان ستاک ساخته شده و č آن دگرگونی پسوند تصغیر *-ka- پیش از واکهٔ پیشین است. آنچه نورایی «kaničak» نوشته همان خوانش کهن‌تر و پازندی همین املاست (هرن نیز kanīčak/kanīžak آورده) و مکنزی آن را kanīzag می‌خواند؛ این دو واژهٔ جدا نیستند. هر دو معنای نمودار درست است.\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\n       \"ref\": \"HRN:194\",\n       \"status\": \"supports\",\n       \"note\": \"Horn, Grundriss p.194 no. 870 (HRN.txt leaf 216): 'kenīz \\\"Jungfrau, Mädchen\\\", kenīzek. aw. kanyā-, kainīn-, kainikā- \\\"Jungfrau, Mädchen\\\"; phlv. kanīk, phlv. pāz. kanīčak bezw. kanīžak, kanīzak (PPGl.); ai. kanyā-, kanīnā-.' Horn gives Nourai's Pahlavi forms verbatim, kanīk and kanīčak, and derives them from the Avestan words of node 1.\"\n      },\n      {\n       \"ref\": \"FSF:275\",\n       \"status\": \"not_found\",\n       \"note\": \"Noushin's Vazhe-namak is on disk as FSF_pages.txt (479 leaves) but the pagination of this scan does not match Nourai's: کنیزک stands on leaf 371, whose printed number reads ۳۹۹, whereas leaf ~247 (≈ printed 275) is in a quite different alphabetical stretch. So this is evidently a different printing; the کنیزک article itself is there ('کنیزک [دختر شاه] ... -۲ به‌معنی برده', leaf 371) and is a Shahnameh word-list entry, not an etymological statement.\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"PHD\",\n       \"where\": \"MacKenzie, Concise Pahlavi Dictionary p.49 s.v. kanig / kanizag (PHD.txt line 424)\",\n       \"stance\": \"supports\",\n       \"note\": \"'kanig [knyk' | M knyg] girl, maid. kanizag [knyck' | M knycg, N kaniz(ak)] = kanig.' MacKenzie explicitly makes the second word the source of New Persian kanīz(ak).\"\n      },\n      {\n       \"src\": \"NYB\",\n       \"where\": \"Nyberg, Manual of Pahlavi II, s.vv. kanik and kanicak (NYB_vol2_glossary.txt lines 2199, 2204)\",\n       \"stance\": \"supports\",\n       \"note\": \"'kanik [knyk] virgin, maid ... Av. (439) kainyā-, kainī-; MPrthPrs knyg; Paz. kanik' and 'kanicak ... — MPrs knycg; NP kanizah. Dimin. of kanik'. Nyberg's 'Dimin. of kanik' is exactly the relation the chart draws between its two Pahlavi words.\"\n      }\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Persian\",\n     \"words\": \"kanîz «کنیز» : maid (also کنیزک)\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"New Persian کنیز kanīz 'slave-girl, maid' and its diminutive کنیزک kanīzak are the direct continuation of Middle Persian kanīzag: Middle Persian final -ag regularly gives New Persian -a(h)/-ak, so knyck' > kanīzak, from which the shortened kanīz was back-formed (the same pair as Pahlavi ābādag > NP ābād/ābāda). Mo'in's footnote in Borhan-e Qate' takes the word back through Pahlavi to Avestan kanyā-, kainīn-, kainikā- 'young girl' and analyses it as کن (woman) + یز (diminutive suffix); Wiktionary likewise gives 'کنیز, variant of کنیزک, from Middle Persian knyck' /kanīzag/, diminutive of knyk' /kanīg/ \\\"maid\\\", from Proto-Iranian *kanyáH \\\"small girl; maiden\\\", cognate with Sanskrit कन्या (kanyā)'. The semantic step 'girl' > 'female servant, slave-girl' happened already in Middle Persian and is the ordinary meaning in classical New Persian. The gloss 'maid' is exact.\",\n     \"derivation_fa\": \"«کنیز» و مصغّر آن «کنیزک» بازماندهٔ مستقیم فارسی میانهٔ kanīzag است: پایانهٔ -ag فارسی میانه در فارسی نو به -ک/-ه بدل می‌شود، پس knyck' > کنیزک، و از آن صورت کوتاه‌شدهٔ «کنیز» ساخته شده است (همان جفتی که در ābādag > آباد/آباده می‌بینیم). معین در حاشیهٔ برهان قاطع (ص ۱۷۱۵) واژه را از راه پهلوی به اوستایی kanyā-, kainīn-, kainikā- «دختر جوان» می‌رساند و آن را «کن (زن) + یز (پسوند تصغیر)» تحلیل می‌کند و به هوبشمان ارجاع می‌دهد؛ ویکی‌واژه نیز آن را گونهٔ «کنیزک» از فارسی میانهٔ kanīzag، مصغّر kanīg، از ایرانی آغازین *kanyáH و هم‌ریشه با سنسکریت kanyā می‌داند. تحول معنایی «دختر» ← «خدمتکار زن، کنیز» در همان دورهٔ میانه رخ داده است. ادعای نورایی درست است.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/%DA%A9%D9%86%DB%8C%D8%B2\"\n     ],\n     \"ref_check\": [\n      {\n       \"ref\": \"BQT:1715\",\n       \"status\": \"supports\",\n       \"note\": \"Borhan-e Qate' ed. Mo'in p.1715 = BQT_v3_pages.txt pdf page 508: headword 'کنیز - بفتح اول بروزن تمیز، معروف است که پرستار و خدمتگار زنان باشد و بعربی جاریه خوانند' with Mo'in's footnote 4: 'اوستا kanya_, kainin_, kainika_ (دختر جوان). پهلوی ... و این کلمه مرکب است از: کن (زن) + یز (پسوند تصغیر) ... قس: کنیزک (پهلوی، پازند kanicak) «اسئق - هوبشمان ۸۷»'. Nourai's page number is exact and the footnote states his arrow.\"\n      },\n      {\n       \"ref\": \"HRN:174\",\n       \"status\": \"not_found\",\n       \"note\": \"Horn p.174 (HRN.txt leaf 195) is nos. 785-786, 'seyāl \\\"Schakal\\\"' and 'sikār \\\"Jagd\\\"' — nothing to do with kanīz. The Horn passage Nourai wants is p.194 no. 870, which he cites correctly on the Pahlavi node; 174 looks like a digit transposition of 194.\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"HRN\",\n       \"where\": \"Grundriss p.194 no. 870 (HRN.txt leaf 216)\",\n       \"stance\": \"supports\",\n       \"note\": \"'870. kenīz \\\"Jungfrau, Mädchen\\\", kenīzek ... phlv. kanīk, phlv. pāz. kanīčak bezw. kanīžak, kanīzak' — Horn's headword is the New Persian word and both the simplex and the diminutive of the chart.\"\n      },\n      {\n       \"src\": \"PHD\",\n       \"where\": \"MacKenzie p.49 (PHD.txt line 424)\",\n       \"stance\": \"supports\",\n       \"note\": \"'kanizag [knyck' | M knycg, N kaniz(ak)]' — MacKenzie's own equation of the Pahlavi word with New Persian kanīz(ak).\"\n      },\n      {\n       \"src\": \"HUB\",\n       \"where\": \"Hübschmann, Persische Studien (HUB.txt, grep 'kaniz', 'kanik')\",\n       \"stance\": \"silent\",\n       \"note\": \"The OCR of Hübschmann yields no hit for either spelling; Mo'in's footnote cites 'هوبشمان ۸۷' for this word, but that page could not be located in the scan, so Hübschmann is recorded as silent here rather than as support.\"\n      }\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"Sogdian\",\n     \"words\": \"knc : girl; knc`k : young girl\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Sogdian knc (kanc, also spelt qnc) 'girl' and its diminutive knc'k (kancē, also qncq, qnck/cyy) 'small girl, child' are the Sogdian members of the same Old Iranian family: *kanyā- gives Sogdian kanc with the regular Sogdian development of *-ny- to -nc-, and knc'k adds the Sogdian diminutive -'k (< *-aka-), the exact counterpart of Middle Persian kanīzag. Gharib's dictionary derives the words from the Avestan forms of node 1 and equates them with Middle Persian knyg, so the arrow from the Avestan box to the Sogdian box is drawn as the standard handbook draws it. The chart's glosses ('girl' / 'young girl') match Gharib's ('girl' / 'small girl, child').\",\n     \"derivation_fa\": \"واژه‌های سغدی knc (kanc، به املای مانوی qnc) «دختر» و مصغّر آن knc'k (kancē) «دخترک، کودک» اعضای سغدی همین خانوادهٔ ایرانی باستان‌اند: *kanyā- در سغدی با تحول قاعده‌مند *-ny- > -nc- به kanc بدل شده و knc'k پسوند تصغیر سغدی -'k (< *-aka-) را بر آن افزوده است — درست همتای kanīzag فارسی میانه. قریب (فرهنگ سغدی، مدخل‌های ۴۷۵۰ و ۴۷۵۲) خود این واژه‌ها را از صورت‌های اوستایی همین گره می‌گیرد و با knyg فارسی میانه برابر می‌نهد؛ پس پیکان نمودار از جعبهٔ اوستایی به سغدی همان است که کتاب‌های مرجع می‌کشند. ادعای نورایی درست است.\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\n       \"ref\": \"SOD:190\",\n       \"status\": \"supports\",\n       \"note\": \"Gharib, Sogdian-Persian-English Dictionary, entries 4750-4756 (SOD_pages.txt leaf 255, printed p.189/190 by the file's offset 'printed ≈ leaf − 66'): '4750 knc M kanc (qnc) <Av. kainika ->knc'k ... GMS 247'; '4752 knc'k S kance (qncq, qnck/cyy) <Av. kainya-, kainika; MP knyg ... small girl, child'; '4755 kncyk M kancik =>knc'k ... girl'. Both chart words, both glosses and the Avestan parentage are in the cited pages.\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"SOD\",\n       \"where\": \"entries 4750, 4752, 4755, 4756 (SOD_pages.txt lines 17283-17302)\",\n       \"stance\": \"supports\",\n       \"note\": \"Beside the two chart words the same column has '4756 qncystr C kancistar — younger girl', a comparative built on the same stem, which confirms that kanc is a live Sogdian noun and not a ghost form.\"\n      },\n      {\n       \"src\": \"NYB\",\n       \"where\": \"Manual of Pahlavi II s.v. kanik (NYB_vol2_glossary.txt line 2204)\",\n       \"stance\": \"partial\",\n       \"note\": \"'MPrthPrs knyg' — Nyberg records the Middle Persian/Parthian side of the same word that Gharib equates with Sogdian knc'k; he does not treat Sogdian itself.\"\n      }\n     ]\n    },\n    {\n     \"id\": 5,\n     \"lang\": \"Latin\",\n     \"words\": \"re-cens : fresh, new\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Latin recēns, gen. recentis 'fresh, young, new' is analysed by Watkins as re- 'again' + a suffixed *ken-t- of this root, i.e. literally '(having) just arisen', which is what Pokorny too says ('actually \\\"lately arisen, not long in existence\\\"'). Klein gives the same base for the word and the same cognates that stand in the Avestan box (OI. kanīnah 'young', kanyā 'girl'). Nourai's hyphenated spelling 're-cens' is therefore not a typographic accident but the correct morphological cut, and the gloss 'fresh, new' is the dictionary gloss. The word is attested from Plautus and Cato on and yields the Late Latin verb recentāre, whence also French rincer and English rinse.\",\n     \"derivation_fa\": \"لاتین recēns (اضافی recentis) «تازه، جوان، نو» را واتکینز به re- «باز، دوباره» + صورت پسونددار *ken-t- از همین ریشه تحلیل می‌کند، یعنی تحت‌اللفظ «تازه‌برآمده»؛ پوکورنی نیز همین را می‌گوید («eigentlich: gerade vom Ursprung, der Geburt her»). کلاین همان ریشه و همان هم‌ریشه‌هایی را می‌آورد که در جعبهٔ اوستایی این نمودار آمده است (سنسکریت kanīnah «جوان»، kanyā «دختر»). پس نگارش «re-cens» در کتاب نه خطای چاپی بلکه برش درست تکواژی است و معنای «تازه، نو» همان معنای فرهنگ‌هاست. ادعای نورایی درست است.\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\n       \"ref\": \"POK:563\",\n       \"status\": \"supports\",\n       \"note\": \"POK_full.txt (block 'Page(s): 563-564'): 'Latin recens \\\"fresh, young, new\\\", actually \\\"lately arisen, not long in existence, fresh, young, recent\\\"' — the Latin word is listed on the very page Nourai cites.\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"AHD\",\n       \"where\": \"Watkins 1985, s.v. ken-3 (AHD_watkins1985.txt line 608)\",\n       \"stance\": \"supports\",\n       \"note\": \"'1. Suffixed form *ken-t- in Latin recens, young, fresh, new (re-, again; see re-): RECENT.' — the same segmentation as the chart's 're-cens'.\"\n      },\n      {\n       \"src\": \"KLN\",\n       \"where\": \"p.1330 s.v. 'recent' (KLN_1966.txt line 31893)\",\n       \"stance\": \"supports\",\n       \"note\": \"'L. recentem, acc. of recens, \\\"new, fresh\\\", which is formed fr. re- and I.-E. base *qen-, whence also OI. kanīnah, \\\"young\\\", kanā, kanyā, \\\"girl\\\"'.\"\n      },\n      {\n       \"src\": \"WLD\",\n       \"where\": \"Bd. I 398 (WLD_Bd1 djvu line 25052)\",\n       \"stance\": \"supports\",\n       \"note\": \"'lat. recens „frisch, jung, neu\\\" (so schon Döderlein Lat. Syn. IV, 1831, 96 f.) eigentlich „gerade vom Ursprung, der Geburt her\\\"'.\"\n      }\n     ]\n    },\n    {\n     \"id\": 6,\n     \"lang\": \"English\",\n     \"words\": \"recent\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"English 'recent' is a 16th-century learned borrowing: Middle French (= modern French) récent, from Latin recentem, the accusative of recēns, taken into English about 1533 with the sense 'lately happened'. The chart's long arrow from the Latin box to the English box therefore skips only the French intermediary, which is uncontroversial and is spelled out by Klein. The related learned family in English — recension, -cene (Eocene, Miocene), Cenozoic, kainite — comes from the Greek member of the same root, kainós.\",\n     \"derivation_fa\": \"واژهٔ انگلیسی recent وام‌واژه‌ای عالمانه از سدهٔ شانزدهم است: از فرانسهٔ میانه/نو récent و آن از لاتین recentem (حالت مفعولی recēns)، که در حدود ۱۵۳۳ میلادی وارد انگلیسی شده است. پیکان بلند نمودار از جعبهٔ لاتین به انگلیسی تنها حلقهٔ فرانسوی را نادیده می‌گیرد که امری بی‌مناقشه است و کلاین آن را صریح آورده. هم‌خانوادهٔ عالمانهٔ آن در انگلیسی — recension و -cene (Eocene, Miocene) و Cenozoic و kainite — از عضو یونانی همین ریشه (kainós) می‌آید. ادعای نورایی درست است.\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\n       \"ref\": \"None\",\n       \"status\": \"not_checked\",\n       \"note\": \"The node carries no reference of its own in the book; it inherits POK:563 from the Latin parent, which was checked there.\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"KLN\",\n       \"where\": \"p.1330 s.v. 'recent' (KLN_1966.txt line 31893)\",\n       \"stance\": \"supports\",\n       \"note\": \"'recent, adj. — MF. (= F.) récent, fr. L. recentem, acc. of recens, \\\"new, fresh\\\"'. Klein covers the whole chain Latin > French > English.\"\n      },\n      {\n       \"src\": \"AHD\",\n       \"where\": \"Watkins 1985 s.v. ken-3 (AHD_watkins1985.txt line 608)\",\n       \"stance\": \"supports\",\n       \"note\": \"The English derivative printed in caps at the end of the Latin branch is 'RECENT' — Watkins hangs exactly this English word on Latin recens under ken-3.\"\n      }\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 2,\n   \"root\": \"Kenk 1; Koksâ\",\n   \"verdict\": \"plausible\",\n   \"modern_form\": \"Two distinct PIE etyma: *kenk- 'heel, bend of the knee' (Pokorny IEW 566 'kenk-3'; Watkins 'kenk-3') and *koḱsā 'body part (hip, thigh)' (Pokorny IEW 611 'koḱsā'; Watkins 'koksā')\",\n   \"note\": \"The material of the box is real, but the box merges two entries that the handbooks keep apart. Pokorny 566 ('kenk-3, Meaning: knee-cup, heel') gives Lith. kenklė, kinka, ON hæll (*hanhila-), OE hela — the Germanic branch of Nourai's chart. Pokorny 611 ('koḱsā, a part of body (foot, hip etc.)') gives Skt. kakṣa- 'armpit', Av. kaša- 'Achsel', Lat. coxa 'hip', OIr. coss 'foot', OHG hahsina — the Iranian and Latin branches. Walde-Pokorny I 401 discusses precisely the question whether the two may be joined and rejects it as it stands: since Latin coxa's family is IE *koḱso- (with a palatal, proved by Av. kaša-), one would have to assume that Baltic kenk-/kink- replaced the palatal by a velar under the influence of the initial — 'wäre die Annahme nötig'. So combining them is a defensible older view but not the modern standard, and Nourai's own page citation POK:566 covers only the kenk- half (koḱsā is on p.611, as Watkins also notes). Beyond that, the whole Persian wing of this chart — kešāleh, kešīdan, kaškūl, tīr-kaš, kīš 1, kīš 2 — does not belong to either root: it belongs to Old Iranian *karš- 'to draw, pull, plough', which Cheung and Pokorny put at PIE *kʷels- / *kʷel-s- (Pokorny 639-640), and which Bartholomae (col. 456) and Mo'in in Borhan 1657 both connect to NP kašīdan. The Avestan box, which sets 'kaša : arm pit' and 'karš : to pull' side by side, is where the two families were confused.\",\n   \"note_fa\": \"مادهٔ این جعبه واقعی است، اما جعبه دو مدخل جدا را در هم آمیخته است. پوکورنی در صفحهٔ ۵۶۶ مدخل «kenk-3» را با معنای «پاشنه، پشتِ زانو» آورده (لیتوانیایی kenklė، اسکاندیناوی کهن hæll < *hanhila-، انگلیسی کهن hela) که همان شاخهٔ ژرمنی نمودار است؛ و در صفحهٔ ۶۱۱ مدخل جدای «koḱsā» را با معنای «اندامی از تن (پا، ران)» که سنسکریت kakṣa- «زیر بغل»، اوستایی kaša-، لاتین coxa «سُرین» و ایرلندی کهن coss «پا» را در بر می‌گیرد و شاخه‌های ایرانی و لاتینی نمودار از آن است. والده-پوکورنی (جلد ۱ ص ۴۰۱) همین پرسش را که آیا این دو یکی‌اند بررسی و رد می‌کند: چون خانوادهٔ coxa در هندواروپایی *koḱso- با کامی است (که اوستایی kaša- آن را ثابت می‌کند)، پیوند دادن آن به kenk- بالتی نیازمند فرضی ویژه است. پس یکی‌گرفتن آن دو دیدگاهی کهنه و با احتیاط پذیرفتنی است نه معیار امروزی، و ارجاع خود نورایی (POK:566) تنها نیمهٔ kenk- را پوشش می‌دهد. از این مهم‌تر، سراسر شاخهٔ فارسی این نمودار — کشاله، کشیدن، کشکول، تیرکش، کیش ۱، کیش ۲ — به هیچ‌یک از این دو ریشه تعلق ندارد و از ایرانی باستان *karš- «کشیدن، شخم زدن» است که چونگ و پوکورنی آن را به هندواروپایی *kʷels- (پوکورنی ۶۳۹–۶۴۰) می‌برند.\",\n   \"sources\": [\n    \"https://en.wiktionary.org/wiki/cushion\"\n   ],\n   \"ref_check\": [\n    {\n     \"ref\": \"POK:566\",\n     \"status\": \"partial\",\n     \"note\": \"POK_full.txt line 45309 ff. (block 'Page(s): 566'): 'Root / lemma: kenk-3 | Meaning: knee-cup, heel | Material: Old Indic kaṅkāla- \\\"bone, skeleton\\\"; Old Norse hā (*hanha-) ... Old Norse hæll \\\"calcaneus, heel bone\\\" (*hanhila-); Old English hela ...; Lithuanian kenklė \\\"popliteus\\\", kinka'. That page fully supports 'Kenk 1 : heel, knee' and the Germanic node, but it says nothing about Koksâ: Pokorny's 'koḱsā (*hoǵha), Meaning: a part of body (foot, hip etc.), Note: (Aryan also *kokso-s), Material: Old Indic kakṣa-, Avestan kaša- m. \\\"Achsel\\\" (proves -ks-); Latin coxa \\\"hip, haunch\\\"' is a separate entry printed on p.611.\"\n    }\n   ],\n   \"consulted\": [\n    {\n     \"src\": \"WLD\",\n     \"where\": \"Bd. I 401 ('3. kenk-') and Bd. I 456 f. ('koḱsā') — WLD_Bd1 djvu lines 25282 and 28738\",\n     \"stance\": \"partial\",\n     \"note\": \"'3. kenk- etwa „Kniekehle oder Ferse\\\". Lit. kenklė ... anord. hæll „Ferse\\\" (*hanhila-), ags. hēla m. „Ferse\\\". ... Als nasallosen Verwandten betrachtet Fick III⁴ 67 ahd. hacka ... sowie die Sippe von lat. coxa: da letztere idg. *kokso- ist (av. kaša-), wäre die Annahme nötig, daß bait. kenk-, kink- den ausl. Palatal durch Angleichung an den Anlaut durch Velar ersetzt hätte.' Walde-Pokorny thus records the very union Nourai's box performs, but flags it as requiring a special assumption — and keeps the two as separate articles.\"\n    },\n    {\n     \"src\": \"AHD\",\n     \"where\": \"Watkins 1985, s.vv. kenk-3 and koksā (AHD_watkins1985.txt lines 615 and 642)\",\n     \"stance\": \"partial\",\n     \"note\": \"'kenk-3. Heel, bend of the knee. 1. Germanic *hanhaz in Old English hōh, heel: HOCK. 2. Germanic *hanhilōn- in Old English hēla, heel: HEEL. [Pok. 3. kenk- 566.]' and, separately, 'koksā. Body part. Latin coxa, hip: COXA, CUISSE, CUSHION. [Pok. koksā 611.]' Watkins keeps them apart and gives Nourai's own AHD reference for the Latin branch.\"\n    },\n    {\n     \"src\": \"LAT\",\n     \"where\": \"Ernout-Meillet s.v. coxa (LAT.txt line 14253 ff.)\",\n     \"stance\": \"supports\",\n     \"note\": \"'coxa, -ae f.: hanche, os de la hanche, et par extension \\\"cuisse\\\" ... Le mot doit désigner une articulation en général; car les mots correspondants s'appliquent à des articulations diverses: irl. coss \\\"pied\\\", v.h.a. hahsa \\\"partie de derrière de l'articulation du genou\\\", skr. kakṣaḥ et kakṣā \\\"aisselle\\\".' The Latin-Iranian equation of the koḱsā half is standard.\"\n    },\n    {\n     \"src\": \"CHEUNG\",\n     \"where\": \"Etymological Dictionary of the Iranian Verb, s.v. *kars/*xrah (CHEUNG.txt line 16092 ff.)\",\n     \"stance\": \"contradicts\",\n     \"note\": \"'*kars/*xrah \\\"to draw, plough\\\" ... *NWIR: Widely attested: NP kašīdan/kaš- \\\"to pull, draw\\\" ... *PIE *kʷels- \\\"to plough\\\" = LIV: 388 f. | Pok.: 639'. The Persian wing of Nourai's chart therefore hangs on a different PIE root from either half of his root box.\"\n    }\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Avestan / Old Persian\",\n     \"words\": \"kaša : arm pit; karš : to pull\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"The two words in this box are not related to each other. (a) Avestan kaša- m. 'armpit, Achselhöhle' is genuine and is exactly the Iranian witness for *koḱsā: Bartholomae col. 461 has 'kaša- m. Achselhöhle', Pokorny 611 cites 'Avestan kaša- m. \\\"Achsel\\\" (proves -ks-)' beside Skt. kakṣa- and Lat. coxa, and Klein s.v. 'hock' gives 'OI. kakṣaḥ, kakṣā, Avestic kasha, \\\"armpit\\\", L. coxa, \\\"hip\\\"'. That word belongs to the Koksâ half of the root box and is confirmed. (b) Avestan karš- 'to draw, drag, plough' is an entirely different root: Cheung derives it from PIE *kʷels- 'to plough' (LIV 388 f., Pokorny 639), and Pokorny himself files Skt. karṣati / Av. karša- as an s-extension of *kʷel-1 'to turn' on pp. 639-640, not under kenk- or koḱsā. Bartholomae's article (col. 456, 'karš- V. \\\"trahere\\\", nur mit Praev.') gives 'np. kašīdan, arm. LW. kʿaršel', i.e. it is the parent of the whole Persian box below, and it has nothing to do with hips or heels. Putting karš beside kaša here is what lets the chart hang the Persian words on the wrong root. The label 'Avestan / Old Persian' is also loose: both words are Avestan; neither is attested in Old Persian.\",\n     \"derivation_fa\": \"دو واژهٔ این جعبه با هم خویشاوند نیستند. الف) اوستایی kaša- «زیر بغل» اصیل است و درست همان گواه ایرانی *koḱsā است: بارتولمه در ستون ۴۶۱ «kaša- m. Achselhöhle» آورده، پوکورنی در صفحهٔ ۶۱۱ آن را در کنار سنسکریت kakṣa- و لاتین coxa می‌نشاند و می‌گوید که همین صورت وجود -ks- را ثابت می‌کند، و کلاین نیز ذیل hock همین برابری را دارد؛ پس این واژه به نیمهٔ Koksâ تعلق دارد و درست است. ب) اما اوستایی karš- «کشیدن، شخم زدن» ریشه‌ای یکسره دیگر است: چونگ آن را از هندواروپایی *kʷels- «شخم زدن» می‌گیرد (LIV ۳۸۸ و پوکورنی ۶۳۹) و خودِ پوکورنی نیز karṣati سنسکریت و karša- اوستایی را گسترش s-دار ریشهٔ *kʷel- «چرخیدن» در صفحه‌های ۶۳۹–۶۴۰ آورده است، نه ذیل kenk- یا koḱsā. بارتولمه در ستون ۴۵۶ ذیل «karš- «کشیدن»» صریحاً «np. kašīdan» را می‌آورد؛ یعنی این ماده پدر همهٔ واژه‌های جعبهٔ فارسی زیرین است و ربطی به سرین و پاشنه ندارد. نشاندن karš در کنار kaša همان جایی است که نمودار را به خطا می‌اندازد. برچسب «اوستایی / پارسی باستان» نیز نادقیق است: هر دو واژه اوستایی‌اند و هیچ‌کدام در پارسی باستان گواهی نشده‌اند.\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\n       \"ref\": \"KLN:735\",\n       \"status\": \"partial\",\n       \"note\": \"Klein p.735 (KLN_1966.txt line 17900) is 'hobble ... hobo' and contains nothing relevant; the entry Nourai wants is one page on, p.736 s.v. 'hock': 'hock, n., the joint in the hind leg of a horse. — ME. hough, hoch, fr. OE. hōh, \\\"heel\\\" ... and cogn. with OI. kakṣaḥ, kakṣā, Avestic kasha, \\\"armpit\\\", L. coxa, \\\"hip\\\", Lith. kinka, kenklė, \\\"knee joint\\\", cinksla, \\\"knee sinew\\\", OIr. coss, \\\"foot\\\". Cp. bough. Cp. also heel. Cp. also coxa.' That page supports kaša and the whole koḱsā/kenk- comparison, but says nothing about karš 'to pull'.\"\n      },\n      {\n       \"ref\": \"BRT:456\",\n       \"status\": \"supports\",\n       \"note\": \"Bartholomae, Altiranisches Wörterbuch col. 456 (BRT.txt line ~9330, running head '455 karapan- 2 — ¹karš- 456'): '¹karš- V. \\\"trahere\\\", nur mit Praev. Praes. 2 karša-, 24 karšaya-. mit apa \\\"(mit sich) fortschleppen\\\" ... mit ava \\\"(mit sich) herabführen, anschwemmen\\\" ... ai. kárṣati, np. kašīdan, arm. LW. kʿaršel'. The column is exactly right for karš — but Bartholomae files it as a verb of dragging, with no connection to kaša- 'Achselhöhle' (his col. ~461).\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"BRT\",\n       \"where\": \"col. ~461 s.v. kaša- (BRT.txt line 9456)\",\n       \"stance\": \"supports\",\n       \"note\": \"'kaša- m. Achselhöhle: dašinəm (bz. hōyəm) °ahe V.8.48-50, 9.17, 18' with the note 'ai. kákṣa- m., mp. (Pü), np. kaš; vgl. afγ. kṣ̌ē'. Bartholomae's own New Persian equivalent of Av. kaša- is kaš 'armpit/side', not the verb.\"\n      },\n      {\n       \"src\": \"POK\",\n       \"where\": \"IEW 611, s.v. koḱsā, and IEW 639-640, s.v. kʷel-1 (POK_full.txt lines 47873 and 52642)\",\n       \"stance\": \"partial\",\n       \"note\": \"'koḱsā ... Old Indic kakṣā, kakṣa- \\\"Achselgrube, Gurtgegend der Pferde\\\", Avestan kaša- m. \\\"Achsel\\\" (proves -ks-); Latin coxa \\\"hip, haunch\\\"' — supports kaša. But 's-extension in Old Indic karṣū- f. \\\"furrow, headland\\\", karṣati, kr̥ṣati \\\"turn over, rotate something, plow\\\", Avestan karša- m. n. \\\"furrow\\\", karšaiti \\\"ridge, mark with ridges\\\"' stands under kʷel-1 on pp. 639-640 — a different root from the box.\"\n      },\n      {\n       \"src\": \"CHEUNG\",\n       \"where\": \"s.v. *kars/*xrah (CHEUNG.txt lines 16092-16200)\",\n       \"stance\": \"contradicts\",\n       \"note\": \"'*kars/*xrah \\\"to draw, plough\\\". *AVESTAN: YAv. karš- \\\"to draw (furrows), plough\\\" ... *PIE *kʷels- \\\"to plough\\\" = LIV: 388 f. | Pok.: 639'. The modern standard reference for Iranian verbs puts karš- under *kʷels-, not *kenk-/*koḱsā.\"\n      },\n      {\n       \"src\": \"ARY\",\n       \"where\": \"Aryanpur, Farhang-e Rishe-hā, entry کشیدن (ARY_latin_index_pages.txt, pdf page 406)\",\n       \"stance\": \"contradicts\",\n       \"note\": \"The headword کشیدن lists 'KARSH-, KARSHA (AVESTAN); KASHITAN (PAHLAVI); KESHIDAN, KESH-; KISHIN (KURDISH); KASHAG (BALUCHI); KARSH-, KRSH- (SANSKRIT); KARSHEM (ARMENIAN)' with references to Pokorny, MacKenzie '(DRAW) 111, (PULL) 129' and Buck '(DRAW, PULL) 571-572' — an independent modern Persian treatment that puts kešīdan in the 'draw/pull' root and nowhere near the hip/heel root.\"\n      }\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Persian\",\n     \"words\": \"kešâleh «کشاله» : crutch; kešîdan «کشیدن» : to pull; kaškŭl «کشکول» : Dervish's cup that is \\\"carried by the shoulder\\\"; tîr-kaš «تیرکش» : bag for carrying arrows, quiver (also ترکش); kîš 1 «کیش ۱» : distorted form of \\\"tîr-kaš\\\", quiver; kîš 2 «کیش ۲» : a \\\"kîš 1\\\"-looking island south of Iran\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"Every word in this box is built on the present stem kaš-/keš- of کشیدن kešīdan 'to draw, pull', and that verb descends from Avestan karš- (Middle Persian kašīdan/kaš-, Kurdish kišān, Baluchi kašag, Skt. karṣati, Arm. lw. kʿaršel), whose PIE ancestor is *kʷels- 'to plough, draw' (Cheung; Pokorny 639-640), not *kenk-/*koḱsā. So the arrow from the root box is misdirected for the whole box, even though the internal Persian derivations are mostly sound. In detail: (a) کشاله kešāleh is the verbal noun kaš- + -āleh, 'a dragging'; its concrete anatomical sense is کشالهٔ ران 'the groin, the fold where thigh meets trunk' — Nourai's gloss 'crutch' is the old English word for that same body-fork (crotch), so the entry is coherent, but it is a derivative of the verb, not an inherited body-part word. (b) کشیدن kešīdan is the verb itself: Old Iranian *karš- > MP kašīdan with the regular Iranian loss of -r- before -š- and New Persian raising of a > e; Horn no. 859 and Mo'in's footnote at Borhan 1657 both spell out exactly this chain. (c) کشکول kaškūl is a compound kaš 'carry, drag' + kūl 'shoulder' — Borhan itself says so ('معنی ترکیبی آن کشیدن بدوش است چه کش بمعنی کشیدن و کول دوش و کتف را گویند'), and Addi Shir lists the Arabic kaškūl as a Persian loan with that same analysis, though he and Mo'in both record a rival Aramaic derivation, so the compound reading is likely but not certain. (d) تیرکش tīr-kaš 'quiver' is tīr 'arrow' + kaš, contracted in speech to ترکش tarkaš, from which Italian turcasso and French carquois were borrowed (Horn no. 406). (e) کیش kīš 1 'quiver': Borhan 1755 glosses it 'بمعنی ترکش باشد و آن غلافی است که تیر در آن کنند و بر کمر بندند' and cross-refers to تیرکش/ترکش, which is the basis of Nourai's 'distorted form of tīr-kaš'; the shortening tīr-kaš > (tar)kaš > kīš is plausible and is what Dehkhoda assumes, but no standard etymological dictionary derives it phonetically, so this last step is best called folk-lexicographic rather than demonstrated. (f) کیش kīš 2, the Persian Gulf island, is explained by Borhan (and by Tārīkh-e Waṣṣāf, which it quotes) as named from its quiver-like outline seen from the heights near Hormuz — a traditional and quite possibly folk etymology, since the island's older name is Qais/Kīš, arabicised as قيس.\",\n     \"derivation_fa\": \"همهٔ واژه‌های این جعبه بر ستاک حال کَش-/کِش- از «کشیدن» ساخته شده‌اند و این فعل از اوستایی karš- می‌آید (فارسی میانه kašīdan، کردی kišān، بلوچی kašag، سنسکریت karṣati، ارمنی وام‌واژهٔ kʿaršel) که نیای هندواروپایی آن *kʷels- «شخم زدن، کشیدن» است (چونگ؛ پوکورنی ۶۳۹–۶۴۰)، نه *kenk-/*koḱsā. پس پیکانی که از جعبهٔ ریشه به این گره کشیده شده برای تمام واژه‌ها نادرست است، هرچند اشتقاق‌های درونیِ فارسی بیشتر درست‌اند. به تفصیل: (الف) «کشاله» اسم‌مصدر کَش- + -اله است و معنای اندام‌شناختی آن «کشالهٔ ران» است؛ ترجمهٔ نورایی («crutch») همان واژهٔ کهن انگلیسی برای دوراهی ران است، پس معنا نادرست نیست ولی واژه مشتق فعل است نه نامی موروثی برای اندام. (ب) «کشیدن» خودِ فعل است: ایرانی باستان *karš- > فارسی میانه kašītan با افتادن r پیش از š، و a > e در فارسی نو؛ هرن (شمارهٔ ۸۵۹) و حاشیهٔ معین در برهان ص ۱۶۵۷ دقیقاً همین زنجیره را می‌آورند. (ج) «کشکول» ترکیب کَش «کشیدن» + کول «دوش، کتف» است و خودِ برهان قاطع می‌گوید «معنی ترکیبی آن کشیدن بدوش است»؛ ادّی شیر نیز کشکولِ عربی را وام‌واژه‌ای فارسی با همین تحلیل می‌داند، اما هم او و هم معین اشتقاق رقیبی از آرامی را یاد کرده‌اند، پس این تحلیل محتمل است نه قطعی. (د) «تیرکش» = تیر + کَش که در گفتار به «ترکش» کوتاه شده و ایتالیایی turcasso و فرانسوی carquois از آن وام گرفته شده‌اند (هرن شمارهٔ ۴۰۶). (ه) «کیش ۱»: برهان ص ۱۷۵۵ آن را «بمعنی ترکش... غلافی که تیر در آن کنند و بر کمر بندند» می‌داند و به «تیرکش/ترکش» ارجاع می‌دهد؛ کوتاه‌شدن تیرکش به کیش پذیرفتنی است و دهخدا نیز همین را فرض می‌کند، ولی هیچ فرهنگ ریشه‌شناختی معیاری آن را آوایی اثبات نکرده است. (و) «کیش ۲»، جزیرهٔ خلیج فارس، در برهان به نقل از تاریخ وصّاف از شباهت نمای جزیره به ترکش نام گرفته است؛ این توجیه سنّتی و به احتمال زیاد ریشه‌شناسی عامیانه است، چون نام کهن‌تر جزیره «قیس» (معرّب کیش) است.\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\n       \"ref\": \"HRN:191\",\n       \"status\": \"supports\",\n       \"note\": \"Horn, Grundriss p.191 no. 859 (HRN.txt leaf 213): 'kešīden \\\"ziehen\\\". aw. √karš-, karšayeti; phlv. kašītan; ai. 1. √karš-, kárṣati, karṣayati \\\"ziehen, schleppen\\\". kurd. kišān \\\"ziehen\\\"; afγ. kṣ̌əl; bal. kašay \\\"ziehen, abziehen, herausziehen\\\"; arm. LW. (?) kʿaršem \\\"ziehen\\\"'. Supports the Persian verb and its Avestan parent — but from karš-, i.e. from Nourai's second Avestan word only.\"\n      },\n      {\n       \"ref\": \"BQT:1653\",\n       \"status\": \"supports\",\n       \"note\": \"Borhan-e Qate' ed. Mo'in p.1653 = BQT_v3_pages.txt pdf page 446: 'کشکول = بروزن مقبول، بمعنی گدا باشد یعنی شخصی که گدایی کند - و کاسهٔ کشکول کاسهٔ گدا را گویند و معنی ترکیبی آن کشیدن بدوش است چه کش بمعنی کشیدن و کول دوش و کتف را گویند'. That is verbatim Nourai's gloss 'Dervish's cup that is carried by the shoulder'. Mo'in's footnote 6 on the same page adds a rival derivation of the Arabic form from Aramaic.\"\n      },\n      {\n       \"ref\": \"BQT:1657\",\n       \"status\": \"supports\",\n       \"note\": \"Borhan-e Qate' p.1657 = BQT_v3_pages.txt pdf page 450, footnote to کشیدن: 'کشیدن - بکسر اول و فتح چهارم ... از: کش + یدن (پسوند مصدری). جزو اول در اوستا karsh «بارتولمه ۴۵۵» ... [فارسی] باستان karsh (کشیدن)، پهلوی kašītan. کردی kišān (کشیدن) ... بلوچی kashag (کشیدن، برداشتن)، ارمنی karshem (کشیدن) «اسئق ۸۵۹»'. Mo'in's own footnote gives Bartholomae col. 455 — the karš- article — not a hip/heel root.\"\n      },\n      {\n       \"ref\": \"BQT:1755\",\n       \"status\": \"supports\",\n       \"note\": \"Borhan-e Qate' p.1755 = BQT_v3_pages.txt pdf page 552: 'کیش با یای مجهول بروزن ریش، بمعنی ترکش باشد و آن غلافی است که تیر در آن کنند و بر کمر بندند [footnote 1: رك: تیرکش، ترکش — with the Anvarī verse «آسمان گر سلاح بربندد ـ تیر تدبیر تو نهد در کیش» attributed to انوری ابیوردی چاپ تبریز ص ۴۱۲] ... و نام شهری است در جزیره‌ای از دریا ... و وجه تسمیهٔ این آن است که چون بر بلندیهای اطراف هرموز نگرند به هیئت کیش که ترکش باشد بنظر درمی‌آید [footnote 3: قیس، جزیره‌ای از جزایر بحر فارس ... تاریخ وصاف]'. Both kīš 1 and kīš 2 and the very verse quoted in the JSON come from this page.\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"CHEUNG\",\n       \"where\": \"s.v. *kars/*xrah (CHEUNG.txt lines 16092, 16169, 16187)\",\n       \"stance\": \"contradicts\",\n       \"note\": \"'*NWIR: Widely attested: NP kašīdan/kaš- \\\"to pull, draw\\\" ... *SANSKRIT: karṣ \\\"to pull, drag, plow\\\" (RV+) ... *PIE *kʷels- \\\"to plough\\\" = LIV: 388 f. | Pok.: 639'. The Persian verb and everything built on it belong to *kʷels-, so the arrow from Kenk 1/Koksâ is wrong.\"\n      },\n      {\n       \"src\": \"HRN\",\n       \"where\": \"Grundriss p.92 no. 406 (HRN.txt leaf 113)\",\n       \"stance\": \"supports\",\n       \"note\": \"'406. tīr \\\"Pfeil\\\", tīrkeš, terkeš \\\"Köcher\\\" ... aw. tiγri- \\\"Pfeil\\\"; phlv. tīr \\\"Pfeil\\\"' with the footnote 'Daraus ital. turcasso, franz. carquois (de Lagarde, Ges. Abh. 80); vergl. auch mhd. tërkis \\\"Köcher\\\" bei Wolfram'. Horn confirms both the compound tīr-kaš and the contracted tarkaš, and its European progeny.\"\n      },\n      {\n       \"src\": \"AFM\",\n       \"where\": \"Addi Shir, al-Alfaz al-Farisiyya al-Mu'arraba, s.v. الكشكول (AFM_pages.txt line 3462)\",\n       \"stance\": \"partial\",\n       \"note\": \"'(الكشكول) قدح الكدي يجمع فيه ... كشكول وهو [مركب] من ... [كش] ... [كول] اي كتف أو ردف ... المحتمل ان تكون ارامية' — Addi Shir treats Arabic kaškūl as a Persian loan compounded of kaš + kūl 'shoulder or haunch', but adds that an Aramaic origin is possible, matching Mo'in's caveat.\"\n      },\n      {\n       \"src\": \"PHD\",\n       \"where\": \"MacKenzie p.49 s.v. kantīgr (PHD.txt line 424)\",\n       \"stance\": \"partial\",\n       \"note\": \"'kantīgr [kntgl] quiver.' The Middle Persian word for 'quiver' is kantīgr, not anything from kaš-; so there is no Pahlavi ancestor for either tīr-kaš or kīš 1, which is consistent with both being New Persian formations.\"\n      },\n      {\n       \"src\": \"MON\",\n       \"where\": \"Dehkhoda/Mo'in tradition as reported at vajehyab (search result, ترکش and کیش)\",\n       \"stance\": \"partial\",\n       \"note\": \"Dehkhoda glosses ترکش as تیردان and treats it as a shortened form of تیرکش, and connects کیش with ترکش — i.e. the Persian lexicographical tradition Nourai follows, but presented as a gloss rather than a phonetic derivation.\"\n      }\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Latin\",\n     \"words\": \"coxa : hip; coxînus : hip rest\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"Latin coxa 'hip, hip-bone', attested from Nigidius Figulus on, is the regular Latin outcome of PIE *koḱsā and is matched by Skt. kakṣa- 'armpit', Av. kaša-, OIr. coss 'foot', OHG hahsa 'hock' (Ernout-Meillet; Pokorny 611; Watkins 'koksā ... Latin coxa, hip: COXA, CUISSE, CUSHION'). In Romance coxa displaced femur and came to mean 'thigh' — hence Italian coscia, Old Provençal coissa, Spanish coxa, Old French cuisse. The second form on the chart, coxînus, is not a classical Latin word: it is the reconstructed Vulgar/Medieval Latin *coxīnus 'seat-pad', starred in Klein ('ML. *coxinus') and in Wiktionary ('Vulgar Latin *coxīnus \\\"seat pad\\\", derived from Latin coxa, with the suffix possibly modelled on Latin pulvīnus \\\"pillow\\\"'). So the box is right in substance but the unstarred spelling and the label 'Latin' overstate the attestation, and 'hip rest' is a paraphrase rather than a recorded gloss.\",\n     \"derivation_fa\": \"لاتین coxa «سرین، استخوان سرین» که از نیگیدیوس فیگولوس به بعد گواهی شده، بازتاب قاعده‌مند هندواروپایی *koḱsā است و با سنسکریت kakṣa- «زیر بغل»، اوستایی kaša-، ایرلندی کهن coss «پا» و آلمانی علیای کهن hahsa برابر می‌ایستد (ارنو-مه‌یه؛ پوکورنی ۶۱۱؛ واتکینز ذیل koksā). در زبان‌های رومی coxa جای femur را گرفت و معنای «ران» یافت: ایتالیایی coscia، اسپانیایی coxa، فرانسهٔ کهن cuisse. اما صورت دوم نمودار، coxînus، واژهٔ لاتین کلاسیک نیست؛ صورتی است بازسازی‌شده از لاتین عامیانه/میانه *coxīnus «بالشتک نشیمن» که کلاین آن را با ستاره می‌آورد و ویکی‌واژه پسوند آن را به قیاس pulvīnus «بالش» می‌داند. پس محتوای جعبه درست است، ولی نوشتن آن بی‌ستاره و زیر برچسب «لاتین» بیش از اندازه قاطع است و «hip rest» نیز تعبیر نویسنده است نه معنای ثبت‌شده.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/cushion\"\n     ],\n     \"ref_check\": [\n      {\n       \"ref\": \"AHD:326\",\n       \"status\": \"partial\",\n       \"note\": \"Nourai's AHD:326 is a page of the 1975/76 New College dictionary body (the word entries, not the root appendix), which is not open online; the corresponding root article is Watkins 1985 'koksā. Body part. Latin coxa, hip: COXA, CUISSE, CUSHION. [Pok. koksā 611.]' (AHD_watkins1985.txt line 642), which states exactly the claim of this node and of nodes 4 and 6. Note that AHD's own Pokorny reference is 611, not the 566 printed in the root box.\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"LAT\",\n       \"where\": \"Ernout-Meillet s.v. coxa (LAT.txt line 14253)\",\n       \"stance\": \"supports\",\n       \"note\": \"'coxa, -ae f.: hanche, os de la hanche, et par extension \\\"cuisse\\\" ... Attesté à partir de Nigidius. A remplacé dans les langues romanes femur ... Panroman' — and the cognates 'irl. coss \\\"pied\\\", v.h.a. hahsa ..., skr. kakṣaḥ et kakṣā \\\"aisselle\\\"'. No *coxīnus is listed among the derivatives (coxus, coxo, coxosus, coxale, coxarius, coxendix, coxim), confirming that it is a reconstruction.\"\n      },\n      {\n       \"src\": \"KLN\",\n       \"where\": \"p.360 s.v. coxa (KLN_1966.txt line 9492)\",\n       \"stance\": \"supports\",\n       \"note\": \"'coxa, n., the hip (anat.) — L., \\\"hip\\\", cogn. with OI. kakṣaḥ, kakṣā, \\\"armpit\\\", OE. hōh, \\\"heel\\\", and with the first element in OE. hōh-sinu, \\\"hock sinew\\\". See hock ... and cp. cuisse, cushion, Quixotic.'\"\n      },\n      {\n       \"src\": \"POK\",\n       \"where\": \"IEW 611 s.v. koḱsā (POK_full.txt line 47873)\",\n       \"stance\": \"supports\",\n       \"note\": \"'Root / lemma: koḱsā (*hoǵha) | Meaning: a part of body (foot, hip. etc..) | Material: Old Indic kakṣā, kakṣa- \\\"Achselgrube, Gurtgegend the Pferde\\\", Avestan kaša- m. \\\"Achsel\\\" (proves -ks-); Latin coxa \\\"hip, haunch\\\"'.\"\n      }\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"Old French\",\n     \"words\": \"cuisse, coissin : cushion\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"Two separate Old French words are packed into one line with one gloss. (a) OF cuisse means 'thigh', not 'cushion': it is the regular phonetic descendant of Latin coxa (coxa > *cŏxa > cuisse, with the Gallo-Romance diphthongisation of ŏ and the palatalisation of -ks- to -is-), and it is the source of English cuisse/cuish 'thigh-armour' (Klein). (b) OF coissin (variant cussin, modern French coussin) is the source of English cushion and comes from Vulgar Latin *coxīnus 'seat-pad', a suffixal derivative of the same coxa; Klein notes that 'the orig. meaning of OF. coissin was \\\"hip cushion\\\"'. So the derivation from Latin is right for both words and the two-word line is genuinely Old French, but the single gloss 'cushion' is wrong for cuisse.\",\n     \"derivation_fa\": \"در این سطر دو واژهٔ جدای فرانسهٔ کهن با یک معنا کنار هم نشسته‌اند. الف) cuisse در فرانسهٔ کهن «ران» است نه «بالشتک»: بازماندهٔ آوایی قاعده‌مند لاتین coxa است (با دوگانه‌شدن ŏ در گالو-رومی و کامی‌شدن -ks- به -is-) و خاستگاه واژهٔ انگلیسی cuisse «زره ران» است (کلاین). ب) coissin (گونهٔ cussin، فرانسهٔ امروزی coussin) خاستگاه cushion انگلیسی است و از لاتین عامیانهٔ *coxīnus «بالشتک نشیمن»، مشتق پسونددار همان coxa، می‌آید؛ کلاین می‌افزاید که معنای اصلی coissin «بالشتکِ سرین» بوده است. پس اشتقاق هر دو واژه از لاتین درست است و هر دو واقعاً فرانسهٔ کهن‌اند، اما معنای یگانهٔ «cushion» برای cuisse نادرست است.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/cushion\"\n     ],\n     \"ref_check\": [\n      {\n       \"ref\": \"AHD\",\n       \"status\": \"supports\",\n       \"note\": \"Watkins 1985 s.v. koksā (AHD_watkins1985.txt line 642) lists both English reflexes of these two Old French words together: 'Latin coxa, hip: COXA, CUISSE, CUSHION'; the index (line 1402/1404) confirms 'CUISSE koksa' and 'CUSHION koksa'.\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"KLN\",\n       \"where\": \"p.377 s.v. cuisse and p.383 s.v. cushion (KLN_1966.txt lines 9879, 10006)\",\n       \"stance\": \"partial\",\n       \"note\": \"'cuisse, cuish, n., usually in the pl., armor for protecting the thigh. — ME. cuissues, fr. OF. cuisseaux, pl. of cuissel, fr. cuisse, \\\"thigh\\\", fr. L. coxa, \\\"hip\\\"' and 'cushion, n. — ME. quisshin, cusshin, fr. OF. coissin, cussin (F. coussin), fr. ML. *coxinus, fr. L. coxa, \\\"hip\\\" ... The orig. meaning of OF. coissin was \\\"hip cushion\\\".' Klein confirms both derivations and shows that cuisse means 'thigh'.\"\n      },\n      {\n       \"src\": \"LAT\",\n       \"where\": \"Ernout-Meillet s.v. coxa (LAT.txt line 14256)\",\n       \"stance\": \"supports\",\n       \"note\": \"'A remplacé dans les langues romanes femur qui n'est demeuré que dans un dialecte rhéto-roman ... Panroman' — the Romance semantic shift 'hip' > 'thigh' that produced OF cuisse.\"\n      }\n     ]\n    },\n    {\n     \"id\": 5,\n     \"lang\": \"Persian\",\n     \"words\": \"kŭsan «کوسن» : cushion\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"Persian کوسن kusan 'small decorative cushion' is indeed a borrowing of this word, but not from Old French: it is a modern (late 19th-/20th-century) loan from French coussin, taken in during the period of heavy French lexical influence on Persian, with the regular Persian rendering of French [u] as و and of nasalised -in as -ن. Mo'in glosses it simply 'بالش، بالشتک' and Amid as 'a small decorative pillow placed on furniture'; neither prints an etymology, and the reference Nourai cites (Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi) is precisely a dictionary of European loanwords in Persian, so the citation is apt in kind. The chart's arrow from the Old French box is therefore right in substance (same word, same ultimate Latin source) but wrong in date and in the immediate donor: the intermediate is modern French, not Old French coissin.\",\n     \"derivation_fa\": \"«کوسن» فارسی به‌راستی وام‌واژهٔ همین کلمه است، اما نه از فرانسهٔ کهن: وام‌واژه‌ای نو (اواخر سدهٔ سیزدهم/چهاردهم خورشیدی) از فرانسهٔ coussin است که در دورهٔ نفوذ گستردهٔ واژگان فرانسوی در فارسی وارد شده و [u] فرانسوی به «و» و پایانهٔ خیشومی -in به «ن» برگردانده شده است. معین آن را «بالش، بالشتک» و عمید «بالشتک کوچک تزیینی» معنا کرده‌اند و هیچ‌کدام ریشه‌شناسی نیاورده‌اند؛ مأخذی هم که نورایی یاد کرده (فرهنگ واژه‌های اروپایی در فارسیِ مهشید مشیری) دقیقاً فرهنگ وام‌واژه‌های اروپایی است، پس ارجاع بجاست. بنابراین پیکان نمودار از جعبهٔ فرانسهٔ کهن از نظر مادّه درست است (همان واژه، همان خاستگاه لاتینی) ولی از نظر تاریخ و واسطه نادرست: واسطه فرانسهٔ نو است نه coissin کهن.\",\n     \"sources\": [\n      \"https://abadis.ir/fatofa/%DA%A9%D9%88%D8%B3%D9%86/\"\n     ],\n     \"ref_check\": [\n      {\n       \"ref\": \"VOP:296\",\n       \"status\": \"not_checked\",\n       \"note\": \"Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi (Alborz 1371/1992) has no online copy: refs_online.json records 'RE-SEARCH 2026-09: nothing — no catalogue record with a scan, no ebook', with the decoys (Zomorrodian, Nahid Shahidi) explicitly excluded. So the page could not be inspected.\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"MON\",\n       \"where\": \"Mo'in and Amid entries for کوسن via abadis.ir (archived)\",\n       \"stance\": \"partial\",\n       \"note\": \"Mo'in: 'بالش، بالشتک'; Amid: 'بالشتک کوچک تزیینی که روی مبل می‌گذارند'. Both confirm the meaning 'cushion' that the chart gives, but neither states the French origin.\"\n      },\n      {\n       \"src\": \"MON\",\n       \"where\": \"MON_part1.txt / MON_2vol_Adena (grep کوسن)\",\n       \"stance\": \"silent\",\n       \"note\": \"The only hit for the string کوسن in the local Mo'in OCR is inside the unrelated article خارصینی (line 7472), i.e. OCR noise; the printed Farhang-e Farsi article could not be located in these scans.\"\n      },\n      {\n       \"src\": \"KLN\",\n       \"where\": \"p.383 s.v. cushion (KLN_1966.txt line 10006)\",\n       \"stance\": \"supports\",\n       \"note\": \"'F. coussin' — Klein records the modern French form which is the actual donor of the Persian word, alongside 'It. cuscino and Sp. cojín, which are French loan words', i.e. exactly the pattern of secondary borrowing that Persian کوسن belongs to.\"\n      }\n     ]\n    },\n    {\n     \"id\": 6,\n     \"lang\": \"English\",\n     \"words\": \"cushion\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"English cushion is Middle English quisshin, cusshin (14th c.), borrowed from Old French coissin/cussin (modern coussin), itself from Vulgar Latin *coxīnus 'seat-pad', a derivative of Latin coxa 'hip' — literally the pad one sits on with one's hips. The modern spelling with -sh- reflects the Anglo-Norman [s]/[ʃ] variation. Klein, Watkins and Wiktionary all give this chain without qualification, so the chart's arrow from the Old French box is standard.\",\n     \"derivation_fa\": \"واژهٔ انگلیسی cushion در انگلیسی میانه quisshin/cusshin (سدهٔ چهاردهم میلادی) است که از فرانسهٔ کهن coissin/cussin (امروزی coussin) وام گرفته شده و آن از لاتین عامیانهٔ *coxīnus «بالشتک نشیمن»، مشتق coxa «سرین»، می‌آید؛ یعنی تحت‌اللفظ «آنچه بر آن می‌نشینند». املای امروزی با -sh- بازتاب نوسان [s]/[ʃ] در انگلونورمان است. کلاین، واتکینز و ویکی‌واژه هر سه این زنجیره را بی‌قید و شرط می‌آورند، پس پیکان نمودار از جعبهٔ فرانسهٔ کهن معیار است. ادعای نورایی درست است.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/cushion\"\n     ],\n     \"ref_check\": [\n      {\n       \"ref\": \"None\",\n       \"status\": \"not_checked\",\n       \"note\": \"The node carries no reference of its own; it inherits AHD from the Old French parent, and Watkins' koksā article names CUSHION as the English derivative (checked at node 3).\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"KLN\",\n       \"where\": \"p.383 s.v. cushion (KLN_1966.txt line 10006)\",\n       \"stance\": \"supports\",\n       \"note\": \"'cushion, n. — ME. quisshin, cusshin, fr. OF. coissin, cussin (F. coussin), fr. ML. *coxinus, fr. L. coxa, \\\"hip\\\"; see coxa and cp. cuisse.'\"\n      },\n      {\n       \"src\": \"AHD\",\n       \"where\": \"Watkins 1985 s.v. koksā and index (AHD_watkins1985.txt lines 642, 1404)\",\n       \"stance\": \"supports\",\n       \"note\": \"'koksā. Body part. Latin coxa, hip: COXA, CUISSE, CUSHION' and index 'CUSHION koksa'.\"\n      }\n     ]\n    },\n    {\n     \"id\": 7,\n     \"lang\": \"Germanic\",\n     \"words\": \"hanhila : heel\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Proto-Germanic *hanhilōn- / *hanhila- 'heel' is a diminutive-like -ila- formation on *hanha- 'heel, hock' (Old Norse hā- in há-mót 'ankle joint', OE hōh 'heel, hock'), from PIE *kenk- 'heel, bend of the knee' by Grimm's Law (*k > h) and with the Germanic outcome of the nasal-plus-velar sequence. Pokorny 566 cites 'Old Norse hæll \\\"calcaneus, heel bone\\\" (*hanhila-)' and Old English hēla in the same breath, and Watkins writes the same preform as *hanhilōn-. The chart's spelling 'hanhila' is the standard reconstructed stem (Nourai simply drops the asterisk, as he does throughout), and the gloss 'heel' is right.\",\n     \"derivation_fa\": \"ژرمنی آغازین *hanhilōn-/*hanhila- «پاشنه» ساختی با پسوند -ila- بر ستاک *hanha- «پاشنه، بندِ پس‌پا» است (اسکاندیناوی کهن há- در há-mót «مفصل قوزک»، انگلیسی کهن hōh)، و آن از هندواروپایی *kenk- «پاشنه، پشت زانو» با قانون گریم (*k > h) و تحول ژرمنی خوشهٔ خیشومی+کامی پدید آمده است. پوکورنی در صفحهٔ ۵۶۶ صریحاً «anord. hæll «Ferse» (*hanhila-)» و «ags. hēla» را کنار هم می‌آورد و واتکینز نیز همان صورت *hanhilōn- را بازسازی می‌کند. صورت «hanhila» در نمودار همان ستاک بازسازی‌شدهٔ معیار است (نورایی ستاره را، چنان‌که شیوهٔ اوست، نیاورده) و معنای «پاشنه» درست است. ادعای نورایی درست است.\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\n       \"ref\": \"AHD\",\n       \"status\": \"supports\",\n       \"note\": \"Watkins 1985 (AHD_watkins1985.txt line 615): 'kenk-3. Heel, bend of the knee. 1. Germanic *hanhaz in Old English hōh, heel: HOCK. 2. Germanic *hanhilōn- in Old English hēla, heel: HEEL. [Pok. 3. kenk- 566.]' — precisely this node and node 8.\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"POK\",\n       \"where\": \"IEW 566 s.v. kenk-3 (POK_full.txt line 45309)\",\n       \"stance\": \"supports\",\n       \"note\": \"'Old Norse hā (*hanha-) in ha-mót m. \\\"ankle joint, heel joint\\\" ... Old English hōh \\\"calcaneus, heel bone\\\" (*hanha-). Old Norse hæll \\\"calcaneus, heel bone\\\" (*hanhila-). Old English hēla m. \\\"calcaneus, heel bone\\\".'\"\n      },\n      {\n       \"src\": \"WLD\",\n       \"where\": \"Bd. I 401 ('3. kenk-', WLD_Bd1 djvu line 25285)\",\n       \"stance\": \"supports\",\n       \"note\": \"'anord. hā- (*hanha-) in ha-mot \\\"Sprunggelenk, Fersengelenk\\\" ... ags. hoh \\\"Ferse\\\" (: *hanha-), anord. hæll \\\"Ferse\\\" (*hanhila-), ags. hēla m. \\\"Ferse\\\".'\"\n      }\n     ]\n    },\n    {\n     \"id\": 8,\n     \"lang\": \"English\",\n     \"words\": \"heel\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"English heel continues Old English hēla (Middle English hele, heele), from Proto-Germanic *hanhilōn-, contracted from *hōhila-, a diminutive of hōh 'heel, hock'; the cognates are Old Norse hæll, Old Frisian hēl(a), Dutch hiel. It is thus the same word as Nourai's Germanic hanhila, and its ultimate PIE source is *kenk-, the first half of the root box — this is the one branch of the entry for which the root box is unambiguously right.\",\n     \"derivation_fa\": \"واژهٔ انگلیسی heel دنبالهٔ انگلیسی کهن hēla (انگلیسی میانه hele) است، از ژرمنی آغازین *hanhilōn- (منقبض از *hōhila-)، مصغّرِ hōh «پاشنه»؛ هم‌ریشه‌های آن اسکاندیناوی کهن hæll، فریزی کهن hēl(a) و هلندی hiel‌اند. پس همان واژهٔ hanhila در جعبهٔ ژرمنی نمودار است و خاستگاه هندواروپایی آن *kenk- یعنی نیمهٔ نخست جعبهٔ ریشه است — و این تنها شاخه‌ای از این مدخل است که جعبهٔ ریشه برای آن بی‌چون‌وچرا درست است. ادعای نورایی درست است.\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\n       \"ref\": \"None\",\n       \"status\": \"not_checked\",\n       \"note\": \"The node carries no reference of its own; it inherits AHD from the Germanic parent, whose Watkins article names HEEL as the English derivative (checked at node 7).\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"KLN\",\n       \"where\": \"p.723 s.v. heel (KLN_1966.txt line 17435)\",\n       \"stance\": \"supports\",\n       \"note\": \"'heel, n., the hind part of the foot. — ME. hele, heele, fr. OE. hēla, contracted fr. OE. *hōhila, dimin. of OE. hōh, \\\"heel\\\"; rel. to ON. hæll, OFris. hēl, hēla, Du. hiel. See hock, \\\"joint\\\", and dimin. suff. -le.'\"\n      },\n      {\n       \"src\": \"AHD\",\n       \"where\": \"Watkins 1985 s.v. kenk-3 (AHD_watkins1985.txt line 615)\",\n       \"stance\": \"supports\",\n       \"note\": \"'2. Germanic *hanhilōn- in Old English hēla, heel: HEEL. [Pok. 3. kenk- 566.]'\"\n      }\n     ]\n    }\n   ]\n  }\n ]\n}\n"
}
```


### [2026-09-06T16:26:16.978Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe/data/verification/page-254.json (file state is current in your context — no need to Read it back)
```


## [2026-09-06T16:26:23.377Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -m json.tool data/verification/page-254.json > /dev/null && echo \"JSON OK\"; python3 tools/verify_check.py 254"
}
```


### [2026-09-06T16:26:26.878Z] TOOL RESULT

```
JSON OK
nodes verified: 14/14
node verdicts: {'transcription_suspect': 1, 'confirmed': 8, 'disputed': 2, 'plausible': 3}
root verdicts: {'confirmed': 1, 'plausible': 1}
ref checks: {'supports': 13, 'not_found': 2, 'not_checked': 4, 'partial': 2}
books consulted: {'supports': 25, 'partial': 8, 'silent': 2, 'contradicts': 3} | by book: {'KLN': 7, 'AHD': 4, 'WLD': 3, 'NYB': 3, 'PHD': 3, 'POK': 3, 'MON': 3, 'BRT': 2, 'HRN': 2, 'CHEUNG': 2, 'LAT': 2, 'HUB': 1, 'SOD': 1, 'ARY': 1, 'AFM': 1}
```


## [2026-09-06T16:26:46.656Z] AGENT

Page 254 (book p. 224) verified — `data/verification/page-254.json`, `verify_check.py 254` shows 0 PROBLEM lines.

**Counts:** 14/14 nodes. Node verdicts: confirmed 8, plausible 3, disputed 2, transcription_suspect 1. Root verdicts: confirmed 1 (Ken), plausible 1 (Kenk 1; Koksâ). Ref checks: 13 supports, 2 partial, 2 not_found, 4 not_checked. 15 books consulted.

**Flagged items**
- **disputed — Kenk 1/Koksâ, node 1 (Av. `kaša`, `karš`):** `kaša` "armpit" is the genuine Iranian witness for *koḱsā (Pok. 611, Bartholomae col. ~461), but `karš` "to pull" is a wholly different root — Cheung: PIE *kʷels- "to plough" (LIV 388f, Pok. 639); Pokorny himself files Av. karša- under *kʷel-1, pp. 639-640. Also, both words are Avestan; neither is Old Persian.
- **disputed — Kenk 1/Koksâ, node 2 (kešâleh, kešîdan, kaškŭl, tîr-kaš, kîš 1, kîš 2):** all six are built on the present stem kaš-/keš- of kešîdan < Av. karš-, so the whole box hangs off *kʷels-, not the root drawn. The internal Persian derivations are otherwise sound and BQT:1653/1657/1755 support them verbatim (incl. the Anvarî verse and the Kish-island "quiver-shaped" story, which is likely folk etymology).
- **transcription_suspect — Ken, node 1, `kaimyâ`:** `error_in: "book"`. The printed page really reads *kaimyâ*; the extraction is faithful. Correct form is *kainyâ* (Av. kainyā-), as printed by Walde-Pokorny I 397 and Nyberg.
- **Root box Kenk 1; Koksâ = plausible:** it merges two entries the handbooks keep apart (Pok. 566 kenk-3 "heel, knee" vs Pok. 611 koḱsā "hip"); Walde-Pokorny I 401 explicitly says joining them would require an ad-hoc assumption about the palatal. Nourai's POK:566 covers only the kenk- half.

**Reference problems (Nourai's own citations, not extraction errors)**
- `HRN:174` (node 3, kanîz): p.174 is "seyāl / sikār"; the right page is 194 no. 870, which he cites correctly on the parent node — looks like a 194→174 digit transposition.
- `KLN:735` (Av./OP node): p.735 is "hobble…hobo"; the supporting entry is p.736 s.v. *hock*.
- `FSF:275`: the local scan's pagination doesn't match (کنیزک sits at printed ~399); different printing.
- `VOP:296` (کوسن): Moshiri's dictionary has no copy anywhere online — not_checked.

**No extraction errors found.** The JSON matches the printed page throughout (checked against `data/verification/sources/refs/ocr/BOOK/254.png`, copied for audit).

Minor gloss slips in the book worth noting: OF `cuisse` is "thigh", not "cushion"; `coxînus` is reconstructed Vulgar/Medieval Latin *coxīnus, not attested Latin; Persian `kûsan` is a modern loan from French *coussin*, not from Old French.
