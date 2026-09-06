# Verification process log — verify-page-223


## [2026-09-06T15:14:18.104Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 223 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-223.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-223.json. Write /home/sfmqrb/git/rishe/data/verification/page-223.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 223` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T15:14:19.610Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T15:14:20.308Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T15:14:20.321Z] TOOL RESULT

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


## [2026-09-06T15:14:20.612Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-223.txt"
}
```


### [2026-09-06T15:14:20.642Z] TOOL RESULT

```
1	=== PDF page 223 (book page 193) ===
2	--- entry 0 ---
3	ROOT [Arabic] H.š.š : to dry (a vegetable or plant)  (refs FVA:102; KLN:706)
4	#1 (parent #0) [Arabic] refs=FVA:102; KLN:706 | hašîš : hemp ; Hašâšîn : hemp users, referred to the followers of Hasan Sabbâh who used to kill their political enemies after using Hashîsh.
5	  #2 (parent #1) [Persian] refs=FVA:102 | hašîš «حشیش» : hemp
6	  #3 (parent #1) [English] refs=KLN:706 | hašiš
7	  #4 (parent #1) [Italian] refs=None | assassino : murder
8	    #5 (parent #4) [English] refs=KLN:115; | assassin, assassinate
9	--- entry 1 ---
10	ROOT [Greek] Hyakinthos : a bulbous plant with a cluster of very fragrant flowers.  (refs AHD:644; KLN:752)
11	#1 (parent #0) [Pahlavi] refs=SNS:299 | yâkand : ruby
12	  #2 (parent #1) [Persian] refs=BQT:2420; MON:5247; MZF:340 | yâkand «یاکند» : ruby
13	    #3 (parent #2) [Arabic] refs=BQT:2420; SNS:299 | yâqŭt : ruby
14	      #4 (parent #3) [Persian] refs=SNS:299; FAF:712 | yâqŭt «یاقوت» : ruby, also red lips
15	#5 (parent #0) [Latin] refs=AHD:644 | hyacinthus : hyacinth
16	  #6 (parent #5) [French] refs=None | 
17	    #7 (parent #6) [English] refs=AHD | hyacinth
18	--- entry 2 ---
19	ROOT [Semitic] H.y.y : to live  (refs KLN:552; FVA:118)
20	#1 (parent #0) [Arabic] refs=KLN:552; FVA:118 | h.y.y : to live ; hayât : life ; hawwâ : the living being, Eve
21	  #2 (parent #1) [Persian] refs=FVA:118 | hayât «حیات ( حَیّ )» : life ; ehyâ «إحیاء» : to bring back to life, purify ; hayavân «حَیَوان» : living creature, animal ; havvâ «حوّا» : Eve
22	#3 (parent #0) [Hebrew] refs=KLN:552 | hawwâ : a living being, Adam's wife
23	  #4 (parent #3) [Latin] refs=KLN:552; AHD:453 | Eve
24	    #5 (parent #4) [English] refs=AHD:453 | Eve
25	
```


## [2026-09-06T15:14:24.385Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-223.json",
 "description": "Read page 223 source JSON"
}
```


### [2026-09-06T15:14:24.420Z] TOOL RESULT

```
{
  "pdf_page": 223,
  "book_page": 193,
  "entries": [
    {
      "root": {
        "name": "H.š.š",
        "lang": "Arabic",
        "refs": "FVA:102; KLN:706",
        "gloss": "to dry (a vegetable or plant)"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Arabic",
          "refs": "FVA:102; KLN:706",
          "words": [
            {"translit": "hašîš", "gloss": "hemp", "script": null},
            {"translit": "Hašâšîn", "gloss": "hemp users, referred to the followers of Hasan Sabbâh who used to kill their political enemies after using Hashîsh.", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "FVA:102",
          "words": [
            {"translit": "hašîš", "gloss": "hemp", "script": "حشیش"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "English",
          "refs": "KLN:706",
          "words": [
            {"translit": "hašiš", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 1,
          "lang": "Italian",
          "refs": null,
          "words": [
            {"translit": "assassino", "gloss": "murder", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": "KLN:115;",
          "words": [
            {"translit": "assassin, assassinate", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Hyakinthos",
        "lang": "Greek",
        "refs": "AHD:644; KLN:752",
        "gloss": "a bulbous plant with a cluster of very fragrant flowers.",
        "note": "The word is apparently a pre-Hellenic word of the Mediterranean origin. BQT:2420 and SNS:299 interpret the Greek word as \"a kind of poison\"."
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Pahlavi",
          "refs": "SNS:299",
          "words": [
            {"translit": "yâkand", "gloss": "ruby", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:2420; MON:5247; MZF:340",
          "words": [
            {"translit": "yâkand", "gloss": "ruby", "script": "یاکند"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Arabic",
          "refs": "BQT:2420; SNS:299",
          "words": [
            {"translit": "yâqŭt", "gloss": "ruby", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "SNS:299; FAF:712",
          "words": [
            {"translit": "yâqŭt", "gloss": "ruby, also red lips", "script": "یاقوت"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {"text": "ای خنده زده لعل تو بر حقّهٔ یاقوت - یاقوت لب لعل تو مرجان مرا قوت", "poet": "Safâî Qahfarrokhî"}
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD:644",
          "words": [
            {"translit": "hyacinthus", "gloss": "hyacinth", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "French",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "hyacinth", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "H.y.y",
        "lang": "Semitic",
        "refs": "KLN:552; FVA:118",
        "gloss": "to live"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Arabic",
          "refs": "KLN:552; FVA:118",
          "words": [
            {"translit": "h.y.y", "gloss": "to live", "script": null},
            {"translit": "hayât", "gloss": "life", "script": null},
            {"translit": "hawwâ", "gloss": "the living being, Eve", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "FVA:118",
          "words": [
            {"translit": "hayât", "gloss": "life", "script": "حیات ( حَیّ )"},
            {"translit": "ehyâ", "gloss": "to bring back to life, purify", "script": "إحیاء"},
            {"translit": "hayavân", "gloss": "living creature, animal", "script": "حَیَوان"},
            {"translit": "havvâ", "gloss": "Eve", "script": "حوّا"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {"text": "جان رفت در سَر می و حافظ ز عشق سوخت - عیسی دمی کجاست که احیای ما کند", "poet": "Hâfez"}
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Hebrew",
          "refs": "KLN:552",
          "words": [
            {"translit": "hawwâ", "gloss": "a living being, Adam's wife", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Latin",
          "refs": "KLN:552; AHD:453",
          "words": [
            {"translit": "Eve", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": "AHD:453",
          "words": [
            {"translit": "Eve", "gloss": null, "script": null}
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


## [2026-09-06T15:14:24.847Z] TOOL CALL #4: Bash

```json
{
 "command": "sed -n 1,200p data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-06T15:14:24.886Z] TOOL RESULT

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


## [2026-09-06T15:14:29.244Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['FVA','FVQ','KLN','AHD','SNS','BQT','MON','MZF','FAF']:\n    print('==',k, json.dumps(d.get(k),ensure_ascii=False)[:1200])\n\""
}
```


## [2026-09-06T15:14:29.988Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo --- && python3 -c \"\nimport json;d=json.load(open('data/verification/page-202.json'));print(json.dumps(d['entries'][0],ensure_ascii=False,indent=1)[:3000])\""
}
```


### [2026-09-06T15:14:30.987Z] TOOL RESULT

```
== FVA {"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: still no digital copy on any permitted platform. Library catalogues list the 1368 book under the variant title «فرهنگ ریشهٔ وام‌واژه‌های عربی (لغات عربی مستعمل در فارسی دخیل)» — reconcile with Nourai's title when buying. Catalogue record only."}
== FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt"], "page_offset": "printed page = leaf − 17 (0-based \\f blocks in FVQ_pages.txt; 335 leaves)", "covers_etymology": true, "notes": "Good English OCR (Arabic script garbled). Same 1938 edition Nourai cites.", "cites": "page number of Jeffery, The Foreign Vocabulary of the Qurʾān (1938)"}
== KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-styl
== AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt", "page_offset": "1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.", "lookup_hint": "Online: single page https://ahdictiona
== SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt"], "page_offset": "242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image", "covers_etymology": true, "notes": "OCR quality is POOR: Persian text mostly garbage, Latin transliterations partially readable. Verification will usually need the page image."}
== BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.com/file/8230741184/borhane_ghatee_jelde_4.pdf.html (م–ی, 553 pp), vol 5 https://s3.picofile.com/file/8230741300/borhane_ghatee_jelde_5.pdf.html (تعلیقات, Amir Kabir 5th pr. 1376, 293 pp). Same set behind login on ketabnak.com/book/55304-55307 and /58249.", "lookup_hint": "grep the headword in BQT_v1
== MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt", "/home/sfmqrb/git/rishe/data/verification/source
== MZF {"title": "P. Natel Khanlari — Table IV line garbled ('... darbareh Zaban-e Farsi', Sokhan 1340/1961; probably 'زبان‌شناسی و زبان فارسی')", "kind": "none", "url": null, "lookup_hint": "Not found (his تاریخ زبان فارسی is on archive.org as 1_20251010_20251010_2025 but is a different book).", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "none online; title uncertain."}
== FAF {"title": "A. Daneshgar, Farhang-e A'lam-e Farsi, Hafez Novin 1370/1991", "kind": "none", "url": null, "lookup_hint": "Not found.", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "none online. || RE-SEARCH 2026-09: nothing digitised on any permitted platform (archive.org, Google Books, Persian libraries/ebook stores). Check opac.nlai.ir manually / buy second-hand."}
```


### [2026-09-06T15:14:32.697Z] TOOL RESULT

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


## [2026-09-06T15:14:43.583Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i '^hashish\\|^hasheesh\\|hashish,\\|^assassin,\\|^assassinate\\|^Eve,\\|^hyacinth' KLN_1966.txt | head -40"
}
```


### [2026-09-06T15:14:43.662Z] TOOL RESULT

```
3675:assassin,  n.,  murderer.  —  F.,  fr.  It.  assassino,  fr. Arab,  hashshashln,  ‘drinkers  of  hashish',  fr. hashish,  ‘hemp’ ;  see  hashish.  The  first  assassins were  the  fanatic  followers  of  the  Shaykh-ul- Jabal  (the  Old  Man  of  the  Mountains),  who committed  their  murders  under  the  intoxication of  hashish.  The  plural  suff.  -in  in  assassin  was mistaken  for  part  of  the  word.  Cp.  Bedouin. Derivatives:  assassin-ate,  tr.  v.,  assassin-at- ion,  n.
13879:Eve,  1)  fem.  PN;  2)  in  the  Bible,  the  wife  of Adam.  —  Late  L.  Eva,  fr.  Heb.  Hawwdh,  lit. ‘a  living  being’,  from  the  base  of  hawi  —  hdyd, ‘he  lived’.  See  Gen.  3:20.  Heb.  hay&h,  ‘he  lived’, is  rel.  to  Aram.-Syr.  hayd,  ‘he  lived’,  Ugar.  hwy (hyy),  ‘to  live’,  Arab,  hayya,  ‘he  lived’,  Heb. hayytm,  Aram,  hayyfn,  hayyt,  Arab.  haydh, ‘life’.  Cp.  Eva.  Cp.  also  ave. evection,  n.,  irregularity  of  the  moon’s  motion in  its  orbit  ( astron .)  —  L.  evectio,  gen.  -dnis,  ‘a going  upward’,  fr.  evectus,  pp.  of  evehere,  ‘to carry  out’,  fr.  e-  and  vehere,  ‘to  carry,  convey’. See  vehicle  and  -ion.
17269:hashish,  n.,  an  intoxicating  drink  made  from hemp.  —  Arab,  hashish,  ‘hemp’,  prop,  ‘dried grass’,  rel.  to  Heb.  hashash,  ‘dried  grass’.  Cp. assassin.
18294:Hyacinthus,  n.,  a  beautiful  youth,  beloved  and slain  by  Apollo  (Greek  mythology).  —  L.  Hya¬ cinthus,  fr.  Gk.  'Taxiv^c,;.  See  hyacinth. Hyacinthus,  n.,  a  genus  of  plants  of  the  lily  family, the  hyacinth  ( bot .)  —  ModL.,  fr.  hyacinthus. See  hyacinth.
```


## [2026-09-06T15:14:43.841Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i 'hashish\\|hasheesh' KLN_1966.txt | head -20; echo ---; grep -n -i 'assassin' KLN_1966.txt | head -20"
}
```


### [2026-09-06T15:14:43.933Z] TOOL RESULT

```
3675:assassin,  n.,  murderer.  —  F.,  fr.  It.  assassino,  fr. Arab,  hashshashln,  ‘drinkers  of  hashish',  fr. hashish,  ‘hemp’ ;  see  hashish.  The  first  assassins were  the  fanatic  followers  of  the  Shaykh-ul- Jabal  (the  Old  Man  of  the  Mountains),  who committed  their  murders  under  the  intoxication of  hashish.  The  plural  suff.  -in  in  assassin  was mistaken  for  part  of  the  word.  Cp.  Bedouin. Derivatives:  assassin-ate,  tr.  v.,  assassin-at- ion,  n.
17269:hashish,  n.,  an  intoxicating  drink  made  from hemp.  —  Arab,  hashish,  ‘hemp’,  prop,  ‘dried grass’,  rel.  to  Heb.  hashash,  ‘dried  grass’.  Cp. assassin.
---
3675:assassin,  n.,  murderer.  —  F.,  fr.  It.  assassino,  fr. Arab,  hashshashln,  ‘drinkers  of  hashish',  fr. hashish,  ‘hemp’ ;  see  hashish.  The  first  assassins were  the  fanatic  followers  of  the  Shaykh-ul- Jabal  (the  Old  Man  of  the  Mountains),  who committed  their  murders  under  the  intoxication of  hashish.  The  plural  suff.  -in  in  assassin  was mistaken  for  part  of  the  word.  Cp.  Bedouin. Derivatives:  assassin-ate,  tr.  v.,  assassin-at- ion,  n.
4646:Bedouin,  n.  —  F.  bedouin,  fr.  Arab,  badawtn,  lit. ‘desert  dwellers’,  pi .  of  badawi,  fr.  badw  (in  vulgar pronunciation  bedu),  ‘camp;  desert’.  The  plural suff.  -in  in  Arab,  badawtn  was  mistaken  for  part of  the  word.  Cp.  assassin. bedraggle,  tr.  v.  —  Formed  fr.  be-  and  draggle, bedridden,  adj.  —  ME.  bedrede,  fr.  OE.  bedrida, lit.  ‘bed  rider’  (in  contradistinction  to  a  ‘horse rider’),  formed  fr.  bed  and  ridan,  ‘to  ride’.  See bed,  n.,  and  ride.
17269:hashish,  n.,  an  intoxicating  drink  made  from hemp.  —  Arab,  hashish,  ‘hemp’,  prop,  ‘dried grass’,  rel.  to  Heb.  hashash,  ‘dried  grass’.  Cp. assassin.
35118:Sibylline,  adj.,  pertaining  to  a  sibyl  or  the  sibyls. —  L.  Sibyllinus,  fr.  Sibylla.  See  prec.  word  and adj.  suff.  -ine  (representing  L.  -inus). sic,  adv.,  thus.  —  L.  sic,  ‘so,  thus’,  contracted from  the  older  form  sice,  for  si-ce,  which  is compounded  of  si,  ‘if’,  orig.  meaning  ‘so’,  and -ce,  an  emphatic  particle.  L.  si,  orig.  sei,  is  rel. to  Oscan  svai,  suae,  Umbrian  sve.  It.,  Sp.  and Port,  si,  ‘yes’,  F.  si,  ‘so’  (in  answer  to  a  neg. question)  ‘yes’,  derive  fr.  L.  sic.  Cp.  nisi,  quasi. For  the  etymology  of  the  L.  suff.  -ce  see  he.  Cp. the  first  element  in  cy-pres. sicarian,  n.,  an  assassin.  —  Formed  with  suff.  -an fr.  L.  sicarius,  ‘an  assassin,  murderer’,  fr.  sica,  ‘a curved  dagger’,  which  is  rel.  to  sicilis,  ‘a  sickle’ (prop,  ‘a  cutting  instrument’)  and  to  seed,  se- care,  ‘to  cut’.  See  section  and  cp.  sickle.  For  the ending  see  suff.  -ian.
```


## [2026-09-06T15:14:56.058Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\n# map line number -> leaf (count formfeeds before)\ntargets=[3675,13879,17269,18294]\nff=0\nfor i,l in enumerate(lines,1):\n    if i in targets:\n        print(i,'leaf',ff, 'approx printed pages', 2*(ff-12),2*(ff-12)+1)\n    ff+=l.count('\\f')\nEOF"
}
```


## [2026-09-06T15:14:56.648Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i '^hyacinth\\|hyacinth,  n' KLN_1966.txt | head; echo ---AHD---; grep -n -i 'hyacinth\\|Hyakinthos' AHD_watkins1985.txt | head"
}
```


### [2026-09-06T15:14:57.862Z] TOOL RESULT

```
3675 leaf 72 approx printed pages 120 121
13879 leaf 300 approx printed pages 576 577
17269 leaf 380 approx printed pages 736 737
18294 leaf 405 approx printed pages 786 787
```


### [2026-09-06T15:14:57.925Z] TOOL RESULT

```
18293:Derivatives:  huzza,  intr.  and  tr.  v.  and  n. hyacinth,  n„  1)  a  fabulous  flower  supposed  to have  sprung  from  the  blood  of  Hyacinthus (Greek  mythol.);  whence  2)  among  the  ancients, a  precious  stone  of  blue  color;  now,  a  red  or brownish  variety  of  zircon.  —  F.  hyacinthe,  fr. L.  hyacinthus,  a  kind  of  flower,  the  jacinth’,  fr. Gk.  udxivfto;,  ‘wild  hyacinth,  bluebell’,  fr.  ear¬ lier  *fdxiv$o;,  a  pre-Hellenic  word.  Cp.  Hya¬ cinthus.  Cp.  also  jacinth,  Vaccinium. hyacintbine,  adj.,  resembling  the  hyacinth  in color.  —  L.  hyacinthinus,  fr.  Gk.  uaxN&ivo;, fr.  udxiv$o;.  See  hyacinth  and  -ine  (representing Gk.  -Ivo;).
18294:Hyacinthus,  n.,  a  beautiful  youth,  beloved  and slain  by  Apollo  (Greek  mythology).  —  L.  Hya¬ cinthus,  fr.  Gk.  'Taxiv^c,;.  See  hyacinth. Hyacinthus,  n.,  a  genus  of  plants  of  the  lily  family, the  hyacinth  ( bot .)  —  ModL.,  fr.  hyacinthus. See  hyacinth.
---AHD---
```


## [2026-09-06T15:15:20.641Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in SKT.txt LKT.txt DEV.txt PHN.txt LAM.txt DOZ.txt HJB.txt FSD_vol1.txt FSD_vol2.txt WEB_vol1.txt; do echo \"=== $f\"; grep -n -i 'hashish\\|haschisch\\|assassin' $f | head -6; done"
}
```


## [2026-09-06T15:15:22.529Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FVQ yaqut\"; grep -n -i 'yaqut\\|yaqut\\|jacinth\\|ruby' FVQ_pages.txt | head -20; echo \"=== AFM\"; grep -n 'ياقوت\\|یاقوت' AFM.txt AFM_pages.txt | head -10; echo \"=== TAD\"; grep -n 'ياقوت\\|یاقوت' TAD.txt TAD_pages.txt | head -10"
}
```


### [2026-09-06T15:15:22.572Z] TOOL RESULT

```
=== SKT.txt
1048:AaBassiiL.asccrec  niunlerer.  (F.oAnk. F.  assassin.    From  Amb.  kashithitt, ers  of  *  ha5hish.*  the  name  of  a  »ecK ijth  century;  the 'Old  Man  of  the tain '  roused  his  followers'  spirits of  this  drink,   and  sctit  them  to citemies,  esp.  the  leading  v kashisk.  an  intoxtcitin^' the  OuMo^tr  ituii^a,  a  \.\-   ■•-■-
19657:Thug,  an  assassin.  (Hindustani.)  Hind. tha^,  M«if  (with  cerebral  th),  a  cheat,  knave, ft  rohber  who  strangles  travellexs  ;  ManLthi tkaJt,  tka^,  a  thug  (H.  H.  Wilson).
23702:French  from  Arabic:  admiral,  alcohol, assassin,  barberry  (berberry),  bedouin,  calif (caliph),  cipher,  civet,  fardel?,  furl?,  ga- zelle, lute  (1),  Mamaloke  (Mameluke), mattress,  mohair  (moiic),  saflron,  sultaa.
=== LKT.txt
2030:'Gras,  Heu',  später  beng  [s.  hier  Nr.  213] oder  indischer  Hanf,  Cannabis  indica [Über  den  indischen  Hanf  (Haschisch) und  seine  Verwendung  als  narkotisches Genußmittel.  In  Ausland  1863,  Nr.  30  j Ed.  Grimaux,  Du  hachich  ou  chanvre Indien.  Paris  1865];  in  die  europäischen Sprachen  ist  das  Wort  fast  unverändert übergegangen:  frz.  hachiche,  russ.  gasiSf dtsch.  Haschisch.  —  „In  Syrien  steht der  Hasis,  ein  berauschendes  Hanf-  oder Mohnpräparat,  welches  unvermengt  ge- nossen oder  dem  Tabak  beigemengt wird,  bei  den  niederen  Ständen  in Gunst.  Das  Schimpfwort  hassäs  ent- spricht unserem  'Trunkenbold'.  Keines- wegs ist  das  Laster  des  Haschischrauchens derart  verbreitet  wie  bei  uns  der  Ge- nuß der  Spirituosen.  Weit  mehr  als  in Syrien  und  Mesopotamien  ist  das  Hanf-
2033:rauchen  in  Ägypten  verbreitet.  In Marokko  wird  der  Hanf  klf  genannt, klein  geiiackt  und  mit  Tabak  vermischt oder  auch  unvermengt  in  winzig  kleinen Tonköpfchen  aus  etwa  1  Fuß  langen Pfeifen  sehr  viel  geraucht."  Max  Frei- herr V.  Oppenheim,  Vom  Mittelmeer  zum Persischen  Golf  I,  74.  Genaueres  über die  in  Marokko  benutzten  Pfeifen  und die  Art  des  Hanfrauchens  sowie  die  ar. Ausdrücke  dafür  vgl.  MSOS  H,  231 u.  232.  —  Auf  das  oben  erwähnte haMM  hat  SILVESTRE  DE  SAGY  ein weit  verbreitetes  romanisches  Wort zurückgeführt  [de  S.,  Memoire  sur  la dynastie  des  Assassins  et  sur  l'origine de  leur  nom.  Lu  ä  la  seance  publique de  l'Institut  du  7  juillet  1809.  Im  Mo- niteur  no.  210,  an  1809  und  Lettre  de M.  de  S.  au  redacteur  du  Moniteur  sur I'etymologie  du  nom  des  Assassins. Ebenda  no.  359,  an  1809].  Aus  der  Ge- schichte der  Kreuzzüge  ist  der  ,AIte vom  Berge"  bekannt,  der  das  Haupt einer  Sekte  war,  deren  neue  Mitglieder, durch  den  Hanfrausch  fanatisiert,  auf Befehl  ihrer  Obern  selbst  Mordtaten begingen;  aus  dem  ar.  Namen  dieser Sekte  hassäsln  entstand  it.  assassino 'Meuchelmörder',  prov.  asasi,  ansesi, frz.  assassin,  sp.  asesino,  pg.  assassino, rum.  asasin  und  die  dazugehörigen Verba  assassinare  usw.  und  andere  Ab- leitungen. It.  (dial.  Parma)  sasinä  'be- raubt, elend;  Weinbergschnecke'.  — Autiallend  ist,  daß  in  allen  Formen  die beiden  s  verschwunden  sind,  daher schlägt  Lammens  Rem  28  als  Grund- wort den  Namen  des  Gründers  jener meuchelmörderischen  Sekte,  Hasan  ihn §abäh,  vor;  jedoch  scheint  diese  An- nahme nicht  notwendig,  da  im  MA Namen,  die  über  das  Lateinische  ver- breitet wurden,  allgemein  das  s  durch einfaches  s  ersetzten.  [DE  207.  Egui- laz  293.   ML  4074.
4208:razene,  sarazenisch';  engl,  saroccn,  sa- racenie,  dtsch.  Sarazene,  sarazenisch. [Andere  Ableitungen  von  ar.  sarräg, das  aber  nicht  'Reiter',  sondern  'Sattler' heißt,  oder  von  särikln  'Diebe'  sind nicht  annehmbar,  vgl.  Lettre  de  M.  Silv. de  Sacy  au  rödacteur  du  Moniteur  sur l'etymologie  du  nom  des  Assassins.  Im Moniteur,'  an  1809,  no.  359,  pg.  5/6,] [DE  241/243.  Devic  DEt  72.  Lammens Rem.  57/58.    Eguilaz  348.    ML  7595.
5008:Guttapercha  712 jffafcö  792 ifa^M»  GiVai  800 i/am  1157 Harakiri  818 Harmelraute  829 Harün  ar-Rasid  605 Hasan  ibn  Sabäh  839 Haschisch  839 Hedschra  863 Hildegard  v.  Bingen  795 Hobson-Jobson  835 Holothuria  edulis  2096 ifw^fta  655
5781:Hadschi  111 Haferei  138 Hniduck  781 ifa/«Z}  59  d Haifagras  796 Harakiri  818 iJf/r^w  819 Hasard(spiel)  2186 Haschisch  839 hasehart  mhd.  2186 Hassagai  2181 Havarie  138 Hedschra  863 helmbarte  mhd.  823 Dorrfe  1594 Hosanna  872 ÄMr«  848 hurra(h)  2167
6339:alphanette  582 alphinic  683 alquifoux  1227 aludel  2142 alvarde  242 amalgame  1378 aman  66 amhre  78 amhrette  762  b nmiral  69  a amire  afz.  69  a amuUte  866 amulette  866 anafin  1537 andouille  355 angrec  82 «wii  1568 <iw<t/f(;  20ö8 antimoine  918 arabe(sque)  89 «ra^  92 arcawne  867 archine  108 argali  96 argousin  2160 aWeie  100 ar»m  112 armadie  1343 armoise(ur)  1596 armo(i)sin  1596 «rra^e?  1708 arrofee  1725 arsenal  495 artichaut  833 ar^iei  95 assassin  839 assogue  2208 »thanor  2019 a^fcar  2075 a«a6a?  1971 ffM&^e  874 aubergine  161 «MCTtöe  afz.  1221 uufage  afz.  586.  777 auferrant  afz.  586 aw/fe  796 au^n  afz.  605 auforget  884 «M^r^  135
=== DEV.txt
561:Assassin.  Quoi  qu'en  dise  l'annotateur  du  voyage  de Benjamin  de  Tudèle,  dans  la  collection  des  Voyages  anciens et  modernes  publiée  par  M.  Charton^,  personne  ne  doute aujourd'hui  que  le  nom  à^Assassins  donné  aux  Ismaéliens ou  Bathéniens  ne  soit  l'adjectif  arabe  ^Liw^.  hac/iâchï  ou ^^vl^AÂMo».  hachiclil,  dérivé  de  ,j^^i*.s^  hachich,  le  hachich (voy.  ce  mot),  boisson  enivrante  qui  jouait  un  rôle  im- portant dans  la  fanatisation   de  ces  terribles  sectaires  \
568:Le  nom  des  HaclulcJn  a  été  apporté  en  France  par  les Croisés  sous  la  forme  Assaci  qu'on  lit  dans  Joinville.  L'es- pagnol asesfïw  et  le  portugais  assassina  ne  semblent  pas empruntés  directement  à  l'arabe,  mais  reçus  par  l'inter- médiaire du  français  ou  de  l'italien  assassino^.  Le  Diction- naire de  Du  Gange  cite  les  formes  de  bas  latin  heissesin, assassij  assassuii,  assesini^  etc.
569:M.  Defrémery  a  publié  en  i85/i,  dans  le  Journal  asia- tique, de  très-intéressantes  recherches  sur  les  Assassins.
2809:Asesino,  esp.  voy.  Assassin.
2813:Assaci,  voy.  Assassin.
2815:Assassi,  b.  lat.  voy.  Assassin.
=== PHN.txt
1450:dable par son savoir et sa générosité. Il fut assassiné par un
1885:ASSASSIN , s. m. (a.)
1897:eldjebel, en 1190. Les assassins de la Perse furent détraits
3588:Voyez au mot Assassin. — Il suffit d'ajouter une s au singulier
3789:parlant d*un sectaire qui devient assassin par fanatisme : c'est
5611:(lue dérive le mot français assassin. — J'écris hachiche avec un
=== LAM.txt
290:est le plus souvent omise : Alep, assassin, alcool (j) autre-
456:assassin (i), lascar ;x {k l'imitation des Espagnols) : axir*
1870:étrange que dans toutes les formes du mot assassin les
1871:deux ^J» ch aient disparu. En dérivant assassin de Hassan-
3378:Assassins, on Ht dans les Lettres édifiantes i «Nos vieux
3381:les Assassins choisissent pour prince le plus ancien
=== DOZ.txt
=== HJB.txt
2764:BANG,  BHANG,  s.  H.  hhdnq,  the dried  leaves  and  small  stalks  of  hemp {i.e.  Cannabis  indica),  used  to  cause intoxication,  either  by  smoking,  or when  eaten  mixed  up  into  a  sweetmeat ^see  MAJOON).  Hashish  of  the  Ara1)s is  substantially  the  same ;  Birdwood says  it  "consists  of  the  tender  tops of  the  plants  after  flowering."  {Bhang is  usually  derived  from  Skt.  bhangay 'breaking,'  but  Burton  derives  both it  and  the  Ar.  banj  from  the  old  (Joptic Ntbanjy  "meaning  a  preparation  of hemp  ;  and  here  it  is  easy  to  recognise the  Homeric  Nepenthe."
2765:"On  the  other  hand,  not  a  few  apply  the word  to  the  henbane  (hyoacyamn*  ntger)  so much  used  in  mediaeyal  Europe.  The  KiCmds evidently  means  henbane,  aistinguishing  it from  Hashish  al  hardfish,  *■  rascal's  grass,'  i.r. the  herb  Pantagruelion.  .  .  The  use  of  Bhang doubtless  dates  from  the  dawn  of  civilisation, whose  earliest  social  pleasures  would  be  in- ebriants.  Herodotus  (iy.  c.  75)  shows  the^ Scythians  burning  the  seeds  (leaves  and capsules)  in  worship  and  becoming  drunk upon  the  fumes,  as  do  the  S.  African  Bush- men of  the  present  day." — {Arab,  Nights, i.  66.)]
2767:1578. — "Baojnie  is  a  plant  resembling hemp,  or  the  Cannabis  of  the  Latins  .  .  . the  Arabs  call  this  Bangne  *Axi**"  (i.e. Hashish).— C.  Aeosta,  860-61. '  1598.— "They  have  ....  also  many  kinds of  Drogues,  as  Amfion,  or  Opium,  <>imfora> Bangne  and  Sandall  Wood." — Linschoten, IdTlBak,  Soc.  i.  61 ;  also  see  ii.  115].
2782:As  Hashish  dressed,  its  magic  powers '    Can  lap  us  in  Elysian  bowers ;
9176:1781. — (After  an  account  of  an  alleged attempt  to  seize  Mr.  Hicky 's  Dano&n).  *  *  Mr. Hicky  bess  leave  to  make  the  following  re- marks. That  he  is  clearly  of  opinion  that these  horrid  Assassins  wanted  to  dispatch him  whilst  he  lay  a  sleep,  as  a  DooT-YOn  is well  known  to  be  the  alarm  of  the  House,  to prevent  which  the  Villians  wanted  to  carry him  off, — and  their  predpitate  flight  the moment  they  heard  Mr.  Hicky's  Voice  puts it  past  a  Doubt." — Reflections  on  the  con- sequence of  the  late  attempt  made  to Assassinate  the  Printer  of  the  original  Ben- gal OczetU  (in  the  same,  April  14).
14664:an  attempt  was  made  to  Assassinate  him last  Thunday  Morning  between  the  Hours of  One  and  two  o'Qock,  by  two  armed Europeans  aided  and  assistea  by  a  Moor- man. .  .  ."— J7«%'«  Bengal  OazetU,  April  7.
=== FSD_vol1.txt
6705:The  assassin  and  his  wretched  acolyte  came  at  midnight. Nicolat  and  Hat  A.  Lincoln  vol,  x,  ch.  14,  p.  307.  [c.  co.  1890.J
12503:Al-ma'gro,  1   al-ms'gro;  2   al-mS'gro,  n.  1.  Diego  de (14757-1538),  a   Spanish  soldier  in  Peru.  2.  Diego  dc, "   the  Lad  "   (15207- V«1542),  his  son,  assassin  ol  Pliatto.
25951:Ar'tliur,  1   Gr'thur;  2   ilr'thflr,  n.  1*  A   masculine  personal name.  F,  Ar"tbur>*  l   or'tflr\  2Ur'tttr',  Ar"tus%  1   ar'tfis', 2   Hr'tus';  It.  Ar-tu'ro,  1   ar-ta'ro,  2   iir-tu'ro;  L.  Ar-thti'- rus,  1   ar-CblQ'rtis,  2   iir-thfi'rfis.  2.  Ono  of  the  last  of  tho British  chieftains  who  struggled  against  tho  Anglo-Saxon power  In  the  Oth  century.  It  Is  Impossible  to  discrimi- nate between  tho  historical  and  the  legendnry  In  the  caso of  Arthur,  as  a   vast  amount  of  mythical  romance  has clustered  around  his  name,  and  has  been  Immortalized In  Celtic,  English,  and  French  poetry,  forming  the  subject of  agreat  partof  the Mabinooion,  of  Malory’s Mortcd' Arthur, and  of  Tennyson’s  poem,  Idylls  of  the  King.  All  that  Is historically  certain  Is  that  Arthur  defended  West  Britain against  the  Saxons  and  was  killed  In  a   decisive  battle  fought cither  at  Camlan  In  Cornwall  or  Mountbadon  In  Somerset- shire in  the  year  520.  The  Welsh  long  cherished  the  belief thnt  Arthur  had  been  miraculously  transported  to  Fairy- land and  would  one  day  return  to  lead  them  to  victory. For  Arthur’s  famous  sword  see  ExcALimm;  for  his  company of  knights  see  Knights  of  the  Round  Tarle.  3.  (Vt»1187- V*1203).  Son  of  Geoffrey  Plantagcnct;  nephew  of  IClngJolm of  England;  said  to  have  been  murdered  by  his  uncle  at Itoucn,  Normandy;  Introduced  in  Shakespeare's  King  John. 4.  Chester  Alan  (»y»l830-“/iil88G),  21st  President  of  tho United  States:  succeeded  on  the  assassination  of  President Garfield.  [Celt.,  high.]
26959:(Apocrypha,  margin).  1   Mac.  Iv,  16. as-snrt',  1   a-sffrt';  2   fi-eart',  rt.  [Eng.]  To  grub  or  clear of  trees  or  bushes  so  as  to  make  arable:  said  of  forest-lands; also,  to  hoe  or  grub  up:  said  of  trees  or  bushes.  l<  OF. essartcr,  <   LL.  exsarto,  <   L.  cx,  out,  +   sario,  grub.] ns-sart',  n.  The  act  of  assarting;  the  land,  or  any  tree  or bush,  that  has  been  assarted, as-sas'slnt,  r.  To  assassinate.
26963:2.  fA-]  One  of  a   sect  of  Oriental  fanatics  that  prac- tised assassination;  the  original  meaning.
26964:The  sect  was  founded  In  Persia  A.  D.  1090,  but  afterward migrated  to  Mt.  Lebanon.  Syria.  Its  head  was  known  as the  Old  Man  of  the  Mountain  and  was  supposed  to  be  In- vested with  divine  authority.  Tho  Assassins  became  for- midable during  the  crusades,  but  were  suppressed  by  Bi- bars, sultan  of  Egypt,  In  1272.  [F.,  <   Ar.  Hashshashln,
=== FSD_vol2.txt
5840:Els'ner,  1   als’ner;  3   Is'ner,  Kurt  (r/  nl867-V!iI019).  Ger- man statesman;  premier  of  Bavarian  republic;  assassinated, el-su'dl-a,  ci-sod'i-eoii,  n.  Bauie  as  ihodia,  etc. el-sod'ie,  1   a!-sed'!k;  2   i-'-.Od'ic.  n.  HAi/sW.  Same  a-s  esodi(\ eis-tedd'fO(i,  1   ols-tetii'vud;  2Is-tfith'v6d,  re.  [-fo'd.vu,  1 -vd'dau;  2 -vo'duu,  ph]  [W.]  An  as.?en)bly  of  bards  and others  held  annually  in  Widea,  and  sometimes  in  othe,’- countries  where  Wel.«h  people  re.side,  for  the  cultivation of  the  national,  mu.slcal,  and  literary  inte-rest.s  of  people of  Welsh  descent.  In  its  present  form  the  eisteddfod  has  been held  more  or  Jess  regul.-irly  since  1819,  but  the  institiition can  be  clearly  traced  to  the  12th  century,  ehs-tedd'vodi. —   cls-tedd'fod-lsin,  re.  ,   s.
6972:-j-bet'.  2   e-li-sii-bt'L':  It.  E-U'"sa-bot'ta,  1   t!-tl''za-bet'ta, 2   e-li'sa-bet'tii,  A-B'sat;  L.  Ii-ll2"a-beth'a,  1   i-Ii:!*o- both'3,  2   e-!Iz”a-beih'a;  Sp.  I"’s.a-bei',  1   rsa-bcl',  2   ("sa- bSl'.  3.  Bib.  Mother  of  John  tlie  Baptist.  3.  E.  cf Austria  (‘2/silS37-^>/ioI898),  erapre.ss;  wife  of  likancis Joseph  I.,  assassinated.  4.  JG.  of  York  (®/iil4fi5-s/iil003), daughter  of  Elizabeth  Woodviile;  wife  of  Henry  \II.  of England;  mother  of  Henry  VIII.  5.  Pauline  E.  Ottllle Luisc  (’Vaol.SlS-VslOKi).  Prlnees.s  of  Wied  and  queen  of Koumania;  story»writer  and  poet:  pon.name,  “   Carmen Bylva”;  Shadows  of  Life’s  Dial.  6.  Petrovna  (>V  =91703- 1/S17G2),  empress  of  Ru.s.sia;  daughter  of  Peter  the  Great; founded  Academy  of  Fine  Arts,  St.  Petersburg,  and  Uni- versity of  Moscow:  opposed  E'rederick  the  Great  in  tiie Seven  Years’  war,  her  troops  entering  Berlin,  1700.  7. Saint,  of  Hungary  (1207-U/I91231),  daugliter  of  Andrew II,  of  Hungary:  practised  extreme  asceticism.  8.  Stuart (s/-io90— /ial662),  queen  of  Bohemia;  daughter  of  James I.  and  sister  of  Charles  I.  of  England;  married  Fredurielc V..  Elector  Palatine;  mother  of  Prince  Rupert  and  the Eleetress  Sophia  (mother  of  George  I.  of  England).  !). Tudor  (»/7l533-^/jilG03),  queen  of  England:  daughter  of Henry  VIII.  and  Anne  Boleyn;  reestablished  Eefoniied faith.  10.  Woodvlile  (1431?-»/9l492),  wife  of  Sir  John Grey,  then  of  Edward  IV.  of  England;  died  In  a   nunnery; Introduced  In  Shakespeare’s  Jiichard  III,  11.  A   city, county»seat  of  Union  county,  N.  J,  13.  A   borough  la Alleghany  county.  Pa.  [Gr.,  from  Heb.  Elisheba,  wor- shiper of  God  (God  is  her  oath).]
7778:'We  have  room  and  hoHoitalify  for  «rn’cr(i7i(a  who  come  to  our  to  the  Interior  and  was  assassinated  by  Arabs, shores  to  hett.cr  their  eondition  by  the  adoption  of  our  eitizenship.  C-mir',  1   C-mtr';  2   e-nur',  W.  1.  Any  independent  prince, Deplw  Orations  and  .S’pi.i;cA(,a,  Feb.  ss,  1SS8  D.  49.  [c.to.  co.  1890.1  chieftain,  or  Commander  in  the  Mohammedan  East’,  as,
11992:car'pous,  a.  Bot  Having  red  fruit,  as  certain  lichens.  Republic;  signer  of  Armlsttce.  Nov.  11,  1918;  assassinated.
26052:name.  Frank!.  Dan.  Frants*  1   fronts,  2   frants;  Dan.  D. Fran-cis'eus,  1   tran-sts'kus,  2   Iran-cis'eCs;  F.  Fran"cols', frdn'swo',  2   irafl'swii';  G.  Fran-cis'ens,  1   fron-tsls'ktis, 2   friin-tsls'ous;  Franzt;  It.  Fran-ces'eo,  1   fran-tfhes'ko, 2   fran-ches'eo;  Fran'eot;  Pg,  Fran-cls'co,  1   Imn-sis'ko,  2 fran-cis'eo;  Sp.  Fran-cis'eo,  1   fran-tols'ko,  S   Iriin-thla'co: Sw.  Frans,  1   frans;  2 frans.  2.  F.  I.  (s  'ul494- V3a547),  a king  of  France:  met  Henry  VIII.  on  “   Field  of  the  Cloth  of Gold”:  persecuted  Protestants.  3.  F.  II.  (VislS44-"/« 1560),  a   king  of  France;  married  Mary  Queen  of  Scots. 4.F.  L, Stephan  of  Ixirralne  Ci»/il708-»/ial765),  emperor of  Holy  Roman  Empire:  married  Maria  Theresa.  6.  F. Ferdinand  ('',-!slS63~Vnl914),  the  Archduke  of  Austria- Este;  assassinated  with  his  wife  at  Scrajevo.  6.  F.  Joseph
31266:1   jiir'ji-us,  2   6<5i''fd-Os;  PK.  Jwr'Jte,  1   sSfsb.  2   zliSr'zho;  Sp, Jor'gc,  1   hOr'he,  S   hOrihe.  2.  G.  I.,  tlther  of  two  k!ng.s: (1)  Ia?w1s  (v::8lii(10-'>,'isl727),  king  of  England;  elector  of Hanover.  (2)  Christian  William  Ferdinand  Adolphus f‘V!4lS4u-Vi8l9l3j,  king  of  Greece  from  l.WJ;  assassinated at  Salonlkl.  3.  G.II.  CD  Auguslus  (•ViolOS.3-‘V!sl7fiO) , king  of  England:  son  of  George  I.;  fought  at  Oudenarde and  Dettlngcn.  (2)  (’/wlSfiO-  ),  eldc-st  son  of  cx-KIng Constantine  of  Greece:  IClng  of  Greece,  Sept.  27,  1922-24. 4.  G.  III.,  William  Frederick  (Vd7a8->/5alS20),  king of  England;  ruled  during  American  Revolution.  S.  G. IV.,  Augustus  Frederick  (»/iil7e2->/5sl530),  king  of England:  son  of  George  HI.  6.  G.,  Frince  of  Denmark (‘,'j3lBS3-“/t»1708),  consort  of  Queen  Anno  of  England.  7. G.V.,  either  of  two  kings;  (1)  ('/[jl819-«  isl87S).  last  king of  Hanover;  dethroned  1866.  (2)  Frederick  Ernest
=== WEB_vol1.txt
12033:as-sas/sin, n. (Fr. assassin, from Ar. hashsha- shin, hashish eaters, from hashish, hemp.]
12034:1. [A-], a member of a secret band of hashish-eating Moslems who killed Christian leaders during the Crusades.
12036:as-sas/sin, v.t. to assassinate. [Obs.]
12037:as-sas/sin-ate, v.l.; assassinated, pt.. pp,; as- sassinating, ppr. 1. to murder by surprise or secret assault, as an assassin does.
12040:as-sas/sin-ate, n. an assassination or an assas- sin. [Obs.]
12041:as-sas-si-na/tion, n. an assassinating or being assassinated; the act of killing or murdering, by surprise or secret assault.
```


### [2026-09-06T15:15:22.663Z] TOOL RESULT

```
=== FVQ yaqut
317:Yaqut. Mu'jam al-Buldan, ed. Wustenfeld, 6 vols. Leipzig, 1866-1870.
401:Yaqut, Mu'jatn, iii, 664, to the effect that on a certain occasion he sacrificed a ewe to
602:Yaqut's Irshad, ii, 6, and for his works, Fihrist, 80 ; Hajjl Khalifa, 770 ; anjl Flugel,
1266:4 We learn also of a tribe Banu Hadal (or Handal or Bahdal), cf. Yaqut Mu'jam,
1272:8 Shammakh, Divan, ed. Shanqlti, p. 26 ; Yaqut, Alu'jam, i, 907.
1273:fl Yaqut, Mu'jam, ii, 504 ff.
1274:10 Yaqut, Mu'jam, iii, 856, 857 ; Abu Da'ud, Sunan, xix, 26.24 INTRODUCTION
2997:fern, name of more than three radicals (cf. Yaqut, Mu'jam, i, 447). 2
4093:Ta'I mentioned by Yaqut, ii, 270, and celebrated in a verse of Abu
4115:3 Yaqut, Mrijam, ii, 144 ; Mas'udI, Muruj, i, 74 ; Ibn Batuta, ii, 139 ; Qazwmi,
4189:with /%**> which Yaqut collects in his Mu'jam are in Syria : secondly
4839:Yaqut, Mu l jam, iv, 70 ; and vide Noldeke, Ohassanischen Fursten, p. 8.
5390:a Ibn Athlr, Chron, xi, 259 ; Yaqut, Mu'jam, ii, 804.
5450:called because of their eagerness to capture Constantinople (Yaqut,
5452:150, and Yaqut ii, 861. Others, however, recognized the word as
6897:in Aghdrii, xx, 97, and in Yaqut, Mu'jam, iii, 356, we have mention
8547:Yaqut, Mu'jam, iv, 79). Another theory derived the name from a
8556:scoffed at by Yaqut, but is accepted by at-Tabari and al-Damiri, 2 and
8728:222, thinks that by JaJ ai-A'sha means the Gospel) ; and Mutalamrais in Yaqut,
10075:Yaqut, Mu'jam, iv, 729 ; Raghib, Mufrarlat, 514 ; aUi-Tha'labl, Q wo/ f 272.
=== AFM
=== TAD
```


## [2026-09-06T15:15:29.918Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FVQ ruby/jacinth\"; grep -n -i 'ruby\\|jacinth\\|Yaqut,\\|yaquf' FVQ_pages.txt | grep -iv \"Mu'jam\\|Irshad\" | head -20; echo \"=== AFM sample\"; head -c 400 AFM.txt; echo; echo \"=== TAD sample\"; head -c 400 TAD.txt"
}
```


### [2026-09-06T15:15:30.018Z] TOOL RESULT

```
=== FVQ ruby/jacinth
401:Yaqut, Mu'jatn, iii, 664, to the effect that on a certain occasion he sacrificed a ewe to
1272:8 Shammakh, Divan, ed. Shanqlti, p. 26 ; Yaqut, Alu'jam, i, 907.
4093:Ta'I mentioned by Yaqut, ii, 270, and celebrated in a verse of Abu
4115:3 Yaqut, Mrijam, ii, 144 ; Mas'udI, Muruj, i, 74 ; Ibn Batuta, ii, 139 ; Qazwmi,
4839:Yaqut, Mu l jam, iv, 70 ; and vide Noldeke, Ohassanischen Fursten, p. 8.
5450:called because of their eagerness to capture Constantinople (Yaqut,
8556:scoffed at by Yaqut, but is accepted by at-Tabari and al-Damiri, 2 and
8728:222, thinks that by JaJ ai-A'sha means the Gospel) ; and Mutalamrais in Yaqut,
10378:Ruby.
=== AFM sample
8 


0 
ܥܝ 


ܶܡ 7 
ܫ ܢ 0 ܣܚ 
.ܡܨ >  )‏ اعم ܨ 
3 ܛ 5 62 ܨ ܗ 

ܡ 5 

1 ` < 3[ 
1 , 3 5 ܢ 
ل ܨ( : : 
`( × 2 7 : ̄ܡ 

ܝ 2 -. و 

/ ܪ ܇ ܐ ܢ 
. ܥ يبد < ܲܗ 

ܘܨ ܝ ܓ 


بي بهم 0 1 1 
ܗܨ . ܢ 1 ` 
ܙ ^ ܢܢ 
9 ܪ 1 .° 2 
3 0 : 
1 : ܫ" 
ܫ ܠ 1 ܨܢ 7 1 
" ܐ . ܢ 
ܨ.܀ .ܝ 4 ܙ ܗܩ 1 
ل رار ܨ 
هيه ܘ 
ܫ @ < ܟ 
227 5 ܪܐ 8 
` ܫ ܨ 
ܡ ܨܝ ب
=== TAD sample
الف 
8 َ نبي بى اكابى اللبناك 


لحتل 


- اا لدم 
: 7 تت 1 1 ظ 
ا مون 
هني بنشره وتصحيحه وتعليق <واشيه 
ا 


الو مان 


ده ل دام 


« طبعة ثانية 6 


حل ' 


ذكرى الذ ممردص 
الى من حك العل ويغاد على الاادب الى الكير بروحه ونكرة 
وقلبه ؛ الى من �
```


## [2026-09-06T15:15:32.045Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD yakand\"; grep -n -i 'yakand\\|yākand\\|yʾknd' PHD.txt PHD_mackenzie.txt | head; echo \"=== NYB\"; grep -n -i 'yakand' NYB_vol2_glossary.txt | head; echo \"=== SNS\"; grep -n -i 'yakand\\|yakan\\|yʾknd' SNS.txt SNS_pages.txt | head"
}
```


### [2026-09-06T15:15:32.140Z] TOOL RESULT

```
=== PHD yakand
PHD.txt:669:yakand [5^ knd, -nt' | Р ykwnd, N ~] ruby. yal [57 | N ~] hero.
PHD.txt:3485:ruby yakand.
PHD.txt:5564:gāwars dānistan appar-! appurdan! dānišnūmand dānišn jahūd yākand yākand
PHD_mackenzie.txt:5687:yakand [y)knd, -ntl I P y)kwnd, N --] ruby.
PHD_mackenzie.txt:7497:ruby yakand.                               scented boyag, boydiir.
PHD_mackenzie.txt:11007:yakand                         ~\Y'U             awurdan                  \\~\"tU-"U
PHD_mackenzie.txt:11008:yakand                        ''P\~              dan-
=== NYB
=== SNS
```


## [2026-09-06T15:15:37.501Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '10360,10400p' FVQ_pages.txt"
}
```


### [2026-09-06T15:15:37.594Z] TOOL RESULT

```
and we find references to them in the early poetry, where the statements
about them would indicate that knowledge of them came to Arabia
1 West, Glossary, 237. It was a fairly common word, and enters into a number
of compounds ; cf. Nyberg, Qlossar, 242.
2 Bartholomae, AIW, 1438 ; Reichelt, Awestisches Elementarbuch, 490.
3 Hiibschmann, Arm. Gramm, i, 248 ; Spiegel, Huzvaresh Grammatik, Wien, 1856,
p. 188.
* Vullers,Zes,ii, 1411.
6 Vullers, Lex, ii, 1000 ; Horn, Qrundriss, 242 ; Hubschmann, Pers. Studien, 94.FOREIGN VOCABULARY OP THE QTJR S AN 289
from Christian eschatological writings. 1 The names, of course, were
originally Heb. 313 and 3130, which in Syr. are ..CU and yt ^^ - I n
the Syriac Alexander legend ..0,1 is generally spelled yt^vjlL 2 which is
a variant reading of the word in the Qur'an (Noldeke, Qorans, 270).
The Mandaean demons Hag and Mag, which Horovitz, 7P2V,163, quotes,
are more likely to be derived from the Qur'an than the Qur'anic
names from them. 3
(Ydqul).
Iv, 58.
Ruby.
It was very generally recognized as a loan-word from Persian. 4
Some Western scholars such as Freytag 5 have accepted this at face
value, but the matter is not so simple, for the Modern Pers. O^Su is
from the Arabic (Vullors, Lex, ii, 1507), and the alternative form AlJ u,
like the Arm. jui^ai^ 9 is from the Syr. JjJOQj. 6
The ultimate source of the word is the Gk. vaxivdos, used as a
flower name as early as the Iliad, 7 and which passed into the Semitic
languages, cf. Aram. ]1B3 l 'p <l 8 ; Syr. lAjQQji, and into Arm. as
juiltfilift-. 9 It was from Syr. ]AjQQji that the word passed into
Eth. as flillV and with dropping of the weak 3 into Arabic. 11
It occurs in the old poetry (cf. Gcyer, Zwei Gedichte, i, 119), ancfthus
must have been an early borrowing.
I Noldeke, Alfjranderroman, passim ; Mingana, Syriac Influence, 95 ; Geiger, 74,
however, would derive the names from Rabbinic legend. See Horovitz, KU, 150.
Cf. Budge's edition of the metrical discourse of Jacob of Serug in ZA, vi, 357 if.
See on them Lidzbarski, Ginza, p. 154 ; Brandt, Mandaiftche Schriften, p. 144.
al- Jawallqi, Mu'arrab, 156 ; ath-Tha*alibi, Fiqh, 317 ; as-Suyutf, Itq, 325 ;
Mu aw, 47, 48 ; al-KhafajI, 216 ; TA, i, 598.
Lexicon, sub voc.
Noldeke in Bessenberger's Beitrdge, iv, 63 ; Brockelmann, ZDMG, xlvii, 7.
II, xiv, 348. Boissacq, 996, points out that the word is pre-Hellenic.
For other forms see Krauss, Griechische Lehntvorter, ii, 212.
```


## [2026-09-06T15:15:38.427Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i 'hyacinth\\|Yaqut\\b' FVQ.txt | tail -20; echo \"=== search yaqut entry\"; grep -n -i \"^\\s*[Yy]aqut\" FVQ_pages.txt | head"
}
```


### [2026-09-06T15:15:38.501Z] TOOL RESULT

```
710:Yaqut, Mu'jatn, iii, 664, to the effect that on a certain occasion he sacrificed a ewe to 
1000:Yaqut's Irshad, ii, 6, and for his works, Fihrist, 80 ; Hajjl Khalifa, 770 ; anjl Flugel, 
1966:4 We learn also of a tribe Banu Hadal (or Handal or Bahdal), cf. Yaqut Mu'jam, 
1976:8 Shammakh, Divan, ed. Shanqlti, p. 26 ; Yaqut, Alu'jam, i, 907. 
1977:fl Yaqut, Mu'jam, ii, 504 ff. 
1979:10 Yaqut, Mu'jam, iii, 856, 857 ; Abu Da'ud, Sunan, xix, 26. 
4962:fern, name of more than three radicals (cf. Yaqut, Mu'jam, i, 447). 2 
6928:Ta'I mentioned by Yaqut, ii, 270, and celebrated in a verse of Abu 
6964:3 Yaqut, Mrijam, ii, 144 ; Mas'udI, Muruj, i, 74 ; Ibn Batuta, ii, 139 ; Qazwmi, 
7104:with /%**> which Yaqut collects in his Mu'jam are in Syria : secondly 
8215:Yaqut, Mu l jam, iv, 70 ; and vide Noldeke, Ohassanischen Fursten, p. 8. 
9185:a Ibn Athlr, Chron, xi, 259 ; Yaqut, Mu'jam, ii, 804. 
9297:called because of their eagerness to capture Constantinople (Yaqut, 
9299:150, and Yaqut ii, 861. Others, however, recognized the word as 
11834:in Aghdrii, xx, 97, and in Yaqut, Mu'jam, iii, 356, we have mention 
14770:Yaqut, Mu'jam, iv, 79). Another theory derived the name from a 
14786:scoffed at by Yaqut, but is accepted by at-Tabari and al-Damiri, 2 and 
15085:222, thinks that by JaJ ai-A'sha means the Gospel) ; and Mutalamrais in Yaqut, 
17537:Yaqut, Mu'jam, iv, 729 ; Raghib, Mufrarlat, 514 ; aUi-Tha'labl, Q wo/ f 272. 
18239:The name would seem to mean helper (Yaqut, Mu'jam, iv, 1022), 
=== search yaqut entry
317:Yaqut. Mu'jam al-Buldan, ed. Wustenfeld, 6 vols. Leipzig, 1866-1870.
401:Yaqut, Mu'jatn, iii, 664, to the effect that on a certain occasion he sacrificed a ewe to
602:Yaqut's Irshad, ii, 6, and for his works, Fihrist, 80 ; Hajjl Khalifa, 770 ; anjl Flugel,
4839:Yaqut, Mu l jam, iv, 70 ; and vide Noldeke, Ohassanischen Fursten, p. 8.
8547:Yaqut, Mu'jam, iv, 79). Another theory derived the name from a
10075:Yaqut, Mu'jam, iv, 729 ; Raghib, Mufrarlat, 514 ; aUi-Tha'labl, Q wo/ f 272.
```


## [2026-09-06T15:15:59.348Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('FVQ_pages.txt',encoding='utf-8',errors='replace').read()\ni=t.find('The ultimate source of the word is the Gk.')\nprint('leaf(0-based ff blocks before):', t[:i].count('\\f'))\nEOF\necho \"=== BQT v4 yakand/yaqut\"; grep -n 'یاکند\\|یاقوت' incoming/BQT/BQT_v4_pages.txt | head -20"
}
```


### [2026-09-06T15:16:01.085Z] TOOL RESULT

```
leaf(0-based ff blocks before): 306
=== BQT v4 yakand/yaqut
6590:‏۴۳- یاقوت در ممجم‌البلدان هردو شهر را « میمند > بکس میم اول وفتح میم دوم ضبط
11331:شینه ممجمة وآخره راء وهی قربة بلج وقیل قسر» وچنانکه دیده میشود یاقوت نیز حرق‌آلس .
13858:رك : وخشور . یاقوت کوید : ۵ وخش ( بفتح اول ) شهری است از لواحی بلخ از ختلان » و آن
17296:یاقوت در معجم‌البلدان ( چاپ مطبمةالسعادة: مصر.طبع اول ۱۳۹۳ ج ۱ ص۲۷ بیمد ) بتفصیل از
20533:ی زکویند که پاوء باشد۹ . یاقوت مذاب؟ - کنابه از قراب
20536:گرم وخشك‌است درچهارم؛ وقایم‌النار بمنیآتش باقوت ناروان « یاقوت رمانی ۴
20538:طاعو نکند . یاکنده « بفتح‌کاف پروزن‌یابند, بمعنی
20539:یاقوت خام - با خای قطه داربالف باقوت است وآن جوهری باشد معووف .
20541:یاقوت روان - کنایه ازاخشخوین مطلقاً اعم ا زکردن انسان وحیوان دیگر وبعربی
20552:۴ - «قال حمزة بن‌الحن‌الاسفهانی‌ان اسمه (الیاقوت) بالفارسية *, کند»(ء.م.)والیاقوت
20559:8 - رك: باقوت . «یاکند پاقوت باشد . شا کر بخاری گفت:
```


## [2026-09-06T15:16:01.398Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PLA\"; grep -n -i 'yaqut\\|yāqūt\\|Rubin\\|yakand' incoming/PLA/PLA_pages.txt | head -20; echo \"=== ARB mo3rb\"; grep -n 'ياقوت' ARB_mo3rb.txt ARB_abdulraheem.txt | head -10; echo \"=== MON\"; grep -n 'یاکند\\|ياكند' MON_part2.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt | head -10"
}
```


### [2026-09-06T15:16:01.497Z] TOOL RESULT

```
=== PLA
2630:      Ballasrubin °-
3362:          dtsch.       Ballasrubin                    °. s.       badahsan,
3365:5b - balah8:                      "Rubin"           pers.,        mand.        balk.*-
3869:las, -          bißädag:        "Rubin"          aus    dem pers.              sl». bigäde             7,
6700:15.    Yaqut          Bd.        2 S.        517.
10691:3.    Yaqut          Bd.     3 S.          435.
11624:5.   Yaqut      Bd.    3 S.        885,       Nyberg     Bd.    II     ss.    v.
13529:JJ-     la’l:        "Rubin"             pers.               s.        läla.
=== ARB mo3rb
ARB_mo3rb.txt:1059:معجم الأدبا لياقوت 6ه وا 
ARB_mo3rb.txt:1149:و سنة هام ٠‏ فقك نقل ياقوت فى ترحمته فى معجم الأدباء :ب" عن ألى سعد 
ARB_mo3rb.txt:1164:وما أشيه ذلك . قال مؤلف هل ذا الاب أى ياقوت - وهذا الاعتذار 
ARB_mo3rb.txt:1198:السمعانى فى الأنساب وياقوت فى معجم الأدباء واين خلكان فى الوفيات تارم 
ARB_mo3rb.txt:1200:تلدأ التاق » إذ هو متصر كاءةه وياقوت وان خلكان قإدا السمعاق رظنا 
ARB_mo3rb.txt:1469:فر بيع الأول منة باوو» هكذا قال ياقوت فى 56 ب وعم ولكنه قال أيضا 
ARB_mo3rb.txt:1652:كاب ” لمعب » وغيره مر تصانيفه » ٠‏ وقال ياقوت فى معجم الأدباء : 
ARB_mo3rb.txt:1733:ونقل ياقوت فى معجم الأدباء عن أبنه أبى ممد |سمعيل بن موهوب قال : 
ARB_mo3rb.txt:1905:. ول أجد ذكرًا لهذا الكتاب فيا بين يدى» من المراجع ٠‏ وقد قال ياقوت بعد نسمية 
ARB_mo3rb.txt:1929:وقإدهما فى ذلك ابن خلكان وابن الأثير فى اللباب وياقوت ٠‏ وقال ابن الأثير 
=== MON
```


## [2026-09-06T15:16:09.301Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '20525,20575p' incoming/BQT/BQT_v4_pages.txt; echo \"=== page tags nearby ===\"; awk 'NR>=20400 && NR<=20600 && /pdf page/' incoming/BQT/BQT_v4_pages.txt"
}
```


### [2026-09-06T15:16:11.017Z] TOOL RESULT

```
بقیه از حاشيهٌ صفحهٌ قبل
را مخصوص سوسن‌سفید داسته‌اند... وجمهوراطیا تعریف باسمین‌نموده‌اند که درخت اومانند درخت
مورد واملی, برکش نرمتر ویهن‌تر و بنطبری بر که مورد لیست . درخت قسم مفید او ضیف
وگلش مفید و با شایبهٌ مرخی وبسیار خوشبوی وازوقت شکفتن لرکس تا اول عقرب کل میدهد
ودر بلاد حاره همیشه » ودرخت نوع زرد او عظیم و چتری ومانند درخت موز است » وتزد بسنی
قم زره ار مسمي پزایق اسی...» «تحقهٌ حکیم مژمن».
[pdf page 503]
باقوت سید نها
ی زکویند که پاوء باشد۹ . یاقوت مذاب؟ - کنابه از قراب
باقوت؟ « با فاف بروزن هاروت ؛ بام | لعلی- واغك خونی باشد - وکنایه از خون هم
جوهرست مشهور و آن سرخ وکبود وزردمیباشد. ۱ هت ومربی دم خوانند ۱
گرم وخشك‌است درچهارم؛ وقایم‌النار بمنیآتش باقوت ناروان « یاقوت رمانی ۴
اورا ضایع نمیکند وبا خود داشتن آن دفع‌علت راکوبند. وآن لوعی است ازباقوت.
طاعو نکند . یاکنده « بفتح‌کاف پروزن‌یابند, بمعنی
یاقوت خام - با خای قطه داربالف باقوت است وآن جوهری باشد معووف .
کشیده وبمیم زده, کنایه از لب معفوق‌است . یال - بروزت بال » بمعنی کردن باشد
یاقوت روان - کنایه ازاخشخوین مطلقاً اعم ا زکردن انسان وحیوان دیگر وبعربی
شراب لملی باشد عنق کوبند؟ - و بیخ کردترا نیز گفته اند -
5 باقو بسته . وبمعنتی بازوهم آمده است که آزدوش‌باشد تامرفق-
یافوت سر بحمه - کنایه از | ومو ی کردن اسب را نیز کوبند - وبمعنی‌فرزند
ممشوق - ولبهای خاموش باشد. | وعیال هم هست۷ - ومستی حیوانات را نیز یال
۱ - نافهراکیمخت رنگین‌سرزشها کرد و گفت:
يك بد ردگی دداری صورت زیبای من.
افه گفتش: یافه کم کو کایت معنی‌مراست
واینك اينك حجت کوبا دم بوبای من .
«خاقانی شروانی ص۳۲۹ ۰

۴ - «قال حمزة بن‌الحن‌الاسفهانی‌ان اسمه (الیاقوت) بالفارسية *, کند»(ء.م.)والیاقوت
معربه ...؟ «بیرونی. الجماهرص۳۳*. پاقوت ازبونانی 81618808[ (بمعنی نوعی‌از زهی) » در
اسطلاح علمی 867/۳82108 1718 ونیز 20172:0818 18010105ق «نخب‌الذغاثر ص۲ ح۱>
درلانینی 18/80111818 «تفی» برای اطلاع ازانواع باقوت, ر: الجماهر بیرونی ص۳۲ ببعد +

۴ - (عر) کداخته. رك : مذاب. ۴ - رك : الجماهرپیرونی ۰۵۹۰۸۹۰۳۶۰۳۳

8 - رك: باقوت . «یاکند پاقوت باشد . شا کر بخاری گفت:

کجا تو باشی کردند بی‌خطر خوبان جست‌را چه خطرهر کجا بود پا کند؟»
«لفت‌فری ص۹۳ (ایضاً صحاح الفرس تسغخة طاعتی)-
‎٩‏ - «یال, کردن باشد. عنصری (بلخی) کوید:
از او رسیده پتو تقد صد هزار درم زبنده بودن او چون کشید شاید پال؟
فردوسی (طوسی) کوید :
بدین کتف و این قوت پال او شوکشته رستم بچنگال او .>
« لفت فرس ۰۶۳۱۱
(و رك : صحاح‌الفری سغهٌ طامتی).
۷ - مخقف «عیال» (عر) و «بالمند» (ه.م.) مخفف عیالمنداست :
ضیف پالمندم تنگستم چه خوالم داستان رامی وویس؟
سوزتی‌سمرقندی «جهانگیری».
پودم حکیم سوزبي از چند سال باز با پالمند گفتم گشتم تحکمی .
موزلی‌سرقندی «جهانگیری*
[pdf page 504]
-4۲۱- بان
=== page tags nearby ===
[pdf page 500]
[pdf page 501]
[pdf page 502]
[pdf page 503]
[pdf page 504]
```


## [2026-09-06T15:16:27.316Z] TOOL CALL #20: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:2420 --image 2>&1 | tail -40"
}
```


### [2026-09-06T15:16:34.640Z] TOOL RESULT

```
جوهرست مشهوروآن سرخ و کبود وزردمیباشد. ۱ هنت وبعری دم خوانند ۱
گرم وخشك‌است درچهارم, وقایم‌الثار بمنیآتش باقوت ناروات » یاترت رمای ۳
اورا ضایع نمیکند وبا خود داشتن آن دفع‌علت | راگوبند. وآن نوعی است ازباقوت.
طاعون کند . پا کند* - بنتح‌کاف بروزن‌پابندهبمعنی
باقوت خام - با خای شله راربازن | باقوت است وآن جوهری باشد معروف .
کشیده وبمیم زده» کنایه از لب معشوق‌است . یال « بروزن بال » بمعنی کردن باشد
یاقوت روان - کنابه ازاوری., .۱۱ مطلفاً ام ازکردن اسان وحیوان دیگر وبمربی
شراب لملی باشد 7 عنق کوبندا - و بیخ گردترا نیز کفته اند -
- پم 1 نسته ۱ وبمعنی بازوهم آمده‌است که آزدوش‌باشد تامرفق-
یاقوت سرب ه کنایه از | وموی کردن اسب را نیز گوبند - وبمعنی‌فرزند
معشوق - ولیپای خاموش باشد. | وعیال هم هست۷ - ومتی حبوانات را نیز پال
۱ - نافه‌را کیمخت رنگن‌سرزشها کرد و گفت:
ليك بد ردگی دداری صورت زببای من.
بافه گفتش: بافه کم گو کایت معنی‌مراست
واينك اينك حجت کویا دم بوبای من .
«خاقانی شروانی ص۳۲۹ ۰

۴ - «قال حمزة بن‌الحن‌الاسفهانی‌ان اسمه (الیافوت) بالفارسية «,ا کند»(.م.) والیاقوت
معربه ...* «یبرونی. الجماهرص۳۳». پافوت ازبونانی 12286181808 (بمعنی نوعی‌از زهی) » در
اسطلاح علمی 867۵۸۵108 1218 وییز 201۳:۵۵19 812010105 «یخب‌الذخاثر ۲ ح۱»
درلانینی 3[/8601818158 «تفی» برای اطلاع ازانواع باقوت, ر4: الجماهر پیرونی ص۳۲ بیعد .

۴ (عر) گداخته. رد : مذاب. ۴ - رك : الجماهر بدرونی ماهنت ند هس

8 - ر4: پاقوت . «یاکند پاقوت باشد . شا کر بخاری گفت:

کجا تو باشی کردند بی‌خطر خوبان جمت‌را چه خطرهر کجا بود با کند؟»
«لفت‌فرس ص۹۳ (ایضاً صحاح الفرس نسخهٌ طاعتی).
- «بال» کردن باشد. عنصری (بلخی) کوید:
از او رسیده بو نقد صد هزار درم زبنده بودن او چون کشید شاید پال؟
فردوسی (طوسی) گوید :
بدین کنف و این قوت یال او شو دکشته رستم بچنگال او .»
لفت فری ۳۱
(و رك : محاح‌الفری نخهٌ طاعتی).
۷ - مخفف «عیال» (عر) و «یالمند» (.م.) مخفف میالمنداست :
ضمیفم پالمندم تنگستم چه خوالم داستان رأمی وویس؟
سوزنی‌سمرقندی «چهانگیری».
بودم حکیم سوزبي از چند سال باز با پالمنه گشتم کشتم تحکمی .
سوزلی‌سمرقندی دجهانگیری*
```


## [2026-09-06T15:16:42.082Z] TOOL CALL #21: Bash

```json
{
 "command": "ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/ 2>/dev/null | grep 2420"
}
```


### [2026-09-06T15:16:42.157Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb 161891 Sep  6 11:16 2420.png
-rw-rw-r--  1 sfmqrb sfmqrb   3629 Sep  6 11:16 2420.txt
```


## [2026-09-06T15:16:45.864Z] TOOL CALL #22: Bash

```json
{
 "command": "python3 -c \"\nfrom PIL import Image\nim=Image.open('data/verification/sources/refs/ocr/BQT/2420.png')\nprint(im.size)\nw,h=im.size\n# crop bottom half where footnote 4 is\nim.crop((0,int(h*0.45),w,int(h*0.72))).resize((int(w*1.6),int(h*0.27*1.6))).save('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqt2420_fn.png')\n\""
}
```


### [2026-09-06T15:16:48.013Z] TOOL RESULT

```
(1650, 2546)
```


## [2026-09-06T15:16:49.926Z] TOOL CALL #23: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqt2420_fn.png"
}
```


### [2026-09-06T15:16:50.210Z] TOOL RESULT

```

```


## [2026-09-06T15:16:50.207Z] INPUT

[Image: original 2640x1099, displayed at 2000x833. Multiply coordinates by 1.32 to map to original image.]


## [2026-09-06T15:17:27.977Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && mkdir -p ocr/BQT && cat > ocr/BQT/2420.vision.txt <<'EOF'\n[Borhan-e Qate', ed. Mo'in, printed page 2420 (BQT_v4 pdf page 503) — read from the page image\n data/verification/sources/refs/ocr/BQT/2420.png; the machine OCR misreads several words.]\n\nColumn text (headwords):\nیاقوت - با قاف بروزن هاروت، نام جوهری‌ست مشهور و آن سرخ و کبود و زرد می‌باشد. گرم و خشک است\n  در چهارم، و قایم‌النار بمعنی آتش او را ضایع نمی‌کند و با خود داشتن آن دفع علت طاعون کند.\nیاقوت خام - ... کنایه از لب معشوق است.\nیاقوت روان - کنایه از شراب لعلی ...\nیاقوت مذاب - کنایه از شراب ...\nیاقوت رمانی - و آن نوعی است از یاقوت.\nیاکند - بفتح کاف بروزن یابند، بمعنی یاقوت است و آن جوهری باشد معروف.\n\nFootnote 2 (Mo'in's etymological note, verbatim):\n«قال حمزة بن الحسن الاصفهانی ان اسمه (الیاقوت) بالفارسیة «یاکند» (ه.م.) والیاقوت معربه ...»\n«بیرونی. الجماهر ص۳۳». یاقوت از یونانی hyakinthos (بمعنی نوعی از زهر)، در اصطلاح علمی\nIris germanica و نیز gladiolus communis «نخب‌الذخائر ص۲ ح۱» در لاتینی hyacinthus «نفس»\nبرای اطلاع از انواع یاقوت، رک: الجماهر بیرونی ص۳۲ ببعد.\n\n  [NB: «نوعی از زهر» here = \"a kind of BLOSSOM/flower\" (Ar. زهر «flower»), not \"poison\" —\n   confirmed by the two botanical identifications Mo'in gives, Iris germanica and\n   Gladiolus communis, both flowers.]\n\nFootnote 5:\n۵ - رک: یاقوت. «یاکند یاقوت باشد. شاکر بخاری گفت:\n   کجا تو باشی گردند بی‌خطر خوبان / جمست را چه خطر هر کجا بود یاکند؟»\n«لغت فرس ص۹۳» (ایضاً صحاح الفرس نسخهٔ طاعتی).\nEOF\necho written; grep -rn 'یاقوت\\|یاکند' MON_part2.txt | head -5; echo \"=== SNS wide\"; grep -n -i 'yak\\|yaq' SNS.txt | head -20"
}
```


### [2026-09-06T15:17:29.635Z] TOOL RESULT

```
written
MON_part2.txt:6183:معدنی (لعل. یاقوت و غیره). فرزند خاور: 
MON_part2.txt:62080:الادویه). مفرح یاقوت: (پز.) نوعی شراب 
MON_part2.txt:74347:(آهن» مس طلاء نقره» لعل» یاقوت). نتیجه 
MON_part2.txt:80668:یاقوت‌های سبز که در زنجیری زرین گدشته 
MON_part2.txt:93377:یاقوت: ۷2۰(.) (زم.) یکی از سنگ‌های 
=== SNS wide
3692:tj(,fc :&) . W ^ityfc . cxKi'jJ • *fi^ « j'j^ :ajrryak: -3-^ 
6740:( \j_»- :^) yak / Svak: JIM 
6778:yak :^, S6«tt^c«^i **->- j&l* (.Mir.Man. I, 44) 
16320:Uyacinthus w* hyakinthos : „»V3U»«* *1JWtf 
17055:-^i*3'3j-»^ yezI.syaQais :j^-*S:yezI: — ?S* 
17174:.^:yak: 3j 
17176:.*/Yl^ .,/«( :yak-5: -»-»3l> (*^.i)A-*/Y^ (**<***>) 
17177:.*,/•<)£ {^h f> -^)^*-:3 yak: -*£_>" 
17180:£kto.l282)yakrt : ^j^- ySkara -/ySkar- : fc- 
28332:yakrt 317/7 
28777:patyaka- 142/6 
29226:yakar- 317/ 7 
30808:yak/Svak 91/18-317 
31397:si yak-S 10/10 
33885:ajfryak 37/17
```


## [2026-09-06T15:17:30.245Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN yakand/yaqut\"; grep -n -i 'jāḳand\\|jakand\\|jāqūt\\|jakut\\|yakand' HRN.txt HUB.txt | head; echo \"=== SIN\"; grep -n -i 'yakand\\|yaqut' SIN.txt | head; echo \"=== ISS\"; grep -n -i 'yakand' ISS_alt_DKS.txt | head; echo \"=== NYB2\"; grep -n -i 'yakand\\|ykwnd' NYB_vol1.txt NYB_vol2_glossary.txt | head"
}
```


### [2026-09-06T15:17:30.349Z] TOOL RESULT

```
=== HRN yakand/yaqut
HUB.txt:5305:yakand *Rubin aus dem Aramaischen (syr. X*U1p% XH^Ip^ usw.,
=== SIN
1393:The  ancient  Chinese  attribute  saffron  not  only  to  Kashmir,  but  also to  Sasanian  Persia.  The  Lou  Su1  enumerates  yti-kin  among  the  products of  Po-se  (Persia) ;  so  does  the  Sui  $u?  In  fact,  Crocus  occurs  in  Persia spontaneously,  and  its  cultivation  must  date  from  an  early  period. Aeschylus  alludes  to  the  saffron-yellow  footgear  of  King  Darius.3 Saffron  is  mentioned  in  Pahlavi  literature  (above,  p.  193).  The  plant  is well  attested  for  Derbend,  Ispahan,  and  Transoxania  in  the  tenth century  by  Istaxri  and  Edrisi.4  Yaqut  mentions  saffron  as  the  principal production  of  Rud-Derawer  in  the  province  Jebal,  the  ancient  Media, whence  it  was  largely  exported.6  Abu  Mansur  describes  it  under  the Arabic  name  zafardn.6  The  Armenian  consumers  esteem  most  highly the  saffron  of  Khorasan,  which,  however,  is  marketed  in  such  small quantities  that  the  Persians  themselves  must  fill  the  demand  with exportations  from  the  Caucasus.7  According  to  Schlimmer,8  part  of the  Persian  saffron  comes  from  Baku  in  Russia,  another  part  is  culti- vated in  Persia  in  the  district  of  Kain,  but  in  quantity  insufficient  to fill  the  demand.  In  two  places, — Rudzabar  (identical  with  the  above Rud-Derawer),  a  mountainous  tract  near  Hamadan,  and  Mount Derbend,  where  saffron  cultivation  had  been  indicated  by  previous writers, — he  was  unable  to  find  a  trace  of  it.
1896:ana.  From  these  data  Hehn1  infers  that  under  the  rule  of  the  Persians, and  possibly  inconsequence  of  their  rule,  rice-cultivation  advanced  from the  Indus  to  the  Euphrates,  and  that  from  there  came  also  the  Greek name  5pv£ a.  This  rice-cultivation,  however,  can  have  been  but  sporadic and  along  the  outskirts  of  Iran;  it  did  not  affect  Persia  as  a  whole.  The Chinese  verdict  of  "no  rice"  in  Sasanian  Persia  appears  to  me  con- clusive, and  it  further  seems  to  me  that  only  from  the  Arabic  period did  the  cultivation  of  rice  become  more  general  in  Persia.  This  con- clusion is  in  harmony  with  the  account  of  Hwi  Cao  sal  M.,  a  traveller in  the  beginning  of  the  eighth  century,  who  reports  in  regard  to  the people  of  Mohammedan  Persia  that  they  subsist  only  on  pastry  and meat,  but  have  also  rice,  which  is  ground  and  made  into  cakes.2  This conveys  the  impression  that  rice  then  was  not  a  staple  food,  but  merely a  side-issue  of  minor  importance.  Yaqut  mentions  rice  for  the  prov- inces Khuzistan  and  Sabur.3  Abu  Mansur,  whose  work  is  largely  based on  Arabic  sources,  is  the  first  Persian  author  to  discuss  fully  the  subject of  rice.4  Solely  a  New-Persian  word  for  "rice"  is  known,  namely  birinj or  gurinj  (Armenian  and  Ossetic  brinj),  which  is  usually  regarded  as  a loan-word  from  Sanskrit  vrlhi;  Afghan  vriie  (with  Greek  5puf o,  (}pl£ a) is  still  nearer  to  the  latter.  In  view  of  the  historical  situation,  the reconstruction  of  an  Avestan  *verenja5  or  an  Iranian  *vrinji,6  and  the theory  of  an  originally  Aryan  word  for  "rice,"  seem  to  me  inadmissible.
1931:the  Christians  of  the  city  Gundes&pur,  which  was  in  connection  with India  and  cultivated  Indian  medicine,  should  have  propagated  the cane  and  promoted  the  sugar-industry.  This  is  no  more  than  an  in- genious speculation,  which,  however,  is  not  substantiated  by  any documents.  The  facts  in  the  case  are  merely,  that  according  to  the Armenian  historian  Moses  of  Khorene,  who  wrote  in  the  second  half of  the  fifth  century,  sugar-cane  was  cultivated  in  Elymais  near  GundS- sapur,  and  that  later  Arabic  writers,  like  Ibn  Haukal,  MuqaddasI, and  Yaqut,  mention  the  cultivation  of  the  cane  and  the  manufacture of  sugar  in  certain  parts  of  Persia.  The  above  Chinese  notice  is  of  some importance  in  showing  that  sugar  was  known  under  the  Sasanians  in the  sixth  century.  The  Arabs,  as  is  well  known,  took  a  profound  inter- est in  the  sugar-industry  after  the  conquest  of  Persia  (a.d.  640),  and disseminated  the  cane  to  Palestine,  Syria,  Egypt,  etc.  The  Chinese owe  nothing  to  the  Persians  as  regards  the  technique  of  sugar-pro- duction. In  a.d.  647  the  Emperor  T'ai  Tsun  was  anxious  to  learn  its secrets,  and  sent  a  mission  to  Magadha  in  India  to  study  there  the process  of  boiling  sugar,  and  this  method  was  adopted  by  the  sugar- cane growers  of  Yan-eou.  The  color  and  taste  of  this  product  then  were superior  to  that  of  India.1  The  art  of  refining  sugar  was  taught  the Chinese  as  late  as  the  Mongol  period  by  men  from  Cairo.2
2041:East-African  coast.  The  early  texts  relating  to  Ta  Ts'in  do  not  mention the  palm;  but  at  the  end  of  the  article  Fu-lin  (Syria),  the  T'an  Su  speaks of  two  countries,  M  ffl  Mo-lin  (*Mwa-lin,  Mwa-rin)  and  ^  f#  H Lao-p'o-sa  (*Lav-bwi5-sar),  as  being  situated  2000  li  south-west  of Fu-lin,  and  sheltering  a  dark-complexioned  population.  The  land  is barren,  the  people  feed  their  horses  on  dried  fish,  and  they  themselves subsist  on  dates.1  Bretschneider2  was  quite  right  in  seeking  this locality  in  Africa,  but  it  is  impossible  to  accept  his  suggestion  that "perhaps  the  Chinese  names  Mo-lin  and  Lao-p'o-sa  are  intended  to express  the  country  of  the  Moors  (Mauritania)  or  Lybia."  Hirth3 did  not  discuss  this  weak  theory,  and,  while  locating  the  countries in  question  along  the  west  coast  of  the  Red  Sea,  did  not  attempt  to identify  the  transcriptions.  According  to  Ma  Twan-lin,  the  country Mo-lin  is  situated  south-west  of  the  country  ?&  H  H  Yan-sa-lo,  which Hirth  tentatively  equated  with  Jerusalem.  This  is  out  of  the  question, as  Yah-sa-lo  answers  to  an  ancient  Ah-sa5(sar)-la(ra).4  Moreover,  it is  on  record  in  the  T%ai  pHn  hwan  yii  ki5  that  Mo-lin  is  south-west  of #  II  $1  P'o-sa-lo  (*Bwi5-sa5-la),  so  that  this  name  is  clearly  identical with  that  of  Ma  Twan-lin  and  the  transcription  of  the  T'ang  Annals. In  my  opinion,  the  transcription  *Mwa-lin  is  intended  for  the  Malindi of  Edrlsl  or  Mulanda  of  Yaqut,  now  Malindi,  south  of  the  Equator,  in Seyidieh  Province  of  British  East  Africa.  Edrlsl  describes  this  place as  a  large  city,  the  inhabitants  of  which  live  by  hunting  and  fishing. They  salt  sea-fish  for  trade,  and  also  exploit  iron-mines,  iron  being  the source  of  their  wealth.6  If  this  identification  be  correct,  the  geographical definition  of  the  T'ang  Annals  (2000  It  south-west  of  Fu-lin)  is,  of  course, deficient;  but  we  must  not  lose  sight  of  the  fact  that  these  data  rest on  a  hearsay  report  hailing  from  Fu-lin,  and  that,  generally  speaking, Chinese  calculations  of  distances  on  sea-routes  are  not  to  be  taken  too seriously.7  Under  the  Ming,  the  same  country  appears  as  jfefc  ^  Ma-lin, the  king  of  which  sent  an  embassy  to  China  in  141 5  with  a  gift  of
2396:The  Arabs  distinguish  three  varieties  of  carob,  two  of  which  are named  saidalani  and  fabuni.2  There  is  no  doubt  that  the  Arabs  who were  active  in  transplanting  the  tree  to  the*  west  conveyed  it  also  to Persia.  A.  de  Candolle  does  not  mention  the  occurrence  of  the  carob in  that  country.  It  is  pointed  out,  however,  by  the  Mohammedan writers  on  Persia.  It  is  mentioned  as  a  cultivation  of  the  province Sab  Or  by  MuqaddasI3  and  Yaqut.4  Abu  Mansur  discusses  the  medicinal properties  of  the  fruit  in  his  pharmacopoeia;  he  speaks  of  a  Syrian  and a  Nabathaean  xarnub?  Schlimmer6  remarks  that  the  tree  is  very common  in  the  forest  of  Gilan;  the  pods  serve  the  cows  as  food,  and  are made  into  a  sweet  and  agreeable  syrup.  No  Sanskrit  name  for  the tree  exists,  and  the  tree  itself  did  not  anciently  occur  in  India.7
3096:Persian  sakirlat,  sagirlat,  has  been  placed  on  a  par  with  Chinese sa-ha-la  by  T.  Watters8  and  A.  Houtum-Schindler;9  it  is  not  this Persian  word,  however,  that  is  at  the  root  of  Chinese  sa-ha-la,  but saqalat  or  saqalldt,  also  saqalat,  saqalldf  ("scarlet  cloth").  Dr.  E.  D. Ross10  has  been  so  fortunate  as  to  discover  in  a  Chinese-Persian  vocabu- lary of  1549  the  equation:  Chinese  sa-ha-la  =  Persian  saqalat.  This  settles the  problem  definitely.  There  is,  further,  Persian  saqldfiin  or  saqldfin, said  to  mean  "a  city  in  Rum  where  scarlet  cloth  is  made,  scarlet  cloth or  dress  made  from  it."  The  latter  name  is  mentioned  as  early  as a.d.  1040  and  1 150  by  Baihaki  and  Edrlsi  respectively.11  According  to Edrisi,  it  was  a  silk  product  of  Almeria  in  Spain,  which  is  doubtless meant  by  the  city  of  Rum.   Yaqut  tells  of  its  manufacture  in  Tabriz,
3193:Sal  ammoniac  is  found  in  Dimindan  in  the  province  of  Kirman. Yaqut  (1179-1229)  gives  after  Ibn  al-Faqih  (tenth  century)  a  descrip- tion of  how  nuladir  is  obtained  there,  which  in  the  translation  of  C. Barbier  de  Meynard2  runs  as  follows: —
3211:According  to  Yaqut,  mines  of  antimony,  known  under  the  name razi,  litharge,  lead,  and  vitriol,  were  in  the  environs  of  Donbawend  or Demawend  in  the  province  of  Kirman.2  In  the  Persian  pharmacopoeia of  Abu  Mansur,  the  medicinal  properties  of  litharge  are  described  under the  Arabicized  name  murddsanj,  to  which  he  adds  the  synonymous  term murtak*  Pegoletti,  in  the  fourteenth  century,  gives  the  word  with  a popular  etymology  as  morda  sangue*  The  Dictionary  of  Four  Lan- guages5 correlates  Chinese  mi-Vo-sen  with  Tibetan  gser-zil  (literally, "gold  brightness"),6  Manchu  lirlan,  and  Mongol  jildunur.7
3621:9.  Abu  Mansur  discriminates  between  two  kinds  of  rhubarb, —  the Chinese  (rlwand-i  stni)  and  that  of  Khorasan,  adding  that  the  former is  most  employed.4  Accordingly  a  species  of  rhubarb  (probably  Rheum ribes)  must  have  been  indigenous  to  Persia.  Yaqut  says  that  the  finest kind  grew  in  the  soil  of  Nlsapur.5  According  to  E.  Boissier,6  Rheum ribes  occurs  near  Van  and  in  Agerowdagh  in  Armenia,  on  Mount  Pir Omar  Gudrun  in  Kurdistan,  in  the  Daena  Mountain  of  eastern  Persia, near  Persepolis,  in  the  province  Aderbeijan  in  northern  Persia,  and  in the  mountains  of  Baluchistan.  There  is  a  general  Iranian  name  for "rhubarb":  Middle  Persian  rewas,  New  Persian  rewas,  rewand,  riwand (hence  Armenian  erevant),  Kurd  riwas,  rlbas;  Baluci  ravaS;  Afghan rawa!!;. ,7  The  Persian  name  has  penetrated  in  the  same  form  into  Arabic
5292:Yaqut,  320,  373,  377.  389.  425.  497.  507, 509,  547-
=== ISS
=== NYB2
NYB_vol1.txt:9202:a’ y ^nuyngbn: dayakandniban
```


## [2026-09-06T15:17:37.329Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HUB context\"; sed -n '5295,5320p' HUB.txt; echo; echo \"=== HUB page tag\"; python3 - <<'EOF'\nt=open('HUB.txt',encoding='utf-8',errors='replace').read().split('\\n')\nff=0\nfor i,l in enumerate(t,1):\n    if i==5305: print('leaf/ff before:',ff)\n    ff+=l.count('\\f')\nEOF\necho \"=== SNS 16320\"; sed -n '16300,16340p' SNS.txt"
}
```


### [2026-09-06T15:17:39.152Z] TOOL RESULT

```
=== HUB context
— xsofta-. Dazu das LW. Jahud, JuhUd^ afgh. Jahud, phi.
yahut Phi. Min. p. 32, Z. 1, arab. yahud, hebr. ''TlH^
b) Ap. y im Anlaut = np. y in: yavar, yar ^Stfissel'
= zd. yavarena-; yOz 'Jagdleopard' = arm. yovaz^ yavaz;
yoy *Joch' = skr. yOga- (aber bal. J^y) neben Juy *Joch' (afgh.
LW. Ju)) = skr. yuga- ; yOsamln {yasim, yasaman, ydsamun,
arab. ydsamun), arm. yasmik. Das Wort yazdan 'Gott' =
zd. yazatunqm (gen. pi.) ist parsisch (daneben Izad *Gott' =
zd. yazata-X die W5rter Yunan *die alten Griechen, YUsuf
*Joseph', yaqut 'Hyacinth, Rubin' sind aus dem Arabischen,
yakand *Rubin aus dem Aramaischen (syr. X*U1p% XH^Ip^ usw.,
gr. vdydvd^oq, NSldeke, Pers. Stud. II, 44) entlehnt. Die
Worter yar Treund', yad *Erinnerung' lauteten im Pehlevi
nicht mit y an, vgl. Gl. and Ind. p. 23; wie aber der An-
laut zu lesen ist, bleibt unklar, da die Zeichen mehrdeutig
sind; lautgesetzlich soUte man nur a- erwarten (also phi.
ayar^ aydt), da eben nur anlautendes a vor einfachen Eon-
sonanten im Np. abfallt, siehe § 2 und oben p. 106. Vgl.
paz. ayad memory' Min. Gl. 27, ayadagar memorandum',
ayadinldan *to remember Shk. 235, np. y(ld\ paz. ay do oder,
np. yd; paz. aydr helper Min. Gl. 27, Shk. 235, np. ydr\
paz. aydftan *to obtain', aydft a favour' Min. Gl. 27, np.
yaftafiy aber zd. dyapta-l
In yak ein und yax *Eis' geht ya- auf ai- zuriick. So-
mit steht np. y fiir urspr. anlaut. y in echtpersischen WQrtem
nur in sehr wenig Fallen. In diesen kdnnte es vielleicht

=== HUB page tag
leaf/ff before: 161
=== SNS 16320

( flt»o-0 '■&) -o^' 1 *: dastan: \««*>*^ 



. i*.iU «*iUi :daxsag 



, 3_h>-0 



.t/uS-fcliift-. 676 > U) daxsta-:fc- 

( ^U :^) n/Yo*5 'ft/^T^ -O^* (0 
.^...aiiy.a-J*.*: dahisn Omand: jrf«c- wcu-o 

.i.****/*'**-^**" •=*** 4gtt : y akand! "*° 

Uyacinthus w* hyakinthos : „»V3U»«* *1JWtf 

aj ^ ***) *•/ •* -' •-> **• vj " ^ ,a " ' ^ J "* f!" ** 



U iW>. darav-, drav-^rf^drav-, darav- :<=« I 
.{Man. Stud. 65) <8** d'rwg ij8* 738) 

u^\o-*«€> .n/VT^ -o^< **'•** :d3risn: \Ky>*0 
.YT/T*.dtf*-»«*»*» li ** U * , * i =Pad ed dariln: 

.^IjjbKi-.darisnlh: -<0*0>-0 
- o^tfjA^'O^'^W :abaz darisnlh: ^^^3-u^ I 

H/"* 5 -T»/W^ '0^e U 



^^Ujcu^U^L-iI,
```


## [2026-09-06T15:17:48.024Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('HUB.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('n pages',len(pages))\nfor i,p in enumerate(pages):\n    if 'yakand' in p:\n        print('block',i)\n        print(repr(p[:120]))\n        print(repr(p[-120:]))\nEOF"
}
```


## [2026-09-06T15:17:49.383Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SNS_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'yakand' in p or 'hyakinthos' in p:\n        print('block',i, p[:200].replace('\\n',' | '))\nEOF"
}
```


### [2026-09-06T15:17:49.891Z] TOOL RESULT

```
n pages 300
block 161
'— 151 ~\ntrennt\', zd. yuta-; Justan *suchen\' von einer Wzl. "^i/udh?;\nJastan *springen, eilen\' von einer Wzl. yas ? ; Jas'
"aut = np. y:\ndyam *ich komme', siehe Horn Nr. 60; bdyad 'muss'\nH. 179; pdyad schiitzt' H. 282; pddydb (parsisch) H. 268,"
```


### [2026-09-06T15:17:51.932Z] TOOL RESULT

```
block 167                                                        ^ |                                    liJC-yU^L-jlj
```


## [2026-09-06T15:18:25.410Z] TOOL CALL #29: Bash

```json
{
 "command": "pdftoppm -f 223 -l 223 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg223 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg223.png"
}
```


### [2026-09-06T15:18:27.715Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 79615 Sep  6 11:18 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg223.png
```


## [2026-09-06T15:18:29.461Z] TOOL CALL #30: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg223.png"
}
```


### [2026-09-06T15:18:30.005Z] TOOL RESULT

```

```


## [2026-09-06T15:18:29.993Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T15:18:39.737Z] TOOL CALL #31: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-06T15:18:39.743Z] TOOL RESULT

```


```


## [2026-09-06T15:18:44.013Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AD%D8%B4%D9%8A%D8%B4",
 "prompt": "Give the Arabic entry: etymology of حشيش (ḥašīš), the root ح ش ش, its meanings, and any derived terms / descendants (Persian, English hashish, Italian assassino)."
}
```


## [2026-09-06T15:18:45.009Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/assassin",
 "prompt": "Full etymology of assassin and assassinate, including the Arabic hashishiyyin, the Nizari Ismaili sect, Italian/French mediation, and any note that the hashish-eating story is doubted."
}
```


### [2026-09-06T15:18:51.348Z] TOOL RESULT

```
# Arabic Entry: حشيش (ḥašīš)

## Etymology
The word derives from the Semitic root ح ش ش (ḥ š š), which is shared across Arabic dialects.

## Root
**ح ش ش** (ḥ š š) — This triconsonantal root appears in multiple Arabic variants and generates approximately three related terms.

## Meanings
The noun has several definitions:
1. "grass, hay" — the primary botanical sense
2. "hemp, cannabis" — the plant itself
3. "marijuana" and "hashish" — specific preparations of the cannabis plant

## Derived Terms
- حَشَّاش (ḥaššāš) — one who uses or deals with hashish
- حَشَّاشِين (ḥaššāšīn) — plural form

## Notable Descendants/Borrowings
The word spread widely through European languages via Persian and Ottoman Turkish intermediaries, including:
- English: "hashish"
- Italian: "hashish"
- Persian: حشیش (hašiš)
- Multiple European languages adopted the term through direct borrowing or via German "Haschisch"

The word's etymological journey reflects medieval trade routes connecting the Middle East to Europe.
```


### [2026-09-06T15:18:51.940Z] TOOL RESULT

```
# Etymology of Assassin

The word **assassin** originates from Arabic *hashīshīn*, a nickname for the Nizari Ismaili sect operating in medieval Lebanon during the Crusades. Led by Hasan ibn al-Sabbah (known as the "Old Man of the Mountains"), this group earned a fearsome Western reputation.

## The Arabic Route

The term derives from *hashishiyy*, connected to hashish. However, the etymology entry notes: "there is no evidence that the medieval Ismailis used hashish," suggesting the hashish-consumption legend is historically unfounded.

## Path to English

The word traveled through Italian and French before entering English around the 1530s. Notably, "the plural suffix *-in* was mistaken in Europe for part of the word," a linguistic misunderstanding similar to what happened with "Bedouin."

Italian speakers generalized the sect's nickname to describe any assassin by the early 14th century. The term later spread to French and eventually English, where it gained widespread use by the mid-16th century as a common noun for murderers rather than a specific sectarian reference.
```


## [2026-09-06T15:18:56.031Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%8A%D8%A7%D9%82%D9%88%D8%AA",
 "prompt": "Give the Arabic and Persian entries for ياقوت / یاقوت: the etymology (Greek hyakinthos, Aramaic/Syriac mediation, Middle Persian yākand), meanings, and descendants."
}
```


## [2026-09-06T15:18:57.011Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/hyacinth",
 "prompt": "Full etymology of hyacinth: Greek hyakinthos, pre-Hellenic origin, Latin hyacinthus, French jacinthe/hyacinthe, and the gem sense."
}
```


### [2026-09-06T15:19:01.946Z] TOOL RESULT

```
# ياقوت / یاقوت - Arabic and Persian Entries

## Etymology
According to the Wiktionary entry, the word derives from Ancient Greek *ὑάκινθος* (huákinthos), "possibly via Sogdian [script needed] (yγwth /⁠yaγūt⁠/, 'ruby')."

The document does not mention Aramaic/Syriac mediation or Middle Persian *yākand* as intermediaries.

## Arabic Entry (ياقوت)

**Meanings:**
1. Ruby
2. Sapphire

The noun is masculine, with plural form *يواقيت* (yawāqīt).

## Persian Entry (یاقوت)

The entry identifies this as "Classical Persian: یاقوت (yâqut)" and notes it descended from the Arabic term. However, the Wiktionary page provides no separate Persian definitions—it functions primarily as a documented loanword from Arabic into Persian.

## Selected Descendants
The term spread widely through languages influenced by Persian and Ottoman Turkish, including Hindi, Urdu, Turkish, Albanian, Romanian, and Serbo-Croatian.
```


### [2026-09-06T15:19:03.886Z] TOOL RESULT

```
# Etymology of Hyacinth

The word "hyacinth" has ancient roots tracing back to Greek. According to the Online Etymology Dictionary, the term comes from "Greek _hyakinthos_, which is probably ultimately from a non-Indo-European Mediterranean language."

The word entered English through a circuitous path: it was "re-Greeked from _jacinth_ (late 14c.)" which derived from Old French and Medieval Latin forms, all ultimately linking back to that Greek source.

**Historical uses:** In ancient Greece, the term referred to a blue gem (possibly sapphire) and a purple or deep red flower. The exact botanical identity remains uncertain—"gladiolus, iris, and larkspur have been suggested." 

**Mythological connection:** According to Greek mythology, the flower supposedly "sprung from the blood of _Hyakinthos_, Laconian youth beloved by Apollo and accidentally slain by him," with the letters "AI" or "AIAI" (representing a Greek cry of grief) said to appear on its petals.

The modern application to a specific flowering plant genus dates to the 1570s.
```


## [2026-09-06T15:19:10.086Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SOD\"; grep -n -i \"yaghut\\|yaγūt\\|ya.wt\\|y'γwt\\|yγwth\\|ruby\" SOD.txt SOD_pages.txt | head -20"
}
```


### [2026-09-06T15:19:10.151Z] TOOL RESULT

```
=== SOD
SOD.txt:6318:the  area  and  the  kind  of  ruby  for  which  it  was 
SOD_pages.txt:3305:Greek lamptir. In later borrowings, however, /// is                  the area and the kind of ruby for which it was
```


## [2026-09-06T15:19:11.720Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/Eve",
 "prompt": "Etymology of the name Eve: Late Latin Eva, Greek Heua, Hebrew Hawwah, meaning 'life' / 'living', root h-y-y, and any note on Arabic hayya."
}
```


### [2026-09-06T15:19:16.925Z] TOOL RESULT

```
# Etymology of Eve

The name Eve has Hebrew origins. According to the Online Etymology Dictionary, it comes from "Late Latin, from Hebrew (Semitic) *Hawwah*, literally 'a living being,' from base *hawa* 'he lived.'"

The meaning connects to life itself—the name derives from a root associated with living. The etymology entry notes that "in the Hebrew here, the phonetic similarity is between *hawah*, 'Eve,' and the verbal root *hayah*, 'to live.'"

However, the source includes an intriguing scholarly note suggesting alternate origins: the name "sounds suspiciously like the Aramaic word for 'serpent.'" This observation suggests the etymology may be more complex than a straightforward connection to "living," possibly reflecting multiple linguistic layers or folk etymology in the Biblical text.
```


## [2026-09-06T15:19:20.816Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '6310,6325p' SOD.txt; echo \"=== grep ykwnd/y'kntt in SOD\"; grep -n \"y'k\\|ykn\\|yqnt\" SOD.txt | head"
}
```


### [2026-09-06T15:19:20.892Z] TOOL RESULT

```
This,  probably,  was  also  the  case  for  common 
Sogdian.  The  sound  change  Idl  >  III  might  have 
centered,  as  Morgenstierne  puts  it,  in  the  area  of 
Badakhshan,  the  north-eastern  corner  of  Afghanistan 
and  southern  Tajikestan,  in  the  region  neighboring 
on  the  province  of  NOristan  (ancient  KafiristanX  It  is 
noteworthy,  finally,  that  the  word  Badakhshan, 
which  is  used  in  the  Islamic  period  to  designate  both 
the  area  and  the  kind  of  ruby  for  which  it  was 
famous,  is  also  spelled  with  /  as  Balakhsh  (French 
Balaisy  English  Balas). 

The  last  word  about  /  is  said  by  Livsic  and  Sims- 
Wiliiams.  Livsic  thinks  that  the  last  letter  of  the 
Sogdian  alphabet  (in  the  Penjikent  ostracon) 
represents  the  phoneme  191  (voiceless  counterpart  of 
=== grep ykwnd/y'kntt in SOD
8553:159  "nVty'kh   B  cte><c^j 
8554:amtyak   ('mty'kh) 
9258:268  "stny'kCh)   S  piar^jUUoU 
9259:astanya(k)   ^'pw  "stny'kh 
9530:316  "vvm'nty'kh  ksJ^^^j^ 
9660:335  Vskr'ky'kh  i^i^jS^r 
11403:604  'pz'y'krtyh   B  &&+? '*sj£*j. 
11478:614  'pzykrtyh  =*  'Pz'y'krtyh 
11927:)ysykn5h 
12095:709  'ysyknSh   S
```


## [2026-09-06T15:19:27.873Z] TOOL CALL #39: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%AD%D8%B4%D9%8A%D8%B4' --note 'page 223, root H.s.s: Arabic hasis \"grass, hay, hemp\", root h-s-s, derived hassas/hassasin, descendants incl. Persian hasis and English hashish' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/assassin' --note 'page 223, root H.s.s node 4/5: assassin from Arabic hashishiyyin via Italian and French, 1530s; note that there is no evidence the medieval Ismailis used hashish' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D9%8A%D8%A7%D9%82%D9%88%D8%AA' --note 'page 223, root Hyakinthos nodes 3-4: Arabic yaqut from Greek hyakinthos, possibly via Sogdian; Persian yaqut from Arabic' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/hyacinth' --note 'page 223, root Hyakinthos: Greek hyakinthos pre-Greek Mediterranean word; Latin hyacinthus; French; English hyacinth/jacinth' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/Eve' --note 'page 223, root H.y.y nodes 3-5: Late Latin Eva from Hebrew Hawwah \"a living being\", base hawa \"he lived\"' 2>&1 | tail -3"
}
```


### [2026-09-06T15:19:31.821Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/3c1047eaafb6d704.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b4373363c667edaf.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/23a75a387d644fdd.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f1f7889958648e2c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6eb2eab3400c27ce.txt
```


## [2026-09-06T15:19:46.931Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SKT hyacinth\"; grep -n -i 'hyacinth' SKT.txt | head -3; echo \"=== WEB hyacinth/Eve\"; grep -n -i \"^hy'a-cinth\\|hy.a.cinth\\|^Eve,\" WEB_vol1.txt | head -5; echo \"=== FSD hyacinth\"; grep -n -i 'hy\"a-cinth\\|hyacinthus' FSD_vol2.txt FSD_vol3.txt | head -5; echo \"=== LEW/LAT hyacinthus\"; grep -n -i 'hyacinthus\\|hyacinth' LEW_1910.txt LAT.txt | head -5"
}
```


### [2026-09-06T15:19:47.560Z] TOOL RESULT

```
=== SKT hyacinth
9001:S«c  Uunr- AetnUi,  a  flower.   (F»  *L.  -Gk.) mhmiki.  —  U  kyannthys.  «>  Gk.  i^- N,  an  iris,  la^k^pur  mot  our  hyacinth). dcUh,  a  preaous  stooe.    iF.  — L.»
=== WEB hyacinth/Eve
83885:grape hop’pér, an insect, Erythroneura vitis, that attacks grapevine leaves. grape hy’a-cinth, any of a group of small, hardy bulbs of the lily family, with spikes of small, bell-shaped flowers of blue or white. grape moth, any moth, as Eudemis botrans, the larva of which feeds upon grapes. _ grap’ér-y, n.; pl. grap/ér-ies, a building or enclosure used for the growing of grapes. 4 érape’shot, n. a missile formerly discharge from a cannon, intermediate between cast shot and solid shot, having much of thene structive spread of the former with someni a of the range and penetrative force of thee ter. A round of grapeshot consisted of ‘i tiers of cast-iron balls arranged, generaly three in a tier, between four parallel i ee. disks connected together bya central wroug i iron pin. ae grape’stone, n. a seed of the grape. T grape su’găr (shy/gir), a simple sugar. oie ring in many plants aog fruits, especia ripe grapes; dextrose; glucose. S grape’vine, n. 1. any of various woody vin! bearing grapes. a a secret means of spreadinE g information: also grapevime `. 3. a rumor; A report; hears grape worm, the larva of the grape a wings -graph, [from Gr. graphé, a writing or we bining
93139:hy/a-cinth, n. (Fr. hyacinthe; L. hyacinthus, Gr. hyakinthos, the hyacinth.} _ 1, a plant of the genus Hyacinthus, belong- ing to the lily family, with long, narrow leaves and spikes of fragrant, bell-shaped flowers; especially, the cultivated species, Hyacinthus orientalis,
93145:hy’a-cinth béan, a climbing plant, Dolichos ablab, of the bean family.
108066:lil’y-hand/ed, a. having white, delicate hands. lil’y hy’a-cinth, a bulbous perennial o the
=== FSD hyacinth
FSD_vol2.txt:50631:Hy"a-cin'thl-a,  l   hai''a-sin'£hi-a:  2   hy  "a-cin'thi-a,  n.pl  Or. Antig.  A   festival  lasting  for  three  days  at  the  height  of  sum- mer, in  honor  of  Hyacinthus  and  Apollo.  The  first  cere- monies were  mournful,  commemorating  the  death  of  Hyacin- thus; the  last  were  joyful,  celebrating  his  rebirth,  q'he festival  was  celebrated  throughout  the  Peloponnesus,  and with  special  enthusiasm  at  Amyclic.  It  lasted  eleven  days and  took  place  in  the  mouth  of  May,  soon  after  the  Isth- mian games.
FSD_vol2.txt:50634:3.  Like  or  relating  to  Hyacinthus,  the  fabled  favorite  of Apollo;  hence,  lovely;  beautiful.
FSD_vol2.txt:50637:Hy"a-ciii'tbus, Ihara-sin'fhua;  3hy’’a-cJn'thus,ft.  Gr.Myfh. 1.  A   beautiful  youth  of  Amychc,  beloved  of  Apollo,  and accidentally  killed  by  the  god  when  they  were  playing  at discus-throwing.  .4polIo,  unable  to  save  him,  changed  him into  the  flower  called  hyacinth.  Hyacinthus  ia  supposed  to typify  the  early  vegetation  of  spring.  Other  versions  of  the legend  say  that  Zepherus,  out  of  jealousy,  blew  the  discus, cast  by  Apollo,  again.st  the  head  of  Hyacinthus,  thus  causing his  death.  See  htacinthi,  3,  and  Hyacinthia.  Hy-a'- kin-thost.  3.  Boi.  A   notable  genus  of  Old  World  plants  of the  lily  family  (LiUacete),  with  coated  bulbs,  narrow  radical leaves,  and  a   simple  leafless  scape  bearing  a   raceme  of  often handsome  hell-shaped  flowers.  The  numerous  cultivated forms  are  mostly  derived  from  if.  orientalis.  [L.,  see
=== LEW/LAT hyacinthus
```


## [2026-09-06T15:19:48.557Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON hashish\"; grep -n 'حشیش' MON_part1.txt | head -5; echo \"=== MON hayat/hayavan\"; grep -n 'حیات\\|حیوان' MON_part1.txt | head -3; echo \"=== ARY latin index\"; grep -n -i 'HASHISH\\|YAQUT\\|YAKAND\\|HYACINTH' incoming/ARY/ARY_latin_index_pages.txt | head"
}
```


### [2026-09-06T15:19:48.651Z] TOOL RESULT

```
=== MON hashish
53423:به استعمال حشیش؟ ج. 9 
53479:حشیش: ۵۹14" |ع.] (.) (گیا.) گیاه خشکت 
53480:(واحد حشیشه). (گبا.) شاهدانه. سر 
83488:حشیش به بازار عرضه می‌شده و مورد 
83491:حشیش الفقرا» ورق الخیال» جزء اعظم 
=== MON hayat/hayavan
1173:آب حیات: 12(2:-5 (ف. ع.) (امر.) 
1258:کسی يا حیوانی. آب ریختن» جاری کردن 
1490:در آب می‌زید: جانوران آبزی ‏ حیوانات 
=== ARY latin index
```


## [2026-09-06T15:19:58.170Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON yaqut\"; sed -n '93374,93382p' MON_part2.txt; echo \"=== MON yakand\"; grep -n 'یاکند\\|باکند\\|یا کند' MON_part2.txt | head; echo \"=== MON hayat entry\"; grep -n '^حیات\\|حیات:' MON_part1.txt | head -5; echo \"=== MON hayavan\"; grep -n 'حیوان:' MON_part1.txt | head -3; echo \"=== MON hava\"; grep -n 'حوا:' MON_part1.txt MON_part2.txt | head -3; echo \"=== MON ehya\"; grep -n 'احیا:\\|إحیا' MON_part1.txt | head -3"
}
```


### [2026-09-06T15:19:58.370Z] TOOL RESULT

```
=== MON yaqut

یافه: (م)۷2]2 (.) باوه. 

یاقوت: ۷2۰(.) (زم.) یکی از سنگ‌های 
آذرین که جزء کانی‌های سنگهای اسند 


یم 

=== MON yakand
29089:چیز که قلب ماهبت اشیا کند همچون اکسیر. 
=== MON hayat entry
1173:آب حیات: 12(2:-5 (ف. ع.) (امر.) 
4227:حیات: آنچه از اعضاء و غیر آن که برای 
27852:حیاتی گیرد» حشو زاید. پارازیت ول 
38722:تحیات: رد۱۵ (ع.] (مسص. )4 ج. 
50645:چشمه حیات: ینک | بات (اح.) آب 
=== MON hayavan
46865:جان و روان عالم است. جان حیوان: (کد.) 
54648:سج.) (کد.) نفهم» بی‌شعور. آب حیوان: 
=== MON hava
=== MON ehya
```


## [2026-09-06T15:20:08.241Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in ARB_mo3rb.txt ARB_abdulraheem.txt TAD.txt TAD_pages.txt KFL.txt AFM.txt AFM_pages.txt; do echo \"=== $f\"; grep -n 'اقوت' $f | head -4; done"
}
```


### [2026-09-06T15:20:09.988Z] TOOL RESULT

```
=== ARB_mo3rb.txt
1059:معجم الأدبا لياقوت 6ه وا 
1149:و سنة هام ٠‏ فقك نقل ياقوت فى ترحمته فى معجم الأدباء :ب" عن ألى سعد 
1164:وما أشيه ذلك . قال مؤلف هل ذا الاب أى ياقوت - وهذا الاعتذار 
1198:السمعانى فى الأنساب وياقوت فى معجم الأدباء واين خلكان فى الوفيات تارم 
=== ARB_abdulraheem.txt
=== TAD.txt
3052:باقوت وونانى ناسنا وف اللاتينية 5تاطاماعةبرط وهو :3 
=== TAD_pages.txt
2907:      ‫وهو ‪3:‬‬         ‫وونانى ناسنا وف اللاتي‪5‬نتيةاطاماعةبرط‬         ‫باقوت‬
=== KFL.txt
36119:* الياقوت ١م‏ 
36513:٠62‏ - معجم الأدباء » لياقوت الحموى - تحقيق أحمد فريد الرفاعى - القاهره /1977 م. 
=== AFM.txt
1330:ܝܐ حجر دفيق ܪ أحمر اللون كالماقوت 4 ܫܐ ܪܝܬ كاتكهر باء ٠وقال‏ بعضهم هو المرحان 
=== AFM_pages.txt
814:ܝܐ حجر دفيق ܪ أحمر اللون كالماقوت 4 ܫܐ ܪܝܬ كاتكهر باء ٠وقال‏ بعضهم هو المرحان
```


## [2026-09-06T15:20:16.230Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== TAD ctx\"; sed -n '3045,3058p' TAD.txt; echo \"=== TAD page tag\"; awk 'NR>=2890 && NR<=2925' TAD_pages.txt | head -40"
}
```


### [2026-09-06T15:20:18.406Z] TOOL RESULT

```
=== TAD ctx
و صسناصتة فى اللانينة أي جر 


2 ئى «6 
أسمين - فارسي « ياسمين » نقله تحارة البرتوغال الى اوريا حو سئة 0ه 
وهو مستعمل هذا الاسم فى جميع اللغات وهو قسرددا ف اليونانية وقيل ان آم 
تمرك وو اق انوع قل الدع زكر ١‏ عت يليت لزاه 
باقوت وونانى ناسنا وف اللاتينية 5تاطاماعةبرط وهو :3 
أونه أجمر 
(1) وممتاها موضم الثار . وعربيها القصبح الإظير ”قفن الور وق هل فراع 


فيها ويشتوى . وقيل حجارة مدورة اذا حميت لم يقدر اد ان بطا عليها ٠‏ ومنه قوم ج 
الوميس اي اشئدت الغرب 
=== TAD page tag
                              ‫ك ماوق‬
                                   ‫واه‬
                                     ‫© من‬       ‫اق‬
                                                 ‫ج‏‬‫وترى‬
                                                      ‫أب‬‫وأجاق ©‬
      ‫وين عحنب اسود ‏ بين افلعبرانية معناه خر وهو ‪50‬ا«الهيفوىنا‬
                                                 ‫و صسناصتة فى اللانينة أي جر‬

                                 ‫‪ 2‬ئى «‪6‬‬

     ‫سي « ياسمين » ناقللهتبحاررتةوغال الى اوريا حوسئة‪0‬ه‬
                                                      ‫انر‪-‬‬
                                                         ‫فمي‬
                                                           ‫أس‬
     ‫فانية وقيل ان آم‬
                    ‫وهو مستعمل هذا الاسمفى جميعاللغات وهو قاسرلددياون‬
                 ‫تمرك وو اق انوع قل الدع زكر ‪١‬‏عت يليت لزاه‬
      ‫وهو ‪3:‬‬         ‫وونانى ناسنا وف اللاتي‪5‬نتيةاطاماعةبرط‬         ‫باقوت‬

                                                                    ‫أونه أجمر‬

     ‫‪.‬ربيها القصبح الإظير ”قفن الور وق هل فراع‬
                                             ‫(‪ )1‬وممتاها موضم الثار وع‬
     ‫‪.‬قيل حجارة مدورة اذا حميتلميقدر اد ان بطا عليها و‪٠‬م‏نه قوم ج‬
                                                                ‫فيها ويشتوى و‬
                                                        ‫الوميس اي اشئدت الغرب‬
‫بانسون ب وثانى «مونسة وهو نبات زهره اسن طن الرانحة ويستقطرون‬

                                                          ‫ققيمعنه‬
                                                                ‫النعسر‬
   ‫الصثراء وهو يسرّب اصفرار الجلد‬   ‫ركان ب وونانى ‪ 80:611‬معناه مرض‬
                             ‫ولثم وبصب ويصف‬              ‫الثب ويف‬
‫‪ -‬عبراني د بشنه» معناه مصقول‬


‫اوهو مشتق من« شفه » صقل ‪ .‬ونقل الى اليونانية ونودةة ومنها اسلاىئر لئات‬
```


## [2026-09-06T15:20:39.308Z] TOOL CALL #45: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe/data/verification/sources/refs/ | grep -i sns; ls /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ 2>/dev/null; python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'));print(json.dumps(d.get('SNS'),ensure_ascii=False))\""
}
```


### [2026-09-06T15:20:41.781Z] TOOL RESULT

```
SNS_pages.txt
SNS.txt
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
{"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt"], "page_offset": "242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image", "covers_etymology": true, "notes": "OCR quality is POOR: Persian text mostly garbage, Latin transliterations partially readable. Verification will usually need the page image."}
```


## [2026-09-06T15:20:50.668Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && for u in \"https://archive.org/download/VajnameShayest/page/n167_w1000.jpg\" \"https://archive.org/download/VajnameShayest/page/n167.jpg\"; do echo \"-- $u\"; curl -sL -o sns167.jpg -w \"%{http_code} %{size_download}\\n\" \"$u\"; file sns167.jpg; done"
}
```


### [2026-09-06T15:20:55.729Z] TOOL RESULT

```
-- https://archive.org/download/VajnameShayest/page/n167_w1000.jpg
200 147680
sns167.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 1094x804, components 1
-- https://archive.org/download/VajnameShayest/page/n167.jpg
200 147680
sns167.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 1094x804, components 1
```


## [2026-09-06T15:20:57.649Z] TOOL CALL #47: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/sns167.jpg"
}
```


### [2026-09-06T15:20:57.667Z] TOOL RESULT

```

```


## [2026-09-06T15:21:23.617Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2025,2032p' LKT.txt | cut -c1-600"
}
```


### [2026-09-06T15:21:23.675Z] TOOL RESULT

```
837.  Ar.  hasira:
'Verlust  haben,  bankrott  machen' ;  dazu das  Subst.  hasära  'Verlust,  Schaden' ; hieraus  siz.  cassara  in  dem  Ausdrucke fari  cassara  'verschwenden'.  [StGlIt H,  230.    GrSVociSic  231.
838.  Ar.  hasis:
Vulgäre  Form  für  haSsäs  [Imäla :  ä  ^ e  ^  T]  'spitzes  Instrument  z.  B.  zum Heumähen' ;  hieraus  sp.  aciche  'Hand- beil des  Flickschusters'.  [Dicc  Gast 34  b.]   [DE  37/38.
839.  Ar.  hasis:
'Gras,  Heu',  später  beng  [s.  hier  Nr.  213] oder  indischer  Hanf,  Cannabis  indica [Über  den  indischen  Hanf  (Haschisch) und  seine  Verwendung  als  narkotisches Genußmittel.  In  Ausland  1863,  Nr.  30  j Ed.  Grimaux,  Du  hachich  ou  chanvre Indien.  Paris  1865];  in  die  europäischen Sprachen  ist  das  Wort  fast  unverändert übergegangen:  frz.  hachiche,  russ.  gasiSf dtsch.  Haschisch.  —  „In  Syrien  steht der  Hasis,  ein  berauschendes  Hanf-  oder Mohnpräparat,  welches  unvermengt  ge- nossen oder  dem  Tabak  beigemengt wird,  bei  den  niederen  Stä
67
[Ar.  hass.
```


## [2026-09-06T15:22:44.867Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FRS\"; grep -n 'یاکند\\|باکند' FRS.txt FRS_pages.txt | head -5; echo \"=== PHD page\"; python3 - <<'EOF'\nt=open('PHD.txt',encoding='utf-8',errors='replace').read().split('\\n')\nff=0\nfor i,l in enumerate(t,1):\n    if i==669: print('ff blocks before line 669:',ff)\n    ff+=l.count('\\f')\nEOF\necho \"=== FSF\"; grep -n 'یاکند' FSF.txt | head -3"
}
```


### [2026-09-06T15:22:46.961Z] TOOL RESULT

```
=== FRS
FRS.txt:11743:گفت کین مردمان بی باکند همه همواره دزد و حالاکند 
FRS.txt:12394:و کریبلخ زمانی شکار ال کند یاکندهمه‌وادیش را ببط و بچال ۱ 
FRS_pages.txt:4647:‫ریدند بی‌خطرخوبان جمست را چه خطرهر کجا بودیاکند‬
FRS_pages.txt:12884:           ‫همه همواره دزد و حالاکند‬                   ‫گفت کین مردمان بی باکند‬
FRS_pages.txt:13642:   ‫چو‬‫یاکندهمه‌وادیش را بببط‬                    ‫کوریبلخ زمانی شکار ال کند‬
=== PHD page
ff blocks before line 669: 123
=== FSF
11707:ز خاک سیه جان گویاکند 
12739:ز خاک سیه جان گویاکند
```


## [2026-09-06T15:22:58.522Z] TOOL CALL #50: Bash

```json
{
 "command": "set -e\nD=/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr\nmkdir -p $D/SNS $D/BOOK\npython3 -c \"\nfrom PIL import Image\nim=Image.open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/sns167.jpg'); im.save('$D/SNS/299.png')\nim2=Image.open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg223.png'); im2.save('$D/BOOK/223.png')\nprint('ok')\n\"\ncat > $D/SNS/299.vision.txt <<'EOF'\n[Tavoosi, Vazhe-name-ye Shayast ne Shayast, printed page 299 (archive.org VajnameShayest leaf n167,\n left-hand page of the spread; the right-hand page carries the printed number ۲۹۸).\n Read from the page image saved as data/verification/sources/refs/ocr/SNS/299.png.]\n\nEntry (verbatim, middle of the left column):\n\n  yākand: یاکند، یاقوت. «یاکند یاقوت باشد، شاکر بخاری گفت:\n     کجا تو باشی گردند بی‌خطر خوبان / جمست را چه خطر هر کجا بود یاکند»\n  (لغت‌فرس) این واژه اصلاً یونانی: hyakinthos و لاتین: hyacinthus\n  به معنی نوعی زهر است، یاقوت معرّب یاکند فارسی است که گوهری زینتی و سرخ‌رنگ\n  و درخشان و پربها است. ک۱۶/۲\n\nTwo points relevant to Nourai p.193 (pdf 223):\n 1. SNS:299 does say the Greek/Latin word means «نوعی زهر» = \"a kind of poison\" — so Nourai's\n    root note reports SNS correctly. (The claim itself is wrong: Gk. ὑάκινθος is a flower.)\n 2. SNS:299 says «یاقوت معرّب یاکند فارسی است» = \"Arabic yāqūt is the arabicised form of\n    Persian yākand\" — this is Nourai's authority for the Persian → Arabic arrow.\nEOF\necho saved; ls -la $D/SNS $D/BOOK"
}
```


### [2026-09-06T15:23:00.754Z] TOOL RESULT

```
ok
saved
/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK:
total 8936
drwxrwxr-x  2 sfmqrb sfmqrb   4096 Sep  6 11:23 .
drwxrwxr-x 11 sfmqrb sfmqrb   4096 Sep  5 16:42 ..
-rw-rw-r--  1 sfmqrb sfmqrb  71589 Sep  5 10:46 100.png
-rw-rw-r--  1 sfmqrb sfmqrb 104864 Sep  4 19:03 101.png
-rw-rw-r--  1 sfmqrb sfmqrb  68145 Sep  5 10:49 102.png
-rw-rw-r--  1 sfmqrb sfmqrb  79623 Sep  5 10:55 103.png
-rw-rw-r--  1 sfmqrb sfmqrb  78826 Sep  5 10:59 104.png
-rw-rw-r--  1 sfmqrb sfmqrb  82500 Sep  5 11:05 105.png
-rw-rw-r--  1 sfmqrb sfmqrb  55270 Sep  5 11:03 106.png
-rw-rw-r--  1 sfmqrb sfmqrb  68501 Sep  5 13:28 108.png
-rw-rw-r--  1 sfmqrb sfmqrb  63543 Sep  5 13:35 109.png
-rw-rw-r--  1 sfmqrb sfmqrb  67502 Sep  5 13:39 110.png
-rw-rw-r--  1 sfmqrb sfmqrb  72718 Sep  5 13:38 111.png
-rw-rw-r--  1 sfmqrb sfmqrb  50381 Sep  5 13:39 112.png
-rw-rw-r--  1 sfmqrb sfmqrb  83933 Sep  5 13:54 114.png
-rw-rw-r--  1 sfmqrb sfmqrb  64811 Sep  5 14:02 117.png
-rw-rw-r--  1 sfmqrb sfmqrb  42354 Sep  5 14:08 118.png
-rw-rw-r--  1 sfmqrb sfmqrb  50224 Sep  5 14:12 120.png
-rw-rw-r--  1 sfmqrb sfmqrb  82335 Sep  5 14:19 121.png
-rw-rw-r--  1 sfmqrb sfmqrb  61026 Sep  5 14:26 123.png
-rw-rw-r--  1 sfmqrb sfmqrb  91077 Sep  5 14:38 124.png
-rw-rw-r--  1 sfmqrb sfmqrb  75202 Sep  5 14:31 125.png
-rw-rw-r--  1 sfmqrb sfmqrb  86203 Sep  4 19:03 126.png
-rw-rw-r--  1 sfmqrb sfmqrb  83553 Sep  5 16:14 128.png
-rw-rw-r--  1 sfmqrb sfmqrb  74748 Sep  5 16:15 130.png
-rw-rw-r--  1 sfmqrb sfmqrb  87739 Sep  5 16:21 134.png
-rw-rw-r--  1 sfmqrb sfmqrb  68320 Sep  5 16:17 136.png
-rw-rw-r--  1 sfmqrb sfmqrb  70436 Sep  5 16:19 140.png
-rw-rw-r--  1 sfmqrb sfmqrb  53357 Sep  5 16:18 142.png
-rw-rw-r--  1 sfmqrb sfmqrb  63658 Sep  5 16:18 144.png
-rw-rw-r--  1 sfmqrb sfmqrb  89133 Sep  5 16:21 145.png
-rw-rw-r--  1 sfmqrb sfmqrb  60631 Sep  5 16:21 147.png
-rw-rw-r--  1 sfmqrb sfmqrb  81770 Sep  5 16:21 148.png
-rw-rw-r--  1 sfmqrb sfmqrb  72186 Sep  5 16:36 149.png
-rw-rw-r--  1 sfmqrb sfmqrb  31185 Sep  5 16:32 150.png
-rw-rw-r--  1 sfmqrb sfmqrb  96854 Sep  5 16:42 151.png
-rw-rw-r--  1 sfmqrb sfmqrb  61486 Sep  5 16:35 153.png
-rw-rw-r--  1 sfmqrb sfmqrb  63033 Sep  5 16:38 154.png
-rw-rw-r--  1 sfmqrb sfmqrb  77057 Sep  5 16:41 155.png
-rw-rw-r--  1 sfmqrb sfmqrb 101504 Sep  5 16:44 156.png
-rw-rw-r--  1 sfmqrb sfmqrb 169880 Sep  5 16:48 158.png
-rw-rw-r--  1 sfmqrb sfmqrb  27814 Sep  5 16:35 159.png
-rw-rw-r--  1 sfmqrb sfmqrb  14765 Sep  5 16:41 161_am_detail.png
-rw-rw-r--  1 sfmqrb sfmqrb  76745 Sep  5 16:41 161.png
-rw-rw-r--  1 sfmqrb sfmqrb  25911 Sep  5 16:36 163.png
-rw-rw-r--  1 sfmqrb sfmqrb  59398 Sep  5 16:41 164.png
-rw-rw-r--  1 sfmqrb sfmqrb  61265 Sep  5 16:41 165.png
-rw-rw-r--  1 sfmqrb sfmqrb  60832 Sep  5 16:44 166.png
-rw-rw-r--  1 sfmqrb sfmqrb 116877 Sep  5 16:48 167.png
-rw-rw-r--  1 sfmqrb sfmqrb  73551 Sep  5 16:52 171.png
-rw-rw-r--  1 sfmqrb sfmqrb  73400 Sep  5 17:08 172.png
-rw-rw-r--  1 sfmqrb sfmqrb  52970 Sep  5 16:59 173.png
-rw-rw-r--  1 sfmqrb sfmqrb  70664 Sep  5 17:04 174.png
-rw-rw-r--  1 sfmqrb sfmqrb  54907 Sep  5 17:04 175.png
-rw-rw-r--  1 sfmqrb sfmqrb  83583 Sep  5 17:07 176.png
-rw-rw-r--  1 sfmqrb sfmqrb  88207 Sep  5 17:04 177.png
-rw-rw-r--  1 sfmqrb sfmqrb  64024 Sep  5 17:04 178.png
-rw-rw-r--  1 sfmqrb sfmqrb  57139 Sep  5 17:01 179.png
-rw-rw-r--  1 sfmqrb sfmqrb  81598 Sep  5 17:04 180.png
-rw-rw-r--  1 sfmqrb sfmqrb  56794 Sep  5 17:03 181.png
-rw-rw-r--  1 sfmqrb sfmqrb  53414 Sep  5 17:04 183.png
-rw-rw-r--  1 sfmqrb sfmqrb  77310 Sep  5 17:09 184.png
-rw-rw-r--  1 sfmqrb sfmqrb  79537 Sep  5 17:11 185.png
-rw-rw-r--  1 sfmqrb sfmqrb  53749 Sep  5 17:08 187.png
-rw-rw-r--  1 sfmqrb sfmqrb  77516 Sep  5 17:11 189.png
-rw-rw-r--  1 sfmqrb sfmqrb  65970 Sep  5 22:26 190.png
-rw-rw-r--  1 sfmqrb sfmqrb  78016 Sep  5 22:23 191.png
-rw-rw-r--  1 sfmqrb sfmqrb  66901 Sep  5 22:31 193.jpg
-rw-rw-r--  1 sfmqrb sfmqrb  75938 Sep  5 22:38 195.png
-rw-rw-r--  1 sfmqrb sfmqrb  85794 Sep  5 22:32 198.png
-rw-rw-r--  1 sfmqrb sfmqrb  78587 Sep  5 22:28 199.png
-rw-rw-r--  1 sfmqrb sfmqrb  78934 Sep  5 22:26 200.png
-rw-rw-r--  1 sfmqrb sfmqrb  54688 Sep  6 11:00 201.png
-rw-rw-r--  1 sfmqrb sfmqrb  98287 Sep  5 22:35 202.png
-rw-rw-r--  1 sfmqrb sfmqrb  75609 Sep  5 22:29 203.png
-rw-rw-r--  1 sfmqrb sfmqrb  70083 Sep  6 10:53 204.png
-rw-rw-r--  1 sfmqrb sfmqrb  87032 Sep  5 22:33 205.png
-rw-rw-r--  1 sfmqrb sfmqrb  77858 Sep  6 11:03 206.png
-rw-rw-r--  1 sfmqrb sfmqrb  67371 Sep  6 11:02 207.png
-rw-rw-r--  1 sfmqrb sfmqrb  59146 Sep  6 10:59 208.png
-rw-rw-r--  1 sfmqrb sfmqrb  53054 Sep  6 11:00 209.png
-rw-rw-r--  1 sfmqrb sfmqrb  74515 Sep  6 11:06 211.png
-rw-rw-r--  1 sfmqrb sfmqrb  75961 Sep  6 11:07 212.png
-rw-rw-r--  1 sfmqrb sfmqrb  83761 Sep  6 11:07 213.png
-rw-rw-r--  1 sfmqrb sfmqrb  83752 Sep  6 11:05 214.png
-rw-rw-r--  1 sfmqrb sfmqrb 117034 Sep  6 11:09 215.png
-rw-rw-r--  1 sfmqrb sfmqrb  76564 Sep  6 11:19 216.png
-rw-rw-r--  1 sfmqrb sfmqrb  82798 Sep  6 11:18 217.png
-rw-rw-r--  1 sfmqrb sfmqrb  63280 Sep  6 11:19 220.png
-rw-rw-r--  1 sfmqrb sfmqrb  71497 Sep  6 11:20 221.png
-rw-rw-r--  1 sfmqrb sfmqrb  84108 Sep  6 11:17 222.png
-rw-rw-r--  1 sfmqrb sfmqrb  81537 Sep  6 11:23 223.png
-rw-rw-r--  1 sfmqrb sfmqrb 105296 Sep  4 19:03 311.png
-rw-rw-r--  1 sfmqrb sfmqrb  96466 Sep  4 19:03 33.png
-rw-rw-r--  1 sfmqrb sfmqrb  99093 Sep  4 19:03 39.png
-rw-rw-r--  1 sfmqrb sfmqrb  54479 Sep  4 19:03 46.png
-rw-rw-r--  1 sfmqrb sfmqrb  44812 Sep  5 16:36 532.png
-rw-rw-r--  1 sfmqrb sfmqrb  99295 Sep  4 19:03 54.png
-rw-rw-r--  1 sfmqrb sfmqrb  57649 Sep  5 01:38 69.png
-rw-rw-r--  1 sfmqrb sfmqrb  75801 Sep  5 01:35 71.png
-rw-rw-r--  1 sfmqrb sfmqrb  49860 Sep  5 01:47 72.png
-rw-rw-r--  1 sfmqrb sfmqrb  81180 Sep  5 01:53 73.png
-rw-rw-r--  1 sfmqrb sfmqrb  56073 Sep  5 01:50 74.png
-rw-rw-r--  1 sfmqrb sfmqrb  20612 Sep  5 02:01 75_greek_latin_arrow.png
-rw-rw-r--  1 sfmqrb sfmqrb  75134 Sep  5 02:01 75.png
-rw-rw-r--  1 sfmqrb sfmqrb  66505 Sep  5 01:56 76.png
-rw-rw-r--  1 sfmqrb sfmqrb  65211 Sep  5 02:03 77.png
-rw-rw-r--  1 sfmqrb sfmqrb  63822 Sep  5 02:07 78.png
-rw-rw-r--  1 sfmqrb sfmqrb  59439 Sep  5 02:13 79.png
-rw-rw-r--  1 sfmqrb sfmqrb  58953 Sep  5 02:13 80.png
-rw-rw-r--  1 sfmqrb sfmqrb  99904 Sep  5 02:17 81.png
-rw-rw-r--  1 sfmqrb sfmqrb  74477 Sep  5 02:22 82.png
-rw-rw-r--  1 sfmqrb sfmqrb  67094 Sep  5 02:26 83.png
-rw-rw-r--  1 sfmqrb sfmqrb  63329 Sep  5 02:31 85.png
-rw-rw-r--  1 sfmqrb sfmqrb  31530 Sep  5 02:38 86.png
-rw-rw-r--  1 sfmqrb sfmqrb  79874 Sep  5 09:55 87.png
-rw-rw-r--  1 sfmqrb sfmqrb  98452 Sep  5 09:55 88.png
-rw-rw-r--  1 sfmqrb sfmqrb  80984 Sep  5 09:56 89.png
-rw-rw-r--  1 sfmqrb sfmqrb  77182 Sep  5 09:55 90.png
-rw-rw-r--  1 sfmqrb sfmqrb  63799 Sep  5 09:56 91.png
-rw-rw-r--  1 sfmqrb sfmqrb   3476 Sep  5 10:16 92_pahlavi_box.png
-rw-rw-r--  1 sfmqrb sfmqrb  90918 Sep  5 10:16 92.png
-rw-rw-r--  1 sfmqrb sfmqrb  93420 Sep  5 10:18 94.png
-rw-rw-r--  1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r--  1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r--  1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png

/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/SNS:
total 424
drwxrwxr-x  2 sfmqrb sfmqrb   4096 Sep  6 11:23 .
drwxrwxr-x 11 sfmqrb sfmqrb   4096 Sep  5 16:42 ..
-rw-rw-r--  1 sfmqrb sfmqrb   1389 Sep  4 16:10 14.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb 410799 Sep  6 11:23 299.png
-rw-rw-r--  1 sfmqrb sfmqrb   1281 Sep  6 11:23 299.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb   1220 Sep  4 15:51 6.vision.txt
```


## [2026-09-06T15:23:06.908Z] TOOL CALL #51: Bash

```json
{
 "command": "sed -n 1,120p /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-06T15:23:06.960Z] TOOL RESULT

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


## [2026-09-06T15:23:33.449Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BQT v2 hashish\"; grep -n 'حشیش' BQT_v2_pages.txt BQT_v1_pages.txt incoming/BQT/BQT_v3_pages.txt | head -5; echo \"=== BQT hayat/hayavan/hava\"; grep -n 'حیوان:\\|حیات:\\|حوا:' BQT_v2_pages.txt | head -5; echo \"=== HRN/HUB hasis\"; grep -n -i 'hasis\\|ḥašīš\\|Haschisch' HRN.txt HUB.txt | head -5; echo \"=== ARY yaqut\"; grep -n 'یاقوت\\|یاکند' incoming/ARY/ARY_pages.txt | head -5"
}
```


### [2026-09-06T15:23:33.562Z] TOOL RESULT

```
=== BQT v2 hashish
incoming/BQT/BQT_v3_pages.txt:1585:از کر کهای آلوده‌بروغن اساسی متعفن وسمی است که آنرا بنگه وکرد ‎INT‏ حشیش مینامند .
incoming/BQT/BQT_v3_pages.txt:12055:‏بروزن قرقف » حشیشی است کهآن را ب‎
incoming/BQT/BQT_v3_pages.txt:13478:کوهستان حوالی‌شیراز آورند. ‎Sy‏ آنراحشیش-
incoming/BQT/BQT_v3_pages.txt:28867:‏کحیلا ۱ بر وزن هویدا ؛ حشیشی‎
incoming/BQT/BQT_v3_pages.txt:33042:کشیش ۰۱ بروزن حشیش ‎beta‏
=== BQT hayat/hayavan/hava
=== HRN/HUB hasis
=== ARY yaqut
```


## [2026-09-06T15:23:39.631Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1580,1590p' incoming/BQT/BQT_v3_pages.txt"
}
```


### [2026-09-06T15:23:39.689Z] TOOL RESULT

```
‏- پپلوی ‎shah_danak‏ «اونوالا ۱۵۱>.ععرب آن شاعدانه وشاهدانج ۶ دزی ج۱
‎aby lS: Cannabis‏ ازتیرة کزن‌ها که در تقاط معتدل کاشته میشود و در

‏ساقههای ‎OT‏ رشته‌های بافتنی فراوان ‎col‏ و ‎als‏ های ‎OT‏ روغن ‎shar‏ دارد و تمام ‎OT‏ پوشیده
از کر کهای آلوده‌بروغن اساسی متعفن وسمی است که آنرا بنگه وکرد ‎INT‏ حشیش مینامند .
‎۷٩۸ ISS?‏ > ۴ -مصحف «شاءطنان» ( * طنان‌شاء ) . رك : چهاره‌قاله) فهرست :
شامطفان چرخ‌بین بادوغلام روزوشب . «خاقانی‌شروانی4۳۷». ۴ - اشاره ‎VERT‏ ازسورژ ۱۱
‎(sy)‏ :فاستقمم کماامرت ومن‌تاب ممك ولانطفوا انه‌بما تعملون بصیر: پس مستفیم باش آلچنانکه نو
مأمور شده‌ای‌بوه رکه بالوتوبه کرده,وازحدود گنر که حماناام(خدای)پدانچه میکنیدیناست .
[pdf page 26]
```


## [2026-09-06T15:23:47.958Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BQT v2 hayat\"; grep -c 'حیات' BQT_v2_pages.txt; grep -n 'آب حیات\\|حیوان' BQT_v2_pages.txt | head -4; echo \"=== BQT hava\"; grep -n 'حوا ' BQT_v2_pages.txt | head -3; echo \"=== MON hayat ctx\"; sed -n '4224,4230p' MON_part1.txt"
}
```


### [2026-09-06T15:23:48.083Z] TOOL RESULT

```
=== BQT v2 hayat
5
710:      ‫جام جمدردست جان خواعم ناد‬                        ‫آب حیوان چون بتاریکی در است‬
776: ‫حان جو ان ‪ .‬وجان‌خون‌حیوان»‬
828:                       ‫وآب حیات را هم میگویند ‪.‬‬           ‫همآمده است ‪٩‬‏ ‪ -‬ورزق‌وروزی وقوت لابموترا‬
844:‫وحیوانات موذی و غیر موذی باشد از سباع‬
=== BQT hava
=== MON hayat ctx
نر و ماده که سب تولید مثل و نتاج است. 
الا ین : اندام‌ها از حنجره و ریه و غیره 
که در حیوان وسئلهة تنفس است. آلات 
حیات: آنچه از اعضاء و غیر آن که برای 
ادامةٌ زندگانی لازم است. آلات جارحه: 
افزارهای طبیعی و غیر آن از چنگال و دندان 
و شمشیر و کارد و غیره که برای جراحت
```


## [2026-09-06T15:32:26.420Z] TOOL CALL #55: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk223.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW = \"https://en.wiktionary.org/wiki/\"\n\ndoc = {\n \"pdf_page\": 223,\n \"book_page\": 193,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-06\",\n \"entries\": []\n}\n\n# ------------------------------------------------------------------ entry 0\ne0 = {\n \"entry\": 0,\n \"root\": \"H.š.š\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"Arabic root ح ش ش (ḥ-š-š) 'to mow/cut herbage; (of a plant) to dry up' → ḥašīš حشيش 'dried grass, hay'\",\n \"note\": (\"The root is real and the language label is right. Arabic ḥašša / ʾaḥašša means 'to mow, cut grass' and, \"\n   \"of a plant, 'to dry up, wither'; the fiʿīl-noun ḥašīš is 'cut and dried herbage, hay, dry grass', from which the \"\n   \"cannabis sense develops. Klein, the very reference Nourai cites (KLN:706), states the case in one line: Arab. \"\n   \"ḥashīsh 'hemp', prop. 'dried grass', rel. to Heb. ḥāšāš 'dried grass' — so the root sense Nourai gives, 'to dry \"\n   \"(a vegetable or plant)', is a slightly loose but fair rendering of the Arabic root (strictly the verb is 'to mow, \"\n   \"cut; to dry up' and the 'dried' is in the noun). Because the Hebrew cognate ḥāšaš exists, the root is really \"\n   \"common West-Semitic rather than exclusively Arabic, but the Arabic branch alone produced ḥašīš and all the words \"\n   \"on this chart, so 'Arabic' is a defensible label. The one part of the chart that modern scholarship rejects is \"\n   \"not the etymology but the history attached to it in node #1: there is no evidence the Nizārī Ismāʿīlīs actually \"\n   \"used hashish (see the node).\"),\n \"note_fa\": (\"ریشهٔ عربی «ح‌ش‌ش» واقعی است: فعل حَشَّ «علف دُرودن، گیاه بریدن» و دربارهٔ گیاه «خشک شدن»، و اسمِ حشیش \"\n   \"«علفِ خشک، گیاهِ درو شده». کلاین در همان صفحه‌ای که نورایی ارجاع داده (ص۷۰۶) می‌نویسد حشیشِ عربی «شاهدانه» و در \"\n   \"اصل «علفِ خشک» است و با «חשש» عبری («علف خشک») هم‌ریشه است؛ پس معنایی که نورایی برای ریشه آورده — «خشک کردن \"\n   \"(گیاه)» — با اندکی تسامح درست است، هرچند دقیق‌تر آن است که مفهومِ «خشکی» در اسم نهفته است نه در فعل. وجودِ صورت \"\n   \"عبری نشان می‌دهد ریشه سامیِ غربی است نه ویژهٔ عربی، ولی چون همهٔ واژه‌های این نمودار از شاخهٔ عربی برخاسته‌اند \"\n   \"برچسبِ «عربی» پذیرفتنی است. ادعای نورایی در جعبهٔ ریشه درست است؛ آنچه پژوهش امروزی رد می‌کند داستانِ حشیش‌خواریِ \"\n   \"اسماعیلیان است (نگاه کنید به گرهٔ ۱).\"),\n \"sources\": [W + \"%D8%AD%D8%B4%D9%8A%D8%B4\", \"https://www.etymonline.com/word/assassin\"],\n \"ref_check\": [\n   {\"ref\": \"KLN:706\", \"status\": \"supports\",\n    \"note\": \"KLN_1966.txt form-feed leaf 380, s.v. hashish: 'hashish, n., an intoxicating drink made from hemp. — Arab. hashish, ‘hemp’, prop. ‘dried grass’, rel. to Heb. hashash, ‘dried grass’. Cp. assassin.' Exactly the root sense Nourai's box gives.\"},\n   {\"ref\": \"FVA:102\", \"status\": \"not_checked\",\n    \"note\": \"S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (1368/1989) — refs_online.json records no digital copy on any permitted platform (re-searched 2026-09); catalogue record only.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"leaf 380, s.v. hashish\", \"stance\": \"supports\",\n    \"note\": \"'Arab. hashish, ‘hemp’, prop. ‘dried grass’, rel. to Heb. hashash, ‘dried grass’.'\"},\n   {\"src\": \"LKT\", \"where\": \"no. 839 (LKT.txt line 2030), 'Ar. hasis'\", \"stance\": \"supports\",\n    \"note\": \"Lokotsch's entry 839 heads the word 'Ar. ḥašīš: ‘Gras, Heu’, später beng … oder indischer Hanf, Cannabis indica' — the same 'grass/hay' → 'hemp' development; the entry's running foot points back to '[Ar. ḥašš…]', i.e. the same root.\"},\n   {\"src\": \"MON\", \"where\": \"MON_part1.txt line 53479, s.v. حشیش\", \"stance\": \"supports\",\n    \"note\": \"«حشیش: [ع.] (اِ.) (گیا.) گیاه خشک (واحد حشیشه). (گیا.) شاهدانه.» — Moʿin gives both the 'dry plant' sense and the cannabis sense and marks the word [ع.] = Arabic.\"}\n ],\n \"nodes\": []\n}\n\ne0[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Arabic\", \"words\": \"hašîš; Hašâšîn\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"ḥašīš is the regular fiʿīl noun of ḥ-š-š, 'mown/dried herbage, hay' (Lane s.v.); in medieval Arabic \"\n   \"it narrows to the resin and dried tops of Cannabis sativa, the sense in which the word is current from the 12th c. \"\n   \"The second word is the nisba ḥašīšī, plural ḥašīšiyya / ḥaššāšīn, 'hashish people'. As a name for the Nizārī \"\n   \"Ismāʿīlīs it is first attested in the Fatimid caliph al-Āmir's epistle of 1123 and then in Syrian and Egyptian \"\n   \"chroniclers of the 12th–13th c.; it is applied to the SYRIAN Nizārīs, and never appears in the Persian sources \"\n   \"about Alamūt. Nourai's gloss — 'hemp users, referred to the followers of Hasan Sabbâh who used to kill their \"\n   \"political enemies after using Hashîsh' — is the Crusader legend as Marco Polo popularised it. Modern scholarship \"\n   \"(M. G. S. Hodgson, The Order of Assassins, 1955; F. Daftary, The Assassin Legends, 1994) reads ḥašīšī as a term of \"\n   \"abuse meaning 'low-class rabble, herb-eaters', and Etymonline states flatly 'there is no evidence that the medieval \"\n   \"Ismailis used hashish'. The word and its formation from the root are certain; the historical explanation attached \"\n   \"to it in the gloss is not.\"),\n \"derivation_fa\": (\"«حشیش» صورتِ فَعیلِ ریشهٔ ح‌ش‌ش است به معنای «علفِ درو شده و خشک»، و از سدهٔ ششم هجری به معنای \"\n   \"شیره و سرشاخهٔ خشکِ شاهدانه به کار رفته است. واژهٔ دوم، «حشیشی» و جمعِ آن «حشیشیّه/حشّاشین»، نخست در رسالهٔ خلیفهٔ \"\n   \"فاطمی الآمر (۵۱۷ق) و سپس در تواریخ شام و مصر بر اسماعیلیانِ نزاریِ شام اطلاق شده است، نه بر نزاریانِ الموت؛ در \"\n   \"منابع فارسی چنین نامی برای پیروان حسن صبّاح نیامده است. توضیحِ نورایی — «حشیش‌خوارانی که پس از خوردنِ حشیش دشمنان \"\n   \"سیاسی خود را می‌کشتند» — همان افسانهٔ جنگ‌های صلیبی است که مارکوپولو رواج داد؛ پژوهش امروزی (هاجسن ۱۹۵۵، دفتری \"\n   \"۱۹۹۴) «حشیشی» را دشنامی به معنای «فرومایه، علف‌خوار» می‌داند و اتیمآنلاین تصریح می‌کند که هیچ گواهی بر حشیش‌خواریِ \"\n   \"اسماعیلیان در دست نیست. پس اشتقاقِ واژه درست، اما داستانِ همراهِ آن پذیرفتنی نیست.\"),\n \"sources\": [\"https://www.etymonline.com/word/assassin\", W + \"%D8%AD%D8%B4%D9%8A%D8%B4\"],\n \"ref_check\": [\n   {\"ref\": \"KLN:706\", \"status\": \"supports\",\n    \"note\": \"KLN_1966.txt leaf 380 s.v. hashish gives the root sense; the companion entry (leaf 72, s.v. assassin) gives the sect: 'Arab. hashshashin, ‘drinkers of hashish’, fr. hashish, ‘hemp’ … The first assassins were the fanatic followers of the Shaykh-ul-Jabal (the Old Man of the Mountains)'. Klein carries the same legend Nourai repeats.\"},\n   {\"ref\": \"FVA:102\", \"status\": \"not_checked\", \"note\": \"no digital copy of Nahvi's dictionary (refs_online.json).\"}\n ],\n \"consulted\": [\n   {\"src\": \"LKT\", \"where\": \"no. 839 (LKT.txt lines 2030-2033)\", \"stance\": \"partial\",\n    \"note\": \"'aus dem ar. Namen dieser Sekte ḥaššāsīn entstand it. assassino ‘Meuchelmörder’' — Lokotsch confirms the word but reports the intoxication story only as the received tale ('deren neue Mitglieder, durch den Hanfrausch fanatisiert … Mordtaten begingen'), and he notes Lammens's rival derivation from the name Ḥasan ibn Ṣabbāḥ, which he rejects.\"},\n   {\"src\": \"DEV\", \"where\": \"p. ~26, s.v. Assassin (DEV.txt lines 561-569)\", \"stance\": \"supports\",\n    \"note\": \"'personne ne doute aujourd'hui que le nom d'Assassins donné aux Ismaéliens ou Bathéniens ne soit l'adjectif arabe ḥachāchī ou ḥachīchī, dérivé de ḥachich' — Devic derives the sect name from ḥašīš, as Nourai does.\"},\n   {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt line 12033-12034, s.v. assassin\", \"stance\": \"partial\",\n    \"note\": \"'[Fr. assassin, from Ar. hashsha-shin, hashish eaters, from hashish, hemp.] 1. [A-], a member of a secret band of hashish-eating Moslems who killed Christian leaders during the Crusades' — same etymology, same legendary gloss.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Persian\", \"words\": \"hašîš «حشیش»\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"New Persian حشیش is an unaltered Arabic loan taken over after the Islamic conquest, spelling and all \"\n   \"(the ḥāʾ and the two šīns are Arabic orthography that Persian keeps without changing the pronunciation, which is \"\n   \"hašiš with h). It is not an inherited Iranian word: Persian's own names for the plant and the drug are شاهدانه \"\n   \"šāh-dāne (Pahlavi šāh-dānak) and بنگ bang (Av. baŋha-). Moʿin marks the word [ع.] 'Arabic' and glosses it \"\n   \"«گیاه خشک (واحد حشیشه)؛ شاهدانه», i.e. he transmits both the 'dried herb' and the cannabis sense; Borhān-e Qāṭeʿ, \"\n   \"in Moʿin's footnote to شاهدانه, says the resin of the plant «را حشیش می‌نامند». The direction of borrowing \"\n   \"(Arabic → Persian) that Nourai draws is right.\"),\n \"derivation_fa\": (\"«حشیش» در فارسی نو وام‌واژه‌ای عربی است که پس از اسلام بی هیچ دگرگونی، حتی با املای عربی، به فارسی \"\n   \"آمده است. واژهٔ ایرانیِ همین گیاه «شاهدانه» (فارسی میانه šāh-dānak) و «بنگ» (اوستایی baŋha-) است، پس حشیش وام‌واژه \"\n   \"است نه واژهٔ بومی. معین آن را با نشانِ [ع.] آورده و «گیاه خشک (واحدِ حشیشه)؛ شاهدانه» معنی کرده، و در حاشیهٔ خود بر \"\n   \"«شاهدانه» در برهان قاطع می‌نویسد گَردِ آن گیاه را «حشیش» می‌نامند. جهتِ وام‌گیری که نورایی کشیده (عربی ← فارسی) \"\n   \"درست است.\"),\n \"sources\": [W + \"%D8%AD%D8%B4%D9%8A%D8%B4\"],\n \"ref_check\": [\n   {\"ref\": \"FVA:102\", \"status\": \"not_checked\",\n    \"note\": \"Nahvi's dictionary of Arabic words in Persian is not digitised (refs_online.json, re-searched 2026-09). Its subject matter — Arabic words used in Persian — is however exactly the claim of this node, and the claim is independently confirmed by Moʿin.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"MON_part1.txt line 53479 s.v. حشیش\", \"stance\": \"supports\",\n    \"note\": \"«حشیش: [ع.] (اِ.) (گیا.) گیاه خشک (واحد حشیشه). (گیا.) شاهدانه.» — explicitly tagged as an Arabic loan.\"},\n   {\"src\": \"BQT\", \"where\": \"BQT_v3_pages.txt line 1585, Moʿin's footnote to شاهدانه (pdf page 25-26)\", \"stance\": \"supports\",\n    \"note\": \"«… Cannabis sativa … و تمام آن پوشیده از کرک‌های آلوده به روغن اساسی متعفن و سمی است که آن را بنگ و گرد آن را حشیش می‌نامند» — Borhān/Moʿin use حشیش for the resin of شاهدانه (whose Pahlavi form šāh_dānak he gives from Unvala), i.e. the native word is šāhdāne and ḥašīš is the Arabic term.\"},\n   {\"src\": \"HRN\", \"where\": \"grep 'hasis/Haschisch' in HRN.txt — no hit\", \"stance\": \"silent\",\n    \"note\": \"Horn's Grundriss covers inherited Persian vocabulary and has no entry for the Arabic loan; likewise Hübschmann's Persische Studien (grep in HUB.txt: no hit). Their silence is expected and is not evidence against the node.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 3, \"lang\": \"English\", \"words\": \"hašiš\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"English hashish (also hasheesh, hashisch) is a direct learned borrowing of Arabic ḥašīš, first \"\n   \"recorded in English travel writing about the Levant in the 16th–17th c. and made common in the 19th c. under the \"\n   \"influence of French haschisch/hachisch (Silvestre de Sacy's 1809 memoir on the Assassins, Théophile Gautier's \"\n   \"Club des Hachichins, 1844). Klein KLN:706 gives precisely 'hashish, n. … — Arab. hashish, ‘hemp’', i.e. a \"\n   \"borrowing straight from Arabic with no Romance intermediary, which is what Nourai's arrow shows. The only \"\n   \"quibble is orthographic: the box prints 'hašiš', Nourai's own transliteration of the Arabic, not the English \"\n   \"spelling hashish — the printed page does show 'hašiš', so this is the book's transliteration habit, not a \"\n   \"misreading of the scan.\"),\n \"derivation_fa\": (\"واژهٔ انگلیسی hashish (نیز hasheesh) وام‌گیریِ مستقیم از «حشیش» عربی است؛ نخست در سفرنامه‌های \"\n   \"اروپاییانِ شام در سده‌های شانزدهم و هفدهم میلادی دیده می‌شود و در سدهٔ نوزدهم، به‌ویژه از راهِ فرانسویِ haschisch \"\n   \"(رسالهٔ سیلوستر دو ساسی ۱۸۰۹ و «انجمن حشیشیان» تئوفیل گوتیه ۱۸۴۴)، همگانی شده است. کلاین در همان ص۷۰۶ می‌نویسد \"\n   \"hashish یکسر از عربی گرفته شده و واسطهٔ رومی ندارد؛ همان چیزی که پیکانِ نورایی نشان می‌دهد. تنها نکته املایی است: \"\n   \"کتاب در جعبهٔ «انگلیسی» صورتِ آوانگاشتِ عربی «hašiš» را چاپ کرده نه املای انگلیسیِ hashish؛ تصویر صفحه نشان می‌دهد \"\n   \"این شیوهٔ آوانگاریِ خودِ نورایی است، نه خطای اسکن. ادعای نورایی درست است.\"),\n \"sources\": [\"https://www.etymonline.com/word/assassin\"],\n \"ref_check\": [\n   {\"ref\": \"KLN:706\", \"status\": \"supports\",\n    \"note\": \"KLN_1966.txt leaf 380: 'hashish, n., an intoxicating drink made from hemp. — Arab. hashish, ‘hemp’, prop. ‘dried grass’ … Cp. assassin.' Klein derives the English word directly from Arabic, exactly as drawn.\"}\n ],\n \"consulted\": [\n   {\"src\": \"LKT\", \"where\": \"no. 839\", \"stance\": \"supports\",\n    \"note\": \"'in die europäischen Sprachen ist das Wort fast unverändert übergegangen: frz. hachiche, russ. gašiš, dtsch. Haschisch' — a direct, essentially unchanged borrowing into the European languages, English included.\"},\n   {\"src\": \"HJB\", \"where\": \"s.v. BANG, BHANG (HJB.txt lines 2764-2767)\", \"stance\": \"supports\",\n    \"note\": \"'Hashish of the Arabs is substantially the same … Birdwood says it ‘consists of the tender tops of the plants after flowering’' — Hobson-Jobson uses the anglicised word and identifies it with Cannabis indica.\"},\n   {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt s.v. assassin (line 12033)\", \"stance\": \"supports\",\n    \"note\": \"'from hashish, hemp' — Webster treats hashish as the English form of the Arabic word.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 4, \"lang\": \"Italian\", \"words\": \"assassino\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Italian assassino comes from the Arabic PLURAL ḥaššāšīn / ḥašīšiyyīn, taken over as a singular by \"\n   \"Italians in the Crusader Levant (Genoese, Pisan and Venetian traders in Syria in the 12th–13th c.); the Arabic \"\n   \"plural ending -īn was mistaken for part of the stem, the same accident that produced Bedouin from badawiyyīn \"\n   \"(Klein makes this comparison explicitly). Medieval Latin forms heissesin, assassi, assessini (Du Cange) and Old \"\n   \"French Assaci in Joinville show the word travelling with the Crusaders. In Italian it is already generalised from \"\n   \"'member of the sect' to 'hired killer' by Dante (Inferno XIX.50, 'lo perfido assassin'). NOTE: the book's gloss \"\n   \"'murder' is wrong — assassino is the agent noun 'assassin, murderer'; the abstract 'murder' is assassinio. The \"\n   \"printed page (pdf 223) really does read 'assassino : murder', so this is Nourai's slip, not the extraction's.\"),\n \"derivation_fa\": (\"assassino ایتالیایی از جمعِ عربیِ «حشّاشین/حشیشیّین» گرفته شده که ایتالیایی‌زبانانِ شام در روزگار \"\n   \"جنگ‌های صلیبی (بازرگانان جنووا و پیزا و ونیز، سده‌های ۱۲ و ۱۳ میلادی) آن را به‌عنوان صورتِ مفرد وام گرفتند؛ پایانهٔ \"\n   \"جمعِ عربی ‎-īn‎ بخشی از ستاک پنداشته شد — همان اتفاقی که در Bedouin از «بدویّین» رخ داد و کلاین نیز به آن اشاره \"\n   \"می‌کند. صورت‌های لاتینِ میانه heissesin و assassi و فرانسویِ کهن Assaci در سفرنامهٔ ژوانویل گواهِ انتقالِ واژه به \"\n   \"دستِ صلیبیان است. در ایتالیایی تا زمان دانته (دوزخ، سرود ۱۹) معنای «آدم‌کشِ اجیر» یافته است. یک نکته: معنایی که \"\n   \"کتاب داده («murder» = قتل) نادرست است؛ assassino یعنی «قاتل» و قتل assassinio است. تصویر صفحه نشان می‌دهد که خودِ \"\n   \"کتاب چنین چاپ کرده، پس خطا از نورایی است نه از استخراج.\"),\n \"sources\": [\"https://www.etymonline.com/word/assassin\"],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\",\n    \"note\": \"Nourai gives no reference for the Italian box; the claim is however covered by the KLN:115 he cites on the daughter node, which routes English assassin 'F., fr. It. assassino, fr. Arab. hashshashin'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"LKT\", \"where\": \"no. 839 (LKT.txt line 2033)\", \"stance\": \"supports\",\n    \"note\": \"'aus dem ar. Namen dieser Sekte ḥaššāšīn entstand it. assassino ‘Meuchelmörder’, prov. asasi, ansesi, frz. assassin, sp. asesino, pg. assassino, rum. asasin' — note Lokotsch's gloss 'Meuchelmörder' (murderer), not 'murder'.\"},\n   {\"src\": \"DEV\", \"where\": \"DEV.txt line 568, s.v. Assassin\", \"stance\": \"supports\",\n    \"note\": \"'Le Dictionnaire de Du Cange cite les formes de bas latin heissesin, assassi, assassini, assesini' and 'l'espagnol asesino et le portugais assassino … reçus par l'intermédiaire du français ou de l'italien assassino'.\"},\n   {\"src\": \"LAM\", \"where\": \"LAM.txt lines 1870-1871\", \"stance\": \"contradicts\",\n    \"note\": \"Lammens finds it 'étrange que dans toutes les formes du mot assassin les deux š aient disparu' and proposes deriving the word from the name Ḥasan(-i Ṣabbāḥ) instead; Lokotsch (no. 839) rejects this ('jedoch scheint diese Annahme nicht notwendig'), and so does modern scholarship. Recorded here as the one dissenting voice in the library.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 5, \"lang\": \"English\", \"words\": \"assassin, assassinate\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"English assassin is first recorded in the 1530s as the sect name and by the mid-16th c. as a common \"\n   \"noun 'hired killer'; assassinate follows c.1600 (verb) from Medieval Latin assassinatus / Italian assassinare. \"\n   \"Klein (KLN:115) routes it 'F., fr. It. assassino, fr. Arab. hashshashin' — i.e. English ← French ← Italian ← \"\n   \"Arabic; Etymonline agrees ('the word traveled through Italian and French before entering English around the \"\n   \"1530s'). Nourai's chart draws Italian → English directly and omits the French step his own source supplies; that \"\n   \"is a simplification rather than an error, since both Italian assassino and French assassin were available to \"\n   \"16th-century English. The route and the ultimate Arabic source are correct.\"),\n \"derivation_fa\": (\"assassin در انگلیسی نخست در دههٔ ۱۵۳۰ به‌عنوان نامِ آن فرقه و از میانهٔ سدهٔ شانزدهم به معنای «قاتلِ \"\n   \"اجیر» به کار رفته، و assassinate از حدود ۱۶۰۰ از لاتینِ میانهٔ assassinatus / ایتالیاییِ assassinare ساخته شده است. \"\n   \"کلاین (ص۱۱۵) زنجیره را چنین می‌دهد: انگلیسی ← فرانسه ← ایتالیایی assassino ← عربی «حشّاشین»؛ اتیمآنلاین نیز همین \"\n   \"مسیر را می‌آورد. نورایی حلقهٔ فرانسه را — که منبعِ خودش آورده — انداخته و پیکان را یکراست از ایتالیایی به انگلیسی \"\n   \"کشیده است؛ این ساده‌سازی است نه خطا، زیرا هر دو صورتِ ایتالیایی و فرانسوی در سدهٔ شانزدهم در دسترسِ انگلیسی بوده‌اند. \"\n   \"ادعای نورایی در اصل درست است.\"),\n \"sources\": [\"https://www.etymonline.com/word/assassin\"],\n \"ref_check\": [\n   {\"ref\": \"KLN:115\", \"status\": \"supports\",\n    \"note\": \"KLN_1966.txt form-feed leaf 72, s.v. assassin: 'assassin, n., murderer. — F., fr. It. assassino, fr. Arab. hashshashin, ‘drinkers of hashish’, fr. hashish, ‘hemp’; see hashish. … The plural suff. -in in assassin was mistaken for part of the word. Cp. Bedouin. Derivatives: assassin-ate, tr. v., assassin-at-ion, n.' Klein covers assassin AND assassinate, exactly as the box lists them; the only difference from the chart is the French link Klein inserts.\"}\n ],\n \"consulted\": [\n   {\"src\": \"SKT\", \"where\": \"SKT.txt line 1048, s.v. Assassin (OCR damaged)\", \"stance\": \"supports\",\n    \"note\": \"'Assassin, a murderer. (F. — Ar.) F. assassin. From Arab. ḥašīšīn, [drink]ers of hashish, the name of a sect [of the] 11th century; the Old Man of the Mountain roused his followers' spirits [by means] of this drink and sent them to [kill their] enemies' — Skeat's route F. ← Ar., without the Italian.\"},\n   {\"src\": \"FSD\", \"where\": \"FSD_vol1.txt lines 26959-26964, s.v. assassin\", \"stance\": \"supports\",\n    \"note\": \"'2. [A-] One of a sect of Oriental fanatics that practised assassination; the original meaning. The sect was founded in Persia A.D. 1090, but afterward migrated to Mt. Lebanon, Syria … [F., < Ar. Hashshashin,' — Funk & Wagnalls gives the same Arabic source and the French mediation.\"},\n   {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt lines 12033-12041\", \"stance\": \"supports\",\n    \"note\": \"'as-sas/sin, n. (Fr. assassin, from Ar. hashsha-shin, hashish eaters, from hashish, hemp.)' with 'as-sas/sin-ate, v.t.' following — both words of the box.\"}\n ]\n})\ndoc[\"entries\"].append(e0)\n\n# ------------------------------------------------------------------ entry 1\ne1 = {\n \"entry\": 1,\n \"root\": \"Hyakinthos\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"Ancient Greek ὑάκινθος (huákinthos), earlier *ϝάκινθος, a flower (bluebell / larkspur / iris / gladiolus) and a blue gem; a Pre-Greek (Mediterranean substrate) word\",\n \"note\": (\"The root box is right: ὑάκινθος is a real Greek word for a bulbous spring flower and, secondarily, for a \"\n   \"blue-to-red gem, and it is one of the textbook Pre-Greek words — the -νθ- suffix is the classic marker of the \"\n   \"Aegean substrate (Beekes, Etymological Dictionary of Greek, s.v.; Klein KLN:752 'fr. earlier *ϝάκινθος, a \"\n   \"pre-Hellenic word'; Etymonline 'probably ultimately from a non-Indo-European Mediterranean language'). Nourai's \"\n   \"own added line, 'The word is apparently a pre-Hellenic word of the Mediterranean origin', is therefore confirmed, \"\n   \"and it is why the word is absent from Watkins/AHD's Indo-European appendix. His second added line, 'BQT:2420 and \"\n   \"SNS:299 interpret the Greek word as ‘a kind of poison’', needs splitting. SNS:299 does say that: read from the \"\n   \"page image (saved as data/verification/sources/refs/ocr/SNS/299.png), Tavoosi writes «این واژه اصلاً یونانی \"\n   \"hyakinthos و لاتین hyacinthus به معنی نوعی زهر است». BQT:2420 does NOT: Moʿin's footnote 2 there reads «یاقوت از \"\n   \"یونانی hyakinthos (بمعنی نوعی از زهر)» where زهر is the Arabic word for BLOSSOM, not the Persian zahr 'poison' — \"\n   \"proved by what Moʿin writes in the very next clause, that the plant is 'Iris germanica' and 'gladiolus communis', \"\n   \"both flowers. So Nourai (and Tavoosi before him) misread Moʿin's «زهر» ‘flower’ as ‘poison’; the Greek word \"\n   \"never meant a poison. The root itself stands as confirmed.\"),\n \"note_fa\": (\"جعبهٔ ریشه درست است: ὑάκινθος یونانی نامِ گلی پیازی و نیز نامِ گوهری کبود تا سرخ است، و از نمونه‌های \"\n   \"کلاسیکِ واژه‌های «پیشایونانی» است؛ پسوندِ ‎-νθ-‎ نشانهٔ شناختهٔ زیرلایهٔ اژه‌ای است (بیکس؛ کلاین ص۷۵۲: «از صورتِ \"\n   \"کهن‌ترِ *ϝάκινθος، واژه‌ای پیشاهلنی»). پس یادداشتِ نورایی دربارهٔ خاستگاه مدیترانه‌ایِ واژه پذیرفتنی است و به همین \"\n   \"سبب این واژه در پیوستِ ریشه‌های هندواروپاییِ واتکینز نیامده است. اما یادداشتِ دومِ او — که «برهان قاطع ۲۴۲۰ و \"\n   \"شایست‌ناشایست ۲۹۹ آن را نوعی زهر معنی کرده‌اند» — باید دو نیم شود: شایست‌ناشایست ص۲۹۹ به‌راستی می‌نویسد «به معنی \"\n   \"نوعی زهر است»؛ ولی حاشیهٔ ۲ معین در برهان ص۲۴۲۰ می‌نویسد «یاقوت از یونانی hyakinthos (بمعنی نوعی از زهر)» و در \"\n   \"همان جمله آن را Iris germanica و gladiolus communis می‌شناساند؛ یعنی «زهر» اینجا واژهٔ عربیِ «زَهر = گل، شکوفه» است \"\n   \"نه «زهرِ» فارسی. بنابراین نورایی (و پیش از او طاوسی) «زهر» معین را نادرست خوانده‌اند؛ واژهٔ یونانی هرگز معنای زهر \"\n   \"نداشته است. خودِ ریشه اما تأیید می‌شود.\"),\n \"sources\": [\"https://www.etymonline.com/word/hyacinth\", W + \"%D9%8A%D8%A7%D9%82%D9%88%D8%AA\"],\n \"ref_check\": [\n   {\"ref\": \"KLN:752\", \"status\": \"supports\",\n    \"note\": \"KLN_1966.txt form-feed leaf 405, s.v. hyacinth: '… fr. L. hyacinthus, ‘a kind of flower, the jacinth’, fr. Gk. ὑάκινθος, ‘wild hyacinth, bluebell’, fr. earlier *ϝάκινθος, a pre-Hellenic word.' Both the meaning and the 'pre-Hellenic' label of Nourai's box come straight from here.\"},\n   {\"ref\": \"AHD:644\", \"status\": \"not_checked\",\n    \"note\": \"Nourai's AHD page numbers in the 600s are pages of the MAIN dictionary of the 1975/76 New College edition (s.v. hyacinth), which is not openly available; only the Indo-European appendix is on disk (AHD_watkins1985.txt), and a grep of it for 'hyacinth' returns nothing — as expected, since a Pre-Greek word has no IE root entry. The absence is consistent with, not contrary to, Nourai's own 'pre-Hellenic' note.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"leaf 405, s.vv. hyacinth, Hyacinthus\", \"stance\": \"supports\",\n    \"note\": \"'Hyacinthus, n., a beautiful youth, beloved and slain by Apollo (Greek mythology). — L. Hyacinthus, fr. Gk. Ὑάκινθος' and, s.v. hyacinth, '1) a fabulous flower supposed to have sprung from the blood of Hyacinthus; whence 2) among the ancients, a precious stone of blue color; now, a red or brownish variety of zircon.' Klein already links the flower and the gem, which is the hinge of this whole chart.\"},\n   {\"src\": \"FSD\", \"where\": \"FSD_vol2.txt lines 50631-50637, s.vv. Hyacinthia, Hyacinthus\", \"stance\": \"supports\",\n    \"note\": \"'Hyacinthus … A beautiful youth of Amyclæ, beloved of Apollo … Apollo, unable to save him, changed him into the flower called hyacinth' and 'Bot. A notable genus of Old World plants of the lily family (Liliaceæ), with coated bulbs, narrow radical leaves … a raceme of often handsome bell-shaped flowers' — the 'bulbous plant with a cluster of very fragrant flowers' of Nourai's gloss.\"},\n   {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt, grep 'hyacinth' — no hit\", \"stance\": \"silent\",\n    \"note\": \"No entry in Watkins's Indo-European roots, as expected for a Pre-Greek substrate word.\"},\n   {\"src\": \"POK\", \"where\": \"grep 'hyakinth/ὑάκινθ' in POK_full.txt — no hit\", \"stance\": \"silent\",\n    \"note\": \"Pokorny has no IEW entry for the word; again consistent with a non-Indo-European origin.\"}\n ],\n \"nodes\": []\n}\n\ne1[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Pahlavi\", \"words\": \"yâkand\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"Middle Persian yakand 'ruby' is genuine and well attested: MacKenzie's Concise Pahlavi Dictionary has \"\n   \"'yakand [ykknd, -nt' | Psalter ykwnd, New Persian the same] ruby'. But the arrow as Nourai draws it — Greek \"\n   \"ὑάκινθος straight into Pahlavi — skips the mediation that the standard handbooks insist on. Hübschmann, Persische \"\n   \"Studien p. 151, states it flatly: 'yakand ‘Rubin’ aus dem Aramäischen (syr. ܝܩܘܢܕܬܐ usw., gr. ὑάκινθος, Nöldeke, \"\n   \"Pers. Stud. II, 44) entlehnt' — i.e. the word reached Iranian from Aramaic/Syriac yāqūndtā, itself from the Greek. \"\n   \"The Syriac form with -nd- is exactly what yields Pahlavi -kand (Greek -νθ- → Aramaic -nd- → MP -nd), which a \"\n   \"direct Greek borrowing would not explain so neatly. So the ultimate source Nourai names is right and the Pahlavi \"\n   \"form is right; the route is under-specified. Tavoosi (SNS:299), Nourai's own reference, likewise gives only \"\n   \"'yākand … اصلاً یونانی hyakinthos و لاتین hyacinthus' without the Aramaic stage.\"),\n \"derivation_fa\": (\"فارسی میانهٔ yakand «یاقوت، لعل» صورتی واقعی و مضبوط است: مکنزی در فرهنگ کوچکِ پهلوی می‌آورد \"\n   \"«yakand [ykknd, -nt] ruby»، و صورتِ زبورِ پهلوی را ykwnd ثبت می‌کند. اما پیکانی که نورایی کشیده — یونانی ← پهلوی \"\n   \"به‌طورِ مستقیم — واسطه را انداخته است. هوبشمان در «پژوهش‌های فارسی» ص۱۵۱ صریح می‌نویسد: «yakand ‘لعل’ از آرامی \"\n   \"وام گرفته شده (سریانی yāqūndtā و مانند آن، از یونانیِ ὑάκινθος؛ نُلدکه)». صورتِ سریانی با ‎-nd-‎ درست همان چیزی است \"\n   \"که ‎-kand‎ پهلوی را توضیح می‌دهد (‎-νθ-‎ یونانی ← ‎-nd-‎ آرامی ← ‎-nd‎ فارسی میانه)، حال آنکه وام‌گیریِ مستقیم از \"\n   \"یونانی این را چنین روشن توجیه نمی‌کند. پس خاستگاهِ نهایی و صورتِ پهلوی درست است ولی مسیر ناقص است: ادعای نورایی \"\n   \"با احتیاط پذیرفتنی است.\"),\n \"sources\": [W + \"%D9%8A%D8%A7%D9%82%D9%88%D8%AA\"],\n \"ref_check\": [\n   {\"ref\": \"SNS:299\", \"status\": \"supports\",\n    \"note\": \"Read from the page image (archive.org VajnameShayest leaf n167 = printed p. 299, saved as data/verification/sources/refs/ocr/SNS/299.png; transcribed in 299.vision.txt). Tavoosi's entry: «yākand: یاکند، یاقوت … این واژه اصلاً یونانی: hyakinthos و لاتین: hyacinthus به معنی نوعی زهر است، یاقوت معرّب یاکند فارسی است …». It does support a Greek origin for yākand (and it is the source of Nourai's 'a kind of poison' note), but it names no Aramaic intermediary.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"PHD.txt line 669, s.v. yakand\", \"stance\": \"supports\",\n    \"note\": \"'yakand [ykknd, -nt' | P ykwnd, N ~] ruby.' — MacKenzie confirms the Pahlavi word, its heterographic spelling, its Psalter form and its survival into New Persian; PHD.txt line 3485 has the reverse index entry 'ruby yakand.'\"},\n   {\"src\": \"HUB\", \"where\": \"Persische Studien p. 151 (HUB.txt line 5305, form-feed block 161 headed '— 151 —')\", \"stance\": \"partial\",\n    \"note\": \"'die Wörter Yunan …, Yūsuf, yāqūt ‘Hyacinth, Rubin’ sind aus dem Arabischen, yakand ‘Rubin’ aus dem Aramäischen (syr. ܝܩܘܢܕܬܐ usw., gr. ὑάκινθος, Nöldeke, Pers. Stud. II, 44) entlehnt.' Same ultimate Greek source, but through Aramaic — hence 'partial'.\"},\n   {\"src\": \"NYB\", \"where\": \"grep 'yakand' in NYB_vol1/vol2 — no hit\", \"stance\": \"silent\",\n    \"note\": \"Nyberg's Pahlavi glossary (which covers the Manual's texts only) does not contain the word.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Persian\", \"words\": \"yâkand «یاکند»\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"New Persian یاکند yākand 'ruby' is the straightforward continuation of Pahlavi yakand, with no sound \"\n   \"change to explain. It is an early-classical word: Asadi Ṭusi's Loghat-e Fors p. 93 registers it with a verse of \"\n   \"Šākir-e Boḵārī, «کجا تو باشی گردند بی‌خطر خوبان / جمست را چه خطر هر کجا بود یاکند» (the same verse turns up in \"\n   \"Ṣeḥāḥ al-Fors), and Moʿin quotes it in footnote 5 to Borhān-e Qāṭeʿ p. 2420 with the gloss «یاکند یاقوت باشد». \"\n   \"Borhān itself has the headword: «یاکند، بفتح کاف بروزن یابند، بمعنی یاقوت است و آن جوهری باشد معروف». By the \"\n   \"Safavid period the word is archaic and yāqūt has replaced it. The node is exactly right.\"),\n \"derivation_fa\": (\"«یاکند» در فارسی نو دنبالهٔ بی‌واسطهٔ yakand فارسی میانه است و هیچ دگرگونی آوایی‌ای نیاز به توضیح \"\n   \"ندارد. واژه‌ای کهن و کلاسیک است: اسدی طوسی در «لغت فرس» ص۹۳ آن را با بیتی از شاکر بخاری ثبت کرده — «کجا تو باشی \"\n   \"گردند بی‌خطر خوبان / جمست را چه خطر هر کجا بود یاکند» — و معین همان بیت را در حاشیهٔ ۵ برهان قاطع ص۲۴۲۰ آورده است. \"\n   \"خودِ برهان مدخل دارد: «یاکند، بفتح کاف بروزن یابند، بمعنی یاقوت است و آن جوهری باشد معروف». از دورهٔ صفوی به بعد \"\n   \"این واژه کهنه شده و «یاقوت» جای آن را گرفته است. ادعای نورایی در این گره درست است.\"),\n \"sources\": [W + \"%D9%8A%D8%A7%D9%82%D9%88%D8%AA\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:2420\", \"status\": \"supports\",\n    \"note\": \"Verified on the page image (data/verification/sources/refs/ocr/BQT/2420.png; BQT_v4_pages.txt pdf page 503, the following page opening '۲۴۲۱'). The headword «یاکند - بفتح کاف بروزن یابند، بمعنی یاقوت است و آن جوهری باشد معروف» stands in the right-hand column, with footnote 5 «رک: یاقوت. ‘یاکند یاقوت باشد. شاکر بخاری گفت …’ لغت فرس ص۹۳». Nourai's page number is exact.\"},\n   {\"ref\": \"MON:5247\", \"status\": \"not_checked\",\n    \"note\": \"Only the 2-volume Adena abridgement of Moʿin is on disk (MON_part1/2.txt, different pagination and no page breaks); a grep of MON_part2.txt for یاکند returns nothing, and the online Moʿin at vajehyab/abadis cannot be mapped to page numbers. The 6-volume page 5247 could not be reached.\"},\n   {\"ref\": \"MZF:340\", \"status\": \"not_checked\",\n    \"note\": \"refs_online.json records MZF (Nāṭel Ḵānlarī) as not identified and not online.\"}\n ],\n \"consulted\": [\n   {\"src\": \"FRS\", \"where\": \"Loghat-e Fors, FRS_pages.txt line 4647\", \"stance\": \"supports\",\n    \"note\": \"The Šākir-e Boḵārī verse «… بی‌خطر خوبان جمست را چه خطر هر کجا بود یاکند» is in Asadi's dictionary itself, confirming the word in 5th/11th-century Persian.\"},\n   {\"src\": \"BQT\", \"where\": \"printed p. 2420, headword یاکند and footnote 5\", \"stance\": \"supports\",\n    \"note\": \"«یاکند … بمعنی یاقوت است و آن جوهری باشد معروف».\"},\n   {\"src\": \"HUB\", \"where\": \"Persische Studien p. 151\", \"stance\": \"supports\",\n    \"note\": \"Hübschmann lists np. yakand among the y- words of Persian (borrowed, from Aramaic), i.e. he too takes the New Persian word for a real, inherited-from-Middle-Persian item rather than a lexicographers' ghost.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Arabic\", \"words\": \"yâqŭt\",\n \"verdict\": \"disputed\",\n \"derivation\": (\"This is the one arrow on the page that modern scholarship rejects. Nourai has Arabic yāqūt taken from \"\n   \"Persian yākand, and his two references do say so: Moʿin (BQT p. 2420 fn. 2) quotes Ḥamza al-Iṣfahānī through \"\n   \"Bīrūnī's al-Jamāhir p. 33 — «قال حمزة بن الحسن الاصفهانی ان اسمه (الیاقوت) بالفارسیة ‘یاکند’ … والیاقوت معربه» — \"\n   \"and Tavoosi (SNS:299) writes «یاقوت معرّب یاکند فارسی است». That is the medieval Arabic-Persian tradition of \"\n   \"muʿarrab lists, not a phonological derivation: yākand cannot give yāqūt (the -nd would have to vanish and a k \"\n   \"become q). Jeffery, The Foreign Vocabulary of the Qurʾān pp. 289-290, s.v. یاقوت (Q 55:58), sets it out: 'It was \"\n   \"very generally recognized as a loan-word from Persian … but the matter is not so simple, for the Modern Pers. \"\n   \"یاقوت is from the Arabic (Vullers), and the alternative form یاکند, like the Arm. yakundh, is from the Syr. \"\n   \"yāqūndtā. The ultimate source of the word is the Gk. ὑάκινθος … It was from Syr. yāqūndtā that the word passed \"\n   \"into Eth. and, with dropping of the weak n, into Arabic.' Hübschmann p. 151 says the same. Tobia al-Unaysi (TAD) \"\n   \"lists yāqūt among the Arabic words of Greek origin ('یاقوت — یونانی … وفی اللاتینیة hyacinthus'), with no Persian \"\n   \"step. Wiktionary derives Arabic ياقوت from Ancient Greek ὑάκινθος 'possibly via Sogdian yaγūt', again bypassing \"\n   \"yākand. So yākand and yāqūt are two SEPARATE borrowings of the same Greek word by two different routes, not \"\n   \"parent and child; the word is Qurʾānic and 'occurs in the old poetry, and thus must have been an early \"\n   \"borrowing' (Jeffery).\"),\n \"derivation_fa\": (\"این تنها پیکانِ این صفحه است که پژوهشِ امروزی آن را رد می‌کند. نورایی «یاقوتِ» عربی را از «یاکندِ» \"\n   \"فارسی گرفته است و هر دو مأخذش نیز همین را می‌گویند: معین در حاشیهٔ ۲ برهان ص۲۴۲۰ از حمزهٔ اصفهانی به نقلِ الجماهرِ \"\n   \"بیرونی ص۳۳ می‌آورد «ان اسمه (الیاقوت) بالفارسیة یاکند … والیاقوت معربه»، و طاوسی (شایست‌ناشایست ص۲۹۹) می‌نویسد \"\n   \"«یاقوت معرّبِ یاکندِ فارسی است». اما این سخنِ سنّتِ کتاب‌های «معرّبات» است نه اشتقاقی آوایی: از yākand به هیچ روی \"\n   \"yāqūt به دست نمی‌آید (باید ‎-nd‎ بیفتد و ک به ق بدل شود). آرتور جفری در «واژگان دخیل در قرآن» ص۲۸۹–۲۹۰ ذیل «یاقوت» \"\n   \"(الرحمن ۵۸) روشن می‌کند: فارسیِ نوِ «یاقوت» خود از عربی است، و «یاکند» مانند yakundh ارمنی از سریانیِ yāqūndtā \"\n   \"آمده؛ خاستگاهِ نهاییِ هر دو یونانیِ ὑάκινθος است و عربی آن را از سریانی گرفته با افتادنِ نونِ ضعیف. هوبشمان ص۱۵۱ نیز \"\n   \"همین را می‌گوید و طوبیا العنیسی «یاقوت» را در شمارِ واژه‌های یونانی‌تبارِ عربی آورده است. ویکی‌واژه نیز آن را از \"\n   \"یونانی و شاید به میانجیِ سغدیِ yaγūt می‌داند. پس «یاکند» و «یاقوت» دو وام‌گیریِ جداگانه از یک واژهٔ یونانی‌اند، نه \"\n   \"پدر و فرزند.\"),\n \"sources\": [W + \"%D9%8A%D8%A7%D9%82%D9%88%D8%AA\", \"https://www.etymonline.com/word/hyacinth\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:2420\", \"status\": \"supports\",\n    \"note\": \"Moʿin's footnote 2, read from the page image: «قال حمزة بن الحسن الاصفهانی ان اسمه (الیاقوت) بالفارسیة ‘یاکند’ (ه.م.) والیاقوت معربه …» «بیرونی. الجماهر ص۳۳». The reference does say what Nourai's arrow says — but it is reporting Ḥamza al-Iṣfahānī's 10th-century opinion, not modern philology.\"},\n   {\"ref\": \"SNS:299\", \"status\": \"supports\",\n    \"note\": \"From the page image (ocr/SNS/299.png): «یاقوت معرّب یاکند فارسی است که گوهری زینتی و سرخ رنگ و درخشان و پربها است». Same medieval claim, same page Nourai cites.\"}\n ],\n \"consulted\": [\n   {\"src\": \"FVQ\", \"where\": \"Jeffery pp. 289-290 (FVQ_pages.txt form-feed leaf 306), s.v. yāqūt\", \"stance\": \"contradicts\",\n    \"note\": \"'It was very generally recognized as a loan-word from Persian. Some Western scholars such as Freytag have accepted this at face value, but the matter is not so simple, for the Modern Pers. یاقوت is from the Arabic (Vullers, Lex, ii, 1507), and the alternative form یاکند, like the Arm. yakundh, is from the Syr. yāqūndtā. The ultimate source of the word is the Gk. ὑάκινθος … It was from Syr. yāqūndtā that the word passed into Eth. … and with dropping of the weak n into Arabic.'\"},\n   {\"src\": \"HUB\", \"where\": \"Persische Studien p. 151\", \"stance\": \"contradicts\",\n    \"note\": \"'yāqūt ‘Hyacinth, Rubin’ sind aus dem Arabischen, yakand ‘Rubin’ aus dem Aramäischen' — the two forms are kept apart, and Arabic is not derived from yakand.\"},\n   {\"src\": \"TAD\", \"where\": \"Tobia al-Unaysi, TAD.txt line 3052\", \"stance\": \"contradicts\",\n    \"note\": \"«یاقوت — یونانی [hyakinthos] وفی اللاتینیة hyacinthus وهو … لونه أحمر» — al-Unaysi's dictionary of foreign words in Arabic classes yāqūt as Greek, with no Persian intermediary.\"},\n   {\"src\": \"SOD\", \"where\": \"grep for the Sogdian ruby word in SOD.txt / SOD_pages.txt — no usable hit\", \"stance\": \"silent\",\n    \"note\": \"Wiktionary's proposed Sogdian intermediary (yγwth /yaγūt/) could not be located in Gharib's dictionary as digitised here, so that particular route remains unverified either way.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 4, \"lang\": \"Persian\", \"words\": \"yâqŭt «یاقوت»\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"This arrow is right, and it is right for a reason that undercuts the previous one: New Persian یاقوت \"\n   \"is a loan FROM Arabic. Jeffery p. 289 says so explicitly ('the Modern Pers. یاقوت is from the Arabic', citing \"\n   \"Vullers, Lex. ii, 1507) and Hübschmann p. 151 lists yāqūt among the Persian words that 'sind aus dem Arabischen'. \"\n   \"The Arabic form entered Persian in the Islamic period and displaced the older native yākand, which by the classical \"\n   \"lexicographers' time already needed glossing («یاکند یاقوت باشد»). The second sense Nourai gives, 'also red lips', \"\n   \"is the standard Persian poetic metaphor and is documented in the same Borhān-e Qāṭeʿ page: «یاقوت خام … کنایه از \"\n   \"لب معشوق است», «یاقوت سربسته - کنایه از [لبِ] معشوق - و لب‌های خاموش باشد», beside «یاقوت روان» and «یاقوت مذاب» \"\n   \"for red wine. The Ṣafāʾī Qahfarroḵī couplet the book quotes plays on exactly that. NOTE: because Arabic yāqūt is \"\n   \"not in fact from Persian yākand (node #3), this is not the Persian→Arabic→Persian round trip Nourai's chart \"\n   \"implies; it is a plain Greek → Aramaic → Arabic → Persian borrowing.\"),\n \"derivation_fa\": (\"این پیکان درست است، و درستیِ آن خودْ پیکانِ پیشین را سست می‌کند: «یاقوتِ» فارسی نو وام‌واژه‌ای عربی \"\n   \"است. جفری ص۲۸۹ می‌گوید فارسیِ نوِ یاقوت از عربی گرفته شده (به استنادِ فرهنگِ ولرس) و هوبشمان ص۱۵۱ نیز یاقوت را در \"\n   \"شمارِ واژه‌های عربی‌تبارِ فارسی آورده است. این صورتِ عربی در دورهٔ اسلامی وارد فارسی شد و جای «یاکندِ» کهن را گرفت، \"\n   \"چندان که فرهنگ‌نویسانِ کلاسیک ناچار شدند بنویسند «یاکند یاقوت باشد». معنای دومی که نورایی آورده — «لبِ سرخ» — \"\n   \"استعارهٔ شناختهٔ شعر فارسی است و در همان صفحهٔ برهان ثبت شده: «یاقوت خام … کنایه از لب معشوق است» و «یاقوت سربسته - \"\n   \"کنایه از معشوق - و لب‌های خاموش باشد»، در کنارِ «یاقوت روان» و «یاقوت مذاب» برای شرابِ سرخ؛ بیتِ صفایی قهفرخی نیز \"\n   \"بر همین ایهام است. نکته: چون یاقوتِ عربی در واقع از یاکندِ فارسی نیامده، این رفت‌وبرگشتِ فارسی←عربی←فارسی که \"\n   \"نمودار می‌نمایاند وجود ندارد؛ مسیرِ درست یونانی ← آرامی ← عربی ← فارسی است.\"),\n \"sources\": [W + \"%D9%8A%D8%A7%D9%82%D9%88%D8%AA\"],\n \"ref_check\": [\n   {\"ref\": \"SNS:299\", \"status\": \"partial\",\n    \"note\": \"Tavoosi (p. 299, from the page image) describes yāqūt as «گوهری زینتی و سرخ رنگ و درخشان و پربها» — supporting the meaning of the Persian word, but he calls it 'the arabicised yākand' rather than an Arabic loan into Persian, so the direction he implies is the reverse of what Jeffery and Hübschmann establish.\"},\n   {\"ref\": \"FAF:712\", \"status\": \"not_checked\",\n    \"note\": \"A. Daneshgar, Farhang-e Aʿlam-e Farsi (1370/1991) — refs_online.json: nothing digitised on any permitted platform (re-searched 2026-09).\"}\n ],\n \"consulted\": [\n   {\"src\": \"FVQ\", \"where\": \"Jeffery p. 289\", \"stance\": \"supports\",\n    \"note\": \"'the Modern Pers. یاقوت is from the Arabic (Vullers, Lex, ii, 1507)' — precisely this arrow.\"},\n   {\"src\": \"HUB\", \"where\": \"Persische Studien p. 151\", \"stance\": \"supports\",\n    \"note\": \"'yāqūt ‘Hyacinth, Rubin’ sind aus dem Arabischen … entlehnt.'\"},\n   {\"src\": \"BQT\", \"where\": \"printed p. 2420, the یاقوت article\", \"stance\": \"supports\",\n    \"note\": \"«یاقوت - با قاف بروزن هاروت، نام جوهری‌ست مشهور و آن سرخ و کبود و زرد می‌باشد» plus the metaphorical sub-entries «یاقوت خام … کنایه از لب معشوق است» and «یاقوت سربسته … ولب‌های خاموش باشد» — the 'red lips' sense of the box.\"},\n   {\"src\": \"MON\", \"where\": \"MON_part2.txt line 93377, s.v. یاقوت\", \"stance\": \"supports\",\n    \"note\": \"«یاقوت: (اِ.) (زم.) یکی از سنگ‌های آذرین که جزء کانی‌های سنگ‌های …» — Moʿin's abridgement carries the word as a current Persian noun.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 5, \"lang\": \"Latin\", \"words\": \"hyacinthus\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Latin hyacinthus is a straight learned borrowing of Greek ὑάκινθος, taken over with the Greek \"\n   \"aspirate written hy- and the -us of the second declension; it is in Virgil (Eclogues 3.63, the flower) and Pliny \"\n   \"(Nat. Hist. 37, the gem), and in the Vulgate for the blue stone of Revelation 21:20. Latin, like Greek, carries \"\n   \"both senses — flower and blue-to-red gem — which is why the Western branch of this chart ends in a flower name \"\n   \"while the Semitic branch ends in a gem name. Klein: 'fr. L. hyacinthus, ‘a kind of flower, the jacinth’, fr. Gk. \"\n   \"ὑάκινθος'.\"),\n \"derivation_fa\": (\"hyacinthus لاتین وام‌گیریِ ادبیِ مستقیم از ὑάκινθος یونانی است؛ دمیدگیِ یونانی به‌صورت hy- نوشته و \"\n   \"پایانهٔ صرفِ دومِ لاتین ‎-us‎ به آن افزوده شده است. این واژه در «چوپانی‌های» ویرژیل (۳٫۶۳، به معنای گل) و در \"\n   \"«تاریخ طبیعیِ» پلینی (کتاب ۳۷، به معنای گوهر) و در ترجمهٔ ولگات برای سنگِ کبودِ مکاشفه ۲۱٫۲۰ آمده است. لاتین نیز \"\n   \"مانند یونانی هر دو معنا — گل و گوهر — را دارد و همین است که شاخهٔ غربیِ این نمودار به نامِ گل و شاخهٔ سامیِ آن به \"\n   \"نامِ گوهر می‌انجامد. ادعای نورایی درست است.\"),\n \"sources\": [\"https://www.etymonline.com/word/hyacinth\"],\n \"ref_check\": [\n   {\"ref\": \"AHD:644\", \"status\": \"not_checked\",\n    \"note\": \"Page 644 of the 1975/76 AHD New College main dictionary (s.v. hyacinth); that volume is not openly available and the on-disk Watkins IE-roots appendix has no such entry. The chain is however fully covered by Klein and Etymonline (see consulted).\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"leaf 405, s.v. hyacinth\", \"stance\": \"supports\",\n    \"note\": \"'F. hyacinthe, fr. L. hyacinthus, ‘a kind of flower, the jacinth’, fr. Gk. ὑάκινθος, ‘wild hyacinth, bluebell’.'\"},\n   {\"src\": \"SKT\", \"where\": \"SKT.txt line 9001, s.v. hyacinth (OCR damaged)\", \"stance\": \"supports\",\n    \"note\": \"'…a flower. (F. — L. — Gk.) … L. hyacinthus. — Gk. [ὑάκινθος], an iris, larkspur [not our hyacinth]. [jac]inth, a precious stone. (F. — L.)' — Skeat gives the same F. ← L. ← Gk. route and warns that the ancient plant is not the modern hyacinth.\"},\n   {\"src\": \"FSD\", \"where\": \"FSD_vol2.txt line 50637, s.v. Hyacinthus\", \"stance\": \"supports\",\n    \"note\": \"'[L., see' — Funk & Wagnalls derives the botanical genus name from the Latin word.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 6, \"lang\": \"French\", \"words\": \"\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"An empty pass-through box for the French link. Two French forms are involved: the popular Old French \"\n   \"jacinte / jacinthe (12th c., from Latin hyacinthus with the regular Gallo-Romance loss of initial hy- and \"\n   \"assibilation), and the learned re-Latinised hyacinthe, restored in the 16th c. Klein's entry cites 'F. hyacinthe' \"\n   \"as the immediate source of the English word, so the box is exactly the link his source supplies; Etymonline notes \"\n   \"that English hyacinth was 're-Greeked from jacinth (late 14c.), which derived from Old French and Medieval Latin \"\n   \"forms'.\"),\n \"derivation_fa\": (\"این جعبه تهی است و تنها حلقهٔ فرانسه را نشان می‌دهد. دو صورتِ فرانسوی در کار است: صورتِ عامیانهٔ \"\n   \"فرانسویِ کهن jacinte/jacinthe (سدهٔ دوازدهم میلادی، از hyacinthus لاتین با افتادنِ hy- آغازی و سایشی‌شدنِ آن) و \"\n   \"صورتِ عالمانهٔ hyacinthe که در سدهٔ شانزدهم بازسازیِ لاتینی شد. کلاین منبعِ بی‌واسطهٔ واژهٔ انگلیسی را «F. hyacinthe» \"\n   \"می‌داند، پس این جعبه دقیقاً همان حلقه‌ای است که مأخذِ نورایی می‌دهد؛ اتیمآنلاین نیز می‌گوید صورتِ انگلیسیِ hyacinth \"\n   \"بازیونانی‌شدهٔ jacinth (اواخر سدهٔ چهاردهم) است که خود از فرانسویِ کهن و لاتینِ میانه آمده بود.\"),\n \"sources\": [\"https://www.etymonline.com/word/hyacinth\"],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\",\n    \"note\": \"The box carries no reference in the book; the link is supplied by KLN:752 cited on the root ('F. hyacinthe, fr. L. hyacinthus').\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"leaf 405, s.v. hyacinth\", \"stance\": \"supports\",\n    \"note\": \"'— F. hyacinthe, fr. L. hyacinthus' — the French stage is explicit in Klein.\"},\n   {\"src\": \"SKT\", \"where\": \"SKT.txt line 9001\", \"stance\": \"supports\",\n    \"note\": \"Skeat's formula '(F. — L. — Gk.)' for hyacinth, and separately for jacinth '(F. — L.)', both put French between Latin and English.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 7, \"lang\": \"English\", \"words\": \"hyacinth\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Middle English took the gem sense first, as jacinth (late 14c., Wycliffe's Bible, Rev. 21:20), from \"\n   \"Old French jacinte; the spelling hyacinth is a 16th-century re-Hellenising of that word after Latin/Greek, and \"\n   \"the modern flower sense (the garden Hyacinthus orientalis, introduced from the Ottoman lands) dates from the \"\n   \"1570s. English therefore has the doublet jacinth (gem) / hyacinth (flower and, in older use, gem) from one Greek \"\n   \"original. Nourai's chain Greek → Latin → French → English is the standard one.\"),\n \"derivation_fa\": (\"انگلیسیِ میانه نخست معنای گوهر را گرفت، به صورتِ jacinth (اواخر سدهٔ چهاردهم، در ترجمهٔ ویکلیف از \"\n   \"مکاشفه ۲۱٫۲۰) از فرانسویِ کهنِ jacinte؛ املای hyacinth بازسازیِ یونانی‌مآبانهٔ همان واژه در سدهٔ شانزدهم است و \"\n   \"معنای امروزیِ گل (سنبلِ باغی، Hyacinthus orientalis، که از قلمروِ عثمانی به اروپا آمد) از حدود ۱۵۷۰ رواج یافته \"\n   \"است. پس انگلیسی از یک اصلِ یونانی دو صورتِ دوگانه (doublet) دارد: jacinth «گوهر» و hyacinth «گل». زنجیرهٔ \"\n   \"یونانی ← لاتین ← فرانسه ← انگلیسیِ نورایی همان مسیرِ پذیرفتهٔ کتاب‌های مرجع است.\"),\n \"sources\": [\"https://www.etymonline.com/word/hyacinth\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"not_checked\",\n    \"note\": \"The box cites 'AHD' without a page; the main-dictionary entry of the 1975/76 New College edition is not openly available. Klein and Etymonline cover the same chain (see consulted).\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"leaf 405, s.v. hyacinth\", \"stance\": \"supports\",\n    \"note\": \"'hyacinth, n., 1) a fabulous flower … 2) among the ancients, a precious stone of blue color; now, a red or brownish variety of zircon. — F. hyacinthe, fr. L. hyacinthus … fr. Gk. ὑάκινθος … Cp. jacinth, Vaccinium.'\"},\n   {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt line 93139, s.v. hy'a-cinth\", \"stance\": \"supports\",\n    \"note\": \"'hy/a-cinth, n. (Fr. hyacinthe; L. hyacinthus, Gr. hyakinthos, the hyacinth.) 1. a plant of the genus Hyacinthus, belonging to the lily family … especially, the cultivated species, Hyacinthus orientalis' — the same three-step route and Nourai's 'bulbous plant with fragrant flowers'.\"},\n   {\"src\": \"SKT\", \"where\": \"SKT.txt line 9001\", \"stance\": \"supports\",\n    \"note\": \"'(F. — L. — Gk.)'.\"}\n ]\n})\ndoc[\"entries\"].append(e1)\n\n# ------------------------------------------------------------------ entry 2\ne2 = {\n \"entry\": 2,\n \"root\": \"H.y.y\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"Proto-Semitic *ḥyy / *ḥyw 'to live' (Arabic ḥayya/ḥayiya, Hebrew ḥāyāh, Aramaic-Syriac ḥayā, Ugaritic ḥwy/ḥyy)\",\n \"note\": (\"Correct in every part. Klein, the reference Nourai cites (KLN:552, s.v. Eve), gives the comparative set \"\n   \"himself: 'Heb. ḥāyāh, ‘he lived’, is rel. to Aram.-Syr. ḥayā, ‘he lived’, Ugar. ḥwy (ḥyy), ‘to live’, Arab. \"\n   \"ḥayya, ‘he lived’, Heb. ḥayyīm, Aram. ḥayyīn, ḥayyē, Arab. ḥayāh, ‘life’.' A root attested across Northwest \"\n   \"Semitic, Arabic and Ugaritic is by definition common Semitic, so Nourai's language label 'Semitic' — rather than \"\n   \"'Arabic', which he used for the H.š.š box above — is the right choice here. The gloss 'to live' is right. The \"\n   \"only weak link in the chart below is the Latin box (node #4), where the book prints the English form 'Eve' \"\n   \"instead of Latin Eva, and where the Greek Εὕα of the Septuagint, the actual bridge from Hebrew to Latin, is \"\n   \"missing.\"),\n \"note_fa\": (\"این ریشه در همهٔ اجزا درست است. کلاین در همان ص۵۵۲ که نورایی ارجاع داده (ذیل Eve) خودْ مجموعهٔ تطبیقی را \"\n   \"می‌دهد: «عبری ḥāyāh ‘زیست’ با آرامی-سریانی ḥayā، اوگاریتی ḥwy/ḥyy، و عربی ḥayya هم‌ریشه است؛ و عبری ḥayyīm، \"\n   \"آرامی ḥayyīn/ḥayyē و عربی ḥayāh همه ‘زندگی’ معنی می‌دهند». ریشه‌ای که هم در سامیِ شمالِ غربی، هم در عربی و هم در \"\n   \"اوگاریتی گواه دارد، به تعریف «سامیِ مشترک» است؛ پس برچسبِ «سامی» — برخلافِ برچسبِ «عربیِ» جعبهٔ ح‌ش‌ش در بالای همین \"\n   \"صفحه — انتخابِ درستی است، و معنای «زیستن» نیز درست است. تنها حلقهٔ سست در این نمودار جعبهٔ لاتین (گرهٔ ۴) است که \"\n   \"کتاب در آن صورتِ انگلیسیِ Eve را به‌جای لاتینِ Eva چاپ کرده و حلقهٔ یونانیِ Εὕα در ترجمهٔ سبعینیه — که پلِ واقعیِ \"\n   \"میان عبری و لاتین است — از قلم افتاده است.\"),\n \"sources\": [\"https://www.etymonline.com/word/Eve\"],\n \"ref_check\": [\n   {\"ref\": \"KLN:552\", \"status\": \"supports\",\n    \"note\": \"KLN_1966.txt form-feed leaf 300, s.v. Eve: 'Eve, 1) fem. PN; 2) in the Bible, the wife of Adam. — Late L. Eva, fr. Heb. Ḥawwāh, lit. ‘a living being’, from the base of ḥāwā — ḥāyā, ‘he lived’. See Gen. 3:20. Heb. ḥāyāh … is rel. to Aram.-Syr. ḥayā … Ugar. ḥwy (ḥyy) … Arab. ḥayya … Arab. ḥayāh, ‘life’.' This single entry underwrites the root box and nodes #1, #3, #4 and #5.\"},\n   {\"ref\": \"FVA:118\", \"status\": \"not_checked\", \"note\": \"Nahvi's dictionary is not digitised (refs_online.json).\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"leaf 300, s.v. Eve\", \"stance\": \"supports\",\n    \"note\": \"The full comparative Semitic set quoted above.\"},\n   {\"src\": \"FVQ\", \"where\": \"Jeffery, index and body — no entry for ḥayāt/ḥayawān\", \"stance\": \"silent\",\n    \"note\": \"Jeffery's book lists only FOREIGN words of the Qurʾān; ḥayāh and ḥayawān are absent precisely because they are native Arabic formations of a native Semitic root, which indirectly supports the root box.\"},\n   {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt — no Semitic appendix in this printing\", \"stance\": \"silent\",\n    \"note\": \"The 1985 Watkins volume covers Indo-European roots only; the Semitic appendix Nourai's AHD:453 belongs to is in the main dictionary, not available.\"}\n ],\n \"nodes\": []\n}\n\ne2[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Arabic\", \"words\": \"h.y.y; hayât; hawwâ\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"The Arabic material is right in itself. The verb is ḥayya / ḥayiya 'he lived' (a doubly weak root, \"\n   \"hence the two shapes), imperfect yaḥyā, with the maṣdar ḥayāh حياة 'life' — Qurʾānically spelt حيوة, an archaic \"\n   \"orthography that preserves the third radical w and shows the root to be *ḥyw beside *ḥyy. From the same root come \"\n   \"ḥayy 'alive', ḥayawān 'living creature', and the form-IV ʾaḥyā 'to bring to life'. The third word, however, is \"\n   \"not an Arabic formation: Ḥawwāʾ حواء 'Eve' is not in the Qurʾān at all and reaches Arabic from Jewish and \"\n   \"Christian tradition (Hebrew Ḥawwāh via Syriac Ḥawwā), being then re-analysed by Arab lexicographers as if from \"\n   \"ḥ-y-y. Nourai therefore draws Ḥawwāʾ as an independent Arabic descendant of the Semitic root, in parallel with \"\n   \"Hebrew ḥawwāh (node #3); the historically accurate picture is Hebrew → Aramaic/Syriac → Arabic. That is why this \"\n   \"node is graded plausible rather than confirmed.\"),\n \"derivation_fa\": (\"مادهٔ عربی فی‌نفسه درست است: فعلِ حَیَّ/حَیِیَ «زیست» (ریشه‌ای مضاعف و ناقص، از این‌رو دو صورت)، \"\n   \"مضارعِ یَحیا، و مصدرِ حَیاة «زندگی» که در رسم‌الخطِ قرآنی «حیوة» نوشته می‌شود و همین املای کهن نشان می‌دهد که ریشه در \"\n   \"کنارِ *ḥyy صورتِ *ḥyw نیز داشته است. از همین ریشه‌اند حَیّ «زنده»، حَیَوان «جانور» و بابِ افعالِ أحیا «زنده کردن». \"\n   \"اما واژهٔ سوم ساختهٔ عربی نیست: «حوّاء» در قرآن اصلاً نیامده و از راهِ سنّتِ یهودی و مسیحی (عبریِ ḥawwāh به میانجیِ \"\n   \"سریانیِ ḥawwā) وارد عربی شده و سپس لغت‌نویسانِ عرب آن را به ریشهٔ ح‌ی‌ی بازبسته‌اند. نورایی «حوّاء» را فرزندِ مستقلِ \"\n   \"عربیِ ریشهٔ سامی و هم‌ردیفِ «حوّاهِ» عبری (گرهٔ ۳) کشیده است، حال آنکه تصویرِ تاریخی چنین است: عبری ← آرامی/سریانی ← \"\n   \"عربی. به همین سبب این گره «با احتیاط پذیرفتنی» ارزیابی می‌شود.\"),\n \"sources\": [\"https://www.etymonline.com/word/Eve\"],\n \"ref_check\": [\n   {\"ref\": \"KLN:552\", \"status\": \"supports\",\n    \"note\": \"Klein s.v. Eve (leaf 300): 'Arab. ḥayya, ‘he lived’ … Arab. ḥayāh, ‘life’' — both Arabic words of this box, tied to the same base as Hebrew Ḥawwāh.\"},\n   {\"ref\": \"FVA:118\", \"status\": \"not_checked\", \"note\": \"no digital copy of Nahvi (refs_online.json).\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"leaf 300, s.v. Eve\", \"stance\": \"supports\",\n    \"note\": \"'from the base of ḥāwā — ḥāyā, ‘he lived’ … Arab. ḥayya, ‘he lived’ … Arab. ḥayāh, ‘life’.'\"},\n   {\"src\": \"FVQ\", \"where\": \"Jeffery, no entry for ḥayāh / Ḥawwāʾ\", \"stance\": \"silent\",\n    \"note\": \"Jeffery has no article on either word: ḥayāh because it is native Arabic, Ḥawwāʾ because the name does not occur in the Qurʾān — the latter silence is itself the ground for calling the Arabic Ḥawwāʾ a post-Qurʾānic borrowing from Jewish/Christian usage.\"},\n   {\"src\": \"AFA\", \"where\": \"Fraenkel, Die aramäischen Fremdwörter im Arabischen — grep 'Hawwa' returns nothing\", \"stance\": \"silent\",\n    \"note\": \"Fraenkel does not treat the personal name, so his silence neither confirms nor refutes the Aramaic mediation of Ḥawwāʾ.\"}\n ]\n})\n\ne2[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Persian\", \"words\": \"hayât «حیات ( حَیّ )»; ehyâ «إحیاء»; hayavân «حَیَوان»; havvâ «حوّا»\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"All four are Arabic loans taken into New Persian in the Islamic period with their Arabic spelling \"\n   \"untouched, and they are among the commonest Arabisms in the literary language. حیات ḥayāt 'life' is the Arabic \"\n   \"maṣdar ḥayāh, which Persian pronounces with the final -t of the construct/pausal-less form, as it does with \"\n   \"زکات, صلات etc.; the parenthetical «حَیّ» in the box is the underlying Arabic adjective 'living'. احیاء ehyā is \"\n   \"the form-IV maṣdar of ʾaḥyā 'to revive', hence 'revivification, bringing back to life' — the Ḥāfeẓ line quoted \"\n   \"on the page («عیسی دمی کجاست که احیای ما کند») uses it in exactly that sense. حیوان ḥayavān is the Arabic \"\n   \"ḥayawān 'living creature', which Persian narrowed to 'animal'. حوّا Ḥavvā is the Arabic form of the biblical name, \"\n   \"so in Persian it is a loan at one further remove (Hebrew → Syriac → Arabic → Persian). One correction: the gloss \"\n   \"of ehyā as 'to bring back to life, purify' is half wrong — إحیاء never means 'purify'; that sense belongs to no \"\n   \"member of this root and looks like a stray from Nourai's notes. The page image confirms the book itself prints \"\n   \"'purify', so this is the author's slip, not the extraction's.\"),\n \"derivation_fa\": (\"هر چهار واژه وام‌واژه‌های عربی‌اند که در دورهٔ اسلامی با همان املای عربی وارد فارسی شده‌اند و از \"\n   \"پربسامدترین عربی‌های زبانِ ادبی‌اند. «حیات» همان مصدرِ عربیِ حَیاة است که فارسی آن را با تای پایانی تلفظ می‌کند \"\n   \"(مانند زکات و صلات)؛ «حَیّ» درونِ کمانک صفتِ عربیِ زیربنایی به معنای «زنده» است. «احیاء» مصدرِ بابِ افعال از أحیا \"\n   \"«زنده کردن» است، یعنی «زنده‌گردانی»؛ بیتِ حافظ که در همان صفحه نقل شده («عیسی دمی کجاست که احیای ما کند») دقیقاً \"\n   \"در همین معناست. «حیوان» از حَیَوانِ عربی «جانْ‌دار» است که در فارسی به «جانور» تخصیص یافته. «حوّا» صورتِ عربیِ نامِ \"\n   \"کتابِ مقدس است، پس در فارسی وام‌واژه‌ای است با یک واسطهٔ بیشتر (عبری ← سریانی ← عربی ← فارسی). یک تصحیح: معنایی که \"\n   \"کتاب برای «احیاء» آورده — «to bring back to life, purify» — نیمی نادرست است؛ «احیاء» هرگز «پاک کردن» معنی نمی‌دهد. \"\n   \"تصویرِ صفحه نشان می‌دهد خودِ کتاب چنین چاپ کرده، پس خطا از نویسنده است نه از استخراجِ داده.\"),\n \"sources\": [\"https://www.etymonline.com/word/Eve\"],\n \"ref_check\": [\n   {\"ref\": \"FVA:118\", \"status\": \"not_checked\",\n    \"note\": \"Nahvi's Farhang-e Vazheha-ye Arabi dar Farsi is exactly the kind of book that would list these four words, but no digital copy exists (refs_online.json, re-searched 2026-09). The claim — that these are Arabic loans in Persian — is not in doubt and is confirmed by Moʿin's [ع.] tagging and by Borhān.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"MON_part1.txt (e.g. lines 1173, 4227, 46865, 54648: آب حیات، آلات حیات، جان حیوان، آب حیوان)\", \"stance\": \"supports\",\n    \"note\": \"Moʿin's abridgement carries حیات and حیوان throughout as ordinary Persian vocabulary and in the fixed Persian compounds آب حیات / آب حیوان 'the water of life', i.e. Arabic loans fully naturalised.\"},\n   {\"src\": \"BQT\", \"where\": \"BQT_v2_pages.txt lines 710, 828, 844 (آب حیوان / آب حیات / حیوانات)\", \"stance\": \"supports\",\n    \"note\": \"«آب حیوان چون بتاریکی در است / جام جم در دست جان خواهم نهاد» and «… و آب حیات را هم می‌گویند» — Borhān-e Qāṭeʿ treats the words as current 17th-century Persian.\"},\n   {\"src\": \"HRN\", \"where\": \"grep for hayat/hayawan in HRN.txt — no hit\", \"stance\": \"silent\",\n    \"note\": \"Horn's Grundriss der neupersischen Etymologie deliberately excludes Arabic loanwords; the silence is expected.\"}\n ]\n})\n\ne2[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Hebrew\", \"words\": \"hawwâ\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"Hebrew חַוָּה Ḥawwāh is the name given to the woman in Genesis 3:20, where the text supplies its own \"\n   \"explanation: 'and the man called his wife's name Ḥawwāh, because she was the mother of all living (kol-ḥāy)'. \"\n   \"That is the derivation Klein reproduces — 'lit. ‘a living being’, from the base of ḥāwā — ḥāyā, ‘he lived’. See \"\n   \"Gen. 3:20' — and it is what Nourai draws. Modern Semitists, however, generally read Genesis 3:20 as a \"\n   \"paronomastic folk etymology rather than a real derivation: the form Ḥawwāh with -ww- does not regularly derive \"\n   \"from the root ḥ-y-y, and an old competing proposal connects it to Aramaic ḥiwyā 'serpent' (Etymonline notes the \"\n   \"name 'sounds suspiciously like the Aramaic word for ‘serpent’'). Nourai's arrow is thus the traditional, \"\n   \"text-internal etymology, well attested in the reference literature but not the last word.\"),\n \"derivation_fa\": (\"«حوّاه» (חַוָּה) نامی است که در سِفر پیدایش ۳٫۲۰ به زن داده شده و خودِ متن آن را چنین توضیح می‌دهد: \"\n   \"«و آدم زن خود را حوّا نام نهاد، زیرا او مادرِ همهٔ زندگان (کل‌حَی) بود». همین اشتقاق است که کلاین نقل می‌کند — «در \"\n   \"اصل ‘موجودِ زنده’، از ستاکِ ḥāwā/ḥāyā ‘زیست’» — و همان است که نورایی کشیده است. اما سامی‌شناسانِ امروزی این \"\n   \"بند را بیشتر «ریشه‌شناسیِ عامیانه» و بازیِ لفظیِ متنِ مقدس می‌دانند تا اشتقاقی واقعی: صورتِ Ḥawwāh با ‎-ww-‎ به \"\n   \"قاعده از ریشهٔ ح‌ی‌ی به دست نمی‌آید، و پیشنهادِ رقیبِ دیرینی آن را با آرامیِ ḥiwyā «مار» می‌سنجد. پس ادعای نورایی \"\n   \"همان اشتقاقِ سنّتی و درون‌متنی است: در منابعِ مرجع پرگواه، ولی سخنِ آخر نیست.\"),\n \"sources\": [\"https://www.etymonline.com/word/Eve\"],\n \"ref_check\": [\n   {\"ref\": \"KLN:552\", \"status\": \"supports\",\n    \"note\": \"Klein leaf 300, s.v. Eve: 'Heb. Ḥawwāh, lit. ‘a living being’, from the base of ḥāwā — ḥāyā, ‘he lived’. See Gen. 3:20.' Exactly the arrow Nourai draws, and Klein's own gloss 'a living being' is word for word Nourai's gloss for the box.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"leaf 300, s.v. Eve (and the cross-reference 'Cp. Eva. Cp. also ave.')\", \"stance\": \"supports\",\n    \"note\": \"Klein derives the name from the root and cites Gen. 3:20 as the authority.\"},\n   {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls, s.v. Eve — grep of FSD_vol2.txt for the proper-name entry returns only compounds\", \"stance\": \"silent\",\n    \"note\": \"No usable etymological entry located in the OCR of the volume.\"},\n   {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt — Indo-European roots only\", \"stance\": \"silent\",\n    \"note\": \"Nourai's AHD:453 is a main-dictionary page, not on disk; the Semitic name has no IE root entry.\"}\n ]\n})\n\ne2[\"nodes\"].append({\n \"id\": 4, \"lang\": \"Latin\", \"words\": \"Eve\",\n \"verdict\": \"transcription_suspect\",\n \"error_in\": \"book\",\n \"book_prints\": \"Eve\",\n \"correct_form\": \"Eva\",\n \"derivation\": (\"The Latin form of the name is EVA, not 'Eve': Late Latin / Vulgate Eva (Gen. 3:20 'et vocavit Adam \"\n   \"nomen uxoris suae Hava' in the Hebraica, Eva in the common tradition), and Klein — the very reference cited in \"\n   \"this box, KLN:552 — writes 'Late L. Eva'. 'Eve' is the English form, which the book then repeats in the English \"\n   \"box to its right, so the Latin box and the English box on the printed page carry the identical word. I rendered \"\n   \"pdf page 223 at 200 dpi and read it: the page really does print 'Eve' in the Latin box, so the extraction is \"\n   \"faithful and the fault is Nourai's (the page image is filed as \"\n   \"data/verification/sources/refs/ocr/BOOK/223.png). A second, smaller gap: the route from Hebrew to Latin ran \"\n   \"through Greek — the Septuagint renders Ḥawwāh as Εὕα (Gen. 3:20 Ζωή 'Life' in the etymologising rendering, Εὕα \"\n   \"at Gen. 4:1), and Latin Eva is taken from that Greek form, not directly from Hebrew.\"),\n \"derivation_fa\": (\"صورتِ لاتینِ این نام Eva است نه Eve: لاتینِ متأخر و ولگاتِ Eva، و خودِ کلاین در همان ص۵۵۲ که این \"\n   \"جعبه به آن ارجاع می‌دهد می‌نویسد «Late L. Eva». «Eve» صورتِ انگلیسی است که کتاب بلافاصله در جعبهٔ انگلیسیِ کناری \"\n   \"نیز همان را آورده، چنان‌که دو جعبهٔ لاتین و انگلیسی روی صفحهٔ چاپی یک واژه‌اند. صفحهٔ ۲۲۳ نسخهٔ پی‌دی‌اف را با \"\n   \"دقتِ ۲۰۰ نقطه بر اینچ تصویربرداری و خواندم: کتاب به‌راستی در جعبهٔ لاتین «Eve» چاپ کرده است؛ پس خطای چاپیِ کتاب \"\n   \"است نه خطای خوانشِ اسکن. نکتهٔ کوچک‌ترِ دوم: مسیرِ عبری به لاتین از یونانی می‌گذشته است — ترجمهٔ سبعینیه «حوّاه» را \"\n   \"Εὕα (و در پیدایش ۳٫۲۰ به‌صورتِ معناییِ Ζωή «زندگی») برگردانده و Eva لاتین از همان صورتِ یونانی گرفته شده، نه \"\n   \"یکسر از عبری.\"),\n \"sources\": [\"https://www.etymonline.com/word/Eve\"],\n \"ref_check\": [\n   {\"ref\": \"KLN:552\", \"status\": \"partial\",\n    \"note\": \"Klein leaf 300 supports the Hebrew → Latin step but gives the Latin form correctly: 'Eve … — Late L. Eva, fr. Heb. Ḥawwāh'. The reference therefore contradicts the FORM printed in the box while supporting the arrow.\"},\n   {\"ref\": \"AHD:453\", \"status\": \"not_checked\",\n    \"note\": \"A page of the main 1975/76 AHD New College dictionary (s.v. Eve), not openly available; the on-disk Watkins volume covers Indo-European roots only.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"leaf 300, s.v. Eve\", \"stance\": \"partial\",\n    \"note\": \"'Late L. Eva' — the correct Latin form.\"},\n   {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt, s.v. Eve\", \"stance\": \"silent\",\n    \"note\": \"The proper-name entry could not be isolated in the OCR of the volume.\"}\n ]\n})\n\ne2[\"nodes\"].append({\n \"id\": 5, \"lang\": \"English\", \"words\": \"Eve\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"English Eve comes from Latin Eva through Old English (Eue, Eua in Ælfric and the Old English \"\n   \"Genesis) and Middle English Eve; the final -e is the ordinary English reflex of the Latin -a in an unstressed \"\n   \"syllable, as in Anna/Anne, Maria/Mary. The name is entirely a learned, ecclesiastical borrowing carried by the \"\n   \"Bible, not by ordinary contact. Klein and Etymonline both give the same one-step chain 'Late Latin Eva, from \"\n   \"Hebrew Ḥawwāh'. (English Eve 'evening, the day before' is a wholly different word, from Old English æfen, and is \"\n   \"not involved here.)\"),\n \"derivation_fa\": (\"Eve انگلیسی از Eva لاتین آمده است، از راهِ انگلیسیِ باستان (Eue/Eua در آثارِ الفریک و «پیدایشِ» \"\n   \"انگلیسیِ باستان) و انگلیسیِ میانهٔ Eve؛ ‎-e‎ پایانی بازتابِ معمولِ ‎-a‎ لاتین در هجای بی‌تکیه است، مانندِ \"\n   \"Anna/Anne و Maria/Mary. این نام یکسره وام‌واژه‌ای کلیسایی و کتابی است که از راهِ ترجمه‌های کتاب مقدس رسیده، نه از \"\n   \"تماسِ روزمرهٔ زبان‌ها. کلاین و اتیمآنلاین هر دو همین زنجیرهٔ یک‌مرحله‌ای را می‌دهند: «لاتینِ متأخر Eva از عبریِ \"\n   \"ḥawwāh». (واژهٔ همنامِ eve به معنای «شامگاه، شبِ پیش از» واژه‌ای یکسره دیگر و از æfen انگلیسیِ باستان است و به این \"\n   \"بحث ربطی ندارد.) ادعای نورایی درست است.\"),\n \"sources\": [\"https://www.etymonline.com/word/Eve\"],\n \"ref_check\": [\n   {\"ref\": \"AHD:453\", \"status\": \"not_checked\",\n    \"note\": \"Main-dictionary page of the 1975/76 AHD New College edition, not openly available; the chain is covered by Klein (leaf 300) and Etymonline instead.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"leaf 300, s.v. Eve\", \"stance\": \"supports\",\n    \"note\": \"'Eve, 1) fem. PN; 2) in the Bible, the wife of Adam. — Late L. Eva, fr. Heb. Ḥawwāh, lit. ‘a living being’.'\"},\n   {\"src\": \"SKT\", \"where\": \"grep 'Eve' in SKT.txt — only the common noun eve 'evening' (< OE æfen)\", \"stance\": \"silent\",\n    \"note\": \"Skeat's concise dictionary omits proper names, so it has nothing on the biblical Eve; recorded to show the search was made.\"}\n ]\n})\ndoc[\"entries\"].append(e2)\n\nwith open(\"/home/sfmqrb/git/rishe/data/verification/page-223.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(doc, f, ensure_ascii=False, indent=1)\n    f.write(\"\\n\")\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk223.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-223.json > /dev/null && echo \"JSON OK\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 223"
}
```


### [2026-09-06T15:32:32.066Z] TOOL RESULT

```
ok
JSON OK
nodes verified: 17/17
node verdicts: {'plausible': 4, 'confirmed': 11, 'disputed': 1, 'transcription_suspect': 1}
root verdicts: {'confirmed': 3}
ref checks: {'supports': 9, 'not_checked': 13, 'partial': 2}
books consulted: {'partial': 4, 'supports': 32, 'silent': 10, 'contradicts': 4} | by book: {'KLN': 7, 'WEB': 5, 'SKT': 5, 'BQT': 4, 'HUB': 4, 'LKT': 3, 'MON': 3, 'FSD': 3, 'FVQ': 3, 'DEV': 2, 'HRN': 2, 'HJB': 1, 'LAM': 1, 'PHD': 1, 'NYB': 1, 'FRS': 1, 'TAD': 1, 'SOD': 1, 'AFA': 1, 'AHD': 1}
```


## [2026-09-06T15:32:40.232Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"POK:\"; grep -c -i 'hyakinth\\|ὑάκινθ\\|hyacinth' POK_full.txt; echo \"AHD:\"; grep -c -i 'hyacinth' AHD_watkins1985.txt; echo \"HRN hayat:\"; grep -c -i 'hajat\\|hayat\\|hayawan' HRN.txt; echo \"AFA Hawwa:\"; grep -c -i 'hawwa' AFA.txt; echo \"SKT Eve:\"; grep -n -i '^Eve,' SKT.txt | head -3; echo \"FVQ hayat:\"; grep -c -i \"^hayat\\|Ḥayāt\" FVQ_pages.txt"
}
```


### [2026-09-06T15:32:40.331Z] TOOL RESULT

```
POK:
0
AHD:
0
HRN hayat:
0
AFA Hawwa:
0
SKT Eve:
6039:Eve,  Even,  the  latter  part  of  the (K)  £ve  ii  short  for /v^« ;  (for see  below).  M.  E.  w/,  eum,  A //m.  ^  O.  Sax.  (ffdW,  IccI  ofian^ afton^  Dan.  aflen,  G.  abend.  Soppotdl mean  the  '  after '  part  of  the  <Uy ;  aUiid Aft.  Cf. Skt.  d^ra. posterior;  ^a4B dhyd,  evening  twilight  Dttr.  tvtm- ifeniid. evening,  even.    (£.)     M.  E
FVQ hayat:
0
```


## [2026-09-06T15:33:04.760Z] AGENT

Page 223 (book p. 193) verified; `verify_check.py 223` → 17/17 nodes, 0 PROBLEM lines.

**Counts** — roots: 3 confirmed. Nodes: 11 confirmed, 4 plausible, 1 disputed, 1 transcription_suspect. Ref checks: 9 supports, 2 partial, 13 not_checked (FVA, MZF, FAF, and Nourai's AHD main-dictionary pages are all undigitised). 20 different books consulted.

**Flagged items**
- `disputed` — *Hyakinthos* #3, Arabic **yâqŭt** ← Persian yâkand. Nourai's own sources do say this (BQT 2420 fn. 2 quotes Ḥamza al-Iṣfahānī via Bīrūnī; SNS 299 «یاقوت معرّب یاکند فارسی است»), but Jeffery FVQ 289–290, Hübschmann *Pers. Stud.* 151 (after Nöldeke) and Tobia al-Unaysi all derive Arabic yāqūt from Syriac yāqūndtā < Gk. ὑάκινθος, with NP yāqūt from Arabic and NP/MP yākand separately from Aramaic. yākand cannot phonetically give yāqūt.
- `transcription_suspect` — *H.y.y* #4, Latin box printed as **"Eve"**; correct Latin is **Eva** (Klein, the box's own reference, writes "Late L. Eva"). `error_in: book` — pdf p. 223 rendered at 200 dpi confirms the book prints "Eve"; the Greek Εὕα stage is also missing.
- `plausible` ×4: *H.š.š* #1 (word fine, but the "hashish before killing" story is the Crusader legend — Hodgson/Daftary/Etymonline); *Hyakinthos* #1 (Gk → Pahlavi yakand is right in ultimate source but skips the Aramaic/Syriac mediation Hübschmann insists on); *H.y.y* #1 (Arabic Ḥawwāʾ is not a native Arabic formation — not in the Qurʾān, it comes from Hebrew via Syriac) and #3 (Gen 3:20 ḥawwāh ← ḥāyā is read today as folk etymology).

**Notable find on the root note of entry 1**: Nourai says "BQT:2420 and SNS:299 interpret the Greek word as 'a kind of poison'". SNS 299 does say that (read from the page image). BQT 2420 does **not** — Moʿin writes «بمعنی نوعی از زهر» where زهر is Arabic *zahr* "blossom", proved by his next clause identifying the plant as *Iris germanica* / *gladiolus communis*. So the "poison" reading is a misread of «زهر»; ὑάκινθος never meant a poison.

**No extraction errors** — every oddity checked against the printed page is the book's own: Italian *assassino* glossed "murder" (it is the agent noun; "murder" = *assassinio*), Latin "Eve", إحیاء glossed "purify", and the "poison" note.

**New artifacts saved**: `data/verification/sources/refs/ocr/BQT/2420.png` + `2420.vision.txt`, `.../ocr/SNS/299.png` + `299.vision.txt` (archive.org VajnameShayest leaf n167 = printed p. 299 — SNS's page offset is now pinned), `.../ocr/BOOK/223.png`, and 5 archived web sources. The verification file is written but **not committed**.
