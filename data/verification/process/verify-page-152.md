# Verification process log — verify-page-152


## [2026-09-05T20:26:07.976Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 152 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-152.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-152.json. Write /home/sfmqrb/git/rishe/data/verification/page-152.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 152` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T20:26:09.565Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T20:26:10.267Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T20:26:10.283Z] TOOL RESULT

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


## [2026-09-05T20:26:10.637Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-152.txt"
}
```


### [2026-09-05T20:26:10.659Z] TOOL RESULT

```
1	=== PDF page 152 (book page 122) ===
2	--- entry 0 ---
3	ROOT [Indo-European] El 2, Elk, Eln : red or brown used in animal and tree names  (refs POK:302; KLN:509)
4	#1 (parent #0) [Avestan] refs=POK:302 | auruša : pale red, white
5	  #2 (parent #1) [Pahlavi] refs=BQT:55 | arŭs : white
6	    #3 (parent #2) [Persian] refs=BQT:55; MON:80 | âl «آل ۱» : pale red, pink ; âlgŭneh «آلگونه» : a pinkish face powder | extra: آله ، آلک ، آلا
7	#4 (parent #0) [Germanic] refs=AHD | elmo, almo, elwa : red, brown
8	  #5 (parent #4) [English] refs=None | elm, alder, elk
9	#6 (parent #0) [Germanic] refs=KLN:860 | lambiz : lamb
10	  #7 (parent #6) [English] refs=KLN:860 | lamb
11	--- entry 1 ---
12	ROOT [Indo-European] El 3, Elei, Lei, Olěna : to bend, elbow  (refs POK:308; KLN:509)
13	#1 (parent #0) [Avestan] refs=POK:308 | arethna : arm, elbow
14	  #2 (parent #1) [Persian] refs=MPP:79 | âryšnug : elbow
15	    #3 (parent #2) [Persian] refs=BQT:32; MPP:79 | ârenj «آرنج» : elbow | extra: آرن ، آران ، آرنگ
16	  #4 (parent #1) [Avestan] refs=POK:308 | frâ-râthni : forearm ☞Per 1
17	#5 (parent #0) [Old Persian] refs=MPP:79 | arašni : elbow
18	#6 (parent #0) [Germanic] refs=AHD | alino : forearm
19	  #7 (parent #6) [English] refs=None | elbow
20	--- entry 2 ---
21	ROOT Elei -> redirect to El 3
22	--- entry 3 ---
23	ROOT Elk -> redirect to El 2
24	--- entry 4 ---
25	ROOT Eln -> redirect to El 2
26	--- entry 5 ---
27	ROOT Elu -> redirect to Yb
28	--- entry 6 ---
29	ROOT Elu-ephas -> redirect to Yb
30	
```


## [2026-09-05T20:26:14.812Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-152.json",
 "description": "Read source JSON for page 152"
}
```


### [2026-09-05T20:26:14.849Z] TOOL RESULT

```
{
  "pdf_page": 152,
  "book_page": 122,
  "entries": [
    {
      "root": {
        "name": "El 2, Elk, Eln",
        "lang": "Indo-European",
        "refs": "POK:302; KLN:509",
        "gloss": "red or brown used in animal and tree names"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:302",
          "words": [
            {"translit": "auruša", "gloss": "pale red, white", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "BQT:55",
          "words": [
            {"translit": "arŭs", "gloss": "white", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:55; MON:80",
          "words": [
            {"translit": "âl", "gloss": "pale red, pink", "script": "آل ۱"},
            {"translit": "âlgŭneh", "gloss": "a pinkish face powder", "script": "آلگونه"}
          ],
          "script_extra": "آله ، آلک ، آلا",
          "note": null,
          "quote": {
            "text": "آن بناگوش کز صفا گویی - برکشیده است آلگونه به سیم",
            "poet": "Balkhî"
          }
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "elmo, almo, elwa", "gloss": "red, brown", "script": null}
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
            {"translit": "elm, alder, elk", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Germanic",
          "refs": "KLN:860",
          "words": [
            {"translit": "lambiz", "gloss": "lamb", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "English",
          "refs": "KLN:860",
          "words": [
            {"translit": "lamb", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "El 3, Elei, Lei, Olěna",
        "lang": "Indo-European",
        "refs": "POK:308; KLN:509",
        "gloss": "to bend, elbow"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:308",
          "words": [
            {"translit": "arethna", "gloss": "arm, elbow", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "MPP:79",
          "words": [
            {"translit": "âryšnug", "gloss": "elbow", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:32; MPP:79",
          "words": [
            {"translit": "ârenj", "gloss": "elbow", "script": "آرنج"}
          ],
          "script_extra": "آرن ، آران ، آرنگ",
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 1,
          "lang": "Avestan",
          "refs": "POK:308",
          "words": [
            {"translit": "frâ-râthni", "gloss": "forearm", "script": null, "see": ["Per 1"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "MPP:79",
          "words": [
            {"translit": "arašni", "gloss": "elbow", "script": null}
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
            {"translit": "alino", "gloss": "forearm", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "elbow", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {"name": "Elei", "redirect": "El 3"},
      "nodes": []
    },
    {
      "root": {"name": "Elk", "redirect": "El 2"},
      "nodes": []
    },
    {
      "root": {"name": "Eln", "redirect": "El 2"},
      "nodes": []
    },
    {
      "root": {"name": "Elu", "redirect": "Yb"},
      "nodes": []
    },
    {
      "root": {"name": "Elu-ephas", "redirect": "Yb"},
      "nodes": []
    }
  ]
}
```


## [2026-09-05T20:26:15.232Z] TOOL CALL #4: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo --- && cat tools/verify_check.py",
 "description": "List verification dir and read checker"
}
```


### [2026-09-05T20:26:15.281Z] TOOL RESULT

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
page-129.json
page-130.json
page-131.json
page-133.json
page-137.json
page-138.json
page-146.json
page-311.json
page-31.json
page-32.json
page-33.json
page-345.json
page-34.json
page-35.json
page-36.json
page-37.json
page-38.json
page-39.json
page-40.json
page-41.json
page-42.json
page-43.json
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


## [2026-09-05T20:26:18.723Z] TOOL CALL #5: Bash

```json
{
 "command": "head -c 4000 data/verification/page-124.json && echo && echo === && cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Sample verification file and source matrix"
}
```


### [2026-09-05T20:26:18.765Z] TOOL RESULT

```
Exit code 1
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
       
(eval):1: == not found
```


## [2026-09-05T20:26:21.125Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','BQT','MON','AHD','MPP','WLD','BRT','KNT','PHD','NYB','HRN','HUB','ARY','IEC','SYN','SKT','WEB','FSD','CHEUNG']:\n    v=d.get(k)\n    print(k, json.dumps(v,ensure_ascii=False)[:400] if v else 'MISSING')\n\"",
 "description": "Inspect refs_online entries"
}
```


### [2026-09-05T20:26:22.937Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
MPP {"title": "W. B. Henning, 'Mitteliranisch', Handbuch der Orientalistik I.4.1, Leiden 1958 (pp. 20-130)", "edition_found": "1958", "kind": "archive_djvu", "url": "https://archive.org/details/henning-1958-mitteliranisch", "identifier": "henning-1958-mitteliranisch", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/MPP.txt", "page_offset": "leaf = printed - 14 (e.g. leaf 7 = p.21)
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
CHEUNG MISSING
```


## [2026-09-05T20:26:28.356Z] TOOL CALL #7: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','MPP','BQT','MON','AHD','BRT','KNT','PHD','NYB','HRN','HUB','ARY','IEC','SYN','WLD','SKT']:\n    v=d.get(k)\n    if not v: continue\n    print('==',k)\n    for f in ['kind','local_file','page_offset','lookup_hint','scans']:\n        if f in v: print('  ',f,':',str(v[f])[:300])\n\"; ls data/verification/sources/refs/ | head -80",
 "description": "Get local file paths and offsets"
}
```


### [2026-09-05T20:26:30.033Z] TOOL RESULT

```
== POK
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt
   page_offset : POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' giv
== KLN
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt
   page_offset : KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/detai
   lookup_hint : Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
== MPP
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/MPP.txt
   page_offset : leaf = printed - 14 (e.g. leaf 7 = p.21). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Nourai's Table IV entry for MPP is garbled in the OCR (reads like a Persian title, 'Honari darbareh Zaban Farsi ... 1961'); Table III credits MPP to Henning, so this is most likely 'Mitteliranisch'. Treat identification as tentative and verify that cited page numbers fall in 20-130.
== BQT
   kind : archive_djvu+local_scan_ocr
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/re
   page_offset : vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vo
   lookup_hint : grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --d
   scans : [{'volume': '3', 'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', 'first_printed': 1208, 'last_printed': 1925, 'pdf_offset': -1205, 'page_map': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json', 'lang': 'fas', 'o
== MON
   kind : website+archive_djvu
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/in
   page_offset : None
   lookup_hint : Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbe
== AHD
   kind : archive_djvu+website+archive_restricted
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt
   page_offset : 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.
   lookup_hint : Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru
== BRT
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt
   page_offset : Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th 
   lookup_hint : Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops.
== KNT
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt
   page_offset : leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; section refs like '$147'. Nourai's page numbers should fall in 164-215 for lexicon citations.
== PHD
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt
   page_offset : leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB).
== NYB
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt
   page_offset : Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.
== HRN
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt
   page_offset : leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.
== HUB
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt
   page_offset : leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.
== ARY
   kind : local_scan_ocr
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt']
   page_offset : printed page = pdf page + 1
   lookup_hint : Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY
   scans : [{'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf', 'first_printed': 1, 'last_printed': 546, 'pdf_offset': -1, 'lang': 'fas+eng', 'ocr_text': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.tx
== IEC
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt
   page_offset : TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.
== SYN
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt
   page_offset : leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.
== WLD
   kind : archive_djvu
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe/data/verificat
   page_offset : Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.tx
   lookup_hint : Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP.
== SKT
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt
   page_offset : leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.
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
```


## [2026-09-05T20:27:18.225Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"lemma: el-\" POK_full.txt | head -30\necho \"=== page 302-308 lemmas\"\ngrep -n \"Page(s): 30[0-9]\" POK_full.txt | head -20",
 "description": "Grep Pokorny full for el- lemmas"
}
```


### [2026-09-05T20:27:18.286Z] TOOL RESULT

```
3967:Root/ lemma: ab'^o-{*heb'^o-)\ "white' derived from Root/ lemma: el-1, ol-, J-\ red, brown 
4448:lemma: el-3\ ol-\ "to rot, poison'. 
25153:Root /lemma: el-1, ol- e/-{*t>e/-) 
25265:darkness ', Old Prussian aglov\. "rain". Hence Root / lemma: el-1, ol- J- {* heghl-): red, 
25355:Root / lemma: el-2{*hel-2) 
25370:Root /lemma: el-3. ol-i^hel-3) 
25375:The extension of Root/ lemma: el-3\ ol-\ "to rot' into e/Ar"'^- caused k'^> p, bihen b > mb > 
25390:lemma: el-3: ol-\ (to rot, poison). 
25459:Root / lemma: el-5, ol-{*het-) 
25482:Root /lemma: el-6, el9-. la- ef-eu-fd'"-) 
25522:Root / lemma: el-7, els-, with -Ar-extension elk-, elak- 
25549:Root / lemma: el-8, elei-, lei- {*huel-) 
29278:Root / lemma: el- 
54041:lemma: el-1, ol-, J-\ red, brown (in names of trees and animals). 
55612:derived from a zero grade of Root/ lemma: el-6, eleh-: lah-, el-ehu-(6y-) : 'to drive; to 
55765:derived from a zero grade of Root/ lemma: el-6, eleh-: la-, el-ehu-(6y^ : "to drive; to 
70485:Root/ lemma: reu6!^-\ "red' derived from a zero grade of Root/ lemma: el-1, ol-, J-\ "red, 
=== page 302-308 lemmas
24796:Page(s): 301 
25106:Page(s): 301-302 
25351:Page(s): 302-304 
25368:Page(s): 304-305 
25429:Page(s): 305 
25457:Page(s): 306 
25480:Page(s): 306 
25520:Page(s): 306-307 
25547:Page(s): 307 
25713:Page(s): 307-309 
29296:Page(s): 309-310
```


## [2026-09-05T20:27:19.869Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"--- PHD arus/arisn\"; grep -n -i \"^arus\\|^arus \\|arus\\b\" PHD.txt | head -20\necho \"--- PHD arisn\"; grep -n -i \"arišn\\|arisn\\|ʾlyšn\" PHD.txt | head -20\necho \"--- PHD arenj\"; grep -n -i \"ārenǰ\\|arenj\\|ārenj\" PHD.txt | head",
 "description": "Grep MacKenzie"
}
```


### [2026-09-05T20:27:19.953Z] TOOL RESULT

```
--- PHD arus/arisn
214:a-pus [' BRE] without a son, childless. ár-, v. árdan. 5 āranj "Inc | N ~] elbow.. 9-43. "Ant *a-rāst Prst'] untruth. ārāstan, ārāy- [Pstn!,^Pd- | N ~] prepare, arrange, adorn. ~ién: arrangement, adornment. a-rawüg [”/wbk!] immobile. Ard р | M?yrd, N ~] a goddess; cal. 25th day. ard [KHM A < А gm; п | N ~] flour. агаа [py | (M rd?w)] righteous, truthful. ardan, ār- [THNN-tn' < А V thn; ?l-tn'] grind, mill. ardāyīh ['i?dyh | M?rd?yyh] righteousness, rectitude. ardig [/tyk! | M ?rdyg] battle. ardikkar рук], -kl | M?rdyqr] warlike, warrior. ~ith: doing battle. arduš [”ldwš = Av. aroduš-] a degree of sin. Ardwahišt Prtwhst' | M ?rdywhyst, (N urdībihist)] Right, the second Amahraspand, guardian of fire; cal. 2nd month; 3rd day. arešk [lysk' | M ()rysk, N rašk] envy, jealousy. ~én [-yn'] envious, jealous. ārešn Pim! | M ”7ysn-, N (a)rif] cubit. aryand [?/епа | N ~] horrible. arģawān [*/gwk'*n! | N aryawān] purple. armēšt ["/myst'] inactive, infirm. ~ih: infirmity. armēšt-ģāh [-g’s] secluded place for the infirm. агбуї&п [/wdšn'] growth. ~ig [-y&!] growing, vegetable. ars Dis | M?rs, N ~] tear (drop). artēštār УЯ? | N artēšdār!] warrior. „īh: warriorhood. arus [2/00] white. arwand [wnd] swift, valiant; river Orontes. ~ih: swiftness, valour. arwés [lwys | M ?rwys, N ~] rope. arz [KSP! < А Ар; с | N ~] worth, value. Arzah [Iz h == Av. arazahi-] the eastern continent of the earth. arzan [PE < А prg’; len! | N <) millet. arzàn Plen | M *rz'n, N ~] valuable, worthy. ~ig [-yk'] worthy. ~igih: value, worth, worthiness. arzidan, arz- [?/с-уїп! | N ~] be worth. ~išn: value, worth. arziz (сус | M ?rzyz, N ~] tin, lead. —ën [-yn'] tin, leaden. ārzōg Picwk! | M'wrzwg, N àrzó] desire, lust,
4306:which čē, kadam, kadār, ke. whichever kadām-iz-ē(w). whip aštar, tāzānag. whirlwind wād-girdag. white spēd, arus; (n.) spēdag. who kē, kadār.
--- PHD arisn
221:aswār [252002/, ?shw'l | N suwār] horseman, rider. ~th: horsemanship, riding. āsyāb [?sy?5] (water-)mill. āsyāg [sy’k!' | N asya] mill(-stone). aš [P$] the evil eye. āšixtan, āšinj- Pšyhtn!, ”*šnc- | P ?fyxt] pour, flow, overflow. aškamb [KLSE < A krs’; ”$kmb! | M *fkmb, N šikam] belly, womb. ~ag [-k! | N šikamba] = aškamb. āškārāg (34 1Q)k! | M sq?rg, N āškārā] obvious, evident. ~ih: revelation, confession. aškaragënidan [$k*Pkyn-ytn!] reveal, confess. aškūb рор | N dškē(b)) roof, ceiling. aškom(b) [’skwm(b')] = a$kamb. ašmā [LKWM < А l-kwm | MO fm'(h), N šumā] you (?1.). āšnāg Pwk! | M ”šYg, N ama] known. āšnawāģ [?$nw?k! | M ?snz?g, N šunawā] hearing. —ih: (sense of) hearing. āšnūdan, āšnaw- [OSMEN-tn! < А « ўт; топі | M? fnwdn, ?fnw-, N funüdan, funaw-] hear, understand. ~išn: hearing. або [šwk! = Av. ašawa] righteous. āšūb [>р | P swb, N ~] disturbance, turmoil. Aštād [s?t! | Md, N ~] the goddess Rectitude; cal. 26th day. aštag [štk'] messenger. ~th: mission. aštar РД whip. āštīh Pštyh | M 7st, N āštī] peace. Ašwahišt Piwhst'] = Ardwahišt. āšyān(ag) ['syd?n(k) | (M ?hy*ng), N ašyana] nest, lair. ātaxš Pths = Av. ātarš | N ātaš] fire. āwādaģ Pwb'tk! | J ?zo?d] generation. āwahan [wb’hn'] fortified place, stronghold. амат ['wbm | M ?w^m] time, season. -āwand [ла | M 2w(y)nd] suffix forming adjectives of quality. awar [LPNME < A I-pn-h | M ?wr] hither! come! awar-, v. āwurdan. a-wardàg ['wit?k&!] undeviating. a-wardisnig [?wltsnyk'] immutable. Аһ: immutability. āwarišn [zoblfn! | M *wryšn) abode, home. a-warzid [Pwicyt'] untilled. *Aiwas-, v. tāwištan. ама [Pc | N ~] voice, sound. a-wazisnig ['wcfnyk!] immobile. āwēnīdan, āwēn- ['wyn-ytn! | (P ?bzoyn-)] admonish, blame. ~i$n: blame, reproach.
607:~išn: conquest, destruction. wanigarih [4W BDN-, wny-klyh] waste. wany [A(W)BDN' < APbdn | M wny] lost, destroyed. wany(b)ūdīh [4WBDN'butyh, -YHWWNtyh | M wny(b)wdyh] destruction, ruination. iwar [wl | M wr, N bar] breast. *war [w/] lake. Zwar [wl] oath, ordeal. ‘war [wl] shelter, enclosure. war-, v. waridan. warāy [wl”g | J bry] crow. waran [win'] desire, lust. warān [wi’n'] ram. wārān [w’Pn' | M wrn, N bārān] rain. waranig [wlnyk'] greedy. ~ih: greed, lust. waranig [wL nyk! | N bārānī) rain(y). warāz [wl”c | N gurāz] boar. war-čašm [wicfm] with eye(s) in the breast. ward-, v. 'waštan. lwardag [witk! | M wrdg, N barda] captive, prisoner. ~ih: captivity. *warda$ [witk'] on heat (female animal). ~ih: heat. *wardānāģ (wi? mk! | N gardana] (roasting) spit. wardénidan, wardén- [wityn-ytn! | (N gardànidan)] cause to turn; change, alter. wardišn [witšn! | M wrdyšn, N дака] turning, change, metamorphosis. ~ig [-y%!] transient, changeable. ~(ig)ih : transience, mutability. wardyün [wltywn! | P wrdywn, N gardiin] vehicle, carriage, chariot. warg [wlg | N barg] leaf. wārīdan, wār- [w?l-ytn' | M w’r-yst, N bàáridan] rain. warišn [wilsn'] conduct, behaviour. lwarm [wlm | N barm] memory. — kardan: learn by heart, memorize. *warm [wim | N barm] pool, reservoir. wārom [w’lwm] mind. warómand [wl’wmnd] doubtful. ih: doubt. warr [LBWS Y A < A lbw?] wool; garment. warrag [КММА < ?; wlk! | M wrg, N barra] lamb, ram; astr. Aries. wars [wils] hair. lwarz [wle | M wrz, N barz] work, agriculture. *warz [wic | М wrc/z] miracle, miraculous power. *warz [wlz | N gurz] club, mace.
698:abode šāwarišn,  bunag, nišēmag; (daevic) dwārišn.
951:bearing barišn.
967:behaviour barišn, rawišnīh, warišn.
1365:consumption xwarišnīh,
1388:cooling afsarišn.
1515:decision wizarišn, wizir.
1696:drink xwarišn; alcoholic — hur.
1731:eating xwarišnīh; (daevic) jēyišn.
1735:edible xwarišnīg, xwārēn, xwardār.
1738:education frahang, parwarišn.
1990:food čāštag, nan, pih, xwār, xwardig, xwarišn; ~ and drink xwār-bār.
2298:home āwarišn, mëhan; (daevic) gilis- tag.
2943:nourishment parwül(i$n), parwarišn.
3356:reflection handēšišn, uskarišn(ih).
3808:stealing apparišn.
4322:wiping awestarišn.
4667:parwar- parwarisn Frawardin Frawardīgān fraward parwardan frawardag franam- parwast parwastan franaftan frušag
5146:nifrin wafrūnag nifrīdag Obad-/oft-1 Obastan! nibard- nibardīdan nibard nibardag nibastan wabz wafišn xwest xwestant nibistan 1-2paft waz- wizār wizür- wizarisn wizārdan wizārdwars wizīh-
--- PHD arenj
```


## [2026-09-05T20:27:27.344Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '25153,25360p' POK_full.txt",
 "description": "Pokorny el-1 lemma"
}
```


### [2026-09-05T20:27:27.426Z] TOOL RESULT

```
Root /lemma: el-1, ol- e/-{*t>e/-) 

Meaning: red, brown (in names of trees and animals) 

Note: mostly A, u-and n-{a\so m-) stem, rare from the bare root, which seems extended 

then with ^or R. In names of swan and other sea birds the meaning is "white, gleaming', as 

in aZ-bho- "white' refined names (above S. 30 f), thus both roots are probably identical 

originally. 

Material: 

A. Adjektiva: 

Old Indie a/ic//7a-/7 "reddish, golden ', arusa-h^ fire-color ', Avestan a^/Y/s5- "white'; 

Germanic *elwa- "brown, yellow' in Old High German elo{elawer). Middle High German 
el{elwei); 

compare also gall. VN Helvii, Helvetii, perhaps also Swiss FIN llfis{*Elvisia). B. e/-in 
tree names for " alder ', "elm' and " juniper ': 



1. ■ alder' 

Latin alnus^ alder' (from *a/snos or *alenos, the aniaut a/goes back to older el-)\ 

maked. (Illyrian?) aAi^a {*elisa) " abele, white poplar'; 

Hittite: ^'Salanzan- c. ' a tree and its wood ' (other etymologies in Tischler 15) 

after Bertoldi (ZfceltPh. 17, 184 ff.) places proto gall. *alisa^ alder ' in many PN and FIN; 
besides die later dominant meaning " service tree ' in *alisia, French alise. Modern High 
German Else, lllyrian-Ligurian origin is proved through frequent occurence in Corsica (FIN 
Aliso, A//stro etc., a/zo' alder '); compare gall. PN A//s/a, FIN Alisontia, French Aussonce, 
Auzance, Modern High German Elsenz, etc.; 

for Gothic is according to span, aliso " alder ' ein *alisa " alder ' must be assumed; Old 
High German eliraav\6 with metathesis erila. Modern High German Eller, Erie, mndd. eire 
{*alizd), else {* aliso), Dutch els ds.. Old Norse elrln., eirlrm.; air, glr{*aluz-) ds., Old 
English alor6s.; Indo Germanic eroot is guaranteed through Old \ce\an6'\c Jglstr {* elustra) 
' alder ' and llsfn" willow, Salix pentandra' {* ells-tr-Jo-; Middle High German dial, hllster, 
halster6s. with secondary /?, as Swedish {h)llstei); an adj. formation is Old High German 
e/y/T? "of alder '; perhaps to compare also Old English ellen, ellern, engl. e/o'e/'" elder'; 

It is to be compared further Lithuanian alksnls, elksnls, Latvian alksnls. East Latvian 
elksnis. East Lithuanian aliksnls. Old Prussian alskande {Hs. abskande) " alder', yet one 
will have to assume various basic forms *alsnia, *elsnia (with ablaut) and *allsnla 
(Trautmann Bsl. Wb. 6, yet compare v. d. Osten-Sacken IF. 33, 192). The suffix from Old 
Prussian alskande reminds after Trautmann an Slavic *jagngdb ' black poplar '; 

also the Slavic shows old e/oablaut; go back to Slavic *Jelbcha {*ellsa): Old Bulgarian 
jelbcha^ alder', Bulgarian (j)elha6s.; on Slavic *olbcha {*ollsa): poln. olcha, russ. olbcha^ 
alder' (dial, also elcha, elocha, volbcha); 

The origin of labialized Old laryngeals: 

common Armenian Celtic *hue- > gw- > g- ; Slavic Albanian gw- > v-. 

Maybe alb. verr^ alder' : russ. dial, also elcha, elocha, volbcha^ alder'. 

Slavic *jelbsa, respectively *olbsa\\es before in Serbo-Croatian dial. ye/s'a (compare yie/^s/e 
" alder bush ' from *jelbSbje), sloven. y^7s5, dial, gisa, jolsa 6s., russ. dial, olbsa, olbsfna, 
elbs/na and les/na {compare Pedersen KZ. 38, 310, 317). 



Common /7->y- Slavic Albanian; h->j-, y-0\d Indie Tocharian. 

As derived Adj. appears Balto-Slavic *al(i)seina- : Lithuanian alksninis. East Lithuanian 
aliksninis. Old Bulgarian ye/6S/>7b (compare Old High German erITn). 

2. "elm": elem-. 
Note: 

-m- suffix is of lllyrian Greek origin. 

Latin u/mus ^an elm, elm-tree' goes to Indo Germanic *o/-mo-s or to zero grades */-md-s 
back; full grade (but s. S. 309) in Middle Irish /e/77"elm' {*lemos). 

The origin of labialized Old laryngeals: 

common Armenian Celtic *hue- > gw- > g- ; Latin gw- > u-. 

There, one puts gall. Lemo-, L/mo- etc.; cymr. //tyyf'elm' falls out of the frame, that due to 
the basic form */e/ma must be placed probably to e/e/- 'bend' (see 309). 

Compare further Old High German e/mboum ' e\m' , Old Norse a/mr{\N\t\r\ ograde). 
Middle Low German Old English elm 6s:, Modern High German Ulme, Middle High 
German ^//77i?c»^/77 should derive from Latin (Kluge), what is not sure at all, because 
compare Old English ulmtreow. Middle Low German olm, so that possibly Germanic 
contains all three Abl. -grades; russ. flim, G. f/'ma etc. derives from Germanic 

3. juniper and other conifers: e/-eu-, el-en-. 
Armenian eievin. Gen. eievni^ spruce, cedar'; 
perhaps gr. sAarn "fir, spruce' {*el-n-ta)\ 

extended in -g'- suffix: 

Lithuanian {*hielge) egliusru. (for *eA/s after egle^W) " juniper ', Latvian pa-egle\. ds.; 

Note: 

The name of juniper derived from the concept of "smoking wood, dark color' hence 
Lithuanian egliusxw. is the closest form to primordial root. Armenian eievin. Gen. eievni^ 
spruce, cedar' similar to Armenian *alj- in aijaij, aijamuijkh^ 6,2xVx\es^ : Gr. C(xAu(; " fog. 



darkness ', Old Prussian aglov\. "rain". Hence Root / lemma: el-1, ol- J- {* heghl-): red, 
brown (in names of trees and animals), derived from Root/ lemma: aghl(u)- {* heghel-): 
rainy weather. 

Slavic *elovbCb ' juniper ' in Czech Jalovec, russ.ya/oi/ecds., besides /7-forms in wruss. 
jel-en-ec etc. 

C. e/-in animal names: 

1 . 'deer and similar to animal.' 

a. with X'-forms (Germanic Slavic olRis). 

Old High German elho, elaho^e\k\ Old English eolh, engl. elk6s.\ with o-gradation 
{*olRfs) Old Norse e/gr6s.; from an initial stressed form Germanic *ai^/s derives Latin 
a/ces, alcei. and gr. qAkh f. 'elk'; russ. lost, Czech los, poln. /os. Upper Serbian /os'elk' 
(from *olkis)\ zero grade: Old \n6\c rsa-h rsya-h ' male antelope ', pam. ms'wild mountain 
sheep '. 

b. stem e/-en-, el-Q-{el9nT hind '); zero grade l-6n-: 
Armenian ein. Gen. e///7'deer'; 

gr. sAacpoc; m. f. 'deer' ( *eln-b'^o-s), zkKoc, 'young deer' ( *elno-s)\ 

cymr. elain^ hind ' {*elanT= Old Bulgarian a/b/7/; /an/6s.), Old Irish e//t'roe deer' {*eln-tfj 
perhaps also Middle Irish elli. 'herd' ( *elna)\ ablaut. *lon- in Gaelic lonxu. ' elk '; gall, 
month name Elembiu{: gr. D'EAacpnpoAicbv); 

Lithuanian e/n/s and einias. Old Lithuanian ellenisxw. 'deer' (out of it Middle High 
German elent. Modern High German Elen), Latvian a7/7/5'elk'; 

Old Church Slavic (/J^/ent'deer' (older consonant-stem), russ. o/ent etc. 

Femin. *e/a/7/"-and *a/9nr-' hind ' in: 

Lithuanian e/neand aine ds.. Old Prussian a/ae 'animal'; 

Old Bulgarian altni, lani^ hind ' (= cymr. elain), russ. (with junction in die /^Dekl.) lant, 
Czech lanfeic; 



in addition furtlier very probably as 7-c»/7-bhc»-s (witli tlie same suffix as sAacpoq) also 
Gothic /a/77i6' "sheep', Old Norse /amb'\amb, sheep', Old High German /amblamb' (mostly 
neutr. -es-stem, what appears basic Germanic innovation after calf); 

Maybe Alb. lope^ coW {*lapa), Latvian A/ops "cattle'; also Swiss loobe, lioba^ coW see Root 
/ lemma: lap-: cow 

As metathesis from *elen- understands Niedermann lA. 18, 78 f. gr. es/ekoq V£(3p6(; Hes.; 
Latin {h)inuleus borrowed out of it. 

2. waterfowl: el-, ol-, with guttural extension or r-and ^-stem. 

Gr. 1 . ikta f. " a kind of owl, a small marsh bird ' (to zKoq, n. "swamp, marsh'?); 2. 
£Au)piO(; " water-bird ' (not quite supported word, leg. ipu^bxoc,!); 

Latin o/or^ swan' {*eldr)\ 

Old Irish elae {*elouio-) ds., with /r-suffix acorn, elerhc, cymr. alarch {a-ixom e-, s. 
Pedersen KG. I 40); 

Old Swedish and Swedish Dialectal alle, al(l)a, a{l) (Finnish loanword alio), Swedish 
written-linguistic alfager long-tailed duck ', Norwegian Dialectal hav-al, -ella; with Indo 
Germanic ^^derivative: Old Norse alka "black and white North Atlantic auk, razorbill, 
penguin '; a//ra could also belong to onomatopoeic word roots el-, c»/-"cry' (see 306); 

Maybe alb. Geg alka, alke^ white cream, dirt, spot, fat of wool'. 

because Indo Germanic -k(o)- suf^\x is common in animal names (above corn, elerhc), 
could be also added perhaps: gr. aAKucbv " kingfisher ' (Latin alcedoseerws reshaped out 
of it), Swiss wTss-eIg av\6 bircb-llge irom variant kinds of duck. 

3. "polecat'? 

Perhaps here the 1 . component from Old High German illi(n)fTso, Modern High German 
litis an6 Old High German elledJso {Modern High German dial, elledels), ndd. ullek 
"polecat', if from * lllit-wTso {\.o Modern High German Wiesel); Germanic *ella- from *el-na-, 
because of the red-yellow hair; different sees Kluge''"' therein Old High German ellenti 
(from elllenti, see above S. 25) " strange '. 

References: WP. I 151 f., 154 f., WH. I 28, 31, Specht Dekl. 37, 58 f., 116, Trautmann 6, 
68 f., Pokorny Urillyrier 137 f. 



Page(s): 302-304 



Root / lemma: el-2{*hel-2) 
Meaning: to lie 

Material: After Persson Wortf. 743 has defended a Indo Germanic root eZ-'rest' and base 
*e/r-with consecutive pattern: Old Indie ilayati^ stands still, gets some peace ' {ilayati 
should be faulty spelling), an-ilaya-h^ restless, not still', wherefore probably Old Indie
```


## [2026-09-05T20:27:37.984Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '25549,25720p' POK_full.txt",
 "description": "Pokorny el-8 lemma"
}
```


### [2026-09-05T20:27:38.044Z] TOOL RESULT

```
Root / lemma: el-8, elei-, lei- {*huel-) 

Meaning: to bow, bend; elbow, *rainbow 

Material: A. Here names position themselves at first for "elbow' and "ulna, ell': 

Gr. (JbAEvri "elbow', tbAr|v, -£voq ds.; wAEKpavov (from wAsvo-Kpavov through remote 
dissimilation, compare Brugmann Ber. d. sachs. Ges. d. W. 1901, 31 ff.) " the point of the 
elbow '; wAAov Tr|v tou (3paxiovo(; Kaijnrjv Hes.; 

Latin ulna {irom *olina) " elbow, arm; an ell '; 

Old Irish uilenn^ elbow ', (common Celtic -ns-, -nt- > -nn-). Middle Irish u/7//nd^e\bo\N' (- 
/A from -/n- the syncopated case, compare Pedersen KG. II 59), cymr. e//n, acorn. e//n, 
bret. ////7 'elbow' {*olTna)\ 

Gothic: aleina^ \}\na, ell' shows the same long middle vowel, however, Germanic forms 
have remaining short middle vowel: Old English e//7(engl. ell). Old High German elina. 
Middle High German elline, eine. Modern High German Elle; Old Norse shows form 
variegation: Old Icelandic seldom alen {0\d Norwegian also alun) with preserved middle 
vowel, otherwise gin, eln{gln, ain); 

simple root *dle-'\n Old Indie aratnf-hm. "elbow', Avestan ara^na- ds. fra-ra^n/- 'u\na, 
eir. Old pers. arasnis ds.; 

in alb. /ereGeg /ans' arm from elbow to wrist, ell ' {*/ena, yet compare Pedersen KZ. 
33, 544) lacks the aniaut vowel. 

Note: alb. Geg fans " ell ' derived from zero grade of * a/ana 'e\bo\N' 

B. The same root placed furthermore in: Old Indie anf-hm. " pin, leg part about the knee 
' {^arni-, Indo Germanic *elni- or *dlni-), arala-h " bent, curved ', artnf end of curve ', 



probably also in alaka-^ hair lock ', perhaps in ala-valam^ vemeTun^jrT^i^vu 
Baumes, urn das fur den Baumbestimmte Wasser einzufangen '; 



rzel eines 



Armenian c»//7(Gen. oHn) "dorsal vertebrae, backbone, spine, shoulder', i//iy "backbone, 
spine, shoulder' (from Indo Germanic *c»/e/7, respectively *dlen)\ further Armenian a/e//7 
(Gen. aieian) "bow, rainbow', //(Gen. ilo}/) " spindle, arrow, spindle ' {*e/o-), ///kds.; 

Albanian mixed etymology: alb. ul-ber, ylber, ilber^ rainbow ' : Armenian afefn {Gen. 
aieian) "bow, rainbow' contaminated by a mistranslation of Romanian {* curcu-beu) 
curcubeu : Sardinian {* circu-voglia), circuvoglia, {* circu-vrongia) circuvrongia^ rainbow', 
Sardinian Logudoresu arcu de chelu, {* arcu-baradu) arcubaradu, Sicilian {* arcu-bbalenu) 
arcubba/enu 'ra\nbo\N (arch of the whale)', Welsh bwa'rarch, Romagnolo {* arco-balein) 
arcobalein, Italian {* arco-balend) arco-ba/eno' ra\nbo\N (arch of the whale)'. 

'Circu' means 'circle' in Sardinian, as 'cere' (> Latin circus) means 'circle' in Romanian 
(circle > arc > rainbow). (Hence alb. ylber 'rainbow' is a compound of a 1 foreign word + 2 
explanatory word). 

cymr. o/wyn {*oleina) "wheel'; 

Germanic ablaut. */un/-\n Old High German Old Saxon Middle High German /un' axle 
pin, linchpin ', Modern High German tonnage/, compare Old High German luning^ linchpin 
', Old English /yn/-bor' borer', next to which a s-derivative Old English /yn/s, asachs. lunisa. 
Middle Low German luns(e). Modern High German Lunse; 

Lithuanian lusis^ axle pin ' (Specht Dekl. 100, 125, 163); 

Old Bulgarian /an/ta ' cbeeW {*olnita). 

C. further formations el-eq-: 

1 . In names for elbow, arm, now and then also other body parts: 

Armenian c»/o/r'"shinbone, leg' {*eloq-ox *oloq-); 

gr. [aA^ Koi] aAa^ nrixu(;, 'AGapavojv Hes.; 

Lithuanian uolektisi., Latvian uolekts^eW (originally conservative stem *dlekt-); 

Maybe alb. i//c»/r "lame' : Middle Irish /c>5c"lame'. 

Old Prussian woaltis, M/o///5"ulna, ell, forearm' {*dlkt-); 



The origin of labialized Old laryngeals: 

common Armenian Celtic *hue- > gw- > g- ; Old Prussian Lithuanian Tocharian gw- > w-. 

Lithuanian alkune, elkunei.. Old Prussian a/kun/s'e\bo\N', Latvian e/ksn. e/kuons6s., Old 
Bulgarian /akbtb, russ. /okotb ' ulna, ell ' ( *o/kb-tb); russ. dial. a/bc/k{7) " ankle, ankle 
bone; heel '. 

2. Gr. ko^oq " bent, dislocated, slantwise ' (Middle Irish /c»5C "lame'), Asxpioc; "slant, 
skew, quer' {*KzKO-pioq), A£xpi<; "quer', AiKpi(pi(; "quer' (diss, from *Aixpicpi(;, Saussure MSL. 
7, 91, Hirt IF. 12, 226; whose /of the first syllable probably rather from £ assimilated as 
with I = e, as indeed:) AiKpoi Hes. besides AsKpoi " the prongs of deer antlers ', Ai^, Aiy^ 
nAayioc; Hes., as " incurvation, trough ' Aekoc; n., Aekk;, AsKOvri "trough, platter '; 

cymr. //echwedd ^s\ope, inclination ', gall. Lexovii, L/xov/7VH; Middle Irish /osc'lame'; 

Latin //c/nus^bent or turned upward, having crooked horns' (from *lecinos), lanx, -cis^ a 
plate, platter; the scale of a balance ' (probably also lacuseic, s. *laqu-)\ 

quite dubious is the interpretation from Old Bulgarian /0/70 "bosom, lap' etc. from *loq-s- 
no-^ incurvation ', also from Bulgarian /onecetc. "pot, pan' from /oq-s-no- {see Berneker 
732). 

D. To /e/-"bend' belong also: 

Perhaps Gothic undar/e/ja' lowest, faintest'; 

Latvian /ey5"valley, lowland, depression', /ejs' situated low'. 

1 . With /7^suffixes: 

presumably gr. Asiijcbv "meadow' ("*lowland, depression, indentation '), k\[}r\\/ " harbor ', 
Thessalian " market ' ("*bay'), Aipvri "sea, pond, pool' ("*immersion, depression bent 
inwards, dent'); 

cymr. //wyrelm' {* lei-ma), nir. PN Liamhain {\.o *ITamh6s.), perhaps zero grade Middle 
Irish /emds. {*limo-), nir. PN Leamha/n {whether not from *lemo-, see below el-f); 

Latin //777£/s "sidelong, askew, aslant, askance; an apron crossed with purple; slime, 
mud, mire', ITmes -itis " a path, passage, road, way, track ', Oscan lifmftum " a path, 
passage, road, way, track ', ITmen^ doorsill ' ("*crossbar, crossbeam'); 



Old Norse limr{u-s\.exr\) f. "limb, member, thin twig, branch' ("*pliable'), limi. ds., ///77n. " 
the fine branches which carry the foliage ', Old English lim n. "limb, member, twig, branch', 
zero grade Old Norse lfmivc\. " trunk, Korperstatur ' (Lithuanian liemuovn. "tree truck, 
Korperstatur', originally " round timber, curvature '?). 

Maybe alb. Geg {*lemes) /amsh^baW of (pliable) wool, globe of earth, pool, spellet'. 

2. With /■-suffix: perhaps alb. A///'-/e "valley' from prefix ke+li-r. 

3. With ^suffixes: 

Latin lituus^ a crooked staff borne by an augur, augur's crook, crosier, augural wand ' 
(being based on *li-tu-s^ curvature '); 

Gothic //^^5"limb, member'. Old Norse lidr {u-s\.exr\) "joint, limb, member, curvature, 
bay'. Old English lid, liodu- m.. Old Saxon ////? "joint, limb, member'. Old High German lid. 
Middle High German ///, lldesxw. n. "ds., part, piece' (s-stem), wherefore Old Norse lida 
"bend, bow'. Old English alldian^ dismember, separate'. Old High German lidon^ cut in 
pieces ' as well as Old Norse lldugr^ {i\ey\b\e) a little bit movable, free, unhindered'. Middle 
High German ledec^ available, single, free, unhindered '; 

Tocharian AB ///- "go away, die, tumble, fall down'. 

E. guttural extensions: 

Latin oblTquus^ sidelong, slanting, awry, oblique, crosswise, skew' {-uo- could be suffix, 
compare curvus), ilquis ds. (probably with /), liicium' in weaving, the thrum or perhaps a 
leash; in gen., a thread, a cross thread; plur., the woof ' ("*weft'), llxulae " a round pancake 
made of flour, cheese, and water'; 

perhaps cymr. Ilwyg {*lei-ko-) " balky horse', bret. loeg-rin^au askance look' (Loth RC 
42, 370 f). 

References: WP. I 156 ff., WH. I 744, 761, 798. 
Page(s): 307-309 

Root / lemma: e-3, ei-, /-, fem. T-{*he-3) 
Meaning: this, etc. (demonstrative stem); one 



Note: {e, /probably originally demonstrative particle). To /-is joined the relative stem^o-.
```


## [2026-09-05T20:27:53.534Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN elm\"; grep -n \"^elm,\" KLN_1966.txt | head\necho \"=== KLN elbow\"; grep -n \"^elbow,\" KLN_1966.txt | head\necho \"=== KLN elk\"; grep -n \"^elk,\" KLN_1966.txt | head\necho \"=== KLN lamb\"; grep -n \"^lamb,\" KLN_1966.txt | head\necho \"=== KLN alder\"; grep -n \"^alder,\" KLN_1966.txt | head\necho \"=== KLN ell\"; grep -n \"^ell,\" KLN_1966.txt | head",
 "description": "Grep Klein headwords"
}
```


### [2026-09-05T20:27:53.658Z] TOOL RESULT

```
=== KLN elm
=== KLN elbow
=== KLN elk
12842:elk,  n.,  the  largest  existing  deer.  —  ON.  elgr, rel.  to  OE.  eolh,  OHG.  elaho,  MHG.  elhe,  G. Elch;  Gk.  itXxT)  and  L.  alces,  ‘elk’,  are  Teut. loan  words.  The  above  Teut.  words  are  cogn. with  OI.  fsah,  fsyah,  ‘buck  of  the  antelope’, Russ,  losu,  Czech  los,  etc.,  ‘elk’.  These  words derive  fr.  I.-E.  base  *elk-,  a  -^-enlargement  of base  *el-,  ‘brown’.  For  derivatives  of  *eln-, -n-enlargement  of  base  *-<?/-,  see  eland  and  cp. words  there  referred  to.  Cp.  also  Alces  and  the first  element  in  hellebore.
=== KLN lamb
21040:lamb,  n.  —  ME.  lamb,  lomb,  fr.  OE.  lamb,  rel.  to OS.,  ON.,  OFris.,  OHG.,  Goth,  lamb,  MHG. lamp,  Dan.,  Du.  lam,  Swed.  G.  lamm,  ‘lamb’, for  orig.  *Ion-bho-s;  cogn.  with  Gk.  eXatpoi; (for  *eln-bhos),  ‘hart’,  eXX6 c,  (for  *elnos),  ‘fawn’. All  these  words  are  traceable  to  I.-E.  base  *el-, ‘brown’.  See  eland,  elk,  and  cp.  the  first  element in  lammergeier.
=== KLN alder
=== KLN ell
12844:ell,  n.  —  ME,  ellen,  eln,  fr.  OE.  eln,  rel.  to  OS., OHG.  elina,  ON.  din,  Du.  el,  elle,  MHG.  elene, ele,  G.  Elle,  Goth,  aleina,  fr.  I.-E.  base  *olena, whence  also  OI.  aratnih,  ‘elbow,  ell’,  Gk.  coXev?), ‘elbow’,  L.  ulna,  ‘elbow,  ell’,  OIr.  itile  (gen. uilenn),  W.  and  Co.  elin  (for  *olina),  ‘elbow’, OI.  anih  (for  *dlni),  ‘part  of  leg  above  the  knee’, Arm.  ofn,  ‘dorsal  vertebra,  spine,  shoulder’, uln,  ‘spine,  shoulder’,  OSlav.  lanita  (for  *olnita), ‘cheek’.  Cp. — with  -^-enlargement — Lith.  al- ktine,  ‘elbow’,  Lith.  uolektis,  OSlav.  lakiiti,  ‘ell’, Alb.  fire,  Gheg  lane,  ‘the  arm  from  the  elbow to  the  hand’.  Cp.  elbow.  Cp.  also  alnage,  ulna and  the  first  element  in  linchpin.
```


## [2026-09-05T20:27:54.954Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD el-\"; grep -n \"^el-\\|^el-1\\|^el-2\\|^elm\\|^alino\\|^elk\" AHD_watkins1985.txt | head -20",
 "description": "Grep Watkins"
}
```


### [2026-09-05T20:27:54.996Z] TOOL RESULT

```
=== AHD el-
423:el-2
434:el-1. Elbow, forearm. Extended o-grade form *olind, elbow, in: a. Germanic “alind in Old English ein, fore- arm, cubit: ELL?; b. Germanic compound *alino-bugén-, “bend of the forearm,” elbow (*bugén-, bend, bow; see bheug-’), in Old English elnboga, elbow: ELBOW; c. Lat- in ulna, forearm: ULNA; d. lengthened variant form *6lena in Greek dlené, elbow: OLECRANON, [Pok. 8. el- 307.]
435:el-2. Red, brown (forming animal and tree names). 1. Ex-
436:el-?
438:el-3, To go. Suffixed extended form *ela-un-yo- in Greek elaunein, to drive (< “to cause to go”): ELASTIC, ELATER, ELATERITE; ELASMOBRANCH. [Pok. 6. el- 306.]
440:elk-es-. Wound. Latin ulcus (stem ulcer-), a sore: ULCER. [Pok. elkos- 310.]
```


## [2026-09-05T20:28:03.998Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '435,437p' AHD_watkins1985.txt\necho \"=== leaves for KLN lines\"\npython3 - <<'EOF'\np='KLN_1966.txt'\nlines=open(p,encoding='utf-8',errors='replace').read().split('\\n')\nimport bisect\n# compute leaf index by counting \\f up to each line\nleaf=0\ntargets={12842:'elk',12844:'ell',21040:'lamb'}\nfor i,l in enumerate(lines,1):\n    leaf+=l.count('\\f')\n    if i in targets:\n        print(targets[i],'line',i,'leaf(after)',leaf,'approx printed page',(leaf-12)*2)\nEOF",
 "description": "Watkins el-2 and Klein leaf calc"
}
```


### [2026-09-05T20:28:06.633Z] TOOL RESULT

```
el-2. Red, brown (forming animal and tree names). 1. Ex-
el-?
tended form *elmo- in Germanic *elmo-, *almo- in Old English elm, elm: ELM. 2. Germanic extended form *aliza, alder, in Old English alor, alder: ALDER. 3. Possi- bly Old English ellen, ellzrn, the elder: ELDER?. 4. Ex- tended o-grade form “olki- in Germanic “alkiz, elk, in Old Norse elgr, elk, akin to Old English eolh, elk: ELK. 5. Perhaps Germanic extended form *alk- in Old Norse alka, auk: auK. 6. Extended form *elno- in Greek ellos, hellos, fawn: HELLEBORE. 7. Extended form *elani- in Lithuanian élnis, stag: ELAND. [Pok. 1. el- 302.]
=== leaves for KLN lines
elk line 12842 leaf(after) 277 approx printed page 530
ell line 12844 leaf(after) 278 approx printed page 532
lamb line 21040 leaf(after) 462 approx printed page 900
```


## [2026-09-05T20:28:15.517Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ntxt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\nfor n in (277,278,462):\n    L=leaves[n]\n    print('--- leaf',n,'len',len(L))\n    print(L[:300].replace('\\n',' | '))\n    print('   ...tail:',L[-200:].replace('\\n',' | '))\nEOF",
 "description": "Inspect Klein leaves for page numbers"
}
```


### [2026-09-05T20:28:17.368Z] TOOL RESULT

```
--- leaf 277 len 11960
h’,  and  yapi?, ‘grace,  delight’.  The  first  element  is  cogn.  with OI.  sdras-,  ‘pond’.  For  the  second  element  see Charis. | elephant,  n.  —  ME.  elifaunt,  olifaunt,  fr.  OF.  oli- font  (F.  elephant),  fr.  L.  elephantus ,  fr.  Gk. sXsT>a;  (gen.  -av-ro;).  The  first  element  o
   ...tail: bore. | Elkanah,  n.,  1)  masc.  PN.;  2)  in  the  Bible,  name of  the  father  of  the  prophet  of  Samuel.  —  Heb. Elqandh,  lit.  ‘God  has  created  or  acquired’.  For the  first  element  see
--- leaf 278 len 12081
  El.  Heb.  qandh,  ‘he  created or  acquired’,  from  which  derive  qinydn,  ‘thing acquired,  acquisition’,  and  miqneh,  ‘cattle’,  is rel.  to  Aram.-Syr.  q(na,  ‘he  acquired’,  Arab. qdnd,  ‘he  acquired,  procured’,  and  prob.  also to  Akkad,  qanu,  ‘to  gain,  acquire’.  Cp.  Cain. | el
   ...tail: zevir,  adj.,  pertaining  to  the  Elzevirs,  a  Dutch family  of  printers,  or  to  books  printed  or published  by  them. | Derivative:  Elzevir,  n.,  a  book  printed  by  the Elzevirs. | em,  n., 
--- leaf 462 len 11828
-ly,  adv.,  laggard-ness,  n. | lagniappe,  n.,  gift,  gratuity.  —  Amer.  F.,  fr.  Amer. Sp.  la  hapa,  ‘the  gift’,  fr.  Sp.  la,  ‘the’,  fern,  of  el, fr.  L.  ille,  ‘that’  (see  ille),  and  Amer.  Sp.  hapa, yapa ,  ‘lagniappe’,  fr.  Quechua  yapa,  ‘something added,  gift’. | lago-,  be
   ...tail: ee  prec.  word. | laminate,  tr.  v.,  to  cause  to  form  laminae;  intr.  v., to  split  into  thin  layers.  —  Formed  with  verbal suff.  -ate  fr.  L.  lamina.  See  lamina. | Derivatives:  lamina
```


## [2026-09-05T20:28:30.294Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ntxt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\nfor n in (265,266,267,268):\n    L=leaves[n]\n    print('--- leaf',n)\n    print(L[:200].replace('\\n',' | '))\n    print('  tail:',L[-150:].replace('\\n',' | '))\nEOF",
 "description": "Klein leaves around p.509"
}
```


### [2026-09-05T20:29:07.835Z] TOOL RESULT

```
--- leaf 265
astis  and  in  lithontriptic. drop,  tr.  and  intr.  v.  —  OE.  dropian,  fr.  dropa, ‘drop’.  See  drop,  n. | Derivatives :  dropp-er,  n.,  dropp-ing,  n. droplet,  n.  —  Formed  fr.  drop,  n., 
  tail: bitative-ly,  adv. ducal,  adj.,  pertaining  to,  or  resembling,  a  duke. | —  F.  ducat,  fr.  Late  L.  ducdiis,  ‘pertaining  to  a leader’,  from
--- leaf 266
  the  stem  of  L.  dux,  gen.  duds, ‘leader’.  See  duke  and  adj.  suff.  -al. | Derivative :  dueal-ly,  adv. | ducat,  n.,  name  of  several  coins.  —  OF.  (  =  F.), fr.  It.  ducato,  of  s.m.
  tail: ldrums,  dolt, dwalc,  dwell.  Base  *dhwel-  is  an  -/-enlargement of  base  *dheu-,  ‘to  fly  about  like  dust’.  See  thio- and  cp.  words  the
--- leaf 267
re  referred  to. | Derivatives:  dull,  tr.  and  intr.  v.,  dull-ard,  n., du/l-ish,  adj.,  dull-ness,  n.,  dul-ly,  adv. | dulocracy,  also  doulocracy,  rule  of  slaves.  — Compounded  of  Gk.  So
  tail: te,  adj. | Derivatives:  duplication  (q.v.),  duplicat-ive,  adj., duplicator  (q.v.) | duplication,  n.  —  F.,  fr.  L.  duplicationem,  acc.  of dupl
--- leaf 268
icatid,  ‘a  doubling’,  fr.  duplicatus,  pp.  of duplicare.  See  duplicate,  v.,  and  -ion. | duplicator,  n.  —  L.,  ‘a  doubler’,  fr.  duplicatus, pp.  of  duplicare.  See  duplicate,  v.,  and 
  tail:  See  dike. | dyna-,  combining  form  meaning  ‘power’.  — • Shortened  fr.  Gk.  Suvapu;,  ‘power’.  See  dy¬ namic. | dynameter,  n.,  an  instrument
```


## [2026-09-05T20:29:30.203Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification\ngrep -ho \"Klein[^\\\"]\\{0,200\\}\" page-1*.json | grep -i \"leaf\\|1966\\|pagination\" | head -20",
 "description": "Look at prior KLN handling"
}
```


### [2026-09-05T20:29:30.317Z] TOOL RESULT

```
Klein: 'Ben, masc. PN. — Dimin. of Benjamin'. Big Ben is that clipping applied as a nickname: Klein (printed p. 170-171, leaf 101/102 of KLN_1966.txt) 'Big Ben, name of the bell attached to the clock at We
Klein (1966) s.v. balsam names \
Klein 1966 p.144 s.v. balsam: \
Klein, but on p.144, not 143: the leaf containing pp.144-145 of KLN_1966.txt has \
Klein 1966 and 1971 files
Klein s.v. chibouk (KLN_1966.txt leaf 155)
Klein s.v. chibouk (KLN_1966.txt leaf 155)
Klein, Comprehensive Etymological Dictionary (KLN_1966.txt leaf 155, in the 'chemo-…chicanery' block; the scan's rough offset formula puts the leaf at printed ≈ 286, so Nourai's p.275 is a few pages out or
Klein s.v. chicane, v. (KLN_1966.txt leaf 155)
Klein s.v. chicane, chicanery (KLN_1966.txt leaves 155-156)
Klein (KLN_1966.txt leaf 280-281 s.v. smaragdite): 'F., formed with subst. suff. -ite fr. Gk. smaragdos, emerald'.
Klein p.399 s.v. Danaüs (KLN_1966.txt line 10300)
Klein has no separate 'Danube' headword (grep 'Danube' in KLN_1966.txt gives only Danaüs, delta and Rhaetia).
Klein p.403 s.v. date 'fruit of the palm tree' (KLN_1966.txt line 10373; page markers '403' at line 10344, '404' at 10389)
Klein 1966 s.v. dufter (KLN_1966.txt leaf 266 ≈ printed pp. 489-490; the cited 487 is within the two-page-per-leaf tolerance of this scan): 'dufter, n., a bundle of sheets of paper (India). — Hind. daftar,
Klein 1966 s.v. diphtheria (KLN_1966.txt leaf 248, whose running number in the OCR is 454, so printed pp. 453-454 — Nourai's 452 is within the ±2 tolerance of this two-pages-per-leaf scan): 'Medical L., fr
Klein does have the entry — KLN_1966.txt, leaf 247 (≈ printed p.470 by the file's leaf/page formula, some 20 pages off Nourai's '450'): 'dinar, n. — Arab. dīnār, fr. Late Gk. δηνάριον, fr. L. denarius. See
Klein does have exactly this entry, but on pp.442-443 of the 1966 two-volume edition, not 440: KLN_1966.txt leaf 242 runs from 'diaconus' to 'Diana', while leaf 241 (which carries the printed numerals 440 
Klein 1966 ed., page marker '1479' at KLN_1966.txt line 36025, entry at line 36036: \
Klein gives Nourai's chain without any reservation; he is a 1966 authority repeating the traditional account.
```


## [2026-09-05T20:29:38.716Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nlines=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\n')\ndef near(t,lo,hi):\n    for i in range(lo,hi):\n        s=lines[i].strip()\n        if re.fullmatch(r'\\d{3,4}',s) or re.fullmatch(r'\\d{3,4}\\s+\\S{0,12}',s):\n            print(t,i+1,repr(lines[i][:60]))\nnear('ELK',12700,13000)\nprint('---')\nnear('LAMB',20900,21200)\nEOF",
 "description": "Find printed page markers near elk and lamb"
}
```


### [2026-09-05T20:29:40.822Z] TOOL RESULT

```
ELK 12731 '504'
ELK 12732 '505'
ELK 12777 '506'
ELK 12788 '507'
ELK 12823 '508'
ELK 12851 '510'
ELK 12911 '512'
ELK 12912 '513'
ELK 12998 '516'
---
LAMB 20911 '1967'
LAMB 20958 '857'
LAMB 20987 '858'
LAMB 21001 '859'
LAMB 21029 '860'
LAMB 21030 '861'
LAMB 21075 '862'
LAMB 21076 '863'
LAMB 21118 '864'
LAMB 21119 '865'
LAMB 21155 '866'
LAMB 21180 '867'
```


## [2026-09-05T20:29:47.549Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '12823,12852p' KLN_1966.txt",
 "description": "Klein printed page 509"
}
```


### [2026-09-05T20:29:47.613Z] TOOL RESULT

```
508
elevat-ed-ness,  n.,  elevation  (q.v.),  elevator  (q.v.), elevat-ory,  adj.
elevation,  n.  —  F.  elevation ,  fr.  L.  elevationem, acc.  of  elevatio,  ‘a  raising,  lifting’,  fr.  elevatus, pp.  of  elevare.  See  prec.  word  and  -ion. elevator,  n.  —  Late  L.  elevator,  ‘one  who  raises or  lifts’,  fr.  L.  elevatus,  pp.  of  elevare.  See  ele¬ vate  and  agential  suff.  -or. eleven,  adj.  and  n.  —  ME.  elevyn,  enleven,  fr.  OE. endleofan ,  endlufon,  endlyfon,  rel.  to  OS.  elle- Van,  ON.  ellifu,  Dan.  elve,  Swed.  elva,  OFris. andlova,  elleva,  Du.  elf,  OHG.  einlif  MHG. einlif  eilif  eilf  G.  eilf  later  elf  Goth,  ainlif These  words  are  formed  fr.  Teut.  *ain-,  ‘one’, and  I.-E.  base  *liqw-,  ‘to  be  left  over’,  whence also  Gk.  Xeittew,  ‘to  leave  behind,  leave’,  L. linquere,  of  s.m.  Accordingly  eleven  prop, means  ‘one  left  over  (after  ten)’;  cp.  Lith. vienudlika,  ‘eleven’  (lit.  ‘one  left  over’),  dvylika, ‘twelve’  (lit.  ‘two  left  over’).  For  the  first  ele¬ ment  see  one,  for  the  second  see  loan.  Cp.  twelve, eleventh,  adj.  and  n.  —  Formed  fr.  eleven  with numeral  suff.  -th  on  analogy  of  fourth.  Cp.  OE. endleofta,  endlyfta,  which  is  rel.  to  OS.  ellifto, ON.  ellifti ,  Dan,  elvte,  OFris.  andlofta,  ellefta, Du.  elfde,  OHG.  einlifto,  MHG.  eilifte,  eilfte, G.  elfte,  ‘eleventh’.
elf,  n.  —  OE.  self  ylf  rel.  to  ON.  alfr,  OS.,  MLG. alf  MHG.,  G.  alp,  ‘incubus’.  The  connection of  these  Teut.  words  with  L.  albus,  ‘white’,  is due  to  folk  etymology.  See  alp,  ‘a  demon’,  and and  cp.  Alfred,  Aubrey,  eldritch,  oaf,  Oberon, Oliver.  Cp.  also  the  first  element  in  erlking. Derivatives:  elfin  (q.v.),  elf-ish,  adj.,  elf-ish-ly, adv.,  elf-ish-ness,  n.,  elf-kin,  n. elfin,  adj.,  pertaining  to,  or  resembling,  elves;  n., 1)  an  elf;  2)  a  child.  —  Coined  by  Spenser  fr. prec.  word.  For  the  ending  see  adj.  suff.  -in. Eli,  1)  masc.  PN.;  2)  in  the  Bible,  a  high  priest of  Israel  and  teacher  of  Samuel.  —  Heb.  ‘Elf, lit.  ‘high’,  from  the  base  of  ‘aldh,  ‘he  .went  up, ascended',  which  is  rel.  to  Aram.  —  Syr.  'air, Ugar.  ‘ly,  Arab,  ‘aid,  Akkad,  elu,  ‘he  went  up, ascended’,  Heb.,  Aram,  'al,  Arab,  aid,  ‘on, upon’.  See  aliyah  and  cp.  Alenu.
Elias,  masc.  PN.  —  Gk.  ’EX(5t?,  fr.  Heb.  Eliydh. See  Elijah.
elicit,  tr.  v.,  to  draw  forth,  provoke.  —  L.  Hicitus, pp.  of  elicere,  ‘to  draw  forth,  elicit’,  fr.  e-  and lacere,  ‘to  entice,  allure’,  which  is  rel.  to  laqueus, ‘a  noose,  snare’,  deliciae,  ‘delight,  charm’.  See lace  and  cp.  delicious,  delight.  For  the  change of  Latin  a  (in  lacere)  to  i  (in  e-iicere)  see  abigeat and  cp.  words  there  referred  to. elide,  tr.  v.,  to  leave  out.  —  L.  elidere,  ‘to  strike out’,  fr.  e-  and  laedere,  ‘to  hurt,  injure’.  See lesion.  For  the  change  of  Latin  ae  (in  laedere) to  i  (in  e-lidere)  see  acquire  and  words  there referred  to  and  cp.  esp.  collide. eligibility,  n.  —  Formed  fr.  eligible  with  suff.  -ity. Cp.  F.  eligibilite.
eligible,  n.  —  F.  eligible,  fr.  L.  eligere,  ‘to  pick
50V
out,  choose’,  fr.  e-  and  legere,  ‘to  gather,  col¬ lect,  pick  out,  choose;  to  read’.  See  lecture  and -ible  and  cp.  elect,  v.  For  the  change  of  Lati  1 e  (in  legere)  to  i  (in  e-ligere),  see  abstinent  and cp.  words  there  referred  to.
Derivatives:  eligibility  (q.v.),  eligible-ness,  n., eligibl-y,  adv.
Elihu,  1)  masc.  PN.;  2)  in  the  Bible,  the  name  of several  personages,  amongst  whom  the  most famous  is  found  in  the  Book  of  Job  (see  chap¬ ters  32-37);  he  is  the  youngest  of  the  four  men who  visited  Job.  —  Heb.  Elihd,  lit.  ‘He  is  my God’.  For  the  first  element  see  El.  Heb.  hu, ‘he’,  is  rel.  to  Aram.-Syr.  hit,  Arab,  huwa, Ethiop.  we'tu,  Akkad,  shu,  ‘he’.
Elijah,  1)  masc.  PN. ;  2)  in  the  Bible,  name  of  the great  prophet  also  known  as  the  Tishbite.  — Heb.  Eliyydh,  lit.  ‘The  Lord  is  God’.  For  the first  element  see  El  and  words  there  referred  to and  cp.  esp.  Joel.  For  the  second  element  in Elijah  cp.  the  second  element  in  hallelujah, Hezekiab,  Isaiah,  Jeremiah,  Matthew,  Matthias, Nehemiah,  Obadiah,  Zachariah,  Zephaniah.  Cp. also  Elias,  a  shortened  form  of  Elijah. eliminable,  adj.  —  See  eliminate  and  -able, eliminant,  adj.,  promoting  elimination  ( med .)  — L.  eliminans,  gen.  -antis,  pres.  part,  of  eliminare. See  next  word  and  -ant.
eliminate,  tr.  v.,  1)  to  remove;  2)  to  exclude.  — L.  eliminatus,  pp.  of  eliminare,  ‘to  turn  out  of doors,  banish’,  fr.  e-  and  limen,  gen.  liminis, ‘threshold,  entrance’.  See  limen  and  verbal  suff. -ate.
Derivatives:  eliminat-ion,  n.,  eliminat-or,  n., eliminat-ory,  adj.
Elishah,  1)  masc.  PN.;  2)  in  the  Bible,  an  Israelite prophet,  disciple  and  successor  of  Elijah.  — Heb.  Elishd‘,  lit.  ‘God  is  salvation’,  fr.  El,  ‘God’, and  yesha',  ‘salvation’.  For  the  first  element  see El  and  cp.  words  there  referred  to.  The  second element  is  rel.  to  yishu‘dh,  ‘salvation,  deliver¬ ance,  welfare,  prosperity’,  hoshfa',  ‘he  saved’. See  hosanna  and  cp.  the  first  element  in  Isaiah and  the  second  element  in  Joshua, elision,  n.  —  L.  elisio,  gen.  -onis,  ‘a  striking  out, elision’,  fr.  elisus,  pp.  of  elidere,  ‘to  strike  out’. See  elide  and  -ion  and  cp.  collision, elisor,  n.,  a  person  appointed  to  return  a  jury (law).  —  OF.  elisour  (F.  eliseur),  from  the  stem of  elire  (F.  el  ire),  ‘to  choose’.  See  next  word, elite,  n.,  a  choice  part.  —  F.,  fr.  OF.  eslite,  fern, of  eslit,  pp.  of  e  si  ire  (F.  elire),  ‘to  choose’,  fr. L.  clectus,  pp.  of  eligere.  See  elect  and  cp. prec.  word.
elixir, n.,  1)  asubstance  supposed  to  prolonglife; 2)  a  substance  supposed  to  change  all  metals into  gold.  —  ML.,  fr.  Arab,  al-iksir,  which  is formed  fr.  Arab,  al-,  ‘the’,  and  Gk.  jjp'.ov,  ‘dry medicinal  substance,  cataplasm’,  fr.  ‘dry’. See  serene  and  cp.  xero-.
Elizabeth,  1)  fern.  PN.;  2)  in  the  Bible,  the  name of  the  wife  of  Aaron.  —  Late  L.  Elisabeth,  fr.
Gk.  ’EXELaotJUeft,  ’EXtaafte-r,  fr.  Heb.  Elishebha', lit.  ‘God  is  an  oath’.  For  the  first  element  see  El. The  second  element  is  rel.  to  shivfdh,  fem.  sheva‘, ‘seven’,  and  to  nishbd‘,  ‘he  swore’,  orig.  ‘he bound  himself  by  the  sacred  number  seven’.  See Shabuoth  and  cp.  the  second  element  in  Bath- sheba.  Cp.  also  Elsa.
Elizabethan,  adj.,  pertaining  to  the  age  of  Queen Elizabeth  I.  —  First  used  by  Carlyle,  instead  of Elizabethian,  which  was  coined  by  Coleridge. See  prec.  word  and  -ian,  resp.  -an.
elk,  n.,  the  largest  existing  deer.  —  ON.  elgr, rel.  to  OE.  eolh,  OHG.  elaho,  MHG.  elhe,  G. Elch;  Gk.  itXxT)  and  L.  alces,  ‘elk’,  are  Teut. loan  words.  The  above  Teut.  words  are  cogn. with  OI.  fsah,  fsyah,  ‘buck  of  the  antelope’, Russ,  losu,  Czech  los,  etc.,  ‘elk’.  These  words derive  fr.  I.-E.  base  *elk-,  a  -^-enlargement  of base  *el-,  ‘brown’.  For  derivatives  of  *eln-, -n-enlargement  of  base  *-<?/-,  see  eland  and  cp. words  there  referred  to.  Cp.  also  Alces  and  the first  element  in  hellebore.
Elkanah,  n.,  1)  masc.  PN.;  2)  in  the  Bible,  name of  the  father  of  the  prophet  of  Samuel.  —  Heb. Elqandh,  lit.  ‘God  has  created  or  acquired’.  For the  first  element  see  El.  Heb.  qandh,  ‘he  created or  acquired’,  from  which  derive  qinydn,  ‘thing acquired,  acquisition’,  and  miqneh,  ‘cattle’,  is rel.  to  Aram.-Syr.  q(na,  ‘he  acquired’,  Arab. qdnd,  ‘he  acquired,  procured’,  and  prob.  also to  Akkad,  qanu,  ‘to  gain,  acquire’.  Cp.  Cain.
ell,  n.  —  ME,  ellen,  eln,  fr.  OE.  eln,  rel.  to  OS., OHG.  elina,  ON.  din,  Du.  el,  elle,  MHG.  elene, ele,  G.  Elle,  Goth,  aleina,  fr.  I.-E.  base  *olena, whence  also  OI.  aratnih,  ‘elbow,  ell’,  Gk.  coXev?), ‘elbow’,  L.  ulna,  ‘elbow,  ell’,  OIr.  itile  (gen. uilenn),  W.  and  Co.  elin  (for  *olina),  ‘elbow’, OI.  anih  (for  *dlni),  ‘part  of  leg  above  the  knee’, Arm.  ofn,  ‘dorsal  vertebra,  spine,  shoulder’, uln,  ‘spine,  shoulder’,  OSlav.  lanita  (for  *olnita), ‘cheek’.  Cp. — with  -^-enlargement — Lith.  al- ktine,  ‘elbow’,  Lith.  uolektis,  OSlav.  lakiiti,  ‘ell’, Alb.  fire,  Gheg  lane,  ‘the  arm  from  the  elbow to  the  hand’.  Cp.  elbow.  Cp.  also  alnage,  ulna and  the  first  element  in  linchpin.
Ella,  fem.  PN.  —  Fr.  earlier  Ela,  Ala,  fr.  OHG. Alia,  a  name  derived  fr.  OHG.  al,  ‘all’,  ala- las  the  first  element  of  compounds),  ‘entirely, quite’;  see  all.  Quite  frequently  the  name  Ella appears  as  the  diminutive  or  pet  form  of Eleanor.
-ella,  dimin.  suff.  —  L.  -ella,  fem.  of  -ellus.
ellagic,  adj.,  rel.  to  the  acid  C14H6Os  ( chem .)  — F.  ellagique,  coined  by  the  French  chemist Henri  Braconnot  (1781-1855)  fr.  ellag,  anagram of  galle,  ‘gallnut’  (see  gall,  ‘gallnut’),  and  -ique : so  called  by  him  because  it  was  first  obtained from  oak  galls.
Ellen,  fem.  PN.  —  An  earlier  form  of  Helen.
ellipse,  n.,  one  of  the  three  conic  sections  ( geom .) —  Back  formation  fr.  L.  ellipses,  pi.  of  ellipsis, ‘want,  defect,  omission,  ellipse’,  fr.  Gk.  SXXsujiti;,
ellipsis
510
emasculate
```


## [2026-09-05T20:29:59.750Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v1 آلگونه\"; grep -n \"آلگونه\" BQT_v1_pages.txt | head\necho \"=== BQT v1 آرنج\"; grep -n \"آرنج\" BQT_v1_pages.txt | head\necho \"=== BQT v1 آلک\"; grep -n \"آلک\" BQT_v1_pages.txt | head -5\necho \"=== BQT v1 aruš\"; grep -n \"arus\\|aruš\\|arus̆\" BQT_v1_pages.txt | head -5",
 "description": "Grep Borhan-e Qate vol 1"
}
```


### [2026-09-05T20:29:59.870Z] TOOL RESULT

```
=== BQT v1 آلگونه
8630:« آرغدء » . رك : آرغده. ۲ -.لفتی درآ لگونه . رك : آلگونه .
8635:۰- آن بناکوی کز ساکویی ‏ " بر کشيده است آلگونه بسيم
=== BQT v1 آرنج
7260:آرنج را گوشد که‌بند گاه ساعد وبازوست وبعریی
7417:] دن ه بر وزن فارن . مخفف آرنج
7425:آرنج‌است که مرفی‌داشد - ور نگ ولون (4)را
10772:آرنج - و انجمن و مجمم و جمعیت مردم راهم
11111:وجیم. , بمعنی آرنج است ت که بندگاه ساعد
16841:دوش تا آرنج را عامل است .اک
17011:گفته‌اند ازخانه تاآرنج
17360:از آرنج دست: باشد ناسر دوش - و چوبدست
23179:پاد نج بر وزن آرنج . زری باشد
=== BQT v1 آلک
=== BQT v1 aruš
```


## [2026-09-05T20:30:01.289Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MPP page ~79\"; python3 - <<'EOF'\ntxt=open('MPP.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\nprint('nleaves',len(leaves))\n# leaf = printed - 14 -> printed 79 = leaf 65\nfor n in (64,65,66):\n    print('--- leaf',n)\n    print(leaves[n][:1500])\nEOF",
 "description": "Henning Mitteliranisch p.79"
}
```


### [2026-09-05T20:30:03.018Z] TOOL RESULT

```
=== MPP page ~79
nleaves 140
--- leaf 64
78
IRANISTIK — LINGUISTIK
stehend ansehen, dass sich die Christen dabei der einheimischen Schrift
d.h. des Pehlewi, bedienten; dafür zeugen das einzig überlebende Frag¬
ment der alten christlich-persischen Bibelübersetzung, der Pehlewi-
Psalter (§ 16), das wohl auch aus christlichen Kreisen herrührende Tur-
faner Farhang-Bruchstück (§ 16 Ende) und die freilich bescheidenen
Schriftdenkmäler der persischen Mission in Indien (§ 17 Ende) L Per¬
sisches in syrischer Schrift gibt es im Westen erst aus neupersischer Zeit;
ein paar noch immer nicht recht erklärte 2 Verse in einer Hs. des I3ten
Jhdts. (D. S. Margoliouth,’ JRAS., 1903, 765-70). Auch recht später
Zeit gehört der gelegentliche Versuch an, Persisch mit armenischen
Buchstaben darzustellen, in einer Hs. aus dem I5ten Jhdt., die ein
kurzes christliches Gebet in sieben Sprachen enthält, darunter nicht
nur Persisch, Arabisch usw., sondern auch — und das ist das Interes¬
sante — ‘die Sprache der Meder’, d.h. ein nordiranischer Dialekt aller¬
dings nicht sehr alten Gepräges (H. W. Bailey, JRAS., 1943, 4sq.);
man findet dort vernarb ‘unsterblich’ (mpers. abemarg), hat ‘ ‘gehängt*
(älter haxt, vgl. pers. ähixt usw.), koy ‘welcher’ (mpers. ke) und 9 §hr
‘für, wegen’ in Okarina ‘für uns’, gewiss als ursprüngliches ai-kdrd-
zu mpers. ’c 'yd kyrd (parth. MN ZK * krty) ‘deshalb’ gehörig. Als die
christliche Mission, vielleicht schon im 5ten Jahrhundert 4 auf soghdi-
sches Sprachgebiet Übergriff, sowie bei ihrem weiteren Vorschreiten in
--- leaf 65
MITTELIRANISCH
79
Hier ist, neben der im einheimischen Soghdischen sowie im Manichäisch-
Soghdischen aufgegebenen Unterscheidung von 8 und 0 , die Schaffung
zusätzlicher Zeichen (F. W. K. Müller, Sb. P. A. W., 1907, 2Öisq.) zu
beachten, die mit der seinerzeit von den Manichäern für das Westiranische
vorgenommenen Zeichenerfindung (§ 27) merkwürdig parallel geht: *
und / aus k bzw. p durch Veränderung am Buchstabenkopf, f entspre¬
chend manich. 7 (auch der Form nach ähnlich). Die so gewonnene sogh-
disch-syrische Schrift wurde dann weiterhin für das Uigurisch-Türkische
(F.W.K. Müller, Handschriftenreste, II, 107) und, allerdings modifiziert,
für das Neupersische gebraucht. Für das letztere stellt das von F. W. K.
Müller vorgelegte Psalmenbruchstück (Festschrift E. Sachau, 1915,
215-22) das wichtigste Zeugnis dar (vgl. H. H. Schaeder, Ungar. Jbb.,
XV, 570 A. 2; E. Benveniste, J.A., 1938, I, 458-62); dazu ein noch
unveröffentlichtes pharmakologisches Fragment über medizinische Öl-
Arten; Z kommt leider nicht vor, / und 6 werden beide mit Säde wieder¬
gegeben, für y 1 tritt, im Gegensatz zum Soghdischen, ein modifiziertes g
ein.
30. Die ältesten Dokumente des Jüdisch-Persischen
An wirklich mitteliranischem Sprachmaterial haben uns die Juden,
die in späteren Jahrhunderten so viele Sprachen mit ihrer hebräischen
Schrift aufzeichneten, nichts hinterlassen. Aus den bislang nicht veröffent¬
lichten Inschriften von Persepolis darf man schliessen, dass die persischen
Juden zur Sassanide
--- leaf 66
So
IRANISTIK — LINGUISTIK
gebraucht (z.B. Zeile 29 q'r ’y prmwdy *J> skt qwnwm t* qrdh bwd = kär i
farmüSi a$ saxt kunom tä har de buva§ c die Arbeit, die Du angeordnet
hast, ich werde sie energisch betreiben, bis sie vollendet sein wird’), der
Wortschatz ist altertümlich (z.B. bind-, bindäd- ‘finden* Z. 26 = mpers.
wind-äd-an). Manche der bisher unerklärten Wörter sind freilich auf die
Rechnung der benachbarten zentralasiatischen Sprachen zu setzen, so
das aus dem Soghdischen stammende Wort für ‘Eunuch’, 'ndryq >y
sy[h !] ‘der schwarze Eunuch’ Z. 27 (soghd. ’ nir y yk ), und das seltsame
tmkwy (Z. 24/25), das genau 1 dem sonst nur im Soghdischen belegten,
vielleicht ursprünglich fernöstlichen cmxwy entspricht und zweifellos
Name eines Saiteninstruments ist 2 . Von solchen Zentralasiatismen ab¬
gesehen, ähnelt die Sprache des Briefes der des nächstältesten Doku¬
ments, des im Jahre 1021 in Ahwäz ( Hwrmiyr) geschriebenen gericht¬
lichen Vergleichs (Bodleian Library, MS. Heb. b. 12 fol. 24; D. S. Mar-
goliouth, Jewish Quarterly, 1897, 67isqq.); die Orthographie ist frei¬
lich verschieden. Hier findet man ebenfalls hu (geschr. kw) für ‘dass*,
mehrmals auch die durch merkwürdigerweise dem folgenden Worte
vorgesetztes einfaches Yöd bezeichnete Idäfe- Partikel in ihrer alten Funk¬
tion als Relativum; z.B. Zeile 5 br'dr'nwtn yp* rnysr hynd ‘meine Brüder,
die in Ägypten sind’, Z. 7 p'yn ykyrdy — pa'in i kerdi ‘für dieses, welches
Du getan hast’, Z. 1 , ym i n shd’n yktni'n *zyr *yn m
```


## [2026-09-05T20:30:10.986Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\ngrep -rn \"MPP\" --include=*.md --include=*.json data/verification/sources/refs_online.json | head -5\necho ---\ngrep -rln \"MPP\" data/verification/*.json | head\necho ---\ngrep -ho \"MPP[^\\\"]\\{0,300\\}\" data/verification/*.json | head -20",
 "description": "Find prior handling of MPP"
}
```


### [2026-09-05T20:30:11.085Z] TOOL RESULT

```
(eval):2: no matches found: --include=*.md
---
data/verification/page-32.json
data/verification/page-44.json
data/verification/page-95.json
---
MPP), which gives ʾptʾb/ʾbdʾb with the preverb.
MPP:79
MPP = Henning, 'Mitteliranisch' (HdO I.4.1, 1958). MPP.txt \\f-leaf 65, which carries the printed page number '79' at the head, is §29-30 on the Sogdian-Syriac script and the oldest Judeo-Persian documents — nothing about āluh or eagles. The citation is probably meant for Henning's other work, the 'Lis
MPP 291b; 3pl pywsynd, perf. pass. pywst), matched by Parthian bws- 'to await, wait for, expect' and pdbws- 'to desire, yearn' (Ghilain 65, 80). The reading is *payōs-/paywas- < Old Iranian *pati-baud-sa-: pati- > MP pay- (the intervocalic -t- voiced and the -i- became the glide -y-), and *-ds- > -s-. 
MPP: 291b'; '*PARTHIAN: bws- (inch.) ‘await, wait for, expect’ || (+ *pati-) pdbws- ‘to desire, yearn’'.
MPP: 119a'.
```


## [2026-09-05T20:30:17.033Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nls; ls data/extracted | head; ls tools",
 "description": "Explore repo layout"
}
```


### [2026-09-05T20:30:17.088Z] TOOL RESULT

```
CONTRIBUTING.md
data
docs
EtymologicalDictionary-persian-english.epub
EtymologicalDictionary-persian-english.pdf
README.fa.md
README.md
site
tools
batch
NEXT_CHUNK
RETRY.txt
test
build_site.py
fetch_source.py
ganjoor.py
__pycache__
ref_index_latin.py
ref_index_pages.py
ref_locator
ref_ocr_book.py
ref_page.py
research.py
validate.py
verify_archive_sources.py
verify_check.py
verify_export_process.py
verify_publish.sh
```


## [2026-09-05T20:30:20.828Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 -c \"\nimport json,glob\nfor f in sorted(glob.glob('data/extracted/batch/page-*.json'))[:1]: pass\n\" \npdftotext -f 20 -l 30 EtymologicalDictionary-persian-english.pdf - 2>/dev/null | grep -n \"MPP\" ",
 "description": "Search PDF front matter for MPP"
}
```


### [2026-09-05T20:30:22.906Z] TOOL RESULT

```
101:66 MPP
```


## [2026-09-05T20:30:25.486Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npdftotext -f 20 -l 30 EtymologicalDictionary-persian-english.pdf - 2>/dev/null | sed -n '80,130p'",
 "description": "Print reference table context"
}
```


### [2026-09-05T20:30:27.108Z] TOOL RESULT

```
W. B. Henning, Bibliography of Important Studies on
Old Iranian Subjects, Ketâb Khâneh Dânesh, Tehran 1950.

62 MAG G. Widengren, Mohammad, The Apostle of God,
Chapter VIII, “Ïranian Elements in the Kurânic Vocabulary”,
Uppsala Universitets Arsskrift, Uppsala, 1955
63 MFL A. M. Orânskî, Moqaddameh Feqh Al-Logheh Îrânî,
ÁúZÆûZ È∏æöZ ‰∫ï Èõ¨∫õ
Translated into Persian by K. Keshâvarz, Payâm press, Tehran 1358 (1979).

A-12

TABLE IV - Reference Abbreviations (continued ...)
64 MMF K. Khalîlî, Dictionary of Derivatives of the Persian Áçf£ï fd£≥õ \£∫•≤õ ‡¿ùÆï
Infinitives or Farhang Moshtaqqât Masâder Fârsî,
Institute of Cultural Studies and Research, Tehran, 1993.
65 MON M. Mo` în, Farhang Fârsî Moî`n,
Six volumes, Amîr Kabîr press 1363 (1984).

„√∑õ Áçf£ï ‡¿ùÆï

66 MPP

W. Henning, "A List of Middle – Persian and Parthian Words",
Bulletin of the School of Oriental and African Studies
(BSOAS IX:1937-39) pp 79-92, University of London.

67 MZF

P. Nâtel Khânlarî, Mabâhes Adabî va
Áçf£ï x£Ög Çf£Öfd }Æ¿ù z ÁÖdZ Œä£§õ
Honarî darbâreh Zabân Fârsî, Sokhan press, Tehran 1340 (1961).

68 NAT

C. Berlitz, Native Tongues, Grosset & Dunlapp Publishers, New York, 1982

69 NFI

F. Jonaydî, Nâmeh Farhang Îrân,
xZÆûZ ‡¿ùÆï Èõ£ú
Bonyâd Nayshâbûr, Tehran 1368 (1989). Section 4, translated
from C.H. Rempis' "Persische Wörter im Deutschen," in Mitteilungen, Institut
für Auslands-Beziehungen, Iran-Nummer, 3/4, Stuttgart, 1960, S.229-233.

70 NYB

H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1974.

71 OEW
```


## [2026-09-05T20:30:36.951Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== title\"; grep -n \"List of Middle\" HENNING_selected_papers.txt | head\necho \"=== arisn forms\"; grep -n \"ryšnwg\\|ʾryšn\\|arisn\\|ārišn\\|arēšn\\|ryšn\" HENNING_selected_papers.txt | head -20",
 "description": "Grep Henning Selected Papers"
}
```


### [2026-09-05T20:30:37.040Z] TOOL RESULT

```
=== title
=== arisn forms
```


## [2026-09-05T20:31:00.655Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT auruša\"; grep -n \"auruša\\|auruSa\\|aurusa\" BRT.txt | head -10\necho \"=== BRT arethna\"; grep -n \"arə0na\\|arəθna\\|are0na\\|araOna\\|arefna\\|araGna\" BRT.txt | head -10\necho \"=== BRT frararathni\"; grep -n \"frāra\\|frara0ni\\|frärafcni\\|frāraθni\" BRT.txt | head -10\necho \"=== KNT arasni\"; grep -n \"arašni\\|arasni\\|arašnis\" KNT.txt | head -10",
 "description": "Grep Bartholomae and Kent"
}
```


### [2026-09-05T20:31:00.747Z] TOOL RESULT

```
=== BRT auruša
5350:aurusa-
5880:•  j.  asp5.stao/ah-  Adj.  (fem.  °ye/tJ-) 'starker,  umfangreicher  als  ein  Pferd, Pferdeleib"':  xä  'yehls  apam  \'t.8.$,A2; —  srira  vü  ar»)im  b.lzava  aurusa  "ythTs'^
12246:spähe  kihrpa  aurusake  .  .  äal  paiti avaiti  .  .  avi  zrayS  vourukasttn  .  .  ä  äim paüi.yq^  nisdvaraili  daevS  yS  apaoiö aspahe  kfhrpa  iümahe .  .  kam  läcit  bäzus barats  . .  'ryaica  . .  -vasca .  .'täyüitya%ö  . . a    rapi^winfm    srvämm    ä    Mm    bavatli
18174:•  '}.  frä-d«r«sra-  Adj.  'hervorleuchtend, strahlend':  ti^trlm  stSrfm.,aurus?m  raoxs- mm  °r)m'^X.8.z;  —  asMatumys..raoxins °rS  Yt  13.  2;  —  nmatam  .  .  raoxihfm 'r?m  V.  22. 1 ;  —  aurvanlö  aurusa  raoxiha *ra  Y.57.  27;  —  yeAhe  urva  .  .  aurufe raoxins  'rS  Yty.81.
29306:•  j.  hanhauruSay-  patr.  Adj.  'von Hanhaumai  stammend,  dessen  Nach- komme': varihahe  -löii ataonö  Yt  13. 104; *FrD.7'>.
=== BRT arethna
=== BRT frararathni
=== KNT arasni
```


## [2026-09-05T20:31:05.062Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT aurusa- context\"; sed -n '5345,5360p' BRT.txt\necho \"=== BRT Ellbogen\"; grep -n \"Ellbogen\\|Ellenbogen\" BRT.txt | head -10\necho \"=== KNT cubit\"; grep -n -i \"cubit\" KNT.txt | head -10",
 "description": "Bartholomae aurusa and Ellbogen; Kent cubit"
}
```


### [2026-09-05T20:31:05.142Z] TOOL RESULT

```
=== BRT aurusa- context
diu. j.  *ar5t  niümät  N,  ^l  T:  lies  anlaräi  «*.
•  j.  a-rÄna-  Adj.  'keinen  Kampf  führend, nicht  kämpfend':  'na  F.  7.
Pü.:  apatkär.
•  j.  ar«m,  g.  arvm  Adv.  'recht,  passend, wie  sichs  gehört':  y3cä  alä  arttau!  °r}m *vaiidyäiisd.)\.44.S;—'KimF.y.  a)  mit V.  'man-  und  Dat.  der  Pcrs.  'so  denken, wies  einem  recht  ist'  sva.  'ergeben  sein': yastä  da!i'3ng  aparS  masyqscä  tarS.mqstä ySi  Im  tarS.mainyanta  anySng  ahmlt  yS Aoi  'rSm  mainySii  "wer  danim  kUnfÜg die  Daiva  und  Menschen  missachten  wird, die  ihn  (den  Saoiyant)  missachten,  die andern  (alle)  ausser  den,  der  ihm  ergeben ist"  Y.  45.11.  b)  adjektivisch"  'füg- sam, gehorsam',  mit  Dat:  nSit  urvsha (sd.)  dätinbyas^  iarapanS  väsiräi  'rfm "den  Geboten  und  Satzungen  fdr  die  Land- wirtschaft" wollen  sich  dieÄ",  nicht  fUgen"
dby  Google
aurusa-
190
Y.  5/.  143'.  [P.  25:    lies    anm.maiii,
arsm-uxti,  ar^m.varsii.]
KompA.  —  VgL  aach  ärmatay-,  ra/'i^vfl:  —
Zum
•<  Adv.
PQ.:
JaH\  Sü.;  sampärnam.  —  1)  Vgl,  Dbr.  ALS. 146.  —  ')  Eig.  'von  -  her'  sva.  'wegen,  be- treffs'. —  J)  Anders  Btkl.  AF.  2.  166,  Gd\. KZ.  27-  24*.  583,  aS.  263,  BB.  i^.  z6o.  —  ; <)  Vgl.  auch  zu  'ar-,  'ar-.
•  j.  *ar»m.uxtay  ■'  f.  'rechtes,  angemesse- nesSprechen':  *ar7m.maiH  *kumata  mamne (sd.)    "uxti    küxta     anm.varsti     kvarasta
Pu. ;  bavandak  gekoisn.  —  ')  Hds,  anm  müxr.
=== BRT Ellbogen
5498:•  j.  'araöna-  m.  'Ellenbogen':  -^nd  (ND.) F-,?g.
18269:*)  D.  i.  das  Mass  vom  Ellenbogen  bis  zu  den Fingerspitzen,  doppell  so  lang  als  ein  vilaslay- (sd.),  halb  so  lang  als  ein  frabiiaV'  (sd.);  vgl. West  SBE.  £.  99,  Bthl.  AT.  2.  43,  ferner  F. 3/  at).
18270:*frS-r&nay-  n.  'Elle';  S.  dfllö  ai.  atalaiy- 'Ellenbogen,  Elle'  und  Btmi.  BB.  ty.  Iii; s.  auch  'ar3%na-;  mp.  fräräsl  ist  eine  Ver- unstaltung des  Aw.-Worts.  —  Pii.:  ftäc adrln  (or^n?)])  drahnii.  —  »  Hds.  •ra%tK.- dr".  —  »)  S.  zu  gämait:  —  1)  S.  zu  ^arAna-.
=== KNT cubit
1118:thus the pAr. *aratn- aratan- gave Av. dual arana, but OP arašn- and (with extension of the $) arasan- ‘cubit’, in inst. pl. arašaniš (see
2761:was packed down, some 40 cubits in depth, another (part) 20 cubits in depth’. Appositive substantives do not necessarily agree in gender; thus DPd 6f уат dahydus Pürsa ‘this province Persia’, where dahydus is feminine and Påãrsa is masculine.
4292:$3e. 22-7. This palace which I built at Susa, from afar its ornamentation was brought. Down- ward the earth was dug, until I reached rock in the earth. When the excavation had been made, then rubble was packed down, some 40 cubits in depth, another (part) 20 cubits in depth. On that rubble the palace was constructed.
5049:araían- sb. ‘cubit’ (832, §82, S155.ID): Av. nom. dual araénd, to Iran. stem aratan- атап, ef. Skt. aratnt-; Lg. 15.176-7 (borrowed from Iran. into General Slavic as aršin ‘ell’, Wb. AfOF 7.41, against Berneker, Slav. etym. Wrtb. 31, who thinks it borrowed from Turkish); cf. also Bv. Orig. 105. arasanit ipm. (§187) DSf 26 bis (not nom. sg., with Ву. Gr. $308, $318: not асс. pl.).
```


## [2026-09-05T20:31:22.883Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nlines=open('BRT.txt',encoding='utf-8',errors='replace').read().split('\\n')\ndef near(t,i,w=60):\n    out=[]\n    for j in range(max(0,i-w),min(len(lines),i+w)):\n        s=lines[j].strip()\n        if re.fullmatch(r'\\d{3,4}',s):\n            out.append((j+1,s))\n    print(t,out)\nnear('arethna',5498)\nnear('frararathni',18270)\nnear('aurusa',5350)\nEOF",
 "description": "Find Bartholomae column numbers"
}
```


### [2026-09-05T20:31:24.508Z] TOOL RESULT

```
arethna [(5446, '193')]
frararathni []
aurusa [(5351, '190')]
```


## [2026-09-05T20:31:32.330Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR>=5350 && NR<=5560' BRT.txt | grep -n \"auru\\|weiss\\|weiß\" | head -20\necho \"=== find col markers 190-200\"\npython3 - <<'EOF'\nimport re\nlines=open('BRT.txt',encoding='utf-8',errors='replace').read().split('\\n')\nfor j in range(5300,5620):\n    s=lines[j].strip()\n    if re.fullmatch(r'\\d{3,4}',s) or 'auru' in s.lower()[:20]:\n        print(j+1,repr(lines[j][:80]))\nEOF",
 "description": "Locate Bartholomae auruša entry"
}
```


### [2026-09-05T20:31:34.017Z] TOOL RESULT

```
1:aurusa-
34:•  j.,  g-  auruna-  'wild,  fenis,  saevus': maSsahe  kihrpa  'na^e  Yt.  l4- 23;  —  'na/a gairisiicö  sizdraca  ravascarätö  "die  wilden (Tiere),  die  in  den  Bergen  hausen,  und die  scheuen,  die  in  den  Ebenen  streifen" Yt.  ^36;  —  alityS  mos  aia  syasdal{sA.) yavaf  ahmal  'nä  xra/strä  ".  .  soweit  als vor  uns  die  wilden  Raubtiere"  \.34. 9.
37:•  j.  auruäa-  Adj.  'weiss',  1)  von  Tieren: pttsüm  .  .  'hm  vH  vohu.gaon^m  vä  "ein weisses  oder  schwarzes  Schaf  Yt.ÄsS; —  aspa/ie  ktkrpa  'iahe .  .  aspahe  kihrpa sämahe  "in  Gestalt  eines  weissen  Rosses . .  in  Gestalt  eines  schwarzen  Rosses"  Vt. Ä  18-21";  —  aurvants  'la  raoxsna  fnl- ä)r»sra  Y. 57, 37;  YL  JO.  136.  z)  sonst: srlra  i-a  auhtn  blzava  'h  (ND.)  Yt.5.7;
43:=«,  -weiss'.    -    .;  Vgl.   zSt.  Bd.  >.  7Y-  /,; ,      It-  ^-  180  No.
48:•  j.  auru5a.bäzav-    Adj.    (auch   : 'weissarmiß':  kaininö  kihrpa  . .  "Zfh  \^o.,  .  ^  ,,     ,
51:•  j.  auniSaspa-  Adj.   'des  Rosse   weiss  |     AbleiL  -  Zum  V.  a,^--.   -   mp.  (Fü.)  a^i, sind':  mi'irim  °f)m  Yt/o.ioa.  1     np.  nn,  «f/.
=== find col markers 190-200
5350 'aurusa-'
5351 '190'
5383 "•  j.,  g-  auruna-  'wild,  fenis,  saevus': maSsahe  kihrpa  'na^e  Yt.  l4- 2"
5386 "•  j.  auruäa-  Adj.  'weiss',  1)  von  Tieren: pttsüm  .  .  'hm  vH  vohu.gao"
5397 '•  j.  auru5a.bäzav-    Adj.    (auch   : \'weissarmiß\':  kaininö  kihrpa  . .  "'
5446 '193'
```


## [2026-09-05T20:31:42.465Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '5386,5405p' BRT.txt\necho \"=== arethna full\"\nsed -n '5494,5505p' BRT.txt\necho \"=== frararathni region\"\nsed -n '18262,18275p' BRT.txt\npython3 - <<'EOF'\nimport re\nlines=open('BRT.txt',encoding='utf-8',errors='replace').read().split('\\n')\nfor j in range(18150,18320):\n    s=lines[j].strip()\n    if re.fullmatch(r'\\d{3,4}',s): print('colmark',j+1,s)\nEOF",
 "description": "Bartholomae entries in full"
}
```


### [2026-09-05T20:31:44.282Z] TOOL RESULT

```
•  j.  auruäa-  Adj.  'weiss',  1)  von  Tieren: pttsüm  .  .  'hm  vH  vohu.gaon^m  vä  "ein weisses  oder  schwarzes  Schaf  Yt.ÄsS; —  aspa/ie  ktkrpa  'iahe .  .  aspahe  kihrpa sämahe  "in  Gestalt  eines  weissen  Rosses . .  in  Gestalt  eines  schwarzen  Rosses"  Vt. Ä  18-21";  —  aurvants  'la  raoxsna  fnl- ä)r»sra  Y. 57, 37;  YL  JO.  136.  z)  sonst: srlra  i-a  auhtn  blzava  'h  (ND.)  Yt.5.7;
dby  Google
auniäa.bäzav-
*ar9tay-
—  yt^he  urva  . .  "/j  raoxlnU  fräd?r?srS  •  j.  ar^lavan-  m.  EN.  eines  Gläubigen: Yt  JJ.  8i;  —  tislrlm  .  ,   "hm   raoxsti>m  •  °jaonaie''>  alaenS  Yt  ij.iij. frädinsram  YtA'.a.  ;     Abldi.  aus  "arija-  (svs.  ««>*-),  eig.  '«-ert.
KompA.  —  i\.a,u,A-  Adj.  'rüllich',  mp. (Pü.)       voll';  s.  a^/tf^r^«/-.  —  D    Ihero.;  vgl.BTHL.
=«,  -weiss'.    -    .;  Vgl.   zSt.  Bd.  >.  7Y-  /,; ,      It-  ^-  180  No.
asp  karf  i  sp7i  . .  /fl  humSnik  1  asfi  i  sy.U:      .  j,  ar«Jah-  n.  'Wert,  Preis';  Dur  AS.  'i:
u  (GS.)
den  ^^'ert,  Preis  von  — '  (Gen.  oder  Instr.
oder  Akk.);  aspö  (sd.)  ayryi).hmo  .
•  j.  auru5a.bäzav-    Adj.    (auch   : 'weissarmiß':  kaininö  kihrpa  . .  "Zfh  \^o.,  .  ^  ,,     ,
Pü! Tarii!  i.ä:r,t.  ^  •)  Vgl.  sumü/,  Rv.  j.  32. 7 1  N-  *5;  "  -  ■  "TriAam  mazyät  gava  dmu und  Panihi  4.  1.  67.  1 "/?  V.  j.  42 ;  42  ^;  —  nmUnS^aillm  bisazyat
V-  .,.,,„  \mt»m3>n  staonm  "Ja  V.7.41:  41J,  43'.
•  j.  auniSaspa-  Adj.   'des  Rosse   weiss  |     AbleiL  -  Zum  V.  a,^--.   -   mp.  (Fü.)  a^i, sind':  mi'irim  °f)m  Yt/o.ioa.  1     np.  nn,  «f/.
Komp.!  a«™™.+fl0.-.  I  ♦  j   arajahvant-  m.  EN.  eines  Gläubigem
*arka'dray-'>  m.  Name  eines  Beres   'jamikaiö  türahe  asaonS  1
(in  Persien?):  'drisnäma"  kauf<^  ^\\.i.\
Eig.  vi].  'Burg  l^aria-  m.,  np.  if'i' ;  vgl,  lat.  a) tragend';    vgl.    FuV  V,'l.  35.  61,   jy.  53. ')  Ausg.  araka'.
■  V.  'wert  s
=== arethna full
•  j.  ara^a'mant-  Adj.  sva.  'an^a-z rasnvö  'mal  (ASn.)'*  bairilta  (sd.) , .  tlyüm nijaynUia  Yti2.7.
>)  Man  verlangte  ASm.
•  j.  arflfl-a'van-  Adj.  'gegen  den  ein  Rechts- streit erhoben  ist,  dem  der  Prozess  gemacht wird,  verklagt,  angeklagt':  lal  arüalie (sd.)  tat  'i-anB  F.2;b.
pü.!  däUulünömand,  tt\.:  fasmSr.
•  j.  'araöna-  m.  'Ellenbogen':  -^nd  (ND.) F-,?g.
Vgl. /j-jj-dim".  —  np.  araii  (aus  *ar*«");  vgl. ai.  nralaäy-  m.  —  Pü.:  nti%  (in  Aw.-Buchsl.).
•  j.  'araStia-  n.  Name  eines  daiiAscXitn
Tiers'':  yas^  ^Jita  nSit  aiwijinizSnti  aÜsVa (sd.)  'iiaisca  (als  Subj.)  .  .  Y't.5.50. >l  Falsches  bei  DST.  ZA.  2,  388.
•  j.  araflya-"  n.  'Rechtshandel,  Prozess: kahmi  kahmiUt . .  -yanam  "^waeis  biwiva Yt.7/.5.
Ableit.  aus  'jwirt-.  —  ai.  vgl.  ärlhya-.  Adj.  — Pi.:  dj/as/äii.  —  ')  Lesung  unsicher;  vgl.Yt. 4.  5,  wo  rai%lt,anqm.
•  j,  aroS-ra-  n.  'Gerichtsverhandlung':  yö alta  (sd.)  pairi  "ra  (IS.)  frazanattt  F.  5.
Vgl.  «r>%a-.  —  Pü.:  i--<r,-,  5.  daiu  Btul.  IF.
=== frararathni region
•  j.  ^frirayatraS-a-**  m.  EN.  eines  Gläu- bigen: '"^aAe  aiaenS  Yt/J.  108.
Eig,  'den  (Streit)wagen  in  Bewegung  setzend'; frä+'ärayanl;  lum  V.  'ar-.  —  •)  So  J  lO, Mf  3i  NA.  mit  F  i  /räyalj'.  Ich  glaube,  dass die  drei  hinter  einander  genannten  Gläubigen, jedenfalls  drei  Brüder,  Reimnamen  hatten: därayal,ra%a-, /rar' ,  siär'.
•  j.  frä-rätay-  f.  'Freigebigkeit,  Mildtätig- keit', nur  in  Verbindung  mit  vTdlsä-  (sA): tä  nS..°räiti  tä  vldlse  uzjamyqn yS  staota yesnya  Y.55. 3;  —  hSc3  tiH  fsBmh  .. aiwyäxlayatü  kadä  asä/ä  vilsträ/ä  °rä- Hca  vldlSayücä  ainiUca  ..  Y.5Ä4;  — 'räitfi'a  *vTälsasM  antar?  *3^aäalnsi^ asaonis  P.  jff ;  —  in  Dual  Verbindung:  °räili ■i'ldfh  yazamaide  yat  asli  atitar?  :^ädal- nais  asaotiTl  Vr.  21.  3  •' ;  —  °räili  *vldXs€ (?)'>  ainitii  ags's  *växsf  f.  26.
*)  Freigebigkeit  gegenüber  Religionsgenossen wird  oft  genug  eingeschärft;  vgl.  iB.  unter 'dS%ra-,  dagegen  halte  man  F.  50  unter  itaod-.
Pü.-. /rä/ rälU.  —  ■)  Hds.  vlidim.
\. /räräi%yam(m  V.  JA:  lies /rärniV".
•  j.  frl'riflmdräjah-  n.  'I.änge  eines  Fr. (Elle)'*':  °Js yai  hulkanqm  frabazu.dmjö yat  naptanqm  "in  der  Länge  eines  Fr. von  trockenem,  eines  Frab.  von  feuchtem Holz"  V.  7. 30,  33 ;  29,  5.  4  PiiZ.3;  —  *"> N.  10  j  ".
*)  D.  i.  das  Mass  vom  Ellenbogen  bis  zu  den Fingerspitzen,  doppell  so  lang  als  ein  vilaslay- (sd.),  halb  so  lang  als  ein  frabiiaV'  (sd.);  vgl. West  SBE.  £.  99,  Bthl.  AT.  2.  43,  ferner  F. 3/  at).
*frS-r&nay-  n.  'Elle';  S.  dfllö  ai.  atalaiy- 'Ellenbogen,  Elle'  und  Btmi.  BB.  ty.  Iii; s.  auch  'ar3%na-;  mp.  fräräsl  ist  eine  Ver- unstaltung des  Aw.-Worts.  —  Pii.:  ftäc adrln  (or^n?)])  drahnii.  —  »  Hds.  •ra%tK.- dr".  —  »)  S.  zu  gämait:  —  1)  S.  zu  ^arAna-.
'Mnay-  loaa
•  j.  itä'x&zay-  m,  EN.  eines  Gläubigen: 'röis  türahe  a^aonS  Yt  y,  123.
Eig.  Bed.?     Vgl.  zBed.  iirrziräs-i g.  frärinti  V.  46.  3 :  s.  'a*--.
•  j.  frä-urustay-  f.  *-?  — :   nSil  'H  N.  2. Pu.:  fehlt
•  j.  frä.uruzda-payah-  Adj.  'dem  die Milch  verhalten  ist,  was  keine  Milch  (zum Säugen)  hat',  von  weiblichen  Tieren:  pa- ssu?  ganbus  yDütahe  (sd.)  °yai>ks  A.3.  3.
colmark 18162 1016
```


## [2026-09-05T20:32:08.588Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ntxt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\n# find leaf containing آلگونه\nfor i,L in enumerate(leaves):\n    if 'آلگونه' in L:\n        print('leaf',i, 'tag:', L[:120].replace('\\n',' | '))\nprint('---- آرنج leaves')\nfor i,L in enumerate(leaves):\n    if 'آرنج' in L and i<400:\n        print('leaf',i, L[:100].replace('\\n',' | '))\nEOF",
 "description": "Locate Borhan leaves"
}
```


### [2026-09-05T20:32:10.518Z] TOOL RESULT

```
leaf 267 tag: کت ۱ آننک | و امٌال اینها باشد 0.٩‏ | ۲ لر - بروزن لاغر ۰ کقل و رین را | کوند مطلقا ۴ . | ۷ ۷ ۱ | بمعنی آلراست ک هکفل وسرین باشد م
---- آرنج leaves
leaf 238 آرا | آداه بروزن خارا . آرایش. وآرایش | کننده و آراینده را کویند همچو خن آرا | و بزمآرا وامی باینمعتی هم ه
leaf 242 ]دی ح بکر الث و رايع و سکون | تحتانی ۰ بمعنی ممنوی باشد که در مقابل لفظی | است ۰ چه آرش بمعنی «معنی» است
leaf 316 لرسانیفون | ارسانقون » با اك بالف کشیده | و نون تحتانی رسیده و فاف مضموم بواو و نون | زده » بلفت‌بونانی زر
leaf 323 از یا | وجیم. , بمعنی آرنج است ت که بندگاه ساعد | وبازو باشد وبحربی مرفق خوانند . | ار ندان بر وزن‌قلمدان
```


## [2026-09-05T20:32:17.476Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ntxt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\nprint(\"======= leaf 266\")\nprint(leaves[266][:2500])\nprint(\"======= leaf 267\")\nprint(leaves[267][:3000])\nEOF",
 "description": "Print Borhan leaves 266-267"
}
```


### [2026-09-05T20:32:19.254Z] TOOL RESULT

```
======= leaf 266
۲ ۰ وا
آلان ِ پروزن‌بالان » ام ولایتی ونم
محله ایست ویسنی کوبند شهرست در ت رکستان
و نام کوهی‌هم هست1" .
لاو بسکون واو, آ تس شمله با را
کوند. و بفتح همزه‌هم درست‌است ۷ .
عندی ام درختی است که ازیخ‌آن دنگه سرخی
حاسل شودمانند رنگه رونای وبدان جامه رنگه
کنند و در دواها نیز بکار آید .
! لا » پروزنکلا»
بمعتی‌اول آل اس تکه
رخف سرنگه باشد .89 ۳
]لاس « یسکون لاوه « بنتح واو» بمعنی دیگدان و
سیخ ی فا 221 جایکه درآن آش روش نکنند - دوپارچشچوب
وانگفت راگونند ۴ رانیز کوبند که اطفال‌بدان‌بازی کنند یکی‌بز رکه
٩‏ ( - قدر سه زجب و دیگر یکوجك بمقدار بك‌فیشه
ختح لام » بمعنی لاله - وس‌های چوب کوچاك نیز میباشد .
ی اند وت ا سا و تن
همزه هم درست است ۴ . 9 آلودگی و عیب - ترداهشی وفسق وفجوروخیات
اک آزد ۱ مر خن آ من
۴ - تاب قپرش تیغ را الماس کرد برق خشمش کوه را آلا کرد
۱ سراح‌آالدین راجی « لفت نامه ».
۴ - مرش لال ( سرخ ) . پهلوی 21226 « بندهشن. یمبشی ۱۹۰۸ ص 4۱۱۷. فارسی نیز
لاله ولاله » طبری طفاغاهظ < واژه نامه۸4۳ ». ۴ بش ازه»۱۲۰ جنس مختلف آلاله
وجود دازد و آلالمهای اصلی شامل ۷۲اه 5ناللات(تلا 210 و جنس های فرعی‌آن وشفایق نعمانی
علانامعا عدمصعمه ر ختایق یچ عتلهانا ونافتهن لت.. . « کل کلاب
۷ ببعد * و رك : فرهنگه روستابی 4۸ :
چون دواتی بسدین است خراسانی وا باز کرده سرالاله بطرف‌چمنا «منوچهری4».
۵ و اران . از رشة 27727 ( آربائی ) وآن نام قومی است که در شمال آذربابجان
سکن دائتند و سرزمن آنانرا بنام ابشان اران والان خوانده اند . ۱ - « سخن اندر
ناحیت الان ( ۸120 ) و شهرهای وی - مشرق و جنوب وی سربر است و مغرب وی روم است
و شمال وی دربای گرز ( 42۷172 ) و بجنا خزرانت ؛ و اين تاحیتی است اندر شکتگی ها
و کوهها وجابی بانسمت , و ملکشان ترساست و ایشانرا هزار ده است بز رکه و اندرمیان مردمانی
اند ترسا ومردمانی بت پرستند و مردمان وی گروهی کوهی اند و گررهی دشتی . » « حدودالعالم
هرآن۱۰۰ * ورك: تعلیقات حیئورسکی برهمین کتاب ص 44 1-8 4. ۷ - نیز بمعنی‌شمله :
بر اوج گنبد گردون از آن بتابد هور که بات از تف قندیل میتی آلاو .
۱ یع ‏ اف قفا آ2ن
۵ آلاچق - ترکی‌الاجو ختح همزه وضم جیم؛ بممنی سراپرده و سایبان دوستونیاست
« کاشخری ص ۱۲۲ :
چیست خود آلاچق آن تر کمان پیش یی نره یبلان جهان
دمثنوی 4 ص۳۰۸ » < ندان ۹-۵:۴ص ۵ >
(برهان قاطع ۱۳)
======= leaf 267
کت ۱ آننک
و امٌال اینها باشد 0.٩‏
۲ لر - بروزن لاغر ۰ کقل و رین را
کوند مطلقا ۴ .
۷ ۷ ۱
بمعنی آلراست ک هکفل وسرین باشد مطلناً ۴ .
] ل‌طمفا - برکون ثالت » مهرودگین |
یادشاهان را گوبنده ویضی کویند اين, لفث ترکی .
است ؟ .
۲ لفده * - باغین قطمداربروزن آزرده,
بمعنی قهرآلود وخشمگین - وجنگه آورباشد .
۲ لو زه رن اه نش فاد
است و آن‌سرخی باش که زنان برروی مالند ۰
] فتن - بافاء بروزن ومعن ی آشفتن باشت.
۲ قشته مه پروژن و معتی آخفته ۱ هت
رردیکی و کی ودروش نامراد را نیز گوء بند.
ای او سار ء بل
الطيب را کویند ودردواها بکار برند ۷ - و مصغر
آهرهت ۸
۲ لگو نه سکاف و بروزن‌وععتی
آلفونه است که غازه و سرخی زنان باشد ٩۳‏ .
] ل معصفر « بکر ثالث ۳ نوعی از
ماهی درم دار ۳ 9 را نیز
نته‌اند .
آ مج - بن تلد وسکون نون وجیم»
آلوچه را کویند و آن میومایست ممروف ‏
آ لگ « بروزن آهنکه . کوی بلشد
که در اطراف قلمه‌حا بجهث محاصره و کرفتن
آ نکنند ومورچال همان است- و بسنی دبولربرا
کوبند که بجهت محافظت خود و حواله کماز
پرای قلمه سازند - وجنمی ازمردم را نیز گویند
که مردم. بیرون قلمه جابجا بواسطهٌ کرفتن قلمه
عصسدی: لشت‌نامه ».
۴ التمفا . اللون نمفا » هر پادشاهان ترث که با م رکب سرخ برفرمانها فش میکردد ۰
اين فرامن را منصوصاً « بارليغ التون تمغا * مینامیدند . «جنتابی ۳۱ *. ه‌ لغتی دد
« آرغدء » . رك : آرغده. ۲ -.لفتی درآ لگونه . رك : آلگونه .
۰ ۷ - از تبانات پست سبز است که دد ته اهر با روی آب شیرین با شور دیده میشود .
با گ نه رشه دارد نه ساقه نه ب رگهه . ته اش دارای « کلور فبل » است و شکهای مختلف دنده
ميشود. طول آن ممکن است مندها متر برسد. ركك : فرهشگه روستابی 4۸ - ۹٩‏ ؛ ورگ : آله.
4,۸ : آل. ٩‏ مرکب از: آل (سرج) + کونه (رنگه ).
۰- آن بناکوی کز ساکویی ‏ " بر کشيده است آلگونه بسيم
1 شهید بلخی . « لغت نامه *.
» آئبالو 6مع۳1ه وناصطظ درخئی است از وتا بادامی ها از تیرژ کل
مرخبان . « کل گلاب ۲۲۳۷>. 4 آلتمغا - را: آل طمفا. » آلنوی - ترکی
بمعنی طلا « کاشنری ] : ۱۰۵ > :
ظای و مثدیل وگل ازآلتون بگیر ۷ بگرمابه دوم ای «ا کززیر
« مثنوی ۳ ص 0۵۱۱ > < نداب ۳ : ۵ ٩‏ س۵ ٩‏
```


## [2026-09-05T20:32:39.696Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ntxt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\nprint(\"======= leaf 264\"); print(leaves[264][:1800])\nprint(\"======= leaf 265\"); print(leaves[265][:3000])\nEOF",
 "description": "Print Borhan leaves 264-265"
}
```


### [2026-09-05T20:32:41.407Z] TOOL RESULT

```
======= leaf 264
و بکرکاف فارسی محکم بتهراگویند ۱ .
] گففت - بنتح کاف نک
وغای فرشت شت » ت» آزارورنج وهمجنت وت با ریز
و بکس‌کاف فارسی نیز همین معنی دارد ۴
آ گن باکاف فارسی‌بروزن دأمن؛بمعنی
آکندنی باشد مثل آنچه درجامه و لحافوباش
کنند از پثبه و پشم وغیره - وبمعنی پر کننده
که فاعل پر کردن باشد , عم آعده است
کنج بفتح‌کاف ثازی بروزن نارنج؛
قلابی باشد که بدان يخ در بخدان اندازند؟ - و
بقةح کاف‌فارسی بمعنی پروهملو باشد؟ - وبمعنی
روده و آممای کوسیند هم‌هست که انرا با گوشت
و برنج و مصالح‌بر کرده باشند و بعربی «عصیب
ند .
آ "گثف « بر وزن پابند , ماضی آ"کندن
وی رکردن باشد بعنی پر کرد وانباشت - و بمعنی
پر کرده‌شده عم آمده است- و پر کردنی را پیز
ند .
(۱) چك : الپاشتن .
۱ - رد کته :
دلش خود ز تد تخت د که کشته بود
۳۳ بنالم از ۱ ن رو زکارو این کفت
و اماشتن(۱) ۷ .
نده بروزن‌ساز نده» بمعثی‌پر کرده
شدء و انباشته )۱( شده پاشذب و طوبله واصمطبل
و پایگاه را یز گوشد. و آخوردواب راهم کفته
اند ویعربی «معلف» خوانند. و بمضی باين معنی
جنم‌کاف آورده‌اند - و بمعنی بزر که و فربه لیز
ات استت و بمعئی آ یاه کردن ومعمور ساختن
هست .
| گنده گوش - جنم‌کاف فارسی و
سکون واووشین فرشت ۰ بمعنی | لوده دامن است
وناشتوا- رچیزی در کوش[ کنده را نز گویند.
] گنش » بتح تالث و کس نون‌وسکون
شین نقطه دار » بمعنی پر کردن باشد - و بمعتی
هرچیز که درون چیزها را بدان پر کنند وربی
«حشو» خواند ۸ .
| گنه « بنتح ثاك ونون » بمعنی آخر
و پیله که دربالش و هالی ولحاف و اثال آن پر
(۷) چك : اپاشته
بثیمار اغربرت! کشته بود. فردوسی
۶« لت نایه ».
که هرچه‌ید سب شادی وشاط برفت۰
اب اج پین هت هم میک تا( : انجیلکنتك )
قاسد و عمیوب و بیهوده . ۴ ره : اکح وآکج. ۴ - درکلمات مر کب مانند:
جگر آکنج ( جگرآکند ) . رك : لت نامه : ۱ کنج .
9 - عیب وکرده برون کن تو زود و برهم کوب
جکر بیازن و ۲ گنج را بامان کن . کسائی « لت ناعه >.
۲ - و آ کندن , بپلوی 2080081 « اونوالا۲۵ >. اش ]۱ کت خی
و آبادان کردن :
میا کند کنج وسپاه ورا
رف .]کف :
چون راست بود خوب نماید سخن
بباراست ابوان و کد ورا
======= leaf 265
و شین فرشت » بممنی در آوجخته باشد چه اندر
آکیشید پمنی الدر آوشت - و چنکه درچیزی
زده ودراز کردمرا نیز گویند.- وبمعنی دراز کردن
و درآوسنتن بجیزی هم هست 4 ۱
آ گین عبروزن آبن؛ بمعنی مالامال‌ویر
و آغشته و آ کنده باشد وبمعنی فربه نیزآمده
اس تب که هض لاغرباشد ٩‏ .
آل ت‌ِ مسکون لام بروزن زال » سرخ
یمرنگ را کوبند ۷ - و نام مرضی است مهلك
که زنان نوزاییده را تاهفت روز واقع مشود و
اعتفاد عوام آست که جنیی باشد باین نام که
مز احمت بر نان‌نوزاییده عیرساند - ونوعی ازماهی
هم‌صت - ودرعربی مرابرا گویند وآن‌بضاری
باشد آب‌نما - وبمعتی‌اولاد وعشیرت وقوم‌هم آمده
است.- و چیزی که مانشد سراب درصیح وشام‌از
دور نمایان میشود- وبتر کی مهرولگین پادشاهان
باشد ٩‏ - وامرستدن هم‌هست یمنی بستان - ودر .
گذارند ٩‏ .
گثیدن؟ - بروزن پااکنیدن » بمعنی
انباشتن (۱) و پرساختن باشد ؟  .‏
آ کو - نم کاف تازی وسکون و او ء
بوم را گوبند و آن پرنده امست شوم ونامبارگ .
آ گوز باکاف‌فارسی بروزن ساطور »
خشت یخته را کویند و آجور ععرب آئت .
گوش ع باکاف فارسی» بروژن وعمنی
آغوش است که بر وبغل باشد - وپرستار وبنده
راهم میگویند که درمقابل آژاد است ۴ -
۲ "لو شیدن - بروزن ومعتی آغوشیدن
است که حریر کشیدن و دریش لکرفتن باشد .
آ گون - بروزن و معتی واژون‌ونگون
باشد چه‌سراکون سرنگون راگوند ۵ . *
] گیش ه بکر ثاك وسکون تحتابی
(۱) چك : اپاختن . ۱
۱ - نیزآکنه: شد زمستان و زجودت بنه ای میخواهم ابرء و آستر وآکنه‌ای میخواحم.
سوژنی . < لفت نامه »
۴ نیز آکنیدن. . ۴ - یز بممنی جای دادن و دفن‌کردن ؛ زبر خاك کردن .
۴ ۲ کوش نامی ازنامپای پرستاران تراست * لنت‌نامه » رك : آخوش. ۵ _ ایا
این کسه جزدر حال ت رکب مستعمل نست ۶ لفت نامه *. ۱ - یزیمعنی حشوه آکنه :
خود پر کبوتران میلوست کا کین چهار بالش اوست . خافانی
و در کلمات م رکبه بممئی : آلود » مرصم » اباشته , ماد و گونه » دارا و صاحب . اندود آید
همچون : زهرا کین . کوهرآ کین » ضیقآ کین , طلسم آکین » عشرتآ کین » زرا کین . ر:
لت نامه.. . ۷ - اوستا شتاکداتلا2 ( سفید ) , ساسکریت 870155 ( سرخ رنگ ) » در
ترجمه و نی پهلوی 85115 ( سفید ) « پارتولمه ۱4۰ - ۰۰۹۱ طبری اه (مبز ) ,
مازندران ی کنولی ام ( سرخ وکم رنگ ) « واژه نامه ۵ » :
شتم پرآن ناقاً آل پبکر فکندم براو نطع ودلو مصلی « منوچهری۱۱4>.
۱ ۸ - ظاهراً همان که امروز قزل آلا کویند. ٩‏ - در ث کی بمعنی حنور» پیشانی ؛
خدعه + مکر» شنگرف سرخ» مهر؛ جای مهرسلاطین ترا که با م رکب سرخ برفرامین نفش میشد
« جنالی ۲٩‏ . ۵ آکنیده - ] کنده :
منم در کشور عشقت خنیده دلی از مهر روت آکنیده شاکربخاری « لفت نامه * .
]له _ مخفف آگاه» رك : ۲گاه. آیاری - رك : آتش بهرام .
۰ آگیبیفی - و آکیشبدن بممنی آویختن و پیچیدن . رك : کش .
```


## [2026-09-05T20:33:02.769Z] TOOL CALL #35: Bash

```json
{
 "command": "sed -n '1,60p' tools/fetch_source.py",
 "description": "Inspect fetch_source.py"
}
```


### [2026-09-05T20:33:02.881Z] TOOL RESULT

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


## [2026-09-05T20:33:13.505Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wiktionary.org/wiki/%D8%A2%D9%84\" \\\n \"https://en.wiktionary.org/wiki/%D8%A2%D8%B1%D9%86%D8%AC\" \\\n \"https://www.etymonline.com/word/elbow\" \\\n \"https://www.etymonline.com/word/elk\" \\\n \"https://www.etymonline.com/word/elm\" \\\n \"https://www.etymonline.com/word/lamb\" \\\n \"https://www.etymonline.com/word/alder\" \\\n ; do echo \"### $u\"; python3 tools/fetch_source.py \"$u\" --note \"page 152 (El 2 / El 3): verifying Persian al, arenj and the Germanic elm/elk/lamb/elbow branches\"; done",
 "description": "Archive Wiktionary and Etymonline pages"
}
```


### [2026-09-05T20:33:18.963Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/%D8%A2%D9%84
/home/sfmqrb/git/rishe/data/verification/sources/web/e7d5093de14dbfab.txt
### https://en.wiktionary.org/wiki/%D8%A2%D8%B1%D9%86%D8%AC
/home/sfmqrb/git/rishe/data/verification/sources/web/d70aeaf1eadb9c42.txt
### https://www.etymonline.com/word/elbow
/home/sfmqrb/git/rishe/data/verification/sources/web/65affeb76ac87b68.txt
### https://www.etymonline.com/word/elk
/home/sfmqrb/git/rishe/data/verification/sources/web/6b6e66e59b0fc9a7.txt
### https://www.etymonline.com/word/elm
/home/sfmqrb/git/rishe/data/verification/sources/web/e8c78aa91f01ba6a.txt
### https://www.etymonline.com/word/lamb
/home/sfmqrb/git/rishe/data/verification/sources/web/29474facdb6e63a4.txt
### https://www.etymonline.com/word/alder
/home/sfmqrb/git/rishe/data/verification/sources/web/357887f43952c447.txt
```


## [2026-09-05T20:33:22.293Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"#### AL\"; grep -n -A30 \"Persian\" e7d5093de14dbfab.txt | head -60\necho; echo \"#### ARENJ\"; sed -n '1,120p' d70aeaf1eadb9c42.txt | grep -n \".\" | sed -n '20,90p'",
 "description": "Read archived Wiktionary pages"
}
```


### [2026-09-05T20:33:22.405Z] TOOL RESULT

```
#### AL
144: Persian 
145-
146: Toggle Persian subsection 
147-
148- 4.1 
149- Pronunciation 
150-
151- 4.2 
152- Etymology 1 
153-
154- 4.2.1 
155- Noun 
156-
157- 4.3 
158- Etymology 2 
159-
160- 4.3.1 
161- Adjective 
162-
163- 4.3.1.1 
164- Derived terms 
165-
166- 4.4 
167- References 
168-
169- 5 
170- Ushojo 
171-
172- Toggle Ushojo subsection 
173-
174- 5.1 
175- Noun 
176-
--
358: → Persian: آل ( âl ) 
359-
360- Etymology 2
361- [ edit ] 
362-
363- Root 
364-
365- ء و ل ( ʔ w l ) 
366-
367- 16 terms 
368-
369- Pronunciation
370- [ edit ] 
371-
372- IPA ( key ) : /ʔaː.la/ 
373-
374- Verb
375- [ edit ] 
376-
377- آلَ • ( ʔāla ) I ( non-past يَؤُولُ ( yaʔūlu ) , verbal noun أَوْل ( ʔawl ) or إِيَال ( ʔiyāl ) or أَيْلُولَة ( ʔaylūla ) ) 
378-
379- to return 
380-
381- to turn into , to become [ with إِلَى ( ʔilā ) ]
382- Synonyms: see Thesaurus: صار 
383-

#### ARENJ
27: Special pages 
29: Search 
31: Search 
33: Appearance 
35: Donations 
37: Create account 
39: Log in 
41: Personal tools 
43: Donations 
45: Create account 
47: Log in 
49: Contents
51: move to sidebar 
52: hide 
54: Beginning
56: 1 
57: Persian 
59: Toggle Persian subsection 
61: 1.1 
62: Alternative forms 
64: 1.2 
65: Etymology 
67: 1.3 
68: Pronunciation 
70: 1.4 
71: Noun 
73: 1.4.1 
74: Descendants 
76: 1.5 
77: Further reading 
79: Toggle the table of contents 
81: آرنج 
83: 7 languages 
85: فارسی 
86: Bahasa Indonesia 
87: Kurdî 
88: ລາວ 
89: Malagasy 
90: Polski 
91: Русский 
93: Entry 
95: Discussion 
97: English 
99: Read 
101: Edit 
103: View history 
105: Tools 
107: Tools
109: move to sidebar 
110: hide 
112: Actions
114: Read 
116: Edit 
118: View history 
120: General
```


## [2026-09-05T20:33:27.414Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"#### ARENJ etym\"; awk 'NR>150' d70aeaf1eadb9c42.txt | grep -n -m1 -A45 \"^ Etymology\" \necho; echo \"#### AL persian section\"; awk 'NR>380' e7d5093de14dbfab.txt | grep -n -B3 -A40 \"Etymology 1\" | head -80",
 "description": "Extract etymology sections"
}
```


### [2026-09-05T20:33:30.206Z] TOOL RESULT

```
#### ARENJ etym
7: Etymology
8- [ edit ] 
9-
10- From Middle Persian [Book Pahlavi needed] ( ʾplnc /⁠āranǰ⁠⁠/ ) , borrowed from Sogdian 𐫀𐫀𐫡𐫀𐫏𐫗𐫝 ( ʾʾrʾync /⁠ārinǰ⁠⁠/ ) , ultimately from Proto-Indo-Iranian *Haratníš . Compare Sanskrit अरत्नि ( aratni ) .
11-
12- Pronunciation
13- [ edit ] 
14-
15- ( Classical Persian ) IPA ( key ) : /ʔaː.ˈrand͡ʒ/ 
16-
17- ( Dari, formal ) IPA ( key ) : [ʔɑː.ɾánd͡ʒ] 
18-
19- ( Dari, formal ) IPA ( key ) : [ʔɑː.ɾánd͡ʒ] 
20- ( Kabuli ) IPA ( key ) : [ʔɑː.ɾánd͡ʒ] 
21-
22- ( Hazaragi ) IPA ( key ) : [ʔɔː.ɾánd͡ʒ̥] 
23-
24- ( Iran, formal ) IPA ( key ) : [ʔɒː.ɹǽnd͡ʒ̥] 
25-
26- ( Tajik, formal ) IPA ( key ) : [ʔɔ.ɾínd͡ʒ] 
27-
28- Rhymes: -and͡ʒ 
29-
30- Readings
31-
32- Classical reading ? 
33-
34- āranj
35-
36- Dari reading ? 
37-
38- āranj
39-
40- Iranian reading ? 
41-
42- âranj
43-
44- Tajik reading ? 
45-
46- orinj
47-
48- Noun
49- [ edit ] 
50-
51- آرنج • ( āranj / âranj ) ( plural آرنج‌ها ( āranj-hā / âranj-hâ ) , Tajik spelling оринҷ ) 
52-

#### AL persian section
509-
510- ալ ( al ) — Armeno-Turkish 
511-
512: Etymology 1
513- [ edit ] 
514-
515- From Arabic آل ( ʔāl ) .
516-
517- Noun
518- [ edit ] 
519-
520- آل • ( al ) 
521-
522- family 
523-
524- References
525- [ edit ] 
526-
527- Mallouf, Nassif ( 1856 ), Dictionnaire français-turc , 2nd edition, Paris: Maisonneuve, page 261 
528-
529- Etymology 2
530- [ edit ] 
531-
532- From Proto-Turkic *āl .
533-
534- Adjective
535- [ edit ] 
536-
537- آل • ( al ) 
538-
539- crimson , red 
540-
541- Descendants
542- [ edit ] 
543-
544- Turkish: al 
545-
546- → Albanian: all 
547-
548- → Armenian: ալ ( al ) 
549-
550- → Greek: άλικος ( álikos , “ crimson ” ) 
551-
552- See also
--
617-
618- ol
619-
620: Etymology 1
621- [ edit ] 
622-
623- Borrowed from Arabic آل ( ʔāl ) .
624-
625- Noun
626- [ edit ] 
627-
628- آل • ( âl ) ( Tajik spelling ол ) 
629-
630- ( literary or historical ) family , lineage , house 
631-
632- Etymology 2
633- [ edit ] 
634-
635- Émile Benveniste claims that āl-γonak , the precursor of modern آلگونه ( âlgune ) , is attested and connects this to the Persian female name Ἀλογούνη ( Alogoúnē ) mentioned in Ctesias . [ 1 ] Harold Walter Bailey suggests that this is a merger of two Proto-Iranian [Term?] roots, *āla- and *harda- , cf. Avestan 𐬵𐬀𐬭𐬆𐬛𐬀 ( harəda ) . [ 2 ] Walther Hinz similarly posits Proto-Iranian *Hr̥da- from Proto-Indo-European *h₁rewdʰ- ( “ red ” ) and suggests that this is the source of آلو ( âlu , “ plum ” ) and آله ( âloh , “ eagle ” ) , [ 3 ] though the latter is also traced to a different Indo-European root. The link to Proto-Turkic *āl is likely coincidental, or otherwise the Turkic is from Iranian.
636-
637- Adjective
638- [ edit ] 
639-
640- آل • ( âl ) 
641-
642- bright red , scarlet 
643-
644- Derived terms
645- [ edit ] 
646-
647- آلگون ( âlgun ) 
648-
649- References
650- [ edit ] 
651-
```


## [2026-09-05T20:33:54.666Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in 65affeb76ac87b68 6b6e66e59b0fc9a7 e8c78aa91f01ba6a 29474facdb6e63a4 357887f43952c447; do echo \"###### $f\"; grep -n -m1 -A12 \"Advertisement\\|Etymology\\|origin of\" $f.txt | head -30; done",
 "description": "Read etymonline archives"
}
```


### [2026-09-05T20:33:56.581Z] TOOL RESULT

```
###### 65affeb76ac87b68
4:TITLE: Elbow - Etymology, Origin & Meaning
5-
###### 6b6e66e59b0fc9a7
4:TITLE: Elk - Etymology, Origin & Meaning
5-
###### e8c78aa91f01ba6a
4:TITLE: Elm - Etymology, Origin & Meaning
5-
###### 29474facdb6e63a4
4:TITLE: Lamb - Etymology, Origin & Meaning
5-
###### 357887f43952c447
4:TITLE: Alder - Etymology, Origin & Meaning
5-
```


## [2026-09-05T20:33:59.553Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in 65affeb76ac87b68 6b6e66e59b0fc9a7 e8c78aa91f01ba6a 29474facdb6e63a4 357887f43952c447; do echo \"###### $f\"; sed -n '1,80p' $f.txt; echo; done",
 "description": "Dump etymonline text"
}
```


### [2026-09-05T20:34:01.475Z] TOOL RESULT

```
###### 65affeb76ac87b68
URL: https://www.etymonline.com/word/elbow
FETCHED: 2026-09-05T20:33:16Z
STATUS: 200
TITLE: Elbow - Etymology, Origin & Meaning

Elbow - Etymology, Origin & Meaning 

 Search 
 Log in 

 Columns 
 Forum 
 Apps 
 Premium 

 Log in 

 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of elbow 

 elbow (n.) 

 "bend of the arm," c. 1200, elbowe , from a contraction of Old English elnboga "elbow," from Proto-Germanic *elino-bugon , literally "bend of the forearm" (source also of Middle Dutch ellenboghe , Dutch elleboog , Old High German elinbogo , German Ellenboge , Old Norse ölnbogi ).

 First element is from PIE *elina "arm," from root *el- "elbow, forearm." Second element is from Proto-Germanic *bugon- , from PIE root *bheug- "to bend." To be out at elbows (1620s) was literally to have holes in one's coat. Phrase elbow grease "hard rubbing" is attested from 1670s, from jocular sense of "the best substance for polishing furniture." Elbow-room "room to extend one's elbows," hence, "ample room for activity," is attested from 1530s.
 also from c. 1200 

 elbow (v.) 

 "thrust with the elbow," c. 1600, from elbow (n.). Figurative sense is from 1863. Related: Elbowed ; elbowing .
 also from c. 1600 

 Entries linking to elbow 

 *bheug- 

 Proto-Indo-European root meaning "to bend," with derivatives referring to bent, pliable, or curved objects.

 It might form all or part of: akimbo ; bagel ; bight ; bog ; bow (v.) "to bend the body;" bow (n.1) "weapon for shooting arrows;" bow (n.2) "front of a ship;" bowsprit ; buxom ; elbow .

 It might also be the source of: Sanskrit bhujati "bends, thrusts aside;" Old English bugan , German biegen , Gothic biugan "to bend;" Old High German boug , Old English beag "a ring."

 *el- 

 Proto-Indo-European root meaning "elbow, forearm." It might form all or part of: elbow ; ell (n.1) unit of measure; uilleann ; ulna .

 It might also be the source of: Sanskrit anih "part of the leg above the knee;" Greek ōlenē "elbow;" Latin ulna , Armenian uln "shoulder;" Lithuanian alkūnė "elbow;" Old English eln "forearm."

 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 More to explore

 cubit 

 ancient unit of measure (usually from 18 to 22 inches) based on the forearm from elbow to fingertip, early 14c., from Latin...cubitum, cubitus "the elbow, the forearm," generally regarded as a derivative of PIE *keu(b)- "to bend," but de Vaan finds...People lie down on their elbow if they sleep on their side, and the Romans even reclined when dining....It matters little whether the original meaning was 'forearm' or 'the elbow joint'....

 funny 

 Funny bone "elbow end of the humerus" (where the ulnar nerve passes relatively unprotected) is from 1826, so called for the...

 ell 

 originally "forearm, length of the arm" (as a measure, anywhere from a foot and a half to two feet), from PIE root *el- "elbow...

 not 

 [Century Dictionary, 1895] To not know X from Y (one's ass from one's elbow, shit from Shinola, etc.) was a construction...

 pygmy 

 etymologically "of the length of a pygmē; a pygmē tall," from pygmē "a cubit" (literally "a fist"), the measure of length from the elbow...

 tennis 

 .; tennis court from 1560s; tennis elbow from 1883; tennis shoes from 1887....

 hook 


###### 6b6e66e59b0fc9a7
URL: https://www.etymonline.com/word/elk
FETCHED: 2026-09-05T20:33:17Z
STATUS: 200
TITLE: Elk - Etymology, Origin & Meaning

Elk - Etymology, Origin & Meaning 

 Search 
 Log in 

 Columns 
 Forum 
 Apps 
 Premium 

 Log in 

 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of elk 

 elk (n.) 

 late Old English elch , from Old Norse elgr or from an alteration of Old English elh , eolh (perhaps via French scribes), or possibly from Middle High German elch (OED's suggestion), all from Proto-Germanic *elkh- (source also of Old High German elaho ). The modern word "is not the normal phonetic representative" of the Old English one [OED].

 The Germanic words are related to the general word for "deer" in Balto-Slavic (such as Russian losu , Czech los ; also see eland ), from PIE *olki- , perhaps with reference to the reddish color from root *el- (2) "red, brown" (in animal and tree names); compare Sanskrit harina- "deer," from hari- "reddish-brown." Greek alke and Latin alces probably are Germanic loan-words. Applied to similar-looking but unrelated animals in North America. Benevolent and Protective Order of Elks founded N.Y.C. 1868, originally a society of actors and writers.

 Entries linking to elk 

 eland (n.) 

 Cape elk, large South African antelope, 1786, from Dutch eland "elk," probably from a Baltic source akin to Lithuanian elnias "deer," from PIE *el- (2) "red, brown" (see elk ), cognate with first element in Greek Elaphebolion , name of the ninth month of the Attic year (corresponding to late March-early April), literally "deer-hunting (month)." Borrowed earlier in English as ellan (1610s, via French), ellend (from the German form of the word).

 alder (n.) 

 tree related to the birch, Old English alor "alder," from Proto-Germanic *aliso (source also of Old Norse ölr , Danish elle , Swedish al , Dutch els , German erle ), from the ancient PIE name of the tree (source also of Russian olicha , Polish olcha , Latin alnus (French aune ), Lithuanian alksnis ), from root *el- (2) "red, brown," used in forming animal and tree names (see elk ).

 The unetymological -d- was added 14c.; the historical form aller survived until 18c. in literary English and persists in dialects, such as Lancashire owler , which is partly from Norse.

 elm 
 hellebore 
 See All Related Words (4) 

 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 More to explore

 elm 

 common name of a type of trees noted for majestic height and the wide-spreading and gracefully curving branches, Old English elm, from Proto-Germanic *elmaz (source also of Danish elm, Old Norse almr, Old High German elme), perhaps from PIE root *el- (2) "red, brown" (see elk); c

 hellebore 

 late 14c., from Old French ellebore, from Latin elleborus, from Greek helleboros, the name given to various plants of both poisonous and medicinal qualities, reputed to cure madness; of uncertain origin. Perhaps literally "plant eaten by fawns," from Greek ellos/hellos "fawn" (fr

 moose 

 "large quadruped mammal of northern North America noted for its enormous horns," 1610s, from an Algonquian language, probably Narragansett moos or Abenaki moz (compare Penobscot muns, Ojibwa mooz, Unami Delaware /mo:s/), said by early sources to be from moosu "he strips off," sup

 each 

 From a common West Germanic expression *aina-galīk (source also of Dutch elk, Old Frisian ellik, Old High German iogilih,...

 deer 

 Old English deor "wild animal, beast, any wild quadruped," in early Middle English also used of ants and fish, from Proto-Germanic *deuzam, the general Germanic word for "animal" (as opposed to man), but often restricted to "wild animal" (source also of Old Frisian diar, Dutch di

 rede 

 "counsel, advice," Old English ræd "advice, counsel," from Proto-Germanic *redin (source also of Old Saxon rad "advice, counsel, help, advantage," Old Frisian red "council, advice," Dutch raad "advice, counsel," German Rat "advice, counsel," Old Norse rað "advice, consideration, 

 reed 

 "tall, broad-leafed grass growing on the margins of streams or in other wet places," Middle English rēd, rede, from Old English hreod "reed, rush," from Proto-Germanic *kreut- "reed" (source also of Old Saxon hraid, Old Frisian hriad, Middle Dutch ried, Dutch riet, Old High Germa

 hart 

 Middle English hert, from Old English heorot "hart, stag, male of the red deer," from Proto-Germanic *herutaz (source also of Old Saxon hirot, Old Frisian and Dutch hert "stag, deer," Old High German hiruz, Old Norse hjörtr, German Hirsch "deer, stag, hart"), perhaps from PIE *ke


###### e8c78aa91f01ba6a
URL: https://www.etymonline.com/word/elm
FETCHED: 2026-09-05T20:33:17Z
STATUS: 200
TITLE: Elm - Etymology, Origin & Meaning

Elm - Etymology, Origin & Meaning 

 Search 
 Log in 

 Columns 
 Forum 
 Apps 
 Premium 

 Log in 

 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of elm 

 elm (n.) 

 common name of a type of trees noted for majestic height and the wide-spreading and gracefully curving branches, Old English elm , from Proto-Germanic *elmaz (source also of Danish elm , Old Norse almr , Old High German elme ), perhaps from PIE root *el- (2) "red, brown" (see elk ); cognate with Latin ulmus , Old Irish lem . German Ulme , Dutch olm are from or influenced by the Latin word. The toughest native European wood, used for ship-building, wheel-naves, etc. Middle English had adjective forms elmen , elmin , which survived longer in poetry. New Haven was informally the Elm City (1871).

 Entries linking to elm 

 elk (n.) 

 late Old English elch , from Old Norse elgr or from an alteration of Old English elh , eolh (perhaps via French scribes), or possibly from Middle High German elch (OED's suggestion), all from Proto-Germanic *elkh- (source also of Old High German elaho ). The modern word "is not the normal phonetic representative" of the Old English one [OED].

 The Germanic words are related to the general word for "deer" in Balto-Slavic (such as Russian losu , Czech los ; also see eland ), from PIE *olki- , perhaps with reference to the reddish color from root *el- (2) "red, brown" (in animal and tree names); compare Sanskrit harina- "deer," from hari- "reddish-brown." Greek alke and Latin alces probably are Germanic loan-words. Applied to similar-looking but unrelated animals in North America. Benevolent and Protective Order of Elks founded N.Y.C. 1868, originally a society of actors and writers.

 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 More to explore

 weeping 

 Used of various trees whose branches arch downward and suggest drooping, such as weeping elm (c. 1600); weeping cherry (1824...

 fortress 

 For change of medial -l- to -r- in Old French, compare orme "elm" from Latin ulmus; chartre from cartula; chapitre from capitulum...

 poplar 

 produced popular), which is of unknown origin, possibly from a PIE tree-name root *p(y)el- (source also of Greek pelea "elm...

 slippery 

 The slippery elm (1748) of eastern North America (also moose or red elm) is so called for its mucilaginous inner bark, used...

 Dutch 

 Dutch elm disease (1927) so called because it was first discovered in Holland (caused by fungus Ceratocystis ulmi)....

 tree 

 Old English treo, treow "tree" (also "timber, wood, beam, log, stake"), from Proto-Germanic *trewam (source also of Old Frisian tre, Old Saxon trio, Old Norse tre, Gothic triu "tree"), from PIE *drew-o-, suffixed variant form of root *deru- "be firm, solid, steadfast," with speci

 wood 

 Old English wudu, earlier widu "tree, trees collectively, forest, grove; the substance of which trees are made," from Proto-Germanic *widu- (source also of Old Norse viðr, Danish and Swedish ved "tree, wood," Old High German witu "wood"), from PIE *widhu- "tree, wood" (source als

 ground 

 Old English grund "bottom; foundation; surface of the earth," also "abyss, Hell," and "bottom of the sea" (a sense preserved in run aground), from Proto-Germanic *grundu-, which seems to have meant "deep place" (source also of Old Frisian, Old Saxon, Danish, Swedish grund, Dutch 

 reciprocal 

 1570s, "existing on both sides, exclusive or interchangeable" (of duties, etc.), with -al (1) + stem of Latin reciprocus "returning the same way, alternating," from pre-Latin *reco-proco-, from *recus (from re- "back;" see re-, + -cus, adjective formation) + *procus (from pro- "f

 bed 

 Old English bedd "bed, couch, resting place; garden plot," from Proto-Germanic *badja- (source also of Old Frisian, Old Saxon bed, Middle Dutch bedde, Old Norse beðr, Old High German betti, German Bett, Gothic badi "bed"). This is said to mean perhaps "sleeping place dug in the g

 Share elm 


###### 29474facdb6e63a4
URL: https://www.etymonline.com/word/lamb
FETCHED: 2026-09-05T20:33:18Z
STATUS: 200
TITLE: Lamb - Etymology, Origin & Meaning

Lamb - Etymology, Origin & Meaning 

 Search 
 Log in 

 Columns 
 Forum 
 Apps 
 Premium 

 Log in 

 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of lamb 

 lamb (n.) 

 "young animal of the sheep kind," Middle English lomb , from Old English lamb , lomb , Northumbrian lemb , from Proto-Germanic *lambaz (source also of Old Norse, Old Saxon, Old Frisian, Gothic lamb , Middle Dutch, Dutch lam , Middle High German lamp , German Lamm "lamb"). Common to the Germanic languages but with no certain cognates beyond them.

 The -b probably has been silent since 13c. The Old English form was sometimes lombor , plural lambru .

 As a symbol of Christ (Lamb of God), typified by the paschal lamb, it is attested from late Old English. Also applied from late Old English to persons gentle or innocent as a lamb (especially young Church members); from mid-15c. it was applied to persons easy to cheat (compare figurative use of fleece (v.)), especially an inexperienced speculator deceived into making bad investments.

 Lamb also sometimes was used ironically for cruel or rough characters (such as Kirke's Lambs in Monmouth's rebellion, 1684-86, "an ironical allusion to the device of the Paschal Lamb on their flag" [OED]); Farmer and Henley ("Slang and Its Analogues") say "specifically applied to Nottingham roughs, and hence to bludgeon men at elections." Compare lambaste .

 Diminutive form lambie is attested from 1718. Lamb's-wool , also lambs-wool , "the wool of lambs" used commercially, hence delicate wool generally (used in hosiery, etc.) is from mid-14c. as a noun ( lambwoll ), by 1804 as an adjective.

 lamb (v.) 

 "to bring forth young," as a sheep, 1610s, from lamb (n.). Related: Lambed ; lambing .

 also from 1610s 

 Entries linking to lamb 

 fleece (v.) 

 1530s in the literal sense of "to strip (a sheep) of fleece," from fleece (n.). From 1570s in the figurative meaning "to cheat, swindle, strip of money." Related: Fleeced ; fleecer ; fleecing .

 lambaste (v.) 

 1630s, apparently from baste "to thrash;" see baste (v.3). The first element is the obscure verb lam "to beat, to lame" or the related Elizabethan noun lam "a heavy blow" (implied by 1540s in puns on lambskin ). To lambaste was, "In sailors' use, to beat with a rope's end" [Century Dictionary].

 Compare earlier lamback "to beat, thrash" (1580s, used in old plays). A dictionary from c. 1600 defines Latin defustare as "to lamme or bumbast with strokes." Related: Lambasted ; lambasting .

 lambkin 
 lamblike 
 lambskin 
 lammergeier 
 tomb 
 See All Related Words (7) 

 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 More to explore

 dear 

 Old English deore (Anglian diore, West Saxon dyre), "precious, valuable; costly, expensive; glorious, noble; loved, beloved, regarded with affection" from Proto-Germanic *deurja- (source also of Old Saxon diuri "precious, dear, expensive," Old Norse dyrr, Old Frisian diore "expen

 Agnus Dei 

 Late Latin, literally "lamb of God."...Latin agnus "lamb" is from PIE *agwh-no- "lamb" (see yean). For deus "god," see Zeus....The phrase is used from 1620s in reference to an image of a lamb as emblematic of Christ; usually it is pictured with a nimbus...

 shadowland 

 also shadow-land, 1821 (Lamb), "abode of ghosts and spirits," from shadow (n.) + land (n.)....[Charles Lamb, "Witches and other Night-fears"]...

 ossifrage 

 By this name Pliny meant "the Lammergeier" (that name is from German and means literally "lamb-vulture"), a very large Old...

 Mary 

###### 357887f43952c447
URL: https://www.etymonline.com/word/alder
FETCHED: 2026-09-05T20:33:18Z
STATUS: 200
TITLE: Alder - Etymology, Origin & Meaning

Alder - Etymology, Origin & Meaning 

 Search 
 Log in 

 Columns 
 Forum 
 Apps 
 Premium 

 Log in 

 A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 

 Quick and reliable accounts of the origin and history of English words. Scholarly, yet simple.

 About
 Who Did This 
 Sources 
 Introduction 
 Links 

 Support
 Premium 
 Patreon 
 Donate with PayPal 
 Merch 

 Apps

Get Chrome Extension 

Get iOS App 

Get Android App 

 Dark
 Auto
 Light

 Terms of Services Privacy Policy 

 English (English) 
 © 2001–2026 Douglas Harper & Talia Felix 

 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of alder 

 alder (n.) 

 tree related to the birch, Old English alor "alder," from Proto-Germanic *aliso (source also of Old Norse ölr , Danish elle , Swedish al , Dutch els , German erle ), from the ancient PIE name of the tree (source also of Russian olicha , Polish olcha , Latin alnus (French aune ), Lithuanian alksnis ), from root *el- (2) "red, brown," used in forming animal and tree names (see elk ).

 The unetymological -d- was added 14c.; the historical form aller survived until 18c. in literary English and persists in dialects, such as Lancashire owler , which is partly from Norse.

 Entries linking to alder 

 elk (n.) 

 late Old English elch , from Old Norse elgr or from an alteration of Old English elh , eolh (perhaps via French scribes), or possibly from Middle High German elch (OED's suggestion), all from Proto-Germanic *elkh- (source also of Old High German elaho ). The modern word "is not the normal phonetic representative" of the Old English one [OED].

 The Germanic words are related to the general word for "deer" in Balto-Slavic (such as Russian losu , Czech los ; also see eland ), from PIE *olki- , perhaps with reference to the reddish color from root *el- (2) "red, brown" (in animal and tree names); compare Sanskrit harina- "deer," from hari- "reddish-brown." Greek alke and Latin alces probably are Germanic loan-words. Applied to similar-looking but unrelated animals in North America. Benevolent and Protective Order of Elks founded N.Y.C. 1868, originally a society of actors and writers.

 Alamo 

 nickname of Franciscan Mission San Antonio de Valeroin (begun 1718, dissolved 1793) in San Antonio, Texas; American Spanish, literally "poplar" (in New Spain, also "cottonwood"), from alno "the black poplar," from Latin alnus "alder" (see alder ).

 Perhaps so called in reference to trees growing nearby (compare Alamogordo , New Mexico, literally "big poplar," and Spanish alameda "a shaded public walk with a row of trees on each side"); but the popular name seems to date from the period 1803-13, when the old mission building was the base for a Spanish cavalry company from the Mexican town of Alamo de Parras in Nueva Vizcaya.

 elder 
 Erl-king 
 See All Related Words (4) 

 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
```


## [2026-09-05T20:34:13.961Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '1,120p' data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T20:34:13.999Z] TOOL RESULT

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
```


## [2026-09-05T20:34:25.273Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN ārang/āranj\"; grep -n -i \"ārang\\|āranǰ\\|aran^g\\|arang\\|arendsch\\|Ellbogen\\|Ellenbogen\" HRN.txt | head -15\necho \"=== HUB\"; grep -n -i \"Ellbogen\\|Ellenbogen\\|arus\\|auruša\" HUB.txt | head -15\necho \"=== NYB arus/aresn\"; grep -n \"^arus\\|arus \\|ʾlws\\|arēšn\\|ārēšn\" NYB_vol2_glossary.txt | head -10\necho \"=== SOD arinj\"; grep -n -i \"ārinǰ\\|arync\\|elbow\" SOD.txt | head -10",
 "description": "Grep Horn, Hubschmann, Nyberg, Gharib"
}
```


### [2026-09-05T20:34:25.615Z] TOOL RESULT

```
=== HRN ārang/āranj
608:oss. arm-arün *Elle'; sar. yovn 'Ellbogen*; gr. wXsvfj;
1095:wa;^. yurm 'Vorderarm*; arm. armukn 'Ellbogen'
1576:ap. *avaranga- oder wohl besser '^abiranga- (vergl.
=== HUB
1045:an afgh. maca *Kuss'. — Arab, 'arus lautet im Persi-
6587:hrmak {xru§ak) *pasta dolce* (Wb.) = np. farusa, phi. *frd-
=== NYB arus/aresn
=== SOD arinj
```


## [2026-09-05T20:34:29.593Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '600,615p' HRN.txt\necho \"=== find Horn entry number/page\"\npython3 - <<'EOF'\nimport re\nlines=open('HRN.txt',encoding='utf-8',errors='replace').read().split('\\n')\nfor j in range(560,640):\n    s=lines[j].strip()\n    if re.match(r'^\\d{1,4}\\.\\s',s) or re.fullmatch(r'\\d{1,3}',s):\n        print(j+1,repr(lines[j][:90]))\nEOF",
 "description": "Horn entry for elbow word"
}
```


### [2026-09-05T20:34:31.732Z] TOOL RESULT

```
\ Käs. ort, ürt, vergl. auch s. v. äsyäh : ör, ä/-, ir,
aw. asa- gemahlen', anasa- (Hübschniann ZDMG.
38, 428); phlv. ärd ^Mehl'.
kurd. är, ärd (Jaba-Justi), ärf, irt (Houtum-
Schindler); af/. öra; bei. ärt n. arf (15); arm. aZ^wr
*Mehr, ahxm 'mahlen* (unsicher, H. No. 7).
14. uren *Elle', äreng^ ärenj,
phlv. äranj (PPGL).
oss. arm-arün *Elle'; sar. yovn 'Ellbogen*; gr. wXsvfj;
lat. ulna.
Vergl. aw. radni- in frara&nidrajö^); phlv. eratn (?);
ai. aratni' 'Elle'.
Die neupersischen Worte werden richtiger mit ä
(bezw. e) zu schreiben sein.
15. äroy (AM. S. 95 Zeile 2), üröq *das Rülpsen , äröytden,
röy,
=== find Horn entry number/page
567 "10. ärazis 'Guttat' (unbelegt)."
581 "11. är asten 'schmücken', Praes. üLräy-em^ ärayis,"
593 "12. äräm *Ruhe*, ärarmden, arätnis, nu^'0'nN (jüd.-pers."
606 "14. uren *Elle', äreng^ ärenj,"
614 '15. äroy (AM. S. 95 Zeile 2), üröq *das Rülpsen , äröytden,'
622 "16. äri 'fürwahr."
633 "17. ärey 'Hass, Feindschaft*, rey,"
639 "18. äz 'Begierde' (z. B. Vis und RämTn, Seite 47 Vers 14),"
```


## [2026-09-05T20:34:41.233Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nfor f,ln in [('HRN.txt',606),('HUB.txt',1045)]:\n    txt=open(f,encoding='utf-8',errors='replace').read()\n    lines=txt.split('\\n')\n    leaf=sum(l.count('\\f') for l in lines[:ln])\n    print(f,'line',ln,'leaf',leaf,'printed',leaf-21)\nEOF\necho \"=== IEC olena / elbow\"; grep -n \"^olen\\|^olēn\\|^olina\\|^elen\\|Ellbogen\\|elbow\" IEC.txt | head -20",
 "description": "Horn page and Mann grep"
}
```


### [2026-09-05T20:34:43.156Z] TOOL RESULT

```
HRN.txt line 606 leaf 26 printed 5
HUB.txt line 1045 leaf 42 printed 21
=== IEC olena / elbow
3543:elnā (elnà), see Inā, olenio “ell, elbow’. WP
3832:ormos (rmos, us) “arm, shoulder, extension, branch'. WP I, 73. Cf. armn- Skt. irmáh; Av. aromo; Oss. arm, pl. àrmttà “hand” beside ràmbín ‘elbow’; Arm. dim. type armukn Celbow. forearm’, fr. *ormuko-, or *armuko-); Go. Let arms; OHG arm; OE earm; ON armr; Lat. armus, m. o-st. 'shoul- der, arm’ beside ramus, n. o-st. “branch, arm of sea; OCS rame, gs. ramene, Srb. ràme ‘shoulder’; OPr. irmo “arm; Li. cf. irmos, f. pl. ‘stays, bars, crosspieces'
7644:kopsó, eið, ið ‘cut, strike’. Cf. kop- Arm. kopem, id.; Gk. kópso ‘will cut, will strike’; Cz. kosit ‘cut, mow; crop; cross-har- row’; Ir. cf. cuise ‘grass’. (Isophonic: Br. kof, kov ‘belly’: W coff ‘belly; hollow treetrunk’; Skt. kaphah ‘froth’; Av. kafo, id. but Skt. kaphin ‘elephant’; kaph-anih ‘elbow’)
8255:kub- (kubis, kubos) “joint, bend’. (Variant: kubit-). Cf. WP I, 374 Gk. kúbos ‘hollow in the flank’; cf. kúbiton ‘elbow’: Lat. cubitum, id. (Gk. fr. Lat. accdg. to WH); Hes. cf. kubisis ‘hernia’; Go. hups, f. i-st. ‘hip of body’; OE hype, wf. id.; Du. (*-ü-) heup, f. id.
8257:kubito- (variant of type kub-, q.v.) Gk. kúbiton (*elbow?. Fr. Lat. accdg. to WH); Lat. cubitum, id.; G Hüfte, f. ‘hip’; Hes. cf. kubisís ‘hernia’
9669:lenquó, ið “bend, turn, twist'. Cf. lonqu-, Inqu-. WP II, 435 Skt. cf. rankutih, f. ‘vetch’; OCS lẹkọ, lesti “bend, turn, twist", beside leto, lecati, denom. *ensnare'; Li. lenkiü, leükti ‘bend’, cf. also lenkmuó, eps m. “bend of elbow or knee’; lenke, f. “valley”; Latv. liecu, liekt “bend” be- side lencu, lenkt ‘go round; haunt’
12110:olénà, olinà, olənā ‘forearm, elbow, ell" WP I, 156 Per. cf. arang ‘elbow’; Oss. cf. árm-àárin, Dig. cáng-arinà "elt: Gk. oléne, f. ‘elbow’; Alb. llânë, T llërë, f. ‘forearm; eil; Lat. ulna, Fa- liscan olina "elt": Olr. uilen & uilind, f.; Ir. uille, gs: uilleann, f. ‘elbow, forearm, bend’; OBr. elin, Br. élin, ilin, pl. -u, m. ‘elbow’; W elin, pl. au, f. ‘elbow, bend’; Cor. elyn, pl. elynnow, m. id. (and “angle'); Go. aleina, f. "ell: OHG elina, f. ‘elbow’; OFris. elne, OE eln ‘forearm; el’; MHG elline, ellen, elne, len, sf. "ell": ON alin, ọln, pl. alnir & alnar, id.; Sw. aln, pl. -ar, f. id.
13725:pug- (pung-) “jab, jolt, stab'. Cf. pung- asa separate entry Gk. cf. püx, adv. “with the fist; pugón, gs: -onos, f. ‘elbow’; pugmé, f. ‘fist’; Lat. cf. pügio, -onis, f. ‘dagger’; pugna, f. ‘fight’; pugnus, gs: -1, m. ‘fist, punch’ beside pungo, Gre, v. ‘prick’: Li. pungu, pugti, v. ‘erupt in pimples’; LG fuck, m. “tap, jab, jolt’; fucken, v. id.; Latv. cf. puksts, s. “single heartbeat'. (Isophones: SWG Fucke, f. ‘pullet’: Du. vokken, v. ‘breed’; Icel. fok, n. “drift; spray”; fokka, f.: Sw. fock, -a, mf. *foresail")
14093:qulpos, à “bend, turn, twist’. Cf. quelp-, quolp-. Cf. WP I, 440, 474; II, 595 Skt. kürpam, n. “bridge of nose’; cf. kurparah, m. ‘bend of elbow or knee, hock’; Per. (?) kulbe ‘closet, cel; Alb. kulp, m. ‘clematis’; Lat. culpa, f. (^wrong'. Semantics of ON rangr ‘crooked, bent’: Sw. vrång ‘perverse, false’: E wrong); Li. kilpà, f. loop, noose’; Latv. cilpa, id. beside kilpe, kilpis ‘bearing-block; violin- bridge’
14276:Latv. kirpis ‘woodworm’; kirpas, fpl. ‘dust from woodworm’; Skt. kürparah, m. ‘elbow; knee’, lit. ‘turn, bend'(?) in view of Icel. horfa (2) v. ‘turn, bend”; horf "rend
```


## [2026-09-05T20:34:52.172Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nfor f,lns in [('IEC.txt',[12110,3543])]:\n    lines=open(f,encoding='utf-8',errors='replace').read().split('\\n')\n    for ln in lns:\n        leaf=sum(l.count('\\f') for l in lines[:ln])\n        print(f,ln,'leaf',leaf,'printed ~',(leaf-15)*2)\nEOF\necho \"=== SYN ELBOW\"; grep -n \"ELBOW\\|4\\.3[0-9] \" SYN.txt | head -10\necho \"=== SYN LAMB\"; grep -n \"^3\\.2[0-9]\\|LAMB\" SYN.txt | head -10\necho \"=== IEC elk/elen\"; grep -n \"^elk-\\|^elkis\\|^elnos\\|^elenos\\|^lombhos\\|^lambh\" IEC.txt | head -10",
 "description": "Mann page, Buck greps"
}
```


### [2026-09-05T20:34:54.104Z] TOOL RESULT

```
IEC.txt 12110 leaf 486 printed ~ 942
IEC.txt 3543 leaf 145 printed ~ 260
=== SYN ELBOW
5195:4.29 Turoar 4.30 SHovutprer
5196:4.32 Ersow 4.33 Hanp 4.34 Fincer 4.342 Taumes 4.35 Lxc 436 Kner 4.37 Foor 4.38 Tor 4.39 Nar 4.392 Wincg 4.393 FeaTaer
6140:¢ upper arm, shoulder’ (4.30). 2.145 f. 4.32 ELBOW
6152:4.33 HAND Grk. —xelp Goth. handus Lith. ranka NG xépt ON hond, mund Lett. ruoka Lat. manus Dan. haand ChSl. raka It. mano Sw. hand SCr. ruka Fr. main OE hand, mund Boh.  ruka Sp. mano ME hand Pol. reka Rum. mind NE hand Russ. ruka é Tr. lam Du. hand Skt. hasta-, kara-, pan- Nir. lamh OHG hant, munt Ay. zasta-, gu- W. law MHG hant Br. dourn NHG hand
6184:4.34 FINGER
6228:4.35 LEG
6270:4.37 Grk. — zobs Goth. fotus NG 66, wodé pu ON Jotr Lat, pés Dan. fod ae piede Sw. fot as pied OE Sot sp. pie ME sfote : um.  picior NE foot ae traig, coss Du. voet a troigh OHG fuoz u troed MHG T. troad NHG oe aay Se the inherited group, con- ee © Toot connection of which
6313:4.38 TOE Grk.  daxrvdos Goth. Lith. pirStas (kojos) NG daxr7vd0 (Tod zodtod) ON ta Lett. (kdjas) pirksts Lat.  digitus Dan. taa ChSl.  priistii(?) It. dito (del piede) Sw. td SCr. _ prst (od noge) Fr. orteil, doigt du pied OE ta Boh.  prst (na nahou) Sp. dedo (del pie) ME to Pol. palec (u nogi) Rum. deget de la picior NE toe Russ. alec (na noge) Ir. mér (coise) Du. teen Skt.  anguli-, padaiiguli- NIr. = méar (coise) OHG zaha Av. angusta- W. bys troed MHG ze(he) Br. biz troad NHG zehe
6323:4.39 NAIL Goth. «.-- Lith. mnagas Lett. nags out ON _ nagl J oe ie Dan. negli ChSl.  nogittt N unguts Sw. nagel SCr.  nokat Bs unghia OE negl Boh. nehet " — ongle ME We oe pene “ ufia NE nat E Rum. unghie Du. nagel Skt. nakha- ingen OHG  nagal Av. sri, srvd- Nir. tong MHG  nagel ' lal NHG  nagel ivin
18870:NG mavw, new present formed to aor. émaca, fr. Grk. métw, mdtw ‘press (9.342), late ‘seize’ (cf. Theocr. 4.35 Tabpov... migtas ras éaAas, and so reg. 0 NT and pap.).
=== SYN LAMB
4096:3.20-3.24. Groups of cognates which appear under several of these headings.
4113:3.20. ‘Cattle’, understood here as a generic term for the bovine species, may be expressed by plural forms or by singu- lar collectives belonging to the inherited group, Grk. Bods, etc. just discussed. Others have come through ‘cattle’ in the wider sense, mostly from ‘property’, several of these already discussed in 3.15. <A few reflect ‘living creature’, ‘horned’, ‘head’.
4132:3.21. ‘Bull’. 1. Grk. radpos; Lat. taw- rus (>It., Sp. toro, Rum. taur, OF'r. tor, Fr. faureau), Osc. ravpoz, Umbr. toru; Gall. tarvos, Ir. tarb, NIr. tarbh, W. tarw, Br. taro (Celtic forms with cons. transposition); ON Ajorr, Dan. tyr, Sw. tjur (these influenced by the group ON stjorr, ete.) : OPruss. tauris, Lith. tauras ‘wild ox’, ChSI. turii ‘wild ox’(?). Perh. IE *tau-ro- fr. *téu- ‘swell, be strong’ in Skt. taut, taviti ‘is strong’, etc. (so Walde-P. 1.711, Brugmann, Grd. 2.1.353), but more prob. to be combined with OF stéor, etc. Ernout-M. 1018. Falk-Torp 1309. Feist 454.
4141:3.22. Most of the words for ‘ox’ haye been discussed above (pp. 152, 153), The others are:
4147:3.23. The majority of the words for ‘cow’ represent the IE word for ‘ox, cow’, Grk. Bois, etc., with specialization to ‘cow’ in Gme. and Celtic. See above, p. 152. The others are:
4175:3.25 3.26
4179:3.25. Generic words for ‘sheep’, sev- eral of them also or only ‘ewe’.
4183:3.27 3.28 3.29 WETHER EWE LAMB roplas ols auvos, dpny pouvouxtopLevo ampoBariva apvl, dpvaxe Kptapte vervex ovis agnus castrone pecora agnello mouton brebis agneau carnero llano oveja cordero berbec castrat oaie micl molt (lon) 61, cdira; uan, dinu disc molt foisc uan molli, gwedder _ dafad, oen mamog maout danvadez oan Sti aters lamb, wiprus geldingr @r lamb bede jaar lam galigumse tacke lamm weder eowu lamb wether ewe lamb wether ewe lamb hamel oot lam widar (hamal) ou (ouwt) lamp hamel ouwe lamp hammel, schéps mutterschaf lamm avinas avis éras, avinélis auns avs gers cane ovtca agne, agnict skopac ovan ouca jagnje skopec, beran ovce, bahnice jehné, beranek skop, baran owca jagnig, baranek baran ovca jagnenok petva- avi-, mesi-, urd- maéesi-
4230:3.27. ‘Wether’. The castration of male sheep for fattening is an old and almost universal practice, and the ‘weth- er’ (understood here in the technical sense of NE wether ‘castrated sheep’) is the grown sheep par excellence. Hence the generic word for ‘sheep’, where it is not a distinctively feminine form, may be commonly applied to the ‘wether’ ; even though distinctive terms for the latter exist. Some of these are unfamil- iar to the layman (as NE wether except in bellwether). Conversely some words that were originally specific for ‘wether’ have become generic (as Fr. mouton) or through generic use have acquired a new specialization (as Fr. brebis ‘ ewe’, fr. Lat. vervex ‘wether’).
4271:3.29. ‘Lamb’. 1. IE *ag*(h)no-.
=== IEC elk/elen
10023:lombhos 'edge, rim, frame'. Cf. lembhos Cz. lub, m. ‘frame of millstone’; Blg. láb, m. ‘wooden hoop; e-gde in Lat. limbus, gs -1, m. ‘seam, edging’
```


## [2026-09-05T20:34:58.803Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '6140,6152p' SYN.txt\necho \"==== LAMB\"\nsed -n '4271,4290p' SYN.txt\necho \"==== pages\"\npython3 - <<'EOF'\nlines=open('SYN.txt',encoding='utf-8',errors='replace').read().split('\\n')\nfor ln in (6140,4271):\n    leaf=sum(l.count('\\f') for l in lines[:ln])\n    print(ln,'leaf',leaf,'printed',leaf-24)\nEOF",
 "description": "Buck ELBOW and LAMB sections"
}
```


### [2026-09-05T20:35:00.901Z] TOOL RESULT

```
¢ upper arm, shoulder’ (4.30). 2.145 f. 4.32 ELBOW
Goth. . Lith. alkiiné ON olnbogi Lett. elkuons Dan. albue ChSl. lakitilt Sw. — armbdge SCr. lakat OF elnboga Boh.  loket ME elbowe Pol. _lokied NE elbow Russ. lokot' Du. _—_elleboog Skt.  aratni- OHG  e()linbogo Av. aradna- MHG e(2)lenboge NHG ellenbogen
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
238
Words for ‘elbow’ are regularly from the notion of ‘bend’. There is frequent in- terchange between ‘elbow’ and ‘fore- arm’, the latter also as a measure ‘ell, cubit’.
1. Derivs. of IE *el-, *ele-, etc. ‘bend’ (but primary verbal forms lacking) in words for ‘forearm’ (as measure ‘ell, cubit’), and ‘elbow’. Walde-P. 1.156 ff. Ernout-M. 1120. Pedersen 2.59.
Grk. aden ‘forearm’, &ddév" rHv Tod Bpaxtovos xaprnv Hesych., &déxpavov ‘el- bow’ (so reg. in Aristot., where é&yxéyv is ‘upper arm’, as HA 493527, etc.), fr. *odevo-kpavoy, epd. with second part ‘tip’ : xapa ‘head, top’, etc.; Lat. ulna ‘forearm’ as measure ‘ell’; Ir. wilind, Ni. wille, W. elin, Br. ilin ‘elbow’; Goth. aleina, ON gin, eln, OE eln, OHG elina ‘ell’, in cpds. for ‘elbow’, ON olnbo- gt, Dan. albue, OSw. alboghi (Sw. arm- bdge by popular connection with arm; Hellquist 32), OE elnboga, ME elbowe, NE elbow, Du. elleboog, OHG e(I)lin- bogo, MHG e(1)lenboge, NHG ellenbogen, ellbogen, with final member : ON bogi,
SELECTED INDO-EUROPEAN SYNONYMS
ete. ‘bend, bow’; Lith. alkineé, Lett. elkuons (beside Lith. wuolektis, Lett, uolekts ‘ell’, OPruss. woaltis, woltis ‘ell forearm’) ; ChSI. lakitt (‘rixus, ell’), SCr lakat, Boh. loket, Pol. tokieé, Russ, lokot' ‘elbow, ell’; Skt. araini-, Ay, ara6éna- ‘elbow’ (Av. fraraéni- ‘ell’).
2. Grk. ayxwv (‘elbow’ Hom.+, but ‘upper arm’ in Aristot.), NG pop. aykavas : ayxbdos ‘bent’, Skt. afic- ‘bend’, etc. Walde-P. 1.60 f.
3. Lat. cubitus, cubitum (> It. gomito, Fr. coude, Sp. codo, Rum. cot; REW 2354) : Lat. cubdre ‘recline, lie down’ (as orig. ‘bend’), Goth. hups, ete. ‘hip’, OE hoppian, etc. ‘hop’, Grk. xbBos ‘hol- low above the hips on cattle’, fr. IR *keub-, beside *keu-, *keup-, etc. in words for ‘bend, hollow’. From Lat, cubitum (or a similar Italic form) through Sicilian (not conversely, as Bechtel, Griech. Dial. 2.284, Ernout-M. 237), comes Grk. xiBirov ‘elbow’ in Hippoc., ete. Walde-P. 1.374. Walde- H. 1.297,
4.33 HAND Grk. —xelp Goth. handus Lith. ranka NG xépt ON hond, mund Lett. ruoka Lat. manus Dan. haand ChSl. raka It. mano Sw. hand SCr. ruka Fr. main OE hand, mund Boh.  ruka Sp. mano ME hand Pol. reka Rum. mind NE hand Russ. ruka é Tr. lam Du. hand Skt. hasta-, kara-, pan- Nir. lamh OHG hant, munt Ay. zasta-, gu- W. law MHG hant Br. dourn NHG hand
==== LAMB
3.29. ‘Lamb’. 1. IE *ag*(h)no-.
Walde-P. 1.39. Ernout-M. 24. Walde- H. 1.23;
Grk. duvés; Lat. agnus, dim. agnellus (> It. agnello, Fr. agneau, Rum. miel; REW 284); Ir. wan, W. oen, Br. oan; Gme. only in verb, OE éanian ‘bring forth lambs’; ChSl. agne, agnici, etc., the general Slavic word (Berneker 24).
2. Grk. apnv (Cret. rapqy), gen. apvos, dim. dpviov, NG dpvi, dpvax : Skt. urad- ‘ewe’, urana- ‘ram’, Lat. vervex ‘wether’, Grk. épov ‘wool’, Aeol. éepos lit. ‘having wool on’ used for ‘male sheep’ (érepor kal dpynades ‘male sheep and ewes’), all going back to a word for ‘wool’ or the wool-bearing animal. Walde-P. 1.268 ff.
3. Sp. cordero, deriv. of Lat. c(h)ordus ate-born’. Cf. Varro, RR 2.1.29, di- cuntur agni chordi qui post tempum nas- cuntur. So (Diez, REW 1883 in first ed.) much better than deriv. fr. chorda, as ‘led on a rope’ (Gouchat, REW 1881 innewed.). For Lat. cordus, cf. Walde- H. 1.273.
4. Ir. dinu, fr. dinim ‘suck’ : Grk. @fjcbar ‘suck’, etc. Pedersen 1.183. Walde-P. 1.830.
5. Goth., ON, OE lamb, etc., the gen- eral Gmc. word, perh.: Grk. @&ados ‘stag’ and other animal names, but root
CC-O0. In Public Domain. Gurukul Kangri Collection, Haridwar
160
connection and primary sense dub.
Digitized by Arya Samaj Foundation Chennai and eGangotri
SELECTED INDO-EUROPEAN SYNONYMS
Walde-P. 1.154. Feist 321.
Goth. wiprus, see 3.26, OF weder, etc. 6. Lith. éras, Lett. jérs, orig. ‘yearling’, like SCr. jare ‘kid’, etc. : Goth. jér
‘year’, etc. Walde-P. 1.135 (to be
added 1.105).
ChSl. SCr. Boh. Pol. Russ. Skt. Ay.
3.31-3.35. Note that in the headings and translations either swine or hog, is used as the generic term, barrow for the castrated, and pig for the young animal, that is, in accordance with its original (and still mainly U.S.) use, in contrast to the now current British generic use.
3.31 SWINE
bs, xotpos youpobvi, Xotpos
==== pages
6140 leaf 275 printed 251
4271 leaf 192 printed 168
```


## [2026-09-05T20:35:12.079Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming\necho \"=== WLD Bd1 Ellbogen\"; grep -n \"Ellbogen\\|Ellenbogen\" WLD/WLD_Bd1_pages.txt | head -10\necho \"=== WLD Bd1 lamb\"; grep -n \"Goth. lamb\\|got. lamb\\|lamb \" WLD/WLD_Bd1_pages.txt | head -10\necho \"=== ARY آرنج\"; grep -n \"آرنج\" ARY/ARY_pages.txt | head -10\necho \"=== ARY آل\"; grep -n \"^آل\\|آلگونه\" ARY/ARY_pages.txt | head -10",
 "description": "Grep Walde-Pokorny Bd1 and Aryanpur"
}
```


### [2026-09-05T20:35:12.180Z] TOOL RESULT

```
=== WLD Bd1 Ellbogen
5488:     Gr. dyy.ojv „Bug, Ellenbogen“,                       (d. pi.   dyxdai, apokopiert dyy.dg, Lit. bei
5499:(vgl. u. anord. dl, al ds.), dyxvga „Anker“; dyxdhj „Ellenbogen, Bucht,
6332:die Worte ai. aratni-h   ratni-li „Ellenbogen, Elle, Arm“, Ctni-h „der un-
6346:„Ellenbogen“, frurCi&ni- „Elle“ ( rcina „Oberschenkel“?? I)och s. Fick
6651:„Ellenbogen“, apr. irmo „Arm“, lit. 'irmidc („ArmfraB“, d. i. :) ,,Gicht in
14310:            Hierher stellen sich zuniichst Bezeicbnungcn fiir „Ellenbogen“ und „Elle“:
14311:            Gr. tb/.tvy ,,Ellenbogen“, v>h)v. -trog ds.: d>/.Ey.guvov (aus d>/.tvo-y.ouvor durch
14314:        „Ellenbogenknocben, der ganze Arm";                                                             air.    uilenn „Winkel“,                    mir.         itill'tnd
14315:„Ellenbogen, \Yinkel“ (-11- aus -In- der synkopierten Kasus, vgl. Pedersen
14316:KG. If 59), cymr. cl in, acorn, elin, bret. din „Ellenbogen“ ( *olina Thur-                                                                                    ,
=== WLD Bd1 lamb
14023:got. lamb „Schaf", anord. lamb „Lamm, Schaf”, ahd. lamb „Lamm“ (groBen-
14025:andere Deutiingen von lamb s. Falk-Torp 620, 1506, Endzelin KZ. 44, 62).
28463:540); vermutlich (nach Petersson IvZ. 47, 270) lamb (-;', -tv) ,.Ring, Kreis"
51695:teten — aschw. gummerlamb „Widder“, isl. gumarr, norw. gumse, schw.
58398:unter *gel-g-), got. kalbo ..jurigc Kuh, Farse", mit e-Stufe ags. cilfor-lamb                                          ,
65607: lamb ds. (daneben vom es-St. ahd. kilbira ds. und         mit Abtonung o nach  —
=== ARY آرنج
1483:۴ ۲ آرنج آرنگ, آران :
1524:۴ معلی اين واژه در برخی زبان‌های رومانس: زند زبرین؛ استخوان آرنج.
2324:این واژه با "آرنج " از یک واجریشه است. ۹
=== ARY آل
133:آلمان به خارج مهاجرت کردند ولی هر چه از آلمان دورتر شدند آمیزش آنان با اقوام محلی موجب
307:آلمانی 43186077 لتونی 81:828؛ روسی 3۳:882۸) در برخی زبانها (مثلاً فارسی) از بین رفته
802:آلمانی وین (از ۱۹۰۰ به بعد). دیگر زبان‌های کهن ژُرمنی عبارتند از: ایسلندی کهن پا نورس کهن
932:آلمانی کهن: 017۷/1؛ ایرلندی‌کهن: ۵1 آیسلندی کهن:۸۳) لیتوانی: ۰۹۸۷1۸۷۸8
1246:آلمانی همریشه است. همینطور واژه‌ی فارسی «دندان» با واژه‌ی آلمانی 2۸1721 همريشه است ولی
1352:آلمانی: 1307) از کجا آمده و اجریشه‌ی هند و اروپایی آن چیست؟ ۸30۶ موی
1450:آلمانی کهن (/(688۵/۸ 0ات صا0): 371
1479:آلمانی کهن(شاید) (022944(۷ ۲۲۵ .0۱): 2 (5۸55) ,79 :۸/۸۲25
1506:آلمانی کهن (/(082914 04[لط ا0): پسگشت‌ها هرد تیان
1509:آلمانی (/(0874): ان نهر اند 8 8 ان ] 319 ی
```


## [2026-09-05T20:35:16.436Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming\necho \"=== ARY around 1483\"; sed -n '1470,1530p' ARY/ARY_pages.txt\necho \"=== pdf page tag\"; awk 'NR<=1490 && /\\[pdf page/ {p=$0} END{}' ARY/ARY_pages.txt; grep -n \"\\[pdf page\" ARY/ARY_pages.txt | awk -F: '$1<1490' | tail -3",
 "description": "Read Aryanpur arenj entry"
}
```


### [2026-09-05T20:35:18.018Z] TOOL RESULT

```
=== ARY around 1483
پهلری (۲1اتزهه): ,28۸۸41۲۸۵ لینوانی (4(/40ل 27 7ل): ,833171 ,8۸31118
۸ ,م۸ ,۶2/158 1
نخاری ۸ (۸4 4/7 7001۸): ۴۸6 ماگ۶ آدرنی (لی) (7۲14۸ا): 5
تخاری 8 (8 [(4ل7۸ل707): اس ایرلندی کهن (بلدتا صاه): 3
4 ابانکرت (/۵۸۹: 1۸۲۸1۲( اس
پرناتی 0888/0): .۲ 8۸ | پسگشت‌ها آشرد دا
گرتبکه(شاید) (00714/0): نیا 3 4 ۶0090
ایسلند یکهن (شاید) (21۸240۷/ 50/0 ۳:)0۱۵ "جر کر 930 +87
۳ 7 | 276 اتف 88) :ما05
آلمانی کهن(شاید) (022944(۷ ۲۲۵ .0۱): 2 (5۸55) ,79 :۸/۸۲25
۸۸ برهان قاطع : نفر مرن
انگلیسی گهن(شاید) (//5/ر20/07 012): 131۸
[pdf page 53]
۴ ۲ آرنج آرنگ, آران :

یادداشت/

۱- معنی این واژه در لیتوانی: آرام کردن,

معنی این واژه در ایرلندی کهن: قرار دادل, ۰

معنی این واژه در انگلیسی: حاشیه) لیه. دا و .

۲- 13۸۶۷13۸7 واژه‌های ژُرمئی این فهرست را از یک ریشه‌ی ناشناخته می‌پندارد. ی
اوستایی (4۲287۸۷): انا این ان کشا
پارسی باستان (884(۷ 0/.0): ۸۸811071815 لهستانی (۳0/5)+ 10
پهلوی (1الل۳۸): ۸۳۸ روسی (/75514): 1.007
کردی(شاید) (۸//0157): ۵ ول چکه (7ل25)): 10
سانسکریت (5۸۸/۶5/7)+ نوات اسلرا کی (81.0۸0): دید ی ۱
ار نی (/(ما/۸۵۸/8۸): ات۸ ,0 لیتوا انی ([(۵/۵تا 717 /). زا ۱۸
یونانی (0لظق0): ند لدرنی (لتی) (471404ا): یناه 8 ادا
لاتین (7[0ا): 1۸ ایرلندی کهن (57ل1# 01): 111
گونیکد (0077170): ۸۸ ولزی (517 )+ 1
ابسلندی‌کهن (۷۸۸ ‎٩4۸۷/۵/۸۸‏ 0): برتونی (8870/4): ۱ تا

00 ۱
آلمانی کهن (/(082914 04[لط ا0): پسگشت‌ها هرد تیان
نن ‏ 8 9 309 :۶080820

آلمانی (/(0874): ان نهر اند 8 8 ان ] 319 ی
انگلیسی کهن (8۸/0757 010): 801806۸ 105 شا
انگلیسی (7ل5/ا۰)8۸/0 0 2 (81301) ,13 :28انه ۸
دانمارکی (0۸(//8377): ۸5 23 ملق‌تاظ
سوئدی (5750[527): لاد ات 5 (8801) :0/08
نروژی (۸/0۸/0۸۸۷): #اناشل۸ 40 (۳80۷) وا ان
هلندی (077624): ای داد ۱8۸ 7 (ما8) ما ی ات اما
اسلاوی کهن (12لا؟ 2۳64 012): :| برهان قاطع : ۳۹
[pdf page 54]
۳
آرواره» آره / ۵۵
یادداشت:
۱ برهان قاطع : و دهخدا و معین ریشه‌ی این واژه را نمی‌دهند.
۲- 0۸1008 ,3۸8۸11۸۹7 فقط ریشه‌های ژرمنی این واژه را می‌دهند.
۳ 813۸7 ریشه‌ی سانسکریت این واژه را می‌دهد ولی ریشه‌ی اوستایی آن را نمی‌دهد.
۴ معلی اين واژه در برخی زبان‌های رومانس: زند زبرین؛ استخوان آرنج.
اوستایی (/۸۲59740): ۰ 17۸011۸482۸ لیتوانی (77۸1۸ل): 5اه
پپلری (2۸/1471) :۷۸8۸16 0,118 88۷۷۵۸ پروسی کهن (/(554نا۲# 0۵): اآاطلاتا۸
یونانی (005524): ۸1۵5
لاتین (4770): 8تا8لانقة ,8تآن۸17801 پسگشت‌ها 5
فراشسه (ن7لق۳8): رد 8 ت۶0
آسپانیایی (52۸/157): ادها 7 (50118له) و
=== pdf page tag
1426:[pdf page 51]
1451:[pdf page 52]
1482:[pdf page 53]
```


## [2026-09-05T20:35:31.858Z] TOOL CALL #49: Bash

```json
{
 "command": "pdftoppm -f 152 -l 152 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg152 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render PDF page 152"
}
```


### [2026-09-05T20:35:34.655Z] TOOL RESULT

```
total 16792
drwx------ 2 sfmqrb sfmqrb    4096 Sep  5 16:35 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  5 16:02 ..
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
-rw-rw-r-- 1 sfmqrb sfmqrb   67648 Sep  5 16:29 build128.py
-rw-rw-r-- 1 sfmqrb sfmqrb  105345 Sep  5 16:30 build132.py
-rw-rw-r-- 1 sfmqrb sfmqrb   56126 Sep  5 16:29 build136b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   13830 Sep  5 16:22 build136.py
-rw-rw-r-- 1 sfmqrb sfmqrb   66341 Sep  5 16:28 build139.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53260 Sep  5 16:29 build142.py
-rw-rw-r-- 1 sfmqrb sfmqrb   76989 Sep  5 16:32 build145.py
-rw-rw-r-- 1 sfmqrb sfmqrb   50861 Sep  5 16:34 build148b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   21485 Sep  5 16:29 build148.py
-rw-rw-r-- 1 sfmqrb sfmqrb    7816 Sep  5 16:35 c_am2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   14765 Sep  5 16:35 c_am3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   10038 Sep  5 16:35 c_empty2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4123 Sep  5 16:34 crop_am.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4986 Sep  5 16:34 crop_arabic_refs.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7702 Sep  5 16:34 crop_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb   16978 Sep  5 16:34 crop_morocco.png
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep  5 16:18 kent.txt
-rw-rw-r-- 1 sfmqrb sfmqrb     222 Sep  5 16:30 leaf.py
-rw-rw-r-- 1 sfmqrb sfmqrb   57617 Sep  5 16:20 mk129.py
-rw-rw-r-- 1 sfmqrb sfmqrb   74680 Sep  5 16:26 mk131.py
-rw-rw-r-- 1 sfmqrb sfmqrb   33365 Sep  5 16:25 mk133.py
-rw-rw-r-- 1 sfmqrb sfmqrb   42635 Sep  5 16:29 mk140.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51288 Sep  5 16:30 mk143.py
-rw-rw-r-- 1 sfmqrb sfmqrb   11831 Sep  5 16:32 node4.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7427 Sep  5 16:32 node7.png
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep  5 16:13 oldpers_djvu.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   22067 Sep  5 16:29 part0.json
-rw-rw-r-- 1 sfmqrb sfmqrb   14156 Sep  5 16:22 part1.json
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
-rw-rw-r-- 1 sfmqrb sfmqrb   62516 Sep  5 16:35 pg152.png
-rw-rw-r-- 1 sfmqrb sfmqrb   39131 Sep  5 16:28 pg153.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63033 Sep  5 16:30 pg154.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77057 Sep  5 16:32 pg155.png
-rw-rw-r-- 1 sfmqrb sfmqrb  169880 Sep  5 16:34 pg158_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80624 Sep  5 16:34 pg158.png
-rw-rw-r-- 1 sfmqrb sfmqrb  124379 Sep  5 16:31 pg159_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   27814 Sep  5 16:31 pg159.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4694 Sep  5 16:31 pg159_word.png
-rw-rw-r-- 1 sfmqrb sfmqrb  168057 Sep  5 16:34 pg161_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   76745 Sep  5 16:34 pg161.png
-rw-rw-r-- 1 sfmqrb sfmqrb   25911 Sep  5 16:32 pg163.png
-rw-rw-r-- 1 sfmqrb sfmqrb   59398 Sep  5 16:33 pg164.png
-rw-rw-r-- 1 sfmqrb sfmqrb   44812 Sep  5 16:34 pg532.png
-rw-rw-r-- 1 sfmqrb sfmqrb  153161 Sep  5 16:34 pg532_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4868 Sep  5 16:14 prt.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  333088 Sep  5 16:16 sod135_c.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1817364 Sep  5 16:16 sod135.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  101641 Sep  5 16:15 sod136_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1892712 Sep  5 16:15 sod136.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   56398 Sep  5 16:26 write144.py
```


## [2026-09-05T20:35:39.670Z] TOOL CALL #50: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg152.png"
}
```


### [2026-09-05T20:35:40.047Z] TOOL RESULT

```

```


## [2026-09-05T20:35:40.044Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T20:35:55.891Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad\npdftoppm -f 152 -l 152 -r 600 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg152_600\npython3 - <<'EOF'\nfrom PIL import Image\nim=Image.open('pg152_600.png'); print(im.size)\nw,h=im.size\n# node2 box approx at x 605-790 /1545 , y 750-815 /2000\nbox=(int(600/1545*w),int(745/2000*h),int(800/1545*w),int(820/2000*h))\nim.crop(box).save('p152_node2.png')\nbox2=(int(330/1545*w),int(280/2000*h),int(620/1545*w),int(430/2000*h))\nim.crop(box2).save('p152_e0left.png')\nEOF\nls -la p152_node2.png p152_e0left.png",
 "description": "Crop node images at 600dpi"
}
```


### [2026-09-05T20:36:01.290Z] TOOL RESULT

```
(5100, 6600)
-rw-rw-r-- 1 sfmqrb sfmqrb 6054 Sep  5 16:36 p152_e0left.png
-rw-rw-r-- 1 sfmqrb sfmqrb 2672 Sep  5 16:36 p152_node2.png
```


## [2026-09-05T20:36:03.636Z] TOOL CALL #52: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p152_node2.png"
}
```


### [2026-09-05T20:36:03.648Z] TOOL RESULT

```

```


## [2026-09-05T20:36:29.228Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/aru%C5%A1as\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/lambaz\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/alin%C5%8D\" \\\n \"https://en.wiktionary.org/wiki/ulna%23Latin\" \\\n \"https://en.wiktionary.org/wiki/%D8%A7%D8%B1%D8%B4\" \\\n ; do echo \"### $u\"; python3 tools/fetch_source.py \"$u\" --note \"page 152 El2/El3: Proto-Indo-Iranian arusas, PGmc lambaz/alino, Latin ulna, Persian arash\"; done",
 "description": "Fetch more Wiktionary reconstruction pages"
}
```


### [2026-09-05T20:36:34.209Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/aru%C5%A1as
/home/sfmqrb/git/rishe/data/verification/sources/web/42ca426264a2de75.txt
### https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/lambaz
/home/sfmqrb/git/rishe/data/verification/sources/web/936781827400b263.txt
### https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/alin%C5%8D
/home/sfmqrb/git/rishe/data/verification/sources/web/edeb6d2ad5582c5f.txt
### https://en.wiktionary.org/wiki/ulna%23Latin
/home/sfmqrb/git/rishe/data/verification/sources/web/dd0ce1cd45d33705.txt
### https://en.wiktionary.org/wiki/%D8%A7%D8%B1%D8%B4
/home/sfmqrb/git/rishe/data/verification/sources/web/6b0bafa2b4fa662b.txt
```


## [2026-09-05T20:36:37.313Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in 42ca426264a2de75 936781827400b263 edeb6d2ad5582c5f; do echo \"###### $f\"; grep -n -m2 -A14 \"Etymology\" $f.txt | head -45; echo; done",
 "description": "Read reconstruction pages"
}
```


### [2026-09-05T20:36:38.947Z] TOOL RESULT

```
###### 42ca426264a2de75

###### 936781827400b263
65: Etymology 
66-
67- 1.3 
68- Pronunciation 
69-
70- 1.4 
71- Noun 
72-
73- 1.4.1 
74- Declension 
75-
76- 1.4.2 
77- Descendants 
78-
79- 1.5 
--
150: Etymology
151- [ edit ] 
152-
153- Inherited from Proto-Indo-European *h₁l̥h₁-on-bʰ-os- (related to Scottish Gaelic lon ( “ elk ” ) , Ancient Greek ἔλᾰφος ( élăphos , “ red deer ” ) ), enlargement of *h₁elh₁én , from *h₁el- ( “ deer, elk ” ) . [ 1 ] 
154-
155- Pronunciation
156- [ edit ] 
157-
158- IPA ( key ) : /ˈlɑm.bɑz/ 
159-
160- Rhymes: -ɑm.bɑz 
161-
162- Noun
163- [ edit ] 
164-

###### edeb6d2ad5582c5f
65: Etymology 
66-
67- 1.3 
68- Pronunciation 
69-
70- 1.4 
71- Noun 
72-
73- 1.4.1 
74- Inflection 
75-
76- 1.4.2 
77- Derived terms 
78-
79- 1.4.3 
--
151: Etymology
152- [ edit ] 
153-
154- From Proto-Indo-European *Heh₃l-én-eh₂ , from *Heh₃l- ( “ to bow, elbow ” ) . Cognate with Ancient Greek ὠλένη ( ōlénē ) , Latin ulna , Welsh elin . [ 1 ] 
155-
156- Pronunciation
157- [ edit ] 
158-
159- IPA ( key ) : /ˈɑ.li.nɔː/ 
160-
161- Noun
162- [ edit ] 
163-
164- *alinō   f [ 1 ] 
165-
```


## [2026-09-05T20:36:49.783Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"### PII arusas\"; wc -l 42ca426264a2de75.txt; grep -n \"does not exist\\|No entry\\|Wiktionary does not yet\" 42ca426264a2de75.txt | head\necho \"### arash\"; grep -n -m3 -A12 \"Etymology\" 6b0bafa2b4fa662b.txt | tail -30",
 "description": "Check PII page and Persian arash"
}
```


### [2026-09-05T20:36:49.884Z] TOOL RESULT

```
### PII arusas
5 42ca426264a2de75.txt
### arash
76- Toggle Urdu subsection 
77-
--
79: Etymology 
80-
81- 2.2 
82- Pronunciation 
83-
84- 2.3 
85- Noun 
86-
87- 2.4 
88- References 
89-
90- Toggle the table of contents 
91-
--
164: Etymology
165- [ edit ] 
166-
167- From Middle Persian [script needed] ( ”ryšn /⁠ārešn⁠/ ) , from Old Persian 𐎠𐎼𐏁𐎴𐎡 ( a-r-š-n-i /⁠arašni⁠/ ) .
168-
169- Pronunciation
170- [ edit ] 
171-
172- ( Classical Persian ) IPA ( key ) : /ʔa.ˈraʃ/ 
173-
174- ( Dari, formal ) IPA ( key ) : [ʔä.ɾáʃ] 
175-
176- ( Dari, formal ) IPA ( key ) : [ʔä.ɾáʃ]
```


## [2026-09-05T20:37:15.669Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nlines=open('PHD.txt',encoding='utf-8',errors='replace').read().split('\\n')\nfor ln in (214,):\n    leaf=sum(l.count('\\f') for l in lines[:ln])\n    print('line',ln,'leaf',leaf,'printed',leaf-21)\nEOF\necho \"=== PHD_pages check\"; grep -n \"arus\\|āranj\\|ārešn\" PHD_pages.txt | head -5\ngrep -n \"\\[pdf page\" PHD_pages.txt | head -3",
 "description": "MacKenzie page number"
}
```


### [2026-09-05T20:37:17.558Z] TOOL RESULT

```
line 214 leaf 33 printed 12
=== PHD_pages check
1186:arus ['Iws] white.
7974:white sped, arus; (n.) spedag.          word cwaz, marig, saxwan, sraw,
```


## [2026-09-05T20:37:25.597Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON آلگونه\"; grep -n \"آلگونه\" MON_part1.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt 2>/dev/null | head -5\necho \"=== MON آل (\"; grep -n \"آل (\" MON_part1.txt | head -5\necho \"=== MON size\"; wc -l MON_part1.txt",
 "description": "Grep Mo'in Farhang"
}
```


### [2026-09-05T20:37:25.684Z] TOOL RESULT

```
=== MON آلگونه
incoming/MON/MON_2vol_Adena_v1_djvu.txt:2748:آلغونه» آلگونه. گونه» روش طرز. 
MON_part1.txt:2748:آلغونه» آلگونه. گونه» روش طرز. 
=== MON آل (
=== MON size
99339 MON_part1.txt
```


## [2026-09-05T20:37:28.112Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '2730,2760p' MON_part1.txt",
 "description": "Read Mo'in around algune"
}
```


### [2026-09-05T20:37:28.173Z] TOOL RESULT

```
ارمیچر: عکآصة (ا.) (مکد.) محور سیم 
پیچی شده‌ای که در داخل استوانةٌ استارت 
قرار دارد و در ابتدای حرکت و با گردش 
خود» مو تور را به گردش در می آورد. محور 
سیم پیچی شده‌ای که در داخل دینام قرار 


دارد و با گردش موتور باتری را «شارژم 
می‌کند. 

آرنسج: م2 ,لحعتة (- آران ‏ آرن - 
آرنگ] (.) بندگاه میان ساعد و بازو از 
طرف بیرون» مرفق. از فنون کشتی‌گیری در 
خاکك است و آن عبارت است از اینکه کت 
طرف را گرفته درو می‌کنند بطوری که پشت 
طرف به خاک رسد. نوعی از آن استاده 
عمل می‌شود و آن را «آرنج سرپاء گویند. 
ارنگ: عهوعة 1 رنگ] )1( رنگ» لون. 
آلغونه» آلگونه. گونه» روش طرز. 
آرنگ: 8 [- رنسج] )۱( رنح» اد یت» 
آزار. مکر؛ حبله. 

ارواره؛ (0-)27۷312 [- ارواره - اروار] (ا.) 
(جاذ.) هر یک از دو قطعه استخوان که 
حفره‌های دندانی در آن جای دارند» فک 
(فره.) ۱ 

ارویند: 271-40 (ص مر .) آنکه استخوان 
شکسته و از جای برآمده را بهم پیوندد) 
شکسته بند.
```


## [2026-09-05T20:37:36.344Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^آل\\b\\|آلگون\\|آل:\\|آل؛\" MON_part1.txt | head -20\necho \"---\"; grep -n \"سرخ رنگ\\|سرخ‌رنگ\" MON_part1.txt | sed -n '1,10p'",
 "description": "Find Mo'in al entry"
}
```


### [2026-09-05T20:37:36.427Z] TOOL RESULT

```
2105:آلز مه ره ماه انقر نان : داهن 
2414:آلاله. از تبر ۵ الاله‌ها. برگ‌هایش بریده و 
2748:آلغونه» آلگونه. گونه» روش طرز. 
3344:آلیز. تماس» ساش» تلاقی. تبش» هرم. 
4003:آلات و اسباب از قبیل پارالل» بارفیکس و 
4079:آلات موسیقیء دارای زبانه‌های فلزی که به 
4185:سر ح » احمر : لاله آل: از خون دیده دامن 
4211:آل: 2 [ع.] (.) دودمان» خاندان» امل» 
4213:آل‌علی» خاندان علی(ع) ؛ بن ابی‌طالب. 
4215:آل ا8 [ع.] )٩(‏ جایی_ در بیابان که به هنگام 
4257:آلاچق ۳ آله‌چوق ] (.) سراپرده و سایبان دو 
4262:آلاخون‌والاخون: 21201111-7 آثر. 
4263:آلاخان - آلامان» (سیخانمان ] آلاخون 
4268:آلاس: 5 (.) رغال» زگال؛ انگشت. 
4269:آلاکلنگ: 21128 (امر.) دو چجوبت 
4274:آلاله‌هاء جزو دو لیه‌ای‌های جدا گلی رک که 
4280:آلام: سقاة [ع ۰) (.) ج. . الم» در دها» رنج‌ها. 
4281:آلام جسمانی: دردهایی که به تن رسده 
4288:آلاو: 0 (- آلو - الاو] ((.) شعلة آتش 
4295:آلایشنا ک: 2.086 (ص‌مر.) دارای آلایش» 
---
21369:سرخ‌رنگ که در خراسان و کرمان یافت 
22721:حل می‌شود و محلول سرخ رنگی بنام آب 
28844:است سرخ رنگ يا زرد رنگ که در طب 
37515:(گیا.) عناب. چوبی سخت و سرخ رنگ که 
51626:روپاکی سرخ رنگ که بر سر بندند. (جان.) 
53525:و بثور سرخ رنگ در سینه و پشت و شکم و 
56258:سنت است.) (جاذ.) حشره‌ای سرخ رنگگ 
70099:نیز طوبلتر و قویتر از کبوتر و سرخ رنگ 
70783:خرد و سرخ رنگ باشد. زر سرخ: طلای 
76038:برخی گونه‌ها چوب کمی سرخ رنگ هم
```


## [2026-09-05T20:37:39.259Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '4178,4215p' MON_part1.txt",
 "description": "Mo'in al entry context"
}
```


### [2026-09-05T20:37:39.315Z] TOOL RESULT

```
اگیم: سَعة ( ۰ کم غر بال. 
اک سر [- آکین] (.) حشو» آکنه» 
ره (س. اتصاف و دار ندگی) در کلمات 
هستز کم به معنی آلود (آلوده)؛ مر صع» 
انباشته» مانند و گونه دارا و صاح. اندود 
(اندوده) ات زه رآ گین. 
ال ا [- آلا. ماز. سرخ کم رنگ | (ص.) 
سر ح » احمر : لاله آل: از خون دیده دامن 
افلاک آل کرد. (شمس طبسی). سرخ 
نیمرنگ: خون آل. (.) (گی.) درختی که از 
بیخ آن رنگی سرخ گیرند و جامه بدان سرخ 


ی رو 


ال؛ ۱ ((.) (عم.) بیماریی که زن نوزاییده را 
تا شش روز پس از وضع حمل رسد. (عم.) 
مو جودی نامر ثی ماننل جن که زن تاره زا را 


سا 


1 فرهنگ فارسی معین ۵2۷ 


اگر تنها بماند - صدمه رساند (خف.) 

ال: ا2 (یت.) بصورت پسوند نسبت و 
شباهت به آخر کلمات ملحق شود: انگشتال 
چنگال» خشکال. 

آل: 2 [ع.] (.) دودمان» خاندان» امل» 
آ تون تلع خاندان پیامبر اسلام؛ 
آل‌علی» خاندان علی(ع) ؛ بن ابی‌طالب. 

آل ا8 [ع.] )٩(‏ جایی_ در بیابان که به هنگام
```


## [2026-09-05T20:37:53.293Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\npython3 - <<'EOF'\nlines=open('WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read().split('\\n')\nfor ln in (14023,14310,6332):\n    leaf=sum(l.count('\\f') for l in lines[:ln])\n    print('line',ln,'leaf0',leaf,'printed ~',leaf+1-9)\nEOF\nsed -n '14018,14030p' WLD_Bd1_pages.txt\necho \"...\"\nsed -n '14305,14320p' WLD_Bd1_pages.txt",
 "description": "Walde-Pokorny Bd1 el- section"
}
```


### [2026-09-05T20:37:55.063Z] TOOL RESULT

```
line 14023 leaf0 162 printed ~ 154
line 14310 leaf0 164 printed ~ 156
line 6332 leaf0 78 printed ~ 70
laniji     auf *ldn-i, nicht *olnl zuriiekfiihren) ;                               ablautendes *lon- in gal. Ion
„Elentier“ (Strachan BB. 20, S f. Anm. 4                               ;
                                                                               Ficks II 4 255 Annahme von Ent-
lehnung ist haltlos); dazu weiter (nach Ilirt Abl. 122, Osthoff aaO. 303ff.)
sehr wahrscheinlich als *l-on-bho-s (mit demselben Suffix wie elacpos) auch
got. lamb „Schaf", anord. lamb „Lamm, Schaf”, ahd. lamb „Lamm“ (groBen-
teils neutr. -es-St.. was gemeingerm. Neuerung nach Kalb scheint; gegen
andere Deutiingen von lamb s. Falk-Torp 620, 1506, Endzelin KZ. 44, 62).
   Als Umstellung aus *<lcn- fa lit Niedermann IA. IS, 78 f. gr. i've/.og veftgog                                 '




...


        1IT 4       26 (cl a                 I   >,    Falk-Torp 4 (aal Y), Yasmer bei Senn Germ. Lw.-Stud. 47.

        elei-. lei- „biegen“.
            Hierher stellen sich zuniichst Bezeicbnungcn fiir „Ellenbogen“ und „Elle“:
            Gr. tb/.tvy ,,Ellenbogen“, v>h)v. -trog ds.: d>/.Ey.guvov (aus d>/.tvo-y.ouvor durch
        Ferndissimilation, vgl. Brugmann Bcr. d. siichs. Ges. d. W. 1901, 31 ff.i „Ellen-
        bogenkopf": <b)./.ov i yv tov jkoayioroi yapayv lies., lat. ulna aus *olena)
        „Ellenbogenknocben, der ganze Arm";                                                             air.    uilenn „Winkel“,                    mir.         itill'tnd
„Ellenbogen, \Yinkel“ (-11- aus -In- der synkopierten Kasus, vgl. Pedersen
KG. If 59), cymr. cl in, acorn, elin, bret. din „Ellenbogen“ ( *olina Thur-                                                                                    ,


neysen Ildb. I 44, Fick II 4 52, Pedersen aaO.). Den gleichen langen
Mittelvokal zeigt das Got.    aleinu „Elle“, doch haben die iibrigen germ.
```


## [2026-09-05T20:38:04.357Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\nsed -n '6325,6350p' WLD_Bd1_pages.txt",
 "description": "WP I p.70 context"
}
```


### [2026-09-05T20:38:04.426Z] TOOL RESULT

```
      Mit Zerdehnung opr]oos „Gatte; Geisel, Unterpfand", ourjor.co „treffe zu-
sanimen'''.
      Aus dem Slav, vielleicht poln. ko-jarzyc „kniipfen, verbinden, vereinigen“
(z.B. Miklosich EWb. 100, Berneker 31, 532).
   Uber das vielleicht verwandte gr. doa, lit. ir s. *ar „nun, also".    Zur                                        —
Bed. „Fuge — Gelenk, Glied" ( ao&oov) vgl. auch u. die Worte fur „A.rm“. Da-
gegen bleiben trotz Persson Beitr. 634 f. besser bei der Sippe von cbtevt]
die Worte ai. aratni-h   ratni-li „Ellenbogen, Elle, Arm“, Ctni-h „der un-
                                                  ,


mittelbar liber dem Knie liegende Teil des Beines“ (mind, aus *arni-
die Bed. ,in der Nabe laufender Achsenzapfen         beweist nicht fur Yer-             1




wandtschaft mit ard-h Radspeiche“ und arpayati sondern geht auf das
                                                      j:                                    ,

Bild des in der Gelenkpfanne sich drehenden Knochenkopfes), av. ars&na-
„Ellenbogen“, frurCi&ni- „Elle“ ( rcina „Oberschenkel“?? I)och s. Fick
I 4 339).


      t- Bildungen:
```


## [2026-09-05T20:38:13.954Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor w in ELM ELK ELBOW LAMB ELL ALDER; do echo \"== $w\"; grep -n \"^$w\" SKT.txt | head -3; done",
 "description": "Skeat greps"
}
```


### [2026-09-05T20:38:15.729Z] TOOL RESULT

```
== ELM
== ELK
== ELBOW
== LAMB
== ELL
== ALDER
```


## [2026-09-05T20:38:18.677Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"Elm\\|ELM,\" SKT.txt | head -5; echo ---; grep -n -i \"elbow\" SKT.txt | head -5; echo ---; grep -n -i \"^Lamb\\|Lamb,\" SKT.txt | head -5",
 "description": "Skeat retry"
}
```


### [2026-09-05T20:38:18.747Z] TOOL RESULT

```
373:Admiral.  (F.-Arab.)  M.E. more  often  amiraLm^O.  F.  amiral, also  amirt\  cf.  Low  L.  admu prince,  chief.* Arab,  amlr^  a  pri Elmir.  The  suffix  is  due  to  Arab.] amir-ai-baJir,  pnncc  of  ihc  sea.
5761:Elm,  a  tree    (E.i     A.S.  e/«+Pa-«fa. Icel.  iilmr,  Dan  aim,  Swed.  «/»n,  G- (formerly  elnie),  L.  uimus.      ( ^  AL.)
---
4461:Cubit.  ( L. )  L.  ^v^V»i.  an  elbow^  bend; the  length  &oni  the  elbow  to  the  middle finger's  end.  Allied  to  L.  cuhart,  to  lie down,  recline  ;  see  Covey.
5735:Elbow,  the  bend  of  the  arm.  i,E.)  M.  E. eibffwt,  A.  S.  eiSoga.^K.S.  el-,  signifying •elbow  [*  and  boga^  a  bow,  a  bending  (see Bow).  A.  S  eit'xk  allied  to  Goth,  aleina, a  cubit,  L.  vlna,  Gk.  otKivr},  Skt.  anittti.  the elbow.  (VARand  VBHUG.)  +  Du,^//rf- Socg,  Icel.  ain-dcgi.  Dam.  al-6ue^  G.  ellen- bem.    SeeXU,
5759:Ell.    (E.)      M.  E-  eiU, a  cubit  +  Du.c//f ;  Icel.  «</ the  elbow  to  the  tip  of  the  miiidie Swed.  a/ii,  Dan.  aien,   Goth- eiU.  ell ;  L.  ulna,  elbow,  cubit ;  Gki elbow.     Ell  ^  el-  in  el-bow.
15274:Pygmy.  (F.-L.-GkO  V. pygm/,  adj. dwarflike;  Cot.  — L.  pygmauj,  adj.,  dwarf- like ;  from  pL  Pygmtti,  the  race  o( Pygmies.  — Gk.  niry^uuM,  pygmies.  fabaU dwarfs  of  the  length  of  a  mryftrj,  i.e.  aboi 13J  in.,  from  the  elbow  Co  the  knuckles  or tist.  —  Gk.  wvytirt,  B  6st ;  sec  PugiUat.
---
9874:Lamb.  (£.)  M.  £.  lamb^  lemb.  A.  S. lamb.  ^  Du.  lam^  Icel.  lamb,  Dan.  lam, Swed.  and  G.  lamm,  Goth,  kunb,  a  young ibeep.
9946:Lap  {i),  the  loose  part  of  a  coat,  oa apron,  part  of  the  body  covered  by  an apron,  a  fold,  (E)  M.  E.  lapp€.  A.S. Itrfpa,  a  loosely  hanging  portion.  +  Du. lap,  Dan.  iap,  Swed.  lapp,  G.  lap  pen.  a patch,  shred,  rag.  Cf.  IccL  lapa,  to  hang down ;  Skt.  lamb,  ramb,  to  hang  donn. (^RAB).  Allied  to  ItobejLlmbo,  Lapse, Limp  (i),
```


## [2026-09-05T20:38:27.679Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nlines=open('SKT.txt',encoding='utf-8',errors='replace').read().split('\\n')\nfor ln in (5735,5761,9874):\n    leaf=sum(l.count('\\f') for l in lines[:ln]); print(ln,'leaf',leaf,'printed',leaf-20)\nEOF",
 "description": "Skeat pages"
}
```


### [2026-09-05T20:38:29.714Z] TOOL RESULT

```
5735 leaf 154 printed 134
5761 leaf 155 printed 135
9874 leaf 259 printed 239
```


## [2026-09-05T20:39:02.874Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== WLD Bd1 aurusa\"; grep -n \"aurusa\\|aurusa-\\|arusd\\|arusa\" incoming/WLD/WLD_Bd1_pages.txt | head -10\necho \"=== WLD band3 index olena\"; grep -n \"aratni\\|arusa\" WLD_band3.txt | head -10\necho \"=== IEC arus/elwa\"; grep -n \"^arus\\|^elwo\\|^elmos\\|^elkis\\|^olkis\" IEC.txt | head",
 "description": "WLD and Mann extra greps"
}
```


### [2026-09-05T20:39:02.940Z] TOOL RESULT

```
=== WLD Bd1 aurusa
=== WLD band3 index olena
=== IEC arus/elwa
```


## [2026-09-05T20:39:06.510Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '13990,14020p' incoming/WLD/WLD_Bd1_pages.txt\necho \"======= find el-1 heading\"\ngrep -n \"„rot, braun\\|rot, braun\" incoming/WLD/WLD_Bd1_pages.txt | head",
 "description": "WLD el-1 section"
}
```


### [2026-09-05T20:39:06.582Z] TOOL RESULT

```
to$,    osorb. los (letztere nicht aus                    dem Russ, entlehnt, s. v. d. Osten-Sacken
IF. 33, 192) „Elch“ (aus *olkis)\ schwundstufig ai. fca-h rcya-h „Antilopen-
bock‘ r pam. rus „wildes Bergschaf“ (s. dazu Ostholf aaO. 3 IS). Lit. bei
           i,



Zupitza         GG. 1SS. Yf. LEWb. 2 24.
   2.    Stamm *el-en-, *el-n-, mit Schwundstufe der Wz. *l-on-:
                                          -
   Gr. tlaffOQ ,,Hirseh‘ (*eln-bho-s),     „junger Hirsch" ( *elnos ; gegeii
Osthoft's aaO. Gdf. *dnios s. Brugmann Grdr. II 2 264a I); aksl. jelem, gen.
jelene „Hirsch“ (fem. lamp, laniji, alniji „Hirschkuh“ aus abgetontem *olnl ;
zur     Form s. Brugmann Grdr. II 2 219), lit. elnis, altlit. ellenis, ellinis „Elen-
tier“    (daraus            mhd. elent, nhd. Elen),                   lett.     alnis   „Elentier“,      lit.   elne       dine
.,Hirschkuh“, apr. alno ds.                   ;                         „Reh“
                                                  cymr. elain „Hirschkuh“                  (
                                                                                             *eltnl ), air. el it
(* rln-lt-s Fick II 4 42; iiber Formans -ti- in Tiernamen s. Petersson KZ. 47,
                 ;



240 f.), gall. Elembiu Monatsname, entsprechend dem gr. ekayrjfiofawv (Ricci
Rc. 21, 17, 23;; arm. t In, gen. el in .,Hirschkuh“ (Hiibschmann Arm. St. I,
29, Arm. Gr. I, 442).
   Apr. lonix               „Stier“               aber   lit.    *!onikas setzt           einen     n.   sg.    idg. *lan
voraus,         s.   Trautmann Apr. 371 mit Lit.; Osthoff Par. I 278 will aucli aksl.
laniji     auf *ldn-i, nicht *olnl zuriiekfiihren) ;                               ablautendes *lon- in gal. Ion
„Elentier“ (Strachan BB. 20, S f. Anm. 4                               ;
                                                                               Ficks II 4 255 Annahme von Ent-
======= find el-1 heading
```


## [2026-09-05T20:39:14.116Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"auru\\|aunisa\\|arusd-\\|„weiB“\\|„weiss“\" incoming/WLD/WLD_Bd1_pages.txt | sed -n '1,15p'\necho \"=== 13930-13970\"; sed -n '13930,13975p' incoming/WLD/WLD_Bd1_pages.txt",
 "description": "Find WP el-1 opening"
}
```


### [2026-09-05T20:39:14.191Z] TOOL RESULT

```
1304:ys/.drag. Wilamowitz Isyll y. Epidaurus 92 ff., berechtigt nicht zu einer Zer-
4624:sen KZ. 2, 17, Yanicek 15, Thesaurus s. v.) ist ebensowenig annehmbar
7507:„weiB“ etymologisch aich decke, a. dariiber zuletzt Geldner Rgveda Glos-
7517:„weiB“ verschiedenea Wort, gegen Bechtel Lexil. 57, der den Begriff des
7690:„fern, fremd" (= av. auruna- „wild"?),                           m
8288:Pflanze (vielleieht trotz Plin. n. h. 27, 41 gall. Wort? s. Thesaurus; wenn
8439:  Beziehung zu *albh- „weiB“ (Kuhn KZ. 4, 109 f., weitere Lit. bei Osthoff
8443:alblio- „weiB“.
8453:     lat.    albus          „weiB“,          Alafaternum „Alfaternorum“,
8528:u. dgl. auf den Begriff „weiB“ oder aber auf ,.bocli“ (4 al[e\blt-, *[a]loblt:
12736:vielleicbt av. auruna- „wild, grausam, von Tieren‘
14651: (Fick III 4 27), av. auruia- „weiB“ (Ygl. S. 359 unter reudh -), wohl mit
26916:    vara ..aufmerksam machen. wahren, vermuten, refl. sich hiiten"; got. dauru-
35254:   Lat. caurus (corns) „Nordwind“ (nach Hirt IF. 37, 224 mit lat. Wandel
35257:LEWb. 2 307 nicht wahrscheinlicher stellt Thurneysen Thes. fur caurus
=== 13930-13970
                                                                 1




bzw. gr. dgdco ai. drdm, wozu man erd- „zerllie£5en, Feuchtigkeit“ ver-
gleiche; weiter Petersson KZ. 47, 250ff.). mit anl. *ld- diber die arm.
Formen im                Bes.     vgl.    Petersson aaO.j.                      Dazu    altn.    nldua „schimmeln“,
wohl auch [/Ida „Moderduft“ (s. o.l, isl. uldinn (Bed. wie bei ul, ulen s. o.)                                         ,

usw., ahd. oltar „Schmutzkrume“.     tlber das im Not'd, auftretende u vgl.
(nicht iiberzeugendj Falk-Torp aaO.

   w-Formantien finden sich in:
  norw. dial, ithna ,.schimmeln“. nd. ostfr. ulm, uhn „Fiiulnis, bes. im IIolz“.
ulmen „verfaulen“, mnd. idmich „von Fiiulnis angefressen“, mhd. ulmic ds.
lit.times, almens „die aus der Leiche flietlende Fliissigkeit".
   Labialerweiterung liegt in arm. alb ,,Dreck“ vor (Liden aaO. 30).
   S. auch Yf. LEWb. 2 unter alga.



5. el-, ol- Schallwurzel.
  Arm. abnuk „Larm, Aufruhr usw.“ {[mo-, oder vielleicht *ubno-), isl. jalmr
,,Larm“, jalma „strepere, stridere, crepareT norw. mdartl. jalm, jelm „Schall“,
schwed. mdartl. jalm „Scbrei, Mi61aut“; norw. mdartl. alka          Handel an-                                .,


fangen        1
          ostfries. itlken ,,Unwesen treiben, sclireien, spotten, hohnen“ (nhd.
                  ’,



ulkcn), schwed. dial, alkeu „zu knurren anfangen"; lit. mialdcti „erschallen‘                                                 :
                                                                                                                                  .



S Falk-Torp u. id, Petersson KZ. 47. 2fi3: vielleicht beruhen auch die
154                                                             el-




Namen
```


## [2026-09-05T20:39:21.051Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '14640,14665p' incoming/WLD/WLD_Bd1_pages.txt\npython3 - <<'EOF'\nlines=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read().split('\\n')\nfor ln in (14651,):\n    leaf=sum(l.count('\\f') for l in lines[:ln]); print(ln,'leaf0',leaf,'printed',leaf+1-9)\nEOF",
 "description": "WP I auruša context and page"
}
```


### [2026-09-05T20:39:22.832Z] TOOL RESULT

```
d. Wiesel; vgl. Kluge EWb., Falk-Torp 461); germ. *ella- ware aus el-na-
zu erkliiren, der litis also nach den rotgelben Haaren benannt. Weitere
mogliche Ankniipfung an el- in Baumnamen wie Erie Ubne (s. *el-).                                                            ,


   Yerglichen wird ai. aruna- „rotlich, goldgelb , amid „rot, feuerfarben“
                                                                                                     11




 (Fick III 4 27), av. auruia- „weiB“ (Ygl. S. 359 unter reudh -), wohl mit
 Recht, weiter lit. divas lett. alvs, alva apr. alicis „Zinn“ ( *olu -), abg. olovo
                                             ,                                 ,


 „Blei“, ru. olovo „Zinn“ *olou -), vgl. Brugmann Grdr 2 II, 1,201. Persson
                                                     (
                                                                                                                         .



 Wortf. 302 f. s. u. Bd. II 359 {reudh-). t)ber lat. luridus s. u. ghtl- „gelblicli“.
                       ;


14651 leaf0 167 printed 159
```


## [2026-09-05T20:41:04.032Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nlines=open('KNT.txt',encoding='utf-8',errors='replace').read().split('\\n')\nfor ln in (5049,1118):\n    leaf=sum(l.count('\\f') for l in lines[:ln]); print(ln,'leaf',leaf,'printed(lex +15)',leaf-15,'printed(gram +13)',leaf-13)\nEOF\necho \"=== BQT leaf 242 (p.32)\"\npython3 - <<'EOF'\ntxt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nL=txt.split('\\f')[242]\nimport re\ni=L.find('آرنج')\nprint(L[max(0,i-700):i+400])\nEOF",
 "description": "Kent page and Borhan p.32 text"
}
```


### [2026-09-05T20:41:05.701Z] TOOL RESULT

```
5049 leaf 191 printed(lex +15) 176 printed(gram +13) 178
1118 leaf 46 printed(lex +15) 31 printed(gram +13) 33
=== BQT leaf 242 (p.32)
دخانه ات .
]دغده ؟- بن الك ( ۲ ) بر وزن
آزرده. بمعنی نخبناك (۳)وخشمگین وقهر آ لود -
و جنگاور باشد - و بفتخ الث حريصي در چپزها
را گویند .
۲۰ ریش «- بنتح اول و ثانی ۰ بر وزت
صم کیش ۷. بوست. بیرخت زرهاباخد وآنرا
دو دازو ها چشم نیزبکار برند .
۱ آآرمان ۴ بر وزن آسمان ۰ بمعنی
جح تب و آرزو - و رنج بردن باشد - و پشیمانی
و آفوی را نیز گویند . *
آمده - بکر میم ۵ . مخفف
وسکون میم بروزن دارنده. بمعنی دریغ‌وافوی
و پشیمانی باشد .
] دهش » بکس میم . مخنف آرامش
)۱ خم ۳ آارغاوه ۰
)4( خم ۳ 0 رنگ دادن.
و
است که ساکن شدن و آساش ‏ فراغت وراحت
کردن باشد .
آدهون - بر وزن ولژگون » زری
را گوند که پیش از کارکردن بکارگر و هزدور
دهند . و معربی «عربون» خواند . 4
| رهیفه » بر وزن نا رسیده . قرار
] دن ه بر وزن فارن . مخفف آرنج
است که بند گاه ساعدوبازو باشد. وبعربی«مرفق»
خوانند ۷ ,
اد نج - بر ون نارنج . بندکگاه
ساعد و بازوست که عرب « مرفق » گوید ۷ - و
بمعنی بازو هم بنظر آعده است که ازمرفق باشد
تا دوش .
]را نگ - باکاف فارسی. بروزن وهعنی
آرنج‌است که مرفی‌داشد - ور نگ ولون (4)را
یز کنته اند - و بمعنی حمانا و پنداری وگمان
بری حم‌آعده است - وونج ومجنت‌را عم گویشدب
و بمعئی مکر و حیله و فررت تیز حستتویمعنی
کونه وروش و طرز
```


## [2026-09-05T20:51:07.555Z] TOOL CALL #71: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build152.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW_AL   = \"https://en.wiktionary.org/wiki/%D8%A2%D9%84\"\nW_AR   = \"https://en.wiktionary.org/wiki/%D8%A2%D8%B1%D9%86%D8%AC\"\nW_ARAS = \"https://en.wiktionary.org/wiki/%D8%A7%D8%B1%D8%B4\"\nW_LAMB = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/lambaz\"\nW_ALIN = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/alin%C5%8D\"\nE_ELB  = \"https://www.etymonline.com/word/elbow\"\nE_ELK  = \"https://www.etymonline.com/word/elk\"\nE_ELM  = \"https://www.etymonline.com/word/elm\"\nE_LAMB = \"https://www.etymonline.com/word/lamb\"\nE_ALD  = \"https://www.etymonline.com/word/alder\"\n\ndoc = {\n \"pdf_page\": 152,\n \"book_page\": 122,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"El 2, Elk, Eln\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *el- / *h₁el- 'red, brown' (in tree and animal names) — Pokorny '1. el-, ol-, l-' pp. 302-304; Watkins/AHD 'el-²'\",\n   \"note\": \"The root box is right on all three counts. Pokorny's lemma reads 'Root/lemma: el-1, ol-, l- ... Meaning: red, brown (in names of trees and animals) ... Page(s): 302-304', so Nourai's gloss is a near-verbatim rendering of Pokorny's own and POK:302 is the correct page. His two extra head-names are Pokorny's own extensions: 'Elk' = the k-extension *olki- (OHG elaho, OE eolh, ON elgr 'elk'), 'Eln' = the n-stem *el-en-/*l-on- (Gk. ἔλαφος, Lith. elnis, Arm. eḷn 'deer'). KLN:509 is right too: Klein's printed p.509 (the leaf running from 'elevation' to 'ellipse' in KLN_1966.txt, between the page markers 508 and 510) carries s.v. elk 'These words derive fr. I.-E. base *elk-, a -k-enlargement of base *el-, ‚brown‘'. Watkins's appendix has 'el-2. Red, brown (forming animal and tree names)' and lists under it exactly ELM, ALDER, ELK, i.e. Nourai's nodes #4-#5, with '[Pok. 1. el- 302.]'. Two branches of the chart are weaker than the root: the Germanic lamb branch (nodes #6-#7) is Pokorny's and Klein's view but is called doubtful by Buck and Etymonline, and the Persian outcome آل (node #3) cannot be got out of Pahlavi arus by any Persian sound law — that link is the one real error on this chart.\",\n   \"note_fa\": \"خودِ ریشه درست است: پوکورنی در صفحات ۳۰۲–۳۰۴ مادهٔ el-1 را با معنای «سرخ، قهوه‌ای — در نام درختان و جانوران» آورده و همان را نورایی ترجمه کرده است؛ دو نام دیگرِ سربرگ (Elk و Eln) نیز همان گسترش‌های *olki- و *el-en- در کتاب پوکورنی‌اند. کلاین نیز در ص ۵۰۹ زیر elk همین ریشه را می‌دهد و واتکینز در پیوستِ فرهنگ American Heritage زیر el-2 دقیقاً همین سه واژهٔ elm و alder و elk را می‌آورد. دو شاخه سست‌تر است: پیوندِ lamb به این ریشه را باک و اتیمولاین مشکوک می‌دانند، و مهم‌تر اینکه واژهٔ فارسی «آل» با هیچ دگرگونی آوایی شناخته‌ای از پهلوی arus به دست نمی‌آید و تنها خطای جدی این نمودار همان پیکان است.\",\n   \"sources\": [E_ELK],\n   \"ref_check\": [\n    {\"ref\": \"POK:302\", \"status\": \"supports\", \"note\": \"POK_full.txt block 'Root /lemma: el-1, ol- el- ... Meaning: red, brown (in names of trees and animals) ... Page(s): 302-304' (lines 25153-25351). Its material section A opens 'Old Indic arusa-h ‚fire-color‘, Avestan aurusa- ‚white‘; Germanic *elwa- ‚brown, yellow‘ in Old High German elo' and section B/C give the alder, elm and elk words — the whole chart except the Persian outcome.\"},\n    {\"ref\": \"KLN:509\", \"status\": \"supports\", \"note\": \"KLN_1966.txt, printed page 509 (between the OCR page markers '508' at line 12823 and '510' at line 12851), s.v. elk: 'These words derive fr. I.-E. base *elk-, a -k-enlargement of base *el-, ‚brown‘. For derivatives of *eln-, -n-enlargement of base *-el-, see eland'. The same printed page also carries 'ell', which is why Nourai cites p.509 for the next root as well.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. el-2 (AHD_watkins1985.txt line 435)\", \"stance\": \"supports\", \"note\": \"'el-2. Red, brown (forming animal and tree names). 1. Extended form *elmo- in Germanic *elmo-, *almo- in Old English elm, elm: ELM. 2. Germanic extended form *aliza, alder, in Old English alor: ALDER. ... 4. Extended o-grade form *olki- in Germanic *alkiz, elk ... : ELK. [Pok. 1. el- 302.]'\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. I 151-159 (WLD_Bd1_pages.txt leaves 162-167)\", \"stance\": \"supports\", \"note\": \"Walde-Pokorny treat the same complex: p.154 the stem '*el-en-, *el-n-, mit Schwundstufe der Wz. *l-on-' with Gk. ἔλαφος and Goth. lamb, p.159 'Verglichen wird ai. aruna- ‚rötlich, goldgelb‘, arusá- ‚rot, feuerfarben‘ ..., av. aurusa- ‚weiß‘ (vgl. S. 359 unter reudh-), wohl mit Recht'.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 3.29 'Lamb', p.160\", \"stance\": \"partial\", \"note\": \"'Goth., ON, OE lamb, etc., the general Gmc. word, perh.: Grk. ἔλαφος ‚stag‘ and other animal names, but root connection and primary sense dub. Walde-P. 1.154.' — Buck accepts the root but flags the lamb branch as doubtful.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Avestan\", \"words\": \"auruša\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Avestan auruša- 'white' is the exact Iranian counterpart of Sanskrit aruṣá- 'reddish, flame-coloured' (epithet of Agni's horses); both continue Indo-Iranian *arušá-, a u-stem colour adjective built on PIE *el- 'red, brown'. The Avestan au- for expected a- is the regular Avestan u-epenthesis in the sequence a-ru- (compare Av. auruna- 'wild' beside Skt. aruṇá-), not a separate ablaut grade. In the Yašts it is an animal colour word — aspahe kəhrpa aurušahe 'in the shape of a white horse' (Yt. 8.18-21), pasūm aurušəm 'a white sheep' (Yt. 8.58) — and it is the Iranian narrowing 'ruddy' > 'bright pale' > 'white' that produces Nourai's double gloss 'pale red, white'.\",\n     \"derivation_fa\": \"اوستایی auruša- «سپید» برابرِ دقیقِ سنسکریت aruṣá- «سرخ‌فام، آتش‌رنگ» است و هر دو از هندوایرانی *arušá- می‌آیند، ستاکی بر ریشهٔ هندواروپایی *el- «سرخ، قهوه‌ای». الفِ آغازین در اوستایی به سبب «پیش‌آوایی» (epenthesis) پیش از ru به au- بدل شده است، همان‌گونه که auruna- در برابرِ aruṇá-ی سنسکریت. بارتولومه (ستون ۱۹۰) آن را صفتِ جانوران می‌داند: «اسبِ سپید»، «گوسفندِ سپید». تحول معنایی «سرخ‌فام > روشن > سپید» در ایرانی رخ داده است؛ ادعای نورایی درست است.\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\"ref\": \"POK:302\", \"status\": \"supports\", \"note\": \"Pokorny el-1 (pp.302-304), material A: 'Old Indie arusa-h ‚fire-color‘, Avestan aurusa- ‚white‘; Germanic *elwa- ‚brown, yellow‘' (POK_full.txt line ~25163) — exactly the arrow drawn.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"col. 190 (BRT.txt line 5386, running head 'aurusa- / 190')\", \"stance\": \"supports\", \"note\": \"'j. auruša- Adj. ‚weiss‘, 1) von Tieren: pasūm .. ˚həm ... ‚ein weisses oder schwarzes Schaf‘ Yt.8.58; — aspahe kəhrpa ˚he .. ‚in Gestalt eines weissen Rosses‘ Yt.8.18-21'. This is the column Mo'in's Borhan footnote cites for the whole chain.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. I 159 (WLD_Bd1_pages.txt line 14651)\", \"stance\": \"supports\", \"note\": \"'Verglichen wird ai. aruna- ‚rötlich, goldgelb‘, arusá- ‚rot, feuerfarben‘ (Fick III⁴ 27), av. aurusa- ‚weiß‘ (vgl. S. 359 unter reudh-), wohl mit Recht' — Walde-Pokorny accept the equation but note the competing tie to *reudh- 'red', which matters for node #3.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"arŭs\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Middle Persian arus [ʾplws] 'white' is the regular Pahlavi continuation of Old Iranian *aruša- (= Av. auruša-): the Avestan epenthetic u- of the first syllable is not shared by Persian, intervocalic -š- is kept, and the thematic -a is lost with the general Middle Persian apocope. MacKenzie's Concise Pahlavi Dictionary p.12 has the bare entry 'arus [ʾplws] white', and it is also the word the Pahlavi Zand puts where the Avesta has auruša-; Mo'in states this equation on the very page Nourai cites (Borhān p.55, footnote 7: 'در ترجمهٔ پهلوی arus (سپید) «بارتولومه ۱۹۰-۱۹۱»'). Nourai's transcription with a breve, arūs, is his usual notation for the Pahlavi u.\",\n     \"derivation_fa\": \"پهلوی arus «سپید» دنبالهٔ مستقیم ایرانی باستان *aruša- است: پیش‌آواییِ ویژهٔ اوستایی (au-) در فارسی میانه نیست، شین میان‌واکه‌ای می‌ماند و اِ پایانی با حذفِ عامِ پایانه‌ها می‌افتد. مکنزی در ص ۱۲ می‌آورد: arus [ʾplws] white، و معین در حاشیهٔ ص ۵۵ِ برهان قاطع همین زنجیره را با ارجاع به بارتولومه ثبت کرده است. ادعای نورایی در این خانه درست است.\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\"ref\": \"BQT:55\", \"status\": \"supports\", \"note\": \"Borhān-e Qāţeʽ printed p.55 = BQT_v1_pages.txt leaf 265, footnote 7 to the headword آل: 'اوستا auruša (سفید)، سانسکریت aruṣa (سرخ رنگ)، در ترجمه و زند پهلوی arus (سفید) «پارتولمه [= بارتولومه] ۱۹۰-۱۹۱»' — Nourai's node #1>#2 arrow verbatim.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"p.12 (PHD.txt leaf 33, PHD_pages.txt line 1186)\", \"stance\": \"supports\", \"note\": \"MacKenzie: 'arus [ʾplws] white.' (the same page also has āranj and ārešn, the two words of the next chart).\"},\n      {\"src\": \"NYB\", \"where\": \"Part II Glossary\", \"stance\": \"silent\", \"note\": \"grep of NYB_vol2_glossary.txt for 'arus', 'ʾplws' and 'white' finds no headword; Nyberg's glossary covers only the texts of Part I, which do not contain the word.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Persian\", \"words\": \"âl; âlgūneh\", \"verdict\": \"disputed\",\n     \"derivation\": \"Both words are real and well attested. آل (āl) 'crimson, red; pale red' is in Borhān p.55 ('آل ... سرخِ رنگ را گویند') and in Mo'in ('آل [= آلا، ماز. سرخ کم‌رنگ] (ص) سرخ، احمر'), and آلگونه / آلغونه 'rouge' is Borhān p.57 ('که غازه و سرخیِ زنان باشد') with Mo'in's note 'مرکب از: آل (سرخ) + گونه (رنگ)' and Shahid Balkhi's line quoted in the chart. What is disputed is the parentage. Middle Persian arus would give New Persian arus/aros; there is no Persian development by which -ruš yields -āl, and no lexicographer records an intermediate. The modern accounts collected by Wiktionary are all different: Benveniste treats āl-gōnak as the attested older form and connects it with the Achaemenid woman's name Ἀλογούνη in Ctesias; Bailey makes āl a merger of Proto-Iranian *āla- and *harda- (cf. Av. harəda-); Walther Hinz posits Proto-Iranian *Hṛda- from PIE *h₁rewd̤ʰ- 'red', the same source he gives for آلو 'plum' and آله 'eagle'. The link with Turkic al 'scarlet' is judged coincidental (or Turkic < Iranian). Nourai is faithfully reproducing Mo'in's 1963 footnote, which is the older view; Walde-Pokorny I 159 already redirected the Indo-Iranian 'red' words of this group to *reudh-, and that is where modern Iranists put آل.\",\n     \"derivation_fa\": \"خودِ واژه‌ها درست‌اند: «آل» در برهان قاطع (ص ۵۵) «سرخِ رنگ» و در فرهنگ معین «سرخ، احمر» (و در مازندرانی «سرخ کم‌رنگ») آمده و «آلگونه/آلغونه» هم به گفتهٔ معین مرکب است از «آل (سرخ) + گونه (رنگ)» و در بیت شهید بلخی همین نمودار گواهی شده است. امّا پیوند دادنِ آن به پهلوی arus «سپید» از نظر آوایی شدنی نیست؛ arus در فارسی نو باید arus/aros می‌شد و هیچ قاعده‌ای شین را به لام بدل نمی‌کند. پژوهش امروزی سه راهِ دیگر پیش می‌نهد: بنونیست صورت کهن را āl-gōnak می‌داند و آن را با نامِ «آلگونه»ی هخامنشی در کتزیاس مرتبط می‌کند؛ بیلی آن را آمیزهٔ دو ستاکِ *āla- و *harda- می‌داند؛ و هینتس ایرانی باستان *Hṛda- از ریشهٔ *h₁rewd̤ʰ- «سرخ» را پیشنهاد کرده که همان خاستگاهِ «آلو» و «آله» است. پس پژوهش امروزی ادعای نورایی را رد می‌کند؛ او حاشیهٔ معین (۱۳۴۲) را بازگو کرده که دیدگاهی کهنه است.\",\n     \"sources\": [W_AL],\n     \"ref_check\": [\n      {\"ref\": \"BQT:55\", \"status\": \"supports\", \"note\": \"Borhān p.55 (BQT_v1_pages.txt leaf 265) headword 'آل: به سکون لام بر وزن زال، سرخِ رنگ را گویند' with footnote 7 giving Nourai's whole chain (Av. auruša > Skt aruṣa > Phl. arus); the printed آلگونه entry with Mo'in's note 'مرکب از: آل (سرخ) + گونه (رنگ)' and the Shahid Balkhi verse 'آن بناگوش کز صفا گویی — برکشیده است آلگونه به سیم' is two pages further on (leaf 267 ≈ p.57). So the reference does say what Nourai says — it is the reference, not the transcription, that modern scholarship has moved past.\"},\n      {\"ref\": \"MON:80\", \"status\": \"partial\", \"note\": \"Mo'in's Farhang s.v. آل (MON_part1.txt line 4184): 'آل [= آلا. ماز. سرخ کم رنگ] (ص.) سرخ، احمر: لاله آل ... سرخ نیمرنگ: خون آل' — confirms Nourai's gloss 'pale red, pink' precisely (سرخ کم‌رنگ / سرخ نیم‌رنگ), but the copy on disk (2-vol Adena reprint) carries no etymological tag, so it does not corroborate the Pahlavi source.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"p.12\", \"stance\": \"partial\", \"note\": \"MacKenzie has arus 'white' but records no New Persian continuant for it in his '| N ~' column, whereas he does for the neighbouring āranj and ārešn — i.e. no Pahlavi dictionary posits arus > آل.\"},\n      {\"src\": \"HRN\", \"where\": \"Grundriss der neupersischen Etymologie\", \"stance\": \"silent\", \"note\": \"grep of HRN.txt finds no entry for āl/ālgūna; Horn's alphabetical ā- section (nos. 1-40) jumps from āšām- to ālū, with no 'red' word.\"},\n      {\"src\": \"ARY\", \"where\": \"Aryanpur, Rishe-hā-ye Hend-o-Orupāyi\", \"stance\": \"silent\", \"note\": \"grep of ARY_pages.txt finds no آل / آلگونه headword (only آلمانی etc.), although Aryanpur does treat آرنج on p.54 — an independent modern Persian root-dictionary declines to derive آل at all.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"Germanic\", \"words\": \"elmo, almo, elwa\", \"verdict\": \"confirmed\",\n     \"derivation\": \"All three forms are quotations from Nourai's cited source. Watkins's appendix under el-2 has 'Extended form *elmo- in Germanic *elmo-, *almo- in Old English elm' — the *elmo-/*almo- pair is the o- and zero-grade doublet behind OE/OHG elm on the one hand and ON almr, MLG olm on the other (Latin ulmus is the same formation, *l̥-mo-). *elwa- is Pokorny's Germanic colour adjective 'brown, yellow' (p.302: 'Germanic *elwa- ‚brown, yellow‘ in Old High German elo (elawer), Middle High German el (elwer)'), the -w- stem beside the tree-name -m- stem. All three are reconstructions, not attested words, which is why the box has no script column.\",\n     \"derivation_fa\": \"هر سه صورت، بازساخته‌اند و عیناً از منابعِ مورد استنادِ نورایی گرفته شده‌اند: واتکینز زیر el-2 می‌نویسد *elmo-, *almo- در ژرمنی آغازین که به انگلیسی کهن elm می‌رسد (و لاتین ulmus هم‌ساختِ همان است)، و پوکورنی در ص ۳۰۲ صفتِ رنگِ *elwa- «قهوه‌ای، زرد» را با شاهدِ آلمانی بالای کهن elo می‌آورد. ادعای نورایی درست است.\",\n     \"sources\": [E_ELM],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. el-2 (AHD_watkins1985.txt line 437): 'Extended form *elmo- in Germanic *elmo-, *almo- in Old English elm, elm: ELM. 2. Germanic extended form *aliza, alder ... 4. Extended o-grade form *olki- in Germanic *alkiz, elk'. Nourai cites AHD without a page, as he does for all Watkins references.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"pp. 302-303 (POK_full.txt lines 25163, 25230 ff.)\", \"stance\": \"supports\", \"note\": \"'Germanic *elwa- ‚brown, yellow‘ in Old High German elo (elawer). Middle High German el (elwei)'; and under 'elm': 'Compare further Old High German elmboum ‚elm‘, Old Norse almr (with o-grade)... so that possibly Germanic contains all three Abl.-grades'.\"},\n      {\"src\": \"SKT\", \"where\": \"p.135 s.v. Elm\", \"stance\": \"partial\", \"note\": \"'Elm, a tree (E.) A.S. elm + Icel. almr, Dan. alm, Swed. alm, G. (formerly) elme, L. ulmus. (√AL.)' — Skeat has the same Germanic ablaut set but files it under a root '√AL', not under el- 'red, brown'.\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"English\", \"words\": \"elm, alder, elk\", \"verdict\": \"confirmed\",\n     \"derivation\": \"The three English words are the ones Watkins himself lists under el-2. ELM < OE elm < PGmc *elmaz (Etymonline: 'from Proto-Germanic *elmaz ..., perhaps from PIE root *el- (2) ‚red, brown‘'). ALDER < OE alor < PGmc *aliso, with an unetymological -d- inserted in the 14th century (the older aller survives dialectally as Lancashire owler); the tree is named from its bark, which turns red-orange when cut. ELK: late OE elch, reinforced by ON elgr, from PGmc *elkh- < PIE *olki-, 'perhaps with reference to the reddish colour from root *el- (2)'; Greek ἄλκη and Latin alces are borrowings from Germanic, not cognates. Each of the three therefore names its referent by colour, which is the whole point of Pokorny's lemma.\",\n     \"derivation_fa\": \"هر سه واژه همان‌هایی‌اند که واتکینز زیر el-2 می‌آورد. elm از انگلیسی کهن elm و ژرمنی آغازین *elmaz؛ alder از انگلیسی کهن alor و ژرمنی *aliso که دالِ غیراشتقاقی در سدهٔ چهاردهم میلادی به آن افزوده شده است (صورت کهن aller)؛ و elk از *olki- و ژرمنی *elkh-، که یونانی ἄλκη و لاتین alces وام‌واژه از ژرمنی‌اند نه هم‌ریشه. هر سه نام بر پایهٔ رنگِ سرخ‌قهوه‌ای نهاده شده‌اند و ادعای نورایی درست است.\",\n     \"sources\": [E_ELM, E_ELK, E_ALD],\n     \"ref_check\": [\n      {\"ref\": \"(none)\", \"status\": \"not_checked\", \"note\": \"the box carries no reference in the printed book; the parent Germanic box cites AHD, and Watkins's el-2 entry names precisely ELM, ALDER and ELK as its English outcomes.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"p.509 s.v. elk\", \"stance\": \"supports\", \"note\": \"'elk, n., the largest existing deer. — ON. elgr, rel. to OE. eolh, OHG. elaho ... These words derive fr. I.-E. base *elk-, a -k-enlargement of base *el-, ‚brown‘.'\"},\n      {\"src\": \"SKT\", \"where\": \"p.135 s.v. Elm\", \"stance\": \"partial\", \"note\": \"Skeat has elm with the Germanic and Latin cognates but files it under '√AL' and has no colour gloss; he gives no root for alder either.\"}\n     ]\n    },\n    {\n     \"id\": 6, \"lang\": \"Germanic\", \"words\": \"lambiz\", \"verdict\": \"plausible\",\n     \"derivation\": \"Nourai's 'lambiz' is Proto-Germanic *lambaz/*lambiz-, a neuter es/os-stem whose oblique and plural stem is *lambiz- (OE plural lambru < *lambizu, OHG lembir); the class was extended in Germanic on the model of *kalbiz- 'calf'. The derivation from the colour root is Klein's and Pokorny's: Klein p.860 'for orig. *lon-bho-s; cogn. with Gk. ἔλαφος (for *eln-bhos) ‚hart‘, ἔλλός (for *elnos) ‚fawn‘. All these words are traceable to I.-E. base *el-, ‚brown‘'; Walde-Pokorny I 154 'sehr wahrscheinlich als *l-on-bho-s (mit demselben Suffix wie ἔλαφος)'; Wiktionary still reconstructs *h₁l̥h₁-on-bʰ-os-, an enlargement of *h₁elh₁én from *h₁el- 'deer, elk'. But the connection is not universally accepted: Buck (3.29, p.160) says 'root connection and primary sense dub.' and Etymonline flatly reports 'Common to the Germanic languages but with no certain cognates beyond them'. Hence plausible rather than confirmed.\",\n     \"derivation_fa\": \"صورتِ lambiz همان ژرمنی آغازین *lambaz/*lambiz- است، ستاکی خنثی از گونهٔ -es/-os که جمعِ انگلیسی کهن lambru و آلمانی کهن lembir از آن می‌آید. پیوند زدنِ آن به ریشهٔ «سرخ/قهوه‌ای» از آنِ کلاین و پوکورنی است (*l-on-bho-s با همان پسوندِ ἔλαφος «گوزن») و ویکی‌واژه نیز هنوز همین را می‌پذیرد؛ امّا باک (ص ۱۶۰) آن را «مشکوک» می‌خواند و اتیمولاین می‌گوید بیرون از ژرمنی هیچ هم‌ریشهٔ قطعی ندارد. پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n     \"sources\": [W_LAMB, E_LAMB],\n     \"ref_check\": [\n      {\"ref\": \"KLN:860\", \"status\": \"supports\", \"note\": \"KLN_1966.txt line 21040, immediately after the printed page markers '860'/'861' at lines 21029-21030: 'lamb, n. — ME. lamb, lomb, fr. OE. lamb, rel. to OS., ON., OFris., OHG., Goth. lamb ... for orig. *lon-bho-s; cogn. with Gk. ἔλαφος (for *eln-bhos), ‚hart‘ ... All these words are traceable to I.-E. base *el-, ‚brown‘. See eland, elk.' — Nourai's page is exact.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"WLD\", \"where\": \"Bd. I 154 (WLD_Bd1_pages.txt line 14023)\", \"stance\": \"supports\", \"note\": \"'dazu weiter ... sehr wahrscheinlich als *l-on-bho-s (mit demselben Suffix wie ἔλαφος) auch got. lamb ‚Schaf‘, anord. lamb ‚Lamm, Schaf‘, ahd. lamb ‚Lamm‘ (großenteils neutr. -es-St., was gemeingerm. Neuerung nach Kalb scheint)'.\"},\n      {\"src\": \"SYN\", \"where\": \"Buck 3.29 'Lamb', p.160\", \"stance\": \"partial\", \"note\": \"'Goth., ON, OE lamb, etc., the general Gmc. word, perh.: Grk. ἔλαφος ‚stag‘ and other animal names, but root connection and primary sense dub.'\"},\n      {\"src\": \"SKT\", \"where\": \"p.239 s.v. Lamb\", \"stance\": \"silent\", \"note\": \"'Lamb. (E.) M.E. lamb, lemb. A.S. lamb. + Du. lam, Icel. lamb, Dan. lam, Swed. and G. lamm, Goth. lamb, a young sheep.' — Germanic cognates only, no IE root offered.\"}\n     ]\n    },\n    {\n     \"id\": 7, \"lang\": \"English\", \"words\": \"lamb\", \"verdict\": \"plausible\",\n     \"derivation\": \"English lamb continues Middle English lomb/lamb, Old English lamb (Northumbrian lemb, plural lambru), from Proto-Germanic *lambaz; the -b has been silent since the 13th century. The word itself is beyond doubt — what carries over from the parent node is the uncertainty about the Indo-European connection: Klein (Nourai's source, p.860) and Pokorny 302-304 file it under *el- 'brown' beside Greek ἔλαφος 'hart', and Wiktionary follows them, while Buck and Etymonline treat Germanic *lambaz as isolated. The same verdict therefore stands here as on node #6.\",\n     \"derivation_fa\": \"انگلیسی lamb از انگلیسی میانه lomb/lamb و انگلیسی کهن lamb (جمع: lambru) می‌آید و بای پایانی آن از سدهٔ سیزدهم به بعد خوانده نمی‌شود. خودِ واژه مسلّم است؛ آنچه محل تردید است، پیوندِ آن با ریشهٔ هندواروپاییِ «سرخ/قهوه‌ای» است که کلاین (ص ۸۶۰، همان مأخذِ نورایی) و پوکورنی می‌پذیرند و باک و اتیمولاین رد می‌کنند. داوری همان است که در خانهٔ پیشین آمد: با احتیاط پذیرفتنی است.\",\n     \"sources\": [E_LAMB, W_LAMB],\n     \"ref_check\": [\n      {\"ref\": \"KLN:860\", \"status\": \"supports\", \"note\": \"same entry as node #6 — Klein's headword is the English word 'lamb' itself, on printed p.860 of the 1966 edition; he traces ME lamb, lomb < OE lamb and then to *el- 'brown'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"SYN\", \"where\": \"Buck 3.29, p.160\", \"stance\": \"partial\", \"note\": \"lists NE lamb in the Germanic column of 3.29 'Lamb' but calls the root connection 'dub.'\"},\n      {\"src\": \"SKT\", \"where\": \"p.239\", \"stance\": \"silent\", \"note\": \"Skeat gives only the Germanic cognates, no IE root.\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 1,\n   \"root\": \"El 3, Elei, Lei, Olěna\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *el-, *elē̆i-, *lē̆i- 'to bow, bend', with the derived noun *olī̆nā / *Heh₃l-én- 'elbow, forearm, ell' (Pokorny '8. el-, elei-, lei-' pp. 307-309)\",\n   \"note\": \"Correct on every count, and the four head-names are the lemma line of Nourai's sources read straight off the page. Pokorny 307-309 has 'Root/lemma: el-8, elei-, lei- ... Meaning: to bow, bend; elbow', which is Nourai's 'El 3, Elei, Lei : to bend, elbow' exactly; Walde-Pokorny I 156 head the same article 'elei-, lei- ‚biegen‘' and open it 'Hierher stellen sich zunächst Bezeichnungen für ‚Ellenbogen‘ und ‚Elle‘'. The fourth name Olěna is the noun *olena/*olīnā that Klein p.509 s.v. ell gives as the base ('fr. I.-E. base *olena, whence also OI. aratnih ‚elbow, ell‘, Gk. ὠλένη, L. ulna'), and which Mann (IEC p.942) enters as 'olénā, olinā, olənā ‚forearm, elbow, ell‘'; so KLN:509 does double duty for this root and the previous one, both words falling on that single printed page. Buck's 4.32 ELBOW (p.238) sets out the same family, ending 'Skt. aratni-, Av. araθna- ‚elbow‘ (Av. fraraθni- ‚ell‘)', i.e. Nourai's nodes #1 and #4. The one thing that needs correcting is not the root but the Persian column: node #2 is a Middle Persian word in a box labelled Persian, and node #3 is not its descendant but its cousin (see those nodes).\",\n   \"note_fa\": \"ریشه و معنا و نام‌های سربرگ همگی درست‌اند: پوکورنی در صفحات ۳۰۷–۳۰۹ مادهٔ el-8, elei-, lei- «خم کردن؛ آرنج» را آورده، والده–پوکورنی (ج۱ ص ۱۵۶) همین ماده را با عنوان «خم کردن» آغاز می‌کند و نخست نام‌های «آرنج» و «ذراع» را می‌شمارد، و نامِ چهارم (Olěna) همان *olena است که کلاین در ص ۵۰۹ ذیل ell پایهٔ یونانی ὠλένη و لاتین ulna می‌داند. باک نیز در بخش ۴٫۳۲ (ص ۲۳۸) همین خانواده را با سنسکریت aratni- و اوستایی araθna- و frāraθni- می‌آورد. تنها لغزشِ نمودار در ستون فارسی است: خانهٔ ۲ واژه‌ای فارسی میانه است که «فارسی» برچسب خورده، و «آرنج» فرزندِ آن نیست بلکه هم‌نیای آن است.\",\n   \"sources\": [E_ELB, W_ALIN],\n   \"ref_check\": [\n    {\"ref\": \"POK:308\", \"status\": \"supports\", \"note\": \"POK_full.txt lines 25549-25713: 'Root / lemma: el-8, elei-, lei- ... Meaning: to bow, bend; elbow ... Page(s): 307-309'. Material A: 'Gr. ὠλένη ‚elbow‘ ... Latin ulna (from *olina) ... Gothic aleina ‚ulna, ell‘ ... simple root *ōle- in Old Indic aratní-ḥ ‚elbow‘, Avestan araθna- ds., fra-raθni- ‚ulna, ell‘, Old pers. arašniš ds.' — the entire chart in one paragraph, so p.308 is exactly right.\"},\n    {\"ref\": \"KLN:509\", \"status\": \"supports\", \"note\": \"KLN_1966.txt printed p.509, s.v. ell: 'ME. ellen, eln, fr. OE. eln ... Goth. aleina, fr. I.-E. base *olena, whence also OI. aratnih, ‚elbow, ell‘, Gk. ὠλένη, ‚elbow‘, L. ulna ... Cp. elbow.' The same page carries 'elk', which is why Nourai gives KLN:509 for El 2 as well.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. I 156 (WLD_Bd1_pages.txt line 14310)\", \"stance\": \"supports\", \"note\": \"'elei-, lei- ‚biegen‘. Hierher stellen sich zunächst Bezeichnungen für ‚Ellenbogen‘ und ‚Elle‘: Gr. ὠλένη ‚Ellenbogen‘ ... lat. ulna aus *olena ... Den gleichen langen Mittelvokal zeigt das Got. aleina ‚Elle‘'. Nourai's root names 'Elei, Lei' are this lemma's title.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 4.32 ELBOW, p.238\", \"stance\": \"supports\", \"note\": \"'1. Derivs. of IE *el-, *ele-, etc. ‚bend‘ (but primary verbal forms lacking) in words for ‚forearm‘ (as measure ‚ell, cubit‘), and ‚elbow‘. Walde-P. 1.156 ff. ... Skt. aratni-, Av. araθna- ‚elbow‘ (Av. fraraθni- ‚ell‘).'\"},\n    {\"src\": \"IEC\", \"where\": \"Mann, ~p.942 (IEC.txt line 12110)\", \"stance\": \"supports\", \"note\": \"'olénā, olinā, olənā ‚forearm, elbow, ell‘ WP I, 156 Per. cf. arang ‚elbow‘; Oss. árm-àrin ...: Gk. olénē ...; Lat. ulna ...; Go. aleina ...; OE eln' — Mann's headword is Nourai's fourth root name, and he even lists the Persian word.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Avestan\", \"words\": \"arethna\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Avestan arəθna- m. 'elbow' (Nourai transliterates the θ as th) continues Proto-Iranian *aratni-, the exact match of Sanskrit aratní- 'elbow, ell'; the group *-tn- gives Avestan -θn- while Old Persian gives -šn- (node #5). It is a rare word, cited by Bartholomae (col. 193) only in the nominative-accusative dual arəθnā from the Frahang ī Ōim; the gloss 'arm, elbow' is a little wide — Bartholomae, Buck and Pokorny all give simply 'elbow' — but the extension to 'forearm' is what the derived measure frāraθni- (node #4) presupposes. Walde-Pokorny I 70 make the point explicitly against Persson: aratní-, arəθna- and frāraθni- 'bleiben ... besser bei der Sippe von ὠλένη', i.e. under this root and not under *ar- 'to join'.\",\n     \"derivation_fa\": \"اوستایی arəθna- «آرنج» دنبالهٔ ایرانی باستان *aratni- است که برابرِ دقیقِ سنسکریت aratní- می‌باشد؛ خوشهٔ *-tn- در اوستایی به -θn- و در پارسی باستان به -šn- بدل می‌شود (نگ: خانهٔ ۵). بارتولومه در ستون ۱۹۳ آن را تنها در صورتِ دوگانهٔ arəθnā از فرهنگ اویم می‌آورد و معنای آن را «آرنج» می‌دهد؛ پس افزودنِ «بازو» در نمودار کمی فراخ‌تر از منابع است. والده–پوکورنی (ج۱ ص ۷۰) صریحاً می‌گوید این واژه‌ها را باید در خانوادهٔ ὠλένη نگاه داشت. ادعای نورایی درست است.\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\"ref\": \"POK:308\", \"status\": \"supports\", \"note\": \"Pokorny el-8 (pp.307-309): 'simple root *ōle- in Old Indic aratní-ḥ m. ‚elbow‘, Avestan araθna- ds., fra-raθni- ‚ulna, ell‘, Old pers. arašniš ds.'\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"col. 193 (BRT.txt line 5498)\", \"stance\": \"supports\", \"note\": \"'j. arəθna- m. ‚Ellenbogen‘: -ənā (ND.) F.īŌ. — Vgl. frāraθni-. — np. araš (aus *arašn°); vgl. ai. aratni- m.' — note that Bartholomae's New Persian continuant is araš, not ārenj (relevant to nodes #2-#3).\"},\n      {\"src\": \"SYN\", \"where\": \"Buck 4.32, p.238\", \"stance\": \"supports\", \"note\": \"in the word table 'Av. araθna-' stands opposite NE elbow, and the discussion files it under 'Derivs. of IE *el- ‚bend‘'.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. I 70 (WLD_Bd1_pages.txt line 6332)\", \"stance\": \"supports\", \"note\": \"'Dagegen bleiben trotz Persson Beitr. 634 f. besser bei der Sippe von ὠλένη die Worte ai. aratni-h ... av. arəθna- ‚Ellenbogen‘, frāraθni- ‚Elle‘.'\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Persian\", \"words\": \"âryšnug\", \"verdict\": \"plausible\",\n     \"derivation\": \"The printed page really does read 'âryšnug' in a box labelled Persian, but the form is Middle Persian, not New Persian: MacKenzie's Concise Pahlavi Dictionary p.12 has 'ārešn [ʾplynʹ | M ʾryn-, N (a)raš] cubit', i.e. Book Pahlavi ʾryn with Manichaean MP ʾryšn, and Nourai's -ug is the common Middle Persian adjectival/diminutive extension -ūg written ʾryšnwg. Two things about the arrow are not right. First, this word does not go back specifically to Avestan arəθna-: the -šn- shows it continues the Old Persian type arašni- of node #5, since Old Persian turns Proto-Iranian *-tn- into -šn- while Avestan gives -θn- (Kent, Old Persian p.33: 'the pIr. *aratn-, aratan- gave Av. dual arəθnā, but OP arašn- and (with extension of the š) arašan- ‚cubit‘'). Second, its New Persian outcome is ارش (araš) 'cubit' — Bartholomae col.193 'np. araš (aus *arašn°)', Wiktionary 'From Middle Persian ʾryn /ārešn/, from Old Persian arašni' — not آرنج. The node is therefore a real word correctly attached to the root, but hung from the wrong parent and given the wrong child.\",\n     \"derivation_fa\": \"آنچه در کتاب چاپ شده واقعاً «âryšnug» است، امّا این صورت فارسی نو نیست بلکه فارسی میانه است: مکنزی در ص ۱۲ «ārešn [ʾplyn] cubit» دارد و پسوندِ -ūg هم پسوندی معمول در فارسی میانه است؛ پس برچسبِ خانه باید «پهلوی» می‌بود. دو ایراد به پیکان‌ها وارد است: یکی آنکه شینِ این واژه نشان می‌دهد که از گونهٔ پارسی باستان arašni- (خانهٔ ۵) می‌آید نه از اوستایی arəθna-، زیرا *-tn- در پارسی باستان به -šn- و در اوستایی به -θn- بدل می‌شود (کنت، ص ۳۳)؛ دیگر آنکه بازماندهٔ فارسی نوی آن «ارش» است نه «آرنج» (بارتولومه ستون ۱۹۳: np. araš؛ ویکی‌واژه نیز همین). پس خودِ واژه درست است ولی جای آن در درخت نادرست است: با احتیاط پذیرفتنی است.\",\n     \"sources\": [W_ARAS],\n     \"ref_check\": [\n      {\"ref\": \"MPP:79\", \"status\": \"not_checked\", \"note\": \"MPP is not Henning's 'Mitteliranisch' as refs_online.json guesses: Nourai's Table IV no. 66 (PDF p. A-12) reads 'W. Henning, ‚A List of Middle-Persian and Parthian Words‘, BSOAS IX (1937-39) pp 79-92, University of London', so MPP:79 is simply the article's opening page, cited as a blanket reference. No copy of that BSOAS article is on disk — HENNING_selected_papers.txt contains neither the title nor any ʾryšn-form — and Mitteliranisch p.79 (MPP.txt leaf 65) is about the Sogdian-Syriac script and the oldest Judeo-Persian documents, nothing to do with elbows. Worth correcting in refs_online.json.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"p.12 (PHD.txt leaf 33)\", \"stance\": \"supports\", \"note\": \"MacKenzie: 'ārešn [ʾplynʹ | M ʾryn-, N (a)raš] cubit' — the word exists in Middle Persian with this shape, but as 'cubit' and with New Persian araš, not ārenj.\"},\n      {\"src\": \"KNT\", \"where\": \"p.33 and p.176 (KNT.txt lines 1118, 5049)\", \"stance\": \"partial\", \"note\": \"'thus the pIr. *aratn-, aratan- gave Av. dual arəθnā, but OP arašn- and (with extension of the š) arašan- ‚cubit‘, in inst. pl. arašaniš' — places the š-form on the Old Persian side, i.e. under node #5 rather than under the Avestan node.\"},\n      {\"src\": \"NYB\", \"where\": \"Part II Glossary\", \"stance\": \"silent\", \"note\": \"grep of NYB_vol2_glossary.txt for 'ārešn', 'arišn' and 'ʾryn' returns nothing; the word does not occur in Nyberg's texts.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Persian\", \"words\": \"ârenj\", \"verdict\": \"plausible\",\n     \"derivation\": \"آرنج (ārenj) 'elbow' and its variants آرن / آران / آرنگ are all genuine and all belong to this root, and Nourai's reference is exact: Borhān p.32 has three consecutive headwords — 'آرن: مخفف آرنج است که بندگاه ساعد و بازو باشد، و به عربی مرفق خوانند', 'آرنج: بر وزن نارنج، بندگاه ساعد و بازوست', 'آرنگ: ... بر وزن و معنی آرنج است'. The line of descent, though, runs through a different Middle Persian word from the one drawn: MacKenzie p.12 'āranj [ʾplnc | N ~] elbow', which Horn (no. 14, p.5) already gives — 'urēn ‚Elle‘, āreng, ārenj, phlv. āranj (PPGl) ... gr. ὠλένη; lat. ulna. Vergl. aw. raθni- in frāraθnidrājō; ai. aratni- ‚Elle‘'. MP āranj reflects Old Iranian *āraθni-ka-/*āranya- (Wiktionary makes Middle Persian ʾplnc a loan from Sogdian ʾʾrʾync /ārinǵ/, from Proto-Indo-Iranian *Haratníš), the -θni-ka > -nǵ palatalisation giving the New Persian -نج. So ārenj and ārešn/araš are two parallel suffixations of the same *aratni-, and the second cannot be the source of the first; Aryanpur (p.54, s.v. آرنج، آرنگ، آران) lays the family out with Av. araθna, OP arašniš, Phl. āranj, Gk. ōlenē, Lat. ulna, Goth. aleina, OE elnboga side by side, citing the same Borhān page 32. Word, root and reference right; immediate parent wrong.\",\n     \"derivation_fa\": \"«آرنج» و گونه‌های آن (آرن، آران، آرنگ) همگی واقعی‌اند و به همین ریشه می‌رسند، و ارجاعِ نورایی هم دقیق است: در برهان قاطع ص ۳۲ هر سه مدخل پشت سر هم آمده‌اند. امّا راهِ تحول از راهِ دیگری است: فارسی میانهٔ āranj [ʾplnc] (مکنزی ص ۱۲؛ هرن شمارهٔ ۱۴ ص ۵) که از ایرانی باستان *āraθni-ka- می‌آید و ویکی‌واژه آن را وام‌واژه‌ای از سغدی ārinǵ می‌داند؛ جیمِ پایانی حاصلِ کامی‌شدنِ *-θni-ka است. پس «آرنج» و «ارش» دو ساختِ موازی از *aratni-اند و یکی از دیگری نیامده است. آریان‌پور هم در ص ۵۴ همین خانواده را با ارجاع به همان صفحهٔ ۳۲ برهان می‌آورد. واژه و ریشه درست، پدرِ بلافصل نادرست.\",\n     \"sources\": [W_AR],\n     \"ref_check\": [\n      {\"ref\": \"BQT:32\", \"status\": \"supports\", \"note\": \"Borhān printed p.32 = BQT_v1_pages.txt leaf 242: 'آرن: بر وزن فارن. مخفف آرنج است که بندگاه ساعد و بازو باشد و بعربی مرفق خوانند' / 'آرنج: بر وزن نارنج. بندگاه ساعد و بازوست که عرب مرفق گوید' / 'آرنگ: با کاف فارسی، بر وزن و معنی آرنج است که مرفق باشد'. All three of the chart's extra forms are on that one page; only آران is absent (it is in Mo'in's Farhang).\"},\n      {\"ref\": \"MPP:79\", \"status\": \"not_checked\", \"note\": \"see node #2: MPP = Henning, 'A List of Middle-Persian and Parthian Words', BSOAS IX 79-92, not available on disk.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"HRN\", \"where\": \"no. 14, p.5 (HRN.txt line 606)\", \"stance\": \"supports\", \"note\": \"'14. urēn ‚Elle‘, āreng, ārenj, phlv. āranj (PPGl). oss. arm-arūn ‚Elle‘; šar. γōvn ‚Ellbogen‘; gr. ὠλένη; lat. ulna. Vergl. aw. raθni- in frāraθnidrājō; ai. aratni- ‚Elle‘.' Horn derives ārenj from Pahlavi āranj, not from ārešn.\"},\n      {\"src\": \"PHD\", \"where\": \"p.12\", \"stance\": \"supports\", \"note\": \"'āranj [ʾplnc | N ~] elbow' — the Middle Persian ancestor of آرنج, listed separately from ārešn 'cubit' on the same page.\"},\n      {\"src\": \"ARY\", \"where\": \"p.54 (ARY_pages.txt, [pdf page 53]), s.v. آرنج، آرنگ، آران\", \"stance\": \"supports\", \"note\": \"Aryanpur's entry lists Avestan ARAΘNA, Old Persian ARAŠNIŠ, Pahlavi ARANJ, Greek ὠλένη, Latin ULNA, Gothic ALEINA, Old English ELNBOGA and English ELBOW, and cites 'برهان قاطع: ۳۲' — the same page Nourai gives.\"},\n      {\"src\": \"MON\", \"where\": \"Farhang-e Farsi s.v. آرنج (MON_part1.txt line 2739)\", \"stance\": \"supports\", \"note\": \"'آرنج: āranj [= آران، آرن، آرنگ] (ا.) بندگاه میان ساعد و بازو از طرف بیرون، مرفق' — confirms the fourth variant آران that Borhān lacks.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"Avestan\", \"words\": \"frâ-râthni\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Avestan *frā-rāθni- n., the preverb frā- 'forward' (Nourai's cross-reference '☞ Per 1' points at his entry for that preverb) plus the lengthened-grade *rāθni- of node #1. It is a unit of length, and Bartholomae accordingly glosses it 'Elle' (ell, cubit), defining it in the footnote as 'das Mass vom Ellenbogen bis zu den Fingerspitzen, doppelt so lang als ein vitastay-, halb so lang als ein frabāzav-'; the form is attested in the compound frā-rāθni-drājah- 'the length of a frārāθni' in Videvdad 7.30, 33. Nourai's gloss 'forearm' is the etymological rather than the lexical sense — the measure is the forearm — so it is a permissible shorthand, though Pokorny, Buck and Bartholomae all say 'ell'. Bartholomae adds that Middle Persian frārāst is 'eine Verunstaltung des Aw.-Worts', a garbled borrowing.\",\n     \"derivation_fa\": \"اوستایی *frā-rāθni- از پیشوند frā- «پیش، جلو» و همان *rāθni-ی خانهٔ یکم (با درجهٔ کشیده) ساخته شده و واحدِ طول است. بارتولومه آن را «ذراع» معنا می‌کند و در حاشیه می‌نویسد «اندازهٔ از آرنج تا نوک انگشتان، دو برابرِ vitastay- و نیمِ frabāzav-»؛ گواهِ آن ترکیبِ frā-rāθni-drājah- در وندیداد ۷٫۳۰ است. پس معنای «ساعد» در نمودار معنای ریشه‌شناختی است نه معنای واژگانی، و در کل ادعای نورایی درست است.\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\"ref\": \"POK:308\", \"status\": \"supports\", \"note\": \"Pokorny el-8: 'Avestan araθna- ds., fra-raθni- ‚ulna, ell‘' — the form appears on the very page Nourai cites.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"col. ~1016-1017 (BRT.txt lines 18269-18270)\", \"stance\": \"supports\", \"note\": \"'*frā-rāθnay- n. ‚Elle‘; s. dazu ai. aratnay- ‚Ellenbogen, Elle‘ ...; s. auch arəθna-; mp. frārāst ist eine Verunstaltung des Aw.-Worts', with the preceding entry 'frā-rāθni-drājah- n. ‚Länge eines Fr. (Elle)‘ ... V. 7.30, 33' and the footnote 'D. i. das Mass vom Ellenbogen bis zu den Fingerspitzen'.\"},\n      {\"src\": \"SYN\", \"where\": \"Buck 4.32, p.238\", \"stance\": \"supports\", \"note\": \"'Skt. aratni-, Av. araθna- ‚elbow‘ (Av. fraraθni- ‚ell‘)' — Buck too glosses it 'ell', not 'forearm'.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. I 70\", \"stance\": \"supports\", \"note\": \"'av. arəθna- ‚Ellenbogen‘, frārāθni- ‚Elle‘' listed together under the ὠλένη family.\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"Old Persian\", \"words\": \"arašni\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Old Persian *arašni- / arašan- 'cubit', the Persian-dialect match of Avestan arəθna-: Proto-Iranian *aratn- gives Old Persian -šn- where Avestan gives -θn-. It is attested only in the instrumental plural arašaniš, twice in Darius' foundation charter from Susa (DSf 26), measuring the depth of the packed rubble — 'some 40 cubits in depth, another (part) 20 cubits in depth'. Kent's lexicon (p.176) enters it as 'arašan- sb. ‚cubit‘ ... Av. nom. dual arəšnā, to Iran. stem aratan-, cf. Skt. aratní-', and notes the word was borrowed into Slavic as aršin 'ell'. Nourai's citation form arašni follows Pokorny's 'Old pers. arašniš'; his gloss 'elbow' is the etymological sense, the attested one being the measure. This node, not node #1, is the true parent of node #2.\",\n     \"derivation_fa\": \"پارسی باستان *arašni- / arašan- «ذراع» همتای پارسیِ اوستایی arəθna- است؛ خوشهٔ ایرانی باستان *-tn- در پارسی باستان به -šn- بدل می‌شود. تنها گواهِ آن صورتِ بایی جمعِ arašaniš در سنگ‌نبشتهٔ داریوش در شوش (DSf ۲۶) است که ژرفای پی را «چهل ذراع» و «بیست ذراع» می‌سنجد. کنت (ص ۱۷۶) آن را با همان ریشه می‌آورد و می‌افزاید که از ایرانی به اسلاوی به صورت aršin وام رفته است. صورتِ arašni در نمودار از پوکورنی گرفته شده و درست است؛ و همین خانه است که باید پدرِ خانهٔ ۲ می‌بود.\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\"ref\": \"MPP:79\", \"status\": \"not_checked\", \"note\": \"Henning's BSOAS word list (pp.79-92) is a Middle Persian and Parthian list and would not in any case cover an Old Persian form; no copy on disk. Pokorny 308, cited on the sibling nodes, has 'Old pers. arašniš' and is Nourai's real warrant here.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KNT\", \"where\": \"Lexicon p.176 (KNT.txt line 5049)\", \"stance\": \"supports\", \"note\": \"'arašan- sb. ‚cubit‘ (§32, §82, §155.I D): Av. nom. dual arəšnā, to Iran. stem aratan-, cf. Skt. aratní-; ... (borrowed from Iran. into General Slavic as aršin ‚ell‘) ... arašaniš ipm. DSf 26 bis'.\"},\n      {\"src\": \"POK\", \"where\": \"p.308\", \"stance\": \"supports\", \"note\": \"'Old pers. arašniš ds.' immediately after the Avestan forms — Nourai's spelling.\"},\n      {\"src\": \"BRT\", \"where\": \"col. 193 s.v. arəθna-\", \"stance\": \"partial\", \"note\": \"Bartholomae gives the New Persian outcome of this š-form as 'np. araš (aus *arašn°)', which is why آرنج cannot belong on this branch.\"}\n     ]\n    },\n    {\n     \"id\": 6, \"lang\": \"Germanic\", \"words\": \"alino\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Proto-Germanic *alinō f. 'forearm, ell' from PIE *Heh₃l-én-eh₂ (the *olīnā of Klein and Pokorny), whence Gothic aleina, Old English eln, Old High German elina, Old Norse ǫln, German Elle. Watkins's appendix has it verbatim: 'el-1. Elbow, forearm. Extended o-grade form *olinā, elbow, in: a. Germanic *alinā in Old English eln, forearm, cubit: ELL; b. Germanic compound *alino-bugôn-, ‚bend of the forearm‘, elbow ... in Old English elnboga: ELBOW'. Nourai's spelling 'alino' is Watkins's compound-form stem, and his gloss 'forearm' is the source's own.\",\n     \"derivation_fa\": \"ژرمنی آغازین *alinō «ساعد، ذراع» از هندواروپایی آغازین *Heh₃l-én-eh₂ (همان *olīnāی پوکورنی و کلاین) است که گوتی aleina، انگلیسی کهن eln، آلمانی کهن elina و آلمانی Elle از آن برخاسته‌اند. واتکینز زیر el-1 دقیقاً همین صورتِ alinō را در ترکیب *alino-bugôn- «خمِ ساعد» می‌آورد که منشأ elbow است. ادعای نورایی درست است.\",\n     \"sources\": [W_ALIN, E_ELB],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. el-1 (AHD_watkins1985.txt line 434): 'el-1. Elbow, forearm. Extended o-grade form *olinā, elbow, in: a. Germanic *alinā in Old English eln, forearm, cubit: ELL; b. Germanic compound *alino-bugôn-, ‚bend of the forearm‘, elbow ..., in Old English elnboga, elbow: ELBOW; c. Latin ulna: ULNA; d. lengthened variant form *ōlenā in Greek ōlenē: OLECRANON. [Pok. 8. el- 307.]'\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"p.509 s.v. ell\", \"stance\": \"supports\", \"note\": \"'OS., OHG. elina, ON. ǫln, Du. el, elle, MHG. elene, ele, G. Elle, Goth. aleina, fr. I.-E. base *olena'.\"},\n      {\"src\": \"SYN\", \"where\": \"Buck 4.32, p.238\", \"stance\": \"supports\", \"note\": \"'Goth. aleina, ON ǫln, eln, OE eln, OHG elina ‚ell‘, in cpds. for ‚elbow‘, ON ǫlnbogi, Dan. albue, OSw. alboghi ... OE elnboga, ME elbowe, NE elbow'.\"},\n      {\"src\": \"IEC\", \"where\": \"Mann ~p.942 s.v. olénā\", \"stance\": \"supports\", \"note\": \"'Go. aleina, f. ‚ell‘: OHG elina, f. ‚elbow‘; OFris. elne, OE eln ‚forearm; ell‘ ... ON alin, ǫln'.\"}\n     ]\n    },\n    {\n     \"id\": 7, \"lang\": \"English\", \"words\": \"elbow\", \"verdict\": \"confirmed\",\n     \"derivation\": \"English elbow < Middle English elbowe (c.1200) < Old English elnboga, a compound of eln 'forearm, ell' (node #6) and boga 'bow, bend' (Proto-Germanic *bugôn-, from PIE *bʰewgʰ- 'to bend'), so literally 'the bend of the forearm'; the -n- of eln- was lost by assimilation to the following b. The same compound recurs across Germanic — Middle Dutch ellenboghe, Dutch elleboog, Old High German elinbogo, German Ellenbogen, Old Norse ǫlnbogi — which shows it is inherited, not an English innovation. Skeat p.134 and Klein p.509 (s.v. ell, 'Cp. elbow') both give the same analysis.\",\n     \"derivation_fa\": \"انگلیسی elbow از انگلیسی میانه elbowe (حدود ۱۲۰۰ م.) و انگلیسی کهن elnboga است، ترکیبی از eln «ساعد، ذراع» (خانهٔ ۶) و boga «کمان، خم» (از ریشهٔ *bʰewgʰ- «خم کردن»)، یعنی «خمِ ساعد»؛ نونِ eln- در همگونی با b افتاده است. همین ترکیب در هلندی elleboog، آلمانی Ellenbogen و نوروژی کهن ǫlnbogi دیده می‌شود؛ پس میراثی است نه ساختهٔ انگلیسی. ادعای نورایی درست است.\",\n     \"sources\": [E_ELB],\n     \"ref_check\": [\n      {\"ref\": \"(none)\", \"status\": \"not_checked\", \"note\": \"the box carries no reference in the printed book; the parent Germanic box cites AHD, whose el-1 entry names ELBOW as the outcome of *alino-bugôn-.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"SKT\", \"where\": \"p.134 s.v. Elbow\", \"stance\": \"supports\", \"note\": \"'Elbow, the bend of the arm. (E.) M.E. elbowe, A.S. elboga. — A.S. el-, signifying ‚elbow‘, and boga, a bow, a bending (see Bow). A.S. eln allied to Goth. aleina, a cubit, L. ulna, Gk. ὠλένη.'\"},\n      {\"src\": \"KLN\", \"where\": \"p.509 s.v. ell\", \"stance\": \"supports\", \"note\": \"ends 'Cp. elbow. Cp. also alnage, ulna and the first element in linchpin', i.e. Klein files elbow with the *olena family on the page Nourai cites.\"},\n      {\"src\": \"SYN\", \"where\": \"Buck 4.32, p.238\", \"stance\": \"supports\", \"note\": \"'OE elnboga, ME elbowe, NE elbow ... with final member: ON bogi, etc. ‚bend, bow‘'.\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-152.json','w',encoding='utf-8') as f:\n    json.dump(doc, f, ensure_ascii=False, indent=2)\n    f.write('\\n')\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build152.py",
 "description": "Write page-152.json"
}
```


### [2026-09-05T20:51:09.946Z] TOOL RESULT

```
written
```


## [2026-09-05T20:51:14.204Z] TOOL CALL #72: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-152.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 152",
 "description": "Validate and run verify_check"
}
```


### [2026-09-05T20:51:52.486Z] TOOL RESULT

```
JSON OK
nodes verified: 14/14
node verdicts: {'confirmed': 9, 'disputed': 1, 'plausible': 4}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 10, 'partial': 1, 'not_checked': 5}
books consulted: {'supports': 25, 'silent': 6, 'partial': 7} | by book: {'SYN': 6, 'SKT': 5, 'BRT': 4, 'WLD': 4, 'PHD': 4, 'KLN': 3, 'NYB': 2, 'HRN': 2, 'ARY': 2, 'POK': 2, 'KNT': 2, 'MON': 1, 'IEC': 1}
```


## [2026-09-05T20:52:15.125Z] AGENT

Done. `data/verification/page-152.json` written; `verify_check.py 152` reports 14/14 nodes, 0 PROBLEM lines.

**Page 152 (book p.122) — 2 chart entries, 5 redirects skipped**

Verdicts: roots 2 confirmed. Nodes: 9 confirmed, 4 plausible, 1 disputed. Ref checks: 10 supports, 1 partial, 5 not_checked. 13 different books consulted (25 supports / 7 partial / 6 silent).

- **disputed** — El 2, #3 Persian آل / آلگونه: MP *arus* "white" cannot give NP *āl* by any Persian sound law; modern accounts (Benveniste's *āl-gōnak* ~ Ctesias' Ἀλογούνη; Bailey *āla-* + *harda-*; Hinz PIr *Hṛda- < PIE *h₁rewdʰ- "red") all reject the *auruša-* source. Nourai is faithfully repeating Mo'in's 1963 Borhān footnote (p.55), which does say exactly what he draws.
- **plausible** — El 3, #2 *âryšnug*: real word but Middle Persian (MacKenzie p.12 *ārešn* "cubit"), mislabelled "Persian"; its -šn- shows it continues OP *arašni-* (node #5), not Av. *arəθna-*, and its NP outcome is ارش *araš*, not آرنج.
- **plausible** — El 3, #3 *ârenj*: word, root and BQT:32 reference all correct (Borhān p.32 has آرن/آرنج/آرنگ consecutively), but its parent is MP *āranj* [ʾlnc] (Horn no.14, MacKenzie p.12; Wiktionary: a Sogdian loan *ārinǰ*), a sibling of *ārešn*, not its descendant.
- **plausible ×2** — El 2, #6/#7 Germanic *lambiz* → lamb: Klein p.860 and WP I 154 do derive it from *el-* "brown", but Buck 3.29 calls the root connection "dub." and Etymonline says Gmc *lambaz has no certain cognates outside Germanic.

No extraction errors: the 600-dpi render of the printed page matches the JSON exactly (including "âryšnug" and the آل ۱ / آله ، آلک ، آلا extras), so nothing for the owner to fix in `data/extracted/batch/page-152.json`.

Two data-hygiene findings for the reference library:
- `refs_online.json` misidentifies **MPP**. Nourai's Table IV no. 66 (PDF p. A-12) reads: W. Henning, "A List of Middle-Persian and Parthian Words", *BSOAS* IX (1937-39), pp. 79-92 — not "Mitteliranisch". So every `MPP:79` is just the article's opening page, and Mitteliranisch p.79 (about Sogdian-Syriac script) is a false lead. That article is not on disk. This also explains the same dead end hit on page 95.
- The **KLN** leaf→page formula in `refs_online.json` is off by ~20 pages in this range; the OCR carries real printed page markers (e.g. "508" / "510" bracketing *elk* and *ell*), and by those Nourai's KLN:509 and KLN:860 are both exact. Locating by marker rather than by the leaf formula is the reliable method.
