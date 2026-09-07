# Verification process log — verify-page-308


## [2026-09-06T23:08:13.625Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 308 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-308.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-308.json. Write /home/sfmqrb/git/rishe/data/verification/page-308.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 308` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T23:08:15.161Z] AGENT

I'll start by reading the agent instructions.


## [2026-09-06T23:08:15.874Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T23:08:15.894Z] TOOL RESULT

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


## [2026-09-06T23:08:16.198Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-308.txt"
}
```


### [2026-09-06T23:08:16.215Z] TOOL RESULT

```
1	=== PDF page 308 (book page 278) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Leip : to smear with oil, cover, preserve  (refs POK:670)
4	#1 (parent #0) [Sanskrit] refs=BQT:991 | rěp : to deceive ; pra-rěp : cover, deceive
5	  #2 (parent #1) [Persian] refs=HRN:142,184; MON:1707 | farîb «فریب ( فریبا ، فریبنده )» : deceit, trick ; farîftan «فریفتن ( فریبیدن ، فریبش )» : to deceive ; rîv «ریو ( ریوه )» : deceit
6	#3 (parent #0) [Germanic] refs=AHD; KLN:874,887,899 | 
7	  #4 (parent #3) [English] refs=None | life, live, liver
8	--- entry 1 ---
9	ROOT [Indo-European] Leith : to go forth, die  (refs POK:672)
10	#1 (parent #0) [Avestan] refs=POK:672; WLD:401; ETM:66 | raěth, ris 1, rith : to die ; iris-ta, ris-ta : dead
11	  #2 (parent #1) [Pahlavi] refs=NYB:170; HRN:103 | rist : dead ; rist-axez : rising dead ☞Swîğ
12	    #3 (parent #2) [Persian] refs=BQT:948; HRN:136; NYB:170 | rastâxîz «رستاخیز ( رستخیز )» : rising of the dead
13	#4 (parent #0) [Germanic] refs=AHD | laipjan : to lead ; laidô : way
14	  #5 (parent #4) [English] refs=None | lead, load
15	--- entry 2 ---
16	ROOT [Indo-European] Lek : to leap, fly, kick  (refs POK:673; OEW:217)
17	#1 (parent #0) [Old Iranian] refs=AHM:182 | lakata, rakata : kick
18	  #2 (parent #1) [Persian] refs=AHM:182; MON:3620 | lagad «لگد ( لغد )» : kick
19	#3 (parent #0) [Greek] refs=OEW:217; POK:673 | lagadon : a leap, kick
20	  #4 (parent #3) [English] refs=OEW:217 | leg
21	#5 (parent #0) [Latin] refs=OEW:217 | locusta, lacertilia : leaping animals
22	  #6 (parent #5) [English] refs=AHD; KLN | locust, lobster, lizard, alligator
23	
```


## [2026-09-06T23:08:19.415Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-308.json",
 "description": "Read source JSON for page 308"
}
```


### [2026-09-06T23:08:19.457Z] TOOL RESULT

```
{
  "pdf_page": 308,
  "book_page": 278,
  "entries": [
    {
      "root": {
        "name": "Leip",
        "lang": "Indo-European",
        "refs": "POK:670",
        "gloss": "to smear with oil, cover, preserve"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "BQT:991",
          "words": [
            {"translit": "rěp", "gloss": "to deceive", "script": null},
            {"translit": "pra-rěp", "gloss": "cover, deceive", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "HRN:142,184; MON:1707",
          "words": [
            {"translit": "farîb", "gloss": "deceit, trick", "script": "فریب ( فریبا ، فریبنده )"},
            {"translit": "farîftan", "gloss": "to deceive", "script": "فریفتن ( فریبیدن ، فریبش )"},
            {"translit": "rîv", "gloss": "deceit", "script": "ریو ( ریوه )"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {"text": "که زنهار از این مکر و دستان و ریو - بجای سلیمان نشستن چو دیو", "poet": "Sa`dî"}
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD; KLN:874,887,899",
          "words": [],
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
            {"translit": "life, live, liver", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Leith",
        "lang": "Indo-European",
        "refs": "POK:672",
        "gloss": "to go forth, die"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:672; WLD:401; ETM:66",
          "words": [
            {"translit": "raěth, ris 1, rith", "gloss": "to die", "script": null},
            {"translit": "iris-ta, ris-ta", "gloss": "dead", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "NYB:170; HRN:103",
          "words": [
            {"translit": "rist", "gloss": "dead", "script": null},
            {"translit": "rist-axez", "gloss": "rising dead", "script": null, "see": ["Swîğ"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:948; HRN:136; NYB:170",
          "words": [
            {"translit": "rastâxîz", "gloss": "rising of the dead", "script": "رستاخیز ( رستخیز )"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {"text": "به کین من امروز تا رستخیز - نبینی جز از گرز و شمشیر تیز", "poet": "Ferdowsî"}
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "laipjan", "gloss": "to lead", "script": null},
            {"translit": "laidô", "gloss": "way", "script": null}
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
            {"translit": "lead, load", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Lek",
        "lang": "Indo-European",
        "refs": "POK:673; OEW:217",
        "gloss": "to leap, fly, kick"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Old Iranian",
          "refs": "AHM:182",
          "words": [
            {"translit": "lakata, rakata", "gloss": "kick", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "AHM:182; MON:3620",
          "words": [
            {"translit": "lagad", "gloss": "kick", "script": "لگد ( لغد )"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Greek",
          "refs": "OEW:217; POK:673",
          "words": [
            {"translit": "lagadon", "gloss": "a leap, kick", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "English",
          "refs": "OEW:217",
          "words": [
            {"translit": "leg", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Latin",
          "refs": "OEW:217",
          "words": [
            {"translit": "locusta, lacertilia", "gloss": "leaping animals", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "English",
          "refs": "AHD; KLN",
          "words": [
            {"translit": "locust, lobster, lizard, alligator", "gloss": null, "script": null}
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


## [2026-09-06T23:08:20.048Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-06T23:08:20.090Z] TOOL RESULT

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


## [2026-09-06T23:08:24.839Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','BQT','HRN','MON','AHD','KLN','NYB','WLD','ETM','AHM','OEW','ARY','IEC','SYN','SKT','LEW','LAT','BRT','PHD','HUB','CHEUNG','FSD','WEB']:\n    v=d.get(k)\n    print('==',k,json.dumps(v,ensure_ascii=False)[:700])\n\""
}
```


### [2026-09-06T23:08:26.641Z] TOOL RESULT

```
== POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index 
== BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.c
== HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the 
== MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol 
== AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifie
== KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO pri
== NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's 'NYB' nu
== WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015
== ETM {"title": "Mohsen Abolghasemi, Risheh-shenasi (Etimoloji), Qoqnus 1374/1995", "kind": "catalog", "url": "https://ketabnak.com/book/107170/ (no download) ; https://ketab.ir/book/2ebb5f53-ba49-4955-98f4-d419919d0ebc ; purchase: https://adinehbook.com/gp/product/9643110451", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: no digital copy on any permitted platform; catalogue/purchase only."}
== AHM {"title": "I. Gershevitch, The Avestan Hymn to Mithra, Cambridge 1959", "edition_found": "1959", "kind": "archive_djvu", "url": "https://archive.org/details/gershevitch-ilya-the-avestan-hymn-to-mithra-cambridge-university", "identifier": "gershevitch-ilya-the-avestan-hymn-to-mithra-cambridge-university", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHM.txt", "page_offset": "leaf = printed + 14 (e.g. leaf 18 = p.4). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Commentary is by stanza/note number; the Glossary (end of book) lists Avestan word
== OEW {"title": "J. T. Shipley, The Origins of English Words: A Discursive Dictionary of Indo-European Roots, Baltimore 1984", "edition_found": "1984 (lending-only)", "kind": "archive_restricted", "url": "https://archive.org/details/originsofenglish0000ship ; https://archive.org/details/originsofenglish00jose (both JHU 1984, borrowable) ; HathiTrust mdp.49015002910322 search-only ; Google ELSm5zUgP_wC no view", "identifier": "originsofenglish00jose (also originsofenglish0000ship)", "local_file": null, "page_offset": null, "lookup_hint": "Borrow via IA lending (djvu.txt returns 401/403). Entries are IE roots in alphabetical order; use IA's in-book search: https://archive.org/details/originsofenglis
== ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", "local_file": ["/home/sfmqrb/git/rishe/
== IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstruct
== SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i
== SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i
== LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.o
== LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for most of the book (e.g. leaf 21 = p.3); drifts in places (leaf 219 = p.301 -> -82?? probably a mis-detec
== BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between 
== PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<ident
== HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by parag
== CHEUNG null
== FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt", "page_offset": "vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: le
== WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/WEB_vol1.txt", "page_offset": "not reliably detected (page_numbers.json sparse); grep headword. local
```


## [2026-09-06T23:09:00.481Z] AGENT

Now let me look up the roots in the local Pokorny and other references.


## [2026-09-06T23:09:01.877Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor f in POK_01.txt POK_02.txt POK_03.txt; do echo \"### $f\"; grep -n -c '' $f | head -1; done\ngrep -n 'leip-' POK_02.txt | head -40"
}
```


## [2026-09-06T23:09:02.961Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n 'leit(h)\\|leith-\\|lei-t\\|leit-' POK_02.txt | head -30; echo \"---lek\"; grep -n '^lek-\\|lek-1\\|lek-2\\|lēk-' POK_02.txt | head -30"
}
```


### [2026-09-06T23:09:03.823Z] TOOL RESULT

```
### POK_01.txt
5152
### POK_02.txt
6716
### POK_03.txt
5975
5142:leip-  ,mit  Fett  beschmieren',  s.  unter  eigenem  Schlagwort.
5178:S.  unter  1.  leip-  ^beschmierend
5240:hieber  auch  lit.  vienuö-,  dvy-lika  usw.  ,11,  12^  usw.  (bis  19),  altlit.  liekat , elfter'  (,*was  über  die  zehn  hinaus  noch  überbleibt,  Überschuß^) ;  aber got.  ain-,  tioa-lifj  ahd.  ein-,  zwe-lif  ,11,  12^,  aisl.  ellifu,  anorw.  cellugu ,11^,  ellykti  ,der  11/  usw.  sind  entweder  zu  1.  leip-  zu  stellen  oder  mit Marstrander  (Eriu  5,  206)  aus  kelt.  *lipi-  {*lik^i-)  entleht.
5242:I.  leip-  ,mit  Fett  beschmieren,  kleben'  (daraus  auch  ,sich  anheftend  hinauf- klettern, klettern');  wohl  Erweiterung  zu  lei-  , schleimig'.
```


### [2026-09-06T23:09:03.875Z] TOOL RESULT

```
235:E.  glei-,  z.  T.  mit  weiterer,  konsonantischer  Ableitung  (bes.  glei-t-,  -d-, glei'bb-,  glei-m-)  ,kleben,  schmieren',  aber  wohl  ursprüngl.  abgeleitet von  gel-  ,ballen';  nach  Specht  Dekl.  144  Grundbed.  ,glänzend'  (zu gel-,  gel-?)]  nominal:  gli-io-,  -no-,  -tu-;  gloi-uo-.
252:glei't'  in  ags.  cetcllpan  , festkleben,  anhangen',  schwachstufig  cZida, clioda  m.  ,Wundpflaster',  ags.  cUde  ,Klette'  (,die  anhaftende'),  ahd.  kledda, kletta,  ndl.  klis,  klit  ,Klette',  nhd.  klettern-,  auch  wohl  mhd.  kleit,  nhd.  E2e%d, ags.  cläd  ds.;  mhd.  kllster  ,Kleister',  nisl.  kllstra  ,kleistern'  (als  ^gleit-tro- hierher  oder  mit  dem  germ,  Formans  -stra-  von  der  einf.  Wzf.  *kli-j  idg. glei-)',  norw.  kleisa  ,kleben;  (mit  der  Zunge  kleben  =)  lispelnd  oder  unrein reden',  anord.  kleiss  l  male  ,stotternd^
4076:ilei-tu-s  f.  , Abhanges  klei-trä  ,StangeiigerippeS  S:ieio-s,  kli-tö-s  angelehnt', kli-ti'S  ,Neigung%  klei-uo-s,  kloi-uo-s  ,Hügel%  kloi-no-s  , schräg*.
5143:lei-t-  , darüber  streichen,  sanft  berühren,  streicheln':  wahrscheinlich Xlttj  , Bitte',  XLaao(.iac,  ?Jto(X(xl  ,bitten,  flehen',  Xlravog  ,flehend',  Xiravevü) , flehe';  lat.  litäre  ,unter  günstigen  Vorzeichen  opfern;  sühnen,  versöhnen' (beruht  auf  Hitä  aus  Xivr])]  lit.  lyteti  , berühren',  lett.  läittt  , streichen, streicheln',  lit.  lieciii,  liesti  , berühren,  betreffen'.
5269:1.  leit-  , verabscheuen;  freveln*^.
---lek
```


## [2026-09-06T23:09:08.810Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '5242,5300p' POK_02.txt"
}
```


### [2026-09-06T23:09:08.864Z] TOOL RESULT

```
I.  leip-  ,mit  Fett  beschmieren,  kleben'  (daraus  auch  ,sich  anheftend  hinauf- klettern, klettern');  wohl  Erweiterung  zu  lei-  , schleimig'.
Ai.  lip-  (limpdti-,  lipydte)  , beschmieren',  liptd-  ,klebend,  an  etwas  haf- tend^, lepayati  ,beschmiert'  (=  slav.  Upiti),  rip-  , schmieren,  kleben,  be- trügen'; rip-  f.  ,Betrug;  Verunreinigung'  (=  gr.  XiTta  Akk.),  lepa-  m. ,das  Bestreichen,  das  Aufgestrichene,  Schmutz',  ripas-  n.  ,Fleck,  Schmutz', riprd-  n.  , Schmutz'  (ähnlich  gr.  XiuaQog,  alb.  laparös),  ripu  , tückisch, Betrüger' ;
nipers.  fi-reftmi  , betrügen',  rew  ,Betrug',  osset.  fä-letvun,  -llwyn  ,betrügen';
gr.  XiTcog  n.  ,Fett',  Xcrcagög  ,fett,  gesalbt',  mit  Auslautentgleisung  äXsiq)^ ,salbe',  ^lei(paq,  äloicpri  ,Salbe' ;  mit  der  Bed.  ,klettern'  (wie  lit.  lipü,  lipti) gr.  aiyiXiip  ,nur  von  Ziegen  erkletterbar',  HXixp'  nhqa  Hes.,  eig.  ,uner- steiglich',  Xlip'  Tthqa,  äcp"  ^g  VSwq  gtoCsi  Hes.;
alb.  laparös  , beschmutze,  stinke',  laperdhi  , schmutzige  Rede',  gelepe^ shklepei.j  glep  , Augenbutter'  (Präfix  ke- ~\- *loipos  oder  Hoipä)]
lat.  lippus  , triefäugig,  triefend'  (mit  expressiver  Konsonantenschärfung) ;
got.  hileiban,  ahd.  hillban  ,bleiben',  ags.  bellfan  , bleiben,  übrigbleiben' (zum  l  s.  Meillet  MSL.  14,  351),  Kaus.  got.  bilaibjan;  aisl.  leifa,  ahd. leiben,  ags.  Töefan  ,übriglassen' ;  got.  laiba  f.,  aisl.  leif,  ahd.  leipa,  3Lgs.  läf ,Überbleibsel' ;  got.  aflifnan,  aisl.  lifna  ,übrigbleiben',  aisl.  Ufa  ,übrig  sein';
germ.  llb-  ,(kleben)  bleiben'  hat  auch  die  Bed.  ,übrigbleiben'  von  llh {leik^-  ,verlassen')  aufgesaugt,  das  dadurch  nunmehr  in  der  Bed.  ,über- lassen,  leihen'  lebendig  blieb;
[eine  verschiedene,  auch  in  lat.  cae-lebs  aus  *caivi-lib-  (s.  kai-  ,allein') vorliegende  Wz.  *leibh-  ,leben'  enthalten  got.  liban  (3.  Sg.  libaip),  ahd. leben,  as.  libbian,  lebön,  ags.  libban,  aisl.  Ufa  ,leben',  lifna  ,lebendig werden';  Siisl.  llf  n.,  ags.  lif,  as.  llf  llb  n.  ,Leben',  ahd.  llb,  llp,  mhd. Zip,  libes  m.  n.  ,Leben ;  Leib,  Person'] ;
lit.  livipii,  lipti  ,klebenbleiben'  (und  lipii,  lipti  ,klettern',  s.  oben),  li'pniis
671
klebrig^  Up^s  ,ds.^  anhänglich',  lett.  lipu,  lipt  ^anhangen',  lipigs  ^klebrig', lipns^   laipns  ^mild,  leutselig,  freundlich';
slav.  *^ftw^,  *lhnoti  in  aksl.  pri-Unqti  , ankleben'  und  slav.  *hpHi  in  aksl. pri'hpljg,  pri-hpäti  , ankleben',  dazu  Kaus.  aksl.  pri-Upiti  s§  ds.,  usw. und  aksl.  Häpz  m.  ,Leini'  (=  ai.  lepa-)^  auch  abg.  lep^  ,passend,  schön' (ursprüngl.  , anklebend') ;
toch.  A  lip'  ^übrigbleiben' ;  lyipär  ,Rest' ;
hitt.  lip'  ^schmieren'.
WP.  II  403  f.,  WH.  I  811  f.,  Trautmann  161  f.,  Jokl  L-k.  U.  314,  Specht KZ.  64,  67.
2.  leip'  ,begehren,  etwas  von  jemandem  verlangen'.
Gr.  Xl7trofj,aCj  jünger  XiftTo),  Partiz.  Perf.  Med.  (in  akt.  Bed.)  Xslifiixivog ^begehren',  llip'  iTti-d-v^la  Hes.,  Xixpovqla  , Verlangen  zu  pissen';
lit.  liepiit,  liepti,  pa-liepti  , befehlen',  apr.  pallaips,  Akk.  -san  , Gebot' (-so-St.),  pallaipsl  twei  , begehren',  laipinna  , gebot'.
WP.  II  404,  Trautmann  155.
leis-  ,am  Boden  gezogene  Spur,  Geleise,  Furche',  im  Germ,  daraus  auch verbale  Bildungen  für  ,nachspüren,  auch  im  geistigen  Sinne';  loisä , Furche'.
Lat.  llra  [Heisa)  ,Furche  im  Ackerbeet',  dellrus  , geistig  aus  dem  Geleise gekommen,  verrückt',  dellrö,  -äre  ,aus  dem  Geleise  kommen,  verrückt sein'  (auch  dialekt.  delerus,  deleräre) ;  umbr.  disleralinsust  ,inritum  fecerit* i^dis-leisa-li)  ;
ahd.  wagan-leisa  , Wagenspur'  (=  abg.  lecha),  mhd.  leis(e)  ,Spur, Geleise';  schwundstufig  mndl.  lese  (*lis-)  f.  ,Spur,  Furche,  Furche  im Gesicht,  Runzel',  ahd.  lesa  ,Runzel';  got.  laists  m.  ,Spur'  (i-St.  f.  älteren o-St.),  aisl.  leistr  m.  ,Fuß;  Socke',  ags.  last,  Icest  , Fußspur,  Spur';  ahd. mhd.  leist  ,Spur,  Leisten'  {*lois-to-),  wovon  got.  laistjan  ,(auf  der  Spur) nachfolgen,  nachstreben',  ahd.  leisten  ,einem  Gebote  oder  Versprechen nachkommen,  leisten',  ags.  Icestan  , folgen,  helfen,  ausführen,  aushalten' (engl,  last  , dauern') ;  got.  lists  f.  ,List',  aisl.  list  f.  ,Kunstfertigkeit,  Scharf- sinn', ahd.  as.  ags.  list  , Kunstfertigkeit,  Klugheit,  List'  (abg.  hstb  ,List, Betrug'  aus  got.  lists) ;  got.  lais  Prät.-Präs.  ,ich  weiß,  d.  i.  verstehe  etwas zu  tun'  (Y orhild  loait),  Kaus.  laisjan  ,lehren'  (galaisjan  sik  ,lernen');  ahd. lerran,  lereUj  as.  lerian,  ags.  Iceran  , lehren'  (eig.  ,jmdn.  eine  Spur  führen') ; ahd.  Urnen,  lernen,  lernön  (Hiznön),  afries.  lirna,  lerna,  ags.  leornian ,lernen',  as.  llnön  ds. ;  got.   lubja-leis  ,giftkundig'  (Vorbild  weis)-,
abg.  lecha  , Ackerbeet',   russ.  lechd,  skr.  lijeha,  cech.  Ucha  (*loisa)'j
lit.  lyse  , Gartenbeet',  apr.  lyso  , Ackerbeet'.
WP.  II  404  f.,  WH.  I  812  f.
672  •
1.  leit-  , verabscheuen;  freveln*^.
Gr.  älsixriq  ^Frevler',  äol.  älo'iTrjg  ,Räclier'^  äloixög  ,Frevler^,  ^liTalvuv ^freveln,  sündigen^,  dliv^ixcov  ^Sünder^  Frevler^,  äXirgög  ;ds.^  böse;
air.  Uuss  , Abscheu^  {Hit-tu-),  ni  er-lissaigther  ^nunquam  fastiditur^;
anord.  leid?-  ^unangenehm ;  verhaßt^,  ags.  lad  (engl,  loath),  as.  leth^  ahd leid  ds.^  nhd.  Subst.  Leid  (im  Ursprung  ganz  verschieden  vom  Verbum leiden) ;
daß  got.  sleipja  (N.  PL  n.)  ^schädlich,  schlimm'^;  anord.  slldr  ;Schliinm* ags.  slide,  as.  slithi  ^grimmig^^  grausam,  böse^,  ahd.  slldic  ds.  unter  An- nahme eines  beweglichen  s-  anzureihen  seien,  scheint  möglich.
WP.  II  401,  WH.  I  813,  Schwyzer  Gr.  Gr.  1,  411.
2.  Ieit(hy  , fortgehen;  sterben;  gehen'.
Av.  7'ae-d--  , sterben^  (Präs.  iri&yeiti):
got.  ga-leipan  ,gehen',  anord.  Uda  st.  V.  ,gehen,  vergehen,  dahinschwinden verlaufen,  zu  Ende  g"ehen,  verscheiden',  as.  llthan  st.V.  ,gehen,  wandern, fahren,  befahren,  vergehen',  schw.  V.  lithon  ,bringen,  sich  begeben';  ags. Upan  St.  V.  ,gelien,  reisen',  ahd.  lldan  st.  V.  ,einen  Weg"  nehmen,  gehen, fahren,  weggehen,  vergehen,  verderben;  erfahren,  erleben,  leiden',  nhd.- leiden  (verschieden  vom  Subst.  Leid,  s.  Heit-  ,verabscheuen') ;  anord.  liS> n.  ,Fahrzeug',  ags,  n.  , Fahrzeug,  Schiff';  ahd.  üz-lit  ,excessus';  -__  
germ.  Haidö:  1.  ,Weg'  in  aisl.  leid  f.  ds.,  ags.  lad  ds.,  ,Wasserlauf', Primärbildg.  zu  germ.  llpan  ,gehen,  fahren';  2.  ,Führung'  in  ags.  lad  f. n.  ds.,  , Transport,  Unterhalt',  ahd.  leita  , Führung',  zum  Kausat.  germ. Haidjan  , gehen,  machen,  führen';  3.  ags.  lad  , Reinigungseid',  afränk. lade  ds.,  auch  zu  Haidjan  als  , Beibringen  von  Eideshelfern',  auch  ahd. laida  (das  d  von  leida  ,Anklage');
Kaus.  (germ.  Haidian)  anord.  leida  ,führen,  geleiten,  begleiten',  ags. l^dan,  as.  ledian  ,leiten,  bringen',  ahd.  leittan,  leiten  ,leiten,  führen,  mit sich  tragen,  haben';  anord.  lidinn  ,tot',  Uidi  n.  ,Grabstätte'  (,*Geleit'), ahd.  leita  (Heitia),  leiti  ,funus'  (,*zu  Grabe  geleiten'),  mhd.  hileite  n.  ,Be- gräbnis';  mit  letzterer  Bed.  vermutlich  auch  gr.  loirrj  ytacpog^,  XoiTsveLv' d-aTtTBiv  Hes.,  auch  loirög'  XoL(j>ög  Hes.?
toch.  A  lit-  , fortgehen,  herabfallen'.
Ob  Erweiterung  von  *lei-  ,sich  ducken,  verschwinden'??  Vgl.  got.  aflinnan ,fortgehen'  usw.
WP.  II  401  f.,  Wissmann  Postverbalia  57  f.
leizd-,  loizd-  ,Rand,  Saum'.
Ahd.  llsta  , bandförmiger  Streifen,  Saum,  Borte,  Leiste',  nhd.  Leiste, ags.    llst  ,Rand,   Saum,    Kante'   (aus   asächs.   Zis^a :  aisl.  lista  f.  ,Streifen,
j
Ö73
^      Kante;  Leiste');    alb.  leih   ^der   erhöhte  Rand    eines    Grundstückes^  Rain, ;      ^(auer;  Flußufer^  (Hoizd-). '  WP.  11  405.
'      nek-'^)'  ^^^~  ^tadeln,  schmähen^?    Nur  keit.  und  germ. ^    *      Air.  locht  m.  (*lok-tu-)  , Schuld,  Fehler^;
ahd.  as.  lahan,  ags.  Uan  ;,tadeln^,  nisl.  Id  ds.,  ags.  leahtor  in.  ,Laster, Verbrechen,  Tadel^,  mnl.  lachter  ,Schande,  Hohn^;  afries.  lasier,  ahd.  as. lastar  ,Tadel,  Schimpf,  Fehler^  {*lahstra-\  aisl.  Igstr  m.  , Fehler,  Laster' (*lahstru-).
Unklar,  ob  mit  lengh-  ,schmähen^  zu  verbinden    (Osthoff  MU.  VI  7  ff.). WP.  II  436  f.
2,  lek-  (:  Uk-)  und  lek-  :  lok-  in  Worten  für  , Gliedmaßen^  und  für  ,biegen, winden,  springen,  zappelnd
Ai.  r^salä  ,Fußgelenk  bei  Huftieren^  (*lk-s-elä) ;
gr.  Xd^,  Xdydrjv  ,mit  dem  Fuße  ausschlagend',  laxi^tög  (*lay,a(j,og)  ,das Ausschlagen  mit  dem  Fuße*",  Aaxr/^w  , stoße  mit  dem  Fuße^,  AdxTfg,  -tog ,Mörserkeule'^ ;  ablaut.  hrf^äv  td  nqdg  (pdrjv  dgxsi^^cci,  Irj-^fiaaL'  nard^ai Hes.  (:lett.  Ifkät);  ?uy,€gzi^etv'  oyciQT&v  Hes.  {*l,q-)'j  s.  liy.Qoi  u.  dgl.  S.  308 unter  el-  , biegen';
ob  lat.  lacertus,  meist  PI.  ,die  Muskeln,  bes.  der  Oberarm^,  lacerta  , Ei- dechse' (,die  Biegsame')??  lacca  , Geschwulst  an  den  Unterschenkeln  der Zugtiere^  (wäre  eine  späte  Kurzform  mit  Kons. -Gemination);  locusta , Heuschrecke ;  Meerkrebs'  (,mit  Gelenken  versehen'?);?
gall.-rom.  *lakä7'e  ,biegen',  v.  Wartburg  FEW  s.  v. ;
aisl.  leggr  ,Unterbein,  Knochen',  arm-,  hand-leggr  ,Arm',  föt-,  löer-leggr ,Wade'  (Hagiz);  langob.  lagi  ,Schenkel';  aisl.  löer,  aschwed.  lär  ds.  (*lahaz- oder  Hehaz-  n.),  ags.  llra  ,das  Dickfleisch  an  Waden,  Schenkeln,  Weichen und  Gesäß'  {Higizan-)\  mhd.  lecken^  nhd.  alt  locken  ,hinten  ausschlagen, hüpfen',  norw.   dial.  lahka  ,(auf  einem  Fuß)   hüpfen,   trippeln'  (*lakjan)'^
lit.  lekiü,  llkti  ,fliegen',  Iterat.  lakstyti  ,hin  und  her  fliegen',  Kausat, lakinti  ,fliegen  machen',  laktä  , Hühnerstange'  (,*Aufflug'),  laküs  ,flüchtig, behend',  lett.  lezu,  lekt  ,springen,  hüpfen',  Iterat.  Ifkät  (:  lrjY.äv)y  lekas f.  PI.  , Herzschlag';  apr.  lagno  (aus  Hakno)  , Beinkleid,  Hose';  vielleicht abg.  -leUq,  -leteti  ,fliegen',  wenn  aus  *lek-t-  vor  dunklen  Vokalen  oder aus  lek-  und  pet-  kontaminiert.
WP.  I  420  f.,  WH.  I  743  f.,  Trautmann  156;  vgl.  auch  oben  S.  308  f.
/.  lek- :  lok-  ,Reis,  zur  Schlinge  gedrehtes  Reis  oder  Strick,  in  einer  solchen fangen*  ?  ?  Wort  der  Jägersprache  (Vendrjes  Arch.  Ling.  I  25). Lat.    laciöj   -ere   ,locken',    laeessö,   -ere   ,herausfordern,   necken,   reizen',
43
```


## [2026-09-06T23:09:29.064Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD leip\"; grep -n -i 'leip-\\|leit-\\|^lek-\\|lek-\\.' AHD_watkins1985.txt | head -30\necho \"=== AHD context\"; grep -n -i 'locusta\\|lacerta' AHD_watkins1985.txt | head -20"
}
```


### [2026-09-06T23:09:29.121Z] TOOL RESULT

```
=== AHD leip
280:al-1, Beyond. 1. Variant *ol-, “beyond,” in: a. suffixed forms “*ol-se-, *ol-so- in Old Latin ollus in Latin ille (feminine illa); “yonder,” that: ALARM, ALERT, ALLIGA- TOR; b. suffixed forms “*ol-s, *ol-tero- in Latin uls, *ulter, ultra; beyond: OUTRE, ULTERIOR, ULTIMATE, ULTRA-, UTTERANCE®, 2, Suffixed form *al-tero-, “other of two,” in: a. Latin alter, other, other of two: ALTER, ALTER- CATE, ALTERNATE, ALTRUISM; SUBALTERN; b. Latin adulier, “one who approaches another (unlawfully), an adulterer” (ad-, to; see ad-), hence adulterdre, to commit adultery with, pollute: ADULTERATE, ADULTERINE, ADULTERY. 3. Extended form *alyo-, “other of more than two,” in: a. Germanic *aljaz (with adverbial suffix) in Old English elles, else, otherwise: ELSE; b. Latin alius, other of more than two: ALIAS, ALIEN; ALIBI, ALIQUOT, HIDALGO; Cc. Greek allos, other: AGIO, ALLO-; ALLEGORY, ALLELOMORPH, MORPHALLAXIS, PARALLAX, PARALLEL, TROPHALLAXIS. [Pok. 1. al- 24.] al-2, To wander. 1. Latin ambuldre, to go about, walk (ambi-, around; see ambhi): ALLEY!, AMBULATE; FU- NAMBULIST, PREAMBLE. 2. Latin exsul, exul, wanderer, exile (ex-, out; see eghs): EXILE. [Pok. 3. al- 27.] al-3, To grow, nourish. I. Suffixed (participial) form *al-to-, “grown,” in: 1. Germanic *alda- in: a. Old Eng- lish eald, ald, old: ALDERMAN, OLD; b. Old English (comparative) ieldra, eldra, older, elder: ELDER}; c. Old English (superlative) ieldesta, eldesta, eldest: ELDEST; d. Germanic compound *wer-ald-, “life or age of man” (see wi-ro-). 2. Latin altus, high, deep: ALT, ALTIMETER, ALTO, HAUGHTY, HAWSER; ALTITUDE, ALTOCUMULUS, ALTOSTRATUS, ENHANCE, EXALT, HAUTBOY. II. Latin alere, to nourish: ADOLESCENT, (ADULT), ALIBLE, ALI- MENT, ALIMONY, ALTRICIAL, ALUMNUS; COALESCE. III. Suffixed (causative) form “ol-eye- in Latin abolére, to retard the growth of, abolish (ab-, from; see apo-): ABOLISH. IV. Compound form “pro-al- (pro-, forth; see per’) in Latin prélés, offspring: PROLAN, PROLETARIAN, PROLIFEROUS, PROLIFIC. V. Extended form *aldh- in Greek althein, althainein, to get well: ALTHEA. [Pok. 2. al- 26.] al-4, To grind, mill. Suffixed form ‘*al-euro- in Greek aleuron, meal, flour: ALEURONE. [Pok. 5. al- 28.] [al-5. All. Germanic root. Suffixed form *al-na- in Ger- manic *allaz in Old English all, eall, eal-, al-, all: ALL; ALSO.] albho-. White. 1. Possibly Germanic ‘*albiz, *albaz, if meaning “white ghostlike apparitions,” in: a. Old Eng- lish e/f, elf: ELF; b. Old Norse alfr, elf: OAF; c. Old High German Alberich, “elf-ruler,” akin to the source of Old French Auberon: OBERON. 2. Latin albus, white (> Old Spanish alba, dawn): ABELE, ALB, ALBEDO, ALBESCENT, ALBINO, ALBITE, ALBUM, ALBUMEN, ALBURNUM, AU- BADE, AUBURN; DAUB. 3. Greek alphos, dull-white lep- rosy: ALPHOSIS. [Pok. albho- 30.] alek-. To ward off, protect. Earlier form *olek-. 1. Suf- fixed zero-grade form “alk-d- in Greek alké, strength: ANALCIME. 2. Extended form *aleks- in Greek alexein, to protect: ALEXIPHARMIC. [Pok. aleg- 32.] algwh-. To earn, be worth. Sanskrit arhati, he is worthy: ARHAT. [Pok. algvh- 32.] alu-. In words related to sorcery, magic, possession, and intoxication. Suffixed form *alu-t- in Germanic *aluth- in Old English (e)alu, ale: ALE. [Pok. alu- 33.] ambhi. Also mbhi. Around. Probably derived from ant-. 1. Reduced form *bhi in Germanic *bi, *bi- (intensive prefix) in: a. Old English bi, bi, be, by: By}; b. Old English bi-, be-, on all sides, be-, also intensive prefix: BE-; C. Middle Dutch bie, by: BILANDER; d. Old High German bi (> German bei), by, at: Brvouac. 2. Germanic *umbi in: a. Old English ymbe, around: EMBER DAY;
652:kwelek-. Bundle. Proposed by some as the root of Latin culcita, mattress, sack, which is more likely of unknown origin: QUILT. [Pok. kuelak- 630.] kwelp-. To arch. 1. Germanic *hwalbjan in Old English *hwelfan, hwylfan, with parallel form *hwelman (> Middle English whelman), to turn over: WHELM. 2. Suf- fixed o-grade form *kwolp-o- in Greek kolpos, bosom, womb, vagina: GULF; COLPITIS, COLPOSCOPE, COLPOS- copy. [Pok. 2. kuelp- 630.] kwen-. Holy. Suffixed zero-grade form *kwn-s-lo- in Germanic *hunslam in Old English hisl, hiisel, Eucha- rist: HOUSEL. [Pok. kuen- 630.] kwent(h)-. To suffer. 1. Suffixed form *kventh-es- in Greek penthos, grief: NEPENTHE. 2. Zero-grade form *kenth- in: a. Greek pathos, suffering, passion, emotion, feelings: PATHETIC, PATHO-, PATHOS, -PATHY; PATHOGNO- MONIC, SYMPATHY; b. suffixed form *k“nth-sko- in Greek paskhein, to feel, suffer: PROTOPATHIC. [Pok. kventh- 641.] kwép-. To smoke, cook, move violently, be agitated emotionally. Hypothetical base of possibly related words. 1. Suffixed variant form *kup-yo- in Latin cupere, to desire: COVET, CUPID, CUPIDITY; CONCUPISCENCE. 2. Zero-grade form *kwap-, becoming *kwap- possibly in: a. Latin vapor, steam, vapor: VAPOR; EVAPORATE; b. Latin vapidus, that has emitted steam or lost its vapor, flat, poor: VAPID; c. Greek kapnos, smoke: ACAP- niA. [Pok. kuép- 596.] kver-1, To make. 1. Sanskrit karoti, he makes: SANSKRIT. 2. Suffixed form *kver-6r with dissimilated form *kel-6r in Greek pelér, monster (perhaps “that which does harm”): PELORIA. 3. Suffixed form *ker-as- in Greek teras, monster: TERATOCARCINOMA, TERATOGEN, TERA- TOID, TERATOMA. 4, Suffixed form *ker-mn in Sanskrit karma, act, deed: KARMA. [Pok. 1. kver- 641.] kwer-2. Something shaped like a dish or shell. Suffixed variant form *k”ar-yo- in Scottish Gaelic coire, cauldron, hollow, whirlpool: corrt&. [Pok. 2. kver- 642.] kwerp-. To turn oneself. 1. Germanic *hwarb- in Old English hwearf, wharf (< “place where people move about”): WHARF. 2. Germanic *hwerban in: a. Old Norse hverfa, to turn: VARVE; b. Old Norse *hvirfa, to whirl, perhaps assimilated to Danish hvirre, to whir, akin to the Scandinavian source of Middle English whirren, to whir: WHIR; C. Old Norse hAvirfla, to whirl: WHIRL; d. Old North French werble, a warbling: WARBLE!. 3. Possibly suffixed zero-grade form *kwrp-o- in Greek karpos, wrist: CARPAL, CARPUS. [Pok. kuerp- 631.] kwes-. To pant, wheeze. 1. Germanic *hwésjan in Old Norse huzsa, to hiss: WHEEZE. 2. Latin queri, to com- plain: QUARREL!, QUERULOUS. 3. Suffixed zero-grade form *kus-ti- in Greek kustis, bladder, bag (< “bellows”): cyst, cysTo-. [Pok. kues- 631.] kwé6t-. To shake. Zero-grade form *kwet-, becoming *kwat- in Latin quatere (past participle quassus, in composition -cussus), to shake, strike: CASCARA, KVETCH, SCUTCH, SQUASH?; CONCUSS, DISCUSS, PERCUSS, RESCUE, succussIoNn. [Pok. kuét- 632.] kvetwer-. Four. I. O-grade form *ketwor-. 1. Probably Germanic *fe(d)wor- in: a. Old English féower, four: Four; b. Old English féowertig, forty: FORTY; c. Old English féowerténe, fourteen: FOURTEEN. 2. Latin quat- tuor (> Italian quattro), four: CAHIER, CARNET, QUATRAIN; CATER-CORNERED, QUATTROCENTO. IT. Mul- tiplicatives *kveturs, kvetrus, and combining forms *kvetur-, *kvetru-. 1. Latin quater, four times: (CARIL- LON), QUATERNARY, QUATERNION, QUIRE’. 2. Latin gua- drus, four-sided thing, square: CADRE, QUADRATE, QUARREL?, QUARRY?; SQUAD, SQUARE, TROCAR. 3. Latin quadri-, four: QUADRI-. 4. Latin quadra, square: QUA- DRILLE!. 5, Latin quadrdns, a fourth part: QUADRANT. 6. Latin quadrdagintd, forty (-gintd, ten times; see dekm): QUARANTINE. 7. Variant form *ket(w)r- in: a. Greek tetra-, four: TETRA-; b. Greek tessares, tettares,
671:extensions in: a. Old English slim, slime: sLIME; b. Old English slipor, slippery: SLIPPERY; Cc. Old English *slice, smooth (> Middle English slike, smooth): sLick; d. Old English lim, cement, birdlime: LIME; e. Old English lam, loam: LOAM; f. Old Norse s/éttr, smooth, sleek, akin to the probable Scandinavian source of Middle English slight, slender: SLIGHT; g. Middle Dutch and Middle Low German slippen, to slip, slip away, akin to the probable source of Middle English slippen, to slip: sL1P!; h. Middle Low German slépen, to drag: SCHLEP. 2. Suffixed form *lei-mo- in Latin limus, slime: LIMACINE, LIMICOLINE. 3. Suffixed form */ei-w- in Latin oblivisci (ob-, away; see epi), to forget (< “to wipe, let slip from the mind”): OBLIVION, OUBLIETTE. 4. Extended form *(sjleia- in: a. nasalized zero-grade form */i-n-a- in Latin linere, to anoint: LINIMENT; b. Suffixed zero-grade form *li- (< *lig-) in Greek litos, plain, simple: LiToTEs. [Pok. 3. lei- 662.] léi-. Also lei-. To flow. 1. Extended form “/eib- in Latin libdre, to pour out, taste: LIBATION; PRELIBATION. 2. Possibly suffixed extended form */eit-os- in Latin litus, shore: LITTORAL. [Pok. 4. lei- 664.] leid-. To play, jest. Suffixed o-grade form *loid-o- in Latin lidus, game, play, with its derivative lidere, to play (but both words may possibly be from Etruscan): LUDICROUS; ALLUDE, COLLUDE, DELUDE, ELUDE, ILLU- SION, INTERLUDE, PRELUDE, PROLUSION. [Pok. leid- 666.] leie-. To waste away. Zero-grade form “li- (< *lia-) in Greek limos, hunger, famine: BULIMIA. [In Pok. 2. lei- 661.] leig-'. To bind. 1. Germanic */ik- in Middle Low German lik, leech line: LEECH?. 2. Zero-grade form */ig-d- in Latin ligare, to bind: LEAGUE!, LEGATO, LIABLE, LIEN, LIGASE, LIGATE; ALLOY, (ALLY), COLLIGATE, COLLIGATIVE, FURL, OBLIGE, (RALLY), RELY. [Pok. 4. leig- 668.] leig-?. Poor. Perhaps Greek oligos, few, little: OLIGO-. [Pok. 1. leig- 667.] leig-5. To leap, tremble. O-grade form */oig- in Germanic *laik- in: a. Old English -lac, suffix denoting activity: WEDLOCK; b. Old Norse leika, to play: LARK?. [Pok. 3. leig- 667.] leigh-. To lick. 1. Greek leikhein, to lick: ELECTUARY. 2. Zero-grade form *lig- in Germanic *likk6n in: a. Old English liccian, to lick: Lick; b. Old French lechier, to live in debauchery: LECHER. 3. Nasalized zero-grade form *ling- in Latin lingere, to lick: ANILINGUS, CUNNI- LinGus. [Pok. leigh- 668.] leikw-, To leave. 1. Basic form *leikv- in Greek leipein, to leave: ECLIPSE, ELLIPSIS. 2. O-grade form *loikv- in: a. Germanic */aihwnjan in Old English lénan, to lend, give (< “to leave to”): LEND; b. suffixed form *loikv-nes- in Germanic */aihwniz in Old Norse Jan, loan: LOAN. 3. Zero-grade form *likv- in Germanic *-lif-, left, in: a. Germanic *ain-lif-, “one (beyond ten),” in Old English endleofan, eleven (see oi-no-); b. Germanic *twa-lif-, “two left (beyond ten),” in Old English twelf, twelve (see dwo-). 4. Nasalized zero-grade form *li-n-kv- in Latin linquere, to leave: DELINQUENT, DERELICT, RELINQUISH. [Pok. leike- 669.] leip-. To stick, adhere; fat. 1. Germanic *libam in Old English Jif, life (< “continuance”): LIFE, LIVELY. 2. Ger- manic “libén in Old English lifian, libban, to live: LIVE}. 3. Germanic */aibjan in Old English léfan, to leave, have remaining: LEAVE!. 4. Germanic “libro in Old English lifer, liver (formerly believed to be the blood-producing organ): LIVER}. 5. Zero-grade form *lip- in Greek lipos, fat: L1po-. 6. Variant form *aleibh- in Greek aleiphein, to anoint with oil (> aleiphar, unguent): ALIPHATIC; SYNA- LEPHA. [Pok. eip- 670.] leis-'. Track, furrow. 1. O-grade form *lois- in: a. Ger- manic */aist- in Old English Jast, lést, sole, footprint: Last’; b. Germanic */laistjan, “to follow a track,” in Old English /éstan, to continue: LAST?; c. suffixed form *lois-G in Germanic */aiz6 in Old English Jar, learning:
676:leit-'. To detest. 1. Germanic */aithaz in Old English lath, loathsome: LOATH. 2. Germanic */aithén in Old English lathian, to loathe: LOATHE. [Pok. 1. leit- 672.]
677:leit-2. To go forth, die. 1. Suffixed o-grade form *loit-eyo- in Germanic *laidjan in: a. Old English dan, to lead: LEAD!, b. Old High German /eiten, to lead: LEITMOTIF. 2. Suffixed variant o-grade form *loit-4 in Germanic *laid6é in Old English /éd, course, way: LOAD, LODE; LIVELIHOOD. [Pok. leit(h)- 672.]
679:lek-. To leap, fly. Possibly suffixed o-grade form */ok-ost- in Latin locusta, locusta, a marine shellfish, lobster: LOBSTER, Locust. [Pok. 2. lek- 673.]
862:flad6, flat cake, pancake: FLAN. 4. Germanic nasalized suffixed form *flu-n-th-r-j6- in Old Swedish flundra, flatfish, flounder, probably akin to the Scandinavian source of Middle English flounder, flounder: FLOUNDER?. 5. Nasalized form *pla-n-t- in Latin planta, sole of the foot, and denominative plantdre, to drive in with the sole of the foot, plant, whence planta, a plant: CLAN, PLAN, PLANT, PLANTAIN!, PLANTAR; PLANTIGRADE, SUPPLANT. 6. Suffixed form “plat-u- in Greek platus (feminine plateia), flat, broad: PIAZZA, PLACE, PLAICE, PLANE‘, (PLANE TREE), PLATE, (PLATEAU), (PLATITUDE), (PLATY?), PLATY-, (PLAZA). [Pok. plat- 833.] [plegan. To pledge for, stake, risk, exercise oneself. West Germanic verb. 1. Old English plegian, to exercise one- self, play: PLAY. 2. Late Latin plevium (> Old French plevir, to pledge), pledge, guarantee: PLEDGE; REPLEVIN. 3. Germanic derivative noun *plehti- in Old English pliht, danger, peril: PLIGHT?.] plek-. To plait. Extension of pel-*. 1. Suffixed o-grade form *plok-so- in Germanic *flahsam, flax, in Old Eng- lish fleax, flax: FLAX. 2. Full-grade form *plek- in Latin -plex, -fold (in compounds such as duplex, twofold; and supplex, “with legs folded under one,” kneeling, entreat- ing; see dwo-, upo): MULTIPLEX, QUINTUPLE, SUPPLE. 3. Latin plicdre, to fold (also in compounds used as denominatives of words in -plex, genitive -plicis): PLAIT, PLIANT, PLICA, PLICATE, PLIGHT!, PLISSE, PLY!; APPLY, COMPLICATE, COMPLICE, DEPLOY, DISPLAY, EMPLOY, EXPLICATE, IMPLICATE, REPLICATE, SUPPLICATE. 4. Suf- fixed forms “plek-to- and *plek-t-to- in Latin plectere (past participle plexus), to weave, plait, entwine: PLEACH, PLEXUS; AMPLEXICAUL, COMPLECT, (COMPLEX), PERPLEX. 5. Greek plekein, to plait, twine, and plektos, twisted: PLECOPTERAN, PLECTOGNATH. [Pok. plek- 834.] plék-. Also pleik-. To tear. 1. Zero-grade form *pbk- becoming *plak- in Germanic *flahan in Old English fléan, to strip the skin from: FLAY. 2. Suffixed o-grade form “ploik-sk- perhaps in Germanic “flaiskjan, piece of flesh torn off, in Old English flésc, flesh: FLESH. 3. Zero-grade form *plik- in Germanic *flikkja in: a. Old English flicce, side of a hog: FLITCH; b. Germanic ablaut form *flekkja in Old Norse flekkr, piece of skin or flesh, spot, stain: FLECK. [Pok. plék- 835.] pleu-. To flow. I. Basic form “pleu-. 1. Latin pluere, to rain: (PLOVER), (PLUVIAL), PLUVIOUS. 2. Greek pleusis, sailing: PLEUSTON. 3. Suffixed zero-grade form *plu-elos dissimilated into Greek puelos, trough, basin: PYELITIS. 4. Suffixed form *pl/(e)u-mon-, ‘‘floater,” lung(s), in: a. Latin pulmé (< *plumonés), lung(s): PULMONARY; b. Greek pleumén, pneumon, lung: PNEUMONIA, PNEU- MONIC. 5. Suffixed o-grade form *plou-to- in Greek plou- tos, wealth, riches (< ‘‘overflowing’’): PLUTO; PLUTOCRACY. 6. Lengthened o-grade form *pl6(u)- in: a. Germanic *fléwan, to flow, in (i) Old English flowan, to flow: FLOW (ii) perhaps Middle Dutch vluwe, fishnet: FLUE?; b. suffixed form *pld-tu- in Germanic *fléduz, flowing water, deluge, in Old English fléd, flood: FLOOD. II. Extended form *pleuk-. 1. Germanic *fleugan, to fly, in Old English fléogan, to fly: FLY!. 2. Germanic *fleu- gon-, flying insect, fly, in Old English fléoge, a fly: FLY?. 3. Probably Germanic *fleuhan, to run away, in Old English fléon, to flee: FLEE. 4. Germanic causative *flauhjan in Old English flygan, flégan, to put to flight: FLEY. 5. Germanic suffixed form *fleug-ika in Old French fleche, arrow: FLECHE, FLETCHER. 6. Zero-grade form *pluk- in: a. Germanic *flugja-, feather, in Old English -flycge, with feathers (only in unfligge, featherless): FLEDGE; b. suffixed form *flug-ti- in Old English flyht, act of flying, and *flyht, act of fleeing, escape: FLIGHT, FLIGHT?; Cc. possibly (but unlikely) suffixed form *flug- laz, dissimilated into *fuglaz, bird, in Old English fugol, bird: FowL; d. Germanic suffixed form *flug-ila in Mid- dle High German viiigel (> Germanic Fliigel), wing: FLUGELHORN, FUGLEMAN. III. Extended form *pleud-.
1228:ALERT al-1 ALEURONE al-4 ALEXIA feg-1 ALEXIPHARMIC alek- ALGOLAGNIA  slég- ALIAS al-1 “ ALIBI al-1, kWo- ALIBLE al-3 ALIEN al-1 ALIFORM_ aks- ALIKE fik- ALIMENT al-3 ALIMONY al-3 ALIPHATIC leip- ALIQUOT al-1, kwo- ALL al-5
1739:LEAGUER! legh- LEAK leg-2 LEAN! klei- LEAP klou- LEARN leis-1 LEASING leu-! LEAST leis-2 LEATHER letro- LEAVE! leip- LEAVE? §leubh- LEAVEN legWh- LECHER leigh- LECTERN leg-1 LECTION leg-1 LECTURE leg-' LEDGE legh- LEDGER legh- LEE kele-1 LEECH! feg-1 LEECH? leig-1 LEEK leug-! LEER kleu-! LEES legh- LEGACY leg-1 LEGAL leg-1 LEGATE leg-1 LEGATO leig-1 LEGEND leg-1 LEGERDEMAIN leg¥h- LEGIBLE leg-1 LEGION leg-1 LEGISLATOR leg-1, tele- LEGIST leg-1 LEGITIMATE leg-1 LEITMOTIF leit-2 LEMAN leubh- LEMMA! (s)lag¥- LEMMA? lep-t LEMURES_ lem-2 LEND leikw- LENGTH del-1 LENIENT [6-2 LENIS [6-2 LENITIVE |@-2 LENITY 16-2 LENT del-1 LENTO lento-, lep-1. LEPIDO- lep-1 LEPIDOTE lep-1 LEPRECHAUN kWrep-, legwh- -LEPSY (s)lag¥- LEPTO- lep-1 LEPTON! lep-1
1747:LIEN leig-1 LIENAL_ spelgh- LIEUTENANT ten- LIFE leip-
1752:LIPO- leip- LIQUATE wileik- LIQUEFY wleik- LIQUESCENT wleik- LIQUID wleik- LIQUOR wileik- LIRA lithra
1757:LITHE lento- LITHOTRITY dhreu- LITIGATE ag- LITMUS meu-, wel-1 LITOTES lei- LITTER legh- LITTLE leud- LITTORAL [éi- LITURGY werg- LIVE! leip- LIVELIHOOD leit-2 LIVELONG leubh- LIVELY leip- LIVER! leip- LIVERWURST wers-! LIVERY leudh-? LIVID — sfi-
1759:LOAD leit-2 LOAM lei- LOAN leikw-
1760:LOATH leit-1 LOATHE leit-1 LOBBY leup- LOBE leb-1 LOBO wikwo- LOBSTER lek- LocH laku- LOCHIA legh- LOCK! leug-1 Lock? leug-1 LOCKET leug-1 Locust lek- LOCUTION  tolkw- LODE leit-2 LODGE leup- LOEss leu-1 LOFT leup- LOGARITHM ar-, leg-1 LOGE leup- Locic leg-1 LOGISTIC leg-1 Loco- leg-1 Locos leg-1
2331:SWING sweng(w)- SWINGE sweng(w)- SWINGLETREE sweng(w)- SWIRL swer-2 SWITCH swei-2 SWIVEL swei-2 swoop swei-2 SWORD swer-4 SYCAMORE moro- SYCOPHANT bha-! SYLLABLE (s)lag’- SYLLEPSIS (s)lag¥- SYLLOGISM leg-1 SYMBIOSIS gWei- SYMBOL gvele-1 SYMPATHY kWent(h)- SYMPATRIC peter- SYMPHONY bha-2 SYMPHYSIS bheue- SYMPODIUM ped-! SYMPOSIUM pd@(i)- SYMPTOM pet- SYN- ksun SYNAGOGUE ag- SYNALEPHA leip-
=== AHD context
679:lek-. To leap, fly. Possibly suffixed o-grade form */ok-ost- in Latin locusta, locusta, a marine shellfish, lobster: LOBSTER, Locust. [Pok. 2. lek- 673.]
```


## [2026-09-06T23:09:29.547Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHM lagad\"; grep -n -i 'lagad\\|rakata\\|lakata\\|lak-\\|kick' AHM.txt | head -40"
}
```


### [2026-09-06T23:09:29.594Z] TOOL RESULT

```
=== AHM lagad
1638:+ The opportunity may be taken to draw attention te the provable etymo- logical connection af NPers. lagad ‘kick’ with Gr. daft, Adyiyy ‘kicking with the heel’. Jagad should resresent Olr. *i/rakata-. For the suffix cf. Av. nemata- ‘felt’ (see Liiders, APAW, 1935, No. 3, 15 s9g.), and Sogd. spAth, Olnd. sikata ‘sand’, beside *sikitd- (in Yd. séyio and Oss. sidZit) and *sika- (in OPers. #ka- and Bal, six), see Morg., IIFL, 1, 245, NTS, v, 51. If the somewhat artificial connection of Adf with Skt. lakuta ‘club’ (supggasedly < *lakrta) and Tat. lacertus (cf. Walde -Ilofmann, LEW, s.v.) should happen to be correct, one may assume an 7/n alternation *leky-to~ (> Ind. *lakyta-):*leky-to- (> Tyan.
1970:qt. frastacd hamars9a8a, Wi. ‘der hervorstirzt vom Gegner gefalgt’; Gdn. (followed by Bth, and Lo.) ‘den feind im laufe iiberholend’; Da, ‘poursuivant.. .l’ennemi’; Spi. ‘welcher vorwarts stiirzt nachdem er an den Feind sich gehangt hat’; Htl. ‘der, dem Gegner entgegenlaufend, sich an ihn macht’. Far the meaning assumed by Gdn. there is a parallel in Arezd.’amana’s epithet afrakatacim (Yt 19.42), far which Bth.’s translation ‘not running forward (from the caver he had taken)’ is unconvincing; one expects a positive, not a negative quality.} Gdn.’s
1971:t¢ The epithets which precede afrakatacim in Yi 19.42 include frazustam [... Justem (the latter probably a compound of °zustam with a preverb other than
1976:interpretation, Drei Yasht, 26, n. 4, is therefore to be preferred: he took afrakatak- for a bahuvrihi containing *fraka-tak- ‘Zuvorkammer’, hence meaning ‘who has no Zuverkommer, cannot be caught up with’. 7°. stija, Wi. ‘verwundend’ (comparing Gr. arilw, ortyua); W. Geiger, OK, 447, n. 1, ‘spitze Waffe’ (comparing Ved. tigmd, etc.), a view which was revived by Duch., BSOS, 1x, 865; Justi, Spi, Gdn, Da., Bth., Lo., Hth, ‘im, mit, Kampf’, comparing NPers, sit2z. Justi’s interpretation deserves preference over Geiger’s, inasmuch as a ‘pointed weapon’ is unwanted: the bestial treatment meted out to the victim clearly shows that the attacker is the boar, nat Varaérayna, let alone Mithra, as might appear from some translations; the baar’s fangs and
1977:opposite meaning, and seek a connection with Oss. (Digor) zust ‘hart, finster, grob’ (Miller-Freiman’s Dictionary, 1, 627), provided, of course, the lattar is not from *e-zusta- (cf. Morg.’s explanation of NPers. 2af ‘vehement, vialent, wicked’ as from *a-szausa-, EVP, 106); cf. Middle krish guss < *ghustu-s, ‘force, violence, anger’, Pokorny, Indagermanisches Wirterbuch, 448? On the other hand, for the epithet avd. zusam (Sth. ‘wearing a jewel’ (?)), which immediately follows afrakatacim, a connectian with P&. zwaz 'naise, clamaur’ may he sug- gested, which Morz., lac. ciz., derives from *zausa-; ‘raising a noise’, with bar-, is reminiscent af the cammon Av, expression vacim bar-, see Bth., W3., 935 sa.
3080:*abi-dasta(ua)-, 220 n. *dvya-, 200 0. *apavant-, 201 *cam-, 184 *dug-gva-, 230 *havya-, 200 n. *7i(va)Ora-, 260 *lakata-, 182 n. *ndxar|n-, °aka-, 277 *niba-, 282 *pati-dastana-, 220 n. *pati-mauga-, 203 *pitt-, 231
3090:afrakatak-, 219 sq. anhaéna-, 281 anaipi paramna-, 247 aintka-, 278 ainiZbarat®, 200 n. anu .mainyai, 283 sq. anu. sastrai, 283 sq. anya-, 286
```


## [2026-09-06T23:09:44.757Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### AHM leaf for line 1638\"\nawk 'NR<=1638{n+=gsub(/\\f/,\"\")} END{print \"formfeeds before:\",n}' AHM.txt\necho \"### HRN farib\"\ngrep -n -i 'firēftan\\|fireftan\\|firîftan\\|farib\\|firib\\|rew.*Betrug\\|frēftan' HRN.txt | head -20"
}
```


## [2026-09-06T23:09:45.680Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### HRN leaf 163-164 (p142-143)\"; awk 'BEGIN{RS=\"\\f\"} NR==164' HRN.txt | head -60"
}
```


### [2026-09-06T23:09:57.698Z] TOOL RESULT

```
### AHM leaf for line 1638
formfeeds before: 199
### HRN farib
5690:643. rew 'Betrug, List* (Sahn. II, 735 Vers 939), rewäs,
```


### [2026-09-06T23:09:59.611Z] TOOL RESULT

```
### HRN leaf 163-164 (p142-143)
— 142 —
639. rlden *kacken', Praes. rii/^em, rtsten, rtm *), rime.
aw. l/^raf-, avi dim irita *kackt darauf (vd. 5, 1);
phlv. }*ttan, reman, remamh; ai. l/^re-, riyäti *frei
lassen, laufen lassen .
kurd. rltin *kacken'; oss. d. liyun, t. Hin (168); bei.
rii/ay (315).
610. vis (*m) *Bart', rese *Haai'\
aw. ra^sa- zweifelhaft (Hörn, ZDMG. 43, 33,
Jackson, Amer. Journ. of Philology, Vol. XI, 88);
phlv. res *Bart' (AV.), resak *Haar (vd. 7 (28) Gl).
kurd. ruh, ri *Bart'; afy. ^Ira (aus *riSa) bezw.
^ire; oss. d. re/e, t. rt/T (213); wa/. reyis, i^itr. ri/is,
rikis, minj. yarzd,
Vergl. Bartholomae, Studien II, 54, 55.
641. veH') 'Wunde, Geschwür, rese, resTde,
aw. ra^sah' 'Wunde', [/^rars-, ra^ayat 'verwunden ;
phlv. res, resiian ; ai. l^reS-, resat^ reHyati *versehrt
werden ; beschädigen'.
LW. kurd. m; bei. res 'Wunde' (225).
642. reg \Sand' (AM. 242 Zeile 9), rez (Käs. Z. ryz).
LW. (?) kurd. rik^ rig; afy. reg; bei. rek^ n.
re/ (317).
Bartholomae (ZDMG. 46, 301 No. XIX) stellt die
iranischen Worte zu ai. sikata- 'Sand', während sie
Geiger an aw. l/^rafx- (No. 638) anschliessen wollte.
643. rew 'Betrug, List* (Sahn. II, 735 Vers 939), rewäs,
reimen, rlmen 'betrügerisch'^).
ai. rip' 'Betrug* (l/"rep-, lep- 'anschmieren').
Vergl. fireften (No. 829).
») *liem', LW. kurd. afy. rim *Eiter*, bei rgm 'Eiter* (224), wa/.
rim *Schmutz\
2) Der Mftihülvokul ist bezeichnet AM. 231 Zeile 3.
*) *Repmetiy vergl. * Verlorenes Sprachgut* No. 83. Die Volks-
otyraologie macht das Wort zu einer Verkürzung von Ahrlmen. Da die
Bedeutung 'sclimutzig, unrein* dem Worte nach der Überlieferung nicht
zukommt, so wird man os nicht zu phlv. reman^ np. rim (oben No. 039)
zi(5licn dürfen.
```


## [2026-09-06T23:10:05.255Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==206' HRN.txt | head -50; echo \"=== grep 829\"; grep -n '829\\.' HRN.txt | head"
}
```


## [2026-09-06T23:10:05.762Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN 103 rist\"; awk 'BEGIN{RS=\"\\f\"} NR==125' HRN.txt | head -50"
}
```


### [2026-09-06T23:10:07.207Z] TOOL RESULT

```
— \Si -
826. ftHh viel, mehr.
aw. vergl. fräyäo, fraesta-; phlv. fr ah, f rahist
(Päz. freh^ frehest), ursprünglich freh^ vergl. freh[dätär
(AV.).
Die Aussprache ßrih (nicht fireh) bezeugen die
Keime der beiden bei Vullers s. v. mitgeteilten
Verse {bih und girih). Ich stelle das Wort zu den
von Andreas erklärten bih, kih, mih (No. 241).
827. ferl *lieb, schön .
aw. frya- geliebt, Freund*; ai. pnyä-,
828. feryäd *Hilfe; Hilferuf, Klage.
aw. fraöäia- ^Gedeihen, Förderung' (yt. 13, 68);
phlv. frayät bezw. fradät 'Hilfe*.
Die mittelpersische Bedeutung *Hilfe* findet sich
auch noch im Neupersischen, z. ß. AM. 43 Zeile 6, 82
Zeile 1 V. u., Öähn. I, 126 Vers Uli (NB. wohl un-
echter Vers).
LW. kurd. af/. feryad-, bei. paryat 'Geschrei* (199).
Anders Fr. Müller, WZKM. 5, 353.
829. fireften 'betrügen*, Praes. fireb-em , ßreb 'Betrug*,
ßreftär, JTJKSnE^ (Jer. 20, 7).
ai. pra + [/"rep- 'anschmieren, betrügen', vergl. rip^
'Betrug, ripü' 'Betrüger ; phlv. freftan^ frepet^ f^^P^
frep(i)sn, freftär.
oss. d. fälewun, t. fäliwin 'betrügen* (271). Sar.
rof-am hat noch die Bedeutung 'beschmieren' bewahrt.
830. fe^, fuy 'Götterbild (Geliebter, Geliebte)', fuyistün
V
'Harem* (Sahn. II, 532 V. 198), fuyäk 'töricht', fuyvare
sprachlos, vergl. Fayfür (Seite 71 Note 1).
ap. baga- 'Gott*; aw. baya-; phlv. bag]baxt (ge-
schrieben baW) ; ai. bhdgha-.
Die echt persische Form hat sich im Np. nur in
Ba/däd erhalten, das / ist eine Arabisirung.
=== grep 829
7215:829. fireften 'betrügen*, Praes. fireb-em , ßreb 'Betrug*,
12278:ßrefie,, 643, 829.
12281:/™/Mr 829.
15914:/rtft,,,, 829.
15917:fi-e/lär 829.
15923:/i-6;i 829.
15926:/.■gpfÜÄ« 829.
17989:^■pra 829.
18010:raSs- 829.
19003:ITJNiinS 829.
```


### [2026-09-06T23:10:09.317Z] TOOL RESULT

```
=== HRN 103 rist
— 103 —
(7) Gl.), rTstjayee, ä/ezJt (Phlv.-Vend. für aw. [^ha/s-;
AV.), päz. d/ezed (Men.).
oss. ra]xlzai *du willst herabsteigen', d. s^ezun 'hinauf-
steigen' (301).
Das awestische Wort ist nicht sicher; die Päzend-
lesung mit z beweist nichts.
463. xäm *roh, ungekocht'.
ai. amd' *roh*; arm. huni 'roh' (H. No. 171; vergl.
Bartholomae, Studien II, 44. Daneben LW. /aw)5
gr. (Ojiwc; air. 6w.
kurd. xäv; oss. LW. /öm (Hübschniann, S. 133);
afy. öm, um; bei. hämag, n. häniay, liänvcuj (155);
wa/. yüng,
464. yritnös^) ^schweigend, still*, /ämösl.
skr. a + \/^marS' geduldig ertragen' ; vergl. fcrämös
(No. 812).
465. ^Jiän, yßne 'Haus , xänef/T.
phlv. /ßnak, /an, /änaklk (n''Nn"*2, Nöldeke,
ZDMG. 46, 142).
Von i^khan- 'graben'. Vergl. np. (arab.) yendeq
neben kenden,
466. yi^miT 'Quelle, Wasserbassin , x^^ (unbelegt und un-
sicher 2)).
aw. x^fw-, Nom. ;^äo 'Quelle'; phlv. ;fäw, /ßnlk (Bund.) ;
ai. khiin- [khä-),
kurd. känT, kahm,
467. xäwer {/"äwer) 'Herr.
aw. /'äpara- 'gnädig, barmherzig*; phlv. y^äpar
(Darmesteter, Et. ir. I, 60 Note).
468. ^äye 'Ei*.
phlv. xäyak *Ei' (Men.); arm. Jw *Ei' (unsicher; H.
No. 179); lat. öoiim; gr. rJov; ksl. aje^ jaje *Ei*.
kurd. haik, hl, liek; afy. hä; oss. t. aik, d. aißä
(12); bei. haik (159).
») Reimt auf hös Sahn. I, 429 V. 730.
*J Auch an SteUen wie AM. 240 Zeile 4 v. u. wird man nicht
etwa ;^ä»e *eine Quelle*, sondern ^^änl *die Quelle* (allg.) lesen müssen.
```


## [2026-09-06T23:10:22.135Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== p102\"; awk 'BEGIN{RS=\"\\f\"} NR==124' HRN.txt | tail -25\necho \"=== p136\"; awk 'BEGIN{RS=\"\\f\"} NR==158' HRN.txt | head -60"
}
```


### [2026-09-06T23:10:24.303Z] TOOL RESULT

```
=== p102
im Neupersischen durchaus unbelegt, und die Über-
setzung von aw. /äo durch 'Schultern (man erwartet
einen Dual) nicht sicher^).
461. y^ar, x^^^ 'Fels; Dorn 2), x^*'^ (Häliz 16, 3), ;fä£?e?r
(aus *;^6Zr^^r ?) 3), x^^P^^^ Igel-
skr. khara- 'hart, rauh; scharf; phlv. /ßr, /drpust
Igel* (Bund.); arm. fear 'Stein*.
462. '^Kitsten 'aufstehen*, Praes.;^e2-e/w (AM. 84 Zeile 2 v. u.),
yeztden [x^ztden).
aw. pairi]./aezayiuha^) erhebe dich'; phlv./ös^ (vd. 16
*) Bartholomae (briefl. MitteiluDg) nimmt nach dem Glieder-
parallelismus (s. Neuausgabe)
erezöis x^o
bäzväo aojö
tnnvö vazdvare
für yäo eine mit aojö und vazdvare ungefähr synonyme Bedeutung an.
*) In der Bedeutung Tenis* in alb. Tcär^ kars (G. Meyer,
Alban. Wörterbuch, 176); auch arm. xw (S. Bu gge, KZ. 32, 9).
») Vergl. Rückert, ZDMG. 10, 166, 167 und dann Vullers zu
V ^^
Sahn. I, 196 Vers 1211 (der Rückert, wie gewöhnlich, nicht nennt).
*) D armestet er, 6t. ir. I, 201 weicht hier von Vullers,
Institutiones, ab und macht die Sache nur schlimmer, indem er mi^
dem Pehlevl-Commcntator auf aw. ^'^Isat *er fing an zu schwitzen* (!)
verfällt.
=== p136
— 136 -
609. reje^ reze *Reihe\
aw. razista- ^geradester ; ai. räjistha- (Nöldeke,
mündliche Mitteilung). Jüd.-pers. T]T\ dagegen dürfte
zu aw. rasman- 'Schlachtreihe', ai. ragmän-^ racmi'^
ragi- gehören.
Geldner hatte KZ. 24, 387 Note 2 aw. razura-
'Geleis' (yt. 5, 50) vergleichen wollen.
np. rede 'Richtung, Linie, Reihe' (Öähn. I, 367
Vers 823) scheint dagegen zu aw. ereta-, areta-y ai.
ftd' 'richtig, vollkommen' zu gehören (ursprünglich
'etwas Rechtes, Gerades).'
610. ru%8 {rexs) 'Glanz, Licht', ru/^Tden [rexsiden).
aw. vergl. rao/snc^ 'glänzend, leuchtend, strahlend' ;
ai. ruksd' 'glänzend'.
oss. d. ro/s^ t. rü/s 'Licht, leuchtend', rü/say (214);
ya;'n. ru/sinie.
Gehört np. ru/ 'Wange' auch zu derselben Wurzel?
611. red 'weise, tapfer' (z. B. Sahn. I, 149 Vers 365; Vis
und Rämin S. 13, V. 5 v. u.).
aw. ratU' 'Herr'; phlv. rat, -rat^),
612. rezm 'Schlacht, Kampf.
aw. vergl. areza- 'Schlacht'; arm. LW. paterazm
'Kampf, auch razm.
An Ableitung von aw. rasman- 'Schlachtreihe' zu
denken {s könnte statt z vor m stehen), verbietet die
Bedeutungsverschiedenheit (s. No. 609).
613. rest]äy(^e^ 'Auferstehung der Todten'^).
aw. irista- 'todt'; phlv. rist^ ristä/ez (paz. ristaxez),
614. rasten 'wachsen, Praes. röy-em, röylden, röyäniden,
rösta (arab. syr. LW. rustOq), pNDDn, Is. 42, 11.
aw. |/>c/orf-, raoöahe 'wachsen'; phlv. rustan (bezw.
rödastan , aber nicht wahrscheinlich), röyend bezw.
rödent (3. Plur.), rostäk [rödastak, Salemann, Eine
*) Vergl. Nöldeke, Tabarl-Obersetzung, 447.
*) Kaum gehört hierher röz-l *ir,9 'Todestag' (Pertsch, Die
persischen Handschriften der herzogl. Bibl. zu Gotha, S. 115, 116),
vergl- de t^agarde, Ges. Abb» 3?,
```


## [2026-09-06T23:10:39.903Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== NYB p170\"; awk 'BEGIN{RS=\"\\f\"} NR==179' NYB_vol2_glossary.txt | head -60"
}
```


## [2026-09-06T23:10:40.619Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n 'pdf page' BQT_v2_pages.txt | head -3; echo \"---\"; grep -n 'رستاخیز\\|ریو' BQT_v2_pages.txt | head -20"
}
```


### [2026-09-06T23:10:41.682Z] TOOL RESULT

```
=== NYB p170
 "pišt, from "piš-, Skr pinasti ‘to grind’, Av. (907) pt. pišant-.
pistàn [pst’n'] female breast: ~-pān breast bodice, v.s. v. patsén. - NP pistän.
Pišišētan [pyššwtn'] n. pr. 5921. 11017, —
Av. (908) Piši.šyaodna-.
pit [>B'; pt'], cas. obl. pitar [PBY-tl; ptl 143], pl. cas. obl. pitarän PBY-tl’n'] fa- ther; the difference between pit and pitar is fading: pit is the subj. of the sentence 22°. 3216, 3716, 633, but the cas. obl. in the majority of cases; the cas. obl. pitar is much restricted in use, and stands for the cas. rect. 2711. 28?!; voc. pit 10018, pitar 27°; — pl. parents 2712, 3818, 4115-26, 513 (all in the function of cas. obl.). — Olr pitar-, nom. pita > Milr pit; pitar is a secondary formation. NP old pid, commonly ptdar. — MPrthPrs pyd, pydr indifferently used. V. also apé-pit.
pitik [ptyk] belonging to the father, is the better reading, instead of patitik, 41? pat — mändak for a lapse affecting the father; thus Antiá and two of Sanjana’s MSS.
pēc [pwc'] excuse, apology: cif andar/pat ~ hast a th. serves as an excuse 1021.2, — NP pozidan ‘to apologize’, poziš.
polavatčn [pwl'ptyn'] (made) of steel 2118. 120?'; steely, of one of the cosmic periods 110%. — From pölävat ‘steel’, MPrs pwl’wd, Henning, BSOAS XII, 1947, 45; Arm. lw. polopat, potovat; Paz. adj. pulddin; NP pülad. l
pūryētkēš [pwlywtkyš] adherent, teacher of the primeval (Zoroastrian) religion 11118; pl. cas. obl. —-än the first Zoro- astrian believers 621, 1115. 1124-16, — Bor- rowed from Av. (877) paoiryö.tkaesa-, ci keš.
poryotkčščh the primeval Zorosatrian creed 6414, 8674,
post [pwst'] skin 54%; pl. pēstihā [pwstyh?] 1079. — OP pavastä ‘clay en- velope of a tablet’, Benveniste, BSL XLVII, 1951, 42-49 (thus also Kent); MPrs pwst (A-H II), Paz. NP post.
pöstiyän [pwsty’n'] leather, pl. ~-iha [-yh’] 1102, — Derived from post: NP pöstiyän ‘a kind of leather’.
Pēšang [pwšng] n. of a town 11487. — Yaqut 1, 758 Bušanj.
Pourušisp [pwlwš'sp'] Zartuxšt's father 38—53, passim, — Av. (903) Pourušaspa-.
puhl [pwhl, inser. pwhly] bridge F:l. 6412, 7212.25.26 7423, 8917. 1147. — Av. (892) porotu-, (897) pasu- (cf arota-, -orota-: aša < rta-); MPrth pwrt (MHC); Paz. puh(a)l; NP pul. — Of s.v. Mahlāt:
1puhr [pwhl; Prth BRY] son HajA: 3. SPrth:6; v. also apäk-puhr, apé-puhr, puhrépuhr. — The NW form of Av. (909 sqq.) pudra-; cf pus.
?puhr [pwhl] punishment, penance 665. 7419, — Av. (892) parafa- ‘penalty’.
puhré-puhr (Prth) [pwhrypwhr] grand- son HajA:4. SPrth:7, corresponding to Prs nap (q. v.). - V. puhr.
purr [pwl; M’LH] full: ~ äp full of water 151; ~ tigr full of arrows 2013; 542-7.11, 581; often united with the follow- ing subst. so as to form a compound, from which an abstr. subst. may be derived: ~ Yarrah full of splendour 48?3: ~ avarrahēh 37°. 10619; ~-marg full of death 11719: ~-margéh 648; (—-xrat full of Wisdom): =-xratēh 90%; —-nerök full of power 50%; — before an adj.: fully, thoroughly, perfectly: ~ névak 1 ävam the perfectly brave man of the (World)- era, ‘‘the perfect hero of the generations", of the Prophet 5533, whence the abstr. subst. ~-névakéh 1109; — = hac... kartan to fill with 1218. 12815-16, — Av. (894) parana-; MPrthPrs pwr; Paz. NP pur.
www.parsianjoman.org | vlt
Purr-gav
Purr-giv [pwl TWR’] n. pr. 47°. —
‘Having plenty o
```


### [2026-09-06T23:10:41.734Z] TOOL RESULT

```
---
965:‫جای مند = ببامریومزن پای‌بند ‪.‬‬                    ‫جاو یداه ه بر وزن تازنخانه ‪,‬‬
2686:      ‫است که را بیونانی قنطوریون خوانند*‪.٩‬‏‬
2702:  ‫‪ ۰۱ . ۳‬رك‪ :‬قنطوریون‪.‬‬         ‫‪:6‬‬
5026:              ‫‪.‬‬    ‫آنگاه مه بمه بود این هردو‬             ‫و‬                               ‫نان سياه و خوردی بی چریو‬
7535:           ‫‪ - ۴‬رك‪ :‬چور » جوریور » تذرو ‪.‬‬                          ‫« اونوالا ‪۱٩‬‏ > رك ‪ :‬جوریور » چورپور و تذرو ‪.‬‬
10821:                                         ‫‪:‬‬   ‫خریواز‬   ‫‪:‬‬    ‫شب بازه ‪:‬ورك‬      ‫شب پره»‬    ‫‪-‬رکه‪:‬‬        ‫‪1‬‬
11443:                                                   ‫راد ‪٩‬‏ ‪:‬‬      ‫‪۰‬‬      ‫سریوش‬   ‫‪ - ۴‬بر وزن‬     ‫خر گوش‬
11893:      ‫برها ‪:.‬وخزان خاصه روز هدهم بود ازماه‌شپریور ‪ .‬وخزان عامه روز دوم ازمهرعاه وهردوعیدند‬
13394: ‫چانیدن خوانند» وآیورردن همگویند ‪ -‬وبمعنی‬        ‫کشیده و نون زده » بیونانی نوعی از مازریون‬
13690:                                ‫باشد و چریو بخ خروی گوبد ‪:‬‬                                   ‫‪۸‬‬
14503: ‫= باانیمدوله وخای‬        ‫خحوجریون‬                                                           ‫خوانند ‪. ۷‬‬
16085:                                                                                     ‫‏‪ ٩‬قم)؛ داریوش‬
17784: ‫بواو رسیاه کوسربای ابجد (‪ )۳‬وطای حطی(‪)4‬‬              ‫درواب تاست که‌خروریومابستاح باشد‪.‬وسرگشته‬
17980:                                   ‫درووزه (ھ م‪ (.‬۾ دریوز *‬           ‫=‬   ‫‪۸‬‬              ‫حلاحجان» «نوروزنامه ‪۹۳٩‬‏ ‪.‬‬
18913:‫مطرب وسازنده گوسوریو‌دوخواننده‌باند‪ .‬ولادم‬                        ‫وپرداختة فلان ‪ -‬رشان وفرمان وتفش وکار نامه‬
20254: ‫هندوستان_ ونام گریوه‌ای هم‌هست در رکاشهمیر‬                            ‫براه‬    ‫مان‬
21698: ‫بالف کشیده بروزن سه و چار » بمعنی دگاریور‬                   ‫ترکی آن ده نفراهسمت‪ .‬باد وعربان مسکران‬
21976:‫دار فك ‪ = ۱‬بر وزن ریوند ‪ .‬بمعنی‬
23205: ‫قزوین ‪ ۷‬و راوندی منوب بلاجاست ‪ -‬وریوند‬                   ‫راو حه = بر وزن لاوچه » بوعی از‬
23502:      ‫نت نا‪٤‬‏‬    ‫ار یون = اربان‬       ‫‪e‬‬    ‫‪۳‬‏‬         ‫‪.‬‬   ‫رك ‪ :‬ریوسه‬        ‫‪۴‬‬           ‫‪ - ۱‬رك‪ :‬ریوشه‬
```


## [2026-09-06T23:10:47.886Z] TOOL CALL #18: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'));print(json.dumps(d['NYB'],ensure_ascii=False,indent=1));print(json.dumps(d['BQT'],ensure_ascii=False,indent=1)[:2500])\""
}
```


## [2026-09-06T23:10:48.494Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n 'ristāxēz\\|ristax\\|rist-\\|^rist\\|irista' NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-06T23:10:49.803Z] TOOL RESULT

```
{
 "title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)",
 "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg",
 "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt",
 "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.",
 "notes": " local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt (Part II, pp. 1-286); /home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol1.txt (Part I, plain djvu.txt)",
 "local_files": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol1.txt"
 ],
 "cites": "page number of Nyberg, A Manual of Pahlavi, Part II Glossary (1974)"
}
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
  "/home/sfmqrb/git/rishe/data/
```


### [2026-09-06T23:10:49.841Z] TOOL RESULT

```
1599:MPrth frystg, Arm. lw. hreštak; MPrs prystg, frystg; Talm. Syr. lw. prystq’; Paz. fristaa (SGV); NP firištah ‘angel’ and firistah “messenger, ambassador’.
1600:fröstitan [ŠDRWN-tn' 38°] frést- [SDR- WN-; 2nd. p. sg. plystyh: fréstéh 3°]; pt. = pret. pass. 3d p. sg. frestit [ply- styt' 44 with act. construction; SDRWN- yt', -t']: to send 211, 39.11, 44 ete. passim. — In FrP 23 some MSS give fréstdtan, others frestitan as the equivalent of the ideogr. MPrs pryst’dn, pt. pryst’d, fryst’d, prystyd, pres. pryst-; NP firistädan firist-. A secondary formation from Av. fračšta- v. fréstak. l
1717:gristan [glystn; BKYWN-stn'] . griy- (BKYWN-], pt. pret. 3d p. grist [glyst', BKYWN-st'], to weep, to cry, to lament 111’. 7418-26 (Paz. substitutes here vagined, cf vàng); be ~ to burst out crying 1138. 3417.18, 511.4, �� gristan < *griy-istan formed from the pres. griy- < *grady-; * grad- SW form of garz-, v. girzitan and gil-. Ps. pt. glydyt = gliyit, pres. glydty = griyet; MPrs pres. gryy-; NP giristan giry-. Verbum 204 sq.
2961:paristätan [plst’tn'], paristitan [plstytn'] parist- to worship, to adore, to submit to, to embrace (a religion) 194. 7511, 82.12, — < pari + stā-, v. ēstātan and cf par- ēstātan; Prth *part-štā- in Arm. lw. am- barišt ‘impious’ < Arm neg. an- + *parištā-, pastaun < *parštaun < "pariš- tamna- (middle pt.) ‘cult, service, office’, past-em ‘to worship’; in SW with -st- > -st-: MPrs pres. pryst-, and the inf. assum- ing the SW ending -ītan (cf MPrth pwrs'dn: MPrs pwrsydn, etc.): Paz. pa- rastidan parast- = NP; Verbum 194 sq.
3317:rist
3318:rist [lyst'] the dead, the bodies of the dead 10015-17, 1014-9-23, — Borrowed from Av. (1480 s. v. raēd-) irista-; Paz. rist, Skr. v. sava. V. w-äzxez, -drezišneh.
3321:ristakéh [lstkyh], v. yuvat-~.
3322:ristakénitan [lystkynytn'] to make firm, to fix, to secure, pt. pass. ristakénit 11218. — Den. of ?ristak.
3323:rist-āxēz [lyst?hyc'] the resurrection of the dead 12?5, 6411-13, 7118. 7610. 8326, 8821. 91°. 1057. 12022. — From rist (g. v.) + Gxéz, pres. st. of dxistan (g. v.); Paz. rist-@xeZ (and other spellings); NP rastā- xéz ‘day of resurrection’, ‘tumult’.
3324:rist-āxēzišnēh [~-Snyh] = the preceding w., 1061,
3711:tan [tn'] body, passim, stalk of a plant 9524; ~ u jan body and vital spirit 1523. 6422 (the constituents of human physical nature); ~ u jan u hir u xvāstak 4%; kanišn 4 jan u višopišn i ~ the destruc- tion of the vital spirit and the decom- position of the body (= the physical death) 64191; ~o as opposed to the immortal soul, ruvān 6625. 6820, 6927, 7615-17-18; — — also refers to the human individual as a whole, with all its physical and spiritual qualities, cf 65? sqq. 6611. 8414. 8671; har —-E rad hamgöhr fravahr et 4 x"eš paitak it is revealed that every human individual has its own fravahr (g. v.) of the same substance as itself 88°; xueš.— and ~ 4, avēš v. aueš; — ~ i pasen the ultimate form of existence the Universe will be given after the now running eycle of millenia has elapsed, the next world, Eternity; very often ristaxéz (q. v.) u ~ + pasen: 12%, 6411-13, 7118-19, 7610, 8326, 8821, 919; ~ 4 pasén alone 5212-13, 66°. 677. 934. 104%. — Av. (633 sqq.) tanū-; common Ir.
5199:i0yajah-, iOyejah-: sēž irimant-: rīman irista-: rist
6782:rist: ~ ristaxčž- rist-āxēz rčd: rot
7137:firéftan, firéb: fréftan firistádan, firist: fréstitan firistah: fréstak
7159:giristan, giry-: gristan
7353:rastāxēz: rist-āxēz.
```


## [2026-09-06T23:10:58.136Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR<=3318{n+=gsub(/\\f/,\"\")} END{print \"NYB leaf(0-based) =\",n, \" -> printed p.\", n-8}' NYB_vol2_glossary.txt\necho \"=== PHD\"; grep -n 'ristāxēz\\|rist-āxēz\\|ristaxez\\|^rist ' PHD.txt PHD_mackenzie.txt | head -10"
}
```


## [2026-09-06T23:10:59.041Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT raeth\"; grep -n 'irista\\|iriθyeiti\\|iriOyeiti\\|raēθ\\|1480' BRT.txt | head -25"
}
```


### [2026-09-06T23:11:00.779Z] TOOL RESULT

```
NYB leaf(0-based) = 186  -> printed p. 178
=== PHD
PHD.txt:559:rēšaģ [/yšk! | N rēša] root, fibre. rēšīdan, rēš- [lysyin' | N ~] wound, hurt. rëškën [/yškn'] hurtful, harmful. ~th: harmfulness. réxtan, réz- [lyhtn', lyc- | P ryxt, M ryz-, N ~] flow, pour. --išn: flow. ridan, riy- [/ytn', Id- | N ~] defecate, void. rist [lyst' | M ryst] dead. Iristag [lystk'] corpse. 'ristag [/ystk!] way, manner; sect. rist-āxēz [/yst?hyc | M ryst?hyz, N ~] resurrection of the dead, rištaģ [/(y)stk! | N ~a] rope, string, thread. riy-, v. ridan. riyahrih [/d?hlyh] scorn, mockery. rdb [/wp] robbery. rób- [/wp- | N ruftan, ~} rub, sweep. rūbāh [TALE < A tP; lwph | N ~] fox. Irēd [Iowt! | M rwd, N ~] river. *rdd [lwt' | N ~] stringed instrument. réd-bar [lwtb’] | N ~] river bank. rddig [/zvtyk! | (N róda)] intestine, gut; ~4n, (p/.) entrails, guts. тбүп [M(H)SY A < A ті; lwkn! | Р тшеп, (M rwyyn), N rauyan] oil, butter. ~-xwardig [-hwltyk'] sweetmeats. ron [lwn' | M rwn] direction. б... ~: towards. róspig [lwspyk! | N ~i] whore. ~th: whoredom. róstág [lw(t)st?k! | (P rwdyst?g), N rūstā] river-bed; district, province. rošn [lwfn! | M rwšn, N rūšan] light; bright, light. ~ih: light. röšnjag [lwsnk'] clear, obvious. ~gar [-Al | (P gr, M -ygr), N -gar] illuminator. irēy [ltd | M rwy, N ~] face. *rdy [lwd | M rwy, N ~] copper, brass. гбу-, -išn, v. rustan. гӧуап [/wdyn! | N ~] madder. róyen [/wdyn! | M r'wyn, N róyin] (made of) copper, brazen. roz [YWM < А ушт; Гос | M rwc[z, N ~) day. rózag [lwck! | M rweg, N roza] fast, fasting. rozāģ [wc k'] lightning. rózan [/wcn! | N ~] window. roz(b)ānaģ [lwe(p)’nk'] window. rózénidan, rózén- [Iwcyn-ytn! | M rweyn-] lighten, brighten. rozģār [/wck”l | N ~] daytime. r6zig [/wcyk! | N rózi] daily bread, sustenance.
PHD.txt:3419:resurrection ristāxēz.
PHD_mackenzie.txt:4399:rist [lyst ' I M ryst] dead.
PHD_mackenzie.txt:7423:reliability awestwiirih, ostiganih.      resurrection ristaxez.
PHD_mackenzie.txt:9360:                                          ristaxez
```


### [2026-09-06T23:11:00.824Z] TOOL RESULT

```
=== BRT raeth
2472:dalvil  . .  atibyö  kam  Y.44.20;  46.12;  — li  narS..aeiqm  nmäna  Yt.i~.yC;  g— 14.^, J0.39f.s,  33,Y./j.3,j7.37,Vr.//.i9,V.2, 43-J.i4,Ä4i,  12.1, 13.50,  i5.22,FrV/. 10. 40,  N.<S'5; — g3ui..ya  dar>nlhu  mi^rS.- drujqm  ..frazarsta  (sd.)  aglqm  rai'iya  .. hiit»nte  Yt. /o.  38;  —  vTspanqmca  , .  asae- nqm  aiaoninqmca  .,  vUpanqmca  allqm  za- ra'iuStnm  ..  *susruma ikatsim  Yt.Jj.148; —  a^qm  anyS  N.  61,  62;  —  aifam  aOiai»- kam  .  .  adqmcH  S  ahmt  .  .  vicC^ei  (sd.) aipT\.32.i;  30.1,  8,55.9;  —  haxays .. astvat.gr3take  .  .  assu  paro  fräntmlite aismü  Ytiff.g$;  — gä^a  . .  yezi  argAqm *Syutnpe  väUm  framaraiti  N.  42;  —  xi paiti  apqm  .  .  a^ra  atthqm  V.  y.  5 1 ,  Y. 6Ä7;  Yl/j.68;  —  duzvarmanhS  .  .  rä- mqmcä  J//'"'  dadätu  V.  ^3.  8 ;  —  yaia  ta r  ,  ,  minghäeä  .  .  yH  vohü  .  ,  a'iä  %WJ Si/'"'  yazamaide  Y.  j(?.4;  —  karapsAsaJ (sd.)  kfvitäsca  . .  töi  abyH  (AbL)  bairyänts (sd.)  .,  Y.52. 15; — spuda..kuir3  ayä.. Y.44-I5;  30.6,  3t.io;  —  /J  mainyn  .  . ascä  (GD.)  .  .  Y.30.3;  —  Gen.  in  Ver- bindung mit  hava-i  zasta  hl . .  frasniöa- v paityesii  V.22.7  — 13;  /.z;- — \y"t  aSahe  yat  apirmäyükahe  ahe  hava- aiwySr3hafi?m,.äat  aiijhi  ahi  aiwyästö  Y.  _v(7«  tütroö  "die  Hände  ..  des  Kindes  an ij.zb;  — ahur>m  ..  ahyä  x!a~i:räc3  ..  *hva- 1  dessen  Leib"  V.itf,  7  (?)  "';  —  dgL,  zugleich paphsiica  (sd.)  lim  .  .  yasämaidi  Y.  J7.  vorausweisend:  astvatjr3iö  ..  kB  ..  aiike if.;  —  sraosim  ..yazamaide  ahe  raya  . .  j  haxayB  /räyente  astvat.iritahe  Yt.  ip.  95: aiÄke  ama  ,.  ahe  yasna  ..  t?m  yai3i  "den '  - —  dalnqm  .  .  yao:dai%xSa  ai:a  sT  aiAka Sr.  .  .;  ob  seiner  Pracht  .  ."  Y.  57.3;  Yt.  yaoidaitii  ..  havaya  .  .  dainayä  Y.io. J-i^i  5i  9  (statt  fem.!);  —  noii  kl  anyö\i9.  a)  spez.  auf  das  Subjekt  des  gleichen urva  kaum  urvämm  paiti  irista  (sd.)  ^a-|Satzes,  Reflexivum:  ka%S  .  .  gqm  Ha- zaiti  xraosyü(a{%t^voyaca*a>»he^^.*at3hr^^  sSil  y}  kirn  ahmai  ..  stsi  usyaj  (sd.) Y.  13.9;  —  fravasayS  . .  ankam  raya  . .  Yt  ".  .  qui  eam  sibj  .  .  esse  cupiat"  Y.  ^o.  2 ; 13.2, 14—18"';  — gunäayäi  ..  za/an  ta/-  ^  —  nsit  sp>ntqm  d3r?st  (sd).  akmai  stöi San  (sd)  aya^'*  masJY.3.32;  —  vac?  ..\armaitlm  Y.4^.2;  —  hvJ  tat  n3  ..  ak- yii  . ,  akmai  straohm  dqn  Y.  45. 5 ;  —  |  mai  "'  dazdl  (sd.)  Y.  5/.  1 9 ;  —  aada  (sd.) ustä  ahmst  yahmai  .  .  kakmaicTt  . .  atca  \  vinzyötüca  It  akmai  fracä  vatöyBtü  (sd) <ihmai  Y.  43. 1  f ;  —  gavöi  . .  ha  %X  to\lt  alibyB  yöi  .  .  "..  sibi  (ipse)  . ."  Y.  J5.  6; huisii»m3  .  .  dal  .  .  at  ahyäi  .  .  masda  \- —  at  hT . .  /ravanll  (sd.)  vasirim  ahyai orvara  vaxsat  Y.4S-6;  31-9;  —  raya  ..\fntyant3m  Y.jj.  10;  —  nSit  ta  Im  x^3ui koya  aiiiAä  raiavö  Y.iff.iS;  *YyX.  50; — {vaipyö  .,  zara'iuhrtm  ..  Ayat  akml'^ paoiryö  gairis  . .  akmat  haca  garayO  tu- 1  urüraost  astö  hyat  , .  v3z3  (sd,)  Y.  31. uxiyqHYt.ig.\i.;  34,80;  —  hö  nBit..*/r3-\  12.  aa)  Der  Gen,  vertritt  dann  die  ent- nJmaite  ,.  /rä  ahmst  parö  ..  «jÄion/i;  j  sprechendeFormdeslat  suus:  airj  *i'jiri»i Y. 57-18,  ungeschickt  benutzt  Ytp.4;  lo.  baraiti  mi>akvac3  vä  irvivaca  (sd.)  vä.. 117;- —  *haltuma  . .  kacaiti  dim  . .  astica  akyl  zaridaca  manat»kac3  ", .  ex  suo  (uter- ahmi  avavat;^arin6  yäi:a  yat..Yx.ig.(>Z;\c^^)  corde  et  animo"  Y.ji.ti; —  akya —  :^aitu/  . .  vtrizifum  mat  airyamnä  . .  \xrata  frö  ma  sastB  (sd.)  vakistä  Y.  45. 6  ;
2551:spjmm  taropi^w)m{'&&.)  dastccvai  °tal-  kelterler Ä,.,  ..aber  (die.)  die  ungekelter- sqm  Syachnanqm  ästäraiti  "wenn  einer  ,.,  ten  . ,"  V.  Ij.  43;  — ■  yesi  nöit  sänö  . .  ^ta»- . .  solches  Thun?"  V.  jj,  ao;  —  yaica  vao-  hqtn  astqm  .  ,  barptit?m  frajasqn  "sonst cät  . .  aSaoa  (sd.)  ..  *havanli  (sd)  -tuhe  könnten  Hunde  .,  die  Knochen  verschlep- ryao'knaAe  .  .  V, /j, I3f.;  —  foa  iristaAe  psa"  V-6.46;  T,—yat ..Strim  natuplhm tatiüm  ovaMsta  . .  "tahe  ^aöinahe  , ,  V.  frajasqn  .  .  ava  °tim  nasupiknn  lanaeta 8. 100;  —  ä^ravamm  yaoida'i^ö  (sd.)  . .  . .  apa  'tarn  disiam  (sd.)  baray^n  apa  -t?m Hahmiii  natre  ".  .  einem  solchen  Mann  aa/jnjni  (iariy;'«  "wenn  (sie)  ..  auf  leichen- (der  purifizirtj"  V.p. 37— 39.  4)  auf  kochendes  Feuer  stossen  ..,  den  Leichen-
2552:direkte Rede  oder  Zitat;  a)  adjektivisch:  kochersoll  man  niederschlagen,  den  Kessel usia  ahmni  (usw.,  Y.4J-I)  ■  ■  ciit  °taya  sollen  sie  .  .,  den  Aufbau  ,  ."  V,(V.73f.; paiti.vaca paityümraoti  Y,2/,4;  ■ —  kini  zl  — ■  "//  jrVr.ji./  y^aratu  °i^  vasträ  i-iiv än4  (usw.,  Y.4Ö.6)  .,  'te  zT  väcö  ..  mazdä  katu  V.J.  19;  —  asta-ja  hz  'te  mazäayasna frii mrao tY.yi.i^t-jy. 4.  i^üZ.;- — arrum'a  °t»m  iristam  nidanzaym  "da  sollen  (sie) „afrJnSmi  ..'tarn  mq^nm  fradaisayöH ..  die  J/l  (ihn)  den  Toten  .,"  V.  6'.46;_;.  18, Yti4-46;  benutzt  Y'l4-9.  b)  substan-  5.13,  14,  41,  61,  6.7,  51'.  7-i2i  t''-S,  10, tivisch,  in  Kongruenz  mit  dem  Praedikat:  9.39',  '4-7,  iö-z,  12,  A.3.^  falsVok.?); am?mca  .,  Sfrlnämi  ..  'taSca  tivlcö  yöi  —  'tanhqm  astqmca  var»sqm:a  .,\.h;-; ".  .  und  das  sind  die  Worte,  die  .  ."  Yl  —  'te  ratavö  .  .  'ta£sqm  ra>wam  'S.i'o 14-46'.  1)    vorausweisend    (öfters   -82;  Vd.  2;    —    'ts  ja'iä  V.A16-22S;
2556:fraea  'tat  vacb  vaoce yat  akumat yat  ratu-  zurückweisend,  s.  I  i  a  a);  a)  adjektivisch: mat  Y.jp.8;  Yt.  /p.47;  —  °tat  dät»m  yim  °ipm  aism>m  yÖ  7-aoU  . .  '-tay,i  urvaray,i vtdöyum  "das  GeseU  wider  die  Z»."  V.  yä  vao.'e  Yt  i4-%5',  V.  74.4;  —  *'te  vacö 5.22;  —  'tahe  nars  .  .  yat  paiti.iristahe  . .  yöt  hinti  . .  N.jj;  V.;o.i6,  17;  —  *ta V.J.  15;  JÄ29;  —  'taaha  äpö  yat  ar-  dämqn  ..  *yqm  dj'iat  ahurö  .,  Vr. /2. 4; maistayä  V.  6. 30;  33,  36,  39;  —  'lahmi  —    'tanham    diimanqtn  yöi    Amti  .  .    V,
2799:relativisch  angeschlossenes  Nomen  voraus- weisend; aoxtd  ratui . .  'lö  yö  ratul  V.  5. i6;  —  * af?r3n-iyüka  ..  'sa  *yd  apirin^- /ö^.>  N.  7;  V.  75. 16; — yö  kainitDtn  upaiti ..  ml  . .  'la  yä  kaitu  V.  15.9;  10,  13,  14'; — paiti-iristpot  ..  'sa  yJ  paitt.irista  V,  9. ,1  (?)■>.  2)  auf
2928:•  j.  aojyah-  Adj.  (fem.  'yehl-)  'der  stär- kere': ya  ijravaiayö)  °_>'«4f/(NPf.)  ahmst ..  ya'ia  va/a  /ramravaire{sA.)  Yt/y-64; — aö/  anya^qm  /ravaiayo  jvanqm  narqm . .  'yekll ,  .  ya'i:a  iristanqm  "aber  sonst sind  die  Fr.  der  lebenden  Männer  stärker als  die  der  gestorbenen"  Yt  y.17.  [Y, J4.8:  lies  aoß^
3212:mit  paiti  i)  'etwas  (Akk.)  beantworten, worauf  antworten':  paili  //  (als  Akk.) Shaydit  aSsa  paiti.irista  tumascS..  "darauf soll  der  Verunreinigte  antworten:  tum" ." Y.g.i2.  1)  'Jmdm.  (Dat.,  Gea)  ant- worten auf  — '  (Akk.),  im  kirchlichen Wechselgesang:  äaj  *atravaxsaAe {sd.)  yal ,.  zaokralca  vacim  failiMoaySi  aHä  ratus N.  7J;  72  (wo  paiti.aoayät);  —  aoäj  an- yalsqm  rähivqm  (nämL  väam)  paiti.äla- yöit  "darauf  soll  er  (der  Zaotar)  den  Ä.s auf  der.  andern  Seite  (auf  Ihren  Gesang) antworten"  N.  83.         [S.  noch  paityäüa-^
3771:•  j.  a-banta-"',  a-vanta-'*  Adj.  (fem.  °tä-) "nicht  krank,  gesund':  'Umcit  bandayeifi\ bantimät  (sd.)  drüm  hrmaoili  V.  22.5;! —  pasulca  . .  'ta  (NSf.)  airista  N.  56;  —  ' yat  fräyatayat  . .  aei  nmämm  .  .  drBm  1 't)nt  airistsm  (sd.)  YL5.65.  1
4235:•  j.  an-aeäam  Absol.''  'ohne  danach  zu suchen,  zu  streben,  ohne  etwas  dafür,  dazu zu  tun':  ita  tanam  iristahe  avaMsia  an' manS  an'  vacö  an'  ryad^nfm  "ich  bin  da auf  einen  Leichnam  gestossen,  ohne  dass ich  etwas  dazu  getan  hätte  in  Gedanken, Wort  und  Werk"  V.Äioo.
4368:•  j,  an-^azdya-  Adj.  'nicht  fett,  mager*: nSit  pasusLO  (statt  IS.)  iazda  nsi/  irista (sd.)  {nOit)  °ya  ratufris  abanta  airista *asdya  .  .  N.  ^6;  —  ratufrii  *paysbis  . . ^azdyäisca  *'\\iuca'^^  .  .  pitus  .  .  *atdysii n5it*°yäis'K.  mskSmua  rTzuüa..  *asdyäif näit *'y3is'> N.5 7 ; — ratufris  carTmanqmca pasv.vastranqmca  .  .  *asdyanqm  nSit *'yanqm ''    (nämL   pasunqm)  ^     "r.    wird
4536:•  j.  an-us'kante  Inf.  'nicht  (wieder)  aus- zugraben':^j/  aitika  zsmS  nikante  spsnasifa irista  ,  .  ttaimtm  yär3.dräjS  an'  "wenn man  hier  in  die  Erde  eingräbt  tote  Hunde und  . .,  ein  halbes  Jahr  lang,  (um  sie  nicht sva.)  ohne  sie  wieder  auszugraben"  V.  J.36.
4650:äahtmm  gä'^anqm  sraohrät  pairistaytili  N.^'<>;  —  mmS  ahuräi  mazdai  mmö N.4^;45^*fH.2.i3; — yd  'nyehe  dahmahe  amisaiibys spintaHbyS mmS'nyagsqm  asao- bansma  *frast»r3nfe  ii.104;  lOi;  —  bsöalnqm  V.i^. 25:32;  —  »üi/  xsnSvayeiti  ahu- iia  hislahe  ..  'nyehe  dvan  (sd)  srayatül  r?m  mazdam  tUSit  °nye  (als  AP.)  amisO. V.j.zg;  N.6',7; —  hvSiits  vä  ySiitö  (i'3)  |  ¥1,70.139;'  '39;  —  hapta  hanti  *käva- yim  vä  'inim  *hais^aeTia  (sd.)  .  .  cayqn ,  iiayS  ratavS  .  .  aai  'nyahu  ralu/risü  N. N./;  — ]avada  'niyam  md^ifia/fi  . .  Bh.  102.  a)  mit  ciV'' :  saoiyanlqm  vfn'üra- 5.  4(?);  —  "nyqmca  suttm  ..  N.ff2(,?);  — jamm  Uta  "nyasHt  (als  APn.)  haxayS  Yt. ^rayS 'nya  (als  APm.)  maya  nihwirgsöU  /p.S9'*'.  NSm.  "/yJ,  ASm.'fiim,  ASn.
4653:vorausg.  nagclm  und  la-  'nicht  irgend  ein anderer';  naSclm  tsm  'nySm  yOsmat  vasdä asa  "ich  kenne  nicht  irgend  einen  andern als  euch,  0  Asä"  Y.  j^7">.  II  a)  mit AbL  des  Verglichenen:  ttsit  mSi  vaiiä(sd.) x/mai  *nyS  Y.  2g.  1 ;  ^0. 1 ;  —  h3m  tta mavaitl  payBm  dadat  'nyJm  %wahmat a^rasciJ  ..Y.46.J;  34.7.  ni)  'alienus', a)  im  Gegensatz  zu  'eigen':  nsii  hl  'iiys ttrva  kaom  urvantm  paiti  irista  bqzaiti V.  y,  9'";  — jahikayai  ya  aom  pu>^r»m baraiti  'nyahmai  arsänai  varit»m  pai'^e apa.baraiti(sd.)Ytij.s8.  b), lim  Gegen- satz zu  'heimisch',  sva.  'hostis':  yadiy  ava'ia *maniyähay  hacä  'niyaria  (iS.)  ma  tarsam ".  ,  vor  keinem  Feind  will  ich  mich  zu fürchten  haben"  D.5,3;  D.4.2;  —  karam tyam  ..ajanam  vasiy  'iiiyJ'  apiy3*ahyaiä (sd)  Bh.  j.  19.  IV)  In  ungenauer  Aus- drucksweise; das  mit  a'  Bezeichnete  ist dem  Vorausgehenden,  dem  es  gegenüber- gestellt wird,  nicht  gleichartig'J':  daat {taeta)  -nyatsam  rähwqm  paiti.maydi^i^d^
5112:•  j.  avavat  Adv.  'in  solcher  Grösse,  Masse, Entfernung,  Weise;  ebensosehr,  ebenso': *av'  F.  7  " ;  —  'vatat  Vd.  75.  a)  sonst  1 mit  dem  Korrelat. ^a^u :  ye^Ju  av  . .  tüti  1 SpS  ava.barpnte  yaia  vupa  imi  äpS  .  . Yt  5.  1 S ;  —  ^^  haca  iristaäbyS  yaia ^rigäim  V.Äii;  39,  76,  p.39;  — yd^a iattm  kaydhanqm  av  asava./aalYt  JO.z; — y3  av°  xSva^zvs  vasaiti .. yäka  tiyris.. YtÄö;  —  'vaiai  yaka  kv5  ptruahe'^. 7.53  PüZ.
5258:mit  US  und  paiti  'sich  wieder  erheben, wieder  auferstehen',  von  den  Toten:  us irista  paiti  aranti^^  FrW.  4.3.
6052:•  j.  *azdya-'>  Adj.  'wohlgenährt,  fett': »^  pasusca  (statt  IS.)  ^nsii'a  «aV  irisla (sd.)  (sAV)  anatäya  ratu/ris  aianta  airista *°yii . .  N.  56;  —  ratufris  *paysbis  . .  *yaista an&idyäisia  .  .  *pitui . .  *'yäiil  nSit  *aitaz- ifas..SiUlJkSniscä  vitttsca,.*'yais  nSii  *anaz~ ijäU  N.57;  —  ratu/ris  ^anmanqmca  . . *'yanam  nSit  ^anazäyanam  (sd.)  N.5<?.
6641:j'ff  . .  hö  ba   azh   3s  ys  .  .  V.p.51  f.;  —  yat  Ae  narS  irista  apuirai  ariAat  Vd.  2;
7884:mit  a  'auszugehen  von  -'  (Abi.),  sv^' iristaAe  tanüm  avaMita  V.i*,ioo;  Yt/J. 'sich  abhängig  zu  machen':  hyai  ahyiii\^^^(^.^  — yaica  'la  narS  .  .  fasan  .  .  ycÄ dadä  pa^qm  (sd.)  vfistryHl  vä  aitl  yS  vä  taltö.änaaAö  jasan  kam  'oa  /aMm  A.jm.- nsit  anhai  västryS  ".  .  von  dem  Bauern  i  ^j^^^.j„  V.  4.44;  ij.22,  Y.  6j.6; — n'a^s sich  ablwngig  zu  machen  oder  von  dem,  +=3««  jß/ (sd.)  ydi^a  . .  FrD.j.  a)  mit der  nicht  Bauer  ist"  Y.j/. 9.  I  folgendem    yal    sva.    yai^ra    'wo':     tä
8965:zur  vorläufigen  Unterbringung  vonI.*ichen: I  nmitne  umätte  .  .  %riiyS  "ta  uzdaihyqn \aitahe  yat  irisiahe  V. 5. 10;  —  ci-ants i  aukpn  aäe  'ta  aetalte  yat  irisiahe  "wie gross  sollen  die  Kammern  für  den  Leich- nam sein?"  V.J.  ii'>;  —  also  ..  asii däitys  kata  (statt  NS.)  ..  iristake  V.5.11.
9019:•  }.,  g.  kat  Adv.,  an  der  Spitze  des  Satzes; i)  'wann';  -4'  tä  nara  irista  ..nasus  upa.- dvqsaitii  . .  isar>  pasca  parairistim  V,  -j, \l.  2)  als  Fragepart. 'obwohl?,  num?': if=''  asavä  inazdä  vSng/iat  drjgvanim» "wird  der  .,^/aanhänger,  o  M.,  den  Drug- genossen  überwinden?'  Y.  ^iV.  2 ;  —  h asava  .  .  ranat  dnantjmf  asava  vana[ drvantjm  Yty.  28;  —  kat  möi  un-ä  isi (sd.)  caAyil  avauhS  "ob  (wohl)  .  .*'  Y.  50. i;  —  alä  k'  ^wä  darssäiij  i!S&?i  Y.  J<V,5;
9435:setzend'    in    'vawAf    Jfl»yi.lj     ^ai^jV/    'er  •  j-  iristanqm  "kaäin^m  Vd.  14.
9547:('Leichnam':  nDrfjtm  ..  upa  tarn  'ptm ' fratauharaitl  yqm  iristake  maiyeheV.^.x; ' — pqslö./ra'^a?»h»m  (sd.)  Al  kam?r?}.»m Ivinä^ay^n  ..  as.:^arft3maEiby3  ..*k3r»ß.- ifarqm  '/s  (als  Akk.)*'  paiti  nisirinuyJl \va\)qm  .  ,'^. 3.20;  —  yd  nar!  asaonö 1  iriri>usö  z»m  -pa  (statt  AS.)  nikainti  V. j.  40  PüZ.;  —  ma:dayasrta  aStsm  'pim hvarp-dansim  (sd.)  k?rjiiavqn  V.  5.  13; 14;  —  s.  noch  KompA.  a)  im  Gegen- satz zu  urvan-,  matiah-,  ifvTsl-:  ahurahe mazda  . .  yeähe  urfa  . .  "pas.'a  (NP.)  y3 ral^wayeiti  (sd.)  .  .  Yt  13.  81;  —  yö aSnatthaiti  nö  maiiS ,  .  nB  'p?m  Y.  9.  ag; —  frä  tS  'p»mca  imulmca  yao'zda'^äni V.3i,6;  —  ima  'pasca  tn-lsls:a  Vr.j/,3; Y.  55.  1.  3)    von   Tieren:  yal  barata
10078:1)  'leben,  am  Leben  sein':  Aaca  irista upa  jvantjm  V./O.i';  —  irJrPiidqm  .. jvantam  .  .  azStanam  Y.  24.  5;  —  :^a- saya  .  .  vTspS  atikus  *jvaiti'*  ax^äse  fra- miryeite  V.  .9.  33;  —  ||  ut~i  dargam  jtva (aSKA.)J'  "und  du  sollst  lange  leben" Bh.^.io,  16;  —  darpy)m  jva  ustn  jva (zSIA.)  A. /.  la;  — tä  xsapaiiB  ya.  *}Vähi "(all)  die  Nächte,  die  du  leben  wirst"  Y. 62.  10*'.  a)  mit  '[S>.gaya\  yavata  gaya
10139:—  ^rühräi  pasvä  virayä  ..  "Äj/aMiTy.- ;  Mischung  des //ao/na  und  als  Opferspende: Ayayä  "zum  Schutz  der  Haustiere  und  I  aa£  rai%wiikaraAe  (sd.)  yal  haotmmca Menschen,  , .  des  fünfartigen**'  Getiers"  1  °ava  (IS.)  *rm'ä<wayät  . .  N.  j6;  —  yasj Yt/y.  10;  ig. 6g;  —  vjspam^a  °qm  upä-^U  ..  haoma  ..  'ava  iristahe  baxlaite  V. pqtn!a  upasmqmca  fraptmjätqmca  ravasAio.  ly,  —  haomaySi^d^  'ava  bansmana carätqmca  cat»raf»hälasca  Y.  7J.9;  —  vi-  Ny.  J.  16;  —  ^rt  (sd.)  lääi  "Sus  .  ,  paiti.- spanqm  narqm..vlspanqtn  'Sus  sariöanqm  barö  *ratufrii  ti.108"^;  6o"\  60,  yt;  — ..vJspanqm  urvaranqm  laox>naV.2.zTf.;\*iake  nä  *''ava  ratufriS  N.J^;  —  imq 41;  —  ahitrö  masda  yi  °qm  dadä  yS  narim  Jiaomqsta  myasdqila  zaohrasta  ..  ^qrnca asttvan?m  Y.  12.  j;  —  giusta  (s. III)  aSvS.-  \huhst»h»m'''>  Y.^.  i;  1,  Yi.ii.  3;  —  haur- dä/ayä{sd.}  'Susca  p<mru.sar:^ayä  Yt/.o;   vata  amgr^tata  yazamaide  'äid kuda{AM.
10324:—  yj  °iä(f  asravayö  *qsta  (sd.)  va  ,  . N.  4i\  4^—45^'^\'^y^*  *alte  maiXyanqm (sd.)  pars  x''arftöil  *°IJaJ'  nöif  srävayeiti N.  25;  —  yS  .  .  *aimm  dahm>m  '%anqm *sraoi!rat  pairistayeiti  N.  44.  A)  für die  einzelnen  Tagesabschnitte  {asnya-)  war das  Beten  bestimmter  Grf^^stücke  vorge- schrieben: .(■aiOTJi'  kaca  ulaAinanqm  "^a- nqin . .  * Aavaiiinqm  °'ianqm  . .  *rapi^wina' nqm  ''ianqm  .  .  uzayairinqm  '"hanqm  . . aiwi.srO^rimanqm  'ianqm  ratu/rii  fra- jasaitil  N.46—S1.
```


## [2026-09-06T23:11:32.555Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"total formfeeds NYB_vol2:\"; tr -cd '\\f' < NYB_vol2_glossary.txt | wc -c\necho \"=== KLN life/liver\"; grep -n 'ME. lif, fr. OE. lif\\|OE. lif, life\\|liver.*OE. lifer\\|to live.*OE. libban' KLN_1966.txt | head -10"
}
```


## [2026-09-06T23:11:32.952Z] TOOL CALL #23: Bash

```json
{
 "command": "sed -n '1,60p' tools/ref_page.py"
}
```


### [2026-09-06T23:11:32.996Z] TOOL RESULT

```
#!/usr/bin/env python3
"""Fetch ONE cited page of a scanned reference, on demand.

    python3 tools/ref_page.py BQT:918          # printed page 918 of Borhan-e Qate'
    python3 tools/ref_page.py IRN:119 --image  # also print the path of the page image
    python3 tools/ref_page.py BQT:918 --pdf-page 375   # override the offset mapping

Looks up the reference in data/verification/sources/refs_online.json
(`scans`: list of {file, first_printed, last_printed, pdf_offset, lang}), renders the
matching PDF page to PNG (for reading with a vision model), OCRs it with tesseract in
the reference's language(s), caches both under
data/verification/sources/refs/ocr/<ABBR>/<printed page>.{png,txt}, and prints the
OCR text. Only the cited page is ever processed — never the whole book.

`pdf_offset` means: pdf page index (1-based) = printed page + pdf_offset.

If the OCR is too poor and you transcribe the relevant passage(s) from the PNG yourself,
save that transcription as <printed page>.vision.txt next to the .txt; from then on this
tool prints the transcription instead of the OCR, so no page is ever read twice.
"""
import sys, os, json, subprocess, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "data", "verification", "sources")
TABLE = os.path.join(SRC, "refs_online.json")
REFS = os.path.join(SRC, "refs")
OCR = os.path.join(REFS, "ocr")
TESSDATA = os.path.join(REFS, "tessdata")


def main(argv):
    args = [a for a in argv if not a.startswith("--")]
    if not args:
        print(__doc__); return 2
    m = re.match(r"^([A-Z]+)(\d*):(\d+)$", args[0])
    if not m:
        print("expected ABBR:page (e.g. BQT:918 or MON5:528)"); return 2
    abbr, vol, page = m.group(1), m.group(2), int(m.group(3))
    table = json.load(open(TABLE, encoding="utf-8"))
    ref = table.get(abbr, {})
    scans = ref.get("scans") or []
    if vol:
        scans = [s for s in scans if str(s.get("volume", "")) == vol] or scans
    scan = None
    for s in scans:
        if s.get("requires_volume") and not vol:
            continue
        if s.get("first_printed", 0) <= page <= s.get("last_printed", 10**9):
            scan = s; break
    if "--pdf-page" in argv:
        pdf_page = int(argv[argv.index("--pdf-page") + 1])
        scan = scan or (scans[0] if scans else None)
    elif scan:
        pdf_page = None
        pm = scan.get("page_map")
        if pm and os.path.exists(pm):
            pdf_page = json.load(open(pm)).get("map", {}).get(str(page))
        if pdf_page is None:
            pdf_page = page + int(scan.get("pdf_offset", 0))
            print(f"(no exact page map; using offset {scan.get('pdf_offset', 0)} -> pdf page {pdf_page}; check the printed number and re-run with --pdf-page if off)")
```


### [2026-09-06T23:11:36.186Z] TOOL RESULT

```
total formfeeds NYB_vol2:
294
=== KLN life/liver
```


## [2026-09-06T23:11:55.284Z] TOOL CALL #24: Bash

```json
{
 "command": "pdftoppm -f 308 -l 308 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf \"$PWD/../../tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg308\" 2>&1 | head; ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/ 2>/dev/null"
}
```


## [2026-09-06T23:11:57.878Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN life\"; grep -n -o '.\\{80\\}life.n., ME. lif.\\{200\\}' KLN_1966.txt | head -3\necho \"=== KLN2\"; grep -n -o '.\\{60\\}liver.*OE. lifer.\\{200\\}' KLN_1966.txt | head -3\necho \"=== KLN locust\"; grep -n -o '.\\{60\\}locust.*L. locusta.\\{200\\}' KLN_1966.txt | head -3\necho \"=== KLN lizard\"; grep -n -o '.\\{60\\}lizard.*lacerta.\\{200\\}' KLN_1966.txt | head -3"
}
```


### [2026-09-06T23:11:58.480Z] TOOL RESULT

```
Could not write image to /home/sfmqrb/git/rishe/../../tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg308.png; exiting
total 130208
drwx------ 8 sfmqrb sfmqrb    12288 Sep  6 19:11 .
drwx------ 4 sfmqrb sfmqrb     4096 Sep  6 16:32 ..
-rw-rw-r-- 1 sfmqrb sfmqrb   774972 Sep  6 18:54 afm143.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1046357 Sep  6 18:54 afm144.png
-rw-rw-r-- 1 sfmqrb sfmqrb   533122 Sep  6 17:21 afm41_a.png
-rw-rw-r-- 1 sfmqrb sfmqrb   508509 Sep  6 17:21 afm41_b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   969829 Sep  6 17:21 afm41.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1322100 Sep  6 17:20 afm46.png
-rw-rw-r-- 1 sfmqrb sfmqrb   416305 Sep  6 17:20 afm46_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1078 Sep  6 19:10 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  5157031 Sep  6 18:05 aiw.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    26688 Sep  6 18:20 ary377_bot_p294.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71464 Sep  6 18:20 ary377_p294.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71267 Sep  6 18:19 ary378_p294.png
-rw-rw-r-- 1 sfmqrb sfmqrb    25966 Sep  6 18:19 ary378_top_p294.png
-rw-rw-r-- 1 sfmqrb sfmqrb    76489 Sep  6 17:24 bqt1237_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   127656 Sep  6 18:17 bqt1267_foot_p294.png
-rw-rw-r-- 1 sfmqrb sfmqrb   362419 Sep  6 17:50 bqt1583_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   456331 Sep  6 16:54 bqt1594_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   105420 Sep  6 18:16 bqt27.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2824 Sep  6 16:59 bqt83_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb   703015 Sep  6 17:50 bqt_fn4.png
-rw-rw-r-- 1 sfmqrb sfmqrb   299015 Sep  6 17:50 bqt_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb   325427 Sep  6 17:50 bqt_n552.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   315487 Sep  6 17:50 bqt_n553.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   330101 Sep  6 17:50 bqt_n554.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   332775 Sep  6 18:33 bqtv2_289_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   560485 Sep  6 17:53 bqtv2_650_s.png
-rw-rw-r-- 1 sfmqrb sfmqrb   541712 Sep  6 17:53 bqtv2_651_s.png
-rw-rw-r-- 1 sfmqrb sfmqrb     9689 Sep  6 18:33 bqtv2_meta.json
-rw-rw-r-- 1 sfmqrb sfmqrb   726576 Sep  6 18:33 bqtv2_n289.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   729454 Sep  6 17:53 bqtv2_n650.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   702551 Sep  6 17:53 bqtv2_n651.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   100817 Sep  6 17:36 bqt_v3_111.png
-rw-rw-r-- 1 sfmqrb sfmqrb   110820 Sep  6 17:36 bqt_v3_112.png
-rw-rw-r-- 1 sfmqrb sfmqrb    91526 Sep  6 16:59 bqt_v3_83.png
-rw-rw-r-- 1 sfmqrb sfmqrb   137595 Sep  6 18:10 buck2.txt
-rw-rw-r-- 1 sfmqrb sfmqrb      146 Sep  6 18:10 buck3.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    64531 Sep  6 16:53 build261.py
-rw-rw-r-- 1 sfmqrb sfmqrb    60498 Sep  6 17:11 build269.py
-rw-rw-r-- 1 sfmqrb sfmqrb    97300 Sep  6 17:16 build270.py
-rw-rw-r-- 1 sfmqrb sfmqrb    52615 Sep  6 17:36 build275.py
-rw-rw-r-- 1 sfmqrb sfmqrb    74145 Sep  6 17:43 build278.py
-rw-rw-r-- 1 sfmqrb sfmqrb    72342 Sep  6 17:58 build283.py
-rw-rw-r-- 1 sfmqrb sfmqrb    28249 Sep  6 18:25 build290a.py
-rw-rw-r-- 1 sfmqrb sfmqrb    63778 Sep  6 18:33 build290b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    68833 Sep  6 18:30 build291.py
-rw-rw-r-- 1 sfmqrb sfmqrb    61310 Sep  6 19:11 build302.py
-rw-rw-r-- 1 sfmqrb sfmqrb     5043 Sep  6 17:05 c1.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3501 Sep  6 17:05 c2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    56424 Sep  6 17:05 c3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78058 Sep  6 17:05 c4.png
-rw-rw-r-- 1 sfmqrb sfmqrb 60831599 Sep  6 18:01 cad_k.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb  2530822 Sep  6 18:01 cad_k.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    37980 Sep  6 17:16 c_av.png
-rw-rw-r-- 1 sfmqrb sfmqrb    29703 Sep  6 17:16 c_cros.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1174 Sep  6 17:16 c_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2612 Sep  6 18:28 c_germ.png
-rw-rw-r-- 1 sfmqrb sfmqrb    13418 Sep  6 18:28 c_greek.png
-rw-rw-r-- 1 sfmqrb sfmqrb     8430 Sep  6 18:28 c_ital.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11245 Sep  6 18:28 c_katrang.png
-rw-rw-r-- 1 sfmqrb sfmqrb     6717 Sep  6 18:28 c_katvar.png
-rw-rw-r-- 1 sfmqrb sfmqrb    28872 Sep  6 18:28 c_katvar_zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb    95615 Sep  6 16:39 coord_pg262.png
-rw-rw-r-- 1 sfmqrb sfmqrb  8373934 Sep  6 18:09 cpd.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb   378445 Sep  6 18:09 cpd.txt
-rw-rw-r-- 1 sfmqrb sfmqrb     4560 Sep  6 16:39 crop_ak2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4014 Sep  6 16:39 crop_ak.png
-rw-rw-r-- 1 sfmqrb sfmqrb    25373 Sep  6 16:42 crop_alk.png
-rw-rw-r-- 1 sfmqrb sfmqrb    24852 Sep  6 17:04 crop_fr269.png
-rw-rw-r-- 1 sfmqrb sfmqrb    43238 Sep  6 16:55 crop_germ269.png
-rw-rw-r-- 1 sfmqrb sfmqrb    51654 Sep  6 17:04 crop_gk269.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2585 Sep  6 17:05 crop_gk271.png
-rw-rw-r-- 1 sfmqrb sfmqrb    64142 Sep  6 17:02 crop_gr267.png
-rw-rw-r-- 1 sfmqrb sfmqrb     6411 Sep  6 16:39 crop_gr.png
-rw-rw-r-- 1 sfmqrb sfmqrb    23559 Sep  6 16:42 crop_kohul.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59386 Sep  6 16:39 crop_lat2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    51357 Sep  6 16:55 crop_latin269.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4761 Sep  6 16:39 crop_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4311 Sep  6 19:00 crop_loll2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3325 Sep  6 19:00 crop_loll3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3612 Sep  6 19:00 crop_loll.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3974 Sep  6 16:37 crop_me2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3300 Sep  6 16:37 crop_me.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10236 Sep  6 16:39 crop_op2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4935 Sep  6 16:37 crop_op.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5599 Sep  6 16:37 crop_pers.png
-rw-rw-r-- 1 sfmqrb sfmqrb    18514 Sep  6 18:52 crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb    22007 Sep  6 17:10 crop_sak.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5110 Sep  6 17:10 crop_sax.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4854 Sep  6 17:10 crop_shekar.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1249 Sep  6 17:05 crop_sirish.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30419 Sep  6 17:02 crop_skt267.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5359 Sep  6 19:00 crop_skt2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4064 Sep  6 19:00 crop_skt.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10043 Sep  6 16:58 crop_slav.png
-rw-rw-r-- 1 sfmqrb sfmqrb    24463 Sep  6 16:58 crop_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb  2144625 Sep  6 17:55 dmmpp.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    14732 Sep  6 18:27 e0.json
-rw-rw-r-- 1 sfmqrb sfmqrb    17126 Sep  6 17:54 e1.json
-rw-rw-r-- 1 sfmqrb sfmqrb    51742 Sep  6 18:33 e2.json
-rw-rw-r-- 1 sfmqrb sfmqrb  5301166 Sep  6 17:01 ediv.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb  1773345 Sep  6 17:01 ediv.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  1845041 Sep  6 18:04 gharib.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  3698758 Sep  6 17:50 IEC_full_djvu.txt
-rw-rw-r-- 1 sfmqrb sfmqrb      228 Sep  6 16:34 jscheck.js
-rw-rw-r-- 1 sfmqrb sfmqrb     4265 Sep  6 17:53 kapi_script.png
-rw-rw-r-- 1 sfmqrb sfmqrb   944060 Sep  6 18:06 kent_full.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   288525 Sep  6 18:07 kent_n222.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   285652 Sep  6 18:07 kent_n223.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   282304 Sep  6 18:07 kent_n224.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   268920 Sep  6 18:07 kent_n225.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb     1433 Sep  6 16:45 merge262.py
-rw-rw-r-- 1 sfmqrb sfmqrb    63035 Sep  6 16:56 mk265.py
-rw-rw-r-- 1 sfmqrb sfmqrb    73111 Sep  6 17:13 mk267.py
-rw-rw-r-- 1 sfmqrb sfmqrb    71564 Sep  6 17:08 mk268.py
-rw-rw-r-- 1 sfmqrb sfmqrb    41609 Sep  6 17:31 mk274.py
-rw-rw-r-- 1 sfmqrb sfmqrb    51778 Sep  6 17:32 mk276.py
-rw-rw-r-- 1 sfmqrb sfmqrb    46494 Sep  6 17:52 mk279.py
-rw-rw-r-- 1 sfmqrb sfmqrb    16605 Sep  6 17:54 mk280b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    17667 Sep  6 17:56 mk280c.py
-rw-rw-r-- 1 sfmqrb sfmqrb    43177 Sep  6 17:50 mk280.py
-rw-rw-r-- 1 sfmqrb sfmqrb    58322 Sep  6 17:51 mk282.py
-rw-rw-r-- 1 sfmqrb sfmqrb    63940 Sep  6 18:05 mk285.py
-rw-rw-r-- 1 sfmqrb sfmqrb    67974 Sep  6 18:09 mk286.py
-rw-rw-r-- 1 sfmqrb sfmqrb    60646 Sep  6 18:11 mk287.py
-rw-rw-r-- 1 sfmqrb sfmqrb    50446 Sep  6 18:33 mk292b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    14748 Sep  6 18:27 mk292.py
-rw-rw-r-- 1 sfmqrb sfmqrb    41011 Sep  6 18:29 mk294.py
-rw-rw-r-- 1 sfmqrb sfmqrb    45170 Sep  6 18:47 mk297.py
-rw-rw-r-- 1 sfmqrb sfmqrb    67312 Sep  6 18:51 mk298.py
-rw-rw-r-- 1 sfmqrb sfmqrb    44967 Sep  6 18:51 mk299.py
-rw-rw-r-- 1 sfmqrb sfmqrb    50897 Sep  6 18:54 mk300.py
-rw-rw-r-- 1 sfmqrb sfmqrb    49830 Sep  6 19:05 mk301.py
-rw-rw-r-- 1 sfmqrb sfmqrb    60810 Sep  6 19:07 mk303.py
-rw-rw-r-- 1 sfmqrb sfmqrb  8373934 Sep  6 17:00 mk.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb   378445 Sep  6 17:00 mk.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    11601 Sep  6 16:42 p262-g01.json
-rw-rw-r-- 1 sfmqrb sfmqrb    10625 Sep  6 16:43 p262-g02.json
-rw-rw-r-- 1 sfmqrb sfmqrb    19393 Sep  6 16:46 p262-g03.json
-rw-rw-r-- 1 sfmqrb sfmqrb    19959 Sep  6 16:44 p262-g04.json
-rw-rw-r-- 1 sfmqrb sfmqrb    12063 Sep  6 16:43 p262-g05.json
-rw-rw-r-- 1 sfmqrb sfmqrb    12051 Sep  6 16:44 p262-g06.json
-rw-rw-r-- 1 sfmqrb sfmqrb    12737 Sep  6 16:44 p262-g07.json
-rw-rw-r-- 1 sfmqrb sfmqrb    17259 Sep  6 16:46 p262-g08.json
-rw-rw-r-- 1 sfmqrb sfmqrb    17820 Sep  6 16:53 p262-g09.json
-rw-rw-r-- 1 sfmqrb sfmqrb    17855 Sep  6 16:45 p262-g10.json
-rw-rw-r-- 1 sfmqrb sfmqrb    14983 Sep  6 16:44 p262-g11.json
-rw-rw-r-- 1 sfmqrb sfmqrb    25352 Sep  6 16:46 p262-g12.json
-rw-rw-r-- 1 sfmqrb sfmqrb    17745 Sep  6 16:44 p262-g13.json
-rw-rw-r-- 1 sfmqrb sfmqrb   105748 Sep  6 16:39 p263hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5565 Sep  6 17:22 p275_krei_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb    53703 Sep  6 17:22 p275_pahlavi.png
-rw-rw-r-- 1 sfmqrb sfmqrb     7106 Sep  6 17:34 p279_greek.png
-rw-rw-r-- 1 sfmqrb sfmqrb    12970 Sep  6 17:34 p279_word.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3647 Sep  6 17:34 p279_xsaeta.png
-rw-rw-r-- 1 sfmqrb sfmqrb   130651 Sep  6 17:48 p283_arrow.png
drwxrwxr-x 2 sfmqrb sfmqrb     4096 Sep  6 18:02 p284
-rw-rw-r-- 1 sfmqrb sfmqrb    43108 Sep  6 17:51 p284_e0_fa.png
-rw-rw-r-- 1 sfmqrb sfmqrb    89734 Sep  6 17:51 p284_e0.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59639 Sep  6 17:48 p284_e2b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   106502 Sep  6 17:48 p284_e2.png
drwxrwxr-x 2 sfmqrb sfmqrb     4096 Sep  6 18:25 p289
-rw-rw-r-- 1 sfmqrb sfmqrb    54419 Sep  6 18:05 p289_labibi.png
drwxrwxr-x 2 sfmqrb sfmqrb     4096 Sep  6 18:33 p290
-rw-rw-r-- 1 sfmqrb sfmqrb     1476 Sep  6 18:11 p291_esfand.png
-rw-rw-r-- 1 sfmqrb sfmqrb    31043 Sep  6 18:11 p291_root.png
drwxrwxr-x 2 sfmqrb sfmqrb     4096 Sep  6 18:53 p295
drwxrwxr-x 2 sfmqrb sfmqrb     4096 Sep  6 18:49 p296
-rw-rw-r-- 1 sfmqrb sfmqrb     9447 Sep  6 18:41 p297_av2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     8787 Sep  6 18:41 p297_cav.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2803 Sep  6 18:41 p297_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb     8189 Sep  6 18:41 p297_op.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5216 Sep  6 18:55 p303_n18b.png
-rw-rw-r-- 1 sfmqrb sfmqrb     7082 Sep  6 18:55 p303_n18.png
-rw-rw-r-- 1 sfmqrb sfmqrb     7046 Sep  6 18:55 p303_n5.png
drwxrwxr-x 2 sfmqrb sfmqrb     4096 Sep  6 19:11 p304
-rw-rw-r-- 1 sfmqrb sfmqrb     2952 Sep  6 19:00 p305_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5794 Sep  6 19:00 p305_lat0.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4047 Sep  6 19:00 p305_lat1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66777 Sep  6 16:42 pg261.png
-rw-rw-r-- 1 sfmqrb sfmqrb    84660 Sep  6 16:39 pg262.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71156 Sep  6 16:38 pg263.png
-rw-rw-r-- 1 sfmqrb sfmqrb    92930 Sep  6 16:37 pg264hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    57862 Sep  6 16:35 pg264.png
-rw-rw-r-- 1 sfmqrb sfmqrb    13324 Sep  6 16:57 pg265_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb    86370 Sep  6 16:57 pg265.png
-rw-rw-r-- 1 sfmqrb sfmqrb    79922 Sep  6 16:42 pg266.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70622 Sep  6 16:56 pg267.png
-rw-rw-r-- 1 sfmqrb sfmqrb    69592 Sep  6 16:52 pg268.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71754 Sep  6 16:55 pg269.png
-rw-rw-r-- 1 sfmqrb sfmqrb   122626 Sep  6 16:58 pg270hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    87489 Sep  6 16:55 pg270.png
-rw-rw-r-- 1 sfmqrb sfmqrb   115300 Sep  6 17:05 pg271hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66696 Sep  6 17:04 pg271.png
-rw-rw-r-- 1 sfmqrb sfmqrb    68566 Sep  6 16:58 pg272.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66829 Sep  6 17:28 pg273_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb   157304 Sep  6 17:10 pg273hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70615 Sep  6 17:27 pg273.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65586 Sep  6 17:18 pg274.png
-rw-rw-r-- 1 sfmqrb sfmqrb    80338 Sep  6 17:21 pg275.png
-rw-rw-r-- 1 sfmqrb sfmqrb    76740 Sep  6 17:15 pg276.png
-rw-rw-r-- 1 sfmqrb sfmqrb    44171 Sep  6 17:16 pg277.png
-rw-rw-r-- 1 sfmqrb sfmqrb    89267 Sep  6 17:26 pg278.png
-rw-rw-r-- 1 sfmqrb sfmqrb   168655 Sep  6 17:34 pg279hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75777 Sep  6 17:34 pg279.png
-rw-rw-r-- 1 sfmqrb sfmqrb    82065 Sep  6 17:34 pg280.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61535 Sep  6 17:39 pg281.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70575 Sep  6 17:34 pg282.png
-rw-rw-r-- 1 sfmqrb sfmqrb    74784 Sep  6 17:47 pg283.png
-rw-rw-r-- 1 sfmqrb sfmqrb    81024 Sep  6 17:50 pg284hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    81024 Sep  6 17:51 pg284.png
-rw-rw-r-- 1 sfmqrb sfmqrb   144566 Sep  6 17:49 pg284_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    84487 Sep  6 17:53 pg285.png
-rw-rw-r-- 1 sfmqrb sfmqrb   106264 Sep  6 17:53 pg286hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    76099 Sep  6 18:10 pg286.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72442 Sep  6 17:59 pg287.png
-rw-rw-r-- 1 sfmqrb sfmqrb    53847 Sep  6 17:58 pg288.png
-rw-rw-r-- 1 sfmqrb sfmqrb    28862 Sep  6 18:27 pg289_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb    91779 Sep  6 18:26 pg289.png
-rw-rw-r-- 1 sfmqrb sfmqrb   187988 Sep  6 18:19 pg290hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    98901 Sep  6 18:18 pg290.png
-rw-rw-r-- 1 sfmqrb sfmqrb   105586 Sep  6 18:11 pg291hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70592 Sep  6 18:10 pg291.png
-rw-rw-r-- 1 sfmqrb sfmqrb   103438 Sep  6 18:12 pg292.png
-rw-rw-r-- 1 sfmqrb sfmqrb    36312 Sep  6 18:20 pg294_p294.png
-rw-rw-r-- 1 sfmqrb sfmqrb    24759 Sep  6 18:56 pg295_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb   125960 Sep  6 18:28 pg295hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    80086 Sep  6 18:56 pg295.png
-rw-rw-r-- 1 sfmqrb sfmqrb    56184 Sep  6 18:39 pg296.png
-rw-rw-r-- 1 sfmqrb sfmqrb   130247 Sep  6 18:41 pg297hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66500 Sep  6 18:33 pg297.png
-rw-rw-r-- 1 sfmqrb sfmqrb    60960 Sep  6 18:39 pg298.png
-rw-rw-r-- 1 sfmqrb sfmqrb    99543 Sep  6 18:52 pg299hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    52844 Sep  6 18:38 pg300.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61588 Sep  6 18:56 pg301.png
-rw-rw-r-- 1 sfmqrb sfmqrb   182431 Sep  6 19:00 pg302hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    91158 Sep  6 18:59 pg302.png
-rw-rw-r-- 1 sfmqrb sfmqrb   122418 Sep  6 18:55 pg303hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    89589 Sep  6 18:52 pg303.png
-rw-rw-r-- 1 sfmqrb sfmqrb    48728 Sep  6 19:00 pg304.png
-rw-rw-r-- 1 sfmqrb sfmqrb   151120 Sep  6 19:00 pg305hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    58313 Sep  6 18:59 pg305.png
-rw-rw-r-- 1 sfmqrb sfmqrb    50721 Sep  6 18:58 pg306.png
-rw-rw-r-- 1 sfmqrb sfmqrb   132637 Sep  6 18:38 sns_n155.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   129771 Sep  6 18:38 sns_n156.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   130970 Sep  6 18:38 sns_n90.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   531356 Sep  6 18:38 sns_n90_right.png
-rw-rw-r-- 1 sfmqrb sfmqrb   124445 Sep  6 18:38 sns_n92.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   522585 Sep  6 18:38 sns_n92_left.png
-rw-rw-r-- 1 sfmqrb sfmqrb   495290 Sep  6 18:38 sns_n92_right.png
-rw-rw-r-- 1 sfmqrb sfmqrb   390669 Sep  6 18:10 syn_n1548.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   390669 Sep  6 18:10 syn_n1549.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   390669 Sep  6 18:10 syn_n1550.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   300608 Sep  6 19:11 tadA_n63.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   311561 Sep  6 19:11 tadA_n64.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   334767 Sep  6 19:11 tadA_n65.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   351684 Sep  6 18:35 tad_n59.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   342929 Sep  6 18:35 tad_n59_mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb   242025 Sep  6 18:34 tad_n60_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   282364 Sep  6 18:34 tad_n60.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   335678 Sep  6 18:34 tad_n60_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   276093 Sep  6 18:34 tad_n61.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   332662 Sep  6 18:34 tad_n62.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   334767 Sep  6 18:35 tad_n65.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   265879 Sep  6 18:35 tad_n65_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   295896 Sep  6 19:11 tad_n66.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   304367 Sep  6 19:11 tad_n67.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   308480 Sep  6 19:11 tad_n68.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb     3698 Sep  6 18:19 zar_line.png
```


### [2026-09-06T23:12:08.051Z] TOOL RESULT

```
=== KLN life
=== KLN2
ugrep: error: error at position 118
xbf][\x80-\xbf]*) lifer(?:[^\n\x80-\xbf][\x80-\xbf]*){200}
                             exceeds complexity limits___/


=== KLN locust
ugrep: error: error at position 120
f][\x80-\xbf]*){200}
                    \___exceeds complexity limits


=== KLN lizard
ugrep: error: error at position 88
\x80-\xbf][\x80-\xbf]*){200}
                            \___exceeds complexity limits
```


## [2026-09-06T23:12:15.796Z] TOOL CALL #26: Bash

```json
{
 "command": "pdftoppm -f 308 -l 308 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg308 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg308.png"
}
```


### [2026-09-06T23:12:17.834Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 72091 Sep  6 19:12 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg308.png
```


## [2026-09-06T23:12:18.321Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re,io\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nfor pat in [r\"life,\\s*n\\.\", r\"liver,\\s*n\\.\", r\"live,\\s*intr\", r\"locust,\\s*n\\.\", r\"lizard,\\s*n\\.\", r\"lobster,\\s*n\\.\", r\"alligator,\\s*n\\.\", r\"leg,\\s*n\\.\"]:\n    print(\"=====\",pat)\n    for m in re.finditer(pat,t):\n        print(repr(t[m.start()-80:m.start()+520]).replace('\\\\n',' '))\n        print('---')\nEOF"
}
```


### [2026-09-06T23:12:21.534Z] TOOL RESULT

```
===== life,\s*n\.
'd  the  same  letter  (vjj. Cp.  locum  tenons. lieve.  —  The  same  as  lief. life,  n.  —  MF.  lif,  fr.  OE.  lif,  rel.  to  ON.  lif,  ‘life, body’,  Du.  lijf,  ‘body’,  OHG.  lib,  ‘life’,  MHG. Up,  lib,  ‘life,  body’,  G.  Leib,  ‘body’,  prop,  ‘con- lifer lilac 888 tinuance,  perseverance’,  fr.  I.-E.  base  *lip-,  ‘to remain,  persevere,  continue,  live’.  See  leave,  v., and  cp.  live,  liver,  alive. lifer,  n.,  one  sentenced  to  imprisonment  for life,  —  Formed  fr.  life  with  agential  suff. -er. lift,  tr.  and  intr.  v.  —  ME.  liften,  leften,  fr.  ON. lypt'
---
===== liver,\s*n\.
'en,  tr.  and  intr.  v.  —  Formed  fr.  life  with  suff. -en.  Cp.  enliven. liver,  n.,  one  who,  or  that  which,  lives.  —  Formed from  the  verb  live  with  agential  suff.  -er. liver,  n.,  secreting  organ  of  the  body.  —  ME.,  fr. OE.  lifer,  rel.  to  ON.  lift,  Dan.,  Swed.  lever, OFris.  livere,  MDu.  levere,  lever,  Du.  lever, OHG.  lebara,  MHG.  lebere,  leber,  G.  Leber, ‘liver’,  and  cogn.  with  Arm.  leard  (fr.  *lepard), ‘liver’,  and  possibly  also  with  Gk.  Xinapo;  ‘oily, fat,  greasy’.  See  leave,  v.,  and  cp.  life,  live. livery,  n.,  1)  al'
---
't  which,  lives.  —  Formed from  the  verb  live  with  agential  suff.  -er. liver,  n.,  secreting  organ  of  the  body.  —  ME.,  fr. OE.  lifer,  rel.  to  ON.  lift,  Dan.,  Swed.  lever, OFris.  livere,  MDu.  levere,  lever,  Du.  lever, OHG.  lebara,  MHG.  lebere,  leber,  G.  Leber, ‘liver’,  and  cogn.  with  Arm.  leard  (fr.  *lepard), ‘liver’,  and  possibly  also  with  Gk.  Xinapo;  ‘oily, fat,  greasy’.  See  leave,  v.,  and  cp.  life,  live. livery,  n.,  1)  allowance  of  food;  2)  distinctive  uni¬ form  of  servants.  —  ME.  livere,  fr.  OF.  livree (F.  livree), '
---
'rry.  F.  Olivier  was  influenced  in form  by  OF.  olivier,  ‘olive  tree’. Oliver,  n.,  a  small  tilt  hammer.  —  Prob.  from  the PN.  Oliver. olivet,  n.,  olive  yard.  —  L.  olivetum,  ‘olive  yard’, formed  fr.  oliva ,  ‘olive  tree’,  with  -etum,  a  suff. used  to  form  names  of  gardens  and  woods.  Cp. L.  arbor-etum,  ‘a  place  grown  with  trees’, querqu-etum,  ‘oak  forest’,  palm-etum,  ‘palm forest’.  See  olive. olivet,  n.,  imitation  pearl  —  F.  olivette,  dimin. formed  fr.  olive.  See  olive  and  -et,  -ette. Olivia,  also  Olive,  fem.  PN.  —  It.  Olivi'
---
'  slide  (q.v.) Derivatives :  slither,  n. ,  slither-ing,  slither-y,  adjs. sliver,  n.,  splinter.  —  Formed  from  the  obsol. verb  slive,  ‘to  part,  divide’,  fr.  ME.  sliven,  fr.  OE. slifan.  See  sleave. Derivatives:  sliver,  tr.  and  intr.  v.,  sliver-er,  n., sliver-y,  adj. slivovitz,  n.,  a  plum  brandy.  —  Russ.,  ‘plum brandy’,  fr.  Russ.  (=  OSlav.)  sliva,  ‘plum’,  fr. I.-E.  base  *(s)li-,  ‘bluish’.  See  sloe, slob,  n.,  mud.  —  Ir.  slab,  prob.  of  Scand.  origin. Cp.  ON.  slabb,  ‘mud’,  and  see  slab,  ‘mud’, slobber,  intr.  and  tr.  v.  —  ME.  sl'
---
===== live,\s*intr
'E. lim,  ‘member’.  See  limb,  ‘member’,  and  cp.  words there  referred  to. live,  intr.  and  tr.  v.  —  ME.  liven,  livien,  fr.  OE. libban,  lifian,  rel.  to  OS.  libbian,  ON.  lifa,  OFris. libba,  liva,  OHG.  leben.  MHG.,  G.  leben, Goth,  liban,  ‘to  live’,  fr.  I.-E.  base  *leip-,  ‘to remain,  persevere,  continue,  live’,  whence  also Gk.  Xitrapeiv,  ‘to  persist,  persevere’.  See  leave, v.,  and  words  there  referred  to  and  cp.  esp.  life, liver  and  the  second  element  in  celibate. Derivatives:  liv-able,  adj.,  live,  adj.,  liv-ing,  adj. and  n. liv'
---
===== locust,\s*n\.
'ds there  referred  to.  Cp.  also  lieu  and  the  second element  in  milieu. locust,  n.  —  ME.,  fr.  L.  locusta,  ‘grasshopper, locust’,  prob.  fr.  *lokos-ta,  lit.  ‘the  jumper’,  and rel.  to  lacertus  (masc.),  lacerta  (fern.),  ‘lizard’; see  lizard  and  cp.  lobster.  For  the  form  of  L. locusta  cp.  robustus,  ‘strong’,  onustus,  ‘laded, loaden’.  For  the  sense  development  of  locusta cp.  F.  sauterelle,  ‘grasshoper,  locust’,  fr.  sauter, ‘to  leap,  hop’,  G.  Heuschrecke,  ‘grasshopper, locust’,  lit.  ‘hay-jumper’,  fr.  Heu,  ‘hay’,  and schrecken,  in  the '
---
===== lizard,\s*n\.
"id, be  liquid’.  See  liquid  and  cp.  prolix. Derivative:  lixiviat-ion,  n. lizard,  n.  —  ME.  lesard,  fr.  OF.  laisard,  lesard, fem.  laisarde  (F.  lezard,  fem.  lizarde),  formed — with  change  of  suffix — fr.  L.  lacerlus  (masc.), resp.  lacerta  (fem.),  ‘lizard’,  which  stand  for *lacer-tos,  *lacro-los,  resp.  *lacer-ta,  *lacro-ta, and  derive  fr.  I.-E.  base  *leq-,  *leq-,  ‘to  bend, twist’,  whence  prob.  also  L.  locusta,  ‘grass¬ hopper,  locust',  lit.  ‘thejumper’,  ON.  leggr,  ‘leg’. See  leg  and  cp.  Lacerta,  lacertian,  lobster,  locust. Cp.  also  I"
---
===== lobster,\s*n\.
'at,  vegetables, etc.  —  Of  uncertain  origin;  cp.  prec.  word  and scouse. lobster,  n.,  an  edible  marine  shellfish.  —  ME.,  fr. OE.  lopustre,  loppestre,  prob.  corruption  of  L. locusta,  ‘lobster;  locust’.  See  locust. Lobularia,  n.,  a  genus  of  plants,  the  sweet  alyssum (bot.)  —  ModL.,  fr.  Late  L.  lobulus,  ‘lobule’,  fr. F.  lobule.  See  next  word  and  adj.  suff.  -ary. lobule,  n.,  a  small  lobe.  —  F.  lobule,  dimin.  of lobe.  See  lobe  and  -ule. Derivative:  lohul-ar,  adj. lobworm,  n.,  a  lugworm  —  Compounded  of  lob and  worm. local,  adj.'
---
===== alligator,\s*n\.
' and  ligdre, ‘to  bind,  tie,  fasten’.  See  ligament  and  cp. alloy,  ally. alligator,  n.  —  Corruption  of  Sp.  el  lagarto. which  is  shortened  fr.  el  lagarto  de  Indias,  name of  the  cayman,  lit.  ‘the  lizard  of  the  (West) Indies’.  Sp.  el,  ‘the’,  derives  fr.  L.  ille,  ‘that  one’, lagarto  comes  fr.  L.  lacertus,  ‘lizard’.  See  ille and  lizard. alligator  pear,  the  avocado.  —  Formed  fr.  Na- huatl  ahuacatl  through  the  medium  of  the  Mex. Sp.  forms  alvacata,  alligato.  Cp.  avocado, alliterate,  intr.  v.,  to  use  alliteration.  —  ML.  al- Uter'
---
===== leg,\s*n\.
',  ‘leprosy’  (see  leper).  See Walde-Hofmann,  LEW.,  I,  786  s.v.  lepidus. leg,  n.  —  ME.  legge,  leg,  fr.  ON.  leggr,  ‘leg’ (which  is  rel.  to  ON.  armleggr,  ‘arm’),  which  is prob.  rel.  to  OE.  lira  (for  *ligiza),  ‘fleshy  part  of the  body,  flesh’,  ON.  Her,  Swed.  lar,  ‘thigh’,  and prob.  cogn.  with  OI.  rk^ald,  ‘foot  joint  of  a hoofed  animal’,  L.  lacertus,  ‘upper  arm,  arm’, lacerta,  ‘lizard’,  locusta,  ‘grasshopper,  locust’, lit.  ‘the  jumper’,  Gk.  Xa$,  XayS^v,  ‘kicking with  the  foot’,  Xa>m?av,  ‘to  kick  with  the  foot’, Xdz.TLC,  ‘pes'
---
' L.  prola- tus.  See  prolate  and  -ive. Derivative:  prolative-ly ,  adv. proleg,  n.,  one  of  the  abdominal  legs  of  the  larvae of  several  insects.  —  A  hybrid  coined  fr.  L.  pro, ‘before,  for’  (see  1st  pro-),  and  E.  leg. prolegomenary,  adj.,  introductory.  —  See  next word  and  adj.  suff.  -ary. prolegomenon,  n.,  introduction.  — -  Gk.  npo- Xeyopcvov,  neut.  pass.  pres,  part  of  npoXsyeiv,  ‘to say  beforehand’,  fr.  npo  (see  2nd  pro-)  and Xcyetv,  ‘to  say’ ;  see  lecture.  For  the  Greek  pass, suff.  -jjcvoc  see  alumnus  and  cp.  words  there '
---
```


## [2026-09-06T23:12:36.908Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\n# find running heads: two words then 3-digit number\nfor pat in [r\"leave,\\s*v\\.\", r\"live,\\s*intr\", r\"liver,\\s*n\\.,\\s*secreting\", r\"life,\\s*n\\.\"]:\n    m=re.search(pat,t)\n    if not m: print(\"no\",pat); continue\n    seg=t[max(0,m.start()-3000):m.start()+3000]\n    heads=re.findall(r\"[a-zA-Z’'\\-]+\\s+[a-zA-Z’'\\-]+\\s+(\\d{3})\\b|\\b(\\d{3})\\s+[a-zA-Z’'\\-]+\\s+[a-zA-Z’'\\-]+\", seg)\n    print(pat, \"->\", [h[0] or h[1] for h in heads][:10])\nEOF"
}
```


## [2026-09-06T23:12:37.651Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\ni=t.find(\"leave,  v.\")\nprint(repr(t[i-200:i+800]))\nEOF"
}
```


### [2026-09-06T23:12:39.864Z] TOOL RESULT

```
leave,\s*v\. -> []
live,\s*intr -> []
liver,\s*n\.,\s*secreting -> []
life,\s*n\. -> ['888']
```


### [2026-09-06T23:12:42.897Z] TOOL RESULT

```
"o-,  which  is  rel.  to  *qai-lo,  appearing  in Lett,  kails,  OE.  hdi,  ‘whole,  uninjured,  healthy'. See\x0c  whole  and  cp.  words  there  referred  to.  For derivatives  of  I.-E.  *leip-  see  leave,  v.,  and  cp.\n256\n257\nesp.  life,  live.  Derivative;  celibat-ic,  adj. celio-,  combining  form.  —  A  variant  spelling  of coelio-.\ncell,  n.  —  ME.  cede,  fr.  OF.  cede,  fr.  L.  cella, ‘storeroom,  granary,  bee's  cell,  hut,  cot’,  fr. I.-E.  base  *kel-,  ‘to  hide,  conceal’,  whence  also L.  celdre,  ‘to  hide,  conceal’,  oc-culere,  ‘to  cover, conceal’,  OI.  sdla,  ‘hut,  house,  hall,  stable’, sdlah,  ‘hedge,  enclosure,  wall’,  Gk.  xaXTS,  ‘hut, nest’,  xocX')!3r,,  ‘hut,  cabin’,  xaXu-TEtv,  ‘to  cover, hide,  conceal’,  xsXOtpoc,  ‘sheath,  case’,  xoXeoi;, ‘sheath’,  Mir.  cul,  ‘defence,  shelter’,  culaid, ‘cover’,  OIr.  cttile,  ‘cellar,  magazine’,  OE.  head, hall,  ‘hall’,  hel,  hell,  helle ,  ‘hell’,  helan ,  ‘to  cover, hide’,  Goth,  hulj"
```


## [2026-09-06T23:12:48.924Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nmarks=[(m.start(),m.group(1),m.group(2)) for m in re.finditer(r\"\\n(\\d{3})\\n(\\d{3})\\n\",t)]\ndef page_of(pos):\n    prev=[m for m in marks if m[0]<pos]\n    return prev[-1][1:] if prev else None\nfor pat in [r\"leave,\\s*v\\.\\s*—\", r\"live,\\s*intr\", r\"liver,\\s*n\\.,\\s*secreting\", r\"life,\\s*n\\.\\s*—\", r\"leg,\\s*n\\.\\s*—\", r\"lizard,\\s*n\\.\", r\"locust,\\s*n\\.\", r\"lobster,\\s*n\\.\", r\"alligator,\\s*n\\.\"]:\n    for m in re.finditer(pat,t):\n        print(pat, m.start(), \"after page marker\", page_of(m.start()))\nEOF"
}
```


### [2026-09-06T23:12:52.837Z] TOOL RESULT

```
live,\s*intr 5524240 after page marker ('892', '893')
liver,\s*n\.,\s*secreting 5525464 after page marker ('892', '893')
life,\s*n\.\s*— 5454446 after page marker ('880', '881')
leg,\s*n\.\s*— 5382653 after page marker ('872', '873')
lizard,\s*n\. 5527496 after page marker ('892', '893')
locust,\s*n\. 5541040 after page marker ('892', '893')
lobster,\s*n\. 5535176 after page marker ('892', '893')
alligator,\s*n\. 360089 after page marker None
```


## [2026-09-06T23:13:07.888Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nfor name,pos in [(\"leave\",t.find(\"leave,  v.\")),(\"life\",5454446),(\"live\",5524240),(\"liver\",5525464),(\"leg\",5382653)]:\n    seg=t[pos-2500:pos+2500]\n    heads=re.findall(r\"(?m)^\\s*(?:[A-Za-z’'\\-]+\\s+[A-Za-z’'\\-]+\\s+(\\d{3})|(\\d{3})\\s+[A-Za-z’'\\-]+\\s+[A-Za-z’'\\-]+)\\s*$\", seg)\n    inline=re.findall(r\"[a-z’'\\-]{3,}\\s+[a-z’'\\-]{3,}\\s+(\\d{3})\\b|\\b(\\d{3})\\s+[a-z’'\\-]{3,}\\s+[a-z’'\\-]{3,}\", seg)\n    print(name, pos, \"heads:\", [h[0] or h[1] for h in heads][:6], \"inline:\", [h[0] or h[1] for h in inline][:8])\nprint(repr(t[t.find(\"leave,  v.\")-100:t.find(\"leave,  v.\")+500]))\nEOF"
}
```


### [2026-09-06T23:13:11.199Z] TOOL RESULT

```
leave 1603249 heads: [] inline: []
life 5454446 heads: ['888'] inline: ['888']
live 5524240 heads: [] inline: []
liver 5525464 heads: [] inline: []
leg 5382653 heads: [] inline: []
"lthy'. See\x0c  whole  and  cp.  words  there  referred  to.  For derivatives  of  I.-E.  *leip-  see  leave,  v.,  and  cp.\n256\n257\nesp.  life,  live.  Derivative;  celibat-ic,  adj. celio-,  combining  form.  —  A  variant  spelling  of coelio-.\ncell,  n.  —  ME.  cede,  fr.  OF.  cede,  fr.  L.  cella, ‘storeroom,  granary,  bee's  cell,  hut,  cot’,  fr. I.-E.  base  *kel-,  ‘to  hide,  conceal’,  whence  also L.  celdre,  ‘to  hide,  conceal’,  oc-culere,  ‘to  cover, conceal’,  OI.  sdla,  ‘hut,  house,  hall,  stable’, sdlah,  ‘hedge,  enclosure,  wall’,  Gk.  xaXTS,  ‘hut, nest’,  xocX')!"
```


## [2026-09-06T23:13:15.860Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nfor m in re.finditer(r\"leave,\\s+(tr\\.|v\\.|intr)\", t):\n    if m.start()>5300000 and m.start()<5450000:\n        print(m.start(), repr(t[m.start()-100:m.start()+700]))\n        print(\"=====\")\nEOF"
}
```


### [2026-09-06T23:13:17.603Z] TOOL RESULT

```
5370317 " hybrid  coined  fr.  leather and  Gk.  -oetSf]?,  ‘like’,  fr.  clSo;,  ‘form,  shape’. See  -oid.\nleave,  tr.  and  intr.  v.  —  ME.  leven,  fr.  OE.  He  fan, ‘not  to  take  away,  to  leave,  bequeath’,  rel.  to OE.  Idf,  ‘what  remains,  remnant’,  OE.  belifan, OS.  biliban,  OHG.  biliban,  MHG.  beliben,  G. bleiben,  Goth,  bileiban,  ‘to  remain’,  and  prob. also  to  OE.  Ilf,  ‘life’,  libban,  lifian,  ‘to  live’,  orig. ‘to  remain’ ;  cogn.  with  Gk.  Xinoq,  ‘grease,  fat’, Xi-xpo;,  ‘oily,  fat,  greasy’,  XiTrocpr)?,  ‘persist¬ ing,  persevering’,  lit.  ‘sticky’,  Xlrrapeiv,  ‘to  per¬ sist,  persevere’,  lit.  ‘to  stick’,  OI.  limpdti, 'smears’, liptdh,  ‘sticking  together’,  lepah,  ‘unguent’,  L. lippus,  ‘blear-eyed’,  Lith.  limpit,  lipti,  ‘to  stick, ad"
=====
5372441 'and  love  and  cp.  words  there  referred  to.  Cp.  also the  second  element  in  furlough.\n875\nleave,  intr.  v.,  to  put  forth  leaves,  to  leaf.  —  ME.\nleven,  fr.  lef,  ‘leaf’.  See  leaf, leaved,  adj.,  having  leaves.  —  Formed  fr.  prec. word  with  suff.  -ed.\nleaven,  n.  — -  ME.  levain,  levein,  fr.  F.  levain,  fr. VL.  *levamen,  ‘something  that  raises’  (classical L.  levamen,  means  ‘alleviation,  mitigation’),  fr. levare,  ‘to  lift,  raise;  to  lighten,  alleviate,  miti¬ gate’,  fr.  levis,  ‘light’.  See  level  and  cp.  relieve. Derivatives :  leaven,  tr.  v.,  leaven-ing,  n. leban,  lebban,  also  leben,  n.,  coagulated  sour  milk (an  Arab  beverage).  —  VArab.  laban,  leben, ‘sour  milk’,  fr.  Arab,  laban,  ‘milk’,  which  is  rel. to  He'
=====
5382305 '  and  pp.  of  leave.  —  ME.  lafte, lefte,  past  tense  and  pp.  of  Ieven,  ‘to  leave’.  See leave,  v.\nleft,  adj.,  adv.  and  n.  —  ME.  luft,  lift,  left,  orig. ‘weak,  infirm’,  fr.  OE.  lyft,  ‘weak’  (whence  OE. lyftadl,  ‘paralysis’),  rel.  to  MLG.  lucht,  MDu. lucht,  luft,  ‘left’,  prob.  not  connected  with  Gk. Xs7ip6;,  ‘scaly’,  Xlirpa,  ‘leprosy’  (see  leper).  See Walde-Hofmann,  LEW.,  I,  786  s.v.  lepidus. leg,  n.  —  ME.  legge,  leg,  fr.  ON.  leggr,  ‘leg’ (which  is  rel.  to  ON.  armleggr,  ‘arm’),  which  is prob.  rel.  to  OE.  lira  (for  *ligiza),  ‘fleshy  part  of the  body,  flesh’,  ON.  Her,  Swed.  lar,  ‘thigh’,  and prob.  cogn.  with  OI.  rk^ald,  ‘foot  joint  of  a hoofed  animal’,  L.  lacertus,  ‘upper  arm,  arm’, lacerta,  '
=====
```


## [2026-09-06T23:13:25.894Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nfor m in re.finditer(r\"\\b(8[7-9]\\d|90\\d)\\b\", t[5440000:5545000]):\n    print(m.group(1), 5440000+m.start(), repr(t[5440000+m.start()-60:5440000+m.start()+60]))\nEOF"
}
```


### [2026-09-06T23:13:30.283Z] TOOL RESULT

```
888 5454642 'life,  body’,  G.  Leib,  ‘body’,  prop,  ‘con-\nlifer\nlilac\n888\ntinuance,  perseverance’,  fr.  I.-E.  base  *lip-,  ‘to'
889 5461153 '  the  sense  development  of  Du.  lichtercp.  F.  allige.\n889\n‘lighter’,  fr.  alleger,  ‘to  lighten’,  fr.  L.  alle'
890 5470543 ') lim  bate,  adj.,  edged,  bordered.  —  Late  L.  limbd-\n890\ntus,  fr.  L.  limbus,  ‘hem,  border’.  See  prec.  wor'
891 5473628 'urvy.\nIlmen,  n.,  the  threshold  of  consciousness  (pry-\n891\nchol.)  —  L.  Ilmen,  gen.  liminis,  ‘threshold’,  pro'
892 5483056 'an’.  Sec lean,  ‘to  incline’,  and  -et  and  cp.  links.\n892\n893\nlinchpin,  n.,  a  pin  passing  through  the  end  '
893 5483060 '  Sec lean,  ‘to  incline’,  and  -et  and  cp.  links.\n892\n893\nlinchpin,  n.,  a  pin  passing  through  the  end  of  '
897 5504998 '  and  SivSpov,  ‘tree’.  See  lily  and  dendro-.\nliripipe\n897\nlithotrity\nliripipe,  liripoop,  n,,  the  tail  at  the'
898 5520801 " tive  is  expressed  by  the  negative  of  its  opposite.\n898\n—  Gk.  XFnj-n'ic,  ‘plainness,  simplicity’,  fr. Xtxoc"
899 5523992 '\nUtaus,n.,  the  crooked  staff  borne  by  the  augurs.  —\n899\nL.,  of  uncertain  etymology ;  possibly  a  deriv.  of'
900 5533323 'l,  hos¬ tile’.  See  loath.\nDerivative:  loathli-ness,  n.\n900\nlob,  n.,  a  clumsy  person.  —  Orig.  prob.  imitativ'
901 5536256 'itds,  ‘locality’,  fr.  locdlis.  See  local .  and  -ity.\n901\nlocate,  tr.  v.,  to  find  the  place  of.  —  L.  loe'
```


## [2026-09-06T23:13:42.788Z] TOOL CALL #34: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg308.png"
}
```


### [2026-09-06T23:13:43.147Z] TOOL RESULT

```

```


## [2026-09-06T23:13:43.144Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T23:14:12.381Z] TOOL CALL #35: Bash

```json
{
 "command": "sed -n '1,50p' tools/fetch_source.py; echo ...; sed -n '50,120p' tools/fetch_source.py"
}
```


### [2026-09-06T23:14:12.433Z] TOOL RESULT

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
...
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
                title = html.unescape(mt.group(1)).strip() if mt else ""
                text = html_to_text(body)
            else:
                text = body
    except Exception as ex:
        status = -1
        text = f"FETCH FAILED: {ex}"
    header = f"URL: {url}\nFETCHED: {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}\nSTATUS: {status}\nTITLE: {title}\n\n"
    with open(path, "w", encoding="utf-8") as f:
        f.write(header + text)
    with open(INDEX, "a", encoding="utf-8") as f:
        f.write(json.dumps({"url": url, "file": os.path.relpath(path, ROOT), "fetched": header.split("\n")[1][9:],
                            "status": status, "bytes": len(text), "title": title, "note": note}, ensure_ascii=False) + "\n")
    print(path)
    return 0 if status == 200 else 1


if __name__ == "__main__":
    sys.exit(main())
```


## [2026-09-06T23:14:24.461Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wiktionary.org/wiki/%D9%81%D8%B1%DB%8C%D9%81%D8%AA%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D9%81%D8%B1%DB%8C%D8%A8\" \\\n \"https://en.wiktionary.org/wiki/%D8%B1%DB%8C%D9%88\" \\\n \"https://en.wiktionary.org/wiki/%D8%B1%D8%B3%D8%AA%D8%A7%D8%AE%DB%8C%D8%B2\" \\\n \"https://en.wiktionary.org/wiki/%D9%84%DA%AF%D8%AF\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 308 verification: Persian nodes (farib/fariftan/riv, rastaxiz, lagad)\"\ndone"
}
```


## [2026-09-06T23:14:26.123Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://www.etymonline.com/word/leg\" \\\n \"https://www.etymonline.com/word/lizard\" \\\n \"https://www.etymonline.com/word/locust\" \\\n \"https://www.etymonline.com/word/lobster\" \\\n \"https://www.etymonline.com/word/life\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 308 verification: Lek/Leip English nodes\"\ndone"
}
```


### [2026-09-06T23:14:30.208Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/4c7df3280459d0b8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/140b2454e1a6aa49.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5653ce2c75428577.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/bd6a4475dbb86574.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/229f34747fe8e9aa.txt
```


### [2026-09-06T23:14:34.220Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/7502f7141ec1eb93.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5cdb7745fcd8f314.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5dc557f8f2a8e707.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cd1f2717df1b062f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/94c7c8960dbf2e96.txt
```


## [2026-09-06T23:14:37.090Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in 4c7df3280459d0b8 140b2454e1a6aa49 5653ce2c75428577 bd6a4475dbb86574 229f34747fe8e9aa; do echo \"########## $f\"; head -4 $f.txt; grep -n -A6 -i 'Etymology' $f.txt | head -60; done"
}
```


### [2026-09-06T23:14:39.043Z] TOOL RESULT

```
########## 4c7df3280459d0b8
URL: https://en.wiktionary.org/wiki/%D9%81%D8%B1%DB%8C%D9%81%D8%AA%D9%86
FETCHED: 2026-09-06T23:14:27Z
STATUS: 200
TITLE: فریفتن - Wiktionary, the free dictionary
65: Etymology 
66-
67- 1.3 
68- Pronunciation 
69-
70- 1.4 
71- Verb 
--
150: Etymology
151- [ edit ] 
152-
153- From Middle Persian [script needed] ( pldp /⁠frēb-⁠/ , “ to deceive ” ) , from Proto-Iranian *fra- + *dab- ( “ to deceive ” ) , the latter from Proto-Indo-European *dʰebʰ- ( “ to harm, deceive ” ) and cognate with Sanskrit दभ् ( dabh , “ to harm, deceive ” ) and Hittite [script needed] ( tepnu- , “ to decrease, to humble ” ) .
154-
155- Pronunciation
156- [ edit ] 
########## 140b2454e1a6aa49
URL: https://en.wiktionary.org/wiki/%D9%81%D8%B1%DB%8C%D8%A8
FETCHED: 2026-09-06T23:14:28Z
STATUS: 200
TITLE: فریب - Wiktionary, the free dictionary
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
--
85: Etymology 
86-
87- 2.2 
88- Pronunciation 
89-
90- 2.3 
91- Noun 
--
172: Etymology
173- [ edit ] 
174-
175- Present stem of فریفتن . From Middle Persian [script needed] ( plyp /⁠frēb⁠/ , “ deceit, deception ” ) , from Proto-Iranian *fra- ( “ toward ” , from Proto-Indo-European *pro- ) + *dab ( “ to deceive ” , from Proto-Indo-European *dʰebʰ- ( “ to deceive; to harm ” ) ) .
176-
177- Pronunciation
178- [ edit ] 
--
248: Etymology
249- [ edit ] 
250-
251- Borrowed from Classical Persian فریب ( fareb, firēb ) . First attested in c. 1692 as Middle Hindi فریب ( fryb ) . [ 1 ] 
252-
253- Pronunciation
254- [ edit ] 
########## 5653ce2c75428577
URL: https://en.wiktionary.org/wiki/%D8%B1%DB%8C%D9%88
FETCHED: 2026-09-06T23:14:29Z
STATUS: 200
TITLE: ریو - Wiktionary, the free dictionary
########## bd6a4475dbb86574
URL: https://en.wiktionary.org/wiki/%D8%B1%D8%B3%D8%AA%D8%A7%D8%AE%DB%8C%D8%B2
FETCHED: 2026-09-06T23:14:29Z
STATUS: 200
TITLE: رستاخیز - Wiktionary, the free dictionary
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
--
139: Etymology
140- [ edit ] 
141-
142- Inherited from Middle Persian [Book Pahlavi needed] ( lystʾhyc /⁠rist-axēz⁠/ , “ resurrection ” ) . That latter part xēz is related to خاستن ( xâstan , “ to rise ” ) .
143-
144- Pronunciation
145- [ edit ] 
########## 229f34747fe8e9aa
URL: https://en.wiktionary.org/wiki/%D9%84%DA%AF%D8%AF
FETCHED: 2026-09-06T23:14:30Z
STATUS: 200
TITLE: لگد - Wiktionary, the free dictionary
65: Etymology 
66-
67- 1.3 
68- Pronunciation 
69-
70- 1.4 
71- Noun 
--
146: Etymology
147- [ edit ] 
148-
149- Inherited from Proto-Indo-Iranian [Term?] , a suffixed form of Proto-Indo-European *lek- ( “ to bend, leg ” ) . [ 1 ] Cognate with Ancient Greek λάξ ( láx , “ with the leg/heel ” ) , Ancient Greek λᾰκτῐ́ζω ( lăktĭ́zō , “ to kick ” ) ; Sanskrit लकुट ( lakuṭa , “ stick, club ” ) ; Sauraseni Prakrit 𑀮𑀢𑁆𑀢𑀸 ( lattā , “ kick ” ) , the latter probably from an unattested Sanskrit word for "to kick". [ 2 ] 
150-
151- Pronunciation
152- [ edit ]
```


## [2026-09-06T23:14:56.726Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== CHEUNG raip\"; grep -n -i 'raip\\|frēftan\\|fre:ftan\\|fareftan\\|farēftan\\|frēb' CHEUNG.txt | head -30\necho \"=== CHEUNG dab\"; grep -n -i '^\\*dab\\|\\*dab \\|dab: to deceive\\|dabaiti' CHEUNG.txt | head -20"
}
```


### [2026-09-06T23:14:56.794Z] TOOL RESULT

```
=== CHEUNG raip
20237:308 *raip ? 
20267:*raip ? ‘to smear’ 
57930:*dauH’, *raip, *sard 
=== CHEUNG dab
3846:42 *dab 
3873:*dab ‘to deceive’ 
55361:*dab (s.v.), *ia(m)b/p (s.v.), 
56001:*dab, *drauj, *karz 
56284:*dab, *drauj, *karz
```


## [2026-09-06T23:14:57.858Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HUB fireften\"; grep -n -i 'fireften\\|firēften\\|rew\\b' HUB.txt | head -20\necho \"=== NYB freftan\"; grep -n 'fréftan\\|freftan' NYB_vol2_glossary.txt | head"
}
```


### [2026-09-06T23:14:57.924Z] TOOL RESULT

```
=== HUB fireften
2828:hismarento^ aiwi-smareW^ paiti-smaremna^ aber SumuV"
=== NYB freftan
1592:fréftan [pldptn'] frév- [pldp-] to deceive, to seduce 3311. 6812.. 9017, — From fra + Av. (679 sq.) !dab-; Paz. fréftan frév-; NP fweftan fireb-. V. also frēv, viyiftan.
5102:(fra-)dab-: fréftan
6574:fréftan, frév-:
7137:firéftan, firéb: fréftan firistádan, firist: fréstitan firistah: fréstak
```


## [2026-09-06T23:15:02.971Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== CHEUNG *dab p42\"; sed -n '3873,3960p' CHEUNG.txt"
}
```


### [2026-09-06T23:15:03.019Z] TOOL RESULT

```
=== CHEUNG *dab p42
*dab ‘to deceive’ 

*AVESTAN: dab- ‘to deceive’ — Liste: 27 

Pres. nu-: INJ. 2р1. OAv. dobonaota (Y 325); Caus.: pres. IND. 3sg. OAv. dabaiieiti (Y 43.6), INJ. 35р. 
OAv. aipi.dabauuaiiat (Y 31.17); Inf.: desid. OAv. diBZdiiai (Y 45.4) 

*MIDDLE PERSIAN: (+ *fra-) BMP pldp- /fréb-/ ‘to deceive’ || (+ *ui-) MMP wyyb-, 
MMP wyd(y)b- ‘to deceive, delude’, MMP wyps- (inch.) ‘to be deceived’, 
(denomin., sec. caus.) BMP wyd’p’nyn- /wiyabén-/, wyd’p’n’n- /wiyaban-/ ‘to 
deceive, seduce’ > DMMPP: 351a f. 

(+ *fra-) Pres.: IND. 3sg. BMP pldpyt /frébéd/, 3pl. BMP pldpynd /frébénd/; Partic.: perf. pass. BMP 
pldptk /fréftag/ || (+ *ui-) Pres.: IND. 359. MMP wyybyd, 3р1. MMP wyybynd, MMP *wybynd, SUBJ. 
3sg. MMP wyb’d, 3pl. ? MMP "wyb'nd; Partic.: pres. MMP wyyb'g, perf. pass. MMP wyptg, MMP 
wyftg, MMP wyptg, MMP wypt, wypt, муй, муй, caus. BMP wyd’p’nynyt /wiyabénid/; Inf.: caus. BMP 
wyd’p’n’nytn /wiyabanidan/; Inch./Pass.: pres. IND. 35р. wypsyd, SUBJ. 3р1. MMP *wyps’nd 
*PARTHIAN: db ‘trick, deception’ || (+ *ui-) wdyfs- (orig. inch.) ‘to be deceived’ 
c Ghilain: 81 | DMMPP: 136b, 339b f. 

(+ *ui-) Pres.: IND. 3pl. “wdyfsynd; Partic.: perf. pass. wdyftg, (pl.) wdyftg’n, wdyft 

*KHOTANESE: (+ *ui-) LKh. bev- ‘to deceive, injure’ = SGS: — 

*SOGDIAN: (+ *pari-) CSogd. prdbn ‘deceit’ || (+ *ui-) CSogd. wyd’b ‘harm’, CSogd. 
wyd'bqyn ‘harmed’ 


*daHl 43 


*CHORESMIAN: (+ *pari-) prößs- ‘to be deceived’, prö’ßy- (caus.) ‘to deceive’ 
= Samadi: 151 

*NWIR: (+ *fra-) NP faréftan/faréb- ‘to deceive’ 

*NEIR: Oss. І. davyn/davd, D. davun/davd ‘to steal’, Wa. ӧыу(ы)у-/боуоуй, 
ӧым(ы)у-/бомоуа ‘to steal’, also berw-/bowd ‘to deceive’ 

*SANSKRIT: dabh ‘to deceive’ (RV+) = EWAia I: 694 f. 

«PIE *d"eb"- ‘to deceive, harm (someone), belittle, lessen’ > LIV: 132 f. | Pok.: 240 
*IE COGNATES: Hitt. /tepnu-/ ‘to decrease, to humble’ 

*REFERENCES: IIFL II: 521; Abaev, Slovar’ I: 348; DKS: 304b; Werba 1997: 193 f.; Steblin-Kamenskij 
1999: 112, 168; ESIJa II: 274 ff. 


*daH! чо give’ 

*AVESTAN: dă- (6a-) ‘to bestow, place upon’ || (+ *abi-) *beigeben, beilegen’ || (+ 
*3-) ada- ‘to give, pay back, return the favour (sim.), [med.] to receive [Panaino, 
Tist.: 109]? (occasional, late shortening of initial 4-, De Vaan 2003: 135) || (+ *para-) 
‘to give away’ || (+ *pari-) ‘to pass, hand over’ || (+ *fra-) ‘to bestow’ || (+ *ui-) ‘to 
divide, share to’ | Liste: 29 

Pres. {1} ает. red.: IND. 15р. YAv. dadami, med. OAv. dade (Y 28.4), YAv. dai8e (Y 11.17), 2sg. 
Y Av. daöähi (Yt 10.30), 3sg. OAv. dadaiti (Y 33.14), Y Av. daóaiti (N 84), med. OAv. daste (Y 34.1), 
Y Av. daste, Y Av. adaste (Yt 8.14), 1р1. OAv. dadomahi? (Y 35.5, Y 39.4), OAv. dadamahi (Y 41.1), 
Y Av. dadomahi(?) (Vr 8.2, Vr 11.21, A 3.6), YAv. danmahi (Y 68.1), 1р1. med. dadomaide (Y 35.9, Y 
41.3, etc.), 3pl. OAv. райт dadaiti (Y 46.1), ? Y Av. *daóaiti (Yt 10.3), INJ. 1sg. YAv. дадат, 25р. OAv. 
dada (Y 31.9, Y 31.11, Y 44.15, Y 46.7), 3sg. OAv. dadät (Y 30.7, Y 30.11, Y 31.21, ete., YAv. daöät, 
3pl. OAv. ni dadat (Y 32.14), SUBJ. 1sg. YAv. da0ani, 2sg. Y Av. para.da00 (V 18.28), 3sg. OAv. dadat 
(Y 27.13, Y 29.9), Y Av. da@at, YAv. para.dadat (V 18.28), 1р1. YAv. “Чабата, 3р1. OAv. dadon (Y 
30.8), YAv. dadon, med. 3р1. OAv. dadente (Y 31.14), OPT. 15р. med. (?) ҮАУ. аде (Yt 5.130, Yt 
10.80), YAv. fradaidiia (V 18.52), med. Y Av. *dai0isa (V), 3sg. OAv. daidit (Y 28.2, Y 43.14, Y 43.16, Y 
46.2), YAv. daióiiat, YAv. para.daidiiät (A 3.7 f£), Y Av. para.daiöiiät (V 19.27), med. OAv. daiditä 
(43.12, 46.18), YAv. °dai@ita, 3du. Y Av. daióitom, 3р1. YAv. daiOiiaras, Y Av. °daidiian, IMPV. 250. 
Y Av. dazdi, med. 2sg. OAv. dasuuä (Y 33.12), 3sg. OAv. dadatü (Y 53.8), 2pl. YAv. dasta (Y 68.21), 
med. 2р1. OAv. -dazdüm (Y 53.5); Pres. {2} them. red.: IND. 3sg. YAv. "data (V 4.3 £), med. 35р. 
Y Av. dadaite (Yt 19.11, Yt 19.89, Vyt 50), med. 3pl. YAv. *da6onte (V 8.100 f£), INJ. 1sg. YAv. da0om, 
3sg. YAv. dadat, 3pl. YAv. da0on, SUBJ. 3sg. YAv. *da0aiti, ОРТ. 3pl. Y Av. *°da@aiion (V 7.74); Aor. 
{1} athem.: INJ. 2sg. OAv. dà (Y 28.6 £., Y 31.3, Y 34.15, etc.), med. 2sg. OAv. dänhä (Y 44.18), 3sg. 
OAv. dat (Y 37.1, Y 44.3, Y 45.4, etc.), med. 3sg. ? OAv. data (Y 44.20), med. 1pl. OAv. duuaidi (Y 
29.5), 2pl. OAv. data (29.2, ? Y 31.5, Y 33.1), 3pl. OAv. dan (Y 45.10, ? Y 47.1, Y 49.4), SUBJ. med. 
Isg. OAv. -dané (Y 44.9), 2sg. OAv. dāhī (Y 53.9), med. 2sg. OAv. danhe (Y 36.1), 3sg. OAv. daitr (Y 
44.19), OAv. dat, med. 3sg. OAv. daite (Y 44.19, VdPZ 8.10), YAv. daite (Yt 17.15), 1pl. OAv. dama (Y 
34.3), med. 2pl. OAv. daduiie (Y 46.15), 3pl. OAv. dainti (Y 32.15), (Inj.?) OAv. dan (Y 47.1), med. 3pl. 
OAv. danté (Y 48.11), OPT. Isg. OAv. diiam (Y 44.14), med. Isg. OAv. à diia (Y 43.8), 2sg. Y Av. daiia, 
med. 2sg. OAv. disa (Y 43.7), 3sg. OAv. d(a)iiat (Y 43.10, Y 45.9), med. 2pl. YAv. daiiata, IMPV. 2sg. 
OAv. daidi (Y 28.6 f., Y 40.3, Y 51.2, etc.), med. Zeg OAv. dähuuä (Y 50.2), 3sg. OAv. datü (Y 51.17), 
2р1. OAv. data (Y 29.10, Y 34.6, Y 43.13); Aor. {2} s-: IMPV. med. 2pl. OAv. -danhö.düm (Y 45.1); 


44 *daHl 


Perf.: IND. 2sg. OAv. fradada0a (Y 40.1), YAv. dada0a (Y 71.10), 35р. Y Av. dada (Y 12.7), Y Av. dada,
```


## [2026-09-06T23:15:03.561Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== CHEUNG *raip p308\"; sed -n '20267,20340p' CHEUNG.txt"
}
```


### [2026-09-06T23:15:03.609Z] TOOL RESULT

```
=== CHEUNG *raip p308
*raip ? ‘to smear’ 

*NEIR: (+ *ui-) Oss. D. ilivd (old ppp.) “pitiful, wretched’ 

*SANSKRIT: rep, lep ‘to smear, attach’ (RV) = EWAia II: 460 

Except for the fossilised Oss. past participle, no certain Ir. cognate forms of Skt. 
rep, lep can be cited: even the Oss. form is semantically not evident. Several Iranian 
forms frequently cited as cognate are probably unconnected: BMP pldp- /fréb-/, NP 
fireb- (fareb-) ‘to deceive’ (< *fra-dab, *dab), Oss. I. felivyn, D. fzelevun ‘to 
deceive; to be unfaithful’ (< Oss. fiel- + I. тууп, D. evun ‘to (ex)change’ < *yaip, 
Cheung 2002: 185). The NP form rév ‘deceit, ruse’ is difficult to assess: Ir. *p can 
hardly yield NP -v in final position, cf. tab ‘fever’, tab ‘glow’ (*tap), x'ab ‘sleep’ 
(*huäp-an-, *huap/f). It cannot be excluded that the NP form is a rhyming word. In 
Persian script rev (,.,) is almost identical with dev (>) ‘devil’. 

«PIE *leip- ‘to stick, be sticky’ — LIV: 405 f. | Pok.: 670 f. 

*IE COGNATES: Gr. Aınatvo ‘I oil’, Aınapog ‘fat, oily’ Lith. тро (lipti) ‘I stick’, 
Russ. lipkij ‘sticky’ 

*REFERENCES: Abaev, Slovar’ I: 543; Werba 1997: 228 


*rai§ ‘to suffer (damage, illness)’ 
*AVESTAN: Y Av. raes- ‘to get hurt, suffer damage’ = Liste: 59 


*га102 309 


Pres. ja-: IND. 350. YAv. irisiieiti (V 13.38, V 15.4, V 15.6, V 15.8, etc.), SUBJ. 3sg. YAv. irisiiat (V 
7.38, V 13.37, V 15.4, etc.), 3pl. YAv. irisiian (V 15.22, V 15.40); Partic.: pres. YAv. irisint- (V 15.12, V 
15.22, V 15.40, Vyt 44); Caus.: pres. IND. 3sg. Y Av. "raesaiieiti (V 5.12), SUBJ. 3sg. YAv. raesaiiat (V 
15.11, Vyt 44) 

*MIDDLE PERSIAN: BMP lys- /rés-/ ‘to wound, hurt’ 

*NWIR: NP res ‘wound’, also borrowed into Kurd. ris, Bal. res ‘id.’ 

*NEIR: Oss. I. rissyn/ryst, D. resun/rist, Wa. riZ/rizd- ‘to be ill’, (caus.) 
riZ(bI)v-/riZovd- ‘to cause illness’ (pres. -Z- from pret.), Oss. I. ris ‘illness’, Wa. rizg 
‘illness, disease’, ? Sariq. rizd ‘pain’ (rather *rais ?) || (+ *upa-) Pash. bréx (m.) 
‘twitch of pain, cramp, spasm’, ? Sh. biréj ‘a worm dangerous for sheep’ (< 
*upa-raisa-Ci- ?) 

*SANSKRIT: res ‘to get harmed, hurt’ (RV+) = EWAia II: 462 

9 The root appears to be exclusively Ш. 


*REFERENCES: Horn 1893: 142; EVP: 15; MacKenzie, Pahlavi: 72; Abaev, Slovar’ II: 411 f.; EVS: 20b, 
71b; Nyberg II: 169b; Werba 1997: 229; Steblin-Kamenskij 1999: 296 f.; NEVP: 15 


*rai0! ‘to lead, go forth; [euphem.] die, pass away’ 

*AVESTAN: Y Av. IrI0- ‘to die, pass away’ || (+ *para-) ‘id.’. Ф Kellens 1984: 320 also 
assigns iridontom (Yt 5.130) to this root, but the passage is rather obscure. = Liste: 
58 

Pres. ja-: IND. 35р. ҮАУ. iridiieiti (V 6.10, V 6.12, V 6.14, etc.), 3р1. YAv. para.iriinti (V 6.1 ЁЁ), INJ. 
25р. Y Av. para.iri0iiö (H 2.16), SUBJ. 3sg. YAv. iriiiat (V 5.27, V 5.39, V 8.1, eet Perf.: OPT. 35р. 
irraidiiät (ViD 17); Partic.: pres. YAv. para.iridiiant- (H 2.16), perf. YAv. iririüus- (Y 24.5, Y 26.6, Y 
59.21 f£, Vr 11.7), med. YAv. iririüana- (Р 23, P 34), perf. pass. YAv. irista- (Yt 13.9, Yt 19.11, Yt 
19.89, etc.) 

*NEIR: (+ *apa- or *abi-) Oss. I. evrityn/aervyst, D. aervetun/zrvist ‘to send, lead’ 

9 Further Ir. cognates are unknown. 

«PIE *leitH- ‘to go (forth), pass (away)’ = LIV: 410 | Pok.: 672 

*IE COGNATES: Toch. Ш- ‘to pass on, move’, Goth. ga-leiban ‘to go’, ON Iida ‘to go
```


## [2026-09-06T23:15:56.605Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad\npdftoppm -f 308 -l 308 -r 600 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg308hi\npython3 - <<'EOF'\nfrom PIL import Image\nim=Image.open('pg308hi.png'); print(im.size)\n# page at 200dpi was 1700x2200 -> at 600dpi 5100x6600 ; scale 3\n# laipjan box approx x 365-545, y 915-990 at 1545-wide display -> original 1700 wide: *1.10\n# use fractions from the 1700x2200 render\ndef crop(name, x0,y0,x1,y1):\n    W,H=im.size\n    im.crop((int(x0*W),int(y0*H),int(x1*W),int(y1*H))).save(name)\ncrop('p308_germ.png', 0.20,0.405,0.40,0.455)\ncrop('p308_greek.png',0.20,0.550,0.45,0.590)\ncrop('p308_skt.png',  0.20,0.135,0.40,0.185)\nEOF\nls -la p308_*.png"
}
```


### [2026-09-06T23:16:00.782Z] TOOL RESULT

```
(5100, 6600)
-rw-rw-r-- 1 sfmqrb sfmqrb 4663 Sep  6 19:16 p308_germ.png
-rw-rw-r-- 1 sfmqrb sfmqrb 3008 Sep  6 19:16 p308_greek.png
-rw-rw-r-- 1 sfmqrb sfmqrb 3816 Sep  6 19:16 p308_skt.png
```


## [2026-09-06T23:16:03.077Z] TOOL CALL #44: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p308_germ.png"
}
```


### [2026-09-06T23:16:03.104Z] TOOL RESULT

```

```


## [2026-09-06T23:16:10.001Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad\npython3 - <<'EOF'\nfrom PIL import Image\nim=Image.open('pg308hi.png'); W,H=im.size\ndef crop(name, x0,y0,x1,y1):\n    im.crop((int(x0*W),int(y0*H),int(x1*W),int(y1*H))).save(name)\ncrop('p308_germ2.png', 0.20,0.450,0.40,0.505)\ncrop('p308_greek2.png',0.20,0.605,0.45,0.650)\ncrop('p308_skt2.png',  0.20,0.140,0.40,0.200)\ncrop('p308_lat2.png',  0.20,0.650,0.80,0.700)\nEOF\necho ok"
}
```


### [2026-09-06T23:16:12.405Z] TOOL RESULT

```
ok
```


## [2026-09-06T23:16:14.490Z] TOOL CALL #46: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p308_germ2.png"
}
```


### [2026-09-06T23:16:14.508Z] TOOL RESULT

```

```


## [2026-09-06T23:16:18.389Z] TOOL CALL #47: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p308_greek2.png"
}
```


### [2026-09-06T23:16:18.407Z] TOOL RESULT

```

```


## [2026-09-06T23:16:27.045Z] TOOL CALL #48: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg308.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/308.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | tail -5"
}
```


## [2026-09-06T23:16:27.083Z] TOOL CALL #49: Bash

```json
{
 "command": "timeout 300 python3 tools/ref_page.py BQT:991 --image 2>&1 | head -40"
}
```


### [2026-09-06T23:16:27.118Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb  90918 Sep  5 10:16 92.png
-rw-rw-r--  1 sfmqrb sfmqrb  93420 Sep  5 10:18 94.png
-rw-rw-r--  1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r--  1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r--  1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
```


### [2026-09-06T23:16:28.842Z] TOOL RESULT

```
no scan of BQT covers printed page 991 (see 'scans' in refs_online.json)
```


## [2026-09-06T23:16:33.228Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nhead -5 BQT_v2_pages.txt; echo \"...\"; grep -c $'\\f' BQT_v2_pages.txt; grep -o '\\[pdf page [0-9]*\\]' BQT_v2_pages.txt | head -3; grep -o '\\[pdf page [0-9]*\\]' BQT_v2_pages.txt | tail -3"
}
```


### [2026-09-06T23:16:35.152Z] TOOL RESULT

```
                                         ‫‪7‬‬

                          ‫رن‪۳‬‬
    ‫نات‬
      ‫ا م‬
...
680
```


## [2026-09-06T23:16:47.867Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(\"pages:\",len(pages))\nimport re\nfor w in ['رستخیز','رستاخیز','ریو','ریوند','فریب','فریفتن','رستم']:\n    hits=[i for i,p in enumerate(pages) if w in p]\n    print(w, hits[:12])\nEOF"
}
```


### [2026-09-06T23:16:49.587Z] TOOL RESULT

```
pages: 684
رستخیز [408, 561]
رستاخیز [408, 450, 563, 595]
ریو [20, 48, 87, 128, 185, 195, 202, 227, 231, 245, 273, 302]
ریوند [371, 393, 453]
فریب [18, 43, 66, 86, 87, 174, 277, 300, 336, 339, 341, 349]
فریفتن [212, 303, 453]
رستم [89, 123, 236, 317, 329, 380, 402, 408, 409, 434, 460, 470]
```


## [2026-09-06T23:17:08.870Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in [396,397,398,406,407,408,409]:\n    p=[l for l in pages[i].split('\\n') if l.strip()]\n    print(\"### leaf\",i, \"first:\",p[:2], \"last:\",p[-2:] if p else None)\nEOF"
}
```


### [2026-09-06T23:17:11.261Z] TOOL RESULT

```
### leaf 396 first: ['\u202bومطلوب را گویند و مردم ماز ندران ربکا\u202c         \u202bمصوب\u202c        \u202bراهی = بر وزن ماهی \u202a" ۰\u202cان لواشرا\u202c', '                             \u202bخواناد حذف الف \u202a.\u202c\u202c                        \u202bکومند بت و راه رونده را نیزگفته\u200cایر\u202a٩\u202c\u200f\u202c'] last: ['                                                   \u202bرا\u202c\u202bاز\u202a :\u202cرای (\u202c            \u202b\u202a۷\u202c\u202c            \u202b(رعتی) \u202ayerT\u202c\u200f (سر) \u202a۰\u202c\u202c', '                                                                                            \u202bراعگان («\u202a.\u202cم\u202a. ).\u202c\u202c']
### leaf 397 first: ['                                                 \u202bبیان دوم\u202c', '                        \u202bدررای بی\u200cنقطه بابای |بحد مشتمل بر دوازده لغت\u202c'] last: ['                  \u202b\u202aBenveniste; ,3391,.۸1 .0.1 061,413 ,8810 naidgoS naol\u202c\u202c                                \u202b\u202a5\u202c\u200f\u202c', '        \u202b\u202a... BSOS., .۸2 ,1 .p\u202c\u202c            \u202b\u202a۰\u202c\u200f\u202c']
### leaf 398 first: ['  \u202b—\u202a—Ara\u202c\u202c                                                                                                         \u202bربوسه\u202c', ' \u202bبرون؟ \u202a -\u202cبفتح اول بر وزن زبون \u202a.\u202c\u202c                              \u202bومجاممت بهم رسد خصوصاً ؛ و باینه\u200cعنی با زای\u202c'] last: ['                                                           \u202bمانوی (یهلوی) \u202andwbr\u202c\u200f ( ربودن غ*ارت ) \u202a.\u202c\u202c', '           \u202b\u202aHenning, A list of Middle\u202c\u202c                         \u202b\u202aPersian..., BSOS, IX, 1, p. 87.\u202c\u202c']
### leaf 406 first: ['      \u202b\u202a- 6\u202c\u202c                                                                               \u202bرژیدن\u202c', '\u202bرر بدن "ت بورژن رسیدن » بمعنی\u202c                      \u202bاندازند وبعربی شربط کوبند وبزبان دیگر سازو\u202c'] last: ['                         \u202b\u202a ۸\u202cا\u202c                            \u202b[\u202a( 8۲\u202cردیف \u202a .\u202cصف )\u202a .\u202cرك\u202a :\u202cرده » رجه \u202a.\u202c\u202c', '                                                                  \u202bبرایررفرمانده «رژه » گوبند\u202a.\u202c\u202c']
### leaf 407 first: ['                                                    \u202bبیان دهم\u202c', '          \u202bرای می نقطه باسین بی نقطه مشتمل بر ببست وبك لفت و کنایت\u202c                                  \u202bدر\u202c'] last: ['               \u202b\u202a.\u202c\u202c     \u202bخمروی\u202c    \u202b\u202a.\u202c\u202c   \u202bبر خادم هندو دو رست\u202c   \u202bکردش\u202c', '      \u202b\u202a€\u202c\u202c    \u202bد لفت فرس*\u202a4\u202c\u202c']
### leaf 408 first: [' \u202b—\u202aAtA-\u202c\u202c                                                                                          \u202bرستاخیز\u202a\u200e\u202c\u202c', ' \u202bرستگار است کهبمعنی خلاص و فجات باشد \u202a-\u202c\u202c                    \u202bبموط هم\u202c     \u202bضحک\u202c'] last: [' \u202b\u202a ۱\u202cاابمرده ( اتيانربخ در مجلهٌ پیام لو\u202a .\u202cتهران \u202a .\u202cسال سوم اشزمار \u202a ۱\u202cببعد از ترجمةً روسی\u202c', '     \u202bشبه درصفحهٌ \u202a44٩\u202c\u200f\u202c']
### leaf 409 first: ['  \u202bبا\u202c                                                                                             \u202b\u202a-\u202c\u202c', '\u202bوفتح فوقالی وها ومیم هردوسا کن » رستم زالرا\u202c         \u202bرسته \u202a ۱\u202cب«روزن دسته \u202a ۰\u202cبمعنی خلاص\u202c'] last: ['                                 \u202b=ویدن («\u202a.\u202cم\u202a ).\u202c؛ تموکردن ؛ بالیدن ؛ بیرونآمدن؛ سیز شدن\u202a.\u202c\u202c', '                                                                                     \u202bر\u202c']
```


## [2026-09-06T23:17:22.444Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in [450,451,452,453]:\n    p=[l for l in pages[i].split('\\n') if l.strip()]\n    print(\"### leaf\",i,\"printed\",i+540)\n    for l in p[:3]: print(\"  \",l)\n    print(\"   ...\")\n    for l in p[-4:]: print(\"  \",l)\nEOF"
}
```


### [2026-09-06T23:17:24.996Z] TOOL RESULT

```
### leaf 450 printed 990
       ‫اس‬                                                                                                  ‫رىژك‬
                ‫ماضی ریدن و لجاست کردن باشد ‪.‬‬                          ‫وآرزو و هوا وهوس را بیز گفته‌اند ‪٩‬‏ ‪.‬‬
   ‫= بروزن زستن» فرورفتن بچاه‬              ‫ی‬‫ل‬                   ‫ریژ ك ‪ -‬بکر اول وفتح زای فارسی‬
   ...
              ‫ز‪7‬‬ ‫(وچی‬
                    ‫_ هندی باستان ربشه ‪tahsêr , ۲5۵۲ -‬‏ (زخمی‌شدن)‪ ,‬کردی وبل‬        ‫‪0‬‬
           ‫«اسشق ‪« : ۱8۹‬مصلحت ندبدم ازین بیش ریش دروش را بملامت‌خراشیدن » « کلستان ‪۰ ۹۳‬‬
                    ‫‪ -۴‬مصدر است معنی عمر رابسفاعت کنرانیدن‬                       ‫(«‪.‬م‪).‬‬    ‫رس‬     ‫=‬   ‫‪۴۷‬‬
### leaf 451 printed 991
                                                                                                       ‫‪.‬هرهس‬
    ‫چویزها بیاویز قد ‪-‬‬         ‫ا‬
                               ‫هاز‬‫اه‬
   ...
       ‫»ردی‬
          ‫حاصل شده * سنگریزه «ناظم الاطبا»‪ .‬وآن در استی ‪( 81۲‬کردوغبار) «ك ‪ .‬است ‪۲۳۱٩‬‏ ک‬
      ‫ةا و ‪ , 81۲‬افقانی ‪ * 8۵۲‬بلوچی ‪ ۵۲‬و ‪» 5۵۲‬یارسی باستان ‪ * 4612۲ -‬آمده‪ .‬رك ‪:‬اسشق‬
                                 ‫و هوشمان ‪ ۲44.۰‬اشکاشمی ‪( 86۲‬رمل) «کربرسن ‪» ۲۹۰‬کیلکی ‪.811‬‬
### leaf 452 printed 992
      ‫مهوت‬
   ‫دم ‪ = 1‬بروزن‌ميم ‪ ۰‬چرکی باشد که‌از‬                                   ‫و بمعنی ليك بخت هم هست که عربان وبحك‬
                                        ‫جراحت برود ‪.‬‬                    ‫خوانند ‪ ۱‬؛ وباین‌معتی بجای حرف اول واونیز‬
   ...
                       ‫‪:‬‬    ‫‪‘<۴4‬‬   ‫ته دانته «اسشق‬         ‫همر‬           ‫(«‪.‬م‪ ).‬و «ریواین>‬       ‫را بافریو»‬   ‫این معتی‬    ‫رمن“‬
                    ‫بتك خیزند عبانان ريمن ‪.‬‬                                         ‫چو هنگام عزایم زی معزم‬
            ‫‪ ۵‬منوچهری دامفالی ‪۸‬ه * ‪.‬‬
            ‫( برهای فاطع ‪) ۳۱‬‬
### leaf 453 printed 993
     ‫رواد‬                                                                                                ‫‪۱‬‬         ‫‪-‬‬
                                                ‫‪.‬‬        ‫اف‬       ‫و بکر اول مخفف اهریمن امت ‪ ۱‬کرهاه‬
   ‫ریوجام ‏ با جيم بروزن نيك نام ‪۱‬‬                              ‫نمایند بدیها وشیطان باشد ‪ -‬ومحیل و مکار را‬
   ...
     ‫لان ربرند حواصل الریبای و مبابلغم‌الماءِ فى العمق لم بنبت وان كان رأسه فى ذرى الجبال»‪.‬‬
     ‫ح ‪.9‬‬   ‫رکت‪ :‬دراز دست» ربوندرست؛ درازانگل بقلم تگارنده‪ .‬اندو ابرانعاج؟ شمارء‪ ۳-6‬ص‪۵۲‬‬
     ‫ربرنجو («‪.‬م‪).‬‬    ‫‪=۹‬‬              ‫روجو( «م‪ ۴ ).‬رولجه («م‪ ).‬ر‪۳‬بولجە(ھ‪ .‬م‪.).‬‬                           ‫‪۰‬‬
     ‫خبه درصفحة ‪۲٩٩‬‏‬                                                            ‫ر که‪ :‬ربرای ‪.‬‬       ‫‪=۴‬‬
```


## [2026-09-06T23:17:37.244Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(445,462):\n    lat=re.findall(r\"[A-Za-z][A-Za-z\\-\\.']{2,}\", pages[i])\n    if lat: print(i, i+540, lat[:25])\nEOF"
}
```


### [2026-09-06T23:17:38.823Z] TOOL RESULT

```
447 987 ['Rai', 'htiB', 'RAj', 'kihzaR', 'zaR.', 'kazaR.']
448 988 ['Rheum', 'Ribes']
449 989 ['kat', 'Titan', 'hgayir', 'nuj', 'nij', 'nit']
450 990 ['Henning', 'Sogdian', 'BSOS.', 'loan', 'words...', 'hser', 'kahs', 'tayhser', 'tahs']
454 994 ['Rheum', 'officinalis']
456 996 ['zaak']
461 1001 ['Zam', 'EER']
```


## [2026-09-06T23:17:52.652Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\np=[l.strip() for l in pages[408].split('\\n') if l.strip()]\nprint(len(p))\nfor l in p: print(l)\nEOF"
}
```


### [2026-09-06T23:17:54.475Z] TOOL RESULT

```
55
‫—‪AtA-‬‬                                                                                          ‫رستاخیز‪‎‬‬
‫رستگار است کهبمعنی خلاص و فجات باشد ‪-‬‬                    ‫بموط هم‬     ‫ضحک‬
‫می م‬‫وعت‬
‫روبید وبرآمد ‪ - ۱‬وی‬
‫و تزد محققین صاحب دولتی است که زخارف‬                      ‫آمده است ؟ ‪ -‬و نوعی از خاك سخت باشد ‪-‬‬
‫او‬   ‫دامنگیر حال‬   ‫وممنوی‬       ‫و تملقات موری‬    ‫دلوی‬
‫ومطلق خاکه را نکیفزته اند‪ -‬و بمعنی شجاع‬
‫نباشد ‪.‬‬    ‫ودلیر ‪ -‬وچیره وغالب آمدن ومتولی شدن هم‬
‫‪۰‬‬   ‫صبت‬
‫‏‪ o‬بروزن افلااء ‪ ۰‬شاج ءازه ای‬        ‫رستاك‬
‫راکومند که ازبیخ درخت برآبد ؛ و پاین معنی‬                   ‫‪)۱‬‬
‫رستاخیژ ‪ ۴۰‬با خای قطه د(ار‬
‫بشاین قطه دار هم آمده است‪.‬‬                ‫بر وزن دستاویز ‪ ,‬قیامت را گوبند که محشر‬
‫رستخیز ‪ = ۱‬بنتح اول وثالك » بمعنی‬                                                                  ‫باشث ‪.‬‬
‫؛بم اول بمعنی‬
‫رستاخیز است که فیامت باشد و‬
‫رستاد ‪ - ۴‬بر وزن هقتاد ‪ .‬مخفف‬
‫لوخیز باشد ‪.‬‬
‫رستگار ‪ ۲۰‬با ان فارسی بر وزن‬                              ‫راستاد است که بمعنی وظیفه و راب و روزباله‬
‫باشك ‪.‬‬
‫قندهار » بمعتی خلاص ونجات وفیروزی بابنده‬
‫باشد ‪¥.‬‬         ‫رستار * ‪ -‬بر وژن دستار ‪ .‬مخفف‬
‫(‪ )۱‬چك ‪ :‬باخا ‪.‬‬
‫هکر ‪‎ :‬یر ‪.‬‬      ‫‪۰‬‬        ‫‪ :‬رستن ‪.‬‬     ‫رکه‬
‫‪١‬‬
‫‪.‬دذرشته) ‪ .‬بهلوی ‪ + 451۲‬خیز (رك ‪ :‬خاستن) ‪,‬‬
‫‪1‬ست‪۳‬ا‪ ( 805-1‬مرده گ‬
‫‪ - ۴‬از او‬
‫‪,‬ازند ‪ 012۵58051۲‬داسشق ‪ ۳۱۱2‬؛ بنابرین رستاخیز (مخفف آن » رستخیز)‬
‫پهلوی ‪ 2072۱51۲‬پ‬
‫رك‪ :‬راستاد ‪.‬‬   ‫‪۴‬‬              ‫ح ‪۱٩‬‏ ‪.‬‬       ‫لغةبمعنی برخاستن مرد کان است « بشتها اس ‪۳۳۳‬‬
‫تار (یودد فاعلی و اصان ‪.‬رکه ‪ :‬دادار) ‪.‬‬             ‫از ‪ :‬رس ( رستن » رهیدن) ‪+‬‬       ‫‪6‬‬
‫‪۳‬‬   ‫ومخفف خود آن «سَخز » (م‪).‬‬            ‫رستاخیز («‪.‬م‬    ‫‪ - ۷‬مخفف‬
‫‪ - ۷‬از ‪ :‬رست (رستن » رهیدن) ‪ +‬کار (یسوند فاعلی ومبالفه) ‪.‬‬
‫بضم راء و فتح تاء مرکب ازدو جزو‪ :‬رس =‬               ‫تم‬
‫ومس ‪۳‬‬
‫رسته‬
‫‪ #‬رستم = رستهم ‪ ۳‬رو‬
‫(بالش ‪ ,‬نمو) ر[ستن و روبیدن از همين ربشه است] ‪ +‬نهم = ‪ 301321‬درپارسی‬                             ‫‪8‬‬
‫باستان کوانها و دیگر بخشهای اوستا بمعنی دلیرو پپلوان‪ .‬تهمتن ایز ازهمین ریشه است بمعنی‬
‫بزر که پیکر وقوی الدام و درق قت تهمتن معن یکم رستم است‪ .‬بثایرآ اجه کفته شد رستم‌سنی‬
‫کشیده بالا و بز رگے تن وقوی پیکر «یشتها ‪ ۲‬ص‪ ۹۳۱‬نام‌جهان پهلوان ابرانی پسر زال‌پسرسام‪.‬‬
‫مارکوارت تصور کرده است که رتتخم ( اوستا ‪ ) 210251 - 20۳7805‬عنوان وصفتی برای‬
‫ل ‪۰‬ی‪4‌۱۲‬نلد که این فولرامردود داسته‪.‬‬
‫کرشاسپ جهان پهلوان بوده ک‪۵‬رستنسن ک‪.‬یانیان وص‪6‬‬
‫تراكر‪:‬بخ باستاشناسی ‪.‬‬  ‫ست(ان ) یکی میداند ‪.‬‬      ‫یان‬
‫سکت‬
‫پاکانددفشراه س‬‫هرئفلد رستم را با‬
‫تالف هرتفلد ‪ .‬للدن ‪ ۵۳۹۱‬ص ‪۲٩‬‏ ‪ . ۳۱ -‬اتاد هنینگه درمجلة مدرسةٌ السنةٌ شرفی‬
‫لندن ح]]‪ 162‬س ‪۵ - 4۱۱‬ه درمعرفی ونقد کتاب ( مذکور ) هرنفلد کوبد ‪« :‬س رگذشت‬
‫جذاب ‪ 7728۵0۷۳6‬و قصر واقع در «کوه خواجه» (سیستان) بارویگر درسغنرانی (هرتسفلد)‬
‫شرح داده‌شده است ‪ .‬ما میدادم نام ‪0۳0050‬تشدر ‪ ( 5005۷2۳ 620۵۸2۳۱‬قرن پنجم‬
‫که هوبشمان در دستور ارمنی‬         ‫‪ ۳۳۳‬و تاریج بلیام سربالی‬       ‫میلادی) چاپ ‪ecineV‬‏ ‪۶ ۰‬ص‬
‫‪ ۱‬اابمرده ( اتيانربخ در مجلهٌ پیام لو‪ .‬تهران ‪ .‬سال سوم اشزمار ‪ ۱‬ببعد از ترجمةً روسی‬
‫شبه درصفحهٌ ‪44٩‬‏‬
```


## [2026-09-06T23:18:29.542Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (452,453):\n    print(\"======== leaf\",i)\n    for l in [l.strip() for l in pages[i].split('\\n') if l.strip()]: print(l)\nEOF"
}
```


### [2026-09-06T23:18:30.992Z] TOOL RESULT

```
======== leaf 452
‫مهوت‬
‫دم ‪ = 1‬بروزن‌ميم ‪ ۰‬چرکی باشد که‌از‬                                   ‫و بمعنی ليك بخت هم هست که عربان وبحك‬
‫جراحت برود ‪.‬‬                    ‫خوانند ‪ ۱‬؛ وباین‌معتی بجای حرف اول واونیز‬
‫تب‬       ‫ات‬
‫بفارسی کر گدن‌خوانند وکوندشاخی برسربینی‬                              ‫رکا ؟ ه بروزن‌زیبا‪ ,‬مطنوب ومحبوب‬  ‫ی‬
‫دارد ‪۲‬‬
‫و معشوق باشد ‪.‬‬
‫بر وزن شیراز » نوعی از‬          ‫ر بمار س‬                              ‫ریگاسه ‪ ۴‬م با ای مجپول سوین‬
‫جام لطیف بود و آنراکیمیا باکاف فارسی هم‬                              ‫بی‌نقطه بروزن بیجاده » بزبان اهل مروخاریشت‬
‫وف‬                                 ‫کلاترا کونند و بعربی قنقذ خوانند ‪.‬‬
‫زیرکاشه (‪ ۱۸۳‬د با شین نقطه دار ‪.‬‬
‫باشد که دروقت گداختن در کوره‌م‌ماند وبهنگام‬                         ‫بر وزن و معنی ریکاسه است که خارپشت کلان‬
‫يتك زدن ازآن مر یرد ‪.‬‬                                                              ‫تبرانداز باشد ‪.‬‬
‫باکاف‌فارسی ‪ ۰‬بروزن‬     ‫‪ ۲‬هننگ س‬        ‫رلم‬                         ‫ریگ روان = بکس کاف فارسی »‬
‫نیمج استکه بیخ خرغول باشد »‬     ‫هر‬‫آعنی‬
‫وم‬                              ‫ریگی است که درجانب جذوب میباشد و پدوسته‬
‫روان است ‪ .‬گوند آن ریگ تمام نقره است‬
‫وآن چر کے وریم زخم را پاک ازد وآرهبنج‬
‫و هرچشمه که ازآن بر می‌آبد آبش با سیحاب‬
‫آميخته باشدآ ب بربالاوسیماب درزبروهرحیوانیکه‬
‫یمز" بکسراول وفتح‌تالك وسکون‬
‫ر‬                                                             ‫اآزن آب بخورد فی‌الحال بمیرد ‪.‬‬
‫زریگ ریگ کنابه ازذره ذره‌باشد‪.‬‬
‫است که نوعی‬    ‫بمعنتی ریماز‬    ‫نقطه‌دار ‪¢‬‬    ‫انی وزای‬
‫از جامه باشد ‪.‬‬
‫بمعنی ماهی صقنقور‬           ‫ر نگ راده =‬
‫رهسفت ه با سین و عین بی‌نقطه بر‬
‫ل‬                                      ‫ات ‪ » ۵‬وآن جالورست شبیه بماهی وییوسته‬
‫وزن بی‌زحمت» بلفت سربانی دوابی است کهآ نرا‬                                                                ‫در ریگ میباشد ‪.‬‬
‫گرم ست‬     ‫بعربی‌سمد کوبندوبتر کی‌طبلاق‌خوانند‪.‬‬
‫رلو = با لام بروزن بیکو‪ .‬اشخار وقلیا‬
‫ب‬
‫دراول ودوم > وبعضی گوبند بونانی است‪.‬‬                         ‫کضویبند ربلو شنجار است» و آن‬
‫باشد » و بع‬
‫ھن د بفتح اول والك و سکون ثانی‬
‫ر‬                                       ‫رستنیی باشدکه بر کهآن سیاه وبیخش سطبربود ‪.‬‬
‫ولون » محیل ومکار ودغا باز و کینه‌ور باشد‪-۱٩‬‏‬                                                                        ‫آفه اعلم‬
‫)‪ (۱‬چش ‪ :‬ریخاشه ‪.‬‬
‫‪ = ۳‬ریکاشه(هم‪ = ,).‬رکاےه = رکاشه‪.‬‬                  ‫رك‪ :‬رایک‪.‬‬              ‫؟‬           ‫‪ -‬ر ک‪:‬ح‪٩‬‏ صفحهفبل‪.‬‬     ‫‏‪۱٩‬‬
‫‪ - ۹‬شکل پهلوی ‪= 0167‬‬                      ‫‪۰‬‬   ‫رك ‪ :‬سقنقور‬           ‫=‬    ‫‪۵‬‬             ‫= ریکاسه (ھ‪ .‬م(‬      ‫‪۳‬‬
‫و محفف‬     ‫مصحف‬        ‫رك ‪ :‬ریم آهن ‪ ۰‬رم آودكث »> رىمن ‪ ۰‬زریمه ‪۷.‬‬                            ‫بلوچی ‪ « 0۲6۲‬هو شمان ‪۴۹‬‬
‫یو ن‪1‬ان‪7‬ی‪ [50761-62‬یعنی شاخ( دار ) ] کرکدن «فرهنک ہونالی ‪ -‬انگلیسی دل رامکات» ‪.‬‬
‫هرن‬    ‫‪-۱‬‬            ‫‪ :‬ریماز ‪.‬‬   ‫رك‬   ‫‪-°‬‬                ‫‪.‬‬   ‫رم‪‎‬‬    ‫رك ‪:‬‬       ‫‪-‬‬   ‫‪٩‬‬
‫‪ _ ۵‬رك ‪ :‬ریمز ‪.‬‬
‫‪:‬‬    ‫‪‘<۴4‬‬   ‫ته دانته «اسشق‬         ‫همر‬           ‫(«‪.‬م‪ ).‬و «ریواین>‬       ‫را بافریو»‬   ‫این معتی‬    ‫رمن“‬
‫بتك خیزند عبانان ريمن ‪.‬‬                                         ‫چو هنگام عزایم زی معزم‬
‫‪ ۵‬منوچهری دامفالی ‪۸‬ه * ‪.‬‬
‫( برهای فاطع ‪) ۳۱‬‬
======== leaf 453
‫رواد‬                                                                                                ‫‪۱‬‬         ‫‪-‬‬
‫‪.‬‬        ‫اف‬       ‫و بکر اول مخفف اهریمن امت ‪ ۱‬کرهاه‬
‫ریوجام ‏ با جيم بروزن نيك نام ‪۱‬‬                              ‫نمایند بدیها وشیطان باشد ‪ -‬ومحیل و مکار را‬
‫بمعنی بطلان شهوت امت وآن بازایستادن باشد‬                     ‫نیزگفته‌اند ‪ -‬واسب را هممیگویند ‪ -‬و بمعنی‬
‫از کب لذات مطلقاً ‪.‬‬                      ‫‪-‬یک‬
‫پبر هم هت که نقیض دختر باشد ‪ ۴‬و‬
‫اول ثوالث بروزن چرکن » زخهی رگاویند که‬
‫و قاف = بىمنی قاف و دال است‬              ‫ری‬
‫پرومته از آن چرك و ریم آید؟‪ ۴‬و اين نون هم‬
‫که کنابه از هرزه و هرزه کاری و هرزه گوبی‬                     ‫نون ڃر کن است که در | نبا درآ خرچر له‬             ‫همحو‬
‫و کار های عبث باشد ‪ -‬و فول و دلیل را لیز‬                      ‫ودراینجا درآخر ریم افزوده‌اند نه‌لون اصل کلمه‪.‬‬
‫گویند ‪.‬‬
‫ريمه ‪ ۶‬بروزن‌یمه » چركکنج چشم‬
‫ریو اج و" ه بکر اول وسکون ثالی‬                                                            ‫ومیان کمارنها باشد ‪.‬‬
‫مجهول و فتح واو و نون ساکن و جيم مضموم‬
‫ارضه‬   ‫هری‬   ‫که‬   ‫است‬     ‫«محعمی دبوك‬    ‫›‬       ‫بواو زرده‬
‫رلو = بکراول وسکون انی مجهول‬
‫‪7۳‬‬            ‫وواو» بمعتی مکروحیله وترویروفرب باشد ‪۵‬‬
‫وئام پر کی کاوس هم هت که داماد طوس بود‬
‫ريو نحه‪ = ۱۱‬یکی اول وسکون انی‬                                          ‫و بردست فرود بن سیاوش کشته شد ‪.‬‬
‫مجهول و فتح واو و نون ساکن وجیم مفتوح »‬
‫بمعنی ریونجو امت که ارضه باشد ؛ و آن کرمی‬                     ‫دیواج ‪ - ۲‬با انی مجهول وجیم‪ .‬بر‬
‫وزن ومعنی ربوای است که رستنی میخوش نازك‬
‫خودرو باشد ‪.‬‬
‫بکر‬       ‫د‬   ‫ريو ند‬                     ‫دواد د بروزن شیراز » بمعنی عدالت‬
‫اول و سکون نانی و فتح‬                    ‫باشد وآن درستی افعال است وضع هرچیز در‬
‫ثالث و نون و دال هر دو‬                                                      ‫موضم لابق ‪.‬‬
‫است‬       ‫دارو‪:‬ی‬        ‫ساکن ‪۰‬‬           ‫ربو اس باسین‌بی نقطه» بروزن ومعئی‬
‫معروف که اسهال آورد‪۴۱‬‬                 ‫ربواح امت ک‪۸‬ه رستنی مشهور باشد ‪ -‬ویمعنی‬
‫‪.‬‬    ‫و بعربی راوند گویند ‪۴۶‬‬               ‫وریب وافون هم آعده‬       ‫ربا و لفاق ‪ -‬ف‬
‫کرلن‌پهلوی‬
‫‪ ۴‬شه‬                     ‫» رانک ‪.‬‬         ‫‪:‬ریگ‬    ‫ق‬    ‫‪۴‬‬          ‫‪:‬‬    ‫رك ‪ :‬آهریمن‬   ‫_‬   ‫‪۱‬‬
‫ور ‪ 081020۳06۲‬را هم ریش ‪ 621‬اوستابی وربدن فارسی داسته « اسشق ‪ ۰ * ۹۳۱‬وجود‬                                    ‫‪08‬‬
‫ین لبت ) تر کیب شده لظیر ‪ :‬رشکن » ربخن »‬                        ‫‪ 4‬ان ( =‬        ‫‪ 0‬میرساند کهکلمه از ‪ :‬ریم‬
‫*‏ هندی باستان ‪( 01-۲‬حیله) ( از ربعْ ‪806۲-861-‬‬                              ‫رم‬    ‫رك‪:‬‬     ‫‪۴‬‬
‫چر کن‪.‬‬
‫‪ :‬ص نود وسه عقدمه ‪ :‬ریولیز (!) ‪.‬‬                ‫رك‬    ‫‪۱‬‬            ‫کول زدن) ق ‪ :‬فریفتن‪.‬‬
‫‪٩‬‏ ریبای ‏ ریوند‬                      ‫‪ = ۸‬ریبای («م‪. ).‬‬                    ‫‪ = ۷‬رای (هم‪. ).‬‬               ‫‪۱‬‬
‫(‪ 8522-52۷682‬بمعنی ربوند دست ‪۰‬‬
‫ریواج ‏ روج = رویز ؛ از اوستا ‪۲ 52۷6۸2۲‬‬
‫فردست» دارندة دست بافرو باشکوه)‪ .‬بیرونی گوبد «الجماهر ‪ « :»۵۲‬بهمن اردشیر ربوند دست ‪.‬‬
‫لان ربرند حواصل الریبای و مبابلغم‌الماءِ فى العمق لم بنبت وان كان رأسه فى ذرى الجبال»‪.‬‬
‫ح ‪.9‬‬   ‫رکت‪ :‬دراز دست» ربوندرست؛ درازانگل بقلم تگارنده‪ .‬اندو ابرانعاج؟ شمارء‪ ۳-6‬ص‪۵۲‬‬
‫ربرنجو («‪.‬م‪).‬‬    ‫‪=۹‬‬              ‫روجو( «م‪ ۴ ).‬رولجه («م‪ ).‬ر‪۳‬بولجە(ھ‪ .‬م‪.).‬‬                           ‫‪۰‬‬
‫خبه درصفحة ‪۲٩٩‬‏‬                                                            ‫ر که‪ :‬ربرای ‪.‬‬       ‫‪=۴‬‬
```


## [2026-09-06T23:18:53.432Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor f in MON_part1.txt MON_part2.txt; do echo \"### $f size $(wc -c <$f)\"; grep -c 'فریب' $f; grep -c 'لگد' $f; done"
}
```


### [2026-09-06T23:18:55.465Z] TOOL RESULT

```
### MON_part1.txt size 4377831
67
12
### MON_part2.txt size 4331421
45
6
```


## [2026-09-06T23:18:56.183Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \"https://abadis.ir/fatofa/%D9%81%D8%B1%DB%8C%D8%A8/\" \"https://abadis.ir/fatofa/%D9%84%DA%AF%D8%AF/\" \"https://abadis.ir/fatofa/%D8%B1%DB%8C%D9%88/\"; do python3 tools/fetch_source.py \"$u\" --note \"page 308: Mo'in (MON) entries for farib, lagad, riv\"; done"
}
```


### [2026-09-06T23:19:02.327Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/4a9e7301e65219b7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/89a96aee05430523.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0a75a7cbfd555b2b.txt
```


## [2026-09-06T23:19:05.295Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in 4a9e7301e65219b7 89a96aee05430523 0a75a7cbfd555b2b; do echo \"###### $f\"; head -4 $f.txt; grep -n -m3 -A4 'فرهنگ معین\\|معین' $f.txt | head -30; done"
}
```


### [2026-09-06T23:19:07.085Z] TOOL RESULT

```
###### 4a9e7301e65219b7
URL: https://abadis.ir/fatofa/%D9%81%D8%B1%DB%8C%D8%A8/
FETCHED: 2026-09-06T23:18:59Z
STATUS: 200
TITLE: فریب - معنی در دیکشنری آبادیس
20: فریب. [ ف ِ / ف َ ] ( اِ ) در زبان پهلوی فرپ و همریشه است با فریفتن. ( از حاشیه برهان چ معین ). عشوه و مکر و غافل شدن یا غافل کردن به خدعه. ( برهان ) : 
21-توانی بر او کار بستن فریب 
22-که نادان همه راست بیند وریب. بوشکور.
23-چنان دان که یکسر فریب است و بس 
24-بلندی و پستی نماند بکس. فردوسی.
--
58: فرهنگ معین
59-
60- (فِ یا فَ ) [ په . ] (اِ. ) مکر، حیله ، نیرنگ . 
61-
62- فرهنگ عمید
--
191:• فرهنگ فارسی، محمد معین، انتشارات امیر کبیر، تهران، ۱۳۷۵
192-• غلط ننویسیم، ابوالحسن نجفی، مرکز نشر دانشگاهی، تهران، ۱۳۸۶
193-• فرهنگ کوچک زبان پهلوی، دیوید نیل مکنزی، ترجمه مهشید فخرایی، پژوهشگاه علوم انسانی و مطالعات فرهنگی، تهران، ۱۳۷۹
194-
195- منبع. عکس فرهنگ فارسی یافرهنگ عمید
###### 89a96aee05430523
URL: https://abadis.ir/fatofa/%D9%84%DA%AF%D8%AF/
FETCHED: 2026-09-06T23:19:00Z
STATUS: 200
TITLE: لگد - معنی در دیکشنری آبادیس
61: فرهنگ معین
62-
63- (لَ گَ ) (اِ. ) ۱ - ضربه ای که با پا زده شود. ۲ - حرکت یا ضربة قهقرایی تفنگ یا توپ هنگام تیراندازی . ، ~ به بخت خود زدن به ضرر خود اقدام کردن . 
64-
65- فرهنگ عمید
--
148: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
149-
150- لینک ها 
151-
152- حقوق این سامانه وابسته به دیکشنری آبادیس می باشد. 
###### 0a75a7cbfd555b2b
URL: https://abadis.ir/fatofa/%D8%B1%DB%8C%D9%88/
FETCHED: 2026-09-06T23:19:02Z
STATUS: 200
TITLE: ریو - معنی در دیکشنری آبادیس
65: فرهنگ معین
66-
67- [ هن د . ] (اِ. ) مکر، حیله . 
68-
69- فرهنگ عمید
--
109:• فرهنگ فارسی، محمد معین، انتشارات امیر کبیر، تهران، ۱۳۷۵
110-• غلط ننویسیم، ابوالحسن نجفی، مرکز نشر دانشگاهی، تهران، ۱۳۸۶
111-• فرهنگ کوچک زبان پهلوی، دیوید نیل مکنزی، ترجمه مهشید فخرایی، پژوهشگاه علوم انسانی و مطالعات فرهنگی، تهران، ۱۳۷۹
112-
113- ری به رشتی یعنی تو آخر خط یا تو آخر خطی. ر یعنی راه و حرف ی آخرین حروف الفبا است که بمعنی حرف یا خط آخر و حرف ر بمعنی راه و ر. معنی تو هم به زبان گیلکی هست در نتیجه و هم بار بمعنی او هست ریو میشود او یا و آخر خطی هست معنی میدهد
--
130: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
131-
132- لینک ها 
133-
134- حقوق این سامانه وابسته به دیکشنری آبادیس می باشد.
```


## [2026-09-06T23:19:19.873Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== ARY لگد/فریب/رستاخیز\"; grep -n 'لگد\\|فریب\\|رستاخیز' incoming/ARY/ARY_pages.txt | head -20\necho \"=== ARY latin index leip/leit/lek\"; grep -n -i 'LEIP\\|LEIT\\|^LEK\\|LEK ' incoming/ARY/ARY_latin_index_pages.txt | head -20"
}
```


### [2026-09-06T23:19:19.964Z] TOOL RESULT

```
=== ARY لگد/فریب/رستاخیز
48:تفریباً همه‌ی زبانهای اروپا و فلات ایران و بخش شمالی شبیه قاروی هند می‌شود. کوچگری
300:گزمسیری می‌بود در حالیکه تفریباً همه‌ی واژه‌های گرمسیری و استوایی از ریشه‌ی هند و اروپایی
1019:تفریبی مشخص می‌کنند. ۱ :
10068:و زبان‌های رومانس و ژرمنی چم آن ابتدا "لگد زدن" و "پاگذاردن روی چیزی" برده ولی امروزه (به ویژه در
11623:فریفتن» فریب / ۳۹۳
=== ARY latin index leip/leit/lek
8988:LEKKI, LEKKO POLISH) ling) LUK :(TOKHARIAN A) A 5 5
9036:BUCK: 317 LEIPO (GREEK) 3h y 1
11419:(LIVE) 603, (LIFE) 594 BELIBAN, LEIBEN, LEIPA, LEIP, LIB
```


## [2026-09-06T23:19:21.893Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== IEC leip\"; grep -n 'leipō\\|leipo\\|leip-\\|loibho' IEC.txt | head -10\necho \"=== IEC leit\"; grep -n 'leitō\\|leidhō\\|leit-' IEC.txt | head -10\necho \"=== SYN die/dead leit\"; grep -n 'leiþan\\|ga-leiþan' SYN.txt | head -5"
}
```


### [2026-09-06T23:19:21.966Z] TOOL RESULT

```
=== IEC leip
9595:leipos, à (?) (D dime’. Cf. WP II, 404 Skt. lepah, m. ‘smearing; ointment’; OCS and com. SI. lipa ‘limetree’; Li. liepa, Latv. liepa, id. (cf. dual sense of E lime ‘glue’ & "Inder"?
9596:leipos (?) (2) Sk. repah, adj. “base, cruel; répas, n. ‘stain’; Li. cf. leipstu, inf. leipti ‘grow numb, weaken, faint
9597:leipo ‘stick, be stuck, be left, remain, stop’ Tokh. lip- “be left; MHG liben, sv. 1. (w. dat: ‘spare’; (2) ‘be left); OFris. liva, sv. 1. ‘remain’ beside bi-liva, id. (= Du. blijven: G bleiben)
9887:liqutos “left, remaining’. Cf. liquos, etc. WP II, 396 Skt. riktáh “left; empty, destitute’; Arm. lik (*abandoned', but cf. liquos); Lat. cf. re-lictus “abandoned; remaining”; Gk. cf. apo-, ek-leip- téon “fit for leaving’; (the Gmc. forms OHG Iiban, bi-^; fir-leiben: OE læfan; and ON lifat (sic), pp. “left, remaining, fr. lifa, v. are am- biguous, perh. fr. *leip-, loip-, lip-, but cf. the phonol. of ‘seven, wolf); Li. liktas “left, remaining; likütis, usu. pl. liküciai ‘leavings, remains’. (Latv. likt ‘put; leave"; liktenis ‘fate’ is also ambig.)
9958:(loibhos ‘thin, slim’. See leibh-. E-gde in Cz. libovy ‘lean’; ambig. in Li. líebas ‘thin, slender'; o-gde in Li. láibas, id. A possible variant occurs in Du. leep ‘shrewd’; Fris. liep, id. beside Fris. leip ‘lanky one’, from a type *loib-. For Gk. loibé and Lat. libum, see sloib-)
=== IEC leit
7355:klitis, os, io ‘enclosure, cover’. Cf. kleitos (leist) & Kleit-, Klit- Gk. klísia ‘outbuildings’; OE bid. n. (cover, door, gate, vault, roof. In some senses pos- sibly fr. Klit-, q. v.); ON hlið ‘gate’; cf. OS
8939:(Kloios, us ‘closure, cover, shelter’. Cf. klai- with velar initial. Supt: K Li. šlajùs ‘leaning, sloping’; Slájus, m. *cot- tage’. For ON hlé, E lee, etc. see kleit-, klit- w. velar initial)
9612:leit- (1) “evil, sorrow, strife'. Cf. loitos. (Var- iant: lit-) k Gk. a-leíto ‘offend; sin; err’ beside a-litéo, id., a-litrós ‘wicked’; OHG līdan, sv. 1. (2) “suffer” beside ga-lidonti ‘calamitous, awful
9613:leit- (2) ‘go, creep, flow’. Cf. WP IL, 401. (Variant Hit-) Skt. cf. ritíh, f. ‘going; line’; Tokh. A let-, AB Dt. v. depart; Gk. cf. leiít-or, gs -oros ‘priest’; leit-ourgéo ‘serve in office’; Lat. cf. (?) satelles, -itis (attendant, fr. *sat-ed-lit-?); Go. af-leipan, sv 1. ‘depart’; OHG lidan, MHG liden, sv. 1. (1) ‘go, pass’; OE lióan, wd: ON líða, id.; OS fithan, id.
9895:Ät- (3) ‘go; going, gait, procedure’. Cf. Iit- (1). Variants: leit-, loit- Skt. cf. retum, inf. ‘release’; Gk. cf. (?) litós, adj. ‘praying’; lité, f. (prayer, to líssomai *pray?); (*ei- in) OE lian, sv. 1. ‘g0’; (*-oi- in
9904:Icel. leiða, v. 1ead^); (*-i- in), OE lióian *re- lease'; Icel. lið, n. “army”. (Isophonic: Skt. retum ‘melt, flow, drip’; Li. litis, ies, f. “wet or waterlogged place: *-ei-/-i-. See lit- (2) and leit- (2)
9905:ba, ið ‘touch, affect, hurt’. Cf. leit- (1), loi- tos Gk. cf. a-liteo, a-leíto, a-litaíno ‘offend; sin, err’; Ir. cf. líathaim (‘be dismayed’, fr. *leit-); W (ambig.) llid, m. ‘anger’; llidio, denom. vb. ‘enrage; be angry”, cf. er-lidio, v. (*persecute', fr. *per-Iit-); OHG Iidan sv. 1. ((2) ‘suffer’. For Ddan (1) ‘go’ see lit- and leit- (2)); (o-gde in MHG be-leidigen Cham, hurt: G ‘insult’; Li. lyCià, lytéti touch, concern? beside liečiù, Ji&sti, id. (fr. *leit-). WP cf. IL, 394 & 415
=== SYN die/dead leit
```


## [2026-09-06T23:19:29.814Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '11600,11660p' incoming/ARY/ARY_pages.txt"
}
```


### [2026-09-06T23:19:29.857Z] TOOL RESULT

```
۱ ۷828۸3 ,۷8880 5 بل78(/3/۸ ۱۲5
ایتالیایی (۷نمنتم5): ۰ ,۷۳۸8۸3 ,۷80 هتیت (77178/). ۷۷۳29۸ ,ات1088
رومانی (۸(/4(۷/): ,۷888۸5 ,۷8523
پرتغالی (۳0771701885): . اپسگشت‌ها رد ان

۷888۸3 ,۷8880 63 و۶
گوتیکك (0017110): زاد (اا ی( 4 (۲۵8۸۵) دی ان انا
ایسلندی کهن (مفا اه اجا نید صرم. 7 (۲0۱/۸1۸۵0) :۸۸25

00 119 لاه
ساکسونی کهن (54240(0 6۵2 ۷۵8۸0 :0100/8
فریزی کهن (#لفادل۲۸ صان): ۷۷۵ 7 (۳131۸0) ,1012 (۲۵73)
آلمانی کهن (08704۸2 انز صاه): 2 (۲۵83) :537
ای انا 2 (0(۸۵۸۵) :/0 0( هزم
آلمانی (0874(۷): لا نایدا برهان قاطع : ‎٩‏ و ۱۴۷۰
انگلیسی کهن (للقلاه/نق صام: ۷۷۵۸
بادداشت,
۱ واژه‌ی پارمی‌باستان ۳8۸1۸87۸8 (فرماندار) نیز از همین ريشه است.
۱ ۲ واژه‌ی فرمان 31881۸41 به زیان انگلیسی هم وارد شده و چم "دستور" و "اجازه" و حکم" را دارد.
۳ چم این واژه در زبان‌های رومانس و ژرمنی: سخن» واژه گفتار,
چم این واژه در زبان‌های اسلاوی کهن و روسی: سوگند.
چم این واژه در زبان لیتوانی و لثونی؛ فریاد زدن,
[pdf page 392]
فریفتن» فریب / ۳۹۳
پهلری (4(7ات۸: ۰ 3۸۴۵ ,83۳7۸۷ هلندی (7ع007): و1۴[
تخاری 4 (۸ (1۸4ل707): 1۳۰ اسلاوی کهن (12شا5 6[7نابل 00):
سانسکریت (84(/5777): رد8
8 مامتا 11۳۰ لینوانی (07۸2ل724/ل).

بونانی 870ق07): ۸ ,11808 1 ,138185 1.13۸78
لاتین (7100ا): 11۳۳5 لتونی (لتی) (7127بمل): 7 تالآ
گریکه (0077110): آلبانی (/(714له8ا4م):

۸1 ,811818۸0 ,لل8۸ق] بغقظتش] 1 ,138۸08
ایسلندی کهن (/(0104۵/نفت5 صا0): هنبت. (7177175): 71۳

وقاقلنا ,1813۸
ساکسونی کهن (54200(۷ 0ا0): 17 پسگشت‌ها کت تا
فریزی گهن (/۲/540 صا۵): 17 0 جطو0 ۶0
آلمانی کهن (052824۸21 ۷/04( ضا0): ی
8 اهنا ,181۳۸ ,181850 ,8118۸ 4 (38) ,603 (175).
آلمانی (08582۸): 25
,لت 8181880 7 (0865۳71100 ,0568775)
: انگلیسی کهن (30/-801 0ا0): :0۸/0/5
فا ,کل ,8513۴۸۵ 41 (12۸75) ,527 (178)
انگلیسی (84/.ا8۸0): 5 ,۴۴لا +7
دانمارکی 0۸84+ 8 1 5 (0.5) ,340 لته
۸ 2 سو ندی (81205): ۸ و1۴ برهان قاطع + ۱۴۸۴

نروژق ان 17 ۹

یادداشت: 1 ۰

۱- واژه‌ی انگلیسی 11۷13 نیز از همین واجربشه است: انگلیسی کهن: ۳.131۸۷ فریزی کهن: 1318۸ن1؛ ساکسونی

کهن: 11881۸3 هلندی: 1.2۷87 آلمانی کهن: 188500 ایسلندی کهن: 11۳۸ گوتبک: 128۸۷

۲ چم این واژه در زبان لاتین: دارای چشم تارء

چم این واژه در زبان‌های ژرمنی و زبان تخاری: ماندن» بجا ماندن؛ رفتن,
```


## [2026-09-06T23:19:51.077Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== WLD Bd2 leit\"; grep -n 'leit(h)\\|leith-\\|401' incoming/WLD/WLD_Bd2_pages.txt | head -10\necho \"=== WLD grep laidjan\"; grep -n 'laidian\\|laidō\\|leiþan\\|ga-leipan' incoming/WLD/WLD_Bd2_pages.txt | head -10"
}
```


### [2026-09-06T23:19:51.137Z] TOOL RESULT

```
=== WLD Bd2 leit
623:          37, 401) „feindselig gesinnt, iibel gesinnt^^ teils in aktiver Feindselig-
4065:595 f., Trautmann Apr. 392, 401; die bsl. Worte werden andrerseits, z. B.
10326:vr-a-tam „Gebot‘' u. dgl, s. Persson Wzerw. 20 A 7, Bgm. II ^        401   vgl,                    ;
16700:KZ. 37, 401j kaum mit Gutturalwechsel q:k hieher. Gbrigens konnte
22504:483 ala s-Pormen mit anguis usw. verbunden) s. z. B. Kluge 8, 401, Falk-
23198:rzee „wiehem" (W. Meyer KZ. 28, 175, Nehring IF. 4, 401           lit. rugoii „ubel-
24960:     Osthoff PBrB. 13, 401 ff. verbindet gr. XaQivog „gemastet, fett‘‘ als Haies-
26550:                                                    leit     leit(h)-                               401
26600:2. leit(h)- „fortgehu; sterben;                     gehn‘^
27114:zur Wzf. auf             s.          u.;    Hiibschmann Arm. Gr. I 453, Pedersen KZ. 39, 401),
=== WLD grep laidjan
```


## [2026-09-06T23:19:53.238Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== ARY lagad\"; grep -n 'لگد' incoming/ARY/ARY_pages.txt | head; echo \"--- latin index LAK\"; grep -n 'LAKATA\\|LAGAD\\|LAX ' incoming/ARY/ARY_latin_index_pages.txt | head\necho \"=== SKT leg/lizard\"; grep -n -o 'Leg, .\\{0,200\\}' SKT.txt | head -3; grep -n -o 'Lizard, .\\{0,200\\}' SKT.txt | head -3; grep -n -o 'Locust, .\\{0,200\\}' SKT.txt | head -3; grep -n -o 'Lobster, .\\{0,200\\}' SKT.txt | head -3"
}
```


### [2026-09-06T23:19:55.045Z] TOOL RESULT

```
=== ARY lagad
10068:و زبان‌های رومانس و ژرمنی چم آن ابتدا "لگد زدن" و "پاگذاردن روی چیزی" برده ولی امروزه (به ویژه در
--- latin index LAK
13204:LEZU, LEKT — (LATVIAN) (3) iy) LAX GREEK) gb
=== SKT leg/lizard
```


## [2026-09-06T23:20:01.064Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '26596,26625p' incoming/WLD/WLD_Bd2_pages.txt"
}
```


### [2026-09-06T23:20:01.122Z] TOOL RESULT

```
den‘‘ ist), wozu auch grm. "^laiiva- in anord. Ice „Schaden, Yernichtung'',
ahd. leives „leider‘^


2. leit(h)- „fortgehu; sterben;                     gehn‘^
   Av. ratd- „sterben“ (Praes. iridyeiti ) dazu nach Bezzenberger KZ. 22,
                                                                :



4S0, Bartholomae ZfdtWtf. 6, 231, 355 die germ. Sippe von got. -leipan
,,gehn‘', anord. lida st. Y, „gebn, vergehn, dahinschwinden, verlaafen, zu
Ende gehn, verscheidem', as. lithan st. Y. „gehn, wandern, fahren, befahren,
vergehn“, ags. lipan st. Y. ,.gehn, reisen^', ahd. lidan st. Y. „einen Weg
nehmen, gehn, fahren, weggehn, vergehn, verderben; erfahren, erleben,
leiden'', nhd. leiden (verschieden vom Subst, Leid. s.      „verabscheuen“)
anord. lid n. „Fahrzeug'', ags. lid n. „Fahrzeug, Schiff'‘; anord. leid f.
„Weg, Eichtang, Weise“, ags. lad f. Weg, Reise, Lebensunterhalt'', ahd.
lelta „Fuhrung, Leitung''; kaus. anord. leida „fuhren, geleiten, begleiten‘‘,
ags,    VMan, as. ledian „leiten, bringen“, ahd. leiitan, leiten „leiten, fahren,
                                                                                                               ;




402                                               leid-



mit sich tragen, haben“;                anord. lidinn                    Uidi      n. „Grabstatte“,         ahd.
```


## [2026-09-06T23:20:02.210Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '13190,13215p' incoming/ARY/ARY_latin_index_pages.txt\necho \"=== SKT\"; grep -n -i -o 'leg (1).\\{0,180\\}\\|lizard\\..\\{0,180\\}\\|locust\\..\\{0,180\\}\\|lobster\\..\\{0,180\\}' SKT.txt | head -8"
}
```


### [2026-09-06T23:20:04.726Z] TOOL RESULT

```
SKEAT: | (LAME) 327 poxor, ——SOS~*~S~S~«S
wey ¥ ys gb obey BARNHART: (LAME) 574

nagtirrh) gene Say BUCK: (LAME) 318-319

feet lool
wb yw ely IS, get edd ool leeds Sara plas! a ta ceeds ool WES" gael “1
thot (alt) aby slg te set zely se 2 bl! sly Jo cane ts
SE SBN 9 ssl UES 22 Slo cal ET
aka JF jeal st gon 9 Se Gal y srs suis 2 edly cal
eee em |
LAG (SWEDISH) 55 y LINK, LANK, LINGE :(KURDISH) 52,5
LEGG (NORWEGIAN) $33, LENGAY (AFGHANI) (54) 3!
Lakos LITHUANIAN) gy) RKSALA SANSKRIT) ey Suile
LEZU, LEKT — (LATVIAN) (3) iy) LAX GREEK) gb
LAGNO — (OLD PRUSSIAN) 95 3. LACERTUS LATIN) 3
(OLD SCANDINAVIAN) AS 54}
‘REFERENCES cata LEGGR
POKORNY? ””~”~”~™””” 63 | {MLDDLE LOW GERMAN) aes 339 3,glST
BARNHART: (LEG) 587 LECKEN
ONIONS: (LEG) 522 LOKEN (LOW GERMAN) «33,8 gst
SKEAT: (LEG) 335 LIRA (OLD ENGLISH) pS 58
vert ope Sad LEG ENGLISH) lS3i
ey ight oby LAG DANISH) lait
icntlook
I5R5oSY OY; 22 Slo cal
=== SKT
9100:lizard. (Span.  •■  W.  Indian.)  Span,  iguana.  Of Caribbean  origin.
10535:lizard.** L.  iUi,  he,  that ;  4l a  lizard.
10588:locust.
10589:locust.  It  was  perhaps  confused  with  Don, lofpe,  a  flea  (lit.  a  jumper),  as  though  /<?/• pestrt  meant  jumper ;  but  the  true  A.  S. form  of  '  leap*  is  nUdpan. liod
12257:lizard.  (£.)  The  ini- tial n  is  unoriginal ;  a  tuwi  stands  for  an twt,  M.  £.  nntfU ;  also  tvf/t,  which  is  a contraction  of  M.  E.  evete.  «  A.  S.  i/tta^  a liiard.
16398:lizard.  Of  Eastern origin;  cf.  Pen.  tamatuiar,  a  Balanuin- der.
16545:lizard.
23132:lobster.
```


## [2026-09-06T23:20:17.296Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i 'LACERTUS\\|LEGGR\\|RKSALA' incoming/ARY/ARY_pages.txt | head -10"
}
```


### [2026-09-06T23:20:17.347Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T23:20:27.954Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '10580,10595p' SKT.txt; echo \"-----\"; sed -n '23125,23140p' SKT.txt; echo \"----- leg\"; grep -n -i -o 'Leg,.\\{0,250\\}' SKT.txt | head -4"
}
```


### [2026-09-06T23:20:29.508Z] TOOL RESULT

```
LOFT.
255
From  pp.  of  L.  duiM^rt,  to  pot  out  of
place.
lieu,  place,  stead.  (.T.-L.)  F. /r>w.- L.  locum,  acc  of  locus,  a  place,
lieutenant,  a  'locum  tenens,*  deputy, Sec  (F.  —  L.)  F.  lieu  tenant. ^L.  locum' tencnt;  stem  of  locum  tetirns.  one  who hold's  another's  place.  —  L.  locum,  acc of  loius.  a  place  ;  /eMctu,  pies.  pt.  of  tenen, to  bold.
local:  (F.  -  L.)  F.  local,  -  L.  tocalis, belonging  to  a  place.  — L.  lorm,  a  place.
locate,  to  place.  (L.)  From  pp.  of  L. locare,  to  place.  — L.  locus.
looomotioo.  motion  from  place  to place.  (L.)  Coined  from  loco-,  crude  fojiD of  locus,  a  place  ;  and  motion, IiOCUSt,  a  winged  insecL  (L.)  M,  K. locujti.  —  L.  lacuita,  a  &hcll-li&h,  also  a locust.
lobster,  a  kind  of  shcU-6&h.  (L.)  A.S. hpfistrt,  3  corrupter  t'oira  ol  A.S,  lo/>ujt, a  corruption  of  L.  locusta,  <i)  a  lobster,  (2) a  locust.  It  was  perhaps  confused  with  Don, lofpe,  a  flea  (lit.  a  jumper),  as  though  /<?/• pestrt  meant  jumper ;  but  the  true  A.  S. form  of  '  leap*  is  nUdpan. liode,  a  vein  of  ore,  a  water-course.  (E.) The  true  mum  is  *  couree.'  A.  S.  hid,  a way,  course,  journey.  —  AS.  /JO,  pt.  t.  of Ux^am,  to  travel,  go.^-IceL  Ui^,  lode,  way, course,  from  //^a,  to  go ;  Swed.  ltd,  a C0Qr«.  (Base  LITU.)  Dor.  lode  ■  star (bclow\    ^  And  m.'i:  load,  p.  a.^O,  col.  l.
lead  (1),  to  coDduct  (E.)  M.  E.  Udcu, pL  t  laddt,  pp.  ;^.- A.  S.  lAdan,  to  lead. —  A.  S.  Idd,  a  course,  way  (abovcK  -f-  Icel. Ui^,  from  UiiS ;  Su  cd.  UdOf  from  Ud ;  G. Iciten,  Du.  leidcn.
lodeatar,  loadstar,  the  polar  star. (E.)  Lit.  'way-slar,'  fctor  that  guides;  see Lode  above.
lodestone,  loadstone,  a  magnet.  (E.; Compounded  of  lale  and  stotte^  in  iroitatinn of  lodestar',  it  should  rather  have  been lead-stone^  since  it  means  a  stone  that  leads or  draws,  not  a  stone  to  guide. Iiodge :  see  Xieaf.
IfOft^  an  upi>er  room.  (Scand.)  M.  E. loft,  properly  *  air ; '  the  peculiar  sense  is Scaod.  — IccL /p// (pron  loft),  tO  air,  sky, (2)  an  Dp])er  room:  Don.  Swed.  toft,  a garret.  Allied  to  A-  S.  lyft,  air.  sky,  G'  th. luftM.  Du.  hu'ht  I. for  luft  •\  G.  luft.  the  air.
aloft,  in  the  air.  iScand.)  IceV  d  lot/ (pron.  lAft^.  aloft,  in  the  air.  H«k  v«^ J- « IceL  <^  «  A.  S,  MS,  m.
I
-----
load— lade  (I).
paddle  (i) — patter.            ^^^|
I)— whole.
lobby — lodge.
paddle
(a) — spatula.          ^^^H
tr  (J)— hanaper.
locust — lobster.
paddoc
k  (2)— park.           ^^M
[ve — ling,  Tank  (i).
lone — alone.
p.-iin,  v6. — pine  (i).           ^^^M
thatch  ^3).
paladin — palatine.            ^^^^|
jy— oboe.
----- leg
7376:leg,  also  a  jamb  (see  Cotgn See  Gambol.
17376:leg,    cognate   with    E.
```


## [2026-09-06T23:20:38.927Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in 7502f7141ec1eb93 5cdb7745fcd8f314 5dc557f8f2a8e707 cd1f2717df1b062f 94c7c8960dbf2e96; do echo \"###### $f\"; head -4 $f.txt; sed -n '1,200p' $f.txt | grep -n -m2 -A3 'Old Norse\\|from Latin\\|Proto-Germanic' | head -20; done"
}
```


### [2026-09-06T23:20:40.378Z] TOOL RESULT

```
###### 7502f7141ec1eb93
URL: https://www.etymonline.com/word/leg
FETCHED: 2026-09-06T23:14:32Z
STATUS: 200
TITLE: Leg - Etymology, Origin & Meaning
25: late 13c., from a Scandinavian source, probably Old Norse leggr "a leg, bone of the arm or leg," from Proto-Germanic *lagjaz (cognates Danish læg , Swedish läg "the calf of the leg"), a word with no certain ulterior connections. Perhaps from a PIE root meaning "to bend" [Buck]. For Old Norse senses, compare Bein , the German word for "leg," in Old High German "bone, leg" (see bone (n.)). Replaced Old English shank (n.), itself also perhaps from a root meaning "crooked."
26-
27- Distinguished from an arm, leg, or fin in being used for support. Of triangle sides from 1650s (translating Greek skelos , literally "leg"). Extended to furniture supports from 1670s. Meaning "part of pants which cover the leg" is from 1570s. By 1870s as an adjective it had a salacious suggestion of artistic displays focused on the female form, such as leg-piece in theater jargon, leg-business as slang for "ballet."
28-
--
41: Middle English bon , from Old English ban "bone, tusk, hard animal tissue forming the substance of the skeleton; one of the parts which make up the skeleton," from Proto-Germanic *bainan (source also of Old Frisian and Old Saxon ben , Old Norse bein , Danish ben , German Bein ). Absent in Gothic, with no cognates outside Germanic (the common PIE root is *ost- ); the Norse, Dutch, and German cognates also mean "shank of the leg," and this is the main meaning in Modern German, but English seems never to have had this sense.
42-
43- To work (one's) fingers to the bone is from 1809. To have a bone to pick (1560s) is an image of a dog struggling to crack or gnaw a bone (to pick a bone "strip a bone by picking or gnawing" is attested from late 15c.); to be a bone of contention (1560s) is of two dogs fighting over a bone; the images seem to have become somewhat merged. Also compare bones .
44-
###### 5cdb7745fcd8f314
URL: https://www.etymonline.com/word/lizard
FETCHED: 2026-09-06T23:14:32Z
STATUS: 200
TITLE: Lizard - Etymology, Origin & Meaning
25: "an animal resembling a serpent, with legs added to it" [Johnson], late 14c., lusarde , from Anglo-French lusard , Old French laisarde "lizard" (Modern French lézard ), from Latin lacertus (fem. lacerta ) "lizard," a word of unknown origin. The ending in French and English is probably influenced by words in -ard .
26-
27- It is identical to Latin lacertum "upper arm, muscular part of the arm, from the shoulder to the elbow" (opposed to bracchium ), which suggests a pattern similar to that of Latin musculus "a muscle," literally "little mouse" (diminutive of mus "mouse"), so called because the shape and movement of the biceps were thought to resemble mice. It is unclear which Latin sense, the arm-muscle or the lizard, is original. De Vaan finds the words perhaps connected to Greek likertizein "to jump, dance," which Beekes finds likely from Pre-Greek.
28-
--
36: 1560s, "large carnivorous reptile of the Americas," lagarto , aligarto , a corruption of Spanish el lagarto (de Indias) "the lizard (of the Indies)," from Latin lacertus (see lizard ), with Spanish definite article el , from Latin ille (see le ).
37-
38- The modern form of the English word is attested from 1620s, with unetymological -r as in tater , feller , etc. ( Alligarter was an early variant) and an overall Latin appearance. The slang meaning "non-playing devotee of swing music" is attested from 1936; the phrase see you later, alligator is from a 1956 song title.
39-
###### 5dc557f8f2a8e707
URL: https://www.etymonline.com/word/locust
FETCHED: 2026-09-06T23:14:33Z
STATUS: 200
TITLE: Locust - Etymology, Origin & Meaning
25: "grasshopper, large orthopterous insect noted for mass migrations accompanied by destructive ravages of vegetation," early 14c., borrowed earlier in Old French form languste (c. 1200), from Latin locusta "locust; lobster" (see lobster ).
26-
27- In the Hebrew Bible there are nine different names for the insect or for particular species or varieties; in the English Bible they are rendered sometimes 'locust,' sometimes 'beetle,' 'grasshopper,' 'caterpillar,' 'palmerworm,' etc. The precise application of several names is unknown. [OED, 1989]
28- also from early 14c. 
--
79: Old English treo, treow "tree" (also "timber, wood, beam, log, stake"), from Proto-Germanic *trewam (source also of Old Frisian tre, Old Saxon trio, Old Norse tre, Gothic triu "tree"), from PIE *drew-o-, suffixed variant form of root *deru- "be firm, solid, steadfast," with speci
80-
81- wood 
82-
###### cd1f2717df1b062f
URL: https://www.etymonline.com/word/lobster
FETCHED: 2026-09-06T23:14:33Z
STATUS: 200
TITLE: Lobster - Etymology, Origin & Meaning
47: "grasshopper, large orthopterous insect noted for mass migrations accompanied by destructive ravages of vegetation," early 14c., borrowed earlier in Old French form languste (c. 1200), from Latin locusta "locust; lobster" (see lobster ).
48-
49- In the Hebrew Bible there are nine different names for the insect or for particular species or varieties; in the English Bible they are rendered sometimes 'locust,' sometimes 'beetle,' 'grasshopper,' 'caterpillar,' 'palmerworm,' etc. The precise application of several names is unknown. [OED, 1989]
50-
--
53: Old English -istre , from Proto-Germanic *-istrijon , feminine agent suffix used as the equivalent of masculine -ere (see -er (1)). Also used in Middle English to form nouns of action (meaning "a person who ...") without regard for gender.
54-
55- The genderless agent noun use apparently was a broader application of the original feminine suffix, beginning in the north of England, but linguists disagree over whether this indicates female domination of weaving and baking trades, as represented in surnames such as Webster , Baxter , Brewster , etc. (though modern spinster probably carries an originally female ending). For Dempster , see deem (v.).
56-
###### 94c7c8960dbf2e96
URL: https://www.etymonline.com/word/life
FETCHED: 2026-09-06T23:14:34Z
STATUS: 200
TITLE: Life - Etymology, Origin & Meaning
58: Old English life (dative lif ) "animated corporeal existence; lifetime, period between birth and death; the history of an individual from birth to death, written account of a person's life; way of life (good or bad); condition of being a living thing, opposite of death; spiritual existence imparted by God, through Christ, to the believer," from Proto-Germanic *leiban (source also of Old Norse lif "life, body," Old Frisian, Old Saxon lif "life, person, body," Dutch lijf "body," Old High German lib "life," German Leib "body"), properly "continuance, perseverance," reconstructed in Watkins to be from PIE root *leip- "to stick, adhere."
59-
60- The transition toward 'live', etc. is only Gmc. and disputed, but semantically comprehensible: stick → remain (also Tocharian) → live (Gmc.). [Boutkan]
61-
--
94: Middle English liven , from Old English lifian (Anglian), libban (West Saxon) "to be, be alive, have life; continue in life; to experience," also "to supply oneself with food, procure a means of subsistence; pass life in a specified fashion," from Proto-Germanic *libejanan (source also of Old Norse lifa "to be left; to live; to live on," of fire, "to burn;" Old Frisian libba , German leben , Gothic liban "to live"), from PIE root *leip- "to stick, adhere," forming words meaning "to remain, continue."
95-
96- Meaning "to make a residence, dwell" is from c. 1200. Meaning "express in one's life" ( live a lie ) is from 1540s. Intensified sense "have life abundantly, make full use of life's opportunities" is from c. 1600. Related: Lived ; living .
97-
```


## [2026-09-06T23:21:37.708Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== WLD Bd2 leip\"; grep -n '1. leip-\\|leip- „mit\\|leip-  „' incoming/WLD/WLD_Bd2_pages.txt | head -5\necho \"=== WLD Bd2 lek\"; grep -n 'lek- „\\|2. lek-\\|leq- „' incoming/WLD/WLD_Bd2_pages.txt | head -5\necho \"=== LEW lacerta\"; grep -n -o 'lacerta.\\{0,180\\}' LEW_1910.txt | head -4; echo \"--- LEW locusta\"; grep -n -o 'locusta.\\{0,180\\}' LEW_1910.txt | head -4"
}
```


### [2026-09-06T23:21:39.246Z] TOOL RESULT

```
=== WLD Bd2 leip
26687:1. leip- „init Fett beschmieren, Fett. klebrige Masse; kleben, klebenbleiben“
=== WLD Bd2 lek
6446:plek- „flechten, zswickeln", vermutlich Weiterbildung von pel- „falten".
26223:(: lit. Ukti „fliegen" usw., s. 6’Z-, oleq- „biegen") sei, ist aber sehr erwagens-
27880:        Avahrscheinlich alte Spezialisierungen von leq- „biegen“; vgl. zur Bed.
37465:Xiog^ langob. lagi „Schenkel** leq- „biegen     GliedmaBen** auch angereiht
40027:skleq-, s£leq- „na6, spritzen, sprengen“?
=== LEW lacerta
--- LEW locusta
```


## [2026-09-06T23:21:39.803Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LAT lacerta\"; grep -n -o 'lacerta.\\{0,200\\}' LAT.txt | head -4\necho \"=== CHEUNG lagad\"; grep -n -i 'lagad' CHEUNG.txt | head -5\necho \"=== HUB rew/fireften\"; grep -n -o '643\\..\\{0,150\\}\\|829\\..\\{0,150\\}' HUB.txt | head -6"
}
```


### [2026-09-06T23:21:41.325Z] TOOL RESULT

```
=== LAT lacerta
31783:lacerta, -ae f. ; lacertus, -I f. (les deux formes sont egalement
31787:lacerta
=== CHEUNG lagad
=== HUB rew/fireften
3010:829. Anders Mann ZDMG. 47, 705. Ich stehe auf Horn's
9401:829.
```


## [2026-09-06T23:21:49.723Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LAT lacerta\"; sed -n '31783,31800p' LAT.txt\necho \"=== HUB ctx\"; sed -n '3000,3020p' HUB.txt"
}
```


### [2026-09-06T23:21:49.778Z] TOOL RESULT

```
=== LAT lacerta
lacerta, -ae f. ; lacertus, -I f. (les deux formes sont egalement
attestees, comme en gr.ouupa et craupoc;) : i*lezard; a* poisson inde-
termine glose xpa^oupoC, saurel? Atteste depuis Cic., M.L.4821.
V. lacertus.
lacertus, -J m.(surtout usite au pl. lacerti; n. collectif lacerta
dans Acc., d 1 ou lacertum, Gloss.): muscles du bras superieur, par
opposition a bracchium: subiecta lacertis bracchia sunt, Ov., M.14,304;
par extension "muscles de 1'epaule" et "muscles" en general, "force
musculaire"; en poesie "bras". Semble le meme mot que lacertus "le-
zard"; cf. [iuS en grec et le rapport mus: musculus. Ancien (Lucii.),
class. M.L.48gia et 4833. Iri. laghairt.
Derives: lacertulus (Apul.)j lacertosus (et lacertuosus, d'apros
neruSsus).
Aucun rapprocbement sur.
lachanizS, - 5 s: synonyme vulgaire de languere (cf. Suet.Aug.87),
fait sur le gr. Xa)(avov "l< 5 gume", d'apres betizo (v. ce mot).
lacinia, -ae f.: a designe d'abord un flocon de laine qui n'est
pas tortilia en forme de frange [fimbria), mais qui reste en touffe.
=== HUB ctx
setzen. Nur ein zd. *frahy& = ap. *frahy(l (als nom.
sg. masc.) wurde paz. freh = np. firih genau ent-
sprechen.
828. Nach N old eke bedeutet np. farydd ursprunglich
nur 'Geschrei* und erst secundar *Hilfe*; vgl. gr. lio^
und lioTjd^oog (np. faryod^ras)^ fioiid^siv. Die Bedeutung
'Hilfe' belegt Horn aus Abu Muwaffaq, sie findet
sich auch schon Min. cap. 2, 166 (o friyOS ne rased
*kommt nicht zu Hilfe', phi. frayOt Phi. Min. p. 16,
Z. 5).
829. Anders Mann ZDMG. 47, 705. Ich stehe auf Horn's
Seite, vgl. meine Etym. und Lautl. der osset. Spr.
Xr. 271.
834. Zum Suffix -zar in hdrzdr == phi. kdrJcar (so kann
doch ohne Weiteres gelesen werden, wie auch karJjar
oder kanzdr) = paz. karlzdr Min. Gl. 121 vgL Dar-
mesteter, Etud. iran. I, p. 296. — Xp. kOrcan =
paz. kdravdn Shk. 253 hat nach Ausweis von arm.
LW. karavan 'Earavane, Heerhaufen (bei Elise, Fau-
stus etc.) im Phi. karavan oder karuran (geschrieben
karupdn) gelautet, kann also nicht so erklart werden
```


## [2026-09-06T23:21:52.110Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read().split('\\n')\n# find nearest standalone page number lines around 26687 and 37465\nimport re\nfor target in (26687,37465):\n    nums=[]\n    for i in range(target-80,target+80):\n        m=re.match(r\"^\\s*(\\d{3})\\s*$|^(\\d{3})\\s+[A-Za-zÄÖÜäöü]\",t[i].strip()) if 0<=i<len(t) else None\n        if m: nums.append((i,t[i].strip()[:40]))\n    print(target, nums[:8])\nEOF"
}
```


### [2026-09-06T23:21:53.929Z] TOOL RESULT

```
26687 [(26620, '402                                     '), (26751, '404                                     ')]
37465 [(37421, '564                                     ')]
```


## [2026-09-06T23:22:07.990Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== WLD Bd1 lek\"; grep -n 'lek-\\|leq- „\\|2. leq' incoming/WLD/WLD_Bd1_pages.txt | head -8\necho \"=== BRT 1480\"; grep -n 'raeS-\\|raed-\\|iri&-\\|iriO-\\|iriS-' BRT.txt | head -8"
}
```


### [2026-09-06T23:22:08.064Z] TOOL RESULT

```
=== WLD Bd1 lek
7401:  Ahnlieh *alek- „abwehren, schiitzcn"                    (s.       d.) und *areg- in ai. argala-li       ,
7895: *alek-, Anm. 1), lat. altus „hoch“ (d. i. „groBgewachsen“), mir. alt „Hohe; Ufer,
8104:                                                al-    — alek-                                         89
8166:alek- „abwehren, schiitzen“, vermutlieh eigentlich „abschlieBen und dadurch
10239:als gegen den Vokalismus wenigstens letztere kaum zwingend), PI. kollek-
10302:jelinn sei (s. lek- „sprechen“).   gyavev   elnev Hes. mit Augment g- zu
14599:trotz     Persson Beitr. 151                             aus Hecinus ,             \Vz. *lek-,             bei                   der auch hy.oiqk
30506:                                                qleiq-   — nlek-                  321
=== BRT 1480
10572:•  g.  (,  j.)  xraod-  V,  '(sich)  ängstigen', Praes.   i  xraed-,
23923:pat-,  va(y)-,  'raed-,  stj-  usw.).  snathisa  "mantim  :^arfm  jairtti  Y.57, 10;
25473:•  j,  iriS-ya^s'tät-  f.  'Sterben,  Tod':  ya^a yat  . .  visps  atahul  astvS  . .  til  pairi  'iätai haraite  "dass  die  ganze  Menschheit,  wenn sie  .  .,  sich  vom  Sterben  retten  kann" Y.  ig,  I  o  ''.
25542:*urusday-  f.,  zum  V.  iraed-;  %  S3  !■  7-  —  ^■'■
27196:•  j.  sraeS-  V.  '(sich)  heften',  Praes.  3 trUa;  17  (Fut)  srai^a-.  —  Absol.  sral- iyäntim.
```


## [2026-09-06T23:22:26.238Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/leyp-\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/leyt-\" \"https://en.wiktionary.org/wiki/leg\"; do python3 tools/fetch_source.py \"$u\" --note \"page 308: PIE roots Leip/Leith and English leg\"; done\ncd data/verification/sources/web\nfor f in $(tail -3 index.jsonl | python3 -c \"import sys,json;[print(json.loads(l)['file'].split('/')[-1][:-4]) for l in sys.stdin]\"); do echo \"#### $f\"; grep -n -m2 -B1 -A3 'Root\\|Etymology' $f.txt | head -20; done"
}
```


### [2026-09-06T23:22:29.078Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/249bec2c6995a437.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0fd20f27e0063050.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/221e7c08686cd902.txt
#### 249bec2c6995a437
61- 1.1 
62: Etymology 
63-
64- 1.2 
65: Root 
66-
67- 1.2.1 
68- Derived terms 
#### 0fd20f27e0063050
#### 221e7c08686cd902
61- 1.1 
62: Etymology 1 
63-
64- 1.1.1 
65- Pronunciation 
--
97- 1.2 
98: Etymology 2 
99-
100- 1.2.1 
101- Noun
```


## [2026-09-06T23:22:31.921Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"=== leyp-\"; sed -n '80,140p' 249bec2c6995a437.txt | grep -v '^\\s*$' | head -30\necho \"=== leyt-\"; head -8 0fd20f27e0063050.txt; sed -n '50,120p' 0fd20f27e0063050.txt | grep -v '^\\s*$' | head -20"
}
```


### [2026-09-06T23:22:33.585Z] TOOL RESULT

```
=== leyp-
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
=== leyt-
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/leyt-
FETCHED: 2026-09-06T23:22:28Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found
```


## [2026-09-06T23:22:37.253Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\ngrep -n -A6 'Proto-Indo-European' 249bec2c6995a437.txt | sed -n '1,60p' | grep -v '^\\s*--\\s*$' | head -40"
}
```


### [2026-09-06T23:22:38.908Z] TOOL RESULT

```
1:URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/leyp-
2-FETCHED: 2026-09-06T23:22:27Z
3-STATUS: 200
4:TITLE: Reconstruction:Proto-Indo-European/leyp- - Wiktionary, the free dictionary
5-
6:Reconstruction:Proto-Indo-European/leyp- - Wiktionary, the free dictionary 
7-
8- Jump to content 
9-
10- Main menu 
11-
12- Main menu
57: Proto-Indo-European 
58-
59: Toggle Proto-Indo-European subsection 
60-
61- 1.1 
62- Etymology 
63-
64- 1.2 
65- Root 
78: Reconstruction:Proto-Indo-European/ leyp- 
79-
80- Add languages 
81-
82- Reconstruction 
83-
84- Discussion 
132: This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.
133-
134: Proto-Indo-European
135- [ edit ] 
136-
137- Etymology
138- [ edit ] 
139-
140- Often supposed to be an extension of *ley-, *(s)ley- ( “ to slip, slide, glide; slimy ” ) .
154: Terms derived from the Proto-Indo-European root *leyp- (35 c, 0 e) 
155-
156- *léyp-os ~ *léyp-es-os [ 1 ]
```


## [2026-09-06T23:22:41.317Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nsed -n '140,175p' 249bec2c6995a437.txt | grep -v '^\\s*$'"
}
```


### [2026-09-06T23:22:42.914Z] TOOL RESULT

```
 Often supposed to be an extension of *ley-, *(s)ley- ( “ to slip, slide, glide; slimy ” ) .
 Root
 [ edit ] 
 *leyp- [ 1 ] [ 2 ] [ 3 ] 
 to stick 
 fat or sticky substance 
 Derived terms
 [ edit ] 
 Terms derived from the Proto-Indo-European root *leyp- (35 c, 0 e) 
 *léyp-os ~ *léyp-es-os [ 1 ] 
 Proto-Indo-Iranian: *ráypas 
 Proto-Indo-Aryan: *ráypas 
 Sanskrit: रेपस् ( répas , “ dirty spot, stain ” ) 
 *leyp-ó-m [ 1 ] 
 > ? Proto-Germanic: *lībą ( see there for further descendants )
 *li-né-p-ti ~ *li-m-p-énti ( nasal-infix present ) 
 Proto-Indo-Iranian: *limpáti 
 Proto-Indo-Aryan: *limpáti 
 Sanskrit: लिम्पति ( limpáti , “ to smear, pollute ” ) ( see there for further descendants )
 *lip-yé-ti ( yé-present ) 
 > ? Proto-Germanic: *libjaną ( “ to live, be alive ” ) ( see there for further descendants )
 *loyp-éye-ti ( causative ) 
 Proto-Balto-Slavic: *laip- 
 Eastern Baltic:
 Lithuanian: lipi̇̀nti , láipioti
```


## [2026-09-06T23:22:52.714Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; grep -n -c 'Persian' 5653ce2c75428577.txt; grep -n -m5 'Persian\\|Noun\\|deceit' 5653ce2c75428577.txt | head"
}
```


### [2026-09-06T23:22:52.773Z] TOOL RESULT

```
12
57: Persian 
59: Toggle Persian subsection 
65: Noun 
131: Persian
137: ( Classical Persian ) IPA ( key ) : /ˈreːw/
```


## [2026-09-06T23:22:55.180Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; sed -n '131,160p' 5653ce2c75428577.txt | grep -v '^\\s*$'"
}
```


### [2026-09-06T23:22:57.264Z] TOOL RESULT

```
 Persian
 [ edit ] 
 Pronunciation
 [ edit ] 
 ( Classical Persian ) IPA ( key ) : /ˈreːw/ 
 ( Dari, formal ) IPA ( key ) : [reːw] 
 ( Dari, formal ) IPA ( key ) : [reːw] 
 ( Kabuli ) IPA ( key ) : [reːw] 
 ( Hazaragi ) IPA ( key ) : [reːw] 
 ( Iran, formal ) IPA ( key ) : [ɹiːv] 
 ( Tajik, formal ) IPA ( key ) : [ɾew] 
 Rhymes: -eːw 
 Readings
 Classical reading ? 
 rēw
 Dari reading ? 
 rēw
```


## [2026-09-06T23:23:00.596Z] AGENT

Now I'll write the verification file.


## [2026-09-06T23:33:14.658Z] TOOL CALL #81: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk308.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW_LEYP = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/leyp-\"\nW_FARIFTAN = \"https://en.wiktionary.org/wiki/%D9%81%D8%B1%DB%8C%D9%81%D8%AA%D9%86\"\nW_FARIB = \"https://en.wiktionary.org/wiki/%D9%81%D8%B1%DB%8C%D8%A8\"\nW_RIV = \"https://en.wiktionary.org/wiki/%D8%B1%DB%8C%D9%88\"\nW_RASTAXIZ = \"https://en.wiktionary.org/wiki/%D8%B1%D8%B3%D8%AA%D8%A7%D8%AE%DB%8C%D8%B2\"\nW_LAGAD = \"https://en.wiktionary.org/wiki/%D9%84%DA%AF%D8%AF\"\nW_LEG = \"https://en.wiktionary.org/wiki/leg\"\nE_LEG = \"https://www.etymonline.com/word/leg\"\nE_LIZARD = \"https://www.etymonline.com/word/lizard\"\nE_LOCUST = \"https://www.etymonline.com/word/locust\"\nE_LOBSTER = \"https://www.etymonline.com/word/lobster\"\nE_LIFE = \"https://www.etymonline.com/word/life\"\nA_FARIB = \"https://abadis.ir/fatofa/%D9%81%D8%B1%DB%8C%D8%A8/\"\nA_LAGAD = \"https://abadis.ir/fatofa/%D9%84%DA%AF%D8%AF/\"\nA_RIV = \"https://abadis.ir/fatofa/%D8%B1%DB%8C%D9%88/\"\n\ndata = {\n \"pdf_page\": 308,\n \"book_page\": 278,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-06\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Leip\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *leyp- 'to smear with fat/grease, stick, cling' (Pokorny 1. leip- 670 f.; Watkins/AHD leip- 'to stick, adhere; fat')\",\n   \"note\": \"Pokorny 670 f. prints '1. leip- ‚mit Fett beschmieren, kleben‘ (daraus auch ‚sich anheftend hinaufklettern‘); wohl Erweiterung zu lei- ‚schleimig‘' — exactly the root, language label and (approximately) the gloss Nourai gives. Nourai's 'cover, preserve' is a loose rendering: 'preserve' reflects only the Germanic specialisation 'remain, be left over' (Goth. bileiban, OE lǣfan), not the PIE meaning. The one substantive problem on this chart is the Persian node: Pokorny and Horn do put NP firēftan/fīrēb here, but Nyberg 1974 and Cheung 2007 derive them instead from *fra-dab (PIE *dʰebʰ-); see node 2.\",\n   \"note_fa\": \"ریشهٔ هندواروپایی آغازین *leyp- به معنای «به چربی اندودن، چسبیدن» است که پوکورنی در صفحهٔ ۶۷۰ و واتکینز (پیوست ریشه‌های هندواروپایی) همین معنا را می‌دهند؛ پس نام ریشه، زبان و معنای آن درست است. افزودن «پوشاندن، نگاه داشتن» در معنای ریشه دقیق نیست؛ معنای «بر جای ماندن» ویژهٔ شاخهٔ ژرمنی است. ادعای نورایی دربارهٔ خود ریشه درست است، امّا دربارهٔ پیوند فارسی با آن اختلاف هست (نگاه کنید به گرهٔ ۲).\",\n   \"sources\": [W_LEYP, E_LIFE],\n   \"ref_check\": [\n    {\"ref\": \"POK:670\", \"status\": \"supports\", \"note\": \"POK_02.txt line 5242 (Pokorny p.670): '1. leip- ‚mit Fett beschmieren, kleben‘ (daraus auch ‚sich anheftend hinaufklettern, klettern‘); wohl Erweiterung zu lei- ‚schleimig‘' — the page also lists 'nipers. fi-reftan ‚betrügen‘, rew ‚Betrug‘', i.e. Pokorny himself puts the Persian words here.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. II p.403 (WLD_Bd2_pages.txt line 26687, between page marks 402 and 404)\", \"stance\": \"supports\", \"note\": \"'1. leip- ‚mit Fett beschmieren, Fett, klebrige Masse; kleben, klebenbleiben‘' — Walde-Pokorny's original article that Pokorny 670 abridges.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. leip- (AHD_watkins1985.txt line 671)\", \"stance\": \"supports\", \"note\": \"'leip-. To stick, adhere; fat. 1. Germanic *libam in Old English lif, life (< “continuance”): LIFE, LIVELY ... [Pok. leip- 670.]'\"},\n    {\"src\": \"IEC\", \"where\": \"Mann s.v. leipo (IEC.txt line 9597)\", \"stance\": \"supports\", \"note\": \"'leipo “stick, be stuck, be left, remain, stop” Tokh. lip- “be left”; MHG liben ... OFris. liva “remain”'.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Sanskrit\", \"words\": \"rěp; pra-rěp\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Skt. rip- / rep- / lep- 'to smear, stick; to cheat, deceive' is the regular Indo-Aryan continuant of PIE *leyp- (Indo-Iranian shows the usual l/r fluctuation, so lip- ~ rip-). Pokorny 670 lists 'ai. lip- (limpáti, lipyáte) ‚beschmieren‘ ... rip- ‚schmieren, kleben, betrügen‘; rip- f. ‚Betrug; Verunreinigung‘ ... ripú ‚tückisch, Betrüger‘'. The semantic bridge 'smear' > 'besmirch, cheat' is the same as in Lat. lippus / Gk. liparós. Nourai's 'pra-rěp' is the preverbed pra-rip- 'to smear over, cover; to deceive', which is precisely the form Horn (no. 829) cites as the base of NP firēftan ('ai. pra + √rep- ‚anschmieren, betrügen“'). Both words and the arrow from the root are sound; the vowel Nourai writes (ě) reflects the guna grade rep-.\",\n     \"derivation_fa\": \"سنسکریت rip-/rep-/lep- به معنای «اندودن، چسباندن» و از همین راه «فریفتن، فریب دادن»، دنبالهٔ منظم ریشهٔ هندواروپایی *leyp- است؛ در هندوایرانی ابدال l/r معمول است (lip- ـ rip-). تحول معنایی «اندودن ← آلودن ← فریفتن» در لاتین lippus و یونانی liparós نیز دیده می‌شود. صورت pra-rip- (با پیشوند pra-) همان است که هرن در شمارهٔ ۸۲۹ پایهٔ «فریفتن» دانسته است. ادعای نورایی در این گره درست است.\",\n     \"sources\": [W_LEYP],\n     \"ref_check\": [\n      {\"ref\": \"BQT:991\", \"status\": \"supports\", \"note\": \"Borhan-e Qate' vol. 2, entry ریو, Mo'in's footnote (BQT_v2_pages.txt \\\\f-leaf 453; our leaf mapping makes that printed p.993, Nourai cites 991 — the OCR leaf count drifts by ~2 here): 'هندی باستان rip- (حیله) (از ریپ rep-, lep- ... گول زدن) ق: فریفتن.' — exactly Nourai's Sanskrit forms and his link to فریفتن.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"p.670 (POK_02.txt line 5243)\", \"stance\": \"supports\", \"note\": \"'Ai. lip- ... rip- ‚schmieren, kleben, betrügen‘; rip- f. ‚Betrug; Verunreinigung‘ ... ripú ‚tückisch, Betrüger‘'.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"EDIV s.v. *raip ? 'to smear', p.308 (CHEUNG.txt line 20267)\", \"stance\": \"supports\", \"note\": \"'*SANSKRIT: rep, lep “to smear, attach” (RV) = EWAia II: 460 ... «PIE *leip- “to stick, be sticky” — LIV: 405 f. | Pok.: 670 f.' (Cheung accepts the Sanskrit forms under this root; he rejects only the Iranian ones — see node 2).\"},\n      {\"src\": \"IEC\", \"where\": \"Mann s.v. leipos (IEC.txt lines 9595-9596)\", \"stance\": \"supports\", \"note\": \"'Skt. lepah, m. “smearing; ointment” ... Sk. repah, adj. “base, cruel”; répas, n. “stain”'.\"},\n      {\"src\": \"HRN\", \"where\": \"no. 829, p.184 (HRN.txt \\\\f-leaf 206)\", \"stance\": \"supports\", \"note\": \"'ai. pra + √rep- ‚anschmieren, betrügen‘, vergl. rip- ‚Betrug‘, ripú- ‚Betrüger‘' — Horn's exact source for Nourai's pra-rěp.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Persian\", \"words\": \"farîb; farîftan; rîv\", \"verdict\": \"disputed\",\n     \"derivation\": \"Nourai follows Horn (nos. 643 and 829) and Pokorny 670, who derive NP فریفتن farēftan / present stem فریب farēb from Old Iranian *fra- + *raip- (= Skt. pra-rip-), MP frēftan / frēb-, and NP ریو rēw 'deceit' from the simplex (Skt. rip- 'Betrug'). Modern Iranian scholarship prefers a different origin for the verb: Nyberg (Manual of Pahlavi II, s.v. frēftan) states 'From fra + Av. (679 sq.) 1dab-', and Cheung (EDIV 2007) s.v. *dab 'to deceive' lists BMP pldp- /frēb-/ and 'NWIR: (+ *fra-) NP farēftan/farēb-' under PIE *dʰebʰ- 'to deceive, harm' (Skt. dabh-, Hitt. tepnu-), while under *raip he says flatly: 'Several Iranian forms frequently cited as cognate are probably unconnected: BMP pldp- /frēb-/, NP fireb- (fareb-) “to deceive” (< *fra-dab, *dab)'. Wiktionary follows Cheung. For ریو rēw Cheung is agnostic-to-negative: 'The NP form rēv “deceit, ruse” is difficult to assess: Ir. *p can hardly yield NP -v in final position, cf. tab “fever” (*tap) ... It cannot be excluded that the NP form is a rhyming word.' That phonological objection (Old Iranian intervocalic/final *-p- gives NP -b, not -v) is the crux: *raipa- should have given NP *rēb, not rēw. On the other side stand Hübschmann (Persische Studien, note to Horn 829: 'Anders Mann ZDMG. 47, 705. Ich stehe auf Horn's Seite'), Mo'in (footnote to ریو in Borhan-e Qate') and Aryanpur (p.393), so the chart is not eccentric — but the specialist consensus since Nyberg 1974 and Cheung 2007 is against it. The parenthetical secondary forms in the JSON (فریبا، فریبنده؛ فریبیدن، فریبش؛ ریوه) are all real Persian derivatives of the same stems.\",\n     \"derivation_fa\": \"نورایی به پیروی از هرن (شمارهٔ ۶۴۳ و ۸۲۹) و پوکورنی، «فریفتن/فریب» را از *fra-raip- (فارسی میانه frēftan، frēb-) و «ریو» را از همان ریشهٔ ساده گرفته است. امّا نیبرگ (در واژه‌نامهٔ پهلوی، ذیل frēftan) و چونگ (فرهنگ ریشه‌شناختی فعل ایرانی، ۲۰۰۷) این فعل را از *fra-dab- و ریشهٔ هندواروپایی *dʰebʰ- «فریب دادن» (سنسکریت dabh-) می‌دانند و ویکی‌واژه نیز همین را می‌آورد. چونگ دربارهٔ «ریو» می‌گوید پـ ایرانی باستان در پایان واژه در فارسی نو به «ب» بدل می‌شود نه به «و» (مانند tap > تب)، پس *raipa- باید «ریب» می‌شد. در مقابل، هوبشمان صریحاً طرف هرن را می‌گیرد و معین در حاشیهٔ برهان قاطع و آریان‌پور هم همین پیوند را می‌آورند. نتیجه: پژوهش امروزی ادعای نورایی را دربارهٔ «فریب/فریفتن» رد می‌کند و دربارهٔ «ریو» آن را مشکوک می‌داند.\",\n     \"sources\": [W_FARIFTAN, W_FARIB, W_RIV, A_FARIB, A_RIV],\n     \"ref_check\": [\n      {\"ref\": \"HRN:142\", \"status\": \"supports\", \"note\": \"Horn no. 643, p.142 (HRN.txt \\\\f-leaf 164): 'rēw ‚Betrug, List‘ (Šahn. II, 735) ... ai. rip- ‚Betrug‘ (√rep-, lep- ‚anschmieren‘). Vergl. firēften (No. 829).'\"},\n      {\"ref\": \"HRN:184\", \"status\": \"supports\", \"note\": \"Horn no. 829, p.184 (HRN.txt \\\\f-leaf 206): 'firēften ‚betrügen‘, Praes. firēb-em, firēb ‚Betrug‘ ... ai. pra + √rep- ‚anschmieren, betrügen‘ ... phlv. frēftan, frēpēt, frēp'.\"},\n      {\"ref\": \"MON:1707\", \"status\": \"partial\", \"note\": \"Mo'in, Farhang-e Farsi s.v. فریب (read via abadis.ir, which reprints the entry; print page numbers are not mappable online): '(فِ یا فَ) [په.] (اِ.) مکر، حیله، نیرنگ' — Mo'in tags the word only as Pahlavi, and gives no Sanskrit ancestor; the meaning matches, the derivation is not stated.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"CHEUNG\", \"where\": \"EDIV s.v. *dab p.42 and s.v. *raip p.308 (CHEUNG.txt lines 3873, 20267)\", \"stance\": \"contradicts\", \"note\": \"Under *dab: '*MIDDLE PERSIAN: (+ *fra-) BMP pldp- /frēb-/ “to deceive” ... *NWIR: (+ *fra-) NP farēftan/farēb- ... «PIE *dʰebʰ-'. Under *raip: 'Several Iranian forms frequently cited as cognate are probably unconnected: BMP pldp- /frēb-/, NP fireb- (fareb-) “to deceive” (< *fra-dab, *dab) ... The NP form rēv “deceit, ruse” is difficult to assess: Ir. *p can hardly yield NP -v in final position'.\"},\n      {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II, s.v. frēftan (NYB_vol2_glossary.txt line 1592)\", \"stance\": \"contradicts\", \"note\": \"'frēftan [pldptn'] frēv- [pldp-] to deceive, to seduce ... From fra + Av. (679 sq.) 1dab-; Paz. frēftan frēv-; NP firēftan firēb-.'\"},\n      {\"src\": \"HUB\", \"where\": \"Persische Studien, note to Horn no. 829 (HUB.txt line 3010)\", \"stance\": \"supports\", \"note\": \"'829. Anders Mann ZDMG. 47, 705. Ich stehe auf Horn's Seite, vgl. meine Etym. und Lautl. der osset. Spr. Nr. 271.' — Hübschmann explicitly endorses Horn's *rep- derivation.\"},\n      {\"src\": \"BQT\", \"where\": \"vol. 2, footnote to ریو (BQT_v2_pages.txt \\\\f-leaf 453 ≈ printed p.993)\", \"stance\": \"supports\", \"note\": \"Headword 'ریو = بکسر اول ... بمعنی مکر و حیله و تزویر و فریب باشد' with Mo'in's note 'هندی باستان rip- (حیله) (از ریپ rep-, lep-) ... ق: فریفتن'.\"},\n      {\"src\": \"ARY\", \"where\": \"Aryanpur p.393, entry فریفتن، فریب (ARY_pages.txt line 11623 ff., after tag [pdf page 392])\", \"stance\": \"supports\", \"note\": \"Aryanpur puts فریفتن/فریب with Pahlavi FRYFTN/FRYB, Sanskrit REP, Greek LIPOS/LIPAROS, Latin LIPPUS, Gothic BILEIBAN/LAIBA, and notes 'واژهٔ انگلیسی LIVE نیز از همین واج‌ریشه است' — i.e. the same chart as Nourai's.\"},\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary (PHD_mackenzie.txt, F section)\", \"stance\": \"silent\", \"note\": \"MacKenzie records 'frēftan, frēb- [plyptn'] deceive' but gives no etymology, so he neither supports nor contradicts.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Germanic\", \"words\": \"\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Empty pass-through box: the Germanic stage between PIE *leyp- and the English words. The relevant forms are Proto-Germanic *līban 'to remain, be left' (Goth. bileiban, OHG bilīban, OE belīfan), the derived noun *lībą 'life, body' (OE līf, ON líf, OHG līb > German Leib), the weak verb *libjaną 'to live' (OE libban/lifian, Goth. liban) and *librō 'liver' (OE lifer, OHG lebara). The semantic path is 'stick' > 'stick around, remain' > 'continue, live', a development Boutkan calls Germanic-only but 'semantically comprehensible'.\",\n     \"derivation_fa\": \"این جعبه تهی است و تنها مرحلهٔ ژرمنی میان ریشهٔ هندواروپایی و انگلیسی را نشان می‌دهد. صورت‌های بازسازی‌شده عبارتند از *līban «بر جای ماندن»، *lībą «زندگی، تن»، *libjaną «زیستن» و *librō «جگر». تحول معنایی «چسبیدن ← بر جای ماندن ← زیستن» ویژهٔ شاخهٔ ژرمنی است. ادعای نورایی درست است.\",\n     \"sources\": [W_LEYP, E_LIFE],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. leip- (AHD_watkins1985.txt line 671): '1. Germanic *libam in Old English lif ... 2. Germanic *libēn in Old English lifian, libban ... 3. Germanic *laibjan ... 4. Germanic *libro in Old English lifer, liver'.\"},\n      {\"ref\": \"KLN:874\", \"status\": \"supports\", \"note\": \"Klein 1966 p.874 s.v. 'leave, tr. and intr. v.' (KLN_1966.txt offset 5370317, immediately before the page mark 875): 'ME. leven, fr. OE. lǣfan ... rel. to OE. lāf ... OE. belīfan ... Goth. bileiban “to remain”, and prob. also to OE. līf “life”, libban, lifian “to live”, orig. “to remain”; cogn. with Gk. lipos ... OI. limpáti “smears” ... L. lippus'.\"},\n      {\"ref\": \"KLN:887\", \"status\": \"supports\", \"note\": \"Klein p.887 s.v. 'life, n.' (running head 'lifer lilac 888' follows): 'ME. lif, fr. OE. līf, rel. to ON. líf “life, body” ... prop. “continuance, perseverance”, fr. I.-E. base *lip-, “to remain, persevere, continue, live”.'\"},\n      {\"ref\": \"KLN:899\", \"status\": \"supports\", \"note\": \"Klein p.899 (the entries 'live, intr. and tr. v.' and 'liver, n., secreting organ' both stand just after the page mark 899): 'live ... fr. OE. libban, lifian ... fr. I.-E. base *leip-'; 'liver ... ME., fr. OE. lifer ... possibly also with Gk. liparos “oily, fat, greasy”. See leave, v.'\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"p.670 f. (POK_02.txt lines 5248-5250)\", \"stance\": \"supports\", \"note\": \"'got. bileiban, ahd. bilīban ‚bleiben‘ ... got. laiba f., aisl. leif, ahd. leiba, ags. lāf ‚Überbleibsel‘ ... germ. līb- ‚(kleben) bleiben‘ hat auch die Bed. ‚übrigbleiben‘ ... aufgesaugt'. Pokorny does bracket off Goth. liban/OE līf under a variant *leibh- 'leben' — a nuance Nourai's box does not show.\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 index (AHD_watkins1985.txt lines 1747, 1757)\", \"stance\": \"supports\", \"note\": \"'LIFE leip-' ; 'LIVE! leip- ... LIVER! leip-'.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"English\", \"words\": \"life, live, liver\", \"verdict\": \"confirmed\",\n     \"derivation\": \"OE līf > ME lif > life; OE libban/lifian (Anglian) > ME liven > live; OE lifer > liver. Etymonline: life 'from Proto-Germanic *leiban ... properly “continuance, perseverance”, reconstructed in Watkins to be from PIE root *leip- “to stick, adhere”'; live 'from Proto-Germanic *libejanan ... from PIE root *leip-'. Liver is the least secure of the three: OE lifer, PGmc *librō, is attached to the root only on the assumption that it means 'the fatty/greasy organ' (Klein: 'possibly also with Gk. liparos “oily, fat, greasy”'), and Kroonen and Beekes leave the noun's ulterior origin open; Watkins nevertheless files LIVER¹ under leip-.\",\n     \"derivation_fa\": \"انگلیسی کهن līf > انگلیسی میانه lif > life؛ libban/lifian > liven > live؛ lifer > liver. این زنجیره را واتکینز، کلاین و اتیمولاین یکسان می‌آورند و ادعای نورایی درست است. تنها دربارهٔ liver «جگر» احتیاط لازم است، زیرا پیوند آن با این ریشه بر پایهٔ معنای «اندام چرب» است و قطعی نیست.\",\n     \"sources\": [E_LIFE, W_LEYP],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The node carries no references of its own; it inherits AHD and KLN:874,887,899 from the Germanic parent box, all of which were checked there and support it.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"pp.887, 899 (KLN_1966.txt s.vv. life, live, liver)\", \"stance\": \"supports\", \"note\": \"See the quotations under the Germanic node; Klein puts life, live, liver and leave under one I.-E. base *leip-.\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. leip- and index (lines 671, 1747, 1757)\", \"stance\": \"supports\", \"note\": \"'LIFE, LIVELY ... LIVE! ... LIVER!' all listed under leip-.\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict. (SKT.txt, L section)\", \"stance\": \"silent\", \"note\": \"Skeat's 'life/live' entries were not legible in this OCR at the point searched; no statement either way.\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 1,\n   \"root\": \"Leith\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *leyt(H)- 'to go forth, depart; (euphem.) die' (Pokorny 2. leit(h)- 672; Watkins/AHD leit-² 'To go forth, die'; LIV *leitH-)\",\n   \"note\": \"Pokorny 672 prints exactly '2. leit(h)- ‚fortgehen; sterben; gehen‘' and Watkins's heading is word-for-word Nourai's gloss, 'To go forth, die'. Root, language label and gloss are all correct. Note that Pokorny 672 also carries a homonym '1. leit- ‚verabscheuen; freveln‘' (whence English loath) which is a different root and is not what this chart is about.\",\n   \"note_fa\": \"ریشهٔ هندواروپایی آغازین *leyt(H)- «رفتن، درگذشتن، مردن»؛ پوکورنی در صفحهٔ ۶۷۲ عیناً همین معنا را می‌آورد و واتکینز نیز با همین ترجمهٔ انگلیسی. باید توجه داشت که در همان صفحه ریشهٔ همآوای دیگری (leit- «نفرت داشتن») هست که ربطی به این نمودار ندارد. ادعای نورایی دربارهٔ ریشه درست است.\",\n   \"sources\": [W_RASTAXIZ],\n   \"ref_check\": [\n    {\"ref\": \"POK:672\", \"status\": \"supports\", \"note\": \"POK_02.txt (page mark 672 present in the text): '2. leit(h)- ‚fortgehen; sterben; gehen‘. Av. raeθ- ‚sterben‘ (Präs. iriθyeiti); got. ga-leipan ‚gehen‘ ... germ. *laidō ... Kaus. (germ. *laidian) anord. leida ‚führen‘ ... WP. II 401 f.'\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. II p.401 (WLD_Bd2_pages.txt line 26600, running head 'leit leit(h)- 401')\", \"stance\": \"supports\", \"note\": \"'2. leit(h)- ‚fortgehn; sterben; gehn‘. Av. raeθ- ‚sterben‘ (Praes. iriθyeiti) ... got. -leiþan ‚gehn‘ ... anord. leið f. ‚Weg, Richtung, Weise‘ ... kaus. anord. leiða ‚führen‘'.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. leit-² (AHD_watkins1985.txt line 677)\", \"stance\": \"supports\", \"note\": \"'leit-2. To go forth, die. 1. Suffixed o-grade form *loit-eyo- in Germanic *laidjan ... 2. Suffixed variant o-grade form *loit-ā in Germanic *laidō ... [Pok. leit(h)- 672.]'\"},\n    {\"src\": \"CHEUNG\", \"where\": \"EDIV s.v. *raiθ¹ (CHEUNG.txt, p.308-309)\", \"stance\": \"supports\", \"note\": \"'*raiθ¹ “to lead, go forth; [euphem.] die, pass away” ... «PIE *leitH- “to go (forth), pass (away)” = LIV: 410 | Pok.: 672. *IE COGNATES: Toch. lit- “to pass on, move”, Goth. ga-leiban “to go”'.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann s.v. leit- (2) (IEC.txt line 9613)\", \"stance\": \"partial\", \"note\": \"'leit- (2) “go, creep, flow”. Cf. WP II, 401 ... Go. af-leiþan, sv 1. “depart”; OHG lidan ... OE liðan' — Mann keeps the 'go' sense but does not gloss the root 'die'.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Avestan\", \"words\": \"raěth, ris 1, rith; iris-ta, ris-ta\", \"verdict\": \"plausible\",\n     \"derivation\": \"Young Avestan has the root raēθ- / weak grade iriθ- 'to die, pass away' (present iriθyeiti V 6.10 etc., para.iriθyeiti 'passes away'), with the perfect passive participle irista- 'dead' (Yt 13.9, Yt 19.11, V 5.10 etc.); Nourai's 'raěth' and 'rith' are these two ablaut grades, and 'iris-ta / ris-ta' are irista- with its later, aphaeretic Pahlavi shape rist. All of that is confirmed by Pokorny 672, Walde-Pokorny II 401, Bartholomae's AiW (irista- is cited there dozens of times, s.v. raēθ- at col. 1480) and Cheung's *raiθ¹. The doubtful item is the middle form 'ris 1' (with Nourai's homonym number): a form with a sibilant belongs rather to Av. raēš- / iriš- 'to be hurt, suffer damage' (present irisiieiti, MP rēs-, NP ریش rēš 'wound'), which Bartholomae, Horn (no. 641, p.142) and Cheung (*raiš, a separate article) all treat as a distinct root; folding it in here conflates 'die' with 'be injured'. The rest of the node stands.\",\n     \"derivation_fa\": \"در اوستای متأخر ریشهٔ raēθ-/iriθ- «مردن، درگذشتن» با زمان حال iriθyeiti و اسم مفعول irista- «مرده» آمده است؛ دو صورت «raēth» و «rith» در نمودار همین دو درجهٔ ابلاوت است و بارتولومه، پوکورنی و چونگ آن را تأیید می‌کنند. امّا صورت میانی «ris 1» مشکوک است؛ صورتی با سایشی به ریشهٔ دیگری تعلق دارد: raēš-/iriš- «آسیب دیدن» (فارسی میانه rēs-، فارسی نو «ریش») که چونگ و بارتولومه آن را ریشه‌ای جداگانه می‌دانند. پس: ادعا در کلیّت درست است، ولی با احتیاط دربارهٔ یک صورت.\",\n     \"sources\": [W_RASTAXIZ],\n     \"ref_check\": [\n      {\"ref\": \"POK:672\", \"status\": \"supports\", \"note\": \"'Av. raēθ- ‚sterben‘ (Präs. iriθyeiti)' — Pokorny p.672 (POK_02.txt); the Avestan lemma and gloss are exactly Nourai's.\"},\n      {\"ref\": \"WLD:401\", \"status\": \"supports\", \"note\": \"Walde-Pokorny Bd. II p.401 (WLD_Bd2_pages.txt line 26600 ff.): '2. leit(h)- ‚fortgehn; sterben; gehn‘. Av. raēθ- ‚sterben“ (Praes. iriθyeiti)'.\"},\n      {\"ref\": \"ETM:66\", \"status\": \"not_checked\", \"note\": \"Abolghasemi, Risheh-shenasi (Etimoloji), Qoqnus 1374 — refs_online.json records it as 'catalog' only: no digital copy on archive.org, ketabnak or noorlib, purchase/catalogue links only.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"Bartholomae AiW s.v. raēθ-/irista- (BRT.txt, e.g. lines 2551, 5258, 8965, 9547)\", \"stance\": \"supports\", \"note\": \"irista- 'dead, corpse' is quoted throughout, e.g. 'us irista paiti arənti' (FrW 4.3) 'the dead rise again'; 'aētahe yat iristahe' (V 5.10) 'of that dead man'; 'iriš-ya-stāt- f. ‚Sterben, Tod‘' (line 25473). Nyberg cites this article as AiW 1480 s.v. raēθ-.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"EDIV s.v. *raiθ¹ and *raiš (CHEUNG.txt, pp.308-309)\", \"stance\": \"partial\", \"note\": \"Supports raēθ-/iriθ-/irista- ('Partic. ... perf. pass. YAv. irista- (Yt 13.9, Yt 19.11 ...)'), but keeps *raiš 'to suffer (damage, illness)' (YAv. raēš-, irisiieiti) as a separate root — so 'ris 1' does not belong under Leith.\"},\n      {\"src\": \"AVG\", \"where\": \"Jackson, Avesta Grammar (AVG.txt)\", \"stance\": \"silent\", \"note\": \"No usable entry found for the verb in the searched OCR.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"rist; rist-axez\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Book Pahlavi rist [lyst'] 'the dead, the bodies of the dead' is Av. irista- with loss of the initial (prothetic) i- and shortening: irista- > *rist. The compound rist-āxēz [lyst'hyc'] 'the resurrection of the dead' joins it to āxēz, the present stem of āxistan 'to rise up' (ā- + *xaiz-/xez-, cf. NP خاستن/خیز-), hence literally 'rising of the dead'; it is a technical term of Zoroastrian eschatology, standing in the Bundahišn and the Dādestān ī Mēnōg ī Xrad beside tan ī pasēn 'the final body'. Nourai's cross-reference to the root Swîğ is for the āxēz element. Nyberg and MacKenzie give exactly these two entries.\",\n     \"derivation_fa\": \"فارسی میانه rist [lyst'] «مرده، تن مردگان» همان irista- اوستایی است که الف آغازین را از دست داده است. ترکیب rist-āxēz از این واژه + ستاک حال فعل اخیستن (ــ خاستن/خیز-) ساخته شده و تحت‌اللفظ یعنی «برخاستن مردگان»؛ اصطلاحی در معادشناسی زرتشتی است که در بندهش و مینوی خرد در کنار tan ī pasēn می‌آید. نیبرگ و مکنزی هر دو همین دو مدخل را دارند؛ ادعای نورایی درست است.\",\n     \"sources\": [W_RASTAXIZ],\n     \"ref_check\": [\n      {\"ref\": \"NYB:170\", \"status\": \"supports\", \"note\": \"Nyberg, Manual of Pahlavi II (Glossary), s.v. (NYB_vol2_glossary.txt lines 3318, 3323): 'rist [lyst'] the dead, the bodies of the dead ... Borrowed from Av. (1480 s. v. raēd-) irista-; Paz. rist' and 'rist-āxēz [lyst'hyc'] the resurrection of the dead ... From rist (q. v.) + āxēz, pres. st. of āxistan (q. v.); Paz. rist-āxež; NP rastāxēz “day of resurrection”, “tumult”.' (Our leaf mapping of the OCR would put this at p.178, but Cheung's EDIV cites 'Nyberg II: 169b' for rēs, the entry immediately preceding, which confirms Nourai's p.170.)\"},\n      {\"ref\": \"HRN:103\", \"status\": \"supports\", \"note\": \"Horn no. 462 xēzīden 'aufstehen' spans pp.102-103; the top of p.103 (HRN.txt \\\\f-leaf 125) reads 'rīst-āxēz, āxēzīt (Phlv.-Vend. für aw. √haiž-; AV.)' — i.e. the āxēz element and the compound rist-āxēz, as the chart's arrow needs.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary, R section (PHD.txt line 559; PHD_mackenzie.txt line 4399)\", \"stance\": \"supports\", \"note\": \"'rist [lyst' | M ryst] dead. ˈristag [lystk'] corpse ... rist-āxēz [lyst'hyc | M ryst'hyz, N ~] resurrection of the dead'; the English-Pahlavi part has 'resurrection ristāxēz'.\"},\n      {\"src\": \"NYB\", \"where\": \"same volume, cross-reference list (NYB_vol2_glossary.txt lines 5199, 6782, 7353)\", \"stance\": \"supports\", \"note\": \"'irista-: rist'; 'rist: ~ ristaxež- rist-āxēz'; 'rastāxēz: rist-āxēz.'\"},\n      {\"src\": \"SNS\", \"where\": \"Tavoosi, glossary of Shayast ne Shayast (SNS.txt)\", \"stance\": \"silent\", \"note\": \"No entry located in the searched OCR.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Persian\", \"words\": \"rastâxîz\", \"verdict\": \"confirmed\",\n     \"derivation\": \"NP رستاخیز rastāxēz (and the contracted رستخیز rastaxīz used by Ferdowsī in the verse quoted on the page) is the direct continuation of MP rist-āxēz, with the regular Pazand/New Persian lowering of the unstressed first vowel i > a before the cluster (Paz. rist-āxež beside rastāxēz). The meaning stays technical, 'the resurrection of the dead, the Last Day', and in classical poetry is extended to 'uproar, tumult'. Wiktionary: 'Inherited from Middle Persian lystʾyc /rist-axēz/ “resurrection”. That latter part xēz is related to خاستن (xāstan, “to rise”).' Horn (no. 613) and Mo'in's footnote in Borhan-e Qate' say the same.\",\n     \"derivation_fa\": \"«رستاخیز» (و صورت مخفف «رستخیز» که در بیت فردوسی آمده) دنبالهٔ مستقیم rist-āxēz فارسی میانه است؛ واکهٔ i در هجای نخست به a بدل شده (پازند rist-āxež ـ rastāxēz). معین در حاشیهٔ برهان قاطع (ص ۹۴۸) می‌نویسد: پهلوی rist (مرده) + خیز (رک: خاستن)، پازند rastāxēz، «بنابرین رستاخیز لغةً بمعنی برخاستن مردگان است». ادعای نورایی درست است.\",\n     \"sources\": [W_RASTAXIZ],\n     \"ref_check\": [\n      {\"ref\": \"BQT:948\", \"status\": \"supports\", \"note\": \"Borhan-e Qate' vol. 2 p.948 (BQT_v2_pages.txt \\\\f-leaf 408, whose running head is the headword رستاخیز): 'رستاخیز ... بر وزن دستاویز، قیامت را گویند که محشر باشد'; Mo'in's footnote: '... پهلوی rist (مرده، گذشته) + خیز (رک: خاستن) ... پازند rastāxēz ... بنابرین رستاخیز (مخفف آن، رستخیز) لغةً بمعنی برخاستن مردگان است'.\"},\n      {\"ref\": \"HRN:136\", \"status\": \"supports\", \"note\": \"Horn no. 613, p.136 (HRN.txt \\\\f-leaf 158): 'restāxēz ‚Auferstehung der Todten‘. aw. irista- ‚todt‘; phlv. rist, ristāxēz (paz. ristaхēz).'\"},\n      {\"ref\": \"NYB:170\", \"status\": \"supports\", \"note\": \"Nyberg's rist-āxēz article ends 'NP rastāxēz “day of resurrection”, “tumult”' — the New Persian outcome Nourai draws.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"Mo'in's own etymological footnotes as printed in Borhan-e Qate' p.948 (see ref_check)\", \"stance\": \"supports\", \"note\": \"Same note as above; Mo'in derives رستاخیز from Pahlavi rist + خیز.\"},\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, English-Pahlavi index (PHD_mackenzie.txt line 7423)\", \"stance\": \"supports\", \"note\": \"'resurrection ristaxez' — the MP ancestor of the NP word.\"},\n      {\"src\": \"HRN\", \"where\": \"no. 613, p.136\", \"stance\": \"supports\", \"note\": \"See ref_check; Horn's headword is the New Persian word itself.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"Germanic\", \"words\": \"laipjan; laidô\", \"verdict\": \"transcription_suspect\",\n     \"derivation\": \"The second form is right: Proto-Germanic *laidō 'way, course' (o-grade *loit-ā) gives OE lād 'course, way, carrying' > ME lode/lade > load, lode. The first form is wrong as printed: the causative 'to lead' is Proto-Germanic *laidjan (< *loit-eyo-), whence OE lǣdan, OS lēdian, OHG leiten, ON leiða — there is no Germanic *laipjan. Watkins prints '*laidjan' and Pokorny 'Kaus. (germ. *laidian)'. The printed page of Nourai (PDF p.308, book p.278, rendered at 600 dpi) clearly shows 'laipjan : to lead', so the extraction is faithful and the error is the book's: a p for d, either Nourai's own slip or a typesetting error. Apart from that letter the node is correct and the arrow from PIE *leyt- is standard.\",\n     \"derivation_fa\": \"صورت دوم درست است: ژرمنی آغازین *laidō «راه، مسیر» که به انگلیسی کهن lād و سپس load/lode رسیده است. امّا صورت نخست غلط چاپ شده است؛ فعل سببی «رهبری کردن» در ژرمنی آغازین *laidjan است (انگلیسی کهن lǣdan، آلمانی کهن leiten) و صورت *laipjan وجود ندارد؛ پوکورنی و واتکینز هر دو *laidjan/*laidian دارند. تصویر صفحهٔ چاپی (ص ۲۷۸ کتاب) نشان می‌دهد که خود کتاب «laipjan» چاپ کرده؛ پس خطای چاپی کتاب است نه خطای خوانش اسکن.\",\n     \"error_in\": \"book\",\n     \"book_prints\": \"laipjan\",\n     \"correct_form\": \"laidjan\",\n     \"sources\": [E_LEG],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"Watkins 1985 s.v. leit-² (AHD_watkins1985.txt line 677) supports the sense and the second form but prints the first differently: 'Suffixed o-grade form *loit-eyo- in Germanic *laidjan in: a. Old English lǣdan, to lead: LEAD!, b. Old High German leiten ... 2. Suffixed variant o-grade form *loit-ā in Germanic *laidō in Old English lād, course, way: LOAD, LODE'. So AHD, Nourai's own cited reference, has *laidjan, not *laipjan.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"p.672 (POK_02.txt)\", \"stance\": \"partial\", \"note\": \"'germ. *laidō: 1. ‚Weg‘ in aisl. leið f. ... Kaus. (germ. *laidian) anord. leiða ‚führen, geleiten‘, ags. lǣdan, as. ledian ‚leiten, bringen‘, ahd. leiten' — confirms *laidō and the causative *laidian, not *laipjan.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. II p.401 (WLD_Bd2_pages.txt line 26608 ff.)\", \"stance\": \"partial\", \"note\": \"'anord. leið f. ‚Weg, Richtung, Weise‘, ags. lād f. ‚Weg, Reise, Lebensunterhalt‘ ... kaus. anord. leiða ‚führen, geleiten, begleiten‘, ags. lǣdan, as. ledian' — same, with d.\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat s.vv. lode, lead (1) (SKT.txt around line 10589)\", \"stance\": \"supports\", \"note\": \"'lode, a vein of ore, a water-course. (E.) The true sense is “course”. A.S. lād, a way, course, journey. — A.S. līðan, to travel, go ... (Base LITH.)'; 'lead (1), to conduct (E.) ... A.S. lǣdan, to lead. — A.S. lād, a course, way'.\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"English\", \"words\": \"lead, load\", \"verdict\": \"confirmed\",\n     \"derivation\": \"OE lǣdan (< PGmc *laidjan) > ME leden > lead (verb); OE lād 'way, course, carrying' (< PGmc *laidō) > ME lode 'course, carrying' > load (with the modern spelling and the sense 'burden carried' separating from lode 'vein of ore, watercourse' only in the 16th-17th c.). Watkins files LEAD¹, LOAD, LODE and LIVELIHOOD under leit-²; Skeat gives the same chain.\",\n     \"derivation_fa\": \"انگلیسی کهن lǣdan (از *laidjan ژرمنی) > lead «رهبری کردن»؛ انگلیسی کهن lād «راه، بردن» (از *laidō) > lode و load. جدایی معنایی load «بار» و lode «رگهٔ معدنی» تنها از سدهٔ شانزدهم/هفدهم میلادی رخ داده است. ادعای نورایی درست است.\",\n     \"sources\": [E_LEG],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No references of its own; it inherits AHD from the Germanic parent, which was checked there and lists LEAD!, LOAD, LODE under leit-².\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 index (AHD_watkins1985.txt lines 1739, 1759)\", \"stance\": \"supports\", \"note\": \"'LOAD leit-2 ... LODE leit-2'; the leit-² article itself names LEAD!, LOAD, LODE, LIVELIHOOD.\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat s.vv. lode, lead (1), lodestar, lodestone (SKT.txt line 10589 ff.)\", \"stance\": \"supports\", \"note\": \"'A.S. lād, a way, course, journey. — A.S. līðan, to travel, go ... Icel. leið, lode, way, course, from líða, to go; Swed. led, a course. (Base LITH.)'\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 2,\n   \"root\": \"Lek\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *lek- 'to leap, fly; (of limbs) to bend, jerk' (Pokorny 2. lek- 673; Watkins/AHD lek- 'To leap, fly')\",\n   \"note\": \"Watkins's heading is verbatim Nourai's gloss: 'lek-. To leap, fly. ... [Pok. 2. lek- 673.]'. Pokorny 673 gives the fuller '2. lek- (: lək-) und lek- : lok- in Worten für ‚Gliedmaßen‘ und für ‚biegen, winden, springen, zappeln‘', citing Gk. λάξ, λάγδην 'kicking with the foot', ON leggr 'leg', Lith. lekiu 'to fly' — so the root, the language label and the gloss are right, and Nourai's 'kick' is precisely the Greek evidence. Two of the three branches drawn here are, however, weaker than the chart suggests: Pokorny himself marks the Latin words with '??' and modern Latin etymology (Ernout-Meillet, de Vaan) treats lacerta/locusta as of unknown origin; and English leg is not from Greek but from Old Norse.\",\n   \"note_fa\": \"ریشهٔ هندواروپایی *lek- «جهیدن، پریدن، لگد زدن»؛ عنوان واتکینز عیناً «To leap, fly» است و پوکورنی در ص ۶۷۳ می‌نویسد «واژه‌هایی برای اندام‌ها و برای خمیدن، جستن، تکان خوردن» با گواهی یونانی λάξ، λάγδην. پس خود ریشه درست است؛ ولی دو شاخهٔ لاتین و انگلیسی در نمودار دقیق رسم نشده‌اند (نگاه کنید به گره‌های ۴ و ۵).\",\n   \"sources\": [W_LAGAD, E_LEG],\n   \"ref_check\": [\n    {\"ref\": \"POK:673\", \"status\": \"supports\", \"note\": \"POK_02.txt (page mark 673): '2. lek- (: lək-) und lek- : lok- in Worten für ‚Gliedmaßen‘ und für ‚biegen, winden, springen, zappeln‘. Ai. ṛkšalā ‚Fußgelenk‘; gr. λάξ, λάγδην ‚mit dem Fuße ausschlagend‘ ... aisl. leggr ‚Unterbein, Knochen‘ ... lit. lekiū, lėkti ‚fliegen‘'.\"},\n    {\"ref\": \"OEW:217\", \"status\": \"not_checked\", \"note\": \"Shipley, The Origins of English Words (1984). refs_online.json marks it 'archive_restricted': both IA copies (originsofenglish0000ship, originsofenglish00jose) are lending-only and the djvu.txt returns 401/403; HathiTrust is search-only. No page 217 text could be obtained.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. lek- (AHD_watkins1985.txt line 679)\", \"stance\": \"supports\", \"note\": \"'lek-. To leap, fly. Possibly suffixed o-grade form *lok-ost- in Latin locusta, a marine shellfish, lobster: LOBSTER, LOCUST. [Pok. 2. lek- 673.]' — note Watkins's 'Possibly' and that he does NOT put lizard/alligator here.\"},\n    {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. lizard (p.899 f.) and leg (p. c.877)\", \"stance\": \"partial\", \"note\": \"Klein derives lacertus/lacerta 'fr. I.-E. base *leq-, *lēq-, “to bend, twist”, whence prob. also L. locusta ... ON. leggr, “leg”' — the same root complex, but glossed 'bend, twist' rather than 'leap, fly'.\"},\n    {\"src\": \"ARY\", \"where\": \"Aryanpur, Latin index (ARY_latin_index_pages.txt line 13195 ff.)\", \"stance\": \"supports\", \"note\": \"An entry whose references are 'POKORNY 673; SKEAT (LEG) 335; ONIONS (LEG) 522; BARNHART (LEG) 587' groups LAX (Greek), LACERTUS (Latin), RKSALA (Sanskrit), LEGGR (Old Scandinavian), LAKAS (Lithuanian), LEZU/LEKT (Latvian), LAGNO (Old Prussian), LEG (English) — i.e. Aryanpur reproduces Pokorny's 673 grouping for the Persian headword; the Persian headword itself is illegible in this OCR.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Old Iranian\", \"words\": \"lakata, rakata\", \"verdict\": \"plausible\",\n     \"derivation\": \"These are not attested Old Iranian words but Gershevitch's reconstruction, which Nourai prints without asterisks. In The Avestan Hymn to Mithra (1959) p.182 n., Gershevitch writes: 'The opportunity may be taken to draw attention to the provable etymological connection of NPers. lagad “kick” with Gr. λάξ, λάγδην “kicking with the heel”. lagad should represent OIr. *(l/r)akata-. For the suffix cf. Av. nəmata- “felt” ... and Sogd. šʼkṭh, OInd. sikatā “sand”'. The l/r alternation is precisely why Nourai gives two shapes; Gershevitch even floats an *lekʷ-to-/*rekʷ-to- alternation (with Skt. lakuṭa 'club' and Lat. lacertus). Sound: an Old Iranian *rakata-/*lakata- is a -ta- formation on the root *lak-/*rak- 'kick', of the type Av. nəmata-.\",\n     \"derivation_fa\": \"این دو صورت گواهی‌شده نیستند بلکه بازسازی گرشویچ (۱۹۵۹، ص ۱۸۲ حاشیه) هستند: «فارسی نو lagad باید بازماندهٔ ایرانی باستان *(l/r)akata- باشد؛ برای پسوند بسنجید با اوستایی nəmata- ‚نمد‘ و سغدی شکته، سنسکریت sikatā ‚ریگ‘». ابدال l/r دلیل آوردن دو صورت در نمودار است. ادعای نورایی با احتیاط پذیرفتنی است؛ تنها باید گفت این صورت‌ها بازساخته‌اند نه مضبوط.\",\n     \"sources\": [W_LAGAD],\n     \"ref_check\": [\n      {\"ref\": \"AHM:182\", \"status\": \"supports\", \"note\": \"Gershevitch, The Avestan Hymn to Mithra, p.182 n. (AHM.txt line 1638; the book's index confirms '*lakata-, 182 n.'): 'the provable etymological connection of NPers. lagad “kick” with Gr. λάξ, λάγδην “kicking with the heel”. lagad should represent OIr. *(l/r)akata-.'\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"CHEUNG\", \"where\": \"EDIV (CHEUNG.txt, searched for lagad, *lak, *rak)\", \"stance\": \"silent\", \"note\": \"Cheung has no verbal root *lak/*rak and does not mention lagad; his dictionary covers verbs only, so the absence is not evidence against.\"},\n      {\"src\": \"BRT\", \"where\": \"Bartholomae AiW (BRT.txt)\", \"stance\": \"silent\", \"note\": \"No Avestan *lakata-/*rakata- is recorded — as expected, since Gershevitch's form is a reconstruction from the New Persian word.\"},\n      {\"src\": \"POK\", \"where\": \"p.673\", \"stance\": \"partial\", \"note\": \"Pokorny's 2. lek- article has no Iranian material at all (Skt. ṛkšalā is the only Indo-Iranian item), so the Iranian branch rests on Gershevitch alone.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Persian\", \"words\": \"lagad\", \"verdict\": \"confirmed\",\n     \"derivation\": \"NP لگد lagad 'a kick' continues Gershevitch's Old Iranian *(l/r)akata-: intervocalic *-k- is voiced to -g- and *-t- to -d in the passage to New Persian (the same lenition as in *raθa- > rad, *pitā- > pidar), and the final -a is lost, giving *lakata- > *lagad(a) > lagad. Wiktionary derives it 'from Proto-Indo-Iranian, a suffixed form of Proto-Indo-European *lek- (“to bend, leg”), cognate with Ancient Greek λάξ (láx, “with the leg/heel”), λᾰκτῐζω (laktízō, “to kick”); Sanskrit लकुट (lakuṭa)'. The variant spelling لغد given in the chart's parenthesis is an orthographic Arabicism, not a separate word.\",\n     \"derivation_fa\": \"«لگد» دنبالهٔ ایرانی باستان *(l/r)akata- است: واکمانع k در میان دو واکه در فارسی نو به g و t به d نرم شده و واکهٔ پایانی افتاده است (*lakata- > lagad)؛ همان دگرگونی که در pitar > پدر دیده می‌شود. ویکی‌واژه آن را از ریشهٔ هندواروپایی *lek- و هم‌ریشه با یونانی λάξ و λακτίζω و سنسکریت lakuṭa می‌داند. معین تنها معنا را می‌آورد و ریشه نمی‌دهد. ادعای نورایی درست است.\",\n     \"sources\": [W_LAGAD, A_LAGAD],\n     \"ref_check\": [\n      {\"ref\": \"AHM:182\", \"status\": \"supports\", \"note\": \"See node 1: Gershevitch's note is written expressly about NPers. lagad and derives it from OIr. *(l/r)akata-.\"},\n      {\"ref\": \"MON:3620\", \"status\": \"partial\", \"note\": \"Mo'in, Farhang-e Farsi s.v. لگد (read via abadis.ir; print pagination not mappable online): '(لَ گَ) (اِ.) ۱- ضربه ای که با پا زده شود. ۲- حرکت یا ضربة قهقرایی تفنگ یا توپ ...' — the gloss 'kick' is confirmed, but Mo'in gives no origin tag, so he neither supports nor contradicts the Old Iranian etymon.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"HRN\", \"where\": \"Horn, Grundriss (HRN.txt, L section)\", \"stance\": \"silent\", \"note\": \"Horn has no entry for lagad.\"},\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary (PHD.txt)\", \"stance\": \"silent\", \"note\": \"No Middle Persian *lagad is recorded; the word is first attested in New Persian, which is why Gershevitch had to reconstruct the Old Iranian form.\"},\n      {\"src\": \"MON\", \"where\": \"Mo'in s.v. لگد (abadis.ir)\", \"stance\": \"partial\", \"note\": \"Meaning confirmed, etymology not given — see ref_check.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Greek\", \"words\": \"lagadon\", \"verdict\": \"transcription_suspect\",\n     \"derivation\": \"There is no Greek word 'lagadon'. The form meant is the adverb λάγδην (lágdēn) 'kicking with the foot', which stands beside λάξ (láx) 'with the foot/heel', λακτίζω (laktízō) 'I kick' and λάκτισμος 'a kicking'. Pokorny 673 prints 'gr. λάξ, λάγδην ‚mit dem Fuße ausschlagend‘', Klein (s.v. leg) 'Gk. λάξ, λαγδήν, “kicking with the foot”', and Gershevitch AHM 182 n. the same pair; the -δην suffix is the ordinary Greek adverbial ending (cf. κρύβδην, σχέδην). The 600-dpi rendering of the printed page (book p.278) shows 'lagadon : a leap, kick', so the JSON is a faithful transcription and the corrupt form is Nourai's own — a misreading of the -δην ending as -don plus an inserted a. The chart's gloss 'a leap, kick' is right for λάγδην, and the derivation from *lek- is Pokorny's.\",\n     \"derivation_fa\": \"در یونانی واژه‌ای به صورت «lagadon» وجود ندارد؛ مراد قید λάγδην (lágdēn) «لگدزنان، با پا» است که در کنار λάξ و λακτίζω می‌آید؛ پوکورنی (ص ۶۷۳)، کلاین (ذیل leg) و گرشویچ هر سه همین دو صورت را می‌آورند؛ پسوند -δην پسوند قیدساز یونانی است. تصویر صفحهٔ چاپی نشان می‌دهد کتاب خود «lagadon» چاپ کرده؛ پس خطای چاپی کتاب است نه خطای خوانش اسکن؛ معنا و انتساب به ریشه درست است.\",\n     \"error_in\": \"book\",\n     \"book_prints\": \"lagadon\",\n     \"correct_form\": \"λάγδην (lágdēn)\",\n     \"sources\": [E_LEG, W_LAGAD],\n     \"ref_check\": [\n      {\"ref\": \"POK:673\", \"status\": \"partial\", \"note\": \"Pokorny p.673 has the word but in its true shape: 'gr. λάξ, λάγδην ‚mit dem Fuße ausschlagend‘, λάκτισμος ‚das Ausschlagen mit dem Fuße‘, λακτίζω ‚stoße mit dem Fuße‘' — so the reference supports the etymology but contradicts the printed form.\"},\n      {\"ref\": \"OEW:217\", \"status\": \"not_checked\", \"note\": \"Shipley 1984 is lending-only on archive.org (djvu.txt 401/403) and search-only on HathiTrust; the page could not be read, so it is not possible to say whether the corrupt 'lagadon' was taken over from Shipley.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. leg (KLN_1966.txt offset 5382653, p. c.877)\", \"stance\": \"partial\", \"note\": \"'prob. cogn. with OI. ṛkṣalā ... L. lacertus ... Gk. λάξ, λαγδήν, “kicking with the foot”, λακτίζειν, “to kick with the foot”' — the correct Greek forms.\"},\n      {\"src\": \"AHM\", \"where\": \"Gershevitch p.182 n. (AHM.txt line 1638)\", \"stance\": \"partial\", \"note\": \"'Gr. λάξ, λάγδην “kicking with the heel”' — again λάγδην, not 'lagadon'.\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. lek- (line 679)\", \"stance\": \"silent\", \"note\": \"Watkins's lek- article cites no Greek material at all.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"English\", \"words\": \"leg\", \"verdict\": \"disputed\",\n     \"derivation\": \"The arrow Greek → English is wrong: English leg was never borrowed from Greek. It is a Norse loan of the late 13th c. — ME legge, from Old Norse leggr 'a leg, bone of the arm or leg' (cf. ON armleggr 'arm', fótleggr 'shank'), Proto-Germanic *lagjaz, which displaced native OE sceanca 'shank'. What is true, and is presumably what Nourai meant to draw, is that Pokorny 673 files ON leggr in the same root as Gk. λάξ/λάγδην, so the two are cognates, not ancestor and descendant. Even that grouping is not secure: Etymonline calls *lagjaz 'a word with no certain ulterior connections. Perhaps from a PIE root meaning “to bend” [Buck]'.\",\n     \"derivation_fa\": \"پیکان «یونانی ← انگلیسی» نادرست است: واژهٔ leg در انگلیسی میانه (سدهٔ ۱۳م میلادی) وام‌واژه‌ای است از نورسی کهن leggr «پا، استخوان پا» (ژرمنی آغازین *lagjaz) که جای واژهٔ بومی sceanca را گرفت؛ نه از یونانی. آنچه درست است این است که پوکورنی leggr را با λάξ/λάγδην هم‌ریشه می‌داند، یعنی هم‌ریشه نه فرزند. پژوهش امروزی (اتیمولاین، بر پایهٔ باک) حتی همین هم‌ریشگی را قطعی نمی‌داند.\",\n     \"sources\": [E_LEG, W_LEG],\n     \"ref_check\": [\n      {\"ref\": \"OEW:217\", \"status\": \"not_checked\", \"note\": \"Shipley 1984 p.217 could not be consulted (IA lending-only, djvu.txt 401/403; HathiTrust search-only). Shipley's book is a discursive popular treatment of IE roots and may well be the source of both the false Greek form and the Greek→English arrow, but that cannot be verified from an accessible copy.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. leg (KLN_1966.txt offset 5382653)\", \"stance\": \"contradicts\", \"note\": \"'leg, n. — ME. legge, leg, fr. ON. leggr, “leg” (which is rel. to ON. armleggr, “arm”) ... prob. cogn. with OI. ṛkṣalā ..., L. lacertus ..., Gk. λάξ, λαγδήν' — cognate with the Greek, derived from Old Norse.\"},\n      {\"src\": \"POK\", \"where\": \"p.673\", \"stance\": \"partial\", \"note\": \"'aisl. leggr ‚Unterbein, Knochen‘, arm-, hand-leggr ‚Arm‘, fót-, lær-leggr ‚Wade‘ (*lagiz); langob. lagi ‚Schenkel‘' — same root, but a Germanic, not a Greek, line.\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. lek- and index\", \"stance\": \"contradicts\", \"note\": \"LEG does not appear under lek- at all in Watkins's index; only LOBSTER and LOCUST are listed there.\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"Latin\", \"words\": \"locusta, lacertilia\", \"verdict\": \"plausible\",\n     \"derivation\": \"Latin locusta 'locust; a marine shellfish, lobster' is the well-attested word; Klein explains it as '*lokos-ta, lit. “the jumper”', and Watkins as a 'possibly suffixed o-grade form *lok-ost-'. Nourai's second form is not classical Latin: lacertilia is New Latin, the 19th-century zoological name of the lizard suborder Lacertilia, itself coined from Latin lacerta/lacertus 'lizard'; the etymon of lizard and alligator is lacerta/lacertus, which is what the box should read. On the substance, the attachment of both words to *lek- is only 'plausible' in modern terms: Pokorny himself hedges — 'ob lat. lacertus ... lacerta ‚Eidechse‘ (‚die Biegsame‘)?? ... locusta ‚Heuschrecke; Meerkrebs‘ (‚mit Gelenken versehen‘?)?' — Watkins writes 'Possibly', Ernout-Meillet conclude 'Aucun rapprochement sûr', and Etymonline (following de Vaan and Beekes) calls lacertus 'a word of unknown origin', perhaps connected with Gk. likertízein 'to jump, dance', which Beekes thinks Pre-Greek. So the branch is defensible but not established.\",\n     \"derivation_fa\": \"لاتین locusta «ملخ؛ خرچنگ دریایی» واژه‌ای گواهی‌شده است و کلاین آن را *lokos-ta «جهنده» می‌داند. امّا صورت دوم، lacertilia، لاتین کلاسیک نیست؛ لاتین نو و نام ردهٔ جانورشناسی مارمولک‌ها (سدهٔ ۱۹م) است که خود از lacerta ساخته شده؛ نیای واقعی lizard و alligator همان lacerta/lacertus است. از نظر ریشه‌شناسی نیز پیوند این دو واژه با *lek- قطعی نیست: پوکورنی دو علامت پرسش می‌گذارد، ارنو‌مییه می‌نویسد «هیچ مقایسهٔ مطمئنی نیست» و دووان/بیکس آن را ناشناخته می‌دانند. پس: با احتیاط پذیرفتنی است.\",\n     \"sources\": [E_LIZARD, E_LOCUST],\n     \"ref_check\": [\n      {\"ref\": \"OEW:217\", \"status\": \"not_checked\", \"note\": \"Shipley 1984 is lending-only (see above); the page could not be read.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"p.673 (POK_02.txt)\", \"stance\": \"partial\", \"note\": \"'ob lat. lacertus, meist Pl. ‚die Muskeln, bes. der Oberarm‘, lacerta ‚Eidechse‘ (‚die Biegsame‘)?? ... locusta ‚Heuschrecke; Meerkrebs‘ (‚mit Gelenken versehen‘?)?' — Pokorny lists them but with a double question mark.\"},\n      {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.vv. lacerta, lacertus (LAT.txt line 31783 ff.)\", \"stance\": \"contradicts\", \"note\": \"'lacerta, -ae f.; lacertus, -ī ... Semble le même mot que lacertus “lézard”; cf. μῦς en grec et le rapport mus: musculus ... Aucun rapprochement sûr.' — no secure IE connection.\"},\n      {\"src\": \"KLN\", \"where\": \"Klein 1966 s.vv. locust (p.902) and lizard (p.899 f.)\", \"stance\": \"supports\", \"note\": \"'locust ... fr. L. locusta ... prob. fr. *lokos-ta, lit. “the jumper”, and rel. to lacertus (masc.), lacerta (fem.), “lizard”'; 'lizard ... fr. L. lacertus ... derive fr. I.-E. base *leq-, *lēq-, “to bend, twist”, whence prob. also L. locusta'.\"}\n     ]\n    },\n    {\n     \"id\": 6, \"lang\": \"English\", \"words\": \"locust, lobster, lizard, alligator\", \"verdict\": \"confirmed\",\n     \"derivation\": \"All four are Latin, and the routes are well documented. locust: ME locuste, early 14c., from Latin locusta 'locust; lobster' (earlier borrowed in the Old French shape languste, c.1200). lobster: OE loppestre/lopustre, a native reshaping of Latin locusta under the influence of OE loppe 'spider' and the feminine agent suffix -estre. lizard: ME lesard/lusarde, late 14c., from Anglo-French lusard, Old French laisarde (Mod.Fr. lézard), from Latin lacerta/lacertus, the ending assimilated to English -ard. alligator: 1560s lagarto/aligarto, a corruption of Spanish el lagarto (de Indias) 'the lizard (of the Indies)', Sp. lagarto being Latin lacertus, with the article el (< L. ille) agglutinated; the unetymological final -r appears from the 1620s. The only qualification is the one carried up from the parent node: what is uncertain is not the Latin→English step but whether Latin locusta/lacerta really belongs to *lek-.\",\n     \"derivation_fa\": \"هر چهار واژه از لاتین‌اند و مسیرشان روشن است: locust از locusta؛ lobster از همان locusta که در انگلیسی کهن به loppestre دگرگون شده (به اثر loppe «عنکبوت» و پسوند -estre)؛ lizard از راه فرانسهٔ کهن laisarde از lacerta؛ و alligator از اسپانیایی el lagarto «آن مارمولک» (سدهٔ ۱۶م) که حرف تعریف به خود واژه چسبیده است. تنها نکتهٔ مورد تردید همان است که در گرهٔ پیشین گفته شد: پیوند خود لاتین با ریشهٔ *lek-. ادعای نورایی دربارهٔ این گره درست است.\",\n     \"sources\": [E_LOCUST, E_LOBSTER, E_LIZARD],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"Watkins 1985 s.v. lek- (line 679) gives only 'LOBSTER, LOCUST'; LIZARD and ALLIGATOR are filed elsewhere in his index (ALLIGATOR under al-1, from Latin ille), so AHD supports two of Nourai's four words in this box.\"},\n      {\"ref\": \"KLN\", \"status\": \"supports\", \"note\": \"Klein has all four: 'locust ... fr. L. locusta'; 'lobster ... ME., fr. OE. lopustre, loppestre, prob. corruption of L. locusta'; 'lizard ... fr. OF. laisard, lesard ... fr. L. lacertus (masc.), resp. lacerta (fem.)'; 'alligator ... Corruption of Sp. el lagarto ... lagarto comes fr. L. lacertus. See ille and lizard.'\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"SKT\", \"where\": \"Skeat s.vv. locust, lobster (SKT.txt line 10588 f.)\", \"stance\": \"supports\", \"note\": \"'Locust, a winged insect. (L.) M.E. locuste. — L. locusta, a shell-fish, also a locust.'; 'lobster ... A.S. lopustre, a corrupted form of A.S. loppestre, a corruption of L. locusta'.\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 index (lines 1228, 1760)\", \"stance\": \"partial\", \"note\": \"'LOBSTER lek- ... LOCUST lek-' but 'ALLIGATOR al-1' — Watkins does not put alligator (or lizard) under this root.\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nimport io, os\np = \"/home/sfmqrb/git/rishe/data/verification/page-308.json\"\nwith io.open(p, \"w\", encoding=\"utf-8\") as f:\n    json.dump(data, f, ensure_ascii=False, indent=1)\n    f.write(\"\\n\")\nprint(\"written\", os.path.getsize(p))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk308.py && python3 -m json.tool data/verification/page-308.json > /dev/null && echo \"JSON OK\""
}
```


### [2026-09-06T23:33:16.997Z] TOOL RESULT

```
written 60790
JSON OK
```


## [2026-09-06T23:33:17.550Z] AGENT

You've hit your session limit · resets 9:30pm (America/Toronto)
