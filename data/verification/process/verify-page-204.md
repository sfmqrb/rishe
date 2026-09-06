# Verification process log — verify-page-204


## [2026-09-06T14:51:39.348Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 204 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-204.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-204.json. Write /home/sfmqrb/git/rishe/data/verification/page-204.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 204` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T14:51:40.939Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T14:51:41.689Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T14:51:41.703Z] TOOL RESULT

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


## [2026-09-06T14:51:41.867Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-204.txt"
}
```


### [2026-09-06T14:51:41.879Z] TOOL RESULT

```
1	=== PDF page 204 (book page 174) ===
2	--- entry 0 ---
3	ROOT Gwag -> redirect to Wag 2
4	--- entry 1 ---
5	ROOT Gwâk -> redirect to Wag 2
6	--- entry 2 ---
7	ROOT [Indo-European] Gwebh 1 : to dip, sink  (refs POK:465)
8	#1 (parent #0) [Avestan] refs=POK:466 | jafra : deep
9	  #2 (parent #1) [Pahlavi] refs=FVA:293 | žafr
10	    #3 (parent #2) [Persian] refs=BQT:1059; HRN:152 | žarf «ژرف ( ژرفا )» : deep
11	#4 (parent #0) [Greek] refs=POK:466; AHD | baptein : to dip
12	  #5 (parent #4) [English] refs=None | Baptist
13	--- entry 3 ---
14	ROOT [Indo-European] Gwebh 2 : slime, sliminess, toad  (refs POK:466)
15	#1 (parent #0) [Old Persian] refs=POK:466 | gabawo : toad
16	  #2 (parent #1) [None] refs=None | 
17	#3 (parent #0) [Germanic] refs=AHD:1519 | quabbeln : to shake like jelly, tremble
18	  #4 (parent #3) [English] refs=None | quaver, quiver
19	--- entry 4 ---
20	ROOT [Indo-European] Gwedh : to injure, destroy  (refs POK:466)
21	#1 (parent #0) [Avestan] refs=POK:466; SYN:1024 | gantay, ganti, gainti : bad smell
22	  #2 (parent #1) [Persian] refs=BQT:1841; HRN:208; SYN:1179 | gand «گند» : stink ; gandîdan «گندیدن» : to rot
23	  #3 (parent #1) [Sogdian] refs=SOD:164 | gnc : bad smelling
24	#4 (parent #0) [Old Persian] refs=SYN:1024; KNT:183 | gasta : offensive, evil
25	  #5 (parent #4) [Pahlavi] refs=MON:3314 | gasta : ugly
26	    #6 (parent #5) [Persian] refs=MON:3314; SYN:1024 | gast «گست» : bad, ugly
27	--- entry 5 ---
28	ROOT Gwěguos -> redirect to Wag 2
29	
```


## [2026-09-06T14:51:45.880Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-204.json",
 "description": "Read source JSON for page 204"
}
```


### [2026-09-06T14:51:45.921Z] TOOL RESULT

```
{
  "pdf_page": 204,
  "book_page": 174,
  "entries": [
    {
      "root": {
        "name": "Gwag",
        "redirect": "Wag 2"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Gwâk",
        "redirect": "Wag 2"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Gwebh 1",
        "lang": "Indo-European",
        "refs": "POK:465",
        "gloss": "to dip, sink"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:466",
          "words": [
            {"translit": "jafra", "gloss": "deep", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "FVA:293",
          "words": [
            {"translit": "žafr", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:1059; HRN:152",
          "words": [
            {"translit": "žarf", "gloss": "deep", "script": "ژرف ( ژرفا )"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "یکی ژرف دریاست بن ناپدید - در گنج رازش ندارد کلید",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Greek",
          "refs": "POK:466; AHD",
          "words": [
            {"translit": "baptein", "gloss": "to dip", "script": null}
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
            {"translit": "Baptist", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Gwebh 2",
        "lang": "Indo-European",
        "refs": "POK:466",
        "gloss": "slime, sliminess, toad"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "POK:466",
          "words": [
            {"translit": "gabawo", "gloss": "toad", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": null,
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD:1519",
          "words": [
            {"translit": "quabbeln", "gloss": "to shake like jelly, tremble", "script": null}
          ],
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
            {"translit": "quaver, quiver", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Gwedh",
        "lang": "Indo-European",
        "refs": "POK:466",
        "gloss": "to injure, destroy"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:466; SYN:1024",
          "words": [
            {"translit": "gantay, ganti, gainti", "gloss": "bad smell", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:1841; HRN:208; SYN:1179",
          "words": [
            {"translit": "gand", "gloss": "stink", "script": "گند"},
            {"translit": "gandîdan", "gloss": "to rot", "script": "گندیدن"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Sogdian",
          "refs": "SOD:164",
          "words": [
            {"translit": "gnc", "gloss": "bad smelling", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "SYN:1024; KNT:183",
          "words": [
            {"translit": "gasta", "gloss": "offensive, evil", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Pahlavi",
          "refs": "MON:3314",
          "words": [
            {"translit": "gasta", "gloss": "ugly", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Persian",
          "refs": "MON:3314; SYN:1024",
          "words": [
            {"translit": "gast", "gloss": "bad, ugly", "script": "گست"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "چه عاشق باشد اندر عشق ، چه مست - کجا بر چشم او نیکی بود گست",
            "poet": "Vîs-o-Râmîn"
          }
        }
      ]
    },
    {
      "root": {
        "name": "Gwěguos",
        "redirect": "Wag 2"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-06T14:51:46.452Z] TOOL CALL #4: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo \"---MATRIX---\" && cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "List verification dir and read source matrix"
}
```


### [2026-09-06T14:51:46.507Z] TOOL RESULT

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
---MATRIX---
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


## [2026-09-06T14:51:58.081Z] TOOL CALL #5: Bash

```json
{
 "command": "ls data/verification/page-20*.json && python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','FVA','BQT','HRN','AHD','SYN','KNT','MON','SOD','BRT','PHD','NYB','CHEUNG','WLD','IEC','KLN','SKT','ARY','HUB','FSF','FRS','IRN','FFD']:\n    v=d.get(k)\n    print(k, json.dumps(v, ensure_ascii=False)[:600] if v else 'MISSING')\n\""
}
```


### [2026-09-06T14:52:01.017Z] TOOL RESULT

```
data/verification/page-200.json
data/verification/page-202.json
data/verification/page-203.json
data/verification/page-205.json
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_
FVA {"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: still no digital copy on any permitted platform. Library catalogues list the 1368 book under the variant title «فرهنگ ریشهٔ وام‌واژه‌های عربی (لغات عربی مستعمل در فارسی دخیل)» — reconcile with N
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf
CHEUNG MISSING
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol
FSF {"title": "Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/1984", "kind": "archive_djvu", "url": "https://archive.org/details/20220809_20220809_1444", "lookup_hint": "grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushin book (گزارشی چند درباره شاهنامه).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF.txt"], "page_offs
FRS {"title": "Asadi Tusi, Loghat-e Fors, ed. Mojtaba'i & Sadeqi, Kharazmi 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/LughatEFurs-AbuMansurAliBinAhmadAsadiTusiFarsi (Abbas Eqbal's 1319/1940 Tehran edition); also dli.ernet.439493 / dli.ernet.437743 (Horn's 1897 Göttingen edition, 'Lughat Faras')", "lookup_hint": "Look up the headword (entries grouped by final letter); FRS_pages.txt has \\f page breaks (567 leaves). Pagination differs from the 1365 Kharazmi edition Nourai cites — verify the entry, not the page.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/s
IRN {"title": "Bahram Farahvashi, Iranvij, Tehran University Press 1368/1989", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ایرانویج-بهرام-فره-وشی/ -> https://dl.eliteraturebook.com/storage/img/ایرانویج.pdf (free PDF site; grey) ; Google Books kP8bAAAAIAAJ (1368 ed., no view)", "lookup_hint": "archive.org 'Iranvej' item is a radio programme, not the book; nothing on ketabnak/noorlib. | For pages in a scanned volume use: python3 tools/ref_page.py IRN:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)", "local_file": ["/home/sfmqrb/git/rishe/data/v
FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/s
```


## [2026-09-06T14:52:07.706Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport json\nd=json.load(open('../refs_online.json'))\nprint(d['POK']['page_offset'])\nprint(d['POK'].get('lookup_hint'))\n\""
}
```


## [2026-09-06T14:52:08.830Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"g^u̯ebh\\|gu̯ebh\\|guebh\" POK_full.txt | head -30; echo \"=== search jafra ===\"; grep -n \"jafra\" POK_full.txt POK_01.txt POK_02.txt | head -20"
}
```


### [2026-09-06T14:52:09.665Z] TOOL RESULT

```
POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\data\ie\pokorny&root=config
```


### [2026-09-06T14:52:09.730Z] TOOL RESULT

```
=== search jafra ===
POK_02.txt:1840:Eine  vielleicht  verwandte,  aber  nur  die  Bed.  .tief  aufweisende  Wurzel *g(U')embh-,  *g(}f)7nhh-  zeigt  das  Arische  (wobei  im  Ai.  das  g  der  Tiefstufe oder  o-Stufe  durchgeführt  ist.  gegenüber  av.  j  der  e-Stufe)  :  ai.  gabhlrd- gambhlrd-  .tief',  gambha-,  gdmbhan-,  gambhdra-  n.  .Tiefe.  Abgrund',  gahha- m.  .Vulva',  gabhi-sdk  AV.  Adv.  vielleicht  .tief  unten  oder  innen',  av. jaiwi-vafra-\  Adj.  .mit  tiefem  Schnee',  jafra-  .tief,  jqfnu-s  .Vertiefung-, Einsenkung';  vgl.  Frisk  Nominalbildung  30.
```


## [2026-09-06T14:52:14.378Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('POK_02.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\n# find line index\nfor i,l in enumerate(lines):\n    if 'jafra-' in l:\n        print('line',i+1)\n        idx=sum(len(x)+1 for x in lines[:i])\n        leaf=t[:idx].count('\\f')\n        print('leaf',leaf,'printed page approx',leaf+344)\n\"\n"
}
```


## [2026-09-06T14:52:14.490Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1800,1900p' POK_02.txt"
}
```


### [2026-09-06T14:52:16.881Z] TOOL RESULT

```
line 1840
leaf 123 printed page approx 467
```


### [2026-09-06T14:52:16.921Z] TOOL RESULT

```
464
Trotz  Thurneysen  Gr.  §§  547,  728  ist  ein  Stamm  hus-  nicht  nachzuweisenj  |^ s.  richtiger  Pedersen  Litteris  2,  89  f.  -^^'
2.  g'iem-'.  ^:},'
Unthematisch  *{e)-gi}em-t  (>  *e-guen-t),  -gMm-te,  -gnm-ent  im  ai.  Aor.  dgan,  '-  ■ gan  (g  für  j  nach  Formen  mit  ursprünglichem  *g^7ri-,  *gum-'^  1.  Sg.  dgamam\ dgata   {*g'^m-),  dgman,   dgmata]    gthav.    3.  Sg.   Inj.   uz-J9n,   3.  PI.   ^»T/ian;
arm.  3.  Sg.  ekn  ,er  kam'  (=  ai.  dgan)-,  über  die  noch  unklare  1.  Sg.  eki, 3.  PI.  ekin  siehe  Meillet  Esquisse  134  f.;
gr.  ßdTTjv  3.  Du.,  vnsQßäaav  3.  PL  wohl  zur  Wurzelf.  *^?^ä-;
Konj.  *gi^emeti  in  ai.  gdm-at,  -anti,  gthav.  jamaHi,  jimaHi]  Opt.  gurji. jet  in  ai.  gamyät,  av.  jamyät,  ap.  jawjä''  {J  für  g  aus  Formen  mit  hoch- stufigem idg.  *guem-) ;  ags.  cyme  s.  unten ;
thematisch:  hochstufig  ai.  gdmati,  av.  jamaiti  ,geht'  (ai.  gamdyati ,läßt  kommen,  führt  herbei^  av.  jämayeiti  ^briogt  zum  Weichen'),  tiefstufig; ai.  (Opt.  Aor.)  gamit,  gamimay  gamemahi,  wohl  auch  Aor.  dgamat]  PerL^ ja-gdma  ,ich  ging'  (vgl.  got.  1.  PL  qemum);  av.  frä-ymat  (gthav.  -g'maQ] ,er  kam  hinzu',  apers.  a-gmatä-,
osk.  kümhened  ,convenit',  cebnust  (aus  *ce-henust)  ,(huc)  venerit',  umbrj &ewws<,  benurent  ,venerit,  -int';  lat.  Konj.  advenam  (über  n  für  w  s.  unten;* vielleicht  mit  analogischem  -en-  nach  den  Formen  wie  lat.  veniöj  ventumy venl) ;
got.  qiman  (Prät.  qam,  1.  PL  qemum:  ai.  1.  Sg.  Perf.  ja-gäma),  ahdj queman  und  (tiefstufig?)  coman  =  ags.  cuman,  anord.  Äöma  ,kommen^\ ags.  Konj.  Präter.  (alter  Optat.)  c2/we  {^gu^m-l-t)]
toch.  A  kam-,  kum-,  B  kam-,  kam-,  sem  ,kommen'.
io-Präsens  *gum-{ö  in  gr.  ßaivo)  .gehe'  (Fut.  ßrjooixai  usw.),  lat.  veni^ ,komme'  mit  sehr  altem  Wandel  von  -mi-  zu  -ni- ;  nach  Schwyzer  Gr.  Gr.  I, 309  könnte  das  n  auch  von  Formen  wie  av.  jantu  (*g^em-tu-),  arm.  ekn (*e-guem-t)  bezogen  sein;  zu  venimus  stimmt  got.  qemum-,
sAro-Präsens  * gurri-skö  :  2Ä.  gdcchati,  SLV.jasaiti  ,er  geht',  gr.  ßäoTis  ^ehl komm!'  toch.  A  kumnäs  ,er  kommt',  Med.  kumnästär,  B  känmasträ.
Verbaladjektiv:  ai.  gatd-h  ,gegangen',  av.  gata-  ds.,  gr.  ßazög  ,gangbar' {*gum-to-s),  lat.  in-ventus.
Andere  Nominalbildungen:
ai.  gdti-}^  f.  ,GaDg',  av.  aiwi-gati-  ,das  Herbeikommen  =  Eintreten, Beginnen',  gr.  ßäoig  f.  ,Schritt;  Grundlage'  (*gum-ti-s),  lat.  con-venti-ö ,Zusammenkunft',  got.  gaqum^s  ,Zusammenkunft'  {*-gifm-tis),  anord.  saTH- kund  f.  ds.,  ahd.  cumft,  nhd.  Ankunft ;  ai.  gdntu-h  m.  ,Gang,  Weg',  lat.  i adventus,  -üs  ,Ankunft';  got.  qums  ,Ankunft'  (*gi^e'^-is),  ags.  cyme^  ahd. cumi'j   •&[.  gamya-  ,wohin  man  gehen   kann  oder  soll',  osk.  kümbennieis
465
Ten.   conventüs^ ;  ahd.  biquämi  ^bequem^  (vgl.  ^bekömmlich^)^  ags.  gecweme
no-enehni;  passend^^  anord.  hvcemr  ^zum  Kommen  berechtigt  oder  im- tinde^;  kväma  f.  ,Kommen^  Besuch^^  köma  ds. ;
toch.  A  kzim-j  AB  kam-j  A  kam-,  B  sem-  ^kommen^;,  A  kumnds,  Med. htiinndstdr  ^kommt^,  A  kakmu,  B  kekamu  ,gekommen^
^lit  einer  Bed. -Entwicklung  ,{2,mv  Welt)  kommen^  =  _,geboren  werden^:
av.  ni-jämayeinti  _,sie  bringen  zum  Gebären^  (*ni-jäma-  ^GeburtQ;
crr.  i'ßäS-r]'  iysvvsd-r]  Hes. ;
alban.  pre-gjim  ^Gastmahl  bei  der  Erstgeburt^;
lit.  gemü,  gimti  ^geboren  werden^  =  lett.  dzemu,  dzimt  ds.,  lit.  glmstu (zum  Akzent  siehe  Schulze  KZ.  45,  230)  =  lett.  dzwistu  ds.,  lit.  gimine Familiö^  gymis  ^Geburt^,  gämas  ^Angeborenes^,  Kausat.  gammti  ^Kinder erzeugen,  Vieh  züchten^,  lett.  dzimts  ^angeboren,  erbgehörig,  leibeigen^, Jzlmsa  ,Geburt'  =  apr.  gimsenin  Akk.  Sg.  ,Geburt^,  apr.  gemton  ,gebären^, qemmons  Partiz.  Perf.  ,geboren^
WP.  I  675ff.,  MeiUet  Esquisse^  134f.,  Schwyzer  Gr.  Gr.  I  309,  689, 742»,  7072,  Trautmann  76,   Pedersen  Toch.  170  ff.,  221,  234.
&^Udh-  ,eintauchen,  untersinkend
Ai.  gdhate  ,taucht,  dringt  ein^,  Partiz.  gädka-h  ,tief,  stark,  fest^,  gähd-h ,Tiefe,  das  Innere^;  mit  a:  gähana-,  gdhvara-  ,tief,  dicht^,  n.  ,Tiefe,  Ab- o-rund, Dickicht^,  dur-gdha-m  ,böser  Ort  oder  Weg^ ;
das  Partiz.  gädhd-  ist  wohl  Analogiebildung  nach  Wurzeln  mit  ai.  k  = idg.  gh]  gädhd-  ,seicht^,  m.  n.  ,Un tiefe,  Furt^  ist  vielleicht  aus  einem  ai. Wurzelnomen  gä  (zu  idg.  g^ä-  ,Gang^)  +  ^^^  ^Is  ,(Über)gang  gewährend^ zu  erklären;
av.  Akk.  PI.  vi-gä&ö  ,Schluchten^  (:  ai.  vi-gähd-)  ,sich  eintauchend^, schwundstufig  guda-  ,Tiefe^;
gr.  ßfjoaa,  dor.  ßäoaa  {*ßad-ia)  f.  ,Talgrund,  Schlucht^;  ßaooog  n.  ds. {*ßad-oog),  schwundstufig  ßvd-ög,  ßvoaög  , Tiefe,  Meeresgrund^  mit  ß  statt  y nach  ßfjaaa;  Ußvoaog  ,wo  sich  nicht  tauchen  läßt,  grundlos,  Tiefe^,  ßdd-og n."  ,Tiefe^;  ßev&og  ,Tiefe^  sekundär  nach  Ttevd-og  :  TiaS^og]
air.  hä{i)dim  , tauche  unter,  ertränke^,  cymr.  hoddi  ,ertränken,  ertrinken, überfluten^,  corn.  bedhy,  mbret.  beuziff  ,ertränken^;  cymr.  diffoddi  ,aus- löschen^  aus  *di-spad-  (^dl-eks-bad-),
WP.  I  665,  Schwyzer  Rhein.  Mus.  81,  193  ff.
''  g"ebh-  (oder  g}iäbh-?),  g^gbb-  ,eintauchen,  versenken,  versinkend
Gr.  ßccTTTw  ,tauche  ein^,  ßacpijvaL,  ßacprj  ,das  Eintauchen,  Färben'  (äol. ßvTCTSLv'  ßaTtTi^eiv  Hes.  nach  övnzcoj  das  selber  Kreuzung  von  ßänto)  mit oyw;  ßiTtzccl^o)  umgestellt  aus  ßanTi^aj)]
30
466
f
makcd.  ßaßor^v  .Bodensatz  des  Öls'  Hes.;  ob   auch  yvßa  .taucht'  Hes.?
anord.  kafa  .tauchen',  kmfja  (und  kefja  nach  dem  Prät.  köf  aus  ""kvoj) trans.  .untertauchen,  ersticken',  kvafna  intrans.  .ersticken',  kaf  n.  .Meeres^ tiefe',  dann  .Untertauchen.  Schwimmen  unter  Wasser';  aschwed.  kvaf .Tiefe',  anord.  kvcefa  (idg.  e!).  kefa  trans.  .ersticken',  mhd.  erqueben  ^er- sticken' (=  anord.  kvefja).
Eine  vielleicht  verwandte,  aber  nur  die  Bed.  .tief  aufweisende  Wurzel *g(U')embh-,  *g(}f)7nhh-  zeigt  das  Arische  (wobei  im  Ai.  das  g  der  Tiefstufe oder  o-Stufe  durchgeführt  ist.  gegenüber  av.  j  der  e-Stufe)  :  ai.  gabhlrd- gambhlrd-  .tief',  gambha-,  gdmbhan-,  gambhdra-  n.  .Tiefe.  Abgrund',  gahha- m.  .Vulva',  gabhi-sdk  AV.  Adv.  vielleicht  .tief  unten  oder  innen',  av. jaiwi-vafra-\  Adj.  .mit  tiefem  Schnee',  jafra-  .tief,  jqfnu-s  .Vertiefung-, Einsenkung';  vgl.  Frisk  Nominalbildung  30.
Fick  setzt  die  Wurzel  *gmbh-  an.  was  zur  Annahme  zwänge,  daß anord.  kvcefa  Ablautsneubildung  sei.
WF.  I  674.  Wissmann  Nom.  postverb.  75.
2.  g^eb{h)-  .schleimig,  schwabbelig.  Quappe.  Kröte'.
Vermutlich  onomatopoetisch;  doch  ist  mit  der  Möglichkeit  zu  rechnen, daß  ein  altes  Wort  für  Frosch  erst  im  Germ,  in  die  lautmalende  Sippe hineingezogen  wurde.  *.v
Asächs.  quappa,  quappia,  quappo  .Aalquappe'  (mit  bei  lautmalenden  Worten häufiger  Konsonantengemination),  daraus  mhd.  quappe^  quape,  kobe,  nhd. Quappe,  hoU.  kivab(be)  .Quappe.  Kropf.  Wamme',  isl.  kvap,  kvapi  .Gallert oder  gallertartige  Dinge',  schwed.  dial.  (s)kvabb  .etwas  Dickes.  Fettes', {s)kvebba  .feiste  Frau',  engl,  quab  .Morast',  quaver  .zittern,  vibrieren'. Dazu  das  Verb  norw.  dial.  kvapa  .eine  Flüssigkeit  aussenden',  schwed. dial.  kvabba,  ndd.  quabbeln  .vor  Fettigkeit  zittern';
apr.  gabawo  .Kröte'  {* g>^b  {h)-) -^  u
slav.  ^gebä  .Kröte' :  in  aksl.  zaba,  russ.  zdba,  skr.  zäba,  usw.
WP.  I  674.  WH.  I  121.  Trautmann  8.
gy.edh-  .stoßen^  verletzen,  zerstören'.
ili.  gandh-  .stoßen,  stechen,  verletzen,  zerstören'  (bei  Grammatikern), gandhd-h  m.  .Geruch.  Duft',  av.  gantay-  .Gestank',  mpers.  gand  .Gestank', apers.  gasta-  .eklig,  widerwärtig',  afgh.  yandal  ,Ekel  empfinden',  bal. gandag  .schlecht'.  (Zur  Bedeutungsentwicklung  .stoßen,  stechen'  >  .Geruch' vgl.  z.  B.  ahd.  stinkan  .riechen,  stinken'  gegen  got.  stigqan  .zusammen- stoßen' und  gr.  y.vLar]  .Fettdampf  gegenüber  aisl.  hnlta  .stoßen,  stechen'.)
Gr.  ösvvog  .Beschimpfung.  Schande'  {""guendJino-) ;  nach  Kuiper  Nasalpräs. 65  hierher  cpHvog  m.  .Neid'  (Präs.  ^cpd^ivü)  aus  *gudk-en-)',
467
über  mhd.  quetsen,  quetschen  ^schlag-en^,  stoßen^,  quetschen'  s.  Kluge g  V.  quetschen  j
lit.  gendü,  gesti  ^Schaden  nehmen,  verderben^  zugrunde  gehen'^  gadinil, (jadinti  ^verderben^  beschädigen^  stören'^  pagadas  ;,Verderben',  lett.  ginstu, jijit  ^zugrunde  gehen'.
WP.  I  672  f.,   Benveniste  BSL.  38,  143.
-  gHei-  ^klagen,  jammern'?  Außerhalb  des  Germanischen  nur  unsichere Vergleiche;  wohl  onomatopoetisch.
Got.  qainön  ,weinen,  trauern'^,  anord.  kveina  jammern',  ags.  cioänian klagen,  traurig  sein',  anord.  kveinka  ,klagen,  wehklagen'  und  mit  anderer Ableitung  aisl.  st.  Verb,  kvida  ,sich  ängstigen',  kvida  f. , Angst',  kvldi  m.  ds. ; ags.    cwldany    schw.   Verb.   ,klagen,    beklagen',    as.    quldian   ,wehklagen' ;
hieran  erinnern  formell  lit.  giedu  und  giestu,  giedöti  ,singen,  krähen', usw.,  die  zu  der  nur  in  den  Satem-Sprachen  belegten  Wurzel  *^ei-  ,singen' o-ehören  (s.  dort);  ist  der  nicht  zusammenstimmenden  Bedeutung  wegen zweifelhaft.
WP.  I  665  f.
2,  g"ei-   ,zusammendrängen,    einschließen,    einpferchen'?    *gl^iiä    ,Pferch'? Umbr.  bio,  pälign.  Akk.  biam  ,eingefriedeter  Bezirk' ; anord.  kve  f.  ,Pferch,  enge  eingefriedete  Passage',  kvla  ,einpferchen'. WP.  I  666.
^,  g^ei-  und   g'Aew-  \  g^{i)ie- i  g^(i)iö- i  g^i-,    häufig    mit    -iz-    erweitert: ,lebeu'.    Nominal:  g)ioio-s    m.,  g'^iti-s    f.   ,Leben',    g^):uo-s,    g"igo-s , lebendig',  g}i.iuo-to-s,  -tä  ,Leben'. A.  von  *g'^eiö:
A\.  ßvätu-h  , Leben'  (s.  unten),  gdya-h  ,Haus,  Hof,  Hauswesen'  (s.  unten); av.  jlyaesa  ,du  sollst  leben'  (2.  Sg.  Präs.  Med.,  oder  theraat.  2.  Sg.  Opt. für  *jigäyae§a)'^  jljisdnti  (ursprüngl.   Desiderativ)   ,sie  erquicken,  nähren', jdya-  m.  , Anregung';  gayö  ra.  ,Leben,  Lebenszeit,  Lebensführung'  (=  ai. gdya-h   ,Haus    und    Hof,   Hauswesen'    =    russ.    goj  , Friede;    Heil!');    av. gaed-ä,  apers.  gaid-ä  ,Wesen,  Haus  und  Hof; arm.  keam  ,lebe'  {^ginyä-ye-mi)]  Meillet  Esquisse  110,  176. gr.  hom.  ßso^ai  ,ich  werde  leben'  (*ßsieoo{xaL]  Schwyzer  Gr.  Gr.  I  780, 7881);
lit.  gajüs  ,leicht  heilend';  lit.  gyjü,  gyti  (*gUi-)  ,aufleben,  sich  erholen, heil  werden'  (dazu  i-gyti-  ,erlangen',  eigentlich  ,sich  hineinleben'),  lett.  dzit ,heilen;  heil  werden'^  gydau  ,heile',  lett.  dziedet  ,heilen'  (Mühlenbach- Endzelin  I  559),  aksl.  ziti  ,leben'  (Präs.  zivo  s.  unten);  dazu  aksl.  zith ^eben'  (^gntis),  pa-zith  jvoixrj,  xöqtog^  XeL(X(bv^ ',
30*
468
slav.  *goj'b  ;das  Leben'  {*guoio-s)  in  aruss.  goj  .Friede',  alt  skr.  gßj  ^^C.\ acech.  hoj  .Fülle'  (:  ai.  gdya-h),  Kausativ  slav.  *gojiti  .leben  machen',  skr^^^  ' gbjiti  .pflegen,  mästen',  usw.;  '    '
toch.  B  sai-  .leben'.  Van  Windekens  Lexique  127.
*g"Jo-  in:
av.  -jyäiti-  f.  (in  Kompositis)  .Leben',  jyätus  Gen..  jyätum  Akk.  .Leben' (im  Ai.  wurde  dies  *jyä-tu-h  nRch  jlvati  zu  fwätu-h);  ..
ep.   ion.  ld)(x),    gort,  dwo)   .lebe'   (aus  *^w-tw.   idg.   *gu{ö-io),   Aor.  iß[f^ {*guiiö-m  mit  vokal,  i,    das   vermutlich    durch   ßioo)   gestützt  wurde), ?w.  ifig,  tfi  {*t,'riisi,  idg.  *gv^ie-),  tfnog  .lebendig'.  ?w?y  .Leben',  tt^ov  .Tier^i gr.  vyLrjg  .gesund'  {*su-guiies  .wohllebend');
*g^i-   (außer   in    baltosl.  *giti-j   s.  oben)   in   av.   yavae-jl-   .fortwährenl lebend',  av.  jlti-  f.  .Leben',  ai.  jlrd-  .lebhaft,  rasch',  av.  jlra-  .lebhaft  v< Verstand,  schlau';    apr.  geits  .Brot',  aksl.  zito  .Getreide'.
*g^i-  in  kelt.  *hitu-j  air.  hith  (Gen.  hetho),  cymr.  hyd,  bret.  hed  .Weil gall.  Bitu-rlges,  d.  i.  .Leute  des  Weltkönigs'  (vgl.  die  ähnliche  Bed.  vd av.  gasd-ä) ;  daneben  hochstufiges  idg.  *gueito-  in  cymr.  bwyd  .essen^ acorn.  buit  .Speise',  abret.  hoitolion  .esciferis'.  nbret.  hoed  .Nahrung das  zweisilb.  air.  hiad.  Gen.  hiid  .Nahrung.  Speise'  (altes  *hiveto-m).
Mit  idg.  g'-Suffix  (guig-):  ahd.  queh  und  quek,  Gen.  queckes  , lebendig',  nhd? kecky  Schweiz,    check  .stark,   fest'   (kk  aus   einer   Form   mit  kiv  wie  mhd. quicken  .erquicken'),  ags.  cwicu,  cucu  .lebendig',  anord.  kvikr,  kykr  (Akk. kykkvan)  .lebendig',  auch  nhd.  Quecke,  ags.    cwice   .Hundegras'  (von  der außerordentlichen  Lebens-  und  Keimkraft  der  Pflanze);
lett.  dziga  .Leben'  (wie  dzive  ds.),  dziguot  .leben'  (wie  dztvuot  ds.).
Lat.  vigere  .lebenskräftig  sein'  von  vegere  zu  trennen,  scheint  unbe- rechtigt. Wood  KZ.  45,  68  reiht  an  nord.  kvikr  usw.  auch  viele  germ. Worte  für  lebhafte  Bewegung  aller  Art  an,  so  außer  anord.  kveikja  .be- leben, anzünden',  mit  anderen  Weiterbildungen  ags.  cwiferlice  Adv.  .eifrig', engl,  quiver  .lebhaft,  hurtig',  fries.  kwistern  .wedeln,  schwänzeln',  kwispeln .sich  rasch  und  unruhig  hin  und  her  bewegen',  schwed.  dial.  ^üIc?  .werfen', jüt.  kwlddr  .munter'.
B.  von  *g^iöu-,  g^^U'i
mit  l:  ai.  jlvd-  .lebendig,  m.  Leben',  apers.  jlva-,  av.  jva-  (d.  i.  jlva-) .lebendig'  =  lat.  vivus  ds.,  osk.  bivus  PI.  .vivi',  cymr.  biw,  corn.  hito .Hornvieh'  (.*Lebendvieh').  lit.  gyvas,  lett.  dzivs,  aksl.  z^v^  .lebendig';
mit  i:  gr.  ßiog  .Leben'  (*^i-w-05).  got.  qlus  .lebendig'  (gaqiunan  ,dva^fjv*), air.  biuj  beo,  cymr.  byw,  bret,  beo,  com.  byw,  bew  .lebendig'  (davon  kelt Hivo-tüt-s  in  air.   bethu,  Gen.  bethad  ==  cymr.  bywyd  .Leben');
f
469
mit  Ä-Suffix:  lat.  vlväx  ^lebenskräftig,  langlebig^,  bildungsähnlichmit  lit. (tuvökas  ^lebendig^,  entfernter  ai.  jlvaka-  ds. ;
jjjit  ^Suffix;  1.  mit  l:  Sii.  jlvita-m  , Leben,  Lebewesen  usw/,  lit.  gyvatä T  eben,  Lebensunterhalt,  Bauerngut^  ==  lat.  vlta  ,Leben^  (^gmwta)  und iksl.  zivoti  m.  ,Leben'^,  ai.  ßvatha-h ;
2.  mit  i:  ßioxrj,  msisc.  ßlovog]  ,Lebensatem  usw.^;
mit  oi:  lit.  gaiv��s  ,munter,  lebendig^;
verbale  Ableitung:  ai.  jivatij  av.  jvaiti  (d.  i.  jlvaiti)  ,lebt^,  ap.  jwä |g]r)e!^==  lat.  vlvöj  aksl.  zivq  ,lebe^  (Inf.  ziti  s.  oben),  erweitert  lit.  gyvenü lebe';  ai.  jinvati^ prd-jinösi  ,lebendig  sein,  sich  erregen;  anregen,  beleben, erquickend
WP.  I  668  ff.,  Meillet  Introduction^  165,  Specht  KZ.  62,  111,  Schwyzer Gr.  Gr.  I  298,  300,  330,  501^  675«,  Trautmann  75  f.
rMQi-  (oder  g^eJQ-):  g^I-  mit  Formans  -no-,  -lo-  ,Haut,  FelF?
Pä.  jina-  ,lederner  Sack^,  jlla-h  ,Schlauch^;  mir.  blan  ,Haut,  Fell'^;  das ir.  Wort  könnte  freilich  auch  zu  bhei-  ,schlagen^  gehören,  dessen  kelt. Vertreter  auch  die  Bed.  ,schneiden^  haben  (vgl.  scortum  :  scheren  u.  dgl.) ; s.  oben  S.  118.
WP.  I  666.
g^eid{hy  ,Schlamm,  halbfliissiger  Schmutz^?
Gr.    öetoa    ,Dreck,    Schlamm^   {*gueidh-ia    oder    -sa^    oder    *g^eid-s-a)  - vielleicht  anord.  kveisa  f.  , Beule,  Geschwulst^,  mnd.  quese  ,Blutblase^,  neben norw.  kvisa^  schwed.  kvissla  ds. ; aksl.  zid^k^  ,succosus^,  russ.  usw.  zidkij  , dünnflüssig;   weich,   biegsam^ WP.  I  671.
g^e/a-  ,überwältigen,  Gewalt,  gewaltsam  niederdrücken^;  g^iis.  ,Gewalt^ Aä.  jyä,  jiyä  f.  ,Ubergewalt^  (=  gr.  ßlct),  jyäna-m^  jyänl-h  ,Bedrückung^, jyäyän  ,mächtiger,  überlegener^,  jyestha-,  jyesthd-  ,mächtigst,  stärkst^ ; jdyati  (Per  f.  jigdya),ersiegtj  besiegt^  (av.  Inf.  jayäi,  Vollstufe  I  der  Wurzel, ,zu  besiegen^),  yaytsnw-  ,siegreich^,  Je^a?--  ,ersiegend,  besiegend^;  jindti  (Fut. jyäsyati,  Pass.  jlydte,  Partiz. ^*Ua-)  ,überwältigt,  unterdrückt^;  jigisati^  v,'^i\\ besiegen,  ersiegen^  ( :  av.  jijUaiti  ,sucht  für  sich  zu  erlangen,  ausfindig  zu machen^),  jigyü-  ,siegreich^ ;
ai.  jinäti  bedeutet  auch  ,um  etwas  bringen^,  jyäni-h  auch  ,Schwund, Verlust^  und  ist  so  zugleich  der  Fortsetzer  der  palatal  anlaut.  Wurzel  von av.  zinät  ,schädigt^,  apers.  adinät  ,brachte  worum,  nahm  weg^,  Partiz. Perf.  Pass.  dlta-,  av.  zyänäj  zyäni-  f.  ,Schädigung^,  Inf.  zyänäi  ,zu  schaden^, bal.  zinay  ,an  sich  reißen,  hastig  ergreifen,  mit  Gewalt  wegnehmen^ (außerarische  Entsprechungen  nicht  bekannt);
470  f
gr.  ßla  ^Gewalt'  (==  ai.  ßyä),  ßido),  ßiät^w  .zwinge',  ßiaiog  .gewalttäti uivuidioq  wohl  =  Arrlßiog]   ßlvslv  .futuere';,   Idei'  ßiveZ  Hes.   .vergewi tigen'    (wobei    ßlveXv    von    einem    Partiz.  *ßl-vö-g  =   ai.  jl-na-j    Gram abzuleiten  wäre);   nach  Liden  IF.  19,  328   mit  npers.  gäyad  .futuit', gädan,  gän,  von  einer  Wurzel  "^guäi-  oder  (?)  *guöi-,  die  nur  bei  letztere^ Ansatz  mit  giiei-  als  Dehnstufe  der  o-Abtönung  allenfalls  theoretisch  ver- einbar  wäre;
mit  gueid-  ,niederzwingen'  scheinen  auch  folgende  Worte  für  ;Schwächen entkräften';,  Intr.  Pass.  .zusammengehen,  altern,  hinschwinden'  ürsprün«^! zusammenzugehören :
ai.  jinäti  auch  .altert',  jyäni-h  .Altersschwäche',  djyäni-h  ,Unvergäng. lichkeit'.  jma-  .bejahrt,  alt'.  d-jUa-  .unversehrt,  unverwelkt',  d-fiti-k .Unversehrtheit',  jivri-  .alt.  gebrechlich,  hilflos',  av.  jyä-,  Präs.  jinäitx .schwächt',  ajyamna-  .sich  nicht  vermindernd,  unversieglich.  wozu  mhd. verqulnen,  Prät.  quein  .hinschwinden',  ags.  cwlnan,  ä-cwlnan^  Prät.  cwän .hinschwinden,  abnehmen,  kränkeln',  erweitert  ags.  ciuincan,  äcwincan .verschwinden,  abnehmen'  (Kaus.  mit  Ablautneubildung  acicencan,  engl. quench  .löschen'),  und  mit  m-Formans  wfäl.  kiüimen  .kränkeln',  kivmelig .verweichlicht'.
Aus  dem  Germ,  scheinen  in  beiden  Bedeutungsfärbungen  anreihbar:
anord.  kveita  .überwältigen'  (cZ-Präs.);  «-Erweiterungen  mnd.  quisi .umkommen  lassen,  verschwenden',  quist  .Schaden.  Verlust',  mnl.  quisten .terere.  atterere.  friare'.  got.  qistjan  .verderben',  ahd.  quist  f.  .Vernich- tung', archwistan,  firquistan  .verderben,  vernichten',  ags.  cioiesan  .zer- •  quetschen',  jüt.  kiols  .drücken,  auspressen',  nisl.  kveisa  .Bauchgrimmen' (.*Zwicken') ;  norw.  kveisa  .verkümmertes  Geschöpf,  kvisla  .hinschwinden'; ^-Erweiterung  (gebrochene  Reduplikation?)  fries.  kwlke,  kwikken  .zwicken', in  der  Bed.  abgeschwächt  in  preuß.  queicheln  .hätscheln'.
WP.  I  666  ff..  Schwyzer  Gr.  Gr.  I  300,  694.
```


## [2026-09-06T14:52:45.402Z] TOOL CALL #10: Bash

```json
{
 "command": "pdftoppm -f 204 -l 204 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg204 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


## [2026-09-06T14:52:46.617Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT jafra ===\"; grep -n \"jafra\\|jafnu\" BRT.txt | head -10; echo \"=== BRT gantay/ganti ===\"; grep -n \"gantay\\|gaiṇti\\|gainti\\|ganti-\" BRT.txt | head -15"
}
```


### [2026-09-06T14:52:47.916Z] TOOL RESULT

```
total 160
drwx------ 2 sfmqrb sfmqrb  4096 Sep  6 10:52 .
drwx------ 4 sfmqrb sfmqrb  4096 Sep  6 10:51 ..
-rw-rw-r-- 1 sfmqrb sfmqrb 70083 Sep  6 10:52 pg204.png
-rw-rw-r-- 1 sfmqrb sfmqrb 77858 Sep  6 10:52 pg206.png
```


### [2026-09-06T14:52:47.972Z] TOOL RESULT

```
=== BRT jafra ===
8494:•  j,  urv-äp-  Adj.  'des  Wasser  sich  weit ausdehnt,  mit  weiter  Wasserfläche' '' :  ainö.- /aya>um  . .  yahmya  jafra  varayö  °apat>hd (NPm.)'>  hisl-itie\i.io.  14;  —  *pasne  varöis *äu^aitahe  jafrahe  'spahe'^  YL  V49.
11100:•  j.  £aeiiasta-')  m.  Name  eines  Sees*': 't)m  vairlm  S.  2.9;  —  'iahe  varffi/ tfy. 5,5;  —  tarn  yatata  .  .  Aaosrava  *pasne varöi?  'tahe  jafrahe  urväpahe  Yt5.49.
11513:Vgl.  ^\.  jagkatevan,  ja^knrvan  -.jaghnäfah.  — ')  Ob  V  nach  S  368.  17  für  iv  (s.  das  i\. jaghnrvaa)'t  Oder  wnrde  «  sonantisch  ge- sproclien?  Ein  Ausgleich  zwischen  'jayarn'' und  *jafnu}'  konnte  wohl  (sekundär)  lu  einer solchen  Form  (mit  son.  n)  ßhren.
22796:von  Yima  auf  AAuras  Befehl  errichteten  D'e  Lesung  isi  nicht  recht  sicher.  Das  zweite Baus«:  Jat  t»m  -rptn  k?r?nava  ^ar^tu.-  "  »H'" falls  anaptykusch. drajS  ktmät  paiti  ca%rulanqm  V.  2.  2  5 '; '  •  j.  'varay-  :  vairi-  m.  'See**;  Bucht  einer 33*;  —  aat  mqsta  yimS  Aüia  tg  azim  Sc^':  airyö.iayamm  ..yaAmyajaJra'rayS.. 'rwt  ksrgnavane yä  ml aoxta  ahurS  mazdä  Yt.  10.  14;  —  bune  jafranqm  •iryanqm'^ V.2.31;  —   apifa  t>m  'r>m  manza  dva- ^t.  ir).  ^i,    V.  jp.  42;     —     'iflÜS    (AP.)
28733:%ai  . .  haraihyS  paiti  bamayä;  äat  ^wä . .  spmta  , .  mtnya  vlivama  vlbann  . .  Sat ttkva  paurvatahva  pouru.sar3hs  viraehahe 'mS  gaoma  zairi^aoiiB;  H  tl  ba^ata  irJ- ra'iar»  (sd)  .  .  Y.IO.  lofF.;  —  vlipe  'ma ufasiaomi  yoteit  barlnusva  gairinqm yaieii  jafnuSva  raonqm  yaiäi  atahu  thn- tanko. .  V.10.1 7; — yi>  barfsman  */rasl?r>nte 'mqsca  var^sisd.)ca  ..  ti.gj;  —  •m^m täirim  binzantifn  ..'m?m  fra^mim  frädat.- gafi-»>n  'mim  düraosim  yatamaide  Y.  lO. 3i;  7f.i,  Vr.  //.  a',  V.J9.19;  —  pasi^a fra»uharHÜ  'inahe  huiahe  H.  1. 9;  — vai>hus  *mö  huiätö  °mS  .  .  zairi^aons namyqsul  yaia  :^arinte  vahiitS  urunaica ps'^mainyB.hmö  Y.t).i6;  —  äriiyj  . .  ä/ri- Z'acaahs  zavainti  gäul^a  aspasc'a  'masca . .  'mS  ^älär»m  (sd.)  tavaiti  . .  Y.  //. 1—3;  — yasf  ti  bäla  °ma  zlire  gava iristoAe  baxsatte  'S..  10.  13;  —  hd yS  'mähe maid  (sd.)  asa  hacaite  urvilsmana  Y.  10.  8 ; YL  /7.  S  ;  —  nnjaiti  'mähe  mmö  Y.  lo.  8 ; —  als  Amulet;  'mim  batre  (Sp.  933  u.) *slliriJ)aoy»m  .  .  'imin  yim  nivizaili  (sd.) uivandät  apayettt  Vt  /4-  5  7 ;  S  7 ;  —  'm Kult;  'ma  .  .  asaya  kuitvana  asaya  hag- syanta  Vr,  g.  3  ;  12.  x,  3,  Y.g.  3,  4,  V.  18. 1 2 ;  — /rab?rita  *zaoi:ra  frabarStl. .  hävana 'man  hunyät  N.  61?;  —  hävananS  (näml. kairim  aahat)yal'mimca  ahunavat  anha- vammia  *vlmanitt  (Sp.  1135  u.)  ,.  *äsna- iars  yat  'mfmca  äsnayät  °m>mca  pairi.- hanzM . .  ^raehwiskarake  (sd.)  yat  'm^m^a gtiva  *rai'iaiay>Jt  baxsayäatla  N.j2-y6;  — 'manqmca  har.'iyamnanqm  ySi  hansyente ra^we  bimaiie  Vr. /2.  i;  Y.  2y.f>;  —  °m)m aiaya  usdutun  (Stverz.  Sp.  719  o.)  Y.  22. I  i  usw. ;  —  ahuräi  mazdäi  'ma  Sva^ia- yamoAl  Yi.ii.i;  i',  Yt.io.120;  —  imq 'mqsla  myazdqsia  zao%räsca  barasmala  . . gqmca  huiiänk)m  ..*m3mca paraMaomimca aismqsca  baothlmla  . .  pairica  dad»mahl . . Y.4'1;  3Z,7-i(>,  ''''■h  "3;  Vr.p.3, //.  3;  —  hSvanaca  tastaca  °maca  V. /fj.  9; 5.  39;  —  kal  in  'ma  yaozdayan  aahtn  . . yä  nasäum  avaJiirtta  .  .1  V.6.43;  —  neil 'mB  hutB  axtU , .  nSit  *nasus.ava.b3r>tS  (sd.) ava  alte  ahuta . .Y . 6. 4y,  — yö..aiiaiaons 'mähe  kutake  dalaiti  Y.iS.ia;  —  *jarsi/ *'r/wn''>  zarähusira  .  .  yaka  *%risar>m nitim^m  P.2p,  A) alsGottheit**>'*:  wni5 'mai  Y.p.3,  16,  /o.  13,  17,  Yt/7.  S;  — 'ntü   upail  tard>!uitr»m  .  .  ä  dtm  pmsat
=== BRT gantay/ganti ===
2516:•  j.  acxa-  n.  'Frost,  Eis':  kam.stirittm'^^^^  ..  deine  Z"  N.  Ö5.  a)  in  Verbin- 'sam  . .  dalum  apaohm  "den  erstarrenden  düng  mit  dem  Relativum:  *yH  He  . .  nöit Frost  .  ."  Yt.  /tf.  2 ;  6.  a)  Plur.  'Eis-  * srävayeinti  "qiii  ibi  . ."  N.  25  3).  H)  in felder":  *''xakuca'''"''  patti  *gaintis7a  rX-  schwachdeiktischer  Verwendung  'dieser, di'iänmnö  H.2.25.                                        der,  er":   I)  aufVorhergenanntes  —  oder
2801:Irrlehrer,  der  . ."  \.g,$i{.;  —  yavat  °fa *gaintii  upankacaili  (sd.)  V.  7.  56;  — yavat  'sa  ilß  bySrixfi  (sd.)  .  ,  frabavai \.i4.\y,  — yavat  -lö  spä  anya{sA.) )asö V./5.48,  a)mitrelativischemAnschIuss: "jS  zT  asti  baslazyö.t3mö  .  .yal  *mahnm.- sppni»m.baei'azyd  (sd.)  V.  7.44;  —  '/a  bi~ paitisiana  (sd.)  y3  kaine  V.  75. 19;  19;  — vXsp»m  ä  ahmst.,  yat  -ia  yö  apsntinyBkB uxjasnf  (sd.)  "bis  es,  das  Kind  . ,"  V.  75. 15;  —  'sa  yS  *ar?mBiidd'a.W3.  2)  auf ein  Relativum  als  dessen  Korrelat,  sub- stantivisch: ci'at  dra)ö  avaMUlüt  '^a  yö näirikaya  . .  !^ar>^3tn  frabamt  V.  /J.  4 1 ; —  °sö  .  .  aitayä  vihrkayh  (sd.)  Jq'^-wS.' tarö  *at3kat  . .  ya^a  spä  vtkrkake  k»r?- naoiti  V.  y .  4 1 ;  — "/?  ratufris  *yö  jayara N.if};  24,  60;  —  'sa  yetjhe  apirinSyükö ^•9i  7;  —  °^'''  zaoiranqm  tnaziltaca  . . yiJ  *naire  asaone  *daste  N.^4.  III)  In
9995:•  j.  gantay-  f.  libler  Genich,  Gestank'": yaf  aiia  *gainHs  upaaAacaiti  (sd.)  V.  j, 56;  —  *gainfli(a'^  vidihärimns  H.  2.  25.
13834:757  duzgantay-
13837:•  j.  duz-gantay-  Adj.  'übelriechend, stinkend':  väß  .  .  'gaintii  H.a.  25.
13839:•  j.  duigainti'tara- Adj.  'der  stinkendere': välö  ..  dusgaititis  'rS  anyaHbyB  vätalibyS H.2.2S.
13841:•  j.  duzgainti't^ma-  Adj. 'der  stinkendste' : yim  .  .  vätMn  .,  °mpm  ßgaurva  H.  2.  26.
25112:•  j.  rapaka-  Adj.  'eine  Stiitze  bildend für  -,  im  Dienst  stehend  von  — '  (Gen.): a^  (näml.  daxmS)  sJ  asti  daibaitqtn  'AS vupsm  a  oAmOi  yat  alfa  *gainti/ tipaioAa- aüti  (sd.)  V.7."s6.'
25629:yütii  yä  n»rqs  sädra  (sA)  drsgfoß  Y.  \  *gaintlsca)  —  vidiiäryinnS  sahayeiti;  ä  dim 45- 7 i  —  dr^vütö ..ydtyä  'vä  xraodaitl  väts  upa.vävO  salayäti  {sA.)  rapi^witarat HttvatB  ftnlä  aka  (sd.)  ¥.5/.  13;  —  at  ..\—  {apäxtarat)  —  iaca  naimat . .  hubae&i- dngvatS  akail  il'an'häis  i^A.)  pmtf  *vqnS' tarü  —  {duägaintitarS)  —  anyaiibyS  va- paityäntf  '^.4g.\\.  a)  neben  *daittä-\taähy8  H.2.  7;  25;  —  aAhä  dim  vä/ayi usw. :  karapanB  isvayasca  . .  yJng  afs  'vä  ■frSntOa  (sd.)  sai/ayätt  yl  hava  daOia ifai^  xraodai  {sA.)  damn  hyal  aibt.g3tian\kamtt0  kihrpa  sflrayä  H-2. 9**;  —  äat yahra  anvatö  pgntui  (sd.)  Y.  46.11;  —  Am  (nänü.  da&iqm,  sd,  Sp.  666  m.)  aoxta tatca  .  .  %v»akml  *ä  *dqm  (Sp,  684  o.)  ,p»nsS  yö  nari  asaotß  'va:  a^ca  caräitis m^inhi    matiS    voAs    'utiasca    asäunqm  i  ahi  yqm  it  yava  . .  sraistqm  äädarysa  (sd.)
```


## [2026-09-06T14:52:54.180Z] TOOL CALL #12: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg204.png"
}
```


### [2026-09-06T14:52:54.547Z] TOOL RESULT

```

```


## [2026-09-06T14:52:54.544Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T14:53:08.577Z] TOOL CALL #13: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg204.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/204.png && echo copied"
}
```


### [2026-09-06T14:53:08.644Z] TOOL RESULT

```
copied
```


## [2026-09-06T14:53:10.414Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KNT gasta ===\"; grep -n \"gasta\" KNT.txt | head -10; echo \"=== SYN gasta/stink/gand ===\"; grep -n \"gasta\\|gandīdan\\|OPers. gasta\" SYN.txt | head -20"
}
```


### [2026-09-06T14:53:10.497Z] TOOL RESULT

```
=== KNT gasta ===
1141:replaced by *batsta- in Iranian. gasta- evil’, pte. to pIE root in Av. ganti- ‘stench’,
1210:Sometimes OP has sí instead of st; this is probably analogical to the -sf- of dental stems, such as basta- to plE *bhendh-, gasta- ‘evil’ to рЇ® *gendh- (cf. §85), since pIE Ё and §(h) gave OP @ and d in other forms of the paradigm.! The examples are:
1490:azdi and Aura-maedüh-, with -dzdh-, see $85; for basta- and gasta-, with participial -tst- re- placing -dzdh-, see §85.
2627:(§58.D), Skt. baddhá-, but Av. basta-, OP basta-. pIE *gendh-: OP gasta- ‘evil’, cf. Skt. gandhd-
4705:A’Ha = Artaxerxes IT, HAMADAN A. 1 Gatiy : Artax&agà : XS : vazraka : XS : XSyanim : XS : DHyünàm : XŠ : ah 2 yaya : BUyà : Dárayavasahy& : XShya : puça : Dérayavasahyd : ArtaxSatra 3 hyà : XShy& : puça : Artaxšaðrahyā : Xšayāršahyā : XShya : puça : XSayar 4 šahyā : Darayavagahya : XShya : puça : Dérayavasahyd : V?Stáspahyà : puça 5 : Haxàmanisiya : imam : apadàna : vašnā : AM : Anah*la : иа : Mitra : adam : akun 6 ат : AM : Anah'ta : uta : Mitra : mam : püluv : ћасӣ : vispd : gaslá : ut Т & : imam : tya : akunà : mà : vijanátiy : mà : vinátayàtuy Notes то А?На: *? ArtazXatrahyá, acc. to Tm. Lex. 54, and not -cahyd. * [hacd : gastá] WB; [utàmaiy : zsagam] Tm.; [ћасӣ : vispé : gasta] Kent, after A°Sd. " akuna for akundm, and ma with following lost verb, as in A'Sa;
5359:gan- vb., see jan-. gand- vb., see gasta-.
5371:gasta- adj. ‘repugnant, evil’; пі, as sb., ‘evil, harm’: past pte. ($85, $242.I) of vb. *gant- *gandh- ‘smell’, Av. ganti- ‘evil odor’ (AIW 493), duZ-gantt- ‘evil-smelling’ (AiW 757), Skt. gandhá- ‘odor’ (Bv. Gr. $179); for meaning, ef. Lt. odor ‘smell’, бй ‘(I have smelled), I hate’, odium ‘dislike, hatred’. Not abstract to same root, *gant-tdi-, nom. gasta', abl. shortened by haplology, as taken by Hz. AMI 8.68, ApL 173-7. gastá nsf. DNa 57f. дазій absn. DNa 52; XPh 57; ASa 5°; A’Sde 4 (gasta da, db; $53); A?Ha 6°.
=== SYN gasta/stink/gand ===
13809:2, Lat. catena (>It. catena, Fr. chaine, Sp. cadena; also Celt. and Gmc. words, below), etym. dub., but perh. : cassis (*cat-sis) ‘hunting net’, Skt. gasta- ‘sort of belt’. Walde-P. 1.338. Wald-H. 1.177f. Ernout-M. 162. (Etruscan orig, ?)
18784:Goth. gastaldan, aigan Lith. turetz a ie ie) ON Ape Lett. phrase = have ‘ iat possidére, tenére Dan. je, besidde ChSl. pritezati, siitezali | It possedere Sw. dga, bestia SCr. posjedovatt (imatz) fr. _posséder OE dgan, Ggnian, steal- Boh. = dreti (mitt) bp. poseer dan Pol.  posiadaé, dzierzeé Rum. poseda ME owe (ohne) (miéé) I. _techlaim, selbaim NE own, possess Russ. vladet’, obladat’, imet’ Nr. sealbhuighim Du. bezitten Skt. = ‘have’, ksi-, ig- W.  meddu OHG  bisizzan, eigan Av. = ‘have’ Br. piaoua MHG besitzen
18800:4. Goth. gastaldan, renders xréopat and once éw (gastaldand = eouow, Cor. 7.28), cf. andstaldan ‘supply with’, OE  stealdan ‘possess’ : OF gesteald ‘dwelling’, hagu-steald, OHG hagu-stalt, etc. ‘one living in the lord’s house, un- married person’, fr. an extension of the root *stel- in OE séellan, OHG stellen ‘put, place’, etc. Walde-P. 2.646. Feist 50.
18945:F rth. ar erneker 258. Bat at” g. (807). B ee 11.16 GET, OBTAIN Goth. gastaldan Lith. gauti Grk. eS (ralpr) ON Le pele. ne ere i Tete dimisch Dan. faa . poluciti . nancisci, adipisct, a fa SCr. dobili pe? OE begielan Boh.  dostati, dobylti : oor ME _ gete, obteine Pol. cee te 0 y Keg! , , Y t NE get, obtain Russ. polutit’, dostat', dobyt : eine, Du. krijgen, bekomen Skt.  dp- am adcola (3sg.) OHG (bi)gezan Av. Sra-ap- Nir. faghaim MHG (er)krigen (bekom- is caffael, cael . men) kavout NHG kriegen, bekommen
18965:4. Goth. gastaldan ‘possess’ (11.12), also ‘get, acquire’ (gastaistald = éxrnoé- unv Neh. 5.16).
19350:Fr. also ‘lay waste’; Sp. gastar ‘waste, spend’), fr. a blend of Lat. vastare and (init. fr.) Gme. *wdstjan (OS awostian, OHG wuosten), both ‘lay waste’, and derivs. of the adjs. Lat. vastus and OHG wuostt, etc. ‘empty, waste’, themselves cognate. REW 9168. Gamillscheg 461,
20526:Sp. gasto, also and orig. ‘waste’, fr. gastar ‘waste, spend’, this fr. Gmc., OHG wuostan, etc. ‘lay waste’. REW 9168.
22305:Av. daogatara-, daogastara-, adj. (-3- fr. usastara- ‘eastern’), fr. *daogq- ‘eve. ning, west’ = Skt. dosa- ‘evening, dark- ness’ (prob. : dicis, etc., above, 1), Barth. 674. Walde-P. 1.777 f.
26001:Skt. gandha- : Av. ganti- ‘bad smell’, OPers. gasta- ‘offensive’ (NPers. gast ‘bad’), fr. a root seen in gandh- ‘hit, in- jure’, Lith. gesti, gendu ‘spoil’, etc. Walde-P. 1.672 f.
29729:OPers. gasta- (‘repugnant’ or already ‘bad’, as NPers. gast), pple. of root in Skt. gandha- ‘smell’ (obj.), Av. ganii- NPers. gand ‘stench’ (15.23).
```


## [2026-09-06T14:53:18.091Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ndef page_of(fn, needles, off, label):\n    t=open(fn,encoding='utf-8',errors='replace').read()\n    lines=t.split('\\n')\n    pos=0\n    ffs=[]\n    for i,l in enumerate(lines):\n        for n in needles:\n            if n in l:\n                idx=sum(len(x)+1 for x in lines[:i])\n                leaf=t[:idx].count('\\f')\n                print(label, 'line',i+1,'leaf',leaf,'printed', leaf-off, '|', l[:90])\npage_of('SYN.txt', [\"Skt. gandha- : Av. ganti-\",\"OPers. gasta- (‘repugnant’\"], 24, 'SYN')\npage_of('KNT.txt', [\"gasta- adj. ‘repugnant\"], 15, 'KNT')\nEOF"
}
```


### [2026-09-06T14:53:19.830Z] TOOL RESULT

```
SYN line 26001 leaf 1101 printed 1077 | Skt. gandha- : Av. ganti- ‘bad smell’, OPers. gasta- ‘offensive’ (NPers. gast ‘bad’), fr. 
SYN line 29729 leaf 1266 printed 1242 | OPers. gasta- (‘repugnant’ or already ‘bad’, as NPers. gast), pple. of root in Skt. gandha
KNT line 5371 leaf 206 printed 191 | gasta- adj. ‘repugnant, evil’; пі, as sb., ‘evil, harm’: past pte. ($85, $242.I) of vb. *g
```


## [2026-09-06T14:53:19.933Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD ===\"; grep -n \"gand\\b\\|gandag\\|gast\\b\\|žafr\\|zafr\\|jafr\" PHD.txt PHD_mackenzie.txt | head -25; echo \"=== NYB ===\"; grep -n \"gand\\|gast\" NYB_vol2_glossary.txt | head -15"
}
```


### [2026-09-06T14:53:20.008Z] TOOL RESULT

```
=== PHD ===
PHD.txt:316:drón yaštan: consecrate the sacrificial bread. drēš [410] mark, branding; punishment. ~ag [-k!] *desolation. drēšīdan, dro$- [d/w$-ytn'] brand. drēūšom [dlwšwm] mark. droz-, v. druxtan. drózan [dlwen! | M, J drwzn] lying, liar. ^h: falsehood. drubušt [di(w)pwst'] fortress. ~ih: defence, fortification. drüdan, *drün- (HCDLWN-tn! < A У hsd | M ача, (dwr-), N durüdan, diraw-] reap, mow. drust [drw(y)st' | (M dryst), N durust] right; well, healthy. —Ih: righteous; health. drustabed [drwystpt'] chief physician. društ [dlwšt' | N durust] harsh, rough, severe. ~ih: harshness, severity. ~-Awaz, ~-éwaz [-p'c, ~yw’c] harsh-spoken. druwand [dlwnd | M drwnd] evil, sinful, unrighteous. ~īh: sin, unrighteousness. druxtan, dróz- [dlwhtn', dlwc- | M drwxt, drwz-] lie, deceive. druz [dlwe | (P drwj)] demon. айа [dwt! | M dwd, N ~] smoke. düdag [dwtk! | N —a] family. dudigar [dtykl | M dwdygr, N digar] second. duj-, = duš-. ~-daft [dwsdpt'] ill-breathing, short of breath. ~-dānāg [dwšd”7?k!] ignorant. ~-dén [dwšdyn' | M dwjdyn-] of evil religion. «=dēys*rīh [dwsdwyslyh] the evil eye. ~-gand (dtwsgnd | P dwjgnd] stinking. ~-gandih: stench. dum(b) [dwm(b') | N ~] tail. ~dmand [-'wmnd) tailed. ааг [LH YK'! < А rhyq; dul | M dur, N ~] far, distant, remote. durgar [dwlgl | N ~] carpenter. dusraw [dwslwb!] notorious, dishonoured. ^Ah : notoriety, dishonour. duš- [dws- | = M] ill-, evil-. ~īh: evil, wickedness. ~-абаһ [dw??^ Es] foolish, stupid, ignorant. ~-абаһіһ : foolishness, stupidity. ~-arz [2 ic] worthless. 7--Ca&m [-cém] envious. —-Ca$mih: envy. ~-tihr [-cyhl | M dwfcyhr] ugly, hideous.
PHD.txt:378:galēģ [glwk' | N guld] throat. бато [gm | = M, N ~j pace, step, stride; a yard (3 ft.). ~ í dó pay: a pace (s ft.). -рапаб [-k’nk' | M eng, N -gàna] suffix forming numerical adjectives, -fold. бапа [gnd | N ~] stench. gandag [gndk' | (M gng), N —a] foul, stinking. ~th: stench. ģandanāģ [gndn’k' | N gandanā] leek. gandum [Hš < A nth | (M gnwm), N ~] wheat. ganj [gnc | (M gnz), N e treasure, treasury. ~war [-wbl | M -wr, N ~] treasurer. ģan(n)āģ [gr &! | (P gnd?g)] foul, corrupt (v. gandag). ~ ménó$g the Evil Spirit. ~ih: corruption. gar [gl] mountain. -gar [-Al, -gl | M -gr, N ~] suffix forming actor nouns. -gar [-£1| M -g’r, N ~] suffix forming actor nouns. garan [gPn! | M г?л, N girán] heavy, serious, difficult. АҺ; heaviness, weight. garasman [glsm’n' | М ртт?п] = garddman. gard [g/t! | N ~] dust. gardan [gitn! | M grdn, N ~] neck. ģardānāģ [gl h] die (for gaming). gardanidan, gardan- [gl n-ytn! | M grd(y)nydn, N ~] turn (tr.). gardidan, gard- [git-yin' | M grd-, N ~] turn, revolve. ~išn: revolution, turning. garm [gim | M grm, N ~] warm, hot. «„«ih: warmth, heat. garm-ābag [gim'pk! | N ~a] bath-house. garmāģ [glm^ k! | М grmg, N garmá] warmth, heat. g£armóg [gimwk!] warm, ardent, fervent. garmówar(ih) [glmwk wl(yh)] heat ordeal. ģarmsēr [gimsyl | N ~] warm region, lowlands. garódman [glwtmn' = Av. garó dəmana- | M grdm?n] paradise. ~ig [-yk'] (worthy) of paradise. yarranag [g”7k! | M grn’g ?] thunder. yarranidan, yarran- [gl’n-ytn' | (N yurridan)] roar, thunder. ~i$n: roaring. garzag [gick! | N garza] snake, serpent. garzidan, garz- [glc-ytn'] complain; confess. ~i$n: complaint. ~iSnig : complaining. gaw [gw!'] hand (daevic). базу [ТИРА < А twr) | M gw, N ~] ox, bull, cow; astr. Taurus. gawars [PZ < A prg’; g”wls | N ~] sorghum, giant millet.
PHD.txt:542:~ AZ: free (oneself) from. pargandan, pargan- [plkn-, plgn-dn! | (P pr'gnd, N parāgandan)] scatter, distribute, disperse. pargast [plgst' | N ~] let it not happen! Heaven forbid! pargüd [plgwt' | P prgwdg], ~ az: free, exempt from. parig [plyk' | M pryg, N pari] witch. paristag [pistk! | N pirista] servant. ~th: service; worship. paristar [plsť] | N parastár] maidservant. paristidan, parist- [plst-ytn' | M pryst-, N parastidan] serve, worship. ~išn: service, worship. paristog/k [plstwk' | P prstwg, N piristū(k)] swallow. рагпабап [pinyE?n! | M prng?n, N parniyān] polychrome damask. parr [pl | M pr, N ~] feather, wing. parrag [plk', pig | P prg, N ~a] wing. ~ig [-vk'] winged. parréxtan, parréz- [plyhin', plyc-] remain over, be superfluous. parrón [plwn' | M prwn] hence, away. parrwar [plwl | M prwr] winged. parsig [p’lsyk' | N pārsī] Persian. pars [5/f] spotted, speckled. parwāl [plwl | (P prwrz)] refreshment, nourishment. parwal- [plw���l- | (P prwrz'dn)) foster, nourish, -išn: nourishment. parwanag [phonk! | M prw’ng, N ~a] guide, leader. ^h : guidance, leadership. parwand [plwnd | N —] enclosure, comprehension. parwand-, v. parwastan. P parwānģāh [*plw?ng’s] throne. parwār [plyw?l | N ~] citadel; circumvallation; suburb, surroundings. parwardan, parwar- [plwl-tn' | M prwrdn, N ~) foster, nourish, cherish, educate. ~išn: nourishment, fostering, education. parwast [plwst'] enclosure. parwastan, parwand- [plwstn', plwnd-] surround, enclose, contain, comprise. parwāz [plw’c | N ~] flight. parzin [picyn' | M prcyn, J przyn, (N parčīn)] fence, hedge. pas [AHL < A?hr; BATL < Ab2tr; ps| = M, N ~] then, afterwards, behind. ~ az: after. ~ih: rear. pas [p’s | = M, N ~] guard, watch. ~ dāštan: keep watch, guard. pāsbān [p’sp’n' | M p’sb’n, N ~] guardian, watcher. ~ih: defence, protection.
PHD.txt:555:rabih [/pyh | M rbyh] noon, midday (heat). rad [/t! | N —] (spiritual) chief, master. АҺ: office of rad. rad [Pu | P rd, N ~] generous, liberal. ~ih: generosity, liberality. radag [itk! | M rdg, N rada] line, rank, row. radómand [/t?^wmnd] having a rad. rad-passag [/tps’k'] ceremonies of the gáhanbar festivals. radunay [/twny = Av. ratunaya-] one under the guidance of a rad. raftan, raw- [SGY TWN-tn! < А V sg’; lwb- | M rptn, rw-, N ~] go, move, proceed. ~išn, v. rawišn. raftār [/pt?] | N ~] goer. rag А! | M rg, N ~] vein. «ЛЬ: disposition, character. ray [/gy | P rg] quick, swift. ray [Pg | N —] meadow, plain. rah [/s, lh, [hy | M rh(y)] chariot, wagon. rah-, у. rastan. rah [Ps | M rh, N ~] road, way. rahag [/hk! | P rhg] = rag. rāh-dār [lsd] | N ~] brigand, highway robber. ~ih: brigandage. rahig [/syk!, Ikyk' | M rhyg, N rahi] child, page. ~ih: childhood. rāh-nimāy [Psnm?d | (M r’-hnmwd’r), № ~numa] guide. ram [Pm | М әт, N ~] peace; cal. 21st day. ram(ag) [/m(k') | P rm, N ram(a)] herd, flock. ráménidan, rāmēn- [Pmyn-ytn! | M ?myn-] give peace, pleasure. rāmišn [P min! | M rmyfn, N rāmi$] peace, ease, pleasure. ~ig [-vk! | N —z#] peaceful, at ease. ran [Рп! | N ~] thigh. P rān- [/^n-] fight. randidan, rand- [/nd-ytn! | N —] scratch, grate, abrade. rang [/ng | M rng, N —] colour, dye. ranj [Inc | P rnj, (M rnz), N ~] toil, trouble. ~ag [-k' | N —a] troubled. ranjénidan, ranjén- [/ncyn-ytn'] trouble.
PHD.txt:566:se-pay [3-p'd | N sipá] three-legged. sēr, v. Sagr. se-Sabag [3-spk!] three-night-long, trinoctial. seyom [зит | N ~] -third (in compound numerals). sëzd [s(y)zd | P syzd, (N séz/agi?)] might, tyranny; tyrannous. sézdah [sycdh | M syzdh, N ~] thirteen. sézdén [s(y)zdyn! | P syzdyn] mighty, tyrannous. si [sy] goose. sidig(ar) [styk', -kl | M sdyg, N sidigar] third. sih [30 | M syh, N si] thirty. ~om [-wm] thirtieth. sik [HLYA < А hP; sk | N ~] vinegar. sisimbar [sysymbl, -nbl | N sisambar] sisymbrium, wild-thyme. *Skandar [swkndl | N sikandar) = Aleksandar. snāh [sph] blow, strike, violence. sneh [snyh] sword. snéxr [snyhl] snow. snézag [snyck!] snow. snóy [snwd] (rain-, snow-)cloud. sófistà [swkpst’k'] sophist. 1s68 [swk'] use, profit, advantage. 25806 [swk!'] burning, combustion. 3806 [swk! | N só(y)] side, direction. sógand [swknd | M swgnd, N saugand] oath. ~ XWardan: take, swear an oath. sóhistan, sóh- [swh-stn'] touch, feel. ~iSn: feeling, sense. ~iSnig : feeling, sensitive. sēr [sz] salty. ~ag [-k!] salt (land). ѕӧзап [swsn! | N ~] lily. Só&yans [swkšydns = Av. saošyās] saviour (especially the final Saviour who will bring about the frašagird). sóxtan, sūz- [swhtn!, swe- | М swxt, swc-, N ~] burn. ~išn: burning, combustion. ~išnīg: burning, flaming. sūzāg [swo k! | М swe'gyn, N séza] burning. sózan [swen' | N ~] needle. spāh [sp’h | N sipah] army. ~bed [-pt! | N -bud] general, commander. spandān [spnd”x! | N sip~] mustard seed. Spandarmad [spndrmt'] N isfandármuó] Holy Thought, the fourth Amahraspand, earth goddess; cal. 12th month; sth day. spar [spl | M ‘spr, N sipar] shield. spar-, v. spurdan. spas [sp’s | M ?s-, “р>, N sipas] service, gratitude, thanks.
PHD.txt:1090:brigand rahdar.
PHD.txt:1091:brigandage rāhdārīh.
PHD.txt:1657:distribute baxtan, pargandan.
PHD.txt:2023:foul gandag, gannag, püdag.
PHD.txt:2950:oath sógand, war.
PHD.txt:3811:stench gand, gandagih, dujgandih.
PHD.txt:3820:stinking gandag, dujgand.
PHD.txt:3907:swear (oath) sogand xwardan.
PHD.txt:4682:frasang parragig pargan- parwar pargandan pargüd frég, parig frest- fréstadan fréstidan pargast fréstag fréb
PHD.txt:5415:duSoxig dušox dušxwaršt dušhumat gūšūsrūd dušxwadāyīh dušāgāh dušāgāhīh dūšāram dušarz dušīh dujdānāg yojdahr yójdahrih yojdahrgar yējdahrgarīh dujdén dušgēwišn dujgand dujgandīh dujdēysšrīh dūšīzagīh dēšīzag dujdatt
PHD.txt:5450:gandanag drahm! gandagih
PHD.txt:5451:| gandag dóvs?r jūvišn judāgīh judāg judbēš jud-dādcstān! jud judnāy -Cnīdan 1 *lawīdan juttar
PHD.txt:5471:gand, бу, gung, jang, jov, juy
PHD.txt:5509:snóy déwók sanwar dēnūdag 1-356g sūgand Skandar sūfistā Sūšyans sor, sür sūrāx stirigomand sūrāg sūragīg
PHD_mackenzie.txt:2444:gand [gnd I N -..] stench.
PHD_mackenzie.txt:2445:gandag [gndk' I (M gng), N """a] foul, stinking.
PHD_mackenzie.txt:2451:gan(n)ag [gn)k I (P gnd)g)] foul, corrupt (v. gandag).
PHD_mackenzie.txt:4033: pargast [plgst' IN,....,] let it not happen! Heaven forbid!
PHD_mackenzie.txt:4320:rAh-dar [l'sd)ll N ......] brigand, highway robber.
PHD_mackenzie.txt:4321:   ......ih: brigandage.
=== NYB ===
477:apa-cand [pend] pt. pass. thrown away daru i jün-—-it thy trunk (body) whose life is thrown away, which is lifeless 267. — Pt. pass. of *apa-can- = apa-kan-, v. apakandan, NP aužand ‘thrown’ = afgand (BQ), whence a den. v. auzandidan (BQ, Steingass). Cf also NP bazandi ‘disap- pointment, helplessness, poverty’ (BQ, Steingass), abstr. of "bažand which may safely be derived from "aBa-žand < apa- cand ‘cast down’. V. also daru.
496:apa-kandan [LMYTN-tn'; Prth RMY-] pt. = pret. pass. 3d p. sg. apakand, written LMYTN without complement HajB:8, books LMYTN-t', Prth RMY-t HajA:7; LMYTN without complement = opt. apakané HajB:15; subju. 2nd p. sg. LMYTN-h = apakanäh 1009; cond. 2nd p. sg. LMYTN-t' HWH'-? = apakand hà 2226: to throw; bē ~ to throw away, with 6 or andar 6 to, into, against 2226 etc. passim; to throw (a bucket into the well) 142°. 151; to drive (a horse) against (6) 1145; to shoot (an arrow) HajA: 7. B: 8.15; - to arouse (fear) 5278; 6 miyān ~ to provoke (enmity) 10715; pat menišn 1... m to suggest to a p.’s mind 3712-13; — pt. apakand fallen, slain 2626. — < Olr *apa-kan- and *upa-kan- (v.s. v. apa-), from kandan, q.v.; MPrthPrs >bgndn; Verbum 172, Ghilain 55; Paz. pt. awagad, pres. awa-gan- (SGV); NP afgan- dan, augandan. V. also apa-cand, frakan- dan, pargandak.
1406:*duš-viyāk [dwSwyd’k] *nasty-smelling, *stinking 859-13-20; Paz. substitutes duš- gand. — Y suppose viyāk < *vayäk, pt. of Av. (1406) va- ‘to blow’ (Skr also ‘to smell’) whence Av. vayu-, v.S. v. vāt; Mir vénik, NP bini ‘nose’ < *vayana-.
1621:gandakéh [gndkyh] stench 62%, — Cf Av. (493) ganti-; MPrth gndgyft (S), cf gnd’g ‘fetid’ (A-H III); MPrs gngyy (A- H I); Paz. gandai, cf gand ‘stench’, gandaa ‘fetid’; NP gand, ganda 'any- thing putrid’, gandagi ‘filth’.
2036:scent, of Paradise 7320-25, 761, 857.11; comp. ~-tar 7321. — Paz. hüböi. V. bod. hubódéh sweet scent, the quality of being sweet-scented 621%, opp. gandakéh; hac hamäk ~ hubodtar 7371. — Paz. hubdi. Huböd-Xösröi [hwbwd-hwsrwd] a town 114%, cf s. v. Xosroi.
2196:kandan [HPLWN-tn', kndn'] kan- 1. to dig, pl. kand engraved 113%. — 2. to destroy 4271, 7114. 9918; to tear up by the root 3316, — 3. bé ~ to throw out, to drive away 34’. — Two different vbs.: 1. Av. OP (437 sg.) 2kan-‘ to dig’, whence also gukān- (g. v.); 2. kan- ‘to throw’, whence also apakandan, frakandan, par- gandan, Morgenstierne, AO I, 249; Ver- bum 172. MPrs and NP ‘to dig’, Paz. cadan, xan- with an initial x- confirmed by the Arab. lw. randag ‘trench’ and Skr khan- (pt. khāta-). V. also kanišn.
2945:par-bütan [pr-YHWWN-tn'] to shun, to avoid: yuvatak hac 63%. — I maintain the reading of the MSS; J.-A. deleted pr-. From Olr pard (Av. 852 pard) + butan, cf MPrs przyr ‘to abstain from’, prer- ‘to avoid’ <  "para-car-; prgn- (v. pargandak); Verbum 227.
2954:pargandak [plgndk'] scattered, dispersed 1092-10, 1121, — Pt. of para + kan- ‘to throw’ (Verbum 227), v. apakandan; M Prs prgn- (S); NP pargandah (the vb. is here pardgandan).
2955:pargandakéh the state of being scattered 111/5. 1122-8,
2956:pargandakiha [~-yh’] ina scattered state (some parts here and others there) 108%.
3191:pūt [*pwt'] putrid matter 76%, — MS pwn, but Paz. pid, Skr. v. durgandhi; Av. (909) pūti- *putrescence'.
3460:sökand [swknd] oath; ~ xtartan to swear an oath (pat by) 2118-23, 2225, 2322. — Ps. swkndy; MPrs swgnd; Paz. sawagand (SGV); NP saugand.
4645:Glossary and Index of the Pahlavi Texts of the book of Arda Viraf, the tale of Gosht-i Fryano, the Hadokht Nask, and to some extracts from the Din-kard and Nirangastan, prepared from Destur Hoshangji Jamaspji Asa’s Glossary to the Arda Viraf Namah. and from the original texts, with notes on Pahlavi grammar, by E. W. West, revised by Martin Haug. London & Bombay 1874. V. also Paz. AV. AZ = Ayyätkär i Zareràn v. MP I, p. XII sg.
4758:Nir. ed. Sanj. = Nirangastan. A photozincographic Facsimile of a MS belonging to Shams ul-ulama Dastur Dr. Hoshangjee Jamaspjse of Poona edited ... by Darab Dastur Peshotan Sanjana. Bombay 1894.
5147:gač0a: gēhān, gētāh fra-gam-: fražaftan gāman-: gam Gandarewa: Gandarv ganti-: gandakēh Gao-cidra: Göcihr lgaona-: gönak lgaona-: cigön gaosponta-: Göspand gaoyaoti-: gäviyöt gaoša-: gos
```


## [2026-09-06T14:53:28.955Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD zofr/deep ===\"; grep -n \"zofr\\|zopr\\|zufr\\|zwpl\\|deep\\b\" PHD_mackenzie.txt | head -20"
}
```


### [2026-09-06T14:53:29.019Z] TOOL RESULT

```
=== PHD zofr/deep ===
3686:·nayda~ [n)ywt>k ] deep, unfordable, navigable.
5840:zofay [zwp)d 1M zwp)y] deep; depth.
5842:zofr [zwpll M zwwpr, J zwrf, (N zarf)] deep.
5844:  ....-payag [-p)dyk ] deep.
6356: deep zofay, zofr(-payag); (water)          desperate gyiin-abespiir.
6393:   zofray.                                 digestible hugugiir.
9773:zofr                      ~Q)~      zcfiin                    \r' cu---S
9774:zofray                  ~Cl)lS      zist                       ,~
9775:zofr-payag       \¥O-~Q)~           zayt
```


## [2026-09-06T14:53:30.525Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN zarf ===\"; grep -n \"zarf\\|žarf\\|zerf\\|ẓarf\\|zarfâ\" HRN.txt | head -20; echo \"=== HRN gand ===\"; grep -n \"gand\\b\\|gandīdan\\|gandīden\" HRN.txt | head -20"
}
```


### [2026-09-06T14:53:30.621Z] TOOL RESULT

```
=== HRN zarf ===
6040:685. Serf 'tief*, PJniT (Is. 29, 15 ^), zerfi;.
14135:zerfi 68Ö.
=== HRN gand ===
1084:Geldner, Drei Yasht 27)^); phlv. argand [argimd ist
8115:aw. gaifiti- 'Gestank'; phlv. gand 'Gestank', gandak
8118:af}'. ganda 'stinkend'; bei. LW. gand 'Kot, Mist'
10403:duzdaena-), dtisdänäk (aw. duMäo), dmgand (Men.,
15959:'Iiiigand 70.
```


## [2026-09-06T14:53:41.237Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('HRN.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor target in [6040,8115]:\n    i=target-1\n    idx=sum(len(x)+1 for x in lines[:i])\n    leaf=t[:idx].count('\\f')\n    print('line',target,'leaf',leaf,'printed',leaf-21)\n    print('\\n'.join(lines[i-3:i+6]))\n    print('-----')\nEOF"
}
```


### [2026-09-06T14:53:43.623Z] TOOL RESULT

```
line 6040 leaf 173 printed 152
Diese Etymologie verdient vor der meinigen (KZ.
32, 588 No. 23) aus skr. Jada- 'kalt, starr, regungs-
los den Vorzug.
685. Serf 'tief*, PJniT (Is. 29, 15 ^), zerfi;.
aw. jfafra- 'tief; phlv. zufar^ zafr.
kurd. ziör, zaza /ör; afy. zavar; bei. juhl, n. jahl
(178).
686. MobTti, zöpm-), zöpin 'kurzer Speer (in Gelän bezw.
Delem gebräuchlich)', pDIT (Jer. 50, 42).
-----
line 8115 leaf 230 printed 209
ist verschrieben). Gewiss wird es sich im Np. noch häufiger finden.
Auch kurd. gtirdale (s. oben No. 905) wird hierher gehören (Correctur-
note).- 209 -
aw. gaifiti- 'Gestank'; phlv. gand 'Gestank', gandak
stinkend*, gandakth ; ai. gandhd- *Geruch, Duft (wohl-
riechend)'.
af}'. ganda 'stinkend'; bei. LW. gand 'Kot, Mist'
(97) — gandag, n. ganday schlecht, böse' dagegen stellt
Bartholomae, ZDMG. 44, 552 zu ap. gasta- *übel,
-----
```


## [2026-09-06T14:53:53.063Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '8100,8125p' HRN.txt"
}
```


### [2026-09-06T14:53:53.112Z] TOOL RESULT

```
egl, gende, gendamden (AM. 45 Zeile 1; 78 Zeile 3
V. u.).
*) Lautlich stünde der Heranziehung von skr. \y^gorj-^ garjati
*brüllen, brummen, toben, brausen, tosen* nichts entgegen; denn sowohl
e/i wie g^h setzen ein ap. d voraus. Doch stimmt die Bedeutung von
garh^ besser als die von garj- (s. auch Bartholoma e, ZDMG. 44, 552).
notirt : hüzle *junge Ziege', desle 'Händchen', yellele 'Bischen, Stückchen*,
kuzowle 'Wasserkrüglein', kulaile *Köter* (eigentlich Demin. von kulai
'Hofhund'j, nazule 'Kätzchen*, perdele 'Häutchen', segle 'Hündchen*,
/unele 'Häuschen'.
Dasselbe Suffix erkenne ich nunmehr in np. ähle 'Bläschen' (AM.
50, 14; 153, 11), auch abile^ äwile^ vergl. äbek (änek^ VuUers No. 2 s. v.
ist verschrieben). Gewiss wird es sich im Np. noch häufiger finden.
Auch kurd. gtirdale (s. oben No. 905) wird hierher gehören (Correctur-
note).- 209 -
aw. gaifiti- 'Gestank'; phlv. gand 'Gestank', gandak
stinkend*, gandakth ; ai. gandhd- *Geruch, Duft (wohl-
riechend)'.
af}'. ganda 'stinkend'; bei. LW. gand 'Kot, Mist'
(97) — gandag, n. ganday schlecht, böse' dagegen stellt
Bartholomae, ZDMG. 44, 552 zu ap. gasta- *übel,
widerwärtig* ; sar. yofid.
935. gend/um *Weizen', ar. LW. jandum in jauz-i jandum.
skr. gödhüma- 'Weizen* (dagegen iran. ^gandhüma-^
Hübschmann, ZDMG. 44, 556 2)); phlv.-paz. gantum
d. i. gandum (PPGl.).
```


## [2026-09-06T14:53:54.840Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HUB ===\"; grep -n \"jafra\\|zafr\\|žarf\\|gand \\|gantay\\|gaiṇti\\|gasta\" HUB.txt | head -20; echo \"=== CHEUNG gand ===\"; grep -n \"GAND\\|\\*gand\" CHEUNG.txt | head -20"
}
```


### [2026-09-06T14:53:54.904Z] TOOL RESULT

```
=== HUB ===
2721:757. Es ist Haugand zu sprechen, vgl. sougdnd bei Rosen,
4486:(A gat bias), lat. Segestani (Am mi an), arm. Sagastan^
5515:gardtdaUy gastan (pr. gardam) 'sich drehen, wenden',
5728:Min. Gl. 207; gastan in dusman-gastl Shk. 242 neben
6520:in: zd. gafya- *Tiefe*, jafra- *tief, jqfnu- 'Tiefe von arisch
6521:gap, jap neben zd. jaiwi- *tief (das fiir jafra- in Komp.
6943:angastan = angdrdan *glauben, halten fiir', pr. angdram,
6967:angird^ angirdl *a summary* (also die Form angastan jedenfnlls nicht
6971:Unklar ist daa Verhaltniss von gastan wenden, drehen'
6972:(iiber das ^v.^garam s. Horn p. 198 Anm. 1) und gastan *sich
6980:zu gastan u. s. w. werden konnte ^). Es liegt daher nahe zu
8502:nigastan malen, nigar 'Bild*, arm. nkar 'Gemalde';
8563:Agathias IV, 24, arm. Sagastan bei Sebeos 110, Mos.
8810:gulu *Kehle', zd. garah-; gulula 'Kugel* H. 929; gand 'Ge-
9541:mrf *tief' = zd. jafra- (aber zafar,
9542:zafr 'Kachen , das nicht urspr. persisch
10700:saugand 77.
=== CHEUNG gand ===
```


## [2026-09-06T14:54:04.700Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('HUB.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor target in [6520,8810,9541]:\n    i=target-1\n    idx=sum(len(x)+1 for x in lines[:i])\n    leaf=t[:idx].count('\\f')\n    print('### line',target,'leaf',leaf,'printed',leaf-10)\n    print('\\n'.join(lines[i-4:i+7]))\nEOF"
}
```


## [2026-09-06T14:54:05.888Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== CHEUNG ===\"; grep -n -i \"gand-\\|ganti\\|jafra\\|zofr\" CHEUNG.txt | head -20; echo \"=== SOD gnc ===\"; grep -n \"gnc\" SOD_pages.txt | head -20"
}
```


### [2026-09-06T14:54:07.042Z] TOOL RESULT

```
### line 6520 leaf 194 printed 184
echt pers. dahan = zd. zafan-) = zd. zafar- von iran. zaf-
(= ar. g^aph) neben skr. jabh *schnappen nach* (idg. ghmbh,
g^fpbh), vgl. np. zav *Spalt, Riss .
d) Wie hier ph und bh, so wechselten auch p und bh
in: zd. gafya- *Tiefe*, jafra- *tief, jqfnu- 'Tiefe von arisch
gap, jap neben zd. jaiwi- *tief (das fiir jafra- in Komp.
eintritt, vgl. KZ. 31, 266), skr. gabhlrd-j gambhird- 'tief von
arisch gabh, jabh (idg. g^embh, g'^fphh) ; gusuftan 'zerstreuen*,
paz. 3. pr. vasGved zerstort' ^ phi. v(i)sopet Phi. Min. p. 37,
Z. 7; Gl. and Ind. 245 von iran. vi-xsup^) neben skr. m-
'ksubh ; Osuftan Verwirrt werden', (isdb *Verwirrung' = phi.
### line 8810 leaf 256 printed 246
garenU' (?) ; giran *schwer H. 898 ; giriftan ergreifen , girav
'Pfand', ap. grh, skr. grabh; girtstan *weinen, oben p. 93
garm 'warm' — zd. garenia-; gire 'Hals' -- zd. grwd-
guftan *sprechen', ap. gaub-; gila 'Klage = zd. gereza-
gulu *Kehle', zd. garah-; gulula 'Kugel* H. 929; gand 'Ge-
stank', zd. gainti-; gandum 'Weizen, skr. godhuma-; gunda
'Hefenballen', zd. gunda-; gos 'Ohr ^= ap. gausa-; gun
'Farbe* == zd. gaona-; guh 'Sehmutz, Koth* = zd. guda-;
gohar 'Ursprung H. 948, oben p. 96; ges^ gesU 'Locken\
zd. ga^sa-; gehan *Welt* = zd. gaedanqm (gen.pl.); angust
'Finger, Zehe' = zd. angiista-; angist 'Kohle', vgl. skr. an-
### line 9541 leaf 276 printed 266
arm. Balx, Balh (Faust us), Bald
(Mos. Chor. u. s. w.), phi. JSa/x- Bdh.,
Baxr vd. 1, 22, ap. Baxtri- (zd. baxdi-),
c) Ap. /r ~ np. rf: barf *Schnee* = phi. i;a/*r = zd. y«/n/- ;
mrf *tief' = zd. jafra- (aber zafar,
zafr 'Kachen , das nicht urspr. persisch
ist (§ 111) = zd. zafar-).
d) Ap. sr = np. rs : ars 'Thrane' = zd. asm- (aber inlautend
sr : xusrfij Xusrav u. s. w.).
o) Ap. zr = np. rz : ffurz, gurza *Keule' = mand. NnTi;i, phi.
vazr, paz. vazra ZDMG. 43, 38 Anm.,
```


### [2026-09-06T14:54:07.097Z] TOOL RESULT

```
=== CHEUNG ===
4537:form, clay’ (with assim.), Goth. digand- (pres.) ‘kneading’, Gr. teixog (n.) ‘wall’, 
7608:*AVESTAN: YAv. ganti- (f) ‘bad smell’ (V 7.56), YAv. duz-gainti- ‘smelling badly’ 
33428:ganti-, 103 
53400:digand-, 53 
=== SOD gnc ===
```


## [2026-09-06T14:54:14.990Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '7590,7640p' CHEUNG.txt"
}
```


### [2026-09-06T14:54:15.031Z] TOOL RESULT

```
9 In several modern languages and dialects, a stem gen-, gin-, etc. is found. This 
verbal stem has hitherto no known etymology, cf. Eilers, WIM I: 68 and WIM III: 
107, fn. 22. It is perhaps a denominative form of *gana-, the nominal derivative of 
*jan. This derivative is often used in impersonal constructions. In the Zazaki dialects 
of Siwerek and Kor, the original meaning may be found. For the semantics compare 
the usages of Engl. to strike (as in struck with terror, to strike upon an idea, vel 
sim.). 

«PIE *g”"ono- ‘slaying’ > LIV: - | Pok.: 491 f. 

*IE COGNATES: Gr. gó vog ‘murder’, Arm. gan ‘strike’, Russ. gon ‘hunt’ 

*REFERENCES: KPF I: 82a, 207a, 247a f.; KPF IV: 116, 255; MacKenzie 1966: 114; Abaev, Slovar’ II: 
290 Е; WIMI: 68; WIMII/1: 87; DKS: 38b; Safari 1373: 68, 229; Lecoq 2002: 162 


* gant ‘to smell badly, stink’ 

*AVESTAN: YAv. ganti- (f) ‘bad smell’ (V 7.56), YAv. duz-gainti- ‘smelling badly’ 
(H 2.25) 

*OLD PERSIAN: gasta- <g-s-t-a> (ppp.) ‘evil, repugnant’ = Kent: 183b 

*MIDDLE PERSIAN: MMP gngyy ‘stench’, BMP gndk(-) /gandag(-)/ ‘stench, stinking’ 
c DMMPP: 163a 

*PARTHIAN: gnd'g ‘stinking, smelling’, gst (old ppp.) ‘loathsome, disgusting’ 
c DMMPP: 163a 

*SOGDIAN: CSogd. ynt ‘stench’, SSogd. ynt'kw, BSogd. ynt’’k, ynt'k, CSogd. ynt'q 
“bad, evil’ || (+ *a-) BSogd. ’’y’ynt- (caus.) ‘to defile’ 

(+ *à-) Pres.: IND. 3sg. ’’y’ynt (Dhu. 127(N), SCE 180(N)) 


104 *garl 


*NWIR: Kurd. ganin/gan- ‘to rot’, NP gand ‘stench’, NP gandah ‘fetid, stinking, 
rotten; filthy, dirty’, Bal. gandag ‘bad’, Kurd. gani ‘rotting; stinking’, (orig. ppp.) 
Siv. gäs(s) ‘bad’ 

*NEIR: Pash. yandol ‘to dislike’ (+ *pari-) Oss. D. feelgandun/faelgzst ‘to smear; 
paint’ (+ *ui-) Oss. D. igaendun/igest ‘to smell; defile, desacrate’, Oss. I. gast, D. 
iğæstæ ‘desacration by something contagious or poisonous; desacrated’ 

*MISC: ? Par. ges ‘bad, sinful’, Orm. yanj ‘bad’ (< Pash. or other Ir. language ?) 
*SANSKRIT: gandh ‘to smell’ (RV+) = EWAia I: 461 

© The Ir. root *gant- (and Skt. gandh-) can hardly be of IE origin. The IE 
correspondences, notably Gr. ö£vvog (m.) ‘blame, reproach’ and @@dvoc (m.)
```


## [2026-09-06T14:54:16.169Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SOD files ===\"; ls -la SOD*; echo \"=== search bad smelling ===\"; grep -n \"bad smell\\|stink\\|stench\" SOD_pages.txt | head -20; echo \"=== gn c ===\"; grep -n \"^[0-9]* *gn\" SOD_pages.txt | head -20"
}
```


### [2026-09-06T14:54:16.247Z] TOOL RESULT

```
=== SOD files ===
-rw-rw-r-- 1 sfmqrb sfmqrb 3741182 Sep  4 14:06 SOD_pages.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1845041 Sep  4 14:06 SOD.txt
=== search bad smelling ===
15492: 4125 ync(h) B                                    J*fj*              stinking
15495:      bad smelling                                                    SCE 287; GMS 435, 496
15547:      stench =»ynsl                                                           BSTBL, Intox. 9
15922:4270 yrtr'k B                                           j&          stinking
27752:     GMS 119                                                          (fl)stinking insect
37659:  10345                                     at each step 6839                       bad smelling 4125
39529: stench      4147                             4166                                  suitable 254, 1082*1085, 1086,
39543: stinking 4138, 4282                        (to)stumble   2638                     sunlight 4417, 4502, 10764
39544: (a)stinking insect     8341                stumbling block    3998                sunset   10771
=== gn c ===
13888:                                                                      gnashingG?/ teeth)
30322:     gnashing                                                9221 sk*yr-      B                       jj&^J^j < jjiiJUs
```


## [2026-09-06T14:54:26.934Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '7640,7660p' CHEUNG.txt; echo \"=== SOD entry ===\"; sed -n '15480,15500p' SOD_pages.txt; echo \"=== page tag ===\"; awk 'NR<=15500 && /\\[pdf page/ {p=$0} END{print p}' SOD_pages.txt"
}
```


### [2026-09-06T14:54:29.668Z] TOOL RESULT

```
correspondences, notably Gr. ö£vvog (m.) ‘blame, reproach’ and @@dvoc (m.) 
‘envy’, are not compelling. The strange dental "alternation" in the Skt. and Ir. roots 
points to borrowing. 

*PIE — = LIV: — | Pok.: 466 f. 


“IE COGNATES: — 
REFERENCES: Horn 1893: 208; EVP: 26; IIFL I: 254b, 396a; Abaev, Slovar’ I: 542; Nyberg П: 81; 
Abaev, Slovar’ II: 297 f.; DKS: 79a; WIM III: 313 f.; Cabolov 2001: 368 f. 


*gar! ‘to rejoice’ 

*KHOTANESE: (+ *fra-) hayár- ‘to rejoice, be happy’. Ф The reconstructions and 
inherent etymology cited in SGS, Le, are all unconvincing. = SGS: 148 
*CHORESMIAN: m/yry- ‘to rejoice’, m/yw’ry- (caus.) ‘to let rejoice? > Samadi: 80 
*NWIR: ? NP zar ‘wish’ (nonce ?) 

*SANSKRIT: har ‘to be glad, enjoy, like’ (RV+) = EWAia II: 804 

=== SOD entry ===
      ynaPat ©pt. inf.
                                                                 4136 ynpn(h)    B, S                         j& tj±j>.
      (/^lament
      VJ 1120                                                         yamban,pain
                                                                      effort,  yanpan =»ymbn, ympn, ynp'wnh

 4124 yn'pSV- S            f                    fr/«J                 TSP 9.130 n p222; Hen. Talcs. 486.3; KG 384,
      ynaf3dar- ©trans. pret.; lsg. impf. Yn'flw                        484; MSP bl05
      0o)larncnt
                                                                4137 ynpwn =» ynp'wnh
      Mack. AI 25,422, 19.28
                                                                4138 yns1 B                                      JLuai^
 4125 ync(h) B                                    J*fj*              stinking
                                                                     yans ©nom. -y -»ynt\ ysn
      vane ©<Av. gainti ©f. adj.
      bad smelling                                                    SCE 287; GMS 435, 496
      TSP 2,636, 712, 793
                                                                4139 yns: B, S                                 Jy^*^
                                                                     xans ~»xns, xs
4126 ynd'k M                   (tjJ' <jjf)^jcxX^x                    stable, strong
     yandak ©Parth. gnd'g «*ynt>k(,), ynt»kC)>
=== page tag ===
```


## [2026-09-06T14:54:35.792Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\ni=15491\nidx=sum(len(x)+1 for x in lines[:i])\nleaf=t[:idx].count('\\f')\nprint('leaf',leaf,'printed approx',leaf-66)\nEOF\ngrep -n \"\\[pdf page\" SOD_pages.txt | head -3"
}
```


## [2026-09-06T14:54:37.560Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD quabbeln/quaver ===\"; grep -n -i \"quabbeln\\|gweb\\|quaver\\|quiver\" AHD_watkins1985.txt | head -20; echo \"=== AHD baptein/gwabh ===\"; grep -n -i \"baptein\\|bapt\" AHD_watkins1985.txt | head -10"
}
```


### [2026-09-06T14:54:38.136Z] TOOL RESULT

```
leaf 229 printed approx 163
```


### [2026-09-06T14:54:38.209Z] TOOL RESULT

```
=== AHD quabbeln/quaver ===
408:[dud-. To shake, deceive. Germanic root. 1. Norwegian dudra, to quiver, akin to: a. Middle English daderen, to tremble: DODDER!; b. Middle English doder, vine (< “that which quivers in the wind”): DODDER2. 2. Middle English doten, to be foolish: DOTE. [In Pok. 4. dheu- 261.]]
540:(COVEN), (COVENANT), EVENT, INTERVENE, INVENT, MIS- ADVENTURE, PARVENU, PREVENIENT, PREVENT, PROV- ENANCE, (PROVENIENCE), REVENANT, REVENUE, SOUVENIR, SUBVENTION, SUPERVENE. 3. Suffixed zero-grade form *gvm-yo- in Greek bainein, to go, walk, step, with basis (< *gm-ti-), a stepping, tread, base, and -batés (< *gwa-to-, zero-grade of gd-, contraction of *gaa-), agential suffix, “one that goes or treads, one that is based”: BASE!, BASIS; ABASIA, ACROBAT, ADIABATIC, AMPHISBAENA, ANABAENA, DIABASE, DIABETES, STEREO- BATE, STYLOBATE. 4, Suffixed zero-grade form “g“(g)-u- in compound form “pres-gu-, “going before” (see per’). 5. Basic form *gvd- in Greek béma, step, seat, raised platform: BEMA. 6. Sanskrit jigdti, he goes: JUGGER- NAUT. [Pok. g¥d- 463.] gvadh-. To sink. Possible root. 1. Suffixed form *guadh-u- in Greek bathus, deep (> bathos, depth): BATHOS, BATHY-. 2. Greek benthos, depth, may be formed on bathus by analogy with penthos, grief, and pathos, passion, suffering (or it may be from an unrelated root *g¥(e)ndh-): BENTHOS. 3. Suffixed variant form *gudh-yo- in Greek bussos, bottom of the sea: ABYSS. [Pok. gddh- 465.] g’ébh-'. To dip, sink. Suffixed zero-grade form *gvabh-yo- in Greek baptein, to dip: (BAPTIST), BAPTIZE; ANABAPTIST. [Pok. g¥ébh- 465.] g”ébh-2. Hypothetical base of some Germanic words associated with the notion of sliminess. 1. Middle Dutch quac-, unguent, liquid, in obsolete Dutch quacksalver, quacksalver: QUACKSALVER. 2. Low German quabbeln, to shake like jelly, tremble, akin to Middle English quaven, to tremble: QUAVER. [Pok. 2. g¥ébh- 466.] grei-. Also gveia-. To live. I. Suffixed zero-grade form *gwi-wo-, *gi-wo- (< *gi9-wo-), living. 1. Germanic *kwi(k)waz in: a. Old English cwic, cwicu, living, alive: QUICK, QUICKSILVER; b. as a name for couch grass (from its rapid growth), in Old English cwice, couch grass: (COUCH GRASS), QUITCH GRASS. 2. a. Latin vivus, living, alive: VIVIFY, VIVIPAROUS; b. Latin denominative vivere, to live: VIAND, VICTUAL, VIVA, VIVACIOUS, VIVID; CON- VIVIAL, REVIVE, SURVIVE. 3. Further suffixed form *gvi- wo-td in Latin vita, life: VIABLE, VITAL; LIGNUM VITAE, VITAMIN. II. Suffixed zero-grade form *gia-o- in Greek bios, life (> bioté, way of life): BIO-, BIOTA, BIOTIC; AEROBE, AMPHIBIOUS, ANABIOSIS, CENOBITE, MICROBE, RHIZOBIUM, SAPROBE, SYMBIOSIS. III. Variant form *gwyd- (< *gvyoo-). 1. Greek z0é, life: AzO-, (DIAZO). 2. Suffixed form *gvy6-yo- in Greek zdon, zdion, living being, animal: (-Z0A), -ZOIC, ZOO-, ZOON, -ZOON. IV. Pre- fixed and suffixed form *su-g~ia-es- (*su-, well; see su-), “living in good condition,” in Greek hugiés, healthy: HYGEIA, HYGIENE. [Pok. 3. gei- 467.] g”eia-. To press down, conquer. Sanskrit jayati, he con- quers: JAIN. [Pok. gveio- 469.] gvel-'. To pierce. 1. Suffixed o-grade form “gvol-eyo- in Germanic *kwaljan in Old English cwellan, to kill, destroy: QUELL. 2. Suffixed zero-grade form *g“/-yo- in Germanic *ku/jan in Old English *cyllan, to kill, perhaps the source of Middle English killen, to kill: KILL}. 3. Full-grade form *gvel- in Greek beloné, needle: BEL- ONEPHOBIA. [Pok. 1. g¥el- 470.] gel-2. To fly; a wing. Possibly in Latin voldre, to fly: VOLANT, VOLATILE, VOLE2, VOLITANT, VOLLEY. gvel-3, To swallow. Dissimilated to *gel-. 1. Germanic *kel- in Old English ceolu, throat, dewlap, perhaps akin to Middle English cholle, throat: JowL?. 2. Germanic *keluz in Old Norse Aj6ir, keel: KEEL}. 3. Suffixed zero-grade form “gul-d in Latin gula, gullet, throat, palate: GOLIARD, GULAR, GULES, GULLET. 4, Extended (expressive) form *glutt- in: a. Latin gluttire, gliitire, to swallow: GLUT; DEGLUTITION; b. Latin glutté, a glutton: GLuTTon. [In Pok. 2. gel- 365.] gvelbh-. Womb. 1. Suffixed form *gvelbh-u- in Greek delphus, womb, whence delphis, dolphin (referring to its
946:skot-. Dark, shade 1. Suffixed form *skot-wo- in Ger- manic *skadwaz in Old English sceadu, shade: SHADE, SHADOW. 2. Suffixed form *skot-o- in Greek skotos, darkness: scoToMa. [Pok. skot- 957.] skreu-. To cut; cutting tool. Extension of sker-'. 1. Basic form *skreu- in: a. Germanic *skraw- in Old English scréawa, shrew (having a pointed snout): SHREW, (SHREWD); b. Germanic *skraud- in Old English scréade, piece, fragment: SCREED, SHRED; C. Germanic *skrid- in (i) Old English scriid, garment (< “piece of cloth”): SHROUD (ii) Old French escro(uje, scroll: SCROLL (iii) Dutch schrood, a slice, shred: scRop. 2. Extended form “skreut- in Latin scriita, trash, frippery: SCRUTINY. 3. Extended variant form ‘*skraut- in Latin scrétum, scrotum (probably identified with scrautum, leather quiver for arrows): SCROTUM. [Pok. 4. (s)ker-, Section ITI. 947.]
2147:QUASI kWo-, swo- QUATERNARY kWetwer- QUATERNION kWetwer- QUATRAIN kwetwer- QUATROCENTO dekm QUATTROCENTO kWetwer- QUAVER gWébh-2 quay kagh-
=== AHD baptein/gwabh ===
540:(COVEN), (COVENANT), EVENT, INTERVENE, INVENT, MIS- ADVENTURE, PARVENU, PREVENIENT, PREVENT, PROV- ENANCE, (PROVENIENCE), REVENANT, REVENUE, SOUVENIR, SUBVENTION, SUPERVENE. 3. Suffixed zero-grade form *gvm-yo- in Greek bainein, to go, walk, step, with basis (< *gm-ti-), a stepping, tread, base, and -batés (< *gwa-to-, zero-grade of gd-, contraction of *gaa-), agential suffix, “one that goes or treads, one that is based”: BASE!, BASIS; ABASIA, ACROBAT, ADIABATIC, AMPHISBAENA, ANABAENA, DIABASE, DIABETES, STEREO- BATE, STYLOBATE. 4, Suffixed zero-grade form “g“(g)-u- in compound form “pres-gu-, “going before” (see per’). 5. Basic form *gvd- in Greek béma, step, seat, raised platform: BEMA. 6. Sanskrit jigdti, he goes: JUGGER- NAUT. [Pok. g¥d- 463.] gvadh-. To sink. Possible root. 1. Suffixed form *guadh-u- in Greek bathus, deep (> bathos, depth): BATHOS, BATHY-. 2. Greek benthos, depth, may be formed on bathus by analogy with penthos, grief, and pathos, passion, suffering (or it may be from an unrelated root *g¥(e)ndh-): BENTHOS. 3. Suffixed variant form *gudh-yo- in Greek bussos, bottom of the sea: ABYSS. [Pok. gddh- 465.] g’ébh-'. To dip, sink. Suffixed zero-grade form *gvabh-yo- in Greek baptein, to dip: (BAPTIST), BAPTIZE; ANABAPTIST. [Pok. g¥ébh- 465.] g”ébh-2. Hypothetical base of some Germanic words associated with the notion of sliminess. 1. Middle Dutch quac-, unguent, liquid, in obsolete Dutch quacksalver, quacksalver: QUACKSALVER. 2. Low German quabbeln, to shake like jelly, tremble, akin to Middle English quaven, to tremble: QUAVER. [Pok. 2. g¥ébh- 466.] grei-. Also gveia-. To live. I. Suffixed zero-grade form *gwi-wo-, *gi-wo- (< *gi9-wo-), living. 1. Germanic *kwi(k)waz in: a. Old English cwic, cwicu, living, alive: QUICK, QUICKSILVER; b. as a name for couch grass (from its rapid growth), in Old English cwice, couch grass: (COUCH GRASS), QUITCH GRASS. 2. a. Latin vivus, living, alive: VIVIFY, VIVIPAROUS; b. Latin denominative vivere, to live: VIAND, VICTUAL, VIVA, VIVACIOUS, VIVID; CON- VIVIAL, REVIVE, SURVIVE. 3. Further suffixed form *gvi- wo-td in Latin vita, life: VIABLE, VITAL; LIGNUM VITAE, VITAMIN. II. Suffixed zero-grade form *gia-o- in Greek bios, life (> bioté, way of life): BIO-, BIOTA, BIOTIC; AEROBE, AMPHIBIOUS, ANABIOSIS, CENOBITE, MICROBE, RHIZOBIUM, SAPROBE, SYMBIOSIS. III. Variant form *gwyd- (< *gvyoo-). 1. Greek z0é, life: AzO-, (DIAZO). 2. Suffixed form *gvy6-yo- in Greek zdon, zdion, living being, animal: (-Z0A), -ZOIC, ZOO-, ZOON, -ZOON. IV. Pre- fixed and suffixed form *su-g~ia-es- (*su-, well; see su-), “living in good condition,” in Greek hugiés, healthy: HYGEIA, HYGIENE. [Pok. 3. gei- 467.] g”eia-. To press down, conquer. Sanskrit jayati, he con- quers: JAIN. [Pok. gveio- 469.] gvel-'. To pierce. 1. Suffixed o-grade form “gvol-eyo- in Germanic *kwaljan in Old English cwellan, to kill, destroy: QUELL. 2. Suffixed zero-grade form *g“/-yo- in Germanic *ku/jan in Old English *cyllan, to kill, perhaps the source of Middle English killen, to kill: KILL}. 3. Full-grade form *gvel- in Greek beloné, needle: BEL- ONEPHOBIA. [Pok. 1. g¥el- 470.] gel-2. To fly; a wing. Possibly in Latin voldre, to fly: VOLANT, VOLATILE, VOLE2, VOLITANT, VOLLEY. gvel-3, To swallow. Dissimilated to *gel-. 1. Germanic *kel- in Old English ceolu, throat, dewlap, perhaps akin to Middle English cholle, throat: JowL?. 2. Germanic *keluz in Old Norse Aj6ir, keel: KEEL}. 3. Suffixed zero-grade form “gul-d in Latin gula, gullet, throat, palate: GOLIARD, GULAR, GULES, GULLET. 4, Extended (expressive) form *glutt- in: a. Latin gluttire, gliitire, to swallow: GLUT; DEGLUTITION; b. Latin glutté, a glutton: GLuTTon. [In Pok. 2. gel- 365.] gvelbh-. Womb. 1. Suffixed form *gvelbh-u- in Greek delphus, womb, whence delphis, dolphin (referring to its
1242:ANA- an! ANABAENA gWa- ANABAPTIST g¥ébh-1 ANABIOSIS gWei- ANACOLUTHON sem-! ANACRUSIS kreue-2 ANADEM dé- ANADIPLOSIS dwo- ANADROMOUS der-1 ANAGLYPH gleubh- ANAGOGE ag- ANALCIME = alek- ANALECTS leg-1 ANALEPTIC (s)lag¥- ANALOGOUS leg-! ANALYSIS leu-1 ANAMNESIS men-1 ANAPEST peu- ANAPHORA bher-? ANARTHROUS ar- ANASARCA twerk- ANASTOMOSIS ste-men- ANASTROPHE  streb(h)- ANATHEMA dhé-1 ANATOMY tem- ANCESTOR ked- ANCHOR ank- ANCHORITE ghé- ANCIENT! ant- ANCILLARY kWel-1 ANCON ank-
1276:BABA baba- BABBLE baba- BABE baba- BABKA baba- BABU baba- BABUSHKA baba- BABY baba- BACILLUS bak- BACTERIUM bak- BACULIFORM bak- BAGEL bheug-3 BAGUETTE bak- Bails bheug-3 BAIRN bher-1 BaIT! bheid- BAKE bhé- BAKSHEESH bhag-' BALALAIKA baba- BALCONY bhelg- BALE! bhel-2 BALE? bhelu- BALEEN bhel-2 BALK bhelg- BALL! bhel-2 BALL2 gWele-1 BALLAD gWele-1 BALLAST bhoso-, kla- BALLET gWela-1 BALLISTA gWele-1 BALLOON bhel-2 BALLOT bhel-2 BALLOTTEMENT bhel-2 BAMBINO _baba- BAN! bha-2 BANAL bha-2 BAND! bhendh- BANDANNA bhendh- BANDIT bha-2 BANDOLEER bha-1 BANDORE pandoura BANE gWhen-1 BANG! bheg- BANIAN wen-1 BANISH bha-2 BANK! bheg- BANK? bheg- BANK? bheg- BANKRUPT bheg-, reup- BANNER bha-! BANNERET bha-1 BANNS bha-? BANQUET bheg- BANQUETTE bheg- BANSHEE gWen- BANTLING bheg- Baptist gébh-!
1278:BAPTIZE gWébh-1 BAR? gWere-2 BARB! bhardha BARBARIAN baba- BARBARISM baba- BARBAROUS_ baba- BARBEL bhardha BARBELLATE bhardha BARBER bhardha BARBETTE bhardha BARBICEL bhardha BARBULE bhardha BARD! gWera-3 BARE! bhoso- BARGAIN bhergh-? BARITE gWera-2 BARITONE gWera-2 BARIUM gWera-2 BARK! bherg- BARLEY bhares- BARM_ Dbhreu-2 BARMY bhreu-2 BARN bhares- BARO- gWera-2 BAROUCHE dwo-, ret- BARROW! bher-1 BARROW? bhergh-2 BARROW’ = bher-2 BARYON gWere-2 BARYSPHERE gWere-2 BARYTA gWere-2 BASCULE (s)keu- BASE! gWa- BASE? bassus BASIS gWa- BAS-RELIEF bassus Bass! bhar- Bass? bassus BASSET! bassus BASSO bassus BAT? bhiag- BATE? battuere BATEAU bheid- BATH! bhé- BATHE bhé- BATHOS gWadh- BATHY- gWadh- BATHYSCAPH skep- BATTEN! bhad- BATTERY battuere BATTER! battuere BATTER’ battuere BATTLE battuere BAWD bhel-2 BAWL bhel-4 Bay? bat-
```


## [2026-09-06T14:54:50.727Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -o \"QUIVER[^ ]* [a-zA-Z¥ẃgWébh0-9-]*\" AHD_watkins1985.txt | head; echo \"---KLN quaver/quiver/Baptist---\"; grep -n -i \"^quaver\\|quaver (v\\|quiver, adj\\|quiver, tr\\|quiver, intr\\|Baptist, n\" KLN_1971.txt | head -20"
}
```


### [2026-09-06T14:54:50.802Z] TOOL RESULT

```
---KLN quaver/quiver/Baptist---
13923:Anabaptist, n. — ModL. anabaptista , ‘one who 
25802:baptist, n. — OF. (= F.) baptiste , fr. Eccles. L. 
67349:quaver’. See demi- and semiquaver, 
197984:quaver, intr. and tr. v. — ME. quaver en, freq. of 
198698:quiver, intr. v., to tremble; tr. v., to cause to 
252367:tremere , ‘to shiver, quiver, tremble’, fr. I.-E.
```


## [2026-09-06T14:54:53.500Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '197984,197996p;198698,198712p;25802,25812p' KLN_1971.txt"
}
```


### [2026-09-06T14:54:53.567Z] TOOL RESULT

```
baptist, n. — OF. (= F.) baptiste , fr. Eccles. L. 
baptista , fr. Gk. (Ja7maT7)<;, ‘one who dips’. See 
baptism and -ist. 

baptistery, baptistiy, n. — OF. baptisterie (F. bap- 
tist tre), fr. Eccles. L. baptisterium, fr. Gk. pait- 
Twrrijptov, ‘bathing place’, in Eccles. Gk., bap- 
tistery’. See baptist and -ery, resp. -ry. 
baptize, tr. and intr. v. — ME. baptisen , fr. F. 
baptiser , fr. Eccles. L. baptizdrc , ‘to baptize’, fr. 
Gk. PaTrr^etv. See baptism and -ize, 
quaver, intr. and tr. v. — ME. quaver en, freq. of 
quaven, which is prob. of imitative origin. Cp. 
LG. quappig , ‘puffy, swelled’, Du. kwabbig, 
‘flabby’, G. quabbeln, ‘to wobble, shake, quake’, 
which all are imitative. Cp. also quiver, v., 
squab. 

Derivatives: quaver , n., quaver-er , n., quaver- 
ing, verbal n., quaver-ing-ly , adv., quaver-y , adj. 
quay, n. — ME. kai, kei, fr. OF. chai (F. quai ), 
fr. Gaul, caio, ‘circumvallation’, which is rel. to 
W. cae , ‘fence, hedge’, Co. ke, ‘hedge’, fr. I.-E. 
base *quagh-, ‘to encompass, enclose’, whence 
quiver, intr. v., to tremble; tr. v., to cause to 
quiver. — A var. of quaver (q.v.) 

Derivatives: quiver, n., quiver-ing, adj. 

quiver, n., a case for holding arrows. — ME., fr. 
AF. quiveir , fr. OF. quivre (also cuivre, cue v re), 
which is prob. of Teut. origin. Cp. OHG. kochar, 
kochari, OE. cocur , cocer , ‘quiver’, and see 
cocker, ‘quiver’. 

qui vive, a sentinel’s challenge corresponding to
```


## [2026-09-06T14:54:55.645Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC ===\"; grep -n \"g'ebh\\|gʷebh\\|quabb\\|gabawo\\|zaba\\|Kröte\" IEC.txt | head -15; echo \"=== WLD band3 register ===\"; grep -n \"gabawo\\|quabbeln\\|jafra\" WLD_band3.txt incoming/WLD/WLD_Bd1_pages.txt 2>/dev/null | head -15"
}
```


### [2026-09-06T14:54:55.733Z] TOOL RESULT

```
=== IEC ===
2045:dakKru 'téardrop, droplet’. WP I, 769. (A rhyming influence is seen in the unrelated Skt. á$ru: Li. ašara *teardrop") Arm. artawsr, pl. artasuK; Gk. dákru; MIr. deór, dér; OBr. dacr-; W dagr; Br. daér; Cor. dager; OHG zabar, MHG zaher, zeher; Go. tagr; OE teagor, tear; ON tár, cpds. tárug-, id.
5094:Lat. (once) vabrum, adj. n. “varied?” beside (dial.) vafer *wily'; E quaver, s. & v. beside ME quavien ‘shake’; G cf. quabbeln ‘shake like a jelly
5918:ĉuhuos (£houos) “shout, call, appeal, impre- cation’. Cf. &uhuo, guhon- Skt. hū, adj. ‘calling’; juhū, jihva ‘tongue’; ` havah 'invocation' in Vedic; ‘sacrifice’ in Skt.; Av. zavō ‘call’; hizu, -áh-, n. and hizva, f. ‘tongue’; Ober, (alleged) izáva, id.; Oss. äv- zag, dim. type, id.; Per. cf. hazvan, zaban, id.; Arm. cf. n-zovK, gp. n-zovic (curse: Skt. ni- havah ‘invocation’; ni-hvaye invoke); Gk. Hes. cf. oló-phus or ol-óphus ‘mourning’; olo- phudnós, adj.; Mir cf. guth, pl. gothanna (“+ voice”. See next); Go. gaunópus ‘plaint’; OE géanobp, id.; MHG cf. guft ‘shout’; OCS züvü (cal, and com. Sl.); Cz. cf. ná-zev 'appella- tion’; Li. Zavai (charms, spells’; Zavüs *be- witching’
=== WLD band3 register ===
incoming/WLD/WLD_Bd1_pages.txt:63869:Grdr. d. iran. Phil. I 10;, jafrat-s ..Yertiefung, Einsenkung" (J. Schmidt
incoming/WLD/WLD_Bd1_pages.txt:63929:keit“, ndd. quabbeln „vor Fettigkeit zittern".            PreuB. gabawo „Krote'‘,
```


## [2026-09-06T14:55:02.575Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=63850 && NR<=63950' incoming/WLD/WLD_Bd1_pages.txt | head -80; echo \"=== page tags near ===\"; awk 'NR<=63940 && /\\[pdf page/ {p=NR\": \"$0} END{print p}' incoming/WLD/WLD_Bd1_pages.txt"
}
```


### [2026-09-06T14:55:04.646Z] TOOL RESULT

```
v            besonders fraglic.h);
         wegfiillt,
  anord. k vrfja fund kefja nach dem Praet. kof aus *krof) trans. ..nieder-
driicken. untertauchen, ersticken", kvef „Katarrh", kvafna intr. ..ersticken".
knf n. ..das Untertauchen, Schwimmen unter Wasser: Meer". aschw. kraf
„Tiefe", anord. kvcefo (idg. e!), kg fa trans. ..ersticken", mhd. crqueben ..er-
sticken" (= anord. kvcfju ) 2                        ).       S.   Fick BB. 2, 189.     Wb. I 4 33f., 196, 399,
Zupitza GG. 83.
  Eine vielleicht verwandte, aber nur die Bed. ,,tief" aufweisende Wz.
*yWrmbh-.            zeigt das Arische (wobei im ai. das   der Tiefstufe                       (j


oder o-Stufe                   durcbgeftihrt         ist.      gegeniiber av. j der e-Stufe)        :   ai.   gabhird-,
(jumbhlrd- „tief", tjumbht              yamhhdra- n. ,,Tiefe, Abgrund“, gabhd
                                                ;
                                                    ymibhan
m. ..vulva", jabh i-sak AY. adv. vielleicht ..tief unten oder innen", av. jaiwi-
vafra- Adj. ,.mit tiefem Schnee". jafni- „tief" fuber f = w s. Bartholomae
Grdr. d. iran. Phil. I 10;, jafrat-s ..Yertiefung, Einsenkung" (J. Schmidt
KZ. 25. 88. Bartholomae BB. 15. 10, (.'aland KZ. 31, 267 Anm. 2).
   Fernzuhalten ist ai. gillutle „tauchcn, eindringen" Ptc. qadha- s. auch                (
                                                                                                              ;



Wz. i/"adh-): ferner (gegen Scheftelowitz BB. 28, 301) arm. cov ,,Meer"
fsei            wie anord. kaf „Meer“; aber Palatalisierung vor a ist nicht
anzunehmen); endlich russ .gala ..Lippe" usw. (Uhlenbeck Ai. Wb. 77, der
der Wz. *(j“umbh- die Bed. ..klaffen" geben will: doch siehe dagegen Ber-
neker 34(1). Fick setzt die \Yz. *tfi ribh- an. was zur Annahme zwiinge, daB
anord. liviefn Ablautsneubildung sei.


 2. gliebfh)-              ..schleimig, schwabbelig,                   Quappe, Krote".
   Yermutl. letzlich                     onomatopoetiscli (Weise ZfdWf. 3, 231); doch
                                                                  ist mit

 der Moglichkeit zu rechnen. daB ein altes Wort fur Frosch erst im Germ,
 in die laufmalende Sippe hineingezogen wurde.
    And. ijiin/ijiii quappui qnajipo „Aalquappe" (mit bei lautmalenden Worten
                               ,            ,

 haufiger Konsonantengemination),      mhd. quappe, quape kobe, nhd. Quappe.              ,


 holl. kwnb, hr       Quappe. Kropf,                               W
                                        amine", isl. kvup, kvttpi ..Gallert oder
 gallertartigeDingo", norw. rndartl. kvabb, \p)kvrq> ..breiartige schleimige
 Masse", schw. dial. a'jlvdhb ..etwas Dickes, Fettes", (s)kvehba „feiste Frau",
 mnd. qnabhr ..Bebemoos. Scblamm", engl. rjuah „Morast". quaver ..zittern,
 vibriereir  Dazu das Yerb norw. dial, kmpa „cine Fliissigkeit aussendon".
                       .




          ')   Gegen J<iculi~ohii' Ws. ", 10s Verbindunff yiq f<jn
                                                               lat. ribnt ..Balken" «pricht die
                                                                                    :




    alter?  Bed. ..Datum” Kretschmer Gl. 4. 34S'. Prellwitz KZ. 47. 208 will in den gi.
                                     i




    Woiten cine Rcd.-Bilduug inaeh \rt von ved. jobhunt von bharoti) ^elien and als die
    tragende. lit.       deuteiiV't
       -) Mnd. qua ’hi’ ..Snmpf*.
                           1        mnd. o-tpreufi (piebhc gelioit in andern Zusammenhang,
    s.   mitei    2.
                                              guem-, gua-                              675

schw. dial. Ivabba „zittern, vor Pettigkeit quatschen", dan. dial, kvappe,
kvabe „eine breiartige Masse aussenden", Icvabbe „quatscheln vor Fettig-
keit“, ndd. quabbeln „vor Fettigkeit zittern".            PreuB. gabawo „Krote'‘,
=== page tags near ===
```


## [2026-09-06T14:55:10.880Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BQT v2 zarf ===\"; grep -n \"ژرف\" BQT_v2_pages.txt | head -20"
}
```


### [2026-09-06T14:55:10.941Z] TOOL RESULT

```
=== BQT v2 zarf ===
15210:                 ‫تابان مان گوهر اندر میان خوید‪.‬‬                   ‫بگفای چشم وژرف‌نگه کن بشنبلید‬
30171:                                                                   ‫رو فرن ِ = پروزن‌دور‪,‬ین» ژرفین‌در‬
31046:                                                                   ‫مکی ژرف دریاست بین ل‬
31048:   ‫« تارادیا ‪ ۲ : ۷۹۱‬از ‪ :‬ژرف ‪( ۱ 4‬حاصل مصدر) چون‪:‬یپناه‬                 ‫‪- ۴‬بهلوی ‪61‬‬
31050:   ‫«روستای‌وی (ارغان) چاهی آبستکه ژرفی آن همه جهان‌شواند داست * هحدود‬
33524:                ‫‪ _ ۸‬از ‪ :‬ستبر («‪.‬م‪ - ).‬بای (= با‪,‬یوند اسم مصنر همجو حرازنا ‪,‬ژرفنا) ‪.‬‬
```


## [2026-09-06T14:55:11.948Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON gast ===\"; grep -n \"گست\" MON_part1.txt MON_part2.txt | head -10; echo \"=== BQT v4 gand ===\"; grep -n \"گند\" incoming/BQT/BQT_v4_pages.txt | head -10"
}
```


### [2026-09-06T14:55:12.028Z] TOOL RESULT

```
=== MON gast ===
MON_part2.txt:1439:گستاخ» مغرور» مشک 
MON_part2.txt:4080:جسوره گستاخ. 
MON_part2.txt:4672:برگ‌های سبز را بالای سینی گستر ده؛ چند تا 
MON_part2.txt:5487:فق. تکفا پهناور» گسترده. سار فراوان. 
MON_part2.txt:5780:معلوم کردن. آموختن؛ یاد گرفتن. گسترش 
MON_part2.txt:5781:بافتن؛ گستر ده 4 ۳ و گرگ عادت کر دن. 
MON_part2.txt:7074:فرهنگستان اینران نام آن ر یه وزارت 
MON_part2.txt:7082:فرهنگستان 
MON_part2.txt:7091:فرهنگستان: 0 [آمکتب؛ مدرسه] 
MON_part2.txt:9845:آنجه بتوان آن را وسعت داد» گسترش پذیر. 
=== BQT v4 gand ===
7915:و همچنین چوب خوشة گندم را تیز(۲) و بعربی | فخی کردن ومباهات نمودن باشد ‏
8734:آن تودساله عجوز(عجوزی) گند هکس لی(نه) خرد هشت آن‌ماكرا-ونه «س.
9478:پیداست؛ وفل * لفط » درعریی بمعلی پراگنده شد وخارج شده آمده ومبدل آن « لبط » است
9823:نگزده ۴ « بفتح‌اول وثانی‌وسکون زای تگندن - یکسر اول بروژن فکندن ّ
9846:۷ -رك : گنده . ۸« اللذان ‏ رشتةٌ نکنده» «الامی فی‌الاسامی ص 4۳>.
9851:(ص بز) نویسد : ۸« نگنده - نگندن - موْلف این لفت را بمنی دوعی ا زکو رکردن با چال کردن
9854:بکشت. پایهابربالا وتابسینه بزمین‌درنگنده» - بازجای دیگر کوید: « بیست وسوم این‌ما. قرمطی
9855:در مکه رفت وبمیاری ازملءانان بکشت وچاه زمزم را ا زکشته پر کرد تا بگندرید وسدهز ا رکشته
9856:پیرامن کمبه افکنده بود , چون قرامطه برفتند و(کذا ) ایشان را همانجا بنگندند » (ص ۳۷۵)
9913:« دفن » را به « نگندن » ترجمه کرده است وبنظرحقیرباستی این لغت باکاق فارسی باشدچنانکه
```


## [2026-09-06T14:55:18.078Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR<=31060 && /\\[pdf page/ {p=NR\": \"$0} END{print p}' BQT_v2_pages.txt; echo \"--- context ---\"; sed -n '31030,31060p' BQT_v2_pages.txt"
}
```


### [2026-09-06T14:55:19.679Z] TOOL RESULT

```
--- context ---
               ‫ژغاله ‪۱‬و=زبر‬           ‫>‬   ‫‪۵‬‬

                                                       ‫بروزن کناره ‪ .‬بان‬         ‫شر‬
                                                                                              ‫‪°‬‬   ‫‪۵‬‬




  ‫»ردی ‪ , ۲6102‬زازا ‪,[10‬‬
                       ‫‪ ۳18.‬ک‬‫ا‪-‬وستا ‪( 8]12012-‬عمیق) ‪ .‬پهلوی ‪2 2 ۲۵‬‬
   ‫‪۰‬یلکی‬‫* پلوچی انا و انز « اسدق‪ .» ۵۸۱‬استی ‪ 172‬دك ‪ .‬امت ‪ ۷۰۱‬ک‬   ‫افتانی ت‬
  ‫‪۰‬ازند‬
      ‫(هلوی ) ‪ ( ۷۳772‬عمق ) پ‬
                            ‫‪( [0‬کود) » دامغانی ‪( [10‬کاة کود)‪ .‬دراوراق مانوی ب‬
           ‫ر‪:‬هنینگه‪ .‬فپرست لفات پارسی میانه ‪, 50051 ,...‬ج ×‪.1, 1‬س ‪۰٩‬‏ ‪:‬‬                               ‫‪6‬‬
             ‫در گنج رازی ددارد کلید‬                             ‫داند‬
                                                                   ‫مکی ژرف دریاست بین ل‬
  ‫فردوسی طوسی‪ « .‬لفت نامه * ‪.‬‬
   ‫« تارادیا ‪ ۲ : ۷۹۱‬از ‪ :‬ژرف ‪( ۱ 4‬حاصل مصدر) چون‪:‬یپناه‬                 ‫‪- ۴‬بهلوی ‪61‬‬
         ‫‪ -‬از '‪-‬زیرف(نسبت)‬                    ‫‪ ۴‬از‪ :‬ژرق ‪ +‬ی (حاصل‌مصدر) ‪.‬‬                   ‫درازاءستیرا‪.‬‬
   ‫«روستای‌وی (ارغان) چاهی آبستکه ژرفی آن همه جهان‌شواند داست * هحدود‬
                                                                    ‫® ‪ -‬ب‬
  ‫ژخار (ه م‪).‬ورك‪ :‬زعاره ‪:‬‬   ‫=‬   ‫‪۲‬‬             ‫زخار (ه م‪ ).‬‏ زغار («‪.‬م‪. ).‬‬    ‫=‬   ‫‪۹‬‬      ‫‪.‬‬     ‫نوا ‪۸۷‬‬
  ‫‪ (41 .‬هیچ‬      ‫]]‪۷‬‬    ‫‪(2212‬فر باد)و غبره (شمس فخری ص ‪۳٩‬‏ —‬                ‫ستاد هنینگه گوید و ‪۲7‬‬
   ‫سفدی‬      ‫لزم‬
               ‫ک ا‬
                 ‫همریشه در فارسی ندارد ‪ .‬ممکن است اسم سفدی ‪«۶ 74801812‬را بیذ مریم که‬
                                                      ‫‏‪( xzhghêr‬ناميدن ‪ 3‬را خواندن) ئاشی مود‬
  ‫‪Henning , Sogdian loan words..., BSOS‘X,1, p.‬‬                              ‫‏‪0 .‬‬
   ‫بزدم جنگه چه‌سازی» چه کنی‌بانگه(و)ژغار‪.‬‬                ‫بیکی زخم تیانچه که بدان روی کربه‬
  ‫ابوالمثل بخارى‪« .‬لغت فرس‪ ۱ ۲۲‬ورك ‪ :‬لفت نامه ‪.‬‬
```


## [2026-09-06T14:55:30.430Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport json\nd=json.load(open('../refs_online.json'))['BQT']\nprint(d.get('page_offset'))\nprint(d.get('lookup_hint'))\n\"; python3 - <<'EOF'\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\ni=31045\nidx=sum(len(x)+1 for x in lines[:i])\nprint('leaf',t[:idx].count('\\f'))\nEOF"
}
```


### [2026-09-06T14:55:32.631Z] TOOL RESULT

```
vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)
leaf 521
```


## [2026-09-06T14:55:41.665Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('incoming/BQT/BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\nfor i in range(625,645):\n    p=pages[i]\n    if 'گند' in p:\n        print('=== leaf',i,'printed ~',i+1207)\n        print(p[:1500])\n        break\nEOF"
}
```


### [2026-09-06T14:55:43.314Z] TOOL RESULT

```
leaves 721
=== leaf 625 printed ~ 1832
[pdf page 626]
۱۸۲۹

تولد اطفال تا اوان عقیقه وکپواره بتن بطریق
سنت وعرف بفعلآورند .
گل کردن این ان لفط را بجای‌خاموش
کردن استعمال کنند چنانکه کوبند : « چراغ‌را
کل کن » یمنی خاموش کن ‎٩‏ - و بمعنی ظاهر
شدن ر نمودار گردیدن عم هت چد ‎AS po‏
‎a‏ « کچه کل کرد » معنی‌آن باشد کدظاهر
شد و تمودا رگردید .
‎JF JS‏ - بفتح هردوکاف‌فار-ی‌وسکون
هر دو لام . ‎gee‏ از لیمون باشد بمقدار نارنجی
بمثابه‌ای ترش ‎SVS‏ سوزنی در آن فرو برند
‎dul,‏ زمانی بگذارند سوزن کداخته شود ۴ -
ویضم هر دوکاف + ‎Sash gos‏ آ را بعربی
‎Sie‏ خوانند بضم میم و سکون قاف و لام در
آخر ۴ .
گ لگندم بکس اول و سکون‌انی
و فتح‌کاف فارسی و سکون نون و ضم دال ابجد
۱ - در هند متعمل است :
درین داوریگاء ظلیت شان

۴ - رك : جهانگیری + رشیدی .

کلگون

و میم ساکن + بیغ گياهیست دوائی وآن در نظر
چنان نمای دک هکوبی پنج شش دالا کندم بر هم
چنبیده است ۴ .#

گل گنده = پفتح ‎GE‏ فارسی بر وزن
جنبنده , ‎yey‏ از کمای باشد و آن بغایتکنده
و بدیو میشود و زنان بجهت فربهی حلوا کنند
وخورند ۴ .

گل ‎gt‏ = نم ‎Jot‏ و کاف بواو
رسیده وبای ابجد ‎glint‏ کشیده ۰ سیر و گشتی
باشد که در اول بپار کنند و ‎OT‏ چنان بود که
مقدم برجمیم ‎LAS‏ کل زردی بشکفد و مردمان
ازآن کل بسیار بچینند وبرباغها رفته‌درحوشهای
باغ ریزند و جشن‌کنند ۲ .

گل کوده ۷ ‎one‏ را گویند -
و ‎Sy‏ را هم کفته‌اند چه قلم آنرا در کوزها
کرده در خاله نهند .

گلگون 4 »با ات فارسی بر وزن

شد از باد ‎pater‏ کل , شمم جان.
اسلام خان ‎Vy‏ « فرهنگ نظام »
- کل کندم , درائی است که در ‎Myo‏

‎KE‏ ریزها ‎wT yey‏ ونام دیگرش «کورکندم » ( است ) » چون دانه‌هابی است که‌در کورستان
هم میروید 6 و مقصود از کل همان کور است . م
```


## [2026-09-06T14:55:49.560Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('incoming/BQT/BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (636,637,638):\n    print('=== leaf',i,'===')\n    print(pages[i][:2600])\nEOF"
}
```


### [2026-09-06T14:55:51.478Z] TOOL RESULT

```
=== leaf 636 ===
[pdf page 637]
کنج شادآور
گنج شاه آوده - ‎ef (ue‏ حفتم

است ازجبلة هنت کنج 20% برویز ۱

گنج شایگان ۴ - بسن ی کویندحان
کنج بادآورد است که کنج دوبم خسرو باشد »
وچون ‎AGL‏ چیزیرا مبگویند که لابق‌وسزاوار
پادشاهان و ذخیرء و مال بیار و بی پابان باشد
و اين کنج بقابت بز رکه بود و جواهر بی‌نهایت
داشت , بنابرآن بدین نام خوالدند .

گنچشاك ۴ = بنم اول ‎Ss‏ ثالك »

معروف است و آن‌پر نده‌ای
باشد که عربان عصفور
خوانند واو را خانگی
نیز کوبندومرغ‌جوجه *
و مرغ کوچك را حم
‎alo‏ - وهر ‎fap‏
‏کوچك را به اودبت
آوقوت باه دهد .

دهتد. مضز سس

گنج عروس -« نام کنج اول است
‎teed‏ کنوزئمالة خسروی. کوبند این کنج را
خود جمم کرده گذاشته بود ۴ - و نام یکی از
تصنیفات پارید «م هست .

گنج قریهگن - بکس اك و فا »

هرا

نام ‎gly‏ است از موسیقی 5

گنج گاو ۱ - ‎ae‏ از
کنجهای جمشید . وآن در زمان بپرام گورظاهر
شد . گویند دهقالی زراعت را آب میداد ‎AS‏
‏سوراخی بهم رسید وآبها تمام بآن‌سوراخ میرفت
و صدائی عجیب ازآن سوراخ بر می‌آمد دهقان
بنزد بپرامآمد واحوال را گفت. بهرام با نجارفته
فرمودآ نجا را کندند عمارتی پیدا شد بس عالی +
اشاره بموبد کرد که « درآی ‎ol‏ خانه» . چون
در آمد دو کاومیش دید از طلا ساخته بودند
و ‎late‏ آنها از بافوت قیمتی بود و شکمهای
‎WT‏ را پراز نار وسیب وامرود زرین کرده‌ودرون
میوه‌های زرین را پرازمروارید ساخته بودند ودر
پیش س رکاومیش آخوری از ‎Mh‏ بسته بودندوآ نها
را پر از جواهر قیمتی نموده و بر کاومیشها نام
جمشید کنده بودند و بر اطراف کاومیشها اقام
جانوران پرنده و چرنده از طلا ساخته و مرصع
کرده بودند » خبر به بهرام آورد بهرام فرمود
تمام آن گنج‌را بستحقین ومردمان کم بضاعت‌داد ند
و در ممالك اومستحق ویریشان نماندکه صاحب
سامان‌نشد - وتاملحن‌هفدهم استازسی لحن‌باربد .

گنج گاوان ۲ همان کنج کاو

۱ ر: حصفحةه۱۸۳

۴ رك : شایگان .

۴ کیلکی(ع)»5ع[0۳ع

. ۱ص ۲۸۸ ۲ , شپمیرزادی ‎gunjashk‏ « کت . ۲ می ۱۷۷ ۰ ۱۸4 ‎٩‏ ؛ پرنده است
دستهةٌ سبکبالان با منقار مخروطی .که جذه‌ای کوچك دارد و دانه خوار است

۴ رك : ح ه ‎baie‏ ۱۸۳۸

© برگل تر عندلیب گنج فربدون زده است
لشکر چین در بهار خیمه بهامون زده است .

? منوچهری دامقالی ص ۱:۷ * .

۱ = کنج کاوان ‏ گنج گاومیش . شرح این داستان درشاهنامة فردوسی « شاعنامة بخ

ج ۷ص ۲۱۸۵ - ‎tor‏ آمده است :

مرا چون دعوت عیسی است عیدی هرزمان دردل .

ن جگاو = کنجکاومیش :
جم چون سخن ‎wail,‏

دلم قربان ‎Le‏ فقر و کنج کاو قربانش .
« خاقانی شروانی ص ۲۱ *.

ورا «کنج کاوان» همی خوا ند ند.
فردوسی طوسی« شاهنامة بخ ج ۷ ص۲۱۸۹*.

=== leaf 637 ===
[pdf page 638]
NALA

است که از جمشید بود و بدست بهرام گورافتاد.
گنج گاو میش ۱ ‎wee‏ کنج
‎AIT‏ است که کنج جمشید باشد .
گنج او ‎oo‏ نام لحن‌هفدهم‌است
از سی ‎god‏ باربد وآن را کنج کاو ‎ec‏ میگوبند
ورسم‌الخط این زمان بيك واو است
گنچگاه ؟ = بروزن وسعتی پنجگاه
است که ‎Les‏ بلندی مقام راست و تمیپستیآن
مرتفع است .
گنجور ۴
را گوبند .
گنجو یر ۴ » با واربه تستانی‌مجهول
رسده بروزن سردسیر ؛ بلفت زند وبازند بمعنی
گنجور است که خزانه‌دار باشد ؛ و در جای‌دیگر
بجای تحتانی بای ابجد ‎lata Boyde yl‏ .

گنحه ۰

Sate ‏بر وزن پنجه » نام‎ © x

‎Oban ©‏ رنجور. خزانه‌دار

‏)1( چك » چش : کاوس.
‎AT eS = eS =‏ .

‏ند پیدسنی

‏است مشهورمابین تبربز وشیروان؟ ‎ole Ss‏
و مولد شیخ نظامی علیه‌الرحمه از ‎tT‏ است -
و خر الاغ دم بریده را نیز گوبند و بعربی ابتر
خوانند ۷ .#۶

‎AP‏ - پنتح اول و سکون ثانی و دال
ابجد . بوی بد را کویند ۸ - وضم اول, بمعنی
خایه باشدکه یمربی خمیه خوانند ‎٩‏ .

‎eS‏ *. بر وزن ‎lane‏ چیزی را
کویند که گندیده باشد و ازآن بوی‌ناخوشآید.

‏گند ]ور ۱.- بضم اول‌وفتح واوبروزن
‎SS‏ مردم شجاع و دلاور و مردانهرا گویند-
و سیهالار را نیز کفته‌اند ۱

‏گثد‌ای ۰۱۳ بر وزن دروای ؛ ‎eee‏
‏کند است که هر چیز بدبوی و گنده ومنعفن
باشد .

‏گند لیدستر ۱۴- ‎te,‏ خابة سکه

‏از :گنج ‎gas wale Vail‏ « اوستابی 881102 سرود [ رك : کانها بقلم

‏پورداود ۳ اول ص ‎Af ٩۱‏
دارند گی ) »
وحام لگنج .

‏بوتکرص۷۹. رلك : ح۳.
‎٩‏

‎te ‏رك:‎

‎femal -‏ «شروان» است

‏از :کنج ور 0۲ ‎vars yy)‏ پوند ‎Slat‏ و
پپلوی ‎ganjbar‏ ۳۳ ۶ . جزء دوم ازمصدر ‎bar‏ (بردن) است معنی‌برنده
‎ganjobar , wa ws ۴‏ پهلوی‌بمعنی‌خزانه‌دار, گنجور. رله :

‎me‏ گنک مس ‎IGS‏ مه غزنه > غزنین(لفة محل گنج » گنجینه).
۷ - نیزه کنجه» بمسی قفه ودولابچه استعمال‌شود.

‏- اوستا 88101 ( ‎cy‏ متعفن ) ۰ پپلوی ‎gand‏ , 88208 ( گنده ) , هندی

‏باستان ‎gandhé‏ ( بو, عطر [خوشبو] ) ‎ganda sis!‏ بلوچی ع 8874 (گل ‎oS]‏

‏اوز ] , فنله ) , 820028 ۰ 8220288 ( بد , شربر ) » پارسی باستان - 88508 ‎asa)‏
‏تتفرآور ) . ‎JS.‏ 80080 « اسشق ‎٩۳6‏ > و رك : هویشمان ‎٩۳4‏ .

‎-] ‏-کردی 800 ( خمیتین ) «ژاباس ۰۳۹۹ , معرب‌آن « جند » [ جند بیدستر‎ ٩

‏نیز ‎Ha‏ پهلوی ‎gund‏ ( سرباز , سپاء ) ‎(pease » ۲۷۵ ple‏ مرب « جند ‎٩‏ ۰

‏کردی 8074 ( دهکد» . ببلاق ) « ژابا ص ۲۹ .
( پسوند قاعلی و صفت مشبهه ) ‎Sy‏ کندای .
و ‎af:‏ ( بضم ) و رد : پیدستر +
» از: کنج ‎peo]‏ اول] (ه.م.) + یدن (پسوندصدری)؛

‎a VF‏ کندا (هم) . وزا
۵ گنجیدن - بنم اول رفتح پنجم

‏*- از :کند ( کندیدن ) +۱
‎NN‏ ره : کندآور .

‏جاکرفتن مظروفی در ظرفی » درآمدن چیزی در چیزی -

=== leaf 638 ===
[pdf page 639]
‎oy‏ چه گند ‎gine:‏ خایه و ‎ete‏ حیوالی است
آبی شبیه بسکه و ممرب ‎OT‏ جند پیدستر باشد
و آن ‎TH‏ بچگان کوبند وبعربی خسیةالبحر
خوانند .
‎SAP‏ - بنتح اول ‎SLT,‏ وسکون
ثانی و زای فارسی ۰ مخفف کنگه‌دژ ۱ (۱)است
وآن قلعه‌ای ‎Soy‏ ضحاك در شهر بابل ساخته
‎op‏ وآلرا بپشت ‎KF‏ نام بهادء بود ودرآن قلعه
‎gale‏ کران وساحران ‎her‏ بودندوا کنون ‎AS‏
‎cal‏ وبجز تلی باقی ‎als‏ و برسرآن تل چاهی
است بسیارعمیق ‎SaaS.‏ اروت و ماروت در
‎oT‏ چاه محبون اند .
گندسك = ‎ee‏ اول ‎Sy‏ تالك‌وفتح

‏سین بی‌نقطه » تفنیر خصی‌الکلب ۳ است ,وآن
بیخی باشد مالند خصیةالتملب و هر زوجی برهم
‎gener‏ یکی بزرکه ودبگری کوچك. اکرمرد
بزرکه ‎YT‏ بخورد و با زنان جماع کند فرزند
ترینهآورد واگر زن کوچك ‎LT‏ بخورد مادینه,
‎OT cles‏ قطم شهوت کند ‎OTs‏ مقوی‌باهباشد,

‏(۱) چش :کنگه دز .

‏۱ رك :کنگه دژ.
‎Ke‏ مومن : خصی الکلب .
«رشیدی» . ۴ ركه ‎ga:‏ .

‎.) ‏از :کندم با ( ابا رآش‎ - ٩

‎NARI

‏و عربان ‎oT‏ را قاتل اخیه کوبند بوامطةٌ آنکه
‎eT‏ دوییخ‌اند مانند دو زبتون برهم چسییده که
‎ILS‏ یکی فربه و دیگری ‎AV‏ ميشود و سال
‎GTS‏ فربه ‎oy‏ لاغر وآنکه لا بود فربه
میگردد ۰

‏گندش ۲ = بکرئاكث بروزن‌واجش:
کو کرد را گونند وآن در ‎eb‏ میشود : احمر
و ایيش . کوکرد ‎pol‏ بکجزو از اجزای
‎ST‏ است و کوکرد ‎Gaal‏ بکجزو از اجزاي
باروت +

‎Sa‏ © © بروزن‌اند,بممنی ک و کرد
است - وباروت را نیز گوبند .

‏نك ‎OF‏ = بنتح اولو کسرکاف‌فارسی,
بمعنی‌خر ی کیاه است. گوبند. شقاقل بی ‎ASS‏
‏است وخریآنرا ‎cals‏ دوست میدارد» ؛
‎bp Sa‏ صحرائی است #۰

‏گندما ۱ - آش کندم را کوبند که
حلیم باشد .

‎Oa‏ - بر وزن توجمه ۷ ۰ کرهی
باشد سخت ‏ وآن از بدن آدمی‌برمیایسوعربان

‎wn

‏۴ - پیونانی ‎orchis‏ .)4 : لك #س۳۳ ؛ و رل : ‎fins‏
‏۴ ۰ کندش و کندکه . کوکرد » ‎elt‏ هندست »
- رك : خر یگیاه .

‏- مولف «ترجمه» را طبق تلفظ معمولی

‎pus? ۵‏ - بفتح اول رضم سوم + پهلوی و پازند 88011018 , معرب جندم ‎Jandum‏

‏( در : چوزجندم ) ,کردی ع ‎Jul. genim‏ ع ‎ghanum‏ . رخی ‎ghidim‏ , سنکلیچی
و منجی ‎ghandém‏ . مریکلی ‎zhandum . zhandam‏ , شفتی ‎zhindam‏ . بردغا
‎ghadum‏ , بلوچی ‎gandim‏ « استق ‎٩۳۵‏ > و رگ : هوبشمان ایا ؛ کیلکی » فریزندی ۰
برلیونطنزی 8800010 «کک. ۱ص ۰۲۸۹ دردیه‌های گیلان 8804181۳ ؛ سمنانی ‎gundum‏
‏سنگری ‎.gannim‏ سرخدیی ‎.gunném‏ لاشگردی 80048۳0 . شهییرزادی ‎gandim‏
‏۰ . ۲ ص ۰۱۸۲ ؛ گیاهی است از ‎Sy‏ غلات , یکاله . با اقةٌ از بند بند و تو خالی .
‎SUT‏ بی دمب رک ولی ‎OT als‏ ساقه را درمحل کره‌ها می‌پوشاند . گل کندم ازسنبله‌عابی
تشکیل يافته که شامل سنبله‌های کوچکتر میباشند .
(برهان فاطع ‎(ver‏
```


## [2026-09-06T14:56:08.651Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"بود گست\\|نیکی بود\\|گَست\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head -10; echo \"--- sizes ---\"; wc -l MON_part1.txt MON_part2.txt"
}
```


### [2026-09-06T14:56:08.731Z] TOOL RESULT

```
--- sizes ---
  99339 MON_part1.txt
  94500 MON_part2.txt
 193839 total
```


## [2026-09-06T14:56:10.124Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== ARY latin index ===\"; grep -n -i \"GWEBH\\|GWEDH\\|gʷebh\" incoming/ARY/ARY_latin_index_pages.txt | head -10; echo \"=== ARY zarf/gand ===\"; grep -n \"ژرف\\|گند \" incoming/ARY/ARY_pages.txt | head -10"
}
```


### [2026-09-06T14:56:10.207Z] TOOL RESULT

```
=== ARY latin index ===
=== ARY zarf/gand ===
13138:گند گن (به چم "خایه "و "غده) / ۴۳۴۳
```


## [2026-09-06T14:56:14.274Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '13120,13160p' incoming/ARY/ARY_pages.txt; echo \"=== search zarf ===\"; grep -n \"ژرف\" incoming/ARY/ARY_pages.txt | head"
}
```


### [2026-09-06T14:56:14.351Z] TOOL RESULT

```
فریزی کهن (/۸ط2۶/5 ۵ا0): ۰ 1188۴ :۸12507218
آلمانی کهن مه ۵۲۲ 0۵ 7 (اتش] ۲0۱/۴ ,۸5317 ۲0(/7)
۸007 4 (336ت)) 57
۱ آلمانی (08244(0): 61۸680۲ ,65شل1 برهان قاطع ‏ ۱۳۲
انگلیسی کهن (8۷08 ص01): 2106۸۷
یادداشت؛ ۱
چم این واژه در زبان‌های ژرمنی: صدا ایجاد کردن» سر و صداکردن, :
پپلری (ماتق۳۸): 611/8۸0 ,6118۸7 سرئدی (5515): ادا
کردی (7ل60015): زد زا ان نروژی (0737501۸/: لدیرده ۱
لاتین (4710ا): ۸ هلندی (7ع017): 4 ,۴71۴
نررس کهن (۸088 01): ۸ اسلاوی کهن (ع/۲شا5 تت#ناتل ص2ل0):
فریزی کهن (/(مل5ل۶# 2ا۵): 0۳۳ 608۸
آلمانی کهن (/(4/ل058 ۲۲04 صا0): 0۳7 روسی (/۸/551۸): زان
: آلمانی (05701۵(7): 07 لیترانی (/7۸(740ا714ل) ققاجاه
انگلیسی کهن (#لدناه2۸/0 ۰:۱۵ ۲۲۸8 لترنی (لتی) (2ف71ا): ان
انگلیسی (تلوانا8/0): زاره
[pdf page 442]
۹
گند گن (به چم "خایه "و "غده) / ۴۳۴۳
پسگشت‌ها ند کرد ما :57
5و 200800 مق ۵0۷۷۵ هام
1 (00(658) :۲62/28 ۸4 برهان قاطع : ۱۳۶
بادداشت:
چم‌های این واژه در زبان‌های غیرایرانی: کاسه» ظرف گرد و گنبد مانند؛ فرورفتگی گرد به شکل کاسه» سس کله. ۱
ا
پهلری (۲7ماتلمه): نان ایتالیایی ((لله4): کیان
کردی (8013[4): 0 پرتغالی (۳0371010895): ان
سانسکریت (54۸/58077): زان ی
پرنانی 0510): 5 6 (00 پسگشت‌ها ار هن دی دادن
لاتین (71ل): 08 ۶0000 .
فرانسه (ح/۸ظ۳۴): ان ورن 6 1287108 :۸5213
اسپانیایی (5۳۸(۷/54): ه00 برهان قاطع : ۴۱
یادداشت:
واژه‌ی انگلیسی 0081۸80 (به چم "گناد" و "خاپه" و "تخمدان") نیز از همین واجریشه آمده است.
اْ
۱
۱ اوستایی (04۷88742۷: سانسکریت (54۸/577): ه0۸0
مت لا۸ 0۸3 رالان6۸ با7ان6۸ لبتوانی ((فا/(هنال72لل): رانا دی
پارسی باستان (( ۰:65 6۸83۸ لتونی (لتی) (1۵(0 7 مل): زان ان
پهلو ی (1ا7ل[۳۸):
6۸0۸615 ,6۸0 پسگشت‌ها 5
=== search zarf ===
```


## [2026-09-06T14:56:18.838Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '13155,13200p' incoming/ARY/ARY_pages.txt"
}
```


### [2026-09-06T14:56:18.888Z] TOOL RESULT

```
۱
۱ اوستایی (04۷88742۷: سانسکریت (54۸/577): ه0۸0
مت لا۸ 0۸3 رالان6۸ با7ان6۸ لبتوانی ((فا/(هنال72لل): رانا دی
پارسی باستان (( ۰:65 6۸83۸ لتونی (لتی) (1۵(0 7 مل): زان ان
پهلو ی (1ا7ل[۳۸):
6۸0۸615 ,6۸0 پسگشت‌ها 5
بلوچی (اتله‌تاتمه): 7 ۶010/00
57 6۸70۸6 ,6۸0 4 (878673) دم ما
افقانی (پشنر) (/۸۳۵۸(۷): 9 ,1024 ماه
6۸۷۵۸3 ,6۸10۸ برهان قاطع + ۱۸۴۱
[pdf page 443]
اند
بادداشت.
> به عقیده‌ی ۳016013909 واژه‌های انگلیسی 87186 و آلمانی 4 (آلسانی کمهن:5718136۸3 و
گرنبک: 871876۸01) نیز از همین واجریشه‌ی هند و اروپایی هستند. ۶
۲ چم این واژه در بلوچی: بد» شرور» فضله. ۰ اا ۳
چم این واژه در اوستایی و سانسکریت؛ بد. قشت
هند و آروپایی (۸00-81025۸0/): ۳01 [ هروش ۵ ۳
اوستایی (4۷887۸۷): خلاا نوم هتیت (7177172), ۷ قراگا
پپلری (/2۸1۸۲): 6۸۳۲736 بااتا0ابیج ۰
کردی (۸)80[5(7): رالد نی پسگشت‌ها خد یی راد ار ۳
بلوچی (الق‌تاتمه: 06 91 و
افغانی (پشتر) (//(4۳0۸): 40 (5ه5 ۲ دام ما
04 ملافغانمتی 53516 عناق
تخاری 8 (8 (۸ل۶ه70807). ۱ قنزانرریانن :۸0/5 2 2 تته ید
ختنی (7707۸7832)): خاداندی برهان قاطع : ۱۸۴۲
سانسکریت (8۸۸8807): 00021۸
یادداشت,
شاید واژه‌های انگلیسی 1۷ و آلمانی 0107 (گوتیکه: 801 نیز از همین واجریشه باشند.
کت
هند و اروپایی (4۸00-200754(۷): 6۰ ,۹0517105
پهلری (7لماللمم): رات زاره ۱
کردی (۸)]80[5(7): 01 نآ نررس کهن (۸0788 صا0): هآ
سانسکریت (8۸(/58077): آلمانی کهن (/2/ن027 بزهزبز صرم):
6004 بقا60 بنتشاقی ۸ بآ10
آرمنی (4۸15۸1۸): 4ات۸ آلمانی (0870/۸0): 65
پرنانی (0768۸0): رن انگلیسی کهن (بلقلا نت صاه):
لاتین (10آما): 62۲8 8 اوق
ایسلندی کهن (۵ 5۸/01۸۷ صان): هلندی (7ع017), 068
[pdf page 444]
ا
أ
گواریدن گواردن / ۴۴۵
۱
لهستانی (۳0/34): 00۸ پسگلتهل ۶2۳3۵۷۵۵5 : ۱
روسی (8314(7/): هتاختاه 19497 ۸002 أ
```


## [2026-09-06T14:56:28.445Z] TOOL CALL #43: Bash

```json
{
 "command": "sed -n '1,60p' tools/fetch_source.py"
}
```


### [2026-09-06T14:56:28.551Z] TOOL RESULT

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


## [2026-09-06T14:56:33.012Z] TOOL CALL #44: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%DA%98%D8%B1%D9%81\" \\\n \"https://en.wiktionary.org/wiki/%DA%AF%D9%86%D8%AF\" \\\n \"https://www.etymonline.com/word/baptize\" \\\n \"https://www.etymonline.com/word/quaver\" \\\n \"https://www.etymonline.com/word/quiver\" \\\n ; do echo \"### $u\"; python3 tools/fetch_source.py \"$u\" --note \"page 204 verification (Gwebh 1/2, Gwedh)\"; done"
}
```


### [2026-09-06T14:56:38.367Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/%DA%98%D8%B1%D9%81
/home/sfmqrb/git/rishe/data/verification/sources/web/d3bc71b82df6bd73.txt
### https://en.wiktionary.org/wiki/%DA%AF%D9%86%D8%AF
/home/sfmqrb/git/rishe/data/verification/sources/web/9369b7ccb1f24186.txt
### https://www.etymonline.com/word/baptize
/home/sfmqrb/git/rishe/data/verification/sources/web/9759bef4c6a7a138.txt
### https://www.etymonline.com/word/quaver
/home/sfmqrb/git/rishe/data/verification/sources/web/b1c9d399c68860a9.txt
### https://www.etymonline.com/word/quiver
/home/sfmqrb/git/rishe/data/verification/sources/web/0ae7aa4802a87d44.txt
```


## [2026-09-06T14:56:41.044Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in d3bc71b82df6bd73 9369b7ccb1f24186; do echo \"##### $f\"; grep -n -A25 -i \"Etymology\" $f.txt | head -60; done"
}
```


### [2026-09-06T14:56:43.383Z] TOOL RESULT

```
##### d3bc71b82df6bd73
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Adjective 
69-
70- 1.3.1 
71- Derived terms 
72-
73- 1.3.2 
74- Descendants 
75-
76- Toggle the table of contents 
77-
78- ژرف 
79-
80- 9 languages 
81-
82- فارسی 
83- Français 
84- हिन्दी 
85- Kurdî 
86- Malagasy 
87- Русский 
--
149: Etymology
150- [ edit ] 
151-
152- Inherited from Middle Persian *žarf , borrowed from Parthian 𐫋𐫜𐫡 ( jfr /⁠žafr⁠/ , “ deep ” ) , displacing native [Book Pahlavi needed] ( zwpl /⁠zofr⁠/ ) , both from Proto-Iranian *ǰafráh ( “ deep ” ) . Possibly a doublet of جَفْر ( jafr , “ occult knowledge ” ) , an Arabic loanword perhaps originally borrowed from Iranian.
153-
154- Pronunciation
155- [ edit ] 
156-
157- ( Classical Persian ) IPA ( key ) : /ˈʒarf/ 
158-
159- ( Dari, formal ) IPA ( key ) : [ʒäɾf] 
160-
161- ( Dari, formal ) IPA ( key ) : [ʒäɾf] 
162- ( Kabuli ) IPA ( key ) : [ʒäɾf] 
163-
164- ( Hazaragi ) IPA ( key ) : [ʒäɾf] 
165-
166- ( Iran, formal ) IPA ( key ) : [ʒæɹf] 
167-
168- ( Tajik, formal ) IPA ( key ) : [ʒäɾf] 
169-
170- Rhymes: -arf 
171-
172- Readings
173-
174- Classical reading ? 
##### 9369b7ccb1f24186
62: Etymology 1 
63-
64- 1.1.1 
65- Pronunciation 
66-
67- 1.1.2 
68- Noun 
69-
70- 1.1.2.1 
71- Derived terms 
72-
73- 1.1.3 
74- References 
75-
76- 1.2 
77: Etymology 2 
78-
79- 1.2.1 
80- Pronunciation 
81-
82- 1.2.2 
83- Noun 
84-
85- 1.2.3 
86- References 
87-
88- 1.3 
89: Etymology 3 
90-
91- 1.3.1 
92- Verb 
93-
94- 2 
95- Persian 
96-
97- Toggle Persian subsection 
98-
99- 2.1 
100: Etymology 
101-
102- 2.2 
103- Noun 
104-
105- 2.2.1 
106- Derived terms 
107-
108- 2.2.2 
109- References 
110-
111- 3 
112- Southwestern Fars 
113-
114- Toggle Southwestern Fars subsection 
115-
116- 3.1 
117- Noun 
118-
119- 4 
120- Urdu 
121-
```


## [2026-09-06T14:56:49.532Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && awk '/^ Persian *$/{f=1} f' 9369b7ccb1f24186.txt | sed -n '1,60p'"
}
```


### [2026-09-06T14:56:51.235Z] TOOL RESULT

```
 Persian 

 Toggle Persian subsection 

 2.1 
 Etymology 

 2.2 
 Noun 

 2.2.1 
 Derived terms 

 2.2.2 
 References 

 3 
 Southwestern Fars 

 Toggle Southwestern Fars subsection 

 3.1 
 Noun 

 4 
 Urdu 

 Toggle Urdu subsection 

 4.1 
 Etymology 

 4.2 
 Noun 

 4.2.1 
 See also 

 Toggle the table of contents 

 گند 

 9 languages 

 বাংলা 
 فارسی 
 Magyar 
 Bahasa Indonesia 
 Kurdî 
 Malagasy 
 پنجابی 
 Русский 
 سرائیکی 

 Entry 

 Discussion 

 English
```


## [2026-09-06T14:56:53.870Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n \"Middle Persian\\|Proto-Iranian\\|Avestan\\|Hasandust\\|stench\" 9369b7ccb1f24186.txt | head -20"
}
```


### [2026-09-06T14:56:53.917Z] TOOL RESULT

```
209: Unclear. Cognate with dialectal Persian گند ( gond ) and Southwestern Fars گند ( gond ) . See Middle Persian gwnd for further etymology.
280: From Middle Persian gwnd ( /⁠gund⁠/ ) .
316: Inherited from Sanskrit गन्ध ( gandha , “ smell, stink ” ) . Cognate with Persian گنده ( gande , “ stenchy ” ) .
325: stench 
347: Persian terms inherited from Middle Persian 
348: Persian terms derived from Middle Persian
```


## [2026-09-06T14:57:03.531Z] TOOL CALL #48: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%DA%AF%D9%86%D8%AF%DB%8C%D8%AF%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%CE%B2%CE%AC%CF%80%CF%84%CF%89\" \\\n \"https://abadis.ir/fatofa/%DA%AF%D8%B3%D8%AA/\" \\\n ; do echo \"### $u\"; python3 tools/fetch_source.py \"$u\" --note \"page 204 verification (Gwedh: gand/gandidan, gast; Gwebh 1: Greek baptein)\"; done"
}
```


### [2026-09-06T14:57:08.210Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/%DA%AF%D9%86%D8%AF%DB%8C%D8%AF%D9%86
/home/sfmqrb/git/rishe/data/verification/sources/web/4f9e5a364fe5c936.txt
### https://en.wiktionary.org/wiki/%CE%B2%CE%AC%CF%80%CF%84%CF%89
/home/sfmqrb/git/rishe/data/verification/sources/web/c29e71b2ff91b614.txt
### https://abadis.ir/fatofa/%DA%AF%D8%B3%D8%AA/
/home/sfmqrb/git/rishe/data/verification/sources/web/0526ff69bab80adc.txt
```


## [2026-09-06T14:57:12.163Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"### gandidan\"; grep -n -i \"Middle Persian\\|Proto-Iranian\\|Avestan\\|Etymology\" 4f9e5a364fe5c936.txt | sed -n '1,20p'; echo; echo \"### bapto\"; grep -n -i \"Proto-Indo-European\\|Etymology\\|dip\" c29e71b2ff91b614.txt | head -20; echo; echo \"### abadis gast\"; grep -n -i \"معین\\|پهلوی\\|گست\" 0526ff69bab80adc.txt | head -25"
}
```


### [2026-09-06T14:57:12.262Z] TOOL RESULT

```
### gandidan

### bapto
62: Etymology 
156: Etymology
159: From Proto-Hellenic *gʷápt͏̌ō , from Proto-Indo-European *gʷh₂bʰ-yé-ti , from *gʷeh₂bʰ- ( “ to dive, dive in ” ) . Cognate with Proto-Germanic *kwēbijaną , [ 1 ] Avestan 𐬘𐬀𐬟𐬭𐬀 ( jafra ) , Persian ژرف ( žarf ) , Lurish گںهںر ( gəhər , a lake ) , and Sanskrit ग॒भी॒र ( gabhīrá ) .
181: to dip ; to submerge 
1239: Categories : Ancient Greek terms inherited from Proto-Indo-European 
1242: Ancient Greek terms derived from the Proto-Indo-European root *gʷeh₂bʰ- 
1243: Ancient Greek terms derived from Proto-Indo-European 

### abadis gast
4:TITLE: گست - معنی در دیکشنری آبادیس
6:گست - معنی در دیکشنری آبادیس 
10: گست
18: گست. [ گ َ ] ( ص ) زشت. قبیح. نازیبا. ( برهان ) ( از آنندراج ). زشت. ( لغت فرس اسدی ) ( جهانگیری ) : 
20:از چه با یارکار گست کنی. عماره.
21:روی ترکان بست نازیبا و گست 
23:سخنها که گفتی تو بر گست باد
24:دل و جان آن بدکنش گست باد. فردوسی.
25:اگر بر چرخ با این عادت گست 
28:کجا بر چشم او نیکو بود گست. ( ویس و رامین ).
30:قافیه شد نرم گردن گرچه توسن بود و گست. سوزنی.
32:به پیش صورت خوبت بود گست. شمس فخری.
37:( صفت ) ۱ - زشت نا زیبامقابل زیبا : چه عاشق باشد اندر عشق چه مست کجا بر چشم او نیکو بود گست . ( ویس ورامین ) ۲ - شرم آور فضیح دلبرا . دورخ تو بس خوبست از چه با یار کار گست کنی ? ( عمار. مروزی . رودکی ) 
39: فرهنگ معین
45: زشت، قبیح، نازیبا: دلبرا دو رخ تو بس خوب است / از چه با یار کار گست کنی (عماره: شاعران بی دیوان: ۳۶۳ ). 
49: گست ( به انگلیسی: Ghost ) گروه هوی متال سوئدی است که در سال ۲۰۰۶ در شهر لینشوپینگ تشکیل شد. این گروه تا به این لحظه چهار آلبوم استودیویی منتشر کرده است. [ ۲] [ ۳] 
67: wiki: گست 
69: گست (مجارستان). گست ( به مجاری: Geszt ) یک منطقهٔ مسکونی در مجارستان است که در ناحیه شارکاد واقع شده است. [ ۱] گست ۵۱٫۴۲ کیلومتر مربع مساحت و ۸۲۱ نفر جمعیت دارد. 
70: wiki: گست (مجارستان) 
82:من گزاره ای از پیامِ پیشینم را در پیوند با " پَرگست" پاک کردم تا بیشتر درباره این واژه که" به چمِ " مبادا، امید به رُخ ندادن" است، کاوش کنم؛ چرا که پی بردم در زبانِ پارسیِ میانه کارواژه یِ " گَستَن" دیگری نیز وجود دارد که گویا پیوندی با " گستَ، گست، گند، گندگ" در پیامِ پیشین ندارد. به هر روی چنانچه از آن آگاهی یافتم، دریغ نمی کنم. درباره یِ پیشوندِ " پَر" و چگونگیِ کاربستِ آن در زبانِ پارسیِ کُنونی، در زیرواژه " پَر" پیامم را خواهم گذاشت. این پیشوند بسیار از دیدِ ما دور مانده بود و در آینده نقش بسزایی را در زبانِ پارسی بازی خواهد کرد. به گمانم این پیشوند را نباید با پیشوندِ اوستاییِ " پَئیری" به چمِ " پیرا، پیرامون" که آنهم به ریختِ " پَر" در زبانهایِ میانه آمده است، یکی انگاشت. 
113:پهلوی: گیزیستَگ ( gizistag ) 
121:سگستان ( سکاستان ) >>> سَجَستان >>> سیستان: پرورش سگ ) ) 
129:پهلوی: ویستاخ ( wistāx ) 
142:معنی: در برابر ( نسبت ) به خدای بزرگ[اهورامزدا]، خودسر ( مغرور ) و "گستاخ" مَباش! 
153:پیامِ شما بویژه درباره یِ واژه یِ " پَرگست" روشنگرانه و آموزنده بود.
```


## [2026-09-06T14:57:24.799Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SYN.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor leaf in (1101,1266):\n    p=pages[leaf]\n    print('=== leaf',leaf,'first 200 chars ===')\n    print(p[:300].replace('\\n',' | '))\n    print('...tail:', p[-200:].replace('\\n',' | '))\nEOF"
}
```


### [2026-09-06T14:57:26.645Z] TOOL RESULT

```
=== leaf 1101 first 200 chars ===
efer to assume a more | complicated development through ‘break | up into small particles, vaporize, ex- | hale’. Walde-P. 2.617. Falk-Torp 1168. Franck-v. W. 667. | OE swecc, swec (also ‘taste’), vb. gesweccan, OS swec, OHG sweche, vb. swehhan ‘smell, stink’ : W. chweg ‘sweet, pleasant’, cwaeth ‘taste’, etc
...tail: ’ (cf. NPers. sb. bu, vb. buzdan ‘smell’) : Skt. budh- ‘be awake’, ‘become aware of’. Walde- P. 2.147. Barth. 917 f. | 15.25, 26. Aristotle (De anim. 2.9) remarked on the lack of any independent classif
=== leaf 1266 first 200 chars ===
ti(s) ‘cease, quit’, OPruss. aulaut ‘die’, etc.; ‘bad’, fr. ‘pliant, yield- ing’. Walde-P. 2.405. Miihl.-Endz. 3.632, | 7. ChSL. ziti, SCr. zao, Boh. zly, Pol. ay, Russ. zloj (in SCr. and Russ. now mostly ‘malicious’ or ‘angry’), prob. as ‘bent, crooked’ : Lith. pa-gvilti ‘bow’, pa-zulnus ‘slanting, s
...tail: Ir. cert, coir Du. recht Skt. rla-, tju- Nir. ceart, cir OHG reht ; | W. tawn, cyfiawn, cywir MHG reht, gercht Br. gwirton, ecun NHG recht, gerecht | ‘Right’ is understood here in its moral sense and in t
```


## [2026-09-06T14:57:33.752Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '25985,26005p' SYN.txt; echo \"==== 2nd ====\"; sed -n '29715,29735p' SYN.txt"
}
```


### [2026-09-06T14:57:33.873Z] TOOL RESULT

```
pleasant smell or taste’ : ON hnita ‘to strike’). Some prefer to assume a more
complicated development through ‘break
up into small particles, vaporize, ex-
hale’. Walde-P. 2.617. Falk-Torp 1168. Franck-v. W. 667.
OE swecc, swec (also ‘taste’), vb. gesweccan, OS swec, OHG sweche, vb. swehhan ‘smell, stink’ : W. chweg ‘sweet, pleasant’, cwaeth ‘taste’, etc. Walde-P. 2.521,
ME smelle, NE smell, sb. and vb. : LG smelan, Du. smeulen ‘smolder’, Flem. smoll ‘hot’, NE smoulder, outside con- nections dub., but English development through ‘steam, vapor’, as in NHG riechen. Walde-P. 2.691. Franck-y. W. 626.
OHG riohhan ‘give forth smoke, steam or smell’, sb. rouh, then for ‘smell’ also subj. MHG, NHG riechen, sb. MHG rouch, geruch, NHG (rauch ‘smoke’) geruch, Du. ruiken, sb. reuk : OF réc ‘smoke’, réocan ‘give forth smoke or steam’, NE reek, outside connections dub. Weigand-H. 2.585. Franck-—y. W. 562.
MHG smecken, smacken, sb. smac ‘taste’ (15.31-34) are also used for ‘smell’ (both subj. and obj.), and so for- merly and still dial. NHG schmecken, schmack. Cf. Paul, Deutsches Wtb. s.v.
6. Lith. uosti, uostyti, Lett. uost, uositt, see above, 1. Hence sbs. Lith. uoslé (also ‘nostril’), Lett. woza, uodl’a,
Lith. kvapas, vb. kvapéti : Grk. xarvos ‘smoke’, Lat. vapor ‘steam, vapor’, etc. Walde-P. 1.379 f.
"Lett. smaka, vb. smakuot, fr. MLG smak(e) ‘smell’ and ‘taste’ (cf. 15.31). Mihl.-Endz. 3.950.
7. ChSl. qchati, sb. qchantje (both rare), vonjati, obonjati, sb. vonja, obo- njanije, SCr. vonjati, vonj, njuh, Boh. vonéli, viiné, Pol. wachaé, wech, wor,
Russ. njuchat’, obonjanie (vonjat’ ‘stink? von’ ‘stench’), all fr, *on-, *on-s, with a without the development of initia} ; (ee Vondrék 1.214) : Skt. an- ‘breathe Grk. avepos ‘wind’, Lat. animus ‘mind? halare ‘breathe’, ete. Walde-P. 1.56 ff. Miklosich 222. Otherwise, separating into three groups, Briickner 364, 604 630 f. ‘
Boh. pdchnouti, Pol. pachnaé, Russ, pachnit', Boh., Pol., Russ, zapach : ChSI. pachati ‘toss, fan’, Russ, pachnut! ‘blow’, prob. fr. a root *pér- ‘blow’, perh. seen in some Gme. words, as OF foes ‘fringe’. Walde-P. 2.67. Briickner 389,
Boh. éichati, sb. Gich : &ti ‘perceive, feel’ (15.11), also with specialization to ‘smell’ (so freq. also Pol. czué), as in Fr. sentir. Berneker 162.
8. Skt. ghra-, with sb. ghrana- (mostly obj., but also subj.; cf. Béhtlingk, Wtb. s.v.), see Grk. éc¢patvouat, above, 1.
Skt. gandha- : Av. ganti- ‘bad smell’, OPers. gasta- ‘offensive’ (NPers. gast ‘bad’), fr. a root seen in gandh- ‘hit, in- jure’, Lith. gesti, gendu ‘spoil’, etc. Walde-P. 1.672 f.
Av. bud- ‘become aware of’, ‘feel’ (hunger, etc.), and ‘smell’, sbs. baoga- baodi- ‘good smell, fragrance’ (cf. NPers. sb. bu, vb. buzdan ‘smell’) : Skt. budh- ‘be awake’, ‘become aware of’. Walde- P. 2.147. Barth. 917 f.
15.25, 26. Aristotle (De anim. 2.9) remarked on the lack of any independent classification of smells analogous to that of tastes (as ‘sweet, bitter’, etc.), and the
situation is the same today. There is still neither an accepted scientific class! fication nor a popular classification re flected in common speech, that is truly distinctive of the sense of smell.
The only widespread popular distinction 18
==== 2nd ====
Boh, Sp ete, ef,
» heg. of valjan ‘honest, : valjati ‘be worth’.
any (also ‘ugly, misshapen’, ol. szpetny ‘ugly, nasty’) fr.
igitized by Arya Samaj Foundation Chennai and eGangotri
x; TEMPERAMENTAL, MORAL, AESTHETIC NOTIONS 1179
pata ‘ugliness’, this, with generalization through ‘physical defect’, fr. pat ‘spa- vin’, fr. NHG spatid. Brickner 553.
Russ. plochoj (now perh. the most common word) : Pol. ptochy ‘negligent, careless’, ChSl. plachi ‘wavering, timid’, etc., perh. fr. the root in Grk. 74\hw ‘sway, swing, shake’. Walde-P. 2.52.
Russ. chudoj (also ‘lean, worn out’) : Ch8&l. chudi ‘little, needy, paltry’ (12.56), Boh. chudy ‘poor’ (11.52), ete. Walde-P. 1.502. Berneker 405.
Russ. durnoj (also ‘ugly’) : dur’ ‘fool- ishness, caprice’, Pol. dur ‘swoon, sense- lessness’, etc., Grk. @o3pos ‘rushing, raging, furious’. Walde-P. 1.842. Ber- neker 239.
8. Skt. pdpa-, prob. redupl. nursery word (like Grk. zama?, wézox ‘alas’) fr. the root in Grk. rfua ‘evil, misfortune, hurt’, etc. Walde-P. 2.8.
Skt. asddhu-, abhadra-, Av. avanhu-, neg. cpds. of the words for ‘good’ (16.71)
Av. aka- (NPers. ak ‘insult, misfor- tune’), etym.? Barth. 44f.
Av. aya- : Skt. agha- ‘mischief, guilt, wickedness’, and perh. Goth. agls ‘shameful’, Ir. dil ‘insult’, ete. Walde- P. 1.41. Barth. 47 f.
Av. aara-, mostly in a#ra- mainyu- ‘evil spirit, Ahriman’ : Av. qsta- ‘hate, enmity’, root connection? Walde 1.134. Barth, 103 f.
OPers. gasta- (‘repugnant’ or already ‘bad’, as NPers. gast), pple. of root in Skt. gandha- ‘smell’ (obj.), Av. ganii- NPers. gand ‘stench’ (15.23).
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
| | | q |
Digitized by Arya Samaj Foundation Chennai and eGangotri
1180 SELECTED INDO-EUROPEAN SYNONYMS
16.73 RIGHT (adj., in moral sense, vs, Wrong) Grk. — dlxatos Goth. garaihts Lith.
NG _ txatos ON rétir Lett. fake Lat.  itistus (réctus) Dan. ret ChSl.  pravidins It. giusto (retto) Sw. ratt SCr. pray Fr. Juste OE riht Boh. — pravy Sp. justo ME rigt, right Pol. prawy Rum. drept, just NE right Russ. pravyj
```


## [2026-09-06T14:57:50.573Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5085,5100p' IEC.txt; echo \"=== SKT ===\"; grep -n \"^Quaver\\|^Quiver\\|^Baptize\\|^Baptism\\|Quaver,\\|Quiver,\" SKT.txt | head"
}
```


### [2026-09-06T14:57:50.654Z] TOOL RESULT

```
ghür-(1) *sway, rollick, revel'. Cf. ghül- and gür- (1). Evidence ambig. Skt. (ambig.) ghür- nàmi (‘sway’, but equally to ghül-, q. v.); Cz. hytit, v. (2) ‘reveľ, but see gür-; (R cf. elo girla ‘estuary’, but equally to gür-, q. v.); Latv. cf. güra ‘strutter, flamboyant person?
ghür- (ghüro, io) (2) (expressive variant: ghurr-) ‘growl’ Skt. cf. ghurghurayah, adj. ‘growling’; Per. yur- ram ‘roar’; Arm. goram ‘growl’ beside grgram ‘caw’; MHG gurren ‘growl’; OE gyrran ‘grunt, creak, clatter’.
ghuros ‘outflow, filth, matter’. Cf. &huuo (1) (For Gk. i-khór *gore, matter, serum', see uis and ghuuo); Lat. (?) dial. foria (‘thin excre- ment’, for *horia?); Ir. gur, gor ‘pus, abscess’; Br. gor, pl. -iu, f. abscess; W gori 'suppura- tion’; OE gor, gyr (dirt, mud’; E gore; G Gur ‘dung; filthy water from coalmining'; ON gyrja (bloodstain': Lat. foria?); Sw. gorr ‘pus’; OCS cf. voz-grja (ómucus', fr. uos-, q.v. + ghurio); Cz. voz-her, m. ‘mucus, snot
ghus- (gheus-) “noise, sound”. Cf. WP I, 566 & 569 Skt. ghusah ‘resounding’; ghusyah "to be noised abroad); ghustah ‘sounded, noised" beside ghosah ‘noise’; ghosami ‘resound’; ON guss ‘fuss’; gussa, v. ‘resound’ beside gjósa, v. ‘erupt’
Gu
guabh- ‘swallow, engulf, immerse’. WP I, 674 Av. jaiwis ‘deep’; Gk. báptō ‘dip, dye, wash’; baphé ‘immersion’; cf. Hes. bákhtho húdatos ‘quaff water; MHG er-queben ‘choke’; E to quaff ‘drink in gulps’; ON kvefja ‘immerse, drown’; Sw. kväva ‘stifle’; kvaf ‘sultry; anxie- ty; Norw. cf. kvamne ‘choke while eating’,
45
A
for *kvabna-, cf. hamn ‘haven’; extn. in Skt. gabhiráh, adj. ‘deep’; Per. Zarf, id.; Oss. Kurf, quif, id. guabhro- *twist, turn'
Lat. (once) vabrum, adj. n. “varied?” beside (dial.) vafer *wily'; E quaver, s. & v. beside ME quavien ‘shake’; G cf. quabbeln ‘shake like a jelly
351
guaduå ‘chatter; a chattering bird’ Oss. cf. qäza (‘waterfowl’, fr. *guadio?); Alb. gadé (‘heron’, beside gaté and gac, id.); Ir. badhbh ‘crow’; G cf. quasseln ‘chatter’
guådh- ‘deep; depth, plunge, immerse’. Var- iant: guádhsio-, guadhsio Skt. gahe, mp. ‘plunge’; gadhah (1) ‘deep’; Gk. béssa, Dor. bàssa, f. ‘glen’; Ir. bádhaim, bái- dhim *immerse, drown’; W boddi, 3s. bawdd ‘drown’; Br. boezi, tr. & intr. id.; Cor. büdhy, id. Variant in Skt. gadhah & Gk. bé&ssa beside Doric (*-à- in) básson ‘deeper’: LLat. (Gallo- Lat.?) bassus ‘low’; W, Cor. bas “low, shallow’; W bais, mpl. ‘flats, mudshallows'. (NB: the sense of ‘shallow’ is also present in Skt. gad- háh adj. and gadhám, n. id. and in Srb. gaz
“ford”, gaziti, v. id.) l guādhs- ‘squeeze, tight, close’ Skt. gådhah (2) ‘close, tight’; Alb. cf. ngos (‘sate’, fr. *en-guadhs- ?); LLat. (Osc. or Gallo- L.?) bassus (1) ‘thick, fat’; G quetschen, MHG quetzen, MLG quetsen ‘squeeze’ (*-à-). Bas- sus was a com. R. name.
(guadhus ‘deep, low’ only in Gk. bathús, id. See guādh-)
guag- (1) ‘fluctuate, flag, flounder, waver’. (The evidence is ambig. cf. uag-) Lat. (ambig.) vagus ‘roving, random, un- steady’; vagārī ‘wander, waver, fluctuate’; Hes. bagaios “empty, idle, vain’; OE cwacian ‘wag, shake’: E quake; Li. cf. gõglinti ‘moon around, gawp'; fr. *guag- (?) but cf. also gožiù, góZti ‘rampage, run wild”, fr. *gua$-?, beside (ex- pressive) gvagZdü, -eti “pine away, fail
=== SKT ===
15368:Quaver.  (E.)  Frequent  of  ^wotv, M.  E.  quaufn  (M  =  t/).  to  quake.  Allied to  M.  £.  quappen,  to  throb»  palpitate. (Base  KWAP,  allied  to  KWAK )  Sec Quake.  I>er.  quaver,  sb..  a  note  in mufeic,  orig.  a  trill,  shake.  And  see quiver  (i).
```


## [2026-09-06T14:58:01.803Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 9759bef4c6a7a138 b1c9d399c68860a9 0ae7aa4802a87d44; do echo \"##### $f\"; sed -n '1,80p' $f.txt | grep -v \"^ *$\" | head -30; echo; done"
}
```


### [2026-09-06T14:58:03.748Z] TOOL RESULT

```
##### 9759bef4c6a7a138
URL: https://www.etymonline.com/word/baptize
FETCHED: 2026-09-06T14:56:37Z
STATUS: 200
TITLE: Baptize - Etymology, Origin & Meaning
Baptize - Etymology, Origin & Meaning 
 Search 
 Log in 
 Columns 
 Forum 
 Apps 
 Premium 
 Log in 
 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
 Origin and history of baptize 
 baptize (v.) 
 "to administer the rite of baptism to," c. 1300, from Old French batisier "be baptized; baptize; give a name to" (11c.), from Latin baptizare , from Greek baptizein "immerse, dip in water," also figuratively, "be over one's head" (in debt, etc.), "to be soaked (in wine);" in Christian use, "baptize." This is from baptein "to dip, steep, dye, color," which is perhaps from PIE root *gwabh- (1) "to dip, sink." Christian baptism originally was a full immersion. Related: Baptized ; baptizing .
 also from c. 1300 
 Entries linking to baptize 
 baptise (v.) 
 chiefly British English spelling of baptize ; for spelling, see -ize . Related: Baptised ; baptising .
 baptism (n.) 
 "initiatory sacrament of the Christian faith, consisting in immersion in or application of water by an authorized administrator," c. 1300, bapteme , from Old French batesme, bapteme "baptism" (11c., Modern French baptême ), from Latin baptismus , from Greek baptismos , noun of action from baptizein (see baptize ). The -s- was restored in late 14c.
 The signification, qualifications, and methods of administration have been much debated. The figurative sense of "any ceremonial ablution as a sign of purification, dedication, etc." is from late 14c. Old English used fulluht in this sense (John the Baptist was Iohannes se Fulluhtere ).
 Phrase baptism of fire "a soldier's first experience of battle" (1857) translates French baptême de feu ; the phrase originally was ecclesiastical Greek baptisma pyros and meant "the grace of the Holy Spirit as imparted through baptism;" later it was used of martyrdom, especially by burning.
 baptist 
 unbaptized 
 See All Related Words (4) 
 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
 More to explore

##### b1c9d399c68860a9
URL: https://www.etymonline.com/word/quaver
FETCHED: 2026-09-06T14:56:37Z
STATUS: 200
TITLE: Quaver - Etymology, Origin & Meaning
Quaver - Etymology, Origin & Meaning 
 Search 
 Log in 
 Columns 
 Forum 
 Apps 
 Premium 
 Log in 
 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
 Origin and history of quaver 
 quaver (v.) 
 early 15c., quaveren , "to vibrate, tremble, have a tremulous motion," probably a frequentative of cwavien "to tremble, shake, be afraid" (early 13c.), which probably is related to Low German quabbeln "tremble," and possibly of imitative origin. With Germanic verbal suffix indicating repeated or diminutive action (see -er (4)). The meaning "sing in trills or quavers, sing with a tremulous tone" is recorded by 1530s. Related: Quavered ; quavering .
 also from early 15c. 
 quaver (n.) 
 1560s, in music, "an eighth-note," from quaver (v.). Sense of "a shake or trill in singing" is from 1610s; meaning "a tremble in the voice" is by 1748.
 also from 1560s 
 Entries linking to quaver 
 demisemiquaver (n.) 
 "musical note half the value of a semiquaver , 32nd note," 1706; see demi- + semi- + quaver (n.). A semiquaver (also demiquaver) was a 16th note.
 hemidemisemiquaver (n.) 
 "sixty-fourth note" in music, 1846, from hemi- + demi- + semi- + quaver (n.).
 quake 
 quiver 
 semiquaver 
 -er 

##### 0ae7aa4802a87d44
URL: https://www.etymonline.com/word/quiver
FETCHED: 2026-09-06T14:56:38Z
STATUS: 200
TITLE: Quiver - Etymology, Origin & Meaning
Quiver - Etymology, Origin & Meaning 
 Search 
 Log in 
 Columns 
 Forum 
 Apps 
 Premium 
 Log in 
 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
 Origin and history of quiver 
 quiver (v.) 
 "to tremble, shake tremulously, shudder," late 15c., perhaps imitative, or possibly an alteration of quaveren (see quaver ), or from quiver (adj.) "active, agile, lively, brisk" (mid-13c.), from Old English cwifer- (in cwiferlice "zealously"), which is perhaps related to cwic "alive" (see quick (adj.)). Compare Middle Dutch kuyveren "to tremble." Related: Quivered ; quivering . As a noun, "act or state of quivering," by 1715, from the verb.
 also from late 15c. 
 quiver (n.) 
 "case for holding arrows," early 14c., from Anglo-French quiveir , Old French quivre , cuivre , probably of Germanic origin, from Proto-Germanic *kukur "container" (source also of Old High German kohhari , German Köcher , Old Saxon kokar , Old Frisian koker , Old English cocur "quiver"); "said to be from the language of the Huns" [Barnhart]. Related: Quiverful .
 also from early 14c. 
 Entries linking to quiver 
 quaver (v.) 
 early 15c., quaveren , "to vibrate, tremble, have a tremulous motion," probably a frequentative of cwavien "to tremble, shake, be afraid" (early 13c.), which probably is related to Low German quabbeln "tremble," and possibly of imitative origin. With Germanic verbal suffix indicating repeated or diminutive action (see -er (4)). The meaning "sing in trills or quavers, sing with a tremulous tone" is recorded by 1530s. Related: Quavered ; quavering .
 quick (adj.) 
 Middle English quik , from Old English cwic "living, alive, animate, characterized by the presence of life" (now archaic), and figuratively, of mental qualities, "rapid, ready," from Proto-Germanic *kwikwaz (source also of Old Saxon and Old Frisian quik , Old Norse kvikr "living, alive," Dutch kwik "lively, bright, sprightly," Old High German quec "lively," German keck "bold"), from PIE root *gwei- "to live." Sense of "lively, active, swift, speedy, hasty," developed by c. 1300, on notion of "full of life."
 NE 
 swift or the now more common 
 fast may apply to rapid motion of any duration, while in 
 quick (in accordance with its original sense of 'live, lively') there is a notion of 'sudden' or 'soon over.' We speak of a
```


## [2026-09-06T14:58:44.303Z] TOOL CALL #54: Bash

```json
{
 "command": "sed -n '1,80p' tools/verify_check.py"
}
```


### [2026-09-06T14:58:44.347Z] TOOL RESULT

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
```


## [2026-09-06T14:58:46.593Z] TOOL CALL #55: Bash

```json
{
 "command": "sed -n '80,140p' tools/verify_check.py"
}
```


### [2026-09-06T14:58:46.639Z] TOOL RESULT

```
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


## [2026-09-06T14:58:49.611Z] AGENT

Now I'll write the verification file.


## [2026-09-06T15:05:39.109Z] TOOL CALL #56: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/page-204.json",
 "content": "{\n  \"pdf_page\": 204,\n  \"book_page\": 174,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-06\",\n  \"entries\": [\n    {\n      \"entry\": 2,\n      \"root\": \"Gwebh 1\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *gʷebʰ- (also written *gʷeh₂bʰ-) 'to dip, sink, submerge'\",\n      \"note\": \"Pokorny 465f. prints exactly 'gʷebh- (oder gʷābh-?), gʷəbh- \\\"eintauchen, versenken, versinken\\\"' — the root, the language label (Indo-European) and the gloss 'to dip, sink' are all correct, and Nourai's POK:465 is the page where the article begins (it runs onto 466). Watkins/AHD has the same root as 'gʷébh-¹. To dip, sink' with Pok. 465. Mann (IEC 351) writes it guabh- 'swallow, engulf, immerse' and, unlike Pokorny, puts the Iranian 'deep' words (Av. jafra-, Pers. žarf) under it — which is Nourai's arrangement. Wiktionary's current reconstruction is *gʷeh₂bʰ- 'to dive (in)'. The one caveat, discussed at node #1, is that Pokorny himself files Av. jafra- under a 'possibly related' nasal variant *gʷembʰ-.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *gʷebʰ- (بازسازی امروزی‌تر: *gʷeh₂bʰ-) به معنی «فروبردن، غوطه‌ور کردن، فرورفتن». پوکورنی (ص ۴۶۵–۴۶۶) همین ریشه را با همین معنی آورده و واتکینز در پیوستِ ریشه‌های هندواروپاییِ AHD نیز آن را با ارجاع به همان صفحهٔ پوکورنی تکرار کرده است. برچسب زبان و معنایی که نورایی داده درست است. تنها نکته آن است که پوکورنی صورت اوستایی jafra- را زیر گونهٔ خیشومیِ *gʷembʰ- («شاید هم‌ریشه») می‌گذارد، حال آنکه مان و ویکی‌واژه آن را مستقیماً ذیل همین ریشه می‌آورند — یعنی چیدمان نورایی با پژوهش امروزی سازگار است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%CE%B2%CE%AC%CF%80%CF%84%CF%89\",\n        \"https://www.etymonline.com/word/baptize\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:465\", \"status\": \"supports\", \"note\": \"POK_02.txt line ~1822 (leaf 121, printed p.465): \\\"gʷebh- (oder gʷābh-?), gʷəbh- ,eintauchen, versenken, versinken'. Gr. βάπτω ,tauche ein', βαφῆναι, βαφή ,das Eintauchen, Färben'\\\" — the article opens on p.465 and continues on 466, exactly as cited.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"POK\", \"where\": \"Bd. I pp. 465-466 (POK_02.txt leaf 121-122)\", \"stance\": \"supports\", \"note\": \"\\\"gʷebh- ... ,eintauchen, versenken, versinken'\\\" with Gk. βάπτω and ON kafa 'tauchen', kvefja 'untertauchen, ersticken'.\"},\n        {\"src\": \"WLD\", \"where\": \"Bd. I 674 (WLD_Bd1_pages.txt ~line 63840)\", \"stance\": \"supports\", \"note\": \"Walde-Pokorny I 674 carries the same article ('anord. kvefja ... trans. \\\"niederdrücken, untertauchen, ersticken\\\"'), and it is the WP reference Pokorny prints at the foot of the entry ('WP. I 674').\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. gʷébh-¹ (AHD_watkins1985.txt line 540)\", \"stance\": \"supports\", \"note\": \"\\\"gʷébh-¹. To dip, sink. Suffixed zero-grade form *gʷabh-yo- in Greek baptein, to dip: (BAPTIST), BAPTIZE; ANABAPTIST. [Pok. gʷébh- 465.]\\\"\"},\n        {\"src\": \"IEC\", \"where\": \"Mann p.351, s.v. guabh-\", \"stance\": \"supports\", \"note\": \"\\\"guabh- 'swallow, engulf, immerse'. WP I, 674: Av. jaiwiš 'deep'; Gk. báptō 'dip, dye, wash' ... extn. in Skt. gabhiráh, adj. 'deep'; Per. žarf, id.; Oss. ǧurf, quif, id.\\\" — Mann groups the Greek and the Iranian 'deep' words under one root, as Nourai's chart does.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"jafra\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Young Avestan jafra- 'deep' is well attested (Yt. 10.14 yahmya jafra varəyō 'in which are deep waters'; Yt. 5.49 varəiš … jafrahe 'of the deep lake'; also the bahuvrīhi jaiwi-vafra- 'having deep snow' and jafnu- 'hollow, depression'). Its j- is the Avestan reflex of PIE *gʷ before a front vowel (*gʷe- > Av. je-/ja-), and -fr- continues *-bʰr-; Sanskrit shows the nasal-infixed by-form gabhīrá-/gambhīrá- 'deep', where g- is generalised from the zero/o-grade. Nourai's arrow (PIE 'to dip, sink' → Av. 'deep') is the semantics of 'sunk down' → 'deep'. Pokorny (466) hedges: he prints jafra- not under gʷebh- proper but under 'eine vielleicht verwandte, aber nur die Bed. \\\"tief\\\" aufweisende Wurzel *gʷ(e)mbh-'; Mann (IEC 351) and current Wiktionary (s.v. βάπτω) instead list Av. jafra alongside Gk. baptein under the one root *gʷeh₂bʰ-, which is Nourai's grouping.\",\n          \"derivation_fa\": \"«jafra-» در اوستای نو به معنی «ژرف، عمیق» بارها به کار رفته است (یشت ۱۰٫۱۴ «yahmya jafra varəyō» و یشت ۵٫۴۹ «varəiš … jafrahe»)، و در ترکیب jaiwi-vafra- «دارای برف ژرف» و jafnu- «گودی» نیز دیده می‌شود. آغازهٔ j- بازتاب اوستاییِ *gʷ هندواروپایی پیش از واکهٔ پیشین است و -fr- دنبالهٔ *-bʰr-؛ در سنسکریت گونهٔ خیشومیِ gabhīrá-/gambhīrá- «ژرف» آمده است. تحول معنایی «فرورفتن» ← «ژرف» طبیعی است. بارتولومه (ستون ۴۹۳ به بعد و مدخل varay-) این صورت‌ها را ثبت کرده و مان و ویکی‌واژه آن را دقیقاً هم‌ریشهٔ βάπτω یونانی می‌دانند؛ اما پوکورنی خودِ jafra- را ذیل گونهٔ خیشومیِ *gʷembʰ- «شاید هم‌ریشه» آورده است. ادعای نورایی در مجموع درست است، با این ملاحظه.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%CE%B2%CE%AC%CF%80%CF%84%CF%89\"],\n          \"ref_check\": [\n            {\"ref\": \"POK:466\", \"status\": \"partial\", \"note\": \"POK_02.txt line 1840 (leaf 123 = printed p.466) does carry jafra- on the cited page: \\\"av. jaiwi-vafra- Adj. ,mit tiefem Schnee', jafra- ,tief', jafnu-s ,Vertiefung, Einsenkung'\\\" — but introduced as \\\"Eine vielleicht verwandte, aber nur die Bed. ,tief' aufweisende Wurzel *gʷ(e)mbh-, *gʷm̥bh-\\\", i.e. Pokorny attaches it to a possibly-related nasal root rather than to gʷebh- itself.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"Altiranisches Wb., s.v. varay- and Yt.5.49/Yt.10.14 citations (BRT.txt lines 8494, 11100, 22796)\", \"stance\": \"supports\", \"note\": \"\\\"yahmya jafra varayō (NPm.)\\\" Yt.10.14 and \\\"pasne varōiš *āuθaitahe jafrahe\\\" Yt.5.49 — Bartholomae records jafra- as a genuine Avestan adjective 'tief'; cf. jafnu- s.v.\"},\n            {\"src\": \"HUB\", \"where\": \"Persische Studien p.184\", \"stance\": \"supports\", \"note\": \"\\\"in: zd. gafya- ,Tiefe', jafra- ,tief', jafnu- ,Tiefe' von arisch gap, jap neben zd. jaiwi- ,tief' … skr. gabhīrá-, gambhīrá- ,tief' von arisch gabh, jabh (idg. gʷembh, gʷm̥bh)\\\" — Hübschmann too puts jafra- with the (nasal) gabh/jabh group.\"},\n            {\"src\": \"IEC\", \"where\": \"Mann p.351 s.v. guabh-\", \"stance\": \"supports\", \"note\": \"\\\"Av. jaiwiš 'deep'; Gk. báptō 'dip, dye, wash' … Per. žarf, id.\\\" — the Iranian 'deep' words are placed under the same root as Greek báptō.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I 674\", \"stance\": \"partial\", \"note\": \"Walde-Pokorny I 674 has the same wording as Pokorny: \\\"Eine vielleicht verwandte, aber nur die Bed. ,tief' aufweisende Wz. *gʷembh- … av. jaiwi-vafra- … jafra- ,tief', jafnu-s\\\".\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"žafr\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"A Middle Iranian continuant of Av. jafra- is certainly there, but the shape depends on the dialect. Book Pahlavi has zwpl = zofr 'deep' (MacKenzie, PHD p.98: 'zofr [zwpl | M zwwpr, J zwrf, (N zarf)] deep'), with the regular Southwest-Iranian development *ǰ- > z-. The form with initial ž- and the sequence -afr, i.e. žafr, is Parthian: Manichaean Parthian 𐫋𐫜𐫡 jfr /žafr/ 'deep' (so Wiktionary s.v. ژرف, which derives NP žarf from a Middle Persian *žarf borrowed from that Parthian word, 'displacing native zofr'). Horn (Grundriss no. 685, p.152) writes the Middle Iranian ancestor as 'phlv. zufar, zafr'; Mo'in's footnote in Borhan (p.1059ff.) writes 'پهلوی zafr'. So Nourai's 'Pahlavi žafr' is a real form, but the ž- belongs to Parthian (and to New Persian), not to Book Pahlavi, where it is z-.\",\n          \"derivation_fa\": \"دنبالهٔ فارسی میانهٔ jafra- اوستایی هست، اما ریختِ آن بسته به گویش فرق می‌کند: در پهلویِ کتابی zwpl یعنی zofr «ژرف» آمده است (مکنزی، فرهنگ کوچک پهلوی، ص ۹۸: «zofr [zwpl | M zwwpr, J zwrf, (N zarf)] deep»)، با تحول قاعده‌مندِ *ǰ- ایرانی باستان به z- در فارسی میانه. صورت با ژ آغازین، یعنی žafr، پارتی است: پارتیِ مانوی jfr /žafr/ «ژرف». هرن (بند ۶۸۵، ص ۱۵۲) نیای این واژه را «phlv. zufar، zafr» می‌نویسد و معین نیز در حاشیهٔ برهان «پهلوی zafr» آورده است. پس صورتی که نورایی داده واقعی است، ولی ژ آغازینِ آن از پارتی (و فارسی نو) است نه از پهلوی کتابی؛ ادعا با احتیاط پذیرفتنی است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%DA%98%D8%B1%D9%81\"],\n          \"ref_check\": [\n            {\"ref\": \"FVA:293\", \"status\": \"not_checked\", \"note\": \"FVA = S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), 1368/1989; refs_online.json records that no digital copy exists on any permitted platform (re-searched 2026-09), local_file null. Cannot be consulted.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie p.98 s.v. zofr (PHD_mackenzie.txt line 5842)\", \"stance\": \"partial\", \"note\": \"\\\"zofr [zwpl | M zwwpr, J zwrf, (N zarf)] deep\\\" — the Book Pahlavi form is zofr, not žafr; MacKenzie nonetheless links it to NP zarf/žarf.\"},\n            {\"src\": \"HRN\", \"where\": \"Grundriss no. 685, p.152 (HRN.txt line 6040, leaf 173)\", \"stance\": \"supports\", \"note\": \"\\\"685. žerf 'tief' … aw. jafra- 'tief'; phlv. zufar, zafr\\\" — Horn gives precisely the Avestan → Pahlavi zafr → NP žerf chain Nourai draws, but with z-.\"},\n            {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II (glossary), searched zofr/zafr/žafr\", \"stance\": \"silent\", \"note\": \"grep 'zofr|zafr|jafr' in NYB_vol2_glossary.txt returns nothing; the word does not occur in Nyberg's text corpus.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"žarf «ژرف ( ژرفا )»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"New Persian ژرف žarf 'deep' (with the abstract ژرفا žarfā 'depth', formed with the -ā suffix as in پهنا, درازا) continues the Middle Iranian word by metathesis of the cluster: Old/Middle Iranian -fr- > NP -rf-, exactly the change Hübschmann sets out as a sound law (Persische Studien p.266, §c: 'Ap. fr ~ np. rf: barf \\\"Schnee\\\" = phl. vafr = zd. vafra-; žarf \\\"tief\\\" = zd. jafra-'). Horn (no. 685) gives žerf and Judaeo-Persian ژרף (Isaiah 29:15). The initial ž- (rather than z-) points to the Parthian/Northwestern form žafr rather than to Book Pahlavi zofr. Ferdowsī's line quoted in the chart, یکی ژرف دریاست بن ناپدید / در گنج رازش ندارد کلید, is the same verse Mo'in prints in his footnote to Borhan-e Qāṭeʿ. Nourai's chain Av. jafra > MIr. žafr/zafr > NP žarf is the standard account.\",\n          \"derivation_fa\": \"«ژرف» فارسی نو (و مصدرِ حاصلیِ «ژرفا» با پسوند ـا مانند پهنا و درازا) از راهِ قلبِ خوشهٔ همخوانی به دست آمده است: -fr- ایرانی به -rf- فارسی نو بدل شده؛ هوبشمان (پژوهش‌های پارسی، ص ۲۶۶) این را قاعده‌ای آوایی می‌داند و مثال می‌زند: «barf = پهلوی vafr = اوستایی vafra-؛ žarf = اوستایی jafra-». هرن (بند ۶۸۵) صورت žerf و گونهٔ یهودی‌فارسیِ آن را از اشعیا ۲۹:۱۵ می‌آورد. ژِ آغازین نشان می‌دهد که میانجی، صورتِ شمال‌غربی/پارتیِ žafr بوده است نه zofr پهلویِ کتابی. بیت فردوسی که نورایی نقل کرده («یکی ژرف دریاست بن ناپدید…») همان بیتی است که معین در حاشیهٔ برهان قاطع آورده. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%DA%98%D8%B1%D9%81\"],\n          \"ref_check\": [\n            {\"ref\": \"BQT:1059\", \"status\": \"supports\", \"note\": \"BQT_v2_pages.txt leaf 521 (printed p. ≈1059-1064 by the vol-2 offset printed ≈ leaf+543) carries the entry ژرف with Mo'in's footnote: «اوستا jafra- (عمیق)، پهلوی zafr … پازند (پهلوی) … دراوراق مانوی…، هنینگ، فهرست لغات پارسی میانه» and the very Ferdowsī verse «یکی ژرف دریاست بن ناپدید ـ در گنج رازش ندارد کلید»; a further note derives ژرفا from ژرف + ا (حاصل مصدر) 'چون پهنا، درازا'.\"},\n            {\"ref\": \"HRN:152\", \"status\": \"supports\", \"note\": \"HRN.txt line 6040 = leaf 173 = printed p.152: \\\"685. žerf 'tief', [Judaeo-Persian] ژרף (Is. 29,15), žerfī. aw. jafra- 'tief'; phlv. zufar, zafr. kurd. ziǝr, zaza žōr; afγ. zavar; bal. juhl, n. jahl\\\" — the cited page is exactly this entry.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HUB\", \"where\": \"Persische Studien p.266 (HUB.txt line 9541)\", \"stance\": \"supports\", \"note\": \"\\\"c) Ap. fr ~ np. rf: barf 'Schnee' = phl. vafr = zd. vafra-; žarf 'tief' = zd. jafra- (aber zafar, zafr 'Rachen', das nicht urspr. persisch ist (§111) = zd. zafar-)\\\" — Hübschmann derives žarf from jafra- by metathesis and warns against confusing it with the (non-Persian) zafr 'maw'.\"},\n            {\"src\": \"IEC\", \"where\": \"Mann p.351 s.v. guabh-\", \"stance\": \"supports\", \"note\": \"\\\"extn. in Skt. gabhiráh, adj. 'deep'; Per. žarf, id.; Oss. ǧurf, quif, id.\\\"\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie p.98 s.v. zofr\", \"stance\": \"supports\", \"note\": \"\\\"zofr … (N zarf) deep\\\" — MacKenzie explicitly gives New Persian zarf/žarf as the descendant.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Greek\",\n          \"words\": \"baptein\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Ancient Greek βάπτειν (pres. βάπτω) 'to dip, steep, dye' goes back to a suffixed zero-grade *gʷabʰ-yé-ti of the root, via Proto-Hellenic *gʷáptyō: PIE *gʷ gives Greek b before a non-front vowel (labiovelar > labial), and *-bʰy- yields -πτ- by the usual assibilation/assimilation of the yod-present. Derivatives βαφή 'dipping, dyeing', βαπτίζειν 'immerse'. Watkins (AHD, s.v. gʷébh-¹) states the derivation in exactly these terms, and Pokorny prints βάπτω at the head of the entry on p.465-466.\",\n          \"derivation_fa\": \"فعل یونانی باستان βάπτειν / βάπτω «فروبردن، در رنگ زدن» از ستاکِ درجهٔ صفرِ *gʷabʰ-yé-ti می‌آید که از راهِ یونانیِ آغازین *gʷáptyō به βάπτω رسیده است: *gʷ هندواروپایی در یونانی پیش از واکهٔ غیرپیشین به b بدل می‌شود و خوشهٔ *-bʰy- در فعل‌های یایی به -πτ- می‌انجامد. مشتق‌های آن βαφή «فروبردن، رنگرزی» و βαπτίζειν «غوطه‌ور کردن» است. واتکینز در پیوستِ AHD همین را می‌گوید و پوکورنی نیز βάπτω را در سرِ همان مدخل ص ۴۶۵–۴۶۶ آورده است. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%CE%B2%CE%AC%CF%80%CF%84%CF%89\"],\n          \"ref_check\": [\n            {\"ref\": \"POK:466\", \"status\": \"supports\", \"note\": \"The gʷebh- article runs 465-466 and opens with \\\"Gr. βάπτω ,tauche ein', βαφῆναι, βαφή ,das Eintauchen, Färben'\\\" (POK_02.txt leaf 121, printed p.465, continuing on 466 with makedon. βαβρήν etc.).\"},\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt line 540: \\\"gʷébh-¹. To dip, sink. Suffixed zero-grade form *gʷabh-yo- in Greek baptein, to dip: (BAPTIST), BAPTIZE; ANABAPTIST. [Pok. gʷébh- 465.]\\\"\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"IEC\", \"where\": \"Mann p.351 s.v. guabh-\", \"stance\": \"supports\", \"note\": \"\\\"Gk. báptō 'dip, dye, wash'; baphé 'immersion'\\\" under guabh- 'swallow, engulf, immerse'.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein 1971 s.v. baptize\", \"stance\": \"supports\", \"note\": \"\\\"baptize … fr. Eccles. L. baptizāre, 'to baptize', fr. Gk. βαπτίζειν\\\" and s.v. baptist \\\"fr. Gk. βαπτιστής, 'one who dips'\\\".\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I 674\", \"stance\": \"supports\", \"note\": \"The Walde-Pokorny article the Pokorny entry cites ('WP. I 674') contains the same Greek material.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"English\",\n          \"words\": \"Baptist\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Greek βαπτιστής 'one who dips (in water)', agent noun of βαπτίζειν, was taken into Ecclesiastical Latin as baptista (the epithet of John the Baptist in the Vulgate), thence Old French baptiste, and into Middle English by c.1300; the denominational sense 'member of a Protestant body practising believers' baptism by immersion' dates from the 1610s. Klein and the AHD index both trace BAPTIST to gʷébh-¹; the route is Greek → Church Latin → Old French → English, an uncontroversial chain.\",\n          \"derivation_fa\": \"واژهٔ انگلیسی Baptist از یونانیِ βαπτιστής «آن که [در آب] فرومی‌برد» می‌آید، اسم فاعلِ βαπτίζειν، که در لاتینِ کلیسایی به شکل baptista (لقبِ یحیای تعمیددهنده در وولگاتا) درآمد و از راه فرانسهٔ باستان baptiste نزدیک سال ۱۳۰۰ میلادی وارد انگلیسی میانه شد؛ معنای فرقه‌ایِ آن («باپتیست‌ها») از سدهٔ هفدهم است. کلاین و نمایهٔ AHD هر دو این واژه را به همان ریشهٔ *gʷebʰ- بازمی‌گردانند. زنجیرهٔ یونانی ← لاتینِ کلیسایی ← فرانسهٔ باستان ← انگلیسی بی‌مناقشه است و ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/baptize\"],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The chart gives no reference for this node; the parent Greek node cites POK:466 and AHD, and the AHD index line 1276 confirms 'Baptist gʷébh-¹'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein 1971 s.v. baptist (line 25802)\", \"stance\": \"supports\", \"note\": \"\\\"baptist, n. — OF. (= F.) baptiste, fr. Eccles. L. baptista, fr. Gk. βαπτιστής, 'one who dips'.\\\"\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985, English index line 1276\", \"stance\": \"supports\", \"note\": \"\\\"Baptist gʷébh-¹\\\" (and line 1278 \\\"BAPTIZE gʷébh-¹\\\").\"},\n            {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/baptize\", \"stance\": \"supports\", \"note\": \"\\\"from Latin baptizare, from Greek baptizein 'immerse, dip in water' … This is from baptein 'to dip, steep, dye, color,' which is perhaps from PIE root *gwabh- (1) 'to dip, sink'.\\\"\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 3,\n      \"root\": \"Gwebh 2\",\n      \"verdict\": \"plausible\",\n      \"modern_form\": \"PIE (2.) *gʷeb(ʰ)- 'slimy, flabby; eelpout, toad' — an expressive/onomatopoeic base\",\n      \"note\": \"Pokorny 466 does have '2. gʷeb(h)- ,schleimig, schwabbelig, Quappe, Kröte'', so Nourai's root name, language label, gloss and page are all right. Both Pokorny and Watkins, however, mark it as barely a root: Pokorny 'Vermutlich onomatopoetisch; doch ist mit der Möglichkeit zu rechnen, daß ein altes Wort für Frosch erst im Germ. in die lautmalende Sippe hineingezogen wurde', and AHD calls it 'Hypothetical base of some Germanic words associated with the notion of sliminess'. Hence 'plausible' rather than 'confirmed'. Its whole non-Germanic evidence is Baltic and Slavic (Old Prussian gabawo 'toad', OCS žaba) — there is no Iranian member at all, which is the source of the error at node #1.\",\n      \"note_fa\": \"پوکورنی در ص ۴۶۶ همین مدخل را دارد: «2. gʷeb(h)- «لزج، لق‌ولق، ماهیِ قورباغه‌ای، وزغ»»، پس نام ریشه و معنا و شمارهٔ صفحه‌ای که نورایی داده درست است. اما هم پوکورنی و هم واتکینز آن را ریشه‌ای سست می‌شمارند: پوکورنی می‌نویسد «احتمالاً نام‌آوا (onomatopoeia) است» و AHD آن را «پایه‌ای فرضی برای شماری واژهٔ ژرمنی مربوط به مفهوم لزجی» می‌خواند؛ از این رو حکم «با احتیاط پذیرفتنی است». گواهِ غیرژرمنیِ آن تنها بالتی و اسلاوی است (پروسیِ باستان gabawo «وزغ»، اسلاویِ کهن žaba)، و هیچ عضو ایرانی ندارد — و همین سرچشمهٔ خطای گرهِ نخست این مدخل است.\",\n      \"sources\": [\"https://www.etymonline.com/word/quaver\"],\n      \"ref_check\": [\n        {\"ref\": \"POK:466\", \"status\": \"supports\", \"note\": \"POK_02.txt leaf 123 (printed p.466): \\\"2. gʷeb(h)- ,schleimig, schwabbelig, Quappe, Kröte'. Vermutlich onomatopoetisch … Asächs. quappa … ndd. quabbeln ,vor Fettigkeit zittern'; apr. gabawo ,Kröte' (*gʷ(e)b(h)-); slav. *gebā ,Kröte': in aksl. žaba … WP. I 674.\\\"\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. I 674-675 (WLD_Bd1_pages.txt ~line 63920)\", \"stance\": \"supports\", \"note\": \"\\\"2. gʷeb(h)- ,schleimig, schwabbelig, Quappe, Kröte'. Vermutl. letzlich onomatopoetisch … ndd. quabbeln ,vor Fettigkeit zittern'. Preuß. gabawo ,Kröte'\\\".\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. gʷébh-² (line 540)\", \"stance\": \"partial\", \"note\": \"\\\"gʷébh-². Hypothetical base of some Germanic words associated with the notion of sliminess. 1. Middle Dutch quac-, unguent, liquid … 2. Low German quabbeln, to shake like jelly, tremble, akin to Middle English quaven, to tremble: QUAVER. [Pok. 2. gʷébh- 466.]\\\" — same root, but Watkins keeps only the Germanic words and drops the toad.\"},\n        {\"src\": \"IEC\", \"where\": \"Mann p.351 s.v. guabhro-\", \"stance\": \"partial\", \"note\": \"\\\"guabhro- 'twist, turn': Lat. (once) vabrum … E quaver, s. & v. beside ME quavien 'shake'; G cf. quabbeln 'shake like a jelly'\\\" — Mann files quaver/quabbeln under a different root and does not recognise a 'slime/toad' root at all.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Old Persian\",\n          \"words\": \"gabawo\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"There is no Old Persian word gabawo, and none is attested for 'toad' at all. The form on the page comes from Pokorny p.466, where the line reads 'apr. gabawo \\\"Kröte\\\" (*gʷ(e)b(h)-)': 'apr.' is Pokorny's abbreviation for altpreußisch, Old PRUSSIAN, the Baltic language, not for Old Persian (which Pokorny abbreviates 'apers.', as on the very next page, 'apers. gasta- \\\"eklig, widerwärtig\\\"'). Walde-Pokorny I 675 spells it out in full: 'Preuß. gabawo \\\"Kröte\\\"'. Old Prussian gabawo (Elbing Vocabulary) is a Baltic word, cognate with Old Church Slavonic žaba, Russian žába 'toad' (< Balto-Slavic *geb-/*gēb-). The printed page (PDF 204) does read 'Old Persian … gabawo : toad', so the extraction is faithful and the misreading of the abbreviation is Nourai's own; the whole node should be relabelled Old Prussian, and with it disappears the only Iranian member of this root.\",\n          \"derivation_fa\": \"در پارسی باستان نه واژه‌ای به شکل gabawo هست و نه اصلاً واژه‌ای برای «وزغ» ثبت شده است. این صورت از پوکورنی ص ۴۶۶ گرفته شده که در آنجا آمده: «apr. gabawo ,Kröte' (*gʷ(e)b(h)-)»؛ اما apr. کوتاه‌نوشتِ altpreußisch یعنی «پروسیِ باستان» (زبانی بالتی) است، نه پارسی باستان — که پوکورنی آن را apers. می‌نویسد، چنان‌که در همان صفحهٔ بعد «apers. gasta-» آمده. والده-پوکورنی (جلد ۱، ص ۶۷۵) همین را به‌صراحت «Preuß. gabawo ,Kröte'» نوشته است. پروسیِ باستان gabawo (واژه‌نامهٔ البینگ) هم‌ریشهٔ اسلاوی کهن žaba و روسی žába «وزغ» است. تصویر صفحهٔ چاپی (ص ۱۷۴ کتاب) نشان می‌دهد که خودِ کتاب «Old Persian» چاپ کرده است؛ پس خطا از نویسنده است نه از استخراج داده. پژوهش امروزی این گره را رد می‌کند: باید «پروسیِ باستان» باشد، و با این تصحیح تنها عضو ایرانیِ این ریشه از میان می‌رود.\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"Old Persian ▯ POK:466 | gabawo : toad\",\n          \"correct_form\": \"Old Prussian gabawo 'toad' (Baltic; Pokorny's 'apr.' = altpreußisch)\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"POK:466\", \"status\": \"contradicts\", \"note\": \"POK_02.txt leaf 123, printed p.466: \\\"apr. gabawo ,Kröte' (*gʷ(e)b(h)-); slav. *gebā ,Kröte': in aksl. žaba, russ. žába, skr. žȁba, usw.\\\" — 'apr.' = altpreußisch. The cited page contains no Old Persian word; two lines further on (p.466 bottom, under gʷedh-) Pokorny writes 'apers. gasta-' with the different abbreviation.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"WLD\", \"where\": \"Bd. I 675\", \"stance\": \"contradicts\", \"note\": \"\\\"Preuß. gabawo ,Kröte'\\\" — Walde-Pokorny writes 'Preuß.' in full, removing any doubt that the language is Old Prussian.\"},\n            {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon pp.164-215 (KNT.txt)\", \"stance\": \"silent\", \"note\": \"grep 'gabawo|gabaw|toad' in KNT.txt returns nothing; Kent's Old Persian lexicon has no such word.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. gʷébh-²\", \"stance\": \"contradicts\", \"note\": \"Watkins lists only Middle Dutch quac- and Low German quabbeln under this base — no Iranian, and no toad.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": null,\n          \"words\": \"\",\n          \"verdict\": \"unverified\",\n          \"derivation\": \"An empty pass-through box: the printed page (PDF 204) shows a blank rectangle drawn to the right of the 'Old Persian gabawo' box, with no language label, no reference and no word in it — evidently a slot the author left unfilled (there is no Persian reflex of a Baltic word for 'toad'). The extraction is faithful to the page; there is nothing to verify.\",\n          \"derivation_fa\": \"این گره جعبه‌ای تهی است: در صفحهٔ چاپی (ص ۱۷۴) کنارِ جعبهٔ «Old Persian gabawo» مستطیلی خالی کشیده شده که نه برچسب زبان دارد، نه ارجاع و نه واژه — ظاهراً جایی است که نویسنده آن را پر نکرده (و طبعاً برای واژه‌ای بالتی به معنی «وزغ» بازتاب فارسی وجود ندارد). استخراج با صفحهٔ چاپی مطابق است و چیزی برای راستی‌آزمایی نیست.\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"(an empty box, no language label, no word)\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference is printed in the box.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BOOK\", \"where\": \"printed page 174 = PDF page 204 (data/verification/sources/refs/ocr/BOOK/204.png)\", \"stance\": \"silent\", \"note\": \"The rendered page confirms an empty rectangle to the right of the gabawo box.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Germanic\",\n          \"words\": \"quabbeln\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"quabbeln 'to shake like jelly, tremble' is Low German (niederdeutsch)/dialectal German, not Proto-Germanic: Pokorny 466 lists 'ndd. quabbeln \\\"vor Fettigkeit zittern\\\"' beside Swedish dial. kvabba, Danish dial. kvappe, alongside the nouns Old Saxon quappa 'eelpout', Dutch kwab(be) 'flab, wattle', Icelandic kvap 'jelly'. Watkins gives the gloss Nourai copies word for word: 'Low German quabbeln, to shake like jelly, tremble'. Nourai's language label 'Germanic' is therefore a loose cover-term for a West Germanic (Low German) expressive verb; the form, gloss and attachment to the root are right.\",\n          \"derivation_fa\": \"quabbeln «مانند ژله لرزیدن» واژه‌ای از آلمانیِ سفلی (niederdeutsch) و گویشی است، نه از ژرمنیِ آغازین: پوکورنی در ص ۴۶۶ آن را چنین می‌آورد «ndd. quabbeln ,vor Fettigkeit zittern'» در کنار سوئدیِ گویشی kvabba و دانمارکیِ گویشی kvappe و نام‌هایی چون ساکسونیِ کهن quappa، هلندی kwab(be) و ایسلندی kvap «ژله». واتکینز نیز دقیقاً همان معنایی را می‌دهد که نورایی رونویسی کرده است: «Low German quabbeln, to shake like jelly, tremble». پس برچسب «ژرمنی» تعمیمی سهل‌انگارانه برای فعلی از شاخهٔ ژرمنیِ غربی است، اما صورت و معنا و پیوندش با ریشه درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/quaver\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD:1519\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt line 540, s.v. gʷébh-²: \\\"2. Low German quabbeln, to shake like jelly, tremble, akin to Middle English quaven, to tremble: QUAVER.\\\" Nourai's gloss is verbatim from this entry; p.1519 falls inside the gʷ- stretch of the 1975 New College appendix (pp.1505-1550), so the page reference is consistent.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"Bd. I 466\", \"stance\": \"supports\", \"note\": \"\\\"schwed. dial. kvabba, ndd. quabbeln ,vor Fettigkeit zittern'\\\".\"},\n            {\"src\": \"KLN\", \"where\": \"Klein 1971 s.v. quaver\", \"stance\": \"supports\", \"note\": \"\\\"Cp. LG. quappig, 'puffy, swelled', Du. kwabbig, 'flabby', G. quabbeln, 'to wobble, shake, quake', which all are imitative.\\\"\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I 675\", \"stance\": \"supports\", \"note\": \"\\\"ndd. quabbeln ,vor Fettigkeit zittern'\\\" in the same list.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"English\",\n          \"words\": \"quaver, quiver\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"quaver (v.) is well placed here: early 15c. quaveren 'to vibrate, tremble', a frequentative in -er of Middle English cwavien/quaven 'to tremble' (early 13c.), which is related to Low German quabbeln; Pokorny p.466 himself lists 'engl. quaver \\\"zittern, vibrieren\\\"' in this article and the AHD index has 'QUAVER gʷébh-²'. quiver (v.) is the weaker half: Klein calls it simply 'a var. of quaver', which is Nourai's basis, but Etymonline and Watkins prefer to keep it apart — 'late 15c., perhaps imitative, or possibly an alteration of quaveren, or from quiver (adj.) \\\"active, agile, lively, brisk\\\" (mid-13c.), from Old English cwifer- (in cwiferlice \\\"zealously\\\"), which is perhaps related to cwic \\\"alive\\\"', i.e. from PIE *gʷeyh₃- 'to live' (Pokorny 468 already lists 'engl. quiver \\\"lebhaft, hurtig\\\"' under 3. gʷei-). The node is therefore right for quaver, uncertain for quiver; per the worse-of-the-two rule it is 'plausible'.\",\n          \"derivation_fa\": \"واژهٔ quaver «لرزیدن، تحریر خواندن» به‌درستی اینجا جای گرفته است: از آغاز سدهٔ پانزدهم میلادی quaveren، ساختی تکراری با پسوند -er از انگلیسی میانهٔ cwavien/quaven «لرزیدن» (سدهٔ سیزدهم)، هم‌خانوادهٔ quabbeln آلمانیِ سفلی؛ خودِ پوکورنی در ص ۴۶۶ «engl. quaver» را در همین مدخل آورده و نمایهٔ AHD نیز «QUAVER gʷébh-²» دارد. اما quiver «لرزیدن» سست‌تر است: کلاین آن را «گونه‌ای از quaver» می‌داند (و همین مبنای کار نورایی است)، ولی اتیمانلاین و واتکینز آن را جدا نگاه می‌دارند و ترجیح می‌دهند از صفتِ quiver «چابک، سرزنده» از انگلیسی کهن cwifer- بدانند که با cwic «زنده» پیوند دارد، یعنی از ریشهٔ *gʷeyh₃- «زیستن» (پوکورنی ص ۴۶۸ نیز «engl. quiver ,lebhaft, hurtig'» را ذیل 3. gʷei- آورده است). پس برای quaver درست و برای quiver با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/quaver\",\n            \"https://www.etymonline.com/word/quiver\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The chart gives no reference for this node; the parent Germanic box cites AHD:1519, whose entry names QUAVER (but not quiver) as the English outcome.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein 1971 s.v. quaver and quiver (lines 197984, 198698)\", \"stance\": \"supports\", \"note\": \"\\\"quaver, intr. and tr. v. — ME. quaveren, freq. of quaven, which is prob. of imitative origin. Cp. LG. quappig … G. quabbeln … Cp. also quiver, v.\\\"; \\\"quiver, intr. v., to tremble … — A var. of quaver (q.v.)\\\" — Klein supports both.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict. s.v. Quaver (SKT.txt line 15368)\", \"stance\": \"supports\", \"note\": \"\\\"Quaver. (E.) Frequent. of quave, M.E. quaven … to quake. Allied to M.E. quappen, to throb, palpitate. (Base KWAP, allied to KWAK.) See Quake. … And see quiver (1).\\\"\"},\n            {\"src\": \"POK\", \"where\": \"Bd. I 466 and 468\", \"stance\": \"partial\", \"note\": \"p.466 has \\\"engl. quaver ,zittern, vibrieren'\\\" under 2. gʷeb(h)-, but p.468 lists \\\"engl. quiver ,lebhaft, hurtig'\\\" under 3. gʷei- 'leben' — Pokorny splits the two words.\"},\n            {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/quiver\", \"stance\": \"partial\", \"note\": \"\\\"quiver (v.) … late 15c., perhaps imitative, or possibly an alteration of quaveren (see quaver), or from quiver (adj.) 'active, agile, lively, brisk' … from Old English cwifer- … perhaps related to cwic 'alive'.\\\"\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 4,\n      \"root\": \"Gwedh\",\n      \"verdict\": \"plausible\",\n      \"modern_form\": \"PIE *gʷedʰ- 'to push, hurt, destroy' (Pokorny); the Indo-Iranian 'smell/stink' words may in fact be a non-IE borrowing\",\n      \"note\": \"Pokorny 466f. has exactly 'gʷedh- ,stoßen, verletzen, zerstören'' with the whole Iranian file Nourai reproduces: 'ai. gandh- \\\"stoßen, stechen, verletzen, zerstören\\\", gandhá-ḥ m. \\\"Geruch, Duft\\\", av. gantay- \\\"Gestank\\\", mpers. gand \\\"Gestank\\\", apers. gasta- \\\"eklig, widerwärtig\\\", afgh. γandal, bal. gandag \\\"schlecht\\\"' plus Lith. gendù, gèsti 'be spoiled'. So the root name, gloss, language label and page are all correct, and Buck (SYN 15.23, p.1024) repeats the same account. The reservation is modern: Cheung (Etymological Dictionary of the Iranian Verb, s.v. *gant, p.103f.) sets the PIE column to '—' and writes that 'the Ir. root *gant- (and Skt. gandh-) can hardly be of IE origin … The strange dental \\\"alternation\\\" in the Skt. and Ir. roots points to borrowing', explicitly rejecting Pokorny's Greek comparanda (ὄδεννος, φθόνος) as 'not compelling'. Hence 'plausible': the Indo-Iranian family tree drawn on the page is right, its attachment to an Indo-European root is not certain.\",\n      \"note_fa\": \"پوکورنی در ص ۴۶۶–۴۶۷ همین مدخل را دارد: «gʷedh- «زدن، آسیب رساندن، ویران کردن»» و همان پروندهٔ ایرانی را می‌آورد که نورایی بازنویسی کرده است: «سنسکریت gandh-، gandhá-ḥ «بو»؛ اوستایی gantay- «بوی بد»؛ فارسی میانه gand «بوی بد»؛ پارسی باستان gasta- «نفرت‌انگیز»؛ پشتو γandal؛ بلوچی gandag «بد»» و نیز لیتوانیایی gèsti «تباه شدن». پس نام ریشه، معنا، برچسب زبان و شمارهٔ صفحه درست است و باک (فرهنگ مترادف‌ها، بند ۱۵٫۲۳، ص ۱۰۲۴) نیز همین را می‌گوید. اما تحفظ امروزی این است که چونگ در فرهنگ ریشه‌شناختی فعل ایرانی (ذیل *gant، ص ۱۰۳) ستونِ هندواروپایی را خالی می‌گذارد و می‌نویسد ریشهٔ ایرانیِ *gant- و سنسکریت gandh- «به‌سختی می‌تواند هندواروپایی باشد» و «تناوبِ عجیبِ دندانی در این دو ریشه نشان از وام‌گیری دارد». بنابراین: درخت هندوایرانیِ این صفحه درست است، ولی پیوند آن به ریشه‌ای هندواروپایی قطعی نیست.\",\n      \"sources\": [\"https://abadis.ir/fatofa/%DA%AF%D8%B3%D8%AA/\"],\n      \"ref_check\": [\n        {\"ref\": \"POK:466\", \"status\": \"supports\", \"note\": \"POK_02.txt leaf 123-124 (printed pp.466-467): \\\"gʷedh- ,stoßen, verletzen, zerstören'. Ai. gandh- ,stoßen, stechen, verletzen, zerstören' (bei Grammatikern), gandhá-ḥ m. ,Geruch, Duft', av. gantay- ,Gestank', mpers. gand ,Gestank', apers. gasta- ,eklig, widerwärtig', afgh. γandal ,Ekel empfinden', bal. gandag ,schlecht'.\\\"\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"CHEUNG\", \"where\": \"Etym. Dict. of the Iranian Verb, s.v. *gant 'to smell badly, stink', p.103f.\", \"stance\": \"partial\", \"note\": \"Gives the whole Iranian family exactly as charted (YAv. ganti-, OP gasta- '= Kent: 183b', MMP gngyy, BMP gandag, Parth. gnd'g/gst, Sogd. γnt, NP gand) but writes \\\"*PIE — = LIV: — | Pok.: 466 f.\\\" and \\\"The Ir. root *gant- (and Skt. gandh-) can hardly be of IE origin.\\\"\"},\n        {\"src\": \"SYN\", \"where\": \"Buck 15.23 SMELL, p.1024\", \"stance\": \"supports\", \"note\": \"\\\"Skt. gandha- : Av. ganti- 'bad smell', OPers. gasta- 'offensive' (NPers. gast 'bad'), fr. a root seen in gandh- 'hit, injure', Lith. gesti, gendu 'spoil', etc. Walde-P. 1.672 f.\\\" — Buck's account is Pokorny's and Nourai's.\"},\n        {\"src\": \"WLD\", \"where\": \"Bd. I 672f. (cited as the WP reference of the Pokorny article)\", \"stance\": \"supports\", \"note\": \"Pokorny closes the entry 'WP. I 672 f., Benveniste BSL. 38, 143'; Buck cites the same 'Walde-P. 1.672 f.' for the etymology.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"gantay, ganti, gainti\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All three shapes are genuine: Bartholomae's headword is 'gantay- f. \\\"übler Geruch, Gestank\\\"' (Altiranisches Wörterbuch col. 493), the stem-form ganti- is the usual citation form, and gaiṇti- is the epenthetic Young Avestan spelling of the same word in the actual passages — 'yat aša *gaiṇtiš upanhacaiti' (Vd. 7.56) and '*gaiṇtiš vīdvārəmnō' (H. 2.25) — with the derivative duz-gaiṇti- 'evil-smelling' (AiW 757). The word is a ti-abstract *gan-ti- 'a striking (of the nose)' from the root *gan(dʰ)- 'to strike, hurt', the same semantic path as OHG stinkan 'to smell/stink' beside Gothic stigqan 'to collide', which Pokorny cites on p.466 as the parallel. Nourai's node reproduces Pokorny and Bartholomae accurately.\",\n          \"derivation_fa\": \"هر سه صورت واقعی‌اند: سرمدخلِ بارتولومه «gantay- (مؤنث) «بوی بد، گَند»» است (فرهنگ ایرانی باستان، ستون ۴۹۳)؛ ganti- ریختِ ستاکیِ همان واژه است؛ و gaiṇti- املای اوستای نو با میانجی‌واکه است که در خودِ متن‌ها می‌آید (وندیداد ۷٫۵۶ و هادخت ۲٫۲۵)، در کنار مشتقِ duz-gaiṇti- «بدبو» (ستون ۷۵۷). این واژه اسم مصدرِ *gan-ti- از ریشهٔ *gan(dʰ)- «زدن، آسیب زدن» است؛ همان مسیر معنایی که پوکورنی در ص ۴۶۶ با نمونهٔ آلمانی کهنِ stinkan «بو دادن» در برابر گوتیک stigqan «برخورد کردن» نشان می‌دهد. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"POK:466\", \"status\": \"supports\", \"note\": \"POK_02.txt leaf 123 printed p.466: \\\"av. gantay- ,Gestank'\\\" heads the Iranian material of the gʷedh- article.\"},\n            {\"ref\": \"SYN:1024\", \"status\": \"supports\", \"note\": \"SYN.txt line 26001, section 15.23 SMELL (printed p.1024): \\\"Skt. gandha- : Av. ganti- 'bad smell', OPers. gasta- 'offensive' (NPers. gast 'bad'), fr. a root seen in gandh- 'hit, injure'.\\\"\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch col. 493 (BRT.txt line 9995) and col. 757 (line 13837)\", \"stance\": \"supports\", \"note\": \"\\\"gantay- f. ,übler Geruch, Gestank': yat aša *gaiṇtiš upaŋhacaiti V.7.56; *gaiṇtiš(ca) vīdvārəmnō H.2.25\\\" and \\\"duz-gantay- Adj. ,übelriechend, stinkend'\\\" — both of Nourai's variant spellings are Bartholomae's.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"s.v. *gant, p.103\", \"stance\": \"supports\", \"note\": \"\\\"*AVESTAN: YAv. ganti- (f) 'bad smell' (V 7.56), YAv. duz-gainti- 'smelling badly' (H 2.25)\\\".\"},\n            {\"src\": \"HRN\", \"where\": \"Grundriss no. 934, p.208-209 (HRN.txt line 8115)\", \"stance\": \"supports\", \"note\": \"\\\"aw. gaiṇti- 'Gestank'; phlv. gand 'Gestank', gandak 'stinkend', gandakīh; ai. gandhá- 'Geruch, Duft'.\\\"\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"gand «گند»; gandîdan «گندیدن»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"New Persian گند gand 'stench' continues Middle Persian gand [gnd] 'stench' (MacKenzie p.35; Manichaean MP gngyy, Parthian gnd'g 'stinking') without change; the Avestan ti-stem gaiṇti- and the MP noun both go back to Old Iranian *gandi-/*ganda-. گندیدن gandīdan 'to rot, to stink' is a New Persian denominative built on that noun with the productive infinitive suffix -īdan (cf. ترسیدن, خندیدن), attested from the classical period; the participle گنده gande 'putrid' is the same stem + -a. Mo'in's etymological footnote in Borhan-e Qāṭeʿ p.1841 gives precisely this file: «اوستا gaiṇti (بوی متعفن)، پهلوی gand, gandag (گنده)، هندی باستان gandha، افغانی ganda، بلوچی gandag، پارسی باستان gasta- (نفرت‌آور)». Nourai's arrow Avestan → Persian is right in substance (the actual route runs through Middle Persian, which the chart leaves out here).\",\n          \"derivation_fa\": \"«گند» فارسی نو دنبالهٔ بی‌واسطهٔ فارسی میانهٔ gand [gnd] «بوی بد» است (مکنزی ص ۳۵؛ فارسی میانهٔ مانوی gngyy، پارتی gnd'g «بدبو»)؛ هم اسم اوستاییِ gaiṇti- و هم اسم فارسی میانه به ایرانیِ باستانِ *gandi-/*ganda- بازمی‌گردند. «گندیدن» فعلی است که در فارسی نو از همان اسم با پسوند سازندهٔ مصدرِ ـیدن ساخته شده (مانند ترسیدن و خندیدن) و از دورهٔ کلاسیک گواه دارد؛ صفتِ «گنده» نیز همان ستاک + ـه است. معین در حاشیهٔ برهان قاطع (ص ۱۸۴۱) دقیقاً همین پرونده را می‌آورد: «اوستا gaiṇti (بوی متعفن)، پهلوی gand, gandag (گنده)، هندی باستان gandha (بو، عطر)، افغانی ganda، بلوچی gandag، پارسی باستان gasta- (نفرت‌آور)». پس ادعای نورایی درست است؛ تنها حلقهٔ فارسی میانه در نمودار نیامده است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"BQT:1841\", \"status\": \"supports\", \"note\": \"BQT_v3_pages.txt leaf 637 = [pdf page 638], running head ۱۸۴۱: entry «گند - بفتح اول و سکون ثانی و دال ابجد. بوی بد را گویند» with Mo'in's footnote 8 «اوستا gaiṇti (بوی متعفن)، پهلوی gand، gandag (گنده)، هندی باستان gandha (بو، عطر [خوشبو])، افغانی ganda، بلوچی gandag … پارسی باستان gasta- (نفرت‌آور). استق ۹۳۶ و رک: هوبشمان ۹۳۴» — the cited page is exactly this entry, and it also lists «گندیده» on the same page.\"},\n            {\"ref\": \"HRN:208\", \"status\": \"supports\", \"note\": \"HRN.txt line 8115, Grundriss no. 934 (the entry straddles pp.208-209): \\\"aw. gaiṇti- 'Gestank'; phlv. gand 'Gestank', gandak 'stinkend', gandakīh; ai. gandhá- 'Geruch, Duft' … bal. LW. gand 'Kot, Mist'\\\".\"},\n            {\"ref\": \"SYN:1179\", \"status\": \"supports\", \"note\": \"SYN.txt line 29729, printed page 1179 (running head 'TEMPERAMENTAL, MORAL, AESTHETIC NOTIONS 1179'), section 16.72 BAD: \\\"OPers. gasta- ('repugnant' or already 'bad', as NPers. gast), pple. of root in Skt. gandha- 'smell' (obj.), Av. ganti- NPers. gand 'stench' (15.23).\\\"\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie p.35 (PHD_mackenzie.txt lines 2444-2451)\", \"stance\": \"supports\", \"note\": \"\\\"gand [gnd | N ~] stench. gandag [gndk' | (M gng), N ~a] foul, stinking. ~īh: stench.\\\" — plus duš-gand [dwšgnd] 'stinking' s.v. duš-.\"},\n            {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II, s.v. gandakēh (NYB_vol2_glossary.txt line 1621)\", \"stance\": \"supports\", \"note\": \"\\\"gandakēh [gndkyh] stench. — Cf Av. (493) ganti-; MPrth gndgyft, cf gnd'g 'fetid'; MPrs gngyy; Paz. gandai, cf gand 'stench', gandaa 'fetid'; NP gand, ganda 'anything putrid', gandagi 'filth'.\\\"\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e Rishe-hā, entry گند (ARY_pages.txt ~[pdf page 443])\", \"stance\": \"supports\", \"note\": \"The entry lists اوستایی GAṆTI / پارسی باستان GASTA / پهلوی GAND, GANDAG / بلوچی / افغانی and cites «برهان قاطع ۱۸۴۱» — the very page Nourai cites.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"s.v. *gant, p.103f.\", \"stance\": \"supports\", \"note\": \"\\\"*NWIR: Kurd. ganin/gan- 'to rot', NP gand 'stench', NP gandah 'fetid, stinking, rotten' … *MIDDLE PERSIAN: MMP gngyy 'stench', BMP gndk(-) /gandag(-)/.\\\"\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Sogdian\",\n          \"words\": \"gnc\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Gharib's Sogdian dictionary has the word at entry 4125: 'γnc(h) B — γanc — <Av. gaiṇti — f. adj. bad smelling', attested in the Buddhist texts TSP 2.636, 712, 793. Nourai's 'gnc' is the same transliteration with g for the Sogdian γ (Buddhist Sogdian writes the voiced velar fricative with the letter that transliterates as γ/g). The relation to Avestan is one of common inheritance rather than descent — Sogdian γanc and Av. gaiṇti- both continue Old Iranian *ganti- — but this is exactly how Gharib himself puts it ('<Av. gaiṇti'), so the arrow reproduces the cited source. Cheung adds the cognate Sogdian forms CSogd. γnt 'stench', BSogd. γnt''k 'bad, evil'.\",\n          \"derivation_fa\": \"در فرهنگ سغدیِ بدرالزمان قریب، مدخل ۴۱۲۵: «γnc(h) B — γanc — <Av. gaiṇti — صفت مؤنث — بدبو»، با شواهدی از متن‌های بودایی (TSP ۲٫۶۳۶، ۷۱۲، ۷۹۳). آنچه نورایی «gnc» نوشته همان است، با g به جای γ سغدی. پیوند این واژه با اوستایی از راهِ میراثِ مشترک است نه اشتقاق مستقیم — γanc سغدی و gaiṇti- اوستایی هر دو دنبالهٔ ایرانیِ باستانِ *ganti- اند — اما خودِ قریب نیز همین‌گونه نوشته («<Av. gaiṇti»)، پس پیکانِ نمودار با منبعِ استنادشده می‌خواند. چونگ نیز صورت‌های سغدیِ مسیحی γnt «گَند» و سغدی بودایی γnt''k «بد، شریر» را می‌افزاید. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"SOD:164\", \"status\": \"supports\", \"note\": \"SOD_pages.txt line 15492, entry no. 4125 on leaf 229 (printed page ≈163-164 by Gharib's offset printed ≈ leaf−66): \\\"4125 γnc(h) B / γanc ⊙ <Av. gaiṇti ⊙ f. adj. bad smelling / TSP 2,636, 712, 793\\\" — Nourai's page number lands on this entry, and Gharib's own etymological note is the arrow Nourai draws.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"CHEUNG\", \"where\": \"s.v. *gant, p.103, Sogdian section\", \"stance\": \"supports\", \"note\": \"\\\"*SOGDIAN: CSogd. γnt 'stench', SSogd. γnt'kw, BSogd. γnt''k, γnt'k, CSogd. γnt'q 'bad, evil' || (+ *a-) BSogd. ''γ'γnt- (caus.) 'to defile'.\\\"\"},\n            {\"src\": \"BRT\", \"where\": \"Altiranisches Wb. col. 493\", \"stance\": \"supports\", \"note\": \"The Avestan source-word Gharib points to, gantay-/gaiṇti- 'übler Geruch, Gestank', is Bartholomae's headword.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Old Persian\",\n          \"words\": \"gasta\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Old Persian gasta- 'repugnant, evil' is securely attested in the Achaemenid inscriptions: DNa 52 and 57f., XPh 57, A²Sa 5, A²Sd 4 and A²Ha 6 (Artaxerxes II, Hamadan: hacā vispā gastā 'from all evil'). Morphologically it is the past participle of the verb *gand- 'to smell (offensively)': the expected *gandta- is replaced by -sta- exactly as in basta- 'bound' beside Skt. baddhá- (Kent §85 — dental+dental gives st in Old Persian). Kent's lexicon entry is on p.183 and Cheung cites it there. The semantic step 'stinking' → 'repugnant, evil' is the one Latin shows in odium beside odor. Nourai's arrow root → OP gasta is Pokorny's own ('apers. gasta- \\\"eklig, widerwärtig\\\"', p.466).\",\n          \"derivation_fa\": \"«gasta-» پارسی باستان به معنی «نفرت‌انگیز، بد» در سنگ‌نبشته‌های هخامنشی گواهِ استوار دارد: DNa بند ۵۲ و ۵۷، XPh ۵۷، A²Sa ۵، و A²Ha ۶ (اردشیر دوم، همدان: «hacā vispā gastā» یعنی «از هر بدی»). از دید ساختواژی، صفت مفعولیِ فعلِ *gand- «بوی بد دادن» است: صورتِ منتظرهٔ *gandta- به gasta- بدل می‌شود، دقیقاً مانند basta- «بسته» در برابر baddhá- سنسکریت (کنت، بند ۸۵: خوشهٔ دو دندانی در پارسی باستان به st می‌انجامد). مدخلِ کنت در ص ۱۸۳ است و چونگ نیز به همان صفحه ارجاع می‌دهد. تحول معنایی «بدبو» ← «نفرت‌انگیز، بد» همان است که در لاتین میان odor و odium دیده می‌شود. پیکانِ نورایی از ریشه به gasta- عیناً از پوکورنی (ص ۴۶۶: «apers. gasta- ,eklig, widerwärtig'») گرفته شده است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"KNT:183\", \"status\": \"supports\", \"note\": \"KNT.txt line 5371 (Kent's Lexicon, p.183b — the page Cheung also cites as 'Kent: 183b'): \\\"gasta- adj. 'repugnant, evil'; nt. as sb., 'evil, harm': past pte. (§85, §242.I) of vb. *gant- *gandh- 'smell', Av. ganti- 'evil odor' (AIW 493), duž-gainti- 'evil-smelling' (AiW 757), Skt. gandhá- 'odor' … gastā nsf. DNa 57f.; gastā absn. DNa 52; XPh 57; A²Sa 5; A²Sd 4; A²Ha 6.\\\"\"},\n            {\"ref\": \"SYN:1024\", \"status\": \"supports\", \"note\": \"SYN.txt line 26001, printed p.1024 (§15.23): \\\"OPers. gasta- 'offensive' (NPers. gast 'bad')\\\".\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KNT\", \"where\": \"Kent §85 and §242.I (KNT.txt lines 1210, 2627)\", \"stance\": \"supports\", \"note\": \"\\\"pIE *gendh-: OP gasta- 'evil', cf. Skt. gandhá-\\\" and \\\"for basta- and gasta-, with participial -st- replacing -zdh-, see §85\\\" — the morphology of the form.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"s.v. *gant, p.103\", \"stance\": \"supports\", \"note\": \"\\\"*OLD PERSIAN: gasta- <g-s-t-a> (ppp.) 'evil, repugnant' = Kent: 183b\\\".\"},\n            {\"src\": \"POK\", \"where\": \"Bd. I 466\", \"stance\": \"supports\", \"note\": \"\\\"apers. gasta- ,eklig, widerwärtig'\\\" in the gʷedh- article.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"gasta\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"A Middle Iranian continuant of the participle is attested, but in Parthian rather than in Book Pahlavi: Cheung records 'Parthian … gst (old ppp.) \\\"loathsome, disgusting\\\"' (DMMPP 163a), and Ossetic I. gast, D. iǧæstæ shows the same old participle in the East. MacKenzie's Concise Pahlavi Dictionary has no gast/gasta at all (the Book Pahlavi words for the notion are gandag, gannāg 'foul, corrupt'), and Nyberg's glossary likewise has only gandakēh 'stench'. So Nourai's intermediate step is real as a Middle Iranian form, but the label 'Pahlavi' overstates the evidence; the New Persian word may equally continue the Parthian/Northwestern form directly. Mo'in (the reference given, MON:3314) is the only source Nourai cites for it.\",\n          \"derivation_fa\": \"دنبالهٔ این صفت مفعولی در دورهٔ میانه گواه دارد، اما در پارتی نه در پهلویِ کتابی: چونگ صورتِ پارتیِ «gst (صفت مفعولیِ کهن) «نفرت‌انگیز، مشمئزکننده»» را ثبت کرده است (DMMPP ۱۶۳a)، و آسیِ gast / iǧæstæ نیز همین صفت مفعولی کهن را در شرق نشان می‌دهد. اما در فرهنگ کوچک پهلویِ مکنزی هیچ gast/gasta نیست (واژه‌های پهلوی برای این مفهوم gandag و gannāg اند) و در واژه‌نامهٔ نیبرگ هم تنها gandakēh «گَند» آمده است. پس این حلقهٔ میانی به‌عنوان صورتی ایرانیِ میانه واقعی است، ولی برچسب «پهلوی» بیش از گواهِ موجود ادعا می‌کند؛ چه‌بسا «گست» فارسی نو مستقیماً دنبالهٔ صورتِ شمال‌غربی/پارتی باشد. با احتیاط پذیرفتنی است.\",\n          \"sources\": [\"https://abadis.ir/fatofa/%DA%AF%D8%B3%D8%AA/\"],\n          \"ref_check\": [\n            {\"ref\": \"MON:3314\", \"status\": \"partial\", \"note\": \"Mo'in's Farhang-e Fārsi is on disk only as the 2-vol Adena OCR, whose pagination differs from the 6-vol Amir Kabir edition Nourai cites, so p.3314 could not be opened directly; the entry itself was read through abadis.ir (فرهنگ معین section, s.v. گست): «زشت، قبیح، نازیبا: دلبرا دو رخ تو بس خوب است / از چه با یار کار گست کنی (عماره)». Mo'in confirms the word and its meaning; the online text of Mo'in does not reproduce the print edition's Latin-script Pahlavi form, so the specific claim 'Pahlavi gasta' could not be verified from this reference.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary (grep 'gast' in PHD.txt / PHD_mackenzie.txt)\", \"stance\": \"contradicts\", \"note\": \"No entry gast/gasta exists; the only 'gast' string in the dictionary is pargast [plgst'] 'let it not happen!'. MacKenzie's words for the notion are gandag 'foul, stinking' and gan(n)āg 'foul, corrupt'.\"},\n            {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II (glossary)\", \"stance\": \"silent\", \"note\": \"grep 'gast' returns nothing relevant; s.v. gandakēh Nyberg lists Paz. gandai, NP gand/ganda but no gast.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"s.v. *gant, p.103, Parthian and NEIR sections\", \"stance\": \"partial\", \"note\": \"\\\"*PARTHIAN: gnd'g 'stinking, smelling', gst (old ppp.) 'loathsome, disgusting' ⇐ DMMPP: 163a\\\"; \\\"Oss. I. gast, D. iǧæstæ 'desacration …; desacrated'\\\" — a Middle Iranian gast exists, but it is Parthian, not Book Pahlavi.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Persian\",\n          \"words\": \"gast «گست»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Classical New Persian گَست gast 'bad, ugly, repulsive' is well attested in the older lexica and poets: Borhan-e Qāṭeʿ and Asadi's Loghat-e Fors gloss it زشت، قبیح، نازیبا, and it is used by Rudaki's contemporary ʿAmmāre, by Ferdowsī ('دل و جان آن بدکنش گست باد'), by Suzanī and by Vis-o-Rāmin — the last being the verse the chart quotes, 'چه عاشق باشد اندر عشق، چه مست / کجا بر چشم او نیکی بود گست' (Dehkhodā prints نیکو for نیکی in the second hemistich). Formally it continues the old past participle *gasta- (OP gasta-, Parth. gst) with regular loss of the final vowel in New Persian; Buck states the equation outright, 'OPers. gasta- (\"repugnant\" or already \"bad\", as NPers. gast)'. The word died out in modern usage, surviving mainly in dictionaries and in the compound-like پرگست.\",\n          \"derivation_fa\": \"«گَست» در فارسیِ کلاسیک به معنی «زشت، قبیح، نازیبا» گواهِ فراوان دارد: برهان قاطع و لغت فرسِ اسدی همین معنا را می‌دهند و شاعرانی چون عمارهٔ مروزی، فردوسی («دل و جان آن بدکنش گست باد»)، سوزنی و سرایندهٔ ویس و رامین آن را به کار برده‌اند — و همان بیتِ ویس و رامین است که نورایی نقل کرده: «چه عاشق باشد اندر عشق، چه مست / کجا بر چشم او نیکی بود گَست» (دهخدا در مصراع دوم «نیکو» ضبط کرده است). از دید ساختواژی، دنبالهٔ صفت مفعولیِ کهنِ *gasta- است (پارسی باستان gasta-، پارتی gst) با افتادنِ قاعده‌مندِ واکهٔ پایانی در فارسی نو؛ باک این برابری را به‌صراحت می‌نویسد: «OPers. gasta- … as NPers. gast». این واژه در فارسی امروز از کاربرد افتاده و بیشتر در فرهنگ‌ها و در «پرگست» بازمانده است. ادعای نورایی درست است.\",\n          \"sources\": [\"https://abadis.ir/fatofa/%DA%AF%D8%B3%D8%AA/\"],\n          \"ref_check\": [\n            {\"ref\": \"MON:3314\", \"status\": \"supports\", \"note\": \"Read via abadis.ir (فرهنگ معین, s.v. گست): «زشت، قبیح، نازیبا: دلبرا دو رخ تو بس خوب است / از چه با یار کار گست کنی (عماره: شاعران بی‌دیوان: ۳۶۳)» — Mo'in has the headword with Nourai's gloss 'bad, ugly'; the page number itself could not be checked (see node #5).\"},\n            {\"ref\": \"SYN:1024\", \"status\": \"supports\", \"note\": \"SYN.txt line 26001, printed p.1024: \\\"OPers. gasta- 'offensive' (NPers. gast 'bad')\\\" — Buck names the New Persian word on the cited page.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"abadis.ir/fatofa/گست/ , section فرهنگ معین\", \"stance\": \"supports\", \"note\": \"«(صفت) ۱ - زشت، نازیبا، مقابل زیبا: چه عاشق باشد اندر عشق چه مست / کجا بر چشم او نیکو بود گست (ویس و رامین) ۲ - شرم‌آور، فضیح».\"},\n            {\"src\": \"BQT\", \"where\": \"Borhan-e Qāṭeʿ, s.v. گست, quoted by Dehkhodā via abadis.ir\", \"stance\": \"supports\", \"note\": \"«گست. [گَ] (ص) زشت. قبیح. نازیبا. (برهان) (از آنندراج). زشت. (لغت فرس اسدی) (جهانگیری)» with the Vis-o-Rāmin and Ferdowsī citations.\"},\n            {\"src\": \"SYN\", \"where\": \"Buck 16.72 BAD, p.1179\", \"stance\": \"supports\", \"note\": \"\\\"OPers. gasta- ('repugnant' or already 'bad', as NPers. gast), pple. of root in Skt. gandha- 'smell' (obj.), Av. ganti- NPers. gand 'stench' (15.23).\\\"\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie (grep 'gast')\", \"stance\": \"silent\", \"note\": \"No Book Pahlavi ancestor is listed; see node #5.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-09-06T15:05:39.137Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe/data/verification/page-204.json (file state is current in your context — no need to Read it back)
```


## [2026-09-06T15:05:42.964Z] TOOL CALL #57: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-204.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 204"
}
```


### [2026-09-06T15:05:45.590Z] TOOL RESULT

```
Exit code 1
Expecting ',' delimiter: line 323 column 665 (char 50362)
```


## [2026-09-06T15:05:47.722Z] TOOL CALL #58: Bash

```json
{
 "command": "sed -n '323p' data/verification/page-204.json | cut -c600-750"
}
```


### [2026-09-06T15:05:47.770Z] TOOL RESULT

```
nues the old past participle *gasta- (OP gasta-, Parth. gst) with regular loss of the final vowel in New Persian; Buck states the equation outright, 'O
```


## [2026-09-06T15:05:52.544Z] TOOL CALL #59: Bash

```json
{
 "command": "python3 - <<'PY'\np='data/verification/page-204.json'\ns=open(p,encoding='utf-8').read()\nold='''Buck states the equation outright, 'OPers. gasta- (\"repugnant\" or already \"bad\", as NPers. gast)'.'''\nnew='''Buck states the equation outright: OPers. gasta- (\\\\\"repugnant\\\\\" or already \\\\\"bad\\\\\", as NPers. gast).'''\nassert old in s\ns=s.replace(old,new)\nopen(p,'w',encoding='utf-8').write(s)\nPY\npython3 -m json.tool data/verification/page-204.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 204"
}
```


### [2026-09-06T15:05:54.513Z] TOOL RESULT

```
JSON OK
nodes verified: 15/15
node verdicts: {'confirmed': 10, 'plausible': 3, 'disputed': 1, 'unverified': 1}
root verdicts: {'confirmed': 1, 'plausible': 2}
ref checks: {'partial': 2, 'not_checked': 4, 'supports': 15, 'contradicts': 1}
books consulted: {'supports': 33, 'partial': 5, 'silent': 5, 'contradicts': 3} | by book: {'PHD': 5, 'CHEUNG': 5, 'WLD': 4, 'KLN': 4, 'BRT': 3, 'IEC': 3, 'NYB': 3, 'POK': 3, 'HUB': 2, 'HRN': 2, 'AHD': 2, 'Etymonline': 2, 'KNT': 2, 'BOOK': 1, 'SKT': 1, 'ARY': 1, 'MON': 1, 'BQT': 1, 'SYN': 1}
```


## [2026-09-06T15:06:12.225Z] AGENT

0 PROBLEM lines. Page 204 done.

**Page 204 (book p. 174) — 3 non-redirect entries, 15 nodes** (2 redirect entries skipped: Gwag, Gwâk, Gwěguos → Wag 2)

- Node verdicts: 10 confirmed, 3 plausible, 1 disputed, 1 unverified (empty box)
- Root verdicts: 1 confirmed (Gwebh 1), 2 plausible (Gwebh 2, Gwedh)
- Ref checks: 15 supports, 2 partial, 1 contradicts, 4 not_checked. 19 books consulted.

**Disputed**
- **Gwebh 2, node #1 "Old Persian gabawo 'toad'"** — Nourai misread Pokorny's abbreviation. POK 466 has `apr. gabawo` = *altpreußisch*, Old **Prussian** (Baltic, cognate of OCS žaba); Walde-Pokorny I 675 spells it out "Preuß. gabawo 'Kröte'". Pokorny writes Old Persian as `apers.` (e.g. `apers. gasta-` two lines later). Kent's OP lexicon has no such word. With this correction the root loses its only Iranian member. **The printed page really does say "Old Persian", so the extraction is faithful — the error is the book's** (`error_in: "book"`, page PNG saved to `data/verification/sources/refs/ocr/BOOK/204.png`).

**Plausible (with reasons)**
- Gwebh 1 #2 "Pahlavi žafr": the ž-form is Parthian (Man. `jfr` /žafr/); Book Pahlavi is `zofr` (MacKenzie), Horn p.152 prints `zufar, zafr`.
- Gwebh 2 #4 "quaver, quiver": quaver confirmed; quiver preferred by Etymonline/Watkins under *gʷeyh₃- 'live' (OE cwifer-, cwic), though Klein calls it a variant of quaver.
- Gwedh #5 "Pahlavi gasta": MacKenzie and Nyberg have no such Pahlavi word (only gandag/gannāg); the old participle survives as Parthian `gst` (Cheung).
- Root Gwedh: Pokorny 466 says exactly what Nourai says, but Cheung (s.v. *gant, p.103) sets PIE to "—" and holds the Ir./Skt. root "can hardly be of IE origin".
- Root Gwebh 2: both Pokorny ("vermutlich onomatopoetisch") and Watkins ("hypothetical base") treat it as barely a root.

**No extraction errors found** — the JSON matches the printed page throughout, including the deliberately empty box under `gabawo` (Gwebh 2 node #2). One minor variant worth noting, not an error: the chart's Vis-o-Rāmin verse reads `نیکی بود گست` where Dehkhodā/Moʿin print `نیکو`.

**Not checkable:** FVA:293 (Nahvi 1368) — no digital copy exists on any permitted platform. MON:3314 — the local Moʿin OCR is the 2-vol Adena edition with different pagination, so the entry was read via abadis.ir instead (confirms the word and gloss, not the Pahlavi form).
