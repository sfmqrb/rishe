# Verification process log — verify-page-182


## [2026-09-05T20:54:04.603Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 182 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-182.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-182.json. Write /home/sfmqrb/git/rishe/data/verification/page-182.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 182` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T20:54:05.910Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T20:54:06.788Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T20:54:06.807Z] TOOL RESULT

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


## [2026-09-05T20:54:07.201Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-182.txt"
}
```


### [2026-09-05T20:54:07.215Z] TOOL RESULT

```
1	=== PDF page 182 (book page 152) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Ghebh-el : head, top  (refs POK:423)
4	#1 (parent #0) [Greek] refs=POK:423; KLN:259 | kephalě : head
5	  #2 (parent #1) [Arabic] refs=MON:2769; KLN:259 | qîphaleh, al-qîphâl : head | NOTE: KLN:259 claims this is of an unknown origin and is mistaken with the Greek word by translators of Avicena
6	    #3 (parent #2) [Persian] refs=MON:2769 | qîfâl «قیفال» : head | extra: ورید قیفالی
7	    #4 (parent #2) [Latin] refs=KLN:259 | cephalicus : head
8	      #5 (parent #4) [English] refs=AHD | cephalic
9	  #6 (parent #1) [Italian] refs=TAD:65 | cuffia : headband, scarf
10	    #7 (parent #6) [Arabic] refs=TAD:65 | kŭfîyyah : scarf
11	      #8 (parent #7) [Persian] refs=MON:3127 | kŭfîyyeh «کوفیّه» : scarf
12	#9 (parent #0) [Germanic] refs=AHD | gabl : top
13	  #10 (parent #9) [English] refs=None | gable
14	--- entry 1 ---
15	ROOT [Indo-European] Ghěi, Ğhî, Ğhiâ : to yawn  (refs POK:419; IEC:418)
16	#1 (parent #0) [Persian] refs=IEC:418; MON:2470; FRS:120 | fâž «فاژ ، فاژه» : yawn ; fâžîdan «فاژیدن» : to yawn
17	#2 (parent #0) [Germanic] refs=AHD:1517 | ginôn : yawn
18	  #3 (parent #2) [Old English] refs=AHD:1517 | geonian : yawn
19	    #4 (parent #3) [English] refs=AHD | yawn
20	#5 (parent #0) [Greek] refs=AHD:1517 | khasma : yawning (wide open) gulf
21	  #6 (parent #5) [English] refs=AHD | chasm
22	#7 (parent #0) [Old Norse] refs=AHD:1517 | gap : chasm ; gapa : to open mouth ; geispa : to yawn
23	  #8 (parent #7) [English] refs=AHD | gap, gape, gasp
24	
```


## [2026-09-05T20:54:10.967Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-182.json",
 "description": "Read source JSON for page 182"
}
```


### [2026-09-05T20:54:11.007Z] TOOL RESULT

```
{
  "pdf_page": 182,
  "book_page": 152,
  "entries": [
    {
      "root": {
        "name": "Ghebh-el",
        "lang": "Indo-European",
        "refs": "POK:423",
        "gloss": "head, top"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Greek",
          "refs": "POK:423; KLN:259",
          "words": [
            {"translit": "kephalě", "gloss": "head", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Arabic",
          "refs": "MON:2769; KLN:259",
          "words": [
            {"translit": "qîphaleh, al-qîphâl", "gloss": "head", "script": null}
          ],
          "note": "KLN:259 claims this is of an unknown origin and is mistaken with the Greek word by translators of Avicena",
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "MON:2769",
          "words": [
            {"translit": "qîfâl", "gloss": "head", "script": "قیفال"}
          ],
          "script_extra": "ورید قیفالی",
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 2,
          "lang": "Latin",
          "refs": "KLN:259",
          "words": [
            {"translit": "cephalicus", "gloss": "head", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "cephalic", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 1,
          "lang": "Italian",
          "refs": "TAD:65",
          "words": [
            {"translit": "cuffia", "gloss": "headband, scarf", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Arabic",
          "refs": "TAD:65",
          "words": [
            {"translit": "kŭfîyyah", "gloss": "scarf", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Persian",
          "refs": "MON:3127",
          "words": [
            {"translit": "kŭfîyyeh", "gloss": "scarf", "script": "کوفیّه"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "gabl", "gloss": "top", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "gable", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Ghěi, Ğhî, Ğhiâ",
        "lang": "Indo-European",
        "refs": "POK:419; IEC:418",
        "gloss": "to yawn"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "IEC:418; MON:2470; FRS:120",
          "words": [
            {"translit": "fâž", "gloss": "yawn", "script": "فاژ ، فاژه"},
            {"translit": "fâžîdan", "gloss": "to yawn", "script": "فاژیدن"}
          ],
          "note": null,
          "quote": {
            "text": "اگر ندانی باندیش تاچگونه بود - که سیرخورده بفاژد بهارگه اشتر",
            "poet": "Labîbî"
          }
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD:1517",
          "words": [
            {"translit": "ginôn", "gloss": "yawn", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Old English",
          "refs": "AHD:1517",
          "words": [
            {"translit": "geonian", "gloss": "yawn", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "yawn", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD:1517",
          "words": [
            {"translit": "khasma", "gloss": "yawning (wide open) gulf", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "chasm", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Old Norse",
          "refs": "AHD:1517",
          "words": [
            {"translit": "gap", "gloss": "chasm", "script": null},
            {"translit": "gapa", "gloss": "to open mouth", "script": null},
            {"translit": "geispa", "gloss": "to yawn", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "gap, gape, gasp", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-05T20:54:11.073Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T20:54:11.110Z] TOOL RESULT

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


## [2026-09-05T20:54:15.849Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','MON','TAD','AHD','IEC','FRS','WLD','SYN','SKT','LKT','LEW','FSD','WEB','PHN','DEV','AFM','ARB','RCH']:\n    v=d.get(k)\n    print(k, json.dumps(v, ensure_ascii=False)[:600])\n    print()\n\""
}
```


### [2026-09-05T20:54:17.657Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640", "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; insi

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

FRS {"title": "Asadi Tusi, Loghat-e Fors, ed. Mojtaba'i & Sadeqi, Kharazmi 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/LughatEFurs-AbuMansurAliBinAhmadAsadiTusiFarsi (Abbas Eqbal's 1319/1940 Tehran edition); also dli.ernet.439493 / dli.ernet.437743 (Horn's 1897 Göttingen edition, 'Lughat Faras')", "lookup_hint": "Look up the headword (entries grouped by final letter); FRS_pages.txt has \\f page breaks (567 leaves). Pagination differs from the 1365 Kharazmi edition Nourai cites — verify the entry, not the page.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/s

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 

LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f b

FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt

WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W

PHN {"title": "A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, Paris 1866", "edition_found": "1866", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairetym01pihagoog", "identifier": "dictionnairetym01pihagoog (others: bub_gb_QnsSAAAAIAAJ, dictionnairetym00pihagoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt", "page_offset": "leaf = printed + 31 (e.g. leaf 33 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://ar

DEV {"title": "L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876", "edition_found": "1876", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairety00devi", "identifier": "dictionnairety00devi (also dictionnairetym02devigoog, fr105comparative41)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt", "page_offset": "leaf = printed + 26 (pp. <80) to +30 (pp. >84), e.g. leaf 29 = p.3, leaf 118 = p.88. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.

AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/

ARB {"title": "al-Jawaliqi, al-Mu'arrab min al-kalam al-a'jami, Tehran 1966 (reprint of Ahmad M. Shakir's Cairo 1361/1942 edition)", "kind": "archive_djvu", "url": "https://archive.org/details/mo3rb (probably the Shakir edition) ; https://archive.org/details/almo3rab_gwaliqy_f_abduraheem (F. 'Abd al-Rahim ed., Damascus 1990) ; also uc1.aa0003615705 / AAlexandrina-148752 (Sachau's Leipzig 1867 ed.) ; text on shamela.ws", "lookup_hint": "Alphabetical Arabic headwords; grep in ARB_mo3rb.txt / ARB_abdulraheem.txt (raw, no page breaks); edition of mo3rb not confirmed — check its title page image.", "lo

RCH {"title": "J. Richardson, A Dictionary, Persian, Arabic and English, new ed. by F. Johnson, London 1829 (Lahore reprint 1984)", "edition_found": "1829 Johnson edition (DLI scan, 1814 leaves)", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.24303", "identifier": "in.ernet.dli.2015.24303 (other editions: 1806-10 a-dictionary-persian-arabic-and-english-vol.-i, india.history.resource.17812; 1852 Johnson dictionarypersia00johnuoft)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/RCH.txt", "page_offset": "leaf ~= printed + 93..94 (e.g. leaf 336 =
```


## [2026-09-05T20:54:21.835Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','AHD','IEC','TAD','MON','FRS']:\n    print(k, d[k].get('page_offset'))\n    print('  hint:', str(d[k].get('lookup_hint'))[:400])\n    print('  local:', d[k].get('local_file'))\n    print()\n\""
}
```


### [2026-09-05T20:54:23.471Z] TOOL RESULT

```
POK POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  hint: Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-d
  local: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt

KLN KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  hint: Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
  local: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt

AHD 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.
  hint: Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.
  local: /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt

IEC TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  hint: Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.
  local: /home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt

TAD 86 leaves (small book, ~80 printed pages); offset ≈ leaf − 4..6, verify against the printed numeral on the page image
  hint: Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; inside.php search works.
  local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD.txt']

MON None
  hint: Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/ab
  local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt']

FRS different edition — no mapping
  hint: Look up the headword (entries grouped by final letter); FRS_pages.txt has \f page breaks (567 leaves). Pagination differs from the 1365 Kharazmi edition Nourai cites — verify the entry, not the page.
  local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/FRS_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/FRS.txt']
```


## [2026-09-05T20:54:27.952Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"lemma: ghebh\" POK_full.txt | head -20\necho ---\ngrep -n -i \"lemma: ĝhē\" POK_full.txt | head -20\necho ---\ngrep -n -i \"lemma: ghē\" POK_full.txt | head -30"
}
```


### [2026-09-05T20:54:28.038Z] TOOL RESULT

```
---
---
```


## [2026-09-05T20:54:28.441Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"Page(s): 42[0-9]\" POK_full.txt | head -20\necho ---\ngrep -n \"Page(s): 41[5-9]\" POK_full.txt | head -20"
}
```


### [2026-09-05T20:54:28.514Z] TOOL RESULT

```
32433:Page(s): 423 
32486:Page(s): 423-424 
32508:Page(s): 423 
32524:Page(s): 424 
32559:Page(s): 426-427 
32611:Page(s): 427 
32653:Page(s): 427 
32862:Page(s): 428 
36112:Page(s): 424 
36160:Page(s): 424-425 
36272:Page(s): 425-426 
36631:Page(s): 429-434 
---
37427:Page(s): 418-419 
37647:Page(s): 419-422 
38005:Page(s): 416-417
```


## [2026-09-05T20:54:30.606Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '32400,32530p' POK_full.txt"
}
```


### [2026-09-05T20:54:30.659Z] TOOL RESULT

```
Old Icelandic gagr greylag goose '; 

Lithuanian gaJgalas^ drake, male duck ', Latvian gaigale^ a gull kind ', Old Prussian 
gegalis^ aquanaut ', See N Gaygelitfr, 

russ. gogolb " common goldeneye. Golden Eye ', poln. gogoi, g^goF European 
goldeneye ', old gogolica^ a coot, a water-fowl ' (Berneker 318). 

Maybe alb. ^0^0/ "ghost' 

References: WP. I 526, Trautmann 74 f. 
Page(s): 407 

Root/ lemma: gh^^-el- -el- -lo- 

Meaning: weathercock; head 

Material: Gr. KscpaAn " head, end, acme, apex ', maked. KspAri, KspaAn, PN K£paAo(;; 

unclear yapaAav syKscpaAovri KScpaAnv Hes.; compare in addition Schwyzer Gr. Gr. I 70 f., 

Pisani RIEtBalk. 1937, 15 ff.; 



Gothic giblaxw. " gable, pinnacle', changing through ablaut Old Norse gaflrw. ' gable; 
point of an island '; Old High German gibilm. " gable, pole of the earth '; gibillai., gebalm.. 
Middle High German gebercraumm'; 

Tocharian A spa/- "head' (: gr. KScpaAn), Instr. spalyo. 

References: WP. I 571, Feist 214, W. Schuize Kl. Schr. 252, 261. 
Page(s): 423 

Root / lemma: ghedy-, ghcA^- 

Meaning: to join, make a bond 

Material: Old Indie gadhya-h " stick firmly '; a-gadhita-h " clipped, dinged ', pari-gadhita-h " 

clasps ' (from sexual union); 

Old Frisian ^aoVa "unite ', Middle Low German gaden {* gadon) " suit, please, be married 
', Old High German bigaton. Middle High German gaten, gegaten\ntr. " gather, so that it 
fits ', trans. ' Gleiches zu Gleichem gesellen, zusammenbringen ', refl. " sich fijgen ', Old 
High German gi-gat^ fitting'. Old Saxon gi-gado^ ilk ', Old English (gejgada^ comrade, 
husband ', Modern High German Gafte; Gothic gad/7/ggs' cousin ', Old Saxon gaduling 
"kinsman, relative'. Old English gsede/fng ' comrade' , Old High German gatulinc, gatilinc 
"kinsman, relative, cousin, journeyman '; Old English geador, to gaedere {er\<^\. togethei) 
"together'. Old Frisian gadur. Middle Low German gader. Middle High German gaterds., 
Old English gadrian, gged(e)rian {er\<^\. gathei) "gather, collect'. Old Frisian gaderia. Middle 
Low German gad(d)eren ds.. Middle High German vergatern^be united, merge ', Modern 
High German vergattern ds.\ in addition presumably also Old High German gataro. Modern 
High German Gatter {umge\au\.e\ Middle High German geter. Modern High German Gittei), 
Old Swedish gadder, Middle Low German gaddere^ Gitter '; 

with lengthened grade: Go\.\\\c got^s. Old Icelandic ^dd/; Old English god. Old High 
German guot. Modern High German gut {Qermar\\c *gdda-^ fitting'); Old Icelandic ^oda" 
gut machen ' etc. 

Old Church Slavic godi) "time, right time', god/na ' G) pa' , godtnb "compliant', russ. 
godnyj^ suitable ', Old Church Slavic u-goditi^ please ', 

maybe alb. Geg ^ooV/" strike (chime?)', goditun' suitable ' 

russ. -Church S\aN\c goditids.. Church Slavic ugoda^ satisfaction ', russ. kk^oo''5" benefit, 
advantage'. Old Church Slavic negodovati^ be undisposed ', iter. Old Church Slavic 



ugozdg, ugozditr it make right, please ' (etc., Berneker 317 f., where also about poln. 
loanword Lithuanian gadas^ association ', gadytis^ occur, meet ' among others). 

In addition perhaps Lithuanian dial, guddas, Latvian ^i/oo's "honour, fame; decorum, 
courteousness; festivity, feast '; 

whereas are Latvian gads, sagads^ stock, acquired property ', gadat'care, worry' 
probably from borrowed Russ.; 

here (compare Van Windekens Lexique 32) Tocharian AB kafk-, is softened A kack-, B 
kacc- " rejoice ' (compare above Middle Low German gaden " please '); different Pedersen 
Tocharian 172. 

References: WP. I 531 ff., Trautmann 74, Feist 218. 
See also: see also under ghend- 
Page(s): 423-424 

Root / lemma: ghed- 

Meaning: to defecate; hole 

Material: Old Indie hadati, hadate^ defecates', Avestan zadah- m. 'rump'; 

Armenian ye/(ostem) "tail (of animals)'; 

gr. x£^w " defecate ', Perf. K£xo5a; x65avo(; "rump'; 

Phrygian ^swa nuAr) (leg. nuyn?); 

alb. dhjes^ defecate ', ndjete^Wxdeous, disgusting', fem. "repugnance'; ndotem^ be 
stained, smeared ', Geg ndishem "hideous'; common alb. gh- > d-. 

Old Norse gatv^. "hole, aperture ', Old English geaC door, aperture ' (out of it nir. gead^ 
the bottom '), Old Frisian yie/n. "hole, aperture ', Old Saxon ^a/"hole'. Middle Low German 
also 'anus', ndd. Kattegaf Katzenloch '. 

References: WP. I 571 f. 
Page(s): 423 

Root / lemma: ghegh- 
Meaning: to curve, bend 



Material: Armenian ^og "cavity, lap, bosom, belly' etc., as adjective "hollow, concave', 
^o^e/r? "hollow out'; gugem {* ghogh-) " hug, embrace, hold tight, care'; 

Norwegian gagr^ crooked back ', Old Icelandic gag-ha/s'\N\t\r\ neck crooked backward ', 
ablaut, gseg/ask'te stretched ', etc.; 

Lithuanian gogasm. " withers of horse '. 

References: WP. I 570, Liden Armen. Stud. 93 f. 
Page(s): 424 

Root / lemma: gheti'^- 
Meaning: to yearn for 

Material: Old Irish gra//= cymr. gwysti, acorn, guister captive ', bret. goest/'pay, caution', 
gall, in Conge/st/usMH. (cymr. cyngwystr commitment ') = Old High German gTsal,
```


## [2026-09-05T20:54:31.115Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '37380,37440p' POK_full.txt; echo =====; sed -n '37600,37660p' POK_full.txt"
}
```


### [2026-09-05T20:54:31.178Z] TOOL RESULT

```
Exit code 1
Latin hems " heir ' {*ghero- + e-c^d\-, " das verwaiste Gut an sich nehmend '?, s. about 
the ending under e-particle); 

Note: 

Common Old Indie : Latin gh-> h-. 

Avestan zazamil dismiss from, fire from ', with ava-^ leave, go away, scare, frighten ', 
with upa-3iU6 fra-^ leave, allow here, lead here, conduct here '; a-za- ' go near, approach 
', uz-za- " jump, be elevated ' {uzayanto par\.\c\p\e Nom. PI.); 

Maybe alb. Geg me zane' quarrel, capture, occupy ' 

gr. hom. Kixcivu) (*KixavFu)), Attic Kiyxavw {*gha-n-u-). Inf. present hom. KixniJevai, 
participle present Kix£i<; 'reach, catch up, meet, attain, take'; with formant -d-\ gr. xa^ofjai, 
Fut. ep. xacraoijai, Aor. ep. xaoaapriv " retreat, flee, cease, stop, halt, desist ', avaxa^u) tr. 
" drive back, repel ', intr. " retreat, go back', as Med. xaAau) ' reduce, decrease, become 
limp ' in partizip. Adj. *gha-lo-s ' going away, leaving ' or ' gaping, loose, slack '? be based 
on, is perhaps mentionable; after Meillet Esquisse 36 rather to Armenian Aa/'game', xai^ai 
" peaceful, friendly ' (with Indo Germanic kh-)\ 



Maybe alb. ndar cease, stop, halt, desist ' [common alb. gh- > d-] : gr. xaAaoo " reduce, 
decrease, become limp '. 

Old High German gan{= Old Indie hana-m) "go'. Old Frisian Old Saxon Old English gan. 
Old Swedish Old Danish ga, Crimean Gothic geends.; about the additional form Old High 
German gens. Kluge'''' 193, Braune Old High German Gr.s p. 382''; Lithuanian by Feist, 
182 b. 

With the meaning- coloring A: 

gr. *xnT'c; (Risch word formation d. hom. Spr. 74), Dat. xHtsi " in absence of, lack of ', 
ablaut. {*gha-t-) xareaj, xQTi^u) 'lack, need, long for, yearn for, lust, desire'; xnpo<; " stolen; 
looted, empty, bare, lacking' (= Latin ^M/r*- in hems), xnpa " orphan, widow'; with gradation 
X(I)po(;, xwpa ' empty, free room, free country (in contrast to town, city), region', epid. 
Xcbpa ' empty eye socket ', xwpi<; Adv. and preposition m.Gen. 'apart, separated; without; 
with exception from; besides', x^pi^u) "slit, separate', xwpsTv "catch, can absorb, from 
container' (actually "make room') and " withdraw, leave, depart; go forever '; 

Gothic ga/dwn. "lack'. Old English gad, gsedn. "lack, need, desire'. Old Frisian gad' 
necessary'. Old Saxon Gen. PI. mef/gedeono' lack of food, famine' (basic form *ghai-tu6-); 
in addition probably also Old High German geisini' indigence, penury, necessity, want ', 
Old English gaesne' lacking, missing'; 

References: WP. I 542 ff., WH. I 451 , 641 f. 
Page(s): 418-419 

Root / lemma: ghe-2. gha- and ghei- : ghT- 

Meaning: to gape, yawn 

Note: onomatopoeic for the yawning sound (in addition the further formation stem ghn-a); 

(see also under ghans- "goose '; similarly, but with Velar, gha ghaior gaggle, cackle, 

chitchat, talk, snicker and likewise, see there). Beside ghei- also gheu-: ghsu- (see there), 

either as other perception of yawning sound, or with originally formant u. 

(eval):2: ==== not found
```


## [2026-09-05T20:54:41.687Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '37430,37650p' POK_full.txt"
}
```


### [2026-09-05T20:54:41.750Z] TOOL RESULT

```
Meaning: to gape, yawn 

Note: onomatopoeic for the yawning sound (in addition the further formation stem ghn-a); 

(see also under ghans- "goose '; similarly, but with Velar, gha ghaior gaggle, cackle, 

chitchat, talk, snicker and likewise, see there). Beside ghei- also gheu-: ghsu- (see there), 

either as other perception of yawning sound, or with originally formant u. 

Material: Gr. xaoKU) {gha-skd) " yawn, gape' (only present and Impf.; later replaced by 

xaivu), see below ghan-), xaa|ja " gaping mouth '; xnpci|JO(; "hole', xnpaMU'^ a big, giant 

shell ', after xapaijoqn Tpq yf|(; SiaaraaK; Hes., x^Koc, f. " hutch, chest; drawer '; xHMn " the 

yawn, mussel living in the coral seas, mussel whose bowls have a leafy surface '. 

Maybe alb. {gha-sko) guaske' shell ' a Greek loanword. 

Von ghei- from: Old Church Slavic zejg " to gape wide ' {*gheid). 



Von gM-a-irom: 

Latin h/'o, -are {*gh//a-/dj^ yawn, gape, be open ', Oscan eehianasum^ emittendamm 
(an animal sacrificed, victim, sacrifice) ', Umbrian ehiato^ let go, let loose, release, drop, 
let out"; 

Lithuanian zi6-ju, -//"open', reflexive ziotis^ ^jb^nv^ ' {zi6tysP\. f. "crack, deep cleft, gap; 
mouth, jaw '), wherefore Lithuanian ziovauti, Latvian zavaties^ yawn ' {zavasi. PI. " yawns 
') 

and with p.- Lithuanian ziopsau, -soti^ sit there, remain with open mouth '; 

Serbo-Croatian zjam, zjati^ open the mouth', iterative Old Church Slavic zijaj^, zijati, 
russ. zijaju, -atb ds. and sloven. zevatT hold the mouth open ', Czech zivati, russ. zevatb " 
yawn ' (sloven, zev, poln. ziew, russ. zei/" jaw '); 

with p (compare under the root form gheip-): big. zepam, poln. ziepac^ breathe with 
difficulty ', kir. zfpaty^ struggle for breath ', Czech z/p5//"pant, gasp'. 

similarly, but after e-verbs. Old High German gTen^ ^i^^nv^ ' (would be Gothic *gijan, - 
aida); besides with still the need for clarification (but barely deriving from from the root 
form gheu-) w\v\ Hiat Old High German anagiwen^ gape, be open mouthed with 
astonishment, covet, desire ', gewon' open the mouth, yawn ' (Middle High German 
gewen, giwen6s.). Old English giwian, giowian^\ov\Q, want, arrogate' (from " *with open 
mouth, greedy whereupon pant for, long for, desire '); in addition Old Icelandic gjat 
{*giwd) on the one hand "col, gap, cleft, gap in the earth', on the other hand (from " pant 
for, long for, desire ' from) " voluptuous life'. Middle High German giude {* giwiPo) " loud 
pleasure, joy', giuden^ boast, brag (*open the mouth wide); be in noisy joy, live wastefully 
', Modern High German vergeuden; Old High German inginnan^ open up, open, lacerate, 
split' from *ginuan\s probably Causative to Old High German g/nen{see below) in formal 
connection with the similar sound biginnan. (under the influence of common Celtic -ns-, - 
nt- > -nn-). 

sAropresent: Latin hTsco, -ere{*ghhsRd) " yawn, gape, be open '; similarly Old English 
giscian. Middle High German gischen^ sob, weeping ' and Norwegian Dialectal geiska^ 
stretch the legs ' (see Persson Beitr. 318). 

/^ present and related nouns: Old Icelandic ^/77astem V., Old English to-glhan stem V. 
"gape, yawn '; with /Old Icelandic ^//7e, Old High German ginen. Middle High German 
ginen, genen. Modern High German gahnen= Old English ginian, gionian^ be far open ', 



Old Icelandic gina^ yawn ', ^//7n. "gullet', Old English ^//7n. ds.; with Germanic a/(lndo 
Germanic ghei-l or rather the preterite ablaut of stem V. gJnarR) Old High German geinon, 
Swiss gaine, Gothic *gainon. Old English ganian; but engl. yawn^ yawn ' for *yone irom 
Old English gionian; 

Old Church Slavic zing, -Qti{*ghTnd) " yawn, gape '. 

other nominal formation: 

with Lf. Old English giw, geowm. " vulture' {*gTwaz^\he voracious '); 

with m: Old Icelandic g/mat " cleft, mouth ', Swiss gTm ds.; Old Icelandic geimixw. " 

r 

|Vleeresschlund '; nisi, geimr^ big, empty room'; 

with r. Germanic *gTr{i)a- " greedy ' (actually "* long for, desire '), in Norwegian Dialectal 
gTrm. " eagerness, ferventness, passion'. Old High German gTri^ eager, avid', gTr ' vulture\ 

with / Old Icelandic Norwegian gilu. " cliff crack ', Swedish Dialectal giljai. " defile, 
narrow passage between mountains'. Old High German Middle High German giTbreak, 
hernia'; Old Icelandic geili. " defile, narrow passage between mountains, Engpaft'; Middle 
Low German gTlen^\\}s\., crave, beg' (from *gTla- Adj. " yearning', compare to meaning 
above Old English gTwa^. 

With meaning-development from "gape' to " stand crookedly (at first e.g. from woods )' 
probably to be added ndd. Dutch gillen " abscise slantwise ', Dutch gillinghouV cut through 
wood at an angle ', further isl. ^e//a "separate' (" *make gape '), Old English gaelan 
{*gailjan) "hinder, hesitate'; from r-forms Low German gTren, Dutch (out of it Modern High 
German) gieren, Norwegian Dialectal gTra^ deviate from the course '; Dutch geerends., 
Norwegian Dialectal geira' run crookedly '. 

extensions with /-vocalism: 

*ghei-gh- : Old Icelandic Norwegian dial., geiga^ deviate sideways ', Old Icelandic geigr 
m. "damage' (originally outlook "* stand crookedly, gape' e.g. from woods); compare 
Modern High German Swiss Geigle^ double branch in a tree which breaks up in any 
corner; PI. the thighs ', Modern High German Heugeige^ Stecken mit seitwarts 
abstehenden Astresten zum Aufschobern des Heus '; Modern High German dial, geigen^ 
move to and fro ', Old Icelandic gTgJa, from Middle Low German Middle High German gTge, 
Modern High German Geigeas musical instrument; Old English for-, of-gsegan^ deviate 
from, overstep ', g^glaud gagoF exuberant, bending ', Old Frisian geia^ contravene. 



refrain from, desist from, penance, atonement pay for, atone'; Norwegian dial, giga, gigia, 
g/gralose stand, wobble, sway', engl. g/g{nord. loanword) " light cart, light racing boat ', 
whirligig, Danish gig^ spinning top as plaything '; ndd. giggelen, engl. to giggie^ titter, 
laugh in a foolish high-pitched manner, furtive, sneering laugh '; as " sticking out freely, 
movable sail pole ' here Dutch gei^ Raa ' (basic form geig(*j)a?), ndd. gTI<, Dutch gi/k ds. 
and Middle Low German gec/cirom revolvable things (e.g. lid, top, cover, shutter. 
Pumpman gen), also 'fool' (Modern High German Gecl<); here (after Wissmann Nom. 
postverb. 41) Gothic geigoi. 'greed, lust', ga-geigan^ gain ', faiiiu-geigan^\us\., crave'; s. 
S. 427. 

similar is (from giina- from) with ^/7 shaped Lithuanian ziogautr \/a\Nn ', ziogas' locust, 
grasshopper ', ziogris ' palisade, fence made from stakes; protective fence made from 
poles that are inserted into the ground '. 

gfiei-p-(\u Germanic perhaps partly also ghei-b^-): 

Maybe with i&-formant alb {* gtiei-bo-n) zfigabonje, stiqiponje^ (greedy, voracious) eagle, 
vulture ' : Old English giw, geowm. ' vulture' : Old High German gTr ' vulture' 

Latin (Gloss.) hippitare, exippitare (*hJpitare)^ hietare, gape; yawn ' (span, hlpar^ sob, 
weeping '); Czech z/pa//'pant, gasp' (etc., see above); 

Old English gTfer^ devourer'. Old Icelandic ^/T^m. 'fiend, demon'; Modern High German 
dial, geifen, geiben, geipen' yawn, gawk, desire greedily '; from ' stand crookedly, stand 
loose ' Norwegian dial, geivia ' deviate sideways; shiver', also geivra, from stretching the 
mouth ndd. gib(b)elen^ mocking laugh ', Modern High German geifeln^ mocking laugh ', 
engl. to gibe, jibe ' mock '. 

In Germanic also: 

ghei-b-, Germanic *glp-:0\d Icelandic gTprm. 'muzzle, jaw ', FIN for Gipa, Norwegian 
Dialectal gipa^ make gape, struggle for breath ' = Old English gTpian^ struggle for breath '; 
Middle Low German gippelt^ crazy, stupid'; Swedish dial, gippa^ cmck, col, gap'; with /" 
schwed dial, gipa^ stretch the mouth ', ndd. gTpen^ struggle for breath '; Modern High 
German Bavarian gaif(f)en yor\ einem nichtfestsitzenden, schlotternden Schuh; with the 
meaning ' twist mockingly the mouth '. 

With Germanic ai Old Icelandic geipa^ babble, chatter', Norwegian dial, geipa^ 
chatter; open the mouth wide; sit or go with spread legs ' ; 



Old Icelandic geispa^ struggle for breath ', Middle English gaspen< Old English 
*gaspian, probably from *^a/pso/7 (through amalgamation from *gaip-av\6 *gais). 

gheis-:\s\. gisinn^ leaking, cracked from dryness ' (participle from *gfsa=) Norwegian 
dial, g/sa' grin, blink'; Norwegian dial, g/sfa 'get split, become thin, of the wood ', Old 
Swedish gistinn' leaking, cracked from dryness '; from this meaning further Middle Low 
German gest. Old Frisian gest, gasV the higher dry land in contrast to marsh depression ' 
(related ^-forms Low German guste, Dutch gust' infertile, dry, gelt' from the basis gheu-?? 
S. Persson Beitr. 318). 

extensions with e- : a-vocalism (fast only Germanic): 

*ghagh- (: ghegh-): 

Old English geaglm. n. "mandible, lower jaw bone, throat', PI. ' grinder, molar tooth ', 
Middle Low German gagel, gegelm. n. " palate, gums' {*gagula-, -ila)\ 

Modern High German dial, gagen, gagein, gagern "spread themselves (from the legs, 
the fingers), wobble, gesticulate, flutter', gackelicht'ioo\\s\\, loony'. Middle High German 
gagen, gageren' move to and fro, thrash, wriggle ', Old Icelandic gagr' writhed, crooked, 
humped, crooked behind ', gaghals' back crooked neck ', Norwegian dial, gag' crooked 
backward (e.g., from crooked standing off device parts) ', engl. gag-toothed {nor6. 
loanword) " with protruding teeth ': ablaut. Old Icelandic gsegjask' prestretch oneself to 
look ', and (both with consonant-sharpening) md. gaken'gawk'. ' ' 

Maybe alb. guak' gawk ', expressive form alb. {*gha-skS), gogesij' yawn, gape ' 

Old Icelandic gjggrarP\. " cliff gaps ' {*gegura-) compares Liden Armen. Stud. 70 f. 
probably more properly with Armenian gez' co\, gap, crack, incisure '. 

*ghep-: 

Old Indie haphika' echo, resound, ring ' (with new p/? instead of p, Persson Beitr. 565). 

*gh9b-:0\^ Icelandic gap' wide aperture, hole, chaos; shout, call, scream ', gapa' 
open the mouth, cry'. Old English gapian, ndd. gapen. Middle High German Modern High 
German gaffen' look with open mouth '. 



*gtido 



h.- 



Old English geaflas PI. " jaws ' (in the meaning directed after ceafr jaw ', see below 
geph^. Old Danish paa gafle^^eW offen', Swedish pa gavel 6s. 

Maybe Latin {*gnoffula) offula{-ae) [n] " slice ' : alb. nofulla^ jaw ' : Rumanian falca^ jaw '. 

Old Icelandic gabba^ play jokes, play a joke on, fool ', Old English gabbian ^b3ibb\e\ 
deride, mock ', gaffetung^ derision ', gafspraec^ brainless speech ', Dutch gabberen^ trifle, 
joke ' (probably from Ndd. derive Lithuanian gabl(i)6-ju, -ti^ banter, vex ', gablys^ one who 
teases, vexes ', s. Berneker287 f. - also about poln. gabac^sKyx, tease, irritate, banter'). 

References: WP. I 548 ff., WH. I 647 ff., Trautmann 368, Schwyzer Gr. Gr. I 694. 
See also: compare still ghe-1 " empty, bare, lacking sein, fehlen'; Specht (Dekl. 282) 
places eine root *agh-e-eic. an; see above under ghan-. 
Page(s): 419-422 

Root / lemma: ghe/a
```


## [2026-09-05T20:55:10.768Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^cephal\" KLN_1966.txt | head -20\necho \"--- context ---\"\ngrep -n -i \"qifal\\|qifāl\\|kifal\\|cephalic vein\\|Avicenna\" KLN_1966.txt | head -20"
}
```


### [2026-09-05T20:55:10.844Z] TOOL RESULT

```
6991:cephalate,  adj.,  having  a  head.  —  See  cephalic and  adj.  suff.  -ate.
6992:cephalic,  adj.,  pertaining  to  the  head.  F.  ce- phalique,  fr.  L.  cephalicus,  fr.  Gk.  xccpaXixip, ‘pertaining  to  the  head’,  fr.  xetpaXfj,  ‘head’,  dis- similated  fr.  *ye<paXf),  fr.  I.-E.  base  *ghebel-, whence  also  Toch.  A  spat-,  ‘head’,  Goth,  gibla, ON.  gafl,  ‘gable’,  OE.  gafol,  ‘fork’.  See  gable and  -ic  and  cp.  Acanthocephala,  acephalous, acrocephalic,  anencephalic,  autocephalous,  bi¬ cephalous,  Bucephalus,  dolichocephalic,  Draco- cephalum,  encephalic,  encephalon,  Enchelyce- phali,  hydrocephalus,  isocephalic,  macrocephalic, megacephalic,  mesocephalic,  microcephalous, orthocephalic.
6993:cephalic  vein  (anat.)  —  ML.  vena  cephalica,  fr. Arab,  al-qif&l,  fr.  al-,  ‘the’,  and  qifdl,  a  word  of uncertain  origin,  which  was  confused  by  the translators  of  Avicenna  with  Gk.  xccpxXr,,  ‘head’ (whence  xetj>aXtx6i;,  ‘pertaining  to  the  head,  see prec.  word).  The  word  cephalic  in  its  above sense  appears  first  in  a  translation  of  Avicenna by  Armegandus  Blasius  de  Montepessulano  in 1564.  See  Joseph  Hyrtl,  Das  Arabische  und HebraischcinderAnatomie.Wien,  1879, p.96-98. cephalo-,  before  a  vowel  cephal-,  combining  form meaning  ‘head,  with  reference  to  the  head’.  — Gk.  xe9<xXo-,  xEtpaX-,  fr.  xEtpaXf),  ‘head’.  See cephalic.
6994:cephaloid,  adj.,  shaped  like  a  head.  —  Gk.  xetpa- XoeiS 7)4,  fr.  xeq>aXf),  ‘head’,  and  -osiSrjp,  ‘like’, fr.  elSoi;.  ‘form,  shape’.  See  cephalic  and  -oid. cephalopod,  n.,  one  of  the  Cephalopoda.  —  See next  word.
22477:cephalic.  —  See  prec.  word  and  -y  (representing Gk.-ia).
--- context ---
1276:Abutilon,  n.,  a  genus  of  plants  of  the  mallow family  (hot.)  —  ModL.,  fr.  Arab,  aubutildn,  a name  coined  by  the  Arab  philosopher  Avicenna (=  Ibn-Sina).
4117:aviator,  n.  —  Refashioned  after  F.  aviateur.  See prec.  word  and  agential  suff.  -or. aviatress,  aviatrix,  n.,  a  woman  aviator.  —  For¬ med  fr.  aviator  with  suff.  -ess,  resp.  -trix. Avicennism,  n.,  the  teachings  of  the  Arab,  philo¬ sopher  Avicenna  (=  Ibn  Sina)  (980-1037).  For the  ending  see  suff.  -ism.
4519:basilica,  n.  —  L.,  ‘a  public  hall  with  double  co¬ lonnades’,  fr.  Gk.  PxctXixY)  (scil.  rrxox),  lit. royal  colonnade’,  fern,  of  PaaiXixo?,  ‘kingly, royal’,  fr.  PaoiXeii?,  ‘king’,  which  is  of  un¬ certain  origin.  It  is  possibly  a  loan  word  from a  language  of  Asia  Minor;  cp.  Lydian  paxxo?, king’.  Cp.  basil,  the  plant,  basilisk, basilic  vein  ( anat .)  —  ML.  vena  basilica,  fr.  Arab, r il-basiltq ,  fr.  «/-,  ‘the’,  and  bdsilfq ,  a  word  of uncertain  origin,  which  was  confused  by  the translators  of  Avicenna  with  Gk.  paaiAncop, ‘royal’  (see  prec.  word).  The  term  vena  basilica appears  for  the  first  time  in  a  translation  of  Avi¬ cenna  by  Gerardus  Cremonensis.  See  Joseph Hyrtl,  Das  Arabische  und  Hebraische  in  der Anatomic,  Wien,  1879,  pp. 74-77. basilisk,  n.,  a  mythical  serpent,  cockatrice;  a Central  American  lizard.  —  L.  basiliscus,  fr.  Gk. fixmAlaxo?,  ‘princelet,  chieftain,  basilisk’,  di- min.  of  pacrtXc'j?,  ‘king’;  so  called  after  Pliny, Naturalis  Historia,  8,  33,  from  ist  ‘crown’,  i.e. a  white  spot  on  its  head.  See  basilica  and  cp. the  second  element  in  aspic,  ‘asp’, basin,  n.  — ■  ME.,  fr.  OF.  bacin,  bassin  (F.  bassin), fr.  VL.  *baccinum,  fr.  bacchinon  (cited  by  Gre¬ gory  of  Tours  as  a  vulgar  word),  fr.  *bacca, ‘a  water  vessel’  (whence  F.  bac,  ‘vat’).  See back,  ‘vat’,  and  cp.  next  word, basinet,  n.,  a  light  steel  helmet,  later  made  with a  visor.  —  ME.,  fr.  OF.  baciner,  bassinet  (F.  bas¬ sinet),  dimin.  of  bacin,  bassin  (F.  bassin ),  ‘basin’. See  prec.  word  and  -et,  and  cp.  bassinet, basis,  n.  —  L.,  fr.  Gk.  pa  at?.  See  base,  n. bask,  intr.  and  tr.  v.  —  ME.  basken,  fr.  ON.  bada- sk,  a  reflexive  verb  lit.  meaning  ‘to  bathe  one¬ self’,  fr.  bada,  ‘to  bathe’  (see  bathe),  and  reflex, suff.  -sk.
6993:cephalic  vein  (anat.)  —  ML.  vena  cephalica,  fr. Arab,  al-qif&l,  fr.  al-,  ‘the’,  and  qifdl,  a  word  of uncertain  origin,  which  was  confused  by  the translators  of  Avicenna  with  Gk.  xccpxXr,,  ‘head’ (whence  xetj>aXtx6i;,  ‘pertaining  to  the  head,  see prec.  word).  The  word  cephalic  in  its  above sense  appears  first  in  a  translation  of  Avicenna by  Armegandus  Blasius  de  Montepessulano  in 1564.  See  Joseph  Hyrtl,  Das  Arabische  und HebraischcinderAnatomie.Wien,  1879, p.96-98. cephalo-,  before  a  vowel  cephal-,  combining  form meaning  ‘head,  with  reference  to  the  head’.  — Gk.  xe9<xXo-,  xEtpaX-,  fr.  xEtpaXf),  ‘head’.  See cephalic.
7863:Claviceps,  n.,  a  genus  of  sac  fungi  (bot.)  —  ModL., compounded  of  L.  clava,  ‘club’,  and  -ceps, ‘-headed",  fr.  L.  caput,  ‘head’.  See  clava  and capital,  adj.  For  the  change  of  Latin  a  (in  caput) to  e  (in  -ceps)  see  biceps. clavichord,  n.,  an  early  keyboard  instrument.  — ML.  davichordium,  compounded  of  L.  clavis, ‘key’,  and  chorda,  ‘string’.  See  clavicle  and  chord, clavicle,  n.,  the  collarbone.  —  F.  clavicule,  fr.  Late L.  cldvicula,  ‘a  little  key,  bar,  bolt,  tendril’,  dimin. of  L.  clavis,  ‘key’,  which  is  rel.  to  clavus,  ‘nail’, claudere,  ‘to  shut’.  In  its  anatomical  sense  Late L.  cldvicula  was  first  used  by  the  translators of  Avicenna  about  the  year  980.  See  close,  adj., and  cp.  chiave,  clavelization,  clavier,  clavis,  clef, autoclave,  conclave,  enclave,  kevel,  laticlave, subclavian.  Cp.  also  lot.
12449:duodenitis,  n.,  inflammation  of  the  duodenum (med.)  —  A  Medical  L.  hybrid  coined  fr.  duo¬ denum  and  -itis,  a  suff.  of  Greek  origin, duodeno-,  combining  form,  meaning  ‘referring  to the  duodenum’.  —  See  next  word, duodenum,  n.,  the  first  part  of  the  small  intestine leading  from  the  stomach  to  the  jejunum  (ana¬ tomy).  —  ML.  duodenum,  coined  by  Gerard  of Cremona  (died  in  1187),  the  translator  of  the Canon  Avicennae,  fr.  L.  duodeni,  ‘twelve  each’, fr.  duo,  ‘two’,  and  deni,  ‘ten  each’*  which  is  rel.  to
23273:Median,  adj.,  pertaining  to  Media;  n.,  1)  a  Mede ; 2)  the  language  of  ancient  Media.  —  Formed with  suff.  -an  fr.  Gk.  MrjSio?,  ‘of  Media’,  fr. MrjSo;.  See  Mede  and  cp.  Medic, median  vein  ( anat .)  —  L-  vena  mediana.  Accord¬ ing  to  Joseph  Hyrtl  (in  his  Onomatologia  anato- mica,  p.  320),  these  words  do  not  mean  ‘the middle  vein’,  but  are  derived  from  the  name  of Al-Madyan,  ibn  Abderrahman,  a  commentator of  Avicenna’s  Canticum.  So  arose  the  term ‘vein  of  Al-Madyan',  whence  Armegandus coined  the  name  vena  mediana,  which  was  mis¬ interpreted  later  as  ‘the  middle  vein’  (see  median). mediant,  n.,  the  third  note  of  the  diatonic  scale (music).  —  It.  mediante,  fr.  Late  L.  mediantem, acc.  of  medians,  ‘dividing  in  the  middle’,  pres, part,  of  medidre;  so  called  as  being  midway  be¬ tween  the  tonic  and  the  dominant.  See  mediate, adj.,  and  -ant.
26471:orbicular,  adj.,  having  the  shape  of  an  orb;  spher¬ ical.  —  ME.  orbiculer,  fr.  Late  L.  orbicularis, ‘circular,  orbicular’,  fr.  L.  orbiculus ,  dimin.  of orbis.  See  orb  and  the  suffixes  -cule  and  -ar. orbiculate,  orbiculated,  adj.,  orbicular.  —  See prec.  word  and  adj.  suff.  -ate,  resp.  also  -ed. orbit,  n.,  the  eye  socket  ( anat .)  —  L.  orbita,  ‘a track  or  rut  made  in  the  ground  by  a  wheel’,  fr. orbis',  see  orb.  In  its  anatomical  sense  the  word orbita  was  first  used  by  Gerard  of  Cremona,  the translator  of  Avicenna’s  Canon.  Cp.  periorbita. Derivatives:  orbit-al,  orbit-ary,  adjs. orbito-,  combining  form  denoting  the  orbit  (anat.) —  See  prec.  word.
```


## [2026-09-05T20:55:21.281Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\np='KLN_1966.txt'\nt=open(p,encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor tgt in [6991,4519,22477]:\n    pre='\\n'.join(lines[:tgt])\n    leaf=pre.count('\\f')\n    print(tgt,'leaf',leaf,'est printed p', (leaf-12)*2, 'to', (leaf-12)*2+1)\nEOF"
}
```


### [2026-09-05T20:55:23.225Z] TOOL RESULT

```
6991 leaf 147 est printed p 270 to 271
4519 leaf 91 est printed p 158 to 159
22477 leaf 494 est printed p 964 to 965
```


## [2026-09-05T20:55:27.600Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in (146,147,148):\n    L=leaves[i]\n    print('=== leaf',i,'len',len(L))\n    print(L[:300].replace('\\n',' | '))\n    print('...TAIL...', L[-300:].replace('\\n',' | '))\nEOF"
}
```


### [2026-09-05T20:55:29.475Z] TOOL RESULT

```
=== leaf 146 len 11778
  whole  and  cp.  words  there  referred  to.  For derivatives  of  I.-E.  *leip-  see  leave,  v.,  and  cp. | 256 | 257 | esp.  life,  live.  Derivative;  celibat-ic,  adj. celio-,  combining  form.  —  A  variant  spelling  of coelio-. | cell,  n.  —  ME.  cede,  fr.  OF.  cede,  fr.  L.  cella, ‘storer
...TAIL...   plant, whence  its  name  xcvxaupeiav  or  xevxaupiov, ‘Centaur's  plant’  (see  centaur).  In  Latin,  folk etymology  altered  the  foreign  word  into  the compound  of  the  Latin  words  centum,  ‘hundred’, and  aurum,  ‘gold’.  As  a  loan  translation  of  L. centaureum  in  this  mistaken 
=== leaf 147 len 11340
 sense,  arose  G. Tausendgiildenkraut,  ‘centaury’,  lit.  ‘thousand- golden-herb’. | centenarian,  adj.,  pertaining  to  a  period  of  a hundred  years;  n.,  a  person  one  hundred  years old.  —  L.  centendrius,  ‘relating  to  a  hundred’,  fr. centeni,  ‘a  hundred  each’,  fr.  centum,  ‘a 
...TAIL... with  suff.  -aceae  fr.  Ceramium. ceramiaceous,  adj.  —  See  prec.  word  and  -aceous. ceramic,  adj.,  i)  of  pottery;  2)  of  ceramics.  — Gk.  y.Epxjxtxop,  ‘of  pottery,  made  of  earthen¬ ware’,  fr.  xEpauop,  ‘earthen  vessel,  jar,  potter’s clay,  pottery’,  a  pre-Hellenic  word  d
=== leaf 148 len 11704
erived  from a  language  of  Asia  Minor  and  not  cognate  with L.  cremdre,  ‘to  burn’.  See  Kretschmer,  Glotta, | 1 1 ,  284,  and  Schrader,  Reallexikon  der  indo- germanischen  Altertumskunde  IF,  694.  Cp. Ceramium,  and  the  second  element  in  Inoce- ramus. | ceramics,  n.,  1)  the  a
...TAIL... and ypatpeoi,  ‘to  write’.  See  cere,  n.,  and  -graphy. Derivatives:  cerograph-ie,  cerograph-ic-al,  adjs., cerograph-ist,  n. | cerolite,  n.,  a  hydrous  magnesium  silicate  (min¬ eral.)  —  Compounded  of  cero-  and  -lite;  so called  in  allusion  to  its  waxy  appearance, ceroplastic,
```


## [2026-09-05T20:55:35.305Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"ghebh-el\\|ghebhel\\|^ghebh\" AHD_watkins1985.txt | head\necho \"=== ghe- ===\"\ngrep -n \"^ghē-\\|^ghe-\\|^ghēi-\\|^ghei-\" AHD_watkins1985.txt | head -20\necho \"=== gable ===\"\ngrep -n -i \"gable\" AHD_watkins1985.txt | head"
}
```


### [2026-09-05T20:55:35.377Z] TOOL RESULT

```
510:*ghait-d in Greek khaité, long hair: CHAETA; (CHAETOG- NATH). [Pok. ghait-d- 410.] ghalgh-. Branch, rod. Germanic *galgon- in: a. Old English g(e)alga, cross, gallows: GALLOWS; b. Old North French gauge, gauge: GAUGE. [Pok. ghalgh- 411.] ghans-. Goose. 1. Germanic *gans- (nominative plural *gansiz) in: a. Old English gds (nominative plural gés), goose: GOOSE!; (GOSHAWK); b. Old Norse gas, goose, diminutive geslingr, gosling: GOSLING. 2. Germanic *ganr- in Old English ganra, gandra, gander: GANDER. 3. Germanic *gandton- in Old English ganot, gannet: GANNET. 4, Suffixed form *ghans-er- in Latin dnser (< *hanser), goose: ANSERINE; MERGANSER. 5. Basic form *ghans- in Greek khén, goose: CHENOPOD. [Pok. ghans- 412.) ghasto-. Rod, staff. 1. Variant form *ghazdh- in Ger- manic *gazdaz in: a. Old English gierd, gerd, staff, twig, measuring rod: YARD}; b. Old Norse gaddr, rod, goad, spike: GAD?. 2. Form “ghast-d- in Latin hasta, spear: HASLET, HASTATE. [Pok. 1. ghasto- 412.] ghé-. To release, let go; (in the middle voice) to be released, go. Contracted from *ghea-. 1. Germanic vari- ant form *gaian in Old English gdn, to go: GO; AGO, FOREGO!, FoRGO. 2. Suffixed form *ghé-ro- in Latin hérés, heir (? < “orphan” < “bereft”):; HEIR, HEREDITA- MENT, HEREDITY, HERITAGE; INHERIT. 3. Suffixed o-grade form *ghé-ro-, “empty space,” possibly in: a. Greek khéros, place, country, particular spot: CHO- ROGRAPHY; b. Greek denominative khorein, to move, go, spread about, make room for: -CHORE; ANCHORITE. 4. Perhaps suffixed zero-grade form *gha-l- in Greek khalan, to slacken, let down (but this is more likely of unknown origin): CALANDO, CHALONE; ACHALASIA. 5. Suffixed zero-grade form *gho-t(w)d- in Germanic *gatwon-, a going, in Old Norse gata, path, street: GAIT. [Pok. ghé- 418.] ghebh-el-. Head. 1. Germanic *gablaz, top of a pitched roof, in Old Norse gafl, gable: GABLE. 2. Dissimilated form *khephel- in Greek kephalé, head: CEPHALIC, CEPH- ALO-, -CEPHALOUS; ENCEPHALO-, ENKEPHALIN, HYDRO- CEPHALUS. [Pok. ghebh-el- 423.] ghedh-. To unite, join, fit. 1. Lengthened o-grade form *ghédh- in Germanic *gédaz, “fitting, suitable,” in Old English géd, good: GooD. 2. Germanic *gaduri, “in a body,” in Old English tégezdere (t6, to; see de-), together: TOGETHER. 3. Germanic “gadurén, “to come or bring together,” in Old English gad(e)rian, to gather: GATHER. [Pok. ghedh- 423.] ghei-'. To propel, prick. 1. Suffixed and extended o-grade form *ghoidh-d in Germanic *gaidé, goad, spear, in Old English gdd, goad: GOAD. 2. Suffixed form *ghei-s- per- haps in nasalized zero-grade form *ghi-n-s- in Sanskrit himsati, he injures: AHIMSA. [Pok. 1. ghei- 424.] ghei-2. Theoretical base of *ghyem-, *ghiem-, winter. 1. Form *ghiem- in Latin hiems, winter: HIEMAL. 2. Suf- fixed variant form *gheim-ri-no- in Latin hibernus, pertaining to winter: HIBERNACULUM, HIBERNATE. 3. Suffixed zero-grade form *ghim-ar-ya, “female animal one year (winter) old,” in Greek khimaira, she-goat: CHIMERA. [Pok. 2. ghei- 425.] gheis-. Used of the emotion of fear or amazement (origi- nal part of speech uncertain). Suffixed o-grade form *ghois-do- in Germanic *gaistaz, a ghost, in: a. Old English gdst, ghost: GHOST; AGHAST; b. Old High Ger- man geist, ghost: POLTERGEIST; Cc. Germanic denomina- tive *gaistjan in Old English g&stan, to scare: GAST. [Pok. gheis- 427.] ghel-'. To call. 1. Germanic “gel-, *gal-, in: a. Old Eng- lish gellan, giellan, to sound, shout: YELL; b. Old English gielpan, to boast, exult: YELP; c. Old English galan, to sing: NIGHTINGALE. 2. Reduplicated form *ghi-ghl- in Greek kikhilé, thrush, later also the name for a kind of wrasse (a sea fish that has bright colors and jagged waving fins, reminiscent of the plumage of a bird):
1342:CENTROBARIC gWere-2 CENTUM dekm CENTURY dekm CEPHALIC ghebh-el- CEPHALO- ghebh-el- -CEPHALOUS ghebh-el- CERAMIC ker-4 CERASTES ker-! CERATODUS dent-, ker-1 CERATOID ker-! CEREAL ker-3 CEREBELLUM ker-1 CEREBRUM ker-1 CERES ker-3 CERTAIN krei- CERVINE ker-1 CERVIX ker-1 CESSION ked- CESSPOOL spirare cEsTus! kent- CEsTUS? kae-id- CHAETA ghait- CHAETOGNATH genu-2, ghait- CHAFE dhé-1, kele-1 CHAFER gep(h)- CHAFF! gep(h)- CHAIR sed-1 CHALAZA gheled- CHALAZION gheled- CHALCID ghelegh- CHALCOCITE ghelegh- CHALCOPYRITE ghelegh- CHALCOsIS ghelegh- CHALICE kal-1 CHALLENGE kel-8 CHALONE ghé- CHAMAEPHYTE dhghem- CHAMBER kamer- CHAMELEON dhghem- CHAMFER bhreg- CHAMFRON kaput CHAMOMILE dhghem-, mélon CHANCE kad- CHANCEL carcer CHANCELLOR carcer CHANCRE kar-1 CHANGE skamb- CHANT kan-
1456:ENAMEL mel-1 ENAMOR amma ENANTIOMER §ant- ENANTIOMORPH ant- ENARTHROSIS at- ENATE gene- ENCAUSTIC kéu- ENCEINTE? kenk-1 ENCEPHALO- ghebh-el- ENCHANT kan- ENCHASE kap- ENCHIRIDION ghesor- ENCLAVE kleu-3 ENCLITIC klei- ENCOUNTER kom ENCROACH ger-2 ENCYCLICAL kwel-1 ENCYCLOPEDIA pau- END ant- ENDEAVOR ghabh- ENDEMIC da- ENDERGONIC werg- ENDOCARDIUM kerd-1 ENDOCRINE krei- ENDOERGIC werg- ENDORSE dorsum ENDOSTEUM ost- ENDOTHECIUM dhé-1 ENDOTHELIUM dhé@(i)- ENDOW do- ENDUE deuk-, eu-1 ENDURE deru ENEMA yé-
1460:ENKEPHALIN en, ghebh-el-
1550:GABERDINE per-2, wel-3 GABFEST dhés- GABION keue-2 GABLE ghebh-el- GABRO gladh- GaD2 ghasto- GAEA gé
1658:HUM kem-3 HUMAN dhghem- HUMANE dhghem- HUMBLE dhghem- HUMECTANT wegw- HUMERUS omeso- HUMID wegw- HUMILIATE dhghem- HUMILITY dhghem- HUMOR wegw- HUMUS dhghem- HUNDRED dekm HUNGER kenk-2 HUNKER keu-2 HURDLE kert- HUSBAND bheue- HUSSAR kers-2 HUSTINGS tenk-1 HUT (s)keu- HYATHODE sed-2 HYDATHODE wed-1 HYDATID wed-1 Hypra_ wed-! HYDRANT wed-! HYDRANTH andh- HYDRAULIC aulo- HYDRO- wed-1 HYDROCEPHALUS ghebh-el- HYDROMEL melit- HYDROUS wed-1 Hyprus_ wed-! HYENA sil- HYGEIA gWei- HYGIENE gWej- HYGRO- wegw- HYLOZOISM _hulé HYMEN  syil- HYMNODY wed-2 HYOSCINE si- HYPER- uper HYPERBOLA gWele-1 HYPERBOLE gWelg-1 HYPERBOREAN gWere-1 HYPERKINESIA kei-3 HYPERPNEA pneu- HYPHA webh- HYPNAGOGIC ag- HYPNO- swep-! Hypnos swep-! HYPNOSIS swep-1 HYPNOTIC swep-1 HYPO- upo HYPOCHONDRIA ghrendh- HYPOCORISM ker-3 HYPOGEAL gé HYPOPHYSIS bheue- HYPOPNEA pneu- HYPOSTASIS sta- HYPOSTYLE sta- HYPOTAXIS tag- HYPOTENUSE ten- HYPOTHERMIA gWher- HYPOTHESIS dhé-1 HYPROCRISY krei- HYPSO- upo HYSTERESIS ud- HYSTERIC udero- HYSTERO- udero- HYSTERON PROTERON per!, ud-
=== ghe- ===
=== gable ===
510:*ghait-d in Greek khaité, long hair: CHAETA; (CHAETOG- NATH). [Pok. ghait-d- 410.] ghalgh-. Branch, rod. Germanic *galgon- in: a. Old English g(e)alga, cross, gallows: GALLOWS; b. Old North French gauge, gauge: GAUGE. [Pok. ghalgh- 411.] ghans-. Goose. 1. Germanic *gans- (nominative plural *gansiz) in: a. Old English gds (nominative plural gés), goose: GOOSE!; (GOSHAWK); b. Old Norse gas, goose, diminutive geslingr, gosling: GOSLING. 2. Germanic *ganr- in Old English ganra, gandra, gander: GANDER. 3. Germanic *gandton- in Old English ganot, gannet: GANNET. 4, Suffixed form *ghans-er- in Latin dnser (< *hanser), goose: ANSERINE; MERGANSER. 5. Basic form *ghans- in Greek khén, goose: CHENOPOD. [Pok. ghans- 412.) ghasto-. Rod, staff. 1. Variant form *ghazdh- in Ger- manic *gazdaz in: a. Old English gierd, gerd, staff, twig, measuring rod: YARD}; b. Old Norse gaddr, rod, goad, spike: GAD?. 2. Form “ghast-d- in Latin hasta, spear: HASLET, HASTATE. [Pok. 1. ghasto- 412.] ghé-. To release, let go; (in the middle voice) to be released, go. Contracted from *ghea-. 1. Germanic vari- ant form *gaian in Old English gdn, to go: GO; AGO, FOREGO!, FoRGO. 2. Suffixed form *ghé-ro- in Latin hérés, heir (? < “orphan” < “bereft”):; HEIR, HEREDITA- MENT, HEREDITY, HERITAGE; INHERIT. 3. Suffixed o-grade form *ghé-ro-, “empty space,” possibly in: a. Greek khéros, place, country, particular spot: CHO- ROGRAPHY; b. Greek denominative khorein, to move, go, spread about, make room for: -CHORE; ANCHORITE. 4. Perhaps suffixed zero-grade form *gha-l- in Greek khalan, to slacken, let down (but this is more likely of unknown origin): CALANDO, CHALONE; ACHALASIA. 5. Suffixed zero-grade form *gho-t(w)d- in Germanic *gatwon-, a going, in Old Norse gata, path, street: GAIT. [Pok. ghé- 418.] ghebh-el-. Head. 1. Germanic *gablaz, top of a pitched roof, in Old Norse gafl, gable: GABLE. 2. Dissimilated form *khephel- in Greek kephalé, head: CEPHALIC, CEPH- ALO-, -CEPHALOUS; ENCEPHALO-, ENKEPHALIN, HYDRO- CEPHALUS. [Pok. ghebh-el- 423.] ghedh-. To unite, join, fit. 1. Lengthened o-grade form *ghédh- in Germanic *gédaz, “fitting, suitable,” in Old English géd, good: GooD. 2. Germanic *gaduri, “in a body,” in Old English tégezdere (t6, to; see de-), together: TOGETHER. 3. Germanic “gadurén, “to come or bring together,” in Old English gad(e)rian, to gather: GATHER. [Pok. ghedh- 423.] ghei-'. To propel, prick. 1. Suffixed and extended o-grade form *ghoidh-d in Germanic *gaidé, goad, spear, in Old English gdd, goad: GOAD. 2. Suffixed form *ghei-s- per- haps in nasalized zero-grade form *ghi-n-s- in Sanskrit himsati, he injures: AHIMSA. [Pok. 1. ghei- 424.] ghei-2. Theoretical base of *ghyem-, *ghiem-, winter. 1. Form *ghiem- in Latin hiems, winter: HIEMAL. 2. Suf- fixed variant form *gheim-ri-no- in Latin hibernus, pertaining to winter: HIBERNACULUM, HIBERNATE. 3. Suffixed zero-grade form *ghim-ar-ya, “female animal one year (winter) old,” in Greek khimaira, she-goat: CHIMERA. [Pok. 2. ghei- 425.] gheis-. Used of the emotion of fear or amazement (origi- nal part of speech uncertain). Suffixed o-grade form *ghois-do- in Germanic *gaistaz, a ghost, in: a. Old English gdst, ghost: GHOST; AGHAST; b. Old High Ger- man geist, ghost: POLTERGEIST; Cc. Germanic denomina- tive *gaistjan in Old English g&stan, to scare: GAST. [Pok. gheis- 427.] ghel-'. To call. 1. Germanic “gel-, *gal-, in: a. Old Eng- lish gellan, giellan, to sound, shout: YELL; b. Old English gielpan, to boast, exult: YELP; c. Old English galan, to sing: NIGHTINGALE. 2. Reduplicated form *ghi-ghl- in Greek kikhilé, thrush, later also the name for a kind of wrasse (a sea fish that has bright colors and jagged waving fins, reminiscent of the plumage of a bird):
1550:GABERDINE per-2, wel-3 GABFEST dhés- GABION keue-2 GABLE ghebh-el- GABRO gladh- GaD2 ghasto- GAEA gé
```


## [2026-09-05T20:55:42.687Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -o \"ghei-[0-9]*\\. To yawn[^]]*]\" AHD_watkins1985.txt | head\necho \"===\"\ngrep -n -o \".\\{200\\}YAWN.\\{200\\}\" AHD_watkins1985.txt | head\necho \"=== chasm/gasp ===\"\ngrep -n -o \".\\{120\\}CHASM.\\{120\\}\" AHD_watkins1985.txt | head"
}
```


### [2026-09-05T20:55:42.793Z] TOOL RESULT

```
===
=== chasm/gasp ===
504:Latin hidre, to gape, be open: HIATUS; DEHISCE. 2. Suffixed variant form *gha-smn in Greek khasma, yawning gulf, chasm: CHASM. 3. Suffixed variant form *gha-n-yo- in Greek khainein, to gape: ACHENE. 4. Labial extensions: a. Old Norse gap, chasm:
```


## [2026-09-05T20:55:44.759Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '504p' AHD_watkins1985.txt | grep -o \".\\{600\\}CHASM.\\{1500\\}\""
}
```


### [2026-09-05T20:55:44.829Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T20:55:47.008Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nL=open('AHD_watkins1985.txt',encoding='utf-8',errors='replace').read().split('\\n')[503]\ni=L.find('CHASM')\nprint(L[max(0,i-900):i+1400])\nEOF"
}
```


### [2026-09-05T20:55:48.534Z] TOOL RESULT

```
ghai-. To yawn, gape. Contracted from *ghagi-. 1. Vari- ant form *ghyd- (< *ghyaa-) in: a. nasalized form *ghi-n-d- in Germanic *gindn in Old English ginan, ginian, geonian, to yawn: YAWN; b. Latin hidre, to gape, be open: HIATUS; DEHISCE. 2. Suffixed variant form *gha-smn in Greek khasma, yawning gulf, chasm: CHASM. 3. Suffixed variant form *gha-n-yo- in Greek khainein, to gape: ACHENE. 4. Labial extensions: a. Old Norse gap, chasm: GaP; b. Old Norse gapa, to open the mouth: GAPE; C. Old Norse geispa, to yawn: GASP. 5. Germanic *gil- in Old Norse gil, ravine, chasm: GILL’. 6. Germanic *gir-, vulture (< “voracious or yawning bird”), in Old High German gir, vulture (> German Geier): LAMMER- GEIER. [Pok. 2. ghé- 419.]
```


## [2026-09-05T20:55:57.533Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint('nleaves',len(leaves))\nfor i in (222,223,224,225):\n    print('=== leaf',i)\n    print(leaves[i][:1500])\nEOF"
}
```


### [2026-09-05T20:55:59.576Z] TOOL RESULT

```
nleaves 858
=== leaf 222
er’; Gk. thermós, adj.; thérme, f. s. beside thérma, n.; Alb. zjarr, zjerm, m. ‘fire’; cf. Dac. (?) Germi-sara (a wa- tering-place); OLat. cf. formus, adj. (Fest.); Formiae (a town nr. Naples); Lig. Bormium, Aquae Bormiae (places in Switzerland); Go. cf. warmjan, v. beside *warms (^warm', and com. Gmc.); Li. (Zemaité?) germe (“virgin
381
forest’. Cf. šilas *pine-forest': šilti “be warm
guheros “hot; heat’. WP I, 687. Cf. guhermos. (O-gde in Iran.) Skt. háras, n. (anger; Av. (o-gde) gar-, v. ‘burn’; Arm. ğer, o-st. ‘hot; Gk. théros, n. "summer, harvest’; Olr. cf. fo-gerim, v. ‘heat’; OCS cf. Zeravü *^white-hot'; Srb. Zerava "em. bere": long-gde in OCS Zarü Cheat and com. Sl.)
guhesl- (guhesdhil-?) “a yellow juice, bitter sap, gall Per. zahr ‘poison’; Lat. fel, gs fellis ‘poison, bitterness, gall’; felleus, adj. of gall’; Go. *wizdils (uisdil- in a LLat. LW) ‘plant with yel- low sap”; E weld; LW in Fr. gaude, Sp. gualda
guhon- (R-gde variant of guhen-, q. v. Cf. Gk. phtháno ‘forestall’, a synthetic cpd.; Alb. për- zàj, T pér-zé ‘chase’; OCS Zinjo Zeti ‘mow’)
guhiguros (guhiguhro-) ‘burning, hot. Cf. guheguh-, var. of dheguh- Gk. thibrós “hot, roasted in embers'; Cz. cf. Zebra ‘fiery one’; Zehravy ‘fiery’; žhavý red. hot’; R cf. Zgu, Zec “burn, scorch’; (*-1- in) Sło- vene žíg ‘brand’; žigati, v. ‘brand, burn’
guhindhos, io? ‘scorching, burning; heat, drought, thirst. (Slav. ambig.) ' Gk. tinthós 'scorching'; OCS (ambig.) ZeZdi, žęžda “thirst'.
guhislà ‘sinew, gut, vein". WP I, 
=== leaf 223
r. gonim, goinim ‘wound, gore’; OCS gonjọ, -iti ‘chase’; Latv. ganu, it ‘put out to graze’
guhonos, à, is ‘blow, chase, slaughter’. Cf. guhen-, etc. WP I, 679 Skt. ghanáh; Av. vand; Oss. qün, gänä ‘wound’; Arm. ğan, i-st. ‘effort’; Gk. phónos, phoné ‘slaughter’; cf. synth. cpd. phthónos, m. ‘envy, reproof; Alb. záné, xânë ‘padlock’; Mir Ir. guin, goin, f. wound"; MIr. con-guin ‘violation; compunction’; Cz. hon, m. ‘drive, chase’; OCS iz-gonü ‘chasing’; Big. s-gani (*-0-) ‘gang, crowd’; Li. gánas ‘pasture; tend- ing; drover’; Latv. gans ‘drover’. Cf. the cpds.
383
of type *guou-guhon- in Vedic go-hán “killing of cattle’; Gk. boú-phonos *'ox-killing'; Latv. gov-gans ‘drover’
guhoreið ‘warm, heat'. Cf. guher-, guhermos, etc. Olr. goirim, id.; OCS gorjọ, čti Chur", and com. SL); Li. gariü, éti, v. ‘steam’. For the o-gde root, cf. OLat. formus, and perh. Gk. Phorüe ‘Titan’. See next
guhormos ‘hot, warm’. Cf. guhermos, guher-, guhor- & guhrnos. WP I, 687-8 Skt. gharmáhb, s.; Av. garomo, adj.; garomus, s.; Per. garm, adj.; OPer. garma-, id.; OLat. for- mus; Go. *warms, and com. Gmc.; OPr. gor- me, s. (*-?a-)
guhoros, is “heat, warmth; hot place, burn’. WP I, 688. Cf. guher-, etc. Lat. cf. (Isidor) forvus ‘hot’; OIr. guire, MIr. & Ir. gor, sg Br. gor m. ‘heat’; (pl. iu, m. ‘abscess’ to guhr-, q.v.); OCS gorü, s.; Cz. hof, m.f. ‘heartburn’ beside vy-hor 'burnt-out spot: OCS gorikyj ‘hot’; Li. gáras ‘heat, zeal, steam’; pra-garas ‘hell’; Latv. gars ‘spirit: steam’; OPr. goro (for *goàr
=== leaf 224
 -yti ‘scour’. Variant in Du. grint (gravel, fr. *guh- rend-). Of uncertain connexions are Alb. grí, gs grini ‘whetstone’; er, aor. grina, v. ‘whet’; OE grind ‘crash’, grinde ‘shingle’; Br. brenn *bran', fr. either *gurendh- or *bhrendh-
guhretos “narrow, close; closeness' Lat. fretus, üs, m. & fretum, n. “strait”; Li. grétas ‘close, adjoining"; gretà ‘alongside’; gré- Cum, gréciui ‘near’. (For Lat. fretus see Supt. dhret-: OCS drëtt ‘to confirm")
guhrét- (guhrést-, guhrot-, guhrt-) “warm, heat; burn, warmth'. Cf. guhre- Olr. cf. grís, Ir. gríos “burning; warmth' (fr. *euhrest-); mod. Ir. also: ‘embers’; ON gráó ‘warm wind’; cf. W graid (burning! adi: m. ‘heat of the sun’ beside gwres (^warmth' < *guhrotis beside *guhrest-); Arm. cf. éah, i-st. Ctorch, fr. *guhrtis); OCS gréti, inf. (and com. SI.) ‘to warm’. Cf. guhrt-
guhro-, r-gde of guhré-, guhret-, etc. q.v.
guhriio (?) ‘crush, pound’. (All the evidence is ambig.)
385
Gk. (?) cf. Hes. thriésai "to wanton’; thrió ‘festivity of Apollo, and his kind’; thrízo (2) ‘mow’; Lat. frio, friare ‘crush’, of ambiguous phonology, but cf. Gk. thriaí ‘pebbles — as used for divination’; Alb. (ambig.) grij, aor. griva & grijta, inf. pp. grimé *mince, chop; punish, destroy’; Li. cf. grystu, gristi ‘annoy, bore?
guhrndó (guhrmdo) ‘grunt, growl’ (?). (Am- biguous. Cf. guhremdh-) Lat. frendo, ére (2) *grunt' is ambig. but equa- tes w. MHG. G grunzen: E to grunt
guhrom-, see guhrem- and cf. ghrom-, ghrem-. See next
guhromdio- (guhrondio-) ‘bee,
=== leaf 225
hrn-ec, -ek, id.; Srb. grnac. id. Cf. ON orna v. ‘warm’. (For the semantics cf. Skt. kundam ‘firepit’ and ‘pot’, and that Aus- tralian aborigines still build earth-ovens. Cf. the structure of the Sardinian nuraghi, of co- nical shape, primitive blast-furnaces?)
guhrn- (2) (?) “group, crowd? OE worn, id.; Cz. sou-hrn “set, collection’; cf. hrnouti ‘amass’; Srb. grnuti, id.
guhrt-, cf. guher-, guhor-, etc. Skt. ghatah, adj. ‘zealous, fiery’; m. ‘pot’; Arm. gah, Let ‘firebrand, torch'. The zero-gde seems to be present in Gk. thár-gelos, s. “pot for firstfruits'; thar-gelía “June harvest cele- bration’
guhurs- ‘foulness’. Cf. ghuros, guhros Gk. cf. phüro ‘mix, defile’; OE worsm, worms ‘pus’. A variant formula of type *guhrs- may be present in Gk. pharikón “a poison-plant
387
?agh- (?aghis, os, iô(n), iə) ‘tip, spike’. WP I, 570. See next Arm. cag, Let ‘tip, peak’; OE ceacga ‘gorse’; Du. keg, kegge, f. ‘wedge’; Li. Zágas ‘stack’ beside Zaginai ‘stumps of young firs, palisade’
$agholos ($aghilo-, $aghlo-) (1) ‘spike, point’. Variant: gaghoros. Cf. &agh-. WP I, 570 Oss. zágàl ‘nail’; OHG kegil ‘peg’: MHG. Du. kegel ‘cone; skittle, icicle’. Variants in Oss. dzagur ‘chisel’: Li. Ziogras ‘stake’, fr. a type *saghuro-, *&aghro-; Icel. kógur, n. fringe"; Li. Zágaras ‘twig’; pl. ‘brushwood’; Zagre ‘plow- share’ beside Zagáre, id.
$agholos ($aghilos, $aghlios) (2) ‘rogue’. Same as (1)?
MHG kegel (2) ‘bastard’; Li. Zaglys ‘thief; Latv. zagls, id. beside zogu, zagt (fr. *g&angh-: *&agh- 'ste
```


## [2026-09-05T20:56:06.371Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"yawn\" IEC.txt | head -30"
}
```


### [2026-09-05T20:56:06.415Z] TOOL RESULT

```
4575:gham- "open mouth, chasm’ Hes. khémé ‘yawn, gape; Alb. gomën, pl. gomna 'water-hole, chasm’; OHG guomo, wm. ‘palate’; ON gómr, gs góms, id.; (cpds. *-mouth"); Li. cf. gomurys, gomerë ‘palate’; Latv. gamurs ‘windpipe’
5588:gänlos, à, om ‘open jaws, gape, yawn, depth; gaping, deep’. WP I, 570 Av. zafrəm, pl. zafarə, id. beside jafrō ‘gaping; deen": Arm. (?) cf. coc, o-st (bosom, gulf. Vocalism obscure); OE ceafl ‘jaws, jow? cf. E dial. to chavvel ‘to chew’; Du. (*-à-) keuvelen ‘chat’; Sw. kafle ‘gag? beside käft “jaw, jowl’; Li. (*-à-) žioplà “mouth, phiz'; Zioplas, adj. ‘gaping, silly’
5923:(8haiuo ‘yawn’, see ghiia- and extns.)
6041:ehiiaio (ghia-, £ha-, 2hi-) ‘gape, yawn’ (ono- matopoeic). WP I, 548 Per. fa-Zidan, cpd. id.; Gk. cf. kháos; Lat. hio, hiāre; OHG gen. beside MHG giegen ‘yawn; play the fool; OCS ziajọ, ziati beside z&ig, zéti; Cz. zen, záti; Li. Zióju, Zióti, id. beside žiojù, čti ‘snarl’
6044:Gk. khēlé “claw, notch, breakwater’; khelóo ‘split open’; MHG giel “open jaws’ beside Du. geul ‘gully, channel; Li. cf. Zioklë “open jaws, hob-hole, blowhole’ etc. Variant: ghiiom-, ghim- etc. Gk. khéme “yawn, gape'; MHG giem- in giem- olf ‘snarling wolf; G Giemen ‘chink’; Icel, gjamm ‘bark of dog’; Li. žiomuð, gs -eñs m. ‘jaws’. (Cf. also *&£hiien-, *&hin- in MHG ginen, gënen ‘yawn’; G gienen ‘burst open, gape’. See ghiiaio, etc. OE goma “open jaws’ is ambig. See gham-, as also for ON gómr ‘roof of mouth? < *gh-, or *gh- in view of Li. gomurjs, m. crater)
6047:ghiiatos, ios (8hiiot-, ghiát-, hit-) ‘yawning, gaping; gap, emptiness’.
6052:dial. to yowl: ON gaula ‘moo’; gaul, n. wd: Cz. zevel ‘gaper’; Li. Ziovulys ‘yawn’; radical in Latv. Zàvas, fpl. ‘yawning’
6053:£hiiaunos, ghiaun-, &haun-, cf. Gk. khaünos, adj. ‘hollow, porous; variant in OHG gien ‘yawn’; G gienen ‘gape, burst open’. See ghi- iamaá
6054:£hiiau- (hiau-), theme of following entries: ‘gape’, etc. Extn. of type 8hiià-, q. v. WP I, 548 OHG géwon, v.; MHG géwen, giwen, v.; Fris. gouwe, v.; Du. geeuwen, v.; beside geeuw, m.; R zév “open mouth'; OCz. zievaju, v. beside zével, m. *yawner'; ON gjá ‘chasm’; Li. Ziova ‘gaper’; Ziovuljs ‘yawn’; Latv. Zavas, fpl. ‘yawning’; Zàva ‘gaper’. Cf. Srb. zurim 'gawp'; Li. Ziaunóju ‘munch, open mouth wide?
6057:$hiiosKo (Shask-, &hisK-) ‘gape, yawn, crack open’. Cf. ŝhiiã- theme Gk. khásko; Lat. hiāscō, ére beside hisco, Gre: OHG géscon ‘hiccup’; MHG gischen (2), id.; OE geocsian, giscian, id.; EME to yex, id.; G cf. Giesch (2) “mouth, mug”, beside gicksen “catch the breath; sing falsetto; cackle’
6070:$him- ‘gape, yawn, open mouth’, etc. see $hiiàm-, etc. Oss. cf. zàmbín, v. ‘yawn’; LG gimen, v. ‘gasp’; Sw. gima “opening, mouth of oven'; G Gie- men, s. ‘chink’. Cz. zmol, zmola ‘ravine’ re- presents a type *&himolo-, A
6071:ehin- ‘gape’. See ghiià- and derivatives OE ginn ‘spacious’; ON gin ‘mouth, muzzle’; gina ‘gape’; OCS zinọ, -iti ‘yawn’; Slovene ziniti, id.; Li. cf. Zynýs, io, m., Zyne, f. “py- thon'
14513:reng- ‘show the teeth’ Oss. cf. be-rinžun, pp. -rixt, v. ‘yawn’; Lat. ringor, ringi, rinctus, v. ‘snarl, bare the teeth: OCS regnoti, inf. ‘gape, open out’; Slovene regati, inf. id.; rega, f. ‘cleft’; Srb. režim, režati, v. ‘snarl’; Cz. cf. řehnit, fehonit, inf. ‘guffaw’; (o-gde in) OCS rogati, inf. ‘mock’; rogü, m.
```


## [2026-09-05T20:56:13.184Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\npre='\\n'.join(lines[:6041])\nleaf=pre.count('\\f')\nprint('leaf',leaf)\nleaves=t.split('\\f')\nprint(leaves[leaf][:2500])\nEOF"
}
```


### [2026-09-05T20:56:15.139Z] TOOL RESULT

```
leaf 241
nt'; Sw. gása beside Norw. gjære, v. 1d.; gjær ‘barm’; Du. gier, Fris. jarre liquid manu- re
ghesmn-, see ghes- G cf. Germ ‘barm’; Icel. gisinn ‘leaky, thin, sleazy’?
&hesteros *yesterday's, previous’. Cf. &hdhes, etc. WP I, 664 Alb. cf. djethi ‘yesterday’; Go. gistra-, OE geostra; Lat. hesternus, adj.
$hestós, see &hes- Sw. cf. gisten, adj. ‘porous’
£hesuo-, -uo MHG gis ‘foam’; gérwe ‘yeast, dross’. See $hes-
gheubo, ið “snap, bite, cheat’. (For seman- tics cf. &neub-, gnib-, $nibh-) OE géopan, pf. géap ‘dupe’; LG cf. giepsen ‘snap at? beside giepern ‘desire’; Li. Ziaubiu, "ti (2) ‘snap at, snatch’. O-gde in OE geap: MHG góuf- ‘astute’. (Isophonic: MHG giefen ‘rave’; gief ‘fool, dupe’. A possible LW of type
417
*&houb-, Gmc. *gaup- in Fr. jobe ‘dupe’)
$heumn- ($houm-, $houono-) 'outpour, yield". Cf. 8heuo (1) & WP I, 563 Skt. hóman ‘oblation’; homih, m. “fluid, ghee’; hávanam ‘offering’; Arm. dzawn, Let. ‘gift, dedication’; dzawni, adj. ‘dedicated’; Gk. kheüma "outpour": khóanos ‘crucible, fur- nace’; Phryg. zeüma- ‘fountain’; Lat. cf. hū- in hü-mectare ‘moisten’; hü-meo, -mere “be moist'. (For the isophone Li. Ziaumuó 'crater' see &heuos). (Extn. in ON gjósa ‘pour, gush’. See Supt: gheud-)
2heuð (1) “pour, shed, empty, yield". WP I, 563, Cf. 8heumn- Skt. juhómi, pp. hutáh “pour on to a fire, li- bate’; Av. cf. *us-zavaiti “wells up’; zao-6Ora “holy water’; Tokh. B ku- ‘pour’; Arm. cf. dzev, o-st “form, shape’; Gk. khéo, Hom. kheuo ‘pour, shed’; cf. Phryg. zeuma- ("fountain'. Hes.); Alb. cf. zucé (‘dross’, fr. a type *&heu- tio). Extn. in Av. zaotar: Skt. hotr ‘priest’. See Supt: &heud-
$heuó (variant of guhuo, $houo, q.v.) (2) ‘call’, etc. Ved. háve; Av. zavai(mi) ‘curse’; zbayemi “call, praise’; Arm. n-zovem ‘curse’; OE giwian ‘ask, petition; OCS zovo, züvati (‘cal and com. SL); Li. Zaviü, éti ‘bewitch’; Zavai ‘witchcraft’; Zavüs ‘charming’; Latv. zavet, v. ‘bewitch’
&heuos, eio ‘hollow’. WP I, 563 Arm. dzor, o-st. ‘valley’; Gk. kheiá, kheié “hole, den": Lat. fovea, id. Li. cf. Ziau-muó ‘crater’
($hom, see g8hm-, &hem-)
(£hou-, £hou$hou-, see guhu-)
ehíghàmi, see ghà-mi, etc. and cf. gheighó. Arm. (ambig.) dzgem ('stretch; draw; throw; leave; let; drop’. See 8heigho); G dial. (IE Sei, *-1- or *-oi-) geigen ‘sway’; Li. Zygiu, -éti *go move'. O-gde in ON geiga 'swerve'. (For Go. ga-, faihu-geigan, see gheigh-)
8hiia-, radical of the following terms:
ghiiadmn- "open jaws, space, chasm’ Gk. khásma; MHG cf. gin *animal's mouth, jaws'; Li. Ziodmens, as Gk.
gh
```


## [2026-09-05T20:56:22.159Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor f in MON_part1.txt MON_part2.txt; do echo \"### $f\"; grep -n \"فاژ\" $f | head -10; done\necho \"### BQT\"\ngrep -n \"فاژ\" BQT_v1_pages.txt BQT_v2_pages.txt incoming/BQT/BQT_v3_pages.txt incoming/BQT/BQT_v4_pages.txt incoming/BQT/BQT_v5_pages.txt 2>/dev/null | head -20\necho \"### FRS\"\ngrep -n \"فاژ\" FRS_pages.txt FRS.txt | head -10"
}
```


### [2026-09-05T20:57:00.025Z] TOOL RESULT

```
### MON_part1.txt
87289:شوفاژ: 082 (ا.) ایجاد حرارت. طرز گرم 
### MON_part2.txt
4218:فاز: 7۶ |- فاژه] (.) خمبازه ۳ اش 
### BQT
BQT_v1_pages.txt:23259:وشاهدی بافته سل .. ۴ - معرب آن‌فاژ.  *‏ ویازاح 1
incoming/BQT/BQT_v4_pages.txt:11058:پرای تفاژل میکاشتند وکمان میکر‌دند که هر يك ازآنهاکه تیکوتر و پارورتر شد , محصولش‌در
incoming/BQT/BQT_v4_pages.txt:15779:۴ «فاژه (ه.م.) : ر4 : هاز , هاژویدن . 8 رك : هاژو. سروری و رشیدی
incoming/BQT/BQT_v3_pages.txt:6694:‎ath‏ و ازغایت فاژ کی ‎See‏ بجانب زمین کندلهذا
incoming/BQT/BQT_v3_pages.txt:16341:‏فاژه (۳) - بنتح زای‌فارسی؛ بممنی‌اول
incoming/BQT/BQT_v3_pages.txt:16342:فاژ است که خمیازه باشد ‎٩۱‏ - و بمعنی سایبان
incoming/BQT/BQT_v3_pages.txt:16364:‏(۱) چك : بکس را . (۷) چك : _ ابجد . (۳) ‎ote‏ , چك : فاژد» .
incoming/BQT/BQT_v3_pages.txt:16370:ح 4سفحلقبل. ۷ ‎Cea) Ghee‏ > پارباب . ‎joa A‏ د رشیدی » رك : فاژیدن :
incoming/BQT/BQT_v3_pages.txt:16372:‎٩‏ رك : فاژیدن .. ۶ - مضارع است بمعنی‌خمیاژه کشد. ۱ - ره ‎je:‏ .
incoming/BQT/BQT_v3_pages.txt:16387:فاژیدن ۱ - با زای ‎ed‏ بر وزن
incoming/BQT/BQT_v3_pages.txt:16428:‏۱ - از : فاژ (ه.م.) + پدن ( پوند مصدری ) :
incoming/BQT/BQT_v3_pages.txt:16432:‏که سیر خورده بفاژد بها رکه اشتر .
### FRS
FRS.txt:7546:اکرندانی؛ بندیش تا چکونه بود که‌سبزه* خوردهفاژدبهار که" اشتر | 
FRS.txt:15668:٩‏ - معلوم نشد این چه کلمه‌است و شاد« فاژ » بوده که انب بسهو آنرا باین‌جورت 
FRS.txt:21906:فاژ ۱۷۲۸ 
FRS_pages.txt:8183:‫اکرندانی؛ بندیش تا چکونه بود کخه‌وسبرزده*هفاژدبهار که"اشتر|‬
FRS_pages.txt:17438:  ‫‏‪ - ٩‬معلوم نشد این چه کلمه‌است و شاد« فاژ » بوده کهانببسهو آنرا باین‌جورت‬
FRS_pages.txt:22862:          ‫فاژ ‪۸۲۷۱‬‬                ‫غمزه ‪۸۸4‬‬                      ‫غرم ‪۳۳‬‬
```


## [2026-09-05T20:57:09.385Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '16320,16440p' incoming/BQT/BQT_v3_pages.txt"
}
```


### [2026-09-05T20:57:09.430Z] TOOL RESULT

```
و ظهیرالدین فاربابی شاعر مشهور ازین فارباب است .

‎oe‏ محمد قروینی. بیست مقاله چ
[pdf page 227]
Net ‏ظرد‎

بمعنی فاراب است ‎٩‏ وآن ولابتی با شهری‌باشد
از تر کستان - و زمینی را نی زکویند که با آب
رودخانه وآب‌کاریز مزروع شود ۲۵.

فار یاو © باواو » پروزن و معنی‌فارباب
است که ولایتی با شهری باشد از ترکستان ‎٩‏
‏- و زمینی که با آب رووخانه زراعت شود۷ .#

فا - بسکون زای فارسی ؛ بمعتی دهن
دره است که خمیازه باشد ۸ ؛ و بسضی کونند
دهان باز کردن در خواب است .

‎phe 1350‏ زای فارسی و ‎OS‏
‏دالابجد(۲). ماضی ‎VO‏ خمیازه کشبدن‌است بعنی

‏فاژه (۳) - بنتح زای‌فارسی؛ بممنی‌اول
فاژ است که خمیازه باشد ‎٩۱‏ - و بمعنی سایبان
حم بنظر آمده است .

‏مزروع شود برخلاف زمین دیمه که پاآب باران
زراعت میشود ۷ .

‏فارد - بکر رای قرشت (۱) بر وزن
بارد ۰ یکی از بازبپای نرد است و ‎OT‏ بفرید
شهرت دارد ۴ - و در عربی پمعنی تنها باشد -
وکا و کوهی را نیز کوبند ۳ . *#

‏قار سطاد ون - بکر اك بمنی
قرستاربون است و آن بلفت ‎iby,‏ غله‌ای باشد
بزر کتر ازماش که‌بعربی رعی‌الحمام خوانند؛و آ نرا
کبوتر بسیار دوست دارد -

‎FEM‏ پروزن ‎Sb‏ » بمعنی‌فرصت
‎ooh‏ باشد - و سرور قلب - و باد سرد تابتانوا
‎aS ps‏ - و در عربی خلاص و نجات بابنده را
بشد .
‎WY‏ - با بای حطی‌بروزن ماعتابه

‏(۱) چك : بکس را . (۷) چك : _ ابجد . (۳) ‎ote‏ , چك : فاژد» .

‏۱ - رك ‎bb:‏ فارباو پارباب ۰ پارباو » باراب . ۴ - رك : خانه گیر .
۴ - (مر) « فارد ( بکرسوم ) ‎WK,‏ - و درخت یکو وتنها — وآهو ماد جدا ماندء
از کله » « منتهی ‎LOOM‏ ۴ - (عی) « فارغ » پردازنده از کاری » « منتهی ‎OM‏
‏۵ رك : ‎lk‏ پارباو, باراب. فارباو, فاراب . = فاریاب ‎(pe)‏ ورگ :
ح 4سفحلقبل. ۷ ‎Cea) Ghee‏ > پارباب . ‎joa A‏ د رشیدی » رك : فاژیدن :
میکند چون ز یبدمافی فلژ در دهانش نهاده باید ژاژ . طیان مرغزی.*فرهشکه‌نظام».
‎٩‏ رك : فاژیدن .. ۶ - مضارع است بمعنی‌خمیاژه کشد. ۱ - ره ‎je:‏ .
# فارس - رك : ‎oh‏ . فاری تاحیتی است که از مشرق بکرمان . از جنوب بخلیج
فاری » از مغرب بخوزستان و ازشمال ببختیاری وبزد و اصفهان محدود است. مهمترین حوزه‌های
‎oT‏ عارتست از: ۱ شیراز وحومه »-آباده ۳- ‎Mis‏ 4-کوه‌کیلونه , ممسنی هولابات
‎CS >‏ ( شامل بلو کهای :کوه مره شگفت 6 خواجه . سیاخ .کوار » صیمکان ۰ قبر و کارزین
وجوبم) , ولابات خسه (شامل بل و کهای : بوانات . قنقری . سرچاهان .آباده طشتك دارابگرد.
قا ء خفر , محال هقتگانه ( سبعه ) » رودان احمدی . جپرم » کمین ۰ ارسنجان ۰ کربال .
مروستان ) » نیریز لارستان . < جفرافای سیاسی .کیهان ص ۲۱5 -۷8۳ ۴ اکنون فاری را
> استان هفتم * کویند . رل : راهنمای جفرافبایی ‎ol pl‏ . چاپ ستاد ‎st‏ . جلد ۷ ( استان
* فاریدن - بقتح دال < واریدن < ‎IF‏ واردن ؛ لقمه بدهان فروبردن :«آنآش‌اورا
تفارد ونگوارد ۰ فیه مافیه ممحح آقای‌فروزانفر ص ۲8 ورگ : ص ۳۹۲ ۰۱2
‎sles)‏ قاطع ۱۸۳)
[pdf page 228]
-6۳۵-

فاژیدن ۱ - با زای ‎ed‏ بر وزن
پاشیدن » بمعنی خمیاز کشیدن باشد .
فاسقون - ‎on Oe‏ بی قطه (۱)
وضم قاف بروزن واژ کون . بلفت رومی نام بيشه
و جنگلی‌است در روم ۴ ۰
فاش ۴ ۰ بر وزن پاش » بمعنی آشکارا
وظاهر باشد ۴ - و بمعنی پرا کندسهمآمده‌است.
فاشرا ه‌ © بفتح وسکون‌شین نقطه‌دار(۲)
و رای بی ‎abt‏ (۳) بالف کشیده . بسربانی نوعی
ازرستنی باشد که‌مانند ‎dite‏ بردرخت پیچدوخوشه
و میو ‎OT‏ زباده برده ‎ails‏ لمیشود وآن در اول
سبز ودرآخر ‎cal‏ سرخ کردد و ‎Oke aly‏
کوبند ‎ge‏ هزارکز و بشیرازی نخوشی‌خوانند
ببب آنکه ‎OT tye‏ در زستان ‎Chis‏ نمیشود
(۱) چك : - بی‌نقطه .
(4) چش : ‎Atle‏
‏(٩)چك:‏ بسکون ‎Ab‏

‎ele )0(‏ : - نقطدار .
)0( چش : شش بند است.
‎(v)‏ چك : - بی‌نقطه .

‏و سربی کرمةالبیضا ‎pill Play‏ و عنب‌الحیه )8(
هردوبا حای بی‌نقطه وییونانی انبالس لوق یکوند.
‎a‏ ۳۹
فاشرستین ‎Ge ٩‏ شین ورای‌قرشت
وسکون مین بی نقطه و فوقانی بتحتالی رسیده
وبنون زده ۰ بلفت سریانی و بسن ی ‎BU plc‏
بمعتی دافع شصت ‎che‏ باشد و آن کیاهیست که
شیرازبان ‎Le‏ داروگویند و بعربی کرمةالاسود
خوانند و آن ثش‌بندان ‎col‏ (۵) که مانندععقه
بردرخت پیچد .
‎a AC}‏ 7
سر صتی._. « بروزن ومعنی فاترسین
است که خردل وسیند سوختن باشد .
قاط ‎og = A‏ طای حطی ‎)٩(‏ بلقت
رومي . چدوار را کوبند که ماه پروین است.
فاعیه ‎٩‏ - بکس‌عین بی‌طه(ب) وت

‎. ‏ورا‎ : dle )۳

‏۱ - از : فاژ (ه.م.) + پدن ( پوند مصدری ) :

‏اکر نداتی بندیش تا چگونه بود

‏که سیر خورده بفاژد بها رکه اشتر .
لییبی « فرهنگ نظام ‎٩‏ .

‏۴ - در معجم‌البلدان و ‎pulls‏ و حدودالعالم نیامده (قی : ۱285608506 )

‏۴ - مخفف فاشی ( عر) اسم فاعل از « فشو > ( پفتح اول » نیز بضم اول و دوم و سوم
مشدد ) رفشی * بضم اول ودوم و سوم مشدد ) آشکارا و پراکنده کردیدن . رثك : منتهی‌الارب .
قس : صاف ‎ile‏ » درپارسی بیز ‎SAP‏ (هم.) (پاشیدن) بمعنی پرا کنده و اقتان آمده .
```


## [2026-09-05T20:57:29.151Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### CHEUNG\"; grep -n -i \"fāž\\|fāz̆\\|fazid\\|fāzīdan\\|fāžīdan\\|hāž\\|xamyaz\\|yawn\" CHEUNG.txt | head -20\necho \"### HRN\"; grep -n -i \"fâž\\|fāž\\|fâz\\|gähnen\\|Gähnen\" HRN.txt | head -20\necho \"### HUB\"; grep -n -i \"fāž\\|gähnen\" HUB.txt | head -10"
}
```


### [2026-09-05T20:57:29.228Z] TOOL RESULT

```
### CHEUNG
11453:*NEIR: Sh. (Baj.) yan-/yiyd, упа, Sariq. yon-/, yüyj, уйе, Yzgh. yawn-/yüg ‘to 
13269:*4-rux-S° ) = argay (m.) ‘belch, sour eructation’, argamdy (f.) ‘yawning’, (Wan.) irZa 
14815:*jäs ‘to yawn, open the mouth’ 
14821:*CHORESMIAN: (+ *ui-) ? m/wy’s- ‘to yawn’ = Samadi: 224 
14823:*NWIR: (+ *ui-) Bal. g(iy)asit/g(iy)as-, gihasit/gihas- (etc.) ‘to yawn’, ? Kurd. 
14824:(Kurm.) bäwisk, bahusk (f.), (Sor.) bawésk ‘yawn(ing)’. © The Kurd. forms are 
14827:*NEIR: (+ *ni-) Yi. niáské, M. niezye ‘yawn’ 
24598:dough, clay, dung)’ || (+ *us-) Wa. istind- ‘to yawn’ || (+ *ui-) Yi. wien-/wiet-, M. 
29595:*NWIR: Kurd. (Kurm.) heniZin/heniZ- ‘to sneeze, yawn; to snooze’, Siv. esnis, Sang. 
29921:*zamb! ‘to open the mouth, yawn’ 
29930:*NEIR: Oss. I. zembyn/zembyd ‘to yawn’, Wa. zeumb(w)y-/zombovd- ‘to yawn, 
29931:open the mouth’, Wa. zim ‘yawn’ || (+ *abi-) Sariq. veizom(b)-, verjom(b)- ‘to yawn, 
50298:yawn-/yüg, 166 
58348:to yawn 
### HRN
### HUB
```


## [2026-09-05T20:57:34.435Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### ARY fa\"; grep -n \"فاژ\" incoming/ARY/ARY_pages.txt | head\necho \"### ARY latin\"; grep -n -i \"FAZH\\|FAJ\\|YAWN\" incoming/ARY/ARY_latin_index_pages.txt | head\necho \"### cheung zamb\"; sed -n '29921,29945p' CHEUNG.txt\necho \"### cheung jas\"; sed -n '14815,14835p' CHEUNG.txt"
}
```


### [2026-09-05T20:57:34.544Z] TOOL RESULT

```
### ARY fa
### ARY latin
10899:fajlaayry SCHAF JST ~
### cheung zamb
*zamb! ‘to open the mouth, yawn’ 

*MIDDLE PERSIAN: (+ *apa-, *abi-) MMP "bhwm- ‘to disclose. reveal’ = DMMPP: 
lla 

Pres.: IMPV. 2sg. MMP ’bhwm; Pass.: pres. IND. 3sg. MMP "bhwmyhyd 

*PARTHIAN: (+ *apa-, *abi-) 'bhwmb ‘disclosure’ (< MP) = DMMPP: lla 

*NEIR: Oss. I. zembyn/zembyd ‘to yawn’, Wa. zeumb(w)y-/zombovd- ‘to yawn, 
open the mouth’, Wa. zim ‘yawn’ || (+ *abi-) Sariq. veizom(b)-, verjom(b)- ‘to yawn, 
gape’ 

*SANSKRIT: jambh ‘to open the jaws wide, snap’ (RV+) = EWAia I: 572 f. 

9 The nominal derivative *zamba- ‘tooth’ (= Skt. jambha-) is also attested in Ir., 
notably Khot. ysima- ‘tooth’, Pash. zama (f.) ‘molar tooth’ 

*PIE ? *éemb"- ‘to show one’s teeth’, *gomb'o- ‘tooth, (set of) teeth’ > LIV: 162 | 
Pok.: 369 

*IE COGNATES: Arm. camem ‘I chew’, (?) OCS pro-zebnoti, Lith. Zémbéti ‘to sprout’ 
(with unexpl. acute accent), Gr. үбрфос̧ ‘nail, peg’, Lat. gemma (Ё) ‘bud, precious 
stone’, OCS zobs, Russ. zub (etc.), Latv. zuobs, Toch. A kam, B keme ‘tooth’, OHG 

### cheung jas
*jäs ‘to yawn, open the mouth’ 

*KHOTANESE: (+ *ui-) biyass- ‘to open’ = SGS: 97 

*SOGDIAN: (+ *ш-) Sogd. wy s/š ‘to open (the mouth)’ (L37.5) 

*CHORESMIAN: (+ *ui-) ? m/wy’s- ‘to yawn’ = Samadi: 224 

*NWIR: (+ *ui-) Bal. g(iy)asit/g(iy)as-, gihasit/gihas- (etc.) ‘to yawn’, ? Kurd. 
(Kurm.) bäwisk, bahusk (f.), (Sor.) bawésk ‘yawn(ing)’. © The Kurd. forms are 
hardly from the root *yamH ‘to vomit’, as stated by Cabolov, l.c. 

*NEIR: (+ *ni-) Yi. niáské, M. niezye ‘yawn’ 

© A reconstruction *kas-ja- (*xà- ‘to open’) is cautiously cited for the Khot. forms 
by Emmerick (SGS: 97). The comparison with Sogd. wy’s and Chor. m/wy’s- rather 
suggests *ш-1аза-1а- (Sims-Williams 1989: 286), to which the Y1./M. and Bal. forms 
may be added. The root "jas is exclusively Iranian. 

*PIE— > LIV: – | Pok.:
```


## [2026-09-05T20:57:43.504Z] TOOL CALL #26: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-05T20:57:43.510Z] TOOL RESULT

```


```


## [2026-09-05T20:57:46.247Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### TAD kufiyya\"; grep -n \"كوفية\\|كوفيه\\|قوفية\\|كوفيّة\" TAD_pages.txt TAD.txt | head\necho \"### TAD qifal\"; grep -n \"قيفال\\|القيفال\" TAD_pages.txt TAD.txt | head\necho \"### MON qifal\"; grep -n \"قیفال\" MON_part1.txt MON_part2.txt | head\necho \"### MON kufiyye\"; grep -n \"کوفیه\\|کوفیّه\" MON_part1.txt MON_part2.txt | head"
}
```


### [2026-09-05T20:57:46.354Z] TOOL RESULT

```
### TAD kufiyya
### TAD qifal
### MON qifal
MON_part1.txt:20588:جلد قرار دارد و حجیم‌تر از سياهرگک قیفال 
MON_part2.txt:85716:چین آرنج به دو شاخهةٌ ورید قیفال و باسلیق 
### MON kufiyye
```


## [2026-09-05T20:57:50.948Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('TAD_pages.txt',encoding='utf-8',errors='replace').read()\nlv=t.split('\\f')\nprint('n',len(lv))\nfor i in (68,69,70,71):\n    print('==== leaf',i)\n    print(lv[i][:1800])\nEOF"
}
```


### [2026-09-05T20:57:56.151Z] TOOL RESULT

```
n 87
==== leaf 68
                               ‫به اسه‬   ‫سكم‬




‫نونانى عترمهط وهي حشيشة تقتل برائحنها البراغيث والختافس‬              ‫‪5‬‬
                                                         ‫اشةغيث‬
                                                              ‫رشي‬
                                                                ‫اقالل لبهاح‬
                                                                          ‫وي‬
‫«نوشتا » الارامية لا من ‪8‬زهقاكاتاه إليونانية ومعناها‬
                                                   ‫كندسة ‏ من ك‬
                                                                  ‫اهمع والجاعة‬
 ‫كن م«نكاه ‪ 4‬أي تبن ومن « ربا » أجياذب‬                       ‫ار‬       ‫ال‬
‫فنا ‪ 5‬اص الاجسام التي اذا حكنت جذبت الاجسام الحفيغة‬
                                                  ‫وطزلمقان‬
                                              ‫‪...‬‬      ‫صتاب‬
                                                          ‫عحرك‬
                                                             ‫ار و‬
                                                                ‫للنو‬
                                                                   ‫اثت ا‬
                                                                       ‫وبع‬
‫‪6‬عيرانية‬
       ‫كورة ‪ -‬فالييونانية ‪#‬دوطه معناها بلاد وهي مأخوذة منق‪2‬ريه ال‬
     ‫بممنىبلادثمنقلتالىالسريانية ‏ كورا و‪6‬الى العربية كورةبممنىقرية‬
 ‫فو‬‫كروك هيوق ‪١‬ك‏رس" الازاية والسرائية وميا الكامن ‪:‬ومتان‬
                                           ‫الكأس والقدح والمشربة‬
‫كوقة و كقة حتإشاق متو تجا داغطا الرأس وعز هعم افلىبونائتة‬
                                                                     ‫معيأه راس‬


‫كولر نل ‪ -‬ايطالي العهناهاهه معناه قائد فيل "وهو رتبة ولقب فيقيادة‬
                      ‫|‬                           
==== leaf 69
                               ‫اخسب سد‬
                            ‫الكشك مرادفه المبضوم أي مطبوخ المعدة والخثارة‬
 ‫بوناني تسطنةمعم‪ -‬أواتك معناه الف غرام وهو بساوي ؟الم‬        ‫كيلوغرام‬    ‫[ْ‬


          ‫‪.٠‬‏‬   ‫‪73‬‬                    ‫ة‬   ‫‪8‬‬           ‫‏‪٠.‬‬
 ‫يمس معئاه سيال وعصارة وف العلب هو‬              ‫وين ‪ -‬وونابي ‪5‬‬
‫استحالة الطعام فى المدة بعد الحضم الجوعر اشر هو مادة عتنة” الى الامقراد‬
          ‫تأخذ لونها غالبامنلونالغذاء الذي تتحلبمنهمرادفه عصارة الحضم‬
 ‫كيميا ‏ في اليونانية ‪#‬نسيرا معنا اختلاط وامئزاج وهو الاكير عند‬
                               ‫القدماء كانوا حولون به المعادن الى ذهب وفضبة‬
‫م كيورة فثر هامر الطعم يطرد‬        ‫كيناوكينهوقينااوري‬

                                      ‫فى امريكا‬
                                              ‫الحمّئ ومنشأها بلاد ابرط‬


                          ‫عل النارسة كوه الاراية‬
                                               ‫ل ان س اممز‬

                                     ‫ل‬
      ‫لازورد ‪ -‬فارسي « لازورد ولاجورد ‪ 6‬وهو حجر ‪ 3 1‬أزرق اللون‬
‫اللات ‪ -‬صم هو مؤنث إل األياله افلىاشورية فيكون معنىاللات الالة‬
‫‪,‬لأمع‪ 1‬معناه فرقة‬    ‫وناني لمعم وى الللانيتي‪9‬‬    ‫ا لحنة ولدة ولاجدون ‪0‬‬

                                                             ‫عسكر وجيش‬
                     ‫لعل حجركم أجمر س‪ -‬فارسبي ‪ 2‬لال » معنا أحمر‬
‫ىليونانية معناه حمْرة‬
                    ‫ل م ‪ -‬تركي « (لن »م معناه قناةوعهرى و ‪807‬هلاه ف ا‬
                ‫والمرادبه حشوة‪ 0‬ندس فى ثقب الص<ور فتنسفبا مرادفه نسفة‬

‫لعن و[لكوت فقالارشية ‪ 2‬لكن ‪ 6‬وف اليونانية ‪ 888101‬وى الارامية‬

==== leaf 70
                                 ‫ف أفنا© ممناه ست من محاس يفسل فيه‬
‫ا وقد يكال‬        ‫الث ‪ -‬فارسي‪ 0‬نك © وهوصبغأجمريصبغبهويطلى‬
                                      ‫الابطالية و‪ 21‬والى الافر نسية ‪6921‬‬
              ‫لما نونالي ‪ 580021‬معنأه لامعوالمراد به السراج والمصباح‬
‫أوجادت اللقنازيية ليهولزها ‪#‬جنقا عن اتناك يلاهالحتد كرت انيه‬
‫هندي وهو نبات يعرش له سنوف فها حبوب لونما أبيض وأحمر ويقال له‬
                   ‫‪1‬‬                                           ‫الدرجر والثامر‬
‫تركواو قدا شعوق التو ‪:‬ولوذا فىالنازسية لاون عن‬                        ‫‪0‬‬
                             ‫القريشة عندهم أما الِبّأ فهو أول الابن فى النتاج‬
‫اقدفه تزلومزل‬
            ‫رند‬
              ‫داهن ايطالي ‪202‬نه‪ !0‬معناه للانجار وبراد يمهف‬
                                                         ‫ف‬

‫مشتقمن ولا! كك وهو الاصل فىكي اللمائعات‬       ‫ار ولمثر ل وناني ‪11‬‬

  ‫ليتورجية ‪ -‬بوناتى هاعتنامانها معناه الحرفي خدمة عمومية والعرفي قداس‬
‫مون ‪ -‬فارمي «ليسو» وأصل هذه الشجرة من الهند فيكون اسمبا هندي‬
‫أموناصة ‏ ايطالي ‪8‬ا‪ !88001‬معناه به ليون وهو عيارة عن ماء يارد يُعصر‬
                       ‫فيه يمون ويذر عليه ار فشر مرادفه شربة مون‬


        ‫ظ‬                           ‫‪0‬‬
‫مادلا ‪| 53‬يطالي ‪ 411830211‬معئاه قرصة معدن صغيرة ‪ 60‬مرادفه الوط‬

                                                                 ‫يعاق بالعئق‬
  ‫ماخور ‪ -‬فارسي منحوت معناه شرب الخر واأراد به بدت الربية والفسق‬
 ‫أرابي «ماري» معئأة سيدي ‪.‬‬   ‫مار عبت أراني «مارا» معناه السيد وماري ‪-‬‬

==== leaf 71
                                   ‫بين‬
                                     ‫عدؤ‬
                                       ‫مع‬

                    ‫ومارعندنا وعندم بر داد به قدرس أمام أسمالقديس خاصة‬
        ‫مالاريا ‪ -‬ايطالي ‪ 21312‬معناه هواء ردي مرادفه الحمى الخبيثة‬
                  ‫« ماله » وعربيه الميسيعة والمملط‬    ‫‪-‬ي‬
                                                       ‫رقس‬
                                                         ‫امال‬
                                                            ‫فلج و‬
                                                                ‫ما‬
 ‫‪-‬ن الاراي ‪2,‬ل ‪ 6‬أي نش ونتف وهو كووة ورا امتوك‬
                                             ‫مالوش م‬
                                                 ‫الننات وف اللاتينية ‪5‬ناداءناءط‬

            ‫بوناني ‪ 8001621‬معناه قباس وهو الاصل فى قياس المساحة‬        ‫مر‬

  ‫مجوس ‪ -‬ف الارامية « مجوشا »‪ 6‬وف اليونانية ‪ 60825‬وف اللائينية كندهةم‬
 ‫ذفالمبرانية‪,٠‬مج‏ ‪ 4‬ورب مج رئيس المهوس ارميا ليق وصّجٍأوماج لفل‬
 ‫أشوري معتاة ع ناظيم وذكرهرودط ان الجوس زوج ‪2‬م كانوا السبط السادش من‬
 ‫حكاء ‪ .‬وقال أحد الملماء ان انظ مجوس منذ القرن‬           ‫أسباط مادي ‪0‬‬
                                      ‫الثاألث صار يدل على ااسحرة وعبدة الدار‬
                 ‫مل‪ -‬بوناني دوااءمدد مخلس وعرببه المتلة والزبرة‬
 ‫ا‪-‬يطالى ‪ 263‬واهليمسحاة أيجر تيا آنأ التيتشبه الرفش فيقال‬
                                                                    ‫ها‪0‬‬
  ‫مرجان ‪(١) -‬‏ صغار الاؤلؤ(؟) الخرز الاحمر (م) عزوق حمر تطلع ناملبحر‬
  ‫(طر حيط ) فى اليونائية‬
                       ‫كاصابع الكف وهو المشهور (‪ )4‬بقل ربيعي ق‬
 ‫اهعمو مقه ‪,‬قغالتدوتهد وق اللائينية هاتتوععويم معناه نولو ودر وهو مادة‬
 ‫كلسة تتكون فى مغابن الحيوان اهلايالذي يميش فى جوف الصدفه البحرية‬
 ‫والمهرية وهو ‪:‬وافق الامع
```


## [2026-09-05T20:58:12.369Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### LKT cuffia\"; grep -n -i \"cuffia\\|kūfīja\\|kufija\\|Kufa\\|kūfa\" LKT.txt | head -20\necho \"### KLN coif\"; grep -n \"^coif\" KLN_1966.txt | head\necho \"### KLN keffiyeh\"; grep -n -i \"keffiyeh\\|kufiyah\\|kaffiyeh\" KLN_1966.txt | head\necho \"### SKT gable\"; grep -n -i \"^gable\\|gable,\" SKT.txt | head\necho \"### KLN gable\"; grep -n \"^gable\" KLN_1966.txt | head"
}
```


### [2026-09-05T20:58:12.493Z] TOOL RESULT

```
### LKT cuffia
4854:2171.  Tk.  yskiiflja: 'Nachtmütze'  [Kelekian  KämCis  90;  aus it.  scuffia,  cuffia] ;  hieraus  russ.  skiif'ja, bulg.  skufa,  serb.  skutvija,  skowija, poln,  skofija,  skofija,  kofija  'Kappe'; rum.  scufie  'Nachthaube'.  [Gorjajew  327. Mikl  SlEtWb  304  b.
### KLN coif
8158:coif,  n.,  cap,  headdress.  —  ME.  coif,  coife,  fr. OF.  coife,  coiffe  (F.  coiffe),  fr.  VL.  cofia,  cofea, cuphia,  ‘a  cap’  (whence  also  It.  cuffia,  scuffia. Sp.  cofia,  escofia,  of  s.m.  ),  fr.  OHG.  kupphia, ‘cap,  coif’.
8160:coiffeur,  n.,  a  hairdresser.  —  F.,  fr.  coiffer,  ‘to dress  the  hair  of’,  fr.  coiffe.  See  prec.  word, coiffure,  n.,  headdress.  —  F.,  fr.  coiffer.  See  prec. word  and  -ure.
### KLN keffiyeh
### SKT gable
7033:irrefragable,  not  to  be  refuted. L.)    F.  irre/tagable  — L.  irte/n§^ 10  be  withsioovl.  — L.  ir-  (>  im,  o< /rdptri.  to  oppose,  thwart ;  from  rr-, an<r(ptobably)  L.  /tm:-,  base  ©f  / to    break-      (For   thc^lo-  '    ^
7299:M  H.  G  -  C)  M  E.  ga^ft.  -  O.  F. gnbU  ;  Low  L.  gatulmu.  —  M.  H.  G.  gaUU, G.  ^vaV/,  n  fork ;  giM  (G.  gubel),  a  gable. +  Icel.  fa/7,  Dan  gi^vl,  Swed.  gafv*i,  a gable,  gaffe!,  a  fork,  Goth,  ^'^/o,  a  gable, Du.  .^n^r/.  Uut  it  siccms  to  be  of  Celtic origin  ;  cf.  Irish ^iiMii/.  a  fork,  gable.  Gael. gohhiit,  ^  gafi,  a  fork;  see  Gaff.
12194:navigable,  that  can  be  mveised ships.  (K.—  L.)  F.  narif^bU.  mt  L.  •« ^fVu.  — L.  nauigare,  to  navigate.—  L.  ivo crude  fonn  of  nauis,  a  ahip;  •^parr, o^wir,  to  drivt
### KLN gable
15635:gable,  n.,  the  triangular  upper  part  of  a  wall  at the  end  of  a  ridged  roof.  —  ME.,  fr.  OF.  gable, fr.  ON.  gafl,  which  is  rel.  to  MDu.  ghevel,  Du. gevel,  OHG.  gibil,  MHG.  gibel,  G.  Giebel, Goth,  gibla,  ‘gable’,  OHG.  gibilla,  OS.  gibillia, ‘skull’,  OE.  gafol,  OS.  gafala,  Du.  gaffel,  OHG. gabala,  MHG.  gabele,  gabel,  ‘pitchfork’,  G. Gabel,  ‘fork’,  for  I.-E.  *ghebh*l,  whence  also OIr.  gabul ,  ‘forked  twig,  fork’,  W.  gafl,  ‘fork’, Toch.  A  spat-,  ‘head’,  Gk.  xeyaXrj,  ‘head’.  See cephalic  and  cp.  gaffle.
```


## [2026-09-05T20:58:19.185Z] TOOL CALL #30: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%81%D8%A7%DA%98%D9%87",
 "prompt": "Is there a Persian entry فاژه? What is its meaning and etymology (any Proto-Iranian / PIE reconstruction, Hasandust citation)? Also report any mention of فاژیدن."
}
```


## [2026-09-05T20:58:21.151Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%83%D9%88%D9%81%D9%8A%D8%A9",
 "prompt": "Give the Arabic entry كوفية (kūfiyya): meaning and full etymology. Does it derive from the city of Kufa, or from Italian cuffia / Greek kephalē?"
}
```


### [2026-09-05T20:58:22.932Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-05T20:58:26.996Z] TOOL RESULT

```
# Arabic Entry: كوفية (kūfiyya)

**Meaning:** A keffiyeh (a traditional headwear garment)

**Etymology:** According to the Wiktionary source, the term derives from the city of Kufa. The entry states it is "Literally meaning from the city of _الْكُوفَة_ (al-kūfa, 'Kufa') or in the Kufan style."

The provided source does not mention alternative etymologies from Italian *cuffia* or Greek *kephalē*. It presents only the geographic origin from Kufa as the etymology for this Arabic word.
```


## [2026-09-05T20:58:30.314Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%81%D8%A7%DA%98%DB%8C%D8%AF%D9%86",
 "prompt": "Is there a Persian entry فاژیدن? Meaning and etymology?"
}
```


## [2026-09-05T20:58:31.498Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/cuffia",
 "prompt": "Give the Italian entry cuffia: meaning and etymology (Late Latin cofia? Frankish/Germanic origin? any Greek kephalē link?)."
}
```


### [2026-09-05T20:58:32.176Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-05T20:58:36.199Z] TOOL RESULT

```
# Italian Entry: *cuffia*

**Meanings:**
1. Bonnet or cap (e.g., *cuffia da bagno* = bathing cap)
2. Headphones (plural form)

**Etymology:**
According to the Wiktionary source, *cuffia* derives from "Late Latin _cofia_ ('bonnet'), probably of Germanic origin, from Proto-West Germanic _*kuffju_."

The word traces back through Germanic languages rather than Greek. There is no mention of a Greek *kephalē* connection in this entry.
```


## [2026-09-05T20:58:42.730Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%BA%CE%B5%CF%86%CE%B1%CE%BB%CE%AE",
 "prompt": "Ancient Greek κεφαλή: meaning and etymology. What PIE root is given (*ǵʰebʰ-ol-? *gʰebʰ-el-?) and what cognates (Gothic gibla, Old Norse gafl, Tocharian A śpāl)? Any note about dissimilation from *kʰephalē?"
}
```


## [2026-09-05T20:58:43.771Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/gasp",
 "prompt": "Etymology of gasp; also mention what etymonline says about gape and gap if present on the page."
}
```


### [2026-09-05T20:58:50.178Z] TOOL RESULT

```
# Ancient Greek κεφαλή: Etymology and Roots

Based on the Wiktionary article provided:

## PIE Root
The documented root is **\*gʰébʰōl** ("head"), derived from Proto-Indo-European. The article states it comes "from [Proto-Indo-European](https://en.wikipedia.org/wiki/Proto-Indo-European_language) _[\*gʰebʰ-l̥](/wiki/Reconstruction:Proto-Indo-European/g%CA%B0%C3%A9b%CA%B0%C5%8Dl "Reconstruction:Proto-Indo-European/gʰébʰōl")_ ("head")."

## Etymology Chain
The word derives from Proto-Hellenic **\*kʰepʰəlā́**, which combined the root with a nominal suffix **\*-éh₂**.

## Important Notes
The article does **not** provide information about:
- The specific cognates you mention (Gothic *gibla*, Old Norse *gafl*, Tocharian A *śpāl*)
- Any discussion of dissimilation patterns
- Alternative PIE reconstructions (*ǵʰebʰ-ol* vs *gʰebʰ-el*)

The only cognate mentioned is a comparison to another Greek word: **κεβλή** (keblḗ). The article also notes Sanskrit **कपाल** (kapā́la) is a **false cognate**, not a genuine related term.
```


### [2026-09-05T20:58:51.201Z] TOOL RESULT

```
# Etymology of Gasp

**Verb (late 14c.):** The word "gaspen" originally meant to "open the mouth wide; exhale," with uncertain origins. It likely derives from Old Norse *geispa* ("to yawn") or Danish *gispe* ("gasp"), which connect to Old Norse *gapa* ("open the mouth wide").

**Noun (1570s):** Derived from the verb form, with the earliest recorded usage appearing in the phrase "last gasp," referring to a final breath before death.

## Related Terms from the Page

**Gap (n.):** Dating to the early 14c., this word described "an opening in a wall or hedge; a break, a breach." It comes from Old Norse *gap* meaning "chasm, empty space," and connects to the Proto-Indo-European root *\*ghieh-* ("to yawn, gape, be wide open").

**Gape:** While not extensively detailed separately, the page indicates that Old Norse *gapa* ("to gape, open the mouth wide") is the foundational concept linking gap and gasp etymologically, tracing back to the same Proto-Indo-European root governing words related to opening and yawning.
```


## [2026-09-05T20:58:56.088Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/yawn",
 "prompt": "Etymology of yawn: Old English forms (ginian, geonian, gionian), Proto-Germanic, PIE root."
}
```


## [2026-09-05T20:58:56.659Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/chasm",
 "prompt": "Etymology of chasm: Greek khasma, Latin chasma, date of entry into English, PIE root."
}
```


### [2026-09-05T20:59:01.883Z] TOOL RESULT

```
# Etymology of Yawn

The word "yawn" traces back to around 1300, derived from Old English *ginian* and *gionian*. These terms descended from Proto-Germanic *\*gin-*, which scholars reconstruct from the Proto-Indo-European root *\*ghieh-*, meaning "to yawn, gape, be wide open."

Originally, the term simply meant to "open the mouth wide." By the mid-15th century, it specifically referred to "opening the mouth involuntarily through drowsiness or boredom." The modern spelling emerged during the 16th century.

Related words across Germanic languages share this origin, including Old Norse *gina*, Dutch *geeuwen*, and German *gähnen*. The same PIE root appears in etymologically distant words like "chaos," "chasm," and "gap."

The noun form appeared later, around 1690, and the colloquial sense meaning "something boring" is attested from 1889.
```


### [2026-09-05T20:59:04.564Z] TOOL RESULT

```
# Etymology of Chasm

**Origin:** The word "chasm" entered English in the 1590s, derived from Latin *chasma*, which came from Greek *khasma* meaning "yawning hollow, gulf."

**Root Connection:** The Greek term relates to *khaskein*, which means "to yawn," connecting chasm etymologically to the word "chaos."

**Early Usage:** In 17th-century English, the term was frequently spelled *chasma*. Its figurative application—describing "a great interruption or wide breach of any kind"—emerged in the 1640s.

**Historical Note:** During the American Civil War era, "the bloody chasm" became established rhetorical language (documented by 1868).

**Related Terms:** Related derivatives include *chasmy* (1786), *chasmal* (1842), and *chasmic* (1885).

**Proto-Indo-European Root:** Chasm traces back to the PIE root *\*ghieh-*, meaning "to yawn, gape, be wide open," which also produced words like gap, gasp, and hiatus.
```


## [2026-09-05T20:59:12.767Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/gable",
 "prompt": "Etymology of gable: Old French gable, Old Norse gafl, Proto-Germanic, PIE root and Greek kephale connection."
}
```


## [2026-09-05T20:59:13.674Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/cephalic",
 "prompt": "Etymology of cephalic: French céphalique, Latin cephalicus, Greek kephalikos/kephale. Any mention of the cephalic vein and Arabic al-qifal?"
}
```


### [2026-09-05T20:59:19.444Z] TOOL RESULT

```
# Etymology of Gable

The word "gable" has an interesting architectural and linguistic history. It entered English in the mid-14th century from Old French *gable*, meaning "facade, front, gable," which derived from Old Norse *gafl* "gable, gable-end."

## Etymology Chain

The term traces back through Proto-Germanic *gablaz* ("top of a pitched roof") to the Proto-Indo-European root *ghebh-el-*, meaning "head." Interestingly, this root also yielded words for "fork" across various Germanic languages—reflecting a possible original meaning of "top" or "vertex."

## Historical Interpretation

Scholars have noted that "a gable being originally formed by two pieces of timber crossed at the top supporting the end of the roof-tree," which may explain how a term for "top" or "head" came to describe this architectural feature. The word is related to the combining form *cephalo-* (from Greek *kephalē*, "head"), sharing the same ancient root.

The definition solidified to mean "end of a ridged roof cut off in a vertical plane, together with the wall from the level of the eaves to the apex."
```


### [2026-09-05T20:59:19.854Z] TOOL RESULT

```
# Etymology of Cephalic

Based on the provided content, the word "cephalic" traces back through Latin and Greek origins:

**Etymology Chain:**
The term comes from "Latin _cephalicus_, from Greek _kephalikos_ 'pertaining to the head,' from _kephalē_ 'head.'"

The ultimate root is Proto-Indo-European *ghebh-el-, which also produced related words in other ancient languages like Tocharian, Old High German, Gothic, and Old Norse.

**Regarding Your Questions:**

The page does not mention French "céphalique," an Arabic "al-qifal," or the cephalic vein specifically. The etymological information provided focuses exclusively on the Greco-Latin pathway of the word "cephalic" itself, with documentation dating to the early 15th century in English usage.

If you're researching connections between the anatomical term (cephalic vein) and Arabic linguistic roots, that information would require additional sources beyond what this etymology dictionary entry contains.
```


## [2026-09-05T20:59:26.433Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '20580,20595p' MON_part1.txt\necho \"-----\"\nsed -n '85710,85722p' MON_part2.txt\necho \"### search kufiyya variants in MON\"\ngrep -n \"كوفية\\|کوفیة\\|كوفيه\" MON_part1.txt MON_part2.txt | head"
}
```


### [2026-09-05T20:59:26.521Z] TOOL RESULT

```
نخ می کشند؟ باسدق» باررسق» فراته. 


۳۳۴ فررهنگ فار سی معیر باسلیق 


ب‌اسلیق: ,۰2۰1 [- ب اسیلیق] (ا.) (بز.) 
سیاهرگی که به محادات محور بازو در ز بر 
جلد قرار دارد و حجیم‌تر از سياهرگک قیفال 
است و به دو سیاهرگ زند اسفل و میانی 
تقسیم می‌شود. این سیاهرگ مسیرش در زیر 
توشت در سل فوقانی بازو با چشم کال 
مشهو د است؛ شاه رک دست. 
بباسم. 2 [ع.] (افا.) تبسم کننده 
نت6 
ناسمه: (۵-)02973 [تر. باصمه] (۱.) چاپ. 
-----
می‌ریزد. ورید غیفال: (پز.) نام ورید سطحی 
خارجی بازو که از انشعابات ورید میانی 
دست محسوب است [اين ورید ممکن است 
از یکی بیشتر باشد.] ورید میانی بازو: (پز.) 
ورید میانی دست. ورید میانی دست: (پز.) 
ورید سطحی ناحیهٌ قدامی ساعد که در بایین 
چین آرنج به دو شاخهةٌ ورید قیفال و باسلیق 
تقسیم می‌شود و در همین ناحیه است که ۱6 
وریدی درست می‌شود؛ ورید اکحل» ورید 
میانی بازو» ورید هفت‌اندام» رگ هفت 
اندام» رک میانی دست. ورید وداج: (بز.) 
نام هر یک از وریدهای بزرگ گردن. ورید 
وداج خارجی: (يز.) نام ورید وداجی که در 
### search kufiyya variants in MON
```


## [2026-09-05T20:59:36.031Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%82%DB%8C%D9%81%D8%A7%D9%84/",
 "prompt": "What do the Persian dictionaries (especially فرهنگ معین and دهخدا) say s.v. قیفال? Give the definition and any origin tag (e.g. [ع.] or [يو.] Greek)."
}
```


## [2026-09-05T20:59:37.434Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%DA%A9%D9%88%D9%81%DB%8C%D9%87/",
 "prompt": "What do Persian dictionaries (فرهنگ معین، دهخدا) say s.v. کوفیه / کوفیّه? Definition and origin tag."
}
```


### [2026-09-05T20:59:43.615Z] TOOL RESULT

```
# قیفال (Cephalic Vein) - Dictionary Definitions

## فرهنگ معین
This dictionary provides the most concise entry, marked with [ع.] (Arabic origin):
> "رگِ بازو" (a vein in the arm)

## لغت نامه دهخدا
The Dehkhoda dictionary offers extensive coverage. It identifies the term as معرب (arabicized) and notes the Greek origin: "از یونانی کفاله بمعنی سر و رأس است" (from Greek *kephalē* meaning head/summit).

The entry details two primary meanings:
1. **General anatomical use**: adjective form meaning "relating to the head" (رأسی), as in *vein of the head* or *artery of the head*
2. **Specific use**: referring specifically to the cephalic vein itself

It emphasizes the vein's medical application: "فصد قیفال علتهای سر و چشم و بینی و کام و دهان" (bloodletting from the cephalic vein benefits head, eye, nose, and mouth conditions).
```


### [2026-09-05T20:59:43.691Z] TOOL RESULT

```
# Persian Dictionary Definitions of کوفیه

**Origin Tag:** Arabic (ع. کوفیة)

**Definitions:**

From **Dehkhoda Dictionary:**
A square headscarf worn by Arab men, with a special cord (عقال) placed over it. The entry describes it as "a square piece of linen, silk, or cotton placed on the head such that two corners fall on the shoulders and two on the forehead."

From **Farhang-e Moein:**
"A four-cornered headscarf that Arab men wear on their heads, with a special cord placed over it called عقال."

From **Farhang-e Amid:**
A square headscarf worn by Arab men, with a special band placed over it; also called چپیه (a cap).

Both dictionaries identify it as traditional Arab male headwear with accompanying binding or cord elements.
```


## [2026-09-05T21:00:00.536Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### WLD Bd1 ghebhel\"; grep -n -i \"ghebhel\\|ghebh-el\\|kefalh\\|κεφαλή\\|gibla\" incoming/WLD/WLD_Bd1_pages.txt | head -20\necho \"### WLD Bd1 gafl\"; grep -n \"gafl\" incoming/WLD/WLD_Bd1_pages.txt | head -10\necho \"### IEC ghebh\"; grep -n -i \"ghebh\\|khephal\\|kephale\" IEC.txt | head -10\necho \"### SYN head\"; grep -n -i \"kephale\" SYN.txt | head -5"
}
```


### [2026-09-05T21:00:00.635Z] TOOL RESULT

```
### WLD Bd1 ghebhel
50337: der Yerg'leich mit ahd. gib 'd „Giebel“ bei Pedersen KG. I 39            (s.   *ghebhel-).
54327:ghebh-el-,      -ol-, -( e )l-   „Giebel; Kopf".
### WLD Bd1 gafl
50073:gaflFen' , ags.cPpan „beobachten, ausschauen nach, sorgen fiir, schiitzen",
50310:vulva",      cymr. gaflGabel; Schenkelgabel, vulva", abret. Plur. gablau
50323:dings aisl. gaflak ags. gafduc „Ieichter WurfspieB aus einem air. *gablach
52037:dan. paa gafle „weit offcn", schwed. pa gavel ds.
### IEC ghebh
4608:ghargho- — ghebholos, à
4623:ghebh- “be able, be capable, master, acquire”. Cf. ghabh-, ghabh- Ir. cf. do-gheibhim *be able; be allowed; get, find’; geab “charm; Li. gebu, en “be able; be wont; use’. Cf. MHG gabe “acceptable?
4624:ghebholos, à (1) ‘peak, tip, top; knob, head, spike'. WP I, 533 Gk. kephalé; Maced. kebalé, keblé, kéble ‘head’; Tokh. $pal, id.; Galatian (Hes.) gaba- lán, id.; Gallo-Lat. gabalus, gabalum ‘gal- lows’; Oir. gabul ‘gibbet; fork’; MIr. gabal ‘fork’; Ir. gabhal ‘fork, beam, pillar, branch’;
4626:OBr. gabl ‘fork’; W gafl, id.; Br. gaól, gavl “fork, spit' (Celtic LW in G Gabel, etc.); OHG gëbal, MHG gëbel ‘head, skull, gable’; Du. gevel *gable-end'; Slovene žebelj "nat" (A variant of type *ghebhor- arises in Ir. geabar *arge-headed fish’, cf. Gk. képhalos ‘mullet’, and in Latv. Zeburs ‘two-pronged fork") (ghebholos (2) *piece' in OE geofola, giefel *morsel'. See gabholos and cf. WP I, 571) ghed- “acquire; acquisition'. Cf. ghnd- and WP I, 589 Oss. zíd, zudà (‘greedy fr. *ghedu-, *gheduo); Lat. cf. -da (for *-heda in prae-da ‘booty’; hedera ‘ivy’, fr. a neut. pl. *ghedeso; and helluo (?) ‘glutton’, if for *ghed-leuon, see leu-); OE gietan ‘get; ON geta, id. beside geta, f. ‘guess’; MHG -gezs- in a-gezzel "Tor, getful'; er-gezzen ‘forget; (*-6- in) gæze, adj. ‘greedy’ and ON gæta ‘watch, heed', ON gáta ‘riddle’, Sw. gåta, id. and apparently *-0- in Cz. zá-hada, id.; OCS cf. Zadati ('desire', if distinct from ZeZdo, Zedéti, id. See ghnd- and cf. OCz. žádný *beloved") (*-e-); Li. gedáuju, -auti ‘desire’. Uncertainly Alb. gjuej, gjuaj ‘hunt beside gjojé, f. ‘hunt’, fr. *ghed- (cf. the LW rruej, rruaj ‘shave’ fr. Lat. radere). Cf. ghend-. Alb. gjej “find, guess? is ambig. A desiderative form of type *ghedsio occurs
4632:ghebholos — gheltos
### SYN head
```


## [2026-09-05T21:00:09.645Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '54320,54360p' incoming/WLD/WLD_Bd1_pages.txt\necho \"=== pdf page tag near ===\"\nawk 'NR>=54200 && NR<=54360 && /pdf page/' incoming/WLD/WLD_Bd1_pages.txt\necho \"=== WLD ghei yawn WP I 548 ===\"\ngrep -n \"gh.i- : ghi-\\|„gähnen\\|gähnen, klaffen\\|ghē-, ghǝ-\" incoming/WLD/WLD_Bd1_pages.txt | head -10"
}
```


### [2026-09-05T21:00:11.132Z] TOOL RESULT

```
   Lit. labas „Ast, Reisig, Zaum",            labd „Rute, Gerte", sfi.hu r as „diirrer Ast",
zciboju , zaboti „aufzaumen“, zaboklas „Zugel", r.aboklis „Knebel“, lett.             zababt
,,mit einem Knebel das junge                 Tier am Saugen verhindern", lit. zuobris
(Kurscbat zuobrys) „Pflugschar".
   Zupitza G. 193, Ficklll 4 34, Falk-Torp 505, 518, Trautmann Bsl. Wb. 364.

ghebh-el-,      -ol-, -( e )l-   „Giebel; Kopf".
   Gr. y.Ecpakrj „Haupt, Ende, Gipfel", alexandr. y.efih), maked. y.efiaXfj EM.,
Hes. (und wohl ebenfalls maked. yafialav lyy.kcpaXov ) y.ezpaXyv Hes., siehe
                                                             '
                                                                        I


Fick KZ. 42, 147); got. ijibla „Giebel, Zinne", ahd. gib'd „Giebel, Pol",
gebal „Schadel, Kopf", ablautend anord. <jafl m. „Giebelseite eines Hauses,
Spitze einer Insel".   Fick I 4 415, III 4 126, Falk-Torp u yavl, usw.        .




   Air. gualu „Schulter" (Pedersen KG. 1117 z w.) vielmehr zu *geu „biegen“.

ghed- „scheiBen“. (DaB bierin eine Erweiterung von                  ,.gahnen, klaffen"
     yorliege und von der im Germ.                   —
                                                und Phrygischen ?        vorhandenen
                                                                                   -
                                                                                       —
     Bedeutung „Offnung‘ auszugelien sei, ist eine umvahrscheinliche Yer-
     rautung Perssons Beitr. 599 und Boisacqs).
  Ai. lmdati hadatc ,8cheit>t“, av. zadah- m. ,,Steili arm .jet (o. St.) „Sch\vanz,
               ,

(des Ilundes, Fuchses. Lowen)" I'Htibscbmann Arm. Gr. 1 470.: gr. yklfco
„scheiBo", yodarov zip’ edgai’ Hes., yodizevsiv azroziazeli’ lies., phryg. Qkzva                                •



<Pgvyiog     f] Xk$ig. orpxalvti de zijv nvhp’. Photius (1. ztvyrp’1 s. Solmsen KZ.

34, 7 0 f. ), alb. djes „scheitie" (G. Meyer BB. S. 187, Alb. Wb. 86, Pedersen
=== pdf page tag near ===
=== WLD ghei yawn WP I 548 ===
```


## [2026-09-05T21:00:18.695Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"pdf page\" incoming/WLD/WLD_Bd1_pages.txt | head -3\npython3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nprint('leaf for 54327:', '\\n'.join(lines[:54327]).count('\\f'))\nEOF\necho \"=== WLD ghe yawn ===\"\ngrep -n \"ghe- : gh.-\\|ghei- : ghi-\\|ghēi\\|„gähnen\" incoming/WLD/WLD_Bd1_pages.txt | head -20"
}
```


### [2026-09-05T21:00:20.423Z] TOOL RESULT

```
leaf for 54327: 579
=== WLD ghe yawn ===
```


## [2026-09-05T21:00:25.126Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\nlv=t.split('\\f')\nfor i in (555,556):\n    print('=== leaf',i)\n    print(lv[i][:1600])\nEOF"
}
```


### [2026-09-05T21:00:27.047Z] TOOL RESULT

```
=== leaf 555
                                                        ghei-       :
                                                                        ghi-                                                      547

wetter, \Yinter“ (dazu stellt Sommer aaO. auch ydgagog .Zapfen" ala
„Schlechtwetterspund". ?? Nicht wahrscheinlich deutet Prellwitz 2 504 yd-
yagog aus |     ghei- „antreiben“ -f- mar ,Wasser, Meer"); alb. dimen m.
„Winter“ (G. Meyer BB. 8, 187, Alb. Wb. 67, Pedersen KZ. 36, 333).
      Lit. ziema, lett. z'lema, pr. sumo „Winter“, aksl. zima, russ. zimd, bulg. zima,
skr. zima,              slov.    zima, cech. zima, poln. zima ds.                                (m < mn Job. Schmidt
                                                                                                            :



KdS. 100, 119).
      Dazu *yheim(e)rinos und '*yheiminos „winterlich“.
      In gr. ysifisgivog,             lat.   hibernus (< %gheimrinos                        s.   Solmsen KZ. 34, 18 mit
Lit.),       lit.   ziemmis       ,
                                      aksl. zimvnz, russ. zimnij. skr. zhmu,                            cech zimni (cech.
                                                                                                                .




zimnij „kalt“), poln. zimny „kalt, winterlich" (vgl. mit                                            i   in der Wurzelsilbe
arm. jmern „Winter“ Hiibschmann Arm. Gr. I 471).
      Zu *gheimen auch av. zaen- m. „Winter“, np. tlai.
   (Nach Bartholomae Ir. Wb. 1666 zacna < *ghehnno), av. zayana „winter-
lich“  und mit Vrddhierung
=== leaf 556
                                                                                        d                                                  ;




548                                                            ghei-        :
                                                                                ghl-



liches    Lamm",  dial, aber „einjahriges Lamm“     (Pedersen KZ. 32, 248),
andfrk.   (Lex Saliea) ingimus ? „poreus anniculus". (Die Formen mit y                                                                 :



aisl. ijymbr  „einjahriges Lamm", norw. gymber, schw. gymmer beruben
wahrscheinlich auf EinfluB des nicht verwandten          iibrigens ungedeu-                 —
teten — aschw. gummerlamb „Widder“, isl. gumarr, norw. gumse, schw.
gumse „\Yklder" siehe Hellquist SyEO. 210. Unwahrscheinlich Peder-
sen KZ. 32, 248: yijmbr                          <
                            *ghhnrl, und Torp Sprogl. hist. Studier tilegn.
Unger 18S; gm- in gymber, gumse nsw. ablautend mit gam- in ahd. gamiz
„Steinbock“   letzteres ist nach Liden KZ. 40, 257, oben 385 wahrschein-
                      ;


licb entlebnt.)
   Ygl. im            allgemeinen Curtius 202,            Vanirek 96, Fick I 4 53, 218, 434,
II 4 104, III 4 126 f.,                    Falk-Torp 218, 310, 321, Trautmann Bsl. Wb. 367,
Specht aaO.


ghei-     :  ghl- (dazu der weitergebildete Stamm ghii-a; die langdiphthongische
         Basis erkannt von Schulze KZ. 27, 425, vgl. auck Persson Beitr. 696 f.)
         , .gahnen,  klaffen"; schallmalend fur den Gahnlaut (s. auch u. ghans-
         „Gans“; ahnli
```


## [2026-09-05T21:00:34.176Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\nlv=t.split('\\f')\ns=''.join(lv[556:562])\nimport re\nprint(s[1200:4000])\nprint('--- np. mentions ---')\nfor m in re.finditer(r'np\\.\\s*\\S+', s):\n    print(m.group(0))\nEOF"
}
```


### [2026-09-05T21:00:35.790Z] TOOL RESULT

```
ek 96, Fick I 4 53, 218, 434,
II 4 104, III 4 126 f.,                    Falk-Torp 218, 310, 321, Trautmann Bsl. Wb. 367,
Specht aaO.


ghei-     :  ghl- (dazu der weitergebildete Stamm ghii-a; die langdiphthongische
         Basis erkannt von Schulze KZ. 27, 425, vgl. auck Persson Beitr. 696 f.)
         , .gahnen,  klaffen"; schallmalend fur den Gahnlaut (s. auch u. ghans-
         „Gans“; ahnlich, aber mit Yelar, gha gha fur gackern und dgl., s. d.).
         Neben ghei und wohl daraus vor Ivons, entstanden ghe gho: kaum                                 :




         ist umgekehrt ghei- in ghe + formantischem i zu zerlegen. Im Gr. auch

         gho-, vermutlicb infolge etwas anderer Auffassung des Gahnlautes (vgl.
         dieselbe Yeranderlichkeit des Yokals bei gha gha ghe ghe ghl gh     .).                :               :            .   .


         Endlich auch ghe a ghdu, entweder als wieder etwas andere Auffassung
                                                 :




         des Gahnlautes, oder mit ursprgl. formantischem u (ahnlich Bechtel
         Hauptprobleme 276; s. auch Persson Beitr. 708f.). Ygl. noch ghri-
         „fehlen, mangeln".
      Ai. vi-hu-, Praes. vijilute „auseinander klaffen“ (s. auch u. ghe(ij- „fehlen,
 mangeln“\ vihaya-h „Luftraum“.
      Gr. yday.a)               „giihne. klaffe" (nur Praes. und Impf. spater von
                              (ghy-slv i                                                                    ;



 yaivio       abgelost,        ghan-; ydaxco, yaivco nicht nach Hirt Abl. § 360,
                                 s.       u.
 GrGr. 2       191 aus ghh-), ydo/ua „klaffende Offnung"; yggayvg „Loch“, yrj oayk
 „eine groBe Muschel", nach yaoayo ?         ?/ rij? yrjg diaaraaig Hes. wohl mit
                                                                                '




 urgr. d (s. auch u. ghe(i)- „fehlen‘ ) yrjkrj, dor. yak   ,,die gespaltene (*klaf-
                                                                        ;


 fendej Ivlaue von Rindern, Schafen usw.; chirurgische Pinzette, zweispaltige
 Xadel, u. dgl."', yglog „Kiste, Lade" (nach Apoll. Dysk. ..ano rfjg biaord-
 OEO)5 rij; yard ryv uvoijv yivoyh'gg“) yj'jyg ,,das Gahnen, Gienmuschel".       ;


 Schwerlich hierher lat. fumes, fatlgo (s. u. dhe „hinsclrwinden“).
    Yon ghei- aus aksl. z'jg ,,hio" (nicht nach Zubaty AfslPh. 13, 622 f.
                                  :




 15. 500ff., Meillet Msl. 9, 137 ff. ;                          14, 14, Et. 175 aus *zjajq = lit. Zioju diss.,
 noch weniger nacli                       Ilirt Abl.         98 aus ghoi-vd- oder ghoi-ta-).
      Yon       ghiifi-        aus    :   lat.       liio,   -are   ,   .gahnen, klaffen,   aufgesperrt sein";                       lit.

  -Ju-ju, -fi
--- np. mentions ---
```


## [2026-09-05T21:00:52.545Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D9%83%D9%88%D9%81%D9%8A%D8%A9' --note 'page 182, root Ghebh-el node 7: Arabic kufiyya etymology (from Kufa, not Italian cuffia)' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/cuffia' --note 'page 182, root Ghebh-el node 6: Italian cuffia < Late Latin cofia < Proto-West-Germanic *kuffju' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%CE%BA%CE%B5%CF%86%CE%B1%CE%BB%CE%AE' --note 'page 182, root Ghebh-el node 1: Greek kephale < PIE *gwhebhol / *ghebh-l' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/gable' --note 'page 182, root Ghebh-el nodes 9-10: gable < OF gable < ON gafl < PGmc *gablaz < PIE *ghebh-el-' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/cephalic' --note 'page 182, root Ghebh-el nodes 4-5: cephalic < L cephalicus < Gk kephalikos' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/yawn' --note 'page 182, root Ghei nodes 2-4: yawn < OE ginian/gionian < PGmc *gin- < PIE *ghieh-' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/chasm' --note 'page 182, root Ghei nodes 5-6: chasm 1590s < L chasma < Gk khasma' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/gasp' --note 'page 182, root Ghei nodes 7-8: gasp < ON geispa; gap < ON gap; gape < ON gapa' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://abadis.ir/fatofa/%D9%82%DB%8C%D9%81%D8%A7%D9%84/' --note 'page 182, root Ghebh-el node 3: Persian qifal, Dehkhoda derives from Greek kephale; Moin tags [ع.] rag-e bazu' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://abadis.ir/fatofa/%DA%A9%D9%88%D9%81%DB%8C%D9%87/' --note 'page 182, root Ghebh-el node 8: Persian kufiyye, Moin [ع. کوفیة]' 2>&1 | tail -3"
}
```


### [2026-09-05T21:01:00.162Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/7fb0790131ff780c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b8b1e8481602be16.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4591756d9ef43c32.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d67f670f42cebac7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4ab744f48ae253e0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/be1338012fe8c84c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f00ddc5f74e91db3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/18314c9a13708dbc.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e4d4cda68901436b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4a85505cb5f6166e.txt
```


## [2026-09-05T21:01:07.327Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### AFM qifal\"; grep -n \"القيفال\\|قيفال\" AFM.txt AFM_pages.txt 2>/dev/null | head\necho \"### FVQ\"; grep -n -i \"qifal\\|kufiyy\" FVQ.txt | head\necho \"### DEV coiffe\"; grep -n -i \"coiffe\\|cuffia\" DEV.txt PHN.txt | head\necho \"### SYN yawn/head\"; grep -n -i \"4\\.20 HEAD\\|yawn\" SYN.txt | head\necho \"### WEB cephalic\"; grep -n -i \"cephalic\" WEB_vol1.txt | head -3\necho \"### FSD\"; grep -n -i \"al-qifal\\|qifal\" FSD_vol1.txt FSD_vol2.txt 2>/dev/null | head"
}
```


### [2026-09-05T21:01:07.449Z] TOOL RESULT

```
### AFM qifal
### FVQ
### DEV coiffe
PHN.txt:3954:COIFFE, s. f. et COUFFIN , s. m. (a.)
### SYN yawn/head
4785:1, If *§hans-, prob. fr. the root seen in Grk. xéoxw, éxavov ‘yawn, gape’, with reference to the goose’s characteristic Squawk with wide open bill. Walde-P. 1.536. Ernout-M. 56. Walde-H. 1.52. Berneker 342,
5210:Yawn, Garp
5803:Lett. Zuokls, perh. with Zakle ‘fork of a tree’, fr. the root in Lith. -zioti ‘yawn, gape’, etc. (4.52). Mihl.-Endz. 4.839.
6737:in general (of the earth, etc.). Nearly all of them show secondary associations with mental attitudes of which the ac- tion is indicative, namely wonder, stu- pidity, or fatigue. In such secondary associations they may be differentiated, as NE yawn (with fatigue) and gape (in- dicating wonder or stupidity; hence also ‘stare at? with open mouth, as usually NHG gaffen; but gape formerly and still locally ‘yawn’), or be restricted to one or another of these notions.
6739:2 oe Sit.) NOW ‘yawn’; Lat. hiadre; ON gina, OER ginan 14) Z . =) sane gan, ganian, ME zone, 1 gane, NE yawn (NED vb. and yawn S.VV. gane, Ginén, geinon, ae Du - geeuwen, ONG Teton omen, ots. Wace iene th. Ziovaut; in ees AG gahnen; “Avdties; Chg). 4; cpds. ~Zioti, Lett. tnd eijaja), ete. penn at (Pres: ahha tr (G8 ty eREAl Slave; Took “ane, Language 21.21),
6743:op THE BODY; B pants ° 4.52 YAWN, GAPE . Goth aan Lith. Ziovauli, -Ziolt xy, XATHAOH AE ina, gapa Lett.  2dvdties Grk- a xa pouprouHat ON: Cabe ChSI. zingli, zijati NG piare Sw. gapa ay SCr. Zijevati Lat spadigliare OE ginan, ginian, ganian Boh. —zivati It pailler, bayer ME = gone, yane, gape Pol. = ziewaé a hostezar NE yawn, gape Russ. zevat! ay cisca Du. gapen, geeuwen Skt.  grmbh- Tf ER itn fadh- OHG ginén, gién, giwen, Av. Beets Ir. 409! etc. N a bi: MHG ginen, geinen, gewen, w. oe gen, bazailhat ete. Br «ts NHG gédhnen, gaffen . sary notion of the words list- Here prob. also ON, Sw. gapa, Dan. TNE ec ide’ ME, NE gape fr. N e mouth wide’. Many gabe (ME, gape fr. Norse), Du. gapen,
6746:Sp. bostezar, a differentiated form (with unexplained st, Cuervo, s.v.; perh. by a blend with a VLat. *dsticare by transposition fr. Lat. dscitare ‘yawn’), of bocezar formerly ‘yawn’ (now ‘move the lips’, of animals eating), Port. bocejar ‘yawn’ : It. boccheggiare ‘gasp’ (of fish out of water), dial. boccheare ‘yawn’, all derivs. of bo(c)ca ‘mouth’ (4.24).
6748:3. Ir. ménaigim, NIv. méanfuighim (not used; rather doghnim méanfadhach ‘make a yawn’), deriv. of mén, NIr. méan ‘mouth’ (4.24).
19971:OHG giri (generally renders avarus) MHG giric, girisch, (cf. NHG habgier ‘avarice’), Du. gierig : Goth. fathu-geiro OS fehu-girt ‘avarice’, perh, through the notion of standing ‘open, yawning’, fr, the root in OHG gren, etc. ‘yawn’, Walde-P. 1.549. Franck-v. W - 198. Feist 136f.
20581:Sp. ganancia, fr. ganar ‘win, gain’, orig. dub., perh. fr. a Goth. form be- longing with OF ginan, ganian, etc. ‘yawn, gape’ (4.52), with semantic de- velopment through ‘open the mouth for, snap at’. Cf. the equally radical change in OE (Lindisf.) gtwian ‘ask for’ : OHG giwen ‘yawn’ (Sievers, Anglia 16.98 f.).
### WEB cephalic
2324:ac’r0-ceph/a-lous, a. acrocephalic. a
22898:bra-chis’to-cé-phal/ic, bra-chis-to-ceph’a- lous, a. (Gr. brachistos, superl. of brachys, short, and kephalé, head.) having a wide head; having the breadth of the cranium greater than the length, according to the cephalic index.
30048:cephalic index
### FSD
```


## [2026-09-05T21:01:19.257Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '3954,3975p' PHN.txt\necho \"=== Buck 4.20 head ===\"\ngrep -n -o \".\\{0,300\\}4\\.20 HEAD.\\{0,600\\}\" SYN.txt | head -3\ngrep -n -o \"kephale.\\{0,300\\}\" SYN.txt | head -5"
}
```


## [2026-09-05T21:01:21.508Z] TOOL CALL #51: Bash

```json
{
 "command": "ls site/pages/182.jpg 2>/dev/null; pdftoppm -f 182 -l 182 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg182 && echo OK && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-05T21:01:23.154Z] TOOL RESULT

```
COIFFE, s. f. et COUFFIN , s. m. (a.)
iULi [^otf^i] Espèce de cabas ou panier fait de jonc ou de
feuilles de palmier, et dont l'usage est très-répandu en Pro-
vence. — Les Espagnols écrivent alcofa, en faisant précéder le
mot arabe de l'article al. Comparez aussi avec l'arabe le grec
x6(ptvoç et le latin œphinus.
COLFIQUE et KOUFIQUE, adj. des a g. (a.)
Ji^ [^^^^H^yy] ^^ Koufat (Âi^^), ville de l'Irak Arabi, située
à 1 39 kilomètres au sud de Baghdad. — On appelle ^Jk^)a^^
\khaH hAjiyy\ ou écriture koujique, celle dont les Arabes de
Koufat faisaient jadis usage; elle est lourde et peu facile à
bre, vu l'absence des points particuliers à certaines lettres. Elle
présente une très-grande analogie avec l'ancienne écriture
syriaque, dite estranghélo, dont elle paratt dérivée, et sert quel-
quefois encore, dans les manuscrits maghrébins, pour indi-
quer les principales divisions des ouvrages et pour les som-
maires des chapitres. — Voyez, h la suite du mot Nbskhy, les
noms des divers genres d'écriture arabe, turque et persane.
COULOGHLI, s. m. composé, (t.)
Jls^I 9i^[keuleh oghhf]fh d'esclave. En Algérie, cette déno-'
mination s'applique aux fils de Turcs et de femmes mauresques.
Les coulogkli» ou Tureo-Arabeê ne se rencontrent qu'en petit
=== Buck 4.20 head ===
ugrep: error: error at position 88
80-\xbf][\x80-\xbf]*){0,600}
                            \___exceeds complexity limits
```


### [2026-09-05T21:01:25.229Z] TOOL RESULT

```
site/pages/182.jpg
OK
total 24264
drwx------ 2 sfmqrb sfmqrb    4096 Sep  5 17:01 .
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
-rw-rw-r-- 1 sfmqrb sfmqrb   24939 Sep  5 17:01 n14.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2692 Sep  5 16:49 n16.png
-rw-rw-r-- 1 sfmqrb sfmqrb    6463 Sep  5 17:01 n17.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7472 Sep  5 17:01 n19.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3215 Sep  5 17:01 n5.png
-rw-rw-r-- 1 sfmqrb sfmqrb   11831 Sep  5 16:32 node4.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7427 Sep  5 16:32 node7.png
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep  5 16:13 oldpers_djvu.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    6054 Sep  5 16:36 p152_e0left.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2672 Sep  5 16:36 p152_node2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   35268 Sep  5 16:59 p162a.png
-rw-rw-r-- 1 sfmqrb sfmqrb   14337 Sep  5 16:59 p162b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   76438 Sep  5 16:59 p162.png
-rw-rw-r-- 1 sfmqrb sfmqrb   41788 Sep  5 16:53 p173_ital.png
-rw-rw-r-- 1 sfmqrb sfmqrb   32898 Sep  5 16:53 p173_op.png
-rw-rw-r-- 1 sfmqrb sfmqrb  161412 Sep  5 17:01 p174hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  173427 Sep  5 17:01 p176hi.png
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
-rw-rw-r-- 1 sfmqrb sfmqrb   70664 Sep  5 17:00 pg174.png
-rw-rw-r-- 1 sfmqrb sfmqrb   54907 Sep  5 16:54 pg175.png
-rw-rw-r-- 1 sfmqrb sfmqrb   83583 Sep  5 17:00 pg176.png
-rw-rw-r-- 1 sfmqrb sfmqrb   64024 Sep  5 17:01 pg178.png
-rw-rw-r-- 1 sfmqrb sfmqrb   57139 Sep  5 16:54 pg179.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81598 Sep  5 16:58 pg180.png
-rw-rw-r-- 1 sfmqrb sfmqrb   56794 Sep  5 17:00 pg181.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66020 Sep  5 17:01 pg182.png
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


## [2026-09-05T21:01:30.048Z] TOOL CALL #52: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg182.png"
}
```


### [2026-09-05T21:01:30.380Z] TOOL RESULT

```

```


## [2026-09-05T21:01:30.379Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T21:01:50.742Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%81%D8%A7%DA%98%D9%87/",
 "prompt": "What do فرهنگ معین and لغت‌نامه دهخدا say s.v. فاژه (and فاژ / فاژیدن)? Give the definition and any etymological note or origin tag."
}
```


## [2026-09-05T21:01:52.297Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '7540,7552p' FRS.txt\necho \"=== leaf for FRS 7546 ===\"\npython3 - <<'EOF'\nt=open('FRS_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nprint('leaf', '\\n'.join(lines[:8183]).count('\\f'))\nEOF"
}
```


### [2026-09-05T21:01:56.261Z] TOOL RESULT

```
Based on the webpage content provided, I can only report what appears for **لغت‌نامه دهخدا** (Dehkhoda Dictionary):

**Definition:** "فاژه است که خمیازه باشد" (a yawn or the act of yawning)

**Etymology/Source note:** The entry references "برهان" (Burhan dictionary) and includes a poetic citation from Anouri illustrating the term's usage.

---

Regarding **فرهنگ معین** (Moein Dictionary): The webpage does not provide specific content from this source. It only mentions that Abadis's dictionary includes "فرهنگ معین" among its referenced works, but no actual definitions or etymological information from that dictionary appears on this page.
```


### [2026-09-05T21:01:57.927Z] TOOL RESULT

```
۱۷۸ 
ژاژ داری تو و هستند بسی زاژ خوران 
وین عجب نیست که تازند سوی ژاژخران 
دهن دره بود که که آنرا آسا کفتیم | لییبی گفت 
قیاس کو نش چکونه کنم بباوبکوی ایا گذشته بشعرازییانی ۲ وبوالحر ۳ 
اکرندانی؛ بندیش تا چکونه بود که‌سبزه* خوردهفاژدبهار که" اشتر | 


و۳ 
کیاهی بود سخت تلخ درد شکم راسود دارد | منحيك گفت : 
ويحك ای بزقعی ای تلختر از آب فرژ 
تاکی این طبع۸ بد تو که بکیرد سر پژ | 
=== leaf for FRS 7546 ===
leaf 197
```


## [2026-09-05T21:02:15.760Z] TOOL CALL #55: Bash

```json
{
 "command": "sed -n '1,200p' tools/verify_check.py"
}
```


### [2026-09-05T21:02:15.794Z] TOOL RESULT

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


## [2026-09-05T21:03:40.354Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### LEW cephalicus\"; grep -n -i \"cephalic\\|cofia\\|cuphia\" LEW_1910.txt LAT.txt | head\necho \"### WEB gable\"; grep -n -i \"^gable\\|gable, n\" WEB_vol1.txt | head -3\necho \"### FSD gable/chasm\"; grep -n -i \"gable\" FSD_vol2.txt | head -3\necho \"### SKT chasm/gasp/gap\"; grep -n -i \"^chasm\\|^gasp\\|^gape\\|^gap,\" SKT.txt | head\necho \"### KLN chasm gasp\"; grep -n \"^chasm,\\|^gasp,\\|^gape,\\|^gap,\\|^yawn,\" KLN_1966.txt | head\necho \"### IEC ghebholos page\"; python3 -c \"\nt=open('IEC.txt',encoding='utf-8',errors='replace').read(); lines=t.split('\\n')\nprint('leaf', '\\n'.join(lines[:4624]).count('\\f'))\""
}
```


### [2026-09-05T21:03:42.471Z] TOOL RESULT

```
### LEW cephalicus
LAT.txt:34301:racine de linquS et que liquor serait a rapprocher de gr. XetTCOfiai,; la racine.
### WEB gable
### FSD gable/chasm
1285:(<  OF.  doniiBor.  <   L. mitorium;  see  dormitory.! dor'mart.— dor'nicr-wtn"- dow,  n.  Arch.  A   vertical window  placed  In  or  forming a   small  gable  rising  from  a   jb sloping  roof,  and  usui  ' opening  Into  asleepiag-ro' whenee  the  name;  also,  the  ‘ gable-like  structure  eontaln- Ing  it.  dormant  windowt.
11589:completed  In  1825.  In  1907  the  State  of  New  York  uudci-  !,r  i>"l“«  -nli  Wos  »   t   J')  'R  e- took to  render  it  navigable  for  vessels  of  1.000  to  1,20(1  Ions.  H V   r   w   i-‘>  l>bJ  C.S,  u,  (t.  g.)  (s
15174:Hard  fxveriencea  aro  often  the  foundati life,  __  Gable  Hr.  Seller  ■’  "
### SKT chasm/gasp/gap
7399:gap,  (Scand.)  M.E.  ^^//tf.  — Icel.  and Swed.^/,  a  gap,  abi'ss.  —  Icel.  and  Swcd. ^nAs  (above).     And  see  Oabblo.
### KLN chasm gasp
7259:chasm,  n.,  a  deep  crack  in  the  earth;  abyss.  — L.  chasma,  fr.  Gk.  /dupia,  ‘a  yawning  hollow, gulf’,  which  is  rel.  to  ytxftz tv,  ‘to  yawn,  gape’. See  chaos  and  cp.  polychasium.
15787:gape,  intr.  v.  —  ME.  gapen,  fr.  ON.  gapa,  whence also  Swed.  gapa ,  Dan.  gabe;  rel.  to  Du.  gapen, MHG.,  G.  gaffen,  ‘to  gape,  stare’.  The  ultimate origin  of  these  words  is  unknown.  Cp.  prec. word.  Cp.  also  gasp.
### IEC ghebholos page
leaf 186
```


## [2026-09-05T21:03:49.322Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"gasp,  \\|^gasp\" KLN_1966.txt | head -3\ngrep -n \"^yawn\" KLN_1966.txt | head -3\ngrep -n \"^gap,\\|gap,  n\" KLN_1966.txt | head -3"
}
```


### [2026-09-05T21:03:49.397Z] TOOL RESULT

```
15830:pixpr.v,  ‘measure’.  See  meter,  ‘poetical  rhythm’, gasp,  intr.  and  tr.  v.  —  ME.  gaispen,  gaspen,  ‘to yawn’,  fr.  ON.  geispa,  ‘to  yawn’,  whence  also Swcd.  gaspa,  Dan.  gispe,  ‘to  gasp’.  ON.  geispa is  prob.  formed  by  metathesis  fr.  *geip-sa  and is  rel.  to  ON.  gapa,  ‘to  gape’.  Cp.  LG.  gapsen, ‘to  gasp’,  and  see  gape.
15831:Derivatives:  gasp,  n.,  gasper  (q.v.),  gasp-ing, adj.,  gasp-ing-ty,  adv.
4294:yawn’,  which  also  derive  fr.  VL.  bataeulare,  and see  bay,  ‘part  in  the  wall’, bain-marie,  n.  double  pan  for  holding  food.  — F.,  ‘water  bath’,  fr.  ML.  balneum  Mariae,  lit. ‘bath  of  Mary  (sister  of  Moses)’,  to  whom  var¬ ious  works  dealing  with  alchemy  were  attributed. See  balneal.
15786:Derivative:  Gaon-ic,  adj. gap,  n.  —  ME.  gap,  fr.  ON.  gap,  ‘chasm,  abyss’, rel.  to  ON.  gapa,  ‘to  gape’.  See  next  word. Derivative:  gapp-y,  adj.
```


## [2026-09-05T21:11:08.306Z] TOOL CALL #58: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build182.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\n\ne0 = {\n \"entry\": 0,\n \"root\": \"Ghebh-el\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *gʰebʰ-el- / *gʰébʰōl 'head; gable, top of a pitched roof'\",\n \"note\": \"Pokorny 423 has the lemma exactly as Nourai gives it: 'ghebh-el-, -ol-, -(e)l-', Meaning 'weathercock; head' (German 'Giebel; Kopf'), with Gk. κεφαλή, Goth. gibla, ON gafl, OHG gibil, Toch. A śpāl; Walde-Pokorny I 571 the same. Watkins/AHD heads the entry 'ghebh-el-. Head.' The root has a plain velar *gʰ (Lat. would give f-, Gk. χ-, hence the dissimilation in κεφαλή); Wiktionary reconstructs the noun as *gʰébʰōl. Language label ('Indo-European'), form and the double gloss 'head, top' are all correct — 'top' is the Germanic 'gable' sense. The two problems on this page are not in the root box but in the two loan-chains hung on the Greek node (Arabic al-qifāl, Italian cuffia), both of which modern scholarship rejects.\",\n \"note_fa\": \"ریشهٔ هندواروپایی آغازین *gʰebʰ-el- «سر؛ نوکِ بام، شیروانی» ریشه‌ای است شناخته و پذیرفته؛ پوکورنی در ص ۴۲۳ همین سرواژه را با همین معنی («Giebel; Kopf») آورده و والده-پوکورنی (جلد ۱، ص ۵۷۱) و واتکینز (پیوست ریشه‌های هندواروپایی فرهنگ AHD) نیز آن را تأیید می‌کنند. بازمانده‌های آن یونانی kephalē «سر»، گوتی gibla، نورس باستان gafl «کنارهٔ شیروانی» و تُخاری الف śpāl «سر» است. صورت، برچسب زبانی و معنیِ دوگانهٔ «سر، بالا» که نورایی داده هر سه درست است؛ اشکال کارِ این صفحه در ریشهٔ آن نیست، بلکه در دو زنجیرهٔ وام‌گیریِ عربی (قیفال) و ایتالیایی (cuffia) است که پژوهش امروزی هر دو را رد می‌کند.\",\n \"sources\": [W+\"%CE%BA%CE%B5%CF%86%CE%B1%CE%BB%CE%AE\"],\n \"ref_check\": [\n   {\"ref\": \"POK:423\", \"status\": \"supports\",\n    \"note\": \"POK_full.txt block ending 'Page(s): 423': 'Root/lemma: ghebh-el-, -el-, -lo- | Meaning: weathercock; head | Material: Gr. κεφαλή \\\"head, end, acme, apex\\\", maked. κεβλή … Gothic gibla \\\"gable, pinnacle\\\", changing through ablaut Old Norse gafl … Old High German gibil … Tocharian A śpāl \\\"head\\\" (: gr. κεφαλή). References: WP. I 571.' Exactly Nourai's root and gloss.\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. I leaf 579 = p. 571\", \"stance\": \"supports\",\n    \"note\": \"'ghebh-el-, -ol-, -(e)l- „Giebel; Kopf\\\". Gr. κεφαλή „Haupt, Ende, Gipfel\\\" … got. gibla „Giebel, Zinne\\\", ahd. gibil „Giebel, Pol\\\", gebal „Schädel, Kopf\\\", ablautend anord. gafl m. „Giebelseite eines Hauses, Spitze einer Insel\\\".' (grep 'ghebh-el' in incoming/WLD/WLD_Bd1_pages.txt)\"},\n   {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt line 510, s.v. ghebh-el-\", \"stance\": \"supports\",\n    \"note\": \"'ghebh-el-. Head. 1. Germanic *gablaz, top of a pitched roof, in Old Norse gafl, gable: GABLE. 2. Dissimilated form *khephel- in Greek kephalē, head: CEPHALIC … [Pok. ghebh-el- 423.]'\"},\n   {\"src\": \"IEC\", \"where\": \"IEC.txt line 4624, leaf 186 (≈ p. 342), s.v. ghebholos\", \"stance\": \"supports\",\n    \"note\": \"'ghebholos, ā (1) \\\"peak, tip, top; knob, head, spike\\\". WP I, 571. Gk. kephalé; Maced. kebalé, keblé …; Tokh. špal, id.; … OHG gëbal, MHG gëbel \\\"head, skull, gable\\\"; Du. gevel \\\"gable-end\\\".' Mann's o-stem beside Pokorny's -el-.\"}\n ],\n \"nodes\": []\n}\n\ne0[\"nodes\"] = [\n {\n  \"id\": 1, \"lang\": \"Greek\", \"words\": \"kephalě\", \"verdict\": \"confirmed\",\n  \"derivation\": \"Ancient Gk. κεφαλή 'head, top, end, summit' goes back to Proto-Hellenic *kʰepʰəlā́ < PIE *gʰebʰ-l̥- with the feminine suffix *-eh₂. The regular Greek outcome of *gʰ…bʰ… would be *χεφαλή; the first aspirate was dissimilated to a plain κ- (Klein p. 259: 'dissimilated fr. *χεφαλή'; Watkins: 'Dissimilated form *khephel-'), and the undissimilated variant survives in Macedonian κεβλή / κεβαλή, quoted by Pokorny and by the Etymologicum Magnum. The cognates that fix the root are Gothic gibla 'gable, pinnacle', OHG gebal 'skull, head', ON gafl and Tocharian A śpāl 'head'. Nourai's root→Greek arrow, form and gloss are all correct.\",\n  \"derivation_fa\": \"یونانی باستان κεφαλή (kephalē) «سر، قله، نوک» از یونانیِ آغازین *kʰepʰəlā́ و آن از هندواروپایی آغازین *gʰebʰ-l̥- با پسوند مادّینهٔ *-eh₂ است. بر پایهٔ قاعده باید *χεφαλή می‌شد؛ دمیدگیِ نخست به‌سبب ناهمگونی (dissimilation، قاعدهٔ گراسمان‌گونه) از میان رفته و κ- برجای مانده است — کلاین در ص ۲۵۹ همین را می‌گوید و صورتِ دگرگون‌نشدهٔ مقدونی κεβλή/κεβαλή گواه آن است. هم‌ریشه‌های قطعیِ آن گوتی gibla و آلمانی علیای باستان gebal «کاسهٔ سر» و تُخاری الف śpāl «سر» است. ادعای نورایی در این گره کاملاً درست است.\",\n  \"sources\": [W+\"%CE%BA%CE%B5%CF%86%CE%B1%CE%BB%CE%AE\"],\n  \"ref_check\": [\n    {\"ref\": \"POK:423\", \"status\": \"supports\", \"note\": \"'Material: Gr. κεφαλή \\\"head, end, acme, apex\\\", maked. κεβλή, κεβαλή' — the Greek word is the first item under the root (POK_full.txt, Page(s): 423).\"},\n    {\"ref\": \"KLN:259\", \"status\": \"supports\", \"note\": \"KLN_1966.txt line 6992 (leaf 147 = printed pp. 258-259), s.v. cephalic: 'fr. L. cephalicus, fr. Gk. κεφαλικός … fr. κεφαλή, \\\"head\\\", dissimilated fr. *χεφαλή, fr. I.-E. base *ghebel-, whence also Toch. A śpāl-, \\\"head\\\", Goth. gibla, ON. gafl, \\\"gable\\\".' Nourai's page number is exact.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. I p. 571 (leaf 579)\", \"stance\": \"supports\", \"note\": \"'Gr. κεφαλή „Haupt, Ende, Gipfel\\\", alexandr. κεβλή, maked. κεβαλή EM.'\"},\n    {\"src\": \"AHD\", \"where\": \"s.v. ghebh-el- (AHD_watkins1985.txt line 510)\", \"stance\": \"supports\", \"note\": \"'2. Dissimilated form *khephel- in Greek kephalē, head: CEPHALIC, CEPHALO-, -CEPHALOUS; ENCEPHALO-, ENKEPHALIN, HYDROCEPHALUS.'\"},\n    {\"src\": \"IEC\", \"where\": \"s.v. ghebholos (leaf 186)\", \"stance\": \"supports\", \"note\": \"'Gk. kephalé; Maced. kebalé, keblé, kéblē \\\"head\\\"; Tokh. špal, id.'\"}\n  ]\n },\n {\n  \"id\": 2, \"lang\": \"Arabic\", \"words\": \"qîphaleh, al-qîphâl\", \"verdict\": \"disputed\",\n  \"derivation\": \"Arabic القيفال al-qīfāl is not a word for 'head' at all: it is the medieval anatomists' name of the vein of the outer upper arm — the 'cephalic vein' — as Mo'in ([ع.] 'رگ بازو') and Dehkhoda both give it. Klein p. 259 — Nourai's own reference, and the source of the chart's NOTE — states flatly that qifāl is 'a word of uncertain origin, which was confused by the translators of Avicenna with Gk. κεφαλή, \\\"head\\\"', following Joseph Hyrtl, Das Arabische und Hebräische in der Anatomie (Vienna 1879, pp. 96-98); the exactly parallel case is Arab. al-bāsilīq → ML vena basilica, wrongly matched with Gk. βασιλικός 'royal' (Klein p. 159). So the modern view is the reverse of the arrow drawn: no Greek word was borrowed into Arabic; a native Arabic vein-name was re-spelt in Latin as if it were Greek. The old Persian-Arabic lexicographic tradition (Dehkhoda: 'معرب و از یونانی کفاله بمعنی سر و رأس است') does take it from Greek, but that is precisely the identification Hyrtl and Klein showed to be a medieval folk etymology. Nourai's gloss 'head' is in any case wrong for the Arabic word.\",\n  \"derivation_fa\": \"«قیفال» در عربی هرگز به معنی «سر» نیست؛ نامِ سیاهرگِ رویهٔ بیرونیِ بازوست (ورید قیفال) که در طبّ دورهٔ اسلامی به کار می‌رفت — معین آن را با نشانِ [ع.] و معنی «رگِ بازو» آورده است. کلاین در همان ص ۲۵۹ که نورایی به آن ارجاع می‌دهد می‌نویسد qifāl واژه‌ای است با خاستگاهِ ناشناخته که مترجمانِ قانونِ ابن‌سینا آن را به‌خطا با یونانی kephalē «سر» یکی گرفته‌اند (به پیرویِ یوزف هیرتل، ۱۸۷۹)؛ نمونهٔ کاملاً همانند آن «الباسلیق» است که به‌غلط با یونانی basilikos «شاهانه» سنجیده شده. پس جهت‌گیریِ فلش نورایی وارونه است: واژه‌ای یونانی به عربی نرفته، بلکه واژه‌ای عربی در لاتینِ سده‌های میانه به شکلِ یونانی بازنویسی شده است. سنّتِ فرهنگ‌نویسیِ فارسی (دهخدا: «معرّب و از یونانی کفاله به معنی سر») همان ریشه‌شناسیِ عامیانهٔ کهن را تکرار می‌کند؛ پژوهش امروزی آن را نمی‌پذیرد.\",\n  \"sources\": [\"https://abadis.ir/fatofa/%D9%82%DB%8C%D9%81%D8%A7%D9%84/\"],\n  \"ref_check\": [\n    {\"ref\": \"KLN:259\", \"status\": \"contradicts\", \"note\": \"KLN_1966.txt line 6993 (leaf 147 = p. 259), s.v. 'cephalic vein (anat.)': 'ML. vena cephalica, fr. Arab. al-qifāl, fr. al-, \\\"the\\\", and qifāl, a word of uncertain origin, which was confused by the translators of Avicenna with Gk. κεφαλή, \\\"head\\\" … See Joseph Hyrtl, Das Arabische und Hebräische in der Anatomie, Wien, 1879, p. 96-98.' The chart's own NOTE quotes this correctly; it contradicts the arrow above it.\"},\n    {\"ref\": \"MON:2769\", \"status\": \"partial\", \"note\": \"Mo'in does have قیفال, but tagged [ع.] and glossed 'رگِ بازو' (a vein of the arm), not 'head' (abadis.ir/fatofa/قیفال, section فرهنگ معین); the print pagination cannot be checked in the OCR text (MON_part1/2 have only the running phrases 'سیاهرگ قیفال' and 'ورید قیفال', lines 20588 / 85716).\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"p. 259 s.v. cephalic vein\", \"stance\": \"contradicts\", \"note\": \"'qifāl, a word of uncertain origin, which was confused by the translators of Avicenna with Gk. κεφαλή'.\"},\n    {\"src\": \"MON\", \"where\": \"abadis, فرهنگ معین s.v. قیفال\", \"stance\": \"partial\", \"note\": \"'[ع.] رگِ بازو' — Arabic-origin tag, vein sense, no Greek etymology.\"},\n    {\"src\": \"AFM\", \"where\": \"grep 'قيفال' in AFM.txt / AFM_pages.txt\", \"stance\": \"silent\", \"note\": \"Addi Shir has no entry for قيفال (it is not a Persian loan in Arabic, so his book would not carry it).\"},\n    {\"src\": \"FVQ\", \"where\": \"grep 'qifal' in FVQ.txt\", \"stance\": \"silent\", \"note\": \"Jeffery has nothing (not a Qur'anic word).\"},\n    {\"src\": \"TAD\", \"where\": \"grep 'قيفال' in TAD_pages.txt / TAD.txt\", \"stance\": \"silent\", \"note\": \"'Unaysi's list of Arabic loanwords does not contain qīfāl, though it does contain كوفية (leaf 68).\"}\n  ]\n },\n {\n  \"id\": 3, \"lang\": \"Persian\", \"words\": \"qîfâl «قیفال»\", \"verdict\": \"plausible\",\n  \"derivation\": \"Persian قیفال is a straight technical borrowing of the Arabic anatomical term al-qīfāl into the Persian medical vocabulary (whence the compound ورید قیفالی 'the cephalic vein' printed in the chart's extra field, and MON's ورید قیفال). That Arabic→Persian step is certain — Mo'in tags the word [ع.] and Dehkhoda cites the phlebotomy formula 'فصد قیفال علتهای سر و چشم و بینی و کام و دهان [را سود دارد]'. Two things in the box are wrong, however: the gloss is not 'head' but 'the cephalic vein of the arm' (an adjective 'of the head' only in the ورید قیفالی compound), and the ultimate Greek source shown by the parent arrow is the disputed one of node #2 — Dehkhoda repeats it ('معرب و از یونانی کفاله بمعنی سر و رأس است'), Klein and Hyrtl reject it. Hence plausible rather than confirmed.\",\n  \"derivation_fa\": \"«قیفال» در فارسی وام‌واژه‌ای است اصطلاحی از عربیِ القیفال که از راهِ متونِ پزشکیِ دورهٔ اسلامی وارد فارسی شده؛ ترکیبِ «ورید قیفالی» که در همان جعبه چاپ شده گواهِ همین کاربردِ فنّی است و معین نیز آن را با نشانِ [ع.] آورده. این گامِ عربی ← فارسی بی‌گمان درست است و دهخدا شاهدِ «فصدِ قیفال علتهای سر و چشم و بینی و کام و دهان [را سود دارد]» را می‌آورد. اما دو نکته در جعبه نادرست است: نخست آنکه معنیِ واژه «سر» نیست بلکه «سیاهرگِ بازو» است؛ دوم آنکه خاستگاهِ یونانیِ آن — که فلشِ بالادست نشان می‌دهد و دهخدا نیز تکرارش می‌کند — همان ریشه‌شناسیِ محلِّ اختلافِ گرهِ پیشین است. از این رو حکم «با احتیاط پذیرفتنی».\",\n  \"sources\": [\"https://abadis.ir/fatofa/%D9%82%DB%8C%D9%81%D8%A7%D9%84/\"],\n  \"ref_check\": [\n    {\"ref\": \"MON:2769\", \"status\": \"partial\", \"note\": \"Mo'in s.v. قیفال: '[ع.] رگِ بازو' (abadis, فرهنگ معین). The word and the Arabic origin are Mo'in's; the gloss 'head' is not. Page 2769 could not be checked — the MON OCR files carry no page markers and only the running phrases سیاهرگ قیفال (MON_part1:20588) and ورید قیفال (MON_part2:85716).\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"MON\", \"where\": \"MON_part2.txt line 85716 (s.v. ورید)\", \"stance\": \"supports\", \"note\": \"'ورید قیفال: (پز.) نام ورید سطحی خارجی بازو که از انشعابات ورید میانی دست محسوب است' — Mo'in's own definition of the compound, i.e. the cephalic vein, not 'head'.\"},\n    {\"src\": \"BQT\", \"where\": \"grep 'قیفال' in BQT_v1/v2/v3/v4/v5_pages.txt\", \"stance\": \"silent\", \"note\": \"Borhān-e Qāṭeʿ has no قیفال entry (it is a medical, not a lexical-Persian, word).\"},\n    {\"src\": \"ARY\", \"where\": \"grep 'قیفال' in incoming/ARY/ARY_pages.txt\", \"stance\": \"silent\", \"note\": \"Aryanpur's dictionary of Indo-European roots of Persian does not list it.\"}\n  ]\n },\n {\n  \"id\": 4, \"lang\": \"Latin\", \"words\": \"cephalicus\", \"verdict\": \"disputed\",\n  \"derivation\": \"Latin cephalicus 'pertaining to the head' is a plain loan of Gk. κεφαλικός (from κεφαλή) and was already used in Latin medical writing; it does not come from Arabic, and the arrow #2→#4 as drawn is wrong. What does come from Arabic is only the anatomical phrase: Medieval Latin vena cephalica renders Arabic al-qifāl, the translator having taken the Arabic vein-name for the Greek adjective. Klein dates that phrase precisely — 'The word cephalic in its above sense appears first in a translation of Avicenna by Armengaud Blaise of Montpellier' (Armegandus Blasius de Montepessulano), printed 1564. So Latin cephalicus descends from the Greek node #1 directly; the Arabic word only supplied the referent 'vein', not the form. Etymonline s.v. cephalic gives the same chain (L. cephalicus < Gk. kephalikos) with no Arabic step.\",\n  \"derivation_fa\": \"لاتینیِ cephalicus «مربوط به سر» وام‌واژه‌ای است سرراست از یونانی κεφαλικός (از κεφαλή) و در متون پزشکیِ لاتین پیش از دورهٔ ترجمه‌های عربی هم به کار رفته است؛ بنابراین فلشِ «عربی ← لاتینی» که نورایی کشیده نادرست است. آنچه از عربی آمده تنها ترکیبِ اصطلاحیِ vena cephalica در لاتینِ سده‌های میانه است که برگردانِ «القیفال» است: مترجم نامِ عربیِ رگ را با صفتِ یونانی یکی گرفته. کلاین تاریخِ آن را هم می‌دهد: نخستین بار در ترجمهٔ قانونِ ابن‌سینا به قلمِ آرمنگو بلز مون‌پلیه‌ای (چاپ ۱۵۶۴). پس گرهِ لاتینی باید مستقیماً زیرِ گرهِ یونانی می‌نشست؛ ریشه‌شناسیِ آنلاینِ اتیمآنلاین نیز همین زنجیره را می‌دهد و هیچ گامِ عربی در آن نیست.\",\n  \"sources\": [\"https://www.etymonline.com/word/cephalic\"],\n  \"ref_check\": [\n    {\"ref\": \"KLN:259\", \"status\": \"contradicts\", \"note\": \"KLN_1966.txt line 6992 s.v. cephalic: 'F. céphalique, fr. L. cephalicus, fr. Gk. κεφαλικός, \\\"pertaining to the head\\\", fr. κεφαλή' — no Arabic. Line 6993 restricts the Arabic to the phrase 'vena cephalica'. Nourai's own reference therefore contradicts his arrow.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"p. 259 s.v. cephalic / cephalic vein\", \"stance\": \"contradicts\", \"note\": \"Two separate entries: the adjective from Greek, the vein-phrase from Arabic al-qifāl by confusion.\"},\n    {\"src\": \"LEW\", \"where\": \"grep 'cephalic' in LEW_1910.txt and LAT.txt\", \"stance\": \"silent\", \"note\": \"Neither Walde nor Ernout-Meillet carries cephalicus — it is a late Greek technical loan, outside the inherited Latin lexicon.\"},\n    {\"src\": \"AHD\", \"where\": \"s.v. ghebh-el-\", \"stance\": \"contradicts\", \"note\": \"Watkins files CEPHALIC under the Greek branch ('*khephel- in Greek kephalē … : CEPHALIC'), with no Arabic transmission.\"}\n  ]\n },\n {\n  \"id\": 5, \"lang\": \"English\", \"words\": \"cephalic\", \"verdict\": \"confirmed\",\n  \"derivation\": \"English cephalic is attested from the early 15th century, taken from Old/Middle French céphalique and directly from Latin cephalicus < Gk. κεφαλικός. Its specifically anatomical use, 'cephalic vein', enters English through the Avicenna translations described at node #4 (Klein: first in Armengaud Blaise's version). AHD/Watkins lists CEPHALIC, CEPHALO-, -CEPHALOUS, ENCEPHALO-, HYDROCEPHALUS under *ghebh-el-, so Nourai's 'AHD' reference is exact for this node; the Latin→English step itself is uncontroversial.\",\n  \"derivation_fa\": \"انگلیسیِ cephalic از آغازِ سدهٔ پانزدهم میلادی گواهی شده و از فرانسویِ céphalique و مستقیماً از لاتینیِ cephalicus (< یونانی κεφαλικός) گرفته شده است. کاربردِ پزشکیِ ویژهٔ آن، یعنی cephalic vein، از راهِ همان ترجمه‌های قانونِ ابن‌سیناست که در گرهِ پیشین گفته شد. واتکینز در پیوستِ ریشه‌های هندواروپاییِ فرهنگ AHD واژه‌های CEPHALIC و CEPHALO- و HYDROCEPHALUS را زیرِ *ghebh-el- آورده است؛ پس ارجاعِ نورایی به AHD دقیق است و این گام از زنجیره جای چون‌وچرا ندارد.\",\n  \"sources\": [\"https://www.etymonline.com/word/cephalic\"],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt line 510 s.v. ghebh-el-: '… in Greek kephalē, head: CEPHALIC, CEPHALO-, -CEPHALOUS'; and the index line 1342: 'CEPHALIC ghebh-el-'.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"p. 259 s.v. cephalic\", \"stance\": \"supports\", \"note\": \"'cephalic, adj., pertaining to the head. — F. céphalique, fr. L. cephalicus, fr. Gk. κεφαλικός.'\"},\n    {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt line 22898 s.v. brachistocephalic, and line 30048 'cephalic index'\", \"stance\": \"supports\", \"note\": \"Webster glosses the element as '(Gr. … kephalē, head)' throughout the cephal- family.\"}\n  ]\n },\n {\n  \"id\": 6, \"lang\": \"Italian\", \"words\": \"cuffia\", \"verdict\": \"disputed\",\n  \"derivation\": \"Italian cuffia (also scuffia) 'cap, coif, bonnet' continues Vulgar/Late Latin cofia, cofea, cuphia 'a cap', which is Germanic, not Greek: Klein s.v. coif derives VL. cofia (whence also It. cuffia, scuffia, Sp. cofia, escofia, OF coife > E coif) 'fr. OHG. kupphia, \\\"cap, coif\\\"', and Wiktionary the same, from Proto-West-Germanic *kuffju. Neither the geminate -ff- nor the u-vocalism can be got from κεφαλή, and no Greek *κουφία of this meaning exists. 'Unaysi (TAD 65) does print the claim Nourai reproduces, but his booklet is a popular list of foreign words in Arabic without phonological argument. The arrow Greek kephalē → Italian cuffia is therefore rejected by modern scholarship. Nourai's gloss ('headband, scarf') is also skewed: cuffia is a close-fitting cap, not a scarf — the 'scarf' sense has been read back into it from the Arabic word of node #7.\",\n  \"derivation_fa\": \"ایتالیاییِ cuffia (و گونهٔ scuffia) «کلاهک، کلاهِ چسبان» دنبالهٔ لاتینیِ عامیانه/متأخّرِ cofia, cofea, cuphia «کلاه» است و این خود وام‌واژه‌ای ژرمنی است، نه یونانی: کلاین ذیلِ coif آن را از آلمانی علیای باستان kupphia «کلاه» می‌گیرد و ویکی‌واژه از ژرمنیِ غربیِ آغازین *kuffju؛ از همین سرچشمه است فرانسویِ coife/coiffe و اسپانیاییِ cofia. نه همخوانِ مشدّدِ ff و نه واکهٔ u را می‌توان از kephalē بیرون آورد و در یونانی هم واژه‌ای به این معنی و به این شکل نیست. طوبیا العنیسی (TAD ص ۶۵) همان ادعای نورایی را دارد، ولی کتابِ او فهرستی است عامّه‌پسند از واژه‌های دخیل در عربی و استدلالِ آوایی ندارد. افزون بر این، معنیِ «سربند، شال» که نورایی داده درست نیست؛ cuffia کلاه است، و معنیِ «شال» از واژهٔ عربیِ گرهِ بعدی به آن بازتابانده شده. پژوهشِ امروزی این پیوند را رد می‌کند.\",\n  \"sources\": [W+\"cuffia\"],\n  \"ref_check\": [\n    {\"ref\": \"TAD:65\", \"status\": \"supports\", \"note\": \"TAD_pages.txt leaf 68 (printed p. ≈ 63-65): 'كوفة وكوفية … ايطالي [cuffia] معناه غطاء الرأس … من اليونانية [kephalē] معناه رأس' — 'Unaysi does derive the Arabic head-cloth from Italian cuffia and that in turn from Greek kephalē 'head', exactly Nourai's two arrows. The reference supports the chart; it is the reference itself that modern scholarship rejects.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 8158, s.v. coif\", \"stance\": \"contradicts\", \"note\": \"'ME. coif, coife, fr. OF. coife, coiffe (F. coiffe), fr. VL. cofia, cofea, cuphia, \\\"a cap\\\" (whence also It. cuffia, scuffia, Sp. cofia, escofia, of s.m.), fr. OHG. kupphia, \\\"cap, coif\\\".' Germanic, not Greek.\"},\n    {\"src\": \"LKT\", \"where\": \"LKT.txt no. 2171\", \"stance\": \"partial\", \"note\": \"'Tk. üsküflü \\\"Nachtmütze\\\" [… aus it. scuffia, cuffia]; hieraus russ. skuf'ja, bulg. skufa, serb. skufija …' — Lokotsch treats cuffia as the Romance source of the Balkan/Turkic forms and gives it no Greek ancestry.\"}\n  ]\n },\n {\n  \"id\": 7, \"lang\": \"Arabic\", \"words\": \"kŭfîyyah\", \"verdict\": \"disputed\",\n  \"derivation\": \"Arabic كوفية kūfiyya, the Arab men's square head-cloth held down by the ʿiqāl, is standardly explained as the nisba adjective of الكوفة al-Kūfa, the Iraqi garrison city — '(a cloth) of Kufa / in the Kufan style' (Wiktionary, with the same formation as kūfī 'Kufic' script, for which Pihan s.v. COUFIQUE gives 'de Koufat, ville de l'Irak Arabi'). Nourai follows 'Unaysi (TAD 65), who instead takes it from Italian cuffia; but that requires (a) the rejected Greek etymology of cuffia (node #6) and (b) an Italian→Arabic loan for a garment that is an inland Iraqi-Syrian, not a maritime-Mediterranean, item. Direction and source are both against Nourai here, so the node is disputed; only the 'scarf/head-cloth' gloss is right.\",\n  \"derivation_fa\": \"عربیِ «کوفیّه»، همان سرپوشِ چهارگوشِ مردانِ عرب که با «عقال» بر سر نگه داشته می‌شود، در ریشه‌شناسیِ پذیرفته صفتِ نسبیِ «الکوفة» است، یعنی «[پارچهٔ] کوفی، به شیوهٔ کوفه» — درست همان‌گونه که «کوفی» برای خطّ کوفی ساخته شده (ویکی‌واژه؛ پیهان نیز ذیلِ COUFIQUE آن را «از کوفه، شهری در عراقِ عرب» می‌داند). نورایی از طوبیا العنیسی پیروی کرده که آن را از ایتالیاییِ cuffia می‌گیرد؛ ولی این رأی هم به ریشه‌شناسیِ ردشدهٔ cuffia (گرهِ پیشین) نیاز دارد و هم وام‌گیریِ ایتالیایی ← عربی را برای پوششی می‌طلبد که کالای درون‌سرزمینیِ عراق و شام است نه کالای بندریِ مدیترانه‌ای. پس هم جهتِ وام‌گیری و هم سرچشمه محلِّ ایراد است و پژوهشِ امروزی نسبتِ «کوفه» را ترجیح می‌دهد؛ تنها معنیِ «شال/سرپوش» درست است.\",\n  \"sources\": [W+\"%D9%83%D9%88%D9%81%D9%8A%D8%A9\"],\n  \"ref_check\": [\n    {\"ref\": \"TAD:65\", \"status\": \"supports\", \"note\": \"TAD_pages.txt leaf 68: 'كوفة وكوفية … ايطالي cuffia معناه غطاء الرأس … من اليونانية kephalē معناه رأس'. 'Unaysi's page number is confirmed to within a leaf or two (86-leaf book, offset ≈ leaf − 4).\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"grep 'keffiyeh|kufiyah|kaffiyeh' in KLN_1966.txt\", \"stance\": \"silent\", \"note\": \"Klein has no entry for the word (it entered English only as a 20th-c. orientalism).\"},\n    {\"src\": \"PHN\", \"where\": \"PHN.txt line 3960 s.v. COUFIQUE / KOUFIQUE\", \"stance\": \"partial\", \"note\": \"'de Koufat (الكوفة), ville de l'Irak Arabi' — Pihan derives the kūfī family from the city name, the formation Wiktionary applies to kūfiyya; and his separate entry COIFFE/COUFFIN (line 3954) keeps the Arabic couffa 'basket' apart from it.\"},\n    {\"src\": \"AFM\", \"where\": \"grep in AFM.txt / AFM_pages.txt\", \"stance\": \"silent\", \"note\": \"Addi Shir does not list كوفية among the Persian loans in Arabic.\"}\n  ]\n },\n {\n  \"id\": 8, \"lang\": \"Persian\", \"words\": \"kŭfîyyeh «کوفیّه»\", \"verdict\": \"confirmed\",\n  \"derivation\": \"New Persian کوفیّه is an unaltered Arabic loan: Mo'in gives it as '[ع. کوفیة] چارقدی که مردان عرب بر سر گذارند و بندی مخصوص به نام عقال روی آن نهند', and Dehkhoda describes the square linen/silk/cotton cloth 'so that two corners fall on the shoulders and two on the forehead'. The Persian form keeps the Arabic gemination (shadda) and renders the tāʾ marbūṭa as -e, the normal treatment of Arabic feminines in Persian (cf. خلیفة > خلیفه). The Arabic→Persian arrow and the gloss are therefore right; only the further ancestry of the Arabic word (node #7) is disputed.\",\n  \"derivation_fa\": \"«کوفیّه» در فارسیِ نو وام‌واژه‌ای است دست‌نخورده از عربی: معین آن را با نشانِ [ع. کوفیة] و معنیِ «چارقدی که مردان عرب بر سر گذارند و بندی مخصوص به نام عقال روی آن نهند» آورده و دهخدا نیز همان پارچهٔ چهارگوشِ کتانی یا ابریشمی را وصف می‌کند. صورتِ فارسی تشدیدِ عربی را نگاه داشته و «تاء مربوطه» را — چنان‌که در فارسی معمول است (خلیفة > خلیفه) — به «ـه» بدل کرده است. پس گامِ عربی ← فارسی و معنیِ آن هر دو درست است؛ تنها خاستگاهِ خودِ واژهٔ عربی (گرهِ پیشین) محلّ اختلاف است.\",\n  \"sources\": [\"https://abadis.ir/fatofa/%DA%A9%D9%88%D9%81%DB%8C%D9%87/\"],\n  \"ref_check\": [\n    {\"ref\": \"MON:3127\", \"status\": \"partial\", \"note\": \"Mo'in does have the entry — '[ع. کوفیة] چارقدی که مردان عرب بر سر گذارند …' (abadis, فرهنگ معین s.v. کوفیه) — so the reference is real, but p. 3127 cannot be verified: the MON OCR files carry no page markers and a grep for 'کوفیه/کوفیّه' in MON_part1/2 returns nothing (the ک- section is not in the OCR'd portion).\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"MON\", \"where\": \"abadis, فرهنگ معین s.v. کوفیه\", \"stance\": \"supports\", \"note\": \"'[ع. کوفیة]' — Arabic-origin tag, exactly the arrow drawn.\"},\n    {\"src\": \"BQT\", \"where\": \"grep 'کوفیه' in BQT_v1..v5_pages.txt\", \"stance\": \"silent\", \"note\": \"Borhān-e Qāṭeʿ has no کوفیه entry.\"},\n    {\"src\": \"ARY\", \"where\": \"grep in incoming/ARY/ARY_pages.txt\", \"stance\": \"silent\", \"note\": \"Aryanpur (Indo-European roots of Persian) does not list it — consistent with a Semitic, not Iranian, word.\"}\n  ]\n },\n {\n  \"id\": 9, \"lang\": \"Germanic\", \"words\": \"gabl\", \"verdict\": \"confirmed\",\n  \"derivation\": \"Nourai's bare 'gabl' stands for Proto-Germanic *gablaz / *gablō 'top of a pitched roof; fork', the o-grade continuation of *gʰebʰ-el- (Watkins: 'Germanic *gablaz, top of a pitched roof'). Its attested reflexes are Gothic gibla 'gable, pinnacle', OHG gibil 'gable' beside gebal 'skull, head', MDu. ghevel, Du. gevel, G. Giebel, and — with the ablaut grade that matters here — Old Norse gafl 'gable end of a house, point of an island'. The 'top/head' semantics that Nourai glosses is exactly the pair Pokorny and Walde-Pokorny record ('Giebel; Kopf'), the gable being the head or vertex of the roof. The root→Germanic arrow is correct.\",\n  \"derivation_fa\": \"صورتِ کوتاهِ «gabl» که نورایی نوشته همان ژرمنیِ آغازینِ *gablaz / *gablō «نوکِ بامِ شیب‌دار؛ دوشاخه» است، یعنی گونهٔ o-دارِ *gʰebʰ-el- (واتکینز: «Germanic *gablaz, top of a pitched roof»). بازمانده‌های آن گوتی gibla «شیروانی، کنگره»، آلمانی علیای باستان gibil «شیروانی» در کنارِ gebal «کاسهٔ سر»، هلندی gevel و آلمانیِ Giebel است و — که برای این نمودار مهم است — نورسِ باستان gafl «کنارهٔ شیروانیِ خانه، دماغهٔ جزیره». همان جفتِ معناییِ «سر / نوکِ بام» که پوکورنی و والده-پوکورنی ثبت کرده‌اند («Giebel; Kopf») در معنیِ «بالا»یِ نورایی بازتاب یافته است. این فلش درست است.\",\n  \"sources\": [\"https://www.etymonline.com/word/gable\"],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt line 510: 'ghebh-el-. Head. 1. Germanic *gablaz, top of a pitched roof, in Old Norse gafl, gable: GABLE.'\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"POK_full.txt, Page(s): 423\", \"stance\": \"supports\", \"note\": \"'Gothic gibla \\\"gable, pinnacle\\\", changing through ablaut Old Norse gafl … Old High German gibil m. \\\"gable, pole of the earth\\\"; gibilla, gebal m.'\"},\n    {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 15635, s.v. gable\", \"stance\": \"supports\", \"note\": \"'ON. gafl, which is rel. to MDu. ghevel, Du. gevel, OHG. gibil, MHG. gibel, G. Giebel, Goth. gibla, \\\"gable\\\", OHG. gibilla, OS. gibillia, \\\"skull\\\" … for I.-E. *ghebh-l, whence also … Gk. κεφαλή, \\\"head\\\".'\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. I p. 571\", \"stance\": \"supports\", \"note\": \"'got. gibla „Giebel, Zinne\\\", ahd. gibil „Giebel, Pol\\\", gebal „Schädel, Kopf\\\", ablautend anord. gafl.'\"}\n  ]\n },\n {\n  \"id\": 10, \"lang\": \"English\", \"words\": \"gable\", \"verdict\": \"confirmed\",\n  \"derivation\": \"English gable is first recorded in the mid-14th century, but not as a direct native descendant of the Germanic word: ME gable was taken from Old French gable 'facade, front, gable', itself borrowed from Old Norse gafl by the Normans (Klein: 'ME., fr. OF. gable, fr. ON. gafl'; Etymonline the same). The native English cognate of *gablaz survives instead as OE gafol 'fork' (Klein, Skeat), and Skeat notes the parallel MHG gabel(e) 'fork' beside gibel 'gable'. So Nourai's compression Germanic→English is right in substance — AHD too routes GABLE through Old Norse gafl — but it hides one Romance relay; the node itself is sound.\",\n  \"derivation_fa\": \"انگلیسیِ gable از میانهٔ سدهٔ چهاردهم گواهی شده، امّا نه به‌عنوانِ بازماندهٔ بومیِ واژهٔ ژرمنی: انگلیسیِ میانه آن را از فرانسویِ باستان gable «نما، پیشانیِ ساختمان، شیروانی» گرفته و فرانسویِ باستان خود آن را از نورسِ باستان gafl وام گرفته بود (کلاین: «ME., fr. OF. gable, fr. ON. gafl»؛ اتیم‌آنلاین نیز همین). هم‌ریشهٔ بومیِ انگلیسیِ *gablaz به‌جای آن در انگلیسیِ باستان gafol «دوشاخه» بازمانده است. پس فشرده‌سازیِ نورایی («ژرمنی ← انگلیسی») در جوهرِ مطلب درست است — واتکینز هم gable را از راهِ gafl می‌آورد — و تنها یک حلقهٔ فرانسوی را نانوشته گذاشته است.\",\n  \"sources\": [\"https://www.etymonline.com/word/gable\"],\n  \"ref_check\": [\n    {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The node carries no reference in the book; verified instead against AHD (which lists GABLE under ghebh-el-), Klein p. 611 s.v. gable and Etymonline.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 15635, s.v. gable\", \"stance\": \"supports\", \"note\": \"'gable, n., the triangular upper part of a wall at the end of a ridged roof. — ME., fr. OF. gable, fr. ON. gafl … for I.-E. *ghebh-l.' Adds the Old French relay Nourai omits.\"},\n    {\"src\": \"SKT\", \"where\": \"SKT.txt line 7299 (s.v. gable)\", \"stance\": \"supports\", \"note\": \"'M.E. gable. — O.F. gable; Low L. gabulum. — M.H.G. gabele, G. Gabel, n. fork; gibel (G. Giebel), a gable. + Icel. gafl, Dan. gavl, Swed. gafvel, a gable … Goth. gibla, a gable.' (Skeat adds a possible Celtic source, now not followed.)\"},\n    {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt line 1550, index\", \"stance\": \"supports\", \"note\": \"'GABLE ghebh-el-'.\"}\n  ]\n }\n]\n\ne1 = {\n \"entry\": 1,\n \"root\": \"Ghěi, Ğhî, Ğhiâ\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *ǵʰeh₁(i)- / *ǵʰi- 'to gape, yawn' (Pokorny's ghē-2, ghǝ- and ghēi- : ghī-; Watkins *ghēi-; Etymonline *ghieh-)\",\n \"note\": \"Pokorny 419-422 heads the entry 'Root/lemma: ghē-2, ghǝ- and ghēi- : ghī-. Meaning: to gape, yawn', with the note 'onomatopoeic for the yawning sound (in addition the further formation stem ghii-ā)' — so all three of Nourai's variants (Ghěi, Ǧhî, Ǧhiâ) are Pokorny's own, and the starting page 419 is exact. Walde-Pokorny I 548 has the same lemma 'ghei- : ghī- … „gähnen, klaffen\\\"; schallmalend für den Gähnlaut'. Watkins/AHD gives 'ghēi-. To yawn, gape. Contracted from *gheəi-. [Pok. 2. ghē- 419.]' The velar is palatal (*ǵʰ), as Lat. hiāre, Lith. žióti, OCS zijati show; Mann accordingly writes ǵhiiaiō. Root, label and gloss all correct. The one weak link on this chart is the Persian node, which rests on Mann alone.\",\n \"note_fa\": \"ریشهٔ هندواروپاییِ آغازینِ *ǵʰeh₁(i)- / *ǵʰi- «دهان گشودن، خمیازه کشیدن» ریشه‌ای است پذیرفته و آوانمود (onomatopoeic): پوکورنی در صص ۴۱۹–۴۲۲ سرواژه را چنین می‌آورد: «ghē-2, ghǝ- and ghēi- : ghī- — to gape, yawn» و می‌افزاید که ساختِ آن تقلیدِ آوایِ خمیازه است و ستاکِ گسترش‌یافتهٔ ghii-ā نیز از همان است؛ پس هر سه گونه‌ای که نورایی نوشته از خودِ پوکورنی است و شمارهٔ صفحه هم دقیق است. والده-پوکورنی (جلد ۱، ص ۵۴۸) همان را با عبارتِ «gähnen, klaffen؛ schallmalend für den Gähnlaut» دارد و واتکینز نیز ذیلِ ghēi-. همخوانِ آغازینِ آن کامی است (*ǵʰ)، چنان‌که لاتینیِ hiāre و لیتوانیاییِ žióti و اسلاویِ کهنِ کلیسایی zijati گواهی می‌دهند. تنها حلقهٔ سستِ این نمودار گرهِ فارسی است که فقط بر مانْ (فرهنگِ تطبیقیِ هندواروپاییِ اِس. ای. مان) تکیه دارد.\",\n \"sources\": [\"https://www.etymonline.com/word/yawn\"],\n \"ref_check\": [\n   {\"ref\": \"POK:419\", \"status\": \"supports\",\n    \"note\": \"POK_full.txt block 'Root / lemma: ghē-2, ghǝ- and ghēi- : ghī- | Meaning: to gape, yawn | Note: onomatopoeic for the yawning sound … Page(s): 419-422'. The Material section contains, in order, all four branches Nourai draws: Gk. χάσκω / χάσμα; OE ginian, gionian ('but engl. yawn for *yone from Old English gionian'); ON gap, gapa; ON geispa ('Middle English gaspen').\"},\n   {\"ref\": \"IEC:418\", \"status\": \"supports\",\n    \"note\": \"IEC.txt line 6041, leaf 241 (which carries the printed page number 417, so the entry falls on p. 417/418): 'ǵhiiaiō (ghiā-, ǵhā-, ǵhi-) \\\"gape, yawn\\\" (onomatopoeic). WP I, 548. Per. fa-žīdan, cpd. id.; Gk. cf. kháos; Lat. hio, hiāre; OHG gēn beside MHG giegen \\\"yawn\\\"…'. Nourai's page number is right and this is also the sole source for his Persian node.\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. I leaf 556 = p. 548\", \"stance\": \"supports\",\n    \"note\": \"'ghei- : ghī- (dazu der weitergebildete Stamm ghii-ā …) „gähnen, klaffen\\\"; schallmalend für den Gähnlaut.' Confirms both the form and Pokorny's onomatopoeic note; lists no Iranian reflex.\"},\n   {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt line 504, s.v. ghēi-\", \"stance\": \"supports\",\n    \"note\": \"'ghēi-. To yawn, gape. Contracted from *gheəi-. 1. … *ghi-n-ə- in Germanic *ginōn in Old English ginan, ginian, geonian, to yawn: YAWN … 2. *ghə-smn̥ in Greek khasma …: CHASM … 4. Labial extensions: a. Old Norse gap, chasm: GAP; b. Old Norse gapa, to open the mouth: GAPE; c. Old Norse geispa, to yawn: GASP. [Pok. 2. ghē- 419.]'\"},\n   {\"src\": \"SYN\", \"where\": \"SYN.txt § 4.52 YAWN, GAPE (lines 6737-6748)\", \"stance\": \"supports\",\n    \"note\": \"Buck's list for 'yawn, gape' is the same set — 'ON gina, gapa; OE ginan, ginian, ganian; ME gone, yane, gape; NE yawn, gape; OHG ginēn, gien, giwen; NHG gähnen, gaffen; Lat. hiāre; Lith. žiovauti; ChSl. zinǫti, zijati; Skt. jr̥mbh-' — and carries no New Persian member.\"}\n ],\n \"nodes\": []\n}\n\ne1[\"nodes\"] = [\n {\n  \"id\": 1, \"lang\": \"Persian\", \"words\": \"fâž «فاژ ، فاژه»; fâžîdan «فاژیدن»\", \"verdict\": \"plausible\",\n  \"derivation\": \"The Persian words are genuine and old: Asadi Tusi's Loghat-e Fors glosses فاژ as 'دهن‌دره' (yawn) and quotes the very verse the chart prints, attributing it to Labībī — 'اگر ندانی بیندیش تا چگونه بود / که سبزه‌خورده بفاژد بهارگه اشتر' (FRS.txt line 7546, leaf 197, printed p. 178; Mo'in's footnote in Borhān-e Qāṭeʿ gives the same line with the variant سیر خورده and the same attribution, 'لبیبی، فرهنگ نظام'). Borhān-e Qāṭeʿ has فاژ, فاژه and فاژیدن as separate entries, with Mo'in's footnote deriving the verb simply as 'از: فاژ + ـیدن (پسوند مصدری)' and cross-referring to the variants هاژ / هاژیدن. What is not secure is the IE derivation. Nourai's only authority is Mann, who does list 'Per. fa-žīdan' under ǵhiiaiō 'gape, yawn' but marks it 'cpd.', i.e. he analyses fā- as a prefix (presumably *fra-) rather than deriving fāž directly from the root; no Iranian specialist confirms it. Pokorny, Walde-Pokorny, Horn, Hübschmann, Bartholomae and Cheung list no Iranian reflex at all — Cheung's yawn-roots are *jās (which he calls 'exclusively Iranian') and *zamb-, neither of which yields f-. A PIE palatal *ǵʰ gives Iranian z-, never f-, so the form cannot be a straight inheritance; and since the root is itself onomatopoeic (Pokorny: 'schallmalend für den Gähnlaut'), an independent Persian sound-imitation is at least as likely as inheritance. Plausible, on Mann's authority alone.\",\n  \"derivation_fa\": \"خودِ واژه‌ها اصیل و کهن‌اند: اسدی طوسی در لغتِ فرس «فاژ» را «دهن‌دره» معنی کرده و همان بیتی را می‌آورد که در نمودار چاپ شده و آن را به لبیبی نسبت می‌دهد — «اگر ندانی بیندیش تا چگونه بود / که سبزه‌خورده بفاژد بهارگه اشتر»؛ معین نیز در حاشیهٔ برهان قاطع همین بیت را با ضبطِ «سیر خورده» و همان انتساب به لبیبی («فرهنگ نظام») نقل کرده است. برهانِ قاطع سه مدخلِ فاژ، فاژه و فاژیدن دارد و معین در پانوشت تنها می‌نویسد «از: فاژ + ـیدن (پسوند مصدری)» و به گونه‌های هاژ/هاژیدن ارجاع می‌دهد؛ یعنی ریشه‌شناسیِ کهن‌تری نمی‌دهد. اشکال در پیوندِ هندواروپایی است: تنها پشتوانهٔ نورایی مانْ است که «Per. fa-žīdan» را ذیلِ ǵhiiaiō آورده، امّا آن را «مرکّب» (cpd.) نشانه‌گذاری کرده، یعنی fā- را پیشوند (احتمالاً *fra-) گرفته است نه بخشی از ریشه. پوکورنی، والده-پوکورنی، هرن، هوبشمان، بارتولومه و چونگ هیچ بازماندهٔ ایرانی برای این ریشه نمی‌آورند؛ ریشه‌های «خمیازه» نزدِ چونگ *jās (به گفتهٔ خودِ او «منحصراً ایرانی») و *zamb- است که هیچ‌کدام به f نمی‌رسد. از سوی دیگر *ǵʰ کامیِ هندواروپایی در ایرانی به z بدل می‌شود، نه به f؛ پس این صورت نمی‌تواند میراثِ مستقیمِ ریشه باشد. و چون خودِ ریشه آوانمود است، ساختِ مستقلِ آوانمود در فارسی هم به همان اندازه محتمل است. حکم: با احتیاط پذیرفتنی، و آن هم تنها به اعتبارِ مانْ.\",\n  \"sources\": [],\n  \"ref_check\": [\n   {\"ref\": \"IEC:418\", \"status\": \"supports\", \"note\": \"IEC.txt line 6041 (leaf 241, printed p. 417/418): 'ǵhiiaiō (ghiā-, ǵhā-, ǵhi-) \\\"gape, yawn\\\" (onomatopoeic). WP I, 548. Per. fa-žīdan, cpd. id.' — Mann does make Nourai's claim, but hyphenates fa-žīdan as a compound, i.e. he does not derive fāž itself from the root.\"},\n   {\"ref\": \"MON:2470\", \"status\": \"partial\", \"note\": \"Mo'in has the word — MON_part2.txt line 4218 reads (OCR) 'فاژ … |ـ فاژه] (اِ.) خمیازه', i.e. 'فاژ [= فاژه] (n.) yawn' — but he gives no etymology and the page number cannot be checked (no page markers in the MON OCR).\"},\n   {\"ref\": \"FRS:120\", \"status\": \"supports\", \"note\": \"Content confirmed, page differs by edition: FRS.txt line 7546 (FRS_pages.txt leaf 197, printed p. 178 of the Eqbal 1319 edition): 'دهن دره بود … لبیبی گفت: اگر ندانی بیندیش تا چگونه بود / که سبزه‌خورده بفاژد بهارگه اشتر'. Nourai cites the 1365 Kharazmi edition, whose pagination differs.\"}\n  ],\n  \"consulted\": [\n   {\"src\": \"BQT\", \"where\": \"incoming/BQT/BQT_v3_pages.txt [pdf page 227-228], s.vv. فاژ، فاژه، فاژیدن\", \"stance\": \"partial\", \"note\": \"'فاژ — بسکون زای فارسی، بمعنی دهن‌دره است که خمیازه باشد'؛ 'فاژه — بمعنی اول فاژ است که خمیازه باشد'؛ 'فاژیدن — بمعنی خمیازه کشیدن باشد', with Mo'in's footnote '۱ - از: فاژ (ه.م.) + یدن (پسوند مصدری)' and the Labībī verse. Confirms the words and the verse, gives no Indo-European etymology.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"CHEUNG.txt, roots *jās (line 14815) and *zamb¹ (line 29921)\", \"stance\": \"silent\", \"note\": \"Cheung's two 'to yawn' roots have no New Persian fāž; of *jās he says 'The root *jās is exclusively Iranian', and *zamb¹ gives Oss. zembyn, Wa. zeumb-, not f-.\"},\n   {\"src\": \"HRN\", \"where\": \"grep 'fāž|fâz|gähnen' in HRN.txt\", \"stance\": \"silent\", \"note\": \"Horn's Grundriss has no entry for the word.\"},\n   {\"src\": \"HUB\", \"where\": \"grep 'fāž|gähnen' in HUB.txt\", \"stance\": \"silent\", \"note\": \"Hübschmann's Persische Studien has nothing.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I pp. 548-551 (leaves 556-559)\", \"stance\": \"silent\", \"note\": \"The whole ghei- : ghī- entry lists no Iranian form (a scan for 'np.' across the entry returns none).\"},\n   {\"src\": \"ARY\", \"where\": \"grep 'فاژ' in incoming/ARY/ARY_pages.txt\", \"stance\": \"silent\", \"note\": \"Aryanpur's dictionary of the Indo-European roots of Persian does not carry فاژ — notable, since this is exactly the kind of word it collects.\"}\n  ]\n },\n {\n  \"id\": 2, \"lang\": \"Germanic\", \"words\": \"ginôn\", \"verdict\": \"confirmed\",\n  \"derivation\": \"Proto-Germanic *ginōn / *ginēn 'to gape, yawn' continues the nasal present *ǵʰi-n- of the root (the same formation as OCS zinǫti 'to yawn' and ON gína), with the Germanic ō-/ē-verb suffix. Watkins gives it in so many words: 'nasalized form *ghi-n-ə- in Germanic *ginōn'. Its reflexes are OHG ginēn, MHG ginen/genen > NHG gähnen, ON gína, and the Old English forms of node #3. Nourai's 'ginôn' is exactly Watkins's reconstruction, and AHD:1517 is the right place in the 1976 appendix (the root ghēi- stands with the other gh- roots there).\",\n  \"derivation_fa\": \"ژرمنیِ آغازینِ *ginōn / *ginēn «دهان گشودن، خمیازه کشیدن» دنبالهٔ ستاکِ حالِ خیشومیِ *ǵʰi-n- از همان ریشه است — همان ساختی که در اسلاویِ کهنِ کلیسایی zinǫti و نورسِ باستان gína دیده می‌شود — با پسوندِ فعلیِ ō/ē در ژرمنی. واتکینز عیناً می‌نویسد: «nasalized form *ghi-n-ə- in Germanic *ginōn». بازمانده‌های آن آلمانی علیای باستان ginēn، آلمانی علیای میانه ginen/genen و آلمانیِ امروز gähnen است. صورتی که نورایی نوشته دقیقاً بازسازیِ واتکینز است و ارجاعِ AHD:1517 نیز درست می‌نماید.\",\n  \"sources\": [\"https://www.etymonline.com/word/yawn\"],\n  \"ref_check\": [\n   {\"ref\": \"AHD:1517\", \"status\": \"supports\", \"note\": \"The 1976 appendix page cannot be opened online, but the identical entry in Watkins 1985 (AHD_watkins1985.txt line 504) reads 'a. nasalized form *ghi-n-ə- in Germanic *ginōn in Old English ginan, ginian, geonian, to yawn: YAWN'. Nourai's form and gloss are Watkins's.\"}\n  ],\n  \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"POK_full.txt, ghē-2 entry, Page(s) 419-422\", \"stance\": \"supports\", \"note\": \"'n-present and related nouns: … Old Icelandic gína, Old High German ginēn, Middle High German ginen, genen, Modern High German gähnen = Old English ginian, gionian \\\"be far open\\\" … Old Church Slavic zinǫ, -ǫti (*ghīnō) \\\"yawn, gape\\\".'\"},\n   {\"src\": \"SYN\", \"where\": \"SYN.txt § 4.52\", \"stance\": \"supports\", \"note\": \"Buck lists 'OHG ginēn, gien, giwen; MHG ginen, geinen, gewen; NHG gähnen' as the Germanic members of the group.\"}\n  ]\n },\n {\n  \"id\": 3, \"lang\": \"Old English\", \"words\": \"geonian\", \"verdict\": \"confirmed\",\n  \"derivation\": \"OE geonian (also gionian, beside ginian, gānian) 'to yawn, gape' is the West Saxon variant of *ginian with back-mutation/breaking of the stem vowel before the back vowel of the ending (i > io/eo), a regular OE development; the g- before a front vowel was already palatalised to /j/, which is why the word is often written geonian and gives ME yone-/yane-. Pokorny cites the pair explicitly — 'Old English ginian, gionian \\\"be far open\\\"' — and Watkins the triplet 'Old English ginan, ginian, geonian'. Nourai's form and gloss are right and the Germanic→OE arrow is trivially correct.\",\n  \"derivation_fa\": \"انگلیسیِ باستان geonian (و gionian، در کنارِ ginian و gānian) «خمیازه کشیدن» گونهٔ وِسِکسیِ *ginian است با شکستِ واکه/دگرگونیِ پسین پیش از واکهٔ پسینِ پایانه (i > io/eo) که در انگلیسیِ باستان قاعده است؛ g آغازین نیز پیش از واکهٔ پیشین کامی و به /j/ بدل شده بود، و همین است که املای geonian را پدید آورده و در انگلیسیِ میانه به yone-/yane- رسیده است. پوکورنی همین جفت را می‌آورد («Old English ginian, gionian») و واتکینز هر سه صورت را. صورت و معنیِ گرهِ نورایی درست است و پیوندِ ژرمنی ← انگلیسیِ باستان بدیهی است.\",\n  \"sources\": [\"https://www.etymonline.com/word/yawn\"],\n  \"ref_check\": [\n   {\"ref\": \"AHD:1517\", \"status\": \"supports\", \"note\": \"Watkins 1985 (line 504): 'Germanic *ginōn in Old English ginan, ginian, geonian, to yawn: YAWN'.\"}\n  ],\n  \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"POK_full.txt, ghē-2 entry\", \"stance\": \"supports\", \"note\": \"'Old High German ginēn … = Old English ginian, gionian \\\"be far open\\\" … but engl. yawn \\\"yawn\\\" for *yone from Old English gionian.'\"},\n   {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.v. yawn (checked via the same root family, cp. gape/gasp entries)\", \"stance\": \"partial\", \"note\": \"Klein's yawn entry could not be isolated in the OCR (the y- section is heavily run together), but his gape and gasp entries (lines 15787, 15830) place the Norse and English members together in the same group.\"},\n   {\"src\": \"SYN\", \"where\": \"SYN.txt § 4.52\", \"stance\": \"supports\", \"note\": \"'OE ginan, ginian, ganian; ME gone, yane, gape; NE yawn, gape'.\"}\n  ]\n },\n {\n  \"id\": 4, \"lang\": \"English\", \"words\": \"yawn\", \"verdict\": \"confirmed\",\n  \"derivation\": \"English yawn is attested from c. 1300 in the sense 'to open the mouth wide', from OE ginian/gionian (node #3); by the mid-15th century it is specialised to the involuntary drowsy yawn, and the modern spelling with -w- settles in the 16th century (the earlier ME forms are yone, yane). Pokorny notes the irregularity himself: 'engl. yawn \\\"yawn\\\" for *yone from Old English gionian' — the -n of ganian and the -w- of the later spelling have crossed. The noun follows about 1690. Chain uncontroversial.\",\n  \"derivation_fa\": \"انگلیسیِ yawn از حدودِ سالِ ۱۳۰۰ میلادی به معنیِ «دهان را گشودن» گواهی شده و از انگلیسیِ باستان ginian/gionian (گرهِ پیشین) می‌آید؛ تا میانهٔ سدهٔ پانزدهم معنیِ ویژهٔ «خمیازهٔ ناخواسته از خواب‌آلودگی» را می‌گیرد و املای امروزی با w در سدهٔ شانزدهم استوار می‌شود (صورت‌های کهن‌ترِ انگلیسیِ میانه yone و yane است). پوکورنی خود به این بی‌قاعدگی اشاره می‌کند: «engl. yawn for *yone from Old English gionian». اسمِ آن نیز از حدودِ ۱۶۹۰ به کار رفته است. این زنجیره جای بحث ندارد.\",\n  \"sources\": [\"https://www.etymonline.com/word/yawn\"],\n  \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt line 504 lists YAWN as the English derivative of *ghi-n-ə- / Germanic *ginōn.\"}\n  ],\n  \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"POK_full.txt, ghē-2 entry\", \"stance\": \"supports\", \"note\": \"'but engl. yawn \\\"yawn\\\" for *yone from Old English gionian.'\"},\n   {\"src\": \"SYN\", \"where\": \"SYN.txt § 4.52 YAWN, GAPE\", \"stance\": \"supports\", \"note\": \"'ME gone, yane, gape; NE yawn, gape' in the same column as OE ginan, ginian, ganian.\"}\n  ]\n },\n {\n  \"id\": 5, \"lang\": \"Greek\", \"words\": \"khasma\", \"verdict\": \"confirmed\",\n  \"derivation\": \"Gk. χάσμα 'yawning hollow, gulf, chasm' is a neuter -μα noun built on the zero grade of the root, *ǵʰh₂-s-mn̥ (Watkins: 'Suffixed variant form *ghə-smn̥ in Greek khasma'), beside the sk-present χάσκω 'I yawn, gape' (*ǵʰh₂-sḱ-ō) which supplies the present stem of χαίνω. Pokorny lists both on p. 419: 'Gr. χάσκω (ghǝ-skō) \\\"yawn, gape\\\" … χάσμα \\\"gaping mouth\\\"'. The same root also gives χάος, whence chaos, which is why chasm and chaos are doublets in the family. Nourai's form, language and gloss are all right.\",\n  \"derivation_fa\": \"یونانیِ χάσμα «شکافِ دهان‌گشوده، مغاک» اسمی است خنثی با پسوندِ -μα بر پایهٔ درجهٔ صفرِ ریشه، یعنی *ǵʰh₂-s-mn̥ (واتکینز: «Suffixed variant form *ghə-smn̥ in Greek khasma»)، در کنارِ ستاکِ حالِ sk-دارِ χάσκω «دهان می‌گشایم، خمیازه می‌کشم» (*ǵʰh₂-sḱ-ō) که ستاکِ حالِ χαίνω را نیز فراهم می‌کند. پوکورنی هر دو را در ص ۴۱۹ آورده است. از همین ریشه χάος (khaos) نیز هست، و به همین سبب chasm و chaos در انگلیسی دوگانه (doublet) به شمار می‌آیند. صورت، زبان و معنیِ گرهِ نورایی درست است.\",\n  \"sources\": [\"https://www.etymonline.com/word/chasm\"],\n  \"ref_check\": [\n   {\"ref\": \"AHD:1517\", \"status\": \"supports\", \"note\": \"Watkins 1985 line 504: '2. Suffixed variant form *ghə-smn̥ in Greek khasma, yawning gulf, chasm: CHASM.'\"}\n  ],\n  \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"POK_full.txt, ghē-2 entry, Page(s) 419-422\", \"stache\": None, \"stance\": \"supports\", \"note\": \"'Gr. χάσκω (ghǝ-skō) \\\"yawn, gape\\\" (only present and Impf.; later replaced by χαίνω) … χάσμα \\\"gaping mouth\\\".'\"},\n   {\"src\": \"IEC\", \"where\": \"IEC.txt line 6047, s.v. ghiiatos / and line 6041 ǵhiiaiō\", \"stance\": \"supports\", \"note\": \"Mann files 'Gk. khásma' under ghiiadmn- 'open jaws, space, chasm' (line 6041 area: 'ghiiadmn- \\\"open jaws, space, chasm\\\" Gk. khásma'), i.e. the same root.\"},\n   {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 7259, s.v. chasm\", \"stance\": \"supports\", \"note\": \"'L. chasma, fr. Gk. χάσμα, \\\"a yawning hollow, gulf\\\", which is rel. to χαίνειν, \\\"to yawn, gape\\\". See chaos.'\"}\n  ]\n },\n {\n  \"id\": 6, \"lang\": \"English\", \"words\": \"chasm\", \"verdict\": \"confirmed\",\n  \"derivation\": \"English chasm is first recorded in the 1590s, borrowed from Latin chasma (itself the Greek word taken over unchanged) rather than straight from Greek; 17th-century English writers still often spell it chasma. The figurative sense 'a wide breach of any kind' follows in the 1640s. Nourai's Greek→English arrow is therefore right in substance but omits the Latin relay through which learned Greek words of this period regularly entered English. AHD lists CHASM under the root, matching Nourai's 'AHD' reference.\",\n  \"derivation_fa\": \"انگلیسیِ chasm نخستین بار در دههٔ ۱۵۹۰ گواهی شده و نه مستقیم از یونانی بلکه از لاتینیِ chasma (که خود همان واژهٔ یونانیِ دست‌نخورده است) وام گرفته شده؛ نویسندگانِ انگلیسیِ سدهٔ هفدهم هنوز آن را بارها chasma می‌نوشتند. معنیِ مجازیِ «شکافِ ژرف میانِ دو چیز» از دههٔ ۱۶۴۰ پیدا می‌شود. پس فلشِ «یونانی ← انگلیسی» در جوهر درست است، امّا حلقهٔ لاتینی را — که در آن دوره راهِ معمولِ ورودِ واژه‌های عالمانهٔ یونانی به انگلیسی بود — نانوشته گذاشته است. واتکینز نیز CHASM را ذیلِ همین ریشه آورده، پس ارجاعِ AHD درست است.\",\n  \"sources\": [\"https://www.etymonline.com/word/chasm\"],\n  \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt line 504: '… in Greek khasma, yawning gulf, chasm: CHASM.'\"}\n  ],\n  \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 7259, s.v. chasm\", \"stance\": \"supports\", \"note\": \"'chasm, n., a deep crack in the earth; abyss. — L. chasma, fr. Gk. χάσμα' — Klein makes the Latin relay explicit.\"},\n   {\"src\": \"POK\", \"where\": \"POK_full.txt, ghē-2 entry\", \"stance\": \"supports\", \"note\": \"Greek χάσμα is listed as the root's Greek noun; the English word is a learned borrowing of it.\"}\n  ]\n },\n {\n  \"id\": 7, \"lang\": \"Old Norse\", \"words\": \"gap; gapa; geispa\", \"verdict\": \"confirmed\",\n  \"derivation\": \"All three Old Norse words belong to the labial extensions of the root that Watkins groups as '4. Labial extensions': gap n. 'wide aperture, hole, chasm' and gapa 'to open the mouth, cry' go back to Pokorny's *ghəb- (Pokorny p. 421: '*ghəb-: Old Icelandic gap \\\"wide aperture, hole, chaos; shout\\\", gapa \\\"open the mouth, cry\\\"', beside OE gapian, MHG/NHG gaffen); geispa 'to gasp, struggle for breath, yawn' Pokorny puts under the ghei-b-/ghei-s- extensions, explaining it as '*gaipsōn (through amalgamation from *gaip- and *gais-)', and Klein independently as 'formed by metathesis fr. *geip-sa … rel. to ON. gapa'. Nourai's three forms and glosses are accurate. One caveat: Klein regards the ultimate origin of the gap/gapa group as unknown ('The ultimate origin of these words is unknown', s.v. gape), so the attachment of the labial extensions to *ǵʰeh₁i- is Pokorny's and Watkins's, not universally held.\",\n  \"derivation_fa\": \"هر سه واژهٔ نورسِ باستان به گسترش‌های لبیِ همین ریشه بازمی‌گردند که واتکینز آن‌ها را زیرِ «Labial extensions» گرد آورده است: gap «سوراخِ گشاد، مغاک» و gapa «دهان گشودن، بانگ زدن» از *ghəb- پوکورنی (ص ۴۲۱)، در کنارِ انگلیسیِ باستان gapian و آلمانیِ gaffen؛ و geispa «به‌سختی نفس کشیدن، خمیازه کشیدن» را پوکورنی ذیلِ گسترش‌های ghei-b-/ghei-s- می‌آورد و آن را *gaipsōn می‌داند، یعنی آمیزهٔ *gaip- و *gais-، در حالی که کلاین آن را با قلب (metathesis) از *geip-sa می‌گیرد و به gapa می‌پیوندد. صورت‌ها و معناهایی که نورایی داده درست است. تنها نکتهٔ احتیاطی: کلاین ذیلِ gape خاستگاهِ نهاییِ خوشهٔ gap/gapa را ناشناخته می‌داند؛ پس پیوستنِ این گسترش‌های لبی به ریشه رأیِ پوکورنی و واتکینز است، نه رأیِ همگان.\",\n  \"sources\": [\"https://www.etymonline.com/word/gasp\"],\n  \"ref_check\": [\n   {\"ref\": \"AHD:1517\", \"status\": \"supports\", \"note\": \"Watkins 1985 line 504: '4. Labial extensions: a. Old Norse gap, chasm: GAP; b. Old Norse gapa, to open the mouth: GAPE; c. Old Norse geispa, to yawn: GASP.' Exactly Nourai's three words with his glosses.\"}\n  ],\n  \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"POK_full.txt, ghē-2 entry, Page(s) 419-422\", \"stance\": \"supports\", \"note\": \"'*ghəb-: Old Icelandic gap \\\"wide aperture, hole, chaos; shout, call, scream\\\", gapa \\\"open the mouth, cry\\\"'; and 'Old Icelandic geispa \\\"struggle for breath\\\", Middle English gaspen < Old English *gaspian, probably from *gaipsōn (through amalgamation from *gaip- and *gais-)'.\"},\n   {\"src\": \"KLN\", \"where\": \"KLN_1966.txt lines 15786, 15787, 15830 (gap, gape, gasp)\", \"stance\": \"partial\", \"note\": \"Klein has the Norse forms and links them to each other ('ON. geispa is prob. formed by metathesis fr. *geip-sa and is rel. to ON. gapa') but says of the group 'The ultimate origin of these words is unknown' — he does not attach them to the IE root.\"},\n   {\"src\": \"SYN\", \"where\": \"SYN.txt § 4.52\", \"stance\": \"supports\", \"note\": \"'Here prob. also ON, Sw. gapa, Dan. gabe (ME, NE gape fr. Norse), Du. gapen' — Buck too files the gap-group with the yawn root, with 'prob.'\"}\n  ]\n },\n {\n  \"id\": 8, \"lang\": \"English\", \"words\": \"gap, gape, gasp\", \"verdict\": \"confirmed\",\n  \"derivation\": \"All three English words are Norse loans of the Middle English period, taken in from the Danelaw dialects: gap n. (early 14c.) 'an opening in a wall or hedge' from ON gap 'chasm, empty space'; gape v. (c. 1200) from ON gapa 'to gape, open the mouth wide'; gasp v. (late 14c., ME gaispen, gaspen 'to yawn') from ON geispa 'to yawn', with the Scandinavian cognates Swed. gaspa, Dan. gispe. Klein gives all three with these Norse etyma; Skeat, s.v. gap, likewise 'M.E. gappe. — Icel. and Swed. gap, a gap, abyss'. AHD lists GAP, GAPE and GASP under the root, matching Nourai's reference. Note the semantic shift in gasp from 'yawn' to 'catch the breath convulsively', already complete by the 16th century ('last gasp', 1570s).\",\n  \"derivation_fa\": \"هر سه واژهٔ انگلیسی وام‌واژه‌هایی نورسی‌اند که در دورهٔ انگلیسیِ میانه از گویش‌های دِین‌لا (Danelaw) گرفته شده‌اند: gap (اسم، اوایلِ سدهٔ چهاردهم) «رخنه در دیوار یا پرچین» از نورسِ باستان gap «مغاک، فضای تهی»؛ gape (فعل، حدودِ ۱۲۰۰) از gapa «دهان گشودن»؛ و gasp (فعل، اواخرِ سدهٔ چهاردهم، در انگلیسیِ میانه gaispen/gaspen به معنیِ «خمیازه کشیدن») از geispa «خمیازه کشیدن»، با هم‌ریشه‌های سوئدیِ gaspa و دانمارکیِ gispe. کلاین هر سه را با همین ریشه‌های نورسی می‌آورد و اسکیت نیز ذیلِ gap. واتکینز هر سه را زیرِ همین ریشهٔ هندواروپایی فهرست کرده، پس ارجاعِ نورایی به AHD درست است. تحوّلِ معناییِ gasp از «خمیازه» به «نفس‌نفس زدن» تا سدهٔ شانزدهم کامل شده بود (ترکیبِ last gasp از دههٔ ۱۵۷۰).\",\n  \"sources\": [\"https://www.etymonline.com/word/gasp\"],\n  \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt line 504 lists GAP, GAPE and GASP as the English derivatives of ON gap, gapa, geispa under the root.\"}\n  ],\n  \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"KLN_1966.txt lines 15786, 15787, 15830\", \"stance\": \"supports\", \"note\": \"'gap, n. — ME. gap, fr. ON. gap, \\\"chasm, abyss\\\"'; 'gape, intr. v. — ME. gapen, fr. ON. gapa'; 'gasp — ME. gaispen, gaspen, \\\"to yawn\\\", fr. ON. geispa, \\\"to yawn\\\", whence also Swed. gaspa, Dan. gispe.'\"},\n   {\"src\": \"SKT\", \"where\": \"SKT.txt line 7399, s.v. gap\", \"stance\": \"supports\", \"note\": \"'gap, (Scand.) M.E. gappe. — Icel. and Swed. gap, a gap, abyss. — Icel. and Swed. gapa (above).'\"},\n   {\"src\": \"POK\", \"where\": \"POK_full.txt, ghē-2 entry\", \"stance\": \"supports\", \"note\": \"'Middle English gaspen < Old English *gaspian, probably from *gaipsōn' — Pokorny carries the English word itself.\"}\n  ]\n }\n]\n\nfor n in e1[\"nodes\"]:\n    for c in n.get(\"consulted\", []):\n        c.pop(\"stache\", None)\n\nout = {\n \"pdf_page\": 182,\n \"book_page\": 152,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [e0, e1]\n}\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-182.json\",\"w\",encoding=\"utf-8\") as f:\n    json.dump(out, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build182.py"
}
```


### [2026-09-05T21:11:11.167Z] TOOL RESULT

```
written
```


## [2026-09-05T21:11:14.749Z] TOOL CALL #59: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-182.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 182"
}
```


### [2026-09-05T21:11:16.812Z] TOOL RESULT

```
JSON OK
nodes verified: 18/18
node verdicts: {'confirmed': 12, 'disputed': 4, 'plausible': 2}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 15, 'contradicts': 2, 'partial': 4, 'not_checked': 1}
books consulted: {'supports': 29, 'contradicts': 4, 'partial': 6, 'silent': 15} | by book: {'KLN': 12, 'POK': 8, 'SYN': 4, 'WLD': 3, 'AHD': 3, 'MON': 3, 'BQT': 3, 'ARY': 3, 'IEC': 2, 'AFM': 2, 'SKT': 2, 'FVQ': 1, 'TAD': 1, 'LEW': 1, 'WEB': 1, 'LKT': 1, 'PHN': 1, 'CHEUNG': 1, 'HRN': 1, 'HUB': 1}
```


## [2026-09-05T21:11:37.400Z] AGENT

Done. `python3 tools/verify_check.py 182` → **0 PROBLEM lines** (18/18 nodes, both roots).

**Page 182 (book p. 152) — verdicts:** roots 2 confirmed; nodes 12 confirmed, 4 disputed, 2 plausible. Ref checks: 15 supports, 4 partial, 2 contradicts, 1 not_checked. 20 different books consulted.

**Disputed**
- *Ghebh-el* #2 Arabic `qîphaleh, al-qîphâl` — Klein p. 259 (Nourai's own ref, and the chart's NOTE) says al-qifāl is "of uncertain origin, confused by the translators of Avicenna with Gk. κεφαλή" (after Hyrtl 1879); no Greek word was borrowed into Arabic. Gloss "head" is also wrong — it is the cephalic **vein** of the arm.
- *Ghebh-el* #4 Latin `cephalicus` — comes straight from Gk. κεφαλικός (Klein, Etymonline); only the ML phrase *vena cephalica* renders Arabic al-qifāl. Arrow drawn from the Arabic node is wrong.
- *Ghebh-el* #6 Italian `cuffia` — Late Latin *cofia/cuphia* < Proto-West-Germanic *\*kuffju* (Klein s.v. coif; Wiktionary), not Gk. kephalē. Gloss "headband, scarf" also skewed (it is a cap).
- *Ghebh-el* #7 Arabic `kŭfîyyah` — standard etymology is the nisba of al-Kūfa (Wiktionary; cf. Pihan s.v. COUFIQUE), not Italian cuffia. TAD:65 does print Nourai's claim (verified at leaf 68) — the reference is right, the reference is wrong.

**Plausible**
- *Ghebh-el* #3 Persian `قیفال` — Arabic→Persian loan certain (Moʿin [ع.] "رگ بازو"), but gloss "head" wrong and the Greek ancestry is the disputed one.
- *Ghěi* #1 Persian `فاژ/فاژیدن` — word and Labībī verse fully confirmed (Loghat-e Fors p. 178, Borhān-e Qāṭeʿ v3 pdf 227-228 with Moʿin's footnote). The IE derivation rests on Mann (IEC 418) alone, who marks *fa-žīdan* "cpd."; Pokorny, Walde-Pokorny, Horn, Hübschmann, Cheung, Aryanpur all silent, and *ǵʰ- > Iranian z-, never f-.

**Transcription / extraction errors: none.** I rendered pdf p. 182 and compared: every form, script string, the ورید قیفالی extra, the کوفیّه shadda, and the Labībī verse match the JSON exactly. Page numbers verified where checkable: POK:423 ✓, POK:419 ✓, KLN:259 ✓ (leaf 147 = pp. 258-259), IEC:418 ✓ (leaf 241), TAD:65 ✓ (±1 leaf). MON:2769/2470/3127 marked `partial` — entries confirmed via abadis/Moʿin, but the MON OCR has no page markers, and FRS:120 is content-confirmed under a different edition's pagination.
