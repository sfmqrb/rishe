# Verification process log — verify-page-491


## [2026-09-14T03:08:40.717Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 491 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-491.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-491.json. Write /home/sfmqrb/git/rishe/data/verification/page-491.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 491` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T03:08:41.640Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T03:08:42.554Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T03:08:42.566Z] TOOL RESULT

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


## [2026-09-14T03:08:42.918Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-491.txt"
}
```


### [2026-09-14T03:08:42.946Z] TOOL RESULT

```
1	=== PDF page 491 (book page 461) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Swel 1 : to eat  (refs POK:1045)
4	#1 (parent #0) [Avestan] refs=POK:1045; AEF:10 | xvar 2, xwar : to eat ; avô-xvarena : animal shelter for drinking and eating ☞Ab 1
5	  #2 (parent #1) [Pahlavi] refs=MON:1455; BQT:788 | xvartan : to eat ; xvariš : stew ; av-xur : stable
6	  #3 (parent #1) [Persian] refs=MON:1455; FVF:221 | xordan «خوردن ( خور ، خوره )» : to eat ; xoreš «خورش» : stew ; xorangâh «خورنگاه ( خورنگه )» : dining room ☞Gwâ ; xavarnağ «خَوَرنَق» : royal dining room (castle) ; âxor «آخور ( آخُر ، آبخور )» : animals' "drinking place" | NOTE: IEC:1348 derives "xoreh: leprosy" from Indo-European root "Swer: to cut".
7	#4 (parent #0) [Germanic] refs=AHD | swel-han : to swallow
8	  #5 (parent #4) [English] refs=None | swallow
9	--- entry 1 ---
10	ROOT Swel 2 -> redirect to Sâwel
11	--- entry 2 ---
12	ROOT [Indo-European] Swen : to sound  (refs POK:1046)
13	#1 (parent #0) [Avestan] refs=POK:1046 | xvan, xwan : to call, sound
14	  #2 (parent #1) [Pahlavi] refs=BQT:784 | xvantan : to read, sing, call
15	  #3 (parent #1) [Persian] refs=HRN:110; BQT:784 | xândan «خواندن ( خوان ۲ )» : to read, sing, call ; xanîdan «خنیدن» : to echo, to be famous ; âxŭnd «آخوند» : preacher
16	#4 (parent #0) [Latin] refs=AHD | sonus : sound
17	  #5 (parent #4) [English] refs=None | sound, sonic
18	#6 (parent #0) [Germanic] refs=AHD | swanon : singer
19	  #7 (parent #6) [English] refs=None | swan
20	
```


## [2026-09-14T03:08:45.970Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-491.json",
 "description": "Read source JSON for page 491"
}
```


### [2026-09-14T03:08:46.011Z] TOOL RESULT

```
{
  "pdf_page": 491,
  "book_page": 461,
  "entries": [
    {
      "root": {
        "name": "Swel 1",
        "lang": "Indo-European",
        "refs": "POK:1045",
        "gloss": "to eat"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:1045; AEF:10",
          "words": [
            {"translit": "xvar 2, xwar", "gloss": "to eat", "script": null},
            {"translit": "avô-xvarena", "gloss": "animal shelter for drinking and eating", "script": null, "see": ["Ab 1"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "MON:1455; BQT:788",
          "words": [
            {"translit": "xvartan", "gloss": "to eat", "script": null},
            {"translit": "xvariš", "gloss": "stew", "script": null},
            {"translit": "av-xur", "gloss": "stable", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Persian",
          "refs": "MON:1455; FVF:221",
          "words": [
            {"translit": "xordan", "gloss": "to eat", "script": "خوردن ( خور ، خوره )"},
            {"translit": "xoreš", "gloss": "stew", "script": "خورش"},
            {"translit": "xorangâh", "gloss": "dining room", "script": "خورنگاه ( خورنگه )", "see": ["Gwâ"]},
            {"translit": "xavarnağ", "gloss": "royal dining room (castle)", "script": "خَوَرنَق"},
            {"translit": "âxor", "gloss": "animals' \"drinking place\"", "script": "آخور ( آخُر ، آبخور )"}
          ],
          "note": "IEC:1348 derives \"xoreh: leprosy\" from Indo-European root \"Swer: to cut\".",
          "quote": {"text": "برافراشت قصری که قصر خَوَرنَق - به بازار کالای آن گشت مغبون", "poet": "Sohbat Lârî"}
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "swel-han", "gloss": "to swallow", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "swallow", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Swel 2",
        "redirect": "Sâwel"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Swen",
        "lang": "Indo-European",
        "refs": "POK:1046",
        "gloss": "to sound"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:1046",
          "words": [
            {"translit": "xvan, xwan", "gloss": "to call, sound", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "BQT:784",
          "words": [
            {"translit": "xvantan", "gloss": "to read, sing, call", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Persian",
          "refs": "HRN:110; BQT:784",
          "words": [
            {"translit": "xândan", "gloss": "to read, sing, call", "script": "خواندن ( خوان ۲ )"},
            {"translit": "xanîdan", "gloss": "to echo, to be famous", "script": "خنیدن"},
            {"translit": "âxŭnd", "gloss": "preacher", "script": "آخوند"}
          ],
          "note": null,
          "quote": {"text": "خنیده به گیتی به مهر و وفا - زآهرمنی دور ودور از جفا", "poet": "Ferdowsî"}
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "sonus", "gloss": "sound", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "sound, sonic", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "swanon", "gloss": "singer", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "swan", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-14T03:08:48.044Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','AEF','MON','BQT','FVF','AHD','HRN','IEC','WLD','PHD','NYB','HUB','CHEUNG','ARY','KLN','SKT','BRT','KNT']:\n    v=d.get(k)\n    print(k, json.dumps(v, ensure_ascii=False)[:400] if v else 'MISSING')\n\""
}
```


### [2026-09-14T03:08:49.171Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
AEF {"title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence", "kind": "catalog", "url": "https://openlibrary.org/works/OL38785552W (vol. 1, 1356) ; 2015 complete ed. «فرهنگ ریشه
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
FVF {"title": "S.M.A. Emam Shushtari, Farhang-e Vazheha-ye Farsi dar Zaban-e Arabi, Anjoman-e Asar-e Melli 58, Tehran 1347/1968", "kind": "website", "url": "https://noorlib.ir/book/info/105056 (page viewer: https://noorlib.ir/book/view/105056?pageNumber=<N>&viewType=pdf) ; https://ketabnak.com/book/48613 (818 pp. PDF, login) ; http://parsianjoman.org/?p=1265 (download post)", "lookup_hint": "Alphabeti
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
CHEUNG MISSING
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
```


## [2026-09-14T03:08:57.693Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; ls data/verification/sources/refs/ | head -60; echo ---; python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','MON','BQT','AHD','HRN','IEC','PHD','NYB','HUB','ARY','KLN','BRT','SYN','WLD','FVF','AEF','SKT','WEB','FSD']:\n    v=d.get(k) or {}\n    print(k,'|',v.get('local_file'),'|',v.get('page_offset'))\n\""
}
```


## [2026-09-14T03:08:58.284Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '1,120p' data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-14T03:08:58.799Z] TOOL RESULT

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
KNT_full.txt
KNT.txt
LAM.txt
LAT.txt
LEW_1910.txt
LKT.txt
LST.txt
MON_part1.txt
MON_part2.txt
MPP.txt
---
POK | /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt | POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
MON | ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'] | None
BQT | ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'] | vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
AHD | /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt | 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.
HRN | /home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt | leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
IEC | /home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt | TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
PHD | /home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt | leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
NYB | /home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt | Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
HUB | /home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt | leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
ARY | ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt'] | printed page = pdf page + 1
KLN | /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt | KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
BRT | /home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt | Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
SYN | /home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt | leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
WLD | ['/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt'] | Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696).
FVF | None | None
AEF | None | None
SKT | /home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt | leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
WEB | /home/sfmqrb/git/rishe/data/verification/sources/refs/WEB_vol1.txt | not reliably detected (page_numbers.json sparse); grep headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
FSD | /home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt | vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably detected (pages ~ 700-1640) - grep the headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
```


### [2026-09-14T03:08:58.867Z] TOOL RESULT

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
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt` (truncated before the lexicon's h–z section, ~p. 208 on)
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT_full.txt` (complete archive.org djvu text — use this for lexicon pages 208–215: haumavarga-, siyamam, etc.)
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
```


## [2026-09-14T03:09:03.106Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for n in 279 280 281 282 283 284; do echo \"=== POK_03 leaf $n ===\"; awk 'BEGIN{RS=\"\\f\"} NR=='\"$n\"'' POK_03.txt | head -60; done 2>/dev/null | head -250"
}
```


### [2026-09-14T03:09:04.106Z] TOOL RESULT

```
=== POK_03 leaf 279 ===
�-
»m  a:  cymr.  sa/n, Kinnlade';  sefnig  ,Kehle',  acorn.  stefenic  , Gaumen', [•l)ret.  staffn,  nbret.  staofi  ds.
WP.  II  648.
1036  •
storos,  Stornos  (strnos?)  ,Star  und  Vögel  ähnlichen  Lauteindruckt« Lat.  sturnus,  -i  m.  ^Star',  aus  *strnos  oder  *stornos,  in  letzterem  J'tU. ags.  stearn  ,Seeschwalbe*,  apr.  starnite  ,Möwe'  (Ms.  stamite) ;  vgl.  ^^^^j^     ** strnad,  russ.  strendtka  , Goldammer*?  ^^
ahd.  star{a),  nhd.  Star,  aisl.  stari,  ags.  stc^r,  Demin.  stcerling  ^^ WP.  II  649,  WH.  II  610,  Frisk  173,  Vasmer  3,  26.
1.  streig-  ^stehenbleiben,  steckenbleiben,  innehaltend
Lat.  strigöj  -äre  , stehenbleiben,  innehalten  (besonders  von  Zugtii^r*«. wozu  wohl  auch  obstrigillö,  -äre  ,hemmend  entgegenstehen,  liinderiick  k, Wege  sein';  norw.  strika  (*strikön  =  strigäre)  ^einhalten,  stoppen*,  t<HW ^hinderlich',  strika  st.  V.  ^den  Lauf  hemmen,  stoppen* ;  lit.  straigjü  Ji* einstoßen',  stringü,  strigti , steckenbleiben',  lett.  striegt  und  strigt  ^einsj^^ (eig.  ,steckenbleiben'),  straignis  ,Morast';  slav.  *str^g-ti  in  poln.  «oilrfe ustrz(ic.  *-4
WP.  II  649,  WH.  II  604  f.,  Trautmann  290.  -v
2.  streig-  , steif,   straff'   und   ,zusammendrehen,  Strick';  wohl  Erweittru? von  ster-  , starrend  ...
Lat.  stringö,  -ere,  strictus  in  der  Bed.  ,straff  anziehen,  zusammenziii^ schnüren' ;
norw.  dial.  strlkja  ,die  Augen  aufsperren,   schwellen',  striky  strt aufgeschossener  Knabe';  *strikki-  ,Strick'  in  afries.  strik,  mnd.  strik" ahd.   mhd.   stric  [-ck-)   ßtrickf  \    davon   mnd.   stricken  , schnüren,  biaJtt stricken',    ahd.    strickan    , heften,    festschnüren,    stricken^,    ags. ,stricken,  ausbessern'.
WP.  II  649,  WH.  II  604  f.
3.  {s)treig-,  streid{h)-  ,zischen,  schwirren';  Schallwort.
Gr.  TQitwj  thqiya  ,zirpe,  schwirre,  knirsche',  Tqiyiidg  (neugebild oii6q)  m.  ,das  Zirpen,  Schwirren',  TQtylrj  , Seebarbe',  TgiyöXag  ,Knurrbll9- arglyS,  -yyög  f.,  auch  ct^i^,  (ttAi?;  atqlyXoq  Hes.  ,ein  Nachtvogel',: J*' strlx,  -gis  f.  , Ohreule',   strid{e)ö,  -ere,  strldl  ,zischen,  schwirren,  schrägt
WP.  II  651,  WH.  II  606.
strenk-,   streng-   ,straff,   beengt'   u.   dgl.   (wie  bei  ster-g-,  stre-g-,  s.
ster-  ,starren');  ,Strang,  zusammendrehen,  zusammenziehen'.       ^: Gr.  OTQayyög  ,gedreht';  durch  eine  schmale  Öffnung  tröpfelnd'  {(J^ft yovQia  ,Striktur'),  argay^,  -yyög  f.  ,aussickernder,  ausgedrückter  TropW» aTQayysvea&ai  ,sich  zusammendrehen,  hindurchpressen,  zögern',  ctQ
1037
^■'
L  gtrang;  Strick,  Schlinge',  argayyaXsvwy  -i?w,  -dw  (woraus  lat.  strangulo)
[  /^roßleS  (^'pQoyyvXog  (aus  *aTQayyvlog)  ^gedreht  =  rund^;
L    mir«    srengim    ,ziehe,    schleppe',    sreng    , Strick'
=== POK_03 leaf 280 ===
,    srincne    ,Nabelschnur'
^iftrenginiä);
lett.  stringt  , stramm  werden;  verdorren'  (,*sich  zusammenziehen*),  Strangs
^ti'^;  frisch'  (Lituanismus);
jjji  Germanischen   von   der  Wurzelform   auf   k   oder   gh:    aisl.    strengr
Schnur,    Strang,    Streifen,    schmaler    Strom*    {*strangi-),    ags.    streng  >m.
Schnur,  Strang',  ahd.  stranc  (-g-),  nhd.  Strang-,  Denominativ  aisl.  strengja
festbinden,  schließen' ;
^     mit  anderer  Bedeutung  aisl.   strangr  ,heftig,   stark,   streng,  hart',   ags.
•5.  sträng  ds.,   strenge  , streng',   mnd.   strenge,  ahd.   strengi  , scharf,   stark,
feUpfer,   streng',   und   ags.    strengan   ,hef estigen',    mhd.    strengen   , strecken,
^drängen',  nhd.  anstrengen-,
norw.  strungen  , steif  oder  beklemmt  im  Magen';  aisl.  strangi  m.  ,Baum-
itomm' ;
ron  der  Wurzelform  auf  idg.   Media:  aschwed.   strunker  , aufgerichtet,
fererade',  norw.  dän.  Strunk  ,ds.,  stolz',  norw.  Strünken  =  strungen  (s.  oben),
;jihd.   Strunk   ßtrunk'^    mnd.    Strunk    , Stengel',    mhd.    Strünken^    strunkein
btraucheln',  (könnten  auch  nasalierte  Formen  von  st{e)reu-g-  sein);
lett.  streükals  ,ein  Stück  verhärteten  Auswurfs'  (etwa  ,steif,  starr').
WP.  II  650  f.,  WH.  II  605.
\trep-,  (s)treb-  ,wild  lärmen,  schreien  u.  dgl.';  Schallwurzel. Lat.  strepöj  -ere  ,lärme,  schreie,  rausche' ;  vielleicht  der  ital.  FIN  Trehia ; v&X.prefa  , zanken',  dXsl.prapt  n.  , Geschwätz',  ags.  prceft  n.  , Zwist,  Zank', md.  drevelinge  ds.  (mit  p :  aisl.  Jjrapr  , Schwätzer',  pray  n.  ,garrulitas') ; vgl.  3.  {s)treig-j  streid(hy  , zischen,  schwirren'  und  lat.  stertö  , schnarche'. WP.  II  649  f.,  WH.  II  602.
I-  ,greis,  alt';  nur  kelt.  und  balto-slav.
Air.   sruith   ,alt,    ehrwürdig'  (*stru-ti-s),  acymr.   strutiu  gl.   ,antiquam'; it.  strüjus  , Greis';  aksl.  stryjh  ,patruus',  strynja  ,amita'.
WP.  II  651,  Trautmann  290,  Vasmer  3,  29.
so-  ,wohl,  gut'  als  1.  Kompositionsglied;  su-bhago-  ,beglückend'. Ai.  SU-,  av.  /m-,  apers.  u-,  z.  B.  in  ai.  su-drü-  , starkes   Holz'  su-bhdga- [iClticklich,  beglückend',  av.  hu-baya-  , gutes  Eheglück  gewährend'; ?r.  vyLTJg  ,gesund'  (*su-gni{es  , wohllebend*) ;
gall.  SU-    (z.  B.   Su-carus  =)    cymr.    hy-gar   , Hebens  würdig',   corn.   hy-, fet,  he-
=== POK_03 leaf 281 ===
,  air.  su-,  so-  (z.  B.  su-thain  ,ewig',  so-scel{a)e  , Evangelium') ;
1038  •
germ.  su-  in  Su-gamhri  VN,   aisl.   sü-svort  f.   ,Schwarzamsel'  (,^ Schwarze');
lit.  südrus  ,gei\,  üppig*;  aksl.  s^drav^  „tyLrjg"  ,öech.  zdravy  (y^^  *_ ai.  su-drü-)  usw.;  slav.  '^s-bbozhje,  cech.  zhozi  ^Besitztum'  aus  *si>-log^  t^^ suhhdga-,  oben  S.  107);
SU-  ist  Tief  stufe  zu  *swe-  (oben  S.  882  f.);  vgl.  ai.  sva-  in  sva-dhä  ^  g^. ,süßer  Trank'  (oben  S.  241),  svd-dhita-  =  sü-dhita-  ,fest,  gesund*;
WH.  II  512,  E.  Fraenkel  Mel.  Pedersen  443  ff.,  Vasmer  1,  450  f.
sü-Sf  suu-ös  , Hausschwein,  Sau';  erweitert  su-ko-]  suuino-  ,zum  Scl»W|^ gehörig'.  -
Av.  hü  (Gen.  Sg.  für  *huvö)  , Schwein';  gr.  ^g,  vög,  Akk.  h  m.  J^
f.  ,Sau'  (davon  ilaiva  f.  , Hyäne')  neben  (xvg,  avög  ds. ;  dazu  ovfjlai' t4n^
ßoQßoQwösig  Hes. ;  av(pE{C)6g,  ov(p6g  m.  ^Schweinestall  {*-q)£J^iog,  m
idg.  bheu-j  oben  S.  146 ff.);  Sternbild  der  'Yddsg  , Gruppe  von  Schi
vgl.  gr.  lak.  aUa'j
alb.  thi  jSchwein';  lat.  süSj  suis  ,Schwein',  umbr.  sif  ,sues',  «im' sufum,  sorsorrij  sorsalem  ^suillum'  {^sü-do-,  *sü-dali-)]
gall.  *8u-tegis  .Schweinestall'  (M.-L.  8492);
ahd.  ags.  sü,  aisl.  syr  ,Sau';
lett.  suvensj  sivens  ,Ferkel*  (unklar  apr.  seweynis  , Schweinestall*);  tocL  I* 8UW0  ^Schwein';
adjektivische  12 o- Ableitungen:  einerseits  gr.  (spät)  trjvög  ,vom  Schw^*^,^ andererseits  (ursprachlich)  lat.  sulnus  ds.,  aksl.  svim  ds.  =  lett.  tiHNü  ^ ,beschmutzt';  toch.  B  swänana  misa  , Schweinefleisch';
substantiviert  got.  swein,  aisl.  suln,  ags.  ahd.  swln  , Schwein';  aksl.  mn^ ,Schwein'  wohl  aus  *svml  (fem.  zu  svim)  umgebildet.
k-Ableitungen :
ai.  sükara-  m.  ,Eber,  Schwein'  (umgedeutet  als  ,>Sw-macher^);  mper«.  fr«\ osset.  x«i  ds. ;  lat.  sucula  , junge  Sau';  mit  expressiver  Gemination ySjH *sw/i:Ä:o- , Seh  wein,  (Schweine-)  Schnauze,  Pflugschar'  in  air.  socc  sdil  flul^^ Schwein'  (ein  Fisch),  mir.  soc  m.  , Pflugschar,  Schnauze  (des  Schweiata^, air.  FIN  -Socc;  cymr.  hwch  m.  f.,  später  nur  f.  , Schwein',  com.  hochf% liouc'h,  hoc'h  m.  , Seh  wein';  aus  dem  Gallo-Lat.  stammen  cymr.  swch, soch,  bret.  souc'h  und  frz.  soc  , Pflugschar';
ags.  sugu  ,Sau',  as.  suga,  mnd.  soge^  nhd.   Schwab,  suge  ,Sau';  mit  ^ pressiver  Gemination  norw.  schwed.  s
=== POK_03 leaf 282 ===
ugga,  mnd.  sugge.
WP.  II  512  f.,  WH.  II  635  ff.,  Trautmann  294,  Vasmer  2,  593,  Benve»^' BSL  45,   74 f..    90,  Thieme,   Heimat   d.   idg.   Gemeinsprache  26  f.,  8^^
1039
^^bl  ursprüngl.  .Gebärerin',  zu  2.  seu- :  sü~  ^gebären'  (oben  S.  913 f.);  vgl. ^' -j.  herit  ^Sau'  (*bherenti) ]  oder  aber  lautnachahmend?
.^^  soU'TO-  ,sauer,  salzig,  bitter',  zunächst  von  käsig  Gerinnendem^ ■^     schleimig  Nassem;  auch  in  Flußnamen;  Wurzel  seu(a)-,  sou(a)-:sa-.
^isl.  surr  ,sauer,  scharf,  m.  , Sauerteig',  mnd.  mhd.  sür  n.  ,Bitterkeit'; ^1^  syra  f.  , saure  Milch',  ags.  syring  ds.,  ahd.  sürl  ßäure^-^  ahd.  ags.  sür tauer%  aisl.  sür-eygr,  ahd.  sür-ougi,  ags.  sür-lege  ,trief äugig' ;  vgl.  toch.  B ^rrna  , Augenkrankheit';
lit.  suras  jSalzig',  lett.  surs  , salzig,  bitter*,  lit.  suris  m.  ,Käse',  apr.  suris
ds.;
aksl.  syn>  ,feucht',  russ.  syröj  ,feucht,  roh,  sauer*;  substantiviert  aksL pp^  russ.  syr  ,Käse';
ablaut.  aisl.  saurr  m.  , Schmutz,  tier.  Same' ;  abg.  surovz  ,roh*,  russ. turövyj  ,rauh,  roh'  (*sou-ro-)]
vgl.  die  FIN  kelt.  Süra^  nhd.  Sauer,  Sür,  apr.  Sure^  lett.  Sür-wpe,  und ^en  ON  2vQdyL0vGai  PI.  ,Syrakus'  (Sizilien),  mit  «^Ableitung  zu  IvQayid) ^'ame  eines  Sumpfes.
WP.  II  513,  Trautmann  293 f.,  Vasmer  3,  49,  58;  vielleicht  zu  1.  seu(9)- ,Saft'  (oben  S.  912 f.);  über  , Milch'  zu:  ,geronnene,  saure  Milch'.
(05-  Schallnachahmung  für  , sausen';  nur  germ.  und  slav.
Ahd.  süsö7b  jSausen',  mnd.  süsen,  schwed.  susa,  dän.  suse  ds. ;
aksl.  sysati  ,s2iUseTi,  pfeifen'  (Schallkorrektur  für  lautgesetzliches  *sych-)- iruss.  susol  , Zieselmaus,  Hausratte',  bulg.  szsel  ds. ;  s^sham  ^zische';  vgl. lett.  susuris  , Spitzmaus',  susers  , Haselmaus'.
WP.  II  514,  Trautmann  294,  Vasmer  3,  50  f.
Is-    ,Erzeuger'^  süsä  ,die  Gebärende';  nur  altind.  und  alban. i  Ai.  süh  ^Erzeuger';  aXh. gjysh  , Großvater'  (*sü-s-io-),  ursprüngl.  , Erzeuger'; tregjysh  , Urgroßvater',  gjyshe  , Großmutter'  (*sü-s-ie). Jokl.  Ling.-kult.  Untersuchungen  28ff. ;  zu  seu9  :  sü-,  oben  S.  913  f.
^W-  ,süß;  an  etwas  Geschmack,  Freude  finden'.
I.  suädü-s  ,süß':  ai.  svädü-,  f.  svädvi  ,süß,  lieblich';   gr.   i^^ug,   f.   -eZa
(*-5/ta),  -V,  dor.  advg  ,süß' ;  mit  Formans  -mo- :  ädvi,iog,  hom.  fjdv{.iog  ^ange-
aelim';  lat.  suävis  (*suäduis)  ,süß';  as.  swöti,   ahd.   suozi^  ags.   swet
=== POK_03 leaf 283 ===
e,   aisl.
■^tr  ,süß';  gall.  PN  SuadurJx,  -genus,  ir.  Sadb  f.  PN;  über  got.  sutis  , ruhige
«anff,  s.  Mayrhofer  KZ  71,  74 f.  u.  73,  116 f.
Kompar.  Superl.  ai.  svddlyas-,  gr.  ijdlwv',  ai.  svädistha-  ==  gr.  fjöiCTog]
1040  •
2.  suädos-  n.  ^Süßigkeit,  Wohlgefallen' :  ved.  prd-svädas-  »Hebli^ nehmS  ^ehijdrjg  »honigsüß^  ^dog  n.  ,Essig'  (gr.  ^öog  n.  ,Vorteü',  bleibt  ^^
5.  suädonom,  -ä:  ai.  svädanam,  gr.  i^dovij  f.  ,Lust^
4.  Verba  und  andere  Nominalbildungen:
ai.  ved.  svädate  ,ist  erfreut,  genießt*  =  gr.  ^So^xai  (böot.  S&dofit)  t*^ mich';  ^
av.  x'^äs^ö  , durch  Kochen  gar  (schmackhaft)  gemacht,  gekocbt*^» svättd-   ,gewürzt';   ai.   svdda-   m.   , Geschmack,  Wohlgeschmack*,  bit  \p|^ ,Salz'  (Mittelbegriff  ,WürzeO;
Kausat.  bzw.  Intensivum  sväddyati  (=  lat.  suadeö,  s.  u.)  und  9Vüdd'--^^p ,schmackhaft,   annehmbar   machen;   kosten,   genießen*,  tiefstufig  tU^L., ,gehörig  einrichten,  gut  machen,  fertigmachen  =  töten,  vemicbteti* derselben  Ablautstufe  Perf.  susüdimdj  südä-  m.  ,Koch',  lit.  ^cZyH,gol,j
mit  analog,  ä:  svddati  , macht  schmackhaft,  würzt*,  svddate  ,i Partiz.  svattd-'j  nasaliert  av.  x"andra-hara-  , angenehmes  tuend afgh.  x^and  ,Wohlgeschmack,  Vergnügen'  (vgl.  gr.  ävödva))]      "^^
Gr.  fjdofMXL  (s.  oben);  ^a^evog  jerfreut',  nicht  sicher  hierher zum  s- Aorist  ijaaro  (der  Lenis  unerklärt);  *afäde(jj,  ^arjöso)  (boi <7eis,  ddrjXÖTsg)  ,bin  verdrossen',  lokr.  J^sSaörj'KÖTa  (ß  oder  ^?); falle',  Aor.  hom.  sUade,  gortyn.  eJ^aös,  Perf.  eaöa  (:  ai.  sa8vadi\\ ,mißfalle'  {dq)aÖLa  ,Feindschaft'),  ion.  &dog  m.  , Beschluß',  Sörj^ia a-öd^äörjg^  ion.  avrcbdrjg  , anmaßend,  selbstgefällig'  {*ai)Tofdör]g)y  äSaSf^j^. drossen',  wovon  daöetv '  dxlslv,  drtOQetv  Photios ;  dieser  -e^-St.  Sdog  iit  11^ gr.  Neuschöpfung  von  ävöavo)  aus;  "        "-^Jf;
lat.  suädeö,  -ere  ,rate'  (d.  i.  ,mache  einem  etwas  gefallen');  --?l'^,
lit.  südyti  , würzen,  salzen';  *;7^^
vielleicht  hierher  ags.  swatan  PL  ,Bier',  schott.  swats  , frisch  gebflili^ Bier'.  :C
WP.  II  516  f.,  WH.  II  611  f.,  Frisk  104,  166,  184  f.  i^f
suard-  ,lachen'?
aaqddvLog  ,höhnisch,  spöttisch',  aagdl^eiv  ,hohnlachen' ;  cymr.  eh com.  hwertliirij  mbret.  huersin  ,lachen'. WP.  II  517.
ßuei-,  sui-  ,zischen,  pfeifen',  Schallwort;  erweitert  sueizd-)  ital siieighl-. Idg.  Alters  ist  *sueizdö:   ai.   Jc?vedatij   ksvedati   ,saust,  braust, (wenn  Jcs-  Schallverstärkung  eines  aus  *svaizdati  assimilierten  *i air.  set-  ,(ein  Instrument)  blasen',  mir.   airfitiud  , durch  Musik
1041
^r.  Ind  fet  .sibilus*,  nir.  fead  ,a  whistle'  (*swizdä),  mir.  fetdn  »fistula', ^yinr.  chiüythu  .wehen,  (ein  Instrum
=== POK_03 leaf 284 ===
ent)  blasen^  chwyth  ,das  Blasen^ Ay^ytJiell  »Pfeife'  (chwib  ds.,  Kreuzung  von  chwyth  mit  pib  ,Pfeife'  aus t^l  pip^)i  corn.  lühythe,  whethe,  bret.  c'houeza  »blasen';  aksl.  svistatij  zviz- iflti  ;Sibiläre^  (kann  aus  *svizdati  assimil.  sein);
rr.  <y^^^  ,zische',  Aor.  eai^a  {ai^Lg,  aiyfxög  ,das  Zischen')  ist  ähnliche gchallbil<i^^&  wie  lett.  slkt  ds.;
ebenso  lat.  sibüöj  -äre  ,zischen,  pfeifen*,  slUlus  ,zischend;  das  Zischen', Igkundär  slfilöj  sißlus,  vgl.  schwundstuf.  got.  swiglön  ,die  Flöte  blasen, •feifenS  ahd.  sweglön  ds.,  swegala  ,Flöte*  (*suighlä-)j
j^  jhnhch,  aber  ohne  geschichtlichen  Zusammenhang  mit  obigen  Worten Iflch  npers.  sifllden  .pfeifen,  zwitschern*,  aksl.  sipota  .Heiserkeit*,  sipm^ti
)iser  werden',  öech.  sipati  ,zischen,  heiser  werden'.
;^P.  I  215,  II  517 f.,  WH.  II  531  f.,  Vasmer  2,  594f.
f(/)-  ,biegen,  drehen,  schwingen';  sui-lo-,  sui-mo-  ,Drehung'  (s.  auch seu-  und  sueng-  ,biegen*). I  Gr.  ai^og  .aufwärts  gebogen,  stumpfnasig,  spöttisch'  (dazu  trix/dg  ,ekel. les  tadelnd'?);  vielleicht  auch  aiQÖg  .Grube*  (*Einbiegung?); ,cymr.  chwid  .lebhafte  Wendung,  Kunstgriff',  chwidl  .sich  im  Kreise jhend,  schwindlig',  chwidr  .schnell,  flüchtig,  übereilt*;  chwim  m.  i^sul-smo-) jwegung,  Antrieb*,  Adj.  .schnell',  chwyf  m.  ,Bewegung'  {*sui-mo-j  vgl. iten  germ.  swXm-),  chwyfio  ,movere',  bret.  ftnval,  gwiüval  ,sich  bewegen, Iren* ;
cymr.  chwyn  ,Bewegung*.  chwil  {^ml-lo-)  ,sich  schnell  drehend';  chwyl id  chwel  {*mi-to-,  -lä  vgl.  norw.  svil)  ,Wendung,  Lauf*,  corn.  wheyl Irbeit',  air.  sei  .Wendung,  Drehung,  Zeitraum',  mir.  des-sel  .Wendung ;h  rechts',  tuath-hil  ,Wendung  nach  links'; mnd.  siväien,  sweimen  .sich  schwingen*;  als  Partiz.  aisl.  svad  n.  ,das ifileiten',  (^sud-to-),  svada  .gleiten',  ags.  S2^;a(f2aw  .(ein)  wickeln',  engl.  swath{e)j id.  mhd.  sioade  .Reihe  von  gemähtem  Gras,  Schiuaden^  ] norw.  svlma  .schwanken,
```


## [2026-09-14T03:09:09.233Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for n in 285 286 287; do echo \"=== POK_03 leaf $n ===\"; awk 'BEGIN{RS=\"\\f\"} NR=='\"$n\"'' POK_03.txt; done 2>/dev/null"
}
```


### [2026-09-14T03:09:10.288Z] TOOL RESULT

```
=== POK_03 leaf 285 ===
taumeln',  mhd.  swlmen  ds. ;  ags.  swlma  m. ihwindel,  Ohnmacht*,  aisl.  svlmij  ndl.  zwijm  ds. ;  mhd.  swlmel,  swimmel tWindel';  aisl.  sveimr  m..  sveim  n.  , Getümmel,  Tumult',  sveima  ,um- siehen',  mhd.  sweim  m.  ,das  Schweben,  Schweifen,  Schwingen',  sweimen ih  schwingen,  schwanken';  norw.  svil  n.  , Spirale;  der  krause  Samen- itel  dorschartiger  Fische';  nd.  svnr  , Schwung,  Drehung,  Bummeln', ?*"««  ,sich  schwingend  bewegen,  umherfliegen,  in  Saus  und  Braus  leben*.
\*^eib~ :  av.  xsvaewayat-aHra-  .die  Peitsche  schwingend*,  xSviwra-  .flink' ; 'midja-sweipains  , Sintflut'  (eig.  ,Fegung  der  Mitte*);  aisl.  sveipa  , werfen,
66
1042  ,
umhüllen*,  ags.  swäpan  ,schwingen,  fegen,  treiben*,  as.  sicep  f ahd.  sweifan  , schwingen,  schweifen,  streiten',  5i/;ezy  ,Umschwunp' =  aisl.  svei'pr  ,Band,  Schlingung;  gekräuseltes  Haar*,  aisl.  svipa
sueid-:   in   lit.    sviesti,    lett.    sviest  ^werfen',   Frequentativ  Hl' lett.   svaXdit   ,wiederholt   schleudern*;    ob   lett.   svaXdit  , salben (unten  unter  suBid-)  hierher?
sueig-:  germ.  auch  »nachgeben,  nachlassen'  (von  sui-  ,schwm( gegangen)  ,(listig)  etwas  drehen,  ausweichen,  Trug'  u.  dgl. :  ahdJ ags.  sttncian  , schweifen,  wandern,   betrügen',  aisl.  svzkva  siJküa svikja  , betrügen,  verraten',  ags.  swican  »verlassen,  betrügen' gehen,  wandern',  as.  swlan  ds.  ,ermatten';  ahd.  swihhan  ,ermÄtt '     lassen,  verlassen*,  mhd.  swlch  m.  , Zeitlauf',  ä-swich  ,heimlicher sweichen  ,ermatten*;  aisl.  svik  n.   , Verrat,  Betrug*,  ags.  svno  n^ biswih  m.  ds. ;
lit.  svaigti  ,Schwindel  bekommen',  svaiginUi  ,sch windelig  umHi russ.  svigdt'  ,herumtreiben^;
toch.  A  wäweJcu  , gelogen',  B  waike  ,Lüge'.
sueik-i    aisl.    sveigr   ,biegsam',    m.   ,biegsamer   Stengel',  stü svnga,  sveg  ,sich   biegen',   Kaus.   aisl.  sveigja  , biegen',  Pass.* beugen,  nachgehen*,  svigi  m.  ,biegsamer  Stengel*;  ahd.  sweiga  ^^ (♦Geflecht).  ,.y/
sueip-:  aisl.  svifa  ,schwingen,  drehen,  umherschweifen,  schwelofi Stolfan  jdrehen,  fegen,  wenden  (engl,  stuiß  ,schnell'),  schwenkoe*, sueifla  ,schwingen*,  mhd.  swibeln,  swivelen  ,taumeln*,  ahd.  swethlhi  Ach^ schwingen',  sweben  , schweben'.  ^
lett.  sväipit  ,peitschen',  svipst(ijf)s  ,Hasenfuß,  Zierbengel'.  '^'
WP.  II  518  ff.,  Vasmer  2,  591  f.,  Johannesson  794 ff.  ''^''
-■    ■   •  m
it\ 1.  sueid-  ,glänzen,  schimmern*.  *  J
Av.    x^'aena-   ,glühend,   lohend*    (*x''aedna-) ;   lat.    sidus,    -eriif conslderäre  , betrachten',  desideräre  ,verlangen*;  -^\
lit.  svidüs  ,blank,  glänzend',  svysti  ,zu  gl
=== POK_03 leaf 286 ===
änzen  beginnen*,  ,?»Ü% ,glänzen',  lett.  svist  ,anbrechen,  vom  Tage*,  svdidlt  ,salben'  (^Ig^^ machen*) ;
ein  ähnliches  *sueit-,  aber  in  der  Bed.  ,sengen,  brennen'  iiaTSii- ahd.  swldan  ,brennen';  dazu  wohl  als  Aoristpräs.  ahd.  8wedan*ßch^ verbrennen*  und  mit  Ablautentgleisung  ags.  swadul  ,Rauch*,  xolfd*  f^ ,RauchscÄM;a(ien,  Dunst*  u.  dgl.
WP.  II  520  f.,  WH.  II  534,  Trautmann  296.
1043
gVieid'  ^schwitzen';  sueides-  n.,  su{e)id-ro-,  suoido-  ,Schweiß^ ^i.  svidyatij  svidate  ,schwitzt*,  svida-  m.  =  av.  xvaeda- , Schweiß*  (=  germ.
^m-  l^ii^t-T^,  Gen.  -an  ,Schweiß^  {rt  aus  dr^  vgl.  gv.  \dqwg,  lett.  sviec^W); -y.  (5)1(^04;  (ion.)  n.  , Schweiß',  hom.  usw.  {e)idiu},  att.  id/w  ,schwitze^ y^^  'wrog,  att.  id^wg  wohl  nach  eigcog,  -cjrog  , Moder'  aus  dem  ursprüngl. .^.St.  von  hom.  Dat.  Iöqm,  Akk.  Iöqco-  (erwachsen  aus  idg.  *suidro-)  Idgcbo) ^hvvitze'  {*ldQwa-iü));
jlb.  dirse^  djerse  ^Schweiß',  djers  ,schwitze'  (mit  s  aus  ti  im  Präs.  *sui-
['     lat.  swc?or,  -öWs  ^Schweiß'  i^suoidös),  südo,  -äre  »Schwitzen*; kymr.  chwysj  corn.  tüÄys,  bret.  c'houez  , Schweißt  (*swi£Zso-); 3gs.   swätj    as.   si<7g^^   ahd.    s?^e22   m.   ßchweiß',  aisl.   svei^i  m.   ds.;   ahd. tjtizzen  (=  ai.  svidyati)  ,schwitzen^,  Kaus.-Iter.  ahd.  sweizzan,  mhd.  sweizen ^•jScliweiß  vergießen,  bluten,  naß  werden',  mhd.  auch  ,heiß  machen,  rösten, 0 Gluthitze  aneinanderhämmern,  schweißen^  (=&[.  sveddyati , läßt  schwitzen'); ;,  lett.   sviedri  PL   , Schweiß',    svhtUj    svist   , schwitzen*,    svtdet   ,schwitzen jiachen'. l  WP.  II  521,  WH.  II  623,  Trautmann  295.
id'  ,Milch'.
Ai.   ksvidyati,   ksvedate   (unbel.)   ,wird   feucht';    av.    xSvld-   m.    , Milch*, l'Tielleicht  zu  lit.  sviesti  ,schmieren*,  lett.   svatdit  ds.,  lit.  sviestas  ,Butter', Ifctt.  svie(k)st  ds. I  WP  II  521,  WH.  II  624;  s.  auch  sueid-  oben  S.  1042,  Z.  5.
ik-  ,(gut)  riechen';  nur  brit.  und  westgerm.
Cjmr.  chweg  ,süß,  angenehm',  corn.  whek^  bret.  c'houek-  cymr.  chwaeth .Ifniekto-)  ^Geschmack*;  ahd.  swehhan  ,riechen,  stinken,  hervorquellen*; iit  Geminata  ahd.  swekJie,  sueckia  PI.  ,odores',  as.  swec  , Geruch,  Duft', l§8.  sioecc,  swcBcc  , Geschmack,  Geruch,  Duft',  sweccan  , riechen'.
WP.  II  521.
ikrü-  ,Mutter  des  Ehemannes*,  davon  abgeleitet  suekuro-  (aus  *suekruro- dissimiliert)  , Vater  des  Ehemannes';  suekuro-  ,zum  Schwiegervater gehörig'.
I  Ai.   svdsura-j    av.    x^asura-  
=== POK_03 leaf 287 ===
  »Schwiegervater',    ai.    ivasrü-    ,Schwieger- |tntter';  npers.  x'^^''^  <Is.;
arm.  skesur  , Schwiegermutter*  aus  *kue]curä)j  darnach  skesrair  ,Schwie- j^rvater',  eigentlich  ,Mann  der  Schwiegermutter*;  gr.  e^vgög  ,Schwieger- per,  u.  zw.  der  Vater  des  Ehemanns*,  ky.vqä  »Schwiegermutter*;  alb.  vjeherr
66*
1044
, Schwiegervater^,  vjeherre  , Schwiegermutter^;   lat.    socer,   -eri  ßf,]^^
■^HraPHp;
germutter*,  neugebildet  cymr.  chwegrwn,  corn.  hwigeren  ,Schwi
ahd.   swehuTj   ags.   sweor  ,SchwäherS    ahd.    swigar,   ags.    -^^e^er  "(♦^Z*^
, Schwiegermutter';  ,^
got.  swaihrö  =  anord.  svWi^a  »Schwiegermutter'  (*swehrön'),  nerutAa^. got.  swaihra  »Schwiegervater*  {*siüehran-),  wie  auch  nhd.  ^chutUo^nm^ nach  Schwieger  {mutier)  für  Schwäher;  *™^.
lit.  Sesuras  ^Schwiegervater' ;  aksl.  svehry  , Schwiegermutter*  (4^4 Dissimil.   gegen   den   Anlaut   nicht  zu  -sr-  geworden),  wonach  m.  nJU ,  Schwiegervater* ;  |g&
dehnstufig:  ai.  §vä§ura-  ,zum  Schwiegervater  gehörig*,  ahd^Efey— .. {*suekur6s)  ,Schwager  (*Sohn  des  Schwiegervaters)^  auch  ,Schwir^^^* Schwiegersohn^
WP.  II  521  f.,  WH.  550  f.,  Trautmann  295  f.,  Vasmer  2,  588
suekSf  seks,  kseks,  ksueks,  ueks  (:  uks)  ,sechs'.
Ai.  sdt  (aus  sats),  av.  x§va§]  arm.  vec  (in  vat'sun  ,60*  ist  a  auj  «  ^^ gelautet) ;  gr.  €?,  dial.  /f?  (knidisch  ^earqi^  ,sechszeilige  Gerste',  tU{^S|| aus  *?«?);  alb.  gjashte;  lat.  sex-,  air.  se  ,6*,  seser  ,6  Mann*,  rnör-fe$er  ,mii seviratus,  7  Mann',  cymr.  usw.  chwech  ,6' ;  got.  saihs,  aisl.  «ea?,  ahd.  ^n^ lit.  flektiert  ieB;  aksl.  äesth  (=  ai.  sasti-)]  toch.  A  säÄ:,  B  ^Jfcatj  y*}.  %^ sedecim:  ai.  södaSa  16  (av.  xSvasdasa-  ,der  16.*).
Ordinale:  ai.  sa§thd-j  av.  xHva-]  arm.  t7eceror(Z;  gr.  gWog;  alb.  t-o/a«  v  «' i-gjashte',  illyr.  Sestus]  lat.  sextus,  sestus  (SesHus,  osk.  Seariegj  umbr.  i#  * tasiaru  ,sextantariärum' ;   idg.  wohl  *5(«)eto5,  im   Lat.   und  Oer£B Eindringen  des  5  aus  der  Grundzahl) ;  gall.  suexos,  air.  sessed^  cymr«  iW cÄed;  got.  saihsta,  ahd.  sehsto,  sehto,  aisl.  je^^e;  lit.  §e§tas^  apr.  m.  II^K^ uschts,  vgl.  alit.  wiios-  ^Wochenbett*  (apr.  Lw.),  echt  lit.  i??iiw  ds.J ^cs^i;  toch.  A  sÄJäs^,  B  §Jcaste.
WP.  II  522  f.,  WH.  II  528  f.,  Wackernagel-Debrunner  III  31 TPS  1944,  54  f.
s{u)ek"o-s  ,pflanzlicher  Saft;  Harz'.
Gr.  ÖTtög  , Pflanzensaft,  Baumharz',  örcoeig  , saftig',  wovon  der  Ol (inschr.  hoTtowlmv)  ]
lett.  svakas  f.  PL,  umgelautet  sveWis,  PL  sveTci  ,Harz,  Gummi',  lit  ***'^J PL,  apr.  sackis  ds.  ,Saft  der  Pflanzen  und  Früc
```


## [2026-09-14T03:09:13.656Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for n in 288 289 290; do echo \"=== POK_03 leaf $n ===\"; awk 'BEGIN{RS=\"\\f\"} NR=='\"$n\"'' POK_03.txt; done 2>/dev/null"
}
```


### [2026-09-14T03:09:14.642Z] TOOL RESULT

```
=== POK_03 leaf 288 ===
hte*;  mit  ÜbertrÄ^f  il|[ tierische  russ.  osoka  ,Bluteiter',  klr.  posoJca  ,Blut  eines  Tieres'  os«   ' gjak  ,Blut'.
WP.  II  515  f.,  WH.  II  623,  Trautmann  248,  Vasmer  2,  688,
1045
^y^el^(k-), schlingen,  essen,  trinken*?  Nur  iran.  und  germ.? ^v.  x^'ar-  ^genießen,  verzehren* ;  engl,  swül  ,verschlingen,  gierig  trinken' Uüch  jSpülen',  wie  ags.  swillan,  swillian),  mnd.  swellen  ,üppig  leben',  isl. ^llr  ,Trinkgelage' ;  norw.  soll  ,Milch  mit  Brotbrocken*,  aisl.  hräsollr  ,Blut* /  ♦naßklumpiges*) ;  aisl.  sollr  , Spültrank  für  Schweine'  (welche  Bed.  auch gijo-1.  sivill  hat);
yon  einer  Erweiterung  suelk- :  ahd.  swelhan  und  swelgan  ,verschlucken, trinken',  ags.  swelgan,  aisl.  svelga,  nhd.  schwelgen-,  aisl.  svelgr  , Stromwirbel, fresser';  mnd.  mhd.  swalch  ^Schlund',  nhd.  Schwalch  ^Öffnung  des  Schmelz- ofens^  nd.  swalgen  ^ersticken';  schwed.  svalg,  svulg  , Schlund',  aisl.  sylgr ^Schluck'. '  WP.  11  530,  Specht  KZ  66,  25 f.;  vgl.  oben  S.  901  und  unten  s.  v.  uelk-.
Süd-  , schwelen,  brennen'.
Ai.  svdrati  ,leuchtet,  scheint';  svargd-  m.  , Himmel*;
gr.  s'iXrjj  slXtjj  sXr]  f.  , Sonnenwärme,  Sonnenlicht',  ysXav  aiyfjv  'fjXiov,  lak. ßila  Hes.,  iXdvr]  ,Fackel',  assim.  iXevr]  Hes.,  '^EXevrj  ursprüngl.  eine  Licht- göttin; schwundstufig  äXia  f.  ,Sonnenwärme',  äXsalvo)  , erwärme',  dXeeivög [ieiß^  äXv'AQÖg  (Nikand.)  ,warm';
unsicher  Zugehörigkeit  von  aiXag  n.  ,Glanz',  asXrjvT],  äol.  asXdwa  ,Mond' [*osXaava),  aeXayelv  ,glänzen';
ags.  swelan  st.  V.  ,(ver)  brennen,  sich  entzünden',  mnd.  swelen  schw.  V. (nhd.  schwelen),  ahd.  sioilizön]  aisl.  svalr  ,kalt'  (eigentlich  , sengend'),  mnd. twalm  , Qualm',  ags.  swol  n.  (*swula-),  sw(e)olod{a)  m.  ,das  Brennen,  Hitze'; dehnstufig  *swel-  in  aisl.  sv^la  , räuchern',  f.  ,dicker  Rauch',  ags.  swälan t,7erbrennen  (trans.)*,  und  *swöl-  in  nd.  swöl  , schwül'  (umlaut.  nhd.  schwül), fndl.  zwoel,  zoel  ds.;  —  mit  germ.  k:  nd.  swalk  , Dampf,  Rauch*,  mhd.  swelk ^,welk,  dürr',  ahd.  swelchen,  mhd.  swelken  ,welk  werden'.  —  Ein  (i-Präs. fb  ahd.  swelzan  , brennen,  verbrennen  (intr.)',  wozu  vermutlich  als  ,ver- iichmachten'  (vgl.  engl,  sweltry,  sultry  ,drückend  heiß'),  ags.  a
=== POK_03 leaf 289 ===
s.,  sweltan jt.  V.  »sterben',  mndl.  swelten,  aisl.  svelta  st.  V.  ,hungern,  sterben',  got. [tmltan  st.  V.  ,hinsterben*,  tiefstufig  got.  swulta-wairpja  ,der  sich  zum Tode  neigt',  aisl.  sultr  m.  , Hunger',  ags.  swylt  m.  ,Tod';  vielleicht  zu |lrm.  kaic-nu-m  ,hungern*,  kaic  ,Hunger*  (^*suld-sk-ö)]
Ht.  svilii,  svilti  , sengen  (intr.),  ohne  Flamme  brennen*,  Kausat.  svUinti [y»engen  (tr.)',  zem.  svtlis  ,Hitze,  Fieber',  svelti  ,schwelen*,  lett.  sveVu,  svelt jjBengen  (tr.)',  svelme  f.  ,Dampf,  Glut*,  svals  m.  ,Dampf',  svelains  ,scharf, rkalt'  (vgl.  die  Bed.  von  anord.  svalr).
WP.  II  531  f..  Scherer  Gestirnnamen  49 f.,  Trautmann  296,  Frisk  65 f.; ».  oben  S.  881  f.  sauel-.
1046  •
3.  (suel-),  suol-,  sul-  , Fußsohle,  auch  Grundlage,  Unterstes*      {]
Lat.    solea   , Schnürsohle,   Sandale^;   solum   ,Boden,   Grund  n  il^ Grundfläche,  Fußsohle*;
mir.  fol.  i.  bond  , Grundlage,  Fußsohle^  Akk.  Sg.  folaig^  Nom Dat.  PL  air.  soilgih  ;
schwundstufig  gr.  vUa  (Hes.)  , Sohlet
WP.  11  552,  WH.  II  554  f.
4    suel-  , Balken';  s.  oben  S.  898 f.  unter  2.  sei-.
sue-lo-,    suelno{n)-  ^Schwäger,   die   Schwestern  zu    Frauen   hal
griech.  und  germ.
Gr.  äeXiOL  (ä-  cop.,  vgl.  ahd.  ge-  in  ge-swio  ,Sch westermann' :  suji^  * siXlovsg  (für  zu  erwartendes  ^eXioveg)  ds.  (Hes.,  PolL); aisl.  svilar  PL  ds.,  Sg.  svili  , Schwager^; zum  Reflexivum  *se,  seue-. WP.  II  533,  Specht  Ursprung  166,  Frisk  24.
suelplo-s  , Schwefel'.  f|
Got.  swibls,  ags.  sweflj  ahd.  sioehal  ,SchwefeF  =  lat.  sulpur  ds.  (*m germ.  dissim.  zu  *swe[l]fla-,  *swe[l]bla'.  .-^
WP.  II  533,  WH.  II  628;   volksetymologisch   beeinflußt  von  IT
suem-  ,sich  bewegen',  im  Germ,  meist  ,schwimmen'.  C
Air.  to-senn-  ,verfolgen*  (*suem-d-ne-),  Verbalnomen  tofunn,  wohl j norw.  svamla  ,phantasieren',  svamra  ,umherirren,  schwärmen*; {frija^  symja  (Prät.  svamm  summum  und  svam  svqmum)  ,schwi as.    ags.   swimman   ds. ;    Kaus.    mhd.   swemmen  ,schwimmen schwemmen  j  afries.  swammia,  mhd.  swamen  ,schwimmen',  isl.  no sumla  ,plätschern',  got.  swumsl  n.  ,Teich';  aisl.  sund  n.  ,das  Seh" Meerenge,  Sund*  (d.  i.  ,*noch  überschwimmbar'),  syndr  ,schwiro ■■    ags.   sund  n.   , Schwimmfähigkeit',   poet.   ,See,   Wasser',   mnd. ,Meerenge*  (nhd.  Sund)]  anders  über  nhd.  Sund  Kluge-Götze*' T WP.  II  524.
suen-,  , tönen,  schallen';  suono-s  ,Ton,  Schall'.
Ai.  svdnati  (sekundär  dsvanlt)  ,tönt,  schallt'  (=  lat.  sonit), ,Geräusch*,  svand-  m.  ,Ton,  Schall*  (=  lat.  sonus),  svänd-  ,raus< x^anat.caxra-  ,einer,   des  Räder  sausen';    lat.   sonö^   -äre,  -uij sonere  (*suenö)  , tönen,  schal
=== POK_03 leaf 290 ===
len,  klingen,  rauschen*,  sonus  (*su>
1047
son  ,Laut*  lat.  Lw.);  wahrscheinlich  air.  senn-,  Prät.  sephainn  ,sonäre
ielen  (ein  Instrument)'^  das  nn  wohl  nach  to-senn-  ^verfolgen',  das  (aus
'^em-d-ne-  entstanden)  zur  Wz.  suem-  gehört;  air.  senim  (d.  i.  seinm)  ,das
§pielen;   Tönen';   ags.   swinsian    ,singen,    Musik    machen',    swinn    ,Musik,
(jesang^;  auch  ahd.  ags.  swan  ,Schwan^,  aisl.  svanr  »männlicher  Schwan';
Qb  sen-  neben  suen-  in  lett.   sanet^  senet  ,summen',  ir.   sanas  , Flüstern',
I  ftrur.  hanes  ,history'  eig.  ,*rumor'  ?
I   VP.n  524  f.,  WH.  II  559  f.
iueadh-  ,sch winden'?
Ahd.   swintan   ,schwinden,    abmagern,   welken,   bewußtlos  werden',   as.
f.swindan  ^verschwinden' ,  ags.  swindan  , abnehmen,  schwinden*,  Kaus. p^bd.   swenden    ,schwinden    machen,    ausreuten',    nhd.    verschwenden    dial.
iurch  Verbrennen  des  Grases  urbar  machen',  ahd.  sxointilönj  nhd.  schwin-
/n;  ablaut.  nhd.  Schwund;  aksl.  uvedati  ,welken',  ablaut.  ksl.  gditi Jüchen' ;
v^l.  air.  a-sennad  Adv.  ,denique,  postremo'  (*suendh-no-?)'j
ob  germ.  swindan  zu  swinan  ,schwinden'  (s.  sul-)  gehört  und  erst  durch
itgleisung  in  die  e-Reihe  übergetreten  ist?
WP.  II  526,  Vasmer  1,  245.
*'^S-f  suenk- :  sueg-,   suek-  ,biegen ;   drehend  schwingen,  schwenken'.
Ai.  svdjaUj  -ti  (svajdksyate)  ,umschlingt',  Partiz.  svaJctd-,  parisvakta-  = ir.  pairi§x^axta-  ,rings  umschlossen';  air.  seng  , schlank'  (,*biegsam'),  kelt. ON  Singi-dünum 'j
mhd.  mnd.  swanc  ,biegsam,  schlank,  fein,  schmächtig',  ags.  sioancor )iegsam,  schmächtig';  norw.  svekTc,  svokk  f.  (*swank-iöj  -ö)  , Höhlung  der
ißsohle',  dän.  schwed.  svank  ,Tal,  Höhlung';  ags.  swincan  ,arbeiten,  sich p|uälen'  (eig.  ,sich  winden  bei  der  Arbeit'),  Kaus.  swencan  ,plagen,  peinigen* ifwenc  m.  ,Trübsal'),  ahd.   mhd.  swenken  ,schwingen   lassen,   schleudern',
id.  schwenken]  mhd.  swank  (-k-)  , Wendung,  Schwung,  Streich,  Einfall', flhd.  Schwank]
daneben  germ.  *sweng-  (idg.  *suenk-) :
ahd.  as.  swingan  ,(sich)  schwingen,  fliegen^  as.  swingan  {swinga  , Keule'),
|lg8.  swingan  , schlagen,  peitschen,  sich  schwingen';  Kaus.  got.  af-swaggwjan
[ilchwankend  mach
```


## [2026-09-14T03:09:53.115Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== BRT x'ar ===\"; grep -n \"x''ar-\\|x'ar-\" BRT.txt | head -30; echo \"=== BRT search xvar ===\"; grep -n -i \"verzehren\\|geniessen, verzehren\" BRT.txt | head -20"
}
```


### [2026-09-14T03:09:53.188Z] TOOL RESULT

```
=== BRT x'ar ===
3742:•  j.  apiäma.x'ar-  Adj.  'blindlings  essend': 'rS  (NSm.",  näml.  'ist  der  Hund')  yaia  |     "'  '  '■ t3yus  V.  /J.47;  47-  I  •  j-  aipy-öxSay-  f  'Hineinsprechen,  Ein-
7208:•  j.  a-x'ar-  Adj.  'ohne  Essen,  der  kein Essen  bekommt':  spänö  yöi  hisl3'ite  °rg (NP.)  upa  s^armtem  V. /j.jS.
9561:•  j.  k3r«ß.x''ar-  Adj,  'Leichen-,  Aas-  Aleiandre  et  l'oppression  hell^nique";  s.  auch fressend',  von  Hunden  und  Vögeln:  ydiüit  f^-  ^"^  Y'  u''""  /'^'-e  <?°<ä»<^.'"l'!  ^.  33.
=== BRT search xvar ===
10290:mit  «r  'verzehren':  *janySts  .  .  yä  tat yal  haomahe  draon5  nigarthmii  *nilhi- oatti  (sd.)  V.  70.15.
24794:•  j.  raez-  V.  'lecken,  leckend  verzehren*. Praes.   1  rau-.
29072:Part.  Praes.  'sich  hinsetzen  etwas  zu  tun sva.  sich  daran  machen,  anheben  etwas  zu lun'*>:  aat  tum  niUilöt^  (PraeL)  gähasca srävayB  apasla  vanuhls  yassmnS  "da  hobst du   an,   die    G.   aufzusagen   und   die  . . Wasser  zu  verehren"  H.a.  13;  —  ya  tat yal    haomahe    draonS    nighttlwtti    *nishi' oaiti''>   "die  sich  dran  macht  den  Anteil desÄ  zu  verzehren"  Y.  10. 1 5.        3)  'sitzen, sitzenbleiben,  sich  aufhalten'*':  airimeisd.) gatüm    ht  niskihaita    V.p.  33,  16.  &;  — asne  vay^anät  nishihaiti  "in  der  Nähe  des Kopfes   hält   sie  sich  auf  H.  2. 1";   — yat  aAmi  nmäneyat  mäzdayasnBii!  näirika li%ravaUi  . .  niihSiäl  "wenn  sich  in  dem Hause  ..  befindet"  V. /6'.  i. mit  vT,  viy:  s.  unter  viltäspa-, *i.  iiditti,  sädäyaü,  sidih  \  np.  mlaslan,  niSinad, sbaL  nindag,    nUta   (%' g6.  l);    lit  ädmi.     - Pu.!  niiaslan,  (firs  Kaus.);  nüämtan;  %,  noch No.  7,  —   ■)  So  nach  dem  Herkommen,  *gl. aber    vonRozwadowski   BB.  31.  247,    Bau. Grdr.»  /.  486,  504,    ferner  No.  3.    —    »)  In iiisanhasH  für  'nilatti,    S  36S.  48.  —  .1)  jAw. Aiia-  iit   die   ICamposiiionifoim   zu  ai.  sTda-, IF,  7.  107;  das  np.  Verbum  enthält  altes  /.  — O  S  sS-   I.  -  s)  S  -^9.   ~   *'  Vgl  ifl*-  I.  — 7)  NA.  HilAai',    i.  Var.     Pü.:  3 yavisn  dänil. Sä, :    ihädanäya    tüvedayaü.      MlLU    Lesnng ZDMG.  J(5.  143  ist  mir  gani  Unverstand! ich.  — B)  Vgl.  die  Bedeutung  des  Verb*  im  Bai.  — 9)  An    der   Parallelilelle  H.  7.  20  steht  han-
```


## [2026-09-14T03:09:55.211Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== PHD xwardan ===\"; grep -n \"xward\\|xwar \\|xwarišn\\|āxwar\\|ʾhwl\" PHD.txt | head -40; echo \"=== PHD xwandan ===\"; grep -n \"xwān\\|xwand\" PHD.txt | head -30"
}
```


### [2026-09-14T03:09:55.292Z] TOOL RESULT

```
=== PHD xwardan ===
32:Sincethe ambiguities ofthe script make a mechanical translitera- tion of one letter by one roman symbol of no practical value, a certain amount of interpretation is essential, This interpretation can be based, either directly or by the use of analogy, on the less ambiguous evidence of the above-mentioned earlier documents of the language. With this help it is possible to go far in distin- guishing between the original values °’, й, dy, etc., of -», n, w, Р of у, and so on. But it is neither necessary nor desirable to go beyond this by attempting to give closer “phonetic” values to the letters, such as r for written /, or x for written h. For example, Sy hwl represents xwar ‘sun’, but to transliterate it *xwr entails both confusion with the true letter r \ and the introduc- tion of even greater ambiguity into the interpretation of .». It is better to accept that the scribes wrote r and / almost indis-
212:anērān [?7°3?n'] non-Eran, the world beyond Eran. an-érang [?n’ylng] blameless. an-espās [’nsp’s] ungrateful. ~ih: ingratitude. 2 AY angubén [DW BS Y.A < A dbf ; ?ngpyn! | N angubin] honey. By? Wat), angür [AN BE < A ‘nb’; ?ngwl | N ~] grape. А AC k angust Pngwst! | (N angust)] finger, toe; unit of length (š in.). Va м ~arig [-lyk'] finger ring. „bān [-p’n'] finger-guard, -stall. anidan, ānay- [HY TYWN-tn! < А hyty, ^? th; ?nytn!] bring, lead. anig Payk! | (N pēšānī)] front, forehead. anī-z [AH RN(y)e, v. any | N niz] other also. anjir Pncyl | N ~] fig. anódag [nwtk! | M ?nwdg] strange, alien. ~ig [-yk'] foreign. ünóh, *ànóy [TME < A tmh | M ?nwh, ?wy] there. an-dst Pwwst'] infirm, unreliable. anos [nws] lit. immortal, i.e. the next life; elixir, antidote. — xwardan : risk death, fight to the death. anošag Pxwšk! | M ?nwsg, N ~a] immortal. «ii: immortality. ~-ruwan [-lwb’n'] the late, deceased. an-Ošmār [?7wsm’l] countless, innumerable. anó$-xwar [поў] mortal. *апбу, v. ānēh. anSahrig [nstr'yk'] slave. an-umméd P7wmyt! | J *nwmyd, N nauméd] hopeless, despairing. an-uspurrig [^r wspwlyk') imperfect. any [AH RN < A *hrn; (corruptly, 2К?у = *dn-i) | M ?n()] other. a-pattüg [ptwk!] impatient. a-paymān (?ptm?n!] immoderate. ~ih : immoderation. *apédag [ругА! | P?pyd(g)] lost, stray. ~dar [-d?/] custodian of stray animals. a-petitig žtytyk!] unrepentant, unconfessed. 7h : unrepentance. a-petyürag Pf(y)tyd'lk'] without misfortune, unassailed. a-pohisn Pwhšn'] incorruptible. appar [?5/ | М ’pr] robbery, theft. appar ['P?/] taken away, removed. ~ih : removal, loss, deprivation. apparag [25/6] robber. appurdan, appar- [YHNCLWN-tn' < A yhnslwn, V asi: >pl- | M эрит, *p(w)r-] steal. ~išn: stealing, theft. a-pursišnīg Ppwrsinyk'] irresponsible.
223:āwēnišnīg : blameworthy. a-wēnišnīģ Pzwynšnyk'] invisible. awérag [”wylk!] = awērān. awērān Pwyln', ?5yPn! | N wērān] desolate, ruined. awestad ['zos??t! | M *zxoyst?d, N ēstād] master (craftsman). awestām [*wst?m | M ?wyst?m] province, district. awestarag [”wstlk! | N ustura] razor. awestardan, awestar- [*xvst/-tn! | P °wystr-, N suturdan] wipe; shave. mišn : wiping. awestwār Pwstwb’l | M ?wystw?r, N ustuwār] firm, reliable. “Аһ: reliability, firmness. awēšān [OLE?n, у. бу | М юу п, N ēšān] they, those. a-wināh Pwrs] innocent. a-winast [”wnst'] unharmed, immaculate. awiš [wbš | M ?wys] to him, it; postposition (= ©) to. awištāb Puwst*5 | M ’wyst?b, N šitāb] oppression. P awištādan, awišt- ['zoft2tn! | P ?wyst!dn] stand. awištāftan, awištāb- ['wi?j-tm | M ?wyšt?b-, N sitāftan, šitāb-] oppress; hasten (tr.). tāwištan, tāwāš- [HTYMWN-tn! < A Мут, V htm; ?wbstn' | M *wyšt] seal. a-wiyabanig Pwyd?f?nyk! | N biyābānī] astr. fixed (star). a-wizirignig Pweylinyk'] unavoidable, inevitable. āwurdan, awar- [YHYTYWN-in' < A hyty, У № | M wrd, "wr-, N ~] bring. āxēzīdan [>лусуѓп!] = āxistan. āxistan, āxēz- Phstn', ?hyc- | М *xyst, ?xyz-] rise, stand up. Axrámidan, āxrām- >А?т-уѓп! | M ?xr’m-, N xiram-idan] stride, strut. axtar [Atl | M *xtr, N ~] star, constellation, sign of the zodiac. axtar(ā)mār [Phil(?)m’/] astrologer. ~th: astrology. laxw Dell being, existence, world. ?axw Phw! | M *xvx] mind, will; vital force. *axw Phu'] lord. a-xwamn [’hwmn'] sleepless. axwān Phw’n'] = захм. a-xwārīh ['Aw'iyh] unhappiness. āxwarr [hwi | N àxur] manger, stable. --Sālār [-srd?I] head groom. a-xwaš [D BS YM] unpleasant; unhappy. ~ih: unhappiness. a-xwēškār [kwyšk'I] undutiful. ay Dy | N —J that is to say. āy-, у. amadan. ayāb [уор | М ik, N уд] or. ayāb- v. ayāftan.
318:^-éwüzih [-yxw'cyk | (M dwšw'cyh)) evil speech, calumny. ~+farrag [-plg | P dwéfr] unfortunate. ~-farragih : misfortune. ~-gowisn [-gwbsn'] of evil speech, ill-spoken. ~-humat [-hwmt'] evil thought. ~-hixt [-Awht' | M dwfxwptyy!] evil speech. ~-kām [-2’m] ill-will, malevolence. ~-kanig [-knyk'] hag. — kar LAT difficult. ~-kuni&n [-kwngn'] of evil behaviour, ill-doing. dušmat [dwfmt! = Av. dufmata- | M dw$mtyy!)] evil thought. dušmen [dwsm(y)n' | = M, N dušman] enemy. ~ih: enmity. „ādīh [dušmntyh | M dwkmny’dyh, J dwfmn'dy] enmity, hostility. duš-|-menišn [dwf-myntn!] of evil thought, ill-thinking. --nàm [->”m | N ~] abuse, insult. dušox [dwshw! | M dtws(w)x] hell. ~ig [-yk'] hellish. duš-pādixšā(y) [dušp*thš*(d)) evil ruler. ~th: evil rule, misrule. dušrām [dwsl())m] unhappy. ~ih: unhappiness. dušwār [2001 | M dwšw”r, № ~] difficult, disagreeable. ~ih: difficulty, trouble, misfortune. du&-|-wir [dws-wyl] evil-minded. ~-wurréyisnih [-wlwdsnyh] heresy. c-.xém [-hym] evil-natured. ~-xwadiayih [-hwt'yh] misrule. ~-xwar Lea! | N ~] = dušwār. dušxwaršt [до оной! | M dwkxw styh!] evil deed. duxt [BRTE < A brt-h; dwht' | M dwxt, N ~] daughter. ~ar [dwhtl | N ~] daughter. duz(d) [GN BA < A gnb’; dwc(t) | M dwz, N duzd] thief. ~th [dwe(d)yh] theft. duzidag [dwcytk'] stolen; intercalary (days). duzidan, duz- [dwe-yin' | N duzdidan] steal. dwārīdan / dwāristan, dwür- [dwP?l-ytn!, -stn! | M dwr-] run, move (daevic). ~išn: abode (of demons), hell. dwāzdah [dw'cdh | M dw'zdh, N duwazdah] twelve. ~ап [-’n'] the zodiac.
538:pādīrān [p'igP n!] restrained, held back. pādīrān(ēn)īdan, pādirān(ēn)- [þptgľn(yn)-ytn'] restrain, impede. padīriftan, padir- [MK BLWN-tn!Ü < A mqbl, V qbl; ptgl-ptn! | M pdyr-yptn, N paóiruftan] receive, accept. ~išn: reception, acceptance. īpadisār [ptys' | N padīsār ?] beginning, basis. tpadisār [ptys’/] bridle, halter. padisāy [pts’d | M рдуу] on account of, for the sake of. padist [ptst! | P pdyst] promise, vow. & (abar) burdan: promise. padistadan, padist- [ptyst-”tn! | (P pdystwd)] promise, vow. padistā(£) [ptyst*k! | (M pdystw)] = padist. padiš (pts | M pdys] to him, it; postposition (= pad) to, etc. padištān [pryst?n' | P pdyst??n] leg. padišxwar [ptshwl] dish, bowl. pādixšā(y) [SL Y TA < A йур; p’ths?(d) | M раху] ruler; powerful, authoritative, authorized. ~ЛЬ : sovereignty, authority. pādixšīr [p’thsyl] agreement, treaty. pad-néróg [PW Nnylwk!] strong. pad-niģerišn [PWNnkylin'] cared for, guarded. pādofrāh [p’twpl’s) = pādifrāh. pad-panag [PWNpnk!] guarded, protected. Р pádrazm [p’tlcm] battle. pàd-rózag [p’tlwck' | M p'drweg] fasting. pād-uzwān [p’??wzw’n'] reticent. ~ih: reticence. pad-wizén [PW Nwcyn!] choice, select. pādyāb [pty | N ~] ritually clean; ceremonial ablution. ~ih : ceremonial ablution. pādyāwand [p?tyd’wnd | J p'dywnd] strong, powerful. cAh : strength, superiority. pádzahr [p’tzhl | N pa(d)zahr] bezoar, antidote. pad-zyān [PWNzyd"?n'] harmful. pafšār- [pps?/-] shame. pafšīr- [ppsyl-] be ashamed. ~i8n(ih): shame. pah [p’h] sheep. ~ast [-st'] sheep-fold, -pen. pahikaftan, pahikaf- [ptkp-tn! | M phykf-] fall on, touch, hit, attack. ~išn: attack, fight. pahikāftan, pahikāf- [ptk’p-in'] throw on, make fight. pahikar [ptk] | M phykr, N paykar] picture, image. pahikār [ptk?! | M phyk”r, N paykār] struggle, battle, dispute. īpahikār- [ptk?/-] fight, contend with, defeat. pahikardan, *pahikār- [ptk’/-tn'] request, claim, consult.
559:rēšaģ [/yšk! | N rēša] root, fibre. rēšīdan, rēš- [lysyin' | N ~] wound, hurt. rëškën [/yškn'] hurtful, harmful. ~th: harmfulness. réxtan, réz- [lyhtn', lyc- | P ryxt, M ryz-, N ~] flow, pour. --išn: flow. ridan, riy- [/ytn', Id- | N ~] defecate, void. rist [lyst' | M ryst] dead. Iristag [lystk'] corpse. 'ristag [/ystk!] way, manner; sect. rist-āxēz [/yst?hyc | M ryst?hyz, N ~] resurrection of the dead, rištaģ [/(y)stk! | N ~a] rope, string, thread. riy-, v. ridan. riyahrih [/d?hlyh] scorn, mockery. rdb [/wp] robbery. rób- [/wp- | N ruftan, ~} rub, sweep. rūbāh [TALE < A tP; lwph | N ~] fox. Irēd [Iowt! | M rwd, N ~] river. *rdd [lwt' | N ~] stringed instrument. réd-bar [lwtb’] | N ~] river bank. rddig [/zvtyk! | (N róda)] intestine, gut; ~4n, (p/.) entrails, guts. тбүп [M(H)SY A < A ті; lwkn! | Р тшеп, (M rwyyn), N rauyan] oil, butter. ~-xwardig [-hwltyk'] sweetmeats. ron [lwn' | M rwn] direction. б... ~: towards. róspig [lwspyk! | N ~i] whore. ~th: whoredom. róstág [lw(t)st?k! | (P rwdyst?g), N rūstā] river-bed; district, province. rošn [lwfn! | M rwšn, N rūšan] light; bright, light. ~ih: light. röšnjag [lwsnk'] clear, obvious. ~gar [-Al | (P gr, M -ygr), N -gar] illuminator. irēy [ltd | M rwy, N ~] face. *rdy [lwd | M rwy, N ~] copper, brass. гбу-, -išn, v. rustan. гӧуап [/wdyn! | N ~] madder. róyen [/wdyn! | M r'wyn, N róyin] (made of) copper, brazen. roz [YWM < А ушт; Гос | M rwc[z, N ~) day. rózag [lwck! | M rweg, N roza] fast, fasting. rozāģ [wc k'] lightning. rózan [/wcn! | N ~] window. roz(b)ānaģ [lwe(p)’nk'] window. rózénidan, rózén- [Iwcyn-ytn! | M rweyn-] lighten, brighten. rozģār [/wck”l | N ~] daytime. r6zig [/wcyk! | N rózi] daily bread, sustenance.
663:xwāb [hw’b | N ~] sleep. xwābar [hw’l | M xwbr] beneficent. ~ig [-yk!] beneficial. —ih: beneficence, benefit. xwad [BNPSE < A b-nps-h; hwt' | M xwd, N ~] self; indeed. САҢ: selfhood, essence. xwaday [лору | M xwd'y, N ~] lord. ~th: lordship, sovereignty. ~war [-w’/] lordly. xwad-dósag [hwtdwsk'] self-indulgent. 7h : self-indulgence. xwah [AH TE < A *hth | N ~] sister. 1, ?x wüh-, ~išn, v. xwastan, xwāstan. xwahar [AH TEL v. xwah ; hw'hl | (M xwr), N xwdhar] sister. xwahl [eo hl | (M xwhr), № ~] bent, crooked. xwā(h)rīh [hw (h)yh | M xw'ryy] happiness, bliss. xwālist [hw’lyst' | (M xw’ryst)] sweetest. xwamn [hwmn', hmn' | M xwmn] sleep, dream. ~-wizar [-wc'/] interpreter of dreams, oneirocritic. xwān [hw!n! | M xw’n, N ~] tray, table. xwandan, xwān- [KRY TWN-, KLY TWN-tn! < А У д | M xwnd, xw'n-, N xwāndan) call, summon. Xwanirah [hwnyls = Av. x"aniraüa-] the central, inhabited continent of the earth. !xwar [kwl | M xwr, N ~] sun; cal. 11th day. Zwar [kwl = Av. x"ara-] a degree of sin. xwar-, —išn, v. xwardan. lxwàr [kw] | M xwr, N ~] light, easy; mean, abject. ~ih: ease; v. also x wührih. *xwar [%w/ | M xwr] food. xwür-, —išn, v. xwārīdan. xwaran [%w/n! | M xwrn] banquet. xwarāsān [hwlsn! | M xwr'?n, N ~] sunrise, east. xwār-bār [how?1b?l | M xwr w Pr, N ~] food and drink. xwardan, xwar- [OS TEN-tn! < Ath, V fth; hwltn! | M xwrdn, xwr-, N ~] eat, consume. ~išn: food. ~ignig : edible. ~išnīh: eating, consumption. xwardār [hwit?I] (legally) edible, not murdār. xwardig [hwityk' | M xwrdyg, N ~i] food. xwārēn [hw’lyn'] edible. xwārēn- [hw’lyn-] cause to eat, drink; feed; irrigate. xwarģ [wig | J xwwrg] ember. xwārīdan, xwār- [heo?1-ytnt] drink. —išn: drink, drinking.
665:xwarūfrān [hwl(’)wpl’n' | M xwrwpr'n) sunset, west. xwarrah [GDE < A gdh | (M prh, N farr)] fortune, glory, splendour. ~6mand [-’wmnd] fortunate, glorious. xwarséd, v. xwarxséd. xwartar [hw ltl] minor (sins). xwarwarān [hwlwPn!, -bPn'] = xwardfran. xwar(x)8éd [Azl(h)syt' | M xwrxšyd, № xuršēd] sun. xwāstag [NKSY A < A nksy’; hw'stk! | M xw’stg, N ~a] property, wealth. i ~õmand [-wmnd] wealthy. xwastan, !xwāh- [(Y)PLHWN-tn! < А V plh; hwstn!, hw'd- | J xwh-, N xwast] tread, trample; thresh. ~išn: trampling. xwāstan, *xwāh- [BOYHWN-stn! < A МУ Бу; hw'stn!', hwd- | M xw’stn, xt h-, N ~] seek, want, desire; attract, acquire. --j&n : desire, attraction. xwastüg [hwstwk!' | N xustū] confessing, believing. ~ih: confession, belief, faith. xwaš [BS YM < А bsym; hw | M xw, N ~] pleasant, sweet, nice. ~ih: pleasantness, pleasure. xwēd [Awyt! | M xwyd, N ~] moist, fresh. ~ih: moisture, freshness. xwédódah [hwytw(k)ds, -d^t! = Av. x"aetwada0a-] kin-marriage. xwēn-āhan [Ahw(y)n ?syn! = Av. x"aéna- (ayah-)] shining metal. xwēš [NP ŠE < А npf-h; hwyš | M xwy(b)s, N ~] (one's) own. ~ih: possession. ~awand [kwyš*wnd | N ~] relative, kinsman. xwēšēnīdan, xwēšēn- [/nwyfyn-ytn!] appropriate, make one’s own. xwēš-kār [леу dutiful. ~th: proper function. xwēš-tan [NPSE tn! | N ~] self. xwéy [hwyd | N xway] sweat, perspiration. xwistan [hwystn'] sweat, perspire. xwurd [hwlt' | N ~] small, little. xwurdag [hwltk' | N ~a] something small, particle; astr. lunar mansion; (horse's) pastern. ~ih: smallness.
1364:consume xwardan.
1365:consumption xwarišnīh,
1502:death marg(īh), ēš, widerišn(īh), P murd; moment of — gyān kandan; deserving — margarzān; risk —, fight to ~ anēš xwardan.
1696:drink xwarišn; alcoholic — hur.
1730:eat xwardan; cause to ~ xwürén-.
1731:eating xwarišnīh; (daevic) jēyišn.
1735:edible xwarišnīg, xwārēn, xwardār.
1990:food čāštag, nan, pih, xwār, xwardig, xwarišn; ~ and drink xwār-bār.
2717:manger āxwarr.
3794:stable āxwarr, stērgāh.
3907:swear (oath) sogand xwardan.
3913:sweetmeat royn-xwardig; afrōšag, gēzēnag, lawzénag, Šiftēnag, watrēnag.
4927:ruzdīh royn-xwardig royn
5118:ašnawišnt ašnūdan! nišast nišastan waštīh 1-2waštan waštagīh waštag xwar-! xwardant widaxtan wadxém widār widār- widārīdan widārdan widūz- widazih- widāzīhistan wadbaxt
=== PHD xwandan ===
223:āwēnišnīg : blameworthy. a-wēnišnīģ Pzwynšnyk'] invisible. awérag [”wylk!] = awērān. awērān Pwyln', ?5yPn! | N wērān] desolate, ruined. awestad ['zos??t! | M *zxoyst?d, N ēstād] master (craftsman). awestām [*wst?m | M ?wyst?m] province, district. awestarag [”wstlk! | N ustura] razor. awestardan, awestar- [*xvst/-tn! | P °wystr-, N suturdan] wipe; shave. mišn : wiping. awestwār Pwstwb’l | M ?wystw?r, N ustuwār] firm, reliable. “Аһ: reliability, firmness. awēšān [OLE?n, у. бу | М юу п, N ēšān] they, those. a-wināh Pwrs] innocent. a-winast [”wnst'] unharmed, immaculate. awiš [wbš | M ?wys] to him, it; postposition (= ©) to. awištāb Puwst*5 | M ’wyst?b, N šitāb] oppression. P awištādan, awišt- ['zoft2tn! | P ?wyst!dn] stand. awištāftan, awištāb- ['wi?j-tm | M ?wyšt?b-, N sitāftan, šitāb-] oppress; hasten (tr.). tāwištan, tāwāš- [HTYMWN-tn! < A Мут, V htm; ?wbstn' | M *wyšt] seal. a-wiyabanig Pwyd?f?nyk! | N biyābānī] astr. fixed (star). a-wizirignig Pweylinyk'] unavoidable, inevitable. āwurdan, awar- [YHYTYWN-in' < A hyty, У № | M wrd, "wr-, N ~] bring. āxēzīdan [>лусуѓп!] = āxistan. āxistan, āxēz- Phstn', ?hyc- | М *xyst, ?xyz-] rise, stand up. Axrámidan, āxrām- >А?т-уѓп! | M ?xr’m-, N xiram-idan] stride, strut. axtar [Atl | M *xtr, N ~] star, constellation, sign of the zodiac. axtar(ā)mār [Phil(?)m’/] astrologer. ~th: astrology. laxw Dell being, existence, world. ?axw Phw! | M *xvx] mind, will; vital force. *axw Phu'] lord. a-xwamn [’hwmn'] sleepless. axwān Phw’n'] = захм. a-xwārīh ['Aw'iyh] unhappiness. āxwarr [hwi | N àxur] manger, stable. --Sālār [-srd?I] head groom. a-xwaš [D BS YM] unpleasant; unhappy. ~ih: unhappiness. a-xwēškār [kwyšk'I] undutiful. ay Dy | N —J that is to say. āy-, у. amadan. ayāb [уор | М ik, N уд] or. ayāb- v. ayāftan.
663:xwāb [hw’b | N ~] sleep. xwābar [hw’l | M xwbr] beneficent. ~ig [-yk!] beneficial. —ih: beneficence, benefit. xwad [BNPSE < A b-nps-h; hwt' | M xwd, N ~] self; indeed. САҢ: selfhood, essence. xwaday [лору | M xwd'y, N ~] lord. ~th: lordship, sovereignty. ~war [-w’/] lordly. xwad-dósag [hwtdwsk'] self-indulgent. 7h : self-indulgence. xwah [AH TE < A *hth | N ~] sister. 1, ?x wüh-, ~išn, v. xwastan, xwāstan. xwahar [AH TEL v. xwah ; hw'hl | (M xwr), N xwdhar] sister. xwahl [eo hl | (M xwhr), № ~] bent, crooked. xwā(h)rīh [hw (h)yh | M xw'ryy] happiness, bliss. xwālist [hw’lyst' | (M xw’ryst)] sweetest. xwamn [hwmn', hmn' | M xwmn] sleep, dream. ~-wizar [-wc'/] interpreter of dreams, oneirocritic. xwān [hw!n! | M xw’n, N ~] tray, table. xwandan, xwān- [KRY TWN-, KLY TWN-tn! < А У д | M xwnd, xw'n-, N xwāndan) call, summon. Xwanirah [hwnyls = Av. x"aniraüa-] the central, inhabited continent of the earth. !xwar [kwl | M xwr, N ~] sun; cal. 11th day. Zwar [kwl = Av. x"ara-] a degree of sin. xwar-, —išn, v. xwardan. lxwàr [kw] | M xwr, N ~] light, easy; mean, abject. ~ih: ease; v. also x wührih. *xwar [%w/ | M xwr] food. xwür-, —išn, v. xwārīdan. xwaran [%w/n! | M xwrn] banquet. xwarāsān [hwlsn! | M xwr'?n, N ~] sunrise, east. xwār-bār [how?1b?l | M xwr w Pr, N ~] food and drink. xwardan, xwar- [OS TEN-tn! < Ath, V fth; hwltn! | M xwrdn, xwr-, N ~] eat, consume. ~išn: food. ~ignig : edible. ~išnīh: eating, consumption. xwardār [hwit?I] (legally) edible, not murdār. xwardig [hwityk' | M xwrdyg, N ~i] food. xwārēn [hw’lyn'] edible. xwārēn- [hw’lyn-] cause to eat, drink; feed; irrigate. xwarģ [wig | J xwwrg] ember. xwārīdan, xwār- [heo?1-ytnt] drink. —išn: drink, drinking.
1049:both jomā; of ~ worlds dē-axwānīg.
1140:call xróstan, xwandan.
3888:summon xwandan.
3924:table xwān; ‘table-cloth’ maškīzag.
5038:nay! kundāgīh kundāg nayestān! kandan kanīg kanīzag xwan-! xwandan! -gen
5545:dē-axwānīgx mardi
```


## [2026-09-14T03:10:11.058Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== BRT xvarena-ish ===\"; grep -n \"x'ar9na\\|x'ar3na\\|x'arena\\|x''ar9na\\|x'arana\" BRT.txt | head -20; echo \"=== BRT x'an ===\"; grep -n \"x'an-\\|x''an-\\|x'anat\\|x'anat.caxra\" BRT.txt | head -20; echo \"=== BRT tönen ===\"; grep -n \"tönen\" BRT.txt | head -20"
}
```


### [2026-09-14T03:10:11.145Z] TOOL RESULT

```
=== BRT xvarena-ish ===
8763:mahl  .  .  V.55.  i;    —    "iiöit  fnysi  'täna^  •  j.  usta.x''ar9nah-  m.  Name  eines  Bergs
16322:•  j.  pouru.x''ar9nah-  Adj.  'der  viel  Herr- lichkeit, Glanz  besitzt,  hoheitsvoll';  °nat»Ad (NS.)''  asava  sarahusIrSY .ig.y, — 'nanha (VS.)"'  ahura  mazda  Vyt.  2.^'*;  —  yasata 'naiaha  (AP.)  yasata  pouru.bailaza  Ny.5. 6 ; —  yazata  'nanha  (VP.)  Ny.  J.  1 1 ;  — jc^arj»?  "««»^iffi  (ASm.  statt  n.)  Yt.iÄi.
16952:•  j.  barö.x'ar3nah-  Adj.  'der  Hoheit, Herrlichkeit  besitzt,  gewinnt':  virihraymm . .  'nS  masd{^t>m  V,  ig.  37.
24186:•  j.  vindi-x''ar9nah-  Adj.  'der  Ruhm  vcr schafft':  'm>  <NSm.) "  nqma  ahmt  (näml. vayus)  Yt/5.4S'
=== BRT x'an ===
30657:•  j.,  g.  hvar-,  g.  x'an-  n.  'Sonne;  Sonnen- ball, Sonnenlicht',  auch  als  Gottheit:  avat hvar»  ..hau  mä..  ave  siärS  V.p.  41;  Yt ij. 1 6,  *FrBy. ;  —  upa  tairtm  (sd.)  haraihyä . .  yat  ml  aiwtts  urvtsMit  starasca  mäsca hvarica  Yti2.25;  V.2.40;  —  strSuSca manhimca  hvar?ca  Y.  2,  11,  77.  9,  Yt. 10. 145,  G.J.  6,  V, /J.  I,  3,  7.5a,  Vyt.4j;
=== BRT tönen ===
15580:Ableit.  la  pairi.\-ga{%ä-;  vgL  No.  1.  —  Pü.: ape    rasim    S   in  i  imäi    Hyäyisn   ckrmatd  .  . 111/in  anjar  garöttnän  itäjrem,  —    ')  Ich  ver- weise für  meine  Fassung  des  Worts  und  der ganien   Stelle   auf  V.  38.  11  (s.  '/J(j>   mit No.  4),  4g.   10  (s.  dam.  mit  No.  3I,  37. 13  (s. äii^ar-*)).   Der  ■heilige  Mann'  ist  ZitmäHi/rit, der  'gute  Sinn'  seine  Anhingenchaft;  f^röbS ifiiqm  ergänzt  mamiifkä  und  i(j^SflM  tu  der bekannten  Drei  bei  t. •  j.  ■•■pairi.gä.-vacah-"  Adj.   'der   seine Worte  ringsum  singt,  d.  L  ettönen,  erklingen lässt':    kaomS  /räimil . .  hvaca  päpB.vach •/J  Y.  57,  30,
16807:stimme, den  Ruf  erheben,  ertönen  lassen*:  tragen,  abreissen,  zerstören':  apa  aetam yS  mq'^rä  {sd.)  . .  *väcim  baraitT  Y,  50,  6;  \distqm  {sd.)  baraym    apa    a!t>m   taddtum
19252:KompA.;  Ableit.  —  iL  ai/',  w-' (luw.)  Adv., Praev.  —  Pii.:  afie.  —  ')  Wenn  yoio  Verbum getrennt,  sowie  vor  tonlosen  Leuten.  —  ')  Vor tönenden  I^naten.  —  3)  In  nijiyam,  Sp.  I53ni.
```


## [2026-09-14T03:10:12.831Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== AHD swel ===\"; grep -n -i \"^swel\\|swel-\\|swelg\\|swallow\" AHD_watkins1985.txt | head -30; echo; echo \"=== AHD swen ===\"; grep -n -i \"swen-\\|swan\\b\\|sonus\\|sonāre\" AHD_watkins1985.txt | head -30"
}
```


### [2026-09-14T03:10:12.954Z] TOOL RESULT

```
=== AHD swel ===
120:For the notions of eating and drinking, the roots ed- and péi-' are most widespread. A root swel-' is attested in Avestan and sur- vives in English both in SWALLOW! and in as humble a word as SWILL. For drink, a root srebh- is found in some dialects (ABSORB). The metaphor in “drunk, intoxicated” seems to have been created independently a num- ber of times in the history of the Indo- European languages; Latin ébrius, “drunk”
512:CICHLID. 3. Greek khelidw6n, khelidén, the swallow: CELANDINE. [Pok. ghel- 428.] ghel-2. To shine; with derivatives referring to colors, bright materials (probably “yellow metal”), and bile or gall. I. Words denoting colors. 1. Suffixed form *ghel-wo- in Germanic *gelwaz in Old English gealu, yellow: YELLOW. 2. Suffixed variant form *ghlé-ro- in Greek khioros, green, greenish yellow: CHLORO-; CHLORITE!. 3. Suffixed variant form *ghlo-wo- in Greek khloos (< *khlo-wo-s), green color: CHLOASMA. 4, O-grade form *ghol- in Russian zola, ashes (from their color): PODZOL. II. Words denoting gold. 1. Suffixed zero-grade form *ghl-to- in Germanic *gultham, gold, in: a. Old English gold, gold: GOLD; b. denominative verb *gulthjan in Old English gyldan, to gild: GILD!; c. Middle Dutch gulden, golden: GUILDER, GULDEN; d. Old Norse gulinn, golden, akin to the possible source of Middle English gollan, yellow flower: GOWAN. 2. Suffixed o-grade form *ghol-to- in Polish zloto, gold: zLoTy. 3. Suffixed full-grade form *ghel-i- in the unknown Iranian source of Syriac zarnikd, orpiment: ARSENIC. III. Words denoting bile. 1. Suffixed o-grade form “ghol-no- in Germanic *gallon-, bile, in Old English gealla, gall: GALL!. 2. Suffixed o-grade form *ghol-& in Greek kholé, bile: CHOLE-, CHOLER, (CHOL- ERA); ACHOLIA, MELANCHOLY. 3. Suffixed full-grade form *ghel-n- in Latin fel, bile: FELON?. IV. A range of Germanic words (where no preforms are given, the words are late creations). 1. Germanic *glaimiz in Old English glém, bright light, gleam: GLEAM. 2. Middle High Ger- man glimsen, to gleam, akin to the source of Middle English glimsen, to glimpse: GLIMPSE. 3. Swedish dialec- tal glinta, to shine, akin to the source of Middle English glent, a glint: GLINT. 4. Swedish glimra, akin to the source of Middle English glimeren, to glimmer: GLIM- MER. 5. Old Norse glitra, to shine: GLITTER. 6. Old English glisnian, to shine: GLISTEN. 7. Middle Dutch glisteren, to shine: GLISTER. 8. Germanic *glasam, glass, in Old English gles, glass: GLASS, GLAZE. 9. Germanic *glaz- in Middle Low German glaren, to glisten, akin to the source of Middle English glaren, to glitter, stare: GLARE!. 10. Icelandic glossi, a spark, perhaps akin to the source of GLoss!. 11. Old High German glanz, bright: GLANCE2. 12. Old Norse gléggr, clear-sighted: GLEG. 13. Germanic *gladaz in Old English gled, shining, joyful: GLAD. 14. Germanic *gleujam in Old English gléo, sport, merriment: GLEE. 15. Old English gléd, ember: GLEED. 16. Germanic *gié- in: a. Old English gléwan, to glow: GLow; b. Norwegian dialectal glora, to gleam, stare, akin to the probable source of Middle English gloren, to gleam, stare: GLOWER; C. Old Norse glotta, to smile (scornfully), perhaps akin to the source of GLOAT. 17. Germanic *glé-m- in Old English glém, twilight: GLOAMING. 18. Possibly distantly related is Germanic *glidan, to glide, in: a. Old English glidan, to slip, glide: GLIDE; b. Old French glier, to glide: GLISSADE; c. Old High German glitan, to glide: GLITCH; d. derivative Germanic “glidén- in Old English glida, kite (< “gliding, hovering bird”): GLEDE. 19. Middle Low German glibbe- rich, slippery, possibly akin to the source of GLrB. [Pok. 1. &hel- 429.] ghel-. To cut. 1. Germanic “galdjan, to castrate, in Old Norse gelda, to castrate, and geldingr, a castrated ani- mal: GELD!, (GELDING). 2. Germanic *gulti- in Old Norse gyltr, a sow (< “castrated pig”): GiLT?. [Pok. 2. ghel- 434.] gheldh-. To pay. Only in Germanic and Slavic. 1. Ger- manic *geldam, payment, in: a. Old English geld, gield, payment, service: GELD?; DANEGELD, WERGELD; b. Old High German gelt, payment, reward: GELT!. 2. Germanic *geldan, to pay, in Old English gieldan, to pay, yield: YIELD. 3. Germanic *geldjam, payment, contribution, hence an association founded on contributions, a crafts- men’s guild, in Old Norse gildi, guild: GuILD. [Pok. ghel-t6 436.] ghelegh-. A metal. Possible root of Greek khalkos,
540:(COVEN), (COVENANT), EVENT, INTERVENE, INVENT, MIS- ADVENTURE, PARVENU, PREVENIENT, PREVENT, PROV- ENANCE, (PROVENIENCE), REVENANT, REVENUE, SOUVENIR, SUBVENTION, SUPERVENE. 3. Suffixed zero-grade form *gvm-yo- in Greek bainein, to go, walk, step, with basis (< *gm-ti-), a stepping, tread, base, and -batés (< *gwa-to-, zero-grade of gd-, contraction of *gaa-), agential suffix, “one that goes or treads, one that is based”: BASE!, BASIS; ABASIA, ACROBAT, ADIABATIC, AMPHISBAENA, ANABAENA, DIABASE, DIABETES, STEREO- BATE, STYLOBATE. 4, Suffixed zero-grade form “g“(g)-u- in compound form “pres-gu-, “going before” (see per’). 5. Basic form *gvd- in Greek béma, step, seat, raised platform: BEMA. 6. Sanskrit jigdti, he goes: JUGGER- NAUT. [Pok. g¥d- 463.] gvadh-. To sink. Possible root. 1. Suffixed form *guadh-u- in Greek bathus, deep (> bathos, depth): BATHOS, BATHY-. 2. Greek benthos, depth, may be formed on bathus by analogy with penthos, grief, and pathos, passion, suffering (or it may be from an unrelated root *g¥(e)ndh-): BENTHOS. 3. Suffixed variant form *gudh-yo- in Greek bussos, bottom of the sea: ABYSS. [Pok. gddh- 465.] g’ébh-'. To dip, sink. Suffixed zero-grade form *gvabh-yo- in Greek baptein, to dip: (BAPTIST), BAPTIZE; ANABAPTIST. [Pok. g¥ébh- 465.] g”ébh-2. Hypothetical base of some Germanic words associated with the notion of sliminess. 1. Middle Dutch quac-, unguent, liquid, in obsolete Dutch quacksalver, quacksalver: QUACKSALVER. 2. Low German quabbeln, to shake like jelly, tremble, akin to Middle English quaven, to tremble: QUAVER. [Pok. 2. g¥ébh- 466.] grei-. Also gveia-. To live. I. Suffixed zero-grade form *gwi-wo-, *gi-wo- (< *gi9-wo-), living. 1. Germanic *kwi(k)waz in: a. Old English cwic, cwicu, living, alive: QUICK, QUICKSILVER; b. as a name for couch grass (from its rapid growth), in Old English cwice, couch grass: (COUCH GRASS), QUITCH GRASS. 2. a. Latin vivus, living, alive: VIVIFY, VIVIPAROUS; b. Latin denominative vivere, to live: VIAND, VICTUAL, VIVA, VIVACIOUS, VIVID; CON- VIVIAL, REVIVE, SURVIVE. 3. Further suffixed form *gvi- wo-td in Latin vita, life: VIABLE, VITAL; LIGNUM VITAE, VITAMIN. II. Suffixed zero-grade form *gia-o- in Greek bios, life (> bioté, way of life): BIO-, BIOTA, BIOTIC; AEROBE, AMPHIBIOUS, ANABIOSIS, CENOBITE, MICROBE, RHIZOBIUM, SAPROBE, SYMBIOSIS. III. Variant form *gwyd- (< *gvyoo-). 1. Greek z0é, life: AzO-, (DIAZO). 2. Suffixed form *gvy6-yo- in Greek zdon, zdion, living being, animal: (-Z0A), -ZOIC, ZOO-, ZOON, -ZOON. IV. Pre- fixed and suffixed form *su-g~ia-es- (*su-, well; see su-), “living in good condition,” in Greek hugiés, healthy: HYGEIA, HYGIENE. [Pok. 3. gei- 467.] g”eia-. To press down, conquer. Sanskrit jayati, he con- quers: JAIN. [Pok. gveio- 469.] gvel-'. To pierce. 1. Suffixed o-grade form “gvol-eyo- in Germanic *kwaljan in Old English cwellan, to kill, destroy: QUELL. 2. Suffixed zero-grade form *g“/-yo- in Germanic *ku/jan in Old English *cyllan, to kill, perhaps the source of Middle English killen, to kill: KILL}. 3. Full-grade form *gvel- in Greek beloné, needle: BEL- ONEPHOBIA. [Pok. 1. g¥el- 470.] gel-2. To fly; a wing. Possibly in Latin voldre, to fly: VOLANT, VOLATILE, VOLE2, VOLITANT, VOLLEY. gvel-3, To swallow. Dissimilated to *gel-. 1. Germanic *kel- in Old English ceolu, throat, dewlap, perhaps akin to Middle English cholle, throat: JowL?. 2. Germanic *keluz in Old Norse Aj6ir, keel: KEEL}. 3. Suffixed zero-grade form “gul-d in Latin gula, gullet, throat, palate: GOLIARD, GULAR, GULES, GULLET. 4, Extended (expressive) form *glutt- in: a. Latin gluttire, gliitire, to swallow: GLUT; DEGLUTITION; b. Latin glutté, a glutton: GLuTTon. [In Pok. 2. gel- 365.] gvelbh-. Womb. 1. Suffixed form *gvelbh-u- in Greek delphus, womb, whence delphis, dolphin (referring to its
542:shape): DELPHINIUM, DOLPHIN. 2. Prefixed and suffixed form *sm-gvelbh-o-, “born of one womb” (*sm-, one; see sem-'), in Greek adelphos, brother: -ADELPHOUS. [Pok. gtelbh- 473.] gvele-1. To throw, reach. Variant *g/é-, contracted from *guleg-, 1. Suffixed zero-grade form *g/-n-o- in: a. Greek ballein, to throw (with o-grade *bol- and variant *b/é-): BALLISTA; AMPHIBOLE, ASTROBLEME, CATABOLISM, DEVIL, (DIABOLIC), (EBLIS), ECBOLIC, EMBLEM, EPIBOLY, (HYPERBOLA), HYPERBOLE, METABOLISM, (PALAVER), PARABLE, (PARABOLA), (PARLEY), (PARLIAMENT), (PAR- LOR), (PAROL), (PAROLE), PROBLEM, SYMBOL; b. Greek ballizein, to dance: BALL?, (BALLAD), (BALLET), BAYA- DERE. 2. Suffixed o-grade form *gvols-d in Greek bolé, beam, ray: BOLOMETER. 3. Suffixed o-grade form *gwolo-sdé in Greek boulé, determination, will (< “throw- ing forward of the mind”), council: BOULE!; ABULIA. 4. Suffixed variant zero-grade form *gvele-mno- in Greek belemnos, dart, javelin: BELEMNITE. [Pok. 2. g¥el- 471.] gwela-2, An acorn. 1. Suffixed zero-grade form *g¥/o-nd- in Latin gldns (stem gland-), an acorn: GLAND, GLAN- DERS, (GLANDULAR), GLANS. 2. Suffixed zero-grade form *gulg-no- in Greek balanos, acorn, date: VALONIA; MYRO- BALAN. [Pok. 3. gvel- 472.] gven-. Woman. 1. Suffixed form *gven-d- in: a. Germanic *kwen6n- in Old English cwene, woman, prostitute, wife: QUEAN; b. Old Irish ben (> Irish Gaelic bean), woman: BANSHEE; C. Persian zan, woman: ZENANA. 2. Suffixed lengthened-grade form *gvén-i- in Germanic *kwéniz, woman, wife, queen, in Old English cwén, woman, wife, queen: QUEEN. 3. Suffixed zero-grade form *g“n-d- in Greek guné, woman: GYNO-, -GYNOUS, -GYNY; GYNAE- CEUM, GYNECOCRACY, (GYNECOLOGY), POLYGYNY. [Pok. gvend 473.) g”ere-'. Mountain. Possibly o-grade form *gvors- in: a. Greek boreios, “coming from the north” (? < “coming from the mountains of Thrace, north of Greece”), whence Boreas, the north wind: Boras; b. Greek Huperboreioi, Huperboreoi, name of a people living in the far north, variously explained as “they who live beyond the north wind” and “they who live beyond the mountains” (hu- per-, beyond; see uper): HYPERBOREAN. [Pok. 3. gver- 477.) gvere-2. Heavy. I. Zero-grade form *gra-. 1. Suffixed form “g“ra-u-i- in Latin gravis, heavy, weighty: GRAVE?, GRAVID, (GRIEF), GRIEVE; AGGRAVATE, AGGRIEVE. 2. Suffixed form “gro-u- in: a. Greek barus, heavy: BARITE, BARITONE, (BARIUM), BARYON, (BARYSPHERE), BARYTA; b. Sanskrit guru-, heavy, venerable: GURU. 3. Suffixed form *gro-es- in Greek baros, weight: BAR?, BARO-; CENTROBARIC, ISALLOBAR, ISOBAR. 4. Possibly *guri- in Greek bri- in compound *u(d)-bri- (see ud-). II. Suffixed extended form *g-rii-to- in Latin britus, heavy, unwieldy, dull, stupid, brutish: BRUT, BRUTE. III. Suffixed extended form *g»ri-g- in: a. Celtic *brig-o-, strength, in Italian brio, vigor: BRIO; b. Germanic *krig- in Old High German krég, chrég, stubbornness (> Ger- man Krieg, war): BLITZKRIEG, SITZKRIEG. IV. Suffixed full-grade form *gvero-nd-, millstone, in Old English cweorn, quern: QUERN. [Pok. 2. g¥er- 476.] gvere-*. To praise (aloud). 1. Suffixed zero-grade form *gvra-to- in Latin grdtus, pleasing, beloved, agreeable, favorable, thankful: GRACE, GRATEFUL, GRATIFY, GRATIS, GRATITUDE, GRATUITY; AGREE, CONGRATULATE, IN- GRATE, INGRATIATE. 2. Suffixed zero-grade form *gwro-do-, “he who praises,” in Celtic bardo-, bard, in Welsh bardd and Scottish and Irish Gaelic bard, bard: BARD}. [Pok. 4. gver(a)- 478.] gvere-4. To swallow. 1. Possibly suffixed extended form *gro-gh- in Germanic *krag-, throat, in: a. Old English *craga, throat, possible source of Middle English crawe, craw: CRAW; b. Middle Dutch craghe, throat: scrac. 2. Suffixed o-grade form *gvor-d- in Latin vordre, to swallow up: VORACIOUS, -VOROUS; DEVOUR. 3. Expres-
754:‘ TAL), MORTGAGE, MORTIFY, MORTMAIN, POSTMORTEM; c. suffixed form *mr-yo- in Latin mori, to die: MORI- BUND, MURRAIN; d. prefixed and suffixed form *n-mr-to-, “undying, immortal” (*n-, negative prefix; see ne), in (i) Greek ambrotos, immortal, divine (a- + mbrotos, brotos, mortal): AMBROSIA (ii) Sanskrit amrta, immortal (a- + mrta, death): AMRITA. 2. Suffixed o-grade form *mor-t-yo- in Old Persian martiya-, a mortal man, in Iranian compound *martiya-khvdra- (attested in Persian mard-khvdr), ‘‘man-eater”’ (*khudra-, to eat; see swel-'), probable source of Greek mantikhoras (corrupted from martiokhéras), manticore: MANTICORE. See extended root smerd-. [Pok. 4. mer-, 5. mer- 735.]
905:sawel-. Also s(u)wel-, su(a)el-, su(@)en-, sun-. The sun. Contracted from *saswel-. 1. Variant forms *swen-, *sun- in: a. Germanic *sunndn- in Old English sunne, sun: SUN; b. Germanic compound *sunn6én-dagaz, “day of the sun” (translation of Latin diés sdlis), in Old English sunnandeg, Sunday: SUNDAY; c. Germanic de- rivative *sunthaz, “sun-side,” south, in Old English sith, south, and sitherne, southern: SOUTH, SOUTHERN. 2. Variant form *s(2)wol- in: a. Latin sd/, the sun: soL’, SOL, SOLAR, SOLARIUM; GIRASOL, INSOLATE, PARASOL, SOLANINE, TURNSOLE; b. Latin compound sdlstitium, “a standing of the sun,” solstice (-stitium, a standing; see sta-): SOLSTICE. 3. Suffixed form *sdwel-yo- in Greek hélios, sun: HELIACAL, HELIO-, HELIOS, HELIUM; ANTHE- LION, APHELION, ISOHEL, PARHELION, PERIHELION. [Pok. sdwel- 881.]
914:sécula, sickle: SICKLE. 8. Suffixed variant form *sak-so- in Latin saxum, stone (< “broken-off piece”): SAXATILE; SAXICOLOUS, SAXIFRAGE. See also extended roots sked-, skei-, sker-', sker-4. [Pok. 2. sék- 895, sken-(d)- 929.] s@k-. Slack, calm: relax. Greek (h)éka, slowly, a little (> héss6n, inferior): ESSONITE. [Pok. 3. sék- 896.] sekw-1, To follow. 1. Latin sequi, to follow: SECT, SEGUE, SEGUIDILLA, SEQUACIOUS, SEQUEL, SEQUENCE, SUE, SUITOR; CONSEQUENT, ENSUE, EXECUTE, OBSEQUIOUS, PERSECUTE, PROSECUTE, (PURSUE), SUBSEQUENT. 2. Latin sequester, “follower,” mediator, depositary: SEQUESTER, SEQUESTRUM. 8. Suffixed (participial) form *sekv-ondo- in Latin secundus, following, coming next, second: SECOND2, SECONDO, SECUND, SECUNDINES. 4. Suffixed form *sekv-os, following, in Latin secus, along, alongside of: INTRINSIC. 5. Suffixed form *sekv-no- in Latin signum, identifying mark, sign (< “standard that one follows”): SEAL!, SEGNO, SIGN; AS- SIGN, CONSIGN, DESIGNATE, INSIGNIA, RESIGN. 6. Suf- fixed o-grade form *sok’-yo- in Latin socius, ally, companion (< “follower”): SOCIABLE, SOCIAL, SOCIETY, SOCIO-; ASSOCIATE, CONSOCIATE, DISSOCIATE. [Pok. 1. seky- 896.] sekw-2, To perceive, see. 1. Germanic *sehwan, to see, in Old English séon, to see: SEE}. 2. Germanic abstract noun *sih-tiz in Old English sihth, gesiht, vision, specta- cle: SIGHT. [Pok. 2. sek¥- 872.] sekw-3, To say, utter. 1. O-grade form *sokv- in: a. suf- fixed form *sokv-yo- in Germanic *sagjan in Old English secgan, to say: SAY; b. suffixed form *sok-d- in Ger- manic *sag6, a saying, in (i) Old English sagu, a saying, speech: sAw? (ii) Old Norse saga, a saying, narrative: saGA. 2. Suffixed zero-grade form *sk~-e-tlo-, narration, perhaps in North Germanic “skathla in Old Norse skdid, poet, “narrator,” perhaps akin to the probable Scandina- vian source of Middle English scolde, an abusive person: SCOLD, SKALD. [In Pok. 2. sek¥- 897.] sel-1, Human settlement. 1. O-grade form *sol- in Ger- manic *sal-, room, in Italian sala, hall, room: SALON, (SALOON). 2. Suffixed form *sel-o- in Latin solum, bot- tom, foundation, hence sole of the foot: SOLE!, SOLUM; ENTRESOL. [Pok. 1. sel- 898, 3. (swel-) 1046.] sel-2, Also sele-. Of good mood; to favor. 1. Germanic lengthened form *sél- in Old English ges#lig, happy (ge-, completely; see kom): SILLY. 2. Suffixed lengthened o-grade form *sdl-d- in Latin sdlari, to comfort, console: SOLACE; CONSOLE}. 3. Possibly suffixed form *sels-ro- in Greek hilaros (< *helaros), gay: HILARITY; EXHILARATE. [Pok. 6. sel- 900.] sel-3, To take, grasp. 1. Suffixed o-grade (causative) form *sol-eyo- in Germanic *saljan, to offer up, deliver, whence West and North Germanic “‘to sell,” in Old English sellan, to sell, betray: SELL. 2. Germanic *sal-, giving, sale, in: a. Old Norse sala, sale: SALE; b. Old Norse compound handsal, giving of the hand (in closing a bargain): HANDSEL. [Pok. 3. sel- 899.] sel-4, To jump. 1. Suffixed zero-grade form *sal-yo- in: a. Latin salire, to leap: SALACIOUS, SALIENT, SALLY, (SAUTE); ASSAIL, DESULTORY, DISSILIENT, EXULT, IN- SULT, RESILE, RESULT, SOMERSAULT; b. Greek halles- thai, to leap, jump: HALTER2. 2. Perhaps Latin salmé (borrowed from Gaulish), salmon (< “the leaping fish”): SALMON. [Pok. 4. sel- 899.] sel-es-. Swamp, marsh, sea. Greek helos, marsh: ELODEA. [Pok. selos- 901.] selk-. To pull, draw. 1. Perhaps Germanic *selhaz, seal (the animal), “that which drags its body along with difficulty” (but more likely an early Germanic borrowing from Finnic), in Old English seolh, seal: SEAL?. 2. Suf- fixed o-grade form *solk-o- in Latin sulcus, furrow, groove (< “result of drawing or plowing”): (SULCATE), sucus. [Pok. selk- 901.] selp-. Fat, butter. 1. Germanic *salb- in Old English sealf, healing ointment: SALVE}. 2. Germanic denomina-
1044:s(w)eks. Six. I. Form *seks. 1. Germanic *seks in Old English s(iJex, six, six: sIx. 2. Latin sex (> Italian sei), six: SENARY, SEX-; SEICENTO, SEMESTER. 3. Suffixed form *seks-to- in Latin sextus, sixth: SESTET, SESTINA, SEXT, SEXTAN, SEXTANT, SEXTILE; SEXTODECIMO. II. Form *sweks in Greek hex, six: HEXA-, HEXAD. [Pok. sueks 1044.] swel-', To eat, drink. 1. Perhaps Germanic *swil- in Old English swilian, to wash out, gargle: swILL, 2. Extended form *swelk- in Germanic *swelgan, *swelhan in Old English swelgan, to swallow: SWALLOW!; GROUNDSEL!. 3. Iranian *khvdra- (attested in Avestan), to eat, in the probable source of Greek mantikhdras, manticore (see mer-?). [Pok. 1. suel(k)- 1045.] swel-2, To shine, burn. 1. Extended form *sweld- in Germanic *swiltan in Old English sweltan, to die, perish (perhaps < “be overcome with heat”): (SULTRY), SWEL- TER. 2. O-grade form *swol- in Germanic *swal- in Old Norse svalr, cool (< “lukewarm” < “hot”), akin to the Scandinavian source of Middle English swale, shade, shady place: SWALE. [Pok. 2. swel- 1045.]
1045:swel-3, Post, board. Germanic *suljé- in Old English sylXe), doorsill, threshold: stLL. [Pok. 2. sel-, swel- 898.] swem-. To move, stir, swim. Possibly an Indo-European root, but perhaps Germanic only. 1. Germanic *swimjan in Old English swimman, to swim: SWIM. 2. Suffixed zero-grade form *swum-to- in Germanic *sundam in: a. Old English sund, swimming, sea: SOUND’; b. Old French sonde, sounding line: SOUND‘; RADIOSONDE, ROCKETSONDE. [Pok. syem- 1046.]
1568:GROUNDSEL! ghendh-, swel-1
2257:SIGHT sekw-2 SIGN sekw-1 SIGNORY sen-1 SIKH kak-1 SILENT si-lo- SILL swel-3
2325:SUE sekw-1 SUFFER bher-1 SUFFICE dhé-1 SUFFICIENT dhé-1 SUFFIX dhig’- SUFFRAGAN bhreg- SUFFRAGE bhreg- SUFFUSE gheu- SUGGEST gerere SUICIDE s(w)e- SUINT sweid-2 SUITOR sekw-1 SULCATE selk- SULCUS selk- SULLEN s(w)e- SULTRY swel-2 SUM uper SUMMER! sem-2 SUMMIT uper
2328:SURE cilra, s(w)e- SURFACE dhé-1 SURFEIT dhé-1 SURGE reg-! SURGEON ghesor- SURGERY ghesor-, werg- SURLY sen-1 SURMISE (s)meit(9)- SURMULLET mel-2, saus- SURPLICE pel-4 SURPLUS pele-' SURPRISE ghend- SURRENDER d6- SURREPTITIOUS rep- SURROUND wed-! SURVEILLANT weg-2 SURVEY weid- SURVIVE gWei- SUSCEPTIBLE kap- SUSPECT spek- SUSPEND (s)pen- SUSPIRE spirare SUSTAIN ten- SUSURRATION swer-2 SUTLER seut- SUTRA syil- SUTTEE e@8- SUTURE syu- SVELTE wel-4 SWAB swep-2 SWAG sweng(W)- SWAIN s(w)e- SWALE swel-2 SWALLOW! swel-1 SWAMI s(w)e- SWAMP swombho- SWAN swen- SWANK sweng(w)- swaP swei-2 SWARF swerbh- SWARM swer-2 SWART swordo- SWASTIKA @S-, SU- SWEAR swer-1 SWEAT sweid-2 SWEET swad- SWELTER swel-2 SWERVE swerbh- SWIFT swei-2 SWILL swel-!

=== AHD swen ===
628:keuk-. To be white, be bright, shine. Suffixed zero-grade form *kuk-no- in Greek kuknos, swan: CYGNET, CYGNUS. [Pok. keuk- 597.]
905:sawel-. Also s(u)wel-, su(a)el-, su(@)en-, sun-. The sun. Contracted from *saswel-. 1. Variant forms *swen-, *sun- in: a. Germanic *sunndn- in Old English sunne, sun: SUN; b. Germanic compound *sunn6én-dagaz, “day of the sun” (translation of Latin diés sdlis), in Old English sunnandeg, Sunday: SUNDAY; c. Germanic de- rivative *sunthaz, “sun-side,” south, in Old English sith, south, and sitherne, southern: SOUTH, SOUTHERN. 2. Variant form *s(2)wol- in: a. Latin sd/, the sun: soL’, SOL, SOLAR, SOLARIUM; GIRASOL, INSOLATE, PARASOL, SOLANINE, TURNSOLE; b. Latin compound sdlstitium, “a standing of the sun,” solstice (-stitium, a standing; see sta-): SOLSTICE. 3. Suffixed form *sdwel-yo- in Greek hélios, sun: HELIACAL, HELIO-, HELIOS, HELIUM; ANTHE- LION, APHELION, ISOHEL, PARHELION, PERIHELION. [Pok. sdwel- 881.]
1046:swen-. To sound. 1. Suffixed o-grade form *swon-o- in: a. Germanic *swanaz, *swanon-, “singer,” in Old English swan, swan: SWAN; b. Latin sonus, a sound: SONE, SONIC, SONNET, SOUND!; UNISON. 2. Form *swen-d- in Latin sondre, to sound: SONANT, SONATA, SONOROUS; ASSO- NANCE, CONSONANT, DISSONANT, RESOUND. [Pok. suen- 1046.]
1263:ASH? os- ASININE asinus ASK ais- ASPECT spek- ASPEN apsa ASPERSE (s)preg- ASPIRATE spirare Ass? ors- ASSAI? Sa- ASSAIL  sel-4 ASSAY ag- ASSEMBLE sem-! ASSENT sent- ASSERT ser-3 ASSESS sed-1 ASSET sa- ASSEVERATE weéro- assIDUOUS_ sed-1 ASSIGN sekw-1 ASSIMILATE sem-1 ASSIST sta- ASSOCIATE sekw-1 ASSOIL feu-1 ASSONANCE swen- ASSORT ser-3 ASSUAGE swad- ASSUASIVE swad- ASSUME em- ASSURE cira ASTASIA sta- ASTATINE  sta- ASTER  ster-3
1392:CONFOUND gheu- CONFRERE bhrater- CONFUSE gheu- CONFUTE bhau- CONGE mei-1 CONGEAL gel-3 CONGENER gene- CONGENIAL gene- CONGENITAL gene- CONGERIES gerere CONGEST gerere CONGLOBATE gel-1 CONGLOMERATE gel-1 CONGLUTINATE gel-1 CONGRATULATE gWera-3 CONGREGATE ger-! CONGRESS ghredh- CONGRUENT ghréu- CONIDIUM keni- CONIOSIS keni- CONJECTURE yé- CONJOIN yeug- CONJUGAL yeug- CONJUGATE yeug- CONJUNCT yeug- CONJURE yewes- CONNATE gene- CONNECT ned- CONNIVE kneig’h- CONNOISSEUR gn6- CONNOTE gné- CONNUBIAL sneubh- CONQUER quaerere CONQUIAN kom, kWo- CONSCIENCE skei- CONSCIOUS | skei- CONSCRIPT skribh- CONSECRATE sak- CONSENT sent- CONSEQUENT sekw-1 CONSERVE ser-1 CONSIDER sweid-1 CONSIGN sekw-1 CONSIST sta- CONSOCIATE sekw-1 CONSOLE! sel-2 CONSOLIDATE sol- CONSOLUTE leu-1 CONSONANT swen- CONSORT ser-3 CONSPICUOUS _ spek- CONSPIRE spirare CONSTABLE ei-1 CONSTANT sta- CONSTELLATION  ster-3 CONSTERNATE  ster-2 CONSTIPATE  steip- CONSTITUTE sta- CONSTRAIN | streig- CONSTRUCT  ster-2 CONSUETUDE s(w)e- CONSUME em- CONTACT tag- CONTAIN ten- CONTAMINATE tag- CONTEMPLATE tem- CONTEND ten- CONTEST trei- CONTEXT teks- CONTINUE ten- CONTORT terkw- CONTOUR tera-1 CONTRA- kom CONTRABAND bha-2 CONTRACT tragh- CONTRADICT deik- CONTRARY kom CONTRAST sta- CONTRAVENE gWa- CONTRITE tere-1 CONTRIVE trep-2 CONTROL ret- CONTROVERSY wer-3 CONTUSE (s)teu- CONVALESCE wal- CONVECTION wegh- CONVENE gWa- CONVENIENT gWa- CONVENT gWa- CONVENTICLE gWa- CONVENTION gWa- CONVERGE wer-3 CONVERSE! wer-3 CONVERT wer-3 CONVEX wegh- CONVEY wegh- CONVINCE weik-5 CONVIVIAL gWei- CONVOKE wekw-
1429:DIN dhwen- DINGUS _{enk-1 DINOSAUR dwei- DINOTHERE dwei- DIOCESE weik-! DIOECIOUS weik-1 DIOICOUS_ weik-1 DIOPTER oOkW- Dioscuri_ deiw-, ker-3 pip dheub- DIPHTHERIA deph- DIPHYODONT bheue- DIPLO- dwo- DIPLOCARDIAC kerd-1 DIPLODOCUS dek-1 DIPLOE dwo- DIPLOID pel-3 DIPLOMA dwo- DIPNOAN pneu- DIRE dwei- DIRECT reg-! DIRNDL tek- DISARM ar- DISASTER ster-3 DISBURSE bursa DISCERN krei- DISCIPLE dek-! DISCIPLINE dek-? DISCOMFIT dhé-1 DISCORD kerd-1 DISCOURSE kers-2 DISCRIMINATE krel- DIscuss kwét- DISDAIN dek-1 DISEMBOGUE beu-! DISFIGURE dheigh- DISGUST geus- DISK deik- DISMAL deiw-, mel-5 DISMAY magh-! DISMISS (s)meit(9)- DISPARATE pere-1 DISPATCH ped-! DISPEL pel-6 DISPENSE (s)pen- DISPERSE (s)preg- DISPLAY plek- DISPOSE apo- DISPUTE peu- DISQUISITION quaerere DISRUPT reup- DISSECT sek- DISSEMINATE 6-1 DISSENT sent- DISSERTATE ser-3 DISSIDENT sed-1 DISSILIENT sel-4 DISSIPATE swep-2 DISSOCIATE sekw-1 DISSOLVE leu-! DISSONANT swen- DISSUADE swad- DISTANT sta- DISTEND ten- DISTICH steigh- DISTINGUISH _ steig- DISTORT terkw- DISTRACT tragh- DISTRAIN  streig- DISTURB twer-! DITCH dhigw- DITTO deik- DITTY deik- DIURETIC wers-2 DIURNAL deiw- DIVA deiw- DIVARICATE wa- DIVE dheub- DIVERGE wer-3 DIVERT wer-3 DIvEs_ deiw- DIVIDE weidh- DIVINE! deiw- DIVINE? deiw- DIVULSION wel-4 Dizzy dheu-!
2180:REQUIEM kWeie-2 REQUIESCAT kWeia-2 REQUIRE quaerere REREDOS dorsum, re- RESCIND skei- RESCRIPT skribh- RESCUE kwét- RESEAU  era-2 RESECT sek- RESEMBLE sem-! RESENT sent- RESERVE ser-1 RESERVOIR ser-1 RESIDE sed-! RESIGN sekw-1 RESILE sel-4 RESIST sta- RESOLVE leu-1 RESORB srebh- RESOUND swen- RESPECT spek- RESPIRE spirare RESPITE spek- RESPLENDENT spel-2 RESPOND _spend- REST? sta- RESTITUTE sta- RESTIVE sta- RESTORE sta- RESTRICT  streig- RESULT sel-4 RESUME em- RESUSCITATE kei-3 RETAIN ten- RETALIATE telo- RETCH ker-2
2276:SoL sdwel- SOLACE sel-2 SOLANINE sAwel- SOLAR sawel- SOLARIUM sawel- SOLE! sel-1 SOLE? s(w)e- SOLEMN sol- SOLICITOUS_ kei-3, sol- SOLID sol- SOLILOQUY s(wW)es, tolkw- SOLIPSISM s(w)e- SOLITARY s(w)e- SOLITUDE s(w)e- SOLO s(w)e- SOLSTICE sawel- SOLUBLE leu-1 SOLUM sel-1 SOLUTE leu-1 SOLVE leu-! SOMA teue- SOMATO- teua- SOME sem-! -SOME! sem-1 -SOME2  teue- SOMERSAULT sel-4, uper SOMNI swep-! SOMNOLENT swep-! SON seue-! SONANT swen- SONATA swen- SONE swen- SONG sengWh- SONIC swen- SONNET swen- SONOROUS swen- sooT sed-1 SOOTH es- SOOTHE es-
2277:SOP seue-2 SOPOR swep-1 SOPORIFIC swep-1 SOPRANINO uper SOPRANO uper SORCERER ser-3 SORDID swordo- SORDINO swer-2 SORE sai- SORITES teue- SORORAL swesor- SORORITY swesor- SORREL! siiro- SORREL? saus- SORROW swergh- SORRY Sai- SORT ser-3 SORTILEGE leg-1, ser-3 SORUS teue- SOTERIOLOGY teue- SOUBRETTE uper SOUFFLE bhlé-2 SOUGH (s)wagh- SOUND! swen- SOUND2 swento- SOUND3 swem- SOUND4 swem- SOUP seue-2 sOUR siiro- SOURDINE swer-2 SOUSE sal-1 SOUTANE upo SOUTH sawel- SOUTHERN sawel- SOUVENIR gWa- SOVEREIGN uper SOVIET sem-! sow! sé-1
2328:SURE cilra, s(w)e- SURFACE dhé-1 SURFEIT dhé-1 SURGE reg-! SURGEON ghesor- SURGERY ghesor-, werg- SURLY sen-1 SURMISE (s)meit(9)- SURMULLET mel-2, saus- SURPLICE pel-4 SURPLUS pele-' SURPRISE ghend- SURRENDER d6- SURREPTITIOUS rep- SURROUND wed-! SURVEILLANT weg-2 SURVEY weid- SURVIVE gWei- SUSCEPTIBLE kap- SUSPECT spek- SUSPEND (s)pen- SUSPIRE spirare SUSTAIN ten- SUSURRATION swer-2 SUTLER seut- SUTRA syil- SUTTEE e@8- SUTURE syu- SVELTE wel-4 SWAB swep-2 SWAG sweng(W)- SWAIN s(w)e- SWALE swel-2 SWALLOW! swel-1 SWAMI s(w)e- SWAMP swombho- SWAN swen- SWANK sweng(w)- swaP swei-2 SWARF swerbh- SWARM swer-2 SWART swordo- SWASTIKA @S-, SU- SWEAR swer-1 SWEAT sweid-2 SWEET swad- SWELTER swel-2 SWERVE swerbh- SWIFT swei-2 SWILL swel-!
2436:UNCIAL ol-no- UNCIFORM = ank- UNCINARIA ank- UNCINATE ank- UNCINUS ank- UNCLE awo- UNCOUTH gn6- UNCTION ong¥- UNCTUOUS ongW- UNCUS ank- UNDER ndher- UNDERNEATH ni UNDERSTAND sta- UNDINE wed-! UNDULATE wed-1 UNGAINLY gagina UNGUENT ong¥- UNGUIS nogh- UNI- oi-no- UNICORN ker-1, oj-no- UNION oi-no- UNIQUE oi-no- UNISON swen- UNITE oi-no-
```


## [2026-09-14T03:10:28.008Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== caxra ===\"; grep -n \"caxra\" BRT.txt | head -10; echo \"=== x'ar essen ===\"; grep -n \"x'ar\\b\\|x''ar\\b\\|x'ar-\\|x''ar-\" BRT.txt | head -40"
}
```


### [2026-09-14T03:10:28.082Z] TOOL RESULT

```
=== caxra ===
2686:*zamarigusa    avazat   vXspe   daifa    Yt /<?.       AbleiV  aus  ■arr'OB.u'ajflZw. 'elf;  vgl.  tF,  S  ?/o 81 ;  —  yahmai  . .  aurvantö  . .  v3sa  '^an-  ■     aK  und  IF.  p.  245.  —  Pü. :  yHdahum. }aianie   °va   caxra  (sd.)    Yt  10.136;    —  •  j-    aeväkam    Adv.    'zugleich' (?):    aiv aim  .  .  yß  t0  °ve  säsnä   (sd.)  gäsatä    Y.   narqm  asaonqm  ahunvitim  ga^qm  frasrä- ^9.8;  YtJ7.i9,2i;    —  yö  nö  °v6  at  U  vay'nti  Vd. /2.
5485:•  j.,  g.  aradra-  Adj,  (fem.  'rJ-)  'getreu, 'verlässig':  'rS  '^wävqs(sd.)  ÄitzSntuü  sfmtö mazdä  Y. 4:_j.3;  46.^;  — fravasayB..  °rä taxmä  *at>javuAai/i/ \l.  ij.  $2;  75;  — mihrgm  . .  y5  äsunqtn  äsus  yS  'ranqm  °rö y3  taxmanqm  taxmS  Yt.  70. 65.  a)  mit DaL:  kuirä  tsi  °rä  masdä  ysi..  caxrayö' (sd.)  "ob  sie  wohl  dir  getreu  sind,  die  . ," Y._j4-7-  A)  insbes. 'dem  Glauben  treu, gläubig,  fromm':  firasaosträ  air3  tu  'r.lis idi  hvB^S  täis  yitig  . .  "o  Fr.Hv.,  dahin geh  mit  diesen  Frommen,  denen  . ."  Y. 4'j^i6;  —  kä  iw'ffi  a/a  äk,i  (sd.)  'ring isyl  Y.  4S.  8;  S*}.  4;  —  fatrijasai  .  .  at vä  aia  "rahyacä  mmankä  "..und  vor  euch, o  Asa,  auch  mit  dem  Gebet  des  Frommen" Y.50.8;  —  da^at  ahrnili  tat..  arfdvJ . . 'räi  yavmiini  jatoyantäi  da^ris  ayaphm Ytj.ig;  13a,  /5.1,  21.
5855:•  g.  'a-spä-  n.  'Unglück,  Leid':  ySt vanhSus  vaidinä  (sd.)  manatthiS  sSnghaS raSxma  °spsn^l  (AP.)"  sadräcU  caxrayS (sd.)  tuMro  Y.34.T,  — yJn7  usJn  (sd.) &r;>i  sp7nlä  'spJnla.  (AP.)"'  Y.^ij.g.
7279:charakterisirenden  Adj.  (sd.,  auch  fdSt.): vispasca  äpS  yazamaide  ya  z)m3  armaesta (sd.)  *fratat.ear3tasca  (sd.)  *xqnyk  '^raots.- stälasca  par^uya  *v3iryäsca  (sd.)  "alle Wasser  auf  der  Erde  . , :  die  stehenden  und fliessenden,  die  in  Quellen  und  in  Fluss- laufen,  die  Schnee-  und  Regenwasser"  Y. 61^.6;  usw.;  —  vJspä  apd  xä  pttiti '^raotS.- stSiasca  Y.yi.g;  —  sps yal  armal^tayä.. yat  cätayä  uzuityäsca  .  .  yat  sna^ntyaica srasUntyaica  . . yat ß^tat.^antayä'W .  6.^0, 33i  36,  39;  —  äpim*  tacintqm  . .  xayanqm .  .  zrayanqm  .  .  artmaistqm  Yt.6.2;  Y.ig. 26,  Vd.4;  —  caval  nä  apa  (statt  DS.) ''frälat.cartte  .  .  paiti.iaräi  .  .  cval .  .  ape armaisfaya  (statt  DSf.)  .  .  nävayayai  tia ape  ..  ti.66(.;  —  apqm  ..  nävayaiiqm (sd.)  paiti  pintüs  Yt  //.  4 ;  usw.;  —  andvim . .  ye^he  avavat  .  .  äps  lata  (sd.)  ava.- barmle ya%ia  ..  Yt.5.15;  Ä.47; — gairil yS  uiiiä  yim  aiwiid  paoiris  äpS  hqm  gairi- ü(/('(sd.)/(WJ«/JYL/9.66; — spim  laokmta' vaitim  zaranyävaitlm  vihusavaifim  (sd.) V.^.54;  —  ap3mca  haomyqm  {sA.)  Y.  22. 2;  usw.;  — yaSsyatitim  äp^m  *pararihät Y.g.ii;F.4 f.,  V.21;  —  ?iqm.taptibyB  aiwyS caxrare(sii.)  n^r^bydY.  4.46; — apU  ai yaza- maide malkaintllcä  (sd.)  * hsbavaintlicä  . . Y.JÄ3«.  C)  GP.  apqm  mit  napat-m. (sd.,  auch  fdSt.)  Name  einer  Gottheit: apqm  napäs?  tä  apff  ..  vliax/aiti  YtS. $4; usw.  2)  von  bestimmten  Flüssen  oder Seen,  'Gewässer':  andvl  (sd.)  nqrna  äpa (NS.)"'  V.  7. 16;  —  n?mS  artduya  aps  anü- hitaya  Yt  r.  2 1 ;  Y.  6$.  i ,  Ny.  4.  o.  Vr.  1. 5 ; —  *atikäs^a  (näml.  artduyä)  mS *aaatiAä aps  apayiarsY .  65.  i;  5;  —  upa  äp.'myqm vltaaukaittm  Yt5,76;  —  njinB  ape  däit- yayä  (sd.)  Yt./.2i;  5.112,  5,29,  /7.61, V, ig.2;  —  aoi  apjm  yqm  raiakqm  (sd.) Yt.5. 63;  —  haca  apat  kqsaeyät  (sd.)  Yt ig.92,  V.ig.$;  —  a/s  ya  aw^änva  nqma Yt  ig.  62;  —  yazäi  äp^m  frazdänaom  F. 4%.  I,  2  Anhang:  apqm  (näml  ayar^y
8730:tßi  aridrä  (sd.)  .  .  ysi  vanhSus  vazd>na (sd.)  manauhö . .  aspSncit  sildrJcU  caxray3 (sd.)  'S3ura  (IS.)  \.34.T,  —  hamSm  tat vahiitäat  y!  's'urvye(DS.)  syasclt  (sd.)  dah- mahyä  Y.  J2.  r6.
11131:•  j.  caxra'vant-  Adj.  (fem.  •vaia-)  'ein Rad  (als  Feldzeichen)  führend"':  hafnayä 'vailyh  Aog.Si.
11243:Z'um  V,  )ak-,  s.  ta/'ar-  und  BTHL.IF. /o.  3. — i>  Hds.  j''a"ftjw;  Tgl.  iiar-  No.  2  und  anya- No.  6;  femer  zu  lanal,caxra-.
18701:Aus  dem  Zusammenhang  gerissene,  un- deudiche,  verderbte  oder  wertlose  Stellen mit  nar-.  «flr/(GS.)  ..  nara  (ND.)  .. «(jr?(NP.)  F.  2e;  —  «3  Fsd;  — nanm ..sar>t)m  V.^.  14  PüZ'J»;  N.52"';  — panca  narB  V.  75.  loPüZ.;  Vyt.  42,  Vd 13,15;  —  dva  nar^FiB.; — para  "iafah- mät(sd.)  n»r>t  (AblS.)  V.  j.  42  PÜZ.;  — aBsqmia  naram  V.  5.  gPUZ.;  —  ham.- tapiibyB  aiwys  caxrart  (sd)  n^r^byB  V. 4. 4  7 ;  I  o  PiiZ. ;  —  tl  ^narsS paitismarmitm Vy^  52;  —  nöil  dim  "nara  . .  avasyil  Yt /.  aS;  — ya'ia  na  ttäifyaY.  20.  2;  Yyt  28, 30.  narSm  nartm  als  Adv.  sbes.  [N. 301  streiche  «a.J
20847:I  et  (eum)  qui  (est)  faciendi  et  dicendi" I  Y.  33. 14;  —  *grSkms . .  atikSus  maraxtärB I  (sd.)  ahya  \yai(a  ^'Grlhmas  . .  et  (ii)  qui (sunt) ..  destructores"  Y.J2. 13; —  ku%ra töi  andrS  (sd.)  .  .  yöi  .  ,  caxrays  "num tibi  (sunt)  fidi  (ü)  qui  . ,"  Y.^4.7;  — kada  .  .  yOi  uxiäiiS  ainqm  .  .  frärmtl "quando  . .  (ii)  qui  (sunt)  tauri  .  ."  Y.  4G. 3;  —  naldä  dahySus  \ydi  iastSrS  drjsvatas "neque  (ii)  qui  (sunt)  . .  imperatores"  Y. 4O.  I ;  —  tat  ..  uitanai  data  . .  ySi  sl gSus  v^nzinl  (sd.)  azyi  ".  .  vitae  (eorum) qui  .  ."  Y.  34.  14;  —  tim  at  yasna- nqm  paurvataia  yazamaidl  ySi  ..  iyeintJ ".  .  imprecationum  .  .  (eorum)  qui  .  ." ^•37-  2;  —  yi  varpsaiil  (sd.)  kyat vasnä  firasöJ^mim  "qui  . .  fecerit  . .  (id) quod  (est)  .  ."  "^.46.  19;  —  hyatcS dar>gSm  dr)gvll.d»byS  rasB  savai'a  alavabyö "et  (id)  quod  (est)  . .  damnum  et  lucra  . ." Y._jo.  11;  —  Aaihyavanitqm  {%A.)  hyat vasna  f?rasS.t}m}m  "verificationem  (eius) quod.."  Y. 50.11;  —  ai  zt  töi  vaxsya .. hyai  aksyä  (NSf.;  sd.)  dngvaiii  wörtlich ",.  von  dem,  was  die  Androhung  ist,,"  Y, 51.  8;  —  hyat  "qsasutä  (sd.)  yä  (NPn.) daiiiiana  (sd.)  fraoxta  "..  (ea)  quae  (sunt) . .  enuntiata"  Y.  48.  1 ;  —  das  Relativ  kon- gruirt  mit  dem  Praedikat:  vldvä  yalclt güzra  (sd.)  singhanhS  (wörtlich)  "kennend auch  (das),  was  die  geheimen  Lehren  (sind)" Y.4<V,3;  —  anais  a  vT.nSnasa  ya  (NSt) iarapsjis{ad.}cä  kjvltäscä  Y._J2.  15;  — *m>ndäiäyai  (sd.)  ya  (NSf)  toi  adisHi Y.44.8;  5,^.13;  —  nipatihw . .  tumas^a ya  armaitiH&d.)  Tiilcä  Y.4g.  10;  —  yS va  mSi  \yh  (NPf)  gasha  dasdi  (Sp. 7 1 S  u.)  *asnatihe  wörtlich  ". .  (das),  was meine  Besitztümer  (sind)  .  ."  Y,  46. 8;  — vtayUta  yä  (NPn.)  mrqi  sädra  drtgvats (wörtlich)  "immer  (wird  sein)  was  die Qualen  (sind)  .  ."   Y.45.  7;  43-5,  49-6;
22013:—  yesi  .  .  dim  nsit  tanu.ptn'Afm  *v^ar)  im  Besitz  des  wahren  heiligen  Wissens (sPPfA.)''  "wenn  sie  es  (von  ihm)  nicht ^  befindlich,  darin  eingeweiht"-^;  n)  von wissen,  dass  er  /,  ist"  ^.3$ ,3g, 38')  — \AhM.:  *yqm  mBi  vtdva  matda  vaocat at  vS  xsmaibyä  asBrtä  vasdä  x^arai'^yä '  a/iurS  "was  mir  der  wissende  MAk. (sd)  srava  Y.2Ä10.  a)  'etwas  (Akk.)  1  verkündet  hat"  Y.45-3;  —  vaocä  mH kennen  als  (das)  des  —  (praedik.  Gen.),  j^i?  (VJ'w  zTrfz'i  a^ars  "tu  mir  kund  — denn scire  rem  (esse,  fore)  ahcuius':  yehyäxda  ja  bist  der  wissende,  o  Ah.  —"  Y, tnHi  asät  hacä  vahist>m  yesnl paiti  vaidä  4IS.2.  ß)  sonst:  müahvacff  v3  *Pr7s,- mazda  ahurü  ySi  nnharsia  htnticä  "wen '  rairc  vä  vTävä  vä  >vfdva  {sd.)  vä  Y. von  denen,  die  waren  und  die  sind,  MAh. als  einen  solchen  kennt,  dem  durch  Asa mein  Bestes  fiir  sein  Gebet  zu  teil  vrird" '^.51.22;  —  ynihe  Aätqm  aat  yesm  paitt vaahs  mazdä  ahurö  vatha  asät  hacä  Y. 27.  15;  —  yaisqm  nS  ahur5  .  .  va^hs vaiha  "quorum  nostium  Ahuras  ..  melius (fore)  seit"  Yt.iÜ.s;—  *yat  nSil  vist»m drvats  "wovon  man  nicht  weiss,  ob  es einem  Ungläubigen  gehört"  N.  54**;  — ysi  vaahsul  vaEdtnä  (PPfM.)  mananhs .  ,  ralxsnh  .  .  caxrayS  (sd.)  ".  .  die  dem guten  Sinn  gewissen  Erbanteile  .  ."  Y. 34.  7.  3)  Perf.  Pass.  'bekannt  sein als  —    (Nom.),    etwas   (Nom.)    gewisslich
=== x'ar essen ===
3742:•  j.  apiäma.x'ar-  Adj.  'blindlings  essend': 'rS  (NSm.",  näml.  'ist  der  Hund')  yaia  |     "'  '  '■ t3yus  V.  /J.47;  47-  I  •  j-  aipy-öxSay-  f  'Hineinsprechen,  Ein-
4303:•  j.  an-aiwi5.x''ar«8'a-  Adj.  (fem,  -iJa-) 'zum  Genuss  ungeeignet,  ungeniessbar' : vtsprm  ä  ahmät  alsa  ä/s  ayaoidya  (sd.) ";jo  yavat  aisa  nasus  niibtrsta  V. Ö.31.
5197:•  j.  avo.x'ar^na-  n.Tränke':  gaeyaoitis^a maSianyhsca  -näsca  Y.  2. 16;  — gaoyaoili- nqm^a  magiananqmla  "itanqm^a  Y.  7.  ifi.
5546:Ableit.  aus  airya-.  —  Vgl.  'Apiä-f^l  —  Pü.; erSii  (vH).  —  'I  S.  /■.  9  =  Ny.j.  5  steht  air- yanqm  x'ar^nä.
6958:•  j.  ahyäsä-"  fem.  Adj,  'die  Worte  ahyä '  •  j.  a-x'^sa-  n.  'Nichtessen':  s^älaya  vispö yäsä    enthaltend,    damit    beginnend':    'ia  '  afvhtts  .  .  jvaiti  "se  fi-amiryeite  V.^.33. Äaiii/ (sd.)'i   Y.  2<S'  Überschr.;    —    'sqm       Fa.:  Aa^  ax'arü-  - AaUlm  yazamaide  V,  a.S' is,
7208:•  j.  a-x'ar-  Adj.  'ohne  Essen,  der  kein Essen  bekommt':  spänö  yöi  hisl3'ite  °rg (NP.)  upa  s^armtem  V. /j.jS.
9561:•  j.  k3r«ß.x''ar-  Adj,  'Leichen-,  Aas-  Aleiandre  et  l'oppression  hell^nique";  s.  auch fressend',  von  Hunden  und  Vögeln:  ydiüit  f^-  ^"^  Y'  u''""  /'^'-e  <?°<ä»<^.'"l'!  ^.  33.
9568:V.7.30";  39;    -   alx'ar,üma?il>y3  isA.)   •  J" .  ^'T^^f  P^',  "^^  ^.^^  ^"^^?  H^'^!*^  'l"
10138:—  tistryS ..vaz»mnö  -Jus  k)hrpa  zaranyS.-  bagä  x^ar^mnif  (sd.)  Y. 32. 8;  —  "Su/x'ar»- srvahe  YLÄ16;  i4-l,  Y.ig.yi.  A)  Das  \%ahe  nr^yJ  V.7.  43; — 'Sul  vä  s^var3%ahe Rind  gilt  als  Repräsentant  aller  nützlichen  j  (sd.)  vä  W.14.1T,  —  '!us  i^ar/itinqm {ahumohtn)  Tiere,  daher  ^gav-  auch  inJH, /.  5;  —  yasca  ..  lanumazs {^A.)  'Jui weiterem  Sinn  gebraucht  wird*"':  para\da%at  "W-iS.!!);  —  °amla  ifsst)m  anäp»m •Su^  ca^war).paitistanaya  dänheit  para\{%d.)  V.5,  52;  S3f.',  7.55;  —  buiri 'aas  ,  . nars  asaotiB  bipaittstänahe  zq%st  Y.  /p.  8 ;  j  3far>^a  . .  VyL  4:5.  3)  'Milch',  bes.  zur
19892:mainyui.x'ar^Oti-  1140
19910:•  j.  mainyuä.x'ar«&a-  Adj.  (fem.  •%a^ i)  'die  Nahnmg  des  Geistes  bildend':  yh nS  htnti  gdhä  Aarfhravaitls^a . .  '^äsca  yä nö  hsnti  urune  tvaim  i^an'äfmld  vastr^mSi Y.55.  a;  2.  2)  'die  Nahrung  der  Geister geniessend':   aurvants  .  .  *&a  anaa^ahs
24034:—  ')  Bed.?  Als  Herren  der  beiden  Karivar fr'  und  i!td°  gelten  /rädat-^ar^nah-  und  vida[.- x'ar^ttah-.  Danach  lässt  sieb  annehmen,  das: vJd'  für  vWal.fiü-  geichtieben  ist;  vgl.  Cld. GGA.  iSge-'m.
24037:•  j.  vi8at.x''ar»nah-  m.  EN.  eines  der sechs  Genossen  des  Saesyant  bei  der Auferstehung  und  Ratav  des  Karsvar Vidata/sa  (sd.)'':  °na>9hs  alaonS  Yt jj.  1
25526:•  j.  urupay-m.EN.  des  zweiten  iranischen Königs,  eines  altem  Bruders  Yimas,  der ihm  nachfolgt"':  taxmO  °/a  (NS.)  asinavä Yt.75,11;  —  kavann  x'ar»nB  . .  yat  upa- nhaca^  taximm  'pi  (alsAS.)*'  azinavantam .  .  yat  barata  anrim  mainyBm  framittm (sd.)  aspahe  kihrpa  %risattm  aiwi^äma- nam  Yt.  jp.  28f.;  —  ^zainanuhanttm  .  . ya%a  taxmS  °pa  Az.  2.
28762:•  j.  *haoma.x''ar»tay-''  f-'^aömagenuss': nititnaHt  'nitiS  AatanraynyHi  asti  dalva- nqm  Y.J0.6.
30574:•  j.  hus.ham.b^rat-  Adj.  'etwas  (Akk.) gut  zusammenbringend,  leicht  sich  er- werbend'; x''ar^n5 . .  °i^m  (ASü.)  xraha/^m Uiin  saa»m  "die  Herrlichkeit  .  -,  die  sich
```


## [2026-09-14T03:10:29.370Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== HRN leaf 131 (p.110) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==131' HRN.txt; echo \"=== HRN 132 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==132' HRN.txt | head -40"
}
```


### [2026-09-14T03:10:30.422Z] TOOL RESULT

```
=== HRN leaf 131 (p.110) ===
-- 109 -
will auch np. /äsdk (jüd.-pers. T^^Z, Is. 7, 24) heran-
ziehen.
490. xiSm, xesm *Zorn*.
aw. aesma- 'Zorn*; phlv. /ism, x(h^fi^'
491. yi^eSTn 'bläulich, blauschwarz'; vergl. x^sisar (äähn. I,
157 Vers 510).
aw. a/saena- (Darmesteter, Et. ir. II, 53); phlv.
/asTn (Jamaspji, Pahlv. Dict. II, 421; falsch asgun,
asTu, 241), ;^ai;fm« oder axsin(?), vd. 22 (12).
kurd. stn, heslu 'blau ; afy. s7n bezw. xtn; oss. ä/sinäg
'Taube (46; vergl. Hübschmann, ZDMG. 38, 427/8);
sar. xoin, siyn. soin 'blau, yidg. ayßin (Tomaschek,
BB. VII, 204).
492. lele {jule) 'Wunde, Spitzes; Geschwätz', /ehden,
aw. hareöis; phlv. havak bezw. yarah^ vd. 2 (89).
Die Etymologie stammt von West (PPGl.s. vJialeh);
die Bedeutung der aw. und mittelp. Worte ist unsicher,
ebenso die Grundbedeutung des neupersischen. Im Men.
fasst West päzJiala als 'foolish, silly'. de Lagarde,
Beitr. z. altb. Lex. 38 wollte aw. /"ara- * Wunde' ver-
gleichen.
493. %ufn^ ;^Mw/;, yiimh Topf, Krug , /umre (HIOID, Is. 13, 12).
aw. /umba- *Topf ; phlv. yurnb*^ ai. Jcmnhhd',
kurd. LW. /um: bei. kumb, n. fftimh 'Teich, Pfuhl;
mit Wasser gefüllte Vertiefung im Felsgestein* (204);
wa/. Imbun,
494. fmkde 'Gelächter, ymdtden.
phlv. /andlta^i, yandak (PPGl.).
kurd. kenin 'lachen' ; bei. kandag, n. Uanday, yanday,
LW.') handag (186); wa/. känd-am, sar. söwrf-am (?).
oss. d. ;^odww, t. ;^wd/w (303) scheint hiervon ge-
trennt werden zu müssen und zu [/^svad- zu gehören.
Oder ist doch Urverwandtschaft vorhanden?
ffindeq 'Graben' siehe s. v. kenden (No. 869).
») Vergl. Bartholomae, ZDMG. 44, 550.
I
=== HRN 132 ===
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
```


## [2026-09-14T03:10:53.419Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== BRT 5197 ctx ===\"; sed -n '5190,5200p' BRT.txt; echo \"=== HRN axur ===\"; grep -n -i \"Krippe\\|axur\\|ä/ur\\|a/ur\" HRN.txt | head -20; echo \"=== HUB xvar ===\"; grep -n -i \"Krippe\\|x'ar-\\|xvar\" HUB.txt | head -20"
}
```


### [2026-09-14T03:10:53.516Z] TOOL RESULT

```
=== BRT 5197 ctx ===
Zum  V.  az-;    zu  S  25/-    t  oder  2  c.   —    Pü.: j.  avf  Y.  j7.  25:  lies  <kv,  sd. •  j.  'avö  Praev.   (nur  mit  xsn-1-)''   dnw.
•  g,  'av5  Int  'zu  helfen':  /lyat  7'lsSnt>J (sd.)  df^gvantitn  a"  Y.^2. 14;  —  yJ  du- raofsm  saa/ayat  (sd.)  a"  Y.J2.14.
Zum  V.  mr- ;  vgl.  'ot-aA-,  —  Pü. :  /lyäi.'äriA, ö  ay'.
•  g.  avöi  Inteij.  'wehe!',  als  SubsL:  asifyj affhlu^  177'°  ari/ial  apsmim  "denen  wird Wehe  werden  am  letzten  Ende  des  Lebens" V.45-3-
Ableit.  {avami-\  —  Vgl.  S-,-öy/i,  vaySi.  —  PÜ.: pa  Bsaii  andar  as?5n  aiiäk  ast  ISi  0  11«  apatiim, y  az-ei  YL  4-   I-  Ues  «iV.
•  j.  avö.däta- Adj. 'ins Wasser  gelegt' (?)": upa  tu  nS  aiwyästa  bartsma . .  aiwySsl^m anabdütsm  (sd.)  'tim  Vyt.  2j,
i)  Nach  Gdk.  KZ.  28.   187   und  Dst.  ZA.  2. 671  wire  avö  Praev. j.  aviirisyäl:  S.  un-ti^s-.
•  j.  avo.x'ar^na-  n.Tränke':  gaeyaoitis^a maSianyhsca  -näsca  Y.  2. 16;  — gaoyaoili- nqm^a  magiananqmla  "itanqm^a  Y.  7.  ifi.
'Eig.  (aU  Adj.)  'WässerCm-'oA-jgcnuss  bietend'. Vgl,  GON.  KZ.  2S.  186  (gegen  Hbu,  PSt,  5). —  Pü.!  äp  j^ar,  Sü. :  i'OT-iiw  t«M/(i  (wozu Sp.  Komm.  2.  68).
•  j.  a-vint-  Adj.,  PPA.:  s.  bn-.
j.  m-n«  Vi.  A  7,  36:  s.  an-,  -  N.  p:   lie.-.
=== HRN axur ===
=== HUB xvar ===
136:*) ^gl- jfid. tat. ovxur *Krippe* (Miller p. 75; «u qv 'Wasser'
8319:xsaet^m, syr. noch 1tt?D*lD = xvarxs(^d Hoffmann, Aus-
8391:xvarxsBd ^^ zd. hvare xsaetem,
9382:—13, JRAS. 1894, 463). Np. xursBd 'Sonne', ^yr.xvarxm^
10254:andarxvar 18.
```


## [2026-09-14T03:10:55.685Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== AFM khavarnaq ===\"; grep -n \"خورنق\\|الخورنق\" AFM.txt AFM_alt.txt AFM_pages.txt 2>/dev/null | head; echo \"=== FVQ ===\"; grep -n \"خورنق\" FVQ.txt FVQ_pages.txt 2>/dev/null | head; echo \"=== LKT ===\"; grep -n -i \"chawarnaq\\|Chawarnak\\|khawarnaq\" LKT.txt 2>/dev/null | head"
}
```


### [2026-09-14T03:10:55.785Z] TOOL RESULT

```
=== AFM khavarnaq ===
AFM_alt.txt:3425:وفه کانت E‏ اکا ل ( خورنقی رک من خورن ای | اک ومن CC‏ ای 
=== FVQ ===
=== LKT ===
```


## [2026-09-14T03:11:06.082Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '110,145p' HUB.txt"
}
```


### [2026-09-14T03:11:06.152Z] TOOL RESULT

```
14. Kurzes a im Aniaut hatte abfallen miissen, also wird
dran u. s. w. die Vichtigere' Form sein, vgl. die kas.
Dialectformen orinj u. s. w.
16. Ich wiirde np. art fiir contrahirt aus aoari (vgl. arad
aus avarad *bringt* halten), wenn das Wort nicht are
lautete, wie mir No Id eke aus Reimen (mit bar-e, mar-e
etc.) nachweist, vgl. kas. orE^ are,
Ueber das Vorkommen von np. avar certitudo',
avan 'flde dignus' vgl. Mann, ZDM6. 47, 701. Ist fur
phi. paz. evar 'certain , evarth 'certainty', evarik certain
(Shk. p. 243 etc.) avar u. s. w. zu lesen? An e = adhi
(das weder im Zd. noch im Ap. vorkommt) glaube ich
nicht.
17. Ist unsicher, da im Ap. ebensogut arika *feindlich* (zu
skr. ari' Teind*) gelesen werden kann, das im Np. zu
*rig geworden ware. Aw. ara^ka, Beiwort der Ameise,
ist dunkel. Die Form rey belegt Vullers aus Firdusi.
20. Fiige hinzu: np. dzard-a = zd. azareta- *beleidigt\
Sal. Shuk. geben freilich azurdan *kranken fiir
Vullers' Ozardan. Dazu stimmt afgh. LW. azurda
afflicted, sad*.
24. Zd. dstdrayettti ist mit Darmesteter, Le Zend-
Avesta II, p. 66, Anm. 7 durch *sundig, schuldig machen'
zu ubersetzen und als Denom. von *a8tara- = parsi
astar *Sunde' zu fassen; es geh5rt zu zd. anastareta--
ohne Schuld, ohne Siinde'. Ap. ma starava wird von
*) ^gl- jfid. tat. ovxur *Krippe* (Miller p. 75; «u qv 'Wasser'
= np. CUb.PERSISCHE STUDIEN
VOK
m HtBSCHMANN.
STRASSBURG.
VERLAG VON KARL J. TRttBNIlR.
1895.- 8 —
neben ap. sit/dti-, np. savam neben ap. asiyavam. Laut-
lich wiirde OSiyana ein ap. ^asidana- oder ^Osadana^
(vgl. np. piyada = skr. padati-) voraussetzen, das viel-
```


## [2026-09-14T03:11:12.091Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for n in 14 15 16; do echo \"=== HUB leaf $n ===\"; awk 'BEGIN{RS=\"\\f\"} NR=='\"$n\"'' HUB.txt | head -45; done"
}
```


### [2026-09-14T03:11:13.108Z] TOOL RESULT

```
=== HUB leaf 14 ===
H9f
=== HUB leaf 15 ===

=== HUB leaf 16 ===
y
5. Aus zd. *apu&ratanu- konnte np. nur bustan u. s. w.
(mit b im Anlaiit) werden, da das Gesetz besteht: die
kurzen Vocale a, i, u vor einfachen Consonanten fallen
im Neupersischen stets ab. Also ist np. dbistan aus
'^abustan auf zd. ^apud^ratanu- oder nur *apu&ra- *be-
kindet* (mit spater zugesetztem tan, vgl. x^^tan) zu-
riickzufuhren, wie auch die von Horn angefuhrten
Dialectformen ^) zeigen, die samtlich a haben. Zd.
apud^ra- schwanger steht fiir ^Opu&ra- neben richtigem
apu&ra- *kinderlos'.
6. Np.a&«5i3C^ar beiFirdusi (ed. Vullers) I, 439, v. 103.
Das Wort wird das Thema dpi- ^Wasser enthalten 2),
das doch noch nicht endgiltig durch Bartholomae
aus Bh. I, 95, 96 {apiyd, apisim) beseitigt ist. Jeden-
falls ist Bartholomae's Erklarung des np. abis-
(aus avah') unbegriindet und nicht zu begrunden, zumal
ein avah' 'Wasser durch Geldner KZ. 28, 186 fur
das Awesta nicht erwiesen ist.
7. Vgl. g. tag Teuer ZDMG. 36, 61, arm. LW. afas
*Feuer Sebeos p. 27.
8. Np. dxur 'Stair = phi. dxur oder besser ax^ar (Yatkar-i-
Zariran p. 63, Nr. 49), arm. LW. axovy kurd. LW. ax6r
(Socin, Samml. II, 281), afgh. LW. Oxdr setzt offenbar
ein zd. "^ax^ara- oder a-x^arena- voraus, das sich nur
^) Dazu noch paz. awastan = phi. dpustan 'pregnant* Shk. p. 234.
^) Dies liegt doch naher als mit Mann (ZDMG. 47, 701) zd.
aiwisx^aresa *trinkbar* heranzuziehen and Anlehnung an ab 'Wasser*
^p;;uneh|nen,
```


## [2026-09-14T03:11:24.821Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== HUB leaf 17 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==17' HUB.txt | head -30"
}
```


### [2026-09-14T03:11:25.871Z] TOOL RESULT

```
=== HUB leaf 17 ===
— 6 ~
im 2. Gliede mit zd. avo-x^arena- = phi. apx^ar^)
(so, nicht avx^ar ist zunachst zu lesen!) deckt.
Zd. avdx^arena- miisste im Neupersischen den Laut-
gesetzen nach durch *dx^arr = *dxur vertreten sein.
9. Ap. A^Hna- kann nicht sicher als persisch gelten, da
der Mann ein Susier war, wie die Inschriften zweiter
Art ausdriicklich sagen.
14. Kurzes a im Aniaut hatte abfallen miissen, also wird
dran u. s. w. die Vichtigere' Form sein, vgl. die kas.
Dialectformen orinj u. s. w.
16. Ich wiirde np. art fiir contrahirt aus aoari (vgl. arad
aus avarad *bringt* halten), wenn das Wort nicht are
lautete, wie mir No Id eke aus Reimen (mit bar-e, mar-e
etc.) nachweist, vgl. kas. orE^ are,
Ueber das Vorkommen von np. avar certitudo',
avan 'flde dignus' vgl. Mann, ZDM6. 47, 701. Ist fur
phi. paz. evar 'certain , evarth 'certainty', evarik certain
(Shk. p. 243 etc.) avar u. s. w. zu lesen? An e = adhi
(das weder im Zd. noch im Ap. vorkommt) glaube ich
nicht.
17. Ist unsicher, da im Ap. ebensogut arika *feindlich* (zu
skr. ari' Teind*) gelesen werden kann, das im Np. zu
*rig geworden ware. Aw. ara^ka, Beiwort der Ameise,
ist dunkel. Die Form rey belegt Vullers aus Firdusi.
20. Fiige hinzu: np. dzard-a = zd. azareta- *beleidigt\
Sal. Shuk. geben freilich azurdan *kranken fiir
Vullers' Ozardan. Dazu stimmt afgh. LW. azurda
afflicted, sad*.
24. Zd. dstdrayettti ist mit Darmesteter, Le Zend-
```


## [2026-09-14T03:11:27.512Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for n in 688 689 690; do echo \"=== IEC leaf $n ===\"; awk 'BEGIN{RS=\"\\f\"} NR=='\"$n\"'' IEC.txt | grep -n -i \"sṷer\\|swer\\|1348\\|1347\\|cut\" | head -20; done; echo \"=== grep xoreh ===\"; grep -n -i \"xōra\\|xora 'lepros\\|leprosy\" IEC.txt | head -20"
}
```


### [2026-09-14T03:11:28.566Z] TOOL RESULT

```
=== IEC leaf 688 ===
=== IEC leaf 689 ===
=== IEC leaf 690 ===
=== grep xoreh ===
8007:kroupos (kreup-) ‘rough, gritty; roughness; grit, scab’. WP I, 481. See kreup-, krüp- OHG cf. hriuva (for *hriuba ‘scab’ or «leprosy?) (e-gde as also) OE hrēof “rough, scabby’; ON hrjüfr, id.; Latv. kraupis, kraupa ‘scab, mange’; (o-gde in) OCS krupa ('groat, crumb’, and com. Sl.); OCZ. krupy ‘coarse’; cf. Blg. krupen, adj. id.; Li. kraupüs “rough, rugged”; Latv. kraupis & kraupa (beside kr-) ‘scab, mange’; kraupis (2) *toad'; kraupes, pl. ‘wrinkles’
8041:krüp- (1) “rough”, hard, crusty; roughness, hardness, scab’. Cf. kreup- Alb. kripë ‘salt’; krip, kryp, v. id.; OHG brut, MHG ruf, rufe, s. wf. ‘scurf; leprosy’; G Rufe ‘roughness, scab, crust’; ON hrufa, f. “rough surface’; cf. G rüften ‘get scabby’; (long-gde in) OE hrýfing ‘scabbiness’; Li. (Žemaitē) krüpis, krüpe ‘toad’; Latv. krupis, id.; Li. cf. krumpü, krüpti ‘get scabby’; ON hrufla, v. ‘scratch’; EMDou. rove, f. ‘scab’
9087:Krb- (Krob-) (?). Cf. WP I, 418 Lat. cf. carbunculus, 1, m. (tumour, smut in trees? beside carbo, onis; W (r-gde?) crafu, v. “scratch, scrape’; Blg. sárbja, v. ‘itch’ beside R srab, m. (o-gde) “itch, leprosy’
9237:Kueitolos, is, io ‘brightness, whiteness’ Skt. cf. (vrddhi) $vaitarih “white cow’; $vait- ryam ‘leprosy’; Li. $veitalas ‘polish’
9240:Kueitros (Kuitros), variant of Kueitos, Kuitos, q.v. WP I, 470 Skt. cf. (vrddhi) $vaitryam ‘leprosy’ beside $vi- tráh ‘white’; Li. Sveitrüs ‘bright’
9337:Kuitros, us (variant of Kuitos CU). WP I, 470 Skt. $vitráb (^white"; s. leprosy’); Arm. cf. &rt- um ('dazzling', fr. *Kuitr-umo-); Li. $vytrüs “flashing”
9685:lepos (2) “leaf, petal, peel’. Cf. lop- Gk. lépos, gs -eos, n. & lepís, f. “scale, shell", cf. also Hes. lepastís, f. ‘scale; limpet': R lè- Dest, f. “strip; petal; leprós ‘scaly’; lépo, v. (peel. Adj: leptós Ou: lépra ‘leprosy’; LLat. (Ps. Apul) cf. penplepios 'spurge-laurel, lit. “five leaves', from its terminal cluster; Ir. leo, m. ‘film, esp. of oil on water’; Slovene f. lepen, m. “leaf”; R cf lépestt, f. “strip; petal; Srb. cf. lepetati, inf. ‘flutter’
10213:Skt. luta ((2) “a skin-disease; (?) leprosy’); Lat. lūtum ‘yellow dye’; ON lúða, f. ‘halibut’; Li. liútas, m. “lion?
14794:roupos (3) ‘rough; roughness’. Cf. (1) and (2) Latv. raupjš, adj. ‘rough, shaggy’. Other iso- phones ambiguously to (1) or (2), but cf. also Li. raupsai, pl. ‘leprosy’; raupežē, f. ‘frog
17993:suer-, -on, -en (suor-, sur-) (4) 'swelling, suppuration, gangrene, ulcer. Cf. suer- (3) above. Av. xwaro, m. *wound'; Per. xware, s. 'gan- grene; leprosy?’ beside re, adj. ‘malignant’; Oss. cf. xàlmag, xwálmag, s. ‘scab, wound’; W cf. chwaren, f. (“gland”, fr. *suoren-); chwa- rel, m. (“breast tumour’, fr. *suorel-); OHG swéro, wm., MHG swér(e), s. & wm. ‘ulcer’;
18934:treudo, io (2) “fail, decay ON prjóta, sv. 2. "Ta: Sw. tryta, v. id.; *-ü- in Late trüdu, et, v. ‘decay’; trüda, f. ‘humus’; trüdi, mpl. "rot: (*-ü- in) Go. pruts-fill, OE prust-fell, s. ‘leprosy’; (G Ver-druss, m. either here or to treudó (1))
19005:trondis, os ‘rot, mould'. (Li. also *trend-) OCS trodü, m. 'touchwood; leprosy’; Cz. troud, Slovene trod, m. ‘tinder’; Pol. trad, m. *leprosy ; Li. trandis, gs: -iés, f. ‘rot, woodrot'; (e-gde: trendu, eti, v. “get wormeaten' beside trenu, êti, v. *decay). (OE e-gde isophone: printan, v. 'swell")
19117:trust- (2) ‘filth, ooze’ Ir. cf. trostar, m. ‘filth, dirt’; OE cf. brust- fell, s. leprosy’, lit. ‘foul skin’); Cz. Dest, gs: tresti, f. extract, juice’. (ISophone: W trws, pl. -oedd, m. ‘covering, dress’)
```


## [2026-09-14T03:11:42.957Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\n# find line number 17993 offset\nlines=t.split('\\n')\noff=sum(len(l)+1 for l in lines[:17992])\nleaf=t[:off].count('\\f')\nprint('leaf(0-based ff count)=',leaf, 'approx printed page=', (leaf-15)*2)\n# print surrounding suer entries\nfor i in range(17984,18000):\n    print(i+1, lines[i][:300])\nEOF"
}
```


### [2026-09-14T03:11:44.103Z] TOOL RESULT

```
leaf(0-based ff count)= 742 approx printed page= 1454
17985 30
17986 35
17987 40
17988 45
17989 1348
17990 sweran, wv. ((respect', lit. ‘weigh, consider’, fr. swérs ‘honoured’, lit. weighty"); Li. sveriù, sveiti, aor: sveriau, v. ‘raise, lever up’; Latv. sveru, svert, tr. & intr. ‘weigh’. (Long-gde in) Av. xwairis, f. ‘blame’; Per. xwar, adj. “indi- gent; Go. swērs, adj. 'honoured', lit. ‘weighty’; MHG s
17991 suer- (2) (suor-) “call, declare, state, speak, utter’. WP II 527 Skt. svaràmi, v. ‘sound; sing’; Gk. érō, éromai, v. ‘ask’; eíro, v. (2) “say, speak, tell’; cf. eirén, gs: -énos, m. “youth of speaking-age in Spar- tan parliament; MHG swéren, sv. 6. ‘swear’; OE swerian, sv. 6. id.; (o-gde in) Cz. ne
17992 suer- (3) “harm, hurt, corrupt. See next Skt. svaràmi, v. (1) ‘blame’; Av. xwar-, v. “blame, injure’; xwairis, s. “abuse, blame"; Per. xware, s. ‘corruption, gangrene’; cf. xire, adj. ‘malignant’; MHG swérn, sv. “hurt; suppurate’
17993 suer-, -on, -en (suor-, sur-) (4) 'swelling, suppuration, gangrene, ulcer. Cf. suer- (3) above. Av. xwaro, m. *wound'; Per. xware, s. 'gan- grene; leprosy?’ beside re, adj. ‘malignant’; Oss. cf. xàlmag, xwálmag, s. ‘scab, wound’; W cf. chwaren, f. (“gland”, fr. *suoren-); chwa- rel, m. (“breast tumo
17994 1349
17995 (Z-gde in) G Geschwür, id.
17996 suer- (5) “post, pole, pillar, stump’. Cf. suir-. (Lat. ambig.) Skt. sváruh, m. id.; Gk. cf. hermís, gs: hermí- nos, f. id.; Lat. (ambig.) surus (“bough, stake, palisade’, fr. *suer- as in vocalism of vulva: Gk. eiláo or fr. type *guelbh-, oe: vult ^wishes', fr. *uel-, cf. (alleged) OLi. pa-velt, id
17997 suér- (1) “heavy, hanging”, etc. See suer- (1)
17998 suér- (2) ‘tasty, piquant' in Tokh. swar, B sware, adj. (sweet, pleasant; Li. svere, f. ‘winter cress’: Latv. cf. (?) përkoni svere(s) *ground-ivy'
17999 suerbh- (suorbh-) (1) ‘twist; thong, rope". WP II, 529 and squerbh-. (Gmc. ambig.) Arm. karb, i, iv, s. “asp, basilisk’; Tokh. A svarp, sparp, s. ‘rope’; W cf. chwerfu, v. ‘spin, roll": chwarf, pl. au f. ‘whirl; rocket’, fr. *suorbh-; OFris. swerva, MHG swérben, sv. 3. ‘swerve’; ME swerven, id.; Du
18000 suerbh- (2) ‘wipe, smooth, lay out. (var. suorbh-). Cf. squerbh- Go. af-swairban, sv. 3. ‘wipe off; OE sweor- fan, sv. 3. ‘wipe; polish, file, scour’; ON sverfa, sv. 3. file’; cf. Swiss schwarben, v. ‘lay in swaths and E dial. swarf, s. “black grease from machinery'
```


## [2026-09-14T03:11:57.794Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for n in 239 240 241 242; do echo \"=== BQT_v2 leaf $n ===\"; awk 'BEGIN{RS=\"\\f\"} NR=='\"$n\"'' BQT_v2_pages.txt | head -25; done"
}
```


### [2026-09-14T03:11:58.814Z] TOOL RESULT

```
=== BQT_v2 leaf 239 ===
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
=== BQT_v2 leaf 240 ===
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


=== BQT_v2 leaf 241 ===
 ‫‪“VAY‬‬                                                                                                      ‫خوای‬
‫هر گاه‬    ‫چنانکه‬   ‫ارادی باشد‬     ‫راستی » بمعنی‬         ‫سازند ‪ ۱‬؛ وبایتمعنی بقتح اول بروزن ملازه هم‬
‫کوبند «حر کت خواسی » ازآن حر کت ارادی‬                                                                ‫آمده است ‪.‬‬
                                        ‫خواهدد ‪.‬‬
                                                         ‫خو اس س بانانی معدوله بروزن طای‪.‬‬
‫حو اسه = بفتح اول بر وزن نواسه ‪۰‬‬                        ‫بمعنی خواستگار و طلبکار باشد ‪ -‬و بفتح اول‬
 ‫نند‬ ‫صورتی باشد که در فالیزها و زراعتهپا نکصب‬             ‫بروزن‌پلای» بمعنی تریس و بیم وهرای باشد ‪.‬‬
‫تا وحوش وطبور ازآن رمیده خان بکشت زار‬
                                        ‫فسرانند ‪.‬‬
                                                        ‫وجزیر؛ مبان دربا باشد؟ ہے‬            ‫فته شده ‪- ۴‬‬        ‫راه‬

 ‫اه بائانی معدوله وسکون کاف‬   ‫خو‬                         ‫و طلب چیزی از کی کردن را نیز گوبند ‪- ۴‬‬
‫فارسی * مرغ خانگی رگوابند ‪ -‬وتخم هرغ را‬                  ‫وبمعنی زر ومال وسامان هم‌هست_ و گاهی یمعتی‬
 ‫نکیفزته اند کوخیوناه (‪ )۱‬تخم مرغ بروغن‬                  ‫اراده گفته مشود چنالکه گویند « خواست خدا‬
                                ‫«ربان کرده باشد ‪.‬‬                         ‫‪.‬‬       ‫‪۵‬‬   ‫اراد خدا‬   ‫شی‬    ‫نود ‪٩‬‏‬   ‫رین‬

 ‫خو ال ‪ -‬با انی معدوله بروزن مال »‬                       ‫‏‪ me‬بائانی‌معدو له باس‌داز ‪۰‬‬       ‫خواستار"‬
 ‫دوده‌ای که بحهت ساختن سداهی ومر کب از دود‬
                                                         ‫لر وکواکار ور خواهتده و طلت هه را‬
‫چراغ کیرند؛ و صم اول بروزن جوال همأ مده‬                                              ‫کوند ‪#*.‬‬
           ‫است ‪ -‬وخوردئی را نگیوزبند *‪.۹‬‬
                                                         ‫خو استه ‪ = ۷‬بائانیمعدو له بروزن راسته»‬

                                                          ‫لءاه‬
                                                             ‫زر ومال واسباب وجمعدت ومامان وملك وا‬
=== BQT_v2 leaf 242 ===
‫خوان پابه‬                                                                                                      ‫یز پا‬
                                                      ‫خوالگر ‪ - ۱ )۱‬باانی معدوله بر باشد ‪.‬‬
‫حوان ه با نانی ممدوله بر وزن نان »‬                               ‫وزن شالگر (‪ .)۷‬مطبخی و طباخ و طعام پز را‬
‫کنابه ازخوردنی وماده باشد ‪ ۵‬و‪-‬طبق بزرگی‬                          ‫گویند ‪ - ۴‬و بمعنی سفره چی هم بنظر آمده‬
                                                                                                                    ‫است‬
          ‫را یز گوبند که از چوب ساخته باش‬
     ‫طندبچه‬
     ‫ق‬
‫کوچك راخوانجه گویند ‪ -‬وخاروخلاشه وگیاه‬                           ‫خو‌الی‪ -‬باانی ممدوله بروزن عالی»‬
‫خودرو را نگیفزته اند که از ميان زراعت قوت‬                         ‫وزبند ‪ - ۴‬ورود‬‫زیبا ومهنا باشد ‪ -‬وطعام رگای‬
‫برهسماند ‪ - ۷‬وبمعنی چیزی خواندن وطلیسن‬                           ‫خانهٌآب را همگفته‌اند ‪ -‬و بمعنی مطبخی نیز‬
‫هم هت ‪ - ۷‬و امرباین دومعنی آیمزده است‬                            ‫؛بکراول بروزن نهالی هم‬
                                                                                      ‫بنظرآمده است ‪ ۴‬و‬
                                 ‫بعنی بخوان وبطلب ‪. ۷‬‬                                                  ‫‪۰‬‬       ‫ات‬   ‫درست‬



‫خوان پایه ‪ -‬با انی معدوله و بای‬                                   ‫خوالیگر ‪ - ۴‬بنانی ممدوله بروزن‬
‫فارسی بالف کشیده وفتح نحتانی‪ .‬دستار خوالرا‬                        ‫بازیگرطباخ‌ومطبخی‌وخوالالار وسفره چی‌باشد؛‬
                                                ‫‪.‬‬     ‫فمف‬
                                                                   ‫و بکر اول نیزگفته اندکه بر ونزانلیگر‬
                                                       ‫‪:‬الك‪.‬‬
                                                           ‫(‪ )۲‬خم ش‬                 ‫(‪ )۱‬خ‪٠‬‏ ‪ :‬خوالك ‪.‬‬

        ‫‪۰‬ص‪.‬‬
```


## [2026-09-14T03:12:08.000Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for n in 243 244; do echo \"=== BQT_v2 leaf $n ===\"; awk 'BEGIN{RS=\"\\f\"} NR=='\"$n\"'' BQT_v2_pages.txt; done"
}
```


### [2026-09-14T03:12:09.051Z] TOOL RESULT

```
=== BQT_v2 leaf 243 ===
 ‫‪۷‬‬                                                                                             ‫خوانچة زر‬
                                                ‫خو) نجه‪ .‬ررو خوانجه‌دد لن‪-‬‬
                                                         ‫‪۱ ۶‬‬       ‫‪۰‬‬     ‫‪۰‬‬         ‫‪۰‬‬       ‫‪۰‬‬      ‫‪۰‬‬

‫خواو؟ = با ثانی معدوله بروزن گاو ‪۰‬‬
   ‫بممنی خواب است که بعربی نوم خوانند ‪*.‬‬
                                                 ‫‪“e‬‬                                    ‫‪6‬‬          ‫‪۲‬‏‬
                                                      ‫و حوانجه‬               ‫سهر‬       ‫خوانجه‬
        ‫مال واسباب وخواسته وخواستنی باشد ‪.‬‬
   ‫‪۲‬‬            ‫‪8‬‬            ‫‪0‬‬
‫د بمعنی خوش ولیکو باشد ‪-‬‬         ‫حوب"‬                                           ‫خورشید آنور باشد ‪*# .‬‬
        ‫‪۹‬‬   ‫ویمعمی محکم واستوار نىزآمدە است‬

                                                 ‫افن‌سالاراست که‬
                                                               ‫بی‌نقطه بروزن‌جاندار‪ .‬خموخف‬
 ‫دن ‪ -‬بمعنی نرك عادت‬
                   ‫رار‬
                     ‫خکو ی‬
                                  ‫دادن باشد ‪۰‬‬                                ‫بکاول سوفره چی باشد ‪. ۷‬‬
‫انی » زرد لوی‬
            ‫گو‬‫خوبانی‪ -‬بروزن چ‬
‫باشد که مغز بادام در درون آن‬       ‫شده‬   ‫خشك‬     ‫و طباخ باشد ؛ و گویند بکاول ترکی است و در‬
                                                                       ‫هندوستان چاشنی گیر خوانند ‪.‬‬
‫بابای‌فارسی وخای قطه دار‬   ‫حو بخین ‪4‬‬            ‫خوان لاه کناه از خوانی باشد که‬

‫بروزن دوریین » بممنی مومیابی است وان کانی‬        ‫وهعدی‬   ‫عام دردهند‬          ‫انند و صلای‬       ‫کرعمان ‪,‬نگ‬




                                                       ‫)‪ ۱‬چك » چش ‪ :‬انسانی وکالی‪.‬‬

  ‫‪ - 8‬یز نام بخشی اگلزیابگان واقم در دره‌ای کوهستانی‌وخوش آب و هوا ‪ .‬م رکز آن‬
  ‫خوانار باهفت فربة اطراف ‪۰۰۰۷۱‬سکنه دارد «کنهان ‪.‬جفرافیای سباسی ‪ ...2 ۴. ۸۰4‬چنان‬
  ‫=واب (‪ ۴ . ).).‬اسم مصراز‬   ‫برددصبر ازدل که‌تکران‌خوانبخمارا»‪«.‬حافظنیرازی‪ ۴ »۳‬خ‬
   ‫‪٩‬‏ ‪ -‬پازند ‪. 802‬افتانی ع ‪( 05‬قشنك)»ساس کربت_‪(5۷۳3۷115‬ازلا‪( 5‬خوب)‬                             ‫دخواستن» ‪.‬‬
   ‫‪( 51۱02۷ +‬شکل‪.‬صورت ؛زسابی ) « هویشمان ‪ . › ۳۰۵‬پهلوی ‪ «01۱0‬منای ‪۲2۷ ۷۷۲6۰‬‬
   ‫«مینا ‪ ×0 ۹۳۱۰‬داونوالا ‪» ۱4۲۲‬گیلکی وفربزندی ‪, 0۵‬برنی ‪0‬ل‪ ,5‬نطنزی‪۵.۱ « 0625‬‬
                                                ‫ص ‪۲۹۲٩‬‏ » شهمیرزادی ‪« 00‬ك‪۷۷۱٩ ۷ .‬‏ ‪.‬‬
   ‫‪ ۵‬خوالدن ‪ -‬بفتح اول و پنجم » بووزن هماندن » از ريشة اوستایی ×‪-٥3۷‬‏ پپلوی‬
    ‫(یز ‪« 02002۷5‬مینا ‪« ۲ : ۹۳۱‬اونوالاه‪ ) »۸4‬؛ ربش هندی باستانی‪,88۷5-‬‬ ‫‪0‬‬
    ‫‪( 1120‬صدا دادن)‪ .‬کردی ‪( 81۳0 . 81۵۵۷۲‬فرائت کردن) » استی ‪8106:01061‬‬
  ‫( بامیدن » صدا کردن» دعوت کردن) ‪ ۰‬وخی ‪( 012-021‬سخنکفتن‪ .‬کفتن» «اسشق ‪[ ۹۹46‬از‬
   ‫دن(یوندمصدری) ] ‪ :‬فرائت کردن " مطالعه کردن ‪ -‬دعوت‬           ‫‪+‬‬               ‫خوان ‪nãvx‬‏ «مسینا ‪۹‬‬

                            ‫کردن » بمهمانی خواستن ‪ -‬دعاکردن ‪ -‬تغنی کردن‪« .‬ناطم الاطباءِ > ‪.‬‬
   ‫‪ #‬خواهر ‪ -‬بروزن مادر ‪ .‬اوستا‪( ۲212۷1-‬خواهر) ‪ .‬بپلوی ‪ » 7212۷‬هندی‌باستان‬
   ‫‪ . 7262۷5‬ارمنی ‪ , ۲106‬کردی ‪ . 61۵2 2۵0 , ۲۵2‬افنانی ‪»۲۵۳‬استی ‪. ×0 , 6۲02‬‬
    ‫بلوچی ‪ . ۲2۷8 . 1۵068 ۲2۵۷8۰ ۰ ۲802۷8‬وخی ال س؛ربکلی ‪ 2۷2۰‬منجی ‪8۷63۷۰‬‬
    ‫سنکلیجی ‪« 4۷51‬اسشق ‪» ۱۰۵‬ر کک‪ :‬هویشمان‪*۱‬ه؛استی‪.05«2‬است ‪ ۰8۱‬گیلکی ‪ ۴10522‬؛نطنزی‬
   ‫‪ ۱ . 1: 78‬ص ‪٩ ۹۸۲‬‏ ‪.‬سمنانی ‪ , 8۵۳‬منگری ‪ . 681.۵2‬سرخه بى ‪ 625‬؛‬
   ‫لاسگردی )‪ » ×4‬شهمیرزادی ‪4 ۳8121‬ك ‪ ۲.‬ص ‪ » ۸۸۱‬طبری خواخر «صاب طبری ‪ ۳۷۳‬؛‬
                   ‫‪.‬‬   ‫اشدخ»ت‬
                            ‫دختری که باشخص هم پدر و مادر باشد با دریکی از آ نان مشتركك با‬

=== BQT_v2 leaf 244 ===
 ‫خود خروه‬                                                                                ‫”‪“YA‬‬


 ‫دایر‪ - ۷‬ویمعنی‌ذات و لقیض‌غیرهم آمده‌انت ‪۷‬‬         ‫و لام الف »‬   ‫کلاا صیفتح کاف‬        ‫خوب‬

‫ونان‬
   ‫چ‬        ‫چدنریان‬
                  ‫چنالکه کوبند ف«لانی خو‬
‫میداند؟عنی ذات خود راله دمگریرا »ودر نع‬             ‫خوب کلان۔ بر وزن موی کشان ‪.‬‬
‫مضاف مضمری آید ‪ -‬و ضد پیگانه هم هست‬                 ‫تنگه باشد ‪.‬‬ ‫بهاترضم‬
                                                                      ‫بمعنی خوب کلا است ک‬
‫چنانکه کوبند «فلانی ازخوداست » معنی بیگاله‬
                                 ‫يت ‪. ۸‬‬
                                                    ‫بای قارسی‬   ‫خو بله ‪٣‬‏ ا انی ممدو لد و‬

‫خود بر ست د باانی معدوله و کر‬
                                                            ‫بروزن طبله » بمعنی ابله ونادان باشد ‪.‬‬
  ‫ستا‬
    ‫خجبوردو‬
          ‫بای فارسی ؛ مردم متکبر و مت‬               ‫حوج ‪ -‬بروزن کوچ کله سر وفرق‌سر‬
                                       ‫باشد ‪.‬‬       ‫مرغانرا گونند ‏ وکوشت پار سرخی باشدکه‬
 ‫خود یسور ‪٩‬‏ با‪-‬نالی مسوله کور‬                      ‫برسرخروی است؟ ‪ -‬ونامگلی‌است سرخ‌رنگه‬
‫بای ابجد (‪ )۱‬و سین بی لقطه (‪ )۲‬بواو رسیده‬            ‫که آنرا بستان افروز کوبند ‪ -‬کووسفندجنگی‬
‫ویزای قطه دار (‪ )۳‬زده ‪ ,‬آتشکده آنربابجان‬             ‫رانز گفته‌اند ‪ 1 ۴‬وترك کلاه‌خودهم‌هست ‪ -‬وتبزی‬
‫است*‪٩‬‏ و بجای بای ابجد بای حطی (‪ )4‬نیز‬              ‫طاق وایوان را نگیوزبند ‪ -‬و حربر سرخیکه‬
                                      ‫هست ‪.‬‬                                  ‫بکرلوگاه نیز نندند ‪.‬‬

‫خودخروج‪ -۱۱‬با جيم فارسی »‬                            ‫خو چه ‪ - °‬بانانی‌نجهول بروزنکوچه‪.‬‬
‫به‌عنی تاج‌خروس است وآن گوشت سرخی باشد‬              ‫نمعتی دوم خوچ است که گل‌ستان افروز‪ -‬وتاج‬

                      ‫که برسرخروس است ‪.‬‬                                           ‫ومغفر خروی باشد ‪.‬‬
 ‫خود خروه؟ د باهای هوز‪ .‬بروزن‬                       ‫با ثانی معروف بر وزن زود »‬         ‫جود‪.‬‬

 ‫ومعنی خود خروس است که تاج و مغفر خروس‬                ‫بمعنی تاج ومخفرباشد ‪ - ۷‬وبائانی معدوله‌بمعن‬
                  ‫و کل بتان‌افروز‪ ۳۱‬باشد ‪.‬‬          ‫او باشد چنانکه گویند د خود داند » سنی او‬

     ‫(‪ )۳‬چك‪ _:‬شطه دار ‪.‬‬             ‫(‪ )۷‬چك ‪- :‬بی لقطه ‪.‬‬               ‫(‪ )۱‬چك ‪ :‬و کسربا ‪.‬‬
                                                                          ‫(‪ )4‬چك‪ :‬با‪.‬‬

  ‫رك ‪ :‬لفت فری ‪ ۵۹۰‬ورك‪ :‬خروج و خوچه‪.‬‬            ‫‪۴‬‬    ‫مصحف «خو بله»‪.‬‬     ‫‪۳.‬‬    ‫رکه‪:‬خوب کلان‬       ‫‪۱‬‬

                                     ‫غوچه (تاج خروس)‪« :‬اسفا‪۲ :۱‬ص ‪۰۷6‬‬         ‫عه‬    ‫‪۵‬‬    ‫غوچ ‪.‬‬
   ‫» تاج خروی‬   ‫ورك ‪ :‬خوچ ‪ « :‬خوج‬

   ‫(ر‬
    ‫‪ - ۱‬پارسی باستان ‪ 801121‬د‬                   ‫بود و خوچه نکیوزبند ‪« ».‬لفت فری ‪۵٩‬‏ ح‪٩۱‬‏ ‪.‬‬
    ‫خود سر تیز) « اثپیگل ص ‪. ۱۲۲۰‬استی ‪ (005‬کلاه ناح) «ك ‪ .‬است‪۱٤۸‬‏ =‬                      ‫‪09‬‬     ‫‪8‬‬
   ‫‪ - ۲‬ضمیرافس" پهلوی )‪×4۷‬‬              ‫پارسی خوی «لغت فرس ‪۱۲٥۰‬‏ ممرب آن خوذة «نفی؟ ‪.‬‬
   ‫ربک ‪« ۹۳۱۰‬مینا ‪۲٥ :۹۳۱‬‏ «ناوادبا ‪ ۷۹۱۰‬قس‪:‬پارسی باستان ‪ )2۷(01 -‬او ‪6687۷5‬‬
                                                                          ‫‪ ۵‬نی‬
  ‫(خود» خویش)‪:‬اسفا ‪ ۰۲ ۱‬ص ‪ ۰۹۱۳۷۸۳ ۰۱6۲ ۰۹۱۱ ۸‬استی‪« 8680621‬کث‪ .‬است‪› ۹۳۱‬‬
  ‫باين معنی «خودی»است‌و مقپوم آن از جملهمذ کور‬          ‫‪۸‬‬          ‫ورک‪ :‬ص لد از دباچه موف ‪.‬‬
  ‫‪٩‬‏ رکه ‪ :‬خود سوز‪.‬خودی سوز (ظ‪ ,‬مصحف ‪:‬‬                          ‫در متن مستفاد میشود نه از «خود) ‪.‬‬
  ‫‪۶‬أخون ازقول نظامی است ‪ .‬رکه ‪:‬‬
                              ‫م‬                      ‫خودیوز در شعر نظامی ‪ ,.‬ک ‪ :‬خودسوز) ‪.‬‬
                ‫خودی سوز ‪.‬مهمترین آآتشذکرد؛بایجان آذ رکشنپ است ‪.‬رکه ‪:‬کآذشرسب ‪.‬‬
   ‫‪۹۸۷‬‬   ‫حرهٌ‬
            ‫فد‬‫صبه‬
                ‫بق‬
```


## [2026-09-14T03:12:24.664Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for n in 245 246 247; do echo \"=== BQT_v2 leaf $n ===\"; awk 'BEGIN{RS=\"\\f\"} NR=='\"$n\"'' BQT_v2_pages.txt; done"
}
```


### [2026-09-14T03:12:25.605Z] TOOL RESULT

```
=== BQT_v2 leaf 245 ===
‫‪e Cs‬‬                                                                             ‫خجودرا رسن کردن‬

‫ونایه از علف خودروی هم‬
                     ‫و خودسر باشد ‪ -‬ک‬
                                                   ‫کر دن ‪ -‬کنابه از‬
                                                                             ‫خود رارسن‬

                                               ‫ت‬      ‫خود را محبوس کردن و بقید أنداختن باشد ‪.‬‬

‫حود نما۔ با ثانی معدوله بروزن‌بدتماء‬                 ‫خودستان ‪ -‬باانی مسوله وبزرن‬
‫شخصی را گویند که خود را بمردم وانماید ‪-‬‬             ‫شبستان » شاخ تازه ای باشد که از درخت تاك‬
‫کویاه خودرو را نگیفزته‌اند ‪ -‬وبمعنی خودستا‬          ‫انگور سرزند آونرا ببب خوشمز کی میخورند؛‬
‫ومتکبرهم‌هت * چه خودنمایی‌بممنی خودستایی‬                     ‫و بروزن بزرکان هم منظر آهده است‪٩‬‏‬
                                         ‫باشف ‪.‬‬     ‫م ثعاندیوله بر وزن‬
                                                                     ‫خودسور = با‬
‫معدوله‬     ‫بوااو‬       ‫حودی سور ‪/‬‬                   ‫وز » بمعنی خود موز است که نام آتشکدة‬
                                                                                                  ‫سرد‬
‫بمعنی‌خودسوزاست‬       ‫وسن بینقطه بروزن پبروز‪.‬‬                                ‫آذربایجان باشد ‪*#. ۴‬‬
             ‫که اكد آذرباسان بائد © ‪.‬‬               ‫ولهومیم بر‬   ‫الی‬
‫خور ‪ » ۱‬بثانی معدوله ورای قرشت‬
                                                                        ‫با‬
                                                    ‫وزن هنکامه “ بمعنی خود رای و بکام برآمده‬

         ‫سوز ‪.‬‬     ‫_ رك‪ :‬خودسوز » خودی‬     ‫‪۳‬‬        ‫‪ - ۱‬رك‪ :‬خوردستان ‪ ,‬خوردوستان ‪.‬‬
  ‫‪ -‬بعنی ازخود سوزد‬      ‫‪۴‬‬               ‫‪ ۱‬خحودکام اه (یسوند) ‪ .‬رك ‪ :‬خودکام ‪.‬‬          ‫‏‪۴٣‬‬
                              ‫رك‪:‬خود بسوز » خود سوز ‪.‬‬        ‫ا)رجی»‬
                                                                  ‫خمین‬
                                                                     ‫ربرز‬
                                                                        ‫دتیز‬
                                                                           ‫م لف‬
                                                                              ‫‌واد‬
                                                                                 ‫یهٌم‬
                                                                                    ‫باسط‬
                                                                                       ‫(بو‬
                                           ‫® ۔ درآن خطه (آذربایجان) بود آعتی سنك بست‬
                 ‫که خواندی « خودی سوز > آتس پرست ‪.‬‬
  ‫کنجینه ‪«۵0‬‬          ‫نظامی کتجوی‬
 ‫‪ - ۱‬اوستا ‪ 72۷1-‬ت هور(پارسی) ‏ اوستا ‪* ۲2۷2‬بهلوی (‪( ۲2۷5 )16015‬خورشید )‬
 ‫*اسفا‪۱:۲‬ص ‪۸1٩‬‏ «هوبشمان ‪.»۵۰۵‬هندی باستان_ ‪ ۵8۷۹‬کردی]‪ ۰ 058.81111‬استی ‪» 6061, 05‬‬
 ‫شغنی ‪« 711, ۲61‬اسشق‪ . 2« »۵۰6‬است‪»»۱4۱‬طبری لا » مازندرانی کنونی ‪« ۲661 ۰ ×۲0‬واژه‬
 ‫نامه ‪ .> ۶۲۳‬در اوستا هوره و هورشنه هم بمعنئی قرص خورشد و کر آفتاب است وهم از آن‬
    ‫فرشته‌ای اراذه شده است ‪ .‬غالبا صفات حاودان و باشکوه وتند اس وغنی بخورشید داده شده ‪.‬‬
  ‫بقبه در صفحه ‪۷۸۷‬‬
 ‫‪ +‬خود كام ‪ -‬هم اول و واو معدوله » بمعنی خودکامه («‪.‬م‪ ).‬است ‪« :‬بدان ای سر !‬                   ‫‪۱‬‬

  ‫که ‪ ...‬چون ساز رحیل کردم آنچه صیب مآنمده بودپیش نوفرستادم » تاتوخودکام نباشی‬
                                                   ‫و از اشاست برهیز کنی ‪« ».‬قابوسنامه ص‪. “۲‬‬

                                                                                 ‫بقیه از صفحهٌ ‪۵۸۷‬‬

  ‫‪ -۴‬بیرولی‌درالجماهر ص ‪(۱٩‬‏ ‪ ۲٩) -‬گوید ‪« :‬وجنی(من‬                     ‫سر کک ‪ :‬خود خروه ‪.‬‬
  ‫البند) بسمی خروهك و عرب بالخراهكوهوتشبیهلاصل البدبفلن وةالديك کماشبه به نوع‌من‌بستان‬
    ‫افروز عرض متشنج وبسمی خود خروه» جزو اول خود خروه ‏ همان خود (ناح » مففر ا)ست‬
  ‫وخروه‌لفتی ست درخروس (ه‪.‬م‪ ).‬و خود خروه خ(و=دخروج) لفة درست بمعنی « تاج خروس »‬
  ‫امت ‪.‬رك‪ :‬بعض فواید لفوی کتاب الجماهر بیرونی بقلم نگارنده در یادنامةٌ بیرونی چاپ ‪]886-‬‬
  ‫=اج خروی = ‪itneurc‬‏ ‪suhtnaramA‬‬         ‫‪ ۴‬ت‬       ‫‏‪ › Society‬کلکته ص ‪. ۲8۲۳‬‬
                                              ‫‪1‬‬ ‫‪2‬‬‫=‬‫‪7‬‬                 ‫«دارونامه ‪۰‬ا‬
                                                      ‫دکحترمد پ‪8‬ار‪1‬سا‬
 ‫‪7‬س‪( 62110 =12)۸0‬فر) «فرهنك فرانه ‪ -‬فارسی‪ .‬کازیمیر سکی»‬
     ‫ورك ‪ :‬یعض فواید لغوى کتاب الجماهر (مذ كور درشماة فبل) ص‪ ۳۸۲‬ورك ‪ :‬لفت‌فری ‪. ۷۲۸‬‬

=== BQT_v2 leaf 246 ===
  ‫خورخجیون‬                                                                                    ‫‪YAY‬‬


‫جوی کوچکیاست که‌ازرودخانةٌ بزر گی‌جدا کرده‬              ‫و نام فرشته ابست‬    ‫بمعنی روشنی بسیار باشد ‪-‬‬
‫وبن که‬
     ‫بزراعت برند ‪ - ۷‬و برزیگری را نگیز‬                  ‫مو کل آفتاب که تدبیر امور ومصالحی که درروز‬
‫جمبح امباب زراعت کردن و برزیگری را مهيا‬                 ‫خور وافم‌میشود متعلق بدوست ‪-‬ونام روزبازدهم‬
                                   ‫داشته باشد ‪1‬‬         ‫ازهرماه شمسی باشد ‪ - ۱‬ونامی است از نامهای‬

 ‫خوران = باثانی مجهول بوزن نوران»‬                       ‫آفتاب ‪ - ۷‬وسعنی مزه ولذت و خوردنی اندك‬
  ‫نام یکی از ءبارزان کیخسروین سیاوش بوده ‪.‬‬              ‫باشد که آنرا قوت لابموت گونند ؟ ‏ وخوردن‬
                                                        ‫‪ -‬و اهراز چیزی خوردن هم هت یعنی چیزی‬
                                                        ‫بخور؟ ‪ -‬ونوعی ازچلیاسه را نز گفته‌اند راخ‬
 ‫باشد ؛ وبا ثانی ممدوله بروزن‬    ‫ناج ومغفررخروی‬
                           ‫قرابه نازمده است ‪.‬‬             ‫وتر‬
                                                            ‫ه اس‬
                                                               ‫ششگی‬
                                                                  ‫ممکو‬
                                                                     ‫بسربالی بحارخوانند؟ ‪ -‬ونا‬
                                                                                             ‫بخورنق © ‪.‬‬
 ‫حورای سه با انی ممدوله بر ون‬                           ‫خور! ‪ -‬باانی »مدوله بروزن سرا ‪.‬‬
                                                        ‫بمعنی درخور وسزاوار و لابق باشد ‪-‬و خوردلی‬
                                        ‫باشد ‪٩‬‏ ‪.‬‬
                                                        ‫الدكك را نیز کویند که بعربی قوت لایموت‬
 ‫= باانیمدوله وخای‬        ‫خحوجریون‬                                                           ‫خوانند ‪. ۷‬‬
 ‫نقطه دار (‪ )۱‬وجیم و واو بر وزن بگرزیدن »‬               ‫خو رال‪ - 4‬باواومعدوله بروزن قرابه‪.‬‬
 ‫بافت سریالی نام دبوی است از جملة شیاطین ‪-‬‬               ‫برناد که از بندی که در یشاب‬     ‫ومی‬
                                                                                           ‫گک‬‫ب‬
‫‪ ۰‬وآن سنگینیی باشد که‬       ‫نس‬     ‫وکابویس را ن‬          ‫بسیار باشد تراوش کند ‪ -‬و آبی را نگیوزیند‬
                          ‫درخواب برمردم افتد ‪.‬‬          ‫که ازبرای خوردن باشد‪ -‬وبسی گفته‌اند بمعنی‬

                                                                            ‫(‪ )۱‬چك ‪ :‬خا ‪.‬‬

           ‫خور از چرخ فلك باده خور ‪.‬‬        ‫نات‬          ‫‪ - ۱‬روز خورست ای‌بدو رخ همجو خور‬
  ‫صفحة قمل‪.‬‬    ‫ورك‪۳ :‬‬      ‫مسعود سمدلاهوری‪ ۶ .‬روز شماری‪ »۳۳‬ورك‪ :‬هزدسسنا ‪33‬‬

   ‫‪ ۳‬سر که‪:‬خوردن‪.‬‬        ‫بهلوی ‪ ( ۲4۷۸‬خوردن ) «مسینا ‪۲٩ :۹۳۱‬‏ ‪ ۶‬اونوالا ‪. * ۳۲‬‬               ‫‪۴‬‬
                     ‫‪.‬‬   ‫است ‪ .‬رك ‪ :‬آفتاب پرست‬      ‫خوریرست‬     ‫› مضفف‬     ‫باین هعنی ظ‬   ‫‪-‬‬   ‫‪۴‬‬

          ‫رك ‪ :‬خور » خورای ‪.‬‬        ‫‪۱‬‬          ‫‪ ۶‬خورنگه » و خورنق» («‪.‬م‪).‬‬         ‫مخفف‬
                                                                                     ‫‪_ ۵‬‬



                           ‫خوارخوارآب همی پالاید ‏ آن خورآ بهباشد ‪ ,‬عنصری (بلخی) گفت ‪:‬‬
        ‫که (چو) بسیار گردد بيك باراوی‪».‬‬              ‫ز جوی خورابه تکومتر بگوی‬
   ‫‪.‬‬   ‫دفت فرس ‪ ۱۳‬ورك ‪۲۰۵:‬‬
                         ‫ل‬
                             ‫رکه‪ :‬خوره خورا‪۰ ‎‬‬      ‫‪٩‬‬           ‫رك ‪ :‬خروه » خود خروه ‪.‬‬           ‫‪۸‬‬


                                                                          ‫حزهٌ ‪۹۸۷‬‬    ‫فا‬‫صبه‬
                                                                                          ‫بق‬
   ‫بمناسبت نام فرشتةُ مزبور روز بازدهم هرماه ‪(.‬خورشید) با (خور) با ( خیر ) روز نامیده میشود‪.‬‬
                                                                          ‫سرونی‌درفهرست‬
  ‫روزهای ایرانی ایشروز را (خور) ودرسفدی(خویر) و درخوارزمی (اخیر)یاد کرده‪.‬‬
        ‫زرشتیان ابران ابن روز را (خیر) نامند‪ .‬در بیت ذبل بمعنی آفتاب وفرشته هردو آمده ‪:‬‬
       ‫بسان‌خور که‌نگهبان فرص‌خور باشد‪.‬‬           ‫تو یاسبان سلیل پربوشت میباش‬
    ‫خروانی «روز شماری ‪.۰,۹۷-۳۳‬‬

=== BQT_v2 leaf 247 ===
                                                                                               ‫خورد‬

 ‫خورده زه با انی معدوله بر وزن‬                          ‫ت بائانی ممدوله " ماضی‌خوردن‬      ‫جورد‬
             ‫کنده پر‪ .‬مطبخی وطباخ راگوبند ‪.‬‬         ‫‪-‬‬   ‫باشد ‪ - ۱‬و بمعنی شکست‬         ‫ن‬ ‫دکل‬‫ه|‬‫ر‬‫کک‬ ‫است‬
 ‫خوردی؟ ‪ -‬با انی معدوله بر وزن‬                          ‫و ریزه ریزه کرد هم در مبودّالصلا نوشته‌اند ‪-‬‬
                                                         ‫ویمعتی درخور ولایق وسزاوار نیزآهده است ‪.‬‬
         ‫مردی » مکاولات واطعمه رگاونند ‪۸. ۵‬‬
 ‫ر‌سواد ان «کنایه سازحر‬
                      ‫خشوید‬                             ‫خور دستان دبا انی معدوله و دال‬
 ‫خیزان و شب‌بداران وعیسی رنبگان باشد ‪٩‬‏ ‪-‬‬               ‫وسین بی‌قطه بروزن انگشتان » شاخ تازه ای را‬
                ‫کآه‬
                  ‫نو‬‫اگان‬  ‫وعقربان‌پادشاه ‪ -‬وف‬
                       ‫نرشت‬                             ‫گویندکه اتزاك انگور سرزند و آفرا ببب‬
 ‫بوقت گرما‬
                                      ‫سوار شوند ‪.‬‬        ‫ترش مز کی خورند‪ -.‬و شاخهای تاز درختان‬
                                                         ‫دیگر و نهال ګل و رباحن را لیز گفته‌اند ‪#. ۳‬‬
‫خو رمك ت باثانیممدوله و میمبر‬
‫وزن مردك » »هره ای باشد که بجهت دفم چشم‬                 ‫خور دوستان‪ -‬بانالی مسوله بروزن‬
 ‫زغم بر گردن اطفالآویزند ؛ وباین معنی بثالك‬             ‫متصورخان > ببهمعنی‌خوردمتان است که شاج تارءٌ‬
 ‫مشدد هم هت ؛ وبا ثالث لقطه دار لیز کنته‌اند‪.‬‬                                    ‫تاك انکور وغره باعد؟‬

                            ‫ذا ‪:‬‬
                               ‫غ‪-‬‬‫‪۱‬هلوی ‪( 172۷5‬خوردن) « مسینا ‪ «۹۳۱:۲۰‬اونوالا ‪» ۳۲‬‬
                                                                                ‫پ‬
              ‫سیر ‪.‬‬      ‫ونم‬
                           ‫شم‬‫آبثان خایند و‬                        ‫خوردی که خورد گوزن با شیر‬
       ‫نظامی گنجوی‪ «.‬کنجینه ‪.*6۵‬‬
                 ‫‪۰‬‬    ‫‪ = ۳‬رك‪ :‬خوردستان ‪.‬خودستان‬             ‫‪۰‬‬    ‫‪ _ ۳‬رك‪ :‬خودستان»خوردوستان‬

       ‫‪ - ۴‬پهلوی ‪. « 61۲2۷6‬سینا‪kîtrux » ۹۳۱:۲‬‏ «ناوادبا ‪ ۷۹۱۰‬ارمتیع ‪611۲0‬‬
                          ‫«اسشق ‪ »۷۰۵‬زرکه ‪ :‬اسفا ‪ : ۱‬اص ‪۲۹۲٩۱‬‏ ‪۲ :‬ص ‪ ۰۹۱‬هوبشمان ‪. ۷۰۰‬‬
              ‫و آنگاه مه یمهبود این هردو ‪۰‬‬                      ‫بان سياه وخوردی بی‌چربو‬    ‫‪6‬‬
       ‫‪.‬الممجم ‪AY‬‏‬       ‫کایی مروری‬

                 ‫‪ - 1‬بدان مناسبت کهکوبند عیسی درآسمان چهارم فرین خورشید است ‪:‬‬
              ‫سابة خورشید سواران طلب ‪.‬‬              ‫رنج خود و راحت باران طلب‬
   ‫‪۰‬‬    ‫نظامی کنجوی‪ .‬دگنجینههه»‬

       ‫‪ #‬خورد ی ‪ -‬بروزن بردن» اوسنا ‪( 1872۷ .18۷۳3-‬اکل ) » بپلوی ‪02172۷‬‬
       ‫ارمنی ع ‪kitrox‬‏ (‪۱‬کل‌طعام)‪ .‬کردی‪ (0۳1۲۷۲, 0۳1۳1۱۳‬کل)‪.‬افتانی ‪. 12۲05‬استی ‪۲1۷8۷5‬‬
   ‫‪.‬سرربکلی ‪ 0718-۲05‬سگلیسی ‪« 777 012‬اسشق ‪۷۰6»9‬اسفا‪:۱‬‬                      ‫‪2‬ی‪11‬‬
                                                                              ‫‪-‬منج‬
                                                                                 ‫‪۲‬ی و‬
                                                                                    ‫‪ 0‬مشغن‬
   ‫رگ‪-‬ے‪۰۷۳۱‬‏ «بونکر ه‪٩ ۷‬‏ < که ‪.‬‬
                               ‫‪۸۳‬‬‫‪٣‬ص‏ ‪ ۰۵۰۳ ۰۰۹۲ ۱۵‬روکه‪ :‬فهرست» «مسینا ‪ ۹۳۱‬ن‪٩‬یب‬
       ‫است ‪ ۰۱‬؛زاگلو فرودادن وبلعیدن نذا »ک‪۱‬ل‪ :‬فروباه پیشتر رفت وماهی خوردن گرفت ‪« »۰‬سند‬
                                            ‫بادنامه‪ .‬ظهیری‪ - »۸4‬آشامیدن ‪ -‬تلف کردن» برباد دادن‪.‬‬
  ‫‪ #‬حورشید ‏ بضم اول وواو ممدوله از خ‪:‬ور (آقتاب )(هم‪ + ).‬شید ( هم‪ ) ۰‬اوستا‬
  ‫هکر ‪ :‬زور‬
          ‫‏‪ «hvara xshaeta‬یولهپ ‪ ۷2751264‬ةغل( باتفآینعمب )ناشخرد هکر ‪ :‬روخ و‬
                                                                                  ‫شماری ص ‪: ۹۲-۳۳‬‬
                     ‫بوتس اندر دهان ماهی شد‬                 ‫قخروصرشید درسیاعی شد‬
       ‫«کلتان‪.»۲۲‬‬
```


## [2026-09-14T03:12:51.948Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== MON files ===\"; wc -c MON_part1.txt MON_part2.txt; echo \"=== grep 1455 pages ===\"; grep -n \"pdf page\" MON_part1.txt | head -3; echo \"=== search خوردن in MON ===\"; grep -c \"خوردن\" MON_part1.txt MON_part2.txt"
}
```


### [2026-09-14T03:12:52.120Z] TOOL RESULT

```
=== MON files ===
4377831 MON_part1.txt
4331421 MON_part2.txt
8709252 total
=== grep 1455 pages ===
=== search خوردن in MON ===
MON_part2.txt:158
MON_part1.txt:214
```


## [2026-09-14T03:12:54.270Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== KLN swallow ===\"; grep -n -o \"swallow, v\\..\\{0,400\\}\" KLN_1966.txt | head -5; echo \"=== KLN swan ===\"; grep -n -o \"swan, n\\..\\{0,400\\}\" KLN_1966.txt | head -5; echo \"=== KLN sound ===\"; grep -n -o \"sound, n\\.[^|]\\{0,350\\}\" KLN_1966.txt | head -6; echo \"=== KLN sonic ===\"; grep -n -o \"sonic, adj\\..\\{0,250\\}\" KLN_1966.txt | head -3"
}
```


### [2026-09-14T03:12:55.470Z] TOOL RESULT

```
=== KLN swallow ===
=== KLN swan ===
=== KLN sound ===
=== KLN sonic ===
```


## [2026-09-14T03:13:00.595Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== KLN swallow ===\"; grep -n -i \"swallow\" KLN_1966.txt | head -8; echo \"=== KLN swan ===\"; grep -n -i \"OE. swan, 'swan'\\|swan, n\" KLN_1966.txt | head -8"
}
```


### [2026-09-14T03:13:00.685Z] TOOL RESULT

```
=== KLN swallow ===
1246:■**<*lve,  tr.  v.  —  L.  absolvere,  ‘to  set  free’,  fr. •h-  and  solvere,  ‘to  loosen,  set  free'.  See  solve and  cp.  assoil.  Cp.  also  dissolve,  resolve. ^*orb,  tr.  v.  —  L.  absorbere,  ‘to  swallow  up’, fr.  ab-  and  sorbere,  ‘to  suck  in,  swallow  up’, which  is  cogn.  with  Arm.  arbi  (from.  *srbh-), ‘I  drank,  Gk.  poipeiv  (for  *apo<peLv),  ‘to  sup UP’>  Alb.  gerp  (for  *serbhd-),  ‘I  sip’,  OSlav. *rubati,  Lith.  surbiu,  surbti,  sribiu,  srebti,  ‘to •  Mir.  srub,  ‘snout’.  Cp.  absorption,  resorb, •*•*1  v.,  and  the  second  element  in  Sangui- ■orba.
1818:Derivatives:  aeronaut-ic,  aeronaut-ic-al,  adjs., aeronaut-ic-al-ly,  adv.,  aeronaut-ics,  n. aerophagia,  aerophagy,  n.,  air  swallowing  (med.)
5706:bronchia,  n.  pi.,  the  bronchial  tubes  (anat.)  — Late  L.  bronchia,  gen.  -drum,  fr.  Gk.  Ppoyyia, fr.  PpoYX°S>  ‘windpipe’.  See  bronchus, bronchiole,  n.,  a  minute  bronchial  tube  (anat.)  — Medical  L.  bronchiola,  a  diminutive  coined  by E.  Schultz  fr.  L.  bronchia  (pi.),  ‘the  bronchial tubes’;  see  bronchia.  Cp.  Joseph  Hyrtl,  Ono- matologia  anatomica,  p.  557- Derivative:  bronchiol-ar,  adj. bronchiolitis,  n.,  inflammation  of  the  bronchioles (med.)  —  Medical  L.  formed  fr.  bronchiola  with suff.  -itis.  See  prec.  word, bronchitis,  n. ,  inflammation  of  the  bronchial  tubes (med.)  — -  Medical  L.,  coined  by  Charles  Bed- ham  in  1808  fr.  bronchus  and  suff.  -itis;  intro¬ duced  into  medicine  by  P.  Frank  in  his  Inter- pretationes  Clinicae  in  1812. broncho-,  before  a  vowel  bronch-,  combining  form denoting  relation  to  the  bronchi.  —  Gk.  |3poyxo-, Pp °YX.->  fr-  Pp°TX°?>  ‘windpipe’.  See  next  word, bronchus,  n.,  each  of  the  two  forked  branches  of the  windpipe.  —  Medical  L.,  fr.  Gk.  ppoyxo?, ‘windpipe’,  which  is  prob.  rel.  to  (ipoyhoc, ‘throat’,  (aor.),  ‘he  swallowed  up’,
6478:fr.  L.  captivus,  ‘caught,  taken  prisoner’,  fr.  cap¬ tus,  pp.  of  capere,  ‘to  catch,  seize,  take  hold  of, take,  receive,  hold,  contain’,  whence  L.  capsa, ‘repository,  box,  chest,  case’,  capulus,  ‘sarco¬ phagus,  bier’ ;  fr.  I.-E.  base  *qap-,  ‘to  seize,  hold, contain’,  whence  also  Gk.  yAnzeiv,  ‘to  swallow greedily,  gulp  down’,  xam;,  ‘manger’,  xcotty), ‘handle,  handle  of  an  oar,  haft’.  Alb.  kap,  ‘I take,  seize’,  kam,  ‘I  have’,  Lett.  kamp(j)u,  kdmpt, ‘to  seize*,  Goth,  hafjan,  OE.  hebban,  ‘to  raise, lift’,  Goth,  haban,  OE.  habhan,  ‘to  have’, and  prob.  also  OI.  kapati,  ‘two  handfuls’. See  heave  and  have  and  cp.  words  there  referred to.  Cp.  also  accept,  anticipate,  apperccive,  apper¬ ception,  aucupate,  cabas,  cabbage,  ‘to  pilfer’, cable,  cachalot,  caisson,  caitiff  (which  is  a  dou¬ blet  of  captive),  caja,  cajeta,  cajole,  capable,  ca¬ pacious,  capacity,  capias,  capistrate,  capsa,  Cap¬ sella,  Capsicum,  capstan,  capsule,  captation, caption,  captious,  captor,  capture,  Carpocapsa, case,  ‘box,  chest’,  casement,  cash,  catch,  chara¬ banc,  chase,  conceive,  concept,  conception,  cop, ‘to  catch',  Copepoda,  deceipt,  deceive,  deception, disciple,  discipline,  emancipate,  except,  excipient, forceps,  imperceptible,  incept,  inception,  inter¬ cept,  intussusception,  mancipate,  mercaptant, municipal,  nuncupative,  occupy,  participate,  per¬ ceive,  percept,  perception,  precept,  preceptor, prince,  principal,  principle,  purchase,  recado,  re¬ ceipt,  receive,  recept,  receptacle,  reception,  re¬ ceptive,  recet,  recipe,  recover,  recuperate,  sus¬ ceptible,  usucapion.
6536:Carduus,  n.,  a  genus  of  prickly  herbs  ( bot .)  — L.  carduus ,  ‘thistle’.  See  prec.  word, care,  n.  —  ME.  care,  fr.  OE.  caru,  cearu,  ‘anxiety, sorrow,  care’,  rel.  to  OS.  kara,  ‘sorrow’,  OHG. chara,  ‘lament’,  Goth,  kara,  ‘sorrow’,  OS.  (mod) karag,  ‘anxious,  sad,  sorrowful’,  OE.  cearig, MDu.  carich,  ‘sad,  sorrowful’,  Du.  karig, ‘scanty,  frugal’,  OHG.  karag,  ‘anxious’,  MHG. karc,  karg,  ‘shrewd,  clever’,  G.  karg,  ‘stingy, scanty’;  fr.  Teut.  *karo ,  ‘sorrow,  care’.  These words  are  cogn.  with  Gk.  yr,pu?,  Dor.  yapu ;, ‘voice,  sound’.  Arm.  cicarn,  ‘swallow’,  cicarnuk, ‘nightingale’,  Ossetic  zar,  ‘song’,  zarun,  ‘to  sing’, L.  garrire,  ‘to  chat,  talk,  chatter',  W.  garm, OIr.  gair,  gairm,  W.  gawr,  ‘noise,  cry’,  Toch. karye,  ‘care’.  All  these  words  derive  front  the I.-E.  imitative  base  *gdr-,  ‘to  shout,  cry’.  The sense  development  of  Toch.  karye,  ‘care’,  E.  care and  the  related  Teut.  words  may  be  illustrated by  the  following  stages:  cry — lamentation — grief.  Cp.  chary,  cur,  garrulous,  Gerygone.  Cp. also  German.
6605:Carpocapsa,  n.,  a  genus  of  moths  ( entomol .)  — ModL.,  compounded  of  carpo-,  fruit’,  and xxiJik;,  ‘a  gulping,  devouring’,  from  the  stem  of xdbnreiv,  ‘to  swallow  greedily,  gulp’,  which  is cogn.  with  L.  capere  ‘to  catch,  seize,  hold’.  See captive.
6907:Celaeno,  n.,  one  of  the  Harpies  (Greek  mythol.)  — L.,  fr.  Gk.  KeXcclvco,  lit.  ‘the  Black  one’,  fr. xeXcuvo;,  ‘black’,  fr.  I.-E.  base  *qel-,  *qol-, ‘black,  spotted’,  which  is  rel.  to  base  *qdl-,  of s.m.,  whence  L.  caligo,  ‘darkness’.  See  caliginous. celandine,  n.,  the  swallowwort.  —  ME.  celydoine, fr.  OF.  celidoine  (F.  chelidoine),  fr.  L.  chelido- nium,  fr.  Gk.  yeXlSrlvLov,  fr.  yeXlStuv,  gen. X.eXi86vo;,  ‘the  swallow’,  which  is  rel.  to  xi/}:r,, ‘the  thrush’,  and  cogn.  with  OE.  gellan,  ‘to  yell, shriek’,  galan,  ‘to  sing'.  See  yell  and  nightingale and  cp.  chelidonium.
9118:Derivatives:  cope,  tr.  v.,  to  dress  in,  or  furnish with,  a  cope,  coping  (q.v.) cope,  intr.  v.,  to  struggle,  deal  with.  —  ME.  cou¬ pon,  fr.  OF.  colper,  couper,  ‘to  strike’  (whence also  F.  couper,  ‘to  cut’),  fr.  colp,  coup  (F.  coup), ‘stroke,  blow’.  See  coup  and  cp.  words  there referred  to.  Derivative:  cop-ing,  n. cope,  tr.  and  intr.  v.,  formerly  to  buy;  now,  to barter  (dial.  Eng.)  —  ME.  copen,  fr.  MDu.  copen (Du.  kopen),  ‘to  buy’,  which  is  related  to  OE. ceapian,  of  s.m.  See  cheap,  v. copeck,  n.  —  A  var.  spelling  of  kopeck, copepod,  n.,  a  minute  crustacean  pertaining  to the  order  Copepoda.  —  See  next  word. Copepoda,  n.  pi.,  an  order  of  minute  crustaceans ( zool .)  —  ModL.,  compounded  of  Gk.  xura;, ‘handle  of  an  oar,  oar’,  and  tcoui ;,  gen.  rroSoc, ‘foot’.  Gk.  xcoro;  is  rel.  to  xcbrrEtv,  ‘to  swallow greedily’,  and  cogn.  with  L.  capere,  ‘to  catch, seize,  hold’.  See  captive.  For  the  second  element see  -poda.
=== KLN swan ===
```


## [2026-09-14T03:13:02.188Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== MON آخور ===\"; grep -n -o \".\\{0,120\\}آخور.\\{0,200\\}\" MON_part1.txt | head -8; echo \"=== MON خورنق ===\"; grep -n -o \".\\{0,150\\}خورنق.\\{0,250\\}\" MON_part1.txt MON_part2.txt | head -8"
}
```


### [2026-09-14T03:13:09.605Z] TOOL RESULT

```
=== MON آخور ===
ugrep: error: error at position 86
-\xbf][\x80-\xbf]*){0,200}
                          \___exceeds complexity limits


=== MON خورنق ===
ugrep: error: error at position 88
80-\xbf][\x80-\xbf]*){0,250}
                            \___exceeds complexity limits
```


## [2026-09-14T03:13:14.971Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== KLN swelgan ===\"; grep -n -i \"swelgan\\|svelgja\" KLN_1966.txt | head -5; echo \"=== KLN swan OE ===\"; grep -n -i \"svanr\\|swon-\\|swen-\" KLN_1966.txt | head -8"
}
```


### [2026-09-14T03:13:15.045Z] TOOL RESULT

```
=== KLN swelgan ===
16764:ME.  groundeswele,  fr.  OE.  grundeswelge ,  fr. earlier  gundeswelge,  lit.  ‘pus  swallower  ,  ft.gund, ‘pus’,  and  swelgan,  'to  swallow’ ;  so  called  in allusion  to  its  use  in  making  poultices.  OE.  gund is  rel.  to  OHG.  gunt,  ‘pus’,  Goth,  gund,  ‘can¬ cer’,  dial.  Norw.  gund,  ‘scurf,  scab  ,  and  pos¬ sibly  cogn.  with  Gk.  xavthjXv]  (dissimilated  fr. *yavfHjX?j),  ‘swelling,  tumor’.  For  OE.  swelgan see  swallow,  v.
37661:swallet,  n.,  underground  stream  (provinc.)  — Prob.  derived  fr.  the  stem  of  the  verb  swallow, swallow,  tr.  and  intr.  v.  —  ME.  swelowen,  swale- wen,  fr.  OE.  swelgan,  rel.  to  OS .farswelgan,  ON. svelgja,  Swed.  svalja,  ‘to  swallow',  MDu.  swel- ghen,  Du.  zwelgen,  ‘to  gulp,  swallow’,  OHG. swelahan,  swelgan,  ‘to  swallow’,  MHG.  swelhen, swelgen,  ‘to  swallow’,  G.  schwelgen,  ‘to  revel’. Cp.  swill  and  the  second  element  in  groundsel, ‘name  of  a  plant’.
37662:Derivatives:  swallow-able,  adj.,  swallow-er,  n, swallow,  n.,  the  act  of  swallowing;  gullet.  —  ME. swelowe,  swalowe,  fr.  OE.  geswelg,  ‘gulf,  abyss', fr.  swelgan,  ‘to  swallow’.  Cp.  MHG.  swalch, ‘abyss',  ON.  svelgr,  ‘swallower;  whirlpool’,  and see  swallow,  v.
=== KLN swan OE ===
35905:Derivative:  somnolent-ly,  adv. son,  n.  —  ME.  sune,  sone,  fr.  OE.  sunu,  rel.  to OS.,  OFris.  sunu,  ON.  sour,  Dan.  sen,  Swed.  son, MDu.  sone,  Du.  zoon,  OHG.  sum,  sun,  MHG. sun,  G.  Sohn,  Goth,  sunus,  ‘son’,  and  cogn.  with OI.  suniih,  Avestic  hunush,  OSlav.  synu,  Lith. sunus,  ‘son’,  and — without  n-formativc  ele¬ ment — with  Toch.  B  soya,  A  se,  Gk.  ui6?,  ‘son’, Arm.  ustr,  ‘son’  (influenced  in  form  by  dustr, ‘daughter’),  OI.  sulah,  ‘son’,  sute,  siyate,  savati, ‘begets,  procreates’,  OIr.  suth  (for  su-tu),  ‘fetus’. All  these  words  derive  fr.  I.-E.  base  *seu-,  *su-, ‘to  bear,  bring  forth ;  birth’, sonance,  sonancy,  n.  —  Formed  from  next  word with  suff.  -ce,  resp.  -cy.  Cp.  assonance,  conso¬ nance,  dissonance,  resonance, sonant,  adj.  and  n.  —  L.  sonans,  gen.  -antis,  pres, part,  of  sonare,  ‘to  sound’,  which  stands  for *swenare  and  is  rel.  to  sonus  (for  *swonos), ‘sound’,  fr.  base  *swen-,  ‘to  sound'.  See  sound, ‘noise’,  and  cp.  assonant,  consonant,  dissonant, resonant,  resound,  sonata,  sonnet,  sound,  ‘noise’, and  the  second  element  in  unison.  For  the  ending see  suff.  -ant.
36005:sound,  n.,  noise.  —  ME.  soun,  fr.  OF.  ( =  F.)  son, fr.  L.  sonus,  ‘sound’,  which  stands  for  *swonos, and  is  rel.  to  sonare  (for  *swendre),  ‘to  sound’, fr.  I.-E.  base  *swen-,  ‘to  sound’,  whence  also OI.  svanati,  ‘it  sounds’,  svdnas-,  ‘noise’,  svanah, ‘sound,  tone’,  svanah,  ‘rustling’,  OIr.  senim,  ‘the playing  of  an  instrument’,  OE.  geswin,  ‘music, song’,  swinsian,  ‘to  sing’,  ON.  svanr,  OE.  swan, ‘swan",  prop,  ‘the  singing  bird’.  See  sonant  and cp.  swan.  The  d  in  sound  is  excrescent.  Cp. bound,  ‘ready’,  and  words  there  referred  to.
37455:sun,  n.  —  ME.  sonne,  fr.  OE.  sunne,  rel.  to  ON., OS.,  OHG.  sunna,  MDu.  sonne,  Du.  zon,  MHG., G.  sonne,  ‘sun’,  Goth,  sunno.  These  words  are -en-enlargements  of  l.-E.  base  *sdu-,  * su -,  ‘to shine;  sun’,  and  cogn.  with  Avestic  xveng  (for *swen-s),  ‘of  the  sun’,  xvanvant,  ‘sunny’.  For-/- enlargements  of  base  *sau-,  *su-  see  Sol.  Cp. south.
37670:swan,  n.  —  ME.,  fr.  OE.  swan,  rel.  to  OS.  swan, ON.  svanr,  Dan.  svane,  Swed.  svan,  MDu. swane,  Du.  zwaan,  OHG.,  MHG.  swan,  G. Schwan.  Swan,  prop,  means  ‘the  singing  bird’. The  name  derives  from  a  gradational  var.  of I.-E.  base  *swen-,  *swon-,  ‘to  sound’,  whence sonare  (for  *swondre),  ‘to  sound'.  See  sonant and  cp.  words  there  referred  to.
```


## [2026-09-14T03:13:17.510Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re,io\nfor fn in ['MON_part1.txt','MON_part2.txt']:\n    t=open(fn,encoding='utf-8',errors='replace').read()\n    for w in ['آخور','خورنق','خورنگاه','خنیدن','آخوند']:\n        idxs=[m.start() for m in re.finditer(w,t)][:3]\n        for i in idxs:\n            print(fn,w,'>>',t[max(0,i-120):i+220].replace('\\n',' '))\n        print('---',fn,w,'count',len(re.findall(w,t)))\nEOF"
}
```


### [2026-09-14T03:13:18.661Z] TOOL RESULT

```
MON_part1.txt آخور >> پیوسته» متصل. نواخته» سامان  کرده» کوک کردن (الت مو سیقی).  اخته‌چی: آ-.2 [تر.] (ص‌مر.) داروغه  اصطبل,» ناظر طویله. میر آخور.  اخد: : 6 [ع.] (افا) گیر نده؛ ج ج. آخذین.  آخسر: تة (ع.] (ص.) در دگس  دیگری» یکی از دو چیز یا دو کس» غیر؛ ج.  آخرین.  اخر: 2 [ع.] (ص.) پسین» وایسین,» بابان؛  انجام فرجام؛ مق. اولی اغاز.  اخر: ۲ (ا.) جایگاهی از گل و
MON_part1.txt آخور >> اید.   اشت: (ع.] (ا.) خواهر» همشیره. مانند»  مثل» فرین؛ ج. اخوات.   اختاجی: آ-2021 [- اختاچی - اخته‌چی»  تر.] (امر.) میرآخور» طو بله‌دار» مهتر»  ستوربان.   اختبار: تفت [ع.] (مسص ع.) آزمودن»  امتحان کردن. (مصل.) آگاهی یافتن از  چیزی يا خبری» خبردار شدن؛ ج. اختبارات.    ۲ ۰ ۱ فر هکت فارسی وه 7 اختتام    اختتام. صقاهاه [ع ۳ (مسص م ۰ به پابان
MON_part1.txt آخور >>  بی‌خایهةٌ فاقد  موی چهر ۰۰  اخته‌بیگ: (و/9۵):(ه۰-۱ (تر.] (امر.) کسی  که اخته کردن حوانات به دستور او است.  اخته‌چی. میرآخور» رئیس طویله و اصطبل.  اختبار: 0/2۲ [ع.] (سصم.) گزبدن؛  برگزیدن» گزین کردن» انتخاب کردن.  (ص.) مسختار» برگزبده» (امص.) آزادی  عمل» قدرت سر انجام دادن کار به ارادة  خویش؛ مقّ. اجبار» اضطرار. غلبه» قدرت»  تصرف. (فل.) ح
--- MON_part1.txt آخور count 9
MON_part1.txt خورنق >> زید آنکه از غم و  ضصه به دور است. (فع. امر.) تهنت»  تبریکث.   خوشباور: ۲.-: (رص مر .) آنکه زود و    فرهنگ فارسی معین    خورنق  به سادگی هر چیز را باور کند؛ زود باوری.  خو شخت: 7-۱ (ص‌مر.) نبککابخت؛  خوش اقبال» سعادتمند» سعید؛ مق. بدیخت.  خوش بر خورد: ۲.0 (ص‌مر .)  کسی که با روی کشاده مردم را ملاقات کند»  خوش معاشرت؛ مق. بد برخورد.  خوش‌بر
--- MON_part1.txt خورنق count 1
--- MON_part1.txt خورنگاه count 0
MON_part1.txt خنیدن >>   خئا: 3 (.) سر وده نغمه» آواز.  ها ات ۷-۲ [- خنبا] (ص‌فا.)  آوازخوان» خواننده؛ سرودگوی. خنيا گر  فلک: ( کذ.) ز هر ه.   خنیدن: 227-1190 (مص‌ل.) بیجیدن آواز  (در کوه؛ حمام» گنبد و غبره). آوازه بیدا  کردن مشهور شدن.   نید ۵: (2:۸-12)۵ (امف.) مسعروف»  شهرت افته.   حنید ه۵: (0-)2]-2:7 (امف.) سروده خوانده  شده. دانای در کار سرود؛ مصنف»  موسیقی
--- MON_part1.txt خنیدن count 1
MON_part1.txt آخوند >>  با مخف. آقا + خوند  خداوند؟ با خوند - خواندن!] (ص. )  ماه عالم باسواد. عالم روحانی» بیشوای  مذهبی. . معلم مکتب خانه.   آخوندبازی: 0321 - ۰ (حامص.) توسل به  حیله‌های شرعی.   اخسوندک: 2000-21 (ا.سصف.) آخوند  کوچک. (جان.) حشره‌ای از راستة راست    بالان که همشکلی کامل با محبط خود دارد و    اکثر در لای شاخ و برگ‌های سبز درختان»  خود را به شکل
MON_part1.txt آخوند >> انی» بیشوای  مذهبی. . معلم مکتب خانه.   آخوندبازی: 0321 - ۰ (حامص.) توسل به  حیله‌های شرعی.   اخسوندک: 2000-21 (ا.سصف.) آخوند  کوچک. (جان.) حشره‌ای از راستة راست    بالان که همشکلی کامل با محبط خود دارد و    اکثر در لای شاخ و برگ‌های سبز درختان»  خود را به شکل شاخه‌های کوچک قرار  می دهد » شبخکد.   آداب: 210 [ع. ۰ (.) 3 . ادب» رسسوم»  عادا
--- MON_part1.txt آخوند count 2
MON_part2.txt آخور >> نگان کرده مانند  خرما» انگور و جز 0 قطره.  زبان؟ ج ج. معالیق.   ۳۳ -16 ,]12 1112 [ع.] (۰) علف‌دان ستور  از چوب و جز آن» آخور. علف.   معلق: رخا 220 [غ.] (امف.) آو بخته ۲  سته شده» مربوط. (ص.) آویزان. بحر  معلق: (کد.) آسمان. سبز طشت معلق: ( کد.)  آسمان. سقف معلق: (کد.) آسمان. معلق  حصار (محکم): (کد.) آسمان. (.) (خط.)  یکی از اشکال خطوط اسلا
MON_part2.txt آخور >> : کسی که مخارج بیوتات  دولتی را متعهد بود. (صفویه) (فلسفی.  شاه‌عباس ۴۱۳:۲). ناظر دواب: بازرس  چار پایان بارکش شاه؛ میر آخورباشی صحرا.  (صنوبه). ناظر رسومات: داروغه‌ای که  خراج مکان‌ها و راه‌ها به عهدة او محول  نو د8.    ناظم: 132700 [ع.] (افا.) ترست دهنده) نطم  دهند ه. آراینده؛ آرايش کننده. کسی که  مروارید و گوهرها را به رشته کشد. گویندة
--- MON_part2.txt آخور count 2
--- MON_part2.txt خورنق count 0
--- MON_part2.txt خورنگاه count 0
--- MON_part2.txt خنیدن count 0
MON_part2.txt آخوند >> ر: 101.0 [ع. ف. - ملاخورده)  (ص‌مف..) آنچه از خوردنی که به ملایان  دهند. جبری که مورد سوء استفادة کسی بت  جمعی (مخضوضاً آخوندها) شو ده آنجه که  حیف و میل گردد. میوه و جز آن که به سبب  ضایم شدن و غیره بسیار ارزان فروخته شود.  ملاد: ۶۸ [ع.] (.) پناهگاه» جای بناه.  قلعه» دژ.   ملار: اند | ملازه < ملاج | .۲ (بر.)  زبان کوچک. (پز.) فضایی که بی
MON_part2.txt آخوند >>  (تکعده)معموقاهه [ع. ملامسه ]  (مسصم.) لمس کردن یکدیگر را؛ دست  مالبدن بهم.   مانقطی: آ-امرمصق] امه [ع. . ف.ا  (ص‌نسب.) آخوندی که در مورد ثبت  نقطه‌های حروف در کلمات اصرار تام دار د  ولی به معنی و مفهوم آنها اعتنایی ندارد.  کی کر تفای کرد او  مصر است.   ملاهی: ال (ع ۰] (.) 3 . ملهی؛ ات  لهو» اسات بازی.   ملایزغل: آعرمج۱0115-۷ [ع. مسلایزقل
--- MON_part2.txt آخوند count 2
```


## [2026-09-14T03:13:33.741Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nt=open('MON_part1.txt',encoding='utf-8',errors='replace').read()\nprint('FF count',t.count('\\f'))\nfor w in ['خورنق','خورش:','خوردن:','خواندن:','آخر: ۲']:\n    for m in list(re.finditer(w,t))[:2]:\n        i=m.start(); print('>>',w,'::',t[max(0,i-60):i+500].replace('\\n',' '),'\\n')\nEOF"
}
```


### [2026-09-14T03:13:34.919Z] TOOL RESULT

```
FF count 0
>> خورنق ::   خوشباور: ۲.-: (رص مر .) آنکه زود و    فرهنگ فارسی معین    خورنق  به سادگی هر چیز را باور کند؛ زود باوری.  خو شخت: 7-۱ (ص‌مر.) نبککابخت؛  خوش اقبال» سعادتمند» سعید؛ مق. بدیخت.  خوش بر خورد: ۲.0 (ص‌مر .)  کسی که با روی کشاده مردم را ملاقات کند»  خوش معاشرت؛ مق. بد برخورد.  خوش‌برش: 0۳۵5-.:(ص‌مر.) خباطی که  لباس را خوب می‌برد و نیک می‌دوزد؛  خوشدست. جامه‌ای که برش و دوخت آن  نیک باشد.   خوشیبو(ی): (000- (ص‌مر.) آنجه که  دارای بوی خوش باشد؛ معطر.  خوش‌بین: ۲-7 [- خوش‌بننده ] (ص فا.)  آنکه بنظر نیک در امور می‌نگرد) مسق .  بدبین. (فد.) آنکه جهان آفرینش را پر 

>> خورش: :: وردنی: آ-0۲۸7: (ص‌لب..) جیزی که  قابل خوردن باشد؛ خوراکی.   خورش: (قد. :2۰-۶300 [- خورشت]  (امص.) خوردن. (.) حوردنی» طعام» غدا.  آنچه با نان یا برنج خورند؛ قاتق.  خورشگر: 0۲۵-۲( (ص‌شغد.) آشیز»  خوالیگر؛ طباخ.   حو رشید: (قد. -.۲۵۲-۹]0002۲-560 [خور.  درخشنده] (امر.) (اخ.) آفتاب. هر ستارة  ابتی که مرکز یکی از منظومه‌های شمسی  باشد. نوعی اسب.   خورند: 0۲:٩‏ (امر.) فراخورء سنأسب»  در خور» شایسته.    ۳۴    حورئق: ۲2۷۵۲۵۷ [معر . خورنگه - خره]  (.) کاخ با شکوه» کوشکک با جلال. (اخ.)  خوره: (0۲-۵)0: (.) انجه که جیزی را  بخورد و از میان برد. (پز.) جذام.   خوره: (ق 

>> خوردن: :: داروسازی بکار می‌رود. ترکیبات فعلی و  جملات: آب از آب تکان نخوردن: (عم.)  حاد ثه‌ای رخ ندادن» ارام بودن اوضاع. اب  از آب نجنبیدن. آب از تارکك کسی بر تر  گذشتن: کار او به ام وش | متاااز سر   کلشتم: آب از جگر بخشیدن: عطا کر دن»  بخشیدن» چیز دادن. آب از جک و چانه...  سرازیر شدن: (عم.) تمایل شدید داشتن.  آب از سر تبره نودن: : گل آلود بودن آب از  سر‌جشمه. ناقص ودن امری از آغاز. آب از    ۳۲ فرهنگ فارسی معین آب    سرچشمه گل آلود بودن. آب از سر شدن  (کسی را): نزول آفات و بلیات بیشمار (بر  وی) ات از سشرشنعه کل( آلود) نودن:  عیب و نقص در اصل و بنیان امر بودن. آب   

>> خوردن: :: مل لغو و بیهوده  کردن (قس. آب به فربال پیمودن). آب  بی‌لجام خوردن: مطلق العنان بودن» سر خود  بودن. آب پاکی روی دست (کسی) ریختن:  (عم. ) کاملاً (او را) مأْیوس کردن. آب تویه  بر (به روی) سر ریختن: (عم.) توبه کردن.  آب توبه بر (به روی) سر (کسی) ریختن:  (عسم.) توبه دادن (وی را). آب در جگر  آهلن رسدن آب به جگر. . صح. - به عقمدة    به جوی باز آمدن. آب به دهان.    قدما معده محل غذا و جکر مرکز آب است.  [ دوس دامن میت بو ون اس  آب در جر نداشتن ۰ : مفلس بودن» سی چیز  بودن. آ در جوی اسان ادن فولت  رفته» با زگشتن اقبال از دست رفته. آب در  جوی داشتن: داشتن دولت و اقا 

>> خواندن: :: دن: بوسه دادن بر  دست وی. (مح.) احترام کردن وی. دست  کسی را خواندن: (قمار) ورق‌های او را  0 (مج.) اند شه او را دریافتن. دست  گرفتن برای کسی: (عم.) خطای کسی را  مستمسکک قرار دادن و گاه و بیگاه به رخ او  کشیدن. دست مریزاد: دعایی است که در  ی ۱  کو‌ند. دست نکٌاهداه شتن: تأمل کردن»  توقف کردن» اجرای امری را متوقف کردن.  دست و پا زدن: دست و پا را به کار انداختن  (در شنا). ( کد.) طلب کردن به جد و جهد  تمام. ( کد.) جان کندن. دست و پای خود را  گم کردن: (عم.) دست باچه شدن. دست و  وروی را در (تسوی) پوست گردو   شتن: (عم.) او را گرفتار مخمصه کردن.  وج ی  جنگ کر دن ب 

>> خواندن: ::  را در دهان کسی گذاشتن: به او باد  دادن گفتن آن را. یک دهان خواندن: (سد.)  یک بار قطه‌ای را به آواز خواندن. (کن.)    آلت مر ده بر ۵. مدخل.    دهان: مقططمك [ع.] (ص.) روغن فروش.  دهان‌بند: :4.02 (امر.) پارچه‌ای که برابر  دهان بندند. پوزبند. (کد.) پول با مالی که به  کسی دهند تا در امری سکوت کند.  دهان‌دره: (0-)1272-.1 (امسص.) کشودن  دهان به سبب غلبة خواب یا خماری و با  تسلی. خمیازه.   دهانه: (0-)-:0208 (امر.) آنچه که شبیه به  دهان باشد. لگام اسب لجام؛ افسار. مبله‌ای  آهنی متصل به افسار که در دهان اسب افتد.  زنگار معدنی که از معدن مس حاصل شود و  رنگ آن به سب
```


## [2026-09-14T03:13:49.023Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nt=open('MON_part1.txt',encoding='utf-8',errors='replace').read()\nfor pat in [r'خوردن: ?\\(?', r'آخر: ?۲', r'آخور:']:\n    for m in list(re.finditer(pat,t))[:4]:\n        i=m.start(); print('>>',pat,'::',t[max(0,i-200):i+450].replace('\\n',' '),'\\n')\nEOF"
}
```


### [2026-09-14T03:13:50.173Z] TOOL RESULT

```
>> خوردن: ?\(? ::  +۲۲۵1۲-001 +0  این محلول نیز خواص شیمیایی آب ژاول را  دارا است. آب مقطر: (شیم.) آبی که با قرع  و انییق جوشانده و تقطیر کرده باشند و آن  در داروسازی بکار می‌رود. ترکیبات فعلی و  جملات: آب از آب تکان نخوردن: (عم.)  حاد ثه‌ای رخ ندادن» ارام بودن اوضاع. اب  از آب نجنبیدن. آب از تارکك کسی بر تر  گذشتن: کار او به ام وش | متاااز سر   کلشتم: آب از جگر بخشیدن: عطا کر دن»  بخشیدن» چیز دادن. آب از جک و چانه...  سرازیر شدن: (عم.) تمایل شدید داشتن.  آب از سر تبره نودن: : گل آلود بودن آب از  سر‌جشمه. ناقص ودن امری از آغاز. آب از    ۳۲ فرهنگ فارسی معین آب    سرچشمه گل آلود بودن. آب از سر شدن  (کسی را): نزول آفات و بلیات بیشمار (بر  وی) ات از سشرشنعه کل( آل 

>> خوردن: ?\(? :: هشتن:  فریب دادن. حیله کردن. آب به فربال  پیمودن: آب به هاون کوبیدن. آب به کس  ندادن: نم بس ندادن» جبزی ندادن. آب به  هاون کوییدن (کوفتن): عمل لغو و بیهوده  کردن (قس. آب به فربال پیمودن). آب  بی‌لجام خوردن: مطلق العنان بودن» سر خود  بودن. آب پاکی روی دست (کسی) ریختن:  (عم. ) کاملاً (او را) مأْیوس کردن. آب تویه  بر (به روی) سر ریختن: (عم.) توبه کردن.  آب توبه بر (به روی) سر (کسی) ریختن:  (عسم.) توبه دادن (وی را). آب در جگر  آهلن رسدن آب به جگر. . صح. - به عقمدة    به جوی باز آمدن. آب به دهان.    قدما معده محل غذا و جکر مرکز آب است.  [ دوس دامن میت بو ون اس  آب در جر نداشتن ۰ : مفلس بودن» سی چیز  بودن. آ در جوی اسان ادن فولت  رفته» با زگشتن اقب 

>> خوردن: ?\(? :: نگ‌های  پنجگانه: سبز» سفید» سیاه» زرد و قرمز  است. و به تر تیب نقش‌های شاه» سی‌بی»  آس» سرباز و لکات را به سک دلخواه بر  آن نقش کنند. تکك‌خال» ورق بازی که یک  خال بر آن باشد. چهار شاهش به چهار: آس--  خوردن: به قوی‌تر از خودی مصادف شدن»  به حیله و چاره‌ای رساتر از حیلةٌ خود دچار  گردیدن.   آسا: 28 (.) خمیازه» دهان دره» سباستو  باسکث.    ۳  ابا 252 ۱( زبور» رینت» ارایش. وقار»    تثات» تمکین» آهستگی. هت صلات.    آسا فرهنگ فارسی معین ۴۵    طرز» روش قاعده» قانون. (- اسا - سا  (پ.) بصورت پسوند به آخر اسم ملحق  شود و صفتی دال بر شباهت و مانندگی  سازد: آشتعان سا بر آسای: مانند» به منز له.  آسا: 2 (- آسای) (افا.) آساینده. آسایش  دهنل ۵.   اسان: 8 (ص.  

>> خوردن: ?\(? :: ب کم ۱ چرمی که  میرشکاران بر دست کنند و بدان باز و چرغ  و غیره را بر دست گيرند.  بسهمان: «عدءا آقس. بهمن از اسمای  معمول در ايران اباستان] (مبهم.) شخص یا  شیْ مجهول) باستار» بستار: فلان و بهمان.  بهم خوردن: 9,7 تصادم کردن»  برخورد کردن. منحل شدن جمعیت» حزب  و غیره. آشوب شدن مزاجء بهم خوردن  حال شخص.   رسیدد: ۳2)0(51420-. (مسص‌ل.)  وان یکلا گر خساقات کر3 هو کر    بوصال یکدیگر رسیدن (زن و مرد). بوجود    آمدن» ایجاد شدن. پیدا شدن» بدست  آمدن: در این فصل موز بهم نمی‌رسد.   بهم زدن: (مص‌م.) خراب کردن»  بی تر تیب کردن» آشفته ساختن. باطل کر دن.  منحل کردن (جمعیت» حزب و غیره).  مخلوط کردن» زیر و رو کردن. قهر کردن با  1"   بهمن: ۳2۲۳20 [نیک منش] (اح.)
```


## [2026-09-14T03:13:56.574Z] TOOL CALL #34: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-14T03:13:56.581Z] TOOL RESULT

```


```


## [2026-09-14T03:13:59.550Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nt=open('MON_part1.txt',encoding='utf-8',errors='replace').read()\nfor m in list(re.finditer('اخر: ۲',t))[:3]:\n    i=m.start(); print('::',t[max(0,i-100):i+400].replace('\\n',' '),'\\n')\nfor m in list(re.finditer('میرآخور|میر آخور',t))[:2]:\n    i=m.start(); print('MIR::',t[max(0,i-150):i+200].replace('\\n',' '),'\\n')\nEOF"
}
```


### [2026-09-14T03:14:00.664Z] TOOL RESULT

```
:: چیز یا دو کس» غیر؛ ج.  آخرین.  اخر: 2 [ع.] (ص.) پسین» وایسین,» بابان؛  انجام فرجام؛ مق. اولی اغاز.  اخر: ۲ (ا.) جایگاهی از گل و سنگک و  مانند آن که برای علف و کاه و جو خوردن  چهار بایان سازند؛ معلف» طو له اصطبل.  گودیی که در سنگت با چوب برای آب  ایجاد کنند» حوضجه. (جاذ.) قوس مانندی  از استخوان بالای سینه و زیر گردن. . 0  صورتی فلکی که عرب آن را معلف گوید.  اخسریین: 206۲-01 [ع. ف.] (اف.ا.)  عاقبت‌اندیش» آنکه از پیش نتيجهةٌ کارها را  در یابد.  آخرت: تفت 4 ۰ (.) 11 جهان» جهان  دیگر سرای دیگی عقمی.  

MIR:: جامه)؛ بر کنده. کشیده  (صف. رده). پیوسته» متصل. نواخته» سامان  کرده» کوک کردن (الت مو سیقی).  اخته‌چی: آ-.2 [تر.] (ص‌مر.) داروغه  اصطبل,» ناظر طویله. میر آخور.  اخد: : 6 [ع.] (افا) گیر نده؛ ج ج. آخذین.  آخسر: تة (ع.] (ص.) در دگس  دیگری» یکی از دو چیز یا دو کس» غیر؛ ج.  آخرین.  اخر: 2 [ع.] (ص.) پسین» وایسین,» بابان؛  انجام فرجام؛ مق. اولی اغاز.  اخر 

MIR:: ه  کار را بطور قطع و یقین بیان نماید.   اشت: (ع.] (ا.) خواهر» همشیره. مانند»  مثل» فرین؛ ج. اخوات.   اختاجی: آ-2021 [- اختاچی - اخته‌چی»  تر.] (امر.) میرآخور» طو بله‌دار» مهتر»  ستوربان.   اختبار: تفت [ع.] (مسص ع.) آزمودن»  امتحان کردن. (مصل.) آگاهی یافتن از  چیزی يا خبری» خبردار شدن؛ ج. اختبارات.    ۲ ۰ ۱ فر هکت فارسی وه 7 اختتام    اختتام. صقاهاه
```


## [2026-09-14T03:14:07.588Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/swel-",
 "prompt": "Does this page list a Proto-Indo-European root *swel- meaning \"to eat, drink\" or \"to swallow\"? What reflexes (Avestan, Germanic) are given, and what Pokorny page is cited?"
}
```


### [2026-09-14T03:14:08.743Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-14T03:14:09.527Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A2%D8%AE%D9%88%D9%86%D8%AF",
 "prompt": "Give the full etymology section for Persian آخوند (āxund) — what origin does Wiktionary give, and which scholars/sources are cited?"
}
```


### [2026-09-14T03:14:14.603Z] TOOL RESULT

```
# Etymology of Persian آخوند (āxund)

According to Wiktionary, the origin is **unclear**. The entry presents several competing theories:

1. **Compound theory**: The word may combine the first element from آقا (âqâ, "agha") with a second element that could derive from either:
   - خواندن (xândan, meaning "to read, study"), or
   - خداوند (xodâvand, meaning "master, God")

2. **Scholar assessment**: The Encyclopædia Iranica is cited as stating this set of etymologies is "[not] entirely satisfactory."

**Source cited**: H. Algar (July 29, 2011), "Āḵūnd," in Encyclopædia Iranica Online, Encyclopædia Iranica Foundation.

The entry emphasizes uncertainty, noting no definitive etymological consensus exists for this term.
```


## [2026-09-14T03:14:29.675Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/swenh%E2%82%82-",
 "prompt": "What is the reconstructed PIE root for \"to sound\"? List its descendants (Latin sonus/sonare, Proto-Germanic *swanaz 'swan', Sanskrit svanati, Avestan) and any cited references."
}
```


## [2026-09-14T03:14:31.728Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AE%D9%88%D8%B1%D8%AF%D9%86",
 "prompt": "Give the Persian etymology section for خوردن (xordan) 'to eat': Middle Persian form, Proto-Iranian, Avestan, PIE root cited, and sources (Hasandust, Cheung, MacKenzie)."
}
```


### [2026-09-14T03:14:36.120Z] TOOL RESULT

```
# Proto-Indo-European Root for "to Sound"

## Root
The reconstructed PIE root is **\*swenh₂-**, meaning "to sound."

## Key Descendants

**Latin:** The root yields *sonō* ("to sound") and *sonus* ("sound"), derived from Proto-Italic forms.

**Proto-Germanic:** \*swanaz develops into the word for "swan," reflecting the bird's characteristic sounds.

**Sanskrit:** The root appears as *svánati* ("to sound"), demonstrating preservation in Indo-Aryan languages.

**Avestan:** Iranian reflexes include forms like *apaxᵛanuuaiṇti* ("sound away"), showing the root's spread across Indo-Iranian branches.

## Additional Descendants
Welsh *honni* ("to announce") and Kurdish *xwêndin*/*xwendin* also derive from this root through various phonetic transformations across different language families.

## References
The entry cites seven scholarly sources, including works by Cheung (2007), Derksen (2008), De Vaan (2008), Kroonen (2013), Matasović (2009), Rix (2001), and Schrijver (1991)—all part of the Leiden Indo-European Etymological Dictionary Series.
```


### [2026-09-14T03:14:39.889Z] TOOL RESULT

```
# Persian Etymology of خوردن (xordan)

## Middle Persian Form
The word is "Inherited from Middle Persian" with the form noted as OŠTEN-tn' (/xwardan/), also appearing in Book Pahlavi as 𐫑𐫇𐫡𐫅𐫗 (k̇wrdn).

## Proto-Iranian and Earlier Origins
It derives from Proto-Iranian *hwar- ("to eat, consume"), which itself comes from Proto-Indo-Iranian *suar-. The source notes that "further origin unknown, with no obvious Indo-European cognates outside of Iranian."

## Avestan Cognate
The Avestan cognate is 𐬓𐬀𐬭𐬀𐬌𐬙𐬌 (xᵛaraiti), meaning "to consume, eat."

## Semantic Development
The etymology explains that the "Original meaning of the root was 'to take.' During the Proto-Iranian period it replaced the native Indo-European root for 'to eat.'"

## Sources
The page cites **Johnny Cheung's *Etymological Dictionary of the Iranian Verb*** (Brill, 2007, page 147) as the primary etymological source. The other reference is Hayyim's 1934 *New Persian–English dictionary*.

Note: The entry does not cite Hasandust or MacKenzie in the provided content.
```


## [2026-09-14T03:14:47.452Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== CHEUNG Hwar ===\"; grep -n -A12 \"^\\*HWAR\\|HWAR ‘to eat\\|Hwar ‘to eat\" CHEUNG.txt | head -40; echo; grep -n \"to eat, consume\\|hwar-\" CHEUNG.txt | head -15"
}
```


### [2026-09-14T03:14:47.526Z] TOOL RESULT

```
=== CHEUNG Hwar ===

10326:*PARTHIAN: wxr- ‘to eat’ || (+ *4-) "xwr- ‘to eat, consume, devour (of fire)’ 
10334:*SOGDIAN: SSogd. xwr-, BSogd. xwr-, CSogd. xwr-, MSogd. xwr- ‘to eat, consume’, 
10375:Ó This root is probably identical to *hyar’. The meaning ‘to eat, consume’ is 
10448:*huar ‘to swear’ etymologically separate from *hyar! ‘to eat, consume’.
```


## [2026-09-14T03:14:50.105Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '10300,10400p' CHEUNG.txt"
}
```


### [2026-09-14T03:14:50.201Z] TOOL RESULT

```
*REFERENCES: Zhukovskij I: 114; KPF I: 80a, 137a f., 206a, 244a; Ivanow 1926: 421; EVP: 9; KPF II: 
191; Christensen, Contributions I: 63, 157 f., 257; Christensen, Contributions II: 53, 113, 157; Lambton 
1938: 40b, 76a; IIFL II: 538b, 270a; MacKenzie 1966: 39, 112; EVS: 51b, 70b, 99a, 101a, 119a, 64a; 
WIM Т: 70; WIM II/1: 84; DKS: 495a f., 37b f., 392b; Vahman — Asatrian 1987: 148; WIM III: 100, 105; 
Abaev, Slovar’ IV: 272; Werba 1997: 422; Paul 1998: 319a; Steblin-Kamenskij 1999: 305, 411; Lecoq 
2002: 122, 127 (passim); NEVP: 7; Korn 2005: 87, 411 (passim) 


*huar' ‘to consume, eat’ 

*AVESTAN: ҮАУ. x’ar- ‘to consume, eat’ || (+ *fra-) ‘to consume, eat’ = Liste: 18 
Pres. them.: IND. 3sg. YAv. x'araiti, 3р1. YAv. x'aronti, med. 3р1. YAv. x'aronte (Y 9.16), SUBJ. 3sg. 
Y Av. x‘arat, OPT. YAv. ? x'arois (P 28), 3sg. YAv. x‘ardit (N 45), YAv. fra.gharöit (N 71), IMPV. 3sg. 
Y Av. x'aratu (У 3.19), 2pl. YAv. x‘arata, 3pl. Y Av. frax'arontu (Yt 5.92, Yt 5.93); Partic.: pres. x'arant-; 
Pass.: pres. IND. 35р. YAv. x'airiieite (V 2.26, V 2.34); Caus.: pres. INJ. 3sg. YAv. fran‘haraiiat (A 3.4) 


*MIDDLE PERSIAN: MMP xwr-, BMP hwl- /xwar-/ (‘STHN-) ‘to drink, eat, enjoy 


(food), consume’ = DMMPP: 368b f. 
Widely attested: Pres.: IND. 35р. MMP xwryd, MMP xwryyd, 1р1. MMP xwr'm, BMP hwlym /xwarém/, 
etc. 


*PARTHIAN: wxr- ‘to eat’ || (+ *4-) "xwr- ‘to eat, consume, devour (of fire)’ 
= Ghilain: 57 | DMMPP: 349a, 79b 

Pres.: SUBJ. 15р. wxr’n, 3sg. wxr’h; Partic.: perf. pass. wxrd; Inf.: wxrd, wxrdn || (+ *a-) Pres.: IND. 35р. 
"xwryd, ’xwrynd 

*KHOTANESE: Khot. hvar- ‘to consume’ — SGS: 156 

*SOGDIAN: SSogd. xwr-, BSogd. xwr-, CSogd. xwr-, MSogd. xwr- ‘to eat, consume’, 
BSogd. xwyr, CSogd. xwyr (caus.) ‘to cause to eat’ || (+ *a-) MSogd. "xwyr ‘to 
feed’ || (+ *pati-) BSogd. ptxwrk’ ‘devouring, devourment’ 

Widely attested: Pres.: IND. 3sg. BSogd. хиті, 3р1. BSogd. xwr’nt, CSogd. xwrnt, MSogd. xwr’nt, etc. || 
(+ *a-) Caus.: pres. IMPV. 2р1. MSogd. "xwyró 

*CHORESMIAN: x(w)r- ‘to consume, eat, drink’, xw’ry- (caus.) ‘to feed, give to drink’ 
|| (+ *pati-) рсхг- ‘to taste’, bexw’ry- (caus.) ‘to give (something to someone) to 
taste’ = Samadi: 238, 146 f., 244 

*NWIR: Widely attested: NP xurdan/x’ar-, Bal. wärt/war-, Kurd. (Kurm.) xwärin/xu-, 
(Sor.) xwardin/x6-, Abz. xarda/xor-, Abyan. xarda/xar-, Anar. -ixo(r)/ (impv.) ixur, 


148 *huar | 


Awrom. wärdäy/(-)war-, Fariz. -yärd-, -xa/-yär-, Yar. -ya/-yor-, Gz. yer-/yort, yü-, 
Gil. (Rsht.) yiirdeen/yir-, Gur. (Kand.) wärd-/-uwär-, Ham. xortän/xär-, Isfah. 
xortän/xer-, Jow. bam-xard/a-xor-, Meim. bem-xa:/a-xor-, Nn. xärte/xur-, Natan. 
-yard/yor-, Qohr. xarda/xor-, Semn. -xurd-, -xurt/-xur-, Tt. xarda/xr-, xer- ‘to eat, 
drink’, Soi xa/4-xor-, Zaz. werdis/wen- ‘to eat’, Khuns. xur-, xor-/yurt, Mah. hur-, 
Sang. -yórt-, -yord/yun-, Shamerz. -yórd-/rorán-, ? Khr. for-, ? Siv. üer-, (Ner-/fard 
‘to eat’ || (+ *nis-) Anar., Nn. nisxar ‘rumination’. 9 The "Median" development of 
*hu- > f- might explain Siv. far-, Khr. for- ‘to eat’ (and some other Central Iranian 
dialects of Iran) from *huar-. However, the assumption of this development cannot 
be applied to Khot. phude ‘food’ and the Pamir forms, Sh. fur-/furt, Khf. fur-/furt, 
Sariq. fir-/fird, für-/fürd, Ishk. far-, etc. ‘to eat (with a spoon)’. These forms rather 
point to yet another (different) root for ‘to eat’: *far?. 

*NEIR: Oss. I. xeryn/xord (xzerd), D. xweerun/xward, Pash. xwarol/xür-, Yghn. x"ar-/ 
x"órta, Sh. xar-/xüd, Rosh. xar-/xüg, Bart. xar-/xüg, Sariq. xor-/xig, xüg, Yzgh. 
xar-, x" ar-/xug ‘to eat’, (caus.) Sariq. xaron-/xarond ‘to feed’, Yi. xóar-/xür-, M. 
xur-/xur- ‘to eat’, Oss. І. хага, D. xwærdæ ‘food’, І. xor, D. xwar ‘grain’, Rosh. 
xarüc ‘glutton’, Yzgh. x"arag ‘hungry’ || (+ *pati-) Sariq. paxig ‘luncheon’, paxik 
‘morning meal’ 

*MISC: Par. xar-/xur ‘to eat’, Orm. x(u)r-/xuluk, xwalak ‘to eat, drink’ = xr-/xólók, 
xr-/xolok, xollok 

Ó This root is probably identical to *hyar’. The meaning ‘to eat, consume’ is 
therefore secondary and perhaps originally used in a more informal way in PIr., 
replacing the IE ‘eat’ root: *H,ed-, Hitt. e-ed-mi, Gr. Éópevou, Lat. edo ‘I eat’, Skt. 
ad, OCS jasti ‘to eat’, Lith. ésti ‘to eat (of animals)’, Goth. itan, Engl. to eat, etc. 
(LIV:230; Pokormy: 287 ff.). The Ir. continuation *Had appears to have been 
preserved in several nominal formations: NP aspast ‘lucerne (Medicago sativa)’, 
Oss. I. ad, D. ade ‘taste’, I. lae£z-ad ‘unpleasant taste of spoilt, rotting products’, D. 
reft-ad ‘lunch’, ? Pash. 3pésta (Е) ‘lucerne’ (ESIJa I: 77f). On the Iranian expression 
for ‘to swear, take an oath’, as in Sogd. swk’nt xwr-, MMP swgnd xwrdn, NP 
saugand xurdan, Kurd. sont xarin, etc., see Schwartz 1989: 293 ff. 

«PIE — 9 There is probably no need to reconstruct an IE root *suel- ‘verschlucken 
(vel sim.)’, as done in IEW, Le, and LIV, Le, on which see above. = LIV: 609 | 
Pok.: 1045 


*IE COGNATES: — 

*REFERENCES: KPF I: 80b, 137b f., 206a, 244b f.; Ivanow 1926: 421; EVP: 99; IIFL I: 299b, 412b; KPF 
II: 193 f.; IIFL II: 267a; Christensen, Contributions I: 63, 159, 258; Christensen, Contributions II: 113, 
158; Abrahamian 1936: 125, 134; Lambton 1938: 42a, 77b; Andreev — PeSéereva: 364a f.; MacKenzie 
1966: 111; EVS: 98a, 119a, 33a, 54b; WIM I: 70; WIM II/1: 79; DKS: 503b f.; WIM III: 105, 117; 
Abaev, Slovar’ IV: 183, 178, 215 f.; Cabolov 1997: 71; Paul 1998: 318b; Lecoq 2002: 121, 124, 610a, 
634a (passim); NEVP: 96; Kiefer 2003: 209; Korn 2005: 97, 411 (passim)
```


## [2026-09-14T03:15:22.169Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; pdftoppm -f 491 -l 491 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg491 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg491.png"
}
```


### [2026-09-14T03:15:23.869Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 70427 Sep 13 23:15 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg491.png
```


## [2026-09-14T03:15:24.035Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A2%D8%AE%D9%88%D8%B1",
 "prompt": "Give the etymology of Persian آخور (āxur) 'manger, stable' — Middle Persian form, Proto-Iranian reconstruction, and any relation to آب 'water' or خوردن 'to eat'."
}
```


### [2026-09-14T03:15:29.195Z] TOOL RESULT

```
# Etymology of Persian آخور (āxor)

## Middle Persian Origin
The word derives from Middle Persian *āxwarr* meaning "manger; stable."

## Proto-Iranian Root
It traces back to **Proto-Iranian *\*hwar-*** meaning "to eat, consume," reflecting the literal sense of "a place for eating."

## Relation to خوردن (xwardan)
The entry explicitly notes that خوردن (xwardan, "to eat") derives from the same Proto-Iranian root *\*hwar-*. This shared etymological root demonstrates a direct semantic connection between the two words.

## No Connection to آب (water)
The documentation provides no evidence linking آخور to آب (water). The word's meaning and etymology center entirely on eating/consumption and animal feeding facilities, not water-related concepts.
```


## [2026-09-14T03:15:31.012Z] TOOL CALL #44: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg491.png"
}
```


### [2026-09-14T03:15:31.604Z] TOOL RESULT

```

```


## [2026-09-14T03:15:31.586Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-14T03:15:42.776Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && /home/sfmqrb/git/rishe/../ 2>/dev/null; pdftoppm -f 491 -l 491 -r 400 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg491big && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg491big.png'); print(im.size)\nw,h=im.size\nim.crop((int(0.24*w),int(0.42*h),int(0.42*w),int(0.48*h))).resize((int(0.18*w*2),int(0.06*h*2))).save('crop491.png')\n\"; ls"
}
```


### [2026-09-14T03:15:45.878Z] TOOL RESULT

```
(3400, 4400)
391-top.png
394hi.png
394-zoom.png
400-bot.png
400-top.png
404-top.png
411-top.png
412-zoom.png
414-bot.png
417hi.png
417-top.png
417-zoom.png
421-top.png
428hi.png
428-zoom2.png
428-zoom.png
429hi.png
429-zoom.png
431-top.png
432-bot.png
436-full.png
440-top.png
442hi.png
442-zoom.png
444hi.png
444-zoom.png
445-mid.png
446-full.png
450hi.png
450-zoom.png
454-top.png
457hi.png
457-zoom.png
460-top.png
462-full.png
466hi.png
466-mid.png
472-top.png
474hi.png
474-zoom.png
afm74-420.png
afm76-421.png
agents.txt
ahd430.txt
asha-468.txt
beekes410.txt
bly78-473.png
bqt1328-ftr-437.png
bqt1328-hdr-437.png
bqt1328-top-437.png
bqt1330-top-437.png
bqt1-440.txt
bqt2123-fn-435.png
bqt390_436_foot.jpg
bqt390_436_top.jpg
bqt390_662_foot.jpg
bqt390_662_top.jpg
bqt390_n436.jpg
bqt390_n662.jpg
bqt439-l254.jpg
bqt469-n486-bottom.png
bqt469-n486.jpg
bqt469-n486-top.png
bqt469-n547-bottom.png
bqt469-n547-fn2.png
bqt469-n547-hdr.png
bqt469-n547.jpg
bqt469-n547-mid.png
bqt469-n547-top.png
bqt-482-389-foot.png
bqt-482-389.jpg
bqt-482-390-foot2.png
bqt-482-390-foot.png
bqt-482-390.jpg
bqt508-495-bl2.png
bqt508-495-bl.png
bqt508-495.jpg
bqt509-495.jpg
bqt509-495-tr.png
build2-434.py
build2-471.py
build3-434.py
build-389.py
build-390.py
build-391.py
build393.py
build-394.py
build-395.py
build-396.py
build-398.py
build-400.py
build-401.py
build-405.py
build-406.py
build-407.py
build-412.py
build-414.py
build-415.py
build-417.py
build-418.py
build-419.py
build-422.py
build-425.py
build-426.py
build-428.py
build-429.py
build-430.py
build-431.py
build-434.py
build-435.py
build-438.py
build-439.py
build-440.py
build-444.py
build-445.py
build-446.py
build-447.py
build-448.py
build-450.py
build-452.py
build-453.py
build-454.py
build-455.py
build-458.py
build460.py
build-461.py
build-463.py
build-464.py
build-465.py
build-468.py
build-470.py
build-471.py
build-472.py
build-473.py
build-474.py
c404-empty.png
c404-greek.png
c404-patil.png
c404-pest.png
c404-symp2.png
c404-symp.png
c412_cedar.png
c412_makrome.png
c412_makrome_zoom.png
c412_meqrameh.png
c412_meq_zoom.png
c412_sedr_zoom2.png
c412_sedr_zoom.png
c442-fa8b.png
c442-fa8c.png
c442-fa8.png
c442-samavar2.png
c442-samavar3.png
c442-samavar.png
c442-symp-zoom2.png
c442-symp-zoom.png
c497-arabic.png
c497-shakuk.png
crop14-394.png
crop18-394.png
crop411_a.png
crop411_b.png
crop411_c.png
crop419_a.png
crop419_b.png
crop419_c.png
crop419_d.png
crop419_grk.png
crop419_skt.png
crop428a.png
crop428b.png
crop428c.png
crop428d.png
crop-437.png
crop460-fa.png
crop460-latin.png
crop460-mithere.png
crop460-shamunhdr.png
crop460-shamun.png
crop468a.png
crop480_astro.png
crop480_chol2.png
crop480_chol.png
crop480_ster.png
crop491.png
crop496-a.png
drd496.wiki
e0-434.json
edit_about.py
edit_research.py
ffprof
gen-420.py
irn-425.pdf
irn-425.txt
kent2-448.txt
kent-448.txt
knt-440.txt
knt443.txt
meta-443-knt.json
oew459.txt
out488.bin
part1-471.json
pg390b.jpg
pg390b.png
pg390.png
pg391big.png
pg391crop.png
pg391.png
pg391root.png
pg391sog.png
pg392.png
pg393.png
pg394hi.png
pg394.png
pg397.png
pg398.png
pg399-crop1.png
pg399-greek.png
pg399.png
pg399-sog.png
pg400big.png
pg400_fa_heli.png
pg400_fr2.png
pg400_french.png
pg400_kasak2.png
pg400_kasak3.png
pg400_kasak.png
pg400.png
pg402.png
pg404hi.png
pg404.png
pg405.png
pg406.png
pg407.png
pg408-ampus.png
pg408-germ.png
pg408.png
pg409.png
pg410hi.png
pg410-k2.png
pg410-kadm2.png
pg410-kadm.png
pg410-persian.png
pg410.png
pg410-q2.png
pg410-qedam.png
pg411_300.png
pg411.png
pg412_hi.png
pg412.png
pg412_uhi.png
pg413.png
pg414-greek.png
pg414.png
pg415-emptybox.png
pg415hi.png
pg415.png
pg416-v.png
pg417.png
pg418hi.png
pg418.png
pg418-raj2.png
pg418-raj3.png
pg418-rajidan.png
pg419_hi.png
pg419.png
pg420b.png
pg420.png
pg421.png
pg422.png
pg423.png
pg424.png
pg426.png
pg428hi.png
pg428.png
pg429-crop1.png
pg429-crop2.png
pg429-crop3.png
pg429hi.png
pg429.png
pg431.png
pg432.png
pg433.png
pg435-n1.png
pg435-n4.png
pg435.png
pg436.png
pg437-437.png
pg437hi-437.png
pg438.png
pg439.png
pg440.png
pg442hi-442.png
pg442-p442.png
pg442uhi-442.png
pg443.png
pg444.png
pg444-serom.png
pg444-sibum.png
pg445-crop.png
pg445.png
pg446.png
pg447-crop.png
pg447.png
pg449.png
pg450hi.png
pg450-pechkam.png
pg450.png
pg450-shangarf.png
pg451.png
pg452.png
pg453.png
pg454.png
pg456-germ.png
pg456hi.png
pg456.png
pg457_crop3b.png
pg457_crop3c.png
pg457_crop3.png
pg457hi.png
pg457.png
pg458.png
pg459.png
pg460hi.png
pg460.png
pg462-fa.png
pg462hi.png
pg462.png
pg462-sog2.png
pg462-sog.png
pg463-v.png
pg464.png
pg465.png
pg466-crop1.png
pg466-crop2.png
pg466-crop3.png
pg466hi.png
pg466-osqof.png
pg466.png
pg467.png
pg468hi.png
pg468.png
pg469.png
pg470.png
pg471.png
pg472-crop.png
pg472hi.png
pg472.png
pg473.png
pg474.png
pg474-sogd.png
pg475.png
pg476.png
pg477.png
pg479.png
pg480hi.png
pg480.png
pg484.png
pg486.png
pg487.png
pg488.png
pg490.png
pg491big.png
pg491.png
pg494hi.png
pg494.png
pg494-root.png
pg494-tambour.png
pg495.png
pg496hi.png
pg496.png
pg497.png
pla18-468-crop.png
pla18-468.png
queue.txt
sem410.html
u_mak.png
u_meq.png
u_sedr.png
write397.py
write-402.py
write409.py
write410.py
write436.py
write469.py
write476.py
```


## [2026-09-14T03:15:49.001Z] TOOL CALL #46: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/crop491.png"
}
```


### [2026-09-14T03:15:49.021Z] TOOL RESULT

```

```


## [2026-09-14T03:15:53.225Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg491big.png'); w,h=im.size\nim.crop((int(0.25*w),int(0.455*h),int(0.44*w),int(0.50*h))).resize((int(0.19*w*2),int(0.045*h*2))).save('crop491b.png')\nim.crop((int(0.22*w),int(0.175*h),int(0.44*w),int(0.25*h))).resize((int(0.22*w*2),int(0.075*h*2))).save('crop491c.png')\n\""
}
```


### [2026-09-14T03:15:54.712Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T03:15:56.713Z] TOOL CALL #48: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/crop491b.png"
}
```


### [2026-09-14T03:15:56.743Z] TOOL RESULT

```

```


## [2026-09-14T03:16:00.277Z] TOOL CALL #49: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/crop491c.png"
}
```


### [2026-09-14T03:16:00.354Z] TOOL RESULT

```

```


## [2026-09-14T03:16:12.308Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; echo \"=== WLD Bd2 leaf 535 (p.530) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==535' WLD_Bd2_pages.txt | head -40; echo \"=== WLD Bd2 leaf 529-530 (p.524-525) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==529' WLD_Bd2_pages.txt | head -40"
}
```


### [2026-09-14T03:16:13.514Z] TOOL RESULT

```
=== WLD Bd2 leaf 535 (p.530) ===
abwischen^, mhd. swerben „umlierwirbelii“ (ahd. mhd. swarp, -bes m. „gur-
ges‘', ahd. swirbil m. „Wirbeb Struder^).

   Gr. ovQcpog n., ovQ<peT6g m. „Kehrichfe‘^, ovQ(pai, -dxog „Kehricht der
Menschheit, Gesindel“?
   Persson Wzerw. 55, Much ZfdA. 32, 169, Falk-Torp u. svarve; die germ.
Worte     sind kaum nach Zupitza Gutt. 57 mit kuerpjbh in germ, hwerban
unter idg. skuerpjbJi- zu vereinigen, sondern svsrbh- und kuerpjbh nur als
Parallel wurzeln neben einander einzuschatzen.
   ovgq^og ist nur unter dem Yorbehalt zu vergleichen, da8 fiir die Be-
wahrung des o- Hermanns (vielleicht auch dem Paare ays' vg gerecht                 :




werdende?) satzphon. Erklarung richtig, oder a- nach den flgd. Worten
erhalten ist: einerseits aalgco „fege‘‘, adgov, odgvg m. „Besen; Keh-
richt‘‘, aagovv „fegen“, andrerseits (Pick BB. 5, 167, G. Meyer Alb. St.

Ill 53 ff.) ovgco (fut. ovgd>) ziehe, schleppe, reiBe fort, fege, schlemme,
wasche“, ovgpog „das Hinziehen; das Sich-winden der Schlange, das Er-
brechen“, ovgjbiaia „Brechmittel“, ovgfxa n. „Schleppkleid; Kehricht'^, ovgTrjg
„Zugseil;  ein Kloben, um den das Sell lauft“, ovgiig „Sandbank“ (nach
Wilamowitz „Strudel“, s. Prellwitz ^ 44 1 f.) ob diese die unerw. Wz. dar-
                                                          ;


       woraus suerbh- erweitert ware, ist fraglich, desgleichen, ob oaigco
stellen,
uberhaupt auf su^rid beruht mit Erhaltung des a- (s. Brgm. Thumb 141)
oder aus tu^r-id, tur- und zu iuer- „drehen, quirlen*^? (s Hirt Abl. 12.
Aber anders Vok. 88, wo er wieder zu suer zuriickkehrt. Prellwitz aaO.).

1. snel- jjSchlingen, essen,               trinken“?
  Pick      341 vergleicht av. x^ar- „genie6en, verzehren, essen, trinken“
mit flgd. germ. Grappe (s. die Zsfassung bei Palk-Torp u. svelge^ sold III,
soli)  engl. sicill „verschlingen, viel und gierig trinken“ (auch „spulen“, wie
        ;


=== WLD Bd2 leaf 529-530 (p.524-525) ===
         ;                                                                                                       ;




524                                        suep-, sup              snen-


   Curtius^ 289, Fick               153, 341, 579, 11^ 325                 (ir.    socM „Sclxweigen“ aus
^sopto-^     Oder   '^supto^)   kaum annehmbar), III^ 548, Falk-Torp u, sove^ sevn^
Trautmann Bsl. Wb. 292 f.

2, suep-,   sup- „schwingend werfen, schleudern, ausschiitten^'.
   Yollstufig nur in aksL svepitisq „agitari'‘; schwundstufig                                          „schutten,
streuen'". Iter, sypati „schutten“, rasypati „ausstreuen''; sunqii „efFundere“,
^p^ „Haufe‘' (aber lit. siipti „schaukeln, megen“ eher zu sen „biegen“) ; lat.
supo, -are „werfen‘^ dissip)0, are „auseinanderwerfen, zerstreuen'S obsipo, -are
„entgegensprengen (Wasser,                     um
                                      zu erfrisclien)“, insipere „hineinwerfen‘\
   Fick I® 676,     579 (als Alternative auch Froehde BB. 21, 329). Die
lat. Worte nicht zu ai. ksipdti „wirft“ (Kuhn KZ. 4, 23       (Froehde aaO.
s. dagegen Zup. BB. 25, 93, Vf. LEWb.^ s. v.).    Zupitzas Analyse von sypp-,
sup- als          -up- (: ai.      ,,wirft“; ks- wie in     s-uper) liberzeugt
nicht; solches "^ksup- ist auch (gegen Trautmann bei Vf. aaO.) nicht die
Grundlage von gr. xrvnog „dr6hnender Schlag“, das vielmehr ein Schall-
wort ahnlich wie e^t-ydovnog^ dovnog ist (Boisacq 1 98, 526 a 2).        Sehr                           —
fragwiirdige germ. Anreihungen bei Fick III ^ 548, Palk-Torp u. sope,
svaber
  germ, svab- und svap- (idg. ^sueb-) in aisl. soft „Kehrbesen“ (*swdtala-)^
sopa „kehren"* (^^sivbpdn), nd. sicabbeln „(von Wasser u. dgl.) hin- und her-
schlagen, wogen^^, nhd. schwapp-en^ -eln^ -ern u. dgl.


sueni- etwa   „sich (hin- und her- oder fort-) bewegen“, im Germ, meist
     „8chwimmen“ (wohl iiber „im Wasser herumpatschen, platschern‘").
  Cymr, chwyf „motus“; chivyfio „movere'" (u. dgl., Fick 11^ 323; auch nir.
siubhal „gehen'" fiir *siumhal-^ suemul-1 Uber air. to-senn- „treiben“, das
viell.    als     suem-d- mit     lit.   sumdyti „hetzen“ zu vgl.                  ist,   s.   u.   sen- „in   Be-
wegung setzen“); wahrscheinlich lit. sumdyti „hetzen‘' (Kaus. „sich schnell
bewegen machen^'; ibd,); norw. mdartl. svamla „phantasieren‘‘. svamra
```


## [2026-09-14T03:16:19.490Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; awk 'BEGIN{RS=\"\\f\"} NR==530' WLD_Bd2_pages.txt | head -50"
}
```


### [2026-09-14T03:16:20.540Z] TOOL RESULT

```
                                   suenq-, sunq-   — suento-, sunto                              525

die Gdbed.           und senn- „ein Instrument spielen“ nach der Weise von dt.
„Zitherschlagen'‘ zu beurteilen),       air. seyiim (d, i. wohl seinm^ vgl. nir. seinm)

„das Spielen, T6nen‘"; (aber air. seimin, simm „fistula“ ist nicht aus "^sein-
min dissimiliert; auch der Yergleich mit ahd. semida                      bei
Fick II ^ 300, 111^434 ist schwerlich richtig); ags. sivinsian „singen, Melo-
die Oder Musik machen“, gesivin „Melodie, Musik, Gesang“ (beachtens-
werte Bed.-Ubereinstimmung mit dem Kelt.); wohl auch ahd. ags. swan
„Schwan'‘, aisl. svanr „mannlicher Schwan“.
      Z. B. Pick      I^ 153, 579, IP 322, III^ 546, Kluge u. Scliivan, Suolahti
"Vogeln. 408,         Uhlenbeck As, Wb. 354.               —
                                                 Die Wz. ist wohl schallmalend,
                                                       <




vgl.    die   einigermafien        ahnlichen suer- „surren“,          sus-    5
                                                                                  ,sausen“   (Persson
Wzerw, 90)       ;
                      B. nhd. hell sowohl von Licht- als Gehorseindriicken
                      trotz   z.

also nicht mit su-en- „Sonne, Licht“ (s. u. sauel-) identisch (z. B. Pick I^
341, Uhlenbeck aaO.); ai. hvanati „klingt, t6nt“ darf nicht mit        unter
"^ksum- (Zup. BB, 25, 95) vermittelt werden     abg. zvoyi^ „Schalh‘ (Meillet
                                                               ;


IF. 5, 333: fiir svom nach ^ovc^ bleibt fern s. Osthoff BB. 24, 177).
  Pine Wzf. sen- neben swn- sucht Endzelin KZ. 44, 58 in lett. sanU^
senH „summen‘*, doch weicht es in der Bedeutungsfarbung ebenso ab, wie
das bei Pick II ^ 322 angefiihrte ir. sanas „Fiustern“                       (anl. s-,   vgl.   cymr.
hanes „history“ eig. „*rumor“, Pedersen KG. II 20).


suenq-, snnq- „schwerfallig (schwanger), schwer sein“.
  Ags. swangor „schwerfallig, trage“, nhd. swangar „schwanger''; lit. sunk-
stiijsunkau siinkti „schwer werden“, stinkiis „schwer'’ (von Korpern und
von Arbeiten), alter lit. simkinga „schwanger“. Zup. 9, 139, Persson Beitr.
189f.   An Trenmmg von dt. schicingen, mhd. stvaiiger „schlank“ usw.
(s.   smng „biegen‘') ist trotz Wood Mod. Phil. 5, 21 f. festzuhalten.

suento-, sunto- „rege,             riistig,   gesund“.
      Got. swinps „kraftig, stark, gesund“, aisl. svinnr „rasch, kraftig, klug^^,
ags. swlp „stark“, as. swiih^ swlthi^ swidi „kraftig, heftig, tapfer“, mhd.
sivint^ sivinde „gewaltig, stark, heftig, rasch, geschwind, grimmig“, nhd.
geschivind ; ahd. gistmt (-d-) „gesund“, as. gisund „unverletzt, heil, gesund“,
```


## [2026-09-14T03:16:29.789Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== BRT x'anat ===\"; grep -n \"anat.caxra\\|x'anat\\|hvanat\" BRT.txt | head -10; echo \"=== ARY خوردن ===\"; python3 - <<'EOF'\nimport re\nt=open('incoming/ARY/ARY_pages.txt',encoding='utf-8',errors='replace').read()\nfor w in ['خوردن','خواندن','آخور','خنیدن']:\n    for m in list(re.finditer(w,t))[:2]:\n        i=m.start()\n        seg=t[max(0,i-400):i+300]\n        pg=re.findall(r'\\[pdf page (\\d+)\\]',t[:i])\n        print('>>',w,'pdf page',pg[-1] if pg else '?','::',seg.replace('\\n',' ')[-500:],'\\n')\nEOF"
}
```


### [2026-09-14T03:16:30.935Z] TOOL RESULT

```
=== BRT x'anat ===
=== ARY خوردن ===
>> خوردن pdf page 64 :: 4۸): وت زا 7 (5۸7) دواد اسلواکی 5-07۸0): 1.7 برهان قاطع + ۴۴ بادداشت: 5 ۱- چم اصلی واژه‌ی "آش": خورش (طلاً در واژ‌ی "آشپز). ان واژه‌های همریشه‌ی "آش" در زبان‌های دیگر همه به صورت شکل‌های گرتاگون فمل "خوردن" هستند (مثلاً واژه‌ی آنگلیسی 3۸7 یعنی "خوردن" و واژه‌ی هنبت 131811 یعنی "می‌خورم"). ای ای هو ی ی ند اوسنایی (41557400: ,ش۸181 ,۸۷18189۸ برنانی (07880): ۸ 9 1 لانین (770ه۸ل): ,۸۲701715 پهلری (1شالله۲): ۳ اسلاری کهن (16/بما5 بل تال 0ا0): تخاری 8 (8 ((فلم707): 6 لاه ,۸۷171 ۵0۵0 لینوانی (12هنا777) 

>> خوردن pdf page 64 :: برهان قاطع + ۴۴ بادداشت: 5 ۱- چم اصلی واژه‌ی "آش": خورش (طلاً در واژ‌ی "آشپز). ان واژه‌های همریشه‌ی "آش" در زبان‌های دیگر همه به صورت شکل‌های گرتاگون فمل "خوردن" هستند (مثلاً واژه‌ی آنگلیسی 3۸7 یعنی "خوردن" و واژه‌ی هنبت 131811 یعنی "می‌خورم"). ای ای هو ی ی ند اوسنایی (41557400: ,ش۸181 ,۸۷18189۸ برنانی (07880): ۸ 9 1 لانین (770ه۸ل): ,۸۲701715 پهلری (1شالله۲): ۳ اسلاری کهن (16/بما5 بل تال 0ا0): تخاری 8 (8 ((فلم707): 6 لاه ,۸۷171 ۵0۵0 لینوانی (12هنا777): 05 سانکریت (5۸۸/۶8/7): ,۸۷۸ ۰ ,۸۷18 ام هتبت 

>> خواندن pdf page 22 :: بنیادین کمک زیادی کرد. این زبانهای مرده (تخاری مربوط به قرن‌های " هفتم تانهم میلادی و هتیت مربوط به ۲۰۰۰ تا ۱۲۰۰ سال پیش از میلاد) بیش ما در باره‌ی زبانهای ۱ هند و اروپایی راکامل‌ترکرده‌اند. هنوز کار خواندن هزاران لوح وخشت هنت به پایان نرسیده است [pdf page 23] ۴ ]1 ریشه‌های هندو اروپایی زبان فارسی و باستان شناسان هر سال اشیاء و مدارکك جدیدی را در ارتباط با هندو اروپائیان کهن اراثه می‌دهند. از این رو آینده‌ی پژوهشها وابسته به هند و اروپالیان نوید بخش است. شاخه‌های زبانهای هند و اروپایی ی کهن‌تری 

>> خواندن pdf page 23 :: و لوحه‌ها به حروف میخی (/۲112331۳03) و به زبان‌های هتیت‌کهن (حدود ۲۰۰۰ تا ۱۵۰۰ پیش از میلاد) و هتیت. میانه (حدود ۱۵۰۰ تا ۱۳۵۰ پیش از میلاد) وهتیت نو (حدود ۱۳۵۰ تا ۱۲۰۰ پیش از میلاد) نوشته .. شده‌اند. خواندن این لوحه‌ها و خشت‌ها هنوز ادامه دارد. از لووبان‌ها و پالائیکك‌ها و لیسپان‌ها مدارکك کمتری یافت شده است. این مدارک وابسته به دوران برنز بوده و منحصرند به نوشتارهای روی سنگه قبر و روی گنجانه‌های سفالین. وجود گورهای برجسته (1)1180۸) و آثار ویرانی ساختمان‌ها و جابجایی جمعیت حاکی از این است که این 

>> آخور pdf page 236 :: هب نیم #تهلا فرهنگ معین : ۱۳ ۱ انگلیسی (6۸019(0): (۸۸128375) ۰8177 بادداشت, ۱ واژه‌ی "خرفستر" (اوستایی:811۸۳977۸) از دو بخش ساخته شده است: اوستایی ‏ 1۳1387 به چم ان" و ارستایی -8(0-730)* یا -30 به چم آخوردن" (۳01608879 :620). در زبان پهلوی نیز واژه‌ی 14183 چم تن" پا "بدن" را داشت (31۸66881218 :104) [pdf page 237] ۸ | خروس ۲- 0311008 ریشه‌ی واژه‌های ژرمنی این فهرست را انامعلوم" می‌نامد (۸/103177(:0011075) 875) ۳ چم این واژه در همه‌ی وازه‌های اين فهرست (به جز اوستایی و پهلری): "تن "» "پدن" اوستای 

>> آخور pdf page 248 :: ان :5/ نم ظ الما 4 برهان قاطع : ۷۸۲ آلمانی (0882/(۷): اما اند هن لغت‌نامه دهخدا: ۱۰۰۳۷ انگلیسی کهن 8۸۷01820 2ت0): 8۷/8۸7 فرهنگ معین : ۱۳۳۹ انگلیسی (50/ا8(/0): لا اون ا [pdf page 248] ۹ ۲ خوان (به چم آخوردنی" و سینی یا طبق "مواد خوراکی") / ۲۴۹ بادداشت: ۱ ۱ بازگشت به: سیاه. ۲ چم این واژه در زبان لاتین: کلیف و چرکین. ۳ چم این واژه در زبان‌های ژرمنی: سیاه, اوستایی (۸887400): پرتغالی (۳087001288): ۳88(81۸018) 2۷۸۷08۸۰ ,2۸810 گرنبک (ع007[71): نان پهلری (۲7ائله): 7 70۷2 انگلیسی کهن (للولا8۸۷0 010)(شای
```


## [2026-09-14T03:16:37.734Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY; python3 - <<'EOF'\nimport re\nt=open('ARY_pages.txt',encoding='utf-8',errors='replace').read()\nparts=re.split(r'\\[pdf page (\\d+)\\]',t)\nd={}\nfor i in range(1,len(parts),2):\n    d[int(parts[i])]=parts[i+1]\nfor p in [247,248,249]:\n    print('=== pdf page',p,'(printed',p+1,') ===')\n    print(d.get(p,'')[:1800])\nEOF"
}
```


### [2026-09-14T03:16:38.809Z] TOOL RESULT

```
=== pdf page 247 (printed 248 ) ===

۸ / خواستن, خواست
آوستابی (4287/۷): یناه لیتوانی (۸۷ال۸تا 77 7آا): دا دا ری
بهلری (۲1اهاتزهه): ۸7
کردی (180150)): پسگشت‌ها ۹ ۸8782265
08710 ,20/۸8712 0 ۸000
سانسکریت (5275807): 26 نقققماتساطط
5 8۷۸2-870۸7 9 (۷۸۲) :25( ۸
آرمنی (۸ا/2452/): 0۸۴ 9 (81۸0) 57
برنانی (07888): تف800(1 ,11500۸1۸ 1 (088138) :۸10
این (0710): 5۷۸0585 ,8۷۸080 برهان قاطع : ۷۸۳
بادداشت:
۱ بازگشت به: شیرین.
فارسی (/۳881۸4): خوال (به چم "دو ده‌ای که برای ساختن مرکب از دود چراغ می‌گیرند")
اوستی (08557/6): ۸۲ دانمارکی (0۸۸/187): اک زان
سغخدی (/90001۸): نی نید سرئدی (317810150): این
خُتنی (2707۸/1885): 112۸۸ نروژی (/(0/05014: لاد
لاتین (/47): ۰ 9080588۳ ,8507255 هلندی (0076(7): اي ۸۷
گرتیک (007710): دی اد
نورس کهن (۸0782 010): دای امد پسگشت‌ها ۸5
ساکسونی کهن (54:00۷ ۰:01 8۷۷۸۲ 6 200220
فریزی کهن (۷لفا8لج7 صرا0): داد 0 (8۸35) 80
آلمانی کهن (/050/40 ۱۵ صا0): 3 داان :5/ نم ظ الما
4 برهان قاطع : ۷۸۲
آلمانی (0882/(۷): اما اند هن لغت‌نامه دهخدا: ۱۰۰۳۷
انگلیسی کهن 8۸۷01820 2ت0): 8۷/8۸7 فرهنگ معین : ۱۳۳۹
انگلیسی (50/ا8(/0): لا اون
ا

=== pdf page 248 (printed 249 ) ===

۹ ۲
خوان (به چم آخوردنی" و سینی یا طبق "مواد خوراکی") / ۲۴۹
بادداشت: ۱
۱ بازگشت به: سیاه.
۲ چم این واژه در زبان لاتین: کلیف و چرکین.
۳ چم این واژه در زبان‌های ژرمنی: سیاه,
اوستایی (۸887400): پرتغالی (۳087001288): ۳88(81۸018)
2۷۸۷08۸۰ ,2۸810 گرنبک (ع007[71): نان
پهلری (۲7ائله): 7 70۷2 انگلیسی کهن (للولا8۸۷0 010)(شاید)
کردی (80154/). 8 وال72 ل ان
بلوچی (/8۸/0[7): ۷۸ لیترانی (/12اهمتا7/): ادور ان
افغانی (پشتر) (/۸70/۸):
0 ال2 70۷ پسگشت‌ها 5
ساسکریت (64(/98/7): ,5۷70۸78 ری 0 سا
1 5۵ 5۷313 2 (۸81010ن81) ای انیت
پونانی (08627): لا ۱2۳۱۱۱ ۱ :2 ۸4
لاتین (47100): 51۸20580 ,81۸050 6 (8آق۸ ,95 (020)
فرانسه (لل2ق۳): لد نگ اند دی 1 (ه2) دی آاو ۱
اسپانیایی (7ل3]/مم52). 3 ارا ان دی برهان قاطع + ۷۸۳
ایتالیایی (فل7): ۰ 88طظ۳88(51۸0) فرهنگ معین : ۱۳۴۹
بادداشت. َ
شا ۱ چم این واژه در زبان لاتین و دیگر زبان‌های رومانس: وادار کردن» قبولاندن» متقاعد کردن.
۲ واژ‌ی آخوانجه" باه" نیز از همین ریشه است.
اوستایی (4188740): ۰ -7۷۸3/۸1 ,10۷۸8۰ ۸ ,2۷/۸۷0۸
پهلوی (۳۸/]۸4/1): اوستی (08587/6): ,20072

=== pdf page 249 (printed 250 ) ===

۵۱ ) خوافر
کردی (37//-): ۷8۸۲۵1۸۱ ,20۷201010 ایرلندی کهن (لا5ت#ا 0):
افغانی (پشتو) (//۸۳۵/7۸۸): ,5826
,8۸8787 ,120681 برتونی 700 ای : لین
سانسکریت (54(/5828/7): 5181۸71 ,-5۷7۸37 ۰ وی
لاین 80708:4710 ,800۸385 ,831/0 پسگشت‌ها ی
فرانسه (ثل/(۳8): 500 7 ۲0/0
اسپانبایی (52۸(]877): زدراال‌ران 4 (801770) مه
ایتالیایی (2ات74): 500 6 (تتف)) اد مد ی
رومانی (۸14۸(/۸): لزان 2035036[ ما8
پرتغالی (۳087001285): 507 8 (89017103) :0/105
ایسلندی کهن (0010۸14(4ف5 ا۵): 3 (801803) 7
َ لا مان 5 (81757) اابزک
انگلیسی کهن (تلوالا80/0 صان): 5 (858۸90) مدیم
۸7 ,811881۸ برهان قاطع : ۷۸۴
انگلیسی (8(70]50): 0
لیتوانی (01هنا 77 م: 5۸۸
بادداشت:
چم این واژه در زبان‌های رومانس (زبان‌های ناشی از لانین): صدا.
اوستایی (70۷۸۷۳3۸8:)4۲874/۷ ,7۷۸31۸ لاتین (۹7100س): ق لا ان
پپلوی (7اللم۳). ۸7 م#فلل7۷۸ فرانسه (7ق/(۳82). 521
اوستی (05557/0): 5 ,700 ایتالیایی ((مله7): ات8085
کردی (1/821577): هلال2 ,103 رومانی (42فلان۸): 508۸
بلوچی (/6ل۵۸): 0۷28 ,0۷۸11۵8 گونبکه (0077712): ۸
افنانی (پشتر) (/4۳0۸۷): ۰ 301 ,161108 ایسلندی کهن ((10۸۵ م5 02+
تخاری ۸ (۸ ((ل70227۸): 3 اند
تخاری 2 (8 [ل703۸2): ق ان فریزی کهن (۷لفاکل۲۴ ۰:00 :5۷788788
سانسکریت (84(/8877): 5۸ آلمانی کهن (08701۵(7 210 012):
ارمنی (/۸74480014): 01 ند رید
یونانی 08650): 10 آلمانی ((14ل057): ادا اند رنه هن
```


## [2026-09-14T03:16:56.663Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/swallow",
 "prompt": "Give the etymology of the verb \"swallow\" (Old English swelgan) and the PIE root cited."
}
```


## [2026-09-14T03:16:58.604Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://iranicaonline.org/articles/kavarnaq",
 "prompt": "What does Encyclopaedia Iranica say about the castle Ḵavarnaq / al-Khawarnaq near Hira — its name's Persian origin (xwarnag / xwarangāh)?"
}
```


### [2026-09-14T03:16:59.589Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-14T03:17:01.281Z] TOOL RESULT

```
# Etymology of "Swallow" (Verb)

**Old English Origin:**
The verb derives from Old English *swelgan*, described as "a class III strong verb" with the past tense *swealg* and past participle *swolgen*.

**Proto-Germanic Ancestry:**
It traces back to Proto-Germanic *swelgan/*swelhan*, which also produced cognates in Old Saxon, Old Norse, Middle Dutch, Old High German, and German.

**PIE Root:**
The ultimate source is PIE root *\*swel-* (1), meaning "to eat, drink." This same root appears in Iranian *\*khvara-* ("eating").

**Semantic Development:**
Beyond the literal sense of ingestion, the verb acquired figurative meanings by late 12c., including "drown, engulf" (of seas/graves), and by the 1590s, the sense of accepting beliefs "without question" and credulously.
```


## [2026-09-14T03:17:03.381Z] TOOL CALL #56: WebSearch

```json
{
 "query": "Khawarnaq castle Hira name from Persian khwarnagah \"place of eating and drinking\" etymology"
}
```


### [2026-09-14T03:17:08.527Z] TOOL RESULT

```
Web search results for query: "Khawarnaq castle Hira name from Persian khwarnagah "place of eating and drinking" etymology"

Links: [{"title":"Khawarnaq","url":"https://en.wikipedia.org/wiki/Khawarnaq"},{"title":"Al-Hira","url":"https://en.wikipedia.org/wiki/Al-Hira"},{"title":"ḴAWARNAQ - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/kawarnaq/"},{"title":"(PDF) The Landscape of Khawarnaq: From Reality to Symbol, the Evolution of Narratives About the Landscape of the Sassanid Khawarnaq Palace in Islamic Period Sources","url":"https://www.researchgate.net/publication/394421671_The_Landscape_of_Khawarnaq_From_Reality_to_Symbol_the_Evolution_of_Narratives_About_the_Landscape_of_the_Sassanid_Khawarnaq_Palace_in_Islamic_Period_Sources"},{"title":"Khawanaq - Wikidata","url":"https://www.wikidata.org/wiki/Q3814976"},{"title":"Al-Hira - Wikipedia","url":"https://en.wikipedia.org/wiki/Hira_(city)"},{"title":"The Palace of Khawarnaq: A Legendary Masterpiece in Arab History","url":"https://archup.net/the-palace-of-khawarnaq-a-legendary-masterpiece-in-arab-history/"},{"title":"Qalat Khawari Castle","url":"https://en.wikipedia.org/wiki/Qalat_Khawari_Castle"},{"title":"(PDF) The Landscape of Khawarnaq: From Reality to Symbol, the Evolution of Narratives About the Landscape of the Sassanid Khawarnaq Palace in Islamic Period Sources","url":"https://www.academia.edu/143126116/The_Landscape_of_Khawarnaq_From_Reality_to_Symbol_the_Evolution_of_Narratives_About_the_Landscape_of_the_Sassanid_Khawarnaq_Palace_in_Islamic_Period_Sources"}]

Based on the search results, I found the information you were looking for:

Khawarnaq was a medieval, pre-Islamic Arab castle built by the Lakhmids near their capital al-Hira. Regarding the etymology you asked about, Al-Asmaʿi speculated it was a Persian loanword into Arabic, ḵu(w)ran-qāh, meaning "place of eating and drinking".

However, it's worth noting that the etymology or origins of the name, Khawarnaq, is unresolved.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-14T03:17:11.815Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://en.wikipedia.org/wiki/Khawarnaq",
 "prompt": "What does the article say about the etymology of the name Khawarnaq — al-Asma'i's Persian derivation xu(w)ran-gāh 'place of eating and drinking', and any alternative proposals?"
}
```


### [2026-09-14T03:17:16.231Z] TOOL RESULT

```
# Etymology of Khawarnaq

According to the article, multiple scholars have proposed different etymological origins for the name:

**Al-Asmaʿi's Theory:** He suggested it derived from Persian _ḵu(w)ran-qāh_, meaning "place of eating and drinking."

**Alternative Proposals:**

- **Khalil ibn Ahmad** proposed an Arabic origin from _ḵerneq_, meaning "young hare" or "leveret"

- **Theodor Nöldeke** agreed with Persian origins, linking it to the Talmudic _aḵwarneqa_, meaning "pergola" or "summerhouse"

The article notes that "the etymology or origins of the name, Khawarnaq, is unresolved" and that most theories favor a Persian background, though no consensus exists among scholars.
```


## [2026-09-14T03:17:22.879Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/swan",
 "prompt": "Etymology of \"swan\": Proto-Germanic form and PIE root cited, and the \"singing bird\" sense."
}
```


## [2026-09-14T03:17:24.870Z] TOOL CALL #59: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AE%D9%88%D8%A7%D9%86%D8%AF%D9%86",
 "prompt": "Give the Persian etymology of خواندن (xāndan) 'to read, call, sing': Middle Persian, Proto-Iranian, Avestan, PIE root, and cited sources."
}
```


### [2026-09-14T03:17:27.070Z] TOOL RESULT

```
# Swan Etymology

The word "swan" originates from Old English and has a musical connection. According to etymonline, it comes from Proto-Germanic *swanaz, meaning "singer," which is "probably etymologically 'the singing bird.'"

The term traces back to the Proto-Indo-European root *swen-, meaning "to make sound." This linguistic heritage links the word to related terms like Old English "geswin" (melody) and "swinsian" (to make melody).

Historically, swans held cultural significance: "In classical mythology the bird was sacred to Apollo and to Venus." The compound term "swan-song" emerged from this tradition, while other related words developed over time, such as "swanherd" (swan tender) in the late 15th century and "swan-neck" (curved architectural elements) by the 1680s.
```


### [2026-09-14T03:17:32.039Z] TOOL RESULT

```
# Etymology of خواندن (xāndan)

Based on the Wiktionary entry, here's the etymological chain:

**Direct lineage:**
The word is "inherited from Proto-Iranian *hwanH- ('to call'), from Proto-Indo-Iranian *swanH-, from Proto-Indo-European *swenh₂- ('to sound')."

**Middle Persian:** Not explicitly mentioned in the provided content.

**Avestan:** Not cited in this source.

**PIE root:** *swenh₂- meaning "to sound"

**Cited source:** 
"Cheung, Johnny (2007), Etymological Dictionary of the Iranian Verb (Leiden Indo-European Etymological Dictionary Series; 2), Leiden, Boston: Brill, pages 144-5"

**Cognates provided:** The entry notes related words in Northern Kurdish (xwendin), Latin (sonō), and Sanskrit (svanati), all reflecting the common Indo-European sound-related root.

The semantic evolution traces from the meaning "to sound" through "to call" to the modern senses of "to read," "recite," and "sing."
```


## [2026-09-14T03:17:38.727Z] TOOL CALL #60: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%D8%A2%D8%AE%D9%88%D9%86%D8%AF\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/swenh%E2%82%82-\" \\\n \"https://en.wiktionary.org/wiki/%D8%AE%D9%88%D8%B1%D8%AF%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D8%AE%D9%88%D8%A7%D9%86%D8%AF%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D8%A2%D8%AE%D9%88%D8%B1\" \\\n \"https://www.etymonline.com/word/swallow\" \\\n \"https://www.etymonline.com/word/swan\" \\\n \"https://en.wikipedia.org/wiki/Khawarnaq\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 491, roots Swel 1 / Swen: verification of xordan, xandan, axur, axund, xavarnaq, swallow, swan\" 2>&1 | tail -2\ndone"
}
```


### [2026-09-14T03:17:42.295Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/2f166019c0b969c7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5e432a56897907fe.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f2a175c6a18dacab.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/fe89e69ae1f27aeb.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/939e4549f3f582ba.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2375844fde1437c6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a5fbed6f8a213b1f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e1f1993915d2d49a.txt
```


## [2026-09-14T03:17:57.092Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"urden 'essen\\|xurden\\|/urden\" HRN.txt | head -10; echo \"---\"; awk 'BEGIN{RS=\"\\f\"} NR==134' HRN.txt | head -50"
}
```


### [2026-09-14T03:17:58.146Z] TOOL RESULT

```
1448:gemessen, ender/iird, der/urd, ender/urden ^) (Sahn.
---
- 112 —
aw. Iwar-; phlv. vergl. ;K?/r[pa;Y7// hez\^\ /var[varätt',
ai. svar.
kurd. /or, hilr[efaü; af;'. mar, nmar (Darmesteter>
Chants pop. XXXII); oss. d. yor, t. /Tir (306); si/n.
yer, yiv.
506. x^irsed 'Sonne'.
aw. hvare./sa^tem ^strahlende Sonne'; phlv. ;^"'arset
bezw. ;^?/r8rf, auch y^'arhsel (vergl. Hörn, Mitteilungen,
Heft IV, 34 No. 31).
507. y^itrden (FirdüsT, AM.: p^^'t'/v/ew ^)) essen, trinken',
/uräk, /^(lt\, /unl'i, /uris,
Kää. /ürfdri; /ürest,
ap. vergl. fxa()Tt\y6oa dy&Qomofdyog Ktesias; aw.
i/^X^'a)'-, yntraiti *essen'; phlv. /^'arfan, /^'ar(i)siij
yyartar, y^är etc., bezw. yurtan, arm. LW. yortlk
*Essen, Speise* (d. i. phlv. yurtik, AV.).
kurd. ymnn^ y^ärin essen ; af;'. yöral; oss. d. xvärun,
t. yärin (308); bei. varag, n. varay (404); si/n. minj.
ydr-am, sar. yör-am, sangl. y^är-afn.
Die l^y^m*' bedeutet sowohl essen' als auch 'trinken',
vergl. aw. äfs anaiui^.y^ared^a' (vd. 6, 31); ai. sürä-,
aw. hurä'^), lit. .wla (*Birkensaft') werden aber besser
zu i/^sav' 'auspressen' gestellt, woran Fick, Wörter-
buch^ noch zweifelt.
np. yurde, ynrd 'klein', phlv. yiirtak^ arm. LW. yortak
'zerbrochen, zerschlagen* kann nicht hierher gehören,
da es auf u reimt (Vis und RämTn S. 51, Vers 12,
V
Sahn. I, 179 Vers 905) und auch AM. u spricht; auch
mit aw. y^ara- 'W^unde* (de Lagarde) wird es schwer-
lich zusammengestellt werden können. Nöldeke
(mündliche Mitteilung), vergleicht lat. curttts 'kurz',
das zur [/^qert- 'schneiden' gehört. Die Aspiration im
Anlaut wäre dann neupersisch, wie öfter {yiramidev,
yerceng^ yired u. a. m.).
^) So auch immer in der Poesie.
*) EinmnI im Pehlevivondidäd, aber wohl nur umsohreibend, hur,
7d. 14 (72). - Zu aw. Inträ- vergl. Bartholomae, ZDMG. 37, 459.
```


## [2026-09-14T03:18:11.226Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"Stall'\" HRN.txt | head -10; echo \"---\"; awk 'BEGIN{RS=\"\\f\"} NR==26' HRN.txt | head -40"
}
```


### [2026-09-14T03:18:12.231Z] TOOL RESULT

```
2935:aw. *2)airivära?ia-, vergl. pairi.vära- 'Wall*, 'Stall'
10138:28. aspastän 'Pferdestall'; arm. LW. aspastan.
10139:aw. aspöMäna- Pferdestall'; skr. agvasthamt'.
---
— 4 -
8. üj^xir *Stair.
aw. avöx^'arena- *Stall, Futterplatz' ; phlv. av;(ur oder
avx^'ar (Darmesteter, Et. ir. II, 136), arm. LW. ayor,
vergl. Talmud LW. •imnx (de Lagard e, Semitica
I 42) 'Stallmeister' (arm. LW. axorapet, a/orapan), —
Anders Geldner KZ. 28, 186.
9. ä(fer *Feuer', ader,
ap. vergl. Äd^rina-, Ä&riyädiya- ; aw. äfar- 'Feuer ;
phlv. ätiir (häufig auch auf Gemmen), schon ad^o' ge-
sprochen, vergl. Hörn, Mittigen Heft IV, 32 (daneben
arm. LW. atr-).
kurd. aür, a7\ er; af/. ör; oss. arf (36); bei. äs (16);
minj. yür; arm. vergl. airem verbrennen, anzünden*
(H. No. 18).
10. ärazis 'Guttat' (unbelegt).
vgl. aw. rä-^ayfm^/ 'sie ordnen', rä^a-, räzar- 'Richt-
schnur; schon im Pehlevl verloren gegangen^). Also
zu {/reg- 'richten, aufrichten. Vergl. Hübsch mann
zu oss. ardzin 'richten' (28). Die Bedeutung des neu-
persischen Wortes lässt sich nicht weiter zurück ver-
folgen; es kam mir nur darauf an, dasselbe an seine
noch sonst vorkommenden, aber bereits im Pehlevl
verschwundenen Verwandten anzuschliessen.
Dazu efröiZiden 'ordnen, das aber ebenfalls unbelegt
ist; heraz 'Schmuck', beräztdeM (No. 193) können wegen
phlv. hräzisak, hräzisakth nicht zu [^räz- gestellt werden,
zu der sie sonst sehr gut passen würden {upa + räz).
äöm s. äyin (No. 61).
11. är asten 'schmücken', Praes. üLräy-em^ ärayis,
ap. l/^räd' in rästa- Vichtig'; aw. [^rad- zurecht
machen', radaiti; phlv. ärästan, äray(i)sn^); ai. [/^rädh-,
rädhati 'zu Stande bringen'.
oss. arazi 'schmückt, kleidet', aräfif geschmückt' (28).
Vergl. Bartholomae, BB. 10, 269. Die falsche, laut-
1) Im ÄYestakommentar stehen immer Formen von ärästan^
vir äst an,
2) Vgl. auch phlv. vlrästav^ viräyOßn ; hamrästcni.
```


## [2026-09-14T03:18:40.434Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== NYB xwar/xwan ===\"; grep -n \"xvartan\\|xvar-\\|xvāntan\\|xvān-\\|hwltn\\|KLYTWNtn\" NYB_vol2_glossary.txt | head -12; echo \"=== SYN eat ===\"; grep -n -o \"5\\.11 EAT.\\{0,200\\}\" SYN.txt | head -3; grep -n -o \"swelgan.\\{0,200\\}\" SYN.txt | head -3; echo \"=== SYN sound ===\"; grep -n -o \"sonus.\\{0,150\\}\" SYN.txt | head -3"
}
```


### [2026-09-14T03:18:41.534Z] TOOL RESULT

```
=== NYB xwar/xwan ===
4318:xuan-sand [hwnsnd] contented, happy with what one possesses, ‘‘not jealous of other people's greater prosperity" (cf FrP 30), magnanimous 1312, 3725, 661. — MPrth hwnsnd-yft (S); MPrs hwnsnd (BBB). From z"an- = xtar- ‘sun’ (v. s. v. axvar-xšēt) and (Av. 1559) sand- ‘to be, become visible’, v. s. v. sahistan and pas- sand, thus ‘having a sunny look’, ‘of sunny disposition’ (Benveniste). Also xtar-sand = Paz. NP.
4352:x"artan [hwltn'; ŠTHn-tn'] 1. to eat, passim; be ~ 102. 82%, frac ~ 60° to de- vour, consume; to earn one’s livelihood 6920.24. 8917. — 9. to drink 14?! ete. ; sēkand (q. v.) ~ pat to swear an oath by 2118.23, 2225, 2322, — 1920 ŠTHn-yt': read "wlyt' and v. avar and honeh. — Av. (1865 sq.) z"ar-; MPrth wzr- and xwr-; MPrs zwr-; Paz. NP xvar-. — V. x"arg, xYarisn, xYā- ritan, xudrenitan and the next w.
4354:x'ar-xšēt [hwlhšyt'] 869. 872-15, 884-8, 8914, 903, elsewhere xvar-šēt [hwlšyt'] the sun. — Av. (1848 sq.) hvaro.xšaēta- from hvar-, x"an- (1847 sq.) ‘the sun’ + (541) ašaēta- 'splendent'; MPrthPrs xwrxšyd; Paz. xtarsed, xuršed; NP xuaršed, xuarščid.
=== SYN eat ===
8318:5.11 EAT sate th 20° tpayov Goths malian itan un ager (ésti) iy 1 .
8348:swelgan ‘swal- low’, NE swallow, ete. Walde-P. 2.530. Barth. 1865f. For ‘eat? fr. ‘swallow’, cf. Grk. B:Bpdcxw, above, 2.
=== SYN sound ===
26213:sonus
26260:sonus ‘sound’ (> It. swono, Fr. son, OSp. sueno, Rum. sun; Sp. sonido new deriv.; Rum. swnet fr. Lat. sonitus), with vb. sonere, sonare (> It. suonare, Fr.
26273:sonus. Pedersen 1.195, 375. Walde-P. 2.627.
```


## [2026-09-14T03:18:48.427Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '8338,8352p' SYN.txt; echo \"=== SOUND ===\"; sed -n '26255,26278p' SYN.txt"
}
```


### [2026-09-14T03:18:48.501Z] TOOL RESULT

```
W. bwyita, fr. bwyd ‘food’ (5.12).
Br. dibri, MBr. dibriff, OBr. sb. diprim ‘food’, Corn. dibry., prob. fr. a cpd. *di-prim-: NIr. creimim ‘gnaw, chew’ (Ir. vbl. n. creim, K. Meyer, Contrib. 511). Henry 95. Loth, Vocab. vieux-breton 105. (Otherwise, but to be rejected, Pedersen 1.111).
5. Goth. matjan (more common than titan), fr. mats ‘food’ (5.12).
Dan. spise, fr. sb. spise, loanword fr. MLG spise ‘food’ (5.12). As the polite term this has displaced the old ede (above, 1), as NHG speisen has en- croached on essen, but without displac- ing it (Kretschmer, Wortgeogr. 469).
6. Lith. valgyti (displacing és¢; 1), fr. valgis ‘food, meal’ (5.12),
7. Russ. kugat’, polite term ‘partake of’ food or drink : ChSl. = kuszij ‘taste? etc. (15.31). :
8. Skt. ag- ‘eat, devour’, et: ; Walde-P. 1.112, pe!
Skt. bhuj- ‘enjoy’, esp. ‘enjoy food eat’, prob. : Lat. fungi ‘be engaged in, perform’. Walde-H. 1.566 (with Tefs.)
Skt. ghas-, Av. gah- ‘eat, devour’ (Av. only of evil beings), etym.? Walde- P. 1.640. Barth. 517.
Skt. khad- ‘chew’, colloq. for ‘eat’ and in MIndic mostly displacing ad-. Wack- ernagel-Debrunner, KZ 67.158.
Av. x"ar- ‘consume, eat or drink’ (ef. NPers. zurdan, the reg. word for ‘eat’) points to a root *swer- or *swel-, and under the latter head may be connected with the Gmc. group, OE swelgan ‘swal- low’, NE swallow, ete. Walde-P. 2.530. Barth. 1865f. For ‘eat? fr. ‘swallow’, cf. Grk. B:Bpdcxw, above, 2.
» ab OVe,
?
5.12 FOOD Grk.  zpod4, Bpdya, w57, Goth. mats, fodeins Lith. _valgis, maistas cirla ON matr, fda, al, vist Lett. bariba NG Tpogh, dayt Dan. mad, féde, spise ChSl. pi8ta, jadt, braStno, Lat. —_cibus, sca, penus, etc. Sw. mat, féda, spis kritma It. cibo, mangiare, vilto OE mele, foda, wist, feorm SCr. _hrana, jelo Fr. nourriture, aliment ME mete, fode Boh.  jidlo, pokrm, potrava Sp. alimento, comida NE food Pol.  jadlo, pokarm, Rum. hrand, mincare Du. _voedsel, spijs potrawa Ir. biad, tiare OHG ‘muos, maz, spisa, az, Russ. pista, jastva Nir. _ biadh wist Skt. anna-, pitu- W. bwyd MHG muos, spise, maz, az Ay. z’arada-, pitu- Br. boed NHG speise, essen, nah- rung, kost
Many of the words listed cover ‘food’ for man or beast. Words that are used only of food for animals (‘fodder’) are not included in the list, though several of these belong to the same cognate groups and are mentioned in the discus- sion.
=== SOUND ===
word for ‘sound’ (axo} Wddov parallel to yedots xvpod, Aristot., De anim. 2.6), prob. of imitative origin.
Grk. 4x7 ‘sound’ (usual word in Hom.), later #xo0s as NG (lit.) : Lat. vagire ‘cry, squall’, with different exten- sions of an imitative *wa-. Walde-P. 1.215. Ernout-M. 1070.
Grk. xpé7os ‘a rattling or clashing sound’, in NG the usual word for any inarticulate sound, perh. : OF hrindan ‘strike, hit’, ChSl. krotitc ‘tame’, etc. Walde-P. 1.484.
3. Lat. audire ‘hear’ (> It. udire, Sp. ofr, Rum. auzi; Fr. ouir now nearly obs.), sb. auditus ‘hearing’ (> It. udito, Fr. ouie, Sp. ofdo; Rum. auz, back-for- mation fr. vb.), by itself most simply taken as fr. *aus-dh- (cf. auscultdre) : Lat. auris, Grk. ods, Lith. ausis, etc. ‘ear’ (4.22), but perh. better (to help explain the difficult cpd. oboedire) fr. *qwis-dh- : Grk. alcOavouar ‘perceive’, Skt. avis ‘openly’, etc. (15.11), belonging ultimately to the same group. Walde-P. 1.17f. Walde-H. 1.80. Ernout-M. 86.
Lat. auscultare ‘listen’, VLat. ascul- tare (> the Romance forms listed), epd. of *aus- : Lat. auris ‘ear’, etc., second part prob. fr. *cultos by metath. fr. *clutos : UE *kleu- (above, 1). Walde- H. 1.86f. REW 802.
Lat. sonus ‘sound’ (> It. swono, Fr. son, OSp. sueno, Rum. sun; Sp. sonido new deriv.; Rum. swnet fr. Lat. sonitus), with vb. sonere, sonare (> It. suonare, Fr. sonner, Sp. sonar, Rum. suna) : Skt. svan- ‘to sound, make a noise’, sb. svana-, svana- ‘sound’, etc. Walde-P. 2.524f. Ernout-M. 956 f.
Fr. entendre ‘hear’, fr. Lat. intendere ‘stretch out, direct one’s attention to’, whence ‘understand’ (as It. intendere, Sp. entender, and still in part Fr. en- tendre), then ‘hear’, replacing the old ouir. REW 4483.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
|
Digitized by Arya Samaj Foundation Chennai and eGangotri
1038 SELECTED INDO-EUROPEAN SYNONYMS
It. sentire ‘perceive by the senses’ (15.11) is used also esp. for ‘hear’, tend- ing to replace udire in pop. speech.
4. Celtic words for ‘hear’ and W., Br. words for ‘hearing’, above, 1.
Ir. con-tuasi, in-tuasi (both 8sg.), MIr. eitsim, NIr. @istim ‘listen’, with vbl. n. MIr. @ttsecht, NIr. @isteacht ‘hearing’, epds. of -tois-, -tuais- (only in epds.), fr. 6 ‘still, silent’, as also W. gwrando ‘listen’ (gwr-an-do, cf. MW an-daw ‘listen’), fr. taw ‘silence’ : Skt. tus- ‘be content’, tasnim ‘silently’, etc. For the converse semantic relation, cf. ON hijad, Dan. lyd ‘sound’ and ‘silence’, etc. (Falk- Torp 668). Walde-P. 1.714f. Pedersen 2.651 f.
Br. selaou ‘listen’, MBr. sezlou, Corn. golsowas, goslow, etym.? Pedersen 1.489. Henry 245.
Ir. fuaim, NIr. fuaim ‘sound’, etym.? Walde-P. 1.215 (vs. Stokes 260).
Ir. fogur, NIr. foghar ‘sound’ (esp. of the voice), epd. fo-gur : gairim ‘cry out, call’, gair, W. gawr ‘a cry’, Grk. Yiipus ‘voice’, etc. Walde-P. 1.587. Peder- sen 2.536.
Ir., NIv. glor, perh. same word as gloir ‘glory’ (fr. Lat. gloria), with devel- opment through ‘noisy celebration’ to ‘noise, sound’. Macbain 198.
W. sain ‘sound’, back-formation to vb. seinio, deriv. of son (arch.) = Br. son fr. Lat. sonus. Pedersen 1.195, 375. Walde-P. 2.627.
5. Goth. hausjan, OB hyran, etc., gen- eral Gme. word for ‘hear’, prob. : Grk. dxobw ‘hear’, xoéw ‘perceive’, etc. See above, 2. Hence also for ‘listen’ OF heorenian, herenian, ME herken, NE harken, hark, OHG horechen, MHG horchen, NHG horchen. Hence also for ‘hearing’ ON heyrn, Dan. horelse, Sw. hérsel, ME hering, NE hearing, OHG gihorida (also gihdrnesst Tat.), MHG gehoerde, NHG gehér, Du. gehoor,
Goth. hiiwma, OF hlyst ‘hearing’, ang Gme. words for ‘listen’ and ‘sound? ¢ above, 1. 3
OE sweg peur * swogan ‘roar’, Goth, ga-swogjan ‘groan’, prob. Lith, ‘resound, ring’, Lett. svadzat ‘Tatt of imitative orig. Walde-P. 1,215
OE hlyn(n) ‘sound, noise’ : hlimma ‘make a sound’, Grk. xadtw, Lat. cla- mare ‘call’, etc. Walde-P. 1.444,
ME soun, NE sound, fr. Anglo-Fy. sia = OFr. son, fr. Lat. sonus (above,
```


## [2026-09-14T03:18:56.665Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '1,120p' tools/verify_check.py"
}
```


### [2026-09-14T03:18:56.721Z] TOOL RESULT

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


## [2026-09-14T03:19:52.681Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for w in \"SWALLOW\" \"SWAN,\" \"SOUND (1)\" \"SONIC\"; do echo \"=== $w ===\"; grep -n -o \"$w.\\{0,300\\}\" SKT.txt | head -2; done"
}
```


### [2026-09-14T03:19:53.744Z] TOOL RESULT

```
=== SWALLOW ===
18935:SWALLOW.
=== SWAN, ===
22739:SWAN,  to  resound,  sound. 464.  y^SWAP(.V'SWAB),toslecp» slumber.
=== SOUND (1) ===
=== SONIC ===
```


## [2026-09-14T03:19:57.208Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '18925,18945p' SKT.txt; echo \"=== sound ===\"; grep -n -o \"Sound (1).\\{0,320\\}\\|Sound, a noise.\\{0,320\\}\" SKT.txt | head -3; grep -n -o \"Swan, a bird.\\{0,300\\}\\|Swan\\. (E\\.).\\{0,300\\}\" SKT.txt | head -3"
}
```


### [2026-09-14T03:19:58.291Z] TOOL RESULT

```
Burround ,  see  p.  407,  coL  i.
Surtout;  see  Total.
Burvoillonce ;  sec  VigQ.
Survey;  ieeViaion.
Survive ;  see  Victuala.
BiJs  ,  prefix  \  see  Sub-.
SuBceptible;  see  Oapaoioua.
Buapoot;  sec  Bpeciea.
ci/l
i
SWALLOW.
BuBpend ;  see  Pendjsav
SuBpicion ;  see  Speciae.
Sustain :  see  Tenable.
Sutler,  one  who  sells  proi camp.     (Do.  >      Du.     soettlaaf^ usually   tfieUUtar;    O.    Du. scullion,  a  sutler,  or  a  victnallet/  1 Orig.  a  scqIIIod.  dxurl^,  cnenialj dirty  work;  formed  wilh  sufliji •^r)   from    seefelen^   *  to   sullic.^ Cognate    with     Low    G.    /wAJ sudU,  G.  tudeln,  to  solly,  danb.^ are  frequentative  forms,  urilh •I- ;    from    Swed.   suddd^   to  djul soil.     Allietl    to  Icel.  suJM» cooking,  driirling  rain,  suJdc dank,  s^,  broth  in  which  me sodden;    all    from    leal,  tji Further  allied  to  £■  tudi,  and Seothe,  q.  t.
Buture,  a  seam.  (F.^L.) L.  r«/«n2.  — L.  nttus,  pp.  of  j see  Sew.
Suttee.    (SkO    Skt.    as//. virtuous  wife,  a  term    ap|.lird who  immolates  bcrxlf  on  the of  her  husband;    hence    0 burning  of  a  widow.    Skt. fem.  oT  sant,  being,  existing, virtuous;    pres.  pt  of  at,  to Sec  Sooth.
Suzerain;  sec  Bub-.
Bwabbor.  (Du.)    OldrrlhaaJ —  Du.  twabiser,  'a  swabber,  the a  ship:*    ScwcL    Cf.   Du. drudge.  +  Swed.  svab,  a  fiie-l to    swab ;     Dan.    stsiife, schzoabber^  a    swabber.     CC rvahba^  to  splaiih  about.     Allil Swoop.  Sweep.
Swaddle ;  see  Swath.
Bwagffer :  see  8 vsy.
=== sound ===
```


## [2026-09-14T03:20:05.525Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -o \"swan[,.] .\\{0,200\\}\" WEB_vol1.txt WEB_vol2.txt 2>/dev/null | head -4; echo \"===\"; ls WEB*; grep -n -o \"swelgan.\\{0,160\\}\" WEB_vol*.txt FSD_vol*.txt 2>/dev/null | head -4"
}
```


### [2026-09-14T03:20:06.659Z] TOOL RESULT

```
36091:swan, cd/burg, n. {named from Coburg, in Germany. a fabric for women's wear, made of worste: and silk or cotton. cob/wall, ‘x. a wall made of unburned clay, mixed with straw. cob/web, n. [ME. copweb; cop, a
43515:swan. pee AUCE cose, v.i.; cosed, pt. ; i pepo pt., pp.; cosing, ppr. Same as
48190:swan, from cygnus, a swan.] in botany, curved to resemble a swan's neck.
58590:swan. 2 2. soft, fine hair. 3 The frst down begins to shade his face.
===
WEB_vol1.txt
FSD_vol4.txt:28499:swelgan, swallow  1
WEB_vol1.txt:84936:swelgan, e in poult Jany of a f the genus Senecio, ers, as the golden
FSD_vol2.txt:37590:swelgan,  swallow.]  gronnd'sweUt.— bal'sam>ground"sel,  n.  A   tufted  per- ennial herb  {Senedobalsamilx)  with  slen- der stems,  oblong  radical  leaves,  and yel
```


## [2026-09-14T03:27:04.229Z] TOOL CALL #69: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-491.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW_XORDAN = \"https://en.wiktionary.org/wiki/%D8%AE%D9%88%D8%B1%D8%AF%D9%86\"\nW_XANDAN = \"https://en.wiktionary.org/wiki/%D8%AE%D9%88%D8%A7%D9%86%D8%AF%D9%86\"\nW_AXUR   = \"https://en.wiktionary.org/wiki/%D8%A2%D8%AE%D9%88%D8%B1\"\nW_AXUND  = \"https://en.wiktionary.org/wiki/%D8%A2%D8%AE%D9%88%D9%86%D8%AF\"\nW_SWENH2 = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/swenh%E2%82%82-\"\nE_SWALLOW= \"https://www.etymonline.com/word/swallow\"\nE_SWAN   = \"https://www.etymonline.com/word/swan\"\nWP_KHAW  = \"https://en.wikipedia.org/wiki/Khawarnaq\"\n\ndoc = {\n \"pdf_page\": 491,\n \"book_page\": 461,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-13\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Swel 1\",\n   \"verdict\": \"plausible\",\n   \"modern_form\": \"PIE *swel- (*swel-k-) 'to swallow, eat, drink' (Pokorny 1045 '1. su̯el-(k-)'; Watkins/AHD swel-1 'to eat, drink')\",\n   \"note\": \"The root name, the language label and the gloss are all as the standard handbooks print them: Pokorny IEW p.1045 heads the entry '1. su̯el-(k-) „schlingen, essen, trinken“?' and immediately adds '?Nur iran. und germ.?' — the whole root rests on exactly two witnesses, Av. xʷar- and Gmc. *swelgan/*swelhan. Watkins (AHD IE roots, 1985 ed. p.87) keeps it as 'swel-1. To eat, drink' and explicitly cites 'Iranian *khvāra- (attested in Avestan), to eat'. Buck (Selected Synonyms 5.11) is more cautious: Av. xʷar- 'points to a root *swer- or *swel-, and under the latter head MAY be connected with the Gmc. group'. Cheung, Etymological Dictionary of the Iranian Verb (2007) 147-148, rejects the equation outright under *huar1: 'There is probably no need to reconstruct an IE root *suel- „verschlucken (vel sim.)“, as done in IEW', and prints 'IE COGNATES: —'. Hence 'plausible', not 'confirmed': the root is real in Pokorny/Watkins/Walde-Pokorny but the Irano-Germanic equation that is its only content is abandoned by the current standard work on Iranian verbs.\",\n   \"note_fa\": \"ریشهٔ بازسازی‌شدهٔ هندواروپایی آغازین *swel- «فروبردن، خوردن، آشامیدن» در فرهنگ پوکورنی (ص ۱۰۴۵) با همین معنا آمده است، اما خود پوکورنی در برابر آن علامت پرسش گذاشته و افزوده است «تنها ایرانی و ژرمنی؟»، زیرا این ریشه فقط بر دو گواه استوار است: xʷar- اوستایی و *swelgan ژرمنی. واتکینز (پیوست ریشه‌های هندواروپایی فرهنگ American Heritage) آن را با همین معنا نگه داشته و صریحاً صورت ایرانی *xʷāra- را ذیل آن آورده است. در برابر، چونگ در فرهنگ ریشه‌شناختی فعل ایرانی (۲۰۰۷، ص ۱۴۷ـ۱۴۸) این برابرنهاد را رد می‌کند و می‌نویسد بازسازی ریشهٔ هندواروپایی *suel- ضرورتی ندارد و برای ایرانی آغازین *Hwar- هیچ هم‌ریشهٔ هندواروپایی نمی‌شناسد. بنابراین ادعای نورایی «با احتیاط پذیرفتنی است»: نام و معنای ریشه درست نقل شده، ولی پیوند ایرانی و ژرمنی امروزه مورد تردید جدی است.\",\n   \"sources\": [W_XORDAN, E_SWALLOW],\n   \"ref_check\": [\n    {\"ref\": \"POK:1045\", \"status\": \"supports\", \"note\": \"Pokorny IEW p.1045 (local POK_03.txt, leaf 288): '1. su̥el-(k-) „schlingen, essen, trinken“? Nur iran. und germ.? Av. xʷar- „genießen, verzehren“; engl. swill … von einer Erweiterung suelk-: ahd. swelhan und swelgan „verschlucken, trinken“, ags. swelgan …' — root, gloss and both branches exactly as Nourai draws them, including the author's own question mark.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. II p.530 (WLD_Bd2_pages.txt leaf 535)\", \"stance\": \"supports\", \"note\": \"'1. suel- „Schlingen, essen, trinken“? Fick I4 341 vergleicht av. xʷar- „genießen, verzehren, essen, trinken“ mit flgd. germ. Gruppe … engl. swill' — the same two-branch equation, again with a question mark.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. swel-1 (AHD_watkins1985.txt line 1044)\", \"stance\": \"supports\", \"note\": \"'swel-1, To eat, drink. 1. Perhaps Germanic *swil- … SWILL. 2. Extended form *swelk- in Germanic *swelgan, *swelhan in Old English swelgan, to swallow: SWALLOW1 … 3. Iranian *khvāra- (attested in Avestan), to eat … [Pok. 1. suel(k)- 1045.]'\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 5.11 EAT (SYN.txt line 8348)\", \"stance\": \"partial\", \"note\": \"'Av. xʷar- “consume, eat or drink” (cf. NPers. xurdan …) points to a root *swer- or *swel-, and under the latter head may be connected with the Gmc. group, OE swelgan “swallow” … Walde-P. 2.530. Barth. 1865f.' — 'may be', not an assertion.\"},\n    {\"src\": \"CHEUNG\", \"where\": \"EDIV 2007 pp.147-148 s.v. *huar1 (CHEUNG.txt lines 10307-10380)\", \"stance\": \"contradicts\", \"note\": \"'◊ There is probably no need to reconstruct an IE root *suel- „verschlucken (vel sim.)“, as done in IEW, l.c., and LIV, l.c. … *IE COGNATES: —'. Cheung derives NP xurdan only back to PIr. *huar- and leaves its further origin open.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Avestan\",\n     \"words\": \"xvar 2, xwar; avô-xvarena\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"Both Avestan items are genuine. (1) Younger Av. xʷar- 'to consume, eat, drink' (pres. xʷaraiti Y 9.16, V 2.26; Bartholomae, Altiran. Wb. cols. 1865ff.), with the derivatives a-xʷar- 'getting no food' (V 13.28), kərəfš.xʷar- 'corpse-eating' (BRT.txt lines 7208, 9561) that guarantee the stem; Nourai's '2' merely separates it from xʷar-/hvar- 'sun' and xʷara- 'wound'. (2) Younger Av. avō.xʷarəna- n., attested Y 2.16 and Y 7.16, which Bartholomae glosses 'Tränke' (watering trough) with the note 'Eig. (als Adj.) ‚Wässer(?)-genuss bietend‘ … Pü.: āp xʷar' — i.e. the Pahlavi version renders it 'āp-xwar'. Horn, Grundriss no.8 (p.4) glosses the same word 'Stall, Futterplatz', which is precisely Nourai's 'animal shelter for drinking and eating', and his cross-reference ☞ Ab 1 ('water') reflects Bartholomae's/Horn's first element. What is uncertain is not the words but the arrow from the root: the descent of Iranian *huar- from a PIE *swel- is accepted by Pokorny, Walde-Pokorny and Watkins but denied by Cheung (2007) and by Wiktionary after him ('further origin unknown, with no obvious Indo-European cognates outside of Iranian'). Formally *sw- > Ir. *hw- > Av. xʷ- is regular (cf. Av. xʷahřa- : Skt. svásar- 'sister'), so the phonology is no obstacle; the doubt is purely about whether the Germanic group belongs with it.\",\n     \"derivation_fa\": \"هر دو واژهٔ اوستایی واقعی‌اند: xʷar- «خوردن، آشامیدن» (مضارع xʷaraiti در یسنا ۹٫۱۶ و وندیداد ۲٫۲۶؛ بارتولومه، ستون ۱۸۶۵ به بعد) که ترکیب‌هایی چون a-xʷar- «بی‌خوراک» و kərəfš.xʷar- «مردارخوار» آن را تأیید می‌کند؛ و avō.xʷarəna- (یسنا ۲٫۱۶ و ۷٫۱۶) که بارتولومه آن را «آبشخور» معنا کرده و یادآور شده که ترجمهٔ پهلوی‌اش «āp-xwar» است، و هُرن (بند ۸، ص ۴) آن را «اصطبل، جای علف» گرفته است؛ همین معنای هُرن است که نورایی نقل کرده و ارجاعش به ریشهٔ «آب» نیز از همین‌جاست. آنچه تردیدآمیز است خودِ واژه‌ها نیست، بلکه پیوند آن با ریشهٔ هندواروپایی است: تبدیل *sw- هندواروپایی به hw- ایرانی و سپس xʷ- اوستایی قاعده‌مند است (قس. xʷaŋhar- «خواهر»)، اما چونگ (۲۰۰۷) ایرانی آغازین *Hwar- را بی‌هم‌ریشهٔ هندواروپایی می‌داند. پس ادعای نورایی دربارهٔ واژه‌ها درست و دربارهٔ ریشه با احتیاط پذیرفتنی است.\",\n     \"sources\": [W_XORDAN, W_AXUR],\n     \"ref_check\": [\n      {\"ref\": \"POK:1045\", \"status\": \"supports\", \"note\": \"POK_03.txt leaf 288 (p.1045): 'Av. xʷar- „genießen, verzehren“' stands as the Iranian witness of the root, exactly the arrow root→Avestan that Nourai draws.\"},\n      {\"ref\": \"AEF:10\", \"status\": \"not_checked\", \"note\": \"No copy of Khaleqi Motlaq's Asas-e Eshteqaq-e Farsi on disk or online (refs_online.json gives only an OpenLibrary catalogue record). AEF is, however, the Persian translation of Horn's Grundriss, and Horn's own no.8 (p.4, HRN.txt leaf 26) reads 'āxur ‚Stall‘. aw. avō-xʷarena- ‚Stall, Futterplatz‘; phlv. avxur oder avxʷar' — i.e. the cited page almost certainly is this entry, and it supports the node word for word.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"Altiran. Wb., s.v. avō.xʷarəna- (BRT.txt line 5197) and s.vv. a-xʷar-, kərəfš.xʷar- (lines 7208, 9561)\", \"stance\": \"supports\", \"note\": \"'j. avō.xʷarəna- n. ‚Tränke‘: gaeyaoitišca mašyanhəsca °nāsca Y. 2.16; … Y. 7.16' with footnote 'Eig. (als Adj.) ‚Wässer(?)…genuss bietend‘. Vgl. GDN. KZ. 28.186 (gegen Hbm. PSt. 5). — Pü.: āp xʷar'.\"},\n      {\"src\": \"HRN\", \"where\": \"Grundriss no.8, p.4 (HRN.txt leaf 26)\", \"stance\": \"supports\", \"note\": \"'āxur ‚Stall‘. aw. avō-xʷarena- ‚Stall, Futterplatz‘; phlv. avxur oder avxʷar (Darmesteter, Et. ir. II, 136), arm. LW. axoṛ … — Anders Geldner KZ. 28, 186.' This is Nourai's source for both the Avestan form and its gloss.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"EDIV 2007 p.147 s.v. *huar1\", \"stance\": \"partial\", \"note\": \"'*AVESTAN: YAv. xʷar- “to consume, eat” … Pres. them.: IND. 3sg. YAv. xʷaraiti' — the Avestan verb is confirmed, but Cheung gives it no IE ancestry.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. II p.530\", \"stance\": \"supports\", \"note\": \"av. xʷar- 'genießen, verzehren, essen, trinken' cited as the Iranian member of suel-.\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Pahlavi\",\n     \"words\": \"xvartan; xvariš; av-xur\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"xvartan = MP xwardan, xwar- [heterogram OŠTEN-tn', phonetic hwltn'] 'to eat, consume' (MacKenzie, CPD p.96; Nyberg, Manual II p.219: 'xʷartan [hwltn'; ŠTHn-tn'] 1. to eat … 2. to drink … Av. (1865 sq.) xʷar-'), the regular continuant of Av. xʷar-, with the Iranian past stem in -t- (*hwar-ta-). xvariš = MP xwarišn 'food' (MacKenzie p.96 's.v. xwardan, ~išn: food'), the ordinary MP verbal noun in -išn; Nourai's gloss 'stew' is the later New Persian narrowing, not the Pahlavi sense. 'av-xur ‚stable‘' is the weak item: it is Horn's 1893 reading of the Pahlavi gloss of Av. avō.xʷarəna- ('phlv. avxur oder avxʷar', Grundriss no.8). Hübschmann, Persische Studien pp.5-6, corrected this two years later — 'phl. āp-xʷar (so, nicht avxʷar ist zunächst zu lesen!)' — and MacKenzie's dictionary knows only 'āxwarr [ʾh wl | N āxur] manger, stable' with the compound āxwarr-sālār 'head groom'. So the Pahlavi word for 'stable' is āxwarr, and 'av-xur' is a superseded nineteenth-century reading that Nourai took over from Horn/AEF, not a form any modern Pahlavi dictionary prints.\",\n     \"derivation_fa\": \"«xvartan» همان xwardan فارسی میانه است (نویسهٔ هزوارشی OŠTEN-tn'، آوانگاشت hwltn')، که مکنزی (ص ۹۶) و نیبرگ (جلد دوم، ص ۲۱۹) آن را «خوردن، آشامیدن» و بازماندهٔ xʷar- اوستایی دانسته‌اند؛ ستاک گذشتهٔ ایرانی با پسوند -ta- ساخته شده است. «xvariš» همان xwarišn پهلوی است، اسم مصدر با پسوند -išn به معنی «خوراک»؛ معنای «خورش» به‌مثابهٔ خوراکِ همراه نان و برنج تحولی فارسی نو است. اما «av-xur» به معنی «اصطبل» صورتی است که هُرن در ۱۸۹۳ (بند ۸) برای برگردان پهلویِ avō.xʷarəna- پیشنهاد کرده بود؛ هوبشمان دو سال بعد در «مطالعات فارسی» (ص ۵ـ۶) آن را تصحیح کرد و نوشت باید āp-xʷar خواند نه avxʷar، و فرهنگ مکنزی تنها āxwarr «آخور، اصطبل» را می‌شناسد. پس این بخش از نمودار بر خوانشی کهنه استوار است.\",\n     \"sources\": [W_AXUR, W_XORDAN],\n     \"ref_check\": [\n      {\"ref\": \"MON:1455\", \"status\": \"supports\", \"note\": \"The content is Mo'in's: his Farhang gives خورش '[= خورشت] خوردن؛ خوردنی، طعام، غذا؛ آنچه با نان یا برنج خورند؛ قاتق' and آخُر 'جایگاهی از گِل و سنگ … که برای علف و کاه و جو خوردن چهارپایان سازند؛ معلف، طویله، اصطبل' (MON_part1.txt). The page number itself could not be confirmed: the local copy is the two-volume abridgement, which carries no printed pagination in the OCR.\"},\n      {\"ref\": \"BQT:788\", \"status\": \"supports\", \"note\": \"Borhan-e Qate' vol.2, leaf 247 of BQT_v2_pages.txt = printed p.788 (offset printed = leaf+541, checked against the running head ۷۸۷ on leaf 246). Mo'in's etymological footnote there reads: 'خوردن - بر وزن بردن، اوستا hvar-, hvarə- (اکل)، پهلوی xvartan، ارمنی xortik …' and the neighbouring footnote gives 'پهلوی xvarišn' — Nourai's two Pahlavi forms verbatim.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD pp.96 and 14 (PHD.txt lines 663, 223)\", \"stance\": \"partial\", \"note\": \"'xwardan, xwar- [OŠTEN-tn' < A ʾth, √ʾth; hwltn' | M xwrdn, xwr-, N ~] eat, consume. ~išn: food' supports xvartan/xvariš; but for 'stable' MacKenzie has only 'āxwarr [ʾhwl | N āxur] manger, stable. ~-sālār head groom' — no 'av-xur'.\"},\n      {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II p.219 (NYB_vol2_glossary.txt line 4352)\", \"stance\": \"supports\", \"note\": \"'xʷartan [hwltn'; ŠTHn-tn'] 1. to eat, passim … 2. to drink … — Av. (1865 sq.) xʷar-; MPrth wxr- and xwr-; MPrs xwr-; Paz. NP xvar-. — V. xʷarg, xʷarišn …'\"},\n      {\"src\": \"HUB\", \"where\": \"Persische Studien pp.5-6, no.8 (HUB.txt leaves 16-17)\", \"stance\": \"contradicts\", \"note\": \"'Np. āxur ‚Stall‘ = phl. āxur oder besser āxʷar … setzt offenbar ein zd. *āxʷara- oder ā-xʷarena- voraus, das sich nur im 2. Gliede mit zd. avō-xʷarena- = phl. āpxʷar (so, nicht avxʷar ist zunächst zu lesen!) deckt.' Hübschmann rejects both 'av-xur' and the avō- prefix.\"},\n      {\"src\": \"HRN\", \"where\": \"Grundriss no.507, p.112 (HRN.txt leaf 134)\", \"stance\": \"supports\", \"note\": \"'xurden … ‚essen, trinken‘ … aw. √xʷar-, xʷaraiti ‚essen‘; phlv. xʷartan, xʷar(i)šn, xʷartār, xʷār etc., bezw. xurtan, arm. LW. xortik ‚Essen, Speise‘' — Nourai's xvartan and xvariš stand here side by side.\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Persian\",\n     \"words\": \"xordan «خوردن ( خور ، خوره )»; xoreš «خورش»; xorangâh «خورنگاه ( خورنگه )»; xavarnağ «خَوَرنَق»; âxor «آخور ( آخُر ، آبخور )»\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"xordan: MP xwardan > early NP xwardan, spelt خوردن; the labial of the xw- cluster was lost before a back vowel from about the 15th c., giving modern xordan, with present stem خور xor(-) < MP xwar-. Cheung (EDIV 147) and Wiktionary put it on PIr. *huar-, Av. xʷaraiti — the chain is beyond doubt. xoreš: MP xwarišn 'food' > NP خورش (MP -išn > NP -eš), narrowed in modern usage to the stewed dish eaten with rice, Mo'in: 'آنچه با نان یا برنج خورند؛ قاتق'. xorangâh/xorangeh: خورن (verbal stem of خوردن) + گاه 'place' = 'eating place, banqueting hall'; cf. MP xwaran 'banquet' (MacKenzie p.96). xavarnağ: the Arabicised form of this word — Mo'in's dictionary gives 'خورنق [معرّب خورنگه] کاخ با شکوه، کوشک با جلال', and the Lakhmid palace al-Khawarnaq near al-Hira, built for al-Nu‘mān I by the architect Sinimmār in the 5th c. CE, was already explained by al-Aṣma‘ī as Persian ḵu(w)ran-gāh 'place of eating and drinking'. The Persian origin is generally accepted, though Nöldeke preferred to compare Talmudic aḵwarneqā 'pergola, summer-house' and the matter is not settled. âxor: MP āxwarr 'manger, stable' (MacKenzie p.14) > NP آخور, also borrowed into Armenian axoṛ, Kurdish axōr, Pashto āxōr. Nourai's gloss 'animals' \\\"drinking place\\\"' and the variant آبخور follow Horn/Bartholomae, who read the Pahlavi gloss of Av. avō.xʷarəna- as āp-xwar; Hübschmann (PSt 5), MacKenzie and Wiktionary instead derive it from *ā-xʷara-/ā-xʷarəna- 'eating place' (ā- + the same xʷar- 'eat'), with آبخور a later folk-etymological reshaping. Mo'in's entry keeps both senses ('معلف، طویله، اصطبل' and 'گودیی که در سنگ یا چوب برای آب ایجاد کنند، حوضچه'). On the chart's own NOTE: Mann (IEC p.1348) really does list 'Per. xware ‚gangrene; leprosy‘' — but under 'suer- (3) ‚harm, hurt, corrupt‘' and 'suer- (4) ‚swelling, suppuration, gangrene, ulcer‘', beside Av. xʷarō 'wound', NOT under a root meaning 'to cut'; Nourai has mis-stated Mann's gloss. Modern opinion is genuinely split: Mann's grouping is supported by Av. xʷara- 'Wunde' (Bartholomae) and by MP xwar 'a degree of sin' = Av. xʷara- (MacKenzie p.96), whereas Mo'in derives خوره straight from خوردن ('آنچه که چیزی را بخورد و از میان برد؛ (پز.) جذام'). Because خوره is only a bracketed side-form here, it does not change the node's verdict, but the NOTE's 'to cut' should be read as 'to harm, to ulcerate'.\",\n     \"derivation_fa\": \"«خوردن» بازماندهٔ xwardan فارسی میانه است؛ خوشهٔ xw- در فارسی نو از سدهٔ نهم هجری به بعد عنصر لبی خود را از دست داد و xwardan به xordan بدل شد، با ستاک حال «خور». «خورش» از xwarišn پهلوی است (پسوند -išn پهلوی در فارسی نو به -eš بدل می‌شود) که نخست «خوراک» و سپس «قاتق، آنچه با نان یا برنج خورند» معنا یافت. «خورنگاه/خورنگه» ترکیب ستاک خورن + گاه «جای خوردن» است؛ قس. xwaran «بزم» در پهلوی. «خورنق» معرّبِ همین «خورنگه» است؛ معین نیز می‌نویسد «خورنق [معرّب خورنگه]: کاخ باشکوه»، و اصمعی از دیرباز آن را فارسی «خُورَن‌گاه» یعنی «جای خوردن و آشامیدن» دانسته بود؛ هرچند نُلدکه آن را با «اخوَرنَقا»ی تلمودی به معنی سایه‌بان سنجیده و مسئله قطعی نیست. «آخور» از āxwarr فارسی میانه «آخور، اصطبل» است (مکنزی ص ۱۴) که به ارمنی axoṙ و کردی axōr نیز وام رفته است؛ معنای «آبخور» که نورایی آورده از خوانش هُرن و بارتولومه (āp-xwar) می‌آید، اما هوبشمان و مکنزی و ویکی‌واژه آن را از *ā-xʷarana- «جای خوردن» می‌دانند و «آبخور» را ریشه‌شناسی عامیانه. دربارهٔ یادداشت نمودار: مان در ص ۱۳۴۸ «خوره» را ذیل *suer- «آزردن، زخم و آماس» آورده نه ذیل ریشه‌ای به معنی «بریدن»؛ معین در مقابل خوره را از خوردن می‌گیرد. روی‌هم‌رفته ادعای نورایی با احتیاط پذیرفتنی است.\",\n     \"sources\": [W_XORDAN, W_AXUR, WP_KHAW],\n     \"ref_check\": [\n      {\"ref\": \"MON:1455\", \"status\": \"supports\", \"note\": \"Mo'in's own entries carry the claims: 'خورش: [= خورشت] (امص.) خوردن. (ا.) خوردنی، طعام، غذا. آنچه با نان یا برنج خورند؛ قاتق'; 'خورنق: [معرّب خورنگه] (ا.) کاخ با شکوه، کوشک با جلال'; 'خوره: (ا.) آنچه که چیزی را بخورد و از میان برد. (پز.) جذام'; 'آخُر: (ا.) جایگاهی از گِل و سنگ و مانند آن که برای علف و کاه و جو خوردن چهارپایان سازند؛ معلف، طویله، اصطبل' (MON_part1.txt). The cited page 1455 itself is not checkable in the local two-volume abridgement, which has no pagination in its OCR.\"},\n      {\"ref\": \"FVF:221\", \"status\": \"not_checked\", \"note\": \"Emam Shushtari, Farhang-e Vāžehā-ye Fārsi dar Zabān-e ‘Arabi, exists only behind the noorlib.ir page viewer (refs_online.json: kind 'website', no local file); the page could not be opened. It is cited here for the Arabicised خورنق, and the claim is independently confirmed by Mo'in and by al-Aṣma‘ī's derivation reported in the Khawarnaq literature.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"HRN\", \"where\": \"Grundriss no.507, p.112 and no.8, p.4\", \"stance\": \"supports\", \"note\": \"no.507: 'xurden (Firdusī: xʷarden) ‚essen, trinken‘, xurāk … xuriš'; no.8: 'āxur ‚Stall‘ … arm. LW. axoṛ, kurd. LW. axōr'.\"},\n      {\"src\": \"BQT\", \"where\": \"vol.2, printed p.788 (leaf 247) and p.789\", \"stance\": \"supports\", \"note\": \"Mo'in's footnote 'خوردن — بر وزن بردن، اوستا hvar-، پهلوی xvartan … به معنی فروبردن و بلعیدن غذا'; the entry خور on leaf 246 has the sense 'خوردنی اندک … قوت لایموت' and the footnote 'مخفف خورنگه و خورنق'.\"},\n      {\"src\": \"MON\", \"where\": \"Farhang-e Farsi, s.vv. خورش، خورنق، خوره، آخُر\", \"stance\": \"supports\", \"note\": \"quoted in ref_check above; note especially 'خورنق [معرّب خورنگه]', which is exactly Nourai's xorangâh > xavarnağ arrow.\"},\n      {\"src\": \"HUB\", \"where\": \"Persische Studien p.5 no.8\", \"stance\": \"partial\", \"note\": \"accepts NP āxur < Av. *ā-xʷara-/ā-xʷarəna-, i.e. from xʷar- 'eat' as Nourai has it, but rejects the avō- 'water' first element and hence the gloss 'drinking place'.\"},\n      {\"src\": \"IEC\", \"where\": \"Mann, IECD p.1348 (IEC.txt lines 17992-17993)\", \"stance\": \"partial\", \"note\": \"'suer- (3) “harm, hurt, corrupt” … Per. xware, s. “corruption, gangrene”'; 'suer-, -on, -en (4) “swelling, suppuration, gangrene, ulcer” … Av. xwaro, m. “wound”; Per. xware, s. “gangrene; leprosy”'. The page and root-name in Nourai's NOTE are right; the gloss 'to cut' is not Mann's.\"},\n      {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e Rishe-ha-ye Hend-o-Orupayi, printed p.249 (pdf 248), s.v. خوان\", \"stance\": \"supports\", \"note\": \"the entry for خوان 'خوردنی / سینی یا طبق مواد خوراکی' cites Avestan and Pahlavi forms alongside Old English SWEALLOW/SWELGAN and refers to برهان قاطع ۷۸۳ and فرهنگ معین ۱۳۴۹ — an independent modern Persian source grouping خوردن-words with Gmc. 'swallow'.\"}\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"Germanic\",\n     \"words\": \"swel-han\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Proto-Germanic *swelhan-/*swelgan- 'to swallow, gulp down', a strong class-III verb: OHG swelahan/swelgan, MHG swelhen/swelgen, G schwelgen 'to revel', OE swelgan, ON svelgja, OS far-swelgan, MDu. swelghen, Du. zwelgen. Watkins derives it from an 'extended form *swelk-' of swel-1; Pokorny p.1045 has the same ('von einer Erweiterung suelk-: ahd. swelhan und swelgan „verschlucken, trinken“'). Nourai's spelling 'swel-han' is Watkins's *swelhan with the k/h alternation of Verner's law (*swelk- > *swelh-/*swelg-). The hyphen marks the reconstruction, not a compound.\",\n     \"derivation_fa\": \"صورت ژرمنی آغازین *swelhan-/*swelgan- «فروبردن، بلعیدن»، فعل قوی ردهٔ سوم: آلمانی علیای کهن swelahan/swelgan، انگلیسی کهن swelgan، نورس کهن svelgja، هلندی zwelgen. پوکورنی (ص ۱۰۴۵) و واتکینز هر دو آن را از گسترشِ k-دارِ ریشه (*swel-k-) می‌دانند؛ دوگانگی h/g بازتاب قانون ورنر است. صورتی که نورایی آورده (swel-han) همان *swelhan واتکینز است و خط تیره نشانهٔ بازسازی است، نه ترکیب. ادعای نورایی درست است.\",\n     \"sources\": [E_SWALLOW],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. swel-1: 'Extended form *swelk- in Germanic *swelgan, *swelhan in Old English swelgan, to swallow: SWALLOW1; GROUNDSEL1' — both variants, both glosses, as on the chart.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein, CEDEL s.v. swallow, v. (KLN_1966.txt line 37661)\", \"stance\": \"supports\", \"note\": \"'ME. swelowen, swalewen, fr. OE. swelgan, rel. to OS. far-swelgan, ON. svelgja, Swed. svalja “to swallow”, MDu. swelghen, Du. zwelgen … OHG. swelahan, swelgan “to swallow”, MHG. swelhen, swelgen … G. schwelgen “to revel”.'\"},\n      {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. II p.530\", \"stance\": \"supports\", \"note\": \"lists the same Germanic group (ahd. swelhan/swelgan, ags. swelgan, aisl. svelga, engl. swill) under 1. suel-.\"},\n      {\"src\": \"POK\", \"where\": \"IEW p.1045\", \"stance\": \"supports\", \"note\": \"'von einer Erweiterung suelk-: ahd. swelhan und swelgan „verschlucken, trinken“, ags. swelgan, aisl. svelga, nhd. schwelgen'.\"}\n     ]\n    },\n    {\n     \"id\": 5,\n     \"lang\": \"English\",\n     \"words\": \"swallow\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"ME swelowen/swalewen < OE swelgan (class III strong, pret. swealg, pp. swolgen) < PGmc *swelgan-/*swelhan-. The modern spelling with -ow- is the regular ME outcome of OE -g- after a back vowel (cf. follow < folgian). The noun swallow 'gullet, abyss' is OE geswelg. This is the homonym of swallow 'the bird' (OE swealwe), which is unrelated. Etymonline and Klein agree, and Watkins lists SWALLOW1 under swel-1 precisely as the chart does.\",\n     \"derivation_fa\": \"انگلیسی swallow «بلعیدن» از انگلیسی میانهٔ swelowen و آن از انگلیسی کهن swelgan (فعل قوی ردهٔ سوم، گذشته swealg) از ژرمنی آغازین *swelgan-. املای امروزی با ‎-ow-‎ نتیجهٔ قاعده‌مندِ تحول ‎-g-‎ انگلیسی کهن پس از واکهٔ پسین در انگلیسی میانه است (قس. follow از folgian). این واژه با swallow «پرستو» (انگلیسی کهن swealwe) هم‌آواست ولی هم‌ریشه نیست. کلاین، اتیمآنلاین و واتکینز همگی این زنجیره را تأیید می‌کنند؛ ادعای نورایی درست است.\",\n     \"sources\": [E_SWALLOW],\n     \"ref_check\": [\n      {\"ref\": \"(none given)\", \"status\": \"not_checked\", \"note\": \"the node carries refs=None in the book; the parent Germanic box's AHD citation covers it (Watkins swel-1 … 'Old English swelgan, to swallow: SWALLOW1').\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein, CEDEL s.vv. swallow v. and swallow n. (KLN_1966.txt lines 37661-37662)\", \"stance\": \"supports\", \"note\": \"'swallow, n., the act of swallowing; gullet. — ME. swelowe, swalowe, fr. OE. geswelg, “gulf, abyss”, fr. swelgan, “to swallow”.'\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985, index 'SWALLOW1 swel-1'\", \"stance\": \"supports\", \"note\": \"the index line 'SWALLOW1 swel-1' and the root entry both place the English word under this root.\"},\n      {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/swallow\", \"stance\": \"supports\", \"note\": \"'from Old English swelgan … class III strong verb (past tense swealg, past participle swolgen), from Proto-Germanic *swelgan/*swelhan … from PIE root *swel- (1) “to eat, drink” … also in Iranian *khvara- “eating”.'\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 2,\n   \"root\": \"Swen\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *swenh₂- 'to sound, resound' (Pokorny 1046 'suen-'; Watkins swen-; LIV 611)\",\n   \"note\": \"Pokorny IEW p.1046 has 'suen-, „tönen, schallen“; suono-s „Ton, Schall“' with Skt. svánati, Lat. sonō/sonus, OIr. senim, OE swinsian, OHG/OE swan, ON svanr — exactly the tree Nourai draws. Watkins prints 'swen-. To sound' with Germanic *swanaz/*swanon- 'singer' and Latin sonus. The laryngeal-set reconstruction is *swenh₂- (Rix, LIV 611; Wiktionary), a refinement of the shape, not of the content. Root name, language label and gloss are all correct; every branch on the page is standard.\",\n   \"note_fa\": \"ریشهٔ هندواروپایی آغازین *swenh₂- «صدا دادن، طنین افکندن» در فرهنگ پوکورنی (ص ۱۰۴۶) با صورت suen- و معنی «tönen, schallen» آمده و مشتق اسمی *suono-s «صدا» را نیز آورده است، با گواهانی چون svánati سنسکریت، sonus و sonāre لاتین، swinsian انگلیسی کهن و swan «قو». واتکینز نیز آن را با همین معنا و همین شاخه‌ها آورده است. بازسازی امروزی با حنجره‌ای (*swenh₂-، ریکس، LIV ۶۱۱) تنها اصلاح صوری است و محتوا را تغییر نمی‌دهد. نام ریشه، برچسب زبانی و معنایی که نورایی آورده هر سه درست است.\",\n   \"sources\": [W_SWENH2, E_SWAN],\n   \"ref_check\": [\n    {\"ref\": \"POK:1046\", \"status\": \"supports\", \"note\": \"POK_03.txt leaf 289 (p.1046): 'suen-, „tönen, schallen“; suono-s „Ton, Schall“. Ai. svánati … (= lat. sonit) … sváná- m. „Ton, Schall“ (= lat. sonus) … xʷanat͟.caxra- „einer, des Räder sausen“; lat. sonō, -āre … ags. swinsian „singen“ … auch ahd. ags. swan „Schwan“, aisl. svanr.'\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. II pp.524-525 (WLD_Bd2_pages.txt leaves 529-530)\", \"stance\": \"supports\", \"note\": \"'… ags. swinsian „singen, Melodie oder Musik machen“, geswin „Melodie, Musik, Gesang“ … wohl auch ahd. ags. swan „Schwan“, aisl. svanr „männlicher Schwan“ … also nicht mit su-en- „Sonne, Licht“ identisch.'\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. swen- (AHD_watkins1985.txt line 1046)\", \"stance\": \"supports\", \"note\": \"'swen-. To sound. 1. Suffixed o-grade form *swon-o- in: a. Germanic *swanaz, *swanon-, “singer”, in Old English swan, swan: SWAN; b. Latin sonus, a sound: SONE, SONIC, SONNET, SOUND1; UNISON. 2. Form *swen-ā- in Latin sonāre … [Pok. suen- 1046.]'\"},\n    {\"src\": \"SYN\", \"where\": \"Buck, Selected Synonyms 15.45 'sound' (SYN.txt line 26260)\", \"stance\": \"supports\", \"note\": \"'Lat. sonus “sound” (> It. suono, Fr. son …) with vb. sonere, sonāre … : Skt. svan- “to sound, make a noise” … Walde-P. 2.524f.'\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Avestan\",\n     \"words\": \"xvan, xwan\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Avestan xʷan- 'to sound, call', the regular Iranian reflex of *swenh₂- (*sw- > Ir. *hw- > Av. xʷ-). Its Avestan attestation is indirect but secure: Pokorny cites the compound xʷanat͟.caxra- 'whose wheels resound' (an epithet in the Yasht literature), and Horn (Grundriss no.499) writes 'aw. √xʷan- in xʷanat͟.caxra- („klirrend“)'; Wiktionary adds the finite form apa-xʷanuuaiṇti 'they sound away'. Skt. svánati 'sounds' is the exact Indic match, so the Indo-Iranian stem *swanH- is uncontroversial.\",\n     \"derivation_fa\": \"xʷan- اوستایی «صدا دادن، خواندن» بازتاب قاعده‌مند ریشهٔ *swenh₂- است: *sw- هندواروپایی در ایرانی به hw- و در اوستایی به xʷ- بدل می‌شود. گواه آن در اوستا غیرمستقیم اما مطمئن است: پوکورنی ترکیب xʷanat̰.caxra- «آنکه چرخ‌هایش طنین می‌افکند» را می‌آورد و هُرن (بند ۴۹۹) می‌نویسد «اوستایی √xʷan- در xʷanat̰.caxra-»؛ ویکی‌واژه نیز صورت فعلی apa-xʷanuuaiṇti را نقل می‌کند. برابر دقیق هندی باستان آن svánati است. ادعای نورایی درست است.\",\n     \"sources\": [W_XANDAN, W_SWENH2],\n     \"ref_check\": [\n      {\"ref\": \"POK:1046\", \"status\": \"supports\", \"note\": \"IEW p.1046 lists 'xʷanat͟.caxra- „einer, des Räder sausen“' immediately after Skt. svánati as the Iranian witness of suen- — the arrow root→Avestan of the chart.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"HRN\", \"where\": \"Grundriss no.499, p.110 (HRN.txt leaf 132)\", \"stance\": \"supports\", \"note\": \"'aw. √xʷan- in xʷanat͟.caxra- („klirrend“); phlv. xʷāntan, xunīt (GF.); ai. √svan-, svánati „tönen“.'\"},\n      {\"src\": \"BRT\", \"where\": \"Altiran. Wb. col. 1847ff. (BRT.txt line 30657)\", \"stance\": \"partial\", \"note\": \"Bartholomae's headword 'j., g. hvar-, g. xʷan- n. „Sonne; Sonnenball, Sonnenlicht“' is the SUN word, a different xʷan-; the sounding root appears only in the compound xʷanat͟.caxra-, so Bartholomae is not a witness against, but he does show that Av. xʷan- is homonymous and must be kept apart from 'sun'.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"EDIV 2007 pp.144-145 s.v. *huanH (cited on the Wiktionary page for خواندن)\", \"stance\": \"supports\", \"note\": \"Cheung reconstructs PIr. *hwanH- 'to call', from PIIr. *swanH-, from PIE *swenh₂- 'to sound' — unlike *huar1, this root keeps its Indo-European pedigree.\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Pahlavi\",\n     \"words\": \"xvantan\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"MP xwāndan, xwān- [heterograms KRYTWN-/KLYTWN-tn'] 'to call, summon, read, recite' (MacKenzie, CPD p.95; Manichaean MP xwnd, xwān-), from Av. xʷan- with the causative/denominative long vowel and the Iranian past stem in *-ta-. Horn no.499 gives the same: 'phlv. xʷāntan, xunīt'. Mo'in's footnote in Borhan-e Qate' p.784-785 also prints 'پهلوی xvāndan'. NB the book prints the form with a long ā ('xvântan'); the JSON has 'xvantan' without the circumflex — a small extraction slip, see the page summary.\",\n     \"derivation_fa\": \"«xvāntan» همان xwāndan فارسی میانه است (هزوارش KRYTWN-tn'، مانوی xwnd/xwān-) به معنی «خواندن، فراخواندن، تلاوت کردن»، بازماندهٔ xʷan- اوستایی با کشیدگی واکه و ستاک گذشتهٔ ایرانی با ‎*-ta-‎. مکنزی (ص ۹۵) و هُرن (بند ۴۹۹: «پهلوی xʷāntan») و حاشیهٔ معین بر برهان قاطع (ص ۷۸۴ـ۷۸۵: «پهلوی xvāndan») هر سه همین را می‌گویند. ادعای نورایی درست است. (نکته: در چاپ کتاب «xvântan» با الف کشیده آمده، ولی در داده‌های استخراج‌شده «xvantan» ثبت شده است.)\",\n     \"sources\": [W_XANDAN],\n     \"ref_check\": [\n      {\"ref\": \"BQT:784\", \"status\": \"supports\", \"note\": \"Borhan-e Qate' vol.2, leaf 243 of BQT_v2_pages.txt = printed pp.784-785 (offset printed = leaf+541). Mo'in's footnote 5 there reads: 'خواندن - بفتح اول و پنجم، بر وزن ماندن، از ریشهٔ اوستایی xvan-، پهلوی xvāndan … ریشهٔ هندی باستانی svan- (صدا دادن)، کردی xwāndin … استی … وخی xan- … : قرائت کردن، مطالعه کردن، دعوت کردن …' — Nourai's Avestan→Pahlavi→Persian chain word for word.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD p.95 (PHD.txt line 663)\", \"stance\": \"supports\", \"note\": \"'xwandan, xwān- [KRYTWN-, KLYTWN-tn' < A qry | M xwnd, xwān-, N xwāndan] call, summon.'\"},\n      {\"src\": \"HRN\", \"where\": \"Grundriss no.499, p.110\", \"stance\": \"supports\", \"note\": \"'phlv. xʷāntan, xunīt (GF.)' — Horn's Pahlavi form is spelled exactly as the book prints it (xʷāntan).\"},\n      {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (NYB_vol2_glossary.txt)\", \"stance\": \"silent\", \"note\": \"grep for 'xvāntan / xwān-' in the glossary returns only the homonymous xʷan- 'sun' in xʷar-xšēt and xuān-sand; the verb is not glossed in the Manual's selection.\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Persian\",\n     \"words\": \"xândan «خواندن ( خوان ۲ )»; xanîdan «خنیدن»; âxūnd «آخوند»\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"xândan: MP xwāndan > NP خواندن, with the same loss of the labial in the xw- cluster as in خوردن (so xwāndan > xāndan), present stem خوان xwān- 'call!, read!'; the semantic range 'call → summon → invite → recite → read' is already Middle Persian. Wiktionary/Cheung: PIr. *hwanH- 'to call' < PIIr. *swanH- < PIE *swenh₂-. Confirmed. xanîdan: the short-vowel doublet of the same stem, denominative/intransitive 'to resound, echo; to become famous', with Mo'in's gloss 'پیچیدن آواز (در کوه، حمام، گنبد و غیره)، آوازه پیدا کردن، مشهور شدن' — precisely Nourai's 'to echo, to be famous'; Horn no.499 groups it with خواندن ('xanīden, xunīde, xunyā „Musik“'), and Firdowsi's line quoted on the chart ('خنیده به گیتی به مهر و وفا') shows the 'famous' sense. Confirmed. âxūnd: this is the weak link and is why the node is only 'plausible'. Mo'in himself brackets the word '[ظ. با مخف. آقا + خوند = خداوند؛ یا خوند = خواندن]' — i.e. he puts āqā + xwand (< xudāvand) first and derivation from خواندن second; Wiktionary, following H. Algar in Encyclopaedia Iranica, says the origin is unclear and that neither set of etymologies is 'entirely satisfactory'. Nourai puts آخوند under خواندن without accounting for the initial آ-, which no reading from خواندن alone explains. The word is therefore uncertain, not wrong.\",\n     \"derivation_fa\": \"«خواندن» از xwāndan فارسی میانه است؛ همان فرایندی که در «خوردن» دیده می‌شود عنصر لبی خوشهٔ xw- را از میان برد و xwāndan به xāndan بدل شد، با ستاک حال «خوان». گسترهٔ معنایی «صدا زدن ← فراخواندن ← دعوت کردن ← تلاوت کردن ← خواندنِ نوشته» از همان دورهٔ میانه پیداست (چونگ: ایرانی آغازین *hwanH- «صدا زدن»). «خنیدن» گونهٔ واکهٔ کوتاه همان ستاک است: معین آن را «پیچیدن آواز (در کوه، حمام، گنبد و غیره)، آوازه پیدا کردن، مشهور شدن» معنا کرده و هُرن (بند ۴۹۹) آن را در کنار «خواندن» و «خنیا» آورده است؛ بیت فردوسیِ روی نمودار نیز معنای «مشهور» را نشان می‌دهد. اما «آخوند» حلقهٔ سست این جعبه است: خود معین در کروشه می‌نویسد «ظ. با مخف. آقا + خوند = خداوند؛ یا خوند = خواندن»، یعنی نخست ترکیب آقا + خداوند را می‌آورد؛ دانشنامهٔ ایرانیکا (الگار) هیچ‌یک از این ریشه‌شناسی‌ها را کاملاً رضایت‌بخش نمی‌داند. نورایی «آ» آغازین را توضیح نمی‌دهد. پس دو واژهٔ نخست تأیید می‌شود و سومی نامطمئن است.\",\n     \"sources\": [W_XANDAN, W_AXUND],\n     \"ref_check\": [\n      {\"ref\": \"HRN:110\", \"status\": \"supports\", \"note\": \"Horn, Grundriss p.110 no.499 (HRN.txt leaf 132): 'xʷānden ‚rufen, lesen etc.‘, xanīden, xunīde, xunyā ‚Musik‘, xunyāger. aw. √xʷan- in xʷanat͟.caxra- („klirrend“); phlv. xʷāntan, xunīt (GF.); ai. √svan-, svánati „tönen“. kurd. xʷāndin, xūndin ‚lesen‘ …' — the cited page carries both xândan and xanīdan and the whole Avestan→Pahlavi chain. It does not mention āxūnd.\"},\n      {\"ref\": \"BQT:784\", \"status\": \"supports\", \"note\": \"Mo'in's footnote on خواندن at Borhan vol.2 p.784-785 (leaf 243) gives Av. xvan- > Pahl. xvāndan > NP خواندن with the senses 'قرائت کردن … دعوت کردن … تغنی کردن', matching 'to read, sing, call' exactly. Silent on آخوند.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"Farhang-e Farsi s.vv. خنیدن and آخوند (MON_part1.txt)\", \"stance\": \"partial\", \"note\": \"خنیدن: '(مصل.) پیچیدن آواز (در کوه، حمام، گنبد و غیره). آوازه پیدا کردن، مشهور شدن' = supports; آخوند: '[ظ. با مخف. آقا + خوند = خداوند؛ یا خوند = خواندن]' = only the second of two options.\"},\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD p.95\", \"stance\": \"supports\", \"note\": \"'xwandan, xwān- … N xwāndan' explicitly carries the Middle→New Persian arrow.\"},\n      {\"src\": \"ARY\", \"where\": \"Aryanpur, printed p.250 (pdf page 249), entry خواندن\", \"stance\": \"supports\", \"note\": \"the entry lists اوستایی xʷan-, پهلوی xwāndan beside Latin, French SON, Italian SUONO, Romanian SUNET and the Germanic 'swan' words, with the note 'چم این واژه در زبان‌های رومانس (زبان‌های ناشی از لاتین): صدا' and the reference 'برهان قاطع: ۷۸۴' — the same page Nourai cites, and the same Iranian/Latin/Germanic grouping.\"},\n      {\"src\": \"Encyclopaedia Iranica (via Wiktionary)\", \"where\": \"H. Algar, 'Āḵūnd', EIr. online, summarised at en.wiktionary.org/wiki/آخوند\", \"stance\": \"contradicts\", \"note\": \"'Unclear. Perhaps a compound of the first element of آقا with either خواندن or خداوند'; Iranica calls the set of etymologies not 'entirely satisfactory'. A plain descent from خواندن, as drawn, is not the modern view.\"}\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"Latin\",\n     \"words\": \"sonus\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Latin sonus, -ī m. 'noise, sound' < *swonos, the o-grade thematic noun *swon-o- of *swenh₂-, with the regular Latin loss of *w after *s (cf. soror < *swesōr); the matching verb sonō, sonāre (archaic sonere) continues *swenā-/*swen-. The exact Indic counterpart is Skt. svána- m. 'sound', which is why Pokorny sets up *suono-s. Klein states it in so many words, and Watkins files sonus under swen-.\",\n     \"derivation_fa\": \"لاتین sonus «صدا» از *swonos، اسم مایه‌ای درجهٔ o از ریشهٔ *swenh₂-؛ در لاتین *w پس از *s به‌قاعده می‌افتد (قس. soror «خواهر» از *swesōr). فعل هم‌خانواده‌اش sonō/sonāre (کهن‌تر sonere) بازماندهٔ *swen(ā)- است. برابر دقیق هندی باستانِ آن svána- «صدا» است و از همین‌رو پوکورنی صورت *suono-s را بازسازی کرده است. کلاین و واتکینز هر دو همین را می‌گویند؛ ادعای نورایی درست است.\",\n     \"sources\": [W_SWENH2],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. swen-: 'Suffixed o-grade form *swon-o- in … b. Latin sonus, a sound: SONE, SONIC, SONNET, SOUND1; UNISON.'\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein, CEDEL s.vv. sonant and sound n. (KLN_1966.txt lines 35905, 36005)\", \"stance\": \"supports\", \"note\": \"'L. sonus, “sound”, which stands for *swonos, and is rel. to sonāre (for *swenāre), “to sound”, fr. I.-E. base *swen-, “to sound”, whence also OI. svánati … ON. svanr, OE. swan, “swan”, prop. “the singing bird”.'\"},\n      {\"src\": \"SYN\", \"where\": \"Buck 15.45 (SYN.txt line 26260)\", \"stance\": \"supports\", \"note\": \"'Lat. sonus “sound” (> It. suono, Fr. son, OSp. sueno, Rum. sun …) with vb. sonere, sonāre … : Skt. svan- “to sound” … Walde-P. 2.524f.'\"},\n      {\"src\": \"POK\", \"where\": \"IEW p.1046\", \"stance\": \"supports\", \"note\": \"'lat. sonō, -āre, -uī … sonere (*suenō) „tönen, schallen, klingen, rauschen“, sonus (*suonos)'.\"}\n     ]\n    },\n    {\n     \"id\": 5,\n     \"lang\": \"English\",\n     \"words\": \"sound, sonic\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"sound 'noise': ME soun, borrowed from Anglo-French soun / Old French son < Latin sonus; the final -d is excrescent (as in bound, pound, from ME soun + d after -n, 16th c.). sonic: a 20th-century learned formation on Latin sonus with the adjectival suffix -ic (first in 'sonic' of sound waves, then in supersonic, 1919). Both are therefore Latin-mediated, exactly as the chart's Latin→English arrow shows. The homonym sound 'strait' and sound 'healthy' belong elsewhere (*swem-, *swento-), and the chart correctly does not include them.\",\n     \"derivation_fa\": \"«sound» به معنی «صدا» از انگلیسی میانهٔ soun است که از فرانسویِ انگلونورمان soun / فرانسهٔ کهن son و آن از sonus لاتین گرفته شده؛ «د» پایانی افزودهٔ ثانوی انگلیسی است (مانند bound و pound). «sonic» ساختی نوین و عالمانه است از sonus لاتین با پسوند صفت‌ساز ‎-ic‎ که از سدهٔ بیستم رواج یافت (سپس supersonic). پس هر دو از راه لاتین آمده‌اند، درست همان‌گونه که پیکان نمودار نشان می‌دهد. هم‌آواهای دیگرِ sound («تنگهٔ دریا» و «سالم») ریشهٔ دیگری دارند و به‌درستی در نمودار نیامده‌اند. ادعای نورایی درست است.\",\n     \"sources\": [W_SWENH2],\n     \"ref_check\": [\n      {\"ref\": \"(none given)\", \"status\": \"not_checked\", \"note\": \"the node carries refs=None; the parent Latin box's AHD citation covers it (Watkins swen- … 'Latin sonus, a sound: SONE, SONIC, SONNET, SOUND1').\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein, CEDEL s.v. sound, n. (KLN_1966.txt line 36005)\", \"stance\": \"supports\", \"note\": \"'sound, n., noise. — ME. soun, fr. OF. (= F.) son, fr. L. sonus, “sound” … The d in sound is excrescent.'\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985, index entries 'SOUND1 swen-' and 'SONIC swen-'\", \"stance\": \"supports\", \"note\": \"both English words are indexed to swen-.\"},\n      {\"src\": \"SYN\", \"where\": \"Buck 15.45\", \"stance\": \"supports\", \"note\": \"'ME soun, NE sound, fr. Anglo-Fr. soun = OFr. son, fr. Lat. sonus (above).'\"}\n     ]\n    },\n    {\n     \"id\": 6,\n     \"lang\": \"Germanic\",\n     \"words\": \"swanon\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Proto-Germanic *swanaz / *swanon- '“singer”, swan', an o-grade *swon-o- formation of *swenh₂- identical in shape with Latin sonus; the name is a kenning, 'the singing bird', and its family in Germanic still shows the verbal sense (OE swinsian 'to make melody', geswin 'melody, song'). Nourai's gloss 'singer' is Watkins's own word. Pokorny and Walde-Pokorny list the same set and explicitly warn that this swan- is NOT the *su-en- of 'sun'.\",\n     \"derivation_fa\": \"صورت ژرمنی آغازین *swanaz / *swanon- «قو»، از درجهٔ o‌ی ریشه (*swon-o-)، از نظر ساخت دقیقاً همتای sonus لاتین است؛ نام پرنده در اصل کنایه‌ای است به معنی «پرندهٔ آوازخوان»، و خویشاوندان ژرمنی‌اش هنوز معنای فعلی را نگه داشته‌اند (انگلیسی کهن swinsian «نغمه ساختن»، geswin «نغمه، سرود»). معنای «singer» که نورایی آورده عین واژهٔ واتکینز است. پوکورنی و والده‌ـ‌پوکورنی همین گروه را می‌آورند و تصریح می‌کنند که این *swan- با *su-en- به معنی «خورشید» یکی نیست. ادعای نورایی درست است.\",\n     \"sources\": [E_SWAN, W_SWENH2],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. swen-: 'Suffixed o-grade form *swon-o- in: a. Germanic *swanaz, *swanon-, “singer”, in Old English swan, swan: SWAN.' Nourai's 'swanon: singer' is a direct lift of this.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"IEW p.1046\", \"stance\": \"supports\", \"note\": \"'ags. swinsian „singen, Musik machen“, swinn „Musik, Gesang“; auch ahd. ags. swan „Schwan“, aisl. svanr „männlicher Schwan“.'\"},\n      {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. II p.525\", \"stance\": \"supports\", \"note\": \"'wohl auch ahd. ags. swan „Schwan“, aisl. svanr „männlicher Schwan“ … also nicht mit su-en- „Sonne, Licht“ identisch (z. B. Fick I4 341, Uhlenbeck aaO.).'\"},\n      {\"src\": \"KLN\", \"where\": \"Klein, CEDEL s.v. swan (KLN_1966.txt line 37670)\", \"stance\": \"supports\", \"note\": \"'Swan, prop. means “the singing bird”. The name derives from a gradational var. of I.-E. base *swen-, *swon-, “to sound”, whence sonāre …'\"}\n     ]\n    },\n    {\n     \"id\": 7,\n     \"lang\": \"English\",\n     \"words\": \"swan\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"OE swan (m.) > ME swan > NE swan, the direct inherited continuant of PGmc *swanaz, with cognates OS swan, ON svanr, Dan. svane, MDu. swane, Du. zwaan, OHG/MHG swan, G Schwan. No borrowing is involved; the chart's Germanic→English arrow is simple inheritance. The bird's 'singer' name survives in the calque swan-song (from the classical belief, reported by Aeschylus and Plato, that the swan sings before dying).\",\n     \"derivation_fa\": \"انگلیسی swan «قو» بازماندهٔ مستقیم swan انگلیسی کهن و آن از *swanaz ژرمنی آغازین است، با هم‌ریشه‌هایی چون svanr نورس کهن، zwaan هلندی و Schwan آلمانی؛ هیچ وام‌گیری در کار نیست و پیکان نمودار صرفاً وراثت را نشان می‌دهد. معنای اصلی «آوازخوان» در ترکیب swan-song «آواز قو» (از باور کهن یونانی که قو پیش از مرگ می‌خواند) باقی مانده است. ادعای نورایی درست است.\",\n     \"sources\": [E_SWAN],\n     \"ref_check\": [\n      {\"ref\": \"(none given)\", \"status\": \"not_checked\", \"note\": \"the node carries refs=None; the parent Germanic box's AHD citation covers it (Watkins swen- … 'Old English swan, swan: SWAN').\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein, CEDEL s.v. swan (KLN_1966.txt line 37670)\", \"stance\": \"supports\", \"note\": \"'swan, n. — ME., fr. OE. swan, rel. to OS. swan, ON. svanr, Dan. svane, Swed. svan, MDu. swane, Du. zwaan, OHG., MHG. swan, G. Schwan.'\"},\n      {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/swan\", \"stance\": \"supports\", \"note\": \"'from Proto-Germanic *swanaz “singer” … probably etymologically “the singing bird”, from PIE root *swen- “to make sound”; cf. Old English geswin “melody”, swinsian “to make melody”.'\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985, index 'SWAN swen-'\", \"stance\": \"supports\", \"note\": \"the English word is indexed to swen-.\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-491.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(doc, f, ensure_ascii=False, indent=1)\n    f.write(\"\\n\")\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-491.py"
}
```


### [2026-09-14T03:27:05.370Z] TOOL RESULT

```
ok
```


## [2026-09-14T03:27:09.633Z] TOOL CALL #70: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-491.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 491"
}
```


### [2026-09-14T03:27:10.695Z] TOOL RESULT

```
JSON OK
nodes verified: 12/12
node verdicts: {'plausible': 4, 'confirmed': 8}
root verdicts: {'plausible': 1, 'confirmed': 1}
ref checks: {'supports': 11, 'not_checked': 5}
books consulted: {'supports': 33, 'partial': 6, 'contradicts': 2, 'silent': 1} | by book: {'KLN': 6, 'HRN': 5, 'WLD': 3, 'PHD': 3, 'POK': 3, 'AHD': 3, 'BRT': 2, 'CHEUNG': 2, 'NYB': 2, 'HUB': 2, 'MON': 2, 'ARY': 2, 'Etymonline': 2, 'SYN': 2, 'BQT': 1, 'IEC': 1, 'Encyclopaedia Iranica (via Wiktionary)': 1}
```


## [2026-09-14T03:27:16.221Z] TOOL CALL #71: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg491.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/491.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/491.png"
}
```


### [2026-09-14T03:27:16.302Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 70427 Sep 13 23:27 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/491.png
```


## [2026-09-14T03:27:38.685Z] AGENT

Page 491 (book p. 461) verified. `verify_check.py 491`: 12/12 nodes, **0 PROBLEM lines**.

**Verdicts** — roots: 1 confirmed (Swen), 1 plausible (Swel 1). Nodes: 8 confirmed, 4 plausible, 0 disputed, 0 transcription_suspect.
Ref checks: 11 supports, 5 not_checked. 17 books/sources consulted (33 supports, 6 partial, 2 contradicts, 1 silent).

**Plausible (not confirmed) items**
- **Root Swel 1 "to eat"** — Pokorny p.1045 prints it with his own question mark ("Nur iran. und germ.?"), and Watkins keeps it; but Cheung, *EDIV* 2007 pp.147-8, rejects it outright: "There is probably no need to reconstruct an IE root *suel-… IE COGNATES: —". Buck says only "may be connected". So the Avestan↔Germanic equation that is the root's whole content is abandoned by the current standard on Iranian verbs (node #1 Avestan xvar- carries the same caveat; the words themselves are genuine).
- **Pahlavi #2 "av-xur 'stable'"** — this is Horn's 1893 reading (Grundriss no. 8, p. 4, which is almost certainly what AEF:10 translates). Hübschmann corrected it in 1895 (PSt 5-6: "āp-xʷar, *so, nicht avxʷar* ist zunächst zu lesen"), and MacKenzie knows only **āxwarr** 'manger, stable'. Not a misprint — a superseded reading. xvartan/xvariš are fully confirmed (Nyberg, MacKenzie, Mo'in's BQT:788 footnote).
- **Persian #3 (âxor, xavarnağ)** — âxor: modern view (Hübschmann, MacKenzie, Wiktionary) is *ā-xʷarana- "eating place"; Nourai's "drinking place" / آبخور follows Horn-Bartholomae's āp-xwar gloss. xavarnağ: Persian origin widely accepted (Mo'in: «خورنق [معرّب خورنگه]»; al-Aṣmaʿī's ḵu(w)ran-gāh), but Nöldeke prefers Talmudic aḵwarneqā and the name is formally unresolved.
- **Persian #3 of Swen (âxŭnd)** — Iranica (Algar) calls all etymologies "not entirely satisfactory"; Mo'in puts آقا+خداوند first and خواندن second, and the initial آ- is unexplained on Nourai's tree. خواندن and خنیدن themselves confirmed (Horn no. 499 p. 110 is exact).

**On the chart's own NOTE**: Mann IEC p. 1348 does carry "Per. xware 'gangrene; leprosy'", but under **suer- (3) 'harm, hurt, corrupt' / suer- (4) 'swelling, suppuration, ulcer'** beside Av. xʷarō 'wound' — **not** a root "to cut". Nourai mis-states Mann's gloss; the substantive dispute (خوره from *swer- 'wound' vs. Mo'in's derivation from خوردن) is real and recorded.

**Extraction error for the owner to fix** (page image saved to `data/verification/sources/refs/ocr/BOOK/491.png`):
- Entry 2, node #2: the book prints **`xvântan`** (long â); `data/extracted/batch/page-491.json` has `"xvantan"` — the circumflex was lost. Everything else on the page (incl. `avô-xvarena`, `av-xur`, `xavarnağ`, the Sohbat Lârî and Ferdowsî quotes) matches the printed page exactly.

Useful side-result: BQT vol. 2 page offset confirmed as **printed = leaf + 541** in `BQT_v2_pages.txt` (leaf 243 = p. 784 خواندن footnote; leaf 247 = p. 788 خوردن footnote), which resolves the ±3 uncertainty noted in `refs_online.json`.
