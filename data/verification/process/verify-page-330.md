# Verification process log — verify-page-330


## [2026-09-07T16:10:04.187Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 330 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-330.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-330.json. Write /home/sfmqrb/git/rishe/data/verification/page-330.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 330` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T16:10:06.071Z] AGENT

I'll start by reading the instructions.


## [2026-09-07T16:10:06.770Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T16:10:06.787Z] TOOL RESULT

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


## [2026-09-07T16:10:07.253Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-330.txt"
}
```


### [2026-09-07T16:10:07.274Z] TOOL RESULT

```
1	=== PDF page 330 (book page 300) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Mel 3 : soft, soft material  (refs POK:716)
4	#1 (parent #0) [Greek] refs=POK:719 | malaxos : soft ; malagma : soft material
5	  #2 (parent #1) [Arabic] refs=KLN:58 | al-mâlâgmâ : the "soft" material
6	    #3 (parent #2) [Persian] refs=MON:4345 | malğam «ملغم» : paste, ointment | extra: ملغمه ، الغام
7	    #4 (parent #2) [French] refs=KLN:58 | amalgame
8	      #5 (parent #4) [English] refs=AHD | amalgam
9	#6 (parent #0) [Germanic] refs=AHD | meltan : to melt ; milks : mulch ; smelt, malta, mildja, milks
10	  #7 (parent #6) [English] refs=AHD | melt, smelt, malt, mild, mulch, enamel
11	#8 (parent #0) [Latin] refs=AHD | mollis : soft
12	  #9 (parent #8) [English] refs=AHD | mollusk
13	#10 (parent #0) [Celtic] refs=AHD | molto : sheep
14	  #11 (parent #10) [English] refs=AHD | mutton
15	--- entry 1 ---
16	ROOT [Indo-European] Mělg : to wipe off, to milk  (refs POK:722)
17	#1 (parent #0) [Avestan] refs=POK:722; FFD:77 | marz, marez, mrz, mard : to wipe, sweep, rub
18	  #2 (parent #1) [Persian] refs=BQT:1948,2010; HRN:214; SYN:569; MON:4010; SNS:245; FFD:77 | mâlîdan «مالیدن» : to rub ; moštan «مُشتن» : to rub, massage ; morz «مُرز ۲» : intercourse, also the anus, bottom | extra: ماله ، مالش، مال ؛ مُشت ۲ ؛ مُرزیدن
19	#3 (parent #0) [Avestan] refs=POK:722; BQT:1448; HRN:12 | â-marz : wipe out the sins, forgive ; fra-â-marz : one who forgives all sins ☞Per 1
20	  #4 (parent #3) [Persian] refs=None | âmorzîdan «آمرزیدن» : to forgive ; Farâmarz «فرامرز» : "one who forgives", male name | extra: آمرزش
21	#5 (parent #0) [Germanic] refs=AHD | milkan : to milk
22	  #6 (parent #5) [English] refs=None | milk
23	#7 (parent #0) [Latin] refs=AHD | mulgĕre : to milk
24	  #8 (parent #7) [English] refs=None | emulsion
25	--- entry 2 ---
26	ROOT Melo -> redirect to Mel 2
27	
```


## [2026-09-07T16:10:10.760Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-330.json",
 "description": "Read source JSON for page 330"
}
```


### [2026-09-07T16:10:10.797Z] TOOL RESULT

```
{
  "pdf_page": 330,
  "book_page": 300,
  "entries": [
    {
      "root": {
        "name": "Mel 3",
        "lang": "Indo-European",
        "refs": "POK:716",
        "gloss": "soft, soft material"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Greek",
          "refs": "POK:719",
          "words": [
            {
              "translit": "malaxos",
              "gloss": "soft",
              "script": null
            },
            {
              "translit": "malagma",
              "gloss": "soft material",
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
          "lang": "Arabic",
          "refs": "KLN:58",
          "words": [
            {
              "translit": "al-mâlâgmâ",
              "gloss": "the \"soft\" material",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "MON:4345",
          "words": [
            {
              "translit": "malğam",
              "gloss": "paste, ointment",
              "script": "ملغم"
            }
          ],
          "script_extra": "ملغمه ، الغام",
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 2,
          "lang": "French",
          "refs": "KLN:58",
          "words": [
            {
              "translit": "amalgame",
              "gloss": null,
              "script": null
            }
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
            {
              "translit": "amalgam",
              "gloss": null,
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {
              "translit": "meltan",
              "gloss": "to melt",
              "script": null
            },
            {
              "translit": "milks",
              "gloss": "mulch",
              "script": null
            },
            {
              "translit": "smelt, malta, mildja, milks",
              "gloss": null,
              "script": null
            }
          ],
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
            {
              "translit": "melt, smelt, malt, mild, mulch, enamel",
              "gloss": null,
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {
              "translit": "mollis",
              "gloss": "soft",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {
              "translit": "mollusk",
              "gloss": null,
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 0,
          "lang": "Celtic",
          "refs": "AHD",
          "words": [
            {
              "translit": "molto",
              "gloss": "sheep",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {
              "translit": "mutton",
              "gloss": null,
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Mělg",
        "lang": "Indo-European",
        "refs": "POK:722",
        "gloss": "to wipe off, to milk"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:722; FFD:77",
          "words": [
            {
              "translit": "marz, marez, mrz, mard",
              "gloss": "to wipe, sweep, rub",
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
          "refs": "BQT:1948,2010; HRN:214; SYN:569; MON:4010; SNS:245; FFD:77",
          "words": [
            {
              "translit": "mâlîdan",
              "gloss": "to rub",
              "script": "مالیدن"
            },
            {
              "translit": "moštan",
              "gloss": "to rub, massage",
              "script": "مُشتن"
            },
            {
              "translit": "morz",
              "gloss": "intercourse, also the anus, bottom",
              "script": "مُرز ۲"
            }
          ],
          "script_extra": "ماله ، مالش، مال ؛ مُشت ۲ ؛ مُرزیدن",
          "note": null,
          "quote": {
            "text": "چند کوبد زخمهای گرزشان - بر سر هر ژاژخا و مُرزشان",
            "poet": "Molavî"
          }
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:722; BQT:1448; HRN:12",
          "words": [
            {
              "translit": "â-marz",
              "gloss": "wipe out the sins, forgive",
              "script": null
            },
            {
              "translit": "fra-â-marz",
              "gloss": "one who forgives all sins",
              "script": null,
              "see": [
                "Per 1"
              ]
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": null,
          "words": [
            {
              "translit": "âmorzîdan",
              "gloss": "to forgive",
              "script": "آمرزیدن"
            },
            {
              "translit": "Farâmarz",
              "gloss": "\"one who forgives\", male name",
              "script": "فرامرز"
            }
          ],
          "script_extra": "آمرزش",
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {
              "translit": "milkan",
              "gloss": "to milk",
              "script": null
            }
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
            {
              "translit": "milk",
              "gloss": null,
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {
              "translit": "mulgĕre",
              "gloss": "to milk",
              "script": null
            }
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
            {
              "translit": "emulsion",
              "gloss": null,
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Melo",
        "redirect": "Mel 2"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-07T16:10:11.399Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-07T16:10:11.435Z] TOOL RESULT

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


## [2026-09-07T16:10:23.332Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs/../refs_online.json'))\nfor k in ['POK','AHD','KLN','MON','BQT','HRN','SYN','SNS','FFD','WLD','IEC','LEW','LAT','BRT','CHEUNG','PHD','NYB','HUB','ARY','SKT','LKT','PLA','AFM','FVQ','TAD','ARB']:\n    v=d.get(k)\n    if not v: print(k,'MISSING'); continue\n    print('==',k, v.get('kind'), '| offset', v.get('page_offset'), '|', str(v.get('local_file'))[:120])\n    print('   hint:', str(v.get('lookup_hint'))[:300])\n\""
}
```


## [2026-09-07T16:10:24.103Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo ---- && ls data/verification/page-3*.json | tail -5"
}
```


### [2026-09-07T16:10:24.707Z] TOOL RESULT

```
== POK archive_djvu | offset POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt
   hint: Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' giv
== AHD archive_djvu+website+archive_restricted | offset 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. | /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt
   hint: Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru
== KLN archive_djvu | offset KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt
   hint: Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
== MON website+archive_djvu | offset None | ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/source
   hint: Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbe
== BQT archive_djvu+local_scan_ocr | offset vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). | ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sou
   hint: grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --d
== HRN archive_djvu | offset leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt
   hint: Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.
== SYN archive_djvu | offset leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt
   hint: Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.
== SNS archive_djvu | offset 242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image | ['/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt', '/home/sfmqrb/git/rishe/data/verification/source
   hint: grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.
== FFD local_scan_ocr | offset 115 leaves (PDF pages); printed page = PDF page − 5 (PDF 40 = p.35). 2nd printing 1385 of the same Qoqnus setting (ISBN 964-311-015-X). | ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf', '/home/sfmqrb/git/rishe/data/
   hint: Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).
== WLD archive_djvu | offset Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696). | ['/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe/data/verification/source
   hint: Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP.
== IEC archive_djvu | offset TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt
   hint: Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.
== LEW archive_djvu | offset 1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt
   hint: Latin headword in bold at line start. For 1938 pagination borrow lateinischesetym0000awal.
== LAT archive_djvu | offset leaf = printed + 18 for most of the book (e.g. leaf 21 = p.3); drifts in places (leaf 219 = p.301 -> -82?? probably a mis-detected number) - grep the headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt
   hint: Latin headword in bold at line start followed by gender/declension, e.g. grep -n '^pater,'.
== BRT archive_djvu | offset Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt
   hint: Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops.
CHEUNG MISSING
== PHD archive_djvu | offset leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt
   hint: Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB).
== NYB archive_djvu | offset Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt
   hint: Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.
== HUB archive_djvu | offset leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt
   hint: Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.
== ARY local_scan_ocr | offset printed page = pdf page + 1 | ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt', '/home/sfmqrb/git/rishe/data/verifi
   hint: Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY
== SKT archive_djvu | offset leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt
   hint: Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.
== LKT archive_djvu | offset leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt
   hint: Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages. grep the oriental source word in transliteration or the number.
== PLA archive_djvu | offset 301 leaves (pdftotext -layout, \f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276). | ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf', '/home/sfmqrb/git/rishe/d
   hint: HathiTrust search-only; Google Books id q_ErAAAAMAAJ snippet view; DDB has only the table of contents. No full text online. | For pages in a scanned volume use: python3 tools/ref_page.py PLA:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)
== AFM archive_djvu | offset 198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image | ['/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt', '/home/sfmqrb/git/rishe/data/verification/source
   hint: Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').
== FVQ archive_djvu | offset printed page = leaf − 17 (0-based \f blocks in FVQ_pages.txt; 335 leaves) | ['/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt', '/home/sfmqrb/git/rishe/data/verification/source
   hint: Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).
== TAD archive_djvu | offset 86 leaves (small book, ~80 printed pages); offset ≈ leaf − 4..6, verify against the printed numeral on the page image | ['/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD_pages.txt', '/home/sfmqrb/git/rishe/data/verification/source
   hint: Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; inside.php search works.
== ARB archive_djvu | offset None | ['/home/sfmqrb/git/rishe/data/verification/sources/refs/ARB_mo3rb.txt', '/home/sfmqrb/git/rishe/data/verification/source
   hint: Alphabetical Arabic headwords; grep in ARB_mo3rb.txt / ARB_abdulraheem.txt (raw, no page breaks); edition of mo3rb not confirmed — check its title page image.
```


### [2026-09-07T16:10:24.750Z] TOOL RESULT

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
----
data/verification/page-35.json
data/verification/page-36.json
data/verification/page-37.json
data/verification/page-38.json
data/verification/page-39.json
```


## [2026-09-07T16:10:31.086Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"lemma: mel\" POK_full.txt | head -30; echo ====; grep -n \"Page(s): 71[0-9]\\|Page(s): 72[0-5]\" POK_full.txt | head -20"
}
```


### [2026-09-07T16:10:31.136Z] TOOL RESULT

```
Exit code 1
57843:Root / lemma: meljd^u 
59192:Root / lemma: melo-, smelo-: small animal, derived from Root/ lemma: mel-6, mela- : 
60886:Root / lemma: melo-, smelo- 
60892:Root/ lemma: melo-, smelo-: small animal, derived from Root/ lemma: mel-6, mele- : 
(eval):1: === not found
```


## [2026-09-07T16:10:31.290Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==725' POK_01.txt | head -60"
}
```


### [2026-09-07T16:10:32.666Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-07T16:10:36.828Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in POK_01.txt POK_02.txt POK_03.txt; do echo \"$f leaves: $(tr -cd '\\f' < $f | wc -c)\"; done; echo ====; grep -n \"melg\" POK_02.txt | head -20"
}
```


## [2026-09-07T16:10:37.550Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"smel\\|mel-1\\|mel-6\\|mel-8\" POK_full.txt | head -40"
}
```


### [2026-09-07T16:10:38.040Z] TOOL RESULT

```
Exit code 1
POK_01.txt leaves: 363
POK_02.txt leaves: 433
POK_03.txt leaves: 429
(eval):1: === not found
```


### [2026-09-07T16:10:38.086Z] TOOL RESULT

```
3253:of smells, penetrating; of sight, keen; of emotions, painful; of understanding, quick, 
3657:odoriferous flower ', wki^jov ' basil ' (if here suitablly, named after the sharp smell?). 
4477:worship, offer sacrifice, burn a sacrifice; to sacrifice on an altar; in gen., to burn; to smell ', 
4852:"smell, odour; person' as in Armenian sat//? (for older *anj). Gen. anjin^ soul, being, person 
4854:': Old Norse ang/m. " odour, smell ' : alb. aA7y"swell, puff' [common alb. ng > nj\. 
4877:"breathe, smell' (Denominative *an-slo-;W\\h phoney h, the sound value described here 
4903:maybe alb. a/yo^a "taste, smell' [common alb. n > nd\: Old Norse anda, -ada "breathe, 
4917:Old Church Slavic vonja {*ania) "smell' {vonjatT scent, smell '), *pc/7a//" smell' in Old 
4921:Maybe nasalized alb. {^unhati) nuhat, nuhas'scent, smell', huna, hunda' nose'. 
5062:Meaning: "smell, odour; person' 
5066:m. " odour, smell '. 
7888:breath, draft of the bellows, the wind, smell, hot aura of the fire ', aurtjriv ds. 
7960:waas^ white frost, ripe, smell, fragrance ', Lithuanian vestu, vesti^ cool off, become chill or 
15089:Meaning: to smell, scent 
15091:Material: Latin fragro, -are ^to emit a smell, esp. a sweet smell', denominative *b^r9g-ro-s' 
15092:smelling '; Old High German bracko {Modern High German Bracke), Middle Low German 
19870:Saxon d/7//, Old High German /////; o'/ZZ/'dill, strongly smelling plant umbel ', changing 
20421:Norwegian daam {'d'^emo-) "dark', daamem. " cloud haze ', daamm. "taste, smell, odor' 
21555:0UMO(;, -ov " thyme ' (strong-smelling plant as also 9u|jppa, 9u|jPpov "Satureja thymbra L.' 
21652:smell': Guw (Guow), teGukq " saerifiee ', Guaia "saerifiee, oblation', Gupa " saerifieial animal 
21680:done; of events, to happen ' from *b'^u-//d, foeteo, -e/ie'evi! smell, stink' due to a participle 
21713:dfj'em, dfti^ blow, smell, breathe quietly '; Old Church Slavic dung dungti {Woun-) "blow' 
21776:smell, odor' (or zur root form 6^eup-, see below); Gothic {hraiwa-) dubo. Old Norse dufa. 
22048:Gen. f/i/as/bs "ghost', "breath', Latvian dvasa' air, breath, smell ' (: russ. dvocfiatb, Indo 
25416:Old Norse ylda^ mustiness smell '. 
26384:above Armenian ampan6 Schwyzer Gr. Gr. I 333); here also lak. opcpa "smell, odor, 
34451:gourmand, voraeious eater ', Ypaao(; m. ' smell of a goat: henee, of men ' from *Ypaa-ao(; 
38531:m. "smell, odor, fragrance ', Avestan gantay- " fetidness ', Middle Persian gand^ fetidness 
38534:"smell, odor' compare e.g. Old High German 5///7/ra/7 "smell, stink' against Gothic stigqan^ 
38536:from roasting meat, smell or savour of a burnt sacrifice ' compared with Old Icelandic hmta 
40194:Old English gyrwe-fenn' morass', gyre' manure', mnl. gore, gore'smoke, smell, odor'. 
40325:Meaning: to smell, scent 
40327:Material: Old \x\(i\c jfghrati, ghrati^ it smells, it smells in anything, kisses, perceives ', 
40329:participle ghrata-, ghrana-m. n. 'smell, odor, fragrance ', ghranai. and ghrana-v\. 'nose', 
40331:ghrat'h 'olfaction, smell, odor'; 
40333:gr. OGcppaivoiJai 'smell, scent, feel' (< loo'es 'smell, odor' + *g"hr-), Aor. Attic (JbacppoMnv; 
40334:oocppnoK; 'olfaction, smell, odor' (: Old \y\(\\c ghrati-); 
45592:Under the imagining of the scratching, piercing smell are addable: hom. Kviar) ' steam 
45593:and odour of fat which exhales from roasting meat, smell or savour of a burnt sacrifice, 
45597:Latin mdor {*cnTdds) m. ' a vapor, steam, smell, fume (from something burned) ';
```


## [2026-09-07T16:10:49.029Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=372 && NR<=373' POK_02.txt | head -80"
}
```


### [2026-09-07T16:10:50.340Z] TOOL RESULT

```
n  Leistungen*,  communis  (alat.  comoinlerri]) ,gemeinsam*  (=  got.  usw.  gamains),  osk.  müinikad  ,communi*,  umbr. muneklu  ,munus,  Sportein*;
air.  möin,  mäin  , Kostbarkeit,  Schatz*,  dag-möini  ,gute  Gaben,  Wohltaten*» ablaut.  cjmr.  mwyn  ,Wert*  (*meino-)',
got.  gamainsj  ags.  gemcene,  ahd.  gimeini  ,gemein(sam)*;  als  ,vertauscht =  verfälscht*  auch  ahd.  mein  , falsch,  trügerisch*  (nhd.  Meineid)^  ags.  man ds.,  aisl.  meinn  ,schädlich*,  mein  , Schade,  Beschädigung,  Unglück*;
lit.  mainas  m.,  lett.  mains  ,Tausch*,  lit.  mainaü^  -ytij  lett.  mainit  ,wechseln, tauschen* ;  abg.  m^na  ,Wechsel,  Veränderung*,  izmeniti  „dLai.islßeLVj  diaXih- Tfity".  Hierher  auch  ai.  meni-  f.  , Rache*,  av.  maeni-  , Strafe*  (vgl.  abg.  mtsth jRache*  von  der  erw.  Wzf.  meit-).
Erw.  Wzf.  s.  unter  mei-g^-,  mei-k-,  mei-t-.
WP.  II  240  f.,  WH.  I  254  f.,  II  128,  Berneker  II  48  f.,  Trautmann  175  f.
5.  mei-  , wandern,  gehen*;  Flußnamen  wort  mein-,  moin-,  min-.
Lat.  meö,  -äre  ,gehen,  wandeln*  (vielleicht  altes  ä-Verbum  =)  poln. mijam,  mijac,  öech.  mijimj  mye^i, vorübergehen,  vergehen,  meiden*;  auf  dieser Basis  *meiä'  kann  auch  das  wä-Präs.  *mi-nämi  beruhen:  abg.  minq^  -^^i, vor- übergehen, vergehen^  (auch  minujg,  minovati  „Tr^o/^atVftv")  und  mcymr. mynet  , gehen*;  abg.  mimo  ,vorüber,  vorbei*;  (vgl.  gr.  ^r^og  , Schauspieler*?)
hierher  auch  die  Flußnamen  gall.  Moenus  ,Main*,  mir.  Moin  (in  Kerry), poln.  Mieii^  Mianka-,  *mein-  in  poln.  üfima,  schwundstufig  min-  in  lit. Minija,  poln.  Mnina,  hispan.  Minius  (Galicien),  Etrurien  Miniö.
Das  Verhältnis  migrare  :  ä(.iBißeLv  läßt  alte  Gleichheit  mit  mei-  , wechseln* als  , Ortsveränderung'  möglich  erscheinen.
WP.  II  241,  WH.  II  73,  Trautmann  176,  Berneker  II  59,  Krabe  BzfN 1,  256  f.
4.  mei-  jbinden,  verknüpfen*;  mi-tro-  , Bindung*.
Ai.  mitrd-  n.  (sekundär  m.)  , Freund*  (ursprüngl.  ,Freundschaft*  aus ,*Verbindung*),  av.  mid-ra-  m.  , Freund;  Vertrag;  Name  eines  Gottes (Personifikation  des  Vertrages)',  apers.  Mipra-  ,Gottesname* ;
gr.  hom.  ^Irgr]  ,Gurt ;  Kopfbinde,  Mitra* ;  unsicher  f^hog  ,Einschlagfaden^;
lett.  miemuriy  meimuri  ,Femerstricke*.
WP.  II  241  f.,  Güntert  Weltkönig  50 f.;  vgl.  1.  mei-.
711
f        jxiei-  mi-neu-  ,mindern*;  Adj.  mi-nu-  ,kleiii'.
\  Ai.  wm^^i,  minöti  ,mindert,  schädigt,   hindert*,   miyate^  miydte  ,inindert
sich*,   Partiz.    Perf.    mltd--  manyu-ml-   ,deii   Groll  mindernd,  vernichtend*;
gr.  fuvvd-cü  , mindere*,  Adj.  *(XLvv-g  in  ^Lvv-wgiog  ,kurzlebig*,  ^Ivvvd-cx  ,ein kleines  Weilchen,  nur  kurze  Zeit*  (Akk.  *^iVw,  erw.  nach  dr]-^d)]  fxsiojv, asiov  »geringer*,  nach  nleiaiv  für  *ixsivü)v,  das  noch  in  df.iSLva}v  ,besser*  = ♦nicht  minder*  erhalten  ist  {*mei-no-)]
lat.  ni-mis  (,*nicht  zu  wenig*  =)  , allzusehr*  i*ne-7ni-is)^  nimius  Adj. (*ne-'mi-os) ;  lat.  minor,  n.
  und  Adv.  minus  , kleiner*,  minimus  ,der  kleinste* (*r}iinu-mos),  minister  , Untergebener,  Diener*  (nsi.ch.  magister ;  osk.  minstreis minoris'),  minerrimus  ( :  minus  nach  vet-errimus :  -us),  minuö  ,vermmdere*, osk.  menvum  ,minuere*  (wohl  mit  nachlässigem  e  für  i);
corn.  minow  ,verkleinern,  mindern*,  mbret.  mynhuigenn,  nbret.  minvik ,mie  de  pain*;
ndd.  mirjTi,  minne  ,klein,  gering,  mager*  ist  aus  dem  Komparativ  rück- orebildet ;  Kompar.  got.  minniza,  aisl.  minni,  ahd.  minniro  , geringer,  minder*, Superl.  got.  minnistrj  ahd.  minnist,  aisl.  minnstr  , kleinste,  mindeste*  {-nn- aus  -nu-,  idg.  *minu-  mit  neuer  echter  Steigerungsbildung  durch  -izon-, 'ista-)j  Adv.  got.  mins  (*minniz),  aisl.  minnr,  ahd.  ags.  min  ,geringer, weniger* ;
abg.  mtnijh  (f.  mtrihH)  ,kleiner,  geringer,  jünger*  {*mbnvjh-jb) ]
hierher  auch  lit.  mdila  , Kleinigkeit,  kleine  Fische*,  lett.  maXle  ^kleiner Fisch*,  slav.  *mSh-k^  in  altserb.  mioki  , seicht*,  cech.  milky  ,klein,  seicht*, meliti  , zerbröckeln*,  und  aisl.  w/ör,  mjär,  rricBr  ,schmal,  dünn^  aus  *maiwa-, *maiwi-',  toch.  B  maiwe  ,klein^  j^ng^
WP.  II  242,  WH.  II  92  f.,  Trautmann  165,  184.
6.  mei-,  meiu-,  niin(u)-y  inini{ei)-  in  Schallnachahmungen  für  helle,  dünne Töne  und  Schreie.
Ai.  mimäti  ,blökt,  brüllt,  schreit*,  mimäyat,  dmlmet  ,brüllte,  blökte*, mäyü-  m.  ,das  Blöken,  Brüllen*;  vermutlich  maya-  m.  ,Roß*  (,* wiehernd*), mayüra  m.  ,Pfau*  (,*schreiend*) ;  min-mina-  ,undeutlich  durch  die  Nase sprechend* ;
gr.  (MLfxi^ü)  , wiehere*,  ^L^ix^^ög  ,das  Wiehern*,  ^L^id^aaa-  xQe^Bxlaaaa' (ptüvrjGaGa  Hes.,  ^iwgög  ,wimmernd*,  (xivigo^ac,  ixiwQitm  ,winsle*;  aus  lat. minur{r)iö^  ,zwitschere,  girre*  (gr.  Lw.  ?)  umgebildet  mintriö,  -Ire  ,pfeifen, piepen,  von  der  Maus*;  abg.  m^mat^,  mtmati  ,stammeln\
WP.  II  243,  WH.  II  93 ;  s.  auch  mü-.
7.  mei-  :  möi-  :  mi-,  oft  mit  1-,  n-,  r-,  t-  erweitert  ,mild,  weich,  lieblich*. Ai.  mdyas-  n.  ,Labsal,  Freude,  Lust*,  dazu  *m({)ies  dli{e)  in  ai.  miyBdha-
712  '
m.  , Opferspeise',    av.    myazda-   m.  ,OpfermahP;    als  *mei-dho-    ai.   medha. m.  jFettbrühe',  midhas-  n.  , Opfer*;
mit  1-:  cjmr.  mul  ,bescheiden*,  di-ful  ,kühn*  (*möi-Zo-);  apr.  mijU  \{i mieJas  und  mylas  ,lieb,  angenehm*,  mei'Ze  f.  , Liebe*,  meilüs  »liebreich* myliu^  myUti  ,lieben*,  pa-milstu,  pa-milti  ,liebo-ewinnen* ;  lett.  mTp  (alter lA-St.)  und  müs  (aus  *mielas)  ,lieb*,  mlZe^  ,lieben*,  mieluöt  ,bewirten* ;  aksl mi'Z^  , erbarmenswert*,  russ.  müyj  ,lieb*,  usw.;
mit  12-:  cymr.  mwyn  , freundlich*,  acorn.  muin^  moin  ,zierlich*,  bret.  moan ,dünn,  winzig*  (*mei-no-)]  air.  min  ,glatt,  sanft'  (*ml-no-)',
mit  r-:  alb.  mire  ,gut,  schön*;  aksl.  miH  , Friede';  ablaut.  aserb.  mijer (*moiro-)j  apoln.  mier  , Friede*  (alit.  mierasj  lett.  miers  ds.  sind  slav.  Lw.)«
mit  f-:  l
```


## [2026-09-07T16:10:58.654Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=374 && NR<=378 {print \"### LEAF \" NR; print}' POK_02.txt | head -200"
}
```


### [2026-09-07T16:11:00.128Z] TOOL RESULT

```
### LEAF 374
at.  mltis  ,mild,  weich*  (*meit-);  air.  möith^  möeth  (^*möit-)  ds. auch(?)  PL  me(i)th  ,fett,  fruchtbar*;  cymr.  mwydo  (*meit-)  , erweichen* mwydlon  ,Weichteile* ;   lett.  at-mist  , weich   werden*,   at-mietet  , erweichen*.
WP.  II  244,  WH.  II  96  f.,  Trautmann  174,  175.
meigh-f  auch  meik-  ^flimmern,  blinzeln;  dunkel  (vor  den  Augen  flimmernd)**
mighlä  ,Nebel,  Wölket I.  meigh-:
A.  mit  der  Bed.  ^flimmern,  blinzeln^  micäre^
Mnd.  micken  ^beobachten  (*hinblinzeln)',  awfries.  mitza  ,beachten^;
lit.  mingUy  mzgti  ^einschlafen'  (mit  «i-);  lett.  miegu,  migt  ds.  (mit  äiz^, le-) ;  apr.  enmigguns  , eingeschlafen',  ismige  ^entschlief ;  lett.  miegt  ,die  Augen schließen',  apr.  maiggun  Akk.,  lit.  miegas^  lett.  mlegs  , Schlaf,  dazu  lit. miegil  (alt  miegmi),  miegöti  und  apr.  meide  , schlafen';
slav.  *mig^  in  bulg.  russ.  mig  , Augenblick';  slav.  *mhgnqti  in  russ.-ksl. megnuti  ,nictare',  serb.  namägnuti  , winken',  und  migati  ^blinzeln';  Iterat.- Kaus.  aksl.  sz-meziti  , Augen  schließen',  mit  aor.-pass.  Bedeutung  slav. *m'b^ati,  sloven.  me^dti  , Augen  geschlossen  halten',  russ.  mzat , schlummern'; serb.-ksl.  migliv^  ,blinzelnd';
B.  mit  der  Bed.  , dunkel  vor  den  Augen  werden,  Nebel,  Wolke^.
Ai.  meghd-  m.  , Wolke',  mih  ,Nebel,  wässeriger  Niederschlag',  av.  maeya- ,Wolke';  arm.  we^, Nebel';  gr.  dfiixlr]  (att.  öfxixl'T])  ,Wolke,  Nebel',  hom. änLxd-aXöeaaav  ,nebelig,  Beiwort  von  Lemnos'  (mit  Vokalvorschlag);
ndl.  miggelen  ,staubregnen' ;   aisl.  mistr  ,trübes  Wetter'  usw.  (^mixstu-)]
lit.  miglä  ,Nebel',  lett.  migla  ds.  (=  dfxix^) ',    abg.  mbgla  ,Nebel',   russ. mgia  ,Schneegestöber,  kalter  Nebel',  öech.  mha  , Nebel',  russ.  mzit  ,staub- regnen,  nebeln'  usw. 2»  meik-:  Npers.  miza,  muza  (pehl.  *micak),   balüci  micäS  ,Augenwimper';
lat.  micöj  -äre  ,sich  zuckend  bewegen,  funkeln'  (*mikäiö)]  dl-micö  ,fechte, kämpfe';  cymr.  mygr  ,leuchtend',  di-r-mygu  ,verachten'  (wie  de-spiciö)]  air.
T
713
^g.jneccim   (cc  =  g)   ,verachte^   ist   brit.  Lw. ;    abg.    mhChU   ^Vision,    Spuk, q^liiinmer^;  osorb.  mikac  ^blinzeln,  blinken^,  usw. ^yp.  II  246  f.,  WH.  II  86,  Trautmann  174,  184;  s.  auch  unter  meis-.
Oicigb'  ;harnen^
\[,  mihati  ,harnt^,  Partiz.  midhd-  (=  lat.  mictus),  mldJia-  n.  ,Kot',  meha- uj.  ,Harn^;  av.  maezaiti  ,harnt,  diingt^,  maesman-  jH^-rn*^;
arm.  mizem  ,barne',  mez  ,Harn^ ;
gr.  d{.Lei%siv,  Aor.  lo^ei^a  (=  lat.  miccz),  jünger  dfxlxso)  ^barnen^^,  d^t^ai ' ovQTjaai  Hes.  (ßi-,  d-  sind  wohl  Vokalvorschlag);  vgl.  [xotx(^g  m.,  f-iocxccg, 'dSog  f.  ,Ehebrecher(iny??
lat.  meiöy  -ere,  mixi,  mictum  (sekundär  mingö,  minxi,  minctum)  , harnen^ (*7neigh-{ö) ;
aisl.  migaj  ags.  mlgan,  mnd.  mlgen  ,harnen^,  ags.  micga  m.,  micge  f., migoda  ,Harn^,  got.  maikstus,  as.  ahd.  mist  ,Mist',  ags.  meox  ,Kot,  Dünger^, nfrie
### LEAF 375
s.  mjuksj  ags.  miexen  f.  ,Misthaufe^,  as.  mehs  n.  ,Harn^,  mnd.  mesj afries.  mese  ds. ;  wahrscheinlich  hierher  der  Name  der  nur  durch  den  Mist der  Vögel  verpflanzten  Mistel:  ahd.  mistil,  ags.  mistel,  aisl.  mistil-teinn ,Mistelzweig^;  (mit  aufgefrischter  Tennis  des  Formans:)  mhd.  meisch ,Maische^,  mnd.  meisch,  mesch  ,ungegorener  Malzsaft,  Maische^,  ags.  masc-, mäx-wyrt  , Maischwürze ^,  engl,  mash  ,Maische,  zerquetschen^;
lit.  mlziX  (Neubildung  für  *minzü),  misti  , harnen^,  lett.  mieznu  und  mizu, Partiz.  mizu,  Inf.  mizt  ,harnen^  (aber  lit.  meziu,  mezti  ,den  Dünger  bear- beiten' ist  vielmehr  meziu  =  lett.  mezu,  mezu,  mezt]  es  liegt  ein  dehn- stufiges Wurzelnomen  *we[z]§fA-  zugrunde);
skr.  m\2-äm,  -ati  ,harnen'  {z  aus  dem  Präs.  *miz-jg  verallgemeinert) ; sloven.  mdzi,  mdzeti  ,hervordringen  (von  Flüssigkeiten)',  m922?ia  ,Moorgrund'; slav.  *m^zga  (*moigzghä  aus  *moigh-ska)  ,Baumsaft'  (,*hervortröpfelnd') in  skr.  mezga,  öech.  mizha,  miza  usw.;
toch.  B  mi§o  ,Harn^
WP.  II  245  f.,  WH.  II  60  f.,  Kuiper  Nasalpräs.  159,  Trautmann  185, Berneker  II  54.
mei-g^-  ,wechseln,  tauschen;  eine  Ortsveränderung  vornehmend
Gr.  d[j,eLßü)  ,wechsle^.  Med.  ,erwidere,  vergelte,  wandere',  ä^oißög  ,wech- selnd',  di^ioiß/j  ,Wechsel^;
lat.  migröj  -äre  ,wandern',  Denom.  eines  ^migVi-ros. Erweiterung  von  mei-  ,wechseln^. WP.  II  245,  WH.  II  86  f.
714
mei-k-  (und   mei-g-?)  ,mischen^,   auch   mei- :  mi-ek-,  mi-n-ck--^  Präsens Stämme  auch  mit  -so-,  -sko-]  znik-ro-  ,vermischt^
Ai.  meksdyati,  mimiksB  , rührt  um^,  miSrd-  , vermischt^,  misrdyati  ,mischf  • av.  minasti  ^vermischt^,  misvan-  ,die  Gemischten  enthaltend^ ;  myäsaite  si« mischen  sich^;
gr.  f.dyvv^L  (richtiger  ^elyw^i),  (lei^o),  SfiSL^cc,  eix(s)Ly,TOj  iixtyrjv  ^mische* f-ilayü)  ds.,  iiiya^  i-dyda  Adv.  ^gemischt',  f-nyog,  -ddog  ^Gemisch^  (mit  qq. klarem  y);  (.ilayw  ^mische'  aus  *fiiy-(Txw,  oder  zu  mezg-'j
lat.  misceö,  -ere  ^mischen'  (Erw.  von  mi[Jc]-sköy,
air.  mesc  ,betrunken^,  mir.  auch  ^verwirrt*;  mesc{a)id  ,mischt,  taucht ein^  verwirrt^*  cymr.  mysgu  ^mischen^;
ahd.  miskaUj  ags.  miscian  ^mischen^  (eher  lat.  Lw.);
lit.  mieHü,  mieUi  (*meik{ö)  ,mischen^,  Iterat.  mai^au,  maisyti,  lett.  mäitu mäisit  ds.;  auch  ,zum  zweiten  Male  pflügen^;  vgl.  apr.  maysotan  ,gemengt' d.  i.  ,bunt^ ;  Intransit.  su7ni§ü  und  sumistü,  -miHi  ,m  Verwirrung  geraten* lett. 
### LEAF 376
 samist  ds.;  lett.  miset  ^mischen,  irre  machen';  lit.  maistas  m.  ,Auf. ruhr^  Triisras  ^vermischt^^  lett.  mistrs  ds. ;
abg.  mes(^j  mesiti  usw.  ^mischen^,  das  seine  iterat.  Bedeutung  verloren  hat.
Hierher  wohl  ai.  ä-miksä  ,Quark  von  Milch^,  osset.  misin  , Buttermilch', mir.  medg,  cymr.  maidd,  ncorn.  meith,  abret.  meid,  gall.-lat.  *mesga  (frz. megue)  , Molken'  (*misga),  aisl.  mysa  ,Molken'  (*mihswön').
WP.  II  244  f.,  WH.  II  95  f.,  Trautmann  175;  Kuiper  Nasalpräs.  50,  123.
mei-no-  .Meinung,  Absicht'.
Air.  mian  n.  ,Wunsch,  Verlangen',  cymr.  mwyn  (*meinO')  ,Genuß',  er mioyn  ,um  —  willen';  ahd.  meina  f.  ,Sinn,  Meinung,  Absicht',  afries.  mew«, ags.  man  f.  , Meinung,  Erwähnung,  Klage';  ahd.  meinen  , meinen,  sagen', ags.  mcenan  ds.,  auch  , klagen';  slav.  *mainiö  ,meine'  in  aksl.  minj^, mHiti  , erwähnen,  halten  für',  usw.
WP.  II  302,  Trautmann  165.
meis-  ,flimmern,  blinzeln,  dunkel  (vor  den  Augen  flimmernd),  Nebel,  Wolke;
auch  betrügen,  Trug'.
Ai.  mi?dti  ,schlägt  die  Augen  auf,  ni-mis  f.,  ni-misa-  m.  ,das  Blinzeln, Schließen  des  Auges';  misa-  n.  ,Betrug,  Täuschung';  mtdam  ,leise'  (*miz-do- jVerstohlen' ?),  mllati  , schließt  die  Augen';
ndd.  mis  ,nebliges  Wetter',  misein  ,fein  regnen',  ndl.  (fläm.)  mijzelen, mizelen  ,Staub  regnen';
aksl.  mhseh  ,turpis  quaestus',  russ.  mSel  , Gewinn',  oh-michnütbäa  ,sich irren'.
WP.  II  248 f.;  Erweiterung  der  auch  in  meigh-j  meik-  vorliegenden Wurzel.
715
jneiti^y  ,  Aufenthalts  (ort)',  woraus  balt.  auch  .Lebensunterhalt,  Nahrung^ Av.  maed-andm  n.  ,Aufenthaltsort  für  Menschen  und   Götter,  Wohnung, gausS  mid-näiti  ,weilt,  wohnt,  bleibt^-
lit.  mintü,  misti  ,sich  nähren*^,  mltas  ,Lebensunterhalt',  maitmti  ,nähren', inaistas  ,Nahrung',  auch  lit.  maitä,   lett.  mäita  ,Aas';   apr.  maitä  ,nährt*^; lett.  mitidt  Aufenthalt  und  Nahrung  geben^,  mitii,  mist  , wohnen,  sich  auf- halten, seine  Nahrung  habend WP.  n  247,  Trautmann  185,  Berneker  2,  52.
■     2>
;  mei--t(h)-  »wechseln,  tauschen*;  mei-tu-,  moi-tu-  ,Tausch*.
Ai.  mithati,  mithdti  »wechselt  ab,  zankt,  gesellt  sich  zu',  mithd-  Adv. ^gegenseitig,  abwechselnd,  zusammen'  =  av.  midö  Adv.  ,verkehrt,  falsch'; ai.  mühüs,  mithus,  mithuyä  Adv.  ds.,  av.  mi^wa(na)-^  mi&wara- 
### LEAF 377
 Adj.  ,ge- paart' ;
gr.  (sizil.)  ^oiTog  ,Vergeltung,  Dank'  (Lw.  aus  dem  Italischen);
lat.  mntöj  -äre  {^moitäio)  ,ändern,  verändern,  tauschen',  mütuus  , wechsel- seitig' ;
air.  Negativpräfix  mi-,  misis)-'^  die  vollere  Form  in  mis-cuis  ,Haß';  vgl. unten  germ.  Tjima-;  hierher  auch  air.  messa  ,schlimmer'?
got.  maidjan  .verändern,  verfälschen',  in-maidjan  , verwandeln' ;  got. maipms  , Geschenk',  aisl.  PI.  f.  meidmar^  ags.  mädum,  as.  medom  , Geschenk, Kostbarkeit,  Kleinod';  Partiz.  *mitHo-  , verwechselt,  falsch'  in  got.  missö »wechselseitig,  einander',  aisl.  (ä)missy  mnd.  to  misse  ,verkehrt,  ungünstig', ahd.  missi  , verschieden  (artig)',  Präfix  got.  missa-  ,verkehrt,  miß-'  (missa- deds  =  nhd.  Missetat,  missa-leiks  ,verschieden',  vgl.  nhd.  mißfarben  ,ver- schiedenfarbig',  vielleicht  auch  got.  missa-qiss  ,Wortstreit'),  aisl.  mis-  (selten missi-),  as.  ags.  mis-,  ahd.  missa-,  missi-,  nhd.  miss-]
etwas  anders  ahd.  ags.  missan  .vermissen,  entbehren,  verfehlen',  aisl. missa  ,vermissen,  verlieren',  mhd.  misse  f.  , Mangel',  ags.  miss  n.  ,Verlust', aisl.  missir  m.  missa  f.  , Verlust,  Schaden',  zu  ahd.  mldan  ,meiden,  ent- behren*, refl.  ,sich  enthalten';  intr.  ,wegbleiben,  mangeln,  sich  verbergen', as.  mlthan,  mldan  ds.,  ags.  mldan  ,verhehlen;  meiden';
baltoslav.  *meitu-  in  lett.  mietus  m.  , Tausch,  Wechsel',  dazu  mituot  und mietuot  ,tauschen',  mitet  ,verändern',  refl.  ,aufhör,en',  Adv.  pa-misu  ,wechsel- weise';
aksl.  mite  , abwechselnd',  russ.-ksl.  mitush  Adv.  ds.,  usw. ;  dazu  aksl. mbsth  usw.  , Rache'.
WP.  II  247 f.,  WH.  II  137,  140,  Trautmann  176 f.;  s.  unter  2.  mei-.
mek-  Schallwort  für  , meckern'.
Ai.  makamakayate  ,meckert',  mekd-  m.  ,Bock*;  arm.  makH  , Schaf;  gr. hom.     firjxäa^ai    ,meckern,    blöken';     lat.    micciö,    -ire    ,meckern';    mhd.
716
meckatzeUj  mechzen,   nhd.  meckern,  mhd.  mecke  , Ziegenbock*;    lit.  mekenik  '<
-enti  , meckern,  stammeln* ;  klr.  mekaty  , meckern,  blöken*,  usw.  ^
WP.  II  256,  WH.  II  85  f.,  Trautmann   177;    vgl.  6.  mei-.  T|
I.  mel-  (auch  sznel-),  mels-  :  mle-,  mel-d-  :  ml-ed-,  mel-dh-,  ml-ei^  • mli-,  melo-k-  :  mlä-k-,  znleu-  :  min-  , zermalmen,  schlagen,  mahlen* speziell  Korn;  aus  ,zerrieben*  auch  ,fein,  zart,  weich*  und  »aufgerieben, schwach';  meluo-  ,Mehl';  mol-to-,  ml-to-,  ml-to-  , Zermalmung'. mli-no-  ,zermalmt^
A.  Ai.  mrnäti,  mrnati  ,zermalmt,  mahlt',  mür
### LEAF 378
nd-  ,verwelkt,  schlaff*  uq^ , zermalmt*  (auch  z.  T.  mit  3.  mer-  vermischt),  mlä-  , weich,  welk,  schlaff werden',  mlätd-  , weich  gegerbt*,  av.  mräta-  ds.,  vielleicht  ai.  malvd-  ,töricht, läppisch*  (,*schwach*  in  geistigem  Sinne);  vgl.  got.  ga-malwjan,  ahd« molawen,  lit.  malvinti]  von  der  2-Basis  ai.  mrityati  ,zerfällt,  löst  sich  auf*«
arm.  malern  , zerstoße*  {*mj,-),  ml-ml-em  , reibe*,  meim  ,weich,  schlaff* ma-mul  , drückt' ;  .^
gr.  iivXr^  f.,  spät  ixvXog  m. , Mühle',  i.LvXXa)  , mahle,  zerreibe,  zermalme'  (auch  ' wie  lat.  molö  ,beschlafe' :  sizil.  ixvXXoq  ^pudendum  muliebre') ;  ^aXsgög  ,zer- malmend';  iidXsvqov  ,Mehl*  ist  Kreuzung  von  äXsvgov  und  f^vXr];  dfxaXög jSchwach,  zart*,  ä^ßXvg  ,kraftlos,  schwach*;  von  der  i-Basis  gr.  ßXlxov jMelde*  (vgl.  zur  Bed.  nhd.  Melde  unter  mel-dh-),  ßXLTO-^du^ag  ,Dumm" köpf*,  ßXirdg  , wertlose  Frau* ;
alb.  mjel  ,Mehl*  (*meluo-  =  nhd.  Mehl)  •
lat.  molö-,  -ere  , mahlen*  (=  air.  melid),  mollna  , Mühle*,  mola  ,Mühlsteia* umbr.  kumaltu,  kumultu,  comultu  ,commolitö*,  kumates,  comatir  ,commolitis*, maletu  ,molito*  (idg.  ^m^lö)]  lat.  mulier  ,Weib*  (aus  *muliesi,  idg.  *ml-j^i ,die  zartere',  Kompar.  zu  mollis  [S.  718]);  marcus  , Hammer*,  Rückbildung zu  marculus,  martellus  (*mal-tl-os),  das  a  wie  in  lat.  palma  :  gr.  rtaXdi^rj] lat.  malleus  , Hammer,  Schlägel*  aus  *mal-ni-  , Zermalmung';
air.  melim  ,molö*  (mit  com-  , zerreiben*,  mit  to-  ,verzehren') ;  cymr.  malu (*mel-),  bret.maZa/, mahlen',  meil  ,Mühle'  {*melia);  air.  mlith  Pat.  ,zu  mahlen, (*ml-t-),  mol  , Mühlstange*;  *malduo-  , weich*  in  bret.  divalo  ,(nicht  zart  =) roh,  häßlich',  cymr.  malwoden  , Schlamm';  von  schwerer  Basis  gall.  *bläto- (frz.  ble),  mcymr.  hlawtj  ncymr,  hlawd,  acorn.  blot,  bret.  bleud  ,Mehl* {ml-to-  =  lit.  miltai)  air.  mläith,  mir.  bläith  , sanft,  glatt',  mbret.  blot , weich,  zart'  (*ml-tL-]  cymr.  mwlwg  , Kehricht*  (*molu-ko-)  ]  kelt.  *molto- in  cymr.  mollt,  corn.  mols,  bret.  maout,  mir.  molt,  gall.-rom.  multo,  -öne , (verschnittener)  Widder' ;
got.  ahd.  malan,  aisl.  mala  , mahlen'  (germ.  a-Präsens);  ahd.  muljan jZermalmen',  aisl.  mylia  ds.,  ahd.  gimulli  ,Gemüll*  (aber  ahd.  mull,  -iw, ags.  myln,  aisl.  mylna  ,Mühle*  aus  spätlat.  mollna) ;  got.  mulda,  ags.  molda,
717
aisl.  'mold,  ahd.  molta  f.  ,Staub,  Erde'  (*ml-ta);  got.  malma  m.  ,Sand\ ji
```


## [2026-09-07T16:11:08.706Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=379 && NR<=381 {print \"### LEAF \" NR; print}' POK_02.txt"
}
```


### [2026-09-07T16:11:10.178Z] TOOL RESULT

```
### LEAF 379
isl.  Tnalmr  ,Erz*,  ablaut.  ags.  mealm-stän  , Sandstein',  mhd.  malmen  ,zer- pialmen',  as.  ahd.  melm  ,Staub,  Sand'  (:  lit.  melmuo  »Nierenstein,  Stein- krankheit*) ;  nhd.  dial.  mulm  »zerfallene  Erde,  Staub,  vermodertes  Holz' ; ahd.  as.  melo,  Gen.  -wes^  ags.  meZw-,  Gen.  -wes^  aisl.  mjgl  ^Mehl''  {*meluo-  = alb.  rniel)]
ahd.  mü(i)wa  ^Milbe^  (*melwjö)',  got.  malö  n.,  aisl.  m^lr  {*molu-)  ,Motte (mehlmachendes  Tierchen');  abg.  moh  (*moli-)  ds.,  arm.  dial.  mdymöy (aus  *moimol)  ^Motte';  sehr  fraglich  ist  Zugehörigkeit  von  ai.  malüka- m.  ,Art  Wurm',  arm.  mlukn  , Wanze',  und  die  von  as.  mnd.  mol  m.,  mhd.  n. jEidechse',  ahd.  mol,  molm^  molt  , Eidechse',  nhd.  Molchy  das  an  arm.  moiez Eidechse'  erinnert;    eher  zu  6.  mel-  S.  721;
got.  ga-malwjan  , zermalmen,  zerstoßen',  aisl.  melva  ,in  Stücke  brechen', ahd.  molawen  ,tabere';  aisl.  mjgll  , feiner  Schnee',  schw.  dial.  mjäl(l)a ,Art  feiner  Sanderde'  {*melnä);  got.  mulda^  ags.  molde,  ahd.  molta  , Staub, Erde'  (Partiz.  *7}il-td  ,die  zerriebene');
lit.  malü,  mdlti  (Akzent  der  schweren  Basis)  ,mahlen',  malünas,  apr. malunis  ,Mühle',  miltai^  lett.  mUti  ,Mehl'  (=  cymr.  blawd),  apr.  meltan ,Mehl';  lit.  malinys,  milinySj  lett.  milna  , Quirlstange' ;  lit.  maJvinti,  mul- vinti  ,plagen' ;  mit  Formans  -to- :  lett.  mältU,  miltit  , schlagen' ;  lit.  melmuo s.  oben;
aksl.  inelJQy  mleth,  russ.  molötby  skr.  mljeti  (schwere  Basis)  ,mahlen'; poln.  mlon  , Griff  an  der  Handmühle'  (*melm)j  russ.  meiern  (*mel-eno)y skr.  cak.  mldn  (^molm)  ds. ;  skr.  mlevo^  mlijevo  , Mahlgut,  Korn'  (=  ahd. meloj  alb.  mjei]  daneben  serb.  ml-i-vOj  russ.  mel-i-vo  ,Mahlgut');  klr.  möiot m.  ,Treber,  Hülsen  von  Malz',  sloven.  mldto  n.,  mldta  f.  ,Malztreber', cech.  mldto  ds.,  apr.  piva-maltan  , Biermalz'  (germ.  ?  s.  mel-d-)  usw. ; wohl  auch  (leichte  Basis)  aksl.  mlat^,  russ.  mölot^  usw.  , Hammer'  als *mol-to-  ,Zermalm-ung,  -er';  ksl.  mlatiti  (*moltiti)  ,schlagen';  dehnstufig mHzkz  ,klein'  und  aksl.  meh  ^Kalk'  usw. ;
toch.  A  malywet  ,du  drückst,  zertrittst^,  B  melye  ,sie  zertreten^;
hitt.  ma-al-la-i  ,zermalmt^;
mit  anl.  s-:  norw.  smola  ,zermalmen';  mhd.  smoln  , Brotkrümchen  ab- lösen', aschw.  smola,  smula,  smule  ,Brocken'  (neben  aisl.  moli  ds.,  mgl  f. , Haufe  von  Steinen') ;  lett.  smelis,  smelis  , Wassersand  im  Felde',  lit.  smelys, Gen.  smllio  ,Sand',  smiltls  ds.
B.  Basis  m{e)lei'- :  mli-  in:  cymr.  blin  ,müde'  (*mll-no-),  abr.  PI.  blinion jinertes';  lett.  bllnis  ,müder  Mensch',  bUnet  ,siechen';  serb.  mlitäm,  -ati ,faul  werden,  schlendern'  (vgl.  mit  i:  ai.  mrityati,  gr.  ßlirov),  russ
### LEAF 380
.-ksl. mlim  ,Kuchen',  russ.  blin  , Pfannkuchen',  serb.  mtinac  ,gewalkter  Teig, Matze';  klr.  mlity  ,vergehen^,  Kaus.  mloity  ^Übelkeit  erregen^*
718
unsicher  serb.  mledan  ^mag-er,  schwach*,  dial.  ,fade,  flau*   (in  Slavon* mUdan),  usw.
hierher  wohl  (als  , Mahlfrucht')  gr.  [xeXtvT]^  lat.  müium  (*meliio~)  ij*  r PL  malnos  , Hirse*;  ursprüngl.  Flexion  *inel-i-,  -n-es.
C.  Von  einer  u-Basis  (vgl.  gr.  dfißXvg,  ai.  malvd-,  nhd.  Mehl  uswV av.  mruta-  , aufgerieben,  schwach*,  mrüra  , aufreibend,  verderblich*.
mel-d-  (vielleicht  zuerst  in  einem  d-Präs.);  i22(e)ie-cf-;  mldu-,  m(e)u dui-  ,weich*.
Ai.  mdrdati,  mrdnäti  »zerdrückt,  reibt,  reibt  auf*,  av.  mardd-  {mardaitt- mordnda-t  aus  *mrnda-)  ,zuschandeu  machen*,  Kaus.  ai.  mardayati  zer« drückt,  zerbricht,  bedrängt,  quält*  (diese  ar.  Worte  können  und  werden z.  T.  auch  idg-.  mer-d-  gleicher  Bed.  fortsetzen);  ai.  mfdü-  (=■■  gr.  ßladvc) , weich,  zart*,  fem.  mrdvij  Kompar.  mradlyän^  Superl.  mradistha-]  vi-mradati ,erweicht';  ai.  mrt-  (mj-d-)  ,Erde,  Lehm,  Ton',  mrtsnd-  m.  n.  , Staub,  Pulver* mftsnä  , schöne  Erde,  guter  Lehm,  Lehm*  (:  nisl.  mylsna  , Staub*);
arm.  meik  , weichlich,  schlaff*  {*meldu-i-)'^
gr.  dLixaXdvvo)  , seh  wache,  zerstöre*  (zu  *[ä']^alöv-g  =  ai.  mrdü-);  ßXadvg^ ßXaöaQÖg  , schlaff*  (*{xXad-,  *mld-)',  ^sXScj  ,schmelze*  (tr.,  med.  intr.  == ags.  meltan  usw.);  mit  der  Vokalstellung  und  Bed.  von  ai.  vimradatl^ mradlyän  auch  ßXevva  f.,  ßXsvvoq  n.  ,Schleim,  Rotz*,  ßXevvog  , langsam  von Verstand,  verdummt*  {*mled-sno-^  vgl.  ai.  mft-snd-) ;
lat.  mollis  , weich,  geschmeidig,  biegsam*  (^mldu-is,  vgl.  ai.  fem.  mfdvi)*^ hlandus  »schmeichelnd,  liebkosend,  freundlich*  aus  *ml9ndo-?j
cymr.  hlydd  ,sanft,  zart*,  bret.  hie  , schwach*  (*mldo-)j  air.  meldach  ,ange- nehm'  (können  auch  zu  mel-dh-  gehören;  ebenso  :)  schott.-gäl.  moll  m. , Spreu*;
mir.  blind,  blinn  ^eines  toten  Mannes  Speichel^  (wohl  '*mld-sno-?);
ags.  meltan  ^schmelzen,  verbrennen,  verdauen^,  aisl.  melta  _,(im  Magen) auflösen,  verdauen^,  norw.  molten  ,mürbe;  weich^,  Kaus.  ags.  mieltan ^schmelzen,  reinigen^  verdauen*^;  got  ga-malteins  f.  , Auflösung^,  aisl.  ma^^r ^verfault,  verdorben^;  ahd.  malz  ,hinschmelzend,  kraftlos*;  ahd.  malz^  ags. mealtj  as.  aisl.  malt  ,Malz'  (slav.  *molto,  cech.  mldto  usw.  ds.  entlehnt  aus dem  Germ.) ;
mit  ai.  mrd-,  mj'tsnä-  vgl.  nisl.  mylsna  , Staub',  ags.  formolsnian  ,z\x  Staub werden'  (s.  oben) ;
mit  anl.  s-:  ahd.  sirtElzan  ,zerf
### LEAF 381
lließen,  schmelzen',  smalz  ^ausgelassenes Fett  oder  Butter',  ags.  smolt,  smylte  ,ruhig,  von  der  See',  aschwed. smultna  ,ruhig  werden' ;  hierher  vielleicht  ahd.  milzi,  ags.  mute  f.,  milt  m., aisl.  milti  ,Milz'   (läßt  sich  leicht  ausstreichen,  gleichsam  zerschmelzen);
abg.  mlad^,  russ.  mölodz  usw.  ,jung,  zart*  (*moldo-);  apr.  maldai  Nom. PI.  m.  , Jungen',  maldü-ni-n  Akk.  Sg.  , Jugend',  maldian  ,Fohlen';  apr. maldenikis  ,Kind',  abg.  mladenhchj  mladbndcd  ,Jüngling'  i*molden-y  *moldin-)'i
719 fuel-dh-  (vielleicht  zuerst  in  einem  cfi2-Präsens  *mel-dh-o) : Ai.  märdhati,  mrdhdti  ,läßt  nach,  vernachlässigt,  vergißt^  (,*wird  weich
schlaff  =  aufgerieben'); gr.  ^ald-av.oq   ,weich,   zart,    mild^    (nach  f^aXaxög  erweitert  aus:)  ^dld?]
^Wachs',   ^iaX^u)(Xa)'   ^«Aaxaxrw    Hes.,    (Äal&cjv   ^Weichling^^  ^al&aLvco   ,er-
weiche' ; hierher  (oder  zu  mel-d-)  cymr.  hlydd  usw. ; got.   unmildjai   Nom.   PL  ,lieblos',   mildipa   ,Milde',  aisl.  mildr  .gnädig,
barmherzig^,  ags.  milde,  ahd.  milti  , milde,  gütig,  freundlich^- ahd.  melta^  ags.  melde^  aschwed.  mceldj  molda,  ahd.  malta,  multa  , Melde'
(vgl.  gr.  ßliTOv  ,Melde'  aus  *mli-to-,  von  der  Mehlbestäubung  der  Blätter).
(s)niel-k-
aisl.  melr  ,Sandhügel'  {*melha-),  schwed.  dial.  mjäg  {*melga-)  ds. lett.  smelknes  , Mehlabfall',  smalknes  ,Feilstaub,  Sägespäne',  smalks  ,fein' smulksne  ,Stäubchen,  Kleinigkeit';
lit.  smulküs  ,fein',  smülkti  ,fein  werden^,  smulkme  .Kleinigkeit' ; lit.  smiltiSj  lett.  srmlts,  smilkts  ,Sand'.
melo-k-,  mläk-  , weich,  schwach,  matt,  albern'.
Gr.  i^aXa-KÖg  .weich',  ßlä^,  -liög  .schlaff,  träge,  weichlich,  töricht';  ßlrjXQoq, I  hom.  dßXrjxQog  ,schwach,  sanft'  {*iJ.Xay(,-aQÖg) ;  ^alytr]  ,das  Erstarren  vor  Kälte, Erfrieren',  (j.aXy.ttü  .habe  vor  Kälte  steife  Glieder'  weicht  in  der  Bed.  zu weit  ab;
mir.  malcad  , Verfaulen' ;  vermutlich  mir.  bleu  (air.  *mlen)  .die  Weichen' aus  *7nlaknä]
aksl.  mU6ati,  russ.  molödth  .schweigen'  (*m^lke'),  aksl.  u-mhciti  , bezäh- men', u-mhkn
```


## [2026-09-07T16:11:42.864Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=381 && NR<=384 {print \"### LEAF \" NR; print}' POK_02.txt | grep -n \"72[0-3]\\|melg\\|melag\\|mel.g\\|amelg\\|mulg\\|milk\\|abstreif\" "
}
```


## [2026-09-07T16:11:43.633Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=382 && NR<=384 {print \"### LEAF \" NR; print}' POK_02.txt"
}
```


### [2026-09-07T16:11:44.409Z] TOOL RESULT

```
11:aisl.  melr  ,Sandhügel'  {*melha-),  schwed.  dial.  mjäg  {*melga-)  ds. lett.  smelknes  , Mehlabfall',  smalknes  ,Feilstaub,  Sägespäne',  smalks  ,fein' smulksne  ,Stäubchen,  Kleinigkeit';
12:lit.  smulküs  ,fein',  smülkti  ,fein  werden^,  smulkme  .Kleinigkeit' ; lit.  smiltiSj  lett.  srmlts,  smilkts  ,Sand'.
23:720  '
26:Gr.  ix6XX(x),  Fut.  ^eXlrjaü)  ^zögere,  bin  im  Begriffe^  (f^ölLg  ,lfaum^?\. fiiXsi  liOL  ,es  liegt  mir  am  Herzen'_,  nelo),  -Ofjai,  -rjow^  {.is^rjXa  (dor.  H€(.iGXa\ f^€(.tßXsT(Xi  ,am  Herzen,  im  Sinne  liegen,  besorgt  sein',  iisXidrjy  ^eX£d(i)v ueUöri^ia  ,Sorge^,  fieXerr]  ds.,  ^sXhcoQ  ^Fürsorger' ;  lat.  prö-mellere  (-ZZ-  =-, -In-)  ,litem  prömovere^,  re-mellgö  ,remoratrix',  re-mulcum  ,Schlepptau' prö-mulcum  ds. ;  air.  mall  (*ml-so-)  ,langsam^
30:Eine  durch  g(h)  erw.  Wurzelf.  ist  vielleicht  mel'gh-  ^schwellen',  s.  dort.
43:721
64:722
76:znelg-  (oder  nielog;-? )  .abstreifen,  wischen*,  europ.  , melken* ;  Präs.  melg-mi, PI.  WLclg-mes,  Partiz.  Perf.  Pass.  mlg-tö-]  molgo-  , Melken'.
79:723
81:lat.  mulgeö,  -ere,  mulsi,  mulctus  (=  ai.  mYstd-  ,abgewiseht')  ,melken* (aus  *molgeiö  :  lit.  mdlzau,  mdlzyti),  auch  prö-mulgäre  legem  ,ein  Gesetz verkünden'  (,*hervorziehen');  mulctra  , Melkkübel';
```


### [2026-09-07T16:11:46.897Z] TOOL RESULT

```
### LEAF 382
qti  ,verstummen'  ( :  ir.  malcaim  ,verfaule') ;  bulg.  serb.  mläk .lauwarm',  usw.  dazu  lit.  mülkis  (^mlkios)  .Dummkopf.
Mit  -sko-:  got.  un-tila-malsks  .unbesonnen',  as.  malsc  ,stolz'.  nhd.  mulsch .weich',  mulschen  dial.  .schlafen'.
WP.  II  284  ff.,  WH.  I  508,  II  16,  103  ff.,  Trautmann  167  f.,  177,  184, 188.
2.  mel-  ,verfehlen.  trügen';   nicl-io-  .böse'.
Av.  mairya-  , betrügerisch,  schurkisch':  arm.  mei,  PI.  meilh  .Sünde';  gr. idlsog  .vergeblich,  nichtig,  unglücklich,  elend'  (scheint  als  * i-islslal^og  auf dem  -e5-St.  *meles-  zu  beruhen,  dessen  schwächste  Stufe  *mls-,  ßXaa- vielleicht  in  ßXda-(p7]i.iog  als  .Verfehltes,  Unpassendes  sagend');  vielleicht I-ivXt)  ,Mißgeburt'?  zu  ä^ßXlaytcü,  d^ßXöü)  .tue  eine  Fehlgeburt';  mir.  mell .Irrtum,  Fehler'  {*mel-s-os,  vom  es-St.).  mellaim  ,betrüge'.  maile  , Böses'; cymr.  maZZ  , verderbt'  (*7nZso-);  lit.  melas  ,Lüge'.  lett.  PL  m^li  ds.,  mäldit
720  '
girren,  sich  versehen^^  mxildet  ^herumirren,  phantasieren^  sich  plagen^  mkUi , verwirrt  redend WP.  II  291.
5.  mel-  , zögernd
Gr.  ix6XX(x),  Fut.  ^eXlrjaü)  ^zögere,  bin  im  Begriffe^  (f^ölLg  ,lfaum^?\. fiiXsi  liOL  ,es  liegt  mir  am  Herzen'_,  nelo),  -Ofjai,  -rjow^  {.is^rjXa  (dor.  H€(.iGXa\ f^€(.tßXsT(Xi  ,am  Herzen,  im  Sinne  liegen,  besorgt  sein',  iisXidrjy  ^eX£d(i)v ueUöri^ia  ,Sorge^,  fieXerr]  ds.,  ^sXhcoQ  ^Fürsorger' ;  lat.  prö-mellere  (-ZZ-  =-, -In-)  ,litem  prömovere^,  re-mellgö  ,remoratrix',  re-mulcum  ,Schlepptau' prö-mulcum  ds. ;  air.  mall  (*ml-so-)  ,langsam^
WP.  II  291  f.,  WH.  II  370/427  f.
4.  mel-  , stark,  groß^
Gr.  (xdXa  ,sehr^,  (xäXXov  ,mehr'  (für  *(j,iXXov  =  lat.  melius  eingetreten nach  d^äaaovj  d^äzTov  :  Tax«),  ix&XiOTa  ,am  meisten^;  lat.  melior  ,besser' (ursprüngl.  ,*stärker^);  multus  ,vieP  {*mlto-)\  hierher  multa,  älter  molta ,Strafe,  Buße',  multö,  -äre  ,bestrafe',  Dialektwort,  vgl.  osk.  moltam  ,multam' moltaum  ,raoltare'^,  multasikad  ,multaticia',  umbr.  motar  ,multae',  mutu ,multa'  (*mltä  ,Vergütung,  Ersatz';  vgl.  germ.  *bötö  ,Buße' :  *bata-  ,besser')j lett.  milns  ,sehr  viel'.
Eine  durch  g(h)  erw.  Wurzelf.  ist  vielleicht  mel'gh-  ^schwellen',  s.  dort.
WP.  II  292,  WH.  II  63  f.,  123  f.
5.  mel-  ,Glied;  zusammenfügen'.
Ai.  mdrman-  n.  ,Glied,  offene,  ungeschützte  Körperstelle',  arm.  marmin ,Leib,  Fleisch'  (aus  dem  Iran?),  lit.  melmenys  ^Fleisch  an  den  Nieren', lett.  melmeni  .Weichen,  Lenden';  anders  Mühlenbach-Endzelin  II  596  (aus *meldm-  zu  S.  718);
gr.  (.isXog  n.  , Glied'  und  ,gegliederte  Weise,  Gesang,  Melodie',  daher fxeXiCu)  , besinge';  bret.  mell  m.,  corn.  mel,  PL  mellow  , Knöchel',  cymr. cym-mal  ,articulus,  junctura,  commissura'  (urkelt.  
### LEAF 383
*melsO'  :  (.leXog  ==  lit. tamsid:a,i.  tdmas  n.);  toch.  AB  mälk-  , zusammenfügen'.
WP.  II  292.
6.  mel-,  mela-  in  Farbbezeichnungen,  bes.  von  dunklen,  unreinen,  schmut-
zigen   Farbentönen ;    Schmutz,    beschmutzen' ;    melo-no-   ,schmutzigS Ai.  malind-  , schmutzig,  schwarz',  mlä-na-  , schwarz,  dunkelfarbig',  mala-
m.  n.  , Schmutz,  Unrat,  Sünde';
gr.   ueXäg,    -aiva,    -äv    ,schwarz'    (wohl    für  *[.isXavog    nach    dem    Fem.
(xsXaLva    =   ai.    malini),    ^iXiog    , Rötel',    fxoXvvco    , besudle'    (vielleicht    aus
721
*uaUvix)),  ^vllog  , Rotbarbe'  (Ablaut  wie  lat.  mulleus,  lit.  mulvas),  mit ^Stufe  ixü)Xwip  , Striemen,  blutunterlaufene  Stelle';
alb.  mel-ene  (KoUekt.  *mel-imo-)  ,Ulme'  (von  der  Farbe  des  Holzes), .jjiel-eze  ds.,  mjere  »unglücklich'  (*mel-ro-  ,schwarz'),  usw.  ;
vorrom.   *melix,  -ice  (frz.  meleze)  , Lärche^;
lat.  mulleus  , rötlich,  purpurfarben'  (*mHneios) ;  vgl.  ahd.  mol  S.  717 ;
got.  mela  Nom.  PL  , Schriftzeichen',  meljan  »schreiben',  ahd.  ana-mali ^Fleck,  Narbe',  mhd.  mal  n.  ,Fleck',  ahd.  mälön,  -en  .malen,  zeichnen', anorw.   mmla   , färben,   malen'   (ursprüngl.   ,mit   schwarzer  Farbe   malen');
halt.  *melna-  (*meh-no-)  in  lett.  m^lns  , schwarz',  apr.  meine  , blauer Fleck',  lit.  melsvas  , bläulich'  (auch  lit.  meletä,  -ata  »Grünspecht;  Hasel-, Waldhuhn',  apr.  melato  ,Grünspecht'?);  lit.  m^las,  melynas  ,blau',  melyne , blauer  Fleck  infolge  eines  Schlages',  lett.  me}s  , dunkelblau'  {*melias);  apr. milinan  Akk.  fem.  , Fleck';  lit.  mölis,  lett.  mdls  ,Lehm';
mit  i/-farbiger  Red.-Stufe:  lit.  mulvas  , rötlich,  gelblich',  mulv-yti,  -inti , beschmieren',  mulve  , Schlamm,  Sumpf;
russ.  malina  , Himbeere,  Brombeere'.
WP.  II  293 f.,  WH.  II  122  f.,  Trautmann  177  f.,  188.
7.  mel-  , Wolle,  Wollgewand'?
Gr.  iiallog  (*ml-nö-)  , Zotte,  Flocke';  lit.  rnilas  ,Tuch',  lett.  mil(n)a jgrobes  Tuch',  apr.  milan  ds.  (skr.  mälje.  Gen.  mäljä  PL  f.  , Flaum,  Milch- haar' ist  Lw.  aus  ngr.  jimAAtd  PL).
WP.  II  294.
B.  mel-j  xnelQ-  :  mlö-  »hervorkommen,  erscheinen,  hochkommen;  Erhöhung, Wölbung';  molä  ,Ufer^
Vielleicht  ai.  mani-  ,Perle',  manika-  m.  »(runder)  Wassertopf';  gr.  (xoXetv , gehen,  kommen'  (Aor.),  Präs.  ßlojaxu),  Perf.  (xs^ßXü}v,a]  eßXo)'  i(pdvr]' aüT6-(.ioXoq  , Überläufer',  TtQO-fioXrj  , Auslauf  eines  Berges,  Flusses',  ^oXsvo) »beschneide  die  Pflanzenschößlinge' ;
venet.  FIN  Mal-ont-ina  »Maltein'  (Kärnten),  südillyr.  ON  Malontum, usw.  (Krabe,  Würzburger  Jahrb.  1,  214);
alb.  waZ  ,Berg'  {*mol-no-)',  tosk.  maje  , Spitze,  Gipfel'  (*mol{a)',  alb.  mol jWald'  (, Bergwald)  aus  *melo-'^  geg.  moje  , hochgelegener  Ort'  (*meZ-iä); vorrom.  malga  ,  Alpen  wirtschaff  (*mal-ika)]
air.  Akk.  PL  mailgea  (*mal-ik-),  mir.  Nom,  Sg.  mala  ,Augenwimper' ; mell  , Klumpen,  Hügel'  (*mel-no-)  =  bret.  mell  »großer  Ball';  mir.  mul , Kugel,  Klumpen'  {*molu-),  mul-lach  , Gipf
### LEAF 384
el,  Scheitel';  abrit.  Inselname MaXaiog,  später  Malea  Insula  (Adamnan),  neugael.  Muile  ,Mull';
46
722
lett.  mala  f.  ,Rand,  Ufer,   Gegend';  lit.  lyg-mala  ,Höhe  des  Randes*- serb.  iz-mollm,  iz-mbliti  , hervorzeigen'   (d.  h.  kausatives  »hervorkomm
lassen'),  slov.  moliti  , hinstrecken,  hinhalten',  moZ^^i, ragen,  hervorragen*,  us*». . WP.  II  294 f.,  Jokl  L.-k-U.  162,  ßerneker  II  74,  J.  Loth  RC.  44,  293«!
46,  161  f.  '  *
1.  meldh-  , rituelle  Worte  an  die  Gottheit  richten*.
Arm.  maUem  ,ich  bitte' ;  asächs.  meldön  , angeben,  erzählen',  ahd.  melda , Angeberei,  Verleumdung',  meldön,  -en  , melden,  angeben,  verraten',  a»«" meld  , Bekanntmachung' ;  lit.  meldziü,  melsti  , bitten,  beten',  waZcZa  f.  , Bitte* Gebet',  Iterat.  maldaü,  maldyti;  apr.  maddla  , Bitte,  Gebet';  auf  Grund von  Dissimilation  von  *mold-lä  zu  *modlä  , Bitte'  :  cech.  modla  , Götzenbild Tempel'  und  poln.  modia  f.  , Gebet';  mit  -dl-  zu  -l- :  aksl,  rnoljg,  moliti jbitten',  refl.  , beten',  usw. ;  aus  , weihen  und  schlachten'  dann  ,zu  bestimmter Zeit  schlachten'  in  russ.  moUth,  usw. ;
hitt.  ma-al-ta-i,  ma-al-di  (mala)  , betet'.
WP.  II  289,  291,  WH.  II  20,  Trautmann  177,  Benveniste  BSL.  33, 133  ff.,  Mudge  Lg.  7,  252.
2,  meldh-  , Blitz,  Hammer  des  Donnergottes'.
Cjmr.  PI.  melltj  Sg.  -en  , Blitz*,  mit  sekundärem  t]
aisl.  mjgllnir  , Thors  Hammer'  (*meld[ii']nnaz)]  dazu  aisl.  poet.  myln , Feuer' ;  apr.  mealde  (*meldiä)  , Blitz',  tiefstufig  lett.  milna  i^mildna)  ,der Hammer  des  Donnerers';  wruss.  maZacZna  ,  Blitz' (*weZcZ57ia),  tief  stufig  abg. mhntji,  russ.  mölnija  ds.  (*mbldnhji).
WP.  II  300,  Trautmann  177.
znelg-  (oder  nielog;-? )  .abstreifen,  wischen*,  europ.  , melken* ;  Präs.  melg-mi, PI.  WLclg-mes,  Partiz.  Perf.  Pass.  mlg-tö-]  molgo-  , Melken'.
Ai.  märäti,  märjati,  rnfjäti  , wischt,  reibt  ab,  reinigt',  Partiz.  Perf.  mrstd-, s-Präs.  mxksdti  , streicht,  reibt,  striegelt',  mrksdyati,  mraksdyati  , bestreicht*; av.  mardzaiti,  mdrdzaiti  , berührt  streifend',  zastä-marsta-  , durch  Hand- schlag (d.  i.  Berührung  der  Hände)  geschlossen  (Vertrag)';  d-Präsens  ai. mrddti,  mrddyati  ,ist  gnädig,  verzeiht,  verschont',  av.  mdrdzdä-  ,verzeihen' {mdrdzdika-,  marzdika-  ,sich  erbarmend',  n.  , Barmherzigkeit');  diese  ar. Worte  können  auch  *merg-  enthalten ;  nichtpalatalen  Guttural  zeigt  ai. nir-märgd-h  »Verwischung;  Abgestreiftes,  Abfall',  ni-mxgra-  , sich  anschmie- gend', vi-mjrgvari  f.  , reinlich',  apämargdh-  ,Achyranthes  aspera'  (J.  Schmidt KZ.  25,  114);
\
723
crr.  äusXyo)  »melke',  hom.  h  vvY.xdq  d(.wXy(p  ,im  Augenblick  des  nächt- lichen Melkens';  iTturj^olyög,  ßovfioXyög  ,Roß-,  Kuhmelker',  d^olyevg, i^sU'J^nQ  ,MelkküheP;
lat.  mulgeö,  -ere,  mulsi,  mulctus  (=  ai.  mYstd-  ,abgewiseht')  ,melken* (aus  *molgeiö  :  lit.  mdlzau,  mdlzyti),  auch  prö-mulgäre  legem  ,ein  Gesetz verkünden'  (,*hervorziehen');  mulctra  , Melkkübel';
mir.  hligim  ,ich  melke'  (aus  *mligim),  Perf
```


## [2026-09-07T16:12:04.554Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD mel roots ===\"; grep -n \"^mel-\\|^melə\\|^meld\\|^mel\\b\\|^mel[a-z]*-\" AHD_watkins1985.txt | head -30; echo \"=== AHD context mel ===\"; grep -n -A12 \"^mel-1\" AHD_watkins1985.txt | head -60"
}
```


### [2026-09-07T16:12:04.615Z] TOOL RESULT

```
=== AHD mel roots ===
735:mele-
737:melg-
739:melg-. To rub off; also to milk. I. 1. Zero-grade form *mig- in Latin mulgére, to milk: EMULSION. 2. Full-grade form *melg- in Germanic *melkan, to milk, was contami- nated with an unrelated noun for milk, cognate with the Greek and Latin forms given in II. below, to form the blend *meluk- in: a. Old English meolc, milc, milk: MILK; b. suffixed form *meluk-ja-, giving milk, in Old English -milce, milch: MILCH Cc. Old High German miluh, milk: MILCHIG. II. Included here to mark the unexplained fact that no common Indo-European noun for milk can be reconstructed is another root *g(ajlag-, *g(a)lakt-, milk, found only in: a. Greek gala (stem galakt-), milk: (GA- LACTIC), GALACTO-, GALAXY; AGALACTIA, POLYGALA; b. Latin lac (stem lact-), milk: (LACTATE), LACTEAL, LACTESCENT, LACTO-, LETTUCE; C. the blended Germanic form cited in I. 2. above. [Pok. melg- 722, glag- 400.]
740:melit-. Honey. 1. Greek meli, honey: HYDROMEL, MARMA- LADE, MELILOT, OENOMEL. 2. Latin mel (stem meil-), honey: MELLIFEROUS, MELLIFLUOUS, MOLASSES. 3. Ger- manic *melith- in compound *melith-dauwaz (*dauwaz, dew; see dheu-?), honeydew (a substance secreted by aphids on leaves; it was formerly imagined to be distilled from the air like dew), in Old English mildéaw, honey- dew, nectar, later also mildew: MILDEW. [Pok. melit- 723.]
743:melst-. To burgeon. Zero-grade form *mist- in Greek blastanein, to burgeon, and blastos, shoot, bud, hence embryo, germ: -BLAST, BLASTEMA, BLASTO-, BLASTULA. [Pok. melédh- 725.]
=== AHD context mel ===
```


## [2026-09-07T16:12:04.828Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN amalgam ===\"; grep -n -i -B2 -A14 \"^amalgam\" KLN_1966.txt | head -60"
}
```


### [2026-09-07T16:12:04.899Z] TOOL RESULT

```
=== KLN amalgam ===
2389-(formed  on  the  analogy  of  the  plural  sumus,  ‘we are’),  OSlav.  jesmi,  Lith.  esmi,  OPruss.  asmai, OIr.  am,  ‘I  am’,  fr.  I.-E.  base  *es-,  ‘to  be’.  See esse  and  cp.  are,  art,  is.
2390-Amabel,  fem.  PN.  — ■  Lit.  ‘lovable’,  fr.  L.  arnd- bilis,  fr.  amare,  ‘to  love’.  See  amatory  and  cp. the  PN.s  Amandus,  Amanda,  Amy. amadou,  n. ,  a  spongy  substance.  —  F.,  fr.  Proven?. amadou,  lit.  ‘loving,  amorous’,  fr.  L.  amator , ‘lover’  (see  amatory) ;  so  called  from  the  inflam¬ mability  of  the  substance, amain,  adv.  —  Formed  fr.  a-,  on  ,  and  main, ‘strength’.
2391:amalgam,  n.,  i)  a  mixture  of  mercury  with  a metal  or  metals ;  2)  a  mixture,  blend.  —  F.  amal- game,  fr.  ML.  amalgama,  dissimil.  fr.  Arab,  al- malgham,  which  is  formed  fr.  Arab,  al-,  the and  Syr.  malagmd,  fr.  Gk.  paXocyp-a,  ‘a  soft mass’,  fr.  paXdcmeiv,  ‘to  soften’,  fr.  paXaxo?, ‘soft’.  See  malaco-  and  cp.  Amalthaea. Derivatives:  amalgam,  v.  (q.v.),  amalgam-ate, tr.  and  intr.  v.,  amalgam-at-ion,  n.,  amalgam-al¬ ive,  adj.,  amalgam-at-or ,  n.,  amalgam-ist,  n., amalgam-ize,  tr.  v.,  amalgam-iz-al-ion,  n. amalgam,  tr.  and  intr.  v.,  to  amalgamate.  F.
2392:amalgamer,  fr.  amalgame.  See  amalgam,  n. Amalthaea,  Amalthea,  n„  the  nurse  of  Zeus (Creek  mythol.)  —  L.,  fr.  Gk.  ’ApdXffcia,  which is  prob.  rel.  to  paXdxxos;,  ‘soft,  light,  weak’, paXax6?,  ‘soft’.  See  malaco-  and  cp.  amalgam. Amanda,  fem.  PN.  —  Lit.  ‘worthy  to  be  loved’, fem.  of  amandus,  gerundive  of  amare,  ‘to  love’. See  amatory  and  cp.  Amabel  and  names  there referred  to.  For  other  Latin  gerundives  used  in English  cp.  agenda  and  words  there  referred  to. Amandus,  masc.  PN.  —  L.  See  prec.  word, amanuensis,  n.,  a  person  employed  to  write  from dictation;  secretary.  —  L.  amanuensis,  formed with  suff.  -ertsis  from  the  phrase  servus  a  manu, ‘a  servant  from  the  hand’,  i.e.  ‘a  servant  writing from  dictation’.  See  pref.  a-,  ‘from’,  and manual.
2393-Amara,  n.,  a  genus  of  beetles,  the  ground  beetle ( entomol .)  —  ModL.,  fr.  Gk.  AptApa,  ‘trench’ which  is  prob.  rel.  to  £pv],  ‘shovel,  mattock’
2394-59
2395-(whence  Siapav,  ‘to  cut  through,  clear  away’), and  cogn.  with  OSlav.  jama,  ‘a  pit’, amaranth,  n.,  1)  a  mythical  plant  that  never  fades; 2)  any  plant  of  the  genus  Amaranthus;  3)  purple color.  —  Gk.  apapavTO?,  ‘unfading ;  amaranth’, fr.  A-  (see  priv.  pref.  a-),  and  the  stem  of  pocpod- veiv,  ‘to  put  out,  quench,  extinguish,  to  make to  waste  away’,  fr.  I.-E.  base  *m'er-,  ‘to  rub, consume,  wear  away’;  see  smart,  v.,  and  cp. marasmus.  The  ending  of  amaranth  (for  amarant) is  due  to  the  influence  of  plant  names  formed with  Gk.  avffo;,  ‘flower’.
2396-amaranthine,  adj.,  1)  unfading,  undying;  2)  of purple  color.  —  Coined  by  Milton  fr.  amaranth and  adj.  suff.  -ine.
2397-Amaranthus,  n.,  a  genus  of  plants  (hot.)  —  ModL., fr.  Gk.  ApApavTo?.  See  amaranth, amargoso,  n.,  the  bark  of  the  goatbush.  —  Sp., lit.  ‘bitter’,  fr.  VL.  *amaricdsus,  fr.  L.  amarus. See  amarine.
2398-amarillo,  n.,  any  of  several  tropical  American trees.  — -  Sp.,  for  *ambarillo,  fr.  Arab,  'anbart, ‘amber-colored’,  fr.  'anbar,  ‘amber".  See  amber, amarine,  amarin,  n.,  a  poisonous  compound (chem.)  —  Formed  with  chem.  suff.  -ine,  -in,  fr. L.  amarus,  ‘bitter’,  which  is  cogn.  with  ON.  apr, ‘sharp',  Swed.,  Norw.,  Du.  amper,  ‘sharp,  bit¬ ter’,  OE.  ampre,  OHG.  ampfaro,  MHG.,  G. ampfer,  ‘sorrel’,  OI.  amiah,  amblah,  ‘sour’; wood  sorrel’,  Arm.  amok',  ‘sweet,  Alb.  taml'e, ‘(curdled)  milk’,  embls,  ‘sweet’ ;  fr.  I.-E.  *am-ro-, fr.  base  *am-,  ‘bitter’,  which  is  rel.  to  *omo-. Taw,  unripe’,  in  OI.  amah,  ‘raw,  unripe,  un¬ cooked’,  Gk.  cop.6<;,  of  s.m.  See  omo-,  ‘raw,  un¬ ripe’,  and  cp.  amargoso,  maraschino,  margosa, and  the  second  element  in  picamar.  For  the  -re¬ formative  element  cp.  Gk.  mx-po?,  ‘bitter’  (see picric).
2399-amaryllid,  n.,  any  plant  of  the  order  of  Amarylli- daceae  (hot.)  —  See  Amaryllis  and  -id. Amaryllidaceae,  n.  pi.,  an  order  of  plants.  — ModL.,  formed  with  suff.  -aceae  from  the  PN. ’ApapuXXi?,  gen.  ’ApiapoXXtScx;.  See  Amaryllis, a  genus  of  plants.
2400-Amaryllis,  n.,  name  of  a  shepherdess  in  Theocri¬ tus’  Idyls.  —  L.,  fr.  Gk.  ApixpuXXh;.
2401-Amaryllis,  n.,  a  genus  of  plants  (hot.)  —  From prec.  word.
2402-amass,  tr.  v.,to  pile  up.  — F.  amasser,  ‘to  accumu¬ late,  heap  up’,  fr.  Late  L.  *admassare,  fr.  ad- and  massare,  ‘to  heap  up’,  fr.  L.  massa,  ‘a  lump, mass’.  See  mass.
2403-Derivatives:  amass-er,  n.,  amass-ment,  n. amastia,  n.,  absence  of  the  breasts.  —  Medical L.,  fr.  Gk.  A^ixoto;,  ‘without  breasts’,  fr.  A- (see  priv.  pref.  a-)  and  piacrrS;,  ‘breast’.  See
2404-masto-  and  -ia.
2405-amateur,  n.  —  F.,  ‘lover  of  something,  amateur’, fr.  L.  amator  em,  acc.  of  amator,  ‘lover’,  fr.  ama- lus,  pp.  of  amare,  ‘to  love’.  See  amative. Derivatives:  amateur,  adj.,  amateur-ish,  adj., amateur-ish-ly,  adv.,  amateur-ish-ness,  n.
2406-Amati,  n.,  a  violin  made  by  a  member  of  the Amati  family  at  Cremona  (16th  and  17th  cent.) amative,  adj.,  pertaining  to  love,  amatory.  — Formed  with  suff.  -ive  fr.  L.  amatus,  pp.  of  amd- re,  ‘to  love’,  from  the  I.-E.  infantile  imitative base  *ama-,  whence  also  amita,  ‘father’s  sister’, amicus,  ‘friend’.  Cp.  Gk.  ASxpivEiv,  ‘to  love’ (Hesychius),  which  is  formed  fr.  Phrygian  in¬ tensive  pref.  AS-  and  *ap.veiv,  ‘to  love’.  See aunt  and  cp.  Amabel,  amadou,  Amanda,  Aman¬ dus,  amateur,  amenity,  amiable,  amicable,  amity, amorous,  amour,  enamor,  enemy,  enmity,  ina¬ morato,  inimical.
```


## [2026-09-07T16:12:20.508Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '725,742p' AHD_watkins1985.txt"
}
```


### [2026-09-07T16:12:20.548Z] TOOL RESULT

```
[margarités. Pearl. Greek noun of Oriental origin (prob- ably immediately from Iranian). Greek margarités, mar- garon, pearl: MARGARIC, MARGARIC ACID, (MARGARINE), MARGARITE!, MARGARITE?.]
mari-. Young woman. Suffixed form *mari-to-, “provided with a bride,” in Latin maritus, married, a husband: MARITAL, MARRY!. [Pok. merio- 738.]
marko-. Horse. 1. Germanic *marhaz in Old High Ger- man marahscalc, “horse-servant” (Germanic *skalkaz, slave; see skalkaz), hence groom, later a title for a cavalry leader, akin to the Germanic source of Old French mareschal, cavalry officer: MARSHAL. 2. Ger- manic feminine *marhjén- in Old English mere, miere, mare: MARE}. [Pok. marko- 700.]
[mas. Male. Latin adjective of unknown origin. Deriva-
mat-
tive masculus, male, manly: MACHO, MALE, MASCULINE; EMASCULATE.] mat-. A kind of tool. Old English mattuc, mattock (prob- ably borrowed from Vulgar Latin *mattea): MATTOCK. [Pok. 2. mat- 700.] mater-. Mother. Based ultimately on the baby-talk form ma-2, with the kinship term suffix -fer-. 1. Germanic *méthar- in Old English mddor, mother: MOTHER}. 2. Latin mater, mother: MATER, MATERNAL, MATERNITY, (MATRICULATE), MATRIX, MATRON; MADREPORE, MATRI- MONY. 3. Greek métér, mother: METRO-; METROPOLIS. 4, Latin mdteriés, materia, tree trunk (< “matrix,” the tree’s source of growth), hence hard timber used in carpentry, hence (by a calque on Greek Aulé, wood, matter) substance, stuff, matter: MATERIAL, MATTER. 5. Greek compound Démétér, name of the goddess of produce, especially cereal crops (dé-, possibly meaning “earth”): DEMETER. [Pok. mdter- 700.] math-. Worm. With uncertain preform, but clearly re- lated, is Old English moththe, moth: motu. [Pok. 1. math- 700.] [Mawort-. Name of an Italic deity who became the god of war at Rome (and also had agricultural attributes), hence also the name of the planet Mars (doubtless from its red color, the color of blood). Latin Mars (stem Mart-), Mars: MARCH, MARS, MARTIAL, MARTIAN.] mazdo-. Pole, rod, mast. Germanic *mastaz in Old Eng- lish mest, mast: MAST}. [Pok. mazdo-s 701.] me-1. Oblique form of the personal pronoun of the first person singular. For the nominative see eg. 1. Germanic *mé- in Old English mé (dative and accusative): ME, MYSELF. 2. Possessive adjective “mei-no- in Germanic *min- in: a. Old English min, my: MINE?, My; b. Middle Dutch mijn, my: MYNHEER. [Pok. 1. me- 702.] me-2, In the middle of. 1. Suffixed form *me-dhi in Germanic *mid- in Old English mid, among, with: MID- WIFE. 2. Suffixed form *me-ta in Greek meta, between, with, beside, after: META-. See also medhyo-. [Pok. 2. me- 702.] mé-1, Expressing certain qualities of mind. Contracted from *meo-. 1. Suffixed o-grade form *mé6-to- in Ger- manic *méthaz in (i) Old English méd, mind, disposition: MooD! (ii) Old High German muot, mind, spirit, in German Gemiit, spirit, feelings, temperament: GEMUT- LICH, GEMUTLICHKEIT. 2. Perhaps Latin més (< *mé-s-), wont, humor, manner, custom: MORAL, (MORALE), MORES, MOROSE. [Pok. 5. mé- 704.] m6-2, To measure. Contracted from *meo-. I. Basic form mé-. 1. Suffixed form *mé-lo- in Germanic *mélaz in Old English m#l, “measure, mark, appointed time, time for eating, meal”: MEAL?; PIECEMEAL. 2. Suffixed form *mé-ti- in Latin métiri, to measure: MEASURE, (MEN- SURAL); (COMMENSURATE), DIMENSION, IMMENSE. 3. Possibly Greek metron, measure, rule, length, propor- tion, poetic meter (but this is referred by some to med-): METER!, METER?, (METER?), -METER, METRICAL, -METRY; DIAMETER, GEOMETRY, ISOMETRIC, METROLOGY, METRO- NOME. 4, Suffixed form *mé-trd- in Sanskrit mdtrd, a measure: MAHOUT. II. Extended and suffixed forms *mén-, *mén-en-, *mén-s-, *mén-dt-, moon, month (an ancient and universal unit of time measured by the moon). 1. Germanic *ménén- in Old English ména, moon: Moon; (Monpay). 2. Germanic *ménéth- in Old English ménath, month: MONTH. 3. Greek mén, méné, month: AMENORRHEA, CATAMENIA, DYSMENORRHEA, (MENARCHE), MENISCUS, MENOPAUSE. 4. Latin ménsis, month: MENSES, MENSTRUAL, (MENSTRUATE); BIMES- TRIAL, SEMESTER, TRIMESTER. [Pok. 3. mé- 703, ménot- 731. fen Big. Contracted from *meo-. 1. Suffixed (compara- tive) form *mé-is- in Germanic *maiz6n- in Old English mara, greater, and madre (adverb), more: MORE. 2. Suf- fixed (superlative) form *mé-isto- in Germanic *maista- in Old English m&st, most: Most. 3. Suffixed o-grade
meg-
form *m6-ro- in Gaelic mor, big, great: CLAYMORE. [Pok. 4, mé- 704.] mé-4, To cut down grass or grain with a sickle or scythe. Contracted from *mea-. 1. Germanic *mé- in Old English mawan, to mow: Mow?. 2. Suffixed form *mé-ti- in Germanic *médiz in Old English m#th, a mowing, a mown crop: AFTERMATH. 3. Suffixed form *mé-twd-, a mown field, in Germanic *médw6 in Old English méd (oblique case m&@dwe), meadow: MEAD?, MEADOW. [Pok. 2. mé- 703.] med-. To take appropriate measures. 1. a. Germanic *metan in Old English metan, to measure (out): METE!; b. Germanic derivative *m#t6, measure, in Old English gem&te (ge-, with; see kom), “commensurate,” fit: MEET?. 2. a. Latin medéri, to look after, heal, cure: MEDICAL, MEDICATE, (MEDICINE), (MEDICO); METHEG- LIN, REMEDY; b. Latin meditdri, to think about, con- sider, reflect: MEDITATE. 3. Suffixed form *med-es-, replaced in Latin by *modes- by influence of modus (see 4. below), in: a. Latin modestus, “keeping to the appro- priate measure,” moderate: MODEST; IMMODEST; b. Lat- in moderdre, “to keep within measure,” to moderate, control: MODERATE; IMMODERATE. 4. Suffixed o-grade form *mod-o- in Latin modus, measure, size, limit, man- ner, harmony, melody: MODAL, MODE, MODEL, MODERN, MODICUM, MODIFY, MODULATE, MODULE, MODULUS, MOLD!, (MOOD?), (MOULAGE); (ACCOMMODATE), (COM- MODE), COMMODIOUS, (COMMODITY). 5. Suffixed o-grade form *mod-yo- in Latin modius, a measure of grain: MODIOLUS, MUTCHKIN. 6. Possibly lengthened o-grade form *méd- in Germanic *mét-, ability, leisure, in: a. Old English métan, to have occasion, to be permitted or obliged: MOTE2, MUST}; b. Germanic compound é-mot-ja- (prefix *é-, meaning uncertain, from Indo- hinppoes é, 6; see Pok. é, 6 280) in Old English émetta, rest, leisure: EMPTY. [Pok. 1. med- 705.] medhu-. Honey; also mead. 1. Germanic *medu in Old English meodu, mead: MEAD!. 2. Greek methu, wine (> methuein, to be intoxicated): AMETHYST, METHYLENE. [Pok. médhu 707.] medhyo-. Middle. 1. Germanic *midja- in: a. Old English midd(e), middle: M1D!; AMID; b. West Germanic diminu- tive form *middila- in Old English middel, middle: MIDDLE; Cc. Germanic compound *midja-gardaz, “middle zone” (*gardaz, enclosure, yard; see gher-1), name of the earth conceived as an intermediate zone lying between heaven and hell, in Old Norse Midhgardhr, Midgard: MipGarD. 2. Latin medius, middle, half: MEAN, MEDIAL, MEDIAN, MEDIASTINUM, MEDIATE, MEDIUM, MITTEN, MIZZEN, MOIETY, MULLION; INTERMEDIATE, MEDIEVAL, MEDIOCRE, MEDITERRANEAN, MERIDIAN, MILIEU. 3. Greek mesos, middle: MESO-. See also me-2. [Pok. medhi- 706.] meg-. Great. 1. Germanic suffixed form *mik-ila- in: a. Old English micel, mycel, great: MUCH; b. Old Norse mikill, great: MICKLE. 2. Suffixed form *mag-no- in Latin magnus, great: MAGNATE, MAGNITUDE, MAGNUM; MAG- NANIMOUS, MAGNIFIC, (MAGNIFICENT), (MAGNIFICO), (MAGNIFY), MAGNILOQUENT. 3. Suffixed (comparative) form *mag-yos- in: a. Latin major, greater: MAJOR, MAJOR-DOMO, MAJORITY, MAJUSCULE, MAYOR; b. Latin majestds, greatness, authority: MAESTOSO, MAJESTY; c. Latin magister, master, high official (< “he who is greater”): MAESTRO, MAGISTERIAL, MAGISTRAL, MAGIS- TRATE, MASTER, (MISTER), MISTRAL, (MISTRESS). 4. Suf- fixed (superlative) form *mag-samo- in Latin maximus, greatest: MAXIM, MAXIMUM. 5. Suffixed form *mag-to-, “made great,” in Latin mactus, worshiped, blessed, sacred: MATADOR. 6. Suffixed (feminine) form *mag-ya-, “she who is great,” in Latin Maia, name of a goddess: May. 7. Suffixed form *meg-a-l- in Greek megas (stem megal-), great: MEGA-, MEGALO-; ACROMEGALY, ALMA- GEST, OMEGA. 8. Variant form *megh- in Sanskrit maha-,
mei-'
mahat-, great: MAHARAJAH, MAHARANI, MAHARISHI, MAHATMA, MAHAYANA, MAHOUT. [Pok. meg(h)- 708.] mei-'. To change, go, move; with derivatives referring to the exchange of goods and services within a society as regulated by custom or law. 1. Latin medre, to go, pass: MEATUS; CONGE, IRREMEABLE, PERMEATE. 2. Suffixed o-grade form *moi-t- in: a. Germanic *ga-maid-az (*ga-, intensive prefix; see kom), “changed (for the worse),” abnormal, in Old English gemdd, insane: MAD; b. Latin mitdre, to change: MEW!, MOLT, MUTATE; COMMUTE, PERMUTE, REMUDA, TRANSMUTE; C. Latin miituus, “done in exchange,” borrowed, reciprocal, mutual: MUTUAL. 3. Suffixed extended zero-grade form *mit-to- in Ger- manic “missa-, “in a changed manner,” abnormally, wrongly, in: a. Old English mis-, mis-: Mis-!; b. Old Norse mis(s), mis(s)-, miss, mis-: AMISS, MISTAKE; C. Ger- manic *missjan, to go wrong, in Old English missan, to miss: MISs!, 4, Suffixed o-grade form *moi-n- in com- pound adjective *ko-moin-i-, “held in common” (*ko-, together; see kom), in: a. Germanic *gamainiz in Old English geméne, common, public, general: MEAN?; (DE- MEAN?); b. Latin commiinis, common, public, general: COMMON, COMMUNE, COMMUNICATE, (COMMUNISM). 5. Suffixed o-grade form *moi-nes- in: a. Latin minus, “service performed for the community,” duty, work, “public spectacle paid for by a magistrate,” gift: MUNICI- PAL, MUNIFICENT, REMUNERATE; b. Latin immiinis (in-, negative prefix; see ne), exempt from public service: IMMUNE. 6. Extended form *()meigv- in: a. Greek amei- bein, to change: AMOEBA; b. Latin migrdre, to change one’s place of living: MIGRATE; EMIGRATE. [Pok. 2. mei-, 3. mei- 710, meig¥- 713, 2. meit(h)- 715.] mei-2. Small. 1. Greek meidn, less, lesser: MEIOSIS; MIo- CENE. 2. Latin nimis, too much, very (< *ne-mi-s, “not little’; ne-, negative prefix; see ne). 3. Suffixed zero-grade form *mi-nu- in: a. Latin minuere, to reduce, diminish: MENU, (MINCE), MINUEND, MINUTE2; COMMI- NUTE, DIMINISH; b. Latin minor (influenced by the comparative suffix -or), less, lesser, smaller: MINOR, MINUS, MIS-!; MINUSCULE; GC. further suffixed (superla- tive) form *minu-mo- in Latin minimus, least: MINIMUM; d. Latin minister, an inferior, servant (formed after magister, master; see meg-): MINESTRONE, MINISTER, MINISTRY, MYSTERY?; @. Russian men’she, less: MENSHE- vik. [Pok. 5. mei- 711.] mei-3, To fix; to build fences or fortifications. 1. Suffixed o-grade form *moi-ro- in: a. Germanic *mair-ja- in Old English mére, boundary, border, landmark: MERE®; b. Latin miirus, wall: MURAL, MURAMIC ACID, MURE; IMMURE. 2. Suffixed o-grade form *moi-ni- in Latin miinire, to fortify, protect, strengthen: MUNITION; (AM- MUNITION), PRAEMUNIRE, PREMUNITION. 3. Possibly suffixed lengthened-grade form *méi-t- in Latin méta, boundary stone, limit: METE?. [Pok. 1. mei- 709.] mei-4, To tie. 1. Suffixed zero-grade form *mi-tro-, “con- tract, that which binds,” in: a. Greek mitra, headband, earilier a piece of armor worn around the waist: MITER; b. Old Persian Mithra-, name of a god (< “contract” < “bond”): MiTHRAS; c. Russian mir, commune, joy, peace (possibly borrowed from Iranian): mR. 2. Possibly a suffixed zero-grade form *mi-to- in Greek mitos, a warp thread: MITOSIS; DIMITY, MITOCHONDRION, SAMITE. [Pok. 4. mei- 710.] méGi-. Mild. Contracted from *meoi-. Suffixed zero-grade form *mi-ti- (< *mis-ti-) in Latin mitis, soft: MITIGATE. [Pok. 7. mei- 711.] meigh-. To urinate, 1. Germanic suffixed form *mih-stu-, urine, hence mist, fine rain, in: a. Old English mist, mist: MIST; b. Middle Dutch mieselen, to drizzle, perhaps akin to the source of Middle English misellen, to drizzle: MIZZLE; Cc. Germanic diminutive form *mihst-ila-, mistle- toe (which is propagated through the droppings of the missel thrush), in Old English mistel, mistletoe: (MISSEL THRUSH), MISTLETOE. 2. Suffixed form *migh-tu- in
mele-
Latin micturire, to want to urinate (desiderative of meiere, to urinate): MICTURATE. [Pok. meigh- 713.] meik-. To mix. 1. Variant form *meig- in Greek mig- nunai, to mix: AMPHIMIXIS, APOMIXIS, PANMICTIC, PAN- MIXIS. 2. Suffixed zero-grade form *mik-sk- in Latin miscére (past participle mixtus), to mix: MEDDLE, (MED- LEY), (MELANGE), MESTIZO, MISCELLANEOUS, MISCIBLE, MIX, MIXTURE; ADMIX, COMMIX, IMMIX, MISCEGENATION, (PELL-MELL), PROMISCUOUS. 3. Possibly a Germanic form *maisk- in Old English mdsc, macs, mdx, mashed malt: MASH. [Pok. meik- 714.] mei-no-. Opinion, intention. 1. Germanic *main- in Old English *mdn, opinion, complaint (> Middle English mone, complaint): MOAN; (BEMOAN). 2. Germanic *main- Jan in Old English ménan, to signify, tell, complain of, moan: MEAN}, [Pok. mei-no- 714.] mel-1, Soft; with derivatives referring to soft or softened materials of various kinds. I. Extended form *meld-. 1. Germanic *meltan in Old English meltan, to melt: MELT. 2. Possibly Germanic *miltja- in Old English milte, spleen, and Middle Dutch milte, milt: mit. 3. Possibly Germanic *malta- in Old English mealt, malt: MALT. 4. Suffixed variant form *mled-sno- in Greek blennos, slime, also a name for the blenny: BLENNY. 5. Suffixed zero-grade form *mid-wi- in Latin mollis, soft: MOIL, MOLLIFY, MOLLUSK, MOUILLE; EMOLLIENT; 6. Possibly nasalized variant form *mlad- in Latin blandus, smooth, caressing, flattering, soft-spoken: BLAND, BLANDISH. II. Variant form *smeld-. Germanic *smelt- in: a. Middle Dutch and Middle Low German smelten, to smelt: SMELT!; b. Old High German smalz, animal fat: SCHMALTZ; C. Italian smalto, melted glass: SMALT; d. Old French esmail, enamel: ENAMEL; e. perhaps Old English smelt, smylt, a marine fish, smelt: SMELT?. III. Extended form *meldh-. 1. Germanic *mildja- in Old English milde, mild MILD. 2. Possibly Greek maltha, a mixture of wax and pitch: MALTHA. IV. Suffixed form *mel-sko- in Ger- manic *mil-sk- in Old English melfi)sc, mylsc, mild, mellow (> Middle English melsche, friable): MULCH. V. Extended form *mfk- in Greek malakos, soft: CHON- DROMALACIA, MALACOLOGY, OSTEOMALACIA. VI. Possi- bly Celtic *molto-, sheep, in Old French moton, sheep: MUTTON. VII. Suffixed zero-grade form *()ml-u- in Greek amblus, blunt, dull, dim: AMBLYGONITE, AMBLY- opiA. [Pok. 1. mel- 716.] mel-2, Of a darkish color. 1. Greek melas, black: MEL- ANO-; MELANCHOLY, PSILOMELANE. 2. Greek mullos, a marine fish: MULLET; (SURMULLET). 3. Latin mulleus, reddish purple (used only to designate a ceremonial shoe worn by Roman magistrates): MULE. 4. Perhaps Ger- manic *mal- in Middle Dutch malen, to paint: MAUL- STICK. [Pok. 6. mel- 720.] mel-3. A limb. Greek melos, limb, hence a musical member or phrase, hence music, song, melody: MELISMA; ACRO- MELIC, MELODRAMA, MELODY. [Pok. 5. mel- 720.] mel-4. Strong, great. 1. Suffixed (comparative) form *mel-yos- in Latin melior, better: (AMELIORATE), MELIO- RATE, MELIORISM. 2. Suffixed zero-grade form *m/J-to- in Latin multus (neuter multum), much, many: MOLTO, MULTI-, MULTITUDE. [Pok. 4. mel- 720.] mel-5. Bad. Latin malus, bad, and male, ill (> malignus, harmful): MAL-, MALICE, MALIGN; DISMAL, MALADY, MALEDICT, MALEFACTOR, MALEVOLENT, MALVERSATION. [Pok. mélo- 724.] mel-€, Wool. Possibly suffixed zero-grade form *ml-no- in Greek mallos, wool. [Pok. 2. mel- 719.] mel-?. To miss, deceive. Germanic *mai- in Middle Dutch mal, foolish, silly: MALLEMUCK. [Pok. 2. mel- 719.] meldh-. To pray, speak words to a deity. Germanic *meld- in Old High German meldén, to proclaim, reveal: MELD}. [Pok. 1. meldh- 722.] mele-. Also mel-. To crush, grind; with derivatives referring to various ground or crumbling substances (such as flour) and to instruments for grinding or crush-
melg-
ing (such as millstones). 1. O-grade form *mol- in Ger- manic *mal- in: a. obsolete Dutch malen, to whirl: MAELSTROM; b. Germanic suffixed form *mal-mén- in Old English mealm-, perhaps “crumbling, friable” (only in compounds, as mealmstdn, sandstone): MALM. 2. Full-grade form *mel- in Germanic suffixed form *mel-wa- in Old English melu, flour, meal: MEAL}. 3. Zero-grade form *mJ- in Germanic *mul- in: a. suffixed form *mul-dé in (i) Old English molde, soil: MOLD? (ii) Old Norse *muldhra, to crumble, akin to the probable Scan- dinavian source of MOLDER; b. Middle Dutch mul, dust: MULL2, 4. Full-grade form *mel- in: a. Latin molere, to grind (grain), and its derivative mola, a millstone, mill, coarse meal customarily sprinkled on sacrificial animals: MILL!, MOLAR2, MOLE‘, (MOULIN); IMMOLATE, ORMOLU; b. suffixed form *mel-iyo- in Latin milium, millet: MEAL- IE, MILIUM, MILLET. 5. Suffixed variant form *mal-ni- in Latin malleus, hammer, mallet: MALLEABLE, (MALLET), MALLEUS, MAUL; PALL-MALL. 6. Zero-grade form *mlJ- in Greek mulé, mulos, millstone, mill: AMYLUM, MYLONITE. 7. Possibly extended form “mili- in: a. possibly Greek bliton, blite (a plant that in some varieties has dusty leaves): BLITE; b. Russian blin, pancake: BLINI, BLINTZ. [Pok. 1. mel- 716.]
melg-. To rub off; also to milk. I. 1. Zero-grade form *mig- in Latin mulgére, to milk: EMULSION. 2. Full-grade form *melg- in Germanic *melkan, to milk, was contami- nated with an unrelated noun for milk, cognate with the Greek and Latin forms given in II. below, to form the blend *meluk- in: a. Old English meolc, milc, milk: MILK; b. suffixed form *meluk-ja-, giving milk, in Old English -milce, milch: MILCH Cc. Old High German miluh, milk: MILCHIG. II. Included here to mark the unexplained fact that no common Indo-European noun for milk can be reconstructed is another root *g(ajlag-, *g(a)lakt-, milk, found only in: a. Greek gala (stem galakt-), milk: (GA- LACTIC), GALACTO-, GALAXY; AGALACTIA, POLYGALA; b. Latin lac (stem lact-), milk: (LACTATE), LACTEAL, LACTESCENT, LACTO-, LETTUCE; C. the blended Germanic form cited in I. 2. above. [Pok. melg- 722, glag- 400.]
melit-. Honey. 1. Greek meli, honey: HYDROMEL, MARMA- LADE, MELILOT, OENOMEL. 2. Latin mel (stem meil-), honey: MELLIFEROUS, MELLIFLUOUS, MOLASSES. 3. Ger- manic *melith- in compound *melith-dauwaz (*dauwaz, dew; see dheu-?), honeydew (a substance secreted by aphids on leaves; it was formerly imagined to be distilled from the air like dew), in Old English mildéaw, honey- dew, nectar, later also mildew: MILDEW. [Pok. melit- 723.]
mélo-. Also smé@lo-. Small animal. Zero-grade form *smalo- in Germanic *smal-, small animal, hence also “small,” in Old English smzl, small: SMALL. [Pok. mélo- 724.)
[mé@lon. An apple, or any seed- or pit-bearing fruit. Attic Greek noun (Doric mdlon), possibly borrowed from a Mediterranean language. Earliest form *maoalo-, attested in Hittite mahla-, grapevine. MELINITE, MELON; CHAMO- MILE, MALIC ACID, MARMALADE. ]
```


## [2026-09-07T16:12:43.407Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN leaf 235 (p.214) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==236' HRN.txt | head -60"
}
```


## [2026-09-07T16:12:43.694Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== CHEUNG marz ===\"; grep -n \"marz\\|\\*mard\\|mālīdan\\|malidan\" CHEUNG.txt | head -40"
}
```


### [2026-09-07T16:12:44.990Z] TOOL RESULT

```
=== HRN leaf 235 (p.214) ===
— 214 —
959. mäst saure Milch*, mäsiden gerinnen*.
skr. mdstU' 'saurer Rahm*.
arm. macum saure Milch', macanhn 'ankleben (intr.),
anhangen, gerinnen* (Hübschmann, No. 184), sowie
bei. maiay, pp. masfa *to freeze, curdle', mastay curds
(Dames), die Hübschmann ZDM6. 44, 561 ver-
gleicht, stimmen lautlich nicht genau.
960. mäS 'Erbse, Wicke'.
ai. mäsa- 'Bohne'; sar. ma/ Erbse*.
Kann im Indischen oder Iranischen (doch eher in
ersterem) Lehnwort sein.
961. fnäy 'Wasservogel' (Öähn. I, 444 Vers 191).
ai. madgü' , 'ein Wasservogel* (Hübschmann,
ZDMG. 38, 423).
962. mäliden 'reiben, glätten*, -mal (vergl. destmäV)
'Handtuch*); vergl. musten (No. 983).
aw. [/^marz-, marezaiti 'fegt*; phlv. ktin\marz,
dastän[marz, dösak[marz vd. 1 (18), marz(i)sn, 'Coitus*
(Bund.) 2), marzUan 'coitiren*, mälUan, mCU(i)8n; ai.
I/"7war/-, märsti 'abwischen*.
kurd. LW. malin 'fegen*; bei. LW, malay, malBnay (223)
reiben, mischen, streichen'; oss. märzin 'fegen* (180).
Vergl. Hübschmann, ZDMG. 44, 558; phlv. -marz
weist wohl auf ai. [/^niarj-, nicht auf ai. [/^mard-,
963. mäm 'Mutter' (Öähn. I, 41 Vers 129 u. o.), mama^),
mami,
cambr. corn. arem. mam 'Mutter; lit. mäma, momä
'Mutter; ksl. mama 'Mama*; alb. msmf (O. Meyer,
S. 272).
*) nii^NDDI (Is. 3, 22), vergl. kurd. LW. dasmcß (H.-8oh.). Bei
Polak, Persien I, 144 wird desmäl als gewöhnliche neupersisohe Form
citirt (Mitteilung von Herrn Prof. Justi), Baphael de Mans hörte
'anno 1660) dagegen destemol (Schefer, S. 109).
*) Np. merz *Coitus' ist nicht belegt. Np. jihmerz *Coitus mit
einer Hure' ist natürlich nur Umschrift aus dem PSzend.
^) Hierher gehört gewiss auch mah mäh guften (s. YuUers
8. V. mä}i\ dessen Erklärung in den persischen Originalwdrterbüchern
sehr thöricht ist (der Mond scheint doch nur selten, wenn die Kinder
gewaschen werden).
```


### [2026-09-07T16:12:45.036Z] TOOL RESULT

```
=== CHEUNG marz ===
6350:parallel chain: amarozon ... vimarozon ... framarozon (*Hmarz). 
12009:developments of the root *Hmarz ‘to rub, wipe’ (e.g. ВМР mlc- /marz-/ ‘to 
12339:*NWIR: ? Bal. mus-/musta ‘to smear, rub’ (< WIr. ?, cf. Pth./MP mwst, *Hmarz) || (+ 
12343:*NEIR: ? Pash. muz-/musal ‘to rub’ (also possible: *Hmarz), Wa. msırs-/morst ‘to 
12350:9 Evidently, this root is both formally and semantically similar to *Hmarz, which no 
12365:*Hmarz ‘to wipe, rub’ 
12376:*Hmarz 181 
12391:m’lytn /malidan/; Partic.: perf. pass. BMP m/’lyhst /malihist/ || LW: Pres.: SUBJ. 3pl. MMP mrz’nd; 
12420:*NWIR: NP mälidan/mäl- ‘to rub, polish; to chafe, box the ears’, Bal. marzit/marz- 
12425:|| (+ *ni-) Anar. nimärzi, Gz. nemärzün, nimárzün, Varz. nemarzin ‘broom’ || (+ 
12433:*NEIR: Oss. І. marzyn/marzt, D. marzun/marzt ‘to wipe, brush’, ? Pash. muz-/musal 
12442:rake’, Wa. nomürzg, nomórzg ‘harrow’, (?) Wa. lamarz ‘sloping down of a field’ 
12460:gwamel-, mäl-, marz-; Korn 2005: 97, 317, 404 
13447:Ile Rather *Hraiz ?) || (+ *а-) Oss. І. arzzyn/araezt, D. ar&zumarzzt ‘to be 
17574:266 *mard 
17589:ВМР gwmlc'k /gumarzag/ ‘the pernicious’ (Gershevitch 1977: 66) = DMMPP: 
17623:*mard ‘to despise, disparage (?); to neglect, abandon (?)’ 
17803:*NWIR: Bal. marzit/marz- ‘to absolve, forgive, bless, encourage, support’ || (+ *a-) 
17809:© The Пг. root *marzd has no IE correspondences. On the possible interpretations of 
17815:641b; Shahbakhsh: s.v. marz!-, amurz- 
17976:*SOGDIAN: MSogd. (’)ms (inch.) ‘to plough’ (or < *Hmarz ?, cf. Bal. marz- ‘to 
21046:ruf- (supplet. inf. mestén < *Hmarz), Anar. ha-..-ruft/ (impv.) ha-ru, Gz. rön-/ruft, 
35171:gwmlc 'k /gumarzag/, 
35350:mlc- /marz-/, 175 
41967:marz-, 272 
41968:marzit/marz-, 181, 269 
45090:nemarzin, 181 
46772:marzun/marzt (D), 181 
46773:marzyn/marzt (1), 181 
49572:lamarz, 182 
55097:*mard, *raic, *raz (S.V.), 
55116:*HiH (s.v.), *Hmarz (s.v.), 
55769:*Hranj (s.v.), *mard (s.v.), 
55774:*marzd (s.v.), *suan 
56311:*mard 
56313:Stat, *kan', *Hmarz (s.v.), 
56337:*mard 
56630:*marzd, *xsad 
56797:*xsad, *marzd 
57246:*mard
```


## [2026-09-07T16:12:56.337Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '12360,12470p' CHEUNG.txt"
}
```


### [2026-09-07T16:12:56.388Z] TOOL RESULT

```
*REFERENCES: EVP: 48; IIFL I: 401a; DKS: 86b f; Polomé 1989: 213; Werba 1997: 220; 
Steblin-Kamenskij 1999: 241; Cabolov 2001: 408; Kiefer 2003: 201; Shahbakhsh: s.v. mus-; Korn 2005: 
92, 132, 146 f., 405 


*Hmarz ‘to wipe, rub’ 

*AVESTAN: maraz- ‘to wipe, rub’ || (+ *anu-) ‘to sweep’ || (+ *a-) ‘to sweep to’ || (+ 
*pari-) ‘to brush, wipe around’ || (+ *fra-) ‘to wipe forth, away’ || (+ *ni-) ‘to sweep 
off? || (+ *ui-) ‘to sweep to and fro’ = Liste: 44 


Pres. them.: IND. 3sg. YAv. marezaiti (Yt 10.95), YAv. framarozaiti (V 4.3 f.), INJ. 35р. YAv. marazat 
(Yt 14.21, V 2.38), ҮАУ. pairi.marozat (Yt 17.22), 3du. YAv. anumarozatom (Yt 8.38), 3pl. YAv. 


*Hmarz 181 


amarozon ... vimarozon ... framarozon (Yt 14.45), OPT. 3sg. YAv. framorozoit (V 3.42), IMPV. 25р. YAv. 
maroza (V 2.30); Inf.: pres. n- OAv. ni... moraZdiiai (Y 44.14) 


*MIDDLE PERSIAN: BMP mwst /must/ (pret. stem), m’I- /mäl-/ ‘to rub, sweep’, BMP 
m’lyh- /malth-/ (pass.) ‘to be touched’ || LW: MMP mrz- ‘to mate, have sexual 
intercourse’, MMP *mrzyn- (caus.) ‘to cause to mate’ = DMMPP: 232a f., 234b, 


354a 

Pres.: IND. 3sg. BMP m’lyt /maléd/, 3р1. BMP т упа /malend/, IMPV. 2sg. BMP m’!/mal/; Inf.: BMP 
m’lytn /malidan/; Partic.: perf. pass. BMP m/’lyhst /malihist/ || LW: Pres.: SUBJ. 3pl. MMP mrz’nd; 
Partic.: perf. pass. MMP mrzyst, caus. MMP *mrzynyd 


*PARTHIAN: (+ *ni-) nmrz- ‘to clean, cleanse; make smooth’ = Ghilain: 53 | 
DMMPP: 243b 


Pres.: SUBJ. 1sg. nmrz’n; Partic.: perf. pass. nmwst 

*KHOTANESE: (+ *ati-) ttumals- (ttremvas-) ‘to devour, consume’ || (+ *aua-) LKh. 
vameys- ‘to rub down’ || (+ *ni-) nimals- ‘to rub down’ || (+ *ш-) ggumäls- 
(gumaly-) ‘to besmear’. 9 Khot. malys- ‘rub, crush, groom’, in DKS: 325a, does not 
exist. The attested form malstä can be interpreted differently, from *maré, on which 
see Sims-Williams, SVK Ш: 122 f. || On LKh. vameys- see Emmerick, SVK I: 110f. 
c SGS: 39, 119, 54 f., 29 f. 

*SOGDIAN: (+ *fra-) MSogd. fr’mrz- ‘to spoil’ || (+ *ni-) BSogd. nm’rz- ‘to touch’ || 
(+ *ui-) BSogd. wm(’)rz ‘to do violence, destroy’, SSogd. wmrst-, MSogd. wmst- 
(pret. stem) ‘to destroy; spoil’, SSogd. wmrzw ‘corruption, Verderben’ (AL2.56) 

(+ *fra-) Impf.: IND. 3sg. MSogd. fr’mrz; Partic.: perf. pass. MSogd. frmsty || (+ *ui-) Pres.: IND. 3sg. 
BSogd. wm’rzt, SUBJ. 3sg. MSogd. wmrz’t (BBB: 48); Pret.: tr. IND. 35р. SSogd. wmrstd’r (BBB: 100, 
ad e7); Pass.: pret. IND. 3sg. MSogd. wmstyy ’ktyy 


*CHORESMIAN: mZy- ‘to polish (the mill-stone)’ || (+ *upa-) bmZ- ‘to tuck up, roll up 
(of sleeves, sim.)’ || (+ *pari-) prmZ- ‘to touch, rub’ — Samadi: 114, 21, 154 

*NWIR: NP mälidan/mäl- ‘to rub, polish; to chafe, box the ears’, Bal. marzit/marz- 
(denomin.) ‘to stroke, harrow, plough’, Kurd. (Sor.) тайп/таі- ‘to rub; to wipe 
(off)’, borrowed into: Bal. malit/mal- ‘to rub in’, Gz. mäl-/mälä ‘to stroke, rub’, Gur. 
(Kand.) mäfä-, Khuns. mal-/mala ‘to smear, stroke’, Meim. bem-mä:la/a-mä:l-, 
Qohr. malada/mal-, Siv. mal-/mali ‘to rub’, Tal. mole ‘to wipe’, Gur. mäl- ‘to smear’ 
|| (+ *ni-) Anar. nimärzi, Gz. nemärzün, nimárzün, Varz. nemarzin ‘broom’ || (+ 
*ш-а) ? Bal. gwamelit/gwamel- ‘to besmear, soak, submerge’. © This Bal. word is 
not from *ui-mard- (*Hmard ‘to crush’), as suggested by Shahbakhsh. Although it is 
possible that the Bal. verb is related to Khot. ggumäls- ‘to besmear’ (*Hmars-), the 
-]- has nothing to with the Khot. -/- in ggumäls-. Bal. -/- rather points to borrowing, 
i.c. from Kurd./Pers., or, more likely, to contamination with Bal. mal-, which itself 
has been borrowed from Kurd./Pers. On Bal. -I-, see also Korn 2005: 159 ff. 

*NEIR: Oss. І. marzyn/marzt, D. marzun/marzt ‘to wipe, brush’, ? Pash. muz-/musal 
‘to rub’ (*Hmars is also possible), ? Sh. möyj, (Baj.) mayz, Rosh. mawz, Bart. 


182 *Hnaid 


möwzi, Sariq. morz ‘hunger’, Wa. mərz ‘hungry’ || (+ *uz-) ? Pash. ‘“zmogalay 
‘weakened (by a wound)’ (МЕУР: 102) || (+ *ni-) Sariq. nimiZg, nümüzg ‘harrow, 
rake’, Wa. nomürzg, nomórzg ‘harrow’, (?) Wa. lamarz ‘sloping down of a field’ 
(Lorimer) 

*MISC: ? Arm. (LW) merZem ‘I dismiss, expel’ 

*SANSKRIT: тагу ‘to wipe, clean, rub, polish’ (RV+) = EWAia II: 324 

9 See also *Hmars. 

«PIE *H>merg- ‘to pluck, wipe’ = LIV: 280 f. | Pok.: 722 f., 738 

*IE COGNATES: Gr. &pépyo ‘I pick, pluck’, Lat. mergae (pl. tant.) ‘reaping-board 
[used in pairs for stripping the ears of standing corn]’, merges (f.) ‘a sheaf of corn’ 
*REFERENCES: EVP: 48; КРЕП: 223; IFL П: 530a, 528a; Lambton 1938: 42b; Abaev, Slovar’ П: 100 Ё; 
EVS: 44a, 49b; WIM I: 71; WIM II/1: 79; WIM W/2: 711; WIM Ш: 112; Werba 1997: 363 f; 


Steblin-Kamenskij 1999: 239, 248, 458; Cabolov 2001: 638; Lecoq 2002: 121, 681b; Shahbakhsh: svv. 
gwamel-, mäl-, marz-; Korn 2005: 97, 317, 404 


*Hnaid ‘to insult, scorn’ 

*AVESTAN: Y Av. *n(ä)id- ‘to insult, scorn’ = Liste: 42 

Pres. athem.: IND. 15р. YAv. naismi (Y 12.1, V 22.21 ff., Vr 24.3), (aor. athem. ?) INJ. 3sg. YAv. näist 
(Yt 13.89), (aor. athem. ?) IMPV. 2pl. YAv. nista (V 18.16, V 18.24). 0 Y Av. nista shows lengthening of 
*-j- in closed syllable, cf. De Vaan 2003: 223.
```


## [2026-09-07T16:13:08.027Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '17780,17820p' CHEUNG.txt"
}
```


### [2026-09-07T16:13:08.080Z] TOOL RESULT

```
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
```


## [2026-09-07T16:13:29.744Z] TOOL CALL #23: Bash

```json
{
 "command": "ls site/pages/330.jpg 2>/dev/null; pdftoppm -f 330 -l 330 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg330 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/"
}
```


## [2026-09-07T16:13:30.911Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN 983 musten ===\"; grep -n -A14 \"983\\. mus\" HRN.txt | head -30; echo \"=== HRN 12 (p.12) amurziden ===\"; awk 'BEGIN{RS=\"\\f\"} NR==34' HRN.txt | head -50"
}
```


### [2026-09-07T16:13:31.897Z] TOOL RESULT

```
site/pages/330.jpg
total 2520
drwx------ 2 sfmqrb sfmqrb   4096 Sep  7 12:13 .
drwx------ 4 sfmqrb sfmqrb   4096 Sep  7 11:48 ..
-rw-rw-r-- 1 sfmqrb sfmqrb   8635 Sep  7 12:07 318-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb 101267 Sep  7 12:07 318-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    405 Sep  7 12:13 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  14937 Sep  7 11:56 arrows.png
-rw-rw-r-- 1 sfmqrb sfmqrb  85949 Sep  7 11:57 bqt2002_a.png
-rw-rw-r-- 1 sfmqrb sfmqrb  72256 Sep  7 11:58 bqt2002_f1.png
-rw-rw-r-- 1 sfmqrb sfmqrb 161214 Sep  7 11:57 bqt2002_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  83643 Sep  7 12:12 build.py
-rw-rw-r-- 1 sfmqrb sfmqrb   7075 Sep  7 12:13 c331_av1.png
-rw-rw-r-- 1 sfmqrb sfmqrb  10759 Sep  7 12:13 c331_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3537 Sep  7 11:53 c_migare2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   1829 Sep  7 11:53 c_migare3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   2261 Sep  7 11:53 c_migare4.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3958 Sep  7 11:53 c_migare.png
-rw-rw-r-- 1 sfmqrb sfmqrb  19652 Sep  7 11:53 c_semita2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   2639 Sep  7 11:53 c_semita.png
-rw-rw-r-- 1 sfmqrb sfmqrb  40259 Sep  7 11:50 ferdowsi2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  30950 Sep  7 11:51 ferdowsi3.png
-rw-rw-r-- 1 sfmqrb sfmqrb  28946 Sep  7 11:51 ferdowsi4.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4298 Sep  7 11:50 ferdowsi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   9383 Sep  7 11:55 masjid.wiki
-rw-rw-r-- 1 sfmqrb sfmqrb  33701 Sep  7 12:04 mk319a.py
-rw-rw-r-- 1 sfmqrb sfmqrb  46151 Sep  7 12:09 mk319b.py
-rw-rw-r-- 1 sfmqrb sfmqrb  51516 Sep  7 12:09 mk322.py
-rw-rw-r-- 1 sfmqrb sfmqrb  61981 Sep  7 12:06 mk323.py
-rw-rw-r-- 1 sfmqrb sfmqrb  37635 Sep  7 12:04 part_a.json
-rw-rw-r-- 1 sfmqrb sfmqrb  58545 Sep  7 12:09 part_b.json
-rw-rw-r-- 1 sfmqrb sfmqrb  97817 Sep  7 11:50 pg318hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  62558 Sep  7 11:50 pg318.png
-rw-rw-r-- 1 sfmqrb sfmqrb  67293 Sep  7 11:54 pg319.png
-rw-rw-r-- 1 sfmqrb sfmqrb 146848 Sep  7 12:01 pg320hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  80891 Sep  7 12:00 pg320.png
-rw-rw-r-- 1 sfmqrb sfmqrb  71522 Sep  7 12:00 pg321.png
-rw-rw-r-- 1 sfmqrb sfmqrb  72193 Sep  7 11:57 pg323.png
-rw-rw-r-- 1 sfmqrb sfmqrb  65279 Sep  7 11:49 pg324.png
-rw-rw-r-- 1 sfmqrb sfmqrb  55902 Sep  7 11:58 pg326.png
-rw-rw-r-- 1 sfmqrb sfmqrb 163982 Sep  7 11:53 pg327hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  73619 Sep  7 11:52 pg327.png
-rw-rw-r-- 1 sfmqrb sfmqrb  69765 Sep  7 12:12 pg329.png
-rw-rw-r-- 1 sfmqrb sfmqrb  72757 Sep  7 12:13 pg330.png
-rw-rw-r-- 1 sfmqrb sfmqrb 128240 Sep  7 12:13 pg331hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  94945 Sep  7 12:12 pg331.png
-rw-rw-r-- 1 sfmqrb sfmqrb     12 Sep  7 12:13 queue.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   1308 Sep  7 11:54 v2001.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  27253 Sep  7 12:02 z_maqd2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  63140 Sep  7 12:02 z_maqd3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4293 Sep  7 12:01 z_maqd.png
-rw-rw-r-- 1 sfmqrb sfmqrb   2895 Sep  7 12:01 z_meh.png
-rw-rw-r-- 1 sfmqrb sfmqrb  25378 Sep  7 12:01 z_mezna2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  33685 Sep  7 12:01 z_mezna.png
```


### [2026-09-07T16:13:33.567Z] TOOL RESULT

```
=== HRN 983 musten ===
=== HRN 12 (p.12) amurziden ===
12 -
49. äniurzlden Verzeihen', ämarzis^ amurzlst (Qiss. Dan.).
aw. ä+i/'marz', ämarezen; iphlw, ümurzUan, ämurz(i)sn,
ämurzltär Verzeihen' ; ai. ä -j- [/'marj- Vegwischen .
Vergl. wa/. namurzg, sar. namüzg 'Rechen, Besen.
Im Awesta und Altindischen wird die Bedeutung
gnädig sein, verzeihen' durch das Wurzeldeterminativ
d aus der [/^merg- ^abwischen' gewonnen, vergl. aw.
merezdätä, meresdika-, ai. m^ddti (Bartholomae BB. 13,
87, während Brugmann, Indog. Forsch. I, 171 auch
an ai. mfsyate Vergisst*, lit. mifsztl Vergessen denkt).
50. iimö^ten lehren, lernen*, Praes. ämöz-em, amözis,
phlv. ämö/tan lehren', ämöc-am, amöc(i)sn^ ämöölmtan ;
lit. mokinü „wohl auch faktisch 'lehren*, eigentlich zum
können bringen" (Kurschat), moJdnus (refl.) 'ich lerne'.
Die Zusammenstellung stammt von Spiegel (Tradit.
Lit., 360) ; sie ist indess lautgesetzlich unmöglich, da
lit. (d. i. ö) arischem ä entspricht. Skr. ä + [/"muC'
heisst nur ^bekleiden*.
51. ätney(ten 'mischen , Praes. ämez-em, ämezis^ ümeze, ämey,
vergl. enduh-amey (Vis und Rämin, Seite 83 Vers 16).
phlv. ame/tan, ämeßt (Bund.) mischen*; aw. vergl.
hememyäsaite *sie mischen sich zusammen', minas *du
vereinst' (Bartholomae, Ar. Forsch. III, 61 Anm.;
II 170); skr. a-\- l^miks- f mischen*), vergl. ^miisä-
'Quark', neben ai. migrä- Vermischt*; vergl. gr. ulyw^u^
/List^ai etc.^).
52. an jener*.
Die heutige Aussprache ün findet sich schon in der
bukhärischen Psalmenübersetzung (Et he, Litbl. f. or.
Phil. I, 191).
päz. a7i bez. hän (Aussprache für die Ideogramme
■^T und auch nöD), phlv. in an-gün, an-c.
Zu aw. a«-a, an-agäo, an-äis; skr. an-aycC, Der
Übergang von der aw. skr. Bedeutung 'dieser zu jener'
ist derselbe, wie in ksl. onü^ lit. ans, lat. ollus {*onlus) ;
^) Np. äme/ten hat mit np. meßten (No. 1006) nichts zu thun, wie
Fr. Müller, WZKM. 5, 351 will.
```


## [2026-09-07T16:13:47.544Z] TOOL CALL #25: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg330.png"
}
```


### [2026-09-07T16:13:47.933Z] TOOL RESULT

```

```


## [2026-09-07T16:13:47.926Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-07T16:14:22.657Z] TOOL CALL #26: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-07T16:14:22.664Z] TOOL RESULT

```


```


## [2026-09-07T16:14:24.130Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== Cheung Hmard ===\"; sed -n '17560,17640p' CHEUNG.txt"
}
```


### [2026-09-07T16:14:24.180Z] TOOL RESULT

```
=== Cheung Hmard ===
died’ (Hes.), Lat. morior, Arm. meranim, OCS mréti, Lith. mm ‘to die’, etc. 
*REFERENCES: KPF I: 84b, 146b f., 209b, 249b; Ivanow 1926: 421; IIFL I: 273a, 400b; KPF II: 223; 
Christensen, Contributions I: 75, 173, 263; IIFL II: 228a, 529; Christensen, Contributions II: 64, 118, 
162; Abrahamian 1936: 117; Lambton 1938: 77b; MacKenzie 1966: 102; Abaev, Slovar’ II: 75, 89, 70 f., 
86 f., 96; EVS: 45a, 58b; Lecoq 1974: 63; WIM I: 71; WIM II/1: 79 Е; WIM III: 112; Werba 1997: 218 
f.; Paul 1998: 305b; Steblin-Kamenskij 1999: 239; Cabolov 2001: 663; Lecoq 2002: 122, 125, 127 
(passim); NEVP: 51; Kiefer 2003: 200; Shahbakhsh: s.v. mir-, gimur-; Korn 2005: 314, 404 (passim) 


*maré (*mark) ‘to destroy, damage’ 
*AVESTAN: Ау. mərənc- (maraxs-) ‘to destroy’ || (+ *para-) ‘to damage, injure’ || (+ 
*ш-) ‘to ruin, spoil’ = Liste: 43f. 


266 *mard 


Pres. n-: IND. 3sg. med. Y Av. (them.!) marancaite (Yt 10.2, V 21.1, V 21.3), ҮАУ. para.merencaite (V 
13.3), YAv. moroyonte (Yt 8.44), 2р1. med. OAv. merengeduiie (Y 53.6), 3pl. YAv. merencinti (Yt 6.3, 
Ny 1.13), 3pl.med. OAv. vimoroncaite (Y 31.1), OPT. 2sg. med. ? YAv. *moroncisa (SrB 3), Zeg OAv. 
morasiiät (Y 45.1), 3sg. med. YAv. marancita (V 18.55), IMPV. 250. med. YAv. (them.!) (“)marancan‘ha 
(V 19.1, V 19.6); Aor. s-: SUBJ. 3sg. med. OAv. maroxsaite (Y 51.10); Partic.: pres. aja- ҮАУ. 
meroncaiias ° (V 7.58), pass. (+ priv.) YAv. amarsant- (Y 9.4, Yt 19.12), fut. YAv. amoroxSiiant- (Yt 
19.94), aor. med. Y Av. maroxsana- (Yt 19.41); Inf.: pres. OAv. morongoidiiai (Y 46.11); Desid.: SUBJ. 
3sg. med. mimaroxsäite (V 15.14), IMPV. 25р. med. YAv. mimaraxSar‘ha (V 15.14) 


*MIDDLE PERSIAN: BMP mwincyn- /murnjén-/ (caus.) ‘to destroy’, MMP mwrz(hy)- 
(sec. pass.) ‘to be harmed; to be persecuted’ || (+ *ui-) MMP wymrz- ‘to destroy’, 
ВМР gwmlc'k /gumarzag/ ‘the pernicious’ (Gershevitch 1977: 66) = DMMPP: 


234b, 354a 

Caus.: pres. IND. 1sg. BMP mwlncynym /murnjéném/, 3р1. ВМР mwincynynd /murnjénénd/; Pass.: pres. 
IND. 3sg. MMP mwrzyhyd, 3pl. MMP mwrzyhynd; Partic.: perf. pass. II MMP mwrzyd, mwrzydg, caus. 
BMP mwincynyt /murnjenid/ || (+ *ui-) Partic.: pres. MMP wymrz’g 


*KHOTANESE: OKh. *maljs- ‘to destroy, injure’, LKh. maich- (pass.) ‘to miscarry’, 
Khot. mulch-/mich- (sec. caus.) ‘to cause to miscarry’. 9 The etymology of LKh. 
maich- etc. is deduced by Maggi, SVK III: 127, on the basis of ОК. mulchafiate 
(KV 1.5) which clearly derives from the stem *mré-a- On OKh. malstä see 
Sims-Williams, SVK III: 122 f. = SGS: — 

*SOGDIAN: MSogd. mrync ‘to destroy’ 

*CHORESMIAN: ? mwrnyk (ppp.) ‘slaughtered’ (302.1) = Samadi: 112 

*NWIR: NP marg ‘death’ 

*NEIR: Oss. marg ‘poison’ 

*MISC: Par. mat (supplet. of mör-, *mar') ‘killed’, Orm. mak (ppp.) ‘withered, faded’ 
*SANSKRIT: marc ‘to damage, hurt, injure’ (RV+) = EWAia II: 323 

«PIE *melk*- ‘to damage’ = LIV: 434 f. | Pok.: 737 


*IE COGNATES: Gr. BAG 0 “I hurt, damage’ 
*REFERENCES: JIFL I: 273a, 400a; GMS: §153, 600; Abaev, Slovar’ II: 72 f.; Werba 1997: 219 


*mard ‘to despise, disparage (?); to neglect, abandon (?)’ 

*AVESTAN: OAv. marəd ‘to despise, disparage’ {hapax} = Liste: 44 

Aor. athem.: SUBJ. 3sg. OAv. maredaiti (Y 51.13) 

*CHORESMIAN: (+ *pari-) prmrcy- ‘to blame’ = Samadi: 153 f. 

*SANSKRIT: (*)mardh ‘to despise, disdain’ > EWAia П: 328, s.v. mardh 

o Rejecting the interpretation of Bartholomae, AIW: 1150 (‘to ruin’, *Hmard), 
Humbach, Kellens, Narten (et al.) assign the meaning ‘to neglect, abandon’ to the 
Avestan verb marad-’, on the basis of the Skt. cognate root mardh ‘to neglect, 
abandon’ (accepted by Mayrhofer, EWAia: Lei This interpretation appears rather 
bland and stylistically weak to me, especially as the Av. form is embedded in a quite 
pronounced context. Insler, Gathas: 107, 317 translates marodaiti as ‘misses’, on
```


## [2026-09-07T16:14:29.417Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^\\*Hmard\\|\\*Hmard ‘\" CHEUNG.txt | head; echo ---; grep -n \"Hmard\" CHEUNG.txt | head -20"
}
```


### [2026-09-07T16:14:29.475Z] TOOL RESULT

```
12241:*Hmard 179 
12295:*Hmard ‘to crush’ 
12427:not from *ui-mard- (*Hmard ‘to crush’), as suggested by Shahbakhsh. Although it is 
---
12241:*Hmard 179 
12295:*Hmard ‘to crush’ 
12427:not from *ui-mard- (*Hmard ‘to crush’), as suggested by Shahbakhsh. Although it is 
17633:o Rejecting the interpretation of Bartholomae, AIW: 1150 (‘to ruin’, *Hmard), 
17654:connected to the ‘crush’ root *Hmard by MacKenzie I: 547 f. ("spoil, destroy"). 
56177:*darš , *Hmard, *ka(H)ud,
```


## [2026-09-07T16:14:31.876Z] TOOL CALL #29: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%D8%A7%D9%84%DB%8C%D8%AF%D9%86",
 "prompt": "Give the full etymology section for Persian مالیدن (mālidan) 'to rub', including Middle Persian and Proto-Iranian reconstructions and any cited sources (Cheung, Hasandust, MacKenzie)."
}
```


### [2026-09-07T16:14:38.576Z] TOOL RESULT

```
# Etymology of Persian مالیدن (mālidan)

Based on the Wiktionary entry, here's the etymology:

Persian مالیدن derives from **Middle Persian** mālīdan (mʾlytn'), which comes from **Proto-Iranian** *Hmarz- meaning "to wipe; to rub." This traces back to **Proto-Indo-Iranian** and ultimately to **Proto-Indo-European** *h₃merǵ- ("to wipe").

The entry cites **Cheung (2007)** in his *Etymological Dictionary of the Iranian Verb*, referencing the reconstruction *Hmarz. Cognates include Sanskrit मृज् (mṛj, "to wipe, to rub") and Ancient Greek ὀμόργνῡμῐ (omórgnūmĭ, "to rub").

The page notes that Middle Persian script documentation is needed and that Proto-Indo-Iranian terminology requires further specification. No citations to Hasandust or MacKenzie appear in this entry.
```


## [2026-09-07T16:14:42.714Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '12295,12340p' CHEUNG.txt"
}
```


### [2026-09-07T16:14:42.759Z] TOOL RESULT

```
*Hmard ‘to crush’ 

*AVESTAN: OAv. morand- ‘to crush’ = Liste: 44 

Pres. n-: INJ. 3sg. OAv. mörondat (Y 32.9 f.), 3р1. OAv. morəndən (Y 32.11 f.) 

*OLD PERSIAN: (+ *ui-) vimard- ‘to crush’ = Kent: 203a 

Pres. them.: IND. 3sg. vimardatiy <vi-i-m-r-d-t-i-y> (DSe 40 f£), impf. 3sg. viyamarda <vi-i-y-m-r-d> 
(DB 5.11). 9 Different transcription in Brandenstein — Mayrhofer 1964: 132, viz. vi-mradatiy and 
viy-amrada respectively. 


180 *Hmars 


*MIDDLE PERSIAN: Q The interpretation of BMP ’mwst ‘crushed’ /amust/, made by 
Nyberg 1974: 16a is no longer accepted: /hamwast/ ‘collected, gathered’: 
*ham-uaz-. 

*SANSKRIT: mrditä- ‘crushed’ (A V+), ni-mfdya- ‘pressed down’ (SB). © This root ‘to 
weaken, soften’ has converged with the ‘crush’ root mard. > EWAia II: 386 f., s.v. 
mrad 

«PIE *H5merd- ‘to hurt, injure (someone) = LIV: 280 | Pok.: 736 f. 

*IE COGNATES: Gr. ёрёрёо ‘I rob, deprive’, Lat. mordeö ‘I bite, chew’, ? OE 


smeortan ‘to inflict pain, smart’, Engl. to smart, etc. (with mobile s- ?) 
*REFERENCES: IIFL I: 273b, 401a; Werba 1997: 366 


*Hmars ‘to wipe, rub; touch’ 

*KHOTANESE: (+ *ui-) ? ggumäls- (gümaly-) ‘to besmear’ = SGS: 29 

*SOGDIAN: (+ *pati-) CSogd. pcmrws- ‘to feel, touch’ 

Pres.: IMPV. 2sg. CSogd. pemrws; MSogd. "pemrwsyy (ВВВ: 38) 

*CHORESMIAN: (+ *pari-) prmsy- ‘to rub (the ear)’ || (+ *fra-) šmšy- ‘to rub off’ 
= Samadi: 154, 196 

*NWIR: ? Bal. mus-/musta ‘to smear, rub’ (< WIr. ?, cf. Pth./MP mwst, *Hmarz) || (+ 
*pari-) NP parmäsidan ‘to touch, feel’ || (+ *ui-) Kurd. (Kurm.) guvastin/guves-,
```


## [2026-09-07T16:15:00.942Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && for n in 30 31 32; do echo \"#### v4 pdf $n\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' BQT_v4_pages.txt | head -40; done"
}
```


### [2026-09-07T16:15:03.116Z] TOOL RESULT

```
#### v4 pdf 30
[pdf page 30]
۱۹۵۷ مالخولا
کلوبندء را (۱) گوبند و آن غلامی باشد که | مالش ومالندگی‌هم هت ‎٩‏ -
رتیه بزرگی رسیده باشد چه کلو (۲) بمعنی مالی - بر وزن خالی . بممتی بیار
بز رکه است - و شکم پرست و جوعیرا نیز | و فراوان باشد ۷ - و بلغت بودانی انکیین دا
کفته‌اند . کویند که عبل باعد ۸ - ودرملك دکن باغبانت
هالّه ۱ - بروزن‌خاله. تخته‌ای راکوبند | را مالی میگویند .
که برزیگران بر زمین (۳) شیارکرده بکشند مالیا < بروزن بالیا . «رختی‌است بلريك
ا کلوخهای آنرا نرم کند و زمین را همواد | و درا زکه از چوب آن درخت نیزه و تیور سلزند
سازد ۴ - و افزاری که کلکاران بدان کاهگل | - و بلفت بوتانی بممنی میاء باشد. که در برایر
وکج (4) وآحك ۳ سفید ات ‎٩‏ +
بردیوار مالند۴ مه مالیخ *۱- بائاك بتحتا ی کشیده ویتای
و افزاری که ماله نقطه دار زده ۰ بممتی مالیخولیاست که کوقت
جولاهگان از خی بمانند جاروب و لیف‌سازین | و اخلل دماغی و سودا و خیال خام پلشد -
ربا آن تانه را آهار دهند ۴ - و بمعتی‌مالامال مالیخو لیا ۱۱- بممنی مالیخ اس ت که
هم آمده اس ت که پر و لبربز باشد 8 - وبممنی | کوفت و خلل دمانغی وسودا و خیال خلم باشد -
(۱) چك : کلوبنده را . (۷) چك :کلو . (۳) چش : بزمین .
(4) چش : کچ .
از : مال ( مالیدن )۸ ( پسوند اسم آلت ) » معرب آن «مالق» « تقی > -
۴ - بر زگر دفت و نان و دوغ ببرد ماله و جفت و دای وبوغ ببرد .
سنائی غزتوی « رشیدی >
۴ <معرب « مألج » « المنجد > . ۴ - ... دیشی دارد چوماله آلوده بهیت -
عمارة مروزی « لفت فری چاپ هرن ص ۸۰ > و رك : فرهنگه نظام ‏
8 - سیکیی ده بخانه وام شدست پنج ازآن خوله پنج ازآن ماله .
سوزلی سمرقندی « رشیدی * -
‎٩‏ - از : مال (مالیدن) ۸۰7 (پسوند اس مصدر). ۷ -اين بیت را شاهدآوردماند :
هر که سرمايةٌ.ماهی زتو دارد حاصل آفتابش ز دل ستکه برآید مالی-
سیف اسفرنگه « رشیدی > -
مولف فرهنگه نظا کوید : « شاید در شمر مذ کور « حالی > تصحیف خوانی شده .> ور4: ماله.
مالامال ۰ ۸ - بونانی 5261 ( عل ) « آشتینگای > .۰
‎٩‏ - یونانی 336185 ( سیاء ) « اختینگای ». ۰ رد : مالیخولیا +
۱- مسحف مالنخولیا » لانینی 3361810112 از بودانی 126188870112 « حزی
چ ۷ س ۵۹۵ ۶ اشتینگای : مالنخولیا >۰ مر کب از 33618008 ( سیاء ) و 1018 (خلط
صفرا) جمماً بدمنی خلط سیاء , چون مرش مذ کور سوداوی است لپذا باین اسم‌خوادماند , وآن
نوعی از جنونست که در فکر فاد بهم وسد ولی صاحب آن بکسی ایذا نرساند « غیاث > . این
لفت بسور ماخولبا » ملنخولیا , مالیخ » مالنخ و غیره در آمده است .

#### v4 pdf 31
[pdf page 31]
مالیطرنا م۱۹۶۸
کوبند بوتانی ات .38 خوانند, وصعترا کرچه باسین بی‌نقطه است لیکن
مالیطر فا ۱ « بفتح طای حطی‌وسکون | درکتب طبی بصاد نوشته‌اند تا بشمین مشتبه‌نشود.
رای قرشت و لون بالف کشیده . و پلفت بونانی | خوردن‌آن درطمام ضمف‌چشم را نافع باشد وقوت
زاج سیاه باشد و آن را زاج کفشگران اس باصره را نگاه دارد -
میگوشد؛ وبحذف مانی‌هم آمده است که ملیطرنا مامهستان « بفتح ثالك ‏ و کسرهایروزن
باشد. + ناوکستان . دوائی است که آنرا ساذج هندی
ها » بروزن لام » مادرراگوبند وبمرپی | کوبند و آن برکی است مانند بر که کردکان
والده و ام خوانند ۲ .28 و در روی آب پیدا میشود . بخورآن بجه را از
مامك * بروزن ناوك . مصفر هام است نگ بزیرآورد(؟) -
که مادر باشد پستی ماد رک - و مادر را هم مامیشا ؟ - با ناك بتتای‌رسید. دای
میگوبند ۴۳ .#* متلئه بالف کشیده , بلفت سربانی نام رستنیی‌باشد
مامون « بروزن (۱) هامون . نوعی‌از بفایت بیمزه ودرآب بهم میرسد ودر قاضات بکار
پودنه کوهی باشد و آلرا بس‌بی صعتر الجمام | برند و عصارة آنرا شیاف مامینا خوانند .
() چك : بوزن . () چش : آرد . ۹
۱ - بونانی 33612818712 ‎٩‏ اشتینگای > . ؟ -قی : ماما ۰ مامی » لیتوانی
8 30۵ (مادر) . املاوی کلیسیابی 38778 ( ماما ) » آلبانی 136116 » وخی
.۰ سربکلی 33282 (مادر بز رکه) . افغانی 12181 (عمه » خاله) ۰ بونانی114772302 ۰
6 ( ماما » مادربز رکه ) . لاتینی 33870382 » 17121212118 ( ماما + مادربز رکه ) ۰
آلمانی عالی قدیم 30002 . 3301 ( عمه . خاله ) «اسشق ۹۹۳ > ۰ پازند 133878(مادر)
* باروچا ۰۳۱۱
شاد الا بدر مر که نه‌یینی مردم بکر جز در رحم مام نیابی دختر.
انوری ابیوردی درقصیدء راجع بحملهٌ غزان . « فرهنگه نظام » -
۴ - از : هام (هم.) + که ( پوند تحبیب و تصفیر ) .
۴ - ممیتا « دزی ج ۲ اس چ۹۱ ۰ 80818106۳ (ف) ۸« دزی جس ۲:۵0
0 مالیدن - بفتح دال » اوستا - 33872 » 1287628111 ( جاروب شده ) » پهلوی
2 ] ۸۵۵ ۰ 2۳2 ] فقاطعهل .۰ متفه ] هط۵5ل , ۵ط22720(9 ( جماع ) ۰
(جناع کردن). 2211088 ۰ 332[)1(808 ؛ هندی باستان- 2:۲2 , [ع12279180
( پاك کردن ) »کردی 2 3.3110 ( جارو ب کردن ) بلوچی 2 و2212 . 22160285
( ساییدن ‏ مالیدن , مخلوط کردن ) » استی 323۳218 ( جاروب کردن ) « اسشق ۹۹۲ 4
دست کشیدن روی چیزی ۰ چبزی را دردست مکرر فغار دادن » دوچیز را بهم فشاردادن » مشت
ومال دادن » چیزی را ( مانند رنگه , روغن ) روی جم ی کشیدن .
2 ماما.- رك : مام ؛ در تهرانی 3387528 (قابله . مام‌ناف) » در افغانی 112132 (دائی,
خال ) در فارسی آدیی بمعتی مادر است :
هت مامات اسب و باپا خر تو مشواتر چو خوانمت استن . سنائی غزنوی .
و رل :کنجینة کنجوی ص ۱۳۹ ۰
۵ مام لاف - قابله « رشیدی > و مخقف آن ماناف (ه.م.)

#### v4 pdf 32
[pdf page 32]
-۱۹4۹- مانا
مامیرآن ۱ - با رای بی نقطه پروزن ِ که عربان بیت خوانند ۴ - واسباب وضروریات
غازبخان » نوعی از عروق‌السفر است وآن دوائی | خانه را نیز کوبند - و بمعنی ما باش د که متکلم
باشد زرد رنکه بسپزی مابل » باريك و کره‌رار | مح‌الغیر است ۴ - و بمعتی مارا هم هست که در
میشود . گرم و خغك است در چهارم . برقانرا مقابل شما را باشد ۴ - و امربرگذاشتن ومالدن
نافع است و آنرا بعربی بقلةالخطاطیف و شجرة | هم هست بعنی بگذار و باش و بمان ۴ - و شبه
الخطاطیف خوانند . کوبند چون +جچةٌ پرستوك در و مثل و مانند را نیز کوبند 9 - و بممنی باقی
آشیان نابینا شود مادر وی غاخی از مامبران | و ابد و جاویدان هم کفته اند - و بلفت هندی
آورده درآشیانه نهد چشم بچه‌اش بینا کردد . | بمعنی حرمت وعزت وقبول ومقبول باشد -
۱ ید هافا٩‏ - بر وزن دانا . بزبان زند
۱ ۳ میرمیران « دزی ج؟ ص۹۲۸ * مرمیران « دزی ج ۲ ص۵۸۵ ۰۹ لغت فارمی
است . فرهنگه نوبسان‌آنرا با 3611608108 (خالیدولیون [ه.م.] ) بونانیان مترادف داسته‌اند
و اسم عربی « بقلة الخطاطیف > ترجمهٌ این کلم بودانی - بعنی « گیاه پرستوها » - است -
«ناه) - 11602۵1۵ کنته‌اند که محتملا 61140186-) (فر) راکه دارای عصاره وريشهٌ زرد
رنگه است » با داروی شرقی دیگر ی که آنم دارای ریشه های زرد رنگه است بعنی عنام۲۰
8 خلط کرده‌اند . اصل گیاه اخیر از چین است وریشه های آنرا بابران وهند میبردند ودر
مغزن‌الادویه شرح آن‌آمده . مایرهوف همین قول را معتبرمیداند « عقار ۷۸۱ اف >. ور4: دزی
چص ۵۹۵ ۴ - پپلوی 28 ( خانه » مکن ) « یب رکه ص۱۶۶ * » پارسی باستان
- 328812 ( خانه » سرای ) » در پهلوی بجای - 373288 اوستایی‌کامهٌ 7320 ( خانه ) را
بکار برده اند , 28)1(9878 ۰ 28)1(501 ( منزل ) , 340028 ۰3200:9120
منز لکردن ) »و « ماندن » فارسی نیز ازهمین ربقه است . «اسشق ۹۹4*.
۴ - ضمیراول شخص‌جمع مفعولی: دادمان » گفتمان ؛ وضمیر اضافی (ملکی): کتابمان ۰
کلاهمان . درپهلوی 3328 « نیب رکه ص ۱4۵ . ۴ -ر4 : ماندن .
8 - مان صورت پسوند بمعانی‌ذیل بکاررود: الف) - مان ۳ - من ۰ ازاوستابی 1387225
بهئوی 3281128 ( اندبشیدن ) : شادمان » پشیمان: » پژمان » نربمان , رادمان » قهرمان .
دشمن « فاب ‎٩‏ ص ۰۷۳ ب )مان ( از ريشة 46۳888 (کانتها ) و 8673288 ( دیگر
بخشهای اوستا ۰ پپلوی 1328 بمعمتی خانه ) : کشتمان . دودمان » کرزمان ۶ فاب ۱ ص۷۳ح >
ج ) پسوند سازندة اسم معتی از ربشهٌ قعل : سازمان » زایمان . د): پوند سازندة آسم ذات از
مصدر مرخم : ساختمان . علاوه بر اینها پسوند مان ( از مصدر مانستن ) را ذ کر کرده اند و
« شیرمان > و «آسمان مان » ( رك : فرهنکه نظام ) را شاهدآورده‌اند » ولی استعمال آین‌کلمات
محتاج بأیید شواهد است . - پهلوی ۳32881 (مانند » نظیر ) * ناوادیا ۰۴۱۹۲
در فارسی تصورت ادات تشبیه وشغك و تردید و بممنی گوبی » پنداری ومانند آید :
آنکی که مرا یکشت باز آمد پیش ماناکه دلش بسوخت برکشتهٌ خویش .
« گلتان ۰۱۳۰
```


## [2026-09-07T16:15:18.463Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && for n in 92 93 94; do echo \"#### v4 pdf $n\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' BQT_v4_pages.txt | grep -n \"مرز\\|۲۰۱۰\\|۲۰۰۹\\|۲۰۱۱\" | head -20; done"
}
```


### [2026-09-07T16:15:19.932Z] TOOL RESULT

```
#### v4 pdf 92
#### v4 pdf 93
#### v4 pdf 94
```


## [2026-09-07T16:15:23.350Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && grep -n \"مُرز\\|مرزیدن\" BQT_v4_pages.txt | head -20; echo \"=== pdf tag near ===\"; grep -n \"pdf page\" BQT_v4_pages.txt | sed -n '88,100p'"
}
```


### [2026-09-07T16:15:23.421Z] TOOL RESULT

```
2728:۴ - ره واسم فاعل مرخم از مرزیدن ( مباغرت و مجاممت ) . ور4 « مالیدن » .
=== pdf tag near ===
3438:[pdf page 88]
3492:[pdf page 89]
3525:[pdf page 90]
3569:[pdf page 91]
3616:[pdf page 92]
3658:[pdf page 93]
3693:[pdf page 94]
3731:[pdf page 95]
3769:[pdf page 96]
3814:[pdf page 97]
3876:[pdf page 98]
3915:[pdf page 99]
3960:[pdf page 100]
```


## [2026-09-07T16:15:28.226Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && awk 'NR<=2728 && /\\[pdf page/ {p=$0} END{}' BQT_v4_pages.txt; grep -n \"\\[pdf page\" BQT_v4_pages.txt | awk -F: '$1<2728' | tail -3; echo ===; sed -n '2700,2740p' BQT_v4_pages.txt"
}
```


### [2026-09-07T16:15:29.841Z] TOOL RESULT

```
Exit code 1
2632:[pdf page 68]
2669:[pdf page 69]
2704:[pdf page 70]
(eval):1: == not found
```


## [2026-09-07T16:15:32.648Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && sed -n '2704,2735p' BQT_v4_pages.txt"
}
```


### [2026-09-07T16:15:32.691Z] TOOL RESULT

```
[pdf page 70]
۱۹۸۷ مرزغن
گفته‌اند که مربع سازند و کنارهای آترا بلند | اول هم گفته‌اند ‏
کنند ودرمیاش چیزها بکارند۱ - ویمعتی‌سرحد مر بان * - با زای شله دار بر وزن
هم آمده است ۴ چه مرزبان صاحب و حاکم دشت بان » حاکم و میرن سرحد و صاحب طرف
و نگهدارندء سرحد باشد - و بنمنی آپادان هم و مالك زمین و زمیندار باشد - و نگهدارنده
هست - و بوزه را نیز کوبند » وآن شرایی‌است | ونگاهبانرا نیز کوبند ؛ و بروزن پپلوان هم‌بنظر
که از کندم و کاورس و جو میازند - و مقعد آمده است که بفتح ثالك باشد - و عربان مهت
وشتگاه و مخرج سغلی را نیز کفته‌اند ۴ که :| وبزرکه‌آتش پرستابرامیگویند وجمعآن مرازبه
سوراخ کون باشد از ادان و حیوالات دیگر - | است .
و بمعنی مباغرت و مجاممت هم هست ۴ - ودر مرژغاتن *۱- باغین هطه دار بروزن
عربی چیزیزا بچنگال گرفتن بآهستگی «جیزیر! | پهلوان » دوزخ را کوبند که در مقابل بهشت
بریدن و خراشیدن باشد* - و جنم اول » بمعنی | است - و بمعنی آتشدان و منقل آتش هم‌آمده
مخرج سقلی هم آمده است ‎٩‏ - و موش رالیز | است - وکورستان وقبرستانر| نیز کفته‌اند.
کویند که عربان فاره خوانند ۷ -, مرزغن ۱۱ باغین قطه دار بر وزن
مرف ۸ - بفتح ال وسکون تال وزای | کرکدن . بممنی مرزغان است که دوزخ ۱۳
فارسی ۰ نام یکی ازآتش پرستان است . وبکسر | وکورستان - وآتغدان باشد ۱۴.
۱- در ارا3 ( سلشان آباد ) کناره‌های بلند اطراف زمیتهای زراعتی را کوبند
« مکی نژاد» :ا
تیفهای کوه ازو پرلاله و پرسوسن است مرزهای باغ ازو پرسنبل وسیسنیی است .
* فرخی سیستالی ص 8۳۰ ۰
۲ - بسنده کند زین‌جهان مرز خوش بداند مگر مایه و ارز خوش .
فردوسی طوسی « لغت فری ۱۸۲ ۰
۴ - باین «عنی بشم اول هم آمده است که بعد درامتن ذکر شده .
۴ - ره واسم فاعل مرخم از مرزیدن ( مباغرت و مجاممت ) . ور4 « مالیدن » .
8 - (عر ) « مرز » شکنجیدن بالگشتان نرم لرم بی‌کزند ... و عیب 40 کردن - و
زشت کردالیدن - و بدست زدن - و پاره‌ای بر کندن: از خمیر و جزآن .> « منتهی‌الارب >.
‎٩‏ - بر در مرز چو انباش بهنگام جماع تیز چون زمزمةٌ ای بانبان آرند .
رك : مرزوان . سوزئی سمرقندی « رشیدی * .
۷ - این معنی راظ . از « عرزنگوش » (.م.) ۳ « مرزه کوش » استخراج کرده اند
«مرزهموش راکویند ولپذا گیاهی که بگوش موش شبیه است مرزنگوش کوبند . » « جهانگیری»
رشید ی گوید: « بمعنی موش » مرزه است نه مرز» وظ . صحیح باین معنی «کرزه» (ه.م.) است.
```


## [2026-09-07T16:15:40.055Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && awk 'BEGIN{RS=\"\\f\"} NR==93' BQT_v4_pages.txt | head -45"
}
```


### [2026-09-07T16:15:41.512Z] TOOL RESULT

```
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
```


## [2026-09-07T16:15:50.384Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && grep -n \"فرامرز\" BQT_v3_pages.txt | head; echo \"=== pdf tags ===\"; grep -n \"\\[pdf page 2[3-4][0-9]\\]\" BQT_v3_pages.txt | head -20"
}
```


### [2026-09-07T16:15:50.443Z] TOOL RESULT

```
32307:فرامرز ؛ بمعتی دهقان وبرزیگر و زراعت کننده
=== pdf tags ===
16565:[pdf page 230]
16623:[pdf page 231]
16707:[pdf page 232]
16794:[pdf page 233]
16843:[pdf page 234]
16921:[pdf page 235]
17004:[pdf page 236]
17080:[pdf page 237]
17167:[pdf page 238]
17242:[pdf page 239]
17323:[pdf page 240]
17415:[pdf page 241]
17493:[pdf page 242]
17581:[pdf page 243]
17660:[pdf page 244]
17759:[pdf page 245]
17828:[pdf page 246]
17925:[pdf page 247]
17993:[pdf page 248]
18052:[pdf page 249]
```


## [2026-09-07T16:15:58.642Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && awk 'BEGIN{RS=\"\\f\"} NR==240' BQT_v3_pages.txt | head -6; echo \"...\"; sed -n '32290,32320p' BQT_v3_pages.txt; echo \"=== which pdf page ===\"; grep -n \"\\[pdf page\" BQT_v3_pages.txt | awk -F: '$1<32307' | tail -2"
}
```


### [2026-09-07T16:16:00.251Z] TOOL RESULT

```
[pdf page 240]
~\tty—

فراسیون ۱ = بفتح اول وکس رابع
بر ‎oir‏ حواربون .گندنای کوهی باشد و ‎WT‏
‏بتازی ‎Minto‏ وصوف‌الارش و سندبان‌الارش
...

‏*۶- مرد باید که در کشا کش دهر سنگه رین ‎LT‏ باشد .

‏سعدی شیرازی « امثال و حکم دهشدا ‎NOVY Ey‏

‎Glas ۰-۱‏ بود که ‎thy‏ تبر استاده کنند ‏ وآنرا گنبدی ییزخوانند.»«جهانگیری»

‏و درین زمان « فلندری » و « ‎Ob SOUT‏ » نامند « فرهنگگ ‎lls‏ .
[pdf page 441]
کعلورز

ولات است ۱ - و بمعنی کشنده باشد که فاعل
کئیدن است ۴ - و جمع کش هم‌هست؟ همچو
درد ی ‎wo, US‏ غراب‌خواران 2 ‎oo lS,‏
محویان و ممشوقان .

کشاورز ۴ ‎co‏ اول و واو بروزن
فرامرز ؛ بمعتی دهقان وبرزیگر و زراعت کننده
باشد - و زمین زراعت و کشت‌زار ‎sil‏ گویند.

کشتاد * ‎ost.‏ قرشت بر وزن
‎sate‏ چانور بسمل کرده را گویند که بعربی
مذیوح خوانند .

کشتاو - بفتح اول و سکون ابی
وفوفانی بالف کشیده و بواو زده , بمعنی‌رفت‌است
که آن مفموم بغم مردم بودن‌وبقدر حال درخیر

AMAT

وصلاح آن کوشیدن باشد .
=== which pdf page ===
32225:[pdf page 440]
32298:[pdf page 441]
```


## [2026-09-07T16:16:07.662Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && awk 'BEGIN{RS=\"\\f\"} NR==239' BQT_v3_pages.txt | head -60"
}
```


### [2026-09-07T16:16:09.136Z] TOOL RESULT

```
[pdf page 239]
فراز
فلاطرن , کسیرا و چیزیر! کویند که نه بطریق
‎He THe‏ پس رود. یمنی روز به نباشد وروزبروز
پي رود .

‎ILS‏ ۷ - بروزن نماز . چندممنی‌دارد:
۱- پهن شده و پخش کردیده باشد . ۲ - بسته
و کشاده و ‎He‏ کرده شده - و باز کردن و کشودن
وپوشیدن درباشد ۴ « وباین‌معنی ازاضداد است.
۳ قریب ‎Cho gy‏ وپیش وحضور باشد. 4-جمع
وقراهم‌آمده راکوبند . ه - بمعنی ‎am‏ از یين
و ازین باز باشد . ‎٩‏ - پمعنی عقب و پس باشد
چنانکه کوبند « فراز ده»بعنی پس‌بده. ۷-بمعنی
پاز باشد که از تکرار است چنانکه کوبند «فراز
ده * ‎te‏ باز بده ومکرر بده. ۸ بممنی زمان
باشد چنانکه کوبند « ازسباح فراز» بعنی‌ازسباح
بلز و ازدیروز فراز - بضی ازدیروز باز-انتظار
میکشم ». ‎٩‏ بمملی فروز باشد کداز افروختن
است . *۱- بالا وشیب وزیر وزیر را گویند۴ ؛

‏و باين ممتی هم از اضداد است ۰ ۱۱- بمعتی
بلند وبلندی آمده‌است ؛ و باینمعنی بروزن‌حجاز
هم گفته‌اند - وامر بدین معتی‌هم‌هست بمنی‌بلند

‏ووع اس
شو و بالابرو ؛ واسم فاعل نیز آمده است که‌بلند
شونده وبالارونده باشد . ۱۲- س رکش‌راگویند
عم از مردم نافرمان واسب س رکش. ۳-بمعنی
آلت تناسل ‎gas -۱6 ۰ ath‏ وصل باشد چه
فرازیدن وصل کردترا نز کوبند ‎Ne.‏ زیاده
۹- بمعنی در آمین و فرأرفتن
باشد . ۱۷-در نخه ‎sy‏ بمعنی خون نوشته

‏وزایده باشد .

‏بودند که عربان دم خوانند .

‏فرازمان ۴ = بامیم‌بالف کشیدموینون
زده ؛ حکم وفرمانرا گویند.

‏ق استه }5 ؟ ‏ - ۲

‏فر ‎Bgl‏ = بفتح او و سکون
مين بی نقطه + بمعنی پرستولك است که خطاف

‏قراسو۵ه * = بروزن ناسوده. ‎wins‏
‏بسبار کهنه شده وازهم رفته باشد.

‏قر اسیاب »= بنتح اول .مخفف افراسیاب
است که ‎teal‏ تر کستان بوده ‎٩‏ - وبمعنی‌حباب
هم‌آمده است وآن شیشه مانندی باشد که‌ببب
پاریدن باران بر روی آب بهم میرسد ۷

‏۱ - پهلوی ‎frie‏ ( بهپیش , جلو . باینجا ) از اوستا - ‎frank‏ « بارنولمه۱*۲۵*.
پلزند 16820 ۰ ‎fraz‏ « نب رکه ص۷۰ ۰ . هندی باستان - ۳۳406 ( سانسکریت - ‎prac‏ 4
‎Ge)‏ جلو) . استی ۲42 ( از پیش ) « استق ‎ANN‏ ؟ - ‎ote gee‏ وبا :

‏کس نبیند فرو شده بنشیب
‎ap‏ و کینش مثل دو دربانند
```


## [2026-09-07T16:16:22.293Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && grep -n \"رامرز\\|فرامر\" BQT_v3_pages.txt | head; echo \"=== v1 amorzidan ===\"; cd ../.. && grep -n \"آمرزیدن\\|آمرزش\\|آمرز\" BQT_v1_pages.txt | head -10"
}
```


### [2026-09-07T16:16:23.767Z] TOOL RESULT

```
32307:فرامرز ؛ بمعتی دهقان وبرزیگر و زراعت کننده
=== v1 amorzidan ===
5494:«دانش» و «خواهش» و «آمرزش»: بعنی دانستن و خواستن و آمرزیدن(")
5707:همحو «خردهند » و « دانشمند » ؛ و دیگر یکار همجو « آمرز کار »۲
8763:> آمرزش - پهلوی 21001721508 < مناس۲۹۵ : ۲ ۲ » بخشیدن خدایتعالی کناه را
8764:بربنده پس‌از م رکه , مغفرت » نفران « لهت نامه » رك : آمرزیدن .
```


## [2026-09-07T16:16:30.152Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '8755,8790p' BQT_v1_pages.txt; echo \"=== pdf page ===\"; grep -n \"\\[pdf page\" BQT_v1_pages.txt | awk -F: '$1<8770' | tail -2"
}
```


### [2026-09-07T16:16:32.597Z] TOOL RESULT

```
باستان 2102۲02 *: بسارمضر و زبان‌آور) . اسکندر آنان را گوشمالی داد ونحت اطاعت خویش
در آورد وفرهاد اول اشکانی ابشان‌را به چرکس قرب دربند خز رکوچاند , وبجای آنان» قبیلةٌ غیر
ایرانی دیگر بنام 1۳010704 از ناحبهٌ طابران طوس ( تردبك مشهد. کنونی ) مهاجرت کردند
* مار کوارت شهرستانها ۱۱۰ > آماردان مردمی فقبر ولی جنکی بودلذ . استرابو نلم این فوم را
بقبه در حفحهٌ ٩۱‏
۵ آهدن - بهلوی 28۵ 20۵ «منای ۲:۲۹ *. «بونکر۵۹؟. طبر ی 9617108 ین
« واژه نامه ۱۳۴ », کلکی 2110100 ؛ بمعنی اتبان , اباب » قدوم » مقابل رفتن وشدن :
بدین‌جای ازبهر او آعدم بکینه همی جنگجو آعدم . فردوسی «لفت‌نامه».
> آمرزش - پهلوی 21001721508 < مناس۲۹۵ : ۲ ۲ » بخشیدن خدایتعالی کناه را
بربنده پس‌از م رکه , مغفرت » نفران « لهت نامه » رك : آمرزیدن .
۵ آهرزیدن - بخیدن خدا ی کناه بنده را پی‌از مر که . غفران :
نظیر خوش بنگذاشتند وبگذشتند خدای عزوجل جمله را بیامرزاد « حافظ5۹۳٩‏ >
لآمله ۲ - ینم ثاكك و قح رابغ » دوائی
است کثیرالتفع وممرب آن «آملج» باشد . گویند
دو درم را از آن کوفه تا دوساعت درآب شیرین
بجوشانند و بمد ازآن ساف کنند و سه‌چپارلویت
درچشم چکانند ۰ سفید یرآ که ۳ بود سود
دارد .
]هن - پنتح الك و نون ۰ نود خومن
هیزم شکافنه(۱) را گوبند سوپشته ویشتوار؛ هیزم
ببتهرا ن رگفته‌اند - و بکسرالث یام مادرحصرت
رمالت یناه علیه السلام است .
آمو . نم تالث و سکون واو , مضفف
آمون‌است وآن رودخانه‌ای باشدمشهور وممروف.
واقم در میان ابران وتوران- وبسنی گوبند دهی
است که این رود خانه موسوم بآن ده است ۳
(۱) چش: شکته . . (۲) چك: ژند ویلژند.
وژمینی خم‌هست میان جیحون وفرأت .
] موت - با فوفانی بروزن لاعوت .
آشیان جانوران شکاربرا کوبند حمیویاز وشاهین
]هو یا - بکر فوفانی و تضانی بالف
کشیده , بلفت زد و پازن() کنیزك و پرستا
وخدمتکار (۳) باشد ۴ .
۲ موختگان ادل » اب ر ارب
صلوات اف علیهم اجمعین (4) را کوبند . *#
| مود پروزن تابود » بعنی بر آحیخت
=== pdf page ===
```


## [2026-09-07T16:16:43.077Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON malgham ===\"; grep -n \"ملغم\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head -10; echo \"=== MON malidan ===\"; grep -n \"مالیدن\" MON_part1.txt MON_part2.txt 2>/dev/null | head -5"
}
```


### [2026-09-07T16:16:43.160Z] TOOL RESULT

```
=== MON malgham ===
incoming/MON/MON_2vol_Adena_v2_djvu.txt:64804:ملغم: ۰۱ (زمعر . خمیر کر دن] )1( (بر.) 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:64808:ملغم: ۱۱0۳۱ [ع.] (امف.) فلری که با جیوه 
MON_part2.txt:64804:ملغم: ۰۱ (زمعر . خمیر کر دن] )1( (بر.) 
MON_part2.txt:64808:ملغم: ۱۱0۳۱ [ع.] (امف.) فلری که با جیوه 
=== MON malidan ===
MON_part1.txt:4872:مالیدن (رنگ و مانند آن) (مص‌ل.) درهسم 
MON_part1.txt:5396:آهار مالیدن. 
MON_part1.txt:10085:مالیدن» در خاک افکندن چیزی را از دست 
MON_part1.txt:10087:بینی کسی را بر خاک مالیدن. خوار کردن؛ 
MON_part1.txt:12523:است و سنگ و کلوخ بدانجا مالیدن. سنگی
```


## [2026-09-07T16:16:43.728Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SYN leaf 593/594 (p.569) ===\"; awk 'BEGIN{RS=\"\\f\"} NR>=593 && NR<=594' SYN.txt | head -50"
}
```


### [2026-09-07T16:16:45.099Z] TOOL RESULT

```
=== SYN leaf 593/594 (p.569) ===
orture’ to ‘distress, trouble, weary’, refl. ‘distress, trouble, weary oneself, toil’ (cf., through OFr., ME travail with this sense and also with new semantic development ‘travel’), finally in Fr. and Sp. simply ‘work’. REW 8911. Gamillscheg 860. NED sv. travail, travel.
Rum. lucru ‘work’ (abstr.; and concer. > ‘thing’), fr. Lat. lwerum ‘gain, profit’, as also (and prob. first in this sense), Vb. lucra ‘work’ fr. Lat. lucrari ‘gain, 2¢- quire’. REW 5145, 5146. Cf. the rela- tion of ‘gain’ and ‘work’ in the group OE winnan, etc. (below, 5). os
Rum. munca ‘toil’, vb. munci ‘toil’, fr. Slavic, ChSl. mqka ‘torment’, vb. maciti. Tiktin 1021. Densusianu 270.
4. Ir. sdethar, NIr. saothar (es? ‘toil’) : Ir. sdeth ‘trouble, suffering,
» act?
Good
MISCELLA . OB sar ‘pain’, etc. Walde-P.
Goth. es en. 9.495.
9 A5. ae fe Lat. labor (above, 3) - Ir ee Ir. obatr; hence vbs. pope pret. robair RC 25.388;
oprah ron mostly extoriet raf
vere with sb.), NI. aan ihe oad pert (above, 2). Vendryes,
Lat.
ah ‘(abstr. and concr.; vb.
‘expedition, jour-
‘ Ir. fecht ie vehere ‘carry’, etc. Walde-P. Beep 1.123 f. Development
1,250. Ee 5; h ‘undertaking ; te porrowing, influence of ME
m . s two senses ‘toil’ and ‘travel’
travail in it bove, 3): : Br. labour fr, OFr. labour;
Lat. opera. 5 Goth. waurstw, OE weorc, etc.,
above, 1.
Goth. arbaibs (renders xézos ‘toil’), ON erfidi (cf. adj. erfidr, OE earfepe ‘hard, difficult’; OE earfop ‘hardship’), OHG ar(a)beit, MHG, NHG arbeit, Du. arbeid (MLG > Dan. arbejde, Sw. ar- bele), with vbs. Goth. arbazdjan, etc., all prob. : Grk. dppavés ‘orphan’, Lat. orbus ‘bereft’, ChSI. rabié ‘slave’, etc., with de- velopment fr. ‘condition of an orphan’ to one of ‘slavery, drudgery, toil’. Walde-P. 1.183 f. Falk-Torp 31. Feist 55. Kluge-G. 22. oy vinna (with vb. vinna, also ‘gain’) aan vinno ‘suffering’, winnan ‘suffer’,
enh labor, toil’, later ‘win, gain’,
a a a, ae
’ . alde-P. 1.260. pe 1382 f. NED s.v. win, vb. ° Swincan ay ME swinke, with vb. : » Swinken (NE swink arch ? - or
al), parallel 0 : ‘flog, eat, strike ™ to OF swingan
Br. ober fr.
ell, rush , fling’ and ‘fling one- as ae swingan ‘fling, rush’, tvink yb, - 2526. NED S.v.
NEOUS PHYSICAL ACTS, ETC.
Digitized by Arya Samaj Foundation Chennai and eGangotri
541
NE toil (and vb. toil), fr. ME toyle ‘dispute, fight, struggle’, fr. OFr. toil, touil ‘dispute, fight’, back-formation to toiler, toillier ‘dispute, stir up’ (Fr. touiller ‘stir, mix’), fr. Lat. tudiculare ‘stir’ or ‘bruise’, deriv. of tudicula ‘ma- chine for bruising olives’, fr. the root of tundere ‘strike, beat’, REW 8971. Gamillscheg 852. NED s.v.
6. Lith. darbas, Lett. darbs, with vb. Lith. dirbii : OE deorf ‘toil, trouble’, vb. deorfan, further connections dub. Walde-P. 1.863. Mithl.-Endz. 1.439.
Lett. vb. stra
dat, fr. Russ. stradat’ ‘suffer, endure’.
7. ChSl. trudi (renders xézos ‘toil’), with vb. truditz ‘toil, struggle’ (so Boh., Russ., Pol. trud ‘toil, trouble, etc.’, with vbs. for ‘toil’) : Lat. tradere ‘thrust, push’, Goth. us-priutan ‘trouble’, OE préotan ‘trouble, weary’, préat ‘throng, pressure, distress’, préatian ‘press, urge, threaten’ (cf. NE threat, threaten), etc. Walde-P. 1.755. Briickner 577.
ChSI. délo (renders épyov), ete., gen- eral Slavic for concrete ‘work’ : déti ‘put’, etc. (9.11, 12.18). Hence vb. ChSI. (st-)délati in Gospels reg. for Epya- touat, later for xovéw, Boh. délati ‘do, make’ and ‘work’ (Pol., Russ. ‘do’, 9.11).
SCr. rad, back-formation to vb. raditt ‘work’ : ChSl. raditi ‘care for’, Goth. ga- rédan ‘care for’, OHG ratan ‘advise’, Skt. radh- ‘prepare, perform, succeed’, etc. Walde-P. 1.74. Trautmann 235. SCr. development fr. Slavic ‘care for’ through ‘attend to, be busy with’ to ‘work’.
Boh. prdce, Pol. praca (with vbs. pra- covati, pracowaé), prob. : SCr., Slov. pratiti ‘accompany’, Bulg. pratja ‘send’, with development through ‘errand’ to ‘business, occupation’, then ‘work’ in general. Cf. SCr. posao (gen. posla) ‘one’s occupation, work’ : poslati ‘send’. Briickner 434.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
| Digitized by Arya Samaj Foundation Chennai and eGangotri
542 SELECTED INDO-EUROPEAN SYNONYMS
: |
Pol. robota, Russ. rabota (Boh. robota ‘toil, drudgery’; with vbs. Boh. robotztz, Pol. robié, Russ. rabotat’) : ChSI. rabota ‘slavery’ (cf. NG dovAed, above, 2), de- riv. of rabi ‘slave’, this : Goth. arbazps, etc., above, 5.
8.:Skt. karman- ‘act, activity’ and ‘work’ (cf. karma-kara- ‘workman’) : kr- ‘do’ (9.11).
Skt. ¢grama- ‘fatigue, toil’ (with vb
gram- ‘be weary, toil’), etym,? Walde.
P. 2.426, 498. Skt. ¢am- : Grk. kauvw, above, 2, Av. vorazya- : varaz- ‘do, work’, Grk épyor, etc. (above, 1). . For ‘work’ concr. mostly Skt, krta- Av. karota-, OPers. karta- : Skt, kr- ‘do, make’ (9.11). ¢
9.14 BEND (vb. trans.)
Grk. — xéyarw (Avyltw) Goth. (ga)biugan Lith. — lenkti
NG Auyltw (xéurrw) ON sveigja, benda Lett. liekt, luocit
```


## [2026-09-07T16:16:56.225Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '64795,64815p' MON_part2.txt; echo \"=== SYN RUB ===\"; grep -n \"9\\.3[0-9] RUB\\|RUB (vb\" SYN.txt | head"
}
```


### [2026-09-07T16:16:56.296Z] TOOL RESULT

```
عسل معادل چهار مثقال و از داروها به قدر 
یک مثقال. (رسالهة مقداربه. فاز. ۴-۱:۱۰ 
ص ۱۸ ۴.) 
ملعنت؛ 9۸اه [ع. ملعنه | (.) محل 
قضای حاجت» جای تعغوط (غم.) آنجه 
موجب لعن شود. (ف.) بدذاتی» شطنت. 
ملعون: « هه [ع. ۰ (امف.) رانده از نیکی و 
رحمت؛ لعن شده» نفر بن شده. گجسته) ج. 
ملعونین. 
ملغم: ۰۱ (زمعر . خمیر کر دن] )1( (بر.) 
مرهم. (پز.) کهنه و پنبه‌ای که مرهم را بر آن 
مالند و بر زخم نهند. (پز.) روغن‌مالی بر 
اعضای بدن. 
ملغم: ۱۱0۳۱ [ع.] (امف.) فلری که با جیوه 
که 
ملغی: ۱۵ [ع.] (امف.) ناطل کرده؛ لو 
شلد ۵. 


ملفف: ۱03 (ع. (امف.) در ببچنده؛ 

=== SYN RUB ===
14379:9.31 RUB Grk.  rpiBw Goth. bnauan Lith.  trinti NG tplBw ON gnia Lett. _ berzt, trit Lat. fricare, terere Dan. gnide ChSl. tréti It. Sregare Sw. gnida” SCr.  trljati, ribati Fr. Jrotter OE gnidan Boh. trti Sp. frotar, fregar ME = gnide (gnodde), rubbe Pol. trzeé Rum. freca NE rub Russ.  teret’ Tr. commelim Du. wrijven Skt. ghrs- Nir. cuimlim OHG  gnitan, riban Av. Ohh W. rhwhio MHG gniten, riben
```


## [2026-09-07T16:17:04.725Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '14379,14400p' SYN.txt; echo \"=== leaf ===\"; awk 'BEGIN{RS=\"\\f\"} /9\\.31 RUB/{print NR}' SYN.txt"
}
```


### [2026-09-07T16:17:06.277Z] TOOL RESULT

```
9.31 RUB Grk.  rpiBw Goth. bnauan Lith.  trinti NG tplBw ON gnia Lett. _ berzt, trit Lat. fricare, terere Dan. gnide ChSl. tréti It. Sregare Sw. gnida” SCr.  trljati, ribati Fr. Jrotter OE gnidan Boh. trti Sp. frotar, fregar ME = gnide (gnodde), rubbe Pol. trzeé Rum. freca NE rub Russ.  teret’ Tr. commelim Du. wrijven Skt. ghrs- Nir. cuimlim OHG  gnitan, riban Av. Ohh W. rhwhio MHG gniten, riben
Br. rota NHG reiben
For ‘rub’ there is one considerable in- herited group. There are more or less probable connections with words for such various notions as ‘scrape’, ‘gnaw’, ‘grind’, ‘turn around’ (hence first ‘rub with a circular motion’), ‘strike, break’ (hence first ‘rub to pieces’), etc.
1. IE *ter-, with extensions *i7-, *treu-. Here kept apart fr. *ter-, etc. in words for ‘bore’ (9.46), though gen- erally thought to be ultimately the same, fr. an orig. notion of ‘rub with circular motion’. Walde-P. 1.728 ff. Ernout-M. 1032 ff.
Grk. rptBw (rpt-B-, cf. Lat. trwi, tritus; the common word for ‘rub’ down to the
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
present day; in secondary uses relpw, tptw ‘wear out, distress’, rpixw ‘waste, consume’) ; Lat. terere (trivi, tritus) ; Lith. trinti, Lett. trit; ChSl. tréti (*terti), SCr. irtt (with deriv. trljatz), Boh. i7iti, Pol. irzeé, Russ. teret’.
2. Lat. fricare (>It. fregare, Sp. fregar, Rum. freca), VLat. also *frictare (> Fr. frotter > Sp. frotar, Br. frota; but explanation of o dub.; REW 3505, Gamillscheg 445 f., Wartburg 3.787) : friare ‘rub to pieces’, this perh. : Skt. bhri- ‘hurt, injure’, ChSl. briti ‘shear, and ultimately Lat. ferire ‘strike’, ete. Walde-P. 2.194. Ernout-M. 389. Walde-H. 1.549.
MISCELLAN.
h less common than used esp. for
Lat. tereré (mus t, waste’),
F as for Jain rub ’
* ‘ ie andimostly wear OU hres!
cuimlim, epd. of
1. above, im, NIr. ommel ithe _ molere
3, Ir. ¢
W.
a ie fr. Fr. frotter. Henry 126.
ON bnia (rare),
Bo root connection dub. a aie; OHG nian here or to foll.?), Feist 101. Falk-Torp 335. ‘
ON gnia (Norw. gnu), also gnida (rare), OF gnidan, ME gnide (gnodde), OHG gnitan, MHG gniten, MLG gniden (> Dan. gnide, Sw. gnida), perh. with various extensions : Grk. xvabw ‘gnaw, nibble’, OE gnagan ‘gnaw’, etc., or with variant init, : Grk. xvaw, xviftw ‘scrape’, ete. all uncertain. Walde-P. 1.584 f. Palk-Torp 334, 335.
ME rubbe, NE rub, with East Fris. tubben ‘scrape, rub’, Dan. rubbe ‘rub, scour’, Sw. rubba ‘move from one place to another’, prob. : OF réofan ‘break,
=== leaf ===
623
```


## [2026-09-07T16:17:22.419Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SYN leaf 621-623 page numerals ===\"; awk 'BEGIN{RS=\"\\f\"} NR>=621 && NR<=623' SYN.txt | grep -o \"56[0-9]\\|57[0-9]\" | head; echo \"=== SYN leaf 623 marez ===\"; awk 'BEGIN{RS=\"\\f\"} NR==623' SYN.txt | grep -o -i \"marez\\|marz\\|mareza\" | head"
}
```


### [2026-09-07T16:17:23.761Z] TOOL RESULT

```
=== SYN leaf 621-623 page numerals ===
578
576
563
574
567
568
=== SYN leaf 623 marez ===
```


## [2026-09-07T16:17:24.317Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD ===\"; grep -n \"^mālīdan\\|^mālīd\\|^māl \\|^must\\|^mušt\\|^āmurz\\|^framurz\" PHD.txt PHD_mackenzie.txt | head -20; echo \"=== NYB ===\"; grep -n \"^māl\\|^must\\|^āmurz\\|marz\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-07T16:17:24.379Z] TOOL RESULT

```
=== PHD ===
PHD.txt:2875:must (n.) bādag.
PHD.txt:2876:must (v.) abāy-.
PHD.txt:2877:mustard seed spandān.
PHD.txt:4857:mustgar Se F” ^ ale mozag ^ de 96 "пик
PHD.txt:4858:mustan
PHD.txt:4863:mustabarmānd >
PHD_mackenzie.txt:3622:mustl-abarmand [mwstPPlm'nd] aggressive, aggressor.
PHD_mackenzie.txt:3624:mustomand [mwst)wmnd I N mustmand] complaining, unhappy.
PHD_mackenzie.txt:3629:must [mwst I N ---] fist.
PHD_mackenzie.txt:3632:mustan, mal- [mwstn', m'l- IN .......] rub, sweep.
=== NYB ===
1819:Paz., Skr. v. prativädin. < ham + *emäl < *abi-marda- (as to abi- > ē- cf éraxtan, éstatan), *marda- being the SW form of *_marza-, v. málitan and marzihistan.
2342:kün-marz [kwnmle'] sodomy, pederasty 777, 824. — NP kin ‘backside’ + marz, v. marzihistan.
2397:mālišn [m>lšn'], v. n. of the following vb., of the soft touch of a fragrant wind 73%,
2398:malitan [m'lytn'] to stroke 2119. — < *mard-. SW form of marz-, v. marzthistan ; NP mälidan. Inf. also muštan, pt. must < *mrsta-, e.g. Zsprm II, 9. III, 12, ef hištan: hil-.
2476:marzihistan [mlcyhstn'] pres. 3d p. pl. marzihénd [mleyhynd] they are in con- tact (astronomically : in conjunction) 511. — Pass. of marz-. Av. (1152 sq.) maraz- ‘to touch’; MPrs' mrz- ‘to copulate’, mrzyšn ‘eoition’, borrowed from NW, v. Verbum 170 (cf also kün-marz); the genuine SW form is *mard- > mäl-, v. mdlitan.
2477:marz-pän [mlep’n'] governor of a border district, margrave 1*. 115°. 117’. — Av. (1153) maraza- ‘border district’, MPrth mrz (A-H III, BBB) + pin ‘protector’, v. pünak; borrowed in Arm: marzapan, in Aram: Syr marzbänä = Talm, and in Arab: marzubün; NP marzbün.
2602:must [mwst', inscr. mwsty] violation, outrage: ~ u gilak 761; api-š ... must u dróg andar nést and there is no violation and no lie (fraud) in it (= in the passage, i.e., to be feared when passing over the bridge) F:7; [~ u adātihā i-Sän patiš kunénd violation and iniguities which they commit against them (viz. water and fire) JN 16%]. — Paz. must, Skr. v. balätkära (Mx), possibly SW form < mušti- from Skr mus- ‘to rob, to steal, to plunder’; not identical with NP must, v. S. v. mödak.
2603:must-aparmänd [mwst' ’plm’nd] con- tumacious, insolent (hac towards) 41%; [the drunkard is ~ Mx 168]. — Paz. mustāvarmgd, Skr. v. balātkārin (Mx). Possibly ‘one who is aparmänd through violence, outrage’ (must, v. above): apar- mand (ci ?apar) ‘one who has got the upper hand and retained mastery’, subst. ‘compulsion, force’ [hàn dāt $$ pat aparmünd frdc avis mat ‘the law that has been enforced upon him’ PR 86-7]. The explanation of Bthl, ZsR V, 53- 56, seems little probable; quite unaccept- able is that of Herzfeld, ApI, 247—249.
2604:mustäpät [mwst’p’t'] merry settlement, in Xosrot-— the name of a town, other- wise unknown, in Western Iran 114%. Cat. 58sg. — āpāt v. āpātān; must < *musta-, pt. of Olr *mauö-, Skr modate *to be delighted', whenee Av. (1109) maodanö.kara- ‘affording sensual plea- sure’, (280) ahömusta- < *a-ham-musta- ‘disgusting’.
2605:mustömand [mwst’wmnd] outraged, vio- lated, pl. cas. obl. ~-dn 8?9. — ‘Exposed to must? (g. v.); NP mustmvand ‘poor, wretched’. Cf in active sense must-kar ‘defecting from (hac) his sovereign, re- bellious’ KnS IV, 2.
2930:pänak [p'nk'] protector 521%, 66%, — M PrthPrs p’ng (cf BBB, Gl s.v.); NP panah (v. Steingass). Av. (888) pūna-; cf marz-pän, stör-pän.
3109:must go back to *pati-yam- ‘to take hold of’, from Av. (1262sg.) yam-, chiefly with preverbs. I find *pāyam as a v. n. in two passages: 1. DkM 285 aköman ... menisn päyam ‘A. holding Mind in his grasp’; 2. ibd. 501? páyam hešm andar ménisn “Wrath taking Mind in his grasp’ (?). — Zsprm VIII, 4 has a somewhat divergent, perhaps more original version of the story 441-9: ^L ZLWN ‘L y’twk’n, MH-t L>? HWH-nd byšznyt'l, BR’ L'WHL ‘L h'nk' ZLWN, YDH BYN ml PWN "MŠH' ZY TWR’ ZY MDM thé YDLWN-t', hysme bwd wt'p' PWN NPSH-tn' zhk' MNW-t PWN 'škmb' = mà šav o yātūkān, cē-t nē hend bēšazanī- tar, bē apāc 6 xanak šav, dast andar mal pat rógn % gāv i apar ātaxš burt, hésm-ic bod vitāp pat x"ēš-tan zahak ké-t pat aš- kamb ‘do not go to the sorcerers, for they cannot heel thee, but go back home, rub thy hand with ox-tallow which has been. set on fire, and burn fragrant fuel for the benefit of thy offspring which is in thy womb’.
5227:maé0ana-: mahmančh mahrka-: marg Mahrküsa: Markus maičyšna-: miyan maidy6.zaromaya-: maióyozarm mainyaoya-: mönöi mairya-: ?mar, mérak maxši-: *macäh Iman-: mčnitan, 6mét 2man-: mandan manah-: hešm-manihš Manuš-ciEra-: Manucihr maodanö.kara-: mustā- pät Imar- (mirya- morota-): murtan ?mar-: amar ?mar- + avis: ošmurtan maroz-: marzihistan maroza- -- pana-: marz- pan Maryu (Mouru-): Marv maršo.kara: "maškar mas-, Masan-: mas masya-: mahik mašya-: mart mafra-: mānsr mafra-sponta: mahras- pand (fra-)may-: framātan (ni-ymāy-: ni-mütan (pati-ymāy: patmān mazdayasna-: mazdēsn mazga-: mazg meroždā-, meroždika-: āmuržītan midaoxta- (mi€oxta): mitöxt miOra-: mihr
6045:mrw: ?murv mrz-: marzihistan mwrdy?ng: Mahlah mwrw: lmurv mwrw?: murvāk mwy'g: mödak my?n: miyàn myrd: mart mysg: hamésak mzd: mizd
6733:must: ~
6734:mustävarmad: must- aparmand
7256:malax: Sak malidan: malitan mana: mānākēh mānistan: mānākēh māndagī: māndakēh mary: *murv marzbàn: marz-pàn mäyah: mātakēh mazah: micak
7261:must: modak mustmand: mustómand
```


## [2026-09-07T16:17:42.725Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD amurz ===\"; grep -n \"murz\\|mwlc\\|amurz\" PHD_mackenzie.txt | head -10; echo \"=== BRT marez ===\"; grep -n \"1152\\|1153\" BRT.txt | head -5; grep -n \"maroz-\\|marez-\\|marəz\" BRT.txt | head -10"
}
```


### [2026-09-07T16:17:42.789Z] TOOL RESULT

```
=== PHD amurz ===
1016:imurzidan, iimurz- [)mwlc-ytn l 1M )mwrz-yd, N -] forgive, pity, have
1056:an-Imurzid ['n'mwlcyt l I M 'n'mwrzCyd] merciless.
1057:an-amurzisn ['n'mwlcfn'] mercilessness.
6635:forgive abaxsiiyidan, iimurzidan,            from az.
6637:forgiveness abaxsiiyisn, iimurzisn.          frontier wimand.
7057:marten xaz.                                merciless anamurzid.
7058:marvel abd sahistan.                       mercilessness anamurzisn.
7060:mask padam.                                mercy abaxsayisn, amurzisn; have '"
7061:mast frasp, stun(ag).                        abaxsayidan, amurzidan.
7294:pity amurzidan.                            portionless abahr.
=== BRT marez ===
20063:1152
```


## [2026-09-07T16:17:43.845Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD && awk 'BEGIN{RS=\"\\f\"} NR>=81 && NR<=83 {print \"### pdf \"NR; print}' FFD_pages.txt | head -60"
}
```


### [2026-09-07T16:17:45.922Z] TOOL RESULT

```
### pdf 81
[pdf page 81]
وا فعلهای قارسی دری
دا 2 لشت.
لشت « ایرانی باستان 715-1۵*. برای 1۵ -> آراست. 7:2* صورت اصلی کل* است. 7
َ پیش از ۲ به 5 بدل شده است. ریشهٌ 72* صورت ضعیف ريشةٌ 7۵2* است» به معنی
«لیسیدن).
لیس + ایرانی باستان 1۵12-2*. برای 2 -> آرای. «س» در «لیس» به جای 2 آمده است.
ماندن
ماند < فارسی میانه 13324 < ایرانی باستان ۳30-12:*. برای 1۵ -* آراست. ريشهٌ
به معنی «صبرکردن» است.
مان < فارسی میانه 832 < ایرانی باستان 038-8*. برای 2 آرای.
«ماندن» فارسی دری و 38420 فارسی میانه جانشین دو ريشةٌ ایرانی باستان
شده‌اند» یکی 337 به معنی «صبرکردن» و دیگر 8 ج 0039۵ 930۵ که اسم
است و در فارسی دری «مان» شده» در ایرانی باستان به عنوان مادهٌ جعلی و با معتی
«سکونت کردن» به کار برده شده است.
مانست-
«مانست» مادةٌ ماضی جعلی است. از «مان» < فارسی میانه 830 < ایرانی باستان
42 13302 ماد مضارع جعلی است از 13382. 12372 اسم است به معنی «هیئت
ظاهری».
مُردن :
مُرد < فارسی میانه ۵۶۵ < ایرانی باستان 13-1۵" برای 12 > آراست. 17
صورت ضعیف ريشةٌ 1387 به معنی «مردن» است.
میر < فارسی میانه 3۲۲ < ایرانی باستان 2دیط*. برای ساختن مادهٌ مضارع از
ریشه به کار می‌رفته است.

### pdf 82
[pdf page 82]
ماده‌های ماضی و مضارع قارسی دزی شش ۷۷
مشت.
مُشت + فارسی میانه 151 + ایرانی باستان 1۹-1۵*. برای ۵ > آراست. 177
صورت.اصلی ۲5 است» 2 پیش از ۲ به 5 بدل شده است. 172 صورت ضعیف ريشهةٌ
2 به معنی «مالیدن» است.
مال + فارسی میانه 721 + فارسی باستان 1۵۳4-8* < ایرانی باستان 1۵72-۵*. برای
3 > آرای.
موییدن
«مویید» مادهٌ ماضی جعلی است. از مادهٌ مضارع ساخته شده است.
موی < فارسی میانه 136 < ایرانی باستان 1۳۵-2*. برای 2 آرای.
ریش 13200 به معنی «نالیدن» است.
نازیدن
«تازید» مادهٌ ماضی جعلی است. از مادةٌ مضارع ساخته شده است.
ناز ج فارسی میانه 232 + ایرانی باستان ۸32*. 232 در ایرانی باستان اسم است به
معنی «شادی»» «افتخار». 132 در فارسی میانه «شاد بودن» «مفتخر بودن» معنی
می‌دهد.
نالیدن
«نالید» ماده ماضی جعلی است. از ماده مضارع ساخته شده است.
نال ج فارسی میانه 281 < ایرانی باستان 8۵۲۵-۵*. برای 2 آرای. ريشةٌ 1874 به ۱
معنی «بانگ کردن» است.
نشاست < فارسی میانه 213391 < ایرانی باستان 339-۵-زم"

### pdf 83
[pdf page 83]
۸ فعلهای فارسی دری
برای 1۵ -> آراست. 11 پیشوند فعلی است. ۸34 که صورت بالاندةٌ ريش 144 است.
صورت اصلی 538 است. 1 پس از آبه 5 بدل و 4 پیش از 1 به 8 بدل شده است.
تشان <ج فارسی میانه 81530. 8827 که در فارسی میانهٌ ترفانی مادةٌ مضارع 215291
است» صورت درست مادةٌ مضارع است. از ایرانی باستان ۸1-334-2*. برای 2 > آرای.
«آمدن» 2 به جای در 2538 ظاهراً به قیاس با 2518 و 315281 بوده است.
«نشاخت؛در فارسی‌دری به‌وجود آمده‌است. 134 صورت بالانده در معنی واداری به
کاررفته‌و 40 اصورت افزوده درمعنی لازمی.از 1124(«نشستن) به وجو د آمده‌است-> نشستن.
```


## [2026-09-07T16:17:58.614Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '20055,20080p' BRT.txt"
}
```


### [2026-09-07T16:17:58.669Z] TOOL RESULT

```
•  g.  marad-  V.  'verderben'.  Praes.  3 mand-,  9  mSrmda-''^.
'verderben,  zu  Schanden,  zunichte machen':  dui.sastii  sravS  mdr^ndat  kvs jyatfui  sfnghanais  xratam  "der  Inlehrcr macht  die  (heiligen)  Worte  zu  Schanden, er  den  Plan  des  Lebens  mit  seinen  Lehren" Y.^2,9;  —  hvB  ma  na  srava  mSfyndaJ"dei ists,  der  die  (heiligen)  Worte  zu  Schanden macht"  Y.^2. 10;  —  ta&'^  ma  mSnndm jyBlüm  "die  sinds,  die  das  Leben  zunichte machen"  Y.  32. 11;  —  yöi  gSus  mSnndan urvaxs.uxil{sd.)jysfam  Y.j2.i  2.  a)  Med. im  refl.  Sinn :  fä  dngvats  dalnä  *mandaiti*> *>rxiaos  {sd.)  Aaihm  Y.5/.  13.
ai.  VgL  mi-dnäti  'er  lerreibt'.  —  Pü.i  mum- JinTlanSt,  mumjemhi  däianS),  (la  Y.  J/):  5f- murtan.  —  ')  Ar.  *ii^nd',  %  368.  4.  —  »)  K  5 usw.;   NA.  -/r.  —  J)  Vgl.  in  marik-.
•  p.  »*  "marda"'  »»^  Bh.5.  i. HeratellungsTetBiicb  bei  JOffekt  La  Langue .. des  Mides  159,  Foy  KZ.  3$.  48.
dby  Google
"5>
marotä-
mar»z-
1152
•  j.  man^-  £  -  ?  -,  eine  Landplage Margianes:  mSurum  . .  aat  ahe  paüySrim ß-ak^rmlat  atars  mainyuf..  °ham/a  vl%u- iqmea  V.  i.  5.
*Pä.!  5mil  (HORN  BB,  //.  36s)'J,  erl.:  ahm/') I  ayäaiSrin  an  yäi  kitnind.  S.  dazn  die  GrB.- Stelle  bei  Dst.  ZA.  2.  8.  —  ')  amar;  ich halte  die  obige  Lesung  nicht  für  sicher;  GrB. hat  am  n  ar.
•  p.  marduniya-  m.  EN.  eines  Persers, Mardonius:  *gaubrtan^  nämt^  °yahyä pu%'^J'  parst^  Bh.4. 18.
VIL  AbleiL  aus  "marduna-  m.  •Winier';  Yg'- np.  mul  'Wein',  ai.  m^dvikä-  f.  'Weintlock' 0. —  •)  Doch  ».  auch  ZDMG.  54.  35g,
•  j.  maraSra-  n,  'Merken,  Imgedächtnis- behalten*:  'rtmca  vam,Tmca  dmnaya  vaa- kuy&  Y.  22. 3.        DS.  'räi  als  Inf.  sbcs.
Zum  V.  *niar-.  —  Pü. :  BsmutihüA,  Sü. :  adhya-
•  j.  maradrü  Inf.  'im  Gedächtnis  zu  be- halten'; IUI  ahurahe  mazdä  dan%räi  (sd.) . .  xratam  .  .  m*  .  .  Aisvqm  , .  fraväkäi mahrake  sp?niahe  Yt  i.  aS,
Zum  V.  »«ar-.  —  Vgl.  mar>%ra:  —  Pü. *eimurilii  räi.
•  j.  mairya-  Adj.  (fem.  ya-)  'betrügerisch, tückisch,  schurkisch;  Schurke':  *ahalcti ♦»/•«'>  (NSf.)  nas'atagca  'ys  "und  es  wird  zu Grunde  gehen  die  Schurkin  und  verder- ben wird  der  Schurke"  Yt/p.ia;  4.Z; —  armatsis  deihrubya  avästryaia  (sd.) -ys  Yt/.  29;  —  tmnniaite  vJspqm  daiti- haom  'yS  mihrSjruxl  YLJ0.3;  —  °yS drvi  bizangrs  V.  5,  35;  —  sii^rqm yqm  karafnqmüa  'yanqmla  bieangn aimcur/anqmca  Y,  <>.  18;  —  *JanyS. 'yayh  Y.  JO.  15;  —  mä  hl 'y3  giurvayHt ma  /akika  Yt.<?.59;  —  nSU  *'yehe'''  ttSij jakikayä  t.io;  —  'yS  tBiryS  franrase  Yt. J.41,  J5-S6.  82;  8»,  77.5-5°;  —  'r^^ tairim/raarasyanam  YL5. 18,  zz,  ip.  77, Y. //.  7;  —  °yeke  tyaonaAe  ar»jal.aspahe Yt.  5.  30 ;  —  tafsatca  AS  °yB  (näml.  aiis srvarü)  Y.p.  11;  —  "«(NSC)  .  .  bSsyqsta FrW, /0.4a;  —  Sai  mqm  °yS  äkasat  atsrö mainyui"V.22.a;  2.  '  a)  ASn.  'rfm  ' Adv. 'trügerischer Weise.betrüglich':  a/trqm *rTm  küsayeiti  (sd.)  anaiwySstS  dalnqm "betrüglich  handhabt  die  Strafgeissel,  wer nicht  . ."  V.  18.  41'.  \az»M  maire  Yt /.  ag:  lies  zamara^
Vgl.  mp.  mar,  air.  mtUaim  Ich  betrüge',  liL n/fo/ 'Lüge',  arm.  n^/ 'Sünde';  LitLbeiHBU. AGr.  f.  473.     Falich  GlrPh.  2.  531). —  Pü.:
vua;  {zaY.ro): marämt;  S&. :  n^iamtah,  erL: nüj'ifa^i  Npü.:  räixoH  'Sttaasenränber'.  S. noch  No.  2.  —  >)  NA.  mart.  Lesung  un- sicher.—  ■)  Hds.  maraie.  Vi.:  mär;  s.  aber Yt  S.  59.  —  })  Dst.  'il  manie  un  Ashira mairya  irrf  golier',  womit  zuvor  *ainim  überaetzt wurde.  Aber  ainim  (sd.)  fehlt  hier,  musa  alio dem  Sinn  nach  ungefähr  durch  mairim ,  das D.  stillschweigend  Icoirigirt,  ersetzt  sein.  S. jetzt  auch  Gdn.  SPreussAW.  zg.  423.  zFü.  t. unter  käiaya-.    —  4)  S.  dazu  Bthl.  LG&RFh.
j.  maurvay-  m.'>  'Ameise',  ein  daemscbes Tier,  von  dem  zwei  Arten  geschieden werden:  xrafstnm  ava.Janalta  moffifftn danHjtarsim  (sd.)  V.  16.  la;  —  hagvan maoirinam  danS.iarsanqm  ava.Janyat  V. 14.S1  ^o-73i  —  baiiian  maoirinqm  arai- kanqm  (sd.)  kutakanqm  duiaininqm  ava.- /anyai\:i4.$.
Aus  ar.  'marg'  oder  ^margg' ;  zSchr.  ni*w* s.  S  ^6S.  44.  —  mp.  (Pü.),  np.  mär ').  Weiteres bei  Hbm.  AGr.  /.  476,  IFAnz.  10.  23;  dara noch  Wn.  AiGr.  /.  277.  —  >)  Gegen  den  An- sati  eines  fem.  "vt-  sprechen  die  Epitheta.— ')  VgL  mp.  ier  unter  baoiryo:
•  j.  maraz-  V.  'streifend  berühren'.  Praes. 2  marsza-,  3  mfrpza-,  8  m^qz-''>.  —  Int m^rqidyäi.  [S,  noch  zu  mfr>^yumna-^
1)  'streifend  berühren,  streifen';  mürpm .  .yS  .  .  aiwyaiti  .  .  mar»zaiti  <^a  karatia ai^Aä    z>md    Yt  10.  95.  2)    'im  Flug
streifen':  värrfnahe..y5  vasaiie,.barjmavö marizat  gairinam  Jqfnavd  marpxai  numam Yt.i4~i9-'i;'2i'.
mit  aipi  '(ein  Tor,  Akt.)  anbrmgea  an  -' (Akk.):  apica  hm  vanm  mar»sa  dvanm (sd.)  raolamm  V.  2. 30;  38  (wo  manxat).
```


## [2026-09-07T16:18:00.379Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FSF faramarz ===\"; grep -n \"فرامرز\" FSF_pages.txt FSF.txt 2>/dev/null | head -5; echo \"=== ARY malidan ===\"; grep -n \"مالیدن\\|آمرزیدن\\|ملغم\" incoming/ARY/ARY_pages.txt | head -10"
}
```


### [2026-09-07T16:18:00.452Z] TOOL RESULT

```
=== FSF faramarz ===
FSF_pages.txt:3049:                                                                ‫زواره فرامرز و دستان سام‬
FSF_pages.txt:3959: ‫(‪)۱-۷۸-۲۴۱‬‬                                       ‫فرامرز دستور می‌دهد برای ساختن تابوت‬
FSF_pages.txt:10726: ‫سر به شکل بادبزن چینی بیرون‬                                      ‫زواره فرامرز و دستان گویو‬
FSF_pages.txt:11507:     ‫بمان تاکندشان پزشکان درست‬                             ‫سام‬      ‫و دستان‬    ‫زواره‪ .‬فرامرز‬
FSF_pages.txt:12217:     ‫به سوی فرامرز برگشت باد‬                       ‫فرهنگ‌ها و فهرست و لف نیامده است)‪:‬‬
=== ARY malidan ===
13621:(شاید بدین علت که شبر دوشیدن ستلزم "مالش " با "مالیدن" است.)
13871:بازگشت به: مالیدن,
```


## [2026-09-07T16:18:11.065Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && sed -n '13600,13640p' ARY_pages.txt; echo \"=== pdf page ===\"; grep -n \"\\[pdf page\" ARY_pages.txt | awk -F: '$1<13621' | tail -1"
}
```


### [2026-09-07T16:18:12.487Z] TOOL RESULT

```
5 1۸746 فریزی کهن (۷لفاقل۶ 0۲0): ۸681,0۳
تخاری 8 (8 ۷فل705۸۶): ۸1۸1148 آلمانی کهن (0274۸۷ 07اب صام).
سانسکریت (8۸(۷577): ۱11-7 ,۸1813۸36
[pdf page 458]
تج
مام مامی» ماما (به چم *مادن) / ۴۵۹
آلمانی (4(۷ان027): ۰ ۱/1765 ,۸1812689
انگلیسی کهن (80//80 ۵۲۵): 1/8۸0 پسگشت‌ها کرت
انگلیسی (باقلاه(8): 5 2225 ۶008۳
دانمارکی (0۸۸1874): 8 بای امین ان
سرئدی (81750150): 8 5 مته0)5) ,دککاکه تاج
نروژی (/(۵۷08804): ۱7016 ,3/8 269 هط
هلندی (7ظع007)+ دا 1 (۲8) :2/3
اسلاوی کهن (76هما؟ 64 ناه صا0): 69 ,385-386 ماه
1 ,۸/1۲70 6 (01۵) :00/5
لیتوانی ((414تا734/): ۸2 5 (041134) +357
ایر دی کهن (للفلقا .ا0): را 0 برهان قاطع + 1۹۳۸
آلبانی (/(4ا7لمقته): انا
یادداشت:
۱ چم این واژه در کردی: جاروب کردن,
چم واژه‌های این فهرست (به جز اوستایی و پهلوی و فارسی و کردی و بلوچی و سانسکریت): شیر» شیر دوشیدن
(شاید بدین علت که شبر دوشیدن ستلزم "مالش " با "مالیدن" است.)
۲ میان این واجربشه و واجریشه‌ی م۱187 (716-1717 :۳07۳01079) خویشی نزدیکی وجود دارد.
| تمانگلیس سروازای ارس ۱۷۸۷۸2۸۸
پهلوی (/ا2۸۶):(پازند) 3 ایسلندی کهن (9420/0۸ 0):
اد اففانی (پشتر) (//4۳0۸0): ۹ ۸
ساننکریت )1 ‎٩24۸‏ ,۷2 آلمانی کهن (0570/(0 04 0ا0):
ارمنی (۷۵/8(/4(۷ ۶ ‎٩۸۸۲‏ ,۸۸۵۲۸ 0۸۸
بونانی 028/0): ۰ ۸12۸/۸/5 ,۸180181۸ آلمانی (08//۸(0): ۰ ۱۸/۵/8 بفاق۸
لاتین (/712م): ۸۹۸۸ انگلیسی کهن راتوناه/20 ام : ۸ااحا
فرانسه (۳۳8/4): 11/۸ انگلیسی (8001870): ۱
اسپانیایی (52۸/184): ۸۸ ۸ ,۱۱/۸59 ,36تا34 ,3۸۵10۸ ,۸۸۸۸
ابتالپایی (20مالا7): ۱۸ هلندی (007614): ۸۸۸ : ۱
رومانی (1۸1۸(۷اتاه): ۸ اسلاوی کهن (ع1لشاد 21708614 2ا0):
[pdf page 459]
۰ | مان (به چم *خان* و "خانه" مثلاً در "خان‌ومان», يا «خانمان»)

۸۸ کورن والی (1ل007/15): 3
لهستانی (۳0/./317): ۸۸ آلبانی (الفاقام: هید ,شرجمید
روسی (0لفا59لا): ۸ هتیت ۱ با خلااقهل<
چک (2800): ۱۷۸3/2۸ بفاها( ای
=== pdf page ===
13603:[pdf page 458]
```


## [2026-09-07T16:18:21.754Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && awk 'BEGIN{RS=\"\\f\"} NR==458' ARY_pages.txt | head -25"
}
```


### [2026-09-07T16:18:23.081Z] TOOL RESULT

```
[pdf page 458]
تج
مام مامی» ماما (به چم *مادن) / ۴۵۹
آلمانی (4(۷ان027): ۰ ۱/1765 ,۸1812689
انگلیسی کهن (80//80 ۵۲۵): 1/8۸0 پسگشت‌ها کرت
انگلیسی (باقلاه(8): 5 2225 ۶008۳
دانمارکی (0۸۸1874): 8 بای امین ان
سرئدی (81750150): 8 5 مته0)5) ,دککاکه تاج
نروژی (/(۵۷08804): ۱7016 ,3/8 269 هط
هلندی (7ظع007)+ دا 1 (۲8) :2/3
اسلاوی کهن (76هما؟ 64 ناه صا0): 69 ,385-386 ماه
1 ,۸/1۲70 6 (01۵) :00/5
لیتوانی ((414تا734/): ۸2 5 (041134) +357
ایر دی کهن (للفلقا .ا0): را 0 برهان قاطع + 1۹۳۸
آلبانی (/(4ا7لمقته): انا
یادداشت:
۱ چم این واژه در کردی: جاروب کردن,
چم واژه‌های این فهرست (به جز اوستایی و پهلوی و فارسی و کردی و بلوچی و سانسکریت): شیر» شیر دوشیدن
(شاید بدین علت که شبر دوشیدن ستلزم "مالش " با "مالیدن" است.)
۲ میان این واجربشه و واجریشه‌ی م۱187 (716-1717 :۳07۳01079) خویشی نزدیکی وجود دارد.
| تمانگلیس سروازای ارس ۱۷۸۷۸2۸۸
پهلوی (/ا2۸۶):(پازند) 3 ایسلندی کهن (9420/0۸ 0):
اد اففانی (پشتر) (//4۳0۸0): ۹ ۸
ساننکریت )1 ‎٩24۸‏ ,۷2 آلمانی کهن (0570/(0 04 0ا0):
ارمنی (۷۵/8(/4(۷ ۶ ‎٩۸۸۲‏ ,۸۸۵۲۸ 0۸۸
```


## [2026-09-07T16:18:27.574Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && awk 'BEGIN{RS=\"\\f\"} NR==457' ARY_pages.txt | head -20"
}
```


### [2026-09-07T16:18:29.064Z] TOOL RESULT

```
[pdf page 457]
۵۸ ا مالیدی ‏
ایسلندی کهن (۷ل0104۷لف3 صان): سرئدی (8ا0تزی): ۸7
[ ۱ 7 نروژی (/۸فا۵/08۲/80: 2۸7
۱ ساکسونی کهن (2430000 ضا0): ۰ 11571 آلبانی «مامنا: رقف« ,نفد
فریزی کهن (/(54ل77 2ا0): 7 اه ی
آلمانی کهن (/0870400 104بز طزه): پسگشت‌ها اش
۸2 ,21۸87 5 ما و
آلمانی (/02#9442): دنا نا 06 پاک انا
انگلیسی کهن (لفل2۷0 صام: 1/518 565 :01۵8
انگلیسی (بل8لا8۸/0): ۸7 برهان قاطع : ۱۹۴۱-۹۴۲
دانمارکی (0۸7/5): ۸0
یادداشت,
۱- چم این واژه در زبان‌های ژرمنی؛ خوراکه» چاق کننده» گوشت.
چم این واژه در زبان یونانی؛ پستان,
چم این واژه در زبان لاتین: پر سرشار» خیس بودن.
۲ واژه‌ی فارسی که" (به چم "چربی ماست") یز از همین واجریشه آمده است (6947072070).
۳ واژه‌ی فارسی "ماسیدن" نیز از همین واجريشه آمده است.
اوستایی (487/1): 7 ۱1۸811 3683 2۸32
1 ,ات۸2 دتفا یرنانی (02880): ۸۹۸۵10310 ,۸۸160
```


## [2026-09-07T16:18:40.120Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in \"^mutton\" \"^mollusk\" \"^mulch\" \"^emulsion\" \"^enamel\" \"^malt,\" \"^mild,\" \"^melt,\"; do echo \"--- KLN $w\"; grep -n -m1 -A4 \"$w\" KLN_1966.txt | head -8; done"
}
```


### [2026-09-07T16:18:41.586Z] TOOL RESULT

```
--- KLN ^mutton
24785:mutton
24786-1021
24787-myosin
24788-‘to  grunt,  mutter’,  whence  also  L.  muttire, mutire,  ‘to  grunt,  mutter’,  Lith.  mute,  Lett. mute,  ‘mouth’,  ON.  mudla,  ‘to  murmur',  OHG. mutilon,  ‘to  murmur,  mutter;  to  drizzle’.  Cp. mot,  motet,  motto.  Cp.  also  the  imitative  base *mu-,  whence  Gk.  p,u£tv,  ‘to  be  shut  or  closed (said  esp.  of  the  lips  and  eyes).  See  1st  mystery and  cp.  mute.
24789-Derivatives:  mutter ,  n.,  mutter-er ,  n.,  mutter- ing-ly,  adv.
--- KLN ^mollusk
24206:mollusk,  mollusc,  n.,  any  of  the  Mollusca.  —  F. mollusque,  coined  by  the  French  naturalist,
24207-Baron  Georges-Liopold-Chretien-Fredcric-
24208-Dagobert  Cuvier  (1769-1832)  fr.  L.  molluscus, ‘soft’  (in  mollusca  nox,  ‘a  soft  kind  of  nut  with  a thin  shell’),  fr.  mollis,  ‘soft’.  See  mollify, molly,  n.,  a  milksop,  an  effeminate  person.  Fr. Molly,  a  pet  form  of  Mary.  Cp.  Moll,  moll,  and next  word.
24209-mollycoddle,  n.,  a  person  who  coddles  himseli. Prop,  ‘a  molly  that  coddles  himself  .  —  See  prec. word  and  coddle.
24210-Derivative:  mollycoddle,  tr.  v.
--- KLN ^mulch
--- KLN ^emulsion
13030:emulsion,  n„  a  milky  fluid.  —  ModL.  emulsio, gen.  -dnis,  fr.  L.  emulsus,  pp.  of  emulgere.  See emulgent  and  -ion  and  cp.  prec.  word. Derivative :  emulsion-ize,  tr.  v. emulsive,  adj.  —  Formed  fr.  L.  emulsus,  pp.  of emulgere.  See  emulgent  and  -ive. emunctory,  adj.,  excretory;  n.,  any  organ  of  the body  carrying  off  waste.  —  Late  L.  emuncto- rium,  ‘a  pair  of  snuffers’,  fr.  L.  emunctus,  pp.  of emungere.  ‘to  blow  the  nose’,  fr.  e-  and  mun- gere,  ‘to  blow  the  nose’.  See  mucus  and  -ory. Emys,  n.,  a  genus  of  turtles  (zool.)  —  ModL.,  fr. Gk.  l\Lb;,  gen.  ijuiSo?,  ‘fresh  water  turtle’, which  is  of  uncertain  origin.  It  possibly  stands for  *Fep.ur  and  is  a  derivative  fr.  I.-E.  base *wem-,  ‘to  spit,  vomit’,  whence  also  Gk.  tueiv, ‘to  vomit’,  and  is  so  called  from  the  bubbles emitted  by  the  animal  under  the  water.  See emetic  and  cp.  the  second  element  in  Chry- semys.
13031-en,  n.,  1)  the  letter  n;  2)  anything  resembling  the letter  n.
13032-en-  (em-  before  p,  b,  m),  pref.  meaning  ‘in,  into’.
13033-—  OF.,  F.  en-,  em-,  fr.  L.  in-,  -im;;  see  1st  in-. This  pref.  is  often  used  to  form  verbs  from English  nouns,  in  which  case  the  pref.  en-  means ‘to  put  into’  (cp.  embay,  embed,  enshrine).  It is  also  added  to  English  adjectives  and  nouns to  form  causative  verbs  (cp.  embitter,  enable, ennoble,  enslave).
13034-en-  (em-  before  p,  b,  m;  el-  before  /;  er-  before r),  pref.  meaning  ‘near,  at,  in’.  —  Fr.  Gk.  iv, ‘in’,  which  is  cogn.  with  L.  in.  See  1st  in-  and cp.  prec.  pref.  Cp.  also  Gk.  t;,  d;  (for  *tv;), ‘into’,  foo,  Ion.  efao>  (for  *£vaco),  ‘in,  within’, and  see  eso-,  esoteric.
--- KLN ^enamel
13040:enamel,  tr.  v.  —  ME.  enamelen,  fr.  AF.  ena- mayller,  fr.  1st  en-  and  amayl ,  fr.  OF.  esmail  (F. email),  which  is  a  Teut.  loan  word.  Cp.  OHG. smelzen,  OE.  meltan,  ‘to  melt’,  and  see  melt, smelt.
13041-Derivatives :  enamel,  n.,  enamal(l)-er,  n.,  enamel- (l)-ing,  verbal  n.
13042-enamor,  enamour,  tr.  v.  —  OF.  enamourer,  fr.  1st en-  and  amour,  ‘love’,  fr.  L.  amorem,  acc.  of amor.  See  amorous.
13043-Derivatives:  enamo(u)r-ed,  adj.,  enamo(u)r-ed- ness,  n.
13044-enanthema,  n.,  an  eruption  on  a  mucous  mem¬ brane  (med.)  —  Medical  L.,  fr.  2nd  en-  and Gk.  fiv&7)p.a,  ‘efflorescence’,  fr.  Svllo?,  ‘flower’. See  anther  and  cp.  exanthema, enantio-,  combining  form  meaning  ‘opposite’.  — Gk.  £vav -no-,  fr.  tvtxvrto;,  ‘opposite’,  fr.  ev  (see 2nd  en-),  and  avr'io;,  ‘opposite’,  fr.  avxt,  ‘over against,  opposite’.  See  anti-, enantiopathy,  n.,  allopathy.  —  Fr.  Gk.  £vxv- Ti07talH)i;,  ‘of  contrary  properties’,  fr.  tv avxio;, ‘opposite’,  and  7raffo<;,  ‘suffering’.  See  enantio- and  -pathy  and  cp.  allopathy,  homeopathy, enarthrosis,  n.,  a  ball-and-socket  joint  (anat.)  — Medical  L.,  formed  with  suff.  -osis  fr.  Gk. gvapSIpoi;,  ‘jointed’,  fr.  ev  (see  2nd  en-)  and &p&pov,  ‘joint’.  See  arthro-,  and  cp.  arthritis, en  bloc,  in  a  lump.  —  F.,  fr.  en,  ‘in’,  and  bloc, 'block,  lump’.  See  1st  en-  and  block, encaenia,  n.,  annual  ceremony  of  the  dedication
--- KLN ^malt,
22697:malt,  n.  —  ME.,  fr.  OE.  mealt,  malt,  rel.  to  OS., ON.  malt,  Du.  mout,  OHG.,  MHG.,  G.  malz, ‘malt’,  and  cogn.  with  Ol.  mrduh,  ‘soft,  mild’, Gk.  (3Xa8apo<;  (for  *pXaBap6(;),  [3Xa8u?  (for ‘pXocSui;),  ‘loose,  spongy’,  piXSetv,  ‘to  melt, make  liquid',  apaXStiveiv,  ‘to  grind,  destroy’,  L‘ mollis  (for  *mo!dwis),  ‘soft’.  All  these  words  are traceable  to  I.-E.  *mel-d-,  a  -^-enlargement  of base  *mel-,  ‘to  grind’,  whence  Gk.  poXr),  ‘mill’, L.  molere,  ‘to  grind',  molina,  ‘mill".  See  mill, ‘machine  for  grinding",  and  cp.  meal,  ‘edible grain’,  and  words  there  referred  to.
22698-Derivatives:  malt,  tr.  v.,  malt-ing,  n.,  malt-y,  adj.
22699-Malta,  n.,  an  island  in  the  Mediterranean.  —  Fr. L.  Melita,  Melite,  fr.  Gk.  MsXIttj,  fr.  Phoen. melita,  lit.  ‘place  of  refuge’,  fr.  Phoen.-Heb. mdldt,  ‘he  escaped’.
22700-Derivatives:  Malt-ese,  adj.  and  n.
22701-maltase,  n.,  an  enzyme  that  changes  maltose  into dextrose  ( bioehem .)  —  Coined  fr.  malt  and  -ase.
--- KLN ^mild,
23878:mild,  adj.  —  ME.  milde,  mild,  fr.  OE.  milde,  rel. to  OS.  mildi,  ON.  mildr,  OFris.  milde,  Du.  mild, OHG.  milti,  MHG.  milte,  milde,  G.  milde, Goth,  mildeis,  ‘mild’,  and  cogn.  withGk.  paXIb), mixture  of  wax  and  pitch,  ixaXflcov,  ‘weakling’, [zaXffixxo;,  ‘soft’,  [zakflaocreiv,  [zaXOodvciv  ‘to soften',  and  prob.  also  with  OI.  mardhati,  ‘leaves behind,  neglects’,  fr.  I.-E.  *mel-dh-,  enlargement of  base  *mel-,  ‘to  rub,  grind’.  See  meal,  ‘edible grain’,  and  cp.  maltha,  and  the  first  element  in Mildred.  Derivatives:  mild-ly,  adv.,  mild- ness,  n.
23879-mildew,  n.  —  ME.,  fr.  OE.  meledeaw,  mildeaw, ‘honeydew,  nectar’,  rel.  to  OS.  milidou,  Swed. mjoldagg,  Du.  meeldauw,  OHG.  milituo,  MHG. miltou,  G.  Meltau,  ‘mildew’.  The  first  element  of these  words  prob.  derives  from  a  blend  of  I.-E. *melit-,  ‘honey’,  and  l.-E.  *mel,  ‘to  grind’:  see mel,  resp.  meal,  ‘edible  grain’.  For  the  second element  see  dew.
23880-Derivatives:  mildew,  tr.  and  intr.  v.,  mildew-er, n.,  mildew-y,  adj.
23881-Mildred,  fem.  PN.  —  Fr.  OE.  Milddryd,  com¬ pounded  of  milde,  ‘mild’,  and  dryd,  ‘power, strength’.  For  the  first  element  see  mild.  The second  element  is  rel.  to  ON.  prudr,  OS.  prup-, ‘power,  strength’,  ON.  pro-ask,  ‘to  ripen,  thrive’, proskr,  ‘strong’,  OHG.  triuwen,  ‘to  bloom, blossom’,  trouwen,  ‘to  grow’,  MHG.  drao, ‘fruit’.
23882-mile,  n.  —  ME.,  fr.  OE.  mil,  pi.  mila,  mile,  fr.  L. milia,  pi.  of  milte,  ‘a  thousand’  (in  .  .  .  milia  pas- suum,  ‘. .  .  thousand  paces’,  i.e.  ‘.  . .  miles’).  L. milte  is  of  uncertain  origin.  It  is  perh.  cogn. with  Gk.  xtkioi,  OI.  sa-hasram,  ‘a  thousand’; see  Walde-Hofmann,  LEW.,  II,  88  s.v.  mille. Cp.  mil,  millennium,  millesimal,  million.  Cp. also  kilo-.
--- KLN ^melt,
23411:melt,  intr.  v.,  to  become  liquid ;  dissolve;  tr.  v.,  to cause  to  melt.  —  ME.  melten,  fr.  OE.  meltan {intr.  v.),  mieltan  (tr.  v.),  rel.  to  ON.  melta,  ‘to digest’,  fr.  I.-E.  base  *meld-,  whence  also  Gk. p£X8civ,  ‘to  melt’,  L.  mollis  (for  *moldwis),  ‘soft, mild’.  See  mollify.
23412-Derivatives:  melt-er,  n.,  melt-ing,  n.,  melt-ing-ly, adv.,  melt-ing-ness,  n.
```


## [2026-09-07T16:18:50.033Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -m1 -A3 \"mutton,  n\" KLN_1966.txt | head -6; echo ---; grep -n -m1 -A3 \"mulch,\" KLN_1966.txt | head -6; echo \"=== SKT ===\"; grep -n -m1 -A3 \"^MUTTON\\|^MULCH\" SKT.txt | head -10; echo \"=== IEC melg ===\"; grep -n -m2 -A6 \"^melg\\|^mel-g\\|^melag\" IEC.txt | head -20"
}
```


### [2026-09-07T16:18:50.129Z] TOOL RESULT

```
24790:mutton,  n.,  the  flesh  of  sheep.  —  ME.  motoun,  fr. OF.  moton,  mutton,  ‘a  ram’  (whence  F.  mouton, ‘sheep’),  fr.  Gaul.  L.  *multdnem,  acc.  of  *multd, ‘sheep’  (whence  also  O Proven?,  motto,  ‘wether’, It.  montone,  ‘a  sheep’),  which  is  of  Celtic  origin. Cp.  Gael,  mult,  Mir.  molt,  W.  mollt,  MBret. mout,  Bret,  maul,  ‘wether’.  Cp.  also  moutonne. Derivative:  mutton-y,  adj. mutual,  adj.,  joint,  reciprocal,  done  in  common. —  ME.  mutuall,  fr.  MF.  (=  F.)  mutuel,  fr.  L. mutuus,  ‘borrowed,  lent;  reciprocal,  mutual’, which  stands  for  *moitvos  and  is  rel.  to  L.  mu- tare,  ‘to  change’.  See  mutable  and  adj.  suft'.  -al. Derivatives:  mutual-ism,  n.,  mutual-ity,  n.,  mu- tual-ize,  v.,  mutual-iz-ation,  n.,  mutual-ly,  adv. mutule,  n.,  an  ornamental  block  projecting  under the  corona  of  the  cornice  of  the  Doric  order (i archit .)  —  F.,  fr.  L.  mutulus,  ‘mutule,  modil- lion',  which  is  prob.  of  Etruscan  origin  and  lit. means  ‘something  projecting’,  from  the  Etrus¬ can  base  *mut-,  ‘to  project',  which  appears  in many  geographical  names  (e.g.  in  the  name  of the  town  Mutena  (now  Modena).  Cp.  modillion. muzhik,  also  moujik,  n.,  a  Russian  peasant. Russ,  muzhik,  lit.  ‘a  little  man’,  dimin.  of  muzh, ‘man,  husband’,  fr.  ORuss.  muzi,  fr.  OSlav. mgzi,  ‘man’,  which  is  cogn.  with  OI.  manuh, Goth,  manna ,  OE.  man ,  ‘man  ;  see  man.  Peas¬ ants  were  called  ‘little  men  ,  because  according to  the  ancient  Russian  law,  peasants  were  re¬ garded  as  minors.
24791-muzzle,  n.,  the  projecting  part  of  the  head  of  an animal;  snout.  —  ME.  muselt,  fr.  OF.  musel  (F. museau),  fr.  ML.  musellum,  dimin.  of  musum, ’muzzle,  snout',  whence  It.  muso,  OProven?. mus,  of  s.m.;  of  unknown  origin.  Cp.  muse. Derivatives:  muzzle,  tr.  v.,  muzzt-er,  n. muzzy,  adj.,  confused;  dazed.  —  Of  unknown origin.
24792-Derivatives:  muzzi-ly,  adv.,  muzzi-ness,  n. my,  possessive  pron.  of  the  1st  person  sing.,  of me,  mine.  —  Early  ME.  mi,  short  for  min ,  fr. OE.  min,  ‘my,  of  me’.  The  final  n  was  dropped in  ME.  before  words  beginning  with  consonants. See  mine,  pron.  For  the  loss  of  the  n  before consonants  cp.  thy  and  a,  form  of  the  indef.  art. an  before  consonants, my-,  form  of  myo-  before  a  vowel, myalgia,  n.,  muscular  pain  ( med .)  —  Coined  on the  analogy  of  neuralgia  fr.  Gk.  pu?,  ‘muscle  , and  aXyo 5,  ‘pain’.  See  myo-  and  -algia. Derivative:  myalg-ic,  adj.
24793-Mya,  n.,  a  genus  of  bivalves,  the  common  long clam  (zool.)  —  L.  mya,  ‘a  kind  of  mussel’,  fr. Gk.  pdoc,  which  is  rel.  to  pm?,  gen.  puo?, ‘muscle’.  See  mussel  and  cp.  muscle, myalism,  n.,  a  kind  of  Negro  witchcraft  in  West India.  —  Prob.  formed  from  a  native  word with  suff.  -ism.
---
23234:sense  development  cp.  Rum.  tandr,  young  ,  fr- L.  tener,  ‘soft,  tender’),  OPruss.  maldaisin  (acc.), ‘youngest’,  maldian,  ‘foal’,  OSlav.  mladu,  Russ. molodH,  ‘young’,  OE.  meltan,  mieltan,  ‘to  melt', prob.  also  OIr.  meldach,  ‘pleasant’.  From  base *mel-dh-,  a  -^-enlargement  of  base  *mel-,  de¬ rive  Gk.  paXffaxo?,  ‘soft’,  OE.  melde,  OS. maldia,  OHG.  melta,  molta,  multa,  MHG.,  G. melde,  ‘orach’,  Goth,  mildeis,  OE.  milde,  mild  . (OIr.  meldach  and  the  Balto-Slav.  words  cited above  as  derivatives  of  base  *mel-d-,  could  also be  derived  from  base  *mel-dh-.)  Cp.  amalgam, Amalthaea,  ambly,  blenno-,  blite,  emollient, emolument,  immolate.  Maelstrom,  malaco-  ma¬ lax,  malt,  meldometer,  mellow,  melt,  ‘to  dissolve’, mild,  mildew,  mill,  millet,  milt,  moil,  molar, ‘grinding’,  mold,  ‘soil’,  mole,  ‘false  conception’, molinary,  mollify,  Mollugo,  mollusk,  mouille, moulin,  mulch,  muliebrity,  mull,  ‘to  powder’, mull,  ‘a  snuff  box’,  mullein,  muller,  mullet,  ‘star’, multure,  mylo-,  ormolu.
23235-Derivatives:  meal-y,  adj.,  meal-i-ness,  n. meal,  n.,  food  taken  at  one  time.  —  ME.  mele,  fr. OE.  mil,  ‘mark,  sign ;  measure;  fixed  time;  time for  taking  food,  meal’,  rel.  to  ON.  mal,  ‘meas¬ ure,  time,  meal’,  OFris.  mel(tid),  (time  of) meal’,  Du.  maal,  ‘time;  meal’,  OHG.,  MHG-. mal,  ‘time;  meal',  G.  Mal,  ‘time’,  Mahl,  meal  , Goth,  mel,  ‘time;  hour’,  fr.  I.-E.  base  *me-,  to measure’.  See  meter,  ‘poetical  rhythm  . Derivative:  meal,  tr.  v.,  to  have  a  meal.
23236--meal,  suff.  denoting  quantity  taken  at  one  time; now  used  only  in  piecemeal.  —  ME.  -mele,  fr. OE.  -mxlum,  dat.  pi.  of  OE.  mil,  ‘measure’. See  meal,  ‘food’.
23237-mealie,  n.,  maize.  —  S.  Afr.  Du.  milje,  fr.  Port.
=== SKT ===
=== IEC melg ===
10548:melgos, à, is ‘milk; milky sap, latex’. Cf. melgo, mlgó. WP II, 299 Tokh. A malke ‘milk’; W cf. ar-mael, m. “se- cond milk; Go. miluks, f., MHG milich, milch, OE meolc, Du. melk, f. id. beside MHG mëlch, adj. ‘milch, in milk; OE meolc, id.; LG cf. melk, f. (roe; ON mjólk, f. ‘milk’; OCS cf. mlézivo, Cz. mlezivo *beestings, first milk’; Big. cf. mlez-gà beside mlaz-gà ‘sap, latex’. (For Arm. mec, Lat soot? see smel$&-)
10549-melétis (variant of mel£os, etc.) ‘milk’. (Cel-
10550-721
10551-tic: *mléti-) Olr. blicht, m., Ir. bliocht, bleacht, f. id.; W blith, pl. -ion, m. “milk; milch’; ON mjalt-, cpds. ‘milch’
10552-(meli (1) see melit)
10553-meli (2), (meliom, melinà) ‘millet Gk. cf. melíne, f. id.; Alb. mel, m. id.; Rum. (substrate or fr. Lat.) meiu, id.; Lat. milium, n. id.; OBr. mell, Br. mell, m. id. (not a LW’. J. Loth); ON melr, mod. melur, m. (1) “lyme- grass
10554-(mélinos, à (1) *honey-coloured'; (2) *dark, stained, blue’. (1) due to influence of melit, q.v., (2) due to influence of mēl- (1), q.v.). WP II, 293 (1) Gaul. melinus, OBr. milin-, Br. mélen, W melyn, Cor. melen *honey-coloured, yellow’. But Lat. mēlinus ‘yellow’, a LW from Gk. mé- linos "of a quince, yellowish’ is fr. *mal- in view of Aeol. Boeot. màlinos; (2) Li. mélynas “blue”, beside mélas, id.
```


## [2026-09-07T16:19:03.506Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC melgo ===\"; grep -n -m3 \"^melgo\\|^mlgó\\|^melg\" IEC.txt | head; sed -n '10540,10548p' IEC.txt; echo \"=== IEC meldus soft ===\"; grep -n -m4 \"^meldus\\|^meldos\\|^mldus\\|^melakos\" IEC.txt | head"
}
```


### [2026-09-07T16:19:03.604Z] TOOL RESULT

```
=== IEC melgo ===
10548:melgos, à, is ‘milk; milky sap, latex’. Cf. melgo, mlgó. WP II, 299 Tokh. A malke ‘milk’; W cf. ar-mael, m. “se- cond milk; Go. miluks, f., MHG milich, milch, OE meolc, Du. melk, f. id. beside MHG mëlch, adj. ‘milch, in milk; OE meolc, id.; LG cf. melk, f. (roe; ON mjólk, f. ‘milk’; OCS cf. mlézivo, Cz. mlezivo *beestings, first milk’; Big. cf. mlez-gà beside mlaz-gà ‘sap, latex’. (For Arm. mec, Lat soot? see smel$&-)
35
40
45
750
meles- ‘sweet; sweetness’. Cf. melit, etc. Ir. milis, f. milse, adj. ‘sweet’; milse, f. *sweet- ness’; Li. melisa, f. “nectary”
meleuos, à (melouo-) (1) *millings, flour”. WP II, 286 Myc. cf. meleuro-, id.; Alb. miell, m. id.; W cf. mål, m. *millings; OHG mélo, gs mélawes, n. ‘flour; MHG mél, gs wes n. “flour, dust, powder, slaked lime’; OE melu, gs melwes, n. ‘meal; ON mol ds mjolvi, n. id.; Sw. mjöl, n. id.; OR melevo *millings'; Srb. cf. mlivo (flour. Phonol?); Li. máliava, f. as OR
meleuos (melouos, meluos) (2) “soft, effete, silly. Cf. WP IL, 284 & 291 Skt. malváh ‘foolish’; Arm. molor, molar, gs -i, ab. s. -av, and moli; gs moluo, ab. s. moleav ‘mad, erroneous, false’; Gk. méleos ‘foolish, wretched'; Ir. cf. mealbh-ach ‘sweet, honey- ed; ME melwe ‘mellow’
melĝð ‘caress, titillate, massage, milk’. Cf. ml£o and next. WP II, 298 Skt. cf. (z-gde) mrjámi ‘wipe; Av. marozai- (mi), id.; Tokh. AB malk-, v. ‘milk’; Gk. mélgo “massage, handle’; a-mélgo (*milk', fr. em": Thr. melg-, Illyr. mei. id.; Alb. mjel, aor: mola, id.; Lat. cf. (z-gde) mulgeo, id.; Olr. mligim, MIr. bligim, mod. bleaghaim, v. id. (z-gde as Lat.); W cf. ar-mael, m. ‘second milk; MHG mélken, mélchen, sv. 3 “milk; be in milk’; OE melcan, sv. 3. ‘milk’ beside (o-gde) melcian ‘milk; suckle’; ON mjólka, v. “milk; be in milk’; Du. melken, id.; OCS (z- gde) mlüzo, mlésti, id.; Li. mélZiu, -ti and (z- gde) inf. milZti, id. (The semantic association of ‘wipe’ and “milk? is apparent in Latvian Slauku, slaucit, v. ‘wipe’; slaucu, slaukt, v. “milk?). Cf. melgos, molg- and mlé-.
melgos, à, is ‘milk; milky sap, latex’. Cf. melgo, mlgó. WP II, 299 Tokh. A malke ‘milk’; W cf. ar-mael, m. “se- cond milk; Go. miluks, f., MHG milich, milch, OE meolc, Du. melk, f. id. beside MHG mëlch, adj. ‘milch, in milk; OE meolc, id.; LG cf. melk, f. (roe; ON mjólk, f. ‘milk’; OCS cf. mlézivo, Cz. mlezivo *beestings, first milk’; Big. cf. mlez-gà beside mlaz-gà ‘sap, latex’. (For Arm. mec, Lat soot? see smel$&-)
=== IEC meldus soft ===
```


## [2026-09-07T16:19:04.579Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD band3 index mel ===\"; grep -n \"melg\\|mel-d\\|mel-dh\" WLD_band3.txt | head -15; echo \"=== WLD Bd2 melg ===\"; grep -n \"abstreifen, wischen\\|melken\" incoming/WLD/WLD_Bd2_pages.txt | head -10"
}
```


### [2026-09-07T16:19:04.645Z] TOOL RESULT

```
=== WLD band3 index mel ===
=== WLD Bd2 melg ===
19658:inelg- „abstreifen, wischen^^, europ. „melkeii“.
19682:„abgewischt“) „melken% mulctra ,Melkkubel'^\ ir. lligim „ich melke‘^"(aus
19688:   ahd. milcitu, inelchan, ags. meJcan „melken'' (st. Y. dagegen ags. meol-  ;
19695:moJka „melken“ (= ai. mrjdti), mylkja ,,saugen‘‘.
19704:AnschluB an melken glaubt Hirt IF. 21, 173: 22, 97 Anm. 1 ; Idg. 665,
19726:  Die europ. Bed. „melken“ ist aus „die Milch herausstreifen, abstreifen‘*
21519:Milch" (py^ja „melken"), ags. nytt f., mnd. nutte, 7iuf ..‘N’utzen", ahd. nuz.
```


## [2026-09-07T16:19:16.395Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && grep -n \"\\[pdf page\" WLD_Bd2_pages.txt | awk -F: '$1<19658' | tail -2; echo ===; sed -n '19655,19662p' WLD_Bd2_pages.txt; echo \"=== mel- weich in Bd2 ===\"; grep -n \"zermalmen, schlagen, mahlen\\|fein, zart, weich\" WLD_Bd2_pages.txt | head -5"
}
```


### [2026-09-07T16:19:17.862Z] TOOL RESULT

```
Exit code 1
(eval):1: == not found
```


## [2026-09-07T16:19:21.408Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && grep -n \"pdf page\" WLD_Bd2_pages.txt | awk -F: '$1<19658' | tail -2; echo \"----\"; grep -n \"zermalmen, schlagen, mahlen\" WLD_Bd2_pages.txt | head -3"
}
```


### [2026-09-07T16:19:22.856Z] TOOL RESULT

```
----
```


## [2026-09-07T16:19:27.166Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && head -19658 WLD_Bd2_pages.txt | tr -cd '\\f' | wc -c; echo \"--- mel weich\"; grep -n \"mel-, smel-\\|1. mel-\\|,zermalmen\" WLD_Bd2_pages.txt | head -6"
}
```


### [2026-09-07T16:19:27.239Z] TOOL RESULT

```
302
--- mel weich
```


## [2026-09-07T16:19:36.131Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && awk 'BEGIN{RS=\"\\f\"} NR==290' WLD_Bd2_pages.txt | head -12; echo \"===== leaf 295 (p.290?) =====\"; awk 'BEGIN{RS=\"\\f\"} NR==295' WLD_Bd2_pages.txt | grep -n -i \"weich\\|mollis\\|malakos\\|malthakos\" | head -8"
}
```


### [2026-09-07T16:19:37.572Z] TOOL RESULT

```
                                                                                                                 ;




                                                          mel-                                                 285

(„*schwach‘^ in geistigem Sinne: vgl. Uhlenbeck Ai.Wb, 219,                                  Lewy IF. 32,
164 m. Lit., Persson Beitr. 209 f.; got. gamalwjan, ahd. molawen, lit, mcd-
vinti). Von der ?*Basis wohl ai. mrityati j,zerfallt, lost sich auP (vgl. ^Xhov,
Persson Beitr. 213, und skr. mlitafi, Berneker 1165); bei Verb, des ai.
Wortes mit mer- „aufreiben“ feblten wenigstens entsprechende
===== leaf 295 (p.290?) =====
11:mela-q' in der Bed. „weich, schwach, matt, albern*'.
12:   Gr. juakaxog „weicli“       -xog „8clilaff, trage, weichlich, t6riclit‘‘, plaxevco
20:weicht in der Bed. zu weit ab).
31:(air. melen d. i. mien) „Die Weichen‘‘      ^mlakna (Fick II ^ 221, cymr.
59:„weich“, mulscJien mdartl. „sch]afen“ (Holthausen IP, 32, 335) vgl. Persson
```


## [2026-09-07T16:19:47.214Z] TOOL CALL #63: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/amalgam",
 "prompt": "Full etymology of \"amalgam\", including the Arabic al-malgham and Greek malagma chain, dates, and any alternative theories."
}
```


## [2026-09-07T16:19:49.355Z] TOOL CALL #64: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82mel%C7%B5-",
 "prompt": "What does this page say: reconstruction, meaning, descendants (Latin mulgere, Germanic *melkan, Greek amelgein, Avestan), and does it mention 'wipe off'?"
}
```


### [2026-09-07T16:19:54.234Z] TOOL RESULT

```
# Etymology of Amalgam

The word **amalgam** has a fascinating etymological journey spanning multiple languages and cultures.

## Origin Timeline

The English noun "amalgam" emerged around 1400, initially describing "a blend of mercury with another metal; soft mass formed by chemical manipulation." It derives from Old French *amalgame* or Medieval Latin *amalgama*, terms used by alchemists around 1300.

## Arabic and Greek Roots

The Medieval Latin term likely originated from Arabic *al-malgham*, meaning "an emollient poultice or unguent for sores (especially warm)." This Arabic word may itself stem from Greek *malagma*, defined as a "softening substance," which traces back to *malassein* ("to soften") and *malakos* ("soft").

## Proto-Indo-European Connection

The ultimate root is Proto-Indo-European *\*meldh-*, connected to the root *\*mel-* (1) meaning "soft." This foundational sense of softness links amalgam to numerous English words including melt, mild, mollify, and mollusk.

## Figurative Expansion

The figurative meaning—"compound of different things"—emerged much later, around 1790, extending the metallurgical concept to describe any blended mixture of disparate elements.
```


### [2026-09-07T16:19:54.904Z] TOOL RESULT

```
# Summary of the Page Content

**Reconstruction:** The page documents *h₂melǵ-, a reconstructed Proto-Indo-European root.

**Meaning:** The root has two related definitions: "to milk" (verb) and "milk" (noun).

**Descendants:** The page lists several language families with descendant terms:
- Latin: "mulgeō" ("I milk")
- Proto-Germanic: *melkaz and *meluks
- Proto-Celtic: *mlixtus, with Old Irish mlicht
- Tocharian A and B: malke/malkwer ("milk")
- Balto-Slavic forms like Latvian malks

**'Wipe off' mention:** No, the page does not mention "wipe off." The documented meanings relate exclusively to milking and milk as a substance.
```


## [2026-09-07T16:20:02.582Z] TOOL CALL #65: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82mer%C7%B5-",
 "prompt": "Reconstruction, meaning, and descendants of this root (Greek amergo, Sanskrit mrj-, Proto-Iranian *Hmarz, Latin mergae). Does it mention Persian malidan?"
}
```


## [2026-09-07T16:20:04.037Z] TOOL CALL #66: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%D9%84%D8%BA%D9%85",
 "prompt": "Give all language sections for ملغم (Arabic and Persian): meanings and etymologies, especially any mention of Greek malagma or Syriac."
}
```


### [2026-09-07T16:20:04.741Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-07T16:20:09.712Z] TOOL RESULT

```
# Arabic Section for ملغم

**Etymology:** The word originates from Ancient Greek. Specifically, it derives from "μάλαγμα (málagma, 'emollient; malleable material')," which connects to related Greek terms meaning "to soften" and "soft."

**Meanings:**
1. A softening ointment or emollient poultice
2. An amalgam (metal alloy)

**Note:** The page shows only the Arabic entry. While the header indicates three languages (Persian, Hungarian, and Dutch) have entries for this term, the provided content displays exclusively the Arabic section. The Persian and other language sections are not included in the webpage excerpt supplied.
```


## [2026-09-07T16:20:15.563Z] TOOL CALL #67: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/Hmarz",
 "prompt": "Reconstruction, meaning, PIE ancestor, and descendants (Avestan, Middle Persian, Persian) of Proto-Iranian *Hmarz."
}
```


## [2026-09-07T16:20:16.980Z] TOOL CALL #68: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%81%D8%B1%D8%A7%D9%85%D8%B1%D8%B2",
 "prompt": "Give the Persian entry for فرامرز: meaning and etymology (Middle Persian, Avestan components)."
}
```


### [2026-09-07T16:20:17.259Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-07T16:20:18.519Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-07T16:20:21.868Z] TOOL CALL #69: WebSearch

```json
{
 "query": "Farāmarz etymology name \"one who forgives\" Avestan marz Shahnameh Justi Iranisches Namenbuch"
}
```


## [2026-09-07T16:20:23.630Z] TOOL CALL #70: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A2%D9%85%D8%B1%D8%B2%DB%8C%D8%AF%D9%86",
 "prompt": "Persian آمرزیدن: meaning and etymology (Middle Persian āmurzīdan, Avestan mərəzd-, Proto-Iranian)."
}
```


### [2026-09-07T16:20:28.277Z] TOOL RESULT

```
Web search results for query: "Farāmarz etymology name "one who forgives" Avestan marz Shahnameh Justi Iranisches Namenbuch"

Links: [{"title":"Faramarz - Islamic Name Meaning - Baby Names for Muslims","url":"https://quranicnames.com/faramarz/"},{"title":"Submitted Names in Afghanistan (page 2) - Behind the Name","url":"https://www.behindthename.com/submit/names/place/afghanistan/2"},{"title":"Persian Mythology Submitted Names - Behind the Name","url":"https://www.behindthename.com/submit/names/usage/persian-mythology"},{"title":"Persian Submitted Names (page 2) - Behind the Name","url":"https://www.behindthename.com/submit/names/usage/persian/2"},{"title":"Faramarz (disambiguation)","url":"https://en.wikipedia.org/wiki/Faramarz_(disambiguation)"},{"title":"Faramarz","url":"https://en.wikipedia.org/wiki/Faramarz"},{"title":"Meaning of the name Faramarz","url":"https://www.wisdomlib.org/names/faramarz"},{"title":"Shahrn%C4%81z","url":"https://en.wikipedia.org/wiki/Shahrn%C4%81z"},{"title":"Faramarz (given name)","url":"https://en.wikipedia.org/wiki/Faramarz_(given_name)"},{"title":"Fariborz","url":"https://en.wikipedia.org/wiki/Fariborz"}]

Based on the web search results, I found information about the etymology of Farāmarz:

Faramarz means "one who forgives" from Persian āmorzidan meaning "to forgive". This is the name of a hero in the Persian epic Shahnameh. He was the son of Rostam.

However, the search results do not contain specific information about the Avestan etymology of "marz," the references to Justi's *Iranisches Namenbuch*, or detailed etymological analysis connecting the name to Avestan roots as mentioned in your query. The sources I found focus on the Persian meaning of the name but don't provide the scholarly etymological references you're asking about. You may need to consult specialized academic sources on Iranian language and names to find that level of detailed etymological analysis.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-07T16:20:29.289Z] TOOL RESULT

```
# آمرزیدن (Âmorzidan)

**Definition:** This Persian verb means "to forgive."

**Etymology:** The word derives from Middle Persian *āmurzīdan*, ultimately tracing back to Proto-Indo-Iranian *\*mr̥žd-* meaning "to forgive, spare, to pity."

**Related Languages:** The term has cognates in Avestan (*mərəžd-*), Parthian, and Sanskrit (*mṛḍati*), reflecting a shared Indo-Iranian linguistic heritage.

**Synonyms:** In Persian, similar terms include *baxšidan* and *baxšâyidan*.
```


## [2026-09-07T16:20:36.298Z] TOOL CALL #71: WebFetch

```json
{
 "url": "https://en.wikipedia.org/wiki/Faramarz_(given_name)",
 "prompt": "What does the page say about the meaning and etymology of the name Faramarz?"
}
```


## [2026-09-07T16:20:37.341Z] TOOL CALL #72: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/mutton",
 "prompt": "Etymology of mutton: Old French moton, Medieval Latin multonem, Celtic origin? Any note on the PIE root?"
}
```


### [2026-09-07T16:20:39.245Z] TOOL RESULT

```
Based on the Wikipedia page provided, there is **no information about the meaning or etymology of the name Faramarz**. 

The page only states that "**Faramarz** (Persian: فرامرز) is a Persian masculine given name" and then lists notable people who share this name. It does not explain what the name means or its etymological origins.
```


### [2026-09-07T16:20:43.216Z] TOOL RESULT

```
# Etymology of Mutton

Based on the Online Etymology Dictionary entry, here's the etymological pathway:

**Origin Chain:**
The word traveled from Celtic languages through Medieval Latin into Old French and then into Middle English. Specifically: "from Old French _moton_...from Medieval Latin _multonem_ (8c.), probably from Gallo-Roman _\*multo-s_, accusative of Celtic _\*multo_"

**Celtic Connection:**
The Celtic root appears across multiple languages, including "Old Irish _molt_ 'wether,' Mid-Breton _mout_, Welsh _mollt_"

**PIE Root:**
The dictionary notes this Celtic term "is perhaps from PIE root _\*mel-_ (1) 'soft.'"

The entry indicates some uncertainty about the ultimate origin, using "perhaps" and "probably" to qualify the prehistoric connections. The most concrete evidence traces back to Celtic languages, with the Proto-Indo-European connection being more speculative based on semantic similarity.
```


## [2026-09-07T16:20:53.323Z] TOOL CALL #73: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://www.etymonline.com/word/amalgam' --note 'page 330, root Mel 3, amalgam chain Arabic al-malgham < Gk malagma' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82mel%C7%B5-' --note 'page 330, root Melg, modern PIE *h2melg- to milk (no wipe sense, no Indo-Iranian)' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D9%85%D9%84%D8%BA%D9%85' --note 'page 330 node 2/3, Arabic malgham < Gk malagma' 2>&1 | tail -3"
}
```


### [2026-09-07T16:20:55.838Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/c2ab61cbb80fefe4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8e20c4f4ef737cfd.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0e6dcc2ce56fbd33.txt
```


## [2026-09-07T16:20:57.615Z] TOOL CALL #74: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D9%85%D8%A7%D9%84%DB%8C%D8%AF%D9%86' --note 'page 330 node 2, Persian malidan < MP malidan < PIr *Hmarz' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%A2%D9%85%D8%B1%D8%B2%DB%8C%D8%AF%D9%86' --note 'page 330 node 4, Persian amorzidan < MP amurzidan < PIIr *mrzd-' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://www.etymonline.com/word/mutton' --note 'page 330 nodes 10-11, mutton < OFr moton < Celtic *multo, perhaps PIE *mel- soft' 2>&1 | tail -3"
}
```


### [2026-09-07T16:21:00.177Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/551db37a15a60b2d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1ea32cfb616d6f8f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/69ad5d327d9c7492.txt
```


## [2026-09-07T16:21:07.445Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"marz\\|malitan\\|must\" SNS_pages.txt | head -10"
}
```


### [2026-09-07T16:21:07.491Z] TOOL RESULT

```
848:Herzfeld, E.:          Khareghat Memorial volume, Bombay                                                         Framarz and others. Their Version with In-
2921:                                                                                                                      *o-i*-l'4 :marz / mar^z + a <^r**  £-
8782:cu-U^T -*o^-tf »9^Uw">>»lt .J»I>J«^.a^: kunmarz:                               W«3
9654:                              lt4>iji-^A      j*tf« Jj^. marz§d:
9667:       .«W'o*/tfjs -^ .ja— ^.i marzisn: mrzysn:^
```


## [2026-09-07T16:21:12.528Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -9667 SNS_pages.txt | tr -cd '\\f' | wc -c; sed -n '9650,9672p' SNS_pages.txt"
}
```


### [2026-09-07T16:21:12.622Z] TOOL RESULT

```
139
                                                                                                                                  l/TT^ «jar^ (ji4- imihtar:
                                                                                                                                            *
                                                                                                                                                                             ^
                                                                                                              SJ          -l,*patiy + /-grab
                              lt4>iji-^A      j*tf« Jj^. marz§d:
                                                                                                                         TI/V.J ..f^a^j
                                                                                                                                                          :jlj,
                                                                                                                                                                   Wi/iV
               Aarj           *#**>(*'       i^iarz: >1            maraza-: b.                                                              padlraftan
 marsti,                  :
                                                                                                                                                                         :
                                                                                                                                                                             {,

                                   .o-l^yj0^J *0'VJ "J U
                                                                                                                                V*« padlr, MKBLWN:                  ,^
(GJVPE. 214      >!£*/£>. 1153)

       .«W'o*/tfjs -^ .ja— ^.i marzisn: mrzysn:^
                                                           1
```


## [2026-09-07T16:22:05.207Z] TOOL CALL #77: Bash

```json
{
 "command": "sed -n '1,200p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-07T16:22:05.243Z] TOOL RESULT

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


## [2026-09-07T16:22:10.889Z] TOOL CALL #78: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg330.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/330.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | head"
}
```


### [2026-09-07T16:22:10.962Z] TOOL RESULT

```
total 15196
drwxrwxr-x  2 sfmqrb sfmqrb   4096 Sep  7 12:22 .
drwxrwxr-x 12 sfmqrb sfmqrb   4096 Sep  6 18:36 ..
-rw-rw-r--  1 sfmqrb sfmqrb  71589 Sep  5 10:46 100.png
-rw-rw-r--  1 sfmqrb sfmqrb 104864 Sep  4 19:03 101.png
-rw-rw-r--  1 sfmqrb sfmqrb  68145 Sep  5 10:49 102.png
-rw-rw-r--  1 sfmqrb sfmqrb  79623 Sep  5 10:55 103.png
-rw-rw-r--  1 sfmqrb sfmqrb  78826 Sep  5 10:59 104.png
-rw-rw-r--  1 sfmqrb sfmqrb  82500 Sep  5 11:05 105.png
-rw-rw-r--  1 sfmqrb sfmqrb  55270 Sep  5 11:03 106.png
```


## [2026-09-07T16:22:49.163Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LKT amalgam ===\"; grep -n -i \"malgham\\|amalgam\\|malagma\" LKT.txt | head -5; echo \"=== AFA ===\"; grep -n -i \"malagma\\|ملغم\" AFA.txt | head -5; echo \"=== AFM ===\"; grep -n \"ملغم\" AFM_pages.txt AFM.txt 2>/dev/null | head -5; echo \"=== BQT malgham ===\"; grep -n \"ملغم\" BQT_v1_pages.txt BQT_v2_pages.txt incoming/BQT/BQT_v3_pages.txt incoming/BQT/BQT_v4_pages.txt 2>/dev/null | head -5; echo \"=== PHN/DEV amalgame ===\"; grep -n -i \"amalgam\" PHN.txt DEV.txt 2>/dev/null | head -5"
}
```


### [2026-09-07T16:22:49.288Z] TOOL RESULT

```
=== LKT amalgam ===
3186:1378.  Ar.  malgaiu: 'Erweichende  Salbe'  [aus  gr.  |id\aY|ua mit  Metathesis];  hieraus  sp.  pg.  kat. amalgama,  frz.  amalgame;  engl,  aniaf- gam,  Vb.  amalgamate,  dtsch.  Amalgam, Vb.  amalgamieren;  russ.  amal'gama [und  über  tk.  melhem,  ebenso  tat.]  mal  - han,  bulg.  mehlem,  serb.  meiern  'Saloe'.
5709:St.  75 Amalgam  1378 arnalgamieren  1378 Atnber  78 Amen  68 .4»iocA:  71 Amulett  866 Anakonda  74 Anatolien  76 angeschickert  j.  1787  b Anilin  1568 Antimon  918 Aprikose  247 Araber  89  c Arabeske  89  d v4r/rfftf  St.  1719 .4r?V>-  112 ^riojoTi  St.  1719 ^rnujii«?  104 ^rrai;  92 Arschitie  108 ^rsewa^  495 Artischocke  833 Asangue  St.  392 Äschere  St.  1915 Aschkenasi  120 A  schlauch  119 Assegai  2181 I  ^toir  St.  1574
6339:alphanette  582 alphinic  683 alquifoux  1227 aludel  2142 alvarde  242 amalgame  1378 aman  66 amhre  78 amhrette  762  b nmiral  69  a amire  afz.  69  a amuUte  866 amulette  866 anafin  1537 andouille  355 angrec  82 «wii  1568 <iw<t/f(;  20ö8 antimoine  918 arabe(sque)  89 «ra^  92 arcawne  867 archine  108 argali  96 argousin  2160 aWeie  100 ar»m  112 armadie  1343 armoise(ur)  1596 armo(i)sin  1596 «rra^e?  1708 arrofee  1725 arsenal  495 artichaut  833 ar^iei  95 assassin  839 assogue  2208 »thanor  2019 a^fcar  2075 a«a6a?  1971 ffM&^e  874 aubergine  161 «MCTtöe  afz.  1221 uufage  afz.  586.  777 auferrant  afz.  586 aw/fe  796 au^n  afz.  605 auforget  884 «M^r^  135
7269:alinogaden  1504 i  almogaver  1496 1  almoixe}-if  1519 I  aZwM<  149Ü i  amalgama  1378 *  amoscarse  1436
9972:almojarife  1519 almojarra  1439 almojatre  1581 alnirineda  1511 almoraduj  1411 ahnotacen  1503 almozal(l)a  1511  a almucio  1520 almud  1490 almuecin  1485 almuidano  1485 aloque(ro)  803 aloqueria  803 alpargata  243 alpicoz  576 alquequenge  1016 alqueria  1096 alquez  1174 alquifol  1227 aquilar  1181 alquile(r)  1181 alquhnia  1157 alquitara  1130 alqmtrdn  1128 altramuz  2115 alubia  1333 «Zmc^cZ  2142 aluquete  2153 aZfaci/  2160 amacena  476 amalgama  1378 amapola  762  d amargaza  829 amarillo  70 mnbar  78 amoscarse  1436 amuco  71 amtileto  866 amusco  1515  a anacal(o)  1545 anadel  1566 «w«/?/  1537 anafre  130 anatron  1567 anazea  1583 andamio  520 annafe  130 ante(ado)  1305 antimonio  918 anzarote  86 afiacal  1545 anacea  1583 anaciar  1583 anafil  1537 öw«7  1568 «/Itr  1568 arac  92 arambel  811 arancel  1428 arfceZW  dial.  204 arhollön  204 arcaditz  988
=== AFA ===
=== AFM ===
=== BQT malgham ===
incoming/BQT/BQT_v4_pages.txt:4549:۱ - همین صورت‌اخی رسحیح بنظرمیآ ید - ملغم وملفمه عربی‌ظاهرا ازیونانی 13281287708
incoming/BQT/BQT_v4_pages.txt:4572:ملفم و ملغمه - رك :+ ملم ۰
=== PHN/DEV amalgame ===
DEV.txt:489:Amalgame.  Ce  mot  nous  est  venu  par  les  alchimistes  avec le  sens  de  mélange  intime,  combinaison,  spécialement  en ce  qui  regarde  le  mercure.  Je  n'en  connais  pas  d'exemple avant  le  xiif  siècle;  mais  il  est  à  cette  époque  d'un  usage constant.  Ainsi  dans  la  Semita  recta  Albertimagni  :  c^Deinde recipe  plumbi  et  slagni  calcinatorum  et  in  corpus  reducto- rum;  fiant  unum  corpus  perfusionem  simul  :  et  si  sunt  dua^ librar,  adde  argenti  vivi  libram  i,  et  amalgama,  et  lava cum  sale  et  aceto,  et  sicca^.  w  Dans  le  Parvum  Rosarium  Ar- nalcli  de  Villa  nova:  r^Et  cum  totum  dissolvetur  et  in  mer- curium  reducetur  et  fiet  unum  amalgama '^  ^-i  ;  ce  Et  cum totum  fuerit  dissolutum  et  in  amalgama  positum^.  »  Ail-
DEV.txt:496:leurs  :  :^Fac  tuum  amalgama;  pono  luum  amalgama  snj)ra iinum  pulchrum  folium  papy  ri  ^ ,  etc.  •>)
DEV.txt:497:Outre  la  forme  amalgame,  Lacurne  cite  algamc,  mixtion d'or  et  de  mercure.  Dans  cette  dernière ,  il  semble  qu'on doive  reconnaître  l'arabe  iix^i^  al-djam'a,  conjonction . réunion,  ou  ^-^  al-djima  ,  l'acte  de  consommation  du mariage,  venant  tous  deux  de  la  racine  ^.cljama,  réunir. (Cf.  le  grec  ya^xéù),  yotfxos.)  Mais  qu'est-ce  que  amalgame? Faut-il  y  voir,  comme  je  l'ai  suggéré  antérieurement,  l'ex- pression ffjt.^  J^  'amal  al-cljama,  l'œuvre,  la  pratique  de Yalgame  (J^  \imal,  pratique,  se  dit  par  opposition  à  ks- 'ilm,  tliéorie)?  Ou  bien  est-ce  une  altération  de  iùcoLiJî al-modjmna,  qui,  comme  al-cljnmf,  signifie  l'acte  de  consom- mation du  mariage?  Comme  sens,  l'analogie  est  parfaite, car  les  alchimistes  aiment  à  comparer  la  combinaison  du mercure  avec  les  métaux  à  l'union  de  l'époux  avec  l'épouse. Ainsi,  dans  un  traité  intitulé  De  matrimonio  et  conjunctione , le  mercure  i^zaihat)  est  assimilé  au  mari,  l'argent  (/«m/, la  lune)  à  la  femme,  et  l'amalgame  des  deux  corps  est  cé- lébré par  cette  phrase  :  r^Natura  laetatur  quando  sponsus cum  sponsa  copulatur^.  w  Néanmoins,  n'ayant  point  re- cueilli d'exemple  des  expressions  ci-dessus  dans  les  ou- vrages d'alchimie  arabe,  je  n'oserais  affirmer  l'exactitude de  mes  conjectures.
DEV.txt:1774:cadavres  préparés  par  quelques  Juifs  et  Arméniens  qui cherchent  à  tirer  parti  de  tout. .  .  On  emploie  aujourd'hui cette  momie  en  appât  pour  attirer  les  poissons.  55  (Virey^) La  mumic  ou  momie  des  alchimistes  (amalgame  de plomb)  est  le  même  mot.
DEV.txt:2536:Algame,  voy.  Amalgame.
```


## [2026-09-07T16:23:01.493Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && grep -n \"\\[pdf page\" BQT_v4_pages.txt | awk -F: '$1<4549' | tail -1; sed -n '4540,4575p' BQT_v4_pages.txt"
}
```


### [2026-09-07T16:23:03.014Z] TOOL RESULT

```
4535:[pdf page 115]
مالیدن بر افضا را نیز کویند , و در هندوستان بوده مجتهد و ساحب مذهب ترسایان وفقیه ملت
مردن خوانند بفتح میم ودال ؛ و باغین نقطه‌دار | ایشان واورا ملوکا هم میگوبند ۴ - و بلفت زند
هم بنظر آمده است ۱ . و پازند ‎)٩(‏ پادشاء راکوبند 9 .۹
ملك ‏ نم اول وسکون‌انی وکاف,دانه‌ای منك آردی ۹ > بفتح همزه و رای
باشد بز رکه ترازماشی وآنر! پزند وخورندویمربی |[ قرشت بروزن سلك حبشی ‏ کنابه از ملك ابران
جلبان خوانند؟ - وبکسراول, سفیدیی راکوبند | زمین است.
که دربن ناخنها پدیدآید ؛ وبستی کویندتقیلهای ملکان < بروزن مرجان » نام پدر خض
سفید اس ت که برناخن افتد۴ - و درعربی بممنی | علیه‌اللام باشد و او از احفاد سام پن :توح است
() چك : ژند و پاژند.
۱ - همین صورت‌اخی رسحیح بنظرمیآ ید - ملغم وملفمه عربی‌ظاهرا ازیونانی 13281287708
( خمیر کردن ) ماخوذ است. همن‌لفت عربی «* الملقمه» وارد لاتینی (کیمیاگران ) شده صورت
8 در آمده واز آنجا وارد زبان فرانوی‌شده 278281887۷06(امتز اج فلزات) «نداب۳
۶-۳ .و رك : دزی ج اس ۰۵۳۸ ۴ - « ملك , کلول باشد ( چاپ هرن : ملك
دانه‌است چون ماش و از عدس مه باشد. گروهی کاولش خوانند) . بوالمژید (بلخی) کوید :
باکا که ندیم حریره و بره است وب ی کست که سیری نیابد از ملکی.»
* لت فری‌س ۲۵4 ۶ .۰
۳ - « ملك . سپیدی پن ناخن باشد . احمد برمك گفت :
ملك از ناخن همی جدا خواهی کرد دردت کندای دوست . خطا خواهی کرد.»
«لفت فری ص۲۹۷ ۰
۴ - « مل > بفتح اول * ۸12118 ( آرامی ) بمعنی‌پادشاء > ملك ( بقتح اول وکسر
دوم ) عریی است ( رك : حاشیةٌ بند ) و علم ( اسم خاص ) لیست . خاقانی شروانی کوید :
مرا اسقف محفق تر شناسد ز بمقوب و زنطور و زمل -
« دیوان خاقانی شروالی ص ۲۳ .
غاعر درین بیت اشتباه کرده » چه او خواسته است پیشوایان سه فرقةٌ مسیحی بعنی یمقوبره
6 . نطوربه 3769107188 ۰ و مثکائلیه ۸16161468 را نام ببرد ولی پی نبرده بود که
ملکائیه فقط بمعنی ( فرقه ) شاهی ( 70281 ) است » و ربطی بنام موس فرقه ندارد . رك :
,3505 ۰ 0092608 بش۸ فمه تمقوفط۴ روف ما2 ( عیده
مرحوم فزونی نیز پیش از انتشارکتاب مز بور » همین بود) « النصاری مفترقون فرقاً: فالاولی‌منهم
الملکائیه , و هم الروم . وانما سموا بذلك لان ملك الروم علی قولهم و لیس بالروم سواهم ... >
( آثارالبافیهٌ بیرونی چاپ زاخائو ص ۲۸۸). - هز. 268 . ۳۳811082 ۰ پهلوی
8 (عاء) 3 . ۱۱۹ > ورك : حاشیهٌ قبل . ‎٩‏ - ظ. اسح « منك آرشی >
است هتوب و ۰ ۳
ملفم و ملغمه - رك :+ ملم ۰
+ ملکالیه - رك ناه
[pdf page 116]
وت ملنگه
```


## [2026-09-07T16:35:09.592Z] TOOL CALL #81: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/mk330.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nU_AMAL = \"https://www.etymonline.com/word/amalgam\"\nU_MELG = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82mel%C7%B5-\"\nU_MLGM = \"https://en.wiktionary.org/wiki/%D9%85%D9%84%D8%BA%D9%85\"\nU_MALID = \"https://en.wiktionary.org/wiki/%D9%85%D8%A7%D9%84%DB%8C%D8%AF%D9%86\"\nU_AMORZ = \"https://en.wiktionary.org/wiki/%D8%A2%D9%85%D8%B1%D8%B2%DB%8C%D8%AF%D9%86\"\nU_MUTTON = \"https://www.etymonline.com/word/mutton\"\n\ne0 = {\n  \"entry\": 0,\n  \"root\": \"Mel 3\",\n  \"verdict\": \"confirmed\",\n  \"modern_form\": \"PIE *mel-1 'soft; with derivatives referring to soft or softened materials of various kinds' (Watkins/AHD) = Pokorny 1. mel- (pp. 716-719), the 'weich' half of the 'grind, crush' root\",\n  \"note\": \"Pokorny p.716 opens the entry '1. mel- (auch smel-), mels- : mle-, mel-d- : ml-ed-, mel-dh-, ml-ei- : mli-, mela-k- : mla-k-, mleu- : mlu- ‚zermalmen, schlagen, mahlen‘; speziell Korn; aus ‚zerrieben‘ auch ‚fein, zart, weich‘ und ‚aufgerieben, schwach‘' — i.e. the 'soft' sense is expressly a development inside Pokorny's mel-1, and the extensions that carry it (mel-d- p.718 mollis/meltan/malz, mel-dh- p.719 malthakos/milde, mela-k- p.719 malakos, kelt. *molto- p.716f.) are all on pp. 716-719. Watkins/AHD does exactly what Nourai does: it splits the page into 'mel-1. Soft' and 'mele-. To crush, grind', both tagged [Pok. 1. mel- 716]. So the language label (Indo-European), the gloss ('soft, soft material') and the page (POK:716) are all right; only the numbering 'Mel 3' is Nourai's own bookkeeping. Every branch drawn under it (Greek malakos/malagma, Germanic melt/malt/mild/mulch/smelt, Latin mollis, Celtic molto) is in Watkins s.v. mel-1.\",\n  \"note_fa\": \"ریشهٔ هندواروپایی آغازین *mel- که پوکورنی (ص ۷۱۶–۷۱۹) معنای اصلی آن را «ساییدن، آس کردن، کوبیدن» می‌داند و خود می‌نویسد که از «ساییده‌شده» معنی «نرم، لطیف، سست» نیز پدید آمده است؛ پس برچسب زبانی، معنا و ارجاع POK:716 هر سه درست است. واتکینز در پیوست فرهنگ میراس آمریکایی هم دقیقاً همین را کرده و ریشهٔ mel-1 «نرم» را از mele- «ساییدن» جدا کرده است. شمارهٔ «۳» در «Mel 3» فقط شماره‌گذاری شخصی نورایی است. ادعای نورایی دربارهٔ ریشه درست است.\",\n  \"sources\": [U_AMAL],\n  \"ref_check\": [\n    {\"ref\": \"POK:716\", \"status\": \"supports\", \"note\": \"POK_02.txt leaf 377 (printed 716): '1. mel- (auch smel-), mels- : mle-, mel-d- : ml-ed-, mel-dh-, ml-ei- : mli-, mela-k- : mla-k-, mleu- : mlu- ,zermalmen, schlagen, mahlen‘ speziell Korn; aus ,zerrieben‘ auch ,fein, zart, weich‘ und ,aufgerieben, schwach‘' — the 'soft, soft material' gloss Nourai gives is Pokorny's own secondary sense on exactly that page.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. II pp. 284-291 (WLD_Bd2_pages.txt leaves 290-295)\", \"stance\": \"supports\", \"note\": \"Walde-Pokorny II 285 s.v. mel- and II 290 'mela-q- in der Bed. ‚weich, schwach, matt, albern‘. Gr. malakos ‚weich‘' — the source Pokorny 716 is a revision of.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. mel-1 (AHD_watkins1985.txt)\", \"stance\": \"supports\", \"note\": \"'mel-1. Soft; with derivatives referring to soft or softened materials of various kinds' with I. *meld- (MELT, MILT, MALT, mollis > MOLLUSK), II. *smeld- (SMELT, ENAMEL), III. *meldh- (MILD), IV. *mel-sko- (MULCH), V. *ml-k- (Greek malakos), VI. 'Possibly Celtic *molto-, sheep ... MUTTON'. [Pok. 1. mel- 716]\"},\n    {\"src\": \"IEC\", \"where\": \"Mann s.v. meleuos (2) (IEC.txt line 10547)\", \"stance\": \"supports\", \"note\": \"'meleuos (melouos, meluos) (2) “soft, effete, silly”. WP II, 284 & 291 Skt. malvah “foolish” ... ME melwe “mellow”'.\"},\n    {\"src\": \"KLN\", \"where\": \"s.v. meal 'edible grain' (KLN_1966.txt line 23234)\", \"stance\": \"supports\", \"note\": \"Klein derives from '*mel-dh-, enlargement of base *mel-' Gk. malthakos 'soft', Goth. mildeis, OE. milde, and lists as cognate derivatives 'amalgam, Amalthaea, ... emollient, ... malaco-, malax, malt, ... melt, mild, ... mollify, Mollugo, mollusk, mouille, ... mulch' — the same family Nourai draws.\"}\n  ],\n  \"nodes\": []\n}\n\ne0[\"nodes\"] = [\n {\n  \"id\": 1, \"lang\": \"Greek\", \"words\": \"malaxos; malagma\", \"verdict\": \"transcription_suspect\",\n  \"derivation\": \"The two Greek words are real and belong here, but the first is misprinted. Gk. μαλακός malakós 'soft, gentle' (Homer onwards) goes back to the k-extension of the root, Pokorny's mela-k- : mla-k- 'weich, schwach, matt, albern' (POK p.719: 'Gr. malakos ‚weich‘'), i.e. *ml-k-o- with the zero grade of *mel-; μάλαγμα málagma 'emollient, poultice, soft mass' is the -ma noun of μαλάσσω malássō 'to soften' (< *malak-yō, denominative of malakós), a technical term of Hippocratic and later Greek medicine — exactly the 'soft material' of the chart, and the form that travelled east. But the printed chart reads 'malaxos', which is not a Greek word (μαλακός has κ, not χ/ξ); the -x- is the book's own slip, perhaps contaminated by the future μαλάξω maláxō of malássō. The extraction is faithful: the page image (site/pages/330.jpg, copy at data/verification/sources/refs/ocr/BOOK/330.png) prints 'malaxos : soft'.\",\n  \"derivation_fa\": \"هر دو واژهٔ یونانی در این جایگاه درستند، ولی صورت نخست غلط چاپ شده است: یونانی مالاکوس malakós «نرم» از گونهٔ گستردهٔ *ml-k- ریشهٔ *mel- است (پوکورنی ۷۱۹ زیر mela-k-) و مالاگما málagma «مرهم، خمیر نرم» اسم مفعولیٔ فعل malássō «نرم کردن» و اصطلاحی پزشکی است. اما در کتاب malaxos چاپ شده که واژه‌ای یونانی نیست؛ این خطای چاپی خود کتاب است (شاید زیر تأثیر مضارع maláxō) و خوانش اسکن درست است: تصویر صفحه همین malaxos را نشان می‌دهد.\",\n  \"error_in\": \"book\", \"book_prints\": \"malaxos\", \"correct_form\": \"malakos (μαλακός)\",\n  \"sources\": [U_AMAL, U_MLGM],\n  \"ref_check\": [\n    {\"ref\": \"POK:719\", \"status\": \"supports\", \"note\": \"POK_02.txt leaf 381 (printed 719): 'mela-k-, mlak- ‚weich, schwach, matt, albern‘. Gr. malakos ‚weich‘, blax ...'; the same leaf under mel-dh- has 'gr. malthakos ‚weich, zart, mild‘ (nach malakos erweitert aus:) maltha ‚Wachs‘' — so p.719 is precisely where Pokorny treats the Greek 'soft' words.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. II p. 290 (WLD_Bd2_pages.txt leaf 295)\", \"stance\": \"supports\", \"note\": \"'mela-q- in der Bed. ‚weich, schwach, matt, albern‘. Gr. malakos ‚weich‘ ... -kos ‚schlaff, träge, weichlich, töricht‘'.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. mel-1, section V\", \"stance\": \"supports\", \"note\": \"'V. Extended form *ml-k- in Greek malakos, soft: CHONDROMALACIA, MALACOLOGY, OSTEOMALACIA.'\"},\n    {\"src\": \"KLN\", \"where\": \"KLN_1966 p.58 s.v. amalgam\", \"stance\": \"supports\", \"note\": \"'... Syr. malagma, fr. Gk. μαλαγμα, “a soft mass‘, fr. μαλασσειν, “to soften‘, fr. μαλακος, “soft‘' — Klein spells the adjective malakos, with k.\"}\n  ]\n },\n {\n  \"id\": 2, \"lang\": \"Arabic\", \"words\": \"al-mâlâgmâ\", \"verdict\": \"plausible\",\n  \"derivation\": \"The route is right, the form is not. Greek málagma passed into Aramaic/Syriac medical usage as malagmā and thence, in the Graeco-Arabic translation movement of the 9th c., into Arabic as ملغم malḡam / ملغمة malḡama 'emollient poultice, warm unguent for sores' (Lokotsch no. 1378 calls it a metathesis of μάλαγμα → malgam; Wiktionary derives Ar. ملغم straight from μάλαγμα). What the chart prints, 'al-mâlâgmâ', is not an Arabic word: it is Klein's Syriac intermediary malagmā with the Arabic article stuck in front of it. The real Arabic form is al-malḡam, which is what Medieval Latin borrowed (amalgama, by dissimilation/loss of the first l). So the arrow Greek > Arabic is confirmed; only Nourai's spelling conflates the Syriac and Arabic stages.\",\n  \"derivation_fa\": \"مسیر درست است ولی صورت نادرست: یونانی málagma نخست در سریانی malagmā شد و سپس در نهضت ترجمهٔ سدهٔ سوم هجری به عربی راه یافت و «ملغم / ملغمه» شد به معنای مرهم و ضماد نرم‌کننده (لوکوچ شمارهٔ ۱۳۷۸ آن را حاصل قلب malagma می‌داند). اما صورتی که در کتاب آمده (al-mâlâgmâ) عربی نیست؛ نورایی صورت سریانی را با الف‌ولام عربی درهم آمیخته است؛ صورت عربی درست «الملغم» است. پس پیکان یونانی ــ> عربی پذیرفتنی است و تنها ضبط واژه با احتیاط.\",\n  \"sources\": [U_MLGM, U_AMAL],\n  \"ref_check\": [\n    {\"ref\": \"KLN:58\", \"status\": \"partial\", \"note\": \"KLN_1966.txt line 2391 (printed p.58, the next line carries the running number 59): 'amalgam, n. — F. amalgame, fr. ML. amalgama, dissimil. fr. Arab. al-malgham, which is formed fr. Arab. al-, ‚the‘ and Syr. malagma, fr. Gk. μαλαγμα, ‚a soft mass‘, fr. μαλασσειν ‚to soften‘, fr. μαλακος ‚soft‘.' Klein has the Greek>Arabic>ML>French chain Nourai draws, but (a) inserts Syriac as the intermediary and (b) spells the Arabic al-malgham, not al-malagma.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1378 (LKT.txt line 3186)\", \"stance\": \"supports\", \"note\": \"'1378. Ar. malgam ‚Erweichende Salbe‘ [aus gr. μάλαγμα mit Metathesis]; hieraus sp. pg. kat. amalgama, frz. amalgame; engl. amalgam ... dtsch. Amalgam' — Greek > Arabic > Romance, exactly the chart's chain.\"},\n    {\"src\": \"BQT\", \"where\": \"vol. 4 printed p. 2032 (BQT_v4_pages.txt pdf 115), Mo'in's footnote 1 to ملک\", \"stance\": \"supports\", \"note\": \"'ملغم و ملغمه عربی ظاهراً از یونانی malagma (خمیر کردن) مأخوذ است. همین لفط عربی «الملغمه» وارد لاتینی (کیمیاگران) شده صورت amalgama در آمده و از آنجا وارد زبان فرانسوی شده amalgamer' — Mo'in gives Nourai's whole chain.\"},\n    {\"src\": \"DEV\", \"where\": \"Devic, Dictionnaire étymologique, s.v. Amalgame (DEV.txt lines 489-497)\", \"stance\": \"partial\", \"note\": \"Devic knows amalgame only from the 13th-c. Latin alchemists and canvasses Arabic عمل الجماع 'amal al-djama / al-mudʒāmaʿa instead ('Mais qu'est-ce que amalgame? Faut-il y voir ... 'amal al-djama, l'œuvre, la pratique de l'algame?'), while admitting 'je n'oserais affirmer l'exactitude de mes conjectures' — an older alternative that the malḡam etymology has since displaced.\"},\n    {\"src\": \"AFM\", \"where\": \"Addi Shir, Kitab al-Alfaz al-Farisiyya al-Mu'arraba (AFM_pages.txt)\", \"stance\": \"silent\", \"note\": \"grep 'ملغم' in AFM_pages.txt / AFM.txt: no hit — as expected, since Addi Shir collects Persian, not Greek, loans in Arabic.\"}\n  ]\n },\n {\n  \"id\": 3, \"lang\": \"Persian\", \"words\": \"malğam\", \"verdict\": \"confirmed\",\n  \"derivation\": \"New Persian ملغم malḡam 'salve, ointment, paste' (with the chart's extras ملغمه malḡama and الغام ilḡām, the Arabic IV-stem verbal noun 'amalgamating') is a straight loan from Arabic malḡam, i.e. a Greek medical term that reached Persian through Arabic pharmacology, not through Middle Persian. Mo'in tags it accordingly: 'ملغم [معر. ...] (بر.) مرهم. (پز.) کهنه و پنبه‌ای که مرهم را بر آن مالند و بر زخم نهند. (پز.) روغن‌مالی بر اعضای بدن' and, in a second entry, 'ملغم [ع.] (امف.) فلزی که با جیوه [ممزوج شود]' — both of Nourai's senses. There is a faint irony the chart does not note: the Persian folk association with مالیدن mālīdan 'to rub' (the very verb of the next entry on this page) is accidental, the two being etymologically unrelated.\",\n  \"derivation_fa\": \"«ملغم» فارسی وام‌واژه‌ای است از عربی ملغم (و ملغمه، الغام از باب افعال)، که خود از یونانی malagma است؛ پس یک اصطلاح پزشکی یونانی است که از راه عربی به فارسی رسیده، نه از راه فارسی میانه. معین در فرهنگ فارسی آن را «معرّب» می‌داند و به «مرهم» و «روغن‌مالی بر اعضای بدن» معنی می‌کند و در مدخلی دیگر به «فلزی که با جیوه ممزوج شود». ادعای نورایی درست است؛ تنها باید توجه داشت که شباهت آن به «مالیدن» ریشه‌شناسی عامیانه است.\",\n  \"sources\": [U_MLGM],\n  \"ref_check\": [\n    {\"ref\": \"MON:4345\", \"status\": \"supports\", \"note\": \"MON_part2.txt lines 64804-64809: 'ملغم: [معر. ...] (بر.) مرهم. (پز.) کهنه و پنبه‌ای که مرهم را بر آن مالند و بر زخم نهند. (پز.) روغن‌مالی بر اعضای بدن.' and 'ملغم: [ع.] (امف.) فلزی که با جیوه ...' — Mo'in's 'paste/ointment' and 'amalgam' senses, marked as Arabicized, exactly as the chart has it.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"BQT\", \"where\": \"vol. 4 printed p. 2032 and the cross-reference on the same page (BQT_v4_pages.txt pdf 115: 'ملغم و ملغمه - رک: ملم')\", \"stance\": \"supports\", \"note\": \"Mo'in's footnote there says 'ملغم و ملغمه عربی ظاهراً از یونانی malagma (خمیر کردن) مأخوذ است' — the Persian word is the Arabicized Greek one.\"},\n    {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1378\", \"stance\": \"supports\", \"note\": \"gives the eastern reflexes of Ar. malgam 'erweichende Salbe' (Turk. melhem, Bulg. mehlem, Serb. melem 'Salbe'), the same Arabic word Persian borrowed.\"}\n  ]\n },\n {\n  \"id\": 4, \"lang\": \"French\", \"words\": \"amalgame\", \"verdict\": \"confirmed\",\n  \"derivation\": \"Medieval Latin amalgama, an alchemists' word of c.1300 (Albertus Magnus' Semita recta, Arnald of Villanova's Parvum Rosarium both use amalgama), from Arabic al-malḡam with dissimilation of l...l > 0...l; French amalgame is first the alchemists' 'union of mercury with a metal', later (1790s) any close mixture, with the verb amalgamer. Klein p.58 gives 'F. amalgame, fr. ML. amalgama, dissimil. fr. Arab. al-malgham'; Mo'in in Borhan-e Qate' (p. 2032) describes the same step ('وارد لاتینی (کیمیاگران) شده ... و از آنجا وارد زبان فرانسوی شده amalgamer'). The chart draws the arrow from the Arabic box, which is right; it just skips the Medieval Latin stage.\",\n  \"derivation_fa\": \"فرانسوی amalgame از لاتینی میانه amalgama است، اصطلاحی در متون کیمیاگری سدهٔ سیزدهم میلادی، و آن از عربی «الملغم» با ناهمگونی (dissimilation) دو لام و افتادن لام نخست. کلاین و معین هر دو همین زنجیره را می‌دهند؛ ادعای نورایی درست است و تنها مرحلهٔ لاتینی میانه در نمودار نیامده است.\",\n  \"sources\": [U_AMAL],\n  \"ref_check\": [\n    {\"ref\": \"KLN:58\", \"status\": \"supports\", \"note\": \"KLN_1966.txt line 2391 (p.58): 'amalgam, n. ... — F. amalgame, fr. ML. amalgama, dissimil. fr. Arab. al-malgham'; and line 2392: 'amalgam, tr. and intr. v. ... F. amalgamer, fr. amalgame.'\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"DEV\", \"where\": \"Devic s.v. Amalgame (DEV.txt line 489)\", \"stance\": \"partial\", \"note\": \"'Ce mot nous est venu par les alchimistes avec le sens de mélange intime ... Je n'en connais pas d'exemple avant le XIIIᵉ siècle' — confirms the alchemical Latin > French route and dates it, but prefers a different Arabic source word.\"},\n    {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1378\", \"stance\": \"supports\", \"note\": \"'hieraus sp. pg. kat. amalgama, frz. amalgame'.\"}\n  ]\n },\n {\n  \"id\": 5, \"lang\": \"English\", \"words\": \"amalgam\", \"verdict\": \"confirmed\",\n  \"derivation\": \"English amalgam is attested c.1400 in the alchemical sense 'a blend of mercury with another metal; soft mass formed by chemical manipulation', from Old French amalgame / Medieval Latin amalgama; the figurative 'compound of different things' is c.1790. The arrow French > English is standard; Watkins files the word under mel-1 and Etymonline traces it to '*meldh-, from root *mel- (1) ‚soft‘', i.e. the root box of this chart.\",\n  \"derivation_fa\": \"انگلیسی amalgam از حدود ۱۴۰۰ میلادی در متون کیمیاگری به معنای «آمیزهٔ جیوه با فلزی دیگر» به کار رفته و از فرانسوی کهن / لاتینی میانه وام گرفته شده است؛ معنای مجازی «آمیزهٔ چیزهای ناهمانند» از حدود ۱۷۹۰ است. واتکینز و اتیمولاین نیز آن را به همین ریشهٔ *mel- «نرم» باز می‌گردانند. ادعای نورایی درست است.\",\n  \"sources\": [U_AMAL],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. mel-1 does not spell AMALGAM out in the list, but Klein (the source Nourai cites for the same box, p.58) and Etymonline both put amalgam under *mel- 'soft'; Etymonline: 'from PIE *meldh-, from root *mel- (1) ‚soft‘'.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"KLN_1966 p.58 s.v. amalgam\", \"stance\": \"supports\", \"note\": \"'F. amalgame, fr. ML. amalgama ... See malaco- and cp. Amalthaea.'\"},\n    {\"src\": \"SKT\", \"where\": \"Skeat (SKT.txt)\", \"stance\": \"silent\", \"note\": \"grep '^AMALGAM' in SKT.txt: no entry in the Concise edition.\"}\n  ]\n },\n {\n  \"id\": 6, \"lang\": \"Germanic\", \"words\": \"meltan; milks; smelt, malta, mildja, milks\", \"verdict\": \"confirmed\",\n  \"derivation\": \"Every form in the box is a Watkins reconstruction under mel-1 and the box reproduces his sections I-IV: Gmc. *meltan (OE meltan 'to melt', Watkins I.1); Gmc. *mil-sk- < *mel-sko- (OE mel(i)sc, mylsc 'mild, mellow', whence ME melsche and NE mulch, Watkins IV) — this is Nourai's 'milks : mulch'; Gmc. *smelt- (MDu./MLG smelten 'to smelt', OHG smalz, OFr. esmail > ENAMEL, Watkins II); Gmc. *malta- (OE mealt 'malt', I.3); Gmc. *mildja- < *meldh- (OE milde 'mild', III.1). The second 'milks' at the end of the list is simply the same *mil-sk- repeated. Phonetically these are the Germanic outcomes of the dental extensions of *mel-: *mel-d- > Gmc. *melt-/*malt- by Grimm's law (d > t), *meldh- > Gmc. *mild-, with s-mobile in *smeld- > *smelt-.\",\n  \"derivation_fa\": \"همهٔ صورت‌های این جعبه بازسازی‌های ژرمنی آغازین در پیوست واتکینز زیر mel-1 است: *meltan (انگلیسی کهن meltan)، *mil-sk- (انگلیسی کهن mel(i)sc «نرم، رسیده» که همان «milks : mulch» نورایی است)، *smelt- با s متحرک، *malta- و *mildja-. دگرگونی آوایی طبق قانون گریم است: d هندواروپایی در ژرمنی به t بدل شده (*mel-d- > *melt-) و dh به d (*meldh- > *mild-). ادعای نورایی درست است؛ تنها «milks» دو بار تکرار شده است.\",\n  \"sources\": [],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. mel-1: 'I. Extended form *meld-. 1. Germanic *meltan in Old English meltan, to melt: MELT ... 3. Possibly Germanic *malta- in Old English mealt, malt: MALT ... II. Variant form *smeld-. Germanic *smelt- ... III. Extended form *meldh-. 1. Germanic *mildja- in Old English milde ... IV. Suffixed form *mel-sko- in Germanic *mil-sk- in Old English mel(i)sc, mylsc, mild, mellow (> Middle English melsche, friable): MULCH.'\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"POK_02.txt leaves 380-381 (printed 718-719)\", \"stance\": \"supports\", \"note\": \"'ags. meltan ‚schmelzen, verbrennen, verdauen‘ ... ahd. malz, ags. mealt, as. aisl. malt ‚Malz‘' (mel-d-, p.718) and 'got. unmildjai ... ags. milde, ahd. milti ‚milde, gütig‘' (mel-dh-, p.719); 'mit anl. s-: ahd. smelzan ‚zerfließen, schmelzen‘, smalz'.\"},\n    {\"src\": \"KLN\", \"where\": \"KLN_1966 s.v. malt (line 22697), mild (23878), melt (23411)\", \"stance\": \"supports\", \"note\": \"'malt ... traceable to I.-E. *mel-d-, a d-enlargement of base *mel-'; 'mild ... fr. I.-E. *mel-dh-, enlargement of base *mel-'; 'melt ... fr. I.-E. base *meld-'.\"}\n  ]\n },\n {\n  \"id\": 7, \"lang\": \"English\", \"words\": \"melt, smelt, malt, mild, mulch, enamel\", \"verdict\": \"confirmed\",\n  \"derivation\": \"All six are Watkins's own English outcomes of mel-1: melt (OE meltan intr. / mieltan tr., ME melten), smelt (MDu./MLG smelten, borrowed into English in the 15th c. as a metallurgical term), malt (OE mealt), mild (OE milde), mulch (dial. adj. melsh, melch 'soft, mellow' < OE mel(i)sc, substantivized in the 17th c. for the loose straw laid on soil), enamel (ME enamelen, from Anglo-French enamayller, from Old French esmail 'enamel', itself a Germanic loan cognate with OHG smelzen 'to melt'). Only enamel takes the detour through French, and Klein spells the loop out: 'OF. esmail (F. email), which is a Teut. loan word. Cp. OHG. smelzen, OE. meltan, ‚to melt‘'.\",\n  \"derivation_fa\": \"هر شش واژه در پیوست واتکینز زیر ریشهٔ mel-1 آمده‌اند: melt (انگلیسی کهن meltan)، smelt (وام از هلندی میانه در سدهٔ پانزدهم)، malt، mild، mulch (از گویشی melsh «نرم») و enamel. تنها enamel از راه فرانسه آمده است: فرانسوی کهن esmail که خود وام‌واژه‌ای ژرمنی و هم‌ریشهٔ smelzen آلمانی عالی کهن است. ادعای نورایی درست است.\",\n  \"sources\": [],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. mel-1 lists MELT, SMELT1, SCHMALTZ, SMALT, ENAMEL, SMELT2, MALT, MILT, MILD, MULCH under the Germanic branches — the chart's English box is a subset of that list.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"KLN_1966 s.v. enamel (line 13040), melt (23411), malt (22697), mild (23878), meal (23234)\", \"stance\": \"supports\", \"note\": \"'enamel, tr. v. — ME. enamelen, fr. AF. enamayller, fr. 1st en- and amayl, fr. OF. esmail (F. email), which is a Teut. loan word. Cp. OHG. smelzen, OE. meltan, ‚to melt‘'; the s.v. meal list of cognates includes 'mulch'.\"},\n    {\"src\": \"SKT\", \"where\": \"SKT.txt\", \"stance\": \"silent\", \"note\": \"grep '^MUTTON|^MULCH' in Skeat's Concise: no entries for these headwords in this printing.\"}\n  ]\n },\n {\n  \"id\": 8, \"lang\": \"Latin\", \"words\": \"mollis\", \"verdict\": \"confirmed\",\n  \"derivation\": \"Latin mollis 'soft, supple, pliant' < *ml̥d-w-is, the zero-grade of the d-extension *mel-d- with the -u- suffix, matching Skt. mṛdú- 'soft, tender' (fem. mṛdvī) and Gk. βλαδύς bladús 'flabby'; the -ldw- cluster gives Latin -ll-. Pokorny p.718 states it in those terms: 'lat. mollis ‚weich, geschmeidig, biegsam‘ (*ml̥du-is, vgl. ai. fem. mṛdvī)'. The same page also derives mulier 'woman' from the comparative *ml̥-i̥os-ī 'the softer one' — a byway the chart leaves out.\",\n  \"derivation_fa\": \"لاتینی mollis «نرم، نرمشدنی» از *ml̥d-w-is است، یعنی پایهٔ صفر گونهٔ دندانی *mel-d- با پسوند -u-؛ هم‌ریشه با سنسکریت mṛdú- «نرم، لطیف» و یونانی bladús. خوشهٔ -ldw- در لاتینی به -ll- بدل شده است. پوکورنی (ص ۷۱۸) عیناً همین را می‌گوید. ادعای نورایی درست است.\",\n  \"sources\": [],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. mel-1: 'I. ... 5. Suffixed zero-grade form *ml̥d-wi- in Latin mollis, soft: MOIL, MOLLIFY, MOLLUSK, MOUILLE; EMOLLIENT.'\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"POK_02.txt leaf 380 (printed 718)\", \"stance\": \"supports\", \"note\": \"'lat. mollis ‚weich, geschmeidig, biegsam‘ (*ml̥du-is, vgl. ai. fem. mṛdvī)'.\"},\n    {\"src\": \"KLN\", \"where\": \"KLN_1966 s.v. melt (line 23411)\", \"stance\": \"supports\", \"note\": \"'... fr. I.-E. base *meld-, whence also Gk. μέλδειν ‚to melt‘, L. mollis (for *moldwis), ‚soft, mild‘. See mollify.'\"}\n  ]\n },\n {\n  \"id\": 9, \"lang\": \"English\", \"words\": \"mollusk\", \"verdict\": \"confirmed\",\n  \"derivation\": \"mollusk/mollusc is a Modern Latin coinage: Cuvier (1795-1798) took over Linnaeus's class name Mollusca, the neuter plural of Latin molluscus 'softish' (a diminutive-adjectival derivative of mollis, used by Pliny in mollusca nux 'a soft-shelled nut'), and English took it through French mollusque. Klein sets it out exactly so.\",\n  \"derivation_fa\": \"mollusk ساختهٔ لاتینی نو است: کوویه در پایان سدهٔ هجدهم نام ردهٔ Mollusca را از لاتینی molluscus «نرمینه» (از mollis، به کار رفته در ترکیب mollusca nux «گردوی نرم‌پوست» پلینیوس) گرفت و انگلیسی از راه فرانسوی mollusque آن را وام گرفت. ادعای نورایی درست است.\",\n  \"sources\": [],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. mel-1 I.5 lists MOLLUSK among the derivatives of Latin mollis.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"KLN_1966 line 24206 s.v. mollusk\", \"stance\": \"supports\", \"note\": \"'mollusk, mollusc, n., any of the Mollusca. — F. mollusque, coined by the French naturalist, Baron Georges-Léopold-Chrétien-Frédéric-Dagobert Cuvier (1769-1832) fr. L. molluscus, ‚soft‘ (in mollusca nox [read: nux], ‚a soft kind of nut with a thin shell‘), fr. mollis, ‚soft‘.'\"},\n    {\"src\": \"LEW\", \"where\": \"Walde, Lateinisches etym. Wörterbuch (LEW_1910.txt)\", \"stance\": \"silent\", \"note\": \"the 1910 edition has mollis but no ModL. molluscus (a post-Linnaean coinage), so it cannot speak to this node.\"}\n  ]\n },\n {\n  \"id\": 10, \"lang\": \"Celtic\", \"words\": \"molto\", \"verdict\": \"plausible\",\n  \"derivation\": \"A Celtic *molto-/*multo- 'wether, castrated ram' is securely reconstructed from Welsh mollt, Cornish mols, Breton maout, Middle Irish molt, Gaelic mult, and it is the source of Gallo-Roman *multo, -ōnem. What is not secure is the arrow from the root: Pokorny p.716f. files 'kelt. *molto- in cymr. mollt, corn. mols, bret. maout, mir. molt, gall.-rom. multo, -ōne ‚(verschnittener) Widder‘' under mel-1, and Watkins repeats it with an explicit hedge, 'VI. Possibly Celtic *molto-, sheep'; Etymonline likewise says the Celtic word 'is perhaps from PIE root *mel- (1) ‚soft‘', and Klein s.v. mutton records the Celtic forms without offering any IE root at all. The semantics ('the soft/gelded one'?) are the weak point. Nourai draws the hedged link as a plain arrow.\",\n  \"derivation_fa\": \"واژهٔ سلتی آغازین *molto-/*multo- «قوچ اخته» از ولزی mollt، کورنی mols، برتون maout و ایرلندی میانه molt بازسازی می‌شود و قطعی است؛ اما پیوند آن با ریشهٔ *mel- «نرم» قطعی نیست: پوکورنی آن را زیر همین ریشه می‌آورد ولی واتکینز با قید «شاید» و اتیمولاین نیز با «perhaps»، و کلاین به‌کلی ریشهٔ هندواروپایی نمی‌دهد. پس این پیکان با احتیاط پذیرفتنی است.\",\n  \"sources\": [U_MUTTON],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"Watkins 1985 s.v. mel-1: 'VI. Possibly Celtic *molto-, sheep, in Old French moton, sheep: MUTTON.' — the form and the route are his, but the attachment to the root is marked 'Possibly'.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"POK_02.txt leaf 378 (printed 716-717)\", \"stance\": \"supports\", \"note\": \"'kelt. *molto- in cymr. mollt, corn. mols, bret. maout, mir. molt, gall.-rom. multo, -öne ‚(verschnittener) Widder‘' — listed inside the mel-1 entry with no question mark.\"},\n    {\"src\": \"KLN\", \"where\": \"KLN_1966 line 24790 s.v. mutton\", \"stance\": \"partial\", \"note\": \"'fr. Gaul. L. *multonem, acc. of *multō, ‚sheep‘, which is of Celtic origin. Cp. Gael. mult, MIr. molt, W. mollt, MBret. mout, Bret. maul, ‚wether‘' — Celtic yes, but Klein offers no *mel- connection.\"}\n  ]\n },\n {\n  \"id\": 11, \"lang\": \"English\", \"words\": \"mutton\", \"verdict\": \"confirmed\",\n  \"derivation\": \"Middle English motoun 'sheep's flesh' (c.1300), from Old French moton 'ram, wether' (Modern French mouton 'sheep'), from Medieval Latin multonem (8th c.), accusative of the Gallo-Roman *multo borrowed from Celtic *multo-. The Norman French / English split between the live animal (Germanic sheep) and the meat (French mutton) is the standard post-Conquest doublet. The chain Celtic > Gallo-Latin > Old French > English is uncontroversial; only its ultimate attachment to *mel- is (see node #10).\",\n  \"derivation_fa\": \"انگلیسی میانه motoun (حدود ۱۳۰۰ م.) از فرانسوی کهن moton «قوچ»، از لاتینی میانه multonem (سدهٔ هشتم) و آن وامی از سلتی *multo-. جدایی میان نام جانور زنده (sheep، ژرمنی) و نام گوشت آن (mutton، فرانسوی) از پیامدهای فتح نورمن‌هاست. ادعای نورایی دربارهٔ این حلقه درست است.\",\n  \"sources\": [U_MUTTON],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. mel-1 VI ends 'in Old French moton, sheep: MUTTON.'\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"KLN_1966 line 24790 s.v. mutton\", \"stance\": \"supports\", \"note\": \"'mutton, n., the flesh of sheep. — ME. motoun, fr. OF. moton, mutton, ‚a ram‘ (whence F. mouton, ‚sheep‘), fr. Gaul. L. *multonem ...'\"},\n    {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century (WEB_vol1.txt)\", \"stance\": \"silent\", \"note\": \"vol. 1 of the local scan stops before M, so it cannot be consulted for this word.\"}\n  ]\n }\n]\n\ne1 = {\n  \"entry\": 1,\n  \"root\": \"Mělg\",\n  \"verdict\": \"confirmed\",\n  \"modern_form\": \"Pokorny's melǵ- (mela-ǵ-?) 'abstreifen, wischen', in the European languages 'melken'; modern handbooks split it into PIE *h2melǵ- 'to milk' and *h2merǵ- 'to wipe, strip off'\",\n  \"note\": \"The root box reproduces Pokorny p.722 word for word: 'melǵ- (oder mela-ǵ-?) ‚abstreifen, wischen‘, europ. ‚melken‘; Präs. melǵ-mi, Pl. ml̥ǵ-mes, Partiz. Perf. Pass. ml̥ǵ-tó-; molǵo- ‚Melken‘' — so language label, gloss ('to wipe off, to milk') and page are all exactly right, and Watkins repeats it ('melg-. To rub off; also to milk ... [Pok. melg- 722]'). Mann (IEC) even explains the semantic bridge: 'The semantic association of ‚wipe‘ and ‚milk‘ is apparent in Latvian slauku, slaucit ‚wipe‘; slaucu, slaukt ‚milk‘'. What has changed since 1959 is the unity of the root: LIV, Cheung and Wiktionary keep *h2merǵ- 'to pluck, wipe' (Gk. amérgō, Skt. mṛj-, Ir. *Hmarz) apart from *h2melǵ- 'to milk' (Lat. mulgeō, Gmc. *melkan), the r/l difference being original rather than dissimilatory; Pokorny himself flagged the doubt on the same page ('diese ar. Worte können auch *merǵ- enthalten'). So the two Avestan branches of this chart hang on the older, unified reconstruction — see nodes #1 and #3.\",\n  \"note_fa\": \"جعبهٔ ریشه عیناً مدخل صفحهٔ ۷۲۲ پوکورنی است: melǵ- «زدودن، پاک کردن» و در زبان‌های اروپایی «دوشیدن»؛ پس برچسب و معنا و ارجاع درست است. مان (فرهنگ مقایسه‌ای هندواروپایی) پیوند معنایی دو معنا را با شاهد لتونی slaukt (هم «زدودن» هم «دوشیدن») توجیه می‌کند، و اریان‌پور هم همین را می‌گوید. اما زبان‌شناسی امروز (لیف، چونگ، ویکی‌واژه) این ریشه را دو ریشهٔ جدا می‌داند: *h2merǵ- «مالیدن، زدودن» و *h2melǵ- «دوشیدن»؛ خود پوکورنی نیز در همان صفحه این احتمال را یادآور شده است. پس دو شاخهٔ اوستایی این نمودار بر بازسازی کهن استوار است.\",\n  \"sources\": [U_MELG],\n  \"ref_check\": [\n    {\"ref\": \"POK:722\", \"status\": \"supports\", \"note\": \"POK_02.txt leaf 384 (printed 722): 'melǵ- (oder mela-ǵ-?) ‚abstreifen, wischen‘, europ. ‚melken‘; Präs. melǵ-mi, Pl. ml̥ǵ-mes, Partiz. Perf. Pass. ml̥ǵ-tó-; molǵo- ‚Melken‘.' The entry then lists ai. mārṣṭi/mṛjáti, av. marəzaiti, gr. amélgō, lat. mulgeō, mir. bligim — i.e. all four branches of the chart.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. II p. 298 (WLD_Bd2_pages.txt leaf 303, line 19658)\", \"stance\": \"supports\", \"note\": \"'melǵ- ‚abstreifen, wischen‘, europ. ‚melken‘' and, further down, 'Die europ. Bed. ‚melken‘ ist aus ‚die Milch herausstreifen, abstreifen‘ [entwickelt]' — the WP page Pokorny 722 cites.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. melg- (AHD_watkins1985.txt line 739)\", \"stance\": \"supports\", \"note\": \"'melg-. To rub off; also to milk. I. 1. Zero-grade form *ml̥g- in Latin mulgére, to milk: EMULSION. 2. Full-grade form *melg- in Germanic *melkan ... [Pok. melg- 722, glag- 400.]' — note his caveat that the Germanic verb 'was contaminated with an unrelated noun for milk ... to form the blend *meluk-'.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann s.v. melǵō (IEC.txt line 10547)\", \"stance\": \"supports\", \"note\": \"'melǵō ‚caress, titillate, massage, milk‘ ... Skt. mrjámi ‚wipe‘; Av. mərəzai(mi), id.; Gk. mélgō ‚massage, handle‘; a-mélgō ‚milk‘; Lat. mulgeo, id. ... (The semantic association of ‚wipe‘ and ‚milk‘ is apparent in Latvian slauku, slaucit ‚wipe‘; slaucu, slaukt ‚milk‘).'\"},\n    {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e Rishe-ha, printed p. 458-459 (ARY_pages.txt pdf 457-458), s.v. مالیدن\", \"stance\": \"supports\", \"note\": \"the entry lists Avestan MARZ/MAREZ, Pahlavi, Persian, Kurdish, Baluchi, Sanskrit alongside Greek/Latin/Germanic/Slavic forms, with the note 'چم واژه‌های این فهرست (به جز اوستایی و پهلوی و فارسی و کردی و بلوچی و سانسکریت): شیر، شیر دوشیدن (شاید بدین علت که شیر دوشیدن مستلزم مالش با مالیدن است)' and footnote 2 'میان این واجریشه و واجریشهٔ MEL (Pokorny: 716-717) خویشی نزدیکی وجود دارد' — Nourai's two roots on this page, and their link, in a Persian source.\"},\n    {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007 s.v. *Hmarz (CHEUNG.txt line 12365)\", \"stance\": \"partial\", \"note\": \"'*Hmarz ‚to wipe, rub‘ ... «PIE *H2merǵ- ‚to pluck, wipe‘ = LIV: 280 f. | Pok.: 722 f., 738' — Cheung reaches the same Pokorny page but reconstructs the root with -r-, not -l-.\"}\n  ],\n  \"nodes\": []\n}\n\ne1[\"nodes\"] = [\n {\n  \"id\": 1, \"lang\": \"Avestan\", \"words\": \"marz, marez, mrz, mard\", \"verdict\": \"plausible\",\n  \"derivation\": \"The four forms are all real and all belong to one Iranian verb, and Pokorny does put them here. Bartholomae col. 1152: 'j. marəz- V. ‚streifend berühren‘. Präs. 2 marəza-, 3 mərəza-, 8 mərəz-. — Inf. mərəždẏai' — Nourai's 'marz' (the root), 'marez' (Av. marəza-) and 'mrz' (the reduced mərəz-) are simply these three ablaut shapes. 'mard' is the Southwest Iranian variant: Nyberg s.v. mālītan says '< *mard-, SW form of marz-', and Abolghasemi (FFD p.77) writes 'māl < MP māl < Old Persian *mard-a- < Old Iranian *marz-a-'. Gloss 'to wipe, sweep, rub' is Bartholomae's 'streifend berühren' plus the Sanskrit mṛj- 'wipes, cleans'. What is only plausible is the arrow itself: Pokorny lists av. marəzaiti under melǵ- but adds on the same page 'diese ar. Worte können auch *merǵ- enthalten', and LIV/Cheung now assign it firmly to *h2merǵ- 'to pluck, wipe' (Gk. amérgō, Lat. mergae), a root distinct from the 'milk' root. Caveat: a homophonous Avestan marəd- 'verderben, zuschanden machen' (Bartholomae col. 1151, Cheung *Hmard 'to crush', Pok. 736f.) exists and must not be confused with the SW *mard- meant here.\",\n  \"derivation_fa\": \"چهار صورت درستند و همه به یک فعل ایرانی بازمی‌گردند: بارتولومه (ستون ۱۱۵۲) می‌نویسد «اوستایی marəz- «به نرمی لمس کردن، ساییدن»، مضارع marəza- / mərəza- / mərəz-»؛ پس marz و marez و mrz همان سه گونهٔ ابلاوتی اند. و mard گونهٔ جنوب غربی است: نیبرگ در مدخل mālītan می‌گوید «از *mard-، صورت جنوب‌غربی marz-» و ابوالقاسمی (فعل‌های فارسی دری، ص ۷۷) «مال < فارسی میانه māl < فارسی باستان *mard-a- < ایرانی باستان *marz-a-». آنچه با احتیاط پذیرفتنی است خود پیکان است: پوکورنی این فعل را زیر melǵ- آورده ولی خود افزوده که «این واژه‌های آریایی ممکن است *merǵ- داشته باشند»، و چونگ و لیف امروز قطعاً آن را به *h2merǵ- می‌برند. هشدار: اوستایی marəd- «تباه کردن» (بارتولومه ستون ۱۱۵۱) ریشهٔ دیگری است و نباید با این *mard- درهم آمیخت.\",\n  \"sources\": [U_MALID, U_MELG],\n  \"ref_check\": [\n    {\"ref\": \"POK:722\", \"status\": \"partial\", \"note\": \"POK_02.txt leaf 384 (printed 722) has 'av. marəzaiti, mərəzaiti ‚berührt streifend‘, zastā-marəsta- ‚durch Handschlag ... geschlossen (Vertrag)‘' inside melǵ-, so the arrow is Pokorny's; but the same paragraph warns 'diese ar. Worte können auch *merǵ- enthalten'.\"},\n    {\"ref\": \"FFD:77\", \"status\": \"supports\", \"note\": \"FFD_pages.txt pdf 82 = printed p.77: 'مُشت ← فارسی میانه mušt ← ایرانی باستان *mṛš-ta- ... mṛš صورت اصلی mṛz است، z پیش از t به š بدل شده است. mṛz صورت ضعیف ریشهٔ marz به معنی مالیدن است. / مال ← فارسی میانه māl ← فارسی باستان *mard-a- ← ایرانی باستان *marz-a-' — the exact set marz / mṛz / mard of Nourai's box.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"BRT\", \"where\": \"Bartholomae, Altiranisches Wörterbuch col. 1152 (BRT.txt line ~20063)\", \"stance\": \"supports\", \"note\": \"'j. marəz- V. ‚streifend berühren‘. Präs. 2 marəza-, 3 mərəza-, 8 mərəz-. — Inf. mərəždẏai'; with Yt 10.95 marəzaiti and Yt 14.19-21 'im Flug streifen'.\"},\n    {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007 pp. 181f. s.v. *Hmarz\", \"stance\": \"partial\", \"note\": \"'*AVESTAN: marəz- ‚to wipe, rub‘ || (+ *anu-) ‚to sweep‘ ... «PIE *H2merǵ- ‚to pluck, wipe‘ = LIV: 280 f. | Pok.: 722 f., 738' — same Avestan verb and gloss, but a *merǵ- root, so the chart's parent root box is the older view.\"},\n    {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II pp. 133, 137 s.vv. mālītan, marzihistan\", \"stance\": \"supports\", \"note\": \"'malitan [m'lytn'] to stroke ... < *mard-. SW form of marz-, v. marzīhistan; NP mālidan. Inf. also muštan, pt. must < *mṛsta-'; 'marzīhistan ... Av. (1152 sq.) marəz- ‚to touch‘ ... the genuine SW form is *mard- > māl-'.\"},\n    {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 962, p. 214 (HRN.txt leaf 236)\", \"stance\": \"supports\", \"note\": \"'aw. √marz-, marəzaiti ‚fegt‘; phlv. ... marz(i)šn ‚Coitus‘, marzītan, mālītan, māl(i)šn; ai. √marj-, mārṣṭi ‚abwischen‘' with the remark 'phlv. -marz weist wohl auf ai. √marj-, nicht auf ai. √mard-'.\"}\n  ]\n },\n {\n  \"id\": 2, \"lang\": \"Persian\", \"words\": \"mâlîdan; moštan; morz\", \"verdict\": \"confirmed\",\n  \"derivation\": \"All three Persian words are the regular reflexes of the same Old Iranian verb, and the chart's own extras (ماله māla 'plasterer's float', مالش māleš, مال māl; مشت mošt; مرزیدن morzīdan) are its derivatives. (1) مالیدن mālīdan 'to rub, smear, polish' < MP mālītan / māl- < Old Persian-type (SW) *marda- < Old Iranian *marza-: the -rz- of the North-West dialects appears as -l- in the South-West line, so that NW Ossetic marzyn 'to sweep' and Kurdish mālīn stand beside SW mālīdan (Nyberg; Abolghasemi FFD p.77; Cheung 181). (2) مُشتن moštan 'to rub, massage' is the same verb's past stem: *mṛz-ta- > *mṛš-ta- (z assimilated to the following t) > MP mušt > NP mošt(an); MacKenzie's Pahlavi Dictionary lists the verb as a single lemma 'muštan, māl- ‚rub, sweep‘'. (3) مُرز morz 'coition; the anus' preserves the unlateralized NW/Middle Persian marz-: Pahlavi kūn-marz 'sodomy', marz(i)šn 'coition', marzītan 'coire' (Nyberg; Horn 962), and Mo'in in Borhan-e Qate' refers the Persian noun مرز (glossed 'مقعد ... و بمعنی مباشرت و مجامعت') to 'ره و اسم فاعل مرخم از مرزیدن ... ورک مالیدن', i.e. to this very verb. One qualification: Horn (p.214 n.2) protests that 'Np. merz ‚Coitus‘ ist nicht belegt' and that jih-merz is only a Pāzand transcription — but the Persian lexica (Borhan, Dehkhoda) do record it, and the chart's Molavī line ('چند کوبد زخمهای گرزشان بر سر هر ژاجخا و مُرزشان') is a genuine attestation, so the word stands.\",\n  \"derivation_fa\": \"هر سه واژه بازماندهٔ یک فعل ایرانی باستانند. «مالیدن» از فارسی میانهٔ mālītan/māl-، از گونهٔ جنوب‌غربی *mard-a-، از ایرانی باستان *marz-a-؛ یعنی خوشهٔ -rz- در شاخهٔ جنوب‌غربی به -l- بدل شده است (در برابر کردی mālīn و اُستی marzyn). «مُشتن» مادهٔ ماضی همان فعل است: *mṛz-ta- > *mṛš-ta- (ابدال z به š پیش از t) > mušt؛ مکنزی نیز مدخل را یکجا «muštan, māl-» می‌آورد. «مُرز» صورت شمال‌غربی بی‌ابدال را نگاه داشته: پهلوی kūn-marz و marzītan «جماع کردن»، و معین در حاشیهٔ برهان قاطع آن را به «مرزیدن» و «مالیدن» باز می‌گرداند. تنها یادآوری: هرن منکر وجود merz در فارسی نو است، ولی فرهنگ‌های فارسی و بیت مولوی آن را گواهی می‌دهند. ادعای نورایی درست است.\",\n  \"sources\": [U_MALID],\n  \"ref_check\": [\n    {\"ref\": \"HRN:214\", \"status\": \"supports\", \"note\": \"HRN.txt leaf 236 = printed p.214, entry 962: 'māliden ‚reiben, glätten‘ ... vergl. musten (No. 983). aw. √marz-, marəzaiti ‚fegt‘; phlv. kūn-marz, dastān-marz, d\\u014ди́ak-marz Vd. 1(18), marz(i)šn ‚Coitus‘, marzītan ‚coitiren‘, mālītan, māl(i)šn; ai. √marj-, mārṣṭi ‚abwischen‘' — covers mālīdan, moštan and morz at once; footnote 2 there denies NP merz.\"},\n    {\"ref\": \"BQT:1948\", \"status\": \"supports\", \"note\": \"BQT vol.4 pdf 31 = printed p.1948, Mo'in's footnote 3 to ماله: 'مالیدن - بفتح دال، اوستا - marz-, marəzaiti (جاروب شده)، پهلوی [māl-, marz-] ... [mušt-] (جماع) ... هندی باستان mṛj- (پاک کردن)، کردی mālīn (جاروب کردن)، بلوچی mālag/malēnag (ساییدن، مالیدن)، اُستی marzin (جاروب کردن)' — Nourai's page is right and gives all three words (including the 'coition' sense of mušt-).\"},\n    {\"ref\": \"BQT:2010\", \"status\": \"supports\", \"note\": \"BQT vol.4 pdf 93 (= printed 2010), s.v. مشت: 'و بمعنی مالید هم آمده است که ماضی مالیدن باشد چه مشتن بمعنی مالیدن است' with a cross-reference 'رک: مشتن' — moštan = the past stem of mālīdan, exactly as drawn.\"},\n    {\"ref\": \"FFD:77\", \"status\": \"supports\", \"note\": \"see node #1: FFD p.77 derives مشت from *mṛš-ta- and مال from *mard-a- < *marz-a-.\"},\n    {\"ref\": \"MON:4010\", \"status\": \"not_found\", \"note\": \"the local Mo'in text (MON_part1/part2) is not paginated, so p.4010 could not be located; the lexicon does carry مالیدن and its compounds (MON_part1 lines 4872, 10085 etc.), consistent with the citation.\"},\n    {\"ref\": \"SYN:569\", \"status\": \"partial\", \"note\": \"Buck's section 9.31 RUB stands at SYN.txt leaf 623 (printed ≈571; the running-head numerals on leaves 621-623 read 563-578, so the scan drifts by a page or two around Nourai's 569). It gives the concept table (Grk. tribō, Lat. fricare/terere, Skt. ghṛṣ-, Av. [marz-, OCR-garbled]) and states the inherited group is IE *ter-; Buck does not cover New Persian, so the citation supports the Avestan/Sanskrit line only.\"},\n    {\"ref\": \"SNS:245\", \"status\": \"partial\", \"note\": \"SNS_pages.txt leaf 139-140 has the glossary entries 'marzēd', 'marz: marəza-', 'marsti' and 'marzišn: mrzyšn' with a reference '(GIrPh. 214 / [Bartholomae] 1153)'; the printed page numerals of this scan are illegible, so the exact page 245 could not be confirmed, but the entries Nourai cites are there.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary s.v. muštan (PHD_mackenzie.txt line 3632)\", \"stance\": \"supports\", \"note\": \"'muštan, māl- [mwstn', m'l-] rub, sweep.' — one lemma for both stems, i.e. NP moštan and mālīdan are one verb.\"},\n    {\"src\": \"NYB\", \"where\": \"Nyberg II s.vv. mālišn, mālītan, kūn-marz, marzīhistan\", \"stance\": \"supports\", \"note\": \"'mālišn, v. n. ... of the soft touch of a fragrant wind'; 'malitan ... Inf. also muštan, pt. must < *mṛsta-'; 'kūn-marz [kwnmlc'] sodomy, pederasty ... NP kūn ‚backside‘ + marz'; 'MPrs mrz- ‚to copulate‘, mrzyšn ‚coition‘, borrowed from NW'.\"},\n    {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007 pp. 181f. s.v. *Hmarz\", \"stance\": \"supports\", \"note\": \"'*MIDDLE PERSIAN: BMP mwst /must/ (pret. stem), m'l- /māl-/ ‚to rub, sweep‘ ... || LW: MMP mrz- ‚to mate, have sexual intercourse‘'; '*NWIR: NP mālidan/māl- ‚to rub, polish; to chafe, box the ears‘'.\"},\n    {\"src\": \"BQT\", \"where\": \"vol. 4 printed p. 1987 (BQT_v4_pages.txt pdf 70) s.v. مرز\", \"stance\": \"supports\", \"note\": \"'و مقعد و پشتگاه و مخرج سفلی را نیز گفته‌اند ... و بمعنی مباشرت و مجامعت هم هست' with Mo'in's footnote 4 'ره و اسم فاعل مرخم از مرزیدن (مباشرت و مجامعت). ورک «مالیدن»' — both of Nourai's glosses for morz, and the link to mālīdan.\"},\n    {\"src\": \"ARY\", \"where\": \"Aryanpur printed pp. 458-459 s.v. مالیدن\", \"stance\": \"supports\", \"note\": \"lists Av. MARZ/MAREZ, Pahlavi, Kurdish and Baluchi cognates for مالیدن and cites 'برهان قاطع ۱۹۴۸' — independently confirming that BQT:1948 is the مالیدن note.\"},\n    {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien (HUB.txt)\", \"stance\": \"silent\", \"note\": \"Horn 962 refers to Hübschmann ZDMG 44, 558 rather than to the Persische Studien; no entry for mālīdan was found in HUB.txt.\"}\n  ]\n },\n {\n  \"id\": 3, \"lang\": \"Avestan\", \"words\": \"â-marz; fra-â-marz\", \"verdict\": \"plausible\",\n  \"derivation\": \"Avestan has the compound verb ā-marz- and, with the -d- root-determinative, Old Avestan mərəžd- 'to have pity' (impv. 2pl. mərəždatā, Y 33.11), plus mərəždika- 'merciful, mercy' — the 'wipe out the sins, forgive' of the chart. That this 'forgive' verb is the 'wipe' verb plus -d- is precisely the position of Nourai's two references: Pokorny p.722 lists 'av. mərəždā- ‚verzeihen‘ (mərəždika-, marzdika- ‚sich erbarmend‘)' under melǵ-, and Horn p.12 no.49 writes 'Im Awesta und Altindischen wird die Bedeutung ‚gnädig sein, verzeihen‘ durch das Wurzeldeterminativ d aus der √merǵ- ‚abwischen‘ gewonnen' (after Bartholomae BB 13, 87), so the semantic bridge 'wipe away > wipe away sins > forgive' is the classical account. Modern Iranistics is more cautious: Cheung sets up a separate root *maržd 'to have pity, forgive' and notes 'The Ir. root *marzd has no IE correspondences'; Wiktionary derives آمرزیدن from Proto-Indo-Iranian *mṛžd- with no PIE ancestor. Second point: the form 'fra-â-marz' is Nourai's analysis of Av./MP frā-marz- as fra + ā + marz; the attested Avestan compound is framarəz- 'to wipe forth, away' (framarəzaiti, V 4.3f.), with the ordinary lengthened prefix frā-, not a stacked fra-ā-. The gloss 'one who forgives all sins' is the sense Persian tradition gives the name Farāmarz, not an Avestan attestation.\",\n  \"derivation_fa\": \"در اوستا فعل مرکب ā-marz- و نیز با واج‌افزایی -d- صورت گاهانی mərəžd- «بخشودن، رحم آوردن» (یسنا ۳۳؍۱۱) و mərəždika- «مهربان، رحمت» هست. همان دو مأخذی که نورایی می‌آورد این برداشت را تأیید می‌کنند: پوکورنی (۷۲۲) mərəždā- «بخشیدن» را زیر melǵ- می‌آورد و هرن (ص ۱۲، شمارهٔ ۴۹) می‌نویسد که معنای «بخشودن» در اوستا و هندی باستان از ریشهٔ «زدودن» با واج‌افزایی d پدید آمده است (به پیروی بارتولومه). ولی ایران‌شناسی امروز محتاط‌تر است: چونگ ریشهٔ جدای *maržd را می‌پذیرد و می‌گوید این ریشه هیچ هم‌ارزی هندواروپایی ندارد. دوم: صورت fra-â-marz تجزیهٔ شخصی نورایی است؛ صورت گواهی‌شده framarəz- با پیشوند frā- است، نه fra + ā. پس: با احتیاط پذیرفتنی است.\",\n  \"sources\": [U_AMORZ],\n  \"ref_check\": [\n    {\"ref\": \"POK:722\", \"status\": \"supports\", \"note\": \"POK_02.txt leaf 384 (printed 722): 'd-Präsens ai. mṛḍáti, mṛḍáyati ‚ist gnädig, verzeiht, verschont‘, av. mərəždā- ‚verzeihen‘ (mərəždika-, marzdika- ‚sich erbarmend‘, n. ‚Barmherzigkeit‘)' — the 'forgive' branch is expressly inside Pokorny's melǵ- entry.\"},\n    {\"ref\": \"HRN:12\", \"status\": \"supports\", \"note\": \"HRN.txt leaf 34 = printed p.12, entry 49: 'āmurzīden ‚verzeihen‘ ... aw. ā + √marz-, āmarəzən; phlw. āmurzītan, āmurz(i)šn, āmurzītār ‚verzeihen‘; ai. ā + √marj- ‚wegwischen‘ ... Im Awesta und Altindischen wird die Bedeutung ‚gnädig sein, verzeihen‘ durch das Wurzeldeterminativ d aus der √merǵ- ‚abwischen‘ gewonnen, vergl. aw. mərəzdātā, mərəsdika-, ai. mṛḍáti (Bartholomae BB. 13, 87)'.\"},\n    {\"ref\": \"BQT:1448\", \"status\": \"not_found\", \"note\": \"BQT vol. 3 pdf 239-241 (printed ≈1447-1449) carry فراز, فرازمان, فراسیون, فراسیاب — no فرامرز or آمرزیدن headword; a grep for فرامرز across BQT_v3_pages.txt finds it only as a metrical model ('بر وزن فرامرز') under کشاورز. The vol.3 scan's offset drifts and its OCR is poor, so the citation could not be verified either way.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"BRT\", \"where\": \"Bartholomae col. 1152 s.v. marəz-, with the infinitive mərəždẏai\", \"stance\": \"supports\", \"note\": \"the Avestan verb is entered with the preverb constructions (aipi, ā, fra, ni, vi) that give ā-marəz- and fra-marəz-; col. 1151 keeps marəd- ‚verderben‘ separate.\"},\n    {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007 p. 272 s.v. *maržd\", \"stance\": \"contradicts\", \"note\": \"'*maržd ‚to have pity, forgive‘. *AVESTAN: OAv. mərəžd- ‚to have pity‘ ... © The Ir. root *marzd has no IE correspondences ... «PIE — = LIV: 444 f. | Pok.: 737 f.' — i.e. a root of its own, not a branch of the 'wipe/milk' root, and referred to Pok. 737f. rather than 722.\"},\n    {\"src\": \"NYB\", \"where\": \"Nyberg II, index of Avestan forms (NYB_vol2_glossary.txt line 5227)\", \"stance\": \"supports\", \"note\": \"'mərəždā-, mərəždika-: āmuržītan' — Nyberg derives the Pahlavi verb from exactly the Avestan forms Nourai's box means.\"}\n  ]\n },\n {\n  \"id\": 4, \"lang\": \"Persian\", \"words\": \"âmorzîdan; Farâmarz\", \"verdict\": \"plausible\",\n  \"derivation\": \"آمرزیدن āmurzīdan 'to forgive' (with آمرزش āmurziš in the extras) is the direct continuation of MP āmurzītan / āmurz- (Book Pahlavi 'mwlc-ytn, Manichaean MP 'mwrz-), verbal noun āmurzišn, agent āmurzītār; the -u- comes from the labialization before the cluster -rz-, and the Avestan preverb ā- is preserved as آ-. MacKenzie lists 'āmurzīdan, āmurz- ... forgive, pity, have mercy' and the negative an-āmurzīd 'merciless'; Mo'in's footnote in Borhan-e Qate' s.v. آمرزش gives 'Pahlavi āmurzišn'. That link is confirmed. Farāmarz, the name of Rostam's son in the Shahnameh, is popularly and in the Persian dictionaries read as 'the (all-)forgiver', which is what the chart says; formally it is frā-marz (the prefix frā- + the marz- verb), not fra-ā-marz, and the semantics of Iranian heroic names being what they are, this reading is traditional rather than demonstrated — hence the reduced verdict for the node. The node carries no reference in the book.\",\n  \"derivation_fa\": \"«آمرزیدن» دنبالهٔ راستای فارسی میانهٔ āmurzītan/āmurz- (پهلوی کتابی 'mwlc-ytn) است، با اسم مصدر āmurzišn (> آمرزش) و فاعل āmurzītār؛ پیشوند اوستایی ā- در «آ» مانده و واکهٔ u پیش از خوشهٔ -rz- پدید آمده است. مکنزی مدخل 'āmurzīdan, āmurz- forgive, pity' را دارد و معین در حاشیهٔ برهان قاطع زیر «آمرزش» پهلوی āmurzišn را می‌آورد؛ این حلقه قطعی است. اما «فرامرز»: معنای «بسیاربخشاینده» در فرهنگ‌های فارسی مشهور است، ولی ساخت درست آن frā-marz است (پیشوند frā- + ریشهٔ marz-) نه fra-ā-marz، و این تفسیر سنتی است نه اثبات‌شده؛ از این رو حکم گره «پذیرفتنی با احتیاط» است.\",\n  \"sources\": [U_AMORZ],\n  \"ref_check\": [\n    {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"the node carries no reference in the book (refs=None); its parent box cites POK:722, BQT:1448 and HRN:12, which are checked at node #3, and HRN:12 is in fact an entry on this very Persian verb ('49. āmurzīden ‚verzeihen‘').\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary (PHD_mackenzie.txt lines 1016, 1056-1057)\", \"stance\": \"supports\", \"note\": \"'āmurzīdan, āmurz- [’mwlc-ytn | M ’mwrz-yd] forgive, pity, have mercy'; 'an-āmurzīd ... merciless'; 'an-āmurzišn ... mercilessness'.\"},\n    {\"src\": \"BQT\", \"where\": \"vol. 1 s.vv. آمرزش / آمرزیدن (BQT_v1_pages.txt lines 8763-8765)\", \"stance\": \"supports\", \"note\": \"'آمرزش - پهلوی āmurzišn ‹مناس ۲۹۵›، بخشیدن خدای تعالی گناه را بر بنده پس از مرگ، مغفرت، غفران «لغت‌نامه» رک: آمرزیدن'; the following entry 'آمرزیدن - بخشیدن خدای گناه بنده را پس از مرگ، غفران'.\"},\n    {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007 p. 272 s.v. *maržd\", \"stance\": \"supports\", \"note\": \"'*NWIR: ... (+ *ā-) NP amurzidan/amurz- ‚to forgive, absolve‘, borrowed into Bal. amurzit/amurz-, Qohr. āmerz-, Yzd. amorz-' and '*MIDDLE PERSIAN: (+ *ā-) MMP ’’()mwrz- BMP ’mwlc- /amurz-/ ‚to forgive, absolve‘' — supports the Persian form and its MP ancestor (though not its attachment to the 'milk' root).\"},\n    {\"src\": \"FSF\", \"where\": \"Noushin, Vazhe-namak / Farhang-e Shahnameh (FSF_pages.txt)\", \"stance\": \"silent\", \"note\": \"فرامرز occurs in the Shahnameh lines quoted in FSF (lines 3049, 3959, 11507 etc.) but the glossary has no etymological entry for the name.\"}\n  ]\n },\n {\n  \"id\": 5, \"lang\": \"Germanic\", \"words\": \"milkan\", \"verdict\": \"confirmed\",\n  \"derivation\": \"Proto-Germanic *melkan (strong verb, class III) 'to milk' is the full-grade *melg- of the root with Grimm's law g > k: OE melcan, OHG milchan/melchan, MHG mélken, ON mjólka, Du. melken. Watkins: 'Full-grade form *melg- in Germanic *melkan, to milk'. Pokorny p.723 has the same set ('ahd. milchu, melchan, ags. melcan ‚melken‘').\",\n  \"derivation_fa\": \"ژرمنی آغازین *melkan (فعل قوی ردهٔ سوم) «دوشیدن» از پایهٔ پر *melg- است و طبق قانون گریم g هندواروپایی در ژرمنی به k بدل شده است: انگلیسی کهن melcan، آلمانی عالی کهن melchan، نوردی کهن mjólka. ادعای نورایی درست است.\",\n  \"sources\": [U_MELG],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. melg-: 'I. 2. Full-grade form *melg- in Germanic *melkan, to milk, was contaminated with an unrelated noun for milk ... to form the blend *meluk- in: a. Old English meolc, milc, milk: MILK'.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"POK_02.txt leaf 384-385 (printed 723)\", \"stance\": \"supports\", \"note\": \"'ahd. milchu, melchan, ags. melcan ‚melken‘ (st. V.) ...' inside the melǵ- entry.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann s.v. melǵō and melǵos (IEC.txt lines 10547-10548)\", \"stance\": \"supports\", \"note\": \"'MHG mélken, mélchen, sv. 3 ‚milk; be in milk‘; OE melcan, sv. 3. ‚milk‘ ... ON mjólka' under melǵō; and separately melǵos 'milk' for the noun (Go. miluks, OE meolc).\"}\n  ]\n },\n {\n  \"id\": 6, \"lang\": \"English\", \"words\": \"milk\", \"verdict\": \"confirmed\",\n  \"derivation\": \"English milk continues OE meolc/milc (with OE milcian, meolcian 'to milk'), from Germanic *meluk-; the noun and the verb belong together in the chart's sense, but Watkins adds a caveat worth recording: the verb *melkan 'was contaminated with an unrelated noun for milk ... to form the blend *meluk-', and he files Greek gala / Latin lac beside it 'to mark the unexplained fact that no common Indo-European noun for milk can be reconstructed'. So English milk is the reflex of the Germanic noun built on the verb the chart draws, with that mixed history.\",\n  \"derivation_fa\": \"انگلیسی milk دنبالهٔ انگلیسی کهن meolc/milc از ژرمنی *meluk- است، که بر همان فعل *melkan ساخته شده است. یادآوری واتکینز را باید افزود: این فعل با اسمی بی‌ربط برای «شیر» آمیخته شده و صورت درهم‌آمیختهٔ *meluk- را پدید آورده، زیرا برای «شیر» اسم مشترک هندواروپایی بازسازی‌پذیر نیست (یونانی gala، لاتینی lac ریشهٔ دیگری دارند). ادعای نورایی درست است.\",\n  \"sources\": [U_MELG],\n  \"ref_check\": [\n    {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"the node carries no reference in the book (refs=None); its parent Germanic box cites AHD, whose melg- entry ends the chain at MILK.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. melg-, I.2 and II\", \"stance\": \"partial\", \"note\": \"'Old English meolc, milc, milk: MILK' — but II. is 'Included here to mark the unexplained fact that no common Indo-European noun for milk can be reconstructed'.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann s.v. melǵos (IEC.txt line 10548)\", \"stance\": \"supports\", \"note\": \"'melǵos, à, is ‚milk; milky sap, latex‘. Cf. melǵo, ml̥ǵó ... Go. miluks, f., MHG milich, milch, OE meolc, Du. melk, f. id.'\"}\n  ]\n },\n {\n  \"id\": 7, \"lang\": \"Latin\", \"words\": \"mulgĕre\", \"verdict\": \"confirmed\",\n  \"derivation\": \"Latin mulgeō, mulgēre, mulsi, mulctum 'to milk' is the zero-grade *ml̥g- with the -éye/o- stative-causative suffix (*ml̥g-éye- > *molgeīō > mulgeō, with the regular Latin o > u before l + consonant); its participle mulctus answers Skt. mṛṣṭá- 'wiped off'. Pokorny p.723 sets it out exactly so, and notes the transferred prō-mulgāre legem 'to promulgate a law' (literally 'to draw forth'). Nourai's macron-less 'mulgĕre' is just the book's way of marking the short e of the second conjugation.\",\n  \"derivation_fa\": \"لاتینی mulgeō / mulgēre «دوشیدن» از پایهٔ صفر *ml̥g- با پسوند -éye/o- است (*ml̥g-éye- > *molgeīō > mulgeō، با تبدیل قاعده‌مند o > u پیش از l + همخوان)؛ اسم مفعول آن mulctus برابر سنسکریت mṛṣṭá- «زدوده‌شده» است. پوکورنی (ص ۷۲۳) همین را می‌گوید. ادعای نورایی درست است.\",\n  \"sources\": [U_MELG],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. melg-: 'I. 1. Zero-grade form *ml̥g- in Latin mulgére, to milk: EMULSION.'\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"POK_02.txt leaf 385 (printed 723)\", \"stance\": \"supports\", \"note\": \"'lat. mulgeō, -ēre, mulsi, mulctus (= ai. mṛṣtá- ‚abgewischt‘) ‚melken‘ (aus *molgeĭiō : lit. málzau, málzyti), auch prō-mulgāre legem ‚ein Gesetz verkünden‘ (‚*hervorziehen‘); mulctra ‚Melkkübel‘.'\"},\n    {\"src\": \"IEC\", \"where\": \"Mann s.v. melǵō\", \"stance\": \"supports\", \"note\": \"'Lat. cf. (z-gde) mulgeo, id.' — the zero grade, as in Watkins.\"}\n  ]\n },\n {\n  \"id\": 8, \"lang\": \"English\", \"words\": \"emulsion\", \"verdict\": \"confirmed\",\n  \"derivation\": \"emulsion is a 17th-century learned formation: Modern Latin emulsio, -ōnis, built on Latin ēmulsus, the past participle of ēmulgēre 'to milk out, drain out' (ex- + mulgēre); the sense 'milky suspension of one liquid in another' preserves the milking image (an emulsion of almonds was originally a milk pressed out of them). Klein: 'emulsion, n., a milky fluid. — ModL. emulsio, gen. -ōnis, fr. L. emulsus, pp. of emulgere.'\",\n  \"derivation_fa\": \"emulsion ساخته‌ای عالمانه از سدهٔ هفدهم است: لاتینی نو emulsio از اسم مفعول لاتینی ēmulsus از فعل ēmulgēre «بیرون دوشیدن، کشیدن» (ex- + mulgēre)؛ معنای امروزین «تعلیق شیرمانند» همان تصویر دوشیدن را نگاه داشته است (شیرهٔ بادام را emulsio می‌گفتند). ادعای نورایی درست است.\",\n  \"sources\": [U_MELG],\n  \"ref_check\": [\n    {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"the node carries no reference in the book (refs=None); its parent Latin box cites AHD, whose melg- entry ends the Latin branch at EMULSION.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"KLN_1966 line 13030 s.v. emulsion\", \"stance\": \"supports\", \"note\": \"'emulsion, n., a milky fluid. — ModL. emulsio, gen. -ōnis, fr. L. emulsus, pp. of emulgere. See emulgent and -ion'.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. melg-, I.1\", \"stance\": \"supports\", \"note\": \"'Zero-grade form *ml̥g- in Latin mulgére, to milk: EMULSION.'\"}\n  ]\n }\n]\n\nout = {\n  \"pdf_page\": 330,\n  \"book_page\": 300,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-07\",\n  \"entries\": [e0, e1]\n}\n\nwith open(\"/home/sfmqrb/git/rishe/data/verification/page-330.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(out, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/mk330.py"
}
```


### [2026-09-07T16:35:11.669Z] TOOL RESULT

```
Exit code 1
  File "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/mk330.py", line 225
    {"ref": "HRN:214", "status": "supports", "note": "HRN.txt leaf 236 = printed p.214, entry 962: 'māliden ‚reiben, glätten‘ ... vergl. musten (No. 983). aw. √marz-, marəzaiti ‚fegt‘; phlv. kūn-marz, dastān-marz, d\u014ди́ak-marz Vd. 1(18), marz(i)šn ‚Coitus‘, marzītan ‚coitiren‘, mālītan, māl(i)šn; ai. √marj-, mārṣṭi ‚abwischen‘' — covers mālīdan, moštan and morz at once; footnote 2 there denies NP merz."},
                                                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 251-255: truncated \uXXXX escape
```


## [2026-09-07T16:35:17.452Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && python3 - <<'EOF'\np='mk330.py'\ns=open(p,encoding='utf-8').read()\ns=s.replace('d\\\\u014ди́ak-marz','dōšak-marz')\nopen(p,'w',encoding='utf-8').write(s)\nprint('d\\\\u014' in s)\nEOF\ngrep -c 'dōšak-marz' mk330.py; python3 mk330.py"
}
```


### [2026-09-07T16:35:19.003Z] TOOL RESULT

```
False
1
ok
```


## [2026-09-07T16:35:22.049Z] TOOL CALL #83: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-330.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 330"
}
```


### [2026-09-07T16:35:24.458Z] TOOL RESULT

```
JSON OK
nodes verified: 19/19
node verdicts: {'transcription_suspect': 1, 'plausible': 5, 'confirmed': 13}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 18, 'partial': 5, 'not_found': 2, 'not_checked': 3}
books consulted: {'supports': 37, 'partial': 5, 'silent': 7, 'contradicts': 1} | by book: {'KLN': 9, 'POK': 5, 'BQT': 4, 'CHEUNG': 4, 'AHD': 3, 'LKT': 3, 'NYB': 3, 'IEC': 3, 'DEV': 2, 'SKT': 2, 'BRT': 2, 'PHD': 2, 'WLD': 1, 'AFM': 1, 'LEW': 1, 'WEB': 1, 'HRN': 1, 'ARY': 1, 'HUB': 1, 'FSF': 1}
```


## [2026-09-07T16:35:50.194Z] AGENT

Done. `data/verification/page-330.json` written; `verify_check.py 330` reports **19/19 nodes, 0 PROBLEM lines**.

**Counts (pdf 330 / book 300):** roots 2 confirmed · nodes 13 confirmed, 5 plausible, 1 transcription_suspect · ref checks 18 supports / 5 partial / 2 not_found / 3 not_checked (nodes with `refs=None`).

**Flagged**
- **transcription_suspect — Mel 3, node #1 (Greek) "malaxos"**: no such Greek word; μαλακός is *malakos* (κ). Page image checked (`sources/refs/ocr/BOOK/330.png`) — the book itself prints "malaxos", so `error_in: book`, extraction faithful.
- No `disputed` nodes, and **no extraction errors**: every form, gloss, script and ref in the JSON matches the printed page.

**Plausible (worth knowing)**
- Mel 3 #2 Arabic "al-mâlâgmâ" — route Gk μάλαγμα → Ar. is confirmed (Klein 58, Lokotsch 1378, Mo'in in BQT p.2032, Wiktionary), but the form is Klein's *Syriac* malagmā with the Arabic article; real Arabic is al-malḡam.
- Mel 3 #10 Celtic *molto- → mel- is hedged in every source ("possibly/perhaps"); Klein gives no IE root at all.
- Mělg #1 (Av. marz/marez/mrz/mard) and #3 (ā-marz) hang on Pokorny's unified melǵ- 722; LIV/Cheung split *h₂merǵ- "wipe" from *h₂melǵ- "milk", and treat *maržd "forgive" as a separate root with no IE cognates. Pokorny flags the doubt himself on p.722, and Horn 12 backs Nourai's reading.
- "fra-â-marz" is Nourai's analysis; the attested Avestan is framarəz- (prefix frā-).

**Reference notes for the owner**: `BQT:1448` (Avestan ā-marz box) not found — vol. 3 pp. ~1447-1449 carry فراز/فراسیون, no فرامرز entry. `MON:4010` not locatable (local Mo'in text unpaginated). `SYN:569` is a page or two off Buck's 9.31 RUB, and Buck has no New Persian. `BQT:1948` and `BQT:2010` both verified and exactly right (Mo'in's مالیدن footnote; مشت = past stem of مالیدن); FFD:77 confirmed verbatim (*mṛš-ta- > mušt, *mard-a- < *marz-a- > māl).
