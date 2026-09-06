# Verification process log — verify-page-228


## [2026-09-06T15:24:45.420Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 228 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-228.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-228.json. Write /home/sfmqrb/git/rishe/data/verification/page-228.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 228` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T15:24:47.039Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T15:24:47.750Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T15:24:47.764Z] TOOL RESULT

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


## [2026-09-06T15:24:48.028Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-228.txt"
}
```


### [2026-09-06T15:24:48.051Z] TOOL RESULT

```
1	=== PDF page 228 (book page 198) ===
2	--- entry 0 ---
3	ROOT Jabra -> redirect to J.b.r
4	--- entry 1 ---
5	ROOT [Arabic] Jamal : camel  (refs AHD:192)
6	#1 (parent #0) [Persian] refs=FVA:81 | jamal «جمل» : camel
7	#2 (parent #0) [Greek] refs=AHD:192 | kamělos
8	  #3 (parent #2) [Latin] refs=AHD:192 | camělus
9	    #4 (parent #3) [Old French] refs=AHD:192 | chamel, chameal
10	      #5 (parent #4) [English] refs=AHD | camel
11	--- entry 2 ---
12	ROOT [Sanskrit] Jangalah : wasteland covered with wild growths  (refs AHD:710)
13	#1 (parent #0) [Hindustani] refs=KLN:836 | jangal : forest
14	  #2 (parent #1) [Persian] refs=BQT:592 | jangal «جنگل» : forest
15	  #3 (parent #1) [English] refs=KLN:836; AID:140 | jungle
16	--- entry 3 ---
17	ROOT [Arabic] J.b.b : a long woolen garment  (refs FVA:67)
18	#1 (parent #0) [Persian] refs=FVA:67 | jobbeh «جُبّه» : garment
19	#2 (parent #0) [Spanish] refs=FSD:1333 | juba : garment
20	  #3 (parent #2) [French] refs=PHN:221 | jupe, jupon : skirt
21	    #4 (parent #3) [Persian] refs=VOP:204 | žŭp «ژوپ ( مینی ژوپ ، ژوپن )» : skirt
22	    #5 (parent #3) [English] refs=KLN:836; FSD:1333 | jupon, jupe, mini-jupe
23	
```


## [2026-09-06T15:24:49.716Z] AGENT

I'll start by looking at the source JSON and the reference infrastructure.


## [2026-09-06T15:24:51.139Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-228.json",
 "description": "Read source JSON for page 228"
}
```


### [2026-09-06T15:24:51.196Z] TOOL RESULT

```
{
  "pdf_page": 228,
  "book_page": 198,
  "entries": [
    {
      "root": {"name": "Jabra", "redirect": "J.b.r"},
      "nodes": []
    },
    {
      "root": {
        "name": "Jamal",
        "lang": "Arabic",
        "refs": "AHD:192",
        "gloss": "camel"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "FVA:81",
          "words": [
            {"translit": "jamal", "gloss": "camel", "script": "جمل"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD:192",
          "words": [
            {"translit": "kamělos", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Latin",
          "refs": "AHD:192",
          "words": [
            {"translit": "camělus", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Old French",
          "refs": "AHD:192",
          "words": [
            {"translit": "chamel, chameal", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "camel", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Jangalah",
        "lang": "Sanskrit",
        "refs": "AHD:710",
        "gloss": "wasteland covered with wild growths"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Hindustani",
          "refs": "KLN:836",
          "words": [
            {"translit": "jangal", "gloss": "forest", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:592",
          "words": [
            {"translit": "jangal", "gloss": "forest", "script": "جنگل"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "English",
          "refs": "KLN:836; AID:140",
          "words": [
            {"translit": "jungle", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "J.b.b",
        "lang": "Arabic",
        "refs": "FVA:67",
        "gloss": "a long woolen garment"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "FVA:67",
          "words": [
            {"translit": "jobbeh", "gloss": "garment", "script": "جُبّه"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Spanish",
          "refs": "FSD:1333",
          "words": [
            {"translit": "juba", "gloss": "garment", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "French",
          "refs": "PHN:221",
          "words": [
            {"translit": "jupe, jupon", "gloss": "skirt", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "VOP:204",
          "words": [
            {"translit": "žŭp", "gloss": "skirt", "script": "ژوپ ( مینی ژوپ ، ژوپن )"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 3,
          "lang": "English",
          "refs": "KLN:836; FSD:1333",
          "words": [
            {"translit": "jupon, jupe, mini-jupe", "gloss": null, "script": null}
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


## [2026-09-06T15:24:52.972Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['AHD','FVA','KLN','BQT','AID','FSD','PHN','VOP','MON','HJB','LKT','SKT','WEB','POK','WLD','IEC','SYN','AFM','PLA','DEV','LAM','DOZ','AFA','ARY','HRN','HUB']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:400])\n\""
}
```


### [2026-09-06T15:24:54.561Z] TOOL RESULT

```
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
FVA {"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 202
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
AID {"title": "G. C. Whitworth, An Anglo-Indian Dictionary, London 1885", "edition_found": "1885 (DLI scan); also 1981 reprint scan", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.45332", "identifier": "in.ernet.dli.2015.45332 (also anglo-indiandictionary, 1981 reprint)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AID.txt", "page_offset": "leaf
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
PHN {"title": "A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, Paris 1866", "edition_found": "1866", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairetym01pihagoog", "identifier": "dictionnairetym01pihagoog (others: bub_gb_QnsSAAAAIAAJ, dictionnairetym00pihagoog)", "local_file": "/home/sfmqrb/git/rishe/data/verific
VOP {"title": "Mahshid Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi, Alborz 1371/1992", "kind": "none", "url": null, "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found (only unrelated similar-title books, e.g. Zomorrodian's فرهنگ ریشه‌شناختی واژه‌های دخیل اروپایی, ketabnak 132354).", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09:
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
HJB {"title": "H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)", "edition_found": "1903 Crooke edition (pagination identical to the 1968 reprint)", "kind": "archive_djvu", "url": "https://archive.org/details/hobsonjobsonagl02croogoog", "identifier": "hobsonjobsonagl02croogoog (others: bub_gb_6Z5iAAAAMAAJ, hobsonjobsonglos00yulerich, india.history.resource
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 =
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_page
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/
DEV {"title": "L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876", "edition_found": "1876", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairety00devi", "identifier": "dictionnairety00devi (also dictionnairetym02devigoog, fr105comparative41)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt", "page_offset": "leaf
LAM {"title": "H. Lammens, Remarques sur les mots français dérivés de l'arabe, Beyrouth 1890", "edition_found": "1890", "kind": "archive_djvu", "url": "https://archive.org/details/remarquessurles00lammgoog", "identifier": "remarquessurles00lammgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAM.txt", "page_offset": "leaf = printed + 57 (e.g. leaf 59 = p.2). local file has \
DOZ {"title": "R. Dozy, Oosterlingen: Verklarende lijst der Nederlandsche woorden die uit het Arabisch, Hebreeuwsch, Chaldeeuwsch, Perzisch en Turksch afkomstig zijn, Leiden 1867", "edition_found": "1867", "kind": "archive_djvu", "url": "https://archive.org/details/oosterlingenver00dozygoog", "identifier": "oosterlingenver00dozygoog (also ...01dozygoog, ...02dozygoog)", "local_file": "/home/sfmqrb/git
AFA {"title": "S. Fraenkel, Die aramäischen Fremdwörter im Arabischen, Leiden 1886 (repr. Hildesheim 1962, same pagination)", "edition_found": "1886", "kind": "archive_djvu", "url": "https://archive.org/details/diearamischenfr00fraegoog", "identifier": "diearamischenfr00fraegoog (also bub_gb_SzdbAAAAQAAJ)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFA.txt", "page_offset": "
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
```


## [2026-09-06T15:24:58.714Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['AHD','KLN','BQT','AID','FSD','PHN','HJB','LKT','SKT','DEV','LAM','AFM','PLA','MON','ARY']:\n    print('=====',k)\n    print(json.dumps(d.get(k), ensure_ascii=False, indent=1))\n\" 2>&1 | head -200"
}
```


### [2026-09-06T15:25:00.769Z] TOOL RESULT

```
===== AHD
{
 "title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)",
 "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)",
 "kind": "archive_djvu+website+archive_restricted",
 "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only",
 "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt",
 "page_offset": "1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.",
 "lookup_hint": "Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.).",
 "notes": "AHD is by far the most cited source (1906). Root order is alphabetical in all versions, so root-name lookup is reliable; page numbers can only be checked against a borrowed copy of the 1976 New College Edition. || RE-SEARCH 2026-09: no open scan of the New College Edition; three borrowable copies on archive.org (avoid the ~840-pp Dell abridgements, which lack the appendix). Local proxy remains AHD_watkins1985.txt.",
 "cites": "page number of the 1975/76 New College Edition; pp. 1505–1550 are the Indo-European roots appendix (look the root up by name)"
}
===== KLN
{
 "title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67",
 "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein",
 "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt",
 "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.",
 "notes": "Other 1966 IA copies (comprehensiveety01klei/02klei etc.) are lending-only (401/403). local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt (paginated by leaf); /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt (plain djvu.txt, no page marks)",
 "local_files": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt"
 ],
 "cites": "page number, continuous across the two volumes (1966–67)"
}
===== BQT
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
===== AID
{
 "title": "G. C. Whitworth, An Anglo-Indian Dictionary, London 1885",
 "edition_found": "1885 (DLI scan); also 1981 reprint scan",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/in.ernet.dli.2015.45332",
 "identifier": "in.ernet.dli.2015.45332 (also anglo-indiandictionary, 1981 reprint)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AID.txt",
 "page_offset": "leaf = printed + 18 (e.g. leaf 20 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Headword in bold at line start; grep -n '^Word'.",
 "notes": ""
}
===== FSD
{
 "title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)",
 "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/in.ernet.dli.2015.147439",
 "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt",
 "page_offset": "vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably detected (pages ~ 700-1640) - grep the headword. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Headword in bold at line start with pronunciation; etymology in brackets at entry end '[< L. ...]'. Very large OCR (16 MB per vol); grep -n '^word' vol file.",
 "notes": "Nourai cites 1940; page numbers in the New Standard were stable 1913-1940s (single-volume pagination 1-2814 continues across the DLI volumes). local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt, /home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol2.txt, /home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol3.txt, /home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol4.txt",
 "local_files": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol2.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol3.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol4.txt"
 ],
 "cites": "page number of Funk & Wagnalls New Standard Dictionary (1940)"
}
===== PHN
{
 "title": "A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, Paris 1866",
 "edition_found": "1866",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/dictionnairetym01pihagoog",
 "identifier": "dictionnairetym01pihagoog (others: bub_gb_QnsSAAAAIAAJ, dictionnairetym00pihagoog)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt",
 "page_offset": "leaf = printed + 31 (e.g. leaf 33 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "French headword in caps at line start; Arabic script not OCRed. grep -n '^BAZAR' etc.",
 "notes": "Built from djvu.xml."
}
===== HJB
{
 "title": "H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)",
 "edition_found": "1903 Crooke edition (pagination identical to the 1968 reprint)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/hobsonjobsonagl02croogoog",
 "identifier": "hobsonjobsonagl02croogoog (others: bub_gb_6Z5iAAAAMAAJ, hobsonjobsonglos00yulerich, india.history.resource.89053)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt",
 "page_offset": "leaf = printed + 35..51 (plates inserted; e.g. leaf 83 = p.32, leaf 319 = p.270, leaf 535 = p.490, leaf 905 = p.870). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Headwords in caps at line start followed by ', s.' etc., e.g. grep -n '^BAZAAR' HJB.txt. Also online at dsal: https://dsal.uchicago.edu/dictionaries/hobsonjobson/ (search box) which shows page numbers.",
 "notes": "",
 "cites": "page number of Hobson-Jobson (1903 ed.)"
}
===== LKT
{
 "title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927",
 "edition_found": "1927",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/etymologische00lokoguat",
 "identifier": "etymologische00lokoguat",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt",
 "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages. grep the oriental source word in transliteration or the number.",
 "notes": "",
 "cites": "entry number of Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs (1927)"
}
===== SKT
{
 "title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)",
 "edition_found": "1911 'new and corrected impression' (Google scan)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/aconciseetymolo01skeagoog",
 "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt",
 "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.",
 "notes": "Nourai says '1882-1967'; the 1967 Oxford reprint reproduces the 1911 rewritten edition, so the 1911 scan is the right pagination.",
 "cites": "page number of Skeat, Concise Etymological Dictionary"
}
===== DEV
{
 "title": "L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876",
 "edition_found": "1876",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/dictionnairety00devi",
 "identifier": "dictionnairety00devi (also dictionnairetym02devigoog, fr105comparative41)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt",
 "page_offset": "leaf = printed + 26 (pp. <80) to +30 (pp. >84), e.g. leaf 29 = p.3, leaf 118 = p.88. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "French headword in caps at line start.",
 "notes": "Devic's text is also printed as the supplement of Littré (dictionnairedela00littuoft)."
}
===== LAM
{
 "title": "H. Lammens, Remarques sur les mots français dérivés de l'arabe, Beyrouth 1890",
 "edition_found": "1890",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/remarquessurles00lammgoog",
 "identifier": "remarquessurles00lammgoog",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAM.txt",
 "page_offset": "leaf = printed + 57 (e.g. leaf 59 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "French headword in caps at line start with running heads like '2 ABRI'.",
 "notes": "Built from djvu.xml."
}
===== AFM
{
 "title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)",
 "kind": "archive_djvu",
```


## [2026-09-06T15:25:13.974Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/sources/refs/ | head -80; echo ---; sed -n '1,60p' data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-06T15:25:14.042Z] TOOL RESULT

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
```


## [2026-09-06T15:25:16.686Z] TOOL CALL #7: Bash

```json
{
 "command": "pdftoppm -f 228 -l 228 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg228 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-06T15:25:18.865Z] TOOL RESULT

```
total 3896
drwx------ 2 sfmqrb sfmqrb   4096 Sep  6 11:25 .
drwx------ 4 sfmqrb sfmqrb   4096 Sep  6 10:51 ..
-rw-rw-r-- 1 sfmqrb sfmqrb    550 Sep  6 11:24 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  92182 Sep  6 10:55 bqt1854.png
-rw-rw-r-- 1 sfmqrb sfmqrb  66580 Sep  6 10:57 bqt2023.png
-rw-rw-r-- 1 sfmqrb sfmqrb 431133 Sep  6 11:16 bqt2420_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb  81018 Sep  6 11:16 build213.py
-rw-rw-r-- 1 sfmqrb sfmqrb   6504 Sep  6 11:13 c1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3402 Sep  6 11:22 c224_n10.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4744 Sep  6 11:22 c224_n1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   7793 Sep  6 11:13 c2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4371 Sep  6 11:13 c_gacele.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3485 Sep  6 11:16 c_harmathan.png
-rw-rw-r-- 1 sfmqrb sfmqrb  12347 Sep  6 11:20 c_hdr.png
-rw-rw-r-- 1 sfmqrb sfmqrb   9147 Sep  6 11:16 c_herman2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3841 Sep  6 11:16 c_herman.png
-rw-rw-r-- 1 sfmqrb sfmqrb  12691 Sep  6 11:20 c_ieuo.png
-rw-rw-r-- 1 sfmqrb sfmqrb  14654 Sep  6 11:20 c_ijlak.png
-rw-rw-r-- 1 sfmqrb sfmqrb  12239 Sep  6 11:20 c_latis.png
-rw-rw-r-- 1 sfmqrb sfmqrb   6280 Sep  6 11:13 c_mag.png
-rw-rw-r-- 1 sfmqrb sfmqrb   6971 Sep  6 11:03 crop1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   8619 Sep  6 11:03 crop2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   5240 Sep  6 11:03 crop3.png
-rw-rw-r-- 1 sfmqrb sfmqrb  12820 Sep  6 11:05 crop_germ.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3408 Sep  6 11:05 crop_guthjo.png
-rw-rw-r-- 1 sfmqrb sfmqrb 111118 Sep  6 11:19 crop_habl.png
-rw-rw-r-- 1 sfmqrb sfmqrb   9001 Sep  6 11:05 crop_node12.png
-rw-rw-r-- 1 sfmqrb sfmqrb   5564 Sep  6 11:05 crop_node1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   5286 Sep  6 11:05 crop_varathra.png
-rw-rw-r-- 1 sfmqrb sfmqrb  11652 Sep  6 11:13 c_xzn.png
-rw-rw-r-- 1 sfmqrb sfmqrb  83691 Sep  6 11:19 gen215.py
-rw-rw-r-- 1 sfmqrb sfmqrb    228 Sep  6 11:06 jscheck.js
-rw-rw-r-- 1 sfmqrb sfmqrb  37376 Sep  6 11:09 mk201.py
-rw-rw-r-- 1 sfmqrb sfmqrb  77132 Sep  6 11:11 mk207.py
-rw-rw-r-- 1 sfmqrb sfmqrb  61121 Sep  6 11:11 mk208.py
-rw-rw-r-- 1 sfmqrb sfmqrb  80041 Sep  6 11:14 mk214.py
-rw-rw-r-- 1 sfmqrb sfmqrb  17605 Sep  6 11:25 mk218.py
-rw-rw-r-- 1 sfmqrb sfmqrb  50138 Sep  6 11:24 mk222.py
-rw-rw-r-- 1 sfmqrb sfmqrb  17907 Sep  6 11:25 part1.json
-rw-rw-r-- 1 sfmqrb sfmqrb  54688 Sep  6 10:58 pg201.png
-rw-rw-r-- 1 sfmqrb sfmqrb  70083 Sep  6 10:52 pg204.png
-rw-rw-r-- 1 sfmqrb sfmqrb  77858 Sep  6 10:52 pg206.png
-rw-rw-r-- 1 sfmqrb sfmqrb  67371 Sep  6 10:53 pg207.png
-rw-rw-r-- 1 sfmqrb sfmqrb  59146 Sep  6 10:53 pg208.png
-rw-rw-r-- 1 sfmqrb sfmqrb  53054 Sep  6 11:00 pg209.png
-rw-rw-r-- 1 sfmqrb sfmqrb  74515 Sep  6 11:02 pg211.png
-rw-rw-r-- 1 sfmqrb sfmqrb 141781 Sep  6 11:03 pg212hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  75961 Sep  6 11:02 pg212.png
-rw-rw-r-- 1 sfmqrb sfmqrb  83761 Sep  6 11:03 pg213.png
-rw-rw-r-- 1 sfmqrb sfmqrb  83752 Sep  6 11:01 pg214.png
-rw-rw-r-- 1 sfmqrb sfmqrb 194102 Sep  6 11:05 pg215hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb 117034 Sep  6 10:54 pg215.png
-rw-rw-r-- 1 sfmqrb sfmqrb  76564 Sep  6 11:13 pg216.png
-rw-rw-r-- 1 sfmqrb sfmqrb  82798 Sep  6 11:16 pg217.png
-rw-rw-r-- 1 sfmqrb sfmqrb 147278 Sep  6 11:13 pg218hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  82099 Sep  6 11:13 pg218.png
-rw-rw-r-- 1 sfmqrb sfmqrb  71937 Sep  6 11:19 pg219.png
-rw-rw-r-- 1 sfmqrb sfmqrb  63280 Sep  6 11:18 pg220.png
-rw-rw-r-- 1 sfmqrb sfmqrb  71497 Sep  6 11:18 pg221.png
-rw-rw-r-- 1 sfmqrb sfmqrb 118895 Sep  6 11:16 pg222hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  84108 Sep  6 11:16 pg222.png
-rw-rw-r-- 1 sfmqrb sfmqrb  79615 Sep  6 11:18 pg223.png
-rw-rw-r-- 1 sfmqrb sfmqrb  90848 Sep  6 11:22 pg224hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  55412 Sep  6 11:15 pg224.png
-rw-rw-r-- 1 sfmqrb sfmqrb  74322 Sep  6 11:19 pg226.png
-rw-rw-r-- 1 sfmqrb sfmqrb  52519 Sep  6 11:25 pg228.png
-rw-rw-r-- 1 sfmqrb sfmqrb 147680 Sep  6 11:20 sns167.jpg
```


## [2026-09-06T15:25:22.571Z] TOOL CALL #8: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg228.png"
}
```


### [2026-09-06T15:25:22.913Z] TOOL RESULT

```

```


## [2026-09-06T15:25:22.912Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T15:25:38.657Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN 1966 jungle ===\"; grep -n \"^jungle\" KLN_1966.txt | head\necho \"=== KLN 1966 jupon/jupe ===\"; grep -n \"^jup\" KLN_1966.txt | head\necho \"=== KLN camel ===\"; grep -n \"^camel,\" KLN_1966.txt | head\necho \"=== AID jungle ===\"; grep -n -i \"^Jungle\" AID.txt | head\necho \"=== PHN JUPE ===\"; grep -n -i \"^JUP\" PHN.txt | head\necho \"=== PHN ALJUBA/JUBE ===\"; grep -n -i \"jubbah\\|djoubbah\\|joubbah\" PHN.txt | head"
}
```


### [2026-09-06T15:25:38.774Z] TOOL RESULT

```
=== KLN 1966 jungle ===
=== KLN 1966 jupon/jupe ===
20477:jupon,  n.,  skirt,  petticoat.  —  F„  fr.  Arab.  jubbah, ‘a  long  woolen  garment’  (whence  also  It.  giubba, OProven?.  jupa,  Sp.  aljuba).  Cp.  gyp,  jump,  ‘a kind  of  jacket’,  jumper,  ‘blouse’.
=== KLN camel ===
=== AID jungle ===
3223:Jungle.  [Hindi  jangal ,   from  the Sanskrit  jangala .]  A   wild  or  un- inhabited country,  a   desert  forest.
=== PHN JUPE ===
6318:JUPE, s. f. et JUPON, 8. m. (a.)
10647:Jupe, s. f. et Jupon , s. m. ( a.) 991390 TABLE ALPHABÉTIQUE
=== PHN ALJUBA/JUBE ===
```


## [2026-09-06T15:25:41.091Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FSD vol2 juba ===\"; grep -n \"^juba\\|^ju.ba\\|^jupe\\|^jupon\" FSD_vol2.txt | head -20\necho \"=== FSD vol2 jungle ===\"; grep -n \"^jungle\" FSD_vol2.txt | head\necho \"=== LKT gamal/jubba ===\"; grep -n -i \"kamel\\b\\|gamal\\|ǧubba\\|jubba\\|dschubba\" LKT.txt | head -20\necho \"=== SKT jungle/camel ===\"; grep -n -i \"^JUNGLE\\|^CAMEL\\|^JUPON\" SKT.txt | head"
}
```


### [2026-09-06T15:25:41.189Z] TOOL RESULT

```
=== FSD vol2 juba ===
65762:jupe,  1   ]Qp;  3   Jup,  »•  A   heavy  Jacket;  jupon;  a   long  petti- coat: the  skirt  of  a   dress,  ju'pelt.— ju-pette%  n.  [F.l  A   ' shorUsklrted  jupon.
=== FSD vol2 jungle ===
=== LKT gamal/jubba ===
1323:'Kamel'  [vielleicht  vom  Stamme  tok,  tot 'dicht,  fest,  festmachen',  vgl.  cag.  tüje' mek  'aufladen',  also  tüje,  cuwas.  töve, osm.  dewe  'Kamel',  eigentlich  'Lasttier', Vämbery  TktEtWb  S.  180,  Nr.  1 93 1  Ende] ; hieraus  serb.  dewa  'dass.'.
1627:ö53.  Ar.  gaiual: 'Kamel'  [aus  der  Wurzel  (jamala  'sam- meln', also  'Haufen,  Höcker',  vielleicht urverwandt  mit  hammäl  'Lastträger',  s. hier  Nr.  806,  SCHOTT  in  ZDMG  XXXIH, 54:-!];  aus  dieser  oder  einer  anderen semitischen  Form  gr.  Ka|nriXo;,  lat.  cä- 7nelus,  *cämellus\  hieraus  it.  cammello, siz.  camiddu,  \n-ov.  camels,  Irz.  chameau, kat.  camell,   sp.   cameUo,    pg.  camelo; dtsch.  Kamel,  engl,  caniel;  [aus  gr.  ko- |a»iXiov]  russ.  (alt)  hamil',  bulg.  kamila, serb.  kamila,  kamilj.  —  Vielleicht  nur volksetymologisch    hängt    mit  diesem Grundwort  lat.  camelinum,  camelötum, gr.  KaiwiriXuuTri  zur  Bezeichnung  eines 'langhaarigen,  plüschartigen  Stoffes'  zu- sammen;    hieraus    altit.  cammellino, canibellotto,  it.  cammellotto,  sp.  camelote, frz.  camelot,  dtsch.  Kamelot,  Kamelott [früher:  Schamlott,  Zamlott],  Kamelhaut, russ.  kamlot,  ßech.  kamelot,  poln.  kamlot. —   Aus   dem   tk.  gamal  'Hanswurst, läeherhcher  Kerl'  wurde  rum.  geamalä 'Riese,  Ungetüm'.  —  Vielleicht  ist  aus dem  semitischen  Grundwort  auch  ge- worden   gr.    KaßäWri«;,    lat.  caballus; hieraus  zahlreiche  romanischen  Formen und  schließlich  auch  dtsch.  'GauV.  — Auf  denselben  semitischen  Stamm  geht wahrscheinlich  der  Eigenname  Kam  eil zurück;  nach   dem   Brünner  Jesuiten JOSEF  KAMELL  ist  die  Kamelie  Thea japouica,  frz.  camüia,  benannt,  da  er sie  i.  J.  1738  zuerst  in  zwei  Exemplaren von  Japan  nach  London  brachte.  [Kluge 223.  ML  1544.  Gorjajew  130.  BernSlLlt- Wb477.  GSAJin,  144.
2049:'Tragkorb  auf  einem  Kamele,  Kamel- sänfle',  ebenso  bind,  hauda  'Silz  auf einem  Elefanten' ;  hieraus  angloind, hotvdah,  howder  'ein  großer  Sitz  auf einem  Elefanten',  für  zwei  und  mehr Personen  eingerichtet,  gewöhnlich  noch mit  einem  Schutzdach  versehen.  [Hob- son-Jobson  4!27/428.
3158:N.  pr.,  Stammvater  eines  ar.  Stammes, nach  welchem  schnell  laufende  Kamele in  Nordafrika  als  mahrija,  pl.  mahärt bezeichnet  werden;  hieraus  frz.  mahari, sp.  mahari  [Dicc  Gast  13U0a]  'Laufkamel, Dromedar'  in  Nordafrika.  [Devic  DEt  155.
3936:'Sagenhafter  Vogel'  [wohl  über  das  Pers. aus  mal.  ruivak  'großer  Raubvogel' Pijn  125  und  MMM  47];  'mit  Bogen- schützen besetzter  Elefant  oder  Kamel', auch  Figur  im  Schachspiel;  hieraus  it. rocco  'Turm  im  Schachspiel',  Vb.  arro- care  'den  König  an  die  Stelle  des  Turmes und  umgekehrt  setzen'  [ein  Verfahren, dessen  Einführung  in  das  XVI.  Jhdt. fällt],  sp.  }-oque,  enrocar,  pg.  roque,  kat, roch,  frz.  roc,  roquer,  prov.  roc;  engl. 7-ook,  dtsch.  Boche  "Turm  im  Schach- spiel', tochieren,  rockieren.  —  [Nach anderer  Ableitung  geht  ar.  ruh  in  der Bedeutung  'Wagen'  auf  bengal.  roih zurück.]  [DE  335.  Devic  DEt  196/198. Eguilaz  485.    ML  7366.
5014:1388 Jubii  II.  r)(i7 Juda  941) JuUiin  lOO-i Jute  li93 Kaffa  lOüf) Än/l^f«  lüOn Kala  \m\ kaliktit  1031 Kamel!  653 i:ao/i«  1060 Kapha  851 A'nrZ  rf.  (?r.  605 Kam»  1144 A'rtsfcft  fTunfsi  1108
5787:Äafta?e  977 iCrtöajg  993 iCa^eZ  766 Zaö(//e  979 ^Tad«  984 ifßtZjne  989 i:fl/f  992 Kaffee  4005 ^^//fe;-  992 Ka filier  j.  1150 Kaftan  774 Kaj>'put(öl)  1142 Kakadu  1Ü17 Kolbehasit  St.  1026 Kalbelazguar  St.  1025 Kalbolacrab  St.  1026 kalekutischer  Hahn  1031 kalemine  mhd.  1149 Kalender  1024 Kalenter  1024 kalfatern  1022 Kaliber  1030 ifaZ//"  798 A'rtZiX-o  1031 Kalium  1029 ifaZ/e  j.  1035 ifaZo«^  1038 Ar<?jjrtfc  1039 Kamel  653 Kamelie  653 Kamelhaut  653 Kamelot(t)  653 Kampfer  1100 Kandare  1051 kandieren  1052 Kandis  fzuckerj  1052 Kantschu(k)  1042 iCao/in  1060 Kap(p)ern  978
6043:gamal  714
=== SKT jungle/camel ===
2689:CameL  (F.  -  L.-Gk.  -  Heb.)  M.E. camd,  <amaii,  chameL  ••  O.  F.  camtl,  ihanul.
2691:camelopard,  a  giraffe.  (L.—  Ilcb.  and Gk.)  Formerly  eamdop<u-daiis.  <»  L.  ca- nuhpaniaiis.  —  Gk.  «a^Aovii^>2aAis,  giraffe  ; partly  like  a  camel,  jiaxtly  like  a  pard.* Gk.  j(a/u]Ao-r.  a  camel  i^Wch. gdrndi) \  nud «af>3aA(t,  a  pard  i  see  FartL
```


## [2026-09-06T15:25:49.168Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if re.search(r'\\bjupon\\b',p) or re.search(r'\\bjungle\\b',p,re.I):\n        print('LEAF',i, p[:120].replace('\\n',' '))\nEOF"
}
```


## [2026-09-06T15:25:51.209Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"jungle\" KLN_1966.txt | head -10\necho \"=== camel KLN ===\"; grep -n -i \"camel,\" KLN_1966.txt | head -10\necho \"=== AID leaf for jungle ===\"; python3 -c \"\nt=open('AID.txt',encoding='utf-8',errors='replace').read()\nps=t.split('\\f')\nfor i,p in enumerate(ps):\n    if 'Jungle' in p: print('LEAF',i,'printed~',i-18); print(p[:300])\n\""
}
```


### [2026-09-06T15:25:52.049Z] TOOL RESULT

```
LEAF 344  Glossarium  mediae  et  in- fimae  latinitatis,  s.v.  balare. galingale,  n.,  an  aromatic  root  of  the  ginger fam
LEAF 451  ‘rose’, and  ab,  ‘water’.  See  rose  and  abdest. Julia,  fem.  PN.  —  L.  Julia,  fem.  of  Julius.  See Julius. Ju
```


### [2026-09-06T15:25:53.835Z] TOOL RESULT

```
15729:Gallophobe,  n.,  one  who  fears  or  hates  France  or the  French.  —  Compounded  of  Gallo-  and  Gk. -rfofioQ,  fr.  q>6(3ot;,  ‘fear’.  See  -phobe. Gallophobia,  n.,  fear  or  hatred  of  France  or  the French.  —  Compounded  of  Gallo-  and  -q>o(3toc, ‘fear  of’,  fr.  <po(3o ‘fear’.  See  -phobia. Galloway,  n.,  a  small  horse.  —  Orig.  meaning ‘horse  bred  in  Galloway,  Scotland’, gallows,  n.  —  ME.  galowes,  galwes  (pi.),  fr.  OE. gealga,  rel.  to  OS.,  OHG.  galgo,  ON.  galgi, OFris.  galga,  MHG.  galge,  ‘gallows;  cross’,  G. Galgen,  ‘gallows’,  Goth,  galga,  ‘cross’,  and  to ON.  gelgja,  ‘pole,  perch’,  and  cogn.  with  Arm. jalk,  ‘twig’,  Lith.  zatga,  Lett,  zalga,  ‘pole,  perch’. Gallus,  n.,  a  genus  of  birds,  the  common  domestic fowl  and  the  jungle  fowl.  —  L.  gallus,  ‘cock’. See  gallinaceous.
20463:June,  n.  —  L.  Junius  (mensis),  lit.  ‘the  month (named  in  honor  of)  Juno’,  fr.  Juno.  See  Juno, jungle,  n.  —  Hind,  jangal,  ‘desert,  forest’,  fr.  OI. jangalah,  ‘dry  ground,  waste  land,  desert’,  which is  of  uncertain  origin.
=== camel KLN ===
6268:cameist,  n.,  1)  one  who  makes  or  collects  cameos; 2)  an  expert  in  cameos.  —  A  hybrid  coined  fr. cameo  and  -ist,  a  suff.  of  Greek  origin, camel,  n.  —  ME.  camel,  earned,  charnel,  chamail. fr.  OE.  camel ,  fr.  ONF.  camel,  corresponding  to OF.  charnel  (whence  F.  chameatt),  fr.  L.  came- lus,  fr.  Gk.  xxpvjXoc,  fr.  Heh.  and  Phocn.  gamdl, ‘camel’,  which  is  rel.  to  Arab,  jdmai,  of  s.m. Cp.  gamma,  gimel.
6499:caravan,  n.  F.  caravane,  fr.  Pers.  karwan, ‘company  of  travelers,  caravan’,  which  is  rel. to  OI.  karabhdh,  ‘camel,  young  camel,  young elephant’.
34873:shamble,  n.  —  ME.  schamel,  shamel,  ‘bench’,  fr. OE.  scamel,  ‘stool,  bench,  table’,  rel.  to  ON. skemill,  Du.  schemel ,  OHG.  scamil  (in  fuoy scamil),  ‘(foot)  stool’  (whence  MHG.,  G.  sche¬ me/)  ;  borrowed  fr.  L.  scamellum,  ‘bench,  stool’.
=== AID leaf for jungle ===
LEAF 159 printed~ 141
- men,  as  distinguished  from  the wilder  Kukis.
Jumah.  [Hindustdni,  from  the Arabic.]  The  Muhammadan  Fri- day, the  day  of  public  prayer.
Jumardt.  [Hindustdni  jumah ,   Fri- day, and  rdty  from  the  Sanskrit  rdtn\ night.]  The  Muhammadan  Thurs- day, so  called  as  being  the  ev
```


## [2026-09-06T15:26:11.397Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nps=t.split('\\f')\nfor i in (450,451,452):\n    p=ps[i]\n    print('=== LEAF',i,'len',len(p))\n    print(p[:600])\n    print('...TAIL...')\n    print(p[-400:])\nEOF"
}
```


### [2026-09-06T15:26:13.370Z] TOOL RESULT

```
=== LEAF 450 len 12101
o  gau- dere,  ‘to  rejoice'.  See  gaud  and  cp.  enjoy.  Cp. also  feu  de  joie,  rejoice.
Derivatives:  Joy,  v.  (q .\.),joy-fut,  adj ,,joy-ful-ly, adv.,  joy-ful-ness,  n.,  joy-less,  adj.,  joy-less-ly, adv.,  joy-less-ness,  n.
joy,  intr.  and  tr.  v.,  to  rejoice.  —  OF.  joir  (F. jouir),  fr.  VL.  *gaudire  (whence  also  OProveng. jauzir),  corresponding  to  L.  gaudere,  ‘to  re¬ joice’  (whence  It.  godere,  of  s.m.)  See  joy,  n. Joyce,  fern.  PN.  —  Earlier  Josse,  Goce,  etc.,  orig.
used  both  for  men  and  women;  of  Celtic  origin, joyous,  adj.  —  OF.  j
...TAIL...
phum,  ‘jujube’,  which  together with  Late  L.  zizyphus,  'jujube  tree’,  derives  fr. Gk.  Shipov,  ‘jujube  tree;  jujube’,  which  is  of unknown  origin.  Cp.  Zizyphus. julep,  n.,  a  sweet  drink.  —  F.,  fr.  OProven^.  julep or  fr.  Sp.  julepe,  fr.  VAr.  juleb,  corresponding to  classical  Arab,  juldb,  fr.  Pers.  gulab,  ‘rose water,  julep’,  which  is  compounded  of  gul, 
=== LEAF 451 len 12397
 ‘rose’, and  ab,  ‘water’.  See  rose  and  abdest.
Julia,  fem.  PN.  —  L.  Julia,  fem.  of  Julius.  See Julius.
Julian,  masc.  PN.  —  L.  Julianus,  a  derivative  of Julius.  See  Julius  and  -an.
Julian,  adj.,  pertaining  to  Julius  Caesar.  —  L. Julianus,  ‘of,  or  belonging  to,  Julius  Caesar’. See  prec.  word  and  cp.  the  PN.  Gill.
Juliana,  fem.  PN.  —  L.  Juliana,  fem.  of  Julianus, lit.  ‘belonging  to  Julius'.  See  Julius  and  cp. Julian.
julienite,  n.,  a  hydrous  cobalt  chloronitrate (mineral.)  —  Named  after  the  Belgian  geologist Henri  Julien  (
...TAIL...
 ‘justice,  equity,  uprightness’, fr.  justus.  See  just  and  -ice. justiciable,  adj.,  subject  to  jurisdiction.  —  OF. (—  F.),  fr.  OF .  just  icier,  ‘to  administer  justice’, fr.  ML.  justitiare,  fr.  L.  justitia.  See  prec.  word and  -able.
Derivatives :  justiciable,  n.,  a  person  subject  to jurisdiction,  justici-abil-ity,  n. justiciar,  n.,  the  highest  judicial  offi
=== LEAF 452 len 12166
cer  of  the kings  of  England  from  the  reign  of  William  I to  that  of  Henry  III.  —  ML.  justitiarius,  ‘officer of  justice’,  fr.  L.  justitia.  See  justice  and  subst. suff.  -ary  (representing  L.  -arius). justiciary,  adj.,  pertaining  to  justice;  n.,  an  officer of  justice.  —  ML.  justitiarius,  ‘officer  of  justice’. See  prec.  word.
justifiable,  adj.  —  F.,  fr.  justifier,  ‘to  justify’.  See justify  and  -able.
Derivatives;  justifiabil-ity,  n . ,  justifiable-ness,  n., justifiabl-y,  adv.
justification,  n.  —  Late  L.  jUstificatio,  fr.  justi¬ fie
...TAIL...
  Leiden 1886,  p.203).  See  centenarian  and  cp.  centner. Cp.  also  quintal  and  kilderkin.
Kantian,  adj.,  pertaining  to  Immanuel  Kant (1724-1804)  or  his  philosophy;  n.,  an  adherent of  the  teachings  of  Kant.
Kantianism,  n„  the  philosophy  of  Immanuel Kant.  —  See  prec.  word  and  -ism. kaolin,  n.,  china  clay.  —  F.,  fr.  Chinese  kao-ling , lit.  ‘high  hill’;  so
```


## [2026-09-06T15:26:28.057Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('FSD_vol2.txt',encoding='utf-8',errors='replace').read()\nps=t.split('\\f')\nfor i,p in enumerate(ps):\n    if re.search(r'\\bjupon\\b',p,re.I) or re.search(r'\\bjupe\\b',p,re.I) or re.search(r'\\bjungle\\b',p,re.I):\n        print('=== LEAF',i)\n        print(p[:200].replace('\\n',' '))\n        for m in re.finditer(r'.{0,200}(jupon|jupe|jungle|juba).{0,300}',p,re.I):\n            print('   >>',m.group(0).replace('\\n',' ')[:420])\n        break\nEOF"
}
```


## [2026-09-06T15:26:29.119Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('PHN.txt',encoding='utf-8',errors='replace').read()\nps=t.split('\\f')\nfor i,p in enumerate(ps):\n    if 'JUPE' in p:\n        print('LEAF',i,'printed~',i-31)\n        print(p[:1500])\n        break\nEOF"
}
```


### [2026-09-06T15:26:30.162Z] TOOL RESULT

```
=== LEAF 255
ool  rule,  f.sfootedf.  II.  n.  A four»footed  animal;  mammal.-  f.  genii  of  Amentl,  four guardian  spirits  of  Amentl,  the  Egyptian  nether  world, whose  heads  were  often  sculptured  on
   >> Indian  jungle- fowl  (Gallusfer- rugineus)  is probably  the original.  See table  on  follow- ing page.  3.  The flesh  of  fowls, especially  of  the full »   grown  do- mestic hen,  as food;inoookery, distinguished
```


### [2026-09-06T15:26:31.857Z] TOOL RESULT

```
LEAF 252 printed~ 221
JUP âàl
d'où vient par suite, ainsi qu'on l'a vu, ç^j^ys^ [djavolinriyy\
joaillier.
JULEP, s. m. composé, (a.-p.)
Lj'^k^ [djoulAb] et v^^ [djouUah] Potion médicinale, rafraî-
chissante, composée de fruits, de miel ou de sucre, et d'eau.
— Le terme arabe est une imitation du persan v^^^ [s^^^ |
eau de rose, formé de J^^ [gti/] rose, et de v' [àb] ^^u, à cause
de la couleur rosée que l'on donne habituellement à cette es-
pèce de breuvage. — De là viennent aussi l'espagnol et le por-
tugaisyu/epe, ainsi que l'italien gitdebbo et giulebbe.
JUPE, s. f. et JUPON, 8. m. (a.)
i^u^ [djoubbat] pelisse courte, vêtement sans manches ou à
manches courtes que les Orientaux portent sous la grande pe-
lisse ou sous le manteau appelé bénxch; dérivé de <^^i^- [^^^^]
retrancher, raccourcir. — Chez nous, on appelle jupe la partie
de la robe qui s'étend depuis la ceinture jusqu'aux pieds; et
le jupon est un vêtement court et sans corsage que les femmes
portent le matin avec la camisole, dans leur négligé, ou sous
la robe, pour lui donner plus de grâce. — Comparez l'italien
ffiuppa, fuis giuppone, mots évidemment tirés de l'arabe comme
leurs correspondants français. Les Espagnols, qui ont conservé
le terme arabe précédé de l'article al, écrivent aljuba. On trouve
aussi chez les Portugais aljuba et aljubeta.
```


## [2026-09-06T15:26:40.312Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('FSD_vol2.txt',encoding='utf-8',errors='replace').read()\nps=t.split('\\f')\nfor i,p in enumerate(ps):\n    if re.search(r'jupon',p,re.I) and re.search(r'jupe',p,re.I):\n        print('=== LEAF',i)\n        for m in re.finditer(r'.{0,120}(jupon|jupe|juba).{0,400}',p,re.I):\n            print('   >>',m.group(0).replace('\\n',' ')[:520])\n        print('---- head ----'); print(p[:300].replace('\\n',' '))\nEOF"
}
```


### [2026-09-06T15:26:42.082Z] TOOL RESULT

```
=== LEAF 627
   >> jupe,  1   ]Qp;  3   Jup,  »•  A   heavy  Jacket;  jupon;  a   long  petti- coat: the  skirt  of  a   dress,  ju'pelt.— ju-pette%  n.  [F.l  A   ' shorUsklrted  jupon.
---- head ----
 junior;  rank a   Junior. The  subordiaation  of  Poseidon  to  Zeus  rested  on  i juniority. Gi,adstonb  Juvenlus  Mundi  p.  247.  [n. B.  ico.1869.] 2.  Law.  Same  as  bomough- English.  See  nonouGH.  Also known  as  Junior  right. A   large  brown  scarabceld  beetle  of the  genua  Lachnost
=== LEAF 628
   >> of  jupe,  <   Sp.  juba,  <   Ar.  jubbalt,  gar-  rlsdiction,  the  Jurlsdietlon  held  by  two  or  more  tribunals
   >> M;  togtoL  potot  CrlGdeda-Ntoige;  mor  and  Jupon.  expounded,  and  judicially  applied;  the  science  of
   >> Law.  A   judicial  oath.  [L.,  <   it/ro,  swear;  see  jubati.)  ju-rls'tlc,  1   ju-ria'tik;  2   jij-rls'tlc,  a.  Law.  Of  or  pertaining  to ju'rant,  1   jQTant;  2   ju'raut.  I.  a.  Taking  o.ath.  II.  b.  One  a   jurist  or  the  profession  of  law.  jn-ris'tl-caU.— Jurhstlc
---- head ----
oTLuy  John  of  fJnrneceld  vol.  ii,  p.  411.5.  [ir.  1874.) 2.  Assumed  by  law'  to  exist :   of  the  nature  of  a   legal  fic- tion; as,  ajuriilkal  person.  [   <   h.  juriilir.us,  <   jus  {jur-) , law, -b  dico,  declare.)  ju-rid'tct.- juridical  dstys,  days ■when  the  courts  a
```


## [2026-09-06T15:26:50.212Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('FSD_vol2.txt',encoding='utf-8',errors='replace').read()\nps=t.split('\\f')\nfor i in (626,627,628,629):\n    p=ps[i]\n    nums=re.findall(r'\\b1[23]\\d\\d\\b',p)\n    print(i, nums[:15])\n    print('   first line:', p.strip().split('\\n')[0][:120])\n    print('   last  line:', p.strip().split('\\n')[-1][:120])\nEOF"
}
```


### [2026-09-06T15:26:52.053Z] TOOL RESULT

```
626 []
   first line: den  balsam  (ImpatUns  balsamina).  —   J,  bag,  a   bug
   last  line: 1.  The  state  of  being  Junior  or  a
627 ['1333']
   first line: junior;  rank a   Junior.
   last  line: ilc  fGro(iua)  plunged  once  more  into  tlio.®  claRsical,  furidical, and  theological  studies  which  bud  aivva.v
628 ['1334']
   first line: oTLuy  John  of  fJnrneceld  vol.  ii,  p.  411.5.  [ir.  1874.) 2.  Assumed  by  law'  to  exist :   of  the  nature  o
   last  line: prejia:.  Rigged  up  temporarily;  makeshift:  used in  nautical  compounds;  as,  /nrij-mast;  jury-rudder; j’ury-sail
629 []
   first line: a   bit  of  nautical humor.l— Ju'ry»leg",R.  [Slang.]  An  artificial  leg.— J. -mast, «.  Surg.  An  iron  rod  fixed 
   last  line: 1   yQs-tl  ne,  3   yijs-ti'ne;  It.  Cilas-tl'na,  1   jn.s-tl'na,  3   gi.is-  Ju-vn’Tyin,  n.  Same  as  Salziujiic}
```


## [2026-09-06T15:27:00.353Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nps=t.split('\\f')\nprint('nleaves',len(ps))\nfor i in (50,51,52,53,54):\n    p=ps[i]\n    print('=== LEAF',i,'printed~',i+540)\n    print(p[:800])\nEOF"
}
```


### [2026-09-06T15:27:02.200Z] TOOL RESULT

```
nleaves 684
=== LEAF 50 printed~ 590
   ‫سوت‬                                                                                ‫جنگه‬
‫و بیاض بزر که را حمگفته‌اند ‪ -‬و نومی‬   ‫است ‪-‬‬   ‫و کنکاش کردن جممی باشد باهم» گوبند‬       ‫است ‪-‬‬

                          ‫از قمار یز هت ‪.‬‬                                     ‫ترکی است ‪. ۷‬‬
‫ررچ»نگه را‬‫خگا‬
            ‫جنگار » بروزن زن‬                    ‫جنگ س بفتح اول وسکون‌نالی وکاف»‬
‫‪-‬تی فاعل ‪۴‬‬
         ‫بندمع‬‫وان‬
                ‫گوبند وبمربی‌سرطان خو‬             ‫عوم‬‫معروف است که جدال و قنال باشد ‪- ۴‬‬
 ‫اول شتربرا گوبندکه هنوز او را (‪ )۱‬بزیر بار | که جنگ آورنده باشدسوامرهم هست‪*. ۴ .‬‬
‫جنگ زر گری ه کنابه از جنگه‬                     ‫نکشیده باشند ‪ -‬و بمعنی کشتی و جپاز بزرکه‬
                          ‫ساختگی باشد ‪# .‬‬      ‫هم هت » و باین معتی باجيم ف
=== LEAF 51 printed~ 591
  ‫جنیور‬                                                                                     ‫وت‬   ‫‪۳‬‬


‫جنکو لت (‪ - )۳‬بروزن‌مفلوك ‪.‬کی‌را‬                       ‫بالامبروزن بزمگاهی»‬        ‫جنگالاهی ‏‬

 ‫کوبند که از بیماری برخاسته باشد ق۽وت‬                 ‫غلیواج را گویند » و باینمعنی بجای های هوز‬
                        ‫‪.‬‬        ‫رفتار نداشته باشد‬     ‫نون وبای حطی هم‌بنظرآمده استکه جنگلالی‬
‫جنییت کش ‪ «۰‬شخصی را کوبند که‬                           ‫گیفزته‌اند ‪.‬‬         ‫سمی‬
                                                                              ‫راجی‬
                                                                                 ‫»وب‬
                                                                                   ‫فدا‬
                                  
=== LEAF 52 printed~ 592
                                     ‫يان هجد هم(‪)۱‬‬
           ‫جیم ابجد باواو مشتمل برهفتاد و نهلفت و کنایت‬                                ‫در‬


‫ويره از انگور‬
            ‫که در آن روغن از حبوبات ش‬                     ‫جو » نم اچولوبی باشد که بوقت‬
                                                                         ‫زمین شدبار(‪ )۲‬کردن بر گردن‬
‫و بفتح اول در عربی بمعنی رخصت و اجازت ‪-‬‬                                  ‫کاو گذارند ‪ - ۱‬و مراب نود‬
‫وروالی وروابی‪-‬‬   ‫وخط ودستك راه ‪-‬‬     ‫‪-‬‬    ‫خلاص‬     ‫‪۱‬و‬                   ‫و ششم باشد از خلوص زر که‬
‫و روان شدن ‪ -‬و آب دادن ستور و کشت زار‬                                     ‫"را بعربی‌عیارخوانند ‪ -‬وجوی‬
                                         ‫! باشد ‪٩‬‏ ‪.‬‬                     ‫آبرا یز گوبند ‪ ۴‬وبفتح‌
=== LEAF 53 printed~ 593
  ‫جوج‬                                                                                                     ‫ویس‬
                                                                                                            ‫‪--‬‬


                                           ‫‪۰‬‬   ‫هم هست‬
                                                            ‫جوا = باشومل‌بروزن زغال‪ ,‬معروف‬
‫» بکر اول بر وزن لپالی ؛‬              ‫جوالی‬                ‫اتفمته که چیز ها‬
                                                                          ‫ظآرنفی باشد ابزپ‬
                                                                                         ‫ات و‬

‫بانخواه_ و زنان )‪(٩‬‏ هم گویند ‪ -‬و بفتح اول‬                 ‫و پمعنی مکر و حیله همآمده است ‪ -‬و کنابه‬
           ‫‪.‬‬   ‫معروف است که 
=== LEAF 54 printed~ 594
‫سم"‏‪ ٩,‬چ سس‬                                                                             ‫جو جادو‬
‫يك‌فرسخ وئلث فرسخی‌باشد که چپار گروه‌است‪.‬‬             ‫و علامتی را یز گونند که برسرطاقها وابوانها‬
                                                     ‫صب کنند تا خوشنما شود ‪ ,‬و بفتح اول هم‬
‫جو جو ه بفتح هر دو جيم و سکون‬
                                                                                           ‫گفته‌اند ‪.‬‬

‫اجا مك خوب وفوراعلی وجامهای ابریشمی‬                   ‫جحوبجاهدو‌ا=یت تیه بجولیکن‬
‫رزه‬   ‫و کنانه از باره باره و ررە‬      ‫مشود‬   ‫فس‬       ‫باربکتر و دراز ترمیباشد و طعم آن تلخ است »‬
                           ‫؟ ‪.‬‬    ‫ودره دره هم هت‬      ‫و طبیمت آن گرم و خشك است در اول وسیم‪.‬‬
‫هعنی حوزه‬     ‫و‬   ‫بر ورن‬    ‫‪-‬‬    ‫جوجه ‪°‬‬
```


## [2026-09-06T15:27:11.173Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nps=t.split('\\f')\nfor i,p in enumerate(ps):\n    if 'جنگل' in p:\n        print('LEAF',i,'printed~',i+540)\n        import re\n        for m in re.finditer(r'.{0,80}جنگل.{0,150}',p):\n            print('  >>',m.group(0).replace('\\n',' '))\nEOF"
}
```


### [2026-09-06T15:27:12.887Z] TOOL RESULT

```
LEAF 50 printed~ 590
  >>                                                          ‫‪ #‬جنگل ‪ -‬بفتح اول و سوم »‬
  >>                                               ‫است ‪ « .‬دائرقالمعارف اسلام ‪ °‬جنگل‬
  >>                                                          ‫جنگل مجموعة بزرگی‌است ازدرختان‬
  >>                                                          ‫رك‪ :‬جنگل‌شناسی تألیف مهند یکرم‬
  >>                                                         ‫سال ‪ ۹۲۳۱‬؛ درختان جنگلی تألف‬
  >>                ‫جنگل ارك درکلیداغی‬                     ‫دانشگاه تهران شمارة ‪ ) ۰۲‬سال ‪. ۹۲۳۱‬‬
  >>        ‫‪۰‬جنگل شناسی ‪ .‬کریم ساعی ج ‪ ۲‬ص‪> ۳۱۱‬‬
LEAF 51 printed~ 591
  >>            ‫‪.‬‬        ‫رفتار نداشته باشد‬     ‫نون وبای حطی هم‌بنظرآمده استکه جنگلالی‬
LEAF 124 printed~ 664
  >>                                                                  ‫بر‬    ‫=‬   ‫جنگلاهی‬
LEAF 173 printed~ 713
  >>           ‫ودولت کوچکی درآ نجاتأسیس کرد ‪ .‬ناحيةُ مزبور ازجنگلهای بسیارپوشيده بود ازبنرو اب ک‬
LEAF 437 printed~ 977
  >> ‫هموار و دربعض مواضع دارای درباچه‌ها وباتلاق‌ها ودربرخی امکنه پوشیده از جنگلهاست و در‬
LEAF 552 printed~ 1092
  >> ‫مکل زمین ودرختها وجنگلپا است ومصالح‬
LEAF 638 printed~ 1178
  >>                                                             ‫سند لی ‪ » ۲‬بروزن جنگلی »کرسیی‬
```


## [2026-09-06T15:27:20.273Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 -c \"\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nps=t.split('\\f')\nprint(ps[50])\n\""
}
```


### [2026-09-06T15:27:22.199Z] TOOL RESULT

```
   ‫سوت‬                                                                                ‫جنگه‬
‫و بیاض بزر که را حمگفته‌اند ‪ -‬و نومی‬   ‫است ‪-‬‬   ‫و کنکاش کردن جممی باشد باهم» گوبند‬       ‫است ‪-‬‬

                          ‫از قمار یز هت ‪.‬‬                                     ‫ترکی است ‪. ۷‬‬
‫ررچ»نگه را‬‫خگا‬
            ‫جنگار » بروزن زن‬                    ‫جنگ س بفتح اول وسکون‌نالی وکاف»‬
‫‪-‬تی فاعل ‪۴‬‬
         ‫بندمع‬‫وان‬
                ‫گوبند وبمربی‌سرطان خو‬             ‫عوم‬‫معروف است که جدال و قنال باشد ‪- ۴‬‬
 ‫اول شتربرا گوبندکه هنوز او را (‪ )۱‬بزیر بار | که جنگ آورنده باشدسوامرهم هست‪*. ۴ .‬‬
‫جنگ زر گری ه کنابه از جنگه‬                     ‫نکشیده باشند ‪ -‬و بمعنی کشتی و جپاز بزرکه‬
                          ‫ساختگی باشد ‪# .‬‬      ‫هم هت » و باین معتی باجيم فارسی نیزآمده‬




               ‫‪. - ٩‬آخون از ترکی ‪ :‬مشاورت جمعی با هم ‪ .‬ومجلس‌وانجمن «ناظ‌الاطباه»‪. ‎‬‬
   ‫کراست‪ .‬ک«لستان‪‎.»۷۲‬‬
                     ‫لعشیت‬
                         ‫؟ ‪ -‬باریت‌صلح کن‌وزجنكخصم ایمن‌نشین زآنکه شاهنشاء عادلرا ر‬
                     ‫‪ - ۴‬نی ‪ :‬جنك بيار وجنك کن‪. ‎‬‬            ‫‪ ۳‬مراد اسم فاعل است ‪.‬‬
       ‫*٭ جنگجو ‪ -‬فتح اول» رزم آور ؛ مبارژ ‪ ۰‬جنگی‪‎:‬‬          ‫‪#‬جنطیانا ‪ .‬رك‪ :‬جنطی‪.‬‬
                                                               ‫جنگجوبان پزور پنجه و کتف‬
                                                         ‫دشمنان را کشند وخوبان دوست‪.‬‬
                                                         ‫د کلتانع‪» ۳۱‬‬
                                                         ‫‪ #‬جنگل ‪ -‬بفتح اول و سوم »‬
                                                         ‫سانکربت ‪ «2128021‬اشتینگاس »‬
                                                         ‫لمه درژباتهای مختلف هندشمالی‬
                                                                                    ‫اکبن‬
                                                         ‫به‌منی‌اجم عربی‌بافنای بزر کی پوشیده‬
                                                         ‫استممال‌شود ‪ .‬همین کلمه در‬    ‫اکزون‬
                                                         ‫انگلسی سورت ‪ 618۵‬لا[ داخل شده‬
                                                         ‫است ‪ « .‬دائرقالمعارف اسلام ‪ °‬جنگل‬
                                                         ‫در زبان عادی مر زمین وسمی اطلاق‬
                                                        ‫نرا درختان خود رو فرا‬ ‫مشود آکه‬
                                                         ‫گرفته باشد » ولی در اصطلاح علفی‬
                                                         ‫جنگل مجموعة بزرگی‌است ازدرختان‬
                                                         ‫کویاهان که با بطور طبیعی روبیده‬
                                                         ‫یا پدست آدمی بوجرد آمده باشد ‪.‬‬
                                                         ‫رك‪ :‬جنگل‌شناسی تألیف مهند یکرم‬
                                                         ‫ساعی‌ج‪ ( ۱‬ازاتارات دانشگاه تهران‬
                                                        ‫س‪۲‬ا)ل ‪ ۷۲۳۱‬؛ نج ‪ ( ۲‬از‬   ‫شمارة ‪۳‬‬
                                                        ‫احثارات داشگاه تهران شمارة ‪) ۱۸‬‬
                                                        ‫سال ‪ ۹۲۳۱‬؛ درختان جنگلی تألف‬
                                                         ‫مهندس حبیب‌افه ثابتی ( از اتشارات‬
               ‫جنگل ارك درکلیداغی‬                     ‫دانشگاه تهران شمارة ‪ ) ۰۲‬سال ‪. ۹۲۳۱‬‬
       ‫‪۰‬جنگل شناسی ‪ .‬کریم ساعی ج ‪ ۲‬ص‪> ۳۱۱‬‬
```


## [2026-09-06T15:27:37.868Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AFA gubba ===\"; grep -n -i \"gubba\\|ǧubba\\|jubba\\|dschubbe\" AFA.txt | head -10\necho \"=== FVQ jubba ===\"; grep -n -i \"jubba\\|gubba\" FVQ.txt | head -10\necho \"=== AFM جبه ===\"; grep -n \"الجبة\\|جبة\" AFM_pages.txt | head -10\necho \"=== PLA ===\"; ls incoming/PLA 2>/dev/null; grep -rn -i \"jubba\" PLA*.txt 2>/dev/null | head\necho \"=== DEV jupe ===\"; grep -n -i \"^JUPE\\|jupon\" DEV.txt | head\necho \"=== LAM jupe ===\"; grep -n -i \"^JUPE\\|jupon\" LAM.txt | head\necho \"=== DOZ ===\"; grep -n -i \"jubbe\\|jupe\" DOZ.txt | head"
}
```


### [2026-09-06T15:27:37.982Z] TOOL RESULT

```
=== AFA gubba ===
=== FVQ jubba ===
=== AFM جبه ===
2947:ابيض وبالسر ܨܬ ܣܘܪܐ اي ابيض ٠‏ وقالت فيه العرب عر وجبة الى غير ذلك3 1 ܇ «
=== PLA ===
PLA_asbaghi_1988_ia_djvu.txt
PLA_asbaghi_1988_ia.pdf
PLA_pages.txt
(eval):5: no matches found: PLA*.txt
=== DEV jupe ===
1582:Jupe.   Esp.  juba,  chupa,  veste,   aljuba ;  portug.  aljuba.
3710:Jupe.
=== LAM jupe ===
7695:Jupe. De t^ goubba^ robe. (V. Dozy. Vêtements.)
9206:Jupe
=== DOZ ===
```


## [2026-09-06T15:27:40.093Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN jangal ===\"; grep -n -i \"jangal\\|dschangal\" HRN.txt | head\necho \"=== HUB jangal ===\"; grep -n -i \"jangal\\|dschangal\" HUB.txt | head\necho \"=== ARY جنگل ===\"; grep -n \"جنگل\" incoming/ARY/ARY_pages.txt | head\necho \"=== ARY جمل/جبه ===\"; grep -n \"^\\s*جبه\\|جُبّه\" incoming/ARY/ARY_pages.txt | head\necho \"=== HJB jungle ===\"; grep -n -i \"^JUNGLE\" HJB.txt | head\necho \"=== SYN camel/forest ===\"; grep -n -i \"kamelos\" SYN.txt | head"
}
```


### [2026-09-06T15:27:40.205Z] TOOL RESULT

```
=== HRN jangal ===
=== HUB jangal ===
=== ARY جنگل ===
12894:۲ این واژه در برخی زبان‌های اسلاوی چم "جنگل" و "کوه" راهم دارد.
=== ARY جمل/جبه ===
=== HJB jungle ===
12246:JUNGLE.
12248:JUNGLE-FOWL.
12274:JUNGLE-FOWL,  s.  The  popular name  of  more  than  one  species  of  thdae
12275:JUNGLE-MAHALS.
12282:JUNGLE-MAHALS,  n.^).  Hind. JangcU-Mahdl.  This,  originally  a va^e  name  of  sundry  tracts  and chieftainships  lying  between  the  settled districts  of  Bengal  and  the  hill  country of  Chuti&  Nagpur,  was  constituted  a regular  district  in  1805,  but  again broken  up  and  redistributed  among adjoining  districts  in  1833  (see  Imperial GaaeUeeTy  s.y.).
12283:JUNGLE-TEBBT,  n.p.  Hind. Jangcd-iardi  (see  TERAI).  A  name formerly  applied  to  a  border-tract between  Bengal  and  Behar,  including the  inland  parts  of  Monghyr  ana Bha^lpur,  and  what  are  now  termed the  Santdl  Pargands.  Hodges,  below, calls  it  to  the  "westward"  of  Bhasal- pur ;  but  Barkope,  which  he  describes as  near  the  centre  of  the  tract,  lies, according  to  Rennell's  map,  about 36  m.  S.£.  of  Bha^l^ur  town ;  and the  Cleveland  inscription  shows  that the  term  included  the  tract  occu- pied by  the  Rajmshal  hOl-people. The  Map  No.  2  in  Rennell's  Bengal Atlas  (1779)  is  entitled  "the  Jnngle- teny  District,  with  the  adjacent provinces  of  Birbhoom,  Eajemal,  Bogli- pour,  &c.,  comprehending  the  countries situated  between  Moorahedabad  and Bahar."  But  the  map  itself  does  not show  the  name  Jungle  Terry  anywhere.
=== SYN camel/forest ===
```


## [2026-09-06T15:27:47.435Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HJB ===\"; sed -n '12246,12274p' HJB.txt\necho \"=== DEV ===\"; sed -n '1578,1600p' DEV.txt\necho; echo \"=== HJB leaf ===\"; python3 -c \"\nt=open('HJB.txt',encoding='utf-8',errors='replace').read()\nps=t.split('\\f')\nfor i,p in enumerate(ps):\n    if 'JUNGLE-MAHALS' in p: print('leaf',i); break\n\"\necho \"=== DEV leaf ===\"; python3 -c \"\nt=open('DEV.txt',encoding='utf-8',errors='replace').read()\nps=t.split('\\f')\nfor i,p in enumerate(ps):\n    if 'Esp.  juba,  chupa' in p: print('leaf',i,'printed~',i-30); print(p[:200]); break\n\""
}
```


### [2026-09-06T15:27:49.385Z] TOOL RESULT

```
=== HJB ===
JUNGLE.
470
JUNGLE-FOWL.
was  not  at  first  continuous,  nor  have the  chiefs,  even  when  of  African  blood, been  always  of  one  family ;  but  they have  apparently  been  so  for  the  last aOO  years.  'The  SidV  (see  SEEDY) and  'The  HcMiiy*  are  titles  popularly applied  to  this  chief.  This  State  has a  port  and  some  land  in  E&thiawar. Gen.  Keatinge  writes:  "The members  of  the  Sidi's  family  whom I  saw  were,  for  natives  of  India, particularly  fair."  The  old  Portuguese writers  call  this  harbour  Danda  (or  as they  write  it  Damda)^  e.g,  Jofto  de Castro  in  Primeiro  Roteiro,  p.  48.  His rude  chart  shows  the  island-fort.
'  JUNGLE,  s.  Hind,  and  Mahr. jcmgal^  from  Skt.  jangala  (a  word which  occurs  chiefly  in  medical treatises).  The  native  word  means in  strictness  only  waste,  uncultivated ground ;  then,  such  ground  covered with  shrubs,  trees  or  long  grass ;  and thence  again  the  Anglo-In£an  appli- cation is  to  forest,  or  other  wild {growth,  rather  than  to  the  fact  that it  is  not  cultivated.  A  forest ;  a thicket;  a  tangled  wilderness.  The word  seems  to  have  passed  at  a  rather early  date  into  Persian,  and  also  into use  in  Turkistan.  Prom  Anglo- Indian  it  has  been  adopted  into French  as  well  as  in  EngiifQi.  The word  does  not  seem  to  occur  in Fryer^  which  rather  indicates  that its  use  was  not  so  extremely  common among  foreigners  as  it  is  now.
c.  1200.—".  .  .  Now  the  land  is  humid, Juni^e  ijancalah),  or  of  the  ordinary  kind." SusruiOy  1.  ch.  85.
o.  1870. — "Elephants  were  numerous  as sheep  in  the  Jaacal  round  the  R^'s  dwell- vag.'^—TdHkh-i-Flroz-Skdki.  in  BUiot,  in. 814.
c.  1450.— "The  Kings  of  India  hunt  the elephant.  Thev  will  stay  a  whole  month or  more  in  the  wilderness,  and  in  the jnngle  {Janffoiy—Abdurmzdhf  in  Not.  et Ext.  xiy.  51.
1474. — " .  .  .  Bicheneger.  The  vast  city is  surrounded  by  three  ravines,  and  inter- sected by  a  river,  bordering  on  one  side  on a  dreadful  3juigtl"—Atk/lfikUin,  in  India %%XVtkCaU^.
1776. — "Land  waste  for  five  years  .  .  . is  called  Jungle."— ^a/A«tf'«  Oenioo  Code, 190.
1809.  —  "The  air  of  Calcutta  is  much affected  by  the  closeness  of  the  jusffle around  if'—Xrf.  VaUtUia,  i.  207,
1809.— "They  built  them  here  a  bower  of  jointed cane, Strong  for  the  needful  use,  and  lid^t  and
long Was  the  slight  fnmeworic  rsar'd,  with
little  pain; lithe  creepers  then  the  wicker  aides  supply. And  the  tall  Jungle  grass  fit  roofing  gave Beneath  the  genial  sky."
OvTu  qfKtkmma,  xm.  7. o.  1880.—"  (Test  Ik  qlie  je  renoontnu  las Jungles  .  .  .  j'avoue  one  je  fus  tr^  dtep- points." — JacqwemorUf  Correspond,  i.  184.
c.  1888^8.— "  L'Hippotame  an  laige  ventre Habite  aux  Jungles  de  Java, Oh  grondent,  au  fond  de  chaque  antra Plus  de  monstres  qu'on  ne  rftva."
Theoph.    OAvtiett    in    Pdsia  (Jom- pUtet,  ed.  1876,  L  325. 1848.— "But  he  was  as  lonely  here  as  in leywala."  —  Thadunaf^
his  Jungle  at  Boj^Xv^ VanitylFaiTf  ch.  iii.
„  "  *  Was  there  ever  a  battle  won  like Salamanca?  Hey,  Dobbin?  But  where  was it  he  learnt  his  art?  In  India,  my  boy. The  Jnngle  is  the  school  for  a  general,  mark me  that/"— /&u<.,  ed.  1868,  i.  312.
c.  1868.— "  La  b^te  formidable,  habitante  destaigles S'endort,  le  ventre  en  I'air,  et  duate  sea ongles." — LeconU  de  Liile.
" 'f^  djnngles  du  Pendj-Ab    * Aux  sables  du  Kamate." — Ibid.
1865.— "To  an  eye  accustomed  for  years to  the  wild  wastes  of  the  Jnngie,  the  whole country  presents  the  appearance  of  one  con- tinuous well-ordered  garden." —  Warimff^ Tropical  RetidetU  at  Mome,  7.
1867.—".  .  .  here  are  no  cobwebs  of  plea and  oounterplea,  no  Jnngles  of  argument and  brakes  of  analysis." — StrinJbvme,  Ftmy» and  Studiesy  183.
1873. — "Jnngle»  derived  to  us,  through the  living  language  of  India,  from  the Sanskrit,  may  now  be  regarded  as  good English.^'  —  FUz  -  Edwatrd  Hall,  Modem English,  306.
1878.— "Cet  animal  est  oommun  dans  lea fordts,  et  dans  les  djengles."— ifiorrv,  Kator Kata-Malayou,  83.
1879.— "The  owls  of  metaphydca  hooted from  the  gloom  of  their  various  Jungles." — Fortnightly  Rev.  No.  clxv.,  N.S.,  19.
JUNaiiE-FEVEB,  s.  A  danger- ous remittent  fever  arising  from  the malaria  of  forest  or  jungle  tracts.
1808.— "I  was  one  day  sent  to  a  great distance,  to  take  charge  of  an  officer  who had  been  seized  by  Jnngle-fiSTer."— Letter in  Morion* s  L.  qf  Leyaen,  43.
JUNGLE-FOWL,  s.  The  popular name  of  more  than  one  species  of  thdae
=== DEV ===
Irompctle,  au  son  do  hujuello  on  annonçait  l'ajinée  du jubilé,  '^S'T'  ^ép  clienalh  lin-ijohel.
JuBis,  Terme  de  commerce.  Raisins  secs  en  caisse.  C'est une  altération  de  l'arabe  L^-y^'^  zebib,  raisin  sec,  comme  le prouvent  les  vieilles  formes  azebit,  auzibet  :  «  Pro  cargua de  azebits  seu  racemis,  ?5  dit  un  vieux  tarif  de  Carcassonne, cité  dans  Du  Gange.  Ces  dernières,  ainsi  que  l'espagnol nzebibe,  acebibr,  ont  gardé  l'article  al^  dont  le  l  s'assimile au  z  suivant  :  az~zebïb.  En  portugais,  acipipe  a  pris  une  si- gnification plus  générale,  celle  de  menues  friandises  propres à  aiguiser  rappétit,  à  rafraîchir.  Diverses  contrées  musul- manes, ne  buvant  pas  de  vin,  livraient  leurs  raisins  séchés au  commerce,  et  cet  aliment  était  fort  estimé  des  Arabes; Razi  le  regarde  comme  plus  nutritif  que  la  datte  :  «-.vH>y^ A^-o  t «xil^  ^^yï]  -«Oi  J^Xi  IX  ^ô^j^_  ^  ff  Le  raisin  sec  n'obstrue point  comme  fait  la  datte,  bien  que  plus  nourrissant qu'elle.:)?  (M an.  arabe  déjà  cité,  fol.  63  verso.)
JuGKOLrNE.  —  Voy.  Gengél[.
JuLEP.  Esp.  et  portug.  jidepe;  ital.  giulebbo,  giidebbe; bas  latin ,  julapium.  De  l'arabe-persan  <-->!^:^  djoulâb  ou djoullâb,  qui  a  le  même  sens,  cdls  font  une  potion.  .  . (ju'ils  donnent  au  malade  et  qu'ils  appellent.  ..  jW^/>, c'est-à-dire  eau  bouillie,  mot  d'où  il  y  a  assez  d'apparence qu'est  venu  celui  de  jiilep,  dont  nous  nous  servons,  j? (Chardin  ^)  Le  persan  djoulâb  ou  goulâb,  c.»!^,  est  formé de  J^  poul,  rose,  et  lj\  ab,  eau;  goulâb  signifie,  en  effet, eau  de  rose,  mais  se  dit  aussi  de  plusieurs  autres  prépara- lions.  Cf.  Sacy,  AbdaUaiif,  p.  317,  note  iîî.
Jupe.   Esp.  juba,  chupa,  veste,   aljuba ;  portug.  aljuba.
'    Voyage  en  Perse,  ôd.  Smith,  p.  33-3.
DES  MOTS  D'ORIGINE  OIUENTALE.  \lil
casai|iie  moresque;  ital.  gruppn.  De  l'arabe  iC.:^  (Ijoahha. (Voy.  Dozy,  Dkt.  des  vêt.  p.  107.)  cd^ar-dessus  le  caftan, les  Turcs  mettent  une  jitppe  ou  surtout  à  manches  très- courtes.  57  (Niebuhr,  Voy.  en  Arah.  p.  a  10.)
K
Kabin.  Somme  payée  par  le  mari  musulman  à  la  femme qu'il  répudie.  Le  mot  s'est  dit  aussi  des  mariages  tempo- raires contractés  par  les  marins  provençaux  avec  des  femmes grecques  dans  l'Archipel.  (Littré.)  Du  persan  (^^yjl^  k/lhlu . même  sens.
Kabvle.   Nom  tiré  de  l'arabe  <xAjuj^  qahila,  tribu.
Kadelée.  Espèce  de  haricot  de  la  Malaisie  (^Phaseohis maximus,  cadelium  de  Rumpf).  C'est  le  javanais  fm^STîrL»
hadelé,  en  malais  JJsi  kedeli.  Nos  dictionnaires  de  bota- nique donnent  les  variantes  cadali,  kadali,  cadeli.
Kadiine.  «Mot  qui  signifie  dmne  en  turc  et  se  dit  des maîtresses  en  pied  du  sultan,  w  (Littré.)  Le  turc  ^:>li  qâdin est  une  altération  de  ^yU»-  hhâtoûn,  dame,  maîtresse  de maison.
Kadoche.   Grade   élevé  dans  la   franc-maçonnerie.   De l'hébreu  î^*np^rïJôc/i,  saint,  sacré  (^^ij)qadacli,  être  saint,  , en  arabe  ^<XJj  qadas).
Kaïmac.  Sorte  de  sorbet  turc.  Le  mot  turc  (^i  ou  (^}:i qdimnq  signifie  proprement  crème  du  lait.
Kalpak.  Bonnet  a  la  tarlare,  est  le  m��me  mot  turc  que le  colback.  (Voy.  ce  mol.)
1  o.
ï
J/i8  DICTIONNAIRE  ETYMOLOGIQUE
Kaivchil.  Chevrotaiii  des  forets  de  Sumatra.  (Bouiilet, Scienc.)  En  malais  J^ss^S  hantchl,  moschus  Javanicus.
Kava.  Boisson  enivrante  des  Polynésiens.  ç^Il  y  a  iden- tité entre  ce  mot  et  le  mot  havoua,  café  des  Arabes,  qui se  prononce  de  la  même  manière.  Ces  deux  boissons  sont servies  cbaudes.  ^^  (Rienzi^.)  —  Voy.  Café.
Kazine.  Trésor  du  Grand-Seigneur.  De  l'arabe  io->y^ hhazïnn ,  venant  de  la  même  racine  qui  a  donné  magasin.

=== HJB leaf ===
leaf 522
=== DEV leaf ===
leaf 181 printed~ 151
b,  eau;  goulâb  signifie,  en  effet, eau  de  rose,  mais  se  dit  aussi  de  plusieurs  autres  prépara- lions.  Cf.  Sacy,  AbdaUaiif,  p.  317,  note  iîî.
Jupe.   Esp.  juba,  chupa,  veste,
```


## [2026-09-06T15:28:06.845Z] TOOL CALL #24: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-06T15:28:06.851Z] TOOL RESULT

```


```


## [2026-09-06T15:28:10.324Z] TOOL CALL #25: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/camel",
 "prompt": "Give the full etymology section for English camel: Middle English, Old English/Old North French, Latin camelus, Greek kamelos, and which Semitic source (Phoenician, Hebrew gamal, Arabic jamal) is named."
}
```


## [2026-09-06T15:28:11.256Z] TOOL CALL #26: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/camel",
 "prompt": "Full etymology of camel: Old English/Old North French/Old French forms (chamel, chameal), Latin camelus, Greek kamelos, Semitic source (Hebrew gamal, Phoenician, Arabic jamal)."
}
```


### [2026-09-06T15:28:16.606Z] TOOL RESULT

```
# Etymology of English "Camel"

Based on the Wiktionary entry, here's the etymological path:

**Modern English** derives from **Middle English** *camel*, which came through **Old English** *camel* and **Old Northern French** *camel* (with Old French *chamel*, modern French *chameau*).

These Romance forms trace back to **Latin** *camēlus*, which was borrowed from **Ancient Greek** *κάμηλος* (kámēlos).

The Greek word itself came from a **Semitic source**, ultimately tracing to **Proto-Semitic** *\*gamal-*. The entry specifically notes comparisons to:

- **Arabic** *جَمَل* (jamal)
- **Hebrew** *גמל* (gamál)
- **Aramaic** *ܓܡܠܐ* (gamlā)
- **Coptic** *ϭⲁⲙⲟⲩⲗ* (čamoul)

The word entered European languages through the Mediterranean trade routes, passing from Semitic languages into Greek, then Latin, and finally into Romance and Germanic languages.
```


### [2026-09-06T15:28:18.297Z] TOOL RESULT

```
# Etymology of Camel

The word "camel" has an interesting linguistic journey across multiple languages and cultures.

## Origin Path

The term entered English through Old English _camel_, likely via Old North French _camel_ (from Old French _chamel_). It ultimately derives from Latin _camelus_, which came from Greek _kamelos_, with Semitic roots including Hebrew _gamal_ and Arabic _jamala_ meaning "to bear."

## Historical Linguistic Confusion

Interestingly, an earlier Old English word for the animal was _olfend_, which reflected a common confusion between camels and elephants. As the source notes, "The confusion was general in the older Germanic languages," appearing in Gothic, Old High German, Old Saxon, and Old Norse variants.

## Related Terms

The word spawned related vocabulary:
- **Camelopard**: An archaic name for giraffe, literally combining camel and leopard references due to the animal's long neck and spotted coat
- **Dromedary**: Specifically the single-humped Arabian camel bred for riding, from Greek meaning "running camel"

The two distinct camel species remain the one-humped Arabian variety and the two-humped Bactrian.
```


## [2026-09-06T15:28:24.735Z] TOOL CALL #27: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%BA%CE%AC%CE%BC%CE%B7%CE%BB%CE%BF%CF%82",
 "prompt": "Etymology of Ancient Greek κάμηλος: which Semitic language is named as the direct source (Phoenician, Hebrew, Aramaic, Arabic)? Quote it. Also any note by Beekes."
}
```


## [2026-09-06T15:28:26.955Z] TOOL CALL #28: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AC%D8%A8%D8%A9",
 "prompt": "Etymology of Arabic جُبَّة (jubba) 'long outer garment': is it from root ج ب ب 'to cut', or a loanword (Aramaic, Greek)? Also list descendants (Spanish aljuba/juba, Italian giubba, French jupe, Persian جبه)."
}
```


### [2026-09-06T15:28:29.835Z] TOOL RESULT

```
Based on the Wiktionary content provided, the etymology section does **not name a specific Semitic language as the direct source**. Instead, it traces the word to "Proto-West Semitic" and then provides comparisons:

The article states the word comes "Ultimately from Proto-West Semitic *gamal-; compare Arabic جَمَل (jamal) and Hebrew גָּמָל (gāmā́l)."

These are comparative examples rather than identification of a single direct source language. The entry does not specify whether Phoenician, Aramaic, or another Semitic language served as the immediate etymological source for the Ancient Greek term.

Regarding Beekes' note: The reference cites his *Etymological Dictionary of Greek* (2010) but provides no direct quotation of his commentary on this particular etymology in the visible content.
```


### [2026-09-06T15:28:32.775Z] TOOL RESULT

```
# Etymology of جبة (jubba)

According to the Wiktionary entry, the word جبة derives "From the root ج ب ب (j b b) meaning 'to cut', 'to carve a well or cistern'." The etymology explains that the secondary sense of "to surround" and "to envelop" emerged from imagery of encircling a well.

The entry traces this further back to "Proto-Semitic *gbb ('to bend, curve, cut')," suggesting a native Semitic origin rather than a loanword from Greek or Aramaic.

## Notable Descendants

The word dispersed widely across Mediterranean and European languages:

- **Romance languages**: Spanish *aljuba/juba*, Italian *giubba*, French *jupe*
- **Slavic languages**: Polish *żupan*, Russian *жупан*, Czech *župan*
- **Turkic languages**: Ottoman Turkish *çapan*, Uzbek *chopon*
- **Other languages**: Persian *جبه*, English *jubbah*, Malay *jubah*

This linguistic distribution reflects medieval trade routes and cultural contact between Arabic-speaking regions and Europe.
```


## [2026-09-06T15:28:44.428Z] TOOL CALL #29: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/jungle",
 "prompt": "Full etymology of English jungle: Hindi/Hindustani jangal, Sanskrit जङ्गल (jaṅgala), date of first English attestation, and any note on Persian."
}
```


## [2026-09-06T15:28:45.134Z] TOOL CALL #30: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/jupe",
 "prompt": "Etymology of French jupe and jupon: is it from Italian giubba, Spanish aljuba/juba, or directly Arabic جبة? Quote the etymology exactly. Also English jupon."
}
```


### [2026-09-06T15:28:50.406Z] TOOL RESULT

```
# Etymology of English "Jungle"

**Origin Chain:**
The word "jungle" entered English from Hindustani (Hindi/Urdu), which borrowed it from Sanskrit जङ्गल (*jaṅgala*), meaning "arid or sterile region, desert." The Sanskrit term itself derives from a substrate language of unknown origin.

**First English Attestation:**
According to the Wiktionary entry, jungle "first appears c. 1776 in a translation by Nathaniel Halhed."

**Persian Connection:**
The etymological path shows the word traveled through Indo-Aryan languages (Sanskrit → Prakrit → Hindi/Urdu) rather than through Persian, though Persian جَنْگَل (*jangal*) does exist as a cognate in that language family.

The semantic evolution from "desert/wasteland" in Sanskrit to the modern sense of "dense tropical rainforest" reflects how the term was adapted by English speakers encountering actual jungles in colonial India.
```


### [2026-09-06T15:28:51.867Z] TOOL RESULT

```
# Etymology of "Jupe" and Related Terms

## French "jupe"
According to the Wiktionary entry, the French word derives as follows:

"Inherited from Middle French *jupe*, from Old Italian *giubba*, from Arabic *جُبَّة* (jubba, 'long garment')."

The etymology traces the word through Italian as an intermediate source rather than directly from Arabic.

## English "jupe"
The English term follows a similar path: "From Middle English *jupe*, from Middle French *jupe*."

## Note on "jupon"
The Wiktionary article lists "jupon" as a derived term from French *jupe* but does not provide a separate etymology. The entry does not mention Spanish *aljuba* or *juba* as alternative sources in the documented material provided.

The documented etymology consistently shows the transmission route as: Arabic → Old Italian → Middle French → English/French, rather than presenting competing theories about direct Arabic transmission or Spanish intermediation.
```


## [2026-09-06T15:29:03.848Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://www.cnrtl.fr/etymologie/jupe",
 "prompt": "Give the TLFi/CNRTL etymology of French 'jupe' and 'jupon' verbatim: which language is the immediate source (Italian giubba? Sicilian? Spanish aljuba? Arabic djubba?), first attestation date."
}
```


## [2026-09-06T15:29:05.425Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%DA%98%D9%88%D9%BE%D9%86/",
 "prompt": "Does Persian ژوپن / ژوپ / مینی ژوپ appear? Give the definitions and any etymology (French jupon) from Dehkhoda or Moin."
}
```


### [2026-09-06T15:29:08.553Z] TOOL RESULT

```
I cannot provide the TLFi/CNRTL etymology information you've requested because the webpage content provided contains only a header "Portail lexical" without the actual etymological data for 'jupe' and 'jupon'.

To obtain the specific etymological details you're seeking—the immediate source language, whether it's Italian, Sicilian, Spanish, or Arabic, and the first attestation dates—you would need to access the full TLFi/CNRTL dictionary entries directly through their website or database.
```


### [2026-09-06T15:29:12.576Z] TOOL RESULT

```
# ژوپن - Dictionary Entry

Yes, the Persian term **ژوپن** appears on this Abadis Dictionary page.

## Definitions Provided:

**Farhangi-ye Farsi:** "دامن کوتاه، شلیته" (short skirt, petticoat)

**Farhangi-ye Moein:** "دامن کوتاه، پاچین (زنان)" (short skirt, women's garment)

**Farhangi-ye Amid:** "دامن کوتاه و آهاردار" (short and pleated skirt)

## English Equivalent:

The page lists "half-slip" as the English translation, describing it as "زیر پیراهنی، ژوپن یا زیر پوش زنانه" (an undergarment/slip for women).

## Etymology:

The page does not provide etymological information or mention the French origin "jupon" for this entry. While the page references both Dehkhoda and Moein dictionaries as part of its database, the specific etymological details you requested are not included in the displayed content.
```


## [2026-09-06T15:29:15.922Z] TOOL CALL #33: WebSearch

```json
{
 "query": "CNRTL jupe étymologie \"ital. giubba\" OR \"aljuba\" arabe djubba 1297"
}
```


## [2026-09-06T15:29:16.974Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/jupon",
 "prompt": "Etymology of jupon and jupe in English: Old French jupe/jupon, Arabic jubbah, any mention of Spanish aljuba or Italian giubba."
}
```


### [2026-09-06T15:29:21.982Z] TOOL RESULT

```
# Etymology of Jupon and Jupe

Based on the Etymonline content provided, the words **jupon** and **jupe** trace their origins through a linguistic path crossing multiple languages:

The English terms derive from **Old French jupe/jupon**, which ultimately come from **Arabic jubbah**. The etymology note also references related forms in **Spanish (aljuba)** and **Italian (giubba)**, suggesting a broader Mediterranean linguistic influence.

This etymological chain reflects historical contact and trade between European and Arabic-speaking regions, with the garment term traveling westward through cultural and commercial exchange.
```


### [2026-09-06T15:29:23.937Z] TOOL RESULT

```
Web search results for query: "CNRTL jupe étymologie "ital. giubba" OR "aljuba" arabe djubba 1297"

Links: [{"title":"Littré - jupe - définition, citations, étymologie","url":"https://www.littre.org/definition/jupe"},{"title":"Jupe | Définition du dictionnaire français","url":"https://www.dicocitations.com/definition_littre/15582/Jupe.php"},{"title":"JUPE : Etymologie de JUPE","url":"https://www.cnrtl.fr/etymologie/jupe"},{"title":"Jupe traduction jupe définition jupe dictionnaire","url":"https://fr.thefreedictionary.com/jupe"},{"title":"jupe | Dictionnaire de l’Académie française | 9e édition","url":"https://www.dictionnaire-academie.fr/article/A9J0381"},{"title":"Définition de jupe | Dictionnaire français","url":"https://www.lalanguefrancaise.com/dictionnaire/definition/jupe"},{"title":"Dérivés russes de l'arabe Djoubbah - Persée","url":"https://www.persee.fr/doc/slave_0080-2557_2001_num_73_1_6701"},{"title":"Jupa | Etymologie-occitane","url":"https://www.etymologie-occitane.fr/2011/06/jupa-2/"},{"title":"Quel est l'origine du mot jupe ?","url":"https://www.synonyme-du-mot.com/les-articles/quel-est-lorigine-du-mot-jupe"},{"title":"Centre national de ressources textuelles et lexicales","url":"https://en.wikipedia.org/wiki/Centre_national_de_ressources_textuelles_et_lexicales"}]

Based on the search results, here's what I found regarding the etymology of "jupe":

The word "jupe" comes from Provençal "jupa," Catalan from the 13th century "aljuba," Italian "giubba" or "jupa," which derives from Arabic "jubbet" (meaning "short pelisse").

More specifically, the Arabic "djoubba(h)" or "djibba(h)" may have passed through Sicily to enter the Romance languages, though the word "aljuba" was assimilated directly from Moorish Arabic.

Very ancient attestations from the 10th-11th century show that the Arabic word was probably introduced along with the garment via Sicily to Italy and then to France in two forms—with -u- and with -i-. In the Iberian Peninsula, only the -u- form is found: "aljuba," which was borrowed directly from Arabic.

Regarding the specific date reference in your query (1297), while my search results mention various historical attestations, they don't provide a specific reference to 1297 in connection with the CNRTL etymology entry for "jupe."


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-06T15:29:33.429Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nfor f in ['BQT_v2_pages.txt']:\n    t=open(f,encoding='utf-8',errors='replace').read()\n    ps=t.split('\\f')\n    for i,p in enumerate(ps):\n        for w in ['جبه','جمل ']:\n            if w in p and i<120:\n                for m in re.finditer(r'.{0,60}'+w+r'.{0,120}',p):\n                    s=m.group(0).replace('\\n',' ')\n                    print(f,'leaf',i,'printed~',i+540,'|',s)\nEOF"
}
```


### [2026-09-06T15:29:35.203Z] TOOL RESULT

```
BQT_v2_pages.txt leaf 22 printed~ 562 | ‫جبه هزار میخی ‪ -‬کنابه ازفلك‬                                                ‫ثویند ‪.‬‬   ‫بری‬   ‫سم‬
BQT_v2_pages.txt leaf 34 printed~ 574 |     ‫« جفبوت » پنْبةٌ باشد که در جبه و قبازده باشد و از آنجا باز گرفته » رود کیگفت ‪:‬‬
BQT_v2_pages.txt leaf 44 printed~ 584 | ‫واک مزر بان آندازن کرای بکو‬                         ‫مقوط جبهه باشد و در چهاردهم سقوط زبره‬
BQT_v2_pages.txt leaf 65 printed~ 605 |  .‬وآن‌گاه به ”ش‪٣‬‏ و گاه به « ز >‬     ‫وجودندارد ودر حاب جمل ماد جم آبرا سه مصوب‬
BQT_v2_pages.txt leaf 77 printed~ 617 |    ‫وشمبده‌های اودرازست ‪ « ».‬مجمل التواریخ والقصص ‪ 4۳۳-۵۳‬و « أبن مقنع > بجای«م‪.‬قتم»غاعلی‬
BQT_v2_pages.txt leaf 107 printed~ 647 |                                  ‫ارمنی ‪( 62۳26‬پیشانی ‪ ,‬جبهه) « اسفا ‪ ۲ :۱‬ص‪.* ۳۹۱‬‬
```


## [2026-09-06T15:29:52.426Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/camel' --note 'page 228, root Jamal, English camel < ONF camel < L camelus < Gk kamelos < Proto-West Semitic *gamal-' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/camel' --note 'page 228, root Jamal, camel chain OE/ONF camel, OF chamel, L camelus, Gk kamelos, Heb gamal / Arab jamala' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%CE%BA%CE%AC%CE%BC%CE%B7%CE%BB%CE%BF%CF%82' --note 'page 228, node Greek kamelos: from Proto-West Semitic *gamal-, cf. Arabic jamal, Hebrew gamal' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%AC%D8%A8%D8%A9' --note 'page 228, root J.b.b: Arabic jubba from root j-b-b to cut, Proto-Semitic *gbb; descendants Sp aljuba, It giubba, Fr jupe, Pers jobbe' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/jungle' --note 'page 228, root Jangalah: English jungle < Hindustani jangal < Sanskrit jangala, first attested c.1776 Halhed' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/jupe' --note 'page 228, node French jupe: from Old Italian giubba, not Spanish' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/jupon' --note 'page 228, node English jupon/jupe < OFr jupe/jupon < Arabic jubbah' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://abadis.ir/fatofa/%DA%98%D9%88%D9%BE%D9%86/' --note 'page 228, node Persian zhup/zhupan: Moin and Amid give ژوپن damane kutah, French loan' 2>&1 | tail -3"
}
```


### [2026-09-06T15:29:58.508Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/1ad35a8f52692526.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0aeb9ac7ab9be5d3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6736e2910d2866dc.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3ea0e0d4db8598c6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/48c6ecc562764c5b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/58fca61b928990c1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0cfdcdd41286602b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b4058edfece18a95.txt
```


## [2026-09-06T15:30:03.417Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://www.littre.org/definition/jupe",
 "prompt": "Give Littré's etymology of jupe verbatim (provençal jupa, catalan aljuba, italien giubba, arabe djobbah)."
}
```


## [2026-09-06T15:30:04.380Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AC%D9%86%DA%AF%D9%84",
 "prompt": "Etymology of Persian جنگل (jangal) 'forest': from Sanskrit/Hindustani jangala? Quote the etymology and any note about borrowing direction."
}
```


### [2026-09-06T15:30:06.169Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T15:30:11.155Z] TOOL RESULT

```
# Etymology of Persian جنگل (jangal)

According to the Wiktionary entry, Persian جنگل is described as:

> "Borrowed from Hindustani (Hindi جंगल / Urdu جَن٘گَل), from Sauraseni Prakrit, from Sanskrit جङ्गल (jaṅgala, 'arid or sterile region, desert'), from a substrate language."

The key note about borrowing direction is that Persian **borrowed** this term from Hindustani languages rather than inheriting it directly from Sanskrit. This contrasts with Urdu, which **inherited** the word from Sauraseni Prakrit and Sanskrit.
```


## [2026-09-06T15:30:18.087Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AC%D9%85%D9%84",
 "prompt": "Is there a Persian section for جمل? Give the Persian etymology (borrowed from Arabic جَمَل jamal 'camel') and the Arabic entry's etymology."
}
```


## [2026-09-06T15:30:19.159Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Semitic/gamal-",
 "prompt": "Give the Proto-Semitic *gamal- 'camel' reconstruction, descendants (Arabic jamal, Hebrew gamal, Phoenician, Aramaic gamla), and any note about the Greek borrowing."
}
```


### [2026-09-06T15:30:22.966Z] TOOL RESULT

```
# Persian جمل

No, there is no Persian section in this Wiktionary entry. The page lists "فارسی" (Persian) among the 27 languages with entries for this term, but the actual Persian content is not displayed in the provided text.

## Etymology Information Available

For Arabic جَمَل (jamal, "camel"), the entry states: "Inherited from Proto-West Semitic *gamal-" This Proto-West Semitic root would logically be the ultimate source for Persian borrowings as well, following typical patterns where Persian borrowed animal terminology from Arabic.
```


### [2026-09-06T15:30:24.997Z] TOOL RESULT

```
# Proto-West Semitic *gamal- "Camel"

**Reconstruction:** The proto-form is *gamal-, reconstructed for Proto-West Semitic and conventionally attributed to Proto-Semitic, though noted as "likely a _Wanderwort_ of Arabian (possibly Arabic) origin."

**Key Descendants:**
- Arabic: jamal (جَمَل)
- Hebrew: gamál/gāmāl (גָּמָל)
- Phoenician: gml (𐤂𐤌𐤋)
- Aramaic: gamla (various scripts and dialects)

**Greek Borrowing:** The word entered Ancient Greek as κάμηλος (kámēlos) through Phoenician transmission, subsequently spreading to Latin (camēlus) and Romance languages.

The extensive descendant list demonstrates the term's widespread adoption across Semitic languages and its significant influence on neighboring language families, including Cushitic, Berber, and Georgian language groups.
```


## [2026-09-06T15:30:34.943Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%AC%D9%86%DA%AF%D9%84' --note 'page 228, node Persian jangal: borrowed from Hindustani, from Sanskrit jangala' 2>&1|tail -2\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%AC%D9%85%D9%84' --note 'page 228, node Persian jamal: Arabic jamal inherited from Proto-West Semitic *gamal-' 2>&1|tail -2\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Semitic/gamal-' --note 'page 228, root Jamal: Proto-West Semitic *gamal-, Greek kamelos via Phoenician gml' 2>&1|tail -2\necho \"=== MON grep ===\"\ncd data/verification/sources/refs\ngrep -c . MON_part1.txt MON_part2.txt\npython3 - <<'EOF'\nimport re\nfor f in ['MON_part1.txt','MON_part2.txt']:\n    t=open(f,encoding='utf-8',errors='replace').read()\n    for w in ['جنگل','ژوپن','جبه']:\n        c=len(re.findall(w,t))\n        print(f,w,c)\nEOF"
}
```


### [2026-09-06T15:30:38.156Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/ac23cc207424cc73.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9f4817c6a1249123.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/aea6c0004a6ca087.txt
=== MON grep ===
MON_part2.txt:75975
MON_part1.txt:78085
MON_part1.txt جنگل 46
MON_part1.txt ژوپن 0
MON_part1.txt جبه 40
MON_part2.txt جنگل 30
MON_part2.txt ژوپن 0
MON_part2.txt جبه 28
```


## [2026-09-06T15:30:43.004Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('MON_part1.txt',encoding='utf-8',errors='replace').read()\n# find headword-like context\nfor m in re.finditer(r'.{0,120}جنگل.{0,200}',t):\n    s=m.group(0).replace('\\n',' ')\n    if 'سنسکریت' in s or 'هندی' in s or 'jang' in s or 'Skt' in s or 'jungle' in s.lower():\n        print('>>',s); print()\nfor m in re.finditer(r'.{0,100}جُبّه|.{0,100}جبه \\[.{0,200}',t):\n    print('J>',m.group(0).replace('\\n',' ')[:250])\nEOF"
}
```


### [2026-09-06T15:30:45.219Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T15:30:52.008Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%AC%D9%85%D9%84/",
 "prompt": "Persian جمل: give the Dehkhoda and Moin definitions and any indication that it is an Arabic loanword meaning 'camel' (شتر)."
}
```


## [2026-09-06T15:30:53.145Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%85%DB%8C%D9%86%DB%8C+%DA%98%D9%88%D9%BE/",
 "prompt": "Persian مینی ژوپ: definition and origin (French mini-jupe). Also anything on ژوپ."
}
```


### [2026-09-06T15:30:55.444Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T15:30:58.528Z] TOOL RESULT

```
# جمل (Camel)

## Dehkhoda Definition
According to Lughah-nameh Dehkhoda, جمل refers to a male camel (شتر نر), though it can occasionally apply to female camels. The entry notes: "شتر نر و بندرت بر شتر ماده اطلاق شود" (male camel, and rarely applied to female camel).

## Moin Dictionary Definition
Ferhangh-e Moin provides a concise entry: جَ مَ (ع. اِ.) شتر—identifying it simply as a camel, with Arabic origins.

## Arabic Loanword Status
The word جمل is explicitly marked as an Arabic etymological source (ع) throughout multiple dictionary entries, confirming its status as a loanword from Classical Arabic into Persian. The various classical Arabic references (منتهی الارب, اقرب الموارد) that appear alongside definitions reinforce its Arabic linguistic foundation.

The term also carries secondary meanings in Persian, including ship's rope (طناب کشتی) and the numerical system known as حساب جُمَّل (abjad calculation).
```


## [2026-09-06T15:31:03.974Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%DA%98%D9%88%D9%BE/",
 "prompt": "Persian ژوپ: is there an entry? definition and origin. Also mention of مینی‌ژوپ."
}
```


### [2026-09-06T15:31:09.606Z] TOOL RESULT

```
# ژوپ (Jupe) Entry

Based on the dictionary page provided, **ژوپ does have an entry** in Abadis Dictionary.

## Definition and Origin

The entry defines it as: "( فرانسوی: jupe ) ، دامن" — indicating it's a French loanword meaning "skirt" in Persian.

## Regarding مینی‌ژوپ

The provided content does **not mention مینی‌ژوپ** (mini-jupe/miniskirt). Only the base term ژوپ appears in this dictionary entry, with its French origin and Persian equivalent clearly noted.

The page itself is from Abadis Dictionary, which has been operating since 2006 and offers various Persian-language reference resources.
```


## [2026-09-06T15:31:18.525Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://abadis.ir/fatofa/%DA%98%D9%88%D9%BE/' --note 'page 228, node Persian zhup: abadis gives ژوپ (فرانسوی: jupe) دامن' 2>&1|tail -1\npython3 tools/fetch_source.py 'https://abadis.ir/fatofa/%D8%AC%D9%85%D9%84/' --note 'page 228, node Persian jamal: Moin جَمَل (ع. اِ.) شتر = Arabic loan, camel' 2>&1|tail -1\ncd data/verification/sources/refs\necho \"=== LEW camelus ===\"; grep -n -i \"camelus\" LEW_1910.txt | head -5\necho \"=== LAT camelus ===\"; grep -n -i \"camelus\" LAT.txt | head -5\necho \"=== FSD vol1 camel ===\"; grep -n \"^camel,\" FSD_vol1.txt | head -3\necho \"=== WEB camel ===\"; grep -n -i \"kamelos\\|camelus\" WEB.txt 2>/dev/null | head -3; ls | grep -i \"^WEB\""
}
```


### [2026-09-06T15:31:23.902Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/3e68d82bb9560b74.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9f3557dedd4df16b.txt
=== LEW camelus ===
=== LAT camelus ===
8972:camelus, -I c.: chaaeau. Atteste depuis Pomponius. Varr.,L.L.s,
=== FSD vol1 camel ===
=== WEB camel ===
WEB_vol1.txt
```


## [2026-09-06T15:31:27.410Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LAT ===\"; sed -n '8970,8985p' LAT.txt\necho; echo \"=== WEB_vol1 camel ===\"; grep -n -i \"cam.lus\\|kamelos\" WEB_vol1.txt | head -5\necho; echo \"=== FSD vol1 camel ===\"; grep -n -i \"camel\" FSD_vol1.txt | grep -i \"gamal\\|Heb\\|Gr\\.\" | head -5"
}
```


### [2026-09-06T15:31:27.507Z] TOOL RESULT

```
=== LAT ===
camella, -ae (ga-), f.: vase k boire, ecuelle. M.L.1543. Diainutif
de camera.
camelus, -I c.: chaaeau. Atteste depuis Pomponius. Varr.,L.L.s,
10, -s suo nomine Syriaco in Latium uenit. Le aot est venu au latin
par gr. xap.T]XoC • A du etre alteri en *camellus sous 1 'influence des
aots en -ellus, cf.M.L.1544; iri. comaZ, gall. canval, Derivas latins:
camelinus-, camelarius. Le latin aeaprnnt 4 aussi camelopardalis (= xap.T]-
Xo7tap8aXi,c) qui a eti altare en camSlopardalus, -pardala, -pardus,
-parda.
Camenae, -Arum f.pl.: anciennes deesses des sources et des eaux.
Les anciens pobtes latins, Livius Andronicus, Naevius, se sont servis
du noa de Camenae pour reaplacer le noa des Muses; 1 'equivalence dtait
grossibre et Snnius, suivi par ses successeurs, a transerit simplement
le noa grec MUsae. Livius Andronicus coaaence son pobae par uirum mihi,
Camena, insece uersutum; aais Ennius par Musae, quae pedibus magnum
pulsatis Olumpum. - Repris ensuite par la po^sie de 1 'epoque imperiale,

=== WEB_vol1 camel ===
26813:cam/el, n. [OFr. camel; L. camelus; Gr. kamé- los; Heb. gamal, a camel.) ;
26814:1. a large, domesticated, four-footed animal with a humped back: there are two species, the Camelus dromedarius, the dromedary, or Arabian camel (with one hump), and Camelus bactrianus, or Bactrian camel (with two humps). Both species are long-necked and have broad, cushioned feet and pouches in the paunch to store up water. The camel is valu- able as a beast of burden especially in Asian and African deserts. =

=== FSD vol1 camel ===
24672:Ar'gob,  1   Grigob;  2   tir'gOb,  n.  Bib.  Dcul.  111,4. ar'go!1,  1   ar'gol;  2   fir'&Sl,  n .   The  hard  crust  of  potas- sium acid  tartrate  deposited  from  grape-juice  during fermentation;  crude  cream  of  tartar.  According  to  the color  of  the  grape,  argol  la  dark-red  or  whlttsh-plnk.  It  is used  considerably  In  the  arts.  [Ult.  <   Gr.  argos,  whlte.I ar'galt;  ar'goUc}.  [the  Mongols  as  fuel,  ar'galt- ar'gol*.  n.  [Mongol.J  Dry  dung  of  cattle  or  camels,  used  by Ar-gol'lc,  1   ar-gol'ik;  2   lir-gfll'Ic,  a.  Of  or  pertaining  to  Ar- golls,  the  northeastern  district  of  rcloponncsus.  Ar-go'll- ant;  Ar'go-Ildt.
27885:at'e-lcs,  1   at'i-llz;  2   fit'c-le;,  n.  A   Fpldcr-monkcy  a'thar,  1   n'tar;  2   K'tSr,  n.  The  science  of  deducing  Inf orma- (Atcles).  [   <   Gr.  atelcs;  see  atelectasis.]  tlon  from  the  tracks  of  a   camel  or  a   train  of  camels.
27886:at^C-Ies'Ilte,  1   atVIes'tait;  2   fit'C-ISs'tU,  n.  Mineral.  The  camel’*  foot  loaves  data  for  the  Bedouin  science  of  A(Sar. A   sulfur-yellow  adamantine  bismuth  arsenate  (HsBiz  ruAcv^OM E*  lNOERaOL1***  of  ..  .   Mammal*  p.  337. AsOi),  crv'stallizing  in  the  monoclimc  svstem.  1<  Gr.  l.r'l*  ,
54068:B.  C.),  <   Gr.  right  to  left  <   Fheniclan  f]t  gtoel.  camel. <   Egyptian  hieratic  Z»  <   the  Egyptian'  hieroglyph  0, called  throne.  For  dates,  see  A.
55790:lieve.  See  Matt,  xxiii,  24.  6.  [C-]  Same  as  Camel- opard, 2.  [OF.,  <   L.  camelus,  <   Gr.  kamelos,  <   Heb. gamal,  camel.]  cam'allt;  cam'alllet;  cam'mclf.
```


## [2026-09-06T15:31:37.069Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://ahdictionary.com/word/search.html?q=camel",
 "prompt": "Give the American Heritage Dictionary etymology of 'camel' verbatim (Middle English, Old English/Old North French, Latin camelus, Greek kamelos, Semitic source)."
}
```


### [2026-09-06T15:31:41.044Z] TOOL RESULT

```
# Etymology of "Camel"

According to the American Heritage Dictionary, the word camel traces back through several languages:

"[Middle English, from Old English and from Anglo-Norman _cameil_, both from Latin _camēlus_, from Greek _kamēlos_, of Semitic origin"

The entry indicates the term derives from Semitic roots, with the Greek and Latin forms serving as intermediaries through which it entered Old English and Anglo-Norman French before becoming the modern English word.
```


## [2026-09-06T15:31:49.738Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://ahdictionary.com/word/search.html?q=jungle",
 "prompt": "Give the American Heritage Dictionary etymology of 'jungle' verbatim (Hindi jangal, Sanskrit jangala, meaning given)."
}
```


### [2026-09-06T15:31:56.931Z] TOOL RESULT

```
# Jungle Etymology

According to the American Heritage Dictionary, the etymology of "jungle" is:

"Ultimately from Sanskrit _jaṅgalam_, desert, wasteland, uncultivated area, from _jaṅgala-_, desert, waste."

The entry does not include a separate Hindi form in the etymology section provided on this page.
```


## [2026-09-06T15:32:01.817Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://ahdictionary.com/word/search.html?q=camel' --note 'page 228, root Jamal / nodes Greek-Latin-OF-English: AHD camel = ME < OE and Anglo-Norman cameil < L camelus < Gk kamelos, of Semitic origin' 2>&1|tail -1\npython3 tools/fetch_source.py 'https://ahdictionary.com/word/search.html?q=jungle' --note 'page 228, root Jangalah: AHD jungle ultimately from Sanskrit jangalam desert, wasteland, uncultivated area' 2>&1|tail -1"
}
```


### [2026-09-06T15:32:05.896Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/0230bea9583fd265.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/470beb5e4a20dce2.txt
```


## [2026-09-06T15:32:08.394Z] TOOL CALL #51: Bash

```json
{
 "command": "sed -n '1,200p' tools/verify_check.py"
}
```


### [2026-09-06T15:32:08.431Z] TOOL RESULT

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


## [2026-09-06T15:32:28.828Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\ndef leafof(f,pat,off=None,n=1):\n    t=open(f,encoding='utf-8',errors='replace').read()\n    ps=t.split('\\f')\n    out=[]\n    for i,p in enumerate(ps):\n        if re.search(pat,p):\n            out.append(i)\n    print(f,pat,'leaves',out[:6], 'printed~',[i-off for i in out[:6]] if off is not None else '')\nleafof('SKT.txt',r'CameL\\.\\s+\\(F',20)\nleafof('FSD_vol1.txt',r'<   Gr\\.  kamelos',None)\nleafof('WEB_vol1.txt',r'cam/el, n\\. \\[OFr',None)\nleafof('LKT.txt',r'ö53\\.  Ar\\.  gaiual',26)\nleafof('AID.txt',r'Jungle\\.',18)\nleafof('PHN.txt',r'JUPE, s\\. f\\.',31)\nleafof('DEV.txt',r'Jupe\\.   Esp\\.',None)\nleafof('LAM.txt',r'Jupe\\. De ',57)\nleafof('HJB.txt',r\"JUNGLE,  s\\.\",None)\nEOF"
}
```


### [2026-09-06T15:32:31.433Z] TOOL RESULT

```
SKT.txt CameL\.\s+\(F leaves [] printed~ []
FSD_vol1.txt <   Gr\.  kamelos leaves [436] printed~ 
WEB_vol1.txt cam/el, n\. \[OFr leaves [284] printed~ 
LKT.txt ö53\.  Ar\.  gaiual leaves [78] printed~ [52]
AID.txt Jungle\. leaves [159] printed~ [141]
PHN.txt JUPE, s\. f\. leaves [252] printed~ [221]
DEV.txt Jupe\.   Esp\. leaves [181] printed~ 
LAM.txt Jupe\. De  leaves [322] printed~ [265]
HJB.txt JUNGLE,  s\. leaves [521] printed~
```


## [2026-09-06T15:32:40.926Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('SKT.txt',encoding='utf-8',errors='replace').read()\nps=t.split('\\f')\nfor i,p in enumerate(ps):\n    if 'camelopard,  a  giraffe' in p:\n        print('SKT leaf',i,'printed~',i-20); break\nt=open('FSD_vol1.txt',encoding='utf-8',errors='replace').read()\nps=t.split('\\f')\np=ps[436]\nprint('FSD v1 leaf436 nums', re.findall(r'\\b\\d{3}\\b',p)[:10])\nprint(p[:150].replace('\\n',' '))\nt=open('WEB_vol1.txt',encoding='utf-8',errors='replace').read()\nps=t.split('\\f')\nprint('WEB leaf284 nums', re.findall(r'\\b\\d{3}\\b',ps[284])[:8])\nEOF"
}
```


### [2026-09-06T15:32:43.265Z] TOOL RESULT

```
SKT leaf 82 printed~ 62
FSD v1 leaf436 nums ['350', '383', '600', '680', '529', '522', '718', '702', '222', '218']
.  lamara,  vault,  -f  stoma, mouth.] cam'as,  1   kam'es;  2   cSm'as,  n.  TAm.  Ind.]  Bot.  1.  Any species  of  plant  belonging  to  the  genus
WEB leaf284 nums []
```


## [2026-09-06T15:33:01.926Z] TOOL CALL #54: WebSearch

```json
{
 "query": "\"chameal\" Anglo-Norman Dictionary chamel camel Old French variant"
}
```


### [2026-09-06T15:33:09.781Z] TOOL RESULT

```
Web search results for query: ""chameal" Anglo-Norman Dictionary chamel camel Old French variant"

Links: [{"title":"camelus - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/camelus"},{"title":"camel — definition, examples, related words and more at Wordnik","url":"https://www.wordnik.com/words/camel"},{"title":"Etymology dictionary — Ellen G. White Writings","url":"https://m.egwwritings.org/en/book/14732.514625#14785"},{"title":"Anglo-Norman Dictionary","url":"https://www.anglo-norman.net/entry/chamel_1"},{"title":"Camel - Etymology, Origin & Meaning","url":"https://www.etymonline.com/word/camel"},{"title":"chamel - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/chamel"},{"title":"Anglo-Norman Dictionary","url":"https://anglo-norman.net/entry/cameil"},{"title":"camel - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/camel"},{"title":"Camel Definition & Meaning | YourDictionary","url":"https://www.yourdictionary.com/camel"},{"title":"Anglo-Norman language","url":"https://en.wikipedia.org/wiki/Anglo-Norman_language"}]

Based on the search results, I found relevant information about "chameal" and related terms in the Anglo-Norman Dictionary.

The Anglo-Norman Dictionary lists "chameal" among the variant forms of the word for camel, alongside other variants including camail, camaile, camaille, cameil, camel, chamail, chamaile, chamaille, chameil, and chamoil.

The word originates from Old French "chamel" and comes from Latin "camelus," from Greek "kamelos," ultimately deriving from Hebrew or Phoenician "gamal". The Old French term comes from Vulgar Latin "*camellus," a variant of Classical Latin "camēlus".

In the Anglo-Norman Dictionary entry, chameal is listed as one of the spelling variants used from 1121-35 onwards, showing that this was an accepted form in Anglo-Norman texts during that period.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-06T15:33:26.957Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://www.anglo-norman.net/entry/chamel_1' --note 'page 228, node Old French chamel/chameal: Anglo-Norman Dictionary lists chameal, chamel, cameil, camel as variants from 1121-35' 2>&1|tail -1\npython3 tools/fetch_source.py 'https://www.littre.org/definition/jupe' --note 'page 228, node French jupe: Littre etymology provencal jupa, catalan aljuba, italien giubba, arabe djobbah' 2>&1|tail -1"
}
```


### [2026-09-06T15:33:31.681Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/479ea87f8e29c910.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1dca5e4a24adc7fd.txt
```


## [2026-09-06T15:33:34.408Z] TOOL CALL #56: Bash

```json
{
 "command": "head -c 900 /home/sfmqrb/git/rishe/data/verification/sources/web/1dca5e4a24adc7fd.txt; echo; echo ====; grep -i -A4 \"tymologie\" /home/sfmqrb/git/rishe/data/verification/sources/web/1dca5e4a24adc7fd.txt | head -20"
}
```


### [2026-09-06T15:33:34.461Z] TOOL RESULT

```
Exit code 1
URL: https://www.littre.org/definition/jupe
FETCHED: 2026-09-06T15:33:31Z
STATUS: 200
TITLE: Littré - jupe - définition, citations, étymologie

Littré - jupe - définition, citations, étymologie 

 Dictionnaire Littré 

 Menu
… 
 Mot 

 Rechercher 

 Une requête vide propose un mot au hasard.

 Recherche avancée 

 Mots voisins 
 jument 

 jumenterie 

 jumenteux 

 juncaginées 

 jungle 

 junipène 

 junkérite 

 junon 

 junte 

 juntes 

 jupe 

 jupin 

 jupiter 

 jupitérien 

 jupon 

 juponné 

 jurable 

 jurade 

 jurande 

 jurassien 

 jurassique 

 Annexes 
 Livres cités 

 Prononciation 

 Préface 

 Causerie 

 Informations 
 FAQ 

 Statistiques 

 Étymologie 

 Proverbes 

 Contact 

 « jupe », définition dans le dictionnaire Littré

 jupe 

 Définition dans d'autres dictionnaires :

 TLFi 

 Académie Française 

 Fac-simile de l'édition orig
(eval):1: === not found
```


## [2026-09-06T15:33:36.860Z] TOOL CALL #57: Bash

```json
{
 "command": "grep -n -i -m3 -A8 \"ÉTYMOLOGIE\\|Etymologie\" /home/sfmqrb/git/rishe/data/verification/sources/web/1dca5e4a24adc7fd.txt | sed -n '1,60p'"
}
```


### [2026-09-06T15:33:36.911Z] TOOL RESULT

```
4:TITLE: Littré - jupe - définition, citations, étymologie
5-
6:Littré - jupe - définition, citations, étymologie 
7-
8- Dictionnaire Littré 
9-
10- Menu
11-… 
12- Mot 
13-
14- Rechercher 
--
77: Étymologie 
78-
79- Proverbes 
80-
81- Contact 
82-
83- « jupe », définition dans le dictionnaire Littré
84-
85- jupe
```


## [2026-09-06T15:33:39.660Z] TOOL CALL #58: Bash

```json
{
 "command": "grep -n -i \"provenç\\|aljuba\\|giubba\\|djobbah\\|arabe\" /home/sfmqrb/git/rishe/data/verification/sources/web/1dca5e4a24adc7fd.txt | head -10"
}
```


### [2026-09-06T15:33:39.700Z] TOOL RESULT

```
110: Provenç. jupa  ; catal. du XIII e siècle, aljuba  ; ital. giubba, giuppa  ; de l'arabe jubbet , pelisse courte et de dessous.
```


## [2026-09-06T15:39:22.830Z] TOOL CALL #59: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk228.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\n\ndata = {\n \"pdf_page\": 228,\n \"book_page\": 198,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-06\",\n \"entries\": [\n  {\n   \"entry\": 1,\n   \"root\": \"Jamal\",\n   \"verdict\": \"plausible\",\n   \"modern_form\": \"Arabic جَمَل jamal 'camel' < Proto-West Semitic *gamal-\",\n   \"note\": \"The Arabic word is real and correctly glossed: جَمَل jamal 'male camel', inherited from Proto-(West-)Semitic *gamal-, itself probably a Wanderwort of Arabian origin. What is a simplification is making ARABIC the head of the whole chart: every modern authority derives Greek κάμηλος not from Arabic but from a Northwest Semitic form — Phoenician 𐤂𐤌𐤋 gml / Hebrew גָּמָל gāmāl / Aramaic gamlā (Klein: 'fr. Heb. and Phoen. gamal, which is rel. to Arab. jamal'; Skeat tags the word '(F.-L.-Gk.-Heb.)'; Ernout–Meillet quote Varro's remark that the animal's name 'suo nomine Syriaco in Latium uenit'). Read the root box as Semitic *gamal- and the chart is right; read it literally as Arabic and the Greek arrow is wrong. Nourai's own source, AHD, says only 'of Semitic origin'.\",\n   \"note_fa\": \"واژهٔ عربی «جَمَل» به معنی «شتر (نر)» درست است و از سامی آغازین *gamal- به ارث رسیده است؛ برخی آن را واژهٔ سرگردانی (Wanderwort) با خاستگاه شبه‌جزیرهٔ عربستان می‌دانند. اما قرار دادن «عربی» در رأس این نمودار ساده‌سازی است: کلاین، اسکیت، وبستر و ویکی‌واژه همگی یونانی kámēlos را نه از عربی jamal بلکه از صورت سامی شمال‌غربی (فنیقی gml، عبری gāmāl، آرامی gamlā) می‌گیرند، و ارنو–مِیه هم گفتهٔ وارّو را نقل می‌کنند که این نام «با نام سریانی خود به لاتیوم آمد». اگر جعبهٔ ریشه را «سامی *gamal-» بخوانیم ادعای نورایی درست است؛ اگر تحت‌اللفظی «عربی» بخوانیم، پیکان یونانی نادرست است. خودِ مأخذ نورایی (AHD) تنها می‌گوید «با خاستگاه سامی».\",\n   \"sources\": [W+\"camel\", \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Semitic/gamal-\", \"https://ahdictionary.com/word/search.html?q=camel\", \"https://www.etymonline.com/word/camel\"],\n   \"ref_check\": [\n    {\"ref\": \"AHD:192\", \"status\": \"partial\",\n     \"note\": \"The 1975/76 New College Edition is not open online, so p.192 itself could not be seen (its alphabetical position under c- is consistent). The AHD text for 'camel' (current online edition, ahdictionary.com/word/search.html?q=camel) reads: '[Middle English, from Old English and from Anglo-Norman cameil, both from Latin camēlus, from Greek kamēlos, of Semitic origin]' — it supports the Greek>Latin>French>English chain but says only 'of Semitic origin', not 'from Arabic'.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"LKT\", \"where\": \"no. 653 (leaf 78 = p.52) 'Ar. gamal'\", \"stance\": \"partial\",\n     \"note\": \"Lokotsch 653: \\\"Ar. gamal 'Kamel' [aus der Wurzel gamala 'sammeln'...]; aus dieser oder einer anderen semitischen Form gr. καμηλος, lat. camelus, *camellus; hieraus it. cammello ... frz. chameau ... dtsch. Kamel, engl. camel\\\" — the Arabic word is only one candidate donor ('or another Semitic form').\"},\n    {\"src\": \"SKT\", \"where\": \"p.62 s.v. Camel (leaf 82)\", \"stance\": \"contradicts\",\n     \"note\": \"Skeat: \\\"Camel. (F.-L.-Gk.-Heb.) M.E. camel, cameil, chamel. — O.F. camel, chamel\\\"; under camelopard he glosses Gk. καμηλο- 'a camel (Heb. gāmāl)' — Hebrew, not Arabic, is named as the donor.\"},\n    {\"src\": \"WEB\", \"where\": \"vol. I leaf 284 s.v. camel\", \"stance\": \"contradicts\",\n     \"note\": \"Webster's New Twentieth Century: \\\"cam·el, n. [OFr. camel; L. camelus; Gr. kamēlos; Heb. gamal, a camel.]\\\"\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Persian\", \"words\": \"jamal «جمل»\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"New Persian جمل jamal 'camel' is a straight lexical borrowing of Arabic جَمَل jamal, taken over after the Islamic conquest as a bookish synonym of the inherited Persian شتر šotor (MP uštar, Av. uštra-). Mo'in marks it as such: 'جَمَل (ع. اِ.) شتر' — '(Arabic, noun) camel'; Dehkhoda adds 'شتر نر و بندرت بر شتر ماده اطلاق شود' ('the male camel, rarely used of the she-camel'), which is exactly the Arabic gender restriction, showing the loan is learned and not popular. The same Arabic word underlies the Persian idiom حساب جُمَّل (abjad reckoning), a different word from the same consonants.\",\n     \"derivation_fa\": \"«جمل» در فارسی نو وام‌واژه‌ای مستقیم از عربی جَمَل «شتر (نر)» است که پس از ورود اسلام همچون مترادفی ادبی در کنار واژهٔ ایرانی «شتر» (فارسی میانه uštar، اوستایی uštra-) به کار رفت. معین آن را با نشانهٔ «ع. اِ.» یعنی اسم عربی ثبت کرده و معنی آن را «شتر» داده است، و دهخدا می‌افزاید «شتر نر و بندرت بر شتر ماده اطلاق شود» — همین محدودیت جنسیتیِ عربی نشان می‌دهد که وام‌گیری کتابی است نه عامیانه. ادعای نورایی در این گره درست است.\",\n     \"sources\": [\"https://abadis.ir/fatofa/%D8%AC%D9%85%D9%84/\", W+\"%D8%AC%D9%85%D9%84\"],\n     \"ref_check\": [\n      {\"ref\": \"FVA:81\", \"status\": \"not_checked\",\n       \"note\": \"Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi: refs_online.json records no digital copy (searched archive.org, ketabnak, noorlib); p.81 could not be inspected. The claim it is cited for (Persian jamal is an Arabic loan) is uncontroversial and is confirmed by Mo'in and Dehkhoda.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"vajehyab/abadis, فرهنگ معین s.v. جمل\", \"stance\": \"supports\",\n       \"note\": \"'جَ مَ (ع. اِ.) شتر' — Mo'in tags the headword ع. (Arabic) and glosses 'camel'.\"},\n      {\"src\": \"BQT\", \"where\": \"Borhan vol. 2, ج section (BQT_v2_pages.txt); grep 'جمل'\", \"stance\": \"silent\",\n       \"note\": \"Borhan-e Qate' is a dictionary of Persian words; جمل has no headword there (only حساب جمل and مجمل التواریخ turn up in the grep), so Mo'in's footnotes say nothing about it.\"},\n      {\"src\": \"ARY\", \"where\": \"ARY_pages.txt, grep 'جمل'\", \"stance\": \"silent\",\n       \"note\": \"Aryanpur's dictionary of Indo-European roots of Persian has no entry — as expected for a Semitic loan.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Greek\", \"words\": \"kamělos\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"Ancient Greek κάμηλος kámēlos 'camel' (Aeschylus, Herodotus) is certainly a Semitic loan from *gamal-, but the transmitting language was almost certainly not Arabic. Greek renders a Semitic *g by κ and a long *ā by η (the Ionic reflex of ā), which points to a Northwest Semitic form gāmāl — Phoenician 𐤂𐤌𐤋 gml, Hebrew גָּמָל gāmāl, Aramaic ܓܡܠܐ gamlā — reaching Greek through Phoenician trade in the archaic period; Wiktionary's Proto-Semitic entry states the word 'entered Ancient Greek as κάμηλος through Phoenician transmission'. Arabic jamal has j- (< *g-) and would not have given κ- at the time. Nourai's arrow is right about the family (Semitic *gamal-) but wrong about the specific donor; Lokotsch already hedged, 'aus dieser oder einer anderen semitischen Form'.\",\n     \"derivation_fa\": \"یونانی باستان κάμηλος (kámēlos) «شتر»، که از آیسخولوس و هرودوت به بعد گواهی شده، بی‌گمان وام‌واژه‌ای سامی از *gamal- است، اما زبان واسط به احتمال بسیار عربی نبوده است. یونانی *g سامی را با κ و ā کشیده را با η (بازتاب یونیایی ā) نشان می‌دهد و این به صورت سامی شمال‌غربی gāmāl (فنیقی gml، عبری gāmāl، آرامی gamlā) اشاره دارد که از راه بازرگانی فنیقی در دورهٔ باستان به یونانی رسیده است؛ ویکی‌واژه صراحتاً می‌گوید این واژه «از طریق فنیقی» وارد یونانی شده است. عربی jamal با جیم (< *g) در آن دوره κ نمی‌داد. پس ادعای نورایی دربارهٔ خانوادهٔ سامی درست، اما دربارهٔ زبانِ وام‌دهنده با احتیاط پذیرفتنی است؛ لوکوچ نیز نوشته «از این صورت یا صورتی دیگر از سامی».\",\n     \"sources\": [W+\"%CE%BA%CE%AC%CE%BC%CE%B7%CE%BB%CE%BF%CF%82\", \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Semitic/gamal-\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD:192\", \"status\": \"partial\",\n       \"note\": \"AHD s.v. camel: '...from Latin camēlus, from Greek kamēlos, of Semitic origin' — confirms the Semitic>Greek step but declines to name Arabic. Page 192 of the 1976 edition is not open online.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 78 (p.~135?) s.v. camel — actually leaf found by grep 'camel,  n.'\", \"stance\": \"contradicts\",\n       \"note\": \"Klein s.v. camel: 'fr. L. camelus, fr. Gk. καμηλος, fr. Heb. and Phoen. gamal, \\\"camel\\\", which is rel. to Arab. jamal, of s.m.' — Hebrew/Phoenician is the donor, Arabic only a cognate.\"},\n      {\"src\": \"LAT\", \"where\": \"Ernout–Meillet s.v. camelus (LAT.txt line 8972)\", \"stance\": \"partial\",\n       \"note\": \"'camelus, -i c.: chameau. Atteste depuis Pomponius. Varr., L.L. 5,10: suo nomine Syriaco in Latium uenit. Le mot est venu au latin par gr. καμηλος' — Varro calls the name Syriac (i.e. Aramaic), not Arabic.\"},\n      {\"src\": \"FSD\", \"where\": \"vol. I leaf 436 (p.~383) s.v. camel\", \"stance\": \"contradicts\",\n       \"note\": \"'[OF., < L. camelus, < Gr. kamelos, < Heb. gamal, camel.]'\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Latin\", \"words\": \"camělus\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Latin camēlus is a straight loan of Greek κάμηλος, first attested in Pomponius (2nd c. BCE) and discussed by Varro (L.L. 5,100), who says the beast 'came to Latium under its Syriac name'; Ernout–Meillet: 'Le mot est venu au latin par gr. καμηλος'. Vulgar Latin remodelled it as *camellus under the pull of the very numerous -ellus nouns (REW 1544), and it is that geminated form, not classical camēlus, that gives the Romance words (It. cammello, Sp. camello, OF chamel/chameau).\",\n     \"derivation_fa\": \"لاتینی camēlus وام‌واژه‌ای مستقیم از یونانی κάμηλος است؛ نخستین گواه آن در پومپونیوس (سدهٔ دوم پیش از میلاد) است و وارّو در «دربارهٔ زبان لاتینی» می‌گوید این جانور «با نام سریانی‌اش به لاتیوم آمد». ارنو–مِیه می‌نویسند: «این واژه از راه یونانی καμηλος به لاتینی رسیده است». در لاتینی عامیانه به قیاسِ انبوه اسم‌های ‎-ellus به *camellus بدل شد و همین صورتِ مشدّد است که صورت‌های رومی (ایتالیایی cammello، اسپانیایی camello، فرانسهٔ کهن chamel/chameau) را پدید آورده است. ادعای نورایی درست است.\",\n     \"sources\": [W+\"camelus\", \"https://ahdictionary.com/word/search.html?q=camel\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD:192\", \"status\": \"supports\",\n       \"note\": \"AHD s.v. camel: '...both from Latin camēlus, from Greek kamēlos' — exactly the arrow drawn here. Page number unverifiable (1976 New College Edition not open online).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"LAT\", \"where\": \"Ernout–Meillet s.v. camelus (LAT.txt line 8972)\", \"stance\": \"supports\",\n       \"note\": \"'Le mot est venu au latin par gr. καμηλος. A du etre altere en *camellus sous l'influence des mots en -ellus, cf. M.L. 1544.'\"},\n      {\"src\": \"LKT\", \"where\": \"no. 653 (leaf 78 = p.52)\", \"stance\": \"supports\",\n       \"note\": \"'aus dieser oder einer anderen semitischen Form gr. καμηλος, lat. camelus, *camellus; hieraus it. cammello, siz. camiddu, prov. camels, frz. chameau, kat. camell, sp. camello, pg. camelo; dtsch. Kamel, engl. camel.'\"},\n      {\"src\": \"SKT\", \"where\": \"p.62 s.v. Camel/camelopard\", \"stance\": \"supports\",\n       \"note\": \"'L. camelopardalis ... Gk. καμηλο-, a camel' presupposes the Greek>Latin loan; the camel entry gives 'O.F. camel, chamel' from L. camelus.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"Old French\", \"words\": \"chamel, chameal\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Continental Old French chamel (from VL *camellus, with regular Gallo-Romance ca- > cha- palatalisation) later gave chameau by vocalisation of -l to -u. The Norman/Anglo-Norman dialect did NOT palatalise ca-, so it kept camel/cameil; the Anglo-Norman Dictionary lists chameal beside chamel, chameil, chamail, chamoil, cameil and camel as spellings current from c.1121-35 (the -eal spelling is the ordinary Anglo-Norman way of writing what continental French wrote -eau/-el). Both forms Nourai prints are therefore real, and the odd-looking 'chameal' is not a misprint.\",\n     \"derivation_fa\": \"در فرانسهٔ کهنِ قاره‌ای صورت chamel از لاتینی عامیانهٔ *camellus پدید آمد (با نرم‌شدگی قاعده‌مندِ ca- به cha- در گالو-رومی) و سپس با تبدیل ‎-l پایانی به ‎-u به chameau رسید. گویش نورمان/آنگلو-نورمان این نرم‌شدگی را نداشت و صورت camel / cameil را نگاه داشت. فرهنگ آنگلو-نورمان صورت chameal را در کنار chamel، chameil، chamail، chamoil، cameil و camel از حدود ۱۱۲۱–۳۵ م. ثبت کرده است؛ املای ‎-eal شیوهٔ معمول آنگلو-نورمان برای همان ‎-eau/-el فرانسهٔ قاره‌ای است. پس هر دو صورتی که نورایی آورده واقعی‌اند و «chameal» خطای چاپی نیست.\",\n     \"sources\": [\"https://www.anglo-norman.net/entry/chamel_1\", W+\"camel\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD:192\", \"status\": \"partial\",\n       \"note\": \"The current AHD text names 'Anglo-Norman cameil' rather than Old French chamel; the older (1976) printing that Nourai cites gave 'Old French chamel'. Either way the Latin>Gallo-Romance>English route is the one AHD draws; the page itself is not open online.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.v. camel\", \"stance\": \"supports\",\n       \"note\": \"'fr. ONF. camel, corresponding to OF. chamel (whence F. chameau), fr. L. camelus' — Klein has exactly these two Old French shapes.\"},\n      {\"src\": \"SKT\", \"where\": \"p.62 s.v. Camel\", \"stance\": \"supports\",\n       \"note\": \"'M.E. camel, cameil, chamel. — O.F. camel, chamel.'\"},\n      {\"src\": \"LKT\", \"where\": \"no. 653\", \"stance\": \"partial\",\n       \"note\": \"Lokotsch cites only the modern 'frz. chameau' among the Romance continuations, without the Old French spellings.\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"English\", \"words\": \"camel\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Middle English camel/cameil/chamel replaced Old English olfend (a word that confused camel and elephant, as in Gothic ulbandus). Strictly there are two inputs: Old English camel, itself an early learned borrowing from Latin camelus in Biblical contexts, and the Anglo-Norman camel/chameal brought after 1066; the Norman non-palatalised camel is why English says camel and not *chamel while French says chameau. AHD accordingly writes '[Middle English, from Old English and from Anglo-Norman cameil]'. So Nourai's single arrow Old French > English is right in substance, with the refinement that the French input is the Norman variety and that Old English had the Latin word already.\",\n     \"derivation_fa\": \"صورت انگلیسی میانه camel / cameil / chamel جایگزین واژهٔ انگلیسی کهن olfend شد (واژه‌ای که شتر و فیل را درهم می‌آمیخت، مانند گوتی ulbandus). به‌دقت دو سرچشمه در کار است: انگلیسی کهن camel که خود وام‌گیری کتابی زودهنگام از لاتینی camelus در متن‌های کتاب مقدس است، و آنگلو-نورمان camel / chameal که پس از ۱۰۶۶ م. وارد شد؛ همین صورت نورمانِ بدونِ نرم‌شدگی است که سبب شده انگلیسی camel بگوید نه *chamel، حال آنکه فرانسه chameau دارد. فرهنگ American Heritage می‌نویسد «از انگلیسی کهن و از آنگلو-نورمان cameil». بنابراین پیکان نورایی در جوهر درست است، با این نکتهٔ تکمیلی که ورودی فرانسوی از گونهٔ نورمان است.\",\n     \"sources\": [W+\"camel\", \"https://www.etymonline.com/word/camel\", \"https://ahdictionary.com/word/search.html?q=camel\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"AHD s.v. camel: '[Middle English, from Old English and from Anglo-Norman cameil, both from Latin camēlus, from Greek kamēlos, of Semitic origin]'. Nourai cites AHD without a page here, so only the content could be checked.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.v. camel\", \"stance\": \"supports\",\n       \"note\": \"'ME. camel, cameil, chamel, chamail, fr. OE. camel, fr. ONF. camel, corresponding to OF. chamel.'\"},\n      {\"src\": \"WEB\", \"where\": \"vol. I leaf 284 s.v. camel\", \"stance\": \"supports\",\n       \"note\": \"'[OFr. camel; L. camelus; Gr. kamēlos; Heb. gamal, a camel.]'\"},\n      {\"src\": \"FSD\", \"where\": \"vol. I leaf 436 (p.~383) s.v. camel\", \"stance\": \"supports\",\n       \"note\": \"'[OF., < L. camelus, < Gr. kamelos, < Heb. gamal, camel.]'\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 2,\n   \"root\": \"Jangalah\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"Sanskrit जङ्गल jaṅgala- 'arid, sparsely wooded waste land'\",\n   \"note\": \"The root box is right in language, form and (broadly) sense. Sanskrit jaṅgala- is an adjective/noun 'arid, waterless, sparsely grown' used above all in the medical literature (Suśruta c.1200 classes land as jāṅgala, ānūpa etc.); Monier-Williams and AHD gloss it 'desert, waste land, uncultivated area'. Nourai's 'wasteland covered with wild growths' fuses the Indic sense with the later Indian-vernacular one — Hobson-Jobson p.470 sets it out: 'The native word means in strictness only waste, uncultivated ground; then, such ground covered with shrubs, trees or long grass; and thence again the Anglo-Indian application is to forest'. The word itself has no IE etymology; Wiktionary assigns it to a pre-Indo-Aryan substrate, so the box should not be read as a PIE root.\",\n   \"note_fa\": \"جعبهٔ ریشه از نظر زبان، صورت و (تقریباً) معنی درست است. سنسکریت jaṅgala- صفت/اسمی است به معنی «خشک، بی‌آب، کم‌درخت» که بیش از همه در متون پزشکی به کار رفته (سوشروتا، حدود ۱۲۰۰ م. زمین را به jāṅgala و ānūpa و جز آن بخش می‌کند)؛ مونیر-ویلیامز و AHD آن را «بیابان، زمین بایر، ناکِشته» معنی می‌کنند. معنایی که نورایی داده («بایرِ پوشیده از رستنی‌های خودرو») آمیزه‌ای است از معنی هندی کهن و معنی متأخر زبان‌های هندی؛ هابسون-جابسون (ص ۴۷۰) همین تحول را شرح می‌دهد. خودِ واژه ریشه‌شناسی هندواروپایی ندارد و ویکی‌واژه آن را از زیرلایه‌ای پیشاهندوآریایی می‌داند، پس این جعبه را نباید ریشهٔ هندواروپایی پنداشت.\",\n   \"sources\": [W+\"jungle\", \"https://ahdictionary.com/word/search.html?q=jungle\"],\n   \"ref_check\": [\n    {\"ref\": \"AHD:710\", \"status\": \"supports\",\n     \"note\": \"AHD s.v. jungle (online edition): 'Ultimately from Sanskrit jaṅgalam, desert, wasteland, uncultivated area, from jaṅgala-, desert, waste.' The 1976 New College Edition page 710 is not open online, but j- at p.710 of a 1550-page dictionary is consistent.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"HJB\", \"where\": \"Hobson-Jobson p.470 s.v. JUNGLE (HJB.txt leaf 521-522)\", \"stance\": \"supports\",\n     \"note\": \"'JUNGLE, s. Hind. and Mahr. jangal, from Skt. jangala (a word which occurs chiefly in medical treatises). The native word means in strictness only waste, uncultivated ground; then, such ground covered with shrubs, trees or long grass.'\"},\n    {\"src\": \"AID\", \"where\": \"Whitworth, Anglo-Indian Dictionary p.140/141 (AID.txt leaf 159)\", \"stance\": \"supports\",\n     \"note\": \"'Jungle. [Hindi jangal, from the Sanskrit jangala.] A wild or uninhabited country, a desert forest.'\"},\n    {\"src\": \"SYN\", \"where\": \"Buck, grep 'jangala'/'jungle'\", \"stance\": \"silent\",\n     \"note\": \"Buck's synonym dictionary covers only Indo-European vocabulary for 'forest'; the Indic word does not appear.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Hindustani\", \"words\": \"jangal : forest\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Sanskrit jaṅgala- passed through Middle Indo-Aryan (Sauraseni Prakrit) into Hindi/Urdu जंगल / جَنْگَل jangal by the ordinary NIA losses — the -a- stem vowel dropped and the word became a masculine noun. The semantic move is Indian, not English: 'waste, uncultivated ground' > 'such ground overgrown with scrub and long grass' > 'forest, wild growth' (Hobson-Jobson p.470; Whitworth 'a wild or uninhabited country, a desert forest'). Klein states the step plainly: 'Hind. jangal, \\\"desert, forest\\\", fr. OI. jangalah'.\",\n     \"derivation_fa\": \"سنسکریت jaṅgala- از راه هندوآریایی میانه (پراکریت سوره‌سنی) به هندی/اردو «جنگل» jangal رسیده است؛ در این گذار واکهٔ پایانی ستاک افتاده و واژه اسم مذکر شده است. تحول معنایی هندی است نه انگلیسی: «زمین بایر و ناکِشته» ← «همان زمین که بوته و علف بلند آن را فرا گرفته» ← «بیشه، جنگل» (هابسون-جابسون ص ۴۷۰؛ ویتورث: «سرزمینی وحشی یا نامسکون، بیشهٔ بیابانی»). کلاین نیز می‌نویسد: «هندی jangal «بیابان، جنگل» از هندی باستان jangalah». ادعای نورایی درست است.\",\n     \"sources\": [W+\"jungle\", W+\"%D8%AC%D9%86%DA%AF%D9%84\"],\n     \"ref_check\": [\n      {\"ref\": \"KLN:836\", \"status\": \"supports\",\n       \"note\": \"Klein, KLN_1966.txt leaf 451 (= printed pp. 835/836, the leaf that also carries julep, June, justice): 'jungle, n. — Hind. jangal, \\\"desert, forest\\\", fr. OI. jangalah, \\\"dry ground, waste land, desert\\\", which is of uncertain origin.' Exactly Nourai's arrow, and the page number is right.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"HJB\", \"where\": \"p.470 s.v. JUNGLE\", \"stance\": \"supports\",\n       \"note\": \"'Hind. and Mahr. jangal, from Skt. jangala'; quotes Suśruta c.1200 '...Jungle (jangalah), or of the ordinary kind'.\"},\n      {\"src\": \"AID\", \"where\": \"p.140/141 s.v. Jungle\", \"stance\": \"supports\",\n       \"note\": \"'[Hindi jangal, from the Sanskrit jangala.]'\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Persian\", \"words\": \"jangal «جنگل» : forest\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Persian جنگل jangal 'forest' is a borrowing from Indo-Aryan (Hindustani jangal), not an inherited Iranian word: it has no Old or Middle Iranian antecedent, is absent from Horn and Hübschmann, and is unknown to Pahlavi (MacKenzie has bēšag for 'forest'). Yule already noted that 'the word seems to have passed at a rather early date into Persian, and also into use in Turkistan' (Hobson-Jobson p.470); Wiktionary states it flatly: Persian jangal is 'borrowed from Hindustani ... from Sanskrit jaṅgala'. Mo'in's own footnote in Borhan-e Qate' says the same and is the very reference Nourai cites. Semantically Persian took the developed Indian sense 'forest', not the original 'waste land'.\",\n     \"derivation_fa\": \"«جنگل» در فارسی وام‌واژه‌ای از هندوآریایی (هندی jangal) است، نه واژه‌ای ایرانی به‌ارث‌رسیده: هیچ پیشینهٔ ایرانی باستان یا میانه ندارد، در هرن و هوبشمان نیامده و در پهلوی ناشناخته است (مکنزی برای «جنگل» صورت bēšag را می‌آورد). یول همان زمان یادآور شده بود که «این واژه ظاهراً بسیار زود به فارسی و نیز به ترکستان راه یافته است». ویکی‌واژه صریح می‌گوید فارسی «جنگل» از هندوستانی و آن از سنسکریت jaṅgala وام گرفته شده است. حاشیهٔ معین بر برهان قاطع — که خودِ مأخذ نورایی است — همین را می‌گوید. از نظر معنایی فارسی معنیِ تحول‌یافتهٔ هندی («بیشه») را گرفته است نه معنی اصلی («زمین بایر»). ادعای نورایی درست است.\",\n     \"sources\": [W+\"%D8%AC%D9%86%DA%AF%D9%84\", W+\"jungle\"],\n     \"ref_check\": [\n      {\"ref\": \"BQT:592\", \"status\": \"supports\",\n       \"note\": \"Borhan-e Qate', Mo'in's ed., headword جنگل: found in BQT_v2_pages.txt leaf 50 (running pagination puts it at p.590-592; the file's leaf>page offset is +540±3, so Nourai's 592 is within the scan's tolerance — the neighbouring headwords جنگ, جنگار, جنگجو, جنگولت confirm the place). Mo'in's footnote reads (OCR, cleaned): 'جنگل ـ بفتح اول و سوم، سانسکریت jangala «اشتینگاس»؛ ... این کلمه در زبانهای مختلف هند شمالی اکنون بمعنی اجم عربی، بفضای بزرگی پوشیده ... استعمال شود. همین کلمه در انگلیسی بصورت jungle داخل شده است. «دائرةالمعارف اسلام»' — i.e. Sanskrit jangala (after Steingass), current in the North Indian languages, whence English jungle. That is precisely Nourai's Sanskrit > Hindustani > Persian/English figure.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"HRN\", \"where\": \"HRN.txt, grep 'jangal'/'dschangal'\", \"stance\": \"silent\",\n       \"note\": \"Horn's Grundriss has no entry — consistent with the word being a late Indic loan rather than inherited Iranian material.\"},\n      {\"src\": \"HUB\", \"where\": \"HUB.txt, grep 'jangal'/'dschangal'\", \"stance\": \"silent\",\n       \"note\": \"Hübschmann's Persische Studien likewise has nothing.\"},\n      {\"src\": \"HJB\", \"where\": \"p.470 s.v. JUNGLE\", \"stance\": \"supports\",\n       \"note\": \"'The word seems to have passed at a rather early date into Persian, and also into use in Turkistan.'\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"English\", \"words\": \"jungle\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"English jungle is an Anglo-Indian borrowing of Hindustani jangal, first recorded c.1776 in N. B. Halhed's Code of Gentoo Laws ('Land waste for five years ... is called Jungle', quoted in Hobson-Jobson p.470); the 1809 quotations in Lord Valentia and Southey show it already naturalised. The English sense settled on 'dense tropical forest', i.e. the vegetation, rather than the Indic 'uncultivated ground'. From English it spread to French (les jungles, Jacquemont 1830) — so the word reached Europe through the Company's India, not through Persian. Fitzedward Hall (1873) already called it 'good English'.\",\n     \"derivation_fa\": \"انگلیسی jungle وام‌واژه‌ای هندی-انگلیسی از هندی jangal است که نخستین بار حدود ۱۷۷۶ م. در ترجمهٔ نَتانیل هَلهِد از «قانون‌نامهٔ هندوان» دیده می‌شود («زمینی که پنج سال بایر بماند ... جنگل خوانده می‌شود»، به نقل هابسون-جابسون ص ۴۷۰)، و شواهد ۱۸۰۹ م. نشان می‌دهد که تا آن زمان کاملاً جا افتاده بوده است. معنی انگلیسی بر «بیشهٔ انبوه گرمسیری» یعنی بر پوشش گیاهی تثبیت شد، نه بر «زمین ناکِشتهٔ» هندی. از انگلیسی به فرانسه هم رفت (Jacquemont، ۱۸۳۰ م.). پس این واژه از راه هندِ دورهٔ کمپانی به اروپا رسیده است نه از راه فارسی. ادعای نورایی درست است.\",\n     \"sources\": [W+\"jungle\", \"https://ahdictionary.com/word/search.html?q=jungle\"],\n     \"ref_check\": [\n      {\"ref\": \"KLN:836\", \"status\": \"supports\",\n       \"note\": \"Klein leaf 451 (= p.835/836): 'jungle, n. — Hind. jangal, \\\"desert, forest\\\", fr. OI. jangalah' — the English word derived straight from the Hindustani one, as drawn.\"},\n      {\"ref\": \"AID:140\", \"status\": \"supports\",\n       \"note\": \"Whitworth, An Anglo-Indian Dictionary, AID.txt leaf 159 (printed p.140/141 by the file's leaf = printed + 18 rule): 'Jungle. [Hindi jangal, from the Sanskrit jangala.] A wild or uninhabited country, a desert forest.'\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"HJB\", \"where\": \"p.470 s.v. JUNGLE\", \"stance\": \"supports\",\n       \"note\": \"'From Anglo-Indian it has been adopted into French as well as in English'; earliest English citation 1776 Halhed's Gentoo Code, 190.\"},\n      {\"src\": \"FSD\", \"where\": \"FSD_vol2.txt, grep 'jungle'\", \"stance\": \"silent\",\n       \"note\": \"The jungle headword falls in a badly-OCRed stretch of the Funk & Wagnalls vol. II scan; only 'jungle-fowl' inside the fowl entry (leaf 255) could be retrieved, with no etymology.\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 3,\n   \"root\": \"J.b.b\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"Arabic جُبَّة jubba 'long outer garment', from the root ج ب ب j-b-b 'to cut off'\",\n   \"note\": \"Correct. جُبَّة jubba is a fuʿla-type noun from the sound root ج ب ب 'to cut off, cut short; to hollow out (a well)', which Wiktionary traces to Proto-Semitic *gbb 'to bend, curve, cut'; the garment is thus 'the cut(-short) one', which fits its description as a sleeveless or short-sleeved over-tunic. Pihan gives the same derivation independently: 'جبة [djoubbat] pelisse courte, vêtement sans manches ou à manches courtes que les Orientaux portent sous la grande pelisse ... dérivé de جبّ retrancher, raccourcir'. Nourai's gloss 'a long woolen garment' is Klein's wording verbatim (KLN s.v. jupon). No source treats jubba as a loan into Arabic, so the Arabic root box is sound.\",\n   \"note_fa\": \"درست است. «جُبّه» اسمی از وزن فُعلَة از ریشهٔ سالم «ج ب ب» به معنی «بریدن، کوتاه کردن، کندن (چاه)» است که ویکی‌واژه آن را به سامی آغازین *gbb «خم شدن، بریدن» می‌رساند؛ پس این جامه «بریده/کوتاه‌شده» است و این با توصیف آن به عنوان بالاپوشی بی‌آستین یا کوته‌آستین می‌خواند. پیهان نیز مستقلاً همین را می‌گوید: «جبة، پوستین کوتاه، جامهٔ بی‌آستین یا کوته‌آستین که مشرقیان زیر بالاپوش می‌پوشند ... برگرفته از جبّ به معنی بریدن و کوتاه کردن». معنایی که نورایی داده («جامهٔ پشمی بلند») عیناً عبارت کلاین است. هیچ مأخذی جبّه را وام‌واژه در عربی نمی‌داند، پس جعبهٔ ریشه استوار است.\",\n   \"sources\": [W+\"%D8%AC%D8%A8%D8%A9\", \"https://www.etymonline.com/word/jupon\"],\n   \"ref_check\": [\n    {\"ref\": \"FVA:67\", \"status\": \"not_checked\",\n     \"note\": \"Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil): refs_online.json records no digital copy anywhere (archive.org, ketabnak, noorlib all searched), so p.67 could not be read. The claim it carries — Arabic root j-b-b, garment jubba, loaned into Persian — is confirmed independently by Wiktionary and Pihan.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 451 (p.836) s.v. jupon\", \"stance\": \"supports\",\n     \"note\": \"'F., fr. Arab. jubbah, \\\"a long woolen garment\\\" (whence also It. giubba, OProvenç. jupa, Sp. aljuba)' — Nourai's root gloss is copied from here.\"},\n    {\"src\": \"PHN\", \"where\": \"Pihan p.221 s.v. JUPE, JUPON (PHN.txt leaf 252)\", \"stance\": \"supports\",\n     \"note\": \"'جبة [djoubbat] pelisse courte, vêtement sans manches ou à manches courtes ... dérivé de جبّ retrancher, raccourcir.'\"},\n    {\"src\": \"AFA\", \"where\": \"Fraenkel, Die aramäischen Fremdwörter im Arabischen, grep 'gubba/jubba'\", \"stance\": \"silent\",\n     \"note\": \"Fraenkel does not list jubba among the Aramaic clothing loans in Arabic — negative evidence that the word is native Arabic.\"},\n    {\"src\": \"AFM\", \"where\": \"Addi Shir, Kitab al-Alfaz al-Farisiyya al-Mu'arraba, grep 'جبة'\", \"stance\": \"silent\",\n     \"note\": \"Addi Shir does not claim jubba as an arabised Persian word (the only hit is an incidental mention in another entry).\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Persian\", \"words\": \"jobbeh «جُبّه» : garment\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Persian جُبّه jobbe is an unaltered Arabic loan, carried into Persian with the Arabic gemination (-bb-) intact — a mark of a bookish, post-Islamic borrowing rather than a popular one; the Persian sense is the Arabic one, a long outer coat worn over other clothes (hence the derived جُبّه‌پوش 'wearing a jubba', of scholars and dervishes). Borhan-e Qate' shows the word alive in classical Persian in compounds such as جبه هزار میخی. The word travelled on from Persian and Arabic to Turkish cübbe, Urdu/Hindi jubbā and Malay jubah, and via India to English jubbah — a separate branch from the Romance jupe line drawn below it.\",\n     \"derivation_fa\": \"«جُبّه» در فارسی وام‌واژه‌ای دست‌نخورده از عربی است که با تشدید عربی (‎-bb-) به فارسی آمده؛ همین حفظِ تشدید نشانهٔ وام‌گیری کتابیِ پس از اسلام است نه وام‌گیری عامیانه. معنی فارسی همان معنی عربی است: بالاپوشی بلند که روی جامه‌های دیگر می‌پوشند (از همین‌جا ترکیب «جبه‌پوش» دربارهٔ عالمان و درویشان). برهان قاطع این واژه را در ترکیب‌هایی چون «جبهٔ هزارمیخی» در فارسی کلاسیک نشان می‌دهد. همین واژه از فارسی و عربی به ترکی cübbe، اردو/هندی jubbā و مالایی jubah و از راه هند به انگلیسی jubbah رفته است — شاخه‌ای جدا از خط رومیِ jupe که نورایی زیر آن کشیده است. ادعای نورایی درست است.\",\n     \"sources\": [W+\"%D8%AC%D8%A8%D8%A9\"],\n     \"ref_check\": [\n      {\"ref\": \"FVA:67\", \"status\": \"not_checked\",\n       \"note\": \"No digital copy of Nahvi's dictionary of Arabic words in Persian exists (per refs_online.json); p.67 unreadable. The substance — Persian jobbe < Arabic jubba — is confirmed by Wiktionary's descendants list ('Persian: جبه') and by the word's Arabic shape.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BQT\", \"where\": \"Borhan vol. 2 leaf 22 (~p.562), 'جبه هزار میخی'\", \"stance\": \"partial\",\n       \"note\": \"Borhan attests جبه in Persian compounds but has no separate etymological footnote by Mo'in for it (as usual for transparent Arabic loans).\"},\n      {\"src\": \"PHN\", \"where\": \"Pihan p.221\", \"stance\": \"supports\",\n       \"note\": \"Describes جبة as the garment 'que les Orientaux portent sous la grande pelisse ou sous le manteau appelé bénich' — the Perso-Arabic usage.\"},\n      {\"src\": \"ARY\", \"where\": \"ARY_pages.txt, grep 'جبه'\", \"stance\": \"silent\",\n       \"note\": \"Aryanpur's Indo-European roots dictionary has no entry, as expected for a Semitic loan.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Spanish\", \"words\": \"juba : garment\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Hispano-Arabic al-jubba was taken into Ibero-Romance during the Andalusi period with the article agglutinated, giving Old Spanish and Portuguese aljuba 'a Moorish tunic' (13th c.; Catalan aljuba likewise); alongside it the article-less juba/jub(ón) is current, whence modern Sp. jubón 'doublet' and chupa 'jacket'. Devic p.147 lists them together: 'Jupe. Esp. juba, chupa, veste, aljuba; portug. aljuba, casaque moresque; ital. giubba. De l'arabe جبة djoubba'. Klein confirms 'Sp. aljuba' as one of the Arabic word's Romance offspring. The Spanish node itself is therefore correct; what is doubtful is only the arrow leading out of it (see node #3).\",\n     \"derivation_fa\": \"صورت عربیِ اندلسی al-jubba در دورهٔ حکومت مسلمانان با حرف تعریفِ چسبیده وارد زبان‌های ایبری شد و اسپانیایی کهن و پرتغالی aljuba «جامهٔ مغربی» را داد (سدهٔ سیزدهم میلادی؛ کاتالانی aljuba نیز همین‌گونه)؛ در کنار آن صورت بی‌حرف تعریفِ juba / jubón هم رواج دارد که اسپانیایی امروز jubón «نیم‌تنه» و chupa «کت» از آن است. دِویک (ص ۱۴۷) این صورت‌ها را کنار هم می‌آورد: «Jupe. اسپانیایی juba، chupa، aljuba؛ پرتغالی aljuba؛ ایتالیایی giubba. از عربی جبّة». کلاین نیز «اسپانیایی aljuba» را از فرزندان رومیِ واژهٔ عربی می‌شمارد. پس خودِ این گره درست است؛ آنچه محل تردید است تنها پیکانِ بیرون‌رونده از آن است (بنگرید به گرهٔ ۳).\",\n     \"sources\": [W+\"%D8%AC%D8%A8%D8%A9\", \"https://www.littre.org/definition/jupe\"],\n     \"ref_check\": [\n      {\"ref\": \"FSD:1333\", \"status\": \"supports\",\n       \"note\": \"Funk & Wagnalls New Standard, FSD_vol2.txt leaf 627 carries the running number 1333 and the jupe entry; the jupon entry on leaf 628 (p.1334) reads '... of jupe, < Sp. juba, < Ar. jubbah, garment' — so FSD does give the Spanish form as part of the chain, exactly as Nourai draws it.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"DEV\", \"where\": \"Devic p.147 s.v. Jupe (DEV.txt leaf 181)\", \"stance\": \"supports\",\n       \"note\": \"'Jupe. Esp. juba, chupa, veste, aljuba; portug. aljuba, casaque moresque; ital. giubba. De l'arabe جبة djoubba. (Voy. Dozy, Dict. des vêt. p.107.)'\"},\n      {\"src\": \"KLN\", \"where\": \"KLN_1966.txt p.836 s.v. jupon\", \"stance\": \"supports\",\n       \"note\": \"'(whence also It. giubba, OProvenç. jupa, Sp. aljuba)' — Spanish aljuba is a direct offshoot of the Arabic word.\"},\n      {\"src\": \"LAM\", \"where\": \"Lammens p.265 s.v. Jupe (LAM.txt leaf 322)\", \"stance\": \"supports\",\n       \"note\": \"'Jupe. De جبة goubba, robe. (V. Dozy, Vêtements.)'\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"French\", \"words\": \"jupe, jupon : skirt\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"The French words are real and the ultimate Arabic source is not in doubt: OF jupe (also jupel, 12th c.) 'man's tunic', with the diminutive jupon, the modern senses 'skirt' and 'petticoat' being later. But the parent Nourai draws — Spanish juba — is not the one modern scholarship gives. Littré: 'Provenç. jupa; catal. du XIIIe siècle, aljuba; ital. giubba, giuppa; de l'arabe jubbet', i.e. the Romance forms are parallel borrowings, and the Iberian aljuba (with the agglutinated article) is a separate, direct take-over from Andalusi Arabic that never had the article-less shape French shows. The CNRTL/TLFi and Wiktionary route French jupe from Old Italian giubba (the word reaching Italy from Arabic through Sicily in the 10th-11th c., in an -u- and an -i- variant), and Klein has French straight 'fr. Arab. jubbah'. Only Funk & Wagnalls (1913), Nourai's source here, inserts Spanish. Verdict: the Arabic origin is confirmed, the Spanish > French arrow is not.\",\n     \"derivation_fa\": \"خودِ واژه‌های فرانسوی و خاستگاه نهایی عربی آن‌ها محل تردید نیست: فرانسهٔ کهن jupe (و jupel، سدهٔ دوازدهم میلادی) به معنی «تنپوش مردانه» و مصغّرِ آن jupon؛ معنی‌های امروزی «دامن» و «زیردامنی» متأخرند. اما «پدرِ» ترسیم‌شده از سوی نورایی — اسپانیایی juba — همان چیزی نیست که پژوهش امروزی می‌گوید. لیتره می‌نویسد: «پرووانسی jupa؛ کاتالانی سدهٔ سیزدهم aljuba؛ ایتالیایی giubba، giuppa؛ از عربی jubbet» — یعنی این صورت‌های رومی وام‌گیری‌های موازی‌اند و صورت ایبری aljuba (با حرف تعریفِ چسبیده) وام‌گیری جداگانه و مستقیم از عربی اندلسی است که هرگز صورتِ بی‌حرف تعریفِ فرانسوی را نداشته. TLFi و ویکی‌واژه فرانسهٔ jupe را از ایتالیایی کهن giubba می‌گیرند (واژه در سده‌های دهم و یازدهم میلادی از راه سیسیل از عربی به ایتالیا رسیده است)، و کلاین آن را مستقیماً «از عربی jubbah» می‌داند. تنها Funk & Wagnalls (۱۹۱۳)، همان مأخذ نورایی، اسپانیایی را در میان می‌آورد. حکم: خاستگاه عربی تأیید می‌شود، ولی پیکانِ «اسپانیایی ← فرانسوی» را پژوهش امروزی رد می‌کند.\",\n     \"sources\": [W+\"jupe\", \"https://www.littre.org/definition/jupe\", \"https://www.etymonline.com/word/jupon\"],\n     \"ref_check\": [\n      {\"ref\": \"PHN:221\", \"status\": \"partial\",\n       \"note\": \"Pihan p.221 (PHN.txt leaf 252) s.v. 'JUPE, s. f. et JUPON, s. m. (a.)' derives both from Arabic جبة djoubbat directly — 'mots évidemment tirés de l'arabe comme leurs correspondants français' — and mentions Spanish only as a parallel: 'Les Espagnols, qui ont conservé le terme arabe précédé de l'article al, écrivent aljuba.' So the cited page supports the Arabic origin but not the Spanish intermediary.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"KLN_1966.txt p.836 s.v. jupon\", \"stance\": \"contradicts\",\n       \"note\": \"'jupon, n., skirt, petticoat. — F., fr. Arab. jubbah, \\\"a long woolen garment\\\" (whence also It. giubba, OProvenç. jupa, Sp. aljuba)' — French direct from Arabic, Spanish a sister form.\"},\n      {\"src\": \"DEV\", \"where\": \"Devic p.147 s.v. Jupe\", \"stance\": \"partial\",\n       \"note\": \"Lists Sp. juba/aljuba, Pg. aljuba and It. giubba side by side and derives the French word 'de l'arabe جبة djoubba' — again parallel, not serial.\"},\n      {\"src\": \"FSD\", \"where\": \"FSD_vol2.txt leaf 628 (p.1334) s.v. jupon\", \"stance\": \"supports\",\n       \"note\": \"'< OF. jupon, ... of jupe, < Sp. juba, < Ar. jubbah, garment' — the one book that draws Nourai's chain.\"},\n      {\"src\": \"LAM\", \"where\": \"Lammens p.265\", \"stance\": \"contradicts\",\n       \"note\": \"'Jupe. De جبة goubba, robe' — straight from Arabic, no Spanish stage.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"Persian\", \"words\": \"žŭp «ژوپ ( مینی ژوپ ، ژوپن )» : skirt\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"A 20th-century French loan, not an Arabic one: Persian ژوپ žup is French jupe 'skirt', ژوپن župan is French jupon 'petticoat, half-slip', and مینی‌ژوپ mini-žup is French mini-jupe 'miniskirt', all taken in through Pahlavi-era francophone fashion vocabulary (French, not English, was the language of dress and cuisine borrowings in Iran until the 1960s). The French [ʒ] is rendered by ژ and French [y] by Persian و/u, giving žup, župan. Dictionaries record them: Abadis s.v. ژوپ '(فرانسوی: jupe)، دامن'; Mo'in and Amid s.v. ژوپن 'دامن کوتاه، پاچین'. Nourai's arrow (French > Persian) is therefore right, and it makes this the second, modern entry of the same Arabic word into Persian — a round trip Arabic > Romance > French > Persian beside the direct جُبّه of node #1.\",\n     \"derivation_fa\": \"این گره وام‌گیری سدهٔ بیستمی از فرانسه است نه از عربی: «ژوپ» از فرانسوی jupe «دامن»، «ژوپن» از jupon «زیردامنی» و «مینی‌ژوپ» از mini-jupe «دامن کوتاه» گرفته شده است و همگی از راه واژگان مُد فرانسوی دورهٔ پهلوی وارد فارسی شده‌اند (تا دههٔ ۱۳۴۰ خورشیدی زبانِ وام‌واژه‌های پوشاک و خوراک در ایران فرانسه بود نه انگلیسی). آوای [ʒ] فرانسوی با «ژ» و واکهٔ [y] با «و» نشان داده شده و صورت‌های žup و župan پدید آمده است. فرهنگ‌ها آن‌ها را ثبت کرده‌اند: آبادیس ذیل «ژوپ»: «(فرانسوی: jupe)، دامن»؛ معین و عمید ذیل «ژوپن»: «دامن کوتاه، پاچین». پس پیکان نورایی (فرانسوی ← فارسی) درست است و این واژه دومین ورودِ همان واژهٔ عربی به فارسی است: سفری رفت‌وبرگشتی از عربی به زبان‌های رومی و فرانسه و باز به فارسی، در کنار «جُبّهٔ» گرهٔ نخست.\",\n     \"sources\": [\"https://abadis.ir/fatofa/%DA%98%D9%88%D9%BE/\", \"https://abadis.ir/fatofa/%DA%98%D9%88%D9%BE%D9%86/\"],\n     \"ref_check\": [\n      {\"ref\": \"VOP:204\", \"status\": \"not_checked\",\n       \"note\": \"Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi (Alborz 1371): refs_online.json records 'kind: none' — no copy found on archive.org, ketabnak, noorlib or the open web, so p.204 could not be seen. Its claim (Persian ژوپ/ژوپن from French) is independently confirmed by Abadis (Mo'in, Amid).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"فرهنگ معین s.v. ژوپن (via abadis.ir/fatofa/ژوپن)\", \"stance\": \"supports\",\n       \"note\": \"Mo'in: 'دامن کوتاه، پاچین (زنان)'; Amid: 'دامن کوتاه و آهاردار' — the word is lexicalised in the standard Persian dictionaries.\"},\n      {\"src\": \"ARY\", \"where\": \"ARY_pages.txt, grep 'ژوپ'\", \"stance\": \"silent\",\n       \"note\": \"No entry (Aryanpur covers only Indo-European inherited material of Persian, not modern French loans).\"},\n      {\"src\": \"BQT\", \"where\": \"Borhan-e Qate', grep 'ژوپ'\", \"stance\": \"silent\",\n       \"note\": \"A 17th-century dictionary cannot contain a 20th-century French loan; silence expected.\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"English\", \"words\": \"jupon, jupe, mini-jupe\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"Two of the three are genuine English words taken from French, as drawn: jupon, borrowed in the 14th c. (Chaucer, Knight's Tale) for the close-fitting surcoat worn over armour and later for a petticoat, and jupe, from Middle English jupe < Middle French jupe, a garment word now chiefly Scottish and historical. Klein and Funk & Wagnalls both give the chain (F. jupon > E. jupon). 'Mini-jupe', however, is not English: the French coinage of 1965 was borrowed into Persian (node #4) and into many other languages, but English made its own compound miniskirt and uses mini-jupe only as an italicised gallicism. Verdict plausible: the node is right for jupon and jupe, over-reaching for mini-jupe.\",\n     \"derivation_fa\": \"دو واژه از سه واژهٔ این گره به‌درستی وام‌واژه‌های انگلیسی از فرانسه‌اند: jupon که در سدهٔ چهاردهم میلادی وارد انگلیسی شد (چاسر، «حکایت شوالیه») به معنی نیم‌تنهٔ چسبانی که روی زره می‌پوشیدند و بعدها «زیردامنی»، و jupe از انگلیسی میانه jupe از فرانسهٔ میانه که امروز بیشتر اسکاتلندی و تاریخی است. کلاین و Funk & Wagnalls هر دو همین زنجیره را می‌دهند. اما «mini-jupe» واژهٔ انگلیسی نیست: این ساختِ فرانسویِ ۱۹۶۵ م. به فارسی (گرهٔ ۴) و بسیاری زبان‌های دیگر راه یافت، ولی انگلیسی ترکیب خودش miniskirt را ساخت و mini-jupe را تنها همچون واژه‌ای فرانسوی و بیگانه به کار می‌برد. حکم: با احتیاط پذیرفتنی است — گره برای jupon و jupe درست و برای mini-jupe فراتر از شواهد است.\",\n     \"sources\": [\"https://www.etymonline.com/word/jupon\", W+\"jupe\"],\n     \"ref_check\": [\n      {\"ref\": \"KLN:836\", \"status\": \"supports\",\n       \"note\": \"Klein, KLN_1966.txt leaf 451 (p.836): 'jupon, n., skirt, petticoat. — F., fr. Arab. jubbah ... Cp. gyp, jump, \\\"a kind of jacket\\\", jumper, \\\"blouse\\\".' The English headword is derived from French, as drawn; Klein has no mini-jupe.\"},\n      {\"ref\": \"FSD:1333\", \"status\": \"supports\",\n       \"note\": \"FSD_vol2.txt leaf 627 = p.1333 s.v. jupe: 'jupe, n. A heavy jacket; jupon; a long petticoat: the skirt of a dress'; leaf 628 (p.1334) gives the etymology '< OF. jupe/jupon ... < Sp. juba, < Ar. jubbah'. Both English headwords are there; mini-jupe is not (the 1913/1940 dictionary predates it).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"SKT\", \"where\": \"SKT.txt, grep '^JUPON'\", \"stance\": \"silent\",\n       \"note\": \"Skeat's Concise has no jupon/jupe entry.\"},\n      {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt (A-? only), grep 'jupon'\", \"stance\": \"silent\",\n       \"note\": \"Only vol. I of Webster's New Twentieth Century is available locally, so the J range could not be consulted.\"},\n      {\"src\": \"DEV\", \"where\": \"Devic p.147 s.v. Jupe\", \"stance\": \"partial\",\n       \"note\": \"Confirms the French words and their Arabic origin but says nothing about English.\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-228.json','w',encoding='utf-8') as f:\n    json.dump(data,f,ensure_ascii=False,indent=2)\n    f.write('\\n')\nprint('ok')\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk228.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-228.json > /dev/null && echo JSON-OK && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 228"
}
```


### [2026-09-06T15:39:25.333Z] TOOL RESULT

```
ok
JSON-OK
nodes verified: 13/13
node verdicts: {'confirmed': 10, 'plausible': 2, 'disputed': 1}
root verdicts: {'plausible': 1, 'confirmed': 2}
ref checks: {'not_checked': 3, 'partial': 3, 'supports': 9}
books consulted: {'supports': 19, 'silent': 10, 'contradicts': 4, 'partial': 5} | by book: {'KLN': 5, 'FSD': 4, 'BQT': 3, 'ARY': 3, 'SKT': 3, 'HJB': 3, 'DEV': 3, 'MON': 2, 'LAT': 2, 'LKT': 2, 'WEB': 2, 'LAM': 2, 'AID': 1, 'HRN': 1, 'HUB': 1, 'PHN': 1}
```


## [2026-09-06T15:39:31.043Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 -c \"\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nps=t.split('\\f')\nfor i,p in enumerate(ps):\n    if 'camel,  n.  —  ME.  camel' in p: print('leaf',i,'printed~',(i-12)*2); break\n\""
}
```


### [2026-09-06T15:39:32.881Z] TOOL RESULT

```
leaf 130 printed~ 236
```


## [2026-09-06T15:39:38.107Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 - <<'EOF'\nimport json,io\np='data/verification/page-228.json'\nd=json.load(open(p,encoding='utf-8'))\nfor e in d['entries']:\n    for n in e['nodes']:\n        for c in n.get('consulted',[]):\n            if 'actually leaf found by grep' in c['where']:\n                c['where']=\"KLN_1966.txt leaf 130 (printed pp. 235/236) s.v. camel\"\n        for c in n.get('consulted',[]):\n            c['where']=c['where'].replace('KLN_1966.txt s.v. camel','KLN_1966.txt leaf 130 (pp. 235/236) s.v. camel')\n    for c in e.get('consulted',[]):\n        pass\nio.open(p,'w',encoding='utf-8').write(json.dumps(d,ensure_ascii=False,indent=2)+'\\n')\nprint('done')\nEOF\ngrep -n \"leaf 130\" data/verification/page-228.json\npython3 tools/verify_check.py 228"
}
```


### [2026-09-06T15:39:40.048Z] TOOL RESULT

```
done
108:              "where": "KLN_1966.txt leaf 130 (printed pp. 235/236) s.v. camel",
186:              "where": "KLN_1966.txt leaf 130 (pp. 235/236) s.v. camel",
226:              "where": "KLN_1966.txt leaf 130 (pp. 235/236) s.v. camel",
nodes verified: 13/13
node verdicts: {'confirmed': 10, 'plausible': 2, 'disputed': 1}
root verdicts: {'plausible': 1, 'confirmed': 2}
ref checks: {'not_checked': 3, 'partial': 3, 'supports': 9}
books consulted: {'supports': 19, 'silent': 10, 'contradicts': 4, 'partial': 5} | by book: {'KLN': 5, 'FSD': 4, 'BQT': 3, 'ARY': 3, 'SKT': 3, 'HJB': 3, 'DEV': 3, 'MON': 2, 'LAT': 2, 'LKT': 2, 'WEB': 2, 'LAM': 2, 'AID': 1, 'HRN': 1, 'HUB': 1, 'PHN': 1}
```


## [2026-09-06T15:39:57.317Z] AGENT

Page 228 (book p. 198) verified — `/home/sfmqrb/git/rishe/data/verification/page-228.json`, `verify_check.py 228` shows 13/13 nodes, 0 PROBLEM lines.

**Counts** — roots: 2 confirmed, 1 plausible. Nodes: 10 confirmed, 2 plausible, 1 disputed. Ref checks: 9 supports, 3 partial, 3 not_checked (FVA, VOP — no digital copy exists for either).

**Disputed**
- J.b.b, node #3 French *jupe, jupon* ← Spanish *juba*: the Arabic origin is fine, but the Spanish intermediary is not the modern view. Littré/TLFi/Wiktionary route French *jupe* from Old Italian *giubba* (Arabic → Sicily → Italy → France), with Ibero-Romance *aljuba* a parallel direct borrowing; Klein, Pihan, Lammens all take French straight from Arabic *jubbah*. Only Funk & Wagnalls 1913 (FSD:1333, Nourai's source) draws the Spanish chain.

**Plausible (worth noting)**
- Jamal root + node #2 Greek *kamēlos*: Greek did not borrow from Arabic. Klein, Skeat, Webster, F&W and Wiktionary all give Phoenician 𐤂𐤌𐤋 / Hebrew *gāmāl*; Ernout–Meillet quote Varro's "suo nomine Syriaco in Latium uenit". Nourai's own AHD says only "of Semitic origin". Read the root box as Semitic *\*gamal-* and the chart works.
- J.b.b node #5 English *jupon, jupe, mini-jupe*: *jupon* (14th c., Chaucer) and *jupe* are real English loans from French; *mini-jupe* is not English (English coined *miniskirt*) — it is the Persian loan of node #4.

**Transcription flags:** none. "chameal" looked odd but is an attested Anglo-Norman spelling (Anglo-Norman Dictionary lists *chameal* beside *chamel, cameil, chamail* from c.1121-35), so node #4 is confirmed.

**Extraction errors:** none — I rendered PDF p. 228 and the JSON matches the printed page exactly, including the Persian «ژوپ ( مینی ژوپ ، ژوپن )».

**Notable ref finds:** Mo'in's Borhan footnote (BQT:592, found at BQT_v2 leaf 50, pp. 590-592) explicitly gives Sanskrit *jangala* (after Steingass) → North Indian languages → English *jungle*, confirming the whole Jangalah entry; KLN:836 was verified as the exact leaf carrying both *jungle* and *jupon*; FSD:1333 confirmed by the running head on FSD_vol2 leaf 627; PHN:221 is verbatim "JUPE, s. f. et JUPON". 15 web pages archived via `fetch_source.py`.
