# Verification process log — verify-page-416


## [2026-09-14T01:10:06.584Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 416 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-416.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-416.json. Write /home/sfmqrb/git/rishe/data/verification/page-416.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 416` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T01:10:07.583Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T01:10:08.546Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T01:10:08.562Z] TOOL RESULT

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
226	Several agents run at the same time and share the scratchpad and `/tmp`, so every temporary
227	file you create must carry your page number in its name (e.g. `e0-363.json`, `pg363.png`,
228	`draft-363.json`), never a bare `e0.json` or `entry.json` — another agent will overwrite it.
229	
230	```json
231	{
232	  "pdf_page": 126,
233	  "book_page": 96,
234	  "verified_by": "claude-opus-5",
235	  "verified_on": "2026-09-05",
236	  "entries": [
237	    {
238	      "entry": 0,
239	      "root": "Dheigh, Dhigha",
240	      "verdict": "confirmed",
241	      "modern_form": "PIE *dʰeyǵʰ- 'to knead, form (clay)'",
242	      "note": "Pokorny 244 dheiĝh-; AHD dheigh-. Root, language label and gloss all correct.",
243	      "note_fa": "ریشهٔ هندواروپایی آغازین *dʰeyǵʰ- «خمیر کردن، شکل دادن (گِل)» … ادعای نورایی درست است.",
244	      "sources": ["https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰeyǵʰ-"],
245	      "ref_check": [{"ref": "POK:244", "status": "supports", "note": "…"}],
246	      "consulted": [{"src": "WLD", "where": "Bd. I 833", "stance": "supports", "note": "…"}],
247	      "nodes": [
248	        {
249	          "id": 6,
250	          "lang": "Avestan",
251	          "words": "pairi-daeza",
252	          "verdict": "confirmed",
253	          "derivation": "Av. pairi-daēza- 'walled enclosure' = pairi 'around' (PIE *per-) + daēza- 'wall' …",
254	          "derivation_fa": "«پردیس» … اوستایی pairi-daēza- «دیوارکشیده، باغِ محصور» از pairi «پیرامون» و daēza- «دیوار» …",
255	          "sources": ["https://en.wiktionary.org/wiki/pairidaēza"],
256	          "ref_check": [{"ref": "POK:244", "status": "supports", "note": "…"}],
257	          "consulted": [{"src": "BRT", "where": "col. 866", "stance": "supports", "note": "…"}]
258	        }
259	      ]
260	    }
261	  ]
262	}
263	```
264	
265	Rules:
266	- Include EVERY node of every non-redirect entry on the page (even empty-word pass-through
267	  nodes like `[Latin] refs=None |` — give them a one-line derivation and a verdict).
268	- `words` = the transliterations of the node joined by "; " (copy from the chart).
269	- `derivation` must be specific: forms, sound changes, dates/eras, texts or peoples,
270	  semantic shifts. 1–5 sentences. No hand-waving like "derived regularly".
271	- Keep `note` on the entry for root-level comments and for anything cross-cutting.
272	- If a node lists several words, cover each word; if they differ in verdict, use the worst
273	  verdict for the node and explain per word in `derivation`.
274	- Where the chart's own NOTE already records a dispute, evaluate it: say which side modern
275	  scholarship takes.
276	- Every node has `ref_check` (array, may contain a single `not_checked` item) AND `consulted`
277	  (array) AND `derivation_fa` (string); every entry has `note_fa`.
278	- Valid JSON only. Test it with `python3 -m json.tool` before finishing, then run
279	  `python3 /home/sfmqrb/git/rishe/tools/verify_check.py <pdf page>` — it must show 0 PROBLEM lines.
280	- When done, reply with a SHORT summary (≤ 15 lines): counts of verdicts per page, and a
281	  bullet per `disputed` / `transcription_suspect` item (root, word, one-line reason), plus
282	  any extraction errors (JSON differs from the printed page) the owner must fix.
283	  Do not paste the JSON back into your reply.
284	
```


## [2026-09-14T01:10:08.971Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-416.txt"
}
```


### [2026-09-14T01:10:08.989Z] TOOL RESULT

```
1	=== PDF page 416 (book page 386) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Redh, Regh : to separate, isolate  (refs KNT:205)
4	#1 (parent #0) [Old Persian] refs=KNT:205; BQT:949 | rad 2, radh, ras 2 : set free ; ava-rad : abandon
5	  #2 (parent #1) [Persian] refs=BRT:1505; KNT:205; BQT:949; FFD:55 | rahîdan «رهیدن ( رَستن )» : escape, become free | extra: وارهیدن ، وارستن ، وارسته ، رستگار
6	#3 (parent #0) [Avestan] refs=KNT:205; NYB:167 | rah : to escape, set free ; razah : isolation
7	  #4 (parent #3) [Persian] refs=BQT:926; HRN:134 | râz «راز» : secret
8	
```


## [2026-09-14T01:10:10.331Z] AGENT

I'll read the source JSON and reference metadata.


## [2026-09-14T01:10:11.632Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/extracted/batch/page-416.json",
 "description": "Read source JSON for page 416"
}
```


### [2026-09-14T01:10:11.679Z] TOOL RESULT

```
{
  "pdf_page": 416,
  "book_page": 386,
  "entries": [
    {
      "root": {
        "name": "Redh, Regh",
        "lang": "Indo-European",
        "refs": "KNT:205",
        "gloss": "to separate, isolate"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "KNT:205; BQT:949",
          "words": [
            {"translit": "rad 2, radh, ras 2", "gloss": "set free", "script": null},
            {"translit": "ava-rad", "gloss": "abandon", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BRT:1505; KNT:205; BQT:949; FFD:55",
          "words": [
            {"translit": "rahîdan", "gloss": "escape, become free", "script": "رهیدن ( رَستن )"}
          ],
          "script_extra": "وارهیدن ، وارستن ، وارسته ، رستگار",
          "note": null,
          "quote": {
            "text": "بمیر تا برهی ای حسود ، کاین رنجی است - که از مشقّت آن جز بمرگ نتوان رست",
            "poet": "Sa`dî"
          }
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Avestan",
          "refs": "KNT:205; NYB:167",
          "words": [
            {"translit": "rah", "gloss": "to escape, set free", "script": null},
            {"translit": "razah", "gloss": "isolation", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "BQT:926; HRN:134",
          "words": [
            {"translit": "râz", "gloss": "secret", "script": "راز"}
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


## [2026-09-14T01:10:13.745Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['KNT','BQT','BRT','NYB','HRN','FFD','POK','AHD','WLD','PHD','HUB','MON','CHEUNG','ARY','IEC','SYN','KLN']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:400])\n\"",
 "description": "Check reference metadata"
}
```


### [2026-09-14T01:10:15.072Z] TOOL RESULT

```
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/downloa
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
CHEUNG null
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
```


## [2026-09-14T01:10:20.354Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['KNT','BRT','NYB','HRN','FFD','BQT']:\n    e=d.get(k) or {}\n    print('==',k)\n    for f in ['local_file','page_offset','lookup_hint','scans']:\n        print('  ',f,':',str(e.get(f))[:500])\n\"",
 "description": "Get page offsets for refs"
}
```


## [2026-09-14T01:10:21.448Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/sources/refs/ | head -60 && sed -n '1,80p' data/verification/sources/SOURCE_MATRIX.md",
 "description": "List refs and matrix"
}
```


### [2026-09-14T01:10:22.018Z] TOOL RESULT

```
== KNT
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt
   page_offset : leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; section refs like '$147'. Nourai's page numbers should fall in 164-215 for lexicon citations.
   scans : None
== BRT
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt
   page_offset : Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops.
   scans : None
== NYB
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt
   page_offset : Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.
   scans : None
== HRN
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt
   page_offset : leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.
   scans : None
== FFD
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages_faseng.txt']
   page_offset : 115 leaves (PDF pages); printed page = PDF page − 5 (PDF 40 = p.35). 2nd printing 1385 of the same Qoqnus setting (ISBN 964-311-015-X).
   lookup_hint : Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).
   scans : None
== BQT
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '
   page_offset : vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, 
   lookup_hint : grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf imag
   scans : [{'volume': '3', 'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', 'first_printed': 1208, 'last_printed': 1925, 'pdf_offset': -1205, 'page_map': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json', 'lang': 'fas', 'ocr_text': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', 'ocr_note': '689/721 pdf pages OCRed (tesseract fas+eng, mediocre); pages are separated by form-feeds a
```


### [2026-09-14T01:10:22.101Z] TOOL RESULT

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
```


## [2026-09-14T01:10:29.962Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==220 || NR==221' KNT.txt | head -100",
 "description": "Print Kent leaf 220 (p.205)"
}
```


### [2026-09-14T01:10:31.091Z] TOOL RESULT

```
‘I pierce (as with a spit)’, Gt. faran ‘to travel’. рамо[т- іаїу| nsn. past pte. pass. ($242.1) DNb 54 (dubious con]. of Kent, Lg. 15.167, 178-4).
ipara- adj. ‘later’, possibly in hyáparam (q.v.) : Av. para- ‘farther’, Skt. pára- ‘distant’, Gk. qépav ‘beyond’.
nara prep. with acc. ‘beyond’ (§32, $63.1): Av. pard ‘before’, Skt. purds ‘before’, Gk. таро ‘before’; DPe 15; DPh 5; DH 4, See also para- dayadàm, paradraya.
parü postpos. with acc. ‘along’, and verbal prefix ‘forth’ ($132.3): Av. ?pará ‘before’, Skt. purá ‘before, formerly’, Gk. rapá ‘alongside’: in avapard and with ay-, ar-, gam-, bar-.
parauvaty lsn. as sb. ‘in the east’: руи] "Ре 15, a misreading for pr? : d*r^ ye (uninseribed space between r* and y*) = para : dra ya; seeunder paradraya.
paradayadám sb. asf., perhaps ‘pleasant re- treat’ ($55.II, §148.1V): Аа 3. Possibly mis- written руат“ for p'rud*iljme = paridai- dam, Av. patridaéza- ‘Umwallung, Ummauerung' (Bthl. AiW 865), borrowed in Gk. тарабено ‘park’, cf. JAOS 51.229; or for p'r*d'id^am* = paradidam, from ?para ‘beyond’ + didá- ‘wall’ (q.v.), as ‘that which is beyond or behind the wall’ (ef. Scheil 21.93; Bv. BSLP 30.1.67 j'vadiy paradayadám ‘paradis de vie’).
paradraya phrasal adv. ‘across the sea’ ($44, $191.[V): рата ‘beyond’ + acc. draya ‘sea’. DNa 28f; DSe 29°; XPh 24. paradraiya (848) A?P 24 (Hz. ApI 142). As two words, para draya DPe 15 (Cameron, JNES 2.307-8).
parana- adj. ‘former’: deriv. ($147.11) of stem in OP ?para, para (cf. ВЕШ. AiW 854), Av. рагі, рагб, Skt. рига ‘formerly’ (hardly to be normal- ized parna-, with MB Gr. $267, to Gt. faírneis ‘old’). See also dumlaparanam. — paranam asn. as adv. ‘formerly’ DB 1.51, D'Sb 3.
pariy prep. and prefix ‘around, about’: Av. pairi, Skt. pári, Gk. тері, Lt. per ‘through’, pIE *peri ($64, §75.1, $113, §140.1). Prep. with aec. ‘about’ DB 1.54. Prefix-with ay-, bar-; ef. also pariyana-.
196 OLD PERSIAN
pariyana- sb. ‘superiority’: deriv. ($147.IT) of pariy, in meaning seen in Ау. pairi ‘vorne, über ... hin’, Skt. pári as prefix ‘much, excessively’, cf. Gk. meptoads ‘excessive’ (otherwise Hz. ApI 273, Sen 250). pariyanam nsn. DNb 52.
paru- adj. ‘much, many’: Av. pouru-, Skt. purú-, Gk. modts, Gt. filu, pIE *palu- (§63.1, $107). See also paruzana-. рати) nsm. ($114, $127, $140.I) DB 449; DSf 56 bis. pariindm gpm. DSi 4, 5; DE 9, 10; XPa 5 bis; XPb 9, 10; XPc 4f, 5; XPd 6f, 7f; XPf 6, 7; XPh 5, 6; XE 9f, 11; XV 7,8; А:Ра 7°, 8°; А°Нс 6 bis. parünàm gpf. DPe 4. parüenüm ($28.П) gpm. DNa 6, 7; DSe 6, 7; Азра 6, 7.
paruva- adj. ‘being before in time or place’ (§35.1[): Av. paurva-, Skt. pürva-, pIE *pruos (868, $150), ef. Gk. Ion. трохоѕ ‘early’. See also paruviyata, paruviyaüd. parwā npm. ‘former’ DB 4.51. parwam asn. as adv. ‘formerly’ DB 1.9; DBa 15f; DSe 43°, 47; XPh 36, 39; paruvam- ciy DB 1.63, 67, 69.
parwnyata, adv. with preceding hacd, ‘from long ago’: *paruviya- (ie. *parvya-, deriv. of paruva-), Av. paouruya-, Skt. pürvyd-, + adv. suffix -la^, Av. -£ó, Skt. -tas, Gk. -ros, Lt. -tus asin funditus, pIE *-los ($191.11). C£. also paruviyatà. DB 1.7, 8, 45; DBa 11, 12.
[paruv|iyafà adv. ‘at first attempt’: *paruviya- (see paruviyala) + adv. suffix -0à, Av. -fa, Skt. -ihà ($191.ID). DSj 3 (conj. of Brandenstein, WZKM 39.49-51; ef. note ad loc.).
paruzana- adj. ‘having many men, or many kinds of men’ (‘having men of all tongues’, Wb. ZfA 44.165, after the Akk.): paru- ‘many’ + zana- ‘man’ ($9.11, $88, $120, $161.ППа). paru- zanānām (5140.1) gpf. DE 15f; XE 15f; А!Ра 12°. poruvzandndm (523.1) XPb 15f; XPd 11. раги zandnam ($23.11, $44) XPa 8; XPe 7; XPf 11; XPh 9; XV 12.
Parga- sb. ‘Parga’, a mountain in Persia: Elam. par-rak-qa, NPers. Purg ($30). Parga лет. DB 3.44. |
partara- sb. ‘battle’ (as in Elam. and АКК. versions): extension of -r/n- s
tem (530, $148.I, 6154.1), ef. Av. posana- ‘battle’, Skt. pfiana- ‘battle, army’, to root in Av. poral-onie ‘they fight’? (Bv. TPS 1945.69-4; not agency noun
‘fighter, foe’ as taken by Wb. KIA 90-1, Bv. Gr. $277; not paratara- ‘foe’, with Wackernagel, KZ 59.29-30, as compar. to [Skt.] pára- ‘distant’ = RV ‘enemy’). partaram asn. DNa 47.
Ратдата- (§29.n2, $31) adj. ‘Parthian’, also тазе, as sb. ‘Parthia’, a province of the Persian Empire: Elam. par-tu-ma, АКК. pa-ar-tu-á, Gk. IIapóià. Extension ($150) of stem seen with vriddhi in Pársa-, but with dialectal difference in the 0/s ($9. VT, 887).
(1) ‘Parthian’: Paréava nsm. DN iv; A?P 4. Par&avaibi$ ipm. DB 2.96. (2) ‘Parthia’: Paréava nsm. DB 1.16; 2.7, 92;
DPe 15; DNa 22; DSe 21°; DSm 8°; XPh 20.
Par8avai ism. DB 2.94° 96°; 3.5, 10. parna-, see duildparanam, parana-. ‘parsa- vb., see fraó-.
?parsa- sb. ‘court’, only in Hz. ApI 278; for his pa[r|saiy lsm. DNb 22, see under patiy.
Pársa- adj. ‘Persian’; also masc. as sb. ‘Persia’, a province of the Persian Empire: Elam. par-sin, АКК. pa-ar-su, Gk. Перо, Пероќа (§9. VI, $87, §126, 5143.11). See also Paréava-. `
(1) ‘Persian’: Pársa nsm. DB 1.49; 2.18, 19, 49; 3.18, 26, 31, 32, 56, 84; 4.16, 26, 83, 84 bis, 85 bis, 86; 5.8°; DPe 22; DNa 18, 46; DN i; DSe 12; DZe 7; XPh 12; A?P 1. Pérsam asm. DB 2.81; 8.2, 29f; DPe 21. Pàrsahyà gsm. DNa 13f, 43; DSe 13; XPh 12. Pérsé ism. DPe 8.
(2) ‘Persia’: Pársa пзш. AsH 3 (for loc., §52.1);
DB 1.14, 41; 2.7; DPd 6f; DSm 6°. Pársam asm. AsH 8f; DB 1.46; 3.33, 34; 49, 28; DZe 12. Pérsam-cé DB 1.66. Pürsá ism. XPa 14 (here ‘Persepolis’, acc. to Cameron, by letter; $166, 6166.1). Pürsà absm. РМа 18, 46f; DSe 17°; Юле 7f, 10; XPh 16. Parsa for lsm. AmH 2 (856.V, §314b; wrongly Hz. AMI 4.132-4, 8.17- 9, as instr. of extent); for пзш. AmH 5 ($53; not nsf. adj., as taken by Hz. AMI 820-1, 34). Pärsaiy lsm. DB 1.2, 34; 2.9; 3.23, 24, 28, 34, 52, 58, 71; DBa 2.
pasü prep. ‘after’, temporal with асе. and local with gen. (Bv. BSLP 33.2.153): Av. paséa, NPers. pds, Skt. paácá, isn. to stem in Lith. (dat.) adv. and prep. різки ‘behind, later, after’ (Foy, KZ 35.26); pIE *po as in Lt. po-lið, positus, Gk. &-vó, + *sg*é, inst. to root noun from *seq*- ‘fol- low’, Av... hacatte, Skt) Gdeate, Gk. trerai, Lt.
See nada lai baa a D Lo AMA tae io at OT IPE Ауаз a зз
~
LEXICON
sequitur (§105; Uhlenbeck, Etym. Wtb. d. altind. Spr., s.v. paced). The s in pasá is OP for Med. $c, Av. sé, from pAr. $c (Ву. Gr. §114; otherwise Mt. Gr. §114). Less probably pAr. *pas (Lith. pds ‘at, to’) from the same *po + adv. -s as in OP patiš, + -cà isn. of stems in -айс-, for -acã (from *-ncà) by influence of contracted forms like Skt. praca (*pra-acd) to ртайс- (*pra-atic-) ‘forward’, cf. similar analogical form in Skt. adv. nica ‘downward’ (for *ni-acd) to пуайс-. Hardly from *pas (as above) + -à after its opposite para ‘before’ (Bthl. AiW 879). Direct cognation with Lith. páskw: is eliminated by the second and third etymologies; with Av. pasta, Skt. paícá, by the third. pasã with gen. DB 3.32; with асе. XPf 31 and in pasdva (q.v.).
pasáva phrasal adv. (§191.IV) ‘after that, afterwards’: pasé + asn. ava (8181). DB 1.27, 30, 32, 33, 34°, 35f, 40, 43, 46, 54, 72, 731, 75, 79, 82, 83, 86, 91, 94; 2.1, 3, 4, 12, 16, 19, 21, 27, 31, 32, 47, 49°, 51, 52, 62, 64, 67, 71, 72, 81, 84f, 94; 3.1,4, 9, 12f, 15, 20, 25, 29, 33, 36f, 41, 50, 59, 70, 73,75, 81, 84, 86, 90f°; 4.5, 35, 91; 5.3, 6, 9, 10f, 13, 21°, 28, 25°, 29; DSe 48; DSf 25; DZe 10; XPh 36; XSe 3; XV 23; А:Ра 21°; Рр 4°. pasãva-šim DB 2.76, 90. pasdva-Saiy DB 2.88.  pasáva-dim DNa 33. pasdva-mary XPh 32.
pasti- sb. ‘foot-soldier’: Skt. pailt-, from pIE *ped- ‘foot’ (OP pad-) + suffix -t&- ($85, 5152.11; Wb. Grab 40, Hz. ApI 94-8). — pasti$ nsm. DNb 48, 45.
pilar- sb. ‘father’: Av. pilar-, NPers. pióür, Skt. pitd
```


## [2026-09-14T01:10:31.511Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^rad\" KNT.txt | head -30; echo ---; grep -n \"avarad\\|ava-rad\\|radiy\\|rādiy\" KNT.txt | head -30",
 "description": "Grep Kent for rad"
}
```


### [2026-09-14T01:10:31.715Z] TOOL RESULT

```
1648:radiy; fra-haravam.
---
1638:$133. Encursis is a frequent phenomenon in OP. The enclities are the following: Pronouns: Ist sg. асе. -md, gen. -maty, abl. -ma. 2d sg. gen. -taiy. За sg. acc. -йт, gen. -Saiy, abl. -$a; pl. acc. -&$, gen. -Sàm. acc. -dum; pl. acc. -di$. pl. aec. -àà (dubious; only in avabasa-lé DB 4.72), Coordinating conjunctions: -eà ‘and’, -vë ‘or’. Postpositions: d, patiy; both also as separate words before or after their nouns. Adverbs and particles: -am, -kavy, -ciy, -dty, never separately. -apiy, -paliy both also separately. Miscellaneous: уа in mátya DB 4.43, 48, 71; yadatya XPh 35f (miswritten yadàya XPh 39), cf. yada : tya XPh 29. müm, elsewhere orthotone, in mātyamäm DB 1.52. rádiy in avahya-radiy DB 1.6f, etc.; also separ- ately. Double enclisis: mé-tya-mém DB 1.52; rauca- pati-vd,, DB .1:207 aatpati-mé DNb 20; avā-
1648:radiy; fra-haravam.
2345:The adverbs from this stem are атайй, avadā, ava-pard, avahya-radiy, pasdva (from *pasd ava).
2461:pIE *reghe- (or *redhe-, see Lex. s.v.), Skt. талай ‘he leaves’; inj. 2d sg. OP ava-rado?.
2549:$224. Тнк INiuNCTIVE FORMATIONS are merely secondary indicative forms lacking the augment; the following forms have been found in OP: Ist sg. tarsam; 2d sg. stabava* apa-gaudaya* ava-rada*; 3d sg. fadaya'. See also $237.
2567:II. The secondary ending -s is seen in Skt. ábharas, Gk. édepes; in OP it happens to occur only in injunctive ava-rada, apa-gaudaya, slabava, and in opt. [biylà, in which it is not written be- cause it is final after a (§36).
2573:fer from the sigmatic aorist, where the termina- tions would be pIE -?s-m -is-s -is-t, pAr. -isam -iš -1&; the identity of second and third personal forms gives an analogy to the 2d sg. imperfect in -1-$# (no examples extant in OP), whence impf. 3d sg. in 4$. After u the phenomena are the same.? The OP examples are àt$ ‘went’, 0170-07 ‘went past’, aku- naus ‘паде’ (Skt. ékynot), adarsnaus ‘dared’ (Skt. ddhrgnot); and the thematic optatives active vi- ndlayars, passive kariyars fradiyars (cf. for ending Gk. $€po,, Skt. bhdret).
2603:§237. THE PERSONAL ENDINGS oF THE IMPER- ATIVE. Apart from mjunctive forms, there are im- peratives with special endings, here discussed. The injunctives are those used in prohibitions with mà: ist sg. tarsam (226.1), 2d sg. stabavat apa- gaudaya^ ava-rada? ($227.11), 3d sg. байауа! (8228.II); and those used as regular imperatives: 2d pl. paraità jalà ($231).
2811:§264. Tug DEMONSTRATIVE ava- ‘that’ is simi- larly either pronoun or adjective; it commonly refers to something already mentioned, but some- times has a forward reference, as in naimd ava ката tya tunuvd skaubars radiy miła kariyars ‘that is not my desire, that the mighty should have wrong done to him by the weak’ (DNb 10f; also DB 3.58, 5.21, DNa 39, DNb 20, 53, 55, 57, DSa 4, DSe 34, XPh 49, 51f). It has also the meaning ‘yonder’ as applied to the sky: Auramazdà hya imam bümim ada hya атат asmdénam айй ‘Ahura- mazda, who created this earth, who created yonder sky’ (DNa 1-3, eto.).
2829:verb. yàlà, prep. w. loc. уйй à, prep. w. abl. radiy, postp. w. gen.
2946:$281. Tug Insunctive Моор, which is a sec- ondary indicative form lacking the augment, has in OP only the use in a negative prohibition, with má: in the first person, iarsam DPe 21; in the second person, apagaudaya DB 4.54, avarada and stabava DNa 60; in the third person, &adaya DNa 58, DNb 58.
3076:IV. The postpositions are upariy ($269; only once postposed, as separate word); рата, only in ava-parā; rādiy, in avahya-rddiy and separately; patiy, as enclitic postposition, as separate post- position, and also as preposition; -à, as formative of the locative case; kacã once (DB 1.50), separ- ately, governing a preceding enclitic. Position in the clause varies.
3856:62 5 :х$йуайуа : avahyarādiy : Auramazdà : upastàm : арага : uta : ani
3963:8 Cispi$ ; CispaiS : pita : Haximanis: 4 9 0atiy : Darayavaus : xšāyaðiya : avahya ^ ^^ 10 radiy : vayam : Haxamanisiyà : баһуй 11 mahy : hacá : paruviyata : àmàtà 12 : amahy ; haca : paruviyata : hyà 13 xam : taumá : xšāyaðiyā : dha : 6a 14 бу : Darayavaus : xSdyafiya : ҮНІ : ma 15. nà : taumiya : tyaiy : paruva
4105:28 : Katpatuka : Sparda : Yauna : бака : {уау : pa 29 radraya :Skudra : Yauna : takabarà : Рибу 30 à : Каўуя : Maciya : Karka : дану : D 31 drayavaus : xšāyaðiya : Auramazda : ya 32 & : avaina : imàm : bümim : yaudatem : 33 pasávadim : manā : frábara : mam : 28d 34 уадуат :akunaus : adam : x&àyatiya 85 :amiy.:.vasnd : Auramazdahd : a 30 damSim : gafava : niyašādayam : tyašā 37 m : adam : afaham : ava : akunava : yabā : mam: 38 Ката : aha : yadipatiy : maniyáhaty : t 39 ya :ciyakaram.: dha : ava : dahyiva 40 :tyà : Darayavaus : xSayafiya 4] :adáraya : patikarà : didiy : tyaiy : g 42 àfum : baratiy : vadā : xSnasahy : 43 adataiy : azdà : bavatiy : Pārsahyā : 44 martiyahyà : diraiy : artes : pa 45 ràgmatà : adataiy : azdà : bavāti 46 y :Parsa :martiya : dürayapiy : hacà : Pa 47 rsà : partaram : patiyajata : 6itiy : Da 48 rayavauS : xSdyafiya : aita : буа : karta 49 m :ava :visam : vasnà : Auramazdaha : ak 50 unavam : Àuramazdá(ma)iy : upastàm : aba 51 ra : yütà : kartam : akunavam : mém:A 52 uramazdà : pàtuv : аса : gasid : utama 53 iy : vitam : uta : imàm : dahyàum : aita : ada 54 m : Auramazdam : jadiyámiy : aitama 55 iy : Auramazda : dadatuv : 56 martiya : hyà : Auramazdah 57 & : framana : hauvtaty : gas 58 tā : ma : adaya : раб : .. 50 {уаш : ristim : mà 60 : avarada : mà : stabava Nores то DNa: The text of DNa now rests upon the photographs of F. Stolze (Persepolis: Berlin, 1882) and of А. Sevruguin (accessible in Wb. Grab, Plates 2-3). The following readings, which either replace older wrong readings or confirm older doubted readings, are assured by the photographs; the restorations agree with the length of the gaps: ^? framatà- | ram; ™ düraiapty; 9 patiyazsayaty; 9^? aba[ra]- | ha; * adáraiya (for nor- malization, ef. $48); 25 haumavargá ; * akunava; * yadi- patiy : maniy|ühaty : t]- | ya (for -haiy, cf. note on DB 4.39); * {aha} Wb.; “ no space for [mand] before ga6um; £ a[va]dà; **düraiy; 4 dárayapiy; ® Auramazda(ma)ty, with omission of те; 6 ga(sta], see Lex. s.v. (not sero+). Other textual notes: 3° [ра]- | radraya, after other oc- currences, see Lex. s.v.; not [ta]- | radraya. *^* Put- (älyä, after other occurrences, see Lex. svt; not Put[i]yà. 2 yauldatim] ВЕ, sée Lex: ву. yaud-; hardly yaufdinim],
5854:ava- + rad- ‘leave, abandon’: avarada 2d sg. inj. (5213, $224, $227.11, $237) РМа 60.
5856:rādiy postpos. ($133) ‘on account of’, with gen.: NPers. тё, enel. postpos. as in &-rà ‘why’, also particle of various uses, often affixed to direct object for elarity; also OCS radi, postpos. with gen., “оп account of’; 10е, sgoof räd- (5188111), io root in Ski. radh- ‘effect; complete! (not to
```


## [2026-09-14T01:10:37.499Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=5830 && NR<=5875' KNT.txt; echo \"=== leaf index:\"; head -5854 KNT.txt | tr -cd '\\f' | wc -c",
 "description": "Print Kent rad- entry and leaf index"
}
```


### [2026-09-14T01:10:38.713Z] TOOL RESULT

```
lwadé- conj. ‘where’: GAv yada, Skt. yada; probably rel. nt. pAr. #00 + postpos. 4. уайд- tya XPh 35f ($133, $296; cf. yaa tya ХР 29); yadàyà XPh 39 (perhaps error in writing, §55.1; but ef. Hz. AMI 8.66, ApI 358, Nyberg Rel. 477-8).
*Yadd- sb. ‘Yada’, probably ‘Anshan’ (as shown by the Elam. translation 3.3 an-za-an.mar, read by Cameron; cf. §166.n2): not an abstract yadà- ‘loyalty’ to root yad- (q.v.), as commonly taken (wrongly also Foy; KZ 35.43; Hüsing, ОГЛ
Ы
LEXICON | 205
8.513-6; Hz. ApI 244-9; Nyberg, Rel. 477-8). Yadayd absf. ($141, $175) DB 3.26.
yadiy conj. ^if, when’: Av. yetéi, Skt. yddi: per- haps pAr. nt. rel. *iad + deietic 4. Syntax $297. (1) Sf, with subj.: DB 4.38f, 54, 57, 721, 77; DPe 19, 22; DNa 38 (yadi-patiy), DNb 29 (yadi- và; cf. Hz. ApI 359); XPh 47 (yadi-maniyáty; 841, $92. VI); with opt., DNb 20f; with pres. ind., ОХЬ 25 (yadi-và). (2) ‘when’, with imf. ind., DB 1.38, DSf 11; ‘whenever’, with pres. ind., DNb 38f, 39.
yàna- sb. ‘favor, boon’: Av. yand-; deriv. of
‚ yam-, probably *ya- from *m-, with lengthening
and suffix -na- (5147.1). yànam asm. DPd 21, 23°; XSe 4°.
yaniy соп]. ‘where, whereon’: lsn. *ya^mi (= Skt. ydsmi-n, Av. yahmy-a ‘where’) to relative stem ya-, with -n- after isn. *yand, cf. isn. lyand to tya- (hardly yanazy, loc. formed on stem yana- extracted from isn. *yand, as taken by Bthl. Ат 1262; not miswritten for tyanaty, as taken by Müller, WZKM 7.112; other theories in Tm. Lex. 120 s.v.). Syntax $296. XV 22.
yam- vb. ‘stretch, reach out’: Av. yam- pres. yasaiti, Skt. yam-, pres. ydechati, OP pres. yasa-, pIE *im-ske-. See also уйпа-.
а + yam- ‘reach out for, (mid.) take as one's own’: ãyasatā imf. mid. (§97, $215, $235.IT) DB 147; 34, 49f.
ай- + yam- ‘reach beyond, present, read aloud to’: [аја] уа (823.T, $140.IIT, $220) imf. pass. DB 4.91 (conj. of Kent, JAOS 62.268; for -i-, ef. niyasaya, below).
ni- + yam- ‘reach out and down; (caus.) set down’: niyasaya imf. caus. (823.I, $140.IIT, $215) DNb 5, 46, 49 (In. JAOS 38.123-4; MB Gr. $199; Johnson, Gr. $4780; Hz. ApI 359-61).
уйа con]. ‘as long as’, isn. of *ydva-, exten- sion of pIE rel. */o-, pAr. *ia-, cf. Skt. ydvat, Av. yavala, Gk. dos (from *ayos); hardly from* yàva! à = GAv. (Ys. 43.8) yavat à, with contraction (Wackernagel, KZ 46.275-80). With subj. to show future time ($208): DB 4.71, 74, 78; 5.19, 35°.
raucah- sb. ‘day’: Av. raocah- ‘light’, Phi. rüé, NPers. róz, Skt. rócas- ‘light’, pIE *leugos ($70, $107, $156.ID, ef. Gk. Xexó-s adj. ‘ight’. тамса nsn. ($119, $1851) DB 3.8. rauca-pati-và
(899, $133) asn. DB 1.20. raucabiš ipn. ($119, 51851) DB 1.38, 42, 56, 89f, 96; 2.26, 36, 42, 47, 56, 691, 98^; 3.181, 39, 47, 63, 68, 88f.
ташіаћ- sb. ‘river’ ($166): NPers. ra8, Skt. srólas- ‘current, river’, pIE *sreutos (5118.1, $156.П) to root *sreu- ‘flow’; perhaps same as Av. 6raotah-, with sandhi initial (Bthl. Саг. IP 1.§87.- n2, AW 800). rauta nsn. anacoluthic in naming phrase (wrongly gen.-abl. to stem таш-, Mt. MSLP 19.56-7, MB Gr. $167, $316) DZc 9.
Razé- sb. ‘Rakha’, а town m Persia: Elam. rak-qa-an (S100). Ваха nsf. DB 3.34.
тахйайш! DNb 60, imv. of vb. of unknown etymology and uncertain meaning (§76.II, V, $103.IIT, $213, $237.II), perhaps ‘inflict punish- ment upon’, cf. АКК. version (Lg. 15.174; see also Hz. ApI 284-5).
ra”ga- sb. ‘speed, haste’: Av. rang- "leicht, flink werden’ (Bthl. AiW 1511), Skt. rdhale ‘has- tens, speeds’, rahas- nt. ‘speed, quickness’ (for fur- ther connections, see Uhlenbeck, Wrtb. d. altind. Sprache 241). ragam asn. (or asm.?) as adv. (§143.1, $191.IIT) DB 4.44, perhaps with develop- ment to ‘eagerly’ or ‘confidently’.
Raga- sb. ‘Rhages’, a district in Media: Elam. rak-qa-an, АКК. ra-ga-’, Gk. ‘Payys, now Rai near Teheran. kagä nsf. DB 2.71f. Ваду absf. DB 8.2.
гада- sb. ‘wagon’ (570.11, $148.11), see urata-.
Irad- vb. ‘leave’: Skt. rah-, pres. rahati 'sep- arates, leaves’, to pIE *regh-, Av. razah- 5isola- tion’, or to pIE *redh-, NPers. (through Ars. РЫ.) rähäð ‘he gets free from’; Fr. Müller, WZKM 11.208-4; Foy, KZ 37.564-5; Bthl. AiW 1505; MB Gr. $192.
ava- + rad- ‘leave, abandon’: avarada 2d sg. inj. (5213, $224, $227.11, $237) РМа 60.
?rad- vb. ‘direct’ Ау. raz-, Skt. rdj- ‘reign’, Lt. rego ‘I direct, rule’, pIE *reg-; in uradana-, тазіа-.
rādiy postpos. ($133) ‘on account of’, with gen.: NPers. тё, enel. postpos. as in &-rà ‘why’, also particle of various uses, often affixed to direct object for elarity; also OCS radi, postpos. with gen., “оп account of’; 10е, sgoof räd- (5188111), io root in Ski. radh- ‘effect; complete! (not to
206
"rad-, pIE *rej-, with Hz. ApI 280). DB 4.54; DNb 9, 10f; also in avahyarádiy, q.v.
ram- vb. ‘be at peace’, with prefix d, in Arüjyüramna-, q.v.
rasa- present stem of vb., see ar-.
rüsla- adj. ‘straight, right, true’, with nt. as Sb.; ріс. of ?^rad-: Av. réSta-, Turfan РЫ. тай ‘true’, Lt. réctus ‘straight’, pIE *rékto- (593, §93.- n1-2, $106, $122, 5126, $24211). Cf. arštā-. таӣз- iam asf. DNa 59. rdstam usn. DNb 11; asn. DNb 7.
‚ .. rlaryary, see vart-.
Labandna- (or Labnàna-) sb. ‘Lebanon’ (§6, §107), 2 mountain in Syria famous for its cedars. Labanéna nsm. DSf 31.
-vä encl. conj. ‘or’ (8133, $291.11); -vā .. -vä ‘either... or...’: Av. và, Skt. và, pIE *ue, ef. Lt. -ve.  z$apa-ü rawca-paíi-a DB 1.20. hya-»à DB 4.68. imai-vä DB 4.71, 78, 77. yadi- vä DNb 25, 29.
vaina- present stem of vb. ‘see (mid.) seem’: Av. vaéna-, NPers. bindd, Skt. véda ‘knows’, vinddte ‘finds’, Lt. videt ‘sees’, videtur ‘seems’; pAr. *uaid- na-, plr. *yaina- ($69, 588.1, $130, $210.III; Reichelt, Aw. Ер. $157). See also Vidafarnah-. vainümiy lst sg. (4226.1) DNb 36, 36f, 39, 40. avaina imf. DB 2.76, 90; DNa 32. vainataiy mid. as pass. (8235.1) DNb 2; XPa 16. vaináhy 2d sg. subj. ($37, $222.11, $227.1) DB 4.70, 73, 77; DNb 29. vaindtiy subj. ($222.11) DS} 5°. vainātaiy subj. mid. as pass. ($222.П) DNb 35.
vau- adj. ‘good’ ($11, §153.1); nt. as sb. ‘the good, (religious) goodness’: Av. nsm. vaphus, nsn. vohu, Skt. nsm. vásuş, nsn. vdsu, pIE *yesu-; in Dérayavau-, Vaumisa-, Vahauka-, Vahyazdata-.
Va'umisa- sb. ‘Vaumisa’, a Persian officer of Darius: Elam. ma-u-mi-i8-8a, АКК. ti-mi-is-st, Gk. (Plutarch) Rutens; cpd. of vatu- and mifra- ‘friend’ (849c, $78, $148.ILD): ‘Friend of the Good’ §160.- Ib; cf. MB Gr. $51). Vaumisa nsm. DB 2.49, 51, 62. Vaumisam asm. DB 2.53, 58.
vaz$- vb. ‘grow’, see (Луах${та-.
Waj- vb. ‘be strong’: Skt. vaj-, бјаз- ‘strength’, Av. aof
=== leaf index:
230
```


## [2026-09-14T01:11:06.137Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"1505\\|1506\" BRT.txt | head -20",
 "description": "Find Bartholomae column 1505"
}
```


### [2026-09-14T01:11:06.191Z] TOOL RESULT

```
25060:1506
```


## [2026-09-14T01:11:07.913Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"razah\\|razaŋh\\|razah-\" BRT.txt | head -20; echo \"=== CHEUNG\"; grep -n \"rahati\\|razah\\|rastan\\|reh-\\|\\*rad\" CHEUNG.txt | head -40",
 "description": "Grep Bartholomae and Cheung"
}
```


### [2026-09-14T01:11:07.987Z] TOOL RESULT

```
5594:acht Renoer", Name  cinesGebirgs*>:  ahmat\  j.  »arazah-  n.  'Abend':  yai  uHrSAva ha:a    garayl   fraoxiyqn  .  .    asta    'vants  m»r)neaite  (sd)  -zahva  bisasyät  V.2/.3. fitnkOfö   (sd)    YL  Jp.3.  [Vyt.  IQ:    lies       Et.?   Vgl.  Gdn.  Stud.  /.  51.  —  Vgl.  anzt-hU
14893:von  Vorgängen  und  Umständen,  die  die Satzhandlung  begleiten  oder  die  Voraus- setzung dazu  bilden,  'bei';  i)  mit  Lok.: ahß  at  'tl  adäkü  .  .  büiricä  kar^hia  . . xrapaitT  (sd.)  hyai  ahmat  aibl  Y.  4°. 1.  i)mitAkk.:  ma  yave  imal  nm3t»m  . . s^annB  /razahlt .  .  n^äkrS.disyehe  (sd.)  'ti a^iila  . .  haxma  Y.6o.j; .  .   manB    rämayeiti  [huxsnßittm  (sd.)
19363:•  )•<  E-.  P-  'inä  prohib,  Part  "nicht,  ne,  fi.-^'; drückt  aus,  dass  man  das  Eintreten  der  Sau- aussage nicht  haben  will  mä  tritt  a)  an  die Spitze  des  Satzes  oder  b)  vor  das  Verbum ''. Gilt  die  Aussage  von  mehreren  Nomina, so  wird  m3  wiederholt  (doch  s.  No.  3),  an letzter  Stelle  erscheint  dann  auch  mala (statt  iwa).  i)  mit  Inj.  des  Verbs;  zu  a): iux/ährä  x^ntqm  (sd.)  ma  rß  *du/^xia^rä xsima  Y.  48.  5 ;' —  m  a  S^l  ai  vS  dngvatö mq%rqs!a  güHä  sämatca^^  Y.ji.jS;  — väfva  (sd.)  vtdusl  tnraotu  mS  »vTdva  aipl.- dSbavayatY.31.1-j;  —  mä  »r  ahmt  nmatu mai  ../rfm  vaocata  mqm  ..  V.iy;  — m  3  yave  imat  nmäium  . .  ^artnS  frazahJt /nS' ..  Y.60.  7; —  tnSca  pas!aäa  masda- yasna  tarn  sqm  karaym  mä  äpö  himaygn V.  6'.  a ;  —  mäia  pascaila  mazdayasna vTmshasäf  vTmahayatUa  V,  7.  38*';  —  ma äim  pfnsS  yim  pfrysaki  H.  2. 17;  —  mS m?r?ruainTs  astvaitli  galhä  SrB.  3;  — mä  mqm  . .  Vj^ä»/ VyLfo.j  —  s.  noch zu  6.  zu  b)    am?m  mq^nm   mä  fra-
25197:razah-
25232:•  j.razah-  n.  "Einsamkeit,  Abgelegenheit': 'tS  F.iy,  —  Plur.:  düire  asoAi  °sar»hqm "fem   an   einem  Oit  der  Einsamkeit"  V.
28055:mit  fi-ä  'im  Stich  lassen,  verschwinden aus  — '  (Akk,):  ma  yave  imat  ttmSmm  . . ^armS  frazahlt  Y.  60.  7.
=== CHEUNG
9905:BMP Ih- /rah-/ ‘to escape’, NP rastan/rah- ‘to be delivered, saved, escape’, may 
12636:*KHOTANESE: rraphai (loc. sg.) ‘attack, fight, yuddhe’ || (+ *pati-) OKh. pareh- ‘to 
13115:*rad- (i.e. *(H)ra(n)d), pace Morgenstierne, EVS\: l.c. Most, if not all, intransitive 
13385:Henning 1933: 187: < *uhrastan < *uzrästanai. || Klingenschmitt (Congress Graz 
13399:Pst /arast/, BMP "l'stk /arastag/; Inf.: BMP "Tom /arastan/ || (+ *pati-) Pres.: IND. 1р1. MMP pdr’ywm; 
13440:*NWIR: Awrom. (awa-)faznay/(war-)fazn- ‘to adorn’ || (+ *api- ?) NP pérastan/péray- 
13441:‘to adorn, decorate, ornament’ || (+ *abi-) NP afraxtan, afrastan/afraz- ‘to raise’ (LW 
13442:?), NP afraz ‘exalted’ (LW ?) || (+ *а-) NP arastan/aray- ‘to adorn’ || (+ *ui-) Zaz. 
21155:*AVESTAN: 9 The often cited YAv. razah- is unconnected, as it should rather mean 
21167:(Psalter); Inf.: BMP Istn /rastan/ 
21180:*NWIR: NP rastan/rah- ‘to be liberated, escape; to let go’, NP raz ‘secret’ (LW), 
21198:added as cognates, Skt. rah, OP rad-, MP rastan [wrongly cited: rastan], NP rastan. 
23574:*AVESTAN: (+ *fra-) ? Y Av. frastan- ‘to take, convey forward’ (Gershevitch, Mithra: 
23578:Pres. ua-: IND. 3pl. ? YAv. frastanuuanti (Yt 10.20) 
23827:weapon); to pave (road, way); to cover (the roof)’ || (+ *upa-) Pash. brastan (f.) 
29767:frazahit (Y 60.7); Partic.: perf. YAv. zazus- (Yt 13.18, P 26). 9 YAv. us.zizenti (V 3.5) was corrected to 
30252:interpreted differently: for YAv. frazahit (Y 60.7) see *zaH, and OAv. zaxiia- (Y 
33401:frastan-, 361 
33676:razah-, 322 
37184:pareh-, 185 
40690:afraxtan, afrastan/afraz-, 
40758:arastan/aray-, 198 
41327:pérastan/péray-, 198 
41373:rastan/rah-, 140, 322
```


## [2026-09-14T01:11:11.953Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '21130,21215p' CHEUNG.txt",
 "description": "Read Cheung root entry for rad"
}
```


### [2026-09-14T01:11:12.008Z] TOOL RESULT

```
*raxš ‘to aim, shoot; mark’ 

*SOGDIAN: (+ *abi-) CSogd. brxs- ‘to loosen, release, shoot’, BSogd. Br'xs ‘to shoot’ 
Pres.: IND. 3sg. BSogd. Br’xst; Impf.: IND. 3sg. CSogd. b’rxs; Inf.: Brxs’y 

*NEIR: ? Oss. I. raxsyn ‘to throw out; to shoot at’ 

o The Sogdian forms can only derive from a prefixed formation *abi-raxs-, as 
pointed by Gershevitch 1970: 305; also Sims-Williams 1985: 176 ad 94V.14. Oss. I. 
raxsyn may be included, although it may alternatively derive from *fra- + *Haxš. As 
for a possible IE etymology, Gershevitch (l.c.) cites Lat. laxsus ‘slack, wide, loose’ 
as cognate. Since both the Sogd. and Lat. forms are relatively isolated with their 
respective branch, this remains uncertain. It cannot be excluded that Lat. laxsus is a 
secondary/recent formation. It is similar to lassus ‘tired’, which appears to have a 
(more) certain IE origin ( *leH;d- ‘to let (go)’, LIV: 400). 

*PIE — = LIV: - | Pok.: 959 


*REFERENCES: Abaev, Slovar’ I: 221 f. 


*raz ‘to leave, escape (one's notice)’ 

*AVESTAN: 9 The often cited YAv. razah- is unconnected, as it should rather mean 
*clime, expanse’ (V 8.97), on which see Gonda 1956: 164. 

*OLD PERSIAN: (+ *aua-) avarad- ‘to leave, abandon’. Ф See most recently R. Schmitt 
2000: 32. = Kent: 205b 

Pres. them.: INJ. 2sg. avarada <a-v-r-d> (DNa 60) 

*MIDDLE PERSIAN: MMP rh-, BMP I(’)h- /rah-/ ‘to escape, become free, let go’ 
MMP r’z, BMP Гс /raz/ ‘mystery, secret’ (LW) = DMMPP: 294b 

Pres.: IND. 3sg. BMP Isyt /raséd/, 3р1. MMP rhynd; Partic.: perf. pass. BMP Ist-y /rast-é/ ‘set free’ 
(Psalter); Inf.: BMP Istn /rastan/ 


*KHOTANESE: rraysaa- ‘empty’ 

*SOGDIAN: SSogd. r'zh, BSogd. r’z’y, CSogd. r’z, MSogd. r’z ‘secret, mystery’ || (+ 
*apa-) SSogd. ’pr’st (pret. stem) ‘to flee’, CSogd. pryZ ‘to flee’ 

Pres.: ОРТ. 3sg. CSogd. pryZy, IMPV. 25р. CSogd. pryž, Impf.: IND. 35р. CSogd. p’ryZ; Pret.: intr. IND. 
3pl. SSogd. prst’nt ‘they ran away’ 

*CHORESMIAN: r’z (f.) ‘secret’ (genuine ?) 

*NWIR: NP rastan/rah- ‘to be liberated, escape; to let go’, NP raz ‘secret’ (LW), 
Abyan. rahoya/rah- ‘to be saved’ 

*NEIR: ? Sh. (Baj.) raz-/rixt ‘to fall (leaves, fruit); to crumble, scatter’, Ishk. roZ- ‘to 
crumble, fall (leaves, etc.)’, Sh. razén-/razént (caus.) ‘to cause to fall etc.’, ? Rosh. 
réxt ‘snowfall’ (contaminated with Фаіс !) || (+ *apa-) Yghn. piráyZ- ‘to run away’ || 
(+ *abi-) Oss. I. irvezyn/irvezt, D. ervezun/ervazt ‘to be saved, delivered; to slip 
away, escape’ || (+ *a-) Pash. aratdl ‘to let loose; break wind, fart’, Pash. ár(o)t, 
(Waz.) ‘open, wide, loose’ 


*sacl 323 


*SANSKRIT: rah ‘to be lost, be lonely’ (GrSu.+), || rahas- (n.) ‘secrecy, loneliness’ 
(Ер.+) > EWAia П: 442 

9 Henning, l.c. derived SSogd. ’pr’st and Yghn. piráyZ- from *apa-raz-, to which he 
added as cognates, Skt. rah, OP rad-, MP rastan [wrongly cited: rastan], NP rastan. 
Mayrhofer, Le, has apparently overlooked this footnote and only acknowledges the 
Ir. ‘secret’ forms as related to Skt. rah: MP, NP raz, etc. The meanings ‘secret’ and 
‘to flee, escape’ are not necessarily incompatible, if we assume an older meaning *to 
escape (one’s notice)’. 

«PIE 0 The IE etymology cited in his previous work KEWA III: 49 (IE *leg"- ‘to 
lay’, Gr. Aéxoc ‘bedstead’, etc.) is doubted by Mayrhofer in EWAia, l.c. = LIV: 
401 f. | Pok.: 651 


*REFERENCES: Henning, Anc. Lett.: 612, fn. 5; Abaev, Slovar’ I: 549; Andreev — PeSéereva: 306b f.; 
EVS: 71a; DKS: 359a f.; Werba 1997: 370 f.; Lecoq 2002: 127; NEVP: 10 


Š
```


## [2026-09-14T01:11:21.587Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '25180,25250p' BRT.txt",
 "description": "Read Bartholomae around razah-"
}
```


### [2026-09-14T01:11:21.649Z] TOOL RESULT

```
j.  rayS.näman'  Yt.  4.  3:  lies  nOByS.»'.
•  j.  "ma/  ma  rava  ia%am  haitim^  V.  /. 1  PöZ.
•  j.  rava-  Adj.  sva.  rayav-.
KompA.  (s.  auch  raar*),  E.  (s,  arai/aat^a-).  — VgL  die  Bern,  zu  var^iüisma-  und  S  ^/S-
•  j.  ravat-aspa-  Adj.  (fem.  'pä-)  'der  die Rosse  flink  laufen  lässt':  usatjfum  . .  xJ^iy riTm  °pqm  G.j.  J.
'ravant-  Adj.,  PPA.  zum  V.  rang;  —  VgL r>njal.aspa-  und  ravarti-.
•  j.  ravan-;  rdiin-  m.  'Fluss,  FlusslauT: banlnavS  mansat  gairinqm  JqfhavS  mar^ tat  raonqm  ". .  die  Täler  der  Flüsse"  Yl 14.21;  18.6,  V,  5.  if.*;  —  bansnuh'a gairinam  .  .  jq/nühia  raonam  Y.  io.it, V.2.23.
Vgl.  rttuiah-  —  mp.  rSn  'Richtung';  np.  rin
'wegen' ;  s,  Bthl.  IF.  6. 309,  Salemann  GIrPh. /.  283.  —  Fü.:  raiatiäA  'Flecken,  DorT'), NpG. :  rüilä,  erl, :  daSi;  aber  Sü. :  iryälayai 'Teich'.  —  0  Mills  ZDMG.  ff.  131  hat  ein mir  unverständliches  räfifiäi.
•  j,  ravant-  m.  EN.  eines  Gläubigen; stipsi/  'vatB  asaonS  "des  A.,  Sohns  des H.  .."  Yt7^.i23.
£ig.Bed.?  VIl.Kurznamei  t.  ratrafatpa-'). — ■)  JttSTU  Deutung,  NB.  260,  setzt  ein  Praesens TOrans,  das,  nach  at.  lundti,  sbal.  runag,  jp. runä  (GlrPh.  /  b.  126,  243)  zu  schliessen. schwerlich  existirt  bat
•  j.  rava8-£arät-  Adj.  'was  sich  im  Freien, in  Freiheit  bewegf,  Bezeichnung  der  wildeti, nichtdomestizirten  Landtiere*';  a)  über- haupt; vjspqmia  gqm  .  .  'rütqm^a^A&tyl cat9ranhä&is{sA.)ca  Y.  7/.  9;  —  raiavS 'rata  (AP.)  Vr.  2. 1 ;  —  raiavS  •rätqm  (GP.) Vr.  /.  I ;  —  urutU!  . .  *rJtqm  Yt  13.  74;  — äätnqn  . .  yäca  'ran  (APn.)**  Yt  8. 48  **'.  b)  im  Gegensatz  2a  'den  in  den Bergen  hausenden'  die  der  Ebene:  auru-
:(sd.)ni  galriisä  sizdraca  'rätS  ".  .  und die  scheuen  (Tiere),  die  in  den  Ebenen streifen"  Yt&36.
*)  Sva.  daitiko;  td.;  vgl.  fam-oakai-,  —  All Raiav  dieser  Tierklasse  pit  Bd.  3.^  9  d«  Hase (xargSt).   Wdtere»  a.  unter  aidyü:  —   ••)  Hier
dby  Google
IS13
ravazda-
razah-
1514
scheint  raviuätrqn  den  Geg«n*atz  in  /ri^ffnjqn  j zu  bilden,  also  alle  Landtiere  va  umfassen. Pa.: /räx'  raftär.  —  ')  Nach  der  ä-Dekl.  — ')  Vgl.  iF.  S  39/-  I
•  j.  ravaz-dä-  Adj.  'Freiheit  schaffend, gebend':  xratam  . .  aiavaium  asSMjim (sd.)  'äqm  V.  18.  6.
Pü.:/<ij*a  äätär.
•  j.  ravah-  n.  'freier  Raum,  Freiheit':  ys
.  .  asäi  'vS  yaisa  (Sp.  28  m.)  . .  *vS  vi- va^aYt.ij.gg; — yo..havaiibya  bSzulya tanuye  'vs  agsisii!(sd.)  Yt.  i_3.  107;  —  'vasai x^äiir3m(sd.)ca  ..  qzasca  dui3%r3mla  Y.  8. 8;  ~-  yasca  ml  aibm  nar>tn  ^>j(sd.)  avi ava.gsnptim  °vBhu  paiti  uzbärayat  V.  18. 10;  Vtj.  4(?); —  aca  n6  Jamyai  'vaiAhe ".  .  zur  Freiheit'  Yt.  10.  5.
KompA.  —  Vgl.  nhd,  taum;  Dst.  MSL,  3. 55,  Osthof  MU.  4.  ij6;  anders  Meillet MSL.  12.  2J3.  —  Pü.  -.fTÖ^h,  Sü. :  vzddkahiam,  \ Npü, :  nur  baxG.  1
•  j.  rav5.frao3man- ''  Adj.  (auch  fem.); 'des  Flug  flink  ist':  aspävhu  .  .  äsavs 'ntanS  Yt.  J7, 13  '';  —  tistnm  .  .  'mamm  \ Yt  Ä  a ;  —  fravasayS  .  .  yä  . .  'mans  [ (NPf.)  YLy.29.
*frao%man- a.,  mm  V. /roi'- ;  vgl.  lu  MÄmax-. —  1)  Zn  Yt.  z/.   12  '%im'  geschr.
•  j.  ravö.manah-  Adj.  'des  Denken  flink ist'i  Tivlm  *p3r3ndi>n  yazamatde  rsvTm  'na- T3ham  rrvJm  ravS.valaishqm  rnim  ravS.- syaohmaaqm  "die  flinke  /*.  . .,  die  flinke unter  den  flinkdenkenden  ..  flinksprechen- den . .  flinkhandelnden "  Vr.  7.  2.
Pü.:  frä:^  minü«.
•  j.  ravö.va£ah-  Adj.  'des  Sprechen  flink ist' :  *pärmdlm  , .  nvTm  ravS,manaahqm (sd.)  . .  'laakqm  Vr.  7.  a.
PQ. !  /rÖJ^  S""'"!-
•  j.  ravö.SyaoS^oa-  Adj.  'des  Handeln flink  ist':  ^färmdlm  .  .  nvXm  ravCmana- Kkqm  (sd.)  .  .  '"iiinanqm  Vr.  7.  2.
Pü. :  frä^  kunilti.
p.  ras',  Verbalf.!  s.  ^ar-,
•  j,  raSE^'Qt-  f.  -  ?  — ,  als  Gottheit:  aiSi^ vaahuyh  HstBil . .  "?«&?  ■ .  '/3Ö  vaaiuyä Y.7. 14.
Ableit  «na  rasant-,  J  2^4.  3.  —  Pü. :  reu  esH!- lüh,  Sa.:  ciOastAitik;  s.  in  risanl:
»  ].  rasman-  m.,  n.  'Schlachtreihe ,  Pha- lanx': spala  . .  raihm  (sd.)  rasma  (NSn.) katarasHt  Yt  /4. 43 ;  —  ys  'manS  (APm.) sandaydti  Yti^öa;  61',  10.36,  41;  — antan  rSlta  'mana  (ADm.)  Yt74.47;  —
•»(a«ff(GS.)  amSJütahe  YtJO.36;  — yä 'manB  . .  *jra  *karana  sSnäayänti  Yt  13.
\Z9>  —  ipä%>m  .  .  äeräi  ayartfom  'maoys (DP.  statt  IP.)  Yt5.68;  —  avi  Aqm.- yania  (Sp.  153  m.)   'maeys  Yt/o.  8;   i^.
j  49;    —    *%raxtanam  (sÄ)    'rnanam    Yt
14.  63.
KotnpA.,  E.  —  Zum  V.  rat-,  %  384.  —  mp.D, np.  tazm  'Schltu:bt';  vgl.  gr.  ipt^^u,  Ut  rigi- meti.  —  S.  auch  raean-  mit  No.  z.  —  ')  S. dazu  Hbm.  AGr.  7.  233.  Das  Wort  ündet sich  noch  in  PüErL  lu  Yt  /.  14.
•  j.  rasmÖ.Jata-  Adj.  'in  der  Schlacht- reihe getötet':  'hm  vä  dim  jainti  amö.- jat»m  (sd.)  vä  Yt  lo.  52.
•  j.  raz-  V.  'richten'.  Fiaes.  30  (Iter.) rosaya-,  —  PPfP.  raSia-,  rasla-'\
i)  'richten,  gerade  richten,  ordnen':  yat \sp3ta  han/asänte  .  .  ra/t^m  rasma  kata- rasHt  "wenn  die  beiden  Heere  zusammen !  treffen  .  .,  ein  jedes  eine  (in  Reihen)  ge- richtete Phalanx"  Yt  i4-  43;  —  antan \  rästa(ADm.)rasmanaYti4.4T, — yahmya !  sästärU . .  paoiril  Irs  (sd.)  rätayente  Yt.  10. 14.  a)raii';'walsAdv.  sbes.  a)'recken (gewaltsam),  verrenken':  vT  maityqmm fiänayeinti  {s^)  vTspa  handäma  räzayänti Yt  14-  56.
mit  Rl  —  ?  — :  sao^ayanta  Siti  mrasa- yanli  Vyt.^6'.     Wertlos.
mit  ham  Med.  i)  'sich  aufrichten, emporrecken':  dhat  fraia  hqm.rätayata atarl  Yt  ig.  47;  49.  2)  'sich  etwas  zu- rechtrichten,  (die  Haare)  ordnen,  kämmen': yB  .  .  varMas{sd.ya  *Aqm.rlltayeite  vari- säsca  pairi.brltmiti  Y.iy.  2;  —  yat..  varv- ias(sd.)ca  *Aqm,rasaya»Äa  V.iy.4.
np.  afrSxtait,  woss.  aratjn  'richten',  PDw./»/. rüzam  'ich  recke  mich';  lat.  rfc/ut,  got  raikis.
—  Vgl.  »«ZOT/   Pü,(iuV.v).  Npa.  (in  Yt
/rf):  araiian.   —  ')  S  ^PP-  7  ^°-   '•■
•  g.  razaii-:raÄ-''  n, 'Ordnung,  Satzung': yS..drlta  ayatOim  urvatBif{sd.)..hutSntui .  .  rainH  (IS.)  fvas  yS  aiavä  drsgoanttm
Y.46.5- Zum  V.  rat:    —    VgL  raiaip.  und    «och  rat- man-  •).   —  Pü. :  fia  rahi.  —  ')  S  iS.  1  a.  — ')    Da   man   die  Gleichung   aafstellen  kann: rasma  :  raSnä  -  atma  :  ahta;  s.  ataa-  No.  I.
•  j.razah-  n.  "Einsamkeit,  Abgelegenheit': 'tS  F.iy,  —  Plur.:  düire  asoAi  °sar»hqm "fem   an   einem  Oit  der  Einsamkeit"  V.
Ä97-
aL  yäkat'  n.;    TgL  np.  rät  'verborgen'.  —  S.
m  raä:  —   Pfl.  (tn  V.  S)i  Ikar  'J^d'i),  (lu
dby  Google
>SI5
"raza^^da
F.):  vä-äil  'geordnet'*).  —  »)  West  SBE.  zS. 455  will  valiar  'upon  a  wild  tpot'.  —  >}  Ali ob  ei  räü  hiesse,  vgl.  eq  iarü.rStah:
•  j.  "razsig^da  N.^.
•  ].,  g.  raziita-  Adj.  (fem.  *ta-)  'der  ge- radeste, richtigste,  rechtlichste,  gerechteste': *ya%a  *äis  lä  J  vansaitl  yä  data  ataJau! paouruyehyä  ratüi  iyaohana  °tä  (APn.) dngvata^ä  hya^cä  *aiäomye^aca . .  "wie es  den  Gesetzen  fiir  das  erste  Leben  ge- mäss ist,  so  wird  er  (näml.  Zara^u/tra) als  Richter  in  gerechtestem  Tun  gegen den  27rt(fgenossen  verfahren  und  gegen den,  bei  dem . ."  Y.j;^.  i''.  a)  von^an- tay-  (usw.) :  °öw  pantqm  daoaiti  ätars  . . ySi  ftißirym  lUfil  aiwidruzinÜ  "den  ge- radesten Pfad  gibt  (weist)  A.  .  .  denen, die  . ."  Yt  /o.  3;  —  mit  3  und  Abi.  oder Akk.  'hin  —  zu':  'tah^  pa%S .  .yS  asti  't3 j  aiäi  vahist)m!a  oASrn  asaonqm  "des geradesten  Pfeds  . .,  der  der  geradeste  ist hin  zu  Asa  und  zum  besten  Leben  der Gerechten"  Y.  6Ä  13.  a)  ahatpantay- (usw.),  das  aber  hinzuzudenken  ist:  yö dai^hsus  rqxlyqi^yh para  •/Jfnäml^a^i) baraiti  Yt.  io,  37*';  —  äid3?ar?nä  nastö •ta  (näml.  /a^a)  ". .  der  vom  geradesten Weg  abgegangen  ist"  Yt.  10. 105^';  — amuyamna  (sd.)  'tanqm  (näml.  pa^qm) Vi.17.1j;  13.3s-  b)  von  rainav-  m. (Stverz):  rar'hus 'tH  V.  13.  g  PUZ.jusw.;  — 'tfm,  'tat,  •iahe,  'ta  (VS.).  A)  mit  asts-  f. (Stverz.)  Name  einer  Gottheit:  °ta  ästa \'t.i6.7  usw.;   —  'tqm,  'taya,  'te  (VSf.).
Superl.  in  imav.    —    ai.  täjisfia-  Adj.,  mp.
raüilai.  —  Pü.:  raüslak;  (in  Y.  33):  räiäusn,
SQ. !  hiädAalä.  —  OS.  iSL  unter  myas-  •)  nnd
Gdn.  BB.  1$.  251.    —    ')   Im  Gegensat:
Yt  10.  3.  —  3)  Vgl.  Y.  S'-  '3-
•  j.  razura-n.,  razurä-f.  'Wald':  a%anä
ä.xüa  buyqrt  *ya%a  nä  bi^ät  . .  s^atacina
'ra  (NP.)  Yt.  16. 3;  —  upa  *vimaiiTm  °raya
(LS.)  YL75.31.  a)  m\t  spaätita-,  spaf-
```


## [2026-09-14T01:11:31.999Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^IS0[0-9]\\|1505\\|ISOS\\|1S0S\\|150S\" BRT.txt | sed -n '1,20p'; echo \"=== leaf of line 25197:\"; head -25197 BRT.txt | tr -cd '\\f' | wc -c",
 "description": "Locate Bartholomae col 1505"
}
```


### [2026-09-14T01:11:32.093Z] TOOL RESULT

```
=== leaf of line 25197:
827
```


## [2026-09-14T01:11:35.717Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==825 || NR==826' BRT.txt | head -60",
 "description": "Print Bartholomae leaves 825-826"
}
```


### [2026-09-14T01:11:37.070Z] TOOL RESULT

```
 (sd.)  aiSqm  "i'äj'fl  (LS.)  YL70,38;  — paiti.- stayata  'ihya  aül  vat>uhi  "es  luelt  an  auf dem  Wagen  A.  . ."  YLr7. 17;  —  akmya 'äa  hvasäna  \yX.48;  —  nöit  ihra  ../ras hyat  .  .  halnyS  '%ö  nsit  uspnpts  draßs YlÄsö;  —  yat  janäni  kitäsptm  'i^e paiti  vagaihyai  (sd.)  YLi^.aS;  —  tarn caxnm  (sd.)  . .  asmatam  ''h3in  ktnnavane . . ti  mg  väitm  ^anjaySnte  spirdasca  mainyui' attrasca  Yt.J(j.  43f.
*)  rAa-  und  ^äxra-  bilden  nach  Yt.  /p.  43f. lusammen  den  väia-.  Sonach  bedeutet  ru^fl- im  Gegensatz  zu  väia-,  womit  der  Wagen  als Ganzes  gemeint  ist,  insbesondere  den  Wagen- kasten. Unrichtig  Gor.  OK.  391;  vgl.  Vt.  10. 52,  68  U.Ö.,  sowie  die  Komp. KompA,  (j-flifl",  ra%a!',  ra%Bi'),  E.;  Abieil, (s.  anch  hurä'i<va-'\.  —  aL  rälha-  m.;  mp.  ras.
•  j.  'ra'Ö'a-  m.  Name  einer  Pflanze  (?):  ^J °'%Ssca  pasvamdlsca  bammaine  "Äam,- vanniaymü  N.gj.
Ganz  unsicher.  -—  PQ.:  fehlt
•  j.  raö'ae-star-,  rad-ae-ätä-,  ra95i-ätä-'' m.  'Krieger,  Kriegsheld':  ya'ha  «j  taxmS °tä  (NS.)  Yt  13.  67;  —  taxmim  tusim  'ia- nm  Yt  5,  58;  Vyt  26;  —  mihnm  .  .  yim yaztnte  'tärS  Yt.  10.  \i;  j.  53  '> ;  —  mihrfm . .  laxiram  °tam  Yt  70.  140;  112,  25,  102; —  iraosahe  . .  taxmake  .  .  'ta  (GS.)  Y. 57-33;  —  ätari  spmta  'i3ra<yS.)^  Ny.j. 6;  Y.  ä^2.8Gl.  A)insbe3.alsBezeichnung für  den  zweiten,  den  Kriegerstand  (vgl.  unter 'piära-):  shrava  '/i  (NS.)  västryö /ü^qs Asitis'  Y.  ig.  ij;  11. 6,  Yt.i3.89,  V.5.  38, '^•45^i  —  ähravarum  ..'iär>nt  ..vasirJm fsuyantftn  Vr.^.  2;  Yt2, 12;  —  a%auru- naSca  °tüua  västrySica  fiitymte  Yt/p.  8; 7J.88,  V.5.  57,  58;  —  västry^Z  fsuyatas ..  'tä  (GS.)  ..  a'iiaurunS  Y.  13.21.;  — asti  iir  haim  (sd.)  ydha  'tärahe^l  Y.13. 44;  4Si  Vyt  J,  16,  Az.5;  —  vUpe  saya °%äis'ti  (LS.)  "alle  Ausrilstungsgegenstände für  einen  Krieger"  V.  74-9;  9;  —  '^^<»- urunqscä  -tascä  (AP.)  västryas^a  f/uyants Y.  7j.  3;  —  a^aurunqs^a  'tarSsla  (AP.)3) väitryqsca  fiuyants  Vr.^j,  5;  —  hast»ma alahe  ama  'ta  Y.13.2.
Komp.  mit  LS.  im  I.  Glied,  V/ar-  aus  idg. *jtAer;  der  KompForm  von  *ilAiltr-;  zum V.  stä-.  —  ai.  rathcffha-  m.  'Wagenkämpfer'. Utt  IF.  g.  209,  —  Pü. ;  arateUär  (gelW.), 48
dby  Google
ISO?
rad-aestä-
rapaka-
1508
Sü.:  kfotriyai.  —   0  Nor  in  ra%iuti  V.  14.  9.
—  •)  Ungeschickte  Herubernahme  ansVt 1 1 ;  falsch  S  396,  400.  —  3)  Tfaem.
•  j.  raS^eitä-  m.:  s.  unter  rä^aiÜar-
•  j.  raO^kara-  Adj.  (fem.  •kairJ-)  '(einen Wagen,  Wagenkasten  bildend,  d.  L)  wie ein  Wagenkasten  gestaltet"':  ufairi pusam bandayata  artdvT  .  .  asta^aoiäqm  'iair- yam*^  YL5.  n8.
■)  Anders  (falsch)  Gdn.  KZ.  xj.  401  ('uimutig'}, DsT.  ZA.  2.  396  ('en  forme  de  rone').  — ')  Nach  der  ä-DekL,  in  Ausgleich  mit  dem Tothergeh.  Wort.
•  j.  ra^üiä^nin^in  AbsoL  '>  'beim  Dahin- eilen im  Wagen,  beim  Fahren':  ahmt  .  . yim  sästa  daiähSus  .  .  patititim  (sd.)  vä .  .  'mm  vä  YL  75. 50.
Komp. :  raÄo— t-'iwwfu«,  Absol.  lam  V.  ^aS-
—  Geringe  Stelle.  —  »  Bthu  IF.  li.  348.
•  j.  raJhöi&tä-  m.:  s.  imter  rdhaistar-.
j.  ri&iaayäi  N.  ^6:  lies  rae%w:
•  j.  •ra^'wya-  Adj.  (fem.  'ya-)  'was  der gegebenen  Zeit  entspricht,  angemessen  ist, was  sich  zur  gegebenen  Zeit  und  im  ge- gebenen Fall  gehört':  ya^a  'ya  (NSf) vanna  (Sp.  1372  u.)  V.jj.  46;  —  mthnm .  .  yS  .  .  fravazaite  .  .  'ya  (IS.)  *äxra (sd.)  Aaämnff  Yt/0. 67;  —  yas3  ^wa aextö.nämana  yasna  'ya  (IS.)  vom  yazaite Yt  J0.3o;3i3,  56;  —  'yi  uxlä  F.jf.;  — vavan9  buye  'ya  manaaha  'ya  valargAa 'ya  ^aohna  A.  7, 1 1 ;  —  sonst  neben däitya'{sd.):  viovä  däilyqm ..  *yqm  ävisiim ". .  die  in  rechter  Fonn , ,,  zu  rechter  Zeit ach  vollziehende  Weihe"  Vr,  77.19; —  '^*'- yanqm  'yanqm  kvarstanqm  fyao%nanqm varttäi  pairi  a%3ityanam  ard^wyanam vansäi  Yx.15.  i;  —  argdvlm  .  .  yä  .  . iäirümqm  daitim  'wjtn  patma  ava.baraiti ". .  die  den  Umständen  und  der  Zeit  ent- sprechende Milch  .  ."  Y,  6j.  2 ;  —  in  der Rechtssprache  :f/di>V<i  'ya(APn.)/rSrai^ya (sd.)  F.^e.
KompA. ;  E.  —  Ableit  ans  ^raiav-.  —  ü.  vgl. X-tviya-  Adj.  —  Pü.  (zu  V.,  F.,  Vr.  IK,  Y.>! frirö»  -  (lu  Y.  erl.):  j^^  -,  (zu  Vr.  7/): ralVtä;  Sü.  (lu  A.):  ladätarl.
•  j.  "raÄTwya-  Adj.  'die  Hatav  betreffend, zu  ihnen  gehörig  (usw.)':  avi  ratüf  avi  *ya garmU  Vr.  4.  i  (?).
Ableit.  aas  'tatat-.-^  Gini  nnsicber.  —  Pü.: etän  pa  an  tafih  u  ctSn  fia  an  raliA  rasihüA. VgL  
dain  Sp.  Komm.  2. 17,  DsT.  2A.  /-457-
•  j-  "galwa  kurs  (sd.)  . .  rad-wyasiufm buxts  ma^e"  FrW.2.2.
•  j.*raSTwyö.varstay-'*  f.  'angemessenes Handeln, Tun':  mananhaica*humaiH  Mt- vasca  huxti  zastayasca  *kvarsti  °ti  natdys (sd.)  aAmi  . .  "bei  gutem  Denken  des Sinns,  gutem  Reden  der  Zunge,  gutem, angemessenem  Handeln  der  Hände  bin ich  . ."  P.  28.
Pä.: /raren  iumiH.  —  ')  Hds.  ara%tB'.
•  g.  raiSya-  n.  'Weg':  data  xratsui  hitv9 '%Jm  stöi  mahyä  rizfng  .  .  sOAlJ  (sd.) ". .  damit  meine  Zunge  einen  Weg  habe . ." "' Y.50.Ö.
Ableit  ans  ra%a:  —  Vgl.  ai.  ratkyä-  f. 'Strasse',  np.  räh  'Weg'.  —  Pü.:  ras,  erL: JrahaxBk.  —  1)  D.  i.  dass  sie  den  fechten W«g  finde.     Vgl.  iSt.  Gdn.  GlrPh.  3.  31.
•  j.,  g.  rap-  V.  'Unterstützung  gewähren, —  finden',  Praes.  3  rapa-,  —  In£ ra/ihräi.
i)  'Unterstützung  geK^hren,  eine  feste Stütze  bilden,  sein  fiir  — '  (Dat);  a)  von Göttern:  rapdisca  tu  HS  äangrmiä  lUtäia Aaiqm  hudästsmä  Y.  47. 4;  —  ahunm mazdqm  d(ä)vanh3m  .  .rapantim  tarhia- nhtm  vispa  *voAü  Y.  yo.  1.  b)  von  Men- schen, gegenüber  den  Göttem  sva.  'ge- treulich dienen,  die  Treue  halten':  at  tsi atrJm  .  .  usJmahl . .  stSi  rapantl  ührä,- avatffam  (sd.)  at . .  daibiiyaniw . .  dirvstä- aSianhitn  Y.j4-4r — *stöi  *rapantqm^^ Ny.j.  10;  —  ayaptä{sA.)..yaii  rapantB daidu  x^äiri  ". .,  welche  die  Getreuen  in Wohfbehagen  versetzen"  Y.  28. 2.  2)'Un- terstützung  finden  bei  — ,  eine  feste  Stütze haben  an  — ',  mit  Gen.:  tat  mei  dsidl ahurä  hyal  matda  rapfn  tavä  "das  schaff mir,  o  Ah.,  dass  sie  an  dir,  o  M.,  eine feste  Stütze  haben"  Y.57. 18.
mit  a  dnwS.  i  a:  vanuAl  Oda  gaidi msi  ä  moi  a'^rapa  "mit  der  guten  Ada komm  zu  mir,  sei  mir  eine  feste  Stütze" Y.4P.I.
Et.?  Ohne  Wert  IF.  a.  il.  —  PS.:  rämFni- lär,  'tSrih,  (an  Y.  4g) :  arämemlär  {mit  neg.  a, Npü, :  bl)i  Sü. :  äiiaaJak,  priOHodatBam,  äntm' daiatiä.  —  ■)  Eine  nngescbickt  verwendete Reminiszenr  ans  Y.  34.  4.  —  *)  Nach  dem Metrum  zu  streichen.
•  j.  rapaka-  Adj.  'eine  Stiitze  bildend für  -,  im  Dienst  stehend  von  — '  (Gen.): a^  (näml.  daxmS)  sJ  asti  daibaitqtn  'AS vupsm  a  oAmOi  yat  alfa  *gainti/ tipaioAa- aüti  (sd.)  V.7."s6.'
Znm  V.  rafr.  —  Pü.:  rämilu.
dby  Google
'S09
rapant-
raoha-
1510
•  g.,  j.  rapant-  Adj.,  PPA.:  s.  rap-.
•  j.  ra-piihwä-  f.  'Mittag':  haca  '%wayät *matlyai  utayarai  pain.sacaiti  "sie  währt vom  Mittag  bis  zum  halben  Nachmittag" ^■49',  —  äat  yimB /ralasat  raoch  ä  upa •%wqm  hu  paiti  ahwanam  "da  ging  Y. zum  Licht  vor  am  Mittag  dem  Pfad  der Sonne  entgegen"  V,  3.  10.
Ableit.  —  Vgl.  ar3m.ps%ii,ä-,  ra  ist  AbUut». form  lU  *ata-,  woraus  arim  als  Adv,  —  Pn, (M  N.);  rap,%'«,m,  (lu  V.):  r<,p,%^in,„r  rSn.
"  j.  rapid'wana'tara-  Adj.  'der  südlichere, südlich':    ya^a  vatö  'tarät  nannat  .  .   A,
Kompar.  aus  *rafAwfna-  Adj.,  Ableit.  aus rafAwä-;  s.  rafAioitara-.
•  j.  rapi^Tvi'tara-  Adj.  'der  südlichere,  süd- lich' :  ä  dim  vätS  upa.vävS  satayeiii  'taral haca  naimäX  'iaralibyS  haca  naimatibyö H.  2.  7.
Kompar.  aas  "tap&iwa.y-  Adj.,  Abtcit.  aus  ra- pt^wä-;  \.  rapi^vanatara:  —  Pü.;  rap^^wintar.
•  j.  'rapi^Twina-  Adj.  'mittägig':  ä  °mm zrvamm  Y.p.  1 1,  Yt  &.  a8.  A)  m.  Gott- heit der  zweiten  der  fiinf  (priesterlichen) Tagesabteüungen'^:  'mm  asavamm  asahe ratäm  V.  2.  4;  G.  2,  5;  —  yS  'nahe  ralu- frita  'mm  ratüm  framaraite  *n»m  ratüm fräyazäiie  A.4-5i  —  °n3i  .  .  ra%we  .  . frädatßave  zantumäica  Y.  j.  4;  G.  2.  i; —   'nahe  ra'iwS  A.4.3;  —  'na  aSäum
y.  T.  20.
•)  Genannt  rapi%w3-  (id.)  und  nach  N.  4g von  Mittag  bis  zum  halben  Nachmittag  wäh- rend; TgL  noch  Bd.  35.  9  {nimric  gas)  und  zu asiiya:
Ableit.  — Ableit.  aus  riT/i&wä-.  —  Pa.:trans3iir.;
SQ.  erl. :  madhyähnahsamdhyah,
•  j.  *'rapiOTwina- "  Adj.  (fem.  °«a-)  'den Rapiärwina  betreffend,  ihm  gebührend': kahmäi  haca  ^•'^winanqm''* gä%anqm  ratu- fris  frajasaiti  N.  49.
Ableit.  aus  ^rafÜMiina-  (mit  Verschiebung  des Haupitons).    —    Pü.:    Uansskr.    —     ')  Hds.
j.  rafß  V.  13.  4S  :  lies  yaiö.
•  g.  rafsSra-  n.  'Unterstützung*:  'rSm cagva  hyat  /ryS  (sd.)  fryäi  datdlt  V.  46.
3  i  —  yaz»mniT>hö  (sd.)  nsmaahä  . .  'r>m cag3dB  Y.5J.  30;  —  ahyä  yäsä  (sd.)  mma- nka  ustänazasis  'rahyä  "zum  Gebet  um Unterstützung  die  Hän
```


## [2026-09-14T01:11:46.648Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==824' BRT.txt | head -40",
 "description": "Print Bartholomae leaf 824"
}
```


### [2026-09-14T01:11:47.776Z] TOOL RESULT

```
(statt  NP'.);  —  agtämtJ(sd.)  'fris yaval  framaratti  N._?<S'i  3g  (statt  NP.), 2/',  2j;  —  °fril  canmanqmca  pasu.- vastranqmca  N.  ^8;  —  ci'aiti  narqm  *ÄaxtJ zaota  (sd.)  °fris  ahumm  vainm  frasrao'- yehe  N.  20.
KompE.  —  "J^l-  Adj.,  zum  V.  fräy- ;  ai,   */r7.
Adj.  —  Vgl.  iralii/rl-  t  —  Pü.:  rcOIAi.  — I  ')  Hds. /rfl-V*-  —  ''  Hds.  ralißh  ratuTöö, I      beide   lasammen    slatt   rafu/rii.    —    1)  Hds.
aralu/r*.   —    4>  Hds.  ralai.    —    S)  Hds.  raiu-
•  y  ratu-fritay-  f  1)  'Zufriedenstellung der  Satav,  an  die  Katar  zum  Zweck ihrer  Zufriedenstellung  gerichletes  Gebet': iiisptm  alavarum  aya  °ta  (LS.  als  Instr.) '' hvävayaahiin  ..paiti.bar3hi  humatiisia  .. Y-5i-4;  —  ahm3k>m  havanklica  'tayalca alavastäica  .  .  yai  saoiyanlqm  asaonqm Vr.  5. 1 ;  —  vispalsqmea  ra'^wqm  vlspa- ttqmla  'iinqm  Yi.g.j; — jaymBsyS  asSis .  .  jaymUsyä  °töis  Vr.i?.6;  —  ra'^walca 'layaica  Vr.  4. 2  (?) ;  —  yS  g.fi  anqm  aii^qm °tim  ava.radoayeiti  N.  43;  —  imqmca urvarqm  *bargsmainfm  /aymüslmla  'tlm mar^rsmia  var>zlmca  damaya  .  .  gaha- nqmca  srad^rim  JaymUiSmca  . .  ra>WJ 'ITm  Y.  22.  3;  — /aymuH^mam  ..  ra'iwJ 'iTm  yazamaide  Y.  7/.  3 ;  —  imqm  ar»hu- yqm^a  *asayqmca  ra'hwqmca  Ülm\fa\  Y, 3.4;  —  besonders  von  den  in  den  ver- schiedenen Tageszeiten  an  die  RatavdAmya (sd.)  zu  richtenden  Gebeten":  ys  rapthwi- nahe  '/a  (I.A.  als  Instr.)  rapi'iwinim  ratüm framaräite K. 4.  5; — yalät pascaita  aorqui °Um  ava.raghayeiii  tanüm  *firydti  "wenn er  alsdann  ein  einziges  der  täglichen  Ge- bete versäumt,  so  . ."  N,  42;   DS.  als
Inf.  sbes.  2)  'die  wegen  Beleidigung der  Ratav  notwendige  Sühne' ■^*:  altalsam ratufril  'tim  *hwfrisaili  "ihnen  schret'bt deijenige,  der  den  Ratav  gegenüber  seine Pflicht  erfüllt  hat,  die  Sühne  für  die  Ratav vor"  N.5j;  52.  [N.6'7;  lies  ratufrii.]
KompE.  —  Vgl.  tralu/ri:   —  Pü, :  rai/rani- mismfi,    Sü.:  gurvatmjnä;    %.  noch  Nq.  3.  —
ob,Google
raS'aestar-
1506
9.  _   i)  VgL  ^ratufri-  a.    —   J)  PüErl.!
•  j.  ratu-frit?e  Inf  "die  Ratav  zufrieden zu  stellen':   yat  pairi  Öansma  hanjasante 3at  r'  ". .  so  dient  das  dazu,  die  /?. frieden  zu  stellen"  N.ö's;  —  coat  niümpm hastnm  (sd.)  atshat  V°"/  N.^/.
Zum  V.  fräy-.    ~  'VgL  ral«fritay:    — fa  ral /ranämih^fh).  —  »  Hds.  fry».
j.  ratHfryät  N.  31:  lies  ratu/rißc.
j,  oäTä  ralufiU  ratu/Hs  tt.So:  lies  «iS
•  j.  ratu-naya-  m.  'Laie'  (im  Gegensatz zu  'ratav):  ratus  'nasin  a^a  'nays  ratüm A.J.  13;  —    myazdavi  ratus  amyazdc n?m     'naim    ayasttim   (sd.J    daste    antara mazdayasnäis  K.3.T,  8-12.
Eig.  'unter  der  Leitung  (*naya-  m.,  zum  V nay;  w.  -riaya-  m.)  des  J{.  stellend'. —  Npü. AäviSt,  Sü.:  Ü^a^  'Schüler'.
•  j.  "ratu'mam-   Adj.   'der   einen  Xa/av besitzt',   stets   neben  ahumani-  (sd.,  auch fdSt.):  •mat  P.jj;    —    <matS  (GS.)  Vr.  j. 5;  —  'irantam  Vr.  2.  7 ;  — +'»10^  (NS.) Vr.  2.  7,
Vgl.  aratav-.  —  Pq.  :  ralBmandih ;  vgl.  lu  a/" manl-.  —  1)  NA.  ralümla;  s.  ahumant.  No.  4.
•  j.  ^atu'mant-  Adj.  'das  Wort  ratav- enthaltend"':  aHai  vaiö..yaf  aAumat{s±) yai  ratumat  Y.  ig.  8.
Pü. :  ralämand,  erl. :  daslawar  daran.  —  1)  Vom /üauoräiVcflgebet.
•  j.  *ratuä.mar3t-'>  Adj.  'der  auf  den Ratav  merkt,  seine  Weisungen  beachtet': 'ta.  (IS.)  dagns^aca  Y. /p.  17.
Zum  V.  2mar.;  «tatt  »ratuSm'  geschr.  —  >i. '.J™/'-  Adj.  —  Vgl.  m)r>%7vane..  —  pü.:  rat öimuri,  erl,:  ^  daslawar  däriti  Sü.:  A««». /I/^i/ai.  _  .)  NA.  trennt
•  p.  rad-  V.,  nur  mit  ava  'verlassen'. Praes.  2  rada-.
i)  'verlassen,  abweichen  von  -':  pähim lyam  rästam  ma  avaradc^  m3  *starav<^ (zS.)  "vom  gebahnten  Pfad  weich  nicht  ab, versündige  dich  nicht"  D.6".6.  2)  'ver- lassen, im  Stich  lassen':  vis'tasfc^..  *avam *kanr  avärada^  (3S.)  Bh.2.  j6".
ai.  rahali  'er  verlisst',  np.  rakad  'er  kommt los  von  -•'),  —  I)  Ergänzung  nach  Fov  KZ. 35.  4z;  VgL  Eü.  Aber  Rl.  JrAS.  ij.  iv  las ai--4-^.  —  1)  S.  noch  /Üs.  lu  'j-ai-..  —  Dass ai.  rahah  mit  rähas-  n.,  jAw.  rasak-  lusam- mengehSrt  {so  zuletzt  FoY  KZ.  ^7.  564),  wird flnrcli  das  np.  Wort  unwahrscheinlich.    Viel-
mehr ar.  *radh-\  ».  'rood-  No.  I.  Wegen  der Bed.  des  np.  Verbums  i.  ai.  raAila-  Adj.,  PHP. lu  rah^aH,  eig.  'losgekommen  von  -'.
•  j.  'ra^-a-  m.  'Wagen'*':  gäui  frazarSta
```


## [2026-09-14T01:12:13.632Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD rastan/rah/raz\"; grep -n \"rastan\\|reh-\\|^raz\\b\\|rāz\\|rastagar\\|rastag\" PHD.txt PHD_mackenzie.txt | head -30",
 "description": "Grep MacKenzie"
}
```


### [2026-09-14T01:12:13.706Z] TOOL RESULT

```
=== PHD rastan/rah/raz
PHD.txt:122:/abāz dādan б: 1. attribute, ascribe to; 2. appoint to. br ... add M fr! va-čār add helpless. delete á-distag ... (read ayidtag) add ‚тах |°р1°с | N farāz] acclivity. Afson ... add M ?pswn. Vagar ..., add useless. vāgēš [kw | (M "^ wa, P ?gwc), N aqóš] embrace, armful. add vājištag | gyštk' | P * gyšt, N ayišta] mixed, defiled. add \Ahliswang |*hlygwng] = Ard. delete Khriswang ... for alum ... read „alum |? № | N <] millet. Vāsnūd(ag) ... delete noble. aswür [|PR/LSYA < A pršy';.. āšnāg ... add acquainted with. āštīh ... add concord. ayad ... read |" byd^t' |... for bahr... and bahrag ... read bahr(ag) |b hl(k') | M bhr, N ~(a)] part, portion, share, lot; reason. (az) an bahrag ray : on that account, therefore. for  bahrwar ... read bahr(ag)war [b'hl(k)wl | N bahrawar| partaking, parti- cipator, partner. ~th : participation, advantage. balay add M by. add balgam |[blgm | N balyam] phlegm. baxtan ... add divide. bayaspān [by?sp^n' | = M]... bélür ... for M read P bylwr.
PHD.txt:170:abilag 5/4! | N ~a] blister. a-bim [bym] fearless. āb-kāmag [5A mk! | N ~a] a thick, sour soup. abnüs Pžēnws | (N ābnūs)] ebony. a-biy Pbwd] senseless. ~ih: senselessness. à abr РЫ, Séi | N ~] cloud. M bel abrang [ing | N aurang] glory, splendour. abrastan, abraz- [AP stn',SPc- | М ?br?st, N (afráttan), afrdz-] lift, raise. abraz [Pe | N afrāz] acclivity. abrēšom Pflyš(u)m | M? bryfwm, N ~} silk. ~én [-yn!] silken. abróxtan, abróz- ['piwhtn', ?phoc- | M brwxt, ?)brwc-, N afróxtan, afróz-] light, kindle, illuminate, polish. ~i$n(ih): illumination. āb-tazan Pftcn!] watercourse. a-bun [*dwx!] baseless, bottomless. a-burd-framān ['bwltplm^n'] disobedient. ~th: disobedience. aburnāy f(w)lnd, v. purnāy | N burnā] under age, child. ^h : childhood. aburnáyag [?A(w)/n’(d)yk'] child. abus [pws] (woman) having just given birth. “АҺ: childbirth. арив, -tan Pws, -tn! | M ’bwws, v. ábestan] pregnant. „il: pregnancy. abydxtan, abyóz- Phywhtn', ?bywc-] join, mix. āb-zan zn! | N ~] bath. labzar [el pel] M *6c*7, N afzār] instrument, means; spice. *abzar [6271 | M bail skill, power; powerful. „ūmand [-wmnd] skilled, able. abzāy-, —išn, у. abztidan, abzón [?pzwn! | M, J ”*bzwn, N afzün] increase, growth. ~ig [-yk!] increasing, expansive, bountiful. ~igih: bountifulness. abzüdan, abzáy- ['pzwtn!,^?pzd- | M ?bz'y-, N afzüdan, afzāy-] in- crease, grow. ~i$n: increase, growth. a-čār [cI] inevitable, Jee ~ag [-k'] compelled.
PHD.txt:281:brāzīdan, brāz- [bPc-ytn! | M br?z-, N barázidan] shine, gleam. ~išn: radiance, brightness.
PHD.txt:314:~th: friendship, love. 140$ [dws | N ~] shoulder. 2108 [duš | N ~] last night, previous evening. dēš-, —išn, v. Ł 2 dēšīdan, !doxtan. dēšag [dwsk'] dear, loving. —ih: love. došaram [dwi?m | M dw%’rm] love. dēšastar [dušstl] west. īdēšīdan, 458- [dws-ytn!] like, love. ~ign: liking, pleasure. *došidan [dwsytn'] = *dóxtan. dēšīzap [dwsyck' | (M дох, ] dwskyzh), N —a] maiden, virgin. “АҺ: maidenhood, virginity. dówom [2wm | N ~] -second (in compound numerals). 1dóxtan, dēš- [dwhtn', dws | N ~] milk. *dóxtan, döz- [dwhtn', dwc- | N ~] sew. dóys?r [dwysl = Av. dõiðra-} eye. dēz-, v. ?dóxtan. drafš [dips | P drfš, N ~] banner. drafšīdan, drafš- [dipi-ytn! | P drfi-, N ~] 1. shine; 2. tremble. drahm [ZWZN! < А zwza | M drhm, N dir(h)am] drachm. dra(h)nāy [di(k)rd) length. dramanag [dimnk! | N dirmana] wormwood. dranģ [ding | N dirang] period, duration. dranjidan, dranj- [dInc-ytn!] speak. ~išn: speech. draxt [4/0)А | M drxt, N diraxt] tree. drày-, ~išn, v. drāyīdan. drayā(b) [dlyd?(p) | M dry?b, N darya(b)] sea. ~-bār LI | N -bàr] sea-shore. агауӣп-јбуіёп [did?n ywdsn'] one who speaks while eating. ~ih: (the sin of) speaking while eating. drayidan / drayistan, drāy- [dPd-ytn!, -stn! | M dryst, dPy-, N daráyidan] speak (daevic), chatter. —išn: chatter. drāz [dlc | N diráz] long. *drém [dlym] phlegm. driyó$ [41220 | N daryūš, darwé§] poor, needy. ~th: poverty. dró [KDBA < А kdb’; dlwb! | M drw, (N daróy)] lie, deceit. drd [SRM < A šim; dlwt! | M атта, N daród] health, well-being, prosperity, peace. dró-dadwarih [KDB A d'twblyh] false judgement. īdron [dlwn' | N dariina] bow. *drón [dlwn' | N darūn] consecrated bread, ceremony in which c.b. is used.
PHD.txt:347:~išn: help, assistance. ~išnig: helpful. frāz [рге | M prz, N faraz] forth, focwarile ~ abgandan: throw forward. ~ 82: after, apart from. ~ bréhénidan: fashion forth, create. ~ griftan: undertake, perform; appoint, decide. ~ 6: up to.
PHD.txt:555:rabih [/pyh | M rbyh] noon, midday (heat). rad [/t! | N —] (spiritual) chief, master. АҺ: office of rad. rad [Pu | P rd, N ~] generous, liberal. ~ih: generosity, liberality. radag [itk! | M rdg, N rada] line, rank, row. radómand [/t?^wmnd] having a rad. rad-passag [/tps’k'] ceremonies of the gáhanbar festivals. radunay [/twny = Av. ratunaya-] one under the guidance of a rad. raftan, raw- [SGY TWN-tn! < А V sg’; lwb- | M rptn, rw-, N ~] go, move, proceed. ~išn, v. rawišn. raftār [/pt?] | N ~] goer. rag А! | M rg, N ~] vein. «ЛЬ: disposition, character. ray [/gy | P rg] quick, swift. ray [Pg | N —] meadow, plain. rah [/s, lh, [hy | M rh(y)] chariot, wagon. rah-, у. rastan. rah [Ps | M rh, N ~] road, way. rahag [/hk! | P rhg] = rag. rāh-dār [lsd] | N ~] brigand, highway robber. ~ih: brigandage. rahig [/syk!, Ikyk' | M rhyg, N rahi] child, page. ~ih: childhood. rāh-nimāy [Psnm?d | (M r’-hnmwd’r), № ~numa] guide. ram [Pm | М әт, N ~] peace; cal. 21st day. ram(ag) [/m(k') | P rm, N ram(a)] herd, flock. ráménidan, rāmēn- [Pmyn-ytn! | M ?myn-] give peace, pleasure. rāmišn [P min! | M rmyfn, N rāmi$] peace, ease, pleasure. ~ig [-vk! | N —z#] peaceful, at ease. ran [Рп! | N ~] thigh. P rān- [/^n-] fight. randidan, rand- [/nd-ytn! | N —] scratch, grate, abrade. rang [/ng | M rng, N —] colour, dye. ranj [Inc | P rnj, (M rnz), N ~] toil, trouble. ~ag [-k' | N —a] troubled. ranjénidan, ranjén- [/ncyn-ytn'] trouble.
PHD.txt:557:ranjwar [Incwl | (M rnzwr), N ranjūr] troubled, distressed. rapihwin [/pys-, Ipyt-pyn!, -wyn' = Av. rapiüfina-] the afternoon gah; south. ~tar [-tl] southern. rasan [/sn' | N ~] rope. rasénidan, rasén- [/syn-yin'] bring. rasidan, ras- [YHMTWN-tn' < А yhmtwn, V mt^; ls-ytn! | M rs-ydn, N ~] arrive, mature. raspig [Pspyk!] second officiating priest. rast [Pst! | M rst, N ~] true, straight, direct. ~ih: truth, rastaģ [lstk! | N rasta] series, row, progression; element, газап, rah- [Istn', Ї(?)А- | N ~] escape. rastarih [/st?/y%] escape. rasüg [/swk! | (N rāsū)] weasel. Rašn [/@! | M ri, N ~] god of Justice; cal. 18th day. ra&tan, *raz- [/ftn'] colour, dye. raw-, v. raftan. rawag [/wP^k! | N rawá] current. ~ih: currency. rawügenidan, rawagén- [/zob)hyn-ytn!] set in motion, propagate. rawénidan, rawén- [SGYTWNyn-ytn', v. raftan] cause to go, extend. rawišn [lwbin', SGYTWNsn', v. raftan | N rawif] going, motion. ^h : behaviour; as a suffix, forms abstract nouns. ray [Pd | M ry, N ra] postposition, for, for the sake of. rāyēnāģ [Pdym bi | M r’yn’g] arranger. rayénidan, rāyēn- [Pdyn-ytn! | M r'yn-ydn] lead, direct, arrange, organize. ~išn: action, function; arrangement. rāyēnīdārīh [/”*dynyt?lyh | M r!ynyd?ryh] direction, organization, rāyišn [”dsn'] order, arrangement. rāyomand [Pd^wmnd] rich, majestic. raz [/c, lz | N ~] vine; vineyard. raz [Pc | M Pz, N ~] secret, mystery. ~ig [-yk'] secret. rāz-kirrēģ [Pc kylwk' | M г qrwg] architect, builder. razm [/cm | M rzm, N —] battle. —--$àh [-g's | P -g’h, (M rzm?h), N ~] battlefield. razor [lcw] | M rzwr] forest. rédak [lytk' | N ~] lad, page. тёр [/yā! | N ~] sand. rëm [lym | M rym, N —] dirt, filth, purulence. réman [lymn' | M rymn, N ~] dirty, filthy, purulent. ^b : filth. 1r€§ []yf | N ~] wound, sore. *rēš [/yf | N —] beard.
PHD.txt:593:tan-bahr [żn'Þ’ hl] physique. tand [tnd | = P] faint, languishing. ~ih: faintness, langour. | tan-drust [tn'drw(y)st! | N ~] healthy, whole. ~ih: health. tang [ing | = M, N ~] narrow, tight. ~ih: narrowness; distress. tanig [tn'yk! | N tani] bodily, corporal. tanigard(ig) [tnykrt(yk)! | M inygyrd] corporeal. ` tanīhā [tn'y/? | M tnyP?, N tanha] alone. tanómand [tn wmnd | N ~] corporeal. “АҺ: corporeality. tan-tdhmag [tn'twhmk'] (sap) of plants. tanuk [tnwk! | N ~] thin, shallow, tanür [tnw] | M tnwr, N ~] oven. tar [LCDr! < A l-sd; tl | M tr] over, through, across. ~ kardan, ~ menidan: abuse, despise. -tar [-z# | (M -dr), N ~] suffix forming comparative adjectives. tar [2] | M гу] darkness. tarāzēnīdan, tarāzēn- [tcyn-ytn!] weigh. tarázüg [tPcwk! | (P tPzwg), N tarazü] balance, scales; astr. Libra. targ [tlg | N ~] helmet. tarģumān [tigm?n! | M trgwmn] interpreter. tarig/k [PIyk! | M гуур, N tárik!] dark. ~th: darkness. tarist [¢/st'] = tar. tar-mānīh [t/m’nyh] perversity. tar-menišn [tImynin! | N tarmanist] perverse; contemptuous. 7h : perversity; contempt. tarr [t/, LC Dr (in error, v. tar) | N —] moist, fresh. ~ag [tik! | N ~a] vegetable. tars [2/5 | M trs, N ~] fear, respect. tarság [ts k! | M trs’g, N tarsā] Christian. tarsāģāh [15(?)/?5] respectful, reverent. ~ih: respect, reverence. tarsidan, tars- [tls-ytn' | (M tyrs??dn), N ~] fear, be afraid. tarwénidan, tarwēn- [t/zvyn-ytn! | M trw-] overcome, conquer. tas [25 | N ~] die (for gaming). tasum [tswm | = M] fourth. tāšīdan, tāš- [O i-ytn!'] cut, cleave; create. taSkanag [tšknk!] under-shirt. tašt [tšt' | N ~] bowl. tāšt [021] *certainty. ~ig [-yk'] certain. tāwān [1?(d)w’n' | N ~] compensation, obligation. taxl [t?% | (M thr), P txl, N talx] bitter.
PHD.txt:607:~išn: conquest, destruction. wanigarih [4W BDN-, wny-klyh] waste. wany [A(W)BDN' < APbdn | M wny] lost, destroyed. wany(b)ūdīh [4WBDN'butyh, -YHWWNtyh | M wny(b)wdyh] destruction, ruination. iwar [wl | M wr, N bar] breast. *war [w/] lake. Zwar [wl] oath, ordeal. ‘war [wl] shelter, enclosure. war-, v. waridan. warāy [wl”g | J bry] crow. waran [win'] desire, lust. warān [wi’n'] ram. wārān [w’Pn' | M wrn, N bārān] rain. waranig [wlnyk'] greedy. ~ih: greed, lust. waranig [wL nyk! | N bārānī) rain(y). warāz [wl”c | N gurāz] boar. war-čašm [wicfm] with eye(s) in the breast. ward-, v. 'waštan. lwardag [witk! | M wrdg, N barda] captive, prisoner. ~ih: captivity. *warda$ [witk'] on heat (female animal). ~ih: heat. *wardānāģ (wi? mk! | N gardana] (roasting) spit. wardénidan, wardén- [wityn-ytn! | (N gardànidan)] cause to turn; change, alter. wardišn [witšn! | M wrdyšn, N дака] turning, change, metamorphosis. ~ig [-y%!] transient, changeable. ~(ig)ih : transience, mutability. wardyün [wltywn! | P wrdywn, N gardiin] vehicle, carriage, chariot. warg [wlg | N barg] leaf. wārīdan, wār- [w?l-ytn' | M w’r-yst, N bàáridan] rain. warišn [wilsn'] conduct, behaviour. lwarm [wlm | N barm] memory. — kardan: learn by heart, memorize. *warm [wim | N barm] pool, reservoir. wārom [w’lwm] mind. warómand [wl’wmnd] doubtful. ih: doubt. warr [LBWS Y A < A lbw?] wool; garment. warrag [КММА < ?; wlk! | M wrg, N barra] lamb, ram; astr. Aries. wars [wils] hair. lwarz [wle | M wrz, N barz] work, agriculture. *warz [wic | М wrc/z] miracle, miraculous power. *warz [wlz | N gurz] club, mace.
PHD.txt:653:~agig [-yk!] movable; intercalary (year). wihir- [whyl- | (M whwr-)] change. —išn: change. wimand [wymnd | = M] boundary, frontier, limit. ~ig, —6mand [-yk', 2wmnd] bounded, limited. *wiméhgén [wmyhkn! | M wymyh-] *shapely. wimustan [uwymwstn! | M wymrz- (< P)] spoil, destroy. win [wn'] vina, lute. wināh [zs | М zoyz)h, N gunàh] sin, crime. winahgar [wsk] | M wwhg’r, (N gunahhar)] sinner. ~ih: sinfulness. wināhīdan, wināh- [wn’s-ytn' | M wyn’h-] spoil, damage, destroy. ~išn: damage, destruction. winastag [wnstk'] spoilt, corrupt. windādan, wind- [HŠKHWN-tn' < А ME, V skh; wnd'tn! | M wynd'd, wynd-} find, obtain, acquire. ~išn: acquisition, earnings. ~ignig : findable. winjišk [zvxcšk! | N gunjišk, binjišk] sparrow. win(n)ārdan, win(n)àr- [wyx?7-tn' | M wyn’r-dn] order, fix, arrange. ~išn: arrangement. win(n)irdan [wynltn' | M wynyrdn) be arranged, established; stay. iwir [wyl | M wyyr] man, hero. *wir [wyl | M wyr-, N bir] memory, mind. *wir [wyl | N bir] thunderbolt. wirāstan, wirāy-, (P wirāz-) [wyl’stn', wyPd-, (wPc-) | M турі, tyr y-, (P wyr st, wyr!z-)] arrange, prepare, cultivate, restore. —jišn(ih): arrangement, preparation. wirég [wlyk! | N guréy] flight, escape. wiréxtan, wiréz- [OL YKWN-tn! < А У ‘rq; wlyhtn', wlyc- | P wryxt, N guréxtan, guréz-] flee, escape. wirdmandih [wy”wmndyh | M wyrwmndyy] memory. wirózag [*wiwck! | (P wrwe)] lightning. wis [wys | = M] village. wisandan, wisān- [ws’n-dn'] separate. —išn(ih): separation. wisay- (ws'd- | M wys’y-] rest. wisbed [wyspt! | M wysbyd] village headman. wisé [wsydy | (P wsyd), N gusë] despatch. ~ kardan: send, despatch. wisistan, wisin(n)- [wsstn', wsyn- | N gusistan, (gusil-)] break, split. wisp [wsp | M wysp] all, every. wispurdan, *wispar- [wspwltn'] tread, trample. wist [20; wyst! | = M, N bist] twenty. wistan, *wih- [SDYTWN-tn' < A V šdh; wstn'] shoot, throw. wistar(ag) [wsti(g) | N bistar] bedding, cover.
PHD.txt:843:arrange arastan, payrastan, rayén- idan, win(n)ardan, wirāstan.
PHD.txt:919:balance tarāzūg.
PHD.txt:1031:boar warāz.
PHD.txt:1094:brightness, brilliance Һат, brāzišn, frog, payrég, spig.
PHD.txt:1111:builder rāz-kirrēg.
PHD.txt:1436:create af(u)ridan, (frāz) brēhēnīdan, dādan, tāšīdan; (daevic) kirrén- idan.
PHD.txt:1747:element āmēzišn, rastag, záhag.
PHD.txt:1798:escape (v.) rastan, wiréxtan.
PHD.txt:2108:gleam brāzidan.
PHD.txt:2619:lift abrastan.
PHD.txt:2657:long дарт, dagrand, drāz.
PHD.txt:2883:mystery rāz.
PHD.txt:3090:perform frāz griftan,kardan,wizārdan.
PHD.txt:3242:progression rastag; wihëz(ag).
PHD.txt:3315:radiance brāzīšn; v. brilliance.
PHD.txt:3316:radiant brāzišnīg.
PHD.txt:3416:restore wirastan.
PHD.txt:3482:row radag, rastag.
PHD.txt:3525:scales tarāzūg.
PHD.txt:3588:series rastag.
```


## [2026-09-14T01:12:15.032Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== NYB leaf 175 (p167)\"; awk 'BEGIN{RS=\"\\f\"} NR==176' NYB_vol2_glossary.txt | head -60",
 "description": "Nyberg p.167"
}
```


### [2026-09-14T01:12:16.127Z] TOOL RESULT

```
=== NYB leaf 175 (p167)
. the preceding w. Parallel with the series pattāt, pattūk (v. this w.), pattān is the series with the prev. *ati-: *attāk < *ati-tävaka-, Arm. lw. atak ‘capable’: attūk < *ati-tuvaka- id.: attān < "ati- tāvana- ‘solvent’ (attānīk DkM 139—140, opp. an-attān 'insolvent'). Cf Bthl., MirM III, 15, ZsR III, 53. — Cf ham-tak, tāhēkār, tāk, tāyītan, tuvān.
pat-tanómand [PWN tn’wmnd] corporeal, endowed with a body 34?9. — V. s. v ?pat A II, 11.
pattük [ptwk'] capable of 55%. — V. s. v. pattàn.
pat-uzvinčh [p’t’wzw’nyh] control of one’s own tongue 7111. — V. pätan and UZVvān.
patvac- [ptw’c-] pres. to answer 73121, — pati + Av. (1330 sqq.) !vak-; MPrth pdw’c-; MPrs pyw’c- (BBB), certainly borrowed from NW, as vac- belongs al- most exclusively to the NW area; Paz. padvāžed.
patvand [ptwnd] relationship, kindred, parentage, descent: pat ~ through affini-
159
payam-
ty 10418, because of family ties 117? (in-
sert PWN = pat before ~); ~ rdyénitan to form family connections 6319; ~ kar- tan id. (apäk with) 706; ~ u tohm extrac- tion, descent 625. 632; descendants 63%; ~ u tóhmak % vazurg high lineage 72*; ~ cas. rect. pl. offspring 941°. - MPrs pywn = paivann; Paz. paévand; NP paivand. From patvastan.
patvastak [ptwstk'] continually, regu- larly 51; subsequently 1111.
patvastan patvand-, to bind, to attach, to join: Tir patvast 7'-® meaning not clear: (joined to [the planet] Tir =) be- ing in conjunction with it (?); han hom andar hàn draxt bà patvast this haoma was attached to this tree 4015; cë rād ka mē- noyan u gētīkān dāntšn u kār-ākāhēh har 2 band 6 to patvast? 8811-1? (v. s. v. band); 12017-18, — < pati + band-, v. bastan; MPrs. pywst; Paz. paé- vastan; NP pai- vastan.
patvast-ax"éh [ptwst' ’hwyh] the quality of having united minds, concord, unanim- ity 10615. — V.s. v. ax".
Pät-xösröi [p'thwslwd'] n. pr. 2214. 239. 24°. — Called the brother of Vištasp; the name could mean ‘Protector (pdt < pātā nom. of *pätar-, v. pātan) is Khosroi'; Justi NB 246a, thought it meant ‘instead of, counterpart of Kh,’. Possibly, however, it is only one of the numerous Iraniza- tions of the name Nebuchadnezzar, v.s. v. Baxt — xósro.
patx"ar [pthwl] *pasture 42??. — < *pati- gugra-, v. xtartan and ef àx*ar.
paty'ak (inser.) [pty?k] = paitäk, q. v.
*päyam- [*p’ym-] pres. "to consume: frac ... pat gah *pāyamēš(y) (opt.) thou shalt *consume it (the roasted meat) on the spot 44” (divine order), cf the con- tinuation 1. 9-10: apt-š etön kart; cigon x"art druyist būt thus she did; as soon as she had eaten she got well again. — Read- ing and meaning hypothetical. I think it
www .parsianjoman.org | col ak,
payam-
160
péróz-kar
must go back to *pati-yam- ‘to take hold of’, from Av. (1262sg.) yam-, chiefly with preverbs. I find *pāyam as a v. n. in two passages: 1. DkM 285 aköman ... menisn päyam ‘A. holding Mind in his grasp’; 2. ibd. 501? páyam hešm andar ménisn “Wrath taking Mind in his grasp’ (?). — Zsprm VIII, 4 has a somewhat divergent, perhaps more original version of the story 441-9: ^L ZLWN ‘L y’twk’n, MH-t L>? HWH-nd byšznyt'l, BR’ L'WHL ‘L h'nk' ZLWN, YDH BYN ml PWN "MŠH' ZY TWR’ ZY MDM thé YDLWN-t', hysme bwd wt'p' PWN NPSH-tn' zhk' MNW-t PWN 'škmb'
```


## [2026-09-14T01:12:24.848Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==180' NYB_vol2_glossary.txt | head -40; echo \"########\"; grep -n \"rāz\\|rastan\\|rah-\" NYB_vol2_glossary.txt | head -30",
 "description": "Nyberg page 167 and grep"
}
```


### [2026-09-14T01:12:26.008Z] TOOL RESULT

```
f cattle’.
purr-kamakčh [pwl k’mkyh] the quality of being purr-kämak having his will wholly directed to (6) 555. — V. kāmak.
purr-marg, -ēh; purr-nérók; purr-névak, -éh; purr-avarrah, -ēh; purr-xratéh: v. s. v. purr.
pursišn [pwrsšn'] question 1315. 1055-19. 1119-5; as a det. v. n. —-ēh: pat den —-Eh in order to put questions about Religion 10838.
pursitan [pwrsytn'] to ask, followed by ku introducing direct speech 3? and passim; with a dir. obj.: to consult 481%. 6371; to ask a p. : o 68—88 passim, elsewhere hac; — about: apar 4814-25, 4912, or pat 1615; — frašn, or saxtan ~ hac to ask a question, questions 2114-15, 742.6-7, 766; with a rel. pron. as its dir. obj. 76%, 1055.9; — 6 ham ~ to deliberate 577, cf hampursitan; hakanén ham pursénd thev will converse, communicate with each other 1061-18. — Av. (997 sqq.) fras-, pres. parasa-, OP frad-, pres. p(a)rsa- (Kent); MPrth pwrs’dn pwrs-; MPrs pwrsydn pwrs; Paz. NP pursidan.
pus [BRH; pws 2218. 2615, 277] son, cas. rect. and cas. obl., passim; secondary cas. obl. pusar [BRH-1] 5115.21.24, 523.9; pl. cas. obl. pusän (BRH-'n'] 188, sec- ondary form pusarän [pwsPn'] in the enumeration apāk pusarān brätarän (ete.) 185, 21°. 241-5. — < OP puca-, SW form of pudra- (v. ‘puhr); MPrs pws (cas. rect.), pwsr (cas. obl.). — pusar is modelled on the pattern of pttar, brätar, mātar, duxtar; NP pus (old), pusar; modern pisar influenced by pidar.
pus-kämak [BRH k'mk'] loving her son 4821, 497.21, 501, '
11*
163
Pütik
pušt [pwšt'; Ps. pwšty] the back 1112. 2521. 29%. 6513. 1287; pat ~ tacitan to run after, to pursue 311%; pat ~ bütan to protect, to be the protector 31°; ~ kartan 6 to protect 872%; — pl. eas. obl. ~-dn: pat puštān i Vištāspān for the (acts of) protection of the Vistasp dynasty 9514. — MPrs pws, NP pušt < *pršti-; Av. (878) paršta-, parsti-, v. s. v. puštēpān.
*pušt-aspān [pwSt’sp’n'] 1118, v. next w.
puštēpān [pwštyp'n'] “protector of the back" = life-guards, pl. cas. obl. in ~-an sardär the commander of the life-guards 11911, — pušče cas. obl. of pušt (g. v.) + pan; the Sass. title is transcribed in Arm by p‘ustipanac (gen. pl.) (or p*usti- pan) satar ; besides, Arm has the Prth. lw. pašt-pan “protector, defender’ < *parésti- päna- (v.s. v. pušt); NP pustibän, pustvän. — pušt-aspān 1118 is an old misreading (Paz. pustaspän Mx) of pustepän, cer- tainly due to wrong association with asp ‘horse’, as is suggested by the spelling pwšt'sp'n'; moreover, in the BP writing the ligature -yp- is very often formed so as to coincide with -sp-. Read conse- quently 1118 puštēpān sardär = the Arm. form just quoted.
puštčpinakčh protection, defence 8514. — Paz. puštaspānī, v. above.
pūt [*pwt'] putrid matter 76%, — MS pwn, but Paz. pid, Skr. v. durgandhi; Av. (909) pūti- *putrescence'.
pūtakēh [pwtkyh] decom
########
482:awāž-sār ‘headstrong, rebellious, abstr. awāž-sārī SGV XI, 247-249, < apāc (1) + sār < Av. (1572) sära- = sarah- in compounds. Cf nigne-sär.
590:api-sar [pysl] crown 6%. — MPrs ’bysr (S); NP afsar. Probably < Olr *upa-sarah- ‘that which is on the head’ (v. sar) > *apa-sara- and then remodelled to "api- sara- with variable accent: *api-sara- > apisar, *ápi-sara- > *apsar > afsar.
790:*ā-vēnišn [Pwynšn'] the act of blaming, disgracing a p:: vattarün ~ kartan to disgrace evil people 71%, opp. vehän pat pātdāšin (v.s. v. pat I:II) kartan to reward good people; — [kë an-tškēhtar ? han ke ~ i martömän vattar sahet ku niyäzömandeh who, is (the most not- poor =) the least affected by poverty? he who considers being blamed by men worse than being needy PT 95!-?; when a man makes his confession, hàn ke peš patit bavet (i.e. the priest-confessor) aš xup niyösisn, [MN-š for] api-§ ne ~ [MN-& for] api-$ rüz be ne barišn, ce ka pat vinčis i kart be āvēnēt aivāp rāz bē barét a�� havand bavet shall listen bene- volently (to the man confessing his sin), and he shall not disgrace him, nor divulge his secret, for if he disgraces him for the sin he has committed, or divulges his secret, he becomes equal to him Šnš 8: 9, p. 107, Cod. K 20 fol. 67 r.]. - Paz. avinesn
1013:bwdyst’n ; Arm. lw. burastan ; MPrs bwyst’n Paz. bēstg; NP böstän, from bod (2).
1018:brah [bl’h] splendour, beauty 1419. 1516, 9425, 11121, 1124-19, — SW form of Av. (972) brāz- bräza-; MPrthPrs br’z, br’2’g, br*2yšn; Paz. bräzinidär, brih(ī) (SGV); NP baräz and baräh.
1130:-cihrak [cyhlk'] = cihr used as the last element of an adj. compound, v. dp-~, damik-~, gospand-—, mart6m-~,urvar-~. Cihrāzātān [cyhl’c’t’n'] patron. 116". — From n. pr. C?hrāzāt, ci āzāt.
1329:drāhītan [dl’hytn'] to shout (with a voice resembling the neighing of a horse) 58%. — Skr hräd- ‘to sound, to ring’, whence Av. *zrdd- and OP *drdd-, which devel- oped in SW to dräy- or drah-; hence dra? (g. v.). Thus drahitan is ultimately iden- tical with dräyitan (g. v.).
1446:VII, 1934, 265-274; Nyberg, Rel., v. Index. Eran-x"arrah-kart-Sahpuhr [-GDH- =
1447:z"arrah added by Markwart] ‘“Shapur has made glorious Eran" 116?? is according to Markwart the official name of the town called in Syriac Karka d-Ledän and by Tabari Īrān-xurrah-Sābūr, in the neighbourhood of Susa (Cat. 97. 98).
1634:of Vardzak, v. varāz and Varāzān. Cat. 61.
2902:pairästak [pdl'stk'] ready-made 6°. — Arm lw. patrast; NP vb. patrāstan patrāy-; < pati + Av. (1520) räd- ‘to get ready’ (Skr rddh-). The prev. pat-, generally preserved in the archaistic BP orthogra- phy, is here written phonetically in the genuine SW form pai-. Through mutual exchange MPrth. and MPrs have got one common vb. pdr’stn pdr’y-: Verbum 187, Ghilain 60. There has been some con- fusion between old räd- and old räz-, SW rüd-, but there is no necessity for deriv- ing pairästan from räz- as does Hen- ning. V. the following ws. and cf ärästan, virastan.
3263:rastan [Istn'] rah- to escape: hac dósax" ~ 85°13; the pres. has pass. form: hac band rahihēt [lhyhyt'] 341, bē rahiyét [Ihydyt'] 9822 will get loose from his fetters. — NP rastan rah- both trans. 'to let go’ and intrans. ‘to escape’; similarly Av. (1517 sg.) rah- ‘to apostatize' and ���to seduce into apostasy’. As for rahiyét cf s.v. apasthistan.
3374:sahm [shm] terror 9!. — NP sah(1m; MPrs adj. shmyn ‘terrible, dreadful’; from OP "cahma, nom. of "cahman-, SW form of *Oürah-man-, from Av. (802 sqq.) 0rah-, v. tarsitan.
3395:sar [sl; LYŠH] 1. the head of the body, passim. — 2. the chief: —-xtatäi (g. v.) the supreme sovereign. — 3. kofe ~ 20, kof ~ 24—25. 27. 29 passim: the mountain peak; ~ i cäh the kerbstone of the well 1415, 154. — 4. beginning 711°. 8818. 988. 99°; 3821 and 39? v. aibigatik and anatbi- gatik. — Av. (1565) sarah-; MPrthPrs sr; Paz. NP sar. Cf also apdc-sdréh, nignesär.
3727:191 tarāzūk
3756:instead of kē-mān haciš "we for whom’).-OAr *tras-, *tars-: Av. (802 sqq.) . Orah-, pres. tarasa-; OP pres. trsa-; MPrt Prs tyrs-; Paz. NP tarsidan; v. also sahm.
3947:iyar [wl] breast 108%. — Av. (1365) varah-; MPrs wr (A-H I); Paz. var; NP bar.
3954:varäz [wl’c'] boar; hero 225-9, 26%, — Av. (1366) vardza-; KZŠPrth 1. 23. 25 wrc = Prs, Gr. v. Topat, Tovupat; NP gurāz; cf Gardzak.
4157:vinäristan [wyn'lstn'], vinärtan [wyn’ltn'] pres.: read vindrénd 106%? for virdyénd, to put in order, to arrange, to array, to organize 13?(-2stan)??(-rtam). 85”. 86% (-rt). — MPrth wyn’r’d, wyn'r- (MHC); MPrs wyn'rdn w(y)n’r-; Paz. vinardan, vinärastan, Bailey, JRAS 1953, 106; Henning, TPhS 1954, 175 n. 1. Pass. v. above
4177:virästan [wyl'stn'] vērāy- [wyl’d-] to prepare, to arrange, to adorn: apāc ~ to restore, to renew 711%; pt. viräst well executed 12027; — 10622 read with the MSS vīnārēnd instead of virdyénd. — Av. (1514) raz- and (1520) rad- have inter- mingled in SW where raz- > rad-. MPrth wyr sin wyrz- (S, A-H III), cf viräz-; MPrs wyr’stn wyry-, cf Arm. lw. varsa- viray ‘hair-dresser’ (DkM 7573 wlswyl'd); Ps. wyl’sty, wyl’d-, cf ärastan, patrčistak, räyenitan. Verbum 187; Ghilain 52. 69.
4178:Viraz [wyl’c'] n. pr. 107. — Av. (1454) Vīrāz-, more correct Virdza-. In BP traditionally read Vīrāf, which is now generally regarded as a misreading; de- fended by de Menasce, JA 237, 1949, 3—6.
4562:zor [zwl, Ps. zwly; erroneously zwhl] strength, power, vigour 14. 158.15. 897, 10678; zwhl (v. zöhr) for zor 9415; as to 128’, v.s. v. täyitan. - MPrs zwr, the SW form corresponding to NW zavar (q. v.); NP zör, which in later pronunciation coincided with zur ‘lie’, OP zürah- ‘deceit’, züra-kara- ‘evil-doer’. — The orthographical confusion of zör with zöhr is very frequent.
4570:zréh [zlyh], zré [zlyd] armour, harness 69, 2013-14, 8515, 12027, — Arm. lw. zrah-k‘; Syr. lw. zardä ‘coat of mail’, Talm zrd’, Telegdi 243, Arab. lw. zarad-; Paz. z(a)reh ; NP zirih, zarah: all these forms presup- pose *zrdda- and do not tally with Av. (1703) zrača- (Vd. 14? without variant; Phl. Vd. has zrāt evidently through the influence of the Av. form). Some im- portance should perhaps be attached to the curious gen. zaradvehe (1703) quoted from a fragment preserved in the Phl Vd. — NP zirih, Paz. zreh perhaps < cas. obl. *zrdóe.
5018:zürah- = 5 x : ZOr zūra-kāra :
5294:rah-: rastan
5310:raz-, rad-: virastan
5326:sarah-: sar
5392:tap-, tapa-, tapaya-: taftan (vi-)tar-: vitartan tarasca: turist tarsna-: tisnak taro: !tar, turist taš-: tašitan tašta-: tašt taOra-: tārīk taOrya-: tàrik tauruna-: tarr tav-: tuvan (pati-)!tav-: pattài, pattàn tavah-: stob tiyri-: tigr | Tird.nakaOwa-: Tir Tištrya-: Tistr tiži-: tēž tkaēša-: kēš tõi, to: -t türa-: Tur Tusa-: Tiis tušni-: tušn (fra)-Oang-: frahaxtan Oračtaona-: Fréton Orah-: sahm Orah-, terosa-: tarsitan Orisant-: !sih Orišva-: srišvātak Orita-: Srit Orita-: Oritak Oritya-: sitikar Owa-: to Owaxš-: tuxšitan
5423:var-: varan varah-: !var varana-, varona-: varan varaza-: varaz varocah-: vare vareda-: gul varoka-: varg Varo0rayna-: Varhran väroma-: várom varosa-: vars varot-: vastan ?varota-: vartak varoz-: varzitan varoza-: lvarz vari-: ?var
5749:wxybyh, -byy: x¥és wyg'h, -hyft: gukāi w(y)g'nyšn: gukān wys’r-: apa-sartan wyr'štn, wyr'z-: virastan wyst’f: vistaxu
```


## [2026-09-14T01:12:35.458Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"leaf of 3263:\"; head -3263 NYB_vol2_glossary.txt | tr -cd '\\f' | wc -c; echo \"---context---\"; sed -n '3255,3270p' NYB_vol2_glossary.txt",
 "description": "Locate Nyberg rastan page"
}
```


### [2026-09-14T01:12:35.533Z] TOOL RESULT

```
leaf of 3263:
184
---context---
167
Rašn
. rasend the souls of the Righteous reach salvation 8825-26, — SW only: OP pres. rasa- from ar- ‘to move, to go or come toward’ (Av. [183] !ar-);; MPrs. rsydn; Paz. NP rasidan.
rast [Pst'] right, righteous, true, fair; subst. the truth; epithet of Rašn (q. v.); vimand ~ nimūt indicated the boundary justly 4510-11; the balance ~ dārēt gives the accurate weight 7274; kē-š kirpak u vinds hakanén ~ whose virtue and sin weigh equally 79%; han ké-§ har 2 ~ are equal 937°, — MPrth rst (S, A-H III); MPrs r’st (A-H II, BBB); Ps. Psty; Paz. NP räst; Verbum 187; Ghilain 69.
rasteh, raste [l’sty 9213] righteousness, fairness, truthfulness, truth 66%. 7015-19 etc.; passim. — MPrs r'styh, r'styy; Paz. NP rasti; MPrth r’ätyft.
rast-gobišn [~ gwbšn'] whose speech is true, is the truth 68°.
rastiha [~-yh’] adv.: uzvàn ~ dästan to keep one’s tongue to the truth 641%; ~ baxtan to distribute justly, equitably 7914,
rastak [lstk'] free 91?, from
rastan [Istn'] rah- to escape: hac dósax" ~ 85°13; the pres. has pass. form: hac band rahihēt [lhyhyt'] 341, bē rahiyét [Ihydyt'] 9822 will get loose from his fetters. — NP rastan rah- both trans. 'to let go’ and intrans. ‘to escape’; similarly Av. (1517 sg.) rah- ‘to apostatize' and ���to seduce into apostasy’. As for rahiyét cf s.v. apasthistan.
rastar one who escapes: ~ kartan to bring about an escape, to rescue, to deliver 1135-6, — NP rastär.
Räst-Sähpuhr [Pstšhpwhry] a town in Eastern Iran P2:2. — ‘Righteous Sh.’
Rašn [lšn'] the god of Justice: ~ 4 räst 7218, 74%, — Av. (1516 sq.) rasnu- ‘just’, also the name of the god.
www.parsianjoman.org | col wok
Rašn-cin
Rašn-cin [~ cyn!] the epithet of a brother of Yam 1015 (his name was Narsahé, BdA p. 2288; it was his brother Spetvar, Av. Spityura- who, in alliance with Dahäk, i.e. Aždahāk, killed Yam by sawing him in two, Yt. 1946, BdA 1.c. 1. 12). — *Decid- ing righteously’, cf citan; Av. rasnu-, v. the preceding w.
rat [lt'] "genius", divinity or tutelary spirit presiding over one of the categories or classes into which all beings and things of the good creation are divided: ap?-Sün ~ Gēpet and their genius is G. 8674-25; Zartuxšt is ašūkān ~ the genius of (all) the Righteous 106!; he is in Avestan terminology the ahü and ratu of the world, hence the abstr. ahü-u-ratü-eh 4 gēhān 55%. — Av. (1498 sqq.) ?ratu-; NP rad ‘intelligent, learnd', ‘a high priest of the Magi'. As to the doctrine, v. Modi, Ceremonies 330—334.
```


## [2026-09-14T01:12:36.996Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==831 || NR==832' BRT.txt | grep -n \"rah\" | head -20; echo \"=== print leaf 831\"; awk 'BEGIN{RS=\"\\f\"} NR==831' BRT.txt | tail -30",
 "description": "Bartholomae col 1517 Av rah-"
}
```


### [2026-09-14T01:12:38.207Z] TOOL RESULT

```
6:•  g.,  j.  rah-  V.  'abtrünnig  sein;  —  machen'. Praes.  29  ransya-'^,  30  (Kaus.)  rJw- haya-.        Vgl.  ränla-.
11:•  j.,  g.  rä-  V.  'gewähren;  gönnen'.  PcrC  i rar-;  r-Aor.  i  rah-.  —  PPfP.  rata-.
56:was  besser  ist  als  gut  Jedem  verschafit, der  seinen  Willen  erfüllt,  AhM.'^  Y.  51. 6*>;  —  tsi  varäi  (sd.)  räduntl  ahurahyJ ^■33-  2-
=== print leaf 831
  Mx. /.  118  ff.    S.  JN.  GlrPb.  3.  64a.
Zum  V.  rac:  —  inp.  (Pü.)  rafii.
•  j.  rasnä-  £  'Richtigkeif  (?):  pfnse  "hwam 'Inya  (IS.)  u^ahe  Yt  72.  i.   Geringe  Stelle.
Zum  V.  rat:
•  '].''va^vaXa;mca paUi.aoxta  sara%ustra .." Vyt.  70.
•  g.,  j.  rah-  V.  'abtrünnig  sein;  —  machen'. Praes.  29  ransya-'^,  30  (Kaus.)  rJw- haya-.        Vgl.  ränla-.
1)  'abtrünnig,  abgefallen  sein  von  — ' (Abi),  in  religiöser  Hinsicht:  akmat *mainySus  rän^äntJ  dngvaniS  masää spintat  nSii  ßj  *a^aonö  "von  diesem heiligem  Geist  sind  die  ZJn^enossen abgefallen,  o  M.,  nicht  so  die  A^a- anhänger"  Y.47.4;  —  nyämB  daivayazB ta/an  *aoi^?urvayan  fha  rärpsyantB Yt7i.6(?).  a)  'jemanden  (Alck.)  ab- trünnig, abspenstig  machen,  zum  Abfall verführen  von  -'  (Abi.),  in  religiöser  Hin- sicht: yä  ranhaym  sravaaha  vahistät ^ao%anat  mantanB  oHhyB  (Sp.  7  u.)  .  . "weil  sie  durch  ihre  Lehre  die  Menschen
rata-  1518
vom  besten  Tun  abspenstig  machen,  so  . ." Y.jz.ia;  —  tail{l..yBi  vakÜmt  *a/aon3 mtuäa  ränsyqn  mananhs  ",  .  indem  sie, o  M.,  die  ,<i&3nhänger  von  dem  besten Sinn  abspenstig  machen"  Y.j2. 11.
Vgl  tärfla:  ~  Pü.  (lu  Y.  J3.  II,  4/)t  räCik rtienhid  ~  SÜ.;  Jaifinäm  chindanti  -;  (la  Y. SJ.m):  ki  rn  sräy^  '.  .  ,  (iti  Yt  //)i  -  ?- rStf.  —  ■)  rätisy'  könnte  für  räriiy'  ge- schrieben sein  (IFAni.  4.  12);  aber  ränlä  - das  nicht  etwa,  für  *rär>tfd  geicbriebeDi  als NS.  ans  ränfyaiü'  genommen  werden  kann, da  das  gAw.  solche  NS.  nicht  kennt;  s. LiCHTBKBECK  KZ.  33.  iSo  -  spricht  dagegen. Also  ist  rSni'  wie  väur'  (s.  'vor-)  lu  be- arteilen.
•  j.,  g.  rä-  V.  'gewähren;  gönnen'.  PcrC  i rar-;  r-Aor.  i  rah-.  —  PPfP.  rata-.
Nur  Med.  1) 'gewähren,  spenden',  insbes. 'als  Opfer  weihen':  abyö  ratäbyB  sad^räbyB arhixhaeiiyasca  vaynbyff  .  .  mainyaom yatatftn    yazamaide    Y.iß.t.  2)    'Je-
mandem (Dat)  etwas  (Akk.)  gönnen': T/aAisfym . .  yäsä  (sd.)  väunuJ" (Sp.  1353  o.) .  .f>ralaeärai  maibyaca  yaiibyascS  It  rätf haishBt  (aSKAorM.)  vJspai  yavl  vaahSui manat?hs  (Sp.  1128  o.)  "um  das  Beste bitte  ich . .  und  wem  sonst  du  es  gönnen wirst  für  alle  Zeit,  (das  beste  Gut)  des guten  Sinns"  V.  28.  8.  Aus  dem  Zu- sammenhang gerissen:  *raire^^  (3SPfM.) F.  77.
mit  /rä  I )  dnwS.  i ,  mit  Dat.  der  Person undAkk.derSache:/;'r5  i'7r.7^r(iSAorM.) amfla  spmtä  yastomcä  vaAmiiiüä  fträ mana^hä  ftra^  .  .  fira  tanvas^lt  sfahyä uslamm  Y.//.  18''.  a)  dnwS.  2:  fira manyaHbyS  (sd.,  Ntr.)  raahl  (iSKAorM.) vasS.yäiam  vasS.hitm  Y.  72. 3,
ai.  rari,  räialt  (Ko.),  räläh.  —  Pü.  (dRn.):  fa ilän  rätenit  —  SD.:  Jaipaii^SaiA  -  tSAr;  IIa 5!äH  .  .  rät  c  -  SB.;  daksinVihcaia -;  rät;  (mit frä):  fräl  S  !mäi  rälinem  -  Sü.i  früifi/am daifmayämi,  iiia  dakiäfikaromi  -  ;  fräc  . .  rät int  -  Sa. ;  frai^f/am  .  .  daifiniihaliämL  — ■)  Hds.  raire;  i.  "narrt,  ^nar-  No.  lt.  —  «)  Y. T3.  4  Stellt  an  ähnlicher  Stelle  in  ähnlichem Sinn  fairi  .  .  daiqmi.  S.  übrigen*  Y.  33.  14, dB,s  an  beiden  Stellen  benntit  ist
•  j.  ratu!  "räuininam  d^ranam  srava- nanamca  pasu.vastranamia  N.^:  —  ?— .
VL:  fehlt
•  j.  räjay-  ro.  'Reihe' (?):  'fim  F.ij. Bed.  nach  np.  rata  'Reihe',   woiu  HBM.  PSt. 66.  —  PQ.:  rdda.
•  j.,  g.  rata-  Adj.  (fem.  •«-),  PPfP.: s.  rä:
dby  Google
ISI9
'lätay-
■räd-
1520
•  i^  g.  'rätay- :  raiti-  i)  Adj.  'dienstwillig;  \ Diener,  Gehilfe' :  mßiryin .  .yaihe  aita  *tayB  l ..  spass  ätfhsire  Yt  10.  45.  i)  f.  'Dienst, Dienstwilligkeitj  Pflichterfüllung':  aAurit  na na  avarS  (sd.)  shmä  (3p.  270  o.)  °töis. yüsmävalqm  ".  .:  so  wollen  wir  bereit sein  euresgleichen  zu  dienen"  Y.  2g. ' 11".  a)  bes.  in  religiöser  Hinsicht:  avis\ nä  antan  hSntü  mmaifaitji  ctärä  '/ayS' "oflfenkundig  sollen  unter  uns  werden  die deutlichen  ehrerbietigen  Pflichterfüllungen" ^•33-  7")  *'*•  P- J^  ™''  der  Ausführung:  [ tä  ävifj'ä  °tayg^^  antar?  *afm^sca  sp?nts iaoiyantas^a  fräräUllca  *vldlsäs(sd.)ca arttan  *^3dainäif  asaonis  "die  sollen offenkundig  werden  die  Pflichterfdllungen zwischen  den  ASp.  und  den  Sao^y.  und , die  Freigebigkeit  und  Mildtätigkeit  zwischen  I den  rechtgläubigen  Retigionsgenossen"  P. ^■,  — yäti  catica  . .  dahmS  aiava  *kaurvh *'itl^''''  dähaj  a0i  dim  aiwyäiH  yä dahma  vatshi  äfritis  "so  oft  ein  recht- gläubiger Gemeinder  seine  religiösen  Pflich- ten völlig  erfüllt,  .  ."  P.ja.
KompA.p).
```


## [2026-09-14T01:12:53.461Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"apostat\\|ranhaya\\|rah-'\\|YAv. rah\" CHEUNG.txt | head -20; echo \"=== index rah\"; grep -n \"^rah\\|rah-, \" CHEUNG.txt | head -20",
 "description": "Cheung on Av rah-"
}
```


### [2026-09-14T01:12:53.533Z] TOOL RESULT

```
9890:*AVESTAN: ras- (rāņh-) ‘to be disloyal, (?) apostatize’, YAv. ranha- ‘epileptic’ (Yt 
23900:*PARTHIAN: ‘st’w- ‘to praise’ || (+ *apa-) ’byst’w- ‘to deny, apostate’ || (+ *pati-) 
=== index rah
16175:9 The root *kars- appears to have a rare variant *xrah-, with a different kind of 
41373:rastan/rah-, 140, 322 
43475:rahoya/rah-, 322 
51828:rah, 323 
51829:rahas-, 323
```


## [2026-09-14T01:12:55.226Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== POK rahati/regh/redh\"; grep -n \"rahati\\|reĝh\\|reg^h\\|redh-\\|reĝh-\" POK_full.txt | head -30",
 "description": "Grep Pokorny"
}
```


### [2026-09-14T01:12:55.299Z] TOOL RESULT

```
=== POK rahati/regh/redh
20657:Czech drazitr make a rabbet or a furrow, hollow out '; perhaps also Czech z-drahati se 
20774:alb. drefh {stem *dredh-), Aor. drodha^ turn round, turn together, twine, spin ', alb.-
```


## [2026-09-14T01:12:59.262Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '9875,9935p' CHEUNG.txt",
 "description": "Read Cheung root with Av ras-/rāṇh-"
}
```


### [2026-09-14T01:12:59.316Z] TOOL RESULT

```
for babies’, Wa. rowj ‘teat, comforter made of horn’ || (+ *apa-) Sh. birew-/birewd, 
birud ‘to wean a child’ || (+ *?) ? Yi. fšüv-/fšuvd ‘to suck’ ("*upa-sap-", IIFL, l.c.) 

9 On the IE origin of Ir. *hrab see EVP: 65. 

«PIE *sreb'- ‘to sip, gulp, suck (in) = LIV: 588 | Pok.: 1001 

*IE COGNATES: Hitt. /sarapi/ ‘sips’, Gr. рофёо, Lat. sorbed, Lith. srebiù (srébti) ‘I 
slurp, gulp down’, Arm. arbi ‘I drank’, etc. 

*REFERENCES: IIFL II: 253a, 209b; EVS: 69b, 116a, 20b; Steblin-Kamenskij 1999: 297; NEVP: 71 


*(h)rah ? ‘to fall off, leave, let go, escape, reject ?’ 

*AVESTAN: ras- (rāņh-) ‘to be disloyal, (?) apostatize’, YAv. ranha- ‘epileptic’ (Yt 
5.93) = Liste: 57 

Pres. them. red. ia-: IND. 3р1. OAv. rārəšiieiņtī (Y 47.3), SUBJ. 3р1. OAv. rarasiian (Y 32.11); Partic.: 
pres. Y Av. rärosiiant- (Yt 11.6), intens. OAv. rárosa- (Y 49.2); Caus.: INJ. 3р1. OAv. rághaiion (Y 32.12) 


*NWIR: ? Kurd. (Kurm.) rehandin/rehin- ‘to reproach, decline, reject’, (Sor.) ret 
‘rejection’ 

*SANSKRIT: srams ‘to fall off, asunder, to pieces; to get loose from, loosen’ (KS, 
MS+) = EWAia II: 783 

© The evidence for this root consists of Av. attestations, whose meaning is not 
entirely certain.. The Pers. forms that Nyberg II: 167b cites in support, MMP rh-, 
BMP Ih- /rah-/ ‘to escape’, NP rastan/rah- ‘to be delivered, saved, escape’, may 
rather go back to *rHaz. On the other hand, the Kurd. forms may be included (?). No 
IE etymology can be cited for this Пг. root. 

*PIE — — LIV: - | Pok.: 680 


*hrau ‘to flow’ 

*AVESTAN: YAv. (Gpl.) raonam ‘rivers’ (Y 10.17, Yt 14.21) 

*OLD PERSIAN: rauta(h)- <r-u-t-> ‘river’ (DZc.9) 

*MIDDLE PERSIAN: MMP rwd, BMP [wt /rod/ ‘river, canal? = DMMPP: 299a 
*PARTHIAN: r^w- ‘to pour off’, also rwd ‘rivers’ = Ghilain: — | DMMPP: 293b, 299a 
Pres.: IND. 3pl. r’wynd 


*huah 141 


*SOGDIAN: BSogd., CSogd. rwš ‘to flow, stream’, CSogd. rwt (m.) ‘river’. © The 


sibilant š is from the aor. ?, cf. sigm. aor. Skt. asrausit (SB) ‘flowed’. 
Pres.: ОРТ. 3sg. BSogd. rws’y, CSogd. *rw3y; ’z-Impf.: IND. 3sg. CSogd. rw3’z; Inf.: BSogd. rws’t 


*CHORESMIAN: rw- ‘to flow’, r’wy- (caus.) ‘to let (it) flow’ || (+ *abi-uz-) ? m/Bzrw- 
‘to flow, flood’, m/Bzr’wy- (caus.) ‘to let it flood, to inundate’ || (+ *fra-) hlw- ‘to 
drip; flow (of urine)’, hl’wy- (caus.) ‘to let it drip, drop’ = Samadi: 173, 168, 47,
```


## [2026-09-14T01:13:22.515Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | grep -i pok; echo ---; grep -ln \"rahati\" POK_0*.txt POK_full.txt 2>/dev/null; echo \"--- search legh page 651\"; grep -n \"legh-\\|léghos\\|Aéxos\\|bedstead\" POK_full.txt | head -20",
 "description": "Search Pokorny files"
}
```


### [2026-09-14T01:13:22.598Z] TOOL RESULT

```
POK_01.txt
POK_02.txt
POK_03.txt
POK_full.txt
---
POK_full.txt
--- search legh page 651
17705:widespread extension delegh-3iU6 (d)longho-{see finally Persson Beitr. 889, 903 Anm. 1) 
17719:delegh-, djjgho-: 
19670:pvov "head fascia', Sspvia PI. " bedstead '; hom. present 5i5r|Mi bind' is to 5nau) after 
42881:Material: Armenian p 'and \esse\' {*phond'"o-); Latin sponda ' the frame of a bedstead, 
50470:strap of the bedstead ', PI. (NT.) " shroud ' (the forms Kripia, Kaipia s. Liddell-Scott; the 
54109:Root / lemma: legh- {*lehugh- ) 
54141:Latin lectus, -/""deposit, layer, bed' (from *legh-to-), lectTca^ a litter, sedan, portable 
54146:pigpen ' {*u(p)o-legh-s)\ gall. legaslV has put down, set down, put, placed, set, fixed '; 
54158:*legh-sko-. 
56239:lova' bedstead ', Latvian lava' fool's wand, bedstead ', Danish older /o, Swedish lofve, 
73108:bedstead '; Lithuanian suo/as' bench ', Lithuanian 5//e 'trough, Schweinetrog', Latvian s/7e 
79821:Root / lemma: sp(h)elgh(en, -a), splengh-, splegh- 
85143:Root / lemma: telegh- 
85181:See also: compare above telegh-.
```


## [2026-09-14T01:13:25.479Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"rahati\" POK_full.txt | head; echo ---; grep -n \"Page(s): 651\\|Page(s): 650\\|Page(s): 652\" POK_full.txt | head",
 "description": "Pokorny rahati context"
}
```


### [2026-09-14T01:13:25.549Z] TOOL RESULT

```
20657:Czech drazitr make a rabbet or a furrow, hollow out '; perhaps also Czech z-drahati se 
---
53599:Page(s): 652 
53631:Page(s): 651 
53648:Page(s): 652 
53664:Page(s): 652 
53682:Page(s): 652 
53883:Page(s): 652 
53888:Page(s): 652 
53967:Page(s): 650-651 
54004:Page(s): 651 
54107:Page(s): 652-653
```


## [2026-09-14T01:13:28.015Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '53960,54010p' POK_full.txt; echo \"=== 53620-53650\"; sed -n '53615,53650p' POK_full.txt",
 "description": "Pokorny page 651 entries"
}
```


### [2026-09-14T01:13:28.148Z] TOOL RESULT

```
after Jokl L.-kunder U. 205 to alb. laikatis " flatter, cajole '. 

References: WP. II 376 f., WH. I 752 f., 754 f., 819, Trautmann 146, 156, J. Loth RC 38, 

49 f. 

Page(s): 650-651 

Root / lemma: la-2{*lehLK^'^-) 

Meaning: to be concealed, covered 

Note: also /ah/- and /ahf/J-d'^- 

Material: Gr. ApTO, ArjiTO snsAaGETo Hes., due to a *Ka-F6q 'hide, conceal' perhaps 

Kzix)py6q, TravoupYoq " nefarious, evil, wicked ' (*Ar|Fo-F£pY6c; ' im verborgenen tuend, was 

das Licht sch euen muft '); 

from the d^-extension (d^-present?) Kr\Qio, Doric AaGu) "to lurk, lie hid, be concealed, 
escape notice, skulk', AriGn ' a forgetting, forgetfulness, a place of oblivion in the lower 
world ', Doric KaBoq n. ds., aAr|6nc;, Doric aAaOnq " unconcealed, so true, real, opp. false, 
apparent, of persons, etc., truthful, honest ', AavGavu) (Anau), sAaGov, AsAnGa) ' to escape 
notice, to be unknown, unseen, unnoticed ', AaGp6(; ' clandestine ', Ionian AaGpn, Attic 
AaGpa Adv. " clandestine ', horn. AaGi-Kr|5n(; ' banishing care '; 

/a/-6'^-\r\ AaiG-apYO(; besides Kr]Q-apYoq; 

Latin /ated, -ere' to lurk, lie hid, be concealed, escape notice, skulk ' (from a participle 

*/9-td-S)] 

Old Icelandic /omr' betrayal, deceit'. Middle High German /uo' pestering, temptation; 
snare'; Old High German /uog 'cave, lair', luoga' lair (of an animal) '; 

Old Bulgarian lajati" be after someone, to follow somebody, to pester somebody ', 
Czech (due to a *la-ka= Old High German luoga) lakati' make advances, pursue '; 

Tocharian A lat-, lant-, B lat-, lant- " go after ', preterit 3. Sg. A lac, B lac{: gr. eAqGe), 3. 
PI. A lantsehc, B /a/e" (Pedersen Hittite 173, 189). 

References: WP. II 377 f., WH. I 768 f. 
Page(s): 651 

Root / lemma: /ama {*/ehumta-) 
Meaning: swamp, puddle 
Grammatical information: f. 


=== 53620-53650
Old High German laffan{luof) "lick'. Old High German /e/?^/" spoon'. Middle Low German 
lepelds. (: Gothic *lapins, from which borrowed Old Prussian lapinis); Old English lapian 
"drink, slurp ', Old Swedish lapads. {*lapdn), nisi. Norwegian lepja^ lick slurping like a dog 
' = Middle High German leffen^\\ck, slurp ', Old High German gilepfen 6s:, intensive. 
Middle High German Modern High German /appends, behaves to schlappen as lecken 
"lick' to schlecken; 

besides Modern High German dial. labbe^\\'Q\ /abern'ta\k slowly, simply; drink licking ', 
Serbo-Croatian labati^ drink like dogs or cats '; 

here perhaps russ. dial, lopa^ devourer', lopatb^ devour'; Bulgarian lapam^ devour, 
gobble', etc.; also Old Bulgarian /obbzat/ ^k\ss' ("*munch, smack, chew loudly ')? 

Maybe alb. /ope ^cow (eating slowly?) '. 

References: WP. II 383 f., WH. I 754, Wissmann Nom. postverb. 72 f. 
Page(s): 651 

Root/ lemma: /ati^-, Ikiy-{*lehu6y-) Note: common Proto Germanic -u- > -u-, -y-, -/-. 
Meaning: to cut, hurt 

Material: Gr. Aiarpov n. " shovel, poker, spade; spoon', AioTpsuu) " hoe around ', Aiarpou) " 
level, even ', Aiarpiov n. "spoon'; Aiayapiov "hack, mattock, hoe' (*Ai5-aK0-); 

Latin laedo, -ere "injure, damage'; 



Latvian Ifdu, /fst' clear, cut away ', Lithuanian lydymas, lydimas' clearing, virgin soil, 
untilled land '. (common Baltic alb. y > i) 

Maybe alb. {*lydo) /endoJ'hurV, /end/ne' meadow, virgin soil '; (common Polish alb. y > e). 
References: WP. II 379, WH. I 749. 
Page(s): 652 

Root / lemma: /ai- {*/ehu-os)
```


## [2026-09-14T01:13:39.212Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^Root / lemma: re\" POK_full.txt | head -40; echo \"=== rahas\"; grep -n \"rahas\\|ra-has\" POK_full.txt | head",
 "description": "Pokorny r- roots and rahas"
}
```


### [2026-09-14T01:13:39.285Z] TOOL RESULT

```
69511:Root / lemma: red- rod- 
69534:Root / lemma: reg-2 
69550:Root / lemma: reg-1 
69716:Root / lemma: reg-2, reR- {rek-7) 
69735:Root / lemma: rehg^'os- {* ohrehg''ohs-) 
69763:Root / lemma: reb"^- 
69781:Root / lemma: reid!^- 
69847:Root / lemma: reid- 
69863:Root / lemma: reig- or reig- 
69919:Root / lemma: reik- 
69955:Root / lemma: rei-1 
70038:Root / lemma: rei-2, roi- 
70060:Root / lemma: rei-3, re(i)- 
70111:Root / lemma: rei-4 : rei- 
70138:Root / lemma: rei-5 
70146:Root / lemma: rei-r(ei)- 
70159:Root / lemma: reia-, n- 
70164:Root / lemma: rek-1 
70187:Root / lemma: reRt^h- 
70206:Root / lemma: reR- reg- 
70222:Root / lemma: remb-, romb-, roinb- 
70228:Root / lemma: remb-, romb-, romb- : 'to haek, noteh' derived from a zero grade of Root / 
70256:Root / lemma: rem-, rema- : 'to rest; to support' derived from a zero grade of an extended 
70308:Root / lemma: rend^- 
70324:Root / lemma: rent- 
70340:Root / lemma: rep- 
70379:Root / lemma: ret(h)- 
70434:Root / lemma: reu-b-ax\6 reu-g- 
70479:Root / lemma: reuA^-{*uereuA'^^ (zero grade of *hieleuRh-) 
70576:Root / lemma: reugh-m(e)n- 
70664:Root / lemma: reu-2, reus- : ru- 
70856:Root / lemma: reu-3, reu-s- 
70866:Root / lemma: reu-4 
70871:Root / lemma: reu-smen- 
70888:Root / lemma: reus- 
70898:Root / lemma: reuto-, routo- rut- 
70914:Root / lemma: reua- : ru- 
70941:Root / lemma: rezg- 
70963:Root / lemma: red-1 
70979:Root / lemma: red-2 : rod- : rad- 
=== rahas
```


## [2026-09-14T01:13:53.832Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==384' BQT_v2_pages.txt | head -40",
 "description": "BQT vol2 leaf 384"
}
```


### [2026-09-14T01:13:54.957Z] TOOL RESULT

```
‫‪Go‬‬                                                                                     ‫‪-۲۳-‬‬
                                                                           ‫بقمه از صفحٌ ‪۲۲٩‬‏‬
 ‫است ( ‪ » ) 80303186 . ]6156‬و لیزیمعنی پوست کرتنکله بعتی تمساح است‪)662۳27۵6-‬‬
 ‫(‪6[۵‬ع‪ 61 0۲6‬و باز بمعنی استخوان لان البحر نی ارب بحری و دمیاست‪6620۵72‬ع)‬
 ‫ذ)ر»خش‪ ,‬برق اکستووبند‬     ‫«‪.‬م‪.‬‬
                              ‫فش (‪۵‬‬  ‫دخشر »‬‫‪ = ۵9‬در‬           ‫(‪« . 61 ۱6126‬لت نامه» ‪.‬‬
‫که در زبان پارسی هیچ‌کلمه نیت که اول او ذال بود جزاین‌کلمه ‪ ,‬ایوشکور (بلخی) کوبد ‪:‬‬
            ‫همانا نگرید چنی ابرزار‪.‬‬               ‫ذرخشی ار شندد بگاه بهار‬
 ‫« لفت فری ‪٩ ۸۶۲‬‏ ‪.‬‬
 ‫‏‪« - ٩‬نرع > كوشة کشت بود وزرع بتازی کشت راکوبند ‪ .‬رود کی (سمرقندی) کوبد‪:‬‬
     ‫زرع کشت است و ذرع کوشۀ کشت ‪€.‬‬                   ‫شوت‬‫هشدچ‬ ‫بار‬
                                                               ‫نرع وزرع ازبپ‬
‫« لفت فری ‪ » ۸۲۲‬این کلمه و معنی با همین شاهد در لغت امه عجیبی که در حاشيةٌ لغت لام‬
  ‫هبماین‬‫اسدی آقای نخجوانی است دیده میشود و لغوبین دیگر لیز عین آنرا بپمین صورت و‬
‫شاهد می‌آورند » لکن بگمان من اکر شمرواقعاً از رودکی باشد (وکمان لمیکنم که باشد ) در‬
 ‫این لفت ومعنای آن پیدا شده است ‪ +‬و عصبت بودن‬          ‫داده » و ازآن تصحف‬     ‫روی‬    ‫شمر صصفی‬

 ‫لغت نامه بموزرازین است که برای همه حروف هشتگانه‌ای که درعربی‌هست ودرفارسی لیست امثلة‬
                 ‫بسباری ازکلمات ناشنوده] ورده ومدعی است که همه آنها فارسی است‪« .‬لغت نامه»‪.‬‬
 ‫‪-( ۷‬عر) بککرزدن ‪ .‬بتاراشجپی‌موادنلن(صادر بیپقی) ‪ -‬کز » ارش » رش ‪ -‬فرع »‬
      ‫تكر‬
        ‫مه ب‬
           ‫چون مطلق کوبند ممادل شانزده کره است عنی مك متر وچپارصد بك متر و درنرع شا‬
  ‫ودوازده صد بك متر است (وبیشتر درتبریزمتداول است) * و ذرع مقصرصاوی بك متر وچهارصد‬
                                                                        ‫بك متراست (‬
     ‫وآن درتهران وفاری معمول است) > نرع لشابوری دویرایس وليم نرع شامی است‬
 ‫‪ -۵۸‬برنده ات از بلدرچن بزرکتر و از کيك خردتر و برنگه سنجاب‬                         ‫ل«ت‌نامه ‪٩‬‏ ‪.‬‬
‫و اینکه صاحب برهان میگوید از كبك‬            ‫ایفست‬
                                                ‫رلط‬
                                                  ‫ترو‬
                                                    ‫ازهمةٌ الواع طبر حتی تذ‬            ‫وکوشت آن‬
                        ‫بطراسالیون ‪.‬‬     ‫_‪:‬‬
                                          ‫‪٩‬ر‏ك‬        ‫نست‪« .‬لغت نامه»‪.‬‬      ‫ست‬
                                                                             ‫دتر»‬
                                                                                ‫بزرکتر اس‬
     ‫‪ -۰‬هز ‪ , ۲(2)6(2).2‬پهلوی ‪ ۰ 780‬بر « یونکر ‪( ۹۰۱۰‬عر ) بمعنی ارو آلت‬
     ‫مردان » عبری «ز کر» (بفتح اول ودوم ) ‪.‬آرامی «زکرا» » لغات جنوب‌الجزیره وحيشه «ز کر»»‬
                                 ‫*‪.‬‬    ‫آشوری بابلی ‪ 2‬ز کرو ) بقتح اول ودوم) و ولفنون ص‪۷۸۲‬‬

                                                   ‫‪ -‬م اول و فتح دوم =‬         ‫ذرت‬
```


## [2026-09-14T01:14:06.052Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in رهیدن رستن راز سرّ; do echo \"== $w\"; grep -n \"$w\" BQT_v2_pages.txt | head -8; done",
 "description": "Grep BQT v2 for Persian headwords"
}
```


### [2026-09-14T01:14:07.485Z] TOOL RESULT

```
== رهیدن
24061:         ‫تار (یودد فاعلی و اصان ‪.‬رکه ‪ :‬دادار) ‪.‬‬             ‫از ‪ :‬رس ( رستن » رهیدن) ‪+‬‬       ‫‪6‬‬
24064:                        ‫‪ - ۷‬از ‪ :‬رست (رستن » رهیدن) ‪ +‬کار (یسوند فاعلی ومبالفه) ‪.‬‬
26264:  ‫چ ر ها ‪ -‬بفتح اول» از ‪ :‬ره (رهیدن) ‪( ۱ +۳‬صفت مشبهه) [رك ‪ :‬رهیدن ‪ .‬رستن ] ؛‬
== رستن
414:                                                 ‫جار النهر ‪ -‬رستنیی‌باشد مانندیلوفر‬
4758:‫رای قرشت وواو بالف کشیده » نام رستنیی باشد‬                 ‫چدار ‏ پکر اول بر وزن نگار »‬
4837:   ‫«جفری ‪ .۷۱- ۹۹۱‬شکل پپلوی آن ‪ »08271‬است ‪ « .‬بنا‪٩ ۲ :۲۳۱‬‏ کرستنسن کلمه‬
5139:                                                             ‫ثانی » بمعنی چرخله است » وان رستنی ولباتی‬
5586:      ‫‪« -‬چشمآ لوی‌نگرستن‬                 ‫‪ _ ۱‬مخفف« چشمآغیل» («‪.‬م‪ ).‬ورك‪ :‬چشمآغلیدن‪.‬‬
5617:                                                            ‫از سجده کردن۔ و فرونگرستن بزمین باشد‬
5898:        ‫ورسیدن = وپس سر نگرستن‬
6940:                                 ‫را از روسی عارت مىداند‬       ‫کرستنمن کلم استی ‪02000۳6‬‬
== راز
48:                                                                         ‫وشیرازی) ‪.‬‬
57: ‫آقای علینقی بهروزی دبیر دبرستانهای شبرازنیزسلسلة مقالانی بعنوان «تقریظ‬
442:  ‫عربی «جاسوی‌صاحب‌رازید» « شرح قاموی ‪*.‬‏‬         ‫‪۴‬‬        ‫‪ - ۴‬رك ‪ :‬پبای وپپاسا‪.‬‬
533:‫پبالة پرازآبکوثر باشد ‪ -‬ودهان (‪ )۱‬ممشوقرا‬                                                              ‫است‬
541:‫و بمعنی جام پرازشیرومی است ککنهابه ازیبالة‬             ‫و یال آبخوربرا نیز کوبند ‪ -۴‬وآیینه‌ای باشد‬
1176:     ‫لییبی «جهادگیری >‬         ‫خیکی است پرازباد ودمرنآته از بر‪.‬‬
1301:        ‫قاآلی شیرازی « فرهنك شاهنامه ‪> ۰۰۱‬‬
1388:           ‫دراز کند » و بعربی صرار گوبندش( ‪.‬‬         ‫مردم‬   ‫صف کشیدن‬        ‫و‬          ‫زدن‬   ‫ثالی » بمعنی حلقه‬
== سرّ
```


## [2026-09-14T01:14:13.256Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for L in 24061 26264; do echo \"line $L leaf: $(head -$L BQT_v2_pages.txt | tr -cd '\\f' | wc -c)\"; done; echo; sed -n '24050,24070p' BQT_v2_pages.txt",
 "description": "Leaf indices in BQT v2"
}
```


### [2026-09-14T01:14:14.272Z] TOOL RESULT

```
line 24061 leaf: 408
line 26264 leaf: 445


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
```


## [2026-09-14T01:14:22.638Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 406 407 408; do echo \"##### leaf $n\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' BQT_v2_pages.txt | head -30; done",
 "description": "BQT v2 leaves 406-408"
}
```


### [2026-09-14T01:14:24.156Z] TOOL RESULT

```
##### leaf 406
  ‫رزه‬                                                                                               ‫‪‎-‬ی ) ‪“A‬‬


 ‫مکان‌جنکه‬      ‫زرمگاه‪ -‬بروزن گا‬                         ‫رنگضرا کننزته‌اند ‪-‬و‪٩‬ی‏معنی رنگ کننده ‪- ۴‬‬
                                                         ‫وامر برنگ کردن هم هت ‪٩‬‏ ‪ -‬و زهر هلاهل‬
                                                          ‫را کیویزند ‪ -‬ویکس اول مخقف ریز باه‬
                       ‫گاه باشد ‪۲‬‬   ‫کردن وجنگ‬

   ‫مت‬      ‫که‬         ‫ون‬     ‫ررمگه ‪-‬‬
             ‫رزمگاه است که جنک گاه باشد ‪۹‬‬                ‫ازریختن مشتق است ‪ -۴‬ودرعربی شالی راگوبند‬
 ‫بروزن گرم سیر ‪ ,‬لامروز‬
                                                         ‫کبهرنج پوست دباارشد ‪ ۴‬چرهزاز براج کوب‬
                        ‫مگیر =‬            ‫رد‬
                   ‫بازدهم باشد از ماهپای ملکی ‪۱‬‬
                                                                                      ‫رکاویند ‪.‬‬
 ‫ررمه = بفتح‌اول والك وسکون ثالی»‬                       ‫ربران * د بباای ابجدبالف کشیده‬
  ‫ایند*‪ -۱‬وبك لنگه بار واسباب‬
                            ‫رو‬‫بوفچرخت ک‬                                  ‫بروزن بزدان ‪ .‬باغبانرا گویند ‪.‬‬
 ‫وقماش را نکیفزته‌اند » و بکضویبند ابن لفت‬               ‫ررد ‏‪ = ٩‬بقتح اول وسکون نالی ودال‬
                    ‫غرمی است‪ »:‬وبکسی اول ات‬                     ‫ابجد (‪ » )۱‬پرخور وشکم خوار کروایند ‪.‬‬

 ‫دزم یوز بوامبیامی حطی (»)‬                               ‫ررده ‪ = ۷‬بقتح اول بر وزن زرده »‬
                                                              ‫بمعنی «انده وکوفته شده وآزرد‪ :‬راه باشد ‪.‬‬
‫جوز بمعنی تفحص و تجسی و جستجو کردن حم‬                    ‫درم = بفتح اول وسکون الی و میم »‬
                                    ‫‪٣‬‏‬    ‫آ مده ات‬       ‫بمعتی جنک و جدال باشد ‪ - ۸‬و هیمه وهیزم‬

    ‫زره د بنتح اول وتخفیف ثالی » ن‬                       ‫وی »‬
                                                            ‫طعام پختن را نیزگوند ‪ -‬و بفتحاتولال‬
‫‪۱‬ت‪ .۴‬وآن ناي ا هردوسوآیرا‬                 ‫‪E‬‬             ‫رنگه هم‌آمده‬     ‫بعنیر نگه میکنم‪٩‬‏ چه ربزمعتی‬

##### leaf 407
      ‫‪- 6‬‬                                                                               ‫رژیدن‬

‫رر بدن "ت بورژن رسیدن » بمعنی‬                      ‫اندازند وبعربی شربط کوبند وبزبان دیگر سازو‬
                      ‫رنگه کردن باشد ‪.‬‬             ‫خوانند ‪ -‬وسکه انگور را کیفزته‌اند که بتازی‬
‫ددلن » بر وزن امین ‪ ۰‬بمعنی محکم‬                    ‫عنب‌الملب کوبند = و باتشدید ثالی در عربی‬
                                                  ‫حلقه‌ای که برآستان درس کنند ‪ ۱‬و‪-‬ققل را‬
‫واستوار ومضبوط باشد؟ ‪ -‬ودرعربی‌به‌عتی آرمیده‬
‫و آرامکرفته و کرامایه وچیزبکه بوزن کران‬             ‫لیز کوبند‪ .‬وبمعنی زدن‌هم‌هست که بعربی ضرب‬
                                ‫وسنکن باشد ‪۴‬‬                                            ‫خوانند ‪.‬‬



                                         ‫بیان نهم‬
                  ‫غوت‬
                    ‫لد‬‫ررای بنیقطه با زای فارسی مشتمل بر‬
                                                      ‫د‬

‫ررد (‪ »)۱‬بفتح اول وسکون انی بر | براستی‌آن دبوار سازد وآنرا رزه‌بهنایز کوبند‪-‬‬
‫ورسمالی که هر دو سر آ را برجایی نشدلد ویر‬          ‫درهمه چیز را‬   ‫‪ ,‬سيار خوار وحر‪.‬ص‬     ‫وزن وجد‬

‫ومثال آن اندازند و آنرا‬
                      ‫آن رخوت پوشیدلی ا‬                                              ‫کوبند ‪: ۷‬‬




                                                                    ‫(‪ )۱‬چك‪ :‬رزد ()‬
  ‫از ‪ :‬رز (ه‪.‬م‪٣ ) .‬‏ يدن‬    ‫‪-‬‬    ‫‪۳‬‬             ‫امروز « چفته ورزه » مستعمل است ‪.‬‬   ‫‪- ۱‬‬

                    ‫‪ ۴‬ماخون از (عی) «ناطمالاطبا» رك‪ :‬حاشية ‪: 4‬‬               ‫(پونه مصدری) ‪.‬‬
##### leaf 408
                                                    ‫بیان دهم‬
          ‫رای می نقطه باسین بی نقطه مشتمل بر ببست وبك لفت و کنایت‬                                  ‫در‬

  ‫ویت‬ ‫چیوزی باشد از خحبرکا‬    ‫اضداد است ‪-‬‬                    ‫ر سس س بفتح اول وسکون‌ئالی ‪ ۰‬بمعنی‬
 ‫وامثال آن ‪ -‬ومقدمةٌ ابتدای نب ‪ -‬وبهم رسیدن‬                 ‫رسیدن و وارسدن باشد ‪ - ۱‬و بمعتی فاعل که‬
‫حرارت را نیز گویند ‪ -‬و نامکوهی هم هٽ ‪۹‬‬                       ‫وارسنده باشد ‪ - ۴‬وامربرسدن هم هت بعنی‬
‫رسام = با تشدید ثالی بر وزن قام »‬                           ‫ری ‪٩‬‏ و‪-‬طناب و کمند ورسن را لیز‬
                                                                                          ‫ویاو‬
                                                                                             ‫بر‬
 ‫نآاهمنگری است که تدبیرسکندرآینه ساخت_‬                       ‫کوبند‪ - ۴‬وطلا و لقره ومس و سیماب وسرب‬
          ‫وئام نقاشی که درخدمت بهرامگور میبود ‪.‬‬              ‫وآهن وهرچیز از فلزات که آنراکشته باشند ‪-‬‬
 ‫رسانه = بروزن‌بهانه» حسرت وافوی‬
                                                             ‫ودرهادی شیر هرچیزوهربك از فلزات کشتهرا‬
                                                             ‫رس« یگویند وجمع آن‌رساین‪ -‬ونام رودخانه‌است‬
                                       ‫وتاسف را گونند‬
                                                             ‫که به اری اشتهار دارد ‪ - ۴‬کولوبند زانرالیز‬
 ‫رسپبنا ‪, = .‬ابای فارسی بروزن‌تخمناء‬                        ‫گفتها ند ‪ -‬و یمعنی مفسد وفاد کننده هم‌آمده‬
  ‫بلضت زند وبازند (‪ » )۲‬قصل بابیز رگاونند ‪.‬‬                  ‫است ‪ -‬وشکم خواره وپرخور وحریص درهرچیز‬
‫هفتح اول بروزن مت » ماضی‬   ‫رست ب‬                             ‫خوردلرا نیز گویند‪ .‬وبعربی!کول‌خوانند‪ .‬وبمعنی‬
‫رستن است یعنی خلاص شد و لجات بافت *‪-۷‬‬                        ‫آرخکه کاول وشکم خواره حوریص باشد بم‬
‫حدققین بر کسی اطلاق کنند که از صراط‬
                                  ‫ومنز‬                       ‫و کلونند را لیز گوبندا ‪۳‬‬   ‫اول‌هم | مده‌است ‪۳‬‬
 ‫خواهش‌ضالی رسته باشد واز دوزځ قید به‌بهشت‬                  ‫ومحکم وسخت‪,‬ر | همگفته‌اند‪ ۷‬وبکر اول اهر‬
‫لجات پیوسته ‪ -‬وبمعتی زمین ‪ -‬و صفه وابوان‬                     ‫‪ -‬ودر‬   ‫برسیدن ورشتن (‪ )۱‬است ينی بریس‪۸‬‬
‫شیده را یز‬
         ‫صف‬‫ههمست (‪ - )۳‬و راسته و ک‬                          ‫عربی بفتح اول وثالی مشدد ساکن ‪ ۰‬بمنی صلاح‬
‫کوبند ‪ -۱۷‬وبضم اول ماشی روبیدن باشد معنی‬                    ‫وفساد کردن در ميان مردم باشد و ایذجا بطریق‬
  ‫(‪ )۳‬چك‪ :‬همآ مده است ‪.‬‬                   ‫(‪ )۲‬چك ‪ :‬ژد و بازند ‪.‬‬               ‫(‪ )۱‬چك ‪ :‬رستن‬
```


## [2026-09-14T01:14:36.643Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==408' BQT_v2_pages.txt | tail -25; echo \"#### leaf 409\"; awk 'BEGIN{RS=\"\\f\"} NR==409' BQT_v2_pages.txt | tail -22",
 "description": "BQT leaf 408-409 footnotes"
}
```


### [2026-09-14T01:14:37.765Z] TOOL RESULT

```
‫رستن است یعنی خلاص شد و لجات بافت *‪-۷‬‬                        ‫آرخکه کاول وشکم خواره حوریص باشد بم‬
‫حدققین بر کسی اطلاق کنند که از صراط‬
                                  ‫ومنز‬                       ‫و کلونند را لیز گوبندا ‪۳‬‬   ‫اول‌هم | مده‌است ‪۳‬‬
 ‫خواهش‌ضالی رسته باشد واز دوزځ قید به‌بهشت‬                  ‫ومحکم وسخت‪,‬ر | همگفته‌اند‪ ۷‬وبکر اول اهر‬
‫لجات پیوسته ‪ -‬وبمعتی زمین ‪ -‬و صفه وابوان‬                     ‫‪ -‬ودر‬   ‫برسیدن ورشتن (‪ )۱‬است ينی بریس‪۸‬‬
‫شیده را یز‬
         ‫صف‬‫ههمست (‪ - )۳‬و راسته و ک‬                          ‫عربی بفتح اول وثالی مشدد ساکن ‪ ۰‬بمنی صلاح‬
‫کوبند ‪ -۱۷‬وبضم اول ماشی روبیدن باشد معنی‬                    ‫وفساد کردن در ميان مردم باشد و ایذجا بطریق‬
  ‫(‪ )۳‬چك‪ :‬همآ مده است ‪.‬‬                   ‫(‪ )۲‬چك ‪ :‬ژد و بازند ‪.‬‬               ‫(‪ )۱‬چك ‪ :‬رستن‬


      ‫‪ - ۳‬قس‪ :‬رسمان‪.‬‬                 ‫قس‪ :‬بازری ( باز رسنده )‪.‬‬        ‫‪۴‬‬        ‫‪ - ۱‬رکه‪ :‬رسدن‪.‬‬
                                           ‫رزژد » رزد (ه‪.‬م ‪(.‬‬                 ‫؟ ‏ رکه ‪ :‬اری ‪۰‬‬
                   ‫کلو را ز رسی بسر برمیر‪.‬‬                      ‫بیلفنج و زالففد خوش خور‬
  ‫‪.‬‬       ‫ابوشکور بلخی‪(« .‬فت فری ‪٩۹‬‏‬

  ‫‪ ۸‬رکه ‪ :‬رسیدن»‬                        ‫رکه‪ :‬رست ‪.‬‬      ‫‪۷‬‬            ‫رکه ‪ :‬ی‪٩‬‏ همین ستون‪.‬‬     ‫‪۱‬‬
                       ‫‪٩ .‬‏‬        ‫» ابیز « بوتکر‬    ‫بهلوی ‪72‬‬            ‫هز ‪20102 ,‬‬     ‫‪۹‬‬         ‫رشتن ‪.‬‬

                   ‫» رسته‌بود چون صف‪:‬‬     ‫رجه ؛ رژه ‪” :‬رست‬      ‫‪~۹‬‬           ‫رکه ‪ :‬رستن ‪.‬‬     ‫‪°‬‬
                                          ‫چون ملك الهنداست از ریدکانش (آن دهد کاش ‪ .‬دهشدا)‬
               ‫‪.‬‬     ‫خمروی‬    ‫‪.‬‬   ‫بر خادم هندو دو رست‬   ‫کردش‬

      ‫‪€‬‬    ‫د لفت فرس*‪4‬‬

#### leaf 409
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


## [2026-09-14T01:14:55.940Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in رازیانه راستی راسو; do echo \"== $w\"; for L in $(grep -n \"$w\" BQT_v2_pages.txt | cut -d: -f1 | head -6); do echo -n \"line $L leaf \"; head -$L BQT_v2_pages.txt | tr -cd '\\f' | wc -c; done; done",
 "description": "Locate راز area in BQT v2"
}
```


### [2026-09-14T01:14:57.382Z] TOOL RESULT

```
== رازیانه
== راستی
line 8287 leaf 142
line 8291 leaf 142
line 9760 leaf 167
line 9846 leaf 168
line 14196 leaf 240
line 14636 leaf 247
== راسو
line 10157 leaf 174
line 10584 leaf 181
line 17653 leaf 299
line 19895 leaf 335
line 22993 leaf 389
line 25795 leaf 437
```


## [2026-09-14T01:15:00.344Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 382 383 384 385; do echo \"##### leaf $n (first 12 lines)\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' BQT_v2_pages.txt | head -12; done",
 "description": "BQT v2 leaves 382-385 headers"
}
```


### [2026-09-14T01:15:01.433Z] TOOL RESULT

```
##### leaf 382 (first 12 lines)
  ‫دهیم‬                                                                                            ‫‪۲۱‬‬
                ‫هت که بعربی سنای گوبند ‪.‬‬                  ‫دیو کلو چ ‪ = ۱‬بضم کاف ولام بواو‬
 ‫دو مشنگ‪ -‬بفتح میم وشین‌قطه‌دار‬
                              ‫ډ‬                            ‫کشیده وبجیم فارسی زده» طفل مصروع و کودگ‬
 ‫وسکون نون وکاف فارسی» بمعنی کاومشنگه(‪)۱‬‬                                          ‫نفته راگویند ‪.‬‬
                                                                                               ‫گر‬‫ج‬
 ‫است » وآن نوعی ازحبوب باشد که چون پوست‬                   ‫ديو کلوخ ‪ ۴‬کدلوخهای بزرکهرا‬
                ‫آلرا بکنند بعدس مقشر ماند ‪.‬‬                ‫گویند که در وقت شیار کردن از زمین بر خیزد‬
‫ديو فك ‪ -‬بر وزن ربوند ‪ ,‬هام داروبی‬                                                         ‫وبر اطراف ریزد‪.‬‬
                                     ‫است دوایي ‪.‬‬           ‫دگینودم" د بر وزن دیو مردم »‬
                                                           ‫نوعی از گندم است که هر دو دانه دريك علاف‬
‫وزن موه ‪ ۰‬کرم پبلة‬         ‫‪-‬ر‬
##### leaf 383 (first 12 lines)
                                                     ‫ن|حام‬

        ‫در حرف ذال نقطه دار‪.‬با حروف تپحی مشتمل بر سزده لغت‬
‫بل د بکراول وسکون بای ابجد ‪۴‬‬                                 ‫* ذاقنو بداس ‪ ۱‬سبکرفان ونون‬
‫ولام" بوست لاك بشت‌هندی باشد؛ وبعضی گویند‬                    ‫مواو رسیده و کت بای اند ودال بنوقعاه بالف‬
‫آن با‬   ‫است؟ ‪.‬خاکنتر‬         ‫دكربیشتابی‬
                                      ‫بوست لا‬                ‫کیت ورین مه زود امسانتبای‬
                                                             ‫وویند نوعی‬
                                                                      ‫بعنی مانند غار »آون داروبی‌است گ‬
 ‫‪ ۰ °‬بر وزن و معنی درخش‬                                            ‫از مازربون است وبرکث آن یهن مبباشد‪.‬‬
                                  ‫ذر خش‬
          ‫است که برق وتابندن وروشنی باشد ‪.‬‬                   ‫ذاقی ‪ = ۴‬بروزن سافی؛ بیونالی درخت‬
##### leaf 384 (first 12 lines)
‫‪Go‬‬                                                                                     ‫‪-۲۳-‬‬
                                                                           ‫بقمه از صفحٌ ‪۲۲٩‬‏‬
 ‫است ( ‪ » ) 80303186 . ]6156‬و لیزیمعنی پوست کرتنکله بعتی تمساح است‪)662۳27۵6-‬‬
 ‫(‪6[۵‬ع‪ 61 0۲6‬و باز بمعنی استخوان لان البحر نی ارب بحری و دمیاست‪6620۵72‬ع)‬
 ‫ذ)ر»خش‪ ,‬برق اکستووبند‬     ‫«‪.‬م‪.‬‬
                              ‫فش (‪۵‬‬  ‫دخشر »‬‫‪ = ۵9‬در‬           ‫(‪« . 61 ۱6126‬لت نامه» ‪.‬‬
‫که در زبان پارسی هیچ‌کلمه نیت که اول او ذال بود جزاین‌کلمه ‪ ,‬ایوشکور (بلخی) کوبد ‪:‬‬
            ‫همانا نگرید چنی ابرزار‪.‬‬               ‫ذرخشی ار شندد بگاه بهار‬
 ‫« لفت فری ‪٩ ۸۶۲‬‏ ‪.‬‬
 ‫‏‪« - ٩‬نرع > كوشة کشت بود وزرع بتازی کشت راکوبند ‪ .‬رود کی (سمرقندی) کوبد‪:‬‬
     ‫زرع کشت است و ذرع کوشۀ کشت ‪€.‬‬                   ‫شوت‬‫هشدچ‬ ‫بار‬
                                                               ‫نرع وزرع ازبپ‬
##### leaf 385 (first 12 lines)
    ‫‪۷‬‬                                                                                  ‫فکران مرئوما‬

                    ‫ذ کران از مرتبة عید فروتراست ‪.‬‬       ‫در مقابل ماده است‪,‬وبعربی لیزهمین معتی دآرد‪-‬‬
    ‫رواق » با واو و را و قاف وحرکت‬
                                 ‫د‬                        ‫ولوعی از عود الصلیب هم هت وآن نر و ماده‬
‫مجهول؛ طعامی‌است که آرا ازارد کندم پرلد ‪۲‬‬                 ‫میباشد وبعربی ورد الحمیر خوانند‪ .‬وگآیناهی‬
                                          ‫‪۳‬‬                                              ‫است دوایی ‪.‬‬
    ‫ذوش ‪ - ۲‬بروزن‌هوش»تندخووبدخلق‬
                                          ‫‪۳‬‬   ‫را گوند‬    ‫» بکس ون ‪.‬‬           ‫اا‬
                                                                               ‫ونهمر‬
                                                                                   ‫ذتکرا‬
                                                         ‫روز سیم (‪ )۱‬نموز باشد » و كران بمعنی باد‬
```


## [2026-09-14T01:15:11.876Z] TOOL CALL #36: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:926 2>&1 | head -60",
 "description": "Try ref_page for BQT 926"
}
```


### [2026-09-14T01:15:13.242Z] TOOL RESULT

```
no scan of BQT covers printed page 926 (see 'scans' in refs_online.json)
```


## [2026-09-14T01:15:25.041Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 388 389 390 391 392; do echo \"##### leaf $n\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' BQT_v2_pages.txt | head -8; done",
 "description": "BQT v2 leaves 388-392"
}
```


### [2026-09-14T01:15:26.099Z] TOOL RESULT

```
##### leaf 388
   ‫راست‬                                                                                          ‫سوه‬
‫رارقی ه بر وزن عاشقی ‪ ۰‬نوعی از‬                               ‫بکیوزبند‪ ۱‬و‪-‬امر برنگه کردن همهت عنی‬
 ‫انگور است که دانهای آن کوچك میباشد ؛‬                        ‫رمك کن ‪ -‬و خاریشت را دز گفته اند ‪ ,‬و آن‬
 ‫وبعضی کویند نم کتان‌است واز آن روغ نگیر ند؛‬                 ‫جافورست معروف ‪ -‬وبمعنی زلبورسرخ وبز رکه‬
 ‫وبعضی دیگرکویند سوسن‌سفید است؛ ودیگری‬                       ‫و‌کار رایز گوبند وبعربی‬
                                                                                   ‫همآمده‌است‪ -‬وبنا گل‬
           ‫میکوید رازفی زنبق سفید امت ‪. ۴‬‬                    ‫ی‌اند راز درعربی کلاش‬
                                                                                 ‫طیان خوانند‪ -‬وکبفسته‬
##### leaf 389
 ‫”‪~A‬‬                                                                                             ‫رات‬
                                ‫تسا زع ‪‎‬هناش ‪.‬‬                ‫وبمعنی تمام ومساوات هم آمده است ‪.‬‬
‫زست رو شن ‪ -‬برفتاحوشین فرشت‬
                          ‫ا‬                           ‫راستا ه بر وزن پارسا ‪ .‬بمعنی رات‬
‫وسکون واو و نون » وزیر بهرام کوربود ولم‬               ‫باشد کهلقیض کج امت ‪٩‬‏ و‪-‬راه را لگیوزبند‬
‫بيار میکرد بهرام از قضيةٌ شبان وسگه خائن‬                             ‫که جریی صراط خوانند ؟ ‪.‬‬
     ‫متنبه شده او را سیاست بایغ فرمود ‪. ۴‬‬             ‫راستاد ‪ -‬بسکون سین بروزن بامداد‪.‬‬
                                                                                ‫وظیفه و راتب رگوانند ‪.‬‬
##### leaf 390
                                                                                        ‫‪۲4‬‬
‫خوانند ‪ ۰‬اکر درون وبرا پراز گشنیز کنند‬                 ‫استیثه ‪ = ۲‬بروزن ماستینه ‪ .‬بمعنی‬
 ‫و خشك سازند خوردن قدری از آن کزندکی‬                                     ‫راسترن باشد که حقیقی ‪۳‬‬

‫جالوران زهردار را نافع باشد ‪ .‬کوبند اک رکب‬            ‫اسحت ؟ ب=ضم ثالث و سکون خای‬
                                                                                ‫ر‬
‫باشد بیرون آورند و بریای‬     ‫دهه‬
                               ‫نک‬‫زقتی‬
##### leaf 391
  ‫س‪۳‬‬
   ‫ه‪۳‬‬‫باه‬                                                                                             ‫ران‬
‫راك ‪ -‬بر وزن خاك * فوج گووسفند‬                          ‫راف د بر وزن کاف» بزبازست جربی‬
‫جکنگویبرناد ‪ - ۱‬و بمعنیکاسة آبخوری حم‬                          ‫سیاسه خوالند ‪ .‬گوشد يوست جوزاست ‪.‬‬
‫آمده است‪ -‬ورشتةٌ سوزن رانیز گفته‌اند‪ -‬وبلفت‬            ‫راقو نه= بر وزن بابونه ‪ ۰‬پودله را‬
‫زند ویازند(‪ )۱‬راه باشد که بعربی صراط وطریق‬              ‫گونند ؛ وباین معنی بجای فا قاف وبجای نون‬
                                          ‫خواند ‪. ۴‬‬     ‫تای قرشت هم منظر آمده امت که راقونه‬
‫دگااده » با کاف بر وزن آوار» ‪ ۰‬زن‬                                                                    ‫باشد ‪.‬‬
##### leaf 392
  ‫رامعك‬                                                                                                      ‫‪-۳‬‬
‫رامش د بکراك بروزن داش ‪۰‬‬                                             ‫وآرمیدن رانیز گویندا ‪ -‬وبمعنی روان ‪7‬‬
‫بممنیآرامیدن‌و آرامش وسآود کی وفراغت باشد‪.‬‬                      ‫باشد ‪ -‬ونام شخصی که واضع سازچنگه بوده ؟‪.‬‬
‫گونند هش نگین انوشیروان چنین بوده که‬                           ‫و خوش وشاد و خرم را نیز گفته اند ‪ - ۳‬و نام‬
 ‫ومر‬
   ‫ر‪+‬اه بسیار تاريك است هرا چه بینش ؟ ع‬                         ‫دره‌ایست درملك هنب‌وستان ‪ -‬ونام عاشق ویس‌هم‬
 ‫دوباره ایست مراچه خواهش ؟ ومر گے درقفاست‬                       ‫هت » وچون او بيار عیاش وشادکام و پیوسته‬
 ‫بومعتی ساز و نوا و عیش‬             ‫<<‬     ‫مرا چه رامش‬          ‫خوشحال و خوش طبع بود او را بدن جپت رام‬
```


## [2026-09-14T01:15:36.699Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 410 411 412; do echo \"##### leaf $n\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' BQT_v2_pages.txt | head -10; done",
 "description": "BQT v2 leaves 410-412"
}
```


### [2026-09-14T01:15:37.814Z] TOOL RESULT

```
##### leaf 410
  ‫با‬                                                                                             ‫‪-‬‬

‫وفتح فوقالی وها ومیم هردوسا کن » رستم زالرا‬         ‫رسته ‪ ۱‬ب«روزن دسته ‪ ۰‬بمعنی خلاص‬
                                     ‫ف‪2‬‬              ‫شده ولجات‌بافته باشد ومطلق صفرالگیوزبند‬
                                                     ‫اعم از انان وحیوان دیگر ‪ - ۴‬وراستة هرچیز‬
‫رسقی = بض‌اول بروزن ستی " راحت‬
                                                    ‫بازار‬    ‫و راستة‬    ‫دندان‬   ‫همجو راستةٌ‬     ‫هت‬   ‫هم‬
‫وفراغت باشد ‪ - 6‬وخر کی ودلیری و شجاعت‬
 ‫وغالب شدن و مستولی گردیدن را بیز گوبند ‪-‬‬           ‫وخالهابی که دريك صف واقع شوند ‪ -‬و بمعنی‬
 ‫وبمعنی‌رزق وروزی‪ -‬ونان حولواوماحضروخوردلی‬          ‫فاعده وقانون وطرز وروش باشد ‪ -‬ونزد محفقین‬
##### leaf 411
   ‫ها‬    ‫وی‬   ‫‪-‬‬
                                                                                                                           ‫رس‬




‫مقرب وترديك راگوبند همچو سفرچی و آبدار‬                                           ‫‪۴‬‬    ‫ساد معرباست‬           ‫رصد‬   ‫و‬     ‫هیر سد‬


 ‫وآنانکه سال سال وماه بماه ورور‬              ‫وشرابداروساقی‬         ‫‪ ۰‬خدمتکار‬   ‫يفنح اول بروزن‌خهم‬           ‫”‬   ‫ر سم‬
##### leaf 412
 ‫رشتاك‬                                                                                                       ‫‪-‬ي‬
                                                                                                              ‫‪ --‬ا‬


                ‫‪.‬ویند عربی است ‪.‬‬
                               ‫رزه باشد گ‬                       ‫روز رش باوتعلق دارد ‪ - ۱‬ونوعی‌ازجامة ابرشمی‬
‫ر شت = بفتح اول بر وزن طشت ‪ ۰‬نام‬                                ‫کران بها باشد ‪ -‬وبازورا (‪ )۱‬نیزگویند که‌آن‬
‫شهری است از ولایت کیلانکه آنرا «بیه پس»‬                         ‫از سردوش است نا آرنج ‪ - ۴‬ومسافت ميان دو‬
                                                                 ‫دست‌رالیز گفته‌اند چون‌ازهم‌باز کنند؟ سومخقف‬
                                                                ‫ارش هم‌هست وآن ازآرنج‌ناسرانگشتان دست ‪.۴‬‬
```


## [2026-09-14T01:15:51.907Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==388' BQT_v2_pages.txt",
 "description": "Full BQT leaf 388"
}
```


### [2026-09-14T01:15:53.029Z] TOOL RESULT

```
   ‫راست‬                                                                                          ‫سوه‬
‫رارقی ه بر وزن عاشقی ‪ ۰‬نوعی از‬                               ‫بکیوزبند‪ ۱‬و‪-‬امر برنگه کردن همهت عنی‬
 ‫انگور است که دانهای آن کوچك میباشد ؛‬                        ‫رمك کن ‪ -‬و خاریشت را دز گفته اند ‪ ,‬و آن‬
 ‫وبعضی کویند نم کتان‌است واز آن روغ نگیر ند؛‬                 ‫جافورست معروف ‪ -‬وبمعنی زلبورسرخ وبز رکه‬
 ‫وبعضی دیگرکویند سوسن‌سفید است؛ ودیگری‬                       ‫و‌کار رایز گوبند وبعربی‬
                                                                                   ‫همآمده‌است‪ -‬وبنا گل‬
           ‫میکوید رازفی زنبق سفید امت ‪. ۴‬‬                    ‫ی‌اند راز درعربی کلاش‬
                                                                                 ‫طیان خوانند‪ -‬وکبفسته‬
 ‫راز نهان خا د کنابه از انات‬                                 ‫وبزر که بنایان باشد‪ -‬وبعضی گویند رازی معرب‬
           ‫است که بتدریج از خاکه بره‌ی‌آبد ‪.‬‬                 ‫رازاست چنانکه بازی معرب باز وتام قربه‌است‬
 ‫راره ‪ = ۴‬بر وزن نازه ‪ .‬بمعنی راز‬
                                                             ‫تزديك بسبزوار‪ -‬ونام پادشاهزاده‌ای هم بوده‌است‬
                                                             ‫کوبند او را برادری بود که ری نام داشت هر‬
  ‫امت که بوشیده ۽ بنهان ولهفته واسرار (‪ )۱‬دل‬
                                          ‫باشد ‪.‬‬             ‫دو باتفاق شهری بنا کردند چون بانمام رسید‬
                                                             ‫دام‬
                                                               ‫هر‬‫ميان هردو در‪:‬سمیهٌآن مناقشه شد چه ک‬
 ‫راد یام‪ -‬با میم» بروزن موعنی بادبان‬
  ‫است که رازبانه‌باشد ومعرب‪.‬آن رازبالج ات ‪۵‬‬
                                                              ‫ان‬
                                                               ‫میخواستند کهمسمی بنام خود کنند‪ .‬بگزر‬
                                                             ‫آنزمان بجپت رفم منافثه شهر را بنام ری‬
‫از آدم عله اللام نقل کرده اند که هرکس از‬
                                                             ‫کردند و مردم شهر را بنام راز چنانچه حالالیز‬
 ‫اول‌حمل یعنی روزیکه آفتاب ببرح‌حمل می‌آید‬                   ‫میخوانند و اهل شهر را رازی‬       ‫شپر را ری‬
 ‫هرروز یك درم رازبانه بایکدرم دیگر فندسفوف‬
                                                                                              ‫مبگونشن‪۴ :‬‬
 ‫سازد و مداومت کند تا روزیکه آفتاب برج‬
 ‫سرطان آمد درین سه ماه قطمامر يض نشود وآن‬                              ‫ی‬ ‫وخرهن غلةٌ پاك نکرده گروایند ‪.‬‬
 ‫بوستالی و صحرابی و شامی میباشد » و رازبالة‬
 ‫شامی ایسون است ؛ و بضی کوبند الیسون‬                         ‫رار بان = بروزن بادبان بمعنی صاحب‬
 ‫رازبانة رومی‌است؛ وبعضی‌دیگر کوبند هردویکی‬                  ‫ویبزند کهسخن ارباب‬
                                                                              ‫وی رگال‬
                                                                                    ‫راز باشد ‪ -‬ک‬
                      ‫است وای‌ون است ‪#.‬‬                                  ‫اک را رن ان ران‬
‫وزن طای » بلغت زند‬        ‫=ر‬
                           ‫راس ‪ ۱‬ب‬                           ‫راز دل آب = کنابه از رطوبت‬
 ‫ویازند )‪ (+‬راه وحاده را گونند که بعر بی طریق‬
                                                             ‫وبرودئی بود که در جوهرآب است ‪ ۰‬وآن باعث‬
                             ‫وصراط خواند ‪4.‬‬
                                                             ‫بآرمدن ونموی نبانات میشود‪ -‬و عکسی را لیز‬
‫ارست ‪ -‬بروزن ماست ‪ ۰‬نقیض کج‬                                  ‫کون دکه درآب افتدب ومطلق‌رستنی ومیزشدلی‬
 ‫وضد دروخ باشد ‪ -‬ولام مقامی است‪-‬از موسیقی‪-‬‬                                      ‫و روبدنی را نیزگفته‌اید ‪۲‬‬

   ‫(‪)۲‬چك‪ :‬زند ویاژند‪.‬‬          ‫بنهان واسرار لهفته‪.‬‬           ‫)‪ (۱‬چك‪ :‬ینهان واسرار و نیقته؛ چش‪:‬‬


  ‫‏‪.lys blanc =¥‬‬           ‫‪ _۴‬وحه‌اشتفاق عاممانه‪ .‬ر کک‪:‬ری‪.‬‬                ‫‪ - ۱‬رك ‪ :‬رز رزیدن‪.‬‬
  ‫‪ 1‬ت بپلوی‪ 52۲‬بمعنی‌راه‬            ‫رلك‪ :‬راز بانه‬   ‫=‬   ‫‏‪e‬‬      ‫‪.‬‬   ‫ز‬
                                                                    ‫ا‪:‬‬‫‪- ۴‬ررك‬         ‫(فر) «لك‪۲‬س ‪۷4۱۰‬‬
    ‫» عادل» کت(‬   ‫یوج‬    ‫(هستقیم؛‬   ‫بهلوی)‪52۲‬‬       ‫‪5‬‬           ‫‪٩‬ے‪۱۹‬‏‬
                                                                    ‫رگ‬‫«بونکر ‪٥۰٠۰‬‏ «امشق ‪ ۷۰۸‬ل‪.‬ی‪۰‬ب‪۱‬‬
  ‫دوکلمة ابرانی باستان درین لفت جمم شده‪ 81015۵۲ -۱ :‬ازرشهٌ‪( 23۲-‬راست ودرست کردن »‬
  ‫مرتب کردن)‪ ( ۲-48۵۲ .‬حاضر ومهیا شده‪ .‬تدارك دیده » مرب ) از رة ‪ ۶ 1]02۲-‬بارتولمه‬
  ‫ربکف ‪ ۳۹۱۰‬هندی باستان ‪ . 100۸۲‬استی ‪ 052۲‬ا‪ 58۲۰‬کردیع‬          ‫‪ ۶۵‬و ‪ ۶ ۰۲6۱۰‬نی‬
  ‫اورامانی ‪« 52۲‬ك‪.‬‬      ‫و اففالیم و بلوچیع ‪ . ۸58۲‬وخی ‪ , 52۲‬سربکلی اکلا] « اسذق ‪۳۰۰۰‬‬
   ‫‪۸۲٩‬‏‬   ‫حه‬
           ‫صیهفدر‬
                ‫بق‬
```


## [2026-09-14T01:16:06.940Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==156' HRN.txt | head -40; echo \"=== grep rāz/Geheimnis\"; grep -n \"Geheimnis\" HRN.txt | head -20",
 "description": "Horn p.134"
}
```


### [2026-09-14T01:16:08.205Z] TOOL RESULT

```
- 134 —
R
600. -m, zur Bezeichnung des Objekts dienende Partikel,
rdl * wegen', beräl^ ez her dl.
ap. rad' in -radiy Vegen* ; phlv. ra%^ aj rai (Gemme,
ZDMG. 44, 676 No. 141).
aty. lar^ lara (beim Dativ); kurd. ärai *für (H.-
Sch.) ; oss. rad ^Ordnung, Reihe (209) (?).
Aus der ursprünglichen Bedeutung *für, wegen, was
anlangt* erklärt sich auch das Vorkommen von rä
vor dem Nominativ. In Vis und Rämln ist dieser
Gebrauch nicht selten, z. B. gleich im ersten Verse,
ferner S. 16 Vers 7 b v. u., 73 Vers 2 u. ö. Vergl.
auch Salemann, Litbl. f. or. Phil. II, 84.
Einzelne Redensarten siehe noch bei Salemann-
Shukovski, Neup. Gramm. § 13 b Anm. 1, sowie
die syntaktische Bemerkung bei Rückert, ZDMG.
8, 258, 264.
601. räd 'freigebig.
aw. vergl. aräiti-^); ai. rati- Villig zu geben'; phlv.
rat (auch Titel, vergl. Hörn, Mitteilungen, Heft IV,
27), ratth.
602. räz geheim, verborgen'.
aw. razah' (vd. 8, 97); phlv. raz^ vergl. Qaovav^
Chron. Pasch. I, 730, 14, 15 (de Lagard e, Ges. Abh.
192) ; skr. rdhas- 'Einsamkeit, Geheimniss'.
603. rast recht, wahr, rechts*, 7'äste^ rastl, rästln (Sahn. I,
123 Vers 1070).
ap. rasta- recht, richtig'; aw. rasta--, phlv. rast,
rastlh\ ai. raddhd-,
oss. d. t. rast^ rasf (212).
LW. kurd. af/. bei. (222) rast; wa./. rast, ssiv, rüst.
604. räm *Ruhe; fröhlich, heiter, ramis, ramist (Lex.).
ap. vergl. Äriya]ramna', *Apia]^oi/nvt]g; aw. raman-
^) Aw. rati- (yt. 10, 45) ist = ai. arati- (Bartholomae, Altiran.
Verbum 194, BB. 17, 111 Anm., G;oldnor, KZ. 25,520 Note 61).
=== grep rāz/Geheimnis
5398:192) ; skr. rdhas- 'Einsamkeit, Geheimniss'.
```


## [2026-09-14T01:16:17.077Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HUB\"; grep -n \"räz\\|rāz\\|razah\\|rahati\\|rastan\\|rahad\" HUB.txt | head -20",
 "description": "Grep Hübschmann"
}
```


### [2026-09-14T01:16:17.129Z] TOOL RESULT

```
=== HUB
2302:asparez, aspar^ (g^n. asparisi)? Np. rastan gehort
5620:phi. paz. vtrayam, inf. virastan^) zurichten Min. Gl. 216,
5628:*) Vgl. pairastan § 92, b.— 160 —
6454:ander vorkommen.^) Vgl. afrCistan, avrastan (zd. aiwi -f
6775:pairastan schmiicken, anordnen', arm. patrast 'bereit',
6805:^manifest' Shk. 263. Daneben aber padrastan *to prepare,
7293:179 (zu sprechen sahrastan), arm. sahastan Hauptstadt',
10238:afrastan 16.
```


## [2026-09-14T01:16:18.277Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD && awk 'BEGIN{RS=\"\\f\"} NR==60' FFD_pages.txt | head -40",
 "description": "FFD page 55"
}
```


### [2026-09-14T01:16:19.418Z] TOOL RESULT

```
[pdf page 60]
ماده‌های ماضی و مضارع فارسی دری نا ۵۵
بین < فارسی میانه ۷۷68 + ایرانی باستان ۹/۵۱-3* 23 نشانه‌ای بوده که برای ساختن
مادهٌ مضارع از ريشه به کار می‌رفته است. ريشةٌ ۷۵ به معنی «دیدن» است.
«دیدن» و «بین» چون «آمدن) و «آی» دو ریشه‌ای است.
رامیدن
۰ آرامیدن
راندن
راندن مخفف «روانیدن» است و آن فعل واداری از «رفتن» است. در فارسی دری
فعل واداری از مادةٌ مضارع + «ان» و «(عن» ساخته می‌شود. «۵۶) در متون کهن آمده
مادهٌ ماضی فعل واداری هميشه جعلی است و به جای «انید» ممکن است («اند» به
کار رود.
ربودن
ربود + فارسی میانه 1010.
ربای + فارسی میانه 1003 +« ایرانی باستان ۵رقم۳*, 2رقم" از ۳803: اسم
به‌معنی «ربودن» و 8نشانه‌ای که برای ساختن مادةٌ جعلی از اسم به کار می‌رفته» ساخته
شده است.
مادهٌ ماضی باید «رّفت» < فارسی میانه ۳۵۶۲ < آیرانی باستان ۵۵ می آمد. به قیاس
با 573 و 5736 «ربود» آمده است.
3 از ریشةٌ 780 به معنی «ربودن» و پسوند 3 ساخته شده است.
رّستن
رّست + فارسی میانه 7291 < فارسی باستان ۴۶۵۶-1۵ برای 1۵ -> آراست. 724
صورت اصلی 78 است» ‎٩‏ پیش از 1به 9بدل شده است.
```


## [2026-09-14T01:16:26.643Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD && awk 'BEGIN{RS=\"\\f\"} NR==61' FFD_pages.txt | head -40; echo \"#### search رهیدن\"; grep -n \"رهیدن\\|رَه\\b\\|رهید\" FFD_pages.txt | head -20",
 "description": "FFD page 56 and رهیدن"
}
```


### [2026-09-14T01:16:27.898Z] TOOL RESULT

```
[pdf page 61]
ان 111 0 اه ی ی ار ان نار اه
ره ج فارسی میانه ۲۵10 ج فارسی باستان ۹۳۵-۵ برای 2 -> آرای. اس <ایرانی
باستان 182: گریختن.
رُستن
رُست < فارسی میانه 7۵81 < ایرانی باستان ۳09-1۵*. برای 1۵ > آراست. ۲۳4
صورت اصلی 709 است. 4 پیش از ۲ به 8 بدل شده است. 104 صورت ضعیف 7800 است
و ريشةٌ 1304 به معنی «رشد کردن» است.
روی < فارسی میانه 70 < ایرانی باستان 7۵4-۵*. برای 2 > آرای.
رسیدن
رسید < فارسی میانه 72914. مادةٌ ماضی جعلی است. از ماده مضارع ساخته شده
است.
رس < فارسی میانه 7۵8 + ایرانی باستان ۲۵-۹-۵*. برای ۵ -> آرای. 8نشانه‌ای بوده که
برای ساختن‌مادء آغازی‌از ريشه‌به کار می‌رفته‌است.ريشةٌ ۲3به‌معنی «حرکت‌کردن» است.
«پذیره» بازماندةٌ 0207788 فارسی میانه است و ربطی به «پذیرفتن» ندارد. ۳02477۸8
بازماندةٌ 0211-78-6۵* ایرانی باستان است. 081 پیشوند و 1۵ پسوند و 73 ريشه است.
رشتن
«ریس) ماده مضارع «رشتن» است. ظاهراً «رشتن»» «ریس» از ربشةٌ 5۵12" به معنی
«بافتن» آمده است» به شرح زیر:
رشت < ایرانی باستان 718-1۵*. برای 1۸ -> آراست. ۲2 صورت اصلی قلة است» 7
پیش از 1 به 5 بدل شده است. 717 صورت ضعیف ريشه است.
ریس < ایرانی باستان 112-2*.برای 2 > آرای.در اینجا 2ب بدل شده است. > لشتن.
۱ رقتن
رقت < فارسی میانه 71 « ایرانی باستان ۴۲۵۳4۵. برای 12 -> آراست. 720 صورت

#### search رهیدن
```


## [2026-09-14T01:16:45.796Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && grep -n \"راز\" ARY_pages.txt | head -10; echo \"=== latin index RAZ\"; grep -n \"RAZ\\|RAD\\|RAH\" ARY_latin_index_pages.txt | head -20",
 "description": "Grep Aryanpur"
}
```


### [2026-09-14T01:16:45.865Z] TOOL RESULT

```
331:1089 ۲57۸716) نشان می‌دهد که سفید پوست و «دراز سره (311۸31ه0011017028) از
701:و تپه‌های کوچکی بر فراز آنها قرار دارد. در درون آنها استخوان انسان و اسب و گهگاه اجاقی و اسلحه
1267:فقفط‌گامی در این سفر دراز و پر شگفتی است.
1376:راز اک فارسی با واژه‌های انگلیسی ۸۸01 و آلمانی کهن 31۸3/۸ و هلندی
1986:ساسکریت رازه اد سا پرتغالی "(۳0877010832): (شاید) :۹ ۱7 :۰.۹8۱
2288:رش» زش. آرش (یکان قدیمی برای سنجش دراز) / ۸۱
2998:انگلیسی (0ل8ا8(/0): لاد راز ۵ ((81805) 3
3113:انگلیس یکهن (5ا20/0 ۰:0۵ 88020 برهان قاطم + رازن دروم
3394:۸ / برازیدن» برازء برازندگی
3412:آلمانی (/0270/۸2): راز نا پسگشت‌ها ات دا
=== latin index RAZ
605:(SUTRA) 117.0 y(BRAHMANS)thilasl yp y(VEDAS) cla yx nape De 5 ts Le
943:VAISYA tlnyy 9 (3L,s& >) KASHATRIVA ih sLisy 9 (3 sly) BRAHMAN
1397:RATAN ARADH, -RADH —«(AVESTAN) pl 3\
1399:RADAN, (OLD ENGLISH) oS gS! RADHNOTI, — (SANSKRIT) cy Suse
1400:REDAN, RED RAHYATI, RADH- esa x
1402:(TIL)RADE DANISH) Sails GAREDAN, REDAN (GOTHIC) eng
1403:RADEN (DUTCH) fiche (OLD SCANDINAVIAN) :pSS-e\
1404:(OLD CHURCH SLAVIC) p53 +l RADHA
1405:RADITI OLD HIGH GERMAN) iS galt
1409:REFERENCES both, RADIETE (RUSSIAN) 525,
1410:POKORNY, ——Ss=S—*~=<CS~S~S*~«~ OO RADIT CZECH) Sor
1411:BARNHART: (READ) 891 RADIT (SLOVAK) f\gLel
1412:| MACKENZIE: (ADORN) 101 IMMRADIM (OLD IRISH) 45 545)
2159:RAD :(DUTCH) goska RATHO, RATHA —:(AVESTAN) (gl 3!
2171:ONIONS: (ROTA) 773 RAD HAGERMAN) JT
2172:SKEAT: (RET) 757 RADOR, (OLD ENGLISH) nf g-J&:\
2529:Id ger iebGoby ZAHIAR, ZAHOR, TRAHAN
2703:(OLD HIGH GERMAN) yf gist UDRAS, UDRAH (SANSKRIT) 2 Si
2980:‘MACKENZIE: 102 BRAZD (uLEY(SPANISH) colslyl
3267:BORST (DUTCH) sola VARANGH, VARAH
```


## [2026-09-14T01:16:51.764Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && sed -n '1368,1382p' ARY_pages.txt; echo \"=== pdf tag\"; awk 'NR<=1376 && /\\[pdf page/' ARY_pages.txt | tail -2",
 "description": "Aryanpur راز context"
}
```


### [2026-09-14T01:16:52.912Z] TOOL RESULT

```
۵- واژه‌ی فارسی «فرار؛ با واژه‌های انگلیسی ۳1.88 و آلمانی ۳1.137 و دانمارکی اس
78 (از واجریشه‌ی هند و اروپایی ۶181716" - 837 :۳01۳0379) همسانی‌های جالبی
دارد ولی هیچکدام از پسگشت‌های در دسترس من اشاره‌ای همریشه‌های ایرانی و سانسکریت این
واژه‌ها نمی‌کنند. آیا میان این واژه‌ها خویشی وجود دارد؟
[pdf page 49]
۰ / ریشه‌های هندو اروپایی زبان فارسی

راز اک فارسی با واژه‌های انگلیسی ۸۸01 و آلمانی کهن 31۸3/۸ و هلندی
۸۸۵ همسانی دارد ولی واجریشه‌ی هند و اروپایی این واژه‌ها هنوز تعیین نشده است.

۳- واژه‌ی فارسی «پیشاب» با واژه‌های انگلیسی ۳188 و آلمانی ۳188327 و دانمارکی 818 و
هلندی 81851207 و نروژی 2159 همسانی نسبی دارد ولی و اجریشه‌ی هند و اروپایی آنها لوع:,
نیست وگفته می‌شود که همه‌ی آنها «نامآواء (07701/1۸702070) هستند.

=== pdf tag
[pdf page 48]
[pdf page 49]
```


## [2026-09-14T01:17:03.558Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"رهیدن\\|رَستن\\|رستگار\" MON_part1.txt MON_part2.txt 2>/dev/null | head -10; echo \"=== raz\"; grep -cn \"راز\" MON_part1.txt MON_part2.txt 2>/dev/null",
 "description": "Grep Mo'in Farhang"
}
```


### [2026-09-14T01:17:03.721Z] TOOL RESULT

```
MON_part1.txt:697:راستن» | -رهیدن» آ -وردن؛ ۲ -شسودن. 
MON_part1.txt:15223:افلح: 0 (ع.] (ص تفضد.) رستگار تر. 
MON_part1.txt:58566:رستگاری» خلاص. 
MON_part1.txt:60449:درستگار فرهنگ فارسی معین ۰۹" 
MON_part1.txt:60473:درستگاری» صحت عمل. انتظام نظلم و 
MON_part1.txt:67317:رستگار 
MON_part1.txt:67326:نجات» رهایی. نور رستگاری: در میان 
MON_part1.txt:67329:طلب امداد که آن را «نور رستگاری؛ 
MON_part1.txt:67333:رستگاری است.» 
MON_part1.txt:67336:رسستن: 5-407« [- رهیدن] (مسصل.) 
=== raz
MON_part2.txt:411
MON_part1.txt:554
```


## [2026-09-14T01:17:07.685Z] TOOL CALL #47: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%B1%D8%A7%D8%B2' --note 'page 416, root Redh/Regh, node 4: Persian raz secret etymology' 2>&1 | tail -5; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%B1%D9%87%DB%8C%D8%AF%D9%86' --note 'page 416, node 2: Persian rahidan escape etymology' 2>&1 | tail -5; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%B1%D8%B3%D8%AA%D9%86' --note 'page 416, node 2: Persian rastan escape etymology' 2>&1 | tail -5",
 "description": "Archive Wiktionary pages"
}
```


### [2026-09-14T01:17:10.396Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/6a4b3b3748e98d33.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cf6757288e4b8aa2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4bccb5fbf2b7d52c.txt
```


## [2026-09-14T01:17:13.322Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 6a4b3b3748e98d33 cf6757288e4b8aa2 4bccb5fbf2b7d52c; do echo \"##### $f\"; grep -n -A15 -i \"etymology\" $f.txt | head -50; done",
 "description": "Read archived Wiktionary pages"
}
```


### [2026-09-14T01:17:14.442Z] TOOL RESULT

```
##### 6a4b3b3748e98d33
62: Etymology 1 
63-
64- 1.1.1 
65- Noun 
66-
67- 1.1.1.1 
68- Descendants 
69-
70- 1.2 
71: Etymology 2 
72-
73- 1.2.1 
74- Noun 
75-
76- 2 
77- Urdu 
78-
79- Toggle Urdu subsection 
80-
81- 2.1 
82: Etymology 
83-
84- 2.2 
85- Pronunciation 
86-
87- 2.3 
88- Noun 
89-
90- 2.4 
91- Adjective 
92-
93- 2.5 
94- References 
95-
96- 2.6 
97- Further reading 
--
105: Etymology 
106-
107- 3.2 
108- Noun 
109-
110- Toggle the table of contents 
111-
112- راز 
113-
114- 16 languages 
115-
116- العربية 
117- Azərbaycanca 
##### cf6757288e4b8aa2
##### 4bccb5fbf2b7d52c
62: Etymology 1 
63-
64- 1.1.1 
65- Pronunciation 
66-
67- 1.1.2 
68- Verb 
69-
70- 1.1.2.1 
71- Conjugation 
72-
73- 1.1.2.2 
74- Derived terms 
75-
76- 1.1.3 
77- References 
--
80: Etymology 2 
81-
82- 1.2.1 
83- Pronunciation 
84-
85- 1.2.2 
86- Verb 
87-
88- 1.2.2.1 
89- Usage notes 
90-
91- 1.2.2.2 
92- Conjugation 
93-
94- 1.2.2.3 
95- Related terms 
--
176: Etymology 1
177- [ edit ] 
178-
179- From Proto-Iranian *raz- ( “ to leave, escape (one's notice) ” ) , related to Proto-Indo-Iranian *raȷ́ʰ- ( “ to abandon ” ) . Cognate with Sanskrit रहति ( rahati , “ to abandon ” ) and रहस्य ( rahasya , “ mystery ” ) ; see the latter for more.
180-
181- Pronunciation
182- [ edit ] 
183-
184- ( Classical Persian ) IPA ( key ) : /ras.ˈtan/ 
185-
186- ( Dari, formal ) IPA ( key ) : [räs.t̪ʰán] 
187-
188- ( Dari, formal ) IPA ( key ) : [räs.t̪ʰán] 
189- ( Kabuli ) IPA ( key ) : [räs.t̪ʰán] 
190-
191- ( Hazaragi ) IPA ( key ) : [räs.t̪ʰán]
```


## [2026-09-14T01:17:20.128Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"### raz page persian section\"; sed -n '150,260p' 6a4b3b3748e98d33.txt; echo \"### rahidan file head\"; head -40 cf6757288e4b8aa2.txt",
 "description": "Read raz and rahidan pages"
}
```


### [2026-09-14T01:17:20.190Z] TOOL RESULT

```
### raz page persian section
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

 See also: زار 

 Persian
 [ edit ] 

 Etymology 1
 [ edit ] 

 From Middle Persian lʾc ( rāz , “ secret, mystery ” ) , from Old Persian *rāzah , from Proto-Indo-Iranian *raȷ́ʰ- ( “ secret, mystery; to abandon ” ) . Related to رستن ( rastan , “ set free, leave, escape ” ) , and رها ( rahâ , “ free, liberated ” ) .

 Cognates with Parthian 𐫡𐫀𐫉 ( rʾz /⁠rāz⁠/ ) , and Sanskrit रहस्य ( rahasya , “ secret, mystery, clandestine ” ) .

 Also compare Old Armenian երազ ( eraz ) , Imperial Aramaic 𐡀𐡓𐡆𐡀 ( ʾrzʾ , “ mystery ” ) , Hebrew רָז ( rāz ) , Classical Syriac ܐܪܙܐ ( ʾərāzā ) , Iranian borrowings.

 Noun
 [ edit ] 

 Dari

 راز 

 Iranian Persian

 Tajik

 роз 

 راز • ( rāz / râz ) ( plural رازها ( rāz-hā / râz-hâ ) , Tajik spelling роз ) 

 secret 

 mystery 

 Descendants
 [ edit ] 

 → Punjabi: 
 Gurmukhi script: ਰਾਜ਼ ( rāz ) 
 Shahmukhi script: راز ( rāz ) 

 Etymology 2
 [ edit ] 

 Perhaps from Proto-Indo-Iranian *Hrā́ćš .

 Noun
 [ edit ] 

 Dari

 راز 

 Iranian Persian

 Tajik

 роз 

 راز • ( rāz / râz ) ( plural رازها ( rāz-hā / râz-hâ ) , or رازان ( rāzān / râzân ) , Tajik spelling роз ) 

 hornet 

 bee 

 Urdu
 [ edit ] 

 Etymology
 [ edit ] 

 Borrowed from Classical Persian رَاز ( rāz ) . First attested in c. 1636 as Middle Hindi راز ( raz ) . [ 1 ] 

 Pronunciation
 [ edit ] 

 ( Standard Urdu ) IPA ( key ) : /ɾɑːz/ 
### rahidan file head
URL: https://en.wiktionary.org/wiki/%D8%B1%D9%87%DB%8C%D8%AF%D9%86
FETCHED: 2026-09-14T01:17:09Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found
```


## [2026-09-14T01:17:38.902Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && pdftoppm -f 416 -l 416 -r 200 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg416-v && ls -la pg416-v.png",
 "description": "Render PDF page 416"
}
```


### [2026-09-14T01:17:40.506Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 39289 Sep 13 21:17 pg416-v.png
```


## [2026-09-14T01:17:42.480Z] TOOL CALL #51: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg416-v.png"
}
```


### [2026-09-14T01:17:43.001Z] TOOL RESULT

```

```


## [2026-09-14T01:17:42.996Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-14T01:17:52.811Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD\"; grep -n \"^redh\\|^regh\\|redh-\\|reĝh\" AHD_watkins1985.txt | head -10; echo \"=== WLD band3 index\"; grep -n \"rahati\\|razah\" WLD_band3.txt incoming/WLD/WLD_Bd2_pages.txt 2>/dev/null | head -10; echo \"=== IEC\"; grep -n \"redh-\\|reĝh-\\|rahati\" IEC.txt | head -10",
 "description": "Grep AHD, Walde-Pokorny, Mann"
}
```


### [2026-09-14T01:17:52.912Z] TOOL RESULT

```
=== AHD
335:bher-3. Bright, brown. 1. Suffixed variant form *bhri-no- in Germanic *briinaz in: a. Old English briin, brown: BROWN; b. Middle Dutch bruun (> Dutch bruin), brown: BRUIN; Cc. Old French brun, shining, brown: BRUNET, BURNET, BURNISH. 2. Reduplicated form *bhibhru-, *bhebhru-, “the brown animal,” beaver, in Germanic *bebruz in Old English be(o)for, beaver: BEAVER!. 3. Ger- manic *ber6, “the brown animal,” bear, in Old English bera, bear: BEAR?. 4. Germanic *bernuz in Old Norse bjérn (stem ber-), bear: BERSERKER. [Pok. 5. bher- 136.] bher-4. To cook, bake. Extended root form *bhrig- in Latin frigere, to roast, fry: FRY}. [Pok. 6. bher- 137.] bherdh-. To cut. 1. Zero-grade form *bhrdh- in Germanic *burd-, plank, board, table, in: a. Old English bord, board: BOARD; STARBOARD; b. Old Norse bordh (> Swedish bord), board, table: SMORGASBORD; c. Old French borde, hut, and bort, border: BORDELLO, BORDER. 2. Possibly Latin forfex, a pair of scissors: FORFICATE. [Pok. bheredh- 138.]
526:TRANSFUSE. II. Extended form *gheus-. 1. Germanic zero-grade form *gus- in: a. suffixed form *gustiz in Old Norse gustr, a cold blast of wind: cusT!; b. Icelandic gusa, to gush, perhaps akin to Middle English gushen, to gush: GUSH. 2. Germanic suffixed o-grade form *gausjan in Old Norse geysa, to gush: GEYSER. III. Suffixed form *gheu-ti- in Latin fatilis, “(of a vessel) easily emptied, leaky,” hence untrustworthy, useless: FUTILE. IV. Basic form *gheu- in Greek khein, to pour: CHOANA, CHYLE, (CHYME); CHOANOCYTE, ECCHYMOSIS, PARENCHYMA. [Pok. gheu- 447.] ghéu-. To yawn, gape. Compare ghai-. 1. Germanic suffixed form g6-ma- in Old English goma, palate, jaw: GuM?, 2. Variant form *ghau- in Greek khaos, chasm, empty space, chaos: CHAOS, GAS. [Pok. ghéu- 449.] gheu(e)-. To call, invoke. Suffixed zero-grade form *ghu-to-, “the invoked,” god, in Germanic *gudam, god, in: a. Old English god, god: Gop; b. Germanic *gud-igaz, possessed by a god, in Old English gydig, gidig, possessed, insane: GIDDY. [Pok. ghau- 413.] gh6. Behind, after. Slavic *za in Russian za, by, to: SASTRUGA. [Pok. 26 451.] ghos-ti-. Stranger, guest, host; properly “someone with whom one has reciprocal duties of hospitality.” 1. Basic form *ghos-ti- in: a. Germanic *gastiz in Old Norse gestr, guest: GUEST; b. Latin hostis, enemy (< stranger): HOST?, (HOSTILE). 2. Compound “ghos-pot-, *ghos-po(d)-, “guest-master,” one who symbolizes the relationship of reciprocal obligation (*pot-, master; see poti-), in Latin hospes (stem hospit-), host, guest, stranger: (HOSPICE), (HOSPITAL), (HOSPITALITY), HOST!, (HOSTAGE), (HOSTEL), (HOSTLER). See also xenos. [Pok. ghosti-s 453.] ghow-é-. To honor, revere, worship. 1. Germanic *gaw6n in Old Norse gd, to heed: GAWK. 2. Basic form *ghow-é- in Latin favére, to favor, be favorable: FAVOR, (FAVOR- ITE). [Pok. ghou(é)- 453.] ghré-. To grow, become green. Contracted from “ghreo-. 1. O-grade form “ghré- in Germanic *grd(w)an in Old English gréwan, to grow: GROW. 2. Suffixed o-grade form *ghro-nyo- in Germanic *grénjaz, green, in Old English gréne, green: GREEN. 3. Suffixed zero-grade form *“ghro-so- in Germanic *grasam, grass, in Old English grees, grass: GRASS. [Pok. ghré- 454.] ghrebh-'. To seize, reach. 1. Zero-grade form *ghrbh- in Sanskrit grbhndati, grhndati, he seizes: SATYAGRAHA. 2. Parallel (imitative) Germanic creations with base *grab-, *grap- in: a. Middle English graspen, to grasp: GRASP; b. Middle Dutch and Middle Low German grab- ben, to seize: GRAB. [Pok. 1. ghrebh- 455.] ghrebh-?. To dig, bury, scratch. 1. O-grade form “ghrobh- in: a. Germanic *graban in (i) Old English grafan, to dig, engrave, scratch, carve: GRAVE3; (EN- GRAVE) (ii) Old High German graban, to dig: GRABEN (iii) Old French graver, to engrave: GRAVURE; b. Germanic *grabam in Old English grzf, trench, grave: GRAVE}. 2. Germanic *grub(byan (with secondary ablaut) in Old English *grybban (> Middle English grubben), to dig: GRUB. 3. Germanic *gr6b6 in Middle Dutch groeve, ditch: GROOVE. 4. Perhaps Germanic *greub- in Low German greven, fibrous refuse of tallow: GREAVES. [Pok. 2. ghrebh- 455.] ghredh-. To walk, go. Suffixed zero-grade form ghrdh-yo- in: a. Latin gradi (past participle gressus), to walk, go: GRESSORIAL; AGGRESS, CONGRESS, DEGRESSION, DI- GRESS, EGRESS, INGRESS, PLANTIGRADE, PROGRESS, RE- GRESS, RETROGRESS, TRANSGRESS; b. Latin gradus (< deverbative *grad-u-), step, stage, degree, rank: GRADE; CENTIGRADE, DEGRADE, DEGREE, RETROGRADE. [Pok. ghredh- 456.] ghréi-. To rub. A derivative of gher-4. 1. Germanic *gris-, to frighten (< “to grate on the mind”), in Old English grislic, terrifying: GRISLY. 2. Germanic *grim-, smear, in Middle Dutch grime, grime, akin to the source of Middle English grime, grime: GRIME. 3. Extended form *ghris-
1218:AEDILE aidh- AEGIS aig- AENEOUS ayes- AEOLIPILE pulé AEPYORNIS OrF- AERIAL wer-2 AERO- wer-2 AEROBE gWei- AERODYNE deu-2 AERONAUT nau-2 AESIR ansu- AESTHETIC au-5 AESTIVAL aidh- AETHER aidh- AFFABLE bha-2 AFFAIR dhé-1 AFFECT! dhé-1 AFFECT? dhé-1 AFFECTION dhé-1 AFFERENT bher-1 AFFIANCE bheidh- AFFIANT bheidh- AFFIDAVIT bheldh- AFFILIATE dhé(i)- AFFIRM dher-2 AFFIX dhigy- AFFLATUS bhié-2 AFFLICT bhiig- AFFLUENT bhleu- AFFORD pert AFFOREST dhwer- AFFRAY  pri- AFFRICATE bhréi- AFFUSION gheu- AFTER apo- AFTERMATH mé-4 AGAIN gagina AGAINST gagina AGALACTIA melg- AGAPANTHUS andh- AGE aiw- AGENDUM ag- AGENT ag- AGERATUM gere-1 AGGLOMERATE gel-1 AGGLUTINATE gel-1 AGGRAVATE gWere-2 AGGREGATE ger-? AGGRESS ghredh- AGGRIEVE gWere-2 AGHAST gheis- AGILE ag-
1340:CELLA kel-2 CELLAR kel-2 CELLARER kel-2 CEMBALO keu-2, kleu-3 CEMENT kae-id- CEMETERY kei-1 CENACLE sker-1 -CENE_ ken-3 CENOBITE gWei-, kom CENOGENESIS ken-3 CENOTAPH dhembh-, ken-4 Cenozoic ken-3 CENSOR kens- CENSUS kens- CENT dekm CENTAL dekm CENTAVO dekm CENTENARIAN dekm CENTENARY dekm CENTENNIAL dekm CENTER kent- CENTESIMAL dekm CENTESIS kent- CENTI- dekm CENTIGRADE ghredh- CENTIME dekm CENTNER dekm CENTO kentho- CENTRIFUGAL bheug-'
1392:CONFOUND gheu- CONFRERE bhrater- CONFUSE gheu- CONFUTE bhau- CONGE mei-1 CONGEAL gel-3 CONGENER gene- CONGENIAL gene- CONGENITAL gene- CONGERIES gerere CONGEST gerere CONGLOBATE gel-1 CONGLOMERATE gel-1 CONGLUTINATE gel-1 CONGRATULATE gWera-3 CONGREGATE ger-! CONGRESS ghredh- CONGRUENT ghréu- CONIDIUM keni- CONIOSIS keni- CONJECTURE yé- CONJOIN yeug- CONJUGAL yeug- CONJUGATE yeug- CONJUNCT yeug- CONJURE yewes- CONNATE gene- CONNECT ned- CONNIVE kneig’h- CONNOISSEUR gn6- CONNOTE gné- CONNUBIAL sneubh- CONQUER quaerere CONQUIAN kom, kWo- CONSCIENCE skei- CONSCIOUS | skei- CONSCRIPT skribh- CONSECRATE sak- CONSENT sent- CONSEQUENT sekw-1 CONSERVE ser-1 CONSIDER sweid-1 CONSIGN sekw-1 CONSIST sta- CONSOCIATE sekw-1 CONSOLE! sel-2 CONSOLIDATE sol- CONSOLUTE leu-1 CONSONANT swen- CONSORT ser-3 CONSPICUOUS _ spek- CONSPIRE spirare CONSTABLE ei-1 CONSTANT sta- CONSTELLATION  ster-3 CONSTERNATE  ster-2 CONSTIPATE  steip- CONSTITUTE sta- CONSTRAIN | streig- CONSTRUCT  ster-2 CONSUETUDE s(w)e- CONSUME em- CONTACT tag- CONTAIN ten- CONTAMINATE tag- CONTEMPLATE tem- CONTEND ten- CONTEST trei- CONTEXT teks- CONTINUE ten- CONTORT terkw- CONTOUR tera-1 CONTRA- kom CONTRABAND bha-2 CONTRACT tragh- CONTRADICT deik- CONTRARY kom CONTRAST sta- CONTRAVENE gWa- CONTRITE tere-1 CONTRIVE trep-2 CONTROL ret- CONTROVERSY wer-3 CONTUSE (s)teu- CONVALESCE wal- CONVECTION wegh- CONVENE gWa- CONVENIENT gWa- CONVENT gWa- CONVENTICLE gWa- CONVENTION gWa- CONVERGE wer-3 CONVERSE! wer-3 CONVERT wer-3 CONVEX wegh- CONVEY wegh- CONVINCE weik-5 CONVIVIAL gWei- CONVOKE wekw-
1418:DEEP dheub- DEER dheu-! DEFACE dhé-1 DEFAME bha-2 DEFEASANCE dhé-1 DEFEAT dhé-1 DEFECT dhé-1 DEFEND gWhen-1 DEFENSE gWhen-1 DEFER! bher-1 DEFER? bher-1 DEFERVESCENCE bhreu-2 DEFIANCE bheldh- DEFICIENT _dhé-1 DEFILE! pu-2 DEFILE? gWhi- DEFLAGRATE bhel-1 DEFLATE bhlé-2 DEFLOWER bhel-3 DEFOLIATE bhel-3 DEFORCE bhergh-? DEFORM merph- DEFUNCT bheug-2 DEFY bheidh- DEGAGE wadh-1 DEGENERATE geno- DEGLUTINATE gel-1 DEGLUTITION gWel-3 DEGRADE ghredh- DEGREE ghredh- DEGRESSION ghredh- DEGUST geus- DEHISCE ghal- DEICIDE deiw- DEICTIC deik- DEIFIC delw- DEIGN dek-1 DEISM deiw- DEITY deiw- DEJECT yé- DELAINE wele-1 DELAY slég- DELEGATE leg-1 DELIBERATE [ithra DELINQUENT leikw- DELIQUESCE wileik- DELIRIUM leis-1 DELIVER leudh-2 DELL dhel- DELPHINIUM g¥elbh- DELUDE leid- DELUGE leu(@)- DELVE dhelbh- DEMAGOGUE ag-, da- DEMAND man-2 DEMARCATION merg- DEME da- DEMEAN! men-2 DEMEAN2 mei-1
1426:DIET? deiw- DIFFER bher-! DIFFICULTY dhé-1 DIFFIDENT bheidh- DIFFRACTION bhreg- DIFFUSE gheu- DIG dhigw- DIGEST gerere DIGIT deik- DIGNIFY dek-1 DIGNITY dek-1 DIGRESS ghredh- DIKE dhig¥- DILATE stela- DILATORY tela- DILIGENT leg-1 DILUTE leu(@)- DIME dekm DIMENSION mé-2 DIMER (s)mer-2 DIMINISH mei-2 DIMITY mei-4
1444:EGOIST eg EGOTISM EGREGIOUS ger-! EGRESS ghredh- EIDER &ti- EIDERDOWN dheu-! EIDETIC weid- EIDOLON weid- EIGHT oktd(u) EINKORN gre-no-, oi-no- EISTEDDFOD bheue-, sed-' EITHER kWo- EJACULATE yé- EJECT yé-
1565:GOAD ghei-1 GOAT ghaido- GOD gheu(e)- GODSEND sent- GOFFER webh- GOLD ghel-2 GOLIARD gWel-3 GOMPHOSIS gembh- -GON genu-! GONAD gene- GONFALON gWhen-1 GONIOMETER genu-1 GONIOMETRY genu-! GONION genu-! GONO- gena- coop ghedh- GOOSE! ghans- GORE! ghaiso- GORE? ghaiso- GORGE gWere-4 GORGET gWera-4 GORSE ghers- GOSHAWK ghans- GOSLING ghans- GOSPEL spel-3 GOSSIP s(w)e- GOUACHE akWa- GOWAN ghel-2 GRAB! ghrebh-1 GRABEN ghrebh-2 GRACE gWera-3 GRACKLE gera-2 GRADE ghredh- GRAFFITO gerbh- GRAIN gre-no- GRAM! § gerbh- GRAM? gre-no- -GRAM gerbh- GRAMA gras- GRAMINEOUS_ gras- GRAMMAR gerbh- GRAMPUS_peisk- GRANADILLA gfe-no- GRANARY gre-no- GRANDILOQUENCE tolkw- GRANGE gre-no- GRANITE gr@-no- GRANT kerd-1 GRANULE gre-no- GRAPE ger-2 GRAPH gerbh- -GRAPH gerbh- -GRAPHER gerbh- GRAPHIC gerbh- GRAPHITE gerbh- -GRAPHY gerbh- GRAPNEL ger-2 GRAPPA ger-2 GRAPPLE ger-2 GRASP ghrebh-1 GRAss_ ghré- GRATE! grat- GRATE? kert- GRATEFUL gWere-3 GRATIFY gWere-3 GRATIS gWera-3 GRATITUDE gWero-3 GRATUITY gWera-3 GRAUPEL kreup- GRAVE! ghrebh-2 GRAVE? gwWera-2 GRAVES ghrebh-2 GRAVEL ghréu- GRAVID gWera-2 GRAVURE ghrebh-2 GRAY gher-3 GRAYWACKE wegh-
1567:GREAT ghréu- GREAVES ghrebh-2 GREEDY gher-5 GREEN ghré- GREET gher-2 GREGARIOUS ger-1 GRENADE gre-no- GRESSORIAL ghredh- GREYHOUND gher-3 GRID kert- GRIDDLE kert- GRIDIRON kert- GRIEF gWera-2 GRIEVE gWere-2 GRIM ghrem- GRIMACE ghrem- GRIME ghréi- GRIND ghrendh- Grip! ghreib- GRIPE ghreib- GRIPPE ghreib- GRISAILLE gher-3 GRISEOUS gher-3 GRISETTE gher-3 GRISLY ghréi- GRISON gher-3 GRisT ghrendh- GRIT ghréu- GRIZZLE gher-3 GROAT ghréu- GROATS ghréu- GROCER gWres- GROOVE ghrebh-2 GROPE ghreib- GROSCHEN gWres- GROSS gWres- GROSSULARITE ger-2 GROSZ gWres-
=== WLD band3 index
=== IEC
1671:bhrodhos, à ‘ford, way’. See bhredh- OCS and com. Sl. brodü; Li. brádas, brada, beside bradüs 'fordable'; Latv. bradus (adj. *wading)
4898:(ghredh-, see ghréio, ghrés-)
17094:(srodh-, o-gde of type sredh- ‘run, flow, glide’, etc. O-gde in Gk. rhóthos, m. ‘plash of oars’; tar-rhóthos, m. ‘runner-up, assistant")
20035:ueredh- (uerdh-) 'seethe, boil, stir, rouse, rile, anger Gk. erétho, erethízo, v. ‘rile’; OCS vrézdo, vréditi, v. “harm, injure’; vréZdajo, -ati, v. id.; vrédü, m. ‘wound, sore, harm’; R veredit, v. “Tile? beside vèred, m. ‘boil, abscess’; Ukr. cf. veredlivyj ‘harmful’; Cz. cf. vřed, Pol. wrodek, m. ‘boil, sore; MHG wirt, m. ‘eddy in seg’. (But for Go. fra-wardjan; OE for-wierdan 'des- troy’; OHG *wartjan, werten ‘harm’, see uert-; uort-, in view of Go. fra-wairpan ‘perish’, etc. Li. cf. vérdu, inf. virti, Latv. verdu, virt, v. “boil” where -d- occurs only in the pres. t.)
```


## [2026-09-14T01:18:01.223Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"rahati\\|razah\" incoming/WLD/WLD_Bd1_pages.txt incoming/WLD/WLD_Bd2_pages.txt 2>/dev/null | head; echo \"=== SYN secret\"; grep -n -i \"secret\" SYN.txt | head -12",
 "description": "WLD and Buck greps"
}
```


### [2026-09-14T01:18:01.306Z] TOOL RESULT

```
incoming/WLD/WLD_Bd1_pages.txt:80686: vielleicht auch cech. z-drahati se „sich weigern", poln. wz-dragac siq „sich
=== SYN secret
10346:OE déagian, ME, NE dye, derivs. of OE déah, déag ‘dye’, NE dye, prob. : OE déagol, OHG tougal ‘secret, hidden’, but root connection and semantic se- quence dub. (see 17.36). Walde-P. 1.838.
11733:huis ‘door’ (Fr. @ huis clos ‘with Closed doors, secretly’). Walde-P. 1.168. Tr. nout-M. 716f. REW 6117.
20080:Ir. tadid; ChSl. tatt, ete.; Skt. tayu- (RY), also stayu-, Av. ta@yu-, Skt. stena-; ef. ChSl. taj ‘secretly’, tajiti ‘hide’, Grk. tnrdopar “be in want, bereft of’, Hitt. tdyézzi ‘steals’ (Sturtevant, Hitt. Gloss. 157).
21726:The majority of words for ‘hide’ are connected with others for ‘cover’ or ‘put away’ or ‘keep, preserve’, the notion of concealment being secondary, though dominant in an inherited group (below, 1). But this latter notion is inherent in a few that are connected with words for ‘steal’, ‘lie, deny’, or ‘secret’.
21750:Sw. délja (Dan. délge, ON dylja ‘keep secret, dissemble’), beside ON dul ‘con- cealment, disguise’, fr. the root in ON dvgl ‘delay’, OE dwala ‘error, doubt’, Goth. dwals ‘simple’, OE dol ‘silly’, etc. Semantic development of ‘conceal’ fr. ‘confuse, lead astray’. Falk Torp 177. Hellquist 171.
21752:OE. be-(ge-)diglian, OHG tougalen (Tat.) : OE déagol, digol, OHG tougol ‘secret’ (17.36).
21753:NE conceal (ME concele only ‘keep secret’) fr. OFr. conceler, Lat. concélare ‘hide carefully or completely’, cpd. of célare (above, 1).
22761:Av. Gighe: ‘deep’ and ‘secret, wonder- ful’, prob. : Grk. yin’ xolkwna is" badj- un, yovia. (Hesych.), ON kofi ‘hut, cell’, etc., fr. an extension of *geu- in numer- ous words with common notion of ‘bent, hollow’. Walde-P. 1.562. Barth. 524,
30148:| He UNDERSTAND 17.34 CuxEar, PLatn (to the Mind) WaT Know 17.35 OBSCURE 17,18 SEEM 17.36 Secret (adj.) 17,19 Ippa, NoTION 17.37 Sure, CERTAIN 7.21 WISE 17.38 EXpLaIn a9 FoouisH, STUPID 17.39 SonvE 1123 Insane, Map, ORazy 17.41 Invention, PurrosE 120 aa 17.42 Cause 11.95 MACH 17.43 Dovust (sb.) 1796 Purr 17.44 Suspicion 1197
31128:17.36 SECRET (adj.)
31137:7. Skt. gidha-, lit. ‘hidden, secret’ (17.36).
31138:NG Kpurrés, Nabpatos Goth. fulgins Lith. slaptas, pasléptas Lat Kpudos ON leyndr, leyniligr Lett.  slepens, sleps *  occultus, secrétus, Dan. hemmelig (Ignlig) ChSl.  tajinit It clandestinus Sw. hemlig (lénnlig) SCr. tajan Re arelo OE diegel (déagol), dierne Boh. tajny Sp, Secret ME _ secre(t), derne, dizel Pol. tajny es NE secret Russ. tajnyj hy lainic, ascuns, secret Du. geheim, heimelijk Skt.  gupta-, gii¢ha- Ni tnchlide, diam(a)ir OHG tougan, tougal Ay. guzra-, taya- Ww ‘nach, rinda MHG tougen, heimelich Ry, 2, “eet NHG geheim, heimlich
```


## [2026-09-14T01:18:04.247Z] TOOL CALL #54: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/raz-' --note 'page 416, root Redh/Regh: Proto-Iranian *raz- reconstruction' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%E0%A4%B0%E0%A4%B9%E0%A4%B8%E0%A5%8D%E0%A4%AF' --note 'page 416, node 4: Sanskrit rahasya secret, cognate of Persian raz' 2>&1 | tail -3",
 "description": "Fetch Proto-Iranian raz and Sanskrit rahasya"
}
```


### [2026-09-14T01:18:07.492Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/5e01c0d1b073c65c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5b06c29a6216e02c.txt
```


## [2026-09-14T01:18:10.994Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"### proto-iranian raz\"; grep -n -A12 \"Proto-Iranian\" 5e01c0d1b073c65c.txt | head -40; echo; echo \"### rahasya\"; grep -n -B2 -A10 \"Etymology\" 5b06c29a6216e02c.txt | sed -n '1,60p'",
 "description": "Read PIr raz and rahasya"
}
```


### [2026-09-14T01:18:11.071Z] TOOL RESULT

```
### proto-iranian raz
1:URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/raz-
2-FETCHED: 2026-09-14T01:18:05Z
3-STATUS: -1
4-TITLE: 
5-
6-FETCH FAILED: HTTP Error 404: Not Found

### rahasya
60-
61- 1.1 
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
83-
84- 2.1 
85: Etymology 
86-
87- 2.2 
88- Pronunciation 
89-
90- 2.3 
91- Noun 
92-
93- 2.3.1 
94- Declension 
95-
--
106-
107- 3.2 
108: Etymology 
109-
110- 3.3 
111- Pronunciation 
112-
113- 3.4 
114- Adjective 
115-
116- 3.4.1 
117- Declension 
118-
--
205- [ edit ] 
206-
207: Etymology
208- [ edit ] 
209-
210- Learned borrowing from Sanskrit रहस्य ( rahasya ) .
211-
212- Pronunciation
213- [ edit ] 
214-
215- ( Standard Hindi ) IPA ( key ) : /ɾə.ɦəs.jᵊ/ , [ɾɛ.ɦɛs.jᵊ] 
216-
217- Noun
--
280- [ edit ] 
281-
282: Etymology
283- [ edit ]
```


## [2026-09-14T01:18:13.415Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '282,330p' 5b06c29a6216e02c.txt",
 "description": "Sanskrit rahasya etymology"
}
```


### [2026-09-14T01:18:13.468Z] TOOL RESULT

```
 Etymology
 [ edit ] 

 Borrowed from Sanskrit रहस्य ( rahasya ) .

 Pronunciation
 [ edit ] 

 ' IPA ( key ) : /ɾə.ɦəs.jə/ , [ɾəs.jə] 

 Noun
 [ edit ] 

 रहस्य • ( rahasya )  n 

 secret 
 Synonym: गुपित ( gupit ) 

 mystery , suspence 
 Synonyms: गूढ ( gūḍh ) , गौडबंगाल ( gauḍbaṅgāl ) 

 Declension
 [ edit ] 

 Declension of रहस्य (neut cons-stem) 

 singular
 एकवचन 

 plural
 अनेकवचन 

 nominative
 प्रथमा 

 रहस्य 
 rahasya 

 रहस्ये , रहस्यं 
 rahasye, rahasya 

 oblique
 सामान्यरूप 

 रहस्या 
 rahasyā 

 रहस्यां- 
 rahasyā̃-
```


## [2026-09-14T01:18:19.696Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | tail -40",
 "description": "List remaining refs"
}
```


### [2026-09-14T01:18:19.749Z] TOOL RESULT

```
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
SKT_dli_revised.txt
SKT.txt
SNS_pages.txt
SNS.txt
SOD_pages.txt
SOD.txt
SPG_keilinschriften1881.txt
SYN.txt
TAD_pages.txt
TAD.txt
tessdata
TLM.txt
UNV.txt
WEB_vol1.txt
WLD_band3.txt
ZAP.txt
```


## [2026-09-14T01:18:25.497Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"راز\" MON_part1.txt | grep -n \"پهـ\\|پهلوی\\|سر\\b\" | head -20; echo \"=== rastan entry\"; sed -n '67336,67360p' MON_part1.txt",
 "description": "Mo'in entries"
}
```


### [2026-09-14T01:18:25.587Z] TOOL RESULT

```
3:848:سرازیر شدن: (عم.) تمایل شدید داشتن. 
4:1091:دسته‌دار که دارای لو له درازی است و سر 
5:1319:فوقانی سر آستین درازتر از قسمت تحتانی» 
6:1368:سرنگاه نتواند نشست» کسی که راز نگاه 
7:1457:سرازیری‌هایی که آب آنها به رودی 
11:2794:بند. شاد» فارغ. سرافراز. سالم» بیگزند. 
41:12750:اسرار: 7 (ع.] (.) ج. سر رازها؛ 
42:12751:نهانی‌ها؛ سرها. آشکار کردن رازها. 
56:14834:نازیدن. (امص.) فخر نازش» سرافرازی» ج. 
75:16683:سراز زدن. (امص) خسودداری. (فل) 
77:18434:صفیلی» پارازیت» سرخر. کسی که همنشینی 
80:19637:عوض. به حساب. همطراز» همسر » نظیر . 
96:21480:آشکار شدن راز» فاش شدن سر. 
137:26534:سرازبر گر دد. بهمن گردی: درات سار 
149:28690:باریک و دراز در ظرف آب سردی که زیر 
151:29383:پتک: (.) نوار یهن که سرازان و 
157:29889:سرازیر شود. 
160:30416:رازدار» سر نگهدار سریوش, امین» ساتره 
181:34691:مرازاورا رای سرت باه طرف مان 
189:38349:ریختن. فرودویدن. سرازیر شدن» بنشیب 
=== rastan entry
رسستن: 5-407« [- رهیدن] (مسصل.) 
(رست؛ رهد» خواهد رست» > رهنده» رهاء 
رسته» رهایش) رها شدن» نجات یافتن» 
رستی: «داع" [- روییدن] (مصل.) 
روییدن؛ نمو کردن بالیدن. 

رستنی: آ۲۵۶-۵ (ص. لا.) رو بیدنی» گیاه. 
رستنی‌ها: گیاهان» نباتات. 

رستوران: 0 (۰) جایی که در آن 
غدا و مشر وب نو شند. 

رسته: (۵-)۲9:۱۵ [- راسته - رزدقء معر.] 
(.) راسته, صف» ردهء قطار. دکان‌هایی که 
در یک ردیف در بازار واقع‌اند. بازار. 
کروهی از مردم دارای یک شغل؟ صنف 
(فره.) طرز» روش» طربقه» آیین» قاعده. 


۷۲ فرهنگک فارسی معین رسته 


رسته. (6-)18-:۲2 (امف.) رها شده» خللاص 
گشته نجات بافته.
```


## [2026-09-14T01:18:31.274Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^راز\\|راز: \\|راز‌\" MON_part1.txt | head -10; echo \"---\"; grep -n \"رازدار\" MON_part1.txt | head -3",
 "description": "Find Mo'in raz entry"
}
```


### [2026-09-14T01:18:31.374Z] TOOL RESULT

```
1605:آب‌طراز: 2-7 [<- آنب‌تراز] (امر.) 
7115:اثرطراز: 22 [ع. ف.] (افا. ص‌مر.) 
7703:احتراز: 22 [ع.] (مسص‌ل.) برهیز 
7896:احراز: ۳92 [ع.] (مص م.) فراهم آوردن» 
8959:ادب طراز: ۰-۵:52(ع. ف.] (افا. ص‌مر.) 
13598:اشمئراز: عقعصه ۰] (مص‌ل.) رمیدن» 
14923:افراز: 252 (- فراز] (ری. افرازیدن؛ ا.) 
21980:براز: 222« () چوبکی که کفشگران بین 
23040:براز: ۱327 [ع.] (ص.) کسی که انواع 
30416:رازدار» سر نگهدار سریوش, امین» ساتره 
---
24052:دوست نزدیکث» رازدار» یار ویژه. نزدیکك 
30416:رازدار» سر نگهدار سریوش, امین» ساتره 
65653:رازیان: ۲.05 (ص‌مر.) رازدار. کسی که
```


## [2026-09-14T01:18:33.426Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '65600,65660p' MON_part1.txt",
 "description": "Mo'in raz entry area"
}
```


### [2026-09-14T01:18:33.485Z] TOOL RESULT

```
(غم.) (سیا.) طرفدار اصلاحات کامل در 
امور کشور. (دس.) بخشی از یک کلمه که 
ینعی متیر استت :نمی که 
اتم‌هایی که به منزلة یکك عنصر در ترکیبات 
داخل شوند. (رض.) ریشگی. 

رادیو: ۷0 (.) دستگاه گیرنده که صوت 
را از فواصل دور ضبط و پخش می‌کند. رایو 


۴ ۷ فرهنگ فارسی معین رادیو آکتیو 


باتری: رادیویی که به وسیلة باطری بکا 
افتد. رایو برقی (الکتریکی): رادیویی که به 
وسیلة برق بکار افتد. 

رادیوا کتیو: ۲-۲ (امر.) جسمی که 
دارای تشعشعات اتمی (اشعةٌ آلفا» بتا و گاما) 
باشد مانند اورانیوم» توریوم و رادیوم. 
رادیو] کتیویته: ۲-6 (امر .) تشعشع و 
انتشار خودبجود اشعه از جانب بعضی مواد 
شیمیایی مانند اکتینیو م» اورانیوم» پلونیوم» 
توریوم» رادیوم و غیره. 

رادیو تراپی: آ۱6۲30-.۲ (امر.) (یز.) معالحة 
بعض امراض به وسبلة اث شم ایکس (۱6) 

راد یوگر افی: آ721»-.» (امر.) پر تونگاری. 
رادیوگرامز ۲۰-۲ (امر .) تلگرامی که ره 
وس له تلگران بسی سیم مخابره شود. 
دستگاهی که هم شامل رادیو است و هم 
گرامافون. 

رادیولگ: ۲.82 (امر.) بر توشناس» 
رادیولوژیست. 

رادیولوژی: ۰.09 (امر.) پر توشناسی. 
رادیو ۵ 007 (ا.) (شیم.) عنصری است 
طبیعی و کمیاب و پرقیمت» دارای تشعشعی 
خاص که در ۱۸۹۸ به وسلهة مادام کوری و 
شوهرش در معادن اورانیوم کشف گردیده. 
این عنصر جسمی است سفد رنگ» 
درخشنده (در تاریکی مانند چراغ 
می‌درخشد) و موجد حرارت. 

راز: 22 (- رازه] (.) مطلب پوشیده» امر 
ینهان» سر. 

راز: ۶2 [- رز] (.) رنگ لون. 

راز: 22: [- مسعر. راز] (.) یکی از آلات 
بنایان ج. رازه (لسان العرب). گلکار» طیان. 
رازیان: ۲.05 (ص‌مر.) رازدار. کسی که 
عرایض حاجتمندان را به عرض شاه و امیر 
می‌رسانید. 

رازق: 2 (ع.] (اف) روزی دهنده؛ 


روزی رسان (صفت خدای متعادل).
```


## [2026-09-14T01:19:33.792Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"rahad\\|rastan\\|rihad\\|'frei'\" HRN.txt | head -20; echo \"=== HUB rastan\"; grep -n \"rastan\\b\" HUB.txt | head",
 "description": "Horn/Hübschmann for rastan"
}
```


### [2026-09-14T01:19:33.868Z] TOOL RESULT

```
4713:(188)), vergl. arm. LW. darastan 'Garten'; ai. därtt-
5427:Gehört hierher auch np. reste^i (phlv. rastan, Men.),
10336:65. davärastan 'laufen, dararUan (Phlv.-Vend., AV.),
=== HUB rastan
2302:asparez, aspar^ (g^n. asparisi)? Np. rastan gehort
5620:phi. paz. vtrayam, inf. virastan^) zurichten Min. Gl. 216,
5628:*) Vgl. pairastan § 92, b.— 160 —
6454:ander vorkommen.^) Vgl. afrCistan, avrastan (zd. aiwi -f
6775:pairastan schmiicken, anordnen', arm. patrast 'bereit',
6805:^manifest' Shk. 263. Daneben aber padrastan *to prepare,
7293:179 (zu sprechen sahrastan), arm. sahastan Hauptstadt',
10238:afrastan 16.
```


## [2026-09-14T01:19:36.901Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5415,5440p' HRN.txt; echo \"== leaf:\"; head -5427 HRN.txt | tr -cd '\\f' | wc -c; echo \"== HUB 2295-2310\"; sed -n '2295,2310p' HUB.txt",
 "description": "Horn entry near rastan"
}
```


### [2026-09-14T01:19:36.988Z] TOOL RESULT

```
kurd. bei. (221) LW. ran; af/. vrün.
606. ränden 'treiben, stossen*, ranis,
Contrahirt aus rawdmden^ Causativ von reßen
(No. 619), vergl. Kä»än: Z(efre), beräw, heräivött^
heräft s. v. ränden,
Phlv. rayinTtan, räyma, räyln(i)sn, räymitärih (Men.),
jüd.-pers. pJN^NI (Is. 63, 17) sind nicht klar.
607. rah^ ras ^), reh *Weg ; espyes.
skr. vergl. rathyd- Xandstrasse' (spät) 2); phlv. reis,
aspjräs; af/. lär^),
LW. kurd. rl; bei. ra, n. rah (219); af/. räh;
arm. rah.
Gehört hierher auch np. reste^i (phlv. rastan, Men.),
Praes. reh-em^ rehlden u. s. w. 'befreit werden, ent-
kommen', wörtl. 'sich auf den Weg machen'?**)
608. rubüden 'wegnehmen, rauben', Praes. rubay-em,
riibäyende ; ruften 'fegen , gäten', Praes. röb-em,
ai. V^löp' (älter röp-) 'zerbrechen, packen, plündern,
rauben''^); phlv. röp 'Raub' (AV.-GL), kah]rupäl 'Bern-
stein (Säy. näsay. II, 115); got. biyaubön 'berauben'.
bei. röpcifj 'fegen, kehren' (329).
ö hat noch Kää. Z. böröw (Impt.), börowön (Aor.),
rowon (Praes.).
np. rubäyem geht auf älteres *rupäyati zurück.
^) BQ. Rückert bei do Lagarde, Ges. Abh. 51, Note l.
^) Aw. hizvö raiHm (y. 50, 6) beisst iiacb Bartholomae,
== leaf:
156
== HUB 2295-2310
in alter Zeit docli nur *r5^, jiinger rah gelautet haben.
Ich glaube dann nicht an ras als neupersische Neben-
form. Bei aspras 'Stadium* liegt die Deutung als Pferde-
weg' allerdings nahe, aber warum heisst es nicht *asprah
anstatt np. aspras, aspraz^ aspres, asprlz (Vullers),
aspres (Schefer, Chrest. pers., vgl. ZDMG. 44, 532),
phi. aspras, aspres (Pahl. Diet. Ill, p. 541), arm. LW.
asparez, aspar^ (g^n. asparisi)? Np. rastan gehort
nicht hierher, da es kein Denominativum sein kann.
608. Np. ruhdyad raubt' aus *rupayati ist wohl von robad
*fegt' aus *raupati zu trennen.
609. Np. raja, raSa *Reihe' scheint mir ein phi. *racak oder
"^rajfaky dagegen np. rada 'Richtung, Linie, Reihe* ein
phi.* ratak vorauszusetzen. Mit rajfa = '^racak Hesse
sich skr. raSana- 'Ordnung, Anordnung vergleichen. Fiir
skr. rdji- *Richtung, Linie' wiirde ich np. "^raz-a er-
```


## [2026-09-14T01:19:45.931Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo -n \"HUB leaf for 2302: \"; head -2302 HUB.txt | tr -cd '\\f' | wc -c",
 "description": "Hübschmann leaf"
}
```


### [2026-09-14T01:19:45.986Z] TOOL RESULT

```
HUB leaf for 2302: 76
```


## [2026-09-14T01:19:50.742Z] AGENT

Now I'll write the verification file.


## [2026-09-14T01:24:05.753Z] TOOL CALL #64: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/page-416.json",
 "content": "{\n  \"pdf_page\": 416,\n  \"book_page\": 386,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-13\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Redh, Regh\",\n      \"verdict\": \"plausible\",\n      \"modern_form\": \"Proto-Iranian *raz- 'to leave, escape (one's notice)' (Cheung 2007: 322); Proto-Indo-Iranian *raȷ́ʰ- 'to abandon; secret'. No PIE root *redʰ-/*reǵʰ- 'to separate, isolate' is reconstructed by Pokorny, Walde-Pokorny, Watkins/AHD or Mann.\",\n      \"note\": \"Nourai's root box is copied verbatim from his own source: Kent, Old Persian, p. 205b s.v. ¹rad- vb. 'leave': \\\"Skt. rah-, pres. rahati 'separates, leaves', to pIE *regh-, Av. razah- 'isolation', or to pIE *redh-, NPers. (through Ars. Phl.) rāhaδ 'he gets free from'\\\". Kent offers *regh- and *redh- as two MUTUALLY EXCLUSIVE alternatives (the first if Av. razah- belongs here, the second if the New Persian verb does); Nourai merges them into a single root 'Redh, Regh' and blends the two glosses ('leave/abandon' from OP rad-, 'isolation' from Av. razah-) into 'to separate, isolate'. Modern handbooks do not accept either reconstruction: Pokorny has no such lemma (his p. 651 is lā-2 'to be concealed'), Watkins' AHD appendix and Mann's IEC have no *redh-/*reǵʰ- of this meaning, and Cheung (Etymological Dictionary of the Iranian Verb, s.v. *raz, p. 322 f.) concludes flatly \\\"No IE etymology can be cited for this Ir. root\\\" — Mayrhofer (EWAia II 442) likewise withdrew the older *legʷʰ- comparison of KEWA III 49. What IS solid is the Indo-Iranian level: Skt. rah 'to be lost, be lonely', rahas- n. 'secrecy, loneliness' = Ir. *raz, whence OP (ava-)rad-, MP/NP rastan/rah- and MP/NP rāz. So the family Nourai draws is real; the PIE label on it is not. The two branches of the chart are also not equally secure: the Avestan branch (node 3) is rejected by current scholarship.\",\n      \"note_fa\": \"نورایی ریشه را «Redh, Regh» با معنی «جدا کردن، تنها کردن» و به استناد کنت (Kent, Old Persian, ص ۲۰۵) آورده است. کنت در واقع دو بازسازی را در برابر هم می‌گذارد: اگر razah- اوستایی هم‌ریشه باشد *regh- و اگر فعل فارسی نو در نظر باشد *redh-؛ نورایی این دو را در یک ریشه ادغام کرده و دو معنی را نیز در هم آمیخته است. هیچ‌یک از فرهنگ‌های امروزی هندواروپایی — پوکورنی، والده-پوکورنی، واتکینز (AHD) و مان — چنین ریشه‌ای را با این معنا نمی‌شناسند؛ چونگ در فرهنگ ریشه‌شناختی فعل ایرانی (ذیل *raz، ص ۳۲۲) صریحاً می‌نویسد که برای این ریشهٔ ایرانی هیچ ریشه‌شناسی هندواروپایی نمی‌توان آورد. آنچه استوار است سطح هندوایرانی است: ایرانی آغازین *raz «رها شدن، از نظر پنهان ماندن» برابر با سنسکریت rah- و rahas-، که فارسی باستان (ava-)rad-، فارسی میانه rastan/rah- و rāz از آن برمی‌آید. پس خانوادهٔ واژگانی نمودار درست است، اما برچسب «هندواروپایی» آن پذیرفتنی نیست و شاخهٔ اوستایی (گرهٔ ۳) را پژوهش امروزی رد می‌کند.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%D8%B1%D8%B3%D8%AA%D9%86\",\n        \"https://en.wiktionary.org/wiki/%D8%B1%D8%A7%D8%B2\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"KNT:205\",\n          \"status\": \"supports\",\n          \"note\": \"Kent, Old Persian (KNT.txt, leaf 230 = printed pp. 205-206), s.v. ¹rad-: \\\"¹rad- vb. 'leave': Skt. rah-, pres. rahati 'separates, leaves', to pIE *regh-, Av. razah- 'isolation', or to pIE *redh-, NPers. (through Ars. Phl.) rāhaδ 'he gets free from'; Fr. Müller, WZKM 11.203-4; Foy, KZ 37.564-5; Bthl. AiW 1505; MB Gr. §192.\\\" This is verbatim the source of Nourai's root name, of both branch languages and of the reference BRT:1505 he puts on node 2. Kent's grammar section (§ on injunctives) repeats \\\"pIE *reghe- (or *redhe-, see Lex. s.v.), Skt. rahati 'he leaves'; inj. 2d sg. OP ava-rada\\\". Note that Kent presents the two roots as alternatives, not as one root.\"\n        }\n      ],\n      \"consulted\": [\n        {\n          \"src\": \"POK\",\n          \"where\": \"POK_full.txt, lemma list 'Root / lemma: re…' and p. 651\",\n          \"stance\": \"silent\",\n          \"note\": \"Pokorny has red-, red-1, red-2, reg-1, reg-2, reidʰ-, rendʰ- etc., but no *redʰ-/*reǵʰ- 'to separate, isolate'; 'rahati' occurs nowhere in the IEW text (grep 'rahati' hits only Czech z-drahati se). Pokorny p. 651, the page Cheung cites for Skt. rah, is 'lā-2 (*leh₂k-) Meaning: to be concealed, covered' (Gk. λανθάνω, Lat. lateō) — a different, semantically 'hidden' etymology, and even there no Indo-Iranian form is listed.\"\n        },\n        {\n          \"src\": \"WLD\",\n          \"where\": \"WLD_Bd1_pages.txt / WLD_Bd2_pages.txt (grep 'rahati', 'razah')\",\n          \"stance\": \"silent\",\n          \"note\": \"Walde-Pokorny nowhere quotes Skt. rahati or Av. razah-; the only 'drahati' hit is Czech z-drahati se under a wholly different root. No *redʰ- 'separate' lemma.\"\n        },\n        {\n          \"src\": \"AHD\",\n          \"where\": \"AHD_watkins1985.txt (grep '^redh', '^regh', 'reĝh')\",\n          \"stance\": \"silent\",\n          \"note\": \"Watkins' Indo-European Roots appendix has no entry *redh- or *regh- of this meaning (only ghredh- 'to walk, go', reg- 'to move in a straight line', etc.). Nourai's root has no counterpart in AHD.\"\n        },\n        {\n          \"src\": \"IEC\",\n          \"where\": \"IEC.txt (grep 'redh-', 'reĝh-', 'rahati')\",\n          \"stance\": \"silent\",\n          \"note\": \"Mann's Indo-European Comparative Dictionary has no *redh-/*reĝh- 'separate, isolate' lemma; the only -redh- entries are bhrodhos 'ford' and ueredh- 'seethe, rile'.\"\n        },\n        {\n          \"src\": \"CHEUNG\",\n          \"where\": \"CHEUNG.txt pp. 322-323, s.v. *raz 'to leave, escape (one's notice)'\",\n          \"stance\": \"partial\",\n          \"note\": \"Cheung collects exactly Nourai's family — OP (+*aua-) avarad-, MMP rh-/BMP lh- /rah-/, BMP lstn /rastan/, NP rastan/rah-, NP rāz, Sogd. r'z, Khot. rrays(s)aa- 'empty', Skt. rah, rahas- — under Ir. *raz, and adds \\\"The meanings 'secret' and 'to flee, escape' are not necessarily incompatible, if we assume an older meaning 'to escape (one's notice)'\\\". But on the IE level: \\\"The IE etymology cited in his previous work KEWA III: 49 (IE *leg\\\"- 'to lay'…) is doubted by Mayrhofer in EWAia\\\" and \\\"No IE etymology can be cited for this Ir. root\\\" (the latter under his separate root *(h)rah). So Cheung supports the Indo-Iranian grouping but not Nourai's PIE root.\"\n        },\n        {\n          \"src\": \"SYN\",\n          \"where\": \"Buck 17.36 'SECRET (adj.)'\",\n          \"stance\": \"silent\",\n          \"note\": \"Buck's synonym list for 'secret' gives Av. guzra-, taya-, Skt. gupta-, gūḍha- and has no Iranian rāz-/raz- material; it offers no support for a PIE root of this shape.\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Old Persian\",\n          \"words\": \"rad 2, radh, ras 2; ava-rad\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The core of this node is solid. Old Persian has a verb rad- 'to leave, abandon, deviate from', attested only with the preverb ava-: injunctive 2 sg. avarada <a-v-r-d> in Darius' Naqš-e Rostam inscription DNa 60 (pathim tyām rāstām mā avarada 'do not leave the straight path'), and 3 sg. avārada in Bisotun DB 2.76 (Kent, Old Persian, p. 205b; Bartholomae, AiW col. 1506). It corresponds to Sanskrit rahati 'leaves, forsakes'. The two further stem-shapes Nourai prints are not separate Old Persian words: 'radh' is the Proto-Aryan/pre-form *radh- that Bartholomae posits (AiW 1506: \\\"Vielmehr ar. *radh-\\\"), not an attested OP form, and 'ras' is the Iranian past stem *rad-ta > *rasta, the base of Middle and New Persian rast- (Abolghasemi, FFD p. 55: rast < MP rast < Old Iranian *rad-ta, d assimilating to s before t) — Kent's Old Persian lexicon does contain a stem rasa-, but it belongs to ar- 'to move, come' (whence NP rasidan), an entirely different root. Nourai's gloss 'set free' likewise belongs to the later Persian stage: in Old Persian the verb is transitive-intransitive 'leave, abandon, fall away from', and the 'be set free, escape' sense develops in Middle Persian. Modern reconstruction (Cheung 2007: 322, citing R. Schmitt 2000: 32) files avarad- under Proto-Iranian *raz, i.e. with a voiced palatal, which also explains rast- (*raz-ta) and rāz.\",\n          \"derivation_fa\": \"هستهٔ این گره درست است: فارسی باستان فعل rad- «رها کردن، وانهادن، از چیزی روی‌گرداندن» را دارد که تنها با پیشوند ava- گواهی شده است — صیغهٔ التزامی/اخباری کوتاه avarada در کتیبهٔ داریوش در نقش رستم (DNa سطر ۶۰: «از راه راست منحرف مشو») و avārada در بیستون (DB ۲/۷۶)؛ کنت (ص ۲۰۵) و بارتولمه (ستون ۱۵۰۶) هر دو آن را با سنسکریت rahati «وامی‌گذارد» برابر می‌نهند. اما دو صورت دیگر که نورایی آورده واژه‌های مستقل فارسی باستان نیستند: radh همان صورت بازسازی‌شدهٔ آریایی آغازین *radh- بارتولمه است، و ras همان ستاک گذشتهٔ ایرانی *rad-ta است که ابوالقاسمی (ماده‌های فعل‌های فارسی دری، ص ۵۵) آن را چنین شرح می‌دهد: «رَست < فارسی میانه rast < ایرانی باستان *rad-ta؛ d پیش از t به s بدل شده است». در فرهنگ کنت ستاک rasa- هست ولی از ریشهٔ ar- «آمدن، رسیدن» است و ربطی به این خانواده ندارد. معنی «آزاد کردن» نیز از مرحلهٔ فارسی میانه به بعد پدید آمده؛ در فارسی باستان معنی «وانهادن، منحرف شدن» است. بنابراین ادعای نورایی در بخش اصلی درست ولی در برچسب‌گذاری صورت‌ها سهل‌انگارانه است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B1%D8%B3%D8%AA%D9%86\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"KNT:205\",\n              \"status\": \"supports\",\n              \"note\": \"Kent p. 205b-206a (KNT.txt leaf 230): \\\"¹rad- vb. 'leave': Skt. rah-, pres. rahati 'separates, leaves'…\\\" immediately followed by \\\"ava- + rad- 'leave, abandon': avarada 2d sg. inj. (§213, §224, §227.II, §237) DNa 60.\\\" Confirms both the OP verb rad- and the compound ava-rad- with the gloss 'leave, abandon'. It does NOT contain an OP 'radh' or an OP 'ras' meaning 'set free' (Kent's 'rasa- present stem of vb., see ar-' is on the same page 206 and belongs to a different root).\"\n            },\n            {\n              \"ref\": \"BQT:949\",\n              \"status\": \"partial\",\n              \"note\": \"Borhan-e Qate' (Mo'in ed.), the ر+س section — BQT_v2_pages.txt leaves 408-410 (printed ≈ 946-951; the vol.-2 leaf→page offset is only accurate to ±3). Leaf 408 opens \\\"بیان دهم: در رای بی‌نقطه با سین بی‌نقطه\\\" and has «رست … ماضی رستن است یعنی خلاص شد و نجات یافت»; leaf 410 has «رسته: بمعنی خلاص شده و نجات یافته باشد». So the page attests the Persian verb and its meaning 'be freed, escape', but Mo'in's footnotes there are only cross-references (رك: رستن / رك: رسیدن) and give no Old Persian etymology — the page does not support the OP node itself.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BRT\",\n              \"where\": \"Altiranisches Wörterbuch col. 1506 (BRT.txt leaf 824)\",\n              \"stance\": \"supports\",\n              \"note\": \"\\\"p. rad- V., nur mit ava 'verlassen'. Praes. 2 rada-. 1) 'verlassen, abweichen von —': pathim tyām rāstām mā avarada mā *starava… DNa 60. 2) 'verlassen, im Stich lassen': Vištāspa… avārada (3S.) Bh. 2.76. — ai. rahati 'er verlässt', np. rahad 'er kommt los von —'.\\\" Exactly Nourai's OP forms and the link to New Persian; but Bartholomae's continuation is important for node 3 (see there).\"\n            },\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"Etymological Dictionary of the Iranian Verb p. 322, s.v. *raz\",\n              \"stance\": \"supports\",\n              \"note\": \"\\\"*OLD PERSIAN: (+ *aua-) avarad- 'to leave, abandon'. See most recently R. Schmitt 2000: 32. = Kent: 205b. Pres. them.: INJ. 2sg. avarada <a-v-r-d> (DNa 60)\\\" — the modern standard confirms the form, its only attestation, and Kent's page.\"\n            },\n            {\n              \"src\": \"FFD\",\n              \"where\": \"Abolghasemi, Māde-hā-ye Feʿl-hā-ye Fārsi-ye Dari, p. 55-56 (FFD_pages.txt pdf pp. 60-61)\",\n              \"stance\": \"partial\",\n              \"note\": \"«رَستن: رَست < فارسی میانه rast < ایرانی باستان *rad-ta … d پیش از t به s بدل شده است» and «ره < فارسی میانه rah < ایرانی باستان *rad-a … raz: گریختن». Abolghasemi thus knows both a base rad- and a root raz 'to flee', but he treats ras- as a Persian past stem (*rad-ta), not as an Old Persian verb — which is why Nourai's 'ras 2' is mislabelled.\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"rahîdan «رهیدن ( رَستن )»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian رَستن rastan / رهیدن rahīdan 'to escape, be set free' continues the Old Persian verb of node 1. Middle Persian has the pair rastan, rah- (MacKenzie, CPD: \\\"rastan, rah- [lstn', l(?)h- | N ~] escape\\\"; Nyberg, Manual of Pahlavi II 167b: \\\"rastan [lstn'] rah- to escape: hač dōšaxw ~; the pres. has passive form: hač band rahihēd… bē rahiyēd 'will get loose from his fetters'\\\"). The past stem rast- goes back to Old Iranian *rad-ta / *raz-ta with the regular dental+t > st assimilation (Abolghasemi, FFD 55), the present stem rah- to *rad-a-/*raz-a- with Old Iranian intervocalic *-d- (or *-z-) > MP -h- (FFD 56). New Persian رهیدن rahīdan is a secondary, denominal-type infinitive built on that present stem rah- (rah- + -īd- + -an), a very common Middle-to-New Persian remodelling, so rastan and rahīdan are doublets of one verb — Moʿin's Farhang-e Fārsi states it flatly: «رَستن [= رهیدن] (مصدر لازم) (رست، رهد، خواهد رست، رهنده، رها، رسته، رهایش) رها شدن، نجات یافتن». The words in the chart's extra line are all built on the same two stems: وارَستن / وارهیدن with the preverb وا- < MP abāz < Old Iranian *apāča- 'back, away'; وارسته the past participle 'detached, free (of worldly ties)'; رستگار 'saved, delivered' = past stem rast- + the agent/quality suffix -gār (< MP -kār). The Saʿdi couplet quoted (بمیر تا برهی ای حسود… جز بمرگ نتوان رست) uses both stems, برهی (present rah-) and رست (past), in one line.\",\n          \"derivation_fa\": \"«رَستن / رهیدن» دنبالهٔ همان فعل فارسی باستان است. در فارسی میانه جفت rastan / rah- گواهی شده است: مکنزی می‌نویسد «rastan, rah- [lstn', lh-] escape» و نیبرگ (راهنمای پهلوی، ج ۲، ص ۱۶۷) نمونه می‌آورد «hač dōšaxw rastan» و صیغهٔ مجهولِ rahihēd «از بند رها می‌شود». ستاک گذشتهٔ rast از ایرانی باستان *rad-ta است که در آن d پیش از t به s بدل شده (ابوالقاسمی ص ۵۵) و ستاک حال rah از *rad-a که در آن دندانی میان دو واکه در فارسی میانه به h نرم شده است (همان، ص ۵۶). «رهیدن» مصدر ثانوی و برساختهٔ فارسی نو بر پایهٔ همین ستاک حال (rah + īd + an) است؛ از همین رو «رستن» و «رهیدن» دو صورت یک فعل‌اند، چنان‌که معین در فرهنگ فارسی می‌نویسد: «رَستن [= رهیدن] … رها شدن، نجات یافتن». واژه‌های ردیف دوم نیز از همین دو ستاک‌اند: «وارَستن/وارهیدن» با پیشوند «وا-» (از فارسی میانه abāz، ایرانی باستان *apāča-)، «وارسته» صفت مفعولی، و «رستگار» از ستاک گذشتهٔ rast + پسوند «-گار». ادعای نورایی در این گره درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B1%D8%B3%D8%AA%D9%86\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"BRT:1505\",\n              \"status\": \"supports\",\n              \"note\": \"Nourai took this number from Kent ('Bthl. AiW 1505'); in the 1904 Altiranisches Wörterbuch the entry actually straddles cols. 1505/1506 (BRT.txt leaf 824), s.v. OP rad-, and ends: \\\"ai. rahati 'er verlässt', np. rahad 'er kommt los von —' … Vielmehr ar. *radh-. Wegen der Bed. des np. Verbums s. ai. rahita- Adj., PPP. zu rahati, eig. 'losgekommen von —'.\\\" Bartholomae thus explicitly connects New Persian rahad 'gets free' with OP rad-, which is exactly the arrow drawn here.\"\n            },\n            {\n              \"ref\": \"KNT:205\",\n              \"status\": \"supports\",\n              \"note\": \"Kent p. 205b s.v. ¹rad- names the New Persian outcome in so many words: \\\"or to pIE *redh-, NPers. (through Ars. Phl.) rāhaδ 'he gets free from'\\\" — i.e. the modern verb reached Persian through Arsacid (Parthian/Middle) Persian, as the chart's Old Persian → Persian arrow implies.\"\n            },\n            {\n              \"ref\": \"BQT:949\",\n              \"status\": \"partial\",\n              \"note\": \"BQT_v2_pages.txt leaves 408-410 (printed ≈ 946-951): «رست … ماضی رستن است یعنی خلاص شد و نجات یافت»; «رسته … بمعنی خلاص شده و نجات یافته باشد»; leaf 409 carries Moʿin's footnote «رستگار: از رست (رستن، رهیدن) + کار (پسوند فاعلی و مبالغه)» and «رستاخیز … از rast + xēz» — so the دictionary attests رستن ≡ رهیدن and the derivative رستگار of the chart's extra line, but supplies no Old Iranian etymon.\"\n            },\n            {\n              \"ref\": \"FFD:55\",\n              \"status\": \"supports\",\n              \"note\": \"Abolghasemi, FFD p. 55 (pdf p. 60) ends with the entry «رَستن»: «رَست < فارسی میانه rast < ایرانی باستان *rad-ta … صورت اصلی … است، (d) پیش از t به s بدل شده است», continued at p. 56 (pdf p. 61) «ره < فارسی میانه rah < ایرانی باستان *rad-a … raz: گریختن». This is the precise phonetic derivation of both Persian stems from the Old Iranian base of node 1 — the most exact support any of Nourai's references gives for this arrow.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie, A Concise Pahlavi Dictionary p. 71 (PHD.txt, r- section)\",\n              \"stance\": \"supports\",\n              \"note\": \"\\\"rastan, rah- [lstn', l(?)h- | N ~] escape\\\" and \\\"rastarīh [lst'lyh] escape\\\"; the English index has \\\"escape (v.) rastan, wirēxtan\\\". Confirms the Middle Persian stage with both stems and the identity of the New Persian verb.\"\n            },\n            {\n              \"src\": \"NYB\",\n              \"where\": \"Nyberg, Manual of Pahlavi II (Glossary) p. 167b\",\n              \"stance\": \"supports\",\n              \"note\": \"\\\"rastan [lstn'] rah- to escape: hač dōšaxw ~ 85¹²⁻¹³; the pres. has pass. form: hač band rahihēd [lhyhyt'] 34¹, bē rahiyēd [lhydyt'] 98²² will get loose from his fetters. — NP rastan rah- both trans. 'to let go' and intrans. 'to escape'.\\\" Also on the same page \\\"rastak [lstk'] free\\\" and \\\"rastār one who escapes: ~ kartan to bring about an escape, to rescue, to deliver; NP rastār\\\".\"\n            },\n            {\n              \"src\": \"MON\",\n              \"where\": \"Moʿin, Farhang-e Fārsi, s.v. رستن (MON_part1.txt line 67336)\",\n              \"stance\": \"supports\",\n              \"note\": \"«رَستن: [= رهیدن] (مصدر لازم) (رست، رهد، خواهد رست، رهنده، رها، رسته، رهایش) رها شدن، نجات یافتن» — Moʿin equates رستن and رهیدن outright and lists the whole stem paradigm, including رها and رسته of the chart's extra line. (A separate homonym «رُستن [= روییدن]» 'to grow' is kept apart.)\"\n            },\n            {\n              \"src\": \"HRN\",\n              \"where\": \"Horn, Grundriss der neupersischen Etymologie no. 607, p. 135\",\n              \"stance\": \"contradicts\",\n              \"note\": \"Horn attaches the verb not to OP rad- but to rāh 'way': \\\"607. rah, ras, reh 'Weg'… Gehört hierher auch np. resten (phlv. rastan, Men.), Praes. reh-em, rehīden u.s.w. 'befreit werden, entkommen', wörtl. 'sich auf den Weg machen'?\\\" — a folk-etymological derivation ('to take to the road') which Horn himself marks with a question mark. Modern scholarship follows Nourai's side, not Horn's.\"\n            },\n            {\n              \"src\": \"HUB\",\n              \"where\": \"Hübschmann, Persische Studien § 607, p. 66\",\n              \"stance\": \"partial\",\n              \"note\": \"Hübschmann demolishes Horn's derivation: \\\"Np. rastan gehört nicht hierher, da es kein Denominativum sein kann\\\" (i.e. rastan cannot be a denominative of rāh 'way'). He thereby clears the ground for the OP rad- etymology the chart uses, though he does not himself supply the Old Persian source.\"\n            },\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"CHEUNG p. 322, s.v. *raz\",\n              \"stance\": \"supports\",\n              \"note\": \"\\\"*MIDDLE PERSIAN: MMP rh-, BMP l(')h- /rah-/ 'to escape, become free, let go' … Partic.: perf. pass. BMP lst-y /rast-ē/ 'set free' (Psalter); Inf.: BMP lstn /rastan/\\\" and \\\"*NWIR: NP rastan/rah- 'to be liberated, escape; to let go'\\\" — under the same root as OP avarad-, exactly the descent the chart draws.\"\n            }\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Avestan\",\n          \"words\": \"rah; razah\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Both Avestan words exist, but neither has the meaning Nourai gives and current scholarship detaches both of them from this root. (a) Av. rah- (present raršiia-/rārəšiia-, causative rāŋhaya-) is glossed by Bartholomae, AiW col. 1517 as \\\"'abtrünnig sein; — machen'\\\", i.e. 'to be an apostate; to make (someone) apostatize' — a purely religious term of the Gāthās (Y 47.3 rārəšiieintī 'they have fallen away from the Holy Spirit', Y 32.11-12 'they turn men away from the best action'). Cheung 2007: 140 lists it under a SEPARATE Iranian root *(h)rah '? to fall off, leave, let go, escape, reject ?' with Av. raš- (rāṇh-) 'to be disloyal, (?) apostatize', and says of precisely Nourai's Nyberg reference: \\\"The Pers. forms that Nyberg II: 167b cites in support, MMP rh-, BMP lh- /rah-/ 'to escape', NP rastan/rah- 'to be delivered, saved, escape', may rather go back to *rHaz.\\\" So the very passage Nourai cites (NYB:167) is the one modern scholarship singles out as the mistake. (b) Av. razah- n. is glossed by Bartholomae, AiW col. 1514 as \\\"'Einsamkeit, Abgelegenheit'\\\" ('solitude, remoteness'), attested Vd. 8.97 (plural razaŋhąm 'in a place of solitude') — that is Nourai's 'isolation', taken over from Horn. But Cheung 2007: 322 opens his Avestan section with: \\\"The often cited YAv. razah- is unconnected, as it should rather mean 'clime, expanse' (V 8.97), on which see Gonda 1956: 164.\\\" Bartholomae himself had already gone half this way at col. 1506: \\\"Dass ai. rahati mit rāhas- n., jAw. razah- zusammengehört (so zuletzt Foy KZ 37.564), wird durch das np. Wort unwahrscheinlich. Vielmehr ar. *radh-.\\\" The chart therefore hangs a whole branch on an Avestan node that both of its own principal Iranian authorities decline to connect here.\",\n          \"derivation_fa\": \"هر دو واژهٔ اوستایی وجود دارند، اما نه با معنایی که نورایی می‌دهد و نه با پیوندی که پژوهش امروزی بپذیرد. نخست rah- اوستایی: بارتولمه (فرهنگ ایرانی باستان، ستون ۱۵۱۷) آن را «abtrünnig sein؛ — machen» یعنی «از دین برگشتن، کسی را از دین برگرداندن» معنی می‌کند و شواهدش تنها از گاهان است (یسنا ۴۷/۳ و ۳۲/۱۱-۱۲). چونگ (۲۰۰۷، ص ۱۴۰) آن را زیر ریشه‌ای جداگانه *(h)rah می‌آورد و دقیقاً دربارهٔ همان ارجاعی که نورایی داده می‌نویسد: صورت‌های فارسی که نیبرگ در ج ۲ ص ۱۶۷ به پشتیبانی آورده، به احتمال بیشتر به *rHaz بازمی‌گردند نه به این ریشه. دوم razah-: بارتولمه (ستون ۱۵۱۴) آن را «تنهایی، دورافتادگی» می‌داند (وندیداد ۸/۹۷) و همین است سرچشمهٔ «isolation» نورایی (از راه هرن)؛ ولی چونگ (ص ۳۲۲) می‌نویسد که razah- «بی‌ارتباط است و باید معنی «اقلیم، پهنه» داشته باشد» (به استناد گوندا ۱۹۵۶ ص ۱۶۴). خود بارتولمه نیز پیش‌تر در ستون ۱۵۰۶ گفته بود که پیوند rahati سنسکریت با rāhas- و razah- «به سبب واژهٔ فارسی نو نامحتمل است» و به جای آن *radh- آریایی را می‌نهد. پس این گره را پژوهش امروزی رد می‌کند: خطای نورایی نیست بلکه واگویی دیدگاه کهنِ فوی و هرن است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"KNT:205\",\n              \"status\": \"partial\",\n              \"note\": \"Kent p. 205b does mention \\\"Av. razah- 'isolation'\\\" — Nourai's gloss is Kent's word — but only as the FIRST of two alternatives (\\\"to pIE *regh-, Av. razah- 'isolation', OR to pIE *redh-, NPers. … rāhaδ\\\"), and Kent does not cite any Avestan verb rah- at all. Kent's own reference for the discussion, 'Bthl. AiW 1505', is the article in which Bartholomae rejects the razah- connection.\"\n            },\n            {\n              \"ref\": \"NYB:167\",\n              \"status\": \"supports\",\n              \"note\": \"Nyberg, Manual of Pahlavi II p. 167b, s.v. rastan, does make exactly Nourai's comparison: \\\"NP rastan rah- both trans. 'to let go' and intrans. 'to escape'; similarly Av. (1517 sq.) rah- 'to apostatize' and 'to seduce into apostasy'.\\\" So the reference genuinely supports the arrow — but it is a 1974 comparison that Cheung 2007: 140 quotes by name and rejects (\\\"The Pers. forms that Nyberg II: 167b cites in support … may rather go back to *rHaz\\\").\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BRT\",\n              \"where\": \"Altiranisches Wörterbuch cols. 1514 and 1517 (BRT.txt leaves 827, 831), and col. 1506\",\n              \"stance\": \"contradicts\",\n              \"note\": \"Col. 1517: \\\"g., j. rah- V. 'abtrünnig sein; — machen'. Praes. 29 rārəšiia-, 30 (Kaus.) rāŋhaya-\\\" — not 'to escape, set free'. Col. 1514: \\\"j. razah- n. 'Einsamkeit, Abgelegenheit': … dūire ašahi razaŋhąm 'fern an einem Ort der Einsamkeit' V. 8.97\\\" with the note \\\"ai. rāhas- n.; vgl. np. rāz 'verborgen'\\\". But at col. 1506, in the OP rad- article Kent points to, Bartholomae writes: \\\"Dass ai. rahati mit rāhas- n., jAw. razah- zusammengehört (so zuletzt Foy KZ 37.564), wird durch das np. Wort unwahrscheinlich. Vielmehr ar. *radh-.\\\" — i.e. Bartholomae expressly severs the link that this chart node embodies.\"\n            },\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"Etymological Dictionary of the Iranian Verb pp. 140 (*(h)rah) and 322 (*raz)\",\n              \"stance\": \"contradicts\",\n              \"note\": \"p. 322: \\\"*AVESTAN: ¶ The often cited YAv. razah- is unconnected, as it should rather mean 'clime, expanse' (V 8.97), on which see Gonda 1956: 164.\\\" p. 140: Av. raš- (rāṇh-) 'to be disloyal, (?) apostatize' is put under a separate root *(h)rah, with \\\"No IE etymology can be cited for this Ir. root\\\", and Nyberg's Persian comparison is rejected. Both of Nourai's Avestan words are thus removed from this family by the current standard work.\"\n            },\n            {\n              \"src\": \"NYB\",\n              \"where\": \"Nyberg II 167b s.v. rastan\",\n              \"stance\": \"supports\",\n              \"note\": \"See ref_check: Nyberg is the one authority that does draw Nourai's Avestan → Persian link (\\\"similarly Av. (1517 sq.) rah- 'to apostatize'\\\").\"\n            },\n            {\n              \"src\": \"HRN\",\n              \"where\": \"Horn, Grundriss no. 602, p. 134\",\n              \"stance\": \"supports\",\n              \"note\": \"\\\"602. rāz 'geheim, verborgen'. aw. razah- (vd. 8, 97); phlv. rāz … skr. ráhas- 'Einsamkeit, Geheimniss'.\\\" Horn (1893) is the source of the whole Av. razah- branch; he too glosses razah- as the Skt. rahas- equivalent 'solitude, secret'. This is the view Cheung overturns.\"\n            }\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Persian\",\n          \"words\": \"râz «راز»\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Persian راز rāz 'secret, mystery' is unquestionably an old Iranian word: Middle Persian rāz [l'c], Manichaean MP r'z 'mystery, secret' (MacKenzie, CPD: \\\"rāz [l'c | M r'z, N ~] secret, mystery\\\", with the derivative rāz-kirrēg 'architect'), Parthian r'z, Sogdian r'z / r'zh, Choresmian r'z (f.) 'secret'; the word was borrowed early and widely into Aramaic (ʾrzʾ), Hebrew rāz (Daniel 2), Syriac ʾrāzā and Armenian eraz. Its Indo-Iranian counterpart is Sanskrit rahas- n. 'secrecy, loneliness', rahasya- 'mystery'. So far Nourai is right. The disputable step is the specific parent he draws: Avestan razah- (node 3). That equation is Horn's (Grundriss no. 602, p. 134: \\\"aw. razah- (vd. 8,97); phlv. rāz; skr. ráhas-\\\") and Bartholomae's note at col. 1514 (\\\"vgl. np. rāz\\\"), i.e. the 19th-century consensus — but Cheung 2007: 322 strikes Av. razah- from the family and instead files MP/NP rāz under Ir. *raz, the same root as rastan/rah-, marking the Persian noun 'LW', a loanword (its -z- is the North-West Iranian, Parthian, treatment; an inherited South-West Persian form of *rāzah- would not show z). Wiktionary's current article takes the middle road: \\\"From Middle Persian lʾc (rāz), from Old Persian *rāzah, from Proto-Indo-Iranian *raȷ́ʰ- ('secret, mystery; to abandon'). Related to رستن (rastan) and رها (rahâ).\\\" On that account the word is still a cousin of node 2 — the chart's overall family is right — but it comes from an (unattested) Old Persian *rāzah- or from Parthian, not from the Avestan noun. Verdict: the word, language and gloss are correct and the connection to this word-family is correct; only the Avestan parentage of the arrow is superseded.\",\n          \"derivation_fa\": \"«راز» بی‌گمان واژه‌ای کهن ایرانی است: فارسی میانهٔ rāz (نوشتهٔ l'c، در مانوی r'z) «راز، سرّ» — مکنزی در فرهنگ کوچک پهلوی آن را «rāz secret, mystery» می‌آورد و مشتق rāz-kirrēg «معمار» را نیز — و همچنین پارتی r'z، سغدی r'z/r'zh و خوارزمی r'z. این واژه از همان روزگار هخامنشی/اشکانی به آرامی (ʾrzʾ)، عبری (رازِ کتاب دانیال)، سریانی (ʾrāzā) و ارمنی (eraz) وام داده شده است و برابر هندی باستانش rahas- «نهانی، تنهایی» و rahasya- «راز» است. تا این‌جا سخن نورایی درست است. آنچه جای چون‌وچرا دارد پدرِ نمودار است: razah- اوستایی. این برابرنهاد از آنِ هرن (شمارهٔ ۶۰۲، ص ۱۳۴) و یادداشت بارتولمه در ستون ۱۵۱۴ است، یعنی دیدگاه سدهٔ نوزدهم؛ اما چونگ (۲۰۰۷، ص ۳۲۲) razah- را از این خانواده بیرون می‌گذارد و rāz را زیر همان ریشهٔ *raz (ریشهٔ رستن/رهیدن) می‌آورد و آن را «وام‌واژه» می‌نامد — زیرِ z آن نشانهٔ رفتار شمال‌غربی (پارتی) است و در فارسی جنوب‌غربی انتظار صورت دیگری می‌رفت. ویکی‌واژه راه میانه را می‌گیرد: «از فارسی میانهٔ rāz، از فارسی باستان *rāzah، از هندوایرانی آغازین *raȷ́ʰ-، هم‌ریشه با رستن و رها». پس واژه، زبان و معنی درست است و پیوند آن با این خانواده هم درست، ولی پدرِ اوستاییِ پیکان را پژوهش امروزی کنار گذاشته است: با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B1%D8%A7%D8%B2\",\n            \"https://en.wiktionary.org/wiki/%E0%A4%B0%E0%A4%B9%E0%A4%B8%E0%A5%8D%E0%A4%AF\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"BQT:926\",\n              \"status\": \"partial\",\n              \"note\": \"Borhan-e Qateʿ (Moʿin ed.), the ر+ا section — BQT_v2_pages.txt leaf 388 (printed ≈ 926-931; the vol.-2 offset is good only to ±3-5). The page carries «رازه … بمعنی راز است که پوشیده، پنهان، نهفته و اسرار دل باشد», «رازبان: صاحب راز … که سخن ارباب راز باشد», and the folk-etymological note «بعضی گویند رازی معرب راز است چنانکه بازی معرب باز». It attests the word and its meaning, and Moʿin's footnotes on that page (which do give Pahlavi rās 'راه' and Pahlavi rāst) offer no Avestan etymon for راز itself.\"\n            },\n            {\n              \"ref\": \"HRN:134\",\n              \"status\": \"supports\",\n              \"note\": \"Horn, Grundriss der neupersischen Etymologie, p. 134 (HRN.txt leaf 156), entry no. 602, verbatim: \\\"602. rāz 'geheim, verborgen'. aw. razah- (vd. 8, 97); phlv. rāz, vergl. Ῥαοναν?, Chron. Pasch. I, 730, 14, 15 (de Lagarde, Ges. Abh. 192); skr. ráhas- 'Einsamkeit, Geheimniss'.\\\" This is precisely the arrow Nourai draws (Av. razah- → NP rāz), with the Middle Persian intermediate and the Sanskrit cognate; Nourai's own reference is therefore fully accurate for its date.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie, A Concise Pahlavi Dictionary p. 71\",\n              \"stance\": \"supports\",\n              \"note\": \"\\\"rāz [l'c | M r'z, N ~] secret, mystery. ~īg [-yk'] secret. rāz-kirrēg [l'c kylwk' | M r'z qrwg] architect, builder.\\\" The English index has \\\"mystery rāz\\\". Confirms the Middle Persian stage of the word and its identity with the New Persian noun.\"\n            },\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"Etymological Dictionary of the Iranian Verb p. 322, s.v. *raz\",\n              \"stance\": \"partial\",\n              \"note\": \"\\\"MMP r'z, BMP l'c /rāz/ 'mystery, secret' (LW)\\\", \\\"*SOGDIAN: SSogd. r'zh, BSogd. r'z'y, CSogd. r'z, MSogd. r'z 'secret, mystery'\\\", \\\"*CHORESMIAN: r'z (f.) 'secret' (genuine ?)\\\", \\\"*NWIR: … NP rāz 'secret' (LW)\\\", with Skt. rahas- (n.) 'secrecy, loneliness' as the Indic match. Cheung thus keeps rāz in the family of rastan/rah- but marks the Persian forms as loanwords (North-West Iranian) and removes Av. razah- from the picture — i.e. he supports the word's membership but not the chart's Avestan parent.\"\n            },\n            {\n              \"src\": \"MON\",\n              \"where\": \"Moʿin, Farhang-e Fārsi, s.v. راز (MON_part1.txt line ~65646)\",\n              \"stance\": \"supports\",\n              \"note\": \"«راز: [= رازه] (اِ.) مطلب پوشیده، امر پنهان، سرّ.» — the meaning is exactly the chart's 'secret'. (Moʿin separates two homonyms, «راز [= رز]» 'colour' and the Arabic-mediated «راز» 'mason', from it.)\"\n            },\n            {\n              \"src\": \"ARY\",\n              \"where\": \"Aryanpur, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi, p. 48 (ARY_pages.txt pdf p. 49)\",\n              \"stance\": \"partial\",\n              \"note\": \"Aryanpur lists راز in his appendix of Persian words that resemble Western forms but whose Indo-European root is still undetermined: «واژهٔ فارسی «راز» با واژه‌های انگلیسی … و آلمانی کهن … و هلندی … همسانی دارد ولی واجریشهٔ هند و اروپایی این واژه‌ها هنوز تعیین نشده است». An independent modern Persian handbook thus declines to assign the word any PIE root — consistent with Cheung, and against Nourai's root box.\"\n            },\n            {\n              \"src\": \"HRN\",\n              \"where\": \"Horn, Grundriss no. 602, p. 134\",\n              \"stance\": \"supports\",\n              \"note\": \"See ref_check above — Horn gives Av. razah-, Phlv. rāz, Skt. ráhas- for NP rāz, the exact chain of this node.\"\n            }\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-09-14T01:24:05.792Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe/data/verification/page-416.json (file state is current in your context — no need to Read it back)
```


## [2026-09-14T01:24:08.566Z] TOOL CALL #65: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-416.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 416",
 "description": "Validate and run verify_check"
}
```


### [2026-09-14T01:24:09.769Z] TOOL RESULT

```
JSON OK
nodes verified: 4/4
node verdicts: {'plausible': 2, 'confirmed': 1, 'disputed': 1}
root verdicts: {'plausible': 1}
ref checks: {'supports': 6, 'partial': 4}
books consulted: {'supports': 11, 'partial': 4, 'contradicts': 3} | by book: {'CHEUNG': 4, 'HRN': 3, 'BRT': 2, 'PHD': 2, 'NYB': 2, 'MON': 2, 'FFD': 1, 'HUB': 1, 'ARY': 1}
```


## [2026-09-14T01:24:14.506Z] TOOL CALL #66: Bash

```json
{
 "command": "sed -i 's/the دictionary attests/the dictionary attests/' data/verification/page-416.json && grep -c \"دictionary\" data/verification/page-416.json; python3 -m json.tool data/verification/page-416.json > /dev/null && echo OK",
 "description": "Fix typo"
}
```


### [2026-09-14T01:24:15.719Z] TOOL RESULT

```
0
OK
```


## [2026-09-14T01:24:37.267Z] AGENT

Done — `data/verification/page-416.json` written, valid JSON, `verify_check.py 416` reports 0 PROBLEM lines (4/4 nodes).

**Page 416 (book p. 386) — one entry, root "Redh, Regh" (IE, "to separate, isolate"), 4 nodes**

Verdicts: root `plausible`; nodes: 1 `confirmed`, 2 `plausible`, 1 `disputed`.
Ref checks: 6 supports, 4 partial (no not_checked — every cited reference was readable on disk).

- **Root "Redh, Regh" — plausible.** Copied verbatim from Kent p. 205b, but Kent gives *regh- and *redh- as two *mutually exclusive* alternatives, not one root. No such lemma exists in Pokorny, Walde-Pokorny, Watkins/AHD or Mann; Cheung 2007 says outright "No IE etymology can be cited for this Ir. root". The Indo-Iranian level (Ir. *raz = Skt. rah-/rahas-) is solid.
- **Node 3, Avestan `rah`, `razah` — disputed.** Both words are real but neither means what Nourai says: Bartholomae 1517 glosses Av. rah- 'to be/make apostate' (religious), and razah- (col. 1514) 'solitude'. Cheung 2007:322 removes razah- from the family ("unconnected… should rather mean 'clime, expanse'", after Gonda 1956:164), files Av. raš-/rāṇh- under a separate root *(h)rah, and explicitly rejects Nourai's own reference NYB:167 ("The Pers. forms that Nyberg II:167b cites in support… may rather go back to *rHaz"). Bartholomae himself at col. 1506 already called the razah- link "unwahrscheinlich".
- **Node 1, OP `rad 2, radh, ras 2` — plausible.** OP rad-/ava-rad- 'leave, abandon' (DNa 60, DB 2.76) is confirmed, but "radh" is Bartholomae's Proto-Aryan *radh-, not an OP form, and "ras" is the Persian past stem *rad-ta (Abolghasemi FFD 55); Kent's OP rasa- belongs to ar- 'come'. Gloss 'set free' is the later Persian sense.
- **Node 4, `râz` — plausible.** Word/meaning fully confirmed (MacKenzie, Moʿin, Parthian/Sogdian r'z); HRN:134 no. 602 supports Nourai's arrow verbatim, but that is the 1893 view — Cheung puts NP rāz under *raz (with rastan) and marks it a NW-Iranian loanword; Wiktionary derives it from OP *rāzah-, not Av. razah-.
- **Node 2, `rahîdan/rastan` — confirmed** (MP rastan/rah-, *rad-ta > rast, rah- from *rad-a; rahīdan a secondary infinitive on the present stem). Bonus finding: Horn no. 607 p. 135 instead derived rastan/rahīdan from rāh 'way' ("to set out on the road"), which Hübschmann §607 p. 66 demolishes — modern view sides with Nourai here.

**Extraction errors: none.** I rendered the printed page and the JSON matches it exactly (refs KNT:205 / BRT:1505 / BQT:949 / FFD:55 / NYB:167 / BQT:926 / HRN:134, all forms and glosses).

Minor data note for the owner, not an error: the BQT vol.-2 leaf→printed-page offset in `refs_online.json` (leaf + 543) appears to drift by ~3–5 in this range — راز sits on leaf 388 and the ر+س section on leaves 408–410, so BQT:926 and BQT:949 both land on the right dictionary sections but the stated offset shouldn't be trusted to the page.
