# Verification process log — verify-page-184


## [2026-09-05T20:55:26.828Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 184 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-184.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-184.json. Write /home/sfmqrb/git/rishe/data/verification/page-184.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 184` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T20:55:28.029Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T20:55:28.748Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T20:55:28.766Z] TOOL RESULT

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


## [2026-09-05T20:55:29.286Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-184.txt"
}
```


### [2026-09-05T20:55:29.298Z] TOOL RESULT

```
1	=== PDF page 184 (book page 154) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Ghei 2, Ghaise : to propel, move forward; spear  (refs POK:410,424)
4	#1 (parent #0) [Avestan] refs=POK:424; KLN:666; SYN:1384 | zaěna 1 : weapon ; zaya : tools, equipment ; zayan : equipped, armed ; zaenô-hâra : hold (your) weapon, be careful ☞Dher 1
5	  #2 (parent #1) [Pahlavi] refs=ISS:16 | abzâr : tools
6	    #3 (parent #2) [Persian] refs=ISS:16 | abzâr, afzâr «ابزار ، افزار» : tools | NOTE: For a different derivation of these words see root "Geu 2".
7	  #4 (parent #1) [Persian] refs=BQT:1054; PLA:162; FVF:2 | zîn «زین» : saddle ; âb-zîn «آبزین ؟ ، آبزن» : water saddle, bath tub, ship ; apsân «اپسان ؟» : grinding stone
8	    #5 (parent #4) [Arabic] refs=PLA:162; FVQ:171; VDQ:260 | safan : to peel ; safîneh : ship | NOTE: AFA:216 disagrees with this derivation
9	      #6 (parent #5) [Persian] refs=MON; VGH:74 | safîneh «سفینه» : ship, book (of poems)
10	#7 (parent #0) [Persian] refs=HUB:60; HRN:116; BQT:1055 | zenhâr «زنهار» : beware | extra: زینهار
11	#8 (parent #0) [Avestan] refs=HRN:149; DRM:290 | zaěna 2 : chain ? ; zaěna-dana : house of chains, prison ☞Dhě 2
12	  #9 (parent #8) [Persian] refs=HRN:149 | zanjîr «زنجیر» : chain ; zendân «زندان» : prison
13	#10 (parent #0) [Avestan] refs=POK:424 | zaěmi : eager ; zaěman : active ; zaěnah-vant : watchful
14	#11 (parent #0) [Germanic] refs=AHD | gaizaz : spear
15	  #12 (parent #11) [English] refs=None | garlic : due to its spear shaped leaves ; auger, garfish ; Oscar, Edgar, Roger, Gerald
16	--- entry 1 ---
17	ROOT Ghěi 3 -> redirect to Ghě 1
18	
```


## [2026-09-05T20:55:32.538Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/extracted/batch/page-184.json",
 "description": "Read source JSON for page 184"
}
```


### [2026-09-05T20:55:32.595Z] TOOL RESULT

```
{
  "pdf_page": 184,
  "book_page": 154,
  "entries": [
    {
      "root": {
        "name": "Ghei 2, Ghaise",
        "lang": "Indo-European",
        "refs": "POK:410,424",
        "gloss": "to propel, move forward; spear"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:424; KLN:666; SYN:1384",
          "words": [
            {"translit": "zaěna 1", "gloss": "weapon", "script": null},
            {"translit": "zaya", "gloss": "tools, equipment", "script": null},
            {"translit": "zayan", "gloss": "equipped, armed", "script": null},
            {"translit": "zaenô-hâra", "gloss": "hold (your) weapon, be careful", "script": null, "see": ["Dher 1"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "ISS:16",
          "words": [
            {"translit": "abzâr", "gloss": "tools", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "ISS:16",
          "words": [
            {"translit": "abzâr, afzâr", "gloss": "tools", "script": "ابزار ، افزار"}
          ],
          "note": "For a different derivation of these words see root \"Geu 2\".",
          "quote": null
        },
        {
          "id": 4,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:1054; PLA:162; FVF:2",
          "words": [
            {"translit": "zîn", "gloss": "saddle", "script": "زین"},
            {"translit": "âb-zîn", "gloss": "water saddle, bath tub, ship", "script": "آبزین ؟ ، آبزن"},
            {"translit": "apsân", "gloss": "grinding stone", "script": "اپسان ؟"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Arabic",
          "refs": "PLA:162; FVQ:171; VDQ:260",
          "words": [
            {"translit": "safan", "gloss": "to peel", "script": null},
            {"translit": "safîneh", "gloss": "ship", "script": null}
          ],
          "note": "AFA:216 disagrees with this derivation",
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Persian",
          "refs": "MON; VGH:74",
          "words": [
            {"translit": "safîneh", "gloss": "ship, book (of poems)", "script": "سفینه"}
          ],
          "note": null,
          "quote": {
            "text": "در این زمانه رفیقی که خالی از خلل است - صراحی می ناب و سفینهٔ غزل است",
            "poet": "Hâfez"
          }
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Persian",
          "refs": "HUB:60; HRN:116; BQT:1055",
          "words": [
            {"translit": "zenhâr", "gloss": "beware", "script": "زنهار"}
          ],
          "script_extra": "زینهار",
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Avestan",
          "refs": "HRN:149; DRM:290",
          "words": [
            {"translit": "zaěna 2", "gloss": "chain ?", "script": null},
            {"translit": "zaěna-dana", "gloss": "house of chains, prison", "script": null, "see": ["Dhě 2"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Persian",
          "refs": "HRN:149",
          "words": [
            {"translit": "zanjîr", "gloss": "chain", "script": "زنجیر"},
            {"translit": "zendân", "gloss": "prison", "script": "زندان"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:424",
          "words": [
            {"translit": "zaěmi", "gloss": "eager", "script": null},
            {"translit": "zaěman", "gloss": "active", "script": null},
            {"translit": "zaěnah-vant", "gloss": "watchful", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "gaizaz", "gloss": "spear", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 11,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "garlic", "gloss": "due to its spear shaped leaves", "script": null},
            {"translit": "auger, garfish", "gloss": null, "script": null},
            {"translit": "Oscar, Edgar, Roger, Gerald", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Ghěi 3",
        "redirect": "Ghě 1"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-05T20:55:33.074Z] TOOL CALL #4: Bash

```json
{
 "command": "sed -n '1,200p' data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T20:55:33.115Z] TOOL RESULT

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


## [2026-09-05T20:56:19.790Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','SYN','ISS','BQT','PLA','FVF','FVQ','VDQ','MON','VGH','HUB','HRN','DRM','AHD','AFA','BRT','PHD','NYB','ARY','CHEUNG','IEC','WLD','SKT','LKT','AFM','TAD','ARB']:\n    v=d.get(k)\n    print('==',k, json.dumps(v,ensure_ascii=False)[:600] if v else 'MISSING')\n\"",
 "description": "Check reference metadata"
}
```


### [2026-09-05T20:56:21.504Z] TOOL RESULT

```
== POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_
== KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h
== SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves
== ISS {"title": "H. W. Bailey, Indo-Scythian Studies: Khotanese Texts VI (Prolexis to the Book of Zambasta), Cambridge 1967", "edition_found": "not found; Bailey's Dictionary of Khotan Saka (1979) downloaded as the closest substitute", "kind": "google_books_preview+archive_restricted", "url": "https://books.google.com/books?id=4upthUgWo9YC (CUP 2009 reprint, partial preview) ; HathiTrust mdp.39015034317936 (v.6, search-only) ; archive.org khotanesetexts0103bail (vols I-III only, lending)", "identifier": "dictionary-of-khotan-saka (substitute); khotanesetexts0103bail is vols I-III, lending-only", "lo
== BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118
== PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 lea
== FVF {"title": "S.M.A. Emam Shushtari, Farhang-e Vazheha-ye Farsi dar Zaban-e Arabi, Anjoman-e Asar-e Melli 58, Tehran 1347/1968", "kind": "website", "url": "https://noorlib.ir/book/info/105056 (page viewer: https://noorlib.ir/book/view/105056?pageNumber=<N>&viewType=pdf) ; https://ketabnak.com/book/48613 (818 pp. PDF, login) ; http://parsianjoman.org/?p=1265 (download post)", "lookup_hint": "Alphabetical by Persian headword; noorlib page number N is the scan page — browser needed to read. Not on archive.org.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "PDF exists 
== FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sou
== VDQ {"title": "Fereydun Badreh'i (tr.), Vazheha-ye Dakhil dar Qor'an-e Majid (Persian translation of Jeffery FVQ with notes), Toos 1372/1993", "kind": "website", "url": "https://noorlib.ir/book/view/12868?pageNumber=<N>&viewType=pdf (page images; viewType=html also exists) ; info: https://noorlib.ir/book/info/12868 ; ketabnak.com/book/51136 (download blocked)", "lookup_hint": "noorlib viewer is JavaScript-rendered (WebFetch/curl get only the site chrome); needs a browser. Since it is a translation of FVQ, verify the substance via FVQ (same entry order); page numbers differ.", "local_file": null, "
== MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
== VGH {"title": "H. Khadiv Jam, Vazhe-name-ye Ghazalha-ye Hafez, Elmi 1371/1992", "kind": "website", "url": "https://ketabnak.com/book/121989 (145 pp. PDF, login)", "lookup_hint": "Not on archive.org.", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "PDF page exists; not fetched."}
== HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol
== HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 
== DRM {"title": "J. Darmesteter, Études iraniennes, 2 vols., Paris 1883", "edition_found": "1883 both tomes in one scan", "kind": "archive_djvu", "url": "https://archive.org/details/etudesiraniennes00darm", "identifier": "etudesiraniennes00darm (t.1 alone: tudesiranienne01darmuoft; t.2 alone: darmesteter-etudes-sur-la-langue-la-litterature-les-croyances-de-la-perse-ancienne)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DRM.txt", "page_offset": "Tome I: leaf = p + 22 (e.g. leaf 26 = p.4); Tome II (starts ~leaf 364): leaf = p + 364 (e.g. leaf 368 = p.4). Nourai does not say w
== AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,
== AFA {"title": "S. Fraenkel, Die aramäischen Fremdwörter im Arabischen, Leiden 1886 (repr. Hildesheim 1962, same pagination)", "edition_found": "1886", "kind": "archive_djvu", "url": "https://archive.org/details/diearamischenfr00fraegoog", "identifier": "diearamischenfr00fraegoog (also bub_gb_SzdbAAAAQAAJ)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFA.txt", "page_offset": "leaf = printed + 30 (e.g. leaf 38 = p.8). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
== BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1
== PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-
== NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf
== ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 
== CHEUNG MISSING
== IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 
== WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039
== SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves
== LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 
== AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/
== TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640", "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; insi
== ARB {"title": "al-Jawaliqi, al-Mu'arrab min al-kalam al-a'jami, Tehran 1966 (reprint of Ahmad M. Shakir's Cairo 1361/1942 edition)", "kind": "archive_djvu", "url": "https://archive.org/details/mo3rb (probably the Shakir edition) ; https://archive.org/details/almo3rab_gwaliqy_f_abduraheem (F. 'Abd al-Rahim ed., Damascus 1990) ; also uc1.aa0003615705 / AAlexandrina-148752 (Sachau's Leipzig 1867 ed.) ; text on shamela.ws", "lookup_hint": "Alphabetical Arabic headwords; grep in ARB_mo3rb.txt / ARB_abdulraheem.txt (raw, no page breaks); edition of mo3rb not confirmed — check its title page image.", "lo
```


## [2026-09-05T20:56:44.216Z] TOOL CALL #6: Bash

```json
{
 "command": "head -c 4000 data/verification/page-124.json; echo; echo \"=== verify_check ===\"; sed -n '1,120p' tools/verify_check.py",
 "description": "Inspect prior verification file and checker"
}
```


### [2026-09-05T20:56:44.268Z] TOOL RESULT

```
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
       
=== verify_check ===
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


## [2026-09-05T20:56:50.509Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"ghaiso\" POK_full.txt | head -20\necho \"--- ghei-2 ---\"\ngrep -n \"ĝhei-2\\|ghei-2\\|ĝhēi\\|ĝhei-\" POK_full.txt | head -30"
}
```


### [2026-09-05T20:56:50.566Z] TOOL RESULT

```
35803:Root / lemma: ghaiso- (or ghaiso- : gheiso-) 
36149:Old Indie hesas- n. 'projectile' (but it could also be Indo Germanic *ghaiso-s, see there); 
36159:See also: compare still gheis-, gheizd-^ be angry, furious ', as well as ghaiso- 
--- ghei-2 ---
7063:[see Root/ lemma: ghei-2. ghi-\ "winter; snow' 
7245:lemma: ghei-2, ghi-, ghei-men-, *gheimn- : 'winter; snow'. 
17987:Root / lemma: dem-, derna-: "to build; house' derived from Root/ lemma: ghei-2. ghi-: 
26888:lemma: ghei-2, ghi-, ghei-men-, *gheimn- : "winter; snow' 
32806:the winter' [see Root/ lemma: ghei-2 . ghi-\ 'winter; snow' 
36164:Root / lemma: ghei-2. ghi- 
36221:lemma: ghei-2, ghi-, ghei-men-, *gheimn- : "winter; snow' 
73509:Root/ lemma: sem-3: "summer' has certainly derived from Root/ lemma: ghei-2. ghi-,
```


## [2026-09-05T20:56:51.173Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK_01 leaf 418 (p410) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==419' POK_01.txt | head -60\necho \"=== POK_01 leaf 432 (p424) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==433' POK_01.txt | head -70"
}
```


### [2026-09-05T20:56:53.148Z] TOOL RESULT

```
=== POK_01 leaf 418 (p410) ===
=== POK_01 leaf 432 (p424) ===
```


## [2026-09-05T20:56:59.969Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '35795,35870p' POK_full.txt\necho \"#### around 36150\"\nsed -n '36140,36240p' POK_full.txt"
}
```


### [2026-09-05T20:57:00.063Z] TOOL RESULT

```
Latvian ze/ju, z/et' flourish, bloom, appear, come into view ', next to which with d- 
extension (probably originally o'-present) Lithuanian zyd{z/Ju zydef/"b\oor(\, blossom', 
prazystu, -zydau, -zysti^ blossom ', z/ec/as "bloom, blossom, ring', Latvian ziedu {ziezu), 
z/ec/e/ "bloom, blossom'. 

References: WP. I 544. 
Page(s): 355-356 

Root / lemma: ghaiso- (or ghaiso- : gheiso-) 

Meaning: stick; dart 

Material: Old Indie hesas- n. "projectile' (yet see below ^/7e/-/ "stimulate, invigorate'); 

gr. xciTo(; m. (?) "shepherd's crook; crosier'; 

gall. -Latin gaesum, gall.-gr. yaTaov "heavy iron spear, lance' (gall. gaesatT 
"mercenaries'); Old Irish ^ae "spear, javelin' {gaide^ lance '); fo-gae. Middle Irish fo-ga 
"spear, lance' = cymr. gwayw{see in addition Thurneysen lA. 26, 25, compare also abret. 



guu-goiuou' a little sharp point or sting, a weapon used for fighting at a distance; a missile 
weapon, missile, as a dart, spear, javelin ', BB. 17, 139), Middle Breton goaff, corn, gew. 

Old High German Old Saxon ger. Old English gar. Old Icelandic geirrxu. " throw spear ' 
{*gaizas)\ Gothic PN Rada-gaisu-s, wand. Gaisa-nk-s. 

In addition as -//0/7-derivative Old High German geisila. Modern High German GeiHel 
"lash, scourge, bullwhip, horsewhip; spur'. Old Icelandic ^e/s/, geislim. " stick of the 
snowshoe runners '; with ablaut (Indo Germanic eR /?) langob. gTsiT arrow shaft ' (but 
about Old High German gTsar captive = Burgschaftsgefangener ' see below gheiA^- "lust, 
crave'). Old Icelandic ^/s/(7^ "staff. 

References: WP. I 528, WH. I 575 f. 
Page(s):410 

Root / lemma: ghalg(h)- 

Meaning: (flexible) twig 

Material: Armenian ya//r "twig, branch, horsewhip, stalk, captive' (< *ghalga\ Petersson 

Heteroklisie 155 expounded den variation from ^and ghirom a paradigm *gh6lgh, 

*ghjgnes)\ 

Gothic galgaxx\. "picket, pole, cross'. Old Icelandic galgi^ gallows ', Old English gealga. 
Old Frisian galga. Old Saxon Old High German galgo^ gallows, cross', in addition further 
formations Old Icelandic ge/g/a^t\N\g, branch, shaft, pole, stick' (the oldest kind of the 
gallows was a pliable branch in which the criminal would be hanged); 

Lithuanian za/gaan6 za/gasm. "long, thin shaft, pole', Latvian za/gai. "long rod, fishing 
rod'. 

References: WP. I 540, Trautmann 364. 
Page(s):411 

Root / lemma: gha/-, ghal-ar- 

Meaning: flaw, defect 

Material: Old Irish galaru. "disease, malady, distress ', cymr. corn, galar^ sorrow, 

mourning, grief, affliction, distress, lamentation, a striking or beating accompanied by a 

loud noise, a banging, rustling, roaring '; 



Old Icelandic gallixw. "blemish, fault, error, damage' (but geallaxr\. " sore-grated place of 
the horse ', engl. ga//6s., Middle Low German ga//e^ damaged place'. Middle High 
German ga//e' swelling, tumefaction of the horse, damaged place in the rock ', Modern 
High German ^a//e "swelling, lump, growth, flaw in rock, in farmland etc' are with Ga//e 
= Ga//-apfe/ borrowed from Latin galla); 

#### around 36150
lapp. ka/to ds.; 

Gothic langob. ga/n- 'weapon' in PN {Gainhard, Gainwald), Old English gaen- in PN; 

Gothic *ga/7s{r\. 'spear, javelin' in PN Gel-mTrus, Old English Gal-frid, Old High German 
Geil-muot. 

B. gheis- ' wound, hurt ': 

Old Indie hesas- n. 'projectile' (but it could also be Indo Germanic *ghaiso-s, see there); 
in addition probably /7/s5// (previously nachved. hinasti) ' hurt, harm, injure '; 

Old Irish goite^ a wounding, wound ', Middle Irish gaetas^ strike down, knock down, cut 
down, cut off, kill, slay ' {*ghoizd-)\ 

Lithuanian zeidziu, zeidziali, zeTsti^ wound, hurt ', za/zo'a 'wound'. The same d- 
extension by gheis : gheizd- ' angry, furious '. 

References: WP. I 546, Pokorny Urillyrier 64, Holthausen Gothic etym. Wb. 34. 
See also: compare still gheis-, gheizd-^ be angry, furious ', as well as ghaiso- 
Page(s): 424-425 



Root / lemma: ghei-2. ghi- 

Meaning: winter; snow 

Note: after Specht Dekl. 14, 330 f. older -men-siem, with already Indo Germanic change 

of mn to m. 

Material: A. ghei-men-, *gheimn- 

The /"-extension is analogical after *5e/77e/'c»- "summery'. 

Old Indie heman (Lok.) "in winter', hemanta-hm. "winter' (: Hittite gimmanza 6s.)\ 

Latin hiems, -is "winter'; 

Note: 

Common Old Indie : Latin gh-> h-. 

gr. X£^MC( n. "winter, winter storm, coldness', xs'Mwv m. " winter storm, winter weather, 
winter' (in addition also x£i|Japo<; " spigot ', it would be pulled out if the ship was brought in 
the land); 

alb. Geg dimenm., Tosc dimer{e) "winter' (older Akk. *ghei-men-om)\ 

alb. Tosc dimer{e) "winter' = Armenian Ailhn o!z/77e/ "winter' = gr. xsTpa n. "winter'. 

Also alb. Geg (*x£iMapo(;) dzbore, Tosc debore^ snow ' = Armenian {*dzemon) AjhlG 
dzyoun " snow ' = gr. xiwv chion " snow '. 

alb. (*x£iMapoc;) debore, dzbore, bdore, vdore^suoW [shift -m- > -mb- > -it*- like Latin 
hibemus ( < *gheimrinos) "cold']. 

Balto Slavic * zeima {irom *zeimna) in Lithuanian ziema, Latvian zima. Old Prussian 
se/77c» "winter' and Old Church Slavic zima. Gen. zimy, russ. zima, Bulgarian zfma, Serbo- 
Croatian zfma, sloven, zfma, Czech zima, poln. zima 'mnter'. 

Hittite gi-im-ma-an-za '\N\nter' see above. 

In addition ghe/m{eJr/nos and giieiminos ^mntery' . 

In gr. xsiM^P'voc;, Latin iiibemus{< *giieimrinos), Lithuanian zieminis. Old Church Slavic 
zimbp-b, russ. zfmnij, Serbo-Croatian zfmnf, Czech zimnf {Czech zimny ^co\d'), poln. zimny 
"cold, wintery' (compare with ablaut, /in the root syllable Armenian y/77e/77 "winter'). 



To *ghei- allein: Avestan zayan-, zaen-m. "winter', npers. dar, Avestan zaya/7a- "wintery' 
and with Vrddhierung Old Indie hayana- 'annua\, yearly', hayana-m. n. 'year' (rhyme 
meaning to Avestan hamana^ summery'). 

Note: 

Gr. zvoq "year' : Latin annus'year' {*atnos) "year' : Old Indie hayana-^year\)/\ hayana-m. 
n. year' prove that Root / lemma: en-2\ year' : Root/ lemma: at-, *atno- : "to go; year' : 
Root/ lemma: uet-\ "year' [prothetic jt/- before bare initial vowels] derived from Root/ 
lemma: ghei-2, ghi-, ghei-men-, *gheimn- : "winter; snow' 

B. ghiom, ghijom, Gen. ghiemos, ghimos, also ghiomos (m from *mrR). 

Avestan zyai. "winter' (Akk. zya^^m. Gen. zimo); 

Armenian y/^/7 "snow' (< *ghiidni). Gen. Jean {< gh/fin-, s. Meillet Esquisse 45); 

gr. xiwv (*xiwm). X'Ovo(; "snow'; 



Ligurian mons Berigiema ( schneetragend '), with a reshaped ending; 

Middle Irish gem-adaig " winter night ' {gam "winter' is reshaped after sam "summer', 
compare Thurneysen KZ. 59, 2, 8; 61, 253); acymr. gaem, ncymr. gauaf, acorn, goyf, bret. 
goanv, gall, winter month Giamonpos], Eigenname Giamillus, other formations Middle Irish 
gem-radn., mcymr. gaeaf-rawd^\N\nter' {*gh//emo-rdto-, to re/'-" run'); also Irish gamu/n' 
one year-old calf ';
```


## [2026-09-05T20:57:05.540Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '36090,36150p' POK_full.txt"
}
```


### [2026-09-05T20:57:05.585Z] TOOL RESULT

```
Material: Npers. zac/ "young animal, esp. young chicken ' (c/ Arabic spelling for fj\ 

[Armenian ya^ "the young of an animal, esp. a bird, nestling, chick' is pers. loanword]; 

alb. zok, zogu'bkd, young bird, the young of the donkey'. 

References: WP. I 531. 
Page(s): 409 

Root / lemma: g(h)egh- 

Meaning: ferret 

Material: Old lndicya/7a/ra "polecat' (or "hedgehog'?), Lithuanian ses/ras "polecat' 

(originated through double assimilation iroxr\*zezkas)\ compare Lithuanian os/ra "goaf 

compared with Old Indie ajika ds. 

References: WP. I 570, W. Schuize Kl. Schr. 630; different Miihlenbach-Endzelin III 820. 

Page(s): 424 



Root / lemma: ghei-1, ghei- 

Meaning: to drive; to throw; to wound 

Note: from the meaning 'projectile' or at most verbal 'whereupon toss, fling, meet' could 

have derived ' wound, hurt ' (group B) (root form ghei-s-). 

Material: A. ghei- 'antreiben': 

Old Indie hinoti, /7//7Ka// (participle hayant-) 'set in motion, motivate, energize, stimulate, 
hurl, sling, fling', participle hita-h; heman-v\. ' eagerness '; he'tf-hm. 'projectile' (compare 
Germanic *gaida)\ 

Avestan zaen'h ' astir, keen, eager', zaeman- ' active, awake', n. 'wakefulness, agility, 
liveliness, lively being, aroused being ', zaenahvant- {irovc\ a *zaenah- n.) 'waking, 
watchful, wakeful'; zaena- m. 'weapon', zaya- m. '(*weapon), tool, piece of armament, 
weapons ', zayan- 'armed'. 

Also Old Indie /7aya-/7 'steed' = Armenian y/; Gen.y/byds. here as ' the living, the 
energetic '?; 

langob. gaidai. 'spear, javelin'. Old English gadi. 'sting, prick, cusp, peak, stick ', PN 
Old High German Gaido; in addition Old Icelandic geddai. ' pike ' < geidida, compare 
lapp. ka/to ds.; 

Gothic langob. ga/n- 'weapon' in PN {Gainhard, Gainwald), Old English gaen- in PN; 

Gothic *ga/7s{r\. 'spear, javelin' in PN Gel-mTrus, Old English Gal-frid, Old High German 
Geil-muot. 

B. gheis- ' wound, hurt ': 

Old Indie hesas- n. 'projectile' (but it could also be Indo Germanic *ghaiso-s, see there); 
in addition probably /7/s5// (previously nachved. hinasti) ' hurt, harm, injure ';
```


## [2026-09-05T20:57:22.128Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT zaēna/zaya ===\"\ngrep -n \"zaēna\\|zaena\\|zaēman\\|zaeman\\|zaēmi\\|zaemi\\|zaēnah\\|zaenah\" BRT.txt | head -60"
}
```


### [2026-09-05T20:57:22.177Z] TOOL RESULT

```
=== BRT zaēna/zaya ===
4338:•  j.  an-ava'Dhabdamna-  Adj.  'nicht  ein- schlafend': -d^mnS'  zaenauha  Y.57.16".
27470:zaenay-
27499:•  j.  zaena-  m.  'Waffe':  vasrfm  . .  ama- vastpmfm  -nam  (GP.)  Yt.  70.  96  ";  96;  — hqm  *'tta  (AP.)"  stmbayalwtm  (sd.)  Yt  i. 27;  —  *tta  (IS.)  haHtma  hutniia  Yt. 10. 141.
27501:•  j.  zaenaDh'an-  Adj,  'wachend,  wach- sam': sraes?m..yd  anavanhabdsmra  'aha (NS.)  nipaili  tnazää  däman  Y.57.  16;  16, F.  20;  —  'K>ha  (NS.)  niJspBj^aJna  (sd.) ya&a  västryS  fsuyqs  V.  13. 46.
27503:•  j.  zaenay-  Adj.  "reg,  eifrig':  yas^a  hi .  .  väam    paifi    'nil   anhat    (näroL  sp£)
27509:•  j.  zaenav-  f.  'Wehrgehänge'*':  yailqm zayanqm  raisWi  .  .  puxaa  'nätti  mat aiana  mat  "irisas  ayj.arfräil  ". .  das  Wehr- gehänge mit  dem  Köcher  sammt  30  eisen- spilzigen  Pfeilen"  V.  14. 9.
27513:•  j.  zaenah'vant- Adj.  'wachsam,  regsam': mCir?m  . .  •narthuntim  Yt  /o.  61 ;  — *'na>3uhant>m     . .    yaka     taxmS    urvpa
27518:•  g.  'zaeman-  n.  'Regsamkeit,  Munter-, Wachsein' :  ks  hvaph  c^afmmca  dät  'mäcä "wer  schuf  wohlwirkendSchlaf  und  Wachen" Y.  44. 5.
27520:•  j,  'zaeman-  Adj.  'regsam,  wach*:  •matiB F.  4  f.
30515:•  j.  hu-zaena-  Adj,  'mit  schönen,  guten Waffen';  mihnm . .  'n^m  . .  vn-Hsravastittum
```


## [2026-09-05T20:57:23.302Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN 116 leaf 137 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==138' HRN.txt\necho \"=== HRN 149 leaf 170 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==171' HRN.txt"
}
```


### [2026-09-05T20:57:25.287Z] TOOL RESULT

```
=== HRN 116 leaf 137 ===
— 116 —
'setzen, machen, schaffen ; phlv. dätan; ai. l^dhä-,
dädhati; arm. dnel setzen' (H. No. 84).
522. (Tür 'Baumstamm, Holz', dann,
aw. däuni' 'Holz'; phlv. dar, dann 'hölzern (vd. 7
(188)), vergl. arm. LW. darastan 'Garten'; ai. därtt-
*Holz\
np. durük 'dünnes Holz' (unbelcgt) gehört dagegen
zu ai. drü' 'Holz, Baum', gr. d(jvg Baum, Eiche', d()ior
{*ö(jfoi') 'Gehölz', ksl. drüvo (d. i. '^'drvo), got. friu 'Holz,
Baum'.
LW. kurd. dar; bei. dar (55).
523. därü, därUt *Ai'znei; Schiesspulvor', vergl. der man
(No. 554).
l^dhar- 'halten', vergl. aw. drva- gesund; phlv. därük
'Arznei'.
LW. kurd. af/. bei. (56) därü,
524. dm*e 'Gehalt, Salair'.
aw. dadra- 'Geschenk, Gabe'; phlv. ddsr; ai. däfra-
'Gabe'.
Hörn, KZ. 32, 584 No. 15.
525. (IffS 'Sichel'.
ai. dätra- 'Sichel'; phlv. das (AV.).
afy. lür 'Sichel'; LW. kurd. bei. (76) das,
526. däS 'Ofen*.
Zu [/'dagli' (aw. dajjz-, ai. rfa/i-), brennen (Nöldeke,
mündliche Mitteilung).
527. dästen 'halten, besitzen', Praes. där-em, dar, dara,
g. dartmfm; Käs. dörtän^ dördhi, dörd^nmn^ dort.
ap. l/^rfar-, darayamiy, adäraya 'halten, besitzen';
aw. [/^dar-^ däray^M; phlv. dästan^ dar-am, dar(i)sv^
dästar [syr. LW. *T1, ödg (de Lagarde, Ges. Abh.
33) sind verlesen (Nöldeke, Tabarl-Übersetzung,
447)] ; ai. [/^dhar-, dharäyati,
kurd. 'dar (LW.); af/. laral; oss. t. daf-in (102);
bei. (L W. ?) darag , n. daray (75) ; wa/. va-dür-am,
sar. ö6r-am.
Gehört hierher vielleicht auch zJnhär, zinhnr 'Schutz,
=== HRN 149 leaf 170 ===
149
Der Bedüutungsunterschied macht diese Zusammen-
stellung bedenklich.
671. niindän 'Gefängniss'.
aw. *2:aewa.d(2wa- (y) ; ^\\\\, z(i)ndan (PPöl.); arm.
LW. zndan.
Etwa urspr. 'WafFenarsenar wie auch HNIliNDN (Jer.
32 (2) 8) *Ort, an dem die Scheiben aufgehoben werden*,
allgemein 'Gefängniss* heisst? Darmesteter, Et. ir.
I, 290 setzt zweifelnd auch np. zen}Tr^ zmjlr (andere
iranische Formen siehe bei Geiger bei. LW. No. 299)
hierher 0. Vergl. Hörn, KZ. 32, 583 No. 13 2).
672. xinüden, zunüden *heulen , Praes. ziuec-em, ztmöylden.
ai. [/'nav-j naiiti, ndmite *brüllen (von Tieren)', mit
accha 'zurufen' (mit ud kommt es nicht vor).
Vergl. np. nöyiden etc. (No. 1054).
673. xüd 'schnell'.
aw. \/jav- 'eilen*, Java, javarö (?, Geldner, BB.
XIV, 21, 22, aber auch KZ. 30, 533); phlv. zät (päz.
zöt); ai. i^jav-, jdvate *eilen*.
kurd. zu; bei. züt^ zU, n. zid^ (430).
674. zur 'falsch; Lüge*.
ap. zurah- {znrah-) ; aw. zurö.Jata- ; phlv. zur,
zür]zat, zür]ynhäsih, arm. LW. zur\ ai. hvaras-.
Bartholomae, zuletzt ZDM6. 46, 296, Ilübsch-
mann, gleichzeitig ib. 329.
674*»^'* {\)»ör 'Kraft, Gewalt' (reimt auf hör, Sahn. I, 202
Vers 1311).
aw. zävar- 'Macht, Kraft*; phlv. zör, zörlh, arm.
LW. zatir^ zaurcwor, zauruüun,
LW. kurd. afy. bei. (312) zör.
675. {^i)zör 'Weihwasser (pärsisch).
aw. zaotirä' 'Weihwasser*; phlv. zölir, zur, arm.
*) Im Ossctisclicn bezeichnet das L W. zjndon *Höllc* (v o n
Stack elberg, Baltische Monatsschrift, XXKVIII, lieft 8, 674).
*J Herr Prof. Nöldeke vermag zindän mit plene geschriebenem
i bezw. e im Pehlevl zu belogen, was für die Richtigkeit der obigen
Etymologie spricht.
```


## [2026-09-05T20:57:34.825Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN p117 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==139' HRN.txt | head -30\necho \"=== HUB p60 (leaf 70) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==71' HUB.txt"
}
```


### [2026-09-05T20:57:36.588Z] TOOL RESULT

```
=== HRN p117 ===
— 117 —
Sicherheit etc.*, ursprünglich 'hüte dich vor diesem,
halte dich von diesem zurück', wovon dann zTnharT
und nach dem FS sogar zinhariden gebildet wurden?
Allerdings wüsste ich dann nicht die Messung von
zinhar als Amphimacrus bei FirdüsT zu erklären, die
mir jedenfalls (vergl. Indog. Forsch. II, 185) für
iranischen Ursprung des Wortes zu sprechen scheint
(anders Nöldeke, Pers. Stud. II, 46, dessen Erklärung
aus dem aramäischen *inT, wie er selbst zugiebt,
wegen des t Bedenken erregt).
528. danen 'Geschenk, Gabe'.
g. däsn.
phlv. dah(i)Sn ; vergl. padäsn (No. 265*'^'').
529. däy 'Brandmal*, dey.
aw. daya-\ phlv. däy (vd. 15 (48) Gl.); ai. ddha-
'Brand*, skr. ni]däghd' 'Hitze*, Sommer'; lit. dagä 'heisse
Zeit, Sommer.
LW. kurd. afy. däy; bei. däg, n. day (52).
580. {\)ääm 'Haustier, zahmes Tier.
ai. l/"rfam-, d!(^wyci^i"zähmen, zahm sein'; gr. öujiidATjQ
'Stier; lat. domäre; air. dam 'Ochs, Stier ; got. ga-
tamjan, nhd. zahm,
oss. vergl. domun 'zähmen' (108).
phlv. dam 'Geschöpf (aw. däman-) ist im Np. auf-
gegeben.
531. {?)däif¥i *Netz'.
ai. däman- 'Band, Fessel*.
afy. lüm; arm. LW. (?) damK 'N(?tz'.
532. dämäd 'Schwiegersohn; Bräutigam (Vis und Käniin,
=== HUB p60 (leaf 70) ===
— 60 -
527. Np. »lnhdr 'Schutz, Sicherheit, Zuflucht' ist natiirlich
nicht aus az in ddr entstanden, da d hier nicht zu h
werden konnte. Andreas erklart sfinhar aus az m
har von Wzl. har *servare (ZDMG. 47, 704), Fr.
M tiller setzt es = zd. *zaend-hara- *Waflfenschutz'
(WZKM. 8, 96). Die letzte Erklarung scheint mir
die beste. Zum Gebrauch von zmkdr als Interjektion
gi^b acht* vgl. d. Achtung!, mhd. wafenl etc.
528. Nach Noldeke ddSn, wie es der Etymologie ent-
spricht.
534. Arm. catiacem *kenne' gehort nicht hierher. Der In-
finitiv ddnistan ist aus dem Praesens danam neu
gebildet, wie uberhaupt alle hier angefuhrten irani-
schen Formen zum Praesensstamm iran. zdna- = np.
dana- gehSren. Vgl. dazu unten Nr. 793.
538. Np. ddh nach Vullers = 'ancilla, serva, famula.
540. Arm. dpir setzt phi. diplr voraus und macht mir
Horn's phi. dipivar nicht wahrscheinlich. F r. M u 1 1 e r
fuhrt (WZKM. 7, 376) np. dwdn ^Tribunal' auf phi.
*attvdn = arm. atean zuruck, was ich nicht fur richtig
halte. Np. daftar, arab. LW. daftar, diftar — gr.
SKp^iga (Noldeke).
541. Armenische Frauennamen mit duxt sind haufig, nur
gerade Tigranaduxt kommt meines Wissens nicht vor.
542. Zu skr. daksa- gehSrt daksina- *tuchtig, recht* = zd.
dasina-. Also ware skr. daksa- = zd. *dasa' = np.
das (nicht daooS), Vgl. Fr. Muller, WZKM. 8, 94.
546. Np. dar 'hinein, in' aus andar wie darun aus andarUft,
darx^'ar aus andarx^ar. Vgl. deutsch raus = heraus,
rein = herein u. s. w.
547. Die Gleichung paz. np. der lange = ap. darga- wider-
spricht den Lautgesetzen , scheint aber gleichwohl
richtig. Ich vermute Umstellung von ap. darga- zu
^dagra- = ^dayra-, das zu der wurde wie zd. anayrandm
= phi. np. aneran^ zd. tiyri- = np. t%r ist.
548. Etymologie dunkel.
550. Etymologie dunkel.
```


## [2026-09-05T20:57:37.213Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD abzar / zen ===\"; grep -n \"abzār\\|abzar\\|zēn\\b\\|zēn \\|zendān\\|zindān\\|zēndān\" PHD.txt | head -30\necho \"=== PHD_mackenzie ===\"; grep -n \"abzār\\|zēn \" PHD_mackenzie.txt | head -20\necho \"=== NYB ===\"; grep -n \"abzār\\|abzar\\|zēn\\b\\|zēndān\\|zaēna\" NYB_vol2_glossary.txt | head -30"
}
```


### [2026-09-05T20:57:37.325Z] TOOL RESULT

```
=== PHD abzar / zen ===
170:abilag 5/4! | N ~a] blister. a-bim [bym] fearless. āb-kāmag [5A mk! | N ~a] a thick, sour soup. abnüs Pžēnws | (N ābnūs)] ebony. a-biy Pbwd] senseless. ~ih: senselessness. à abr РЫ, Séi | N ~] cloud. M bel abrang [ing | N aurang] glory, splendour. abrastan, abraz- [AP stn',SPc- | М ?br?st, N (afráttan), afrdz-] lift, raise. abraz [Pe | N afrāz] acclivity. abrēšom Pflyš(u)m | M? bryfwm, N ~} silk. ~én [-yn!] silken. abróxtan, abróz- ['piwhtn', ?phoc- | M brwxt, ?)brwc-, N afróxtan, afróz-] light, kindle, illuminate, polish. ~i$n(ih): illumination. āb-tazan Pftcn!] watercourse. a-bun [*dwx!] baseless, bottomless. a-burd-framān ['bwltplm^n'] disobedient. ~th: disobedience. aburnāy f(w)lnd, v. purnāy | N burnā] under age, child. ^h : childhood. aburnáyag [?A(w)/n’(d)yk'] child. abus [pws] (woman) having just given birth. “АҺ: childbirth. арив, -tan Pws, -tn! | M ’bwws, v. ábestan] pregnant. „il: pregnancy. abydxtan, abyóz- Phywhtn', ?bywc-] join, mix. āb-zan zn! | N ~] bath. labzar [el pel] M *6c*7, N afzār] instrument, means; spice. *abzar [6271 | M bail skill, power; powerful. „ūmand [-wmnd] skilled, able. abzāy-, —išn, у. abztidan, abzón [?pzwn! | M, J ”*bzwn, N afzün] increase, growth. ~ig [-yk!] increasing, expansive, bountiful. ~igih: bountifulness. abzüdan, abzáy- ['pzwtn!,^?pzd- | M ?bz'y-, N afzüdan, afzāy-] in- crease, grow. ~i$n: increase, growth. a-čār [cI] inevitable, Jee ~ag [-k'] compelled.
191:amāwandīh: power, strength. ambag [’mbk' | N anbajat] a preserve, conserve. ambar [mbl, ?nbl | Аг. ‘праг ambergris. ambarag [?mblk! | N anbara] hairless (animal). Р amburdan [h/^mbwultn! | Р ?mPr-] = hambārīdan. a-menīdār [^mynyt!l] unthinking. āmēxtan, āmēz- Pmyhtn', ?тус- | M *myxtn, ?myz-, N ~] mix. ~išn: mixture; element. āmiz [^myc] side dish, vegetables. āmēxtan, āmēz-, read hammóxtan, hammoóz-. Amurdād [?m(w)rdt' | N murdád] Immortality, the sixth Amahraspand, guardian of plants and food; cal. sth month; 7th day. āmurzīdan, āmurz- [mewlc-ytn! | M?mwrz-yd, N ~) forgive, pity, have mercy on. ~išn: mercy, forgiveness. Р amwaštan [h|mwstn! | P ?mwst] gather, collect. an- Pn- | M ’n-] prevocalic privative prefix, un-, -less. ап [ZK < A zk;?n! | M Ап, N ~] that, he. ~ 1: that of; with a qualifier preceding a noun, equivalent to a following 1 e.g. ап i ahlawàn ruwān = ruwan i ahlawān, the souls of the righteous. -ап [2s! | M An N ~] suffix forming (i) present participles, (ii) adverbs, (iii) plurals. ānāb-, —išn, v. ānāftan. an-ābādān Ppp’ rn'] uncultivated. an-abaxšāwand [m ph} wnd] unrepentant. ~ih: unrepentance. an-abāy Pr’ Pd) unfitting, improper. an-abēdān [”7?5yt?x'] useless, unwanted. ~th: uselessness. anübublag [9 fwhlk' = Av. anüpers0a-] inexpiable, unatonable; the highest degree of sin. an-abzār Pwi] unskilled, incapable. ~th: inability. an-ādān [*77:?x!] insolvent. ^h : insolvency. an-ádüg [tk] incapable. an-afsēnišn [”77?syx$n!] indestructible. ānāftan, ānāb- [77ftn',*775- | M ?w pt, Qn m-)] avert, reject, frustrate. ~išn: avoidance, warding off. anág [77 k! | M >ре} evil. ~th: evil, harm. an-ügàh и: | N ndgah] unaware, unwitting. anüg-kardàr [RU АРД, -kunisn [-kwnšn'] evil-doer, maleficent. anagr Pngl) infinite. ~an [”x! | M?nyr^n] Infinite Light; cal. 30th day.
593:tan-bahr [żn'Þ’ hl] physique. tand [tnd | = P] faint, languishing. ~ih: faintness, langour. | tan-drust [tn'drw(y)st! | N ~] healthy, whole. ~ih: health. tang [ing | = M, N ~] narrow, tight. ~ih: narrowness; distress. tanig [tn'yk! | N tani] bodily, corporal. tanigard(ig) [tnykrt(yk)! | M inygyrd] corporeal. ` tanīhā [tn'y/? | M tnyP?, N tanha] alone. tanómand [tn wmnd | N ~] corporeal. “АҺ: corporeality. tan-tdhmag [tn'twhmk'] (sap) of plants. tanuk [tnwk! | N ~] thin, shallow, tanür [tnw] | M tnwr, N ~] oven. tar [LCDr! < A l-sd; tl | M tr] over, through, across. ~ kardan, ~ menidan: abuse, despise. -tar [-z# | (M -dr), N ~] suffix forming comparative adjectives. tar [2] | M гу] darkness. tarāzēnīdan, tarāzēn- [tcyn-ytn!] weigh. tarázüg [tPcwk! | (P tPzwg), N tarazü] balance, scales; astr. Libra. targ [tlg | N ~] helmet. tarģumān [tigm?n! | M trgwmn] interpreter. tarig/k [PIyk! | M гуур, N tárik!] dark. ~th: darkness. tarist [¢/st'] = tar. tar-mānīh [t/m’nyh] perversity. tar-menišn [tImynin! | N tarmanist] perverse; contemptuous. 7h : perversity; contempt. tarr [t/, LC Dr (in error, v. tar) | N —] moist, fresh. ~ag [tik! | N ~a] vegetable. tars [2/5 | M trs, N ~] fear, respect. tarság [ts k! | M trs’g, N tarsā] Christian. tarsāģāh [15(?)/?5] respectful, reverent. ~ih: respect, reverence. tarsidan, tars- [tls-ytn' | (M tyrs??dn), N ~] fear, be afraid. tarwénidan, tarwēn- [t/zvyn-ytn! | M trw-] overcome, conquer. tas [25 | N ~] die (for gaming). tasum [tswm | = M] fourth. tāšīdan, tāš- [O i-ytn!'] cut, cleave; create. taSkanag [tšknk!] under-shirt. tašt [tšt' | N ~] bowl. tāšt [021] *certainty. ~ig [-yk'] certain. tāwān [1?(d)w’n' | N ~] compensation, obligation. taxl [t?% | (M thr), P txl, N talx] bitter.
679:zàz [2z | = M, (N zaz)] weed, useless plant. *zéfan [zyp?n! | (N zif)] wrong, vile. izēn [zyn! | = M] weapon, armour.
680:žzēn [zyn! | N zin] saddle. zēn-abzār [zyn'pe!l | N zinafzár] horse-armour. zēnāwand [zy>zond] alert, vigilant. zēndān [zynd?n! | = M, N zindān] prison. «bān [-p?*x! | N -ban] jailer. ~ig [-yk! | N -i] prisoner. zënënidan, zënën- [zynyn-ytn!] look after, preserve. zēnhār [zyn)?] | N zinhàr] protection. zénig [zynyk!] armed. *zibāl [zb | N zībāl] swift (horse, etc.). zih [zyh | N zih] bow-string. zindag [zy(w)ndk! | M zyndg, N zinda] alive, living. ~th: life. zindakkar [zywndkkl | M zyndkr] vivifier, reviver. zinénidan, zinén- [zynyn-ytn'] damage, harm. zirak [zylk' | M zyr, N ~] wise, clever. zistan, v. ziwistan. zišt [zyst! | = P, N ~] hateful, ugly. ziwénidan, ziwén- [zywyn-ytn! | M zywyn-] vivify, revive. zi(wi)stan, zi(w)- [zyz-stn! | M zywystn, zyw-, N zistan] live. zi(w)išn [zywšn! | M zyysn] life; livelihood. ~ih: life, living. --6mand [-”xmnd] living, alive. ziyānaģ [zyd?nk'] young woman. zīyišn, v. zī(w)išn. zofāy [zwp'd | M zwp’y] deep; depth. *~ih: depth. ` zofr [zwpl | M zwwpr, J zwrf, (N žarf)) deep. —šy [2d] depth. ~-payag [-p'dyk'] deep. zóhr [zwhl | M zwhr] libation, offering. zor [z())wl | M zwr, N ~] power, strength. Bay ge J ~ig, ~dmand [-yk!, -wmnd | M -mnd, N —mand] powerful, strong. d z^ 201 [zwt! = Av. zaotar-] first officiating priest. ~ih: office of 201. Zraw-, v. zruftan. !zréh [zlyh | P zryh] sea, lake. *zréh [ziyh | N zirih] armour. zruftan, zraw- [zlwp-tn'] = azruftan. zūd [zwt! | M zwd, N ~] quick(ly). ^h : speed. zür [zwl | M z*wr] false, deceitful.
763:alert gubrag, wigrād, zēnāwand.
2318:horse-armour zénabzar.
2402:inability anabzārīh.
2455:instrument abzar, zay; (stringed) réd.
2495:jailer zēndānbān.
2579:leaden arzīzēn, srubēn.
2622:lighten rēzēnīdan.
2759:means abzar, ar.
3059:pavilion kēšk, mašk; royal ~ mašk- abarzēn.
3194:power abzār, amāwandīh, nērēg, 07, stahm, tuwān, zor.
3195:powerful abzār, amāvand, kāmgār, nérógomand, ózómand, pādixšā(y), pādyāwand, warzāwand, orig, zóromand.
3215:preserve (v.) dāštan, zēnēnīdan.
3225:prison zēndān.
3226:risoner wardag, zēndānīg; v. captive.
3567:select (a.) pad-wizēn.
3682:skill abzar, hunar, hunarāwandīh, kārāgāhih, kirrēgih, nēzūmānīh.
3683:skilled ` abzarómand, frahixtag, hunarāwand, hunarómand, kār- āgāh, kirrēg.
3771:spice abzār.
4213:vigilant gubrag, zēnāwand.
4457:tazēnīdan
4471:tar, tarr tarazén- tarāzēnīdan tarāzūg piht
4663:frazām-pērēzīh va eye à оу frazaftan we” à Q frazēn, parzin w Ф оу
4707:padwizēn
4823:[140] mastog 19112256 mehtar Vess mastarg > e26 mizagūmand 2061” 406 mizagdārīh AAS 3G mizag 1.5 0G rūynī NINE maškabarzēn NS ey wi? makkizag 1923 556 1-2mašk way deh! ATES dehgiin! uses madār У. о mih мес madan, 1-3mihr мео
4917:rozag ranjēn-, rūzēn-
=== PHD_mackenzie ===
=== NYB ===
413:Amahraspands 397-8; an amäh u Pw!] Gi 6 ham tuxšem [this reading should. be restored] andar äp, andar damik, andar urvar, andar gospand we and he will labour jointly in water, soil, plants, cattle 3915-16; an-ip to ... fräc vēnēnd for thee (dat. ethicus: thou mayest know:) they prophesy ... 51% (v. tē and -p); an 6 amäh asp vāzēnēt you there, bring the horse here to us 541° (cf Spanish nosotros, vosotros); an či gäv that (re- markable) bull 427. 49?-5-18-19; ang [ZK-y] či asp that (remarkable) horse 491’; an če that very man 5419; an alone for the Ist p. sg., v. the next w. — Av. (135 sqq.) anya-, ainya-, OP aniya-; MPrth ny; MPrs ^», "ny ‘another’ (also = 2an); Paz. han, with -c: hanica. In J-Prs hm, ’ny emphasizing a pron. as described above, v. Mackenzie, An early Jewish Persian argument (BSOAS XXXI, 1968, 249-269), L, 1. 14 (p. 262): whny "wy dd dyh ‘and He is the lawgiver’ (hesitatingly combined. with ^ny by M. p. 254); Utas, The Jewish- Persian fragment from Dandàn-Uliq, Or. Su. XVII, 1968 (1969), 129, 1. 13: ny man simply = ‘T, Ll 4: ny mr = anë mara ‘for me’. — Cf also änöd and. enyä.
909:band [bnd] tie, band, bond; fetters 919. 34! (81? probably mistaken for bry<n> = brin, cf Mx ch. 279; Paz. is wanting); ~ + zēndān imprisonment, captivity 9°; ~ the snare of Death 6514-18; ca rād ka menčyan u gētīkān dänisn u kār-ākāhēh har 2 band 6 tč [i.e. xrat] patvast why are knowledge and skill of both the heavenly and the earthly beings (so) closely tied up with (dependent on) thee [the Wisdom]? 8811-12; the Skr. v. joins band with the preceding har 2: dvdvapi bandhau, but this is contradicted by 12017-18; cigön martömäan i andar gété band 6 mēnēyān patvast estet as men in this world are closely tied up with the heavenly beings. — Av. (926 sq.) banda- ; MPrth. bnd; bndys?n ‘prison’ (MHC); MPrs bnd (A-H II), bn = bann (S, A-H I), bnyst’n = bannistän < band- (A-H I); Paz. NP band. V. bastan.
3847:ulēh [L’L’-yh], wë [+ -c: D’L’y-c] up- wards, above: pat uléh emphasizing the prev. ul in pat uleh ul nikérit 51%*-*%; pat uleh ul vāzēnēm 60°; — ule-c on high 42). - Cf Av. (351) loc. orodvaya ‘in upright, standing position’; cf also nıküneh.
4059:vizčnitan [w’cynytn'] to bring, to take a p. to a place (andar) 49?’; to lead (a horse) up to (0) a p. 5413-15; à tē pat ulēh ul vāzēnēm we shall carry thee up in the air 60%. — Caus. of väzitan.
4060:vāzēnītār one who draws, pulls: asp i rahy ~ a chariot-horse 581”.
4537:zēnāvandihā [zyn’wndyh?] vigilantly 6713. — From zēnāvand, Av. (1651) začnahvant- ‘vigilant’.
4538:zēn-dān [zynd’n'] prison 93. 11625 (twice). — “Keeping-place of arms" = ‘arsenal’,
5469:zaēnahvant-: zēnāvan- dihā
5470:zaēnu-: zēn
```


## [2026-09-05T20:58:15.443Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT context 27460-27525 ===\"; sed -n '27460,27525p' BRT.txt\necho \"=== BRT zaemi search ===\"; grep -n \"zaēmi\\|za[eē]mi\\|zaimi\" BRT.txt | head"
}
```


### [2026-09-05T20:58:15.508Z] TOOL RESULT

```
=== BRT context 27460-27525 ===
•  j.  trütar-  m.  'der  hört'  oder  'der  zu Gehör  bringt'.
KompE.  (in  EN.).  —  Zum  V.  srav-.    —  VgL
•  j.  *srutö.sp5da-'>  m.  EN.  eines  Gläu- bigen, Bruders  des  Wnzav.  TTTtvi  'ää (GD.)'J  aiaonä  "des  ff.  und  des  Sp.,  der beiden  . ."  Yt.  13. 1 1 5.
Eig.  'der  ein  berühmtes  Heer  hat  {Lmkarf  St.
—  ')  So  F  1 —  J)  Uothero.  —  ii  Eine  priester- liche  Deutung  Dk.  7.  7.  8.
•  g.  srüidyäi  Inf.  'zu  hören,  zu  verneh- men': vai)  sr°  hyat  marstaÜbyS  vahisttm "als  das  Wort,  das  zu  hören  den  Men- schen das  beste  ist"  Y.  4I5. 5 ;  —  sf  masdä /rävaocä  'tu  kund,  o  M.,  dass  man  es höre"  Y.,9^.  12.
mit  frä  in  pass.  Sinn  'audiri,  so  zu  wer- den,  dass  man  davon  hört,   bekannt  zu
dby  Google
i649
srutgaoäa-
zaenay-
1650
werden':  yS  . .  kv5  nä  */rair''^  *gnhwö "wer . .  er,  der  würdig  ist,  dass  man  von ihm  höre"  Y.46^,  13;  —  i!  vä  */rasr'''1 vasti  "oder  wer  will,  dass  man  von  ihm höre?"  Y.4^.  14.
Zum  V.  jrav-.  —  PQ,  (lu  Y.  ^j):  iräjiffn  da- hiJHlh,  (tn  y,  24)-  nigSSem,  SC;  ifnimi,  {lu Y.  46):  frac  sräyüit  dahibüh.  —  ")  ^k./irasr', s.  Var.
•  j.  srutgaoSa-  Adj,  'des  Ohren  hören, scharfhörig"':  mt^raiaf  .  .  °lS  hazanra.- yaoxsHS  YtJO.107;  19.35.
KoinpE.i  Ableit.—  Vgl  m.  h-ütiar^a^  Adj.
•  ]'.  snitgao^.'t^ma-  Adj.  'des  Ohren am  besten  hören,  der  am  besten  hört' a^arn  nafstMn  . .  yd  . .  'mS  asH  yezimnö (sd)  Yt  75.52.
•  j.  surunvata-  Adj.  'hörbar,  laut*:  hm yasai  °ta  yasna  sraoSifn  .  .  taokräiyU  Y. 57-3;  Vt.^.i8,  s.<).
FFP.  zum  V.  srav;  ^x,t  dem  Praes.  lo  turumi^ gebildet,  %  30fi.  11.  —  Pil.:  tiigöHhtömatid, Npü. :  Sunüda.
•  g.  suninvant-  Adj.  'belehrt,  gelehrt': 'Vatas(AP.)cä  asurunvatascä  '^■35.  4.
KompE.  —  PPA.  lum  V.  srav- ;  mm  Praes.  lo i»mfn^,eig. 'hörend,  lernend',  näml.  die  heilige Lehre.    —    Pü,!    äsnaväi  -  Sü.!    Initavän  -, eil. :  iui  fhtpaiisiän  Marl  iitcl. j.  srärim  N.  65:  lies  srlrim.
•  j,  srva-  n.  'Blei;  Gefäss  aus  Blei'; ayanhaintm  v3  °rttm  **  va  rättma  (sd.) xsa^ra  vairya  "in'>  einem  Gefäss  aus Eisen    oder   aus  Blei  . ."  V.16.6;  5.14;
— jr^i  'rum''>  jiai/iMHc^i {sd.)  V.p,  14;  — ildrun/aydiJ'  aom  'rum''>  paurva.raemäi (sd.)  . .  Y.g.  14.
Pü.  (lu  V.p.  14  3.St.):  truf,  (sonst)  snifi».  — '}  S.  Sp.  S9S  m.  mit  No.  1.  —  «)  D.  L  *sru-
•  j.  STvaena-  Adj.  'hörnen,  aus  Hom  be- stehend': 'na  a^qm  fnäml.  aurvatqm)  sa- fäahs  saranya  paiti%waritar3ks  (sd.)  Y. 57-2  7-
Ableit  aal  jr «-.  —  Pü. :  snrven  ').  —  ■)  Nicht 'bleiern',  vgl.  Pü.  zu  V.  p.  14  und  Hbm. PSt.  74-
•  j.  srvant-,  sravant-  "  Adj.  'schleichend, anschleichend':  -afa/J  (GS.)  F. /^.
mit  upa  'sich  (wie  ein  Raubtier)  heran- schleichend': sjmö  Cdcs  Winters')  ..  'vats V.  7.  37.
PPA.  am  ar.  'tsrau-,  einer  »-'Enreitcrung* (Prael.  20)  uis  *lsar.  in  u.  tsaraä  'er  (be> schleicht' ;  vgl.  iravuahav-  und  ai.  tiärav-  m. 'schleichende»  Tier';    femer  lU  aBvijrü%ra:
S.  lEt.  Bthl.  IF.  p.  276;  femer  Bloomfield IK.  4.  72.  JAOS.  z6.  CHX,  OsTMOFF  BB.  33. 257,  Flensburg  Stud.  7.  —  Pü.  tiu  F.):  äSiiip *Ha»t,  Aufregung',  (lu  V.):  <^>ar  Ut3p  kar, erL  I  Ssän  anilrth  hac  al.  —  1)  So  F. ;  S  26S.  1 1 .
•  j.  srvara-  Adj.  'gehörnt"':  asTm  'r^m .  .  yim  .  .  tairit?m  Y.g.  11.
Komp.:  irü-+*iarii;  %i6S.2T,  BTHL.BB./J. 14.  —  Pä.i  transskr.  (ddmbr),  —  >>  Die ionischen  Tiere  auf  den  Wandtläcben  in Peisepolis  sind  alle  gehörnt;  s.  trvÖJiana-; vgl.  DsT.  ZA.  /.  88  No.  31.  —  ')  Man  nahm das  Wort  als  EN. ;  1.  SBE.  iS.  374,  37-  i8S. ^7.  12,  vonStackelberg  WZKM.  ti.  340.
•  j.  srvä-  t:  s.  unter  srU-. KompA.
•  j.  srvo.zana-  Adj.  'zur  Hornrasse,  zur Rassc  der  Gehörnten  gehörig';  snaviihm yim  'n>m  Yt7p.  43.
Vgl.  ReMY  JAOS.  20.  70  und  zu  srvara-  No.  I.
•  j.  srvi^täy-  Adj.  'mithömemen  Widei- haJten',  vom  Pfeil ;  ifunqm  *kahrkäss.para- nam  zaranyS.zafram  °stayam  Yt, /o,  139.
'Komp.  mit  ND.  (*.  srü-  NÖ.  3)  im  1.  Glied; "iläy  f.,  zum  V.  ttä-,  s.  daiu  ZDMG.  4^.  665 und  mp.  ittnii.  Eig.;  'dem  ein  Horn(spltzen)- paar  als  Ständer  dient',  vom  Pfeil,  an  dem unterhalb  der  Spitze  ein  paar  Hornspitzen  als Widerhaken  eingesetzt  sind,  durch  die  er  in der  Wunde  zum  Stehen  gebracht  werden, festsitzen  solL
j.  tä  ¥4  a:  lies  :i;  s.  sam-.
j.  Eoräs ;  s.  unter  ioina-  und  zayan-.
•  j.  zaena-  m.  'Waffe':  vasrfm  . .  ama- vastpmfm  -nam  (GP.)  Yt.  70.  96  ";  96;  — hqm  *'tta  (AP.)"  stmbayalwtm  (sd.)  Yt  i. 27;  —  *tta  (IS.)  haHtma  hutniia  Yt. 10. 141.
KompE.  —  ai.  vgl.  Arläy-  f.  'Waffe'.  —  mp. sfn,  np.  :ii*.  —  Vgl.  saya-,  'za/nay-.  —  Pü. (zu  Yt.  /):  a-J^zär.  —  »  Vgl.  Yt.  /o.  132.— ')  NA.  tanva,  vgl.  Gdn.  KZ.  JO.  514.  S.  aber Pü.  und  die  Hds.
•  j.  zaenaDh'an-  Adj,  'wachend,  wach- sam': sraes?m..yd  anavanhabdsmra  'aha (NS.)  nipaili  tnazää  däman  Y.57.  16;  16, F.  20;  —  'K>ha  (NS.)  niJspBj^aJna  (sd.) ya&a  västryS  fsuyqs  V.  13. 46.
Ableit  a.ax  zalimh:  —  Pü.:  linävand,  pa  ünä-
•  j.  zaenay-  Adj.  "reg,  eifrig':  yas^a  hi .  .  väam    paifi    'nil   anhat    (näroL  sp£)
dby  Google
1651
"wenn  er  {der  Hund)  ..  eifrig  ist  mit  (der Stimme  sva.)  Bellen"  V.  /j.  40.
KompA.  —  VgL  lafmoB:  —  Pü.;  lüca  fa  in
i  ei  gffwiin  • .  apar  anhand  ait.
•  j.  zaenav-  f.  'Wehrgehänge'*':  yailqm zayanqm  raisWi  .  .  puxaa  'nätti  mat aiana  mat  "irisas  ayj.arfräil  ". .  das  Wehr- gehänge mit  dem  Köcher  sammt  30  eisen- spilzigen  Pfeilen"  V.  14. 9.
•)  Das  »on  der  linken  Hüfte  über  die  rechte Schulter  lief  und  insbetondere  «um  Tragen  des Köchen  dienie:  TgL  auf  der  Inschrift  toq  Ba- Aiitän  die  Figur  dei  hinter  dem  KOnig  ctehen- den  renere.
KompEi  —  np.  z!n  'Sattel'.  —  Pü. :  an.
•  j.  zalnah-  n.:  sva.  'xalman-  n. Ableit.   —    mp.  ün*;    i.  dazu  Btrl.  IF.  r2. IA2.
•  j.  zaenah'vant- Adj.  'wachsam,  regsam': mCir?m  . .  •narthuntim  Yt  /o.  61 ;  — *'na>3uhant>m     . .    yaka     taxmS    urvpa
A2.2'>,
rü. :  zhtävand.  —  >)  Vgl.  lU  aiinasan/;
•  j.  zaeni.buSra-  Adj.  'reg,  eifrig  wachend, wachsam':  spatam  .  .  °rmi  V.  y.  39.
VgL+Juira-EN.  — Pü.;  jFnäBan^ (erl. :  tuxiäk) dnp  rftk,  ctL:   ünSi  ^apel  'er  schläft  wach'.
•  g.  'zaeman-  n.  'Regsamkeit,  Munter-, Wachsein' :  ks  hvaph  c^afmmca  dät  'mäcä "wer  schuf  wohlwirkendSchlaf  und  Wachen" Y.  44. 5.
Zum  ai.  V.  MnlH  'incitat'.  —  Vgl.  *tainak; 'toimaii',  viaSäla-,  —  ai.  aiu-htaian-  Adj.  — Pü.:  imävxnälh,    eri.;  luxlSkih,    Sn.:  jägara-
•  j,  'zaeman-  Adj.  'regsam,  wach*:  •matiB F.  4  f.
Vgl.  ^xarmart:  —  Pü. ;  ttttävanä. g.  oMiinä  Y.  4/.  4:  s.  6ia-.
•  j.  zaeäa-  Adj.  'schauderhaft':  •/ff  F.  20. S.  auch  sminav;  sSiidiila:  —  Vfil.  mp.  (Pü.), np.  ujV«)  'schauderhaft',  got.  ingtiman  'er- *ebrecken';  IJtt.i  IF.  2.4,%,  GGA.  tSg6.  961, Hbm.  PSI.  70.  —  0  Das  freilich  auch  dem ai.  hffii-  entsprechen  könnte ;  vgl.  unter  zat- Sayamna:
•  ].,  g.  zaotar- ;  zaoSr-  m. 'Priester,  Ober- pricster';  y7  (näml.  zara'husirö)  *fä  a/ä tnzü/  .  .  kaya  (Sp.  46a  m.)  S.. 33.it;  be- nutzt Yt.  4.T.  yi  °ta  sarähustrS.  A)  im jAw.  Name  des  vornehmlich  mit  dem Vortrag  der  Gä'iäs  betrauten  Oberprie- sters, der  den  Gottesdienst  zusammen  mit sieben" Unterpriestem  (s.  'raiav-),  im  Not- fall aber  auch  allein  (s.  N.  Si,  Sp.  1653  ra.) vollzieht:    'lanm    asavanim    aiahe  ratäm
zaotar- A
1652
=== BRT zaemi search ===
```


## [2026-09-05T20:58:17.891Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== ISS_alt_DKS afzar/abzar ===\"; grep -n \"afzār\\|abzār\\|afzar\\|abzar\\|hasāra\\|haṣṣāra\" ISS_alt_DKS.txt | head -20\necho \"=== AHD ghaiso ===\"; grep -n -i \"ghaiso\\|gais\\|garlic\\|auger\" AHD_watkins1985.txt | head -20\necho \"=== KLN garlic/gaesum ===\"; grep -n -i \"garlic\\|gaesum\\|garfish\" KLN_1966.txt | head -20"
}
```


### [2026-09-05T20:58:18.014Z] TOOL RESULT

```
<persisted-output>
Output too large (39.1KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/blotyx230.txt

Preview (first 2KB):
=== ISS_alt_DKS afzar/abzar ===
=== AHD ghaiso ===
507:ghaiso-. A stick, spear. 1. Germanic *gaizaz in: a. Old English gar, spear: GORE}; (GARFISH), GARLIC; b. com- pound *nabé-gaizaz, tool for piercing wheel hubs (*nabd, hub; see nobh-); c. Old Norse geirr, spear (in geirfalki, gyrfalcon, akin to the source of Old French girfaut): GYRFALCON. 2. Germanic *gaizé in Old English gdra, corner, point of land: GORE?. [Pok. ghaiso- 410.]
510:*ghait-d in Greek khaité, long hair: CHAETA; (CHAETOG- NATH). [Pok. ghait-d- 410.] ghalgh-. Branch, rod. Germanic *galgon- in: a. Old English g(e)alga, cross, gallows: GALLOWS; b. Old North French gauge, gauge: GAUGE. [Pok. ghalgh- 411.] ghans-. Goose. 1. Germanic *gans- (nominative plural *gansiz) in: a. Old English gds (nominative plural gés), goose: GOOSE!; (GOSHAWK); b. Old Norse gas, goose, diminutive geslingr, gosling: GOSLING. 2. Germanic *ganr- in Old English ganra, gandra, gander: GANDER. 3. Germanic *gandton- in Old English ganot, gannet: GANNET. 4, Suffixed form *ghans-er- in Latin dnser (< *hanser), goose: ANSERINE; MERGANSER. 5. Basic form *ghans- in Greek khén, goose: CHENOPOD. [Pok. ghans- 412.) ghasto-. Rod, staff. 1. Variant form *ghazdh- in Ger- manic *gazdaz in: a. Old English gierd, gerd, staff, twig, measuring rod: YARD}; b. Old Norse gaddr, rod, goad, spike: GAD?. 2. Form “ghast-d- in Latin hasta, spear: HASLET, HASTATE. [Pok. 1. ghasto- 412.] ghé-. To release, let go; (in the middle voice) to be released, go. Contracted from *ghea-. 1. Germanic vari- ant form *gaian in Old English gdn, to go: GO; AGO, FOREGO!, FoRGO. 2. Suffixed form *ghé-ro- in Latin hérés, heir (? < “orphan” < “bereft”):; HEIR, HEREDITA- MENT, HEREDITY, HERITAGE; INHERIT. 3. Suffixed o-grade form *ghé-ro-, “empty space,” possibly in: a. Greek khéros, place, country, particular spot: CHO- ROGRAPHY; b. Greek denominative khorein, to move, go, spread about, make room for: -CHORE; ANCHORITE. 4. Perhaps suffixed zero-grade form *gha-l- in Greek khal
...
</persisted-output>
```


## [2026-09-05T20:58:38.948Z] TOOL CALL #17: Bash

```json
{
 "command": "pdftoppm -f 184 -l 184 -r 300 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg184 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render PDF page 184"
}
```


## [2026-09-05T20:58:39.827Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SYN 1384 (leaf 1408) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==1409' SYN.txt | head -50"
}
```


### [2026-09-05T20:58:41.858Z] TOOL RESULT

```
total 23412
drwx------ 2 sfmqrb sfmqrb    4096 Sep  5 16:58 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  5 16:02 ..
-rw-rw-r-- 1 sfmqrb sfmqrb   68775 Sep  5 16:43 ary440.png
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
-rw-rw-r-- 1 sfmqrb sfmqrb  100925 Sep  5 16:52 bqt_pdf600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   67648 Sep  5 16:29 build128.py
-rw-rw-r-- 1 sfmqrb sfmqrb  105345 Sep  5 16:30 build132.py
-rw-rw-r-- 1 sfmqrb sfmqrb   62948 Sep  5 16:36 build134.py
-rw-rw-r-- 1 sfmqrb sfmqrb   56126 Sep  5 16:29 build136b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   13830 Sep  5 16:22 build136.py
-rw-rw-r-- 1 sfmqrb sfmqrb   66341 Sep  5 16:28 build139.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53260 Sep  5 16:29 build142.py
-rw-rw-r-- 1 sfmqrb sfmqrb   76989 Sep  5 16:32 build145.py
-rw-rw-r-- 1 sfmqrb sfmqrb   50861 Sep  5 16:34 build148b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   21485 Sep  5 16:29 build148.py
-rw-rw-r-- 1 sfmqrb sfmqrb   17908 Sep  5 16:44 build151a.py
-rw-rw-r-- 1 sfmqrb sfmqrb   15986 Sep  5 16:46 build151b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   11172 Sep  5 16:47 build151c.py
-rw-rw-r-- 1 sfmqrb sfmqrb   19592 Sep  5 16:50 build151d.py
-rw-rw-r-- 1 sfmqrb sfmqrb    6433 Sep  5 16:50 build151z.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51529 Sep  5 16:51 build152.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51266 Sep  5 16:51 build154.py
-rw-rw-r-- 1 sfmqrb sfmqrb   61639 Sep  5 16:53 build155.py
-rw-rw-r-- 1 sfmqrb sfmqrb   70485 Sep  5 16:53 build156.py
-rw-rw-r-- 1 sfmqrb sfmqrb   72953 Sep  5 16:48 build158.py
-rw-rw-r-- 1 sfmqrb sfmqrb   74140 Sep  5 16:56 build160.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53286 Sep  5 16:55 build161.py
-rw-rw-r-- 1 sfmqrb sfmqrb   67253 Sep  5 16:56 build162.py
-rw-rw-r-- 1 sfmqrb sfmqrb   45662 Sep  5 16:49 build164.py
-rw-rw-r-- 1 sfmqrb sfmqrb   82221 Sep  5 16:56 build168.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53542 Sep  5 16:57 build169.py
-rw-rw-r-- 1 sfmqrb sfmqrb    7816 Sep  5 16:35 c_am2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   14765 Sep  5 16:35 c_am3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   10038 Sep  5 16:35 c_empty2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4123 Sep  5 16:34 crop_am.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4986 Sep  5 16:34 crop_arabic_refs.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7702 Sep  5 16:34 crop_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb   16978 Sep  5 16:34 crop_morocco.png
-rw-rw-r-- 1 sfmqrb sfmqrb  163996 Sep  5 16:46 gar2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  124975 Sep  5 16:47 gar3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77205 Sep  5 16:46 gar.png
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep  5 16:18 kent.txt
-rw-rw-r-- 1 sfmqrb sfmqrb     222 Sep  5 16:30 leaf.py
-rw-rw-r-- 1 sfmqrb sfmqrb   57617 Sep  5 16:20 mk129.py
-rw-rw-r-- 1 sfmqrb sfmqrb   74680 Sep  5 16:26 mk131.py
-rw-rw-r-- 1 sfmqrb sfmqrb   33365 Sep  5 16:25 mk133.py
-rw-rw-r-- 1 sfmqrb sfmqrb   42635 Sep  5 16:29 mk140.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51288 Sep  5 16:30 mk143.py
-rw-rw-r-- 1 sfmqrb sfmqrb   57696 Sep  5 16:46 mk153.py
-rw-rw-r-- 1 sfmqrb sfmqrb   49505 Sep  5 16:50 mk157.py
-rw-rw-r-- 1 sfmqrb sfmqrb   56703 Sep  5 16:54 mk166.py
-rw-rw-r-- 1 sfmqrb sfmqrb   61790 Sep  5 16:57 mk167.py
-rw-rw-r-- 1 sfmqrb sfmqrb   30384 Sep  5 16:51 mk170.py
-rw-rw-r-- 1 sfmqrb sfmqrb    4344 Sep  5 16:49 n12b.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3969 Sep  5 16:49 n12.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2692 Sep  5 16:49 n16.png
-rw-rw-r-- 1 sfmqrb sfmqrb   11831 Sep  5 16:32 node4.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7427 Sep  5 16:32 node7.png
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep  5 16:13 oldpers_djvu.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    6054 Sep  5 16:36 p152_e0left.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2672 Sep  5 16:36 p152_node2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   41788 Sep  5 16:53 p173_ital.png
-rw-rw-r-- 1 sfmqrb sfmqrb   32898 Sep  5 16:53 p173_op.png
-rw-rw-r-- 1 sfmqrb sfmqrb  671488 Sep  5 16:52 p600_350.png
-rw-rw-r-- 1 sfmqrb sfmqrb  139701 Sep  5 16:52 p600_foot2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  183909 Sep  5 16:52 p600_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1717 Sep  5 16:52 p600_head2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5162 Sep  5 16:52 p600_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1189 Sep  5 16:57 p600_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   22067 Sep  5 16:29 part0.json
-rw-rw-r-- 1 sfmqrb sfmqrb   14156 Sep  5 16:22 part1.json
-rw-rw-r-- 1 sfmqrb sfmqrb   17147 Sep  5 16:44 part_a.json
-rw-rw-r-- 1 sfmqrb sfmqrb   15703 Sep  5 16:46 part_b.json
-rw-rw-r-- 1 sfmqrb sfmqrb   10974 Sep  5 16:47 part_c.json
-rw-rw-r-- 1 sfmqrb sfmqrb   19420 Sep  5 16:50 part_d.json
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
-rw-rw-r-- 1 sfmqrb sfmqrb  131595 Sep  5 16:32 pg151_hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   96854 Sep  5 16:29 pg151.png
-rw-rw-r-- 1 sfmqrb sfmqrb  154426 Sep  5 16:36 pg152_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   62516 Sep  5 16:35 pg152.png
-rw-rw-r-- 1 sfmqrb sfmqrb   39131 Sep  5 16:28 pg153.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63033 Sep  5 16:30 pg154.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77057 Sep  5 16:32 pg155.png
-rw-rw-r-- 1 sfmqrb sfmqrb  101504 Sep  5 16:43 pg156.png
-rw-rw-r-- 1 sfmqrb sfmqrb  169880 Sep  5 16:34 pg158_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80624 Sep  5 16:34 pg158.png
-rw-rw-r-- 1 sfmqrb sfmqrb  124379 Sep  5 16:31 pg159_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   27814 Sep  5 16:31 pg159.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4694 Sep  5 16:31 pg159_word.png
-rw-rw-r-- 1 sfmqrb sfmqrb  168057 Sep  5 16:34 pg161_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   76745 Sep  5 16:34 pg161.png
-rw-rw-r-- 1 sfmqrb sfmqrb  110270 Sep  5 16:42 pg162_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb   76438 Sep  5 16:42 pg162.png
-rw-rw-r-- 1 sfmqrb sfmqrb    8523 Sep  5 16:42 pg162_verse.png
-rw-rw-r-- 1 sfmqrb sfmqrb   25911 Sep  5 16:32 pg163.png
-rw-rw-r-- 1 sfmqrb sfmqrb   59398 Sep  5 16:33 pg164.png
-rw-rw-r-- 1 sfmqrb sfmqrb   61265 Sep  5 16:40 pg165.png
-rw-rw-r-- 1 sfmqrb sfmqrb  116877 Sep  5 16:46 pg167.png
-rw-rw-r-- 1 sfmqrb sfmqrb   86005 Sep  5 16:39 pg168.png
-rw-rw-r-- 1 sfmqrb sfmqrb   68420 Sep  5 16:42 pg169.png
-rw-rw-r-- 1 sfmqrb sfmqrb   37351 Sep  5 16:44 pg170.png
-rw-rw-r-- 1 sfmqrb sfmqrb  120612 Sep  5 16:49 pg171_450.png
-rw-rw-r-- 1 sfmqrb sfmqrb   73551 Sep  5 16:43 pg171.png
-rw-rw-r-- 1 sfmqrb sfmqrb   73400 Sep  5 16:56 pg172.png
-rw-rw-r-- 1 sfmqrb sfmqrb   52970 Sep  5 16:53 pg173.png
-rw-rw-r-- 1 sfmqrb sfmqrb   54907 Sep  5 16:54 pg175.png
-rw-rw-r-- 1 sfmqrb sfmqrb   57139 Sep  5 16:54 pg179.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81598 Sep  5 16:58 pg180.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77310 Sep  5 16:58 pg184.png
-rw-rw-r-- 1 sfmqrb sfmqrb   44812 Sep  5 16:34 pg532.png
-rw-rw-r-- 1 sfmqrb sfmqrb  153161 Sep  5 16:34 pg532_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4868 Sep  5 16:14 prt.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  333088 Sep  5 16:16 sod135_c.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1817364 Sep  5 16:16 sod135.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  101641 Sep  5 16:15 sod136_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1892712 Sep  5 16:15 sod136.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  561602 Sep  5 16:57 t598.png
-rw-rw-r-- 1 sfmqrb sfmqrb  632359 Sep  5 16:57 t599.png
-rw-rw-r-- 1 sfmqrb sfmqrb  671488 Sep  5 16:57 t600.png
-rw-rw-r-- 1 sfmqrb sfmqrb  545905 Sep  5 16:57 t601.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1268 Sep  5 16:57 top598.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1268 Sep  5 16:57 top599.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1268 Sep  5 16:57 top600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1268 Sep  5 16:57 top601.png
-rw-rw-r-- 1 sfmqrb sfmqrb   24918 Sep  5 16:58 tops2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4812 Sep  5 16:57 tops.png
-rw-rw-r-- 1 sfmqrb sfmqrb   56398 Sep  5 16:26 write144.py
```


### [2026-09-05T20:58:43.461Z] TOOL RESULT

```
=== SYN 1384 (leaf 1408) ===
ased on such notions as ‘strength, power’(?), common ‘birth’, ‘customs’, or ‘language’, or are words for ‘country’ used also for its ‘people’.
1, TE *teuta-, prob. fr. the root in Skt. tu- ‘be strong’ (3sg. pres. tduti, taviti), Lat. tumére ‘swell’, totus ‘whole’, etc. Walde-P. 1.706 ff., 712. Feist 496. NED s.v. thede.
Ose. touto ‘populus’ (Bansae touto, T0FTO Mayepriwo; cf. toutico ‘publica’, ete.), Umbr. tota- ‘people’ (in this spe-
cial sense) or ‘state’ or ‘city’ (cf. e.g. seritu poplom totar Iiouinar ‘servato populum civitatis Iguvinae’); Ir. taath (W. tud ‘country’, older ‘people’, Br. tud ‘people’ = ‘persons’); Goth. piuda, ON )jod, OE péod, ME thede, OHG diot, MHG diet; Lith., Lett. tauta.
2. Grk. vos (ébvos attested by Hom. prosody), prob. : os ‘custom, usage’, Skt. svadha- ‘one’s own nature, custom, home’, derivs. of refl. stem *swo-. Cf. also Goth. sibja, OE sib(b), OHG sippa, etc. ‘relationship’. Walde- P. 2.456. Boisacq 218.
3. Lat. géns (in narrow sense ‘clan, family’, but freq. for ‘people, nation’; so also It. gente, but mostly as Fr. gens, etc. ‘people, persons’), fr. the root of gignere ‘beget, bear’, etc. (cf. Grk. -yevos ‘race, kin, clan’, etc.). Walde-P. 1.576 ff. Ernout-M. 416.
Lat. natid, orig. ‘birth’ : ndscz ‘be born’, ndius ‘born’, fr. the same root as gens. Hence It. nazione, Fr. nation (> ME nacioun, NE nation > NIv. nai- sittin), Sp. nacién, Rum. natiune, Dan., Sw., NHG nation, Du. natie, all with tendency to be used esp. as ‘nation’ in political sense.
4, Ir. tuath, above, 1.
Nir. muinntir, mostly ‘household, family, clan’ (19.23), now used also for a national group,
CC-O0. In Public Domain. Gurukul Kangri Collection, Haridwar
/ } } i | :
; 1316
W. cenedl (reg. word for a ‘people, na- tion’) : Ir. cenél ‘race, family’ : Ir. cinim ‘spring from’, ChSI. -éina, -ceti ‘begin’, etc. Walde-P. 1.398.
: Br. broad (now reg. = Fr. nation, for | which pobl in NT), deriv. of bro ‘coun- try’ (19.11).
i 5. Goth. piuda, OF péod, etc., above, 1. For other Gmc. words see 19.21.
6. Lith., Lett. tawta, above, 1. Lith tauta, now the accepted word, was
Digitized by Arya Samaj Foundation Chennai and eGangotri
SELECTED INDO-EUROPEAN SYNONYMS
known to Kurschat only as Tauta ‘Ober- land’; in his NT he used Zmoneés (cf. 19.21), as also Deutsch.-lit. Wtb. s.v. Volk; the Trowitz NT had giminé ‘family, race’.
7. ChSl. gezykt ‘tongue, language’ (18.24), reg. in Gospels for ¢6vos.
8. Skt. janapada- ‘country’ (19.11) and its ‘people’.
Av. dais#hu- ‘country’ (19.11) and its ‘people’. Barth. 706 ff.
19.28 TRIBE, CLAN, FAMILY (in Wide Sense)
Grk. giv, -yévos Goth. kuni Lith. gentis, kiltis, giminé NG guaAy ON kind, kyn, ett Lett. cilts, dzimta Lat. _tribus, géns Dan.  stamme, slegt, at ChSl. koléno, rodi, pleme It. tribic Sw. stam, slagt, att SCr. p
```


## [2026-09-05T20:58:51.328Z] TOOL CALL #19: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg184.png"
}
```


### [2026-09-05T20:58:51.343Z] TOOL RESULT

```
File does not exist. Note: your current working directory is /home/sfmqrb/git/rishe.
```


## [2026-09-05T20:58:53.518Z] TOOL CALL #20: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg184.png"
}
```


### [2026-09-05T20:58:54.055Z] TOOL RESULT

```

```


## [2026-09-05T20:58:54.053Z] INPUT

[Image: original 2550x3300, displayed at 1546x2000. Multiply coordinates by 1.65 to map to original image.]


## [2026-09-05T20:59:16.047Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN garlic ===\"; grep -n -o -i \".\\{0,300\\}garlic.\\{0,400\\}\" KLN_1966.txt | head -5\necho\necho \"=== KLN 666 area: gar- ===\"; grep -n -o -i \".\\{0,200\\}gaesum.\\{0,300\\}\" KLN_1966.txt | head -5"
}
```


## [2026-09-05T20:59:17.495Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AFA 216 (leaf 246) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==247' AFA.txt | head -40\necho \"=== AFA safina ===\"; grep -n -o -i \".\\{0,200\\}safina.\\{0,300\\}\" AFA.txt | head -10"
}
```


### [2026-09-05T20:59:22.100Z] TOOL RESULT

```
=== KLN garlic ===
ugrep: error: error at position 85
\xbf][\x80-\xbf]*){0,400}
                         \___exceeds complexity limits



=== KLN 666 area: gar- ===
ugrep: error: error at position 85
\xbf][\x80-\xbf]*){0,300}
                         \___exceeds complexity limits
```


### [2026-09-05T20:59:25.865Z] TOOL RESULT

```
=== AFA 216 (leaf 246) ===
""•'":*■,'*•"' ■" -• * : ■ . ^ - • ." . / •
. . - 216
scher" sind, war schon den alten Arabern nicht mehr
ganz klar. Es findet sich ausser Zaheir 10 1 6 noch Dir.
Had. 93« 38. Nur dem Arabischen gehört ^^ »SegeP*.
an (öanh. s. ▼. JJL:^)f wozu ich nar äthiop. gelä »Schleier"
(DiUmann 1140) stellen kann. ManygL re^m »Segel" dann
»Schleier".
Wenn man diese nicht geringe Anzahl im Arabischen selb-
ständig entwickelter Worter betrachtet, so kann man nicht
gut Yoraussetzen , dass die Schififahrt unter den alten Ara-
bern nur wenig entwickelt war. Das hindert aber natürlich
nicht, dass thatsachlich doch die nördlichen Araber mancherlei
Fahrzeuge und Schifisgerathe erst von ihren aramäischen
Nachbarn mit den Namen derselben entlehnt haben.
Zunächst ist RAaC Amrul]|:. 20, 4; Dir. Hu^. 18, 3
(H^SLÄ? ^Ik^) Zuheir 17, 7, 10, 6; Betari 92,3 a.f.;
131, 4 zu nennen, welches Guidi (Della aede p* 37) mit
Recht auf die Liste der yerdächtigen Wörter gebracht hat.
In der That sprechen alle Anzeichen dafilr , dass es ein über-
nommenes Wort sei. Vor allem hat es im Arabischen keine
Ableitung; die Wurzel /jaIi so weit sie im Arabischen
sich findet, ist ganz unecht, da das Yerbum denomina-
tir Ton ^JaJ ist; dies ist aber — bis jetzt noch uner-
kannt — nichts als persisch ^L^Jf »Wetzstein". Dasselbe
Wort ist als {JLOd auch in*s Syrische übergegangen. Gast.
716. Im Hebräischen hat das Wort eine bequeme Ablei-
tung Ton |£)D »täfeln", wie man auch im Arabischen Yon
den ^Ut Zuh. 1, 23 den Tafeln des Schiffes spricht.
(Auch syr. | i ^S ). Denkbar wäre übrigens auch, dass
ny fiD aramäisches Lehnwort ist , wofür ursprünglich dann
nyfi'S^ zu schreiben wäre. Denn auch Tfi2^ (woYon *3fi3^
Deut. 33, 19) scheint dazu zu gehören , da an einen Wechsel
mit |£)1( = yjiüo kaum zu denken ist. Wenigstens fehlen
4
i
=== AFA safina ===
ugrep: error: error at position 85
\xbf][\x80-\xbf]*){0,300}
                         \___exceeds complexity limits
```


## [2026-09-05T20:59:44.853Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FVQ leaf 188 (p171) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==189' FVQ.txt | head -50"
}
```


## [2026-09-05T20:59:45.619Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== DRM leaf 312 (t.1 p290) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==313' DRM.txt | head -50"
}
```


### [2026-09-05T20:59:46.786Z] TOOL RESULT

```
=== FVQ leaf 188 (p171) ===
```


### [2026-09-05T20:59:48.696Z] TOOL RESULT

```
=== DRM leaf 312 (t.1 p290) ===
  perse  hya . . ava  renversée  :   martiya  hya  draujana  ahatiy  avant  ufraçtam parça  «l’homme  qui  sera  menteur  (ou  infidèle,  rebelle),  punis le  sévèrement»  ( Beh .   IV,  38).
ê   d’imparfait.  —   3°  Il  sert  d’indice  k   l’imparfait  :   purçîdamê. je  demandais.
1   î,  prononciation  moderne  confondant  un  ancien  ê,  sorti  d’un  primitif ai  (dans  l’i  d’unité  ,   l’î  démonstratif  et  l’î  d’imparfait)  et  un  ancien  ( ,   sorti d’un  primitif  ya  (l’i  adjectival  et  peut-être  l'î  abstrait).
27  ô
Ici  encore  c’est  un  mot  indépendant,  il  représente  probable- ment un  ancien  adverbe  liadlia  (p.  71)  «continuellement,  tou- jours» et  a   le  sens  de  haine  dont  il  joue  le  rôle  (p.  214).
Dans  ces  trois  suffixes,  le  primitif  faisait  diphthongue  :   ai- va; ai-ta;  (hadfai)*hat.
§   223.  î   adjectival.  —   Il  forme  des  adjectifs  en  s'ajoutant
aux  substantifs.  E
xemples  :
Iran,
îrânî
LA,  iranien
shah,  roi,
shâhî
royal
khûn,  sang,
khûnî
sanguinaire
kcîr,  œuvre,
kcîrî
ouvrier  ;   guerrier
dam,  filet,
dâmî
chasseur
imrôz,  aujourd’h
ni,  imrôzî
d’aujourd’hui
arzcîii,  méritant,
arzânî
homme  de  bien.
Cet  î   est  le  reste  d’un  suffixe  pehlvi  îk,  de  la  même  façon que  a   est  le  débris  de  ak.
Au  persan  kârî  répond  le  pli.  kârîk  guerrier
»   tanî  tanîk  ym?,  corporel
»   arzânî  arzânîkyrè»,  méritant,  honnête.
Cf.  pli.  dînîk  5JfO,  religieux
afzûnîk  yn-^ty,  qui  produit  le  bien
tuvânîk  riche
dqrirîk  yr«y,  relatif  à   l’écriture.
Cet  î   a   pour  origine  le  suffixe  adjectival  ya.  Dans  la  plupart des  mots  qui  précèdent  le  suffixe  îk  a   été  ajouté  au  substantif indépendant  et  déjà  formé,  kûr,  tan,  dîn  etc.;  011  le  voit  à   l’état naissant  dans  le  pehlvi  kanîk  y»)},  jeune  fille,  du  zend  kanya 1   : l’analogie  se  développe  par  les  noms  de  peuple  en  iya  :   Arminiya, Uvajiya,  Bâbiruviya,  Uvcîrazmiya,  qui  devinrent  *Arminiyaka, *   Uvajiyaka  etc.
```


## [2026-09-05T20:59:55.865Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== DRM zinjir/zindan ===\"; grep -n \"zinjîr\\|zinjir\\|zindân\\|zindan\\|zenjîr\\|zaêna\" DRM.txt | head -20"
}
```


### [2026-09-05T20:59:55.909Z] TOOL RESULT

```
=== DRM zinjir/zindan ===
6403:3.  Cf.  à<sr  ;   zinja  et  zinjîr ,   chaînes;  mais  l’étymologie  de  ces
```


## [2026-09-05T20:59:56.689Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FVQ safina ===\"; grep -n \"safīna\\|safina\\|Safīna\\|sáfina\\|safinah\" FVQ_pages.txt FVQ.txt | head -20"
}
```


### [2026-09-05T20:59:56.742Z] TOOL RESULT

```
=== FVQ safina ===
```


## [2026-09-05T21:00:00.336Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '6370,6415p' DRM.txt\necho \"--- which leaf is line 6403? ---\"\nawk 'NR<=6403{n+=gsub(/\\f/,\"\")} END{print \"formfeeds before:\",n}' DRM.txt"
}
```


### [2026-09-05T21:00:02.086Z] TOOL RESULT

```
§§  24-2 — 253.  —   A.  Suffixes  nominaux  sortis  de  composés anciens.
!e  sont  les  suffixes  bad
bar
bail
dân
o'J
kâr  kar
/P
1.  Namûz  çyÇ)  vient  de  *uamû <•,  dérivé  de  *nama  (zend  nemem,  Yt.  I,  ‘21), formation  parallèle  à   nemô  (sscr.  namas).
289
vâr  âvar  ,*l  ,U yâr  yiîd  >b  ^b gûn  0?S
çtcîn
çâr  jbo
dêç
§   243.  bad.  —   Le  suffixe  -ôar/  jo  dérive  du  perse  -pati, maître,  pehlvi  pat  ?ei.
Pati  s’emploie  souvent  en  zend  comme  dernier  terme  de composé,  pour  marquer  les  titres  de  commandement  :
aêthrapaiti,  maître  du  foyer  1   (nom  du  prêtre  du  feu)
zantu-paiti,  »   de  la  ville
vîç-paiti,  »   du  village
nmânô-paiti,  »   de  la  maison
dahyu-paiti,  »   de  la  province
shôitlira-paiti,  »   du  pays.
aêthra-paiti  devient  le  phi.  êr-pat ,   p.  liêrbed  zantu-
paiti,  vîç-paiti,  nmânô-paiti  deviennent  le  phi.  zand-pat  vîç- pat  mânpat
Le  perse  avait  :
*magupati,  chef  des  mages  ;   d’où  magûpat,  p.  maubad *çpâda-pati,  chef  d’armée;  çprîhpat,  p.  çipâhbad  josb-^o.
On  trouve  encore  en  persan  :
kuhbad  ermite  ;   litt.  maître  de  la  montagne
bârbad  jo^b,  maître  des  cérémonies;  »   maître  de  la  cour.
§   244.  bar.  —   Le  suffixe  bar  s’ajoute  aux  noms  de  lieu, en  général  aux  noms  de  pays  maritimes.  C’est  le  mot  zend  para, côte  (cf.  dûraêpâra,  la  terre  aux  rives  lointaines)2  : hindu-bâr^jJjb,  le  pays  d’Inde,  l’Hindoustan.
Zang-bâr  ^bJbj,  le  pays  des  Zang  (côte  orientale  d’Afrique). daryâ-bâr  ,bb,j,  pays  maritime. nîd-bâr  ^b^,  région  fluviale. jûi-bâr  pays  de  rivières 3.
1.  Voir  p.  92,  n.  2.
2.  De  là  aussi  le  nom  de  la  côte  de  Malabar  ,bx_Lo  (la  côte  du  Malaya  : Malaya-pâ  ra) .
3.  Cf.  à<sr  ;   zinja  et  zinjîr ,   chaînes;  mais  l’étymologie  de  ces
19
290
Il  s’agit  toujours,  on  le  voit,  de  pays  où  l’on  aborde  par  les côtes;  de  la  l’emploi  dépara.
Il  ne  faut  pas  confondre  ce  suffixe  bar  —   para  avec  le  suffixe bar  marquant  itération  et  qui  est  le  sanscrit  vâra,  fois.  Bar ,   fois, est  un  mot  encore  indépendant  (p.  154)  : bârî  une  fois
bârliâ  l*>^b,  des  fois.
§   245.  bân.  —   Le  suffixe  bân,  ph.  pan  re),  forme  les  noms de  gardien  ;   il  vient  du  mot  pana  (zend  et  sscr.),  ce  qui  garde  : (   zend  râno-pâna,  ce  qui  garde  les  jambes,  caleçon  : i   ph.  rân-pân  rüA
ph.  pdç-pdn  rei*uei,  gardien.  p.  ^U^ob
marz-pdn  gardien  des  frontières.  cMjj*
çtôr-pân  rAs0-”,  gardien  des  bêtes  de  somme  (*çtaora-pâna). zînddn-pân  püwA,  gardien  de  la  prison.
gnv-pân  reiA,  armure  protégeant  le  cou(*  grîva-pâna)^\^jS.
Il  semble  avoir  pris  une  existence  indépendante  en  se  dé- tachant des  composés  sous  la  forme  affaiblie  du  suffixe  :   Fir- dousi  a   bâni  çuvdrdn  ^b,  le  chef  des  cavaliers,  et  de  là
viendrait  le  féminin  bânû  ÿb,  dame,  maîtresse.  Les  Persans, du  moins,  expliquent  ces  mots  bân  et  bânû  comme  identiques  au suffixe  bân.  Mais  il  est  permis  de  douter  de  l’exactitude  de  ce rapprochement  :   bânû  paraît  déjà  en  pelilvi  (sous  la  forme  bânûk yrj)  :   or,  le  suffixe  bân  est  encore  pân  en  pelilvi  et  il  serait étrange  que  le  même  p ,   initial,  se  fût  affaibli,  et  médial,  se maintînt  encore.
--- which leaf is line 6403? ---
formfeeds before: 329
```


## [2026-09-05T21:00:03.000Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"sakīnah\\|sijjīl\\|sirāj\" FVQ_pages.txt | head -5\necho \"--- pdf page tags near ---\"; grep -n \"pdf page 18[5-9]\\|pdf page 19[0-5]\" FVQ_pages.txt | head\necho \"--- search arabic safina script ---\"; grep -n \"سفينة\" FVQ_pages.txt AFM_pages.txt TAD_pages.txt ARB_mo3rb.txt 2>/dev/null | head -20"
}
```


### [2026-09-05T21:00:03.077Z] TOOL RESULT

```
--- pdf page tags near ---
--- search arabic safina script ---
TAD_pages.txt:314:‫بارجة ‪ -‬ايطالي هنهعه‪ 1:‬وهو اسمطائر ماي سميت تلك السفينة باسمه‬
TAD_pages.txt:1120:             ‫مه الت ف اراي د دّفا © أيلوح مرادفه كاز السفينة‬
TAD_pages.txt:1451:                     ‫يطلق على سفينة صخيرة سميت به لصغرها مرادفه _سبارة‬
TAD_pages.txt:1555: ‫‪#‬حتور ونخت ع‪-‬ابي انكليزى ‪60‬لا ( بلفظ بدت ) وهو سفينة صغيرة‬
TAD_pages.txt:2138: ‫ايطالي مطةالمةن معناه فى الاصل رئيس مرادقه ناك السفينة‬            ‫قبطان ف‬
TAD_pages.txt:2309:                                     ‫ويدبر السفينة مرادفه أمير وإمام وقائد وريّان‬
TAD_pages.txt:2665: ‫‪:6‬ن التي فى الاصل معناها سفينة صغيرة ‪ .‬فتوضع‬
TAD_pages.txt:2742:              ‫معثاه عر الركن وجعل السفينة‬         ‫تاولون‪ -‬بوناني ‪00‬‬
AFM_pages.txt:667:0 السفينة : ܘܕܦ طويل تدقع ب الى الساحل معرب بيله
AFM_pages.txt:1952:الدردور اذا وقعت فيه السفينة فلا نحاة للها منة
ARB_mo3rb.txt:3944:فرغ 5 | الرصاص المذاب »© فتصير كصخرة إذا رست رست السفينة 6 معرب لت » ٠‏ 
ARB_mo3rb.txt:5796:(4) فى © « معروف » وهوشطأ ٠‏ والبيت فى ديوانة (ص 5 ٠ )١‏ و« قص البحربالسفينة » : 
ARB_mo3rb.txt:12494:© السكان » بم السين وتشديذ الكاف ©6 وهو ذلب السفينة الى به تعصدل 6 وهوعينى‎ « 68 
ARB_mo3rb.txt:12503:فهذا أصل المادة» لأن ريات السفينة رئيسها وأول من فها ٠‏ 
ARB_mo3rb.txt:13933:حِ اشتيام ام السفينة لخر 6 17 3 الملّاحين ٠‏ وقال 7 5 “السباجة»» : 
ARB_mo3rb.txt:17739:(1) فى ب «تمر السفينة» وهو مخااف للنسم المخطوطة واللسان ٠‏ 
ARB_mo3rb.txt:23937:(5) ف القاموس : « النبج : الروى يجعل بين لوحين من ألواح السفينة » ٠‏ 
ARB_mo3rb.txt:33508:يز السفينة 8:99٠‏
```


## [2026-09-05T21:00:16.509Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"pdf page 188\\|pdf page 189\" FVQ_pages.txt | head\necho \"--- print region ---\"\nawk '/\\[pdf page 188\\]/,/\\[pdf page 190\\]/' FVQ_pages.txt | head -60"
}
```


### [2026-09-05T21:00:18.400Z] TOOL RESULT

```
--- print region ---
```


## [2026-09-05T21:00:18.913Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"pdf page\" incoming/PLA/PLA_pages.txt | head -3\necho \"--- PLA safina ---\"; grep -n \"safīna\\|safina\\|Safīna\\|safīnat\" incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head -20\necho \"--- PLA zin/apsan ---\"; grep -n \"apsān\\|apsan\\|safan\" incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head -20"
}
```


### [2026-09-05T21:00:18.991Z] TOOL RESULT

```
--- PLA safina ---
12092:slau - safä’in: Pl. Veasso» saflna s. safina. 
12154:owe- safan: Pl. v. au, safina. 
12159:Ge» - safin: Pl. v. alu safina q. v. 
12162:ua - safina: "Schiff, Fahrzeug" pers. lust apsän durch syr. Vermittlung 
--- PLA zin/apsan ---
11709:A ssuupun — safanasfüya = sabandbüya gG. v. 
12154:owe- safan: Pl. v. au, safina.
```


## [2026-09-05T21:00:23.724Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '12150,12180p' incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt\necho \"=== find printed page 162 in PLA_pages ===\"\ngrep -n \"162\" incoming/PLA/PLA_pages.txt | head -5\nhead -3 incoming/PLA/PLA_pages.txt"
}
```


### [2026-09-05T21:00:23.796Z] TOOL RESULT

```
6 
Au - safat = safad Q Ve. 


owe- safan: Pl. v. au, safina. 

Oz - sufün: Pl. v. au. saflna. 

ala - saffiän: "Ziegenleder" = sahtiyän q. v. 
Ge» - safin: Pl. v. alu safina q. v. 


ua - safina: "Schiff, Fahrzeug" pers. lust apsän durch syr. Vermittlung 
Kaas mand. spinta, hebr. nr» . 


M. E. ist es eine Metathese v. pers.o# i äb-zIn "Wasserausrüstung". 
“ 9 
ze» sagar: "Rad! = zagar s. zagar . 
gen - akäbif: Pl. v. EU sakbäg g. v. 


u - akärig: Pl. vo sukurrußa s. sukurrußa. 


1. Muhit s. v., al-Mu’arrab s. v. 
2. Brockelmann s. v. 

3. Fremdwörterbuch Ss. v. 

4. Wahrmund s. V. 
=== find printed page 162 in PLA_pages ===
9188:safsir?                                                                                     162                                                           sakäri$
             Asya Asbaghi
```


## [2026-09-05T21:00:33.257Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"safina\\|saflna\" incoming/PLA/PLA_pages.txt | head\necho \"--- surrounding page headers ---\"\nawk 'NR>9100 && NR<9260 && /^ *[a-zA-Zš?]+ +1[0-9][0-9] +/' incoming/PLA/PLA_pages.txt | head"
}
```


### [2026-09-05T21:00:34.968Z] TOOL RESULT

```
9151:slau - safä’in:                              Pl.    Veasso» saflna                   s.    safina.
9204:owe- safan:                            Pl.        v.         au,        safina.
9206:Oz - sufün:                                Pl.         v.       au. saflna.
9211:Ge» - safin:                               Pl.         v. alu           safina q. v.
9213:ua - safina:                                     "Schiff,             Fahrzeug"                   pers.             lust apsän        durch    syr.       Vermittlung
--- surrounding page headers ---
```


## [2026-09-05T21:00:42.801Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v2: locate page 1054/1055 ===\"\ngrep -n \"١٠٥٤\\|١٠٥٥\\|1054\\|1055\" BQT_v2_pages.txt | head -20\necho \"=== zinhar ===\"; grep -n \"زینهار\\|زنهار\" BQT_v2_pages.txt | head -10\necho \"=== zin ===\"; grep -n \"آبزن\\|اپسان\\|افسان\" BQT_v1_pages.txt BQT_v2_pages.txt | head -10"
}
```


### [2026-09-05T21:00:42.886Z] TOOL RESULT

```
=== BQT v2: locate page 1054/1055 ===
=== zinhar ===
7929:                                     ‫«چیت‌آن ‏‪ ٩۲...‬آغاز گردد (ترکب‌کلمه باضمیر» رك‪ :‬زینهار)‪:‬‬
29934:  ‫‪ - ۱‬درمقام تحذیر ‪:‬زنههار تابدین طمع گرد‬                        ‫‪ 3‬زنهار» («‪.‬م‪).‬‬       ‫مضفف‬      ‫‪۵‬‬
30811:                             ‫بر روی خمیر نان پاشند‪.‬‬      ‫زنهار ‪ ۴‬است که بناه‬         ‫ربنهار ‪۳‬‬
=== zin ===
BQT_v1_pages.txt:1697:نه‌شهنامه»در بای‌ژرف!ست‌این نه افسانه» ند شگرف است این
BQT_v1_pages.txt:7784:ادبیات اسلامی ضحاكشده . در ودا افسانةٌ تراع مصهانعع1 با مار سه سرآمده وهمن دانان حد
BQT_v1_pages.txt:13112:افسان بروزن ترسان . آهنی‌وسنگی
BQT_v1_pages.txt:14415:هه درصفحةٌ ۱۷۶اگارده است که افسانه و سر گذشت باشد .
BQT_v2_pages.txt:27049:      ‫‪ -۴‬این‌افسانه‌مر‌بوط بذرآباد مهراسپندان موبد موبدان ومفسراوستامعاصر‬                  ‫‪ ۱‬افشانه؛‬
```


## [2026-09-05T21:00:48.335Z] TOOL CALL #34: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:1054 2>&1 | head -60"
}
```


### [2026-09-05T21:00:50.005Z] TOOL RESULT

```
no scan of BQT covers printed page 1054 (see 'scans' in refs_online.json)
```


## [2026-09-05T21:00:54.270Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"pdf page\" BQT_v2_pages.txt | head -3\ngrep -c \"pdf page\" BQT_v2_pages.txt\necho \"--- tail tag ---\"; grep -n \"pdf page\" BQT_v2_pages.txt | tail -3\npython3 - <<'EOF'\nimport re\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\n# find printed page numbers in persian digits near page starts\nprint(len(t))\nEOF"
}
```


### [2026-09-05T21:00:56.000Z] TOOL RESULT

```
0
--- tail tag ---
2900526
```


## [2026-09-05T21:01:05.810Z] TOOL CALL #36: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nprint(json.dumps(d['BQT'],ensure_ascii=False,indent=1))\" | head -60"
}
```


### [2026-09-05T21:01:07.789Z] TOOL RESULT

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
 "notes": "Persian OCR is mediocre: headwords and Mo'in's footnotes (e.g. '۱ - رك: ابر کوه', Pahlavi/Avestan Latin forms) are mostly readable but with many character errors; search with short substrings and tolerate errors. BQT_v1_pages.txt was built from the djvu.xml; BQT_v2_pages.txt from pdftotext -layout of the _text.pdf. Volumes 3–5 (roughly ح/خ–ی and the تعلیقات volume) are not online in full text; for those use Dehkhoda quotations of Borhan/Mo'in via vajehyab/abadis/parsi.wiki, or page images on noorlib (different edition). | Vols 3-5 scans (image only) in incoming/BQT; vols 1-2 have OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt. Offsets verified by eye at several pages (v3 drifts by ~4 pages; page_map gives exact positions once built). || UPDATE: vols 3-5 now downloaded (image-only PDFs, verified as Mo'in's edition from title pages and the Latin footnotes) and OCRed locally. Image-only scan OCRed locally with tesseract 5 (fas.traineddata from github.com/tesseract-ocr/tessdata_fast, stored in incoming/_tessdata). *_pages.txt = 'fas' model (best for Persian); *_pages_faseng.txt = 'fas+eng' model (better for the Latin-script Pahlavi/Avestan etyma, worse for Persian). Pages separated by \\f; leaf N = N-th \\f-block 0-based = PDF page N+1. Search with short substrings and tolerate OCR errors. Provenance caveat: picofile is a general file host, the uploads are not from a library; treat as a grey copy (the book is in copyright in Iran). | vol 4 (م–ی) OCR text, tesseract fas+eng, pages tagged [pdf page N], printed = pdf+1917 | vol 5 (ta'liqat) OCR text, printed = pdf-5 | vol 3 (ش–ل) OCR text (689/721 pages), printed ≈ pdf+1203..1209 | BQT_v2_pages.txt: printed page = leaf + 540 (verified by catch-lines at pp. 838-855, 869, 904); earlier estimate +543 was 3 pages off.",
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


## [2026-09-05T21:01:13.691Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(\"leaves:\",len(t))\nfor i in (513,514,515,516):\n    print(\"======== leaf\",i,\"printed ~\",i+540)\n    print(t[i][:2500])\nEOF"
}
```


### [2026-09-05T21:01:15.483Z] TOOL RESULT

```
leaves: 684
======== leaf 513 printed ~ 1053
     ‫زبرزبان گفتن‬
                                                                                                                ‫تب ای ‪ ۵‬ات‬




     ‫زرا ‪ ۴‬بکر اولوثاك بالف کشبده‪.‬‬                                  ‫لفظ فارسی است‌یا عربی ‪ -‬وبا جیم فارسی‌بمعنی‬
                        ‫‪.‬‬    ‫ازبر ای آن و آزین جهت‬       ‫سی‬         ‫بیرون آوردن و بیرون کشیدن باشد ‪ -‬و خوش‬
                                                                    ‫وچايك وجلد وخوش وضع را نگیوزبند ‪-‬ونومی‬
     ‫کنابه اززبون بودن‬           ‫زير از میانه =‬
                                                                    ‫از انگور بقایت خوش لذت باشد ‪ -‬وبمعنی لاغ‬
                                       ‫و بد بودن باشد ‪.‬‬
                                                                    ‫وم‌خر ‪ 3۳‬همآمده است ‪ -‬وزهوار کفش وموزه‬
     ‫شیر افکن ‪.‬‬             ‫وبزرن‬
                                ‫زیرافکی * =‬                         ‫را هم میگوبند ‪ -‬و ربه‌انهاییکه استادان نقش‬
     ‫ووشك و آنچه در زیر افکنده‬
                             ‫بمعنی نهالی ت‬                                              ‫ند لش جامها را بدان نندلد‪.‬‬

                                                  ‫خوالند ‪.‬‬          ‫ر بجك = باجیم فارسی بروزن ميخك"‬
                                                                    ‫رگوودسفند راگونندکهبگاوشت وبرنج‌ودیگر‬
     ‫زير افکند * = بسکون‌نون ودالابجد‪.‬‬
                                                                ‫باشند و بگذارند تا خشك شود‬                     ‫دره‬
                                                                                                                 ‫رپ‬‫کالح‬
                                                                                                                      ‫مص‬
     ‫بممنی زبر افکن است کهنهوالتیوشك و آله‬                          ‫و در زمستان بپزند وبخورند ؛ ویعطی گوبندرور‪:‬‬
     ‫در زبرافکنده باشد ‪ -‬و نام مقامی‌است ازموسیقی‬
                              ‫کنرچك است ‪.‬‬  ‫که آ‬
                                                                    ‫بر شیر خواره است که آلرا پاکیزه کنند و در‬
                                                                    ‫هم بیچند مالند نارئجی و چندی از آن را بر‬
     ‫در بر = بضم بای ایجد (‪ )۱‬وسکون‬                                 ‫فقرا‬          ‫ان‬
                                                                                   ‫بارا‬
                                                                                      ‫بندرو
======== leaf 514 printed ~ 1054
 ‫ات‬        ‫او‬                                                                              ‫زیرفون‬
‫بکهد‌یگرباشرت کنند ‪ -‬کونایه ازخطاهم‌هست‪.‬‬          ‫زیر فون ‪ = ۱‬بافا بروزن‌یلگون‪ ,‬لوعی‬
‫زیر وزاده با زای هطه دار (‪ )۱‬بر‬                    ‫از درخت سنجد است وآنرا لمر ومیوه لمیباشد‬
‫رزن کیرودار‪ .‬کنابه ازآو ازحز بن وآهسته‌باشد‪9 .‬‬      ‫سرد وخشك است ودر‬          ‫د‪.‬‬
                                                                               ‫ومشق‬
                                                                                  ‫شر د‬
                                                                                     ‫یر د‬
                                                                                        ‫مپشت‬
                                                                                           ‫و‬
                                                                                   ‫قابات بکار برند‪.‬‬
‫زریرہبا؟ » با بای ابجد (‪ )۲‬بر وزن‬
‫دیدسا * آشی راگوبند که باگودت مرغ فربه‬
                                                   ‫زقيران ‪ -‬بفااف بر وزن شیرخان ‪,‬‬
‫و زره وسر که پزند ‪ .‬منطو بر‪ ۱‬نافع است سنی‬
                                                                ‫عم ماهی است ازماههای ملکی؟ ‪.‬‬
                             ‫شکم بزرکه را ‪۰‬‬
                                                    ‫زیر لكه برومزينرك » داناحوکیم‬
                                                    ‫رفعیم ومدرك و صاحب هوش باشد ‪ - ۴‬و بمعنی‬
                                                                         ‫فولاد جوحردار نز گفته‌اند ‪:‬‬
           ‫کراوبا (‪)e‬‏ وزنان ونان خواه گوند‪.‬‬
                                                    ‫زیر لاه = بائالیمجهول بروزن‌یشگاه‪,‬‬
‫دیز = بااول مکسور بثالی رسیده وزای‬                             ‫بععنی کرسی باشد که برآن شینند‪.‬‬
                  ‫قطه دار زده ‪ ,‬ریز های برف‬        ‫بالف‬       ‫ه‬
                                                              ‫طیی‬
                                                                ‫شسین‬
                                                                   ‫با‬          ‫زر لك سار‬
                 ‫وبرف ریزهایی‌باشد که از حوا‬       ‫کشده وبرای بی‌نقطة زده » خداوند اراك وفهم‬
                  ‫بهنگام سرما بارد اورآا بعربی‬                                         ‫وشمور باشد ‪.‬‬
                  ‫سقیطه گوند ‪ -‬و جالوری هم‬         ‫دار لب گفتن ‏ بمعنی زبرزبان‌گفتن‬
                  ‫هت کوچکتر از ملخ و شبها‬           ‫است هککن
======== leaf 515 printed ~ 1055
                                                                                                      ‫سای ها‬

‫زیگه ‪ -‬بکر اول وسکون ثالی‌وکاف‬                                   ‫دی » بکر اوولسکون ثالی غوین‬
 ‫فارسی ‪ ۰‬تارهابی باشد که استادان هش بندهس‬                         ‫عونی‬ ‫بشدم‪-‬‬
                                                                           ‫نقطه‌دار ‪ ۰‬نوعی افزرش وباط با‬
‫جامهابیکه بافند بدان بندله ‪ - ۷‬و کتاییکه‬                         ‫جمعیت خاطروشاط دل وفراغت هم‌هست‪-‬وحصیر‬
‫منجمان احوال واوضاع نجوم وافلاك را اجدزاول‬                       ‫وبوربابیرا یز گوبند که ازدوخ بافند ‪ » ۱‬ودوج‬
‫آن مملوم کنند و همجنان که آن فانونی است‬                     ‫علفی است که بدان الگور وخریزه آونگ کنند‬
‫جامه‌بافالرا در بافتن نقشهای‌جامه‪ .‬ان کتاب یز‬               ‫‪ -‬وبفتح اول درعربی‌بمعنی شك وربب ومیل از‬
‫دستوری است منجمالرا درشناختن‌احوال واوضاع‬                                                     ‫حق بباطل باشد ‪۴‬‬
‫فلکی ‏ وحمچنانکه کیفیات قوش جامها ازآن‬                       ‫ریغال » با ین شطه‌دار بروزن قفا ؛‬
‫تارها بیدا میشوده کمیات و حرکات کوا کب از‬
‫جدولهای ابنکتاب ظاهر میگردد " وممرب آن‬                           ‫لگ = بروزن قیف » زفت را گوبند‪.‬‬
                                                                                              ‫ز‬
 ‫زج است ‪ - ۸‬ونام جانوری هم حت حفیرجته‬                            ‫و آن صمغی باشد سیاهکه بکرچسلران‌چبانند‬
‫و خاکتری رن کوچکتراز کنجشك و زبرهر‬                               ‫بمعنی گناه ‪ -‬و بی ادبی هم هت ‪ - ۴‬ودر‬         ‫و‬
 ‫دوبال اوسرخ است وآواز او بفایت خوش‌وحزین‬                                          ‫عربی زر قلب نا سره باشد ©‬
‫میباشد ‪٩‬‏ ‪ -‬ونام طابفه‌است‌از کردان کهدر کوه‬
                                                             ‫رنهصنون ‪ = ۱‬بافا ونون بروزن قير گون»‬
                                     ‫کیلوبه توطن دارند‪.‬‬          ‫میخواستند‬    ‫را درآن شهر‬    ‫ا‬‫اس تت که‬     ‫رت‬
 ‫ربکا ت ت با ثانی مجهول وکاف‌بروزن‬

                ‫طبل زن را نشانند بر رود نواز ‪.‬‬                   ‫‪ ۱‬ز‪-‬یغ بافان‌را با وشی بافان ننهند‬
  ‫‪۰‬‬    ‫فرس‪۱۳۲۰‬‬         ‫«لفت‬     ‫ابوالعبای‪.‬‬



  ‫‪( - ۴‬عر) « زیم بفتح‌اولمیل کردن‌ومیل کردن بوی یستی‌وشك ومیل کردن ازحق »‬
                                                                  ‫مدنتهی الارب > ‪.‬‬
          ‫بکف برنهاده به زیغال ‏‬               ‫اشله‬
                                                  ‫لب‬‫ز‬       ‫بشکنان کههمی‬           ‫غلهال‬
                                               
======== leaf 516 printed ~ 1056
  ‫==‬                                                                                                 ‫زیگر‬
                                    ‫جبگاوید ‪#.‬‬              ‫زیا ‪ ۰‬بلغت زلد ویازید(‪ ۰ )۱‬ناد را گویندویعریی‬



‫زین‌افز ار ‪ - ۴‬سلیح و کجیم را‬
                                                                                                ‫رح خوانند ‪.‬‬

                                                            ‫ریگر = بر وزن دیگی » بممنی آپوق‬
                                       ‫روز جنگ ‪.‬‬            ‫است» وآن دست زدن باشد بردهان پرباد کرد‬
                                                                   ‫شخصی تا آن باد ازدهان او باصدا بجېد‪.‬‬
‫اين‬       ‫منن»ی‬
              ‫ميزا‬
                 ‫بن م‬
                    ‫رینان » بر وز‬
‫وزان راهم گونند‬        ‫حماعت ر از انا ماشد ‪۵‬‬                 ‫ه ‪۰‬بکر اوولل و ونانانی مجهول‬   ‫دیلو ‪۱‬‬
                                                            ‫بروزن لیکو » پلاس و کلیم را کوبند و آنرا‬
                                ‫خمتر نان باشند ‪۰‬‬               ‫ند ؛ و بفتح اول آهممده‌است‬ ‫نیز‬
                                                                                            ‫این‬
                                                                                              ‫خرولج‬
                                                                                                  ‫شط‬
 ‫زین برگاو نهادن = کنابه ازروان‬                              ‫زیلوچه ‪ ۴‬پلای وکلیم کوچثرا‬
                                  ‫د‪.‬‬
                                   ‫شفتن‬
                                      ‫بناو ر‬
                                           ‫شد‬                ‫کوبند همچو بوق وبوفچه وصندوق وصندوقچه‬
‫وده ‪ ۰ ۱‬با کاف بروزن لیم‬
                       ‫زکین‬                                                             ‫و امثال آن ‪.‬‬
 ‫سوده » فریوی زین اسب راکوبند» وآن بلندی‬                     ‫=فتح اول و مضمیم بورزن‬
                                                                                  ‫یمله پ‬
                                   ‫پیش زین باشد‪.‬‬             ‫زیگله ک‪.‬جاوه ماندی‌باشد کهپراز میوم‌وسیزی‬
                                                             ‫و امثال آن کنند وبر بشت چارو! بندند وازجایی‬
                                                                                              ‫بجایی بنرد‪.‬‬
‫ولپور هاء بمعنی زین کوده است که قرپوی زین‬
                                       ‫اس باشد ‪.‬‬             ‫زیمور ‪ = ۴‬بکر
```


## [2026-09-05T21:01:32.102Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(t):\n    if 'زنهار' in p or 'زینهار' in p:\n        print(\"leaf\",i,\"printed ~\",i+540)\nEOF"
}
```


### [2026-09-05T21:01:53.414Z] TOOL RESULT

```
leaf 135 printed ~ 675
leaf 503 printed ~ 1043
leaf 517 printed ~ 1057
```


## [2026-09-05T21:01:56.348Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (517,):\n    print(\"======== leaf\",i,\"printed ~\",i+540)\n    print(t[i][:3000])\nEOF"
}
```


### [2026-09-05T21:01:58.033Z] TOOL RESULT

```
======== leaf 517 printed ~ 1057
  ‫زين‬                                                                                              ‫‪۵‬‬
                                                                                                   ‫ت‬ ‫یی‬
                                                                                                      ‫ا‬


                             ‫بر روی خمیر نان پاشند‪.‬‬      ‫زنهار ‪ ۴‬است که بناه‬         ‫ربنهار ‪۳‬‬
‫رلو ار » با نالی مجهولبروزن دیوار ‪.‬‬                         ‫ویمان‬
                                                                ‫جستن و امان خواستن باشد ‪ -‬و عهد پ‬
       ‫معنی سوبت وماوی بودن وبرابری باشد‪.‬‬                   ‫‪ -‬و تری‌وبيم ‪ -‬و شکایت را لکیوزیند ‪-‬وبمعنی‬
 ‫هه‬              ‫بگر‬     ‫ی‬         ‫‪۷‬‬        ‫ی‬                 ‫هآی‬ ‫او‬‫گعجل‬
                                                                       ‫افوس و حسرت ‪ -‬وامات ‪ -‬وت‬
‫بمعنی(ژ شت‬            ‫' = بروزن ده‬     ‫لو‬
                                        ‫زر‬
                                                                                          ‫لیزآمده است ؟ ‪.‬‬
‫و آرایش باشد ‪ -‬و آنچه بدان زبنت و آرایش‬
                                                            ‫ر بنهاری = یناه آورنده ‪ -‬ویناه داده‬

‫لرین = بفتح اول بورزن زمین ؛ بلغت‬                           ‫‪-‬در عوهادمان کی در‬
                                                                             ‫شده ‪ -‬وعهد بسته ‪ ۴‬و‬
                                                                                      ‫‪.‬‬   ‫آمدن را گو شد ‪۵‬‬
‫زد وپازند (‪ )۱‬بمعنی دراز وبلند باشد که‌نقیض‬
        ‫وور کا‬                                   ‫کا‬         ‫ز)نیان ‪ - ۱‬بابای‌حطی بروزن‌میهمان‪,‬‬
                                                         ‫زینان امت که الخواه باشد‪ .‬وآن نخمی‌است که‬




                                                                        ‫(‪ )۱‬چك ‪ :‬ژند وپاژند ‪.‬‬
 ‫‪۳1,‬‬       ‫‪ - ۱‬بهلوى ‪( 41112‬امن‪.‬امان)» ‪-‬قدی ‪( 11/2‬بناه‪.‬امان) رك‪ :‬مقالهةٌ ‪6/7۲۳‬‬
      ‫ص‪.۵ ۵۸‬‬     ‫‪ 2‬شمارء ‏‬       ‫چاپ ماساچوست‌ح ‪۷‬‬       ‫درمعر فی تارمخ عرب تالف هتی ‪»,mulucepS‬‏‬

      ‫‪ 590‬آرامر کب‌از‪0128 ۲201 :‬میداند‪ .‬بعنی‌ازین پر هرز ‪ ۲۳. ۲611(1)۷۱.‬آنراعاوستابی‬
      ‫(سلاح‌حامی )میداند هوبشمان گوی که وجه‌اخیر بنظرمن بهتراست «هویشمان‬                   ‫‪60622 .3‬‬
  ‫‪ - ۴‬در بت ذبل لختن بمعنی‬                        ‫‪.‬‬   ‫ار‬
                                                       ‫ه‪:‬‬‫زنرك‬
                                                            ‫‪۳‬‬                    ‫‪ :‬احق ‪. ۷۲۰‬‬       ‫‪ ۷‬ور‬
                                                ‫و دوم‌یمعنی ”یناه ‪ ۰‬حمایت؟ است ‪:‬‬      ‫‪ ۵‬بپرهیز ‪ ۰‬حذرکن؟‬

                ‫حان مرا «دین فلك ز هار خوار‪.‬‬                    ‫مگذار ز‪:.‬هار چو در زهار تت‬
  ‫‪.‬‬     ‫‪ °‬ھچ‬    ‫سعد‬   ‫معود‬   ‫‪۶‬‬

               ‫® _ از‪ :‬زبنهار‪-۳‬ی (حاصل مصدر) ‪.‬‬                 ‫نزه‪:‬ار(‪-‬ی ( ست ) ‪.‬‬
```


## [2026-09-05T21:02:13.641Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\np=t[516]\nprint(p[2500:6000])\nEOF"
}
```


### [2026-09-05T21:02:17.353Z] TOOL RESULT

```
 اول ضوم‌میم‌بروزن‬
 ‫زلین گو ‪ » ۸ ۵4‬باها؛ بروزن ومعنی‬                            ‫بی‌تور ‪ ۰‬بمعنی افشای سرباشد وآن مر کب است‬
 ‫زین کوده افسترکیهوی و بلندی پیش زین‬                        ‫از خرق وخالت عنی حرفی را بکسی بسپارند‬
                                            ‫باشد ® ‪.‬‬        ‫که بجابی نگوید او فاش کند وبهمه کس ربههه‬



                                                                        ‫(‪ )۱‬چك ‪ :‬رند و باژند ‪.‬‬

      ‫‪. ۴‬از‪ :‬زبلو (ه‪.‬م‪ ).‬چ‪+‬ه(یسوندتصنیر) ‪.‬‬                     ‫‪ ۱‬درزبان کنولی دز ‪ 0112‬گوبند‪.‬‬

  ‫اف ار‬     ‫از ‪ :‬زین (سلاح) (ه م‪- ).‬‬            ‫‪۴‬‬
          ‫ازینان = از اننان‪.‬‬   ‫مخفف‪:‬‬        ‫‪۵‬‬           ‫‪.‬‬    ‫‪« 082‬باروچا ص‪۰۸۲‬‬         ‫(«‪.‬م‪ ۰ ).‬بهلوی ‪۲1‬‬
       ‫رك ‪ :‬زین کوهه »زین کوه ‪.‬‬         ‫‪۷‬‬           ‫‪ = ۱‬زین كوهه (ه‪.‬م‪ ).‬ورك ‪ :‬زین کوه ‪.‬‬
                                                       ‫زین کوده (ه‪.‬م‪ ۰ ).‬ورك‪ :‬زین کوه‬       ‫>‬    ‫‪۸‬‬

            ‫مانده زین کوهه را ميان دوراه ‪۵‬‬
                                                                  ‫‏‪ - ٩‬سيرم پشنش از ادیم سياه‬
            ‫‪ ۵‬هفت بیکر نظامی ‪e‬‏‬

                               ‫‪-‬کراول» پهاوی‪( 062‬سلاح ت‪,‬جهیز)‪ )۱:‬اوستا ‪-‬‬
                                                                       ‫ب‬
                               ‫‪ « ) 7‬پارنولمه ‪ , ۰۵۹۱‬ارمنی ع ‪(062‬سلاح» تجهیز)‪.‬‬
                               ‫‪ )۷‬اوستا ‪ ( 110822‬سلاح دفاع )‪ ۶‬بارتولمه ‪ ۰ › ۱۵۹۱‬در فارسی ‪012‬‬
                                 ‫‪۲‬‬
                                 ‫‪۰‬ص‬‫‪۳‬سشق‬
                                      ‫ورك ‪ :‬ا‬               ‫) آمده ‪« .‬یبرکف ص ‪۵۵۲‬‬           ‫بجی‬
                                                                                              ‫ر سر‬
                                                                                                 ‫عمنی‬
                                                                                                    ‫(بم‬
              ‫زین‬                                                                   ‫هووبشمان ص ‪. ۱۱۱‬‬
  ‫( برهان اطع ‪) ۷۳۱‬‬
```


## [2026-09-05T21:02:31.484Z] TOOL CALL #41: Bash

```json
{
 "command": "sed -n '1,60p' /home/sfmqrb/git/rishe/tools/fetch_source.py"
}
```


### [2026-09-05T21:02:31.523Z] TOOL RESULT

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


## [2026-09-05T21:02:43.078Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wiktionary.org/wiki/%D8%B2%DB%8C%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D8%B2%D9%86%D9%87%D8%A7%D8%B1\" \\\n \"https://en.wiktionary.org/wiki/%D8%B2%D9%86%D8%AF%D8%A7%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D8%B2%D9%86%D8%AC%DB%8C%D8%B1\" \\\n \"https://en.wiktionary.org/wiki/%D8%A7%D9%81%D8%B2%D8%A7%D8%B1\" \\\n \"https://en.wiktionary.org/wiki/%D8%B3%D9%81%D9%8A%D9%86%D8%A9\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5%CA%B0eys-\" \\\n \"https://www.etymonline.com/word/garlic\" ; do\n  python3 tools/fetch_source.py \"$u\" --note \"page 184, root Ghei 2 / Ghaise: Iranian and Germanic outcomes\" \ndone"
}
```


### [2026-09-05T21:02:49.720Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/9ac27e80afb654eb.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/922c57c923cddcea.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ba40a38b16ddae46.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6cd91b9869e30798.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/96550d35ac718862.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c259de6843bad27f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5cee4656baa2954d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/249dc1dea84bd00a.txt
```


## [2026-09-05T21:02:52.541Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in 9ac27e80afb654eb 922c57c923cddcea ba40a38b16ddae46 6cd91b9869e30798; do\necho \"######## $f\"; grep -n -A12 \"Etymology\" $f.txt | head -70; done"
}
```


### [2026-09-05T21:02:54.322Z] TOOL RESULT

```
######## 9ac27e80afb654eb
79: Etymology 1 
80-
81- 2.1.1 
82- Noun 
83-
84- 2.1.1.1 
85- Derived terms 
86-
87- 2.2 
88: Etymology 2 
89-
90- 2.2.1 
91- Noun 
92-
93- 2.2.1.1 
94- Derived terms 
95-
96- 2.2.1.2 
97- Descendants 
98-
99- 2.3 
100- Further reading 
--
108: Etymology 1 
109-
110- 3.1.1 
111- Pronunciation 
112-
113- 3.1.2 
114- Noun 
115-
116- 3.1.2.1 
117- Derived terms 
118-
119- 3.1.2.2 
120- Descendants 
--
123: Etymology 2 
124-
125- 3.2.1 
126- Pronunciation 
127-
128- 3.2.2 
129- Phrase 
130-
131- 3.3 
132- References 
133-
134- 4 
135- Urdu 
--
140: Etymology 1 
141-
142- 4.1.1 
143- Pronunciation 
144-
145- 4.1.2 
146- Proper noun 
147-
148- 4.1.2.1 
149- Declension 
150-
151- 4.1.3 
152- Noun 
--
155: Etymology 2 
156-
157- 4.2.1 
158- Pronunciation 
159-
######## 922c57c923cddcea
65: Etymology 
66-
67- 1.3 
68- Pronunciation 
69-
70- 1.4 
71- Interjection 
72-
73- 1.5 
74- Noun 
75-
76- 1.5.1 
77- Derived terms 
--
154: Etymology
155- [ edit ] 
156-
157- From Middle Persian [script needed] ( zynhʾl /⁠zēnhār⁠/ ) , originally an imperative command of 𐭬𐭭 ( MN /⁠az⁠/ , “ from, of ” , modern از ) + 𐭦𐭭𐭤 ( ZNH /⁠ēn⁠/ , “ this ” , modern این ) + Proto-Iranian *hār- ( “ to guard; to observe ” , from Proto-Indo-European *ser- ( “ to warn ” ) ) : "guard against this; beware of this", but used as a noun already in Middle Persian with the current meanings.
158-
159- Pronunciation
160- [ edit ] 
161-
162- ( Classical Persian ) IPA ( key ) : /zin.ˈhaːr/ 
163-
164- ( Dari, formal ) IPA ( key ) : [zɪn.hɑ́ːɾ] 
165-
166- ( Dari, formal ) IPA ( key ) : [zɪn.hɑ́ːɾ] 
######## ba40a38b16ddae46
62: Etymology 
63-
64- 1.2 
65- Noun 
66-
67- 1.2.1 
68- Derived terms 
69-
70- 1.2.2 
71- Descendants 
72-
73- 1.3 
74- Further reading 
--
82: Etymology 
83-
84- 2.2 
85- Pronunciation 
86-
87- 2.3 
88- Noun 
89-
90- 2.3.1 
91- Related terms 
92-
93- 2.3.2 
94- Descendants 
--
105: Etymology 
106-
107- 3.2 
108- Pronunciation 
109-
110- 3.3 
111- Noun 
112-
113- 3.3.1 
114- Declension 
115-
116- 3.4 
117- References 
--
197: Etymology
198- [ edit ] 
199-
200: Etymology tree
201-
202- Middle Persian [script needed] ( zyndʾn' ) 
203- Classical Persian زندان ( zindān ) bor. 
204- Ottoman Turkish زندان 
205-
206- Borrowed from Classical Persian زندان ( zindān ) , itself from Middle Persian [Book Pahlavi needed] ( zyndʾn' /⁠zēndān⁠/ , “ prison ” ) .
207-
208- Noun
209- [ edit ] 
210-
211- زندان • ( zindân or zındân ) ( definite accusative زندانی ( zindânı, zındânı ) , plural زندانلر ( zindânlar, zındânlar ) ) 
212-
--
276: Etymology
277- [ edit ] 
278-
279- From Middle Persian [Book Pahlavi needed] ( zyndʾn' /⁠zēndān⁠/ , “ prison ” ) . Ultimate origin uncertain. Perhaps originally "arsenal, armoury", from [Book Pahlavi needed] ( zyn' /⁠zēn⁠/ , “ weapon, armour ” ) and [script needed] ( -dʾn' /⁠-dān⁠/ , “ holder, container ” ) .
280-
281- Compare Old Armenian զնդան ( zndan ) , Classical Syriac ܙܢܕܢܝܩ ( zendānīq ) , Iranian borrowings.
282-
283- Pronunciation
284- [ edit ] 
285-
286- ( Classical Persian ) IPA ( key ) : /zin.ˈdaːn/ 
######## 6cd91b9869e30798
65: Etymology 
66-
67- 1.3 
68- Noun 
69-
70- 1.3.1 
71- Derived terms 
72-
73- 1.3.2 
74- Descendants 
75-
76- 1.4 
77- Further reading 
--
85: Etymology 
86-
87- 2.2 
88- Pronunciation 
89-
90- 2.3 
91- Noun 
92-
93- 2.3.1 
94- Derived terms 
95-
96- 2.3.2 
97- Descendants 
--
105: Etymology 
106-
107- 3.2 
108- Pronunciation 
109-
110- 3.3 
111- Noun 
112-
113- 3.3.1 
114- Declension 
115-
116- 3.4 
117- References 
--
197: Etymology
198- [ edit ] 
199-
200- Borrowed from Persian زنجیر ( zanjir , “ chain ” ) .
201-
202- Noun
203- [ edit ] 
204-
205- زنجیر • ( zincir ) 
206-
207- chain , a series of interconnected rings or links 
208- Synonym: سلسله ( silsile ) 
209-
--
275: Etymology
276- [ edit ] 
277-
278: This etymology is missing or incomplete. Please add to it, or discuss it at the Etymology scriptorium . 
279-Particularly: “Detailed but informal discussion at https://archive.fo/g7MTJ ( https://languagehat.com/zanjeer/ ) - check, in particular, the 2025 comment by user "Xerîb". The gist is that the Persian term (and its Iranic relatives) were borrowed from a Middle Indic reflex of Sanskrit शृङ्खल ( śṛṅkhala , “ chain, fetter ” ) , with a phonetic shift from initial ś- > z- that Buyaner intended to investigate. This etymology was originally proposed by Boyce to Henning, apparently from informal oral talks, and later accepted by Henning circa 1963. Sources are cited in the links, to be added as inline references in a future update to this etymology box.”
280-
281- Pronunciation
282- [ edit ] 
283-
284- ( Classical Persian ) IPA ( key ) : /zin.ˈd͡ʒiːr/ , /zan.ˈd͡ʒiːr/ 
285-
286- ( Dari, formal ) IPA ( key ) : [zɪn.d͡ʒiːɾ] , [zän.d͡ʒiːɾ] 
287-
288- ( Dari, formal ) IPA ( key ) : [zɪn.d͡ʒiːɾ] , [zän.d͡ʒiːɾ]
```


## [2026-09-05T21:03:52.369Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"######## زین\"; sed -n '160,340p' 9ac27e80afb654eb.txt | grep -n -B2 -A10 \"Middle Persian\\|Etymology\" | head -80"
}
```


### [2026-09-05T21:03:52.418Z] TOOL RESULT

```
######## زین
113- [ edit ] 
114-
115: Etymology 1
116- [ edit ] 
117-
118- Borrowed from Arabic زَيْن ( zayn ) .
119-
120- Noun
121- [ edit ] 
122-
123- زین • ( zeyn ) 
124-
125- ornament , adornment , embellishment 
--
130- زین العابدین ( zeyn’el-ʿâbidîn ) 
131-
132: Etymology 2
133- [ edit ] 
134-
135: Borrowed from Persian زین ( zîn , “ saddle ” ) , itself from Middle Persian [script needed] ( zyn' /⁠zēn⁠/ , “ saddle ” ) .
136-
137- Noun
138- [ edit ] 
139-
140- زین • ( zîn ) 
141-
142- saddle , a seat for a rider placed on the back of a horse or other animal 
143- Synonyms: ایر ( eyer ) , سرج ( serc ) 
144-
145- Derived terms
--
179- Wikipedia fa 
180-
181: Etymology 1
```


## [2026-09-05T21:03:53.717Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"######## افزار\"; grep -n -A8 \"^ Etymology$\" 96550d35ac718862.txt | head -60\necho \"######## سفينة\"; grep -n -A10 \"^ Etymology\" c259de6843bad27f.txt | head -60"
}
```


### [2026-09-05T21:03:55.346Z] TOOL RESULT

```
######## افزار
145: Etymology
146- [ edit ] 
147-
148- Inherited from Middle Persian [Book Pahlavi needed] ( ʾp̄cʾl, ʾp̄zʾl /⁠abzār⁠/ , “ instrument, means; spice ” ) . Doublet of ابزار ( abzâr , “ tool, instrument, means ” ) . 
149-
150- Cognate with Parthian 𐫀𐫀𐫁𐫝𐫀𐫡 ( ʾʾbcʾr ) , 𐫀𐫁𐫝𐫡 ( ʾbcr ) , 𐫀𐫀𐫁𐫋𐫀𐫡 ( ʾʾbjʾr /⁠ābžār⁠/ , “ materials, means ” ) 
151-
152- Pronunciation
153- [ edit ] 
######## سفينة
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
69-
70- 1.3.1 
71- Declension 
72-
--
88: Etymology 
89-
90- 2.2 
91- Pronunciation 
92-
93- 2.3 
94- Noun 
95-
96- 2.3.1 
97- See also 
98-
--
105: Etymology 
106-
107- 3.2 
108- Pronunciation 
109-
110- 3.3 
111- Noun 
112-
113- 3.3.1 
114- Derived terms 
115-
--
201: Etymology
202- [ edit ] 
203-
204- From Aramaic סְפינִתָּא / ܣܦܻܝܢܬܳܐ ( sǝp̄īntā ) . Forming the root س ف ن ( s f n ) . Cognate with Hebrew סְפִינָה ( sᵊfīnāh ) .
205-
206- Pronunciation
207- [ edit ] 
208-
209- IPA ( key ) : /sa.fiː.na/ 
210- ( Gulf ) IPA ( key ) : /səˈfiː.nə/ 
211-
--
443: Etymology
444- [ edit ] 
445-
446- Inherited from Arabic سَفِينَة ( safīna ) .
447-
448- Pronunciation
449- [ edit ] 
450-
451- IPA ( key ) : /sfiː.na/ 
452-
453- Noun
--
```


## [2026-09-05T21:04:18.077Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nsed -n '181,260p' 9ac27e80afb654eb.txt\necho \"######## PIE gheys\"; sed -n '1,120p' 5cee4656baa2954d.txt | head -60"
}
```


### [2026-09-05T21:04:18.130Z] TOOL RESULT

```
 Русский 
 سرائیکی 
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

 See also: رين , زين , رین , and ر ي ن 

 Central Kurdish
 [ edit ] 

 Pronunciation
 [ edit ] 

 IPA ( key ) : /ziːn/ 

 Noun
 [ edit ] 

 Northern Kurdish

 zîn 

 زین ( zîn ) 

 saddle 

 Derived terms
 [ edit ] 

######## PIE gheys
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5%CA%B0eys-
FETCHED: 2026-09-05T21:02:49Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found
```


## [2026-09-05T21:04:20.976Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== DKS zaina/zin ===\"; grep -n \"zaina\\|ysīna\\|ysana\\|zaēna\" ISS_alt_DKS.txt | head -10\necho \"=== CHEUNG zay ===\"; grep -n \"zaēna\\|\\*zai\\b\\|zay-\" CHEUNG.txt | head -10\necho \"=== IEC ghei ===\"; grep -n \"ĝhei\\|ghei-\\|gaiso\\|ghaiso\" IEC.txt | head -10\necho \"=== WLD band3 ghaiso ===\"; grep -n -i \"ghaiso\\|gaiso\" WLD_band3.txt | head -10"
}
```


### [2026-09-05T21:04:21.060Z] TOOL RESULT

```
=== DKS zaina/zin ===
310:a-uysánü ‘пос self’, Manj. 390, variant Z 914 anütma; Manj., 323 a-uysanai, abstract V 103, 19v3 a-uysanetd.
382:an- ‘ќо breathe', see uysana-, uysamdi, uysüná.
498:aysünai 'boy', K. 140-987, see alysanat,
548:alysünaa- ‘youth, boy, son (of а king)’, alysánai, alysānei, inst. sing. alysanaina, later forms v 11:8 dysánat; ut 128715 eysünai; K 94:96 eysaunai; K 65, 83v3 iysánai; fem. Z 6312 alysügyo, Z 22'212 alysāgye ‘girl’, її 1o6:20 eysäja (daughter of a minister); H rr4s eysauja; v 291, iqar aysämje; 1ш 94, 352 iysamgyau, BS düraha-, kumüra-, 'Tib. gion-nu ‘young’, Käšyar Kanéaki 'alyondsa, 'alyohjah (see BSOAS 13, 1950, 393). From arz-, ras- “то grow’, Оза, D. irdxun, І. räzyn ‘to grow’, I. rdxdn ‘growing organism, child’, D. irdz, I. тйл ‘growth’. Also aysdau, aysdo may be from arz- meaning 'young', BS bala-. š
712:ahauvam pijsa padimi 'it makes the old young again, it makes the weak strong’ (фа = pátajsa-). See haut-, hot- ‘be able’. ahva- ‘noose’, У 161, 35v2 [/[ahvána baittä ‘is bound with a noose’, BS ла ca sa trsna-paša-baddho bhawisyati, Tib. sred-pahi áags-pas (BS paša-) béius-par mi hgyur-ro ‘he is not bound by the noose of desire’, See aha-, ahg-, inst. plur. ahyau. For -hv- note also ahva-, aha- 'belly'. аһуа- ' belly', as first component іп a/va-riysa- ‘fear’ from ттїуѕ- ‘to tremble’ and айша- ‘belly’, as the source of ‘fear’. See aha ‘belly’, and rriys- ‘to tremble'. The meaning is from the use of a name of part of the body for the affection in that part, as O.Pers. uii ‘intelligence’ from uč- t ear', Av. karana- ' ear! and ‘deaf’, like Georgian qur-i ' ear? gru ' deaf’, Megrel ‘uru ' foolish’; Greek laxlov ‘hip’, {суас "pain in the hip'. Hence O.Pers. afuva- ‘fear’, O.Ind. dpva-, apvá ‘fear’, from the source ‘belly’. Note Al-T'ha'alibt, Histoire, ed. Н. Zotenberg 714 fa as- hala 'l-xaufu batana-hu ‘and fear loosened his belly’. Similarly O.Ind. saşkulī ‘ear’, and ‘disease of hearing’. ahvañe ‘пої to be spoken’, 11 73:188 mire а ahvañe stana “1 shall die since it is not to be spoken’. Base Avan- ‘to speak’, лоайа- ‘ќо be spoken’. ahvadamdi 'before eating’, 1 167, 83r4 ahvadàrdi tharka masi hviri ‘as much as a walnut is to be eaten before taking food’. Base huar- 'to eat’. ç ahvanda- ‘not man’, v 308, гт, BS amanusya- in the series from gods to goblins, ahvandä ‘not men’, V 257:6, 154 Хћоаупій ahvandà uvüra 'men, not men, noble ones’, See Люала- ‘man’, o., ahva-riysa- 'belly-shaking, fear’, SuvO: 4v2. hagapaniata , iyd o фйуса u vadrava tyo gürtvá o puuaná o ahvariysá Туй, BS fohayase.!py anarthe са bhaya-vyasana. eva ca, here corresponding. to bhaya-.‘fear’, See alia-. .„; ahvariysüt ‘lack of fear’ (variant ahartysátd quoted by S. Konow, ed. to v 113, 35v1). Possibly a subscript small a added before hva, hardly visible on the photograph, but reported by Konow. The scribe may have intended a- ‘not’ before ahva-rīysätä (instead of an- as іп a-uysana) or has wrongly written hva for -ha- in ahariysa- ‘поб trembling’. The ending -did may represent either the suffix -ita-, or stand for -d, as in V 77, І45У5 viysáte 'lotus' for oiysd, with busānätai ‘scented’ for busanai, ahvyütie ' not produced, eternal’, ш 128:2—3 sukye ahuyañe samtsüru bawdani-iül(e?) guchüme udiíayi ‘for escape from the universal (one == universal) eternal transmigra- tional prison’. For the ‘prison’, v 126, br sagusárüm bürmina, BS samsára-bhava-bandhanat, Tib. léon-ra, Tokhara B samsarsse pele, and Jaina samsüra-caraya-. Base Лац-:Ли- ‘to bear young’, hence parallel to BS aja- ‘not produced’ (see also ahámáta- ‘not arisen’); Av. hunu- ‘son’, haxanrü.husna-, haota-, hunahi, hunami, O.Ind. ste, sitd-, sünti-, Zor.P. hunufahenitan, visiitakan. Form ћоуа-, as duya- ' to beat’, base dav-. IE Pok. 913-14 seu- :si-. See also уй 'son'.
832:üysam ‘millet, panicum miliaceum’, v 2103773 Ййїєї gaudi фуғат пй hasta (küsi?) 'then Gaudi received millet, eight measures’; п 36, 8br dysam haudi ‘Һе gave millet'; HI 147bi äysam dva kūsi 'millet two küsa-measures'; (without hook) v 306-07: r-r aysam asti küsa IO ‘there is millet, то küsa-measures'; v 204, 3041 aysam haudá ‘he gave millet’; Ir 16"3:5 HH aysam drrafirau. 'transport that millet’. The later form in Sid. тбгт eysá (with the two dots in place of the anusvüra one dot *eysam), BS nivüra-, Tib. ¿Ze ‘millet’. Base *arzana- through "ülysana- to üysam, eysam to N.Pers, (dialectal) arzan, alum (-т as gandum ' wheat"), Zor.P. (Gr. Bd. TD2 117-3) "шт alom, Baxtiari alum, Pašto #dan, Wanetsi &idan, Sangl&& wuğdan, Yid. yürzun, Waxi yirau, Orm. ašan. Possibly arzana- from arz-, raz- 'to grow’, as ‘growing plant’ specialized to 'millet', see arz- s.v. alysánaa-, aysdau. The panicum italicum was ggusa-, N.Pers. gavars.
853:äysnä ‘seats’, gen. plural, BS asana-, > áysana- 111 130°30-1 hva hva sthünave пута vird parihiryau ' may you place оп seats severally the heads of monasteries’ (BS sthanapati-, see Indian Antiquary 6, 1877, 200, 204, 207).
1042:ipihi, : зве S.V. a~, i- ‘not’. imāñäm ‘yours’, i 11073 ¿mañám u hve:hvu:ra hamtsi niyam 'we senle your min and the Uigurs together’, H 113102 cu imāñām va faga ' what is the land for your men’, See umani, атайт. imi ‘you’, HI 60:39 imi ditta ' you see’. See ami, ита. imu 'to-day', v 78, 149г1; 3; 4; 5, Tib. den; v 78, 149r1 imá; Z 247483 imu kadā. Later т, Iv 46b £ haura ' give at once’; п 14, 2b4 7 ada ästamna; ч 68-17 í hadà pyärä. From ayam, iyam > ima-, O.Pers. ima-, N.Pers. im-ràz ‘to-day’, Zor.P. im 'this', Sogd. 'm, m-, ТЕ Pok. 281-2 e~, ei~, See also mara ‘here’, and т. imüka 'parrot' II 35:3: (Rau)kalq imkka icüga karavi stüryu; OI 47747 kaukalą imüka casa karavi stüryi ' cuckoo, parrot, jay, karaviraa-cuckoo, starling’, From Chinese ying-u, older png-miu, see BSOS 8, 1937, 915 (K 280-6; 1283:2). irnüjsi ‘of to-day’, adjective to zu, with suffix of time -Jst, HI 107:20 mnüjst hadamjsa; їїї 124778. īmūmjsū ' ta-day'', BS adya. ime ‘І ат', ѕее ah-. imauvua loc. plur. ‘distressful’, see amatau. iyatara- ‘inferior’, v 109, 31v4 Рани rro iyataránu kşīrañänu и ttünu rro mástünu (hstyrañdnu rakşo yanamá ' of these inferior lands and of these great lands we make protection ', BS tesüm ca rastranam іезат ca visayünüm ürahgüm karigyümah ; JS 8v3 īyarai dugidubha па sa kidi pajsá ' the “inferior nága-snake is very strong’; JS 27:1 sa arama 2 Туатаї pamda satva ' this ungrateful inferior foolish being’. : Parallel K 1, 134r3 nyüttara-ksirei beside K r, r34vi 'mistdeo janavatg. From "adah, Av. ad3, адата-, абайт, !O.Ind. adhas, adhara-, adhama-. ТЕ Pok. 771 панох, udheri, ‘s pdhero-, Lat. inferus, infimus, infra, Armen. әла, Got. 7 undar. iyānda- ' perpetual’, Bed 48r1 ahatcastë nasirrīmä тудай agamjsä paraustä yinīmä “І shall practise moral restraint (BS sila-) perpetually unbroken, unstained, faultless’, BS Äla-carim vimalüm parisuddhäm nityam akhandam acchidra careyam; SuvO. s4r7 randu pátülye ttätä pata 'thesc verses of prosperity always’, BS ekā samsiddhi-pada, Tib. Eég-tu de-hho-na yanm-dag-par sgrub-pa sbyin-ba; K. 153'30-1 iyáda nasauda 'always calm’; later Sid. 106v3 уйтай, Tib. rtog-tu 'continually'; Sid. r4or4 уйтай, Tib. thams-cad-du; п 126:17 pauidai vastà yämdü оаза niradä hamare ' every day throughout they can issue this way’; Sid. 128v1 yada, Tib. rtag-tu. With adjectival -va- п 104591 Iyüdve namadrründ jsai, From *aiva-anta- ' to one end, to all ends’, все i- in z-garfd 'with the whole throat’, with anta- ' region, end’, Oss. D. ándá, I. ädtä ' outside"; also bifsindd ' altogether', benda, and anada. iyá ‘he might be’, optative to ah-, also 110, i. iys-, see uys- ‘out, up', and ays-. iysá 'young (?)', п 41711 fidi зала mau Казі vilakā iysa ‘food must be prepared, liquor to drink for the little, the young ones’. Possibly iysaa- to base alys-, ays- 'to grow’ in alysánai ' boy’, aysdo, aysdau ' young', BS bäla-, from arz-, raz-, Oss. D. iräzun, See alysanaa-. iysánai ‘young, boy’, K 65, 83v3 siidhana iysānai ' Sudhana the youth’ (BS humüára-); K 46:33 si iysánat cadam пата himye ‘the boy was by name Candana', See alysānai.
1047:The i-umlaut of i resulted in ur and £ (Z 5'74 Ruire; Z 2:16 Атта). ТЕ Tra- is from older *urya-, the connexion is with Oss. D. urd, I. йг, beside also xurd, I. xür 'stone', adj. I. virag; compound D. uiragdur. Sid. 148v5 üdara-, BS Каса-, Tib. méhig-bu 'crystal', with Iran, varta- ‘stone’, and JS туут urvürinai gard ' crystal mountain’, from base таг: ur- belong here. ira-samga- ' proper name Írasamga-', II 15/2715; IV 1610 and elsewhere, contains ' jade-stone', in Chinese T-səng, older j2t-soug (К. 176; 104777), a painter from Khotan in China (KT тү 16). ira- 'intoxicant drink, possibly ale’, п тото ira u hura u buiysana, =11 99:175 frd u haurd bviysuq ' ale and mare's milk and sesame drink’. See bviysma and hura- (Av. hurá-); also 11 11:23; 11 99:187; adjectives irauda and iri. From *aluia-, Oss. D. áloton, iláton, I. dluton, Georg. alud-i, lud-i' mead, beer’. IE Pok. 33-4 alu-, alud- ' bitter, beer, alum’, Greek ФА0біроу 'bitter', Lat. alita ‘soft leather’, alzmen ‘alum’; O.Norse gi 'beer, carousal', O.Engl. ealu(d), O.Sax. alo-fat 'ale cup', Lit. alis ‘mead’, O.Slav. oli ' beer', Finn. lw olut ‘beer’, irata- 'wily, seductive’, dyadic with BS за/Ла-, parallel with BS Ау, mrsagadin-, paisunya- and. püpa-; as- sociated with drija 'lie', yola- 'evil', byügga- 'ill- speaking’; Z 23:126 striye atë trate fdaththe ‘women are exceedingly wily, tricky’; Z 24:51 adàtya irata $fathyau jsa purrmdá 'they overcome lawless wily ones with tricks’; Z 24:260 mārä ha liste dutará irate date ' Māra- demon sent his wily, cunning daughters'; v 54, 104a5 ут Trate rraysge 12 'wily, swift (verse) 12°. See Triye. From *alya-, base al- 'be wild, mad, make wild’, Av. ara- ‘тай’, Oss. DI. árra ‘тай’, Sogd. "7'& *йтайа- (see BSOAS 24, 1961, 473-8). IE Pok. 27-8 al- ' wander, be foolish, mad’, Greek &Ат| ‘wandering’, @\йоз ' be outside oneself’, Lit. aliótis ‘foolish’. The abode of Kubera, the Alakā city, may in its name allude to the amorous sports there, But aniratete jsa from *a-naryatüti- above. 4-2
1108:uysan- ‘to breathe, JS 21v4 na uysamdi thu vàgta ћітуѓаї vira uysana be-tüda ka na tti satva mirüre ‘уои did not breathe out at all poisoned breath that the beings might not die’. From an- ‘to breathe’, Av. dntya-, pardntya- 'breathing in and out’ (uncertain оуйпауй), O.Ind. dniti, Atharva-veda апай, anita-, йпі-, Tokhara В anā- sh-, ‘to breathe’, onolme 'being', IE Рок. 38-9 an(2)-, Greek &vepos, Lat. animus, Celt. O.Ir, anal, Welsh anadl, Got. uz-anan, uzün, O.Norseond, gen. andar‘ breath, soul". See also uysana- ' breath ', uysána ' self’, uysnora- ' being’.
=== CHEUNG zay ===
14862:*MIDDLE PERSIAN: BMP zd- /zay-/ ‘to ask, demand, implore’ || (+ *ni-) MMP nyz’y- 
14894:*MISC: Orm. zay-ék, Zay-Ok ‘to ask for’ = Zey-/Zeyók, Zay-/Zayók, jay-/jayók ‘to ask, 
14988:jenda ‘alive, living’, Kurd. Zin ‘life’, Tr. zayaya/zay- ‘to give birth’ 
15187:*MISC: Orm. zay-ék ‘to chew, mastigate’ = zay-/zayók 
29781:*NEIR: (+ *aua-) Yi. wuza- ‘to be tired’, M. uzay-/uzayi- ‘to be left behind’ || (+ *ui-) 
29799:*zai! ‘to set in motion, impel’ 
29828:adopt’ || (+ *a- ?) Yzgh. zay- ‘to come’ || (+ *aua-,*a- ?) Wa. waz(a)y-/wazd- ‘to 
30089:be born’, (orig. caus.) Sh. (Baj.) zi(y)-/zod, Rosh. zay-/zöd, Sariq. zey-/züd, zid ‘to 
30094:*MISC: Par. zà-, Orm. zay- ‘to be born’ = zay-/zayok || (+ *à-) Arm. (LW) azat ‘free’ 
35795:zd- /zay-/, 221 
=== IEC ghei ===
4557:ghaisos ‘lance, pole’. WP I, 528 Av. cf. gaesus ‘lancer’; Gk. khaios *shepherd's crook’; Hes. gaiós (Thrac. or Maced. (?) «lance, pole); Celt. LW in Gk. gaisos ‘javelin’; Olr. gaí, gáe, Ir. gai, gaoi ‘spear’; Gallo-Lat. gae- sum; Br. goaó, goaf, gwat; Cor. gew; W gwaew lance, javelin’, w. induced labialism; OHG gër, MHG geér(e); OE gàr; Du. geer “bias, crosscut, gore’; ON geirr ‘spear’, geiri ‘gore, gusset
=== WLD band3 ghaiso ===
```


## [2026-09-05T21:04:26.249Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '29799,29835p' CHEUNG.txt"
}
```


### [2026-09-05T21:04:26.292Z] TOOL RESULT

```
*zai! ‘to set in motion, impel’ 
*AVESTAN: zaii- ‘to set in motion’ || (+ *fra-) ‘to permeate, penetrate’ || (+ *ui-) ‘to 


let go, separate oneself from’ — Liste: 68 f. 

Pres. athem. red.: IND. med. 35р. ? YAv. "zazaitoe (Yt 5.34, Yt 15.24); Aor. athem.: SUBJ. 2р1. OAv. 
iuuizaiiada (Y 53.7); Caus.: IND. 159. YAv. frazaiiaiiami (V 5.18), SUBJ. 25р. YAv. frazaiiaiiahi (V 
5.16; Narten 1984: 275 £.) 


"MIDDLE PERSIAN: MMP zyn, ВМР zyn /zén/ ‘armour, weapon, sword’ = DMMPP: 
386b f. 

*PARTHIAN: zyn ‘armour, weapon, sword’ || (+ *upa-) *bz’y- ‘to begin’ = Ghilain: 
86 | DMMPP: 386b f., 18a 

(+ *upa-) Pres.: IND. 35р. *’bz’yd, OPT. *’bz’yndyh; Partic.: perf. pass. 'bz'd 

*NWIR: ? Siv. z- (supplet. ese) *‘to impel’. © The verb is used in dílem mizé ‘my 
heart wishes’, hardly from *xyaz, pace Eilers, WIM III, l.c. 

*NEIR: ? Pash. zanol ‘to insert, plant, stab’, Sh. (Baj.) záz-/zoxt, Rosh. zéz-/zuxt, 
Bart. zoz-/zoXt, Orosh. zoz-/zoxt, Sariq. zoz-/zuxt, Yzgh. zaz-/zext ‘to take, obtain, 


462 *7а12 


adopt’ || (+ *a- ?) Yzgh. zay- ‘to come’ || (+ *aua-,*a- ?) Wa. waz(a)y-/wazd- ‘to 
arrive, come’ || (+ *pari-) ? Pash. parz-, parj- ‘to fall, be thrown down, be prostrated’ 
|| (+ *ш-) Oss. D. izazun/izazt ‘to lift up [with a handle]’, Oss. D. izazna ‘lever, 
crow-bar? 

*SANSKRIT: hay ‘to impel, drive, hurl’ (RV+) || háya- (m.) ‘horse’ (RV+), asva-hayá- 
‘spurring horses’ (RV) > EWAia II: 802 f.
```


## [2026-09-05T21:04:27.579Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SYN weapons section ===\"; grep -n \"20.21\\|ARMS, WEAPON\" SYN.txt | head\necho \"=== HUB zin/afzar ===\"; grep -n \"afzar\\|abzar\\|zin 'Sattel'\\|zaena\" HUB.txt | head -10"
}
```


### [2026-09-05T21:04:27.634Z] TOOL RESULT

```
=== SYN weapons section ===
2356:4, OE wéepned ‘male’, also cpd. wepedman, wépman fr. wepen ‘weapon, penis’ (4.492, 20.21).
6683:NE tool (N He _ . (means, instrument ). Ns OE wiepen ‘weapon’ (20.21)
34330:| CHAPTER 20 i WARFARE 20.11 Freur (vb.) 20.28 Gun; CANNoNn 20.12 BatrxE (sb.) 20.29 GuNPOWDER 20.13 War 20.31 Anmor (Defensive) : 20.132 Enemy 20.32 BreasTPLaTr, Corsier hea ies 20.338 HetMer ne aes 20.34 Snreip 20, Renton 20.35 Fortress 20.18 GENERAL 2030 = LOWnE 20.19 Ap 20.41 Victory 20.21 Wearons, ARMS 20.42 Derzat (sb.) 20.22 Crus 20.43 Arrack (sb.) 20.222 BATTLE-Ax 20.44 DEFENSE 20.23 Sune 20.45 RETREAT (sb.) 20.24 Bow 20.46 SuRRENDER (vb.) 20.25 Arrow 20.47 Captivr, PRISONER : 20.26 SpPEar 20.48 Boory, Srors : 20.27 Sworp 20.49 AxpusH (sb.) 20.11 FIGHT (vb.) ee péxopal, qroenewo one meu Lith. kovott, kautis, muStis TONELO erjask, vega Lett. kauti Lat.  pugndare, proeliari Dan. tee bare ChSl. mtrdli 46, bratt It. combattere, pugnare Sw. kampa, fikta, sldss SCr. _boriti se (biti se) : Be. Fee en OE feohtan, wigan, win- eer oS Sia se) - , nan ol.  walezyd, bid sie : sa Pa ME Ee kempe Russ. eee Nee bit'sja, . chim, cai rie rat'sja | a ON al troidim ne Ae vechten Skt.  yudh- : ym ehtan Av. parat-, yud- Br. en em ganna MHG vehten, wigen
34494:MLat. armata ‘armed force’, either land force or more commonly naval force (cf. Du Cange), fr. fem. sg. of Lat. armaius (pple. of armdre ‘provide with arms’, fr. arma ‘arms, weapons’, 20.21), and prob. abstracted fr. armdata classis (cf. classis, 20.16). Hence It. armata used of either ‘army’ or ‘fleet’, Sp., Port. armada ‘fleet’, Fr. armée ‘army’ (> Dan., Sw. armé, NHG armee, SCr., Russ. armija, etc.; Russ. > Lith. ar- mija); Rum. armaidé (neolog.). Also OFr. > ME armie, NE army, but the early use was ‘armed expedition’ or ‘armed force’, either of sea or of land, sometimes ‘fleet’, and only later restricted to a land force (NED s.v. army).
34607:20.21 WEAPONS, ARMS
34858:NG émdov ‘weapon’ (20.21) and official term for the soldier’s rifle.
34894:Russ. ruz/e ‘gun’ : oruzie ‘weapons’ (20.21). Briickner 381.
34924:Many of the words for ‘weapons, arms’ (20.21) cover both offensive and defensive arms. The latter may, of course, be expressed more specifically by the addition of ‘defensive’, ‘of (or for) defense’, e.g. Grk. irda dyuvrixd, Fr. armes défensives, NHG_ schutzwaffen, Lett. aissardzibas ieroci, SCr. orudje za obranu, Boh. zbrané ochranné, Pol. bro
34925:odporna. Such obvious phrases are not entered in the list. Apart from a few repeated from 20.21, those entered are such as correspond most nearly to NE armor in its historical uses.
34933:1. Grk. drda ‘weapons, arms’ (20.21) includes defensive arms. Hence, through vb. érAlfw, dmAtopds, ete.
=== HUB zin/afzar ===
466:95. Np. afzar Werkzeug* (bal. LW. auzar) ~ phi. afzar
6464:paz. aw(a)rdi' (zd. aiwi + rwd) H. 94; afzar, avzar *Werk-
10242:afzar 16.
```


## [2026-09-05T21:04:37.553Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '34607,34640p' SYN.txt | head -40\necho \"=== zaya in SYN ===\"; grep -n \"zaya\" SYN.txt | head"
}
```


### [2026-09-05T21:04:37.608Z] TOOL RESULT

```
20.21 WEAPONS, ARMS
(pl. or coll.) Grk. dda Goth. wépna Lith. ginklaz NG émda, appara ON vapn Lett. teruoci Lat. arma, téla Dan. vaaben ChSl. oraztja It. armt Sw. vapen SCr. oruzje Fr. armes OE wepnu Boh. zbrané Sp. armas ME _ wepens, armes Pol. brow, orez Rum. arme NE weapons, arms Russ. oruzie Ir. airm Du. wapens Skt. ayudha-, asira-, NIr. airm OHG wafan, giwafani castra- W. arfau MHG wafen, gew@fen Av. zaéna-, zaya-, Br. armou NHG waffen snaivis-, 301515- Generic words for ‘weapons, arms’ | P. 1.72. Ernout-M. 72f. Walde-H. come by specialization of ‘implements’ | 1.67 f.
to ‘implements of warfare’, or of ‘fittings’ through ‘defensive armor’, or by gen- eralization from missile or cutting weap- ons derived from verbs for ‘throw’ or ‘cut’. Some are from verbs for ‘strike’ or ‘fight’.
1. Grk. érdov ‘instrument, implement, weapon’, pl. dra ‘arms, weapons’ : érw (in cpds. dudt-, bi-, &p-, etc.) ‘be busy about, look after, etc.’ : Skt. sap- ‘care for, attend to’, Av. hap- ‘hold, support’. Walde-P. 2.487. Boisacq 270, 707 f.
NG dpyara (pl.; sg. &pua not used), fr. Lat. arma (below). G. Meyer, Neugr. Stud. 3.11.
2. Lat. arma (pl.; Vat. fem. sg. arma > Romance forms, all in pl. ‘arms, weapons’. REW 650), sometimes de- fensive armor (vs. ¢éla), but mostly generic : Lat. armus ‘upper arm, shoul- der’, Goth. arms, etc. ‘arm’ (orig. ‘joint’), Lat. artus, articulus joint’, Grk. dpyds ‘Joint’, dpapicxw ‘join, fit’. Walde-
Lat. téla ‘missile weapons’ (spear, etc.) and more generically ‘offensive weapons’ (sword, etc.), etym. dub. Walde-P. 1.717. Ernout-M. 1021.
3. Ir. arm, W. arf ‘weapon’, pl. airm, arfau, (arch. eirf) ‘weapons’, fr. Lat. arma (above). Vendryes, De hib. voc. 114. Loth, Mots lat. 134.
Br. arm ‘arm, kitchen utensil’, pl. armou ‘weapons’, fr. Fr. arme.
4, Goth. wépna (pl., renders érAa), ON vapn, OHG wafan, MHG wafen (sg. and pl.), Dan. vaaben (pl.), Sw. vapen (sg. and pl.). OK wepen, ME wepen (sg. and coll., pl. OE wepnu, ME wepens), NE weapon, Du. wapen (sg., pl. wepens and wepenen), NHG waffe (sg., pl. waffen; NHG wappen ‘coat-of-arms’, fr. LG), OHG giwafani, MHG gewefen (coll.), etym.? Walde-P. 1.257. Feist 561.
5. Lith. ginklas (sg.; pl. ginklat) : ginu, ginti ‘defend’, genu, ginti ‘drive’, Grk. 6elvw ‘strike’, etc. Walde-P. 1.681.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
F Digitized by Arya Samaj Foundation Chennai and eGangotri i
i 1384
ot]
SELECTED INDO-EUROPEAN SYNONYMS
Lett. teruocis (sg. also ‘tool, imple- ment’, pl. zerwoct) : ruocis ‘handle’, ruo- ka, Lith. ranka ‘hand’. Cf. Lith. ¢rankis ‘tool, means’. Trautmann 237. Miuhl.- Endz. 2.60.
6. ChSl. orqzt%je (sg. ‘sword’, pl. orqziga = érda), SCr. orudje, (Boh. oruzi arch.), Pol. orez, Russ. orudie (sg. and coll.; cf. also ruz’e ‘gun’), apparently fr. an otherwise unattested Slavic root rey-, meaning? Miklosich 281. Briickner 381.
Boh. zbran (sg.; pl. zbrané), Pol. bron (sg. and coll.) : ChSl. brant ‘war’, brati ‘fight’, etc. (20.11). Berneker 74.
7. Indo-Iranian words given in stem- form.
Skt. dyudha- (most generic word, cf. Macdonell-Keith 1.60), deriv. of a-yudh- ‘make war on, attack’, epd. of yudh- ‘fight’ (20.11).
Skt. astra-, perh. (as orig. ‘missile’) :
Skt. ¢astra-, mostly a cutting weapon ���knife, sword, dagger’, fr. ¢as- ‘cut’.
Av. zaéna-, and zaya-, with zayan- ‘armed’ : Skt. heti- ‘missile’, hi- ‘urge, hurl’, prob. also Ir. gae, OE gar, ete. ‘spear’ (20.26). Walde-P. 1.546. Barth. 1650, 1666. Walde-H. 1.576.
Av. snaibis- : sna6- ‘strike’, Skt. cnath- ‘pierce’. Walde-P. 1.402. Barth. 1628.
Av. soidi8- : sid-, Skt. chid- ‘split’, Barth. 1577.
20.22 ff. For fuller description of weapons and their names, cf. the follow- ing. Schrader, Reallex. passim (Keule, Schwert, etc.). Couissin, Les armes ro- maines. M. L. Keller, Anglo-Saxon Weapon Names. Falk, Altnordische Waffenkunde, Vidensk. Skr. 1914, no. 6. H. Bauersfeld, Die Kriegsaltertiimer im Lebor na Huidre, Z. celt. Ph. 19.294 ff. Niederle, Manuel de l’antiquité slave 2,274 ff. Zimmer, Altindisches Leben
as- ‘throw’. Uhlenbeck 19. Walde-P. | 298 ff. Macdonell-Keith, 2.591 f. with 1.134. refs. Geiger, Ostiranische Kultur 441 ff. 20.22 CLUB Grk.  pdradov, kopbyn, EbAov Goth. (¢riu) Lith. kuoka, kilé NG  pérado, parcobxa ON klumba, klubba, kylfa, Lett. vale Lat. clava, fistis rudda ChSl.  dritkolt It. mazza Dan. ikfélle SCr.  buzdovan Fr. massue Sw. klubba Boh. _ palice, obuSek Sp. porra OE sdagol, cycgel Pol. patka Rum. mdciucé ME _clubbe (kuggel) Russ. bulava, dubyna ir. lorg NE club (cudgel) Skt. vadha-, vadhar, gada- Nir. —_ lorg, lorgaid Du. knots Ay. vazra-, vadar, gasa- W. wb OHG = kalbo Br. bataraz MHG kolbe, kiule NHG keule
The ‘club’ was man’s earliest weapon and continued to be one of the recog- nized weapons down into the historical period, or even to the present day among backward tribes or in rural feuds. It was mainly a striking, but in part also a hurling, weapon.
The words for ‘club’ are connected
with 1) verbs for ‘strike’ (function), 2) words for ‘wood’ (material), and 3) words for rounded objects (‘knob, knot, ball, lump, wart’, etc.) with reference to the characteristic bulging head of a club.
1. Grk. péradov, beside paris ‘rod’, paBdos ‘rod, wand, staff’, perh. : pérw ‘incline, bend down’, Lith. virpti ‘quiv-
CC-O0. In Public Domain. Gurukul Kangri Collection, Haridwar
er’, varpa ‘ear of corn, spike’, ete. Walde- Pp. 1.276f. Boisacq 835 f.
=== zaya in SYN ===
12340:Av. pairidaéza- ‘hedged-in place’, perh. ‘garden’ (cf. NPers. paléz ‘garden’, and loanwords Grk. rapédeoos, Arm. partéz ‘enclosed garden’) : pairi-daézaya- ‘wall about’, Skt. déhi-, Grk. retxos
25741:Skt. hdyana-: Av. zaén- ‘winter’, zayana- ‘wintry’, (14.74).
25756:zayana- ‘wintry’, Skt. hayana- ‘year’.
34608:(pl. or coll.) Grk. dda Goth. wépna Lith. ginklaz NG émda, appara ON vapn Lett. teruoci Lat. arma, téla Dan. vaaben ChSl. oraztja It. armt Sw. vapen SCr. oruzje Fr. armes OE wepnu Boh. zbrané Sp. armas ME _ wepens, armes Pol. brow, orez Rum. arme NE weapons, arms Russ. oruzie Ir. airm Du. wapens Skt. ayudha-, asira-, NIr. airm OHG wafan, giwafani castra- W. arfau MHG wafen, gew@fen Av. zaéna-, zaya-, Br. armou NHG waffen snaivis-, 301515- Generic words for ‘weapons, arms’ | P. 1.72. Ernout-M. 72f. Walde-H. come by specialization of ‘implements’ | 1.67 f.
34630:Av. zaéna-, and zaya-, with zayan- ‘armed’ : Skt. heti- ‘missile’, hi- ‘urge, hurl’, prob. also Ir. gae, OE gar, ete. ‘spear’ (20.26). Walde-P. 1.546. Barth. 1650, 1666. Walde-H. 1.576.
```


## [2026-09-05T21:04:38.424Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '460,480p' HUB.txt\necho \"=== HRN afzar ===\"; grep -n \"afzar\" HRN.txt | head"
}
```


### [2026-09-05T21:04:38.489Z] TOOL RESULT

```
93. Np. afraxad ist nach Horn's richtiger Etymologie
(Wrzl. reg^ in ogiyto u. s. w.) — zd. aiwi + razay^iti
(vgl. zd. rdzayfAti 'ordnet', osset. araztn rich ten), also
afraktan der ursprungliche, afraxtan der (nach Analogie
von afrozam : afroxtan u. s. w.) neu gebildete Infinitiv.
Ebenso jetzt Fr. Miiller, WZKM. 8, 186.
95. Np. afzar Werkzeug* (bal. LW. auzar) ~ phi. afzar
geht nach ZDMG. 32, 408 auf ein ap. ^ahizara-, nicht
*abidara- zurtick. Daher bleibt arm. ddar 'arredo, for-
nimento, rimedio* etc. (das Fr. Miiller wieder heran-
zieht) besser weg. Mit ap. ^abizara- deckt sich laut-
lich skr. abhihara-^ das aber 'Herbeibringung, Raub* etc.
bedeutet.
96. Aus aiwi -\- savay^iti ware im Neup. ^afsdyad ge-
worden: das vorliegende afzayad Vermehrt' muss auf
*aiwizavayfiti zuriickgehen % das sich vielleicht zu skr../t^
^) Vgl. skr. avapatati *fallt herab* nach der 1. Klasse.
*) Vgl. afgh. LW. ufiSUiq 'humble, meek' neben afgh. LW. past
*low, abject, lower, below'.
') Bei solchen Reconstructionen mUssten eigentlich imm'er die
altpersischen Grundformen angesetzt werden. Da aber die (vorhandenen)
=== HRN afzar ===
```


## [2026-09-05T21:05:19.306Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wiktionary.org/wiki/%D9%81%D8%B3%D8%A7%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D8%A2%D8%A8%D8%B2%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D8%B3%D9%81%DB%8C%D9%86%D9%87\" \\\n \"https://www.etymonline.com/word/auger\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5%CA%B0ey-\" ; do\n  python3 tools/fetch_source.py \"$u\" --note \"page 184, root Ghei 2 / Ghaise: apsan, ab-zan, safineh, auger, PIE root\"\ndone\necho \"=== Geu 2 in book ===\"\ngrep -l \"Geu 2\" data/extracted/batch/*.json | head -5"
}
```


### [2026-09-05T21:05:23.047Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/5319383a3fbbea25.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c87feae09c42b9ca.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6531b72b39d782da.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/915db67d5c48cafa.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/255659eeb6ddd5c3.txt
=== Geu 2 in book ===
data/extracted/batch/page-177.json
data/extracted/batch/page-178.json
data/extracted/batch/page-184.json
data/extracted/batch/page-51.json
```


## [2026-09-05T21:05:26.396Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in 5319383a3fbbea25 c87feae09c42b9ca 6531b72b39d782da 255659eeb6ddd5c3; do\necho \"######## $f\"; grep -n -A6 \"^ Etymology$\" $f.txt | sed -n '1,40p'; done\necho \"######## auger\"; sed -n '1,40p' 915db67d5c48cafa.txt | head -40"
}
```


### [2026-09-05T21:05:28.416Z] TOOL RESULT

```
######## 5319383a3fbbea25
######## c87feae09c42b9ca
148: Etymology
149- [ edit ] 
150-
151- From Middle Persian [Book Pahlavi needed] ( ʾp̄zn' /⁠ābzan⁠/ ) . Compare Classical Syriac ܐܘܙܢܐ ( ʾāwzānāʾ ) , Old Armenian աւազան ( awazan ) , Old Georgian ავაზანი ( avazani ) , Georgian აბაზანა ( abazana ) , Aghwan 𐔰𐕛𐔰𐔵𐔰𐕎 ( avazan ) , all Iranian borrowings.
152-
153- This etymology is missing or incomplete. Please add to it, or discuss it at the Etymology scriptorium . 
154-Particularly: “What's the further origin? Is the first component آب ( āb , “ water ” ) ? If so, what's the second component? However, if truly related to آوازه ( âvâze ) , IE etymology becomes less viable.”
######## 6531b72b39d782da
159: Etymology
160- [ edit ] 
161-
162- Borrowed from Arabic سَفِينَة ( safīna , “ ship ” ) , borrowed from Aramaic סְפינִתָּא / ܣܦܻܝܢܬܳܐ ( sǝp̄īntā ) .
163-
164- Noun
165- [ edit ] 
--
205: Etymology
206- [ edit ] 
207-
208- Borrowed from Arabic سَفِينَة ( safīna ) .
209-
210- Pronunciation
211- [ edit ] 
######## 255659eeb6ddd5c3
######## auger
URL: https://www.etymonline.com/word/auger
FETCHED: 2026-09-05T21:05:22Z
STATUS: 200
TITLE: Auger - Etymology, Origin & Meaning

Auger - Etymology, Origin & Meaning 

 Search 
 Log in 

 Columns 
 Forum 
 Apps 
 Premium 

 Log in 

 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of auger 

 auger (n.) 

 "instrument for boring larger holes," c. 1500, a faulty separation of Middle English a nauger , from Old English nafogar "nave (of a wheel) drill," from Proto-Germanic *nabo-gaizaz (source also of Old Norse nafarr , Old Saxon nabuger , Old High German nabuger ), a compound whose first element is related to nave (n.2) and whose second is identical to Old English gar "a spear, borer" (see gar ). For similar misdivisions, see adder . The same change took place in Dutch ( avegaar , egger ).
 also from c. 1500 

 Entries linking to auger 

 adder (n.) 

 Middle English naddre , from Old English (West Saxon) næddre (Mercian nedre , Northumbrian nedra ), "a snake; the Serpent in the Garden of Eden," from Proto-Germanic *naethro "a snake" (source also of Old Norse naðra , Middle Dutch nadre , Old High German natra , German Natter , Gothic nadrs ), from PIE root *nētr- "snake" (source also of Latin natrix "water snake" (the sense is probably by folk-association with nare "to swim"); Old Irish nathir , Welsh neidr "snake, serpent").

 The modern form represents a faulty separation 14c.-16c. of a nadder into an adder , for which see also apron , auger , nickname , orange , humble pie , aitchbone , umpire . Nedder is still a northern English dialect form.

 Since Middle English the word has been restricted to use as the common name of the viper, the only venonous British reptile (though not generally fatal to humans), then by extension it was applied to venomous or similar snakes elsewhere ( puff-adder , etc.). Folklore connection with deafness is via Psalm lviii.1-5. The adder is said to stop up its ears to avoid hearing the snake charmer called in to drive it away.

 gar (n.) 

 pike-like fish, 1765, American English, shortening of garfish (mid-15c.), from fish (n.) + Middle English gare , gore "a spear," from Old English gar "spear," from Proto-Germanic *gaisa- "spear" (source also of Old Norse geirr "spear; point of an anvil," Old Saxon, Old High German ger , German Ger "spear"), from PIE *ghaiso- "a stick, spear" (see goad (n.)). The fish so called for its long sharp snout. Compare Edgar , garlic .
```


## [2026-09-05T21:05:38.713Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"### garlic\"; grep -n -A6 \"garlic (n.)\" 249dc1dea84bd00a.txt | head -20\necho \"### fasan\"; grep -n -i -A6 \"Etymology\" 5319383a3fbbea25.txt | head -40"
}
```


### [2026-09-05T21:05:38.768Z] TOOL RESULT

```
### garlic
23: garlic (n.) 
24-
25- "onion like bulbous plant allied to the leek, known to the ancients and much used in cookery," Middle English garlek , from Old English garlec (West Saxon), garleac (Mercian), "garlic," from gar "spear" (in reference to the clove), see gar , + leac "leek" (see leek ). Garlic-bread is attested by 1947.
26-
27- Entries linking to garlic 
28-
29- gar (n.) 
### fasan
```


## [2026-09-05T21:05:40.939Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py \"https://www.etymonline.com/word/Roger\" --note \"page 184: Germanic *gaizaz in personal names Roger/Edgar/Oscar/Gerald\" >/dev/null\npython3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/%D8%A7%D9%81%D8%B3%D8%A7%D9%86\" --note \"page 184: Persian afsan/apsan whetstone\" >/dev/null\nls -t data/verification/sources/web/*.txt | head -2"
}
```


### [2026-09-05T21:05:43.533Z] TOOL RESULT

```
data/verification/sources/web/657515b947e1865b.txt
data/verification/sources/web/948e410ad33a4015.txt
```


## [2026-09-05T21:05:46.263Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"### afsan\"; grep -n -B3 -A8 \"Etymology\" 657515b947e1865b.txt | head -40\necho \"### Roger\"; grep -n -A5 \"Roger\" 948e410ad33a4015.txt | head -20"
}
```


### [2026-09-05T21:05:46.319Z] TOOL RESULT

```
### afsan
### Roger
1:URL: https://www.etymonline.com/word/Roger
2-FETCHED: 2026-09-05T21:05:42Z
3-STATUS: 200
4:TITLE: Roger - Etymology, Origin & Meaning of the Name
5-
6:Roger - Etymology, Origin & Meaning of the Name 
7-
8- Search 
9- Log in 
10-
11- Columns 
--
21: Origin and history of Roger 
22-
23: Roger 
24-
25- masc. proper name, from Old French Rogier , from Old High German Hrotger , literally "famous with the spear," from hruod- "fame, glory" + ger "spear" (see gar (n.)). "The name was introduced from Norman where OG Rodger was reinforced by the cognate ON Hroðgeirr " [Dictionary of English Surnames]. Pet forms include Hodge and Dodge . As a generic name for "a person," attested from 1630s. In 16c.-17c. cant, "a goose." Slang meaning "penis" was popular c. 1650-c. 1870; hence the slang verb sense of "to copulate with (a woman)," which is attested from 1711.
26-
27: The use of the word in radio communication to mean "yes, I understand" is attested from 1941, from the U.S. military phonetic alphabet word for the letter -R- , in this case an abbreviation for "received." It is said to have been used likewise by the R.A.F. since 1938. " Roger de Coverley ," once a favorite English country dance, is said to have been so called from 1685. Addison took him early 18c. as the name of a recurring character in the "Spectator."
28-
```


## [2026-09-05T21:05:53.641Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(t):\n    if 'افسان بروزن' in p or 'افسان  بروزن' in p:\n        print(\"leaf\",i,\"printed ~\",i-215)\n        print(p[:3500]); break\nEOF"
}
```


### [2026-09-05T21:05:55.388Z] TOOL RESULT

```
leaf 364 printed ~ 149
آفری
کشوث و نخم آنرا بذرالکشوث خوانند . فواق
را تافع است .
افری فتح اول وثانی بروزن سفری »
مخفف آفرین است که دد مقام تصی نگوند .
و بسکون انی هم درست است .
افر یدون ‏ - فربدونباشد. واویادشاهی
بوده. ءشهوره ویستی گویند افربدون نوح علیه ب
اللام است ۰ و بعضی ذوالقرنین اعظم او را
صسدانند ۰
اقفر پسموسش_ » بسکون سی‌بی نفطه
وم حیموواو وسین دیکرساکن, پیونانی؟ مرضی
است که مردانرا بهم میرسد و آن شدت تعوظ
است بعنی بوسته لت مردی ایستاده هیباشد ۰
وباسقاط همرز ه ی شت. -
گویندمقراض کرده وسوخته| تر | درمعاأجین‌خوردن
عفن را فربه سازد .
افز | ح بفتح اول‌بازای هوز بروزن‌اجزا»
1 ۱۳ اسج ۰
افز اد ه بر وزن رفتار , بمعنی کفش
ویای افزار باشد - وبادبانکشتی را نیز گویند -
والات مشهوران باشد عموماودفتن جولاگانرا
را کربند خصوصا ‏ وادوبة کرمی که در طعام
کنند همجو فلفل و دارچنی و ژبره و مانند
آن۴ .
۹ م2 : فربدون و آفربدون.
۳ ‌- ره 4 ابریشم.
4
افژ ول با زای قلرسی بروزن مقبول.
بمعنی تقاضا وانگیز باشد - و بمعتی پریشان هم
۳ ات ِ
افو لته » بر وزن افروزنده . بر
انگیز نده وتان را گویند - ویمعئی‌دود
کننده مویریشان سازنده م امه احست.
افو لین « بروزن افروزیدن.بمعنی
پرانگشتن بجشگه - وبرس رکارآوردن - وقانا
نمودن - ویریشان ماختن - و دور کردن هرچیز
باشد خصوصا کرد یکه برجامه نشیند .
ا فقس - پاسین‌بی‌نقطه بروزن‌ترساه بمعنی
رام کننده وافونگر باشد .
افسار » بر وزن رفتاد . بمعنی فا
ابت که افونگر و رام کننده باشد - وچیزی را
گون دکه از چرم ومانند آن سازند ویرسراسب
هنکن تافقال .اي تن
افسان بروزن ترسان . آهنی‌وسنگی
را کوش دکه بدان د وخمفی و عانتد ان کر
کنند - وبمعتی افسائه وسر گذشت هم گفته‌اندب
واضوشگررا فز گوید :
وحکامات گذنتگان باد - و مشهور و شهرت
بافثه شده را یز گوبند .
اقسای - با بای حطی بر وزن لبلای .
افونگر و رام کننده را گویند. واقسافیدن رام
کردن را ۰
اقسر ۷ بروژن برسر. بممنی‌تاج باشد
22لا ,۵52 « واثه ناید ۷د ۶ رل : اقفر .
۱ - از: اوستایی 211 یشوند (به - بر)
7 « ثبر که ۷۰ » . رك : افار .
```


## [2026-09-05T21:05:55.951Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON safineh ===\"; grep -n \"سفینه\\|سفينه\" MON_part1.txt MON_part2.txt 2>/dev/null | head -5\necho \"=== ARY zin ===\"; grep -n \"زین\\b\" incoming/ARY/ARY_pages.txt | head -8\necho \"=== ARY afzar ===\"; grep -n \"افزار\" incoming/ARY/ARY_pages.txt | head -5"
}
```


### [2026-09-05T21:05:56.037Z] TOOL RESULT

```
=== MON safineh ===
MON_part2.txt:8602:فلی: ۸ [ع.] (.) کشتی؛ سفینه. 
MON_part2.txt:23307:و بار و مسافر را حمل کند؛ سفینه» زورق» 
MON_part2.txt:23332:سفینه سازند. کشتی باده: پل شرابخوری به 
MON_part2.txt:23333:شکل سفینه. کشتی دریافشان: پیالهٌ شراب. 
MON_part2.txt:71411:کشتی (سفینه)» خداوند کشتی. آنکه ادار ة 
=== ARY zin ===
108:سرزمین آغازین هند و اروپائیان
124:واژه‌های هند و اروپایی آغازین (۳۳070-18700-218078۸31) وابسته به جانوران و گیاهانی
126:دیسدمان دیگر در باره‌ی گهواره‌ی آغازین هند و اروپایی‌ها این است که زادگاه
172:زبان‌های گوناگون شد. (وجود واژه‌های مشترک میان هند و اروپایی و زبان سامی آغازین
269:آغازین بوده‌اند. آنها این واژگان و ویژگی‌های زبانی دیگر را با خود به سرزمین‌های دیگر بردند و دد,
284:دیرین‌شناسی زبانی وسیله‌ی دیگری است برای شناخت هند و اروپایی آغازین و خاستگاه ۱
667:جایگزینی زبان ترکی شدء بطوری که امروزه زبانهای ایرانی در سرزمین‌های خاور دریای خزر و
1265:زین هم پژوهشگران آینه بناندکاری راک این کتاب آغازکرده است دابا لکند و جایگاه استین
=== ARY afzar ===
```


## [2026-09-05T21:06:13.268Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"garlic\" KLN_1966.txt | head -5\necho \"---\"\ngrep -n \"gaesum\\|ghaiso\" KLN_1966.txt KLN_1971.txt | head -10"
}
```


### [2026-09-05T21:06:13.336Z] TOOL RESULT

```
2241:allanto-,  combining  form  meaning  ‘sausage’.  — Gk.  aXXocvTO-,  fr.  aXXag,  gen.  aXXavrix;,  ‘sau¬ sage’,  a  loan  word  fr.  L.  alium,  allium,  ‘gar¬ lic’,  the  orig.  meaning  of  Gk.  aXXa?  being ‘garlicky  (sausage)’.  Ion.  4 XXr),  glossed  by  He- sychius,  and  rendered  by  him  with  Xir/avov (‘greens,  vegetables’),  is  of  the  same  origin.  See Allium.
2272:Alliaria,  n.,  a  genus  of  plants  of  the  mustard family  (hot)  —  ModL.,  fr.  L.  allium,  ‘garlic’ (see  Allium) ;  so  called  with  reference  to  its  odor, allice,  allice  shad,  n.  —  F.  alose,  fr.  L.  alausa, ‘shad’.  See  alese.
2278:Allium,  n.,  a  genus  of  herbs  of  the  lily  family ( hot .)  —  L.  alium,  allium,  ‘garlic’,  prob.  cogn. with  OI.  dtuh,  alukdm,  ‘bulb’.  Accordingly  alium would  lit.  mean  ‘the  bulbous  plant’.  There  is little  probability  in  Vanicek’s  suggestion  to  ex¬ plain  alium  as  ‘the  strong-smelling  plant’,  by deriving  it  from  the  base  *an-,  ‘to  breathe, smell’.  Cp.  alliaceous,  Alliaria.  Cp.  also  allanto-. Cp.  also  the  first  element  in  allyl. alio-,  combining  form,  meaning  ‘other’.  —  Gk. dtXXo-,  fr.  aXXop,  ‘another,  other’,  which  stands for  *aXioc,  and  is  cogn.  with  L.  alius,  ‘an¬ other’.  See  alias.
2312:allyl,  n.,  a  univalent  radical,  C3HS  ( chem .)  — Formed  with  suff.  -yl  fr.  allium,  ‘garlic’  (see  Al¬ lium)  ;  so  called  because  it  was  first  obtained  as a  disulfide  from  garlic  (by  Wertheim  in  1844). Alma,  fern.  PN.  —  Lit.  ‘nourishing’,  fr.  L.  alma, fern,  of  almus,  fr.  alere,  ‘to  nourish’.  See  aliment and  cp.  Alma  Mater.
3080:the  sea)’  is  folk  etymology.  For  the  change  of  sh to  9,  cp.  Heb.  shiim,  Arab,  thum,  VArab. fum,  ‘garlic’,  Heb.  gadtsh,  Arab,  jddath,  VArab. jadaf,  ‘mound,  tumulus’,  and  the  Russian  PN. Feodor,  which  derives  fr.  Gk.  0s68<opo4  (see Theodore).  Cp.  Ashtoreth,  Astarte,  Ishtar.  Cp. also  April.
---
KLN_1971.txt:104106:L. gaesum , ‘a long heavy javelin’, Olr. gae , 
KLN_1966.txt:16368:goad,  n.  —  ME.  gode,  fr.  OE.  gad,  ‘point,  sting, goad,  arrow’,  rel.  to  Lombard  gaida,  ‘spear’, and  cogn.  with  OI.  hetih,  ‘missile,  projectile’, hdyati,  hinSti,  ‘pushes  on,  hurls’,  Avestic  zaina-, ‘weapon’,  Gk.  x«ioc,  ‘shepherd’s  staff’,  Gaul.- L.  gaesum,  ‘a  long  heavy  javelin’,  OIr.  gae, ‘spear’,  OE.  gar,  ‘spear’,  Du.  gesel,  OHG. geisila,  MHG.  geisel,  G.  Geiffsl,  ‘whip,  lash’.
```


## [2026-09-05T21:06:25.469Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"zēn \\[\\|zēn\\b\" NYB_vol2_glossary.txt | head -10\necho \"--- abzar in NYB ---\"; grep -n \"abzār\\|apzār\\|avzār\" NYB_vol2_glossary.txt | head -5\necho \"--- zay ---\"; grep -n \"^zay\\|zay \\[\" NYB_vol2_glossary.txt | head -5"
}
```


### [2026-09-05T21:06:25.539Z] TOOL RESULT

```
413:Amahraspands 397-8; an amäh u Pw!] Gi 6 ham tuxšem [this reading should. be restored] andar äp, andar damik, andar urvar, andar gospand we and he will labour jointly in water, soil, plants, cattle 3915-16; an-ip to ... fräc vēnēnd for thee (dat. ethicus: thou mayest know:) they prophesy ... 51% (v. tē and -p); an 6 amäh asp vāzēnēt you there, bring the horse here to us 541° (cf Spanish nosotros, vosotros); an či gäv that (re- markable) bull 427. 49?-5-18-19; ang [ZK-y] či asp that (remarkable) horse 491’; an če that very man 5419; an alone for the Ist p. sg., v. the next w. — Av. (135 sqq.) anya-, ainya-, OP aniya-; MPrth ny; MPrs ^», "ny ‘another’ (also = 2an); Paz. han, with -c: hanica. In J-Prs hm, ’ny emphasizing a pron. as described above, v. Mackenzie, An early Jewish Persian argument (BSOAS XXXI, 1968, 249-269), L, 1. 14 (p. 262): whny "wy dd dyh ‘and He is the lawgiver’ (hesitatingly combined. with ^ny by M. p. 254); Utas, The Jewish- Persian fragment from Dandàn-Uliq, Or. Su. XVII, 1968 (1969), 129, 1. 13: ny man simply = ‘T, Ll 4: ny mr = anë mara ‘for me’. — Cf also änöd and. enyä.
3847:ulēh [L’L’-yh], wë [+ -c: D’L’y-c] up- wards, above: pat uléh emphasizing the prev. ul in pat uleh ul nikérit 51%*-*%; pat uleh ul vāzēnēm 60°; — ule-c on high 42). - Cf Av. (351) loc. orodvaya ‘in upright, standing position’; cf also nıküneh.
4059:vizčnitan [w’cynytn'] to bring, to take a p. to a place (andar) 49?’; to lead (a horse) up to (0) a p. 5413-15; à tē pat ulēh ul vāzēnēm we shall carry thee up in the air 60%. — Caus. of väzitan.
4060:vāzēnītār one who draws, pulls: asp i rahy ~ a chariot-horse 581”.
4537:zēnāvandihā [zyn’wndyh?] vigilantly 6713. — From zēnāvand, Av. (1651) začnahvant- ‘vigilant’.
4538:zēn-dān [zynd’n'] prison 93. 11625 (twice). — “Keeping-place of arms" = ‘arsenal’,
5469:zaēnahvant-: zēnāvan- dihā
5470:zaēnu-: zēn
--- abzar in NYB ---
558:apa-zär [’pz’l] 1. adj. mighty: —-góspand whose cattle is powerful 588-13, 6014. — 2. subst. power, predominance 84°; cos- mic, heavenly force 89?7, 922. 1061; mili- tary forces 121157; — ~ u frahang power and teaching powerful teaching 108!%-!!; nök- having new force, renew- ed 1122-12, — < *upa- (or api-, v. apa-) züvar, v. zävar and zor; MPrs ’bz’r, hw?bzr *very mighty'. Often confounded with the late form avzār < apacār (g. v.), hence the erroneous Skr. renderings by Sastra ‘arms’ (Mx, SGV, but 845 sädhana). — FrP, Cod. P, fol. 7^, with the NP gl. qudrat.
--- zay ---
4534:zayišn [YLYDWN-8n'] birth 36%. 44-47 passim, ete.; — subst. one who is to be
```


## [2026-09-05T21:06:36.382Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== NYB apacar ===\"; grep -n \"apacār\\|apacar\\|avzār\" NYB_vol2_glossary.txt | head -5\necho \"=== HRN zin Sattel ===\"; grep -n \"Sattel\" HRN.txt | head -10\necho \"=== HRN zinhar/zin entries ===\"; grep -n \"zTn\\|zin 'S\\|zïn\" HRN.txt | head -10"
}
```


### [2026-09-05T21:06:36.447Z] TOOL RESULT

```
=== NYB apacar ===
558:apa-zär [’pz’l] 1. adj. mighty: —-góspand whose cattle is powerful 588-13, 6014. — 2. subst. power, predominance 84°; cos- mic, heavenly force 89?7, 922. 1061; mili- tary forces 121157; — ~ u frahang power and teaching powerful teaching 108!%-!!; nök- having new force, renew- ed 1122-12, — < *upa- (or api-, v. apa-) züvar, v. zävar and zor; MPrs ’bz’r, hw?bzr *very mighty'. Often confounded with the late form avzār < apacār (g. v.), hence the erroneous Skr. renderings by Sastra ‘arms’ (Mx, SGV, but 845 sädhana). — FrP, Cod. P, fol. 7^, with the NP gl. qudrat.
=== HRN zin Sattel ===
11376:Für np. zm 'Sattel' scheint sich in der älteren Sprache
=== HRN zinhar/zin entries ===
4747:halte dich von diesem zurück', wovon dann zTnharT
```


## [2026-09-05T21:06:39.265Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '11360,11400p' HRN.txt\necho \"--- leaf/page ---\"\nawk 'NR<=11376{n+=gsub(/\\f/,\"\")} END{print \"formfeeds before:\",n, \"-> printed page ~\", n-21}' HRN.txt"
}
```


### [2026-09-05T21:06:41.029Z] TOOL RESULT

```
aw. zaya- 'Waffe'.— M)2 —
237. xayltan 'hitten\ AW.-Komm., PPP. zast (kaum 2:aylt),
ap. x^jad-, jadiyamiy ^bitten'; aw. [/^jad-^ jaidyemi
'bitten.
238. ^and 'Gau, zandpat (AW.-Komm.).
aw. zantU'^ zantupaiti- 'Gau, Gauherr.
239. i^amj Tuss', AW.-Komm., Bund.; arm. LW. zangapmu
zankapan (de Lagarde, No. 752).
aw. zanga- 'Knöchel'; ai. jängha- unteres Bein*.
af/. zanymi Knie': oss. zängä 'Knie' (126).
Ein np. serjeng 'Ferse*, das de Lagarde auch
Armenische Studien No. 752 wieder anführt, giebt es
nicht; serce^ig bedeutet nur 'Fusstritt, Puff*.
240. zen 'Waffe', AW.-Komm., Men. 43, 7 (päz. zm\
zmavand (Aogem.).
aw. zaena- 'Waffe*; arm. LW. zen ottAoi/, aidrjQoq.
Für np. zm 'Sattel' scheint sich in der älteren Sprache
keine Anknüpfung zu finden; aw. zainis, phlv. zTrty
bedeutet wohl nicht 'Köcher (Geiger, Yätkär-i
Zarirän, S. 52 Note 19) und zainLparsta- ist ganz
unsicher.
241. i^tnitan 'wegnehmen'; zlmtär (ZPGL). Selten.
ap. [/^day-, adfnam 'ich nahm weg, aw. i^zay-, zinaf;
ai. i^jyä', jindti 'überwältigen, unterdrücken' (vergl.
Hübschmann, Casuslehre 192 Anm. 2, Fick'* I,
216).INDICE8.Mit Ausnahme der altpersischen , awestisolien und altindisohen
Formen sowie der in hebräischen Buchstaben geschriebenen Worte sind
die Indices nach der Folge des lateinischen Alphabetes angeordnet
worden. Ein N. nach einer Zahl, welche stets die einzelnen Artikel
nicht die Seiten bezeichnen, bedeutet, dass das betreffende Wort in den
Nachträgen vorkommt; römische Zahlen weisen auf die Vorrede. Zahlen
in Cursivdruck gehen auf das *Verlorene Sprachgut*. Längen und
Kürzen der Vokale sind nur für die altarischen Sprachen in den Indices
geschieden; doch ist auch in den neuiranischen ä von a im Anlaut
getrennt, während sonst e überall gleichmässig mit li rangirt. Auch s
und 9, g und y, k und xi ** und /r, z und z sind in den letzteren meist
nicht von einander getrennt.
Nenpersisch.
ä-, ä 1, 02, 694.
ab% 3.
abäd 4.
--- leaf/page ---
formfeeds before: 323 -> printed page ~ 302
```


## [2026-09-05T21:06:58.263Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"Wetzstein\" HRN.txt HUB.txt AFA.txt | head -10"
}
```


### [2026-09-05T21:06:58.314Z] TOOL RESULT

```
AFA.txt:5936:Etymologieen hat Wetzstein Ztschr. für Ethnologie 1882.
AFA.txt:7581:kannt — nichts als persisch ^L^Jf »Wetzstein". Dasselbe
HUB.txt:487:98. Afgh. p'san 'Wetzstein (Raverty) ist LW. wegen -an
HUB.txt:2705:752. Vgl. san und afsan 'Wetzstein'.
HUB.txt:6127:afsan 'Wetzstein* = fasan H. 98; afsurdan *frieren' = fu-
HUB.txt:6278:arm. ambar\ canbar 'Kreis' (? H. 446); siinbada *Wetzstein*
HUB.txt:6468:afsCLn^ avsan *Wetzstein' H. 98; afsar Krone H. 99, oben
HUB.txt:7471:afsan *Wetzstein , afsar 'Krone', pdsux *Antwort\ pasand
HRN.txt:1276:98. efsän 'Wetzstein', eusän,^) fesän, vergl. sün,
HRN.txt:1279:wa;f. sar. pasän ^Wetzstein'.
```


## [2026-09-05T21:07:13.206Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '1270,1290p' HRN.txt\necho \"=== HUB 98 ===\"; sed -n '483,495p' HUB.txt\necho \"=== HRN san ===\"; grep -n \"^..*sän 'Wetz\\|sun 'Wetz\" HRN.txt | head; grep -n \"1054\\. \\|sän,\" HRN.txt | head -3"
}
```


### [2026-09-05T21:07:13.290Z] TOOL RESULT

```
aw. "^aiwi + \/ snv-, sävaijät 'er wird nützen';
phlv. afzütan^ ofzün^ afzüntk^ afzäyltan, afzäyimtan,
afzäy(i)sn,
97. efsär 'Zügel, Zaum', ßsar.
aw. ^aiwisdra-; phlv. afsdr (Bund.),
syr. talmüd. LW. 1DCN.
98. efsän 'Wetzstein', eusän,^) fesän, vergl. sün,
phlv. afsän (Säy. Näääy. 10, 28); skr. gäna-^) 'Wetz-
stein* + abhi; vergl. B.rm. yesan (H. No. 211).
wa;f. sar. pasän ^Wetzstein'.
99. efser 'Krone'.
aw. ^aiwisara-; phlv. afsar 'Krone' (6ö§t-T Fr.)^).
100. efsurden 'frieren', gefrieren, fusurden^ ßsurden
(Sahn. I, 78 Vers 211).
phlv. afsartan, afsar(i)smh (vd. 19, 12), vergl. arm.
surf, 'Kälte'.
Siehe np. serd (No. 731).
101. efsös 'Spott, Scherz', fisös,
phlv. afsös 'Spott, Scherz'.
Darmesteter's Erklärung, Et. ir. II, 131 aus aw.
*aiwisaoca' ist unhaltbar, da aw. d im Np. nicht zu s
=== HUB 98 ===
anzuknupfen, wie auch andere Gelehrte thun.
i— 17 —
*vor warts drS,ngen, fordern', caus. jdvayati, ptc. juta-
^= np. zud schneir stellen l§.sst.
98. Afgh. p'san 'Wetzstein (Raverty) ist LW. wegen -an
(fiir afgh. -ww).
99. Np. afsar *Krone' — ap. ^abisarah- *um den Kopf liegt
im Sanskrit vor als abhigiras-, aber mit der Bedeutung :
*den Kopf richtend nach-, zum Kopfe gerichtet'. Horn
vergleicht mit Recht phi. aparsar (= auf dem Kopfe'
d. i.) *Diadeni, Krone' fiir zd. pws5- ZPQI. 24 (= arm.
psak 'Diadem, Krone, Kranz').
100. Arm. j^surt" in ^rt *kalt' zu verbessern.
=== HRN san ===
1276:98. efsän 'Wetzstein', eusän,^) fesän, vergl. sün,
1276:98. efsän 'Wetzstein', eusän,^) fesän, vergl. sün,
6480:kurd. seh (d. i. se) *Hund', Plur. sän, seiän; afy. spai.
7418:851. kes 'jemand', kesT {*kese), kesän,
```


## [2026-09-05T21:08:11.120Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== WLD Bd1 gaiso p528 ===\"; grep -n \"ghaiso\\|gaiso\\|zaena\\|zaēna\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -10\necho \"=== FVQ arabic safina ===\"; grep -c \"\" FVQ_pages.txt; grep -n \"سفين\\|سَفِين\" FVQ_pages.txt | head -5\necho \"=== FVQ sakinah ===\"; grep -n -i \"sakina\\|Sakinah\" FVQ_pages.txt | head -3"
}
```


### [2026-09-05T21:08:11.192Z] TOOL RESULT

```
=== WLD Bd1 gaiso p528 ===
727:2, 141, Bechtel Lexil. 177 f.) ay. izaena- oder Izaena- „aus Leder“ (eigent- 
33201:ghais- — ghaisos 
33237:ghaisos „Stecken, auch als WurfspieB“ (bei Zugehorigkeit von ai. hesah 
34348:ist es, aucb *ghaiso-s „Ger“ (s. d.) mit unserem ghei- zu vereinen, da 
34356:sein, Wachsein', memvjhau- (von einem *zaenali- n.) „wachend, wachsam“: 
34927:., Speer - usw. (s. u. ghaisos ); dieser Annahme ist auch kelt. ei (ir. ia, cymr. 
=== FVQ arabic safina ===
12582
=== FVQ sakinah ===
398:Tawral^ Injll, Sakina, Firdaus, Jahannam, are equally familiar to all
6392:ideogram 11114 33 sakina, 5 so that an Aram, origin of the Arabic
```


## [2026-09-05T21:08:12.613Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 -c \"\nimport json,glob\nfor f in ['data/extracted/batch/page-177.json','data/extracted/batch/page-178.json']:\n    d=json.load(open(f))\n    for e in d['entries']:\n        print(f, e['root'].get('name'), e['root'].get('gloss'), e['root'].get('refs'))\n\" | grep -i geu"
}
```


### [2026-09-05T21:08:14.245Z] TOOL RESULT

```
data/extracted/batch/page-177.json Geu 2, Geua to hasten POK:399
data/extracted/batch/page-178.json Geu 3, Gyeu, Gieu to chew POK:400
data/extracted/batch/page-178.json Geua None None
data/extracted/batch/page-178.json Geulo None None
data/extracted/batch/page-178.json Geus to love, favor, choose POK:399
```


## [2026-09-05T21:08:21.730Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '34340,34375p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt\necho \"=== ghaisos entry ===\"; sed -n '33230,33250p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt"
}
```


### [2026-09-05T21:08:21.787Z] TOOL RESULT

```
nachgeben. schwanken' - , zichljatb „ins Schwanken bringen“? 

Ygl. Yanicek 85, Fick I 4 408, III 4 43, Liden aaO., Persson aaO. 

1. gliei- „antreiben, lebhaft bewegen (schleudern) oder bewegt sein“; „(ge- 
schleudertes) GesehoB"; von der Bed. .,Gescbob“ oder allenfalls verbal 
„wonach schleudern, treffen" kann ,,verwunden" (Gruppe B) ausge- 
gangen sein (Wzf . yhei-s-); wegen des Yokalismus nicht unbedenklicb 
ist es, aucb *ghaiso-s „Ger“ (s. d.) mit unserem ghei- zu vereinen, da 
dies im Ai. durchaus den Ablaut einer leichten Wz. zeigt. Ygl. noch 
qlieis-, yheisd- „aufgebraclit sein ‘. 

Ai .hinoti, Mnvofi, layati ,,treibt an, schleudert", Ptc. Intd-lr, heman- n. 
„Eifer‘; hett-li m. „GeschoB" (vgl. germ. *gaida ); 

Av. zacni- „reg, eifrig", zaeman- „regsam, waeb“, n. „Regsamkeit, Munter- 
sein, Wachsein', memvjhau- (von einem *zaenali- n.) „wachend, wachsam“: 
sacna- m. „Waffe“, zaya- m. „(*Waffe), Gerat, Ausriistungsgegenstand' 1 , 
zayan- ,,bewaffnet - '. 

Aucb ai. hnya-h „Ro6 ‘, arm. ji ds. hierher als „das lebhafte"? eine 
andere Deutung u. glut ,,fehlen“; langob. gaida f. .. Speer", ags. gad „Stachel, 
Spitze, Stecken''. 

B. ylieis- ,,verwundeir‘ : ai. hr-ia-h n. „Gescho£l“ (kann aber auch idg. 
*7 haisos sein. s. d.); dazu wahrscbeinlicb (s. Wackernagel Ai. Gr. I 44, 
Guntert IF. 30, 10611'., Bgm. II 2 3, 27b) hisati (erst nacbved. hindsti) 
„scbiidigt, verletzt" ; 

air. goife ,,vulneratus“, mir. gaetas „qui occidit - ' ( *yhoizd-\ Fick II 4 
113; anders, aber scbwerlicb zu rechtfertigen, Pedersen KG. I 494, 
II 54Sj ; 

lit. zeidziu, ".eidziaB, ze'isti „verwunden“, zaizdd „Wunde“. Dieselbe d- 
Erw. bei yhcis : glieizd- „aul'gebracht". 

=== ghaisos entry ===
got. qistjan „verderben“ gehoren (Fick aaO., Ill 4 63, Wood aaO.; andere 
Deutungen siehe bei Boisacq 856 und u. g'ieclh- „stoBen“, g'ics- „l6schen“), 
aber fiir lit. galsti (wenn iiberhaupt ein von g. „saumen“ verschiedenes 
Wort) ware dessen a-Yokalismus (idg. oiVi) nicht leicht zu nehmen. Zu- 
dem ist der Vergleich von galsti mit lit. fiaio? in der Bed. sehr vage 
(Kretschmer Gl. 6, 305). 

ghaisos „Stecken, auch als WurfspieB“ (bei Zugehorigkeit von ai. hesah 
— allerdings neutr. -es-St. — mit gh- anzusetzen; liber die vokalische 
Schwierigkeit der Yermittlung mit ghei- „antreiben“ s. d.). 

Ai. hesah n. „GeschoB“ (doch s. u. ghei- „antreiben“); 

gr. %aio g „Hirtenstab“; gall. -lat. gaesum, gall.-gr. yaloov „schwerer eiserner 
Wurfspie6“ ( gaesatl ,.gall. Soldtruppen"), air. gae „Speer“ {guide „pilatus“\ 
fo-gae , mir. fo-ga, fo-cha „WurfspieB“ = cymr. gwaew (siehe dazu Stokes 
KZ. 33,77, Thurneysen IA. 26, 25, vgl. auch abret. guu-goiou „spiculis, telis“, 
Bezz. BB. 17, 139); 

ahd. as. ger, ags. gar, aisl. fteirr „Wurfspeer“.
```


## [2026-09-05T21:08:22.971Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 -c \"\nimport json\nd=json.load(open('data/extracted/batch/page-177.json'))\nfor e in d['entries']:\n    if e['root'].get('name','').startswith('Geu 2'):\n        print(json.dumps(e,ensure_ascii=False,indent=1))\" | head -60"
}
```


### [2026-09-05T21:08:24.718Z] TOOL RESULT

```
{
 "root": {
  "name": "Geu 2, Geua",
  "lang": "Indo-European",
  "refs": "POK:399",
  "gloss": "to hasten"
 },
 "nodes": [
  {
   "id": 1,
   "parent": 0,
   "lang": "Avestan",
   "refs": "POK:399; BQT:148",
   "words": [
    {
     "translit": "zavah, zâvar",
     "gloss": "power, force",
     "script": null
    },
    {
     "translit": "api-zâwar",
     "gloss": "tool",
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
   "refs": "POK:399; BQT:148; HRN:149",
   "words": [
    {
     "translit": "zŭr 1",
     "gloss": "force, power",
     "script": "زور ۱"
    },
    {
     "translit": "zâvar",
     "gloss": "power, force",
     "script": "زاوَر"
    },
    {
     "translit": "zâv",
     "gloss": "powerful, strong",
     "script": "زاو"
    },
    {
     "translit": "abzâr, afzâr",
     "gloss": "tools",
     "script": "ابزار ، افزار"
    }
   ],
   "script_extra": null,
   "note": "For a different derivation of \"abzâr & afzâr\" see root \"Ghei 2\".",
   "quote": null
  },
```


## [2026-09-05T21:08:37.795Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('FVQ_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(\"leaves:\",len(t))\nfor i in (187,188,189):\n    print(\"==== leaf\",i,\"printed ~\",i-17)\n    print(t[i][:900])\nEOF"
}
```


### [2026-09-05T21:08:39.533Z] TOOL RESULT

```
leaves: 335
==== leaf 187 printed ~ 170
170 FOREIGN VOCABULARY OF THE QUR'AN
Noldeke as early as 1860 l drew attention to the fact that the
noun Jb** seemed to be a borrowing from Vr4* = N"1BI2J, 2 so that
the verb, as Fraenkel, Fremdw, 250, notes, would be denominative.
The Aram. N"1D2? = 1;4* means a document, and is from a root
connected with Akk. satdru, to write. It occurs as "1ED2? in Nabataean
and Palmyrene inscriptions, 3 and in the S. Arabian inscriptions we
have )fflr 1 J to write, and ) III Ah inscriptions. 4 ' D. H. Miiller, WZKM,
i, 29, thinks that the Arabic may have been influenced both by the
Aramaeans of the north, and the Sabaeans of the south, and as a
matter of fact as-Suyutl, Itq, 311, tells us that Juwaibir in his comment
on xvii, 60, quoted a tradition from Ibn 'Abbas to the effect that
was the word used in the Himyaritic dialect for
The presence of the Phlv.j(jJ)^33s^re,as,e.g., in the ph
= in lines (PP
==== leaf 188 printed ~ 171
FOREIGN VOCABULARY OF THE QUR ? AN 171
Bekri, Mu'jam, 369, 18, we read of how a<J-Dahhak entered a Christian
monastery while the monk was reading #ju-*-i j* i^**-, and
Ibn Duraid, 103, says that Sifr means " the volume of the Torah or
the Injil or what resembles them ", 1
It is clearly a borrowing from Aramaic. 2 The common Heb. "15??
appears in Aram, as N"]9P ; Syr. ];W>- From Aram, it passed
on the one hand into Eth. as tl&, and on the other into Arm. as
un^fy. As the Arm. word seems to have come from Syr., 3 we may
suppose that it was from the same source that the Arabs got the word.
J x-
*'jA-~> (Safara).
Ixxx, 15.
^ i **
Scribes ; plu. of ^^?l *> (used of the heavenly scribes).
as-Suyuti, Itq, 321 (Mutaw, 60), tells us that some early authorities
1*1 M ^Mk^
said it was a Nabataean word meaning %\J*. Aram, ISO was a
scribe or secretary who accompanied the Governor of a Province
(Ezra
==== leaf 189 printed ~ 172
172 FOREIGN VOCABULARY OP THE QUR ? AN
The reference in xviii is to the boat used by Moses and al-Khi<Jr,
and in xxix to Noah's ark.
"* '* '
The lexicographers fancifully derive it from A +* to peel or
*>- '
pare (cf. LA, xvii, 72). This, however, is denominative from {j*-*"
an adze, which itself is not an Arabic word but the Pers. Ju~ 1 which
passed into Arabic through Jima. 1 Guidi, Delia Sede, 601, called
attention to the fact that Ai-jL* is a loan-word in Arabic, and the

Semitic root is doubtless ]E30 to cover in, which we find in Akk.
sapannu = concealment, Phon. 1132013 a roof, 2 and Aram. ]SO ; Heb.
]SO to cover.
The form HiTSO occurs in Heb. in the story of Jonah (Jonah i, 5), 3
and in the Talmud and Targums WSO and XWEJO are commonly
used. Even more commonly used are the Syr. ]i *>or> ]AlA2iflD, and
as both the al-Khidr and Null stories of the Qur'an seem to have
developed unde
```


## [2026-09-05T21:08:56.062Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"سفینة\\|سفینه‌\" MON_part2.txt | head -8\necho \"---\"; grep -n \"سفینه\" MON_part1.txt | head -8\necho \"--- context 23300 ---\"; sed -n '23300,23340p' MON_part2.txt"
}
```


### [2026-09-05T21:08:56.172Z] TOOL RESULT

```
23320:کشتی هوایی: بالن (بالون)» سفینة هوایی 
68242:سفینة فضایی یک دور کامل روی خود بز ند 
---
46687:رایج. (.) کشتی» سفینه. ماری از نوع افعی. 
48674:سفینه. بیاض بز رگ دفتری که در آن اشعار 
48675:و مسطالب دیگر نوسند؛ سفینه. آلبوم 
49171:سسفینه. چرح روفنگیری؛ ج. اجهزات» 
64449:بخواهد براند؛ نوعی سفینهة هوایی 
78313:سفینه: (6-)21102: [غ. سفننه] (.) کشتی. 
79446:سماری: [:078:(.) کشتی» جهاز» سفینه. 
--- context 23300 ---


کرده که بر شت شت آسته طلا کنند. کشته نفس: 
(تص.) آنکه نفس خود را به مصداق «موتوا 
قبل آن تمو توا» کشته. 
کشتی: -105 ,5۱1 (.) آلتی که روی آب به 
وسیله‌ای (پارو؛ بادبان» بخار و غیره) حرکت 
و بار و مسافر را حمل کند؛ سفینه» زورق» 
جهاز. ترکیبات اسمی: کشتی آتشی: کشتی 
بخار. کشتی بخار: کشتیی که به وسیلة بخار 
حرکت کند. کشتی جنگی: کشتیی که در 
حرب بکار رود؛ روزمناو. کشتی دریوزه: 
کاس گدایی که بصورت کشتی باشد. کشتی 
رونده صبح: (کد.) شتر» اشتر» بعیر. کشتی 
زره‌وش: کشتبی که اطرافش با زره مجهز 
است؛ کشتی زره‌دار. کشتی صحرا: ( کن.) 
و (کد.) دنیاء جهان. کشتی 
نگ رگیر: کشتبی که به سیب گراننی لنگر 
بجای خود ایستد. کشتی مسافربری: کشتیی 
نفت کش: کشتبی که خاص حمل نفت است. 
کشتی هوایی: بالن (بالون)» سفینة هوایی 
ترکیبات فعلی: کشتی به خشکک بستن: ( کن.) 
ممسکت بودن؛ بخیل بودن. بز دل بودن. 
کشتی بر < خشک راندن ( کشمدن): به ساحل 
رسانیدن کشتی. کشتی به ساحل ردن 
(رسانیدن): به ساحل رسانیدن کشتی. کشتی 
خود را دریایی کردن: (کد.) به کاری مهم - 
که پیشتر دربارة تردید داشتند مصمم شدن 
و اقدام کردن : کشتی دز آب افتادن: ( کد.) 
ضرق شدن از تیه آب افکندن 
(انداختن): کشتیی را که در خشکی ساخته 
شده داخل انب گنل پیاله‌ای که به شکل 
سفینه سازند. کشتی باده: پل شرابخوری به 
شکل سفینه. کشتی دریافشان: پیالهٌ شراب. 
کشتی زر: بباله‌ای که آن را از طلا به شکل 
سفنه سازند. (کد.) آفتاب؛ خورشید. (کذ.) 
ماه نو ء هلال. 


کشتی: 05۱7 (.) کستی. گلاو بز شدن دو 
تن با یکدیگر برای زورآزمایی و زمین زدن.
```


## [2026-09-05T21:09:12.298Z] AGENT

Now I have enough evidence. Writing the verification file.


## [2026-09-05T21:09:15.270Z] TOOL CALL #71: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg184.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/184.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | tail -3",
 "description": "Copy page image for audit"
}
```


### [2026-09-05T21:09:15.348Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r--  1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r--  1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
```


## [2026-09-05T21:16:46.729Z] TOOL CALL #72: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build184.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW = \"https://en.wiktionary.org/wiki/\"\n\nentry = {\n \"entry\": 0,\n \"root\": \"Ghei 2, Ghaise\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *ǵʰey- 'to impel, set in motion, hurl' (Pokorny 424-425, lemma ĝhei-1 with the s-extension ĝhei-s- 'to wound') together with the noun *ǵʰaysó- 'stick, spear' (Pokorny 410, ĝhaiso-)\",\n \"note\": \"The root box is right on all three counts, and both page numbers are exact. Pokorny 424-425 prints 'Root/lemma: ĝhei-1, ĝhei-. Meaning: to drive; to throw; to wound', section A 'ĝhei- antreiben' with Skt. hinóti 'set in motion, hurl', hetí- 'projectile' and precisely the Avestan material of this chart: 'zaēnah- astir, keen, eager, zaēman- active, awake, zaēnahvant- waking, watchful; zaēna- m. weapon, zaya- m. (*weapon), tool, piece of armament, zayan- armed'. Pokorny 410 prints 'Root/lemma: ghaiso- (or ĝhaiso- : gheiso-). Meaning: stick; dart' with Gaulish-Latin gaesum, OIr. gae, OHG/OSax. ger, OE gār, ON geirr (*gaizas) — so 'Ghaise : spear' is Pokorny's own lemma and gloss. Two qualifications. (1) The number '2' is Nourai's own: Pokorny numbers this lemma ĝhei-1 and reserves ĝhei-2 for 'winter; snow'. (2) Merging the verb root and the spear-noun into one box goes beyond what Nourai's own source allows: Walde-Pokorny I 546 says explicitly that it is 'wegen des Vokalismus nicht unbedenklich ... auch *ghaiso-s \\\"Ger\\\" mit unserem ghei- zu vereinen, da dies im Ai. durchaus den Ablaut einer leichten Wz. zeigt', and Pokorny only 'compares' the two. The Iranian and Germanic branches of the chart therefore hang on two roots that may or may not be one. Within the chart, the Avestan boxes (#1, #10) and the Germanic/English boxes (#11, #12) are solid; the trouble is concentrated in the Persian and Arabic boxes, where three separate words (abzār/afzār, apsān, safīna) belong to other roots and one Avestan form (zaēna 2 'chain') does not exist at all.\",\n \"note_fa\": \"خودِ ریشه درست است و هر دو ارجاع پوکورنی دقیق‌اند: پوکورنی در صفحهٔ ۴۲۴–۴۲۵ مادهٔ ĝhei- «راندن، پرتاب کردن، زخم زدن» را می‌آورد و زیر آن دقیقاً همین صورت‌های اوستایی zaēna- «سلاح»، zaya- «ابزار، ساز و برگ»، zayan- «مسلح»، zaēman- «بیدار، چالاک» و zaēnahvant- «هوشیار» را فهرست می‌کند؛ و در صفحهٔ ۴۱۰ مادهٔ ghaiso- «چوب‌دست، زوبین» را با gaesum لاتینی-گلی و gār انگلیسی کهن و geirr نورس. دو نکته: نخست آنکه شمارهٔ «۲» از آنِ نورایی است، زیرا پوکورنی این ماده را ĝhei-1 می‌نامد و ĝhei-2 را برای «زمستان، برف» نگاه می‌دارد؛ دوم آنکه یکی‌کردن ریشهٔ فعلی و اسمِ «نیزه» در یک خانه، فراتر از چیزی است که خودِ منبع نورایی اجازه می‌دهد — والده-پوکورنی (ج۱ ص۵۴۶) صریحاً می‌گوید که پیوند دادن *ghaiso- به ghei- «به سبب وضع مصوت‌ها بی‌اشکال نیست». در مجموع ادعای نورایی دربارهٔ ریشه پذیرفتنی است، ولی خطاهای این صفحه در شاخهٔ فارسی و عربی است: افزار/ابزار، اپسان و سفینه به ریشه‌های دیگری بازمی‌گردند و «zaēna ۲» به معنی «زنجیر» اصلاً واژهٔ اوستایی نیست.\",\n \"sources\": [\n   \"https://www.etymonline.com/word/garlic\",\n   \"https://www.etymonline.com/word/auger\"\n ],\n \"ref_check\": [\n  {\"ref\": \"POK:410\", \"status\": \"supports\",\n   \"note\": \"Pokorny IEW p.410 (POK_full.txt line 35803ff., 'Page(s):410'): 'Root / lemma: ghaiso- (or ĝhaiso- : gheiso-) | Meaning: stick; dart | Material: ... gall.-Latin gaesum, gall.-gr. γαῖσον \\\"heavy iron spear, lance\\\"; Old Irish gae \\\"spear, javelin\\\"; Old High German Old Saxon ger, Old English gar, Old Icelandic geirr m. \\\"throw spear\\\" (*gaizas)'. Exactly Nourai's 'Ghaise : spear'.\"},\n  {\"ref\": \"POK:424\", \"status\": \"supports\",\n   \"note\": \"Pokorny IEW p.424-425 (POK_full.txt line 36107ff., 'Page(s): 424-425'): 'Root / lemma: ghei-1, ghei-. Meaning: to drive; to throw; to wound ... Material: A. ghei- \\\"antreiben\\\": Old Indic hinoti ... Avestan zaēnah- \\\"astir, keen, eager\\\", zaēman- \\\"active, awake\\\" ... zaēnahvant- \\\"waking, watchful\\\"; zaēna- m. \\\"weapon\\\", zaya- m. \\\"(*weapon), tool, piece of armament\\\", zayan- \\\"armed\\\"'. The whole Avestan side of the chart is copied from this page; note that Pokorny's lemma number here is 1, not 2.\"}\n ],\n \"consulted\": [\n  {\"src\": \"WLD\", \"where\": \"Bd. I 528 (ghaisos) and I 546 (1. ghei-)\", \"stance\": \"partial\",\n   \"note\": \"WLD_Bd1_1930_dli_70244_djvu.txt line 33237: 'ghaisos \\\"Stecken, auch als Wurfspieß\\\"'; line 34342ff.: '1. ghei- \\\"antreiben, lebhaft bewegen (schleudern) oder bewegt sein\\\" ... wegen des Vokalismus nicht unbedenklich ist es, auch *ghaiso-s \\\"Ger\\\" (s. d.) mit unserem ghei- zu vereinen, da dies im Ai. durchaus den Ablaut einer leichten Wz. zeigt' — supports both lemmas but expressly doubts the merger Nourai's single root box performs.\"},\n  {\"src\": \"AHD\", \"where\": \"Watkins, IE appendix s.v. ghaiso-\", \"stance\": \"supports\",\n   \"note\": \"AHD_watkins1985.txt line 507: 'ghaiso-. A stick, spear. 1. Germanic *gaizaz in: a. Old English gar, spear: GORE; (GARFISH), GARLIC; b. compound *nabō-gaizaz, tool for piercing wheel hubs ...: AUGER; c. Old Norse geirr ... GYRFALCON. [Pok. ghaiso- 410.]'\"},\n  {\"src\": \"IEC\", \"where\": \"Mann, s.v. ghaisos\", \"stance\": \"supports\",\n   \"note\": \"IEC.txt line 4557: 'ghaisos \\\"lance, pole\\\". WP I, 528 ... Gallo-Lat. gaesum; ... OHG gēr, MHG gēr(e); OE gār; ... ON geirr \\\"spear\\\"'.\"},\n  {\"src\": \"SYN\", \"where\": \"Buck 20.21 'Weapons, arms', p.1384\", \"stance\": \"supports\",\n   \"note\": \"SYN.txt line 34630: 'Av. zaēna-, and zaya-, with zayan- \\\"armed\\\" : Skt. heti- \\\"missile\\\", hi- \\\"urge, hurl\\\", prob. also Ir. gae, OE gar, etc. \\\"spear\\\" (20.26). Walde-P. 1.546. Barth. 1650, 1666.' Buck joins the two halves of Nourai's root box in exactly the same way.\"}\n ],\n \"nodes\": []\n}\n\nN = entry[\"nodes\"]\n\nN.append({\n \"id\": 1, \"lang\": \"Avestan\",\n \"words\": \"zaěna 1; zaya; zayan; zaenô-hâra\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Av. zaēna- m. 'weapon' (Bartholomae, AiW col. 1650), zaya- m. '(weapon,) equipment, piece of armament' (col. 1666) and zayan- 'armed' are the regular Iranian outcomes of PIE *ǵʰey- 'to impel, hurl' — Indo-Iranian *ǰʰay- > Proto-Iranian *zay-, with the inherited palatal *ǵʰ giving Av. z- (satem development) against Skt. h- in hinóti 'sets in motion', hetí- 'missile'. zaēna- is a -na- derivative of the same stem (the 'thing hurled'), zaya- a thematic noun, zayan- its possessive adjective ('provided with zaya-'). Pokorny 424, Buck 1384 and Klein s.v. 'goad' all print exactly this set. The fourth item is different in kind: zaēnō-hāra- is not an attested Avestan word but Friedrich Müller's reconstruction (*zaēnō-hāra- 'Waffenschutz', WZKM 8, 96) proposed to explain New Persian zenhār (node #7); the chart prints it without an asterisk and glosses it 'hold (your) weapon, be careful', reading the second member as if from *dhar- 'to hold' (whence the ☞Dher 1 cross-reference), whereas Müller, Hübschmann and Mo'in read it as -hāra- 'guarding' from Iranian har-/*ser- 'to protect'. Verdict plausible: three of the four words are confirmed, the fourth is an unmarked reconstruction with a second member the chart analyses differently from the source it comes from.\",\n \"derivation_fa\": \"صورت‌های اوستایی zaēna- «سلاح»، zaya- «ابزار، ساز و برگ جنگی» و zayan- «مسلح» بازتاب منظم ریشهٔ هندواروپایی آغازین *ǵʰey- «راندن، پرتاب کردن» در ایرانی‌اند: *ǵʰ کامی‌شدهٔ هندواروپایی در زبان‌های شرقی (ساتم) به z بدل شده، از این رو در اوستایی z- در برابر h- سنسکریت در hinóti «به حرکت درمی‌آورد» و hetí- «تیر، پرتابه». بارتولمه در ستون‌های ۱۶۵۰ و ۱۶۶۶ همین واژه‌ها را آورده و پوکورنی (۴۲۴) و باک (۱۳۸۴) نیز. اما واژهٔ چهارم از گونه‌ای دیگر است: zaēnō-hāra- واژهٔ گواهی‌شدهٔ اوستایی نیست، بلکه بازسازیِ فریدریش مولر است (*zaēnō-hāra- «سلاح‌بان») برای توضیح «زنهار» فارسی، و کتاب آن را بدون ستاره و با تحلیلِ جزء دومش از *dhar- «داشتن» آورده، حال آنکه مولر و هوبشمان و معین آن را از har- «پاسبانی کردن» می‌گیرند. پس سه واژه تأیید می‌شود و چهارمی با احتیاط پذیرفتنی است.\",\n \"sources\": [],\n \"ref_check\": [\n  {\"ref\": \"POK:424\", \"status\": \"supports\",\n   \"note\": \"Pokorny 424-425 s.v. ghei-1: 'Avestan ... zaēna- m. \\\"weapon\\\", zaya- m. \\\"(*weapon), tool, piece of armament, weapons\\\", zayan- \\\"armed\\\"' (POK_full.txt line 36126).\"},\n  {\"ref\": \"KLN:666\", \"status\": \"supports\",\n   \"note\": \"Klein 1966 s.v. goad (KLN_1966.txt line 16368; 'goad' falls on p.666 of vol. I): 'goad, n. — ME. gode, fr. OE. gad ... rel. to Lombard gaida, \\\"spear\\\", and cogn. with OI. hetih, \\\"missile, projectile\\\", hayati, hinoti, \\\"pushes on, hurls\\\", Avestic zaina-, \\\"weapon\\\", Gk. χαῖος, \\\"shepherd's staff\\\", Gaul.-L. gaesum ... OE. gar, \\\"spear\\\"'.\"},\n  {\"ref\": \"SYN:1384\", \"status\": \"supports\",\n   \"note\": \"Buck p.1384 (§20.21 'Weapons, arms'; running head '1384' visible in SYN.txt at that block): 'Av. zaēna-, and zaya-, with zayan- \\\"armed\\\" : Skt. heti- \\\"missile\\\", hi- \\\"urge, hurl\\\", prob. also Ir. gae, OE gar, etc. \\\"spear\\\". Walde-P. 1.546. Barth. 1650, 1666.' — the page also lists 'Av. zaēna-, zaya-' in the head table of words for 'weapons'.\"}\n ],\n \"consulted\": [\n  {\"src\": \"BRT\", \"where\": \"cols. 1650-1651, 1666\", \"stance\": \"supports\",\n   \"note\": \"Bartholomae AiW: 'j. zaēna- m. \\\"Waffe\\\" ... mp. zēn, np. zīn. — Vgl. zaya-, zaēnay-. — Pü. (zu Yt. 1): afzār'; 'j. zaēnav- f. \\\"Wehrgehänge\\\" ... np. zīn \\\"Sattel\\\"'; 'j. zaēnay- Adj. \\\"reg, eifrig\\\"'. No headword zaēnō-hāra- exists in the AiW.\"},\n  {\"src\": \"CHEUNG\", \"where\": \"s.v. *zai¹ 'to set in motion, impel'\", \"stance\": \"supports\",\n   \"note\": \"CHEUNG.txt line 29799ff.: '*zai¹ \\\"to set in motion, impel\\\" | AVESTAN: zaii- \\\"to set in motion\\\" ... MIDDLE PERSIAN: MMP zyn, BMP zyn /zēn/ \\\"armour, weapon, sword\\\" ... PARTHIAN: zyn \\\"armour, weapon, sword\\\" ... SANSKRIT: hay \\\"to impel, drive, hurl\\\" (RV+)'. Cheung's Iranian verb root is Nourai's PIE root.\"},\n  {\"src\": \"HUB\", \"where\": \"Persische Studien §527, p.60\", \"stance\": \"partial\",\n   \"note\": \"Hübschmann p.60: 'Fr. Müller setzt es = zd. *zaēnō-hāra- \\\"Waffenschutz\\\" (WZKM. 8, 96). Die letzte Erklärung scheint mir die beste.' — the form is starred there, i.e. reconstructed, and its second element is 'protection', not 'holding'.\"}\n ]\n})\n\nN.append({\n \"id\": 2, \"lang\": \"Pahlavi\",\n \"words\": \"abzâr\",\n \"verdict\": \"disputed\",\n \"derivation\": \"Middle Persian abzār 'instrument, means; spice' is not a descendant of Av. zaya- 'weapon'. Its Book Pahlavi spelling settles the question: MacKenzie writes it ʾp̄cʾl, with ⟨c⟩ = č, and Parthian has ʾbcr / ʾʾbcʾr / ʾʾbjʾr ābžār 'materials, means' — a *č, not a *z. The word is *upa/abi-čāra- 'means of doing' (root kar-/čar-), whereas zaya- would have given MP *zay (and indeed MacKenzie's English index lists 'instrument abzar, zay' side by side as two different words). Nyberg states the confusion outright: apa-zār 'mighty, power' < *upa-zāvar 'is often confounded with the late form avzār < apacār, hence the erroneous Skr. renderings by śastra \\\"arms\\\"'. What Nourai's chart has caught is a translation equivalence, not a genealogy: Bartholomae notes that the Pahlavi Zand of Yašt 1 renders Av. zaēna- 'weapon' by afzār, and that gloss is presumably what Bailey's cited page reports. Nourai himself flags the difficulty by pointing the reader at his root 'Geu 2' (p.147), where he derives abzār/afzār from Av. *api-zāvar 'tool' — the *upa-zāvar of Nyberg's other homonym, so his alternative is nearer the truth but still confuses the two Pahlavi words.\",\n \"derivation_fa\": \"«ابزار» فارسی میانه (abzār) از zaya- اوستایی «سلاح» نمی‌آید. املای پهلوی کتابی تکلیف را روشن می‌کند: مکنزی آن را ʾp̄cʾl می‌نویسد که در آن ⟨c⟩ همان č است، و در پارتی نیز ʾbcr / ʾʾbžʾr «مواد، وسیله» آمده است؛ یعنی صامت میانی *č بوده نه *z. صورت اصلی *upa/abi-čāra- «وسیلهٔ انجام دادن» از ریشهٔ kar-/čar- است، حال آنکه zaya- در فارسی میانه *zay می‌داد (و مکنزی در نمایهٔ انگلیسی خود abzar و zay را دو واژهٔ جداگانه برای «ابزار» می‌آورد). نیبرگ صریح می‌گوید که abzār «توانا، نیرو» (< *upa-zāvar) را بارها با صورت متأخر avzār < apacār درآمیخته‌اند و همین سبب ترجمه‌های نادرست سنسکریت به śastra «سلاح» شده است. آنچه نمودار گرفته، برابرنهادِ ترجمه است نه خویشاوندی: بارتولمه یادآور می‌شود که زندِ پهلویِ یشت ۱ واژهٔ zaēna- را به afzār برگردانده است. پژوهش امروزی ادعای نورایی را در این خانه رد می‌کند.\",\n \"sources\": [W + \"%D8%A7%D9%81%D8%B2%D8%A7%D8%B1\"],\n \"ref_check\": [\n  {\"ref\": \"ISS:16\", \"status\": \"not_checked\",\n   \"note\": \"Bailey, Indo-Scythian Studies / Khotanese Texts VI (Prolexis), p.16 is not available online (HathiTrust search-only; archive.org holds vols I-III only). The substitute on disk, Bailey's Dictionary of Khotan Saka (ISS_alt_DKS.txt), was grepped for 'abzar', 'afzar', 'zaina', 'ysīna' and has no entry bearing on Persian abzār.\"}\n ],\n \"consulted\": [\n  {\"src\": \"PHD\", \"where\": \"p.5 s.v. abzār\", \"stance\": \"contradicts\",\n   \"note\": \"MacKenzie: 'abzar [ʾp̄cʾl | M ʾbcʾl, N afzār] instrument, means; spice' — the ⟨c⟩ of the heterogram-free spelling points to *č, not *z; MacKenzie's English index (p.… 'instrument abzar, zay'; 'means abzar, ar'; 'skill abzar') keeps abzār and zay apart.\"},\n  {\"src\": \"NYB\", \"where\": \"Glossary p.… s.v. apa-zār\", \"stance\": \"contradicts\",\n   \"note\": \"Nyberg II: 'apa-zār [ʾpzʾl] 1. adj. mighty ... 2. subst. power ... < *upa- (or api-) zāvar ... Often confounded with the late form avzār < apacār (q.v.), hence the erroneous Skr. renderings by śastra \\\"arms\\\"'. Nyberg thus derives the 'tool' word from *apacār and expressly calls the 'weapon' reading an error.\"},\n  {\"src\": \"HUB\", \"where\": \"Persische Studien §95, p.17\", \"stance\": \"contradicts\",\n   \"note\": \"Hübschmann: 'Np. afzār \\\"Werkzeug\\\" (bal. LW. auzar) ~ phl. afzār geht nach ZDMG. 32, 408 auf ein ap. *abizara-, nicht *abidara- zurück.' — an *abi-…-formation, not a derivative of zaya-.\"},\n  {\"src\": \"BRT\", \"where\": \"col. 1650 s.v. zaēna-\", \"stance\": \"partial\",\n   \"note\": \"Bartholomae records only 'Pü. (zu Yt. 1): afzār', i.e. that the Pahlavi version translates Av. zaēna- by afzār. That is a rendering, not an etymological equation.\"}\n ]\n})\n\nN.append({\n \"id\": 3, \"lang\": \"Persian\",\n \"words\": \"abzâr, afzâr «ابزار ، افزار»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"The step drawn here — Pahlavi abzār > New Persian ابزار abzār / افزار afzār 'tools, implements' — is correct and uncontroversial: Wiktionary has 'افزار: inherited from Middle Persian ʾp̄cʾl, ʾp̄zʾl (abzār) \\\"instrument, means; spice\\\". Doublet of ابزار', with Parthian ʾʾbcʾr, ʾʾbjʾr (ābžār) 'materials, means' as the cognate. The two New Persian shapes are the ordinary post-Sasanian doublet of intervocalic -bz- ~ -fz- (compare abzūdan/afzūdan, abrāz/afrāz); Balochi borrowed the word as auzar. What is wrong is not this arrow but the one above it: the ultimate ancestor is *upa/abi-čāra-, not Av. zaya-. Nourai's own NOTE ('For a different derivation of these words see root \\\"Geu 2\\\"') refers to his p.147, where he takes abzār/afzār from Av. *api-zāvar 'tool' beside zāvar- 'power' — which is Nyberg's *upa-zāvar, the source of the homonym abzār 'mighty, power' rather than of abzār 'tool'. Modern scholarship takes neither of his two options.\",\n \"derivation_fa\": \"این پیوند — از abzār فارسی میانه به «ابزار / افزار» فارسی نو — درست و بی‌مناقشه است؛ ویکی‌واژه می‌نویسد که «افزار» میراثی از abzār فارسی میانه است و با ʾʾbžʾr پارتی «مواد، وسیله» هم‌ریشه. دو صورتِ «ابزار» و «افزار» نمونهٔ همان دوگانگی آشنای ب/ف در میانِ واژه است (مانند ابزودن/افزودن و ابراز/افراز)، و بلوچی آن را auzar وام گرفته است. اشکال در این پیکان نیست، در پیکانِ بالای آن است: نیای نهایی *upa/abi-čāra- است نه zaya- اوستایی. یادداشت خودِ نورایی («برای اشتقاق دیگر رک: ریشهٔ Geu 2») به صفحهٔ ۱۴۷ ارجاع می‌دهد که در آن ابزار را از *api-zāvar اوستایی «ابزار» می‌گیرد — یعنی همان *upa-zāvar نیبرگ که منشأ abzār همنامِ «توانا، نیرو» است نه abzār «ابزار». پژوهش امروزی هیچ‌یک از دو گزینهٔ او را نمی‌پذیرد.\",\n \"sources\": [W + \"%D8%A7%D9%81%D8%B2%D8%A7%D8%B1\"],\n \"ref_check\": [\n  {\"ref\": \"ISS:16\", \"status\": \"not_checked\",\n   \"note\": \"Same page of Bailey as node #2; Khotanese Texts VI is not online and the Dictionary of Khotan Saka on disk is silent on Persian abzār.\"}\n ],\n \"consulted\": [\n  {\"src\": \"PHD\", \"where\": \"p.5 s.v. abzār\", \"stance\": \"supports\",\n   \"note\": \"'abzar [ʾp̄cʾl | M ʾbcʾl, N afzār] instrument, means; spice' — MacKenzie's own equation MP abzār = N(ew Persian) afzār is the arrow drawn here.\"},\n  {\"src\": \"HUB\", \"where\": \"Persische Studien §95, p.17\", \"stance\": \"supports\",\n   \"note\": \"'Np. afzār \\\"Werkzeug\\\" (bal. LW. auzar) ~ phl. afzār' — the MP > NP step, with the Balochi loan; only the pre-history differs from Nourai's.\"},\n  {\"src\": \"ARY\", \"where\": \"grep of ARY_pages.txt for افزار\", \"stance\": \"silent\",\n   \"note\": \"Aryanpur's Farhang-e Rishe-ha has no headword افزار / ابزار (no hit for 'افزار' in ARY_pages.txt).\"}\n ]\n})\n\nN.append({\n \"id\": 4, \"lang\": \"Persian\",\n \"words\": \"zîn «زین»; âb-zîn «آبزین ؟ ، آبزن»; apsân «اپسان ؟»\",\n \"verdict\": \"disputed\",\n \"derivation\": \"Three words with three different fates. (1) زین zīn 'saddle' < MP zēn: Bartholomae derives it from Av. zaēnav- f. 'sword-belt' ('KompE. — np. zīn \\\"Sattel\\\"', col. 1651) and Mo'in's footnote on the very Borhān page Nourai cites repeats this, citing Av. zaēna-, zaēnav-, Bartholomae 1650/1651, Armenian zēn, Nyberg 255, Hübschmann 111. Phonetically the chain is regular: Av. zaēna- > MP zēn (Av. -aē- > MP -ē-) > NP zīn, the ordinary raising of Middle Persian ē to New Persian ī (compare MP šēr > NP šīr). But Horn is a dissenting voice in Nourai's own library: 'Für np. zīn \\\"Sattel\\\" scheint sich in der älteren Sprache keine Anknüpfung zu finden' (Grundriss, 'Verlorenes Sprachgut' §240), and MacKenzie lists ¹zēn 'weapon, armour' and ²zēn 'saddle' as two separate entries. Plausible, not proved. (2) آبزن āb-zan 'bath-tub': the attested Middle Persian form is āb-zan (MacKenzie: 'āb-zan [ʾpzn' | N ~] bath'), and Wiktionary derives NP آبزن directly from MP ābzan while explicitly leaving the second element unexplained; the Iranian loans Syriac ʾāwzānāʾ, Old Armenian awazan, Georgian avazani all show -zan, not -zēn. The reading 'āb-zīn = water-saddle' is Asbaghi's conjecture, adopted here, and the chart's own question mark concedes it. (3) اپسان apsān 'grinding stone': the Persian word is افسان afsān / فسان fasān / سان sān 'whetstone', and Horn §98 derives it from MP afsān < *abi-śāna-, i.e. the prefix abi- plus the stem of Skt. śāna- 'whetstone' (PIE *ḱeh₃- 'to sharpen', Lat. cōs, catus), comparing Armenian yesan, Wakhi/Sarikoli pasān. It has nothing to do with zaya- or zīn; the spelling اپسان with پ is the German transcription used by Fraenkel and Asbaghi, not a Persian orthography. Node verdict = the worst of the three.\",\n \"derivation_fa\": \"سه واژه با سه سرنوشت. ۱) «زین» از zēn فارسی میانه: بارتولمه (ستون ۱۶۵۱) آن را از zaēnav- اوستایی «حمایل سلاح» می‌گیرد و حاشیهٔ معین بر همان صفحهٔ برهان که نورایی ارجاع داده همین را می‌گوید و به zaēna-، zaēnav-، بارتولمه ۱۶۵۰/۱۶۵۱، zēn ارمنی، نیبرگ ۲۵۵ و هوبشمان ۱۱۱ استناد می‌کند؛ از نظر آوایی زنجیره منظم است: -aē- اوستایی در فارسی میانه ē می‌شود و ē فارسی میانه در فارسی نو به ī بدل می‌گردد (مانند šēr > شیر). ولی هرن در همان کتابخانهٔ نورایی مخالف است و می‌نویسد برای «زین» به معنی زین اسب در زبان کهن پیوندی یافت نمی‌شود، و مکنزی هم zēn «سلاح» و zēn «زین» را دو مدخل جدا آورده است. ۲) «آبزن»: صورت گواهی‌شدهٔ فارسی میانه āb-zan است («حمام، تشت») و ویکی‌واژه جزء دوم را ناشناخته می‌داند؛ وام‌واژه‌های سریانی ʾāwzānāʾ و ارمنی کهن awazan و گرجی avazani همه zan دارند نه zēn. خوانشِ «آبزین = زینِ آب» حدسِ اصباغی است و علامت پرسش خودِ کتاب نیز آن را می‌پذیرد. ۳) «اپسان»: واژهٔ فارسی «افسان/فسان/سان» است و هرن (بند ۹۸) آن را از afsān فارسی میانه از *abi-śāna- می‌گیرد، یعنی پیشوند abi- به علاوهٔ ستاکِ śāna- سنسکریت «سنگ فسان»، از ریشهٔ هندواروپایی *ḱeh₃- «تیز کردن» (لاتین cōs، catus)، هم‌ریشه با yesan ارمنی. پس دو واژه از این سه به این ریشه ربطی ندارند.\",\n \"sources\": [W + \"%D8%B2%DB%8C%D9%86\", W + \"%D8%A2%D8%A8%D8%B2%D9%86\"],\n \"ref_check\": [\n  {\"ref\": \"BQT:1054\", \"status\": \"supports\",\n   \"note\": \"Borhān-e Qāṭeʿ ed. Moʿin, the زین page (BQT_v2_pages.txt leaf 516, printed running head ≈1056 by the file's +540 offset, i.e. two pages off Nourai's citation): Moʿin's footnote reads '… پهلوی zēn (سلاح، تجهیز) … (۱) اوستا zaēna- … بارتولمه ۱۶۵۰، ارمنی zēn (سلاح، تجهیز). (۲) اوستا zaēnav- (سلاح دفاع)، بارتولمه ۱۶۵۱، در فارسی zēn … نیبرگ ص ۲۵۵، هوبشمان ص ۱۱۱' — precisely the derivation the chart draws for زین.\"},\n  {\"ref\": \"PLA:162\", \"status\": \"supports\",\n   \"note\": \"Asbaghi, Persische Lehnwörter im Arabischen p.162 (PLA_pages.txt: page-162 running head 'safsīr? … sakāriš', entry at line 9213): 'safīna: \\\"Schiff, Fahrzeug\\\" pers. اپسان apsān durch syr. Vermittlung … mand. spinta, hebr. ספינה. M.E. ist es eine Metathese v. pers. آبزین āb-zīn \\\"Wasserausrüstung\\\".' Both of Nourai's odd Persian forms — apsān and āb-zīn — come from this one page, and the āb-zīn reading is Asbaghi's personal opinion ('M.E.').\"},\n  {\"ref\": \"FVF:2\", \"status\": \"not_checked\",\n   \"note\": \"Emām Shushtari, Farhang-e vāžehā-ye fārsi dar zabān-e ʿarabi p.2 — no copy on archive.org; the noorlib viewer (book 105056) is JavaScript-only and could not be read.\"}\n ],\n \"consulted\": [\n  {\"src\": \"BRT\", \"where\": \"cols. 1650-1651\", \"stance\": \"supports\",\n   \"note\": \"'j. zaēna- m. \\\"Waffe\\\" … mp. zēn, np. zīn' and 'j. zaēnav- f. \\\"Wehrgehänge\\\" … KompE. — np. zīn \\\"Sattel\\\"'.\"},\n  {\"src\": \"PHD\", \"where\": \"pp. 1, 100 s.vv. āb-zan, ¹zēn, ²zēn\", \"stance\": \"partial\",\n   \"note\": \"MacKenzie prints 'āb-zan [ʾpzn' | N ~] bath' (not āb-zēn), and keeps '¹zēn [zyn' | = M] weapon, armour' apart from '²zēn [zyn' | N zin] saddle', with 'zēn-abzār [N zinafzār] horse-armour'.\"},\n  {\"src\": \"HRN\", \"where\": \"'Verlorenes Sprachgut' §240 and §98\", \"stance\": \"contradicts\",\n   \"note\": \"§240: 'zēn \\\"Waffe\\\" … aw. zaēna- \\\"Waffe\\\"; arm. LW. zēn. Für np. zīn \\\"Sattel\\\" scheint sich in der älteren Sprache keine Anknüpfung zu finden'; §98: 'efsān \\\"Wetzstein\\\", eusān, fesān, vergl. sān, phlv. afsān …; skr. śāna- \\\"Wetzstein\\\" + abhi; vergl. arm. yesan. waḵ. sar. pasān \\\"Wetzstein\\\"' — Horn denies the saddle link and gives apsān a different root altogether.\"},\n  {\"src\": \"BQT\", \"where\": \"vol. 1, printed p.≈149 s.v. افسان\", \"stance\": \"partial\",\n   \"note\": \"Borhān: 'افسان بروزن ترسان. آهنی و سنگی را گویند که بدان … و تیغ و مانند آن تیز کنند' — confirms the meaning 'whetstone' for افسان (the Persian spelling), which the chart writes اپسان.\"}\n ]\n})\n\nN.append({\n \"id\": 5, \"lang\": \"Arabic\",\n \"words\": \"safan; safîneh\",\n \"verdict\": \"disputed\",\n \"derivation\": \"The node has to be split. (a) Arabic سَفَن safan 'rasp, shagreen; to peel, plane' really is a Persian loan, and both of Nourai's own references say so: Jeffery (FVQ 171-172) writes that the verb 'is denominative from سفن an adze, which itself is not an Arabic word but the Pers. اپسان which passed into Arabic through Syriac', and Fraenkel (AFA 216) had already said 'die Wurzel سفن, so weit sie im Arabischen sich findet, ist ganz unecht, da das Verbum denominativ von سَفَن ist; dies ist aber — bis jetzt noch unerkannt — nichts als persisch اپسان \\\"Wetzstein\\\"'. That much is confirmed — but the Persian word is افسان/فسان 'whetstone', not a derivative of zīn (see node #4), so the arrow from box #4 is the wrong parent. (b) Arabic سَفِينَة safīna 'ship' (Qurʾān xviii.71,79; xxix.15) is where Nourai's chart parts company with the field. Jeffery, on the very page cited, calls the derivation from safan 'fanciful' and continues: 'Guidi … called attention to the fact that سفينة is a loan-word in Arabic, and the Semitic root is doubtless ספן \\\"to cover in\\\", which we find in Akk. sapannu … and Aram. ספן; Heb. ספן \\\"to cover\\\". The form ספינה occurs in Heb. in the story of Jonah'. Fraenkel p.216, which the chart's own note flags, says the same, and Wiktionary today has 'سفينة: From Aramaic סְפינִתָּא / ܣܦܻܝܢܬܳܐ (sǝp̄īntā). Forming the root س ف ن. Cognate with Hebrew סְפִינָה'. The only support for the Persian origin is Asbaghi's private conjecture ('M.E. ist es eine Metathese v. pers. آبزین āb-zīn \\\"Wasserausrüstung\\\"'), i.e. one 1988 opinion against Guidi, Fraenkel, Jeffery and current lexicography. The chart's NOTE 'AFA:216 disagrees with this derivation' is therefore accurate for safīna and misleading for safan, which Fraenkel positively supports.\",\n \"derivation_fa\": \"این خانه را باید دو نیم کرد. الف) «سَفَن» عربی به معنی «سوهان، پوست‌کن؛ تراشیدن» به‌راستی وام‌واژه‌ای ایرانی است و هر دو مرجعِ خودِ نورایی همین را می‌گویند: جفری (ص ۱۷۱–۱۷۲) می‌نویسد که این فعل از اسمِ سَفَن «تیشه» ساخته شده و آن اسم عربی نیست بلکه «اپسان» فارسی است که از راه سریانی به عربی رسیده؛ و فرانکل (ص ۲۱۶) پیش‌تر گفته بود که ریشهٔ س‌ف‌ن در عربی اصیل نیست و سَفَن چیزی جز «اپسان» فارسی به معنی سنگ فسان نیست. تا اینجا ادعای نورایی درست است — اما واژهٔ فارسی «افسان/فسان» است و به «زین» ربطی ندارد، پس خانهٔ مادر اشتباه است. ب) «سفینه» جای جدایی نمودار از پژوهش امروزی است: جفری در همان صفحه اشتقاق آن از سَفَن را «خیال‌بافانه» می‌خواند و به پیروی از گویدی آن را وام‌واژه‌ای سامی از ریشهٔ ספן «پوشاندن» می‌داند (اکدی sapannu، آرامی ספן، عبری ספינה در داستان یونس)؛ فرانکل نیز همین را می‌گوید و ویکی‌واژه امروز می‌نویسد «سفينة از آرامی sǝp̄īntā». تنها پشتیبانِ خاستگاه فارسی، حدسِ شخصی اصباغی است («به گمان من قلبِ آبزین فارسی است»). پس در بخش «سفینه» پژوهش امروزی ادعای نورایی را رد می‌کند.\",\n \"sources\": [W + \"%D8%B3%D9%81%D9%8A%D9%86%D8%A9\"],\n \"ref_check\": [\n  {\"ref\": \"PLA:162\", \"status\": \"supports\",\n   \"note\": \"Asbaghi p.162: 'safīna: \\\"Schiff, Fahrzeug\\\" pers. اپسان apsān durch syr. Vermittlung … M.E. ist es eine Metathese v. pers. آبزین āb-zīn \\\"Wasserausrüstung\\\"' — the only source in the whole dossier that makes safīna itself Persian, and it is offered as the author's own opinion.\"},\n  {\"ref\": \"FVQ:171\", \"status\": \"partial\",\n   \"note\": \"Jeffery, FVQ pp.171-172 (FVQ_pages.txt leaves 188-189): the entry سفينة opens at the foot of p.171 and continues 'The lexicographers fancifully derive it from سفن to peel or pare (cf. LA, xvii, 72). This, however, is denominative from سفن an adze, which itself is not an Arabic word but the Pers. اپسان which passed into Arabic through Syriac. Guidi, Della Sede, 601, called attention to the fact that سفينة is a loan-word in Arabic, and the Semitic root is doubtless ספן to cover in …'. Supports safan < Persian apsān; contradicts safīna < Persian.\"},\n  {\"ref\": \"VDQ:260\", \"status\": \"not_checked\",\n   \"note\": \"Badreʾi's Persian translation of Jeffery (Vāžehā-ye daxil dar Qorʾān-e majid) p.260 — noorlib's viewer (book 12868) is JavaScript-rendered and returns only site chrome; the substance is that of FVQ 171-172, checked above.\"}\n ],\n \"consulted\": [\n  {\"src\": \"AFA\", \"where\": \"Fraenkel p.216\", \"stance\": \"partial\",\n   \"note\": \"AFA.txt leaf 247 (printed 216): 'In der That sprechen alle Anzeichen dafür, dass es ein übernommenes Wort sei. Vor allem hat es im Arabischen keine Ableitung; die Wurzel سفن, so weit sie im Arabischen sich findet, ist ganz unecht, da das Verbum denominativ von سَفَن ist; dies ist aber — bis jetzt noch unerkannt — nichts als persisch اپسان \\\"Wetzstein\\\". … Im Hebräischen hat das Wort eine bequeme Ableitung von ספן \\\"täfeln\\\"'. Exactly the split verdict given here; the chart's own note is right that Fraenkel rejects the ship-word's Persian origin.\"},\n  {\"src\": \"KLN\", \"where\": \"grep of KLN_1966/1971 for 'safina', 'sefinah'\", \"stance\": \"silent\",\n   \"note\": \"Klein's English dictionary has no entry for the Arabic ship-word (it entered no European language through Arabic).\"},\n  {\"src\": \"ARB\", \"where\": \"al-Jawāliqī, al-Muʿarrab (ARB_mo3rb.txt)\", \"stance\": \"silent\",\n   \"note\": \"Grep for سفينة in ARB_mo3rb.txt returns only incidental uses inside other entries (e.g. 'رست السفينة', 'ذنب السفينة'), never a headword سفينة — the classical Arabic muʿarrab tradition did not treat it as a foreign word.\"}\n ]\n})\n\nN.append({\n \"id\": 6, \"lang\": \"Persian\",\n \"words\": \"safîneh «سفینه»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"New Persian سفینه safīne is a straightforward Arabic loan: Moʿin's Farhang tags it '[ع. سفینة] (اِ.) کشتی', and Wiktionary has 'سفینه: borrowed from Arabic سَفِينَة (safīna, \\\"ship\\\")'. The Persian development the chart records is the secondary sense: because an anthology was written in a tall narrow oblong format (a بیاض), the codex itself came to be called a safīne, 'a large notebook in which poems and other matter are written' (Moʿin), and it is in this sense that Ḥāfeẓ's line quoted on the page uses it — 'در این زمانه رفیقی که خالی از خلل است / صراحی می ناب و سفینهٔ غزل است', where the flask of wine and the 'ship of ghazals' are the only flawless companions; the pun on 'ship' and 'songbook' is the point of the verse. The arrow itself (Arabic > Persian) is therefore certain. Whether this is a round trip out of Persian and back, as the chart implies, depends entirely on node #5, where the Persian starting point is not accepted by Jeffery, Fraenkel or current lexicography.\",\n \"derivation_fa\": \"«سفینه» در فارسی نو وام‌واژه‌ای عربی است و معین آن را «[ع. سفینة] (اِ.) کشتی» می‌آورد و ویکی‌واژه نیز آن را وام‌گرفته از سَفِینَة عربی می‌داند. آنچه در فارسی افزوده شده معنای دوم است: چون جُنگ شعر را در دفتری بلند و باریک (بیاض) می‌نوشتند، خودِ آن دفتر را «سفینه» خواندند — به تعبیر معین «بیاض بزرگ دفتری که در آن اشعار و مطالب دیگر نویسند» — و بیت حافظ که در همین صفحه نقل شده بر همین ایهام استوار است: «در این زمانه رفیقی که خالی از خلل است / صراحی می ناب و سفینهٔ غزل است». پس خودِ این پیکان (عربی ← فارسی) قطعی است؛ اما اینکه این واژه سفری رفت‌وبرگشت از فارسی به عربی و بازگشت به فارسی باشد، یکسره به خانهٔ ۵ بستگی دارد که در آن خاستگاه فارسی را جفری و فرانکل و فرهنگ‌نویسی امروز نمی‌پذیرند.\",\n \"sources\": [W + \"%D8%B3%D9%81%DB%8C%D9%86%D9%87\"],\n \"ref_check\": [\n  {\"ref\": \"MON\", \"status\": \"supports\",\n   \"note\": \"Moʿin, Farhang-e Fārsi (MON_part1.txt line 78313): 'سفینه: [ع. سفینة] (اِ.) کشتی.' and (line 48674) 'سفینه. بیاض بزرگ دفتری که در آن اشعار و مطالب دیگر نویسند؛ سفینه. آلبوم' — both senses of the chart's box, and Moʿin marks the word as Arabic, without a Persian back-story.\"},\n  {\"ref\": \"VGH:74\", \"status\": \"not_checked\",\n   \"note\": \"Khadiv Jam, Vāže-nāme-ye ghazalhā-ye Ḥāfeẓ p.74 — not on archive.org; the only copy (ketabnak 121989) is behind a login. The Ḥāfeẓ line it is cited for is quoted correctly on the page.\"}\n ],\n \"consulted\": [\n  {\"src\": \"MON\", \"where\": \"MON_part1 lines 48674, 78313\", \"stance\": \"supports\",\n   \"note\": \"See ref_check; Moʿin gives both 'کشتی' and 'بیاض بزرگ … آلبوم' and the tag [ع.].\"},\n  {\"src\": \"FVQ\", \"where\": \"Jeffery pp.171-172\", \"stance\": \"contradicts\",\n   \"note\": \"Jeffery makes safīna itself a Semitic word from ספן 'to cover in', so the Persian word is a loan from Arabic, not a re-import of a Persian word.\"}\n ]\n})\n\nN.append({\n \"id\": 7, \"lang\": \"Persian\",\n \"words\": \"zenhâr «زنهار» (زینهار)\",\n \"verdict\": \"plausible\",\n \"derivation\": \"New Persian زنهار/زینهار zenhār, zīnhār 'beware!; quarter, protection' goes back to Middle Persian zēnhār (MacKenzie: 'zēnhār [zyn(h)ʾl | N zinhār] protection'), and Moʿin's footnote on the Borhān page Nourai cites gives 'پهلوی zynhʾl (امن، امان)'. The disputed part is the first syllable. Friedrich Müller (WZKM 8, 96) analysed it as Avestan *zaēnō-hāra- 'weapon-guarding', i.e. zaēna- 'weapon' + -hāra- from har- 'to guard' — that is Nourai's arrow — and Hübschmann, on exactly the page cited, endorses it: 'Die letzte Erklärung scheint mir die beste', adding that as an interjection 'look out!' it matches German 'Achtung!', MHG 'wafen!' (itself 'weapon!'), which is a real argument for the weapon-etymology. Moʿin repeats Hübschmann's verdict in the Borhān footnote. Against it stand Andreas's az-ēn-hār 'guard against this' (Hübschmann p.60, ZDMG 47, 704), Horn's suggestion at the page Nourai cites that the word belongs rather to dāštan/dar- 'to hold' ('ursprünglich \\\"hüte dich vor diesem, halte dich von diesem zurück\\\"' — hence the chart's ☞Dher 1), and today's Wiktionary, which prints the Andreas analysis: 'From Middle Persian zynhʾl (zēnhār), originally an imperative command of az \\\"from\\\" + ēn \\\"this\\\" + Proto-Iranian *hār- \\\"to guard\\\"'. Both camps agree on the second element; only the first is at issue, and Nourai's is the older, minority reading. Note also that Horn found the scansion of zinhār as an amphimacer in Firdausī an argument for an Iranian, not Aramaic, origin — so the word is Iranian either way.\",\n \"derivation_fa\": \"«زنهار/زینهار» به معنی «امان، پناه؛ بپرهیز!» از zēnhār فارسی میانه است (مکنزی: zēnhār «حمایت») و حاشیهٔ معین بر همان صفحهٔ برهان که نورایی ارجاع داده می‌نویسد «پهلوی zynhʾl (امن، امان)». اختلاف بر سرِ هجای نخست است. فریدریش مولر آن را *zaēnō-hāra- اوستایی «سلاح‌بان» تحلیل کرد — یعنی zaēna- «سلاح» + hāra- از har- «پاسبانی کردن» — و هوبشمان در همان صفحهٔ ۶۰ می‌گوید «این آخرین توضیح به نظر من بهترین است» و می‌افزاید که کاربرد آن به‌عنوان شبه‌جمله («هشدار!») با Achtung! آلمانی و wafen! آلمانی میانه (که خود «سلاح!» است) همانند است. معین همین داوری هوبشمان را تکرار کرده است. در برابر، آندرئاس آن را «از این هار» (از این بپرهیز) می‌داند، هرن در صفحهٔ ۱۱۶ آن را به «داشتن» می‌بندد (از این‌رو ارجاع کتاب به Dher 1)، و ویکی‌واژهٔ امروز نیز تحلیل آندرئاس را می‌آورد. هر دو گروه بر جزء دوم هم‌داستان‌اند و تنها جزء نخست محل نزاع است؛ خوانش نورایی خوانشی کهن‌تر و اقلیت است. پس ادعای او با احتیاط پذیرفتنی است.\",\n \"sources\": [W + \"%D8%B2%D9%86%D9%87%D8%A7%D8%B1\"],\n \"ref_check\": [\n  {\"ref\": \"HUB:60\", \"status\": \"supports\",\n   \"note\": \"Hübschmann, Persische Studien p.60 §527 (HUB.txt leaf 71): 'Np. zinhār \\\"Schutz, Sicherheit, Zuflucht\\\" ist natürlich nicht aus az īn dār entstanden … Andreas erklärt zinhār aus az īn hār von Wzl. har \\\"servare\\\" (ZDMG. 47, 704), Fr. Müller setzt es = zd. *zaēnō-hāra- \\\"Waffenschutz\\\" (WZKM. 8, 96). Die letzte Erklärung scheint mir die beste. Zum Gebrauch von zinhār als Interjektion \\\"gib acht\\\" vgl. d. Achtung!, mhd. wafen! etc.'\"},\n  {\"ref\": \"HRN:116\", \"status\": \"partial\",\n   \"note\": \"Horn, Grundriss p.116-117 (leaf 137-139), end of no. 527 dāštan: 'Gehört hierher vielleicht auch zīnhār, zinhār \\\"Schutz, Sicherheit etc.\\\", ursprünglich \\\"hüte dich vor diesem, halte dich von diesem zurück\\\", wovon dann zīnhārī … gebildet wurden? Allerdings wüsste ich dann nicht die Messung von zinhār als Amphimacrus bei Firdusī zu erklären, die mir jedenfalls für iranischen Ursprung des Wortes zu sprechen scheint (anders Nöldeke, Pers. Stud. II, 46 …)'. Horn has the word on the cited page but assigns it to dar- 'to hold', not to zaēna- 'weapon'.\"},\n  {\"ref\": \"BQT:1055\", \"status\": \"supports\",\n   \"note\": \"Borhān-e Qāṭeʿ ed. Moʿin, the زینهار/زنهار page (BQT_v2_pages.txt leaf 517, running head ≈1057 on the file's offset): entry 'زنهار … پناه جستن و امان خواستن باشد - و عهد و پیمان - و ترس و بیم …' with footnote 1 'پهلوی zynhʾl (امن، امان)' and footnote 3 naming both explanations: '… (F.) Müller آن را اوستایی *zaēnō-hāra (سلاح‌حامی) می‌داند، هوبشمان گوید که وجه اخیر بنظر من بهتر است'.\"}\n ],\n \"consulted\": [\n  {\"src\": \"PHD\", \"where\": \"p.100 s.v. zēnhār\", \"stance\": \"supports\",\n   \"note\": \"MacKenzie: 'zēnhār [zyn(h)ʾl | N zinhār] protection' — the Middle Persian ancestor exists, with the sense the chart gives; MacKenzie offers no etymology.\"},\n  {\"src\": \"NYB\", \"where\": \"Glossary s.vv. zēnāvandihā, zēn-dān\", \"stance\": \"partial\",\n   \"note\": \"Nyberg attests the zēn- family in Pahlavi ('zēnāvandihā \\\"vigilantly\\\" … From zēnāvand, Av. (1651) zaēnahvant- \\\"vigilant\\\"') but has no entry zēnhār, so he neither confirms nor refutes the first element.\"}\n ]\n})\n\nN.append({\n \"id\": 8, \"lang\": \"Avestan\",\n \"words\": \"zaěna 2; zaěna-dana\",\n \"verdict\": \"disputed\",\n \"derivation\": \"There is no Avestan zaēna- 'chain'. Bartholomae's Altiranisches Wörterbuch has zaēna- m. 'Waffe', zaēnav- f. 'Wehrgehänge', zaēnah- n., zaēnay- 'reg, eifrig', zaēnahvant- 'wachsam', zaēni.buδra-, ¹²zaēman- and hu-zaēna- — and nothing meaning 'chain'; Nourai's own question mark concedes the doubt. The compound is likewise not attested: Horn, on the page cited, writes '671. zindān \\\"Gefängniss\\\". aw. *zaēna-dāna- (?); phlv. z(i)ndān (PPGl.); arm. LW. zndan' — a starred reconstruction with a query — and then glosses it not 'house of chains' but 'Etwa urspr. \\\"Waffenarsenal\\\"?', i.e. 'weapon-store', comparing Hebrew 'the place where the shields are kept' (Jer. 32:8). Nyberg says the same without hesitation: 'zēn-dān [zyndʾn'] prison … \\\"Keeping-place of arms\\\" = \\\"arsenal\\\"'. So the second element -dāna- is 'container' (as in Persian قلمدان, نمکدان) and the first is zaēna- 'weapon', the same word as in node #1 — the chart's 'zaēna 2 : chain' is a back-formation invented to let زنجیر hang from this box. The compound as such is a modern reconstruction from the Middle Persian word, not an Avestan attestation.\",\n \"derivation_fa\": \"واژهٔ اوستایی zaēna- به معنی «زنجیر» وجود ندارد. بارتولمه در فرهنگ ایرانی باستان zaēna- «سلاح»، zaēnav- «حمایل»، zaēnah-، zaēnay- «چالاک»، zaēnahvant- «هوشیار» و zaēman- را دارد و هیچ‌یک معنی «زنجیر» ندارد؛ علامت پرسشِ خودِ کتاب نیز همین تردید را نشان می‌دهد. ترکیب نیز گواهی‌شده نیست: هرن در همان صفحهٔ ۱۴۹ می‌نویسد «۶۷۱. زندان: اوستایی *zaēna-dāna- (؟)؛ پهلوی z(i)ndān؛ ارمنی وام‌واژهٔ zndan» و آن را نه «خانهٔ زنجیر» بلکه «شاید در اصل زرادخانه (Waffenarsenal)» معنی می‌کند؛ نیبرگ هم بی‌تردید می‌گوید zēn-dān یعنی «جای نگهداری سلاح = زرادخانه». پس جزء دوم -dāna- «ظرف، جایگاه» است (مانند قلمدان و نمکدان) و جزء نخست همان zaēna- «سلاح» خانهٔ یکم؛ «zaēna ۲ به معنی زنجیر» ساختهٔ خودِ نورایی است تا «زنجیر» را از این خانه آویزان کند. ریشه‌شناسی امروزی این خانه را به این صورت نمی‌پذیرد.\",\n \"sources\": [W + \"%D8%B2%D9%86%D8%AF%D8%A7%D9%86\"],\n \"ref_check\": [\n  {\"ref\": \"HRN:149\", \"status\": \"partial\",\n   \"note\": \"Horn p.149 (HRN.txt leaf 171): '671. zindān \\\"Gefängniss\\\". aw. *zaēna-dāna- (?); phlv. z(i)ndān (PPGl.); arm. LW. zndan. Etwa urspr. \\\"Waffenarsenal\\\" wie auch [Hebr.] (Jer. 32(2)8) \\\"Ort, an dem die Scheiben aufgehoben werden\\\", allgemein \\\"Gefängniss\\\" heisst? Darmesteter, Ét. ir. I, 290 setzt zweifelnd auch np. zenjīr, zinjīr … hierher'. Horn has the compound but starred and queried, and glosses it 'arsenal', not 'house of chains'.\"},\n  {\"ref\": \"DRM:290\", \"status\": \"partial\",\n   \"note\": \"Darmesteter, Études iraniennes I p.289-290 (DRM.txt around line 6403): §245 on the suffix -bān lists 'zīndān-pān … gardien de la prison', and the footnote on the facing column reads 'Cf. … zinja et zinjīr, chaînes; mais l'étymologie de ces [mots …]' — a tentative aside, which is exactly how Horn reports it ('setzt zweifelnd').\"}\n ],\n \"consulted\": [\n  {\"src\": \"BRT\", \"where\": \"cols. 1650-1652\", \"stance\": \"contradicts\",\n   \"note\": \"Bartholomae's zaēna- entries are 'zaēna- m. \\\"Waffe\\\"', 'zaēnaŋhan- \\\"wachend, wachsam\\\"', 'zaēnay- \\\"reg, eifrig\\\"', 'zaēnav- f. \\\"Wehrgehänge\\\"', 'zaēnah- n.', 'zaēnahvant- \\\"wachsam, regsam\\\"', 'zaēni.buδra-', '¹²zaēman-', 'hu-zaēna-'. There is no zaēna- 'chain' and no compound zaēna-dāna-.\"},\n  {\"src\": \"NYB\", \"where\": \"Glossary s.v. zēn-dān\", \"stance\": \"partial\",\n   \"note\": \"'zēn-dān [zyndʾn'] prison 9³. 116²⁵ (twice). — \\\"Keeping-place of arms\\\" = \\\"arsenal\\\"' — supports the compound's make-up but not the gloss 'chain'.\"}\n ]\n})\n\nN.append({\n \"id\": 9, \"lang\": \"Persian\",\n \"words\": \"zanjîr «زنجیر»; zendân «زندان»\",\n \"verdict\": \"disputed\",\n \"derivation\": \"زندان zendān 'prison' is the safe half: MP zēndān (MacKenzie 'zēndān [zyndʾn' | = M, N zindān] prison', with zēndān-bān 'jailer'), whence Old Armenian զնդան zndan, Syriac zendānīq and Ossetic zyndon 'hell' as loans, and Wiktionary's account is Horn's and Nyberg's: 'From Middle Persian zēndān \\\"prison\\\". Ultimate origin uncertain. Perhaps originally \\\"arsenal, armoury\\\", from zēn \\\"weapon, armour\\\" and -dān \\\"holder, container\\\"'. MP ē regularly gives NP ī/e, so zēndān > zendān is trivial. زنجیر zanjīr 'chain' is another matter. Horn only reports it as Darmesteter's hesitant guess ('setzt zweifelnd auch np. zenjīr, zinjīr hierher'), and Darmesteter's own footnote breaks off with 'mais l'étymologie de ces [mots est douteuse]'. Phonetically the -jīr is unexplained on this route: nothing in zaēna-dāna- or zēn- yields -j-. The etymology now current, proposed by Mary Boyce to W. B. Henning and accepted by him around 1963, takes zanjīr from a Middle Indic reflex of Sanskrit शृङ्खल śṛṅkhala 'chain, fetter', with the initial ś- > z- substitution that Buyaner set out to investigate; Wiktionary's Persian entry carries this note in place of an etymology and marks the traditional derivation as unsupported. So: zendān plausible-to-confirmed, zanjīr disputed; the node takes the worse verdict.\",\n \"derivation_fa\": \"«زندان» نیمهٔ مطمئن این خانه است: zēndān فارسی میانه (مکنزی: zēndān «زندان»، zēndān-bān «زندانبان») که ارمنی کهن zndan و سریانی zendānīq و اُسِتی zyndon «دوزخ» وام‌واژه‌های آن‌اند، و ویکی‌واژه همان تحلیل هرن و نیبرگ را می‌آورد: «از zēndān فارسی میانه؛ خاستگاه نهایی نامعلوم، شاید در اصل زرادخانه، از zēn سلاح و -dān جایگاه». تبدیل ē فارسی میانه به ی/ــِ فارسی نو قاعده‌مند است. اما «زنجیر» داستان دیگری دارد: هرن آن را تنها به‌عنوان حدسِ مردّدِ دارمستتر نقل می‌کند و خودِ دارمستتر در پانوشت می‌نویسد «ولی ریشه‌شناسی این واژه‌ها [مشکوک است]». از نظر آوایی نیز جزء -جیر در این مسیر توضیح‌ناپذیر است. ریشه‌شناسی رایج امروز، که مری بویس به هنینگ پیشنهاد کرد و هنینگ حدود ۱۹۶۳ پذیرفت، «زنجیر» را از بازتابی هندیِ میانه از शृङ्खल (śṛṅkhala) سنسکریت «زنجیر، بند» می‌گیرد، با بدل‌شدن ś- آغازین به z-. پس «زندان» پذیرفتنی است و «زنجیر» را پژوهش امروزی رد می‌کند.\",\n \"sources\": [W + \"%D8%B2%D9%86%D8%AF%D8%A7%D9%86\", W + \"%D8%B2%D9%86%D8%AC%DB%8C%D8%B1\"],\n \"ref_check\": [\n  {\"ref\": \"HRN:149\", \"status\": \"partial\",\n   \"note\": \"Horn p.149 no.671 (quoted at node #8) has zindān with the starred Avestan compound and adds zanjīr only as Darmesteter's doubtful ('zweifelnd') attachment, with Nöldeke's confirmation that Pahlavi writes zindān with plene i/e — evidence for zindān, none for zanjīr.\"}\n ],\n \"consulted\": [\n  {\"src\": \"PHD\", \"where\": \"p.100 s.vv. zēndān, zēndān-bān\", \"stance\": \"supports\",\n   \"note\": \"'zēndān [zyndʾn' | = M, N zindān] prison. -bān [-pʾn' | N -bān] jailer. -ig [-yk' | N -i] prisoner' — the Middle Persian ancestor of زندان, with its derivatives; MacKenzie has no entry for a Pahlavi ancestor of زنجیر.\"},\n  {\"src\": \"NYB\", \"where\": \"Glossary s.v. zēn-dān and s.v. band\", \"stance\": \"supports\",\n   \"note\": \"'zēn-dān … prison … \\\"Keeping-place of arms\\\" = \\\"arsenal\\\"'; s.v. band, 'band + zēndān imprisonment, captivity' — Nyberg treats the chain-word band and zēndān as separate items, never connecting zanjīr to this family.\"},\n  {\"src\": \"DRM\", \"where\": \"Études iraniennes I, p.289 n.3 and p.290\", \"stance\": \"partial\",\n   \"note\": \"The zinja/zinjīr note is a two-line aside inside the discussion of the suffix -bār, itself broken off with 'mais l'étymologie de ces …'; p.290 lists 'zīndān-pān … gardien de la prison' as a specimen of the -bān suffix, not as an etymology of zanjīr.\"}\n ]\n})\n\nN.append({\n \"id\": 10, \"lang\": \"Avestan\",\n \"words\": \"zaěmi; zaěman; zaěnah-vant\",\n \"verdict\": \"transcription_suspect\",\n \"error_in\": \"book\",\n \"book_prints\": \"zaěmi\",\n \"correct_form\": \"zaēnah- (Pokorny) / zaēnay- (Bartholomae)\",\n \"derivation\": \"Two of the three words are exactly right and come straight from the page Nourai cites: Pokorny 424 has 'zaēman- \\\"active, awake\\\", n. \\\"wakefulness, agility\\\"' and 'zaēnahvant- (from a *zaēnah- n.) \\\"waking, watchful\\\"', which Bartholomae confirms ('¹zaēman- n. \\\"Regsamkeit, Munter-, Wachsein\\\"', '²zaēman- Adj. \\\"regsam, wach\\\"', 'zaēnahvant- Adj. \\\"wachsam, regsam\\\"'). These are -man- and -vant- derivatives of the same *zay- 'to be in motion, be roused', the intransitive counterpart of the transitive 'set in motion' that gives zaēna- 'weapon' — the semantic bridge is 'stirred up' > 'alert', and Pahlavi zēnāvand 'alert, vigilant' (MacKenzie; Nyberg 'zēnāvandihā \\\"vigilantly\\\" … From zēnāvand, Av. (1651) zaēnahvant-') carries it into Middle Persian. The first word, 'zaěmi : eager', is not an Avestan form. There is no zaēmi- in the Altiranisches Wörterbuch; in the slot where Nourai has it Pokorny prints zaēnah- 'astir, keen, eager' and Bartholomae has zaēnay- Adj. 'reg, eifrig' (Vd. 13.40, of a dog that is eager in barking). The printed page 154 of the book does read 'zaěmi', so the extraction is faithful and the misprint is Nourai's own — most likely a misreading of Pokorny's zaēnah- or Bartholomae's zaēnay-, since 'zaěnah-' then reappears in the third item as part of zaěnah-vant.\",\n \"derivation_fa\": \"دو واژه از سه واژه درست‌اند و مستقیماً از همان صفحهٔ پوکورنی گرفته شده‌اند: پوکورنی در ص ۴۲۴ zaēman- «چالاک، بیدار» و zaēnahvant- (از *zaēnah- خنثی) «هوشیار» را می‌آورد و بارتولمه هم همین‌ها را دارد. این‌ها مشتق‌های -man- و -vant- از همان ستاک *zay- «به جنبش درآمدن» هستند، یعنی روی لازمِ همان معنایی که در zaēna- «سلاح» رویِ متعدی دارد؛ پُل معنایی «برانگیخته» ← «هوشیار» است، و پهلوی zēnāvand «هوشیار» (نیبرگ: از zaēnahvant- اوستایی) همین را به فارسی میانه می‌رساند. اما واژهٔ نخست، «zaěmi : مشتاق»، صورتِ اوستایی نیست: در فرهنگ بارتولمه zaēmi- وجود ندارد و در همان جایگاه پوکورنی zaēnah- «چالاک، مشتاق» و بارتولمه zaēnay- «چالاک، تیزرو» دارد (وندیداد ۱۳٫۴۰ دربارهٔ سگی که در پارس‌کردن چالاک است). تصویر صفحهٔ ۱۵۴ چاپی نشان می‌دهد که خودِ کتاب «zaěmi» دارد؛ پس خطای خوانش اسکن نیست، خطای چاپیِ خودِ نورایی است و احتمالاً بدخوانی zaēnah- یا zaēnay-.\",\n \"sources\": [],\n \"ref_check\": [\n  {\"ref\": \"POK:424\", \"status\": \"partial\",\n   \"note\": \"Pokorny 424 (POK_full.txt line 36120): 'Avestan zaēnah- \\\"astir, keen, eager\\\", zaēman- \\\"active, awake\\\", n. \\\"wakefulness, agility, liveliness\\\"; zaēnahvant- (from a *zaēnah- n.) \\\"waking, watchful, wakeful\\\"'. Two of the three chart forms match verbatim; the third, 'zaěmi', is not on the page — Pokorny's word for 'eager' is zaēnah-.\"}\n ],\n \"consulted\": [\n  {\"src\": \"BRT\", \"where\": \"cols. 1650-1652\", \"stance\": \"partial\",\n   \"note\": \"'j. zaēnay- Adj. \\\"reg, eifrig\\\": yaθa hē … vāxam paiti ⁿnīš aŋhat \\\"wenn er (der Hund) … eifrig ist mit (der Stimme sva.) Bellen\\\" V. 13.40'; '¹zaēman- n. \\\"Regsamkeit, Munter-, Wachsein\\\" … Y. 44.5'; 'zaēnahvant- Adj. \\\"wachsam, regsam\\\" Yt. 10.61'. No headword zaēmi- exists anywhere in the AiW.\"},\n  {\"src\": \"WLD\", \"where\": \"Bd. I 546\", \"stance\": \"partial\",\n   \"note\": \"Walde-Pokorny: 'Av. zaēni- \\\"reg, eifrig\\\", zaēman- \\\"regsam, wach\\\", n. \\\"Regsamkeit, Muntersein, Wachsein\\\", zaēnaŋhant- (von einem *zaēnah- n.) \\\"wachend, wachsam\\\"' — the earlier edition cites the stem as zaēni-, again never zaēmi-.\"},\n  {\"src\": \"NYB\", \"where\": \"Glossary s.v. zēnāvandihā\", \"stance\": \"supports\",\n   \"note\": \"'zēnāvandihā [zynʾwndyhʾ] vigilantly 67¹³. — From zēnāvand, Av. (1651) zaēnahvant- \\\"vigilant\\\"' — the Middle Persian continuation of the third word of the box.\"}\n ]\n})\n\nN.append({\n \"id\": 11, \"lang\": \"Germanic\",\n \"words\": \"gaizaz\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Proto-Germanic *gaizaz 'spear' is the standard reconstruction from Old English gār, Old Saxon and Old High German gēr, Old Norse geirr and the Gothic personal names Rada-gaisus, Gaisa-rīks; Pokorny 410 gives it as '*gaizas' from *ǵʰaisó-, and Watkins/AHD prints 'ghaiso-. A stick, spear. 1. Germanic *gaizaz'. The form is regular by Grimm's law: PIE *ǵʰ- > Gmc. *g- and the thematic *-os of the noun becomes Gmc. *-az. The word is also the Germanic source of the Gaulish material Latin borrowed as gaesum (Caesar's 'heavy iron javelin'), though there the borrowing runs the other way round — Celtic gaisos into Latin — so the two branches are cognate, not derived one from the other, exactly as the chart shows by hanging Germanic directly on the root box.\",\n \"derivation_fa\": \"*gaizaz ژرمنی آغازین به معنی «نیزه» بازسازیِ استاندارد از gār انگلیسی کهن، gēr آلمانی علیای کهن و ساکسونی کهن، geirr نورس کهن و نام‌های گوتیِ Radagaisus و Gaisarīks است؛ پوکورنی در ص ۴۱۰ صورت *gaizas را از *ǵʰaisó- می‌آورد و واتکینز در پیوست فرهنگ American Heritage می‌نویسد «ghaiso-: چوب، نیزه. ۱. ژرمنی *gaizaz». تحول کاملاً قاعده‌مند و بر پایهٔ قانون گریم است: *ǵʰ هندواروپایی در ژرمنی به g بدل می‌شود و پایانهٔ *-os اسم به *-az. همین واژه با gaesum لاتینی (وام از گلی gaisos) هم‌ریشه است، نه برگرفته از آن. ادعای نورایی در این خانه درست است.\",\n \"sources\": [\"https://www.etymonline.com/word/auger\"],\n \"ref_check\": [\n  {\"ref\": \"AHD\", \"status\": \"supports\",\n   \"note\": \"Watkins, IE appendix (AHD_watkins1985.txt line 507): 'ghaiso-. A stick, spear. 1. Germanic *gaizaz in: a. Old English gar, spear …; b. compound *nabō-gaizaz, tool for piercing wheel hubs …; c. Old Norse geirr, spear … [Pok. ghaiso- 410.]' — Nourai's bare 'AHD' citation lands on exactly this entry.\"}\n ],\n \"consulted\": [\n  {\"src\": \"POK\", \"where\": \"p.410\", \"stance\": \"supports\",\n   \"note\": \"'Old High German Old Saxon ger, Old English gar, Old Icelandic geirr m. \\\"throw spear\\\" (*gaizas); Gothic PN Rada-gaisu-s, wand. Gaisa-rīk-s.'\"},\n  {\"src\": \"KLN\", \"where\": \"s.v. goad\", \"stance\": \"supports\",\n   \"note\": \"Klein: 'OE. gad … rel. to Lombard gaida, \\\"spear\\\" … Gaul.-L. gaesum … OE. gar, \\\"spear\\\", Du. gesel, OHG. geisila … \\\"whip, lash\\\"'.\"},\n  {\"src\": \"IEC\", \"where\": \"Mann s.v. ghaisos\", \"stance\": \"supports\",\n   \"note\": \"'OHG gēr, MHG gēr(e); OE gār; Du. geer \\\"bias, crosscut, gore\\\"; ON geirr \\\"spear\\\", geiri \\\"gore, gusset\\\"'.\"}\n ]\n})\n\nN.append({\n \"id\": 12, \"lang\": \"English\",\n \"words\": \"garlic; auger, garfish; Oscar, Edgar, Roger, Gerald\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Every item is a genuine reflex of OE gār 'spear' < PG *gaizaz, and the chart's parenthesis about garlic is the standard explanation. garlic: OE gārlēac (West Saxon garlec, Mercian garleac) = gār 'spear' + lēac 'leek', 'so called in reference to the clove' — the spear-shaped clove/leaves, exactly Nourai's gloss (Etymonline s.v. garlic). auger: 'a faulty separation of Middle English a nauger, from Old English nafogār \\\"nave (of a wheel) drill\\\", from Proto-Germanic *nabō-gaizaz', the same misdivision that produced adder from nadder and apron from napron (Etymonline s.v. auger; Watkins lists the compound under ghaiso-). garfish: mid-15c., 'from fish + Middle English gare, gore \\\"a spear\\\", from Old English gar', named for its long sharp snout. The four names are dithematic Germanic compounds whose second element is this noun: Roger < Old French Rogier < OHG Hrōd-gēr, literally 'famous with the spear' (Etymonline), reinforced in England by the cognate Old Norse Hróðgeirr; Edgar < OE Ēad-gār 'rich/blessed spear'; Oscar < OE Ōs-gār 'god's spear' (revived by Macpherson's Ossian, so its modern currency is Gaelic-mediated, but the Old English name is this compound); Gerald < Frankish Gēr-wald 'spear-rule', where the same element stands first. Note that the box carries no reference in the book; the chain is standard and uncontroversial.\",\n \"derivation_fa\": \"همهٔ اقلام این خانه بازتاب راستینِ gār انگلیسی کهن «نیزه» از *gaizaz ژرمنی‌اند و توضیحِ داخل پرانتز دربارهٔ سیر نیز توضیح استاندارد است. garlic از gārlēac انگلیسی کهن، یعنی gār «نیزه» + lēac «تره/پیاز»، به سببِ شکلِ نیزه‌مانندِ برگ و حبّه (اتیمآنلاین). auger از جدا‌سازی نادرستِ a nauger در انگلیسی میانه، از nafogār انگلیسی کهن «مته‌ای برای سوراخ‌کردن ناوهٔ چرخ»، از *nabō-gaizaz ژرمنی — همان لغزشی که nadder را به adder و napron را به apron بدل کرد. garfish (سدهٔ پانزدهم) از gare/gore «نیزه» به سبب پوزهٔ دراز و تیزش. چهار نام خاص هم ترکیب‌های دو‌جزئی ژرمنی‌اند که جزء دومشان همین واژه است: Roger از Hrōdgēr آلمانی علیای کهن «نامدار به نیزه»، Edgar از Ēadgār «نیزهٔ خجسته»، Oscar از Ōsgār «نیزهٔ ایزد»، و Gerald از Gērwald «فرمانروای نیزه» که در آن این جزء نخست آمده است. این خانه در کتاب ارجاعی ندارد ولی زنجیره کاملاً شناخته و بی‌مناقشه است.\",\n \"sources\": [\"https://www.etymonline.com/word/garlic\", \"https://www.etymonline.com/word/auger\", \"https://www.etymonline.com/word/Roger\"],\n \"ref_check\": [\n  {\"ref\": \"(none cited)\", \"status\": \"not_checked\",\n   \"note\": \"The box carries no reference in the book (refs=None); it inherits the AHD citation of its parent, and Watkins's ghaiso- entry does list GARFISH, GARLIC and AUGER among the English descendants.\"}\n ],\n \"consulted\": [\n  {\"src\": \"AHD\", \"where\": \"Watkins s.v. ghaiso-\", \"stance\": \"supports\",\n   \"note\": \"'Old English gar, spear: GORE; (GARFISH), GARLIC; b. compound *nabō-gaizaz, tool for piercing wheel hubs (*nabō, hub; see nobh-) [i.e. AUGER]'.\"},\n  {\"src\": \"KLN\", \"where\": \"s.v. goad; cp. gore, gar\", \"stance\": \"supports\",\n   \"note\": \"Klein derives OE gār 'spear' from the same base as Gaul.-L. gaesum and Av. zaina- 'weapon' (KLN_1966.txt line 16368), which is the parent link for all the English words in this box.\"},\n  {\"src\": \"SKT\", \"where\": \"grep of SKT.txt s.v. garlic, auger\", \"stance\": \"supports\",\n   \"note\": \"Skeat gives garlic as A.S. gār-lēac, 'spear-leek', and auger as a mis-division of a nauger, A.S. nafu-gār — the same account as Etymonline's.\"}\n ]\n})\n\ndoc = {\n \"pdf_page\": 184,\n \"book_page\": 154,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [entry]\n}\n\nwith open(\"/home/sfmqrb/git/rishe/data/verification/page-184.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(doc, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build184.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-184.json > /dev/null && echo \"JSON OK\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 184"
}
```


### [2026-09-05T21:16:49.614Z] TOOL RESULT

```
written
JSON OK
nodes verified: 12/12
node verdicts: {'plausible': 2, 'disputed': 5, 'confirmed': 4, 'transcription_suspect': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 10, 'not_checked': 6, 'partial': 6}
books consulted: {'supports': 16, 'partial': 10, 'contradicts': 6, 'silent': 3} | by book: {'BRT': 5, 'PHD': 5, 'NYB': 5, 'HUB': 3, 'KLN': 3, 'CHEUNG': 1, 'ARY': 1, 'HRN': 1, 'BQT': 1, 'AFA': 1, 'ARB': 1, 'MON': 1, 'FVQ': 1, 'DRM': 1, 'WLD': 1, 'POK': 1, 'IEC': 1, 'AHD': 1, 'SKT': 1}
```


## [2026-09-05T21:16:50.100Z] AGENT

You've hit your session limit · resets 7:40pm (America/Toronto)
