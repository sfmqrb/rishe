# Verification process log — verify-page-243


## [2026-09-06T15:48:41.804Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 243 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-243.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-243.json. Write /home/sfmqrb/git/rishe/data/verification/page-243.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 243` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T15:48:42.948Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T15:48:43.648Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T15:48:43.664Z] TOOL RESULT

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


## [2026-09-06T15:48:44.149Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-243.txt"
}
```


### [2026-09-06T15:48:44.174Z] TOOL RESULT

```
1	=== PDF page 243 (book page 213) ===
2	--- entry 0 ---
3	ROOT [Turkish] Kar 2, Qar 2 : black, old, bad luck  (refs TTS:79)
4	#1 (parent #0) [Persian] refs=MON:2650, 2670 | qareh «قره» : black | extra: قرا ، قره نی ، قره قروت ، قراقوش
5	#2 (parent #0) [Turkish] refs=FSD:398; AHD:201 | kara-kŭlâk, qara-qulâq : a wild cat with "black ears"
6	  #3 (parent #2) [Persian] refs=MON:2670 | qareh-qŭlâq «قره قولاق» : black-ear cat, caracal | NOTE: Compare with "syâh-gŭsh:caracal" from root "Kei 1"
7	  #4 (parent #2) [French] refs=AHD:202 | 
8	    #5 (parent #4) [English] refs=FSD:398 | caracal : a wild cat with black ears
9	--- entry 1 ---
10	ROOT Karkar -> redirect to Kar 1
11	--- entry 2 ---
12	ROOT [Sanskrit] Karpâsah : cotton  (refs KLN:238; SYN:402)
13	#1 (parent #0) [Persian] refs=KLN:238; MON:2932 | karpâs «کَرپاس» : cotton cloth
14	  #2 (parent #1) [Arabic] refs=MON:2932;KLN:238 | karbâs
15	    #3 (parent #2) [Persian] refs=MON:2932 | karbâs «کرباس» : cotton cloth
16	#4 (parent #0) [Greek] refs=KLN:238 | karpasos : cotton
17	  #5 (parent #4) [Latin] refs=KLN:238 | 
18	    #6 (parent #5) [English] refs=KLN:238 | carbasus : lint
19	--- entry 3 ---
20	ROOT [Sanskrit] Karpurah, Karpŭrah : camphor tree  (refs KLN:229)
21	#1 (parent #0) [Pahlavi] refs=VDQ:356; BQT:1571 | kâpŭr : camphor
22	  #2 (parent #1) [Persian] refs=BQT:1571 | kâfŭr «کافور» : camphor
23	    #3 (parent #2) [Arabic] refs=PLA:225; DOZ:47; VDQ:356 | kâfŭr | NOTE: TAD:60 derives this from Greek "kafoura".
24	      #4 (parent #3) [Middle Latin] refs=KLN:229 | camphora
25	        #5 (parent #4) [French] refs=None | 
26	          #6 (parent #5) [English] refs=KLN:229 | camphor | NOTE: AHD traces this to the Malay word "kâpŭr: chalk"
27	--- entry 4 ---
28	ROOT Karpŭrah -> redirect to Karpurah
29	
```


## [2026-09-06T15:48:47.345Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/extracted/batch/page-243.json",
 "description": "Read source JSON for page 243"
}
```


### [2026-09-06T15:48:47.430Z] TOOL RESULT

```
{
  "pdf_page": 243,
  "book_page": 213,
  "entries": [
    {
      "root": {
        "name": "Kar 2, Qar 2",
        "lang": "Turkish",
        "refs": "TTS:79",
        "gloss": "black, old, bad luck"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "MON:2650, 2670",
          "words": [
            {"translit": "qareh", "gloss": "black", "script": "قره"}
          ],
          "script_extra": "قرا ، قره نی ، قره قروت ، قراقوش",
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Turkish",
          "refs": "FSD:398; AHD:201",
          "words": [
            {"translit": "kara-kŭlâk, qara-qulâq", "gloss": "a wild cat with \"black ears\"", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "MON:2670",
          "words": [
            {"translit": "qareh-qŭlâq", "gloss": "black-ear cat, caracal", "script": "قره قولاق"}
          ],
          "script_extra": null,
          "note": "Compare with \"syâh-gŭsh:caracal\" from root \"Kei 1\"",
          "quote": null
        },
        {
          "id": 4,
          "parent": 2,
          "lang": "French",
          "refs": "AHD:202",
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": "FSD:398",
          "words": [
            {"translit": "caracal", "gloss": "a wild cat with black ears", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Karkar",
        "redirect": "Kar 1"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Karpâsah",
        "lang": "Sanskrit",
        "refs": "KLN:238; SYN:402",
        "gloss": "cotton"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "KLN:238; MON:2932",
          "words": [
            {"translit": "karpâs", "gloss": "cotton cloth", "script": "کَرپاس"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Arabic",
          "refs": "MON:2932;KLN:238",
          "words": [
            {"translit": "karbâs", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "MON:2932",
          "words": [
            {"translit": "karbâs", "gloss": "cotton cloth", "script": "کرباس"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "وگر چرخ اطلس رود بر خلافت - روانی چو کرباسش از هم درانی",
            "poet": "Vahshî"
          }
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Greek",
          "refs": "KLN:238",
          "words": [
            {"translit": "karpasos", "gloss": "cotton", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Latin",
          "refs": "KLN:238",
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "English",
          "refs": "KLN:238",
          "words": [
            {"translit": "carbasus", "gloss": "lint", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Karpurah, Karpŭrah",
        "lang": "Sanskrit",
        "refs": "KLN:229",
        "gloss": "camphor tree"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Pahlavi",
          "refs": "VDQ:356; BQT:1571",
          "words": [
            {"translit": "kâpŭr", "gloss": "camphor", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:1571",
          "words": [
            {"translit": "kâfŭr", "gloss": "camphor", "script": "کافور"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "نریزد از درخت ارس کافور - نخیزد از میان لاد لادن",
            "poet": "Manŭchehrî"
          }
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Arabic",
          "refs": "PLA:225; DOZ:47; VDQ:356",
          "words": [
            {"translit": "kâfŭr", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": "TAD:60 derives this from Greek \"kafoura\".",
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Middle Latin",
          "refs": "KLN:229",
          "words": [
            {"translit": "camphora", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "French",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "English",
          "refs": "KLN:229",
          "words": [
            {"translit": "camphor", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": "AHD traces this to the Malay word \"kâpŭr: chalk\"",
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Karpŭrah",
        "redirect": "Karpurah"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-06T15:48:49.661Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['TTS','MON','FSD','AHD','KLN','SYN','VDQ','BQT','PLA','DOZ','TAD','POK','WLD','HRN','HUB','ARY','PHD','NYB','SKT','WEB','LKT','AFM','FVQ']:\n    v=d.get(k)\n    print(k, json.dumps(v, ensure_ascii=False)[:400] if v else 'MISSING')\n\""
}
```


### [2026-09-06T15:48:52.646Z] TOOL RESULT

```
TTS {"title": "H. Vámbéry, Etymologisches Wörterbuch der turko-tatarischen Sprachen, Leipzig 1878 (repr. Osnabrück 1972)", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/etymologischesw00vmuoft (Toronto scan; also Google/bub_gb copies)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft.pdf", 
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
VDQ {"title": "Fereydun Badreh'i (tr.), Vazheha-ye Dakhil dar Qor'an-e Majid (Persian translation of Jeffery FVQ with notes), Toos 1372/1993", "kind": "website", "url": "https://noorlib.ir/book/view/12868?pageNumber=<N>&viewType=pdf (page images; viewType=html also exists) ; info: https://noorlib.ir/book/info/12868 ; ketabnak.com/book/51136 (download blocked)", "lookup_hint": "noorlib viewer is JavaSc
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/
DOZ {"title": "R. Dozy, Oosterlingen: Verklarende lijst der Nederlandsche woorden die uit het Arabisch, Hebreeuwsch, Chaldeeuwsch, Perzisch en Turksch afkomstig zijn, Leiden 1867", "edition_found": "1867", "kind": "archive_djvu", "url": "https://archive.org/details/oosterlingenver00dozygoog", "identifier": "oosterlingenver00dozygoog (also ...01dozygoog, ...02dozygoog)", "local_file": "/home/sfmqrb/git
TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://a
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 =
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_page
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.t
```


## [2026-09-06T15:48:55.801Z] TOOL CALL #5: Bash

```json
{
 "command": "ls data/verification/sources/refs/ | head -60 && echo ---- && sed -n 1,80p tools/verify_check.py"
}
```


### [2026-09-06T15:48:55.848Z] TOOL RESULT

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


## [2026-09-06T15:48:56.557Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/page-202.json'))\nprint(json.dumps(d['entries'][0], ensure_ascii=False, indent=1)[:3000])\n\""
}
```


### [2026-09-06T15:48:58.406Z] TOOL RESULT

```
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
   "where": "Bd. I 675-677 (WLD_Bd1 djvu line 42665 ff., running head 'gʷem-, gʷā-'
```


## [2026-09-06T15:49:05.339Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | sed -n '60,200p'; echo ----; ls incoming/"
}
```


### [2026-09-06T15:49:05.390Z] TOOL RESULT

```
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
SKT.txt
SNS_pages.txt
SNS.txt
SOD_pages.txt
SOD.txt
SPG_keilinschriften1881.txt
SYN.txt
TAD_pages.txt
TAD.txt
tessdata
TLM.txt
UNV.txt
WEB_vol1.txt
WLD_band3.txt
ZAP.txt
----
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
```


## [2026-09-06T15:49:05.931Z] TOOL CALL #8: Bash

```json
{
 "command": "sed -n 1,200p data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-06T15:49:05.972Z] TOOL RESULT

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


## [2026-09-06T15:49:16.662Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== TTS dir ===\"; ls incoming/TTS/\necho \"=== FSD caracal ===\"; grep -n -i \"caracal\" FSD_vol1.txt | head -20\necho \"=== FSD karakulak ===\"; grep -n -i \"karakulak\\|kara.kulak\\|qara\" FSD_vol1.txt | head -20\necho \"=== KLN caracal ===\"; grep -n -i \"caracal\" KLN_1966.txt KLN_1971.txt SKT.txt WEB_vol1.txt LKT.txt | head -30"
}
```


### [2026-09-06T15:49:16.780Z] TOOL RESULT

```
=== TTS dir ===
TTS_pages.txt
TTS_vambery1878_uoft_djvu.txt
TTS_vambery1878_uoft.pdf
=== FSD caracal ===
15683:an"a-ke-Iard',l an'0-ko-lard';2fin*a-ke-lard', n.  (Ar.)  The caracal.
15892:an"a-ke-lard',  1   an*&-ko-lGrd';  2   ftn'a-ke-Uird',  n.  |Ar.]  Tho caracal.
36869:3.  A   building,  apartment,  or  receptacle  for  bathing; as  Baths  of  Caracalla  at  Rome;  public  baths ;   a   porce- lain bath;  specif.  [U.  S.]t  a   fully  furnished  bathroom.
57381:Car'a-bus,  1   karie-bus;  2   efir'a-btis,  n.  Entom.  1.  A   genus typical  of  Carablckv.  2.  [c-1  [-ni,  1   -bal;  2   -bl,  pi.]  A   beetle of  this  genus:  a   carabld.  [   <   Gr.  tarabos,  horned  beetle.] car'a-cal*.  1   kar'o-kal;  2   cfir'a-cXl,  n.  1.  The  Persian lynx  (Fen’s  or  Lynx  caracal)  of  southwestern  Asia  and the  greater  part  of  Africa,  somewhat  larger  than  a   fox, and  uniformly  reddish-brown  above  with  long  upright black  ears  tipped  with  black  hairs.  2.  Its  pelt  or  fur. [F„  <   Turk,  qara  gulag,  black  car.l  car'a-cult. car'a-cal1,  n.  An  ancient  Gallic  outer  garment.
57382:CaracaJIa  .   .   .   distributed  nmonc  the  people  tho  long  Gallio coatfl.  named  Caracals,  whence  ho  derived  the  appellation.
57383:Keioutlet  Roman  Empire  pt.  ii,  p.  209.  [ii.  a.  a   co.  1641.] [<  LL.  caracalla ;   of  Celtic  origin.)
90923:n.  The  caracal.—  d, ‘mouse, n,  A   field-mouse  (Calomys cmnlcus)  of  the  plains  of  the western  United  States.— d.» snake,  n.  A   sand-snake  of Psammophls  or  a   related genus.— Deserts  of  Asia,  a chain  of  deserts  from  south- ern Morocco  to  Yellow  Sea,  _   __
=== FSD karakulak ===
11417:Al"co-ran', )   1   al'Ko-ran';  2   filrco-ran'  (xm),n.  Same  as AI"kt>-ran',  f   Koran.^  [F.f  <   Ar.  ctUqorSn,  <   al,  the,  4-  qaraa,
57381:Car'a-bus,  1   karie-bus;  2   efir'a-btis,  n.  Entom.  1.  A   genus typical  of  Carablckv.  2.  [c-1  [-ni,  1   -bal;  2   -bl,  pi.]  A   beetle of  this  genus:  a   carabld.  [   <   Gr.  tarabos,  horned  beetle.] car'a-cal*.  1   kar'o-kal;  2   cfir'a-cXl,  n.  1.  The  Persian lynx  (Fen’s  or  Lynx  caracal)  of  southwestern  Asia  and the  greater  part  of  Africa,  somewhat  larger  than  a   fox, and  uniformly  reddish-brown  above  with  long  upright black  ears  tipped  with  black  hairs.  2.  Its  pelt  or  fur. [F„  <   Turk,  qara  gulag,  black  car.l  car'a-cult. car'a-cal1,  n.  An  ancient  Gallic  outer  garment.
57574:(oxygen)  +   -yl.]  —   car"box-jTlc,  a.  1.  Of  or  relating to  carboxyl.  2.  Rhodizonic. car 'boy,  1   kar'bei;  2   cSr'bSy,  n.  1.  A   large  globular glass  bottle  enclosed  in  a   box  or  in  wickerwork:  used mainly  for  the  transportation  of  corrosive  acids  and  the like.  2f.  A   demijohn.  [   <   Per.  qarabah,  demijohn.] —   car'll  oyed,  pa.
=== KLN caracal ===
LKT.txt:2563:1081.  Tk.  karakolak: 'Schwarzohr'  ist  der  Name  eines  kleinen Raubtieres  [pers.  ebenso  sijäh  gns 'schwarzes  Ohr'  genannt];  hieraus  dtsch. Karakal,  Felis  caracal  Gmelin  'persi- scher Luchs'.
LKT.txt:4986:Daudet  (Alphonse)  1542 Z)eZ«&as  507 Dipus  aegyptiaeus  936 Dollar  (zeichen)  1996 Domback  2012 Dschiu-Dschitsu  963 Dumdum  477 Dmws  Scotus  1927 Elixir  903 jBmM  1528 d'Entrecolles  1060 Equus  onager  1233 Esdragon  2034 Euphorbia  567 Euphorbus  567 Eusebius  1389 jPeZ«s  caracal  1081 Fe«  596 Floririda  1002 J'ooie  (Samuel)  1542
WEB_vol1.txt:27995:car/a-cal, n. [Fr. caracal; Turk. qara qulaq; qara, black, and qulaq, ear.]
WEB_vol1.txt:27996:1. a lynx, the Lynx caracal, a native of northern Africa and southwestern Asia. Its color is a uniform reddish-brown; its ears blag’ externally, and tipped with long, black
WEB_vol1.txt:27998:2. the fur of the caracal.
WEB_vol1.txt:52944:des’ért lynx, the caracal. É
WEB_vol1.txt:71733:Fé’li-dae, n.pl. [from L. felis, properly feles,acat, and -idz.] animals of the cat kind, a family of carnivora. The incisor teeth are equal; the third tooth behind the large canine in either jaw is narrow and sharp, and these, the car- nassial or sectorial teeth, work against each other like scissors in cutting flesh; the claws are sheathed and retractile. This family in- cludes the domestic cat, wildcat, lion, tiger, leopard, lynx, jaguar, anther, cheetah, ounce, caracal, serval, ocelot, etc.
KLN_1966.txt:6489:carabinieri,  n.  pi.,  the  Italian  police.  —  It.,  pi.  of carabiniere,  fr.  F.  carabinier.  See  carabineer, caracal,  n.,  a  kind  of  lynx.  —  F.,  fr.  Turk,  qarah qulak,  ‘black  ear’.
KLN_1966.txt:37765:sy-,  pref.  —  Gk.  ou-,  form  of  ouv-,  before  a  fol¬ lowed  by  a  consonant  and  before  See  syn-. syagush,  n.,  the  caracal.  —  Pers.-Hind.  siyah- gosh,  lit.  ‘black  ear',  fr.  siyah,  ‘black’,  and  gosh, ‘ear’.  The  first  element  is  rel.  to  OI.  syamah, Avestic  sama,  ‘black’,  and  cogn.  with  L.  cimex, ‘a  bug’,  lit.  ‘the  dark-brown  insect’ ;  see  cimex. The  second  element  derives  fr.  OPers.  gausha-, ModPers.  gosh,  ‘ear’,  which  is  rel.  to  Avestic gaosho-,  ‘ear’,  and  to  OI.  ghosah,  ‘noise’. Sybarite,  n.,  and  adj.  —  L.  Sy  bar  it  a,  fr.  Gk. Su(iapf-nf]?,  inhabitant  of  Sybaris,  fr.  EuflapK;, name  of  a  Greek  town  in  southern  Italy  (now called  Sibari).  The  inhabitants  of  Sybaris  were famous  for  their  luxury,  whence  Sybarite  came to  denote  a  luxurious  person.  —  For  the  ending see  subst.  suff.  -ite.
KLN_1971.txt:39374:caracal, n., a kind of lynx. — F., fr. Turk, qarah 
KLN_1971.txt:238636:syagush, n., the caracal. — Pers.-Hind. siyah -
```


## [2026-09-06T15:49:19.438Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN carbasus ===\"; grep -n -i \"carbasus\\|karpasos\\|karpasa\" KLN_1966.txt KLN_1971.txt | head -30\necho \"=== SYN cotton ===\"; grep -n -i \"karpasa\\|karpāsa\\|kárpāsa\" SYN.txt | head -20\necho \"=== KLN camphor ===\"; grep -n -i \"camphor\" KLN_1966.txt | head -20\necho \"=== LKT kampfer ===\"; grep -n -i \"kampfer\\|kafur\\|kāfūr\\|karpura\" LKT.txt | head -30"
}
```


### [2026-09-06T15:49:19.577Z] TOOL RESULT

```
=== KLN carbasus ===
KLN_1971.txt:32707:influence — cp. burro, carbasus and sbirro. 
KLN_1971.txt:39469:carbasus, n., lint. — L., fr. Gk. xapTiaooi;, ‘flax, 
KLN_1971.txt:213576:— cp. box, the tree, burro , carbasus. 
KLN_1966.txt:5477:bowwow,  n.,  and  intr.  v.  —  Of  imitative  origin, bowyer,  n.,  maker,  or  seller  of  bows.  —  Formed fr.  bow,  ‘weapon’,  with  suff.  -yer. box,  n.,  the  tree.  —  ME.,  fr.  OE.  box,  fr.  L.  buxus (whence  also  It.  bosso,  F.  buis),  fr.  Gk.  tuj^oq, ‘box  tree’,  which  is  perhaps  a  loan  word  of Thraco-Phrygian  origin.  Cp.  next  word,  bushing, Buxus,  and  pyx.  Cp.  also  the  second  element  in arquebus,  blunderbuss.  For  the  change  of  Greek 7c  to  b  in  Latin — which  is  prob.  due  to  Etruscan influence — cp.  burro,  carbasus  and  sbirro. box,  n.,  case,  chest.  —  ME.,  fr.  OE.  box,  orig.  ‘a receptacle  made  of  boxwood’,  fr.  L.  buxum, ‘anything  made  of  boxwood’,  fr.  buxus,  ‘box tree’ ;  see  prec.  word.  Cp.  MDu.  bosse,  busse  and OHG.  buhsa  (whence  MHG.  biihse,  G.  Biichse), which  derive  fr.  VL.  *buxem,  contraction  of *buxidem,  acc.  of  buxis,  which  corresponds  to Classical  L.  pyxis,  ‘box  of  boxwood’,  fr.  Gk. Tvu^lc,  of  s.m.,  fr.  rrj'o?,  ‘box  tree’.  Cp.  also OF.  boiste  (whence  F.  boile),  which  comes  fr. VL.  buxida,  acc.  of  buxis.  Cp.  also  Boxing  day and  bush,  ‘metal  lining’.
KLN_1966.txt:6504:carbasus,  n.,  lint.  —  L.,  fr.  Gk.  xxpnxooc,  ‘flax, cotton’,  which  is  prob.  borrowed  fr.  OI.  kar¬ pdsah,  ‘cotton  brush,  cotton’,  whence  also ModPers.  kirpds,  Arm.  kerpas ,  Arab.  kirbds, Heb.  karpds  (Esther  1:6),  ‘cotton,  fine  linen’. See  Manfred  Mayrhofer,  A  Concise  Etymo¬ logical  Dictionary,  I,  p.174  s.v.  karpdsah.  Ac¬ cording  to  Porzig  in  Zeitschrift  fur  Indologie und  Iranistik,  5,  272  fF. ,  both  OI.  karpdsah  and Gk.  xxpnxcop  derive  from  a  language  of  the Mediterranean  or  Asia  Minor, carbide,  n„  a  compound  of  carbon  with  an  clec- troposil  ive  element  (<7iem.)-  -  See  carbo- and  -ide. carbine,  n.,  a  short  rifle.  —  F.  carabine,  ‘carbine’, fr.  carabin,  ‘carabineer’,  fr.  MF.  calabrim,  fr. ML.  Calabrians,  ‘of,  or  pertaining  to,  Calabria’. Accordingly  the  original  meaning  of  F.  carabine is  ‘(rifle)  made  in  Calabria'.  For  the  ending  sec adj.  suff.  -ine  (representing  L.  -inus). carbinol,  n.,  methanol  or  any  alcohol  derived from  it  (chem.)  —  Coined  by  the  German  or¬ ganic  chemist  Hermann  Kolbe  (1818-84)  in  1868 fr.  curbin  (see  carbon),  a  name  used  by  him  to denote  the  methyl  radical,  and  -ol,  a  suff.  de¬ noting  an  alcohol.
KLN_1966.txt:33881:sayyid,  say  id,  said,  n.,  a  Moslem  title  of  honor, applied  to  the  descendants  of  Husain,  Mo¬ hammed’s  grandson.  —  Arab,  sdyyid,  ‘lord, chief’,  prob.  lit.  ‘speaker,  spokesman’,  and  rel. to  Heb.  sddh,  ‘confidential  talk,  council, counsel’,  Aram.  sewadha,  suwddha  ‘friendly, confidential  speech’.  Cp.  sidi. sbirro,  n.,  an  Italian  policeman.  —  It.,  fr.  Late  L. birrus,  ‘red’,  fr.  Gk.  noppog  (for  *7rup<jf6c), ‘red’,  lit.  ‘fire-colored’,  fr.  nup,  ‘fire’.  See  fire and  cp.  pyre.  For  the  change  of  Greek  tc  to  b  in Latin — which  is  prob.  due  to  Etruscan  influence — cp.  box,  the  tree,  burro,  carbasus. scab,  n.- —  ME.,  of  Scand.  origin.  Cp.  Dan.  skab, Swed.  skabb,  which  are  rel.  to  OE.  sceabb, ‘scab’,  seeafan,  ‘to  scrape,  shave’,  and  cogn. with  L.  scabere,  ‘to  scratch,  scrape’,  scabies, ‘roughness;  itch,  mange’.  See  scabies. Derivatives:  scab,  intr.  v.,  scabb-ed,  adj.,  scabb- ed-ness,  n.,  scabb-y,  adj.,  scabb-i-ly,  adv.,  scabb- i-ness,  n.
=== SYN cotton ===
10029:402 SELECTED INDO-EUROPEAN SYNONYMS 6.24 COTTON NG prapraxe Dan. bomuld Lith.  medvilné, bovelna- It. cotone Sw. bomull Lett. kuokvilna Fr. coton ME cotoun, coton SCr. pamuk Sp. algodén NE colton Boh. bavina Rum. bumbac Du. katoen, boomwol Pol. bawelna NIr. _canach, cadas MHG kattiin, boumwolle Russ. chlopok W. colwm NHG  baumuvolle Skt. karpasa- Br. kotoris
=== KLN camphor ===
6300:Campephilus,  n.,  a  genus  of  woodpeckers  ( orni¬ thol .)  —  ModL.,  lit.  ‘lover  of  caterpillars',  fr. Gk.  xau7rg,  ‘caterpillar’,  and  cpiXoe,  ‘lover, friend’.  See  hippocampus  and  philo-. camphene,  n.,  a  hydrocarbon,  C10H16  (chem.)  — Formed  from  the  abbreviation  of  camphor  and suff.  -ene.
6301:camphine,  n.,  purified  oil  of  turpentine  (chem.)  — Formed  from  the  abbreviation  of  camphor  and chem.  suff.  -ine.
6302:camphire,n.,  i)camphor  (obsol.  or  dial.)',  2)  henna (see  Authorized  Version,  Song  of  Songs  1 : 14). —  A  var.  of  camphor.
6303:camphor,  n.  —  F.  camphre,  fr.  ML.  camphora,  fr. Arab,  kafir,  fr.  OI.  kapphrah,  assimilated  fr. earlier  karpQrah.
6304:Derivatives:  camphor,  tr.  v.,  camphor-aceous, adj.,  camphor-ate,  tr.  v.,  camphor-aled.  cam- phor-ic,  camphor-y,  adjs.
26416:6tco-,  fr.  6716?,  ‘juice’.  See  opium, opodeldoc,  n.,  a  camphorated  soap  liniment (med.)  —  Coined  by  Paracelsus,  prob.  fr.  Gk. ttnoq,  ‘juice’.  See  opium.
=== LKT kampfer ===
5787:Äafta?e  977 iCrtöajg  993 iCa^eZ  766 Zaö(//e  979 ^Tad«  984 ifßtZjne  989 i:fl/f  992 Kaffee  4005 ^^//fe;-  992 Ka filier  j.  1150 Kaftan  774 Kaj>'put(öl)  1142 Kakadu  1Ü17 Kolbehasit  St.  1026 Kalbelazguar  St.  1025 Kalbolacrab  St.  1026 kalekutischer  Hahn  1031 kalemine  mhd.  1149 Kalender  1024 Kalenter  1024 kalfatern  1022 Kaliber  1030 ifaZ//"  798 A'rtZiX-o  1031 Kalium  1029 ifaZ/e  j.  1035 ifaZo«^  1038 Ar<?jjrtfc  1039 Kamel  653 Kamelie  653 Kamelhaut  653 Kamelot(t)  653 Kampfer  1100 Kandare  1051 kandieren  1052 Kandis  fzuckerj  1052 Kantschu(k)  1042 iCao/in  1060 Kap(p)ern  978
```


## [2026-09-06T15:49:31.730Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LKT 1081 ===\"; sed -n '2555,2570p' LKT.txt\necho \"=== LKT kampfer 1100 ===\"; grep -n \"^1100\\.\\|1100\\. \" LKT.txt | head\necho \"=== TAD kafur ===\"; grep -n \"كافور\\|كفور\" TAD.txt | head -20\necho \"=== DOZ kamfer ===\"; grep -n -i \"kamfer\\|kamper\\|kafoer\" DOZ.txt | head -20"
}
```


### [2026-09-06T15:49:31.812Z] TOOL RESULT

```
=== LKT 1081 ===
'Schiefer  [aus  tk.  kara  'schwarz',  s.  hier Nr.  1070,  und  das,  fas  'Stein'] ;  hieraus russ.  karandas,  bulg.  karandas  'Bleislift'.
1077.  Tk.  karagan: 'Steppenfuchs';  hieraus  russ.  karagan 'dass.'.
1078.  Tk.  karagol:
Auch  karakol,  karawul,  karaul  'Wache' [vom  Stamme  kar  'Auge,  sehen',  z.  B. tk.  kara  'Augapfel',  Vämbery  TktElWb S.  78.  Nr.  831];  hieraus  rum.  caraulä 'Wächter,  Schildwache';  bulg.  karaul, karaimil,  karakol  'Wache',  serb.  kara- ula,  karawula  'Wachtturm,  Schilder- häuschen', klruss.  kalawur  'Wacht- mann',  russ.  karaul  'Wache',  karaulka 'Schilderhäuschen'.  [Gorjajew  134. Bern  SlEtWb  489.
1079.  Tk.  karagöz:
Die  lustige  Figur  des  tk.  Schattenspiels, etwa  'Kasperle'  [aus  tk.  kara  'schwarz' und  göz  'Auge'  vom  Stamme  kar,  kor, kör,  köz  'Auge,  blicken'  Vämbery  Tkt EtWb  S.  79,  Nr.  83 II];  hieraus  rum. caraghios  'Possenreißer,  närrisch',  ca- raghioslic  'Possenhaftigkeit,  Spaß' ;  frz. caragueiise  'Marionettenfigur'.  [Ausführ- liches über  die  Figur  des  Karagöz  s. Georg  Jacob ,  Türkische  Literaturge- schichte in  Einzeldarstellungen.  Heft  1. Das  tk.  Schattentheater.  Berlin  1900. S.  19  ff.,  sowie  G.  Jacob,  Die  tk.  Volks- lileratur.  Berlin  1901.  S.  33/34  ]
1080.  Tk.  karakol :
'Schwarze  Hand,  d.  h.  schlechte  Hand- schrift' [aus  tk.  ka7-a  'schwarz'  und  kol 'Arm,  Hand'  vom  Stamme  kar,  kor, kol  'Arm,  Hand,  Spanne',  s.  hier  Nr.  1 1 94] ; hieraus  russ.  karakulja  'Gekritzel,  Krä- henfüße', [nach  MSISI  282]  'verkrüppel- ter Baum'.
1081.  Tk.  karakolak: 'Schwarzohr'  ist  der  Name  eines  kleinen Raubtieres  [pers.  ebenso  sijäh  gns 'schwarzes  Ohr'  genannt];  hieraus  dtsch. Karakal,  Felis  caracal  Gmelin  'persi- scher Luchs'.
1082.  Tk.  karakns:
'Adler'  [aus  tk.  kara  'schwarz'  und  kus 'Vogel'  vom  Stamme  kog,  kow  'jagen, verfolgen',  daher  *kous  >  *kuu§  y  kuS 'Jagd,  Treibjagd,  Jagdvogel'  Vämbery TktEtWb  S."91,  Nr.  95];  hieraus  russ. karagus  Falco  chrysaetos,  serb.  kara- kosa.  [Gorjajew  133.  Mikl SlEtWb  112a.
1083.  Ar.  karam:
'Edelmut,  Güte',  tk.  kerem;  hieraus  rum. cheretn  'Laune,  Gunst'.
1084.  Mal.  karauibil: Ursprünglich  die  Frucht  der  Kokospalme [Pijn  176/177:  'Kokosnuß'],  dann  die
Frucht  eines  ostindischen  Baumes,  Aver- rhoa  carambola  und  A.  bilimbi  [nach  dem ar.Philosophen  MUHAMMAD  IBN  RUSD, verlateint  Averroes  (1126/1198),  be- nannt, vgl.  Brockelmann,  Geschichte  der :ir.  Literatur.  Leipzig  1901.  S.  184/185; bilimbi  aus  mal.  halimbang  'eine  Frucht'] ; hieraus  frz.  caramboUer,  pg.  carambola (auf  den  kanarischen  Inseln  carabeli) [Constancio  Dicc  222  b].  [Devic  DEt 83.    MMM  13.
1085.  Pers.  käränfll: 'Gewürznelke'  [wohl  aus  dem  Sskr.], hieraus  mit  volksetymologischer  Um- bildung gr.  KapuöqpuXXov,  aber  mgr. KapoüjaqpouX,  Kapou|U(pi\;  hieraus  it. garofano,  siz.  galofaru  'Nelke',  frz. giroße  'Nelke',  giroflSe  'Levkoje',  prov. kat.  sp.  girofle,  pg.  girofre  'Nelke',  rum. garoufä,  carofil,  garofil;  aus  dem  Frz. wurde  engl,  gilliflower  [mit  Anlehnung an  flotver  'Blume',  ja  sogar  weiter  noch JuUflower  mit  Verkennung  und  ganz falscher  Deutung  des  ersten  Bestand- teiles] 'Nelke'.  Dtsch.  in  der  Aachener Mundart  Groffelsnagel  'Gewürznelke' [wie  ja  die  Nelke  wie  die  Gewürznelke ihren  Namen  'Nägel'  wegen  ihrer  Ge- stalt erhalten  haben,  z.  B.  engl,  clove, it.  chiovo  di  garofano,  frz.  clou  de  girofle, poln.  gwozdzik  von  gwozdz  'Nagel',  ndl. nagelbloem  und  kruidnagel  und  'Ge- tvilrznägelcheri'  im  Deutschen].  Bulg. kalamfir,  karamfil,  serb.  karatnfil.
=== LKT kampfer 1100 ===
2601:1100.  Sskr.  karpfira:
=== TAD kafur ===
2480:كافور س في اليونانية 1210052 وهو صمغ شجرة تنبت في المند والصين 
=== DOZ kamfer ===
1447:KAMFER.
```


## [2026-09-06T15:49:33.911Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FVQ kafur ===\"; grep -n -i \"kafur\\|Kāfūr\\|camphor\" FVQ.txt | head -20\necho \"=== AFM karbas/kafur ===\"; grep -n \"كرباس\\|الكافور\\|كافور\" AFM.txt AFM_pages.txt | head -20\necho \"=== PLA karbas ===\"; grep -n -i \"karbas\\|kirbas\\|kafur\\|kāfūr\" incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head -30"
}
```


### [2026-09-06T15:49:34.007Z] TOOL RESULT

```
=== FVQ kafur ===
15353:Camphor. 
15395:that camphor came to them from India. 
15411:Mada'in found stores of camphor there and took it for salt, would 
=== AFM karbas/kafur ===
AFM_pages.txt:3475:١‏ الكافور» طيب يكون من شجر مجبال بجر ܐܬܝܥ والصين يلل خلقاً كثيرًا
AFM_pages.txt:3476:وخشبة ابيض هش خفيف جدًا ويوجد في اجوافه الكافور وهو انواع ( يط
AFM_pages.txt:3480:أذ ما في جوفه من الاخشاب وإغلائه :وراشحة الكافور المق: © اللنيؤن ٠‏
AFM_pages.txt:3481:ܐܝ معروف عند لاطا ٠‏ بكافور المولى » ٠‏ وهو ± $0«× 3 ܕ ¢2111[(11012
AFM_pages.txt:3482:بالروممة وكافورى بالتركتة امير بالارامسة و 20111013 بالايطاليانة
AFM_pages.txt:3614:والمسك واللادن والكافورܒܝ <
AFM_pages.txt:5104:كافور ܙ ܙ
AFM_pages.txt:5646:كافورى ܙ ܙ
AFM.txt:5543:١‏ الكافور» طيب يكون من شجر مجبال بجر ܐܬܝܥ والصين يلل خلقاً كثيرًا 
AFM.txt:5544:وخشبة ابيض هش خفيف جدًا ويوجد في اجوافه الكافور وهو انواع ( يط 
AFM.txt:5548:أذ ما في جوفه من الاخشاب وإغلائه :وراشحة الكافور المق: © اللنيؤن ٠‏ 
AFM.txt:5549:ܐܝ معروف عند لاطا ٠‏ بكافور المولى » ٠‏ وهو ± $0«× 3 ܕ ¢2111[(11012 
AFM.txt:5550:بالروممة وكافورى بالتركتة امير بالارامسة و 20111013 بالايطاليانة 
AFM.txt:5744:والمسك واللادن والكافور 
AFM.txt:7868:كافور ܙ ܙ 
AFM.txt:8570:كافورى ܙ ܙ 
=== PLA karbas ===
16513:oLsl kirbäs: "feine weiße Leinwand" pers. a m.Ds karbas 5, syr.
```


## [2026-09-06T15:49:40.816Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LKT 1100 ===\"; sed -n '2601,2625p' LKT.txt\necho \"=== DOZ KAMFER ===\"; sed -n '1440,1470p' DOZ.txt\necho \"=== FVQ camphor ===\"; sed -n '15340,15420p' FVQ.txt"
}
```


### [2026-09-06T15:49:40.887Z] TOOL RESULT

```
=== LKT 1100 ===
1100.  Sskr.  karpfira:
Ein  Baum,  Ginnamonum  Camphora,  aus Formosa  stammend;  schon  präkrit  mit Assimilation  kai)püra;  hieraus  ar.  käfür, Grundwort  für  die  europäischen  Ent- sprechungen: mlat.  camjjhora,  rum. camfora,  it.  (alt)  cafura,  (neu)  cänfora, frz.  caynphre,  sp.  pg.  cänfora,  alcanfor; ndl.  kamfer,  mhd.  gaffer  [ohne  ein- geschobenes m  oder  w!],  r\\i<Msch.  Kam- pfer, engl,  camphor;  luss.kamfora,  bulg. kamfora,  serb.  kamfor,  poln.  kamfora, kanfora,  t&ch.kafr.  [Vgl. ngr. Kaqpoupd.j [DE  84.  Eguilaz  131.  ML  4656.  Kluge 224.  Gorjajew  130/131.  Bern  SlEtWb 468.
1101.  Ar.  karräz:
'Krug  mit  engem  Halse',  also  wohl  ge- eignet, das  Wasser  frisch  zu  halten [vielleicht  aus  dem  Pers.  JA  (8)  I,  545; Lammens  Faruk  961];  hieraus  mit  ar. Art.  sp.  pg.  alcarraza  'irdener  Krug, Wasserkühlgefäß'  [dass.  wie  albarrada, s.  hier  Nr.  249;  DE  86/87],  prov.  alca- razas,  frz.  alcarraza.  —  „Diese  werden von  Frauen  [sc.  Spaniens]  besonders  im Zustande  der  Schwangerschaft  gern  zer- brochen und  gegessen ;  der  Genuß  ihrer Scherben  soll  gleichzeitig  auch  die  Haut weiß  färben."  Dtsch.  Rundschau  für Geographie.  Wien-Leipzig.  XXVH,  126. [Eguilaz  133.  Devic  DEt  7.  Lammens Rem  7/8.    ML  4743.
1102.  Sskr.  karsa:
Ein  Silber-  oder  Goldgewicht  von  '/400 Tulä;  über  tamul.  oder  konkani  käsu wurde  zunächst  pg.  caixa  'Münze  von 3  Reis'  [Constancio  Dicc  204  c]  und hieraus  engl,  cash,  Bezeichnung  für  jede kleine  Münze  in  verschiedenen  Teilen Ostasiens;  in  China  ist  seit  mehr  als zwei  Jahrtausenden  der  runde,  mit  einer zentralen  viereckigen  Durchbohrung  ver- sehene Käsch  typisch.  Über  seine  Ge- schichte vgl.  MÜLLER  in  MSOS  XXH, ostasiat.  Abtlg.  S.  10  ff.  Hobson-Jobson 167/168.
[Ar.  karsana.
1103.  Ar.  karsana:
Name  einer  Pflanze,  entweder  'sciiwarze Wicke,  Vicia  sativa'  oder  'Erve,  Ervum'; hieraus  sp.  alcarcena  [=  yero  'dass.' Dice  Gast  111b;  DE  85].
1 104.  A.r  k3.rtfts  •
Tapier'  [aus  gr.  xäpTti?  ZDMG  LI,  301] ; hieraus  pg.  cartaz  'Anschlag-,  Theater- zettel' [niclit  'Tüte',  wie  ML  1866  hat, dies  heißt  viehnehr  cartuxo],  mit  ar. Art.  sp.  alcatraz,  alcartaz  'Tüte'.  — DE  87.    Eguilaz  134.
1105.  Ar.  ka's: [Wahrscheinlich  aus  aram.  käsä,  dazu vgl.  ass.  käsu  'Becher'  ZAkkFW  34] 'Becher,  Kelcli,  Glas',  ebenso  pers.  käsä; hieraus  rum.  chisea  'Einmachglas'  und vielleicht  russ.  kosuha  'Becher'  [Gorjajew XXXIX].
1106.  Ar.  kas'a:
'Großer  und  tiefer  Napf,  Speiseschüssel für  zwei  Personen',  vulg.  ausgesprochen kafat;  hieraus  siz.  cassala,  eine  Süfsig- keit,  deren  Hauptbestandteile  Butter- milch und  Sandkuchenteig  sind,  eine Spezialität  von  Palermo.  [GrSVociSic  232.
1107.  Hebr.  käsaß:
'Er  hat  abgeschnitten,  zerstückelt';  hier- aus gaunerdtsch.  Katzoff  [mit  anschei- neml  sla  vischer  Endung,  talsächlich  durch die  neuhebräische  Aussprache  des  aspi- rierten h  bewirkt],  Spottname  für  Flei- scher, Metzger.    [Ave-L  IV,  4.50.
1108.  Ar.  kasaba:
'Festung,  Zitadelle'  [vom  Vb.  kasaba, dass.  wie  hier  Nr.  1107;  eigentlich  also 'das  von  der  Stadt  Abgeschnittene,  ab- seits Gelegene'];  hieraus  sp.  alcazaha, pg.  alcagova,  frz.  casbah,  casba,  casauba 'dass.'  [bes.  in  Nordafrika,  z.  B.  die  be- rühmte Kasba  von  Tunis,  vgl.  Bädeker, Unteritalien.".  (1906)  S.  459];  angloind. cnsbah  'Hauptplatz  einer  pergunnah' [s.  hier  Nr.  1633].  [DE  90,  Devic  DEt 87.    Lammens  Rem  79.
1109.  Ar.  kasafa:
'Mit  Geschrei  herumspringen':  von  die- sem Stamme  ar.  *knsaifa  'Ort  der  Aus- schweifung'; hieraus  mit  ar.  Art.  pg. alcoceifa  'Bordell;  Stadtteil,  wo  sich diese  befinden',  [mit  Abfall  der  letzten Silbe]  pg.  alcouce  'BordelP  [Constancio Dicc  46  c;  47  c].
1110.  Ar.  kasd:
'Absicht';  hierzu  adverbialer  Akkusativ kasdan  'absichtlich',  ebenso  präpositio- naier  Ausdruck  'an  kasdin  'absicht- lich', tk.  kasden,  en  kasden;  hieraus bulg.  kästen,  enkasten,  enkast,  serb. käste,  kästen  'absichtlich'.  [Bern  SlEt Wh  492.
1111.  Ar.  kasdir:
'Zinn',  hieraus  gr.  KaoaiTepoi;  und  die slav.  Benennungen  des  Zinns:  bulg. kositro,  kositnn,  serb.  kositar,  kositer; auch  rum.  cositoriü  (Walachei).  [Bern SlEtWb  581.
1112.  Hebr.  käser:
=== DOZ KAMFER ===
KALIEF.
Het Arab. chalïfa, eigenlyk plaatsvervanger, na-
melgk van den Profeet.
KALKOEN.
yj Ealkoenschen, oft kalekutschen haen/' Eiliaan. Men
ziet dus, dat het woord van denzelfden eigennaam ge-
vormd is als calico.
KAMFER.
Het Arab. kdfoer (jJ\S)f dat het PrSkr. kappoerd47
of kdpoerd (Skr. karpoera) is. De n of w, die in een
der Ital. vormen (cafura) en in 't middel-Hoogd. (gaffer)
niet is, is ingeschoven. Sp. alcanfor en canfora, It.
ook canfora, Fr. camphre, en dit is onze vorm.
KANDIJ.
Het Perzisch- Arabische kand («uï), dat den zin heeft,
dien wg aan kandijsuiker hechten, en dat op z^ne
beurt het Indische khanda is; zie Mahn, Etymol. Un-
ters. auf dem Gebiete der roman. Spr., p. 47.
KAFOEBES, KAFOBES.
Is van Joodschen oorsprong. Het wortelwoord (Hebr.
kiffeer of kippeer, nes) beduidt eigenlgk bedekken;
van daar, als men van God spreekt, de zonden be-
dekken, d. i. vergeven, en als men van menschen
spreekt, verzoenen. Kappdra (i-rje^ bij Buxtorf) of
kappora^ in 't Jodenduitsch kappore^ is: reiniging,
verzoening, zoenoffer, en door uitbreiding van beteekenis:
het den ondergang gewgde, verderf, onheil, ongeluk,
dood. In 't Jodenduitsch zegt men: Werd' mein Eap-
pore! in den zin van: du solist meinetwegen verder-
ben! Zie Avé-Lallemant, Das deutsche Gaimerthum,
IV, p. 392, 553, die er by voegt: „Kappore machen^
=== FVQ camphor ===
No. 61). 



246 FOREIGN VOCABULARY OF THE QUR^AN 

^ufc'i we may take it as most probable that the Arabic also was 
borrowed at an early period 2 from the same source. 

jjilj (Jfa/iif). 

Ixxvi, 5. 

Camphor. 

The verse is an early one descriptive of the joys of Paradise, where 

the Commentators were uncertain whether J^O was the name 
of the fountain from which the Blessed drink, or the material used to 
temper the drink (cf. Tab. and Baid. on the verse). 

It is usually taken as an Arabic word (LA, vi, 465), but the variety 

> ' * 

of spellmgg jjitf, j^k, jji-J, and jjii would suggest 

otherwise, and several of the early authorities noted it as a loan-word 
from Persian. 3 

The ultimate source is probably to be found in the Munda dialects 
of India, whence it passed into Dravidian, e.g. Tamil */fu(>/ni, 
Malayalam OgGO, and into Skt., cf. jrfj;. 4 It passed also 
into Iranian, where we find Phlv. \$) Mpur,* which 



gives the Mod. Pers. j^iw, and Arm. .f>ui^i"-p 9 B and into 
Aram, where we find Syr. lioao ? and Maud. K1KDU 8 
It is very probable that the Syriac like the Gk. Kafyovpd is from the 
Iranian, and Addai Sher, 136, would make the Arabic also a borrowing 
from the Persians. The probabilities are, however, that it, like the 
TEth. |)4*C, is to be taken as derived from the Syriac. 9 We find the 

1 Addai Sher, 131. The Persian Lexicons take this to be the source of the Arabic 
word, cf. Vullera, Lex, ii, 769, j^-l <uU ^j** j"U' 

2 It occurs in the early poeta, e.g. Al-A'&ha and 'Alqama. 

3 as-Suyuti, Itrj, 324 ; al-.TawallqT, Mu'arrab, 129 ; al-Khafaji, 170 ; uth-Tha'alibl, 
Fiqh, 318. 

4 For further examples see Laufer, Sitw Iranica, 591. 

6 Justi, Glossary to Bundahesk, 201. The Persian Lexicons, e.g. BQ 9 691, note 
that camphor came to them from India. 

Hubsehrnann, Arm. Gramrn., i, 257. 

7 Also ]>Qaa]D, .0^00, and ])QS&]3, PSm, U688, 3689. 

8 Ndldeke, Hand. Gramm., 112. 

Fraenkel, Vocab, 11 ; Fremdw, 147. 



FOREIGN VOCABULARY OF THE QUR*AN 247 

word in the early poetry (e.g. in al-A'sha), 1 but the story told by 
Baladhurl (ed. de Goeje, 264), that the Arab soldiers who conquered 
Mada'in found stores of camphor there and took it for salt, would 
seem to show that the article was not widely known in Arabia. 

^.AU (Kdhin). 

lii, 29;'lxix, 42. 
A soothsayer. 

It occurs only in the early Meccan period and in a depreciatory 
sense, for Muhammad rejects with some asperity the idea that in
```


## [2026-09-06T15:49:43.114Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PLA karbas ctx ===\"; sed -n '16500,16525p' incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt\necho \"=== PLA kafur ===\"; grep -n -i \"kāfūr\\|kafur\\|Kampfer\" incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head -20\necho \"=== TAD ctx ===\"; sed -n '2470,2490p' TAD.txt\necho \"=== TAD page tag ===\"; grep -n \"كافور\" TAD_pages.txt | head"
}
```


### [2026-09-06T15:49:43.191Z] TOOL RESULT

```
=== PLA karbas ctx ===
-| Pag Pa 
©, - karäzin: Pl. v.o,) karzan q. v. 
u, 7 
sw) _ karäsif: Pl. vo) karsaf q. v. 
/_ _ 4 
OS s°- karakidan: Pl. v.@ı karkadan q. v. 
7 r 
ol» - karäwän: Pl. v.glyj karwän q. v. 
B4 _ v4 
Go! - karäwin: Pl. v. O)z) karwän q. v. 
zu“ kirbäf: "Reitpeitsche" pers. 32, 


oLsl kirbäs: "feine weiße Leinwand" pers. a m.Ds karbas 5, syr. 
es Zarbas 
Ks ‘pP, hebr. 097» ®, 


1. Muhit s. v. 

2. Fraenkel s. v. 

3. Muhit s. v. 

4A. al-MuCarrab s. v., Ellenbogen s. v. 
5. Mackenzie s. v. 
=== PLA kafur ===
15676:BRIH - gäfür: "Kampfer" pers. ec MP. Yıa;»s kapur 7 aram, $,85, Yuan sus » 
15677:mand. gapur °, ar. Lw. käfür, engl. camphor, dtsch. Kampfer. 
16334:ebK- käfür: "Kampfer" pers. = gäfür a. v. 6, 
16337:Se. kafüri: "mit Kampfer bereitet". 
=== TAD ctx ===

كابلا - ايطالي 2ااعومهه معناء معبّد أي كنيسة صغيرة 

كاتدرائية - منسوب الى 06002ادك اليونائي الذي مدا واس و1 سي 
وبراد به كنيشة كرسي المطران لان كرسي المطران أي عرشه نصب بها عادة 

كاويك د نانى وعانادط]ه»! معناء جامع شامل عام 

كاغد -- فارسي 2 كاغد » معناة ورق زمقة 

كافور س في اليونانية 1210052 وهو صمغ شجرة تنبت في المند والصين 
واليابان أ بيض لماع شفاف قابل الاحتراق طب ةو ” 

كامن ل ره معناه خادم الاله 0 6 


0 مهئأه العاضى ا 


5 0 8 8 
كاوتشو -_- امه امريكية براد با المطاط سن مط الشيء 0 وهو سيال 
=== TAD page tag ===
```


## [2026-09-06T15:50:01.192Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== DOZ page markers near 1447 ===\"; sed -n '1400,1450p' DOZ.txt | grep -n \"^[0-9]\\+$\\|^ *[0-9]\\+ *$\" ; grep -n \"^\\s*4[5-9]\\s*$\" DOZ.txt | head\necho \"=== PLA pages for kafur ===\"; grep -n \"gäfür\\|käfür\\|kirbäs\" incoming/PLA/PLA_pages.txt | head\necho \"=== TTS 79 ===\"; grep -n \"kara\\b\" incoming/TTS/TTS_vambery1878_uoft_djvu.txt | head -20"
}
```


## [2026-09-06T15:50:02.231Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON files size ===\"; wc -l MON_part1.txt MON_part2.txt\necho \"=== MON karbas ===\"; grep -n \"کرباس\" MON_part1.txt MON_part2.txt | head -10\necho \"=== MON qareh ===\"; grep -n \"قره قولاق\\|قراقولاق\" MON_part1.txt MON_part2.txt | head -10"
}
```


### [2026-09-06T15:50:02.840Z] TOOL RESULT

```
=== DOZ page markers near 1447 ===
=== PLA pages for kafur ===
12075:BRIH -        gäfür:         "Kampfer"              pers.          ec         MP. Yıa;»s kapur            7    aram,    $,85,        Yuan sus      »
12076:       mand.        gapur             °, ar.       Lw.       käfür,          engl.         camphor,       dtsch.    Kampfer.
12326:5% - gafür = gäfür q. v.
12596:ebK- käfür:                      "Kampfer"                 pers.          = gäfür a. v.                6,
12708:kadhudä                                                                                227                                      kirbäs_
12760:     kirbäs:                         "feine        weiße               Leinwand"                  pers.       a m.Ds   karbas
13292:„IJ           - kawäfir:              Pl.        v. _»\W käfür a. v.
=== TTS 79 ===
5123:alt.    kara  =  sehen;  iJ?a/*aaM  =  Horizont. 
5224:cag.  kara  (wie  oben);  karangJcu  =  ünster;  J^oriim,  leurtm  = 
7879:^o^,  eigentl.  dürr,  trocken,  ganz  so  wie  kara,  ehenfalls 
13796:kara  (Augapfel)  83.
```


### [2026-09-06T15:50:02.974Z] TOOL RESULT

```
=== MON files size ===
  99339 MON_part1.txt
  94500 MON_part2.txt
 193839 total
=== MON karbas ===
MON_part1.txt:22597:بلگ. . نوعی درفش برای قطع کردن کرباس 
MON_part1.txt:56905:خف: 78۲ (.) پارةٌ کرباس و پنبه با گیاه 
MON_part1.txt:58685:منزلگاهی از پارچة کلفت (مانند کرباس و 
MON_part1.txt:83250:شانةٌ کرباس: چوبی که جولاهگان بر هر دو 
MON_part1.txt:92654:کرباس را مثل تازیانه تاب داده بر یکدیگر 
MON_part2.txt:11687:قدک: ۸0۸6:(.) جامةً کرباس رنگین» 
MON_part2.txt:14549:از کرباس و کتان و غیره که بر آن به وسیلة 
MON_part2.txt:15924:پنیه ساخته می‌شده و ظاهراً باید از کرباس 
MON_part2.txt:15930:کرباس صادر می‌شود (تعلیقات معارف 
MON_part2.txt:21636:کرباس: 25 - کر باس هند. کر پاس - 
=== MON qareh ===
```


## [2026-09-06T15:50:09.468Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON2 karbas ctx ===\"; sed -n '21620,21660p' MON_part2.txt\necho \"=== MON page markers sample ===\"; grep -n \"^\\s*[0-9]\\{4\\}\\s*$\" MON_part2.txt | head -5; grep -n \"^\\s*[0-9]\\{4\\}\\s*$\" MON_part2.txt | sed -n '1,3p'"
}
```


## [2026-09-06T15:50:10.416Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== TTS around kara entries ===\"; grep -n \"kara\" incoming/TTS/TTS_vambery1878_uoft_djvu.txt | sed -n '1,40p'"
}
```


### [2026-09-06T15:50:12.090Z] TOOL RESULT

```
=== MON2 karbas ctx ===


کرایه: (۵-)۷672۷۸ [ع.] (.) اجرتی که در 
ازای بارکشی ستور و نشستن در خانه و دکان 
و استفاده از زمین کسی و مانند آن به صاحب 
ستور و خانه و دکان و غبره دهند. کرابة 
خانه: وجهی که در ازای اقامت در خانه‌ای به 
صاحخانه دهند؛ اچاره‌بها. 

کس رایس نشین: 27 [ع. ف. - 
کرایه‌نشیننده] (ص‌فا.) آنکه در خانه و جایی 
که کرایه کر ده» اقامت کند. 

کرب: 12۵ [ع.] (.) اندوه دم گیر» عم 
غصه؛ ج. کروب. (مص‌ل.) دشوار و سخت 
گردیدن غم. (مص ع.) اندوهگین کردن. 
کرباس: 25 - کر باس هند. کر پاس - 
معر. کرپاس ] (ا.) پارچة پنبه‌یی سفید و ارزان 
فیمت. سروته یک کرباس بودن: (عم.) 
مساوی هم بودن؛ معادل هم بودن. 

کرباس محله: (ع)هااهتاهد۲ آه‌ند. ع.] 
(امر.) (عم.) (کد.) قبرستان» گورستان (به 
مناسبت کفن‌های کر باس). 

کربت: ۲002۱ (ع. کربة] (.) اندوه دم‌گیر 
حرن» دلگیری. 

کریق: ۵۵ [معر . کربه» کلبه ] (ا.) خانة 
کوچک. کلبه. ححر 4۵ دکان. 

کر یلا یی : ]--۲۵۲0۵۱8 [عسم. کسبلایی] 
(ص‌نسب.) منسوب به کربلاء. اهل کربلاء» از 
موم کییاد کسی که زیار ی کویاه رن 
باشد» ولو یک بار. (قس. مشهدی). عنوانی 


۳۳۲ فرهنگث فارسی معین کربن 


که روستاییان و عامه را دهند (قس. مشهدی). 
=== MON page markers sample ===
```


### [2026-09-06T15:50:12.140Z] TOOL RESULT

```
=== TTS around kara entries ===
325:aralas-karalai  (Wirrwarr). 
919:=  cuvaschiscb,  kk.  =  koibal-karagassisch,  jak.  =  jakutisch. 
5120:herblicken; ^icar am,  A;araZ  =  Blick,  Umsicht;  karagati  = 
5123:alt.    kara  =  sehen;  iJ?a/*aaM  =  Horizont. 
5126:wie  bisher  fälschlich  angenommen  wurde;  Imraul,  karagnl 
5211:nig.  /[•«»•a  =  schwarz,  finster,  Erde,  gemeines  Volk;  karalcu  = 
5224:cag.  kara  (wie  oben);  karangJcu  =  ünster;  J^oriim,  leurtm  = 
5227:rauben;  karaMt^RÄviber;  A-ij«  =  Pech, dunkelgrau,  Schmuz, 
5234:osm.  karatmah  =  schwärzen ;  karaUi  =  Zwielicht,  halbdunkel; 
5241:alt.  ^rtra  =  schwarz,  böse,  unrein  (oj  karazi  =  der  böse  Haus- 
7879:^o^,  eigentl.  dürr,  trocken,  ganz  so  wie  kara,  ehenfalls 
13792:fcar,  karak,  karku  (Arm)  85. 
13796:kara  (Augapfel)  83. 
13798:karakci  (Räuber)  84. 
13800:karalti  84. 
13802:karamak  83. 
13804:karaul  83.
```


## [2026-09-06T15:50:20.236Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '5100,5260p' incoming/TTS/TTS_vambery1878_uoft_djvu.txt"
}
```


### [2026-09-06T15:50:20.287Z] TOOL RESULT

```
mit  ^'ar  =  sehen  verwandt  zu  sein.  Hieran  wenigstens  er- 
innert das  magy.  s^cm-te^^  gegenüber,  wörtlich:  im  Auge, 


78 

zwischen  dem  Auge,  so  auch  das  persische  ru-he-ru  = 
gegenüber,  wörtlich:  Gesicht  in  Gesicht,  und  das  deutsche 
angesichts. 

83. 

^ar^  /cor,  kör,  UÖZ,  Äuge,  Blich,  sehen,  suchen. 

I.   h-. 

uig.  Jjiarak=kvig&,  Augapfel,  Blick;  ^a^a^ü«  =  der  einen  Blick 
hat,  scharfsichtig. 

cag.  ;J;«»*amaÄ  =  sehen,  suchen;  ^»•«raswaÄ  =  umhersehen,  um- 
herblicken; ^icar am,  A;araZ  =  Blick,  Umsicht;  karagati  = 
Horizont. 

alt.    kara  =  sehen;  iJ?a/*aaM  =  Horizont. 

osm.  hara  (^ö^Äarasy  =  Augapfel ,  und  nicht  Schwärze  des  Auges, 
wie  bisher  fälschlich  angenommen  wurde;  Imraul,  karagnl 
^ Wache,  Schildwache,  Aufseher;  Ä'a»'ffHs'  =  Aufseher,  Die- 
ner; aramah  =  suchen  (vgl.  cag.  IcaramaJc,  von  welchem  der 
gutturale  Anlaut  verschwunden  ist). 

jak.  Jcarai:  =  Auge;  Tfarai  =  ^orge  tragen  (beaufsichtigen;  vgl. 
hahma^  =  sehen  und  Acht  geben). 

kk.    Jearak  (wie  oben). 

CUV.  ^o»*a  =  suchen ,  schauen,  bewachen;  Zrofa?  =  Wache. 

Die  hier  vorliegende  hartlautige  Stammsilbe  kommt  auch 
in  weichlautiger  Form  vor,  und  es  ist  das  cuv.  Jcor,  welches 
als  üebergangspunkt  betrachtet  werden  kann. 

n.  ic—. 

uig.  Jcörmek  =  sehen;  JcörJcütmelc  =  zeigen;  JcöriiJc,  kör  Je  = 
Schönheit  (Ansehnlichkeit?);  JeörMüJc  =  schön,  nett,  zierlich. 

cag.  Jcörmch  {wie  oben);  körsetmeJc,  körlcüzmeh=- zeigen,  sehen 
lassen;  Äö>MsmeÄ  =  sich  sehen,  sich  besuchen;  körilra -^ 
Anblick,  soweit  man  sehen  kann;  körnelc  =  M.nsiev ,  was 
sichtbar  gemacht  wird;  körüMüli  (wie  oben). 

az.    görülcmek=^ sich  zeigen;  grörce/i;  =  schön. 

osm.  görmch  =  sehen;  güriiMi  =  schön;  örncJc  =  Muster  (vgl.  cag. 
Mrnelc). 

jak.  kör  —  sehen ;  körün  =  Ansehen,  Aussehen ;  kördöJc  —  seheus- 
werth ;  köriin  =  Spiegel. 


79 

Kk.    körcrhcn  =  sehen. 

In  der  letztgenannten  Form  der  Stammsilbe   verwandelt 
sich  das  auslautende  v 

a)  in  «  und  s.    So: 

nig.  7i'ö«=Auge;  Jeös)etmclc  =^hüten,  bewachen;  ä;ösM= Spiegel; 

/i'ösoKe/i- =: wünschen  (nach  etwas  sehen,  sich  sehnen), 
cag.  ^•ö«  (wie  oben);  közlemeh,  A-öseime/c  =  Acht  geben,  bewahren, 

aufmerken;    /i*ö3:e?= Geliebte,  Schöne;    /cö^cM^r  =  Guckloch ; 

kösci  =  Wächter, 
osm.  grö«  =  Auge,  Blick;   </ösM7i;OTeii;  =  scheinen ,   sichtbar  werden; 

</MÄeJ  =  schön  (vgl.  Mriik,  Jcörk,  TiözeT). 
jak.  kösün  =  sichtbar  werden;    kösUt  =  erwarten,    beobachten 

(vgl.  Tcösetmck). 
6uv.  Ä;o.s  =  Augc  (vgl.  7i-or  =  sehen);  Jios  /.•«s7«  =  Spiegel;  koslgas 

=  äugeln. 

b)  in  t.    So: 

6ag.  kütmek  =^\miQn,  bewachen,  beschützen;  A;ä^eö7— Festungs- 
commandant, Aufseher,  wovon  das  neupersische  Jcutval 
stammt;  Jcöt  vali,  wie  Budgoff  liest,  ist  daher  nicht 
richtig. 

uig.  fcM?CÄweÄ;  =  bewachen,  beschützen;  A'/7<em  =  Beschützer. 

jak.  fc(«<(«  =  behüten ;  A,'«<«&i7  =  Wächter;  Ä;ä<>  =  das  Bewachen ; 
A"M#=  erwarten. 

CUV.  ä;m«  =  hüten  (eine  Heerde);  /i'Mf?ei  =  Heerde;  7cüdii  =  ge- 
schützter Ort;  A;Mf7e=:  bewachen. 

alt.  käsie  =  sich  hüten;  küt  =  hüten;  kütJce  =  jemand  be- 
wachen. 

84. 

^ai',  \cir ,  1cm%  kur,  schwarz,  trocken,  dürr,  alt, 
Unglück,  Schaden,  Fluch. 

nig.  /[•«»•a  =  schwarz,  finster,  Erde,  gemeines  Volk;  karalcu  = 
blind  (vgl.  aj,  ag  —  oSeu,  hell  mit  «äü  =  weiss  und  half;  — 
sehen);  /faW^w  =  Unglück ,  Fluch,  Schimpf  (vgl.  Icara  hün  — 
Unglückstag;  i«4"a*'a?#»  =  Schmach ,  Schwärze  des  Ange- 
sichts als  Gegensatz  zu  jüz  aldiU  =  Ehre ,  Weisse  des  An- 
gesichts);   korulc  —  ^üvv,  trocken,  leer,  alt;    ^»•  =  Alter; 


80 

leari ^a\t;   A-«WZwaZ;  =  alt  werden;    kurtic,   7mrc  =  alt, 
reif;  kurtha  =  bejahrt. 

cag.  kara  (wie  oben);  karangJcu  =  ünster;  J^oriim,  leurtm  = 
Russ,  Schwärze;  kargu,  kargis  =  Yhic\i\  kargamak tün- 
chen, schimpfen;  l^-araJc  =  üauh ,  Schade;  ItaraJßamak  = 
rauben;  karaMt^RÄviber;  A-ij«  =  Pech, dunkelgrau,  Schmuz, 
Feld  (vgl.  Ära m  =  schwarz  und  Erde);  kor,  kur  =  leer, 
wüst,  Alter,  Zeit;  /ifit»')/^  =  trocken ,  dürr,  leer,  wüst,  un- 
fruchtbar; Ä^fflW  =  Alter,  alt;  karimaJc,  kartaimah  =  a,\iein; 
^<;a»*ca  =  trocken,  gut  ausgebacken;  ktirtit =ha,rte,  getrock- 
nete Käse. 

osm.  karatmah  =  schwärzen ;  karaUi  =  Zwielicht,  halbdunkel; 
k^anga  (eigen tl.  fcar^ra)  =  Zank ,  Streit,  Krieg;  karga  = 
Habe;  T^arakus  —  kilev  (beide  von  der  Farbe  ihres  Ge- 
fieders so  genannt);  karmls,  /?r/W  =  alt,  bejahrt;  kari  = 
Weib  (ursprüngUch  die  Alte,  Schwache,  als  Gegensatz  zu  Jfts 
=  Mädchen,  eigentl.  die  junge  feurige  Weibsperson). 

alt.  ^rtra  =  schwarz,  böse,  unrein  (oj  karazi  =  der  böse  Haus- 
geist); Äraraw^ schadenfroh;  kuracM^ dxmkel,  Zwielicht; 
^•«»•l  =  alt;  /rorom  =  später,  nachher;  /i'M»'5f«= trocken. 

jak.  ^«»"0  =  schwarz,  dunkel,  dicht  (hinsichtlich  der  Analogie 
von  dunkel  und  dicht  vgl.  <omj=  dicht  und  fam  =  finster); 
Jfaruna  =  dunkel ;  Teärä  =  grau ;  kärämäs  =  schwarzgrau ; 
Mrfsagas  =  alt;  A^^W«  =  altern;  /i'a/*a/taw=  Urvater;  kürun 
=  verdorrt;  kür,  küraUn  —  irocken  werden. 

kk.  A-a»*a  =  Acker,  Steppe  (vgl.  cag.  ^7V=Feld),  Nacht,  schwarz; 
kargan,  kergan  =  aXi\  kargärmen,  kargcrhm  — schelten, 
verfluchen;  leer,  7i;e>  =  grau;  /«'«»'^fa  =  Krähe. 

CUT.  i^wra  =  trockenes  Gras;  karcik  =  K].ier. 

In  lautlicher  Hinsicht  ist  der  Zusammenhang  der  gegebe- 
nen Beispiele  auf  den  ersten  Anblick  einleuchtend;  was  die 
Begriifsanalogie  des  l^uru  anlangt,  so  finden  wir  ein  ähn- 
liches Verhältniss  in  dem  entgegengesetzten  Jaj^  =;  feucht ;
```


## [2026-09-06T15:50:35.610Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"فرهنگ فارسی معین\\|فرهنگث فارسی معین\" MON_part2.txt | sed -n '1,10p'; echo ...; grep -n \"فرهنگ فارسی معین\\|فرهنگث فارسی معین\" MON_part2.txt | sed -n '200,215p'; echo \"=== near karbas ===\"; grep -n \"فرهنگ فارسی معین\\|فرهنگث فارسی معین\" MON_part2.txt | awk -F: '$1>21400 && $1<21800'"
}
```


### [2026-09-06T15:50:37.280Z] TOOL RESULT

```
720:فرهنگ فارسی معین ف 
767:غده فرهنگ فارسی معین ۱۱۱ 
846:۲ ۱ فرهنگ فارسی معین غد پر 
981:فرهنگ فارسی معین 
1121:عرد فرهنگ فارسی معین 
1266:فرهنگ فارسی معین 
1315:غرم فرهنگ فارسی معین ۱۷ 
1590:۱۱۳۰ فرهنگ فارسی معین غر بو 
2119:فرهنگ فارسی معین 
2393:فرهنگ فارسی معین تس 
...
72837:فرهنگ فارسی معین 
73172:فرهنگ فارسی معین 
73207:1 فرهنگ فارسی معین نان 
73289:نان فرهنگ فارسی معین 
73416:فرهنگ فارسی معین 
73693:فرهنگ فارسی معین 
74558:فرهنگ فارسی معین 
74645:فص فرهنگ فارسی معین نح 
75001:۱۹۳۸ فرهنگ فارسی معین ندبه 
75222:فرهنگ فارسی معین 
75272:1 فرهنگ فارسی معین 
75359:فرهنگ فارسی معین 
75544:فرهنگ فارسی معین 
75991:فرهنگ فارسی معین 
76335:فرهنگ فارسی معین 
76475:فرهنگ فارسی معین 
=== near karbas ===
21657:۳۳۲ فرهنگث فارسی معین کربن
```


## [2026-09-06T15:50:48.805Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON qareh ===\"; grep -n \"^قره\\|قره:\\|قره ‌\" MON_part2.txt | head -20\necho \"=== MON قراقوش/قره قروت ===\"; grep -n \"قراقوش\\|قره قروت\\|قره‌نی\\|قره نی\" MON_part2.txt | head -20\necho \"=== MON kafur ===\"; grep -n \"کافور:\" MON_part2.txt MON_part1.txt | head"
}
```


## [2026-09-06T15:50:48.877Z] TOOL CALL #22: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:1571 2>&1 | head -60"
}
```


### [2026-09-06T15:50:48.905Z] TOOL RESULT

```
=== MON qareh ===
8024:فقره: «جا (ع. فقرة] (1.) (پز.) هر یک از 
30559:آنقره: (جان.) نژادی از گرب اهلی که دارای 
=== MON قراقوش/قره قروت ===
=== MON kafur ===
MON_part2.txt:8545:فلفل (و) کافور: چون کافور بالخاصيه از 
MON_part2.txt:18828:کافور: ۲56 (ع.) () (گیا.) (بز.) ماده 
MON_part2.txt:18894:(موی) (کد. پیر). گرد کافور: سفید مو (کد. 
MON_part2.txt:33764:و بله. گل کافور: (بز. شیم.) قطعات کافور 
MON_part1.txt:86595:و بویند. شمامهٌ کافور: (کد.) آفتاب و ماه.
```


### [2026-09-06T15:50:57.533Z] TOOL RESULT

```
REF: BQT:1571  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 364  OCR-lang: fas

-۱۵۷۱- کافلو

پعنی بشکافد - و بترکاند - وجتج وکند. نافع باغد و خوردن آن قطع‌شهوت جماع کند.
کاف لو لا ۱4 آشاره بسرور کاینات کافور خوردن - بسکون رای

ملوات ال علیه وله وسلم باشد. کافور + کنایه از عدم رجولیت باشد 8 .
کافور ؟ » بر وزن ناسور , معروف کافوری ۹ * بروزن لاهوری,رستنیی

است وآن دوقسم میباشد : ۱ ۰ باشد که آنرا باپونه کوبند » و هربی اقحوان

یکی ازدرخت‌حاصل میشود ی خوانند ؛ ونوعی ا زکل‌بابونه هم‌هت کهآ نراکل

وآترا جودانه میگوبند و خر ها کاوچشم میگوبند وعریان عبن‌البقر مینامند.آنرا

دیگریهملی ؛ وآن چوبی اه | خعك کرده بایند و با سکنجبین بیاشامند ۰

ِ 2 ۱9

است که میجوشانند واز 40۹ اسهال بلغمکند و پوییدن‌آن خواب‌آورد .

آن بر میآورند» وهر چیر 29 که کاف ولا۴ - کنایه ا زکل است که

سفیدرایز بآن نبت کنندم ۹ 1 کجل هم میگوبند: ‎)٩(‏ - و کنایه از کزاف

- و نام پادشاهی هم بوده ۳ ولاف است چه ا زکاف مراد کزاف و ازلام لاف

بیدا د گر و آدمی خوار و کافور باشد - و دروغ وکذب را نیز کوبند - وکنایه

از ت.
رستم بن زال او را کرفته بجهنم واصل کرد - ی
ونام چشمه‌ایست در بهشت . کافی » بر وزن و معتای کاویدن
۹ 8 با ما۸ اه 8

کافوربار ؟۴ - با بای ابجد بالف است که کندن - وشکافتن۸ - وتفحص وتجس

کشیده وبرای قرشت زده , کنایه ازهرچنز بفایت کردن باشد .

سرد و بیار خوشبوی باشد - و بمعنی برف بار کافیشه - بنتح شین نقطه دار بر وزن

هم هت چه‌کافور پاریدن کنایه از برف باربدن | ماهیچه . بمعنی کاجیره است ‎٩‏ وآن کیاهی باشد

است. . که ا زگل‌آن چیزها رن کنند و از تخم آن
کافور جو دا نه - نوعی از کافور روغ ن گیرند ۰

است بغایت خوشبوی . بوبیدن آن درد سر را کافیلو - با نالك بتحتانی رسیده ولاء

() خم۱ :کل است وکنابه ا زکچل هم هت ۰

۹ - آشاره بحدیث قدسی : لولالماخلقت‌الافلاك . اکرتو (محمدص) نبودی , فلکها را
نمی آ فر‌بدم . ۴ - نام فارسی - عربی مأٌخوذ از ناسکربت 1۳800۳8 - 0۵۳3018076
(ضش) سس اطلاقی دیگرآن ۳ قافور ۳ قفورا (ج.م.) 2 عقار ۹ درپهلوی3007 8 «اوتوالا ۶۸۱
لوفر اصل سانکریت کلمه را ۳8۳0078 نوشته . 585 . 0 , 17881608 - 8180 ؛ کافور
2 گیاهی‌است ازتیرء غاربها 181۳10668 که درچین وژاپون وشمال ابران کاشته‌میشود
و از برکهای آن کافور استخراج میکنند. کل کلاب۲۰۰؛.. ۴ - وهرچیز سرد.

۴ - از: کافور ۳ بار ( بلرنده ). ۵ - چهکافور « قاطع باه > است . ر4 : تحقةٌ
حکیم موّمن . ‎٩‏ < کافوربهودی ۳ کافوربه » ربحان‌الکافور است وتزد بخ ی کافوریه‌اسم
اقحواست. «تحقهةٌ حکم موژمن .۰ ۷ <- کافتن > کاویدن (هم.).
```


## [2026-09-06T15:51:09.086Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== grep قره ===\"; grep -c \"قره\" MON_part1.txt MON_part2.txt\necho \"=== lines ===\"; grep -n \"قره\" MON_part2.txt | head -30\necho \"=== MON kafur entry ===\"; sed -n '18828,18845p' MON_part2.txt"
}
```


### [2026-09-06T15:51:09.180Z] TOOL RESULT

```
=== grep قره ===
MON_part1.txt:96
MON_part2.txt:110
=== lines ===
443:می‌رود. پوست درخت غان نقره رنگ است 
1116:ظرچسی: آ۵: (ص.) کول قرهه‌چی» 
1817:چیزی کم بها در طلا و نقره و مشک و 
2128:نقره. بی‌غل؛ بی‌غل و غش: حیله؛ بدون مکر 
5136:حلقره دو چوبت استادة واد یج بند ند . 1 ۲ 
7347:فسفات‌ها با نیترات نقره رسوب زرد فسقات 
7348:نقره تولید می‌کنند که در اسید از تیک و 
7740:فضی: تا (ص‌نسب.) از نقره (ساخته)» 
8024:فقره: «جا (ع. فقرة] (1.) (پز.) هر یک از 
8027:: . فقر» فقرات. . صح. - فقره که معمولاً (در 
8029:می‌شود» در اصل «فقره» به کسر فاء و سکون 
8031:رفقره» به دو فتح بجز اقیانوس و معیار اللغه 
8033:دیده نمی‌شود. صاحب اقبانوس «فقره» به 
8339:و همه حاجب نور هستند (مگر طلا و نقره 
8649:(سابقاً از طلا و امروزه از نقره) واحد پول 
9214:فوه: ۷۵ (۱.) ورق طلاو نقره و مانند آن که 
9952:روی چیزی کشیدن آب طلا یا آب نقره 
11089:طلا یا نقره وضع نمایند و سواران از یک 
12030:- قره‌سوران - قراسورن] (.) سرهنگ 
12059:فرافروت: ۲۲۵۱ [نر. - قره‌فوروت ] 
12095:قارقورت» قره‌قروت» ترپ» ترف» تلف. 
12108:پهلوی و آن مسکوکی نقره بود به وزن ۲۴ 
12764:تشقرق: جعرق, [تر. - قشقره] (1.) (عم.) 
12870:آنچه از نقره و برنج و جز آن باشد. قسمی 
13716:زن. قفل فرح استر؛ سلقه زر یا نقره که بر 
14072:بیتی يا فقره‌ای واقع شود که هر کدام قلب 
14093:مس پا روی بود و بالای آن طلا یا نقره 
14163:است نرم نقره‌یی و دارای جلای فلزی عالی. 
14528:مختلف است بر روی نقره» ورشو یا فلز 
14547:نقاش. آنکه به روی برنج و نقره و طلا 
=== MON kafur entry ===
کافور: ۲56 (ع.) () (گیا.) (بز.) ماده 
معطر جامدی که از برگک گیاهان از قبیل 


۱۳۲۰ فرهنگ ار سی معین کافور بیکر 


ریحان و بابونه خصوصاً دو نوع درخت بنام 
سیناموموم کامفورا و دریوبالانوپس کامفورا 
که هر دو بنام درخت کافور موسومند و در 
ژاپن و چین و جزایر سوماترا و برنئو و 
هندوچین می‌رویند» استخراج می‌شود. 
ترکیب شیمیایی کافور 0۱۰۲۲۱۱0 می‌باشد و 
از دستةٌ ستن‌های ترپنی می‌باشد و ترکیب 
حلقوی دارد. کافور بصورت منشورهای ۸ 
وجهی سفید و شفاف متبلور می‌شود. قطع 
بلورها کمی مشکل است ولی به سهولت 
پودر می‌شود. (مخصوصاً اگر چند قطره
```


## [2026-09-06T15:51:16.869Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== قولاق ===\"; grep -n \"قولاق\\|قلاق\" MON_part1.txt MON_part2.txt | head\necho \"=== ctx 12020-12110 ===\"; sed -n '12020,12110p' MON_part2.txt"
}
```


### [2026-09-06T15:51:16.936Z] TOOL RESULT

```
=== قولاق ===
MON_part1.txt:15555:اقلاق: 912۷ [ع.] (مص‌م.) بی آرام کردن» 
=== ctx 12020-12110 ===
اردنانس» دژبان و غبره است. 
ترارنامه: (ع‌مصقنر [ع. ف.] (امر.) 
عهدنامه. شر ط نامه. 

قراروم‌دار: ۷۰-6۱-3۲ [ع. ف. - 
قرارمدار ] (عم.) بند و بست. عهد. شرط. 
قراسنقر: ۲۲ [آتر. سنقر ساه ] 
(امر.) (جان.) یکی از گونه‌های سنقر که سیاه 
رنگ است. (کد.) شب لیل. غلام ترکث. 
فراسوراد: 0 ۸۲2 [تر . - شاه را 
- قره‌سوران - قراسورن] (.) سرهنگ 
محافطان قافله» آنکه به سرکردگی گروهی 


فررهنگ فارسی معین 


۱ ۱ 
از جانب یادشاه در راه‌ها نشیند تا قوافل را از 
منازل مخوف به سلامت بگذراند» امنیه. 
خراج قراسوران: نوعی خراج که سابقاً از 
قری و قصبات میگ فتند (قارجاریه). 
قراضه: (م)ست۳مر زع. قراضه ] (.) ریز ه‌های 
زر و سیم و جز آن که وقت تراشیدن برافتد. 
ریزهةٌ هر چیز که از مقراض قطع شده بر 
فد 
قراضصیه: (۵-)21۷۸ ۲۱۲ [ع. قراضبه ] 
(ص‌نسب. امر.) نوعی حلوای سخت و لزج 
که آن را مانند قبیطا سازند» با مغز و بی‌مغز و 
با قیچی آن را به اندازهٌ یک گلوله یا بزرگتر 
پرند (بحر الجواهر). 
فراغجی: آ- ۱۲2 مف. - قراقفجی - 
قرقجی| (ص‌مر.) مأمور قرق و خلوت 
ساختن راه با محلی؛ قر قجی. 
فراقر: ۲ (اصت.) آواز کردن شکم. 
آوازی که از درون شکم شنیده شود. قراقر 
بطن: صدای شکم و روده‌ها بر ۹ 
گازهای موجود در لولةً گوارش که گاهی 
تولید درد شکم شدید می‌کند. شور و غوغا. 
فرافروت: ۲۲۵۱ [نر. - قره‌فوروت ] 
(امر.) ماد نیم جامد تیره رنگی است که در 
حقبقت جوشاندة فلظ شده ات کشکت 
1 آن بدین طریق است که ماست 
را می جوشانند و : یس از غلیظ شدن و به قوام 
آمدن آن را در کیسه‌ای پارچه یی می‌ر یز ند 
و آب‌های تراوش شده از آن را در ظرفی 
جمع آوری می‌کنند. سپس آنچه درون کیسه 
است بصورت گلوله یا بیضی درمی آورند و 
در آفتاب خشکک می‌کنند و قروت و کشکك 
ماستی نامند و آبی که چکیده و در ظرف 
شده باشد در دیگ می‌ریزند و قدری 
شیر با آن می آمیزند و می‌جوشانند و پس از 
آنکه قوام گرفت بصورت قرص 
درمی آورند و چون خشک شد شکننده و به 


۱۳۳۲ فرهنگ فارسی معیر قران 


اصطلاح پوک است و ترشی مطلوب و 
مطبوعی دارد و آن موسوم به ترف و آب 
قروت است. دیگر آنکه دوغ کره را گرفته 
را می‌جوشانند و چون غلیظ شد در کیسه 
می‌ربزند و از مادةٌ جنبی که در کیسه است 
کشک دوغی می‌سازند و از چکیدة آن پس 
از جوشانیدن گلوله‌ها می‌سازند که سرخ 
تيرة مایل به سیاهی است و ترشی آن تند و 
زبان گز است و این نوع را قراقروت و ترف 
سسیاه ن‌امند. این است که سعمول 
گ‌وسنندداران در حدود طبس است 
(فروزانفر. تعلیقات معارف بهاءولد ۱۳۳۸ 
ص ۲۰۲ - ۲۰۳). ترکیب قراقروت بیشتر 
از اسید لا کتک و املاح محلول در آب 
است و ترشی قراقروت نیز بواسطه وجود 
مسقادیر فراوان از همین اسید است؛ 
قارقورت» قره‌قروت» ترپ» ترف» تلف. 
قران: 12۰313 [ع.] (مصل.) نزدیکك شدن؛ 
بهم پیوستن. (نج.) یکجا شدن دو کوکب از 
جملهٌ هفت سباره (قدما) سوای شمس در 
برجی به یک درجه يا به یک دقیقه. (امص.) 
نزدیکی» پیوستگی» اتصال. صاحب قران. 
قران سعدین: (اح. نج.) نزدیکك شدن دو 
سیارة سعد مانندی مشتری و زهره در یکت 
سرج. قران نحسین: (اح. نج.) نزدیک 
گردیدن دو ارف نحس ماد زحل و مریخ 
در یک برج. گذشتن قران: > کش مان 
محنت (به سبب گذشتن قران کواکب) () 
واحد پول ايران در عهد قاجاریه و اوایل 
پهلوی و آن مسکوکی نقره بود به وزن ۲۴ 
نخود معادل یک ریال کنونی. 
فراول: ۷0۷ [تر .| (نظ. قد.) دیدبانی که
```


## [2026-09-06T15:51:31.375Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN page markers around 6300 ===\"; awk 'NR>=6280 && NR<=6520 && (/^[0-9]{3}$/ || /^ *[0-9]{3} *$/)' KLN_1966.txt\necho \"--- explicit ---\"; sed -n '6280,6320p' KLN_1966.txt | grep -n \"^.\\{0,6\\}$\"\necho \"=== search page tags ===\"; grep -n \"^\\s*22[0-9]\\s*$\\|^\\s*23[0-9]\\s*$\" KLN_1966.txt | head -20"
}
```


## [2026-09-06T15:51:32.461Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FSD vol1 page markers near caracal 57381 ===\"; sed -n '57330,57385p' FSD_vol1.txt | grep -n \"39[0-9]\\|CARA\\|Carac\" | head -20\necho \"---\"; awk 'NR>=57200 && NR<=57400' FSD_vol1.txt | grep -n \"^[0-9]\\{3\\}\" | head"
}
```


### [2026-09-06T15:51:32.976Z] TOOL RESULT

```
=== KLN page markers around 6300 ===
230
232
233
234
235
236
237
238
239
--- explicit ---
37:canaba
=== search page tags ===
6158:222
6169:223
6187:224
6188:225
6239:226
6240:227
6276:228
6325:230
6375:232
6376:233
6415:234
6416:235
6469:236
6470:237
6507:238
6508:239
```


### [2026-09-06T15:51:34.611Z] TOOL RESULT

```
=== FSD vol1 page markers near caracal 57381 ===
53:CaracaJIa  .   .   .   distributed  nmonc  the  people  tho  long  Gallio coatfl.  named  Caracals,  whence  ho  derived  the  appellation.
---
57:397
173:511,  App.  [macu.
```


## [2026-09-06T15:51:40.078Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR>=57200 && NR<=57460 {if ($0 ~ /^[0-9]{3}[^0-9]?$/) print NR\": \"$0}' FSD_vol1.txt | head -20\necho \"=== AHD watkins caracal? ===\"; grep -n -i \"caracal\\|karpas\\|camphor\" AHD_watkins1985.txt | head"
}
```


### [2026-09-06T15:51:41.915Z] TOOL RESULT

```
57256: 397
=== AHD watkins caracal? ===
```


## [2026-09-06T15:51:49.195Z] TOOL CALL #28: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-06T15:51:49.205Z] TOOL RESULT

```


```


## [2026-09-06T15:51:51.597Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR>=57256 && NR<=58200 {if ($0 ~ /^ *[0-9]{3} *$/) print NR\": \"$0}' FSD_vol1.txt | head -6\necho \"=== HJB / SKT / WEB carbasus, karpas ===\"\ngrep -n -i \"carbasus\\|karpas\" SKT.txt WEB_vol1.txt HJB.txt IEC.txt | head -20\necho \"=== HRN/HUB karbas, kafur ===\"\ngrep -n -i \"karbās\\|karbas\\|kirbās\\|kāfūr\\|kāpūr\\|kapūr\" HRN.txt HUB.txt | head -20"
}
```


### [2026-09-06T15:51:53.781Z] TOOL RESULT

```
57256: 397
57482: 399
57805: 403
58128: 106
=== HJB / SKT / WEB carbasus, karpas ===
IEC.txt:7702:korpos, å ‘cut, cutter; cutting, sharp; spike, point, crag’. Cf. kerp-, krp- Skt. (ambig.) cf. karparah (‘pot, sherd’. Cf. kerep-); Alb. karpë ‘rock, cliff; LW in Big. kàrpa, id.; Ligurian substr. in Rumansh crap, m. (‘boulder’, w. metath, as in cravun *carbonem', crapenda 'carpenta"); LW (?) in Alb. krep (‘crag’, as doublet of karpë?). Cf. WP II, 581. Here also prob. Ir. corr ‘peak, tip, corner, snout, bill, corn on foot"; W cor, pl. od m. (1) ‘point’; ON herfi ‘harrow’; Sw. harv, f. id. beside hárv, pl. -ar, f. ‘rake’; cf. EMSw. härvel ‘buckle’; Blg. krap, adi ‘short’; Li. karpas ‘cutting, clearing’; karpà ‘slice’; kárpa ‘wart; Latv. kārpa, id.
HJB.txt:5165:CAPAS8,  s.  The  cotton  plant  and cotton-wool.  H.  kapas^  from  Skt. karpasa,  which  seems  as  if  it  must  be the  origin  of  Kdfnraain,  though  the latter  is  applied  to  flax.
=== HRN/HUB karbas, kafur ===
```


## [2026-09-06T15:51:58.968Z] TOOL CALL #30: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/caracal",
 "prompt": "Give the full etymology of \"caracal\" in English, including the French, Turkish (kara kulak / karakulak), and any Persian intermediary. Also any mention of siyah-gush."
}
```


## [2026-09-06T15:52:00.027Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Turkic/kara",
 "prompt": "Give the reconstruction, meaning, and descendants of Proto-Turkic *kara. Also note whether 'old' or 'misfortune' senses belong to this root or to a separate root *karı-."
}
```


### [2026-09-06T15:52:03.766Z] TOOL RESULT

```
# Etymology of "Caracal" in English

The word "caracal" traces through multiple languages. It derives from French *caracal*, which was borrowed from Ottoman Turkish *قره‌ قولاق* (kara kulak, meaning "black ear"). 

This Turkish term is itself "a calque of Classical Persian *سیاه‌گوش* (siyāh-gōš)," according to the source. The modern Turkish *karakulak* maintains this same etymological root, demonstrating how the concept traveled across linguistic boundaries while preserving its original meaning related to the animal's distinctive black ears.
```


### [2026-09-06T15:52:05.538Z] TOOL RESULT

```
# Proto-Turkic *kara

**Reconstruction:** *kara

**Meaning:** The adjective means "black"

**Descendants:** The term has extensive descendants across Turkic language families, including:
- Oghur branch: Chuvash (hura, hora)
- Oghuz branch: Turkish, Azerbaijani, Gagauz, Turkmen
- Karluk branch: Uyghur, Uzbek, Chagatai
- Kipchak branch: Kazakh, Kyrgyz, Tatar, Bashkir
- Siberian branch: Yakut, Tuvan, Khakas, Shor

**Note on other senses:** The webpage provided does not discuss whether "old" or "misfortune" senses belong to this root or to a separate *karı- root. The Etymology section notes that information is "missing or incomplete."
```


## [2026-09-06T15:52:10.629Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/camphor",
 "prompt": "Full etymology of camphor: Medieval Latin camphora, Arabic kāfūr, Persian, Sanskrit karpūra, and any Malay/Austronesian kapur origin. Quote the chain."
}
```


## [2026-09-06T15:52:11.833Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/camphor",
 "prompt": "Full etymology of camphor as given by Etymonline, including Medieval Latin, Arabic kafur, Malay kapur Barus, Sanskrit karpuram."
}
```


### [2026-09-06T15:52:16.715Z] TOOL RESULT

```
# Etymology of Camphor

The word "camphor" traces through several languages in this sequence:

**The etymological chain:**

From Old French *camphore* or Medieval Latin *camphora*, derived from Arabic *kāfūr*, which ultimately comes from an Austronesian source such as Malay *kapur*.

**Direct quote from the source:**

"From Old French *camphore* or Medieval Latin *camphora*, from Arabic *كَافُور* (kāfūr), in turn from an Austronesian word such as Malay *kapur*."

This progression demonstrates how the term traveled westward through trade and cultural exchange, entering European languages via Arabic intermediaries, with roots in Southeast Asian languages where the camphor tree originates.
```


### [2026-09-06T15:52:18.673Z] TOOL RESULT

```
# Etymology of Camphor

According to Etymonline, camphor originated from a fascinating linguistic journey across multiple languages and cultures.

The word entered English in the early 14th century as "caumfre," traveling through Old French "camphre" and Medieval Latin "camfora" before reaching Arabic "kafur." The ultimate source traces back through Sanskrit "karpuram" to Malay (Austronesian) "kapur," meaning "camphor tree."

Etymonline describes camphor as a "whitish, translucent, volatile substance with a penetrating odor, the product of trees in east Asia and Indonesia," which was "extensively used in medicine" historically. The term "Camphorated" is a related derivative from this same etymological root.

This word exemplifies how trade routes and cultural exchange facilitated vocabulary transfer from Southeast Asian languages through the Arab world into European languages, ultimately enriching English.
```


## [2026-09-06T15:52:30.298Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%A9%D8%B1%D8%A8%D8%A7%D8%B3",
 "prompt": "Give the Persian entry کرباس: etymology (Sanskrit karpāsa, Arabic kirbās, Middle Persian), meaning. Also any Arabic entry on the same page."
}
```


## [2026-09-06T15:52:32.184Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%BA%CE%AC%CF%81%CF%80%CE%B1%CF%83%CE%BF%CF%82",
 "prompt": "Ancient Greek κάρπασος: meaning and etymology (Sanskrit karpāsa?), and descendants (Latin carbasus)."
}
```


### [2026-09-06T15:52:34.971Z] TOOL RESULT

```
# Persian Entry: کرباس

**Etymology:** The word inherited its lineage "from Middle Persian, from Sanskrit _कर्पास_ (karpāsa)." The page notes alternative forms include کرواس (karvâs) and کرپاس (karpâs).

**Meaning:** The noun denotes "cotton-cloth, canvas"—a textile material.

**Note on Arabic:** The webpage shown contains no separate Arabic entry for this term, only the Persian definition and linguistic information.
```


### [2026-09-06T15:52:38.309Z] TOOL RESULT

```
# κάρπασος (Ancient Greek Word)

**Definition**: This Ancient Greek noun refers to either flax (*Linum usitatissimum* or *Linum bienne*) or cotton.

**Etymology**: The word was "borrowed from Biblical Hebrew כַּרְפַּס (karpás, 'a type of expensive fabric made of cotton')."

**Grammatical Details**: It's a feminine noun following the second declension pattern, with the genitive form being καρπάσου.

**Pronunciation**: The word is transliterated as *kárpăsos* and pronounced /kár.pa.sos/ in 5th century BCE Attic Greek.

**Related Terms**: The entry lists connected words including κάρπᾰσον (a type of plant) and compound forms like ξῠλοκάρπᾰσον.
```


## [2026-09-06T15:52:49.394Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD karbas ===\"; grep -n -i \"karpas\\|karbas\\|kirbas\" PHD.txt PHD_mackenzie.txt NYB_vol2_glossary.txt | head\necho \"=== PHD kapur ===\"; grep -n -i \"kāpūr\\|kapur\" PHD.txt PHD_mackenzie.txt NYB_vol2_glossary.txt | head\necho \"=== HRN/HUB ===\"; grep -n -i \"karbas\\|karpas\\|kafur\\|kapur\" HRN.txt HUB.txt ARB_mo3rb.txt AFA.txt | head -20"
}
```


### [2026-09-06T15:52:49.484Z] TOOL RESULT

```
=== PHD karbas ===
PHD.txt:424:kaman [kin’n' | = M, N ~] bow. 5; 7 ~dar [-d'] | N ~] archer, bowman. ha er mae 4 ba kamar [kml | N —] waist; belt, girdle. ~-band [-bnd | N ~] belt. kāmģār [Emil | P k?*mg?*r, N ~] powerful, absolute. kamist [Amyst'] least. —jh: pad ~ih, at least. kāmistan, kām- [YCBEN-stn' < A ysbh, V shh; k*m-(y)stnt M k*m-yst] want, desire. kám|-rawág [km izvb*k! | N ~rawa] successful. ~-Z1(w)isn [-zywsn'] free, independent. kam-zór [kmzwl | N ~] weak. ~ih: weakness. kan-, v. kandan, kanar [kwl | N ~] side, edge; embrace. ~ag [-k' | M kr?rg, N ~a] edge, limit, boundary. --agómand [-k’wmnd | M -gwmnd] limited, finite. kandan, kan- [HPLWN-tn! < А V hpr; kn-dn', -tn! | M knd, N ~] dig; raze, destroy. kanig [knyk! | M knyg] girl, maid. kanizag [knyck! | M knycg, N kaniz(ak)] — kanig. kantigr [kntgl] quiver. kāpūr [ро | Ar. kāfūr] camphor. kar-, v. kardan. 1Kar [21 | M Pr, N ~] work, deed, affair. ~ framüdan: put to use. 2kàr [%'7], pl. —àn: (other) people. зкаг [%'/] butter. kār-, v. kištan. karafs [klips | N ~] celery. kār-āgāh [РА | N ~] skilled, experienced. ~ih: skill, experience. karak [krk! | N ~] quail. karan [kľn' | P bein, N ~] side, edge, end, limit. kārawān [%?/zv?x! | P k*rw'n, N kārwān] caravan, military column. ~ig [-yk! | N ~7] caravaneer, traveller. karb [klp] priest hostile to Zoroaster. karbāš [5/0 | N karbas, etc.] lizard. karbunag [k/pnk!, klbnk'] lizard. kard [krt! | M kyrd, N ~] action; matter, affair. кага [SK YN A < A skyn’; Kit! | N ~] knife. ikardag [kltk!] division, section, portion. *kardag [krtk!, kltk! | N karda] action. kārdāg [k'/d?k'] traveller, wanderer, migrant. kardaģān [Art-, Rlt&?n! | M kyrdg”n) action. kardagàár [Artk?l | M kyrdg’r, № ~] mighty. C 6084 E
PHD.txt:2651:lizard karbaS, karbunag.
PHD_mackenzie.txt:3214: karbas [klb'f I N karbaf, etc.] lizard.
PHD_mackenzie.txt:7013:lizard karbas, karbunag.                 maid kanig, kanizag, paristar.
PHD_mackenzie.txt:9513:kardagan              \'-'~~'         karbas
=== PHD kapur ===
PHD.txt:424:kaman [kin’n' | = M, N ~] bow. 5; 7 ~dar [-d'] | N ~] archer, bowman. ha er mae 4 ba kamar [kml | N —] waist; belt, girdle. ~-band [-bnd | N ~] belt. kāmģār [Emil | P k?*mg?*r, N ~] powerful, absolute. kamist [Amyst'] least. —jh: pad ~ih, at least. kāmistan, kām- [YCBEN-stn' < A ysbh, V shh; k*m-(y)stnt M k*m-yst] want, desire. kám|-rawág [km izvb*k! | N ~rawa] successful. ~-Z1(w)isn [-zywsn'] free, independent. kam-zór [kmzwl | N ~] weak. ~ih: weakness. kan-, v. kandan, kanar [kwl | N ~] side, edge; embrace. ~ag [-k' | M kr?rg, N ~a] edge, limit, boundary. --agómand [-k’wmnd | M -gwmnd] limited, finite. kandan, kan- [HPLWN-tn! < А V hpr; kn-dn', -tn! | M knd, N ~] dig; raze, destroy. kanig [knyk! | M knyg] girl, maid. kanizag [knyck! | M knycg, N kaniz(ak)] — kanig. kantigr [kntgl] quiver. kāpūr [ро | Ar. kāfūr] camphor. kar-, v. kardan. 1Kar [21 | M Pr, N ~] work, deed, affair. ~ framüdan: put to use. 2kàr [%'7], pl. —àn: (other) people. зкаг [%'/] butter. kār-, v. kištan. karafs [klips | N ~] celery. kār-āgāh [РА | N ~] skilled, experienced. ~ih: skill, experience. karak [krk! | N ~] quail. karan [kľn' | P bein, N ~] side, edge, end, limit. kārawān [%?/zv?x! | P k*rw'n, N kārwān] caravan, military column. ~ig [-yk! | N ~7] caravaneer, traveller. karb [klp] priest hostile to Zoroaster. karbāš [5/0 | N karbas, etc.] lizard. karbunag [k/pnk!, klbnk'] lizard. kard [krt! | M kyrd, N ~] action; matter, affair. кага [SK YN A < A skyn’; Kit! | N ~] knife. ikardag [kltk!] division, section, portion. *kardag [krtk!, kltk! | N karda] action. kārdāg [k'/d?k'] traveller, wanderer, migrant. kardaģān [Art-, Rlt&?n! | M kyrdg”n) action. kardagàár [Artk?l | M kyrdg’r, № ~] mighty. C 6084 E
PHD.txt:5052:kimaghanjamih "age ” 425 kāmagxwadāy ^A pr 563 kāmgār > 56 8 1-2kāmag ($e 3 kāmagwidār ` 156 3 kāmrawāg 1 ө» e 4 kāmistan uerg s kastar `, Let 4 kástan 101635 4 kāč Q» 5 kābēn wars kāpūr N vays kādag Y4ve» 5 wast 25 A wasxwüstag 1341223920 эу "kay 24 drat “ys drodádwarih! >) мео 5 у kch SIE kahist 1825-65 4
PHD_mackenzie.txt:3196:kapur [k'pwl I Ar. hafur] camphor.
PHD_mackenzie.txt:6141:camphor kapur.                          chance (v.) Jastan.
=== HRN/HUB ===
HUB.txt:4541:besagt bei einem Fremdwort (skr. karpasa-, gr. Tidpnaaog,
HUB.txt:6637:np. nafa, phL nafak; Kapur *Kampfer* (Moses, Geogr.) =
HUB.txt:6638:np. kafur; apsos Vehe, ach!' (13. Jhd.) = np. afsds; mit
```


## [2026-09-06T15:52:57.779Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HUB 4530-4560 ===\"; sed -n '4525,4560p' HUB.txt\necho \"=== HUB 6625-6650 ===\"; sed -n '6625,6650p' HUB.txt\necho \"=== HUB page markers ===\"; awk 'NR>=4400 && NR<=4560 {if ($0 ~ /^ *[0-9]{1,3} *$/) print NR\": \"$0}' HUB.txt | tail -3"
}
```


### [2026-09-06T15:52:59.660Z] TOOL RESULT

```
=== HUB 4530-4560 ===
hih = phi. v9h zu erklSren, nicht aber mih und kih (= phi. m-£ und k^s.)
H&bsohmann, Persisohe Studien. 9— 130 —
§ 7. Wie hier bei mh und deh arm. e dem mp. e (e)
= np. i genau entspricht, so konnte auch noch in andern
Fallen ein mp. e auf Grund des Armenischen angenommen
werden, da, wie oben bemerkt, die Armenier pers. a regel-
massig durch a wiedergeben. So kann z. B. naeh -kert
(2. Glied zahlreicher Komposita) = np. -gird, gr. -xf(?ra,
-ysgdfjg (vgl. Valarsakert == Vologesocettay TiyQavcxs^ra, arm.
Yazkert = np. Yazdegird, arab. Yazdajird, gr. 'ladiysgdjjq;
arm. aSakert 'Schiller* — np. sagird; arm. dastakert *An-
siedelung* = mp. AaatayB()d, arab. dastajird oder daskara
Tab. 295 u. s. w.) ein phi. -A;er^ angesetzt werden, das aber
nicht auf al teres -kart sondern auf -krt = ap. krta- (zd.
kereta-, skr. fcrto-) zuriickgehen wird. Die Uebereinstimmung
von arm. kerpas 'feines Linnen mit np. kirpas^ arab. kirhas
besagt bei einem Fremdwort (skr. karpasa-, gr. Tidpnaaog,
lat. carbasus etc.) nicht viel. In den ubrigen Fallen steht
dem arm. e im Persischen nicht e =- i gegeniiber:
Dareh *Darius' = ap. DGrayava(h)vSj phi. Daraydv^
np. DaraVj Ddra ; Xoream, Xorean = arab. Farruhan^ Xora-
han; Nerseh = phi. inschr. N(a)rs(a)M, syr. NarsB, Narsai,
gr. Nagoijg^ pers. NarsS^ vgl. zd. nairydsatiha'^ skr. naragqsa-;
anderjapet^ handerjapet neben andarj 'Testament' = np.
aw(for;e; awvat;er 'unglaubwiirdig', vaver glaubwiirdig, np.
havar *Glaube ; derjak 'Schneider, np. darzT ; kerp 'Form' =
zd. kehrp, phi. k(a)rp; cermak Veiss' (Pferd) = np. darma
'Schimmel*; patker *Bild' = np. paikar; -ker 'machend' (2. Glied
zahlreicher Komp.) = np. -gar. In diesen Wortern steht e
vor h und r. Ausserdem: Spandaramet (fiir gr. /liowaoQ)
= zd. speflta CLrmaiti, np. sipanddrmaS, syr. Ispanddrmed
(Hoffmann, Ausz. p. 128); gmbef'KuippeV = np. gunha6
(aus dem Syrischen, Noldeke, Pers. Stud. II. 41); pet
*Oberhaupt, Chef* (selbstandig und als 2. Glied zahlreicher
Komposita) = np. -bad, -hud, bei Pro cop -^ddrjq, -^edrjg
(Lag. G. A. 185); ahekan (ein Monat) = arsac. *S^raian?;
=== HUB 6625-6650 ===
Xorrazad (Hamza), Farruxzad und Xorazad Tab. 395;
Xorox'Ormizd (Sebeos) = Farrux-Hormizd Tab. 394, phi.
Farr-Ohrmazd ZDMG. 44, 669; Xorohhut (Mos. Xor. 150)
= phi. Farraxvhut Horn, Sassan. Siegelst. 25.
d) durch p in: par-K 'Ruhm, Herrlichkeit', np. farr
'Glanz, Jifajestat' = ap. farnah-; Pharnerseh (Mos. Xor.),
verkiirzt PharSn (Faustus v. Byz.), ein armenischer Ka-
tholikos, p. farr und phi. N(a)rs(a)hi:; i Pharavazeank (lies
Pharnavazeank) die georgische Konigsfamilie (Faustus v.
Byz.), Pharnavaz (Sebeos p. 6), gr. ^aQvdpaC,ogyPharsman
(Elise, Laz. Pharp., Mos. Xor.) = gr. ^agaa/Lidvrjg; napak
Moschusbeutel', Moses, Geogr. ed. Soukry p. 44, 7 v. u..^ 188 —
np. nafa, phL nafak; Kapur *Kampfer* (Moses, Geogr.) =
np. kafur; apsos Vehe, ach!' (13. Jhd.) = np. afsds; mit
p fiir p: Apzut-Kavat 'eine Mauer im Kaukasus* (Moses,
Geogr. ed. Soukry p. 27) = phi. afzut + Kavat,
Die letzten Worter (von nap ah an) sind spat bezeugt
und spat oder doch relativ spat entlehnt. Der Name Phars-
man scheint mir aus dem Griechischen genommen zu sein
(griech. anl. ^ wird regelmassig durch p = ph umschrieben).
Auch Pharnavaz ist vielleicht erst in sassanidischer Zeit
aus einer nicht-persischen Quelle genommen. Dagegen ist
par~lc alt und haufig bezeugt und wenn mit pers. farr
identisch, in alter Zeit aus dem Mp. entlehnt.
Kapitel 15: ap. f.
Ap. t (= idg. t) = np. ^, d und y.
=== HUB page markers ===
```


## [2026-09-06T15:53:11.969Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== ARY ===\"; grep -n \"کرباس\\|کافور\\|کرپاس\" incoming/ARY/ARY_pages.txt | head\necho \"=== BQT karbas ===\"; grep -n \"کرباس\" incoming/BQT/BQT_v4_pages.txt incoming/BQT/BQT_v3_pages.txt | head\necho \"=== SIN (Sino-Iranica) camphor ===\"; grep -n -i \"karpura\\|camphor\" SIN.txt | head -10\necho \"=== ARB mo3rb kirbas ===\"; grep -n \"كرباس\\|الكرباس\" ARB_mo3rb.txt ARB_abdulraheem.txt KFL.txt | head"
}
```


### [2026-09-06T15:53:12.092Z] TOOL RESULT

```
=== ARY ===
=== BQT karbas ===
incoming/BQT/BQT_v3_pages.txt:29635:‏)1( خم۱: هلندور. . (۲) خم۱:کرباسو ‎ .‏ (۳) خم۱: کرباسه ‎ .‏ (4)خم۱:کرباسو.
incoming/BQT/BQT_v3_pages.txt:29643:۵ - کرباسکه ‏ کربانو  ‎MAS ESR Se SOUS‏
incoming/BQT/BQT_v3_pages.txt:29646:. ۱ - مبکند هم نپنگرا رامو "مره عقرب بود زکرباسو ۰ آتری طوسی « فرهنگه نظام >.
incoming/BQT/BQT_v3_pages.txt:29680:بمعنی کرباسه است که چلباسه.و وزغه باشد.
=== SIN (Sino-Iranica) camphor ===
107:Alum,  p.  474. — Lac,  p.  475. — Camphor,  p.  478. — Aloes,  p.  480. — Amomum,  p.  481. — P,  o-lo-te,  p.  482. — Psoralea,  p.  483.— Ebony,  p.  485.
175:others  of  this  genus,  they  call  salad  (terak  or  tdrak,  Persian  tar  ah). Whatever  is  like  spinning  cotton,  and  others  of  this  genus,  they  call clothing  plants  (jdmak).  Whatever  lentil  (mafag)  is  greasy,  as  sesame, dutedh,  hemp,  vandak  (perhaps  for  zeto,  'olive,'  as  Anquetil  supposes, and  Justi  assumes),  and  others  of  this  genus,  they  call  an  oil-seed (rokano).  Whatever  one  can  dye  clothing  with,  as  saffron,  sapan-wood, zalava,  vaha,  and  others  of  this  genus,  they  call  a  dye-plant  (rag). Whatever  root,  or  gum  (tuf),  or  wood  is  scented,  as  frankincense (Pazand  kendri  for  Pahlavi  kundur),  vardst  (Persian  barghast),  kust, sandalwood,  cardamom  (Pazand  kdkura,  Persian  qaqulah,  'cardamoms, or  kakul,  kdkul,  'marjoram')?  camphor,  orange-scented  mint,  and others  of  this  genus,  they  call  a  scent  (bod).  Whatever  stickiness comes  out  from  plants  they  call  gummy  (vadak).  The  timber which  proceeds  from  the  trees,  when  it  is  either  dry  or  wet,  they call  wood  (Zihd).  Every  one  of  all  these  plants  which  is  so,  they  call medicinal  (ddruk).
1851:The  Geography  of  the  Ming  (Ta  Min  i  Vuh  Zi)  states  that  galls  are produced  in  the  country  of  the  Arabs  (Ta-si)  and  all  barbarians,  and that  the  tree  is  like  the  camphor-tree  (Laurus  camphor  a),  the  fruits like  the  Chinese  wild  chestnuts  (mao-li  ^  W) .
2908:62.  The  Malayan  Po-se,  further,  produced  camphor  (Dryobalanops aromatica),  as  we  likewise  see  from  the  Yu  yan  tsa  tsu,7  where  the  tree
2917:The  Malayan  Po-Sb — Lac,  Camphor  479
2918:is  ascribed  to  Bali  §1  ^'J  (P'o-li,  *Bwa-li)1  ancl  to  Po-se.  Camphor  is not  produced  in  Persia;2  and  Hirth3  is  not  justified  in  here  rendering Po-se  by  Persia  and  commenting  that  camphor  was  brought  to  China by  Persian  ships.
2924:2  Schlimmer  (Terminologie,  p.  98)  observes,  "Les  auteurs  indigenes  persans recommendent  le  camphre  de  Borneo  comme  le  meilleur.  Camphre  de  menthe, provenant  de  la  Chine,  se  trouve  depuis  peu  dans  le  commerce  en  Perse."  Camphor was  imported  into  Slraf  (W.  Ouseley,  Oriental  Geography  of  Ebn  Haukal,  p.  133; G.  Le  Strange,  Description  of  the  Province  of  Fars,  p.  42).
3547:s  There  are  a  few  other  Indian  names  of  products  formed  with  "China": clnapitfa  ("minium"),  clnaka  ("Panicum  miliaceum,  fennel,  a  kind  of  camphor"), clnakarpura  ("a  kind  of  camphor"),  clnavanga  ("lead").
4068:46(483).  kafur  (Arabic  and  Persian),  camphor  (Laurus  camphor  a). The  same  word  appears  already  in  Middle  Persian.   Skr.  karpura.
4130:49.  ga-bur,  camphor.  Sir  George  A.  Grierson  (see  below)  observes, "The  softening  of  initial  k  to  g  is,  I  think,  certainly  not  Indian."  The Tibetan  form  has  always  been  a  mystery  to  me:  it  is  not  only  the  initial g,  but  also  the  labial  sonant  b,  which  are  striking  as  compared  with  the surds  in  Skr.  karpura.  As  is  well  known,  this  word  has  migrated  west- ward, the  initial  k  being  retained  everywhere:  Persian-Arabic  kafiir (Garcia:  capur  and  cajur),  Spanish  alcanfor  (Acosta:  canfora).  These forms  share  the  loss  of  the  medial  r  with  Tibetan.  This  phenomenon pre-existed  in  Indian;  for  in  Hindustani  we  have  kapiir,  in  Singhalese kapuru,  in  Javanese  and  Malayan  kdpur.  The  Mongols  have  adopted from  the  Tibetans  the  same  word  as  gabur;  but,  according  to  Kovalev- ski  (p.  2431),  there  is  also  a  Tibeto-Mongol  spelling  gad-pu-ra:  this can  only  be  a  transcription  of  the  Chinese  type  %  ft  %k  kie-pu-lo, anciently  *g'ia5-bu-la,  based  on  an  Indian  original  *garpura,  or ♦garbura.  Tibetan  ga-bur,  of  course,  cannot  be  based  on  the  Chinese form;  but  the  latter  doubtless  demonstrates  that,  within  the  sphere  of Indian  speech,  there  must  have  been  a  dialectic  variant  of  the  word  with initial  sonant.
=== ARB mo3rb kirbas ===
```


## [2026-09-06T15:53:12.471Z] TOOL CALL #39: WebSearch

```json
{
 "query": "Beekes κάρπασος karpasos etymology Sanskrit karpāsa Hebrew karpas cotton Greek"
}
```


### [2026-09-06T15:53:22.563Z] TOOL RESULT

```
Web search results for query: "Beekes κάρπασος karpasos etymology Sanskrit karpāsa Hebrew karpas cotton Greek"

Links: [{"title":"carbasus - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/carbasus"},{"title":"H3768 - karpas - Strong's Hebrew Lexicon (ylt)","url":"https://www.blueletterbible.org/lexicon/h3768/ylt/wlc/0-1/"},{"title":"H3768 - karpas - Strong's Hebrew Lexicon (LSB)","url":"https://www.blueletterbible.org/lexicon/h3768/lsb/wlc/0-1/"},{"title":"H3768 - karpas - Strong's Hebrew Lexicon (LS)","url":"https://www.blueletterbible.org/lexicon/h3768/ls/wlc/0-1/"},{"title":"H3768 - karpas - Strong's Hebrew Lexicon (KJV)","url":"https://www.blueletterbible.org/lexicon/h3768/kjv/wlc/0-1/"},{"title":"κάρπασος - Ancient Greek (LSJ)","url":"https://lsj.gr/wiki/%CE%BA%CE%AC%CF%81%CF%80%CE%B1%CF%83%CE%BF%CF%82"},{"title":"Strong's Hebrew: 3768. כַּרְפַּס (karpas) -- Fine linen, cotton","url":"https://biblehub.com/hebrew/3768.htm"},{"title":"Karpas","url":"https://en.wikipedia.org/wiki/Karpas"},{"title":"Series 2 - Shiur 19 - Karpas.dwd","url":"https://www.ou.org/holidays/files/Halachic-and-Hashkafic-Issues-OU-Series-2-Shiur-19-Karpas.pdf"},{"title":"Karpos","url":"https://en.wikipedia.org/wiki/Karpos"}]

Based on the search results, here's what I found regarding the etymology of κάρπασος (karpasos) and its related forms:

The Greek word κάρπασος (kárpasos, "cotton") was borrowed from Biblical Hebrew כַּרְפַּס (karpás, "fabric of cotton"), which itself came from Sanskrit कर्पास (karpāsa, "cotton"). However, there's some scholarly debate about the ultimate origin.

κάρπασος is considered as a loan from Indian languages, though according to some scholars like Porzig, the origin may be a Mediterranean or Anatolian language. More probably, the word came from Indian; there is no connection with the plant κάρπασον.

The word traveled through multiple languages: from Sanskrit to Hebrew to Greek, and the same Sanskrit word has resulted in the Latin term gossypium ("cotton"). From κάρπασος, the Latin carbasus was derived.

It's worth noting that while the Passover ritual word "karpas" shares the same Hebrew spelling, the karpas referring to the vegetable (parsley or celery) was originally borrowed from the Persian word karafs meaning celery, and the pronunciation "karpas" may be a linguistic corruption due to misvocalization with the similar Hebrew word meaning cotton.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-06T15:53:33.523Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%83%D8%A7%D9%81%D9%88%D8%B1",
 "prompt": "Arabic كافور (kāfūr): meaning and etymology — is it from Middle Persian kāpūr / Persian, or from Sanskrit karpūra, or Syriac? Quote the etymology section. Also list Persian entry if present."
}
```


## [2026-09-06T15:53:35.794Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E0%A4%95%E0%A4%B0%E0%A5%8D%E0%A4%AA%E0%A5%82%E0%A4%B0",
 "prompt": "Sanskrit कर्पूर (karpūra): meaning, etymology (Austronesian/Malay kapur?), and descendants (Prakrit kappūra, Middle Persian, Arabic, Greek)."
}
```


### [2026-09-06T15:53:41.642Z] TOOL RESULT

```
# Etymology of Arabic كافور (kāfūr)

## Etymology Source
According to the Wiktionary entry, the word has two proposed etymologies:

**Etymology 1** (the primary source): "Possibly borrowed from Middle Persian 𐭪𐭠𐭯𐭥𐭫 (kʾpʿl /⁠kāpūr⁠/), borrowed from an Austronesian language, from Proto-Austronesian *qapuʀ."

The entry notes this traces through Middle Persian to ultimately Austronesian origins, comparing it to Malay *kapur*.

**Etymology 2**: Proposed Aramaic origin related to palm inflorescence parts, suggesting connections to Semitic roots meaning "covering."

## Sanskrit Connection
The document does **not** mention Sanskrit *karpūra* as a source. The etymological chain presented goes: Proto-Austronesian → Middle Persian → Arabic, with an alternative Aramaic hypothesis.

## Persian Entry
No separate Persian entry is provided in this Wiktionary page, though Persian کافور (kâfur) is listed as a descendant of the Arabic term in the etymology section.
```


### [2026-09-06T15:53:44.385Z] TOOL RESULT

```
# कर्पूर (Karpūr) - Camphor

Based on the Wiktionary entry, **कर्पूर** is the Sanskrit and Hindi word for camphor.

## Key Information

**Definition:** In both Sanskrit and Hindi, कर्पूर refers to "camphor," an aromatic substance.

**Etymology:** The word has interesting linguistic origins. According to the source, it is "probably of Austroasiatic origin" or alternatively "a borrowing from Proto-Malayic *kapur," which traces back through Proto-Malayo-Polynesian and Proto-Austronesian forms meaning "lime, calcium." The Malay word **kapur** shares this ancestry.

**Linguistic Descendants:** The Sanskrit term produced numerous descendants across Indo-Aryan languages, including Hindi कपूर (kapūr), Punjabi ਕਪੂਰ (kapūr), Marathi कापूर (kāpūr), and many others. It also influenced borrowings in Arabic (كافور), Persian, Greek, and European languages like Spanish *alcanfor* and Portuguese *alcânfora*.

The word demonstrates fascinating cross-linguistic transmission of a commercial product term across Asia, the Middle East, and into European languages.
```


## [2026-09-06T15:54:02.235Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== TAD pages tag near kafur ===\"; grep -n \"كافور\" TAD_pages.txt | head -3\nn=$(grep -n \"كافور\" TAD_pages.txt | head -1 | cut -d: -f1); echo \"line=$n\"; awk -v n=\"$n\" 'NR<=n && /\\[pdf page [0-9]+\\]/ {l=$0; ln=NR} END{}' TAD_pages.txt; grep -n \"\\[pdf page\" TAD_pages.txt | awk -F: -v n=\"$n\" '$1<n' | tail -2"
}
```


## [2026-09-06T15:54:02.763Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://ahdictionary.com/word/search.html?q=caracal",
 "prompt": "Give the American Heritage Dictionary entry for caracal with its etymology (French, Turkish karakulak)."
}
```


### [2026-09-06T15:54:04.387Z] TOOL RESULT

```
=== TAD pages tag near kafur ===
line=
```


### [2026-09-06T15:54:08.706Z] TOOL RESULT

```
# Caracal Dictionary Entry

According to the American Heritage Dictionary, a caracal is "a wildcat _(Caracal caracal)_ of Africa and southwestern Asia having short fawn-colored fur and long tufted ears."

**Etymology:** The word derives from French, which borrowed it from Ottoman Turkish _qaraqūlāq_. This Turkish term combines _qara_ (black) and _qūlāq_ (ear), reflecting the animal's distinctive dark ear tufts. The roots trace back through Old Turkic and possibly to Mongolian and Japanese linguistic ancestors.
```


## [2026-09-06T15:54:14.206Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nhead -3 TAD_pages.txt; echo \"---\"; grep -c $'\\f' TAD.txt; python3 - <<'EOF'\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD.txt',encoding='utf-8',errors='replace').read()\ni=t.find('كافور س في اليونانية')\nprint('pageidx(formfeeds before)=', t[:i].count('\\f')+1)\nprint(repr(t[i-1200:i-900]))\nEOF"
}
```


### [2026-09-06T15:54:15.827Z] TOOL RESULT

```
                                     ‫الف‬
           ‫ياكابىاللبناك‬  ‫‪َ8‬‬
                       ‫نببى‬
---
0
pageidx(formfeeds before)= 1
"يب القولون ممامعآ1 اليونابى الذي معثاه شعية من الأمعاء \nالغلاظط ا مشحمة وهو في الاعور واللستقم \n\nقومندان ايطالي 1366ة200«امء بعال لاس امم ر أي ء من م الحنود \n\n\nع \n\n\nويدبر السفينة مرادفه أمير وإمام وقائد وريّان \n\nقيثار وونانى 0 وهو'لة عار ب ذا تستة وتاك توافق كثارة العيرادة \nأما الزياب فله أربعة أوتا"
```


## [2026-09-06T15:54:25.758Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PLA page headers near 12596 and 12075 ===\"; grep -n \"\\[pdf page\" incoming/PLA/PLA_pages.txt | head -3\nawk 'NR>=11900 && NR<=12800 {if ($0 ~ /^[a-zA-Z].*[0-9]{3}.*[a-zA-Z]/ && length($0)<120) print NR\": \"$0}' incoming/PLA/PLA_pages.txt | head -20"
}
```


### [2026-09-06T15:54:27.504Z] TOOL RESULT

```
=== PLA page headers near 12596 and 12075 ===
```


## [2026-09-06T15:54:30.732Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\np='/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt'\nlines=open(p,encoding='utf-8',errors='replace').read().split('\\n')\nfor i in range(11900,12800):\n    l=lines[i]\n    if re.search(r'\\b2[0-4][0-9]\\b', l) and len(l.strip())<140 and len(l.strip())>3:\n        print(i+1, repr(l.strip()[:130]))\nEOF"
}
```


### [2026-09-06T15:54:32.184Z] TOOL RESULT

```
11975 'm.                       2.212.                                              _           - _._'
12130 '822 9.200 garbädin:                                "Zusammensetzung                    verschiedener                 Medikamente"'
12215 'garamfül                                                                        218                                               '
12318 'quftän                                                           220                                            galyün'
12484 'os - qüß:            "kleiner              Mann" <              pers. 225                  küdak     ı    mp.it1s          ku&(ak)'
12708 'kadhudä                                                                                227                                      ki'
```


## [2026-09-06T15:54:41.253Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nlines=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/DOZ.txt',encoding='utf-8',errors='replace').read().split('\\n')\nfor i in range(1300,1520):\n    l=lines[i].strip()\n    if re.fullmatch(r'\\d{1,3}',l) or re.match(r'^\\d{1,3}\\s',l) or re.search(r'\\s\\d{2,3}$',l):\n        print(i+1, repr(lines[i][:100]))\nEOF"
}
```


### [2026-09-06T15:54:42.924Z] TOOL RESULT

```
1312 "Samengesteld uit den imperativus in 't meervoud van\x0c42"
1338 'toepast. Volgens de opmerking van Fihan, was horde\x0c43'
1365 "1) In dit artikel moet ou steeds als in 't Fransch worden nitgesproken.\x0c44"
1392 '(door de Arabieren overgenomene) woord kabd, of\x0c45'
1422 'den inboorling uit een sarong en een kabaai bestaat.\x0c46'
1448 'Het Arab. kdfoer (jJ\\S)f dat het PrSkr. kappoerd\x0c47'
1476 'als Jodenduitsch opgenomen. Evenmin is kapot een\x0c48'
1505 "drooge dingen,'* had hg gerust weg kunnen laten,\x0c49"
```


## [2026-09-06T15:55:20.816Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"قرنی:\\|قره‌نی\\|قرهنی\\|كلارينت\\|کلارینت\" MON_part2.txt | head\necho \"=== قراقوش ===\"; grep -n \"قراقوش\\|قره‌قوش\\|قراقش\" MON_part2.txt BQT_v2_pages.txt incoming/BQT/BQT_v3_pages.txt | head\necho \"=== LKT karakus done ===\"\necho \"=== TTS index page for kara schwarz ===\"; sed -n '13790,13810p' incoming/TTS/TTS_vambery1878_uoft_djvu.txt"
}
```


### [2026-09-06T15:55:20.932Z] TOOL RESULT

```
24525:کلارینت: ۰2:10 (.) (سد.) یکی از 
=== قراقوش ===
=== LKT karakus done ===
=== TTS index page for kara schwarz ===
Aar  (Schnee)  89. 

fcar,  karak,  karku  (Arm)  85. 

fcara  (schwarz)  84. 

kara  (Augapfel)  83. 

karakci  (Räuber)  84. 

karalti  84. 

karamak  83. 

karaul  83. 

karcimak  22. 

karga  84. 

icari  (alt)  84.
```


## [2026-09-06T15:55:33.241Z] TOOL CALL #49: WebSearch

```json
{
 "query": "قره‌نی ساز بادی ریشه واژه ترکی قره نی کلارینت"
}
```


### [2026-09-06T15:55:43.094Z] TOOL RESULT

```
Web search results for query: "قره‌نی ساز بادی ریشه واژه ترکی قره نی کلارینت"

Links: [{"title":"بشنو از نی چون حکایت می کند...","url":"https://elhammusic.com/%D8%A2%D8%B4%D9%86%D8%A7%DB%8C%DB%8C-%DA%A9%D8%A7%D9%85%D9%84-%D8%A8%D8%A7-%D8%B3%D8%A7%D8%B2-%D9%86%DB%8C/"},{"title":"آشنایی با ساز بادی - چوبی کلارینت یا قره نی | موسیقی نو – پایگاه خبری تحلیلی","url":"https://moosighino.ir/%D8%A2%D8%B4%D9%86%D8%A7%DB%8C%DB%8C-%D8%A8%D8%A7-%D8%B3%D8%A7%D8%B2-%D8%A8%D8%A7%D8%AF%DB%8C-%DA%86%D9%88%D8%A8%DB%8C-%DA%A9%D9%84%D8%A7%D8%B1%DB%8C%D9%86%D8%AA-%DB%8C%D8%A7-%D9%82%D8%B1%D9%87/"},{"title":"تكنيک‌های نواختن ساز «کلارینت» یا قره نی","url":"https://donyayesazha.com/blog/post/1046/%D8%AA%D9%83%D9%86%D9%8A%DA%A9%D9%87%D8%A7%DB%8C-%D9%86%D9%88%D8%A7%D8%AE%D8%AA%D9%86-%D8%B3%D8%A7%D8%B2-%DA%A9%D9%84%D8%A7%D8%B1%DB%8C%D9%86%D8%AA-%DB%8C%D8%A7-%D9%82%D8%B1%D9%87-%D9%86%DB%8C"},{"title":"کلارینت یا همان قره نی معروف در موسیقی ترکیه و ایران | وب نوازان","url":"https://webnavazan.com/%DA%A9%D9%84%D8%A7%D8%B1%DB%8C%D9%86%D8%AA/"},{"title":"درباره کلارینت (قره نی) - دنیای ساز","url":"https://www.donyayesaaz.com/%DA%A9%D9%84%D8%A7%D8%B1%DB%8C%D9%86%D8%AA-%D9%82%D8%B1%D9%87-%D9%86%DB%8C/"},{"title":"آشنایی با ساز نی،نحوه آموزش و اقسام آن - بهار اندیشه","url":"http://bahareandishe.com/blogs/689-%D8%A2%D8%B4%D9%86%D8%A7%DB%8C%DB%8C-%D8%A8%D8%A7-%D8%B3%D8%A7%D8%B2-%D9%86%DB%8C%D8%8C%D9%86%D8%AD%D9%88%D9%87-%D8%A2%D9%85%D9%88%D8%B2%D8%B4-%D9%88-%D8%A7%D9%82%D8%B3%D8%A7%D9%85-%D8%A2%D9%86"},{"title":"ساز کلارینت (قره نی) چیست؟ - ویرگول","url":"https://virgool.io/@minatorabian62/%D8%B3%D8%A7%D8%B2-%DA%A9%D9%84%D8%A7%D8%B1%DB%8C%D9%86%D8%AA-%D9%82%D8%B1%D9%87-%D9%86%DB%8C-%DA%86%DB%8C%D8%B3%D8%AA-kfm3zxkdmosl"},{"title":"معرفی ساز کلارینت، قره نی | Introduction of Clarinet","url":"http://sokhanmusic.ir/introduction%20of%20Clarinet.htm"}]

براساس نتایج جستجو، اطلاعات مربوط به قره‌نی و ریشه واژگان آن به شرح زیر است:

## ریشه واژه قره‌نی

قره‌نی از ترکیب دو واژه ترکی به نام قره (سیاه) و کلمه نی فارسی ایجاد شده است (نی سیاه)، و در کشورهای دیگر با نام کلارینت شناخته می‌شود.

## ساز بادی

قره‌نی در دسته سازهای بادی تک زبانه‌ای قرار دارد و نوعی از کلارینت است که توانایی تولید فاصله‌های موسیقی شرقی (ربع پرده) را دارد.

## ریشه تاریخی کلارینت

ریشه ساز بادی چوبی کلارینت یا قره‌نی در سازهای تک نی یا لوله‌های شاخدار اولیه در یونان باستان، مصر باستان، خاورمیانه و اروپا از قرون وسطی است، و کلارینت مدرن از یک ساز باروک به نام chalumeau ایجاد شد.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-06T15:55:50.853Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/carbasus",
 "prompt": "Latin carbasus: meaning and etymology (Ancient Greek κάρπασος, Sanskrit karpāsa), and descendants. Also any English entry."
}
```


## [2026-09-06T15:55:52.759Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%82%D8%B1%D9%87%E2%80%8C%D9%82%D9%88%D9%84%D8%A7%D9%82",
 "prompt": "Is there an entry for Ottoman Turkish or Persian قره‌قولاق (caracal)? Give etymology and meaning if present."
}
```


### [2026-09-06T15:55:54.488Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T15:55:56.550Z] TOOL RESULT

```
# Carbasus

**Carbasus** is a Latin noun (second declension, feminine) meaning linen, cambric, canvas, sail, awning, or curtain.

## Etymology

The term was borrowed from Ancient Greek *kárpasos* ("cotton"), which ultimately traces to Sanskrit *karpāsa* ("cotton") via Biblical Hebrew *karpás* ("fabric of cotton"). Notably, the same Sanskrit root also produced the Latin term *gossypium* (cotton).

## Declension

It follows the standard second-declension pattern. The genitive singular is *carbasī*, and the nominative plural is *carbasī*.

## Literary Example

Virgil used the word in the *Aeneid* (29–19 BCE): the phrase describes canvas inviting winds, representing the sails of Trojan ships departing from Carthage.

## Related Terms

The adjective *carbaseus* derives from this noun.
```


## [2026-09-06T15:56:08.165Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wiktionary.org/wiki/caracal|page 243 entry 0, English caracal < French < Ottoman Turkish kara kulak, calque of Persian siyah-gush\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Turkic/kara|page 243 root Kar 2/Qar 2, Proto-Turkic *kara 'black'\" \\\n \"https://ahdictionary.com/word/search.html?q=caracal|page 243 entry 0 nodes 4-5, AHD etymology of caracal (F < Ottoman Turkish qaraqulaq)\" \\\n \"https://en.wiktionary.org/wiki/carbasus|page 243 entry 2 nodes 5-6, Latin carbasus < Gk karpasos < Hebrew karpas < Skt karpasa\" \\\n \"https://en.wiktionary.org/wiki/%CE%BA%CE%AC%CF%81%CF%80%CE%B1%CF%83%CE%BF%CF%82|page 243 entry 2 node 4, Ancient Greek karpasos\" \\\n \"https://en.wiktionary.org/wiki/%DA%A9%D8%B1%D8%A8%D8%A7%D8%B3|page 243 entry 2 nodes 1-3, Persian karbas < MP < Skt karpasa\" \\\n \"https://en.wiktionary.org/wiki/camphor|page 243 entry 3 node 6, English camphor chain\" \\\n \"https://www.etymonline.com/word/camphor|page 243 entry 3 nodes 4-6, Etymonline camphor\" \\\n \"https://en.wiktionary.org/wiki/%D9%83%D8%A7%D9%81%D9%88%D8%B1|page 243 entry 3 node 3, Arabic kafur < MP kapur < Austronesian\" \\\n \"https://en.wiktionary.org/wiki/%E0%A4%95%E0%A4%B0%E0%A5%8D%E0%A4%AA%E0%A5%82%E0%A4%B0|page 243 entry 3 root, Sanskrit karpura < Austroasiatic/Malayic kapur\" \\\n ; do\n  url=\"${u%%|*}\"; note=\"${u##*|}\"\n  python3 tools/fetch_source.py \"$url\" --note \"$note\" 2>&1 | tail -2\ndone"
}
```


### [2026-09-06T15:56:13.470Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/3dc32f3c2e575a84.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/04fbeddbacb1210f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8c59571af7bc152f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cb3b737c9565301e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/73f7b8a1a67b5687.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5363b0585d58babc.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/41947311051ddb0a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/60beb4e092304c30.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ded8276bbbd9652a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/bd2df782388fcebf.txt
```


## [2026-09-06T15:56:18.260Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '10029,10060p' SYN.txt"
}
```


### [2026-09-06T15:56:18.309Z] TOOL RESULT

```
402 SELECTED INDO-EUROPEAN SYNONYMS 6.24 COTTON NG prapraxe Dan. bomuld Lith.  medvilné, bovelna- It. cotone Sw. bomull Lett. kuokvilna Fr. coton ME cotoun, coton SCr. pamuk Sp. algodén NE colton Boh. bavina Rum. bumbac Du. katoen, boomwol Pol. bawelna NIr. _canach, cadas MHG kattiin, boumwolle Russ. chlopok W. colwm NHG  baumuvolle Skt. karpasa- Br. kotoris
European names for cotton are mostly borrowed with the plant from oriental sources.
1. Arab. guin, qutun (Sp.-Arab. go- tun). Schrader, Reallex. 1.84. Lo- kotsch, 1272. REW 4796a.
It. cotone, Fr. coton (> Br. kotofis), Sp. algodén, ME cotoun, coton (> W. colwm), NE cotton, Du. katoen, MHG kattin (NHG kattun ‘calico’).
2. An oriental word, perh. orig. Irani- an, represented by Pahl. pambak, Osset. bambag, NPers. panba, Arm. bambak. Schrader, loc. cit. Berneker 100 f.
Hence late Lat. bombazx ‘linteorum aut aliae quaevis quisquiliae’ (Du Cange), bombacitum (> NE bombasine, bombast, Fr. bombasin, etc.), and ap- parently Grk. Boufvt (> Lat. bombyz) ‘silkworm, silk’.
Here also NG prapréx, Rum. bumbac, SCr. pamuk, but by the mediation of different Turkish forms (cf. Berneker, loc. cit.).
MHG boumwolle, bounwolle, bowmwol, etc., NHG baumwolle, LG bomwolle, Du. boomwol, lit. ‘tree wool’. Cf. Hdt. 3.106 (of Indian cotton) ra 62 dévpea ra wypia abroi dépe xapmov etpra. But possibly the first part was orig. bamb or bomb fr.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
the same source as Lat. bombaz, ete, (above) and transformed by popular connection with baum ‘tree’. Falk. Torp 92. :
Dan. bomuld, Sw. bomull, fr. LG bom- wolle with translation of the final mem- ber.
Lith. medvilné, Lett. kuokvilna, lit, ‘tree wool’, semantic borrowings fr. NHG baumwolle.
Pol. bawetna (> Lith. bovelna), Boh. bavina, fr. NHG baumwolle with ba- for baum- and translation of final (cf. Dan. bomuld, above). Briickner 18.
3. NIr. canach (also Gael.) : Ir. ca- nach ‘down, fuzz’, etym.? Macbain 68.
NI. cadas (given first by McKenna s.v. colton), fr. ME cadas (NE caddis) a sort of coarse cotton or wool used in padding, fr. OFr. cadaz, cadas, further orig. unknown. NED s.y. caddis. Macbain 74.
4, Russ. chlopok : chlop’e ‘flocks (of wool), flakes (of snow)’, Boh. chlupaty ‘hairy’, Pol. dial. chtwpy ‘tufts’, other- wise obscure. Berneker 390 f.
5. Skt. karpdsa-, loanword fr. the same source as Grk. xapmacos, Lat. car- basus ‘fine cotton cloth’, Arab. kerpas, etc. Walde-H. 1.165.
of the words for ‘silk’, like the oriental origin. tal word represented 2 ian sirghe, Mongolian sirkek. Et isnate source is dub., the old identification with a Chinese word be- ing unsubstantiated. Cf. Schrader, Reallex. 2.382; Laufer, Sino-Iranica 538 ff, who thinks the word of Iranian origin. Grk. onpixés adj., onpixdy (onp ‘silk- worm’, Dijpes being later back-forma- tions), Lat. séricus adj., séricum, whence Ir. siric, OHG serth. The earliest Grk. reference to ‘silk’, but without the word, is supposed to be Aristot. HA 551°13. Miss Richter, AJA 1929, 27 ff., argues for much earlier use of silk, Pie fat, Russ, Sell, Lith. éilkai, . silkas, borrowed independently
ftom the Orient (rather than through mpixoy, etc)
The Balto-Slavic
Many article, are of j, An orien
word, prob. by meta- ee a). name of Damascus im CE NE damask, etc.). Lokotsch, 1 OP. cit, 383. Hence late
* AN orient thesis fp. the al
i rader
igitized by Arya Samaj Foundation Chennai and eGangotri
L ADORNMENT AND CARE 403 NG; PERSONA cLOTHI 6.25 SILK oth sate Lith. %lkai ampixby BS silkt Lett. zids ; salty per ake Dan. silke ChSI. Selkit, godovablt, svila rium Sw. silke, siden SCr. svila seld OE sioloc, seoloc Boh. heduabi sole ME selk Pol. jedwab seda NE silk Russ. elk malase Du. zijde Skt. kdugeya- "sila, sirte OHG _ sida, serih, silecho Avs “Oares sioda MHG side sidan NHG setde seiz
Grk. péerata, parata, NG péraka, perdks, late Lat. metaxa, mataza, Rum. mdtase ‘silk’, Fr. matasse ‘raw silk’.
3. Late Lat. séta (fr. saeta ‘coarse hair, bristles’), elliptical for séta sérica. Hence It. seta, Fr. soie, Sp. seda; Ir. sita, NIr. stoda, W. sidan, Br. seiz; OHG sida, MHG side, NHG seide, Du. zijde, MLG zide (> Sw. siden, Lett. zids). REW 7498. Vendryes, De hib. voc. 178.
4, Late ChSI., SCr., ORuss. suila, for *stivila, fr. stiviti, epd. of viti ‘wind’ (10.14). Orig. a participial formation meaning ‘wound’, perh. referring to the cocoon of the silkworm.
Russ.—ChSl. godovabli, Boh. hedudbt (> Pol. jedwab) fr. Gme., cf. OHG gotawebbi ‘any fine expensive cloth’, gl. also sericum, ON gudvefr, OE godweb ‘velvet, purple, fine cloth’, perh. lit. ‘God’s cloth’, i.e. ‘fine cloth suitable for use in God’s service’, though the first member may be transformed fr. Arab. quin ‘cotton’ (6.24). Berneker 316. Briickner 204.
5. Skt. kduceya-, fr. koca- ‘cask, ves- sel’, then applied to the ‘cocoon’ of the silkworm; cf. koca-kara- ‘silkworm’, lit. ‘cocoon-maker’.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
```


## [2026-09-06T15:56:30.284Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK karpas/karpur ===\"; grep -n -i \"karpās\\|karpasa\\|karpura\\|carbasus\" POK_full.txt WLD_band3.txt incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt 2>/dev/null | head\necho \"=== LEW carbasus ===\"; grep -n -i \"carbasus\" LEW_1910.txt LAT.txt | head\necho \"=== SKT camphor ===\"; grep -n -i \"camphor\" SKT.txt WEB_vol1.txt | head -5\necho \"=== FSD camphor ===\"; grep -n -i \"cam'phor\\|camphor,\" FSD_vol1.txt | head -3"
}
```


### [2026-09-06T15:56:30.392Z] TOOL RESULT

```
=== POK karpas/karpur ===
=== LEW carbasus ===
LAT.txt:9840:carbas n. (Vitr.), carbasus (Suet.): vent d'est. Du gr. xap^ac»
LAT.txt:9841:carbasus, -i f.; pl. collectif carbasa n.(d'ou carbasum): genus
=== SKT camphor ===
SKT.txt:2709:Camphor.  (F.  — Arab— Malay.)  For- rocrly  spelt  camphire  (with  an  inserted  i").
SKT.txt:2710:—  F.  camphrt,  '  camphire ;  *  Cot,  —  Low L.  camphora  (whence  the  form  eoMtpkor).
SKT.txt:2711:—  Arab,  kiifur^  camphor;  cf.  Ski.  iar;^i^/T», camphor.—  Malay  kdpUr,  liL  chalk;  ktipUi Jiariis,  chalk  of  Baruus,  a  name  for  cam phor.     h'aivHs  is  in  .Sumatra,
WEB_vol1.txt:5206:avant cam’phir, camphor obtained from waits N worn san GiG
WEB_vol1.txt:11649:as/a-rone, as’a-rin, n. camphor of asarum, a crystallized substance obtained from the Asarum Europzum.
=== FSD camphor ===
5451:thol  or  -th51,  n.  Tbe  essential  principle  \   *   i, (CioHitO)  of  oil  of  wormwood,  isomeric  U   ; with  camphor,  ab'sln-tbolct. ab'sls,  1   ab'sis;  2   ab'sls,  n.  See  apsis. ab-slst’t>rt.  Toleaveoff. — ab-sis  tenceT>Ji. ab'slt,  1   ab'sit;  2   ib'slt,  n.  IL.l  Per- mission  to  be  absent  for  a   short  time,  as overnight,  granted  to  a   student, ab'so-lutc,  1   ab'so-liut;  2   Sb'so-lut., a.  I.  Independent;  free  from  lim- itation, dependence,  or  relation:  op- posed to  relative  or  phenomenal .   1.
16550:an'e-thene,  1   an'i-fhln;  2   Sn'e-thfin,  n.  Chem.  A   volatile oil  (CiqHiO,  isomeric  with  oil  of  turpentine,  contained  In dll],  etc.  [   <   L.  anethum,  anise,  <   Gr.  anithon. \ an'e-thol,  1   an'i-ihol  or  -thel;  2   &n'e-thol  or  -th51.  n. Chem .   An  organic  compound  (CioSInO)  contained  in and  forming  the  essential  constituent  of  oils  of  anise, fennel,  and  tarragon.  It  occurs  either  as  a   solid  at  ordinary temperatures  (anlse»camphor,  solid  anethol)  or  as  a   volatile liquid  (liquid  anelhol).  Better  called  methyl  dllylphenol.  [   < L.  anethum  (<  Gr.  anithon),  anise,  4*  -ol.J An'e-thoth-lte,  1   an'i-fheth-dt;  2   an'e-th6th-it,  n.  Bib .
55998:Bembllng  it  and  (2)  to  the  special  camphors  derived  Irom natural  products;  as,  anemone  camphor;  asarum  r   • buchu  c.;  cedar  c.;  chloral  c.;  coiophcnc  c.;  cubcb  c   ’ dcxtro.c.  (same  as  CAJirnon,  1);  Inula  c.  (same  os  alast camphor);  Japan  c.  (same  as  camphor,  1);  Ledum  c- levo.c.  (same  as  camphor,  2);  Matlco  c.;  Matricaria  c’ (same  as  camphor,  2);  mentha  c.;  patchouli  c.;  plchu- rlm  c.;  pyrethrnm  c.  (same  as  PTttETimiN);  sage  c.; salol  c.;  sandalwood  c.;  tar  c.  (same  as  naphthalene); thyme  c.
```


## [2026-09-06T15:56:39.103Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '9838,9850p' LAT.txt; echo \"=== SKT page ===\"; python3 - <<'EOF'\nimport re\nlines=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt',encoding='utf-8',errors='replace').read().split('\\n')\nfor i in range(2650,2720):\n    if re.fullmatch(r'\\s*\\d{1,3}\\s*', lines[i]): print(i+1, lines[i].strip())\nEOF"
}
```


### [2026-09-06T15:56:40.761Z] TOOL RESULT

```
c&rdo
M.L.1673.
carbas n. (Vitr.), carbasus (Suet.): vent d'est. Du gr. xap^ac»
carbasus, -i f.; pl. collectif carbasa n.(d'ou carbasum): genus
lini est, quod abusiue plerumque pro uelo ponitur-, 4 toffe de lin qui
servait de vetement aux divinitas fluviales, ou aux riches (cf. Non.
541,11), et dont on faisait aussi les voiles des vaisseaux ou les
pare-soleil des theatres. Atteste depuis Ennius; rare en prose. Iri.
carbh.
Derives: carbaseus,-sinus,-sineus.
L'identite de sens et de forne avec gr. wxpTtouTOC, au b prbs, est
frappante; cf. cependant Fohalle, Mei.Vendryes, p.173. Carpaseus =
xaproxcr los, carpasinus =‘xapimaivoC; Caecilius unit carpasina, molochina,
=== SKT page ===
```


## [2026-09-06T15:58:11.884Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%82%D8%B1%D9%87-%D9%82%D9%88%D9%84%D8%A7%D9%82/",
 "prompt": "Does Persian قره‌قولاق exist as a headword? Give the definitions from فرهنگ معین and لغت‌نامه دهخدا, and any etymology label (e.g. [تر.])."
}
```


### [2026-09-06T15:58:17.514Z] TOOL RESULT

```
Based on the webpage content provided, **قره‌قولاق does exist as a headword** in the Abadis Dictionary.

However, the page does **not provide specific definitions** from فرهنگ معین or لغت‌نامه دهخدا. 

The only definition given is: "نام طایفه‌ای از ایلات قشقایی و خمسه" (the name of a tribe among the Qashqai and Khamseh confederations).

**No etymology label** is shown in this excerpt. The source credited is "عکس فرهنگ ریشه واژگان فارسی دکتر علی نورایی" (images from Dr. Ali Nouraei's Persian Etymology dictionary), but detailed etymological information is not displayed on this page.
```


## [2026-09-06T15:58:21.038Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://vajehyab.com/dehkhoda/%D9%82%D8%B1%D9%87+%D9%82%D9%88%D9%84%D8%A7%D9%82",
 "prompt": "Give the Dehkhoda entry for قره قولاق: definition and any etymology."
}
```


### [2026-09-06T15:58:23.251Z] TOOL RESULT

```
The server returned HTTP 500 Internal Server Error.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-06T15:58:27.943Z] TOOL CALL #58: WebSearch

```json
{
 "query": "\"قره‌قولاق\" یا \"قراقولاق\" سیاه‌گوش گربه‌سان معنی لغت‌نامه دهخدا"
}
```


### [2026-09-06T15:58:36.555Z] TOOL RESULT

```
Web search results for query: ""قره‌قولاق" یا "قراقولاق" سیاه‌گوش گربه‌سان معنی لغت‌نامه دهخدا"

Links: [{"title":"جست‌وجوی پروانک","url":"https://www.vajehyab.com/?q=%D9%BE%D8%B1%D9%88%D8%A7%D9%86%DA%A9"},{"title":"قره - معنی در دیکشنری آبادیس","url":"https://abadis.ir/fatofa/%D9%82%D8%B1%D9%87/"},{"title":"سیاه‌گوش (وشق) - ویکی‌پدیا، دانشنامهٔ آزاد","url":"https://fa.wikipedia.org/wiki/%D8%B3%DB%8C%D8%A7%D9%87%E2%80%8C%DA%AF%D9%88%D8%B4_(%D9%88%D8%B4%D9%82)"},{"title":"اق - معنی در دیکشنری آبادیس","url":"https://abadis.ir/fatofa/%D8%A7%D9%82/"},{"title":"معنی سیاه گوش | لغت‌نامه دهخدا","url":"https://vajehyab.com/dehkhoda/%D8%B3%DB%8C%D8%A7%D9%87+%DA%AF%D9%88%D8%B4"},{"title":"کنجل در دیکشنری های کمانک, تصویر کنجل","url":"https://fa.kamanak.com/pedia/subject/کنجل"}]

بر اساس نتایج جستجو، در لغت‌نامه دهخدا:

**سیاه‌گوش** جانوری است که گوشهای آن سیاه است و به شاطرشیر مشهور است، و به ترکی **قره قلاغ** گویند. این جانور پیش‌اپیش شیر رود و انگ دهد تا جانوران دیگر از آمدن شیر آگاه شوند و احتیاط نمایند.

همچنین، کاراکال از نام ترکی این حیوان یعنی کاراکولاک (کارا: سیاه و کولاک: گوش) گرفته شده است، که نشان می‌دهد **قره‌قولاق** یا **قراقولاق** به معنی "گوش سیاه" در ترکی است.

بترکی قره قولاق یا قره قولاخ گویند. این نام‌ها متغیرهای مختلف یک واژه ترکی هستند که به حیوان سیاه‌گوش (کاراکال) اطلاق می‌شود.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-06T15:58:42.838Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://vajehyab.com/dehkhoda/%D8%B3%DB%8C%D8%A7%D9%87+%DA%AF%D9%88%D8%B4' --note 'page 243 entry 0 node 3: Dehkhoda s.v. سیاه‌گوش — \"بترکی قره قولاق گویند\"' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://fa.wikipedia.org/wiki/%D8%B3%DB%8C%D8%A7%D9%87%E2%80%8C%DA%AF%D9%88%D8%B4_(%D9%88%D8%B4%D9%82)' --note 'page 243 entry 0: Persian Wikipedia سیاه‌گوش/caracal, Turkish karakulak' 2>&1 | tail -2"
}
```


### [2026-09-06T15:58:45.541Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/66537b92e1d9a419.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/922260947e7b9d3e.txt
```


## [2026-09-06T16:01:27.584Z] TOOL CALL #60: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build243.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW_KLN = \"https://en.wiktionary.org/wiki/caracal\"\ndata = {\n \"pdf_page\": 243,\n \"book_page\": 213,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-06\",\n \"entries\": []\n}\n\n# ---------------- ENTRY 0 : Kar 2, Qar 2 ----------------\ne0 = {\n \"entry\": 0,\n \"root\": \"Kar 2, Qar 2\",\n \"verdict\": \"plausible\",\n \"modern_form\": \"Proto-Turkic *kara 'black' (Old Turkic qara, Ottoman/Turkish kara); the senses 'old' and 'bad luck' belong to separate Turkic stems (*karɨ- 'to grow old', *karga- 'to curse')\",\n \"note\": \"The root box is a verbatim transcript of Vámbéry's entry no. 84, which begins at the foot of TktEtWb p.79: 'kar, kir, kur, schwarz, trocken, dürr, alt, Unglück, Schaden, Fluch' — so the reference is exactly right and Nourai's gloss 'black, old, bad luck' is Vámbéry's 'schwarz … alt, Unglück'. The word itself is unimpeachable: Proto-Turkic *kara 'black' > Old Turkic/Ottoman qara, Turkish kara, Azerbaijani qara, Chuvash hura, Yakut xara. What is no longer accepted is Vámbéry's 1878 root-lumping: modern Turkology keeps *kara 'black' apart from karı 'old' (< *karɨ- 'to grow old', the same stem as karı 'wife, old woman') and from kargış 'curse' (< *karga- 'to curse'), which Vámbéry filed under one stem because of a supposed 'dry, withered' link. Nourai's language label 'Turkish' is loose for a Common Turkic etymon but is the label under which the Persian loans were in fact taken (Oghuz/Ottoman-Azeri). Hence 'plausible' rather than 'confirmed': the form and the 'black' gloss are right, the three-way sense bundle is a 19th-century reconstruction. Note that Nourai's numbering 'Kar 2 / Qar 2' distinguishes this Turkic root from his Indo-European 'Kar 1'.\",\n \"note_fa\": \"این جعبهٔ ریشه دقیقاً برگرفته از مدخل شمارهٔ ۸۴ فرهنگ ریشه‌شناختی ترکی-تاتاری وامبری است که در پایان صفحهٔ ۷۹ آغاز می‌شود: «kar, kir, kur — سیاه، خشک، پژمرده، کهنه، بدبختی، زیان، نفرین»؛ پس ارجاع نورایی (TTS:79) درست است و معنای «سیاه، کهنه، بدشگون» همان معنایی است که وامبری آورده. خودِ واژه تردیدناپذیر است: ترکی آغازین *kara «سیاه» > ترکی باستان و عثمانی qara، ترکی امروز kara، آذربایجانی qara، چوواشی hura. آنچه امروز پذیرفته نیست، یکی‌انگاری ریشه‌هاست: ترک‌شناسی امروزی *kara «سیاه» را از karı «پیر» (از ستاک *karɨ- «پیر شدن») و از kargış «نفرین» (از *karga-) جدا می‌داند و آن‌ها را هم‌ریشه نمی‌شمارد. بنابراین ادعای نورایی دربارهٔ «سیاه» درست است، ولی بستهٔ سه‌گانهٔ معنایی بازسازی سدهٔ نوزدهمی وامبری است و با احتیاط پذیرفتنی است.\",\n \"sources\": [\n   \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Turkic/kara\",\n   \"https://en.wiktionary.org/wiki/caracal\"\n ],\n \"ref_check\": [\n   {\"ref\": \"TTS:79\", \"status\": \"supports\",\n    \"note\": \"Vámbéry, Etym. Wb. der turko-tatarischen Sprachen (TTS_vambery1878_uoft_djvu.txt, lines 5205-5245; the running page number '79' stands immediately above and '80' immediately below): '84. kar, kir, kur, schwarz, trocken, dürr, alt, Unglück, Schaden, Fluch' with 'uig. kara = schwarz, finster, Erde, gemeines Volk; kargis = Unglück, Fluch, Schimpf (vgl. kara kün = Unglückstag)', 'cag. kara (wie oben) … kargu, kargis = Fluch', 'osm. karatmak = schwärzen … kari = alt, bejahrt'. Vámbéry's own index (line 13796 ff.) lists 'kara (schwarz) 84', 'kari (alt) 84', 'karga 84' by entry number. Nourai's gloss and page are exact.\"}\n ],\n \"consulted\": [\n   {\"src\": \"LKT\", \"where\": \"no. 1070 ff. / no. 1081 / no. 1082 (LKT.txt lines 2555-2600)\", \"stance\": \"supports\",\n    \"note\": \"Lokotsch derives a whole family from 'tk. kara „schwarz“, s. hier Nr. 1070': no. 1080 'Tk. karakol: „Schwarze Hand“', no. 1081 'Tk. karakolak: „Schwarzohr“', no. 1082 'Tk. karakus: „Adler“ [aus tk. kara „schwarz“ und kus „Vogel“]'. The 'black' sense is thus the productive one in the loanwords.\"},\n   {\"src\": \"Wiktionary (Proto-Turkic)\", \"where\": \"Reconstruction:Proto-Turkic/kara\", \"stance\": \"partial\",\n    \"note\": \"'*kara — black', with descendants in every Turkic branch (Chuvash hura, Turkish/Azerbaijani/Turkmen kara/qara, Uyghur/Uzbek, Kazakh/Kyrgyz/Tatar, Yakut/Tuvan/Khakas). The page carries no 'old' or 'misfortune' sense, i.e. it does not support Vámbéry's wider bundle.\"},\n   {\"src\": \"TTS\", \"where\": \"no. 83, pp. 78-79\", \"stance\": \"partial\",\n    \"note\": \"Vámbéry's *preceding* entry, '83. kar, kor, kör, köz — Auge, Blick, sehen, suchen', explicitly warns 'osm. kara (göz karasy) = Augapfel, und nicht Schwärze des Auges, wie bisher fälschlich angenommen wurde' — i.e. Vámbéry himself keeps two homophonous kar- stems apart, which is why Nourai numbers his root 'Kar 2'.\"}\n ],\n \"nodes\": []\n}\n\ne0[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Persian\", \"words\": \"qareh «قره»\", \"verdict\": \"confirmed\",\n \"derivation\": \"Persian قره qare / قرا qarā 'black' is a straightforward loan from Oghuz Turkic qara 'black', taken in during the Saljuq–Mongol–Turkmen and then Safavid–Qajar centuries, when Turkic was the language of the army and the court. It is not a free Persian adjective — it survives only as the first member of compounds and of names, exactly the four the chart lists: قراقروت qara-qorut 'black qorut', the dark, sour dried-whey ball (Mo'in: قراقروت [تر. — قره‌قوروت], 'ترشی آن تند و زبان‌گز است … این نوع را قراقروت و ترف سیاه نامند'); قراقوش qarā-qoš 'eagle', lit. 'black bird' (Lokotsch no. 1082 'Tk. karakus „Adler“ [aus tk. kara „schwarz“ und kus „Vogel“]'); قره‌نی qare-ney 'clarinet', lit. 'black reed' (a hybrid: Turkic qara + Persian نی ney); and قرا qarā itself in names such as قراسنقر (Mo'in: [تر. — سنقر سیاه]) and قراسوران (Mo'in: [تر. — قره‌سوران]). Phonetically nothing happens: Turkic /qara/ is simply written قره/قرا, the final -a being rendered by the Persian hē. Mo'in tags every one of these compounds '[تر.]' = Turkish.\",\n \"derivation_fa\": \"«قره / قرا» به معنی «سیاه» وام‌واژه‌ای است از ترکی اوغوز qara، که از دورهٔ سلجوقی و مغول و سپس صفوی و قاجار — یعنی روزگاری که ترکی زبان لشکر و دربار بود — وارد فارسی شده است. این واژه در فارسی صفت آزاد نیست و تنها در ترکیب‌ها و نام‌ها به کار می‌رود؛ درست همان چهار نمونه‌ای که نورایی آورده: «قراقروت» (کشک سیاه و ترش؛ معین: [تر. ـ قره‌قوروت])، «قراقوش» یعنی «مرغ سیاه = عقاب» (لوکوچ، شمارهٔ ۱۰۸۲)، «قره‌نی» یعنی «نیِ سیاه» که ترکیبی دورگه از qara ترکی و «نی» فارسی است، و «قرا» در نام‌هایی چون «قراسنقر» (معین: [تر. ـ سنقر سیاه]) و «قراسوران» (معین: [تر. ـ قره‌سوران]). از نظر آوایی هیچ دگرگونی رخ نداده و تنها ـa پایانی با «ه» نوشته شده است. معین همهٔ این ترکیب‌ها را «[تر.]» برچسب زده است. ادعای نورایی درست است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Turkic/kara\"],\n \"ref_check\": [\n   {\"ref\": \"MON:2650\", \"status\": \"supports\",\n    \"note\": \"The local copy is Mo'in's two-volume Adena reprint, whose pagination differs from the six-volume Amir Kabir set Nourai cites, so the printed number 2650 itself could not be checked; the entries are there and say what the arrow says. MON_part2.txt line 12030 'قراسوران … [تر. ـ شاه را ـ قره‌سوران ـ قراسورن]'; line 12026 'قراسنقر [ـ تر. سنقر سیاه]'; line 12059 'قراقروت … [تر. ـ قره‌قوروت]', ending 'قارقورت، قره‌قروت، ترپ، ترف، تلف'. All are tagged Turkish and all contain qara 'black'.\"},\n   {\"ref\": \"MON:2670\", \"status\": \"supports\",\n    \"note\": \"Same caveat about pagination. The qara- compounds run on for several columns in Mo'in (MON_part2.txt lines 12026-12110), which is consistent with Nourai citing two nearby pages, 2650 and 2670, for the simplex and the compound قره‌قولاق.\"}\n ],\n \"consulted\": [\n   {\"src\": \"LKT\", \"where\": \"nos. 1077-1082 (LKT.txt lines 2555-2600)\", \"stance\": \"supports\",\n    \"note\": \"Lokotsch's whole karagan/karakol/karagöz/karakolak/karakus block is built on 'tk. kara „schwarz“' and shows the same compounding pattern that Persian borrowed.\"},\n   {\"src\": \"MON\", \"where\": \"s.vv. قراسنقر، قراسوران، قراقروت (MON_part2.txt lines 12026-12100)\", \"stance\": \"supports\",\n    \"note\": \"'قراقروت: [تر. ـ قره‌قوروت] … این نوع را قراقروت و ترف سیاه نامند' — Mo'in glosses the compound as the *black* qorut, i.e. he reads قره as 'black' exactly as the chart does.\"},\n   {\"src\": \"TTS\", \"where\": \"no. 84, p. 79\", \"stance\": \"supports\",\n    \"note\": \"'osm. karatmak = schwärzen; karalti = Zwielicht, halbdunkel; karakus = Geier' — the Ottoman stock from which the Persian compounds were taken.\"}\n ],\n \"derivation_note\": None\n})\n# strip helper key\ne0[\"nodes\"][0].pop(\"derivation_note\")\n\ne0[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Turkish\", \"words\": \"kara-kŭlâk, qara-qulâq\", \"verdict\": \"confirmed\",\n \"derivation\": \"Ottoman Turkish قره‌قولاق qara-qulaq is a transparent determinative compound: qara 'black' (Proto-Turkic *kara) + qulaq 'ear' (Proto-Turkic *kulkak, Old Turkic qulqaq), i.e. 'black-ear', from the tall black ear-tufts of Caracal caracal. Funk & Wagnalls p.398 s.v. caracal: 'The Persian lynx (Felis or Lynx caracal) of southwestern Asia … with long upright black ears tipped with black hairs. [F., < Turk. qara qulaq, black ear.]' (the OCR prints 'gulag … car' for 'qulaq … ear'). The American Heritage Dictionary gives the same: 'French, from Ottoman Turkish qaraqūlāq, from qara, black + qūlāq, ear'. Modern Turkish spells the animal karakulak. Semantically the compound is not a Turkic invention: Wiktionary (and the Persian lexicographic tradition behind it) records it as a calque of Classical Persian سیاه‌گوش siyāh-gōš 'black-ear' — the same coinage translated element for element, which is why Nourai's cross-reference note under node 3 is well taken.\",\n \"derivation_fa\": \"«قره‌قولاق» در ترکی عثمانی ترکیبی وصفی و کاملاً شفاف است: qara «سیاه» (از ترکی آغازین *kara) + qulaq «گوش» (از *kulkak، ترکی باستان qulqaq)، یعنی «سیاه‌گوش»، به مناسبت دسته‌موهای سیاه و بلند گوش این گربه‌سان. فرهنگ فانک و واگنالز در صفحهٔ ۳۹۸ زیر caracal می‌نویسد: «سیاه‌گوش ایرانی … با گوش‌های بلندِ سیاه‌نوک [از فرانسه، از ترکی qara qulaq «گوش سیاه»]»، و فرهنگ American Heritage نیز همین را می‌آورد. نکتهٔ مهم آنکه این ترکیب ابداع ترکی نیست، بلکه گرته‌برداری (calque) از «سیاه‌گوشِ» فارسی است — جزء‌به‌جزء ترجمه شده — و ازاین‌رو یادداشت خودِ نورایی در گرهٔ ۳ درست است. ادعای نورایی دربارهٔ این گره درست است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/caracal\", \"https://ahdictionary.com/word/search.html?q=caracal\"],\n \"ref_check\": [\n   {\"ref\": \"FSD:398\", \"status\": \"supports\",\n    \"note\": \"Funk & Wagnalls New Standard Dict. vol. I, FSD_vol1.txt line 57381, on the leaf between the running numbers 397 (line 57256) and 399 (line 57482), i.e. printed p.398: \\\"car'a-cal, n. 1. The Persian lynx (Felis or Lynx caracal) of southwestern Asia … uniformly reddish-brown above with long upright black ears tipped with black hairs. 2. Its pelt or fur. [F., < Turk. qara gulag, black car.]\\\" — OCR garbling of 'qara qulaq, black ear'. Exactly Nourai's claim, on exactly the cited page.\"},\n   {\"ref\": \"AHD:201\", \"status\": \"supports\",\n    \"note\": \"Only Watkins's Indo-European appendix (AHD_watkins1985.txt) is on disk, and it has no 'caracal' (it is not an IE word), so the printed page 201 of the 1975 New College Edition could not be checked directly; the online American Heritage entry, however, reads verbatim 'French, from Ottoman Turkish qaraqūlāq : qara, black + qūlāq, ear', which is the claim Nourai attributes to AHD.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. caracal (KLN_1966.txt line 6489, on the leaf printed 238-239)\", \"stance\": \"supports\",\n    \"note\": \"'caracal, n., a kind of lynx. — F., fr. Turk. qarah qulak, „black ear“.'\"},\n   {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century, vol. 1, s.v. caracal (WEB_vol1.txt line 27995)\", \"stance\": \"supports\",\n    \"note\": \"'car/a-cal, n. [Fr. caracal; Turk. qara qulaq; qara, black, and qulaq, ear.] 1. a lynx, the Lynx caracal, a native of northern Africa and southwestern Asia.'\"},\n   {\"src\": \"LKT\", \"where\": \"no. 1081 (LKT.txt line 2563)\", \"stance\": \"supports\",\n    \"note\": \"'1081. Tk. karakolak: „Schwarzohr“ ist der Name eines kleinen Raubtieres [pers. ebenso sijäh gus „schwarzes Ohr“ genannt]; hieraus dtsch. Karakal, Felis caracal Gmelin „persischer Luchs“.' Lokotsch pairs it with Persian siyāh-gūš just as Nourai's note does.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Persian\", \"words\": \"qareh-qŭlâq «قره قولاق»\", \"verdict\": \"confirmed\",\n \"derivation\": \"Persian قره‌قولاق qare-qulāq 'caracal' is the Ottoman/Azeri compound taken over whole, with no adaptation beyond the Persian spelling of the vowels; it lives alongside the native Persian name سیاه‌گوش siyāh-gūš. Dehkhoda, s.v. سیاه‌گوش, states the relation explicitly: 'جانوری است که گوش‌های آن سیاه است … بترکی قره قولاق (قره قلاغ) گویند'. The chart's NOTE ('Compare with syâh-gŭsh:caracal from root Kei 1') is not merely a comparison but the historical key, and modern scholarship settles the direction: Persian سیاه‌گوش (siyāh 'black' + gōš 'ear', Old Persian gauša-, Avestan gaoša-) is the model, Turkic qara-qulaq the element-for-element calque of it, and قره‌قولاق the calque coming back into Persian as a loan — a semantic round trip. Klein records the Persian original under the Anglo-Indian form: 'syagush, n., the caracal. — Pers.-Hind. siyah-gosh, lit. „black ear“ … The second element derives fr. OPers. gausha-, ModPers. gosh, „ear“'. In modern Persian قره‌قولاق also survives as a Qashqai/Khamseh tribal name.\",\n \"derivation_fa\": \"«قره‌قولاق» در فارسی همان ترکیب ترکی عثمانی/آذربایجانی است که یکجا وام گرفته شده و جز املای فارسیِ واکه‌ها هیچ تغییری نکرده؛ در کنار نام بومی فارسی «سیاه‌گوش» به کار می‌رود. دهخدا در مدخل «سیاه‌گوش» صریح می‌گوید: «جانوری است که گوش‌های آن سیاه است … بترکی قره قولاق (قره قلاغ) گویند». یادداشت خودِ نورایی («با سیاه‌گوش از ریشهٔ Kei 1 بسنجید») تنها یک مقایسه نیست، بلکه کلید تاریخی ماجراست: پژوهش امروزی جهت وام‌گیری را روشن کرده است — «سیاه‌گوش» فارسی (سیاه + گوش، از پارسی باستان gauša-، اوستایی gaoša-) الگوی نخستین است، qara-qulaq ترکی گرته‌برداری جزء‌به‌جزء از آن، و «قره‌قولاق» بازگشت همان گرته به فارسی در جامهٔ وام‌واژه؛ یعنی یک رفت‌وبرگشت معنایی. کلاین نیز صورت اصلی فارسی را زیر «syagush» آورده است. ادعای نورایی درست است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/caracal\", \"https://vajehyab.com/dehkhoda/%D8%B3%DB%8C%D8%A7%D9%87+%DA%AF%D9%88%D8%B4\", \"https://fa.wikipedia.org/wiki/%D8%B3%DB%8C%D8%A7%D9%87%E2%80%8C%DA%AF%D9%88%D8%B4_(%D9%88%D8%B4%D9%82)\"],\n \"ref_check\": [\n   {\"ref\": \"MON:2670\", \"status\": \"not_found\",\n    \"note\": \"Grepped MON_part1.txt and MON_part2.txt for قره قولاق، قره‌قولاق، قراقولاق، قولاق، قلاق — no hit. The local Mo'in is the abridged two-volume Adena reprint, which drops many of the Turkic compounds that the six-volume Amir Kabir set (the edition Nourai cites, and the one whose p.2670 he gives) carries; the headword itself is well attested in Persian (Dehkhoda s.v. سیاه‌گوش: 'بترکی قره قولاق گویند'), so this is a limitation of the available copy rather than evidence against the citation.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON/Dehkhoda (vajehyab)\", \"where\": \"Dehkhoda s.v. سیاه‌گوش\", \"stance\": \"supports\",\n    \"note\": \"'سیاه‌گوش: جانوری است که گوش‌های آن سیاه است و به شاطرشیر مشهور است، بترکی قره قولاق (قره قلاغ) گویند.' — the Persian lexicographic tradition itself equates سیاه‌گوش with قره‌قولاق and marks the latter as Turkish.\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. syagush (KLN_1966.txt line 37765)\", \"stance\": \"supports\",\n    \"note\": \"'syagush, n., the caracal. — Pers.-Hind. siyah-gosh, lit. „black ear“, fr. siyah, „black“, and gosh, „ear“ … The second element derives fr. OPers. gausha-, ModPers. gosh, „ear“, which is rel. to Avestic gaosho-.' Confirms the Persian model that the Turkish compound calques.\"},\n   {\"src\": \"LKT\", \"where\": \"no. 1081\", \"stance\": \"supports\",\n    \"note\": \"'[pers. ebenso sijäh gus „schwarzes Ohr“ genannt]' — Lokotsch too records the Persian doublet.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 4, \"lang\": \"French\", \"words\": \"\", \"verdict\": \"confirmed\",\n \"derivation\": \"Pass-through node: French caracal, the form through which the Turkish word entered western Europe. The word reached French from Ottoman Turkish in the 18th century by way of the naturalists' literature — Buffon uses le caracal in the Histoire naturelle (vol. III of the Quadrupèdes, 1761), taking the name from travellers' reports on the Persian and Ottoman lands; from French it passed to English, German (Karakal), Italian and the zoological binomial Caracal caracal. Neither Nourai's box nor the sources record any intermediate Italian or Latin stage, and the shape of the French word (a single k-vowel-r-a-k-a-l skeleton, no learned Latin ending) confirms a direct oral/travel-literature borrowing rather than a bookish one.\",\n \"derivation_fa\": \"این گره یک حلقهٔ واسطه است و واژه‌ای در برابر آن نیامده: فرانسوی caracal همان صورتی است که واژهٔ ترکی از راه آن به اروپای باختری رسیده است. این نام در سدهٔ هجدهم از ترکی عثمانی و از راه ادبیات طبیعی‌دانان وارد فرانسه شد — بوفون در «تاریخ طبیعی» (۱۷۶۱) آن را به کار می‌برد — و از فرانسه به انگلیسی، آلمانی (Karakal)، ایتالیایی و نام دوجزئی جانورشناسی Caracal caracal راه یافت. شکل واژهٔ فرانسوی، که هیچ پایانهٔ لاتینیِ کتابی ندارد، نشان می‌دهد وام‌گیری مستقیم و از راه سفرنامه‌ها بوده است نه از راه متون. ادعای نورایی درست است.\",\n \"sources\": [\"https://ahdictionary.com/word/search.html?q=caracal\", \"https://en.wiktionary.org/wiki/caracal\"],\n \"ref_check\": [\n   {\"ref\": \"AHD:202\", \"status\": \"supports\",\n    \"note\": \"The printed New College Edition is not on disk (only Watkins's IE appendix), so p.202 itself could not be inspected; the online American Heritage entry for caracal reads 'French, from Ottoman Turkish qaraqūlāq', which is precisely the French link Nourai draws here.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. caracal (KLN_1966.txt line 6489)\", \"stance\": \"supports\",\n    \"note\": \"'caracal, n., a kind of lynx. — F., fr. Turk. qarah qulak' — Klein likewise puts French between Turkish and English.\"},\n   {\"src\": \"FSD\", \"where\": \"vol. I p.398 s.v. caracal\", \"stance\": \"supports\",\n    \"note\": \"'[F., < Turk. qara gulag, black car.]' — the bracket names French as the immediate source of the English word.\"},\n   {\"src\": \"LKT\", \"where\": \"no. 1081\", \"stance\": \"partial\",\n    \"note\": \"Lokotsch gives only 'hieraus dtsch. Karakal' and does not name the French stage, though French is the standard route for such 18th-century zoological names.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 5, \"lang\": \"English\", \"words\": \"caracal\", \"verdict\": \"confirmed\",\n \"derivation\": \"English caracal 'a wild cat with black ears' is a straight borrowing of French caracal, taken over in the later 18th century with the French spelling and no change of meaning; the earliest English uses are in translations and adaptations of Buffon. Funk & Wagnalls p.398 defines it as 'The Persian lynx (Felis or Lynx caracal) of southwestern Asia and the greater part of Africa … with long upright black ears tipped with black hairs' and brackets '[F., < Turk. qara qulaq, black ear]'. The chain Turkish qara-qulaq > French caracal > English caracal is uncontroversial and is given identically by Klein, Webster's Second and the American Heritage Dictionary. English also has the older Anglo-Indian name for the same animal, syagush, direct from Persian-Hindi siyāh-gōš.\",\n \"derivation_fa\": \"واژهٔ انگلیسی caracal «گربه‌سان سیاه‌گوش» وام مستقیم از فرانسوی caracal است که در نیمهٔ دوم سدهٔ هجدهم، با همان املا و بی هیچ تحول معنایی، وارد انگلیسی شد؛ نخستین کاربردهای انگلیسی در ترجمه‌ها و اقتباس‌های آثار بوفون است. فانک و واگنالز در صفحهٔ ۳۹۸ آن را «سیاه‌گوش ایرانی … با گوش‌های بلند سیاه» تعریف می‌کند و در قلاب می‌نویسد «[از فرانسه، از ترکی qara qulaq «گوش سیاه»]». زنجیرهٔ ترکی qara-qulaq ← فرانسوی caracal ← انگلیسی caracal بی‌مناقشه است و کلاین، وبستر و American Heritage نیز همین را می‌گویند. انگلیسی نام کهن‌تر انگلیسی-هندیِ syagush را هم برای همین جانور دارد که مستقیم از «سیاه‌گوش» فارسی گرفته شده است. ادعای نورایی درست است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/caracal\", \"https://ahdictionary.com/word/search.html?q=caracal\"],\n \"ref_check\": [\n   {\"ref\": \"FSD:398\", \"status\": \"supports\",\n    \"note\": \"FSD_vol1.txt line 57381 (between the running numbers 397 at line 57256 and 399 at line 57482 = printed p.398): \\\"car'a-cal, n. 1. The Persian lynx (Felis or Lynx caracal) of southwestern Asia … with long upright black ears tipped with black hairs. 2. Its pelt or fur. [F., < Turk. qara gulag, black car.]\\\" — headword, gloss and etymology all as charted.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. caracal (KLN_1966.txt line 6489)\", \"stance\": \"supports\", \"note\": \"'caracal, n., a kind of lynx. — F., fr. Turk. qarah qulak, „black ear“.'\"},\n   {\"src\": \"WEB\", \"where\": \"vol. 1 s.v. caracal (WEB_vol1.txt lines 27995-27998)\", \"stance\": \"supports\", \"note\": \"'[Fr. caracal; Turk. qara qulaq; qara, black, and qulaq, ear.] 1. a lynx, the Lynx caracal … 2. the fur of the caracal.'\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict.\", \"stance\": \"silent\", \"note\": \"grep for 'caracal' in SKT.txt returns nothing — Skeat does not carry the word.\"}\n ]\n})\ndata[\"entries\"].append(e0)\nPYEOF\necho built-part1"
}
```


### [2026-09-06T16:01:29.936Z] TOOL RESULT

```
built-part1
```


## [2026-09-06T16:04:49.623Z] TOOL CALL #61: Bash

```json
{
 "command": "cat >> /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build243.py <<'PYEOF'\n\n# ---------------- ENTRY 2 : Karpâsah ----------------\ne2 = {\n \"entry\": 2,\n \"root\": \"Karpâsah\",\n \"verdict\": \"plausible\",\n \"modern_form\": \"Sanskrit कर्पास karpāsa- m./n. 'cotton, cotton plant' (nom. sg. karpāsaḥ) — itself a culture word of unknown, probably non-Indo-Aryan origin\",\n \"note\": \"The headword is real and correctly glossed: Sanskrit karpāsa- 'cotton, cotton tree' (Nourai's 'Karpâsah' is the nominative singular karpāsaḥ, not the stem). What makes the box 'plausible' rather than 'confirmed' is that Nourai treats Sanskrit as the fountain-head of the whole tree, and the very reference he cites for it says otherwise. Buck, Selected Synonyms p.402 §6.24 COTTON, item 5 reads: 'Skt. karpāsa-, loanword fr. the same source as Grk. κάρπασος, Lat. carbasus „fine cotton cloth“, Arab. kerpas, etc.' — i.e. Sanskrit, Greek and the Semitic forms are for Buck *parallel* borrowings from one unidentified source, not a chain hanging from Sanskrit. Klein p.238 hedges the same way: Gk. κάρπασος 'is prob. borrowed fr. OI karpāsaḥ … According to Porzig … both OI karpāsaḥ and Gk. κάρπασος derive from a language of the Mediterranean or Asia Minor.' Current Wiktionary routes Greek through Biblical Hebrew כַּרְפַּס karpas (Esther 1:6) rather than straight from Sanskrit. The Iranian and Arabic half of Nourai's tree (nodes 1-3) is solid; the Greek/Latin/English half (nodes 4-6) is where the simplification lies. Neither POK nor Walde-Pokorny has the word at all — it is a Wanderwort, not an inherited Indo-European root, and Nourai is right not to label it one.\",\n \"note_fa\": \"سرواژه درست و معنای آن نیز درست است: سنسکریت کَرپاسَ karpāsa- «پنبه، درخت پنبه» (صورت «Karpâsah» نزد نورایی همان حالت فاعلی مفرد karpāsaḥ است نه ستاک). آنچه این جعبه را «با احتیاط پذیرفتنی» می‌کند این است که نورایی سنسکریت را سرچشمهٔ همهٔ شاخه‌ها گرفته، حال آنکه همان منبعی که خود او یاد کرده خلاف این را می‌گوید: باک در صفحهٔ ۴۰۲ می‌نویسد «سنسکریت karpāsa- خود وام‌واژه است، از همان سرچشمه‌ای که یونانی κάρπασος و لاتین carbasus و عربی kirbās از آن آمده‌اند». کلاین (ص ۲۳۸) نیز با احتیاط می‌نویسد یونانی «احتمالاً» از سنسکریت است و به رأی پورتزیش اشاره می‌کند که هر دو را از زبانی مدیترانه‌ای یا آسیای صغیری می‌داند؛ ویکی‌واژهٔ امروزی نیز یونانی را از عبری کتاب مقدس כַּרְפַּס (استر ۱:۶) می‌گیرد نه یکراست از سنسکریت. نیمهٔ ایرانی و عربیِ درخت (گره‌های ۱ تا ۳) استوار است و اشکال در نیمهٔ یونانی-لاتینی است. این واژه در پوکورنی و والده-پوکورنی اصلاً نیامده، چون واژه‌ای فرهنگی و مهاجر (Wanderwort) است نه ریشهٔ هندواروپایی — و نورایی درست کرده که آن را ریشهٔ هندواروپایی ننامیده است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%CE%BA%CE%AC%CF%81%CF%80%CE%B1%CF%83%CE%BF%CF%82\", \"https://en.wiktionary.org/wiki/carbasus\", \"https://en.wiktionary.org/wiki/%DA%A9%D8%B1%D8%A8%D8%A7%D8%B3\"],\n \"ref_check\": [\n   {\"ref\": \"KLN:238\", \"status\": \"partial\",\n    \"note\": \"Klein 1966, s.v. carbasus, on the leaf carrying printed pp.238-239 (KLN_1966.txt line 6504, between the page markers '237' at line 6470 and '238' at line 6507): 'carbasus, n., lint. — L., fr. Gk. κάρπασος, „flax, cotton“, which is prob. borrowed fr. OI karpāsaḥ, „cotton brush, cotton“, whence also ModPers. kirpās, Arm. kerpas, Arab. kirbās, Heb. karpas (Esther 1:6), „cotton, fine linen“. See Manfred Mayrhofer, A Concise Etymological Dictionary, I, p.174 s.v. karpāsaḥ. According to Porzig in Zeitschrift für Indologie und Iranistik, 5, 272 ff., both OI karpāsaḥ and Gk. κάρπασος derive from a language of the Mediterranean or Asia Minor.' Supports the Persian, Arabic and Latin links, but only 'prob.' for the Greek and expressly records the rival non-Indic origin.\"},\n   {\"ref\": \"SYN:402\", \"status\": \"partial\",\n    \"note\": \"Buck, SYN.txt line 10029 ff. — the page header itself reads '402 SELECTED INDO-EUROPEAN SYNONYMS 6.24 COTTON', and the list has 'Skt. karpāsa-'. But item 5 of the discussion says: 'Skt. karpāsa-, loanword fr. the same source as Grk. κάρπασος, Lat. carbasus „fine cotton cloth“, Arab. kerpas, etc. Walde-H. 1.165.' — the exact page Nourai cites denies that Sanskrit is the source of the Greek and Semitic forms.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"POK_full.txt\", \"stance\": \"silent\",\n    \"note\": \"grep for karpās/karpasa/carbasus returns nothing — Pokorny has no such Indo-European root, as expected for a cotton Wanderwort.\"},\n   {\"src\": \"WLD\", \"where\": \"WLD_band3.txt and WLD_Bd1_1930 djvu\", \"stance\": \"silent\",\n    \"note\": \"grep for karpāsa/carbasus returns nothing in the Walde-Pokorny material on disk.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck §6.24, p.402\", \"stance\": \"partial\",\n    \"note\": \"See ref_check: Buck lists Skt. karpāsa- among the cotton words but calls it itself a loanword; he also notes that most European cotton words come from Arabic quṭn instead.\"},\n   {\"src\": \"HJB\", \"where\": \"s.v. CAPAS (HJB.txt line 5165)\", \"stance\": \"supports\",\n    \"note\": \"'CAPAS, s. The cotton plant and cotton-wool. H. kapas, from Skt. karpasa, which seems as if it must be the origin of κάρπασος, though the latter is applied to flax.' Yule/Burnell affirm the Sanskrit word and the Greek connection, with the same reservation about the flax sense.\"}\n ],\n \"nodes\": []\n}\n\ne2[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Persian\", \"words\": \"karpâs «کَرپاس»\", \"verdict\": \"confirmed\",\n \"derivation\": \"Persian کَرپاس karpās / kirpās 'cotton cloth' is the Indian word taken into Iranian, on the evidence of the shape: the -p- is preserved (an inherited Iranian word would have lenited it), and the -ās reflects Sanskrit -āsa- exactly. Hübschmann, Persische Studien p.130 sets it out in one line: 'Die Übereinstimmung von arm. kerpas „feines Linnen“ mit np. kirpās, arab. kirbās besagt bei einem Fremdwort (skr. karpāsa-, gr. κάρπασος, lat. carbasus etc.) nicht viel' — i.e. New Persian kirpās stands beside Armenian kerpas and Arabic kirbās as parallel reflexes of the same culture word, and Hübschmann explicitly classes it as a Fremdwort. Klein p.238 has the same form ('whence also ModPers. kirpās'). Mo'in likewise derives the Persian word from Indian: 'کرباس [هند. کرپاس ـ معرَّب کرپاس]'. The borrowing must be old — cotton reached Iran from India before the Sasanian period — and Wiktionary treats the modern word as inherited through Middle Persian from Sanskrit karpāsa.\",\n \"derivation_fa\": \"«کَرپاس» فارسی به معنی «پارچهٔ پنبه‌ای» همان واژهٔ هندی است که به ایرانی راه یافته، و گواه آن خودِ ساخت واژه است: «پ» میان دو واکه نگه داشته شده (اگر واژه‌ای موروثی و ایرانی بود، در فارسی میانه نرم می‌شد) و پایانهٔ ـās دقیقاً بازتاب ـāsa- سنسکریت است. هوبشمان در «پژوهش‌های فارسی»، صفحهٔ ۱۳۰، می‌نویسد: «همانندی ارمنی kerpas «کتان نازک» با فارسی نو kirpās و عربی kirbās، در واژه‌ای بیگانه (سنسکریت karpāsa-، یونانی κάρπασος، لاتین carbasus) چندان دلیل چیزی نیست» — یعنی او خود این واژه را صریحاً «وام‌واژه» می‌شمارد. کلاین نیز همین صورت را دارد («و از آن فارسی نو kirpās»)، و معین می‌نویسد «کرباس [هند. کرپاس ـ معرّب کرپاس]». وام‌گیری باید کهن باشد، چون پنبه پیش از دورهٔ ساسانی از هند به ایران رسیده بود. ادعای نورایی درست است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%DA%A9%D8%B1%D8%A8%D8%A7%D8%B3\"],\n \"ref_check\": [\n   {\"ref\": \"KLN:238\", \"status\": \"supports\",\n    \"note\": \"Klein s.v. carbasus (KLN_1966.txt line 6504, leaf 238-239): Gk. κάρπασος 'is prob. borrowed fr. OI karpāsaḥ … whence also ModPers. kirpās, Arm. kerpas, Arab. kirbās, Heb. karpas' — the Persian form and its Indian source are named on the cited page.\"},\n   {\"ref\": \"MON:2932\", \"status\": \"supports\",\n    \"note\": \"Pagination of the local two-volume Adena abridgement differs from the six-volume set Nourai cites, so the number 2932 itself is unverifiable, but the entry is there: MON_part2.txt line 21636 'کرباس: [هند. کرپاس ـ معر. کرپاس] (ا.) پارچهٔ پنبه‌یی سفید و ارزان قیمت' — Mo'in derives it from Indian karpās and marks the b-form as the Arabicised one.\"}\n ],\n \"consulted\": [\n   {\"src\": \"HUB\", \"where\": \"Persische Studien p.130 (HUB.txt line 4541)\", \"stance\": \"supports\",\n    \"note\": \"'… mit np. kirpās, arab. kirbās besagt bei einem Fremdwort (skr. karpāsa-, gr. κάρπασος, lat. carbasus etc.) nicht viel.' Hübschmann has the Persian form and files the whole group as a foreign culture word.\"},\n   {\"src\": \"HRN\", \"where\": \"Grundriss der neupersischen Etymologie\", \"stance\": \"silent\",\n    \"note\": \"grep of HRN.txt for karpas/karbas/kirbas finds nothing — Horn has no entry (unsurprising, since he treats inherited Iranian vocabulary).\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. karbāš (PHD.txt line 424, PHD_mackenzie.txt line 3214)\", \"stance\": \"contradicts\",\n    \"note\": \"MacKenzie's only karbāš is 'karbāš [klbʾš | N karbas, etc.] lizard' — a homonym, not the cloth word; A Concise Pahlavi Dictionary records no Middle Persian 'cotton cloth' karpās. (Asbaghi, PLA p.227, cites 'Mackenzie s.v.' for a Middle Persian karbas — that citation points at this 'lizard' entry and is a slip.)\"}\n ]\n})\n\ne2[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Arabic\", \"words\": \"karbâs\", \"verdict\": \"confirmed\",\n \"derivation\": \"Arabic كِرْباس kirbās (Nourai's 'karbâs') 'coarse white cotton cloth, calico' is the Persian word arabicised. The single diagnostic change is the one Arabic always makes: Arabic has no /p/, so Persian karpās/kirpās becomes kirbās, the p being replaced by its voiced labial neighbour b (compare Pahlavi pīl > Arabic fīl, and the same p > b in Arabic barq̇ for Persian parg). The vowelling kirbās, with i in the first syllable, matches the Persian variant kirpās that Klein and Hübschmann cite. Asbaghi, Persische Lehnwörter im Arabischen p.227, lists it among the Persian loans: 'kirbās: „feine weiße Leinwand“ pers. karbas, syr. …, hebr. …'. Klein p.238 names 'Arab. kirbās' in the same breath as ModPers. kirpās and Arm. kerpas. The word is old in Arabic (Fraenkel treats it among the older cloth terms) and spread with the caliphal textile trade.\",\n \"derivation_fa\": \"عربیِ «کِرباس» (kirbās) به معنی «پارچهٔ پنبه‌ای سفید و درشت‌بافت» همان واژهٔ فارسی است که معرّب شده است. تنها دگرگونیِ تشخیص‌دهنده همان است که عربی همیشه انجام می‌دهد: در عربی واج «پ» نیست، پس karpās/kirpās فارسی به kirbās بدل شده و «پ» جای خود را به هم‌جایگاه واک‌دارش «ب» داده است (سنجیدنی با pīl پهلوی > فیل عربی). واکهٔ نخستِ kirbās نیز با گونهٔ فارسی kirpās همخوان است. اصباغی در «وام‌واژه‌های فارسی در عربی» صفحهٔ ۲۲۷ آن را در شمار وام‌های فارسی آورده است: «kirbās: پارچهٔ کتانیِ سفید و نازک، از فارسی karbas». کلاین نیز (ص ۲۳۸) «عربی kirbās» را در کنار «فارسی نو kirpās» و «ارمنی kerpas» می‌نشاند. این واژه در عربی کهن است و با بازرگانی پارچهٔ دورهٔ خلافت گسترده شده. ادعای نورایی درست است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%DA%A9%D8%B1%D8%A8%D8%A7%D8%B3\"],\n \"ref_check\": [\n   {\"ref\": \"MON:2932\", \"status\": \"supports\",\n    \"note\": \"MON_part2.txt line 21636 s.v. کرباس: '[هند. کرپاس ـ معر. کرپاس]' — 'مُعَرَّب کرپاس', i.e. Mo'in states in so many words that the b-form is the Arabicised shape of karpās, which is exactly the arrow Nourai draws. (Printed page 2932 of the six-volume set not checkable in the local abridgement.)\"},\n   {\"ref\": \"KLN:238\", \"status\": \"supports\",\n    \"note\": \"Klein s.v. carbasus (leaf 238-239): '… whence also ModPers. kirpās, Arm. kerpas, Arab. kirbās, Heb. karpas (Esther 1:6), „cotton, fine linen“.'\"}\n ],\n \"consulted\": [\n   {\"src\": \"PLA\", \"where\": \"Asbaghi p.227 (PLA_pages.txt lines 12760 ff.; the running number 227 stands at line 12708)\", \"stance\": \"supports\",\n    \"note\": \"'kirbās: „feine weiße Leinwand“ pers. karbas, syr. …, hebr. …' — listed as a Persian loanword in Arabic. (Asbaghi's footnote 5 'Mackenzie s.v.' misfires: MacKenzie's karbāš means 'lizard'.)\"},\n   {\"src\": \"HUB\", \"where\": \"Persische Studien p.130\", \"stance\": \"supports\",\n    \"note\": \"'np. kirpās, arab. kirbās' — Hübschmann sets the Arabic form beside the Persian one in a single foreign-word group.\"},\n   {\"src\": \"AFM\", \"where\": \"Addi Shir, Kitāb al-alfāẓ al-fārisiyya al-muʿarraba\", \"stance\": \"silent\",\n    \"note\": \"grep of AFM.txt / AFM_pages.txt for كرباس / الكرباس returns no hit; Addi Shir does not list it among his Persian arabicisms in the copy on disk.\"},\n   {\"src\": \"AFA\", \"where\": \"Fraenkel, Die aramäischen Fremdwörter im Arabischen\", \"stance\": \"silent\",\n    \"note\": \"grep of AFA.txt for karbas/kirbas returns nothing in the OCR available.\"}\n ]\n})\n\ne2[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Persian\", \"words\": \"karbâs «کرباس»\", \"verdict\": \"plausible\",\n \"derivation\": \"Modern Persian کرباس karbās 'coarse cotton cloth, calico' — the form quoted in the chart from Vaḥshī ('وگر چرخ اطلس رود بر خلافت / روانی چو کرباسش از هم درانی'). Nourai makes it a re-borrowing: Persian karpās > Arabic kirbās > Persian karbās, an Arabic-mediated round trip, and the b for p is precisely the fingerprint such a round trip leaves. Mo'in endorses that reading explicitly — 'کرباس [هند. کرپاس ـ معرَّب کرپاس]', 'the Arabicised form of karpās' — and the coexistence in Persian of the learned کرپاس beside the everyday کرباس is the classic doublet pattern of معرَّب returns (compare فارسی/پارسی). The alternative, and the one Wiktionary prefers, is that کرباس is simply inherited: 'from Middle Persian, from Sanskrit करà¥पास (karpāsa)', with the p/b variation internal to Persian and the Arabic form a borrowing from that. Neither can be proved from the shape alone, since Persian tolerates p ~ b in loanwords; hence 'plausible'. What is not in doubt is the ultimate Indian origin and the Persian–Arabic mutual traffic.\",\n \"derivation_fa\": \"«کرباس» فارسی نو به معنی «پارچهٔ پنبه‌ای درشت»، همان صورتی که در بیت وحشی آمده است. نورایی آن را وام‌گیری دوباره می‌داند: کرپاس فارسی ← کِرباس عربی ← کرباس فارسی؛ یعنی یک رفت‌وبرگشت از راه عربی، و «ب» به‌جای «پ» درست همان اثر انگشتی است که چنین رفت‌وبرگشتی بر جای می‌گذارد. معین همین خوانش را تأیید می‌کند: «کرباس [هند. کرپاس ـ معرّب کرپاس]»؛ و هم‌زیستی «کرپاسِ» کتابی با «کرباسِ» روزمره در فارسی همان الگوی دوگانه‌سازی (doublet) واژه‌های معرّب بازگشته است (مانند پارسی/فارسی). دیدگاه دیگر، که ویکی‌واژه بر آن است، این است که «کرباس» یکسره موروثی است و از فارسی میانه و از سنسکریت karpāsa می‌آید و صورت عربی از آن گرفته شده است. از روی خودِ صورت واژه نمی‌توان میان این دو داوری کرد، چون فارسی در وام‌واژه‌ها پ و ب را به‌آسانی جابه‌جا می‌کند؛ ازاین‌رو ادعای نورایی «با احتیاط پذیرفتنی» است. آنچه تردیدی در آن نیست، خاستگاه هندی واژه و داد و ستد دوسویهٔ فارسی و عربی است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%DA%A9%D8%B1%D8%A8%D8%A7%D8%B3\"],\n \"ref_check\": [\n   {\"ref\": \"MON:2932\", \"status\": \"supports\",\n    \"note\": \"MON_part2.txt line 21636: 'کرباس: [هند. کرپاس ـ معر. کرپاس] (ا.) پارچهٔ پنبه‌یی سفید و ارزان قیمت. سروته یک کرباس بودن: (عم.) مساوی هم بودن' — the etymological bracket ('Indian karpās, Arabicised karpās') is Nourai's whole chain in four words, and the gloss 'cheap white cotton cloth' matches his 'cotton cloth'. The cited page number could not be checked against the two-volume abridgement on disk.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"s.v. کرباس and کرباس‌محله (MON_part2.txt lines 21636-21646)\", \"stance\": \"supports\",\n    \"note\": \"Mo'in also has the derivative 'کرباس محله … (کد.) قبرستان، گورستان (به مناسبت کفن‌های کرباس)' — proof the word is fully naturalised in colloquial Persian.\"},\n   {\"src\": \"Wiktionary (Persian)\", \"where\": \"en.wiktionary.org/wiki/کرباس\", \"stance\": \"partial\",\n    \"note\": \"'Inherited from Middle Persian, from Sanskrit कर्पास (karpāsa)'; alternative forms کرواس (karvâs) and کرپاس (karpâs); 'cotton-cloth, canvas'. Same origin, but no Arabic detour — a compatible but not identical picture.\"},\n   {\"src\": \"PLA\", \"where\": \"Asbaghi p.227\", \"stance\": \"partial\",\n    \"note\": \"Asbaghi has the traffic running Persian > Arabic only (kirbās < pers. karbas), so for him the modern Persian karbās is not a return loan.\"},\n   {\"src\": \"BQT\", \"where\": \"Borhan-e Qate', vols 3-4\", \"stance\": \"silent\",\n    \"note\": \"grep for کرباس in BQT_v3_pages.txt / BQT_v4_pages.txt returns only کرباسه/کرباسو 'lizard, gecko' (v3 line 29635 ff.), a different word; no cotton-cloth entry surfaced in the OCR.\"}\n ]\n})\n\ne2[\"nodes\"].append({\n \"id\": 4, \"lang\": \"Greek\", \"words\": \"karpasos\", \"verdict\": \"plausible\",\n \"derivation\": \"Ancient Greek κάρπασος kárpasos, LSJ 'fine flax; cotton', is certainly the same culture word, but the arrow drawn straight from Sanskrit is only one of three current accounts. (i) Klein p.238, Nourai's own source, says it 'is prob. borrowed fr. OI karpāsaḥ' — the traditional view Nourai follows, and the one Hobson-Jobson also assumes ('Skt. karpasa, which seems as if it must be the origin of κάρπασος, though the latter is applied to flax'). (ii) Klein on the same page reports Porzig's rival view that 'both OI karpāsaḥ and Gk. κάρπασος derive from a language of the Mediterranean or Asia Minor', and Buck p.402 adopts exactly this: Sanskrit is itself 'a loanword fr. the same source as Grk. κάρπασος'. (iii) Current Wiktionary makes Greek a borrowing from Biblical Hebrew כַּרְפַּס karpás (Esther 1:6, of the hangings in Ahasuerus's palace) — which would give a Semitic transmission route westward rather than a direct Indian one. Chronology favours some intermediary: the Greek word is attested from the Hellenistic period in the sense 'flax', and the semantic split (Greek 'flax' vs Sanskrit 'cotton') is easier to explain through a trade language than through a direct loan. Hence 'plausible'.\",\n \"derivation_fa\": \"یونانی باستان κάρπασος (kárpasos)، که در فرهنگ لیدل-اسکات «کتان نازک؛ پنبه» معنی شده، بی‌گمان همان واژهٔ فرهنگی مهاجر است، اما پیکانی که نورایی یکراست از سنسکریت به آن کشیده تنها یکی از سه دیدگاه امروزی است. نخست: کلاین (ص ۲۳۸)، یعنی خودِ منبع نورایی، می‌نویسد «احتمالاً از سنسکریت karpāsaḥ وام گرفته شده» — همان دیدگاه سنتی. دوم: کلاین در همان صفحه رأی پورتزیش را می‌آورد که «هم karpāsaḥ سنسکریت و هم κάρπασος یونانی از زبانی مدیترانه‌ای یا آسیای صغیری‌اند»، و باک (ص ۴۰۲) نیز همین را می‌پذیرد. سوم: ویکی‌واژهٔ امروزی یونانی را وام‌گرفته از عبری کتاب مقدس כַּרְפַּס (استر ۱:۶) می‌داند، یعنی راهی سامی به سوی باختر. گاه‌شماری هم به سود وجود واسطه است: واژهٔ یونانی از دورهٔ هلنیستی و به معنی «کتان» گواهی شده، و این جدایی معنایی (کتان در یونانی در برابر پنبه در سنسکریت) از راه زبانی بازرگانی آسان‌تر توضیح داده می‌شود تا از راه وام‌گیری مستقیم. پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%CE%BA%CE%AC%CF%81%CF%80%CE%B1%CF%83%CE%BF%CF%82\", \"https://en.wiktionary.org/wiki/carbasus\"],\n \"ref_check\": [\n   {\"ref\": \"KLN:238\", \"status\": \"partial\",\n    \"note\": \"KLN_1966.txt line 6504 (leaf 238-239): 'Gk. κάρπασος, „flax, cotton“, which is prob. borrowed fr. OI karpāsaḥ … According to Porzig in Zeitschrift für Indologie und Iranistik, 5, 272 ff., both OI karpāsaḥ and Gk. κάρπασος derive from a language of the Mediterranean or Asia Minor.' Klein states Nourai's arrow but immediately records the competing origin, so 'partial' rather than 'supports'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"SYN\", \"where\": \"Buck p.402 §6.24 item 5\", \"stance\": \"contradicts\",\n    \"note\": \"'Skt. karpāsa-, loanword fr. the same source as Grk. κάρπασος, Lat. carbasus … Walde-H. 1.165.' — for Buck the Greek is a sister borrowing, not a daughter of Sanskrit.\"},\n   {\"src\": \"HJB\", \"where\": \"s.v. CAPAS (HJB.txt line 5165)\", \"stance\": \"partial\",\n    \"note\": \"'H. kapas, from Skt. karpasa, which seems as if it must be the origin of κάρπασος, though the latter is applied to flax.' Yule/Burnell accept the link but flag the semantic mismatch.\"},\n   {\"src\": \"Wiktionary (Ancient Greek)\", \"where\": \"en.wiktionary.org/wiki/κάρπασος\", \"stance\": \"partial\",\n    \"note\": \"'Borrowed from Biblical Hebrew כַּרְפַּס (karpás, „a type of expensive fabric made of cotton“)'; glossed 'flax (Linum usitatissimum or L. bienne) or cotton'. Same word-family, different immediate donor.\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. carbasus (LAT.txt lines 9840-9852)\", \"stance\": \"supports\",\n    \"note\": \"'L\\\\'identité de sens et de forme avec gr. κάρπασος, au b près, est frappante' — confirms the Greek word and its shape.\"}\n ]\n})\n\ne2[\"nodes\"].append({\n \"id\": 5, \"lang\": \"Latin\", \"words\": \"\", \"verdict\": \"confirmed\",\n \"derivation\": \"Pass-through node: Latin carbasus, -ī f. 'fine linen, cambric; by extension a sail, an awning, a curtain', with the collective plural carbasa n. Borrowed from Greek κάρπασος, with the one irregularity that gives the loan away — Greek π appears as Latin b. Klein explains it on the cited page: 'For the change of Greek π to b in Latin — which is prob. due to Etruscan influence — cp. burro, carbasus and sbirro', i.e. the word came into Latin through an Etruscan-mediated channel like buxus/box, purrhos/birrus. Ernout-Meillet, s.v.: 'L'identité de sens et de forme avec gr. κάρπασος, au b près, est frappante', noting also the learned doublets carpaseus, carpasinus which preserve the p. Attested from Ennius, rare in prose, and famous from Virgil (Aeneid: the carbasa of the Trojan sails); derivatives carbaseus, -sinus, -sineus.\",\n \"derivation_fa\": \"این گره حلقه‌ای واسطه است و واژه‌ای در برابر آن نیامده: لاتین carbasus (مؤنث) به معنی «کتان نازک، پارچهٔ ظریف» و به گسترش معنایی «بادبان، سایبان، پرده»، با جمع جمعیِ carbasa. این واژه از یونانی κάρπασος وام گرفته شده، با یک بی‌قاعدگی که خود گواه وام‌گیری است: «پ» یونانی در لاتین «ب» شده است. کلاین در همان صفحهٔ ۲۳۸ توضیح می‌دهد: «دربارهٔ تبدیل π یونانی به b در لاتین — که احتمالاً از تأثیر اتروسکی است — با burro و carbasus و sbirro بسنجید»؛ یعنی واژه از مجرایی با واسطهٔ اتروسکی وارد لاتین شده است. ارنو و مِیه نیز می‌نویسند «همانندی معنا و صورت با κάρπασος یونانی، جز در «ب»، چشمگیر است» و به گونه‌های کتابی carpaseus و carpasinus اشاره می‌کنند که «پ» را نگه داشته‌اند. این واژه از انیوس گواهی شده و کاربرد مشهور آن در «انئید» ویرژیل است. ادعای نورایی درست است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/carbasus\"],\n \"ref_check\": [\n   {\"ref\": \"KLN:238\", \"status\": \"supports\",\n    \"note\": \"KLN_1966.txt line 6504 (leaf 238-239): 'carbasus, n., lint. — L., fr. Gk. κάρπασος, „flax, cotton“' and, s.v. box (line 5477), 'For the change of Greek π to b in Latin — which is prob. due to Etruscan influence — cp. burro, carbasus and sbirro.' Both the Greek > Latin arrow and its phonetics are on Klein's pages.\"}\n ],\n \"consulted\": [\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. carbasus (LAT.txt lines 9841-9852)\", \"stance\": \"supports\",\n    \"note\": \"'carbasus, -i f.; pl. collectif carbasa n. … étoffe de lin qui servait de vêtement aux divinités fluviales … et dont on faisait aussi les voiles des vaisseaux ou les pare-soleil des théâtres. Attesté depuis Ennius; rare en prose. … L\\\\'identité de sens et de forme avec gr. κάρπασος, au b près, est frappante … Dérivés: carbaseus, -sinus, -sineus.'\"},\n   {\"src\": \"SYN\", \"where\": \"Buck p.402 §6.24 item 5\", \"stance\": \"partial\",\n    \"note\": \"'Lat. carbasus „fine cotton cloth“' is listed, but as a parallel borrowing from the common source rather than specifically from Greek.\"},\n   {\"src\": \"LEW\", \"where\": \"Walde, Lateinisches etym. Wörterbuch (LEW_1910.txt)\", \"stance\": \"silent\",\n    \"note\": \"grep for 'carbasus' in the OCR on disk returns no hit (the volume text is incomplete at that point).\"}\n ]\n})\n\ne2[\"nodes\"].append({\n \"id\": 6, \"lang\": \"English\", \"words\": \"carbasus\", \"verdict\": \"confirmed\",\n \"derivation\": \"English carbasus 'lint' is a learned, essentially technical borrowing of the Latin word, taken over unchanged in form and narrowed in sense: from Latin carbasus 'fine linen' to the surgical 'lint, linen scrapings used for dressing wounds'. Klein, on the page Nourai cites, gives the whole entry in one line: 'carbasus, n., lint. — L., fr. Gk. κάρπασος, „flax, cotton“' — headword, gloss and etymology exactly as charted. It is a dictionary word rather than a living one (Skeat, who prints only words in general use, has no entry for it), which is why the chart's gloss 'lint' looks so narrow: it is Klein's gloss verbatim.\",\n \"derivation_fa\": \"واژهٔ انگلیسی carbasus به معنی «نخِ پارچهٔ زخم‌بندی» وام‌واژه‌ای کتابی و در عمل فنی از لاتین است: صورت واژه دست‌نخورده مانده و معنا تنگ‌تر شده — از «کتان نازک» لاتینی به «الیاف کتان برای بستن زخم» در پزشکی. کلاین در همان صفحه‌ای که نورایی یاد کرده، همهٔ مدخل را در یک سطر می‌آورد: «carbasus، اسم، lint. — از لاتین، از یونانی κάρπασος «کتان، پنبه»» — یعنی سرواژه و معنا و ریشه دقیقاً همان است که در نمودار آمده. این واژه بیشتر واژه‌ای فرهنگ‌نامه‌ای است تا زنده (اسکیت که تنها واژه‌های رایج را می‌آورد، مدخلی برای آن ندارد)، و همین توضیح می‌دهد که چرا معنای «lint» در نمودار این‌قدر تنگ است: عیناً معنای کلاین است. ادعای نورایی درست است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/carbasus\"],\n \"ref_check\": [\n   {\"ref\": \"KLN:238\", \"status\": \"supports\",\n    \"note\": \"KLN_1966.txt line 6504 (leaf 238-239): 'carbasus, n., lint. — L., fr. Gk. κάρπασος, „flax, cotton“, which is prob. borrowed fr. OI karpāsaḥ …'. Nourai's node reproduces Klein's headword and gloss word for word.\"}\n ],\n \"consulted\": [\n   {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict.\", \"stance\": \"silent\",\n    \"note\": \"grep of SKT.txt for 'carbasus' returns nothing — not a word of general English currency.\"},\n   {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls vols 1-4\", \"stance\": \"silent\",\n    \"note\": \"grep of FSD_vol1.txt for 'carbasus' returns nothing in the OCR available at this point of the C section.\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. carbasus\", \"stance\": \"supports\",\n    \"note\": \"Confirms the Latin sense 'étoffe de lin' out of which the English medical 'lint' is narrowed.\"}\n ]\n})\ndata[\"entries\"].append(e2)\nPYEOF\necho built-part2"
}
```


### [2026-09-06T16:04:49.630Z] TOOL RESULT

```
<tool_use_error>InputValidationError: [
  {
    "code": "custom",
    "path": [
      "command"
    ],
    "message": "command contains control characters that would be hidden in the approval dialog"
  }
]</tool_use_error>
```


## [2026-09-06T16:07:36.059Z] TOOL CALL #62: Write

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/part2.py",
 "content": "# -*- coding: utf-8 -*-\n\ndef build(data):\n e2 = {\n  \"entry\": 2,\n  \"root\": \"Karpasah\",\n  \"verdict\": \"plausible\",\n  \"modern_form\": \"Sanskrit कर्पास karpāsa- m./n. 'cotton, cotton plant' (nom. sg. karpāsaḥ) — itself a culture word of unknown, probably non-Indo-Aryan origin\",\n  \"note\": \"The headword is real and correctly glossed: Sanskrit karpāsa- 'cotton, cotton tree' (Nourai's 'Karpâsah' is the nominative singular karpāsaḥ, not the stem). What makes the box 'plausible' rather than 'confirmed' is that Nourai treats Sanskrit as the fountain-head of the whole tree, and the very reference he cites for it says otherwise. Buck, Selected Synonyms p.402 §6.24 COTTON, item 5 reads: 'Skt. karpāsa-, loanword fr. the same source as Grk. κάρπασος, Lat. carbasus \\\"fine cotton cloth\\\", Arab. kerpas, etc.' — i.e. Sanskrit, Greek and the Semitic forms are for Buck *parallel* borrowings from one unidentified source, not a chain hanging from Sanskrit. Klein p.238 hedges the same way: Gk. κάρπασος 'is prob. borrowed fr. OI karpāsaḥ … According to Porzig … both OI karpāsaḥ and Gk. κάρπασος derive from a language of the Mediterranean or Asia Minor.' Current Wiktionary routes Greek through Biblical Hebrew כַּרְפַּס karpas (Esther 1:6) rather than straight from Sanskrit. The Iranian and Arabic half of Nourai's tree (nodes 1-3) is solid; the Greek/Latin/English half (nodes 4-6) is where the simplification lies. Neither Pokorny nor Walde-Pokorny has the word at all — it is a Wanderwort, not an inherited Indo-European root, and Nourai is right not to label it one.\",\n  \"note_fa\": \"سرواژه درست و معنای آن نیز درست است: سنسکریت کَرپاسَ karpāsa- «پنبه، درخت پنبه» (صورت «Karpâsah» نزد نورایی همان حالت فاعلی مفرد karpāsaḥ است نه ستاک). آنچه این جعبه را «با احتیاط پذیرفتنی» می‌کند این است که نورایی سنسکریت را سرچشمهٔ همهٔ شاخه‌ها گرفته، حال آنکه همان منبعی که خود او یاد کرده خلاف این را می‌گوید: باک در صفحهٔ ۴۰۲ می‌نویسد سنسکریت karpāsa- خود وام‌واژه است، از همان سرچشمه‌ای که یونانی κάρπασος و لاتین carbasus و عربی kirbās از آن آمده‌اند. کلاین (ص ۲۳۸) نیز با احتیاط می‌نویسد یونانی «احتمالاً» از سنسکریت است و به رأی پورتزیش اشاره می‌کند که هر دو را از زبانی مدیترانه‌ای یا آسیای صغیری می‌داند؛ ویکی‌واژهٔ امروزی نیز یونانی را از عبری کتاب مقدس כַּרְפַּס (استر ۱:۶) می‌گیرد نه یکراست از سنسکریت. نیمهٔ ایرانی و عربیِ درخت (گره‌های ۱ تا ۳) استوار است و اشکال در نیمهٔ یونانی-لاتینی است. این واژه در پوکورنی و والده-پوکورنی اصلاً نیامده، چون واژه‌ای فرهنگی و مهاجر (Wanderwort) است نه ریشهٔ هندواروپایی — و نورایی درست کرده که آن را ریشهٔ هندواروپایی ننامیده است.\",\n  \"sources\": [\"https://en.wiktionary.org/wiki/%CE%BA%CE%AC%CF%81%CF%80%CE%B1%CF%83%CE%BF%CF%82\", \"https://en.wiktionary.org/wiki/carbasus\", \"https://en.wiktionary.org/wiki/%DA%A9%D8%B1%D8%A8%D8%A7%D8%B3\"],\n  \"ref_check\": [\n    {\"ref\": \"KLN:238\", \"status\": \"partial\",\n     \"note\": \"Klein 1966, s.v. carbasus, on the leaf carrying printed pp.238-239 (KLN_1966.txt line 6504, between the page markers '237' at line 6470 and '238' at line 6507): 'carbasus, n., lint. — L., fr. Gk. κάρπασος, \\\"flax, cotton\\\", which is prob. borrowed fr. OI karpāsaḥ, \\\"cotton brush, cotton\\\", whence also ModPers. kirpās, Arm. kerpas, Arab. kirbās, Heb. karpas (Esther 1:6), \\\"cotton, fine linen\\\". See Manfred Mayrhofer, A Concise Etymological Dictionary, I, p.174 s.v. karpāsaḥ. According to Porzig in Zeitschrift für Indologie und Iranistik, 5, 272 ff., both OI karpāsaḥ and Gk. κάρπασος derive from a language of the Mediterranean or Asia Minor.' Supports the Persian, Arabic and Latin links, but only 'prob.' for the Greek and expressly records the rival non-Indic origin.\"},\n    {\"ref\": \"SYN:402\", \"status\": \"partial\",\n     \"note\": \"Buck, SYN.txt line 10029 ff. — the page header itself reads '402 SELECTED INDO-EUROPEAN SYNONYMS 6.24 COTTON', and the list has 'Skt. karpasa-'. But item 5 of the discussion says: 'Skt. karpāsa-, loanword fr. the same source as Grk. κάρπασος, Lat. carbasus \\\"fine cotton cloth\\\", Arab. kerpas, etc. Walde-H. 1.165.' — the exact page Nourai cites denies that Sanskrit is the source of the Greek and Semitic forms.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"POK_full.txt\", \"stance\": \"silent\",\n     \"note\": \"grep for karpas / karpasa / carbasus returns nothing — Pokorny has no such Indo-European root, as expected for a cotton Wanderwort.\"},\n    {\"src\": \"WLD\", \"where\": \"WLD_band3.txt and WLD_Bd1_1930 djvu text\", \"stance\": \"silent\",\n     \"note\": \"grep for karpasa / carbasus returns nothing in the Walde-Pokorny material on disk.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck §6.24, p.402\", \"stance\": \"partial\",\n     \"note\": \"See ref_check: Buck lists Skt. karpāsa- among the cotton words but calls it itself a loanword; he also notes that most European cotton words come instead from Arabic quṭn.\"},\n    {\"src\": \"HJB\", \"where\": \"s.v. CAPAS (HJB.txt line 5165)\", \"stance\": \"supports\",\n     \"note\": \"'CAPAS, s. The cotton plant and cotton-wool. H. kapas, from Skt. karpasa, which seems as if it must be the origin of κάρπασος, though the latter is applied to flax.' Yule/Burnell affirm the Sanskrit word and the Greek connection, with the same reservation about the flax sense.\"}\n  ],\n  \"nodes\": []\n }\n\n e2[\"nodes\"].append({\n  \"id\": 1, \"lang\": \"Persian\", \"words\": \"karpâs «کَرپاس»\", \"verdict\": \"confirmed\",\n  \"derivation\": \"Persian karpās / kirpās «کرپاس» 'cotton cloth' is the Indian word taken into Iranian, on the evidence of the shape: the -p- is preserved (an inherited Iranian word would have lenited intervocalic p), and the -ās reflects Sanskrit -āsa- exactly. Hübschmann, Persische Studien p.130 sets it out in one line: 'Die Uebereinstimmung von arm. kerpas \\\"feines Linnen\\\" mit np. kirpās, arab. kirbās besagt bei einem Fremdwort (skr. karpāsa-, gr. κάρπασος, lat. carbasus etc.) nicht viel' — New Persian kirpās stands beside Armenian kerpas and Arabic kirbās as reflexes of the same culture word, and Hübschmann expressly classes it as a Fremdwort. Klein p.238 has the same form ('whence also ModPers. kirpās'). Mo'in derives the Persian word from Indian: «کرباس [هند. کرپاس ـ معرّب کرپاس]». The borrowing must be old — cotton reached Iran from India well before the Sasanian period — and Wiktionary treats the word as inherited through Middle Persian from Sanskrit karpāsa.\",\n  \"derivation_fa\": \"«کَرپاس» فارسی به معنی «پارچهٔ پنبه‌ای» همان واژهٔ هندی است که به ایرانی راه یافته، و گواه آن خودِ ساخت واژه است: «پ» میان دو واکه نگه داشته شده (اگر واژه‌ای موروثی و ایرانی بود، در فارسی میانه نرم می‌شد) و پایانهٔ ـās دقیقاً بازتاب ـāsa- سنسکریت است. هوبشمان در «پژوهش‌های فارسی»، صفحهٔ ۱۳۰، می‌نویسد: «همانندی ارمنی kerpas «کتان نازک» با فارسی نو kirpās و عربی kirbās، در واژه‌ای بیگانه (سنسکریت karpāsa-، یونانی κάρπασος، لاتین carbasus) چندان دلیل چیزی نیست» — یعنی او خود این واژه را صریحاً وام‌واژه می‌شمارد. کلاین نیز همین صورت را دارد، و معین می‌نویسد «کرباس [هند. کرپاس ـ معرّب کرپاس]». وام‌گیری باید کهن باشد، چون پنبه پیش از دورهٔ ساسانی از هند به ایران رسیده بود. ادعای نورایی درست است.\",\n  \"sources\": [\"https://en.wiktionary.org/wiki/%DA%A9%D8%B1%D8%A8%D8%A7%D8%B3\"],\n  \"ref_check\": [\n    {\"ref\": \"KLN:238\", \"status\": \"supports\",\n     \"note\": \"Klein s.v. carbasus (KLN_1966.txt line 6504, leaf 238-239): Gk. κάρπασος 'is prob. borrowed fr. OI karpāsaḥ … whence also ModPers. kirpās, Arm. kerpas, Arab. kirbās, Heb. karpas' — the Persian form and its Indian source are named on the cited page.\"},\n    {\"ref\": \"MON:2932\", \"status\": \"supports\",\n     \"note\": \"The local Mo'in is the abridged two-volume Adena reprint, whose pagination differs from the six-volume Amir Kabir set Nourai cites, so the number 2932 itself is unverifiable; the entry is there: MON_part2.txt line 21636 «کرباس: [هند. کرپاس ـ معر. کرپاس] (ا.) پارچهٔ پنبه‌یی سفید و ارزان قیمت» — Mo'in derives it from Indian karpās and marks the b-form as the Arabicised one.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"HUB\", \"where\": \"Persische Studien p.130 (HUB.txt line 4541)\", \"stance\": \"supports\",\n     \"note\": \"'… mit np. kirpās, arab. kirbās besagt bei einem Fremdwort (skr. karpāsa-, gr. κάρπασος, lat. carbasus etc.) nicht viel.' Hübschmann has the Persian form and files the whole group as a foreign culture word.\"},\n    {\"src\": \"HRN\", \"where\": \"Grundriss der neupersischen Etymologie\", \"stance\": \"silent\",\n     \"note\": \"grep of HRN.txt for karpas / karbas / kirbas finds nothing — Horn has no entry, unsurprising since he treats inherited Iranian vocabulary.\"},\n    {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. karbāš (PHD.txt line 424; PHD_mackenzie.txt line 3214)\", \"stance\": \"contradicts\",\n     \"note\": \"MacKenzie's only karbāš is 'karbāš [klbʾš | N karbas, etc.] lizard' — a homonym, not the cloth word; A Concise Pahlavi Dictionary records no Middle Persian 'cotton cloth' karpās. (Asbaghi, PLA p.227, cites 'Mackenzie s.v.' for a Middle Persian karbas — that citation points at this 'lizard' entry and is a slip.)\"}\n  ]\n })\n\n e2[\"nodes\"].append({\n  \"id\": 2, \"lang\": \"Arabic\", \"words\": \"karbâs\", \"verdict\": \"confirmed\",\n  \"derivation\": \"Arabic kirbās «كرباس» (Nourai's 'karbâs') 'coarse white cotton cloth, calico' is the Persian word arabicised. The single diagnostic change is the one Arabic always makes: Arabic has no /p/, so Persian karpās / kirpās becomes kirbās, p being replaced by its voiced labial neighbour b (compare Middle Persian pīl > Arabic fīl, Persian pālūda > Arabic fālūdaj — Arabic renders Iranian p by b or f). The vowelling kirbās, with i in the first syllable, matches the Persian variant kirpās that Klein and Hübschmann cite. Asbaghi, Persische Lehnwörter im Arabischen p.227, lists it among the Persian loans: 'kirbās: \\\"feine weiße Leinwand\\\" pers. karbas, syr. …, hebr. …'. Klein p.238 names 'Arab. kirbās' in the same breath as ModPers. kirpās and Arm. kerpas. The word is old in Arabic and spread with the caliphal textile trade; the same Semitic family includes Hebrew karpas (Esther 1:6) and Syriac karbāsā.\",\n  \"derivation_fa\": \"عربیِ «کِرباس» (kirbās) به معنی «پارچهٔ پنبه‌ای سفید و درشت‌بافت» همان واژهٔ فارسی است که معرّب شده است. تنها دگرگونیِ تشخیص‌دهنده همان است که عربی همیشه انجام می‌دهد: در عربی واج «پ» نیست، پس karpās/kirpās فارسی به kirbās بدل شده و «پ» جای خود را به هم‌جایگاه واک‌دارش «ب» داده است (سنجیدنی با pīl پهلوی که در عربی «فیل» شده و «پالوده» که «فالوذج» شده است). واکهٔ نخستِ kirbās نیز با گونهٔ فارسی kirpās همخوان است. اصباغی در «وام‌واژه‌های فارسی در عربی» صفحهٔ ۲۲۷ آن را در شمار وام‌های فارسی آورده است: «kirbās: پارچهٔ کتانیِ سفیدِ نازک، از فارسی karbas». کلاین نیز (ص ۲۳۸) «عربی kirbās» را در کنار «فارسی نو kirpās» و «ارمنی kerpas» می‌نشاند. ادعای نورایی درست است.\",\n  \"sources\": [\"https://en.wiktionary.org/wiki/%DA%A9%D8%B1%D8%A8%D8%A7%D8%B3\"],\n  \"ref_check\": [\n    {\"ref\": \"MON:2932\", \"status\": \"supports\",\n     \"note\": \"MON_part2.txt line 21636 s.v. کرباس: «[هند. کرپاس ـ معر. کرپاس]» — 'مُعَرَّب کرپاس', i.e. Mo'in states in so many words that the b-form is the Arabicised shape of karpās, exactly the arrow Nourai draws. (Printed page 2932 of the six-volume set is not checkable in the local abridgement.)\"},\n    {\"ref\": \"KLN:238\", \"status\": \"supports\",\n     \"note\": \"Klein s.v. carbasus (leaf 238-239): '… whence also ModPers. kirpās, Arm. kerpas, Arab. kirbās, Heb. karpas (Esther 1:6), \\\"cotton, fine linen\\\".'\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"PLA\", \"where\": \"Asbaghi p.227 (PLA_pages.txt line 12760; the running number 227 stands at line 12708)\", \"stance\": \"supports\",\n     \"note\": \"'kirbās: \\\"feine weiße Leinwand\\\" pers. karbas, syr. …, hebr. …' — listed as a Persian loanword in Arabic. (Asbaghi's footnote 5 'Mackenzie s.v.' misfires: MacKenzie's karbāš means 'lizard'.)\"},\n    {\"src\": \"HUB\", \"where\": \"Persische Studien p.130\", \"stance\": \"supports\",\n     \"note\": \"'np. kirpās, arab. kirbās' — Hübschmann sets the Arabic form beside the Persian one in a single foreign-word group.\"},\n    {\"src\": \"AFM\", \"where\": \"Addi Shir, Kitab al-alfaz al-farisiyya al-mu'arraba\", \"stance\": \"silent\",\n     \"note\": \"grep of AFM.txt / AFM_pages.txt for كرباس / الكرباس returns no hit; Addi Shir does not list it among his Persian arabicisms in the copy on disk.\"},\n    {\"src\": \"AFA\", \"where\": \"Fraenkel, Die aramäischen Fremdwörter im Arabischen\", \"stance\": \"silent\",\n     \"note\": \"grep of AFA.txt for karbas / kirbas returns nothing in the OCR available.\"}\n  ]\n })\n\n e2[\"nodes\"].append({\n  \"id\": 3, \"lang\": \"Persian\", \"words\": \"karbâs «کرباس»\", \"verdict\": \"plausible\",\n  \"derivation\": \"Modern Persian karbās «کرباس» 'coarse cotton cloth, calico' — the form quoted in the chart from Vahshi. Nourai makes it a re-borrowing: Persian karpās > Arabic kirbās > Persian karbās, an Arabic-mediated round trip, and the b for p is exactly the fingerprint such a round trip leaves. Mo'in endorses that reading explicitly — «کرباس [هند. کرپاس ـ معرّب کرپاس]», 'the Arabicised form of karpās' — and the coexistence in Persian of the learned کرپاس beside the everyday کرباس is the classic doublet pattern of mu'arrab returns (compare پارسی / فارسی). The alternative, which Wiktionary prefers, is that کرباس is simply inherited, 'from Middle Persian, from Sanskrit karpāsa', with the p ~ b variation internal to Persian and the Arabic form borrowed from that. Neither can be decided from the shape alone, since Persian tolerates p ~ b in loanwords and the b-form is already ancient in the Semitic area (Hebrew karpas, Syriac karbāsā); hence 'plausible'. The Indian origin and the Persian–Arabic traffic are not in doubt.\",\n  \"derivation_fa\": \"«کرباس» فارسی نو به معنی «پارچهٔ پنبه‌ای درشت»، همان صورتی که در بیت وحشی آمده است. نورایی آن را وام‌گیری دوباره می‌داند: کرپاس فارسی ← کِرباس عربی ← کرباس فارسی؛ یعنی یک رفت‌وبرگشت از راه عربی، و «ب» به‌جای «پ» درست همان اثر انگشتی است که چنین رفت‌وبرگشتی بر جای می‌گذارد. معین همین خوانش را تأیید می‌کند: «کرباس [هند. کرپاس ـ معرّب کرپاس]»؛ و هم‌زیستی «کرپاسِ» کتابی با «کرباسِ» روزمره در فارسی همان الگوی دوگانه‌سازی واژه‌های معرّبِ بازگشته است (مانند پارسی/فارسی). دیدگاه دیگر، که ویکی‌واژه بر آن است، این است که «کرباس» یکسره موروثی است و از فارسی میانه و از سنسکریت karpāsa می‌آید و صورت عربی از آن گرفته شده. از روی خودِ صورت واژه نمی‌توان میان این دو داوری کرد، چون فارسی در وام‌واژه‌ها پ و ب را به‌آسانی جابه‌جا می‌کند و صورت «ب»دار در حوزهٔ سامی (عبری karpas، سریانی karbāsā) کهن است؛ ازاین‌رو ادعای نورایی با احتیاط پذیرفتنی است.\",\n  \"sources\": [\"https://en.wiktionary.org/wiki/%DA%A9%D8%B1%D8%A8%D8%A7%D8%B3\"],\n  \"ref_check\": [\n    {\"ref\": \"MON:2932\", \"status\": \"supports\",\n     \"note\": \"MON_part2.txt line 21636: «کرباس: [هند. کرپاس ـ معر. کرپاس] (ا.) پارچهٔ پنبه‌یی سفید و ارزان قیمت. سروته یک کرباس بودن: (عم.) مساوی هم بودن» — the etymological bracket ('Indian karpās, Arabicised karpās') is Nourai's whole chain in four words, and the gloss 'cheap white cotton cloth' matches his 'cotton cloth'. The cited page number could not be checked against the two-volume abridgement on disk.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"MON\", \"where\": \"s.vv. کرباس, کرباس‌محله (MON_part2.txt lines 21636-21646)\", \"stance\": \"supports\",\n     \"note\": \"Mo'in also has the derivative «کرباس محله … (کد.) قبرستان، گورستان (به مناسبت کفن‌های کرباس)» — proof the word is fully naturalised in colloquial Persian.\"},\n    {\"src\": \"Wiktionary (Persian)\", \"where\": \"en.wiktionary.org/wiki/کرباس\", \"stance\": \"partial\",\n     \"note\": \"'Inherited from Middle Persian, from Sanskrit karpāsa'; alternative forms کرواس (karvâs) and کرپاس (karpâs); glossed 'cotton-cloth, canvas'. Same ultimate origin, but no Arabic detour — a compatible but not identical picture.\"},\n    {\"src\": \"PLA\", \"where\": \"Asbaghi p.227\", \"stance\": \"partial\",\n     \"note\": \"Asbaghi has the traffic running Persian > Arabic only (kirbās < pers. karbas), so for him the modern Persian karbās is not a return loan.\"},\n    {\"src\": \"BQT\", \"where\": \"Borhan-e Qate', vols 3-4 (BQT_v3_pages.txt line 29635 ff.)\", \"stance\": \"silent\",\n     \"note\": \"grep for کرباس in BQT_v3_pages.txt / BQT_v4_pages.txt returns only کرباسه / کرباسو 'lizard, gecko' — a different word; no cotton-cloth entry surfaced in the OCR.\"}\n  ]\n })\n\n e2[\"nodes\"].append({\n  \"id\": 4, \"lang\": \"Greek\", \"words\": \"karpasos\", \"verdict\": \"plausible\",\n  \"derivation\": \"Ancient Greek κάρπασος kárpasos, LSJ 'fine flax; cotton', is certainly the same culture word, but the arrow drawn straight from Sanskrit is only one of three current accounts. (i) Klein p.238, Nourai's own source, says it 'is prob. borrowed fr. OI karpāsaḥ' — the traditional view Nourai follows, which Hobson-Jobson also assumes ('Skt. karpasa, which seems as if it must be the origin of κάρπασος, though the latter is applied to flax'). (ii) Klein on the same page reports Porzig's rival view that 'both OI karpāsaḥ and Gk. κάρπασος derive from a language of the Mediterranean or Asia Minor', and Buck p.402 adopts exactly this: Sanskrit is itself 'a loanword fr. the same source as Grk. κάρπασος'. (iii) Current Wiktionary makes Greek a borrowing from Biblical Hebrew karpás (Esther 1:6, of the hangings in Ahasuerus's palace), a Semitic transmission route westward rather than a direct Indian one. Chronology favours some intermediary: the Greek word is attested in the sense 'flax', and the semantic split (Greek 'flax' vs Sanskrit 'cotton') is easier to explain through a trade language than through a direct loan. Hence 'plausible'.\",\n  \"derivation_fa\": \"یونانی باستان κάρπασος (kárpasos)، که در فرهنگ لیدل-اسکات «کتان نازک؛ پنبه» معنی شده، بی‌گمان همان واژهٔ فرهنگیِ مهاجر است، اما پیکانی که نورایی یکراست از سنسکریت به آن کشیده تنها یکی از سه دیدگاه امروزی است. نخست: کلاین (ص ۲۳۸)، یعنی خودِ منبع نورایی، می‌نویسد «احتمالاً از سنسکریت karpāsaḥ وام گرفته شده». دوم: کلاین در همان صفحه رأی پورتزیش را می‌آورد که «هم karpāsaḥ سنسکریت و هم κάρπασος یونانی از زبانی مدیترانه‌ای یا آسیای صغیری‌اند»، و باک (ص ۴۰۲) نیز همین را می‌پذیرد. سوم: ویکی‌واژهٔ امروزی یونانی را وام‌گرفته از عبری کتاب مقدس כַּרְפַּס (استر ۱:۶) می‌داند، یعنی راهی سامی به سوی باختر. گاه‌شماری و نیز جدایی معنایی (کتان در یونانی در برابر پنبه در سنسکریت) به سود وجود واسطه است. پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n  \"sources\": [\"https://en.wiktionary.org/wiki/%CE%BA%CE%AC%CF%81%CF%80%CE%B1%CF%83%CE%BF%CF%82\", \"https://en.wiktionary.org/wiki/carbasus\"],\n  \"ref_check\": [\n    {\"ref\": \"KLN:238\", \"status\": \"partial\",\n     \"note\": \"KLN_1966.txt line 6504 (leaf 238-239): 'Gk. κάρπασος, \\\"flax, cotton\\\", which is prob. borrowed fr. OI karpāsaḥ … According to Porzig in Zeitschrift für Indologie und Iranistik, 5, 272 ff., both OI karpāsaḥ and Gk. κάρπασος derive from a language of the Mediterranean or Asia Minor.' Klein states Nourai's arrow but immediately records the competing origin, so 'partial' rather than 'supports'.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"SYN\", \"where\": \"Buck p.402 §6.24 item 5\", \"stance\": \"contradicts\",\n     \"note\": \"'Skt. karpāsa-, loanword fr. the same source as Grk. κάρπασος, Lat. carbasus … Walde-H. 1.165.' — for Buck the Greek is a sister borrowing, not a daughter of Sanskrit.\"},\n    {\"src\": \"HJB\", \"where\": \"s.v. CAPAS (HJB.txt line 5165)\", \"stance\": \"partial\",\n     \"note\": \"'H. kapas, from Skt. karpasa, which seems as if it must be the origin of κάρπασος, though the latter is applied to flax.' Yule/Burnell accept the link but flag the semantic mismatch.\"},\n    {\"src\": \"Wiktionary (Ancient Greek)\", \"where\": \"en.wiktionary.org/wiki/κάρπασος\", \"stance\": \"partial\",\n     \"note\": \"'Borrowed from Biblical Hebrew karpás, a type of expensive fabric made of cotton'; glossed 'flax (Linum usitatissimum or L. bienne) or cotton'. Same word-family, different immediate donor.\"},\n    {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. carbasus (LAT.txt lines 9840-9852)\", \"stance\": \"supports\",\n     \"note\": \"\\\"L'identite de sens et de forme avec gr. κάρπασος, au b pres, est frappante\\\" — confirms the Greek word and its shape.\"}\n  ]\n })\n\n e2[\"nodes\"].append({\n  \"id\": 5, \"lang\": \"Latin\", \"words\": \"\", \"verdict\": \"confirmed\",\n  \"derivation\": \"Pass-through node with no word printed in the box: Latin carbasus, -ī f. 'fine linen, cambric; by extension a sail, an awning, a curtain', collective plural carbasa n. Borrowed from Greek κάρπασος, with the one irregularity that gives the loan away — Greek π appears as Latin b. Klein explains it on the cited page: 'For the change of Greek π to b in Latin — which is prob. due to Etruscan influence — cp. burro, carbasus and sbirro', i.e. the word entered Latin through an Etruscan-mediated channel, like buxus/box and Greek pyrrhos > Late Latin birrus. Ernout-Meillet, s.v.: \\\"L'identite de sens et de forme avec gr. κάρπασος, au b pres, est frappante\\\", noting also the learned doublets carpaseus, carpasinus which keep the p. Attested from Ennius, rare in prose, famous from Virgil's Aeneid (the carbasa of the Trojan sails); derivatives carbaseus, -sinus, -sineus.\",\n  \"derivation_fa\": \"این گره حلقه‌ای واسطه است و واژه‌ای در برابر آن چاپ نشده: لاتین carbasus (مؤنث) به معنی «کتان نازک، پارچهٔ ظریف» و به گسترش معنایی «بادبان، سایبان، پرده»، با جمعِ جمعیِ carbasa. این واژه از یونانی κάρπασος وام گرفته شده، با یک بی‌قاعدگی که خود گواه وام‌گیری است: «پ» یونانی در لاتین «ب» شده است. کلاین در همان صفحهٔ ۲۳۸ توضیح می‌دهد: «دربارهٔ تبدیل π یونانی به b در لاتین — که احتمالاً از تأثیر اتروسکی است — با burro و carbasus و sbirro بسنجید». ارنو و مِیه نیز می‌نویسند «همانندی معنا و صورت با κάρπασος یونانی، جز در «ب»، چشمگیر است» و به گونه‌های کتابیِ carpaseus و carpasinus اشاره می‌کنند که «پ» را نگه داشته‌اند. این واژه از انیوس گواهی شده و کاربرد مشهور آن در «انئید» ویرژیل است. ادعای نورایی درست است.\",\n  \"sources\": [\"https://en.wiktionary.org/wiki/carbasus\"],\n  \"ref_check\": [\n    {\"ref\": \"KLN:238\", \"status\": \"supports\",\n     \"note\": \"KLN_1966.txt line 6504 (leaf 238-239): 'carbasus, n., lint. — L., fr. Gk. κάρπασος, \\\"flax, cotton\\\"'; and s.v. box (line 5477) 'For the change of Greek π to b in Latin — which is prob. due to Etruscan influence — cp. burro, carbasus and sbirro.' Both the Greek > Latin arrow and its phonetics are on Klein's pages.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. carbasus (LAT.txt lines 9841-9852)\", \"stance\": \"supports\",\n     \"note\": \"'carbasus, -i f.; pl. collectif carbasa n. … etoffe de lin qui servait de vetement aux divinites fluviales … et dont on faisait aussi les voiles des vaisseaux ou les pare-soleil des theatres. Atteste depuis Ennius; rare en prose. … Derives: carbaseus, -sinus, -sineus.'\"},\n    {\"src\": \"SYN\", \"where\": \"Buck p.402 §6.24 item 5\", \"stance\": \"partial\",\n     \"note\": \"'Lat. carbasus \\\"fine cotton cloth\\\"' is listed, but as a parallel borrowing from the common source rather than specifically from Greek.\"},\n    {\"src\": \"LEW\", \"where\": \"Walde, Lateinisches etymologisches Wörterbuch (LEW_1910.txt)\", \"stance\": \"silent\",\n     \"note\": \"grep for 'carbasus' in the OCR on disk returns no hit; the volume text is defective at that point.\"}\n  ]\n })\n\n e2[\"nodes\"].append({\n  \"id\": 6, \"lang\": \"English\", \"words\": \"carbasus\", \"verdict\": \"confirmed\",\n  \"derivation\": \"English carbasus 'lint' is a learned, essentially technical borrowing of the Latin word, taken over unchanged in form and narrowed in sense: from Latin carbasus 'fine linen' to the surgical 'lint, linen scrapings used for dressing wounds'. Klein, on the page Nourai cites, gives the whole entry in one line: 'carbasus, n., lint. — L., fr. Gk. κάρπασος, \\\"flax, cotton\\\"' — headword, gloss and etymology exactly as charted. It is a dictionary word rather than a living one (Skeat, who prints only words in general use, has no entry), which is why the chart's gloss 'lint' looks so narrow: it is Klein's gloss verbatim. Note that Nourai's node skips the French/Old French stage because there is none — this is a direct Latin borrowing into learned English, unlike caracal and camphor on the same page.\",\n  \"derivation_fa\": \"واژهٔ انگلیسی carbasus به معنی «نخِ پارچهٔ زخم‌بندی» وام‌واژه‌ای کتابی و در عمل فنی از لاتین است: صورت واژه دست‌نخورده مانده و معنا تنگ‌تر شده — از «کتان نازک» لاتینی به «الیاف کتان برای بستن زخم» در پزشکی. کلاین در همان صفحه‌ای که نورایی یاد کرده، همهٔ مدخل را در یک سطر می‌آورد: «carbasus، اسم، lint. — از لاتین، از یونانی κάρπασος «کتان، پنبه»» — یعنی سرواژه و معنا و ریشه دقیقاً همان است که در نمودار آمده. این واژه بیشتر واژه‌ای فرهنگ‌نامه‌ای است تا زنده (اسکیت که تنها واژه‌های رایج را می‌آورد مدخلی برای آن ندارد). برخلاف caracal و camphor در همین صفحه، اینجا حلقهٔ فرانسوی وجود ندارد و وام‌گیری مستقیم از لاتینِ کتابی است. ادعای نورایی درست است.\",\n  \"sources\": [\"https://en.wiktionary.org/wiki/carbasus\"],\n  \"ref_check\": [\n    {\"ref\": \"KLN:238\", \"status\": \"supports\",\n     \"note\": \"KLN_1966.txt line 6504 (leaf 238-239): 'carbasus, n., lint. — L., fr. Gk. κάρπασος, \\\"flax, cotton\\\", which is prob. borrowed fr. OI karpāsaḥ …'. Nourai's node reproduces Klein's headword and gloss word for word.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etymological Dictionary\", \"stance\": \"silent\",\n     \"note\": \"grep of SKT.txt for 'carbasus' returns nothing — not a word of general English currency.\"},\n    {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls vol. I\", \"stance\": \"silent\",\n     \"note\": \"grep of FSD_vol1.txt for 'carbasus' returns nothing in the OCR at this point of the C section.\"},\n    {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. carbasus\", \"stance\": \"supports\",\n     \"note\": \"Confirms the Latin sense 'etoffe de lin' out of which the English medical 'lint' is narrowed.\"}\n  ]\n })\n\n data[\"entries\"].append(e2)\n"
}
```


### [2026-09-06T16:07:36.116Z] TOOL RESULT

```
File created successfully at: /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/part2.py (file state is current in your context — no need to Read it back)
```


## [2026-09-06T16:07:37.880Z] AGENT

Now part 3 (the camphor entry).


## [2026-09-06T16:11:44.454Z] TOOL CALL #63: Write

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/part3.py",
 "content": "# -*- coding: utf-8 -*-\n\ndef build(data):\n e3 = {\n  \"entry\": 3,\n  \"root\": \"Karpurah, Karpŭrah\",\n  \"verdict\": \"plausible\",\n  \"modern_form\": \"Sanskrit कर्पूर karpūra- m./n. 'camphor' (nom. sg. karpūraḥ), itself a loan from an Austronesian/Austroasiatic source, cf. Malay kapur (Barus) 'camphor, chalk'\",\n  \"note\": \"The Sanskrit word is real and is genuinely the hinge of the whole western chain, but two things keep the box from 'confirmed'. First the gloss: karpūra- means 'camphor', the resin/crystal, not 'camphor tree' (the tree is karpūra-vṛkṣa); Nourai's 'camphor tree' over-specifies. Second, and more important, Sanskrit is not the origin. The camphor of commerce is Dryobalanops aromatica of Sumatra and Borneo, not an Indian tree, and the word travelled with the goods: Malay kapur 'lime, chalk', in the trade name kapur Barus 'chalk of Barus' (Barus on the west coast of Sumatra was the camphor port), whence Sanskrit karpūra- with an inserted -r-. Skeat says so already in 1911 ('Camphor. (F. — Arab. — Malay.) … Arab. kāfūr, camphor; cf. Skt. karpūra … Malay kāpūr, lit. chalk; kāpūr bārūs, chalk of Barus, a name for camphor. Barus is in Sumatra'), and Etymonline, the AHD and Wiktionary all agree today (Wiktionary: karpūra- 'probably of Austroasiatic origin' or 'a borrowing from Proto-Malayic *kapur'). Jeffery, FVQ 246, proposes instead a Munda > Dravidian > Sanskrit route (Tamil karpūram, Malayalam), which is the same idea with a different donor family. So the chart's own NOTE at node 6 ('AHD traces this to the Malay word kâpŭr: chalk') is not a rival opinion to be weighed — it is the currently accepted account, and Nourai's Sanskrit box is one stage downstream of the real origin. The second headword 'Karpŭrah' is only a vowel-length variant of the same word and is handled as a redirect entry on this page.\",\n  \"note_fa\": \"واژهٔ سنسکریت درست است و به‌راستی حلقهٔ گرهیِ همهٔ زنجیرهٔ باختری است، اما دو نکته نمی‌گذارد این جعبه «تأییدشده» شمرده شود. نخست معنا: karpūra- یعنی «کافور» (همان صمغ یا بلور)، نه «درخت کافور» (که در سنسکریت karpūra-vṛkṣa است)؛ پس معنایی که نورایی داده تنگ‌تر و نادقیق است. دوم و مهم‌تر آنکه سنسکریت سرچشمهٔ واژه نیست. کافورِ بازرگانی از درخت Dryobalanops aromatica در سوماترا و بورنئو به دست می‌آمد، نه از درختی هندی، و واژه همراه کالا سفر کرد: مالایی kapur «آهک، گچ»، در نام بازرگانی kapur Barus «گچِ باروس» (باروس بندر کافور در ساحل باختری سوماترا بود)، که در سنسکریت با افزودن «ر» به karpūra- بدل شد. اسکیت همین را در ۱۹۱۱ نوشته است، و Etymonline و AHD و ویکی‌واژه نیز امروز بر همین‌اند (ویکی‌واژه: karpūra- «احتمالاً خاستگاه آسیایی-جنوب‌شرقی» یا وام از *kapur مالایی آغازین). جفری در «واژه‌های دخیل در قرآن» صفحهٔ ۲۴۶ راه دیگری پیشنهاد می‌کند: زبان‌های موندا ← دراویدی (تامیلی karpūram) ← سنسکریت، که همان اندیشه با خانوادهٔ زبانی دیگری است. پس یادداشت خودِ نمودار در گرهٔ ۶ («AHD آن را از مالایی kâpŭr «گچ» می‌گیرد») رأی رقیب نیست، بلکه دیدگاه پذیرفتهٔ امروزی است و جعبهٔ سنسکریتِ نورایی یک پله پایین‌تر از خاستگاه واقعی ایستاده است. سرواژهٔ دوم «Karpŭrah» تنها گونهٔ واکه‌ای همان واژه است و در این صفحه به‌صورت ارجاع آمده.\",\n  \"sources\": [\"https://en.wiktionary.org/wiki/%E0%A4%95%E0%A4%B0%E0%A5%8D%E0%A4%AA%E0%A5%82%E0%A4%B0\", \"https://www.etymonline.com/word/camphor\", \"https://en.wiktionary.org/wiki/camphor\"],\n  \"ref_check\": [\n    {\"ref\": \"KLN:229\", \"status\": \"partial\",\n     \"note\": \"Klein 1966 s.v. camphor (KLN_1966.txt line 6303, on the leaf whose page markers are 228 at line 6276 and 230 at line 6325, i.e. printed p.229): 'camphor, n. — F. camphre, fr. ML. camphora, fr. Arab. kāfūr, fr. OI. kapphraḥ, assimilated fr. earlier karpūraḥ.' Klein confirms the Sanskrit word and the Arabic > Medieval Latin > French > English chain, but he routes Arabic straight from the Indo-Aryan (Prakrit) form with no Iranian stage, and he says nothing of the Malay origin — so 'partial' with respect to Nourai's tree, which inserts Pahlavi and Persian.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"SKT\", \"where\": \"Skeat s.v. Camphor (SKT.txt lines 2709-2711)\", \"stance\": \"partial\",\n     \"note\": \"'Camphor. (F. — Arab. — Malay.) Formerly spelt camphire … F. camphre … Low L. camphora … Arab. kāfūr, camphor; cf. Skt. karpūra, camphor. — Malay kāpūr, lit. chalk; kāpūr bārūs, chalk of Barus, a name for camphor. Barus is in Sumatra.' Skeat has the same chain but makes Malay, not Sanskrit, the source.\"},\n    {\"src\": \"SIN\", \"where\": \"Laufer, Sino-Iranica p.483 no. 46 (SIN.txt line 4068) and pp.478-479 (line 2918)\", \"stance\": \"partial\",\n     \"note\": \"'46(483). kāfūr (Arabic and Persian), camphor (Laurus camphora). The same word appears already in Middle Persian. Skr. karpūra.' And p.479: 'Camphor is not produced in Persia' — the substance is Malayan (Dryobalanops), which is why the word, not the tree, is what travelled. Laufer also notes (p.480 ff.) Hindustani kapūr, Singhalese kapuru, Javanese and Malay kāpur, i.e. the r-less forms that underlie the Iranian shape.\"},\n    {\"src\": \"LKT\", \"where\": \"no. 1100 (LKT.txt line 2601)\", \"stance\": \"partial\",\n     \"note\": \"'1100. Sskr. karpūra: Ein Baum, Cinnamomum Camphora, aus Formosa stammend; schon prākrit mit Assimilation kappūra; hieraus ar. kāfūr, Grundwort für die europäischen Entsprechungen: mlat. camphora, rum. camfora, it. (alt) cafura, (neu) canfora, frz. camphre, sp. pg. cánfora, alcanfor; ndl. kamfer, mhd. gaffer …, nhd. Kampfer, engl. camphor.' Lokotsch starts, like Nourai, from Sanskrit and, like Klein, has no Iranian stage; his Prakrit kappūra is the form that explains the Iranian kāpūr.\"},\n    {\"src\": \"FVQ\", \"where\": \"Jeffery pp.246-247, s.v. kāfūr (FVQ.txt lines 15353-15400)\", \"stance\": \"partial\",\n     \"note\": \"'The ultimate source is probably to be found in the Munda dialects of India, whence it passed into Dravidian, e.g. Tamil karpūram, Malayalam …, and into Skt., cf. karpūra. It passed also into Iranian, where we find Phlv. kāpur, which gives the Mod. Pers. kāfūr, and Arm. kapur, and into Aram. where we find Syr. …' Jeffery too denies that Sanskrit is the origin.\"},\n    {\"src\": \"POK\", \"where\": \"POK_full.txt\", \"stance\": \"silent\",\n     \"note\": \"grep for karpura / camphor returns nothing — no Indo-European root is involved; this is a trade word.\"}\n  ],\n  \"nodes\": []\n }\n\n e3[\"nodes\"].append({\n  \"id\": 1, \"lang\": \"Pahlavi\", \"words\": \"kâpŭr\", \"verdict\": \"confirmed\",\n  \"derivation\": \"Middle Persian kāpūr 'camphor' is directly attested and is exactly the form the chart gives. MacKenzie, A Concise Pahlavi Dictionary, prints 'kāpūr [kʾpwl | Ar. kāfūr] camphor' — the Book Pahlavi spelling kʾpwl with the regular l for r, and MacKenzie's own cross-reference to Arabic kāfūr. The shape shows that Iranian took the word not from the Sanskrit karpūra- but from the Prakrit/Middle Indic development kappūra- (Lokotsch: 'schon prākrit mit Assimilation kappūra'), which loses the first -r- and gives kāpūra- > MP kāpūr; that same r-less type survives all across the trade area (Hindustani kapūr, Singhalese kapuru, Javanese/Malay kapur — Laufer, Sino-Iranica 483). Armenian borrowed the Iranian form: Hübschmann, Persische Studien p.188, 'Kapur „Kampfer“ (Moses, Geogr.) = np. kāfūr', listing it among the late Sasanian-period loans. Mo'in, in his etymological footnote to Borhan-e Qate' p.1571 s.v. کافور, likewise gives Sanskrit karpūra and 'در پهلوی kāpūr'.\",\n  \"derivation_fa\": \"فارسی میانه (پهلوی) kāpūr «کافور» صورتی گواهی‌شده است و درست همان است که در نمودار آمده. مکنزی در «فرهنگ کوچک پهلوی» می‌نویسد: «kāpūr [kʾpwl | عربی kāfūr] کافور» — با املای پهلوی کتابی kʾpwl که در آن «ل» جانشین قاعده‌مندِ «ر» است، و با ارجاع خودِ مکنزی به «کافور» عربی. صورت واژه نشان می‌دهد که ایرانی آن را نه از karpūra- سنسکریت، بلکه از گونهٔ پراکریت و هندی میانه kappūra- گرفته است (لوکوچ: «در پراکریت با همگونی kappūra»)، که «ر» نخست را از دست داده و به kāpūra- > kāpūr پهلوی رسیده؛ همین گونهٔ بی‌«ر» در سراسر حوزهٔ بازرگانی هست: هندی kapūr، سنهالی kapuru، جاوه‌ای و مالایی kapur (لوفر، «چین و ایران»، ص ۴۸۳). ارمنی نیز همین صورت ایرانی را وام گرفته است: هوبشمان، «پژوهش‌های فارسی»، ص ۱۸۸: «Kapur «کافور» (موسی خورنی) = فارسی نو kāfūr». معین نیز در حاشیهٔ ریشه‌شناختی خود بر برهان قاطع، ص ۱۵۷۱، ذیل «کافور» سنسکریت karpūra و «در پهلوی kāpūr» را می‌آورد. ادعای نورایی درست است.\",\n  \"sources\": [\"https://en.wiktionary.org/wiki/%D9%83%D8%A7%D9%81%D9%88%D8%B1\"],\n  \"ref_check\": [\n    {\"ref\": \"BQT:1571\", \"status\": \"supports\",\n     \"note\": \"Fetched with tools/ref_page.py BQT:1571 (BQT_v3_picofile.pdf pdf-page 364; the running number ‑۱۵۷۱‑ is printed at the head of the page). The page carries the entry «کافور، بر وزن ناسور، معروف» with Mo'in's numbered footnote 4: «نام فارسی ـ عربی مأخوذ از سانسکریت karpūra ـ karpūram … اطلاقی دیگر آن قافور، قفورا … در پهلوی kāpūr … لوفر اصل سانسکریت کلمه را karpūra نوشته [Laufer, Sino-Iranica]» — Sanskrit source and Pahlavi kāpūr, exactly Nourai's arrow, on exactly the cited page.\"},\n    {\"ref\": \"VDQ:356\", \"status\": \"partial\",\n     \"note\": \"VDQ is Badre'i's Persian translation of Jeffery with added notes; the noorlib scan is a JavaScript viewer and page 356 could not be opened offline. The underlying original was checked instead: Jeffery, The Foreign Vocabulary of the Qur'an pp.246-247 (FVQ.txt lines 15353-15400): 'It passed also into Iranian, where we find Phlv. kāpur, which gives the Mod. Pers. kāfūr, and Arm. kapur' (with n.5 'Justi, Glossary to Bundahesh, 201'). That is the Pahlavi form Nourai charts; Jeffery, however, derives the Sanskrit itself from Munda/Dravidian, not the reverse.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. kāpūr (PHD.txt line 424; PHD_mackenzie.txt line 3196)\", \"stance\": \"supports\",\n     \"note\": \"'kāpūr [kʾpwl | Ar. kāfūr] camphor'; the English-Pahlavi index (PHD_mackenzie.txt line 6141) has 'camphor kāpūr'.\"},\n    {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (Glossary)\", \"stance\": \"silent\",\n     \"note\": \"grep of NYB_vol2_glossary.txt for kapur / kāpūr returns no hit — the word does not occur in Nyberg's selected texts.\"},\n    {\"src\": \"HUB\", \"where\": \"Persische Studien p.188 (HUB.txt lines 6637-6638)\", \"stance\": \"supports\",\n     \"note\": \"'Kapur „Kampfer“ (Moses, Geogr.) = np. kāfūr' — Armenian kapur borrowed from the Iranian form, listed by Hübschmann among the late loans, which independently attests an Iranian kāpūr.\"},\n    {\"src\": \"SIN\", \"where\": \"Laufer, Sino-Iranica p.483 no.46 (SIN.txt line 4068)\", \"stance\": \"supports\",\n     \"note\": \"'kāfūr (Arabic and Persian), camphor … The same word appears already in Middle Persian. Skr. karpūra.'\"},\n    {\"src\": \"PLA\", \"where\": \"Asbaghi p.~216 s.v. ǧāfūr / p.~225 s.v. kāfūr (PLA_pages.txt lines 12075-12076, 12596)\", \"stance\": \"supports\",\n     \"note\": \"'ǧāfūr: „Kampfer“ pers., MP. kāpur, aram. …, mand. qapur, ar. Lw. kāfūr, engl. camphor, dtsch. Kampfer' — Asbaghi explicitly derives the Arabic from Middle Persian kāpur.\"}\n  ]\n })\n\n e3[\"nodes\"].append({\n  \"id\": 2, \"lang\": \"Persian\", \"words\": \"kâfŭr «کافور»\", \"verdict\": \"plausible\",\n  \"derivation\": \"New Persian کافور kāfūr 'camphor' — the word of Manuchehri's line quoted in the chart. That it continues Middle Persian kāpūr is not in doubt; what is doubtful is the arrow as drawn, i.e. that MP kāpūr yielded NP kāfūr directly. Intervocalic p in Middle Persian does not become f in New Persian: it becomes b or v (āp > āb, ǰuftak > ǰuft is inherited f from earlier -ft-, but *kāpūr would regularly give *kābūr). The f of کافور is the mark of Arabic transmission: Arabic, lacking p, renders Iranian p by f (Pahlavi pīl > فیل fīl, pusht-i pā > …), so MP kāpūr > Arabic kāfūr, and the Arabic form then displaced the inherited one in New Persian — which is why Wiktionary lists Persian کافور as a descendant of the Arabic word, and why Mo'in's own dictionary tags the entry «کافور: (ع.)» 'Arabic'. Mo'in's footnote in Borhan p.1571 splits the difference with the formula «نام فارسی ـ عربی» 'a Persian-Arabic name'. So the substance of Nourai's node is right (Persian kāfūr goes back through kāpūr to the Indian word) but the order of his nodes 2 and 3 is inverted: the Arabic stage stands between the Pahlavi and the modern Persian form, not after it.\",\n  \"derivation_fa\": \"«کافور» فارسی نو، همان واژه‌ای که در بیت منوچهری در نمودار آمده است. در اینکه دنبالهٔ kāpūr فارسی میانه است تردیدی نیست؛ آنچه جای چون‌وچرا دارد خودِ پیکان است، یعنی این ادعا که kāpūr پهلوی یکراست «کافور» فارسی را داده باشد. «پ» میان دو واکه در گذر از فارسی میانه به فارسی نو «ف» نمی‌شود، بلکه «ب» یا «و» می‌شود (āp > آب)؛ پس از kāpūr انتظار *کابور می‌رفت. «ف» در «کافور» نشانهٔ گذر از عربی است: عربی که «پ» ندارد، «پ» ایرانی را «ف» می‌کند (پهلوی pīl > فیل)، پس kāpūr پهلوی در عربی kāfūr شده و سپس همان صورت عربی جای صورت موروثی را در فارسی نو گرفته است — و به همین سبب ویکی‌واژه «کافور» فارسی را بازماندهٔ واژهٔ عربی می‌شمارد و خودِ معین در فرهنگش مدخل را «کافور: (ع.)» برچسب زده است. معین در حاشیهٔ برهان (ص ۱۵۷۱) با تعبیر «نام فارسی ـ عربی» میانه را می‌گیرد. پس محتوای ادعای نورایی درست است (کافور فارسی از راه kāpūr به واژهٔ هندی می‌رسد) ولی ترتیب گره‌های ۲ و ۳ او وارونه است: حلقهٔ عربی میان پهلوی و فارسی نو می‌نشیند، نه پس از آن. با احتیاط پذیرفتنی است.\",\n  \"sources\": [\"https://en.wiktionary.org/wiki/%D9%83%D8%A7%D9%81%D9%88%D8%B1\", \"https://en.wiktionary.org/wiki/camphor\"],\n  \"ref_check\": [\n    {\"ref\": \"BQT:1571\", \"status\": \"supports\",\n     \"note\": \"ref_page.py BQT:1571 (BQT_v3 pdf-page 364): the headword «کافور، بر وزن ناسور، معروف» with the definition «رستنیی است و آن دو قسم می‌باشد: یکی از درخت حاصل می‌شود …», and Mo'in's footnote 4 «نام فارسی ـ عربی مأخوذ از سانسکریت karpūra … در پهلوی kāpūr». Both the Persian headword and the Pahlavi antecedent are on the cited page; Mo'in's label 'Persian-Arabic', however, already signals the Arabic mediation Nourai's arrow order hides.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"MON\", \"where\": \"s.v. کافور (MON_part2.txt line 18828)\", \"stance\": \"partial\",\n     \"note\": \"«کافور: (ع.) (گیا.) (پز.) مادهٔ معطر جامدی که از برگ گیاهان … سیناموموم کامفورا و دریوبالانوپس کامفورا … در ژاپن و چین و جزایر سوماترا و برنئو و هندوچین می‌رویند، استخراج می‌شود.» Mo'in's abridged dictionary tags the word '(ع.)' = Arabic, i.e. borrowed from Arabic into Persian, and names the Sumatran/Bornean Dryobalanops as one of the two source trees.\"},\n    {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. kāpūr\", \"stance\": \"supports\",\n     \"note\": \"'kāpūr [kʾpwl | Ar. kāfūr] camphor' — MacKenzie's own bracket pairs the Pahlavi word with the *Arabic* form, not with a New Persian kāfūr, which is consistent with the Arabic having carried the f.\"},\n    {\"src\": \"HRN\", \"where\": \"Horn, Grundriss der neupersischen Etymologie\", \"stance\": \"silent\",\n     \"note\": \"grep of HRN.txt for kafur / kapur returns nothing — Horn omits it, as he omits Arabic-mediated vocabulary.\"},\n    {\"src\": \"HUB\", \"where\": \"Persische Studien p.188\", \"stance\": \"supports\",\n     \"note\": \"'Kapur „Kampfer“ (Moses, Geogr.) = np. kāfūr' — Hübschmann equates the Armenian (Iranian-derived) kapur with New Persian kāfūr.\"},\n    {\"src\": \"FVQ\", \"where\": \"Jeffery p.246\", \"stance\": \"supports\",\n     \"note\": \"'we find Phlv. kāpur, which gives the Mod. Pers. kāfūr' — Jeffery, like Nourai, derives the New Persian form straight from the Pahlavi one.\"}\n  ]\n })\n\n e3[\"nodes\"].append({\n  \"id\": 3, \"lang\": \"Arabic\", \"words\": \"kâfŭr\", \"verdict\": \"plausible\",\n  \"derivation\": \"Arabic كافور kāfūr 'camphor' — a Qur'anic word (Sura 76:5, of the drink of the blessed in Paradise) and therefore attested by the early 7th century, also in the pre-Islamic poets al-Aʿshā and ʿAlqama. That it is a loan from Iranian is the majority view and is what Nourai draws: Asbaghi, Persische Lehnwörter im Arabischen, s.v. ǧāfūr/kāfūr, 'pers., MP. kāpur … ar. Lw. kāfūr', and Wiktionary, 'Possibly borrowed from Middle Persian kāpūr, borrowed from an Austronesian language, from Proto-Austronesian *qapuʀ'. Phonetically the borrowing is textbook: Iranian p, absent from Arabic, is rendered f (as in fīl < pīl), long ā is kept, and the word is fitted to the fāʿūl pattern. Two reservations make this 'plausible' rather than 'confirmed'. (i) The donor stage is Middle Persian kāpūr, not a New Persian kāfūr as the chart's arrow implies — the f is created by the Arabic borrowing itself. (ii) Jeffery, FVQ 246-247, having noted that Addai Shir 136 'would make the Arabic also a borrowing from the Persians', concludes: 'The probabilities are, however, that it, like the Eth. …, is to be taken as derived from the Syriac', i.e. Syriac kāpūrā as the immediate donor, itself from Iranian; and Klein p.229 and Lokotsch no.1100 route the Arabic straight from Prakrit kappūra with no Iranian stage at all. The chart's NOTE, 'TAD:60 derives this from Greek kafoura', is the weakest of all these: al-Unaysi's Greek καφουρά is itself a late borrowing out of Iranian/Arabic (Jeffery, p.246: 'It is very probable that the Syriac like the Gk. καφουρά is from the Iranian'), so the direction is reversed and no modern authority follows him.\",\n  \"derivation_fa\": \"«کافور» عربی، واژه‌ای قرآنی (سورهٔ انسان، آیهٔ ۵، دربارهٔ نوشیدنی بهشتیان) و ازاین‌رو دست‌کم از آغاز سدهٔ یکم هجری گواهی‌شده، و پیش از آن در شعر اعشی و علقمه. اینکه وام‌واژه‌ای ایرانی است رأی اکثر است و همان است که نورایی کشیده: اصباغی در «وام‌واژه‌های فارسی در عربی» می‌نویسد «از فارسی، فارسی میانه kāpur … وام عربی kāfūr»، و ویکی‌واژه: «احتمالاً از فارسی میانه kāpūr، خود وام از زبانی آسترونزیایی». از نظر آوایی وام‌گیری نمونه‌وار است: «پ» ایرانی که در عربی نیست «ف» شده (مانند pīl > فیل)، «ا»ی کشیده مانده و واژه بر وزن فاعول ریخته شده است. دو نکته این گره را «با احتیاط پذیرفتنی» می‌کند: نخست آنکه مرحلهٔ وام‌دهنده فارسی میانهٔ kāpūr است نه «کافورِ» فارسی نو — «ف» را خودِ وام‌گیری عربی پدید آورده است. دوم آنکه جفری (ص ۲۴۶ ـ ۲۴۷) پس از یادکرد رأی ادی‌شیر (که عربی را وام از فارسی می‌داند) نتیجه می‌گیرد که به احتمال بیشتر عربی آن را از سریانی گرفته است؛ و کلاین (ص ۲۲۹) و لوکوچ (شمارهٔ ۱۱۰۰) یکسره عربی را از پراکریت kappūra می‌گیرند و هیچ حلقهٔ ایرانی نمی‌گذارند. یادداشت نمودار («TAD:60 آن را از یونانی kafoura می‌گیرد») از همه سست‌تر است: καφουρά یونانی خود وامی است متأخر از ایرانی یا عربی (جفری، ص ۲۴۶)، پس جهت وام‌گیری وارونه است و هیچ پژوهندهٔ امروزی از آن پیروی نمی‌کند.\",\n  \"sources\": [\"https://en.wiktionary.org/wiki/%D9%83%D8%A7%D9%81%D9%88%D8%B1\", \"https://en.wiktionary.org/wiki/camphor\"],\n  \"ref_check\": [\n    {\"ref\": \"PLA:225\", \"status\": \"supports\",\n     \"note\": \"Asbaghi, Persische Lehnwörter im Arabischen. The kāfūr headword stands on the leaf between the running numbers 225 (PLA_pages.txt line 12484) and 227 (line 12708): 'kāfūr: „Kampfer“ pers. = ǧāfūr q.v.', and the main entry ǧāfūr (line 12075) reads 'ǧāfūr: „Kampfer“ pers., MP. kāpur, aram. …, mand. qapur, ar. Lw. kāfūr, engl. camphor, dtsch. Kampfer' with the source note 'Mackenzie s.v.'. Asbaghi's whole book is a list of Persian loans in Arabic, so the entry is itself the claim Nourai makes.\"},\n    {\"ref\": \"DOZ:47\", \"status\": \"partial\",\n     \"note\": \"Dozy, Oosterlingen, s.v. KAMFER, on p.46/47 (DOZ.txt lines 1447-1452; the page-break marker '47' falls inside the entry): 'Het Arab. kāfoer (كافور), dat het Prākr. kappoerā of kāpoerā (Skr. karpoera) is. De n of m, die in een der Ital. vormen (cafura) en in 't middel-Hoogd. (gaffer) niet is, is ingeschoven. Sp. alcanfor en canfora, It. ook canfora, Fr. camphre, en dit is onze vorm.' The Arabic word is there on the cited page, but Dozy derives it from Prakrit directly, with no Persian intermediary — hence 'partial'.\"},\n    {\"ref\": \"VDQ:356\", \"status\": \"partial\",\n     \"note\": \"The noorlib scan of Badre'i's Persian Jeffery could not be opened (JavaScript viewer). The original, Jeffery FVQ pp.246-247 (FVQ.txt lines 15353-15411), was read instead: 'It is usually taken as an Arabic word (LA, vi, 465), but the variety of spellings … would suggest otherwise, and several of the early authorities noted it as a loan-word from Persian. … It passed also into Iranian, where we find Phlv. kāpur … Addai Sher, 136, would make the Arabic also a borrowing from the Persians. The probabilities are, however, that it, like the Eth., is to be taken as derived from the Syriac.' Supports an Iranian ultimate source but prefers Syriac as the immediate donor.\"},\n    {\"ref\": \"TAD:60\", \"status\": \"partial\",\n     \"note\": \"Cited only inside the node's NOTE. The claim is genuinely al-Unaysi's: TAD.txt line 2480 reads «كافور ـ في اليونانية kaphoura وهو صمغ شجرة تنبت في الهند والصين واليابان أبيض لماع شفاف قابل الاحتراق» — 'kāfūr: in Greek kaphoura; the gum of a tree that grows in India, China and Japan …'. The OCR of TAD carries no page markers, so the printed page 60 itself could not be confirmed; the entry sits in the alphabetical kāf section right after قيثار/قومندان, which is consistent. The derivation is wrong in direction (see the node's derivation).\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"s.v. camphor (KLN_1966.txt line 6303, printed p.229)\", \"stance\": \"contradicts\",\n     \"note\": \"'camphor, n. — F. camphre, fr. ML. camphora, fr. Arab. kāfūr, fr. OI. kapphraḥ, assimilated fr. earlier karpūraḥ.' Klein takes the Arabic straight from Indo-Aryan, with no Iranian link.\"},\n    {\"src\": \"LKT\", \"where\": \"no. 1100 (LKT.txt line 2601)\", \"stance\": \"contradicts\",\n     \"note\": \"'Sskr. karpūra … schon prākrit mit Assimilation kappūra; hieraus ar. kāfūr' — again Prakrit > Arabic directly.\"},\n    {\"src\": \"AFM\", \"where\": \"Addi Shir, Kitab al-alfaz al-farisiyya al-mu'arraba p.136 (AFM_pages.txt lines 3475-3482)\", \"stance\": \"supports\",\n     \"note\": \"«الكافور: طيب يكون من شجر بجبال بحر الهند والصين …» with the foreign equivalents 'camphora' Latin, «بالرومية» and «كافوری بالترکية». Addi Shir includes kāfūr in his list of *Persian* words arabicised — precisely Nourai's arrow — and Jeffery cites him for it ('Addai Sher, 136, would make the Arabic also a borrowing from the Persians').\"},\n    {\"src\": \"FVQ\", \"where\": \"Jeffery pp.246-247\", \"stance\": \"partial\",\n     \"note\": \"See ref_check VDQ:356 — Iranian ultimate source accepted, Syriac preferred as the immediate donor of the Arabic.\"},\n    {\"src\": \"PLA\", \"where\": \"Asbaghi, s.v. ǧāfūr / kāfūr\", \"stance\": \"supports\",\n     \"note\": \"'pers., MP. kāpur … ar. Lw. kāfūr' — the Arabic is a Persian loan.\"}\n  ]\n })\n\n e3[\"nodes\"].append({\n  \"id\": 4, \"lang\": \"Middle Latin\", \"words\": \"camphora\", \"verdict\": \"confirmed\",\n  \"derivation\": \"Medieval Latin camphora (also camfora, cafura) is the Arabic word taken into the Latin of the medical writers — the Salerno school and the Latin translations of Arabic pharmacology (Constantinus Africanus, Gerard of Cremona, 11th-12th c.), camphor being an Arab-traded drug. Two things happen to the form: the Arabic ū of kāfūr is Latinised as the -ora ending of a feminine noun in -a, and a nasal is inserted before the labial, giving -mph-/-nf-. Dozy states the epenthesis explicitly, s.v. KAMFER: 'De n of m, die in een der Ital. vormen (cafura) en in 't middel-Hoogd. (gaffer) niet is, is ingeschoven' — 'the n or m … is inserted', and the nasalless Italian cafura and Middle High German gaffer prove that it is secondary. From Medieval Latin come Italian canfora, Spanish and Portuguese cánfora / alcanfor (the latter with the Arabic article), Romanian camfora, Dutch kamfer and German Kampfer (Lokotsch no. 1100).\",\n  \"derivation_fa\": \"لاتین میانه camphora (و نیز camfora و cafura) همان واژهٔ عربی است که به لاتینِ پزشکان راه یافته — مکتب سالرنو و ترجمه‌های لاتینیِ داروشناسی عربی (قسطنطین آفریقایی، ژرار کرمونایی، سده‌های یازدهم و دوازدهم میلادی)، چراکه کافور دارویی بود که بازرگانان مسلمان می‌آوردند. دو دگرگونی رخ داده است: «ـو»ی کشیدهٔ kāfūr عربی به پایانهٔ ـora اسم مؤنث لاتینی بدل شده، و پیش از واج لبی یک خیشومی افزوده شده و ـmph-/-nf- پدید آمده است. دُزی این افزایش خیشومی را صریح گفته است: «آن n یا m که در یکی از صورت‌های ایتالیایی (cafura) و در آلمانی عالی میانه (gaffer) نیست، افزوده شده است» — و همین دو صورتِ بی‌خیشوم ثابت می‌کند که خیشومی ثانوی است. از لاتین میانه ایتالیایی canfora، اسپانیایی و پرتغالی cánfora و alcanfor (این یکی با «الـ» عربی)، رومانیایی camfora، هلندی kamfer و آلمانی Kampfer برآمده‌اند (لوکوچ، شمارهٔ ۱۱۰۰). ادعای نورایی درست است.\",\n  \"sources\": [\"https://www.etymonline.com/word/camphor\", \"https://en.wiktionary.org/wiki/camphor\"],\n  \"ref_check\": [\n    {\"ref\": \"KLN:229\", \"status\": \"supports\",\n     \"note\": \"KLN_1966.txt line 6303 (printed p.229): 'camphor, n. — F. camphre, fr. ML. camphora, fr. Arab. kāfūr …' — Medieval Latin camphora from Arabic kāfūr, exactly as charted, on exactly the cited page.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"LKT\", \"where\": \"no. 1100 (LKT.txt line 2601)\", \"stance\": \"supports\",\n     \"note\": \"'hieraus ar. kāfūr, Grundwort für die europäischen Entsprechungen: mlat. camphora, rum. camfora, it. (alt) cafura, (neu) canfora, frz. camphre, sp. pg. cánfora, alcanfor; ndl. kamfer, mhd. gaffer [ohne eingeschobenes m oder n!], nhd. Kampfer, engl. camphor.'\"},\n    {\"src\": \"DOZ\", \"where\": \"Oosterlingen s.v. KAMFER, pp.46-47\", \"stance\": \"supports\",\n     \"note\": \"'De n of m, die in een der Ital. vormen (cafura) en in 't middel-Hoogd. (gaffer) niet is, is ingeschoven. Sp. alcanfor en canfora, It. ook canfora, Fr. camphre.'\"},\n    {\"src\": \"SKT\", \"where\": \"Skeat s.v. Camphor (SKT.txt line 2710)\", \"stance\": \"supports\",\n     \"note\": \"'F. camphre, „camphire“; Cot. — Low L. camphora (whence the form camphor). — Arab. kāfūr.'\"}\n  ]\n })\n\n e3[\"nodes\"].append({\n  \"id\": 5, \"lang\": \"French\", \"words\": \"\", \"verdict\": \"confirmed\",\n  \"derivation\": \"Pass-through node with no word printed and no reference given: Old French camphre / caufre / camphore, the form through which Medieval Latin camphora reached English. The Latin -ora is syncopated to -re in the ordinary French way (cf. ML camera > OF chambre), giving camphre, still the modern French form. Klein names the stage on the page cited for the neighbouring nodes ('camphor, n. — F. camphre, fr. ML. camphora'), and Skeat has 'F. camphre, „camphire“; Cot.' — i.e. attested in Cotgrave's French-English dictionary of 1611. Etymonline gives the English word as coming 'through Old French camphre', with the earliest English spelling caumfre, which is the Old French form itself.\",\n  \"derivation_fa\": \"این گره حلقه‌ای واسطه است، بی‌واژه و بی‌ارجاع: فرانسوی کهن camphre / caufre / camphore، همان صورتی که camphora لاتین میانه از راه آن به انگلیسی رسیده است. پایانهٔ ـora لاتینی، به شیوهٔ معمول فرانسوی، به ـre کوتاه شده (مانند camera > chambre) و camphre را داده که تا امروز صورت فرانسوی است. کلاین در همان صفحه‌ای که برای گره‌های همسایه یاد شده این مرحله را نام می‌برد («camphor — از فرانسوی camphre، از لاتین میانه camphora»)، و اسکیت می‌نویسد «F. camphre، «camphire»؛ کاتگریو» یعنی گواهی‌شده در فرهنگ فرانسوی-انگلیسی کاتگریو (۱۶۱۱). Etymonline نیز کهن‌ترین املای انگلیسی را caumfre می‌داند که خود همان صورت فرانسوی کهن است. ادعای نورایی درست است.\",\n  \"sources\": [\"https://www.etymonline.com/word/camphor\"],\n  \"ref_check\": [\n    {\"ref\": \"None\", \"status\": \"not_checked\",\n     \"note\": \"Nourai gives no reference for this node (refs=None in the JSON and no citation on the printed chart). The stage is nevertheless documented by the references on the adjacent nodes: KLN:229 'F. camphre, fr. ML. camphora' and Skeat s.v. Camphor.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"s.v. camphor (KLN_1966.txt line 6303, p.229)\", \"stance\": \"supports\",\n     \"note\": \"'camphor, n. — F. camphre, fr. ML. camphora, fr. Arab. kāfūr' — French is the immediate source of the English word.\"},\n    {\"src\": \"SKT\", \"where\": \"Skeat s.v. Camphor (SKT.txt lines 2709-2710)\", \"stance\": \"supports\",\n     \"note\": \"'Camphor. (F. — Arab. — Malay.) Formerly spelt camphire (with an inserted i). — F. camphre, „camphire“; Cot.'\"},\n    {\"src\": \"LKT\", \"where\": \"no. 1100\", \"stance\": \"supports\",\n     \"note\": \"'frz. camphre' listed among the European reflexes of Arabic kāfūr.\"}\n  ]\n })\n\n e3[\"nodes\"].append({\n  \"id\": 6, \"lang\": \"English\", \"words\": \"camphor\", \"verdict\": \"confirmed\",\n  \"derivation\": \"English camphor is attested from the early 14th century as caumfre, borrowed from Old French camphre; the later spelling camphor is a re-latinisation after Medieval Latin camphora, and the by-form camphire (Authorized Version, Song of Songs 1:14, where it in fact renders henna) survived into the 17th century. Klein p.229, the page cited: 'camphor, n. — F. camphre, fr. ML. camphora, fr. Arab. kāfūr, fr. OI. kapphraḥ, assimilated fr. earlier karpūraḥ', with the derivatives camphorate, camphoric, and the related camphene, camphine coined from the abbreviation. The chart's NOTE, 'AHD traces this to the Malay word kâpŭr: chalk', must be endorsed rather than merely noted: this is the modern consensus. Etymonline: 'from Medieval Latin camfora, from Arabic kafur, ultimately through Sanskrit karpuram, from Malay (Austronesian) kapur „camphor tree“'; Wiktionary: 'from Arabic كافور (kāfūr), in turn from an Austronesian word such as Malay kapur'; Skeat already in 1911: 'Malay kāpūr, lit. chalk; kāpūr bārūs, chalk of Barus'. The trade name preserves the geography — Barus, the camphor port on the west coast of Sumatra — and the Sanskrit karpūra- of Nourai's root box is one link in that chain rather than its head.\",\n  \"derivation_fa\": \"واژهٔ انگلیسی camphor از آغاز سدهٔ چهاردهم میلادی به صورت caumfre گواهی شده و وام از فرانسوی کهن camphre است؛ املای امروزی camphor بازلاتینی‌سازی بر پایهٔ camphora لاتین میانه است، و گونهٔ camphire (در ترجمهٔ رسمی انگلیسی کتاب مقدس، غزل غزل‌ها ۱:۱۴ که در آنجا در واقع «حنا» است) تا سدهٔ هفدهم زنده بود. کلاین در همان صفحهٔ ۲۲۹ می‌نویسد: «camphor — از فرانسوی camphre، از لاتین میانه camphora، از عربی kāfūr، از هندی باستان kapphraḥ که با همگونی از karpūraḥ کهن‌تر آمده». یادداشت نمودار («AHD این را به مالایی kâpŭr «گچ» می‌رساند») را باید نه‌فقط ثبت که تأیید کرد: این همان دیدگاه پذیرفتهٔ امروزی است. Etymonline: «از لاتین میانه camfora، از عربی kafur، در نهایت از راه سنسکریت karpuram، از مالایی kapur «درخت کافور»»؛ ویکی‌واژه نیز همین را می‌گوید و اسکیت در ۱۹۱۱ نوشته بود «مالایی kāpūr، در اصل «گچ»؛ kāpūr bārūs یعنی «گچِ باروس»». نامِ بازرگانی جغرافیا را نگه داشته است — باروس، بندر کافور در ساحل باختری سوماترا — و karpūra- سنسکریت در جعبهٔ ریشهٔ نورایی حلقه‌ای از این زنجیره است نه سرِ آن. ادعای نورایی دربارهٔ این گره درست است.\",\n  \"sources\": [\"https://www.etymonline.com/word/camphor\", \"https://en.wiktionary.org/wiki/camphor\", \"https://en.wiktionary.org/wiki/%E0%A4%95%E0%A4%B0%E0%A5%8D%E0%A4%AA%E0%A5%82%E0%A4%B0\"],\n  \"ref_check\": [\n    {\"ref\": \"KLN:229\", \"status\": \"supports\",\n     \"note\": \"KLN_1966.txt lines 6302-6304 (printed p.229): 'camphire, n., 1) camphor (obsol. or dial.); 2) henna (see Authorized Version, Song of Songs 1:14). — A var. of camphor.' / 'camphor, n. — F. camphre, fr. ML. camphora, fr. Arab. kāfūr, fr. OI. kapphraḥ, assimilated fr. earlier karpūraḥ.' / 'Derivatives: camphor, tr. v., camphor-aceous, adj., camphor-ate …'. Headword, chain and page all as cited.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"SKT\", \"where\": \"Skeat s.v. Camphor (SKT.txt lines 2709-2711)\", \"stance\": \"supports\",\n     \"note\": \"'Camphor. (F. — Arab. — Malay.) … Arab. kāfūr, camphor; cf. Skt. karpūra, camphor. — Malay kāpūr, lit. chalk; kāpūr bārūs, chalk of Barus, a name for camphor. Barus is in Sumatra.' Independent support for the chart's own AHD/Malay note.\"},\n    {\"src\": \"LKT\", \"where\": \"no. 1100\", \"stance\": \"supports\",\n     \"note\": \"'engl. camphor' listed among the European reflexes; Lokotsch also notes 'ngr. καφουρά'.\"},\n    {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century vol. 1\", \"stance\": \"silent\",\n     \"note\": \"grep of WEB_vol1.txt finds only compounds and the variant 'cam'phir' (line 5206); the main camphor entry is not legible in the OCR of this copy.\"},\n    {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls vol. I\", \"stance\": \"partial\",\n     \"note\": \"grep finds only derivative and compound entries (e.g. line 55998, the list of 'special camphors derived from natural products … Japan c. (same as camphor, 1)'), confirming the English word's currency; the head entry itself is not recoverable from the OCR.\"}\n  ]\n })\n\n data[\"entries\"].append(e3)\n"
}
```


### [2026-09-06T16:11:44.485Z] TOOL RESULT

```
File created successfully at: /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/part3.py (file state is current in your context — no need to Read it back)
```


## [2026-09-06T16:11:54.179Z] TOOL CALL #64: Write

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/drive.py",
 "content": "# -*- coding: utf-8 -*-\nimport json, sys, os, io, runpy\n\nHERE = os.path.dirname(os.path.abspath(__file__))\nsys.path.insert(0, HERE)\n\nns = runpy.run_path(os.path.join(HERE, \"build243.py\"))\ndata = ns[\"data\"]\n\nimport part2, part3\npart2.build(data)\npart3.build(data)\n\n# faithful root names from the source JSON\nsrc = json.load(open(\"/home/sfmqrb/git/rishe/data/extracted/batch/page-243.json\"))\nnames = {i: e[\"root\"][\"name\"] for i, e in enumerate(src[\"entries\"])}\nfor ve in data[\"entries\"]:\n    ve[\"root\"] = names[ve[\"entry\"]]\n\nout = \"/home/sfmqrb/git/rishe/data/verification/page-243.json\"\nwith io.open(out, \"w\", encoding=\"utf-8\") as f:\n    json.dump(data, f, ensure_ascii=False, indent=1)\n    f.write(\"\\n\")\nprint(\"wrote\", out)\n"
}
```


### [2026-09-06T16:11:54.209Z] TOOL RESULT

```
File created successfully at: /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/drive.py (file state is current in your context — no need to Read it back)
```


## [2026-09-06T16:11:57.163Z] TOOL CALL #65: Bash

```json
{
 "command": "python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/drive.py && python3 -m json.tool data/verification/page-243.json > /dev/null && echo JSON-OK && python3 tools/verify_check.py 243"
}
```


### [2026-09-06T16:12:00.276Z] TOOL RESULT

```
wrote /home/sfmqrb/git/rishe/data/verification/page-243.json
JSON-OK
nodes verified: 17/17
node verdicts: {'confirmed': 13, 'plausible': 4}
root verdicts: {'plausible': 3}
ref checks: {'supports': 18, 'not_found': 1, 'partial': 5, 'not_checked': 1}
books consulted: {'supports': 37, 'partial': 9, 'silent': 11, 'contradicts': 4} | by book: {'LKT': 8, 'KLN': 6, 'SKT': 5, 'HUB': 4, 'PLA': 4, 'MON': 3, 'WEB': 3, 'FSD': 3, 'PHD': 3, 'LAT': 3, 'HRN': 2, 'AFM': 2, 'SYN': 2, 'FVQ': 2, 'TTS': 1, 'MON/Dehkhoda (vajehyab)': 1, 'AFA': 1, 'Wiktionary (Persian)': 1, 'BQT': 1, 'HJB': 1, 'Wiktionary (Ancient Greek)': 1, 'LEW': 1, 'NYB': 1, 'SIN': 1, 'DOZ': 1}
```


## [2026-09-06T16:12:09.196Z] TOOL CALL #66: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/page-243.json'))\nprint(d['pdf_page'], d['book_page'], d['verified_by'], d['verified_on'])\nfor e in d['entries']:\n    print('---', e['entry'], e['root'], e['verdict'], 'nodes', len(e['nodes']))\n    assert e.get('note_fa')\n    for n in e['nodes']:\n        assert n.get('derivation_fa') and n.get('ref_check') is not None and n.get('consulted')\n        print('   #%s %s %s | %s' % (n['id'], n['lang'], n['verdict'], n['words'][:40]))\nprint('all fields present')\nprint([k for k in d['entries'][0]['nodes'][0].keys()])\n\"; ls -l data/verification/page-243.json; git -C /home/sfmqrb/git/rishe status --short"
}
```


### [2026-09-06T16:12:11.621Z] TOOL RESULT

```
243 213 claude-opus-5 2026-09-06
--- 0 Kar 2, Qar 2 plausible nodes 5
   #1 Persian confirmed | qareh «قره»
   #2 Turkish confirmed | kara-kŭlâk, qara-qulâq
   #3 Persian confirmed | qareh-qŭlâq «قره قولاق»
   #4 French confirmed | 
   #5 English confirmed | caracal
--- 2 Karpâsah plausible nodes 6
   #1 Persian confirmed | karpâs «کَرپاس»
   #2 Arabic confirmed | karbâs
   #3 Persian plausible | karbâs «کرباس»
   #4 Greek plausible | karpasos
   #5 Latin confirmed | 
   #6 English confirmed | carbasus
--- 3 Karpurah, Karpŭrah plausible nodes 6
   #1 Pahlavi confirmed | kâpŭr
   #2 Persian plausible | kâfŭr «کافور»
   #3 Arabic plausible | kâfŭr
   #4 Middle Latin confirmed | camphora
   #5 French confirmed | 
   #6 English confirmed | camphor
all fields present
['id', 'lang', 'words', 'verdict', 'derivation', 'derivation_fa', 'sources', 'ref_check', 'consulted']
-rw-rw-r-- 1 sfmqrb sfmqrb 96630 Sep  6 12:12 data/verification/page-243.json
 M data/verification/sources/web/index.jsonl
?? data/verification/page-243.json
?? data/verification/sources/web/015096e19c620557.txt
?? data/verification/sources/web/044437dd95a9dd37.txt
?? data/verification/sources/web/09c738b87de63f09.txt
?? data/verification/sources/web/0bb66061d76d51a8.txt
?? data/verification/sources/web/0e3b45e8a2070753.txt
?? data/verification/sources/web/13ca7d09292c7378.txt
?? data/verification/sources/web/157c56c3f0a4fc36.txt
?? data/verification/sources/web/15abe6f767be23b7.txt
?? data/verification/sources/web/1a868c8cb9b965ef.txt
?? data/verification/sources/web/35745a4f20f781b9.txt
?? data/verification/sources/web/3a02bd24b7c44c4f.txt
?? data/verification/sources/web/41fb24c8e6f1c5a3.txt
?? data/verification/sources/web/45ee1822d27b00c1.txt
?? data/verification/sources/web/4743c4573f4f3d10.txt
?? data/verification/sources/web/4daa56ebf780f714.txt
?? data/verification/sources/web/509e52454bc94b92.txt
?? data/verification/sources/web/5edfe64ce81ee291.txt
?? data/verification/sources/web/6b7216a01189ba06.txt
?? data/verification/sources/web/6d095a82f9d3e3c1.txt
?? data/verification/sources/web/724674b0abe31773.txt
?? data/verification/sources/web/74bb1ffff4e282de.txt
?? data/verification/sources/web/7c7bdb49995a819e.txt
?? data/verification/sources/web/8010838e4078cf92.txt
?? data/verification/sources/web/90abb36398180788.txt
?? data/verification/sources/web/9947c1305180ded4.txt
?? data/verification/sources/web/a2b353cd703f8bf3.txt
?? data/verification/sources/web/a51ef95da574605d.txt
?? data/verification/sources/web/a85f291e06611160.txt
?? data/verification/sources/web/b1108df87f62460f.txt
?? data/verification/sources/web/b3175cc86b6116d8.txt
?? data/verification/sources/web/b66b9b6c6f9db6c5.txt
?? data/verification/sources/web/b71c6b2a24d4efe3.txt
?? data/verification/sources/web/c2c684dc0a3faa39.txt
?? data/verification/sources/web/c4169f520f6677fb.txt
?? data/verification/sources/web/c82df06e922f0da9.txt
?? data/verification/sources/web/ec1e5ec3e0b4e3fb.txt
?? data/verification/sources/web/ef2f1a54e18e39c2.txt
?? data/verification/sources/web/f44926dc6ab11a68.txt
```


## [2026-09-06T16:12:24.504Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && ls -l 3dc32f3c2e575a84.txt 66537b92e1d9a419.txt bd2df782388fcebf.txt 2>&1 | head; echo \"---\"; tail -12 index.jsonl | python3 -c \"\nimport sys,json\nfor l in sys.stdin:\n    d=json.loads(l); print(d.get('url','')[:80], '|', d.get('file','')[:20])\n\""
}
```


### [2026-09-06T16:12:26.236Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 12929 Sep  6 11:56 3dc32f3c2e575a84.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   180 Sep  6 11:58 66537b92e1d9a419.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 14888 Sep  6 11:56 bd2df782388fcebf.txt
---
https://en.wiktionary.org/wiki/کلنگ | data/verification/so
https://en.wiktionary.org/wiki/κλών | data/verification/so
https://www.etymonline.com/word/clone | data/verification/so
https://en.wiktionary.org/wiki/Hamlet | data/verification/so
https://www.etymonline.com/word/gladiator | data/verification/so
https://www.etymonline.com/word/calamity | data/verification/so
https://www.etymonline.com/word/columbarium | data/verification/so
https://www.etymonline.com/word/Columbia | data/verification/so
https://en.wiktionary.org/wiki/कलश | data/verification/so
https://en.wiktionary.org/wiki/चरمे | data/verification/so
https://en.wiktionary.org/wiki/چرمه | data/verification/so
https://abadis.ir/fatofa/چرمه/ | data/verification/so
```


## [2026-09-06T16:12:36.186Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"--- 66537b92 (vajehyab dehkhoda) ---\" && cat 66537b92e1d9a419.txt && echo \"--- 92226094 (fa.wikipedia) head ---\" && head -c 900 922260947e7b9d3e.txt && echo && grep -c \"siyah\\|سیاه\" 922260947e7b9d3e.txt; grep -o \"قره[^ ]*\" 922260947e7b9d3e.txt | head"
}
```


### [2026-09-06T16:12:36.269Z] TOOL RESULT

```
--- 66537b92 (vajehyab dehkhoda) ---
URL: https://vajehyab.com/dehkhoda/%D8%B3%DB%8C%D8%A7%D9%87+%DA%AF%D9%88%D8%B4
FETCHED: 2026-09-06T15:58:44Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 500: Internal Server Error--- 92226094 (fa.wikipedia) head ---
URL: https://fa.wikipedia.org/wiki/%D8%B3%DB%8C%D8%A7%D9%87%E2%80%8C%DA%AF%D9%88%D8%B4_(%D9%88%D8%B4%D9%82)
FETCHED: 2026-09-06T15:58:45Z
STATUS: 200
TITLE: لینکس (وشق) - ویکی‌پدیا، دانشنامهٔ آزاد

لینکس (وشق) - ویکی‌پدیا، دانشنامهٔ آزاد 

 پرش به محتوا 

 منوی اصلی 

 منوی اصلی

 انتقال به نوار کناری 
 نهفتن 

 بازدید محتوا

 صفحهٔ اصلی 
 رویدادهای کنونی 
 مقالهٔ تصادفی 

 همکاری

 تغییرات اخیر 
 ویکی‌نویس شوید! 
 راهنما 
 تماس با ویکی‌پدیا 
 صفحه‌های ویژه 

 جستجو 

 جستجو 

 ظاهر 

 کمک مالی 

 ساخت حساب 

 ورود 

 ابزارهای شخصی 

 کمک مالی 

 ساخت حساب 

 ورود 

 فهرست

 انتقال به نوا�
20
قره‌ناز
```


## [2026-09-06T16:12:45.648Z] TOOL CALL #69: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://fa.wikipedia.org/wiki/%DA%A9%D8%A7%D8%B1%D8%A7%DA%A9%D8%A7%D9%84' --note 'page 243 entry 0 node 3: Persian Wikipedia کاراکال / سیاه‌گوش, Turkish karakulak' 2>&1 | tail -2\nf=$(python3 - <<'EOF'\nimport json\nfor l in open('/home/sfmqrb/git/rishe/data/verification/sources/web/index.jsonl',encoding='utf-8'):\n    d=json.loads(l)\n    if 'D8%A7%D8%B1%D8%A7' in d.get('url','') or 'کاراکال' in d.get('url',''):\n        print(d['file'])\nEOF\n)\necho \"FILE=$f\"; grep -o \"قره[^ ]*\\|کاراکولاک\\|کاراکال[^ ]*\\|سیاه‌گوش\" \"/home/sfmqrb/git/rishe/$f\" 2>/dev/null | sort | uniq -c | head -20; grep -n \"کولاک\\|قولاق\" \"/home/sfmqrb/git/rishe/$f\" | head -5"
}
```


### [2026-09-06T16:12:57.380Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/4c80fe1502f4d86a.txt
FILE=data/verification/sources/web/d9f99415246a8d20.txt
data/verification/sources/web/ec1cfc60b91d7745.txt
data/verification/sources/web/4c80fe1502f4d86a.txt
ugrep: warning: /home/sfmqrb/git/rishe/data/verification/sources/web/d9f99415246a8d20.txt
data/verification/sources/web/ec1cfc60b91d7745.txt
data/verification/sources/web/4c80fe1502f4d86a.txt: No such file or directory
```


## [2026-09-06T16:13:00.715Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && head -5 4c80fe1502f4d86a.txt && echo \"=== hits ===\" && grep -o \"کاراکولاک\\|قره‌قولاق\\|قره قولاق\\|سیاه‌گوش\\|کارا[^ ]*\" 4c80fe1502f4d86a.txt | sort | uniq -c | head -20 && echo \"=== ctx ===\" && grep -n \"کولاک\\|قولاق\" 4c80fe1502f4d86a.txt | head -5"
}
```


### [2026-09-06T16:13:00.797Z] TOOL RESULT

```
URL: https://fa.wikipedia.org/wiki/%DA%A9%D8%A7%D8%B1%D8%A7%DA%A9%D8%A7%D9%84
FETCHED: 2026-09-06T16:12:57Z
STATUS: 200
TITLE: کاراکال - ویکی‌پدیا، دانشنامهٔ آزاد

=== hits ===
     48 سیاه‌گوش
      1 کارا:
     35 کاراکال
      2 کاراکال)
      1 کاراکال»
      1 کاراکال&oldid=43808131
      1 کاراکولاک
      1 کاراناها
=== ctx ===
357: هرچند نام سیاهگوش، به عنوان یکی از گربه‌سانان بومی ایران به گوش‌ها کاملا آشناست اما عموما نه تنها توسط رسانه‌ها بلکه از سوی فعالان و کارشناسان حیات وحش و حتی مسئولان محیط زیست هم به اشتباه مورد استفاده قرار می‌گیرد. به گونه‌ای که به ویژه طی سالهای گذشته تصویری که با شنیدن نام سیاه‌گوش به ذهنمان خطور می‌کند، گربه‌سانی است با پوستی نقش‌دار شبیه پلنگ و دمی بسیار کوتاه که به زبان انگلیسی لینکس (Lynx) نامیده می‌شود. اما با جستجوی نام سیاه‌گوش در دائره‌المعارف‌ها، با صاحبی دیگر برای این نام آشنا می‌شویم. صاحبی که از لحاظ ظاهری بیشتر برازنده نام سیاه‌گوش است. گربه‌سانی با پوستی بدون نقش و ساده و گوش‌هایی سیاه‌رنگ که به زبان انگلیسی کاراکال (Caracal) نامیده می‌شود. کاراکال از نام ترکی این حیوان یعنی کاراکولاک (کارا: سیاه و کولاک: گوش) گرفته شده است.
```


## [2026-09-06T16:13:35.966Z] TOOL CALL #71: Write

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/fix.py",
 "content": "# -*- coding: utf-8 -*-\nimport json, io\n\np = \"/home/sfmqrb/git/rishe/data/verification/page-243.json\"\nd = json.load(open(p, encoding=\"utf-8\"))\n\nWIKI_FA = \"https://fa.wikipedia.org/wiki/%DA%A9%D8%A7%D8%B1%D8%A7%DA%A9%D8%A7%D9%84\"\n\nn = [x for x in d[\"entries\"][0][\"nodes\"] if x[\"id\"] == 3][0]\n\nn[\"sources\"] = [\"https://en.wiktionary.org/wiki/caracal\", WIKI_FA]\n\nn[\"derivation\"] = (\n \"Persian قره‌قولاق qare-qulāq 'caracal' is the Ottoman/Azeri compound taken over whole, with no adaptation \"\n \"beyond the Persian spelling of the vowels; it lives alongside the native Persian name سیاه‌گوش siyāh-gūš. \"\n \"Persian Wikipedia s.v. کاراکال states the relation in one sentence: «کاراکال از نام ترکی این حیوان یعنی \"\n \"کاراکولاک (کارا: سیاه و کولاک: گوش) گرفته شده است» — and identifies the animal called سیاه‌گوش in Persian \"\n \"with Caracal caracal. Lokotsch no.1081 makes the same pairing from the other side: 'Tk. karakolak: „Schwarzohr“ \"\n \"ist der Name eines kleinen Raubtieres [pers. ebenso sijäh gus „schwarzes Ohr“ genannt]'. The chart's NOTE \"\n \"('Compare with syâh-gŭsh:caracal from root Kei 1') is therefore not merely a comparison but the historical key, \"\n \"and modern scholarship settles the direction: Persian سیاه‌گوش (siyāh 'black' + gōš 'ear', Old Persian gauša-, \"\n \"Avestan gaoša-) is the model, Turkic qara-qulaq the element-for-element calque of it (so Wiktionary s.v. caracal: \"\n \"Ottoman Turkish kara kulak is 'a calque of Classical Persian سیاه‌گوش'), and قره‌قولاق the calque coming back into \"\n \"Persian as a loan — a semantic round trip. Klein records the Persian original under its Anglo-Indian form: \"\n \"'syagush, n., the caracal. — Pers.-Hind. siyah-gosh, lit. „black ear“ … The second element derives fr. OPers. \"\n \"gausha-, ModPers. gosh, „ear“'. In modern Persian قره‌قولاق also survives as a Qashqai/Khamseh tribal name.\"\n)\n\nn[\"derivation_fa\"] = (\n \"«قره‌قولاق» در فارسی همان ترکیب ترکی عثمانی/آذربایجانی است که یکجا وام گرفته شده و جز املای فارسیِ واکه‌ها هیچ \"\n \"تغییری نکرده؛ در کنار نام بومی فارسی «سیاه‌گوش» به کار می‌رود. ویکی‌پدیای فارسی ذیل «کاراکال» می‌نویسد: «کاراکال \"\n \"از نام ترکی این حیوان یعنی کاراکولاک (کارا: سیاه و کولاک: گوش) گرفته شده است» و همین جانور را در فارسی «سیاه‌گوش» \"\n \"می‌نامد. لوکوچ (شمارهٔ ۱۰۸۱) نیز از سوی دیگر همین جفت را می‌آورد: «ترکی karakolak «گوش‌سیاه» نام جانوری شکاری است \"\n \"[در فارسی نیز همان را سیاه‌گوش می‌نامند]». پس یادداشت خودِ نورایی («با سیاه‌گوش از ریشهٔ Kei 1 بسنجید») تنها یک \"\n \"مقایسه نیست، بلکه کلید تاریخی ماجراست: پژوهش امروزی جهت وام‌گیری را روشن کرده است — «سیاه‌گوش» فارسی (سیاه + گوش، \"\n \"از پارسی باستان gauša-، اوستایی gaoša-) الگوی نخستین است، qara-qulaq ترکی گرته‌برداری جزء‌به‌جزء از آن (ویکی‌واژه \"\n \"ذیل caracal همین را می‌گوید)، و «قره‌قولاق» بازگشت همان گرته به فارسی در جامهٔ وام‌واژه؛ یعنی یک رفت‌وبرگشت معنایی. \"\n \"کلاین نیز صورت اصلی فارسی را زیر «syagush» آورده است. ادعای نورایی درست است.\"\n)\n\nn[\"consulted\"][0] = {\n \"src\": \"Wikipedia (fa)\", \"where\": \"fa.wikipedia.org s.v. کاراکال\", \"stance\": \"supports\",\n \"note\": \"«کاراکال از نام ترکی این حیوان یعنی کاراکولاک (کارا: سیاه و کولاک: گوش) گرفته شده است»; the article \"\n         \"treats سیاه‌گوش and کاراکال as names of the same animal. (Dehkhoda's own entry could not be archived: \"\n         \"vajehyab.com returned HTTP 500 on both attempts, so it is not cited here.)\"\n}\n\nwith io.open(p, \"w\", encoding=\"utf-8\") as f:\n    json.dump(d, f, ensure_ascii=False, indent=1)\n    f.write(\"\\n\")\nprint(\"patched\")\n"
}
```


### [2026-09-06T16:13:35.998Z] TOOL RESULT

```
File created successfully at: /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/fix.py (file state is current in your context — no need to Read it back)
```


## [2026-09-06T16:13:41.132Z] TOOL CALL #72: Bash

```json
{
 "command": "python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/fix.py && python3 -m json.tool data/verification/page-243.json >/dev/null && echo JSON-OK && python3 - <<'EOF'\nimport json\nd=json.load(open('data/verification/page-243.json'))\nimport re\nurls=set()\nfor e in d['entries']:\n    urls.update(e.get('sources',[]))\n    for n in e['nodes']: urls.update(n.get('sources',[]))\nidx={}\nfor l in open('data/verification/sources/web/index.jsonl',encoding='utf-8'):\n    j=json.loads(l); idx[j['url']]=j['file']\nfor u in sorted(urls):\n    print(('OK  ' if u in idx else 'MISS'), u)\nEOF\npython3 tools/verify_check.py 243"
}
```


### [2026-09-06T16:13:43.819Z] TOOL RESULT

```
patched
JSON-OK
OK   https://ahdictionary.com/word/search.html?q=caracal
OK   https://en.wiktionary.org/wiki/%CE%BA%CE%AC%CF%81%CF%80%CE%B1%CF%83%CE%BF%CF%82
OK   https://en.wiktionary.org/wiki/%D9%83%D8%A7%D9%81%D9%88%D8%B1
OK   https://en.wiktionary.org/wiki/%DA%A9%D8%B1%D8%A8%D8%A7%D8%B3
OK   https://en.wiktionary.org/wiki/%E0%A4%95%E0%A4%B0%E0%A5%8D%E0%A4%AA%E0%A5%82%E0%A4%B0
OK   https://en.wiktionary.org/wiki/Reconstruction:Proto-Turkic/kara
OK   https://en.wiktionary.org/wiki/camphor
OK   https://en.wiktionary.org/wiki/caracal
OK   https://en.wiktionary.org/wiki/carbasus
OK   https://fa.wikipedia.org/wiki/%DA%A9%D8%A7%D8%B1%D8%A7%DA%A9%D8%A7%D9%84
OK   https://www.etymonline.com/word/camphor
nodes verified: 17/17
node verdicts: {'confirmed': 13, 'plausible': 4}
root verdicts: {'plausible': 3}
ref checks: {'supports': 18, 'not_found': 1, 'partial': 5, 'not_checked': 1}
books consulted: {'supports': 37, 'partial': 9, 'silent': 11, 'contradicts': 4} | by book: {'LKT': 8, 'KLN': 6, 'SKT': 5, 'HUB': 4, 'PLA': 4, 'MON': 3, 'WEB': 3, 'FSD': 3, 'PHD': 3, 'LAT': 3, 'HRN': 2, 'AFM': 2, 'SYN': 2, 'FVQ': 2, 'TTS': 1, 'Wikipedia (fa)': 1, 'AFA': 1, 'Wiktionary (Persian)': 1, 'BQT': 1, 'HJB': 1, 'Wiktionary (Ancient Greek)': 1, 'LEW': 1, 'NYB': 1, 'SIN': 1, 'DOZ': 1}
```


## [2026-09-06T16:14:09.128Z] AGENT

Page 243 done — `data/verification/page-243.json` written, `verify_check.py 243` reports **0 PROBLEM lines**, 17/17 nodes covered.

**Verdicts** — nodes: 13 confirmed, 4 plausible. Roots: 3 plausible (entries 0, 2, 3; entries 1 and 4 are redirects, skipped).
**Ref checks**: 18 supports, 5 partial, 1 not_found, 1 not_checked. **Books consulted**: 37 supports, 9 partial, 11 silent, 4 contradicts (25 distinct books/sites).

**No `disputed` and no `transcription_suspect` items; no extraction errors** — the JSON matches the chart text everywhere, so no page image had to be rendered.

Why the three roots are `plausible` rather than `confirmed` (the substance of the page):
- **Kar 2/Qar 2** — TTS:79 checks out exactly (Vámbéry entry no. 84 begins at the foot of p.79: "kar, kir, kur, schwarz, trocken, dürr, alt, Unglück…"), but the "black + old + bad luck" bundle is Vámbéry's 1878 root-lumping; modern Turkology separates *kara from *karɨ- "grow old" and *karga- "curse".
- **Karpâsah** — the very page Nourai cites against himself: Buck SYN:402 §6.24 says "Skt. karpāsa-, *loanword* fr. the same source as Grk. κάρπασος, Lat. carbasus, Arab. kerpas", i.e. Greek is a sister borrowing, not a daughter of Sanskrit (Klein 238 adds Porzig's Mediterranean/Asia-Minor source; Wiktionary routes Greek via Biblical Hebrew karpas).
- **Karpurah** — Sanskrit karpūra- means "camphor", not "camphor tree", and is itself a loan (Malay kapur / kapur Barus). The chart's own note ("AHD traces this to Malay kâpŭr") is the accepted modern view, not a rival one — Skeat 1911, Etymonline, AHD and Wiktionary all agree.

Two node-level findings worth the owner's eye:
- **Karpurah #2/#3 order is inverted.** MP kāpūr is well attested (MacKenzie: "kāpūr [kʾpwl | Ar. kāfūr] camphor"; BQT:1571 Mo'in footnote gives Skt karpūra + "در پهلوی kāpūr"), but MP intervocalic *p* does not give NP *f*. The *f* of کافور is Arabic's substitution for Iranian *p*, so the chain is MP kāpūr → Arabic kāfūr → NP kāfūr, not NP → Arabic. Both nodes marked `plausible`.
- **Karpâsah #3** (`plausible`): Mo'in backs Nourai's round trip verbatim — «کرباس [هند. کرپاس ـ معرّب کرپاس]» — but Wiktionary makes NP karbās simply inherited from MP, no Arabic detour. Also noted: Asbaghi (PLA p.227) cites "Mackenzie s.v." for a MP *karbas* — MacKenzie's karbāš actually glosses 'lizard'; that citation is a slip in Asbaghi, not in Nourai.

Ref-check limits: MON:2650/2670/2932 pages can't be verified against the local two-volume Adena abridgement (entries found and supportive; قره‌قولاق absent from the abridgement → `not_found`); AHD:201/202 checked against the online AHD (only Watkins's IE appendix is on disk); VDQ:356 unreachable (noorlib JS viewer) so Jeffery FVQ 246-247 was read instead; TAD's OCR has no page markers so TAD:60 could not be pinned, though the claim ("in Greek kaphoura") is genuinely al-Unaysi's — and backwards, since Greek καφουρά is itself from Iranian.

All 11 cited web pages were archived via `fetch_source.py` and verified present in the index. Nothing was committed.
