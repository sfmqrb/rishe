# Verification process log — verify-page-127


## [2026-09-05T18:29:06.660Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 127 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-127.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-127.json. Write /home/sfmqrb/git/rishe/data/verification/page-127.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 127` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T18:29:08.262Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T18:29:08.970Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T18:29:08.988Z] TOOL RESULT

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


## [2026-09-05T18:29:09.110Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-127.txt"
}
```


### [2026-09-05T18:29:09.132Z] TOOL RESULT

```
1	=== PDF page 127 (book page 97) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Dhem : to make vapor, raise dust  (refs POK:247)
4	#1 (parent #0) [Avestan] refs=POK:247 | dam : to blow, breathe ; da-dhmainya : I inflate, breathe
5	  #2 (parent #1) [Persian] refs=POK:247; BQT:876,877; HRN:127 | dam «دَم» : breath, air, vapor, weather ; damîdan «دمیدن» : to blow, breathe ; damâ «دما» : weather, heat ; Damâvand «دماوند» : a mountain (with vapor) | NOTE: BQT:878 derives "Damâvand" from the root "Dumb".
6	#3 (parent #0) [Germanic] refs=None | 
7	  #4 (parent #3) [English] refs=POK:248; KLN:399 | damp, dim
8	--- entry 1 ---
9	ROOT Dhe-mnâ -> redirect to Dhě 1
10	--- entry 2 ---
11	ROOT Dhě-mo -> redirect to Dhě 2
12	--- entry 3 ---
13	ROOT [Indo-European] Dhen, Dhont : to flow, run around  (refs POK:249)
14	#1 (parent #0) [Sanskrit] refs=POK:249 | dhan : to run
15	  #2 (parent #1) [Persian] refs=BQT:888; POK:249; HRN:128; FSF:88; MON:1562 | danîdan «دَنیدن» : to run joyfully ; dan «دَن» : joyful shouting ; danân «دَنان» : running, excited
16	#3 (parent #0) [Latin] refs=AHD | font : spring, fountain
17	  #4 (parent #3) [English] refs=None | fountain
18	
```


## [2026-09-05T18:29:13.050Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-127.json",
 "description": "Read page-127 source JSON"
}
```


### [2026-09-05T18:29:13.090Z] TOOL RESULT

```
{
  "pdf_page": 127,
  "book_page": 97,
  "entries": [
    {
      "root": {
        "name": "Dhem",
        "lang": "Indo-European",
        "refs": "POK:247",
        "gloss": "to make vapor, raise dust"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:247",
          "words": [
            {
              "translit": "dam",
              "gloss": "to blow, breathe",
              "script": null
            },
            {
              "translit": "da-dhmainya",
              "gloss": "I inflate, breathe",
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
          "refs": "POK:247; BQT:876,877; HRN:127",
          "words": [
            {
              "translit": "dam",
              "gloss": "breath, air, vapor, weather",
              "script": "دَم"
            },
            {
              "translit": "damîdan",
              "gloss": "to blow, breathe",
              "script": "دمیدن"
            },
            {
              "translit": "damâ",
              "gloss": "weather, heat",
              "script": "دما"
            },
            {
              "translit": "Damâvand",
              "gloss": "a mountain (with vapor)",
              "script": "دماوند"
            }
          ],
          "script_extra": null,
          "note": "BQT:878 derives \"Damâvand\" from the root \"Dumb\".",
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Germanic",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "English",
          "refs": "POK:248; KLN:399",
          "words": [
            {
              "translit": "damp, dim",
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
        "name": "Dhe-mnâ",
        "redirect": "Dhě 1"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Dhě-mo",
        "redirect": "Dhě 2"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Dhen, Dhont",
        "lang": "Indo-European",
        "refs": "POK:249",
        "gloss": "to flow, run around"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK:249",
          "words": [
            {
              "translit": "dhan",
              "gloss": "to run",
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
          "refs": "BQT:888; POK:249; HRN:128; FSF:88; MON:1562",
          "words": [
            {
              "translit": "danîdan",
              "gloss": "to run joyfully",
              "script": "دَنیدن"
            },
            {
              "translit": "dan",
              "gloss": "joyful shouting",
              "script": "دَن"
            },
            {
              "translit": "danân",
              "gloss": "running, excited",
              "script": "دَنان"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "پس اندر سپاه منوچهر شاه - دمان و دنان برگرفتند راه",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {
              "translit": "font",
              "gloss": "spring, fountain",
              "script": null
            }
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
            {
              "translit": "fountain",
              "gloss": null,
              "script": null
            }
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


## [2026-09-05T18:29:13.514Z] TOOL CALL #4: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo --- && cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "List verification dir and read source matrix"
}
```


### [2026-09-05T18:29:13.566Z] TOOL RESULT

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
page-126.json
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
page-44.json
page-45.json
page-46.json
page-47.json
page-48.json
page-49.json
page-50.json
page-51.json
page-52.json
page-53.json
page-54.json
page-55.json
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


## [2026-09-05T18:29:18.735Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','BQT','HRN','KLN','MON','FSF','AHD']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:900])\n    print()\n\"",
 "description": "Inspect refs_online entries"
}
```


## [2026-09-05T18:29:19.138Z] TOOL CALL #6: Bash

```json
{
 "command": "head -c 3000 data/verification/page-126.json",
 "description": "Sample previous verification file"
}
```


### [2026-09-05T18:29:20.907Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.c

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.", "notes": "OCR of German Fraktur-free text is decent; Persian

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based l

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different paginati

FSF {"title": "Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/1984", "kind": "archive_djvu", "url": "https://archive.org/details/20220809_20220809_1444", "lookup_hint": "grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushin book (گزارشی چند درباره شاهنامه).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF.txt"], "page_offset": "484 leaves; edition/printing of this scan not identified — determine offset from printed page numbers on the page text/image when checking", "covers_etymology": false, "notes": "Persian OCR fair (readable prose). Mostly glosses; some Pahlavi/Avestan notes. Edition may differ from the 1363 Dony

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt", "page_offset": "1985 Watkins ed.: lea
```


### [2026-09-05T18:29:20.940Z] TOOL RESULT

```
{
 "pdf_page": 126,
 "book_page": 96,
 "verified_by": "claude-fable-5-1",
 "verified_on": "2026-09-04",
 "entries": [
  {
   "entry": 0,
   "root": "Dheigh, Dhigha",
   "verdict": "confirmed",
   "modern_form": "PIE *dʰeyǵʰ- 'to knead, form, build (of clay)'; o-grade noun *dʰóyǵʰos 'something kneaded/formed' > 'wall; dough'",
   "note": "Pokorny IEW 244 dheiĝh- 'Lehm kneten und damit mauern oder bestreichen (Wand, Mauer; Töpferei); auch vom Teigkneten' is exactly Nourai's gloss; AHD dheigh- 'to form, build' cites 'Pokorny dheiĝh- 244'. Wiktionary (Rix LIV 140-141, Kroonen, de Vaan, Beekes) agrees. Nourai's second spelling 'Dhigha' is his rendering of the zero-grade/extended variant (Pokorny gives dheiĝh-, dhoiĝho-s, dhiĝh-lo-s). Two of his branches are weak: the OP 'daika > dīg' branch is rejected by modern Iranian etymology (see nodes 11-12), and the Sogdian, Persian dež and ferdows nodes are cognates/round-trip loans rather than lineal descendants of the parents drawn.",
   "note_fa": "ریشه همان *dʰeyǵʰ- هندواروپایی آغازین است به معنی «سرشتن گِل، ورز دادن و از آن دیوار ساختن»، و صورت اسمیِ درجهٔ o یعنی *dʰóyǵʰos «آنچه سرشته شده» که هم «دیوار» و هم «خمیر» از آن آمده است؛ پوکورنی (ص ۲۴۴) عیناً همین را می‌گوید و AHD نیز dheigh- «شکل دادن، ساختن» را با ارجاع به پوکورنی می‌آورد. نگارش دومِ نورایی، «Dhigha»، صورت درجه‌صفرِ همان ریشه است (پوکورنی: dhiĝh-lo-s). پس جعبهٔ ریشه و معنای آن درست است. اما دو شاخهٔ نمودار سست است: شاخهٔ «daika > دیگ» را ریشه‌شناسیِ ایرانیِ امروزی رد می‌کند (گره‌های ۱۱ و ۱۲) و آن را از *daiH- «تابیدن، سوختن» می‌گیرد؛ و گره‌های سغدی و «دژ» و «فردوس» هم‌ریشه یا وام‌واژهٔ رفت‌وبرگشتی‌اند نه فرزندِ مستقیمِ پدری که نمودار برایشان کشیده است.",
   "sources": [
    "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰeyǵʰ-",
    "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰóyǵʰos",
    "https://www.thefreedictionary.com/_/roots.aspx?type=Indo-European&root=dheigh-",
    "https://www.etymonline.com/word/*dheigh-",
    "https://starlingdb.org/cgi-bin/etymology.cgi?root=config&basename=%2Fdata%2Fie%2Fpokorny&text_recno=1208&single=1"
   ],
   "ref_check": [
    {
     "ref": "POK:244",
     "status": "supports",
     "note": "POK_01.txt leaves 255-256 (IEW pp. 244-245), s.v. dheiĝh-: 'Lehm kneten und damit mauern oder bestreichen (Mauer, Wall; Töpferei; dann auch von anderweitigem Bilden); auch vom Teig kneten (Bäckerei)'; dheiĝho-s, dhoiĝho-s 'Gebilde, Wall' ... 'ai. dēh
```


## [2026-09-05T18:29:26.099Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"dhem\" POK_01.txt | head -40",
 "description": "Grep Pokorny for dhem"
}
```


### [2026-09-05T18:29:26.153Z] TOOL RESULT

```
335:Lat.  aqua  .Wasser.  Wasserleitung'  (davon  aquilus  .dunkel',  aquila .Adler',  eigentl.  .der  Dunkelfarbige',  aquilö  .Nordwind',  eigentl.  .der  den Himmel  Verdunkelnde')  =  got.  a\va  f.  .Fluß.  Gewässer',  aisl.  o.  ags.  ca. as.  ahd.  aha,  nhd.  Ache  ds.  (germ.  *ahioö,  davon  abgeleitet  *ahioj5,  *aicjö .die  vom  Wasser  Umgebene'  in  aisl.  ey  f.  .Insel.  Aue',  ags.  ieg,  ahd. -ouwa,  -awa,  mhd.  ouwe  f.  .Wasser.  Halbinsel  im  Flusse,  wasserreiches Wiesenland',  nhd.  Aue,  vgl.  afries.  ei-land  .Insel'.  Sca(n)din-avia  Kretsch- mer  Gl.  17,  148  ff.),  russ.  FIN  Oka,  pannon.  ON  Aquincum  .Ofen',  apul. FIN  Aquilö,  ven.  ON  Aquileia  (auch  in  Süddeutscliland);  mit  Ablaut (idg.  e)  dazu  aisl.  kgir  (*eKog)  .Gott  des  Meeres',  ags.  xg-iceard  .Wache' an  der  See',  eagor  .Meer.  Flut'  (der  Anlaut  nach  ea);  vielleicht  hierher ai.  kam  .Wasser',  dak.  PflanzenN  y,oaödi.ia'  Tcoraj-ioysiTcov  .Wassersiedler' (*kYia-dhemn),  poln.  (nordill.)  FIN  Kiua.
2888:vielleicht  alb.  dhemje  ,Raupe'  (kann  für  *dhemlie  stehen),  dhemize,  dhimize fleischmade'. *   WP.  I  790.
3383:Ai.  dhäman-  n.  , Satzung,  Gesetz,  Wohnstätte,  Schar  usw.*,  av.  däman- dqman-  n.  , Stätte,  Geschöpf,  gr.  dvä-9'rjf.ia  ,das  Aufgestellte,  Weihgeschenk' ini-d^Tj^a  ,das  Daraufgestellte  oder  -gesetzte:  Deckel;  Bildsäule  auf  einem Grabe',  &rj(.iü)v  m.  , Haufe';  sii^f^mv  ,wohl  in  Ordnung  haltend';  thrak Pflanzenname  7,oa-öd(,ia '  noTaiioysiTCüv  (Dioskor.)  aus  *kua-dhemn  , Wasser- siedlung', ON  Uscu-dama]  sekundär  (nach  -d-eaig)  gr.  d-€(.ia  n.  ,hinterleo-tes Geld,  aufgestellte  Behauptung,  Satz:  Stammform  (Gramm.)',  vgl.  auch  Inf d-efxsrai]  av.  dämi-  f.  , Schöpfung',  Adj.  (auch  fem.)  , schaffend,  Schöpfer'- gr.  ^£uig,  Gen.  ursprüngl.  M^iGTog  ,*die  fest  und  unverbrüchlich  stehende' als  Göttinname,  dann  , Recht,  Gesetz,  Sitte',  d^e^is-d-Xa  PL  ,die  Grundlao-en eines  Gebäudes;  das  Tiefste,  Innerste',  d-ei.ieXioi  Xld-oi  ,die  Grundsteine' hom.  d^Bf-ieiXia  (ec  metr.  Dehnung)  , Grundlage,  Grund';
3404:dhebh-,  dbebh-eu-  ^beschädigen;  verkürzen,  betrügen',  die  nasalierten  Fori (*dhembh-)  sind  als  proportionale  Neubildungen  nach  -^i-haltigen  Wurzel zu  verstehen.
3513:dbem-,  dhemo-   ,stieben,  rauchen  (Rauch,  Dunst,  Nebel;  nebelgrau,  rauch-
3523:norw.  daam   {^dhemo-)    ^dunkel^^  'daame   m.  ^Wolkenschleier',    daant , Geschmack^  Geruch^  =  anord.  dämr  ^Geschmack^;
3532:(dhembb'),  dhmhh-  ,graben^;  nur  griech.  und  armen.
```


## [2026-09-05T18:29:26.930Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"dhen\" POK_01.txt | head -60",
 "description": "Grep Pokorny for dhen"
}
```


### [2026-09-05T18:29:26.981Z] TOOL RESULT

```
2882:Wegen  ai.  damya-  ,zu  zähmen'  und  ,juuger  Stier,  der  noch  gezähmt werden  soll'  und  wegen  gr.  da^ctXrig  einerseits  ,bezwingend,  bändigend' (^'Eqojg,  Anakreon),  andrerseits  ,junger  (noch  zu  zähmender)  Stier*,  avozu daf-idlr]  ,junge  Kuh',  ödixaXiq  ,ds.*;  auch  ,junges  Mädchen*,  dd^aXog  ,Kalb', ist  wohl  alb.  dente,  dhente,  ^q^.  dhent  , Kleinvieh,  Schafe'  {*dem-tä  oder *dem-to-Sj  bzw.-  *dom-tä,  -tos),  dem  ,Rind,  junger  Stier'  (=  ai.  damya-\ sowie  auch  gall.  GN  Damona  f.  und  air.  dam  , Ochse'  (*damos),  dam allaid  , Hirsch'  (,*wilder  Ochse'),  sowie  cymr.  dafad^  a.C0Tn.  dauat,  bret. daTwat  , Schaf  (dann  =  gr.  ä-dd^aTog)  anzureihen  (ursprgl.  Bezeichnungen gezähmter  Horntiere);  lat.  damma  oder  däma  ist  wohl  aus  dem  Kelt.  oder anderswoher  entlehnt;  unklar  ist  ags.  da  f.  ,Reh'  (daraus  acorn.  da  ,dama'), engl,  doe,  alem.  te  ds.,  vgl.  Holthausen  Altengl.  etym.  Wb.  68;  aus  afrz, daim  , Damhirsch'  stammt  bret.  devi  ds.;  germ.  Lehnformen  s.  bei  Falk- Torp  u.  daadyr  m.  Lit.;  entsprechend  niederösterr.  zamer,  zamerl  ,junger Ochs'  (Much  ZfdA.  42,  167;  vorgerm.  *a  oder  *o?).
2914:Über  alb.  dent  , mache  dicht^,  usw.  s.  unter  3.  dhen-.
3222:Ai.  däna-  n.  ,Geschenk^  (substantiviertes  -720-Partiz.)  =  lat.  dönum,  osk. usw.  dumim  ds.  (dtiunated  jdönRvit') ;  cymr.  daicn  ds.,  air.  dän  m.  ,donum, ars,  ingenium  (Begabung)',  vgl.  slav.  *dam-ki  in  serb.  ddnak  , Abgabe, Steuer^  usw.  und  den  -m-St.  aksl.  danh  , Abgabe,  ZolF,  lit.  duönis  ,Gabe^; schwachstufig  alb.  dhene  ,gegeben^,  f.  ,Gabe,  Abgabe^,  geg.  dhdne]
3421:äbS(i)'  (daneben  dh-ei-  ?)  .saugen,  säugen'  ( :  c?Äai-.  dJvt-  und  dhe-j  dhd-)  s. bes.  Schulze  KZ.  27.  425  =  Kl.  Sehr.  363.  Nominalbildungen:  dhe-lä .Mutterbrust',  dhi-lo-  , Zitze',  dbe-lu-  .säugend'.  dbQi-l-  ds.,  dhei-nä .trächtig',  dhe-nä  .Fruchtertrag',  dhedhn-  .(saure)  Milch'. Ai.  dhäya-h  .ernährend,  pflegend',  dhäyas-  n.  .das  Saugen',  dhäyü-  .durstig'. dhätave    .zu    saugen',    Fut.  dhäsyati,    i^or.    ddhät   ,er    sog',    su-dhä    .Saft, Nektar',  dhätrl  .x4mme.  Mutter',  dhenü-  f.  .milchend'  =  av.  daenu-  .Weib- chen von  vierfüßigen  Tieren',  ai.  dJiBnä  .Milchkuh',  ablaut.  dhud-  .gesogen*^, Perf.  Plur.  1.  3.  da-dhi-md  (i  =  »),    da-dh-üh]   redupl.   Nomen    da-dh-an-j Nom.  dd-dh-ij  Gen.  dadhnds  .saure  Milch'  (:  apr.  dadaUj  alb.  djathej'j
3430:lett.  deju,  det  ,saugen',  at-diene,  at-diemte  ,eine  Kuh,  welche  im  zweite] Jahr  kalbt',  lit.  dieni  f.  ,trächtig'  (=  ai.  dhenü-),  dienä  ds.  (=  ai.  dhenä  ,Kuh*3 apr.  dadan  , Milch'  (=  ai.  dadJian-)]  aksl.  dojg  ,säuge'  (ai.  dhdyati),  doilicQ ,Amme',  mit  e  (=  idg.  e  oder  9i)  däth  f.  ,Kinder',  deva,  devica  ,Määchen Jungfrau'  (verschoben   aus   ,*Weib'  =  ,die  säugende',    s.  Berneker  197);
3469:„      ,.     -^  for-ding  ^unterdrückt^,  s.  unter  1.  dhengh- , drücken,  bedecken^  usw.;
3515:dbenguo-,  dhengui-  ,neblig^
3524:mit  Gutt.-Erw.:  dhenguo-,  dhengui-  ,neblig^  in  anord.  dqkk  f.  ^VerS fnng  in  der  Landschaft^  =  lett.  danga  (*dhongua)  _,kotige  Pfütze^  niorastic Land^  Meeresschlamm^,  ferner  anord.  dekhr,  afries.  diunk  ,dunkeF  (gen *denkva-)',  tiefstufig  as.  dunkar^  ahd.  tunkal,  nhd.  dunkel  (ursprüngl.  und der  Bed.  _,neblig" —  feucht^  norw.  und  schwed.  mdartl.  dünken , feucht,  dumpf schwüF^  engl,  dank,  mdartl.  dtonk  ^feucht');  dazu  cymr.  deio  m.  (*dhen(n't( ,Nebel,  Rauch^  Schwüle^  usw.^  deweint  ,Dunkelheit^  (irrig  Loth  RC  42  ^ 43,  398  f.),  hitt.  da-an-ku-i-is  (dankuis)  ^finster,  schwarz^  (Benveniste  BSl 33,  142);
3542:2.  dben-  ,Fläche   der  Hand,  des    Erdbodens,   flaches   Brett',   dhenr  ,flache
3554:alb.  g-dhent  ,behaue  Holz,  hoble,  prügle^,  ge^^.  dliend,  dhenn   ,baue schneide'.
3558:1.  dhengh'  ,d rücken,  krümmen,  bedecken,  ^vorauf  liegen'.
3563:2.  dhengh'  ,ei-reichen,  fest  zugreifen,  fest,  kräftig,  schnell'.
```


## [2026-09-05T18:29:31.236Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3505,3560p' POK_01.txt",
 "description": "Print Pokorny dhem- context"
}
```


### [2026-09-05T18:29:31.281Z] TOOL RESULT

```
Air.  delg  n.  (es-St.)  ^Dorri;  Tuchnadel^;  com.  delc  (d.  i.  deich)  ,moiiile^; nicyiin'-  dala^  dal  .Biß,  Sticli^;
aiiord.  dälkr  ^Nadel,  um  den  Mantel  über  der  rechten  Achsel  zu  be- festigen; Spina  dorsalis  pisciura;  Dolch^  Messer^,  ags.  dalc  m.  ,Spange^  (nhd. Dolch,  älter  Tolch,  ndd.  dolk,  nach  Mikkola  BB.  25^  74  die  Quelle  von cech.  poln.  ^rt^ic/i,  sloven.  tolih,  ist  zwar  zunächst  aus  lat.  dolö  ,Stock- Jc^^en^  entlehnt,  aber  vielleicht  nach  einem  ^erm.  Worte  wie  ags.  dalc umgebildet);
lit.  dilgüs  ^stechend,  brennend'^,  dllge^  dilgele  f.  ^Nessel^,  dilgstu^  dMgti von  Nesseln  verbrannt  werden*^;   dalgis  ^Sense*^   hierher,   nicht  zu  S.  196!
Hierher  vielleicht  lat.  falx  , Sichel,  Sense,  Gartenmesser',  nach  Nieder- uiann  Essais  17  ff.  rückläufige  Ableitung  aus  falcida,  das  er  aus  einem Ijo-ur.  (?)  *dalkla  {*dhal-tla)  ableitet,  ebenso  wie  sizil.  ZayxAiy,  Jav^Xs Messina^  (:  dgsrvavov).  Man  kann  aber  ebensogut  von  *dhalg-tlä  ausgehen; wenn  in  jenem  ital.  Dialekt  idg.  l  zu  al  geworden  wäre,  ließe  sich  auch der  a -Vokal  erklären.  Spätlat.  daculum  , Sichel^  könnte  die  ligur.  Ent- sprechung dazu  sein.    Dagegen  Terracini  Arch.  Glott.  Ital.  20,  5  f.,  30 f.
WP.  I  865  f.
dbelgh-,  dhelg'(?)  ,schlageii' ?  ?
Ags.  dolg  n.,  alid.  tolc,  tolg,  dolg  n.  _,Wunde^  (;*Schlag^),  anord.  dolg  n. ,Feindschaft^_,  dolgr  ,Feind^,  dylgja  ^Feindschaft^,  wozu  wohl  ndd.  dalgen, daljen  jSchlaLgen^  (entlehnt  norw.  mdartl.  dalga  ds.),  nhd.  (hess.-nassauisch, ostpreuß.)  dalgen,  talken  ,prügeln,  schlagen'^,  mhd.  talgen  ,kneten^  Nach Havers  KZ.  43,  231,  IF.  28,  190  ff.  wäre  auch  für  gr.  Mlyw  ,bezauhere, betöre  usw.^,  d-shATcog,  d^el'ArrJQy  -d-eXycTi^Qiog  ,bezaubernd,  verlockend^,  d^eX^ig .  ,Bezauberung^  (idg.  *dhelg-  neben  *dhelgh-?)  die  Grundbed.  ,Bezauberung durch  Schlagt  wahrscheinlich,  so  wie  auch  die  TeXxlveg,  OsXytveg  durch einen  Schlag  die  Gesundheit  der  Menschen  schädigende  Dämonen  und zugleich  Schmiede  waren.  Alles  ganz  unsicher.  Eher  könnte  noch  toch.  A talke  n.,  B  telki  ,Opfer^  dazugehören.
WP.  I  866.
dbem-,  dhemo-   ,stieben,  rauchen  (Rauch,  Dunst,  Nebel;  nebelgrau,  rauch-
farben    ==    düster,    dunkel),    wehen,    blasen    (hauchen    =    riechen)^;
dbenguo-,  dhengui-  ,neblig^
Ai.    dhdmati    ,bläst^    {dhami-syatl,   -td-    und    dhmätd-,    Pass.    dhamyatü
und   dhmäydte)j  av.  daömainya-  ,sich   aufblasend,  blähend,  von  Fröschen^,
npers.    damldan    ,blasen,    wehen^,    dam   ,Atem,    Atemzug^,   osset.    dumun,
dimin  ,rauchen;  wehen,  blasen';
gv.  d-sfASQog  ,(jeuvög\  d-S(.i6Qü)7rtg  ,ernst,  finster  blickend'  (:  ahd.  timber  ,finster^) ;
248
mir.  dem  ^schwarz^  dunkel';
norw.  daam   {^dhemo-)    ^dunkel^^  'daame   m.  ^Wolkenschleier',    daant , Geschmack^  Geruch^  =  anord.  dämr  ^Geschmack^;
mit  Gutt.-Erw.:  dhenguo-,  dhengui-  ,neblig^  in  anord.  dqkk  f.  ^VerS fnng  in  der  Landschaft^  =  lett.  danga  (*dhongua)  _,kotige  Pfütze^  niorastic Land^  Meeresschlamm^,  ferner  anord.  dekhr,  afries.  diunk  ,dunkeF  (gen *denkva-)',  tiefstufig  as.  dunkar^  ahd.  tunkal,  nhd.  dunkel  (ursprüngl.  und der  Bed.  _,neblig" —  feucht^  norw.  und  schwed.  mdartl.  dünken , feucht,  dumpf schwüF^  engl,  dank,  mdartl.  dtonk  ^feucht');  dazu  cymr.  deio  m.  (*dhen(n't( ,Nebel,  Rauch^  Schwüle^  usw.^  deweint  ,Dunkelheit^  (irrig  Loth  RC  42  ^ 43,  398  f.),  hitt.  da-an-ku-i-is  (dankuis)  ^finster,  schwarz^  (Benveniste  BSl 33,  142);
anord.  dy  ^Schlamm,  Kot,  Morast^  aus  *dh7pkio-,  vgl.  mit  gramm.  Wec dän.  dyng  ,naß,  feucht^,  schwed.  mdartl.  düngen  ,feucht^;  '^^|
mit    germ.  -p-:    mhd.   dimpfen,    dampf  ,dampfen,   rauchen*^,   ahd.   mlidf dampf  m.  , Dampf,  Rauch^,  mnd.  engl,  damp  ,Dampf,  feuchter  NebeF,  ndd. dumpig  ,dumpf,  feucht,  moderig^  nhd.  dumpfig,  dumpf  (auch  =  verwirrt gestoben);    kaus.    ahd.   dempfen,    tempfen,    mhd.   dempfen    ,durch    Dampf ersticken,  dämpfen^;
mit  germ.  -h-:  schwed.  dial.  dimha  st.  V.  ,dampfen,  rauchen,  stieben* dimba  ,Dampf^,  norw.  damh  n.  ,Staub^,  anord.  dumba  ,Staub,  Staubwolke' (daneben  mit  -mm-  anord.  dimmr  ,dunkeU,  afries.  ags.  dimm  ds.,  norw. mdartl.  dimma,  dumma  ,Unklarheit  in  der  Luft,  Nebeldecke^,  schwed. dimma  ,dünner  NebelQ,  ahd.  timber,  mhd.  timher,  timmer  ,dunkel,  finster, schwarz^;
inwieweit  die  s-Formen  schwed.  mdartl.  stimma,  stimha  , dampfen^,  norw. mdartl.  stamma,  stamha  ,stinken^  einen  idg.  Hintergrund  haben  oder  nur nach  dem  Nebeneinander  von  ahd.  toum :  ags.  stEam,  dt.  toben :  stieben (s.  unter  dheu-,  dkeu-bh-  ,stieben^)  neugeschaffen  sind,  ist  fraglich;
lit.  dumiüj  dümti  ,blasen,  wehen'^,  apdümti  ,mit  Sand  oder  Schnee  be- tragen (vom  Wind)^,  dümples  ,Blasebalg^,  dümpiu,  dümpti  ,blase^  (wohl  mit p-Erw.),  apr.  dumsle  ,Harnblase^;
aksl.  dzm^j  dgti  ,blasen^  (zum  bsl.  Vokalismus  s.  Berneker  244  f.  m. Lit.,  Meillet  Slave  comm.^  63  f.,  164,  Trautmann  63).
WP.  I851f.
(dhembb'),  dhmhh-  ,graben^;  nur  griech.  und  armen.
Arm.  damban  ,Grab,  Gruft;  Grabmal,  dambaran  ds.; gr.  d^anio)  {*dhmbh-io),  Aor.  Pass.  hdcprp^  ,bestatte,   begrabe^,   Ud-aTtroq ,unbegraben^,  tdcpog  m.  ,Leichenbestattung,  Leichenfeier;  Grab,  Grabhügel';
249
tarn  ;Bestattun^,  Grab%  T&(pqog  {*dhmhh-ro-s)  f.  ^Graben':  aber  apr.  damho \.  f    Gruiid^  ist  in  danbo  (S.  268)  zu  bessern. '  Wp.  I  S52.
dbea-  ^laufen,  rennen;  fließend
Xi.  dhandyati  ^rennt,  läuft,  setzt  in  Bewegung^,  npers.  danidan  ,eilen, laufen^  ai.  dhdnvati}  ,vQniitj  läuft,  fließt',  apers.  danuvatiy  ,fließt',  ai. dhdnutar-  ,rennend,  fließend';
messap.  Flurname  ardannoa  {*ar-dJionu-ä)  ,die  am  AVasser  gelegene'  (?), apul.  ON  Ardaneae  ==  Herdonia  (Krabe  Gl.  17,  102);
lat.  wahrscheinlich  föns,  -tis  ,Quelle';  vielleicht  Kreuzung  des  ^o-St. *fontos  und  tiSt.  *fentis  (*dhn-t{-)]
toch.  AB  tsän  ^fließen',  B  tserie  ,flot',  tsnam  ,ecoulement'.
WP.  I  852,  Couvreur  BSL.  41,  165.
2.  dben-  ,Fläche   der  Hand,  des    Erdbodens,   flaches   Brett',   dhenr  ,flache
Bodensenkung'.
Ai.  dhdnus-  n.,  dhdnvan-  m.  n.  ,trockenes  Land,  Festland,  Strand,  dürres Land,  Wüste',  dhdnu-,  dhanü-  f.  ,Sandbank,  Gestade,  Insel' ;
gr.  d-evaQ  n.  ,Handfläche,  Fußsohle,  auch  von  der  Fläche  des  Meeres oder  von  der  Vertiefung  im  Altar  zur  Aufnahme  der  Opfergaben',  Ötzl- ad^evaq  , Handrücken'  {^önLGd-o&evaQ),  ahd.  tenar  m.,  tenra  f.  (*denara-), mhd.  teuer  m.  ,flache  Hand',  Curtius^  255  (samt  ai.  dhdnus-,  s.  u.).
Dazu  vlat.  danea  ,area'  (Reichenauer  GL),  ahd.  tenni  n.,  mhd.  tenne m.  f.  n.,  nhd.  Tenne  ,geebneter  Lehm-  oder  Bretterboden  als  Dreschplatz, '  Hausflur,  Boden,  Platz,  Fläche  überhaupt',  ndl.  denne  ,area,  pavimentum; tabulatum';  als  ,tennenartig  glatt  getretener  Ort  oder  Ort,  wo  das  Gras durch  Daraufliegen  niedergelegt  ist,  dadurch  entstandene  Vertiefung'  läßt sich  auch  verstehen  mecklenb.  denn  ,Lagerstätte,  niedergetretene  Stelle im  Korn',  mnd.  denne  ,Niederuug'  (und  ,Waldtal'  s.  u.),  mndl.  denne  ,Lager wilder  Tiere'  (und  ,Waldtal',  s.  u.),  dan  ,wüster,  von  Buschwerk  umgebener Platz,  Platz  überhaupt,  Land,  Landschaft;  Schlupfwinkel  des  Wildes'  (und ,Waldtal',  s.  u.),  ags.  denn  ,Höhle,  Wildlager',  nengl.  den  ,Höhle,  Grube', ofries.  dann{e)  ,Beet,  Gartenbeet,  Ackerbeet'.
Über  lit.  denls  m.  , Deckbrett  eines  Kahns',  lett.  denis  ds.  (germ.  Lw.?) s.  Trautraann  51,  Mühlenbach-Endzelin  I  455.
WP.  I  853.
3.  dben-  ,schlagen,  stoßen'.
Nur  in  Erweiterungen  (fast  ausschließlich  germ.):
c?-Erw.:  anord.  detta  st.  V.  ,schwer  und  hart  niederfallen,  aufschlagen' {*dintan.  vgl.   norw.   dial.  datta  [*dantö7i]  ,klopfen':   denta  ,kleine    Stöße
250
geben'),  ufries.  dintje  gleicht  schüttern^  norw.  deise  ^taumelnd  fallen,  gl^Jf (aus:)  ndd.  dei(n)sen  (*dantisöri)  ^zurücktaumeln,  auskneif en^;  ostfries. ,Fall^  (s  aus  -dt-  oder  -c?s-),  anord.  dyntr,  ags.  dynt  m.  (=  anord.  dyi engl,  dint  ,Schlag,  Stoß^;
alb.  g-dhent  ,behaue  Holz,  hoble,  prügle^,  ge^^.  dliend,  dhenn   ,baue schneide'.
Gutt.-Erw.:  anord.  danga  (*dangön)  ,prügeln':  aschwed.  diunga  st.  Y^ ,schlagen^,    mengl.    dingen    ,sclilagen,    stoßen^,    nengl.    ding    (skand.  L^^ mhd.  tingelen   ,klopfen,  hämmernv  norw.   dingle   (und    dangle)   ,bauinela« Kaus.  anord.  dengja,  ags.  dengan,  mhd.  tengen  {tengelen)  ,schlagen,  klopfea' hämmern  (nhd.  dengelnj]  ahd.  tangal  m.  ,Hammer^
Labial-Erw.:  schwed.  dimpa  {damjp)  ,schnell  und  schwer  fallen',  nj dumpen  ,schlagen,  stoßen',  engl.  dial.  dump  ,schwer  schlagen'.
WP.  I  853  f.
1.  dhengh'  ,d rücken,  krümmen,  bedecken,  ^vorauf  liegen'.
Air.  dingid,  for-ding  ,unterdrückt'  (s.  auch  dheigh-)'^  vgl.  Pedersen II  506;
lit.  dengiü,  dengti  ,decken',  dangä  , Decke',  dangia  ,Himrael',  dazu  difu ,versch winden'  (aus  ,*bedeckt  werden'),  slav.  '^d(^ga  ,Bogen'  (:  Yii.  danql in  russ.  dugd  , Bogen',  alt  ,Regenbogen',  bulg.  d^gdy  serb.  düga,  pol dial.  dega  ds.,  wohl  zu:
```


## [2026-09-05T18:29:53.899Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==148 || NR==149 || NR==150' HRN.txt | head -100",
 "description": "Print Horn pages 127-129"
}
```


### [2026-09-05T18:29:55.593Z] TOOL RESULT

```
— 126 -
504. duzd *Dieb', diizdl, dtizdlden.
g. diizadmün *stelilen*, duz 'Dieb'.
aw. duzdäo ^Bösewicht'; phlv. duz (geschrieben duc;
Kommentar für aw. täyu-), diizTh (Mön.), didd,
duzditan (geschrieben duct" ; AV.), duzdlha (geschrieben
duct"; PPGl.), dtizdU (geschrieben dfutU; Bund.), päz.
auch überall dMzd",
LW. (?) kurd. diz *Dieb', dizhi 'stehlen'; bei. duz,
diizl (88).
np. duzd stimmt lautlich ganz genau zu aw. duzddo
(zu z aus z vergl. np. miizd^ ^mizd 'Lohn gegen aw.
mizda- und zu dem Abfall der Endung np. Hor]muzd
gegen aw. Mazdäo). Im Fehle vT ist überall z zu lesen
bis auf die junge Form des Bundehes; duz^ duzJh sind
dann schon noch jüngere Formen.
505. duS', duS' {diz-, dez-) *übel, böse'; vergl. dust (Bahn.
I, 15 Vers 38).
ap. dus-; aw. dtis-, duz-; phlv. dws-; ai. dus-, rfwr-;
gr. Ovo-; arm. LW. dz-, echt ^ (H. No. 267).
Mit duZ'j dtiS' gebildete Composita, deren Zu-
sammensetzung vollständig durchsichtig ist, wie
duz/lm, dmnüm, dmmen sind im Folgenden nicht
aufgeführt.
560. deSe ^Siegel*.
aw. i^daJ/Z', dazaiti Verbrennen'; phlv. dazitan; ai.
[/dali- ddhatl 'brennen, verbrennen',
bei. n. diday, pp. da/fa 'brandmarken' (433).
507. dest 'ITand', vergl. destek^ deste (arab. dastaj ^)), destl
'Hilfe'.
ap. dasta- Hand'; aw. zasta-; phlv. dast; ai. hdsta-.
Allgemein entlehnt: kurd. dest; afy. las (Darmeste-
ter, LXIII, Npte) , dast; bei. dast (51); wa;^. ^ast,
siyn. döst, sar. düst, sangl. dast, minj. last, yidg. lust.
508. destur 'Minister, Vertrauter; Verhaltungsmassregel,
Vorschrift'.
') (^Iml.l. LW. pppi, arm. LW. (htsfnk.
- 127 -
ap. "^dastabara-; phlv. dastwar, dastbar.
Nicht zu dest *Hand\ sondern zu der in aw. dqsfva-
etc. steckenden Wurzel dmts- (Darmestetor, Et. ir.
I, 115 Note)'). Zu derselben Wurzel stellt Nöldeke
(mündliche Mitteilung) auch np. dästan-), destan *Go-
schichte, Erzählung .
5()9. duH^^är, duSvär 'schwierig*, dus/'ün, dusvan,
aw. vergl. duzadra- (Geldner, KZ. 25, 478, Studien
I, 17 folgg.); phlv. dus/J'är, dmx'arlh.
Die neup. phlv. Formen sind Neubildungen aus
dus+x"^'^ (No. 49G).
570. destän 'menstruirende Frau'.
aw. da/stavaitl-; phlv. dastän (arm. LW. dasfan;
chald. LW. ]P\'^'^)j dastan(i)stan^ vorgl. dayßak,
571. dil *Herz', diler (reimt auf ser, Sahn. I, 195, 1194).
aw. zered- (y. :n, 12), zaredaya- *lIorz*; phlv. dil,
päz. diler (Men.); ai. hfd-, hfdaya-; arm. sirf (IT.
No. 250).
kurd. zar 'Herz*; af/. zra; oss. d. zärdd^ t. z'ardä
(131); bei. ^^zVc/c (420); sar. zärd^ si;'n. -^^Il), <m//,
sangl. mrütj^ minj. 2?/.
np. rf// ist ausserdem in alle iranischen Sprachen
entlehnt, meist ohne einen Bedeutuugsunterschi(^d mit
dem betreffenden einheimischen Woite aufzuweisen
(Ausnahme: Tomaschek, S. 78()).
572. dem 'Atem, Atemzug', deine^ demulen 'wehen, blas(Mi\
demäy^ demär,
ai. V^dham-', dhdmiti 'hauchen, bhisen*; phlv. dam;
ksl. dümq, dqti 'blasen'.
< . •
') Bartholomae (BB. 15, 86) legt dieser Wurzel die Bedeutunjij
einweihen, weihen* bei. Dazu passen aber inoht die ebenfalls dazu
gehörigen ai. dasmä-^ dasrä-. Geldner übersetzt KZ. 30, 329 aw.
dldaihhe mit 'ich wurde unterwiesen*.
«j Anders Fr. Müller, WZKM. 5, 354. - Rückert hat
V ••
übrigens in seinen Bemerkungen zu MohTs Sähnäme-Ubersolzung
auch np. (h'sfür mit desf zu voroinigon versucht.
— 128 —
vergl. oss. d. dumun, t. dimin Vauchcn; wehen,
blasen (115)0.
Entlehnt kurd. dem, bei. dam (69).
57P». dum, dumb^), diimbe'^) 'Schwanz', dumhal).
aw. duma- 'Schwanz'; phlv. dutn^ dumb, dumhak,
arm. LW. dmak (= "^dumak).
kurd. düw, dunk; Sify. lam; oss. d. dumaij, t. diniag
(107); bei. (LW. ?) dunhag, n. di^/nJ, de^wfc (87), daneben
sicher echt d%m (briefl. Mitteilung von Dam es an
Geiger); sar. öihn, dümba, wsl/. diimbd (LW.).
Die arische Grundform muss ^dhumblmia- gelautet
haben (Bartholomae, Studien II, 101).
574. dendün 'Zahn*^), dendäne 'Mauerzinne'.
aw. vTmitö.lidanfa7i'; phlv. dandän (AV., Bund.);
ai. ddnta-,
kurd. didän *Zähne'; oss. t. dänddg 'Zahn* (104);
l)el. dantän, n. dafän^ d'anfän (70); minj. land, si/n.
dendäHj sar. dandän, wa/. dundäk.
Nach Joh. Schmidt' (zuletzt KZ. 32, 329) 'die
Esser.
V
571'"'' denuleii 'eilen, laufen, denän (Sahn. I, 121 Vers
1033, 198 Vers 1242).
```


## [2026-09-05T18:30:02.035Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==150 || NR==151' HRN.txt | sed -n '1,60p'",
 "description": "Print Horn page 128-129"
}
```


### [2026-09-05T18:30:03.930Z] TOOL RESULT

```
— 128 —
vergl. oss. d. dumun, t. dimin Vauchcn; wehen,
blasen (115)0.
Entlehnt kurd. dem, bei. dam (69).
57P». dum, dumb^), diimbe'^) 'Schwanz', dumhal).
aw. duma- 'Schwanz'; phlv. dutn^ dumb, dumhak,
arm. LW. dmak (= "^dumak).
kurd. düw, dunk; Sify. lam; oss. d. dumaij, t. diniag
(107); bei. (LW. ?) dunhag, n. di^/nJ, de^wfc (87), daneben
sicher echt d%m (briefl. Mitteilung von Dam es an
Geiger); sar. öihn, dümba, wsl/. diimbd (LW.).
Die arische Grundform muss ^dhumblmia- gelautet
haben (Bartholomae, Studien II, 101).
574. dendün 'Zahn*^), dendäne 'Mauerzinne'.
aw. vTmitö.lidanfa7i'; phlv. dandän (AV., Bund.);
ai. ddnta-,
kurd. didän *Zähne'; oss. t. dänddg 'Zahn* (104);
l)el. dantän, n. dafän^ d'anfän (70); minj. land, si/n.
dendäHj sar. dandän, wa/. dundäk.
Nach Joh. Schmidt' (zuletzt KZ. 32, 329) 'die
Esser.
V
571'"'' denuleii 'eilen, laufen, denän (Sahn. I, 121 Vers
1033, 198 Vers 1242).
ai. \/~dhan-^ dadhdnat 'laufen' (Hörn).
575. du^ do, dö^) zwei', duviim^ duyiim, duvem (AM.).
Käs. du, da.
ap. duoitlga- 'zweiter; aw. dva- 'zwei'; paz. dö,
kurd. du, du; afy. dva; oss. d. t. duvä (113); wa;^.
hüi, sar. däu, si/n. Jö, yaj'n. sangl. du, minj. do.
570. d'UVäxdeh 'zwölf, duvüzdehum.
aw. dvadasa, dvadasa-; phlv. duväcdahum^'); ai.
doädara, dvädard-.
»j Vielleicht auch zu np. dM *Rauch* (No. 579).
2) Auch dunh geschrieben.
') Geschrieben dunh".
*) Np. dend ist wohl nur eine repristinirte Form,
ö) So bei Firdüsi, z. B. Sahn. I, 127 Vers 1125, 189 Vers 1078
u. off.
^'j Wahrsolioinlioh ist wie in panedahum noch c zu lesen.
- 129 -
af/. dvalas; oss. d. duades, t. duädäs.
Die neupersische Form (eine Analogiebildung) ist
entlehnt in kurd. duänzdih (hier findet sich noch
ausserdem das n von np. sänzdeh), hol. duäzdeh,
oll. (\)dö%ten *anheften, durchbohren, nähen', Praes.
döz-em, döz, dözene, kun\döz grosse Nadel' (AM. 52
ZeUe 6, 116 Zeile 2 v. u.).
maz. düj, düjene,
phlv. döc *Speer (Dat. d. 21, 8), phlv. pjiz. dö/tav,
dözEm (PPGl.)
oss. än-düzün, d. än-dozun ^befestigen (von
Stackeiberg, ZDMG. 43, 671); bei. dööag , n.
dösay *nähen (91).
578. (2)döy(ten 'melken', Praes. dös^em, dösTden, döy saure
Milch' (AM. 216 Zeile 5) ').
ai. [/"döh-, dogdhi 'melken', dögha^; phlv. dö/fan
(Bund.), dösUan (Bund., PPGL).
kurd. dötifiy düsim, di-dösim melken'; afy. Ivasal;
oss. d. docufiy t. dücifi (111); bei. dösay (94); wa;^.
```


## [2026-09-05T18:30:14.375Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^\\[pdf page\" BQT_v2_pages.txt | head -5 && echo --- && grep -n \"۸۷۶\\|۸۷۷\\|۸۷۸\\|۸۸۸\" BQT_v2_pages.txt | head -20",
 "description": "Locate BQT v2 pages"
}
```


### [2026-09-05T18:30:14.436Z] TOOL RESULT

```
---
```


## [2026-09-05T18:30:15.079Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"dam\\b\\|damīdan\\|damiden\\|dhamati\" HUB.txt | head -30",
 "description": "Grep Hübschmann"
}
```


### [2026-09-05T18:30:15.120Z] TOOL RESULT

```
3137:doch nur LW. sein (np. praes. kanam, perf, handam).
4423:nach dem Muster: hurdan'^): pras. baratn etc.?; kudam
4426:pa kadam jci Vo?*; azurdan = CUardan ; afsiirdan aus *af-
4564:*koniglich*) ; ieni 'Spaziergang' ^^^ np. dam. Arm. e -= pers. a— 181 —
4636:kudam *was fQr ein?*, paz. kadam: skr. katamd- (vgl. paz.
4848:') Dafiir wird regelmftssig das semitische madam gesohrieben,
5426:212, zd. vdta-; bddrang 'Citrone =^ phi. vatrang\ badam
5515:gardtdaUy gastan (pr. gardam) 'sich drehen, wenden',
6718:gardam 886, ^wrrf899, -^irrf 900, ^irrf 901, gurda 905; fc(Xrrf
6798:penom — iph\, paddm 'Mundtuch*, arab. faddam (Tab. 243),
6799:arm. pandam (Elise 40, 16 v. u.), zd. paitidana- vd. 14, 8.
6973:wenden zu dem Praes. gardam (inf. gardidan), vgl. phi. gast
6977:dam (inf. navardTdan). Denn von der Wzl. vart konnte
7014:b) im Inlaut nach n^ z, zi handam *binde' = zd. ban-
7015:dami ; landa 'Sklave' = ap. bandaka- ; andam *K5rper, Glied'
7707:talm. Dn;n, niil er mass' Lag. A. Stud.; andam *Glied
7708:(5. Jhd.) = np. andam *Glied', auch 'Symmetric' (= Gliede^
7709:rung ), ab er noch arab. hadama^) zerstSrte, handam *Sym-
7713:metrie', aram. haddam 'Stuck' (Daniel), syr. DIH; andarj
7845:298), zd. zrayah-, aber dial, zarah^); 9) ap. adam *ich' —
8641:sitan reimt anf jddUsitoln) ; dam, tardzu^ arzu u. s. w.
9086:penom, phi. parfdm 'Mundtuch*, a,rm, pandam (5. Jhd.), arab.
9114:nistn *Geno8se* = *zusammen-sitzend*.H. 111—127, hangam H. 1109; paz. a«6(5?r, andam, angara
9116:hangam Shk. 249 ; phi. anbdr, andam, angdrtan, hangam,
9127:garam; andacem *untersuche' , np. andaz *Plan'; andam
9128:*Glied* = np. andam; andarj 'Testament* = np. andarz
9133:hambistar *Lagergenosse\ hamdil *gleichgesinnt*, hamdam
```


## [2026-09-05T18:30:20.186Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls -la BQT_v2*.txt BQT_v1*.txt && head -30 BQT_v2_pages.txt && echo \"=== formfeeds:\" && python3 -c \"\nd=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nprint(len(d), d.count('\\f'))\n\"",
 "description": "Inspect BQT v2 file"
}
```


### [2026-09-05T18:30:21.952Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 2247721 Sep  4 14:06 BQT_v1_pages.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 2620060 Sep  4 14:06 BQT_v1.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 4339896 Sep  4 14:06 BQT_v2_pages.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 2359504 Sep  4 14:06 BQT_v2.txt
                                         ‫‪7‬‬

                          ‫رن‪۳‬‬
    ‫نات‬
      ‫ا م‬
              ‫لض‌بال ‪ ۰ ۲۶‬رک‬
‫‪۱‬‬       ‫اسا تعدولیدیارتم و‬
                                     ‫‪7‬‬
‫‪ ۰‬و زل رسوا »وا روون لات سا روصا مواقم‬      ‫وتان‬

                      ‫‪۴2 ۱‬‬

                  ‫رک یمن‬
                  ‫م سارو کی و ررك‬


                 ‫جلررومدا‬
             ‫چاپ دوم فروردین ‪۳۴۳۱‬‬
                 ‫با تجدید نظر کامل‬
          ‫بسرمایه کتابفروشی ابن سیتناپران‬




                   ‫چاپ افست رشدبه‬
                   ‫م‬ ‫و‬
‫نآکو سخنیم بیاموزد مرا‬
                       ‫د‬ ‫د‬ ‫ل‬ ‫ج‬ ‫م‬ ‫ة‬ ‫چ‬ ‫ا‬ ‫ی‬ ‫د‬
‫على ‪۰‬‬             ‫بند گر دا ند ‪۰‬‬                       ‫‪۳‬‬      ‫‪۳7‬‬

=== formfeeds:
2900526 683
```


## [2026-09-05T18:30:26.501Z] TOOL CALL #15: Bash

```json
{
 "command": "sed -n '1,60p' tools/ref_page.py",
 "description": "Inspect ref_page tool"
}
```


### [2026-09-05T18:30:26.540Z] TOOL RESULT

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


## [2026-09-05T18:30:27.331Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"دماوند\\|دمیدن\\|دنیدن\\|دنان\" BQT_v2_pages.txt | head -20",
 "description": "Grep BQT v2 for headwords"
}
```


### [2026-09-05T18:30:27.395Z] TOOL RESULT

```
10979:‫خردما = بضم اول وسکودنانی وفتح‬                                    ‫خر در گله صجماعتی باشندازمتید(ه)‬
13635: ‫حنحر قلت کستابه از دمیدن صبح‬                      ‫۔‬     ‫گویند وبه‌عنی شادی وطربوعش‌هم هت‬
17059:‫بمعنی درافی است که شفتالو باشد بلفت اهل‬                  ‫دنانه از شخصی است که‬
19991:    ‫هرن‌توبد ‪( 0720 - 082 :‬مخز) « از ‪ 05240۰‬فی « با ازدمیدن ‪ » 8200721‬و(زیدن‪,‬‬
20013:                ‫‪ - ۴‬بممنی اسم فاعل له مصدر ‪.‬‬                       ‫اسم فاعل از« دمیدن > وحال ۔‬        ‫‪۱‬‬
20018:    ‫® ‪ -‬دماوند که درمآخف اسلامی «دتباوند »مده بتابتحقرق مرحوم کروی ( مجلةٌابنده‬
20022:     ‫( ازمسدر وندن = نهادن ) و«افع شدن » وهاستادن» » پس دماوند بعنی شهریا آبادی با قلعة‬
20025:    ‫که ترديك بوده « نپاوند * وآن دیگررا «دماوند» نامیده‌اند‪ .‬کروی فکر کرده که شاهراهی از‬
20029:              ‫ونادلدورسراین‌شاهراهپا نهاده‌است‪ .‬کروی در یاءان نگاشته‪« :‬شایدنهاو ندودماوند ثکزونهام‬
20030:    ‫تامها راکاروایان عرب داده ‪ ۲‬قله لزدسکتر را نهاوند وآن یکی را دماوندکفته اند ‪٩‬‏ پیداست که‬
20032:        ‫وعربتان رفت وآمد میکردند بجه دلیل عربستان را ماخ گرفتند ویکی راه دماوند» ودیگریرا‬
20033:        ‫«تپاوند» نامیدند؟ بیشترمتدادربذهن است که اقوام نا کن بین دکووه «دماوند» و«نهاوند» که درماد‬
20038:                                                                                           ‫را «دماوند)» تام‌نه‌اند»‬
20050:                                        ‫منظرءٌ دماوند‬                                 ‫زاخائوص ‪ :۲ ۷۲‬دنباو ند ‪۰‬‬
20212: ‫دمیدن « بروزن خمیدن ؛ بمعنی لاف‬                 ‫جمع کرده باشند ‪ - ۵‬و بکر اول به‌عنی رویاه‬
20236:                      ‫‪ - ۳‬اسم فاعل از «دمیدن» ‪.‬‬           ‫« معجم البلدان پنقل از ابن الفقید» ‪.‬‬
20251:                                                      ‫دماوند ‪.‬‬                    ‫وشراب وروغن وامثال آنراگونند؟ ‪۴ .‬‬
20275:               ‫رك‪ :‬دم (ضم‌اول)‪۰ ‎‬‬       ‫‪۳‬‬    ‫‪e‬‬            ‫ی _ اسم فاعل از «دنیدن» (ه‪.‬م‪. ).‬‬                         ‫خور ‪ -‬دن ‪.‬‬
20641:   ‫‪ - ۷‬طبری [‪ .2۷04‬ز‪( 4۷40‬لحاف)‪ .‬مدارزانی‬                    ‫‪ - ۷‬اسم‌مقمول از«دنیدن» ‪.‬‬
22196:      ‫دیماوند است که ناکموه دماوند باشد ‪.‬‬                           ‫چرم هم هست که سازی ادم خوانندش ‪ -‬وبفتح‬
```


## [2026-09-05T18:30:34.366Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"pdf page\" BQT_v2_pages.txt | head -3; echo \"---\"; python3 - <<'EOF'\nimport io\np='/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt'\nd=open(p,encoding='utf-8',errors='replace').read()\nlines=d.split('\\n')\n# find leaf index for line 20018\nimport bisect\noff=0\npositions=[]\nfor i,l in enumerate(lines):\n    positions.append(off)\n    off+=len(l)+1\nff=[i for i,c in enumerate(d) if c=='\\f']\nimport bisect\nfor ln in [19991,20018,20212,20275,20641]:\n    pos=positions[ln-1]\n    leaf=bisect.bisect_left(ff,pos)\n    print(ln,'-> leaf(0-based)',leaf)\nEOF",
 "description": "Map BQT lines to leaves"
}
```


### [2026-09-05T18:30:36.281Z] TOOL RESULT

```
---
19991 -> leaf(0-based) 337
20018 -> leaf(0-based) 338
20212 -> leaf(0-based) 341
20275 -> leaf(0-based) 342
20641 -> leaf(0-based) 348
```


## [2026-09-05T18:30:40.064Z] TOOL CALL #18: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nprint(json.dumps(d['BQT'],ensure_ascii=False,indent=1))\"",
 "description": "Full BQT ref entry"
}
```


### [2026-09-05T18:30:41.604Z] TOOL RESULT

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


## [2026-09-05T18:30:46.870Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 337 338 339; do echo \"=== leaf $((n-1)) = printed page $((n-1+540)) ===\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' BQT_v2_pages.txt; done",
 "description": "Print BQT pages 876-878"
}
```


### [2026-09-05T18:30:48.166Z] TOOL RESULT

```
=== leaf 336 = printed page 876 ===
   ‫پوس‬                                                                                                         ‫دلهرا‬

 ‫دليك = بفتح اول بروزن‌شريكث ‪ ,‬موه‬                        ‫دلهر | ‪ = ۱‬بکراول وهای هوز(‪)۱‬بر‬
 ‫وئمرکلی است ‪ . ۴‬وآن‌مانندتخمسه كلسەرىگڭ‬                      ‫وزن افترا‪ .‬لباامدشاهی وده آزیادشاهان‌هندوستان؛‬
‫میباشد؛ و بعضی گویند خم کل است کهبعربی‬                                       ‫وبقتح الك یزبنظرآمده امت ‪3‬‬
                                  ‫بذرالورد خواناد ‪.‬‬
                                                          ‫دلی « بکرارل وثالی بتحتان یکشید‪..‬‬
 ‫دینس = بفتح‌اول وثانیبتحتالیریده‬
                                ‫ل‬
                                                          ‫مخفف دهلی باشد وآن شهری است «شهور در‬
 ‫ولون مک‌وربین بی‌نقطهُ زده ‪ ۰‬بیونانی‪ ۴‬لوعی‬                 ‫حندوستان ‪ ۴‬؛ وبا تشدید ثانی کهفمته‌اند ‪۰‬‬
‫از صدف کوچك باشد و آنرا نا خام امت نمك‬
 ‫دلیده = بفتح'ول بروزن رسیده " خرد | سودکرده میخورند و چرن پخته شد نمیتوان‬
                                             ‫خوردن ‪.‬‬                            ‫وبلغور شدن غله راگویند ‪# .‬‬

                                                 ‫بیان هفد هم‬




‫ران بدان آ ش افروزند ‪ -‬و آه را هم‬
                                ‫کر‬‫که ز‬                    ‫» دم ولفی‬       ‫‏‪ a‬بشتح اول وسکون‌الی‬        ‫دم‬

‫وانند ‪ -‬ودهان آدمی‬
                 ‫کون ‪ -‬وافوی را لخیر‬
‫و زءان را هم گفته‌اند‪-‬‬      ‫وغیر آدمی باشد‪ -‬ووقت‬
                                                              ‫باشد © ‪ -‬وفریب وخدعه رانیز گویند ‪ -‬وبمعنی‬
           ‫‪۱‬‬     ‫‪٩‬‏‬             ‫‪۱‬‬   ‫‪۲‬‬                    ‫وبوی را یزگفته‌اند که‬           ‫‪-‬‬   ‫نخوت وتکبرهم‌هت‬
 ‫و درعربی بمه‌نی خون امت ‪٩‬‏‪ -‬وم اول دنب‬
                              ‫ودنباله رگاونشد ‪. ۷‬‬         ‫جرمی‌شم خوانند‪ -‬وبمعنی وزن شمرباشد‪ -‬وانبانی‬

                                                 ‫‪ :‬سی زده ‪.‬‬     ‫(‪ )۳‬چك‬               ‫(‪ )۱‬چك ‪ :‬وها ‪.‬‬

  ‫باستخت‌هندوتان ‪ .‬رك‪ :‬دهلی‪.‬‬              ‫‪ieD _ ۴‬‏‬             ‫رك‪ :‬بلهرا (صس‪ ۳۰۳‬ح ) )‪. (¢‬‬         ‫‏‪٩‬‬
   ‫‏‪) fruit de la rose =۴‬رف( كل ‪ ۲‬ص ‪ ۹۲.‬كلد ( رکب روا =) نرتد س‬
   ‫‪ - ۴‬بونانی ‪« 8811۱61‬ادتدکای» = ‪( 6811161‬فر) «لك‪۲‬‬                                  ‫‪ « 25‬ئاس ‪. ۲۸۱۰‬‬
  ‫‪mahd‬‏ ‪( 1010۳80 .‬نفس كردن > دعیدن)؛‬     ‫‪ - ۵‬هندی باستالی » ره‬   ‫ص‪٩۲‬‏ ‪.‬‬
  ‫ردن » وزیدن ؛ دمیان ) » کردی ع‬
                               ‫پپاوی ‪mad‬‏ ‪,‬فس ‪ :‬استی ‪nimid , 8۱۱۳‬‏ ( دکرد‬
  ‫‪۰,‬آرامی‬   ‫‪mad‬‏‬    ‫از مر ی‬       ‫(عر) ا‬      ‫‪ ۹‬ك‬                  ‫‪.‬‬   ‫“‪Yo‬‏‬    ‫سدق‬     ‫‪mad‬‏‬   ‫بلوچی‬    ‫‪۰‬‬   ‫‏‪den‬‬


  ‫‪ - ۷‬اوتا ‪( 31 -‬ذب) ‪.‬هلوی‬       ‫‪ 3‬آشوری بابلی ‪* 1721‬ولفنون ‪. ۹۸۲‬‬
  ‫‏‪dumb‬د‪.‬ی ‪ 00‬و ‪knud‬‏ افغانی ‪ 0121‬اى ‪ 83۳0‬و ‪" 830110‬باوچی‬‫‏‪ dun‬ر کر‬
  ‫‏‪ dunbag‬ر ‏‪ . dunb , dumb‬سریکلی نان ‪êmid .‬‏ ‪ .‬رخی ‪ 4090‬نا ‪ .‬مکل‬
    ‫آریابی آن ہایتی ۔ ‪ ۵ 3۲۵۳۷0‬باشد ”اق ‪ ۳۷۵‬ورك‪ :‬هوشمان ابسا؛ کیلکی ‪0‬ل‬

            ‫‪.‬‬   ‫‪.‬‬   ‫‪۶‬‬   ‫ص‬     ‫‪۳‬‬   ‫ك‬   ‫‪9‬‬   ‫‪mod‬‏‬    ‫شھمہرزادی‬    ‫و‬   ‫‪ 4‬لاسگردی‬    ‫هی‬     ‫»سر‬   ‫‪ ۰‬منگری‬       ‫‏‪dum‬‬


   ‫کالسکه برای حمل‬          ‫و انگلسی «‪ecnegilid‬‏‬         ‫او[ » از فرانوی‬        ‫© ولیجای ‪ -‬تک‬              ‫‪۱‬‬
                                                                                                ‫و يقل مافر ‪.‬‬
   ‫مشه درصفحه ‪yvA‬‏‬

=== leaf 337 = printed page 877 ===
  ‫دمان‬                                                                                                   ‫ت‬
                                                                                                         ‫ب‪۷‬‬

‫حیوالی که باشد و بهترین آن ازپرندکان مغز‬                   ‫دما = بفتح اول بروزن هوا » بمعثی دم‬
 ‫كربك وتیهوست وازچرند گان بره و کوساله‪,‬‬
                                      ‫س‬                    ‫ونفس باشدا ‪ -‬وبکراول بمعنی رودخانه است‬
 ‫وجمیم مفزها سرد و تر است» و مغز سرخروی‬                    ‫بلغت زند وپازند (‪ - ۱0۴‬ویمعتی مزاج وطبیعت‬
 ‫ومرغ بجهت گزند کیمارو عقرب نافع است »‬                                                    ‫ی‬              ‫هم اه‬
  ‫ومغزسر شت رکه دماغالبعبر خوانند چون خشك‬                  ‫بفتح اول و دال ایجد په‬         ‫دمادم ت‬
 ‫کنند وباسر که بمصروع دهند شفا بابد » ومغز‬                      ‫اهرن‬
                                                                   ‫وعفن تفن و‬       ‫جى مق ‪:‬زامن ف‬
 ‫سرمرغابی درد وآزار مقعف را نافع باثف ‪ ۳‬ومتر‬
                                                           ‫باشد ‪ - ۴‬بوضم‌اول به‌عنی‌متعاقب وپی‌در بیمکدگر‬
 ‫سرخفاش‌راچون‌بر کف با مالند باه رایرانگزاند؛‬                                                           ‫باشد © ‪.‬‬
 ‫وازاعضای رئیسه است که دل وجکرومغزسرباشد‬               ‫=ر وزن شرار » بمعنی هلا کے‬
                                                                                ‫دمار ب‬
 ‫بجهت بقای شخص واآنثیین را نیز ازاعضایرئیسه‬                ‫ونچه مردم بدان محتاح باشند در‬
                                                                                       ‫باشد ‪٩‬‏ ‪ -‬آ‬
                       ‫میدانند بجهت بقای نوع ‪.‬‬             ‫‪۷2‬‬     ‫زندگانی مطلقاً ‪ -‬و دم ولفس وا قکزنن‬
 ‫دمامه = بروزن شمامه ‪ .‬کوس وقارمرا‬                                 ‫وبم‌عنی دود ودخان هم پنظرآمده است ‪.‬‬
 ‫کویند ‪ -‬و بمعتی تفیر همأ مده است که برادد‬                 ‫دما ‏‪ ٩‬ه بفتح‌اول وسکون‌غین‌نقطه‌دار‬
                             ‫کوچك کرنا است ‪.‬‬               ‫بروزن‌رواق‪ ,‬کنابه ازعجب وتکبرونخوت ونبخش‬
‫دمان‪ .‬بروزن‌امان» بمعنی‌وقت وزمان‌بات ‪٩‬‏‬                   ‫روایند عموماً ازهر‬
                                                                            ‫باشد ‪ -‬ودر عربی مغز سر گ‬
                                                                        ‫‪ :‬رند ویاژند ‪۲‬‬        ‫چا‬   ‫)‪۱‬‬


   ‫» زود «بونکر ‪.»۸۸‬‬    ‫‪ ۰‬بهلوی ‪tûr‬‏‬        ‫‪êm)a(d ۰‬‬   ‫هز › ‪êmad‬‏‬         ‫‪۳‬‬       ‫‪2:‬م ‪.‬‬       ‫‪ ۱‬رك‬

   ‫از ‪ :‬دم ‪۱+‬‬      ‫‪۴‬‬         ‫‪ -۴‬باین هعتی‌از دساتیر است ‪ « .‬فرهنگگ دساتبر ‪٥٤۲‬‏ > ‪.‬‬
    ‫‪۰‬‬    ‫دم (جم داز)‬   ‫واسطه) ‪+‬‬        ‫‪۱+‬‬    ‫از ‪ :‬دم‬   ‫‪۵‬‬                ‫دم ( بفتح دال )‪.‬‬           ‫(واسطه ) ‪۳‬‬

   ‫‪( - ۱‬عر) « دمور بروزن سرور » و دمار پروزن سحاب » ودماره بزبادتی ها بمسنی‌هلال‬
                                       ‫کرداندنت » « شرح قا‌وی *؛ دماربر آوردن » هلاك کردن ‪:‬‬
   ‫بدینکرز ازشان برآرم دمار ‪ . .‬فردوسی طوسی ‪.‬‬                          ‫نردم نبرزند يك ذره خاك‬
   ‫‪ - ۸‬درعربی «دماغ بروزن کتاب مغز سراست ‪ ۰‬با اينکه دماغ‬                          ‫‪- ¥‬رك‪ :‬دم ‪-‬‬
   ‫جابی‌است که نرم میباشد ازمیان سرومفزدراوست‪ .‬یا ام الرأی وبالای پیشانی است» «شرح‌قاموس»‪.‬‬
    ‫هرن‌توبد ‪( 0720 - 082 :‬مخز) « از ‪ 05240۰‬فی « با ازدمیدن ‪ » 8200721‬و(زیدن‪,‬‬
   ‫فوت کردن) ساخته شده « اسفا ‪ ۷: ۱‬ص ‪۵۷۱٩‬‏ ‪ -‬در تداول فارسی دماغ (بفتح اول) بمعنی‌بینی‬
   ‫‪ ۳" -‬برای‌این معنی‌فرحنگه وان ( این‌شعر نظامی را شاهدآ ورده‌اند ‪:‬‬                               ‫استعمال‌میشود‬

              ‫برو نقش طرب بتی که خوش باش ‪.‬‬                              ‫صنعت هر دمان استاد نقاش‬
  ‫این بیت از خسرو وشیرین نظامی است و دباررث شاپور نقاش ساخته شده ‪ ,‬پیداست که‬
  ‫اسل آن چنین بوده ‪ :‬هنت هردم آن استاد قاش ‪ > ...‬کاتب دهردم آن » را بهمپیوسته‬
   ‫و« هردمان ‪٩‬‏ نوشته وفرهنگ»ه توسی بی‌خبر «هو» را جداکرده و« دمان» را لغتی جامد و بیط‬
    ‫» ولی این معنی‬     ‫‪۷۲۲-۸‬‏‬
                            ‫‪٩‬ص‬‫انکاشته « نقسی ‪ .‬دربارۂ چند لفت فارسی ‪ .‬بادنامةٌ پور داود ‪۱ ۳.‬‬
                                      ‫مأخوذ از دساتیر است « فرهنگک دساتبره‪ »4۲‬و رك ‪ :‬دمالکش ‪.‬‬
                                                                                              ‫بقبه ازصفحه ‪۷۸‬‬
              ‫‪ ۵‬دلیر ‪ -‬بکر اول وغالاً بفتح آن ‪ ,‬شهمیرزادی ‪ ۲8120‬د‪:‬لاور» شجاع ‪.‬‬
    ‫‏‪ ٩‬دلیری ‪ -‬بکر اول » از ‪ :‬دلیر ‪ +‬ی (مصدری)؛ دلاوری » شجاعت‪« :‬تهی‌دستان‌را‬
                                  ‫‪.‬‬    ‫دست دلیری بته است و بنج شبری شکسته» « کلتان ‪۱۲۱‬‬

=== leaf 338 = printed page 878 ===
    ‫‪0‬‬                                     ‫‪۱‬‬                                                           ‫دان کش‬
             ‫باشد ‪۰‬‬       ‫واه‬   ‫یمعتی وقت و زمان ومدتے‬             ‫بومعتی فرباد کنان از شادی و نشب فرط‬
‫لد "» بر وزن زراوند » تام‬                          ‫دهاو‬            ‫هم حت ‪ - ۱‬وبمعتی تند وتیز رفتن ‪ -‬و سخت‬
                    ‫حمله کردن‌ه مده است‪ ۴‬سودمندموفرباد کننده | شهرست مشهور از م‬
‫سارزان ‪٩‬‏ ‪ -‬وکوهی لیز‬
‫حست‌منسوب بآن‌شپر‪ .‬کوبند ضحاكرا درآن کوه‬                                                          ‫را فيز کویند؟ ‪.‬‬
                                        ‫وزن کان کش ‪ | ۰‬محبوس کرده‌اند ‪.‬‬              ‫‪۰‬‬      ‫دمان کش‬                    ‫‪۱‬‬
                ‫‪ - ۴‬بممنی اسم فاعل له مصدر ‪.‬‬                       ‫اسم فاعل از« دمیدن > وحال ۔‬        ‫‪۱‬‬
     ‫‪ - ۴‬لیزیمعنی مست وخشمناك ‪« :‬منم کهباپیل دمان بزنموبا شیرژبان پنجه درافکنم‪».‬‬
                          ‫‪.‬‬   ‫ان‬
                               ‫م‪:‬‬‫درك‬
                                   ‫“و‬     ‫‪ - ۴‬از دساتیر « فرهنگه دساتیر ‪۵۶‬‬                  ‫‪.‬‬      ‫«کلتان ‪۹۱۱‬‬
    ‫® ‪ -‬دماوند که درمآخف اسلامی «دتباوند »مده بتابتحقرق مرحوم کروی ( مجلةٌابنده‬
     ‫سال اول شمارء ‪ ۰ ۷‬ونیزمقالات کروی ‪۱‬ص ‪ ) ۹۷-۳۸‬کمرب‌است از هدما * ضم‌دال بمعنی‌یشت‬
     ‫ودتبال » چنانکه « نهاوند» فيزمرکب است از نها“ بممنی پیش » واکنون درلهجه های دزفولی‬
    ‫وشوشتری بهمین معنی هردو بکار روند‪ .‬جزودوم درهردو نام «وند» پسوند مایت بمعتی «نهادن»‬
     ‫( ازمسدر وندن = نهادن ) و«افع شدن » وهاستادن» » پس دماوند بعنی شهریا آبادی با قلعة‬
    ‫ایتاده دردلبال ویشت » و لهاوند یمنی شهربا آبادی با قلعة ایستاده درییش‌رو ‪ .‬میتوان کفت که‬
    ‫درنامگذاری این دوآبادی » دوری ونزدیکی آنهارا نیت بجایی با شهری میزان گرفته‌اندآ نچهرا‬
    ‫که ترديك بوده « نپاوند * وآن دیگررا «دماوند» نامیده‌اند‪ .‬کروی فکر کرده که شاهراهی از‬
        ‫روزکاران باستان غرب عالم متمدن را بشرق آن میرسانیده و از لودیا بباختر ( بلخ ) میرفته‬
    ‫وشاهراء دیگری ازشوش بپگمتان (حمدان) می کشیده وبشاهراه باخترمی‌پیوسته وقلعه‌های نهاو ند‬
     ‫‌بوده واین‬
              ‫ونادلدورسراین‌شاهراهپا نهاده‌است‪ .‬کروی در یاءان نگاشته‪« :‬شایدنهاو ندودماوند ثکزونهام‬
    ‫تامها راکاروایان عرب داده ‪ ۲‬قله لزدسکتر را نهاوند وآن یکی را دماوندکفته اند ‪٩‬‏ پیداست که‬
        ‫اکرکاروانیان «عرب» میبودند » نام عربی‌میگذاشتند واگرکاروانیان ایرانیانی بودند که بین ابران‬
        ‫وعربتان رفت وآمد میکردند بجه دلیل عربستان را ماخ گرفتند ویکی راه دماوند» ودیگریرا‬
        ‫«تپاوند» نامیدند؟ بیشترمتدادربذهن است که اقوام نا کن بین دکووه «دماوند» و«نهاوند» که درماد‬
    ‫داشتند ( هگمتانه ( همدان ) باسخت ماد بوده ) کوه بش روی خود را که‬                            ‫(عراق عجم ) کک‬

                                                                                           ‫تردیکتر بآلان بوده‬
                                                                                           ‫«بهاوند“ر کوهیشت‌سر‬
                                                                                           ‫را «دماوند)» تام‌نه‌اند»‬

                                                                                          ‫چنانکه‌یثت کوهوییش کوه‬
                                                                                           ‫درلرستان‪ .‬یاقوت در‬
                                                                                    ‫‪E‬‏‬     ‫«دتیاولد» کوبد‪:‬لغةفی‬
                                                                                 ‫«رماوند» کوهی‌ازنواحی ‪0 ( .‬‬
‫‪۱‬‬                     ‫‪E‬‬                       ‫‪EER‬‏‬            ‫و‬     ‫‪e‬‏‬     ‫‪۰ ۲‬‬             ‫رعبونیزکوهی‌بکرمان‪,‬‬


                                    ‫ی‬         ‫‪SE‬‬          ‫‪9‬‬   ‫‪E‬‏‬                      ‫ج‬     ‫‪:‬عجمم‬
                                                                                                ‫م‬         ‫برداژد ‪ .‬ر‬
                                                                                           ‫ائلبالدرانا‪,‬لب]اقيەچاپ‬
                                        ‫منظرءٌ دماوند‬                                 ‫زاخائوص ‪ :۲ ۷۲‬دنباو ند ‪۰‬‬
     ‫کرزی ومقرفرمانداری است » در*‪ ۷‬کیلومتری شمال خاوری‬
                                                     ‫‪ - ۱‬اکنون جزو استان م‬
    ‫ب(رهان فاطع ‪) ۵۱۱‬‬               ‫‪.‬‬‫‪۸‬ص‬    ‫ای ابر‬
                                         ‫‪۹‬ان‬        ‫م‪:‬‬ ‫ن رک‬
                                                          ‫هه ‪.‬‬
                                                             ‫ر‪۰۰‬اصکن‬‫ار»ای ‪۰۸‬‬
                                                                           ‫دان‬
                                                                             ‫ور‬
```


## [2026-09-05T18:31:11.514Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==349' BQT_v2_pages.txt",
 "description": "Print BQT printed page 888"
}
```


### [2026-09-05T18:31:13.295Z] TOOL RESULT

```
    ‫یات‬                                                                                     ‫دله گرقه‬

‫دلین ‪ = ۴‬بر وزن رسیدن ‪ .‬بمعئی‬
 ‫دوبدن بنشاط و بخوشحالی براه رفتن باشد ® ‪-‬‬           ‫نعمت الهی باشد ‪ -‬و بمعنی خوشحال و شادمان‬

 ‫وبمعنی ازجای دآر‪.‬دن ‪ -‬وازخشم وقپرجوشیدن‬            ‫را لىز‬   ‫و تند براه رونده و دوفده‬        ‫هم همست‬

                                   ‫همگفته‌اند ‪:‬‬                                              ‫کفهداند ‪.‬‬


         ‫راه رفته ناشد ‪۳‬‬   ‫بخوشحالی‬    ‫خرام ده و‬
                                                     ‫وخوشحالی‌بخرامی‪ -‬وبعریی‪ ۴‬مردم دون وخیی‬
                                                                                            ‫رکاویند ‪.‬‬


                                         ‫بان نورد هم‬


 ‫‪ ¥‬دو ] تش ‪-‬کنابه از دوب معشوق | وزن روارو » دویدن بهرطرف باشد از پی‌هم ‪-‬‬
‫شوخصی را نکیوزبند که خدمات جزئی باو‬                                                               ‫باشد‬
     ‫رجوع باشد وهرساعت اورا بکاری فرستند ‪.‬‬
                                                    ‫دواج ‪ = ۲‬بفتح اول بر وزن رواج »‬
‫دوادی ت بفتح اول بر وزن نهاری »‬                                             ‫یمعنی لحان باشد ‪. ۸‬‬
‫از آن به‌ینج‬   ‫رایج ازطلا که هرك‬   ‫زری‌بوده‌است‬


 ‫وال ابجد بد | شیالی خرح میشده " وشیانی زری بوده الزای‬
                                                     ‫دوادو ‏‪ = ٩‬بفتح اول د‬

       ‫(عر) بتشدید اخرآمده ‪.‬‬
                           ‫‪۴‬‬                   ‫؟ ‪۴‬‏ رك‪ :‬دیدن ‪.‬‬          ‫رك ‪ :‬دنه ‪.‬‬      ‫‪۱‬‬
   ‫از ‪ :‬دن ‪٣‬‏ بدن(یسوند مصدری) ‪.‬هندی باستان » ره ‪_131d‬‏ ‪62040020 ,‬‬                      ‫‪۴‬‬
                                                                  ‫(دویدن) د اسشق ‪ 6۷۵‬دوم “ ‪.‬‬

  ‫بر خم همی خرامی و بردن همی‌دلی ‪.‬‬                 ‫‌بهرمی‌شینی و ب رگل همی خوری‬
                                                                              ‫®ل‪-‬‬
                                                                                ‫گ‬
  ‫«‪+‬ءنوچهری دامفانی ‪۹۰۱٩‬‏ ‪.‬‬
   ‫‪ - ۷‬طبری [‪ .2۷04‬ز‪( 4۷40‬لحاف)‪ .‬مدارزانی‬                    ‫‪ - ۷‬اسم‌مقمول از«دنیدن» ‪.‬‬
                                      ‫کنوی [‪ . ۵۷61‬ز‪ . 24‬زا ‪2[ .‬ظ‪ 0‬دواژه نامه ‪. 4۹۳۰‬‬
           ‫همی غلطم اندرمیان دواح ‪.‬‬                     ‫یمآگه از اسل وفرع خراج‬                ‫‪۸‬‬
  ‫فردوسی‌طوسی‪« .‬چهارمقاله‪.>۸4‬‬
                       ‫‏‪ - ٩‬از ‪ :‬دو (دویدن) ‪( ۱ +‬واسطه) ‪ +‬دو (ایسا) ‪.‬‬
 ‫که ‪« ۷۵-۸۵‬منای‬
              ‫‪ #‬دو ‪ -‬م اول (‪ , )00‬پهلوی ‪ , 80‬از ره ل‪« © 13۷‬ریی‬
 ‫‪.‬ردی لال ‪.‬‬‫‪ > ۲۷‬بارسی باستان ‪( 3103۷0۱ -‬دومن) ‪ .‬اوستا ‪( 2۷‬دو) » پازند ‪ ۵4‬ک‬
  ‫‪ . 0‬افمای ‪ . 2۷1‬استی ‪8۷‬ا‪ .1‬وخی ‪ ۰ 099‬سریکلی لوطل ‪ .‬شفنی ‪ » 624‬یفنوبی‬
     ‫ف‬
     ‫صد »‬
        ‫و متکلیجی لا " منجی ‪ « 0‬اسشق ‪ » ۵۷۵‬؛ عدد اصلی بين يك و سه » ضمف واح‬
                                                                ‫چهار ‪ .‬انان ‪.‬‬
```


## [2026-09-05T18:31:27.332Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==348' BQT_v2_pages.txt",
 "description": "Print BQT printed page 887"
}
```


### [2026-09-05T18:31:29.429Z] TOOL RESULT

```
                                                                                               ‫سب برسس‬


‫آیی را کون دکه از جای بلندی تابر زمین بخ‬                        ‫ند ‪#.‬‬
                                                                    ‫وینرا‬
                                                                        ‫کرلب‬
                                                                           ‫ثالی ‪ ۰‬سخن آهسته زی‬
      ‫زیر ناودالرا نکینزته‌اند ‪.‬‬    ‫خ‬
                                    ‫وشدب‪-‬‬
                                        ‫بسته با‬            ‫دن ‪ -‬بروزن رجیدن » درزس‬
                                                                                 ‫یند‬
                                                                                   ‫ك‬
 ‫دنگد اله ‪ - ۱‬بسکون ثالث بر وزن‬                           ‫لب آهسته آهسته بخاود حرف زدن باشد از‬
                                                           ‫جوشیدن اخزشم ‪۰‬‬  ‫نضب و‬   ‫روی فهر و‬
‫ناودان و امثال آن باشد ؛ وبفتح ثالث نیزآعده‬                ‫وشیرازبان لندیدن‌بضملاممیگویند وخراسالیان‌لیز‪.‬‬
                                            ‫است ‪.‬‬          ‫كقر ف«بااف بروزن لنگر» شوره است‬
                                                                                         ‫ن‬
‫دگل ‪ -‬بکرالت بروزن‌منزل » ابله‬
                             ‫ن‬                             ‫وازآن باروت‌سازند‪ .‬بعضی کوبند این لفغت عربی‬
‫وبی‌اندام را کو شف‬    ‫ودیوتث ‪-‬‬     ‫ونادان واحمق ‪۷‬‬                             ‫است وبعضی رومی گفته‌اند ‪.‬‬
    ‫وبفتح ثالثروبرونتن درمجلس باشد؛ وسضی گوبند‬             ‫واف‬
                                                             ‫د هه ‪ -‬بنتح اول و سکون ثالی ق‬
                          ‫باینمعنی ترکی است ‪. ۸‬‬           ‫مفتوح » حبی است دوایی ‪ ۰ ۴‬گویند اگر با‬
‫دنگی ‏‪ -)۱( ٩‬بکراول وسکون ثالی‬                            ‫کگورد بربهق طلاکنند نافع‌است » و آنچه از‬
‫دنگه کوب را گوشد ‪۹‬‬          ‫وئالث بتحتانی کشیده ‪¢‬‬         ‫آن درمیان گندم روید سکر ومدر باشد و آنرا‬



‫دنواش ‪ -‬بکس اول و سکون ثالی‬                               ‫دنگ » بنتح اول بر وزن سنگه »‬
                                                           ‫صدایی که از برهم خوردن دو منگه با دوچوب‬
‫و واو بالف کشده و بشن اقطه دار(‪ )۲‬زده» تلم‬

‫‪.‬‬    ‫است که عثرا ممشوقة وامق را بفر وخت‬       ‫مردی‬
                                                           ‫کرار‬
                                                              ‫وامثال آن برآید ‪ -‬وبمعنی شان ونقطة پ‬
‫بقتح اول وثالی » للمز نی‌است‪-.‬‬     ‫‪ ۵‬زه ‪۳‬‬                 ‫همهت ‪ -‬وبی‌خبر وییهوش واحمق وابلهرا نیز‬

‫وبمعنی نعمت دلیوی = و شادی ‪ --‬وصدا وندا‬                   ‫کویند ‪ - ۴‬و بکسراول چوبی باشد بهیات سر‬
 ‫وزمزمه ازغایت خوشحالی هم‌آمده است‪ -‬ویعضی‬                ‫وردن اسب که بدان شلتوك را بکوبند تابرنج‬
                                                                                               ‫گ‬
 ‫کوبند دنه صدا آوواز خوانندگی زان مطربه‬                                              ‫ازبوست برآید ‪.. ۴‬‬
                                        ‫است ‪۱۱۰‬‬           ‫دنگا له * = بفتح اول بروزن بنگاله‪,‬‬

                                       ‫اقطه دار ‪.‬‬    ‫‪۳‬‬    ‫)«( چك‬            ‫(‪ )۱‬چش ‪ :‬دنکی ‪.‬‬

                                      ‫‪( ]6۱]2۲.۷« ۴‬فر)« لك ‪۲‬ص‪٩۸‬‏ ؟‪.‬‬              ‫رك‪ :‬دندنه ‪.‬‬       ‫‪- ۱‬‬
                                      ‫‪ _ ۴‬رك‪ :‬یادنگه‪ ,‬دنگی‪.‬‬                 ‫رك ‪ :‬دند » دنگل‪.‬‬       ‫‪-‬‬   ‫‪۴‬‬

                                            ‫‪ ۱‬ر‪-‬ك‪ :‬دنگاله ‪.‬‬                ‫® _ رك ‪ :‬دنگداله ‪.‬‬
                                      ‫«دنکل»‬
                                                ‫‪ - ۸‬درتر‬                 ‫رك‪ :‬دنگه » دند ‪.‬‬      ‫‪۷‬‬

                                     ‫‪ :‬دنگه‬    ‫از‬
                                                ‫‪-‬‬                ‫بمعئی اجتماع اجستفت«ابی ‪. > ۹۱۳‬‬
                                                         ‫رك ‪ :‬دن ‪.‬‬   ‫‪1‬‬          ‫ی (دبت) ‪8‬‬      ‫(ه‪.‬م) ‪+‬‬
                                            ‫سمعتی آهنگی مخصوص آ ورده ‪:‬‬          ‫‪ _۷‬منو چهری‬

                                                   ‫بامدادان برچکك» چون چائتگاهان برشخج‬
                                            ‫دمروزان بر لینا » شامگاهان بدرنه ‪.‬‬
                                       ‫دامغانی ‪. > ۹۷‬‬       ‫‪ 2‬منوچهری‬

                                     ‫زی)؛ از‪:‬‬
                                            ‫مر‬‫چردنده ‪ -‬بفتح اول کوسرسوم (درلهجة ک‬
                                      ‫دند (ر که ‪ :‬دند » دندان) اه (یسونددبت)» کیلکی ‘‪adnad‬‏‬
```


## [2026-09-05T18:31:47.237Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"دنان\\|دمان و دنان\" FSF_pages.txt | head -20",
 "description": "Grep Noushin Shahnameh glossary"
}
```


### [2026-09-05T18:31:47.285Z] TOOL RESULT

```
583:                            ‫دنان‬
1184:                                                                       ‫دنانکر‬
2651:             ‫جذ عدنانی‬
12419:‫دنان‬                                         ‫‪۳۳۲‬‬
12451:                             ‫دنان (با زیر اول)‬     ‫میانم به دونیم کردی به‌تیغ‬
12469:             ‫روانش ز انديشه پر دود بود‪...‬‬           ‫بنابراین دنان به معنی شتابان روان شتابان‬
12472:‫و ویران کردن» هلاک و‬        ‫آتش زدن‪ ,‬خراب‬           ‫دمان و دنان برگرفتند راه‬
12476:                                                              ‫گهرد دنان در‬
12477:                                                                         ‫ای همه‌ساله دنان ب‬
12479:                                                    ‫مننهبه گرد دنانم و نه دنانم‬
12481:                                                    ‫(در مصراع اول دنان اول از فعل دنیدن و‬
12482:                                                    ‫دنان دوم جمع دن [با زبر اول ‪-‬تازی] به‬
17593:                                                                          ‫ارمدنانه ش‬
```


## [2026-09-05T18:31:48.241Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^damp\\|^dim\\b\\| damp,\\|'damp'\" KLN_1966.txt | head -20; echo \"--- 1971:\"; grep -n \"^damp\\|^dim,\" KLN_1971.txt | head -20",
 "description": "Grep Klein for damp/dim"
}
```


### [2026-09-05T18:31:48.326Z] TOOL RESULT

```
7813:clamp,  n.,  a  device  for  fastening.  —  ME.  prob. fr.  MDu.  *clampe  (Du.  klamp),  ‘a  clamp’,  which is  rel.  to  OE.  clamm,  ‘bond,  fetter,  chain ;  grasp’, OE.  beclemman,  ‘to  bind,  enclose,  fetter’,  OHG. biklemmen,  ‘to  squeeze  in’,  Du.,  MHG.,  G. klemmen,  ‘to  squeeze’,  MHG.,  G.  klemme, ‘clamp’,  fr.  I.-E.  base  *glem-,  ‘to  embrace, compress,  squeeze’,  whence  also  L.  glomus, gen.  glomeris ,  ‘ball,  sphere’,  Lith.  glomoti,  ‘to embrace’,  Lith.  glemziii,  glemzti,  Lett,  glemzt, ‘to  compress,  crush’.  I.-E.  *glem-  is  an  enlarge¬ ment  of  base  *get-,  ‘to  roll  up  into  a  ball,  com¬ press’.  See  glebe  and  cp.  glomerate.  Cp.  also next  word.  Cp.  also  clam,  ‘bivalve’,  clasp, clem,  clip,  ‘to  embrace’,  club,  clump,  clumsy. Derivatives:  damp,  to  fasten  with  clamps, clamp-er,  n.
10286:after  the  French  chemist  A.  Damour  (1808-1902). For  the  ending  see  subst.  suff.  -ite. damp,  n.  —  MDu.  (  —  Du.),  ‘vapor’,  rel.  to  Dan. damp,  OHG.,  MHG.  damph,  tamph,  G.  Dampf of  s.m.,  ON.  dampi,  ‘dust’,  and  in  gradational relationship  to  MHG.  dimpfen,  ‘to  smoke’,  OE. dimme,  dim,  ‘dark,  obscure’.  See  dim  and  cp. dump,  ‘sadness’.  Cp.  also  dank.
10287:Derivatives:  damp,  adj.  and  tr.  v.,  damp-en,  tr. and  intr.  v.,  damp-er,  n.,  damp-ish,  adj.,  damp-ly, adv.,  damp-ness,  n.
10327:niel  (Bible).  —  Heb.  Ddni'il,  lit.  ‘God  is  my judge’,  rel.  to  Akkad.  Ddnilu.  For  the  first  ele¬ ment  see  Dan,  PN.,  for  the  second  see  El. dank,  adj.,  moist,  damp.  —  ME.  danke,  of  Scand. origin;  cp.  Swed.  dank,  ‘moist  place’,  ddnka, ‘to  moisten’,  which  are  rel.  to  OS.  dunkar, OFris.  diunk,  ‘dark’,  ON.  dokkr,  Du.  donker, OHG.  tunkal ,  dunkal,  MHG.  tunkel,  G.  dunkel, of  s.m.,  and  to  OHG.,  MHG.  damph,  MDu., Du.  damp,  ‘vapbr’.  See  damp.
11442:diluvian,  adj.,  pertaining  to  the  flood.  — -  Formed with  suff.  -an  fr.  L.  diluvium.  See  diluvium, diluvianism,  n.,  the  theory  that  many  geological phenomena  are  due  to  the  Deluge.  —  Formed with  suff.  -ism  fr.  L.  diluvium.  See  next  word, diluvium,  n.,  an  accumulation  of  sand  and  gravel (geol.)  —  L.  diluvium,  ‘flood,  deluge’,  fr.  diluere, ‘to  wash  away’  fr.  di-,  ‘apart’,  and  luere,  ‘to wash,  lave,  cleanse’.  See  lave  and  cp.  deluge. The  accumulation  of  sand  was  formerly  attri¬ buted  to  the  Deluge,  whence  its  name  diluvium. dim,  adj.  —  ME.  dimm,  dim,  fr.  OE.  dimme, dimm,  ‘dark,  obscure;  unknown:  wicked’,  rel. to  ON.  dimmr,  OFris.  dim,  OHG.,  MHG.  tim¬ ber,  ‘dark,  black,  somber’,  and  prob.  cogn. with  Gk.  OEpLcpoq,  ‘grave,  austere’,  »Ep.epai^t?, ‘of  grave  countenance’,  Mir.  dem,  ‘black,  dark’. Cp.  damp,  dump.
40679:uliginose,  uliginous,  adj.,  oozy,  muddy.  —  L.  uli- ginosus,  ‘wet,  damp,  marshy’,  fr.  uligo,  gen. -ginis,  ’moisture,  dampness’,  contraction  of *uviligo,  fr.  in  ere,  ‘to  be  wet’,  whence  also  fivi- dus,  iidits,  ‘wet’.  See  udometer  and  adj.  suff.  -ose, resp.  -ous,  and  cp.  Ulex.
--- 1971:
12691:dim, dull, faint’. See Moor and cp. words there 
63923:damp, n. — MDu. (= Du.), ‘vapor’, rel. to Dan. 
63924:damp, OHG., MHG. damph , tamph , G. Damp f, 
71526:dim, adj. — ME. dimm, dim , fr. OE. dimme, 
95136:damp’, and cogn. with OI. pahkah , ‘mud, mire*,
```


## [2026-09-05T18:32:00.023Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport bisect\np='KLN_1966.txt'\nd=open(p,encoding='utf-8',errors='replace').read()\nlines=d.split('\\n')\npos=[];off=0\nfor l in lines:\n    pos.append(off); off+=len(l)+1\nff=[i for i,c in enumerate(d) if c=='\\f']\nfor ln in [10286,10327,11442]:\n    leaf=bisect.bisect_left(ff,pos[ln-1])\n    print(ln,'leaf',leaf,'-> printed approx', 2*(leaf-12), 'and', 2*(leaf-12)+1)\nEOF",
 "description": "Map Klein lines to printed pages"
}
```


### [2026-09-05T18:32:02.190Z] TOOL RESULT

```
10286 leaf 220 -> printed approx 416 and 417
10327 leaf 221 -> printed approx 418 and 419
11442 leaf 246 -> printed approx 468 and 469
```


## [2026-09-05T18:32:13.529Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"dhen-\\|dhem-\\|dheme-\" AHD_watkins1985.txt | head -20; echo \"=== font:\"; grep -n \"font\\b\" AHD_watkins1985.txt | head -20",
 "description": "Grep AHD Watkins"
}
```


### [2026-09-05T18:32:13.593Z] TOOL RESULT

```
360:[dan-. Low ground. Germanic root. Suffixed form *dan- Jam in: a. Old English denn, lair of a wild beast: DEN; b. possibly Old English Dene (genitive plural Dena), the Danes, and Old Norse Danr, Dane: DANE, DANISH; DANELAW. [In Pok. 2. dhen- 249.]] dap-. To apportion (in exchange). Suffixed form *dap-no- in Latin damnum, damage entailing liability (for repara- tion), harm: DAMAGE, DAMN; CONDEMN, DAMNIFY, IN- DEMNIFY, (INDEMNITY). [In Pok. dd- 175.] de-. Demonstrative stem, base of prepositions and ad- verbs. 1. Germanic *t6 in Old English #6, to: TO, TOO. 2. Perhaps Latin dé, dé-, from: DE-. 3. Latin déterior, worse: DETERIORATE. 4, Latin débilis, weak (see bel-). [Pok. de-, do- 181.] dé-. To bind. Contracted from *deo-. Greek dein, to bind: DESMID; ANADEM, ASYNDETON, DIADEM, PLASMODESMA, (SYNDESMOSIS), SYNDETIC. [Pok. dé- 183.] deigh-. Insect. Possibly in Germanic *tik-6, tikk-6 in Middle English teke, tick: TIck?. [Pok. deigh- 187.] deik-. To show, pronounce solemnly; also in derivatives referring to the directing of words or objects. I. Variant *deig-. 1. O-grade form doig- in: a. Germanic *taikjan, to show, in Old English t&can, to show, instruct: TEACH; b. Germanic *taiknam in (i) Old English tacen, tacn, sign, mark: TOKEN (ii) Old English tdcnian, to signify: BETO- KEN (iti) Gothic taikns, sign: TETCHY (iv) Old French tache, teche, mark, stain: TACHISM. 2. Latin digitus, finger (< “pointer,” “indicator”): picitT. II. Basic form *deik-. 1. O-grade form *doik- possibly in Germanic *taihw6 in Old English ta, tahe, toe: TOE. 2. Basic form *deik- in Latin dicere, to say, tell: DICTATE, DICTION, DICTUM, DITTO, DITTY; ADDICT, BENEDICTION, CONDI- TION, CONTRADICT, EDICT, FATIDIC, (INDICT), INDITE, INTERDICT, JURIDICAL, JURISDICTION, MALEDICT, PRE- DICT, VALEDICTION, VERDICT, VERIDICAL. 3. Zero-grade form *dik-d- in Latin dicdre, to proclaim: ABDICATE, DEDICATE, PREACH, PREDICATE. 4. Agential suffix *-dik- in: a. Latin index, indicator, forefinger (in-, toward; see en): INDEX, INDICATE; b. Latin jiidex (< *yewes-dik-), judge, “one who shows or pronounces the law” (jis, law; see yewes-): JUDGE, JUDICIAL; PREJUDICE; Cc. Latin vindex (first element obscure), claimant, avenger: (VEN- DETTA), VINDICATE; (AVENGE), REVENGE. 5. Greek deik- nunai, to show: DEICTIC; APODICTIC, PARADIGM, POLICY?. 6. Zero-grade form *dik- in Greek dikein, to throw (< “to direct an object”): DIsK. 7. Form *dikd in Greek diké, justice, right, court case: DICAST; EURYDICE, SYNDIC, THEODICY. [Pok. deik- 188.] deiw-. To shine (and in many derivatives, “sky, heaven, god”). I. Noun *deiwos, god. 1. Germanic *Tiwaz in: a. Old English Tiw (genitive Tiwes), god of war and sky: Tiu, (TuEspay); b. Old Norse Tyr, sky god: Tyr. 2. Latin deus, god: DEISM, DEITY, JOSS; ADIEU, DEICIDE, DEIFIC. 3. Latin divus, divine, god: DIVA, DIVINE!, (DI- VINE?). 4. Latin dives, rich (< “fortunate, blessed, di- vine”): Dives. 5. Suffixed zero-grade form *diw-yo-, heavenly, in Latin Didna, moon goddess: DIANA. 6. San- skrit devah, god, and deva-, divine: DEVI; DEODAR, DEVANAGARI. II. Variant *dyeu-, Jove, the name of the god of the bright sky, head of the Indo-European pan- theon. 1. Latin Jovis, Jupiter (> Italian Giove): JovE, JOVIAL. 2. Derivative *jou-il- in Latin Jiilius, “descended from Jupiter” (name of a Roman gens): JULY. 3. Voca- tive compound *dyeu-poter- (*pater-, father; see peater-), “O father Jove,” in Latin Juppiter, Jiipiter, head of the Roman pantheon: JuprTerR. 4. Greek Zeus, Zeus: ZEUS; (Dioscuri). III. Variant *dyé- (< *dyea-) in Latin diés, day (> Late Latin diurnum, day): DIAL, DIARY, DIET?, DISMAL, DIURNAL; ADJOURN, CIRCADIAN, (JOURNAL), (JOURNEY), MERIDIAN, QUOTIDIAN, (POSTMERIDIAN), SOJOURN. IV. Variant *deis- in Greek délos (< *deyalos), clear: PSYCHEDELIC. [Pok. 1. dei- 183.] dek-'. To take, accept. 1. Suffixed (stative) form *dek-é- in Latin decére, to be fitting (< “to be acceptable”):
377:dapper, heavy, strong; later quick, nimble: DAPPER. [Pok. dheb- 239.] dhegvh-. To burn, warm. Suffixed o-grade form *dhogvh- eye- in Latin fovére, to warm, cherish, foment (> fomen- tare, to foment, and fomes, tinder): FOMENT, FOMITE. [Pok. dhegth- 240.] dh@(i)-. To suck. Contracted from *dheoa(i)-. 1. Suffixed reduced form *dhé-mnd- in Latin fémina, woman (< “she who suckles”): FEMALE, FEMININE; EFFEMINATE. 2. Suf- fixed reduced form *dhé-to- in Latin fétus, pregnancy, childbearing, offspring: FAWN, (FETAL), FETUS; EFFETE, (FETICIDE), SUPERFETATE. 3. Suffixed reduced form *dhé-kundo- in Latin fécundus, fruitful: FECUND. 4. Suf- fixed reduced form *dhé-no- in Latin fénum, faenum, hay ( < “produce”): FENNEL, FINOCHIO; (FENUGREEK), SAIN- FOIN. 5. Perhaps suffixed zero-grade form *dhi-lyo- (< *dhia-lyo-) in Latin filius, son, and filia, daughter (but these are equally possibly from the root bheue-): FILIAL, FILIATE; AFFILIATE, HIDALGO. 6. Suffixed reduced form *dhé-lo- in Latin fél(are, to suck: FELLATIO. 7. Suffixed reduced form *dhé-l-ik- in Latin félix, fruitful, fertile, lucky, happy: FELICITATE, FELICITY; FELICIFIC, INFELIC- Ty. 8. Suffixed reduced form *dhé-ld- in Greek thélé, nipple: ENDOTHELIUM, EPITHELIUM, (MESOTHELIUM). 9. Suffixed reduced form *dhé-l-u- in Greek thélus, female: THEELIN. [Pok. dhéi)- 241.] dheia-. To see, look. Variant form *dhyd- (< *dhyag-) in: a. suffixed form *dhyd-mn in Greek sémeion and séma (stem sémat-), sign: SEMANTIC, SEMATIC; SEMAPHORE, SEMASIOLOGY, SEMEME, SEMIOLOGY, SEMIOTIC; b, San- skrit dhydti, he meditates (< “he observes mentally”): ZEN BUDDHISM. [Pok. dheis- 243.] dheigh-. To form, build. 1. Germanic *daigjén in Old English d%ge, bread kneader: DAIRY. 2. Germanic *-dig- in Old English compound Aléfdige, mistress of a house- hold (< “bread kneader”; Al#f, bread, loaf): LADY. 3. Ex- tended o-grade form *dhoigho- in Germanic *daigaz in: a. Old English dag, dough: pouGH; b. Old High German teic, dough: TEIGLACH. 4. Suffixed zero-grade form *dhigh-ird, in Latin figira, form, shape (< “result of kneading”): FIGURE; CONFIGURATION, DISFIGURE, PRE- FIGURE, TRANSFIGURE. 5. Nasalized zero-grade form *dhi-n-gh- in Latin fingere, to shape: (FAINT), FEIGN, (FEINT), FICTILE, FICTION, FIGMENT; EFFIGY. 6. Nasal- ized zero-grade form *dhi-n-g(h)- in Greek thinganein, to touch: THIGMOTAXIS, THIXOTROPY. 7. Suffixed o-grade form *dhoigh-o- in Avestan daéza-, wall (originally made of clay or mud bricks): PARADISE. [Pok. dheigh- 244.] dhel-. A hollow. 1. Germanic *daljé in Old English dell, valley: DELL. 2. Germanic *dalam in Old English del, valley: DALE. 3. Germanic *del- in Old Norse dzla, wooden gutter on a ship: DALLES. [Pok. 1. dhel- 245.] dhelbh-. To dig, excavate. Germanic *de/ban in Old English de/fan, to dig: DELVE. [Pok. dhelbh- 246.] dhembh-. To bury. Suffixed zero-grade form *dhmbh-o- in Greek taphos (< *thaphos), tomb: CENOTAPH, EPI- TAPH. [Pok. (dhembh-), dhmbh- 248.] dhen-'. To run, flow. Suffixed o-grade form *dhon-ti- in Latin fons (stem font-), spring, fountain: FONT!, FOUN- TaIN. [Pok. 1. dhen- 249.] dhen-2. Palm of the hand. Suffixed form *dhen-r in Greek thenar, palm of the hand: THENAR. [Pok. 2. dhen- 249.] dher-1. To make muddy; darkness. 1. Suffixed form *dher-g- in Germanic *derk- in Old English deorc, dark: DARK. 2. Suffixed zero-grade form *dhr-egh- in: a. Ger- manic ‘suffixed form *drah-sta- in Old English drés, dregs: pross; b. Germanic *dragj6 in Old Norse dregg, dregs: DREGS. 3. Suffixed extended zero-grade form *dhro-bh- in Germanic *drab- in: a. Old English dreflian, to drivel: DRIVEL; b. probably Low German drabbelen, to paddle in water or mire, draggle, akin to the Low German source of Middle English drabelen, to draggle: DRABBLE; C. Middle Irish drab, dregs, probably akin to the Celtic source of DRAB2. 4. Suffixed extended
382:blind: TYPHUS; TYPHLOSOLE. 11. Extended form *dheubh., “beclouded in the senses,” in suffixed o-grade form *dhoubh-o- in: a. Germanic *daubaz in Old English déaf, deaf: DEAF; b. nasalized form *dhu-m-bho- in Germanic *dumbaz in Old English dumb, dumb: pumps; c. Germanic *diibén- in Old English *dife, dove (< “dark-colored bird”): DOVE!. 12. Extended zero-grade form *dhwel- in: a. Germanic *dwelan, to go or lead astray, in Old English dwellan, to deceive (but influenced in sense by cognate Old Norse dvelja, to tarry): DWELL; b. Germanic *dulaz in (i) Old English dol, dull: DoL- DRUMS (ii) Middle Low German dul, dull: (DOLT), DULL. 13. Extended zero-grade form *dhwes- in Greek suffixed form *th(wjes-es-, smoke, whence Greek *th(w)es-es-yon, becoming theion, brimstone, sulfur: THIO-, THION-. 14. Perhaps Old English docce, dock (< “dark-colored plant”): Dock‘. 15. Perhaps Irish did, pipe: DUDEEN. [Pok. 4. dheu- 261.] dheu-2. To flow. Germanic *dauwaz, dew, in: a. Old English déaw, dew: DEW; b. compound *melith-dauwaz, “honeydew” (see melit-). [Pok. 1. dheu- 259.] dheu-’. To become exhausted, die. 1. Suffixed o-grade form *dhou-to- in Germanic *daudaz in Old English déad, dead: DEAD. 2. Suffixed o-grade form *dhou-tu- in Germanic *dauthuz in Old English déath, death: DEATH. 3. Suffixed o-grade form *dhow-yo- in Old Norse deyja, to die: DIE}. 4. Suffixed extended zero-grade form *dhwi-no- in Germanic *dwinan in Old English dwinan, to diminish, languish: DWINDLE. [Pok. 2. dheu- 260.] dheub-. Deep, hollow. 1. Germanic *deupaz in Old Eng- lish déop, deep: DEEP, DEPTH. 2. Germanic expressive denominative *duppjan in Old English dyppan, to im- merse, dip: pip. 3. Parallel root form *dheubh- in Ger- manic *deub-, *dub- in verb *diibjan in Old English dyfan, to dip, and difan, to sink, dive: pivE. [Pok. dheu-b- 267.] dheubh-. Wedge, peg, plug. Germanic *dub- in: a. Old English dubbian, to tap, strike (with a sword): DUB); b. Low German dubben, to hit: puB?; c. Germanic di- minutive *dub-ila- in Middle Low German dével, peg: DOWEL. [Pok. dheubh- 268.] dheugh-. To produce something of utility. 1. Germanic extended form *duht- in Old English dyhtig, dohtig, strong (< “useful”): DOUGHTY. 2. Suffixed form *dheugh- os- in Greek teukhos (< *theukhos), gear, anything produced, tool: HEPTATEUCH, HEXATEUCH, PENTA- TEUCH. [Pok. dheugh- 271.] dhghem-. Earth. 1. Suffixed zero-grade form *(dh)ghm-on-, “earthling,” in Germanic *gumén- in Old English guma, man: BRIDEGROOM. 2. O-grade form *dhghom- in Greek khthon, earth: CHTHONIC; AUTOCH- THON. 3. Zero-grade form *dhghm- in Greek khamai, on the ground: CHAMAEPHYTE, CHAMELEON, CHAMOMILE, GERMANDER. 4. Suffixed o-grade form *(dh)ghom-o- in Latin humus, earth: HUMBLE, (HUMILIATE), (HUMILITY), HUMUS; EXHUME, INHUME, TRANSHUMANCE. 5. Suffixed o-grade form *(dh)ghom-on-, “earthling,” in: a. Latin homé, human being, man: HOMAGE, HOMBRE!, HOMINID, HOMO!, HOMUNCULUS, OMBRE; BONHOMIE, HOMICIDE; b. (in part) Latin himdnus, human, kind, humane: HUMAN, (HUMANE). 6. Suffixed form *(dh)ghem-ya in Russian zemlya, land, earth: SIEROZEM, ZEMSTVO. 7. Full-grade form *(dh)ghem- in Persian zamin, earth, land: ZAMINDAR. [Pok. ghdhem- 414.] dhghut-. Fish. Greek ikhthus, fish: 1cHTHYO-. [Pok. ghdha- 416,] dhgh(y)es-. Yesterday. Suffixed (comparative) form (dh)ghes-ter- in Germanic “ges-ter- in Old English geo- stran, giestran, “yester-”: YESTER-, (YESTERDAY). [Pok. ghdhies 416.] dhgvhei-. To perish, die away. Zero-grade form *dhgvhi- in Greek phthinein, to die away: PHTHISIS. [Pok. gthdhei(a)- 487.)
1526:FOLIAGE bhel-3 FOLICOLOUS _bhel-3 FOLIO bhel-3 FOLIUM bhel-3 FOLKMOTE mdd- FOLLICLE bhel-2 FOLLICULITIS bhel-2 FOMENT dheg¥h- FOMITE dheg¥h- FOND? bhudh- FONDANT gheu- FONDUE gheu- FONT! dhen-1 FONT? gheu- FOOD pa-
1534:FOUND! bhudh- FOUND? gheu- FOUNDER bhudh- FOUNTAIN dhen-! FOUR kWetwer- FOURTEEN kWetwer- FOURTH kWetwer- FOWL pleu-
2372:THENAR dhen-2 THENCE to-
=== font:
377:dapper, heavy, strong; later quick, nimble: DAPPER. [Pok. dheb- 239.] dhegvh-. To burn, warm. Suffixed o-grade form *dhogvh- eye- in Latin fovére, to warm, cherish, foment (> fomen- tare, to foment, and fomes, tinder): FOMENT, FOMITE. [Pok. dhegth- 240.] dh@(i)-. To suck. Contracted from *dheoa(i)-. 1. Suffixed reduced form *dhé-mnd- in Latin fémina, woman (< “she who suckles”): FEMALE, FEMININE; EFFEMINATE. 2. Suf- fixed reduced form *dhé-to- in Latin fétus, pregnancy, childbearing, offspring: FAWN, (FETAL), FETUS; EFFETE, (FETICIDE), SUPERFETATE. 3. Suffixed reduced form *dhé-kundo- in Latin fécundus, fruitful: FECUND. 4. Suf- fixed reduced form *dhé-no- in Latin fénum, faenum, hay ( < “produce”): FENNEL, FINOCHIO; (FENUGREEK), SAIN- FOIN. 5. Perhaps suffixed zero-grade form *dhi-lyo- (< *dhia-lyo-) in Latin filius, son, and filia, daughter (but these are equally possibly from the root bheue-): FILIAL, FILIATE; AFFILIATE, HIDALGO. 6. Suffixed reduced form *dhé-lo- in Latin fél(are, to suck: FELLATIO. 7. Suffixed reduced form *dhé-l-ik- in Latin félix, fruitful, fertile, lucky, happy: FELICITATE, FELICITY; FELICIFIC, INFELIC- Ty. 8. Suffixed reduced form *dhé-ld- in Greek thélé, nipple: ENDOTHELIUM, EPITHELIUM, (MESOTHELIUM). 9. Suffixed reduced form *dhé-l-u- in Greek thélus, female: THEELIN. [Pok. dhéi)- 241.] dheia-. To see, look. Variant form *dhyd- (< *dhyag-) in: a. suffixed form *dhyd-mn in Greek sémeion and séma (stem sémat-), sign: SEMANTIC, SEMATIC; SEMAPHORE, SEMASIOLOGY, SEMEME, SEMIOLOGY, SEMIOTIC; b, San- skrit dhydti, he meditates (< “he observes mentally”): ZEN BUDDHISM. [Pok. dheis- 243.] dheigh-. To form, build. 1. Germanic *daigjén in Old English d%ge, bread kneader: DAIRY. 2. Germanic *-dig- in Old English compound Aléfdige, mistress of a house- hold (< “bread kneader”; Al#f, bread, loaf): LADY. 3. Ex- tended o-grade form *dhoigho- in Germanic *daigaz in: a. Old English dag, dough: pouGH; b. Old High German teic, dough: TEIGLACH. 4. Suffixed zero-grade form *dhigh-ird, in Latin figira, form, shape (< “result of kneading”): FIGURE; CONFIGURATION, DISFIGURE, PRE- FIGURE, TRANSFIGURE. 5. Nasalized zero-grade form *dhi-n-gh- in Latin fingere, to shape: (FAINT), FEIGN, (FEINT), FICTILE, FICTION, FIGMENT; EFFIGY. 6. Nasal- ized zero-grade form *dhi-n-g(h)- in Greek thinganein, to touch: THIGMOTAXIS, THIXOTROPY. 7. Suffixed o-grade form *dhoigh-o- in Avestan daéza-, wall (originally made of clay or mud bricks): PARADISE. [Pok. dheigh- 244.] dhel-. A hollow. 1. Germanic *daljé in Old English dell, valley: DELL. 2. Germanic *dalam in Old English del, valley: DALE. 3. Germanic *del- in Old Norse dzla, wooden gutter on a ship: DALLES. [Pok. 1. dhel- 245.] dhelbh-. To dig, excavate. Germanic *de/ban in Old English de/fan, to dig: DELVE. [Pok. dhelbh- 246.] dhembh-. To bury. Suffixed zero-grade form *dhmbh-o- in Greek taphos (< *thaphos), tomb: CENOTAPH, EPI- TAPH. [Pok. (dhembh-), dhmbh- 248.] dhen-'. To run, flow. Suffixed o-grade form *dhon-ti- in Latin fons (stem font-), spring, fountain: FONT!, FOUN- TaIN. [Pok. 1. dhen- 249.] dhen-2. Palm of the hand. Suffixed form *dhen-r in Greek thenar, palm of the hand: THENAR. [Pok. 2. dhen- 249.] dher-1. To make muddy; darkness. 1. Suffixed form *dher-g- in Germanic *derk- in Old English deorc, dark: DARK. 2. Suffixed zero-grade form *dhr-egh- in: a. Ger- manic ‘suffixed form *drah-sta- in Old English drés, dregs: pross; b. Germanic *dragj6 in Old Norse dregg, dregs: DREGS. 3. Suffixed extended zero-grade form *dhro-bh- in Germanic *drab- in: a. Old English dreflian, to drivel: DRIVEL; b. probably Low German drabbelen, to paddle in water or mire, draggle, akin to the Low German source of Middle English drabelen, to draggle: DRABBLE; C. Middle Irish drab, dregs, probably akin to the Celtic source of DRAB2. 4. Suffixed extended
```


## [2026-09-05T18:32:14.798Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"dam\\.\\|daxma\\|dmainya\\|δmainya\\|dam-\" BRT.txt | head -40",
 "description": "Grep Bartholomae for dam"
}
```


### [2026-09-05T18:32:14.853Z] TOOL RESULT

```
2554:nominale  Beifügung;  in  den  meisten  'tat  .  .yat  a:£'ar3t>m  Yt.  J9.48;  46;  — Fällen  entspricht  unser  bestimmter  Artikel  'te yä  spö.jataca  .  -  V.  7,  3;  —  Ue yöt  spatui (schwachtoniges  'der');  a)  adjektivisch:  V.ij.ai,  22,  43;  —  'taisqm yöi gius  sar?- caiti  'te  mi>fa  tava  yat  ahurahe  mazdat  oanqm  V,2.4i;  Ytj.9,  12;  —  'lat?hqm "wie  vielfach  sind  deine,  des  AhM.  Ver-  (GPm.)  yat  myazdanqm  N.  6j;  —  ku>a träge?"  V,4,2;  —  "te  daxma  .  .  aniarSt  (Stverz.)  ti  v>r>zyqn  He  yöi  masdayasna naSmät  iarürirva  V.5.51;  —  i-.a  Vam  ;  V.  5,  i  o  usw. ;  42,  J.18",  (/.3,  26,  9.49, (APm.)  aJsnt^m(s±)..paiti.bar,ltN.ioj;'—  *Vd.i8-20i;  —  't^m  (als  ASn.)  .\  yat °tayä  urvarayä  älan»irfs'V.8.i$;N.6j,'Vd.\spiln~'  .  .  X.ij.sS.  2)  auf  ein  Relati-
2769:mit  pairi  1)  'ringsum  absuchen,  auf- lesen': mazdayasna  aitihh  zimß  pairisa- yanta  (Opt.)  . .  varfsqmca  (als  Obj.)  ..yezi nsit  pairiianie  . .  astqmca  7-arpsqm:a  .  . V.  ö.  7f. 's\  z)  'herumsuchen  nach  — , aussuchen,  auslesen':  asstnanqm  xraoldva- nqm  .  .pairlstanqmY.i4.4'i'>;  A.3.5'^; —  uxtiitn  srlr>m  pairisttm  F.^^f'*'; V.J. 42  PüZ,;  —  pairi  daxma  aSlayqn  vi daxma    calsayqn   Y.S.z.  a)    mit    Dat
2798:auf  ein  relativisch  angeschlossenes  Nomen vorausweisend:  >o/<iW:4a/  sp3  urupis  fuai -so  spl  yS  urupis  .  ,  V.5.33;  —  ufa  vä nasus  raz'iwst  .  .  'sa  Jruxi  yä  ttasus  V. J.14;  5.27,  28,  7.1—4,  *.i6,  41',  9.40, 48;  —  ä^ravaium  yaoida^o  ,  .  'so  nä yö  yaoid.1>ryS  V.<).  37— 39;  40,  42,  If). 21,  Vd.iV.  10.  b)  substantivisch;  aStacTva daxmaisva . .  "sö  zl  asH  äaivanam  rapakö V.  7.55f.;  —  daxme  .  .  yat  °/a  pqsnu ra^'>a'.J/(sd-)  V.  7,49f.;  —  aisa  y5..aiwi.- >r}lti^ätus  (sd.)  *aivayaHi  -io  barfsmö.- sbrfiti  ratufris  N.  /Oj;  —  slaotaca  (sd.) yasnäica  . ,  yat  °sa  ahurake  mazda  "Pre is- lieder  .  .:  das  des  AAM."  Vr.if.ö;  6;  — jtal  ..  kmntiit  ava  hö  mirysüe  anJmltÖ si  'SÖ  , .  "wenn  er  . .  operiit  (und)  der foperirte)  stirbt,  dann  ist  er  disqualifizirt.." ^'■7-37;  —  iD  Kongraenz  mit  dem  Prae- diltkt;  cit  ai-at  vacö  äs  ,  J  baya  °h  3s ahunahe  vairyehe  "Was  war  das  für  ein Sprach  .  .?  Das  war  das  Stück  A/iV." 'W  i<).  I  —3,  o)  öfters  zugleich  auf  ein
3080:Vt/^fl.^ö;  — ^=7.7(APn,)  i>yej.!  Y.J7.14;   aaaih-a  daxmaiha   kqm.batainti  axlUca
3882:•  j.  aiwi.varSta-  Adj.  (fem,  "/(-)  'be- regnet, worauf  es  geregnet  hat':  vlsp3m\ a  ahmät  nasunam  -a  'ianqm  daxmanqmca ' 'tanqm  hixranqmla  'tanqm  vayanqmüi frariuhantanqm  "bis  dass  es  auf  die  Leich- name geregnet  und  .  .  und  auf  die  Lei- chenausscheidungen geregnet  hat  und  bis die  Vögel  (Alles)  aufgefressen  haben"  V.  ]
5048:Schlacht  gehefert"  Bh.  j.3;  usw.  c)  be- gründend 'aus  den  angegebenen  Grün- den, folglich,  in  Folge  dessen'**:  paurvB yat  ditn  usca  usdvanayat  .  .  %raitaonö  .  . hS  °%a  vazata  %ri.ayar3m  ", .  der  schwebte in  Folge  dessen  .."  Ytj.öiC;  —  ai-a •  ].,  p.  ava'^a  Adv.  I)  'de,  ita';  1)  ver-  ait)m  nmä/am  baraytn  °%a  iriststn  hirt- gleichend  'so,  ebenso';  ein  Nebensatz  mit  zayin  "so  sollen  sie  die  Behausung  weg- y<^a  'wie'  geht  voraus  oder  folgt:  l_>'a;ia-  tragen  (und)  folglich  den  Toten  dalassen" sam  ..  ahaAya^  '^ä  *aiunavaya"i3  Bh.  V.  Ä  3;  a;  —  vTspe  fyrisfnti  pinnine 1. 8;  —  yd^a  .  .  hvanxhStm  .  .  fraca .  »&«  mOvayacit  .  .  tinsttUu  (sd.)  YL  14. aiti  ahvica  vazaite  ..  °^a  az»mHf  ..  a/a-.^Z.  4)  'desgleichen,  item';  pagtryäi säniYtio.iiS; — }ydh3 paruvamay  °%ä' mdarftayfn{sA)  af^nitäyukim  °>a  ätrpm Bh./,i4';  4.4,5.2;  —  \- iyam  yuviyS  {sA.)  V.J5.48;  —  mairyS  drva  bizangrB  "äa akäniy  *°^<J  *ya'iä  adam  niyastäyam  D.  ahmaoys  V. 5.35;  — JvS  nanm  ..  Jainli i-/.y,  — yimö  °'^a  kmnaot  yaia  dim  nsit  ''ha  m^nts  V.J. 37;  38;  —  ä'hrö *iiasaf  ahurö  V.  2.32;  i8.-t,t,  35,  38,  ir).  ahurake  . .  °^a  näirikayäi  V.  15.45  Gl.; 33.  a)  vorausweisend 'folgendennassen,  Vd.  2.  11) 'in  einem  solchen  Fall,  unter alio'-.lhauv  karahy3 'hä  adurußyt^  adam  solchen  Umständen':  yat  ..  spä  ahqm.- hardiyc^  amiy  Bh./.ii;  16,  2.3,  5,  ^.x'^}  baöhimtöS  vä  bavaf..°'ha  Al baeidz^m(sd.) 1.16,  2,14,^.5;  —  y-UOT  (sd.)  ..  aduru-  .'.  upi^isayffi  Y. IJ.35;  15.48.  in)'dort's'; jiya*  -hiJ  a%ah<^  adam..  amiy  Bh.  b— j';^,fs  'ha  dasiam..vlbarai  aHaisva  var>ßva 4.29;  —  '^äidiy  a>aAam  paraidiy  "so .  "wer  hat  dort  die  Rehgion  verbreitet..?" befahl  ich  ihm;  'Zieh  aus  . .'"  Bh.j.3;  V.  2.42;  39.  [Vytj^:  lies  'S«".] 9,  14,  2.6,  7,  10,  14;  —yadiy  '%a  *mam-  Ableit.  —  Eig.  'auf  jene  Weise'.  —  wo*s. yüAay  hacä  aniyanä  mä  tanam  D.5.3;Bh.  |  "^ä.  —  Pü.:  ää«,  (mV.  3.  42):  fiar^ 4-l'A — "''^  °^^  marthanS:  ..  Yt.lp.47;  — AS'':ba  vyaxmanyala:..  Yt/p.43-  a)  mit folgendem  _j'fläa  oder^ai  'insofern . .  als
6012:ni/antlni  Ytß.  54;  18,  22',  26,  30,  42,  50, 54,  lOS,  117,  130,  p.4,  9f.s,  18,  22,  26, 72.2,  74- 58',  75.3,  28,  32,  Vytao»,  21, 4ß;  —  da%äni  ti .  ,  kazannm  .  .  uta  Ig 'S3m  äfrinäni  ..  Y.22.4L;  YL5.63;  — j/ai  mam  iura  paedayanta  .  .  äai  'stm tanüm  aguze  .  .  äai  tnam  fraguzayania  . . Yti^-SS;  56;  —  kü^a  tl  'um  varsm i?rjnavane  V.  2.  $t ;  lff.12,  22.6',  Ytij. 57;  —  't?m  II  g<K%ä  frähoyeni  'z?m  .  . 'Z3m  V. 2.5;  27.6,  7,  Vr.j.7;  —  \valnä a''ur(^mazdäha''  'dam  xsäya%iya^  amiy . . 'damsäm  xs'äya^iyi^  aham  Bh.  7. 5!;  — iyam  gaumätJ'  ,  .  avahä  a%ak(r  'dam baräiy^  amiy  . ,  'dam  xl3ya%iye^  amiy Bh.b;  c-j",  7.11,  13,  i6',  2.3,  s,  14,  J-S. 13;  1^2^;  —  ima'  tya'  'dam  akunavatn vasnä  J'ur^mazdäha'  ah/^ ..pasavJ' ya%ä x^aydiiiyJ'  abavam  'dam  19  hamaranä akunavam  vasnä  t^un^mazdäht^  'dam- säm ajanatn  uta  9  xssyaHyä  agarbäyam Bh..^.  2;  — pasäv^  'dam  t^urt^tnazdäm patiyävahaiy  a^urJ'matdämaiy  upastsm abar(^  .  .  avähä  'dam  . .  gaumätam  .  . aväjanam  . .  avadasim  aväjanam  x/a- %''amHm  °dam  adrnam  vasnä  a^urc^maz- dähc^  'dam  xsilya'^iyaf'  abavam  J'ur^- mazdä  x/ä^^am  manS  Jrsbara^  Bh.  J.  13; 14';  —  'damsaiy  uta  ftaham  .  .  frajanam ,  .  pasävJ'  'dam  .  .  uzmayapaiiy  akuna- vam Bh.  2. 13;  — pasävtrsaiy  'dam  ulä näham  .  .  fräjanam  ,  .  pasäve^sim  ,  ,  ut- mayäpatiy  akunavam  fih.2. 14;  —  °dam (s.  I  b)  xläya%iy^  amiy  vasna  c^urt^- mazdäha/"  'damsim  *g'a^avä  niya/ädayam tya^/äm  'dam  a%akam  avc^  .  .  D.  ö.  4 ; 3'.  5>  4-1,  5-2.  ^7-3^  Bh.  j.is,  16,  17', 18I,  19',  2.1',  2,  4,  6',  7,  9,  10,  II,  12*, 13,  Bh.^.  I,  2,  6,  8,  13,  14,  4.4,  6,  8, 12,  IS,  18,  5.1%  X.7.3,  ^.311.  Die Übrigen  Siog.-Kasus  des  Fron.  i.  Fers. s.  unter  ^ma-.  [¥.4:^.14;  lies  a&;  — Yt.  7.29:  lies  zamarf.'j
7794:Komp.;  ä-\-*antay.,  %  2i)8.  7.  —  Vgl.  iSt.  Bthl. IF.  7.  59, —  Pü.;  äyisn  11  SaTihi  i  vFn,  Npil.; ämadait  11  hidaii  i  dam.
8636:•  j.  uz-daeza-  m.  i)  'Aufschütten  von Erde,  Aufmauerung' :  yat . .  paili  . .  daxma -za  kiryeinte  "wo  Leichenstätten  durch Erdaufechüttung  errichtet  werden"  V.j.9 —  y^t  ■  ■  P"'''  •  •  daxma  "-ta'l  *2'7kante
8638:(sd.)  V.J.13;  —   aaaih'a  daxmaih-a  .  .
8721:•  j.  uäi.dam-,  u§i-dain-  tn.  Name  eines Gcbirgs*':  ahmat  haca  garayS  fraoxiyan '0.1  (NS.)')  usi.äar?nd  {i±)  Yt/^.a;  — gairis  yU  °6<j  Yt/p-66;  —  aom  gairuii.. yim  °dam {fuS.y*  usi.darfmm (sd-)Mt.  1.2S.
8927:mit  rf  'zu-,  herrichten':  *pmri  daxmn aisayan  vT  daxma  caisayan  "nach  I^ichen- stätten  sollen  sie  sich  umsehen,  Leichen- stätten sollen  sie  herrichten"  V,  cV.  2,
9063:mit  7'i  'durch  Graben  beseitigen,  ab- tragen; zerstören':  yasca  .  .  daxmatiqm avavanhm  maz3  vtkanayät  ya>a  .  .  V.  7. 51 ; — yat  b.J  paiti  fra!st.>m  daxma  uzdaSza (sd.;  lies  vrd')  vJkanü  (3SPA.)  yahmya  . . "an  welchem  Ort  man  am  meisten  die  D. durch  Abtragung  zerstört,  wo  .  ."  V.  y. 13;  —  yat  bü  paiti  fraüittnt  vikmte (3SPM.)  .  .gjmam  V..J.Z2;  —Wäyadanä (sd.)  tyä  gauiii'ätJ'  . .  viyakai'  (3SPrA.) Bh. /.  14;  —  kyt^  aparam  imilm  dipim vaitnhy  ..  maty^  (sd.)  vikanähy^^  Bh. 4.  15;  16;— _jW;>  imrim  dipim  ..vainähy '.■ikanähidisi^  Bh.  4- 1 7  II  ■
10289:'essen',  von  den  Dasva:  aste  yöi  dagva aitaisva  daxmaisva  gan/i)nti  apäca  vae- pmH  ya>a  .  .  V.7.SS.
11922:daxmaliva  hqm.bavainti  axtilca  garmusca 'ftusca  V.  7. 5  7 ;  VyL  50 ;  —  paiiistätse  gars- näuica  'naoica  Yt  y,  1 3 1 ;  —  apa.ävarata 'nu  Yt.^.8;  1 1 ;  —  paitistätSe  dazu  . .  'nu V.20.3.  a)Plur.mitGS.  a^rö(Sp.3i4  0.) 'Fieberanfälle';  k3 paoirys  a%rS  'nus(AF.) dürayat  tanaot  hata  tnasyehe  V,  20. 1,
12459:•  j-,  g,  'daeva-  m.,  j.  'daevi-''  f.  I)  im gAw.*'  Bezeichnung  f��r  die  Gottheiten der  vor  Zard^ustra  in  Iran  geltenden Religion:  cüma  .  .  Auxs'd^rä  (sd.)  °vä änkarS  .  .  aiibyS  kam  y.lis  gam  karapa usixt^ä  (sd.)  aehmtli  dstä  Y.  44-  *o;  — af  yaf  'vä  (VP.)  vtspitshö  akat  (sd.)  ma- nanha  sta  H^rsm  Y.^2. 3;  i;  —  aya (naml.  mainiva)  nSit  »ris  vSsyilta  °väcinä hyal  Jf  a-d^baoma  (sd.)  , .  upa.jasal  Y.  30. 6;  —  hya^  vi  .  -y^ns  °vSng  akaslä  main- yus  . .  syao%aiiim  ..fracinas  . .  x/ay^(sd.) Y.  J2.  5;  —  sas^ärS  (sd.)  .  .yä  zl  väv>rs- z5i  . .  °väUiä  masylisca  Y.  2p.  4;  —  hyat '"qsasutä  (sd.)  yii  daibitanä  (sd.)  fraoxti, 'iäilla  masySiicä  Y.  4^1;  —  par}  *v3 . . vacxsma  "väisca  xra/strais{sA.)  masyäiscä Y-^4.  5;  verwendet  Y.  75.  a;  —  yastä °ving  apars  masyqscä  tarS.mqsta  Y.  4^. II.  a)  GP.  mit  dam-  m.  sva.  drüjs dam-:  tsi  'VMg  (GP.)  dqn  \3  dngvais dama  (sd.)  Y.  4r).  4,  11)  'im  jAwr.* 'Dämon,  Unhold,  Teufel':  t&m  z^margüti
12460:'äkirsnvS  vJspe  'va  zardhufira  yBt  para akmät  vtr5.rai^a  apataypn  paiii  äya  amS "du  hast  bewirkt,  dass  die  D.  sich  alle  in die  Erde  verkrochen,  die  sich  zuvor  in Männei^estalt  auf  der  Erde  herumtrieben" Y.p.  15;  FrW.4.3;  —  valtumnsm  akmat para  "va  patayjn  .  .  *apaJtarlay?n  (sd.) fainis  haca  maiyakaHbyS  aal  tä  .  .  hazB nivarKaym  (sd.)  'va  äat  tl  aivS  ahunS vaifyS  .  .  *zamangusa  avasai  vXipe  "va ayesnya  avahmya  Yt.  ig.  Za{.;  — ansürahe (sd.)  grlvaya  .  .  yat  ahmya  °va  handva- nnti  druj5  haca  girihSha  Y.^.j;  ig.44;  — alte  yei  "va  aBaisva  daxmalsva  gaafanü apaca  valpptttiY.j.$$; — Jha  'vanqm  han- dvarMS  kva  'vanqm  hantpatanS  kva  '-va hqmjivannti . .  /  . .  altaihßa  daxntaisva . .  V. 7.53 f.;  54^;  —  öAva  vyari%aAva{s,d.)  zpmS
12594:•  j.  daxma-  m.  'Leichenstätte,  Leichen- bestattungsort'*':  'ma  (NP.)  .  .  yaAmya nar/f  irista  niiayeinte  V._9.  9;  13;  —  sairi ..  triste  °me  nihätte  V.  7. 49;  —  avi  Ai irista  tanOm    upa    "ma  fraiaröis  \A.i2;
12598:LcE  Parsii  206,  der  auch  Abbildungen  gibt. El?    VII.   eig.  'Verbrennungsslälte',   mm  V. dag-,  %  33  h.   —    np.  daxm,  daxma.  —    Pä-: daxmai,  in  F.  mit  der  np.  Erl. :  gär  mäna  dar an  matdagän  rä  barajid.
12738:•  j.,  g.  dam-  (:  -d»/!-)  m.  'Haus,  Wohnung' : hyat  k5i  aia  vohucä  cOiH  (sd.)  manaukä xlakröi    hSi    haurvätä    amintätä    ahmäi
12844:•  j,,  g,,  p.  3dar-  V.  'halten;  fassen'. Praes.  i  ä3n-,  dr-,  2  dam-  (?),  4  dara-, 5  däiär-'^,  16  (Des.)  dtdar^Ia-''^,  20  'dru-3\ 24  daraya-(?),  30  (Iter.)  däraya-,  30  +  27 (Pass.)  *'d3rya-''^;  PrP.  adariy;  Perf.  i da^är- :  dadr-,  dalr-,  1  dädr-\  J-Aor,  i dänr- :  dars:  ~  PPfP,  d^r^ta-;  Inf.  dar»- dyai,   dar?hräi,  därayS;  Absol.  dtnigm.
13047:Dnd  in  AkM^  'Hans'  Tcrwahrt  werde-  i.  dam-\ mit  No.  3,  'pä^y  mit  No.  4  -,  wUuend  er  «Is  1 Richter  {ralav-)  die  eDdeiltiKe  Ohnniacbt  der  | .ZVH«"Welt  fesutetlt  und  die  endeiltige  Hemcluft  i AkM^  I
13235:—  tairlm  gäma  (sd.)  frabarat  .  .  urva anayragiva  raocöAva  mdarjät  H.  2. 1 5 ;  1 5^, 33;  vgl.  f;  —  yavat  .  .  kangmrvayqn altavat  . .  Au/ie  (sd.)  zpme  nidaiiyan  V. ''■  29;  31;  —  Ja/W  (sd.)  . .  WM?  nihaite (NDf.)^'>  V.7.45;  49;  —  taohri  ..  ta Als  dasva  garS  nmätu  Yt.  /0. 3  2 ;  —  at  Asi vaAmSng  dfmäTig  garS  (sd.)  nidämä  Y. 45-  8;  —  mi^ma  . .  yaAmt  vyäne  (sd.)  . . masfl  amava  niiälim  Yt./o.64.  b)  wo?- Adverb:  kva  narqm  iristanqtn  tanom  ba- räma..kva  nidäiiäma  V.6'.44;  —  astala . .  tanüm  nidai^yan  V.5, 12;  —  daxma  . . yaAmya  narö  irista  tmayeinte  V,^.  9;  • — an'öpäo  m  nidaiaite^  a/is  .  .  *aniar?.- ar^i^m  nmSnoAe  Yt  iS.  4.  c)  Instr. : Aiiu  pqsnu  (sd.)  gitu  niaayaila  V.  16. 2.  d)T>3X.:  ai^ä  aAmäi  varmüi  ..nidä- tfttt  ahm  süiäyäi  tkalsäi  (sd.)  rSiayeAAf druxSY.4S-Z''  —  amtmca  Vfr^^rayti^mca ni'jät>m  tanuye  Yt  14.  38.  e)  Gen.: huskanqm  (näml.  alsmanqia,  als  Obj.)  . airiAa  S3ms  (sd.)  niäaÜyqn  V.  7.  29;  — aSa^qm:a  (näml.  Aaoliianqm,  als  Obj.) zftitö  nidaiiyqn  antarfin  ar?wtn  nmänaAe V.  6".  43;  -—  äat  vohu  maiiB  nidatoTi.. raocaukiim  yat  Ae  stärqm  aiwi.raocayantt "dann  sollst  du  (ihn)  .  .  dem  Licht  aus- setzen, damit  . ."  V. /^.  23.  f)/(7jÄund Lok. :  paoirim  gäma  (sd.)  frabarat . .  urva Attmate  paiü  nidaläl  H.  2.  15;  15';  vgl.  a,
13515:g.  däkvtt-.  %.  unter  dam-.
13565:Ablcit  —  Zum  V.  dam-.  —  S.  djriii'.  —  d. Tgl.  di-dAä-  Adj.  'fest'.  —  Pa.!  laxl.—  ■)  So {dr?a-')  nur  F,  14;%  26S.  39.
13598:g.  dqn:  ».  unter  dam-  (V.  4S-  'O.  49-  4)  und
13853:Pü.:  duidam.
13998:•  p,  *duvitä-taranam  Adv.  'seit  langem  wie? Adv.  und  folgender  dir.  Rede:  kam' eine  Reihe  bildend,  seit  langem  einander  1 . .  käram  aväiä  adurußya*:  adam..  Jih. folgend':  g  duv  vayam  xsäyaiiyä  amaAy'  i.  16.  4)  'böslich,  dolos  handeln,  (je- "Rönigesind  wir  neun  seit  langem  einander  mandem)  ein  Arg  antun',  absolut:  kaäa- folgend"  Bh./.3.  \{%i.ya  pars  druiintö  (tiP.)  YtÄs;    —
14018:(Gen.  statt  Dat)  vorlügen',  mit  wie  ?Adv.-  dahyauva  vasiy  (sd.)  aiara^  Bh.  ;.  10;  — MnAio\g.^vc.'B.eAe.:ÄauvMSrahyaara>il  i,„.j,„  dahySum  .  .  pstuv  hacä  hainäyä adurujiy^:  adam..  Bh./.ii.  3)  'Je-  j,ai,j  .^,j*  D.4-3;  Bh.^-S:  — '""J«  '^'"*-
14952:Znm  V.  dam-.  —  Pü.t  aparuiand,  erl.:  in  1 hai   ii  ap^i  i  yuf  batt  istil,   —   >)  Variante
15580:Ableit.  la  pairi.\-ga{%ä-;  vgL  No.  1.  —  Pü.: ape    rasim    S   in  i  imäi    Hyäyisn   ckrmatd  .  . 111/in  anjar  garöttnän  itäjrem,  —    ')  Ich  ver- weise für  meine  Fassung  des  Worts  und  der ganien   Stelle   auf  V.  38.  11  (s.  '/J(j>   mit No.  4),  4g.   10  (s.  dam.  mit  No.  3I,  37. 13  (s. äii^ar-*)).   Der  ■heilige  Mann'  ist  ZitmäHi/rit, der  'gute  Sinn'  seine  Anhingenchaft;  f^röbS ifiiqm  ergänzt  mamiifkä  und  i(j^SflM  tu  der bekannten  Drei  bei  t. •  j.  ■•■pairi.gä.-vacah-"  Adj.   'der   seine Worte  ringsum  singt,  d.  L  ettönen,  erklingen lässt':    kaomS  /räimil . .  hvaca  päpB.vach •/J  Y.  57,  30,
15947:frä  ist  Wiederholung  aus  dem  Vorhergehen- den, wie  auch  die  Stellung  von  aSa  (sd.,  No.  5) ausweist.  —  «  Vgl,  V.57.  2S  und  No.  3.  — 5)  S.  iSt.  unter  dam-,  daidar-  and  pairigae'i.a:
16760:bavam  aiwi-sasis  aiwiJmantB  "wenn  ich in  Worten  und  Gedanken  verwünscht werde"  Yt74. 34;  —  iS«  frikiä  paiti.- zantä  buyata  "hier  sollt  ihr  geliebt  und gern  aufgenommen  werden  (sein)"  Yt 13.  147;  —  altallva  daxma^a  .  .  yöi paiti  äya  zima  bavainti  vzda^a  usdista "in  diesen  Z>.,  die  auf  der  Erde  aufge- schüttet werden  (sind)"  V.  7.  54;  —  aat hl  im  za  bvat  psrme  .  .  "drauf  ward ihm  die  Erde  voll  .  ."  V.  2.  8;  —  ana buyä  savanS.sasta(sd.)  ana  buyä  huyaita- tara  (sd.)  Yt  5.  9;  — yif  bavaiti  xratu.- käts  (sd.)  Yt  13.  16;  —  yai  */ranata bun^^  N.  65(?);  —  liu'ha  nmäwm  yaoe- da%ani  iuäa  bun^^  (näml.  nmana)  yaos- data  "wie  kann  ich  das  Haus  purifizi- ren?  wie  können  (die  Häuser)  purifizirt werden?"  V,  72.  2;  77.  a,  72.  3,  75.  33*, 20.  a)  negirt:  yai  St  bavainti  *ana-
16816:mit  ava  1)  'hinab-,  hineinbringen':  y5\      mit    a»/    und    a    'etwas   herzubringen »otJ  ft'jW  kar^ä  frakarayäti  ava  iha  ba- '  zu  — '  (Akk.):  yat  .  .   avi  ätr?m  äbannti rtnü  *yavahe  vä  "wenn  man  in  der  Erde  \  affayä  urvarayä  .  .  Yt  i4-  SS- drei  Furchen  rieht  (und)  sie  bringen  (sva,  1     mit  avi  und/rJ:  pas^aiti  avi  Al  iritta- säen)   hier   Getreide   hinein   oder  . ."  N.  tanüm   Ufa   daxma  frabarBis  Vd.  12;  —
17376:»Suff,  s.  S  20a  —  Npü.!  ai  dam.
17494:'am  meisten'",  nach  Zahl,  Menge,  Um- fang usw.:  mq%raväkahe  .  .  yS  'Um  . . a/irmairyanqm  (Gen.  part  als  Obj.) . .  ava.- jaynat  Yt  1^.105;  —  yat  ba  paiti  'hm kärayeiti  .  .  yavanqnüa  västranqtnca  (sd,; Gen.  part  als  Obj.)  V.  3.  4;  ~  yat  bä paiti  't»m  viksnte  .  .  girihqm  (Gen.  part als  Obj.)  V.J.  22;  —  ya^  b3  paiti  'tim bavainü  .  .  g^rjiqm  (Gen.  Flur,  als  Subj.) V.J.  10;  —  yat  bä  paiti  't)m  malsmti pasvasca  , .  V._j.  6;  —  yat  bä  paiti  °t»m us.zlZ3nti  (sd.)  pasvasla  V,_j,  5;  — yat  bä paiti  'tim  daxma  usdaüa  (sd.)  kiryänte V.J.9;  13;  —  yat  bä  paiti  Uim  lairi nikantt  V.  j.  8;  —  yat  ba  paiti  "tsm uskfnti\.3.i2;  —  yS  't>m  apivataiU  dag- nayh  V.  g,  3.  a)  zur  Verstärkung  des Superlativs  '* :  yai  ahmi  nmäne  . .  'ttm yaozdätU.B3mö.t»n3mca  hu^ö.z3mS.t3m3mca kambistitnla  .  .  V,  5.  46^',
18506:•  j.  'naeza-  m.  Name  einer  Krankheit: aüalfva  daxmalha  kamiavamU  axtiica gannusla  tafnusca  'zasca  sSrastisYaV.j.SJ ; —  paiHstätSe  gamiSusca  tafttaolca  'sahe^a sarastSisca  Yt/J.  131.
18684:—  apqm  napät>m  .  .  yS  nirSus  daha  yO n^rfu/^i  taiasa  Yt/5.  51; — ya>a  nars vay%an?m  "wie  der  Kopf  eines  Menschen" V.ö".a2;Äa3,F.jc,P.j4;  —  narqm  näiri- nqmca  .,  ti  hrmava  mti-viaire  djyammm Visp?m  3  afimät  yat  aSe  narS  "var^/iva anhm  V.2.27C;  —  cvaiti  narqm  ..xaota ratufris  N.  20;  —  yS  narS  kimSgatvS  . . anya  dva  vä  nara  , .  3at  aSsqm  narqm  .. cvat  antari  ^mr^us^'^  V.5.27;  4.i,ä,;- — yä  nara  (NS.)  gätum  baraite  F.^d;  N. 64;  —  paoifTtn  upa  may^m  frä.nasus (sA)  nartm  (statt  NS.)  bavaiti  V.  g. j8.  A)  Gegenüber  einem  attributiven a)  Substsl,  b)  Adj.  oder  c)  Proa  tritt nar-  vielfach  so  zurück ,  dass  wir  es  un- übersetzt  lassen  können;  es  gilt  das  ins- besondre vom  NS,  nä,  der  dabei  meist in  der  Stellung  der  Enklitika  —  hinter  dem ersten  Hochton  des  Satz-  oder  Versteils  — auftritt  a)9>  cvat  na"'^  3%rava  (sd.)  .  , *parayäl  ". ,  (ein  Mann,  der  Priester  ist, sva.)  ein  Priester  .  ."  N,  ^;  —  ydha  na taxmS  ra%a2stä  .  .  kaca  saltät  (sd.)  .  . paiti.ynUa  YtiJ.Sj.  b)  tts  nä  sayeiti (sd.)  vyäxanS  Yt  13.16;  53,  V.5. 40;  — paeiryeheca  na  myatdahe  aZaiit  (sd.)  .  . raius  , .  ratunafm  ayasnXm  (sd.)  daste  A. 3.  7;  8— 12*;  —  daxma  .  .  yahmya  nars irisla  nthayänte  V.3.Q;  Vd.  2',  17,  Vyt 12;  —  kva  narqm  iristanqm  tansm barama  V.  (j.  44;  —  kat  /a'(Sp,  612) nara  iristd  . ,  nasus  upaMvqsaiti  V,  7. 1;
20165:•  j.  'mazah-  n.  i)  'Grösse,  Umfang' :  _>iaj:& .  .  daxmanqm  avavantpm  'xS  vltsnayäj ya^a  hl  tanus  aahat ". .  (soviel  an  Grösse als  . .  sva)  ein  Stück  so  gross  als  . ."  V. 7.  51.  2)  (etwa)  'Fülle':  'zJ  avahyai  °tS raßmSJiyai  däidl  hauruatä  am>r>tätü  "ge- währe zur  Hilfe  die  Fülle,  zur  Unterstützung die  FüUe  des  H.  und  A."  Y.  5Ä  7.
20393:•  j.  m«r9n£ytt,8t9nia-  Adj.  'der  am meisten  zerstört,  der  verderblichste':  aSaZsva daxma^a  masya  hqm  °ma  bavainH  pasca hü  früimSJäitim  V.  7.  58.
```


## [2026-09-05T18:32:24.510Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"dmainya\\|blähen\\|aufblasen\\|blasen'\" BRT.txt | head -20; echo \"=== DAMP/DIM in AHD:\"; grep -n \"DAMP\\|DIM \\|dhem\" AHD_watkins1985.txt | head -10",
 "description": "Grep Bartholomae and AHD"
}
```


### [2026-09-05T18:32:24.581Z] TOOL RESULT

```
13362:•  j.   däSmainya-  Adj.  'sich   aufblasend,
13365:-blähend',  von  Fröschen":  batvar»  vasaya- nam    'nyanatn   .  .   vazayanam    upapanam
13366:Eig.  PPA.  (S aoji.  5),  aas  einem  Prae».7-^  13 »>■ —  Vgl.  aL  dhämaH  'er  bläst',  np.  damidan 'blasen'.  —  Pü.;  vanfj  i  saiuTi  {Erklärung  statt Übersetzung);  dazu  die  Erl.;  Aar  ee  kt  yul  hac äp  lavSn  *iäiitl  tamlki  »gL  No.  I.  —  ')  Ge- meint sind  die  Laubfrosche,  als  Vertreter  der Landft6sche  im  Gegensatz  zu  den  WasserfrÖ- scheo.  —  ')  Ein  Praes.  auf  ainya-  mit  InL- Red,;  ganz  ähnlich  ist  gr.  jtBji^iiiVM  ans  *WJ- gebildet,  ferner,  mit  einfacher  Reduplikation, «nwra/v»  aus  *fal-  (vgl,  got.ßnpaii  und  iBcd. gr,  iIjIv  und  ai.  vindäli;  s.  H'aed-),
=== DAMP/DIM in AHD:
377:dapper, heavy, strong; later quick, nimble: DAPPER. [Pok. dheb- 239.] dhegvh-. To burn, warm. Suffixed o-grade form *dhogvh- eye- in Latin fovére, to warm, cherish, foment (> fomen- tare, to foment, and fomes, tinder): FOMENT, FOMITE. [Pok. dhegth- 240.] dh@(i)-. To suck. Contracted from *dheoa(i)-. 1. Suffixed reduced form *dhé-mnd- in Latin fémina, woman (< “she who suckles”): FEMALE, FEMININE; EFFEMINATE. 2. Suf- fixed reduced form *dhé-to- in Latin fétus, pregnancy, childbearing, offspring: FAWN, (FETAL), FETUS; EFFETE, (FETICIDE), SUPERFETATE. 3. Suffixed reduced form *dhé-kundo- in Latin fécundus, fruitful: FECUND. 4. Suf- fixed reduced form *dhé-no- in Latin fénum, faenum, hay ( < “produce”): FENNEL, FINOCHIO; (FENUGREEK), SAIN- FOIN. 5. Perhaps suffixed zero-grade form *dhi-lyo- (< *dhia-lyo-) in Latin filius, son, and filia, daughter (but these are equally possibly from the root bheue-): FILIAL, FILIATE; AFFILIATE, HIDALGO. 6. Suffixed reduced form *dhé-lo- in Latin fél(are, to suck: FELLATIO. 7. Suffixed reduced form *dhé-l-ik- in Latin félix, fruitful, fertile, lucky, happy: FELICITATE, FELICITY; FELICIFIC, INFELIC- Ty. 8. Suffixed reduced form *dhé-ld- in Greek thélé, nipple: ENDOTHELIUM, EPITHELIUM, (MESOTHELIUM). 9. Suffixed reduced form *dhé-l-u- in Greek thélus, female: THEELIN. [Pok. dhéi)- 241.] dheia-. To see, look. Variant form *dhyd- (< *dhyag-) in: a. suffixed form *dhyd-mn in Greek sémeion and séma (stem sémat-), sign: SEMANTIC, SEMATIC; SEMAPHORE, SEMASIOLOGY, SEMEME, SEMIOLOGY, SEMIOTIC; b, San- skrit dhydti, he meditates (< “he observes mentally”): ZEN BUDDHISM. [Pok. dheis- 243.] dheigh-. To form, build. 1. Germanic *daigjén in Old English d%ge, bread kneader: DAIRY. 2. Germanic *-dig- in Old English compound Aléfdige, mistress of a house- hold (< “bread kneader”; Al#f, bread, loaf): LADY. 3. Ex- tended o-grade form *dhoigho- in Germanic *daigaz in: a. Old English dag, dough: pouGH; b. Old High German teic, dough: TEIGLACH. 4. Suffixed zero-grade form *dhigh-ird, in Latin figira, form, shape (< “result of kneading”): FIGURE; CONFIGURATION, DISFIGURE, PRE- FIGURE, TRANSFIGURE. 5. Nasalized zero-grade form *dhi-n-gh- in Latin fingere, to shape: (FAINT), FEIGN, (FEINT), FICTILE, FICTION, FIGMENT; EFFIGY. 6. Nasal- ized zero-grade form *dhi-n-g(h)- in Greek thinganein, to touch: THIGMOTAXIS, THIXOTROPY. 7. Suffixed o-grade form *dhoigh-o- in Avestan daéza-, wall (originally made of clay or mud bricks): PARADISE. [Pok. dheigh- 244.] dhel-. A hollow. 1. Germanic *daljé in Old English dell, valley: DELL. 2. Germanic *dalam in Old English del, valley: DALE. 3. Germanic *del- in Old Norse dzla, wooden gutter on a ship: DALLES. [Pok. 1. dhel- 245.] dhelbh-. To dig, excavate. Germanic *de/ban in Old English de/fan, to dig: DELVE. [Pok. dhelbh- 246.] dhembh-. To bury. Suffixed zero-grade form *dhmbh-o- in Greek taphos (< *thaphos), tomb: CENOTAPH, EPI- TAPH. [Pok. (dhembh-), dhmbh- 248.] dhen-'. To run, flow. Suffixed o-grade form *dhon-ti- in Latin fons (stem font-), spring, fountain: FONT!, FOUN- TaIN. [Pok. 1. dhen- 249.] dhen-2. Palm of the hand. Suffixed form *dhen-r in Greek thenar, palm of the hand: THENAR. [Pok. 2. dhen- 249.] dher-1. To make muddy; darkness. 1. Suffixed form *dher-g- in Germanic *derk- in Old English deorc, dark: DARK. 2. Suffixed zero-grade form *dhr-egh- in: a. Ger- manic ‘suffixed form *drah-sta- in Old English drés, dregs: pross; b. Germanic *dragj6 in Old Norse dregg, dregs: DREGS. 3. Suffixed extended zero-grade form *dhro-bh- in Germanic *drab- in: a. Old English dreflian, to drivel: DRIVEL; b. probably Low German drabbelen, to paddle in water or mire, draggle, akin to the Low German source of Middle English drabelen, to draggle: DRABBLE; C. Middle Irish drab, dregs, probably akin to the Celtic source of DRAB2. 4. Suffixed extended
382:blind: TYPHUS; TYPHLOSOLE. 11. Extended form *dheubh., “beclouded in the senses,” in suffixed o-grade form *dhoubh-o- in: a. Germanic *daubaz in Old English déaf, deaf: DEAF; b. nasalized form *dhu-m-bho- in Germanic *dumbaz in Old English dumb, dumb: pumps; c. Germanic *diibén- in Old English *dife, dove (< “dark-colored bird”): DOVE!. 12. Extended zero-grade form *dhwel- in: a. Germanic *dwelan, to go or lead astray, in Old English dwellan, to deceive (but influenced in sense by cognate Old Norse dvelja, to tarry): DWELL; b. Germanic *dulaz in (i) Old English dol, dull: DoL- DRUMS (ii) Middle Low German dul, dull: (DOLT), DULL. 13. Extended zero-grade form *dhwes- in Greek suffixed form *th(wjes-es-, smoke, whence Greek *th(w)es-es-yon, becoming theion, brimstone, sulfur: THIO-, THION-. 14. Perhaps Old English docce, dock (< “dark-colored plant”): Dock‘. 15. Perhaps Irish did, pipe: DUDEEN. [Pok. 4. dheu- 261.] dheu-2. To flow. Germanic *dauwaz, dew, in: a. Old English déaw, dew: DEW; b. compound *melith-dauwaz, “honeydew” (see melit-). [Pok. 1. dheu- 259.] dheu-’. To become exhausted, die. 1. Suffixed o-grade form *dhou-to- in Germanic *daudaz in Old English déad, dead: DEAD. 2. Suffixed o-grade form *dhou-tu- in Germanic *dauthuz in Old English déath, death: DEATH. 3. Suffixed o-grade form *dhow-yo- in Old Norse deyja, to die: DIE}. 4. Suffixed extended zero-grade form *dhwi-no- in Germanic *dwinan in Old English dwinan, to diminish, languish: DWINDLE. [Pok. 2. dheu- 260.] dheub-. Deep, hollow. 1. Germanic *deupaz in Old Eng- lish déop, deep: DEEP, DEPTH. 2. Germanic expressive denominative *duppjan in Old English dyppan, to im- merse, dip: pip. 3. Parallel root form *dheubh- in Ger- manic *deub-, *dub- in verb *diibjan in Old English dyfan, to dip, and difan, to sink, dive: pivE. [Pok. dheu-b- 267.] dheubh-. Wedge, peg, plug. Germanic *dub- in: a. Old English dubbian, to tap, strike (with a sword): DUB); b. Low German dubben, to hit: puB?; c. Germanic di- minutive *dub-ila- in Middle Low German dével, peg: DOWEL. [Pok. dheubh- 268.] dheugh-. To produce something of utility. 1. Germanic extended form *duht- in Old English dyhtig, dohtig, strong (< “useful”): DOUGHTY. 2. Suffixed form *dheugh- os- in Greek teukhos (< *theukhos), gear, anything produced, tool: HEPTATEUCH, HEXATEUCH, PENTA- TEUCH. [Pok. dheugh- 271.] dhghem-. Earth. 1. Suffixed zero-grade form *(dh)ghm-on-, “earthling,” in Germanic *gumén- in Old English guma, man: BRIDEGROOM. 2. O-grade form *dhghom- in Greek khthon, earth: CHTHONIC; AUTOCH- THON. 3. Zero-grade form *dhghm- in Greek khamai, on the ground: CHAMAEPHYTE, CHAMELEON, CHAMOMILE, GERMANDER. 4. Suffixed o-grade form *(dh)ghom-o- in Latin humus, earth: HUMBLE, (HUMILIATE), (HUMILITY), HUMUS; EXHUME, INHUME, TRANSHUMANCE. 5. Suffixed o-grade form *(dh)ghom-on-, “earthling,” in: a. Latin homé, human being, man: HOMAGE, HOMBRE!, HOMINID, HOMO!, HOMUNCULUS, OMBRE; BONHOMIE, HOMICIDE; b. (in part) Latin himdnus, human, kind, humane: HUMAN, (HUMANE). 6. Suffixed form *(dh)ghem-ya in Russian zemlya, land, earth: SIEROZEM, ZEMSTVO. 7. Full-grade form *(dh)ghem- in Persian zamin, earth, land: ZAMINDAR. [Pok. ghdhem- 414.] dhghut-. Fish. Greek ikhthus, fish: 1cHTHYO-. [Pok. ghdha- 416,] dhgh(y)es-. Yesterday. Suffixed (comparative) form (dh)ghes-ter- in Germanic “ges-ter- in Old English geo- stran, giestran, “yester-”: YESTER-, (YESTERDAY). [Pok. ghdhies 416.] dhgvhei-. To perish, die away. Zero-grade form *dhgvhi- in Greek phthinein, to die away: PHTHISIS. [Pok. gthdhei(a)- 487.)
1340:CELLA kel-2 CELLAR kel-2 CELLARER kel-2 CEMBALO keu-2, kleu-3 CEMENT kae-id- CEMETERY kei-1 CENACLE sker-1 -CENE_ ken-3 CENOBITE gWei-, kom CENOGENESIS ken-3 CENOTAPH dhembh-, ken-4 Cenozoic ken-3 CENSOR kens- CENSUS kens- CENT dekm CENTAL dekm CENTAVO dekm CENTENARIAN dekm CENTENARY dekm CENTENNIAL dekm CENTER kent- CENTESIMAL dekm CENTESIS kent- CENTI- dekm CENTIGRADE ghredh- CENTIME dekm CENTNER dekm CENTO kentho- CENTRIFUGAL bheug-'
1468:EPIBOLY gWele-1 EPIC wekw- EPICARDIUM kerd-1 EPICENE kom EPICRITIC krei- EPIDEMIC da- EPIDERMIS der-2 EPIDIDYMIS dwo- EPIDOTE do- EPIGASTRIUM gras- EPIGEAL gé EPIGENE gene- EPIGONE gene- EPIGRAM gerbh- EPIGRAPH gerbh- EPILEPSY (s)lag- EPILOGUE leg-1 EPIMYSIUM mis- EPIPHANY bha-1 EPIPHYSIS bheue- EPISCOPAL spek- EPISODE en, sed-2 EPISTASIS sta- EPISTAXIS stag- EPISTEMOLOGY sta- EPISTLE  stel- EPISTYLE sta- EPITAPH dhembh- EPITASIS ten- EPITHELIUM dhé@(i)- EPITHET dhé-1 EPITOME tem- EPOCH segh- EPODE wed-2 EPONYM nd-men- EPONYMOUS nd-men- EPOS wekw-
```


## [2026-09-05T18:32:37.844Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '13350,13372p' BRT.txt; echo \"=== search dam- V.:\"; grep -n \"dam-  V\\.\\|'dam-\\|dman-\" BRT.txt | head",
 "description": "Bartholomae context around dadmainya"
}
```


### [2026-09-05T18:32:37.916Z] TOOL RESULT

```
•  j.  däityö.baoiay-  Adj,  (auch  fem.)  'die gehörigen  Räuchermittel  habend,  daraus bestehend':  aäiim  baoiolm  '6aoiöyff{AP{.y* N.  103.  I
vKonipA.  —  Pü, :  fehlt,  —  0  Auf  kollelcL  AS. , bezogen?     S,  aesma-  No.   1.  |
•  j.  däityö.baoi3i.-bav-  kompV.  'der  ge- hörigen Räuchermittel  teilhaftig  werden': °buyS  ..  äiars  pui:ra  ahurahe  Y.  6'2.  2.
Komp.;  'baoiay-  Adj.  -^iav-;  %  26^.  —  PQ. : liälihä  iöJ  biH't.
•  j.  dädaray-  Adj.  'der  etwas  (Akk.)  be- sitzt': yai  asp>r?nB  vastrahe  . .  'rayS  (NP,) a  anaiwySsH  strmti  yezi  sat  nSit  asp?r}rw vastrahe  .  .  'rayS  nSit  ^anaiwyästt  "wenn  1 sie  ein  vollständiges  Kleid  . .  besitzen,  so versündigen  sie  sich,  wenn  sie  es  nicht! anziehen;  .  ."  N.  96".  1
Zum  V.  3dar-,  mit  Int.-Ked.  gebildet;  ar  bt ! «.  ar  oder  /■-■;  s.  daiu  WH.  Gr.»  S  "SS  «■  -  | Pü. !  iaiar  . .  därriid.  j
•  p.  dädariay-  m.  EN.  zweier  Heerführer  ! Dariuil.,  i)  eines  Persers,  Satrapen  von' Baktrien:  -/iV  mlm<^  pärs^  .  .  bäxtriyä X5a'h''api!vä  Eh.  J.  3;  3.  2)  eines  Ar- j meniers:  'jY/  näme^  armimyc^  tnanä  ba"-  \ äake^  Bh.  2.  J;  7,  9;  —  palis  -sim  Bh. ' 2.  7,  8,  9.
Eig.  'kühn';  zum  V.  dars-,  mit  Inl.-Red.  —  ai. dädhnay  Adj.  -kühn'.  |
•  p.   däduhya-   m.  EN.   eines  Persers:
bagabuxsa''  ndma'  °hyahyä  pti^'^J' pärsa''
Bh.<^.  r8.
Eig.  PPA.  (S  sog.  5),  aus  einem  Praes.  29  b (Int.),  mit  11  nach  S  ^yo.  8  für  ','  aus  ar.  tin, weshalb  k  (nicht  /,  %62.  1  No.)i)j  vgl.  zBild. soBsuHlayö.  Eig.  Bed,?,  s.  No.  2.  —  'I  Das Richtige  über  h  bei  JOppert  Act.  6.  Congr. Ot.,  Sect.  S^m.  63g.  Falsches  neuerdings WZKM.  //.  254.  —  ')  Der  Bildung  scheint ein  Praes.  8  ar.  *,i(Jiyim-  \  'd[k)Hnas.  lu  Grunde lu  liegen;  ob  eig.  'schnaufend,  keuchend'  zu lit.  .hiesiu,  dusik}
•  j.   däSmainya-  Adj.  'sich   aufblasend,
"däSra-
73a
-blähend',  von  Fröschen":  batvar»  vasaya- nam    'nyanatn   .  .   vazayanam    upapanam
Eig.  PPA.  (S aoji.  5),  aas  einem  Prae».7-^  13 »>■ —  Vgl.  aL  dhämaH  'er  bläst',  np.  damidan 'blasen'.  —  Pü.;  vanfj  i  saiuTi  {Erklärung  statt Übersetzung);  dazu  die  Erl.;  Aar  ee  kt  yul  hac äp  lavSn  *iäiitl  tamlki  »gL  No.  I.  —  ')  Ge- meint sind  die  Laubfrosche,  als  Vertreter  der Landft6sche  im  Gegensatz  zu  den  WasserfrÖ- scheo.  —  ')  Ein  Praes.  auf  ainya-  mit  InL- Red,;  ganz  ähnlich  ist  gr.  jtBji^iiiVM  ans  *WJ- gebildet,  ferner,  mit  einfacher  Reduplikation, «nwra/v»  aus  *fal-  (vgl,  got.ßnpaii  und  iBcd. gr,  iIjIv  und  ai.  vindäli;  s.  H'aed-),
•  j.  didrva-  n.  'Holz,  Holzstück,  Baum- stumpf: iafomisd.)  va  'ärumväV.g,  11.
Red.  Bild.;  s.  därav-  und  gr.  ci-^pia*;  BTHL. IFAnz,  4.   13.  —  Pu.:  bandvar  i frafih.
•  j,   däS"-    V.,    nur    mit    us    'ausfüllen'.
Praes.  a  dälia-.
'(ein  Gefäss)  aus-,  bis  oben  anfüllen mit  — '  (Gen.) :  yezi  aahat  (näml,  das  Gefäss) zarmamis  hak?r)t  fi-asnääayfn  maismana gSui  hakint  s^mS  uzdä'kaym  hakirit  apö frasnähaysn  a%a  yaoidayqn  V.  7,  74'',
Et.?').  —  Pü.:  hiak  bär  pa  aamli  bularrd  t uidahhtd,  erl. :  nam  ape  e  *vel^/i).  —  ')  Vgl. zBed.  und  iSt.  V.  /.  14  {wo  haatanayin).  — s)  Jedenfalls  nicht  zu  'da-,  wie  JuBTi  Hdb. 114  wollte.  —  3)  Bei  Sp-  steht;  ndddnd, bei  Dakab:  n  dd  an  d.  Entweder  ist  dd  für dl  =  ei  geschrieben  oder  die  Urschrift  hatte Dddannnd,  GIrPh.  /.  326.  11.
=== search dam- V.:
6012:ni/antlni  Ytß.  54;  18,  22',  26,  30,  42,  50, 54,  lOS,  117,  130,  p.4,  9f.s,  18,  22,  26, 72.2,  74- 58',  75.3,  28,  32,  Vytao»,  21, 4ß;  —  da%äni  ti .  ,  kazannm  .  .  uta  Ig 'S3m  äfrinäni  ..  Y.22.4L;  YL5.63;  — j/ai  mam  iura  paedayanta  .  .  äai  'stm tanüm  aguze  .  .  äai  tnam  fraguzayania  . . Yti^-SS;  56;  —  kü^a  tl  'um  varsm i?rjnavane  V.  2.  $t ;  lff.12,  22.6',  Ytij. 57;  —  't?m  II  g<K%ä  frähoyeni  'z?m  .  . 'Z3m  V. 2.5;  27.6,  7,  Vr.j.7;  —  \valnä a''ur(^mazdäha''  'dam  xsäya%iya^  amiy . . 'damsäm  xs'äya^iyi^  aham  Bh.  7. 5!;  — iyam  gaumätJ'  ,  .  avahä  a%ak(r  'dam baräiy^  amiy  . ,  'dam  xl3ya%iye^  amiy Bh.b;  c-j",  7.11,  13,  i6',  2.3,  s,  14,  J-S. 13;  1^2^;  —  ima'  tya'  'dam  akunavatn vasnä  J'ur^mazdäha'  ah/^ ..pasavJ' ya%ä x^aydiiiyJ'  abavam  'dam  19  hamaranä akunavam  vasnä  t^un^mazdäht^  'dam- säm ajanatn  uta  9  xssyaHyä  agarbäyam Bh..^.  2;  — pasäv^  'dam  t^urt^tnazdäm patiyävahaiy  a^urJ'matdämaiy  upastsm abar(^  .  .  avähä  'dam  . .  gaumätam  .  . aväjanam  . .  avadasim  aväjanam  x/a- %''amHm  °dam  adrnam  vasnä  a^urc^maz- dähc^  'dam  xsilya'^iyaf'  abavam  J'ur^- mazdä  x/ä^^am  manS  Jrsbara^  Bh.  J.  13; 14';  —  'damsaiy  uta  ftaham  .  .  frajanam ,  .  pasävJ'  'dam  .  .  uzmayapaiiy  akuna- vam Bh.  2. 13;  — pasävtrsaiy  'dam  ulä näham  .  .  fräjanam  ,  .  pasäve^sim  ,  ,  ut- mayäpatiy  akunavam  fih.2. 14;  —  °dam (s.  I  b)  xläya%iy^  amiy  vasna  c^urt^- mazdäha/"  'damsim  *g'a^avä  niya/ädayam tya^/äm  'dam  a%akam  avc^  .  .  D.  ö.  4 ; 3'.  5>  4-1,  5-2.  ^7-3^  Bh.  j.is,  16,  17', 18I,  19',  2.1',  2,  4,  6',  7,  9,  10,  II,  12*, 13,  Bh.^.  I,  2,  6,  8,  13,  14,  4.4,  6,  8, 12,  IS,  18,  5.1%  X.7.3,  ^.311.  Die Übrigen  Siog.-Kasus  des  Fron.  i.  Fers. s.  unter  ^ma-.  [¥.4:^.14;  lies  a&;  — Yt.  7.29:  lies  zamarf.'j
12916:•  j,  darsj-ö.väradman-  Adj.  {auch  fem.) langdauemde  Wehr  bietend,  lange  als Wehr  dienend':  a^m  rasainüm  'man»m (ASf.)  Y.52.1;  ■ —  vaaufil/ca  a%ä  vanuhlsca aiayd  .  .  räsainir/  °manS  (NPf.)   Y.  52.  3.
13602:•  j.  d^iinan-  d.:  s.  unter  ^ädman-.
25360:•  j.  rädman-  Adj. mit  —  (Gen.),  Anhänger':  yS yasnS  aojanS  aiahe  'ma  (NS.)  jlslayamnd ya^wa  gai'hä  asahe  tmrrjinte  "wer  .  . sich  einen  M.  nennend,  sich  Tür  einen Anhänger  des  A.  ausgebend  mit  Zauber die  Well  des  A.  zerstört"  Y.  Ä  3.
```


## [2026-09-05T18:32:47.306Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD:\"; grep -n \"^dam\\|dam \\[\\|damīdan\\|dahm\" PHD_mackenzie.txt | head -20; echo \"=== PHD alt:\"; grep -n \"breath\" PHD.txt | head -20",
 "description": "Grep MacKenzie"
}
```


### [2026-09-05T18:32:47.385Z] TOOL RESULT

```
=== PHD:
853:   a-dahm. elPhm] uninitiated.
1851:dahm [d'hm] virtuous, pious; a full member of the Mazdean community,
1856:dam-, ,...,lsn, v. daftan.
1857:Idam [d'm I = M] creature, creation.
1858:lIdam [d'm 1= M, N,...,] tame animal.
1859:adam [d'm I P d'mg, N ,...,] net, snare, trap.
1860:damad [d'm't I M d'm'd, N ,...,] bridegroom, son-in-law.
1863:damenag [dmynk l ] fan.'
1864:damidan [dmytn ] = daftan.
2726:hamdam [hmdm IN ......] intimate.
3131:kadam [kt)m I M kd)m, N kudam] which, what.
3897:padam [pd'm I (N paniim)] mask for the mouth, worn by a celebrating
6870:    damage, injure.                        initiate dahm.
7287:pious dahm, kirbagig; v. righteous.        pool warm.
7885:uninitiated adahm.                         arzomandih, wahiig.
7928:virtuous dahm, hunariiwand, kir-         water ab.
10507:dam-
11071:dahm                                         bahr
12310:mayI                               adahm
=== PHD alt:
306:īdabr [dpi] sinner, deceiver. *dabr [dpl] *dark-coloured. dad [dt' | M dd, N ~] wild animal. 1ааа [d't! | M d?d, N ~] law, justice; those scriptures dealing with legal matters. даа [d’t' | N ~] age. зааа [d>1!] tooth. tdād, v. ahlaw-dād. dādan, dah- [YH BWN-tn! < A Vyhb; d*tn!, dh- | M d'dn, (dy-), P dh- N ~, dih-] 1. give; 2. create. —išn [dh(y)sn'] giving, donation; creation. dādār [d’t?l | N ~] creator. -- ih : creatorship. dādestān [DYNA < А dyn; d'ts?n! | M d'(d)ys?n, N dá(de)stan] judgement, justice, law; case, process. dàd-gàh [2^? gs] proper place, fire temple; = daxmag. dādīg [d'tyk'] legal, concerned with the Law. dad-meh (d"tms] adult, elder. dādwar [d?twbl | (M d^ywr, P d'dbr), N da(d)war] judge. ~ih: judgement. daftan, dam- [dptn', dm- | M dm-, N dam-idan] breathe, blow. «dišn: breath. daftar [dptl | N —] register, account-book. dagr [AL YK < А ryk; dgl | M dgr > dur, N dër] long. dagrand [дата | N dërand] long. ~«xwaday [-hwt’y] eternal, of long dominion. daģr|-pattāy [dgl pt'd] long-lasting. -—-zamáàn [-2т?п!] a long time. ^-zi(w)isn [-zywsn'] long-lived. dah [ro, ASLY A < A ә | M dh, N ~] ten. dah-, —išn, v. dádan. Юаһаӣр [dř k' | (N Dahàk)] = Azdahág. dahān [РИМЕ < A p(w)m-h | M dhyn, N даһап] mouth. dahibed [dhywpt! | M dhybyd] ruler, lord of the land.
316:drón yaštan: consecrate the sacrificial bread. drēš [410] mark, branding; punishment. ~ag [-k!] *desolation. drēšīdan, dro$- [d/w$-ytn'] brand. drēūšom [dlwšwm] mark. droz-, v. druxtan. drózan [dlwen! | M, J drwzn] lying, liar. ^h: falsehood. drubušt [di(w)pwst'] fortress. ~ih: defence, fortification. drüdan, *drün- (HCDLWN-tn! < A У hsd | M ача, (dwr-), N durüdan, diraw-] reap, mow. drust [drw(y)st' | (M dryst), N durust] right; well, healthy. —Ih: righteous; health. drustabed [drwystpt'] chief physician. društ [dlwšt' | N durust] harsh, rough, severe. ~ih: harshness, severity. ~-Awaz, ~-éwaz [-p'c, ~yw’c] harsh-spoken. druwand [dlwnd | M drwnd] evil, sinful, unrighteous. ~īh: sin, unrighteousness. druxtan, dróz- [dlwhtn', dlwc- | M drwxt, drwz-] lie, deceive. druz [dlwe | (P drwj)] demon. айа [dwt! | M dwd, N ~] smoke. düdag [dwtk! | N —a] family. dudigar [dtykl | M dwdygr, N digar] second. duj-, = duš-. ~-daft [dwsdpt'] ill-breathing, short of breath. ~-dānāg [dwšd”7?k!] ignorant. ~-dén [dwšdyn' | M dwjdyn-] of evil religion. «=dēys*rīh [dwsdwyslyh] the evil eye. ~-gand (dtwsgnd | P dwjgnd] stinking. ~-gandih: stench. dum(b) [dwm(b') | N ~] tail. ~dmand [-'wmnd) tailed. ааг [LH YK'! < А rhyq; dul | M dur, N ~] far, distant, remote. durgar [dwlgl | N ~] carpenter. dusraw [dwslwb!] notorious, dishonoured. ^Ah : notoriety, dishonour. duš- [dws- | = M] ill-, evil-. ~īh: evil, wickedness. ~-абаһ [dw??^ Es] foolish, stupid, ignorant. ~-абаһіһ : foolishness, stupidity. ~-arz [2 ic] worthless. 7--Ca&m [-cém] envious. —-Ca$mih: envy. ~-tihr [-cyhl | M dwfcyhr] ugly, hideous.
603:wābar [w’Al | M wbr, (N bāwar)] truth; belief. wābarīģān [w?/yk?n' | M wbryg’n) true, trustworthy. “Аһ: trustworthiness. wabz [wpc, wpz] wasp. wačast [wcst! = Av. vwacas-tasti-] strophe (of the Gathas). watéag [wck!, (bck!) | N bacca] child, baby, cub. wad [SL Y.ÀA < A sry’; wt! | M wd, N bad] bad, evil. ^ Áh : badness, evil. маа [w?t! | M wd, N bad] wind, breath, spirit; cal. 22nd day. wadag [wtk'] evil, vile, wicked. ~ih: evil, vileness. wādām [w’t?m | N bádám] almond. wādbān [w°tp’n' | N bādbān] sail.
649:waxšwar [whiwl | N waxtür] prophet. ~th: prophethood. P wāxtan, wāž- (w’hin', wc- | P wxtn, и?с-] say, speak. lway [wd = Av. way-] bird. *way [wd = Av. wayu- | P шуш] air, atmosphere. ~ í wattar: a demon. ~ i weh: a divinity. way [wd | M wy, N ~] woe. lway- [w*d- | M w’y-] fly. ~endag [-(y)ndk! | J w|B' ynd?] bird. wüyidan, *way- [w'd-ytn'] blow (of wind). wayodagàn [wydwtk’n! | M *wywdg'n, N bayēgān(ī)] nuptials, marriage feast. waz-, -išn(-īg), у. wazidan. waz [wc | = M, (N bāj)] word, speech; ‘grace’ (before meals). ~ griftan: say ‘grace’. 1, *wüz-, ~iSn, v. b *wāzīdan. P wāž-, v. wāxtan. wāzag [w’ck'] utterance, saying. wazay [wzy| N ~, bazay] frog. wāzār [w’c?l | M w?c'r-, N bázár] market. wāzāraģān [wlkn! | M wergn, N bázárgàán] merchant. ~ih: trade. wazidan, waz- [wc-ytn! P wz-, N ~] move, blow (of wind). ~išn: movement. ~i$nig : mobile. Iwāzīdan, wāz- [wc-ytn'] move, carry away; fly. ~išn: flight. *wazidan, w4z- [w'c-ytn! | N bāzīdan) play. wāzīģ [w'cyk! | N Бахт] game, play. wazr [wel] = *warz. wéd [wyt' | N bed] willow. weh [SPYL < А #руғ; wyh | M why, wyh, N bih] better, good. ~ih: goodness. «-dēn [-dyn' | N bih-din] of the good (Mazdean) religion. wēhm [*wyyhm | M wyhm] large, wide, broad. ~ih: width, breadth. wém [шут | = P] rock. wēmār [wyml | M wym’r, N bēmār] ill, sick. «Ih: illness. wén [wyn'] breath. wén-, ~i5n(-ig), v. didan. wēnāb [wyn’p | N binàb] vision. ~dag [-d’h', -t*k!] visible. wënäe [wyr?k! | M wyn!g, N bind] seeing. ~īh: seeing, sight.
1081:breath damišn, wad, wën: short of ~ dujdaft. .
1082:breathe daftan, (damīdan).
2365:ill-breathing dujdaft.
```


## [2026-09-05T18:32:47.928Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== CHEUNG dam:\"; grep -n \"\\*damH\\|\\*dam-\\|\\*danH\\|\\*dan-\" CHEUNG.txt | head -30",
 "description": "Grep Cheung"
}
```


### [2026-09-05T18:32:47.980Z] TOOL RESULT

```
=== CHEUNG dam:
4615:*damH3 55 
4626:*damH ‘to build’ 
4650:*damH ‘to tame’ 
4670:*damH? ‘to blow, breathe; to swell’ 
5236:*das(s)- < IE *dmH)-sk- ?, v. *damH!) 
16837:Zaz. masayis ‘to swell up, become fat’ (*damH?). > DMMPP: 227a 
55740:*damH? (s.v.), *tauH 
55741:*damH? (s.v.), *(d)banz!, 
55784:*damH°, *HuaH!, *pazd' 
55868:жаі! (s.v.), *daiz, *damH", 
58107:*damH’, *ѕаиН? 
58129:*damH?
```


## [2026-09-05T18:32:53.587Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4665,4700p' CHEUNG.txt; echo \"=== dan run:\"; grep -n \"danīdan\\|danidan\\|dan- ‘to run\\|‘to run’\" CHEUNG.txt | head -20",
 "description": "Cheung damH3 entry"
}
```


### [2026-09-05T18:32:53.654Z] TOOL RESULT

```
zähmen, Engl. to tame, etc. 
*REFERENCES: Abaev, Slovar’ I: 365; Slovar’ IV: 8; DKS: 151b f.; Werba 1997: 292; ESIJa II: 321 f. 


*damH? ‘to blow, breathe; to swell’ 
*AVESTAN: Y Av. daómainiia- ‘blowing up (intr.)’ (V 14.5, V 18.73) 
*MIDDLE PERSIAN: MMP dm- {no attested forms ?}, BMP dm- /dam-/ ‘to breathe’ 


c DMMPP: 138a 
Pres.: IND. 3sg. BMP dmydy /damé/, 3pl. BMP dmynd /daménd/; Inf.: BMP dptn /daftan/ 


56 *danh 


*PARTHIAN: dm- ‘to blow, breathe’ || (+ *a-) "dm's- ‘to swell up’ || (+ *ham-) ’ndm- 
‘to sigh; to bleat (of sheep)’ = Ghilain: 56 | DMMPP: 138a, 24b, 44b f. 

Pres.: IND. 3pl. “dmynd, IMPV. 2pl. dmyyd || (+ *a-) Pres.: IND. 3sg. *’dm’syd, 3р1. *’dm’synd || (+ 
*ham-) Pres.: IND. 3sg. *’ndmyd, 1р1. ’ndm’m ‘we sigh’, 3pl. 'ndmynd ‘they bleat’ 

*KHOTANESE: dam- ‘to blow’ || (+ *uz-) uysdem- (uysdaim-) ‘to cool; extinguish’ || 
(+ *pati-) LKh. *padem- (padam-) ‘to blow’, padama- ‘wind’ || (+ *nis-) LKh. 
nasdem- (nasda’m-) ‘to blow out, extinguish’ > SGS: 43 f., 16, 69, 51 

*SOGDIAN: BSogd. öm’s ‘to swell’, BSogd. 6m’k, BSogd. öm’kh ‘breath’ || (+ *fra-) 
CSogd. füm'ty ‘insufflated’ (cf. Schwartz 1967: 57) 

Pres.: SUBJ. BSogd. óm's't (P7.61) 

*CHORESMIAN: m/ém’s- ‘to become fat, strong’ = Samadi: 65 

*NWIR: NP damidan/dam- ‘to blow; to breathe; to blossom; to appear (as the dawn)’, 
Khuns. dum- ‘to pump in, give (air)’, Kurd. (Sor.) таѕап/таѕё- ‘to swell up, inflate 
=== dan run:
492:*saucé ‘to burn, light", *rai9! / *frait/9 ‘to die, decompose’, *caud / *paud ‘to run’. 
5286:*dau? ‘to run’ 
5287:MIDDLE PERSIAN: MMP dw-, BMP dw(b)- (LHTWN-) /daw-/ ‘to run’ = DMMPP: 
5299:*NEIR: Oss. I. dawyn/dawd, D. dawun/dawd ‘to spawn’, Yghn. dau-/dáuta ‘to run’, 
5308:*MISC: Par. daw- (?), dhaw-/dah- ‘to run’ (LW ?), ? Par. daw- ‘to be straight’ 
5891:*dram ‘to run’ 
5910:«PIE *drem- ‘to run’ = LIV: 128 | Pok.: 204 f. 
6036:*drau? ‘to run’ 
6054:*SANSKRIT: drav ‘to run’ (RV) = EWAia I: 755 f. 
6057:«PIE *dreu- ‘to run’ = LIV: 129 | Pok.: 205 
6092:© This root should be separated from *drau^ ‘to run’ (?), on which see Schwartz 
6376:*duar: these "roots" are perhaps extended formations of *dau? (Skt. dhàv) ‘to run’, 
6412:*duar ‘to run’ 
6414:*AVESTAN: duuär- ‘to run’ || (+ *apa-) ‘to run off, away’ || (+ *upa-) ‘to run into, on’ 
7200:yaz-/yext-, Sangl. yuz-/yuzd, Ishk. yoz-/yozd, M. yaz-, Yi. yaz- ‘to run’, ? Oss. I. 
7537:gəfs-/gəfst- ‘to run’ 
19850:*us-paua- from an IE root *peu- ‘to run’ (presumably the unenlarged root of 
19865:*paud ‘to run’ 
21345:*IE COGNATES: OHG scehan, МНС schehen ‘to run’, OHG gi-skehan, MHG 
24355:Bal. tacit, tatk/tac- ‘to run’, Tt. (Cha.) bettat/bettajas ‘he ran’, Delij. ba-taj1 ‘to rush;
```


## [2026-09-05T18:33:00.936Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4700,4730p' CHEUNG.txt",
 "description": "Cheung damH3 continued"
}
```


### [2026-09-05T18:33:00.985Z] TOOL RESULT

```
Khuns. dum- ‘to pump in, give (air)’, Kurd. (Sor.) таѕап/таѕё- ‘to swell up, inflate 
[intr.]’, Zaz. mäsäyis ‘to swell up, become fat’, Awrom. mäsay/mäs- ‘to swell’, Gil. 
(Rsht.) dämeestoen ‘to breathe’ || (+ *а-) NP amas-, Kurd. (Sor.) 4masan-/amasé-, 
awsan-/awse- (inch.) ‘to swell up’ (LW ?) 

*NEIR: ? Oss. I. dymyn/dymd, dymst, D. dumun/dund ‘to blow (up); to smoke’, Oss. 
I. dymsyn/dymst, D. dunsun/dunst (inch.) ‘to swell (up)’, Yghn. dam-/damta ‘to 
dawn; to bud [of flowers]; to rise [of boiling water]? (< NP ?), M. lamdiya (ppp.) 
‘swollen’ || (+ *ham-) Pash. dūmai ‘a cold, catarrh’. ç The Oss. forms, which have 
*u as stem vowel, may either derive or show influence from nominal *duma- (Skt. 
аһата-) ‘smoke’, v. Cheung 2002: 24 f. 

*SANSKRIT: dham ‘to blow, play a windinstrument, fan the fire’ (RV+) > EWAia I: 
775 

«PIE *d'meH- ‘to blow’ > LIV: 153 | Pok.: 247 f. 

*IE COGNATES: OCS дъто, ORuss. demu ‘I blow’, SCr. düti ‘to blow’, Lith. dom 


‘to blow (also of wind)’ 

*REFERENCES: Christensen, Contributions I: 65; IIFL II: 223b; Morgenstierne 1942: 263; Andreev — 
PeSéereva: 243a Ё; Abaev, Slovar’ I: 382 Ё; MacKenzie 1966: 102; WIM I: 68; DKS: 152a; Werba 1997: 
297; Cabolov 2001: 77; ESIJa II: 316 ff. 


*danh ‘to teach, instruct’ 


*AVESTAN: OAv. danh- ‘to teach, instruct’? => Liste: 30
```


## [2026-09-05T18:33:10.411Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON دنیدن:\"; grep -n \"دنیدن\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt 2>/dev/null | head -10; echo \"=== MON دمیدن:\"; grep -c \"دمیدن\" MON_part1.txt MON_part2.txt 2>/dev/null",
 "description": "Grep Mo'in"
}
```


### [2026-09-05T18:33:10.492Z] TOOL RESULT

```
=== MON دنیدن:
incoming/MON/MON_2vol_Adena_v1_djvu.txt:63307:دنیدن: «۵۸]-عیل آهند» دویدن] (مسص‌ل.) 
MON_part1.txt:63307:دنیدن: «۵۸]-عیل آهند» دویدن] (مسص‌ل.) 
=== MON دمیدن:
MON_part1.txt:18
MON_part2.txt:8
```


## [2026-09-05T18:33:11.204Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '12400,12500p' FSF_pages.txt",
 "description": "Read FSF danan entry"
}
```


### [2026-09-05T18:33:11.249Z] TOOL RESULT

```
                 ‫باد سخت بابرف و سرما‪:‬‬
                                                                   ‫بیفتاد و پیران درآمد به زیر‬
               ‫همه لشکر سلم همچون رمه‬
                                                       ‫بغلتید زیرش سوار دلیر‪.‬‬
 ‫که بپراگند روزگار دما‬
 ‫)‪1-4۹4۲۱-۴1‬‬
                                                                             ‫دم زدن (با زبر اول)‬
                           ‫(اسدی ‪:)۵۴-۷۱‬‬                     ‫‪_۱‬کنایه از دیر کردن» تأخیر کردن‪:‬‬
             ‫مر آن گرگ را مرگ به در دمه‬                              ‫گر از آمدن دم زنی یک زمان‬
‫که بی خورد ماند میان گاه‬                               ‫برآید همه کامة بدگمان‬
                       ‫ویس (‪:)۷۴۴-۴۰۵‬‬                  ‫(‪)۲-۱۳۰-۶۷۳‬‬

                                                       ‫=م برزدن‪ :‬نفس تازه کردن‪.‬‬
                                                                              ‫‪-۲‬دم زدن د‬
‫جهان را از دمه بیم هلا کس ‪۰‬‬                                            ‫آسودن» خستگی درکردن‪:‬‬

                                       ‫دمیدن‬                   ‫تو خود رنجه گشتی بدین تاختن‬
                       ‫گشتن‪:‬‬   ‫‪-۱‬شعله‌ور‬
                                                       ‫سپه بسردن کوینه رااساختن‬
‫دنان‬                                         ‫‪۳۳۲‬‬

           ‫‪-۴‬شتابان تاختن» حمله بردن‪:‬‬                           ‫فرستاده نزدیک دستان رسید‬

       ‫سیاوش به دشت اندرون گور دید‬                 ‫بهکردار آتش دلش بر دمید‬

‫چو باد از ميان سپه بر دمید‬                         ‫‏)‪(W-1‬‬
‫)‪(۳-۰4-14۳‬‬                                                        ‫چو رودابه گفتار ایشان شنید‬
                               ‫‪-۵‬وزیدن‪:‬‬            ‫چو از باد آتش؛ دلش بردمید‬
               ‫چو باد سپیده دمان بر دمد‬            ‫(‪)۱-۲۶۱۰-۸۹۳‬‬
 ‫سپه جمله بايد که اندر چمد‬                         ‫‪-۲‬برآمدن بیرون زدن‪ ,‬جوشیدن» فواره‬
‫‏(‪)٩۵۷-۱۷۶-۴‬‬                                                             ‫زدن‪ .‬به موج درآمدن‪:‬‬

                              ‫(حافظ ‪:)۹۷‬‬            ‫زمین شد به زیر تنش [تن ازدها] ناپدید‬
 ‫کنون کهمی‌دمد از بوستان نسیم بهشت‬                  ‫یکی چشمه خون از برش بردمید‬
‫منو شراب فرح‌بخش و یار حور سرشت‬                    ‫(‪)۲-۶۵-۷۸۳‬‬
          ‫‪-۶‬برانگیخته خوشمگین شدن‪:‬‬                             ‫چگودرز توران سپه را بدید‬
          ‫چو اشفته شد هرمز و بردمید‬                 ‫که برسان دریا زمین بردمید‬
‫به گفتار آذرگشسپ پلید‬                              ‫‏)‪(VA-1۰1-0‬‬
‫(‪-‬پرویز ‪)۸۷۴‬‬                                               ‫نه خورشید شمشیر گردان بدید‬
 ‫‪-۷‬برآمدن‪ ,‬طلوع کردن [سپیده‪ .‬صبح‪,‬‬                   ‫نگهردی به روی هوا بردمید‬
                                 ‫افتاب ]‪:‬‬           ‫(‪)۶۰۱-۲۶۲‬‬
          ‫سپیده چو از تیره شب بر دمید‬                                    ‫(رودکی‪ ,‬نفیسی‪:)۱۴ .‬‬

 ‫میان شب تیره اندر خمید‬                               ‫خورشید را ز ابر دمد روی گاه‌گاه‬
 ‫(‪)۱-۱۳۱-۶۱۷‬‬                                       ‫چونان حصاریی که گذر دارد از رقیب‬
                        ‫(ویس‪:)۴۱۴-۰۲ ,‬‬             ‫‪-۳‬خروشیدن‪ .‬غریدن (به واژة دم معنای‬
         ‫دمیده گشت صبح از خاور بام‬                                           ‫پنجم نگاه کنید)‪:‬‬
‫کام‬    ‫ور‬
        ‫شهار‬
           ‫کد ب‬
              ‫شکفته ش‬                                           ‫دمیدی به کردار غرنده ميغ‬
                             ‫دنان (با زیر اول)‬     ‫میانم به دونیم کردی به‌تیغ‬
 ‫قید از دنیدن‪ .‬دنیدن‪ :‬مرکب از دن [‪ :‬دي‬             ‫‏)‪(VA-0.-F‬‬
                    ‫تگ] ‪+‬پسوند مصدری‪:‬‬                    ‫[رستم] بیامد بغرید چون پیل مست‬
 ‫شاهد برای دن به معنی «دو» از اسدی‬                 ‫کمندی ببهازو گورزی به دست‬
                     ‫(‪ ۶۸۳-۰۲۳‬و ‪:)۲۶۱-4‬‬                  ‫چندین مدم‬         ‫متوس‬
                                                                              ‫کواگف‬
                                                                                  ‫بد‬
          ‫گوزنان و غرمان شده تیز دن‬                ‫بمه نیروی این رشته شست خحم‬
 ‫به شورش درون شیر بکارگدن‬                          ‫‏)‪(\FF.-*0-F‬‬
                                              ‫‪۳۳۸‬‬                                           ‫دواج‬



                                                                    ‫کنون بور آهو تگ کرگ دن‬
 ‫چو خورشید تابان به دوپیکر است‬                      ‫کمان و کمین من و کرگدن‬
 ‫(‪)۲-۱۹۱-۹۷۲‬‬                                          ‫از منوچهری در صفت اسب (دیوان ‪)۷۶‬‬
                                          ‫دود‬        ‫یوزجست و رنگ‌خیز کورگ‌پوی و غرم‌نگ‬
             ‫به‌معنی مجازی» تیرگی» تاری‪:‬‬             ‫ببرجه آهو دو و روباه حیله گوردن‬
             ‫روانش ز انديشه پر دود بود‪...‬‬           ‫بنابراین دنان به معنی شتابان روان شتابان‬
‫(‪-۸‬نوشیروان ‪)۸۵۶۱‬‬                                                                 ‫تازباناست‪:‬‬
                                 ‫دود برآوردن‬                        ‫پس اندر سپاه منوچهر شاه‬
‫و ویران کردن» هلاک و‬        ‫آتش زدن‪ ,‬خراب‬           ‫دمان و دنان برگرفتند راه‬
                               ‫نابود ساختن‪:‬‬         ‫(‪)۸۲۵-۱۲۹-۱‬‬

          ‫روان سیاووش راز آن چه سود‬
                                                              ‫گهرد دنان در‬
                                                                         ‫ای همه‌ساله دنان ب‬
 ‫که از شهر توران براری تو دود‬
                                                    ‫مننهبه گرد دنانم و نه دنانم‬
 ‫(‪)۵-۷۸۱-۲۷۷۱‬‬
                                                    ‫(در مصراع اول دنان اول از فعل دنیدن و‬
                                                    ‫دنان دوم جمع دن [با زبر اول ‪-‬تازی] به‬
‫که پیروز بودند گردان ما‬
                                                                       ‫است)‪.‬‬     ‫امب‬
                                                                                   ‫شنیرخح‬
                                                                                        ‫مع‬
                 ‫از اختر تو را روشنایی نمود‬                                                 ‫دواج‬
 ‫ز دشمن برآورد ناگاه دود‬
                                                                                ‫روانداز‪ .‬لحاف‪:‬‬
 ‫(‪)۵-۲۴۱-۰۹۹‬‬
                                                                  ‫یم آگهازاصل و فرع حراج‬
                                         ‫دوده‬
                                                    ‫همی غلتم اندر مبان دواج‬
 ‫دودمان خانواده‪ .‬پهلوی‪ :‬دوتک ‪6۵۱۵۱‬‬
                                                    ‫(‪-‬یزدگرد ‪)۱۵۸‬‬
 ‫«دوده‌ای که من ازش بودم همه نامی و‬                        ‫‪2‬‬                    ‫دوال (بازبراول)‬
 ‫توانگر بودند» (خسرو و ریدک ص ‪ ۲۱‬بند‪)۴‬‬                                    ‫بند چرمین‪,‬کمربند‪:‬‬
         ‫بدو گفت رو پیش دستان بگوی‬                                  ‫به کشتی گرفتن نهادند سر‬
‫کزین دوده سام شد رنگ و بوق‬                          ‫گرفتند هر دو دوال کمر‬
 ‫(‪)۶-۷۸۲-۰۵۱۱‬‬                                        ‫(‪)۷-۶۳۲-۴۸۸‬‬
```


## [2026-09-05T18:33:30.290Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"pdf page\" FSF_pages.txt | head -3; echo \"---\"; awk 'NR<12500 && /\\[pdf page/ {last=$0; ln=NR} END{print ln, last}' FSF_pages.txt",
 "description": "FSF page tags"
}
```


### [2026-09-05T18:33:32.040Z] TOOL RESULT

```
---
```


## [2026-09-05T18:33:41.263Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '63300,63315p' MON_part1.txt; echo \"=== دما:\"; grep -n \"^دما\\b\\|^دما:\" MON_part1.txt | head -5",
 "description": "Mo'in danidan context"
}
```


### [2026-09-05T18:33:41.352Z] TOOL RESULT

```
سج.) یک دنبا: (عم.) سی» سیار» خیلی. 
دنسیایرست: اقته1-۳ [ع. ف. - 
دنیاپررستنده] (ص‌فا.) آنکه دنیا را به غایت 
دوست دارد) دنبادوست. 
دنیاوی: 00۷3 [ع.] ( ص نسه.) مسوت 
به دنیا؛ جهانی» دنیوی؛ این جهانی: امور 
دنبوی. 
دنیدن: «۵۸]-عیل آهند» دویدن] (مسص‌ل.) 
دویدن به نشاط و خوشحالی. 
دو؛ 0 (.) (سه.) اولین حرف از نوت‌های 
هفتگانهٌ موسیقی. 
دو: 40 (امص.) راه رفتن به سرعت؛ دویدن. 
دو استقامت: (ور.) دو ۱۵۰۰ متر که بشتر 
به استقامت و قدرت محتاج است. دو 
امدادی: (ور.) دوی که با معاونت بکدیگر 
انجام می‌شود. دو سرعت: (ور.) دوی که در 
=== دما:
17382:دمادم رسمدن. 
24151:دماغی و بصل النخاع و پایه‌های سغز قرار 
37802:دمادم کشتن» بی در بی شدن. . تتایع اضافات: 
44576:دمادم شدن. 
52164:دماغ است و عبارت از خزانه و هم نگهبان
```


## [2026-09-05T18:33:46.556Z] TOOL CALL #37: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-05T18:33:46.563Z] TOOL RESULT

```


```


## [2026-09-05T18:33:49.526Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%D9%85%DB%8C%D8%AF%D9%86",
 "prompt": "Give the full Persian etymology of دمیدن (damidan): Middle Persian form, Proto-Iranian and PIE root, cognates, meanings."
}
```


## [2026-09-05T18:33:51.035Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/d%CA%B0emH-",
 "prompt": "What is the reconstructed PIE root, its meaning, and descendants? If this page does not exist, say so."
}
```


### [2026-09-05T18:33:53.369Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-05T18:33:55.861Z] TOOL RESULT

```
# Persian Etymology of دمیدن (damidan)

**Middle Persian Origin:**
The word derives from Middle Persian dmytn' (/damīdan/), which is a regularized form of dptn' (/daftan/).

**Proto-Iranian Root:**
Both forms trace back to Proto-Iranian *damH- meaning "to breathe, to blow."

**Proto-Indo-European Root:**
The ultimate source is PIE *dʰemH-, with the same semantic field of breathing and blowing.

**Cognates:**
The word shares common ancestry with Sanskrit धमति (dhamati, "to blow") and Lithuanian dumti ("to blow").

**Modern Meanings:**
The verb conveys four primary definitions: (1) to breathe into or blow (transitive), (2) to swell or expand (intransitive), (3) to appear or dawn (intransitive), and (4) to sprout, grow, or shoot (intransitive).
```


## [2026-09-05T18:33:59.676Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%D9%85%D8%A7%D9%88%D9%86%D8%AF",
 "prompt": "What etymology does Wiktionary give for دماوند (Damāvand)? Quote it."
}
```


## [2026-09-05T18:34:00.198Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/damp",
 "prompt": "Give the full etymology of \"damp\" including PIE root and Germanic cognates, and any link to \"dim\"."
}
```


### [2026-09-05T18:34:03.547Z] TOOL RESULT

```
# Etymology of دماوند (Damāvand)

According to Wiktionary, the etymology is: "From Middle Persian _dmbʾwnd_ (dumbāwand)."

The article notes that the complete etymology is incomplete, with editors requesting additional information about the original interpretation as "the mountain from which smoke and ash arises," potentially linking the first component to Proto-Indo-Iranian terms for "smoke."
```


### [2026-09-05T18:34:06.786Z] TOOL RESULT

```
# Etymology of "Damp"

Based on the provided content, here's the full etymology:

**Origin:** The noun "damp" dates to the early 14th century, referring to noxious vapors in coal mines. It likely derives from Middle Low German *damp*, ultimately tracing to Proto-Germanic *\*dampaz*.

**Germanic Cognates:** The word connects to "Old High German *damph*, German *Dampf* 'vapor,' [and] Old Norse *dampi* 'dust.'"

**PIE Root:** The content does not explicitly identify a Proto-Indo-European root for "damp."

**Semantic Evolution:** The noun initially meant poisonous gas, but by 1706 it shifted to mean "moist air, moisture, humidity." The verb (late 14c.) originally meant "to suffocate," later developing figurative senses around 1540, then acquiring the literal meaning "to moisten" by the 1670s.

**Link to "Dim":** The provided content contains no information connecting "damp" to "dim." No etymological relationship is mentioned between these words.
```


## [2026-09-05T18:34:12.421Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/dim",
 "prompt": "Give the full etymology of \"dim\", including PIE root and any link to damp."
}
```


## [2026-09-05T18:34:12.747Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/fountain",
 "prompt": "Give the full etymology of \"fountain\" and \"font\", including the Latin fons/fontis and any PIE root."
}
```


### [2026-09-05T18:34:18.069Z] TOOL RESULT

```
# Etymology of "Dim"

Based on the provided content, here's the full etymology:

**Origin Chain:**
Old English *dimm* traces back to Proto-Germanic *\*dimbaz*, which is "not known outside Germanic." The word appears in related forms across Germanic languages: Old Norse *dimmr*, Old Frisian *dim*, and Old High German *timber*.

**Key Development:**
The adjective originally meant "dark, gloomy, obscure; not clearly seen, indistinct." By the early 13th century, it applied to eyes "not seeing clearly." Later applications to sound (14c.) and light (14c.) followed. A slang sense meaning "dull of apprehension, stupid" emerged in 1892.

**PIE Root:**
The document does not mention a Proto-Indo-European root for this word.

**Connection to "Damp":**
The provided content contains no information linking "dim" to "damp." These appear to be separate etymological lines.

The source explicitly states the Germanic origin is "not known outside Germanic," suggesting the word may have limited Indo-European ancestry documentation.
```


### [2026-09-05T18:34:20.073Z] TOOL RESULT

```
# Etymology of "Fountain" and "Font"

**Fountain** (noun, early 15c.): Derived from Old French *fontaine* "natural spring," from Medieval Latin *fontana*, ultimately from Latin *fons* (genitive *fontis*) meaning "spring of water." According to Watkins, this traces to the PIE root *\*dhen-* "(1) to run, flow," which also produced Sanskrit *dhanayati* and Old Persian *danuvatiy* "flows, runs."

The extended meaning of "artificial jet of water" emerged around 1500, leading to *fountain-pen* (by 1823), named for its ink reservoir that "supplies a continuous flow of ink."

**Font** (noun, late Old English): Also derived from Latin *fons* (genitive *fontis*) "fountain." Originally referring to "water basin," especially in baptism, it appears in the Medieval Latin phrase *fons baptismalis* "baptismal font." The term is sometimes used poetically to denote "a fountain; a source."

Both words share the same Latin root and ultimately descend from the ancient PIE root denoting flowing water.
```


## [2026-09-05T18:34:26.988Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/damp",
 "prompt": "Give the English etymology section of damp: Proto-Germanic form, PIE root, and cognates including any mention of dim, Persian dam, Sanskrit dhamati."
}
```


## [2026-09-05T18:34:28.699Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%D9%86%DB%8C%D8%AF%D9%86",
 "prompt": "Does Wiktionary have an entry for Persian دنیدن (danidan)? If so give its meaning and etymology. If not, say the page does not exist."
}
```


### [2026-09-05T18:34:32.667Z] TOOL RESULT

```
# English Etymology of "Damp"

Based on the Wiktionary entry provided, here's what is documented:

**Proto-Germanic Form:**
The entry states that "damp" comes from "Proto-Germanic _[\*dampaz](/wiki/Reconstruction:Proto-Germanic/dampaz 'Reconstruction:Proto-Germanic/dampaz')_."

**PIE Root:**
The document does not mention any Proto-Indo-European root for this word.

**Cognates Listed:**
The etymology section identifies several related words across Germanic languages:
- Low German _damp_
- Dutch _damp_
- German _Dampf_ ("vapor, steam, fog")
- Icelandic _dampi_
- Swedish _damm_ ("dust")

**Notable Absence:**
The entry makes no reference to Persian "dam," Sanskrit "dhamati," or the verb "dim" in connection with this word's etymology. The documented lineage traces the term through Middle English, Old English, and Proto-Germanic languages only.
```


### [2026-09-05T18:34:33.525Z] TOOL RESULT

```
# دنیدن (danidan) - Wiktionary Entry

Yes, Wiktionary has an entry for this Persian verb.

**Meanings:**
The verb دنیدن has three definitions:
1. To walk with pomposity
2. To boil with rage
3. To run with alacrity and joy

**Etymology:**
The word traces back through Proto-Iranian *danHáyati and Proto-Indo-Iranian *dʰanHáyati to Proto-Indo-European *dʰenh₂-. It shares cognate relations with Sanskrit धन् (dhan, meaning "to cause to move").
```


## [2026-09-05T18:34:38.767Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/dampaz",
 "prompt": "Give the etymology of Proto-Germanic *dampaz: PIE root cited, cognates, and descendants. Also any mention of *dimbaz or dim."
}
```


## [2026-09-05T18:34:40.280Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/d%CA%B0enh%E2%82%82-",
 "prompt": "Give the PIE root, meaning, and its descendants (Latin fons, Sanskrit, Iranian)."
}
```


### [2026-09-05T18:34:44.754Z] TOOL RESULT

```
# Etymology of Proto-Germanic *dampaz

## Etymology and Origin

According to the Wiktionary entry, *dampaz derives from **"*dimbaną ("to fog, smoke")"**, indicating a semantic connection to vapor and atmospheric phenomena.

The entry does not cite a specific PIE (Proto-Indo-European) root. The only etymological information provided is the relationship to the Proto-Germanic verb *dimbaną.

## Dual Functions

The term appears in two forms:
1. **Noun** (feminine): meaning "vapor"
2. **Adjective**: meaning "damp" or "humid"

## Notable Descendants

The word produced extensive descendants across Germanic languages:
- **English**: damp
- **German**: Dampf
- **Dutch**: damp
- **Swedish**: damm
- **Yiddish**: דאַמף (damf)

## Related Terms

The entry lists **"*dimbaną"** as the primary related term, representing the verbal root underlying the noun/adjective forms.

No mention of *dimbaz appears in the provided content; only *dimbaną (the infinitive form) is documented.
```


### [2026-09-05T18:34:45.978Z] TOOL RESULT

```
# Proto-Indo-European Root *dʰenh₂-

**Root:** *dʰenh₂- (alternative: *dʰen-)

**Meanings:** The root conveys two related concepts—"to set in motion" and "to flow."

**Key Descendants:**

- **Latin:** *fōns* (fountain, spring, source) via Proto-Italic *fontis
- **Sanskrit:** *dhána* (competition, contest, strife; prize) and related verbal forms like *dhánvati*
- **Iranian:** Persian *danidan* (to hasten, run) from a causative formation

The root appears across multiple Indo-European language families, with reflexes in Hellenic (Greek *thnḗskō*, "to die"), Tocharian (*tsnamo*, "flowing"), and Germanic traditions. Its semantic range spans from physical motion and flowing water to competitive struggle.
```


## [2026-09-05T18:34:53.513Z] TOOL CALL #48: Bash

```json
{
 "command": "ls site/pages/127.jpg 2>/dev/null; pdftoppm -f 127 -l 127 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg127 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render PDF page 127"
}
```


### [2026-09-05T18:34:55.629Z] TOOL RESULT

```
site/pages/127.jpg
total 36656
drwx------ 3 sfmqrb sfmqrb    12288 Sep  5 14:34 .
drwx------ 4 sfmqrb sfmqrb     4096 Sep  5 01:20 ..
-rw-rw-r-- 1 sfmqrb sfmqrb     4061 Sep  5 02:00 avestan.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5971 Sep  5 02:13 baga.html
-rw-rw-r-- 1 sfmqrb sfmqrb   189420 Sep  5 02:15 bqt440_bottom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   513902 Sep  5 02:15 bqt440.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   502834 Sep  5 02:02 bqt538_big.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    72705 Sep  5 02:02 bqt538_fn6.png
-rw-rw-r-- 1 sfmqrb sfmqrb    24595 Sep  5 02:02 bqt538_head2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    22593 Sep  5 02:02 bqt538_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb   207980 Sep  5 02:01 bqt538.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   282104 Sep  5 01:29 bqt733_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   669351 Sep  5 01:29 bqt733.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    17369 Sep  5 01:35 bqtv1_361_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb   470042 Sep  5 01:35 bqtv1_361.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   241161 Sep  5 01:36 bqtv1_398_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   482084 Sep  5 01:36 bqtv1_398.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   190109 Sep  5 01:35 bqtv1_399_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    53579 Sep  5 01:36 bqtv1_399_head2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1625 Sep  5 01:35 bqtv1_399_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb   510341 Sep  5 01:35 bqtv1_399.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    63555 Sep  5 01:43 build71.py
-rw-rw-r-- 1 sfmqrb sfmqrb     5214 Sep  5 02:23 build82a.py
-rw-rw-r-- 1 sfmqrb sfmqrb    53401 Sep  5 02:29 build82b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    19831 Sep  5 02:31 build82c.py
-rw-rw-r-- 1 sfmqrb sfmqrb    48417 Sep  5 10:19 build93.py
-rw-rw-r-- 1 sfmqrb sfmqrb    59425 Sep  5 10:54 build98.py
-rw-rw-r-- 1 sfmqrb sfmqrb     4811 Sep  5 02:00 bulca.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2950 Sep  5 10:15 c_anth.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2661 Sep  5 10:15 c_armonica.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5133 Sep  5 14:10 c_avestan120.png
-rw-rw-r-- 1 sfmqrb sfmqrb    22149 Sep  5 01:51 c_belloth.png
-rw-rw-r-- 1 sfmqrb sfmqrb     9603 Sep  5 10:50 c_byz2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11328 Sep  5 10:49 c_byz_persian.png
-rw-rw-r-- 1 sfmqrb sfmqrb    18289 Sep  5 13:48 c_fr.png
-rw-rw-r-- 1 sfmqrb sfmqrb    13620 Sep  5 13:48 c_germ2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10949 Sep  5 13:48 c_germ.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3138 Sep  5 10:50 c_heb1.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4953 Sep  5 10:50 c_heb2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    15141 Sep  5 13:51 c_hektaton.png
-rw-rw-r-- 1 sfmqrb sfmqrb      914 Sep  5 11:04 chicane.html
-rw-rw-r-- 1 sfmqrb sfmqrb    18737 Sep  5 13:51 c_kent.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10687 Sep  5 13:48 c_lat2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    13469 Sep  5 14:10 c_latin120.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4845 Sep  5 10:50 c_root3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30227 Sep  5 09:50 crop_ambor.png
-rw-rw-r-- 1 sfmqrb sfmqrb    25024 Sep  5 09:50 crop_berijab_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb    39114 Sep  5 09:50 crop_berijan_ar.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65413 Sep  5 09:50 crop_persian_roast.png
-rw-rw-r-- 1 sfmqrb sfmqrb    23219 Sep  5 01:51 c_schyth.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1795 Sep  5 10:50 c_scyth2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2953 Sep  5 10:50 c_scyth3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4885 Sep  5 10:49 c_scyth.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3019 Sep  5 10:15 c_sus.png
-rw-rw-r-- 1 sfmqrb sfmqrb    33345 Sep  5 10:55 e0.102.json
-rw-rw-r-- 1 sfmqrb sfmqrb    38686 Sep  5 10:34 e0.95.json
-rw-rw-r-- 1 sfmqrb sfmqrb    58057 Sep  5 02:29 e0full.json
-rw-rw-r-- 1 sfmqrb sfmqrb     4446 Sep  5 02:23 e0.json
-rw-rw-r-- 1 sfmqrb sfmqrb    26175 Sep  5 10:38 e1.95.json
-rw-rw-r-- 1 sfmqrb sfmqrb      456 Sep  5 10:56 g.py
-rw-rw-r-- 1 sfmqrb sfmqrb   445959 Sep  5 01:37 hrn126_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1213019 Sep  5 01:37 hrn126.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   456157 Sep  5 01:37 hrn127_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1278807 Sep  5 01:37 hrn127.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    24046 Sep  5 13:38 latin.png
-rw-rw-r-- 1 sfmqrb sfmqrb    49033 Sep  5 10:53 mk100.py
-rw-rw-r-- 1 sfmqrb sfmqrb    17464 Sep  5 10:55 mk102b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    25511 Sep  5 10:58 mk102c.py
-rw-rw-r-- 1 sfmqrb sfmqrb    21655 Sep  5 10:53 mk102.py
-rw-rw-r-- 1 sfmqrb sfmqrb    62559 Sep  5 11:04 mk103.py
-rw-rw-r-- 1 sfmqrb sfmqrb    79255 Sep  5 13:30 mk104.py
-rw-rw-r-- 1 sfmqrb sfmqrb    47159 Sep  5 13:30 mk105b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    31652 Sep  5 13:24 mk105.py
-rw-rw-r-- 1 sfmqrb sfmqrb    62837 Sep  5 13:37 mk108.py
-rw-rw-r-- 1 sfmqrb sfmqrb    40927 Sep  5 13:43 mk109.py
-rw-rw-r-- 1 sfmqrb sfmqrb    63862 Sep  5 13:46 mk110.py
-rw-rw-r-- 1 sfmqrb sfmqrb    48342 Sep  5 14:00 mk113.py
-rw-rw-r-- 1 sfmqrb sfmqrb    61685 Sep  5 14:01 mk114.py
-rw-rw-r-- 1 sfmqrb sfmqrb    60434 Sep  5 14:01 mk115.py
-rw-rw-r-- 1 sfmqrb sfmqrb    76964 Sep  5 14:09 mk116.py
-rw-rw-r-- 1 sfmqrb sfmqrb    58735 Sep  5 14:20 mk120.py
-rw-rw-r-- 1 sfmqrb sfmqrb    62270 Sep  5 14:32 mk121.py
-rw-rw-r-- 1 sfmqrb sfmqrb    40966 Sep  5 01:40 mk67.py
-rw-rw-r-- 1 sfmqrb sfmqrb    58318 Sep  5 01:45 mk70.py
-rw-rw-r-- 1 sfmqrb sfmqrb    78619 Sep  5 02:02 mk73.py
-rw-rw-r-- 1 sfmqrb sfmqrb    68454 Sep  5 02:01 mk75.py
-rw-rw-r-- 1 sfmqrb sfmqrb    79383 Sep  5 02:19 mk78.py
-rw-rw-r-- 1 sfmqrb sfmqrb    52793 Sep  5 02:18 mk79.py
-rw-rw-r-- 1 sfmqrb sfmqrb    57729 Sep  5 02:31 mk81.py
-rw-rw-r-- 1 sfmqrb sfmqrb    58379 Sep  5 02:39 mk83.py
-rw-rw-r-- 1 sfmqrb sfmqrb    76819 Sep  5 02:39 mk84.py
-rw-rw-r-- 1 sfmqrb sfmqrb    25181 Sep  5 02:44 mk86.py
-rw-rw-r-- 1 sfmqrb sfmqrb    67712 Sep  5 10:03 mk87.py
-rw-rw-r-- 1 sfmqrb sfmqrb    66054 Sep  5 10:10 mk89.py
-rw-rw-r-- 1 sfmqrb sfmqrb    70790 Sep  5 10:04 mk90.py
-rw-rw-r-- 1 sfmqrb sfmqrb    48553 Sep  5 10:03 mk91.py
-rw-rw-r-- 1 sfmqrb sfmqrb    27206 Sep  5 10:38 mk95b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    39501 Sep  5 10:34 mk95.py
-rw-rw-r-- 1 sfmqrb sfmqrb    49433 Sep  5 10:35 mk96.py
-rw-rw-r-- 1 sfmqrb sfmqrb    54149 Sep  5 10:47 mk97.py
-rw-rw-r-- 1 sfmqrb sfmqrb    61159 Sep  5 10:50 mk99.py
-rw-rw-r-- 1 sfmqrb sfmqrb 18949704 Sep  5 02:30 mw1872.htm
drwxrwxr-x 2 sfmqrb sfmqrb     4096 Sep  5 14:28 p117
-rw-rw-r-- 1 sfmqrb sfmqrb     1984 Sep  5 14:27 p125_butik_hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    64316 Sep  5 14:23 p125_dhemo.png
-rw-rw-r-- 1 sfmqrb sfmqrb     8603 Sep  5 14:30 p125_french.png
-rw-rw-r-- 1 sfmqrb sfmqrb    62327 Sep  5 14:23 p125_persian.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2177 Sep  5 14:27 p125_tem_hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30941 Sep  5 14:26 p125_tem.png
-rw-rw-r-- 1 sfmqrb sfmqrb    32690 Sep  5 13:24 part1.json
-rw-rw-r-- 1 sfmqrb sfmqrb     3057 Sep  5 10:05 patch87.py
-rw-rw-r-- 1 sfmqrb sfmqrb    71589 Sep  5 10:41 pg100.png
-rw-rw-r-- 1 sfmqrb sfmqrb    68145 Sep  5 10:44 pg102.png
-rw-rw-r-- 1 sfmqrb sfmqrb   114170 Sep  5 10:49 pg103_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb    79623 Sep  5 10:49 pg103.png
-rw-rw-r-- 1 sfmqrb sfmqrb   169766 Sep  5 10:57 pg104_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    22122 Sep  5 10:58 pg104_charlatan.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78826 Sep  5 10:57 pg104.png
-rw-rw-r-- 1 sfmqrb sfmqrb    31584 Sep  5 11:00 pg104_tea.png
-rw-rw-r-- 1 sfmqrb sfmqrb    82500 Sep  5 10:57 pg105.png
-rw-rw-r-- 1 sfmqrb sfmqrb    55270 Sep  5 11:01 pg106.png
-rw-rw-r-- 1 sfmqrb sfmqrb    48976 Sep  5 11:01 pg107.png
-rw-rw-r-- 1 sfmqrb sfmqrb    68501 Sep  5 13:26 pg108.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63543 Sep  5 13:30 pg109.png
-rw-rw-r-- 1 sfmqrb sfmqrb     6518 Sep  5 13:38 pg110_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb    67502 Sep  5 13:29 pg110.png
-rw-rw-r-- 1 sfmqrb sfmqrb    36325 Sep  5 13:32 pg110_yeth.png
-rw-rw-r-- 1 sfmqrb sfmqrb    46559 Sep  5 13:32 pg110_zbn.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72718 Sep  5 13:38 pg111.png
-rw-rw-r-- 1 sfmqrb sfmqrb    50381 Sep  5 13:37 pg112.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65357 Sep  5 13:45 pg113.png
-rw-rw-r-- 1 sfmqrb sfmqrb   117231 Sep  5 13:48 pg114_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1253 Sep  5 13:48 pg114_french.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11671 Sep  5 13:48 pg114_latin.png
-rw-rw-r-- 1 sfmqrb sfmqrb    83933 Sep  5 13:46 pg114.png
-rw-rw-r-- 1 sfmqrb sfmqrb   163144 Sep  5 13:51 pg115_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70699 Sep  5 13:51 pg115.png
-rw-rw-r-- 1 sfmqrb sfmqrb    64811 Sep  5 13:57 pg117.png
-rw-rw-r-- 1 sfmqrb sfmqrb    42354 Sep  5 14:05 pg118.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78691 Sep  5 14:11 pg119.png
-rw-rw-r-- 1 sfmqrb sfmqrb    84971 Sep  5 14:10 pg120_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb    50224 Sep  5 14:06 pg120.png
-rw-rw-r-- 1 sfmqrb sfmqrb   330167 Sep  5 14:18 pg121_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    82335 Sep  5 14:17 pg121.png
-rw-rw-r-- 1 sfmqrb sfmqrb   461010 Sep  5 14:18 pg121_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61026 Sep  5 14:18 pg123.png
-rw-rw-r-- 1 sfmqrb sfmqrb    91077 Sep  5 14:34 pg124.png
-rw-rw-r-- 1 sfmqrb sfmqrb   300310 Sep  5 14:27 pg125_900.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75202 Sep  5 14:23 pg125.png
-rw-rw-r-- 1 sfmqrb sfmqrb    54329 Sep  5 14:34 pg127.png
-rw-rw-r-- 1 sfmqrb sfmqrb    55169 Sep  5 01:30 pg67.png
-rw-rw-r-- 1 sfmqrb sfmqrb    57649 Sep  5 01:33 pg69.png
-rw-rw-r-- 1 sfmqrb sfmqrb    50966 Sep  5 01:33 pg69_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    77968 Sep  5 01:31 pg70.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75801 Sep  5 01:29 pg71_300.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71145 Sep  5 01:29 pg71.png
-rw-rw-r-- 1 sfmqrb sfmqrb   134140 Sep  5 01:44 pg72_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2377 Sep  5 01:44 pg72_afandi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11769 Sep  5 01:47 pg72_fr2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2947 Sep  5 01:44 pg72_fr.png
-rw-rw-r-- 1 sfmqrb sfmqrb    49860 Sep  5 01:44 pg72.png
-rw-rw-r-- 1 sfmqrb sfmqrb    81180 Sep  5 01:47 pg73.png
-rw-rw-r-- 1 sfmqrb sfmqrb    56073 Sep  5 01:48 pg74.png
-rw-rw-r-- 1 sfmqrb sfmqrb   108877 Sep  5 01:51 pg75_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb    20612 Sep  5 01:51 pg75_greeklatin.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75134 Sep  5 01:51 pg75.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66505 Sep  5 01:51 pg76.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65211 Sep  5 02:00 pg77.png
-rw-rw-r-- 1 sfmqrb sfmqrb   155334 Sep  5 02:00 pg78_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63822 Sep  5 01:59 pg78.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59439 Sep  5 02:09 pg79.png
-rw-rw-r-- 1 sfmqrb sfmqrb    58953 Sep  5 02:08 pg80.png
-rw-rw-r-- 1 sfmqrb sfmqrb    99904 Sep  5 02:15 pg81.png
-rw-rw-r-- 1 sfmqrb sfmqrb    29321 Sep  5 02:20 pg82_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    74477 Sep  5 02:20 pg82.png
-rw-rw-r-- 1 sfmqrb sfmqrb    56108 Sep  5 02:20 pg82_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   154129 Sep  5 02:25 pg83_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb     7123 Sep  5 02:26 pg83_apac.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4363 Sep  5 02:26 pg83_bohyah.png
-rw-rw-r-- 1 sfmqrb sfmqrb    67094 Sep  5 02:25 pg83.png
-rw-rw-r-- 1 sfmqrb sfmqrb    82358 Sep  5 02:23 pg84.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63329 Sep  5 02:25 pg85.png
-rw-rw-r-- 1 sfmqrb sfmqrb    31530 Sep  5 02:35 pg86.png
-rw-rw-r-- 1 sfmqrb sfmqrb    79874 Sep  5 09:47 pg87.png
-rw-rw-r-- 1 sfmqrb sfmqrb   134852 Sep  5 09:54 pg88_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11747 Sep  5 09:54 pg88_e0spine.png
-rw-rw-r-- 1 sfmqrb sfmqrb    31391 Sep  5 09:55 pg88_join.png
-rw-rw-r-- 1 sfmqrb sfmqrb    98452 Sep  5 09:54 pg88.png
-rw-rw-r-- 1 sfmqrb sfmqrb    26700 Sep  5 09:54 pg88_spine.png
-rw-rw-r-- 1 sfmqrb sfmqrb   171528 Sep  5 02:45 pg89_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4628 Sep  5 02:45 pg89_ambor.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4924 Sep  5 02:45 pg89_berijan.png
-rw-rw-r-- 1 sfmqrb sfmqrb    80984 Sep  5 09:49 pg89.png
-rw-rw-r-- 1 sfmqrb sfmqrb    77182 Sep  5 09:48 pg90.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63799 Sep  5 09:55 pg91.png
-rw-rw-r-- 1 sfmqrb sfmqrb   157177 Sep  5 10:09 pg92_500.png
-rw-rw-r-- 1 sfmqrb sfmqrb     8494 Sep  5 10:09 pg92_avestan.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3476 Sep  5 10:09 pg92_pahlavi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    90918 Sep  5 10:07 pg92.png
-rw-rw-r-- 1 sfmqrb sfmqrb    93420 Sep  5 10:15 pg94.png
-rw-rw-r-- 1 sfmqrb sfmqrb    44047 Sep  5 10:16 pg94_sogd.png
-rw-rw-r-- 1 sfmqrb sfmqrb    49714 Sep  5 10:16 pg94_urvar.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78178 Sep  5 10:11 pg95.png
-rw-rw-r-- 1 sfmqrb sfmqrb   163439 Sep  5 10:15 pg96_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72929 Sep  5 10:15 pg96.png
-rw-rw-r-- 1 sfmqrb sfmqrb   101597 Sep  5 10:41 pg99_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb     8738 Sep  5 10:41 pg99_french.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65608 Sep  5 10:40 pg99.png
```


## [2026-09-05T18:34:58.245Z] TOOL CALL #49: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg127.png"
}
```


### [2026-09-05T18:34:58.692Z] TOOL RESULT

```

```


## [2026-09-05T18:34:58.689Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T18:35:09.050Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD Bd1 dhem:\"; grep -n \"dhem\\|dhen\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -20",
 "description": "Grep Walde-Pokorny Bd1"
}
```


### [2026-09-05T18:35:09.103Z] TOOL RESULT

```
=== WLD Bd1 dhem:
23887:wegung sein‘ (dieselben Bed.-Yerhiiltnisse bei *dhen-, s. d.). Aus qn- 
49901:dengiii „decke“ und dt. Dung unter *dhengh- „deckend worauf liegen“ 
49934:gelingen“, iiberzeugt nicht ; vielmehr s. Wz. dhengh-. 
49938:zayvs .,schnell‘ unter idg. *dheng- aus Griinden der Bed. nicbt vorzuziehen; 
51981:sammenfiigung, congeries", s. u. *dhe- „setzen" und *dhembh- ,,graben"). 
51989:u. dhembli- ,,graben“). — Ai. dablura- „gering, diirftig" scheint mir trotz 
52001:nur postuliert‘) und Persson Beitr. 39 f. (s. u. dhen- ,,Flache"). 
52195:beuegy • fie fiat a [oe/ur>], in welcher Bed. zu *dhem- „stieben“] evara&rjg lies, 
52275:chen von vierfuBigen Tieren", ai. dhena „Milchkuh", dhlta- „gesogen“, 
52365:ahd. tenni „Tenne“ als „granary“ anreiht; s. dariiber *dhen- „Flache r ‘), da 
52647:dheu-, dhena- x (vermutlich *dheue-, vgl. die Erw. *dheue-h-, *dheue-s-) 
52869:2. dh- Erw. dhen-dh- „durcheinanderwirbeln, schiitteln, verwirren, auch 
53050:dhen- 
53575:i Jcd/uos, Bgm. II 2 1, 231; s. auch Falk-Torp u. dam, und u. *dhemblt- 
53593:die nasalierten Formen ( *dhembh -) sind nach Bartholomae IF. 7, 82 ff. 
53610:dhem-, dhema 1 - 
53642:dhem-, dhema*- „stieben, rauchen (Rauch, Dunst, Nebel; nebelgrau, rauch- 
53681:(dhembh-), dhmbli- — dhen- 
53705:(dhembh-), dhmbli- „graben“. 
53728:1. dhen- „laufen, rennen; rinnen".
```


## [2026-09-05T18:35:10.795Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LAT fons:\"; grep -n \"fons\\b\" LAT.txt | head -10; echo \"=== LEW fons:\"; grep -n \"fons,\" LEW_1910.txt | head -10; echo \"=== IEC dhen:\"; grep -n \"dhen-\\|dhemos\\|dhemo-\" IEC.txt | head -10",
 "description": "Grep Latin dictionaries and Mann"
}
```


### [2026-09-05T18:35:10.880Z] TOOL RESULT

```
=== LAT fons:
99:mentionner le rapprochement de fons , fontis avec skr .dhdnvati
21056:(Gloss.), qu'on retrouve dans 1 1 adj. osbrien fons "fauSns" (nos.plur.
23342:fons, fontis m.(fem. en bas-latin, cf.Thes. VI 102?, 38sqq.; theme
23347:baptene: fons baptismi, baptismatis, et 1’endroit ou l'on baptise,
24878:5,133, fons unde fund-itur e terra aqua uiua, ut fistula a qua fusus
71096:fons ombr., 393.
=== LEW fons:
362:fratrum, fratrom, frater I 542 frehtef, frehtu I 548 frif, fri I 552 frite I 505, II 4387 frosetom I 543 futa I 504, 505, 558 fuzest I 504, 505 Fulonie I 561 fons, foner I 464 Funtlere, fondlire I 525 furent I 557, II 629 furfant I 473 furo, furu I 537 fust I 557, 558, II 629 futu I 557, 558 Grabovio- I 171, 614 gomia I 587, 626 habe I 630, 868 habiest, habia I 680 habina(f) I 23 habitu, habetu, ha- burent I 630 hahtu I 630
=== IEC dhen:
2755:dheió (1) ‘suckle, milk; suck at the breast’. Cf. dhen- (1), dhinió. WP I, 829, and see dhoið Skt. dhayami; Av. dà-; Oss. däin, dajun, pp. dadton; Arm. diem; Gk. inf. thé-sthai "be suckled'; Hes. thenion ‘milk’, gala-thenós, aj. tunweaned'; Lat. cf. fe-mina; OHG Gen. lsg: taju beside MLG dien ‘suck, suckle’; OE dēon ‘suck’; cf. diend ‘suckling’; Sw. di ‘suck’; giva di ‘suckle’; Latv. dejals ‘mother’s milk, accretion of milk’. For Sw. dägga ‘suckle’ and OCS dojo, id. see dhoið. (NB. Per. dāyā ‘nurse, wetnurse, midwife�� is an Arabic LW). ON akr-dái “galeopsis? may belong here.
2787:dhen- (2) ‘forehead, temple’ MHG cf. tinne ‘forehead’; pl. ‘temples’; Latv. cf. deņini ‘temples’
2801:dhenguhó, ið ‘cover, protect. Cf. dhonguh-, dhnguh- Skt. danghami ‘ward off; protect; Li. den- giù, denen (1) ‘cover’. Isophonic w. MHG tinge ‘forehead’; pl. ‘temples’. Cf. dhen- (1) and (2) and for sense cf. Gk. kró-taphos ‘temple’
2912:dhinió ‘suckle, nourish; suck’. Cf. dheio- (1) and dhen- (3) Skt. cf. dhinomi ‘nourish, satisfy, cheer’ (fr. *dhi-neu-); OIr. dinim, denim 'suckle; suck?
2942:dhngh- (1) “press, force; pressing’. Cf. dhen- guh- (2), variant: dhengh- Gk. takhüs, comp. thàásson; MHG tungen, tüngen (2) ‘oppress, harass’; Ukr. cf. v- djahnutysja “force one’s way in’? Cf. dhongh-
14115:quo-dhen (-dhən-, -dhə) ‘by, in what; to, from what; where’. WP I, 523 Av. kaða ‘how’; Per. -kada, -keda “-where, -place'; Hitt. (ambig.) cf. kwatan, kwatin ‘whither; why’; Gk. (ambig.) póthen ‘whence’; Alb. kah as prp. 'towards'; Osc. cf. puf, Umb. pufe “anywhere”; MIr. caidhe, interrog. ‘what; where’; Go. hwad, hwad- ‘whither’; ON hva- óan ‘whence’; (z-gde in) OCS küde ‘where’ (and com. Sl.); beside Srb. kod ‘among, care of; Li. cf. kadan-gi because’, fr. *quodhen- ghi or sim.)
19527:ūdhər (üdhen-) ‘udder, teat. (Gk. variant uüdhər-, -en- ?). WP I, 111 Skt. üdhar, n., ūdhas, n., udhan, n. ‘udder’; Av. udaro, m. ‘belly’; Gk. cf. oüthar, gs: oGthatos, n. id. perb. w def. article; Lat. über, gs: überis, n. as Skt.; OS üdar, sm. & n., MHG üter & iuter, id. w. def. art.?; LG üder, n. id.; Du. uier, m. ‘teat’; (LW in Finn. udar *udder and in Marian or Cheremis vádar, vodár, id. Mod. Eng. udder shortened fr. OE Oder. n. id. Cf. Li. adróta, adj. f. *milch-; in calf, in pig”, etc.)
```


## [2026-09-05T18:35:15.948Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '53640,53660p;53728,53760p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt",
 "description": "Read Walde-Pokorny dhem/dhen"
}
```


### [2026-09-05T18:35:16.001Z] TOOL RESULT

```
„wenig, gering, dfirftig" ; das gr. Wort stammt aus Italien, s. Yf. LEWb. 2 782. 

dhem-, dhema*- „stieben, rauchen (Rauch, Dunst, Nebel; nebelgrau, rauch- 
farben = dfister, dunkel), wehen, blasen (hauchen = riechen)“. Be- 
deutungsumfang wie bei Wz. *dheii- „stieben“. 

Ai. dhamati „blast“ ( dhami-syati , -ta- und dhmnta -, pass, dhamyate und 
dhmaydte), av. dadmainya- „sich aufblasend, blahend, von Froschen“ (siehe 
Bartholomae Airan. Wb. 731 f.), npers. damtdan „blasen, wehen“, darn 
„Atem, Atemzug“ (Horn Np. Et. 127), osset. dunmn , dimin „rauchen; wehen, 
blasen“ (p-Erw. ? Hfibschmann Et. und Ltl. d. Oss. Spr. 37); 

Gr. de/uegog ,,asuvog“, de/xegdmig „ernst, finster blickend“ (: ahd. timber 
„finster“; Fick BB. 17, 323, Wb. I 4 464; verschieden davon ist de/uegr] • fiefiaia 
. . . Evaradrjg Hes., siehe darfiber oben S. 828 s. v. dhe- u. Schulze Quaestiones 
ep. 224 A. 4), mir. dem „schwarz, dunkel“, deime „Dunkelheit K (Johansson 
IF. 4 145 Anm. 1, Fick II 4 147); norw. daam ( *dhetno -) „dunkel“, daame 
m. „Wolkenschleier“, daam m. „Geschmack. Geruch“ = anord. damr „Ge- 
schmack"; mit Gutt.-Erw. anord. dqkk f. „Yertiefung in der Landschaft“ 
= lett. danga ,.kotige Pffitze, morastiges Land, Meeresschlamm“, ferner 
anord. dfikkr , afries. diunk „dunkel“ (germ. *denkm-), tiefstufig as. dunkar, 
1. dhen- „laufen, rennen; rinnen". 

Ai. dhanayati „rennt, liiuft, setzt in Bewegung", np. danidan „eilen, 

laufen", ai. dhanvati „rennt, lauft, flieBt", ap. danuvatiy , flieBt", ai. dhdnu- 

tar- „rennend, flieBend '; lat. wabrscheinlich fons, -tis „Quelle“. Bugge 

Curt. St. 4, 343 f., BB. 14, 78, Fick I 4 74, 463, Brugmann BSGW. 1893, 

144, Yf. LEWb. 2 s. v. (wo iiber andere Deutungen von fons). 

Fernzuhalten sind gr. dig, dt. Dime (s. dheti- „stieben") und ai. dhanus - 

dhanvan- „trockenes Land" (s. *dhen- „Flache“). Danuvius „Donau“ kelt. 

Entw. aus * dhonu-1 Ygl. vielmekr oben S. 763. 



dhen- 


853 


2. dhen- „Flache der Hand, des Erdbodens, fiaches Brett 11 . 

Gr. ■divciQ n. „Handflache, FuBsohle, auch von der Flache des Heeres 
oder von der Vertiefung im Altar zur Aufnahme der Opfergaben“, om- 
odevaQ „Handriicken 11 o d (.van), abd. tenar m., tenra f. ( *denard -), 

mhd. tener m. „flache Hand“, Curtius 5 255 (samt ai. dhanns-. s. u.), Fick
```


## [2026-09-05T18:35:16.940Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '90,110p' LAT.txt; echo \"===\"; sed -n '23342,23365p' LAT.txt",
 "description": "Read Ernout-Meillet fons"
}
```


### [2026-09-05T18:35:17.011Z] TOOL RESULT

```
maire comparce, toute preuve s'exprime par la formule: "la
concordance ne saurait etre fortuite", Un rapprochement perd
donc en valeur probante tout ce q u 'il gagne en facilitd.
C est ce que les dtymologistes perdent parfois de vue.
Si le rapprochement de -pecu avec fihu du vieux haut alle-
mand et fagu du vddique satisfait, c'est qu'il ne saurait
etre fortuit que trois mots concordent k ce point pour la
forme, le genre, la structure et l'emploij il continuent
donc un seul et mSme mot indo-europden. Si l*on n'a fait que
mentionner le rapprochement de fons , fontis avec skr .dhdnvati
11 court, il coule rapidement",,c'est que f- initial du
latin admet des origines multiples, que la concordance ne
s etend pas au delA de la racine, et que la ressemblance de
sens est vague et g6n6rale. Et si 1'on n'a m^me pas mentionnd
le rapprochement de gruS dans con-grud , in-grud .avec ruo et- V 11 ",
avec gr. -'/pauco, etc.,c'est que le sens n'appuie pas 1'id6e
que con-grutf et in—gruG alent rien k faire avec ruo, et que
le gr. -/pauco est loin de toutes maniores. Peut-gtre s'est-on
encore trop conformd k 1'usage en signalant nombre d'6ty-
mologies qui n'ont pour elles qu'un peu de vralsemblance.
Mais on espbre qu'aucune Atymologie sure ne manque, et
===
fons, fontis m.(fem. en bas-latin, cf.Thes. VI 102?, 38sqq.; theme
en -t-: le g 4 n.pl. est fontium', abl.sg. en -i ou en -e ( fontei et
fonte dans la Sent.Minuciorun), acc.pl. en -is ou en -es, cf.Varr.,
L.L.8,66; 9,113: source, fontaine; = gr.7rr}Yr), xpT]VT]. Sens propre et
figur 4 ; dans la langue de 1 'figl. 3 'emploie pour designer l'eau du
baptene: fons baptismi, baptismatis, et 1’endroit ou l'on baptise,
cf.fr. fonts. Panroman, sauf rounain. Usit 4 de tout tenps. M.L.3435.
Derives: fontanus, d'ou fontSna f. (sc. a<7ua),panroman; M.L.3436, et
en celt.: gall. fynnon, etc.; fontaneus; Fontanal ia, - ium; fontalis',
fonticulus m.; fontinalis; Fontinalia', Fonteius; fontius (Granm.);
fontiuus (Orib.), d'aprbs natiuus ?
Composes savants: fonti-cola, -gena.
Rattache par les inciens a fundo, cf.P.F.74,38, sans doute a cause
de la prononciation avec o fern 4 , not 4 e funtes, signal 4 e par Prisc.
GLK II 37 >i, uetustissini... proferentes "funtes" pro "fontes"... quae
tamen iunioribus repudiata sunt quasi rustico more dicta, et qu'on
retrouve sur un cachet d'oculiste, cf.Thes. VI 1038,31. Sur cette
prononciation, v.Baehrens, Sprach. Komm.z.App. Probi, p.54, et cf. frons,
fruns.
Ombr.Funtlere, Fondlire "in Fontulis (?)" est un non propre sur
lequel on ne peut rien appuyer. On rapproche skr. dhanvati, dhandyati
"il court, il coule". Le vocalisme -o- indique un ancien nom racine;
la forme en -ti- ne peut etre que secondaire; cf. mons. Sans doute
vieux mot religieux, qui ne se retrouve nulle part ailleurs.
```


## [2026-09-05T18:35:26.667Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SKT damp:\"; grep -n \"^DAMP\\|DAMP,\\|DIM,\" SKT.txt | head -10",
 "description": "Grep Skeat"
}
```


### [2026-09-05T18:35:26.717Z] TOOL RESULT

```
=== SKT damp:
```


## [2026-09-05T18:35:27.359Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== ARY latin index DHEM/DHEN:\"; grep -n \"DHEM\\|DHEN\\|dhem\\|dhen\" incoming/ARY/ARY_latin_index_pages.txt | head -20",
 "description": "Grep Aryanpur index"
}
```


### [2026-09-05T18:35:27.414Z] TOOL RESULT

```
=== ARY latin index DHEM/DHEN:
7656:MALLORY & ADAMS 7 DHEN BARNHART:
7662:*DHE, “DHENA, “DHEDHN., *DHELU, *DHEI- (INDO-EUROPEAN) igtlysl 9 ie
8750:DELAMARRE: (LIBRE) 226 LODHENN
```


## [2026-09-05T18:35:29.937Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"damp\" SKT.txt | head -8; echo \"=== dim:\"; grep -n -i \"^dim\\|Dim, adj\\|DIM (E\" SKT.txt | head -8",
 "description": "Grep Skeat again"
}
```


### [2026-09-05T18:35:30.003Z] TOOL RESULT

```
3594:cloy.  (F.  —  L.)    Orig.  to  stop  up,  hence' sate-    O  F.  c foyer,  '  to  cloy,  slop  np,'  Cot. ; a  by  fonn  of  F.  doutr  {O.  F.  doer),  to  nail, fasten  up.     [A  horse  pricked  wilii  a  noil, in  shoeing,  wis  said  to  be  chyedJ^^O. eh,  F.  clou,  a  nail,  as  above. Clove  {i),  a  bulb;  see  Oleave  (i). Clover.  (E.>    M.E,  r/ar^r.   A.S.  da/re. trefoil. +  Dii.  khiver,   Swed.   klo/ver,  Dan. klUver,  G.Al/e.   ^  The  supposed  connection with  cleave  (i)  is  very  doubtful. Clown.  (Scand.)   led-  kiunni,  a  clumsy, boorish  fellow;  Swed.  diaL  klunn,  a  log. kiuHS,  a  clownish  fellow;  Dan.  klunf,  a log;  cf.  Dan.  kluntet,  clumsy.     Allied  to Clump.    The  orig.  sense  is  •  a  log.'     Sec Clumsy. Cloy  ;  sec  Clova  (i). Club  (i).  a  stick :  see  damp. Club  (i),  an  association  ;  see  Clamp Cluck-  (E.)    See  Clack. Clue  ;  see  Clew. Clump ;  see  Clamp. Clunuy.  (Scand.)    From  M.E.r/Mwx/i ciomsed,  benumbed ;  benumbed  fingers  are clumsy.    This  is  the  pp.  of  clomsen,  to  be- numb, or  to  feel  benumbed.  — Swed.  dial. klummun^   benumbed    (Kicti) ;    cf.   IceL klumsa,  lockjaw.     From   the  Teut.    base KLAM,    KRAM,  to   pinch,    whence  also Clamp.    Cramp.     Cf.    Du,    kUmmen,    to pinch.  •^/<'tf/ru-»,  to  be  betiumbed,  kleumsch^ numb  with  cold. Cluster,  a  bunch,    (E)      A.  S.  dtattr, clysUr,  a  bunch.     Allied  to  led   ilAstr^  a bunch,   klasi,  a  duster;  Dan.   and  Sw klau,  %  duster.     We  also  find  Swcil.  d klyi$e,  the  same  as  klifsa,  a  daslcr,  from klibba,  to  cleave,  stick  to.     This  links  it  to Cleave  (j). Clutch :  see  Latoh. 'Clutter  (I),  a  din ;  sec  Clatter. -Clutter  ^a),  to  clot ;  see  Olot. Clutter  (3>,  a  confuseil  heap;  to  hea up.  (W.)     W.  ^/JM^/,  a  heap,  pile;  cl\ einv.  to  heap  up ClysLer.  ^U-Gk.)    L.  cl/tfer,  *o
4663:Dam.n,  to  condemn.  (F.  — L)  M.  E. dammen,  dampn^H.  —  F.  damner  —  L. damnart,  to  condemn,  fiDC.  —  I*,  damnum, loss,  fine,  penalty.
4669:Damp.  <E.)  Cf.  M.  E.  dam/tm,  I focate.  Not  in  A.  S.  +  On  damp,  if steam ;  r>an.  damp,  G.  damp/,  ti Swcd.  damb,  dust.  Allic^l  lo  Gk. vapour,  Skt.  dkiipa^  iDcenae. Sec  Dust.
5565:Dumps,    melancholy.    (Scand.) dial,    duifipin.    mclanchol)',    orig difftba.  to  sleom,  reek ;  Dan.  durn^ low.  +  Du.  domp,  damp,  hazy,  G damp.     Allied   to   Damp^   ct   *lo one's  spiiits.'
12091:muaty,  mouldy,  damp.  (L.)  A  doublet of  moistyt  used  by  Chancer  in  the  sense  o( 'new,*  but  by  Ascham  in  Ihe  sense  of 'moist*  — L.  mustau  (above).  Prob.  coo- fused  with  O.  F.  moifit  'mouldy,  musty, fusty,'  Cot:  from  which,  however,  it cannot  possibly  be  derived.
17441:slag,  slagi,  wet,  damp,   water  penc-
=== dim:
174:dimut — diminutive,
1873:dim- lifted.  (Snnd.)  ME.
3466:dimin.  of  cirrus,  a  ring,  circle;  see  Ring.
4807:dime,  the  tenth  part  of  a  dollar.  (F.— L, )  F.  di'ffUf  O.  F.  disme^  tenth,  ••  L. dtiitfius,  tenth. —L.  dectm,
4845:dimple,  a  small  hollow.  (Scand. ) NaalisoJ  form  of  Nonreg.  dtpil,  difti,  a pool ;  dimin.  of  dapi,  a  pool ;  see  dapple above.    Cf.  Swed.  dial,  difp,  a  pool.
5094:Dimpl«;  see  Doap.
11611:diminish,  to  lesceo.  (F  -L.)  Coiiicd from  L,  t/i-  («(/«),  aparl,  and  E.  mtitii/f, in  imitation  of  L.  diminuere,  to  dimini&b (below).
11612:dimlnutioa  (F.-L.)  F.  t/imi/it/rim. *L.  ace.  diminitluincm^  diminution.*  L. diminutus,  pp.  oi  diminufrt,  to  lessen.— L.  (//•  (  —diM),  apnrt ;  minutre,  to  les^n.
```


## [2026-09-05T18:35:30.878Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '7650,7670p' incoming/ARY/ARY_latin_index_pages.txt",
 "description": "Aryanpur DHEN context"
}
```


### [2026-09-05T18:35:30.941Z] TOOL RESULT

```
DAGG (QUX(SHEDISH) 54 yo FINTINA ARUMANIAN) gly,
DAUW DUTCH) «gle FONTE PORTUGUESE) Ji
[pdf page 265]
eh Le
SKEAT: ‘REFERENCES beth
HEY) 75, DEM 167 POKORNY
MALLORY & ADAMS 7 DHEN BARNHART:
a seas aabicl (FOUNTAL) 404, (DEW) 273
ONIONS: (DEW) 263
: eatloak
hatte (ah A gslagy GUd;) OT 5I tl slabs 9 oY Obj 22 Ss tl o>
eet ei gend slab 22 ao ctl er
*DHE, “DHENA, “DHEDHN., *DHELU, *DHEI- (INDO-EUROPEAN) igtlysl 9 ie
DOJITI DAENO., DAENU-  :(AVESTAN) 3!
DENAID (LITHUANIAN) 3-3 DAYAK, DAYAG — (PAHLAVI) 5 shy
DEJU LATVIAN) (3) 5 DAIN, DAYUN AOSSETIC) sn 3}
DADAN (OLD PRUSSIAN) oS 3.4 DAIN, DAYE, DAE (KURDISH) 62,
DYNU WELSH) 59 DAL (BALUCHI) > sh
DENAFF XBRETON) 334 DAYI 4AFGHAND) (54) lait
DJATHE ALBANIAN) gisT DHA. DHATRI (SANSKRIT) <2 Sse
DAYEAK ARMENIAN) gs)!
```


## [2026-09-05T18:35:40.957Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"دمیدن\\|دنیدن\" incoming/ARY/ARY_pages.txt | head -10",
 "description": "Grep Aryanpur Persian"
}
```


### [2026-09-05T18:35:41.012Z] TOOL RESULT

```
1241:معنی دمیدن) بسیار شبیه واژه‌ی - ۳8۷1۷7(در زبان سرخپوستان ایالت اورگان در امریکا) است ولی
5032:فارسی (//۳8288/4): پف (به چم "فوت") پک (به چم "درون دمیدن دود سیکار و غیره)
5311:چم کلی واژه‌های اين فهرست: دمیدن» دم آهنگری» بادکردگی» بادکردن؛ تاول.
8302:دمیدن (به چم "نفس کشیدن" و "فرت کردن یا ورزیدن") / ۲۸۳
8311:۱ بازگشت به: دمیدن.
```


## [2026-09-05T18:35:43.679Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5300,5340p' incoming/ARY/ARY_pages.txt; echo \"==== pdf tag:\"; awk 'NR<5340 && /\\[pdf page/ {ln=NR; l=$0} END{print ln,l}' incoming/ARY/ARY_pages.txt",
 "description": "Aryanpur damidan entry"
}
```


### [2026-09-05T18:35:45.218Z] TOOL RESULT

```
آلمانی (057417): نداد ۳۵۲8 رونام
انگلیسی کهن (201(/5 ضان): پروسی کهن (۳۸۷554۸ ۰:00 88138
8 ,تا
انگلیسی (8701-7370): ۳ پسگشت‌ها 5
دانمارکي (0۸(۷1317): ۳57 48 ۶08۵3
سوئدی (817521/53[7): انا 0 (۳5۴) + همه
نروژی (۵/07(7501۸(۷+ ۳05۸ 1 (855) :0008
هلندی (01704): 7 ,80 لغت‌نامه دهخدا: ‏ ۵۶۶۵ و ۵۸۰۳ و ۵۶۶۳
اسلاوی کهن (ع1/ما5 8677 7ل) (0): برهان قاطع 9 ۴۸
1 ها فرهنگ معین : دیا دنا هرن
بادداشت:
چم کلی واژه‌های اين فهرست: دمیدن» دم آهنگری» بادکردگی» بادکردن؛ تاول.
پپلوی (/تماتنمم: ۰ ۳0۷1911۲10 ,20 نروژی (077501۸/: ۳05۸
سانسکریت. (54۸5507): لینرانی (40۷لهلابط7ل):
9 ,8۳738۷۸۷۸7 71 5۳۸100
آرمنی (/(۸۵15): - اد دا ما آلبانی (۵۸اللهقلهم. االزا یا
یونانی 6۶۵8/0): ۰ 8۳81700 ,87300
الاتین (710)(شاید) ار ان پسگشت‌ها 5
۱ ایسلند ی کیره (۸0 ۲ باباایی 5 صا۵): 998999 ۶080800
+ 8۳07۸ ,87707 9 ,13 (ن81) :18 2/(قکل ۸/۸
نورس گهن (ت۸08 0ا0): ار ان 8 (878) 51
ساکسونی کهن ((2430 ۰:00 8۳107 اراد و( :لح 2 هگا
آلمانی کهن (0872/۸2 07اب 82102:0120 برهان قاطع ؛ ۴7۹
آلمانی (028۵۷): 35 فرهنگ معین + ۸۴۳-۴
انگلیسی کهن (20/08/8 02: 8۳03۷۸0۷ لغت‌نامه دهخدا : ۳ و ۵۸۲۵
[pdf page 181]
۲ بر
بادداشت:
۱- 5168۸7 معتقد است که واژه‌های 5۳880 ,۳09۳8 ,8۳۸۳5 هم از همین واجريشه آمده‌اند.
۲ چم این واژه در برخی زبان‌های هند و اروپایی: موفق شدن» تغذیه کردن.. . ۹
یی
اوستایی (/۸1857۸0): -۳080817 ,۳۸۹3811۰ لینوانی (۸(1۵07نا7(7/): دنت انا
پهثری (/۲مالم): 6نارآ2۸31 ,۳۸3716
اوستی (0598710): 3/5 پسگشت‌ها شید ۲
کردی (/۷۵/9: ۰ ۳۸۲۵۲ ,نآ8 22 0 2000
اففانی (پشتر) (/۲)4۳6//۸۸۷شاید) ۳1081778 2 (8708) :۸۸05/2/5
سانسکریت. (54(37007):-۳۸5۷۸,-817 ۳۸3 برهان قاطع : ۳۳۰
اسلاوی کهن (1/70ا5 7126( صا0): فرهنگ معین , ۸۳۵
اناد توا
یادداشت:
چم این واژه در زبان لیتوانی: سیئه.
==== pdf tag:
5325 [pdf page 181]
```


## [2026-09-05T18:35:56.613Z] TOOL CALL #60: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/damH-",
 "prompt": "Give the reconstructed Proto-Iranian root, meaning, PIE source and descendants (Avestan, Middle Persian, Persian)."
}
```


## [2026-09-05T18:35:58.158Z] TOOL CALL #61: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%D9%85#Persian",
 "prompt": "For the Persian entry دم (dam): give the etymologies listed (which dam means breath, which means tail), with Middle Persian forms."
}
```


### [2026-09-05T18:35:58.539Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-05T18:36:05.274Z] TOOL RESULT

```
# Persian دم (dam) Etymologies

Based on the Wiktionary entry, Persian has multiple etymologies for دم:

## Tail Meaning
Etymology 1 derives from earlier دُنْب (dunb). The entry states: "From earlier _[دُنْب](/wiki/%D8%AF%D9%86%D8%A8#Persian "دنب")_ (dunb), see there for more." A Middle Persian form is referenced but not fully displayed in the accessible text.

## Breath Meaning
Etymology 2 traces through: "From [Middle Persian](https://en.wikipedia.org/wiki/Middle_Persian "w:Middle Persian") \[script needed\] (dam), from [Proto-Iranian](https://en.wikipedia.org/wiki/Proto-Iranian_language "w:Proto-Iranian language") _[\*damH](/w/index.php?title=Reconstruction:Proto-Iranian/damH&action=edit&redlink=1 "Reconstruction:Proto-Iranian/damH (page does not exist)")_"

The proto-form meant "to blow, breathe; to swell," ultimately deriving from Proto-Indo-European _[\*dʰemH-](/w/index.php?title=Reconstruction:Proto-Indo-European/d%CA%B0emH-&action=edit&redlink=1"Reconstruction:Proto-Indo-European/dʰemH- (page does not exist)")_ ("to blow").
```


## [2026-09-05T18:36:14.307Z] TOOL CALL #62: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%D8%AF%D9%85%DB%8C%D8%AF%D9%86|page 127 Dhem, Persian damidan: MP damidan/daftan < PIr *damH < PIE *dhemH-\" \\\n \"https://en.wiktionary.org/wiki/%D8%AF%D9%85|page 127 Dhem, Persian dam: two etymologies, breath (MP dam < PIr *damH) vs tail (< dunb)\" \\\n \"https://en.wiktionary.org/wiki/%D8%AF%D9%85%D8%A7%D9%88%D9%86%D8%AF|page 127 Dhem, Damavand: from MP dumbawand, i.e. the dumb root not dam- vapor\" \\\n \"https://www.etymonline.com/word/damp|page 127 Dhem, English damp < MLG damp, PGmc *dampaz\" \\\n \"https://www.etymonline.com/word/dim|page 127 Dhem, English dim < PGmc *dimbaz, not known outside Germanic\" \\\n ; do url=\"${u%%|*}\"; note=\"${u#*|}\"; python3 tools/fetch_source.py \"$url\" --note \"$note\"; done 2>&1 | tail -20",
 "description": "Archive first batch of web sources"
}
```


### [2026-09-05T18:36:17.306Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/fffecb896b08a176.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0877deedd98d20e4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/420db2b5a3027c09.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4fda095741cd94af.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b1a98f278ed8c713.txt
```


## [2026-09-05T18:36:23.617Z] TOOL CALL #63: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/damp|page 127 Dhem, English damp: PGmc *dampaz\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/dampaz|page 127 Dhem, PGmc *dampaz < *dimbana to fog, smoke\" \\\n \"https://en.wiktionary.org/wiki/%D8%AF%D9%86%DB%8C%D8%AF%D9%86|page 127 Dhen, Persian danidan: PIr *danHayati < PIE *dhenh2-, to run with joy\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/d%CA%B0enh%E2%82%82-|page 127 Dhen root: PIE *dhenh2- to set in motion, flow; Latin fons, Persian danidan\" \\\n \"https://www.etymonline.com/word/fountain|page 127 Dhen, English fountain < OFr fontaine < L fons, fontis, PIE *dhen-\" \\\n ; do url=\"${u%%|*}\"; note=\"${u#*|}\"; python3 tools/fetch_source.py \"$url\" --note \"$note\"; done 2>&1 | tail -20",
 "description": "Archive second batch of web sources"
}
```


### [2026-09-05T18:36:26.593Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/1af19c8d379c6cb8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1488e57a27735771.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/eccc9672337332f2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b52f792505b7bbf8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d9d5e8e6a1cbfa78.txt
```


## [2026-09-05T18:36:28.880Z] TOOL CALL #64: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py",
 "description": "Read verify_check tool"
}
```


### [2026-09-05T18:36:28.953Z] TOOL RESULT

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


## [2026-09-05T18:37:25.165Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC dhen 1:\"; grep -n \"dhen- (1)\\|dhen- (3)\" IEC.txt | head -5; echo \"=== KLN fountain:\"; grep -n \"fountain, n\\.\\|^fountain\" KLN_1966.txt | head -5; echo \"=== KLN font:\"; grep -n \"font, n\\.\" KLN_1966.txt | head -5",
 "description": "Grep Mann and Klein for fountain"
}
```


### [2026-09-05T18:37:25.265Z] TOOL RESULT

```
=== IEC dhen 1:
2755:dheió (1) ‘suckle, milk; suck at the breast’. Cf. dhen- (1), dhinió. WP I, 829, and see dhoið Skt. dhayami; Av. dà-; Oss. däin, dajun, pp. dadton; Arm. diem; Gk. inf. thé-sthai "be suckled'; Hes. thenion ‘milk’, gala-thenós, aj. tunweaned'; Lat. cf. fe-mina; OHG Gen. lsg: taju beside MLG dien ‘suck, suckle’; OE dēon ‘suck’; cf. diend ‘suckling’; Sw. di ‘suck’; giva di ‘suckle’; Latv. dejals ‘mother’s milk, accretion of milk’. For Sw. dägga ‘suckle’ and OCS dojo, id. see dhoið. (NB. Per. dāyā ‘nurse, wetnurse, midwife�� is an Arabic LW). ON akr-dái “galeopsis? may belong here.
2801:dhenguhó, ið ‘cover, protect. Cf. dhonguh-, dhnguh- Skt. danghami ‘ward off; protect; Li. den- giù, denen (1) ‘cover’. Isophonic w. MHG tinge ‘forehead’; pl. ‘temples’. Cf. dhen- (1) and (2) and for sense cf. Gk. kró-taphos ‘temple’
2912:dhinió ‘suckle, nourish; suck’. Cf. dheio- (1) and dhen- (3) Skt. cf. dhinomi ‘nourish, satisfy, cheer’ (fr. *dhi-neu-); OIr. dinim, denim 'suckle; suck?
=== KLN fountain:
=== KLN font:
```


## [2026-09-05T18:37:28.384Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"fontana\\|fontaine\" KLN_1966.txt | head -5; echo \"=== Mann dhonos/dhentis:\"; grep -n \"dhonos\\|dhontis\\|dhonis\\|dhen-, \" IEC.txt | head -5",
 "description": "Klein fontaine, Mann dhon"
}
```


### [2026-09-05T18:37:28.455Z] TOOL RESULT

```
15106:receive  hospitably,  entertain’.  Cp.  Sp.  alfondega, which  derives  fr.  Arab,  al-,  ‘the’,  and  funduq, ‘inn’,  and  see  pandect.  Cp.  also  fonda,  fondaco. font,  n.,  receptacle  for  baptismal  water —  ME., fr.  OE.  font,  ’baptismal  font’,  fr.  L.  fans,  gen. fontis,  ‘spring,  fountain’,  in  Eccles.  Latin  ‘bap¬ tismal  font’.  See  1st  fount, font,  n.,  set  of  type  of  one  size  ( typogr .)  —  F. fonte,  ‘a  casting’,  prop,  the  fem.  pp.  of  fondre, ‘to  cast,  melt’,  used  as  a  noun.  See  found,  'to cast',  and  cp.  fount,  ‘font’, fontal,  adj.,  1)  pertaining  to  a  fountain;  2)  bap¬ tismal.  —  Late  L.  fantalis,  fr.  L.  fans,  gen.  fon¬ tis,  ‘fountain’.  See  1st  fount  and  adj.  suff.  -al. fontanel,  fontanelle,  n.,  membranous  space  be¬ tween  the  bones  of  the  skull  of  a  baby  or  a young  animal  ( anat .)  —  F.  fontanelle,  trans¬ formation  of  OF.  fontenelle,  fr.  Medical  L.  fon- tanella,  prop,  the  latinized  form  of  the  dimin. of  F.  fontaine,  ‘fountain’.  See  fountain  and dimin.  suff.  -el,  resp.  -elle. food,  n.  —  ME.  fade,  fr.  OE.  fada  (whence OE.  fador,  ‘fodder’),  rel.  to  Goth,  fadeins, ‘food’,  fadjan,  ‘to  feed’,  and  cogn.  with  Gk. TraTsTaff-ai,  ‘to  feed’,  fr,  I.-E.  *pat- ,  * P't-, -/-enlargements  of  base  *pa-,  ‘to  tend,  keep, pasture,  feed,  guard,  protect’,  whence  also  Mes- sapian  roxvo 9,  ‘bread’,  L.  pa-bulum  (for  *pd- dhlo-m),  ‘food,  fodder’,  pa-nis,  ‘bread’,  pa-scere (pp.  pd-stus),  ‘to  graze,  pasture,  feed’,  pa-stor, ‘shepherd’,  lit.  ‘feeder’,  OSlav.  pasp  (for  pa¬ sted),  pasti,  ‘to  feed,  tend  (the  flock)’,  Toch.  A pas-,  B  pdsk-,  ‘to  feed,  tend  (the  flock)’,  Hitt. pahhshi,  ‘I  keep,  tend,  protect’.  Cp.  feed,  fodder, forage,  foster,  fother,  v.  Cp.  also  appanage,  com¬ panion,  company,  impanate,  pabulum,  panda, panetela,  panification,  pannage,  pannier,  pantler, pantry,  pascual,  pastern,  pastille,  pastor,  pasture, repast.  —  Related,  and  equivalent  in  meaning, to  I.-E.  base  *pa-,  is  base  *po-,  *poi-,  *pl-, whence  Ol.  pdti,  ‘he  guards,  protects’,  go-pdh, ‘shepherd’,  payuh,  ‘guarding,  protecting’,  Gk. 7KHp.f]v,  ‘shepherd’,  tc&u,  ‘flock  of  sheep’,  ~oiua, ‘lid,  cover’,  Lith.  piemuo,  ‘shepherd’.  Cp.  the 2nd  element  in  '  ikapala  and  in  satrap.  Cp.  also ban,  ‘governor’,  and  words  there  referred  to. fool,  n.,  a  jester,  a  dupe.  —  ME.  fat,  fr.  OF.  fol (F.  fou,  fol),  ‘foot’,  fr.  L.  follis,  ‘bag,  bellows, ball  filled  with  air’,  in  VL.  ‘empty-headed  per¬ son,  fool’.  See  follicle.  Derivatives:  fool,  intr. and  tr.  v.,  fool-ery,  n ,,faol-ing,  n.,faol-ish,  adj., fool-ish-ly,  adv.,  fool-ish-ness,  n. fool,  n.,  dish  consisting  of  crushed  fruit,  milk  and cream.  —  Fr.  prec.  word  in  its  colloquial  sense ‘a  trick,  a  joke’.  For  sense  development  cp. trifle,  ‘a  thing  of  small  value;  a  sweet  dish’, foolhardy,  adj.,  foolishly  bold;  rash.  —  ME .fol- herdi,  fr.  OF.  fol  hardi.  See  fool,  ‘jester’,  and hardy.
15279:fount,  n.,  the  British  equivalent  of  font.  —  F. fonte.  See  font,  ‘set  of  type  of  one  size’, fountain,  n.  —  OF.  (=  F.)  fontaine,  fr.  Late  L. fontana,  prop.  fern,  of  fontanus,  ‘pertaining  to a  spring’,  used  as  a  noun,  fr.  L  .fons,  gen  .fontis, ‘spring’.  See  font,  ‘receptacle’,  and  cp.  fontanel, four,  adj.  and  n.  —  ME.  feower,  fower,  foure, four,  fr.  OE.  feower,  rel.  to  OS.  fiuwar,  fiwar, OFris.  fiuwer,fidr,  Du.  vier,  OHG.  for,  MHG., G.  vier,  ON.  fjorir,  Dan  .fire,  Swed  .fyra,  Norw. fire,  Goth,  fidwor,  ‘four’,  and  cogn.  with  OI.  cat- vArah,  Avestic  cad  ward,  Pers.  catvdr,  Toch.  A stwar,  B  stwer,  Arm.  cork',  Gk.  -r6<j<rape<;,  Att. -nhrrapes,  Ion.  -reaaepes,  Aeol.  rrfcrjpet;,  toctu- pep,  L.  quattuor,  Oscan  petora,  Umbr.  petur-, OSlav.  cetyre,  Lith.  keturi,  OIr.  cethir,  W.  pet- guar,  pedwar,  ‘four’.  (Alb.  katsr  is  a  loan  word fr.  L.  quattuor.)  All  these  words  derive  fr.  I.-E. base  *quetwAr-,  ‘four’.  Cp.  fardel,  ‘fourth  part’, farthing,  firkin,  forty.  Cp.  also  cadre,  cahier, carfax,  carillon,  cater,  ‘four  at  cards  or  dice’, charpoy,  quadrant,  quadrate,  quadri-,  quadrille, quadroon,  quarantine,  quarrel,  ‘arrow,  bolt’, quarry,  ‘a  place  for  excavating  stones’,  quart, quatrain,  quaternion,  quire  of  paper,  squad, square,  tessara-,  tetarto-,  tetra-,  tetrakis-,  te- trarch,  trapezium,  trocar, fourchee,  fourche,  adj.,  forked,  divided  (her.)  —
=== Mann dhonos/dhentis:
14766:roudhàános ‘reddish; redness’ Ir. ruadhán, m. ‘red dye’; Li. raudonas, adj. ‘red’; W cf. rhuddain, adj. ( crimson’, fr. *rou- dhonis or *-ios); (LW in Finn. raudan- “iron” cpds. cf. rauta “iron”; rautias, adj. ‘bay, brown- ish-red")
```


## [2026-09-05T18:38:06.689Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '8295,8320p' incoming/ARY/ARY_pages.txt",
 "description": "Aryanpur index around damidan"
}
```


### [2026-09-05T18:38:06.736Z] TOOL RESULT

```
بلرچی (لل)نا/8۸): :2 انگلیسی کهن (8۷01380 صا0): 0۸26۳ ا
سانسکریت (5/977): انگلیسی (ب2ولا8(/0): ,0۸357
1 03۸6 دانمارکی (0(/13): ۳ ,0976
ایسلندی کهن (/۵ 5/0104 صاه): سرئدی (8175015): له نالا
201۸ نروژی (/0/07۷8010: نا
۳
[pdf page 282]
دمیدن (به چم "نفس کشیدن" و "فرت کردن یا ورزیدن") / ۲۸۳
هلندی (3ع۰)007 006 پسگشت‌ها 5
لیتوانی (770۸(7140/): ادارا ان 48 ۶0000
لترنی (لتی) (7۳1424): 0۸0۸ 0 (0۸3/۳) 7
پروسی کهن (/(28۷-5584 ۵10): ۰ 0181578 5 (825۸7) :15 72/( الط
57
5 (015) رگا (0۸/2)
برهان قاطع + ۸۶
یادداشت:
۱ بازگشت به: دمیدن.
۲ واژه‌ی "دما" به چم " گرما" هم پکار می‌رود (مثلاً در "دماسنج").
۳- چم این واژه در زبان‌های ژرمنی: بخار» رطوبت» دود و دَم.
چم این واژه در ایسلندی کهن: غباره گرد و خاکد. :
:
پهلوی (477تینم2۸): 2۸77۸۲ ,2۸3110۸۲ دانمارکی (0۸/877): 016
ارستی (05987/6): ۰ 018110 ,01-1110 نررژی (/(۵/08۳864: ۰ 0۸۸
کردی (8۵1/57). 12 اسلاری کهن (72شاد 2770767 0ا0):
سانسکریت (54۸/57077): 1 ,117210
5 011۸9۸7 ,107201۸37 ینوانی (/4(/42ا 7+ 0108171 ,218111
```


## [2026-09-05T18:38:17.573Z] AGENT

Now I'll write the verification file.


## [2026-09-05T18:43:35.771Z] TOOL CALL #68: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk127.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\n\ne0 = {\n \"entry\": 0,\n \"root\": \"Dhem\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *dʰemH- (LIV² *dʰmeh₁-) 'to blow, breathe; to smoke, raise dust'\",\n \"note\": (\"Pokorny IEW 247-248 heads the entry 'dhem-, dhemə- \\\"stieben, rauchen (Rauch, Dunst, Nebel; \"\n   \"nebelgrau, rauchfarben = düster, dunkel), wehen, blasen (hauchen = riechen)\\\"', so Nourai's language \"\n   \"label (Indo-European) and his gloss 'to make vapor, raise dust' are an accurate short rendering of the \"\n   \"German. Cheung (Etym. Dict. of the Iranian Verb, *damH³) writes the same root «PIE *dʰmeH- 'to blow' = \"\n   \"LIV: 153 | Pok.: 247 f.»; Wiktionary reconstructs *dʰemH-. Watkins/AHD carries no dhem- root (its list \"\n   \"goes dhembh- → dhen-¹), simply because no English word reaches it through Latin or Greek, so its silence \"\n   \"is not a disagreement. Two weak spots in the chart: the Avestan node's gloss (node 1) and the name \"\n   \"Damāvand (node 2), which Nourai's own source BQT:878 derives from a different root.\"),\n \"note_fa\": (\"ریشهٔ نمودار همان ریشهٔ هندواروپاییِ آغازینِ *dʰemH- «دمیدن، فوت کردن؛ دود و بخار برخاستن» است. \"\n   \"پوکورنی در صفحهٔ ۲۴۷ کتاب خود آن را با معنای آلمانیِ «stieben, rauchen … wehen, blasen» آورده و برگردانِ \"\n   \"کوتاهِ نورایی («بخار ساختن، گرد برانگیختن») با آن می‌خواند؛ چونگ نیز همین ریشه را *dʰmeH- «دمیدن» \"\n   \"(LIV ۱۵۳) می‌نویسد. پس جعبهٔ ریشه، برچسبِ زبان و معنای آن درست است و ادعای نورایی در این حد پذیرفتنی \"\n   \"است. تنها دو نقطهٔ سست در نمودار هست: معنایی که برای صورتِ اوستایی داده شده (گرهٔ ۱) و نامِ «دماوند» \"\n   \"(گرهٔ ۲) که خودِ مأخذِ نورایی، یعنی حاشیهٔ معین بر برهان قاطع ص ۸۷۸، آن را از ریشهٔ دیگری می‌گیرد.\"),\n \"sources\": [W+\"%D8%AF%D9%85%DB%8C%D8%AF%D9%86\", W+\"%D8%AF%D9%85\"],\n \"ref_check\": [\n   {\"ref\": \"POK:247\", \"status\": \"supports\",\n    \"note\": (\"POK_01.txt (grep -n 'dbem-' → line 3513), IEW p.247: 'dbem-, dhemo- ,stieben, rauchen (Rauch, \"\n             \"Dunst, Nebel; nebelgrau, rauchfarben == düster, dunkel), wehen, blasen (hauchen = riechen)'; \"\n             \"the page continues 'Ai. dhámati ,bläst', av. daδmainya- …, npers. damīdan ,blasen, wehen', dam \"\n             \",Atem, Atemzug''. Exactly the root box as drawn.\")}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. I 851 f. (WLD_Bd1 djvu line 53642)\", \"stance\": \"supports\",\n    \"note\": \"'dhem-, dhemə- „stieben, rauchen (Rauch, Dunst, Nebel; nebelgrau, rauchfarben = düster, dunkel), wehen, blasen (hauchen = riechen)“. Bedeutungsumfang wie bei Wz. *dheu- „stieben“.' — the source Pokorny 247 abridges.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"s.v. *damH³ (CHEUNG.txt line 4670 ff.)\", \"stance\": \"supports\",\n    \"note\": \"'*damH³ \\\"to blow, breathe; to swell\\\" … «PIE *dʰmeH- \\\"to blow\\\" > LIV: 153 | Pok.: 247 f.»'\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, d-list (AHD_watkins1985.txt line 377)\", \"stance\": \"silent\",\n    \"note\": \"the appendix runs 'dhembh-. To bury. … [Pok. (dhembh-), dhmbh- 248.] dhen-¹. To run, flow.' — no dhem- entry at all, since no English word descends from it via Latin/Greek.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, d-section (grep 'dhem' in IEC.txt)\", \"stance\": \"silent\",\n    \"note\": \"Mann has dhen- (2) 'forehead', dhenguhó, dhinió etc. but no *dhem- 'blow, smoke' headword.\"}\n ],\n \"nodes\": []\n}\n\ne0[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Avestan\", \"words\": \"dam; da-dhmainya\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"The Avestan language has no attested finite verb dam- 'to blow': Bartholomae, Altiranisches \"\n   \"Wörterbuch 731 f., knows only the Young-Avestan present participle daδmainiia- 'sich aufblasend, \"\n   \"-blähend', said of (tree-)frogs at Vd. 14.5 and 18.73, which he analyses as 'ein Praes. auf -ainya- mit \"\n   \"Inl.-Red.' and compares directly with 'ai. dhámati \\\"er bläst\\\", np. damīdan \\\"blasen\\\"'. Nourai's \"\n   \"'da-dhmainya' is that very word in his own transcription — he writes Avestan δ as dh and marks off the \"\n   \"reduplication syllable da- with a hyphen — so the form is faithful; but his gloss 'I inflate, breathe' \"\n   \"is wrong: it is an adjective/participle 'puffing itself up', not a 1sg verb. 'dam' is the root abstracted \"\n   \"from that participle, i.e. Proto-Iranian *damH- 'to blow, breathe; to swell' (Cheung 2007 s.v. *damH³), \"\n   \"which is real and is the ancestor of the Persian words in node 2; it is simply not an Avestan word-form. \"\n   \"Hence plausible rather than confirmed: right root, misdescribed gloss, and one of the two 'words' is a \"\n   \"root citation.\"),\n \"derivation_fa\": (\"در اوستا هیچ فعلِ صرف‌شدهٔ dam- «دمیدن» به‌جا نمانده است؛ بارتولومه در فرهنگ ایرانی باستان \"\n   \"(ستون ۷۳۱ به بعد) تنها اسمِ فاعلِ جوان‌اوستاییِ daδmainiia- «باد کرده، خود را باد کننده» را می‌آورد که \"\n   \"دربارهٔ قورباغه‌ها به کار رفته (وندیداد ۱۴٫۵ و ۱۸٫۷۳) و آن را ستاکِ حالِ پسوندِ -ainya- با تکرارِ درونی \"\n   \"می‌داند و مستقیماً با «dhámati سنسکریت» و «دمیدنِ فارسی» می‌سنجد. صورتِ «da-dhmainya» در کتاب نورایی \"\n   \"همان واژه است (او ذالِ اوستایی را dh می‌نویسد و هجای تکرارِ da- را با خط تیره جدا می‌کند)، پس خوانشِ کتاب \"\n   \"درست است؛ اما معنایی که به آن داده («من می‌دمم») نادرست است، چون این صورت صفت/اسمِ فاعل است نه فعلِ \"\n   \"اول‌شخص. «dam» هم واژهٔ اوستایی نیست بلکه ریشهٔ ایرانیِ باستانِ *damH- «دمیدن، باد کردن» است (چونگ، \"\n   \"ذیل *damH³). بنابراین ریشه درست است ولی معنا و صورت‌بندیِ گره با احتیاط پذیرفتنی است.\"),\n \"sources\": [W+\"%D8%AF%D9%85%DB%8C%D8%AF%D9%86\"],\n \"ref_check\": [\n   {\"ref\": \"POK:247\", \"status\": \"supports\",\n    \"note\": \"IEW 247 (POK_01.txt line 3517): 'av. daδmainya- ,sich aufblasend, blähend, von Fröschen''  — the same Avestan form under the same root.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"Altiran. Wb. 731 f., s.v. daδmainya- (BRT.txt line 13362)\", \"stance\": \"partial\",\n    \"note\": \"'j. däSmainya- Adj. \\\"sich aufblasend, -blähend\\\", von Fröschen … Eig. PPA. … — Vgl. ai. dhámati \\\"er bläst\\\", np. damidan \\\"blasen\\\"' — supports the root and the link to Persian, but shows the form is a participle, not '1sg I inflate'; and Bartholomae has no Avestan verb entry dam- 'to blow' (his dam- entries are 'Haus, Wohnung' and a present stem of dar- 'to hold').\"},\n   {\"src\": \"CHEUNG\", \"where\": \"s.v. *damH³ (CHEUNG.txt line 4670 ff.)\", \"stance\": \"supports\",\n    \"note\": \"'*AVESTAN: Y Av. daδmainiia- \\\"blowing up (intr.)\\\" (V 14.5, V 18.73)' listed as the only Avestan reflex of *damH³.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I 851 f.\", \"stance\": \"supports\",\n    \"note\": \"'av. dadmainya- \\\"sich aufblasend, blähend, von Fröschen\\\" (siehe Bartholomae Airan. Wb. 731 f.)'\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Persian\",\n \"words\": \"dam «دَم»; damîdan «دمیدن»; damâ «دما»; Damâvand «دماوند»\",\n \"verdict\": \"disputed\",\n \"derivation\": (\"Three of the four words are right, the fourth is not, so the node takes the worst verdict. \"\n   \"(1) دم dam 'breath' < Middle Persian dam (Manichaean/Book Pahlavi dm-, /dam-/) < Proto-Iranian *damH- < \"\n   \"PIE *dʰemH-; MacKenzie's Concise Pahlavi Dictionary has 'daftan, dam- [dptn', dm- | M dm-, N dam-idan] \"\n   \"breathe, blow. ~išn: breath', and 'damidan [dmytn'] = daftan'. This is a different word from the \"\n   \"homophone دم 'tail' (< dunb, Av. duma-), which Horn keeps apart as his no. 573. \"\n   \"(2) دمیدن damīdan 'to blow, breathe' is the New Persian regularisation of MP daftan (past stem daft) on \"\n   \"the present stem dam-: the inherited -ft- past was replaced by the productive -īd- suffix, exactly as \"\n   \"MacKenzie's 'damidan = daftan' records; hence Horn no. 572 'dem \\\"Atem, Atemzug\\\", deme, demīden \\\"wehen, \"\n   \"blasen\\\"'. \"\n   \"(3) دما damā is a nominal derivative of dam with the abstract/nomen suffix -ā; Borhan-e Qāteʿ p.877 \"\n   \"glosses it 'بمعنی دم و نفس باشد' with Moʿin's footnote '۱ رك: دم' ('see dam'), i.e. 'breath'. Nourai's \"\n   \"gloss 'weather, heat' is the modern technical sense ('temperature', as in دماسنج 'thermometer'), which \"\n   \"Aryanpur records explicitly; that sense is 20th-century, not classical, so the word is right but the \"\n   \"gloss is anachronistic. \"\n   \"(4) دماوند Damāvand does NOT belong here. In Islamic sources the name is written دنباوند dunbāvand, and \"\n   \"Moʿin's own footnote on the page Nourai cites (BQT:878) reports Kasravi's derivation from دُما/دنب 'back, \"\n   \"behind' + the suffix -vand (paired with نهاوند Nahāvand from نها 'front'); Wiktionary likewise gives \"\n   \"'from Middle Persian dmbʾwnd (dumbāwand)'. The 'mountain of vapour' reading is a folk etymology built on \"\n   \"the homophony of dam 'breath/vapour' with dam < dunb 'tail, rear'. Nourai's own NOTE flags the conflict; \"\n   \"modern scholarship sides with BQT:878 against the chart.\"),\n \"derivation_fa\": (\"از چهار واژهٔ این گره سه تا درست است و یکی نادرست، پس حکمِ گره همان بدترین حکم می‌شود. \"\n   \"۱) «دَم» به معنی نفس از فارسی میانهٔ dam (پهلویِ کتابی dm-)، از ایرانی باستان *damH-، از هندواروپایی \"\n   \"آغازین *dʰemH- است؛ مکنزی در فرهنگ کوچک پهلوی می‌آورد: «daftan, dam- … breathe, blow؛ damišn نفس». این \"\n   \"«دم» با «دمِ» هم‌آوایِ به معنی دنباله (از dunb، اوستایی duma-) یکی نیست و هرن هم آن دو را در شمارهٔ ۵۷۲ و \"\n   \"۵۷۳ جدا کرده است. ۲) «دمیدن» صورتِ قاعده‌مندشدهٔ فارسی نو از مصدرِ پهلویِ daftan است: ستاکِ حالِ dam- را \"\n   \"گرفته و پسوندِ زایای -ید- را جایگزینِ گذشتهٔ -ft- کرده‌اند؛ همان که مکنزی با «damidan = daftan» ثبت کرده \"\n   \"است. ۳) «دما» اسمی است از «دم» با پسوندِ -ا؛ برهان قاطع (ص ۸۷۷) آن را «بمعنی دم و نفس» می‌داند و معین در \"\n   \"حاشیه می‌نویسد «رك: دم». معنایی که نورایی داده («هوا، گرما») همان کاربردِ نوِ فرهنگستانی است (چنانکه در \"\n   \"«دماسنج») و آریان‌پور نیز آن را یاد کرده؛ پس واژه درست است ولی معنا امروزی است نه کلاسیک. ۴) «دماوند» به \"\n   \"این ریشه ربطی ندارد: در مآخذ اسلامی «دنباوند» آمده و معین در همان صفحه‌ای که نورایی ارجاع داده (ص ۸۷۸) \"\n   \"تحقیق کسروی را نقل می‌کند که آن را از «دُما/دنب» به معنی پشت و دنبال + پسوندِ «وند» می‌گیرد (در برابرِ \"\n   \"«نهاوند» از «نها» به معنی پیش)؛ ویکی‌واژه نیز آن را از فارسی میانهٔ dumbāwand می‌داند. «کوهِ بخاردار» \"\n   \"ریشه‌شناسیِ عامیانه‌ای است بر پایهٔ هم‌آواییِ «دمِ» نفس با «دمِ» دنباله. خودِ نورایی هم در یادداشت به این \"\n   \"اختلاف اشاره کرده است؛ پژوهش امروزی جانبِ برهان قاطع را می‌گیرد و این پیوند را رد می‌کند.\"),\n \"sources\": [W+\"%D8%AF%D9%85%DB%8C%D8%AF%D9%86\", W+\"%D8%AF%D9%85\",\n             W+\"%D8%AF%D9%85%D8%A7%D9%88%D9%86%D8%AF\"],\n \"ref_check\": [\n   {\"ref\": \"POK:247\", \"status\": \"supports\",\n    \"note\": \"IEW 247 (POK_01.txt line 3517-3518): 'npers. damīdan ,blasen, wehen', dam ,Atem, Atemzug'' — covers dam and damīdan, but says nothing of damā or Damāvand.\"},\n   {\"ref\": \"BQT:876,877\", \"status\": \"supports\",\n    \"note\": (\"BQT_v2_pages.txt leaf 336 = printed p.876 (offset printed = leaf+540, confirmed by the دماوند \"\n             \"entry falling on leaf 338 = p.878, the page Nourai's own NOTE cites): headword «دم» with Moʿin's \"\n             \"footnote 5 «هندی باستان dhamati (نفس کردن > دمیدن)؛ پهلوی dam نفس؛ اُستی dimin, dumun (دمیدن، \"\n             \"وزیدن)؛ کردی dem؛ بلوچی dam». Leaf 337 = p.877 has «دما … بمعنی دم و نفس باشد» with footnote \"\n             \"«۱ رك: دم». Note that footnote 7 on p.876 is the separate دم 'tail' entry (اوستا duma-, پهلوی \"\n             \"dum, dumb …), i.e. the 'Dumb' root.\")},\n   {\"ref\": \"HRN:127\", \"status\": \"supports\",\n    \"note\": (\"HRN.txt leaf 149 (printed p.127, leaf = printed + 21), entry 572: 'dem \\\"Atem, Atemzug\\\", deme, \"\n             \"demīden \\\"wehen, blasen\\\", demāγ, demār. ai. √dham-; dhámiti \\\"hauchen, blasen\\\"; phlv. dam; \"\n             \"ksl. dŭmǫ, dǫti \\\"blasen\\\"' (continuing on p.128 with oss. dumun, dimin). Horn's very next \"\n             \"entry, 573, is 'dum, dumb, dumbe \\\"Schwanz\\\"' — the root under which Damāvand belongs.\")}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, s.v. daftan / damidan (PHD.txt line 306; PHD_mackenzie.txt line 1864)\", \"stance\": \"supports\",\n    \"note\": \"'daftan, dam- [dptn', dm- | M dm-, N dam-idan] breathe, blow. ~išn: breath.' and 'damidan [dmytn'] = daftan.' — gives the exact Middle Persian ancestor of both دم and دمیدن.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"s.v. *damH³ (CHEUNG.txt line 4670-4712)\", \"stance\": \"supports\",\n    \"note\": \"'*MIDDLE PERSIAN: MMP dm- …, BMP dm- /dam-/ \\\"to breathe\\\" … Inf.: BMP dptn /daftan/' and '*NWIR: NP damidan/dam- \\\"to blow; to breathe; to blossom; to appear (as the dawn)\\\"'.\"},\n   {\"src\": \"ARY\", \"where\": \"ARY_pages.txt pdf page 282 = printed p.283, s.v. دمیدن\", \"stance\": \"supports\",\n    \"note\": \"'دمیدن (به چم «نفس کشیدن» و «فرت کردن یا ورزیدن»)' with Pahlavi damīdan/damīnīdan, Ossetic dumun/dimin, Sanskrit dhamati, Lithuanian dūmti and English DAMP, DAMPER among the descendants; footnote ۲ says «واژهٔ \\\"دما\\\" به چم \\\"گرما\\\" هم بکار می‌رود (مثلاً در \\\"دماسنج\\\")», i.e. it confirms Nourai's 'weather, heat' as a (modern) sense of دما.\"},\n   {\"src\": \"HUB\", \"where\": \"Persische Studien (grep 'dam' in HUB.txt)\", \"stance\": \"silent\",\n    \"note\": \"Hübschmann's word list has no entry for dam/damīdan; the hits are unrelated (andām, kudām, hamdam).\"},\n   {\"src\": \"BQT\", \"where\": \"leaf 338 = printed p.878, s.v. دماوند\", \"stance\": \"contradicts\",\n    \"note\": \"Moʿin's footnote ۵: «دماوند که در مآخذ اسلامی \\\"دنباوند\\\" آمده، بنا به تحقیق مرحوم کسروی … مرکب است از \\\"دما\\\" (ضم دال) بمعنی پشت و دنبال، چنانکه \\\"نهاوند\\\" نیز مرکب است از \\\"نها\\\" بمعنی پیش … جزو دوم در هر دو نام \\\"وند\\\" پسوند …» — i.e. Damāvand belongs to the dumb 'tail, rear' root, not to dam 'vapour'. This is the note Nourai himself reports.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Germanic\", \"words\": \"\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"An empty pass-through box: it stands for the Germanic branch of the root, which Pokorny \"\n   \"sets out on p.248 as three parallel enlargements of dhem- — with -p-: MHG dimpfen, dampf 'dampfen, \"\n   \"rauchen', OHG/MHG dampf 'Dampf, Rauch', MDu./Eng. damp 'Dampf, feuchter Nebel'; with -b-: Swed. dial. \"\n   \"dimba 'dampfen, rauchen', ON dumba 'Staub, Staubwolke'; and with -mm-: ON dimmr, OFris./OE dimm 'dunkel', \"\n   \"OHG timber. In modern terms Proto-Germanic *dimbaną 'to smoke, fog', whence the noun/adjective *dampaz \"\n   \"'vapour, damp'. The box carries no reference of its own and asserts nothing beyond 'Germanic continues \"\n   \"the root', which Pokorny and Walde-Pokorny both state.\"),\n \"derivation_fa\": (\"این جعبهٔ خالی تنها نشان‌دهندهٔ شاخهٔ ژرمنی ریشه است. پوکورنی در صفحهٔ ۲۴۸ سه گسترشِ \"\n   \"موازیِ ریشهٔ dhem- را در ژرمنی برمی‌شمارد: با -p- (آلمانی میانه dimpfen «دود کردن»، dampf «بخار، دود»، \"\n   \"هلندی میانه و انگلیسی damp)، با -b- (سوئدیِ گویشی dimba «دود کردن»، نورس کهن dumba «گرد و غبار») و با \"\n   \"-mm- (نورس کهن dimmr، فریزیِ کهن و انگلیسیِ کهن dimm «تاریک»، آلمانیِ کهن timber). به زبانِ امروزی: \"\n   \"ژرمنیِ آغازین *dimbaną «دود کردن» و از آن نام/صفتِ *dampaz «بخار، نمناک». این گره ارجاعی ندارد و ادعایی \"\n   \"جز «ژرمنی دنبالهٔ این ریشه است» نمی‌کند، و همین را پوکورنی و والده-پوکورنی هر دو تأیید می‌کنند.\"),\n \"sources\": [W+\"Reconstruction:Proto-Germanic/dampaz\"],\n \"ref_check\": [\n   {\"ref\": \"(none)\", \"status\": \"not_checked\", \"note\": \"the box carries no reference in the printed chart; the claim is covered by the POK:248 citation on the English node below.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW 248 (POK_01.txt lines 3524-3530)\", \"stance\": \"supports\",\n    \"note\": \"'mit germ. -p-: mhd. dimpfen, dampf ,dampfen, rauchen', ahd. mhd. dampf m. ,Dampf, Rauch', mnd. engl. damp ,Dampf, feuchter Nebel'' … 'mit germ. -b-: schwed. dial. dimba … anord. dumba ,Staub, Staubwolke' (daneben mit -mm- anord. dimmr ,dunkel', afries. ags. dimm ds. … ahd. timber)'.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I 851 f.\", \"stance\": \"supports\",\n    \"note\": \"same Germanic material ('norw. daam (*dhemo-) „dunkel“, daame m. „Wolkenschleier“ … anord. dǫkk …') listed under dhem-.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 4, \"lang\": \"English\", \"words\": \"damp, dim\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"English damp is a Middle English borrowing (early 14c., first of the choke-damp of coal \"\n   \"mines) from Middle Low German/Middle Dutch damp 'vapour' — cognate, not ancestral, with OHG/G Dampf, ON \"\n   \"dampi 'dust'; the sense 'moist air, moisture' is only from 1706 and the adjective 'slightly wet' later \"\n   \"still. English dim continues OE dimm 'dark, obscure' (ON dimmr, OFris. dim, OHG timber). Klein, whom \"\n   \"Nourai cites, ties the two together exactly as the chart does: 'damp, n. — MDu. (= Du.), \\\"vapor\\\" … and \"\n   \"in gradational relationship to MHG. dimpfen, \\\"to smoke\\\", OE. dimme, dim, \\\"dark, obscure\\\". See dim', \"\n   \"and 'dim, adj. … prob. cogn. with Gk. θέμερος \\\"grave, austere\\\" … Mir. dem \\\"black, dark\\\". Cp. damp'; \"\n   \"Pokorny 248 has the same set under dhem-. The reason for 'plausible' rather than 'confirmed' is that the \"\n   \"external comparanda are contested: Etymonline derives damp only as far as Proto-Germanic *dampaz and dim \"\n   \"as far as *dimbaz, 'not known outside Germanic'; Wiktionary derives *dampaz from *dimbaną and offers no \"\n   \"PIE root at all; and Skeat attached damp not to dhem- but to the *dheu- 'dust' family (Skt. dhūpa \"\n   \"'incense', 'See Dust'). So the chart follows Pokorny/Klein, a defensible but not universally accepted \"\n   \"position.\"),\n \"derivation_fa\": (\"واژهٔ انگلیسیِ damp وام‌واژه‌ای است در انگلیسی میانه (آغاز سدهٔ چهاردهم، نخست دربارهٔ گازِ \"\n   \"خفه‌کنندهٔ معدن) از آلمانیِ سفلای میانه / هلندیِ میانهٔ damp «بخار»، هم‌ریشه ‑ و نه فرزندِ ‑ آلمانیِ Dampf و \"\n   \"نورس کهنِ dampi «گرد»؛ معنیِ «نمناک» تنها از ۱۷۰۶ به بعد پیدا شده است. dim دنبالهٔ انگلیسیِ کهنِ dimm \"\n   \"«تاریک» است (نورس کهن dimmr، آلمانیِ کهن timber). کلاین ‑ همان مأخذی که نورایی آورده ‑ این دو را دقیقاً \"\n   \"به همان شکلِ نمودار به هم می‌بندد و پوکورنی هم در صفحهٔ ۲۴۸ همین مجموعه را زیرِ dhem- می‌آورد. اما حکم \"\n   \"«با احتیاط پذیرفتنی» است نه «درست»، زیرا هم‌ریشه‌های بیرونِ ژرمنی مورد اختلاف‌اند: اتیمولوژی‌آنلاین \"\n   \"damp را تا ژرمنیِ آغازینِ *dampaz و dim را تا *dimbaz پی می‌گیرد و می‌گوید بیرون از ژرمنی شناخته نیست؛ \"\n   \"ویکی‌واژه هیچ ریشهٔ هندواروپایی برای *dampaz نمی‌دهد؛ و اسکیت damp را نه به این ریشه بلکه به خانوادهٔ \"\n   \"*dheu- «گرد و غبار» (سنسکریت dhūpa «بخور») بسته است. پس نمودار راهِ پوکورنی و کلاین را رفته که \"\n   \"پذیرفتنی است ولی همگانی نیست.\"),\n \"sources\": [\"https://www.etymonline.com/word/damp\", \"https://www.etymonline.com/word/dim\",\n             W+\"damp\", W+\"Reconstruction:Proto-Germanic/dampaz\"],\n \"ref_check\": [\n   {\"ref\": \"POK:248\", \"status\": \"supports\",\n    \"note\": \"IEW 248 (POK_01.txt lines 3524-3530) lists 'mnd. engl. damp ,Dampf, feuchter Nebel'' and 'afries. ags. dimm' under dhem-, i.e. both English words on the page Nourai cites.\"},\n   {\"ref\": \"KLN:399\", \"status\": \"supports\",\n    \"note\": (\"Content matches word for word: KLN_1966.txt line 10286 'damp, n. — MDu. (= Du.), \\\"vapor\\\", rel. to \"\n             \"Dan. damp, OHG., MHG. damph, tamph, G. Dampf …, and in gradational relationship to MHG. dimpfen, \"\n             \"\\\"to smoke\\\", OE. dimme, dim, \\\"dark, obscure\\\". See dim and cp. dump'; line 11442 'dim, adj. … Cp. \"\n             \"damp, dump.' Caveat on the page number: in the two-volume 1966/67 printing on disk these fall on \"\n             \"leaves 220 and 246, i.e. printed pp. ~416 and ~468, so Nourai's single '399' must be the \"\n             \"one-volume 1971 'unabridged' edition, whose pagination the local scan does not mark.\")}\n ],\n \"consulted\": [\n   {\"src\": \"SKT\", \"where\": \"Skeat, s.v. Damp (SKT.txt line 4669)\", \"stance\": \"contradicts\",\n    \"note\": \"'Damp. (E.) Cf. M.E. dampen, to suffocate. Not in A.S. + Du. damp, steam; Dan. damp, G. dampf, Swed. damb, dust. Allied to Gk. [τῦφος] vapour, Skt. dhūpa, incense. See Dust.' — Skeat files damp under the *dheu- 'dust, smoke' root, not under dhem-.\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. dank (KLN_1966.txt line 10327)\", \"stance\": \"supports\",\n    \"note\": \"'dank, adj., moist, damp … rel. to OS. dunkar, OFris. diunk, \\\"dark\\\", ON. døkkr, Du. donker, OHG. tunkal … and to OHG., MHG. damph, MDu., Du. damp, \\\"vapor\\\". See damp.' — the same 'damp : dark' nexus Pokorny puts under dhem-/dhengu̯o-.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I 851 f.\", \"stance\": \"supports\",\n    \"note\": \"the Germanic p-/b-/mm- enlargements including English damp and dim are listed under dhem-.\"}\n ]\n})\n\ne3 = {\n \"entry\": 3,\n \"root\": \"Dhen, Dhont\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *dʰenh₂- 'to set in motion, run, flow'; o-grade *dʰon-t-/*dʰn̥-ti- in Latin fōns\",\n \"note\": (\"Pokorny IEW 249 '1. dhen- \\\"laufen, rennen; rinnen\\\"' is exactly the root box, and Watkins/AHD has \"\n   \"'dhen-¹. To run, flow. … [Pok. 1. dhen- 249.]'. Wiktionary reconstructs *dʰenh₂- 'to set in motion; to \"\n   \"flow'. Nourai's second citation form 'Dhont' is his way of writing the o-grade *dʰon-t- that underlies \"\n   \"Latin fōns, gen. font-is (Watkins: 'Suffixed o-grade form *dhon-ti-'); it is not a separate root, and the \"\n   \"gloss 'to flow, run around' is right (the 'around' is superfluous). This entry, unlike the Dhem entry \"\n   \"above, is straight out of Pokorny and holds up node by node; the only soft link is the Latin one, which \"\n   \"Pokorny himself marks 'wahrscheinlich' and Ernout-Meillet call a loose comparison.\"),\n \"note_fa\": (\"جعبهٔ ریشه درست است: پوکورنی در صفحهٔ ۲۴۹ «۱. dhen- \\\"دویدن، دواندن؛ روان شدن\\\"» را دارد و \"\n   \"واتکینز در پیوستِ AHD «dhen-¹. To run, flow. [Pok. 1. dhen- 249]». بازسازیِ امروزی *dʰenh₂- «به حرکت \"\n   \"درآوردن، روان شدن» است. صورتِ دومی که نورایی آورده، «Dhont»، ریشهٔ جداگانه‌ای نیست بلکه همان درجهٔ o یعنی \"\n   \"*dʰon-t- است که ستاکِ لاتینیِ fōns/font- از آن آمده. این مدخل، برخلافِ مدخلِ Dhem، بند به بند از پوکورنی \"\n   \"گرفته شده و استوار است؛ تنها حلقهٔ سست پیوندِ لاتینی است که خودِ پوکورنی آن را «wahrscheinlich» \"\n   \"(احتمالاً) خوانده و ارنو-مِیه آن را سنجشی سست می‌دانند.\"),\n \"sources\": [W+\"Reconstruction:Proto-Indo-European/d%CA%B0enh%E2%82%82-\",\n             \"https://www.etymonline.com/word/fountain\"],\n \"ref_check\": [\n   {\"ref\": \"POK:249\", \"status\": \"supports\",\n    \"note\": (\"POK_01.txt line 3540 ff. (IEW p.249): '1. dhen- ,laufen, rennen; fließen'. Ai. dhanáyati \"\n             \"\\\"rennt, läuft, setzt in Bewegung\\\", npers. danīdan \\\"eilen, laufen\\\", ai. dhánvati \\\"rennt, \"\n             \"läuft, fließt\\\", apers. danuvatiy \\\"fließt\\\" … lat. wahrscheinlich fōns, -tis \\\"Quelle\\\"' — \"\n             \"every node of this chart, in order.\")}\n ],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. dhen-¹ (AHD_watkins1985.txt line 377)\", \"stance\": \"supports\",\n    \"note\": \"'dhen-¹. To run, flow. Suffixed o-grade form *dhon-ti- in Latin fons (stem font-), spring, fountain: FONT¹, FOUNTAIN. [Pok. 1. dhen- 249.]'\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I 852 (WLD_Bd1 djvu line 53728)\", \"stance\": \"supports\",\n    \"note\": \"'1. dhen- \\\"laufen, rennen; rinnen\\\". Ai. dhanayati …, np. danidan \\\"eilen, laufen\\\", ai. dhanvati …, ap. danuvatiy \\\"fließt\\\" …; lat. wahrscheinlich fons, -tis \\\"Quelle\\\".'\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, d-section (grep 'dhen-' in IEC.txt)\", \"stance\": \"silent\",\n    \"note\": \"Mann lists dhen- (2) 'forehead, temple' and cross-refers to dhen- (1) and (3) but the 'run, flow' headword itself does not surface in the OCR text.\"}\n ],\n \"nodes\": []\n}\n\ne3[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Sanskrit\", \"words\": \"dhan\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Sanskrit √dhan- 'to run, set in motion' is real and is the standard Indic reflex of the \"\n   \"root: Pokorny 249 cites the causative-shaped present dhanáyati 'rennt, läuft, setzt in Bewegung', the \"\n   \"thematic dhánvati 'rennt, läuft, fließt' and the agent noun dhánutar- 'rennend, fließend'. Nourai gives \"\n   \"the bare root as Indian grammarians do (√dhan), which is the normal way of citing it; the gloss 'to run' \"\n   \"is right. Beside the verb the root gives Skt. dhánvan-/dhanus- in other senses which Pokorny expressly \"\n   \"keeps apart (they belong to 2. dhen- 'flat land'), and Nourai correctly does not draw them.\"),\n \"derivation_fa\": (\"ستاکِ سنسکریتِ √dhan- «دویدن، به جنبش درآوردن» واقعی است و بازتابِ هندیِ همین ریشه: \"\n   \"پوکورنی (ص ۲۴۹) صورت‌های dhanáyati «می‌دود، می‌دواند»، dhánvati «می‌دود، روان می‌شود» و اسمِ فاعلِ \"\n   \"dhánutar- «دونده، روان» را می‌آورد. نورایی، به شیوهٔ دستورنویسانِ هندی، خودِ ستاکِ برهنه (√dhan) را نقل \"\n   \"کرده که شیوهٔ متعارفی است، و معنایی که داده («دویدن») درست است. پوکورنی هشدار می‌دهد که dhánus-/dhánvan- \"\n   \"سنسکریت به معنی «زمینِ خشک» از این ریشه نیست و به «۲. dhen-» تعلق دارد؛ نورایی هم آن‌ها را نیاورده است.\"),\n \"sources\": [W+\"Reconstruction:Proto-Indo-European/d%CA%B0enh%E2%82%82-\"],\n \"ref_check\": [\n   {\"ref\": \"POK:249\", \"status\": \"supports\",\n    \"note\": \"IEW 249: 'Ai. dhanáyati \\\"rennt, läuft, setzt in Bewegung\\\" … ai. dhánvati \\\"rennt, läuft, fließt\\\" … ai. dhánutar- \\\"rennend, fließend\\\"' — the first item under the root, as in the chart.\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. I 852\", \"stance\": \"supports\",\n    \"note\": \"'Ai. dhanayati \\\"rennt, läuft, setzt in Bewegung\\\" … Fernzuhalten sind gr. θίς, dt. Düne … und ai. dhanus-, dhanvan- \\\"trockenes Land\\\" (s. *dhen- \\\"Fläche\\\")' — same Sanskrit evidence, with the explicit warning about the homonyms.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. dhen-¹\", \"stance\": \"partial\",\n    \"note\": \"Watkins gives only the Latin branch under dhen-¹; the Sanskrit dhanayati appears in the current online AHD appendix (cited by Etymonline s.v. fountain: 'Sanskrit dhanayati … Old Persian danuvatiy \\\"flows, runs\\\"'), so AHD supports the root but the 1985 print does not list the Sanskrit.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, d-section\", \"stance\": \"silent\",\n    \"note\": \"no dhen- 'run, flow' headword surfaces in the OCR of Mann.\"}\n ]\n})\n\ne3[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Persian\",\n \"words\": \"danîdan «دَنیدن»; dan «دَن»; danân «دَنان»\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"دنیدن danīdan is a genuine (if rare, largely Šāhnāma-and-lexicographers') Persian verb and \"\n   \"the derivation drawn is the standard one: Proto-Iranian *danHáyati < Proto-Indo-Iranian *dʰanHáyati < \"\n   \"PIE *dʰenh₂-, i.e. the exact Iranian counterpart of Skt. dhanáyati, with Old Persian danuvatiy 'flows' \"\n   \"as the Old Iranian witness; the New Persian infinitive is the present stem dan- plus the productive \"\n   \"-īdan. Nourai's gloss 'to run joyfully' is not his invention: Borhan-e Qāteʿ p.888 defines it 'دویدن به \"\n   \"نشاط و به خوشحالی براه رفتن' and Moʿin's footnote there derives it 'از: دن + یدن (پسوند مصدری). هندی \"\n   \"باستان √dhan-, dadhanat (دویدن)'; Moʿin's own Farhang repeats 'دویدن به نشاط و خوشحالی'; and Wiktionary \"\n   \"glosses it 'to run with alacrity and joy'. دنان danān is its present participle, 'hurrying, running', as \"\n   \"in the Ferdowsi line the chart quotes (پس اندر سپاه منوچهر شاه / دمان و دنان برگرفتند راه); Noushin's \"\n   \"Šāhnāma glossary explains it 'قید از دنیدن … بنابراین دنان به معنی شتابان روان، شتابان تازبان است' — \"\n   \"'running, excited' is fair. The one weak word is دَن dan glossed 'joyful shouting'. As a verbal stem دن \"\n   \"means simply 'run' (Noushin: 'دن [= دو، تگ]'); the 'shouting for joy' sense belongs to Borhan's separate \"\n   \"headword دنه (p.887: 'صدا و ندا و زمزمه از غایت خوشحالی'), and دَنّ with fatḥa is besides an Arabic word \"\n   \"for a wine-jar. So the node is right for two words out of three, with one gloss taken from a neighbouring \"\n   \"entry. Note also that Cheung's Etymological Dictionary of the Iranian Verb has no *dan- 'to run' root at \"\n   \"all — the verb survives only in Persian, and 'to run' in living Persian is دویدن, from a different root \"\n   \"*dauH-.\"),\n \"derivation_fa\": (\"«دنیدن» فعلی راستین اما کم‌کاربرد (بیشتر شاهنامه‌ای و فرهنگ‌نویسانه) است و ریشه‌ای که \"\n   \"نمودار برایش کشیده همان ریشهٔ پذیرفتهٔ امروزی است: ایرانیِ باستان *danHáyati، از هندوایرانیِ آغازین \"\n   \"*dʰanHáyati، از هندواروپاییِ آغازین *dʰenh₂-؛ یعنی درست هم‌ارزِ ایرانیِ dhanáyati سنسکریت، با گواهِ \"\n   \"پارسیِ باستانِ danuvatiy «روان می‌شود». مصدرِ فارسی نو از ستاکِ حالِ «دن-» به‌علاوهٔ پسوندِ زایای «-یدن» \"\n   \"ساخته شده است. معنایی که نورایی داده («دویدن با شادی») از خودِ او نیست: برهان قاطع (ص ۸۸۸) آن را «دویدن \"\n   \"به نشاط و به خوشحالی براه رفتن» می‌داند و معین در حاشیه می‌نویسد «از: دن + یدن (پسوند مصدری). هندی \"\n   \"باستان √dhan-، dadhanat (دویدن)»؛ فرهنگ معین نیز همین را دارد و ویکی‌واژه هم «دویدن با شتاب و شادی». \"\n   \"«دنان» صفت/قیدِ فاعلیِ همان است، چنانکه در بیتِ فردوسی که در نمودار آمده. تنها واژهٔ سستِ این گره «دَن» \"\n   \"است با معنیِ «فریادِ شادی»: «دن» به‌عنوان ستاک تنها «دو، تگ» یعنی «دویدن» است (نوشین در واژه‌نامک)، و \"\n   \"معنیِ «آواز و زمزمه از غایتِ خوشحالی» به مدخلِ جداگانهٔ «دنه» در برهان قاطع (ص ۸۸۷) تعلق دارد؛ «دَنّ» با \"\n   \"فتحه هم واژه‌ای عربی به معنی خمره است. افزون بر این، چونگ در فرهنگ ریشه‌شناختیِ فعل‌های ایرانی اصلاً \"\n   \"ریشهٔ *dan- «دویدن» ندارد، چون این فعل جز در فارسی بازنمانده و «دویدن» زندهٔ فارسی از ریشهٔ دیگری \"\n   \"(*dauH-) است. پس دو واژه از سه واژه درست است و یک معنا از مدخلِ همسایه گرفته شده.\"),\n \"sources\": [W+\"%D8%AF%D9%86%DB%8C%D8%AF%D9%86\",\n             W+\"Reconstruction:Proto-Indo-European/d%CA%B0enh%E2%82%82-\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:888\", \"status\": \"supports\",\n    \"note\": (\"BQT_v2_pages.txt leaf 348 = printed p.888 (printed = leaf + 540): «دنیدن ‑ بر وزن رسیدن. بمعنی \"\n             \"دویدن بنشاط و بخوشحالی براه رفتن باشد …» with Moʿin's footnote ۴ «از: دن + یدن (پسوند مصدری). \"\n             \"هندی باستان √dhan-, dadhanat (دویدن)». Exactly the derivation and the gloss of the chart.\")},\n   {\"ref\": \"POK:249\", \"status\": \"supports\",\n    \"note\": \"IEW 249: 'npers. danīdan ,eilen, laufen'' listed immediately after ai. dhanáyati.\"},\n   {\"ref\": \"HRN:128\", \"status\": \"supports\",\n    \"note\": \"HRN.txt leaf 150 (printed p.128), entry 574ᵇ: 'denīden \\\"eilen, laufen\\\", denān (Šāhn. I, 121 Vers 1033, 198 Vers 1242). ai. √dhan-, dadhánat \\\"laufen\\\"' — both danīdan and danān, from Skt √dhan-, with the Šāhnāma references.\"},\n   {\"ref\": \"FSF:88\", \"status\": \"partial\",\n    \"note\": (\"The entry is in Noushin's glossary but not at p.88 of the scan on disk: FSF_pages.txt lines \"\n             \"12451-12482 (running head ۳۳۲/۳۳۳) «دنان (با زیر اول): قید از دنیدن. دنیدن: مرکب از دن [= دو، \"\n             \"تگ] + پسوند مصدری … بنابراین دنان به معنی شتابان روان، شتابان تازبان است: \\\"پس اندر سپاه منوچهر \"\n             \"شاه / دمان و دنان برگرفتند راه\\\"». It supplies the Ferdowsi verse the chart quotes and supports \"\n             \"danān, but derives دن from دو/تگ 'run' rather than tying it to Skt dhan-, and gives no 'joyful \"\n             \"shouting' sense. Page mismatch is presumably an edition difference (Nourai cites the 1363 Donyā \"\n             \"printing; the archive.org scan is a different printing).\")},\n   {\"ref\": \"MON:1562\", \"status\": \"supports\",\n    \"note\": (\"Content confirmed, page not verifiable: the local Moʿin text is the 2-volume Adena abridgement \"\n             \"with its own pagination. MON_part1.txt line 63307: «دنیدن: [dan(īdan)] (مصدر لازم) دویدن به \"\n             \"نشاط و خوشحالی» — Nourai's gloss verbatim.\")}\n ],\n \"consulted\": [\n   {\"src\": \"CHEUNG\", \"where\": \"Etym. Dict. of the Iranian Verb, d-section\", \"stance\": \"silent\",\n    \"note\": \"there is no *dan- 'to run' lemma; the 'run' roots Cheung reconstructs are *dauH- (MP daw-, NP davīdan), *dram, *drau, *duar. The Persian verb has no Middle Iranian cognate to anchor it, which is why it survives only lexically.\"},\n   {\"src\": \"FSF\", \"where\": \"Vāzhe-nāmak, s.v. دنان (FSF_pages.txt lines 12451 ff.)\", \"stance\": \"partial\",\n    \"note\": \"see ref_check: supports danān/danīdan, silent on 'joyful shouting', and analyses دن as 'دو، تگ'.\"},\n   {\"src\": \"BQT\", \"where\": \"leaf 347 = printed p.887, s.v. دن / دنه\", \"stance\": \"partial\",\n    \"note\": \"p.887 has «دن ‑ … در زیر لب آهسته آهسته با خود حرف زدن باشد از روی قهر و غضب» and, separately, «دنه … و بمعنی نعمت دنیوی و شادی ‑ و صدا و ندا و زمزمه از غایت خوشحالی هم آمده است» — the 'joyful shouting' sense belongs to دنه, not to Nourai's headword دَن.\"},\n   {\"src\": \"MON\", \"where\": \"MON_part1.txt line 63307\", \"stance\": \"supports\",\n    \"note\": \"«دنیدن … دویدن به نشاط و خوشحالی».\"}\n ]\n})\n\ne3[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Latin\", \"words\": \"font\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"The Latin word is fōns, gen. fontis 'spring, fountain'; Nourai's 'font' is the oblique stem \"\n   \"font- rather than the nominative, which is how Watkins cites it too ('Latin fons (stem font-)'). The \"\n   \"derivation from this root is Watkins's and Pokorny's: 'Suffixed o-grade form *dhon-ti- in Latin fons \"\n   \"(stem font-)' (AHD dhen-¹), Wiktionary Proto-Italic *fontis < *dʰn̥-ti-, with word-initial *dʰ- > Latin \"\n   \"f- regularly. But this is a probability, not a certainty: Pokorny writes 'lat. wahrscheinlich fōns, -tis \"\n   \"\\\"Quelle\\\"; vielleicht Kreuzung des o-St. *fontos und ti-St. *fentis (*dhn̥-ti-)', and Ernout-Meillet, \"\n   \"s.v. fons, say only 'On rapproche skr. dhánvati, dhanáyati … Le vocalisme -o- indique un ancien nom \"\n   \"racine; la forme en -ti- ne peut être que secondaire … Sans doute vieux mot religieux, qui ne se retrouve \"\n   \"nulle part ailleurs', and in their preface they cite this very comparison as an example of one they \"\n   \"mention without endorsing, because 'f- initial du latin admet des origines multiples … et la ressemblance \"\n   \"de sens est vague et générale'. Verdict plausible: the chart follows the majority handbook view, which \"\n   \"the standard Latin etymological dictionary treats as unproven.\"),\n \"derivation_fa\": (\"واژهٔ لاتینی fōns است با حالتِ غیرفاعلیِ fontis «چشمه»؛ آنچه نورایی نوشته («font») ستاکِ \"\n   \"غیرفاعلیِ آن است، همان‌گونه که واتکینز هم می‌نویسد «Latin fons (stem font-)». پیوندِ آن با این ریشه از \"\n   \"آنِ واتکینز و پوکورنی است: درجهٔ o با پسوند، *dʰon-ti-، و در ویکی‌واژه ایتالیکِ آغازین *fontis از \"\n   \"*dʰn̥-ti-؛ دگرگونیِ *dʰ- آغازین به f در لاتین قاعده‌مند است. اما این پیوند قطعی نیست: خودِ پوکورنی \"\n   \"می‌نویسد «lat. wahrscheinlich fōns» یعنی «احتمالاً»، و ارنو-مِیه در ذیلِ fons تنها می‌گویند «آن را با \"\n   \"dhánvati سنسکریت سنجیده‌اند … بی‌گمان واژه‌ای دینی و کهن است که هیچ‌جای دیگر یافت نمی‌شود» و در پیشگفتار \"\n   \"همین سنجش را نمونهٔ سنجش‌هایی می‌آورند که تنها ذکر کرده‌اند و نپذیرفته‌اند، چون «f آغازینِ لاتین \"\n   \"خاستگاه‌های گوناگون دارد و شباهتِ معنایی مبهم و کلی است». پس نمودار نظرِ رایجِ کتاب‌های مرجع را دنبال \"\n   \"کرده که با احتیاط پذیرفتنی است.\"),\n \"sources\": [\"https://www.etymonline.com/word/fountain\",\n             W+\"Reconstruction:Proto-Indo-European/d%CA%B0enh%E2%82%82-\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins 1985 (AHD_watkins1985.txt line 377): 'dhen-¹. To run, flow. Suffixed o-grade form *dhon-ti- in Latin fons (stem font-), spring, fountain: FONT¹, FOUNTAIN. [Pok. 1. dhen- 249.]' — Nourai's bare 'AHD' citation is right, and this is the modern standard statement of the claim.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW 249\", \"stance\": \"partial\",\n    \"note\": \"'lat. wahrscheinlich fōns, -tis \\\"Quelle\\\"; vielleicht Kreuzung des o-St. *fontos und ti-St. *fentis (*dhn̥-ti-)' — supported, but hedged.\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet, s.v. fons, fontis (LAT.txt line 23342 ff. and preface line 99)\", \"stance\": \"partial\",\n    \"note\": \"'On rapproche skr. dhanvati, dhanayati \\\"il court, il coule\\\". Le vocalisme -o- indique un ancien nom racine; la forme en -ti- ne peut être que secondaire … Sans doute vieux mot religieux, qui ne se retrouve nulle part ailleurs.' The preface names this comparison as one merely mentioned, since 'la ressemblance de sens est vague et générale'.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I 852\", \"stance\": \"partial\",\n    \"note\": \"'lat. wahrscheinlich fons, -tis \\\"Quelle\\\"' with references to Bugge, Fick, Brugmann and 'Wf. LEWb.² s. v. (wo über andere Deutungen von fons)' — i.e. Walde himself notes rival explanations.\"}\n ]\n})\n\ne3[\"nodes\"].append({\n \"id\": 4, \"lang\": \"English\", \"words\": \"fountain\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"English fountain (early 15c.) is from Old French fontaine 'natural spring', from Late/\"\n   \"Medieval Latin fontāna, properly the feminine of the adjective fontānus 'belonging to a spring', used as \"\n   \"a noun, from Latin fōns, gen. fontis. Klein: 'fountain, n. — OF. (= F.) fontaine, fr. Late L. fontana, \"\n   \"prop. fem. of fontanus, \\\"pertaining to a spring\\\", used as a noun, fr. L. fons, gen. fontis, \\\"spring\\\"'; \"\n   \"Etymonline agrees and adds the sense 'artificial jet of water' from c.1500. Two small refinements to the \"\n   \"arrow as drawn: English inherits the derived fontāna, not the bare stem font-, and it comes through \"\n   \"French, not directly from Latin; and English font 'baptismal basin' is a separate, older borrowing \"\n   \"straight from Latin fōns into Old English (Klein: 'font, n. … fr. OE. font … fr. L. fons, gen. fontis'). \"\n   \"The node carries no reference in the book, but the chain is uncontroversial.\"),\n \"derivation_fa\": (\"واژهٔ انگلیسیِ fountain (آغازِ سدهٔ پانزدهم) از فرانسهٔ کهنِ fontaine «چشمهٔ طبیعی» است، \"\n   \"از لاتینِ متأخر/میانهٔ fontāna که در اصل مؤنثِ صفتِ fontānus «وابسته به چشمه» است و اسم شده، و آن از \"\n   \"لاتینِ fōns با حالتِ غیرفاعلیِ fontis. کلاین همین را می‌آورد و اتیمولوژی‌آنلاین نیز، با این افزوده که \"\n   \"معنیِ «فوارهٔ ساختگی» از حدودِ ۱۵۰۰ پیدا شده است. دو نکتهٔ ریز دربارهٔ پیکانِ نمودار: انگلیسی صورتِ \"\n   \"مشتقِ fontāna را وام گرفته نه ستاکِ برهنهٔ font- را، و راهِ آن از فرانسه گذشته نه یکسره از لاتین؛ \"\n   \"دیگر آنکه واژهٔ انگلیسیِ font «حوضچهٔ غسلِ تعمید» وامی جداگانه و کهن‌تر است که یکراست از لاتینِ fōns \"\n   \"به انگلیسیِ کهن رفته است. این گره در کتاب ارجاعی ندارد ولی زنجیره بی‌مناقشه است.\"),\n \"sources\": [\"https://www.etymonline.com/word/fountain\"],\n \"ref_check\": [\n   {\"ref\": \"(none)\", \"status\": \"not_checked\", \"note\": \"the box carries no reference in the printed chart; the parent Latin box cites AHD, which lists FOUNTAIN among the English reflexes of dhen-¹.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. fountain (KLN_1966.txt line 15279) and font (line 15106)\", \"stance\": \"supports\",\n    \"note\": \"'fountain, n. — OF. (= F.) fontaine, fr. Late L. fontana, prop. fem. of fontanus, \\\"pertaining to a spring\\\", used as a noun, fr. L. fons, gen. fontis, \\\"spring\\\". See font, \\\"receptacle\\\", and cp. fontanel' ; 'font, n., receptacle for baptismal water — ME., fr. OE. font, \\\"baptismal font\\\", fr. L. fons, gen. fontis'.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, index (AHD_watkins1985.txt line 1534)\", \"stance\": \"supports\",\n    \"note\": \"'FOUNTAIN dhen-¹' in the alphabetical index of English words, matching 'FONT¹ dhen-1' at line 1526.\"}\n ]\n})\n\nout = {\n \"pdf_page\": 127,\n \"book_page\": 97,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [e0, e3]\n}\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-127.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(out, f, ensure_ascii=False, indent=1)\n    f.write(\"\\n\")\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk127.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-127.json > /dev/null && echo \"valid JSON\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 127",
 "description": "Write and validate page-127.json"
}
```


### [2026-09-05T18:43:38.869Z] TOOL RESULT

```
written
valid JSON
nodes verified: 8/8
node verdicts: {'plausible': 4, 'disputed': 1, 'confirmed': 3}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 12, 'not_checked': 2, 'partial': 1}
books consulted: {'partial': 7, 'supports': 13, 'silent': 3, 'contradicts': 2} | by book: {'WLD': 5, 'CHEUNG': 3, 'BQT': 2, 'POK': 2, 'KLN': 2, 'AHD': 2, 'BRT': 1, 'PHD': 1, 'ARY': 1, 'HUB': 1, 'SKT': 1, 'IEC': 1, 'FSF': 1, 'MON': 1, 'LAT': 1}
```


## [2026-09-05T18:43:50.821Z] TOOL CALL #69: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json,re\nidx=[json.loads(l) for l in open('data/verification/sources/web/index.jsonl',encoding='utf-8') if l.strip()]\nhave={e.get('url') for e in idx}\nv=json.load(open('data/verification/page-127.json',encoding='utf-8'))\nurls=set()\ndef walk(o):\n    if isinstance(o,dict):\n        for k,x in o.items():\n            if k=='sources': urls.update(x)\n            else: walk(x)\n    elif isinstance(o,list):\n        for x in o: walk(x)\nwalk(v)\nfor u in sorted(urls):\n    print(\"OK \" if u in have else \"MISSING \", u)\nEOF",
 "description": "Check all cited URLs are archived"
}
```


### [2026-09-05T18:43:52.587Z] TOOL RESULT

```
OK  https://en.wiktionary.org/wiki/%D8%AF%D9%85
OK  https://en.wiktionary.org/wiki/%D8%AF%D9%85%D8%A7%D9%88%D9%86%D8%AF
OK  https://en.wiktionary.org/wiki/%D8%AF%D9%85%DB%8C%D8%AF%D9%86
OK  https://en.wiktionary.org/wiki/%D8%AF%D9%86%DB%8C%D8%AF%D9%86
OK  https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/dampaz
OK  https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/d%CA%B0enh%E2%82%82-
OK  https://en.wiktionary.org/wiki/damp
OK  https://www.etymonline.com/word/damp
OK  https://www.etymonline.com/word/dim
OK  https://www.etymonline.com/word/fountain
```


## [2026-09-05T18:44:09.545Z] AGENT

Page 127 (book p. 97) verified. `data/verification/page-127.json` written; `verify_check.py 127` reports 8/8 nodes, **0 PROBLEM lines**.

**Counts** — roots: 2 confirmed (entries 1–2 are redirects, skipped). Nodes: 3 confirmed, 4 plausible, 1 disputed. Ref checks: 12 supports, 1 partial, 2 not_checked (boxes with no refs). 15 books consulted.

**Disputed**
- **Dhem → Persian (node 2), دماوند Damāvand** — Nourai's "mountain (with vapor)" is folk etymology. His own cited page BQT:878 (Mo'in's footnote, reporting Kasravi) derives it from دُما/دنب "back, rear" + ‑vand (paired with نهاوند), and Wiktionary gives MP *dumbāwand*; Islamic sources write دنباوند. The other three words (dam, damīdan, damā) are sound, so the node takes the worst verdict.

**Plausible (not disputed, but worth the owner knowing)**
- **Dhem → Avestan (node 1)**: Av. has no finite verb *dam-*; only the participle daδmainiia- "puffing itself up (of frogs)" (Bartholomae 731f., Vd. 14.5/18.73). Nourai's gloss "I inflate, breathe" is wrong — it is not a 1sg.
- **Dhem → English damp, dim**: Pokorny 248 and Klein tie them together as drawn, but Etymonline/Wiktionary stop at PGmc *dampaz/*dimbaz "not known outside Germanic", and Skeat files damp under *dheu- "dust".
- **Dhen → Persian**: danīdan/danān fully confirmed (BQT:888, HRN:128, MON, Wiktionary *dʰenh₂-); only دَن "joyful shouting" is off — that sense belongs to Borhan's separate headword دنه (p.887).
- **Dhen → Latin font**: AHD and Wiktionary support *dʰon-ti- > fōns, but Pokorny says only "wahrscheinlich" and Ernout-Meillet explicitly cite this comparison as one they mention without endorsing.

**Extraction errors: none.** I read the rendered page 127; the JSON is faithful to the print (including "da-dhmainya" and all Persian script).

**Two citation notes for the owner (book-side, not data-side)**
- `KLN:399` — content matches Klein verbatim, but in the 1966/67 two-volume edition on disk *damp* is at ~p.416 and *dim* at ~p.468; Nourai must be citing the 1971 one-volume edition.
- `FSF:88` — the دنان entry is at pp. 332–333 of the archive.org scan, not p. 88 (different printing of Noushin's Vāzhe-nāmak).

Ten web pages archived via `fetch_source.py`; all URLs cited in `sources` are indexed.
