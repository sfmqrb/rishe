# Verification process log — verify-page-338


## [2026-09-07T17:35:59.417Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 338 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-338.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-338.json. Write /home/sfmqrb/git/rishe/data/verification/page-338.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 338` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T17:36:01.107Z] AGENT

I'll start by reading the instructions.


## [2026-09-07T17:36:01.730Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T17:36:01.757Z] TOOL RESULT

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


## [2026-09-07T17:36:01.870Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-338.txt"
}
```


### [2026-09-07T17:36:01.907Z] TOOL RESULT

```
1	=== PDF page 338 (book page 308) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Meu 1 : damp, dirty  (refs POK:741)
4	#1 (parent #0) [Avestan] refs=POK:741; HRN:285; KLN:1008 | mŭthra : dirty liquid, urine
5	#2 (parent #0) [Germanic] refs=AHD | meus : damp
6	  #3 (parent #2) [English] refs=None | moss
7	#4 (parent #0) [Latin] refs=AHD | mustus : wet, new
8	  #5 (parent #4) [English] refs=None | must 2 : damp ; mustard
9	#6 (parent #0) [Middle Greek] refs=AHD | mudde : wet earth
10	  #7 (parent #6) [English] refs=None | mud
11	--- entry 1 ---
12	ROOT Meu 2 -> redirect to Mew
13	--- entry 2 ---
14	ROOT [Indo-European] Meug : wet, slippery, also to give up, let go, flee, deliver, describe  (refs POK:744)
15	#1 (parent #0) [Avestan] refs=POK:744; FFD:27 | fra-muxti : open up, describe, clarify ; a-maux-ta : learned
16	  #2 (parent #1) [Persian] refs=FFD:27; MON:91 | âmŭxtan «آموختن» : to learn ; âmŭzândan «آموزاندن» : to teach | extra: آموز ، آموزش ، آموزگار ، آموزشگاه
17	#3 (parent #0) [Old Persian] refs=POK:744 | a-mutha, a-muntha : fled
18	#4 (parent #0) [Sanskrit] refs=POK:744 | mŭkti : slipped out, lost, anything thrown away (worthless) ; munthate : untie, describe, explain
19	  #5 (parent #4) [Persian] refs=BQT:2024; HRN:221 | moft «مفت» : worthless, free
20	#6 (parent #0) [Germanic] refs=AHD | smug : wetness, figurative slipperiness
21	  #7 (parent #6) [English] refs=None | smuggle
22	#8 (parent #0) [Greek] refs=None | muxa : lamp wick
23	  #9 (parent #8) [English] refs=None | match 1 : a piece of wood that catches fire by friction
24	#10 (parent #0) [Latin] refs=None | mucŭs : moist
25	  #11 (parent #10) [English] refs=None | moist, mucus
26	
```


## [2026-09-07T17:36:05.638Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-338.json | head -200",
 "description": "Read source JSON for page 338"
}
```


### [2026-09-07T17:36:05.682Z] TOOL RESULT

```
{
  "pdf_page": 338,
  "book_page": 308,
  "entries": [
    {
      "root": {
        "name": "Meu 1",
        "lang": "Indo-European",
        "refs": "POK:741",
        "gloss": "damp, dirty"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:741; HRN:285; KLN:1008",
          "words": [
            {"translit": "mŭthra", "gloss": "dirty liquid, urine", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "meus", "gloss": "damp", "script": null}
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
            {"translit": "moss", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "mustus", "gloss": "wet, new", "script": null}
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
            {"translit": "must 2", "gloss": "damp", "script": null},
            {"translit": "mustard", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Middle Greek",
          "refs": "AHD",
          "words": [
            {"translit": "mudde", "gloss": "wet earth", "script": null}
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
            {"translit": "mud", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Meu 2",
        "redirect": "Mew"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Meug",
        "lang": "Indo-European",
        "refs": "POK:744",
        "gloss": "wet, slippery, also to give up, let go, flee, deliver, describe"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:744; FFD:27",
          "words": [
            {"translit": "fra-muxti", "gloss": "open up, describe, clarify", "script": null},
            {"translit": "a-maux-ta", "gloss": "learned", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "FFD:27; MON:91",
          "words": [
            {"translit": "âmŭxtan", "gloss": "to learn", "script": "آموختن"},
            {"translit": "âmŭzândan", "gloss": "to teach", "script": "آموزاندن"}
          ],
          "script_extra": "آموز ، آموزش ، آموزگار ، آموزشگاه",
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "POK:744",
          "words": [
            {"translit": "a-mutha, a-muntha", "gloss": "fled", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK:744",
          "words": [
            {"translit": "mŭkti", "gloss": "slipped out, lost, anything thrown away (worthless)", "script": null},
            {"translit": "munthate", "gloss": "untie, describe, explain", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "BQT:2024; HRN:221",
          "words": [
            {"translit": "moft", "gloss": "worthless, free", "script": "مفت"}
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
            {"translit": "smug", "gloss": "wetness, figurative slipperiness", "script": null}
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
            {"translit": "smuggle", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Greek",
          "refs": null,
          "words": [
            {"translit": "muxa", "gloss": "lamp wick", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
```


## [2026-09-07T17:36:05.796Z] TOOL CALL #4: Bash

```json
{
 "command": "sed -n 1,200p data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-07T17:36:05.849Z] TOOL RESULT

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


## [2026-09-07T17:36:31.606Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','AHD','HRN','KLN','FFD','MON','BQT','WLD','IEC','SYN','LEW','LAT']:\n    v=d.get(k,{});print(k, v.get('kind'), v.get('local_file'), v.get('page_offset'), str(v.get('lookup_hint'))[:200])\n\"",
 "description": "Check ref metadata"
}
```


## [2026-09-07T17:36:32.076Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/ | head -40 && echo --- && sed -n 1,60p tools/verify_check.py",
 "description": "List verification dir and check tool"
}
```


### [2026-09-07T17:36:32.850Z] TOOL RESULT

```
POK archive_djvu /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.i
AHD archive_djvu+website+archive_restricted /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the 
HRN archive_djvu /home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered ent
KLN archive_djvu /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume p
FFD local_scan_ocr ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages_faseng.txt'] 115 leaves (PDF pages); printed page = PDF page − 5 (PDF 40 = p.35). 2nd printing 1385 of the same Qoqnus setting (ISBN 964-311-015-X). Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a d
MON website+archive_djvu ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'] None Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Aves
BQT archive_djvu+local_scan_ocr ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'] vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'http
WLD archive_djvu ['/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt'] Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696). Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, u
IEC archive_djvu /home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.
SYN archive_djvu /home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed p
LEW archive_djvu /home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt 1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Latin headword in bold at line start. For 1938 pagination borrow lateinischesetym0000awal.
LAT archive_djvu /home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt leaf = printed + 18 for most of the book (e.g. leaf 21 = p.3); drifts in places (leaf 219 = p.301 -> -82?? probably a mis-detected number) - grep the headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Latin headword in bold at line start followed by gender/declension, e.g. grep -n '^pater,'.
```


### [2026-09-07T17:36:32.919Z] TOOL RESULT

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
---
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


## [2026-09-07T17:36:38.735Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in POK_01.txt POK_02.txt POK_03.txt; do echo \"$f: $(awk 'BEGIN{RS=\"\\f\"} END{print NR}' $f) leaves\"; done",
 "description": "Count leaves in Pokorny files"
}
```


### [2026-09-07T17:36:39.909Z] TOOL RESULT

```
POK_01.txt: 363 leaves
POK_02.txt: 433 leaves
POK_03.txt: 429 leaves
```


## [2026-09-07T17:36:40.206Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^meu-\\|^1\\. meu-\\|^2\\. meu-\\|^3\\. meu-\\|^meug-\\|^meu\\b\" POK_full.txt | head -40",
 "description": "Grep Pokorny full for meu roots"
}
```


### [2026-09-07T17:36:40.261Z] TOOL RESULT

```
60513:1. meu-d-; mud-ro-3\er\, awake, smart' (compare "humid, wet-cheerful'). 
60552:3. meu-r(o)-e\.c.:
```


## [2026-09-07T17:36:44.667Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Pages in Pokorny\\|741\\b\" POK_full.txt | head -5; echo ---; grep -n \"meu-\" POK_full.txt | sed -n 1,60p",
 "description": "Explore POK_full structure"
}
```


### [2026-09-07T17:36:44.725Z] TOOL RESULT

```
6896:Root form (a)fi-, re/-{see Person root extension 102, 162, 232; Beitr. 741): 
22509:Gr. I 492, 686, 722, 725, 741, Pedersen Hittite 141 ff., 192. 
23552:741 , 794, 806 ff., Trautmann 56 ff. 
34227:References: WP. I 659, WH. I 337 f., 741 f. 
42341:doubting Schwyzer Gr. Gr. I 686, 741 . Frisk (Eranos 41 , 49 f.) decides because of 
---
57124:"slave'; corn, maw, bret. mao^ youngling, servant', cymr. meu-dwy' hermit, servant of God 
60470:Root/ lemma: meu-1, meue-. mu- 
60507:from *mu-n-d-os{-d-\.o root extension meu-d-) in tlie meaning " washed, made clean ' 
60513:1. meu-d-; mud-ro-3\er\, awake, smart' (compare "humid, wet-cheerful'). 
60526:Latin mundus {see above meu-)\ 
60552:3. meu-r(o)-e\.c.: 
60609:Root / lemma: meu-s- 
60614:Root / lemma: meu-2, meua- 
60640:A s-extension seems *meu-s-\n Old Indie musnati, /77dsa//"stiehlt', mosa-^ robber, 
61735:probably to Old Indie musnati' steals, robs ' etc., see below meu-2'push away '. 
78410:Root / lemma: (s)mei-1, smeu- 
78436:Besides smeu-\x\. 
78668:Root / lemma: smeu- 
78775:A ^/-variant (s)meu-\ (s)m9u-\ (sjmu- seems vorzuliegen in Old Icelandic ma{*mawen)
```


## [2026-09-07T17:36:47.033Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n 60465,60560p POK_full.txt",
 "description": "Read Pokorny meu-1 entry"
}
```


### [2026-09-07T17:36:47.085Z] TOOL RESULT

```
References: WP. II 255, WH. II 117 f. 

Page(s): 745 

Root/ lemma: meu-1, meue-. mu- 

Meaning: wet; dirt; to wash, etc.. 

Material: A. Old Indie mutra-n. "urine', Avestan mu^ra-n. " filth, smut' (: Middle Low 

German modder e\.c.); 

Maybe alb. mut, mutra{p\) 'excrement, dirt' 

Armenian -/77oy/7 "wash in the pot' {*mou-no-)\ 

gr. Cypriot [juAaaaaGai "be washed', Hes. {*mu-dlo-)\ 

Middle Irish munm. "urine'; mur'sWme, mud'; 

perhaps (?) Dutch moo/, mnl. moy, Low German /77c»//'e'y' "beautiful' {*mou-/o-' washed, 
made clean '); 

Latvian maut^ submerge, swim, swig ', Old Prussian aumusnan^ wash, cleansing ', 
causative (Iterat.) Lithuanian maudyti, Latvian maudaV bathe somebody ', Lithuanian 
maustyti 6s.\ Latvian mudet' soit, become moldy '; 

Old Bulgarian myjg, myt/' wash, rinse ', /77y/c» (proto Slavic. Czech etc. mydio-) " soap '; 

Maybe alb. Geg myt, Tosc mt>yt' drown, strangle ' a Slavic loanword? 



with. ani. 5- Latvian smau//s' ein schmutzig gewordener', smu/et' befoul ', smu//s'a 
sloven '; 

poln. kir. /77^/ "slime, mud', russ. dial. mu//tb {vodu) "(water) go cloudy ' {mou-lo-); forms 
with A-suffix, respectively ^-extension see below; 



from *mu-n-d-os{-d-\.o root extension meu-d-) in tlie meaning " washed, made clean ' 
also Latin mundus^ clean, cleanly, nice, neat, elegant, toilet ornament, decoration, dress 
(of women), the world, earth, inhabitants of the earth, mankind ' (after gr. K6apo(;); 

B. extensions: 

1. meu-d-; mud-ro-3\er\, awake, smart' (compare "humid, wet-cheerful'). 

Old Indie mudira-m. "cloud', lex. also "frog'; in addition Old Indie m6date^\s funny', 
moda-m., modana-n. "lust, cheerfulness ', Avestan maodano-karana-^ causing lust ', Old 
Indie /77^o''//a "blithe, glad', Avestan a-h§musta- {*a-sam-musta-) " disgusting, unsavory, 
distasteful'. Old Indie mud-, mudalust, pleasure, joy', mudra-' funny '; 



gr. |ju^w {*mudjd) "suck', [juSoc; m. " damp, decay ', puSau) "be humid, wet, decayed ', 
Mu5aA£0(; "humid, wet' (hom. u: through metr. lengthening, whereupon newer puSaivoj " 
irrigate '); 

Latin mundus {see above meu-)\ 

Middle Irish muad {*moudo-) "pure, stout, proud'; 

Middle Low German muten^ wash the face ', Old High German muzzan^c\eav\\ 
Swedish dial, muta^ fine rain', Dutch /77c»/"fine rain'; 

with ani. 5-engl. smut^ smirch, stain, splotch ', Middle High German smuz. Modern High 
German Schmutz, Middle English smotten, smoteren " befoul '; 

Lithuanian mudrus, Latvian mudrs^a\ert, awake, smart' (: Old Indie mudra-), Lithuanian 
mudrinti, Latvian mudfV set in motion '. 

From in -es-stem m(e)udes-\\3Ne derived: 

Latin mustus {*muds-to-s) " young, new, fresh ' (originally "damp, humid, wet'); gr. puao(; 
(*|ju5ao(;) n. " maculation, blemish'; [juaap6(; " dishonorable '; Old Irish /77c»ss5c/7 "impure, 
unclean' {*mud-s-ako-), cymr. mws, bret. mous ds.; ndd. muss/g'd\(iy, filthy'; russ. muslitb 
" drool, drivel, slaver ', musljaki, " dribbler, unclean person'. 

Maybe alb. /77i/s/7/"must, new wine' a Latin loanword. 

2. meug-, meuk-^ slippery ' see below esp. headword. 



3. meu-r(o)-e\.c.: 

Armenian /770/''smut, swamp, marsh' {*m9u-ri-l), mrur^ deposit ' {*murui)\ gr. pupco 
(*[jupju)), pupofjai " let flow, weep, cry', aAi-|Jupn£ic; ' flowing to the sea '; whether here 
Mupio(; " eternal, infinite, endless ', [jupioi '10.000'? Latin muria' brine, pickle '? Lithuanian 
murstu, murtr become soppy ', m. PI. mauraf duckweed, stemless water plant ', Latvian 
maursm. 'lawn', Lithuanian /77a^/'as 'slime, mud', ablaut, murasxu. 'smut', Latvian murfV 
befoul '; russ. murvn. muravat ' oat-grass, false oat, tall oatgrass ', dial. ' mildew ', muryj' 
dark grey ', etc.; compare S. 741 Middle Irish mur^sWme, mud'.
```


## [2026-09-07T17:36:51.772Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>60470 && NR<60620 && (/^Page\\(s\\)/ || /^References/ || /^Root/)' POK_full.txt; echo \"=== meug ===\"; grep -n \"meug-, meuk-\\|Root/ lemma: meug\\|Root / lemma: meug\" POK_full.txt | head",
 "description": "Find page numbers and meug entry"
}
```


### [2026-09-07T17:36:53.057Z] TOOL RESULT

```
References: WP. Il249ff., WH. II 126 f., 130, 134, 136, Trautmann 172, 188, 190 ff., 
Page(s): 741-743 
Root / lemma: meu-s- 
Page(s): 745 
Root / lemma: meu-2, meua- 
=== meug ===
60336:Root / lemma: meug-1 
60355:Root / lemma: meug-2, meuk- 
60548:2. meug-, meuk-^ slippery ' see below esp. headword.
```


## [2026-09-07T17:36:55.380Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n 60336,60470p POK_full.txt",
 "description": "Read Pokorny meug entries"
}
```


### [2026-09-07T17:36:55.442Z] TOOL RESULT

```
Root / lemma: meug-1 

Meaning: to take by surprise, wily 

Material: Latin muger^ der Falschspieler beim WiJrfelspiel ' {*mug-ro-s^ lurking '); 

Old High German muhhari, muhh(e)o^ highwayman, mugger, footpad, thief, muhhon^ 
lurk secretly, attack ', Middle High German vermuchen^ heimlich auf die Seite schaffen ', 
late-Old High German muhhilari {{o *muchildn). Modern High German Meuchler, Middle 
High German miucher secret ', Old High German muh-heimo^ cricket, leaping insect 
which is related to the grasshopper ', ablaut. Middle High German mocken^ lie hidden, 
concealed ', Middle English /77/c/7e/''thief, engl. dial, /o/t?/^/? 'hidden, concealed sein, 
steal'. 

Maybe alb. mih' dig, hoe '. 

References: WP. II 255, Wissmann Nom. postverb. 137; probably to Folgendem. 
Page(s): 743-744 

Root / lemma: meug-2, meuk- 

Meaning: to slide, slip 

Note: also with aniaut. 5- 

Material: A. Latin /77Jci/s 'mucus', mucor^ mildew ', e-mungo, -ere^ to wipe the nose, blow 

the nose, to cheat, swindle '; mugilvn. ' mullet '; 

Maybe alb. myku^ fungus ' a Latin loanword. 



gr. aiTo-iJuaaoo " blowing one's nose, clear one's nasal passages by forcible exhalation; 
cheat, deceive, swindle; betray, be disloyal; gull, fool', ano-pu^ic; ' the blowing one's nose ' 
(: Latin e-m undid), puKirip 'nose, nostril '. 

Maybe Greek (s)MUKTrip "nose, nostril ' > Basque {*smuktor) sudur^ nose' : Albanian 
{*smukta) hunde, hunda^ nose', hundor^ nasal'. 

gr. \x\}%a 'mucus, nose' (based on *fjuK-a-6(; 'slimy', as also:) mu^O(;, jju^Tvoc;, jju^ojv ' 
mullet ' (also apu^wv with ani. 5- as by Hes. also apuaasTai, apuKirip), \x\}gkoc, piaaija 
Hes. (*[JUK-a-KOc;), a|Juoxp6(;, ajjuxvoc; ' unsoiled; untainted, pure, holy'; |JUKr|<;, -Htoc; ' 
fungus '; 

cymr. mign {*mukino-) 'swamp, marsh'; 

with anI. s- gael. smuc, smug'snot' (expressive); Middle Irish mocht'soit', cymr. mwyth 
ds. ( *muk-to-)\ 

Old Icelandic myg/at ' mildew ', muggal\ne rain'. Middle English mugen^ become 
foggy ', Modern High German dial, mauge/loggy, cloudy, dim, hazy'. Old English for- 
mogod' decayed '; with Indo Germanic g:0\6 Icelandic mykrand myk/i. ( *mukl} ' 
manure'. Middle High German muchein, mucheln^ moldy smell'. Old Icelandic mjukr{o\A 
of it engl. meek) 'soft', changing through ablaut Gothic muka-mode'r gentleness, softness, 
kindness ', mnl. muik^soii'. Modern High German dial, maukig^ decayed ', Swiss mauch^ 
rotten, decayed, decomposed; brittle, faint, languid, hungry' (as Swiss mucMla\nt, 
languid, hungry'); Middle High German muche' quitter, infection of the hoof, Gothic 
*maukd in prov. mauca ' intestines '; 

Latvian mukis, muklams^ fenny, boggy, marshy ', muku {*munku), mukV sink into a 
marsh '; 

Serbo-Croatian /77£/A^/V' humid, wet'. 

B. Old Indie *munakti, muncati, mucatr releases, allows to loose', mukti-^ lysis, 
dissolution, disintegration, release, abandonment '; Avestan fra-muxti-^ loosening '; 
compare Old Indie munthate ' flees ', Old pers. amu(n)&a ' he fled ' from * mu-n-eth-m'r, 

Lithuanian munku, muktT escape; to get away ' = Latvian muku, mukV get free, flee' 
(and ' sink into a marsh ' see above); Lithuanian (s)mauktr wander stealthily ', Latvian 
maukV strip, wipe ', Lithuanian (s)munku, (s)mukti^ sink sliding, slip '; 



Slavic *(s)m-bkngtr slip, slide' in Czech smeknoutF withdraw from, take away ', Old 
Church Slavic Refl. smycg, smykati sg^ grovel, truckle, creep ' (modern Slavic also " slip, 
stumble, glide, slide, strip, wipe '), russ. -Church Slavic nrbknuti sja^ go over, go across, 
cross over, pass over, pass by, pass ', Old Church Slavic mhcati {nrbke-) " throw, cast, 
hurl ', etc. 

A root form meukh-W\Vc\ the specific meaning ' slip into ' probably in Armenian mxem 
{*muxam) " stick in, stick into, put in, dive, bathe ', /77i/A' "dyeing', mxim^ enrare, insinuarsi, 
ingolfarsi ', at first to gr. |jux6(; m. " internal angle ' (perhaps "*hiding place, nook, bolt- 
hole'), Muxioc; " innermost, inmost, located farthest within '. 

Auf (sjmeugh- based on the Germanic family: 

Old Icelandic smjuga' creep into or crawl through ', Old English smugan' slip, slide; 
stumble, grovel, truckle, creep ', Middle High German smiegen^ crouch ', Modern High 
German schmiegen, Kaus. Old Icelandic smeygia^ nestle, cuddle, snuggle, lure, tempt ', 
Middle High German sich smougen' crouch ', Old English 5/77ea^ 'smart, sharp witted, 
shrewd', s/77e5^5/7 "think, seek ', smeagorv\arro\N, tight, slim, slender, thin ', Old Icelandic 
smugat " loop hole; hiding place ', further Swedish i mjugg, Norwegian i mugg^ furtive '. 

with 5- Danish Norwegian i smug, Dutch ter smuig {ter smuik) ds., Danish Norwegian 
smughander illicit trade ', ndd. smuggein. Modern High German (out of it) schmuggein 
(with A/Dutch smokkelen 6s.)\ probably also Modern High German mogein. Low German 
mogelen, muggelen^ heimliches, betrijgerisches Spiel treiben '; with Germanic k{k): 
Norwegian dial, smokia, smuk/alurk, creep forward ', Swiss schmauchen^ steal secretly, 
nibble '; in the meaning ' nestle, cuddle, snuggle' Middle High German smuck^ nestlling 
up, jewellery', smucken. Middle Low German smucken^ nestle, snuggle, apparel, adorn'. 
Old High German smocco; Old English s/77c»c/r "shirt'. Old Icelandic smokkrm. " 
Frauenbrustlatz ', Middle Low German smuk{-ck-) ' sleek, smart, neat ', Middle High 
German gesmuckef slim '; 

-g-o\ -gh-\w Latvian smaugs^ slim ', Lithuanian smaugiT throttle, strangle ', Latvian 
smudzi, smudzT mosquito, small fly ', poln. smug, s/77^^5 (besides smuk) ' defile, narrow 
passage between mountains, bottleneck, narrow stripe '. 

References: WP. II 253 ff., WH. I 402 f., Trautmann 189 f., 271, Kuiper Nasalpras. 124 f., 

129. 

Page(s): 744-745 



Root / lemma: meuR- 

Meaning: to scratch, tear 

Material: Gr. apuKaAai ai qkiSec; twv peAwv, rrapa to ajjuaosiv Hes., ajjuoou), Attic apuTTU) 

" split, scratch ', a'puxn 'crack, scratch ', etc.; Latin mucro^ a sharp point, edge, sword's 

point '; perhaps to Old English ^e-/77ysc5A7 "plague, deform' {*muhskjan) and Lithuanian 

/77^5//"hit'; perhaps also Old Indie mustfi., Avestan must/-l\st'7 

References: WP. II 255, WH. II 117 f. 

Page(s): 745 

Root/ lemma: meu-1, meue-. mu-
```


## [2026-09-07T17:37:20.097Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD meu ===\"; grep -n \"meu-\\|meus-\\|meug-\" AHD_watkins1985.txt | head -30",
 "description": "Grep AHD Watkins for meu roots"
}
```


### [2026-09-07T17:37:20.143Z] TOOL RESULT

```
=== AHD meu ===
760:merk-'. To decay. Latin marcére, to decay, wither: MARCESCENT. [Pok. 1. merk- 739.] [merk-2. Italic root, possibly from Etruscan, referring to aspects of commerce. 1. Latin merx (stem merc-), mer- chandise (> mercdri, to trade): MARKET, (MART), MER- CER, MERCHANT; COMMERCE. 2. Latin merces, pay, reward, price: MERCENARY, MERCY. 3. Probably Latin Mercurius, the god of (inter alia) commerce: MERCURY. [In Pok. merk- 739.]] [merph-. Form. Greek root of unknown origin. 1. Suf- fixed o-grade form *morph-G- in Greek morphé, form, beauty, outward appearance: -MORPH, MORPHEME, MOR- PHO-, MORPHOSIS. 2. Possibly borrowed from Greek morphé, via Etruscan, is Latin forma, form, shape, contour, appearance, beauty: FORM, FORMAL, FORMULA; CONFORM, CORACIIFORM, DEFORM. [In Pok. 2. mer- 733.]] mers-. To trouble. Suffixed o-grade form mors-eyo- in Germanic *marzjan in Old English merran, mierran, to impede: MAR. [Pok. 6. mer- 737.] meu-. Damp; with derivatives referring to swampy ground and vegetation and to figurative qualities of wetness. 1. Extended form *meus- in Germanic *meus-, *mus- in: a. Old English mos, bog: Moss; b. Old Norse mosi, bog, moss, akin to the Scandinavian source of LITMUS. 2. Germanic suffixed form *meuz-i- in Old Norse myrr, bog: MIRE; (QUAGMIRE). 3. Suffixed zero-grade form *mus-to- in Latin mustus, new, newborn (< “wet”): MUST’, MUSTARD. 4. Possibly suffixed extended zero-grade form *mii-ro- in Greek murios, countless (< “flowing, endless”): MYRIAD. 5. Possibly suffixed ex- tended zero-grade form *mud-so- in Greek musos, un- cleanness: MYSOPHILIA, MYSOPHOBIA. [Pok. 1. meu- 741.] meue-. To push away. Latin movére, to move (> mobilis, neuter mobile, fickle, changeable): MOB, MOBILE, MO- MENT, (MOMENTOUS), MOMENTUM, MOSSO, (MOTIF), MO- TION, MOTIVE, MOTOR, MOVE, MOVEMENT; COMMOTION, EMOTION, PROMOTE, (REMOTE), (REMOVE). [Pok. 2. meu- 743.) meug-'. To act surreptitiously. Germanic *muk- or Celtic *mug- in Old French muchier, to skulk: MOOCH. [Pok. 1. meug- 743.] meug-2. Slimy, slippery; with derivatives referring to various wet or slimy substances and conditions. Enlarged form of meu-. 1. Nasalized form *mu-n-g- in Latin mungere, to blow the nose: EMUNCTORY. 2. Possibly Germanic *(s)mug-, referring to wetness and also to figurative slipperiness: a. Old English smoc, shirt: smock; b. Middle High German smuck, “clothing,” adornment, jewel: scHmMuCK; c. Old Norse mugga, driz- zle, akin to the source of Middle English muggen, to drizzle: MuGGY; d. Low German smukkelen, smuggeln, to smuggle (< “to slip contraband through”): SMUGGLE; e. Middle Low German smucken, to adorn (< “to make sleek”): SMUG; f. Old Norse mygla, mold, mildew, akin to the source of Middle English molde, mold: MOLD®. 3. Ger- manic *meuk- in Old Norse mjikr, soft: MEEK. 4. Variant form *meuk- in Latin miicus, mucus: MOIST, MUCILAGE, MUCO-, MUCUS, (MUSTY). 5. Zero-grade variant form *muk- in: a. Greek mukés, fungus, mushroom: -MYCETE, MYCO-; STREPTOMYCES, (STREPTOMYCIN); b. suffixed form *muk-so- in Greek muxa, mucus, lamp wick (< “nozzle of a lamp” < “nostril”): MATCH2, Myxo-. [Pok. 2. meug- 744.] mezg-'. To dip, plunge. 1. Latin mergere, to dip, dive: MERGE; EMERGE, IMMERSE, SUBMERGE. 2. Latin mergus, diver (water bird): MERGANSER. [Pok. 1. mezg- 745.] mezg-*. To knit. Germanic “mésk- in Middle Dutch a maesche, knitted fabric: MESH. [Pok. 2. mezg- 746. [mimos. A mime. Greek noun of unknown origin. MIME, MIMESIS, MIMIC.] [miser. Wretched, unfortunate. Latin adjective of un- known origin. MISER, MISERABLE, MISERY; COMMISER- ATE.]
963:smeug-. To smoke; smoke. Germanic *smuk- in Old English smoca, smoke: SMOKE. [Pok. (s)meukh-, (s)meug-, (s)meugh- 971.]
1454:ELUANT leu(@)- ELUCIDATE leuk- ELUDE leid- ELUTE leu(a)- ELUVIUM leu(a)- ELYTRON wel-3 EMACIATE mak- EMANATE ma-3 EMANCIPATE man-2 EMASCULATE mas EMBASSAGE ag- EMBASSY ag- EMBELLISH deu-2 EMBER eUS- EMBER DAY ambhi, rei-3 EMBLEM gWele-1 EMBLEMENTS bhel-3 EMBOUCHURE beu-! EMBRACE mregh-u- EMBROCATE mergh- EMEND mend- EMERGE mezg-! EMERITUS (s)mer-2 EMESIS weme- EMETIC weme- EMIGRATE mei-! EMINENT men-2 EMIT (s)meit(9)- EMMET mai-1 EMOLLIENT mel-1 EMOTION meue- EMPEROR pere-! EMPHASIS bha-' EMPHYSEMA pu-! EMPIRIC per-4 EMPLOY plek- EMPORIUM per-2 EMPRISE ghend- EMPTY med- EMPYEMA pu-2 EMPYREAL pil- EMULSION melg- EMUNCTORY meug-2 EN-! en
1757:LITHE lento- LITHOTRITY dhreu- LITIGATE ag- LITMUS meu-, wel-1 LITOTES lei- LITTER legh- LITTLE leud- LITTORAL [éi- LITURGY werg- LIVE! leip- LIVELIHOOD leit-2 LIVELONG leubh- LIVELY leip- LIVER! leip- LIVERWURST wers-! LIVERY leudh-? LIVID — sfi-
1829:MATCH2 meug-2 MATE! mad- MATELOTE neud- MATER miater- MATERIAL miater- MATERNAL miater- MATERNITY méater- MATHEMATICAL mendh-1 MATHEMATICS mendh-! MATINEE méa-1 MATINS ma-1 MATRICLINOUS  klel- MATRICULATE miter- MATRIMONY miater- MATRIX miater- MATRON miater- MATTER méater- MATTOCK mat- MATURE ma-1 MATUTINAL ma-1 MAUL mele- MAULSTICK mel-2 MAUVE malakhé MAW mak-2
1842:MEEK meug-2 MEERSCHAUM mori-, (s)keu- MEET! mdéd-
1875:MIR mei-4 MIRACLE smei- MIRAGE smei- MIRE meu- MIRROR smei- MIRTH mregh-u- MIs-1_ mei-1, mei-2 MISADVENTURE gWa- MISANTHROPE ner-2 MISCEGENATION gene-, meik- MISCELLANEOUS meik- MISCHIEF kaput MISCIBLE meik- MISCREANT kerd-1 MISER miser MISERABLE miser MISERICORD kerd-1 MISERY miser MISFEASANCE dhé-1 MISHAP kob- MISNOMER nd-men- MISONEISM newo- MISPRISION ghend-, mei-1 MIss! mei-1 MISSEL THRUSH meigh- MISSILE (s)meit(9)- MISSION (s)meit(a)- MISSIVE (s)meit(e)- MIST meigh- MISTAKE mei-1 MISTER meg- MISTLETOE meigh- MISTRAL meg- MISTRESS meg- MITE! = mai-1
1880:MOIST meug-2 MOLAR? mela- MOLASSES melit- MOLD! med- MOLD2 meug-2 MOLD? mela- MOLDER mele-, mai-2 MOLE! mai-2 MOLE? mo-
1882:MOLTO mel-4 MOLY md6(u)lo- MOLYBDENUM plumbum MOMENT meue- MOMENTOUS meue- MOMENTUM meue- MONAD men-4 MONANTHOUS = andh- MONASTERY men-4 MONAXON aks- MonpDay mé-2 MONEY men-! MONGER meng- MONGREL mag- MONILIFORM mon- MONISH men-1 MONITION men-1 MONITOR men-1 MONK men-4 MONO- men-4 MONOCLE oOkw- MONOCLINIC klei- MONOCLINOUS klei- MONOCOQUE kokkos MONODY wed-2 MONOECIOUS weik-! MONOMER (s)mer-2 MOoNOPHYSITE bheue- MONOPODIUM ped-1 MONOPOLY pel-5 MONOTREME tere-1 MONS men-2 MONSTER men-1 MONTAGNARD men-2 MONTANE men-2 MONTE men-2 MONTH mé-2 MONTICULE men-2 MONUMENT men-! MOOCH meug-! MOOD! mé-1 MOOD? med- MOON mé-2
1892:MORTUARY mer-2 MORT! mer-2 MORULA moro- MOSAIC men-1 MOSQUITO = mu-2 MOss meu- MOssO meue- MOST mé-3
1895:MOTE? med- MOTH math- MOTHER! miter- MOTIF meue- MOTION meue- MOTIVE meue- MOTOR meue- MOTTO mul- MOUILLE mel-1 MOULAGE med- MOULIN mele- MOUNT! men-2 MOUNT? men-2 MOUNTAIN men-2 MOURN (s)mer-1 MOUSE mius- MOUTH men-2 MOVE meue- MOVEMENT meue- mow! mik- Mow? mé-4 MUCH meg- MUCILAGE meug-2 MUCO- meug-2 MUCUS meug-2 MUGGY meug-2 MULBERRY moro- MULCH mel-1 MULE? mel-2 MULEY mai-1 MULL? mele- MULLET mel-2 MULLION medhyo- MULTI- mel-4 MULTIFARIOUS dhé-1 MULTIPLE pel-3 MULTIPLEX plek- MULTITUDE mel-4 MUM! mul- MUM2 mul- MUMPS mul- MUNDANE mundus
1897:MUNIFICENT mei-1 MUNITION mei-3 MURAL mel-3 MURAMIC ACID mei-3 MURDER mer-2 MURE mei-3 MURINE mis- MURK mer-1 MURMUR mormor- MURRAIN mer-2 MURREY moro- Musca mu-2 MUSCARINE mu-2 MUSCLE miis- MUSE misum Muse men-1 MUSEUM men-! MUSH2 mu-2 MUSIC men-1! MUSKET mu-2 MusT! med- MUSTS ~=meu- MUSTACHE mendh-2
1898:MUSTARD meu- MUSTELINE mis- MUSTER men-! MUSTY meug-2 MUTATE mei-1 MUTCHKIN med- MUTE mul- MUTILATE mut- MUTTER mul- MUTTON mel-1 MUTUAL mei-1 MUZHIK man-1 MUZZLE musum MY me-1 MYCELIUM walso- -MYCETE meug-2 MYCO- meug-2 MYCORRHIZA wrad- MYELO- mis- MYIASIS § mu-2 MYLONITE mele- MYNA mad- MYNHEER me-1 MYO- mis- MYOCARDIUM kerd-1 MYOPIA mut-, okw- MYOSOTIS miis-, ous- MYRIAD meu- MYRMECO- morwi- MYROBALAN gWel@-2 MYSELF me-! MYSOPHILIA meu- MYSOPHOBIA meu- MYSTAGOGUE ag- MYSTERY! mut- MYSTERY? mei-2 MYSTIC mul- MYSTICETE miis- MYTHOPOEIC kWeij-2 MYXO- meug-2
2146:QUA kWo- QUACKSALVER gWébh-2, selp- QUADRANT kWetwer- QUADRATE kWetwer- QUADRENNIUM at- QUADRI- kWetwer- QUADRILLE! kWetwer- QUADRILLE? kwetwer- QUADROON kWetwer- QUADRUMANOUS man-2 QUADRUPLE pel-3 QUAESTOR quaerere QUAGMIRE meu- QUAINT gnd- QUALIFY dhé-1 QUALITY kWo- QUANTITY k¥o- QUARANTINE kWetwer- QUARREL! kwes- QUARREL2 kwetwer- QUARRY! kerd-1 QUARRY? kwetwer- QUART kWetwer- QUARTAN kwetwer- QUARTER kWetwer- QUARTO kWetwer- QUARTZ twer-2 QUASH kes-2
2225:SCHISM skei- SCHIST skei- SCHIZO-  skei- SCHIZONT es- SCHLEP |leij- SCHLIEREN sleu- SCHLOCK | slak- SCHMALTZ mel-1 SCHMEER (s)mer-3 SCHMUCK meug-2 SCHNAUZER snu- SCHNITZEL sneit- SCHNORRER sner- SCHNOZZLE snu- SCHOLAR segh- SCHOLASTIC segh- SCHOLIUM segh- SCHOOL! segh- SCHOOL? §skel-1 SCHUss skeud- SCIENCE skei- SCILICET skei- SCINTILLA skeei- SCINTILLATE skeei- SCIOLISM skei- SCION géi-1 SCIRE FACIAS dhé-1, skei- SCISSION  skei- SCISSORS kae-id- SCLERA skele- SCLERO- skele- SCLEROMA §skela- SCLEROSIS skela- SCLEROTIC skelo- SCLEROTIUM skela- SCLEROTIZATION skela- SCLEROUS skelo- SCOFF skeubh- SCOLD sekw-3 SCOLEX skel-3 SCOLIOSIS skel-3 SCONCE? dhé-1 SCONE keu-! SCOOP skep- Scop skeubh- -SCOPE spek- -SCOPY spek- SCORCH skerbh- SCORE sker-1 SCORIA_ sker-4 scoT skeud- SCOT AND LOT skeud- SCOTOMA  skot- SCOUR! cira SCOUR2 kéwero- SCOURGE reig-1 SCOUT! ous- scouT? skeud- SCRABBLE  sker-! SCRAG gWere-4 SCRAP!  sker-1 SCRAPE sker-1 SCRATCH grat- SCREAK ker-2 SCREAM ker-2 SCREECH ker-2 SCREED skreu- SCREEN sker-1 SCREW sker-! SCRIBBLE skribh- SCRIBE skribh- SCRIMP_ skerbh- SCRIPT skribh- SCRIPTORIUM skribh- ScRIPTURE  skribh- SCROBICULATE sker-1 SCROD skreu- SCROFULA  sker-1 SCROLL skreu- SCROTUM skreu- SCRUB!  sker-1 SCRUTINY skreu- SCUDO skei- SCUFF skeubh- SCUFFLE! skeubh- SCUFFLE? skeubh- SCULPTURE skel-1 SCUM (s)keu- SCUTCH kwét- SCUTTLE! skeud- SCUTUM  skei- SCYPHISTOMA skep-, ste-men- SCYPHOZOAN skep- SCYTHE sek- SEAL! sekw-1 SEAL? selk- SEAM syi- SEANCE sed-! SEAR! saus-
2271:SLOE slii- SLOGAN gar-, sloug- SLOOP sleubh- SLOP! sleubh- sLop2  sleubh- SLUG? sleu- SLUGGARD §sleu- SLUMBER sleu- SLUMGULLION leb-1 SLUMP leb-1 SLURP srebh- SLUSH sleu- SLY slak- SMACK! smeg- SMACK? smeg- SMALL mélo- SMALT mel-1 SMART smerd- SMEAR (s)mer-3 SMEARCASE (s)mer-3 SMELT! mel-1 SMELT2 mel-1 SMILE smei- SMIRK smei- SMITE smé- SMITH smi- SMITHY smi- SMOCK meug-2 SMOKE smeug- SMORGASBORD _ bherdh- SMUG meug-2 SMUGGLE meug-2 SNAIL sneg- SNAKE sneg- SNAP snu- SNARE! (s)ner- SNARE? (s)ner- SNARL!  sner- SNATCH snu- SNEER sner- SNEEZE pneu-
2319:STOVE! staup- sTow sta- STRABISMUS streb(h)- STRABOTOMY streb(h)- STRAIN! | streig- STRAIN?  ster-2 STRAIT  streig- STRANGE eghs STRANGLE strenk- STRANGLEs  strenk- STRANGULATE _ strenk- STRANGURY strenk- STRATAGEM ag-, ster-2 STRATH ster-2 STRATOCRACY  ster-2 STRATUS  ster-2 STRAW ster-2 STREAK streig- STREAM sreu- STREET  ster-2 STRENGTH  strenk- STREPTO-  streb(h)- STREPTOMYCES meug-2 STREPTOMYCIN meug-2 STREPTOTHRICIN  thrix STREUSEL ster-2 STREW ster-2
```


## [2026-09-07T17:37:22.356Z] TOOL CALL #14: Bash

```json
{
 "command": "pdftoppm -f 338 -l 338 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg338 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/",
 "description": "Render PDF page 338"
}
```


### [2026-09-07T17:37:23.960Z] TOOL RESULT

```
total 17660
drwx------ 2 sfmqrb sfmqrb     4096 Sep  7 13:37 .
drwx------ 4 sfmqrb sfmqrb     4096 Sep  7 11:48 ..
-rw-rw-r-- 1 sfmqrb sfmqrb     8635 Sep  7 12:07 318-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   101267 Sep  7 12:07 318-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61586 Sep  7 12:18 320-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   115970 Sep  7 12:18 320hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    86272 Sep  7 12:18 320-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    13284 Sep  7 12:18 320-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   107524 Sep  7 12:27 328-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    43713 Sep  7 12:35 331-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   135301 Sep  7 12:35 331-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    52382 Sep  7 12:41 333-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    88345 Sep  7 12:41 333-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    68568 Sep  7 12:43 335-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   105946 Sep  7 12:43 335-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb      725 Sep  7 13:36 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    14937 Sep  7 11:56 arrows.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1413 Sep  7 12:27 box1b.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1385 Sep  7 12:27 box1.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1132 Sep  7 12:27 box2b.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1988 Sep  7 12:27 box2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    85949 Sep  7 11:57 bqt2002_a.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72256 Sep  7 11:58 bqt2002_f1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   161214 Sep  7 11:57 bqt2002_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63319 Sep  7 12:40 build333.py
-rw-rw-r-- 1 sfmqrb sfmqrb    83643 Sep  7 12:12 build.py
-rw-rw-r-- 1 sfmqrb sfmqrb     7075 Sep  7 12:13 c331_av1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10759 Sep  7 12:13 c331_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3537 Sep  7 11:53 c_migare2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1829 Sep  7 11:53 c_migare3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2261 Sep  7 11:53 c_migare4.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3958 Sep  7 11:53 c_migare.png
-rw-rw-r-- 1 sfmqrb sfmqrb    19652 Sep  7 11:53 c_semita2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2639 Sep  7 11:53 c_semita.png
-rw-rw-r-- 1 sfmqrb sfmqrb    40259 Sep  7 11:50 ferdowsi2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30950 Sep  7 11:51 ferdowsi3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    28946 Sep  7 11:51 ferdowsi4.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4298 Sep  7 11:50 ferdowsi.png
-rw-rw-r-- 1 sfmqrb sfmqrb     9383 Sep  7 11:55 masjid.wiki
-rw-rw-r-- 1 sfmqrb sfmqrb    33701 Sep  7 12:04 mk319a.py
-rw-rw-r-- 1 sfmqrb sfmqrb    46151 Sep  7 12:09 mk319b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    51516 Sep  7 12:09 mk322.py
-rw-rw-r-- 1 sfmqrb sfmqrb    61981 Sep  7 12:06 mk323.py
-rw-rw-r-- 1 sfmqrb sfmqrb    63978 Sep  7 12:35 mk330.py
-rw-rw-r-- 1 sfmqrb sfmqrb    64100 Sep  7 12:34 mk331.py
-rw-rw-r-- 1 sfmqrb sfmqrb    90456 Sep  7 12:42 mk332.py
-rw-rw-r-- 1 sfmqrb sfmqrb    99976 Sep  7 12:34 mk334.py
-rw-rw-r-- 1 sfmqrb sfmqrb    57252 Sep  7 12:38 mk337.py
-rw-rw-r-- 1 sfmqrb sfmqrb    37635 Sep  7 12:04 part_a.json
-rw-rw-r-- 1 sfmqrb sfmqrb    58545 Sep  7 12:09 part_b.json
-rw-rw-r-- 1 sfmqrb sfmqrb    97817 Sep  7 11:50 pg318hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    62558 Sep  7 11:50 pg318.png
-rw-rw-r-- 1 sfmqrb sfmqrb    67293 Sep  7 11:54 pg319.png
-rw-rw-r-- 1 sfmqrb sfmqrb   146848 Sep  7 12:01 pg320hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    80891 Sep  7 12:00 pg320.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71522 Sep  7 12:00 pg321.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72193 Sep  7 11:57 pg323.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65279 Sep  7 11:49 pg324.png
-rw-rw-r-- 1 sfmqrb sfmqrb    55902 Sep  7 11:58 pg326.png
-rw-rw-r-- 1 sfmqrb sfmqrb   163982 Sep  7 11:53 pg327hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    73619 Sep  7 11:52 pg327.png
-rw-rw-r-- 1 sfmqrb sfmqrb    69765 Sep  7 12:12 pg329.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72757 Sep  7 12:13 pg330.png
-rw-rw-r-- 1 sfmqrb sfmqrb   128240 Sep  7 12:13 pg331hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    94945 Sep  7 12:12 pg331.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75312 Sep  7 12:17 pg332.png
-rw-rw-r-- 1 sfmqrb sfmqrb   104609 Sep  7 12:27 pg333hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70886 Sep  7 12:26 pg333.png
-rw-rw-r-- 1 sfmqrb sfmqrb    41782 Sep  7 12:18 pg334_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    97297 Sep  7 12:18 pg334.png
-rw-rw-r-- 1 sfmqrb sfmqrb    58407 Sep  7 12:18 pg334_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    88659 Sep  7 12:22 pg335.png
-rw-rw-r-- 1 sfmqrb sfmqrb    57846 Sep  7 12:31 pg336.png
-rw-rw-r-- 1 sfmqrb sfmqrb    60414 Sep  7 12:19 pg337.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65267 Sep  7 13:37 pg338.png
-rw-rw-r-- 1 sfmqrb sfmqrb        0 Sep  7 13:36 queue.txt
-rw-rw-r-- 1 sfmqrb sfmqrb       49 Sep  7 12:17 sns53.png
-rw-rw-r-- 1 sfmqrb sfmqrb    35039 Sep  7 12:17 sns_n53.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    35039 Sep  7 12:17 sns_n54.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  1021826 Sep  7 12:18 sns_p54.png
-rw-rw-r-- 1 sfmqrb sfmqrb 12288786 Sep  7 12:18 sns_text.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb     1308 Sep  7 11:54 v2001.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    27253 Sep  7 12:02 z_maqd2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63140 Sep  7 12:02 z_maqd3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4293 Sep  7 12:01 z_maqd.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2895 Sep  7 12:01 z_meh.png
-rw-rw-r-- 1 sfmqrb sfmqrb    25378 Sep  7 12:01 z_mezna2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    33685 Sep  7 12:01 z_mezna.png
```


## [2026-09-07T17:37:32.671Z] TOOL CALL #15: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg338.png"
}
```


### [2026-09-07T17:37:33.057Z] TOOL RESULT

```

```


## [2026-09-07T17:37:33.052Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-07T17:37:49.615Z] TOOL CALL #16: Bash

```json
{
 "command": "mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg338.png data/verification/sources/refs/ocr/BOOK/338.png && ls -la data/verification/sources/refs/ocr/BOOK/ | tail -3",
 "description": "Copy page PNG to audit location"
}
```


### [2026-09-07T17:37:49.689Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r--  1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r--  1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
```


## [2026-09-07T17:37:50.494Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN leaf 306 (p.285) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==307' HRN.txt | head -60",
 "description": "Read Horn page 285"
}
```


### [2026-09-07T17:37:51.667Z] TOOL RESULT

```
=== HRN leaf 306 (p.285) ===
— 285 —
138. mTitrlh^) 'Urin' (ZI'Gl.), mat (P.-Vend.).
aw. müS^ra-; ai. mätra- 'Urin'.
N.
139. näl {nak?) 'Nase, nur vd. 8 (46), 9 (158).
ap. näh'^) 'Nase' ; aw. naonliau', tiäonhä- ; ai. ndsä-.
Das alte Wort ist schon im Fehle vT aufgegeben,
doch verstand es der Conimentator wohl noch, da er
es nicht erklärt.
140. näirlk Trau, nCiirtklh 'Ehe' (aw. miiruiirana'),
aw. näirika- Trau'; ai. vergl. mir!-.
141. nmnriSflk namentlich, mit Namen*.
aw. *fiqmö.cistika-^) etwa 'mit Beachtung des
Namens*, ai. ^nämacittika^.
142. naslh^) *Leichnam, Aas*.
aw. vam- 'Leichnam, Aas'.
np. nesa, visä kommt nur in Pnrsenschriften vor
(Citate aus Behräm Zerätust).
148. nastnttan Vernichten* (Aw.-Komm., auch in Glossen).
aw. [/lias-, nasyfiti Verschwinden', Causat. ver-
schwinden machen'; ai. [/nag-, ndryati 'verschwinden,
verderben'; lat. necäre, gr. r/xiv.
Hierher wird np. nüslden 'abmagern' gehören (oben
No. 1018), vergl. auch np. fernüs (oben No. 822).
144. nemak 'Gegend'.
aw. na^ma- 'Gegend*.
Im Np. nur in der Bedeutung 'halb' erhalten (vgl.
oben No. 1069).
145. nttan 'führen, treiben* (Men.), näymlüm (vd. 8 (42),
19 (94) für aw. V^vad- 'führen') •).
^) Oder 80 ähnlich; mütrast ist unmöglich.
») Bartholomae, BB. XV, 38.
•) Wechsel von st und st wie öfter.
*) Nasäi; vergl. oben No. 547 zu phlv. dräjlh.
*) Auch vd. 14 (66) pri väirlJäh näyineL
'•■\ »
```


## [2026-09-07T17:37:57.117Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for L in 514 515 516 517 518; do echo \"--- leaf $L ---\"; awk -v n=$((L+1)) 'BEGIN{RS=\"\\f\"} NR==n' KLN_1966.txt | head -4; done",
 "description": "Locate Klein page 1008"
}
```


### [2026-09-07T17:37:58.372Z] TOOL RESULT

```
--- leaf 514 ---
at’  (in  physics  it  is  used  in  the meaning  of  ‘a  million  times’,  e.g.  megavolt  —  a million  volts).  —  Fr.  Gk.  pEyap,  fem.  psyiXv], neut.  peyx,  ‘great,  large,  mighty’,  which  is  cogn. with  L.  magnus,  ‘great,  large,  much,  abundant’, Goth,  mikils,  OE.  micel,  mycel,  ‘great,  big, many’.  See  mickle  and  cp.  magnum.  Cp.  also omega,  acromegaly,  almagest,  Agastache. megacephalic,  megacephalous,  adj.,  large-headed.
—  Compounded  of  mega-  and  Gk.  xeqpaXir), ‘head’.  See  cephalic,  resp.  cephalous.
Megaceros,  n.,  a  genus  of  mammals  of  the  deer family  (zool.)  —  ModL.,  compounded  of  mega- and  Gk.  x£pa?,  ‘horn’.  See  cerato-.
Megachile,  n.,  a  genus  of  bees  (zool.)  —  ModL., compounded  of  mega-  and  Gk.  ypThoc,,  ‘lip’. See  chilo-.
--- leaf 515 ---
elden,  ‘to  announce’,  fr. MHG.  melden,  ‘to  betray,  report’,  fr.  OHG. meldon,  of  s.m.,  which  is  rel.  to  OS.  meldon,  of s.m.,  OE.  meldian,  ‘to  declare,  tell,  display,  pro¬ claim',  OE.  meld,  ‘proclamation*,  Du.  melden, ‘to  report;  to  mention’,  and  perhaps  cogn.  with Lith.  meldiiu,  melsti,  ‘to  request,  pray'.  Arm. malt'em.  T  beg,  request’,  Hitt,  maid-,  ‘to  tell, pray’.
Derivative:  meld,  n.,  the  act  of  melding, meld,  tr.  and  intr.  v.,  to  blend.  —  A  blend  of melt  and  weld.
meldometer,  n.,  an  instrument  for  measuring melting  poinis.  —  Compounded  of  Gk.  |xeXoei.v, ‘to  melt",  and  fr£rpov,  ‘measure’.  See  meal, ‘edible  grain',  and  meter,  ‘poetical  rhythm’. Meleagris,  n.,  the  genus  of  turkeys  (ornithol.)  — ModL.,  fr.  L.  meleagris,  ‘guinea  hen’,  fr.  Gk. peXeaypii;,  which  is  of  uncertain  origin.  It  is perh.  cogn.  with  Avestic  mlr*ga,  ‘bird’,  Afghan
marya,  of  s.m.  The  Greek  word  was  prob.  in¬ fluenced  in  form  by  the  name  of  the  Greek  hero MsX£aYpoc,  Meleagrus,  son  of  Oeneus,  king  of Calydon.
--- leaf 516 ---
er,  meninx. Derivatives:  member-ed,  adj.,  member-less,  adj., member-ship,  n.
membranaceous,  adj.,  membranous.  — -  Late  L. membranaceus,  fr.  L.  membrana.  See  next  word and  -aceous.
membrane,  n.  — -  L.  membrana,  ‘fine  skin,  mem¬ brane,  parchment’,  fr.  membrum ;  see  member. The  orig.  meaning  of  L.  membrana  was  ‘that which  covers  the  members  (or  a  member)  of  the body’.
membranous,  adj.  —  F.  membraneux  (fem.  mem- braneuse),  fr.  membrane,  fr.  L.  membrana.  See prec.  word  and  -ous.
--- leaf 517 ---
alendar  of  the  months.  —  ModL. menologium,  fr.  Late  Gk.  pirjvoXoytov,  which  is compounded  of  Gk.  pvjv,  gen.  \irpoq,  ‘month’, and  Xoyoc,  ‘word,  speech,  discourse,  account’. See  meno-,  ‘month’,  and  -logy.
menopause,  n.,  period  of  life  during  which  men¬ struation  ceases.  —  Compounded  of  meno-, ‘month’,  and  Gk.  raocm;,  ‘a  stopping,  ceasing’, fr.  rcadsiv,  ‘to  cause  to  cease’.  See  pause. Derivative:  menopaus-al,  adj.
Menorah,  n.,  the  seven-branched  candelabrum  in the  Tabernacle  and  in  the  Temple  of  Jerusalem.
—  Heb.  mlnorah,  ‘candlestick’,  from  stem  n-w-r, ‘to  give  light,  shine’,  whence  also  ner,  ‘lamp’ ;  rel. to  Aram. -Syr.  nur,  ‘fire’,  Arab,  nara,  ‘shone’, nur,  ‘light’,  nar,  ‘fire’,  Aram,  mfnarta,  ‘candle¬ stick’,  Arab.  manarah,  ‘candlestick;  lighthouse; tower  of  a  mosque’,  Akkad,  nuru,  ‘light’,  nawa- ru,  namaru,  ‘to  give  light,  shine".  Cp.  the  second element  in  Abner.  Cp.  also  minaret  and  the  last element  in  Koh-i-noor.
--- leaf 518 ---
  subst. suff.  -ise.
Derivative:  merchandise,  intr.  and  tr.  v. merchant,  n.  —  ME.,  fr.  OF.  marcheant  (later mar  chant,  marchand,  F.  marchand),  fr.  VL.
*  mercatantem,  acc.  of  *mercatans,  pres.  part,  of *mercatare  (whence  OProveng.  mercadar,  ‘to trade’),  fr.  L.  mercatus,  ‘trade,  place  for  trade, market  place’,  fr.  mercari.  See  mercantile  and -ant.  It.  mercatante,  Sp.  mercadante,  ‘merchant’, also  derive  fr.  VL.  *  mercatantem.
Derivative:  merchant-ry,  n. merchant,  intr.  and  tr.  v.  —  ME.  marchaunden,  fr. OF.  marcheander  (F.  marchander),  fr.  mar¬ cheant.  See  merchant,  n.
```


## [2026-09-07T17:37:59.048Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT muthra ===\"; grep -n \"mū̆θra\\|muthra\\|mū́θra\\|mūθra\" BRT.txt | head -20; echo \"=== BRT fra-muxti / muxti ===\"; grep -n \"muxti\\|frā.muxti\\|fra-muxti\" BRT.txt | head -20",
 "description": "Grep Bartholomae"
}
```


### [2026-09-07T17:37:59.158Z] TOOL RESULT

```
=== BRT muthra ===
=== BRT fra-muxti / muxti ===
2945:•  j.  aoSra-  n.  'Schuhwerk,  Schuhzeug': *zannya  °ärii(IS.)  *paiti,smuxia  yä  vupö.- pTsa  bamya  "mit  goldenem  Schuhzeug  an- getan, mit  reichverziertem,  glänzendem" Yt5.78;  64;  —  mal  '%ranqm  framuxti . .  upa.mqnaytn  "mit  Ablegung  ihres  Schuh- zeugs  sollen  sie  . ."  V.  ö.  27,
```


## [2026-09-07T17:38:12.216Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in \"^mud,\" \"^moss,\" \"^must,\" \"^mustard,\" \"^moist,\" \"^mucus,\" \"^match,\" \"^smuggle,\" \"^smug,\"; do echo \"=== $w ===\"; grep -n \"$w\" KLN_1966.txt | head -3; done",
 "description": "Grep Klein headwords"
}
```


### [2026-09-07T17:38:13.520Z] TOOL RESULT

```
=== ^mud, ===
24571:mud,  n.,  wet  earth.  —  ME.  mode,  mudde,  of  LG. origin.  Cp.  OLG.,  MLG.  mudde,  ‘mud’,  muddig, ‘muddy’,  vvhich  derive  fr.  I.-E.  base  *meu-,  ‘wet, moist’,  whence  also  MDu.,  Du.  modder,  ‘filth, dregs’.  See  mother,  ‘dregs’,  and  cp.  words  there referred  to.
=== ^moss, ===
24480:moss,  n.  —  ME.  mos,  fr.  OE.  mos,  ‘marsh,  moor  , rel.  to  OE.  meos,  ‘moss’,  ON.  mosi,  Dan.  mos, ‘moss’,  Swed.  mossa,  ‘moss’,  mosse,  ‘moor’, MDu.  mosse,  Du.  mos,  ‘moss',  OHG.,  MHG. mos,  ‘moss,  swamp,  moor’,  OHG.  mios,  MHG. mies,  ‘moss’,  G.  Moos,  ‘moss’,  ON.  myrr,  ‘bog, swamp’,  fr.  I.-E ,*meu-s-,  whence  also  L.  museus, ‘moss’,  Lith.  miisaX,  ‘mold,  mildew’,  OSlav. mucha,  ‘moss’  and  perh.  L.  mustus,  ‘fresh,  new’ (if  fr.  *mus-tos,  ‘wet,  moist’),  whence  mustum (short  for  mustum  vinum),  ‘new  wine’.  F.  mousse, ‘moss’,  is  a  Teut.  loan  word.  I.-E.  *meu-s-  is  an -s-enlargement  of  base  *meu-,  ‘moist;  marsh; moss’.  Cp.  mire,  muscoid,  muscology,  mushroom, must,  ‘new  wine’,  mustard.  For  derivatives  of base  *meu-d-,  a  -(/-enlargement  of  base  *meu-, see  mother,  ‘dregs’,  and  cp.  words  there  referred to.
=== ^must, ===
24753:must,  aux.  v.,  am  (or  is,  are)  obliged  to.  —  ME. moste,  fr.  OE.  moste,  pret.  of  motan,  ‘to  be allowed  to,  be  able  to,  have  opportunity  to, have  to’,  rel.  to  OS.  motan,  ‘to  be  obliged  to, have  to’,  OFris.  mdta,  MLG.  moten,  MDu.,  Du. moeten,  ‘to  be  obliged  to’, OHG.  muo^an,  MHG. mue^en,  ‘to  be  allowed  to,  have  to’,  G.  miissen,
24755:must,  n.,  mold,  mustiness.  —  Prob.  back  forma¬ tion  fr.  musty.
24756:must,  adj.,  frenzied,  mad  (said  of  male  elephants).
=== ^mustard, ===
24761:mustard,  n.  —  MF..,  fr.  OF.  moustarde  (F.  mou- tarde),  fr.  moust  (F.  mout),  ‘new  wine,  must’,  fr. L.  mustum.  Accordingly  mustard  lit.  means ‘seasoned  with  must’.  See  must,  ‘new  wine’,  and cp.  -ard.
=== ^moist, ===
24172:moist,  adj.  —  ME.  moiste,  ‘fresh  (of  fruit,  wine, etc.)’,  fr.  MF.  moiste  (F.  moite),  ‘moist’,  fr.  VL. *muscidus,  which  is  a  blend  of  L.  mucidus,  ‘mo¬ lly,  musty’,  and  musteus,  ‘of  new  wine,  fresh, juicy'.  L.  mucidus  is  a  derivative  of  mucus;  see mucus  and  cp.  must,  ‘mold’.  L.  musteus  derives fr.  mustum,  'must,  new  wine’;  see  must,  ‘new wine’.
=== ^mucus, ===
24569:mucus,  n.,  a  viscid  secretion  of  the  mucous  mem¬ branes.  —  L.  mucus,  ‘mucus  of  the  nose’,  rel.  to mucor,  ‘mold,  moldiness’,  mungere,  emungere, ‘to  blow  the  nose’,  fr.  I.-E.  base  *(s)meuq-, *(s)meug-,  ‘to  slip;  slippery,  slime’,  whence  also OI.  muhedti,  mucati,  ‘he  releases’,  Gk.  jxu^a, ‘mucus  of  the  nose,  slime’,  ‘mullet’,
=== ^match, ===
=== ^smuggle, ===
35692:smuggle,  tr.  and  intr.  v.  —  LG.  smuggeln ,  rel.  to Dan.  smugle,  Norw.  smugla,  Swed.  smuggla, Norw.  smokla,  Du.  smokkelen,  ‘to  smuggle', and  to  OE.  smugan,  ‘to  creep’.  See  smock and  cp.  prec.  word.
=== ^smug, ===
```


## [2026-09-07T17:38:21.832Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ntxt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nlines=txt.split('\\n')\ndef leafof(lineno):\n    s='\\n'.join(lines[:lineno])\n    return s.count('\\f')\nfor ln,label in [(24480,'moss'),(24569,'mucus'),(24571,'mud'),(24753,'must aux'),(24761,'mustard'),(24172,'moist'),(35692,'smuggle')]:\n    lf=leafof(ln)\n    print(label, 'leaf', lf, 'approx printed pages', (lf-12)*2, (lf-12)*2+1)\nEOF",
 "description": "Compute Klein leaf/page for headwords"
}
```


### [2026-09-07T17:38:23.197Z] TOOL RESULT

```
moss leaf 540 approx printed pages 1056 1057
mucus leaf 542 approx printed pages 1060 1061
mud leaf 542 approx printed pages 1060 1061
must aux leaf 545 approx printed pages 1066 1067
mustard leaf 546 approx printed pages 1068 1069
moist leaf 533 approx printed pages 1042 1043
smuggle leaf 776 approx printed pages 1528 1529
```


## [2026-09-07T17:38:38.398Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==517' KLN_1966.txt | head -40; echo \"=== search urine/Avestic mutra ===\"; grep -n \"mutra\\|mǘθra\\|Avestic  mu\\|urine\" KLN_1966.txt | head -20",
 "description": "Inspect Klein leaf 516 and search for mutra"
}
```


### [2026-09-07T17:38:39.652Z] TOOL RESULT

```
<persisted-output>
Output too large (29.3KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/tool-results/bdyrjt41r.txt

Preview (first 2KB):
er,  meninx. Derivatives:  member-ed,  adj.,  member-less,  adj., member-ship,  n.
membranaceous,  adj.,  membranous.  — -  Late  L. membranaceus,  fr.  L.  membrana.  See  next  word and  -aceous.
membrane,  n.  — -  L.  membrana,  ‘fine  skin,  mem¬ brane,  parchment’,  fr.  membrum ;  see  member. The  orig.  meaning  of  L.  membrana  was  ‘that which  covers  the  members  (or  a  member)  of  the body’.
membranous,  adj.  —  F.  membraneux  (fem.  mem- braneuse),  fr.  membrane,  fr.  L.  membrana.  See prec.  word  and  -ous.
membranula,  membranule,  n.,  a  little  membrane. —  L.  membranula,  dimin.  of  membrana.  See membrane  and  -ule.
memento,  n.,  something  serving  as  a  reminder.  — L.  memento,  ‘remember’,  imper.  of  meminisse, ‘to  remember’,  which  is  cogn.  with  Gk.  pipovx, ‘i  am  very  eager,  I  purpose,  intend’,  fr.  I.-E. base  *men-,  ‘to  think,  to  have  one’s  mind  arous¬ ed’,  whence  also  L.  mens,  'mind,  understand¬ ing,  reason",  Goth,  muns,  ‘thought,  mind’,  OE. gemynd,  ‘memory’.  See  mind  and  cp.  words there  referred  to.
Memnon,  n.,  an  Ethiopian  king  slain  by  Achilles in  the  Trojan  war  ( Greek  mythol.)  —  L.  Mem¬ non,  fr.  Gk.  M£pvtov,  a  word  of  uncertain  ety¬
mology.  It  possibly  stands  for  *M68po>v  and  lit. means  ‘ruler’,  fr.  piSrov,  which  is  prop,  the pres.  part,  of  the  ancient  verb  piSeiv,  ‘to  pro¬ tect,  rule  over’,  hence  is  of  the  same  origin  as  the second  element  in  the  name  ’Ayapipvcav.  See Agamemnon.
memo,  n.  —  Short  for  memorandum.
Derivative:  memo,  tr.  v.,  to  make  a  memoran¬ dum  of.
memoir,  n.,  biography,  biographical  notice.  —  F. mdmoire,  orig.  ‘something  written  to  be  kept  in mind’,  masc.,  derived  fr.  mdmoire,  fem.,  ‘mem¬ ory’,  fr.  L.  memoria.  See  memory, memorabilia,  n.  pi.,  things  worth  remembering. —  L.  memorabilia,  neut.  pi.  of  memordbilis.  See next  word.
...
</persisted-output>
```


## [2026-09-07T17:38:56.166Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"leaves: $(awk 'BEGIN{RS=\"\\f\"} END{print NR}' KLN_1966.txt)\"; grep -n \"^la,\\|^mace,\\|^zymurgy\\|^zone,\" KLN_1966.txt | head",
 "description": "Klein file structure"
}
```


### [2026-09-07T17:38:57.373Z] TOOL RESULT

```
leaves: 903
20926:la,  interj.  —  Imitative.  Cp.  the  interjection  law. la,  n.,  a  syllable  used  in  solmization  to  denote  the sixth  tone  of  the  diatonic  scale  ( mus .) laager,  n.,  a  temporary  camp.  —  S.  Afr.  Du.,  rel. to  Du.  leger,  G.  Lager,  ‘camp’.  See  lair  and  cp. lager,  leaguer,  ‘camp’.
22444:mace,  n.,  a  weapon  (hist.);  a  staff.  ME.,
22449:mace,  ‘a  weapon’,  with  agential  suff.  -er. macer,  n.,  a  swindler  (slang).  —  Formed  fr.  mace, ‘to  swindle’,  with  agential  suff.  -er. macerate,  tr.  v.,  to  steep  by  soaking;  to  cause  to waste  away ;  to  torment ;  intr.  v.,  to  waste  away. —  L.  maceratus,  pp.  of  mdcerare,  ‘to  make  soft or  tender’,  fr.  I.-E.  base  *mag-,  *nfg-,  ‘to knead’,  whence  also  Gk.  fzayls>  ‘kneaded  mass, cake’,  (rayeu?,  ‘one  who  kneads,  baker’,  OSlav. maiQ,  mazati,  ‘to  anoint,  smear’,  maslo,  ‘butter, oil’,  masti,  ‘ointment’,  Bret,  meza,  ‘to  knead’, Mir.  maistir,  ‘to  churn’.  From  *mak-,  a  var.  of *mag-,  possibly  derives  Gk.  pdoooj  (if  standing for  *m6q-yo),  ‘I  squeeze,  press  into  a  mold, knead’.  See  make  v.,  and  verbal  suff.  -ate  and  cp. magma,  mazo-,  ‘placenta’.  Cp.  also  mass,  ‘size, quantity’.  —  Cp.  *menq-,  ‘to  knead’,  a  collater¬ al  base,  for  the  derivatives  of  which  sec  mingle. (Gk.  pdaoio  could  also  stand  for  *mnq-yo, hence  be  a  derivative  of  base  *menq-.) Derivatives;  macerat-er,  macerat-or,  n.,  mace¬ ration,  n.
```


## [2026-09-07T17:39:11.524Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"mü9ra\\|mu9ra\\|müSra\\|muSra\\|mü^ra\\|mu\\^ra\\|mtiSra\\|Unreinigkeit\\|Harn\" BRT.txt | head -20",
 "description": "Grep Bartholomae for muthra variants"
}
```


### [2026-09-07T17:39:11.577Z] TOOL RESULT

```
134:fehlt  Harn.  4
19174:•  j,  ni-maraziäta-'*  Adj.  (fem.  °/5-)  --  ?  — , von  der  Cistä:  raeistam  cistam  .  .  Harn Yt.  16.  1.
19489:•  j.  maesma-  m.  'Harn',  als  rituelles j  Reinigungs-  und  als  Heilmittel  verwendet*';
19493:■  j.  maesman-  n.  'Harn',  als  Rcimgungs- und  Heilmittel'':  Ävam  tanüm  pairi.- yaozdat^Ua  gius'mana  apäca  paiti  avd^a
19497:•  j.  *maesinaAima-''  n.  'Schluck  Harn': "  rJ  .  .  ^'mqn  '>  aiamai  (sd.)  P.  g.
20456:1179  "muSra-
20581:ai.  mu/ra-  n.  'Harn'.  —  Pü. :  nmkrdjin,  muht- däi  (geschr.  mn  l  r*).  —  ')  Mit  u  F.  11.
28371:ersten  falschen  Wort  soll  er  drei  Schluck Harn  schlucken  .  ,"  V.g.
29557:AbleiL  aus  hi-apak-  r.,  S  'OO  a.  a.  —  Pii. : Itanssltr.,  mit  der  Erl.:  niisak  'Harn';  vgL  lu
```


## [2026-09-07T17:39:15.177Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n 20450,20460p BRT.txt; echo ...; sed -n 20570,20590p BRT.txt",
 "description": "Read Bartholomae muthra entry"
}
```


### [2026-09-07T17:39:15.240Z] TOOL RESULT

```
KorapE.  —  PFP.  lam  V.  'man-.  —  Pü.:  fti meniln.
•  j.,  g.  'm^Sra-  m.  'Wort,  Ausspruch, Spruch';  1)  im  gAw.  'Wort':  tnä  äs  at vi  drigvatS  'rqs^ä  gBsta  säsnäs(sti.ya  Y. Ji.  18.  a)  sonst  nur  vom  göttlichen Wort:  malfäi/vfs/äis'yäi  tsi  'rA  (als AP.) marynti  Y.  .#J.  14;  —  ni  Aim  mfrqzdyäi (sd.)  ^waAya  'raü  sit^hakyä  Y.44.14; —  ySi  im  v!  noil  thä  Tfm  varpsmtl  (sd.) Y.  45-  3;  —  •''»'  y'"t  AaurvatStS  alahyä am»ntäias{ai[.)Sl  Y.31.6;  —  tlm  asBUii (sd.)  akurö  'rfm  tasat  .  .  gavBi  Y.  2g. 7.  a)  bes.  'Verheissungswort,  -spruch': av3  °ra  yS  rii&pmff  (sd.)  affir/  Aa^  Y. 44. 17;  —  ans  'rS  mazi/tfm  väurSimatdi (sd.)  xra/stra  Y.28.$.  2)  im  jAw.; 'Spruch,  Ausspruch':  f^i^  (Stverz.)  'rym Y.55,33;  usw.;  —  sva. 'Urteil':  vispanqm anu  (ad.)  'nm  Yt5. 93;  —  sva.  'Befehl*''>:
*inaibySi.manhahe  ..y3  paoiryS  sara^uäräi (statt  Gen.)  'r>mca  *gu/ta  säsnhca  Ytij. 95'';  —  gahanqmca  sraohnm  . .  Avarita 'rä  (als  AP.)  äyae  yes'H  Y.3.  4;  4. 1,  Vr. ig.  2;  —  sva.  'Zauberspruch':  'am»mca Vir»%rayfumca  ajrinämi  .  .'  afffm  'mm mä  fradalsaysis  atnyai  /ikre  vH  .  .  Yt. i4-A(>',  4-9;  — /rina  ayanqm  •ranqm  yä vinsyäü  avi.m^riS  Yt  10.  so.  a)  bes. 'götüicher  Spruch':  aityamaram  'ranqm mazist»m  'ranam'"  ..  Yt.j.  5;  —  'ranqm a^a.balsasU  YL^.  6(?).  a)  insbes.  Sing. KctT  di,  oder  mit  ip»nia-  Adj.  'das  heilige Wort',  der  Inbegriff  der  göttlichen  Offen- banmg;  auch  vielfach  als  Gottheit';  I)  kolt' it :  alahepaiti  'nm  V.  4. 43 ;  —  aiwiläitT^äi gravas{sA.)ca  'rahe  V.g.  26;  —  masttm  .. 'raheia  faurvatätim  Y.57.  20;  —  aSa  'r»m ..  mairyatY.j.^^;  Yt./-4(?); — yö  anhat ..'ram  p3r3s3  alava  V,_9,  z; — yS  azrazdäi (sd.)  *'r»m^  !astt  N. 77;  —  vXsptm  °rsm yasamaide  Vr.  13.  i;  V.  20.  3;  —  maynS 'rS  N.  3  **;  —  AaemaAeca  °raheca  alaonaica zara%ustrahe  Y.  8. 1.  a)  beschränkt  auf die  fiinf  (?j2r3s:  atryamansm  isim  . .  yS up»nS  (sd.)  ,  .  zaoxJsuye  tarS  (sd.)  'rfm pania  gäh  ä  G.  1. 6.  H)  mit  sp?nta-  Adj.s> : uH  ahurahe  mazda  yazamaide  dari^räi (sd.)  'rahe  spmtahe  xratüm  .  .  mar»%räi 'rahe  spmfahe  hisvqm  .  .  fravakai  'rahe spmtahe  Yt.7.  z8;  —  ahurahe  masda  .. yeiihe  urva  'rff  sp^tS  Yt.  ij.8i,V.iff.n;
—  iai  hUx/tmf  -rB  sptntsY.ig.  19;  FrW. j).  I ;  —  hat  asti  'rahe  spmtahe  ama^ vastsmtm  ,  .  ?  .  .  ahmäksm  nqtna  .  .  yai amfsanqm  sp^ntanqm  tai  °rahe  spiniahe amavasttmim  YL  /.  1—3;  12.  i;  —  upa  vä 'nm  spmt^m  maraUa  V.4.4S;  —  upa- ratatitn  yqm  asahe  vahillahe  paitiparltJm- (sd,)Äi  °rahe  spmtahe  Yl/o.  33;  —  'rahe spmtahe  aiaonS  varszyanuhahe  dätahe  vi- dalvahe  dätahe  zara'huströis  dar»yayä  upa- yanayä  daEnayä  vaahuyä  mSzdayam5ÜY. /.13;  2.13,  77.5,  YL/AIS,  S.2.39;  —  dätäi hähaJätäi  vTdaevai  .  ,  haoa.ma'^rJi  ,  . upairi^atubyS  (sd.)  gtnptäi  °rai  spmiilt Extr.  /;  2,  3,  4;  —  zarazdättTm  'r-m  spm- t?m  . ,  uii.dan%r3m  daXnqm  mäzdayasnlm ..  vaäiim   'rmt   sp»fil>m  Y.25.  6;  22.  25*;
—  'rB  spmiB  mainy»vTm  druj»m  nUbairillB Yt.ii.$;  i2.2{?),  V.ig.6,  2i.6{?);  —  zqm hiäitiuhmi , .  'ram  sp?nt}m . ,  anayra  raoüa Y.  16.  6;    —    'rahe    sp>ntahe  .  .  damaya
dby  Google
1179  "muSra-
mäsdayasneis  . .  staotanam  yesnyanqm  Vr. 5.  7  j  —  gSuI  .  .  gayehe  .  .  'rahe  spmtake asaonS  vgntyarfuAaAe  Yt.21.3;  —  xara- 'hustnm  .  .  'nm  spnlwt  .  .  g^l  urvätam yazamaide  G.  4-  6  i  —  fravaiayS .  .  yqm^a ahrS  .  .  sraosahe  . ,  mi%raAe  . .  °rtiÄe  spenr tahe  YL/_y,86;  /J.  17;  —  äal  mqm  tum bi/azyöi^  'rö  (alsVok.)  iptnts  ys  aij^arma V.  22.  2 ;  —  ^aiti  ahmSi  avafata  °rö  spmts yH  asjfarmä  V.  22. 6.  a)  *rahe  spfTitahe (näml,  ayars)  heisst  der  39,  Monatstag: 'rahe  spmtahe  alaotüS  v^r»tyar?uhahe  S. /.  29;  vgl.  2.39,  ¥./().  7.  Undeutlich:
yni  'nm  saofyantB  Vr.2.5;  —  yö  nSti 'rat *spmtät  P.45-  [V.J.  44:  lies  mq'^rvm.- spmttm  iaii',  amal.]
KompA.,  %.;  AbleiL  —  VgL  'mqXra-.  —  Zum V.  'man-.  —  ai.  mäntra-  m.  'Spruch'.  —  PB.: mann-  (gelW.)  -  Sü.;  väifJ,  mäntirf,  mSnlkra- väni  -,  CiL  :  den  oder  afasläi  u  wnii;  s.  noch No.  I,  4,  5.  —  t)  ¥i.: /ramätt,  Sü.:  ädtlah. —  ')  An  Y.jr.  18  uigelehnt.  —  S  Hds.  me- S«m ;  s.  P,  7.  —  4)  Der  Text  hat:  afaiiäi H^ön  dät  mafHB  mi^trö,  —  S)  Pü. ;  mätur  spand.
•  j.  'm^Sra-  n.  i)  'Gedanke';  im  Gegensau zu  Wort  und  Werk:  l)m  . .  yazamaide  . . 'raca  vacaca  syao'hnaca  Ny.;.i6.  2)'Be- denken,  Nachdenken  über  — ':  bar>snusia astzhe , .  tnasiiia  *ra  . .  vmsya  , .  urvaitya  . . Aai^yä.v>r3sya..v}ndai%ya  dalnaya  G.2.'j.
...
•  g.  mizda'vant-  Adj.  'mit  dem  (gebühren- den) Lohn  (in  beiderlei  Sinn,  Lohn  tind Strafe)  versehen':  hyat  da  syaokana  'von (APn.)  yäiä  uxiä  akSm  akäi  vanuAlm asim  vanhaov?  "wie  du  den  Taten  ihren Lohn  bestimmtest''  und  den  Worten,  das böse  Los  dem  Bösen,  das  gute  dem  Guten"
Vgl.  milda-  1  aa.    —    Pu.;    kal  däl  ö  kmösH iarän  mizd  u  itia  pa  sax^aii.    —    ')  Wörtl.i . .  die  Taten  lohnversehen  machtest. j.  ar)m  müxli  P.  25:  lies  anm-uxli.
•  j,  inüi«^-  f.  Name  einer  Daevr.  ptn/te "Si  pifitte  kapastis  V.  11. 9.
Pü.!  fehlt.
•  p.  mudräya-  Adj.,  bezeichnet  ein  Volk 'ägyptisch;  Ägypter';  Plur.  und  Sing. (kollekt)  als  Bezeichnung  fUr  Volk  und Land:  imä  dahyävc^  tyä  adam  *adatiiy..
dby  Google
muÖra
'^myastra.barana-
II 90
dahyäv^  tya  manä  patiyaisa" . .  arabäyJ' 'yj"  (NS.)  Bh.j.6;  2.2;  —  kaüa  pärs^ 'yam  agarbäyam  D.  //.  3;  —  pasäva" ka'^büjiye^  'yam  asiyava*  Bh.i.  10;  10;  — pirävtr  nämaf  rauia"  /ya*  °yaiy  danuvatiy D./7.3.
•  j.,  g.  mü'ÖTa-''  n.  'Exkremente,  faeces': '■%r3m  F.  11;  —  aitaKhani  astamca  .  . spämamca  (sd.)  '^ram^' {GV.)  'v.6.j; 29.  a)  sva.  'Unrat,  Unflat':  iadn  apn 'hrym  akyä  *madakya  (sd.)  ^.48. 10.
ai.  mu/ra-  n.  'Harn'.  —  Pü. :  nmkrdjin,  muht- däi  (geschr.  mn  l  r*).  —  ')  Mit  u  F.  11.
•  j.  müra-  Adj.  'stumpf-,  blödsinnig':  mil avä  zag%rä  patti.vlse  yh  .  .frataukannti . . 'räsla  (NP.)  YL  5. 93.
ai.  mürd-  Adj.  —  Vgl.  müraka-.
•  j.  mSraka-  m.  Bezeichnung  i'n^ischer Geschöpfe;  nsit  ahmi  nmäne  *zänaite ä%rava  naä,a  ra^aisti  na^a  västryD fsuyqs  aat  .  .  zayänte  dahaiäla  °kä^a pauru^ariha  varSnä^a  Y.  //.  6  ".
Et.  und  eig,  Bed.?».  —  Pü,:  mülak  kartär; s.  unter  mrüra:  —  ')  Den  drei  aAwrischen Ständen  werden  drei  Klassen  lAjÄ/ischer  Wesen ßcgenüberge stellt.  —  »)  Ob  Ableit.  aus  müra-1
•  j.  mü^-  f.  Name  einer  Pairika*'':  x^viia äzüiti  yazamaide  .  .  äzöis  .  .  hamöistri avaiAha  «ff/  {als  GS.) "'  avaiAha.  pairi- kaysi  paitistqtayaica  .  .  Y.  16.  8.
•)  Neben  jlsay,  dem  Dahia  der  Gier,  elwit als  Hexe  der  Habsucht  od.  dgl.  zu  fa^isen.  Bd. 5.  2,  28.  44  erscheint  duidin  müs  parlk  (so  28) 'die  diebische  P.  MüP,  die  als  dambömand  'mit einem  Schweif  verseben'(s,  ■Eapairikä-\  beieichnet wird,  in  Verbindung  mit  den  Planeten  als  Feind von  Sonn*,  Mond  und  Sternen.
Eig.  Bed.?   Ob'Mausf;  ai.  ™a/- f.,  np,  wi«/;
vgl,  DsT,  ZA.  /.  144.  —  Pü.  r  iransskr.  {viü's
parik;     s.    *>);     Sü.!     muinSmnT    räkfosT,     —
```


## [2026-09-07T17:39:27.453Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"framuxti\\|fra.muxti\\|'muc-'\\|V  'muc\\|muk-\\|maoxta\" BRT.txt | head -20; echo \"=== search 'muc' verb ===\"; grep -n \"muc-\" BRT.txt | head -20",
 "description": "Grep Bartholomae for muc/framuxti"
}
```


### [2026-09-07T17:39:27.529Z] TOOL RESULT

```
2945:•  j.  aoSra-  n.  'Schuhwerk,  Schuhzeug': *zannya  °ärii(IS.)  *paiti,smuxia  yä  vupö.- pTsa  bamya  "mit  goldenem  Schuhzeug  an- getan, mit  reichverziertem,  glänzendem" Yt5.78;  64;  —  mal  '%ranqm  framuxti . .  upa.mqnaytn  "mit  Ablegung  ihres  Schuh- zeugs  sollen  sie  . ."  V.  ö.  27,
=== search 'muc' verb ===
```


## [2026-09-07T17:39:34.445Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"uxti\" BRT.txt | head -30; echo \"=== paiti.smuxta / smuxta ===\"; grep -n \"smuxta\\|smuxti\\|hqm.muxta\\|hqm-muxta\" BRT.txt | head",
 "description": "Grep BRT uxti forms"
}
```


### [2026-09-07T17:39:34.517Z] TOOL RESULT

```
2477:y^  . .  möi  gas'^iä  dazdl  *amaiiklmit  akyä  \  myazdS  . .  äisy.ll  kl  anhe  ava{  mlid^m  A. maä%rilfrö^StY.46.Z\'—yatäröpaurvö^3.(il.;  — yastal  mihdgm  haiuftt? nöit däitX äire  . .  paitiJiaraiti  ahmäi  atars  ä/rJnat  .  .  kä  tsm  ahyä  *maeHis(sA.)  ar»hatY.44. V.1S.26;  YLIJ.51; — y ahmäi  xlnstö  ba-\  i^.  b)  .\Sn.,  f.  mit  Äaca  sva. 'dadurch': vaili  mi^rä  ahmäi  Jasaiti  avaiäke  YLIO.  yezi  mit  spä  ..  maeyevä  . .  pai'jyäite  ahmat 84;  87,  Y.GS.w*;  — yöi  nsil  ahm  main-  haca  irisyät  "sonst  konnte  der  Hund  in  . . yantä  aiibyö  dair?  (sd)  voka  as  manö  Y.  \  geraten,  dadurch  könnte  er  Schaden  neh- 34-&]  9.  2&  10,  45-ii  — yaisqm  ..  mazdä  \iata"  V,/_j.37;  —  ahmat  haca  /«>nj  (sd) ..  vatghö  vai'ja  alsqm  ..  Yt.i6.%; — ^J  sayiJ/A' Nik.  7;  *2; — yesi  tat  paiti  irisjati syao^anä  yä  vacatihä  yä  yasnJ  .  .  ae^qm  '  aiähal  hala  iyae>n!i7ar3za  (sd.)  .  ,  V./_?. töi..}hmä  pourutimäil  äasl?(sd.}Y.j4-^,''  38-  2)  vorausweisend;  i)  adjektivisch ■ —  yöi  *aite  . .  *gä'kä  nSit  *srävayänti  . .  I  auf  direkte  Rede  oder  Zitat:  vahiütsm  . . assqm  fyaohamm\ia'\  .  .  N, 25;  —  ySt  ..'igänii  ..  vir^zyat  öyä  (ISf.)  «>/f  (sd.):  hvö avatahabdgnti  (sd..)  /ramar?nl>m  (sd.)  ag-  *pt3  asahyä  mazdlY.4y.2;~aya  antar?.- £qm  nöit  aita^qm  ratufris  ..  N.52;  ^j\  uxti  (sd.) :  nöit  nS  mana  (usw.,  Y..^5.z) —  yahmät  kakmäicit  nalmaruim  vätS  ä'^rö  Y.ig.i$.  —  a)  mit  ergänzendem  Relativ: baoiolm  vibaraiti  (sd.)  ahmll  kahmäiHt  aya  aibigara  (LS.  als  Instr.)  aya  aibijary- nalmanqm..\.8.&o.  a)  Die  Beziehung  ta{d.^.)  yä  amfsanqm  sp^ntanqm..:  gave ist  ungenau:  ^yJ  räakaytn  (sd.)  sravaahä  rto5j/(usw.,Y._j5.4)  Vr.J2.i.  a)  substan- vahistät  iyadkanäl  mantärü  aeibyö  mazäi  tivisch  und  adjektivisch  auf  eine  erläuternde akä  (sd)  mraot  "qua  alienant  doc-  oder  ergänzende  nominale  Beifügung:  «7.5- trina  . .,  üs  .  ."  (statt  qui  ..  iis  ,  .)  Y.32.  yacä  i^agtuL  yäsat  ahyi  Virßzin3m..ahyä .. 1 2'*^  Anhang  zu  II  I  1,  2.     a)  An   ahurahya  uruasimai^A.)  mazda  Y.j2.i ;  2S.
2769:mit  pairi  1)  'ringsum  absuchen,  auf- lesen': mazdayasna  aitihh  zimß  pairisa- yanta  (Opt.)  . .  varfsqmca  (als  Obj.)  ..yezi nsit  pairiianie  . .  astqmca  7-arpsqm:a  .  . V.  ö.  7f. 's\  z)  'herumsuchen  nach  — , aussuchen,  auslesen':  asstnanqm  xraoldva- nqm  .  .pairlstanqmY.i4.4'i'>;  A.3.5'^; —  uxtiitn  srlr>m  pairisttm  F.^^f'*'; V.J. 42  PüZ,;  —  pairi  daxma  aSlayqn  vi daxma    calsayqn   Y.S.z.  a)    mit    Dat
2945:•  j.  aoSra-  n.  'Schuhwerk,  Schuhzeug': *zannya  °ärii(IS.)  *paiti,smuxia  yä  vupö.- pTsa  bamya  "mit  goldenem  Schuhzeug  an- getan, mit  reichverziertem,  glänzendem" Yt5.78;  64;  —  mal  '%ranqm  framuxti . .  upa.mqnaytn  "mit  Ablegung  ihres  Schuh- zeugs  sollen  sie  . ."  V.  ö.  27,
3844:•  j.  aiwi.druxUm  Absol.  ">  'unter  Belügen, Betrügen  von  — '  (Gen.):  rasnaosÜd  paiti.- sat»h>m  mi'iraAeca  aiwtjiruxtim  "indem er  dem  R.  widerspricht  und  den  M.  be- trügt" V.^S4-
5353:arsm-uxti,  ar^m.varsii.]
5359:•  j.  *ar»m.uxtay  ■'  f.  'rechtes,  angemesse- nesSprechen':  *ar7m.maiH  *kumata  mamne (sd.)    "uxti    küxta     anm.varsti     kvarasta
5365:•  j.  *aram.varstay-''  f.  'rechtes,  ange- messenes Handeln';  anm-maiti  *humata mamne{sä.)''arim.uxti . .  °ti  hvansia  P.25.
12424:oAurischta  Religion :  kahmät  paoiryS  mal-  \ yänqm  , ,  frada^ayS  'nqm  ,  .1  . .  yimäi .  .  fradaisalm  °nqm  .  .  äai  hi  mraom  . . vUanha  ml  minlff  b^ntala  (sd)  "nayäi (als  Gen.)  äat  . .  pailyaoxta  yimS  .  .  nSit dato  ahmt  . ,  tnirstl!  b3r?tala  'nayäi  V. 2.1  ff.;  Ytn.  14;  —  vXltäspaht.  .yS  batuUa upastaca  vTsata  .  .  •nayä  Yt  13.  99;  — ya%a  axsm  Asüyene .  .  zara%uänm  anu- matSe  'nayäi  anuxtie  'nay3i  anu.värltSe •nayäi  Yt.  j,  18;  Y.t?.  7;  —  hutaosqm  .  . yä  rrn  °nam . .  zraiia  (sd.)  dät  apica  aotaf Yt  ().26;'Vyt.  Jo(?);  —  ks  .  .  'nam  .  . vJbarat  aitaisva  vanfsva  ySyimö  ktnrtaoi^ .  .  vTs  iarsipia  V.  2. 42 ;  —  satö  .  .  zara- huiirS  .  .  ita  apam  vTjasaiH  .  .  °na  .  . vlspais  avi  karsvqn  Yt  jj.  94; —  mi^nm . .  yahmi  vyane  (sd.)  °nayäi  (als  Gen.) srirayai  p}r>^u.fräkaysi  . .  Yt  10.  64;  — sraoi^m  .  .  yB  damsJisS  *°nayä  Y. 57.23;
17321:*,«K«Sfl,.    _    .)  Opt.,   oder  «ich  Kon>«  ^^;  buxtiS  njnia  ahf-i  Vtiv47.      '
19716:■  i)  'deoken,  meinen,  sich  vorstellen';  oft im  Gegensatz  zu  sprechen  {'vak-,  mrav-) und  handeln  {'vam-):  Y.  ^5.  3,  35.  3, 39-  4;  '3-  4.  70.  4,  Yt.  IQ.  106,  13.  88,  P.  18, 25,  Aog.  25,  Gkiö^;  a)  mit  wie?-Adverb: *yai  niJij  yava  mihS  mamne  .  .  vavala  . , vavanza  P.  i8\  —  s.  noch  c  a.  b)  das Gedachte  erscheint  im  Akk.i  y^s  tu  T *aAuramazda  mSngAäizSYffA.)^'^  vag^ascä däs^a  varti^ä  yä  voha  Y._jp.  4;  —  zara- %uitrai  .  .  paoiryäi  vohu  mamnanäi  .  . vaokule  .  .  vav7rpzuie  YL 13.  88;  —  tat  ai vainmaidl .  .  hyat  t  maininiaai(i¥OM.yä vaocSimä^a  v>Tvzimäca  yä  . .  /yac'hananqm vahii'iä  ..  Y,j5. 3j  —  ySi  Tm  vS  tOil ßsä  mqhr?m  vansMtT  (sd.)  ya^ä  im m»3j(i*SKM,)<?S  vaoU^aY.45-Z^''\  —  '^i masyS  .  .  aojs  manyete  äusmahm  yaka mi%rasaii  .  .  manyäe  humatim  .  .  mraoiti hBxhfn  .,  vintyeiii  hvarst?m  Vt/o,  106; —  äai..manya{i.^k^  mananka  humatsm Aog.  25*';  —  amit.maiti  *humata  mamne *anm.uxti  hoxta  {vava^a)^'*  anm.variti kvansta  {^avama)^  "mit  rechtem  Denken hat  ei  gut  gedachtes  gedacht,  mit  rechtem Sprechen  gut  gesprochenes  (gesprochen),
20833:—  AblSm.,!!,:  vazrpm..yaAmat  /laca/ra- tpnsaili  ar»rS  mainyul  Yt  10.  97;  97J,  7  y. 87,  Aog.  5<¥;  —  hukairjm  bar>zB  yahmat ml  hala  frazgahaife  ar)dvj  Ytf,  96;  — tistrlm  .  .  *yahmat  haca  b}r»zat  haosra- var?h3m  Ytty.4;  —  GSm.,  n.:  mt^nm  .. yeAhe  zim.frdis  maihanim  vllät^m  .  . yeiihe  asia  rätayä . . spasS  at^häire  Yt  70. 44f.;  60,  68,  69,  70,  82,  85,  104,  143, 5.30,  7J.  81,  93\  107,  V. /;.  13J,  Kj. 44;  —  sraosfm  .  .  yeti/ie  ahiinS  vairyB snaihi/  visata  Y.  ^y.  32;  ai,  23;  — yän^m  vO  yäsämi  . .  yeAhe  däiti  paiti vaahs  nisrJta    anaiwi-druxti  (sd.)   Y.  6j.
23403:*'^Aaahqm  Y.  60.  4^*;  —  tüfit  't?hs  ahmät syao%mm  v?r?zyeiti  yaia  ya^ . .  N,  4S,  V. jÄ.  I o,  I a ;  16.  IT,  —  mit  Dat :  avd^a  tl anhat  -ahs  "V.iS.J;   bes.  in  eschato- logischem Sinn:  vaaAu/a  *'inhas&i^^  äfrl- nami  vTspayä  aiaonB  siSis  "was  gut  und was  noch  besser  ist,  das  wünsche  ich.." Y.  52.  1 ;  -—  vamthisca  ahä  vattuhlüa a^ayB  hupaurvä  'hihls  aparä  (näml.  Sftl- nämi . .,  s.  eben)  Y.  J2. 3 ;  —  ye^hi  hätqm aal  ytsttE  (Sp.  1 370  u.)  paiti  'tiAs  masdä  . . vag^a  Y,  27. 15;  Vr. /6.  3; — yapia..asü matyS  .  .  "nhB  .  .  srays  .  .  tat  nö  dayaia Y.  65. 14'';  —  yatam  , .  yeAhe  daiti  paiti 'nhs nisrita  anaiwi.druxti(.sd.)  Y.65,11*); Vyt.jo  {'tihs);  —  mit  Abi.  aus  ^vanhav—. va>»hu  tu  (Sp.  654  m.)  vaahaot  'nhs  buyai . .  saohre  .  .jamyat  vs  vanhaot  •nho  ma  . . akäi  als  Y.  59. 30  f.  S.  noch  *wfl»- No.  14.  Undeudich:  'ahanhal  a^aha upa.gfr?mbayan  N.  7/»'.
25004:'huItraAe  .  ■  yim  istn  aniisa  sppnta  . .  ahüm  'huiirai  Vr.  12.  i;  —  Zw«  'tum  yatamaide 'tBmca  gai^anam  Yty.92;  91,  Vr.  2.  4, '_>-/«  sarahuHrstn  Y.  70. 1 ;  —  amtrptstö 16.  3;  —  ya%ä  aha  (Sp.  a8a  o.)  vairyö  '^wS  S.  /.  7  '"';  —  kaurvatats  "5aiff  S.  /. (näml. »araättÄrff)  ai-S  °(uP^  a/ätc'it  Äa^'a'6'°>; —  ä%rS  ahurahe  matdä  '%wS  b^rp- ..  dazdä{5Ü.)  Y.  27.  13;  —  yat  dim  (näml.  j  «n/J  yS  asahe  Y.  22.  4;  1.  17,  4.  2;  — tarahuttrfm)  aküm{Si^.  282  o^ca  Hümca  .'hwasca  bfrgzats"^  H.4S;  Vr.^.6;  — adadaj  Y.  iff.  12;  —  zara%ustrS  .  .  'iu/\  avi  iava  'tvS  (VS.)  bima"^ yasmm  g?r?Q- astvaihyB  gal%ayä  bansnul  bipaÜista-^maAi  \x.21.3;  —  kaya  °tavöt  nmänyS naya  Yt.  ig,  41;  —  s.  noch  Yt  8.  ^^' vTy^ö  santumS  dähyumö  tarähustrS  puxtiJ unter  7.  ß)    AHM.  tÜT    die   gtsammle   äfjAam  daÄyurtamyä  anyä  ra/sit..ühru.-
25104:•  j.*raSTwyö.varstay-'*  f.  'angemessenes Handeln, Tun':  mananhaica*humaiH  Mt- vasca  huxti  zastayasca  *kvarsti  °ti  natdys (sd.)  aAmi  . .  "bei  gutem  Denken  des Sinns,  gutem  Reden  der  Zunge,  gutem, angemessenem  Handeln  der  Hände  bin ich  . ."  P.  28.
25953:•  j.  saSay-  Adj.  —  ?  — :  buxtiS  nqma ahmi  'ilis  nama  ahmt  Yt  15. 47.  Geringe Stelle.
26792:•  j.  "stnuiuxtiä  N.  79". Var.  iltiuix'. —  Pü.;  fehlt.  —  ')  Mir  scheint. das  WoTt  gehört  noch  za  ti./S  und  iwai  als Adjektiv  lu  saofa(id.),  in  dem  zum  Aasdruck kommt,  dass  der  Zaatar  im  Gegensatz  za  den /!aiao  einen  festen  Sitzplatz  hat.
30695:zu  duzvaHta-:  daityanqm  rahwyanqm 'lanqm  lyadhnanqm  var)zäi  pairi  . .  duz- variianqm  syaöknanqm  varjzäi  Vr.  7J. I,  a)  sonst  nur  neben  hüxta-  und humata- :  humataht paiti  manaahe  küxtahe paiii  vacatahs  °tahe  paiti  iyao%nahe  Yt 16.  6;  —  ästuyi  humatim  manO . .  küxUm vacö  .  .  •Um  syad^amm  Y.  J2.  8;  — fra- stuyl  kumaisibyascä  hüxtsibyascä  'tdibyascä mahwsibyascä  vax>hwSibyascä  varltvSi- byascä  Y.  //.  17;  —  nanm  alavamm dahrUfUm  kumatimca  manB  hüxümca  vac5 •Umca  syaohtum  Vr.  2.  5;  —  aa^. .  manya mananha  humahm  . .  hitsva  mrätoi  hUxttm .  .  sasiaiibya  var>za  't»m  syadhium  Aog. 25  ff.;  ^  *ar»m.maiti  *Aumata  mamne  (Sp. 1121  f)  *ar>m.uxti  *  hüxta  (vavaca)  anm.- varsti  °ia'^  (vavarfzd)F.2^; — yezi  kuma- tim  mainySt  kUxt^m  väcim  mrväl  'bm'^ v»nsyäl  syadhn»m  Gk-iöy;  —  narS  asa- vanö  humataü  mainimna  hüxtäU  ntrvats 'täis(3.\sOb}.)v>rpzyant3Y.jo.4;—AumiUa- nqm  hüxtanqm  •tanqm  iyadaca  anya- dacä  v»r>zyamnanqmcä  vävtmananqmca mahl  aibT.jaritärS  Y._J5,  aj  FrW.^,  i;  — "•"rfil^r* (sd,) ,  .paiti  nivaitis . .  humaialsuia haxtalsuca  •taisu^a^'*  ti.S4;  —  vTtpäi/ 'hwa   humatäii  .  .  huxtäis  .  .  'täis  pairi-
=== paiti.smuxta / smuxta ===
15965:•  j.  '^päiti.Smuxta-  Adj. :  s.  unter  paiti.- smuxta-.
27918:•  j.  zaranyö.tuvix&na- Adj. 'mit  goldener Verschnüning':  andvl . .  ao%ra  *päili. smuxta  'na  ". .  mit  Schuhwerk  angetan, das  mit  goldenen  SchnUrbändem  befestigt ist"  Yt.5.  64.
```


## [2026-09-07T17:39:45.928Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD && ls; echo \"=== grep آموخ ===\"; grep -n \"آموخ\\|آموز\" FFD_pages.txt | head -20",
 "description": "Grep FFD for amuxtan"
}
```


### [2026-09-07T17:39:45.993Z] TOOL RESULT

```
FFD_asmaneketab.pdf
FFD_pages.txt
FFD_pages.txt.pages
=== grep آموخ ===
434:هن آموختن َوهل: بسیار آموختن
758:آموخت < فارسی میانه 270871 + ایرانی باستان 3-2۵0-1۵*. برای 3و 1۵ >
764:آموز < فارسی میانه 38162 < ایرانی باستان 2 + 3-۵06*. برای 2 آرای. در
2341:8 : (ريشه < آموختن) ۱۵ 8 : (ريشهٌ ضعیف ۰ 8270) ۱۰
```


## [2026-09-07T17:39:49.682Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD && sed -n 745,780p FFD_pages.txt; echo \"=== page tags near ===\"; awk 'NR>700 && NR<790 && /pdf page/' FFD_pages.txt",
 "description": "Read FFD amuxtan entry"
}
```


### [2026-09-07T17:39:51.038Z] TOOL RESULT

```
«حرکت کردن» است و با پیشوند فعلی 2 «حرکت کردن به سوی متکلم» معنی می‌دهد.
+ رفتن.
چنان که دیده می‌شود» «آمد» از یک ريشه و «(آی» از یک ريشه دیگر آمده است. همه
فعلهای فارسی, جز چند فعل از جمله «آمدء آی» از یک ريشه آمده‌اند. بر اثر تحول
لفظی و قواعد دستوری» ماده‌های ماضی و مضارع در فارسی میانه و دری» با هم
رابطه‌ای بی‌قاعده یا سماعی دارند. به عبارت دیگرء قواعدی مطرد در فارسی میانه و
دری وجود ندارد که طبق آن قواعد بتوان ماد ماضی فعلی را از روی مادهٌ مضارع آن و یا
مادهٌ مضارع آن فعل را از روی ماد ماضی آن ساخت.
آمرزیدن
آمرزید» ماد ماضی جعلی است.
«آمرز» < فارسی میانه 20872 + ایرانی باستان 3-774-2*. برای ۵ > آرای. 3
پیشوند فعلی است. ريشهٌ 13720 به معنی «مهربان‌بودن» است. :
اموختن
آموخت < فارسی میانه 270871 + ایرانی باستان 3-2۵0-1۵*. برای 3و 1۵ >
آراست. 2۵0 در اصل 13301 است به معنی «رها کردن»» ۴ پیش از ۲ به #بدل شده
[pdf page 33]
فعلهای فارسی دری
است.

آموز < فارسی میانه 38162 < ایرانی باستان 2 + 3-۵06*. برای 2 آرای. در
6 به جای 1 آمده است.

َ در فارسی میانه مانوی 178۳۱671 به جای 30071 و 127302 به جای 3782 آمده
است. از ريشهٌ 13201 با پیشوند 1278.
امیختن

آمیخت < فارسی میانه 270884 < ایرانی باستان 3-080۳12*. برای 3 و 18->
آراست. *8 در اصل 818 است» 8 پیش از ۲ به #بدل شده است. ريشهٌ 118 به معنی
«آمیختن» است.

آمیز + فارسی میانه 37082 < ایرانی باستان ۵-[3-0۵1*. برای 2 -> آرای. [ در [0۵
به‌جای 8 آمده است.

آوردن

آورد + فارسی میانه 2۳070 < ایرانی باستان 3-07-12*. برای و1۵ - آراست. 3
=== page tags near ===
[pdf page 31]
[pdf page 32]
[pdf page 33]
```


## [2026-09-07T17:40:05.633Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD && pdftoppm -f 32 -l 32 -r 200 -png -singlefile FFD_asmaneketab.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/ffd32 && echo ok",
 "description": "Render FFD page 32"
}
```


### [2026-09-07T17:40:07.165Z] TOOL RESULT

```
ok
```


## [2026-09-07T17:40:07.522Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD hammoxtan ===\"; grep -n \"mōxt\\|moxt\\|hmwxtn\\|hammoz\\|hammōz\" PHD.txt PHD_mackenzie.txt | head -20; echo \"=== NYB ===\"; grep -n \"mōxt\\|moxt\\|hammōz\" NYB_vol2_glossary.txt | head -20",
 "description": "Grep MacKenzie and Nyberg for hammoxtan"
}
```


### [2026-09-07T17:40:07.591Z] TOOL RESULT

```
=== PHD hammoxtan ===
PHD.txt:125:did ... add other. add dig |YTMAL < А *?{т?1 | N di] yesterday. delete *drém ... (read balgam) drubušt ... add protective. drust [drw(d)st' ... duš-čihr ... add ill-natured. duš-nām [-n^m | (M dwjn'm), N ~] add ill-famed. dušwār [dwáw?l | (M dwjw'r), ... ékanag ... for obedient read loyal, faithful. ~th : for obedience read loyalty, faithfulness. for Farrēbāg... read KFarrēbāy [pinb(^)g] ... frayad |pl(y)d^t' | N faryad] ... delete M pry'd. frazand |prz/znd | ... frusag ... add M prwšg. garódman ... read | P grdm'n. gazdum |gcd(w)m, gzd(w)m |... guftàr ..., ~th : add eloquence. hambar |hm-, hnb] |... add  hamest |hmyst'] whose good and bad deeds weigh equal. ~(ag)an |-(k)^n'] limbo, the neutral station between heaven and hell. delete hammist ..., ~(ag)an ... handarz ... add M °’ndrz. hammoxtan, hammoz-, ~i8n : add learning. hast |TWMNYA < A tmny ; ... add hūg [HZWLYA < A hzyr’; hwk' | M hwg, N xiig] pig. add hūkar(ag) |hwkl(k') | N xükara] porcupine. (not hedgehog) add *huzārag [hwc’lk | N хијага) little, small, few. !jadag ... add fortune. jüdan ... | M jwwdn, jwy- ... add karawuš [kl wš| N ^] wine-press. delete karbunag ... read karbūg |klpwk', klbwk'| lizard. kardagān ... add service (ofthe gods). delete karxēš vds
PHD.txt:392:hamēstār, —ih [hmyst!l, -yh] = hamēmāl, ~ih. hamésag [hmyfk! | M hmyšg, N —a] always. ^h : eternity. ~-86z [-swe] ever-burning. hamē-wahār [hmy whl | N haméfa-bahar] marigold. ham-éwénag [Am'dwynk!'] of the same kind, homogeneous. ham-góhr (hmgwhl! | M hmgwhr] of the same substance or nature, consubstantial. ham-ginag [hmgwnk! | M hmgwng] likewise, so. P hāmharz [A())mAlc | P I? mhyrz] adjutant, attendant. hāmīn [A*myn! |= M] summer. ~ig [-yk'] (of) summer. hāmist [KHDE, v. hammis ; )”mst!] all. ham-kār [hmk’l | N ~] collaborator. 7h : collaboration. hāmkišwar [mkyfwl | M. -wr] universe. hammis [KH DE < A k-hdh), ат... ~: together with. hammist [hmyst'] stagnant, peaceful. ~(ag)an [-(kYn'] limbo, the neutral station between heaven and : hell. vl hammóxtan, hammoz- [ALPWN-tn! < A У "Ip: hmwhtn', hmwc-, Ki hmsoz- | M hmwxtn, N āmēxtan, ámóz-] teach; learn. -išn: teaching. hammdxtar [Amwht?!] learner. ~th: learning. hammóz- , ~i8n, v. hammóxtan. —@йг [kmwcek?l | N āmēzgār] teacher. ham-nibardih [hmnpityh] (single) combat. hamēūģ [/tmwg] equal, like. hámón [k mwn' | N kāmūn] level, flat. hámoyén [/?mwdyn!] all. ham-pursag [hmpwrsk!] consulting, taking counsel. ^h : consultation. ham- |-ránih [Am nyh] battle, combat. ~-samiain [-s"m?n!] contiguous. ~-sardag [-sltk'] of the same kind, like. ~-sayag [-sdk! | N hamsáya) neighbour. ~-tag [-t*k! | N hamid] equal, peer. «tan [-tn'] of the same stature, build. ~=-tihmag [-twhmk'] relative, relation. hamwar [hmwl | N hamwār] level, abreast. hámwiür(ag) [%()mw?/, -k! | N hamwdara] always. ham-zamān [hm ODNA | N —] instantly, immediately. handām [And*m | = P, N andàm] member, limb. handarz [hndle | N andarz] advice, injunction, testament. handarzénidan, handarzén- [hndleyn-ytn!] advise.
PHD.txt:4291:wear paymoxtan, pēšīdan. weasel rasüg.
PHD_mackenzie.txt:556:       hammoxtan, hammoz-, ",iAn : add learning.
PHD_mackenzie.txt:1013:timoxtan, iimoz-, read hamm6xtan, hammoz-.
PHD_mackenzie.txt:2765:   hmwz- I M hmwxtn, N iimoxtan, iimoz-] teach; learn.
PHD_mackenzie.txt:4156:paymoxtan, paymoz- [ptmwhtn 1, ptmwc- I M pymwxt, pymwc-] don,
PHD_mackenzie.txt:6416:disbelief anastawanih.                  don paymoxtan, posidan.
PHD_mackenzie.txt:6937:  frahang, sniisagih.                     learn hammoxtan; ....., by heart warm
PHD_mackenzie.txt:6939:koumiss hur.                              learner hammoxtir.
PHD_mackenzie.txt:6940:                                          learning hammoxtiirih.
PHD_mackenzie.txt:7759:teach castan, frahixtan, hammoxtan,       thorn xar.
PHD_mackenzie.txt:7761:teacher hammozgar;          poryotkes ;   those awesan.
PHD_mackenzie.txt:7763:teaching afrah, casisn, hammozisn.        thought handesisn, menisn; v. con-
PHD_mackenzie.txt:7946: wear paymoxtan, posidan.               'winnow wextan.
PHD_mackenzie.txt:8487:casiSn, cwisn             ,~~         paymoxtan            \\~t6~t)
PHD_mackenzie.txt:11565:asanih                            hammozgar            ~jC;~
PHD_mackenzie.txt:11627:hammoxtiir            ~~..-            hamdiidcstiin       \~t(»~~
PHD_mackenzie.txt:11628:hammoxtarih      ~~~                   hamdadcstanl                  ..u~
PHD_mackenzie.txt:11630:hammoxtan               \\tb'    ce-   hamcn-
=== NYB ===
389:imoxtarčh
403:amoxtarčh the act of instructing, in- struction 7011, l
2237:ikartan [krtn'; klty; ‘BYDWN-t'] kun- [ BYDWN-;forms v. I, 179; pres. 3d p.sg. kwnd: read kund] to make, to do, to per- form, to exercise, to commit, to cause, to bring about; to manufacture, to construct (hac ‘of’ a material); — forms active deriva- tive vbs. a) from v.ns. in -išn, e.g. āsāyišn ^ to repose, azbäyisn ~ to invoke; gar- zišn, īzišn, koxšišn, nikērišn, pursišn, za- nisn ete.ete. ~ ; b) from other nouns: čfrin, amoxtareh, appar, hampursakeh, tak, varz ete. ete. —, v. the resp. ws.; — with a pred. adj., e.g. 73. 34" etc.; girt kart = girt kartak (g. v.); vat-kart v. vat; or a pred. subst., e.g. api-$ ... bitaxš kunom 2510-11; . with kart as its cognate obj. P2:6-7. 8 [read (TB =) nev kart" kunän that I may do good deeds]. — With prev.: andar 6 kar ~, v. kar; api-§ Mānušcihr andar 6 Patisz"argar kart he brought M. (as a captive) to P. 1164-5, cf Bd A p. 2315-5; — apüc ~ to repel 42*3 gl.; to reflect 1125; — pat ddr apar ~ to crucify a p. 208; — bé ~ to remove 65; — berön asmän kunst he wil turn them out of heaven 10318; — frāc ~ to send forth 161!5; to bring forth, to produce 48?9; to attempt 81?!. — NB: man kart HWH-wm 374-5 for man kart-om by me it was done, v.s. v. h- and -m. — *BYDWN.x,ot' = kunät 5314, cf BY- DWN-x,-yd = 2nd p.sg.kunēKnS VII, 11. — Av. (444 sqq.) tkar-, pres.ko ranu-; OP kar- kunav-; MPrth kyrdn kr-; MPrs kyrdn kwn-; Paz. NP kardan kun-; cf s.v. hangirtikeh.
3198:2räd [l’d; inser. and Ps. Pdy] postpos. l. for the sake of, because of, for, on behalf of, in favour of (7220-21), con- cerning (37?. 2919 etc. passim); ham cim ~ for that very reason 512-13, 671-2; han cim ~ 342, & ~ 795. 9626, 982° for that reason; ēt ~ cé because (conj.) 773-5; ce ~ why? 3511. 795; õi ke ~ for whom 183; — preceded by an inf. or a v. n.: in order to, for the purpose of, because: ditan i Zartuxšt ~ (in order) to see Z. 4777, 5218-19; ves avis matārēh i xrat ~ because more wisdom had been allotted to him 9041-12; — forms together with hac or pat a frame preposition: hac bim i Artaxšēr ~ for fear of A. 1525; 3719. 4612-19; hac hin cim ~ 118%; kirpak i pat dat ~ kart for the sake of Law 6419; pat omet +... ~ in hope of 1211917; pat hän cim ~ cé because (conj.) 10421-22, — 2. used as in NP: a) ‘to, for’: cahārpādān ~ ap hamë dat 1419; Papak ~ héc fradand ne būt P. had no child 19; 32-4, 422;  ménam to ~ nevakeh 4771, v.s. v. méni- tan; 427; frazand i zu&s m kar u kirpak bē- dimoxtan 652-23; — b) denoting the dir. obj. of the pres. tense: hakar né han ~ <apdc> dārēt if you do not abjure that (religion) 191; 2520-21; 453; — c) denoting
6769:patmoxtan pašsār: patisär padvazed: pat-vac- padyavand- patiyavand pšč: pad paēdā, paidà: paitäk pačma(n): patman pačvand: patvand pačvastan: patvastan pahalim, pahlum : pahlom paharčxtan, paharčž-: pahrčxtan parastidan: paristätan pardazašn: pardaxtan pasand: passand pasaxt: passaxt päsux: passaxu paščman, -màni: pašč- mančh patit: patit patkàr: ~ päya: pädak péda: paitäk pédabar: paitäm-bar pčrož: pérdz pēš: ~
```


## [2026-09-07T17:40:16.044Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== CHEUNG mauk/mauc ===\"; grep -n \"mauk\\|mauč\\|\\*muk\\|hammōxtan\\|āmōxtan\" CHEUNG.txt | head -30",
 "description": "Grep Cheung for mauk"
}
```


### [2026-09-07T17:40:16.096Z] TOOL RESULT

```
=== CHEUNG mauk/mauc ===
```


## [2026-09-07T17:40:19.387Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && wc -l CHEUNG.txt; grep -in \"amoxtan\\|mauc\\|MAUC\\|muxti\" CHEUNG.txt | head -20",
 "description": "Search Cheung loosely"
}
```


### [2026-09-07T17:40:19.437Z] TOOL RESULT

```
58427 CHEUNG.txt
9792:undress ?’, YAv. framuxti- ‘the undressing’ (V 6.27) = Liste: 45 
17760:*maucl 269 
17827:270 *mauc2 
33393:framuxti-, 138 
40755:amoxtan/amoz-, 270 
56024:*(h)mauc, *paus 
56437:*(h)mauc, *paus 
56638:*bauf, *mauc! 
57051:*iauc, *mauc? 
57058:*mauc! , *raic 
57537:*mauc! , *raic 
58132:*iauc, *mauc’, *saHh 
58380:*(h)mauc, *paus
```


## [2026-09-07T17:40:22.394Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n 17750,17870p CHEUNG.txt",
 "description": "Read Cheung *mauc entries"
}
```


### [2026-09-07T17:40:22.456Z] TOOL RESULT

```
*mars (on account of the Pahlavi and Manichaean forms), for which he quotes 
Hübschmann 1895: 84. > DMMPP: 154a 

Pres.: IND. 3sg. BMP pl’mwsyt /framosed/, IMPV. 2р1. MMP m’ pr’mwsyyd, ВМР m’ plmwsyt /ma 
framosed/ ‘don’t forget!’; Partic.: pres. BMP pl’mws’n /framosan/, perf. pass. MMP fr’mwst 
*PARTHIAN: fr’mwS- ‘to forget? > DMMPP: 154a 

Pres.: IND. 35р. fr'mwšyd, SUBJ. 2sg. fr’mws’; Partic.: perf. pass. fr’mwst 


*maucl 269 


*KHOTANESE: ? marsyarä (impv. 2р1.) ‘forget’? {hapax} || (+ *fra-a-) hämura- 
‘forgetfulness, forgetting’ = SGS: — 

*SOGDIAN: (+ *fra-a-) ? BSogd. fr’’wyscy, BSogd. Br'wcy, MSogd. fr’wycyh 
‘forgetfulness’ 

*NWIR: (+ *fra-à-) NP firämüstan, Bal. Samust/Samüs- (intr.), šamošt/šamoš- (tr.) ‘to 
forget’ 

*NEIR: (+ *fra-(a-)) Yghn. firomic/S- ‘to forget’ (< NP ?), Yi. formo-/farmísc-, M. 
formiy-/formisk-, Wa. rom(s1)s-/romost ‘to forget’ 

*MISC: (+ *fra-) Огт. š'amot ‘forgetfulness’, Par. nhamur ‘forgetful’ 

*SANSKRIT: mars ‘to forget’ (RV+) = EWAia II: 332 

«PIE *mers- ‘to forget’ = LIV: 440 f. | Pok.: 737 f. 


*IE COGNATES: Lith. uz-mifsti, Toch. märs-, Arm. mofana- ‘to forget’ 
*REFERENCES: IIFL II: 209a, 537a; DKS: 324b f., 477b f.; Werba 1997: 366; Adams 1999: 455 f.; 
Steblin-Kamenskij 1999: 302; Shahbakhsh: s.v. Samus-; Korn 2005: 117, 132, 146 f., 316, 387 


*marZd ‘to have pity, forgive’ 

*AVESTAN: OAv. moroZd- ‘to have pity’ = Liste: 44 

Pres. them.: IMPV. 2р1. OAv. mereZdatà (Y 33.11) 

*MIDDLE PERSIAN: (+ *ā-) MMP "'()mwrz- BMP "mwic- /amurz-/ ‘to forgive, 
absolve’ = DMMPP: 41а 

Pres.: IND. 1sg. BMP /amurzém/, 1р1. BMP /amurzem/, 3pl. MMP "mwrzyynd ‘they show mercy [= 
Sogd. prm’ndy’ kwn’nd]’; Partic.: perf. pass. BMP ’mwlcyt /amurzid/, MMP ’mwrzyd 

*PARTHIAN: (+ *4-) "тууа ‘compassion’ = DMMPP: 40b 

*KHOTANESE: mulysdi- (f.) ‘compassion’ 

*NWIR: Bal. marzit/marz- ‘to absolve, forgive, bless, encourage, support’ || (+ *a-) 
NP amurzidan/amurz- ‘to forgive, absolve’, borrowed into Bal. amurzit/amurz- ‘id.’, 
Qohr. ämerz-, Yzd. amorz- ‘to forgive’ 

*SANSKRIT: тага ‘to take pity, pardon’ (RV+) = EWAia II: 326 f. 

© The Пг. root *marzd has no IE correspondences. On the possible interpretations of 
the peculiar structure of this root see EWAia, l.c. 


*PIE — = LIV: 444 f. | Pok.: 737 f. 
*REFERENCES: Bailey 1936: 338; DKS: 338a f.; Werba 1997: 365; Kümmel 2000: 375; Lecoq 2002: 
641b; Shahbakhsh: s.v. marz!-, amurz- 


*maut! ‘to release, let loose/free’ 

*CHORESMIAN: (+ *uz-) m/zmxs- (intr./inch.) “о (go to) sleep’, m/zmx’sy- (sec. 
caus.) ‘to let (someone) sleep’ || (+ *pati-) pcmxs- (pcmxš-) ‘to become numb’. > Cf. 
MacKenzie I: 554; 141 f. © Samadi: 264 

*MISC: Orm. moZ-/mók ‘to loosen, untie’ = möZ-/mök ‘to open’ 


270 *mauc2 


*SANSKRIT: moc ‘to release, be(come) free; to liberate, free’ (RV+) = EWAia II: 
382 

9 Further Ir. cognates are unknown. 

«PIE *meuk- ‘to take, untie, etc.’ > LIV: 443 f. | Pok.: 744 f. 

*IE COGNATES: Gr. uócoopnoa ‘I blow my nose’, Lat. e-mungö ‘I blow out, snuff’, 


Lith. maükti ‘to take off’ 
*REFERENCES: IIFL I: 401b; Werba 1997: 217 f.; Kiefer 2003: 201 


*maud? ‘to learn, teach’ 
*MIDDLE PERSIAN: (+ *ham-) MMP hmwc- ‘to teach’, (pass./inch.) MMP hmwxs- 


‘to learn [i.e. to be teached, instructed] > DMMPP: 179a 
(+ *ham-) Well attested: Pres.: IND. 15р. MMP hmwcym, BMP hmwcym /hammözem/, 3sg. BMP 
/hammozed/, 3р1. BMP hmwcynd /hammözend!, etc. 


*PARTHIAN: (+ *ham-) ’mwc- ‘to teach’ = Ghilain: 63 | DMMPP: 40a 


, 


Pres.: IND. 3pl. *’mwcynd, SUBJ. 25р. ’mwc’h; Partic.: perf. pass. ’mwxtg ‘learned’, "mwxt, П "mwc'd; 
Inch./Pass.: pres. IND. 3sg. ’mwxsyd, SUBJ. 3р1. hmwxs’nd; Inf.: *’mwxtn 

*SOGDIAN: BSogd. mwck, BSogd. mwck’, SSogd. mwz’’k’ ‘teacher’, (pl.) SSogd. 
*mwz'kty 

*CHORESMIAN: (+ *4- ?) "mxs- ‘to learn’, mwcy- (caus.) “to teach, instruct’ 
= Samadi: 113, 112 

*NWIR: Zaz. misayis/misen- (inch. ?) ‘to learn, experience’, misnayis/misnen- (caus.) 
‘to teach, show’, Awrom. mısäy/*mıs- ‘to learn, understand’ || (+ *à-) NP ämöxtan/ 
amoz-, Ham. ämotän/ämuz- ‘to learn; teach’ || (+ *fra- or *ham- ?) Anar. ihmut ‘he
```


## [2026-09-07T17:40:28.306Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n 17870,17930p CHEUNG.txt",
 "description": "Read rest of Cheung mauc3"
}
```


### [2026-09-07T17:40:28.355Z] TOOL RESULT

```
amoz-, Ham. ämotän/ämuz- ‘to learn; teach’ || (+ *fra- or *ham- ?) Anar. ihmut ‘he 
learnt’ || (+ *ham- ?) Kafr. hamiitemiin/hamis- ‘to learn’ 

*NEIR: (+ *ni-) Oss. L nymuzyn/nymygd, D. nimozun/nimugd ‘to point out; to carry 
to, out; to recommend’ 

9 The root is exclusively Iranian. It is perhaps no coincidence that it is formally 
similar to *jaué ‘to teach, learn’: таиё may have been abstracted from *ham-Hauc 
(cf. Skt. oc ‘to be accustomed, to get used to’), comparable to *iaué, which has been 
abstracted from prefixed formations in *abi-, *ni-, etc. (q.v.). 


“PIE LIV: — | Pok.: 
*REFERENCES: Zhukovskij II: 96; Ivanow 1926: 419; Abrahamian 1936: 107; MacKenzie 1966: 102; 
Abaev, Slovar’ II: 205; Paul 1998: 306a 


*maud ? ‘to mourn’ 
*MIDDLE PERSIAN: MMP mwy- ‘to mourn’, BMP mwst /must/ ‘mourning’ 


c DMMPP: 234b f. 


Pres.: IND. 3pl. MMP mwyynd, SUBJ. 1sg. MMP mwy’n; Partic.: pres. pl. MMP mwy’g’n, perf. pass. 
BMP mwst /must/ 


*maus(H) ? 271 


*NWIR: NP möyidan ‘to mourn; weep and cry aloud’, NP must ‘trouble, distress of 
mind, complaint, lamentation’ 

*MISC: ? Arm. (LW) moyr ‘begging’ (semantically not evident, Benveniste 1964: 5) 
© The Persian forms are isolated within Ilr.: they might be connected to the IE 
correspondences cited by Pokorny: 743: Lith. maudziu (maüsti) ‘I long for’, Gr. 
u$00c (m.) ‘word; tale’, OCS mysle ‘thought’, etc. However, if the Persian forms 
were from older *maud as assumed generally, they would be identical with the 
semantically antonymous root *maud ‘to rejoice’ (Skt. mod), which is attested in 
Iranian: not only in Avestan (maoóano.kara- “providing joy’), but apparently also in 
OP (*maudabaga- ‘who pleases God’, Mayrhofer 1973: 208, ad 8.1185). The co- 
existence of two formally identical roots with opposite meanings within one 
language is inconceivable. More likely, we are dealing with the root *nau(H) ‘to 
mourn’ (q.v.), which became contaminated with the antonymous root *maud ‘to 
rejoice’ at a certain stage. Cf. NP noyidan ‘to cry aloud, lament’, navistan ‘to groan’, 
NP nöyah ‘plaint, moan’, nöstah, navastah ‘noise in the throat by one’s crying’. 

*PIE — = LIV: — | Pok.: 743 


*REFERENCES: Horn 1893: 223 f. 


*maug (*mauz) ? ‘to err, be foolish’ 

*AVESTAN: YAv. aSamaoya- (m.) ‘teacher of false doctrines’ 

*MIDDLE PERSIAN: MMP *himwg’n (pl.) ‘heretics’ (LW) = DMMPP: 34b 
*KHOTANESE: LKh. muys- ‘to be foolish’ © SGS: 110
```


## [2026-09-07T17:40:39.981Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n 9760,9830p CHEUNG.txt",
 "description": "Read Cheung entry with framuxti"
}
```


### [2026-09-07T17:40:40.035Z] TOOL RESULT

```
*NEIR: Yi. imar-/imur, M. yumar-, Pash. $mörol ‘to count’ (LW ?), Oss. I. mært 
‘measure of dry substances, chiefly of grain’, Pash. dö-mra ‘so much’, cö-mra ‘how 
much’ || (+ *pati-) Oss. D. fzesmarun/£esmard ‘to know, be known; to find out; to 
recall’, Yzgh. pamar- ‘to wait for’ || (+ *ni-) Oss. I. nymzr, D. (med)nimer ‘on 
account of 

*MISC: (+ *à-) Orm. amar-ök, amar-ék ‘to hear’ = amar-/amarók, mar-/marök || (+ 
*ham-?) Arm. (LW) hamar ‘number, account’ 

*SANSKRIT: smar ‘to remember, to become aware, to be mindful of? (RV+) 
= EWAia II: 780 

9 The wide range of meanings which can be assigned to this root is odd: it may 
indicate the convergence of two IE roots ? Cf. LIV: Le. 

*PIE *(s)mer- ‘to observe, consider, think of || *smer- ‘to earn, get a share’ => LIV: 
569 f. | Pok.: 969 

ТЕ COGNATES: Gr. ї1ңєїрө ‘I desire, long’, Goth. *maurnan, OHG mornén, OE 
murnan, Engl. to mourn || Gr. реїіророл ‘I get a share’, (perf.) ëuuope ‘has a share’, 


Lat. mereö ‘I earn, merit’ 

*REFERENCES: KPF I: 82b, 207b; Ivanow 1926: 422; EVP: 74; IIFL I: 387a; KPF IV: 245 f.; IIFL II: 
190b; Abaev, Slovar’ П: 99 f., 201 Ё; EVS: 56b; Lecoq 1974: 60; WIM I: 69; WIM II/1: 80; DKS: 411b; 
Werba 1997: 265; Paul 1998: 291a; Cabolov 1997: 76; Cabolov 2001: 41; Cheung 2002: 204, 209; Kiefer 
2003: 191, 200 


*(h)maué ? ‘to dress, clothe’ 
*AVESTAN: (+ *pati-) YAv. "paitismaoc- ‘to shoe’ || (+ *fra-) YAv. framaoc- ‘to 
undress ?’, YAv. framuxti- ‘the undressing’ (V 6.27) = Liste: 45 


*(h)maué ? 139 


MED.; Pres. them.: INJ. 3sg. ? YAv. 'framaocata {vavcata} (F 484); Partic.: perf. pass. ҮАУ. 
paiti&muxta- (Yt 5.64, Yt 5.78, Yt 10.125). © For the emendation of YAv. 'framaocata see Klingenschmitt 
1968: 484. 


*MIDDLE PERSIAN: MMP mwg, BMP mwk /mog/ ‘shoe, boot’ || (+ *pati-) MMP 
pymwc-, BMP ptmwc- /paymöz-/ ‘to don, wear’ || (+ *fra-) MMP fr’mwc- ‘to put, 
take off (clothes), remove’. Ф The spelling of MMP fr’mwc- with middle [°] points 


to prev. *-2-? = DMMPP: 233a, 289b f., 154a 

(+ *pati-) Pres.: IND. 3sg. MMP pymwcyd, BMP ptmwcyt /paymozed/, 3pl. MMP pymwcynd, BMP 
ptmwcynd /paymözend/, IMPV. 2sg. BMP ptmwc- /paymöz-/; Partic.: perf. pass. MMP pymwxt, 
pymwwxt, Pass.: pres. IND. 3sg. BMP ptmwcyhyt /paymozihed/ || (+ *fra-) Pres.: IND. 3pl. MMP 
pr’mwcynd; Partic.: perf. pass. MMP pr’mwxt, MMP fr'mwxt, Inf.: MMP "pr'mwxtn 


*PARTHIAN: (+ *pati-) pdmwc- ‘to dress in, put on (clothes, and figuratively)’ || (+ 


*fra-) fr'mwc- ‘to take off = Ghilain: 62 f. | DMMPP: 270a, 154a 

(+ *pati-) Pres.: IND. 25р. pdmwcyyh, 3sg. pdmwcyd, 3р1. pdmwcynd, SUBJ. 25р. "pdmwj'h, 3sg. 
“pdmwe’h, IMPV. 2р1. pdmwcyd; Partic.: perf. pass. "pdmwxtg, pdmwxt, П pdmwc'd; Inf.: pdmwxtn || (+ 
*fra-) Pres.: IND. 35р. fr'mwcyd, 1р1. fr'mwc'm, 3р1. fr'mwcynd, SUBJ. 35р. "fr'mwc'h, IMPV. 2pl. 
fr’mwcyd; Partic.: perf. pass. fr’mwxt, П "fr'mwc'd; Inf.: fr'mwxt 


*KHOTANESE: (+ *pati-) pamjs- ‘to put on (clothing)’ = SGS: 66 

*SOGDIAN: (+ *pati-) BSogd. ptm’ync, CSogd. ptmync ‘to clothe’ || (+ *fra-) BSogd. 
Br’’mcn- ‘to undress’, CSogd. fr’mnc- ‘to divest oneself of, take off’. 0 CSogd.
```


## [2026-09-07T17:40:43.861Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n 9830,9870p CHEUNG.txt",
 "description": "Cheung (h)mauc PIE line"
}
```


### [2026-09-07T17:40:43.925Z] TOOL RESULT

```
Br’’mcn- ‘to undress’, CSogd. fr’mnc- ‘to divest oneself of, take off’. 0 CSogd. 
fr’mnc- may have lost the nasal: the stem vowel is possibly nasalized. 

(+ *pati-) Widely attested: Pres.: IND. 3sg. CSogd. ptmynct (Weber 1970: 193); Impf.: IND. 3sg. BSogd. 
pt’ym’ync, BSogd. pt’ym’yncw, CSogd. ptymync, MSogd. *"pt'ymync, etc. 

*CHORESMIAN: (+ *pati-) рсшс- ‘to put on (clothes), don’, (intr./inch.) ‘to dress 
oneself? || (+ *fra-) smc- ‘to undress’ = Samadi: 141, 195 

*NWIR: NP mug ‘large boot’ (< Arab. < MP) || (+ *pati-) NP paymöz-/paymöxtan ‘to 
dress’ 

*NEIR: (+ *upa-) Sariq. baymej-/baymi/üg ‘to close’ (? -y- from naymej-) || (+ 
*ni($)-) Sariq. naymej-/naymi/üg ‘to hide, conceal; conserve’ || (+ *pati-) Ishk. 
pembc-/psmüyd, Sh. (Baj.) pinij-/pinuyd (with lab. dissim., EVS: 56b), Sangl. 
pamej-/pamewg, Wa. pumuc- (pum(s1)c-)/pumayd- (pumayn-) ‘to put on clothing, 
dress’ || (+ *fra-) Oss. І. remuzyn/remygd, D. remozun/remugd ‘to tear apart, rip 
out’ || (+ *ni(3)-) Sariq. naymej-/naymi/üg ‘to hide, conceal; conserve’ 

*MISC: Arab. (LW) muq, Syr. (LW) шода, Arm. (LW) moyk ‘shoe’ || (+ *pati-) 
Arm. (LW) patmucan 

9 The root may have initial *h- (< IE *s-), which depends on YAv. paitismux-, with 
a strange ("ruki") -$-. This root *(h)mau¢ is identical with *mauë! ? 

*PIE ? 9 No exact IE cognates are known, except for a corresponding "unenlarged" 
root in Lith. máuti ‘to put оп, don’, which is to be separated from máuti ‘to rush, tear 
along’. © LIV: 445 | Pok.: 743 


140 *hrab 


*REFERENCES: GMS: §848, 858; Abaev, Slovar’ П: 373 Ё; EVS: 48b, 56b; DKS: 201b; Skjarvo, MP 
Impf.: 163 ff.; Steblin-Kamenskij 1999: 270; Cheung 2002: 218 


*hrab ‘to sip, suck (in)’ 

*CHORESMIAN: (+ *uz-) ? mžß- ‘to absorb, sip, suck in/out’, m/rBY- (sec. tr. ?) ‘to 
squeeze, press out’, m/ZBs- (pass.) ‘to be squeezed, pressed out’, m/Znb- (sec. caus.)
```


## [2026-09-07T17:41:02.244Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN leaf 242 (p.221) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==243' HRN.txt | head -50",
 "description": "Read Horn page 221"
}
```


### [2026-09-07T17:41:03.406Z] TOOL RESULT

```
=== HRN leaf 242 (p.221) ===
— 221 —
Ved. Stud. II, 19); phlv. magu, magupat (arm. LW.
mog^ mogpet, movpetan movpet), daneben maupat (syr.
LW. NtOSID, daraus gr. Mavlnväg d. i. Mavmxäg und
Mavinvüv&d d. i. Mavmvovx^ä, Nöldeke, Karnämak
59 Note 4); ar. LW. majüs (Plur.).
985. mey 'Tiefe, Fluss''), meyak 'Graben, Grube* (Sahn. I,
174 Vers 817).
aw. maya- 'Loch'; phlv. may,
986. meyz 'Gehirn*.
Kä§. magz, magzL
aw. mazga- 'Gehirn'; phlv. mazg; ai. majjdn- 'Mark*.
af;'. mayz, Plur. mayza 'Gehirn'; oss. (LW.?) mayz
(174); bei. mazg (229); sar. muig 'Knochenmark', da-
gegen sar. moyz, siyn. mayz 'Gehirn' wohl LW.
987. unuft unbedeutend, umsonst erhalten'.
ai. l/'möC' ^befreien, wegwerfen* (also mtikta- etwas
Weggeworfenes', wie np. Juft aus yuktd-), Darme-
steter, Et. ir. I, 88 Note 2.
Die entlehnten nslov. muhte 'sorglos', serb. mukte,
muktice 'umsonst', ^wwiton^i 'schmarotzen' (Miklosich,
SWAW. Band 35, 129; 37, 86; 38, 176) würden die
ursprüngliche Form dann nachträglich wieder ent-
wickelt haben.
Unsicher.
988. meger 'wenn nicht, ausser, vielleicht'.
me nicht' + eger (No. 106), päz. ma agar (Aog.).
989. meges 'Fliege', jüd.-pers. Mo (Is. 7, 18)«).
aw. vergl. ma/si- 'Fliege, Mücke' ; phlv. magas (vd. 1
^) Den aus dem F§ bei Vullers abgedruckten Sahnämevers
konnte mir Herr Dr. Landauer nicht nachweisen.
') Z statt 8 findet sich dialektisch häufig: z. B. besbäs (AM. 55),
bezhäz oder semärüy, zemärüy oder kusbura^ kuzbura(YvL\\eT8); sepes
(jüd.-pers.) statt zi pes, vergl. si pester (Vullers); Käs. üzü d. i. an
8än; kauk.-bergjüd. zürnai sonst sürnm u. v. a. m. Umgekehrt steht
8 für z im ar. LW. sauswjird *ein Tuch', wörtlich *nadelgefertigt*
(sözengird), de Goeje, Bibl. geogr. arab. IV, 266. Ebenso wechseln
z und s, z. B. /äksi^ -/äkkl (Vullers, vergl. auch ebenda s. v. j^vhe und
```


## [2026-09-07T17:41:12.601Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && awk '/\\[pdf page 10[5-9]\\]/{p=1} p' BQT_v4_pages.txt | sed -n 1,120p",
 "description": "Read BQT vol4 around pdf page 107"
}
```


### [2026-09-07T17:41:13.910Z] TOOL RESULT

```
[pdf page 105]
مغزین خمته
مغزین ۱ - بر وزن قروین » نام نوعی | بمقل بچهای بی مهن وبی‌باك و خواریز وخودشوار
از حلوا باشد . باشد. .
مغزینه ؟ - بر وزن کنجینه » بممتی مغمومه:*۱- با میم بروزن منظومه .
دماغ باشد ۴ . پلفت احل بربر قلیةٌ بادنجان راگویند .
مفکده ۴ - باکاف و دال ابجد بروزن مغناطیی ۱ پلفت بونانی . سنگه
مقبچه » میغانه و شراب خانه راکویند- وخانةٌ آخن‌ربا باشد .کوبند هر که قدری مفتالیس در
آتش پرستان را نیز گفته‌اند . کردنآویز ده اوژ باده ش دق اه۶
وی 0 ی دن! ويزد دهن اوزباده شود وهیچ چیز فرآهوش
وا مقل ۰ < بنت اول بروزن مقل «بستی نکندء ودرد یت را نیز نافع‌است وهمچنین درد
و پای ونقرسرا ۰ چون بن دست گیرند . و کویند
مفلاح « بفتح اول بروزن کجواج , معدن آن در قعر دربا جوم
کوی راگوبند که بجهت کردکان بازی کنند » | است . اکرآرا باآب ۵۸
و وجه تسمیةٌ این گودال بازست چه مغ بمعنی | سیریاآب دهن‌روزم‌دار ِ 1
کودال ولاج (۱) بمعنی بازی باشد . وبکسراول | بیندایندخاسیتش زابل 5
همگفته‌اند ۰ . کردد . وحذی ال مالس ار
مغلاع ۷ - باغین ضله‌دار . بر وزن [ هم بنظرآمده است که
و معنی مقلاج است که گودال جوز بازی باشد. ‏ | مغنطیی‌باشد ؛ وبجای مفناطییس
مغلگاه - بنتح اول بر وزن تختگاء , | حرف دوم قاف هم درست است .
جای استراحت و خوابگاهآدمی وحیوانات دیگر مفند ۱۳- نم اول وثانی وسکون نون
باشد چه مفل بمعنی استراحت, وگاه بمعتی‌جای | ودال ابجد » بمعنی گلوله باشد مطلقاً - وکرهی
ومقام هم‌آمده است ۸ ۰ را نیز گوبند که درمیان گوشت میباشد وآ براغدد
مغلی‌قندز ‎٩‏ - بنم اول ونای وقاف | میگوبند - وهرچیز ممزوج و درهم آمیخته را
و دال ابجد و سکون نون و زای هوز » اشاره | نیز گفته‌اند .

() چك » چش : لا ۰

۱- از : مغز این (پسوند دبت). - از : مغز ۳ ینه (یوند دبت) . "

۴ - باین‌معنی در دساتیر آمده « فرهنکك دساتیر ص۲۹۹ ۴ ۰ ۴ - از : مغل
کده (پوند مکان) . 8 رد4 : مخلگاه . ۹ - رك : مغلاغ . ۷ - رك :
مفلاج . ۸« مفلگاء » جای خفت و جست (خسب . دهغدا) بود ازآن دو وچهار پای.
حمزءٌ عروض ی گوید :

قرارگاه و «غلگاهشان همی ز بهشت بکوهسارکنی و پژرف غارکنی .»
« لغت فری ص ۵۱۱ ۰

‎٩‏ - از: مغلی ( ۳ مغولی )+ قندز (هم.) *- (عر) وت مقموم ( اسم
مفعول ازه غم > ) بمعنی محزون .رك : اقرب‌الموارد . ۱- از یوتانی 33281188168 با
5 210201 , 2122116 (فر)«دزی ج؟ 4 ۹۰ «خب الذخاترص ۶۱۰۰-۹۸

‏۴۳ مفنده (هم.)
[pdf page 106]
سنهنه نفری
مفنده ۱ - بنم اول و ثانی و سکون | ودرم که شیشه کران بکارپرندوآبرا سنکسلیمالی
نون وفتح‌دال ابجد. کرهی و کنده‌ای(۰)راکوبند ۲ کوبند و بگچ رنك شهرت دارد .
که بر اندام مردم از کوشت مانند کردکان شا ۰
بر اندام مردم ان بر مغیاز ۴ - بکر اول وبای ای
میآید ؛ و بسن ی گره و کندهای (۷) کوچك را و 1 دراه
کنته‌اند که درمیان گوشت وکاهی در زبرپوست . رو او ۱۳ زا
اسپل ماهی‌میباشد و بمربی‌غده میگوبند ؛ وبعضی بعاکن وا ی 1 2 ۰
هر گره وکنده (۱) را گویند که در بدن آدمی | 4 ۳31 2 وم
بهمرسد خواه كوچك و خواه بز رکه خواه درد مغیلات - بالام بر وزن سلیمان , بام
کند و خواه درد نکند ؛ بلکه بسنی کفته اند | درختی است خار دار و بعرپی آنرا ام‌غیلان (۳)
کره وکنده (۱) و دلبلی باشد که بیار درد | خوانند ۴ :
کند - مغیلان باستان - کنایه از دیا
مغتی‌ضا ۴ « باسین بی‌قطه بالف کنید, | و روزگار است .
بروزن مه سیما » گلی باشد سیاه.رنگه وآترا از مغیلان گاه - باکاف فارسی بر وزن
کوه کاشان آورند و آن ,مرقدیعا مانند بود - | سلیمان جاه » بممتی مفیلان باستاست که کنایه
و بعتی گوبند سنگی است الوان و بسیار ست. | از ونیا باشد .
بیان نوزدهم
در میم با فا مشتمل بر چهار لغت وکنایت
مفرج گر ان (4) فلا » کنایه از را نی زگویند .
فرشتگان وملالکه باشد - و ستاره‌ها و کواکب مقر س؟* - با را وسین‌بی نقطه وح ر کت
(۷) چش: کندة . () چش : کندهای. () چش : مفیلان ()
(4) چش : مفرح کران .
۹« مفنده . دمل بود که برتن مردم برآید . مجدی ( مروزی ) گوید:
بردار درشتی ز دل خصم بنرمی بردوستی آندر نبد ای دوست مفنده >
لغت قری ص 4۳۳ .۰
مصراع دوم در چاپ اروپا « نزدوستی اندرآآید ای دوست مفنده » وآقای دهخداآبر| چنین صحیح
کرده‌اند : کز پیه (دنبه ) بنضج‌آید ای دوست مفنده؛ درهرحال این‌کلمه وشاهد محل تأمل‌است.
رد : هفند , غند . غنده -
۳ ۳ مفناسیا (عر ) < 332886916 (فر) « دزی اج ۲ ۹*4 * مآخون از ,یودانی
8 لبدل واسکات »۰ کید دمنیزبوم » برنگك خاک سفید. بی‌طمم » غیر قابل حل
درآب .که آترا بمنزلةٌ شد اسید و مپل بکار برند . ۴۳ مصدف « ففیاز » (ه.م.) ‏
بغیاز (.م.) و رك : سراج اللغات بنقل فرهنگه نظام ج ۵ م‌ها . ۴ - رك : ناح‌العروی
چ اس ۱۹۰ «طلح» . 8 - مصحف «مقرتی» (ع). رك : سراح‌اللغات بنقل فرهنگه‌نظام
چ ه ص‌ماً . ورك : مقزنی .
[pdf page 107]
مفلاك ها
غیر مملوم , لوعی از زیب و زیئت باشد که از مقلحان - با حای حطی بروزن‌مفلان,
سقف عمارت‌ها آویزان کنند . بام رودخانه‌است درسرحد ولایت غزآأن - وبمعنی

مفلاك ۱ - بر وزن افلاك . مردم تهی | رستگاران‌هم‌هست. چه مفلح درعربی بمعنی‌رستگار
دست و پربشان و درویش و مفلی و فلاکتی را | باشد » و الف و الون جمع فارسی است-
کوبند .9

بیان بیستم
در میم با قاف مشتمل بر چهارده لغت وکنایت

مقامات در صو آن -کنایه از هعت | تخم کرفی کوعی‌است وآن سیاء وطولانی میباشد
بهشت است. - وآنرا سالیون هم کوبند .

مقام‌مصلا؟ - جابی را کویند که مقدو یه ؟۴ - بر وزن کردونیه . نام
ابراهیم علیه‌اللام درآنجا نما زگزارده بود - شعریت که دارالملك فیلفوی 8 پدر اسکندر

مقدو نس ؟* - بفتح اول وسکون‌دويم | بوده . َ
و دال ابجد بواو کشیده و تون مکسور بین بی مقر ۱ < بر وزن سبر . علفی است که
نقطةٌ زده » بلفت رومی و بحی کونند بیونانی | اسبر ازآن بهم میرسد واصبر دوائیت معروف.

۱ « مفلاك » تهی دست و دروبش باشد . آبوشکور (بلخی) کوید :
از فلکه نها بی بینند آن که باغد غنی » شود مفلاکه .>
« لغت فری ص ۲۷۹ .

این کلمه برساختهٌ ایرالیاست که ظ . از تر کیب « فلکزده > فلاکت و از آن مفلاك ساخته اند
وامروزه باین معنی مفلوك کوبند . رك: رشیدی .

۲ - مصلی » اسم مکان از تصلية , جای نماز « اقرب الموارد » .

۴ -لغت بیزاسی 22866000015108 ۰ پونانی جدید 1338564008191 ( از
06۲۵1۵ (فر) «مزی ج؟ ص۹۰۰ وآن از انواع کرفی‌است . رك : عقار۱۹۹
عربی و فرانسوی . ۴ - بوای ۸12۳640212 ۰ لاتینی 8/126600812 ۸« فرهنکه
لیدل و اسکات» «مرچنت» » ناحیه‌ای‌بود در شمال ونان » که در زمان فیلیپس واسکندر مقدونی
کب قدرت بیار کرد وبونان را تحت 7سلط درآورد » ولی در۱۶۹ ق.م. جزوایالات روم کردید.
اکنون بدین نام. ناحيةٌ واقع بین پیندوی, الیمپوس, تالی» وردیه را بدین نام نامند که در تحت
تصرف یونان » بو کوسلاوی و بلغاری است . - مصحف « فیلفوی > . رك : فیلقوی .

- « صبر( بفتح اول وکسر دوم ) . هوعمارة النبات الذی بعرفه العامة عندنا بالسبارة,
و اسم ذلك النبات بالمربية المقر » و بالیونانی الوی .» «* عقار ۳۱۸ * ۰ بونانی 2[08 * 5غ810
```


## [2026-09-07T17:41:32.298Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && grep -n \"مفت\" BQT_v4_pages.txt | head -20; echo \"=== v3 ===\"; grep -c \"مفت\" BQT_v3_pages.txt",
 "description": "Grep BQT for موفت/مفت"
}
```


### [2026-09-07T17:41:32.364Z] TOOL RESULT

```
411:بپدل شود . - م ( مفتوح ) 132 چون برسر فعل امر درآید : نهی سازد : مکوه مخور ء هزلیده
444:و رای بی نقطةٌ مفتوح بنون وکاف فارسی زده » ماخ - پسکون خای نقطه‌دار ».زر قلب
1238:بی نقطةٌ مفتوح بکاف زده » بمعنی چکاوك است |[ وبعربی ابوالملیج خوانند ؛ و بسن ی کوبند مرغی
1309:ومرقیون‌مطلم گشت, هنکر مذهب مفتله کردید . مانی‌چند بارمکاشفاتی یافت و فرشته‌ای اسرار
3207:مار وعقرب را نافع است . و نون مفتوح بکاف زده . نام دوائی است که
3572:مسقق - بنتح اول و ثالت بواو رسیده . | و فوقائی بتختان ی کشیده ومیم مفتوح بنون ودال
3687:کردی 7881 ( مفت ) « ژابا س ۳۹۸ کردی ع 3389121 ( مشت ) « ژابا س ۳۹۹ >
3689:۸ - رك: مت . هسته - ‎٩‏ -مفت بکراول » جوی آب :
3772:هت ۱. خای نقطه‌دارونون مفتوح, درفرهنگه جهالگیری
3971:و كوچك و صد برکه وخوشبوی, ووفادار ازآن ] نون وکاف فارسی مفتوح بکاف نازی زده, بممنی
4155:مقبچه » میغانه و شراب خانه راکویند- وخانةٌ آخن‌ربا باشد .کوبند هر که قدری مفتالیس در
4353:وکاف مفتوح بفا وفوقانی‌زده . بممنی رنج وآفت [ خواندد -
4567:مرحوم فزونی نیز پیش از انتشارکتاب مز بور » همین بود) « النصاری مفترقون فرقاً: فالاولی‌منهم
4595:از رستم زال هم هست و او پادشاء سیستان بود - | الون و جیم به تختانی کشیده و دال مفتوح بنون
4804:و جیم مفتوح بخای نقطه دار زده » سنگی باشد هنجل - بکر لول وفتح ثالت وسکون
4858:8 9 3 نقطهٌ مفتوح ء بلغت خم لقاح بری است
5091:جنگی ودلاور میشود وفیل سفید لیز درآنجا #م | دوم مفتوح هردوفارسی بروزن زن برادر؛ به‌منی
5490:‎-٩‏ تیرتو مفتاح شد درکار فتح قلعه‌ها تبرتو مومول شد در دیده‌های دیده بان .
5817:8 - ( مر ) « مهرای » بروزن مفتاح بانه و هاونی است که کوییده میشود پاوکندم -
5878:حرف رابع جیم مفتوح هم گفته‌اند ۴ (۱) مهردهانان ۸ - کنایه ازروزهداران
=== v3 ===
55
```


## [2026-09-07T17:41:37.391Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && awk 'NR>=3600 && NR<=3700' BQT_v4_pages.txt | grep -n \"pdf page\"; echo ---; sed -n 3650,3700p BQT_v4_pages.txt",
 "description": "Read BQT v4 around line 3689"
}
```


### [2026-09-07T17:41:38.689Z] TOOL RESULT

```
17:[pdf page 92]
59:[pdf page 93]
94:[pdf page 94]
---
۸ * ممقوره. لغت«غربی‌است ۳ 10082 2718101061218. این البیطار آنرا اسپانیولی
۱ عجمية الاندلی) میداند . رك : دزی ج ص 0۹۳. « زراوند ... واسم الزراوند بالیوتانی‌ارسطو-
لوخیا و بمجمية الاندلی قلبجوله وبالبربرية مسمقوره . وهوشجرة ابن رستم . و هوالزاثرة » واسم
الطویل منه ایا شجرة الخطاطیف . » « عقار ۱۳۳ * . موه بربری لیست » بلکه اسپانیایی
است (072ع128708) ه ۸۲9101006 (ض) (10082 6۲ ۲۵۱2۵42 ونطم0[0 )یا ه)
« عقار ۱۳۳ ی > ‎٩‏ - (عر) « من » بکر میم فان و آنچه بدان کارد و مانندآن
را نی زکنند.» « منتهی‌الارب ». *- چه جم را سلیمان پنداشته‌اند وطبق داستانها بادمسخر
سلیمان بود وسلیمان بن مرکب باد می‌نشست و برهوا میرفت . ۱- رك : رشیدی .
[pdf page 93]
بنیون مه
مسیفیون (۱) - بفتح اولوتانی بتحتانی] زده . بلفت پونانی شنجرف را گوین د که مصوران
رسیده و کسر نون وبای حطی بواوکشیده وبنون | ولقاشان بکار برند -
بیان پانزدهم
در میم با شین نقطه دار مشمّمز برهفتاد و دو لغت و کنایت
مشاش - بنتح اول و ثانی بالف کشیده بمعنی آنبوه و بسیار وپر و لبریز وسطین وکنده
و بشین نقطه دار زده » انگبیته () را کوبند | وغلیظ باشد ۴ - ونام قربه‌ایست ازبلوکات غزنین
وآن علی‌باشد قوام داد که برطبق ریزند وپهن | نزديك بموضع سکانه که‌آتهم ازقرای‌تزنین است
"کنند تا سرد شود وسخت کردد و دروقت‌خوردن | - و جنم اول . معروف است که گره کردن پِنجةٌ
دندان گیر باشد ۱ - و منع از شاشیدن و بول | دست باشد وجمع نمودن انگشتان چنانچه پنجهٌ
کردن هم هست ۲ - و جنم اول؛ درعربی زمین | دست ظرفیت بهم رساند * - و مردم کم و قلیل
نرم ونفی وطبیمت و استخوانهای نرمی که ثوان | وگروه اندك را نیز کوبند ‎٩‏ - و بمعنی مالید
خوردن ۴ . هم آمده است که ماضي مالیدن باغد چه مشتن
مشبگ قلعه - کنایه ازمجمره و عود | بمعنی مالیدن است ۷ - و بیخکیاهی هم هت
سوز است - وکنایه ازآسمان هم هت . خوشبوی که‌تخمآ نرا تودری‌خوانند ۸‏ وبعربی‌سعد
هشت - بفتح اول وسکون ثانی وفوقانی, | کوبند ‎٩‏ -
(۱) چك » چش : هسینون . (۷) چش : آبگینه .
۱-« مدخته . حلوایی بود صافی و درشت » بتازی آنرا مشاش خوانند . چین درچین
بود .» « لغت فری سس 20۵۸ * » ولی در قاموسهای عربی دیده نشد . رك : مشخته , انگیینه .
۴ رد :شاشیدن . ۴ - رك : منتهی‌الارب » اقرب‌الموارد.
۴ -کردی 19 ( فراوان ) « ژابا س ۳۹۹ ۰ در اراك ( سلطانآ باد ) 132581 و
15 ( پر ولیریز ) « مکی‌نژاد» :
آزرقی دیو چهر بژ مه رنگه از بدی مشت و از هجیری ونگه.
شیخ سودان « جهانگیری »3 رشیدی >.
* - پهلوی 3351 (مشت : قوت) « نیب رکه س۱۵۳* ۰ اوستا 77205011 ( 718011
) [ باندازة يك قبضه ] «* بارتولمه ۱۱۸۹ >, هندی باستان. ]1315121 ۰ مازندرانی
8 . افنابی ۳۶1 ۰ ۵4 ۰ بلوچی ع 130501 ۰ وخی 133086 ۰ سربکلی 3316 «اسشق
۲ ارمنی ع 9016 ( دسته » بته ) » قس : پهلوی 670181011۴ « هوبشمان ۹۸۲*»
کردی 7881 ( مفت ) « ژابا س ۳۹۸ کردی ع 3389121 ( مشت ) « ژابا س ۳۹۹ >
۹ -کوبند : يك مشت مردم بیچاره و مفلس . ۷ -ر4 : هعتن .
۸ - رك: مت . هسته - ‎٩‏ -مفت بکراول » جوی آب :
باز جهان کشت چو خرم بهشت خوید دمید از دو بناگوش مشت .
« منوچهری دامغانی ی ۱۳۹ > ورك : جهانگیری » وشبدی .
( برهان قاطع ۲۵۴ )
[pdf page 94]
-7۱۱- متت‌رنده
هشت آ تشی - بکس ثالك ,کنایه از | گوبند که از انگور پیش‌رس رسانیده باشند ۴+
ظالمان و ظلم کنندگان است - و آنش پرستان | و آنرا باسطلاح شراب خواران شراب جهودی
را هم میگوبند . گوبند و بلفت اهل شام مطار خوانندء وبحذف
مشتاسنف < پبروزن‌مرداستگه,سنگه | همزه هم‌آمده است.
فلاخن راگویند وفلاخن چیزی ازیشم باشد بافته | اهشت خاله * « کنایه از کرة ارض
شده که شبانان بدان سنکه اندازند - ۶ سنکه | است - وکنایه ازدتیا هم هست - وآدمی را نیز
```


## [2026-09-07T17:41:50.089Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && grep -n \"برهان قاطع\" BQT_v4_pages.txt | sed -n 1,40p",
 "description": "Find BQT v4 page footers"
}
```


### [2026-09-07T17:41:50.145Z] TOOL RESULT

```
30:کلیه حقوق‌تجد ید طبع کتاب برهان قاطع باتصمیمات وحواشی و
40:برهان قاطع بر آمد این‌فرهنگ‌را که درایران وممالك‌هسایه
269:‏۷- تصحیح.برهان‌قاطع این ك که دور کامل برهان قاطع مصحح
288:دربارهٌ مطالب مجلدات چپارگانة برهان قاطع مستقیماً به عنوان نگارنده
737:( برهان قاطع ۲۴۵ )
1062:(برهان قاطع ۳۴۱)
1412:(برهان قاطع ۲۳۷)
2031:(برهان قاطع ۲۴۹)
2447:دای «یزی ج۲ ص۵۸۵ وهم دزی کوید ( ایا ) : اشکه دربرهان قاطع ( وفولری )
2703:(برهان قاطع ۳۵۱)
3011:( برهان قاطع ۲۵۲ )
3359:(برهان قاطع ۲۵۳)
3692:( برهان قاطع ۲۵۴ )
4034:(برهان قاطع صه۲)
4346:( برهان قاطع ۳۵۹ )
4646:(برهان قاطع ۲۵۷)
5279:(برهان قاطع ۲۵۸)
5613:( برهان قاطع ۳۹۰ )
5970:بر میشود: وزرشتیان نیز این روز را جشنگیرند . ( برهان قاطع ۲۵۸ )
6293:(برهان قاطع ۳۲۹۳)
6705:از کناب برهان قاطع در حرف نون با حروف تبجی مبتنی
6913:(برهان قاطع ۲۹۴)
7574:( برهان قاطع ۲۹۹ )
8552:( برهان قاطع ۲۳۹۵ )
9158:( برهان قاطع ۳۷۱ )
9455:(برهان قاطع ۳۷۳)
9778:.خاس داشته‌اند . (برهان قاطع ۲۷۳)
10451:‏(برهان قاطع ۳۷۵)
10997:س ۲۱۷) و« جشن بز رکه » ( برهان قاطع ) و * نوروز ملْك > (شرح بیست باب ملامظفر)
11465:(برهان قاطع ۲۷۸)
11770:( برهان قاطع ۳۷۹ )
12270:فری. » جهانگیری » رشیدی » برهان قاطع وانجمنآرا نيامدء و درموضع دیگر درنظم وش دیده
12443:( برهان قاطع ۳۸۱ )
13081:( برهان قاطع ۳۸۴ )
13791:* مخزن الادوپه ۶ , رٍك : اکي , ( برهان قاطع ۳۸۵ )
14775:(برهان قاطع ۳۸۸)
15107:(برهان قاطع ۲۸۸)
15579:از کناب برهان قاطع در حرف های هوز با حروف تبجی
15755:(برهان قاطع ۲۹۱)
16441:( برهان قاطع ۲۹۳ )
```


## [2026-09-07T17:42:10.562Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && awk '/\\[pdf page 62\\]/{p=1} /\\[pdf page 65\\]/{exit} p' BQT_v4_pages.txt | head -100",
 "description": "Read BQT v4 pdf pages 62-64"
}
```


### [2026-09-07T17:42:11.901Z] TOOL RESULT

```
[pdf page 62]
-۱۹۷۹- مراش
وبسی گویند هرمری پنجاه است چه صد رادومی مراد - پکر اول بر وزن فاد دم
و صد وینجاه را سه مر خوانند ۱ - و از جملةٌ | اسنگی باشد بسیار عجیب و از حرکت آقتاب
کلمات زایده هم هست که از برای حسن کلام | الوان مختلفه درو ظاهر میگردد یمنی هر سامت
آورند چنانکه « من او را گفتیم » و« من اورا | برتگی مینماید و آترا بلغفت سر‌بانی سروطالیس
دیدیم» پمنی با وگفتیم واورا دیدیم ۴ - وکاهی | میگویند بمنی سنگه پرنده زیرا که در هوا از
افادة معنی‌حصرهم میکند چنانکه کفته‌اند: مر | بغار لطیف متولد شود وباد آبرا ازجعتی بجهتی
او را رسد کیربا ومنی > یعنی دیگریرا نمیرسد | افکند . کوبند مادام که آفتاب فوق‌الارض باشد
و با تقدید ثانی در عربی بمعتی مرور کردن | هرکه‌آن سنکه را باخود دارد شیاطین تابع وی
وگذشتن برچیزی وازجاییباشد۴ - وبمعنی‌شمار | میشوند - وجنم اول, درعربی‌بمعنی خواسته شده
هم هست . باشد ۴ .

مراحل فشهن -کنایه از هر يك از هراد * « بفتح اول بروزن هزاره نوعی
کوا کب سبعهٌ سیاره باشد که قمر است و عطارد | از باد آورد و شکاعی باشد که بمربی ش وکةالبینا
و زهره وشمس ومریخ ومعتری وزحل -ومافر | خوانند و آن هم بوتة خاری است سفید که در
را نیز کوبند ؛ و مراحل نشینان مجموع هفت خاصیت کار بادآورد میکند .
کوکب - و مافران . همراش - یکی اول بر وزن خراش ,
‎٩‏ مر ما مرامن حاب الممر چون به ینجه رسد حاب » «مر» است.
« خاقانی شروانی ص ۹۷ .۰
مر بود پنجاه وچون‌آمد دو مر ابیات‌آن در صفا و محکمی شای دک ه کویم مر مراست ‏
جامی « جهانگیری » .
سراج‌آرد : «فوسی کوید که این حابی‌است که جولاهان در شمردن تارهای کربای کنند و گوبند
که این کریای چند « هر » است واین اقوی است چرا که محاسبان عقوداعداد مقر رکرده محتاج

باسطلاح دیگرنیستند مگراینکه مراد ازمحاسبان غیر از اهل علم حاب باشند . » (سراح‌اللفه)

بنقل فرهنگه نظام >. ۴ مر 87 اداتی ( 087110116 ) که پیش از مفعول درآید :
عرآن زخم گرزش که بارد چشید ؟ ( فردوسی ‎ )‏ مراو را رسد - ولیز ممکن است با مسندالیه

(با فاعل) استهمال شود : مراو هت پروردة کرد کاره دارمستتر . تتبغات اج ۱ص ۴۱۳۷ » ولیز :

بدل گفت اکر جنگجوی ی کنم به پیکار او سرخروبی کنم
بگربند هر دوده و هیهتم که بی‌سربه‌بینند خسته تنم
عنصری بلخی « لفت فری ص ۰۳۹۰

و رل:: مقدمة کتاب حاضر مس لد. ۴ - رك : منتهی‌الارب . اقرب‌الموارد .

۴ - اسم مفعول از آرادة . ۵ - 2/1076 ۰ 8 (فر) « دزی‌ج

۷ ی ۷۷ » مرار چم اول و تشدید ثالی » اسم عربی خاریست که در آخر بهار میرسد و در
مص «مر‌بر» و ۶ دردریه * نامند . برکش مانند بر که چفندر و مابل بسیاهی وملاسق زمین ودر
تابستان مانند درخت شعبه‌ها از يك بیخ میروید وگلش زرد و درآخرخاردار و شبیه بشکاعی‌میشود
و دران تخمی مانند تخم کافشه وبسیار تلخ وقوتش تا چهار سال بای است» و ساق او را پوست باز
کرده میخورند ومنیتش‌میان زراعات وجای دمناك (است) > «تحفةٌ حکیم موّمن» ورك: ابن‌البیطار.
[pdf page 63]
مراغه ۱۹۸۰۳
بممتی ی باشد و آنرا شکوفه و استفراغ هم | از راندن هم‌هست* - ویضم اول » نام درختیست
میگوبند ؛ و باشمعنی بحذف الف نیزآمده‌است | باريك و درا ز که ازچوب‌آن نیزه وتیرسازند ‎٩‏ .
که مرش باشد ‎٩‏ . مرافیه ۷ (۷) - بروزن علایه (۷) ۰
هراغه - بفتح اول وغین نقطه دار, | بلفت اهل‌مقرب درختی‌است مانند درخت باسمین
نام شهری است از ولایت آذربایجان ۴ - ویمعنی | و آنرا عربان هوم(۳)المجوس ۸ کویند » چه
غللدن باشد عموماً و غلطیدن اسب واخر را | مجوس دروقت‌زمزمه یعنی‌وقنی کهستایش وعبادت
کوبند خصوصاً » و در عربی هم بممنی غلطیدن | کنند و چیزی خورند شاخی از*آن در دست
[ تا کیرند . سنگه مثانه را بربزاند وبول را براند.
۹ مران » بنتح اول بروزن سران » بمعنی مر بع خانه نور- کنایه از خانة
آنست که آشاره بچیزی دور باشد و بلفظ مرکه | که است .
ازجملهٌ الفاظ زایده است ملحق شده ۴ - ومنع مر پویا* » بنتح اول و سکون نانی

(۱) چش : مراینه - (۲) چش : علاینه . (۳) چش : ههوم !

۹ - « مراش » مصحف « هرا > ( «.م. ) است » و «رش عربی است . « مرش بالفتح
خراش وزمین که روش باران رندیده باشد باآنکه باندك باران روان گردد » امراتی جمع... ونیز
مرش خراشیدن و سودن برانگشت و بسخن رنجانیدن کی را .» * منتهی‌الارب » .

۴ - تاحیه‌ای باآنربایجان درجنوب سهند و جنوب شرقی درباچة ارومیه در دره‌ای بسیار
حاسلخیز ویرآب واقع شده . ارتفاع آن از سطح دربا ۱/۳۹۰ متراست. مرکز آن شهر قدریمی
مراغه در کنار صافی رود است . در اطراف شهر مراغه ۷4 قربه است که جمعیت آنها ۳۲۵۰۰
تن است «کیهان . جغر‌افیای سیاسی ص ۳-۱۷۲ > - ونیز عراغه نام دیهی است درایرقوه « ایا
می *1۶ بئقل از تزهة القلوب >. ۴ - باین معنی مأخوت ازعرپی است : « مراغة كمحاية,
جای غلطیدن ستور > « منتهی‌الارب » و فارسیان بمعنی مطلق غلطیدن استعمال تمایند «بهار عجم»
« مراغه , غلتیدن باشد . عنسری ( بلخی ) کوید :

چون مراغه کند کی برخاك چون بود (شود؟ دهغدا) خاك او چه دارد باك .>
و رك : چهار مقاله چاپ دوم تگارنده ص۳۰ یوج * لفت فری ص 24۷ >

۴ - از :هر («.م.) ۳ آن ( ضمیر و ام آشاره بدور ).

* - نپی از راندن (ه.م.) ۹« مران » بفتح اول و تشدید ثانی » درختی است
در بلاد مغرب وروم وهند» و جمیعم‌اجزای اوتلخ وبسیار بلند ورعنا ونرم ‏ و گرعهایی مانند بندهای
نی و میان پر » و از آن نیزه سازند و مشهور بتیزه نی است ...۲ « تحقة احکیم مومن > <
۸اع۵۶ 00۲۵5 ؛ ۲عنللژه 6۵۲2 ( فر ) « دزی ج؟ ۰۲۵۸۵

۷ - درتحفةٌ حکیم موّمن « مراتیا > درنخه‌ای * مراهه > . ودر تذ کرء ضر براتطا کی
« مرائیه > ( ج۱س۵۸ ) ود مزانیه » ( ایا صس ۲۹۱ ) و در دزی ( ج؟ اس 0۸0 ) «مرانیه»
آمده » و همه ظاهراً مسحیف «* پراهه > ۳ پراهوم است . « پشتها اص 2۷۱ ح ۷ ( با استفاده از
افادات شفاهیآقای پورداود) > ورك : هوم . ۸ -ععل ,فهق218 وعل هصسو‌قط ما
دای «یزی ج۲ ص۵۸۵ وهم دزی کوید ( ایا ) : اشکه دربرهان قاطع ( وفولری )
ان کلمه را مغربی دانسته بدون بشغك , خطاست . ورك : وم .

۹ - هز . 2ل(13)8(۲0۵ ۰ پهلوی 38700621۳ ( خربزه ) ۸« بونکر ص ۱۱۹ ۰
[pdf page 64]
-۱۹۸۱- مرجان
و بای آبجد بواو رسیده ویای حطی بالف کشیده, مرج - بغتح اول وسکون نانی و جیمء
بلفت زند وپازند (۱) بمعنی‌خریزه شیرین باشد. | بمعنی مرز است که زمین باشد ‎٩‏ - و زمینی را
ودر نخةٌ دیگر خربزة میان دربا ۱ نوشته شده | نی زکویند که کنارهای آنرا بلند ساخته دردرون
بود ویرهیج يك شاهد تیاورده بودند » ااعلم . آن چیزی بکارند (۷) - ونام شهری هم هست در

مرت - بفتح اول وسکون ثانی‌وفوقانی. | کوهتان سمرقند ۷ ؛ وباین معنی چم اول لیز
بمعنی زنده باشد که درمقابل مرده است ۳ . آمده است - ددرمر ی بمعنی‌ازهم کشودن وبچرا
```


## [2026-09-07T17:42:33.871Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -c \"\" MON_part1.txt MON_part2.txt; echo \"=== آموختن ===\"; grep -n \"آموختن\" MON_part1.txt | head -10; echo \"=== مفت ===\"; grep -n \"مفت \" MON_part1.txt MON_part2.txt | head -10",
 "description": "Grep Mo'in for amuxtan and moft"
}
```


### [2026-09-07T17:42:33.970Z] TOOL RESULT

```
MON_part2.txt:94500
MON_part1.txt:99339
=== آموختن ===
4806:قس. آموختن] (مسصم ِ( تسعلیم دادن 
4807:آموختن. 
4809:آموختن) عمل آموختن» یاد دادن. تعلیم) 
4814:دوسند ز آموختن. 
4863:آمیختن: «داسة [- آموختن - آمیزبدن] 
9190:دادن آموختن به کسی» به باد کسی آوردن» 
15300:کردن. آموختن» فرا گرفتن. (بع.) آوردن 
15467:کردن خوانا گردانیدن؛ خواندن آموختن. 
16231:آموختن. فرازبان دادن. افکندن» درانکندن. 
37170:آموختن» فرهنگگ پذیرفتن» ادب آموختن. با 
=== مفت ===
MON_part1.txt:6091:خدا. همفت تنان» سرهنگان درگاه حق. 
MON_part1.txt:19849:آن را بیاورد. چیزی که مفت و بی‌تعب 
MON_part1.txt:29540:گرانجان. مفت خور: گداء انگل. داماد. 
MON_part1.txt:46651:مفت و باوه گفتن. جاروت از مذگان کردن: 
MON_part1.txt:75929:کشتی که باروبنهٌ شاه را مفت و بدون 
MON_part1.txt:88915:(جستن» یافتن): مفت و رایگان یافتن. از 
MON_part2.txt:10545:سختی و اشکال افتادن. قافيةٌ را باختن (مفت 
MON_part2.txt:19612:کانفت؛: ۱ [- کامفت ِ قامیت ِِ قانفت 
MON_part2.txt:19613:- غامفت (معر. متر)] (.) شیرینی مانند آب 
MON_part2.txt:24626:وی (کد.) مفت و آسان
```


## [2026-09-07T17:42:37.110Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n 4795,4825p MON_part1.txt",
 "description": "Read Mo'in amuxtan entry"
}
```


### [2026-09-07T17:42:37.160Z] TOOL RESULT

```
خواهد اموخت. ساموزء آموزنده. آموخته. 
آموزش). (مصل.) فرا گرفتن» یاد گرفن» 
تعلم. (مسصم.) فرا یاد دادن تعلیم» 
آموزاندن. 
آمودن: 2۳01-27 [قس. آمادن] (مسصم.) 
آمیختن» درهم کردن. . ترصیع» در نشاندن 
چنانکه گوهری را در انگشتری. به سلکك 
درآوردن؛ به نخ کشیدن گوهرها و مهره‌ها. 
آراستن» زشت کردن. سهیا کردن» آماده 
کردن. (مصل.) آميخته شدن. آراسته شدن. 
امو زانیدن: مدلآصعتاهة [- آموزاندن < 
قس. آموختن] (مسصم ِ( تسعلیم دادن 
آموختن. 
آمسوزش: 27024 (اسص. آموزیدن و 
آموختن) عمل آموختن» یاد دادن. تعلیم) 
مق. ترییت» پرورش. 
آموزشگاه: 2.0 (امر.) مدرسه (فره.) 
آمتو ره : 1-.8 (ص‌نسس..) منصوب به 
آموزش. تعلیمی» تعلیماتی. طالب علم؛ 
دوسند ز آموختن. 
آموزگار: ۲-(30102)6 (ص‌شغد.) آنکه 
آموزد» آنکه باد دهد» معلم آموزنده. (فر.) 
معلم مدرسةٌ ابتدایسی. سامح اندرزگوی. 
راهنما؛ هادی. شاک د) مت 
آموز رنده: (6-)202-2002 را آمو حتن» 


۳ فرهنگ فارسی معين 1 


آموزیدن) آنکه به دیگری آموزده آنکه
```


## [2026-09-07T17:42:43.836Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n 4770,4800p MON_part1.txt; echo \"=== nearby page footers ===\"; awk 'NR>4600 && NR<4900 && /فرهنگ فارسی معين/' MON_part1.txt",
 "description": "Read Mo'in amuxtan headword"
}
```


### [2026-09-07T17:42:45.402Z] TOOL RESULT

```
سیلیکات‌های آهن و منگنز می‌باشند. 

آمفی تأتر: ([< آمفی تثاتر ] (امر.) 
جای نشستن تماشا کنندگان در تماشاخانه‌های 
بونان و روم قدیم که ردیف‌های آن به 
شکل دایره با مضی و دارای پلکان بوده و 
صعنه در وسط آن جای داشته است. امروزه 
هم این سبکث در بعضی ممالکک مستعمل 
است. 


آمن: 20( [ع.] (ص‌تفض..) استوار تر» 


یمن تر. 
امن: 2 [ع.] (افا.) بسی‌بیم) سی‌خوف» 
ایمن» به زینهار» در امن و امان» ج. امنون» 
امنین. 
آمنه (0-)210202 [- امنه] (ا.) پشته هیزم» 
بشتوارة هیزم» توده خرمن هیزم شکافته 
تس اتاصة (.) اشتان مرغان شکاری 
مانند باز ر عقاب» آشیانه. 
آموختگار: 20010 (ص‌فا.) معتاد به» 
چشته خور» سته‌خوار. 
اموختن: محا-ستنعة ( آموخت» آموزده 
خواهد اموخت. ساموزء آموزنده. آموخته. 
آموزش). (مصل.) فرا گرفتن» یاد گرفن» 
تعلم. (مسصم.) فرا یاد دادن تعلیم» 
آموزاندن. 
آمودن: 2۳01-27 [قس. آمادن] (مسصم.) 
آمیختن» درهم کردن. . ترصیع» در نشاندن 
=== nearby page footers ===
۳ فرهنگ فارسی معين 1
```


## [2026-09-07T17:42:59.236Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KNT amutha ===\"; grep -n \"amuθa\\|amutha\\|amu(n)θa\\|amuu\\|flee\\|fled\" KNT.txt | head -25",
 "description": "Grep Kent for amutha"
}
```


### [2026-09-07T17:42:59.301Z] TOOL RESULT

```
=== KNT amutha ===
2436:‘he runs away’, OP imf. ати"ба* ‘he fled’, and
3649:§20. 2.1-5. Saith Darius the King: After that, Nidintu-Bel with a few horsemen fled; he went off to Babylon. Thereupon I went to Babylon. By the favor of Aburamazda both I seized Babylon and 1 took that Nidintu-Bel prisoner. After that, I slew that Nidintu-Bel at Babylon.
3679:this Phraortes with a few horsemen fled; a district, E! by name Raga, in Media—along there he went off, — 5
3788:642. 3.40-9. Saith Darius the King: After that, Vahyazdata with а, few horsemen fled; he went off to Paishiyauvada. From there he got an army; later he came against Artavardiya to join battle. A mountain by name Parga—there they joined battle. Ahuramazda bore me aid; by the favor of Ahuramazda my army smote that army of Vah- yazdata exceedingly; of the month Garmapada V days were past—then the battle was fought by them, and that Vahyazdata they took prisoner, and those who were his foremost followers they captured. .
3807:—he fled with a few horsemen (and) got away. A fortress by name Arshada, in Arachosia—past that he went. Afterwards Vivana with his army went off in pursuit of them; there he took him
5755:таш- vb. ‘flee’: meaning established by Мат. and АКК. versions (Hüsing, KZ 38.258); probably to Skt. munthate ‘flees’ (Jn. JAOS 38.122). атида imf. ($211) DB 2.2, 71; 3.41f, 71.
```


## [2026-09-07T17:43:10.339Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n 2430,2440p KNT.txt; echo \"=== IEC ===\"; grep -n \"^meu\\|^meug\\|^meus\\|^mūtro\\|^muk\" IEC.txt | head -20",
 "description": "Kent context and Mann grep"
}
```


### [2026-09-07T17:43:10.393Z] TOOL RESULT

```
pIE *ueid-ne-/-no- in OP vainamiy Ч see’, 3d sg. vainatiy, mid. vainataiy; Skt. véndm? ‘I desire’, vénati, vénate. $211. Tug PnEsENT-TENSE SYSTEM OF TYPE
Lavin jungit: the stem is the root in zero grade,
with an ablauting infix -ne-/-n-: Skt. yu-ná-k-&
‘he joins’, pl. yu-fi-j-dnti, to root *eug-/*iug-. In
some languages the paradigm is leveled to the
form of the plural, and the stem is made thematic; thus Latin jungil, jungunt. This is the situation in the Aryan root *mauth-, Skt. pres. munthate!
‘he runs away’, OP imf. ати"ба* ‘he fled’, and
probably in Ar. *pais-, Skt. pres. рін, OP 3d sg.
imf. ара" (DSf 54).
The same formation is seen in Skt. vi-n-dáti ‘finds’; the present participle OP vi"dat- is seen as the prior element of V«dafarnà ‘Intaphernes’.
$212. Tux PnEsENT-lzNsE SYSTEM OF TYPE
=== IEC ===
10728:meur- ‘ant’. (Variant of type mour-, q.v. Ambig. in Iran. & Cor. Cf. mur- (1) (muruis, murəuis)) Av. maoiris, Per. mür (and mürce, dim. type), id.; Cor. muryon, pl. ‘ants’; Br. cf. mérien, Vannic mérion, pl. id. (vocalism?); Du. mier, f. ant: G Miere, f. id., cf. meng, adj. “mag- goty, scabby'
10729:meus- ‘moss, mildew’. Cf. müs- MHG mies, sm. & n. ‘moss’; OE meos, id.; cf. Big. muxál, müxol & mùxla, s. m & f. *mil- dew?
10730:meuó, ið (miuuó, máu, mou-), tr. & intr. ‘move’. WP II, 252. Cf. máu- S kt. cf. a-mivami, pp. -mütab, id.; OPer. mav-, v. ‘send’; Gk. cf. a-meúð, v. “pass, surpass’; Lat. moveo, ére ‘move’; Li. máuju, máuti, pf. móviau “pull; urge; beat; move”
10732:meuos, ios ‘smali, slim’ Tokh. B maiwe ‘small, dainty’; Myc. mewjo- ‘smaller’; Gk. meíon, gs. -onos "less: ON mjór, f: mjó “thin, slim, tapered?
11348:muk- (mük-, munk-) ‘leave’. WP II, 254 Skt. mucámi, muficámi, pp: muktáh “leave, re- lease; Romani mukav, pp: muklo ‘leave, let, allow’; Av. muč- ‘let, release; Tokh. A muk-, mok-, B mauk., v. leave; OCS müécg, ati
11353:muklos (mukulos?) (1) *stammering, jabber- ing; stammer, gibberish; gibberer Gk. müklos, m. (2) ‘jackass’; Li. muklus (2) ‘stammering’; OCS cf. (?) pomüklt, f. (que- ried: ‘restraint? or 'silence). (Skt. mukulah ‘with one eye closed" and mukurah ‘mirror appear to be mere isophones, cf. mük- (3))
11363:muklos, us (2) ‘messy; mess, sludge, marsh, murk’. Cf. WP II, 253 Gk. müklos, m. (1) ‘smear; debauchee'; Li. mukluüs ‘miry, marshy, oozy’; Latv. mukls, id.
11365:muks- (1) ‘snout; pig; grunt, murmur’. Cf. WP II, 310 Skt. mükbam, n. ‘snout, mouth’; Gk. Hes. cf. mukós “silent, soundless'; Ir. muc, f. ‘sow’; W moch, m., Br. mōch, m. coll. ‘pigs’; (Celt. LW in G Mocke ‘breeding sow); G cf. muck- sen, v. ‘make a faint sound, squeak’
11366:muks- (2) ‘worthless, rejected, ba? It. moscio ‘flabby’; Cor. mogh ‘fruitless’; OE cf. myscan, v. ‘injure, offend’; OCS cf. müselü "gotten gain’; Ukr. cf. (?) pry-mxy, pl. (^whims' but see next)
11367:muksa, io ‘fly, midge’. Cf. muksitio, musio, muska Lat. musca, id.; G Mucks, m. ‘midge’; OE mysci, pl. ‘flies’; OCS cf. müsica f. dim. ‘gnat’; R cf. mó$ka, f. dim. id. Cf. (?) Ukr. pry-mxy, pl. “whims but see maks- (2). For Mod. Icel. my ‘gnats: Gk. mua ‘fiy’, see musio)
11368:muksità, iə “small fly, midge, insect. Cf. muksà, etc. (Variant mukst-) OE mohpe, mopbe, f. ‘moth’; Late MHG motte, f.; Du. mot, f. id.; OCS música ‘gnat, midge’; It. moschetta, id. (beside moschetto: Sp. mosquito)
11369:mukso, ið (1) ‘thrust, plunge, insert, force’. Li. ambig. Cf. müK-, muKtis Arm. mxem, v. tr. id.; mux ‘tempered’ beside mxun, id., cf. also mxlCem, v. (plunge, thrust’, fr. *mukslitio or sim.); Ir. cf. müchaim, v. ‘suppress, destroy’; Li. mùšiu, müsti, v. “beat, strike, shatter; mūšis, m. “battle, fight". Cf. mük- below, & cf. MHG müschen (jog; bat- ter”, fr. *muskio); OE myscan, v. "hurt
11370:muksó (2) (?) Gk. cf. müxa 'snot; Lat. muccare, v. inf. ‘snort’; cf. also Gk. mukteér, s. ‘nostril’. (OCS
11374:muktos ‘left, freed, abandoned, loose, dash- ing, rapid’. Cf. muk-. WP II, 254 Skt. muktáh, pp. ‘freed, loose’; Romani muklo ‘freed, allowed; It. cf. motta, f. ‘subsidence’ beside mucciare, v. ‘run away’ (background uncertain), W mwth, adj. ‘rapid’; cf. chwi- mwth, id. (fr. *su1-9; Li. müktas, pp. of mun- kü, mùkti ‘slip, fall, dash, run’; Latv. mukts, pp. of mukt, 1sg. pres. mūku (1) “be absolved, get free, escape’; Cz. cf. (obs.) mektati se ‘fluc- tuate'. (Isophonic: Arm. mtem ‘gather’, but phon. ambig.)
```


## [2026-09-07T17:43:11.810Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LEW mustus ===\"; grep -n \"^mustus\\|^mustum\\|^mūcus\\|^mucus\\|^mucor\" LEW_1910.txt LAT.txt | head; echo \"=== SKT ===\"; grep -n \"^moss\\|^mud\\|^must\\|^mustard\\|^moist\\|^mucus\\|^match\\|^smuggle\" SKT.txt | head -20",
 "description": "Grep Latin dicts and Skeat"
}
```


### [2026-09-07T17:43:11.874Z] TOOL RESULT

```
=== LEW mustus ===
LAT.txt:34462:mustum lixluum, substantivis sons les formes lixluum, et lixluia,
LAT.txt:37202:mustum ad mediam partem decoctum-, cf.fr. mdlasse, M.L.S48at; mellarius,
LAT.txt:40059:mustum ulnum: vin nonvean. Terne de la langue rustique; usiti snrtont
LAT.txt:55392:mustum resipit ferrum) cf .* r esapium, M.L.7337 (la forme sans apo—
=== SKT ===
10941:match  (i),  an  equal,  a  contest,  mar- riage. (E.)  M.  K.  maccht,  maeht,  orig.  b comrade.  *  A.  S.  mmaa^  commonly^mtxirtra, a  comrade,  companiofi,  spouse;  from  the more  original  form  maca^  a  companion. See  further  below.
11985:muddle,  to  confi         ' "  '        ^^ to  diibble  in  mud  ;  h
17589:smuggle,  to  import  or  export  secretly (Scand)  l>An.  tmugU,  to  smuggle;  cf.  1 itfsug,  secretly,  smug-kandtl,  contraband Uadc;  Swed.  imN^,  4  luikia^\x<QNfc«  Vj^
```


## [2026-09-07T17:43:24.086Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in \"mud, wet\" \"moss, a\" \"must, new\" \"mustard\" \"moist,\" \"mucus\" \"match  (2\" \"match (2\"; do echo \"=== $w ===\"; grep -n \"$w\" SKT.txt | head -3; done",
 "description": "Grep Skeat loosely"
}
```


### [2026-09-07T17:43:25.339Z] TOOL RESULT

```
=== mud, wet ===
=== moss, a ===
=== must, new ===
=== mustard ===
=== moist, ===
22532:r  V^^ARDH  (-  VMALD).  to t.  moist,  or  wet.  An  exteasion  of  ^ i,  to  grind  ;  see  no.  363. For  yMAXi,  to  at'ind,  see  no.  163. ).  ^MI.  to  diminish;  prob.  from rlier  form  MA  Hence  Teat,  base to  cut
=== mucus ===
11216:Match  (a),  a  prepared  rope  for  Brtiif cannon.  (F.-L.-Gk.)  M.  £.  macdu* O.  F.  mcscAc,  meicAt  (F.  michc),  wick  of candle,  matiji  to  fire  a  gun,  '  match  ol lampi*  Cot  — LowL.  wyjE3*,nolfoun»Uifl =  Gk.  fiv(a) ;  Low  I^  myxui,  the  .noule  of lamp,  through  which  the  wick also,  a  wick.  —  Gk  /ii'fi.  the  n lamp;  the  more  original  senses mucus  (i)  DOstriL  Allied  to  Mooua match-lcck,  the  lock  of  a  con  hohttof match  i  hence,  the  gun  itselt
11982:mucila^e^  a  slimy  suUunce.  fiik (F -L.)  F.  mueilage.'^-h.  muciU^i^tt^ Muciiagin-\  mouldy  moisture  (4^1  cent) —  T^  mucus  (above).
17654:snot)  mucus  from  the  nose.  (E.  7)  M.  E. snotft.  Not  in  A.  S.+O.  Fries,  tncfte.; Du.  Dan.  snot.    Allied  to  snite  (1)  above.
=== match  (2 ===
=== match (2 ===
```


## [2026-09-07T17:43:25.815Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC mutrom ===\"; grep -n \"mūtrom\\|mutrom\\|'urine'\\|urine\" IEC.txt | head -10; echo \"=== IEC mustos ===\"; grep -n \"^mustos\\|^musto\\|^mudos\\|^mudso\" IEC.txt | head",
 "description": "Grep Mann for mutrom/mustos"
}
```


### [2026-09-07T17:43:25.897Z] TOOL RESULT

```
=== IEC mutrom ===
9071:(1) and Kerið ‘cut, pierce’ Per. sarmā ‘cold’; Alb. tharm, m. ‘leaven; acid’; G dial. harm ‘urine’; Li. šármas ‘lye, alkali’; Sarmà 'hoarfrost'; Latv. sārms ‘lye’; sarma ‘hoarfrost’; (LW in Finn. härmä 'hoar- frost', thus Toivonen, but not Finn. karmea “harsh, rough”, said to be Finno-Ugrian). Cf. Kortos
10064:‘washed’; lotium ‘urine’; beside lautum, sup., cf. ON loór, lauór (“froth”, whence E lather); Mir lóth *washing-trough'; OCS laty, gs -táve, f. ‘pot; Li. luótas, m. "boat"
10116:lóutos, us ‘trough, washbasin, bath’. Cf. lou-, lou-, loutér- & lotos Gk. (ambig.) lotós, m. “Egyptian water-lily’; Lat. lotus, lautus, adj. ‘washed’; lotium, n. ‘urine’; Olr. lóth ‘washtub’; OCS laty, gs lat- üve, f., latva, f. ‘pot beside Cz. lutna, f. ‘trough’; Li. luótas, m. ‘boat’. WP II, 441. EMAlbanian latë “washed” represents a form of type *loutós
10267:mäk- (4) ‘weť. Cf. makoros, maklos Alb. cf. makér, f. ‘uterine fluid’; Lat. cf. mā- cero, are ‘soak’; Slovene mákati, inf. ‘wet; dip; dive’; R makàt, inf. ‘dip’; Latv. cf. mākonis, mákulis *cloud'; (short-gde in) Alb. make ‘scum, sticky film’; OCS modi, f. ‘urine’; moča ‘marsh’; R močà ‘urine’; Li. makoti, inf. ‘plod, squelch’; maknyne, f.; maknotas, adj. ( ‘mire; miry’. Lalis)
10482:meih- (variant: mégh-) ‘urinate; urine’. Cf. moigh-, mih-. WP II, 245 Skt. méhàmi, id.; Oss. mizín, pp: míst, id.; Arm. cf. mizem, id. (LW?); Gk. cf. omeíkho, id.; Lat. méio, ére, supine: mictum, id.: OE migan, sv. 1., Fris. mige, ON míga, id.; cf. OFris. mese, s. (urine', fr. *moighs-); Srb. miam, id.; Li. meZu, pf. myZau, inf. myZti,
10776:migh-, migholos *urine; urinary'. See next. WP II, 245 Oss. cf. mizg, Dig. mezgä penis: Tokh. B migo ‘urine’; OE micge, id. beside migol, adj. ‘diuretic’; Li. cf. mizalai, mpl. ‘urine’; Latv. cf. mizene (“ants”, sense of E *pissmire"); Kurd. ms s. “urine”
11026:moigh-, cf. meigh-, mingh-. WP II, 245 Skt. méhàmi, v. ‘urinate’; mehanam, n. ‘pe- nis; Av. maizom, n. ‘urine’; (Iran. LW in) Arm. mez, mizi, -av ‘urine’; mizem, v. ‘uri- nate; Gk. moikhós, m. ‘adulterer’; (LLat. moium, muium, mugium “penis of animals” is a Gk. LW, see moiuo- below); OE cf. mag, adj. ‘shameless’; Latv. miezu, mizt, v. 'uri- nate’. (OE variant of mág is mah *wanton'")
11485:mtos, à, is, ios, see müt- (3). In the sense of "liquid filth’ cf. also the following Hind. mut ‘urine’; Gk. mütis, gs -idos, f. “ink of cuttle-fish'; Li. mutinjs, gs -io, m. ‘sop, mess'. Cognate forms of E mud include OHG mot, m., MHG mot, sn.; LG modd, m.; G Mutt, m. ‘mud, marsh, sediment! and the Finn. LW muta ‘mud’. See next
11486:mütros (mutoro-) (1) ‘foul; filth, mud, urine’ Skt. mütram, n. ‘urine’; Av. müOrom, n. ‘filth’; Gk. musarós ‘foul, dirty’; MIr. mothar, adj. ‘dark’; m. (1) ‘wooded swamp’; Ir. cf. modar- tha ‘muddy’; MHG moder, m. ‘rot; marsh'; G Moder, n. ‘mud’; cf. muderig, adj. "oft.
12395:Skt. (ambig.) olah, adj. *wet'; Gk. oüron, n. ‘urine’ beside án-auros, adj. ‘waterless’; aüra, f. *water-nymph'; Lat. cf. ürina, f. ‘water,
=== IEC mustos ===
11308:mudos ‘dirt, trash, réfuse’. Cf. smud-, mut-, and WP II, 251. Gk. ambig. Gk. múdos, m. ‘wetness, sap, pus, decay’ (am- big. cf. smud-); MHG cf. muzzen-, cpds. ‘of a whore’; OE mot, n. speck mote’; Du. mot, f. ‘drizzle beside mot, n. ‘dry peat, shavings’; WFris. mot ‘mud, sand, filth’; G cf. motzen, v. “mess, botch’ beside mutschen, v. (*pollute' fr. *mudsK-); ME & E to mottle (extn. w. *-1-); OCS cf. müZdivü 'rotten'; Latv. müdZi mpl. ‘vermin’. (Isophone: Skt. mud, mudå ‘joy’:
11477:mustos (fr.  **mut-tos or **mud-tos?) ‘mouldy, foul; mould, filth’. C£. WP II, 251 and musos (1). For (2) see mustàr-, & for Gk. muttós, cf. mudio. Lat. (isophone?) mustus, adj. ‘new — of wine’; Ir. cf. mos-ach, adj. ‘nasty’; mos-ar, m. ‘nastiness; W mws, m. ‘stench’; adj. ‘rank, stale’; Cor. most, pl. von. m. ‘filth’; cf. mos-ek, adj. ‘smelly’; E must, s. (in sense of ‘mould, mildew’), Sw. must, m. *earthy damp, must
```


## [2026-09-07T17:43:40.099Z] TOOL CALL #52: Bash

```json
{
 "command": "sed -n 1,40p tools/fetch_source.py",
 "description": "Check fetch_source tool"
}
```


### [2026-09-07T17:43:40.138Z] TOOL RESULT

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
```


## [2026-09-07T17:43:44.318Z] TOOL CALL #53: Bash

```json
{
 "command": "for u in \"https://www.etymonline.com/word/mud\" \"https://www.etymonline.com/word/moss\" \"https://www.etymonline.com/word/mustard\" \"https://www.etymonline.com/word/match\" \"https://www.etymonline.com/word/moist\" \"https://www.etymonline.com/word/mucus\" \"https://www.etymonline.com/word/smuggle\"; do echo \"### $u\"; python3 tools/fetch_source.py \"$u\" --note \"page 338, roots Meu 1 / Meug: English node etymologies\" 2>&1 | tail -2; done",
 "description": "Archive etymonline pages"
}
```


### [2026-09-07T17:43:48.551Z] TOOL RESULT

```
### https://www.etymonline.com/word/mud
/home/sfmqrb/git/rishe/data/verification/sources/web/d2ad98c68bea703a.txt
### https://www.etymonline.com/word/moss
/home/sfmqrb/git/rishe/data/verification/sources/web/09513b90f5c78f67.txt
### https://www.etymonline.com/word/mustard
/home/sfmqrb/git/rishe/data/verification/sources/web/7bb7b10d45b67442.txt
### https://www.etymonline.com/word/match
/home/sfmqrb/git/rishe/data/verification/sources/web/b2d652035a8a42c7.txt
### https://www.etymonline.com/word/moist
/home/sfmqrb/git/rishe/data/verification/sources/web/10629468a3aeaa10.txt
### https://www.etymonline.com/word/mucus
/home/sfmqrb/git/rishe/data/verification/sources/web/b3b9f8b49e115c40.txt
### https://www.etymonline.com/word/smuggle
/home/sfmqrb/git/rishe/data/verification/sources/web/0966d4f7533ff784.txt
```


## [2026-09-07T17:43:52.812Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in d2ad98c68bea703a 09513b90f5c78f67 b2d652035a8a42c7 10629468a3aeaa10; do echo \"########## $f\"; grep -o \"Advertisement.*\" $f.txt | head -1 | cut -c1-100; sed -n 1,80p $f.txt | grep -A6 -i \"mud (n\\|moss (n\\|match (n\\|moist (adj\" | head -40; done",
 "description": "Read archived etymonline text"
}
```


### [2026-09-07T17:43:54.050Z] TOOL RESULT

```
########## d2ad98c68bea703a
Advertisement Remove Ads 
 mud (n.) 

 late 14c., mudde , "moist, soft earth," cognate with and probably from Middle Low German mudde , Middle Dutch modde "thick mud," from Proto-Germanic *mud- from PIE *(s)meu-/*mu- [Buck], found in many words denoting "wet" or "dirty" (source also of Greek mydos "damp, moisture," Old Irish muad "cloud," Polish muł "slime," Sanskrit mutra- "urine," Avestan muthra- "excrement, filth"); related to German Schmutz "dirt," which also is used for "mud" in roads, etc., to avoid dreck , which originally meant "excrement." Welsh mwd is from English. The older word is fen .

 Meaning "lowest or worst of anything" is from 1580s. As a word for "coffee," it is hobo slang from 1925; as a word for "opium" from 1922. Mud-puppy "salamander" is by 1855, American English; the mud-dauber wasp was so called by 1856. The children's mud-pie is attested from 1788. Mud-flat "muddy, low-lying ground near a shore" is by 1779. Mud-room "room for removing wet or muddy footwear" is by 1938.

 The expression clear as mud (that is, "not clear at all") is by 1796. To throw or hurl mud "make disgraceful accusations" is from 1762. To say (one's) name is mud and mean "(one) is discredited" is recorded from 1823, from mud in obsolete sense of "a stupid twaddling fellow" (1708). Mud in your eye as a toast is recorded from 1912, American English.
########## 09513b90f5c78f67
Advertisement Remove Ads 
 moss (n.) 

 the meanings "mass of small, cryptogamous, herbaceous plants growing together" and "bog, peat-bog" are the same word: Old English meos "moss plant" and mos "bog;" both are from Proto-Germanic *musan (source also of Old High German mios , Danish mos , German Moos ), also in part from Old Norse mosi "moss, bog," and Medieval Latin mossa "moss," from the same Germanic source.

 These are from PIE *meus- "damp," with derivatives referring to swamps and swamp vegetation (source also of Latin muscus "moss," Lithuanian mūsai "mold, mildew," Old Church Slavonic muchu "moss"). The Germanic languages have the word in both senses, which is natural because moss is the characteristic plant of boggy places. It is impossible to say which sense is original. The proverb that a rolling stone gathers no moss is suggested from 14c.:

 Selden Moseþ þe Marbelston þat men ofte treden. ["Piers Plowman," 1362]
--
 club-moss (n.) 

 1590s, from club (n.) + moss . So called for the club shape of its upright spore-cases.

 litmus (n.) 

 "blue dye-stuff obtained from certain lichens," early 14c., lit-mose , probably from an Old Norse word related to Norwegian dialectal litmose , from Old Norse lita "to dye, to stain" (from litr "color, dye;" see lit (n.1)) + mos "moss." Said to be also in part from Middle Dutch lijkmoes (Dutch lakmoes ), from lac (see lac ) + moes "pulp." Another idea [Watkins] connects the first element to Middle Dutch leken "to drip, leak" (see leak (v.)). The second element is in any case the common Germanic word for "moss, lichen" (see moss ).
########## b2d652035a8a42c7
Advertisement Remove Ads 
 match (n.1) 

 "stick for striking fire." Late 14c., macche , "wick of a candle or lamp," a sense now obsolete, from Old French meiche "wick of a candle," from Vulgar Latin *micca/*miccia (source also of Catalan metxa , Spanish mecha , Italian miccia ), which is of uncertain origin, probably ultimately from Latin myxa , from Greek myxa "lamp wick," originally "mucus," based on notion of wick dangling from the spout of a lamp like snot from a nostril, from PIE root *meug- "slimy, slippery" (see mucus ). English snot also had a secondary sense from late 14c. of "snuff of a candle, burnt part of a wick," surviving at least to late 19c. in northern dialects.

 The modern spelling is from mid-15c. The meaning "piece of cord or tow soaked in sulfur, used for lighting fires, lamps, candles, etc." is from 1530. It was used by 1830 for the modern type of sulfur-tipped wooden friction match, which were perfected about that time, and competed with lucifer for much of 19c. as the name for this invention. An earlier version consisted of a thin strip of wood tipped with combustible matter that required contact with phosphorous carried separately in a box or vial.

 In the manufacture of matches much trouble has been occasioned by the use of phosphorous .... In some of the small and poorly-managed factories the men and children are never free from the fumes; their clothes and breath are luminous in the dark, and in the daytime white fumes may be seen escaping from them whenever they are seated by the fire. ... The danger arising from the use of matches was magnified, because they could sometimes be seen in the dark, were liable to ignite on a warm shelf, and were poisonous to such an extent that children had been killed by using them as playthings. [John A. Garver, "Matches," in The Popular Science Monthly, August 1877]
--
 match (n.2) 

 "one of a pair, an equal." Middle English macche , from Old English mæcca "companion, mate, one of a pair, wife, husband, one suited to another, an equal," from gemæcca , from Proto-Germanic *gamakon "fitting well together" (source also of Old Saxon gimaco "fellow, equal," Old High German gimah "comfort, ease," Middle High German gemach "comfortable, quiet," German gemach "easy, leisurely"), from PIE root *mag- "to knead, fashion, fit."

 Meaning "person or thing that exactly corresponds to another" is from c. 1400. Middle English sense of "matching adversary, person able to contend with another" (c. 1300) led to sporting meaning "contest," which is attested from 1540s. Meaning "a matrimonial compact" is from 1570s.

 match (v.) 
--
 mid-14c., macchen , "be able to compete with, be an adequate opponent for;" late 14c., "to join one to another" (originally especially in marriage), from match (n.2). Meaning "to place (one) in conflict with (another)" is from c. 1400. That of "to pair with a view to fitness, find or provide something to agree or harmonize with" is from 1520s; that of "to be equal to" is from 1590s. Related: Matched ; matching .
 also from mid-14c. 

 Entries linking to match 

 Lucifer 

########## 10629468a3aeaa10
Advertisement Remove Ads 
 moist (adj.) 

 late 14c., "slightly wet; well-irrigated, characterized by moistness," from Old French moiste "damp, wet, soaked" (13c., Modern French moite ), which is of uncertain origin. Perhaps from Vulgar Latin *muscidus "moldy," also "wet," from Latin mucidus "slimy, moldy, musty," from mucus "slime" (see mucus ). Alternative etymology [Diez] is from Latin musteus "fresh, green, new," literally "like new wine," from musteum "new wine" (see must (n.1)). If this wasn't the source, it influenced the form of the other word in Old French. Related: Moistly ; moistness (mid-14c.).
 also from late 14c. 

 Entries linking to moist
```


## [2026-09-07T17:44:03.242Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && python3 - <<'EOF'\nimport re\nfor f,pat in [('7bb7b10d45b67442','mustard'),('b3b9f8b49e115c40','mucus'),('0966d4f7533ff784','smuggle')]:\n    t=open(f+'.txt',encoding='utf-8').read()\n    i=t.find(pat+' (')\n    print('#####',f,pat); print(t[i:i+1400]); print()\nEOF",
 "description": "Read mustard/mucus/smuggle entries"
}
```


### [2026-09-07T17:44:04.627Z] TOOL RESULT

```
##### 7bb7b10d45b67442 mustard
mustard (n.) 

 late 13c. (late 12c. as a surname), "seed of the mustard plant crushed and used as a condiment paste or for medicinal purposes," from Old French mostarde "mustard; mustard plant" (Modern French moutarde ), from moust "must," from Latin mustum "new wine" (see must (n.1)); so called because it was originally prepared by adding must to the ground seeds of the plant to make a paste. As the name of the plant itself, by mid-14c. in English. As a color name, it is attested from 1848.

 Mustard-pot is attested from early 15c. Mustard gas , World War I poison (first used by the Germans at Ypres, 1917), so called for its color and smell and burning effect on eyes and lungs; chemical name is dichlordiethyl sulfide; it contains no mustard and is an atomized liquid, not a gas. To cut the mustard (1907, usually in negative) is probably from slang mustard "genuine article, best thing" (1903) on notion of "that which enhances flavor."

 I'm not headlined in the bills, but I'm the mustard in the salad dressing just the same. [O. Henry, "Cabbages and Kings," 1904]
 also from late 13c. 

 Entries linking to mustard 

 must (n.1) 

 "new wine," Old English must , from Latin mustum (also source of Old High German, German most , Old French moust , Modern French moût , Spanish, Italian mosto ), short for vinum mustum "fresh wine," neuter of mustus "fresh, new, newborn," perhaps litera

##### b3b9f8b49e115c40 mucus
mucus (n.) 

 "viscid fluid secreted by the mucous membranes of animals," 1660s (replacing Middle English mucilage ), from Latin mucus "slime, mold, mucus of the nose, snot," from PIE root *meug- "slippery, slimy," with derivatives referring to wet or slimy substances or conditions (source also of Latin emungere "to sneeze out, blow one's nose," mucere "be moldy or musty," Greek myssesthai "to blow the nose," myxa "mucus;" Sanskrit muncati "he releases"). Old English had horh , which may be imitative.
 also from 1660s 

 Entries linking to mucus 

 match (n.1) 

 "stick for striking fire." Late 14c., macche , "wick of a candle or lamp," a sense now obsolete, from Old French meiche "wick of a candle," from Vulgar Latin *micca/*miccia (source also of Catalan metxa , Spanish mecha , Italian miccia ), which is of uncertain origin, probably ultimately from Latin myxa , from Greek myxa "lamp wick," originally "mucus," based on notion of wick dangling from the spout of a lamp like snot from a nostril, from PIE root *meug- "slimy, slippery" (see mucus ). English snot also had a secondary sense from late 14c. of "snuff of a candle, burnt part of a wick," surviving at least to late 19c. in northern dialects.

 The modern spelling is from mid-15c. The meaning "piece of cord or tow soaked in sulfur, used for lighting fires, lamps, candles, etc." is from 1530. It was used by 1830 for the mo

##### 0966d4f7533ff784 smuggle
smuggle (v.) 

 "import or export secretly and contrary to law," 1680s, of Low German or Dutch origin (see smuggler ). The figurative sense of "convey in a clandestine way" is by 1783. Related: Smuggled ; smuggling .
 also from 1680s 

 Entries linking to smuggle 

 smuggler (n.) 

 "one who imports and exports secretly and contrary to law," 1660s, from Low German smuggeln or Dutch smokkelen "to transport (goods) illegally," apparently a frequentative formation of a word meaning "to sneak" (from Proto-Germanic *smuganan ; source also of Dutch smuigen "to eat secretly;" Swedish smyg "a lurking-hole," Danish smughandel "contraband trade," Norwegian smjuga , Old English smeogan "to creep"), perhaps literally "to slip (contraband through)," from Proto-Germanic *(s)muk- (see smock ).

 smuggling (n.) 

 "the offense of importing and exporting secretly and contrary to law," 1728, verbal noun from smuggle (v.).

 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 More to explore

 export 

 by 1610s, "carrying out of a place;" perhaps from late 15c., from Latin exportare "to carry out, bring out; send away, export," from ex "out, away" (see ex-) + portare "to carry," from PIE root *per- (2) "to lead, pass over." The sense of "send out (commodities) from one country 

 import 

 early 15c., "signify, show, bear or convey in meani
```


## [2026-09-07T17:44:19.945Z] TOOL CALL #56: Bash

```json
{
 "command": "for u in \"https://en.wiktionary.org/wiki/%D8%A2%D9%85%D9%88%D8%AE%D8%AA%D9%86\" \"https://en.wiktionary.org/wiki/%D9%85%D9%81%D8%AA\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/mewk-\" \"https://en.wiktionary.org/wiki/%D9%85%D9%88%D8%AA%D8%B1\"; do echo \"### $u\"; python3 tools/fetch_source.py \"$u\" --note \"page 338, Meug: Persian amuxtan / moft, PIE *mewk-\" 2>&1 | tail -1; done",
 "description": "Archive Wiktionary pages"
}
```


### [2026-09-07T17:44:26.571Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/%D8%A2%D9%85%D9%88%D8%AE%D8%AA%D9%86
/home/sfmqrb/git/rishe/data/verification/sources/web/c9edb9766a1ae386.txt
### https://en.wiktionary.org/wiki/%D9%85%D9%81%D8%AA
/home/sfmqrb/git/rishe/data/verification/sources/web/5609fb670ce562ec.txt
### https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/mewk-
/home/sfmqrb/git/rishe/data/verification/sources/web/89f04884870b01a6.txt
### https://en.wiktionary.org/wiki/%D9%85%D9%88%D8%AA%D8%B1
/home/sfmqrb/git/rishe/data/verification/sources/web/02297b04625b0e13.txt
```


## [2026-09-07T17:44:30.399Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in c9edb9766a1ae386 5609fb670ce562ec 89f04884870b01a6; do echo \"########## $f\"; python3 -c \"\nimport sys,re\nt=open('$f.txt',encoding='utf-8').read()\ni=t.find('Etymology')\nprint(t[max(0,i-600):i+1800])\n\"; done",
 "description": "Read Wiktionary etymologies"
}
```


### [2026-09-07T17:44:31.690Z] TOOL RESULT

```
########## c9edb9766a1ae386
D8%AE%D8%AA%D9%86
FETCHED: 2026-09-07T17:44:23Z
STATUS: 200
TITLE: آموختن - Wiktionary, the free dictionary

آموختن - Wiktionary, the free dictionary 

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
 Etymology 

 1.2 
 Pronunciation 

 1.3 
 Verb 

 1.3.1 
 Conjugation 

 1.3.2 
 Derived terms 

 1.4 
 References 

 Toggle the table of contents 

 آموختن 

 12 languages 

 Zazaki 
 فارسی 
 Na Vosa Vakaviti 
 Magyar 
 Bahasa Indonesia 
 한국어 
 Kurdî 
 Malagasy 
 Русский 
 Тоҷикӣ 
 اردو 
 中文 

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

 Persian
 [ edit ] 

 Etymology
 [ edit ] 

 From Middle Persian [script needed] ( hmwhtn', hmwc-, hmwz- /⁠hāmmōxtan, hāmmōz-⁠/ , “ to teach, learn ” ) , ultimately from Proto-Iranian *mauč- ( “ to learn, teach ” ) . Akin to Tat amuxtən and to Old Armenian համոզեմ ( hamozem ) , an Iranian borrowing.

 The Iranian root is perhaps abstracted from Proto-Iranian *ham-Hauč- , from Proto-Iranian *ham- ( “ together ” ) + Proto-Iranian *Hauč- ( “ learning ” ) , the latter a denominal form of Proto-Iranian *yauč- ( “ to learn, teach ” ) , from Proto-Indo-European *h₁ewk- ( “ to be accustomed ” ) . 

 Direct cognate with Northern Kurdish hêvotin ( “ to teach ” ) ; outside of Iranian, compare Sanskrit उच् ( uc , “ to take pleasure, be accustomed ” ) , Old Armenian ուսանիմ ( usanim , “ to learn ” ) , Lithuanian jùnkti ( “ to learn ” ) , Russian учить ( učitʹ , “ to teach ” ) , Polish uczyć ( “ to teach; to learn ” ) , Gothic 𐌱𐌹𐌿𐌷𐍄𐍃 ( biūhts , “ accustomed to ” ) .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ʔaː.moːx.ˈtan/ 

 
########## 5609fb670ce562ec
g/wiki/%D9%85%D9%81%D8%AA
FETCHED: 2026-09-07T17:44:24Z
STATUS: 200
TITLE: مفت - Wiktionary, the free dictionary

مفت - Wiktionary, the free dictionary 

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
 Arabic 

 Toggle Arabic subsection 

 1.1 
 Etymology 

 1.2 
 Pronunciation 

 1.3 
 Noun 

 1.3.1 
 Declension 

 1.3.2 
 Descendants 

 2 
 Persian 

 Toggle Persian subsection 

 2.1 
 Etymology 

 2.2 
 Pronunciation 

 2.3 
 Adjective 

 2.3.1 
 Synonyms 

 2.3.2 
 Descendants 

 2.4 
 Further reading 

 3 
 Urdu 

 Toggle Urdu subsection 

 3.1 
 Etymology 

 3.2 
 Pronunciation 

 3.3 
 Adjective 

 Toggle the table of contents 

 مفت 

 10 languages 

 فارسی 
 Suomi 
 Na Vosa Vakaviti 
 Magyar 
 한국어 
 Kurdî 
 Malagasy 
 Bahasa Melayu 
 Русский 
 سرائیکی 

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

 Root 

 ف ت ي ( f t y ) 

 1 term 

 Etymology
 [ edit ] 

 Derived from the active participle of أَفْتَى ( ʔaftā ) .

 Pronunciation
 [ edit ] 

 IPA ( key ) : /muf.tin/ 

 Noun
 [ edit ] 

 مُفْتٍ • ( muftin )  m ( construct state مُفْتِي ( muftī ) , plural مُفْتُون ( muftūn ) , feminine مُفْتِيَة ( muftiya ) ) 

 ( also Islam ) deliverer of formal opinions ; mufti 

 Declension
 [ edit ] 

 Declension of noun مُفْتٍ ( muftin )

 singular

 masculine

 feminine

 singular triptote in ـٍ ( -in ) 

 singular triptote in ـَة ( -a ) 

 indefinite

 definite

 construct

 indefinite

 definite

 construct

 informal

 مُفْتِي 
 muftī 

 الْمُفْتِي 
 al-muftī 

 مُفْتِي 
 muftī 

 مُفْتِيَة 
 muftiya 

 الْمُفْتِيَة 
 al-muftiya 

 مُفْتِيَة 
 muftiyat 

 nominative

 مُفْتٍ 
 muftin 

 الْمُ
########## 89f04884870b01a6
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/mewk-
FETCHED: 2026-09-07T17:44:24Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/(s)mewk- - Wiktionary, the free dictionary

Reconstruction:Proto-Indo-European/(s)mewk- - Wiktionary, the free dictionary 

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
 Proto-Indo-European 

 Toggle Proto-Indo-European subsection 

 1.1 
 Root 

 1.1.1 
 Derived terms 

 1.2 
 References 

 Toggle the table of contents 

 Reconstruction:Proto-Indo-European/ (s)mewk- 

 Add languages 

 Reconstruction 

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
 Get shortened URL 

 Print/export

 Download as PDF 
 Printable version 

 In other projects

 Appearance

 move to sidebar 
 hide 

 From Wiktionary, the free dictionary

 (Redirected from Reconstruction:Proto-Indo-European/mewk- ) 

 This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.

 Proto-Indo-European
 [ edit ] 

 Root
 [ edit ] 

 *(s)mewk- ( perfective ) [ 1 ] [ 2 ] [ 3 ] 

 to let loose ; to release 

 to slip away ; to escape ; to flee 

 Derived terms
 [ edit ] 

 Term
```


## [2026-09-07T17:44:41.400Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && python3 -c \"\nt=open('5609fb670ce562ec.txt',encoding='utf-8').read()\ni=t.find('Persian\\n [ edit ]')\nif i<0: i=t.find('Persian')\nprint(t[t.find('Descendants',i):t.find('Descendants',i)+2500])\n\"",
 "description": "Extract Persian moft section"
}
```


### [2026-09-07T17:44:42.638Z] TOOL RESULT

```
Descendants
 [ edit ] 

 → Azerbaijani: müftə 

 → Bengali: মুফত ( muphot ) 

 → Chagatai: مفت ( mft /⁠muft⁠/ ) 
 Uzbek: muft 

 Uyghur: مۇت ( mut ) 

 → Gujarati: મફત ( maphat ) 

 → Hindustani: 
 Hindi: मुफ़्त ( muft ) , मुफ़त ( mufat ) , मुफ्त ( mupht ) , मुफत ( muphat ) — nuqtaless 
 Urdu: مفت ( muft ) 

 → Marathi: मोफत ( mophat ) 

 Ottoman Turkish: مفت ( müft ) 
 Turkish: müft 

 → Bulgarian: муфта ( mufta ) 

 → Romanian: moft 

 → Serbo-Croatian: mȕktē / му̏кте̄ 

 → Punjabi: 
 Gurmukhi script: ਮੁਫ਼ਤ ( mufat ) , ਮੁਫਤ ( muphat ) — nuqtaless 
 Shahmukhi script: مُفت ( muft ) 

 → Turkmen: mugt 

 Further reading
 [ edit ] 

 Hayyim, Sulayman ( 1934 ), “ مفت ”, in New Persian–English dictionary , Teheran: Librairie-imprimerie Béroukhim 

 Dehkhoda, Ali-Akbar ( 1931– ), “ مفت ”, in Dehkhoda Dictionary Institute , editors, Dehkhoda Dictionary (in Persian), Tehran: University of Tehran Press . 

 Urdu
 [ edit ] 

 Etymology
 [ edit ] 

 Borrowed from Classical Persian مفت ( muft ) .

 Pronunciation
 [ edit ] 

 ( Standard Urdu ) IPA ( key ) : /mʊft̪/ 

 Adjective
 [ edit ] 

 مفت • ( muft ) ( indeclinable , Hindi spelling मुफ़्त ) 

 free of charge 

 Retrieved from " https://en.wiktionary.org/w/index.php?title=مفت&oldid=90003067 "

 Categories : Arabic terms belonging to the root ف ت ي 
 Arabic participles 
 Arabic active participles 
 Arabic terms derived from active participles 
 Arabic 2-syllable words 
 Arabic terms with IPA pronunciation 
 Arabic lemmas 
 Arabic nouns 
 Arabic masculine nouns 
 ar:Islam 
 Arabic nouns with triptote singular in -in 
 Arabic nouns with triptote singular in -a 
 Arabic nouns with sound masculine plural 
 Arabic nouns with sound feminine plural 
 Persian terms inherited from Proto-Indo-Iranian 
 Persian terms derived from Proto-Indo-Iranian 
 Persian terms inherited from Proto-Indo-European 
 Persian terms derived from Proto-Indo-European 
 Persian terms with IPA pronunciation 
 Rhymes:Persian/uft 
 Rhymes:Persian/uft/1 syllable 
 Persian lemmas 
 Persian adjectives 
 Persian offensive terms 
 Urdu terms borrowed from Classical Persian 
 Urdu terms derived from Classical Persian 
 Urdu terms with IPA pronunciation 
 Urdu lemmas 
 Urdu adjectives 
 Urdu indeclinable adjectives 

 Hidden categories: Pages with entries 
 Pages with 3 entries 

 This page was last edited on 31 March 2026, at 03:18.

 Definitions and other text are available under the Creative Commons Attribution-ShareAlike License ; additional terms may a
```


## [2026-09-07T17:44:47.008Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && python3 -c \"\nt=open('5609fb670ce562ec.txt',encoding='utf-8').read()\ni=t.find('nominative')\nj=t.find('Persian\\n [ edit ]',i)\nprint(t[j:j+1500])\n\"",
 "description": "Extract Persian moft etymology"
}
```


### [2026-09-07T17:44:48.244Z] TOOL RESULT

```
Persian
 [ edit ] 

 Etymology
 [ edit ] 

 Ultimately from Proto-Indo-Iranian *muktás (whence also زمخت ( zumuxt ) ), from Proto-Indo-European *muk-tó-s ( “ released, discharged ” ) , from *(s)mewk- ( “ to free, escape ” ) . Compare Sanskrit मुक्त ( mukta ) or मोक्ष् ( mokṣ ) .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ˈmuft/ 

 ( Dari, formal ) IPA ( key ) : [mʊft̪] 

 ( Dari, formal ) IPA ( key ) : [mʊft̪] 
 ( Kabuli ) IPA ( key ) : [mʊft̪] 

 ( Hazaragi ) IPA ( key ) : [muft̪] 

 ( Iran, formal ) IPA ( key ) : [moft̪ʰ] 

 ( Tajik, formal ) IPA ( key ) : [muft̪] 

 Rhymes: -uft 

 Readings

 Classical reading ? 

 muft

 Dari reading ? 

 muft

 Iranian reading ? 

 moft

 Tajik reading ? 

 muft

 Adjective
 [ edit ] 

 مفت • ( muft / moft ) ( Tajik spelling муфт ) 

 free , gratis 

 very cheap 

 ( offensive ) gibberish 
 example: حرف مفت ( harf-e moft ) 

 Synonyms
 [ edit ] 

 مجانی ( majjâni ) 

 رایگان ( râygân ) 

 ارزان ( arzân ) 

 Descendants
 [ edit ] 

 → Azerbaijani: müftə 

 → Bengali: মুফত ( muphot ) 

 → Chagatai: مفت ( mft /⁠muft⁠/ ) 
 Uzbek: muft 

 Uyghur: مۇت ( mut ) 

 → Gujarati: મફત ( maphat ) 

 → Hindustani: 
 Hindi: मुफ़्त ( muft ) , मुफ़त ( mufat ) , मुफ्त ( mupht ) , मुफत ( muphat ) — nuqtaless 
 Urdu: مفت ( muft ) 

 → Marathi: मोफत ( mophat ) 

 Ottoman Turkish: مفت ( müft ) 
 Turkish: müft 

 → Bulgarian: муфта ( mufta ) 

 → Romanian: moft 

 → Serbo-Croatian: mȕktē / му̏кте̄ 

 → Punjabi: 
 Gurmukhi script: ਮੁਫ਼ਤ (
```


## [2026-09-07T17:45:35.988Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD Bd2 leaf 254 (p.249) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==254' incoming/WLD/WLD_Bd2_pages.txt | head -40",
 "description": "Read Walde-Pokorny II p.249"
}
```


### [2026-09-07T17:45:37.279Z] TOOL RESULT

```
=== WLD Bd2 leaf 254 (p.249) ===
                                                                     meu-                                           249

  Ai. misdti „schlagt die Augen auf^, ni-mis £, ni-misa-                                           m. „da8 Blinzelu,
SchlieSen          des                „Betrug, Tauschung^; midam „leise'',
                                 Auges^';             mi^a-     n.

i^miz’do- etwa „versto6en‘^j, milati  „schlie6t  die Augen^^;
  aksl. mhsch „turpis  quaestus^,  russ. miel   ,jGewinn^^, ohmichniihsa „sich
irren^;
  ndl. (flam.) mijzelen, mtzelen „staubregnen“,                                       nd.   mis „feuchtes, nebliges
Wetter^*, miseln „fein regnen“: ob aisL mistr „trubes Wetter, ^TebeldampP,
ags. mist ,,^febel, Staubregen^,                                mndl. nndl. mist „Neber‘ hieher oder                 als

"^miysiu- zu meigh- gehore, ist nicbt entschieden.
  S.     Kern IF. 4,               11 If.            (ai.    me^ati „besprengt             befeuchet“;   Dhatup.     ist

aber eine zweifelhafte Grofie und wird kaum bestatigt durch mrkt „WiddeF‘
als „*Bespringer“,                  s.   "^moisos oder ^maisos „Schaf' ),                      Uhlenbeck      Ai.   Wb.
225, Lewy KZ. 40, 562.
  mei-s- und 7nci-(}h^ -q „flimniern‘' scheinen Erw. einer nicbt                                         mebr nacb-
weisbaren Wz.                7nei-.



1 . nieii-„feucbt,moderig, netzen,unreineFlussigkeit (aucbllarn), bescbmutzen,
      aucb in Nasses taucben, waschen^^; Zerlegung in zwei ursprgl. getrennte
       Sippen, einerseits meu-, mil- „^'ascben“, andererseits 7neu-, mu- (und
               7nn-) in den ersteren Bedd. (s. Schulze Qu. ep. IGOf., KZ. 45,
       235, Uhlenbeck    IF. 25, 144 f.) scbeint nicbt geboten, aufierdem ist
       speziell die Auffassung von .,Harn*'' (ai. miltra-^ air. mun) als „Wa8ch-
       mittel'^      zwar kulturgescbichtlich einwandfrei, ist aber fiir ai.
                    (ibd.)
       nmii'a- wegen av. inu^ra- „Unreinigkeit, Scbmutz“ die Prioritat der
       Bed. jjHarn als Wasehmittel“ unwabrscheinlich (s. Persson Beitr. 949)
       und daher aucb fiir air. man durchaus fraglich.
  Ai. mfdra- n.                   „Harn‘',             av.    7nu&ra-       n.   „Unreinigkeit,   Schmutz^'    (;   ndl.
modeler usw.)           :
```


## [2026-09-07T17:45:44.184Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==259' incoming/WLD/WLD_Bd2_pages.txt | head -45",
 "description": "Read Walde-Pokorny II p.254 area for meug"
}
```


### [2026-09-07T17:45:45.450Z] TOOL RESULT

```
       :                                                ;




254                                       meuq-, meug-


   B.      Ai,   muncdti    „lost,   befreit, laBt los^'      Gj'^streift    ab,   lafit   abgleiten‘‘),
miikti- „L6siing, Befreiung, Aufgeben'S       prati-mimcati „zieht an, legt
an (Kleidung)^*; lit. munhu^ mukti „entwischen'' = lett. mukii, mukt „sich
abstreifen, entwischen, fiiehen“ (und „in einen Sumpf einsinken^^ s. o. da                         ;


die bait. Bed. „entwiscben“ aus „entgleiten, wegscblupfen“                         ohne Schwierig-
keit zu  gewinnen ist, ist Bartholomaes KZ. 47, 292 Vergleich mit ap. amti-
^ah „er floh“, der auch Wechsel q k, bzw. fiirs Balt, westidg. Guttural
                                                  :




voraussetzt, wohl nicht vorzuziehen)   lit. maukti^ smaukti „gleitend streifen“,
                                              ;


lett. maukt „streifen“, lit. smunku, smiikti „gleitend sinken, rutschen“;

   abg. smycci, smykati     „kriechen“ (modern slav. auch „schlupfen, gleiten.
abstreifen“) uber rmknqti sq „transire'‘ s. Berneker.
                 ;


   Eine Wzf. meuqh- mit der spez. Bed. „hineinschlupfen'- wohl in arm.
mxem „stecke hinein, tauche ein (auch das Eisen zum harten ins Wasser),
bade‘^ mux „tinctura, tempra“, mxim „entrare, insinuarsi, ingolfarsi^, nach
Bugge KZ. 32, 20 (Zw.            bei   Hiibschmann Arm. Gr. I 475) zunachst zu gr.
ixvx6(; „innerster Winkel“        (etwa
                                    *Schlupfwinkel“), pvyaxog, juv^oirarog „der
                                          ,



innerste“ (hieher,         nicht zu  ,,Maus, Muskel, Hode'‘, auch juvoyog' to
dvdgeTov xal yvvaixeiov jlioqiov Hes., aus             Kick KZ. 43, 149j. Tgl.
```


## [2026-09-07T17:46:01.599Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LEW mustus/mucus ===\"; grep -n \"mustus\\|mūcus\\|mucus\" LEW_1910.txt | head -10; echo \"=== HUB muft ===\"; grep -n \"muft\\|mukta\" HUB.txt | head -10; echo \"=== TLM amutha ===\"; grep -n \"amuθ\\|amuu\\|amutha\\|mauth\" TLM.txt | head -10",
 "description": "Grep LEW, Hübschmann, Tolman"
}
```


### [2026-09-07T17:46:01.678Z] TOOL RESULT

```
=== LEW mustus/mucus ===
=== HUB muft ===
=== TLM amutha ===
```


## [2026-09-07T17:46:05.965Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for p in \"mustum\" \"muccus\" \"mucor\" \"must\" ; do echo \"=== $p in LEW ===\"; grep -c \"$p\" LEW_1910.txt; done; echo; grep -n \"mustus\" LAT.txt | head -5; echo \"=== TLM flee ===\"; grep -n \"flee\\|fled\" TLM.txt | head -8",
 "description": "Grep Latin dicts loosely"
}
```


### [2026-09-07T17:46:07.168Z] TOOL RESULT

```
=== mustum in LEW ===
0
=== muccus in LEW ===
0
=== mucor in LEW ===
0
=== must in LEW ===
7

40040:^15,137, par Pompeius Lenaeus, quoniam mustaceis subiceretur. V. mustus.
=== TLM flee ===
289:1.  Says  Darius  the  king:  Afterwards  Nidintu-Bel  with  (his) few  horsemen  fled  (and)  went  to  Babylon;  afterwards  I   went  to Babylon;  by  the  grace  of  Ahura  Mazda  I   both  seized  Babylon and  seized  that  Nidintu-Bel;  afterwards  I   slew  that  Nidintu-Bel at  Babylon.
336:13.  Says  Darius  the  king:  Afterwards  this  Phraortes  with  a few  horsemen  fled;  there  is  a   region  Raga  by  name  in  Media — along  there  he  went;  afterwards  I   sent  forth  my  army  in  pursuit; Phraortes  seized  was  led  to  me;  I   cut  off  (his)  nose  and  ears and  tongue,  and  I   put  out  his  eyes;3  he  was  held  bound4  at my  court;  all  the  people  saw  him;  afterwards  I   put  him  on  a cross5  at  Ecbatana,  and  what  men  were  his  foremost  allies,  these I   haled  within  the  fortress  at  Ecbatana.
407:7.  Says  Darius  the  king:  Afterwards  this  Vahyazdata  with few  horsemen  fled  (and)  went  to  Paishiyauvada;  from  thence  he took  an  army  (and)  again  went  against  Artavardiya  to  engage in  battle;  there  (is)  a   mountain  Parga  by  name — here  they  en- gaged in  battle;  Ahura  Mazda  gave  me  aid;  by  the  grace  of Ah ura  Mazda  my  army  smote  that  army  of  Vahyazdata  utterly; 5   da}rs  in  the  month  Garmapada  were  completing  their  course — then  the  battle  (was)  fought  by  them  and  they  seized  that  Vah- yazdata and  what  men  were  his  foremost  allies  they  seized.
412:12.  Says  Darius  the  king:  Afterwards  this  man,  who  was chief  of  that  army  which  Vahyazdata  sent  against  Vivana,  he fled  with  a   few  horsemen  (and)  went  away — there  (is)  a   strong- hold Arshada  by  name  in  Arachosia — he  went  thereby;  after- wards Vivana  with  an  army  went  in  pursuit  of  them;  here  he seized  him  and  what  men  were  his  foremost  allies  he  slew.
1545:naviya,  Bh.  1.  18.  The  word  is  generally  regarded  as  nom. f.  of  an  abstract  formation  from  nav,  ship ,   and  as  signifying  a collection  of  ships ,   fleet ;   so  Kern  (ZDMG,  23,  237),  Muller (WZKM,  11,  252),  Gray  (AJP,  21,  19),  Bartholomae  (Altiran. Wb.,  1065).  The  old  interpretation  (bei  den  Schiffen ,   WB),  de- fended by  Foy  (ZDMG,  51,  371)  regards  the  form  as  loc.  sg.  of nav  with  p»stpos.  a;  so  Pedersen,  KZ,  10,  129,  on  opposite  side (the  enemy)  was  on  shipboard.  Skt.  nav,  ship ,   New  Pers.  nav.
1707:mud  (Pres,  mu0a-,  Bartholomae,  Grundr.  124),  to  flee.  Pret.  3 sg.  amu0a.  Cf .   Htlsing,  KZ,  38,  258.  This  interpretation  (which is  favored  by  both  Elam,  and  Bab.  versions)  is  undoubtedly  cor- rect and  supersedes  the  former  view  of  regarding  amu0a  as  an  adv. Cf.  Tolman,  Vdt.  Stud.  1,  21.  In  Bh.  3.  1.  71  read  am[u0a]  in place  of  ma&sta  of  ed.
1866:[har  (Pres,  hara-,  Bartholomae,  Grundr.  123),  to  flee.  Oppert’s supplement  [aharatja,  pret.  3   sg.  in  Bh.  1.  95.  See  s.  v.  l)ah.]
```


## [2026-09-07T17:46:13.255Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^mustus\\|^mustus,\\|mustus,\" LAT.txt | head -5; echo ---; sed -n 40030,40070p LAT.txt; echo \"=== mucus in LAT ===\"; grep -n \"mūcus\\|mucus,\" LAT.txt | head -5",
 "description": "Read Ernout-Meillet mustus"
}
```


### [2026-09-07T17:46:13.339Z] TOOL RESULT

```
---
Mussare eat conaervd dans quelques dialectes roaans, M.L.S776d.
Cf. aussi *rimHssicdre, M.L.7305.
D'aprbs Varr., L.L.7,x, mussare dictum quod muti non amplius quam
MV dicunt; a quo idem ( ac.Snnius ) id quod minimum est (inc. 10 V 3 ):
" neque, ut aiunt, p.u facere audent". MussS serait donc une ononatopde
(aaalogue k mugiS, muttis) fornde sur mu (coaae aCtus), ou sur mut ,
cf. GLK 1,340,8, mutmut non facere audet. Toutefois la forne indique
au noins une influence du gr. p,u£o>, de aene sens, qu'on troure dans
Esch., Arist., et summussus rappelle U7tpp,u^<0 (Diph.).
mustax, -acis m.: varidtd de laurier, ainsi nomade, dit Pline
^15,137, par Pompeius Lenaeus, quoniam mustaceis subiceretur. V. mustus.
mustela, -ae f. (muste lia): 1* belette, fouine; a* poisson aal dd-755
_ mGto
termini, lotte selon oertains. Ancien (Ena., Pl.). M.L.5778.
Dirivis: nustgl(Uula,-ae f.j mustelinus, nustSlatus, -a, -um: [couleur]
de belette; nustellOriun; nustglopardus.
Pas d'itymologie claire. Cf. nitela.
mustelagS, -inis f.: lauriole, arbrisseau. Correapond an gr. Xa-
|xou, 5 acpvT). Fignre dans Ps.Apnl.yBerb.S 7 / qui a la variante s utilago
(58). Cf. nuit ilagO.
mtistiS, - 5 nls m.: petite nonche. Cf«Isid« 0 r.ia, 8 , 16, bibiones
sunt qui in uino nascuntur, quos uulgo mustiones (musc- var.) a musto
appellant (itymologie popnlaire?). M.L.5781.
Cf. musca, V. Sofer, 104,175.
mustricula, -ae f.: — est machinula ex regulis, in- qua calceus,
nouus suitur, P.F.i3i,i8. Sans antre exemple. La glose de Scaliger,
CGL V 604,14: mustricola : machina ad stringendos mures, confond le
mot avec muscipula .
mttstus,-a, -um: nonvean; musta agna: agnelle nouvean-nie (Caton);
mustum ulnum: vin nonvean. Terne de la langue rustique; usiti snrtont
an neutfe substantivi mustum "vin nonvean"; par suite "vin doux, mout";
sens conservi dans les 1 . roinanes. Ovide, M.14,146, emploie «eme mustd,
-Orum an sens de "vendaages, automnes" tercentum musta uidere. Ancien,
technique. Pamroman, M.L.5783; et gem.: v.h.a,nost, etc.
Dirivis: mustarius: m. urceus (Caton)j musteus : i° nonvean, frais
(musteus caseus) •, a° donx comme le vin nonvean, musteum kSlum "pomme
donce", M.L.5779; m ustuientes: abondant en vin donx ( n. uentus , Pl.
Ci.383); mustdceum n.: gateau de mariage, fait de farine pitrie avec
dn vin doux, du fronage et de 1'anis et cnit suf des fenilles de
lanrier (Cat. Agr. 131); cf .testaceus, etc.
Certaines fomes romanes remontent a *mustidus et *mustosus, M.L.
=== mucus in LAT ===
2668:fjisdh "glissant, visqueux", norv. ulka "moisi, mucus, glaire", etc.
```


## [2026-09-07T17:46:21.293Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n 40070,40085p LAT.txt; echo \"=== mucus headword ===\"; grep -n \"mucus, -i\\|mucus,-i\\|mQcus\\|mucSs\\|muceS\\|mucidus\" LAT.txt | head -8",
 "description": "Ernout-Meillet mustus etymology and mucus"
}
```


### [2026-09-07T17:46:21.355Z] TOOL RESULT

```
Certaines fomes romanes remontent a *mustidus et *mustosus, M.L.
5780,578«.
Pas d*itymologie claire.
mutilagO;-v. multilagO.
mutilus, -a, -um: icorai, m.bos, -a capella, cf.Don., Hec.65, et
logond. nudulu "chbvre sans cornea", M.L. 579 1 , cf.irl.no It "mutilus
(> mulitus ?) ueruex", et britt.nolit (de .multo) "monton". M.L.5739;
plus giniralement "mutili, tronqui, icourti". S 1 emploie des personnes
et des cboses, au propre et an figuri.
S'y rattacbent: muticus: nsiti dans mutica spica , Varr., R.R.1,48,3,
M.L.5787; mutila,-Os (dijA dans Tir.); M.L.5789 et admutilo ; mutilatis,
muti litas (tardifs); immutilatus ( Sali‘. ap. Non. 366,18); et 1 inmuti latus,
integer, Cod.Theod.4,33,1.
Certaines formes romanes remontent A *mutidus, M.L.5788. Cf.pent-
etre anssi M.L.5793 *mUtt- et 5793 *mutius •
Pas d*itymologie certaine. L*adj. qui sert anssi de nom propre
=== mucus headword ===
39293:Formes nominales et ddrivds: mucor; mucidus "noisi" et "morveux",
39681:prend le sens de "qui a da flair" (par opposition i mucidus, mucSsus ):
60122:mucidus.
```


## [2026-09-07T17:46:24.527Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n 39280,39320p LAT.txt",
 "description": "Read Ernout-Meillet mungo/mucus"
}
```


### [2026-09-07T17:46:24.583Z] TOOL RESULT

```
y a des correspondants seuleAent en indo-iranien: skr. m akfii, av.noiu
"bientSt", donc un adverbe propre il*indo-iranien et a 1'italo-celtique.
Irl.no montre que la forne italo-celtique repose sur noks A sans
voyelle finale.
mozlcia: — quasi nodicia, unde et nodicun-, Z pro D sicut solent
Itali dicere ozie pro hodie) Isid.no, y,4. Inexpliqud; v. Sofer, p.110.
-nS: onomatopde, archarque et familibre, correspondant au grec
(U;, usitde surtout dans 1’expression non facere nC "ne pas dire mot",
ou dans P 4 tr,, 57 , nec nu nec na argutas. Cf.n&gid, 'nussd, nuttio,
nUtus.
muc-/mucc-; mQced, -Ss (-ul?), - 8 re: moisir; se couvrir de fleurs,
filer (en pariant du vin; Cat.Agr.143, uinun quod neqUe aceat neque
muceat). Ancien, technique. M.L.5710.
Formes nominales et ddrivds: mucor; mucidus "noisi" et "morveux",
M.L.5711, 57 ia; nUcSscd,-is. • ’
nucus,-\ m.: morve, mucus nasal (les 1. ronanes attysstent .aussi
le sens de "champignon de la mbche d'une lampe", cf. le fr."moucher
la chandelle"); *sur 1 'enploi du pl.mucet en latin vulg., v, Graur,
Mdl.ling., p.13; m UcSsus "norveux" et "noisi; mal mouchd" (par oppos.
i Snunctae, ndris), d'ou "qui manque de flair", cf. Festus s.u.m uger)
mucilSgo: humeur muqueuse, mucositd; cf .tussiIdgSy nUcildgindsus
(Cass.Fel.); nuc(c)iniun n.(Arn.): mouchoir (d'aprbs lacinia, *la-
ciniun?)) nucSdo: morve (Apul.); muculentus :■ norveux. Cf. aussi Mucius.
A cot 4 des formes k voyelle longue et k consonne simple, existent
des doublets A voyelle brbve avec gemination expressive de la consonne,
comme dans les mots qui designent une difformitd physique. Certaines- 741 - magi nor
fornes ro manes remontent i milccus, mUccSsus, *mucceus, *muccdre, dont
le cospoaA exmuccS est at.test 4 k Pompei, CIL JV i3yi, cf. M.L.57°fr"S7 0 y>
et on lit succitud? dans la Mul. Chir. MQcSre, s Ucidus ont aboati a
fr. soidir, ital.socido; muccSre k fr. moucher.
Cf.gf.[xu^a "morVe, sucosit 4 ",'a7to-ry,uaaw "j e souche", pent-etre
lit. snunkii, smiikt i "tosber en gllssant", v. angi, smugan "glisaer",
et e., qui sont loin pour lie sena, caute aussi akr.su AcSti "il d 4 livre".
One aixtre forae de la racine, avec infixe nasal et gutturale sonore
apparaat dana nungd. Le aens presier eat "etre gluant, visqueux".
mflcrS (avec u chee lea pobtea)^ "•Snis m.: pointe (de t°nt objet
piquant, faux, dent, feuille)j dans la 1. militaire "pointe de l' 4 p 4 e",
par opposition k cuspi 3 "pointe de la lance", puis 1 ' 4 p 4 e elle-sese.
Par d 4 rivation: pointe (au aens moral), acuit 4 ; et "extr 4 mit 4 " (ef-
fi 14 e). - Attestd depuia Enn. M.L. 57 iaa.
Ddrivds: mUcrSnStus (Plin.), -iis.
```


## [2026-09-07T17:46:37.375Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && grep -n \"آموخت\\|آموز\" ARY_pages.txt | head -10; echo \"=== moft ===\"; grep -n \"مفت\" ARY_pages.txt | head -10; echo \"=== latin index ===\"; grep -n \"AMUKHTAN\\|AMOKHTAN\\|MOFT\\|MUFT\" ARY_latin_index_pages.txt | head -10",
 "description": "Grep Aryanpur for amuxtan and moft"
}
```


### [2026-09-07T17:46:37.445Z] TOOL RESULT

```
398:در سده‌های شانزدهم و هفدهم میلادی که طی آن آموزش زبانهای خارجی رونق گرفته بود»
3553:سلمان فارسی حفر " کندک" (خندق) را به آنها آموخت.
6613:۱ چم این واژه در زبان پهلوی: آموختن) مزه کردن.
7888:چم این و اجريشه در زبان لاتین : آموختن» آموزاندن,
=== moft ===
7133:۳ چم این واژه در زبان‌های یونانی و لاتین» ارمنی» اسلاوی کهن: نامدار» مفتخر
=== latin index ===
```


## [2026-09-07T17:46:46.868Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^مفت\\|^مفت‌\\|مفت: \" MON_part1.txt MON_part2.txt | head -10; echo \"=== context 29540 ===\"; sed -n 29532,29545p MON_part1.txt",
 "description": "Find Mo'in moft headword"
}
```


### [2026-09-07T17:46:46.944Z] TOOL RESULT

```
MON_part1.txt:1424:مفتضح کردن, او را مفتضح نمودن. 
MON_part1.txt:14832:مفتون شدن. (مص م.) در فتنه انداختن. فتنه 
MON_part1.txt:27039:مفتول. (مکد.) دستگاهی که بدون سیم 
MON_part1.txt:46651:مفت و باوه گفتن. جاروت از مذگان کردن: 
MON_part1.txt:82389:مفتول‌های آهنی که دارای نوک‌های تبزند 
MON_part1.txt:90735:مفتش حساب. مباشر؛ ج. ضابطون» ضابطین» 
MON_part2.txt:19951:مفتون و شیفتةٌ آن بودن. 
MON_part2.txt:41573:مفتو ح؛ مانند: عین و حول. 
MON_part2.txt:44783:مفتخر؛ ماهات کننده. 
MON_part2.txt:48070:مفت» زایکان 
=== context 29540 ===
در کیسه ریزند و در آن دیگ اندازند و 
نجو شانند تا مهرا شود بعد از آن صان 
کرده بنو شند. 

پخته خوار: ۲ [- بسخته خوارنده - 
پسخته خور] (افا. ص‌مر.) آرام طلب و 


گرانجان. مفت خور: گداء انگل. داماد. 
پسخه‌رای: ۳۰-۷ [ف. ۳۵ (ص‌سر.) 
آزموده؛ مجرب. فهمیده» عاقل» لب. 
پخچ: 6 (- پخج - پخش] (ص.) پهن؛ 
بهن شده کو فته» پخ. پخش» پخج. پژمر ده.
```


## [2026-09-07T17:46:54.013Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n 48060,48078p MON_part2.txt",
 "description": "Mo'in moft context"
}
```


### [2026-09-07T17:46:54.066Z] TOOL RESULT

```
(امص.) جماع» ارمش. 
محاملت: (-۱۱6-))10۱1۵ ۱۱۵ (ع. محامله | 
(مصل.) خوش رفتاری کردن؛ به نیکویی 
معامله کردن. چرب زبانی کردن. (امص.) 
خوش رفتاری. چرب زبانی» ج. مجاملات. 
محامله کار: ۲ (0 )۸ ۱۱۵10۸ [ع. 
ف.](ص‌فا.) کسی که چرب زبانی و تملق 
بکار برد. 

محجان؛: 21117 اع. ف. محانی | ص.) 
مفت» زایکان 

محانب: 0۱021۵ [ع.] (افا.) دور شونده» 
دوری کز بننده؛ سق. موالف. (هس.) خط 
مستقیمی را مجانب یک منحنی میگو یند که 
چون نقطه‌ای در روی منحنی حرکت کند و 
به سمت بی‌نهایت رود فواصل این نقطه از 
این خط مرتب کم شود و میل به صفر کند. 
ضح. دو خط منحنی می توانند مجانب
```


## [2026-09-07T17:47:05.755Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb && for u in \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/mews-\" \"https://en.wiktionary.org/wiki/mukti\"; do echo \"### $u\"; python3 tools/fetch_source.py \"$u\" --note \"page 338: PIE *mews- (moss) and Sanskrit mukti\" 2>&1 | tail -1; done; cd data/verification/sources/web && for f in $(python3 -c \"\nimport hashlib\nfor u in ['https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/mews-','https://en.wiktionary.org/wiki/mukti']:\n    print(hashlib.sha1(u.encode()).hexdigest()[:16])\n\"); do echo \"#### $f\"; python3 -c \"\nt=open('$f.txt',encoding='utf-8').read()\ni=t.find('From Wiktionary')\nprint(t[i:i+1200])\n\"; done",
 "description": "Archive and read PIE mews- and mukti"
}
```


### [2026-09-07T17:47:07.070Z] TOOL RESULT

```
Exit code 1
### https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/mews-
python3: can't open file '/home/sfmqrb/tools/fetch_source.py': [Errno 2] No such file or directory
### https://en.wiktionary.org/wiki/mukti
python3: can't open file '/home/sfmqrb/tools/fetch_source.py': [Errno 2] No such file or directory
(eval):cd:1: no such file or directory: data/verification/sources/web
```


## [2026-09-07T17:47:12.250Z] TOOL CALL #71: Bash

```json
{
 "command": "for u in \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/mews-\" \"https://en.wiktionary.org/wiki/mukti\" \"https://en.wiktionary.org/wiki/%E0%A4%AE%E0%A5%81%E0%A4%A3%E0%A5%8D%E0%A4%A0\"; do echo \"### $u\"; python3 /home/sfmqrb/git/rishe/tools/fetch_source.py \"$u\" --note \"page 338: PIE *mews- (moss), Sanskrit mukti / munth\" 2>&1 | tail -1; done",
 "description": "Archive PIE mews- and Sanskrit pages"
}
```


### [2026-09-07T17:47:15.882Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/mews-
/home/sfmqrb/git/rishe/data/verification/sources/web/2eb3f548912964a3.txt
### https://en.wiktionary.org/wiki/mukti
/home/sfmqrb/git/rishe/data/verification/sources/web/906fc00133b6a768.txt
### https://en.wiktionary.org/wiki/%E0%A4%AE%E0%A5%81%E0%A4%A3%E0%A5%8D%E0%A4%A0
/home/sfmqrb/git/rishe/data/verification/sources/web/6276941964af3965.txt
```


## [2026-09-07T17:47:19.593Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 2eb3f548912964a3 906fc00133b6a768 6276941964af3965; do echo \"#### $f\"; python3 -c \"\nt=open('$f.txt',encoding='utf-8').read()\ni=t.find('From Wiktionary')\nprint(t[i:i+1100])\n\"; done",
 "description": "Read archived Wiktionary pages"
}
```


### [2026-09-07T17:47:20.867Z] TOOL RESULT

```
#### 2eb3f548912964a3
From Wiktionary, the free dictionary

 This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.

 Proto-Indo-European
 [ edit ] 

 Root
 [ edit ] 

 *mews- [ 1 ] 

 moss 

 Derived terms
 [ edit ] 

 Terms derived from the Proto-Indo-European root *mews- (10 c, 0 e) 

 *mews-o-m 
 Proto-Germanic: *meusą [ 2 ] 
 Old English: mēos Middle English: mese , messe , mes , meose English: meese , meece 
 Scots: mese 

 Middle Dutch: mies 

 Old High German: mios 
 Alemannic German: Mies 

 *mus-o-m 
 Proto-Germanic: *musą ( see there for further descendants ) [ 3 ] 

 *mus-o-s 
 Proto-Balto-Slavic: *muśas 
 Lithuanian: mū̃sas 

 Proto-Slavic: *mъxъ ( see there for further descendants )

 *mows-ko-s 
 Italic:
 Latin: mūscus 

 *mews-yeh₂ 
 > ? Proto-Germanic: *miuzijō ( “ swamp ” ) ( see there for further descendants )

 *mus-ro-
 > ? Proto-Armenian: *mus-r- 
 Old Armenian: մամուռ ( mamuṙ , “ moss ” ) 

 Root
 [ edit ] 

 *mews- [ 4 ] 

 to shut 

 D
#### 906fc00133b6a768
From Wiktionary, the free dictionary

 English
 [ edit ] 

 Etymology
 [ edit ] 

 Borrowed from Sanskrit मुक्ति ( mukti ) .

 Noun
 [ edit ] 

 mukti ( uncountable ) 

 Feminine synonym of masculine substantive noun मोक्ष ( mokṣa , “ liberation ” ) .
 Synonym: moksha 

 Related terms
 [ edit ] 

 jivanmukti 

 Translations
 [ edit ] 

 liberation — see also moksha 

 Polish: mukti   n 

 Russian: му́кти ( múkti ) 

 Sanskrit: मुक्ति   (sa) ( mukti ) 

 Retrieved from " https://en.wiktionary.org/w/index.php?title=mukti&oldid=90327409 "

 Categories : English terms borrowed from Sanskrit 
 English terms derived from Sanskrit 
 English lemmas 
 English nouns 
 English uncountable nouns 
 en:Hinduism 

 Hidden categories: Pages with entries 
 Pages with 1 entry 
 Entries with translation boxes 
 Terms with Polish translations 
 Terms with Russian translations 
 Terms with Sanskrit translations 

 This page was last edited on 25 April 2026, at 01:11.

 Definitions and other text are available under the Creative Commons Attribution-ShareAlike License ; additional terms may apply. By using
#### 6276941964af3965
d
```


## [2026-09-07T17:49:42.659Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && tail -14 index.jsonl | python3 -c \"\nimport sys,json\nfor l in sys.stdin:\n    d=json.loads(l); print(d['url'])\n\"",
 "description": "List archived URLs"
}
```


### [2026-09-07T17:49:44.627Z] TOOL RESULT

```
https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/m%C3%BAHs
https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/morw%C3%ADs
https://en.wiktionary.org/wiki/%D9%85%D9%88%DB%8C%D9%87
https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/mews-
https://en.wiktionary.org/wiki/%D9%85%D8%B3%D8%AA%D9%85%D9%86%D8%AF
https://en.wiktionary.org/wiki/mukti
https://en.wiktionary.org/wiki/%E0%A4%AE%E0%A5%81%E0%A4%A3%E0%A5%8D%E0%A4%A0
https://en.wiktionary.org/wiki/%D9%85%D8%B4%D8%AA
https://en.wiktionary.org/wiki/mucro
https://en.wiktionary.org/wiki/moveo
https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/mu%C5%A1t%C3%AD%C5%A1
https://bosworthtoller.com/search?q=meo
https://www.etymonline.com/word/move
https://en.wiktionary.org/wiki/%E0%A4%AE%E0%A5%8B%E0%A4%9C%E0%A4%BC%E0%A4%BE
```


## [2026-09-07T17:49:50.368Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -o '\"url\": \"[^\"]*\"' index.jsonl | grep -iE \"mud|/moss|mustard|/match|/moist|/mucus|/smuggle|mewk|mews-|/mukti|%D8%A2%D9%85%D9%88%D8%AE%D8%AA%D9%86|%D9%85%D9%81%D8%AA\\\"\" | sort -u",
 "description": "Verify my archived URLs in index"
}
```


### [2026-09-07T17:49:50.450Z] TOOL RESULT

```
"url": "https://en.wiktionary.org/wiki/%D8%A2%D9%85%D9%88%D8%AE%D8%AA%D9%86"
"url": "https://en.wiktionary.org/wiki/%D9%85%D9%81%D8%AA"
"url": "https://en.wiktionary.org/wiki/mukti"
"url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/mewk-"
"url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/mews-"
"url": "https://www.etymonline.com/word/match"
"url": "https://www.etymonline.com/word/moist"
"url": "https://www.etymonline.com/word/moss"
"url": "https://www.etymonline.com/word/mucus"
"url": "https://www.etymonline.com/word/mud"
"url": "https://www.etymonline.com/word/mustard"
"url": "https://www.etymonline.com/word/smuggle"
```


## [2026-09-07T17:58:52.471Z] TOOL CALL #75: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/mk338.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nE = \"https://www.etymonline.com/word/\"\nW = \"https://en.wiktionary.org/wiki/\"\n\ndata = {\n \"pdf_page\": 338,\n \"book_page\": 308,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-07\",\n \"entries\": []\n}\n\n# ---------------------------------------------------------------- entry 0\ne0 = {\n \"entry\": 0,\n \"root\": \"Meu 1\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *mew- / *mewə-, *mu- 'wet, damp; dirt, filth; to wash' (Pokorny 741-743 '1. meu-, meuə-, mu-'; Watkins/AHD *meu- 'damp')\",\n \"note\": \"Pokorny 741-743 heads the entry '1. meu-, meuə-, mu-', Meaning: 'wet; dirt; to wash, etc.'; Walde-Pokorny II 249 has the same root as 'feucht, moderig, netzen, unreine Fluessigkeit (auch Harn), beschmutzen, auch in Nasses tauchen, waschen'; Watkins (AHD appendix) 'meu-. Damp; with derivatives referring to swampy ground and vegetation and to figurative qualities of wetness. [Pok. 1. meu- 741.]'. The language label (Indo-European), the gloss 'damp, dirty' and the page reference POK:741 are all correct, and Nourai's numbering Meu 1 / Meu 2 reproduces Pokorny's own 1. meu- (p. 741) versus 2. meu-, meuə- 'to push away' (p. 743, = Latin movere), so the redirect entry on this page is also correctly placed. Of the six branches Nourai draws, five are exactly Watkins's *meu- entry (Germanic *meus- > moss, *mus-to- > Latin mustus > must/mustard, plus the Iranian mūθra-); only the 'Middle Greek' mud box is wrong (node 6).\",\n \"note_fa\": \"ریشهٔ هندواروپایی آغازین *mew- (با گونه‌های *meuə-، *mu-) به معنی «نمناک، خیس؛ چرک و پلیدی؛ شستن» است؛ پوکورنی در صفحهٔ ۷۴۱ تا ۷۴۳ آن را با همین معنا آورده و والده-پوکورنی (ج۲ ص۲۴۹) آن را «مرطوب، پوسیده، خیس‌کردن، مایع ناپاک (از جمله ادرار)، آلودن، شستن» معنی می‌کند. واتکینز نیز در پیوست ریشه‌های هندواروپایی فرهنگ American Heritage همین ریشه را با معنی «نمناک» و با ارجاع به همان صفحهٔ پوکورنی ثبت کرده است. پس برچسب زبانی، معنی «نمناک، چرکین» و ارجاع POK:741 هر سه درست است و شماره‌گذاری نورایی (Meu 1 / Meu 2) نیز با تفکیک خودِ پوکورنی می‌خواند. ادعای نورایی در بارهٔ ریشه درست است؛ تنها برچسب زبانِ جعبهٔ mudde («یونانی میانه») نادرست است (گرهٔ ۶).\",\n \"sources\": [E+\"mud\", E+\"moss\", W+\"Reconstruction:Proto-Indo-European/mews-\"],\n \"ref_check\": [\n   {\"ref\": \"POK:741\", \"status\": \"supports\",\n    \"note\": \"POK_full.txt (indo-european.info edition of IEW): 'Root/ lemma: meu-1, meuə-, mu- | Meaning: wet; dirt; to wash, etc.. | Material: A. Old Indic mutra- n. \\\"urine\\\", Avestan mūθra- n. \\\"filth, smut\\\" (: Middle Low German modder etc.)' ... 'References: WP. II 249 ff., WH. II 126 f. ...; Page(s): 741-743'. Exactly Nourai's root, gloss and page.\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. II p. 249 (WLD_Bd2_pages.txt leaf 254)\", \"stance\": \"supports\",\n    \"note\": \"'1. meu- \\\"feucht, moderig, netzen, unreine Fluessigkeit (auch Harn), beschmutzen, auch in Nasses tauchen, waschen\\\"'; and 'Ai. mūtra- n. \\\"Harn\\\", av. mūθra- n. \\\"Unreinigkeit, Schmutz\\\" (: ndl. modder usw.)'.\"},\n   {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt line 760 s.v. meu-\", \"stance\": \"supports\",\n    \"note\": \"'meu-. Damp; with derivatives referring to swampy ground and vegetation and to figurative qualities of wetness. 1. Extended form *meus- in Germanic *meus-, *mus- ... 3. Suffixed zero-grade form *mus-to- in Latin mustus, new, newborn (< \\\"wet\\\"): MUST(3), MUSTARD. [Pok. 1. meu- 741.]'\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, IEC.txt s.vv. meus-, mūtros, mudos, mustos\", \"stance\": \"supports\",\n    \"note\": \"'meus- \\\"moss, mildew\\\"'; 'mūtros (mutoro-) (1) \\\"foul; filth, mud, urine\\\": Skt. mūtram n. \\\"urine\\\"; Av. mūθrəm n. \\\"filth\\\"; ... MHG moder m. \\\"rot; marsh\\\"; G Moder n. \\\"mud\\\"'; 'mustos ... \\\"mouldy, foul\\\"'. Mann groups the same material under the same base.\"}\n ],\n \"nodes\": []\n}\n\ne0[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Avestan\", \"words\": \"mŭthra\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Avestan mūθra- n. is a real word, attested in the Videvdad and the Frahang; Bartholomae (AiW col. 1189 f.) glosses it 'Exkremente, faeces', with the extended value 'sva. \\\"Unrat, Unflat\\\"' (filth, dirt), and equates it there with 'ai. mūtra- n. \\\"Harn\\\"' (urine). The formation is *mu-tro-, i.e. the zero grade *mū- of *mew- plus the instrumental/result suffix *-tro-, with the regular Iranian development of *-tr- to -θr-. Its Middle Persian continuation is mūtrīh 'urine' (Horn no. 138, p. 285). Nourai's gloss 'dirty liquid, urine' thus merges the Avestan sense ('filth, excrement') with the Indo-Aryan and Middle Persian sense ('urine'); Walde-Pokorny II 249 argues from exactly this Avestan meaning that 'filth' is the older value and 'urine (as a washing agent)' the secondary one, so the gloss is defensible but the order of senses is back to front. The derivation of the word from the root, and its use as the Iranian witness for the root, are standard and are repeated even in Etymonline s.v. mud ('Avestan muthra- \\\"excrement, filth\\\"').\",\n \"derivation_fa\": \"واژهٔ اوستایی mūθra- واقعی و در وندیداد و فرهنگ اوئیم به‌کار رفته است؛ بارتولمه (فرهنگ ایرانی باستان، ستون ۱۱۸۹ به بعد) آن را «مدفوع، فضولات» و در معنای گسترده «ناپاکی، پلیدی» می‌داند و آن را با سنسکریت mūtra- «ادرار» هم‌ریشه می‌شمارد. ساخت واژه *mū-tra- است، یعنی درجهٔ صفرِ ریشهٔ *mew- به‌همراه پسوند ابزار/نتیجهٔ *-tra-، و خوشهٔ *-tr- در ایرانی به‌قاعده به -θr- بدل شده است؛ صورت فارسی میانهٔ آن mūtrīh «ادرار» است (هرن، بند ۱۳۸، ص ۲۸۵). معنایی که نورایی داده («مایع چرکین، ادرار») آمیزه‌ای از معنای اوستایی «پلیدی» و معنای هندی و پهلوی «ادرار» است؛ والده-پوکورنی (ج۲ ص۲۴۹) درست بر پایهٔ همین معنای اوستایی استدلال می‌کند که معنای «پلیدی» کهن‌تر و «ادرار» ثانوی است. در مجموع ادعای نورایی درست است و تنها ترتیب معناها جابه‌جا شده.\",\n \"sources\": [E+\"mud\"],\n \"ref_check\": [\n   {\"ref\": \"POK:741\", \"status\": \"supports\", \"note\": \"POK_full.txt s.v. meu-1: 'Old Indic mutra- n. \\\"urine\\\", Avestan mūθra- n. \\\"filth, smut\\\" (: Middle Low German modder etc.)'.\"},\n   {\"ref\": \"HRN:285\", \"status\": \"supports\", \"note\": \"HRN.txt leaf 306 (printed p. 285), no. 138: 'mūtrīh \\\"Urin\\\" (Zi.Gl.), mūt (P.-Vend.). aw. mūθra-; ai. mūtra- \\\"Urin\\\".' Horn's Pahlavi list, exactly the equation Nourai draws.\"},\n   {\"ref\": \"KLN:1008\", \"status\": \"not_found\", \"note\": \"Klein 1966 p. 1008 (KLN_1966.txt leaf 516, calibrated on leaf 438 = p. 853) falls in the 'member / membrane / memento' run and has nothing on mūθra or urine. The Klein entries that do support the claim are s.v. mud (leaf 542, ~p. 1060: 'derive fr. I.-E. base *meu-, \\\"wet, moist\\\"') and s.v. moss (leaf 540, ~p. 1056), so KLN:1008 looks like a slip for ~1056/1060.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW col. 1189 f. (BRT.txt lines 20580-20582)\", \"stance\": \"partial\",\n    \"note\": \"'j., g. mūθra- n. \\\"Exkremente, faeces\\\": ... a) sva. \\\"Unrat, Unflat\\\" ... ai. mūtra- n. \\\"Harn\\\". - Pue.: ...' - the word and the Indic equation confirmed, but the Avestan gloss is 'excrement/filth', not 'urine'.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. II p. 249\", \"stance\": \"supports\",\n    \"note\": \"'Ai. mūtra- n. \\\"Harn\\\", av. mūθra- n. \\\"Unreinigkeit, Schmutz\\\" (: ndl. modder usw.)', with the explicit argument that because of Av. mūθra- 'Unreinigkeit, Schmutz' the priority of the sense 'Harn als Waschmittel' is 'unwahrscheinlich'.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann s.v. mūtros (1)\", \"stance\": \"supports\",\n    \"note\": \"'mūtros (mutoro-) (1) \\\"foul; filth, mud, urine\\\": Skt. mūtram, n. \\\"urine\\\"; Av. mūθrəm, n. \\\"filth\\\"; Gk. musarós \\\"foul, dirty\\\" ... MHG moder, m. \\\"rot; marsh\\\"; G Moder, n. \\\"mud\\\"'.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Germanic\", \"words\": \"meus\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Nourai's 'Germanic meus' is Watkins's s-extension: AHD s.v. meu- '1. Extended form *meus- in Germanic *meus-, *mus- in: a. Old English mos, bog: MOSS; b. Old Norse mosi, bog, moss ... 2. Germanic suffixed form *meuz-i- in Old Norse myrr, bog: MIRE'. The same s-enlargement is Pokorny's separate headword meu-s- and Klein's 'I.-E. *meu-s-, ... an -s-enlargement of base *meu-, \\\"moist; marsh; moss\\\"'. Proto-Germanic *meusa- (< *mews-o-m) yields Old English meos 'moss plant', Old High German mios, Middle Dutch mies, Old Norse mosi; the ablaut variant *musa- yields OE mos 'bog', OHG/MHG mos, German Moos. Outside Germanic the same *mews- gives Latin muscus 'moss' (< *mows-ko-s) and Lithuanian musai 'mold, mildew'. The gloss 'damp' is Watkins's own wording. The one formal quibble: this is a reconstruction, so it should be printed *meus-, not meus.\",\n \"derivation_fa\": \"آنچه نورایی «ژرمنی meus» می‌نویسد در واقع گونهٔ گسترده‌شدهٔ ریشه با پسوندِ s است: واتکینز زیر *meu- می‌آورد «صورت گستردهٔ *meus- در ژرمنی *meus-، *mus-: انگلیسی کهن mos «باتلاق» > moss». همین گسترش با s در پوکورنی سرواژهٔ جداگانهٔ meu-s- است و کلاین نیز آن را «*meu-s-، گسترشِ s-دارِ پایهٔ *meu- به معنی نمناک، باتلاق، خزه» می‌داند. ژرمنی آغازین *meusa- به انگلیسی کهن meos «خزه»، آلمانی علیای کهن mios و نورس کهن mosi رسیده و گونهٔ آواگردیدهٔ *musa- به انگلیسی کهن mos «باتلاق» و آلمانی Moos. بیرون از ژرمنی همین ریشه لاتینی muscus «خزه» و لیتوانیایی mūsai «کپک» را داده است. ادعای نورایی درست است؛ تنها باید این صورت را با ستاره (*meus-) نوشت چون بازسازی‌شده است، نه واژه‌ای گواهی‌شده.\",\n \"sources\": [E+\"moss\", W+\"Reconstruction:Proto-Indo-European/mews-\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt line 760 s.v. meu-: '1. Extended form *meus- in Germanic *meus-, *mus- in: a. Old English mos, bog: MOSS; b. Old Norse mosi, bog, moss, akin to the Scandinavian source of LITMUS. 2. Germanic suffixed form *meuz-i- in Old Norse myrr, bog: MIRE; (QUAGMIRE).'\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. moss (KLN_1966.txt line 24480, leaf 540 ~ p. 1056)\", \"stance\": \"supports\",\n    \"note\": \"'... rel. to OE. meos, \\\"moss\\\", ON. mosi, ... fr. I.-E. *meu-s-, whence also L. muscus, \\\"moss\\\", Lith. musai, \\\"mold, mildew\\\", OSlav. muchu, \\\"moss\\\" ... I.-E. *meu-s- is an -s-enlargement of base *meu-, \\\"moist; marsh; moss\\\".'\"},\n   {\"src\": \"IEC\", \"where\": \"Mann s.v. meus-\", \"stance\": \"supports\",\n    \"note\": \"'meus- \\\"moss, mildew\\\". Cf. mus-: MHG mies, sm. & n. \\\"moss\\\"; OE meos, id.; cf. Blg. muxal ... \\\"mildew\\\"'.\"},\n   {\"src\": \"POK\", \"where\": \"IEW s.v. meu-s- (POK_full.txt line 60609)\", \"stance\": \"supports\",\n    \"note\": \"Pokorny sets up 'Root / lemma: meu-s-' as a separate headword immediately after meu-1, i.e. the same s-extension Watkins uses.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 3, \"lang\": \"English\", \"words\": \"moss\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Old English mos 'bog, marsh' and the related meos 'moss plant' fall together in Middle English mos, and modern moss carries both senses because moss is the characteristic plant of boggy ground - 'It is impossible to say which sense is original' (Etymonline s.v. moss). Formally moss continues the zero-grade Proto-Germanic *musa- rather than *meusa- (which survives only in dialectal meese/meece), so the arrow Germanic *meus- > English moss is right at the level of the root but goes through the ablaut variant. Medieval Latin mossa and French mousse are borrowings from the same Germanic source, not from Latin muscus. The English word thus needs no reference of its own; the derivation is uncontroversial.\",\n \"derivation_fa\": \"انگلیسی کهن mos «باتلاق، مرداب» و همریشهٔ آن meos «خزه» در انگلیسی میانه در صورت mos یکی شدند و moss امروزی هر دو معنا را دارد، زیرا خزه گیاه شاخص زمین‌های باتلاقی است؛ اتیمانلاین می‌گوید «نمی‌توان گفت کدام معنا اصلی است». از نظر آوایی moss ادامهٔ درجهٔ صفرِ ژرمنی آغازین *musa- است نه *meusa- (که تنها در گونهٔ گویشی meese مانده)، پس پیکان «ژرمنی *meus- ← انگلیسی moss» در سطح ریشه درست است ولی از گونهٔ آواگردیده گذشته. لاتینی میانه mossa و فرانسوی mousse نیز وام‌واژه‌هایی از همین سرچشمهٔ ژرمنی‌اند. ادعای نورایی درست است.\",\n \"sources\": [E+\"moss\", W+\"Reconstruction:Proto-Indo-European/mews-\"],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this node; the claim is Watkins's, checked at the parent node (AHD s.v. meu- '...Old English mos, bog: MOSS').\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. moss\", \"stance\": \"supports\",\n    \"note\": \"'moss, n. - ME. mos, fr. OE. mos, \\\"marsh, moor\\\", rel. to OE. meos, \\\"moss\\\" ... fr. I.-E. *meu-s-'.\"},\n   {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt line 1892 index: 'MOSS meu-'\", \"stance\": \"supports\",\n    \"note\": \"The word index of the Watkins appendix assigns MOSS to the root meu-, i.e. Nourai's Meu 1.\"},\n   {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/moss\", \"stance\": \"supports\",\n    \"note\": \"'both are from Proto-Germanic *musan ... These are from PIE *meus- \\\"damp\\\", with derivatives referring to swamps and swamp vegetation'.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 4, \"lang\": \"Latin\", \"words\": \"mustus\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Latin mustus, -a, -um 'young, new, fresh' is a word of the rustic vocabulary, used above all in mustum uinum 'new wine' and in the substantivised neuter mustum 'must, grape juice' (Ernout-Meillet s.v. mustus, citing Cato's musta agna 'newborn ewe-lamb'). Pokorny 742, under the d-extension meu-d-, derives it from an -es- stem: 'From an -es-stem m(e)udes- have derived: Latin mustus (*muds-to-s) \\\"young, new, fresh\\\" (originally \\\"damp, humid, wet\\\")'; Watkins has the same thing more simply as 'Suffixed zero-grade form *mus-to- in Latin mustus, new, newborn (< \\\"wet\\\")'. Nourai's double gloss 'wet, new' reproduces precisely that etymological gloss plus the attested one, so the node is right as drawn. The one caveat: Ernout-Meillet close the article 'Pas d'etymologie claire', so the connection with *meu- is Pokorny's and Watkins's rather than universally granted.\",\n \"derivation_fa\": \"لاتینی mustus «تازه، نو، جوان» واژه‌ای از زبان روستایی است که بیشتر در ترکیب mustum uinum «شرابِ نو» و در صورت اسمیِ خنثای mustum «شیرهٔ انگور، مویز‌آب» به کار می‌رفته (ارنو-میه، ذیل mustus، با شاهدِ کاتو musta agna «برهٔ نوزاد»). پوکورنی در صفحهٔ ۷۴۲ زیر گسترشِ meu-d- آن را از ستاکِ -es- می‌گیرد: «لاتینی mustus (< *muds-to-s) تازه و نو، در اصل نمناک و خیس»؛ واتکینز نیز همان را به صورت «درجهٔ صفرِ پسوند‌دارِ *mus-to-» می‌آورد. پس معنی دوگانه‌ای که نورایی داده («خیس، نو») درست همان معنی ریشه‌شناختی به‌علاوهٔ معنی گواهی‌شده است و گره درست است. تنها نکته اینکه ارنو-میه در پایانِ مقاله می‌نویسد «ریشه‌شناسی روشنی ندارد»، پس این پیوند از پوکورنی و واتکینز است و اجماعی نیست.\",\n \"sources\": [E+\"mustard\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt line 760 s.v. meu-: '3. Suffixed zero-grade form *mus-to- in Latin mustus, new, newborn (< \\\"wet\\\"): MUST(3), MUSTARD.'\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW 742 (POK_full.txt, under meu-d-)\", \"stance\": \"supports\",\n    \"note\": \"'From in -es-stem m(e)udes- have derived: Latin mustus (*muds-to-s) \\\"young, new, fresh\\\" (originally \\\"damp, humid, wet\\\")'.\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. mustus (LAT.txt line ~40059)\", \"stance\": \"partial\",\n    \"note\": \"'mustus, -a, -um: nouveau; musta agna: agnelle nouveau-nee (Caton); mustum uinum: vin nouveau. Terme de la langue rustique; usite surtout au neutre substantive mustum \\\"vin nouveau\\\" ... Pas d'etymologie claire.' - word and senses confirmed, the *meu- etymology not endorsed.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann s.v. mustos\", \"stance\": \"partial\",\n    \"note\": \"'mustos (fr. **mut-tos or **mud-tos?) \\\"mouldy, foul; mould, filth\\\" ... Lat. (isophone?) mustus, adj. \\\"new - of wine\\\" ... E must, s. (in sense of \\\"mould, mildew\\\")'. Mann files Latin mustus here but flags it as a possible isophone.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. moss\", \"stance\": \"supports\",\n    \"note\": \"'... and perh. L. mustus, \\\"fresh, new\\\" (if fr. *mus-tos, \\\"wet, moist\\\"), whence mustum (short for mustum vinum), \\\"new wine\\\"'.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 5, \"lang\": \"English\", \"words\": \"must 2; mustard\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"must 'new wine' is one of the oldest Latin loans in English: Old English must, straight from Latin mustum, short for uinum mustum (Etymonline s.v. must (n.1); the same loan gives OHG/German most, Old French moust > French mout, Spanish/Italian mosto), so the arrow Latin > English needs no Romance intermediary. mustard, by contrast, came through French: Old French mostarde 'mustard, mustard plant' (Mod.Fr. moutarde), a derivative of moust 'must', because the condiment was made by working grape must into the ground seed - 'mustard lit. means \\\"seasoned with must\\\"' (Klein s.v. mustard); it is in English as a surname late 12c., as a noun late 13c., and as the plant name by mid-14c. Nourai's label 'must 2' is his own homograph numbering and his gloss 'damp' is the etymological, not the attested, sense; note that the English homograph that really means 'mould, mustiness' is a back-formation from musty (Klein), which Watkins assigns to meug-2, i.e. to the other root on this page, while MUST(3) 'new wine' is the one he puts here.\",\n \"derivation_fa\": \"must «شرابِ نو» از کهن‌ترین وام‌واژه‌های لاتین در انگلیسی است: انگلیسی کهن must یکسر از لاتینی mustum، کوتاه‌شدهٔ uinum mustum (اتیمانلاین ذیل must)؛ همین وام‌گیری در آلمانی most و فرانسوی mout هم دیده می‌شود، پس پیکان «لاتینی ← انگلیسی» نیازی به واسطهٔ رومانسی ندارد. اما mustard از راه فرانسوی آمده: فرانسوی کهن mostarde (امروز moutarde) برساختهٔ moust «شیرهٔ انگور»، زیرا این چاشنی را با آمیختنِ شیرهٔ انگور به دانهٔ آسیاب‌شده می‌ساختند؛ کلاین می‌نویسد «mustard تحت‌اللفظ یعنی چاشنی‌شده با must». برچسب «must 2» شماره‌گذاری خودِ نورایی است و معنی «نمناک» معنای ریشه‌شناختی است نه معنای گواهی‌شده. توجه شود که همنگارهٔ انگلیسی که به معنی «کپک» است، بازساختی از musty است و واتکینز آن را زیر ریشهٔ دیگرِ همین صفحه (meug-2) می‌گذارد. ادعای نورایی در کل درست است.\",\n \"sources\": [E+\"mustard\"],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"no reference on the node; the parent's 'AHD' covers it - AHD_watkins1985.txt s.v. meu-: '*mus-to- in Latin mustus ... : MUST(3), MUSTARD'.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.vv. mustard, must (KLN_1966.txt lines 24755-24761)\", \"stance\": \"supports\",\n    \"note\": \"'mustard, n. - ME., fr. OF. moustarde (F. moutarde), fr. moust (F. mout), \\\"new wine, must\\\", fr. L. mustum. Accordingly mustard lit. means \\\"seasoned with must\\\"'; and 'must, n., mold, mustiness. - Prob. back formation fr. musty.'\"},\n   {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/mustard (with must (n.1) quoted in the same page)\", \"stance\": \"supports\",\n    \"note\": \"'must (n.1) \\\"new wine\\\", Old English must, from Latin mustum ... short for vinum mustum \\\"fresh wine\\\", neuter of mustus \\\"fresh, new, newborn\\\"'; 'mustard ... from Old French mostarde ... from moust \\\"must\\\"'.\"},\n   {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt lines 1897-1898 index\", \"stance\": \"supports\",\n    \"note\": \"'MUST(3) ~ meu-' and 'MUSTARD meu-' in the word index, but 'MUSTY meug-2' - confirming that only the 'new wine' homograph belongs to this root.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 6, \"lang\": \"Middle Greek\", \"words\": \"mudde\",\n \"verdict\": \"transcription_suspect\",\n \"error_in\": \"book\",\n \"book_prints\": \"Middle Greek\",\n \"correct_form\": \"Middle Low German\",\n \"derivation\": \"There is no Middle Greek word mudde. The source of English mud is Middle Low German mudde 'mud' (beside Middle Dutch modde 'thick mud'), and every source says so: Klein s.v. mud 'ME. mode, mudde, of LG. origin. Cp. OLG., MLG. mudde, \\\"mud\\\", muddig, \\\"muddy\\\", which derive fr. I.-E. base *meu-, \\\"wet, moist\\\", whence also MDu., Du. modder, \\\"filth, dregs\\\"'; Etymonline s.v. mud 'cognate with and probably from Middle Low German mudde, Middle Dutch modde \\\"thick mud\\\", from Proto-Germanic *mud-, from PIE *(s)meu-/*mu-'; Pokorny 741 already prints '(: Middle Low German modder etc.)' right beside Avestan mūθra-, and Mann lists 'OHG mot, MHG mot, LG modd, G Mutt \\\"mud, marsh, sediment\\\"' as the cognates of English mud. I rendered the printed page (pdftoppm -f 338, saved as data/verification/sources/refs/ocr/BOOK/338.png) and the box really reads 'Middle Greek [AHD] | mudde : wet earth', so the extraction is faithful and the error is Nourai's own - almost certainly a slip for 'Middle German'. The reference 'AHD' is loose too: the 1985 Watkins edition of the same appendix has no MUD at all under meu-. Apart from the language label, the derivation (root 'wet, dirty' > Germanic word for wet earth > English mud) is correct.\",\n \"derivation_fa\": \"واژه‌ای به نام mudde در «یونانی میانه» وجود ندارد. سرچشمهٔ mud انگلیسی، آلمانی سُفلای میانه (Middle Low German) mudde «گِل» است، در کنار هلندی میانه modde «گِل غلیظ»؛ کلاین ذیل mud می‌نویسد «انگلیسی میانه mudde، از اصل آلمانی سفلی؛ قس MLG mudde ... که از پایهٔ هندواروپایی *meu- «خیس، نمناک» می‌آید»، و اتیمانلاین نیز همان را با ارجاع به ژرمنی آغازین *mud- آورده است؛ خودِ پوکورنی در صفحهٔ ۷۴۱ در کنار mūθra- اوستایی «آلمانی سفلای میانه modder» را ثبت کرده است. تصویر صفحهٔ چاپی (ص ۳۰۸ کتاب، برگ ۳۳۸ پی‌دی‌اف) را دیدم: در جعبه به‌روشنی «Middle Greek» چاپ شده، پس خطای خوانش اسکن نیست بلکه خطای چاپی خودِ کتاب است و به احتمال بسیار به‌جای «Middle German» نشسته. جز این برچسب زبانی، مسیرِ اشتقاق (ریشهٔ «خیس، چرکین» ← واژهٔ ژرمنی برای خاکِ خیس ← mud انگلیسی) درست است.\",\n \"sources\": [E+\"mud\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"not_found\",\n    \"note\": \"AHD_watkins1985.txt s.v. meu- (line 760) lists MOSS, MIRE, QUAGMIRE, LITMUS, MUST(3), MUSTARD, MYRIAD, MYSOPHILIA/-PHOBIA - no MUD; and the word index has no 'MUD meu-' line. The 1976 New College appendix Nourai cites may have had it, but the language there could only have been Middle Low German.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. mud (KLN_1966.txt line 24571, leaf 542 ~ p. 1060)\", \"stance\": \"contradicts\",\n    \"note\": \"'mud, n., wet earth. - ME. mode, mudde, of LG. origin. Cp. OLG., MLG. mudde, \\\"mud\\\" ... which derive fr. I.-E. base *meu-, \\\"wet, moist\\\"' - Low German, not Greek. (Klein's gloss 'wet earth' is also word-for-word Nourai's gloss, which suggests this is the entry he actually used.)\"},\n   {\"src\": \"POK\", \"where\": \"IEW 741 s.v. meu-1\", \"stance\": \"contradicts\",\n    \"note\": \"'Avestan mūθra- n. \\\"filth, smut\\\" (: Middle Low German modder etc.)' - Pokorny's Germanic comparandum, no Greek word of this shape.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann s.v. mtos/mūt- (3)\", \"stance\": \"contradicts\",\n    \"note\": \"'Cognate forms of E mud include OHG mot, m., MHG mot, sn.; LG modd, m.; G Mutt, m. \\\"mud, marsh, sediment\\\"'.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 7, \"lang\": \"English\", \"words\": \"mud\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"mud first appears in English late 14c. as mudde 'moist, soft earth', taken over from (or at least cognate with and reinforced by) Middle Low German mudde in the period of dense Hanseatic and Low Countries contact; it displaced the older native word fen (Etymonline s.v. mud). Semantically it continues the root's core value 'wet dirt' unchanged, and it belongs to the same Germanic family as Middle Dutch/Dutch modder 'filth, dregs' and German Moder. Klein derives it directly 'fr. I.-E. base *meu-, \\\"wet, moist\\\"', so the arrow from the root through a Germanic intermediary to English mud is correct - only the intermediary's language label in the chart is wrong (node 6).\",\n \"derivation_fa\": \"واژهٔ mud نخستین بار در اواخر سدهٔ چهاردهم در انگلیسی به صورت mudde «خاکِ نرمِ نمناک» پیدا می‌شود و از آلمانی سُفلای میانه mudde گرفته شده (یا دست‌کم هم‌ریشهٔ آن است و از آن نیرو گرفته) در دورهٔ داد و ستدِ گستردهٔ هانزایی؛ این واژه جای واژهٔ بومی کهن‌ترِ fen را گرفت (اتیمانلاین). از نظر معنایی همان معنای هستهٔ ریشه («خاکِ خیس و چرکین») را بی‌تغییر نگه داشته و با هلندی modder «لِرد، دُرد» و آلمانی Moder هم‌خانواده است. کلاین آن را یکسر از پایهٔ هندواروپایی *meu- «خیس، نمناک» می‌گیرد؛ پس پیکانِ ریشه ← واسطهٔ ژرمنی ← mud انگلیسی درست است و تنها برچسب زبانِ واسطه در نمودار غلط است (گرهٔ ۶).\",\n \"sources\": [E+\"mud\"],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"no reference on the node; the parent's 'AHD' does not in fact carry MUD (see node 6), but Klein and Etymonline both do.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. mud\", \"stance\": \"supports\",\n    \"note\": \"'mud, n., wet earth. - ME. mode, mudde ... derive fr. I.-E. base *meu-, \\\"wet, moist\\\"'.\"},\n   {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/mud\", \"stance\": \"supports\",\n    \"note\": \"'late 14c., mudde, \\\"moist, soft earth\\\" ... from PIE *(s)meu-/*mu- [Buck], found in many words denoting \\\"wet\\\" or \\\"dirty\\\" ... The older word is fen.'\"},\n   {\"src\": \"IEC\", \"where\": \"Mann s.v. mūt- (3)\", \"stance\": \"supports\",\n    \"note\": \"'In the sense of \\\"liquid filth\\\" cf. also the following Hind. mut \\\"urine\\\" ... Cognate forms of E mud include OHG mot ... LG modd'.\"}\n ]\n})\n\ndata[\"entries\"].append(e0)\n\n# ---------------------------------------------------------------- entry 2\ne2 = {\n \"entry\": 2,\n \"root\": \"Meug\",\n \"verdict\": \"plausible\",\n \"modern_form\": \"PIE *(s)mewk- / *(s)mewg- 'to slip, slide; slimy, slippery; to let loose, release' (Pokorny 744-745 '2. meug-, meuk-: to slide, slip'; Watkins/AHD meug-2 'slimy, slippery')\",\n \"note\": \"Pokorny 744-745 heads 'Root / lemma: meug-2, meuk-, Meaning: to slide, slip', with the note 'also with anlaut. s-'; his section A collects the 'slimy, wet' words (Latin mucus, mucor, e-mungo; Greek myxa, apomyssomai) and his section B the 'release, flee' words (Old Indic muncati, mukti-, Avestan fra-muxti-, Old Persian amu(n)θa, Lith. munku 'escape'). Watkins: 'meug-2. Slimy, slippery; with derivatives referring to various wet or slimy substances and conditions. Enlarged form of meu-. [Pok. 2. meug- 744.]' - which is also why this chart and Meu 1 share the 'wet' gloss. Wiktionary's *(s)mewk- is glossed 'to let loose; to release; to slip away; to escape; to flee'. So the root, the language label and the page reference are right, and 'wet, slippery, to give up, let go, flee, deliver' are all defensible. The verdict is plausible rather than confirmed for one reason: 'describe' is in no source. It is imported from Nourai's attachment of Persian amuxtan 'to learn' (via a gloss 'clarify, describe' invented for Avestan fra-muxti-) to this root - an attachment modern Iranian etymology rejects (see node 1). Note also that Pokorny has a separate meug-1 'to take by surprise, wily' on p. 743-744, which is not this root.\",\n \"note_fa\": \"پوکورنی در صفحهٔ ۷۴۴ تا ۷۴۵ سرواژهٔ «meug-2، meuk-» را با معنی «لیزخوردن، سُریدن» می‌آورد و یادآور می‌شود که گونهٔ s-دار هم دارد؛ بخش الفِ مقاله واژه‌های «لزج و خیس» را گرد آورده (لاتینی mucus، mucor، e-mungo؛ یونانی μύξα) و بخش ب واژه‌های «رها کردن، گریختن» را (سنسکریت muñcáti و mukti-، اوستایی fra-muxti-، پارسی باستان amuθa). واتکینز نیز آن را «لزج، لیز؛ گسترش‌یافتهٔ *meu-» می‌داند و همین توضیح می‌دهد که چرا این نمودار و نمودار Meu 1 در معنی «خیس» شریک‌اند؛ ویکی‌واژه ریشهٔ *(s)mewk- را «رها کردن، آزاد کردن، گریختن» معنی می‌کند. پس ریشه، برچسب زبانی و ارجاع POK:744 درست است و معناهای «خیس، لیز، رها کردن، ول کردن، گریختن، رهانیدن» همه پذیرفتنی‌اند. تنها ایراد، معنی «توصیف کردن» است که در هیچ منبعی نیست و از آنجا وارد شده که نورایی می‌خواسته «آموختن» فارسی را به این ریشه ببندد؛ ریشه‌شناسی امروزی ایرانی این پیوند را نمی‌پذیرد (گرهٔ ۱). پس ادعای نورایی در بارهٔ ریشه با احتیاط پذیرفتنی است.\",\n \"sources\": [W+\"Reconstruction:Proto-Indo-European/mewk-\", E+\"mucus\"],\n \"ref_check\": [\n   {\"ref\": \"POK:744\", \"status\": \"supports\",\n    \"note\": \"POK_full.txt: 'Root / lemma: meug-2, meuk- | Meaning: to slide, slip | Note: also with aniaut. s- | Material: A. Latin mucus \\\"mucus\\\", mucor \\\"mildew\\\", e-mungo ... gr. muxa \\\"mucus, nose\\\" ... B. Old Indic *munakti, muncati, mucati \\\"releases, allows to loose\\\", mukti- \\\"lysis, dissolution ... release\\\"; Avestan fra-muxti- \\\"loosening\\\"; compare Old Indic munthate \\\"flees\\\", Old pers. amu(n)θa \\\"he fled\\\" ... References: WP. II 253 ff. ... Page(s): 744-745'. Nourai's whole chart is this one page of Pokorny; only the gloss 'describe' is absent.\"}\n ],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt line 760 s.v. meug-2\", \"stance\": \"supports\",\n    \"note\": \"'meug-2. Slimy, slippery; with derivatives referring to various wet or slimy substances and conditions. Enlarged form of meu-. ... 2. Possibly Germanic *(s)mug- ... d. Low German smukkelen, smuggeln, to smuggle ... 4. Variant form *meuk- in Latin mucus ... 5. Zero-grade variant form *muk- in: ... b. suffixed form *muk-so- in Greek muxa, mucus, lamp wick ...: MATCH2, MYXO-. [Pok. 2. meug- 744.]'\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. II pp. 253-254\", \"stance\": \"supports\",\n    \"note\": \"'meuq-, meug-' with section 'B. Ai. muncati \\\"loest, befreit, laesst los\\\" ..., mukti- \\\"Loesung, Befreiung, Aufgeben\\\" ... lit. munku, mukti \\\"entwischen\\\"'; a running head 'meuq-, meug-' on p. 254 confirms the WP reference Pokorny gives.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann s.vv. muk-, muktos, mukso (2)\", \"stance\": \"supports\",\n    \"note\": \"'muk- (muk-, munk-) \\\"leave\\\". WP II, 254: Skt. mucami, muncami, pp. muktah \\\"leave, release\\\"; ... Av. muc- \\\"let, release\\\"'; 'muktos \\\"left, freed, abandoned, loose\\\"'; 'mukso (2) (?) Gk. cf. muxa \\\"snot\\\"; Lat. muccare ... cf. also Gk. mukter \\\"nostril\\\"'.\"},\n   {\"src\": \"Wiktionary\", \"where\": \"Reconstruction:Proto-Indo-European/(s)mewk-\", \"stance\": \"partial\",\n    \"note\": \"Root glossed 'to let loose; to release; to slip away; to escape; to flee' - the 'release/flee' half of Nourai's gloss, with no 'wet/slimy' and no 'describe'.\"}\n ],\n \"nodes\": []\n}\n\ne2[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Avestan\", \"words\": \"fra-muxti; a-maux-ta\",\n \"verdict\": \"disputed\",\n \"derivation\": \"Young Avestan framuxti- is real but means something else. It occurs at Videvdad 6.27 in mat aoθranam framuxti .. upa.manayen 'with the taking off of their shoes they shall ..' (Bartholomae, AiW s.v. aoθra-, col. 40); Pokorny 744 glosses it 'loosening' (Losbinden), and Cheung, Etymological Dictionary of the Iranian Verb (2007) 138 f. files it under Proto-Iranian *(h)mauc 'to dress, clothe' with YAv. paiti-smuxta- 'shod', MP/Parthian fra-mowz- 'to take off (clothes)' and MP paymoz-/paymoxtan 'to don'. It does not mean 'open up, describe, clarify'; that gloss exists only to bridge to amuxtan 'to learn'. The second word, a-maux-ta, is not an attested Avestan form at all. It is the Old Iranian reconstruction that Nourai's own reference gives: Abolghasemi, Fe'lha-ye Farsi-ye Dari 27 (FFD_pages.txt, PDF p. 32) has 'amuxt < Middle Persian [hammoxt] < Old Iranian *a-mauk-ta; ... mauk is originally mauc, meaning \\\"to release\\\", c having been changed to x before t'. So the box mixes an attested Avestan noun with a starred Old Iranian participle and labels both Avestan. More seriously, modern Iranian etymology separates the 'learn' root from *meug- altogether: Cheung sets up *mauc(3) 'to learn, teach' (2007: 270), remarks 'The root is exclusively Iranian', gives 'PIE -- = LIV: -- | Pok.: --' (i.e. no Indo-European ancestry), and suggests it was abstracted from *ham-Hauc; Wiktionary follows him and takes it to PIE *h1ewk- 'to be accustomed' (cf. Sanskrit uc-, Old Armenian usanim, Lithuanian junkti, Russian ucit'). Language label, glosses and root are therefore all disputed.\",\n \"derivation_fa\": \"صورت اوستایی متأخرِ framuxti- واقعی است اما معنایش چیز دیگری است: در وندیداد ۶٫۲۷ در عبارت mat aoθranam framuxti «با از پا درآوردنِ کفش‌هایشان» آمده (بارتولمه، ذیل aoθra-)، پوکورنی (ص ۷۴۴) آن را «گشودن، از تن درآوردن» معنی می‌کند و چونگ در فرهنگ ریشه‌شناختی فعل ایرانی (۲۰۰۷، ص ۱۳۸ به بعد) آن را زیر ریشهٔ ایرانی آغازین *(h)mauč «پوشیدن، جامه کردن» می‌گذارد، در کنار paiti-smuxta- «کفش‌پوشیده» و فارسی میانهٔ paymōxtan «پوشیدن». پس معنی «گشودن، توصیف کردن، روشن کردن» از آن نیست و تنها برای پل زدن به «آموختن» ساخته شده. واژهٔ دوم، a-maux-ta، هیچ گواهی اوستایی ندارد؛ این صورتِ بازسازی‌شدهٔ ایرانی باستانِ *ā-mauk-ta است که خودِ منبعِ نورایی، ابوالقاسمی در «فعل‌های فارسی دری» ص ۲۷، آورده: «آموخت < فارسی میانهٔ hammōxt < ایرانی باستان *ā-mauk-ta … mauk در اصل mauč است به معنی رها کردن، č پیش از t به x بدل شده است». مهم‌تر آنکه ریشه‌شناسی امروزی، ریشهٔ «آموختن» را از *meug- جدا می‌کند: چونگ ریشهٔ *mauč۳ «آموختن، آموزاندن» را جداگانه می‌آورد و می‌گوید «این ریشه منحصراً ایرانی است» و برای آن هیچ نیای هندواروپایی نمی‌شناسد و احتمال می‌دهد از *ham-Hauč انتزاع شده باشد؛ ویکی‌واژه هم به پیروی از او آن را به *h₁ewk- «خو گرفتن» می‌رساند (قس سنسکریت uc-، ارمنی کهن usanim، لیتوانیایی jùnkti، روسی učitʹ). پس پژوهش امروزی این گره را رد می‌کند: هم برچسب زبانی، هم معناها و هم ریشه.\",\n \"sources\": [W+\"%D8%A2%D9%85%D9%88%D8%AE%D8%AA%D9%86\"],\n \"ref_check\": [\n   {\"ref\": \"POK:744\", \"status\": \"partial\",\n    \"note\": \"Pokorny does list 'Avestan fra-muxti- \\\"loosening\\\"' under meug-2, so the root attachment of that one word is his; but he glosses it 'loosening', not 'open up, describe, clarify', and he has nothing resembling a-maux-ta or a 'learn' sense.\"},\n   {\"ref\": \"FFD:27\", \"status\": \"partial\",\n    \"note\": \"FFD_pages.txt PDF p. 32 (printed p. 27), s.v. آموختن: «آموخت < فارسی میانه [hammōxt] + ایرانی باستان *[ā-mauk-ta] ... mauk در اصل mauč است به معنی «رها کردن»، č پیش از t به x بدل شده است» and «آموز < فارسی میانه [hammōz] < ایرانی باستان *[ā-mauč-a]». Abolghasemi does connect the verb to a root mauc 'to release' - which is Nourai's claim - but the form is Old Iranian and starred, not Avestan, and Abolghasemi gives no PIE root and no Avestan fra-muxti-.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW col. 40 s.v. aoθra- (BRT.txt line 2945)\", \"stance\": \"contradicts\",\n    \"note\": \"'j. aoθra- n. \\\"Schuhwerk, Schuhzeug\\\": ... mat aoθranam framuxti .. upa.manayen \\\"mit Ablegung ihres Schuhzeugs sollen sie ..\\\" V. 6. 27' - framuxti- = 'taking off (of footwear)'. Bartholomae has no Avestan a-maoxta- (his only comparable entry is 'j. arəm muxti P. 25: lies arəm-uxti', i.e. an emendation away from muc-).\"},\n   {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007: 138 f. s.v. *(h)mauc, and 270 s.v. *mauc(3)\", \"stance\": \"contradicts\",\n    \"note\": \"*(h)mauc 'to dress, clothe': '(+ *fra-) YAv. framaoc- \\\"to undress ?\\\", YAv. framuxti- \\\"the undressing\\\" (V 6.27)'; and separately *mauc(3) 'to learn, teach' with 'The root is exclusively Iranian ... mauc may have been abstracted from *ham-Hauc' and 'PIE -- = LIV: -- | Pok.: --'.\"},\n   {\"src\": \"FFD\", \"where\": \"Abolghasemi p. 27 (PDF p. 32-33)\", \"stance\": \"partial\",\n    \"note\": \"See ref_check: gives Old Iranian *a-mauk-ta with root mauc 'to release', but as a reconstruction, and with Manichaean MP hmwxtn/hmwz- rather than any Avestan form.\"}\n ]\n})\n\ne2[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Persian\", \"words\": \"âmŭxtan; âmŭzândan (+ آموز ، آموزش ، آموزگار ، آموزشگاه)\",\n \"verdict\": \"plausible\",\n \"derivation\": \"New Persian آموختن amuxtan / آموز- amuz- continues Middle Persian hammoxtan, hammoz- 'to teach; to learn' - MacKenzie, Concise Pahlavi Dictionary: 'hammoxtan, hammoz- [ALPWN-tn' < A 'lp; hmwhtn', hmwc- | M hmwxtn, N amoxtan, amoz-] teach; learn', with hammoxtar 'learner' and hammozgar 'teacher'; Nyberg II glossary has amoxtareh 'the act of instructing, instruction'; Manichaean MP hmwxtn / hmwc-, Parthian 'mwc- 'to teach', Sogdian mwck 'teacher'. The past stem goes back to Old Iranian *(ham-/a-)mauk-ta-, in which the root-final *c was dissimilated to x before the *-t- of the participle - the change Abolghasemi describes at FFD 27 and the same one seen in سوختن soxtan, ریختن rextan, دوختن duxtan - while the present stem keeps the *c as z (*mauca- > MP -moz- > NP amuz-). آموزاندن amuzandan is a New Persian double causative on amuz- with -an-idan, and آموز، آموزش، آموزگار، آموزشگاه are all regular NP derivatives, each of them a headword in Mo'in vol. I. So the step from the parent form to Persian, and the internal Persian morphology, are sound. Two caveats: the prefix in the attested Middle Persian form is ham-, not a- (whence Wiktionary's hammoxtan and Cheung's *ham-Hauc), and the ultimate attachment to PIE *meug- is rejected by Cheung and Wiktionary (see node 1) - hence plausible, not confirmed.\",\n \"derivation_fa\": \"«آموختن / آموز-» فارسی نو ادامهٔ فارسی میانهٔ hammōxtan، hammōz- «آموزاندن؛ آموختن» است؛ مکنزی در فرهنگ کوچک پهلوی می‌آورد: «hammōxtan, hammōz- ... | فارسی نو āmōxtan, āmōz-] teach; learn»، همراه با hammōxtār «آموزنده» و hammōzgār «آموزگار»؛ نیبرگ نیز در واژه‌نامهٔ خود āmōxtārēh «عملِ آموزاندن» را ثبت کرده است. صورت‌های فارسی میانهٔ مانوی hmwxtn و پهلوی اشکانی ʾmwc- «آموزاندن» و سغدی mwčk «آموزگار» نیز گواهند. ستاکِ گذشته از ایرانی باستان *(ham-/ā-)mauk-ta- می‌آید که در آن *č پایانیِ ریشه پیش از *-t- به x بدل شده — همان دگرگونی آوایی که ابوالقاسمی توصیف کرده و در «سوختن، ریختن، دوختن» هم دیده می‌شود — و ستاکِ حال *č را به صورت ز نگه داشته (*mauča- > -mōz- > آموز-). «آموزاندن» سببیِ دوگانهٔ فارسی نو بر پایهٔ «آموز-» با -اندن است و «آموز، آموزش، آموزگار، آموزشگاه» همه مشتق‌های به‌قاعدهٔ فارسی نو و هر یک سرواژه‌ای در جلد یکم فرهنگ معین‌اند. پس گامِ «صورتِ باستان ← فارسی» و صرفِ درون‌فارسی درست است. دو نکته: پیشوندِ صورتِ گواهی‌شدهٔ فارسی میانه ham- است نه ā-، و پیوندِ نهایی به ریشهٔ هندواروپایی *meug- را چونگ و ویکی‌واژه رد می‌کنند (گرهٔ ۱). پس این گره با احتیاط پذیرفتنی است.\",\n \"sources\": [W+\"%D8%A2%D9%85%D9%88%D8%AE%D8%AA%D9%86\"],\n \"ref_check\": [\n   {\"ref\": \"FFD:27\", \"status\": \"supports\",\n    \"note\": \"FFD_pages.txt PDF p. 32-33 (printed pp. 27-28), s.v. آموختن: «آموخت < فارسی میانه hammōxt + ایرانی باستان *ā-mauk-ta ... č پیش از t به x بدل شده است»، «آموز < فارسی میانه hammōz < ایرانی باستان *ā-mauč-a»، and the note that Manichaean MP has hmwxtn / hmwz-. Exactly the Persian half of Nourai's arrow.\"},\n   {\"ref\": \"MON:91\", \"status\": \"partial\",\n    \"note\": \"Mo'in, Farhang-e Farsi vol. I (MON_part1.txt lines 4794-4818) has the whole cluster as consecutive headwords - آموختن (فراگرفتن، یاد گرفتن، تعلم؛ یاد دادن، تعلیم)، آموزانیدن/آموزاندن، آموزش، آموزشگاه، آموزنده، آموزگار، آموزه - which matches Nourai's node and his 'extra' list word for word. The scanned text carries no etymological bracket for آموختن, so Mo'in supports the forms and senses but not the derivation.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD s.v. hammoxtan (PHD.txt line 392)\", \"stance\": \"supports\",\n    \"note\": \"'hammoxtan, hammoz- [ALPWN-tn' < A \\\"lp; hmwhtn', hmwc-, Ki hmwz- | M hmwxtn, N amoxtan, amoz-] teach; learn. -isn: teaching. hammoxtar \\\"learner\\\" ... hammozgar [N amozgar] teacher.'\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II glossary (NYB_vol2_glossary.txt lines 389, 403)\", \"stance\": \"supports\",\n    \"note\": \"'amoxtareh: the act of instructing, instruction 70.11, 1' - the Pahlavi abstract on the same stem.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007: 270 s.v. *mauc(3) 'to learn, teach'\", \"stance\": \"partial\",\n    \"note\": \"'(+ *a-) NP amoxtan/amoz-, Ham. amotan/amuz- \\\"to learn; teach\\\"' - confirms the Persian verb and its prefix, but 'The root is exclusively Iranian' and 'PIE -- ; Pok.: --' contradicts the chart's PIE parentage.\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur, ARY_pages.txt (grep آموخت / آموز)\", \"stance\": \"silent\",\n    \"note\": \"No headword for آموختن; the string occurs only inside other entries' glosses (e.g. line 6613 «چم این واژه در زبان پهلوی: آموختن»).\"}\n ]\n})\n\ne2[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Old Persian\", \"words\": \"a-mutha, a-muntha\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Old Persian amuθa 'he fled' is genuine: it is the 3sg imperfect of a verb written mauθ-/muθ- and occurs four times in Darius's Bisitun inscription (DB 2.2, 2.71, 3.41 f., 3.71) in the recurring formula 'X with a few horsemen fled; he went off to ...'. Kent, Old Persian, lexicon: 'mauθ- vb. \\\"flee\\\": meaning established by Elam. and Akk. versions (Husing, KZ 38.258); probably to Skt. munthate \\\"flees\\\" (Jn. JAOS 38.122). amuθa imf. (para. 211) DB 2.2, 71; 3.41 f., 71'; Tolman, Ancient Persian Lexicon: 'mud (Pres. muθa-), to flee. Pret. 3 sg. amuθa ... This interpretation (which is favored by both Elam. and Bab. versions) is undoubtedly correct and supersedes the former view of regarding amuθa as an adv.' Nourai's second form a-muntha is the nasal-infix shape Pokorny prints as 'Old pers. amu(n)θa ... from *mu-n-eth-mi', matching the Sanskrit nasal present mu-n-θ-; Kent explains it as the type Latin iungit, an ablauting infix -ne-/-n- levelled through the paradigm. Form and gloss are thus both right. What keeps this from 'confirmed' is the root attachment: it requires a dental *-θ- where the root has a guttural, and Walde-Pokorny II 254 rejects it outright - 'ist Bartholomaes KZ. 47, 292 Vergleich mit ap. amuθah \\\"er floh\\\", der auch Wechsel q:k ... voraussetzt, wohl nicht vorzuziehen' - even though Pokorny 744 later admitted it and Kent endorses the Sanskrit comparison.\",\n \"derivation_fa\": \"پارسی باستان amuθa «گریخت» صورتی گواهی‌شده است: ماضی نقلیِ (imperfect) سوم‌شخص مفردِ فعلی است که ستاکش mauθ-/muθ- نوشته می‌شود و چهار بار در سنگ‌نوشتهٔ بیستون داریوش (DB ۲٫۲، ۲٫۷۱، ۳٫۴۱ و ۳٫۷۱) در عبارتِ تکرارشوندهٔ «فلانی با چند سوار گریخت» آمده است. کنت در واژه‌نامهٔ پارسی باستان می‌نویسد: «mauθ- فعل «گریختن»: معنایش از روی روایت‌های عیلامی و اکدی مسلم شده ... احتمالاً هم‌ریشه با سنسکریت muṇṭhate «می‌گریزد»»، و تولمن نیز این خوانش را «بی‌گمان درست» می‌داند. صورت دومی که نورایی آورده (a-muntha) همان شکلِ میان‌وندِ خیشومی است که پوکورنی به صورت amu(n)θa < *mu-n-eth- می‌نویسد و با ستاکِ حالِ خیشومیِ سنسکریت mu-n-ṭh- می‌خواند. پس صورت و معنی هر دو درست است. آنچه این گره را به «با احتیاط پذیرفتنی» می‌کشاند پیوندِ ریشه است: این پیوند نیازمندِ یک دندانیِ θ در جایی است که ریشه واکِ نرم‌کامی دارد، و والده-پوکورنی (ج۲ ص۲۵۴) صریحاً مقایسهٔ بارتولمه را «ترجیح‌دادنی نمی‌داند»، هرچند پوکورنی در ۱۹۵۹ آن را پذیرفته و کنت هم مقایسهٔ سنسکریت را تأیید می‌کند.\",\n \"sources\": [W+\"Reconstruction:Proto-Indo-European/mewk-\"],\n \"ref_check\": [\n   {\"ref\": \"POK:744\", \"status\": \"supports\",\n    \"note\": \"POK_full.txt s.v. meug-2, section B: 'compare Old Indic munthate \\\"flees\\\", Old pers. amu(n)θa \\\"he fled\\\" from *mu-n-eth-m'r' - exactly Nourai's node, including the nasalised variant.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, lexicon s.v. mauθ- (KNT.txt line 5755) and para. 211 (line 2436)\", \"stance\": \"supports\",\n    \"note\": \"'mauθ- vb. \\\"flee\\\": meaning established by Elam. and Akk. versions ...; probably to Skt. munthate \\\"flees\\\" ... amuθa imf. DB 2.2, 71; 3.41 f., 71'; and 'This is the situation in the Aryan root *mauth-, Skt. pres. munthate \\\"he runs away\\\", OP imf. amuθa \\\"he fled\\\"'.\"},\n   {\"src\": \"TLM\", \"where\": \"Tolman, Ancient Persian Lexicon s.v. mud (TLM.txt line 1707)\", \"stance\": \"supports\",\n    \"note\": \"'mud (Pres. muθa-, Bartholomae, Grundr. 124), to flee. Pret. 3 sg. amuθa. Cf. Husing, KZ 38, 258. This interpretation (which is favored by both Elam. and Bab. versions) is undoubtedly correct'.\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 254\", \"stance\": \"contradicts\",\n    \"note\": \"'da die balt. Bed. \\\"entwischen\\\" aus \\\"entgleiten, wegschluepfen\\\" ohne Schwierigkeit zu gewinnen ist, ist Bartholomaes KZ. 47, 292 Vergleich mit ap. amuθah \\\"er floh\\\", der auch Wechsel q:k, bzw. fuers Balt. westidg. Guttural voraussetzt, wohl nicht vorzuziehen' - WP declines the very connection this arrow draws.\"},\n   {\"src\": \"BRT\", \"where\": \"BRT.txt (grep for muθ-/amuθa)\", \"stance\": \"silent\",\n    \"note\": \"Bartholomae's Altiranisches Woerterbuch has no Old Persian amuθa entry in the searchable text; his treatment is in KZ 47, 292, which WP II 254 cites and rejects.\"}\n ]\n})\n\ne2[\"nodes\"].append({\n \"id\": 4, \"lang\": \"Sanskrit\", \"words\": \"mŭkti; munthate\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Sanskrit mukti- f. is real and belongs to this root: Pokorny 744 'Old Indic ... mukti- \\\"lysis, dissolution, disintegration, release, abandonment\\\"'; Walde-Pokorny II 254 'mukti- \\\"Loesung, Befreiung, Aufgeben\\\"', beside the nasal present muncati 'releases, lets loose' (Mann s.v. muk- 'leave': 'Skt. mucami, muncami, pp. muktah \\\"leave, release\\\"; Av. muc- \\\"let, release\\\"'). But Nourai's gloss is not the gloss of mukti-: 'anything thrown away (worthless)' is Horn's rendering of the participle mukta- ('etwas Weggeworfenes'), and it is mukta-, not mukti-, that matters for the next arrow to Persian moft. The two are conflated here. The second word, Sanskrit munthate (muntha-, root muntha/muth), is likewise real but means 'flees, runs away' - so Kent ('probably to Skt. munthate \\\"flees\\\"'), so Pokorny ('compare Old Indic munthate \\\"flees\\\"'), so Jackson JAOS 38.122. Nourai's gloss 'untie, describe, explain' is given by no source; 'describe' again looks imported from the amuxtan branch. Root membership of both words is therefore confirmed, but half the glosses are wrong.\",\n \"derivation_fa\": \"سنسکریت mukti- (مؤنث) واژه‌ای واقعی و به‌درستی از همین ریشه است: پوکورنی (ص ۷۴۴) آن را «رهایی، گشودن، فروگذاشتن» و والده-پوکورنی (ج۲ ص۲۵۴) «Lösung, Befreiung, Aufgeben» معنی می‌کنند، در کنار ستاکِ حالِ خیشومیِ muñcáti «رها می‌کند». اما معنایی که نورایی داده معنای mukti- نیست: «هر چیزِ دورافکنده (بی‌ارزش)» برگردانِ هرن برای اسم مفعولِ muktá- است («چیزی که دور انداخته شده»)، و برای پیکانِ بعدی به «مفتِ» فارسی هم همان muktá- به کار می‌آید نه muktí-؛ این دو در اینجا با هم آمیخته شده‌اند. واژهٔ دوم، munthate (ریشهٔ muṇṭh)، نیز واقعی است ولی معنایش «می‌گریزد» است — چنین است در کنت، در پوکورنی و در مقالهٔ جکسون — و معنایی که نورایی داده («گشودن، توصیف کردن، توضیح دادن») در هیچ منبعی نیست و «توصیف کردن» بازهم از شاخهٔ «آموختن» به اینجا کشیده شده. پس تعلقِ هر دو واژه به ریشه درست است اما نیمی از معناها نادرست‌اند؛ گره با احتیاط پذیرفتنی است.\",\n \"sources\": [W+\"mukti\", W+\"Reconstruction:Proto-Indo-European/mewk-\"],\n \"ref_check\": [\n   {\"ref\": \"POK:744\", \"status\": \"partial\",\n    \"note\": \"POK_full.txt s.v. meug-2 B: 'Old Indic *munakti, muncati, mucati \\\"releases, allows to loose\\\", mukti- \\\"lysis, dissolution, disintegration, release, abandonment\\\"; ... compare Old Indic munthate \\\"flees\\\"'. Both words are on Nourai's page; Pokorny's glosses are 'release' and 'flees', not 'anything thrown away' and 'untie, describe, explain'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 254\", \"stance\": \"partial\",\n    \"note\": \"'B. Ai. muncati \\\"loest, befreit, laesst los\\\" (\\\"streift ab, laesst abgleiten\\\"), mukti- \\\"Loesung, Befreiung, Aufgeben\\\", prati-muncati \\\"zieht an, legt an (Kleidung)\\\"'.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann s.vv. muk-, muktos\", \"stance\": \"supports\",\n    \"note\": \"'muk- (muk-, munk-) \\\"leave\\\". WP II, 254: Skt. mucami, muncami, pp. muktah \\\"leave, release\\\"'; 'muktos \\\"left, freed, abandoned, loose, dashing, rapid\\\". Cf. muk-. WP II, 254: Skt. muktah, pp. \\\"freed, loose\\\"'.\"},\n   {\"src\": \"KNT\", \"where\": \"Kent s.v. mauθ-\", \"stance\": \"contradicts\",\n    \"note\": \"'probably to Skt. munthate \\\"flees\\\" (Jn. JAOS 38.122)' - munthate = 'flees', not 'untie, describe, explain'.\"},\n   {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/mukti\", \"stance\": \"partial\",\n    \"note\": \"'Borrowed from Sanskrit मुक्ति (mukti) ... Feminine synonym of masculine substantive noun मोक्ष (moksa, \\\"liberation\\\")' - mukti- is the abstract 'liberation', not 'a worthless thing'.\"}\n ]\n})\n\ne2[\"nodes\"].append({\n \"id\": 5, \"lang\": \"Persian\", \"words\": \"moft\",\n \"verdict\": \"plausible\",\n \"derivation\": \"New Persian مفت moft (classical muft) 'free, gratis, worthless' goes back to *mukta- 'released, let go, thrown away'; the Old Iranian cluster -kt- becomes -ft- regularly in Persian, the change Horn illustrates with the exact parallel جفت juft < yukta-. Horn no. 987, p. 221: 'muft \\\"unbedeutend, umsonst erhalten\\\" - ai. sqrt-muc- \\\"befreien, wegwerfen\\\" (also mukta- \\\"etwas Weggeworfenes\\\", wie np. juft aus yukta-), Darmesteter, Et. ir. I, 88 Note 2', and he adds that the Slavic loans (Slovene muhte, Serbian mukte 'gratis') would then have re-developed the original shape - closing, however, with 'Unsicher'. Wiktionary makes the word an inheritance rather than a loan: 'Ultimately from Proto-Indo-Iranian *muktas ..., from Proto-Indo-European *muk-to-s (\\\"released, discharged\\\"), from *(s)mewk- (\\\"to free, escape\\\")', with Sanskrit मुक्त mukta as a cognate. That is the substantive correction to the chart: Nourai draws Sanskrit > Persian, but moft is not a borrowing from Sanskrit - it is the Iranian reflex of the same *muk-to-, so the line should be a cognate line, and the Sanskrit form to compare is mukta-, not mukti-. Nourai's gloss is right, and the Persian word is itself the source of Ottoman/Turkish muft, Hindi-Urdu muft, Serbo-Croatian mukte, Bulgarian mufta and Romanian moft.\",\n \"derivation_fa\": \"«مفت» فارسی نو (در فارسی کلاسیک muft) «رایگان، بی‌ارزش» از *mukta- «رهاشده، دورافکنده» می‌آید؛ خوشهٔ -kt- ایرانی باستان در فارسی به‌قاعده به -ft- بدل می‌شود، همان دگرگونی که هرن با نمونهٔ دقیقِ «جفت» < yuktá- نشان می‌دهد. هرن در بند ۹۸۷ صفحهٔ ۲۲۱ می‌نویسد: «muft «ناچیز، به‌رایگان به‌دست‌آمده» — سنسکریت ریشهٔ muc- «رهانیدن، دور انداختن» (و mukta- «چیزی که دور انداخته شده»، مانند «جفت» فارسی از yuktá-)»، و می‌افزاید که وام‌واژه‌های اسلاوی (اسلوونیایی muhte، صربی mukte «رایگان») سپس صورت اصلی را بازساخته‌اند؛ اما مقاله را با کلمهٔ «نامسلّم» (Unsicher) می‌بندد. ویکی‌واژه این واژه را وام‌گرفته نمی‌داند بلکه ارثی می‌شمارد: «سرانجام از هندوایرانی آغازین *muktás، از هندواروپایی آغازین *muk-tó-s «رهاشده»، از ریشهٔ *(s)mewk-»، و سنسکریت muktá- را هم‌ریشه (نه سرچشمه) می‌گیرد. همین نکتهٔ اصلاحیِ نمودار است: پیکانِ «سنسکریت ← فارسی» باید خطِ هم‌ریشگی باشد، نه وام‌گیری، و صورت سنسکریتِ درخور مقایسه muktá- است نه muktí-. معنایی که نورایی داده درست است و خودِ «مفت» فارسی سرچشمهٔ müft ترکی، muft هندی و اردو، mukte صربی و moft رومانیایی است.\",\n \"sources\": [W+\"%D9%85%D9%81%D8%AA\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:2024\", \"status\": \"not_found\",\n    \"note\": \"Borhan-e Qate' vol. 4, PDF p. 107 = printed p. 2024 (offset +1917, confirmed by the running heads -1979-/1980/-1981- at PDF pp. 62/63/64). That page carries the end of بیان نوزدهم «در میم با فا مشتمل بر چهار لغت و کنایت» (only four م+ف entries: مفرج گران، مفلاك، مفلحان ...) and the start of بیان بیستم «در میم با قاف». There is no مفت headword there or anywhere else in BQT_v4_pages.txt (grep مفت returns only مفتوح/مفتون/مفتش etc. inside other entries), so Borhan - and with it Mo'in's footnote apparatus - has nothing on this word.\"},\n   {\"ref\": \"HRN:221\", \"status\": \"supports\",\n    \"note\": \"HRN.txt leaf 242 (printed p. 221) no. 987: 'muft \\\"unbedeutend, umsonst erhalten\\\". ai. sqrt-muc- \\\"befreien, wegwerfen\\\" (also mukta- \\\"etwas Weggeworfenes\\\", wie np. juft aus yukta-), Darmesteter, Et. ir. I, 88 Note 2. Die entlehnten nslov. muhte \\\"sorglos\\\", serb. mukte, muktice \\\"umsonst\\\" ... Unsicher.' Supports the root and gives the sound law, but with the form mukta- and with an explicit caveat.\"}\n ],\n \"consulted\": [\n   {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/مفت, Persian section\", \"stance\": \"partial\",\n    \"note\": \"'Ultimately from Proto-Indo-Iranian *muktas (whence also زمخت zumuxt), from Proto-Indo-European *muk-to-s (\\\"released, discharged\\\"), from *(s)mewk- (\\\"to free, escape\\\"). Compare Sanskrit मुक्त (mukta)' - same root, but inherited, not borrowed from Sanskrit (the page is categorised 'Persian terms inherited from Proto-Indo-European').\"},\n   {\"src\": \"MON\", \"where\": \"MON_part1/part2 (grep مفت)\", \"stance\": \"silent\",\n    \"note\": \"Mo'in has the word only in compounds and glosses (e.g. مفت‌خور; مجانی defined as «مفت، رایگان»); no headword entry with an origin bracket is visible in the scanned text.\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur, ARY_pages.txt (grep مفت)\", \"stance\": \"silent\",\n    \"note\": \"No entry for مفت (the only hit is مفتخر inside another article).\"},\n   {\"src\": \"IEC\", \"where\": \"Mann s.v. muktos\", \"stance\": \"supports\",\n    \"note\": \"'muktos \\\"left, freed, abandoned, loose ...\\\": Skt. muktah, pp. \\\"freed, loose\\\"; ... Li. muktas, pp. of munku, mukti \\\"slip, fall, dash, run\\\"' - the *muk-to- participle from which moft descends.\"}\n ]\n})\n\ne2[\"nodes\"].append({\n \"id\": 6, \"lang\": \"Germanic\", \"words\": \"smug\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"'Germanic smug' is Watkins's *(s)mug-, and Nourai's gloss reproduces Watkins's wording verbatim: AHD s.v. meug-2 '2. Possibly Germanic *(s)mug-, referring to wetness and also to figurative slipperiness: a. Old English smoc, shirt: SMOCK; ... d. Low German smukkelen, smuggeln, to smuggle (< \\\"to slip contraband through\\\"); e. Middle Low German smucken, to adorn (< \\\"to make sleek\\\"): SMUG'. The initial s- is Pokorny's optional s-mobile: he sets the Germanic family on '(s)meugh-', whence Old Norse smjuga 'to creep into or crawl through', Old English smugan 'to slip, slide, creep', MHG smiegen (German schmiegen) 'to crouch, nestle'. Ernout-Meillet cite the same 'v. angl. smugan \\\"glisser\\\"' under Latin mucus. As elsewhere on this page the form should carry an asterisk (*smug-/*(s)mug-), since it is a reconstruction, not an attested Germanic word.\",\n \"derivation_fa\": \"آنچه نورایی «ژرمنی smug» می‌نویسد همان *(s)mug- واتکینز است و معنایی که برایش آورده واژه‌به‌واژه از واتکینز است: «شاید ژرمنی *(s)mug-، اشاره به خیسی و همچنین به لیزیِ استعاری: انگلیسی کهن smoc «پیراهن» > smock؛ ... آلمانی سفلی smukkelen, smuggeln «قاچاق کردن» (< «رد کردنِ کالا از راهِ لیز») > smuggle؛ آلمانی سفلای میانه smucken «آراستن» > smug». واکِ s آغازین همان s متحرک (s-mobile) است؛ پوکورنی خانوادهٔ ژرمنی را زیر گونهٔ *(s)meugh- می‌گذارد که نورس کهن smjúga «خزیدن در»، انگلیسی کهن smūgan «لیز خوردن، خزیدن» و آلمانی میانهٔ علیا smiegen (آلمانی schmiegen) از آن است. ارنو-میه هم زیر mūcus لاتینی همین «انگلیسی کهن smugan لیز خوردن» را می‌آورد. ادعای نورایی درست است؛ تنها باید صورت را ستاره‌دار نوشت چون بازسازی است.\",\n \"sources\": [E+\"smuggle\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"AHD_watkins1985.txt line 760 s.v. meug-2: '2. Possibly Germanic *(s)mug-, referring to wetness and also to figurative slipperiness: ... d. Low German smukkelen, smuggeln, to smuggle (< \\\"to slip contraband through\\\"): SMUGGLE' - Nourai's gloss 'wetness, figurative slipperiness' is a direct quotation.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW 744 f. s.v. meug-2 ('Auf (s)meugh- based on the Germanic family')\", \"stance\": \"supports\",\n    \"note\": \"'Old Icelandic smjuga \\\"creep into or crawl through\\\", Old English smugan \\\"slip, slide; stumble, grovel, truckle, creep\\\", Middle High German smiegen \\\"crouch\\\", Modern High German schmiegen ... with s- Danish Norwegian i smug ... ndd. smuggeln, Modern High German (out of it) schmuggeln'.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. smuggle / smock\", \"stance\": \"supports\",\n    \"note\": \"'smuggle ... rel. to Dan. smugle, Norw. smugla, Swed. smuggla, Norw. smokla, Du. smokkelen, \\\"to smuggle\\\", and to OE. smugan, \\\"to creep\\\". See smock'.\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. mucus\", \"stance\": \"supports\",\n    \"note\": \"'Cf. gr. muxa \\\"morve, mucosite\\\", apo-mussoo \\\"je me mouche\\\", peut-etre lit. smunku, smukti \\\"tomber en glissant\\\", v. angl. smugan \\\"glisser\\\" ... Le sens premier est \\\"etre gluant, visqueux\\\"'.\"}\n ]\n})\n\ne2[\"nodes\"].append({\n \"id\": 7, \"lang\": \"English\", \"words\": \"smuggle\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"smuggle is not an English inheritance but a late-17th-century loan from across the North Sea: Etymonline dates smuggler to the 1660s and smuggle to the 1680s, 'from Low German smuggeln or Dutch smokkelen \\\"to transport (goods) illegally\\\", apparently a frequentative formation of a word meaning \\\"to sneak\\\" (from Proto-Germanic *smuganan ...), perhaps literally \\\"to slip (contraband through)\\\"'; Klein has the same, listing Danish smugle, Norwegian smugla, Swedish smuggla, Dutch smokkelen and tying them to Old English smugan 'to creep'. The word entered with the customs vocabulary of the Dutch and North German carrying trade, and the sense development is 'slip, creep' > 'slip goods past the customs'. The arrow Germanic > English is therefore right, with Low German as the actual donor.\",\n \"derivation_fa\": \"smuggle واژه‌ای ارثی در انگلیسی نیست، بلکه وام‌واژه‌ای از سدهٔ هفدهم از آن سویِ دریای شمال است: اتیمانلاین smuggler را به دههٔ ۱۶۶۰ و smuggle را به دههٔ ۱۶۸۰ می‌برد، «از آلمانی سفلی smuggeln یا هلندی smokkelen «حمل غیرقانونی کالا»، که ظاهراً صورتی تکراری از فعلی به معنی «دزدانه رفتن» است (از ژرمنی آغازین *smuganan)، و شاید تحت‌اللفظ یعنی «لیز دادنِ کالای قاچاق»». کلاین نیز همین را می‌آورد و دانمارکی smugle، نروژی smugla، سوئدی smuggla و هلندی smokkelen را برمی‌شمارد و همه را به انگلیسی کهن smūgan «خزیدن» می‌بندد. این واژه با واژگانِ گمرکیِ بازرگانیِ دریاییِ هلندی و آلمانیِ شمالی وارد انگلیسی شد و تحول معنایی آن «لیز خوردن، خزیدن» ← «رد کردنِ کالا از گمرک» است. ادعای نورایی درست است.\",\n \"sources\": [E+\"smuggle\"],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"no reference on the node; the parent's 'AHD' covers it ('Low German smukkelen, smuggeln, to smuggle ...: SMUGGLE').\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. smuggle (KLN_1966.txt line 35692)\", \"stance\": \"supports\",\n    \"note\": \"'smuggle, tr. and intr. v. - LG. smuggeln, rel. to Dan. smugle, Norw. smugla, Swed. smuggla, Norw. smokla, Du. smokkelen, \\\"to smuggle\\\", and to OE. smugan, \\\"to creep\\\".'\"},\n   {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/smuggle (with smuggler on the same page)\", \"stance\": \"supports\",\n    \"note\": \"'1680s, of Low German or Dutch origin'; 'smuggler ... 1660s, from Low German smuggeln or Dutch smokkelen ... perhaps literally \\\"to slip (contraband through)\\\", from Proto-Germanic *(s)muk-'.\"},\n   {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt line 2271 index: 'SMUGGLE meug-2'\", \"stance\": \"supports\",\n    \"note\": \"The word index of the Watkins appendix assigns SMUGGLE (and SMUG, SMOCK) to meug-2, i.e. Nourai's Meug.\"}\n ]\n})\n\ne2[\"nodes\"].append({\n \"id\": 8, \"lang\": \"Greek\", \"words\": \"muxa\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Greek myxa (muxa) 'mucus, slime' is a real and well attested word; its transferred sense is 'the nozzle of a lamp' and hence 'lamp wick', the wick being seen as hanging out of the spout the way snot hangs from a nostril. Skeat s.v. match (2): 'Low L. myxus, the nozzle of a lamp, through which the wick [passes]; also, a wick. - Gk. myxa, the nozzle of a lamp; the more original senses [are] mucus, nostril. Allied to Mucus'; Watkins derives it from the suffixed zero grade *muk-so- ('suffixed form *muk-so- in Greek muxa, mucus, lamp wick (< \\\"nozzle of a lamp\\\" < \\\"nostril\\\")'); Pokorny 744 sets it beside myktér 'nose, nostril' and apomyssomai 'blow one's nose', and Ernout-Meillet cite it as the Greek match for Latin mucus. So Nourai's gloss 'lamp wick' is the derived, not the basic, sense, but the word and its membership of the root are correct. He gives no reference for the node; the claim is Watkins's.\",\n \"derivation_fa\": \"یونانی μύξα (múxa) «مخاط، آبِ بینی، لزج» واژه‌ای واقعی و پرگواه است؛ معنای مجازی آن «لولهٔ چراغ» و از آنجا «فتیلهٔ چراغ» است، چون فتیله را چنان می‌دیدند که از دهانهٔ چراغ بیرون آویخته، همان‌گونه که آبِ بینی از سوراخِ بینی. اسکیت ذیل match (2) می‌نویسد: «لاتینی سفلی myxus، دهانهٔ چراغ که فتیله از آن می‌گذرد؛ و نیز خودِ فتیله. — از یونانی μύξα، دهانهٔ چراغ؛ معناهای اصلی‌ترِ آن «مخاط» و «سوراخ بینی» است. هم‌ریشه با mucus». واتکینز آن را از درجهٔ صفرِ پسونددارِ *muk-so- می‌گیرد و پوکورنی (ص ۷۴۴) آن را در کنار μυκτήρ «بینی» و ἀπομύσσομαι «بینی گرفتن» می‌نشاند؛ ارنو-میه نیز آن را برابرِ یونانیِ mūcus لاتینی می‌آورد. پس معنایی که نورایی داده («فتیلهٔ چراغ») معنای ثانوی است، اما واژه و تعلقش به ریشه درست است. ادعای نورایی درست است.\",\n \"sources\": [E+\"mucus\", E+\"match\"],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai cites nothing on this node; the source is clearly AHD, which he cites on the neighbouring boxes - AHD_watkins1985.txt s.v. meug-2 '5b. suffixed form *muk-so- in Greek muxa, mucus, lamp wick (< \\\"nozzle of a lamp\\\" < \\\"nostril\\\"): MATCH2, MYXO-'.\"}],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW 744 s.v. meug-2 A\", \"stance\": \"supports\",\n    \"note\": \"'gr. muxa \\\"mucus, nose\\\" (based on *muk-s-os \\\"slimy\\\", as also:) muxos, muxinos, muxon \\\"mullet\\\" ... gr. apo-myssomai \\\"blowing one's nose\\\" ... mykter \\\"nose, nostril\\\"'.\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. Match (2) (SKT.txt line 11216)\", \"stance\": \"supports\",\n    \"note\": \"'Low L. myxus, the ... nozzle of lamp, through which the wick ... also, a wick. - Gk. myxa, the n[ozzle of a] lamp; the more original senses ... mucus, ... nostril. Allied to Mucus'.\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. mucus\", \"stance\": \"supports\",\n    \"note\": \"'Cf. gr. muxa \\\"morve, mucosite\\\", apo-mussoo \\\"je me mouche\\\"' - and, on the Latin side, 'les l. romanes attestent aussi le sens de \\\"champignon de la meche d'une lampe\\\"', the very sense shift Nourai's node presupposes.\"}\n ]\n})\n\ne2[\"nodes\"].append({\n \"id\": 9, \"lang\": \"English\", \"words\": \"match 1\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"The chain is Greek myxa 'lamp nozzle, wick' > Late/Low Latin myxus 'wick' > Vulgar Latin *micca/*miccia (whence Catalan metxa, Spanish mecha, Italian miccia) > Old French meiche/mesche (Mod.Fr. meche) > Middle English macche 'wick of a candle or lamp' (late 14c.), spelled match from mid-15c.; the sense 'cord or tow soaked in sulfur for lighting fires' is 1530, and only about 1830 does the word come to mean the sulfur-tipped wooden friction match that Nourai glosses (Etymonline s.v. match (n.1); Skeat s.v. match (2), quoting Cotgrave's 'wick of candle, match to fire a gun'). So the arrow Greek > English is right in substance but passes through Latin and French, and the gloss 'a piece of wood that catches fire by friction' describes the 19th-century object rather than the word's origin. Nourai's numbering 'match 1' agrees with Etymonline (match n.1); Watkins numbers the same word MATCH2, the homograph 'an equal, a contest' (from PIE *mag-) being the other one.\",\n \"derivation_fa\": \"زنجیره چنین است: یونانی μύξα «دهانهٔ چراغ، فتیله» ← لاتینی متأخر/سفلی myxus «فتیله» ← لاتینی عامیانه *micca/*miccia (که کاتالانی metxa، اسپانیایی mecha و ایتالیایی miccia از آن است) ← فرانسوی کهن meiche/mesche (امروز mèche) ← انگلیسی میانه macche «فتیلهٔ شمع یا چراغ» (اواخر سدهٔ ۱۴)، که از میانهٔ سدهٔ ۱۵ match نوشته شد؛ معنی «ریسمانِ گوگردآلود برای افروختن» به سال ۱۵۳۰ می‌رسد و تنها از حدود ۱۸۳۰ به «کبریتِ چوبیِ سرگوگردی» — همان که نورایی معنی کرده — گفته شد (اتیمانلاین ذیل match؛ اسکیت ذیل match 2). پس پیکانِ «یونانی ← انگلیسی» در جوهر درست است اما از لاتین و فرانسوی گذشته، و معنایی که در جعبه آمده شیءِ سدهٔ نوزدهمی را وصف می‌کند نه خاستگاه واژه را. شمارهٔ «match 1» نورایی با اتیمانلاین می‌خواند (واتکینز همین واژه را MATCH2 می‌شمارد). ادعای نورایی درست است.\",\n \"sources\": [E+\"match\"],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"no reference on the node; the source is AHD s.v. meug-2 ('Greek muxa, mucus, lamp wick ...: MATCH2') and the index line 'MATCH2 meug-2' in AHD_watkins1985.txt line 1829.\"}],\n \"consulted\": [\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. Match (2)\", \"stance\": \"supports\",\n    \"note\": \"'Match (2), a prepared rope for firing cannon. (F.-L.-Gk.) M.E. macche. O.F. mesche, meiche (F. meche), wick of candle, match to fire a gun ... - Gk. myxa, the nozzle of a lamp ... Allied to Mucus'.\"},\n   {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/match, match (n.1)\", \"stance\": \"supports\",\n    \"note\": \"'Late 14c., macche, \\\"wick of a candle or lamp\\\" ... from Old French meiche ... from Vulgar Latin *micca/*miccia ... probably ultimately from Latin myxa, from Greek myxa \\\"lamp wick\\\", originally \\\"mucus\\\" ... from PIE root *meug- \\\"slimy, slippery\\\"'; and 'It was used by 1830 for the modern type of sulfur-tipped wooden friction match'.\"},\n   {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt s.v. meug-2 and index line 1829\", \"stance\": \"supports\",\n    \"note\": \"'MATCH2 meug-2' in the word index; the root entry supplies the Greek link.\"}\n ]\n})\n\ne2[\"nodes\"].append({\n \"id\": 10, \"lang\": \"Latin\", \"words\": \"mucŭs\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Latin mucus, -i m. 'snot, nasal mucus' is real and central to this root, with the derivatives mucere 'to be mouldy', mucor 'mould', mucidus 'mouldy, snotty' and the nasal-infixed e-mungere 'to blow the nose, (fig.) to swindle'. Ernout-Meillet s.v. mucus: 'morve, mucus nasal (les l. romanes attestent aussi le sens de \\\"champignon de la meche d'une lampe\\\", cf. le fr. \\\"moucher la chandelle\\\") ... Cf. gr. muxa \\\"morve, mucosite\\\", apo-mussoo \\\"je me mouche\\\", peut-etre lit. smunku, smukti \\\"tomber en glissant\\\", v. angl. smugan \\\"glisser\\\" ... comme aussi skr. muncati \\\"il delivre\\\". Une autre forme de la racine, avec infixe nasal et gutturale sonore, apparait dans mungo. Le sens premier est \\\"etre gluant, visqueux\\\"' - i.e. exactly the root and the semantic core Nourai assumes. Watkins: 'Variant form *meuk- in Latin mucus, mucus: MOIST, MUCILAGE, MUCO-, MUCUS, (MUSTY)'. Nourai's gloss 'moist' is a loose rendering of 'slimy, viscous'; form, language and derivation are otherwise correct. He gives no reference here.\",\n \"derivation_fa\": \"لاتینی mūcus «مخاط بینی» واژه‌ای واقعی و در کانونِ این ریشه است، با مشتق‌هایی مانند mūcēre «کپک زدن»، mūcor «کپک»، mūcidus «کپکی، مخاطی» و صورتِ میان‌وندِ خیشومیِ ē-mungere «بینی گرفتن، (مجازاً) فریب دادن». ارنو-میه ذیل mūcus می‌نویسد: «مخاط بینی (زبان‌های رومانس معنی «قارچِ فتیلهٔ چراغ» را هم گواهی می‌دهند، قس فرانسوی moucher la chandelle) ... قس یونانی μύξα، ἀπομύσσω «بینی می‌گیرم»، شاید لیتوانیایی smunkù «لیزخوران افتادن»، انگلیسی کهن smūgan «لیز خوردن» ... و همچنین سنسکریت muñcáti «رها می‌کند». گونهٔ دیگری از ریشه با میان‌وندِ خیشومی و واکِ نرم‌کامیِ واک‌دار در mungō دیده می‌شود. معنای نخستین «لزج و چسبناک بودن» است» — یعنی درست همان ریشه و همان هستهٔ معنایی که نورایی فرض گرفته. واتکینز نیز «گونهٔ *meuk- در لاتینی mūcus» را با بازمانده‌های MOIST و MUCUS می‌آورد. معنی «نمناک» که نورایی داده برگردانی آزاد از «لزج» است؛ در بقیهٔ موارد گره درست است.\",\n \"sources\": [E+\"mucus\"],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"no reference on the node; AHD s.v. meug-2 '4. Variant form *meuk- in Latin mucus, mucus: MOIST, MUCILAGE, MUCO-, MUCUS, (MUSTY)' is the source, and Pokorny 744 heads section A with 'Latin mucus \\\"mucus\\\", mucor \\\"mildew\\\", e-mungo, -ere'.\"}],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW 744 s.v. meug-2 A\", \"stance\": \"supports\",\n    \"note\": \"'A. Latin mucus \\\"mucus\\\", mucor \\\"mildew\\\", e-mungo, -ere \\\"to wipe the nose, blow the nose, to cheat, swindle\\\"; mugil m. \\\"mullet\\\"'.\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. muc-/mucc- and mucus (LAT.txt lines 39288-39310)\", \"stance\": \"supports\",\n    \"note\": \"'mucus, -i m.: morve, mucus nasal ... Cf. gr. muxa \\\"morve\\\" ... comme aussi skr. muncati \\\"il delivre\\\". Une autre forme de la racine, avec infixe nasal et gutturale sonore, apparait dans mungo. Le sens premier est \\\"etre gluant, visqueux\\\".'\"},\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. mucus (KLN_1966.txt line 24569)\", \"stance\": \"supports\",\n    \"note\": \"'L. mucus, \\\"mucus of the nose\\\", rel. to mucor, \\\"mold, moldiness\\\", mungere, emungere, \\\"to blow the nose\\\", fr. I.-E. base *(s)meuq-, *(s)meug-, \\\"to slip; slippery, slime\\\", whence also OI. muncati, \\\"he releases\\\", Gk. muxa, \\\"mucus of the nose, slime\\\"'.\"}\n ]\n})\n\ne2[\"nodes\"].append({\n \"id\": 11, \"lang\": \"English\", \"words\": \"moist; mucus\",\n \"verdict\": \"plausible\",\n \"derivation\": \"mucus was borrowed straight from Latin mucus in the 1660s as a medical term, replacing Middle English mucilage (Etymonline s.v. mucus; Klein s.v. mucus), so that half of the node is exact. moist is the weak half. Middle English moiste (late 14c., 'slightly wet') comes from Old French moiste, and the Latin base behind the French word is disputed: Klein s.v. moist derives it from Vulgar Latin *muscidus, 'which is a blend of L. mucidus, \\\"moldy, musty\\\", and musteus, \\\"of new wine, fresh, juicy\\\". L. mucidus is a derivative of mucus'; Etymonline calls Old French moiste 'of uncertain origin', gives *muscidus < mucidus (from mucus) as the likelier source and Diez's alternative Latin musteus 'fresh, green, new' (from mustum - i.e. from the Meu 1 chart on the same page) as a possibility, adding that 'If this wasn't the source, it influenced the form of the other word in Old French'. So moist reaches Latin mucus only through a blended Vulgar Latin adjective, and part of its form may belong to the other root on this page; hence plausible for the node.\",\n \"derivation_fa\": \"«mucus» انگلیسی در دههٔ ۱۶۶۰ یکسر از لاتینی mūcus به‌عنوان اصطلاح پزشکی وام گرفته شد و جای mucilage انگلیسی میانه را گرفت (اتیمانلاین و کلاین)، پس این نیمهٔ گره دقیق است. نیمهٔ سست، «moist» است: انگلیسی میانه moiste (اواخر سدهٔ ۱۴، «کمی خیس») از فرانسوی کهن moiste می‌آید و پایهٔ لاتینیِ واژهٔ فرانسوی محل اختلاف است. کلاین آن را از لاتینی عامیانهٔ *muscidus می‌گیرد که «آمیزه‌ای از mūcidus «کپکی» و musteus «مربوط به شرابِ نو، تازه» است، و mūcidus خود مشتقِ mūcus است»؛ اتیمانلاین moiste را «با خاستگاه نامعلوم» می‌خواند، *muscidus (از mūcidus و آن از mūcus) را احتمالِ قوی‌تر می‌داند و گزینهٔ دیگر، یعنی musteus لاتینی از mustum (یعنی از نمودار Meu 1 در همین صفحه) را که دیتس پیشنهاد کرده نیز ممکن می‌شمارد و می‌افزاید که «اگر سرچشمه نبوده باشد، بر صورتِ آن واژهٔ دیگر در فرانسوی کهن اثر گذاشته است». پس moist تنها از راهِ یک صفتِ آمیختهٔ لاتینِ عامیانه به mūcus می‌رسد و بخشی از صورتش شاید به ریشهٔ دیگرِ همین صفحه بازگردد؛ از این‌رو گره با احتیاط پذیرفتنی است.\",\n \"sources\": [E+\"moist\", E+\"mucus\"],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"no reference on the node; AHD s.v. meug-2 '4. Variant form *meuk- in Latin mucus: MOIST, MUCILAGE, MUCO-, MUCUS, (MUSTY)' and the index lines 'MOIST meug-2', 'MUCUS meug-2' are the source.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.vv. moist and mucus (KLN_1966.txt lines 24172, 24569)\", \"stance\": \"partial\",\n    \"note\": \"'moist, adj. - ME. moiste ... fr. MF. moiste (F. moite), \\\"moist\\\", fr. VL. *muscidus, which is a blend of L. mucidus, \\\"moldy, musty\\\", and musteus, \\\"of new wine, fresh, juicy\\\". L. mucidus is a derivative of mucus' - so moist is at best half from mucus.\"},\n   {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/moist\", \"stance\": \"partial\",\n    \"note\": \"'from Old French moiste \\\"damp, wet, soaked\\\" (13c. ...), which is of uncertain origin. Perhaps from Vulgar Latin *muscidus \\\"moldy\\\", also \\\"wet\\\", from Latin mucidus \\\"slimy, moldy, musty\\\", from mucus \\\"slime\\\" ... Alternative etymology [Diez] is from Latin musteus \\\"fresh, green, new\\\" ...'\"},\n   {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt index lines 1880, 1895\", \"stance\": \"supports\",\n    \"note\": \"'MOIST meug-2' and 'MUCUS meug-2' - Watkins puts both English words under this root, as the chart does.\"}\n ]\n})\n\ndata[\"entries\"].append(e2)\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-338.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(data, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/mk338.py",
 "description": "Write page-338.json"
}
```


### [2026-09-07T17:58:54.144Z] TOOL RESULT

```
written
```


## [2026-09-07T17:58:58.370Z] TOOL CALL #76: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-338.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 338",
 "description": "Validate JSON and run verify_check"
}
```


### [2026-09-07T17:58:59.735Z] TOOL RESULT

```
JSON OK
nodes verified: 18/18
node verdicts: {'confirmed': 11, 'transcription_suspect': 1, 'disputed': 1, 'plausible': 5}
root verdicts: {'confirmed': 1, 'plausible': 1}
ref checks: {'supports': 8, 'not_found': 3, 'not_checked': 8, 'partial': 4}
books consulted: {'partial': 10, 'supports': 38, 'contradicts': 7, 'silent': 4} | by book: {'KLN': 10, 'IEC': 7, 'POK': 6, 'Etymonline': 6, 'AHD': 5, 'LAT': 4, 'BRT': 3, 'WLD': 3, 'CHEUNG': 2, 'ARY': 2, 'KNT': 2, 'Wiktionary': 2, 'SKT': 2, 'FFD': 1, 'PHD': 1, 'NYB': 1, 'TLM': 1, 'MON': 1}
```


## [2026-09-07T17:59:05.816Z] TOOL CALL #77: Bash

```json
{
 "command": "head -c 3 data/verification/page-338.json | xxd | head -1; ls -la data/verification/sources/refs/ocr/BOOK/338.png; python3 -c \"\nimport json;d=json.load(open('data/verification/page-338.json'))\nn=d['entries'][0]['nodes'][5]\nprint(n['id'],n['verdict'],n['error_in'],n['book_prints'],'->',n['correct_form'])\nprint(d['entries'][1]['nodes'][0]['derivation_fa'][:120])\n\"",
 "description": "Final sanity checks"
}
```


### [2026-09-07T17:59:07.107Z] TOOL RESULT

```
00000000: 7b0a 20                                  {. 
-rw-rw-r-- 1 sfmqrb sfmqrb 65267 Sep  7 13:37 data/verification/sources/refs/ocr/BOOK/338.png
6 transcription_suspect book Middle Greek -> Middle Low German
صورت اوستایی متأخرِ framuxti- واقعی است اما معنایش چیز دیگری است: در وندیداد ۶٫۲۷ در عبارت mat aoθranam framuxti «با از
```


## [2026-09-07T17:59:26.003Z] AGENT

Done. `data/verification/page-338.json` written; `verify_check.py 338` reports 18/18 nodes, 0 PROBLEM lines.

**Page 338 (book p. 308) — 2 charts (Meu 2 is a redirect, skipped)**

Verdicts: roots 1 confirmed (Meu 1) + 1 plausible (Meug); nodes 11 confirmed, 5 plausible, 1 disputed, 1 transcription_suspect.
Ref checks: 8 supports, 4 partial, 3 not_found, 8 not_checked (nodes Nourai left unreferenced). 18 books/sites consulted (KLN, POK, WLD, AHD, IEC, LAT, BRT, KNT, TLM, CHEUNG, PHD, NYB, FFD, MON, BQT, ARY, SKT, HRN + Etymonline/Wiktionary).

Flagged items:
- **transcription_suspect — Meu 1, node 6 "Middle Greek mudde 'wet earth'"**: no such Greek word; the source of *mud* is Middle Low German *mudde* (Klein s.v. mud — whose gloss "wet earth" Nourai copied; Etymonline; Pokorny 741 "Middle Low German modder"). The printed page really reads "Middle Greek", so it is the book's misprint (probably for "Middle German"), not an extraction error. `error_in: book`; page PNG saved to `data/verification/sources/refs/ocr/BOOK/338.png`.
- **disputed — Meug, node 1 "Avestan fra-muxti 'open up, describe, clarify'; a-maux-ta 'learned'"**: YAv. *framuxti-* means "the taking off (of shoes)" (Bartholomae s.v. aoθra-, V 6.27; Pokorny "Losbinden"; Cheung 2007:138 f. under Proto-Iranian *(h)mauč "to dress"). *a-maux-ta* is not Avestan at all — it is Abolghasemi's reconstructed Old Iranian *ā-mauk-ta (FFD:27, Nourai's own ref). Cheung 2007:270 makes "to learn" a separate, exclusively Iranian root *mauč³ with **no** PIE ancestry; Wiktionary takes it to PIE *h₁ewk-, not *meug-.
- Plausible with route corrections: Persian **moft** is inherited (*muk-tó- > -kt- > -ft-, cf. جفت < yuktá-, Horn no. 987 "Unsicher"), not borrowed from Sanskrit as drawn, and the relevant Skt form is *muktá-*, not *muktí-*; OP **amuθa** "fled" is certain (Kent, Tolman) but its attachment to *meug- is rejected by Walde-Pokorny II 254; Skt **munthate** means "flees", not "untie, describe, explain"; root gloss "describe" is in no source.
- Ref slips (no data fix needed): **KLN:1008** lands on Klein's "member/membrane" run — the supporting entries are ~pp. 1056/1060 (moss, mud). **BQT:2024** is the right page (Borhan vol. 4, بیان نوزدهم "میم با فا", only four entries) but Borhan has no مفت headword at all. **AHD** for the mud box: the 1985 Watkins appendix lists no MUD under *meu-*.

No extraction errors found: the JSON matches the printed page throughout.
