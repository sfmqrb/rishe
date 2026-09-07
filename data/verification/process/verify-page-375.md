# Verification process log — verify-page-375


## [2026-09-07T20:16:21.098Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 375 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-375.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-375.json. Write /home/sfmqrb/git/rishe/data/verification/page-375.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 375` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T20:16:23.115Z] AGENT

I'll start by reading the instructions.


## [2026-09-07T20:16:23.824Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T20:16:23.856Z] TOOL RESULT

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


## [2026-09-07T20:16:24.448Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-375.txt"
}
```


### [2026-09-07T20:16:24.468Z] TOOL RESULT

```
1	=== PDF page 375 (book page 345) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Opop : a bird sound  (refs POK:325)
4	#1 (parent #0) [Persian] refs=POK:325; BQT:424; IRT:46 | pupu «پوپو» : a bird with tall crown and long beak | extra: پوپک ، پوپه
5	#2 (parent #0) [Latin] refs=POK:424; AHD:633 | upŭpa
6	  #3 (parent #2) [English] refs=None | hoopoe
7	--- entry 1 ---
8	ROOT Or -> redirect to Er 1
9	--- entry 2 ---
10	ROOT [Indo-European] Orghi : testicle  (refs POK:782)
11	#1 (parent #0) [Avestan] refs=POK:782; KLN:1092; SYN:257 | ěrězi, arazi : testicles
12	  #2 (parent #1) [None] refs=None |  | NOTE: box is printed entirely blank in the source (outlined box, no header text or content)
13	#3 (parent #0) [Greek] refs=POK:782 | orxis : orchid flower named after its testicle-shaped root
14	  #4 (parent #3) [Latin] refs=None | orchis
15	    #5 (parent #4) [French] refs=None | 
16	      #6 (parent #5) [Persian] refs=None | orkîdeh «اركیده» : orchid
17	    #7 (parent #4) [English] refs=AHD:924; KLN:1092 | orchid
18	--- entry 3 ---
19	ROOT Ôs -> redirect to Ôus 2
20	
```


## [2026-09-07T20:16:27.623Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/extracted/batch/page-375.json",
 "description": "Read source JSON for page 375"
}
```


### [2026-09-07T20:16:27.706Z] TOOL RESULT

```
{
  "pdf_page": 375,
  "book_page": 345,
  "entries": [
    {
      "root": {
        "name": "Opop",
        "lang": "Indo-European",
        "refs": "POK:325",
        "gloss": "a bird sound"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "POK:325; BQT:424; IRT:46",
          "words": [
            {"translit": "pupu", "gloss": "a bird with tall crown and long beak", "script": "پوپو"}
          ],
          "script_extra": "پوپک ، پوپه",
          "note": null,
          "quote": {
            "text": "پوپک پیکی نامه زده اندر سر خویش - نامه گه باز کند گه شکند بر شکنا",
            "poet": "Manŭchehrî"
          }
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Latin",
          "refs": "POK:424; AHD:633",
          "words": [
            {"translit": "upŭpa", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "hoopoe", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {"name": "Or", "redirect": "Er 1"},
      "nodes": []
    },
    {
      "root": {
        "name": "Orghi",
        "lang": "Indo-European",
        "refs": "POK:782",
        "gloss": "testicle"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:782; KLN:1092; SYN:257",
          "words": [
            {"translit": "ěrězi, arazi", "gloss": "testicles", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": null,
          "refs": null,
          "words": [],
          "note": "box is printed entirely blank in the source (outlined box, no header text or content)",
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Greek",
          "refs": "POK:782",
          "words": [
            {"translit": "orxis", "gloss": "orchid flower named after its testicle-shaped root", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Latin",
          "refs": null,
          "words": [
            {"translit": "orchis", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "French",
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Persian",
          "refs": null,
          "words": [
            {"translit": "orkîdeh", "gloss": "orchid", "script": "اركیده"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 4,
          "lang": "English",
          "refs": "AHD:924; KLN:1092",
          "words": [
            {"translit": "orchid", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {"name": "Ôs", "redirect": "Ôus 2"},
      "nodes": []
    }
  ]
}
```


## [2026-09-07T20:16:28.138Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-07T20:16:28.180Z] TOOL RESULT

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


## [2026-09-07T20:16:39.105Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"opop\\|upupa\\|Wiedehopf\" POK_full.txt | head -40",
 "description": "Grep Pokorny for opop/upupa"
}
```


### [2026-09-07T20:16:39.165Z] TOOL RESULT

```
6688:house '), Aeolic SopopTK; Hes.; iruAapTnc; " Hades as the one who locks the gate(s) to the 
27314:Root / lemma: epop, opop 
27319:Material: Armenian popop, npers. pupD'hoo^oe"; 
27326:Latin upupa 'hoopoe'; 
27328:ndd. Hupphupp; Modern High German Wiedehopf,Q\^ High German wituhopfo. Old 
27384:Material: Gr. 6popO(; m. (from *£popO(; after Gen. etc. opopou); compare however, W. 
59853:opopyvuiJi); s. also under melg-\ Armenian merzem^ banish, expel '; gr. aMspyoj ' strip, 
59857:of oil ' (out of it Latin amurca " the waste in pressing olives, dregs of oil '); opopyvupi " 
73437:samm0dri, opopnipioc; "from the same mother ';
```


## [2026-09-07T20:16:39.899Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"or[ĝgǵ]hi\\|ǝrǝzi\\|orchis\\|Hode\" POK_full.txt | head -40",
 "description": "Grep Pokorny for orghi"
}
```


### [2026-09-07T20:16:39.960Z] TOOL RESULT

```
3984:whitefish ', albarus^ white poplar ', albucus^ asphodel plant ' etc.; 
27788:From Root / lemma: ergh-\ "to shake, tremble, *evil, lustful' derived Root/ lemma: orghi-, 
49129:Old English hOdenian^ shake'. Middle High German botzen^un, swing', nisi, hossa 
64191:Root / lemma: orghi-, j-ghi- {*horghi-a) 
64199:Armenian orJi-k'P\. "testicles', o/y/'not castrated' {*orghi-ios), mi-orjT povopxi^'; 
64205:alb. herdhei. 'testicle' {*orghi-a)\ common alb. -gh- > -dh-, -d-. 
64211:Middle Irish uirgget 'testicle' {*orghia), nir. uirgheW\Vc\ secondary^/?; Lithuanian arzus^ 
64215:orghi-, fghi-\ 'testicle' (hence a taboo word). 
64219:Root / lemma: ort- {*horghi-a) 
64223:Material: Armenian {*h3orghi-a) ort 'vine'; alb. {*h2arghi-a) hardi, hardhia ' grapevine '. 
64229:Root/ lemma: ort- {* horghi-a)\ vine, *grape < Root/ lemma: orghi-, fghi- {* horghi-a)\ 
67220:Root / lemma: perth- {*pe-horghi-a) 
67228:Root / lemma: perth-{*pe-horghi-a)\ pole; sprout, derived from a prefixed pe- of Root/ 
67230:lemma: oii- {* horghi-a)\ vine, *grape < Root/ lemma: orghi-, j'ghi-{*horghi-a)\ testicle. The 
76214:from *harut^Jan) with other the vowel Stellung Old Icelandic hredJarP\. "Hodensack'; 
76522:Latin sc/t7///A/s "venter suillus condita farte expletus', dial. 5C/'(9/i//77"Hodensack', 
76767:cymr. CM/o''Hodensack'; mcymr. esk/'t, esgit, ncymr. esgid, corn, eskit, esg/s' shoe ' 
76808:sack, bag'. Middle Low German schodeu. "vagina' (beim horse), f. " pod, pea'. Middle High 
84155:bedridden' ( *suorghid) common Old Indie -g"h- > -ksu- : lllyrian - alb -g"h- > -d-. 
84157:Maybe alb. {*suorghid) derdh^ pour, ejaculate ' common alb. gh- > -dh-.
```


## [2026-09-07T20:16:42.944Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '27305,27345p' POK_full.txt; echo \"=== ORGHI ===\"; sed -n '64185,64235p' POK_full.txt",
 "description": "Print Pokorny entries"
}
```


### [2026-09-07T20:16:43.068Z] TOOL RESULT

```
Lycian knows only the extended forms epn-, epnte "after'; 

about Tocharian Gen.-ending A -ap, B -epi, which one could put here (also in Lithuanian 
would strengthen the Gen. through epi), s. also Pedersen Tocharian 50 ff. 

References: WP. I 122 f., Pedersen Lycian and Hittite 23, Schwyzer Gr. Gr. I 325, 550^, 
620, 628, 6317, Trautmann 1. 
Page(s): 323-325 

Root / lemma: epop, opop 
Meaning: a kind of exclamation 



Material: Armenian popop, npers. pupD'hoo^oe"; 

gr. ETTOTToT TTOTTOTTO "shout, Call of hoopoe', £TTOi|j, -OTTO(; 'hoopoe', EnojTTa aAsKTpuova 
OYpiovHes. (-wn- probably through support in -u)1|j); anacpoc; £noi|j, to opvsov (assimilated 
from *£nacp6(;, which is reshuffled in ending after animal names suffix -a(po(; = alb. kafshe 
(*-a(po(;, *haphos) 'animal'); 

Latin upupa 'hoopoe'; 

ndd. Hupphupp; Modern High German Wiedehopf,Q\^ High German wituhopfo. Old 
Saxon widohoppa\s a reinterpretation after Germanic widu-{\v\6o Germanic u/d'^u-) 'tree, 
wood' and Middle High German /70yC>/fe/7'hupfen'; 

Latvian puppukis 'hoopoe'. 

similar, but not reduplicated. Upper Serbian hupak, poln. hupek'hoopoe'. Upper 
Serbian hupac'cxy like a hoopoe', compare also more in general Slovak. hupati'ccY, russ. 
old chupsti sja' vaunt, boast'. 

References: WP. I 123 f., Kluge^ S. 689. 
Page(s): 325 



Root / lemma: ereb-, orob-, rob- 
Meaning: to drill, make holes 

=== ORGHI ===
See also: see below perg-. 

Page(s): 782 



Root / lemma: orghi-, j-ghi- {*horghi-a) 
Meaning: testicle 
Grammatical information: m. 



Material: Avestan ardz/'-m. " to scrotum', Du. a/pz/'testicles'; 

Armenian orJi-k'P\. "testicles', o/y/'not castrated' {*orghi-ios), mi-orjT povopxi^'; 

gr. (*/7j6pxi<;) 6pxi<; m. "testicle'; 

-e- grade in alb. 

alb. herdhei. 'testicle' {*orghi-a)\ common alb. -gh- > -dh-, -d-. 

The origin of labialized Old laryngeals: 

common Armenian *hiue- > gw- > g- ; Celtic gw- > u-\ Albanian * hiue- > he-. 

Middle Irish uirgget 'testicle' {*orghia), nir. uirgheW\Vc\ secondary^/?; Lithuanian arzus^ 
lascivious ', e/z/Zas 'stallion', Latvian erze//s6s. 

Maybe Root / lemma: ergh-\ ' to shake, tremble, *evil, lustful ' derived Root/ lemma: 
orghi-, fghi-\ 'testicle' (hence a taboo word). 
References: WP. I 182 f., Trautmann 71. 
Page(s): 782 

Root / lemma: ort- {*horghi-a) 

Meaning: vine, *grape 

Material: Armenian {*h3orghi-a) ort 'vine'; alb. {*h2arghi-a) hardi, hardhia ' grapevine '. 

Note: 

alb. hardhry\'r\e, *grape, round fruit' : /7e/'o'/7e 'testicle'. 

Root/ lemma: ort- {* horghi-a)\ vine, *grape < Root/ lemma: orghi-, fghi- {* horghi-a)\ 

testicle. Common alb. -gh- > -dh-, also alb. has preserved the old laryngeal in alb. herdhe 

f. 'testicle', hardhi^y\v\e, *grape, round fruit', consequently Armenian cognates derived 

from alb.
```


## [2026-09-07T20:16:54.767Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['AHD','POK','KLN','SYN','BQT','IRT','WLD','IEC','LEW','LAT','SKT','FSD','WEB','MON','ARY','BRT','HRN','HUB','PHD']:\n    v=d.get(k)\n    print('==',k,'==')\n    print(json.dumps(v,ensure_ascii=False)[:900])\n\"",
 "description": "Inspect refs_online for keys"
}
```


### [2026-09-07T20:16:56.151Z] TOOL RESULT

```
== AHD ==
{"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt", "page_offset": "1985 Watkins ed.: lea
== POK ==
{"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry
== KLN ==
{"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based l
== SYN ==
{"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept head
== BQT ==
{"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.c
== IRT ==
{"title": "M.A. Sajjadiyyeh, Tabar-e Moshtarek-e Iranian va Turanian, Bonyad-e Neyshabur 1368/1989", "kind": "purchase", "url": "gisoom/iketab (full title «پژوهشی در تبار مشترک ایرانیان و تورانیان», Balkh 1368)", "lookup_hint": "Not found.", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "RE-SEARCH 2026-09: purchase only."}
== WLD ==
{"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015.106625 (Band 3 duplicate)", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_
== IEC ==
{"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.", "notes": "", "cites": "column/page number of Mann, An Indo-Europea
== LEW ==
{"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Latin headword in bold at line start. For 1938 pagination borrow lateinischesetym0000awal.", "notes": ""}
== LAT ==
{"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for most of the book (e.g. leaf 21 = p.3); drifts in places (leaf 219 = p.301 -> -82?? probably a mis-detected number) - grep the headword. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_
== SKT ==
{"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.", "notes": "Nourai says '1882-1967'; the
== FSD ==
{"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt", "page_offset": "vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably detected (pages ~ 700-1640) - grep the headword. local file has \\f between leave
== WEB ==
{"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/WEB_vol1.txt", "page_offset": "not reliably detected (page_numbers.json sparse); grep headword. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword bold at line start; e
== MON ==
{"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different paginati
== ARY ==
{"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt"], "page_offset": "printed page = pdf page + 1
== BRT ==
{"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's BRT numbers are Bartholomae's COLUMN number
== HRN ==
{"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.", "notes": "OCR of German Fraktur-free text is decent; Persian
== HUB ==
{"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.", "notes": "Built from djvu.xml (no hocr); OCR quality moderate.", "cites": "page number of Hübschmann, Persische Studien (1895)"
== PHD ==
{"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsian
```


## [2026-09-07T20:17:07.425Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Page(s): 42[3-5]\" POK_full.txt | head; echo ---; awk 'NR>=1 && /Root \\/ lemma/' /dev/null; grep -n \"Root / lemma\" POK_full.txt | awk -F: '$1>36000 && $1<38000' | head -0",
 "description": "Find Pokorny page 424"
}
```


## [2026-09-07T20:17:08.812Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN hoopoe ===\"; grep -n -i \"hoopoe\" KLN_1966.txt KLN_1971.txt | head -20; echo \"=== KLN upupa ===\"; grep -n -i \"upupa\" KLN_1966.txt KLN_1971.txt SKT.txt | head -20",
 "description": "Grep Klein/Skeat for hoopoe"
}
```


### [2026-09-07T20:17:09.193Z] TOOL RESULT

```
32433:Page(s): 423 
32486:Page(s): 423-424 
32508:Page(s): 423 
32524:Page(s): 424 
36112:Page(s): 424 
36160:Page(s): 424-425 
36272:Page(s): 425-426 
---
```


### [2026-09-07T20:17:09.282Z] TOOL RESULT

```
=== KLN hoopoe ===
KLN_1971.txt:77668:(see de-) with huppe , ‘hoopoe’, fr. L. upupa, 
KLN_1971.txt:77669:‘hoopoe’, a word of imitative origin. See hoopoe. 
KLN_1971.txt:115544:hoopoe, n., an Old World bird with a long curved 
KLN_1971.txt:115547:gin; cp. Gk, ‘hoopoe’. Cp. also dupe, 
KLN_1971.txt:256368:bird’, Lith. tutu6ti s to trumpet’, tutljs, ‘hoopoe’, 
KLN_1971.txt:268174:witehopfe, G. Wiedehopf, ‘hoopoe’, which prob. 
KLN_1966.txt:12458:dupe,  n.,  a  person  who  is  easily  misled.  —  F.  dupe, fr.  de  huppe,  i.e.  the  agglutination  of  the  prep,  de (see  de-)  with  huppe,  ‘hoopoe’,  fr.  L.  upupa, ‘hoopoe’,  a  word  of  imitative  origin.  See  hoopoe. Derivatives:  dupe,  tr.v.,  dup-able,  adj.,  dup-abil- ity,  n.,  dup-ery,
KLN_1966.txt:18050:hoopoe,  n.,  an  Old  World  bird  with  a  long  curved bill  and  a  large  crest.  —  Fr.  early  E.  houpe,  fr. F.  huppe,  fr.  L.  upupa,  a  word  of  imitative  ori¬ gin;  cp.  Gk.  sjiotji,  ‘hoopoe’.  Cp.  also  dupe, hoosegow,  n.,  a  jail  (U.S.  Slang).  —  Prob.  fr.  Sp. juzgado,  ‘court  of  justice,  tribunal’,  prop.  pp. of  juzgar,  ‘to  judge’,  used  as  a  noun,  fr.  L.  judi- care,  ‘to  judge’.  See  judge,  v. hoot,  intr.  and  tr.  v.  —  Of  imitative  origin.  Cp. ME.  hoten,  houten  and  Swed.,  Norw.  hula,  lit. ‘to  utter  the  sound  hut’’.  Cp.  also  F.  huer,  ‘to shout’,  and  see  hue,  ‘an  outcry’.
KLN_1966.txt:40641:Tyto,  n.,  a  genus  of  owls  (ornithol.)  —  ModL.,  fr. Gk.  tutco  (Hesychius),  ‘owl’,  which  is  of  imita¬ tive  origin.  Cp.  Gk.  toutk;  (Hesychius),  ‘black¬ bird’,  Lith.  tutuoti,  to  trumpet’,  tulips,  ‘hoopoe’, ON.  fiota,  ‘to  howl,  resound’,  OE.  peotan,  of s.m.,  which  all  are  imitative.
=== KLN upupa ===
KLN_1971.txt:77668:(see de-) with huppe , ‘hoopoe’, fr. L. upupa, 
KLN_1971.txt:115546:F. huppe, fr. L. upupa, a word of imitative ori- 
KLN_1966.txt:12458:dupe,  n.,  a  person  who  is  easily  misled.  —  F.  dupe, fr.  de  huppe,  i.e.  the  agglutination  of  the  prep,  de (see  de-)  with  huppe,  ‘hoopoe’,  fr.  L.  upupa, ‘hoopoe’,  a  word  of  imitative  origin.  See  hoopoe. Derivatives:  dupe,  tr.v.,  dup-able,  adj.,  dup-abil- ity,  n.,  dup-ery,
KLN_1966.txt:18050:hoopoe,  n.,  an  Old  World  bird  with  a  long  curved bill  and  a  large  crest.  —  Fr.  early  E.  houpe,  fr. F.  huppe,  fr.  L.  upupa,  a  word  of  imitative  ori¬ gin;  cp.  Gk.  sjiotji,  ‘hoopoe’.  Cp.  also  dupe, hoosegow,  n.,  a  jail  (U.S.  Slang).  —  Prob.  fr.  Sp. juzgado,  ‘court  of  justice,  tribunal’,  prop.  pp. of  juzgar,  ‘to  judge’,  used  as  a  noun,  fr.  L.  judi- care,  ‘to  judge’.  See  judge,  v. hoot,  intr.  and  tr.  v.  —  Of  imitative  origin.  Cp. ME.  hoten,  houten  and  Swed.,  Norw.  hula,  lit. ‘to  utter  the  sound  hut’’.  Cp.  also  F.  huer,  ‘to shout’,  and  see  hue,  ‘an  outcry’.
```


## [2026-09-07T20:17:16.894Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '32495,32530p' POK_full.txt; echo \"=== 36090-36115 ===\"; sed -n '36085,36115p' POK_full.txt",
 "description": "Show Pokorny page 424 roots"
}
```


### [2026-09-07T20:17:16.961Z] TOOL RESULT

```
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
=== 36090-36115 ===
Page(s): 413-414 

Root / lemma: ghag^'h- 

Meaning: young of an animal or bird 

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
```


## [2026-09-07T20:17:19.054Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nfor f,lines in [('KLN_1966.txt',[18050,12458]),('KLN_1971.txt',[115544])]:\n    txt=open(f,encoding='utf-8',errors='replace').read().split('\\n')\n    for target in lines:\n        pre='\\n'.join(txt[:target])\n        leaf=pre.count('\\f')\n        print(f,target,'leaf',leaf,'-> printed page ~',(leaf-12)*2)\nEOF",
 "description": "Compute Klein leaf/page"
}
```


### [2026-09-07T20:17:20.560Z] TOOL RESULT

```
KLN_1966.txt 18050 leaf 399 -> printed page ~ 774
KLN_1966.txt 12458 leaf 267 -> printed page ~ 510
KLN_1971.txt 115544 leaf 0 -> printed page ~ -24
```


## [2026-09-07T20:17:37.142Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== BQT v1 پوپو ==\"; grep -n \"پوپو\" BQT_v1_pages.txt | head -20; echo \"== BQT v1 پوپک ==\"; grep -n \"پوپک\" BQT_v1_pages.txt | head -20; echo \"== BQT v1 پوپه ==\"; grep -n \"پوپه\" BQT_v1_pages.txt | head",
 "description": "Grep Borhan vol1 for pupu"
}
```


### [2026-09-07T20:17:37.236Z] TOOL RESULT

```
== BQT v1 پوپو ==
== BQT v1 پوپک ==
== BQT v1 پوپه ==
```


## [2026-09-07T20:17:38.772Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== KLN orchid ==\"; grep -n -i \"^orchid\\|orchid,\" KLN_1966.txt | head; echo \"== KLN orchis ==\"; grep -n -i \"orchis\" KLN_1966.txt | head; echo \"== SYN testicle ==\"; grep -n -i \"testicle\" SYN.txt | head -20",
 "description": "Grep Klein/Buck for orchid"
}
```


### [2026-09-07T20:17:38.869Z] TOOL RESULT

```
== KLN orchid ==
9824:cryptology,  n.,  a  secret  language.  —  Compounded of  crypto-  and  Gk.  -koyti,  fr.  -Xoyop,  ‘one who  speaks  (in  a  certain  manner);  one  who deals  (with  a  certain  topic)’.  See  -logy, cryptorchid,  n.,  one  with  undescended  testicles (anat.)  —  Medical.  L.  cryptorchis,  corrupted  fr. Gk.  xput J/opxt?,  ‘undescended  testicles’,  a  word coined  by  Galen  fr.  xp6<]n;,  ‘hiding,  concealment’ (fr.  xpunTeiv,  ‘to  hide’),  and  op yyc,,  ‘testicle’. See  crypt-  and  orchid.
26487:orchid,  n.  —  Fr.  ModL.  Orchideae,  later  Orchida- ceae  (see  Orchidaceae),  fr.  L.  orchis,  fr.  Gk. op/i;,  ‘testicle",  also  ‘orchis’  (so  called  from  the resemblance  of  the  roots  to  testicles),  which  is cogn.  witn  Avestic  lrizi  (dual),  ‘testicles’.  Arm. orji-k‘,  ‘testicles’,  orji,  ‘not  castrated’,  Alb. Iierde  (for  *erde),  ‘testicle’,  Lith.  eizilas,  ‘stal¬ lion’,  Mir.  uirgge,  Ir.  uirge,  ‘testicle’.
26488:orchid-,  form  of  orchido-  before  a  vowel.
26489:Orchidaceae,  n.  pi.,  the  orchid  family  (hot.)  — ModL.,  incorrectly  formed  fr.  L.  orchis,  whose gen.  was  supposed  to  be  orchidis  (in  reality,  the gen.  is  orchis)  See  orchid  and  -aceae.
26490:orchidaceous,  adj.  —  See  prec.  word  and  -aceous.
26491:orchido-,  before  a  vowel  orchid-,  combining  form meaning  1)  testicle;  2)  orchid.  —  In  the  first sense  orchido-  is  derived  fr.  opy.Soc,  errone¬ ously  formed  gen.  of  Spy.'.;,  ‘testicle.’  (the  correct forms  of  the  gen.  are  opyto;,  opyeoj;).  In  the second  sense  orchido-  stands  for  orchid.  See orchid.
26492:orchidology,  n.,  that  branch  of  botany  which deals  with  orchids.  —  Compounded  of  orchido- and  Gk.  -Xoyia,  fr.  -X6yo;,  ‘one  who  speaks
26495:orchidotomy,  n.,  incision  into  a  testicle  (med.)  — Compounded  of  orchido-  and  Gk.  -Topla,  ‘a cutting  of’,  fr.  Topr]!  ‘a  cutting’.  See  -tomy.
== KLN orchis ==
7957:Clonorchis
7960:Clonorchis,  n.,  a  genus  of  flukes  ( zool .)  —  ModL., compounded  of  Gk.  xXtov,  ‘branch,  twig,  slip’, and  opyLc,  ‘testicle’.  The  first  element  stands  for *xXa<ov  and  is  rel.  to  xXav,  ‘to  break’,  fr.  I.-E. base  *qel(a)-,  *qol(a)-,  ‘to  strike,  beat,  break’; see  calamity.  For  the  second  element  see  orchid. Clonothrix,  n.,  a  genus  of  bacteria  ( bacteriol. )  — ModL.,  compounded  of  xXcov,  ‘branch,  twig, slip’,  and  Dpi?,  ‘hair’.  See  prec.  word  and  -thrix. clonus,  also  clonos,  n.,  a  series  of  violent  muscular spasms  ( med .)  —  Medical  L.,  fr.  Gk.  xXovop, ‘a  violent  motion,  confusion,  tumult’,  prob.  a derivative  of  I.-E.  base  *kel-,  ‘to  move  violently’, whence  xeXeaAai,  ‘to  urge  on,  exhort’,  xeXeusiv, ‘to  urge  on,  exhort,  order’,  L.  celer,  ‘swift’.  See celerity.
9824:cryptology,  n.,  a  secret  language.  —  Compounded of  crypto-  and  Gk.  -koyti,  fr.  -Xoyop,  ‘one who  speaks  (in  a  certain  manner);  one  who deals  (with  a  certain  topic)’.  See  -logy, cryptorchid,  n.,  one  with  undescended  testicles (anat.)  —  Medical.  L.  cryptorchis,  corrupted  fr. Gk.  xput J/opxt?,  ‘undescended  testicles’,  a  word coined  by  Galen  fr.  xp6<]n;,  ‘hiding,  concealment’ (fr.  xpunTeiv,  ‘to  hide’),  and  op yyc,,  ‘testicle’. See  crypt-  and  orchid.
16969:Habenaria,  n.,  a  genus  of  plants,  the  rein  orchis (hot.)  —  ModL.,  fr.  L.  habena,  ‘thong,  rein’, which  stands  for  habe-na,  fr.  habere,  ‘to  hold, to  have’;  habena  prop,  means  ‘that  by  which something  is  held’;  see  habit.  The  genus  is  so called  in  allusion  to  the  shape  of  the  spur, habendum,  n.,  part  of  a  deed  that  defines  the estate  which  the  grantee  is  to  have  (law).  —  L., ‘to  be  had',  neut.  gerundive  of  habere,  ‘to  have’ (see  habit) ;  so  called  because  it  begins  in  Latin with  the  word  habendum.  For  other  Latin  gerun¬ dives  used  in  English  cp.  agenda  and  words there  referred  to.
26487:orchid,  n.  —  Fr.  ModL.  Orchideae,  later  Orchida- ceae  (see  Orchidaceae),  fr.  L.  orchis,  fr.  Gk. op/i;,  ‘testicle",  also  ‘orchis’  (so  called  from  the resemblance  of  the  roots  to  testicles),  which  is cogn.  witn  Avestic  lrizi  (dual),  ‘testicles’.  Arm. orji-k‘,  ‘testicles’,  orji,  ‘not  castrated’,  Alb. Iierde  (for  *erde),  ‘testicle’,  Lith.  eizilas,  ‘stal¬ lion’,  Mir.  uirgge,  Ir.  uirge,  ‘testicle’.
26489:Orchidaceae,  n.  pi.,  the  orchid  family  (hot.)  — ModL.,  incorrectly  formed  fr.  L.  orchis,  whose gen.  was  supposed  to  be  orchidis  (in  reality,  the gen.  is  orchis)  See  orchid  and  -aceae.
26500:Orchis,  n.,  a  genus  of  plants  of  the  orchid  family (but.)  —  L.  orchis,  fr.  Gk.  opyi;,  ‘testicle; orchid’.  See  orchid.
33526:—  Arab.  $aldh,  ‘prayer’,  fr.  Aram.  tz6lotha,  em¬ phatic  form  of  lzelo,  ‘prayer’,  fr.  tzeld',  ‘he bowed’  (whence  Pa'el  tzalle),  ‘he  prayed’,  orig. ‘he  bowed  in  prayer’,  and  rel.  to  Ethiop.  falawa, ‘he  bowed’,  lalaya,  ‘he  prayed’,  Akkad,  yuliu, ‘to  entreat’,  rel.  also  to  Arab,  sdlan,  ‘middle  of the  back’.  Cp.  S.  Fraenkel,  De  Vocabulis  in  an- tiquis  Arabum  carminibus  et  in  Corano  pere- grinis,  Leiden,  1880,  p.  21,  Wensinck,  Encyclo¬ paedia  of  Islam,  art.  Salat. sale,  n.  —  ME.,  fr.  OE.  sala,  fr.  ON.  sala,  which is  rel.  to  OHG.  sala,  Swed.  salu,  Dan.  salg.  See sell,  v.,  and  cp.  the  second  element  in  handsel, salep,  n.,  the  dried  tubers  of  various  kinds  of  or¬ chid,  used  as  food.  —  F.,  fr.  Sp.,  fr.  Arab. sahlab,  in  vulgar  pronunciation  sdhleb,  corrupt¬ ed  fr.  tha'lab  in  (tufa  ath-tha.' lab ,  ‘the  fox’s  tes¬ ticles’,  the  Arabic  name  of  the  tubers  of  the Orchis  mascula.  Cp.  saloop.  For  sense  develop¬ ment  cp.  Orchis.
== SYN testicle ==
3857:evidence of any common term is the limited group Skt. vadhri- and the rare Grk. ‘pis ‘castrated’. It was effected by cutting or crushing the testicles, also by burning, cauterizing. Aristot. HA
4133:2. ON boli, ME bule, bole, NE bull, MLG bulle (> NHG bulle, much used in the north in place of ster; also the source of Lith. bulius, Lett. bullis), Du. bul, prob.: ON bollr ‘ball, testicle’, OHG ballo ‘ball’, OE beallucas ‘testicles’ (so NE balls in vulgar use), Grk. daddés ‘penis’, Lat. follis ‘leather bag’, etc. Walde-P. 2.178.
4413:4. Ir. (muc-)cullach, NIr. collach (used also for ‘stallion’, ‘he-ass’, etc., but esp. ‘boar’), like Ir. (ech-)cullach, Br. marc’h kalloc’h ‘stallion’ (3.42), lit. ‘with testi- cles, uncastrated’ (like Grk. €vopxos fr. 8pxis ‘testicle’), deriv. of word for testi- cle, W. caill, Br. kell (4.49). Stokes 72, Henry 50.
4423:Pol. kiernoz = ORuss., Ukr. knoroz : ChSl. kriini ‘mutilated’, perh. com- pounded with a word for testicle cognate with Grk. dpxis, the whole meaning orig. ‘castrated’, with shift to ‘boar’. Ber- neker 663f. Briickner 229.
4562:3. Iv. ech-cullach, or simply cullach, Br. marc’h-kalloc’h, with deriv. of word for ‘testicle’, W. caill, Br. kell. Cf. Ir. (muc-)cullach ‘boar’ (3.32). Also Br. marc’ h-kalc’h with kalc’h ‘penis’.
4568:5. Lith. erzilas, Lett. érzelis : Grk. dpxis ‘testicle’, etc. Walde-P. 1.183. Miuihl.-Endz. 1.577.
5207:TESTICLE
6545:: ON koddi ‘pillow’, OE codd ‘bag, pod’ (ME cod rarely ‘belly’ or ‘testicle’), prob. Lat. (fr. Oscan) botulus ‘sausage’, all with common notion of ‘swollen, rounded’ object. Walde-P. 1.671. Falk- Torp 606. Feist 390.
6611:449 TESTICLE
6613:It. testicolo, coglione (pl.) Boh.  varle, mudo, kulka Fr. testicule, couille Sw.  testikel, sten Pol.  mudo, jadra (pl.) Sp. testiculo, cojon OE herpan, sceallan, Russ, mudo, jajco Rum.  testicul, bos, cotii beallucas (all pl.) Skt. anda-, muska- Ir. macraille, uirge ME ballok, stone Ay. arazi (du.) Nir. = magairle NE testicle (ballock, ball) W. caill Du. teelbal, zaadbal Br. kell OHG hodo
6620:Lith. pautas, Lett. pauts, formerly ‘ege’, now ‘testicle’ (Lett. dial. ‘egg’) : Lith. pusti ‘blow, swell up’, Lett. pate ‘blister, pustule’, etc. Walde-P. 2.80. Mihl.-Endz. 3.130.
6621:3. Skt. anda- (also ‘testicle’), etym.? Possibly fr. *andra- and : ChSl. *jedro, jadro ‘kernel, testicle’ (but cf. 4.49). So Uhlenbeck, s.v., Barth., IF 3.175.
6622:oF T ARTS 5 for ‘testicle’, though natu- e used mostly in the plural ]), are listed in the singular old dua, noted. ‘The Irish forms
6629:7 ? rotruding testicles’. : 9. Lat. testiculus (whence the literary
6630:Romance words, It. testicolo, etc., and Dan., Sw. testikel, NE testicle), dim. of iestis also ‘testicle’ (Plaut., etc.), but the same word as testis ‘witness’. This pe- culiar use of ¢estés is prob. in imitation of Grk. rapaordrat ‘testicles’ (Plaut. Com., ete.), wrongly associated with the legal sense of rapacrarns ‘supporter, defender’ and so with (cf. suwperstes =) testis ‘wit- ness’, instead of with the use of rapacrd- tat for twin ‘supporting pillars’, ‘props of a mast’, etc., hence ‘testicles’, just as biéywo. ‘twins’ was also used in this sense (Galen, etc.). Cf. (but without a aay explanation proposed ll ce er, Zur lat. Sprachgeschichte ter titine din ; poe oes hess’ to te ti a pepicetion oe ‘wit slang { di. Rs ss !) and quoting Fr, tifiuenead esticles (student’s slang ed by Latin associations?)
6640:Ir. uirge ‘testicle’, not ‘penis’ (K. Meyer, Ber. Preuss. Akad. 1912.800), see above, 1 and Pedersen 2.662.
6641:W. caill, Br. kell : OE sceallan, OFris. skal ‘testicles’, possibly as ‘scrotum’ fr. ‘leather bag’, fr. the root *skel- ‘cut, split’ (cf. ON hredjar, etc., below, 4). Walde-P. 2.592.
6644:ON hredjar (pl.) ‘scrotum with tes- ticles’ (NIcel. ‘testicles’), Dan. redder, OE herpan ‘testicles’, prob. orig. ‘scro- tum’ as ‘leather bag’ : OE heorfa ‘deer- skin’, OHG herdo ‘vellus’, Lat. cortez ‘bark, rind’, scortwm ‘skin, hide’ (here also late scrotum?). Walde-P. 2.578. Falk-Torp 981.
6646:Dan., Sw. sten, as also ME, NE stone frequently used for ‘testicle’.
6651:6. ChSl. isto (pl. istesa ‘kidneys’, ORuss. du. jestesé ‘testicles’), prob. : ON eista ‘testicle’ (both combined under
```


## [2026-09-07T20:17:53.846Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ntxt=open('SYN.txt',encoding='utf-8',errors='replace').read().split('\\n')\nfor target in [5207,6611,6613,6629]:\n    leaf='\\n'.join(txt[:target]).count('\\f')\n    print(target,'leaf',leaf,'printed',leaf-24)\nEOF\necho \"== BRT arezi ==\"; grep -n \"arəzi\\|arazi\\|ərəzi\\|ǝrǝzi\" BRT.txt | head -20",
 "description": "Compute SYN page; grep Bartholomae"
}
```


## [2026-09-07T20:17:54.120Z] TOOL CALL #16: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:424 2>&1 | head -60",
 "description": "Fetch Borhan page 424"
}
```


### [2026-09-07T20:17:55.209Z] TOOL RESULT

```
5207 leaf 231 printed 207
6611 leaf 294 printed 270
6613 leaf 294 printed 270
6629 leaf 294 printed 270
== BRT arezi ==
7607:•  j.  a-varazika-"  Adj.  (fem.  °zikii-)  'nicht wirkend,  faul':  druxi  ojfä^re  'ke  (VSf.) ' V.  /*.3o.  I
17021:•  g.,  j.  baraziman- Adj. 'hoch':  imä  raeüa bartziit^m  •zimanqm  avat  (sd.)  yai  hvarJ avaaY.36.6i  —  Avan  bar7zisi?m  'zima- nqm Vr.  IQ,  2.
17025:•  ].,  g.  baraziäta-  Adj.  'der  höchste,  hüchst- gelegene':  'te paiti  bantaAi  Aaraiiyg paiti bansayä  Y.  57.  19;  —  'taiibyS  gairibyö V. 2. 22;  —  'laihiaia  paiti  gätuha  V, 6^.45;  —  urvaranqm  .  ■  ysi  hftiii ..  'taca V.  2.  28; —  imä  raoiä  't?m  bar»zimanqm
19145:•  j.  niSäto.baraziäta-  Adj.  —  ?  — ,  Beiwort des  Hauses:  tBm  .  .  mstar)ts.spayä  'tä nmünS  masitä  datshi  tarn  .  .  *niltantS.- spatm  'tim  nmsmm  dt^Shi  bir^zimiüm Yt.  10.  30.
19174:•  j,  ni-maraziäta-'*  Adj.  (fem.  °/5-)  --  ?  — , von  der  Cistä:  raeistam  cistam  .  .  Harn Yt.  16.  1.
24197:•  j.  vi-maraziäta-  Adj.  'der  am  meisten, besten  abwischt,  reinigt,  läutert'  (mit  Akk.): ahrnUktm  nqma  yal  amilanqm  spjntanqm . .  tat  vlspahe  atafOus  astvatS  anhvqm  asti 'hm  "unser  Name  ist  es  . .,  was  am  besten die. Seelentriebe  . .  läutert"  Yli,4;  z.
```


### [2026-09-07T20:17:56.629Z] TOOL RESULT

```
no scan of BQT covers printed page 424 (see 'scans' in refs_online.json)
```


## [2026-09-07T20:18:06.267Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json;d=json.load(open('refs_online.json'))['BQT']\nprint(json.dumps(d,ensure_ascii=False,indent=1))\" ",
 "description": "BQT details"
}
```


## [2026-09-07T20:18:07.269Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==295' SYN.txt | head -20; echo \"===== leaf 282 =====\"; awk 'BEGIN{RS=\"\\f\"} NR==282' SYN.txt | head -12",
 "description": "Inspect SYN leaves"
}
```


### [2026-09-07T20:18:08.686Z] TOOL RESULT

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


### [2026-09-07T20:18:10.037Z] TOOL RESULT

```
d for ‘egg’ derived fr. the word for ‘bird’ seen in Lat. avis, Skt. vi- (3.64). Walde-P. 1.21 ff. Ernout-M. 718. Pe- dersen 1.66. Falk-Torp 182. Berneker 26.
Grk. *dreov (Bea wd. "Apyetor, Hesych.), weov (Epich.), Lesb. doy, Att. wov, NG avyé (arising in ra @4 > r’avyd like 7a dria > 7’avria, whence adri ‘ear’; Hatzidakis Mec. 2.322); Lat. ovum (> It. uovo, Fr. euf, Sp. huevo, Rum. ou); Ir. og, NIr. ubh, W. wy, Br. vi; Crim. Goth. ada, ON egg, Dan. ag, Sw. agg, OE @g, ME ey (ME, NE egg fr. ON), Du., OHG, MHG, NHG e; ChSI. *(j)aje, ajtce, SCr. jaje, Boh. vejce, Pol.
449 TESTICLE
Grk. épxis Goth. .... Lith. pautas NG Spxts (lit.), apxlde ON eista, bollr (hredjar Lett.  pauts Lat. testiculus, testis (ca- pl.) ChSl. sto, *mado, lono leus) Dan.  testikel, sten, redder  SCr.  mudo, jajce
It. testicolo, coglione (pl.) Boh.  varle, mudo, kulka Fr. testicule, couille Sw.  testikel, sten Pol.  mudo, jadra (pl.) Sp. testiculo, cojon OE herpan, sceallan, Russ, mudo, jajco Rum.  testicul, bos, cotii beallucas (all pl.) Skt. anda-, muska- Ir. macraille, uirge ME ballok, stone Ay. arazi (du.) Nir. = magairle NE testicle (ballock, ball) W. caill Du. teelbal, zaadbal Br. kell OHG hodo
MHG hode
NHG hode
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
jaje, jajo, Russ. jajco; Av. *Gvaya-, NPers. xaya-; Arm. ju.
2. Lith. kiausinis (also kiaugis) ; Lith. kiausé ‘skull’, Skt. koca- ‘container, cup, pod’ (also rarely ‘egg’), sku- ‘coy- er’, etc. Walde-P. 2.549.
Lett. wola (also ‘round stone, pebble’ ; Lith. uola ‘whetstone, rock’) : Lett, velt, Lat. volvere ‘turn’, Lith. apvalus, ON valr ‘round’, etc. (Walde-P. 1.298 ff, without wola). Muhl.-Endz. 4.416,
Lith. pautas, Lett. pauts, formerly ‘ege’, now ‘testicle’ (Lett. dial. ‘egg’) : Lith. pusti ‘blow, swell up’, Lett. pate ‘blister, pustule’, etc. Walde-P. 2.80. Mihl.-Endz. 3.130.
3. Skt. anda- (also ‘testicle’), etym.? Possibly fr. *andra- and : ChSl. *jedro, jadro ‘kernel, testicle’ (but cf. 4.49). So Uhlenbeck, s.v., Barth., IF 3.175.
oF T ARTS 5 for ‘testicle’, though natu- e used mostly in the plural ]), are listed in the singular old dua, noted. ‘The Irish forms
therwise 0U 4 + ular collectives ‘scrotum, testi ‘ erous slang terms, only
seemed the most important
alee torghi-, etc. Walde-P. 1.182 f.
im. opxt NG
xoyts, late dim. opxtdioy (> ae a ‘airge (prob.); Av. araze tum’); Arm. orjik* (pl.); f. Skt. dvir-rjtka- ‘with
ipxl6t); (dual, sg. -ScTO Alb. herdhe; ¢
===== leaf 282 =====
. Barth. 837.
Digitized by Arya Samaj Foundation Chennai and eGangotri
THE BODY; BODILY F UNCTIONS AND CONDITIONS 2438
paris OF 436 KNEE Goth. kniu Lith. kelys jk 757” ON kné Lett.  celis eG ybvaro Dan. kne ChSI. koléno Lat. gent Sw. knd SCr. _koljeno It ginocchio OE cnéo(w) Boh polip rr genou Cl. ME kne ol. ‘olano : rdilla (hie) NE knee Russ. koleno Rum. genuncit Du. = iknie Skt. janu- Ir, —-gltin OHG  kniu, kneo Avy.  inu- Nir. gltin MHG knie (kniu) W. bi NHG  knie 4 IE *fenu- ‘knee’, root connection? | nes by dissim., Vendryes quoted by Loth, ; Ernout-M. 419f. | RC 40.149). Otherwise for the Celtic
Walde-P. 1.586 f.
lde-H. 1.592 f. see yoru, gen. yovaros (hence NG
yovaro); Lat. gent (VLat. dim. genucu- lum > It. ginocchio, Fr. genou, Sp. hinojo, Rum. genunchiu); Goth. kniu, etc., general Gme.; Skt. janu-, Av. Znu-, NPers. zanu; Arm. cunr; Hitt. genu; Toch. A kanwem, B kenine (dual; SSS 128 f.); here also prob. the Celtic group Ir, gliin, W. Br. glin (*gnii-nes > *glu-
4.37 Grk. — zobs Goth. fotus NG 66, wodé pu ON Jotr Lat, pés Dan. fod ae piede Sw. fot as pied OE Sot sp. pie ME sfote : um.  picior NE foot ae traig, coss Du. voet a troigh OHG fuoz u troed MHG T. troad NHG oe aay Se the inherited group, con- ee © Toot connection of which
4 : : ai be said, words for ‘foot’ may agom move, Tun, walk’, or through
nail’, As noted above
(4.3 for § br foot’ have often been
: 9), Words extended to ‘leg
```


## [2026-09-07T20:18:24.840Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for L in 636 640 644 646 648 650 652; do echo \"---- leaf $L ----\"; awk -v n=$((L+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v1_pages.txt | head -8; done",
 "description": "Inspect BQT vol1 leaves near printed 424"
}
```


### [2026-09-07T20:18:26.132Z] TOOL RESULT

```
---- leaf 636 ----
اشکل , عمروفست که سرکن گوسفند و آخو
باشد ۰ 3
بشکله ‌‌ بفتح لام بمعنی شکل است
ی ماد و کسك
کلیدانرا لیز گوبند .
پشکلید » بکر اول و لام بروزن دل
کشد * یعنی بناخن وانکشت رخن ه کرد
پشکم ه بکر اول بر وزت اشکم »
---- leaf 640 ----
بیان شانزدهم
در بای فارسی با کاف فارسی مشتّمل برپنج لفت و کنایت
نگ « بفتح اول و سکون ثانی . زن | بتحتانی زده بلفت زند و پازند )٩(‏ موبد وحکیم
نار پستان راگوش و کلوله و پندق ی که طفلان "و دائا را کویند ؟ .
بدان بازی کنند - و بمعنی کاوری نیز آمدم یگ« بنتح اول و ثانی وظهور ها" مخثف
امت ۹ ۱ پگاه است که سحر و صبح باشد ۴ .
۲۰ ی و عتاه» و ۱
1 ینت دنت ون پگین» بروزن بقن‌بلت زسوپازیه (6۱. .
---- leaf 644 ----
بیان هیجد هم (۱)
در بای فارسی با نون مشتمل بر شصت ودو لت و کنات
واعمالی که بجهت دفم چشم زخم کنند- وبمعنی
پوشیده و پنهان هم آعده است و بلغت زند
وپازند (۲) پارچه ای باشد چهار کوشه که در دو
کوشة آن دود دوژند ومتابعمان زردشت دروقت
خواندن زند و پازنه (۲) و اوستا آن را برروی
لین « بفتح اول وسکون ثانی» بمعنی اما
---- leaf 646 ----
یتجاب
پنجاب. بر وزن کنجاب » ولابتی
است از ندوستان. که لاهود و توابع آن
باشد ٩‏ . 2
دوچت انگشت ه معروف است- و نام
نبانی هم مت که آن‌ا دلاشوب خوانند و بوته
و درخت آن در کار رودخانه ها روید و ب رگ
آن ماتنه ب رک شاهدانه باشد و آن را عربی
---- leaf 648 ----
کوند وآن دا گربه نز خوانند .
نج هر لم» کیهی باشد خوشبوی
باندام پنج انگشت - کویند مریم مادر عیسی
علیه السلام در هنگام وضع حمل بر آن کیاء
چسسلده بود*
بنج یو ۱۵۵ - با تحنانی و واو مجهور
و دال بر وزن نج روزه : ینعی ضف عشر
است چه ده بوده ۴ عثر را گویندکه ده يك
---- leaf 650 ----
لذیو ۵» بر وزن خمیره » بمعنی پنیرگ
است که آن را خبازی و مل و کیه و .نان کلاغ
خوانند و شاب گردله را تنز گویند که
است » و پنبر از آن جهت کویندش که میوو
آن فه‌ینین مسمانده و[ فتاب ون
کردله مرک نش میت
آنکه بهرطرف که آفتاب 0 تیلوفر - و جالوری باشد که بسربانی حربا
میکند ٩‏ . و بضی کویند 3 0 ثیلی - با ام و ور و حرکت مجبولء
---- leaf 652 ----
. بودان تروش
فوفانی ورای بی‌نقطه وسکون واو وشن‌نقطه دار"
نام ساحخری بوده که درزمان خود عثل و مائند
نداشته ۷ . ۱
فوران دخت س من داد بی نقطه
وسکون خای نقطه دار و تای فرشت بمعنی پسر
است نه دختر » نه يك پسر بلکه چندین پسر
است ؛ چه پوران جمع سر باشد» وان نام دختی
```


## [2026-09-07T20:18:33.033Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for L in 653 654 655 656; do echo \"---- leaf $L ----\"; awk -v n=$((L+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v1_pages.txt; done",
 "description": "Print BQT leaves 653-656"
}
```


### [2026-09-07T20:18:34.341Z] TOOL RESULT

```
---- leaf 653 ----
4 ۷۲۷-
ود یان - بکرثاك بر وزن‌حوربان»
۱ رای شهر کنوح۱ هم هست -
و زای هوز » پبرامونو کردا کرد دهان حیوانات
باشد - ومایین لب و بیتی را نیز گویندسوبم‌عنی
ساق درخت هم امده است.و نقار مرغاثرا نیز
کفته‌اند» و با زای فارسی م ۲۳
۰ ۳۹
پورش ۴ - با ابی مجهول بر وزن
سوزش » بمعتی عذر ومعذرت‌وعذرآوردن‌ومعذرت
خواستن باشد .
لودن » بر وزن سوزن » زمینی را
گویند. که بجهت زرات کردن پاك کرده
بشند .
ور ه ۳ بر وزن دوزه » بیرامون
و کردا کرد دهانرا گونند - و بمعتی ننةٌ درخت
هم‌آمده اس 8۵
ود ین ه بر وزن کوزیدن . عذر
آوردن وحعذرت خواستن باشدل" 3
وس » بر وزن طوس ۰ چرب زبانی
و قرب و فروتتی را گویند۷ .
دو یا نه بر وزن روزانه » قرب دادن
وفرونتی و بزبان خوش مردم را فربفئن .
لو ست هه ی وزن دوست » معروف
۱
است ۸ - و بمعنیغیبت هم آ مده‌استکهبد گوبی
ومذمت باشد .
پوست باد کر دن -کنابه از طبار
نه دلی نمودن وراز گفتن باشد .
پوست یرای - با بای فارسی
حطی زده » چرم کر و دیاغ را کویند .
بوست دادن » کنابه از اظهار ته
دلی نمودن ومافی‌النمیر گفتن باشد .
بوست سگ‌بر و کشدن- کناب
از بی حیامی و بی شرمی‌نمودن باشد .
بوستگال ه باکاف فارسی بالف کشیده
وبلام زده ؛ پوست بی‌مویرا گوسد که درزبردنبة
کوسفتد مي باشد وآرا باندك دلبه جدا کرده
در سبراب بر ند» و دوست در کوسفند را ف ‏
کلته‌ادد که سر ککن از حودیای آنآ و بشتهات .
۱ بوستگا له بالام بر وزن بوست پاره,
بهعنی پوستگال است که پوست زبردنبةٌ گوسفند
ودوست مقعد کوسفندباشد ۰
فوست کردن - کنابه از الیس
و محرم ساختن باشد - و غیبت نمودن و خبث
کردنرا گویند .
و ستین » لباسیاست‌مسرونه۹ .و کنابه
از غیبت ومذعت وعیب هم‌هست .
۴ کردی002, ۳6۵2, افغانی 0672 .
دروس ورامین) «اسشق ۳۳۹*.
۵ رك : بوز .
نت اسم مصدراز پوزیدن ( مسعمل
۷ - ره : پلوی .
و
---- leaf 654 ----
یوستین بگازر ۱
وعیب جوننده باشد ۰
(وستیی در بدن » کنابه از افثای
راز کردن باشد .
کردن. وعیب نمودن باشدا .
که بر وقت رشتن مردوك محند.
زره وجوشن را گویند - وامربردورشدن‌ویکناری
رفتن هم عست یمتی از راء دورشو - ونام کیاهی
است کهآ نرا میکویشد وشافپا میسازند واز جانب
ارمن می‌آورند و آنرا پوش دربندی میخوانند .
نقری را نافم است » و شیاف خوزی همان‌است.
و‌شا؟ - با ات بالفکشیده. پوشنده
وپوشند کی را گونند؟ .*
بو شث با ثانی‌مجهول بررزن‌حوشك»
بزبان ماوراء النه رگربه را گویند و بعربی سنود
خوانند؟ .
بو شگان - با انی مجهول ر فتح الث
وک‌اف فارسی بر وزن م وکشان. نام نوایست‌از
موسیقی - و بمعنی مغیبات‌هم‌هست بعنی‌چیهابی
که درعالم غیبت‌اند- وبسکون ثالث بروزن‌دوستان
نام جایی و مقامی است نردبك‌به نیشابورومقامی
۱ "۳ رژ۵: دوست کردن.
5 ود: بوشنج ۰ 3 له: بوشث.
۵ - کلکی 0۲ .
اسشق ۳۳۹
8۷ سم
است از مقامات سالك که آنرا بعربی غیب‌الفیب
مفدس تجلی لماید وفانی درحق ومافی در وگردد.
بو شنگ سب با ثانی مجپول بر وزن
هوشنگه , نام قربه‌ایست مابین فثدهار و مولتان
وه‌مرب‌آن فوشنج بود6 - و بسکون ثالت وفتح
نون بمعنی پوشك است که گربه باشد ٩‏ .
لو شنه» بنن اول و سکون نانی و فتح
الث و نون ۰ بمعنی سرپوش باشد - وهرچیزی
پو شه ۲ - بر وزن خوشه ؛ بمعنیمطلق
آویزند .
لكش - بنم اول وسکون ثانی و کاف 4
نز گونند که درجابی بنهان کنند وخاله بربالای
آن ریزند - و بادی که بجهت آش‌روشنکردن
از دهن بدمند - و آتشگیره را نیز گفثه‌اند
ویعربی حراقه خواندد .
بول بر وزن غول . معروف است
ویعربی فلوس کویند*۱- و بمعنی پل رودخانه‌هم
آمده است مطلقاً خواه باغعت ومشگت وخواه با
جوب «نخه ساند۱۱.
ترا
دانشگاه نهران ص ۲۳۸ .
0 تراهست محشر. رسول ححاز
دهنده پپول چشود جواز. عنضری بلخی.
بقیه درصفحهٌ 4۹٩‏
---- leaf 655 ----
و
پولاب بر وزن دولاب » بم‌نی
حس باشد و پولاپی‌حسی, بعنی‌|نچه بحس ونظر
درآ مد ۱ ۰
که از آن‌کارد و شمشیر واعثال‌آن سازند -وتیغ
و شمشیر را نیز گویند - و نام پهلواتی است
ای ال اج و نام دو ست ماز ندرانی و اورا بولاد
غندی میگفته‌اند عم غین نقطه دار - و ب‌عنی
و3 هم هست.
ولاد خسای « کنابه ازاس‌سرزور
ماشفد .
و لادد که م کنابه‌از اسب‌پرزورباشد.
بو لادسنحان کنانه از دلاوران
وسارزان واساحه داران باشد ۰
بو لاد هندی ۰ کنابه‌ازشیترهندی
باشد 5 3 ۰
4و لافی ع با ثانی حجهول بی وژن
طولافی » نوعی از اش‌ارد باشد .
و [4 س با ثانی محپول بر وزن لوله .
خریره مضمحل شده را کویند - وهندوانه‌ومیوه
های دمگر را نز گفته‌اند که درون آنها نرم
. فوبه
و ضایع شده باشد .
زسن را گونند که تکلتو باشد .
وک - بر وزن جوی. بمعنی پوبه‌باشد
که رفتار متوط است یعنی نه نند و نه آهسته,
و بعضی رفتار تند را گوشدب واعر بدیشمه‌نی «م
ست ععنی راه رو وقدم‌بردار .
پو با ۶ بروزن کویا» رونده‌را گویشد
- و بعضی دونده را نز گفته‌اند .
بویان ۴ زان جو بارس مت موی
و د بر ورن جودال» مصی‌دوه
باشد که رونده است ه و دونده رانیز گوند ۳
وی وی ح با بای فارحی بر وزن
خوب روی . مبالفةً درا مدن و رفتن باشد بمنی
تندتند و دوان دوان - و امر باینمعنی هم هست
یعثی بدو وزود براه برو .
بو یچه- بفتح‌اول بر وزن درجه» عشقه‌را
گویند وآن گیاهی است که بردرخت یبچد .
و 4 »_ با انی مجهول بر وزن موبه .
رفتاری باشد متوسط ت + رفتار نند و دو دز |
تبز گویند .
فرهنگه دساتیر نیلمده .
«2. است ۱۱۵» کلکی ۵120) ورند: فولاد.
۴ - نمت فاعلی از پوبیدن .
بقبه ازصفحه ۲۸
۴ نعت فاعلی(صفت مشبهه) از بوسدن.
از هم باشبدن .
جامه » آنچه بدن را بپوشاند . رك : پوشا .
---- leaf 656 ----
4 بفتح اول وسکون ثانی » کلمه‌است
که هنگام تصین با حیرتآمیخته برزبان رانن
وتکرار نیز کننه؟ ۰
یاه » بر وزن بهانه . چوبکی باشد
که درود گران درشکاف چوبی که باره‌مشکافند
فرو برند و کفشگران مابین کفثر و فاب نهند
و گاهی در زیر در گذارند تا سته و کشوده
کی
4 4 بفتح هردو بای فارسی وسکون
تین با حيرتآمخت هگوشد .
بر * بم اول بر وزن ظهر ؛ مدرسةٌ
جهودان را گویند - و بقتح اول دك حصه از چپار
حصه روز و چهار حصهثش باشد چه شبانروزیرا
بهشت حصه کرده حربك را پهر گویند. واین در
هندومتان یشتر مصطلح است .
۱ - رك؛ په‌به » امروز به‌به گوبند .
۳
۵۵
ومحافنت باشد .
هر ه داد - با دال ابجد بر وزن
هرزه کار ۰ باس دار ومحافظت کنشدمرا گوند.
پهلو- بفتح اول و سکون ثانی وضم لام
بواو کشیده, معروف‌است وبعربی‌جنب خوانند ۴
- و بفتح لام شهر را کویند مطلفاً چه پهلوی
بمعنی شهري باشد - و تواحی اصفپان را تیز
کنته‌اند و مردم شجاع و دلاور باشد - ومردم
بزر که وصاحب حال راهم میگویند چه مراد از
راه پهلوی‌راه بزرگان بزدانی‌است *ونام ولاشی
هم هت که زبان پهلوی منسوب بان ولابث
است وبعضی گفته اند که لفت بهلوی زبان پای-
* بر وزن دهره , ینعی پای
سام ين نوح است و یاری پر او بوده و پارسی
و پهلوی بدیشان منسوب است» ومعریب آن‌فهلو
باشد ۱ .
2۸ اررهنی1 ۳27۳0۵ افنانی۳21921,09162«اسشق۳4۱.
«اسشق ۰.۳۶۲ ۴ رث: حکمت اشراق تألف نگارنده ص ۱۰ .  *‏ رك : بهلوی.
بوده (کتیبه های داربوش اول) ؛ بمرور زمان پرئوه به پرهوه وپلهوه بدل‌شدم. بعض نوبند کان
ارمنی «یپلوانی» راموافق تلفظ زمان خود 081000۷0۶ خبط کرده اند » یش برای سهولت تلفظ
هبرل مقدم‌شد وحر کت واو حذف کردید ویپلو ۳2010۷۷ شد «ابران باستان ص ۲۱۸4».سابراین
ممنی اصلی «اولی «یهلو» بعنی پارت. و«بهلوی» یعنی پارتی. فردوسی بهمین ععنی گوید:
[لشکر کشیدن سیاوش] گزین کرد ازآن نامداران سوار دلیران جنگی ده ودوهزار
هم از پهلوی » پاری ۰ کوچ و بلوچ ز کبلان جنگی و دشت سروج.
بقیه‌درسفسة 4۳۱ «شاهنامة بخ ج۳ ص+۵۸ع.
```


## [2026-09-07T20:18:47.215Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for L in 651 652; do echo \"---- leaf $L ----\"; awk -v n=$((L+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v1_pages.txt; done",
 "description": "Print BQT leaves 651-652"
}
```


### [2026-09-07T20:18:48.593Z] TOOL RESULT

```
---- leaf 651 ----
حه ی پا حس ۱
بو پل" با بای فارسی , بروزن و معنی
ودر هندونتان با بر کک بان خور ند» ومعرب آن
فوفل است.
و وه با بای فلرسی بر وزن کوکو »
شانه سر وهدحدرا کویند که‌مرغ سلیمان‌است ِ
ک و کو خوانند .
لو له - بنم اول وفتح بای فارسی,بمعنی
لو تاه منم اول وسکون تانی وفوقاتی ؛
جگر کوسقند را کویند و لهذا غلیه‌ای که از
جگر کوسفند سازند قلبه پونی خوانند -
و بمعنی لوت هم آمده است که اقسام خوردنی‌ها
و انواع اطعمه و اثربه باشد - ونوعی از خربزه
هم هست ۰
و 4 - بانای فرشت
و مخزن را کوند . #۶
و خت" بر وزن سوخت : بمعنی پشت
باشد که از يختن است ۲
و ۵ نم اول بروزن سود » نقض ار
است وآن 7 باشد که دریهنامی جامه افته
میشود و تار بدرازی جامه ۴ - و آتشگیره را
نز کویند وآن چیزی بای دکه باچخماق آش
بروزن غوطه.خزانه
۱ -ر: پوپك:
۵ « واژه نامه۱۸۳* .
بزران
برآن زنند ۴ - وبمعت یکهنه هم آمده است که
در مقابل نو باشد ۵ .
لو ذات « با تای قرشت بروزن پوچات,
بمعنی محسوی باشد و پوداتان بمعنی مصوسات
بعنی آنچه بنطر وحس درآید۱ .
لو ده بر وزن روده » معتی جود است
که نقیش نار باشده چه آن درطول جامه و این
عم رفته را هم کفته‌اند ۷ - و رکوی سوخته -
وچوبی بوسیده کهآترا بجپت آتشگیره‌مهیا کرده
باشند ۴ ومعربی‌حراقه خوانند- وسوده وربختهرا
لیز کویند - و کندیده و ضایم شده را حم
کفته‌اند ۷
وه س بضم اول بروزن حور؛ بمعنی‌پسر
است که برادر دختر باشد ۸ و نام رای شهر
کنوج ٩‏ همست واو یکی‌از بادشاهان و رابان
حندوستان بوده. ومعرب آن فور است- وکسی‌را
یز گونند که خود را نادان و هیحمدان
وانماید ٩۴‏ - ودراجرا نز کفته‌اند و آن پرنده -
است ممروف .
پی دنه بروزن توران » نام شه رکنوج
است ومعرب آن قنوج باشد۱۱- و بمعنی خلیفه
وجانشن .- وباد گار حم‌آمده | ست- وجمع پور
حم مت که یسران باشد .
۴ طبری 6 ( بوه )۰ مازندرانی
۰۲۲۳۹ ازدسانیر «فر هگ دساتیر‎ ۳۹ ٩
-٩‏ مرب آن قنوح.
۱- رگ:پوره
کف شکردنه وراز..
---- leaf 652 ----
. بودان تروش
فوفانی ورای بی‌نقطه وسکون واو وشن‌نقطه دار"
نام ساحخری بوده که درزمان خود عثل و مائند
نداشته ۷ . ۱
فوران دخت س من داد بی نقطه
وسکون خای نقطه دار و تای فرشت بمعنی پسر
است نه دختر » نه يك پسر بلکه چندین پسر
است ؛ چه پوران جمع سر باشد» وان نام دختی
خسرویرویز است که پیش ازآزرمیدخت پادشاهی
کرده راورا بدین نام ازجهت آن خوانده‌اند که
ازوکارهای مردانه بظهور آهده است وأورا نوران
سل ملوله تر کسنان‌وده؟
مجهول و را و دال بی نقطه و کاف فارسی بالف
کشفه و بنون زده » مناید دائست که فارسیان
خمسه مسترف4۶ه را بر پنج روزآخرآ بان ماه می-
افزایندکه مجموعه ده روژ شود وآن ده روز را
پورد گان مبگویند» ودراین روزها جشن سازند
وشادی‌تمایند و آنراجشن بورد کان‌خوانند,ومعرب
آن فوردجان است؟ .
9
پوددیان - با بای حطی » بر وزن
و ممنی پورد گان است که ایام جشن پارسیان
باشد .
و د شسب * «پورمعلوم» پفتح‌شن قمله
دار وسکون سین بي نقطه و بای ابجد » نام پدر
پو دعنقا - لفب زال پدر رستم است»
چه کویند او را سیمرغ بز رکه کرد وسیمر غ‌را
عنقا ثبز خوانند .
بور ك بر وژن خوبك , نام دخش
رای قنوج است و او در حبالةٌ بهرام گور بود .
پور کند با کاف بر وزن زورمند ,
طاق وایوان ومتزل را کوند» وباین‌معتی با زای
نقطه دار هم بنظر آمده است .
لبود هنك ه با میم بر وزن حوشمند ؛
صاحب فرزند و عبالمنه را کوند - و با ثالی
مجهول نام کیاهی است خوشیو .
و ده « بر وزن شوره ۰ بمعنی پور
باشد که بر است . و تنهٌ درخت را ای گوشدب
ویز بان هندی یمعتی تمام پاشد۷ . .
.
4۶ تور (سرح) ان (نست) بعئی
بعمنی(از نژاد)سفیداست وسرخاب وسهراب هردو بمعنیآب سرخ‌است. ازافادات امثادپور داود*.
۳ یگ سحیح و رورد کان است. بیرولی گوید 2 پرورد گان چخست 1 نج روز سن اندرآبان ماهء
وسبب نام کردن آن چنانت که کب رکان اندرین پنجروز خورشی وشراب‌نهتد روانهای «رد گان را
و همی کون دکه جان مرده بیابد وزآن غذاگیرد » و چون از بس آبانماه پنجروز افزوئی بوده
افتاد واندر کیش اذان میم ری بود. بي طردو ینجرا بکارهردند از جهت احشاطرا. وسست وششم
روز آبان‌ماه فروردکان کردند وآخرشان آخر دزدبده» وجملةٌ فرورد گان دمروز گشت. * «التفهیم
ص ۲۵۹ رله: فرورد گان . اهر تلا آن: فروردجان «النفهیم ص ۲۵۹ ح » .
۶ پپلوی 3۵۲0511250 مرکب از : پوروش بمعنی دو رنه : صیاه وسپید وییر +
اسب» دعنی دار ندهٌ اسب دورشگف بااسب شبر» درمر و حالذهب «بورشسف؟ ودر طبری پوستف ( بور-
شیف) آهده «مزدیبنا ص۷۶ وجدول برایر ص۹4۹» و ركك : پیثرسپ . ۱ - ازرشة 011۲
درسان‌کریت بمعنی پر کردن , مملو کردن و اسم مفمول آن در سانسکریت ۳00108 است یعنی
درشده» تمام, کامل. «د کتر کونهن راجا».
```


## [2026-09-07T20:19:27.273Z] TOOL CALL #22: Bash

```json
{
 "command": "sed -n 1,200p tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-07T20:19:27.314Z] TOOL RESULT

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


## [2026-09-07T20:19:28.401Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification && grep -l \"printed entirely blank\\|blank box\" page-*.json | head; echo ---; grep -h -o '\"verdict\": \"[a-z_]*\"' page-*.json | sort | uniq -c",
 "description": "Find blank box precedent"
}
```


### [2026-09-07T20:19:28.487Z] TOOL RESULT

```
page-171.json
page-180.json
page-189.json
page-224.json
page-231.json
page-272.json
page-279.json
page-325.json
page-324.json
page-342.json
---
   3409 "verdict": "confirmed"
    604 "verdict": "disputed"
   1328 "verdict": "plausible"
    203 "verdict": "transcription_suspect"
     75 "verdict": "unverified"
```


## [2026-09-07T20:19:32.145Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification && python3 - <<'EOF'\nimport json\nd=json.load(open('page-325.json'))\nfor e in d['entries']:\n    for n in e['nodes']:\n        if 'blank' in (n.get('derivation') or ''):\n            print(json.dumps(n,ensure_ascii=False,indent=1)[:2000]); raise SystemExit\nEOF",
 "description": "Look at blank-box precedent"
}
```


### [2026-09-07T20:19:33.436Z] TOOL RESULT

```
{
 "id": 6,
 "lang": "Hindustani",
 "words": "",
 "verdict": "confirmed",
 "derivation": "The blank box is the Hindustani (Hindi-Urdu) relay through which English received the words: Hindi महाराजा mahārājā, महात्मा mahātmā, continuing Sanskrit mahārāja-, mahātman- with the usual Indo-Aryan loss of the -n stem and final -ā. Hobson-Jobson shows the word in Anglo-Indian use from the 18th-19th c. ('the Maharaja (Sindia)', Elphinstone's Diary 1808; 'the Maharaja of the Isles', Mas'udi as quoted; 'the Maharajah sent us ... dancing girls', Osborne, Court and Camp of Runjeet Singh 1838), which is the channel of the English forms; Klein and Watkins name only the Sanskrit stage, so the Hindustani step is an inference from the transmission history rather than a claim any of them makes explicitly.",
 "derivation_fa": "این جعبهٔ خالی واسطهٔ هندوستانی (هندی‌ـاردو) است که انگلیسی واژه‌ها را از آن گرفته: هندی mahārājā و mahātmā، ادامهٔ mahārāja- و mahātman- سنسکریت با افتادن ستاک -n و -ā پایانی، چنان‌که در هندوآریایی نو معمول است. «هابسن‌جابسن» کاربرد این واژه را در انگلیسیِ هند از سدهٔ هجدهم و نوزدهم نشان می‌دهد («the Maharaja (Sindia)» در یادداشت‌های الفینستون ۱۸۰۸؛ «the Maharajah sent us ...» در سفرنامهٔ آزبورن ۱۸۳۸)، و همین راهِ ورودِ صورت‌های انگلیسی است. کلاین و واتکینز تنها مرحلهٔ سنسکریت را نام می‌برند، پس گامِ هندوستانی نتیجه‌گیری از تاریخ انتقال است نه ادعای صریح آنان. ادعای نورایی پذیرفتنی است.",
 "sources": [],
 "ref_check": [
  {
   "ref": "(none cited)",
   "status": "not_checked",
   "note": "the Hindustani box has no refs="
  }
 ],
 "consulted": [
  {
   "src": "HJB",
   "where": "Hobson-Jobson, quotations (HJB.txt lines 4406, 7891, 8367, 8792 — leaves 190-370 of the 1903 scan)",
   "stance": "partial",
   "note": "there is no headword MAHARAJA or MAHATMA in Hobson-Jobson; the word appears only inside quotations, e.g. '1808. — ... Some Sirdars put the Maharaja (Sindia) in dhurna' (Elphinstone's Diary) and '1838. — The Maharajah sent us in the evening a new set of da
```


## [2026-09-07T20:19:40.826Z] TOOL CALL #25: Bash

```json
{
 "command": "ls site/pages/375.jpg 2>/dev/null; pdftoppm -f 375 -l 375 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg375 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg375.png",
 "description": "Render PDF page 375"
}
```


### [2026-09-07T20:19:42.591Z] TOOL RESULT

```
site/pages/375.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 47783 Sep  7 16:19 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg375.png
```


## [2026-09-07T20:19:46.346Z] TOOL CALL #26: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg375.png"
}
```


### [2026-09-07T20:19:46.751Z] TOOL RESULT

```

```


## [2026-09-07T20:19:46.748Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-07T20:19:58.488Z] TOOL CALL #27: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-07T20:19:58.494Z] TOOL RESULT

```


```


## [2026-09-07T20:20:03.396Z] TOOL CALL #28: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%BE%D9%88%D9%BE%DA%A9",
 "prompt": "Give the Persian entry for پوپک: pronunciation, meaning, and full etymology (any Middle Persian, onomatopoeic notes, cited sources like Hasandust). Also any related forms پوپو/پوپه."
}
```


## [2026-09-07T20:20:04.050Z] TOOL CALL #29: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/hoopoe",
 "prompt": "Quote the full etymology of hoopoe, including the Latin upupa, French huppe, Greek epops, and any note on imitative origin."
}
```


### [2026-09-07T20:20:08.174Z] TOOL RESULT

```
# Etymology of Hoopoe

According to the Online Etymology Dictionary, the word "hoopoe" has the following origin:

**"1660s, from Latin _upupa_, imitative of its cry (compare Greek _epops_ "hoopoe," Polish _dudek_, Russian _udodu_)."**

The etymology shows that this bird's name derives from Latin and is fundamentally **onomatopoetic**—meaning the word imitates the actual sound the bird makes. The entry also provides cognates in other European languages that reflect similar imitative origins, including Greek, Polish, and Russian variants of the term.
```


### [2026-09-07T20:20:08.999Z] TOOL RESULT

```
# پوپک (pupak) - Persian Entry

**Pronunciation:**
- Classical Persian: /poː.ˈpak/
- Iranian formal: [pʰuː.pʰǽkʰʲ]
- Dari formal: [pʰoː.pʰák]

**Meaning:**
The term denotes a "hoopoe," a type of bird. Related synonyms include هدهد (hodhod), شانه‌بسر (šâne-besar), and پوپو (pupu).

**Etymology:**
The word derives from پوپو (pupu) combined with the Persian diminutive suffix ـک (-ak). The entry references a Middle Persian etymon but lacks full historical documentation in the provided content.

**Related Forms:**
- پوپو (pupu) - the base form from which پوپک developed
- پوپک‌ها (pupak-hā) - plural form
- Also used as a female given name in Persian

The etymology tree indicates development through Middle Persian, though specific cited sources like Hasandust are not included in this Wiktionary entry.
```


## [2026-09-07T20:20:16.080Z] TOOL CALL #30: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%BE%D9%88%D9%BE%D9%88",
 "prompt": "Persian entry پوپو: meaning and etymology (onomatopoeic? Middle Persian? cited sources)."
}
```


## [2026-09-07T20:20:16.772Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/upupa",
 "prompt": "Latin upupa: etymology (onomatopoeic, relation to Greek ἔποψ, Pokorny), descendants (French huppe, English hoopoe), and any note from de Vaan."
}
```


### [2026-09-07T20:20:21.443Z] TOOL RESULT

```
# پوپو (Pôpô/Pupu)

Based on the Wiktionary entry, here's what we know about this Persian word:

## Meaning
The term refers to a **hoopoe**, a type of bird. Related synonyms include هدهد (hodhod), شانه‌بسر (šâne-besar), پوپک (pupak), and ببغا (babġâ).

## Etymology
The entry indicates that پوپو is "Onomatopoeic" in origin—meaning the word mimics the sound associated with the bird, likely reflecting the hoopoe's call or vocalizations.

## Classification
The word is categorized as:
- A Persian onomatopoeia
- A Persian lemma (base form)
- A Persian noun

The entry was last updated on May 24, 2025, and appears in multiple language editions of Wiktionary (Persian, Galician, and Malagasy versions also exist).
```


### [2026-09-07T20:20:23.311Z] TOOL RESULT

```
# Etymology and Descendants of Latin "Upupa"

## Etymology

The Latin term is **onomatopoeic** in origin. The entry states: "Onomatopoeic. Compare Ancient Greek _ἔποψ_ (épops), Persian _پوپو_ (pôpô)."

This indicates the word mimics the hoopoe bird's call across multiple language families.

## Key Descendants

The word spawned numerous Romance language variants:

- **French**: huppe
- **English**: hoopoe (the archaic English "upupa" persists as a direct borrowing)
- **Spanish**: abubilla
- **Italian**: upupa (still in use)
- **Portuguese**: bubela
- **Catalan**: puput

The entry notes these derive "through diverse possible derivations," showing how the original Latin root transformed across different linguistic regions while maintaining reference to the same bird species.

The scientific genus **_Upupa_** in Translingual nomenclature directly preserves the Latin form for taxonomic classification.
```


## [2026-09-07T20:20:29.382Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/orchid",
 "prompt": "English orchid: full etymology — New Latin Orchideae/Orchidaceae, the false stem orchid-, Latin orchis, Ancient Greek ὄρχις, PIE root, date of first use."
}
```


## [2026-09-07T20:20:30.933Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E1%BD%84%CF%81%CF%87%CE%B9%CF%82",
 "prompt": "Ancient Greek ὄρχις: meanings, declension/genitive, and etymology (PIE reconstruction, Avestan cognate, Beekes), descendants."
}
```


### [2026-09-07T20:20:34.536Z] TOOL RESULT

```
# Orchid: Etymology and Definitions

## Etymology

The word "orchid" comes from New Latin *Orchideae* and *Orchidaceae*, derived from Latin *orchis*, which traces back to Ancient Greek *ὄρχις* (órkhis). The Greek term referred both to the plant and to testicles, supposedly inspired by "the shape of the roots."

## Definitions

**As a Noun:**
An orchid is "a plant of the orchid family (Orchidaceae), bearing unusually-shaped flowers of beautiful colours" (mid-19th century usage). The term also describes "a light bluish-red, violet-red or purple colour."

**As an Adjective:**
When used as an adjective, orchid means "having a light purple colour."

## Historical Note

The modern English term supplanted the Middle English word *ballokwort*, which literally meant "testicle plant"—a reference to the plant's root appearance that parallels the Greek etymological origin.
```


### [2026-09-07T20:20:36.315Z] TOOL RESULT

```
# ὄρχις (órkhis)

## Overview
This Ancient Greek noun has multiple meanings and can function as either masculine or feminine, belonging to the third declension grammatical class.

## Primary Meanings
The term encompasses four distinct senses:

1. **Anatomical (masculine)**: "testicle" (often used in plural form)
2. **Anatomical (feminine)**: "ovary"
3. **Botanical (feminine)**: "orchid"
4. **Botanical (feminine)**: a specific type of olive plant

## Etymology
The word derives from Proto-Indo-European *h₁órǵʰis ("testicle"). Related words appear across multiple ancient languages, including Old Armenian, Avestan, Hittite, Albanian, and Irish. The "orchid" sense likely emerged from the plant's characteristically elongated root structure.

## Linguistic Descendants
The term influenced Romance languages through Latin, generating English prefixes like "orchi-" and Italian "orchi-" formations. Modern Greek retained the masculine form όρχις (órchis).
```


## [2026-09-07T20:20:43.834Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81%C3%B3r%C7%B5%CA%B0is",
 "prompt": "Reconstruction page for PIE *h₁órǵʰis 'testicle': the reconstruction, gloss, cited references (Pokorny page, Beekes, Kloekhorst), and the full descendant list including Avestan, Hittite, Greek, Armenian, Albanian, Celtic, Baltic."
}
```


## [2026-09-07T20:20:44.979Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D8%B1%DA%A9%DB%8C%D8%AF%D9%87",
 "prompt": "Persian ارکیده: meaning and etymology (borrowed from French orchidée? Russian? date)."
}
```


### [2026-09-07T20:20:46.432Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-07T20:20:50.941Z] TOOL RESULT

```
# Summary of PIE *h₁órǵʰis

This Wiktionary entry reconstructs a Proto-Indo-European word meaning "testicle." The reconstruction itself remains uncertain, with scholars proposing three main variants: *h₁órǵʰis, *h₃órǵʰis, or *h₃érǵʰis.

## Key Scholarly Debates

**Laryngeal preference:** As one expert notes, "Kloekhorst prefers to reconstruct the term with an initial *h₃ laryngeal as numerous descendants in daughter languages appear to have been affected by the o-coloring of vowels."

**Alternative theories:** Linguist Eric P. Hamp suggests a *h₄ laryngeal reconstruction, though this proposed phoneme remains disputed among Indo-European scholars.

## Descendant Languages

The word evolved across multiple language families:
- Ancient Greek: órkhis
- Old Armenian: orjikʻ
- Albanian: herdhe
- Avestan: ərəzī
- Middle Irish: uirge (Irish úirí)
- Slavic languages through Proto-Slavic *orzъ

The range of descendants suggests this anatomical term was already established in the parent language before the Indo-European family dispersed.
```


## [2026-09-07T20:21:02.350Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== LEW upupa ==\"; grep -n \"upupa\" LEW_1910.txt | head; echo \"== LAT upupa ==\"; grep -n \"upupa\" LAT.txt | head; echo \"== LEW orchis ==\"; grep -n \"orchis\" LEW_1910.txt LAT.txt | head; echo \"== IEC orghi ==\"; grep -n \"orghi\\|órǵʰ\\|epop\\|opop\" IEC.txt | head",
 "description": "Grep Latin dictionaries"
}
```


### [2026-09-07T20:21:02.427Z] TOOL RESULT

```
== LEW upupa ==
== LAT upupa ==
7837:L.L.5,75, pleraeque [aues]... ad suis uocibus... upupa... bubo. - M.L.
66121:Terne expressif, imitatif. Pour le reAoublenent, cf.tutubo, upupa,
69466:la forme, cf .upupa. Vlula est peut-etre un postverbal de:
70390:upupa, -ae f.: i° huppe, oiseau; 3° pioche ou pic. - Ancien. M.L.
== LEW orchis ==
LAT.txt:35506:brut et sans revetement, a 1'origine fait de pisd ou de torchis
LAT.txt:35519:(littdralement "fayonner la terre pour une construction ea torchis"),
LAT.txt:60599:stingus, -I m. : orchis, piante (isid. 3 - 7 , 9 , 43 ).
== IEC orghi ==
12044:oistos, -es- (oisto(n), -en-) ‘testicle. WP I, 166. See next Skt. cf. istíh, f. ‘dash, impulse; Av. istis, f. ‘desire’ (semantics of Li. arZüs 'sensual': Gk. órkhis, see orghis, os below; Ger. geil *wan- to: Ger. Geile ‘testicle of game-animal', see ghoilos above); Oss. àicítà, pl. ‘testes’; Alb. cf. eth, v. (mate, a cow, fr. *oidsK-?); ON eista, pl. eistna, n. ‘testicle’; OCS jesto & isto, gs: -ese, n. id. See next
12300:orghis ‘testicle’. WP I, 182 Arm. ordz, i-st. s. ‘male’; am-ordzik ('testi- cles", fr. *ombh-? or *som-?); cf. also ordzat ‘capon’; xol-ordz, gs. -i, ab. s. -av ‘orchid’; Gk. órkhis, gs: -eos, m. ‘testicle’; MIr. uirge, Ir. uirghe, f. id.; Cz. cf. orzej (fr. *orogh-? from the tubers on the roots?: “lesser celan- dine"); R cf. kn-oroz, m. ‘boar; Li. cf. iS-arZa “animal w. strangled testicle’; cf. eržilas *colt'; Latv. cf. ērzelis ‘stallion’
15977:skub- (2) ‘tuft? ` Arm. cf. xopop, s. ‘curl, lock’; xopopik, pl. (locks; hairstyle’. Redup. fr. *skub-skub-); Hes. sküba, skoüba, f. (&colewort' or 'nipple- wort’); MHG schopf, m. ‘forelock, topknot'; ON cf. skopt, n. ‘hair’
20054:uerĝh-, alternative to uerĝ- (1), q.v. (Balto- Slav. ambig.). Cf. uergho (1) ON virgill, m. ‘halter; MHG wergel, m. (Cstrangler, fr. *uorghil-); Blg. vrěž, vrěža, f. ‘tendril’; Li. verzle, f. 'screw-nut'; verZe- klis, m. id.; Latv. verzeles, pl. ‘trappings’; Finn. LW verkko ‘net, web’. (Isophones:
```


## [2026-09-07T20:21:04.351Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== AHD watkins upupa/epop ==\"; grep -n -i \"upupa\\|hoopoe\\|epop\" AHD_watkins1985.txt | head; echo \"== AHD orghi ==\"; grep -n -i \"orghi\\|orchid\\|testicle\" AHD_watkins1985.txt | head; echo \"== SKT hoopoe ==\"; grep -n -i \"hoopoe\\|HOOP\" SKT.txt | head",
 "description": "Grep AHD/Watkins and Skeat"
}
```


### [2026-09-07T20:21:04.433Z] TOOL RESULT

```
== AHD watkins upupa/epop ==
868:[populus. People. Latin noun of Etruscan origin. PEO- PLE, POPULACE, POPULAR, POPULATE, PUBLIC, PUEBLO; DEPOPULATE.]
1420:DEODAR deiw-, deru DEONTOLOGY deu-1 DEPEND (s)pen- DEPICT peig-1 DEPILATE pilo- DEPLOY plek- DEPLUME pleus- DEPONE apo- DEPOPULATE populus DEPORT per-2 DEPOSIT apo- DEPRECATE prek- DEPRECIATE per-6 DEPREDATE ghend- DEPRESS per-5 DEPRIVE pert DEPTH dheub- DEPURATE peue- DEPUTE peu- DERACINATE wrad- DERANGE sker-3 DERELICT leikw- DERIVE rei-3 -DERM der-2 DERMA! der-2 DERMA? tera-1 -DERMA der-2 DERMATO- der-2 DEROGATE reg-! DERRIS der-2 DESCANT kan- DESCEND skand- DESCRIBE skribh- DESERTS = ser-3 DESERVE servus DESICCATE selkw- DESIGNATE sekw-1 DESIRE sweid-1 DESIST sta- DESMID dé- DESOLATE s(w)e- DESPAIR spé-1 DESPICABLE spek- DESPISE spek- DESPOIL spel-! DESPOND spend- DESPOT deme-! DESTINE sta- DESTITUTE sta- DESTRIER deks- DESTROY ster-2 DESUETUDE s(w)e- DESULTORY sel-4 DETAIN  ten- DETECT (s)teg- DETENT ten- DETER tres- DETERIORATE de- DETERMINE ter- DETEST trei- DETONATE (s)tene- DETOUR tera-1 DETRACT tragh- DETRIMENT tera-1 DETUMESCENCE teue- DEUCE! dwo- DEUTERAGONIST deu-? DEUTERIUM deu-!
== AHD orghi ==
330:3. O-grade form *bhol- in Germanic *ball- in: a. Old English beallucas, testicles: BOLLIX; b. Old Norse bdllr, ball: BALL; c. Danish bolle, round roll, akin to the probable Scandinavian source of BILBERRY; d. Middle High German baile (> Italian balla, palla), ball: BAL- LOON, BALLOT; PALL-MALL; e. French baile, ball: BAL- LOTTEMENT; f. Old French baie, rolled-up bundle: BALE!. 4. Suffixed o-grade form *bhol-to- possibly in Germanic *balthaz, bold, in: a. Old English bald, beald, bold: BOLD; b. Old High German bald, bold: BAWD. 5. Suffixed o-grade form *bhol-n- in Latin follis, bellows, inflated ball: FOLLICLE, FOOL!; (FOLLICULITIS). 6. Possibly Greek phalaina, whale: BALEEN. 7. Conceivably (but more likely unrelated) Greek phellos, cork, cork oak: PHEL- LEM; PHELLODERM, PHELLOGEN. (The following deriva- tives of this root are entered separately: bhel-?, bhelgh-, bhlei-, bhleu-.) [Pok. 3. bhel- 120.} bhel-3, To thrive, bloom. Possibly from bhel-?. I. Suffixed o-grade form *bhol-yo-, leaf. 1. Latin folium, leaf: ForL?, FOLIAGE, FOLIO, FOLIUM; CINQUEFOIL, DEFOLIATE, EX- FOLIATE, FEUILLETON, FOLICOLOUS, MILFOIL, PORTFO- LIO, TREFOIL. 2. Greek phullon, leaf: (-PHYLL), PHYLLO-, -PHYLLOUS; GILLYFLOWER, PODOPHYLLIN. II. Extended form *bhlé- (< *bhlea-). 1. O-grade form *bhl6- in: a. suffixed form *bhlé-w- in Germanic *bl6-w- in Old English bléwan, to flower: BLOWS; b. Germanic suffixed form *bl6-m6n- in (i) Old Norse blém, blémi, flower, blossom: BLOOM! (ii) Old English bléma, a hammered ingot of iron (semantic development obscure): BLOOM?; c. Germanic suffixed form *bl6-s- in Old English bléstm, bléstma, flower, blossom: BLOssoM; d. Latin flés (stem flor-), flower: FERRET?, (FLORA), FLORA, (FLORAL), FLOR- IATED, FLORID, FLORIN, FLORIST, -FLOROUS, FLOSCULUS, FLOUR, FLOURISH, FLOWER; CAULIFLOWER, DEFLOWER, EFFLORESCE, ENFLEURAGE, FLORIGEN. 2. Germanic suf- fixed form *blé-do- in Medieval Latin bladium, produce of the land: EMBLEMENTS. 3. Suffixed zero-grade form *bhib-to- in Germanic *bladaz in Old English bled, leaf, blade: BLADE. [Pok. 4. bhel- 122.] bhel-4. To cry out, yell. Germanic *bell- in: a. Old English bellan, to bellow, bark, roar: BELL?; b. Old English belle, a bell: BELL!; c, Old English belgan, bylgan, to become enraged: BELLOW; d. perhaps Old English bealcan, *b(iJelcan, to utter, belch forth: BELCH; e. Middle High German buldern, boldern, to make noise: POLTERGEIST; f. Icelandic baula, to low, akin to the Scandinavian source of Middle English baulen, to howl: BAWL. [Pok. 6. bhel- 123.] bheld-. To knock, strike. Zero-grade form *bhid- in Germanic *bult-, missile, in Old English bolt, heavy arrow, bolt: BouT!. [Pok. bheld- 124.] bhelg-. Also bhelk-. A plank, beam. 1. Germanic *balku- in Old English balc(a), ridge: BALK. 2. Germanic *balk6n- in: a. Old French bauch, beam: DEBAUCH; b. Old Italian balcone, scaffold: BALCONY. 3. Suffixed zero-grade form *bhik-yo- in Latin fulcire, to prop up, support: FULCRUM. 4. Possibly Greek phalanx, beam, finger bone, line of battle: PHALANGE, PHALANX. [Pok. 5. bhel- 123.] bhelgh-. To swell. Extension of bhel-2. 1. Germanic *balgiz in Old English bel(ijg, belig, purse, bellows: BELLOWS, BELLY. 2. Germanic *bulgjan in Old Norse bylgja, a wave: BILLOW. 3. Germanic *bolgstraz in Old English bolster, cushion: BOLSTER. 4. Celtic *bolg- in Latin bulga, leather sack: BUDGET, BULGE. [Pok. bhelgh- 125.) bhelu-. To harm. Germanic *balwaz in Old English bealo, b(e)alu, harm, ruin, bale: BALE?. [Pok. bheleu- 125.] bhendh-. To bind. 1. Germanic *bindan in Old English bindan, to bind: BIND; WOODBINE. 2. O-grade form *bhondh- in Germanic *band- in: a. Old English bend, band, ribbon, akin to the Germanic source of Old French bende, band: BEND?; b. Old English bendan, to bend: BEND!; c. Old Norse band, band, fetter: BAND!, BOND; d. Old French bande, bond, tie, link: BAND!. 3. Zero-
415:in: a. Old English twd, two (nominative feminine and neuter): Two; b. Old English fwégen, two (nominative and accusative masculine): TWAIN. 2. Germanic com- pound *twa-lif-, “two left (over from ten),” twelve (*-if-, left; see leik-), in Old English twelf, twelve, and twelfta, twelfth: TWELFTH, TWELVE. II. Adverbial form *dwis and combining form *dwi-. 1. Germanic *twi- in: a. Old English twi- (> Middle English twi-), two: TWIBIL, TWILIGHT; b. Old High German zwi- (> German zwie-), twice: ZWIEBACK, ZWITTERION. 2. Latin bis (combining form bi-), twice: BI-, BIS; BAROUCHE, BISCUIT. 3. Greek dis (combining form di-), twice: DI-!. 4. Germanic *twis in Middle English twisten, to twist: Twist. 5. Germanic *twiyes in Old English twige, twiga, twice: TWICE. 6. Ger- manic compound *twégentig, “twice ten” (*-tig, ten; see dekm), in Old English twéntig, twenty: TWENTY. 7. Ger- manic *twihna, double thread, twisted thread, in Old English twin, double thread: TWINE. 8. Germanic com- pounds “bi-twihna and *bi-twisk, “at the middle point of two” (*bi, at, by; see ambhi), in Old English betwéonum and betweohs, betwix, between: BETWEEN, BETWIXT, (TWIxT). 9. Germanic compound “twilic-, “two-threaded fabric” in Old English twilic, woven of double thread: TWILL. 10. Suffixed form *dwis-no- in: a. Germanic *twisnaz, double, in Old English twinn, getwinn, two by two, twin: TWIN; b. Latin bini, two by two, two each: BINAL, BINARY; COMBINE. 11. Suffixed form *dwi-ko- in Germanic *twig(g)a, a fork, in Old English twigge, a branch: Twic!. 12. Compound *dwi-plo-, twofold (*-plo-, -fold; see pel-3), in Greek diploos, diplous, twofold: DIPLO-, DIPLOE, DIPLOMA; ANADIPLOSIS. 13. Suffixed reduplicated form *dwi-du-mo- in Greek didumos, dou- ble, the testicles: (DIDYMIUM), DIDYMOUS; EPIDIDYMIS, TETRADYMITE. 14. Suffixed form *dwi-kha in Greek dikha, in two: DICHASIUM, DICHO-. III. Inflected form *duwo. 1. Latin duo, two: DEUCE}, DOZEN, DUAL, DUET, DUO-; DUODECIMAL, 2. Greek duo, dud, two: DUAD, DYAD; DODECAGON, HENDIADYS. IV. Variant form *du-. 1. Compound *du-plo-, twofold (*-plo-, -fold; see pel-%), in Latin duplus, double: DOUBLE, (DOUBLET), (DOU- BLOON), (DOUBLURE), DUPLE. 2. Compound *du-plek- (*-plek-, -fold; see plek-), twofold, in Latin duplex, double: DUPLEX, DUPLICATE, (DUPLICITY); CONDUPLI- CATE. 3. Suffixed form *du-bhw-io- in Latin dubius, doubtful (< “hesitating between two alternatives”), and dubitdre, to be in doubt: DOUBT, DUBIOUS; (REDOUBT- ABLE). [Pok. du6(u)- 228.]
456:ergh-. To mount. 1. Suffixed o-grade form *orgh-i- in Greek orkhus, testicle: ORCHID. 2. Suffixed o-grade form *orgh-eyo- in Greek orkheisthai, to dance: ORCHESTRA. [Pok. orghi- 782, ergh- 339.]
1995:ORATORY? Or- ORCHARD gher-1 ORCHESTRA ergh- ORCHID ergh- ORDAIN  ar- ORDEAL dail- ORDER ar- ORDINAL ar- ORDINANCE ar- ORDINARY ar- ORDINATE ar- ORDO ar-
== SKT hoopoe ==
837:Apse.  (I„  — Gk.)     Now  used  of  a at   the   end   of  a   chaich;   fcmnerljp  af. apsis,  a  luming-poinl  of  a  planet's  orbit. L.  afiis,    pi.  af'siilei,   a  bow,  turn.  — Gl A.^U,  a  tjing,  fastening,  hoop  of  a  wh curve,  bow,  arch.  — Gk.  £rr<ir,  to  tie,  bt
3390:iftodDOslk  whooping-cough.  fE)  Put Movi^^MffA;  cf.  Scotch  k»nJt-<oujih, Jkatr  {Atft  meuis  cfugh).  A  ^i'i4  u  a ll  la  the  brcftlh.  UAsaltted  form  of  a RIK.  ro  c^p.  -f  Du.  kinkhacst ;  0. Mtkkim1\  ^ttvA.  hkhesta,  chincout;h, h.  le  nip ;  G  ^fA^H*  to  gasp.  Cf. tUan.Tcijr-lE*
7100:Fret  {^),  a  kind  of  grating.  (F-  —  L.) Common  in  heraldry.  — O.  F.fre/e,  a  ferrule; /refers,  pL,  an  ifon  giatiog  ( Diez)  ;  frttttr^ to  hoop : /np/^*',  fretiy  (in  heraldry).  Cf. Span,  fretes,  frets  (in  heraldry);  Ital.  yirr* nc(a,  an  iron  grating.  —  F.  ferrer,  to  hoop with  iron  — F  fer^  iron  ^\m.  ferrum,  iron.
8822:Hoop  (I).  A  pliant  strip  of  wood  bent into  a  band.  (E.)  M.  E.  noof,  Aof'c.  A.  S. Atfp.  •^  Du.  Afftp.  Cf.  also  Iccl.  A(f/>,  a  bay^ from  its  circular  foim,  prov.  E.  Afffit,  (1)  a hollow,  (3)  a  mound,  according  as  the  cur- vature is  concave  or  cod  vex  Cf.  Skt.  M^^, a  bow,  Gk  K^firruif,  to  bend.  Allied  to Hop  {t\  Hump.
8823:Hoop  (2),  Whoop,  to  call  out,  shout. (F.  — TcuL)  M.  E.  Aoxiptti,  lo  sbouL  — O.  F.  kouptr^  '  (o  hoop  unto  ; '  Cot.  Of Teul.  origin;  cf.  Goth.  Atoo/Joh,  lo  boasL hoopbiff-cough,  a  cougb  accompanied by  a  Aottfi  or  convulsive  noisy  catch  in  the breath.     (Formerly  called  (Aincough,)
8824:Hoopoe,  the  [lame  of  a  bird.  (L.)  L. Hpupa,  a  hoopoe;  the  initial  A  is  due  to the  F.  Auppe,  also  derived  fiom  ttfmfa.^ Gk.  iitouft,  a  hoopoe.  Of  imitative  origin. %  The  F.  Auppt,  a  tuft  of  feathers,  is  from huppe,  a  hoopoe  (from  its  tufted  head) : not  vice  vcrel.
8908:Eubbuo ;  see  Whoop.
16208:Rope.  (E.)  M.  E.  roop.  A.  S.  rdp.  + Du.  rtep,  Icel.  reip,  Swed.  «/,  Dan.  reb\ G.  rtif,  circle,  hoop,  ring,  sometimes  a rope.     Der.  rop-y,  stringy,  glutinous.
19760:Tire  (3),  a  hoop  of  iron  that  binds  the fellies  of  wheels.  ^F.-TeuL  ?)  *  Tin.  the ornament  of  womcns  heads,  the  iron  hand of  a  cart-wheel,*  Fhillips,  ed.  1706.  Prob. identical  with  lire,  a  woman's  bcad.drcss. Tirt  meant  to  deck,  also  to  arrange. raUgrave  has :  '  I  tytr  an  cgce,  Jf  en- foustrc;  I  ty^  with  garmcntea.  Sec  Sec tire  (3),  s.  V.  Attire.
20741:forthlngalo,  fardingale.  a  hooped petticoat.  (K.  —  Span.  —  L.)  O.  F.  veniu- /o//f,  'a  varilingall ;'  Col.  -Span,  vttdu- gaJo^  a  farthingale,  lie.  'provided  with faoopa.*  —  bpan.  verifujio,  young  shoot  of  a tret,  rod,  hoop.  —  Span.  Vfn/e,  green.  —  L. mriJis,  green.
```


## [2026-09-07T20:21:19.853Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && echo \"== upupa ==\"; grep -n \"upupa\\|Wiedehopf\" WLD_Bd1_pages.txt | head -20; echo \"== orghi ==\"; grep -n \"orghi\\|órghi\\|Hode\" WLD_Bd1_pages.txt | head -20",
 "description": "Grep Walde-Pokorny Bd1"
}
```


### [2026-09-07T20:21:19.915Z] TOOL RESULT

```
== upupa ==
11145:epop. opop Ruf des Wiedehopfs.
11146:     Gr. enonoi nonono Ruf des Wiedehopfs, sjiof, -onog „Wiedehopf “, i'rwma
11152:   lat. upnpa „Wiedehopf“, ndd. Hupphupp u. dgl.,         arm. popop, npers.
11153:pupil, lett. puppukis ,,Wiedehopf‘ (s. Suolahti Yogeln. 12).    Ahnlich, aber
11154:unredupliziert, osorb. hupak, poln. hupek „Wiedehopf“, osorb. Iiupac ,,wie
11155:ein Wiedehopf schreien",                      vgl.         auch allgemeiner slovak. hnpati „schreien“,
70509:              u                                  „tuten“ tuthjs, tututis „ Wiedehopf“
== orghi ==
1674: laidon „natales‘ zu ai. putrd- „Sohn, Rind ', lit. paiitas „Ei. Hode“ zu stellen
2083:(aus apa-*avaya- n. „Ei, Hode“ = np. xaya s. Justi IA. 17, 87, Bartholo-
2136:Das ahnliche Verhaltnis zwischen lit. pailtas „Ei (und Hode)“ lett. pubis, :
12107:  *neg'ih-ros „Niere, Hode“ („rundliche Anschwellung", vgl. zur Bed.
12108:lit.inkstas „Niere“ und „Hode“; -ro- und -en- vielleicht Entwicklungen
12111:„Nieren,        Hoden“ (a. zum lautlichen Yf. IF. 19, 102);
12112:       ahd. nioro „Niere“,T. auch „Hode“, mengl. mnd. nere, aschwed. mure,
13414: der Bed. „geil“ zu doyiz, av. anzi- „Hode“, (Fick III 4 19 zw.; in wegen
15062:usw. „Weicben, Darm, Hoden“ (i-Formans wie in lanita „\Vange“, is to
15063:„Niere“, lysto „Wade“, usta „Mund“) in wruss. jal'ity ,,Hoden“, serb. alt
15191:(= mhd. ei$cl „kleines eiterndes Geschwiir       aisl. eista „Hode“ ( *oid-s-to(n )-,
15219:zu yeben) und ksl. isto, pi. istesa ,,Hode, Niere" aus schwundstufigem *id-
15245:Hoden", jedrny ..kernig, kriiftig, riistig" (usw..                           s.   Berneker 455 f., Bruckner
16677:182                                            ondho               orghi-, jghi
16755: ofglii-, rghi-                 m. ..Hode"     (vielleicht           auch *erghi-).
16756:   Av. onzi- m. „Hodensack“, Du. orozi „Hoden“, ai. urir-rjika- „mit siclit-
16757: bar gewordenen. d. h. hervortretenden Hoden“ (Geldner ZdMG. 52, 746 a 2,
16766:  Arm. orji-R pi. „Hoden“, orji „nicht kastriert" ( *orghi-ios ), mi-orji ,.u6v-
16768:   gr. oq'/js m. „Hoile“; alb. herde f. „Hode“ (G. Meyer Wb. 151; nach
16772:Gdf. dann orghi-a vgl. zu ausl. -e aus betontem -a Pedersen KZ. 36. 279);
```


## [2026-09-07T20:21:32.927Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '11135,11146p' incoming/WLD/WLD_Bd1_pages.txt; echo \"== MON orkideh ==\"; grep -n \"ارکیده\\|اركیده\\|اورکیده\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head; echo \"== MON pupu ==\"; grep -n \"پوپک\\|پوپو\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt 2>/dev/null | head",
 "description": "WLD page marker; grep Mo'in"
}
```


### [2026-09-07T20:21:33.026Z] TOOL RESULT

```
pi „zum Sohne“, lett. ap- „um, fiber“, p'le mit Gen. und Acc. „bei, an“, p'le-
„hinzu,      an-,         voll-“:      apr.   ep-          (ap-      nicht mabgebendere Schreibung), eb-
„be-“,     eher           als    *cpi hierlier,            als     unter Zugrundelegung der Form rb- zu
idg. iblii , obhi (siehe               Trautmann Apr 330, Brugmann II 2 2, 820).
     Ygl. Curtius 5 261;               Brugmann II 2 2, 838, wo auch fiber das Syntaktische
und fiber Gleichungen wie ai. api-dha-,                                       gr.       im-zidyu,        lat.     obdo,   lit.   ap-dcti.


epop. opop Ruf des Wiedehopfs.
     Gr. enonoi nonono Ruf des Wiedehopfs, sjiof, -onog „Wiedehopf “, i'rwma
== MON orkideh ==
== MON pupu ==
incoming/MON/MON_2vol_Adena_v1_djvu.txt:32979:پوپش: کد-ع5م [- پوپه - پوپکك - پوپو - 
MON_part1.txt:32979:پوپش: کد-ع5م [- پوپه - پوپکك - پوپو - 
MON_part2.txt:89304:شانه‌بس» پوپکك» بوبکث» مرغ سلیمان
```


## [2026-09-07T20:21:34.464Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && grep -n \"پوپک\\|پوپو\" ARY_pages.txt | head; echo \"== latin index ==\"; grep -n -i \"PUPAK\\|PUPU\\|HOOPOE\\|ORCHID\" ARY_latin_index_pages.txt | head",
 "description": "Grep Aryanpur"
}
```


### [2026-09-07T20:21:34.527Z] TOOL RESULT

```
5206:۷۸ پوپوایک (به چم
5226:فارسی (/(۳87۶]4): پوپو, پک (به چم ایّریُر"یا اشانه سر) ۸4 ,8177
== latin index ==
5100:pUpO, PUPAK (yu Gd" Lh 8 as) Sacgugs (PERSIAN) gus
5101:HOOPOE gu ath 50 5Ny pa aul oie
5108:SKEAT: (HOOPOE) 276 (OLD HIGH GERMAN) <5 glalT
```


## [2026-09-07T20:21:40.337Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '32960,32995p' MON_part1.txt",
 "description": "Print Mo'in context for pupu"
}
```


### [2026-09-07T20:21:40.381Z] TOOL RESULT

```
باریک کنند. 


نیک فرهنگ فارسي معیر ۳۷۱ 


بنیرک: -0201۲ (امر .) (کیا.) گیاهی از 
تیرة بنی رکیان که پابا است و ارتفاعش ۳۰ تا 
۰ سانه نتبمتر و دارای ک رک‌های دراز است 
که به حالت خودرو در جنگل‌ها و اراضی 
غیر مزروع روییده می‌شود. 

پو: ۲5 [- پوی» ری. پوییدن] (.) رفتار وسط 
که نه تند باشد و نه کند» پوبه. دو. 

پوپ: 05۲ (.) تاجی از پر که بر سر بعضی 
از طبور دیده می‌شود؛ کا کل مرغ. (جاد.) 
پوپش. 

پوپش: کد-ع5م [- پوپه - پوپکك - پوپو - 
بویوء کر ] (اصت.) (جاد.) هدهد» شانه‌سر. 
بویک: ۷ [- بویش ] (.) (جان.) هدهد» 
شانه‌سر. دختر یک دوشیز ه. 

پوت: :05 جگر گوسفند. خوراک قلیه که 
از بوت سازند قلیه پوتی 

پوت: 05۰ (.) اقسام خوردنی» انواع اطعمه 
و اشر یه لوت. 

پوت: اتاه [- پوط» رس.] (!.) مقیاس وزن 
توافت فتعاوان ۰ کیلوگرم 
(قریب ۵ من تبریز و کسری). ضح.- در 
گیلان و مازندران و آذربایجان مستعمل
```


## [2026-09-07T20:21:42.242Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && sed -n '5195,5240p' ARY_pages.txt; echo \"=== pdf page tag ===\"; awk 'NR<=5240 && /\\[pdf page [0-9]+\\]/{p=$0} END{}' ARY_pages.txt; grep -n \"\\[pdf page\" ARY_pages.txt | awk -F: '$1<5240' | tail -3",
 "description": "Print Aryanpur pupu entry"
}
```


### [2026-09-07T20:21:43.577Z] TOOL RESULT

```
بادداشت:
این واجريشه با واجریشه‌ای که واژه‌ی 8181067/8 از آن آمده خویشی نزدیکك دارد (پسگشت: 808 :۳01607779
,383-384 (۲13683) :7 0۸31۸)
اوستایی (1]55700۷ < بلرچی (81لناءا8۸): 0
1 ,7 ,8۸7710 سانسکربت (54۸/5777): 2۸78
پارسی باستان (۳8۴۵14۸ 010): آرمنی (4/۸45214/7): 1 ,808
1 ا2۸۷3 برنانی (0781520): ۲۸۵5
پهلوی (1/ ۸1 ): رل ۱۱ لاتین (710ا): ۳05 205
اوستی (05587/6): 0 گرتبکه (ع007741): ۲17۸77
کردی (6(87018): 20 ایسلندی کهن (010۸۷4۷بی5 صا0):
[pdf page 177]
۷۸ پوپوایک (به چم
۸ پسگشت‌ها کت
فریزی کهن (۶/914/0 0۵0): ۰ ۳۸۵ ,۳۸53 09 رورم
آلمانی گهن (087۵1۸۸ 04 ]بط صا0): » . + فهم8
20 ,85۸1 3 (۲100) ,764 0۸5 اد رد
آلمانی (0657/۸/۷): ۳2۸0 رد ند نها
انگلیسی کهن (تلقلاه(8 صا): ۰ ۲210 1 (۸0۷1۳5) ,64 (۸370ه)
انگلیسی (4لولاه/(8): ۳۸71 40 (0۸71) ۸
هلندی (4ل0076): زد (۳۸7) :0/08
اسلاوی کهن (ع1/ها5 بلع#تابل صت۵): 6 (5180) ,657
1 8007 4 (0۸73) +57
پروسی کهن (/۳055 صا0): ۰ 21۸115 2 (0۲166ه) ۸0
: برهان قاطع ؛ ۴۳۲
یادداشت:
چم این واژه در زبان اوستی: آرزو میل.
چم این واژه در زبان لاتین: پل,
چم اين واژه در زبان‌های گوتبکه و ایسلندی کهن: پافتن.
چم این واژه در زبان‌های دیگر واژگان این فهرست: راه.
۲- برخی واجریشه‌شناسان معتقدند که این واژه از بکك زبان ایرانی به زبان‌های اروپایی راه یافته است. تغییر معنی اپر
واژه از آراه" به "رهنمود" در زبان‌های فارسی و کردی و بلوچی منطقی بنظر می‌رسد.
فارسی (/(۳87۶]4): پوپو, پک (به چم ایّریُر"یا اشانه سر) ۸4 ,8177
چم آنگلیسی سرواژه‌ی فارسی: 10000
هند و آروپایی (۰)/۸00-210720۷ ,۹5807
کردی (78.015): زتولاها لتونی (لتی) (/7۷1با): نی اد ابا
ارمنی (048۸//4/): 7007
بونانی (07886): 205 پسگشت‌ها مینست
لاتین (7100ل): 10۸ 1
فرانسه (۳52/2): 10 0 (31۳۳8) :امد
آلمانی کهن (/(05824۸ هط صاه): 6 (1100708) +7
10۸ 35 (10400)) انم
لهستانی (34ل]۳0): و در برهان قاطم + ۳۳۵
اسلا کی (5107430): 11
[pdf page 178]
۹ ها و
یادداشت:
=== pdf page tag ===
5176:[pdf page 176]
5205:[pdf page 177]
5238:[pdf page 178]
```


## [2026-09-07T20:22:01.735Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A7%D8%B1%DA%A9%DB%8C%D8%AF%D9%87/",
 "prompt": "What do the Persian dictionaries (فرهنگ فارسی معین، دهخدا، فرهنگ عمید) say about ارکیده — meaning and stated origin (French/English)?"
}
```


## [2026-09-07T20:22:02.445Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/orchid%C3%A9e",
 "prompt": "French orchidée: etymology (New Latin Orchideae, date of attestation), and descendants/borrowings into other languages (Persian, Turkish, etc.)."
}
```


### [2026-09-07T20:22:07.718Z] TOOL RESULT

```
# Orchidée - French Word Definition

**orchidée** is a French noun (feminine, plural: orchidées) meaning "orchid."

## Etymology

The word was "Borrowed from New Latin _Orchideae_, Orchidaceae, an irregular formation from Latin _orchis_," which traces back to Ancient Greek ὄρχις (órkhis).

## Pronunciation

The IPA pronunciation is /ɔʁ.ki.de/, with audio recordings available from Swiss French (Valais), French from Lyon, and French from the Vosges region.

## Language Descendants

The French term influenced other languages through borrowing, including:
- German: Orchidee
- Dutch: orchidee
- Swedish: orkidé
- Norwegian: orkidé
- Romanian: orhidee
- Turkish: orkide
- Estonian: orhidee
- Malagasy: orkide
```


### [2026-09-07T20:22:07.846Z] TOOL RESULT

```
# Persian Dictionary Definitions of ارکیده

## Meaning

The Persian dictionaries define ارکیده as:

**فرهنگ فارسی**: "A plant from the fox-tail family with beautiful flowers, planted as an ornamental plant"

**فرهنگ معین**: Describes it as "a plant from the fox-tail family whose varieties possess beautiful flowers and are cultivated as decorative plants in gardens or pots"

**فرهنگ عمید**: Lists two definitions—a type of red and pink flower with one petal larger than the others, and the herbaceous decorative plant itself from the fox-tail family

## Stated Origin

All three dictionaries identify the word as **French in origin** (فرانسوی), with the English equivalent being "orchid." The etymological note indicates it derives from the Greek term "orchis" (meaning testicle), which the Swedish botanist Carl Linnaeus formally adopted in 1753 for this flower genus.
```


## [2026-09-07T20:22:17.301Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/orchid",
 "prompt": "Quote the etymology of orchid: date (1845?), Modern Latin Orchideae, the false genitive orchidis, Latin orchis, Greek orkhis, PIE root, and mention of Middle English ballockwort."
}
```


### [2026-09-07T20:22:22.403Z] TOOL RESULT

```
# Etymology of Orchid

**Date of Introduction:** 1845, when botanist John Lindley introduced the term in "School Botany."

**Etymology Chain:**
The word traces back through Modern Latin *Orchideæ* (Linnaeus) to Latin *orchis*, then Greek *orkhis*, ultimately deriving from a Proto-Indo-European root meaning "testicle."

**Key Quote:** "The plant so called because of the shape of its root; Greek *orkhis* also was the name of a kind of olive, also so called for its shape."

**Earlier English Usage:** Before the modern form, the plant appeared in Latin as *orchis* (1560s) and in Middle English as *ballockwort* (circa 1300)—a direct reference to the anatomical shape that inspired the name across multiple languages.

The botanical nomenclature reflects how ancient peoples recognized the resemblance between orchid root structures and human anatomy, a naming pattern repeated across Indo-European languages from Armenian to Lithuanian.
```


## [2026-09-07T20:22:27.903Z] TOOL CALL #46: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%D9%BE%D9%88%D9%BE%DA%A9\" \\\n \"https://en.wiktionary.org/wiki/%D9%BE%D9%88%D9%BE%D9%88\" \\\n \"https://en.wiktionary.org/wiki/upupa\" \\\n \"https://www.etymonline.com/word/hoopoe\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 375, root Opop: Persian pupu/pupak, Latin upupa, English hoopoe - onomatopoeic origin\" 2>&1 | tail -2\ndone",
 "description": "Archive Opop sources"
}
```


### [2026-09-07T20:22:30.646Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/723500002799194b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8b84464d2757e648.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d5033952bfa145d3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f07a635ea6c24be7.txt
```


## [2026-09-07T20:22:37.391Z] TOOL CALL #47: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/orchid\" \\\n \"https://en.wiktionary.org/wiki/%E1%BD%84%CF%81%CF%87%CE%B9%CF%82\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81%C3%B3r%C7%B5%CA%B0is\" \\\n \"https://en.wiktionary.org/wiki/orchid%C3%A9e\" \\\n \"https://www.etymonline.com/word/orchid\" \\\n \"https://abadis.ir/fatofa/%D8%A7%D8%B1%DA%A9%DB%8C%D8%AF%D9%87/\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 375, root Orghi: Avestan arezi, Greek orkhis, Latin orchis, French orchidee, Persian orkideh, English orchid\" 2>&1 | tail -2\ndone",
 "description": "Archive Orghi sources"
}
```


### [2026-09-07T20:22:41.708Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/c9b3333f78e7da9a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8918518aafee7d40.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ee6698ebcc9c628d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a05ff01c7dfbffcb.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/aff3e382b7a225aa.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/966648906fa63008.txt
```


## [2026-09-07T20:22:50.847Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== BRT Hodensack ==\"; grep -n \"Hodensack\\|Hoden\" BRT.txt | head -10; echo \"== HRN pupu/Wiedehopf ==\"; grep -n -i \"pupu\\|Wiedehopf\" HRN.txt HUB.txt | head -10; echo \"== ISS/DKS ==\"; grep -n -i \"hoopoe\" ISS_alt_DKS.txt | head -5",
 "description": "Grep Bartholomae, Horn, Hübschmann"
}
```


### [2026-09-07T20:22:50.923Z] TOOL RESULT

```
== BRT Hodensack ==
7690:•  j.  «razay-  m.  'Hodensack':  'zöiS  xa "die  Quellen  des  Hodensacks"  Yt.  i4~ 39.         a)  Du.  'Hoden':  'zi  (ND.)  F.jg.
14213:PPfP.  lum  gr.  V.  %paiM;  vgl.  draohSvata-.  — 1)  Hda.  madr°.  —  ')  Oder  vll.  'dem  die  Hoden zermalmt,  zerqueischt  sind,  entmannt'.
18018:•  j.  fraäana-  m.  'Hodensack':  'mm  F.jg. El  und  Bed, ?  —  Pü. :  Vamli,  in  einer  jungen Hds.  mit  np.  xäyagän  iälad  gloaiit,  ZPGl.  51 No.  3.
== HRN pupu/Wiedehopf ==
HRN.txt:3158:333. inipü, püpe, püpek 'Wiedehopf; auch hühü etc.
HRN.txt:3159:Lat. upüpa 'Wiedehopf; gr. snoifj.
HRN.txt:3162:B r e h m , Vögel II : *Wenn zwei Wiedehopfe streiten,
HRN.txt:3182:^) Nach griechiöcher Anschauung ruft der Wiedehopf nov nov,
== ISS/DKS ==
1297:ysyama (-ya- for -ü-), = 11i 46:16 kakva tcirauka u papüska bimjakye, = u1 34:8 kakva tcirüka и papüskya bejakyá, with diferent ш 37:29-30 stürye papüsakyd bidye baijakye ysümá ‘starling, kakva, hoopoe, sparrow, ysüma-', beside tcirauka 'anas casarca, BS cakraváka-, and bīdye ' pecker, BS ріка-(?)'. The further passage ш 96:6 [[/(mü)ra kakye mūra sye mūra hayarida nva kşama àsaijvà ће... birds, the ka&ya-birds, the geese sport themselves at will in the pools’, and the passage t1 75:62 hai tha mürd kakva jastüfia mūra ka tcadá mahasamümdrá ' О you bird kakva, celestial bird, if beside the great sea’, both would suit for kakua the meaning ‘duck’, Two connexions are possible, 1. kakva ‘duck’ as the ' quacking' bird, to be associated with O.Ind. koka- ' duck, cakravaka-', or 2. Zor.P. kpg *kafig, N.Pers. kabg, Greek коккерт, Eastern Pers. kauk ' partridge’. Tokhara A has kok- lw from O.Ind. &oka-. For Waxi kik, kīk ' wild dog’, cf. O.Ind. koka- ‘wolf’.
2845:tcirau 'duck', Z 22:135 sye varata tcirau йсе ' geese there, ducks, (wild) ducks’; rr 35:32 asna tcīrauka п Пага 'doves, ducks and partridges'; rt 3:8 kakva tcirüka u papüskya 'the kakva-bird, duck and hoopoe’; = tt 36:3 teimrrauka, = t 46:16 kakva teirauka u papüska; Z 20°16 ku Һатіха ana, ісітаика daindà duva 'where seated together two ducks are seen'; =V 56, ti4v1i tcirauka d(ai)ndà du(va) ‘two ducks are seen’; n 8:123 khu paradaisai icirauka ‘like ducks in a foreign land’ (BS para-deta-); К. 26:130 ћатуа brrivausta basta fuje vira ita На khu tcarrüka 'they became bound in love to one another like ducks’, =I 18:199; once with js- for te- Ш 43714 sa khu jd syai jsirauvd uc süjai ksaijidd ‘as geese, ducks, (wild) ducks (i£ ucë= ace) cry out оп one another’. From *čayravāka- to Zor.P. Аш *£axravüka- (Vid. 2:42), O.Ind. cakravüka- 'anas casarka', proverbially faithful in connubium, as in Atharva-veda 4:42:64 cakravükéva ddmpati ‘master and mistress of the house like two ducks’. Suffix -ka- to final -au, as hamau, hamauka ' vessel’, dro, drauka- ‘hair’, For -ir- from -agr-, see sira- ‘contented’,
4082:papüskyá 'hoopoe!, in list of bird names, Ш 35:31 papū- Зуй, == 47:48 papiskyi; Sogd. Bud. pwp'pyhi, Chorasm. uopiyk, N.Pers. pipak, pūpū, Suyni bubübak, abūbāūk; outside Iranian, Greek &roy, Erroros, Lat. upupa, Armen. popop, Lit. pupitis, Let. pupukis, bupucis. With suffix -ikya-, as 11 75:58 teimmitkya- ' eye', K. 43'146 tcimaskyi.
5276:bidem ‘upon them’, К. 142-1050 bide-m uhānä pasimdá ‘they send control (= blessing) upon them’ (uhana- = BS adhisthana-). See benda. bidye ‘bird name’, ш 37:29-30 stürye papüikyd bulye baijakye ysiimá ‘starlings, hoopoes, pies, sparrows, rook’, replaced by kakva ' partridge' in 11 33:31 and п 47:48. Possibly base bai- beside pai- (of the woodpecker's sound), *piyaniika-  pindiya- >bidya-. IE Pok. 999 Lat. pica ‘magpie’, Picus ‘woodpecker’, ОНС speht, O.Ind. pika- ‘Indian cuckoo’. bina ‘to be gazed at, longed for’, rt 104732 Ёйуга bina ‘admirable jar’ from *vrna- to base vain- :vin- ‘see’ (see s.v. avida). bimna 'of the wind’, adjective to bata- ‘wind’; compound, binna-vrrará ' having wind nature’, See s.v. bàta-. bina- ‘grove’, ш 105-16 narada Ыпайа 'he went out into the grove', from *vanya- to vana- 'tree, wood', see s.v. banhya- ' tree’. bina ‘musical instrument; harp, lute’, 2 13:111 Айо batána seräte bina ‘аз the instrument is moved by the wind’. Parallel to Maitreya-vyükaraga (ed. S. Lévi, Études d'orientalisme à la mémoire de К. Linossier, Ir, 1932, 383, 18-9) rlum bskyod ta-la de-dag-las sñan-pahi sgra ni ‘le vent dégage de ces tālas des sons harmonieux’. Also TH 47:57 ranija bina ‘a jewelled instrument’; K. 37:120 ttye vaski та shi khū vari parítá auestá ' for her let him touch the instrument so that he may escape without danger’, = К. 28-180 ttye va bina ski и ft(a) pafsta apvaine ‘for her let him touch (=ріау) the instrument and assuredly he will escape without fear", =K 21:5 ttye va bina {Еп u stā ратна, With -zna-, binana- "instrument of music’, Z 23:138 binanë hastama nāmda ‘they took the best instruments’; ш 106:32-3 binauna улаа damida 'they play the instruments; they blow thern'; abstract suffix -afa-, binasa- ‘music’, SuvO. 68у7 satü ysare -hinaiia ükgyuttündd yaná 'they began to make 100,000 (kinds of) music’, BS zzrya-fata-sahasra-; dyadic K 64, Bov4 paja-ttaryauga binauiia ‘music’ (BS pancaturyanga-); SuvP. 72:2 бїпайа pamcatturyamga, BS vinü-mrdangàáh pauavàh sughogahah. Z 5:87 spátyau binarina Бйпа ' with flowers, with music, with incense’, = Manj. 412 baña buna spyau jsa, = Мап). 429 bīnāña bunau spyau jsa; Z soo Мпййа wicitra ‘various music’, = Мапј. 414 bm(a)ña aşkūstai запа ' music although untouched’. On the Iranian side to the base Bina-, Sogd. Man. wyn’, yn kh, Sodg. Chr. wyn’, Zor.P., Gr.Bd 1307 (T D2) wn! *vin, and Husrau ut retak-e 13; 62; Armen. lw om, O.Ind. vīnā. Note also Japanese biwa ‘lute’, from Chinese p-pa <b'ji-b'a (K 7149; 68310). Origin uncertain. Arab.-Pers. шап] is perhaps from *шїп-Са-. Translated *harp' s.v. рапау-. binam- 'open', causative binem- (from ‘bend apart’), Z 22:128 сї hiv kiri hämäte hvamdu атаа binamáte пиа "when a man is to do his private act (defecate), then the earth opens up’; HI 104744. fada ha binamizye brrī sattà vahant ЧЕ the earth should open up, the beloved being descend’, =H 108:4 ‘ayda ka bindmave brri satta valhani. Causative, 11 r, sra =I 8, rsv3 balysüite byamna vasüja binema u pahaita ‘cleanse, open, and drive away the obscuration. (obstacle) to bodhi-knowledge';
```


## [2026-09-07T20:22:53.179Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== FSD hoopoe ==\"; grep -n -i \"hoopoe\" FSD_vol1.txt FSD_vol2.txt WEB_vol1.txt | head -5; echo \"== FSD/WEB orchid ==\"; grep -n -i \"orchidaceae\\|^orchid\" FSD_vol3.txt WEB_vol1.txt | head -5; echo \"== SYN 4.49 whole para ==\"; awk 'BEGIN{RS=\"\\f\"} NR==296' SYN.txt | head -30",
 "description": "Grep Funk&Wagnalls/Webster; SYN next leaf"
}
```


### [2026-09-07T20:22:54.459Z] TOOL RESULT

```
== FSD hoopoe ==
WEB_vol1.txt:60250:ance. dud’m6 (dw5’), n. [It.] a cathedral. dui’6-tone, a. showing a two-tone color effect. dū’ō-tōne, x. a picture having a two-tone color effect. x di’6-type, n. in photoengraving, a print pro- duced from two half-tone plates made from the same negative, but etched separately. dup, v.t. [for do up.] to open; as, to dup a door. [Obs.] dup’a-ble, a. susceptible of being duped. dupe, n. (Fr. dupe, from OFr. dupe, duppe, GE hoopoe, a stupid bird.] a person who is easily deceived; one easily led astray or fooled. 5 dūpe, v.t.; duped (dūpt), pt., pp-; duping, ppr, (Fr. duper, to dupe, take in, from dupe, on A easily taken in.] to deceive: to trick; to cheat. up’ér, n. one who dupes. 3 z dip/ér-y, ”.; pl. dūp’ēr-ieş, a duping or being duped; deception. 3 A dū’piðn, n. [Fr. doupion; It. doppione, nor doppio; L. duplus, double.] a double cocoon, formed by two silkworms. dū’ple, a. [L. duplus, double.]
WEB_vol1.txt:91962:hoop, n. same as hoopoe.
WEB_vol1.txt:91981:upupa, a hoopoe; prob. imitative aipe It,
FSD_vol1.txt:42530:hoopoe  nightjar  reeve  turkey
FSD_vol1.txt:42624:9.  Hoopoe  ( Upupa,  epoos).  Vfe
== FSD/WEB orchid ==
WEB_vol1.txt:73829:orchids, the only known species being the ecasin flower.
FSD_vol3.txt:49137:orchid of the kciius t'ataaetum, remarkable malnlv for Us
FSD_vol3.txt:168821:orchids and milkweeds {Asclcpiadacev) , a polllnlum p.-
FSD_vol3.txt:227345:orchids 3. Karl von, Raron (Vitl788-i/i«1869). a Ger-
FSD_vol3.txt:246266:orchids - Canada r„ the buttiTfiy-wecf] - Ciongo r..
== SYN 4.49 whole para ==
pillars’, ‘props of a mast’, etc., hence ‘testicles’, just as biéywo. ‘twins’ was also used in this sense (Galen, etc.). Cf. (but without a aay explanation proposed ll ce er, Zur lat. Sprachgeschichte ter titine din ; poe oes hess’ to te ti a pepicetion oe ‘wit slang { di. Rs ss !) and quoting Fr, tifiuenead esticles (student’s slang ed by Latin associations?)
Lat, coleus (> Py : ns?).
ab, *coleo Pt | coutlle, Rum. cot; con), etym, “dub ae ne
EW 2036, 2038. e-H. 1.244,
um. bog (or b ‘ 0 oe, fr, Vat. et tant.), ena orsa, ete.) = er’, REW ‘
orig. ‘leather bag’ » Grk. Bipoa ‘hide, 1432. Puscariu 210.
 Macraille, Np. magairle, prob.
Digitized by Arya Samaj Foundation Chennai and eGangotri
HE BODY; BODILY FUNCTIONS AND CONDITIONS 257
epd. of which the first member is related to Ir. macc, W. mab ‘son’, etc., but final member? Pedersen 1.128.
Ir. uirge ‘testicle’, not ‘penis’ (K. Meyer, Ber. Preuss. Akad. 1912.800), see above, 1 and Pedersen 2.662.
W. caill, Br. kell : OE sceallan, OFris. skal ‘testicles’, possibly as ‘scrotum’ fr. ‘leather bag’, fr. the root *skel- ‘cut, split’ (cf. ON hredjar, etc., below, 4). Walde-P. 2.592.
4. ON eista, prob. : ChSl. isto, be- low, 6.
ON boglir, usually ‘ball’ but also ‘tes- ticle’, OE beallucas (pl.), ME ballok, NE ballock (but more commonly bails in vulgar speech) : OHG ballo, balla, etc., ‘ball’, Lat. follis leather bag, bellows’, Grk. dadnos ‘phallic emblem’, all from a root *bhel- ‘swell’. Walde-P. 2.177 ff.
ON hredjar (pl.) ‘scrotum with tes- ticles’ (NIcel. ‘testicles’), Dan. redder, OE herpan ‘testicles’, prob. orig. ‘scro- tum’ as ‘leather bag’ : OE heorfa ‘deer- skin’, OHG herdo ‘vellus’, Lat. cortez ‘bark, rind’, scortwm ‘skin, hide’ (here also late scrotum?). Walde-P. 2.578. Falk-Torp 981.
OE sceallan : W. caill, above, 3.
Dan., Sw. sten, as also ME, NE stone frequently used for ‘testicle’.
Du. teelbal, zaadbal, cpds. of telen ‘beget’, and zaad ‘seed’ with bal ‘ball’
(cf. above).
OHG hodo, MHG, NHG hode, prob. : W. cwd ‘scrotum’, Grk. cxizos ‘leather’, Lat. cutis ‘skin’, OE hyd ‘skin, hide’, etc., fr. [E *skeu-t- ‘cover’ (semantic develop- ment from ‘leather bag’, ‘scrotum’ as in ON hredjar and W. caill, etc., above). Walde-P. 2.549. Falk-Torp 425.
5. Lith. pautas, Lett. pauts, orig. ‘ege’ (4.48).
6. ChSl. isto (pl. istesa ‘kidneys’, ORuss. du. jestesé ‘testicles’), prob. : ON eista ‘testicle’ (both combined under
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri °
258 SELECTED INDO-EUROPEAN SYNONYMS
*id-s-to-, *oid-s-to-) and Grk. oléos ‘swelling, tumor’, oldua ‘swelling’, etc.
Walde-P. 1.166. Berneker 434 f.
ChSl. *jedro, Russ.-ChSl. jadro ‘ker- nel, testicle’, Pol. jadro ‘kernel’, pl. jadra ‘testicles’ (Boh., Russ. jadro ‘ker- nel’), etym.? Perh. as orig. ‘swelling’ and fr. a nasalized *ind- : ChSl. isto, etc., above, but other combinations, as
with Skt. anda- ‘egg, testicle’, possible. Walde-P. 1.166. Berneker 455 f.
ChSl. lono ‘bosom, lap’ (as in Russ., Pol., etc.), late ChSl. also ‘testicle’,
```


## [2026-09-07T20:23:14.244Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3150,3190p' HRN.txt; echo \"=== leaf/page ===\"; python3 - <<'EOF'\ntxt=open('HRN.txt',encoding='utf-8',errors='replace').read().split('\\n')\nleaf='\\n'.join(txt[:3158]).count('\\f'); print('HRN leaf',leaf,'printed',leaf-21)\nb=open('BRT.txt',encoding='utf-8',errors='replace').read().split('\\n')\nleaf='\\n'.join(b[:7690]).count('\\f'); print('BRT leaf',leaf)\ni=open('ISS_alt_DKS.txt',encoding='utf-8',errors='replace').read().split('\\n')\nleaf='\\n'.join(i[:4082]).count('\\f'); print('DKS leaf',leaf)\nEOF",
 "description": "Read Horn 333, compute leaves"
}
```


### [2026-09-07T20:23:15.658Z] TOOL RESULT

```
unmögliche Erklärung des Wortes aus sem. p^ + dästen zugeschrieben
habe. Sie bleibt vielmehr Fr. Müller allein reservirt.
^) FJ und FR belegen es durch folgenden Vers Kemal Isma'll's
(Metrum: Xeflf):
bä ekäbir heniejlis ü ^elvet
guft ü göy'l penäm^ mex^ähem.74 -
haben (die Wörterbücher erklären allierdings das
erstere durch das letztere).
333. inipü, püpe, püpek 'Wiedehopf; auch hühü etc.
Lat. upüpa 'Wiedehopf; gr. snoifj.
kurd. papü (H.-Sch.), päpü (JJ.).
Der Name ist onomatopoetisch gebildet (vergl.
B r e h m , Vögel II : *Wenn zwei Wiedehopfe streiten,
rufen sie unablässig hup^ auch wohl hup-puli) ^).
Die neupersischen Formen mit p sind denen mit b
vorzuziehen (vergl. auch das Gazophylacium, das beide
hat).
334. püde *faul, verfault', päsiden (Inchoat.) *faulen .
aw. päiti' Täulniss, apuyant- *nicht faulend'; phlv.
pütaky püslnitan, püs(i)sn^ arm. LW. put (aaß^pog, v6&og) ;
skr. püyati (Brahm., Sütr.), ai. piiti- *faul, stinkend'.
oss. d. am-bud, t. ämbid ^faul* (18).
335. poz 'Partie um die Nase* 2).
g. püz,
kurd. püZj pöz; bei. pöz, pönz, n. pönz 'Nase (310);
aiy, pöza^ paza ; sangl. fuzik, minj. foska,
oss. d. finje, t. fing 'Nase' (286), arm. pinj (pinS)
'Nasenloch* will Hübschmann hiervon trennen ;
aber vielleicht mit Unrecht. Urverwandtschaft ist
doch gewiss vorhanden (nachträgliche Nasalirung).
336. pöziS 'Reue, Entschuldigung', pöztden (Vis und Kämm, ^
S. 92 Vers 3).
^) Nach griechiöcher Anschauung ruft der Wiedehopf nov nov,
d. i. 7IOV uoa flai (nämlich Procne und Philomela), vergl. Preller,
Griech. Mythologie', II, 142. Mein Freund und College Thraemer
macht mich auch auf Tzetzes, Chil. YII, 479 aufmerksam: uov noZ ds
2) FR hat folgenden Vers Mölevi M a* n e v I ' s (Metr. Remelj :
röl pinhän mehimed z'esän heröz
tä siiyi bäyes ne bu(ßäyend^ pöz
vergl. deutsch *seine Nase in etwas hineinstecken'. F J citirt noch Verse
aus Sa' dl und Gsedl.skr. (Sütr.) püjäyati 'Ehrfurcht bezeigen'; phlv.
=== leaf/page ===
HRN leaf 95 printed 74
BRT leaf 222
DKS leaf 247
```


## [2026-09-07T20:23:24.959Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==223' BRT.txt | head -6; echo \"...\"; awk 'BEGIN{RS=\"\\f\"} NR==223' BRT.txt | grep -n \"razay\\|Hodensack\" ; echo \"== HUB 333 ==\"; grep -n \"^ *333\\.\\|333\\. p\" HUB.txt | head",
 "description": "Bartholomae leaf 223 column, HUB 333"
}
```


### [2026-09-07T20:23:26.325Z] TOOL RESULT

```
anam  .  .
dby  Google
351
*ar»dvaya
■»«zav-
35«
...
33:•  j.  «razay-  m.  'Hodensack':  'zöiS  xa "die  Quellen  des  Hodensacks"  Yt.  i4~ 39.         a)  Du.  'Hoden':  'zi  (ND.)  F.jg.
== HUB 333 ==
```


## [2026-09-07T20:23:38.523Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://www.ahdictionary.com/word/search.html?q=hoopoe",
 "prompt": "Give the American Heritage Dictionary entry for hoopoe: definition and the full etymology line (Middle English, French huppe, Latin upupa, imitative)."
}
```


## [2026-09-07T20:23:39.595Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://www.ahdictionary.com/word/search.html?q=orchid",
 "prompt": "Give the American Heritage Dictionary entry for orchid: definition and the full etymology line (New Latin Orchideae, Latin orchis, Greek orkhis, and the IE root cross-reference)."
}
```


### [2026-09-07T20:23:43.606Z] TOOL RESULT

```
# Hoopoe Entry from American Heritage Dictionary

**Definition:**
"Any of several birds of the family Upupidae found in Eurasia and Africa, especially _Upupa epops,_ having distinctively patterned plumage, a fanlike crest, and a slender, downward-curving bill."

**Etymology:**
The word traces back through an "Alteration (influenced by Latin _ūpupa_) of obsolete _hoop_, from French _huppe_, from Old French, from Vulgar Latin _\*ūppa_, alteration of Latin _upupa, ūpupa_, of imitative origin."

In essence, the term evolved from imitative Latin origins, passing through Vulgar Latin and Old French before entering English, with influence from the Latin form _ūpupa_.
```


### [2026-09-07T20:23:44.392Z] TOOL RESULT

```
# American Heritage Dictionary Entry: Orchid

**Definition:**
The dictionary provides two main definitions: "(a) A member of the orchid family. (b) A flower of one of these plants, especially a cultivated species." Additionally, orchid refers to "A pale to light purple, from grayish to purplish pink to strong reddish purple."

**Etymology:**
The entry traces the word's origin as follows: "From New Latin *Orchideae*, family name, from New Latin *orchis, orchid-*, orchid, from Latin *orchis*, a kind of orchid, from Greek *orkhis*, testicle, orchid (from the shape of its tubers)."

The dictionary notes that this entry is part of the Indo-European & Semitic Roots appendices system, though the specific IE root cross-reference is not explicitly stated in the visible entry content provided.
```


## [2026-09-07T20:23:57.858Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ntxt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\n')\nfor t in [26487,18050]:\n    leaf='\\n'.join(txt[:t]).count('\\f'); print(t,'leaf',leaf,'printed ~',(leaf-12)*2)\nEOF\nfor u in \"https://www.ahdictionary.com/word/search.html?q=hoopoe\" \"https://www.ahdictionary.com/word/search.html?q=orchid\"; do python3 tools/fetch_source.py \"$u\" --note \"page 375: AHD entries for hoopoe (AHD:633) and orchid (AHD:924)\" 2>&1 | tail -1; done",
 "description": "Klein leaf calc; archive AHD pages"
}
```


### [2026-09-07T20:23:59.373Z] TOOL RESULT

```
26487 leaf 584 printed ~ 1144
18050 leaf 399 printed ~ 774
python3: can't open file '/home/sfmqrb/git/rishe/data/verification/sources/refs/tools/fetch_source.py': [Errno 2] No such file or directory
python3: can't open file '/home/sfmqrb/git/rishe/data/verification/sources/refs/tools/fetch_source.py': [Errno 2] No such file or directory
```


## [2026-09-07T20:24:07.333Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==585' KLN_1966.txt | head -5; echo \"-----\"; awk 'BEGIN{RS=\"\\f\"} NR==585' KLN_1966.txt | tail -3; echo \"=== leaf 400 (hoopoe) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==400' KLN_1966.txt | head -4",
 "description": "Check Klein printed page markers"
}
```


### [2026-09-07T20:24:08.717Z] TOOL RESULT

```
ng  to  an  orator’,  fr.  orator.  See  orator, oratory,  n.,  a  small  chapcf —  ME.  oratorie,  fr. Eccl.  L.  oratorium,  ‘place  of  prayer’  (whence also  F.  oratoire),  fr.  L.  oratorius,  ‘pertaining  to prayer;  pertaining  to  an  orator’.  See  prec.  word, orb,  n.,  a  sphere,  globe;  the  emblem  of  sover¬ eignty.  —  MF.  (=  F.)  orbe,  fr.  OF.,  fr.  L.  orbem, acc.  of  orbis,  ‘circle,  ring,  round  surface,  disk’, whence  orbita,  ‘rut  or  track  made  in  the  ground by  awheel’;  of  uncertain  etymology.  Cp.  orbic¬ ular,  orbit.
Derivatives:  orb,  tr.  v.,  to  form  into  a  circle;  to encircle,  orb-y,  adj.
orbicular,  adj.,  having  the  shape  of  an  orb;  spher¬ ical.  —  ME.  orbiculer,  fr.  Late  L.  orbicularis, ‘circular,  orbicular’,  fr.  L.  orbiculus ,  dimin.  of orbis.  See  orb  and  the  suffixes  -cule  and  -ar. orbiculate,  orbiculated,  adj.,  orbicular.  —  See prec.  word  and  adj.  suff.  -ate,  resp.  also  -ed. orbit,  n.,  the  eye  socket  ( anat .)  —  L.  orbita,  ‘a track  or  rut  made  in  the  ground  by  a  wheel’,  fr. orbis',  see  orb.  In  its  anatomical  sense  the  word orbita  was  first  used  by  Gerard  of  Cremona,  the translator  of  Avicenna’s  Canon.  Cp.  periorbita. Derivatives:  orbit-al,  orbit-ary,  adjs. orbito-,  combining  form  denoting  the  orbit  (anat.) —  See  prec.  word.
ore,  n.,  the  grampus.  —  L.  orca,  ‘a  kind  of  w  hale’, fr.  Gk.  opuya,  acc.  of  opui;,  ‘a  kind  of  whale’;  c for  g  in  L.  orca  is  due  either  to  contamination with  L.  orca  in  the  sense  of  ‘butt,  tun’  (see  ur- ceolate),  or  to  Etruscan  influence.  For  the  deri¬ vation  of  the  Latin  word  from  a  Greek  accusa¬ tive  cp.  Numidia  and  words  there  referred  to. Cp.  next  word  and  Orcinus. orca,  n.,  1)  a  killer  whale;  2)  (cap.)  the  genus consisting  of  the  killer  whale  (zool.)  —  L.,  *a kind  of  whale’.  See  prec.  word.
Orcadian,  adj.,  1)  pertaining  to  the  Orkney  Is¬ lands;  2)  a  native  of  the  Orkney  Islands.  —
-----
aeris,  ‘brass’,  fr.  I.-E.  *uyos-,  which  is  perh.  a derivative  of  Ayashya,  later  form  of  Alashya, ancient  name  of  Cyprus,  hence  I.-E.  *ayos would  have  meant  orig.  ‘the  Cyprian  metal’. Cp.  aeneous,  aes,  aerarian,  aerugineous,  era,  es¬ teem;  see  Walde-Hofmann,  LEW.,  1, 19  s.v.  aes. For  sense  development  cp.  L.  cuprum,  ‘copper’, fr.  Kiitrpo;,  ancient  name  of  Cyprus  (see  cop¬ per).
ore,  n.,  a  Dan.  and  Norw.,  resp.  Swed.  coin, equal  in  value  to  1/100  of  a  krone,  resp.  krona.
—  Dan.  and  Norw.  ere  or  Swed.  ore,  fr.  L. aureus,  a  gold 
=== leaf 400 (hoopoe) ===
ed  from  it). See  honey  and  suck.
hong,  n.,  warehouse,  factory.  —  Chin,  hang, ‘warehouse,  factory’,  lit.  ‘a  row  (of  houses)’, honk,  n.,  the  cry  of  a  wild  goose;  any  sound  re¬ sembling  the  cry  of  the  wild  goose.  —  Imi¬ tative.
Derivatives:  honk,  intr.  and  tr.  v.,  honk-er,  n. honor,  honour,  n.  —  ME.  honor,  honour,  fr.  OF. honor,  honur  (F.  honneur),  fr.  L.  honorem,  acc. of  honos,  honor,  ‘honor,  dignity,  office;  repu¬ tation’,  which  is  of  uncertain  origin.  Cp. honesty.  Honors .
honor,  honour,  tr.  v.  —  ME.  honouren,  fr.  OF. honourer  (F.  honorer),  fr.  L.  honorare,  ‘to  ho¬ nor’,  fr.  honos,  honor.  See  honor,  n.
```


## [2026-09-07T20:25:24.886Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nfor f,ts in [('SKT.txt',[8824]),('LAT.txt',[70390,66121]),('IEC.txt',[12300]),('incoming/WLD/WLD_Bd1_pages.txt',[11145,16755])]:\n    txt=open(f,encoding='utf-8',errors='replace').read().split('\\n')\n    for t in ts:\n        leaf='\\n'.join(txt[:t]).count('\\f'); print(f,t,'leaf',leaf)\nEOF\necho \"== SKT orchid ==\"; grep -n -i \"Orchis\\|Orchid\" SKT.txt | head -3",
 "description": "Compute leaves for Skeat/Ernout/Mann/WLD"
}
```


## [2026-09-07T20:25:26.017Z] TOOL CALL #57: Bash

```json
{
 "command": "for u in \"https://www.ahdictionary.com/word/search.html?q=hoopoe\" \"https://www.ahdictionary.com/word/search.html?q=orchid\"; do python3 tools/fetch_source.py \"$u\" --note \"page 375: AHD entries for hoopoe (AHD:633) and orchid (AHD:924)\" 2>&1 | tail -1; done",
 "description": "Archive AHD pages from repo root"
}
```


### [2026-09-07T20:25:26.330Z] TOOL RESULT

```
SKT.txt 8824 leaf 231
LAT.txt 70390 leaf 1351
LAT.txt 66121 leaf 1271
IEC.txt 12300 leaf 494
incoming/WLD/WLD_Bd1_pages.txt 11145 leaf 131
incoming/WLD/WLD_Bd1_pages.txt 16755 leaf 190
== SKT orchid ==
12841:Gk.  A/>xi^crpa,  an  orchestra;  which,  in  the Attic  tbcfllrCf  was  a  space  on  which  the chorus  danced.  — Uk.  6pxioftai,  I  tlaucc. Orchis,  a  plant.  (L.  — Gk.)  L.  anhis.^ Gk.  opx^f,  a  testicle,  a  plant  with  roots  of testicular  shape.  Dor.  orchid,  a  false form,    since    tne    gen.    caM    of   ^x"  ^
```


### [2026-09-07T20:25:28.278Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/9875b4e4807a389d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5f027d2a571fbc25.txt
```


## [2026-09-07T20:25:38.550Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\ntxt=open('SKT.txt',encoding='utf-8',errors='replace').read().split('\\n')\nfor t in [12841]:\n    leaf='\\n'.join(txt[:t]).count('\\f'); print(t,'leaf',leaf,'printed',leaf-20)\nprint('hoopoe printed', 231-20)\"",
 "description": "Skeat orchis page"
}
```


### [2026-09-07T20:25:39.967Z] TOOL RESULT

```
12841 leaf 341 printed 321
hoopoe printed 211
```


## [2026-09-07T20:26:14.635Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"testicle\" PHD.txt PHD_mackenzie.txt NYB_vol2_glossary.txt | head; echo \"== gund/xayag ==\"; grep -n \"^gund\\|xāyag\\|xayag\" PHD.txt PHD_mackenzie.txt | head",
 "description": "Grep MacKenzie for testicle"
}
```


### [2026-09-07T20:26:14.697Z] TOOL RESULT

```
PHD.txt:384:ёгбһ [glwh | N guroh] group, crowd. gubrág [gwpl’k'] awake, alert, vigilant. ģubrās- [gwp/”s-] = wigras-, v. wigrádan. ģuftan, $0(w)- [YMRRWN-, YMLLWN-tn! < A ymlwn, V тЇ; gwptn', gwb- | M gwptn, gw-, N ~, gā(y)-] say, speak. ~išn: speech. ģuftār [gwpt?] | N ~] speaker. ~ih: (power of) speech. gugiin- [gwk’n- | M gwg^n-] destroy. gugar(i)dan, gugar- [gwk”/-(y)tn! | N guwár-idan] digest. tuģāy [gwk*dy | M gwg'y, N guwah] witness. ~ih: testimony. ģūh [gwh | N —] dung, excrement. guhrayénidan, guhrayén- [gw AP yn-ytn!] waken, arouse. gul [gwl | N ~] flower, rose. ботап [gwnmn! | = M, N ~] doubt. ~par [-A/] casting doubt. ~ig [-yk'] doubtful. ~ih, ~igih: doubt. gumardag [gwmltk'] appointee, deputy. ģumārdan, gumār- [gwm’l-tn' | М gwm'r-dn, N gumāštan, gumar-] appoint, commission, entrust. gumbad [gwmbt' | N ~] dome, fire-temple. £umég [gwmyk! | M gwmyg] mixture. guméxtan, gumēz- [gx”myhtn!, gwmyc- | M gwmyxtn, gwmyz-] mix. ~išn: mixing, mixture; = gumézagih. gumëzag [gwmyck'] mixture. ~th: the Mixture, (the duration of) this material world. Jgund [gwnd | = P] army, troop; group, gathering. *gund [gwnd | N ~] testicle. gung [g(w)ng | N ~] dumb. ģurbaģ [gwibk! | N ~a] cat. Бита [gwlt! | P gwrd, N ~] hero. lih: heroism, bravery. gurdag [gwltk! | N ~a] kidney. *gurdih [ewityh] (some piece of) armour. gurdwār [gwltw’!] befitting a hero. ёпгр [gwlg | N ~] wolf. gurganig [gw/g”nyk! | N ~i] of (the province) Gurgan. gursag [ewlsk] | N gurusna !] hungry. «ЛЬ: hunger. Suën [gvfn! | N ~] male. gusnag [gwšnk! | J gušna] hungry. Gušnasp [gwšn(*)sf] the second major Fire of Sasanian Eran, that of warriors. £yà$ [gyw'k! | M gy'g, N jay] place.
PHD.txt:3960:testicle gund.
NYB_vol2_glossary.txt:4275:xüyak [h'dk'] egg 863-7. 922, — Av. aya- < *dya- Yt. 13?, v. Henning, Weller Vol. 1954, 291; NP zäyah (now ‘testicle’).
PHD_mackenzie.txt:2618:llgund [gwnd IN......,] testicle.
PHD_mackenzie.txt:7780:testicle gund.                            thunder (n.) yarranag.
== gund/xayag ==
PHD.txt:1741:egg-shaped xayagdes.
PHD.txt:3013:oval xāyagdēs.
PHD_mackenzie.txt:5549:xayag [h)d(y)k I N xaya] egg.
PHD_mackenzie.txt:6485:egg xayag.                                   envoy bayaspan.
PHD_mackenzie.txt:6486:egg-shaped xayagdes.                         envy aresk, casmareSkih, duscasmih.
PHD_mackenzie.txt:7213:oval xayagdes.                         pavilion kosk, mask; ro:)'ol ...., mask-
PHD_mackenzie.txt:12371:                                              xayag                         \~
PHD_mackenzie.txt:12378:                                   "rut       xayagdts                  -:t>O ~
PHD_mackenzie.txt:12380:                                              xayag
```


## [2026-09-07T20:38:45.309Z] TOOL CALL #60: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-375.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW_PUPAK = \"https://en.wiktionary.org/wiki/%D9%BE%D9%88%D9%BE%DA%A9\"\nW_PUPU  = \"https://en.wiktionary.org/wiki/%D9%BE%D9%88%D9%BE%D9%88\"\nW_UPUPA = \"https://en.wiktionary.org/wiki/upupa\"\nE_HOOP  = \"https://www.etymonline.com/word/hoopoe\"\nW_ORCHID= \"https://en.wiktionary.org/wiki/orchid\"\nW_ORKHIS= \"https://en.wiktionary.org/wiki/%E1%BD%84%CF%81%CF%87%CE%B9%CF%82\"\nW_REC   = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81%C3%B3r%C7%B5%CA%B0is\"\nW_FR    = \"https://en.wiktionary.org/wiki/orchid%C3%A9e\"\nE_ORCHID= \"https://www.etymonline.com/word/orchid\"\nAB_ORK  = \"https://abadis.ir/fatofa/%D8%A7%D8%B1%DA%A9%DB%8C%D8%AF%D9%87/\"\nAHD_HOOP= \"https://www.ahdictionary.com/word/search.html?q=hoopoe\"\nAHD_ORCH= \"https://www.ahdictionary.com/word/search.html?q=orchid\"\n\ndata = {\n \"pdf_page\": 375,\n \"book_page\": 345,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-07\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Opop\",\n   \"verdict\": \"plausible\",\n   \"modern_form\": \"onomatopoeic bird-call base *(e)pop-/*(o)pop- 'the hoopoe's cry' (Pokorny 325 epop-, opop-; not a reconstructible inherited PIE root)\",\n   \"note\": \"Pokorny p. 325 does carry the lemma 'epop-, opop-', Meaning: 'a kind of exclamation' (in the German original the cry of the hoopoe), based on Walde-Pokorny I 123 f., so the root name, the citation and the gloss 'a bird sound' are all accurate. What stands there, however, is not an inherited PIE word but a set of parallel reduplicated onomatopoeias — Gk. epopoi popopo (the cry), epops 'hoopoe', Lat. upupa, Arm. popop, NPers. pupu, Latv. puppukis, Upper Sorbian hupak — and every modern treatment (Wiktionary s.v. upupa 'Onomatopoeic. Compare Ancient Greek epops, Persian pupo'; Etymonline 'imitative of its cry'; Horn no. 333 'Der Name ist onomatopoetisch gebildet') regards each language's form as an independent creation from the bird's call. The root box is therefore a fair label for the word-family, but the arrows leaving it mean 'same imitative type', not descent from one ancestor; hence 'plausible'. Nourai's own gloss and the language label 'Indo-European' are as in his source.\",\n   \"note_fa\": \"پوکورنی در صفحهٔ ۳۲۵ سرمدخل «epop-, opop-» را با معنای «آواز/بانگ (هوپوپ)» آورده است، بر پایهٔ والده‌ـپوکورنی جلد ۱ ص ۱۲۳؛ پس نام ریشه، شمارهٔ صفحه و معنای «آوای پرنده» در کتاب نورایی درست است. اما آنچه پوکورنی گرد آورده ریشهٔ موروثی هندواروپایی آغازین نیست، بلکه مجموعه‌ای از نام‌آواهای همسان و مستقل است: یونانی epops، لاتین upupa، ارمنی popop، فارسی «پوپو»، لتونی puppukis. هرن (شمارهٔ ۳۳۳) صریحاً می‌گوید این نام «نام‌آوا» است و ویکی‌واژه و اتیمانلاین نیز همین را می‌گویند. بنابراین جعبهٔ ریشه برچسبِ درستی برای این خانوادهٔ واژگانی است، ولی پیکان‌های زیر آن به معنای «هم‌گونیِ نام‌آوایی» است نه «فرزندی از یک نیای مشترک»؛ ادعای نورایی با احتیاط پذیرفتنی است.\",\n   \"sources\": [W_UPUPA, E_HOOP, W_PUPU],\n   \"ref_check\": [\n    {\"ref\": \"POK:325\", \"status\": \"supports\",\n     \"note\": \"POK_full.txt lines 27314-27330: 'Root / lemma: epop, opop | Meaning: a kind of exclamation | Material: Armenian popop, npers. pupu \\\"hoopoe\\\"; gr. epopoi popopo \\\"shout, Call of hoopoe\\\", epops, -opos \\\"hoopoe\\\" ... Latin upupa \\\"hoopoe\\\" ... Latvian puppukis \\\"hoopoe\\\". References: WP. I 123 f., Kluge S. 689. Page(s): 325' - exactly Nourai's root box and its two named children.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. I p. 123 (WLD_Bd1_pages.txt leaf 131)\", \"stance\": \"supports\",\n     \"note\": \"'epop. opop Ruf des Wiedehopfs. Gr. epopoi popopo Ruf des Wiedehopfs, epops, -opos \\\"Wiedehopf\\\" ... lat. upupa \\\"Wiedehopf\\\", ndd. Hupphupp u. dgl., arm. popop, npers. pupu, lett. puppukis \\\"Wiedehopf\\\" (s. Suolahti Vogeln. 12). Aehnlich, aber unredupliziert, osorb. hupak ...' - the entry Pokorny 325 abbreviates; it presents the forms as similar reduplications, not as one inherited word.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 appendix (AHD_watkins1985.txt; grep 'upupa|hoopoe|epop')\", \"stance\": \"silent\",\n     \"note\": \"the Indo-European roots appendix has no epop-/opop- root and no HOOPOE headword in its English index - Watkins does not admit this onomatopoeia as a PIE root.\"},\n    {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. upupa (LAT.txt leaf 1351) and s.v. tutubo (leaf 1271)\", \"stance\": \"supports\",\n     \"note\": \"'upupa, -ae f.: 1o huppe, oiseau; 2o pioche ou pic. - Ancien. M.L.'; under the related bird-name: 'Terme expressif, imitatif. Pour le redoublement, cf. tutubo, upupa' - imitative reduplication, matching Pokorny's lemma.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Persian\",\n     \"words\": \"pupu\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"NP pupu (پوپو), with its diminutive pupak (پوپک, NP -ak) and pupe (پوپه), is a real name of the hoopoe (Upupa epops) - Borhan-e Qate' p. 424 s.v. پوپو 'شانه‌سر و هدهد را گویند که مرغ سلیمان است' and Mo'in's Farhang list پوپه/پوپک/پوپو/بوبو together as هدهد، شانه‌سر; Manuchehri's 11th-c. verse quoted in the chart (پوپک پیکی نامه زده اندر سر خویش) attests پوپک in early NP. The Iranian side is a reduplication of the call *pup-/*pupu-, continued in Khotanese papuskya, Buddhist Sogdian pwp'pyh, Chorasmian wpwpyk, Shughni bububak beside NP pupak, pupu (Bailey, Dict. of Khotan Saka s.v. papuskya). Pokorny p. 325 does list 'npers. pupu' under his epop-/opop- lemma, so Nourai's arrow reproduces his cited source faithfully; but Horn (no. 333, p. 74: 'Der Name ist onomatopoetisch gebildet', citing Brehm's observation that quarrelling hoopoes call hup, hup-pup) and Wiktionary ('Onomatopoeic') take the Persian word to be an independent imitation of the bird's cry rather than a descendant of a PIE word - a compatible but not identical picture, hence 'plausible'. The b-forms (بوبو، بوبک) are secondary; Horn notes the p-forms are to be preferred.\",\n     \"derivation_fa\": \"«پوپو» و گونهٔ کوچک‌شدهٔ آن «پوپک» (با پسوند تصغیر ـک) و «پوپه» نام‌های فارسی هوپوپ (شانه‌به‌سر، هدهد) اند؛ برهان قاطع در ص ۴۲۴ ذیل «پوپو» می‌نویسد «شانه‌سر و هدهد را گویند که مرغ سلیمان است» و معین نیز پوپه/پوپک/پوپو را یک مدخل و برابر هدهد و شانه‌سر آورده است. در سوی ایرانی، این واژه دوگان‌سازی (تکرار) آواز پرنده است: ختنی papuskya، سغدی بودایی pwp'pyh، خوارزمی wpwpyk، شغنی bububak در برابر فارسی pupak/pupu (بیلی، فرهنگ ختنی سکایی). پوکورنی در ص ۳۲۵ خودِ «npers. pupu» را ذیل epop-/opop- آورده، پس ارجاع نورایی به منبعش وفادار است؛ ولی هرن (شمارهٔ ۳۳۳، ص ۷۴) و ویکی‌واژه این واژه را نام‌آوای مستقل فارسی می‌دانند نه بازماندهٔ یک واژهٔ هندواروپایی. پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n     \"sources\": [W_PUPU, W_PUPAK],\n     \"ref_check\": [\n      {\"ref\": \"POK:325\", \"status\": \"supports\",\n       \"note\": \"POK_full.txt line 27319: 'Material: Armenian popop, npers. pupu \\\"hoopoe\\\"' - the Persian word is named on the cited page.\"},\n      {\"ref\": \"BQT:424\", \"status\": \"partial\",\n       \"note\": \"Borhan-e Qate' vol. 1 (BQT_v1_pages.txt leaf 651 = printed p. 424, offset leaf-227) s.v. پوپو: 'با بای فارسی بر وزن کوکو، شانه سر و هدهد را گویند که مرغ سلیمان است ... کوکو خوانند', with Mo'in's footnote '۱ - رک: پوپک'. The page confirms the word, the script and the gloss, but Mo'in adds no etymology there, so it does not support the IE arrow itself.\"},\n      {\"ref\": \"IRT:46\", \"status\": \"not_checked\",\n       \"note\": \"IRT = Sajjadiyyeh, Tabar-e Moshtarek-e Iranian va Turanian; refs_online.json marks it 'purchase only / Not found', no copy on disk or online.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"HRN\", \"where\": \"no. 333, p. 74 (HRN.txt line 3158, leaf 95)\", \"stance\": \"supports\",\n       \"note\": \"'333. pupu, pupe, pupek \\\"Wiedehopf\\\"; auch huhu etc. Lat. upupa \\\"Wiedehopf\\\"; gr. epops. kurd. papu (H.-Sch.), papu (JJ.). Der Name ist onomatopoetisch gebildet (vergl. Brehm, Voegel II: \\\"Wenn zwei Wiedehopfe streiten, rufen sie unablaessig hup, auch wohl hup-pup\\\"). Die neupersischen Formen mit p sind denen mit b vorzuziehen.' - same comparison as Nourai, but explicitly as onomatopoeia.\"},\n      {\"src\": \"ISS_alt_DKS\", \"where\": \"Bailey, Dict. of Khotan Saka s.v. papuskya (ISS_alt_DKS.txt line 4082, leaf 247)\", \"stance\": \"supports\",\n       \"note\": \"'papuskya \\\"hoopoe\\\", in list of bird names, III 35:31 papuskya ... Sogd. Bud. pwp'pyh, Chorasm. wpwpyk, N.Pers. pupak, pupu, Shughni bububak, abubauk; outside Iranian, Greek epops, epopos, Lat. upupa, Armen. popop, Lit. pupitis, Let. pupukis, bupucis.' - gives the whole Iranian family plus the same external comparanda.\"},\n      {\"src\": \"MON\", \"where\": \"Farhang-e Farsi, s.v. پوپش (MON_part1.txt line 32979, running head p. 371 of the 2-vol. Adena reprint)\", \"stance\": \"supports\",\n       \"note\": \"'پوپش [= پوپه - پوپک - پوپو - بوبو، کر.] (اصت.) (جان.) هدهد، شانه‌سر' - Mo'in treats پوپو/پوپک/پوپه as one word meaning 'hoopoe'; s.v. شانه‌بسر (MON_part2.txt line 89304) he glosses 'شانه‌بس، پوپک، بوبک، مرغ سلیمان'.\"},\n      {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e Rishe-ha, printed p. 178 (ARY_pages.txt [pdf page 177], line 5226)\", \"stance\": \"supports\",\n       \"note\": \"an independent modern Persian IE-roots dictionary gives the same family: 'فارسی: پوپو، پوپک (به چم ... شانه سر)' with هند و اروپایی *OPOP-, ارمنی POPOP, یونانی EPOPS, لاتین UPUPA, فرانسه HUPPE, انگلیسی HOOPOE, and it cites برهان قاطع - i.e. Nourai's chart in another author's words, with French huppe inserted before English.\"},\n      {\"src\": \"HUB\", \"where\": \"Persische Studien (HUB.txt; grep 'pupu', 'Wiedehopf')\", \"stance\": \"silent\",\n       \"note\": \"Huebschmann has no note on Horn's no. 333; the word is not discussed.\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Latin\",\n     \"words\": \"upŭpa\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"Latin upupa (also ūpupa) 'hoopoe' is attested from Varro on (Varro, LL 5.75 lists it among birds named 'ad suis vocibus', from their own cries) and is universally taken as an imitative reduplication of the bird's call, the exact Italic counterpart of Gk. epops and NP pupu; it survives as It. upupa, Cat. puput, Sp. abubilla and, through Vulgar Latin *uppa, as OF/F huppe. So the word and its position in the family are right, but again the relation to the 'root' is parallel onomatopoeia rather than descent (Ernout-Meillet: 'terme expressif, imitatif'; Wiktionary s.v. upupa: 'Onomatopoeic'), hence 'plausible'. Nourai's citation POK:424 is a slip: Pokorny p. 424 has ghegh- 'to curve, bend' and g(h)egh- 'ferret'; Latin upupa stands on p. 325, the page cited in the box above it.\",\n     \"derivation_fa\": \"لاتین upupa «هوپوپ» از وارّو به‌بعد گواهی شده است (وارّو در «زبان لاتینی» ۵٫۷۵ آن را در شمار پرندگانی می‌آورد که از آوای خود نام گرفته‌اند) و همه آن را دوگان‌سازیِ نام‌آواییِ بانگ پرنده می‌دانند، درست همتای یونانی epops و فارسی «پوپو»؛ بازماندگان آن ایتالیایی upupa، کاتالانی puput و — از لاتین عامیانهٔ *uppa — فرانسویِ کهن و نو huppe است. پس واژه و جایگاهش در این خانواده درست است، ولی پیوندش با «ریشه» هم‌گونیِ نام‌آوایی است نه فرزندی (ارنو-مییه: «اصطلاحی بیانی و نام‌آوایی»). نکتهٔ مهم: ارجاع نورایی POK:424 نادرست است؛ صفحهٔ ۴۲۴ پوکورنی به ghegh- «خمیدن» و g(h)egh- «راسو» اختصاص دارد و upupa در همان ص ۳۲۵ آمده — خطای چاپی/ارجاعیِ خودِ کتاب است (تصویر صفحه نشان می‌دهد کتاب هم POK:424 چاپ کرده).\",\n     \"sources\": [W_UPUPA, AHD_HOOP],\n     \"ref_check\": [\n      {\"ref\": \"POK:424\", \"status\": \"not_found\",\n       \"note\": \"checked POK_full.txt: the two lemmas printed on p. 424 are 'ghegh- | Meaning: to curve, bend' (lines 32519-32524) and 'g(h)egh- | Meaning: ferret' (lines 36101-36112); neither mentions upupa. The correct page is 325 ('Latin upupa \\\"hoopoe\\\"', line 27326) - a citation misprint in the book (the page image of p. 345 shows 'POK:424' printed in the Latin box, so the extraction is faithful).\"},\n      {\"ref\": \"AHD:633\", \"status\": \"not_checked\",\n       \"note\": \"AHD:633 is a page of the main body of the American Heritage Dictionary (New College Edition, 1610 pp.), where 'hoopoe/Upupa' belongs alphabetically; only Watkins' IE-roots appendix is available locally, so the page cannot be verified. The AHD entry itself (ahdictionary.com s.v. hoopoe) does give 'Latin upupa, ūpupa, of imitative origin', which is what the citation is used for.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"LAT\", \"where\": \"Ernout-Meillet, Dict. etym. de la langue latine, s.v. upupa (LAT.txt leaf 1351)\", \"stance\": \"supports\",\n       \"note\": \"'upupa, -ae f.: 1o huppe, oiseau; 2o pioche ou pic. - Ancien. M.L.' and the citation of Varro at LAT.txt line 7837: 'L.L. 5,75, pleraeque [aues]... ad suis uocibus... upupa... bubo.'\"},\n      {\"src\": \"LEW\", \"where\": \"Walde 1910, Lat. etym. Woerterbuch (LEW_1910.txt; grep 'upupa')\", \"stance\": \"silent\",\n       \"note\": \"no hit for upupa in the OCR of the 1910 edition (the letter U section is thin in this scan); nothing found either way.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. I p. 123 (WLD_Bd1_pages.txt line 11152)\", \"stance\": \"supports\",\n       \"note\": \"'lat. upupa \\\"Wiedehopf\\\", ndd. Hupphupp u. dgl., arm. popop, npers. pupu, lett. puppukis \\\"Wiedehopf\\\"' - Latin and Persian side by side under epop/opop, as in the chart.\"},\n      {\"src\": \"AHD\", \"where\": \"ahdictionary.com s.v. hoopoe (archived)\", \"stance\": \"supports\",\n       \"note\": \"'... from Vulgar Latin *uppa, alteration of Latin upupa, ūpupa, of imitative origin' - confirms the Latin form, its imitative character and the *uppa > huppe route.\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"English\",\n     \"words\": \"hoopoe\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"English hoopoe (1660s) does go back to Latin upupa, but with a French relay and a Latin re-fitting: Vulgar Latin *uppa gave Old French huppe (mod. F huppe 'hoopoe', then also 'tuft, crest'), borrowed into English as the now obsolete hoop/houpe, which was then altered to hoopoe under the influence of the learned Latin form upupa (AHD: 'Alteration (influenced by Latin ūpupa) of obsolete hoop, from French huppe, from Old French, from Vulgar Latin *uppa, alteration of Latin upupa'; Skeat: 'the initial h is due to the F. huppe'). Klein reaches the same result by way of 'early E. houpe, fr. F. huppe, fr. L. upupa'. Nourai's single arrow Latin > English is therefore correct as to the ultimate source and only omits the Old French intermediary, which is why the node is confirmed rather than flagged.\",\n     \"derivation_fa\": \"انگلیسی hoopoe (از دههٔ ۱۶۶۰) سرانجام از لاتین upupa می‌آید، اما با واسطهٔ فرانسوی و سپس بازسازی بر پایهٔ صورت لاتینی: از لاتین عامیانهٔ *uppa صورت فرانسویِ کهن huppe پدید آمد، که انگلیسی آن را به شکل hoop/houpe (امروز مهجور) وام گرفت و سپس زیر تأثیر صورت کتابیِ لاتینی upupa به hoopoe بدل شد (فرهنگ American Heritage و اسکیت: «هِ آغازین از huppe فرانسوی است»). کلاین همان راه را می‌دهد: «early E. houpe از F. huppe از L. upupa». پس پیکان یگانهٔ نورایی از لاتین به انگلیسی در سرچشمه درست است و تنها حلقهٔ فرانسویِ کهن را نیاورده؛ ادعای نورایی درست است.\",\n     \"sources\": [E_HOOP, AHD_HOOP],\n     \"ref_check\": [\n      {\"ref\": \"(none cited)\", \"status\": \"not_checked\",\n       \"note\": \"the English box on p. 345 carries no refs= of its own; it inherits POK:325/AHD:633 from the Latin box above it.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein s.v. hoopoe (KLN_1966.txt line 18050, leaf 399; = KLN_1971.txt line 115544)\", \"stance\": \"supports\",\n       \"note\": \"'hoopoe, n., an Old World bird with a long curved bill and a large crest. - Fr. early E. houpe, fr. F. huppe, fr. L. upupa, a word of imitative origin; cp. Gk. epops, \\\"hoopoe\\\". Cp. also dupe' (dupe < F de huppe).\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat s.v. Hoopoe, p. 211 (SKT.txt line 8824, leaf 231)\", \"stance\": \"supports\",\n       \"note\": \"'Hoopoe, the name of a bird. (L.) L. upupa, a hoopoe; the initial h is due to the F. huppe, also derived from upupa. - Gk. epops, a hoopoe. Of imitative origin. The F. huppe, a tuft of feathers, is from huppe, a hoopoe (from its tufted head): not vice versa.'\"},\n      {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century Dict., s.v. hoop/hoopoe (WEB_vol1.txt lines 91962, 91981)\", \"stance\": \"supports\",\n       \"note\": \"'hoop, n. same as hoopoe' and, in the etymology, 'upupa, a hoopoe; prob. imitative'.\"},\n      {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls New Standard Dict., vol. I (FSD_vol1.txt lines 42530, 42624)\", \"stance\": \"partial\",\n       \"note\": \"the word is listed and illustrated as '9. Hoopoe (Upupa epops)' in the bird plate, confirming the identification of the bird, but the OCR of the etymology line itself is not legible.\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 2,\n   \"root\": \"Orghi\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *h1orǵʰis / *h3erǵʰi- 'testicle' (Pokorny 782 orghi-, r̥ghi-)\",\n   \"note\": \"Pokorny p. 782 has exactly 'Root / lemma: orghi-, r̥ghi- | Meaning: testicle | Grammatical information: m.', with Av. arəzi-, Arm. orji-k', Gk. orkhis, Alb. herdhe, MIr. uirgge, Lith. eržilas; Walde-Pokorny I 182 is the underlying entry. Watkins/AHD files the same material as an o-grade *orgh-i- of a root ergh- 'to mount' ('[Pok. orghi- 782, ergh- 339]'), a derivation Pokorny himself only floats ('Maybe Root ergh- \\\"to shake, tremble, lustful\\\" derived orghi- \\\"testicle\\\" (hence a taboo word)'). Current reconstructions write the word with an initial laryngeal, *h1orǵʰis or *h3erǵʰi- (Kloekhorst prefers *h3- because of the o-colouring in the daughter languages; Hamp proposed *h4-), and add Hittite arki- 'testicle' to the cognates. Language label 'Indo-European' and gloss 'testicle' are both correct.\",\n   \"note_fa\": \"پوکورنی در ص ۷۸۲ دقیقاً همین سرمدخل را دارد: «orghi-, r̥ghi- (مذکر) «بیضه»» با اوستایی arəzi-، ارمنی orji-k'، یونانی orkhis، آلبانی herdhe، ایرلندی میانه uirgge و لیتوانیایی eržilas؛ اصل مطلب در والده‌ـپوکورنی جلد ۱ ص ۱۸۲ است. واتکینز (پیوست ریشه‌های هندواروپاییِ AHD) همین مواد را صورتِ درجهٔ o از ریشهٔ ergh- «برجستن، جفت‌گیری» می‌داند و به «Pok. orghi- 782, ergh- 339» ارجاع می‌دهد. بازسازی امروزی این واژه را با حنجره‌ای آغازین می‌نویسد: *h₁órǵʰis یا *h₃érǵʰi- (کلوکهورست *h₃- را ترجیح می‌دهد زیرا رنگ‌گرفتن واکه به o در زبان‌های دختر را توضیح می‌دهد) و هیتی arki- «بیضه» را هم به هم‌ریشه‌ها می‌افزاید. برچسب زبان و معنای «بیضه» در کتاب درست است؛ ادعای نورایی درست است.\",\n   \"sources\": [W_REC, W_ORKHIS],\n   \"ref_check\": [\n    {\"ref\": \"POK:782\", \"status\": \"supports\",\n     \"note\": \"POK_full.txt lines 64191-64217: 'Root / lemma: orghi-, r̥ghi- | Meaning: testicle | Grammatical information: m. | Material: Avestan arəzi- m. \\\"to scrotum\\\", Du. arəzi \\\"testicles\\\"; Armenian orji-k' pl. \\\"testicles\\\" ...; gr. orkhis m. \\\"testicle\\\"; ... References: WP. I 182 f., Trautmann 71. Page(s): 782.'\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. I p. 182 (WLD_Bd1_pages.txt lines 16677, 16755-16768, leaf 190)\", \"stance\": \"supports\",\n     \"note\": \"'orghi-, r̥ghi- m. \\\"Hode\\\" (vielleicht auch *erghi-). Av. arəzi- m. \\\"Hodensack\\\", Du. arəzi \\\"Hoden\\\", ai. uśr-r̥jika- \\\"mit sichtbar gewordenen ... Hoden\\\" ... Arm. orji-k' pl. \\\"Hoden\\\", orji \\\"nicht kastriert\\\" (*orghi-ios) ... gr. orkhis m. \\\"Hode\\\"; alb. herdhe f. \\\"Hode\\\"' - the source of Pokorny's page.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. ergh- (AHD_watkins1985.txt line 456)\", \"stance\": \"partial\",\n     \"note\": \"'ergh-. To mount. 1. Suffixed o-grade form *orgh-i- in Greek orkhis, testicle: ORCHID. 2. Suffixed o-grade form *orgh-eyo- in Greek orkheisthai, to dance: ORCHESTRA. [Pok. orghi- 782, ergh- 339.]' - same material and the same Pokorny page, but filed under a verbal root ergh- rather than as an independent noun root, and with no Avestan form.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann, IE Comparative Dictionary s.v. orghis (IEC.txt line 12300, leaf 494)\", \"stance\": \"partial\",\n     \"note\": \"'orghis \\\"testicle\\\". WP I, 182 Arm. ordz, i-st. \\\"male\\\" ...; xol-ordz \\\"orchid\\\"; Gk. orkhis, gs. -eos, m. \\\"testicle\\\"; MIr. uirge, Ir. uirghe ...; Li. cf. eržilas \\\"colt\\\"; Latv. cf. erzelis \\\"stallion\\\"' - same lemma and gloss, but Mann's cognate list omits the Avestan word.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Avestan\",\n     \"words\": \"ěrězi, arazi\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Avestan arəzi- (stem arəzay-) is the regular Iranian reflex of *h3erǵʰi-/*orghi-: PIE *-ǵʰ- gives Iranian -z- (satem palatalisation, as in *deḱm > dasa), the initial *(h3)o-/e- appears as Av. a-, and the word is an i-stem masculine. Bartholomae's Altiranisches Woerterbuch (col. 351) glosses the singular 'Hodensack' (scrotum), attested in Yt. 14.39 arəzoiš xa 'the springs of the scrotum', and the dual arəzi 'Hoden' (testicles) in the Frahang-i oim - which is exactly the dual that Buck and Klein cite and that the chart glosses 'testicles'. The chart's two spellings are one word in two transliteration systems (Nourai's ě = ə, so 'ěrězi' = arəzi/ərəzi, while 'arazi' is Buck's and Pokorny's spelling); no separate form is being claimed. Semantically the singular 'scrotum' vs dual 'testicles' distinction is worth keeping in mind, but the gloss is not wrong.\",\n     \"derivation_fa\": \"اوستایی arəzi- (ستاک arəzay-) بازماندهٔ قاعده‌مندِ ایرانیِ *h₃erǵʰi- / orghi- است: *ǵʰ هندواروپایی در شاخهٔ ساتم به z بدل می‌شود (چنان‌که *deḱm > dasa) و واکهٔ آغازی در اوستایی a- می‌شود؛ واژه ستاکِ i و مذکر است. بارتولومه (فرهنگ ایرانی باستان، ستون ۳۵۱) صورت مفرد را «Hodensack» یعنی «کیسهٔ بیضه» معنی می‌کند با گواه یشت ۱۴٫۳۹ («arəzoiš xa» = چشمه‌های کیسهٔ بیضه) و صورت مثنّای arəzi را «Hoden» (بیضه‌ها) در «فرهنگ اویم». همین مثنّاست که باک و کلاین نقل کرده‌اند و در نمودار «testicles» ترجمه شده است. دو صورت «ěrězi» و «arazi» یک واژه در دو شیوهٔ آوانگاری‌اند (ě نزد نورایی همان ə است)؛ پس ادعای نورایی درست است، تنها با این نکته که مفرد «کیسهٔ بیضه» و مثنّا «بیضه‌ها» است.\",\n     \"sources\": [W_REC, W_ORKHIS],\n     \"ref_check\": [\n      {\"ref\": \"POK:782\", \"status\": \"supports\",\n       \"note\": \"POK_full.txt line 64197: 'Material: Avestan arəzi- m. \\\"to scrotum\\\", Du. arəzi \\\"testicles\\\"' (OCR of 'Av. arəzi- m. \\\"Hodensack\\\", Du. arəzi \\\"Hoden\\\"').\"},\n      {\"ref\": \"KLN:1092\", \"status\": \"supports\",\n       \"note\": \"Klein s.v. orchid (KLN_1966.txt line 26487, leaf 584; vol. II, the volume covering p. 1092): 'fr. Gk. orkhis, \\\"testicle\\\", also \\\"orchis\\\" ... which is cogn. with Avestic ərəzi (dual), \\\"testicles\\\", Arm. orji-k', \\\"testicles\\\", orji, \\\"not castrated\\\", Alb. herde (for *erde), \\\"testicle\\\", Lith. eržilas, \\\"stallion\\\", MIr. uirgge, Ir. uirge, \\\"testicle\\\"' - Klein's spelling 'ərəzi' is Nourai's 'ěrězi'.\"},\n      {\"ref\": \"SYN:257\", \"status\": \"supports\",\n       \"note\": \"Buck 4.49 TESTICLE, printed pp. 256-257 (SYN.txt leaves 295-296; leaf 296 carries the running head '... 257'): the word table lists 'Av. arazi (du.)' and the discussion opens '... *orghi-, etc. Walde-P. 1.182 f. ... Gk. orkhis, late dim. orkhidion ...; Av. arəzi (\\\"scrotum\\\"); Arm. orjik' (pl.); cf. Skt. uśr-r̥jika- ...' - exactly the arrow root > Avestan.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW col. 351 (BRT.txt leaf 223, whose running heads are 351/352)\", \"stance\": \"supports\",\n       \"note\": \"'j. arəzay- m. \\\"Hodensack\\\": arəzoiš xa \\\"die Quellen des Hodensacks\\\" Yt. 14.39. a) Du. \\\"Hoden\\\": arəzi (ND.) F.jg.' - the Avestan word, its attestations and the dual with the meaning 'testicles'.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. I p. 182 (WLD_Bd1_pages.txt line 16756)\", \"stance\": \"supports\",\n       \"note\": \"'Av. arəzi- m. \\\"Hodensack\\\", Du. arəzi \\\"Hoden\\\", ai. uśr-r̥jika- \\\"mit sichtbar gewordenen, d. h. hervortretenden Hoden\\\" (Geldner ZdMG. 52, 746)'.\"},\n      {\"src\": \"KNT\", \"where\": \"Kent, Old Persian lexicon (KNT.txt; grep 'arzi', 'testicle')\", \"stance\": \"silent\",\n       \"note\": \"no Old Persian counterpart is attested in the inscriptions, so Kent has nothing; the Iranian evidence is Avestan only.\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"None\",\n     \"words\": \"\",\n     \"verdict\": \"unverified\",\n     \"derivation\": \"This node is an outlined box printed completely empty on book p. 345 - no language header, no word, no gloss (checked on the rendered page image; the extraction is faithful and its note says the same). There is therefore no claim to verify: it is an unfilled placeholder in Nourai's drawing, drawn as a child of the Avestan box, presumably reserved for a later Iranian or Modern Persian continuation that was never entered. Nothing could in fact have stood there by inheritance: *h3erǵʰi- has no Middle or New Persian reflex - MacKenzie's Pahlavi dictionary gives gund 'testicle' (NP gund) and xayag 'egg' (NP xaya, which only later took over the sense 'testicle'), and Nyberg notes explicitly 'xayak [h'dk'] egg ... NP xayah (now \\\"testicle\\\")', from OIr. *aya-/*avya- 'egg', a different root.\",\n     \"derivation_fa\": \"این گره در صفحهٔ ۳۴۵ چاپیِ کتاب جعبه‌ای است کاملاً خالی: نه نام زبان دارد نه واژه و نه معنی (با نگاه به تصویر صفحه بررسی شد؛ استخراج داده وفادار است). پس ادعایی برای سنجیدن وجود ندارد و این جعبه جای‌نگه‌دارِ پرنشده‌ای در نمودار نورایی است که زیر جعبهٔ اوستایی کشیده شده، گویا برای ادامهٔ ایرانیِ میانه/فارسی نو که هرگز نوشته نشد. در واقع هیچ صورتی هم نمی‌توانست آنجا بنشیند، زیرا *h₃erǵʰi- در فارسی میانه و نو بازمانده ندارد: مکنزی برای پهلوی «gund» (بیضه، فارسی «گند») و «xayag» (تخم‌مرغ، فارسی «خایه») می‌آورد و نیبرگ صریح می‌گوید «xayak = تخم‌مرغ ... در فارسی نو خایه (امروز به معنی بیضه)»، که از ایرانی باستان *āya-/*āvya- «تخم» است، یعنی ریشه‌ای دیگر. حکم: بی‌ارزیابی (جعبهٔ خالیِ خودِ کتاب).\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\"ref\": \"(none cited)\", \"status\": \"not_checked\",\n       \"note\": \"the box carries no refs= because it carries no content at all.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary, s.v. gund and xayag (PHD.txt line 384; PHD_mackenzie.txt lines 2618, 5549; English index 'testicle gund')\", \"stance\": \"silent\",\n       \"note\": \"'*gund [gwnd | N ~] testicle' and 'xayag [h'd(y)k | N xaya] egg' - Middle Persian has no reflex of *orghi-/arəzi-, so no Iranian continuation existed to fill this box.\"},\n      {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, glossary s.v. xuyak/xayak (NYB_vol2_glossary.txt line 4275)\", \"stance\": \"silent\",\n       \"note\": \"'xayak [h'dk'] egg 863-7, 922, - Av. aya- < *aya- Yt. 13, v. Henning ...; NP xayah (now \\\"testicle\\\")' - confirms that the Persian word for 'testicle' comes from the 'egg' word, not from arəzi-.\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Greek\",\n     \"words\": \"orxis\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Ancient Greek orkhis (ὄρχις, gen. orkheos/orkhios, m.) 'testicle' is the direct Greek reflex of *h3erǵʰi- (PIE *ǵʰ > Gk. kh, the i-stem preserved); it is transliterated 'orxis' in the chart because Nourai renders chi with x. From Theophrastus and Dioscorides on, the feminine orkhis is also the name of the orchid (Orchis mascula and kin) and of an olive variety, in both cases from the shape - the plant has a pair of egg-shaped tubers, so it was named 'testicle-plant', exactly the motivation the chart's gloss gives (the same image gave Middle English ballockwort and Arabic khusa'l-tha'lab 'fox's testicles', the source of salep). The double sense 'testicle' / 'orchid' in one Greek word is what makes the rest of the chain possible.\",\n     \"derivation_fa\": \"یونانی باستان ὄرχις = orkhis (مذکر، «بیضه») بازماندهٔ مستقیم *h₃erǵʰi- است: *ǵʰ هندواروپایی در یونانی به kh بدل شده و ستاکِ i باقی مانده است؛ در نمودار «orxis» نوشته شده چون نورایی حرف خی را x می‌نویسد. از تئوفراستوس و دیوسکوریدس به‌بعد همین واژه در صورت مؤنث نام گلِ ثعلب/ارکیده (Orchis mascula) و نیز نوعی زیتون است، در هر دو مورد به سبب شکل: این گیاه دو غدهٔ تخم‌مرغی‌شکل دارد و از این‌رو «گیاهِ بیضه» نامیده شد — همان انگیزه‌ای که در توضیح نمودار آمده (همین تصویر در انگلیسی میانه ballockwort و در عربی «خُصَی الثَّعلَب» را ساخته که «سحلب/salep» از آن است). همین دومعناییِ یونانی است که زنجیرهٔ بعدی را ممکن کرده؛ ادعای نورایی درست است.\",\n     \"sources\": [W_ORKHIS, E_ORCHID],\n     \"ref_check\": [\n      {\"ref\": \"POK:782\", \"status\": \"supports\",\n       \"note\": \"POK_full.txt line 64203: 'gr. (*h3orkhis) orkhis m. \\\"testicle\\\"' under the lemma orghi-, r̥ghi- on p. 782.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"IEC\", \"where\": \"Mann s.v. orghis (IEC.txt line 12300)\", \"stance\": \"supports\",\n       \"note\": \"'Gk. orkhis, gs. -eos, m. \\\"testicle\\\"' listed as the Greek reflex of orghis, with Arm. xol-ordz 'orchid' showing the same plant-naming in Armenian.\"},\n      {\"src\": \"SYN\", \"where\": \"Buck 4.49 TESTICLE, pp. 256-257 (SYN.txt leaves 295-296)\", \"stance\": \"supports\",\n       \"note\": \"'Grk. orkhis ... late dim. orkhidion' heads Buck's list, with the note that the Greek word is the base of the derivational family (whence also en-orkhos 'uncastrated').\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat s.v. Orchis, p. 321 (SKT.txt line 12841, leaf 341)\", \"stance\": \"supports\",\n       \"note\": \"'Orchis, a plant. (L. - Gk.) L. orchis. - Gk. orkhis, a testicle, a plant with roots of testicular shape' - the double sense and its motivation.\"}\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"Latin\",\n     \"words\": \"orchis\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Latin orchis is a straight borrowing of the Greek plant-name (Pliny, NH 26.95 and 27.65 uses orchis of the plant; the anatomical sense stays Greek in Latin, where the native word is testiculus, itself a calque-like use of testis after Gk. parastatai). Latin kept the Greek third-declension nominative, gen. orchis/orchios, which matters for the next step: when Linnaeus and his successors made a family name they wrongly assumed a stem orchid- (as if gen. orchidis), producing Orchideae/Orchidaceae and the modern combining form orchid-. The box has no refs= of its own, but Klein's orchid entry supplies exactly this Latin link.\",\n     \"derivation_fa\": \"لاتین orchis وام‌واژه‌ای مستقیم از نام گیاه در یونانی است (پلینی در «تاریخ طبیعی» ۲۶٫۹۵ و ۲۷٫۶۵ آن را برای همین گیاه به کار می‌برد؛ معنای اندام‌شناختی در لاتین یونانی می‌ماند و واژهٔ بومی testiculus است). لاتین صورت نهادیِ صرفِ سومِ یونانی را نگه داشت با اضافیِ orchis/orchios، و همین نکته برای گام بعدی مهم است: گیاه‌شناسان سدهٔ هژدهم (لینه و پس از او) به خطا ستاک را orchid- پنداشتند (چنان‌که اضافی orchidis باشد) و از آن Orchideae و Orchidaceae و جزءِ ترکیبیِ orchid- را ساختند. این جعبه ارجاعی از خود ندارد، ولی مدخل «orchid» در کلاین همین حلقهٔ لاتینی را می‌دهد؛ ادعای نورایی درست است.\",\n     \"sources\": [E_ORCHID, W_ORCHID],\n     \"ref_check\": [\n      {\"ref\": \"(none cited)\", \"status\": \"not_checked\",\n       \"note\": \"the Latin box carries no refs=; the claim is covered by KLN:1092 and AHD:924 cited in the English box below it.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein s.v. Orchis and Orchidaceae (KLN_1966.txt lines 26489, 26500, leaf 584)\", \"stance\": \"supports\",\n       \"note\": \"'Orchis, n., a genus of plants of the orchid family (bot.) - L. orchis, fr. Gk. orkhis, \\\"testicle; orchid\\\"'; and 'Orchidaceae ... ModL., incorrectly formed fr. L. orchis, whose gen. was supposed to be orchidis (in reality, the gen. is orchis)'.\"},\n      {\"src\": \"LAT\", \"where\": \"Ernout-Meillet (LAT.txt; grep 'orchis' - only line 60599 'stingus, -i m.: orchis, plante (Isid.)')\", \"stance\": \"silent\",\n       \"note\": \"Ernout-Meillet has no headword orchis (it treats only inherited/old Latin vocabulary); the word appears merely as the French gloss of another plant name, so this dictionary says nothing either way.\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat s.v. Orchis, p. 321 (SKT.txt line 12841)\", \"stance\": \"supports\",\n       \"note\": \"'Orchis, a plant. (L. - Gk.) L. orchis. - Gk. orkhis ... Der. orchid, a false form, since the gen. case of orkhis is [orkhios]' - Latin from Greek, and the false stem behind 'orchid'.\"}\n     ]\n    },\n    {\n     \"id\": 5,\n     \"lang\": \"French\",\n     \"words\": \"\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"The French box is a pass-through with no word printed: the form meant is F orchidee, a learned 18th-19th-c. botanical borrowing from New Latin Orchideae/Orchidaceae (the family name built on the false stem orchid- of L orchis), first as the plural name of the family and then as the singular name of the plant. It is French, not Latin, that supplied the modern word to most of Europe and to Persian: German Orchidee, Dutch orchidee, Swedish orkide, Romanian orhidee, Turkish orkide and Persian orkideh all reproduce the French shape with its stressed final -e. The step is therefore real and is the necessary link to the Persian box that hangs from it.\",\n     \"derivation_fa\": \"جعبهٔ فرانسوی گذرگاهی است و واژه‌ای در آن چاپ نشده؛ صورت مقصود «orchidée» فرانسوی است، وام‌واژه‌ای دانشورانه از لاتینِ نو Orchideae/Orchidaceae (نام تیره که بر ستاکِ نادرستِ orchid- ساخته شده)، نخست نام تیره و سپس نام خودِ گیاه. همین فرانسوی است — نه لاتین — که واژهٔ امروزی را به بیشتر زبان‌های اروپایی و به فارسی داده است: آلمانی Orchidee، هلندی orchidee، سوئدی orkidé، رومانیایی orhidee، ترکی orkide و فارسی «ارکیده»، همه صورت فرانسوی را با ـهٔ پایانی بازمی‌تابانند. پس این حلقه واقعی و همان پیوند لازم به جعبهٔ فارسیِ زیر آن است؛ ادعای نورایی درست است.\",\n     \"sources\": [W_FR],\n     \"ref_check\": [\n      {\"ref\": \"(none cited)\", \"status\": \"not_checked\",\n       \"note\": \"the French box is printed with the language header only, no word and no refs=.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein s.v. orchid / Orchidaceae (KLN_1966.txt lines 26487, 26489)\", \"stance\": \"supports\",\n       \"note\": \"'orchid, n. - Fr. ModL. Orchideae, later Orchidaceae ..., fr. L. orchis' - the New Latin family name from which French orchidee (and thence the European words) is formed.\"},\n      {\"src\": \"DEV\", \"where\": \"Devic, Dict. etym. des mots francais d'origine orientale (DEV.txt; grep 'orchid')\", \"stance\": \"silent\",\n       \"note\": \"no entry - as expected, since orchidee is a Graeco-Latin coinage, not an oriental loan in French.\"}\n     ]\n    },\n    {\n     \"id\": 6,\n     \"lang\": \"Persian\",\n     \"words\": \"orkîdeh\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"NP ارکیده orkide 'orchid' is a 20th-c. loan from French orchidee, taken in with the wave of French botanical and technical vocabulary of the late Qajar and Pahlavi periods; French [ɔʁ.ki.de] is rendered with Persian or- for or-, -ki- for -chi- (French ch = [k] here) and final ـه for the French -ée, which is the normal Persian treatment of French words in -é(e) (cf. کمیته komite < comite, پماد, دوسیه). All three Persian dictionaries mark it French: Mo'in and Amid label ارکیده فرانسوی and gloss it as the ornamental plant of the ثعلبیان/orchid family. This is thus a Persian word that returns to the same Greek orkhis by a completely European route - not an inherited Iranian cognate of the Avestan word in the same chart. Note that the JSON's script form uses the Arabic kaf (اركیده) where p. 345 prints Persian kaf (ارکیده); this is only the usual character-form normalisation of the PDF's font, not a misread letter.\",\n     \"derivation_fa\": \"«ارکیده» وام‌واژه‌ای است از فرانسوی orchidée که در سدهٔ چهاردهم خورشیدی همراه موج واژگان گیاه‌شناسی و فنیِ فرانسوی به فارسی آمده است؛ تلفظ فرانسویِ [ɔʁ.ki.de] در فارسی به «ار-» و «-کی-» (ch فرانسوی اینجا k است) و «ـده» بدل شده، و پایانهٔ ـه همان رفتار معمول فارسی با واژه‌های فرانسویِ پایان‌یافته به -é(e) است (مانند «کمیته»، «دوسیه»). هر سه فرهنگ فارسی (معین، عمید، فرهنگ فارسی) آن را «فرانسوی» نشانه‌گذاری کرده و گیاهی زینتی از تیرهٔ ثعلبیان معنی کرده‌اند. پس این واژه از راهی سراسر اروپایی به همان orkhis یونانی بازمی‌گردد و هم‌ریشهٔ موروثیِ واژهٔ اوستاییِ همین نمودار نیست. نکته: در دادهٔ استخراج‌شده «اركیده» با کافِ عربی آمده، در حالی که صفحهٔ ۳۴۵ «ارکیده» با کاف فارسی چاپ کرده است؛ این تنها یکسان‌سازیِ نویسه در قلمِ PDF است نه بدخوانیِ حرف.\",\n     \"sources\": [AB_ORK, W_FR],\n     \"ref_check\": [\n      {\"ref\": \"(none cited)\", \"status\": \"not_checked\",\n       \"note\": \"the Persian box carries no refs=; verified from Persian dictionaries independently.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"Farhang-e Mo'in s.v. ارکیده, via abadis.ir (archived)\", \"stance\": \"supports\",\n       \"note\": \"Mo'in: 'گیاهی از تیرهٔ ثعلبیان که انواع آن گل‌های زیبا دارد و به عنوان گیاه زینتی در باغ یا گلدان کاشته می‌شود', tagged فرانسوی (French), English equivalent 'orchid' - i.e. a French loan, as the chart's French > Persian arrow says. فرهنگ عمید agrees.\"},\n      {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e Rishe-ha (ARY_pages.txt / ARY_latin_index_pages.txt; grep 'ارکیده', 'ORCHID')\", \"stance\": \"silent\",\n       \"note\": \"no entry: Aryanpur only treats words with an inherited Indo-European pedigree in Persian, and a modern French loan is outside his scope.\"}\n     ]\n    },\n    {\n     \"id\": 7,\n     \"lang\": \"English\",\n     \"words\": \"orchid\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"English orchid dates from 1845 (John Lindley, School Botany) and is a back-formation from New Latin Orchideae / Orchidaceae, the family name coined on the mistaken stem orchid- of Latin orchis (as if the genitive were orchidis rather than orchis/orchios); before that English used Latin orchis itself (1560s) and, in Middle English, the native ballockwort 'testicle-plant' (c. 1300), which shows that the naming image was independently transparent in English. So the arrow Latin orchis > English orchid is correct in substance, with the New Latin botanical coinage as the intermediate stage that both of Nourai's own references spell out. The colour sense 'pale purple' is a late-19th-c. extension from the flower.\",\n     \"derivation_fa\": \"انگلیسی orchid از ۱۸۴۵ (جان لیندلی در School Botany) به کار رفته و ساخته‌ای پس‌ساز از لاتینِ نو Orchideae/Orchidaceae است، یعنی نام تیره که بر ستاکِ نادرستِ orchid- از لاتین orchis ساخته شد (چنان‌که اضافی‌اش orchidis باشد، حال آن‌که orchis/orchios است). پیش از آن انگلیسی خودِ صورت لاتینیِ orchis را به کار می‌برد (دههٔ ۱۵۶۰) و در انگلیسی میانه واژهٔ بومیِ ballockwort «گیاهِ بیضه» (حدود ۱۳۰۰) را داشت، که نشان می‌دهد همان انگیزهٔ نام‌گذاری در انگلیسی نیز آشکار بوده است. پس پیکان «لاتین orchis ← انگلیسی orchid» در جوهر درست است، با این توضیح که حلقهٔ میانی همان نام‌گذاری گیاه‌شناختیِ لاتینِ نو است و هر دو منبعِ خودِ نورایی (کلاین و AHD) همین را می‌گویند؛ ادعای نورایی درست است.\",\n     \"sources\": [E_ORCHID, W_ORCHID, AHD_ORCH],\n     \"ref_check\": [\n      {\"ref\": \"AHD:924\", \"status\": \"not_checked\",\n       \"note\": \"AHD:924 is a page of the main body of the American Heritage Dictionary (New College Edition), where 'orchid' belongs alphabetically; only Watkins' IE-roots appendix is on disk, so the page itself cannot be checked. The AHD entry (ahdictionary.com s.v. orchid, archived) reads 'From New Latin Orchideae, family name, from New Latin orchis, orchid-, orchid, from Latin orchis, a kind of orchid, from Greek orkhis, testicle, orchid (from the shape of its tubers)', which is precisely the arrow; the appendix cross-reference is Watkins s.v. ergh- ('Greek orkhis, testicle: ORCHID').\"},\n      {\"ref\": \"KLN:1092\", \"status\": \"supports\",\n       \"note\": \"Klein s.v. orchid (KLN_1966.txt line 26487, leaf 584): 'orchid, n. - Fr. ModL. Orchideae, later Orchidaceae (see Orchidaceae), fr. L. orchis, fr. Gk. orkhis, \\\"testicle\\\", also \\\"orchis\\\" (so called from the resemblance of the roots to testicles), which is cogn. with Avestic ərəzi (dual), \\\"testicles\\\"' - Nourai's Latin > English arrow and his Avestan box in one entry, on the page he cites.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"AHD\", \"where\": \"ahdictionary.com s.v. orchid (archived) + Watkins 1985 s.v. ergh- (AHD_watkins1985.txt lines 456, 1995)\", \"stance\": \"supports\",\n       \"note\": \"the dictionary entry gives ModL Orchideae < ModL orchis, orchid- < L orchis < Gk orkhis; the appendix index line reads 'ORCHID ergh-' and the root entry 'Suffixed o-grade form *orgh-i- in Greek orkhis, testicle: ORCHID'.\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat s.v. Orchis, p. 321 (SKT.txt line 12841)\", \"stance\": \"supports\",\n       \"note\": \"'Der. orchid, a false form, since the gen. case of orkhis is [orkhios]' - Skeat states the false-stem origin of the English form.\"},\n      {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls New Standard Dict., vol. III (FSD_vol3.txt lines 49137, 168821)\", \"stance\": \"partial\",\n       \"note\": \"the dictionary uses 'orchid' and 'Orchidaceae' throughout its botanical definitions, confirming the 19th-20th-c. English usage, but the OCR of the etymology line s.v. orchid is not legible in this scan.\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-375.json','w',encoding='utf-8') as f:\n    json.dump(data,f,ensure_ascii=False,indent=2)\n    f.write('\\n')\nprint('ok')\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-375.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-375.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 375",
 "description": "Write and check page-375.json"
}
```


### [2026-09-07T20:38:46.951Z] TOOL RESULT

```
ok
JSON OK
nodes verified: 10/10
node verdicts: {'plausible': 2, 'confirmed': 7, 'unverified': 1}
root verdicts: {'plausible': 1, 'confirmed': 1}
ref checks: {'supports': 6, 'partial': 1, 'not_checked': 8, 'not_found': 1}
books consulted: {'supports': 21, 'silent': 8, 'partial': 2} | by book: {'SKT': 4, 'KLN': 3, 'MON': 2, 'ARY': 2, 'LAT': 2, 'WLD': 2, 'AHD': 2, 'FSD': 2, 'HRN': 1, 'ISS_alt_DKS': 1, 'HUB': 1, 'LEW': 1, 'WEB': 1, 'BRT': 1, 'KNT': 1, 'PHD': 1, 'NYB': 1, 'IEC': 1, 'SYN': 1, 'DEV': 1}
```


## [2026-09-07T20:38:59.193Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== DEV orchid ==\"; grep -n -i \"orchid\" DEV.txt | head; echo \"== KNT arzi/testicle ==\"; grep -n -i \"arzi\\|testicle\" KNT.txt | head; echo \"== ARY arkideh ==\"; grep -n \"ارکیده\\|اركیده\" incoming/ARY/ARY_pages.txt | head; echo \"(ARY latin index ORCHID)\"; grep -n -i \"ORCHID\" incoming/ARY/ARY_latin_index_pages.txt | head",
 "description": "Verify remaining cited greps"
}
```


### [2026-09-07T20:38:59.317Z] TOOL RESULT

```
== DEV orchid ==
516:Angrec.  Genre  de  plantes  tropicales  de  la  famille  des orchidées.  Lat.  botan.  angrœcum  (ainsi  orthographié  par analogie  avec  fœnugrœcum).  Le  mot  vient  sans  doute  de l'archipel  Indien;  car  il  existe  dans  le  sounda  et  le  javanais [(ùnrj^><vJls  anggréky,  c'est  en  malais  ^Jii  anggreq,  orchis.
== KNT arzi/testicle ==
== ARY arkideh ==
(ARY latin index ORCHID)
```


## [2026-09-07T20:39:11.198Z] TOOL CALL #62: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json,io\np='data/verification/page-375.json'\nd=json.load(open(p,encoding='utf-8'))\ne=d['entries'][1]\nn3=[n for n in e['nodes'] if n['id']==3][0]\nold=n3['derivation_fa']\nn3['derivation_fa']=old.replace('ὄرχις = orkhis','ὄρχις (orkhis)')\nassert 'ὄρχις (orkhis)' in n3['derivation_fa']\nn5=[n for n in e['nodes'] if n['id']==5][0]\ndev=[c for c in n5['consulted'] if c['src']=='DEV'][0]\ndev['note']=(\"no headword orchidee/orchis: the only occurrence of the word in Devic is inside the entry \"\n \"'Angrec. Genre de plantes tropicales de la famille des orchidees ... c'est en malais anggreq, orchis' \"\n \"(DEV.txt line 516), i.e. a Malay orchid name - Devic says nothing about orchidee itself, as expected for a Graeco-Latin coinage.\")\njson.dump(d,io.open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=2)\nio.open(p,'a',encoding='utf-8').write('\\n')\nprint('patched')\nEOF\npython3 -m json.tool data/verification/page-375.json >/dev/null && echo \"JSON OK\"\nmkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg375.png data/verification/sources/refs/ocr/BOOK/375.png && ls -la data/verification/sources/refs/ocr/BOOK/375.png\npython3 tools/verify_check.py 375",
 "description": "Patch JSON, copy page image, re-check"
}
```


### [2026-09-07T20:39:12.703Z] TOOL RESULT

```
patched
JSON OK
-rw-rw-r-- 1 sfmqrb sfmqrb 47783 Sep  7 16:39 data/verification/sources/refs/ocr/BOOK/375.png
nodes verified: 10/10
node verdicts: {'plausible': 2, 'confirmed': 7, 'unverified': 1}
root verdicts: {'plausible': 1, 'confirmed': 1}
ref checks: {'supports': 6, 'partial': 1, 'not_checked': 8, 'not_found': 1}
books consulted: {'supports': 21, 'silent': 8, 'partial': 2} | by book: {'SKT': 4, 'KLN': 3, 'MON': 2, 'ARY': 2, 'LAT': 2, 'WLD': 2, 'AHD': 2, 'FSD': 2, 'HRN': 1, 'ISS_alt_DKS': 1, 'HUB': 1, 'LEW': 1, 'WEB': 1, 'BRT': 1, 'KNT': 1, 'PHD': 1, 'NYB': 1, 'IEC': 1, 'SYN': 1, 'DEV': 1}
```


## [2026-09-07T20:39:32.727Z] AGENT

Page 375 done — `/home/sfmqrb/git/rishe/data/verification/page-375.json`, `verify_check.py 375` shows 0 PROBLEM lines (10/10 nodes).

**Counts** — roots: 1 confirmed (Orghi), 1 plausible (Opop). Nodes: 7 confirmed, 2 plausible, 1 unverified. Ref checks: 6 supports, 1 partial, 1 not_found, 8 not_checked.

**Flagged / notable**
- **Opop root + #1 pupu + #2 upŭpa → plausible, not confirmed.** Pokorny 325 (`epop-, opop-`) and WP I 123 do carry exactly Nourai's box (incl. "npers. pupū", "lat. upupa"), but they and every modern source (Horn no. 333 p. 74 "onomatopoetisch gebildet", Wiktionary, Etymonline, Ernout-Meillet "terme expressif, imitatif") treat the forms as parallel independent onomatopoeias, not descendants of one PIE word. Bailey (DKS s.v. papūskyā) supplies the Iranian family (Khot. papūskyā, Sogd. pwp'pyh, Chorasm. wpwpyk, NP pūpak/pūpū).
- **Citation error in the book (not extraction): `POK:424` on the Latin upŭpa box.** Pokorny p. 424 holds `ghegh-` "curve, bend" and `g(h)egh-` "ferret"; upupa is on p. 325. The page image confirms the book itself prints "POK:424" — status `not_found`, Nourai's misprint.
- **Blank box (entry Orghi, node #2) → unverified.** The printed page really does show an empty outlined box under the Avestan node (extraction faithful). Nothing could stand there by inheritance: MP has *gund* "testicle" / *xāyag* "egg" (MacKenzie, Nyberg), no reflex of *arəzi-*.
- **BQT:424 verified as `partial`**: BQT vol. 1 leaf 651 = printed p. 424 s.v. پوپو "شانه‌سر و هدهد … مرغ سلیمان است" with Mo'in's footnote "رک: پوپک" — confirms word and gloss, gives no etymology. `IRT:46` unavailable (purchase only). AHD:633/924 are main-dictionary pages (only Watkins' appendix is on disk) → `not_checked`, but the live AHD entries were archived and match.
- **Orghi chain fully confirmed**: BRT col. 351 `arəzay- m. 'Hodensack'`, dual `arəzi 'Hoden'`; Buck 4.49 p. 257 and Klein p. 1092 both as cited; Gk ὄρχις → L orchis → ModL Orchideae → F orchidée → NP ارکیده (Mo'in/Amid tag it فرانسوی) and → E orchid (1845, Lindley, false stem *orchid-*).

**No extraction errors to fix.** One cosmetic note only: the JSON's Persian script for node #6 is "اركیده" (Arabic kaf) where p. 345 prints "ارکیده" (Persian kaf) — font/character normalization, not a misread letter; recorded in the node's derivation. Page image archived at `data/verification/sources/refs/ocr/BOOK/375.png`; 12 web pages archived via `fetch_source.py`.
